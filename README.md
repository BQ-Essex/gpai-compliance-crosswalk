# GPAI Compliance Cross-Walk

A method for testing a frontier model provider’s obligations under the EU AI Act against a **public disclosure record**, together with a worked example and a model Article 91 request for information.

Built for the [Apart Research / CeSIA AI Incident Response Sprint](https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13), 11–13 September 2026, Track 3.

---

## What this is, and what it deliberately is not

This is **not** a legal opinion, and its author is not a lawyer. It is a protocol, and the protocol’s defensibility comes from a single, deliberately narrow claim:

> The method can establish whether a provider’s **own disclosed account**, taken on its own terms, resolves a given statutory obligation. It cannot establish what happened.

Everything here is built to hold that line. Verdicts may only take one of three forms—*appears met*, *appears unmet*, or *does not resolve*—and each is a claim about the disclosed record, never about events. That constraint is not a stylistic preference; it is what lets the analysis rest on accounts published by interested parties without vouching for them.

The constraint is also **machine-checked**, because a discipline that depends on a tired human at hour forty is a discipline that fails at hour forty:

```bash
pip install pyyaml          # the validator's only dependency
python3 tools/validate.py
```

`tools/housestyle.py` checks prose conventions and needs nothing beyond the standard library.

## The method caught itself being wrong, which is the point

Two independent adversarial passes were run over the finished draft with no sight of the reasoning that produced it. They found that the analysis had led on the wrong question.

The first version asked whether a model responsible for ~95% of the attacking agents had been notified to the Commission under Article 52(1), against that provision’s two-week deadline. It had not consulted **Article 3, point (63)**, whose definition of ‘general-purpose AI model’ ends “except AI models that are used for research, development or prototyping activities before they are placed on the market”, nor **Article 2(8)**, which excludes pre-market research, testing and development activity from the Regulation entirely. The scope argument rested on a recital, which cannot derogate from enacting terms.

The corrected analysis asks the prior question, and the gap it finds is larger: whether the obligations attach to that model at all. Findings, corrections and what was done about them are in [`docs/adversarial-review.md`](docs/adversarial-review.md) and [`docs/correction-scope.md`](docs/correction-scope.md).

## Why this framing rather than a legal opinion

Track 3 asks whether a regulator could use the output with light edits. A non-lawyer producing something that reads as confident legal advice is precisely where a trained reader finds the one imprecise sentence and discounts the whole document. What an outsider *can* offer, and what the public record is genuinely short of, is a transparent and replicable procedure: stated limits, tiered evidence, auditable verdicts, and an instrument that follows from them.

## Layout

```
protocol/     the method, abstracted from this incident — reusable on the next one
data/         provisions, sources and cross-walk rows as structured YAML
instrument/   the model Article 91 request for information
tools/        validate.py — enforces the verdict discipline; housestyle.py — prose conventions
docs/         worked example, comparative regimes, the correction record and review findings
```

### `data/provisions.yaml`
Verified statutory text with provenance. Every provision records whether it was amended by **Regulation (EU) 2026/1744** (the Digital Omnibus on AI), taken from the EUR-Lex change markers themselves rather than inferred from commentary. Extracted from the consolidated text at CELEX `02024R1689-20260727`; recitals from the authentic OJ text at `32024R1689`, the consolidated version omitting them.

### `data/sources.yaml`
Every source, tiered by its **relationship to the claim** rather than by prestige:

| Tier | Meaning |
|---|---|
| T1 | The party whose conduct is in question, on its own conduct |
| T2 | The affected party’s forensic account |
| T3 | An investigator operating under access constraints imposed by the subject |
| T4 | An independent third party |

Two providers’ self-reports appear in this register. Both sit at **T1**, and both carry the same reservations. Nothing in the analysis turns on which provider is which—see the `tier_note` on each.

### `data/crosswalk.yaml`
The rows. Each separates **disclosed facts** from the **provider’s characterisation** of those facts, and verdicts are derived from the facts only. The split exists because a verdict drawn from a provider’s own labelling quietly re-derives that provider’s own conclusion; the validator fails any row that states a verdict without recording facts to support it.

## What the validator checks

- Every verdict opens with one of the three permitted registers
- Every provision and source reference resolves
- Every source carries a tier, a date, and a **pinpoint** URL (bare domains are flagged)
- Every row states facts to derive its verdict from
- Every unresolved row carries a route to settlement **and** a dated negative-search note—so that “the record is silent” is something demonstrated rather than assumed

## What this repository does not contain, by choice

The exploit chain in the July 2026 intrusion is already public, published by the affected party in its own technical timeline. This repository **cites it by reference and does not reproduce payloads, injection strings, or a consolidated reconstruction of the escalation path.**

That is a deliberate call rather than an oversight. The same facts scattered across a vendor blog post and an incident timeline are a different artifact from those facts assembled, ordered and annotated in one convenient place—the assembly is the part that adds operational value, and this document’s purpose is regulatory analysis, for which the category of vulnerability suffices and the working detail does not. The sprint’s own guidance asks that novel installation recipes not be published without review; the same spirit is applied here to aggregation.

## Status and limits

Prepared over a sprint weekend by one person. Specific limits:

- **The author is not a lawyer.** The statutory text is verified against primary sources; the reasoning from it is an outsider’s, offered as a method to be checked rather than advice to be relied on.
- **The record is live and moving.** Every negative-search note carries an as-of date for this reason. Several underlying facts were days old when this was written.
- **Two designations remain unreconciled.** The model responsible for the majority of the attacking agents is named differently in the provider’s account and in the independent investigation, and this repository does not assert that they are the same model—establishing that is Request 1 of the instrument.

## Licence

Prose, data and the model instrument: **CC BY 4.0**. Code in `tools/`: **MIT**. See `LICENSE`.

The model instrument in `instrument/` is a **draft**. It has not been issued by, adopted by, or submitted to any Union body, and all fields requiring an issuing authority are left as explicit placeholders so that it cannot be mistaken for an issued document.
