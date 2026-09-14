#!/usr/bin/env python3
"""Stand up an empty repository for the next incident, with the method already in it.

The claim this repository makes about itself is that the verification layer transfers
and the judgement does not. This script is the checkable half of that claim. It creates
a new directory holding the six checkers, the verified statutory register, the method,
the source-register schema and an empty cross-walk, inference register and corrections
log, and then runs `tools/check.py` inside it so that the first thing a new incident's
board shows is a clean run over nothing — which is what a clean board means.

What it copies:
    tools/*.py                     the checkers and this script
    data/provisions.yaml           47 provisions, 7 imported CER provisions, 4 recitals,
                                   5 judgments, all verified against the consolidated text
                                   as of the date in its `meta` block — re-verify before
                                   relying on amendment status
    protocol/00-method.md          the method, unchanged
    _sources/README.txt            what goes in _sources/ and why

What it writes fresh:
    data/sources.yaml              the tier definitions and an empty `sources:` list
    data/crosswalk.yaml            the openers, an empty `rows:` list and one commented
                                   template row carrying every field the checkers expect
    data/inferences.yaml           the schema and an empty `inferences:` list
    data/unverifiable-quotations.yaml   the permitted kinds and an empty list
    data/form-fill.yaml            the form-fill schema and an empty field list
    protocol/01-statutory-foundation.md a corrections log with no rows yet
    README.md                      a stub pointing at the runbook

What it does not do: any of the judgement. There is no incident in the new directory.

    python3 tools/new-incident.py ../next-incident
    python3 tools/new-incident.py ../next-incident --no-check
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

COPY = (
    "data/provisions.yaml",
    "protocol/00-method.md",
    "_sources/README.txt",
)

SOURCES = '''# Source register. Tier by the source's relationship to the claim, not by prestige.
#
#   T1  the party whose conduct is in question, on its own conduct
#   T2  the affected party's forensic account
#   T3  an investigator operating under access constraints imposed by the subject
#   T4  an independent third party with no stake in the characterisation
#
# Every held document gets a `documents:` entry with its file name and SHA-256.
# Every negative-search note gets an `as_of` date and a `corpus`.

tiers:
  T1: "Party whose conduct is in question, reporting on its own conduct"
  T2: "Affected party's forensic account"
  T3: "Investigator under subject-imposed access constraints"
  T4: "Independent third party"

sources: []
'''

CROSSWALK = '''# The cross-walk, as structured data. Verdicts MUST begin with one of the three
# permitted openers; tools/validate.py enforces it. Verdicts derive from `facts` only;
# `characterisation` is analysed separately and is never an input to a verdict.
#
# Template row (uncomment and fill; every field is one the checkers read):
#
#   - id: g0-example
#     gate: "0"
#     provision: art3-63            # an id in data/provisions.yaml
#     applies_to: [incident-key]
#     obligation: >-
#       What the provision requires, in one paragraph.
#     facts:
#       - claim: "What a discloser says occurred, quoted where possible."
#         sources: [source-id]       # ids in data/sources.yaml
#     characterisation:
#       - claim: "What the discloser calls it. Never an input to the verdict."
#         sources: [source-id]
#     verdict: >-
#       The disclosed record does not resolve this; ...
#     conclusion_of_law: >-
#       Reasoning, not evidence, recorded separately. Optional.
#     would_settle: "The document or fact that would."
#     would_not_settle: "What a discloser might offer that would not."
#     negative_search:
#       statement: "No published source states X."
#       as_of: "YYYY-MM-DD"
#       corpus: "What was searched, with what terms, on what date."

incidents: {}

rows: []
'''

INFERENCES = '''# The argumentative steps, enumerated. Each entry carries:
#   claim, type, function (step | graded), premises (ids in provisions.yaml or
#   sources.yaml), depends_on (other inference ids; acyclic), defeater, strength
#   (strong | moderate | contestable), load_bearing, stated_at.

inferences: []
'''

FORMFILL = '''# A regulator's template, filled from the public record, as data. One entry per field:
#   field, label, status (filled | partial | cannot-fill), text, rows (cross-walk ids),
#   sources (source ids). tools/formfill.py checks the ids and renders the fill.

form: "[name and date of the template]"
incident: "[incident key from crosswalk.yaml]"
filled_on: "YYYY-MM-DD"

fields: []
'''

UNVERIFIABLE = '''# Quotations this project cannot verify against a held document, each with a reason.
# Kinds: own-words | source-unheld | method-text | extraction-artefact.

exceptions: []
'''

FOUNDATION = '''# Statutory foundation

## 0. Corrections log

Errors found in this analysis are recorded here rather than silently fixed. The
header sentence states the count in words and `tools/housestyle.py` checks it against
the rows; every sentence elsewhere that quotes the count is checked too.

| Error | Correction |
|---|---|

## 1. Working

*The statutory working for this incident goes here, provision by provision, quoting
the verified text from `data/provisions.yaml`.*
'''

README = '''# New incident

Stood up by `tools/new-incident.py` from the gpai-compliance-crosswalk repository. The
runbook for filling it is that repository’s README, section “Running it on the next
incident”. Run `python3 tools/check.py` after every change; a clean board means the
mechanical failures are absent and nothing more.
'''


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    target = Path(args[0]).resolve()
    if target.exists() and any(target.iterdir()):
        print(f"refusing to write into a non-empty directory: {target}")
        return 1
    for sub in ("tools", "data", "protocol", "_sources", "docs", "instrument"):
        (target / sub).mkdir(parents=True, exist_ok=True)
    for script in sorted(HERE.glob("*.py")):
        shutil.copy2(script, target / "tools" / script.name)
    for rel in COPY:
        src = ROOT / rel
        if src.exists():
            shutil.copy2(src, target / rel)
    (target / "data/sources.yaml").write_text(SOURCES, encoding="utf-8")
    (target / "data/crosswalk.yaml").write_text(CROSSWALK, encoding="utf-8")
    (target / "data/inferences.yaml").write_text(INFERENCES, encoding="utf-8")
    (target / "data/unverifiable-quotations.yaml").write_text(UNVERIFIABLE, encoding="utf-8")
    (target / "data/form-fill.yaml").write_text(FORMFILL, encoding="utf-8")
    (target / "protocol/01-statutory-foundation.md").write_text(FOUNDATION, encoding="utf-8")
    (target / "README.md").write_text(README, encoding="utf-8")
    print(f"stood up {target}")
    if "--no-check" in argv:
        return 0
    print("running the checkers over the empty repository:")
    result = subprocess.run([sys.executable, str(target / "tools/check.py")],
                            cwd=target, capture_output=True, text=True)
    print(result.stdout[-1500:])
    return result.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
