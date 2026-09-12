# Decision tree and cross-walk template

The analytical spine. It determines which questions are askable, in what order, and against which model. Settle it before populating cells—retrofitting the table structure later costs more than designing it once.

Rebuilt 12 September 2026. Two earlier versions of this file led on Article 52(1) notification, then on exclusion by definition. Both were wrong, and the corrections are recorded in [`docs/correction-scope.md`](../docs/correction-scope.md) rather than erased.

---

## Part A: the tree

```
THRESHOLD QUESTION — do the obligations attach at all?
Run this per model, before any obligation is analysed.
│
│  Two models are implicated and they are not in the same position.
│  · GPT-5.6 Sol — on the market. ~5% of attacking agents. Chapter V plainly applies.
│  · The research model (IM1 / HPIM) — internal, never released. ~95% of agents.
│    Everything below concerns the second.
│
├─ THE TEXTUAL READING, available to a provider
│   ├ Art. 2(1)(a): AI SYSTEMS caught on placing on the market OR putting into
│   │   service — and Art. 3(11) 'putting into service' includes supply "for own
│   │   use". GPAI MODELS are caught only on placing on the market, which Art. 3(9)
│   │   defines as first making available and Art. 3(10) ties to supply "in the
│   │   course of a commercial activity".
│   ├ Art. 3(63): the definition of 'general-purpose AI model' excludes models
│   │   "used for research, development or prototyping activities before they are
│   │   placed on the market". No "sole purpose" qualifier. No conditions.
│   └ Art. 2(8): the Regulation does not apply to pre-market research, testing or
│       development activity. Its one exception — testing in real-world conditions,
│       Art. 3(57) — describes an ELECTED activity: temporary, for an intended
│       purpose, outside a laboratory by design, under Art. 57 or 60 conditions.
│       An escape from a sandbox is not that. And the conditions it defers to do
│       not reach a model at all: Art. 57 governs national sandboxes a provider
│       ENTERS; Art. 60 is confined on its face to HIGH-RISK AI SYSTEMS. The one
│       carve-back has no purchase on a general-purpose AI model.
│   ⮕ On this reading the obligations do not attach, and nothing lets them back in.
│
└─ THE COMMISSION'S READING, which governs enforcement
    ├ Recital 97, reproduced at Guidelines ¶54: where a provider "integrates an own
    │   model into its own AI system that is made available on the market or put into
    │   service, that model should be considered to be placed on the market".
    ├ Guidelines ¶51: use for "internal processes that are essential for providing a
    │   product or service to third parties or that affect the rights of natural
    │   persons in the Union" is itself an example of placing on the market.
    ├ Guidelines ¶22: the lifecycle begins at the start of the large pre-training
    │   run; development before or after market placement is the SAME model's
    │   lifecycle; "different stages of the development of a model are not considered
    │   to constitute different models". With Recital 97's closing sentence, the
    │   research exclusion protects a model NEVER placed on the market — not the
    │   development phase of one that is.
    └ Commission Q&A: the internal-use exception has three cumulative conditions, the
        third being that the model is NOT a GPAI model with systemic risk.
    ⮕ The obligations attach.

                              │
                              ▼
RESOLUTION
  The obligations attach. The weight-bearing step sits in a recital and in guidance,
  not in the enacting definition — and that is the finding, not a footnote to it.
  Note HOW Recital 97 does it: not by excepting Art. 2(8), but by moving the moment
  of placement, so the development was never activity 'prior to' placement and
  Art. 2(8) never engages. A recital fixing the point from which enacting terms run.
  Guidelines ¶9: "not binding … Nevertheless … the Commission's interpretation and
  application of the AI Act, on which it will base its enforcement action."
  Determines what the Commission does. Open to challenge before the CJEU.
                              │
                              ▼
THE FACTUAL QUESTION — the only one left, and the only resolvable one
  Does the model exceed 10²⁵ FLOP (Art. 51(2))?
  If yes → Art. 52(1) notification "without delay and in any event within two weeks
           after that requirement is met or it becomes known that it will be met" ran
           DURING DEVELOPMENT. The only determinate period in the chapter.
           Arts. 53 and 55 applied throughout.
  If no  → most of the analysis falls away. Say so.
  ⮕ Instrument Requests 1–5.
                              │
                              ▼
THE OBLIGATIONS, once attached — none of these turn on Art. 3(49)
  ├ 55(1)(a) evaluation per standardised protocols, incl. DOCUMENTED adversarial testing
  ├ 55(1)(d) cybersecurity — Recital 115 enumerates what it must "duly consider",
  │          including "circumvention of safety measures"
  ├ 55(2)    Code of Practice branch, or "alternative adequate means for assessment by
  │          the Commission" — either branch guarantees a requestable artifact
  ├ 53(1)(a) technical documentation incl. training and testing process, to the AI
  │          Office on request — named expressly in Art. 91(1)
  └ 55(1)(b) systemic risk "that may stem from THE DEVELOPMENT, the placing on the
             market, or the use" — in the ENACTING TEXT, not a recital.
             ★ This one holds even on the provider-favourable reading above, because
               the deployed model is indisputably in scope and its provider owed a duty
               to assess risk stemming from development.
                              │
                              ▼
SEPARATE GATE — only for the reporting limb at Art. 55(1)(c)
  Is it a 'serious incident' within Art. 3, point (49)?
  Causal standard "directly OR INDIRECTLY". Limbs disjunctive.
  ├ (a) death / serious health harm ............ not engaged
  ├ (b) serious AND IRREVERSIBLE disruption of critical infrastructure
  │      'critical infrastructure' → Art. 3(62) → CER Dir. Art. 2(4): functional,
  │      tied to an essential service (CER 2(5)), whose list is the Commission's and
  │      is NON-EXHAUSTIVE (CER 5(1)); then requires disruption
  │      of "the management or operation of" it. Rebuilding defeats "irreversible".
  ├ (c) infringement of Union-law fundamental-rights obligations ... does not resolve
  └ (d) serious harm to PROPERTY — NO irreversibility requirement — does not resolve
  ⮕ Bridging gap to state, not assume away: Art. 3(49) is defined by reference to an
    AI SYSTEM (Art. 3(1)); Art. 55(1)(c) binds providers of MODELS.
  ⮕ And 55(1)(c) supplies no period at all — only "without undue delay".
  ⮕ BUT the Code of Practice does, for a Signatory. Measure 9.3: 2 days (critical
    infrastructure), 5 DAYS (serious cybersecurity breach, incl. (self-)exfiltration
    of model weights and cyberattacks), 10 days (death), 15 days (health, rights,
    property). The 5-day limb has NO counterpart in Art. 3(49). Clock runs from
    awareness, on "establish OR SUSPECT with reasonable likelihood".
  ⮕ The Code does not define 'serious incident' and does not cite Art. 3(49) at all,
    so for a Signatory the bridging gap above stops being the operative question.
                              │
                              ▼
THE INSTRUMENT — Art. 91 request for information, issued by THE COMMISSION
  Art. 3(47): the AI Office is "the Commission's function", not a legal person.
  ├ 91(1) Commission on its own initiative
  ├ 91(3) on a duly substantiated request from the scientific panel (see Art. 90)
  ├ 91(2) structured dialogue is an available precursor — say why a formal request
  └ 91(4) required form: legal basis · purpose · information specified · period ·
          indication of Art. 101 fines → specifically Art. 101(1)(b)
  ⮕ Art. 101 applies only from 2 Aug 2026 (Art. 113(b); Guidelines ¶112). No
    101(1)(a) exposure for conduct predating it. 101(1)(b) is unaffected.
```

