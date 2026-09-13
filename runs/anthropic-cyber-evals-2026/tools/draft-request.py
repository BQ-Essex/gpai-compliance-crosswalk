#!/usr/bin/env python3
"""Draft an Article 91 request for information from the cross-walk.

Every unresolved row in `data/crosswalk.yaml` already says what would settle it and
what would not, and names the provision it tests. That is most of a request. This
script assembles the rest: the parts Article 91(4) requires - legal basis, purpose,
specification, period, indication of fines - from boilerplate that does not change
between incidents, and one numbered request per unresolved row from the row's own
`would_settle` and `would_not_settle` fields.

What it automates is the FORM. What it does not automate is any judgement: which rows
are unresolved is the analyst's verdict, what would settle each is the analyst's call,
and the draft it writes is a first draft that a person then edits into the
instrument at `instrument/model-article-91-request.md` (which, for this incident, was
edited a long way from what this script produces). The point is that the next
incident's request starts from its cross-walk in seconds rather than from a blank page.

    python3 tools/draft-request.py                    # writes instrument/draft-request.md
    python3 tools/draft-request.py --out path.md      # elsewhere
    python3 tools/draft-request.py --all              # every row, resolved or not

Rows whose verdict begins "The disclosed record does not resolve this" are treated as
unresolved. The other two permitted openers are treated as resolved on the provider's
own account and are skipped unless --all is given; a request about a resolved row is
still sometimes right (the account may be wrong), which is why --all exists.
"""

from __future__ import annotations

import datetime
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import housestyle  # noqa: E402  - the generated prose is house-styled by construction

ROOT = Path(__file__).resolve().parent.parent
CROSSWALK = ROOT / "data" / "crosswalk.yaml"
PROVISIONS = ROOT / "data" / "provisions.yaml"
UNRESOLVED = "The disclosed record does not resolve this"

HEADER = """---

> ## ⚠ PROVENANCE—READ FIRST
>
> **This is a MODEL instrument, generated as a first draft. It has not been issued.**
>
> Assembled by `tools/draft-request.py` on {date} from the cross-walk at `data/crosswalk.yaml`: one request per row the analysis records as unresolved, each carrying that row’s provision and its own statement of what would and would not settle it. It is not a document of the European Commission, the AI Office or any Union body. Every field requiring an issuing authority’s input is a placeholder in square brackets. A person edits this before it is anything.

---

# MODEL REQUEST FOR INFORMATION
### under Article 91 of Regulation (EU) 2024/1689

**Reference:** [to be assigned by the issuing authority]
**Date:** [to be inserted]
**Addressee:** [Provider concerned—“the Provider”]
**Issued by:** [European Commission—“the Commission”]

## Part A: Legal basis

1. This request is made under **Article 91(1)** of Regulation (EU) 2024/1689 (“the Regulation”), which empowers the Commission to request from the provider of a general-purpose AI model “the documentation drawn up by the provider in accordance with Articles 53 and 55, or any additional information that is necessary for the purpose of assessing compliance of the provider with this Regulation”. No alternative basis is stated.

2. The provisions to which the requested information relates are: {provisions}. Chapter V has applied since 2 August 2025 pursuant to Article 113, point (b); Article 91 has applied since 2 August 2026 under the general rule in Article 113.

3. **Empowerment.** Having regard to Regulation (EU) 2024/1689, and in particular Article 91(1) and (4) thereof, and to the Commission’s competence under Article 88 in respect of providers of general-purpose AI models. [Act of adoption and signatory’s competence to be recited by the issuing authority.]

## Part B: Purpose

4. The Commission is considering the following publicly reported episode(s) involving AI models developed by the Provider: {incidents}

5. The Commission has **not** formed a view that any episode constitutes a serious incident within the meaning of Article 3, point (49), that any obligation under the Regulation applies to any particular model, or that any obligation has been contravened. The purpose of this request, in the terms of Article 91(1), is to obtain information necessary for the purpose of assessing compliance of the Provider with this Regulation, which the public record does not resolve.

## Part C: Defined terms

6. [Define each model by the Provider’s own designation. Do not define a model by a third party’s name for it.]

## Part D: Information required

*Nothing here requires an admission.* Where a request asks the Provider to state a position on the legal characterisation of facts, the Provider may answer or decline, no adverse inference will be drawn from declining, and nothing in this request requires the Provider to admit any infringement. The facts and documents requested are required; the reasoning about them is invited.

*Applicability does not limit production.* Where the Provider considers that a provision does not apply to a model, it shall nonetheless provide the internal documentation it holds covering the matters that provision describes, and may state its position on applicability separately.

*Legal professional privilege is preserved.* Nothing in this request requires production of communications protected by legal professional privilege as recognised in the case-law of the Court of Justice. Where the Provider withholds a document on that ground it shall provide a schedule identifying the document, its date, the category of author and recipient, and the basis of the claim. Privilege is not a ground for withholding the underlying facts or the dates on which steps were taken.

"""

