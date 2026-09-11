# The Method
*Abstracted from the worked example, so it can be run on the next incident rather than only this one.*

---

## The claim, and its ceiling

The method answers one question: **does the discloser's own account, taken on its own terms, resolve this statutory obligation?**

It does not answer what happened. It cannot, and the moment it pretends to, it loses the property that made it worth doing — that it can be built on accounts published by parties with a stake in how those accounts read, without vouching for any of them.

This ceiling is the method. Everything below is machinery for not exceeding it.

## Why an outsider can run this at all

Compliance analysis from public records is ordinary work in other sectors — civil society, journalism, academic audit — and it does not require standing, access, or a practising certificate. What it requires is that the analyst be scrupulous about the difference between *the record does not resolve this* and *this did not happen*, and that the difference be visible to the reader rather than held privately by the author.

## Step 1 — Establish the statutory foundation from primary sources

Explainer sites are a research aid, not a citation. Two failures follow from citing them:

1. **Amendment drift.** An explainer may predate an amending act. Pull the consolidated text and read the change markers directly — EUR-Lex marks amended passages `▼M1` and base text `▼B`. Record amendment status per provision, as `data/provisions.yaml` does.
2. **Lost structure.** Summaries flatten things that carry the argument. In the worked example, the summary of one limb of the serious-incident definition dropped an irreversibility qualifier that appears in one limb and not its neighbour — which turned out to determine which limb the incident actually fell under.

Consolidated texts typically **omit recitals** and carry a notice that they have no legal effect. Take recitals from the authentic publication and say so once in the citation note.

Follow every cross-reference out of the instrument and into whatever it points at. In the worked example a definition resolved into a different directive, where the defined term turned out to be **functional** rather than designation-based — the opposite of what the summary implied, in the direction that mattered.

## Step 2 — Build the gating logic before populating anything

Obligations are not independent rows. Some gate others; some are unconditional. Draw the tree first, because it determines which questions are even askable and which incident each belongs to.

The structural insight worth transplanting: **find the obligations that do not depend on the contested classification.** A report staking everything on a disputed threshold inherits the dispute. Obligations that bite regardless — evaluation duties, risk-assessment duties, security duties, documentation duties — produce findings that stand however the contested question resolves. Build those first. They are the ones that cannot be argued away.

Look also for obligations with **determinate deadlines**. Vague standards ("without undue delay") produce arguable findings; fixed periods ("within two weeks") produce resolvable ones. A single resolvable question is worth more than several arguable ones, and the resolvable question is often in a neighbouring article rather than the obvious one.

## Step 3 — Tier the evidence by relationship, not prestige

| Tier | Relationship to the claim |
|---|---|
| T1 | The party whose conduct is in question, on its own conduct |
| T2 | The affected party's forensic account |
| T3 | An investigator operating under access constraints imposed by the subject |
| T4 | An independent third party |

A verdict resting only on T1 must read more hedged than one corroborated at T4, and the table should make that visible rather than leaving the reader to work it out.

Tier attaches to the source's position, not its reputation. **Apply this symmetrically.** Where more than one party's self-report appears, all sit at T1 and all carry the same reservations. A register that quietly treats one organisation's self-account as more reliable than another's has stopped being a method.

T3 deserves particular care: an investigation commissioned or access-scoped by its subject is not independent, however capable the investigators, and its own stated caveats about what it could not see belong in the record alongside its findings.

## Step 4 — Split facts from characterisation

Every row records two things separately:

- **Disclosed facts** — counts, dates, mechanics, what the record says occurred
- **The provider's characterisation** — how the discloser *labelled* those facts

**Verdicts derive from the facts column only.** A characterisation is an interpretation, frequently of the very ambiguity under test; feeding it into a verdict re-derives the provider's conclusion under new letterhead.

The characterisation column is not discarded. It is analysed separately, and it is often where the sharpest finding lives — a classification choice that determines which statutory pathway engages is itself the phenomenon worth reporting.

## Step 5 — Write verdicts in one of three registers, and nothing else

> "On the provider's own account, this appears **met**, because…"
> "On the provider's own account, this appears **unmet**, because…"
> "The disclosed record **does not resolve** this; it would require…"

Repetitive on purpose. The repetition is what makes the discipline auditable instead of aspirational, and it is checked mechanically by `tools/validate.py` rather than trusted.

## Step 6 — Prove absences rather than asserting them

Any unresolved row carries:

- **what would settle it** — the specific artifact or answer
- **what would not settle it** — the plausible non-answer, named in advance
- **a dated negative-search note** — *"as of [date], no source in [X] states [Y]"*

The third matters most. Without it, "the record is silent" means only "we did not find it," and a request that asks for something already public is the fastest way to lose a reader who knows the material. Write these **as you go**; by hour twenty nobody remembers which searches were actually run.

Naming the non-answer in advance is what converts a request from a question into an instrument: it closes the obvious evasion on the face of the document.

## Step 7 — Let the instrument fall out of the unresolved rows

Every unresolved row is already a question with a settlement condition attached. Drafting the request is then assembly rather than invention.

Two drafting rules earn their place:

1. **Operative voice.** Write the document the authority could send, not a memo recommending they send one. The first is usable with light edits; the second is commentary from outside the machinery.
2. **Follow the instrument's own required form.** Most information-gathering powers specify what a valid request must contain. Meeting that specification exactly is most of what "usable with light edits" means in practice.

And state plainly, in the instrument, that no finding has been made. A request premised on an unproven conclusion is one a lawyer rejects on sight; a request that asks is one they can act on.

## Step 8 — Mark provenance so the draft cannot be mistaken for the real thing

An instrument written in operative voice reads like an issued document, because that is the point. Therefore: an unmissable provenance header, no letterhead, no signature block, and **explicit placeholders rather than plausible values** for reference number, date and signatory.

Beyond the obvious reason, this is better craft. An authority adapting the draft wants to see exactly which fields are theirs to complete.

---

## Running this on something else

The structure is regime-agnostic. To apply it to a different instrument or a different incident:

1. Replace `data/provisions.yaml` with the target regime's provisions, extracted from primary sources with amendment status recorded.
2. Redraw the gate tree — the gating relationships are specific to each regime, and this is the step that cannot be skipped or inherited.
3. Rebuild `data/sources.yaml`, tiering by relationship to the claim.
4. Populate rows, unconditional obligations first.
5. Run `tools/validate.py`. It is regime-agnostic; it checks the discipline, not the law.
6. Draft the instrument from the unresolved rows, in the form the target regime's own procedural provision specifies.

The validator is the portable part. The law changes; the failure modes — dangling citations, unproven absences, verdicts that drift into assertion, a provider's framing smuggled in as a finding — do not.
