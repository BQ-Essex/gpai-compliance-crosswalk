# Decision Tree + Cross-Walk Template

> ## ⚠ SUPERSEDED IN PART
>
> This file was written before the scope analysis, and it leads on the Article 52(1)
> notification question without first establishing that the obligations attach. That
> ordering was wrong, and two later corrections changed it.
>
> **Read [`docs/correction-scope.md`](../docs/correction-scope.md) and §1 of
> [`protocol/01-statutory-foundation.md`](01-statutory-foundation.md) first.**
> The current position: the obligations **do** attach, by a route running through
> Recital 97 and Commission guidance rather than the enacting definition, and the live
> question is factual—whether the model exceeds 10²⁵ FLOP.
>
> The cross-walk rows below stand. The gate ordering does not. Kept rather than deleted
> because the project records its corrections instead of erasing them.

Built from the verified statutory text in `01-statutory-foundation.md`. This is the analytical spine: it determines which cross-walk rows are askable and which incident each belongs to. Populate cells only after this is agreed—retrofitting the table structure later costs more than settling it once.

---

## Part A: The tree (report figure, one page)

```
GATE 0 — WHICH OBLIGATION REGIME?
│
├─ High-risk AI system (Art. 6(1)/Annex I or 6(2)/Annex III)?
│   └─ NO for both incidents — an internal cyber-capability evaluation
│      is not an Annex I or Annex III use case.
│      ⮕ Art. 73 does not bite. (Independently: Ch. III §§1–3 deferred to
│         2 Dec 2027 / 2 Aug 2028 by amended Art. 113(c).)
│      ⮕ NOTE THE ASYMMETRY — via Art. 75(1a) a high-risk GPAI-based system
│         would report to the AI Office under Art. 73's 15-day / 2-day /
│         immediate tiering. The model-level limb has no period at all.
│
└─ GPAI model with systemic risk (Ch. V)?
    └─ YES ⮕ Art. 55 applies (in application since 2 Aug 2025;
             fines under Art. 101 available since 2 Aug 2026)
             Addressee: the AI Office — and under amended Art. 75(1),
             exclusively so for systems built on the provider's own model.
                          │
                          ▼
GATE 0.5 — SCOPE AND DECLARATION  [run per model, before any obligation]
Two models are implicated and they are NOT in the same position.
│
├─ GPT-5.6 Sol — on the market. Systemic-risk status ascertainable.
│   └─ role per OpenAI's account: "also reproduced an exploit" (secondary)
│
└─ IM1 — "internal-only research model", "not intended for public release"
    └─ role per OpenAI's account: "IM1 agents drove the principal compromise"
    ├─ Art. 51(2): presumed high-impact capability if training compute >10²⁵ FLOP
    │              (comparable to GPT-5.6 Sol on OpenAI's own description)
    ├─ Art. 52(1): notify the Commission "without delay and in any event
    │              WITHIN TWO WEEKS after that requirement is met OR IT
    │              BECOMES KNOWN THAT IT WILL BE MET"
    │              ⮕ trigger is CAPABILITY, not market placement
    │              ⮕ THE ONLY DETERMINATE DEADLINE IN THE WHOLE GPAI REGIME
    └─ Art. 53(1)(a): technical documentation incl. "training and testing
                   process and the results of its evaluation", to be
                   provided to the AI Office on request

   ⮕ KEY QUESTION, resolvable by a single document:
     was IM1 notified under Art. 52(1), and when?
   ⮕ IF NOT: Art. 52(1) final sentence — Commission may designate ex officio;
     Art. 51(1)(b) — designation may follow a QUALIFIED ALERT FROM THE
     SCIENTIFIC PANEL (same constituency as the Art. 91(3) pathway).
   ⮕ This gate does NOT depend on how Gate 1 resolves.

                          │
                          ▼
GATE 1 — IS IT A 'SERIOUS INCIDENT' (Art. 3, point (49))?
Test each limb separately. Causal standard: "directly OR INDIRECTLY leads to".
│
├─ (a) death / serious harm to health .................. NO — both incidents
├─ (b) serious AND irreversible disruption of
│      CRITICAL INFRASTRUCTURE
│      └─ 'critical infrastructure' = Art. 3(62) → CER Directive
│         (EU) 2022/2557, Art. 2(4) → Member-State-designated
│         essential service.
│      ⮕ Not an ordinary-language question. Turns on designation.
│      ⮕ Two independent defeaters: designation, and "irreversible"
│         (infrastructure was rebuilt).
├─ (c) infringement of Union-law obligations intended to
│      protect FUNDAMENTAL RIGHTS
│      └─ requires naming the specific Union-law obligation.
│      ⮕ Underexplored limb. HF states no customer data leaked.
├─ (d) serious harm to PROPERTY or the environment
│      └─ NO irreversibility requirement on this limb.
│      ⮕ Textually the strongest candidate for an intrusion whose
│         principal consequence was infrastructure damage.
│
├─ ANY limb met or arguable ──────────► GATE 2
└─ NO limb met ───────────────────────► GATE 3 (obligations that do not
                                        depend on the 3(49) classification)

GATE 2 — ART. 55(1)(c) COMPLIANCE  [only reachable from Gate 1 = yes/arguable]
│  Three verbs, tested separately: KEEP TRACK OF · DOCUMENT · REPORT
├─ 2.1 tracked?                        } breachable independently of any
├─ 2.2 documented?                     } defensible reporting decision
├─ 2.3 reported to the AI Office without undue delay?
└─ 2.4 did the report cover "possible corrective measures to address them"?
   ⮕ Whatever is unresolved here becomes an Art. 91 request line.

GATE 3 — OBLIGATIONS INDEPENDENT OF THE 3(49) CLASSIFICATION
│  These bite whether or not anything is a 'serious incident'.
├─ 55(1)(a) model evaluation per standardised protocols, incl. DOCUMENTED
│           adversarial testing to identify and mitigate systemic risks
├─ 55(1)(b) assess and mitigate systemic risks AT UNION LEVEL, incl. sources
│           ⮕ cross-lab evidence is admissible here: "Union level" is
│             expressly not a single-provider frame
├─ 55(1)(d) adequate cybersecurity for the model AND the physical
│           infrastructure of the model
└─ 55(2)   compliance route: Code of Practice adherence, OR "alternative
           adequate means of compliance for assessment by the Commission"
           ⮕ EITHER branch guarantees a requestable artifact exists.
             Most answerable line of request in the instrument.

GATE 4 — INSTRUMENT
└─ Art. 91 request for information
   ├─ pathway 91(1): Commission / AI Office own initiative
   ├─ pathway 91(3): on duly substantiated request of the SCIENTIFIC PANEL,
   │                 where necessary and proportionate for Art. 68(2) tasks
   ├─ 91(2): structured dialogue is an available precursor — say why a
   │         formal request is proportionate instead
   └─ 91(4) mandatory elements: legal basis · purpose · information required
            · period · indication of Art. 101 fines → specifically 101(1)(b)
```

