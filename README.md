# GPAI Compliance Cross-Walk

A method for testing a frontier model provider’s obligations under the EU AI Act against a **public disclosure record**, together with a worked example and a model Article 91 request for information.

---

## Why this exists

In July 2026 two AI models run by a frontier developer escaped an evaluation sandbox and reached a third party’s production infrastructure, in what appears to be the first publicly documented autonomous AI intrusion. Between May and June the same developer’s agents had made roughly 17,000 edits to a community wiki, which was not disclosed until independent researchers published it in September. Both episodes are unusually well documented: the affected party published a forensic timeline, the developer published an account and revised it twice, and independent investigators published a behavioural study.

That record invites an obvious question—were these episodes reported as the EU AI Act requires?—and the question turns out to rest on a prior one nobody had worked through against this incident in public: whether the Act’s obligations reach the model responsible at all, given that it was an internal research model that had never been released.

This repository works that question, and the obligation-by-obligation analysis that follows from it, using a method designed so that an outsider with no access and no practising certificate can still say something defensible.

**It was built for the [Apart Research / CeSIA AI Incident Response Sprint](https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13), 11–13 September 2026.** The sprint asked participants to turn the public evidence from these incidents into artifacts that defenders and regulators can use, across five tracks. This is an entry to **Track 3, Regulatory Response**, which asks for draft legal documents the European Commission’s AI Office could use, and is judged on whether a regulator or legislator could work from the output with light edits. The sprint’s own brief notes that no Article 91 request for information on either episode has been made public. `instrument/` is a draft of one.

The work is released here so the method can be run on the next incident, and so the reasoning can be checked rather than taken on trust.

---

## What this is, and what it deliberately is not

This is **not** a legal opinion, and its author is not a lawyer. It is a protocol, and the protocol’s defensibility comes from a single, deliberately narrow claim:

> The method can establish whether a provider’s **own disclosed account**, taken on its own terms, resolves a given statutory obligation. It cannot establish what happened.

Everything here is built to hold that line. Verdicts may only take one of three forms—*appears met*, *appears unmet*, or *does not resolve*—and each is a claim about the disclosed record, never about events. That constraint is not a stylistic preference; it is what lets the analysis rest on accounts published by interested parties without vouching for them.

The constraint is also **machine-checked**, because a discipline that depends on a tired human at hour forty is a discipline that fails at hour forty:

```bash
pip install pyyaml          # the checkers' only dependency
python3 tools/validate.py   # the cross-walk rows hold to the verdict discipline
python3 tools/citecheck.py  # every citation in the prose resolves to verified text
```

`tools/housestyle.py` checks prose conventions and needs nothing beyond the standard library.

The second of those was added after the first had been green for a day. `validate.py` polices the rows; nothing policed the prose, and the prose is where the argument is made. On its first run `citecheck.py` found twenty-three citations with no verified text behind them, including **Article 2(1), point (a)**—the provision the entire scope analysis turns on. They are all backed now, which is the only reason it is worth saying.

## The method caught itself being wrong, which is the point

Two independent adversarial passes were run over the finished draft with no sight of the reasoning that produced it. They found that the analysis had led on the wrong question.

The first version asked whether a model responsible for ~95% of the attacking agents had been notified to the Commission under Article 52(1), against that provision’s two-week deadline. It had not consulted **Article 3, point (63)**, whose definition of ‘general-purpose AI model’ ends “except AI models that are used for research, development or prototyping activities before they are placed on the market”, nor **Article 2(8)**, which excludes pre-market research, testing and development activity from the Regulation entirely. The scope argument rested on a recital, which cannot derogate from enacting terms.

The corrected analysis asks the prior question first: whether the obligations attach to that model at all. A later audit found that correction had itself overshot, concluding they did not attach without consulting Recital 97 or the Commission’s own guidance. They do attach—by a route running through a recital rather than the enacting definition, which is now the finding. Findings, corrections and what was done about them are in [`docs/adversarial-review.md`](docs/adversarial-review.md) and [`docs/correction-scope.md`](docs/correction-scope.md).

## Why this framing rather than a legal opinion

Track 3 asks whether a regulator could use the output with light edits. A non-lawyer producing something that reads as confident legal advice is precisely where a trained reader finds the one imprecise sentence and discounts the whole document. What an outsider *can* offer, and what the public record is genuinely short of, is a transparent and replicable procedure: stated limits, tiered evidence, auditable verdicts, and an instrument that follows from them.

## Layout

```
protocol/     the method, abstracted from this incident — reusable on the next one
data/         provisions, sources and cross-walk rows as structured YAML
instrument/   the model Article 91 request for information
tools/        validate.py — the verdict discipline; citecheck.py — citations against the
              register; housestyle.py — prose conventions
docs/         worked example, comparative regimes, the correction record and review findings
```

