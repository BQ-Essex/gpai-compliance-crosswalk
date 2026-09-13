#!/usr/bin/env python3
"""Render the enforcement pack to DOCX, because "light edits" happen in Word.

Every Markdown document in `instrument/` is rendered to `instrument/docx/<name>.docx`
with pandoc. The Markdown stays the source of truth and is what the checkers read; the
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
    for extra in ("model-amended-serious-incident-template.docx", "filled-template.docx"):
        if (SRC / extra).exists():
            shutil.copy2(SRC / extra, OUT / extra)
            done.append(extra)
    print("rendered:", ", ".join(done))
    return 0


if __name__ == "__main__":
    sys.exit(main())