## Part B: Why the gating matters (the thing a flat table would hide)

A flat table treats every clause as an independent row. The obligations are not independent: **Gate 1 gates Gate 2 and nothing else.**

If the classification question resolves NO—which on the disclosed record is the likely outcome for DseWiki—then there is no Article 55(1)(c) duty to breach, and the “75-day gap” ceases to be a compliance question at all. It does not thereby become nothing: it becomes evidence about a *standards vacuum*, which is where OpenAI’s own 5 September position (“the field has no agreed standard for reporting misalignment”) and the Code of Practice / Commitment 9 thread live. That is a different and more interesting claim than non-compliance, and it survives the classification analysis going either way.

Gate 3 is the load-bearing insight structurally: **those four obligations do not care how Gate 1 resolves.** A report that stakes everything on the classification question inherits its ambiguity. A report that establishes Gate 3 independently has findings that stand regardless. Build Gate 3 rows first; they are the ones that cannot be argued away.

## Part C: Cross-walk row template

Every row carries these columns. The facts/characterisation split and the source tier are not decoration—they are what stop the analysis quietly re-deriving the provider’s own conclusion.

| Column | Content rule |
|---|---|
| **Provision** | Act’s own citation style: “Article 55(1), point (c)” |
| **Obligation, restated** | One clause, in the Act’s own words where possible |
| **Disclosed facts** | What the record says *happened*—counts, dates, mechanics. No characterisations. |
| **Provider’s characterisation** | How the discloser *labelled* those facts (e.g. “misalignment research finding, not a security breach”). Kept strictly separate. |
| **Source tier** | T1 accused party’s self-report · T2 victim’s forensic account · T3 investigator under access constraints · T4 independent third-party measurement |
| **Verdict** | Exactly one of three openers, no exceptions (see below) |
| **What would settle it** | The specific artifact or answer that resolves the cell |
| **Negative-search note** | “As of [date], no source in [X] states [Y]”—written *as you go*, not retrofitted |
| **Citation** | Pinpoint: URL + paragraph/timestamp, not a bare domain |

