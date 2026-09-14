#!/usr/bin/env python3
"""Hold a web page as a source, and check that what the register claims to hold is there.

This is the one step of the method that was always done by hand: a page is archived,
printed to PDF, dropped in `_sources/`, hashed, and written into `data/sources.yaml`.
Fifteen times by hand over three days, which is fifteen chances to mistype a hash or
forget an entry, and `tools/validate.py` will refuse a fact whose source is not held —
so the step gates everything downstream and deserved a command.

    python3 tools/hold-source.py                 # what is here, what is registered, what is neither
    python3 tools/hold-source.py --verify        # every registered hash against the file it names
    python3 tools/hold-source.py --draft FILE    # a ready-to-paste sources.yaml entry for FILE
    python3 tools/hold-source.py --text          # extract text for any held PDF missing its cache

THE PROCEDURE THIS AUTOMATES THE SECOND HALF OF, written out because the first half is
still yours: open the page, archive it (web.archive.org/save), open the ARCHIVED copy,
print it to PDF, and save it into `_sources/`. Archive first and print the archived copy:
a page revised in place afterwards is a page your quotation no longer matches, and two
entries in the corrections log began exactly there.

Then run this, paste the drafted entry, and fill in `establishes:` — which is the only
part no tool can do, because it is the register characterising a document, and
characterising a document you have not opened is fourteen of this project's
twenty-eight errors.

Exit codes:
    0  every registered source is present and hashes as recorded
    1  something is registered and missing, changed, or present and unregistered
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "_sources"
CACHE = SOURCES / ".text-cache"
REGISTER = ROOT / "data" / "sources.yaml"

# A source may name one document or several; both shapes are in use and both are read.
def documents_of(entry) -> list[tuple[str, str]]:
    """Every (filename, sha256) pair an entry claims, from either shape it may take."""
    pairs = []
    if entry.get("document") and entry.get("sha256"):
        pairs.append((entry["document"], entry["sha256"]))
    for d in entry.get("documents") or []:
        if isinstance(d, dict) and d.get("file") and d.get("sha256"):
            pairs.append((d["file"], d["sha256"]))
    # A source may hold the same document in two renditions - the Commission publishes
    # its incident template as DOCX and as PDF, and both were read. The second one hides
    # under its own key, and was invisible to this check until it wasn't.
    second = entry.get("second_rendition")
    if isinstance(second, dict) and second.get("document") and second.get("sha256"):
        pairs.append((second["document"], second["sha256"]))
    return pairs


def digest(path: Path) -> str:
    """SHA-256 of a file, read in chunks so a large PDF does not land in memory whole."""
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def held_elsewhere() -> set[str]:
    """Files legitimately in _sources/ that sources.yaml does not register, and should not.

    The statutory texts belong to data/provisions.yaml, which names them in its `verified:`
    lines rather than carrying its own hashes; the folder's own README is a note to whoever
    opens it. Neither is a source in the tiered sense, and flagging them would train a
    reader to ignore this check - which is how a checker stops being run.
    """
    names = {"README.txt"}
    text = (ROOT / "data" / "provisions.yaml").read_text(encoding="utf-8")
    for path in SOURCES.glob("*"):
        if path.is_file() and path.name in text:
            names.add(path.name)
    return names


def registered() -> dict[str, tuple[str, str]]:
    """Filename -> (source id, recorded hash), for everything the register says it holds."""
    data = yaml.safe_load(REGISTER.read_text(encoding="utf-8")) or {}
    held = {}
    for entry in data.get("sources", []) or []:
        for name, sha in documents_of(entry):
            held[name] = (entry.get("id", "<unnamed>"), sha)
    return held


def on_disk() -> list[Path]:
    """Every document actually sitting in _sources/, in the order a person would see them."""
    return sorted(p for p in SOURCES.glob("*") if p.is_file()
                  and p.suffix.lower() in {".pdf", ".docx", ".html", ".txt"})


def verify(held, files) -> list[str]:
    """Compare what the register claims against what is here. Returns complaints.

    Three things can be wrong and they are not the same thing. A registered document can
    be absent, which means a reader cannot check the citation. It can be present and
    hash differently, which means the document changed under a claim made about it — the
    worst of the three and the reason hashes are recorded at all. Or a document can be
    here and unregistered, which is untidy rather than wrong, and is how a source ends
    up quoted before anyone has written down where it came from.
    """
    complaints = []
    names = {p.name for p in files}
    for name, (sid, sha) in sorted(held.items()):
        path = SOURCES / name
        if not path.exists():
            complaints.append(
                f"[{sid}] names {name!r}, which is not in _sources/. Either it was never "
                f"held or it has moved; the register is the thing a reader trusts, so it "
                f"should say which.")
            continue
        actual = digest(path)
        if actual != sha:
            complaints.append(
                f"[{sid}] {name!r} hashes to {actual[:16]}… and the register records "
                f"{sha[:16]}…. THE DOCUMENT CHANGED UNDER A CLAIM MADE ABOUT IT. Re-read "
                f"it before touching the hash: the quotation that cited it may no longer "
                f"be in it.")
    exempt = held_elsewhere()
    for name in sorted(names - set(held) - exempt):
        if name.startswith("."):
            continue
        complaints.append(
            f"{name!r} is in _sources/ and in no register entry. Nothing is wrong with "
            f"the file; it is simply not citable yet. `--draft` will start the entry.")
    return complaints


def draft(path: Path) -> str:
    """A register entry with everything a tool can know filled in, and nothing it cannot."""
    return f"""
  - id: CHANGE-ME
    tier: T?                      # T1 the party whose conduct is in question · T2 the
                                  # affected party's forensics · T3 an investigator under
                                  # the subject's constraints · T4 independent
    date: "YYYY-MM-DD"            # the date the DOCUMENT bears, not the date you read it
    retrieved: "{Path(__file__).stat() and __import__('datetime').date.today().isoformat()}"
    title: ""
    url: ""                       # the live page
    archived_url: ""              # the capture you printed from; required at T1-T3
    document: "{path.name}"
    sha256: "{digest(path)}"
    held_from: "{__import__('datetime').date.today().isoformat()}"
    establishes:
      - >-
        WHAT THIS DOCUMENT SAYS, in its own words where it matters. This is the only line
        here no tool can write, and validate.py will refuse the entry if the document is
        not held - because the register characterising a document nobody opened is the
        failure this project has made fourteen times.
