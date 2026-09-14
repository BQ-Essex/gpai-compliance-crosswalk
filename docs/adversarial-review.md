# Adversarial review: findings

Two independent passes were run over the finished draft with no sight of the reasoning that produced it. Both were briefed on the target and the standard, neither on what the author believed the answers were. Recorded here because the report relies on them and because a method that claims to catch its own drift should show the catch.

*One of two records of the same review. This file is **what the passes found**; [`correction-scope.md`](correction-scope.md) is **the reasoning behind the one finding that restructured the report**. The canonical index of every error, including these, is the corrections log at [`protocol/01-statutory-foundation.md`](../protocol/01-statutory-foundation.md) §0.*

Date: 11 September 2026. Both findings were then verified directly against EUR-Lex, CELEX `02024R1689-20260727`, before being acted on.

---

## Pass 1: overclaim audit

**Brief**: hunt sentences that drift from *the disclosed record does not establish X* into asserting or implying *X happened*, given a method that explicitly disclaims the ability to make the latter claim.

**Result: eight instances, all upheld.**

| # | Location | Problem |
|---|---|---|
| 1 | Abstract, §4.4, §7 | “the classification **determined** which disclosure pathway engaged”—asserts a causal mechanism inside the organisation. The record contains two classifications and two outcomes. |
| 2 | §4.4 | “a taxonomy … is **gating a statutory duty**”—presupposes a duty was engaged, which §4.2 leaves unresolved |
| 3 | §4.6 | “the limb under which containment failures **fall**”—asserts they are serious incidents, contradicting §4.2 |
| 4 | §4.5 heading | “and **the failure** recurred”—reads as failure of the obligation; what recurred was unintended egress |
| 5 | §4.2 | “**Rebuilding defeats limb (b)**”—a flat legal conclusion in none of the three permitted registers |
| 6 | §4.3 | “resolvable … against a **fixed statutory period**”—presupposes the Article 51(2) presumption is engaged |
| 7 | §4.3 | “a question **nobody has publicly asked**”—broader than the dated negative search, which covered enumerated sources |
| 8 | §4.3 | “the objection … **does not survive** that drafting”—attributes to the provider a legal position it has not advanced |

**Clean on the specific trap it was set.** The auditor was told to check whether the interval between provider-attributed IP access on 21 June and public acknowledgment on 5 September was anywhere allowed to imply culpable delay. It found the framing correct throughout, matching the discipline note in the cross-walk and Request 11 in the instrument.

**Untraceable claims flagged**: the Cloud Security Alliance note; the coalition letter to the Commission; the SB 53 and RAISE Act figures; “dormant” as a description of the wiki; and the instrument’s “publicly disclosed by the affected party on 16 July 2026”, which the source register does not carry.

---

## Pass 2: hostile legal review

**Brief**: a sceptical EU technology regulation lawyer, told the author is not a lawyer, asked to find errors before the document reaches a regulator, and asked to verify against primary sources rather than trust the author’s extraction.

### Upheld as wrong

**Article 73(4) mis-transcribed.** Recorded as “immediately” for incidents involving death; the text reads “not later than **10 days**”. “Immediately” is the floor in each tier, not the limit. The report proposed importing the very provision it had mis-stated.

**Article 2(8) never consulted.** “This Regulation does not apply to any research, testing or development activity regarding AI systems or AI models prior to their being placed on the market or put into service.” The draft’s entire answer to the development-stage objection was Recital 115—and a recital has no autonomous binding force and cannot derogate from enacting terms (*Nilsson* C-162/97; *Manfredi* C-308/97; *Tyson Parketthandel* C-134/08).

**“Trigger is capability, not market placement” overstated.** Article 52(1) binds “the relevant **provider**”; Article 3, point (3) ties provider status to placing on the market. The temporal trigger is capability; standing is not. Instrument Requests 3–4 pre-emptively marked “not placed on the market” as non-responsive, excluding what may be the correct answer.

**Instrument vested the power in the wrong body.** Article 91(1) and (3) empower the Commission. Article 3, point (47) makes the AI Office “the Commission’s function”, not a legal person. As drafted for the Office it was ultra vires on its face.

**Internal contradiction.** The foundation listed Code of Practice signatory status as unverified; the instrument asserted it as fact.

**Article 101 non-retroactivity unaddressed.** Article 101 has applied only since 2 August 2026; both episodes predate it. The comparative appendix’s claim of 3%/€15m exposure for the underlying conduct was unavailable on these facts. Article 101(1)(b) survives.

**The Article 55(1)(c) tiering proposal was self-defeating.** The two-day tier attaches only to Article 3(49)(b); on facts sitting in limb (d), importing the scheme yields the 15-day tier—the slowest available.

### Upheld as overstated

- **The CER correction over-corrected.** ‘Essential service’ is not at large. *(This bullet was itself wrong, and is corrected in the foundation’s log as error six: CER Article 5(1) empowers the Commission, not Member States, to draw up a non-exhaustive list of essential services, and the Annex’s third column lists categories of entities rather than services. The bullet’s conclusion survives; its reasoning did not.)* Article 3(49)(b) also requires disruption of “the management or operation of” that infrastructure.
- **Limb (d) was asserted, not argued.** Whether rebuilt clusters and rotated credentials are harm to *property* rather than service disruption and remediation cost, and whether “serious”, was unanalysed.
- **The Article 73 exclusion reached the right answer by the weaker route.** The decisive points are Article 73(1)’s “placed on the Union market” and Article 2(8), not the absence of an Annex I or III classification.

### Verified correct, and left alone

The two-week period at Article 52(1); Article 55(1)(c) as “without undue delay” only; limb (b)’s irreversibility requirement against limb (d)’s absence of one; Article 3(62)’s functional cross-reference and the designation point; the Article 113 derivation of the 2 August 2025 and 2 August 2026 dates; Article 75(1a)’s insertion and effect; and every Recital 115 quotation word for word.

### Strongest unengaged argument, as put

Article 2(8) excludes pre-market testing; Articles 2(1)(a) and 3(3) mean a developer is not a “provider” of a never-marketed model, so Articles 51–55 and 101 do not attach; Article 3(49) defines ‘serious incident’ by reference to an **AI system**, not a model, so Article 55(1)(c) borrows a system-level definition these facts may not satisfy; Recital 115 cures none of it; the harm was third-party infrastructure remediated within days; and Article 101 was not in application.

### Presentation points taken

Harvard author–date for EU legislation reads as amateur—use OJ form with ELI. The declared citation convention was abandoned mid-report. Article 90 governs the qualified-alert pathway and was never cited. Article 91(3)’s cross-reference to Article 68(2) is a known drafting artefact (the panel’s tasks sit in 68(3)) and was reproduced without comment. Request 8 stated a preliminary view while the instrument disclaimed having formed one. Two response periods in one Article 91(4) request is irregular.

---

## What was done about it

Every “wrong” finding was verified against primary text and then acted on. The scope finding restructured the report: the question moved from *was notification made* to *do the obligations attach at all*, which is a larger gap and further upstream. See `correction-scope.md` for the reasoning and `protocol/01-statutory-foundation.md` §0 for the corrections log.

The eight overclaims were rewritten into the permitted registers. The instrument was reissued in the Commission’s name, its scope requests reframed to invite the addressee’s position rather than pre-empt it, its two response periods collapsed to one, and its Article 101 paragraph given a temporal-scope limitation.

One finding was not acted on. The reviewer suggested the phrase “no public disclosure until the day after independent publication” carries an implicature of compelled disclosure. The dates are given plainly in the table at §4.5 and the sequence is a fact about the record; stating it neutrally is not the same as suppressing it.