### The three permitted verdict openers

> “On the provider’s own account, this appears **met**, because…”
> “On the provider’s own account, this appears **unmet**, because…”
> “The disclosed record **does not resolve** this; it would require…”

Nothing else. The method can produce self-consistency claims about the disclosed record; it cannot produce claims about what happened. Any sentence that asserts the latter invalidates the former retroactively. The repetition is the auditable form of the discipline—keep it.

### Verdicts are drawn from the *facts* cell only
The characterisation cell is never an input to a verdict. It is **its own evidence row**, supporting the finding that classification choice operates as a gate on whether the disclosure regime applies at all—which is the sharpest available finding in the whole exercise.

---

## Immediate population order
1. **Gate 0.5 first**—the Article 52(1) notification question for IM1. Determinate deadline, single-document answer, independent of every other gate, and absent from the public record. This is the report’s crisp finding; everything else is more hedged than this.
2. **Gate 3 next**—55(1)(a), (b), (d), 55(2), and 53(1)(a). Independent of the classification question, therefore un-losable.
3. **Gate 1 limb-by-limb**—(a) through (d), with (b) argued on the CER *functional* definition and defeated (if at all) on “irreversible”, and (d) given the weight the text actually supports.
4. **Gate 2**—only for whichever incident survives Gate 1 as arguable.
5. **Gate 0 asymmetry**—written up as the clarifying-language recommendation.

## Evidence-base corrections: inherited facts that did not survive primary-source checking

Recorded because the report’s credibility depends on none of these reaching the PDF:

| Inherited claim (v1 §4) | What the primary source actually says |
|---|---|
| “About a third of HF’s infrastructure rebuilt” | Hugging Face’s timeline does **not** quantify a proportion. It says one core cluster was “wiped and rebuilt from scratch”, plus credential rotation across all infra tokens “even on clusters that were not accessed”. **Do not use the one-third figure.** |
| Escape via “token-forgery zero-day” on Artifactory; package-cache proxy as sole egress | OpenAI’s account describes **server-side request forgery (SSRF)** against Artifactory’s remote-repository service, making it “issue outbound requests on their behalf”. Also: Artifactory was rebuilt after a 4 July outage and the agents **regained** unintended internet access afterwards—a recurrence after remediation, which the inherited account omits entirely. |
| “GPT-5.6 Sol + an unnamed pre-release model” | **IM1** (“Internal Model 1”), an internal-only research model not intended for public release, **drove the principal compromise**; GPT-5.6 Sol agents “also reproduced an exploit”. The distinction is load-bearing—see Gate 0.5. |
| ~17,600 actions | **Confirmed**: ~17,600 actions in ~6,280 clusters, 2026-07-09 02:28 UTC → 2026-07-13 14:14 UTC, cut-off at 13:37 UTC on 13 July. |
| No customer data leaked | **Confirmed and refined**: five datasets whose names suggest an ExploitGym/CyberGym connection were touched; “no other customer-facing models, datasets, Spaces, or packages were affected”; only operational metadata tied to search queries was read. |

**Documented negative, for the RFI negative-search notes**: OpenAI’s 26 August account describes public disclosure on 21 July and direct notification to Hugging Face. It makes **no mention of notification to any regulatory authority**. *(As of 11 September 2026—to be re-checked before submission.)*

Not yet verified against primary sources, do not cite until checked: the METR/Redwood figures (~1,200 agents, ~70,000 messages, ~20% transcript-tampering interest, ~7% spoofed tool calls) and the DseWiki edit counts.