"""


def extract_text(files, held) -> list[str]:
    """Cache the text layer of every held PDF that has none, so quotecheck can read it."""
    if not CACHE.exists():
        CACHE.mkdir(parents=True)
    done = []
    for path in files:
        if path.name not in held or path.suffix.lower() != ".pdf":
            continue
        target = CACHE / (path.stem + ".txt")
        if target.exists():
            continue
        try:
            subprocess.run(["pdftotext", "-layout", str(path), str(target)], check=True)
            done.append(target.name)
        except (FileNotFoundError, subprocess.CalledProcessError):
            print(f"  could not extract {path.name} — pdftotext is not on the path, or "
                  f"the file has no text layer. quotecheck will report it as not held.")
    return done


def main(argv) -> int:
    if not SOURCES.exists() or not on_disk():
        print("No documents held here, so nothing could be checked. That is the expected "
              "state of a fresh clone: _sources/ is gitignored by design, because the "
              "documents are cited by URL and SHA-256 rather than redistributed.\n"
              "Exit 2 rather than 1 — NOTHING WAS CHECKED is not SOMETHING FAILED, and a "
              "runner that cannot tell them apart teaches people to ignore the red one.\n"
              "data/sources.yaml lists every URL and hash; hold them and run this again.")
        return 2

    held, files = registered(), on_disk()

    if "--draft" in argv:
        try:
            name = argv[argv.index("--draft") + 1]
        except IndexError:
            print("--draft takes the name of a file in _sources/.")
            return 1
        path = SOURCES / Path(name).name
        if not path.exists():
            print(f"{path.name!r} is not in _sources/ yet. Print the archived page to PDF "
                  f"and save it there first.")
            return 1
        print(draft(path))
        return 0

    if "--text" in argv:
        done = extract_text(files, held)
        print(f"extracted {len(done)} text cache(s)" if done
              else "every held PDF already has its text cached")
        return 0

    complaints = verify(held, files)
    # Two kinds, and only one is a failure. A document that is missing or has changed
    # breaks a citation somebody may already have relied on. A document sitting here
    # unregistered breaks nothing - it is a file waiting for an entry, and failing the
    # build over it would teach a reader to skip the output.
    broken = [c for c in complaints if "in _sources/ and in no register entry" not in c]
    untidy = [c for c in complaints if c not in broken]
    print(f"{len(held)} document(s) registered · {len(files)} in _sources/\n")
    for c in broken:
        print(f"  - {c}\n")
    for c in untidy:
        print(f"  · {c}\n")
    if broken:
        return 1
    print(("Nothing registered is missing or changed. " if untidy else "") +
          "Every registered document is present and hashes as the register records. Which "
          "says the documents have not changed under the claims made about them, and "
          "nothing about whether those claims are right.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
