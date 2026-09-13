#!/usr/bin/env python3
"""Check that every statutory citation in the prose resolves to verified text.

`validate.py` polices the cross-walk rows. Nothing policed the prose — and the prose
is where the argument is actually made. A report can cite Article 2(1)(a) as the hinge
of its scope analysis while `data/provisions.yaml` has never held that provision's
text, and no tool in this repository would have noticed.

This one notices. It extracts every Article and Recital citation from the Markdown,
canonicalises it, and reports any citation the register cannot back. It also reports
register entries that nothing cites, which is how dead weight is found.

What it does not do, and cannot: check that the citation is apposite. A pinpoint that
resolves to verified text can still be the wrong provision for the proposition. This
tool removes one failure mode, and the removal should not be mistaken for the other.

Two classes of citation are deliberately not checked, and both exclusions are
substantive rather than convenient.

Citations qualified by another instrument — the Charter, the TFEU, the Californian and
New York statutes in the comparative section — are skipped, since the register does not
hold them. The qualifier is looked for in a short window immediately around the
citation, not in the surrounding sentence, so that one foreign citation does not silence
an Act citation later in the same line.

One instrument is an exception, and it earned it. The CER Directive is imported by the
Act's own definition of 'critical infrastructure', and relying on an imported definition
is still relying on text: two of the sixteen errors this analysis has recorded came from
reading a summary of that Directive rather than the Directive. So `imported_provisions`
in the register holds the CER text, citations qualified 'CER' resolve against it, and
prose that cites the Directive without saying so is reported rather than waved through.

Bare-number spans — 'Articles 51 to 56', 'Articles 102–110' — are skipped entirely. A
span names a body of provisions rather than a piece of text: the claim that Chapter V
runs from Article 51 to Article 56 rests on the text of Article 113, which is verified,
and not on the text of Article 56, which nothing here quotes. A span whose first member
carries a pinpoint ('Articles 2(1)(a)–(c)') is not a bare-number span, and its anchor is
checked as usual.

Usage:
    python3 tools/citecheck.py                 # check the prose, print findings
    python3 tools/citecheck.py --quiet         # exit code only, for CI
    python3 tools/citecheck.py --unused        # also list uncited register entries
    python3 tools/citecheck.py FILE...         # restrict to named files

Exit codes:
    0  every citation resolves
    1  at least one citation has no verified text behind it
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PROVISIONS = ROOT / "data" / "provisions.yaml"

DEFAULT_GLOBS = ("README.md", "docs/*.md", "protocol/*.md", "instrument/*.md")

# Another instrument is in play. Looked for immediately before the keyword and
# immediately after the citation, tightly, so that one foreign citation does not
# silence every Act citation sharing its line.
FOREIGN_BEFORE = 14
FOREIGN_AFTER = 44
# Qualifiers naming an instrument the register DOES hold. These resolve rather than
# skip: the key gains the instrument as its first element.
INSTRUMENT_QUALIFIERS = {"cer ": "cer", "cer]": "cer"}

FOREIGN_MARKERS = (
    "directive",
    "2022/2557",
    "2016/679",
    "2016/943",
    "2019/1020",
    "2022/2555",
    "910/2014",
    "tfeu",
    "charter",
    "treaty",
    "sb 53",
    "raise act",
    "health and safety code",
    "nis 2",
    "nis2",
)

ART_KEYWORD = re.compile(r"\bArt(?:icles|icle|s)?\.?\s+", re.IGNORECASE)
REC_KEYWORD = re.compile(r"\bRecitals?\s+", re.IGNORECASE)
# "55(1)(c)", "3, point (63)", "55(1), point (c)", "75(1a)"
ART_BODY = re.compile(r"(\d+)((?:\s*,?\s*(?:point\s*)?\(\s*[0-9a-z]+\s*\))*)")
SUBREF = re.compile(r"\(\s*([0-9a-z]+)\s*\)")
LIST_LINK = re.compile(r"\s*(?:,|and|or|&)\s*(?=\d)", re.IGNORECASE)
SPAN_LINK = re.compile(r"\s*(?:to|–|—|-)\s*(?=\d)", re.IGNORECASE)


def canonical(number: str, tail: str) -> tuple:
    """('55', '(1)(c)') -> ('art', '55', '1', 'c')."""
    return ("art", number, *SUBREF.findall(tail))


def strip_markup(text: str) -> str:
    """Remove emphasis markers so 'Article **55(1)**' parses like the plain form."""
    return text.replace("**", "").replace("*", "").replace("`", "")


def classify(line: str, keyword_start: int, citation_end: int):
    """Return ("act", None), ("instrument", key) or ("foreign", None).

    An instrument qualifier is looked for only immediately before the keyword, because
    that is where a writer puts it. A foreign marker is looked for on both sides, since
    'Article 5 of Directive (EU) 2016/943' qualifies itself afterwards.
    """
    before = line[max(0, keyword_start - FOREIGN_BEFORE) : keyword_start].lower()
    after = line[citation_end : citation_end + FOREIGN_AFTER].lower()
    for marker, key in INSTRUMENT_QUALIFIERS.items():
        if marker in before:
            return "instrument", key
    if any(m in before or m in after for m in FOREIGN_MARKERS):
        return "foreign", None
    return "act", None


def citations_in_line(line: str):
    """Yield canonical keys and the text that produced them."""
    line = strip_markup(line)

    for kw in ART_KEYWORD.finditer(line):
        pos = kw.end()
        pending = []
        spanned = False
        while True:
            body = ART_BODY.match(line, pos)
            if not body or not body.group(1):
                break
            kind, instrument = classify(line, kw.start(), body.end())
            key = canonical(body.group(1), body.group(2))
            if kind == "instrument":
                key = (instrument,) + key[1:]
            if kind != "foreign":
                pending.append((key, body.group(0).strip()))
            pos = body.end()

            span = SPAN_LINK.match(line, pos)
            if span:
                # A span of bare article numbers names a body of provisions, not text.
                if len(key) == 2:
                    spanned = True
                pos = span.end()
                continue
            link = LIST_LINK.match(line, pos)
            if not link:
                break
            pos = link.end()

        for key, shown in pending:
            if spanned and len(key) == 2:
                continue
            yield key, shown

    for kw in REC_KEYWORD.finditer(line):
        pos = kw.end()
        while True:
            body = re.match(r"(\d+)", line[pos:])
            if not body:
                break
            if classify(line, kw.start(), pos + body.end())[0] == "act":
                yield ("rec", body.group(1)), f"Recital {body.group(1)}"
            pos += body.end()
            link = LIST_LINK.match(line, pos) or SPAN_LINK.match(line, pos)
            if not link:
                break
            pos = link.end()


def register_keys() -> dict:
    data = yaml.safe_load(PROVISIONS.read_text(encoding="utf-8"))
    keys = {}
    for entry in data.get("provisions", []):
        cite = strip_markup(entry.get("cite", ""))
        body = ART_BODY.search(cite)
        if body:
            keys[canonical(body.group(1), body.group(2))] = entry["id"]
    for entry in data.get("recitals", []):
        number = re.search(r"(\d+)", entry.get("cite", ""))
        if number:
            keys[("rec", number.group(1))] = entry["id"]
    for entry in data.get("imported_provisions", []):
        instrument = entry.get("instrument", "").lower()
        cite = strip_markup(entry.get("cite", ""))
        # Only article-form citations are addressable. An Annex entry is held in the
        # register and cited in prose by name, but there is no pinpoint grammar here
        # that would resolve it, and pretending otherwise would put "CER Annex,
        # sector 8" in the same key space as "CER Article 8".
        if not ART_KEYWORD.search(cite):
            continue
        body = ART_BODY.search(cite)
        if instrument and body:
            keys[(instrument,) + canonical(body.group(1), body.group(2))[1:]] = entry["id"]
    return keys


def resolves(key: tuple, keys: dict):
    """A prose citation is backed if the register holds it, a broader form of it, or a
    narrower form of it. 'Article 55' is backed by verified text for 55(1)(c); a
    citation of 55(1)(c) is backed by verified text for the whole of Article 55."""
    if key in keys:
        return keys[key]
    for candidate, ident in keys.items():
        if candidate[: len(key)] == key or key[: len(candidate)] == candidate:
            return ident
    return None


def gather(paths):
    found = {}
    for path in paths:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for key, shown in citations_in_line(line):
                record = found.setdefault(key, {"shown": shown, "sites": []})
                record["sites"].append(f"{path.relative_to(ROOT)}:{number}")
    return found


def main(argv):
    quiet = "--quiet" in argv
    show_unused = "--unused" in argv
    named = [Path(a) for a in argv if not a.startswith("-")]

    if named:
        paths = [p if p.is_absolute() else ROOT / p for p in named]
    else:
        paths = sorted({p for glob in DEFAULT_GLOBS for p in ROOT.glob(glob)})

    keys = register_keys()
    found = gather(paths)

    unbacked = {k: v for k, v in found.items() if not resolves(k, keys)}
    cited = {resolves(k, keys) for k in found} - {None}
    unused = {ident for ident in keys.values()} - cited

    if not quiet:
        if unbacked:
            print(f"{len(unbacked)} citation(s) with no verified text behind them:\n")
            for key in sorted(unbacked, key=lambda k: (k[0], int(k[1]), k[2:])):
                record = unbacked[key]
                sites = record["sites"]
                where = ", ".join(sites[:4]) + (" …" if len(sites) > 4 else "")
                if key[0] == "art":
                    prefix = "Article "
                elif key[0] == "rec":
                    prefix = ""
                else:
                    prefix = f"{key[0].upper()} Article "
                print(f"  {prefix}{record['shown']}  ({len(sites)}×)  {where}")
            print(
                "\nEach of these is doing work in the prose on text nobody has verified.\n"
                "Add the provision to data/provisions.yaml, or stop relying on it."
            )
        else:
            print(
                f"Every statutory citation in {len(paths)} file(s) resolves to verified "
                f"text. {len(found)} distinct citation(s) checked."
            )

        if show_unused and unused:
            print(f"\n{len(unused)} register entry/entries nothing cites:")
            for ident in sorted(unused):
                print(f"  {ident}")

    return 1 if unbacked else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