REQUEST = """**Request {n}** *({cite}; cross-walk row `{row}`)*. {ask}

"""

FOOTER = """## Part E: Period for response

{p}. The Provider shall supply the information requested by **[date]**, being the period set by the Commission for the purposes of Article 91(4). [Consider tranching: one period for factual and status questions, a later one for document productions.]

{q}. Where the Provider considers that it cannot comply in full within that period, it may apply in writing, before the expiry of the period and with reasons, for an extension in respect of identified items. An extension takes effect only if granted by the Commission in writing.

{r}. Information supplied in response to this request is subject to Article 78. The Provider is not invited to withhold information on confidentiality grounds, but should identify material it considers confidential, including trade secrets, so that it may be handled accordingly.

## Part F: Indication of fines (Article 91(4))

{s}. In accordance with Article 91(4), attention is drawn to **Article 101(1), point (b)**, under which the Commission may impose on providers of general-purpose AI models fines not exceeding **3 % of annual total worldwide turnover in the preceding financial year or EUR 15 000 000, whichever is higher**, where it finds that the provider intentionally or negligently “failed to comply with a request for a document or for information pursuant to Article 91, or supplied incorrect, incomplete or misleading information”.

{t}. In accordance with **Article 91(5)**, the information requested shall be supplied by the Provider or its representative. Lawyers duly authorised to act may supply information on behalf of their clients; the Provider nevertheless remains fully responsible if the information supplied is incomplete, incorrect or misleading. The response shall be accompanied by a statement, signed by a person authorised to represent the Provider, that the information supplied is to the best of that person’s knowledge correct, complete and not misleading.

{u}. **Format, channel and language.** The response shall be provided in English, in electronic form, to **[address]**, with each item identified by the number of the request to which it responds.

**[Signature block—to be completed by the issuing authority]**

---

## Issuing note (not for the addressee): what would not settle each request

| # | Row | What would not settle it |
|---|---|---|
{table}
"""


def main(argv: list[str]) -> int:
    out = ROOT / "instrument" / "draft-request.md"
    if "--out" in argv:
        out = Path(argv[argv.index("--out") + 1])
    everything = "--all" in argv
    walk = yaml.safe_load(CROSSWALK.read_text(encoding="utf-8")) or {}
    provs = yaml.safe_load(PROVISIONS.read_text(encoding="utf-8")) or {}
    cite = {e["id"]: e["cite"] for s in ("provisions", "imported_provisions", "recitals")
            for e in (provs.get(s) or [])}
    rows = [r for r in (walk.get("rows") or [])
            if everything or (r.get("verdict") or "").strip().startswith(UNRESOLVED)]
    if not rows:
        print("no unresolved rows in the cross-walk; nothing to ask")
        return 1
    incidents = walk.get("incidents") or {}
    inc_text = "; ".join(f"({chr(97 + i)}) {v.get('label', k)}, {v.get('window', '')}"
                         for i, (k, v) in enumerate(incidents.items())) or "[describe]"
    cites = sorted({cite.get(r.get("provision"), r.get("provision")) for r in rows})
    body = HEADER.format(date=datetime.date.today().isoformat(),
                         provisions=", ".join(cites), incidents=inc_text)
    table = []
    for n, r in enumerate(rows, start=1):
        ask = (r.get("would_settle") or "[state what would settle this row]").strip()
        body += REQUEST.format(n=n, cite=cite.get(r.get("provision"), r.get("provision")),
                               row=r["id"], ask=ask)
        table.append(f"| {n} | `{r['id']}` | {(r.get('would_not_settle') or '').strip()} |")
    p = 7
    body += FOOTER.format(p=p, q=p + 1, r=p + 2, s=p + 3, t=p + 4, u=p + 5, table="\n".join(table))
    shelved, stash = housestyle.shelve_protected(body)
    body = housestyle.restore_protected(
        housestyle.curl_the_quotes(housestyle.close_the_dashes(shelved)), stash)
    out.write_text(body, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}: "
          f"{len(rows)} request(s) from {len(walk.get('rows') or [])} row(s). A person edits this next.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
