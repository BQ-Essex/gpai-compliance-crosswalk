#!/usr/bin/env python3
"""Check and fix Markdown prose against Brad's house style.

Two of the checks are not about style at all. One flags a paragraph that repeats an
earlier one, which is what a revision pasted below its original looks like a day
later. The other flags a count written in prose that no longer matches the register
it describes, which is how "seven errors" outlived a table of nine.

Three of the conventions are mechanical and can be fixed outright: closed em
dashes, smart quotes, and range en dashes left alone. The fourth — signposting
that announces a point rather than making it — can only be flagged, because
deciding whether a phrase is doing work is a judgement no script should make.

Code spans, fenced blocks, URLs and YAML/Markdown table pipes are protected, since
the usual way this goes wrong is a smart quote landing inside a path or a build
string and surviving all the way to a cover page.

Usage:
    python3 tools/housestyle.py FILE...          # report only
    python3 tools/housestyle.py --fix FILE...    # rewrite in place

Exit codes:
    0  nothing to change, or everything fixed
    1  changes outstanding (report mode), or signposting flagged
"""

import sys
import re
from pathlib import Path

# Phrases that announce a point instead of making it. Flagged, never auto-removed:
# some of these are load-bearing in the right sentence, and the style note is that
# the frame usually goes while the sentence stays.
SIGNPOSTS = (
    "here is the part",
    "what I'd rather talk about",
    "what I would rather talk about",
    "I'll be straight",
    "I will be straight",
    "the thing is",
    "it's worth noting",
    "it is worth noting",
    "worth stating plainly",
    "it's important to note",
    "it is important to note",
    "let me be clear",
    "to be clear",
    "needless to say",
    "at the end of the day",
)

# Spans whose contents must survive untouched.
PROTECTED = re.compile(
    r"(```.*?```"          # fenced code
    r"|`[^`\n]*`"          # inline code
    r"|https?://\S+"       # bare URLs
    r"|\]\([^)]*\))",      # markdown link targets
    re.DOTALL,
)


def shelve_protected(text):
    """Replace protected spans with placeholders and return (text, originals).

    Returns the text with each protected span swapped for a sentinel that contains
    no character this script rewrites, plus the list needed to restore them.
    """
    stash = []

    def keep(match):
        stash.append(match.group(0))
        return f"\x00{len(stash) - 1}\x00"

    return PROTECTED.sub(keep, text), stash


def restore_protected(text, stash):
    """Put the protected spans back where their placeholders sit."""
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)


def close_the_dashes(text):
    """Convert spaced em dashes to closed ones, leaving range en dashes alone.

    New Hart's Rules and Brad both take the closed form; the spaced form is the
    journalistic convention. En dashes between digits are ranges and stay as they are.
    """
    return re.sub(r"\s+—\s+", "—", text)


def curl_the_quotes(text):
    """Convert straight quotes and apostrophes to their typographic forms.

    Apostrophes are handled before double quotes so that a possessive inside a
    quoted phrase doesn't confuse the open/close alternation.
    """
    # Apostrophes: between word characters (don't, provider's), or leading elision ('90s).
    text = re.sub(r"(?<=\w)'(?=\w)", "’", text)
    text = re.sub(r"(?<=\s)'(?=\d)", "’", text)

    # Possessive after a closing bracket or digit — "Article 91(4)'s own form".
    # Without this the alternation below reads the apostrophe as an opening quote,
    # which is the failure that survives into a rendered document unnoticed.
    text = re.sub(r"(?<=[)\]}0-9])'(?=s\b)", "’", text)

    # Single quotes used as quotation marks around a term: 'serious incident'
    text = re.sub(r"(?<![\w’])'(?=[^\s'])", "‘", text)
    text = re.sub(r"(?<=[^\s'])'(?![\w])", "’", text)

    # Double quotes, alternating open and close across the whole document.
    out, open_next = [], True
    for ch in text:
        if ch == '"':
            out.append("“" if open_next else "”")
            open_next = not open_next
        else:
            out.append(ch)
    return "".join(out)


def find_signposts(text):
    """Return a list of (line number, phrase) for every signposting phrase present."""
    found = []
    for number, line in enumerate(text.splitlines(), start=1):
        lowered = line.lower()
        for phrase in SIGNPOSTS:
            if phrase.lower() in lowered:
                found.append((number, phrase))
    return found


ECHO_MIN = 200      # characters; shorter blocks repeat legitimately
ECHO_PREFIX = 100   # characters of normalised opening that must coincide