## Part B: why the ordering matters

**Scope precedes everything.** The most expensive error available here is a rigorous analysis of obligations that never attached: the clause reasoning can be correct, the citations exact, the evidence properly tiered, and the whole structure still rest on a regime that does not reach the subject. This project made that error, then over-corrected into the opposite one.

**The two-readings structure is not hedging.** Setting out both is what makes the analysis usable by a regulator *and* honest about what a provider would say. A report that gives only the Commission’s reading is not wrong, but it cannot anticipate the answer it will get.

**Find the obligations that survive the contested question.** Article 55(1)(b) reaches development in the enacting text. It holds whichever way scope resolves, which makes it the most durable line of enquiry in the whole cross-walk and the reason the analysis has findings at all.

**One resolvable question beats several arguable ones.** The compute threshold is a single number that settles whether a fixed statutory period was engaged. Everything else here is a judgement.

## Part C: cross-walk row template

Every row carries these columns. The facts/characterisation split and the source tier are not decoration—they are what stop the analysis quietly re-deriving the provider’s own conclusion.

| Column | Content rule |
|---|---|
| **Provision** | The Act’s own citation style: “Article 55(1), point (c)” |
| **Obligation, restated** | One clause, in the Act’s words where possible |
| **Disclosed facts** | What the record says *happened*—counts, dates, mechanics. No characterisations. |
| **Provider’s characterisation** | How the discloser *labelled* those facts. Kept strictly separate. |
| **Source tier** | T1 accused party’s self-report · T2 affected party’s forensics · T3 investigator under subject-imposed constraints · T4 independent third party |
| **Verdict** | Exactly one of three openers, no exceptions |
| **What would settle it** | The specific artifact or answer |
| **What would not** | The plausible non-answer, named in advance |
| **Negative-search note** | “As of [date], no source in [X] states [Y]”—written as you go |
| **Citation** | Pinpoint: URL plus paragraph or timestamp, never a bare domain |

### The three permitted verdict openers

> “On the provider’s own account, this appears **met**, because…”
> “On the provider’s own account, this appears **unmet**, because…”
> “The disclosed record **does not resolve** this; it would require…”

Nothing else. The method produces self-consistency claims about a disclosed record; it cannot produce claims about what happened. Any sentence asserting the latter retroactively invalidates the former. The repetition is the auditable form of the discipline, and `tools/validate.py` enforces it rather than trusting it.

### Verdicts derive from the facts cell only

The characterisation cell is never an input to a verdict. It is analysed separately, and it is often where the sharpest observation sits.

## Part D: population order

1. **Threshold question first**—per model, both readings, before any obligation.
2. **The factual question**—the compute threshold, because it is the only resolvable one and everything downstream is conditioned on it.
3. **Obligations that do not turn on Article 3(49)**—55(1)(a), (b), (d), 55(2), 53(1)(a). Un-losable.
4. **Article 3(49) limb by limb**—only for the reporting limb, and in the alternative.
5. **The instrument**, assembled from whatever remains unresolved.