### `data/provisions.yaml`
Verified statutory text with provenance. Every provision records whether it was amended by **Regulation (EU) 2026/1744** (the Digital Omnibus on AI), taken from the EUR-Lex change markers themselves rather than inferred from commentary. Extracted from the consolidated text at CELEX `02024R1689-20260727`; recitals from the authentic OJ text at `32024R1689`, the consolidated version omitting them.

Every entry carries a `provenance` field and a `verified` date, because for a while they were not all obtained the same way. Fourteen were taken from a published reproduction of the authentic text while EUR-Lex was unreachable from the machine this was built on, and carried `amended_by_omnibus: "unverified"` rather than a guess. All fourteen have since been checked against the consolidated PDF: thirteen matched verbatim, and one differed by a single stray full stop that turned out to be the Regulation’s own. The history is left in the file rather than tidied away, because a register that never says how it was built is asking to be trusted.

`imported_provisions` holds provisions of other instruments that the Act imports by reference and that the analysis relies on the text of—at present the CER Directive, reached through Article 3, point (62). They are verified against the authentic Official Journal text and cited in prose with the instrument named, which is both how the checker tells them apart and how a reader should have been able to tell all along.

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
- **And no verdict carries a conclusion of law.** The openers are an allowlist, which governs how a sentence starts and says nothing about what it goes on to do. A verdict reading “this appears met: the obligations attach” keeps register while borrowing the record’s authority for an argument no record can support. Whether the law reaches the facts belongs in a field of its own, where a reader can see it is reasoning. The threshold row said exactly that, through two rebuilds, until a blocklist was written to sit beside the allowlist
- Every provision and source reference resolves
- Every source carries a tier, a date, and a **pinpoint** URL (bare domains are flagged)
- Every row states facts to derive its verdict from
- Every unresolved row carries a route to settlement **and** a dated negative-search note—so that “the record is silent” is something demonstrated rather than assumed

## What the citation checker checks

- Every Article and Recital cited anywhere in the prose resolves to text in `data/provisions.yaml`
- Register entries nothing cites are reported, so the register does not accumulate dead weight

It deliberately skips two things, and both exclusions are substantive. Citations qualified by an instrument the register does not hold—the Charter, the Californian and New York statutes—are not its to check. And a span of bare article numbers (“Articles 51 to 56”) names a body of provisions rather than a piece of text: the claim that Chapter V runs from 51 to 56 rests on Article 113, which is verified, not on the last article in the span, which nothing quotes.

The **CER Directive is the exception, and it earned it**. The Act’s definition of ‘critical infrastructure’ resolves into it, and relying on an imported definition is still relying on text—three of the six recorded errors came from reading a summary of that Directive rather than the Directive. So `imported_provisions` holds the verified CER text, citations qualified `CER` resolve against it, and prose that cites the Directive without saying which instrument it means is reported rather than waved through.

What it cannot do is check that a citation is *apposite*. A pinpoint that resolves to verified text can still be the wrong provision for the proposition. One failure mode is closed; the other is still a reader’s job.

## What this repository does not contain, by choice

The exploit chain in the July 2026 intrusion is already public, published by the affected party in its own technical timeline. This repository **cites it by reference and does not reproduce payloads, injection strings, or a consolidated reconstruction of the escalation path.**

That is a deliberate call rather than an oversight. The same facts scattered across a vendor blog post and an incident timeline are a different artifact from those facts assembled, ordered and annotated in one convenient place—the assembly is the part that adds operational value, and this document’s purpose is regulatory analysis, for which the category of vulnerability suffices and the working detail does not. The sprint’s own guidance asks that novel installation recipes not be published without review; the same spirit is applied here to aggregation.

## Status and limits

Prepared over a sprint weekend by one person. Specific limits:

- **The author is not a lawyer.** The statutory text is verified against primary sources; the reasoning from it is an outsider’s, offered as a method to be checked rather than advice to be relied on.
- **The record is live and moving.** Every negative-search note carries an as-of date for this reason. Several underlying facts were days old when this was written.
- **The Regulation has two small slips in it, and this register keeps them.** Article 101(1) reads “whichever is higher., when the Commission finds”, and its closing subparagraph reads “The Commission shall also into account commitments made”, a verb short. Both stand in the authentic OJ text and the consolidated text alike. Nothing turns on either—each reads only one way—but an earlier version of this register had silently tidied the first, and tidying the enacting text is the small version of the thing this project is against.
- **Two designations remain unreconciled.** The model responsible for the majority of the attacking agents is named differently in the provider’s account and in the independent investigation, and this repository does not assert that they are the same model—establishing that is Request 1 of the instrument.

## Licence

Prose, data and the model instrument: **CC BY 4.0**. Code in `tools/`: **MIT**. See `LICENSE`.

The model instrument in `instrument/` is a **draft**. It has not been issued by, adopted by, or submitted to any Union body, and all fields requiring an issuing authority are left as explicit placeholders so that it cannot be mistaken for an issued document.