def find_echoes(text):
    """Return (line number, opening) for paragraphs that repeat an earlier paragraph.

    Not a style rule but a drafting one, and it earned its place: a paragraph in the
    report was revised, the revision pasted below the original, and both survived the
    weekend. Exact repetition is the easy case; the one that actually happened shared
    an opening and diverged near the end, so the test is the opening.
    """
    seen = {}
    echoes = []
    line = 1
    for block in text.split("\n\n"):
        stripped = re.sub(r"[*`_>#|]", "", block)
        flat = re.sub(r"\s+", " ", stripped).strip().lower()
        if len(flat) >= ECHO_MIN:
            key = flat[:ECHO_PREFIX]
            if key in seen:
                echoes.append((line, seen[key], flat[:70]))
            else:
                seen[key] = line
        line += block.count("\n") + 2
    return echoes


_UNITS = ("one two three four five six seven eight nine ten eleven twelve thirteen "
          "fourteen fifteen sixteen seventeen eighteen nineteen").split()
NUMBERS = {w: i + 1 for i, w in enumerate(_UNITS)}
for _t, _base in (("twenty",20),("thirty",30),("forty",40),("fifty",50),("sixty",60),
                  ("seventy",70),("eighty",80),("ninety",90)):
    NUMBERS[_t] = _base
    for _i, _u in enumerate(_UNITS[:9]):
        NUMBERS[f"{_t}-{_u}"] = _base + _i + 1


def count_drift(text):
    """Does a stated count of corrections match the rows in the table below it?

    A number written in prose and a table it describes drift apart silently, and this
    one did: the log said seven while the table held nine, through two edits that each
    failed to update it. A count nobody checks is a claim nobody checks.

    Only the table immediately following the sentence is counted. The first version of
    this check counted every pipe-delimited row in the file and reported fifteen, which
    is the same class of mistake in a different costume.
    """
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines)
                  if re.match(r"^\w+ errors have been found", l)), None)
    if start is None:
        return None
    stated = NUMBERS.get(lines[start].split()[0].lower())
    if stated is None:
        return None
    rows, seen_table = 0, False
    for line in lines[start + 1:]:
        if line.startswith("|"):
            seen_table = True
            if not re.match(r"^\|\s*-{2,}", line) and not line.startswith("| Error"):
                rows += 1
        elif seen_table and not line.strip():
            break
    return None if rows == 0 or stated == rows else (stated, rows)


# A count of a register, written in prose, against the register itself. The corrections
# log drifted this way once and was made checkable; the statutory register then drifted
# the same way in a different file, which is the argument for generalising the check
# rather than patching the one place it had already bitten.
REGISTERS = (
    (r"\b([a-z]+(?:-[a-z]+)?|\d+) provisions of the Regulation\b",
     ("provisions.yaml", "provisions"), "provisions of the Regulation"),
    (r"\b([a-z]+(?:-[a-z]+)?|\d+) imported provisions of the CER Directive\b",
     ("provisions.yaml", "imported_provisions"), "imported CER provisions"),
    (r"\b([a-z]+(?:-[a-z]+)?|\d+) recitals behind this report\b",
     ("provisions.yaml", "recitals"), "recitals"),
    (r"\b([a-z]+(?:-[a-z]+)?|\d+) argumentative steps\b",
     ("inferences.yaml", "inferences"), "inferences"),
)


def register_drift(text, path=None, root=None):
    """Does a count written in prose still match the register it describes?

    Same failure as count_drift, one file over. A number is written once and the
    register grows underneath it, and nothing complains because prose is not data.
    Returns a list of (stated, actual, label).

    The corrections log is exempt, and the exemption is the point of the log: it records
    what was once believed, so every number in it is historical by construction. The first
    version of this check did not know that, and reported the log's own account of a past
    drift as a present one - which is the same class of mistake in a third costume.
    """
    root = Path(root or Path(__file__).resolve().parent.parent)
    if path is not None and Path(path).name == Path(CORRECTIONS_LOG).name:
        return []
    try:
        import yaml
    except ImportError:
        return []
    cache, found = {}, []
    for pattern, (filename, key), label in REGISTERS:
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        word = match.group(1).lower()
        stated = int(word) if word.isdigit() else NUMBERS.get(word)
        if stated is None:
            continue
        if filename not in cache:
            path = root / "data" / filename
            if not path.exists():
                return found
            cache[filename] = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        actual = len(cache[filename].get(key) or [])
        if actual and stated != actual:
            found.append((stated, actual, label))
    return found


