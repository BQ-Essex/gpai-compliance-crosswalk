#!/usr/bin/env python3
"""Run every check this repository has, and say plainly what a clean run does not mean.

Four checkers, one command:

    validate.py    the cross-walk rows hold to the verdict discipline
    citecheck.py   every citation in the prose resolves to verified text
    quotecheck.py  every attributed quotation matches the document it is attributed to
    infercheck.py  the inference register is structurally sound
    housestyle.py  the prose conventions, including repeated paragraphs

    python3 tools/check.py            # run all four, summarise
    python3 tools/check.py --verbose  # also print each checker's own output

Exit code is the worst of the four, so this is the single thing to run before a commit
and the single thing to put in CI.

WHAT A GREEN BOARD DOES NOT MEAN, which is the part worth reading. Every one of the
fourteen errors in this project's corrections log passed every check that existed when it
was made. The checks establish that citations resolve, that quotations are accurate,
that verdicts stay in register and that absences are bounded. They cannot establish
that a provision is the right one for the proposition, that an inference from two
recitals is sound, or that a reading of a Commission opinion is the better of two
available readings. Those are the places this analysis has actually gone wrong, and no
checker here would have caught any of them. Green means the mechanical failures are
absent. It is a floor, not a verdict.

What narrows that gap is not a checker but a register. data/inferences.yaml enumerates
the argumentative steps, each stated so it could be denied, each naming what would defeat
it, each ranked by how contestable its own author thinks it is. Run

    python3 tools/infercheck.py --attack

to print the load-bearing steps weakest first. That list, not the report, is what an
adversarial reader should be handed.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent

PROSE_GLOBS = ("README.md", "docs/*.md", "protocol/*.md", "instrument/*.md")

CHECKS = (
    ("validate.py", [], "cross-walk rows hold to the verdict discipline"),
    ("citecheck.py", [], "citations resolve to verified text"),
    ("quotecheck.py", [], "quotations match the documents they are attributed to"),
    ("infercheck.py", [], "inference register: premises resolve, defeaters named, no cycles"),
    ("housestyle.py", None, "prose conventions, and no paragraph repeated"),
)


def prose_files():
    return sorted({str(p.relative_to(ROOT))
                   for glob in PROSE_GLOBS for p in ROOT.glob(glob)})


def run(script, args):
    path = TOOLS / script
    if not path.exists():
        return None, f"{script} is not in tools/"
    result = subprocess.run([sys.executable, str(path)] + args,
                            cwd=ROOT, capture_output=True, text=True)
    return result.returncode, (result.stdout + result.stderr).strip()


def main(argv):
    verbose = "--verbose" in argv
    width = max(len(name) for name, _, _ in CHECKS)
    worst, failures = 0, []

    for script, args, what in CHECKS:
        code, output = run(script, prose_files() if args is None else args)
        if code is None:
            print(f"  {script:<{width}}  SKIPPED   {output}")
            continue
        lines = [l for l in output.splitlines() if l.strip()]
        if script == "housestyle.py":
            # It reports per file and has no summary of its own; make one.
            summary = f"{len(lines)} prose file(s) clean" if code == 0 else ""
        else:
            summary = lines[0] if lines else ""
        mark = "ok  " if code == 0 else "FAIL"
        print(f"  {script:<{width}}  {mark}      {what}")
        if code == 0 and summary:
            print(f"  {'':<{width}}            {summary[:96]}")
        if code != 0:
            failures.append((script, output))
            worst = max(worst, code)
        if verbose:
            print("\n" + output + "\n")

    print()
    if failures:
        for script, output in failures:
            print(f"--- {script} ---")
            print(output)
            print()
        print(f"{len(failures)} of {len(CHECKS)} checks failing.")
    else:
        print("All clean. Which means the mechanical failures are absent, and nothing "
              "more:\nevery error in the corrections log passed every check that existed "
              "when it was made.\nFor the part no checker reaches, run "
              "`python3 tools/infercheck.py --attack`.")
    return worst


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
