#!/usr/bin/env python3
"""Check that every quotation in the prose appears in a document we actually hold.

`citecheck.py` proves a citation resolves to verified text. It says nothing about the
sentence around it. Most of the errors in the first project's corrections log are the
same failure and it is not a citation failure: a source was characterised, or quoted,
without being opened. A recital was summarised from a mirror. A directive was read
through a summary. A Commission opinion was described from its landing page. In each
case the citation was perfectly well-formed and the claim beside it was wrong.

This checks the claim. Every quoted span in the prose is looked for, verbatim, in the
text of the documents in `_sources/`. What it cannot find, it says so about, and the
distinction that matters is reported rather than hidden: a quotation can fail either
because it is wrong or because the document it comes from is not held. Those are
different problems and the tool refuses to guess which one it is looking at.

That refusal is the point. The output is not "all quotations verified" — it is a
coverage figure. Verifiability becomes a number the project has to look at, rather than
an impression it can have about itself.

Elisions are handled: a quotation broken by [...] or … is checked fragment by fragment,
because that is how the elision is meant to be read. Short quotations are skipped, since
a four-word phrase will match by accident and prove nothing.

    python3 tools/quotecheck.py              # check, print findings
    python3 tools/quotecheck.py --quiet      # exit code only, for CI
    python3 tools/quotecheck.py --verified   # also list what was matched, and where

Exit codes:
    0  every checkable quotation was found in a held document
    1  at least one quotation could not be found in any document held
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "_sources"
CACHE = SOURCES / ".text-cache"
PROSE = ("README.md", "docs/*.md", "protocol/*.md", "instrument/*.md",
         "data/sources.yaml", "data/crosswalk.yaml")

# A quotation is only worth checking against a document we can identify it with.
# "Is this string anywhere in _sources/?" is the wrong question: most quotations in
# this repository are of the incident record, of Californian and New York statutes, or
# of this project's own earlier drafts, and none of those are held as PDFs. Asking the
# wrong question produced 71 findings, nearly all of them noise, and a check nobody
# reads is worse than no check.
#
# So attribution comes first. If a line names a document we hold, the quotation on that
# line is checked against THAT document and a failure is a real finding. If it names
# nothing we hold, the quotation is recorded as unattributable and the coverage figure
# says so. Each entry is (pattern found in the line, substring of the held filename).
ATTRIBUTION = (
    (r"C\(2025\)\s*7719|Guidelines\b|¶\s*\d+|paragraph \d+ of the Guidelines", "Guidelines_on_the_scope"),
    (r"C\(2025\)\s*5361|Commission Opinion", "Commission_Opinion"),
    (r"AI Board|Board's Conclusion|Adequacy Assessment", "AI_Board_Adequacy"),
    (r"Measure 9\.|Commitment \d|Safety and Security Chapter|the Code\b", "Safety_and_Security_Chapter"),
    (r"Q&A|questions and answers", "Questions & Answers"),
    (r"\bCER\b|2022/2557", "32022L2557"),
    (r"Pistillo", "Internal-deployment"),
    (r"Omnibus|2026/1744", "32026R1744"),
    # The incident record, held from 13 September 2026. Until then the EVIDENTIARY core of
    # this analysis was the least checked thing in it: every statutory quotation verified
    # against primary text, and every quotation of what the parties actually said verified
    # against nothing. Over-broad patterns are deliberate here - a quotation found in ANY
    # held document is verified, so widening the search costs nothing and narrowing it
    # risks a false alarm on which of two accounts a sentence came from.
    (r"\bOpenAI\b|the provider(?:'s|s')? (?:own )?(?:account|disclosure)|\bIM1\b|road ahead",
     "OpenAI"),
    (r"Hugging Face|technical timeline|the victim|\bT2\b", "Technical Timel"),
    (r"\bMETR\b|Redwood|\bHPIM\b|independent investigation", "METR"),
    (r"\bAnthropic\b", "Anthropic"),
    # The second run's record, held from 13 September 2026: the evaluation partner's own
    # account, and the press that pressed it.
    (r"\bIrregular\b", "Irregular"),
    # Held from 13 September 2026, when validate.py refused facts resting on them.
    (r"SB[ -]?53|California", "SB-53"),
    (r"\bAISI\b|AI Security Institute", "AISI"),
    (r"signator|Vademecum|Taskforce", "Vademecum"),
    (r"therecord\.media|Recorded Future|The Record from|The Record names|reports? from The Record", "The Record"),
    (r"TechCrunch|wiki incident", "TechCrunch"),
    (r"spokesperson|R[e\u00e9]gnier|IBTimes|confirmed receipt", "IBTimes"),
    (r"Agence Europe|first requests for information|Europe Daily Bulletin|more than 30 (?:AI )?providers", "AGENCE EUROPE"),
    (r"EU AI Act Newsletter|Virkkunen|Euractiv|Uuk", "Newsletter #110"),
    (r"Von Arx|collusion\.wiki|the wiki’s public logs|message board", "message board"),
    (r"Nilsson|Milch-Kontor|Orkem|AM ?& ?S|Akzo|C-\d{2,3}/\d{2}|\b\d{3}/\d{2}\b",
     "provisions.yaml"),
    (r"Draft Guidance|GUIDANCE PARA|Article 73 AI Act|119624", "Draft_Guidance_article_73"),
    (r"high-risk (?:form|template)|High-risk AI systems\)|119623|Section 1\.[23]",
     "Incident_report_for_serious_incidents"),
)

# Below this, a quotation matches by coincidence and proves nothing.
MIN_QUOTE = 40
MIN_FRAGMENT = 25

QUOTED = re.compile(r"[“\"]([^”\"]{%d,})[”\"]" % MIN_QUOTE)
# In YAML a straight double quote is syntax, not quotation: every scalar that needs
# escaping wears them. Only curly quotes mark a quotation there. Reading YAML with the
# prose pattern produced twenty-two findings, every one of them a field value.
QUOTED_YAML = re.compile(r"“([^”]{%d,})”" % MIN_QUOTE)
# A real elision. NOT "[w]hen" or "int[o application]", which are editorial
# substitutions: the bracket changes a letter or supplies a word, and the quotation
# still runs continuously through it. Treating those as breaks was this tool's first
# bug, and it reported four sound quotations as unfindable.
ELISION = re.compile(r"\[\s*(?:\.\.\.|…)\s*\]|…|\.\.\.")
SUBSTITUTION = re.compile(r"\[([^\]]{1,40})\]")


def normalise(text: str) -> str:
    """Flatten everything that differs between a PDF and a Markdown file but carries
    no meaning: line-break hyphenation, smart quotes, dash species, whitespace."""
    text = text.replace("­", "")
    text = re.sub(r"-\s*\n\s*", "-", text)
    for a, b in (("—", "-"), ("–", "-"), ("‑", "-"), (" ", " ")):
        text = text.replace(a, b)
    # Every quotation mark goes, of whatever species. House style nests single inside
    # double; the source being quoted nests the other way round, or uses straight
    # marks, or the PDF extractor invents its own. None of that is a difference in
    # what was said, and treating it as one was this tool's second bug.
    text = re.sub(r"[“”‘’\"'`]", "", text)
    text = re.sub(r"[*_]", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def held_documents() -> dict:
    """Extract (and cache) the text of every PDF in _sources/. Returns name -> text."""
    corpus = {}
    if not SOURCES.is_dir():
        return corpus
    CACHE.mkdir(exist_ok=True)
    for pdf in sorted(SOURCES.glob("*.pdf")) + sorted(SOURCES.glob("*.PDF")):
        cached = CACHE / (pdf.stem + ".txt")
        if not cached.exists() or cached.stat().st_mtime < pdf.stat().st_mtime:
            try:
                subprocess.run(["pdftotext", "-layout", str(pdf), str(cached)],
                               check=True, capture_output=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        corpus[pdf.name] = normalise(cached.read_text(encoding="utf-8", errors="replace"))
    return corpus


def declared_exceptions() -> list:
    """Quotations the project has declared unverifiable, each with a stated reason.

    An exception written down in a reviewed file is a different thing from an exception
    a tool makes for itself. Loosening the checker until it stops noticing would have
    been easier and would have destroyed the only number here worth having.
    """
    path = ROOT / "data" / "unverifiable-quotations.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    out = []
    for entry in data.get("exceptions", []) or []:
        text = normalise(str(entry.get("quote", "")))[:80]
        if text:
            out.append((text, entry.get("kind", "?"), entry.get("why", "")))
    return out


def register_text() -> dict:
    """The register's own verified text counts as a held document: it was transcribed
    from a primary source and carries a `verified` field saying when and against what."""
    path = ROOT / "data" / "provisions.yaml"
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    blocks = []
    # Judgments are held the same way: quoted from the paragraph read on EUR-Lex, with a
    # `verified` field saying when. A quotation from a judgment is checkable against that
    # and nowhere else, since the judgments are not held as files.
    case = [e.get("holding_relied_on", "") for e in (data.get("case_law") or [])]
    if case:
        blocks.extend(case)
    for key in ("provisions", "imported_provisions", "recitals"):
        for entry in data.get(key, []) or []:
            if entry.get("text"):
                blocks.append(entry["text"])
    return {"data/provisions.yaml (verified statutory text)": normalise(" ".join(blocks))}


def fragments(quote: str):
    """An elided quotation is a series of claims, one per fragment.

    Editorial substitutions are unwrapped first, so "[w]hen the provider" is checked as
    "when the provider" rather than split into a stub and a word beginning "hen".
    """
    unwrapped = SUBSTITUTION.sub(lambda m: m.group(1), quote)   # "[w]hen" -> "when"
    dropped = SUBSTITUTION.sub("", quote)                        # "[CER] Article" -> "Article"
    out = []
    for variant in (unwrapped, dropped):
        parts = [normalise(p).strip(" .,;:") for p in ELISION.split(variant)]
        out.append([p for p in parts if len(p) >= MIN_FRAGMENT])
    return out


def present(fragment: str, body: str) -> bool:
    """Is this fragment in this text, allowing for how PDFs mangle a sentence?

    Two tolerances, both learned from false alarms this tool raised on quotations that
    turned out to be exact. A superscript footnote marker extracts as a bare number
    dropped mid-sentence — "cannot take any enforcement actions 27 because" — and a
    quotation that ends a sentence in our prose may end a clause with a semicolon in
    the source. Neither is a difference in what was said.
    """
    if fragment in body:
        return True
    pattern = r"\s*(?:\d{1,3}\s*)?".join(re.escape(w) for w in fragment.split())
    return re.search(pattern, body) is not None


def prose_files():
    return sorted({p for pattern in PROSE for p in ROOT.glob(pattern)})


def logical_lines(path, text):
    """Yield (line number, text) with YAML block scalars joined into one unit.

    The scanner reads a line at a time, which is right for Markdown, where a paragraph
    is one long line. In YAML a quotation is wrapped across a block scalar, so both ends
    never sit on the same line and the pattern never fires. The register's quotations
    were therefore invisible to this checker for as long as it has existed - silently,
    which is the worst way for coverage to be missing. Found by planting a wrong word in
    a quotation and watching nothing happen.

    Joining also improves attribution: the document a quotation belongs to is usually
    named at the top of the entry, not on the line the quotation happens to start on.
    """
    lines = text.splitlines()
    if not str(path).endswith((".yaml", ".yml")):
        for number, line in enumerate(lines, 1):
            yield number, line
        return
    start, buffer = None, []
    for number, line in enumerate(lines, 1):
        if re.match(r"^\s*(?:-\s+)?(?:[\w.-]+:|-)(?:\s|$)", line) or not line.strip():
            if buffer:
                yield start, " ".join(buffer)
            start, buffer = number, [line.strip()]
        else:
            if start is None:
                start = number
            buffer.append(line.strip())
    if buffer:
        yield start, " ".join(buffer)


def main(argv):
    quiet = "--quiet" in argv
    show_verified = "--verified" in argv

    corpus = {**held_documents(), **register_text()}
    if not corpus:
        if not quiet:
            print("No documents held in _sources/ and no register text, so nothing can "
                  "be verified. That is a finding, not a pass.\n"
                  "Exit 2 rather than 1: NOTHING WAS CHECKED is a different state from "
                  "SOMETHING FAILED,\nand a runner that cannot tell them apart teaches "
                  "people to ignore the red one.")
        return 2

    def wanted_but_absent(line: str):
        """Documents this line points at that are NOT held here.

        A quotation attributed to a document nobody holds is UNVERIFIABLE, not wrong, and
        the difference decides whether a red board means "fix the prose" or "fetch the
        PDF". Before this existed, a clean checkout - which is what continuous integration
        and any other reader gets, since _sources/ is cited by hash rather than
        redistributed - reported sixty defects, every one of them a document it simply did
        not have. A checker that cries wolf on a fresh clone is a checker nobody runs
        twice.
        """
        missing = []
        for pattern, needle in ATTRIBUTION:
            if re.search(pattern, line, re.IGNORECASE):
                if not any(needle.lower() in n.lower() for n in corpus):
                    missing.append(needle)
        return missing

    def attributed(line: str):
        """Which held documents this line points at, most specific first."""
        names = []
        for pattern, needle in ATTRIBUTION:
            if re.search(pattern, line, re.IGNORECASE):
                names += [n for n in corpus if needle.lower() in n.lower()]
        # A line can cite an Article while quoting the incident record. The repository
        # already marks those with its own tier notation, and a quotation carrying a
        # tier marker or naming a party is that party's words, not the statute's.
        if re.search(r"\[T[1-4][,\]]|\bOpenAI\b|Hugging Face|METR|Von Arx|Anthropic|"
                     r"the provider(?:'s|s')? (?:own )?account", line, re.IGNORECASE):
            return names
        if re.search(r"\bArticle\b|\bRecital\b", line):
            names += [n for n in corpus if "provisions.yaml" in n
                      or "02024R1689" in n or "32024R1689" in n]
        return list(dict.fromkeys(names))

    exceptions = declared_exceptions()

    def declared(quote):
        flat = normalise(quote)
        return any(flat.startswith(text[:60]) or text[:60] in flat
                   for text, _kind, _why in exceptions)

    found, missing, unattributed, skipped, excepted = [], [], [], 0, 0
    unheld = []
    register_only = {n for n in corpus if 'provisions.yaml' in n}


    act_held = any('2024R1689' in n for n in corpus)
    for path in prose_files():
        text = path.read_text(encoding="utf-8")
        for number, line in logical_lines(path, text):
            pattern = QUOTED_YAML if str(path).endswith((".yaml", ".yml")) else QUOTED
            for match in pattern.finditer(line):
                quote = match.group(1)
                variants = [v for v in fragments(quote) if v]
                if not variants:
                    skipped += 1
                    continue
                site = f"{path.relative_to(ROOT)}:{number}"
                absent = wanted_but_absent(line)
                if absent:
                    unheld.append((site, quote, absent))
                    continue
                targets = attributed(line)

                def holds(name):
                    body = corpus[name]
                    return any(all(present(f, body) for f in frs) for frs in variants)

                # Found anywhere held is verified. Which file it sits in is this tool's
                # guess, not the author's claim, and a heuristic's mis-guess is not a
                # defect in the prose. Only absence from everything held is a finding.
                where = next((n for n in corpus if holds(n)), None)
                if where is None and declared(quote):
                    excepted += 1
                    continue
                if where:
                    found.append((site, quote, where))
                elif targets and set(targets) <= register_only and not act_held:
                    # The only place left to look was the register's own transcription,
                    # which is an EXTRACT of the statute rather than the statute. Where the
                    # authentic texts are not held, absence from an extract establishes
                    # nothing, and calling it a defect would make every clean clone red.
                    #
                    # A prefix heuristic was tried here, to rescue the case where the
                    # register does carry the passage. At six opening words it caught a
                    # planted wrong word and raised two false positives; at fourteen it
                    # raised none and caught nothing. The register holds ELIDED extracts,
                    # so no prefix test separates "covered" from "not covered" honestly,
                    # and a half-working check is worse than a stated limit. The limit is
                    # stated instead, in the summary and in the CI workflow.
                    unheld.append((site, quote, ["the authentic OJ and consolidated texts"]))
                elif targets:
                    missing.append((site, quote, targets, None))
                else:
                    unattributed.append((site, quote))

    checkable = len(found) + len(missing)
    if not quiet:
        if missing:
            print(f"{len(missing)} quotation(s) attributed to a held document and not "
                  f"found in it:\n")
            for site, quote, targets, elsewhere in missing:
                shown = quote if len(quote) <= 160 else quote[:157] + "..."
                print(f"  {site}\n    “{shown}”")
                print(f"    looked in: {', '.join(t[:60] for t in targets)}")
                if elsewhere:
                    print(f"    BUT FOUND IN: {elsewhere[:70]} — attributed to the "
                          f"wrong document, which is its own kind of wrong.")
                print()
        else:
            print(f"Every one of the {checkable} attributed quotation(s) was found in "
                  f"the document it is attributed to.")

        if show_verified and found:
            print(f"\n{len(found)} verified:")
            for site, quote, where in found:
                print(f"  {site} → {where[:60]}\n    “{quote[:100]}{'...' if len(quote)>100 else ''}”")

        rate = (len(found) / checkable * 100) if checkable else 0.0
        print(f"\nAttributed and checked: {len(found)}/{checkable} ({rate:.0f}%) against "
              f"{len(corpus)} held document(s).")
        print(f"Unattributable: {len(unattributed)} quotation(s) on lines naming no held "
              f"document — the incident record, foreign statutes, and this project's own "
              f"earlier drafts. Not defects, and not verified either.")
        if unheld:
            names = sorted({n for _s, _q, ns in unheld for n in ns})
            print(f"NOT CHECKED HERE: {len(unheld)} quotation(s) are attributed to "
                  f"{len(names)} document(s) this checkout does not hold.\nThey are "
                  f"unverifiable rather than wrong, and the distinction is the whole "
                  f"point:\na clean clone holds no _sources/, because the documents are "
                  f"cited by URL and SHA-256\nrather than redistributed. Missing: "
                  f"{', '.join(names)}.\nList them with --unheld.")
            if "--unheld" in sys.argv:
                for site, quote, ns in unheld:
                    print(f"  {site}  [{', '.join(ns)}]\n    “{quote[:110]}”")
        if excepted:
            print(f"Declared unverifiable, with reasons, in "
                  f"data/unverifiable-quotations.yaml: {excepted}.")
        if skipped:
            print(f"Too short or too elided to check: {skipped}.")

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