# The count of errors in the corrections log is stated in one place and quoted in six
# others, across prose and tool docstrings. Fixing the log leaves the quotations behind,
# which is what happened: "nine errors" outlived a table of ten in five files at once.
# The canonical number is the table's own row count, not any sentence about it.
CORRECTIONS_LOG = "protocol/01-statutory-foundation.md"
CORRECTIONS_ECHOES = (
    (re.compile(r"\b(?:of|in)\s+the\s+([a-z]+(?:-[a-z]+)?)\s+(?:recorded\s+)?errors\b"), 1),
    (re.compile(r"\b([a-z]+(?:-[a-z]+)?)\s+errors\s+have\s+been\s+found\b"), 1),
    (re.compile(r"\b([a-z]+(?:-[a-z]+)?)\s+of\s+the\s+([a-z]+(?:-[a-z]+)?)\s+are\s+the\s+same\s+failure\b"), 2),
    (re.compile(r"analysis[’']s\s+([a-z]+(?:-[a-z]+)?)\s+errors\b"), 1),
)
SWEPT = ("*.md", "docs/*.md", "protocol/*.md", "instrument/*.md", "tools/*.py")


def corrections_total(root):
    """The row count of the corrections table, which is the only number that is data."""
    path = Path(root) / CORRECTIONS_LOG
    if not path.exists():
        return None
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next((i for i, l in enumerate(lines)
                  if re.search(r"errors have been found", l)), None)
    if start is None:
        return None
    rows, seen = 0, False
    for line in lines[start + 1:]:
        if line.startswith("|"):
            seen = True
            if not re.match(r"^\|\s*-{2,}", line) and not line.startswith("| Error"):
                rows += 1
        elif seen and not line.strip():
            break
    return rows or None


def corrections_sweep(root=None):
    """Every sentence anywhere that states how many errors the log holds, against the log.

    Returns a list of (path, line number, stated, actual). Runs over prose and over the
    tools' own docstrings, because four of the six stale counts were in docstrings and
    a checker that exempts itself is not a checker.
    """
    root = Path(root or Path(__file__).resolve().parent.parent)
    actual = corrections_total(root)
    if actual is None:
        return []
    found = []
    for glob in SWEPT:
        for path in sorted(root.glob(glob)):
            try:
                raw = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            # Numbers in code spans are quotations of a superseded figure, not claims.
            joined, _ = shelve_protected(raw)
            is_log = path.name == Path(CORRECTIONS_LOG).name
            for index, (pattern, group) in enumerate(CORRECTIONS_ECHOES):
                # In the log, the only sentence making a present claim is its header; the
                # rows quote superseded numbers on purpose.
                if is_log and index != 1:
                    continue
                for match in pattern.finditer(joined):
                    word = match.group(group).lower()
                    stated = int(word) if word.isdigit() else NUMBERS.get(word)
                    if stated is not None and stated != actual:
                        number = joined[:match.start()].count("\n") + 1
                        found.append((str(path.relative_to(root)), number, stated, actual))
    return found


def dangling_appendices(text):
    """An "Appendix F" cited in a report whose appendices stop at E.

    Cheap, and it had already happened: the forms appendix was written as its own file,
    cited from the body as Appendix F, and never bound into the report. A cross-reference
    is a claim that something exists, and this repository checks those.

    Only files that define appendices are checked, so prose elsewhere may cite the
    report's appendices freely.
    """
    order = re.findall(r"^#{2,3}\s+Appendix\s+([A-Z])\b", text, re.M)
    defined = set(order)
    if not defined:
        return []
    cited = set(re.findall(r"\bAppendix\s+([A-Z])\b", text))
    missing = sorted(f"{letter} is cited and not defined" for letter in cited - defined)
    # Out of order is not dangling, and a reader notices it just as fast. This file ran
    # A B C D E G F H for a day, because an appendix was inserted ahead of the one it
    # should follow and nothing looked at the sequence.
    if order != sorted(order):
        missing.append("the appendices run " + " ".join(order) + ", which is out of order")
    return missing


