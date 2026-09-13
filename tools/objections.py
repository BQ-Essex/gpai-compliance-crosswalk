#!/usr/bin/env python3
"""Render what the provider will say, from the inference register, for the AI Office.

`python3 tools/infercheck.py --attack` prints the load-bearing steps weakest first with
what their own author says would defeat each. That is the list a provider's counsel
would work from, and it is the list a desk officer should have read before the reply
arrives. This renders it as a page in the pack: one row per load-bearing step, the
objection in the register's own words, and where the step is stated so the answer can
be found. It is generated from `data/inferences.yaml` so it cannot drift from it.

    python3 tools/objections.py        # writes instrument/what-the-provider-will-say.md
"""

from __future__ import annotations

import datetime
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import housestyle  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "data" / "inferences.yaml"
OUT = ROOT / "instrument" / "what-the-provider-will-say.md"
ORDER = {"contestable": 0, "moderate": 1, "strong": 2}

HEAD = """# What the provider will say

*For the AI Office. Rendered by `tools/objections.py` on {date} from `data/inferences.yaml`: every load-bearing step in the analysis, weakest first, with the objection its own author recorded against it. A provider's counsel will reach for these in roughly this order. Each row says where the step is stated so the answer can be found; the register itself, and `python3 tools/infercheck.py --attack`, are the source. Not a document of any Union body.*

A **step** inference flips wholly on one fact; a **graded** one moves the conclusion rather than breaking it. Strength is the author's own estimate and is the softest thing here.

| # | Step | Strength | The objection, in the register's words | Stated at |
|---|---|---|---|---|
"""

TAIL = """
**How to read it.** The first rows are where the analysis expects to be attacked and where a reply should be prepared before the response to the request is opened. Rows marked *strong* are where a provider's objection would have to be argued from something the register has not seen; the register names what that would be. Nothing above is a prediction of what any provider will in fact say.
"""


def main() -> int:
    data = yaml.safe_load(REGISTER.read_text(encoding="utf-8")) or {}
    entries = [e for e in data.get("inferences") or [] if e.get("load_bearing")]
    entries.sort(key=lambda e: ORDER.get(e.get("strength"), 9))
    body = HEAD.format(date=datetime.date.today().isoformat())
    for n, e in enumerate(entries, start=1):
        claim = " ".join(str(e.get("claim", "")).split())
        objection = " ".join(str(e.get("defeater", "")).split())
        body += (f"| {n} | `{e['id']}` — {claim} | {e.get('strength','?')} / {e.get('function','?')} "
                 f"| {objection} | {e.get('stated_at','')} |\n")
    body += TAIL
    shelved, stash = housestyle.shelve_protected(body)
    body = housestyle.restore_protected(
        housestyle.curl_the_quotes(housestyle.close_the_dashes(shelved)), stash)
    OUT.write_text(body, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(entries)} load-bearing steps, weakest first")
    return 0


if __name__ == "__main__":
    sys.exit(main())
