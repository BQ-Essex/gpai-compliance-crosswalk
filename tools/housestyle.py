#!/usr/bin/env python3
"""Check and fix Markdown prose against Brad's house style.

A fifth check is not about style at all: a paragraph that repeats an earlier one,\nwhich is what a revision pasted below its original looks like a day later.\n\nThree of the conventions are mechanical and can be fixed outright: closed em
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

    for number, first, opening in echoes:
        print(f"  line {number}: repeats the paragraph at line {first} — “{opening}…”. "
              f"One of the two is a revision that was never deleted.")

    return (revised == original or fix) and not signposts and not echoes


def main():
    """Run over every file named on the command line."""
    args = [a for a in sys.argv[1:] if a != "--fix"]
    fix = "--fix" in sys.argv

    if not args:
        sys.exit(__doc__)

    # Not a generator: every file should be reported on, not just those up to the
    # first failure.
    clean = all([process(path, fix=fix) for path in args])
    sys.exit(0 if clean else 1)


if __name__ == "__main__":
    main()
