#!/usr/bin/env python3
"""Check the inference register: premises resolve, defeaters exist, the graph is sound.

The other checkers verify correspondence — does this string appear in that document, does
this id resolve, does this sentence open in an approved register. None of them can decide
whether a step FOLLOWS, and soundness is not a decidable property, so no tool here will
ever say an argument is good.

That is not the end of the design. Every error in this project's corrections log was an
unsound step that passed every mechanical check available at the time, and it survived
because it was buried in prose where nobody was reading it as a claim. The fix is not
automation but exposure: enumerate the steps, make each one deniable, and make the
weakest ones the easiest to find. What can then be checked mechanically is real:

  · every premise resolves to a provision, recital or source that exists
  · every inference names something that would defeat it
  · the dependency graph is acyclic, and nothing depends on what is not there
  · every stated_at reference points at a heading that exists in the file it names
  · every inference says whether the provision behind it is a step or a graded one

None of that makes an argument sound. It makes an unsound one findable, which is the
only thing that has ever worked here.

    python3 tools/infercheck.py            # check, print findings
    python3 tools/infercheck.py --map      # print the dependency structure
    python3 tools/infercheck.py --attack   # print the reader's-eye list, weakest first

`--attack` is the reason this file exists. It prints the load-bearing steps ordered by
how contestable their own author thinks they are, which is the list an adversarial reader
should be handed instead of the report.

Exit codes:
    0  the register is structurally sound
    1  something is missing, dangling or circular
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

STRENGTHS = ("strong", "moderate", "contestable")
REQUIRED = ("claim", "type", "premises", "depends_on", "defeater", "strength", "function")
FUNCTIONS = ("step", "graded")


def load():
    inferences = yaml.safe_load((DATA / "inferences.yaml").read_text(encoding="utf-8"))
    provisions = yaml.safe_load((DATA / "provisions.yaml").read_text(encoding="utf-8"))
    sources = yaml.safe_load((DATA / "sources.yaml").read_text(encoding="utf-8"))
    known = set()
    for key in ("provisions", "imported_provisions", "recitals"):
        known |= {e["id"] for e in provisions.get(key, []) or []}
    known |= {s["id"] for s in sources.get("sources", []) or []}
    return inferences.get("inferences", []) or [], known


def check(entries, known):
    complaints = []
    ids = {e.get("id") for e in entries}

    for entry in entries:
        eid = entry.get("id", "<unnamed>")
        for field in REQUIRED:
            if field not in entry or entry[field] in (None, "", []):
                if field == "depends_on" and field in entry:
                    continue  # an empty list is a real answer
                complaints.append(f"[{eid}] has no {field}.")

        for premise in entry.get("premises", []) or []:
            if premise not in known:
                complaints.append(
                    f"[{eid}] rests on {premise!r}, which is not in the register. An "
                    f"inference from a premise nobody verified is the failure this whole "
                    f"file exists to surface.")

        for dep in entry.get("depends_on", []) or []:
            if dep not in ids:
                complaints.append(f"[{eid}] depends on {dep!r}, which is not an inference here.")

        function = entry.get("function")
        if function and function not in FUNCTIONS:
            complaints.append(f"[{eid}] function is {function!r}; use one of {list(FUNCTIONS)}.")

        strength = entry.get("strength")
        if strength and strength not in STRENGTHS:
            complaints.append(f"[{eid}] strength is {strength!r}; use one of {list(STRENGTHS)}.")

        if entry.get("load_bearing") and not entry.get("stated_at"):
            complaints.append(
                f"[{eid}] is load-bearing and does not say where it is stated. A step the "
                f"conclusion depends on should be findable in the prose.")

        for ref in re.finditer(r"([\w./-]+\.md)\s*§\s*([0-9]+(?:\.[0-9a-z]+)?)",
                               entry.get("stated_at") or ""):
            path, section = ROOT / ref.group(1), ref.group(2)
            if not path.exists():
                complaints.append(f"[{eid}] stated_at names {ref.group(1)}, which is not here.")
                continue
            body = path.read_text(encoding="utf-8")
            if not re.search(r"^#{2,4}\s+%s[.\s]" % re.escape(section), body, re.M):
                complaints.append(
                    f"[{eid}] says it is stated at {ref.group(1)} section {section}, and "
                    f"that section does not exist. Three of the first twelve entries here "
                    f"were wrong this way: the field that exists to make a claim findable "
                    f"was itself unchecked.")

        defeater = (entry.get("defeater") or "").strip()
        if defeater and len(defeater) < 40:
            complaints.append(
                f"[{eid}] names a defeater in under forty characters, which is usually a "
                f"gesture rather than a condition.")

    # Cycles: a proof that leans on its own conclusion.
    graph = {e.get("id"): list(e.get("depends_on") or []) for e in entries}
    state = {}

    def walk(node, trail):
        if state.get(node) == "done":
            return
        if state.get(node) == "open":
            complaints.append(f"Circular dependency: {' -> '.join(trail + [node])}.")
            return
        state[node] = "open"
        for nxt in graph.get(node, []):
            if nxt in graph:
                walk(nxt, trail + [node])
        state[node] = "done"

    for node in graph:
        walk(node, [])

    return complaints


def main(argv):
    entries, known = load()
    complaints = check(entries, known)

    if "--map" in argv:
        print("Dependency structure, roots first:\n")
        for entry in entries:
            deps = ", ".join(entry.get("depends_on") or []) or "—"
            flag = " [load-bearing]" if entry.get("load_bearing") else ""
            print(f"  {entry['id']:<26} {entry.get('strength','?'):<12} "
                  f"{entry.get('function','?'):<7} ← {deps}{flag}")
        print()

    if "--attack" in argv:
        order = {s: i for i, s in enumerate(reversed(STRENGTHS))}
        ranked = sorted((e for e in entries if e.get("load_bearing")),
                        key=lambda e: order.get(e.get("strength"), 9))
        print("The load-bearing steps, weakest first. If this analysis is wrong, it is "
              "most likely wrong here.\nA STEP inference flips wholly on one fact; a "
              "GRADED one moves the conclusion rather than breaking it.\n")
        for entry in ranked:
            print(f"  [{entry['strength'].upper()} / {entry.get('function','?')}] {entry['id']}")
            print(f"    {' '.join(entry['claim'].split())}")
            print(f"    would be defeated by: {' '.join(entry['defeater'].split())}")
            print(f"    stated at: {entry.get('stated_at','—')}\n")

    if complaints:
        print(f"{len(complaints)} thing(s) to look at in the inference register:\n")
        for complaint in complaints:
            print(f"  - {complaint}")
        return 1

    load_bearing = sum(1 for e in entries if e.get("load_bearing"))
    contestable = sum(1 for e in entries if e.get("strength") == "contestable")
    print(f"{len(entries)} inferences, all premises resolving, all defeaters named, "
          f"no cycles.\n{load_bearing} load-bearing, {contestable} marked contestable by "
          f"their own author. Structure only: whether any of them follows is not something "
          f"this or any checker decides.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
