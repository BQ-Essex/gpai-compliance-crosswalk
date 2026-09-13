#!/usr/bin/env python3
"""Render the enforcement pack to DOCX, because "light edits" happen in Word.

Every Markdown document in `instrument/` is rendered to `instrument/docx/<name>.docx`
with pandoc, and the report itself to `docs/docx/report-draft.docx` — the submission is
typeset by pasting into the sprint's own template, and a DOCX pastes with its structure
intact where Markdown does not. The Markdown stays the source of truth and is what the checkers read; the
DOCX is what an official opens. Re-run after any edit. The amended template and the
filled template are already DOCX and are copied alongside.

    python3 tools/render-pack.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "instrument"
OUT = SRC / "docx"
ORDER = ("cover-note", "model-article-91-request", "issuing-note", "answer-matrix",
         "what-the-provider-will-say", "amendment-table", "draft-request")


def main() -> int:
    if not shutil.which("pandoc"):
        print("pandoc is not on the path; install it or open the Markdown directly")
        return 1
    OUT.mkdir(exist_ok=True)
    done = []
    for name in ORDER:
        md = SRC / f"{name}.md"
        if not md.exists():
            continue
        target = OUT / f"{name}.docx"
        subprocess.run(["pandoc", str(md), "-o", str(target), "--from", "gfm",
                        "--metadata", f"title={name.replace('-', ' ')}"], check=True)
        done.append(target.name)
    # The report, for typesetting. Same source of truth, same renderer, so the file an
    # official opens is never hand-made and never drifts from the Markdown the checkers read.
    report = ROOT / "docs" / "report-draft.md"
    if report.exists():
        report_out = ROOT / "docs" / "docx"
        report_out.mkdir(exist_ok=True)
        subprocess.run(["pandoc", str(report), "-o", str(report_out / "report-draft.docx"),
                        "--from", "gfm", "--toc", "--metadata",
                        "title=Reached by Recital"], check=True)
        done.append("docs/docx/report-draft.docx")

    for extra in ("model-amended-serious-incident-template.docx", "filled-template.docx"):
        if (SRC / extra).exists():
            shutil.copy2(SRC / extra, OUT / extra)
            done.append(extra)
    print("rendered:", ", ".join(done))
    return 0


if __name__ == "__main__":
    sys.exit(main())