# A path written in prose is a claim that a file is there, and until now nothing checked
# it. Run by hand twice during the final sweep, it found three apparent breaks that were
# my own resolver not knowing that "its `docs/run-report.md`" means the run's own root -
# so the rule below tries every root a reader plausibly would, and only complains when
# none of them works.
PATH_IN_PROSE = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./-]*\.(?:md|py|yaml|yml|docx|cff|txt|png|svg))`")
LINK_IN_PROSE = re.compile(r"\[[^\]]*\]\(([^)#\s]+)\)")


def dangling_paths(text, path):
    """Every file a document points at, checked from each root a reader might use.

    Three roots are legitimate here: the repository root, the directory the document
    sits in, and - for anything under runs/ - that run's own root, because a second run
    is a repository in its own right and its prose is written from its own top. A path
    that resolves from none of them is a pointer to nothing.
    """
    root = Path(__file__).resolve().parent.parent
    here = Path(path).resolve().parent
    roots = [root, here]
    parts = Path(path).resolve().parts
    if "runs" in parts:                       # the run's own root, two levels in
        i = parts.index("runs")
        roots.append(Path(*parts[: i + 2]))
    found = []
    for pattern in (PATH_IN_PROSE, LINK_IN_PROSE):
        for match in pattern.finditer(text):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if any((base / target).exists() for base in roots):
                continue
            # A bare filename in prose - `check.py`, `cover-note.md` - is a name, not a
            # path, and resolves wherever it lives. Only complain about ones with a
            # directory in them, which are claims about location.
            if "/" not in target:
                continue
            found.append(target)
    return sorted(set(found))


def process(path, fix=False):
    """Apply the mechanical fixes to one file and report what changed or remains.

    Returns True if the file is clean (or was made clean), False if anything is
    outstanding.
    """
    with open(path, encoding="utf-8") as handle:
        original = handle.read()

    shelved, stash = shelve_protected(original)
    revised = curl_the_quotes(close_the_dashes(shelved))
    revised = restore_protected(revised, stash)

    spaced = len(re.findall(r"\s—\s", shelved))
    straight = shelved.count('"') + len(re.findall(r"(?<=\w)'(?=\w)", shelved))
    signposts = find_signposts(original)
    echoes = find_echoes(original)
    drift = count_drift(original)
    registers = register_drift(shelved, path)
    dangling = dangling_appendices(original)
    nowhere = dangling_paths(original, path)

    if fix and revised != original:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(revised)
        print(f"{path}: fixed {spaced} spaced dash(es), {straight} straight quote(s)")
    elif revised != original:
        print(f"{path}: {spaced} spaced dash(es) and {straight} straight quote(s) to fix "
              f"— rerun with --fix")
    else:
        print(f"{path}: dashes and quotes are already right")

    for number, phrase in signposts:
        print(f"  line {number}: signposting — “{phrase}”. "
              f"Usually the frame goes and the sentence stays.")

    if drift:
        print(f"  corrections log says {drift[0]} errors; the table has {drift[1]} rows. "
              f"A count written in prose drifts from the table it describes, silently, "
              f"and this one already has.")

    for stated, actual, label in registers:
        print(f"  prose says {stated} {label}; the register holds {actual}. "
              f"The corrections log drifted this way once and was made checkable. "
              f"This is the same failure one file over.")

    for target in nowhere:
        print(f"  points at {target}, which is not there from the repository root, from "
              f"this file's own directory, or from its run's root. A path in prose is a "
              f"claim that a file exists.")

    for complaint in dangling:
        print(f"  {complaint}. A cross-reference is a claim that something exists, and "
              f"an ordering is a claim a reader checks without meaning to.")

    for number, first, opening in echoes:
        print(f"  line {number}: repeats the paragraph at line {first} — “{opening}…”. "
              f"One of the two is a revision that was never deleted.")

    return ((revised == original or fix) and not signposts and not echoes
            and not drift and not registers and not dangling and not nowhere)


def main():
    """Run over every file named on the command line."""
    args = [a for a in sys.argv[1:] if a != "--fix"]
    fix = "--fix" in sys.argv

    # Every other tool here prints its docstring for --help or no arguments. This one
    # treated an unrecognised flag as a filename and handed a stranger a stack trace,
    # which is a poor first impression from the tool that checks the prose.
    if not args or {"--help", "-h"} & set(args):
        sys.exit(__doc__)
    unknown = [a for a in args if a.startswith("-")]
    if unknown:
        sys.exit(f"{__doc__}\nNot a flag this understands: {', '.join(unknown)}. "
                 f"It takes file paths, and --fix.")

    # Not a generator: every file should be reported on, not just those up to the
    # first failure.
    clean = all([process(path, fix=fix) for path in args])

    # Repo-wide, and run once rather than per file: the count being checked lives in one
    # table and is quoted everywhere else, so it is not a property of any single file.
    stale = corrections_sweep()
    for path, number, stated, actual in stale:
        print(f"{path}:{number}: says the corrections log holds {stated} errors; the "
              f"table holds {actual}. The log was updated and the sentences quoting it "
              f"were not, which is how this drifts every time.")

    sys.exit(0 if clean and not stale else 1)


if __name__ == "__main__":
    main()
