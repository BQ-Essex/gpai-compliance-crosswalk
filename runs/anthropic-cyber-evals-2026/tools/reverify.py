#!/usr/bin/env python3
"""Re-verify the statutory register against a consolidated text, or against itself.

`data/provisions.yaml` is the most reusable thing in this repository and the one that
goes stale silently: an amending regulation lands, the register keeps saying what the
Act said, and every citation still "resolves". This script is what makes it safe to
copy the register into the next incident.

Two modes.

    python3 tools/reverify.py --pdf path/to/consolidated.pdf
        Extracts the PDF's text layer and looks for every provision's `text` in it,
        fragment by fragment where the register elides with [...], comparing on the
        alphanumeric residue so that spacing, hyphenation, dashes, quotation marks and
        superscripts cannot produce a false miss. Reports every provision it cannot find.
        Recitals are checked only if the PDF is the authentic OJ text (the consolidated
        version omits them); pass --pdf twice to check both.

    python3 tools/reverify.py --pdf consolidated.pdf --stamp
        As above, and for every entry found, writes or refreshes its `verified` field
        with today's date and the file names, in place, touching nothing else.

    python3 tools/reverify.py --self
        No PDF. Checks that every entry has an id, a cite, a text and a `verified` date,
        that ids are unique, that `amended_by_omnibus` is a recognised value, and that
        the `meta` block names the consolidated CELEX and its date. This is what CI runs
        on a clean checkout, which holds no PDFs.

Exit codes: 0 everything found (or self-check clean); 1 otherwise.

Needs `pdftotext` (poppler) on the path, or falls back to pypdf if installed. What it
does not do: fetch anything. EUR-Lex was unreachable from the machine this was built
on for most of a day, and a re-verifier that quietly succeeds on a cached copy is worse
than one that asks you for the file.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PROVISIONS = ROOT / "data" / "provisions.yaml"
SECTIONS = ("provisions", "imported_provisions", "recitals")
# Anything in square brackets is the register's own voice - an elision, an editorial
# prefix such as "[paragraph 1, first sentence:]", a change marker "[▼M1]" - and never
# the Act's. It splits the text into fragments to be found separately.
ELISION = re.compile(r"\[[^\]]*\]|…")
MIN_FRAGMENT = 20  # alphanumeric characters; shorter fragments match by accident


def normalise(text: str) -> str:
    """Reduce text to what survives a PDF text layer: letters and digits, lower-cased.

    Spacing, hyphenation (hard, soft, or line-break), dashes, quotation marks, list
    punctuation and superscripts all vary between the register and a text layer without
    a word having changed. Comparing on the alphanumeric residue finds every changed,
    missing or added WORD and ignores everything that is not one. That is the right
    tolerance for a register that claims verbatim text, and it is deliberately blind to
    punctuation: a stray comma is not what this check is for.
    """
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def pdf_text(path: Path) -> str:
    if shutil.which("pdftotext"):
        out = subprocess.run(["pdftotext", "-layout", str(path), "-"],
                             capture_output=True, text=True, check=True)
        return out.stdout
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("need pdftotext on the path or pypdf installed")
    return "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages)


def fragments(text: str) -> list[str]:
    parts = [normalise(p) for p in ELISION.split(text)]
    return [p for p in parts if len(p) >= MIN_FRAGMENT]


def load():
    data = yaml.safe_load(PROVISIONS.read_text(encoding="utf-8")) or {}
    return data


def self_check(data) -> list[str]:
    findings = []
    meta = data.get("meta") or {}
    for key in ("consolidated_celex", "consolidation_date", "authentic_celex"):
        if not meta.get(key):
            findings.append(f"meta.{key} missing")
    seen = set()
    for section in SECTIONS + ("case_law",):
        for entry in data.get(section) or []:
            ident = entry.get("id")
            if not ident:
                findings.append(f"{section}: an entry with no id")
                continue
            if ident in seen:
                findings.append(f"{ident}: duplicate id")
            seen.add(ident)
            if not entry.get("cite"):
                findings.append(f"{ident}: no cite")
            body = entry.get("text") or entry.get("holding_relied_on")
            if not body:
                findings.append(f"{ident}: no text")
            if section != "case_law" and not entry.get("verified"):
                findings.append(f"{ident}: no `verified` date - was it read, or described?")
            flag = entry.get("amended_by_omnibus")
            if section == "provisions" and str(flag).lower() not in ("true", "false", "unverified", "partial"):
                findings.append(f"{ident}: amended_by_omnibus is {flag!r}, not a recognised value")
    return findings


# What a EUR-Lex text layer adds that the Act does not say: running page headers of the
# consolidated version ("02024R1689 — EN — 27.07.2026 — 001.001 — 61") and the change
# markers (▼B, ▼M1). Both land mid-sentence when a provision crosses a page.
FURNITURE = re.compile(r"^\s*0\d{4}[A-Z]\d{4}\s*—\s*[A-Z]{2}\s*—.*$|▼[A-Z]\d*", re.MULTILINE)


def against_pdf(data, pdfs: list[Path]) -> tuple[list[str], int]:
    corpus = normalise(FURNITURE.sub(" ", "\n".join(pdf_text(p) for p in pdfs)))
    findings, checked = [], 0
    for section in SECTIONS:
        for entry in data.get(section) or []:
            text = entry.get("text") or ""
            frags = fragments(text)
            if not frags:
                continue
            checked += 1
            missing = [f for f in frags if f not in corpus]
            if missing:
                findings.append(f"{entry['id']} ({entry.get('cite')}): "
                                f"{len(missing)} of {len(frags)} fragment(s) not found; first: "
                                f"\"{missing[0][:70]}…\" (alphanumeric residue)")
    return findings, checked


def stamp(found_ids: set[str], pdfs: list[Path]) -> int:
    """Write `verified:` for each found entry, editing the YAML as text so nothing else moves."""
    import datetime
    note = f"{datetime.date.today().isoformat()} by tools/reverify.py against {', '.join(p.name for p in pdfs)}"
    lines = PROVISIONS.read_text(encoding="utf-8").split("\n")
    out, current, done, written = [], None, set(), 0
    for line in lines:
        m = re.match(r"^(\s*)- id: (\S+)", line)
        if m:
            current = m.group(2)
        if current in found_ids and current not in done and re.match(r"^\s*verified:", line):
            indent = re.match(r"^(\s*)", line).group(1)
            line = f'{indent}verified: "{note}"'
            done.add(current); written += 1
        out.append(line)
        if current in found_ids and current not in done and re.match(r"^\s*cite:", line):
            # no verified field yet: add one after the cite line unless one follows later
            block_has = False
            out_index = len(out)
            # look ahead within the block
            rest = lines[lines.index(line) + 1:]
            for nxt in rest:
                if re.match(r"^\s*- id:", nxt) or re.match(r"^\S", nxt):
                    break
                if re.match(r"^\s*verified:", nxt):
                    block_has = True
                    break
            if not block_has:
                indent = re.match(r"^(\s*)", line).group(1)
                out.append(f'{indent}verified: "{note}"')
                done.add(current); written += 1
    PROVISIONS.write_text("\n".join(out), encoding="utf-8")
    return written


def main(argv: list[str]) -> int:
    data = load()
    if "--self" in argv:
        findings = self_check(data)
        total = sum(len(data.get(s) or []) for s in SECTIONS)
        if findings:
            print(f"{len(findings)} thing(s) wrong with the register's own shape:")
            for f in findings:
                print("  -", f)
            return 1
        print(f"register shape holds: {total} entries, every one with an id, a cite, a text "
              f"and a verified date; meta names {data['meta']['consolidated_celex']} "
              f"of {data['meta']['consolidation_date']}. This says nothing about whether the "
              f"text is still the Act's - for that, --pdf.")
        return 0
    pdfs = [Path(argv[i + 1]) for i, a in enumerate(argv) if a == "--pdf" and i + 1 < len(argv)]
    if not pdfs:
        print(__doc__)
        return 2
    for p in pdfs:
        if not p.exists():
            sys.exit(f"no such file: {p}")
    findings, checked = against_pdf(data, pdfs)
    if "--stamp" in argv:
        missing_ids = {f.split(" ")[0] for f in findings}
        found = {e["id"] for s in SECTIONS for e in (data.get(s) or [])
                 if fragments(e.get("text") or "") and e["id"] not in missing_ids}
        print(f"stamped {stamp(found, pdfs)} entries as verified today")
    if findings:
        print(f"{len(findings)} of {checked} entries not found in the supplied text:")
        for f in findings:
            print("  -", f)
        print("A miss can mean the text changed, the extract was never verbatim, or the "
              "PDF's text layer mangled the passage. Open the document before deciding which.")
        return 1
    print(f"all {checked} entries with checkable text found in {', '.join(p.name for p in pdfs)}. "
          f"Recitals are only in the authentic OJ text; entries elided to fragments shorter than "
          f"{MIN_FRAGMENT} characters were skipped.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
