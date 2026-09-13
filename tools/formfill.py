#!/usr/bin/env python3
"""Fill a regulator's serious-incident template from the public record, as data.

Filling a regulator's form from the public record turned out to be a test of the form:
that is how the awareness-date finding was made (report §5.2). This script makes the
test repeatable. `data/form-fill.yaml` holds, for each field of the template, what the
public record gives, from which cross-walk rows and sources, and with what status. The
script checks every row and source it names exists, then renders the fill twice: into
the amended template as a DOCX, each field carrying its status and text, and as a
Markdown table for a report appendix.

The FILL is judgement and is written by hand in the YAML. The RENDERING is not, and is
what transfers: the next incident edits the YAML and runs this; a different regime's
template needs a different DOCX and a field list, and the same YAML shape.

    python3 tools/formfill.py                 # writes instrument/filled-template.docx
                                              # and docs/filled-template.md
    python3 tools/formfill.py --check         # validate the YAML only

Exit codes: 0 rendered (or valid); 1 a named row or source does not exist, or a status
is not one of filled | partial | cannot-fill.
"""

from __future__ import annotations

import copy
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import housestyle  # noqa: E402  - rendered prose is house-styled by construction

ROOT = Path(__file__).resolve().parent.parent
FILL = ROOT / "data" / "form-fill.yaml"
CROSSWALK = ROOT / "data" / "crosswalk.yaml"
SOURCES = ROOT / "data" / "sources.yaml"
TEMPLATE = ROOT / "instrument" / "model-amended-serious-incident-template.docx"
OUT_DOCX = ROOT / "instrument" / "filled-template.docx"
OUT_MD = ROOT / "docs" / "filled-template.md"
STATUSES = ("filled", "partial", "cannot-fill")
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def validate(fill, rows, sources) -> list[str]:
    findings = []
    seen = set()
    for f in fill.get("fields") or []:
        fid = str(f.get("field"))
        if fid in seen:
            findings.append(f"field {fid}: listed twice")
        seen.add(fid)
        if f.get("status") not in STATUSES:
            findings.append(f"field {fid}: status {f.get('status')!r} is not one of {STATUSES}")
        for r in f.get("rows") or []:
            if r not in rows:
                findings.append(f"field {fid}: cross-walk row {r!r} does not exist")
        for s in f.get("sources") or []:
            if s not in sources:
                findings.append(f"field {fid}: source {s!r} is not in the register")
        if not (f.get("text") or "").strip():
            findings.append(f"field {fid}: no text")
    return findings


def set_cell_text(tc, text: str) -> None:
    """Write into a template cell's first text run and clear the rest, keeping its controls."""
    # The Commission's form puts each prompt inside a content control (w:sdt). Where one
    # exists, write into it and leave the label runs alone; the label and the prompt can
    # share a paragraph, and overwriting the first run in the paragraph erases the label.
    ts = tc.findall(f".//{{{W}}}sdt//{{{W}}}t") or tc.findall(f".//{{{W}}}t")
    if not ts:
        return
    for i, el in enumerate(ts):
        el.text = text if i == 0 else ""
    ts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")


def render_docx(fill) -> None:
    from docx import Document
    doc = Document(str(TEMPLATE))
    by_field = {str(f["field"]): f for f in fill["fields"]}
    table = doc.tables[0]
    rows = table.rows
    # Rows come in label/content pairs; the number cell says which field.
    for i in range(0, len(rows) - 1, 2):
        num = rows[i].cells[0].text.strip()
        if num not in by_field:
            continue
        f = by_field[num]
        text = f"[{f['status'].upper()}] {' '.join(str(f['text']).split())}"
        # The content cell is the last w:tc in the content row. In the Commission's form it
        # is a plain cell for some fields and a cell wrapped in a content control (w:sdt at
        # row level) for others, which python-docx's .cells does not see; a descendant
        # search finds both.
        content_tcs = rows[i + 1]._tr.findall(f".//{{{W}}}tc")
        set_cell_text(content_tcs[-1], text)
    if "10" in by_field:
        f = by_field["10"]
        p = doc.add_paragraph()
        p.add_run(f"10. Submitter information — [{f['status'].upper()}] ").bold = True
        p.add_run(" ".join(str(f["text"]).split()))
    p = doc.add_paragraph()
    p.add_run(f"Filled from the public record on {fill.get('filled_on')} by tools/formfill.py "
              f"from data/form-fill.yaml. Not a filing. Not a document of any Union body. "
              f"Every cell names the cross-walk rows and sources it rests on in that file.").italic = True
    doc.save(str(OUT_DOCX))


def render_md(fill) -> None:
    lines = [f"# The template, filled from the public record",
             "",
             f"*Rendered by `tools/formfill.py` from `data/form-fill.yaml` on {fill.get('filled_on')}. "
             f"Form: {fill.get('form')}. Incident: `{fill.get('incident')}`. "
             f"The fill is judgement, made in the YAML; the table is not.*",
             "",
             "| # | Field | What the public record gives | Rows | Sources | Status |",
             "|---|---|---|---|---|---|"]
    counts = {s: 0 for s in STATUSES}
    for f in fill["fields"]:
        counts[f["status"]] += 1
        text = " ".join(str(f["text"]).split())
        lines.append(f"| {f['field']} | {f['label']} | {text} | "
                     f"{', '.join(f'`{r}`' for r in f.get('rows') or [])} | "
                     f"{', '.join(f'`{s}`' for s in f.get('sources') or [])} | "
                     f"**{f['status']}** |")
    lines += ["", f"**{counts['filled']} filled, {counts['partial']} partial, "
                  f"{counts['cannot-fill']} cannot fill**, of {len(fill['fields'])} fields.", ""]
    body = "\n".join(lines)
    shelved, stash = housestyle.shelve_protected(body)
    body = housestyle.restore_protected(
        housestyle.curl_the_quotes(housestyle.close_the_dashes(shelved)), stash)
    OUT_MD.write_text(body, encoding="utf-8")
    return counts


def main(argv: list[str]) -> int:
    fill = yaml.safe_load(FILL.read_text(encoding="utf-8")) or {}
    rows = {r["id"] for r in (yaml.safe_load(CROSSWALK.read_text(encoding="utf-8")) or {}).get("rows") or []}
    sources = {s["id"] for s in (yaml.safe_load(SOURCES.read_text(encoding="utf-8")) or {}).get("sources") or []}
    findings = validate(fill, rows, sources)
    if findings:
        print(f"{len(findings)} thing(s) wrong with the fill:")
        for f in findings:
            print("  -", f)
        return 1
    if "--check" in argv:
        print(f"fill valid: {len(fill['fields'])} fields, every row and source resolving")
        return 0
    counts = render_md(fill)
    try:
        render_docx(fill)
        docx_note = OUT_DOCX.relative_to(ROOT)
    except ImportError:
        docx_note = "(python-docx not installed; DOCX skipped)"
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {docx_note}: "
          f"{counts['filled']} filled, {counts['partial']} partial, {counts['cannot-fill']} cannot fill.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
