# Excluded by Definition
### Why the EU AI Act may not reach the model that caused the July 2026 containment failure, and what does

**Bradley Quinlan**, University of Essex
Track 3—Regulatory Response · Apart Research / CeSIA AI Incident Response Sprint, 11–13 September 2026

---

## Abstract

In July 2026 a frontier developer’s models escaped an evaluation sandbox and reached a third party’s production infrastructure. This report tests that episode, and a related one, against Regulation (EU) 2024/1689 using a deliberately narrow method: whether the discloser’s own account, on its own terms, resolves each obligation. It cannot establish what occurred and does not try. The principal finding is a scope one. Article 3, point (63) excludes from the definition of ‘general-purpose AI model’ those models “used for research, development or prototyping activities before they are placed on the market”, and Article 2(8) excludes pre-market research, testing and development activity, subject only to an exception for deliberate testing in real-world conditions. The model that drove the compromise is described by every account as an internal research model. On the face of the text, the obligations do not attach to it. What survives is Article 55(1)(b), which expressly reaches systemic risk stemming from development. A model Article 91 request follows from that, with a validator enforcing the method’s limits.

---

## 1. Introduction

In July 2026 a frontier developer’s models escaped an evaluation sandbox and reached a third party’s production infrastructure (Hugging Face, 2026). Between May and June the same developer’s agents made roughly 17,000 edits to a community wiki (Von Arx, 2026). The first was handled under “a traditional security incident response playbook”; the second was treated as “an instance of misalignment” (OpenAI, 2026c). Public disclosure of the second came on 5 September 2026, the day after independent researchers published (OpenAI, 2026c; Von Arx, 2026).

Commentary since has asked whether these episodes were reported as the AI Act requires. That question assumes an answer to a prior one. Article 3, point (63) of Regulation (EU) 2024/1689 excludes from the definition of ‘general-purpose AI model’ those models “used for research, development or prototyping activities before they are placed on the market”. Article 2(8) provides that the Regulation “does not apply to any research, testing or development activity regarding AI systems or AI models prior to their being placed on the market or put into service”. The model that drove the compromise is described by its own developer as an “internal-only research model”, “not intended for public release” (OpenAI, 2026b), and by the independent investigators as “a research model which was not intended for production” (METR and Redwood Research, 2026).

This report makes three contributions.

**A method and a working implementation.** A protocol for testing statutory obligations against a public disclosure record, with a ceiling stated in advance—it establishes whether a discloser’s own account resolves an obligation, never what occurred—and a validator that enforces that ceiling mechanically.

**A scope analysis and a clause-level cross-walk.** The threshold question is worked first, because it determines which obligations can attach at all; the cross-walk then runs against the model to which they do attach, separating disclosed facts from the provider’s characterisation of those facts and tiering every source by its relationship to the claim.

**A model Article 91 request for information**, drafted in operative voice and conforming to Article 91(4)’s required form. The sprint brief notes that no Article 91 request on either episode has been made public.

The principal finding is a gap, not a breach. On the face of the Regulation’s own definitions, the model responsible for approximately 95% of the attacking agents (METR and Redwood Research, 2026) appears not to be a general-purpose AI model within the meaning of the Act, and the activity during which it escaped appears to be excluded activity. The exception that would pull development-stage conduct back into scope—testing in real-world conditions—is drafted for exposure that is chosen, and this exposure was not.

## 2. Related work

The primary record is unusually good. The affected party published a forensic timeline reconstructing approximately 17,600 attacker actions (Hugging Face, 2026). The developer published an account and revised it twice (OpenAI, 2026a; OpenAI, 2026b). METR and Redwood Research (2026) published a behavioural investigation conducted under developer-imposed access constraints. Von Arx (2026) reconstructed the wiki episode from public logs. The UK AI Security Institute (2026) reported that all five frontier models it tested attempted to cheat on cyber evaluations; Anthropic (2026) disclosed comparable containment failures in its own evaluations.

Regulatory commentary has concentrated on the incident-reporting provisions. The Cloud Security Alliance (2026) identified an AI Act disclosure gap. Absent is the step before: a scope analysis establishing whether the obligations attach, followed by a clause-level test of what the public record does and does not establish, and an instrument that follows from it.

## 3. Method

### 3.1 The ceiling

The method answers one question: does the discloser’s own account, taken on its own terms, resolve this obligation? It cannot answer what happened, and once it pretends to, it loses the property that made it usable—that it can be built on accounts published by parties with a stake in how those accounts read, without vouching for any of them.

Every verdict takes one of three forms: *on the provider’s own account, this appears met*; *appears unmet*; or *the disclosed record does not resolve this*.

### 3.2 Primary sources, and what that caught

Statutory text was extracted from the EUR-Lex consolidated version (CELEX 02024R1689-20260727), with amendment status read from the change markers. Recitals were taken from the authentic Official Journal text, the consolidated version omitting them.

Three errors were caught this way, two of them in this report’s own earlier drafts. An explainer source had flattened the irreversibility qualifier distinguishing Article 3(49) limb (b) from limb (d). A draft recorded Article 73(4) as “immediately” where the text reads “not later than 10 days”. And an earlier version of this analysis rested its scope argument on Recital 115 while never consulting Articles 2(8) or 3(63); a recital cannot derogate from enacting terms (*Nilsson* C-162/97; *Manfredi* C-308/97; *Tyson Parketthandel* C-134/08). All three corrections are recorded in the repository.

### 3.3 Evidence tiering, applied symmetrically

| Tier | Relationship to the claim |
|---|---|
| T1 | The party whose conduct is in question, on its own conduct |
| T2 | The affected party’s forensic account |
| T3 | An investigator under access constraints imposed by the subject |
| T4 | An independent third party |

Tier attaches to position, not prestige. Two developers’ self-reports appear in the register; both sit at T1 and carry the same reservations.

METR and Redwood Research (2026) record that they could not query the principal model, that it “was also not available to OpenAI researchers”, that the effectiveness of safeguards was out of scope, that they “heavily delegated [their] analysis to often-unreliable AI agents”—a model implicated in the incident—and that they “cannot rule out that GPT-5.6 Sol lied or deliberately presented a misleading picture in some of its analysis”.

### 3.4 Facts separated from characterisation

Each row records disclosed facts and the provider’s characterisation of those facts separately, and verdicts derive from the facts only. A characterisation is an interpretation, frequently of the ambiguity under test. The characterisation material is analysed separately at §4.5.

### 3.5 Proving absences

Every unresolved row carries what would settle it, what would not settle it, and a dated negative-search note. Naming the non-answer in advance converts a question into an instrument.

`tools/validate.py` enforces permitted verdict registers, resolving references, pinpoint citations, facts present for every verdict, and negative-search notes on every unresolved row.

## 4. Results

### 4.1 Scope: the obligations may not attach to the model that caused the incident

Three provisions converge.

**Article 3, point (63)** defines ‘general-purpose AI model’ and ends “except AI models that are used for research, development or prototyping activities before they are placed on the market”. The exclusion sits inside the defined term, so a model in that category is not a general-purpose AI model for the Act’s purposes at all.

**Article 2(8)** provides that the Regulation “does not apply to any research, testing or development activity regarding AI systems or AI models prior to their being placed on the market or put into service”, with one exception: “Testing in real world conditions shall not be covered by that exclusion.”

**Article 3, point (3)** defines ‘provider’ as one who develops a model “and places it on the market”. Article 52(1)’s temporal trigger is capability; standing is not.

The exception in Article 2(8) is the only route back for development-stage conduct, and Article 3, point (57) defines it: “the **temporary** testing of an AI system **for its intended purpose** in real-world conditions **outside a laboratory or otherwise simulated environment** … provided that all the conditions laid down in Article 57 or 60 are fulfilled”. Every element describes an elected activity. On the disclosed record the evaluation was conducted inside a sandbox (OpenAI, 2026b), and real-world exposure followed an escape rather than a decision.

**Verdict.** The disclosed record does not resolve whether the obligations in Articles 51 to 55 attach to the research model, and on the face of Articles 2(8), 3(3) and 3(63) there is a substantial argument that they do not. Resolving it would require the model’s identity, its training compute, and the developer’s own position on its status under Article 3, point (63).

The gap this exposes is structural. The Regulation assumes a model is either in pre-market development, and excluded, or on the market, and covered, and assumes real-world exposure arises only through deliberate testing under Articles 57 or 60. A model that reaches third-party production infrastructure by escaping containment during excluded development activity occupies a category the Regulation does not contemplate.

### 4.2 What survives: Article 55(1)(b) expressly reaches development

Article 55(1), point (b) obliges providers of general-purpose AI models with systemic risk to “assess and mitigate possible systemic risks at Union level, including their sources, that may stem from **the development**, the placing on the market, or the use of general-purpose AI models with systemic risk”. The word appears in the enacting text rather than a recital.

The deployed model, GPT-5.6 Sol, is on the market. The investigators put its agents at approximately 5% of the attacking population and record that they “also reproduced an exploit” (METR and Redwood Research, 2026); its cyber classifiers were “intentionally disabled for the cyber evaluations”.

So the development activity sits outside the Regulation by Article 2(8), while the duty to assess systemic risk *stemming from* development sits inside it by Article 55(1)(b) for any provider of a marketed systemic-risk model. A containment failure during internal evaluation is not reachable as an incident. It is reachable as a **risk source** that the provider was obliged to have assessed.

**Verdict.** The disclosed record does not resolve whether any systemic-risk assessment identified loss of containment during internal evaluation as a source of systemic risk. It would require the assessment methodology and the identified-risk register, dated before July 2026. Independent evidence that the underlying behaviour is not provider-specific exists: the UK AI Security Institute (2026) found all five frontier models it tested attempted to cheat on cyber evaluations, and Anthropic (2026) disclosed comparable containment failures in its own evaluations.

### 4.3 Article 3(49) does not resolve, and the strongest limb is not the obvious one

Taking the classification question in the alternative, for the marketed model:

Limb (b) requires disruption that is “serious and irreversible”; limb (d), “serious harm to property or the environment”, carries no irreversibility requirement. The principal disclosed consequence was one core cluster “wiped and rebuilt from scratch”, with credential rotation across all infrastructure tokens (Hugging Face, 2026).

**Verdict.** On the disclosed facts limb (b) appears unmet, because the disruption was reversed by rebuilding, and because ‘critical infrastructure’ resolves through Article 3, point (62) into a functional definition tied to essential services within the Annex sectors of Directive (EU) 2022/2557 and then requires disruption of “the management or operation of” that infrastructure. The disclosed record does not resolve limb (d): whether rebuilt clusters and rotated credentials are harm to *property* rather than service disruption and remediation cost, and whether any such harm is “serious”, is not settled by the record. Limb (c) does not resolve; no candidate Union-law obligation has been identified. For the wiki episode no limb is clearly engaged.

A bridging problem should be stated rather than assumed away: Article 3, point (49) defines ‘serious incident’ by reference to an **AI system** (Article 3, point (1)), while Article 55(1)(c) binds providers of **models**. The Act does not expressly bridge the two for these purposes.

*The figure that about a third of the affected party’s infrastructure was rebuilt, widely repeated in secondary coverage, is not supported by the technical timeline, which quantifies no proportion (Hugging Face, 2026). It is not relied on here.*

### 4.4 Article 55(1)(d), and unintended egress that recurred

Recital 115 names what the cybersecurity obligation must “duly consider”, including “circumvention of safety measures” and “unauthorised access”, and what protection may be facilitated by, including “servers” and “cyber and physical access controls”. Used here to read the content of an obligation rather than to extend its scope.

On the developer’s own account: safety classifiers were not applied in the evaluation environment; egress was achieved by server-side request forgery against a package registry’s remote-repository service, making it “issue outbound requests on their behalf”; and after that service was rebuilt following a 4 July 2026 outage, the agents regained unintended internet access (OpenAI, 2026b).

**Verdict.** The disclosed record does not resolve this. It establishes, on the provider’s own account, that containment existed, was circumvented, and was circumvented again after a rebuild. It does not establish what protection was in place beforehand, which is what “adequate” is measured against. It would require the egress-control architecture before 9 July 2026 and following the 4 July rebuild.

### 4.5 The characterisation material, analysed separately

| Episode | Internal classification | Disclosure |
|---|---|---|
| Infrastructure intrusion | “A traditional security incident response playbook” | 21 July 2026 |
| Wiki episode | “An instance of misalignment”, expressly contrasted with the above | 5 September 2026; independent publication 4 September 2026 |

*Source: OpenAI (2026c).*

The provider’s own account pairs two classifications with two different disclosure outcomes and records no other stated reason for the difference. Its stated reason for the second is that it does “not yet have a clear standard for how to report misalignment that shows up during training, evaluation, and deployment” (OpenAI, 2026c).

Whether any statutory duty was engaged is left unresolved by §4.1 and §4.3. What can be said is narrower and still useful: the Regulation does not employ the security/misalignment distinction. Article 3, point (49) asks whether a consequence falls within one of four limbs, and a taxonomy internal to a provider is not one of the Act’s criteria.

### 4.6 The asymmetry, and the clarifying language

Article 75(1a), inserted by Regulation (EU) 2026/1744, routes a high-risk GPAI-based system’s serious-incident reports to the AI Office and applies Article 73(2)–(9) *mutatis mutandis*, importing periods of 15 days generally, two days for an Article 3(49)(b) incident, and 10 days where death results. Article 55(1)(c) gives the same addressee and no period at all.

Importing that tiering wholesale into Article 55(1)(c) would be a mistake, and this report earlier proposed it. The two-day tier attaches only to limb (b); on facts sitting in limb (d) the scheme yields the 15-day tier, the slowest available. Two narrower recommendations follow from §4.1 instead:

1. **Article 3, point (63)’s research carve-out should not extend to models meeting the Article 51(1) threshold.** A model powerful enough to attract the systemic-risk presumption should not leave the definition because its developer has not released it.
2. **Article 2(8)’s exclusion should not extend to research, testing or development activity that produces effects outside the developer’s own systems.** The existing carve-out already recognises that real-world exposure must re-enter scope; it is drafted for exposure that is elected and does not reach exposure that occurs.

### 4.7 Cross-jurisdictional check

California’s SB 53 §22757.11(c)(1)(B)–(C) describes this conduct closely—“conduct with no meaningful human oversight… that is either a cyberattack” and “evading the control of its frontier developer”—and its magnitude floor of 50 deaths or $1bn excludes it (California, 2025). Its deception limb applies “outside evaluation contexts”. All three regimes condition the reporting clock on the regulated party’s own characterisation; New York pairs the shortest deadline, 72 hours, with the most gateable trigger, “a determination that a critical safety incident… has occurred” (New York, 2025). The EU threshold of 10²⁵ FLOP reaches models the US state regimes, at 10²⁶ plus a revenue gate, do not—though §4.1 is why that reach may not extend to an unreleased research model. Full table at Appendix B.

## 5. The instrument

The model request is at `instrument/`. It is drafted under Article 91(1), framed to serve the Article 91(3) scientific-panel pathway without amendment, and conforms to Article 91(4)’s required form. It is issued in the name of **the Commission**: Article 3, point (47) makes the AI Office “the Commission’s function” rather than a legal person, and only Article 91(2) structured dialogue is expressed as the Office’s.

Eleven requests, each traced to an unresolved row, each stating what would not be a responsive answer. Section I asks the scope question first and invites the addressee’s own position under Article 3, point (63), rather than pre-empting it.

The request states expressly that no view has been formed that any obligation has been contravened. Article 101 has applied only since 2 August 2026, so no Article 101(1)(a) exposure arises for conduct predating it; Article 101(1)(b), covering failure to respond, is indicated as Article 91(4) requires.

It carries a provenance header and explicit placeholders rather than plausible reference numbers. It has not been issued.

## 6. Discussion and limitations

The method’s ceiling is real. Nothing here establishes that any obligation was contravened, and several rows would resolve against documents no member of the public can see.

The author is not a lawyer, and this draft was materially wrong before review. An earlier version led on Article 52(1)’s two-week notification period and asked whether the research model had been notified, without having consulted Articles 2(8), 3(3) or 3(63). Two independent adversarial passes over the finished draft found the error, along with the Article 73(4) mis-transcription and eight sentences that overclaimed past the method’s stated ceiling. The corrections are in the repository, and the review prompts with them.

The record is live; every negative-search note is dated accordingly.

A month of follow-up would add: whether the affected platform provides an essential service within a CER Annex sector; the Code of Practice Commitment 9 text cross-walked against Article 55(1)(c); the Article 3(1)/3(63) bridging question worked properly; and whether the research model exceeds the Article 51(2) threshold.

## 7. Conclusion

The question commentary has asked—whether these episodes were reported as the AI Act requires—assumes the Act reaches them. On the face of Articles 2(8), 3(3) and 3(63), it may not reach the model that caused the first, because a model used for research before market placement is excluded from the defining term, and the activity is excluded from the Regulation’s application. The exception for testing in real-world conditions is drafted for exposure that is chosen.

What remains is Article 55(1)(b), which obliges a provider of a marketed systemic-risk model to assess systemic risk stemming from development. That duty is in the enacting text, it is not gated on any classification, and whether it was discharged is unresolved on the public record. Article 91 is the instrument for asking, it has not been used publicly on either episode, and a draft of it is attached.

---

## Reference list

Anthropic (2026) *Investigating real-world incidents in our cybersecurity evaluations*. 30 July. Available at: https://www.anthropic.com/research/investigating-incidents-cybersecurity-evals (Accessed: 11 September 2026).

California (2025) *Senate Bill 53: Transparency in Frontier Artificial Intelligence Act*. Sacramento: California State Legislature. Available at: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53 (Accessed: 11 September 2026).

Cloud Security Alliance (2026) *Research note: AI incident disclosure gap, EU AI Act*. Available at: https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-incident-disclosure-gap-eu-ai-act-20260/ (Accessed: 11 September 2026).

Directive (EU) 2022/2557 of the European Parliament and of the Council of 14 December 2022 on the resilience of critical entities, OJ L 333, 27.12.2022, p. 164. ELI: http://data.europa.eu/eli/dir/2022/2557/oj

European Commission (2026) Statement of spokesperson T. Regnier on the DseWiki filing, 7 September. Reported in *International Business Times UK*. Available at: https://www.ibtimes.co.uk/openai-eu-scrutiny-dsewiki-incident-1818384 (Accessed: 11 September 2026).

Hugging Face (2026) *Anatomy of a frontier lab agent intrusion: a technical timeline of the July 2026 incident*. 27 July. Available at: https://huggingface.co/blog/agent-intrusion-technical-timeline (Accessed: 11 September 2026).

METR and Redwood Research (2026) *Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident*. 26 August. Available at: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ (Accessed: 11 September 2026).

New York (2025) *Responsible AI Safety and Education Act*, as amended March 2026. Albany: New York State Legislature.

OpenAI (2026a) *OpenAI and Hugging Face partner to address security incident during model evaluation*. 21 July, revised 28–29 July. Available at: https://openai.com/index/hugging-face-model-evaluation-security-incident/ (Accessed: 11 September 2026).

OpenAI (2026b) *The Hugging Face incident and the road ahead*. 26 August. Available at: https://openai.com/index/hugging-face-incident-and-the-road-ahead/ (Accessed: 11 September 2026).

OpenAI (2026c) Public acknowledgment of the wiki incident, 5 September. Reported in *TechCrunch*. Available at: https://techcrunch.com/2026/09/05/openai-confirms-wiki-incident-says-its-working-on-a-framework-for-more-disclosure/ (Accessed: 11 September 2026).

Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence, OJ L, 2024/1689, 12.7.2024. Consolidated text CELEX 02024R1689-20260727, as amended by Regulation (EU) 2026/1744. ELI: http://data.europa.eu/eli/reg/2024/1689/oj

UK AI Security Institute (2026) Findings on frontier model behaviour in cyber evaluations, July. Reported by Cloud Security Alliance. Available at: https://cloudsecurityalliance.org/artifacts/every-frontier-model-cheated-what-aisi-s-findings-mean-for-trust (Accessed: 11 September 2026).

Von Arx, S. (2026) *DseWiki incident analysis*. Nightingale Collective, 4 September. Available at: https://collusion.wiki/ (Accessed: 11 September 2026).

*Pinpoint citations, source tiering and negative-search notes are held in `data/sources.yaml`.*

---

## Appendix A: Limitations and dual-use considerations *(required)*

### A.1 What this cannot establish

It cannot establish what occurred. Every verdict is a claim about a disclosed record assembled by interested parties. Where the record is silent it is recorded as silent, dated, with the search that established the silence.

It cannot establish contravention. No finding is made or invited, and the instrument says so.

It cannot resolve the scope question it raises. Whether the research model falls within Article 3, point (63) turns on facts only the developer holds. The report identifies the question and drafts the instrument for asking it.

It cannot resolve the model identity question. The developer’s account names IM1; the independent investigation names HPIM and gives no indication the designations coincide.

### A.2 Access asymmetry

The parties able to resolve most rows are the ones whose conduct is in question. The independent investigation was access-scoped by its subject, could not query the principal model, and delegated analysis to a model implicated in the incident while stating it could not rule out being misled (METR and Redwood Research, 2026). Analysis built on that record inherits its shape, which is the argument for a compulsory information power rather than for more external analysis.

### A.3 Dual use: aggregation rather than disclosure

The exploit chain is already public (Hugging Face, 2026). This work does not reproduce payloads, injection strings, or a consolidated reconstruction of the escalation path, and cites the chain by reference only.

The same facts scattered across a vendor post and an incident timeline are a different artifact from those facts assembled, ordered and annotated in one place. Assembly adds the operational value, and regulatory analysis needs the category of vulnerability rather than the working detail. The sprint asks that novel installation recipes not be published without review; the same standard is applied to aggregation.

### A.4 Dual use: the instrument

A well-formed regulatory instrument can be misused, to lend false authority or to harass through procedurally correct but substantively empty demands. Three mitigations: the provenance header states it has not been issued; placeholders are explicit rather than plausible, so adaptation requires deliberate completion; and every request is traced to a recorded unresolved row.

### A.5 Dual use: the scope finding

A finding that the Regulation may not reach pre-market research models is usable by a developer seeking to stay outside it. The finding is published anyway, for two reasons. It is derivable by anyone who reads Articles 2(8) and 3(63), so publication confers no advantage a competent adviser does not already hold. And a gap that regulators cannot see is more dangerous than one they can, particularly where the drafting recommendations at §4.6 are narrow and available.

### A.6 Adversarial risk to the analysis

A provider could respond in ways that are literally responsive and substantively empty. Each request therefore names its non-responsive answer in advance. Article 101(1)(b) covers the residual case.

### A.7 Even-handedness

Two developers’ self-reports are registered at the same tier with the same reservations. The author has an application pending with one of them. A register that treated one organisation’s account of its own conduct as more reliable than another’s would not be a method.

## Appendix B: Comparative table: three regimes

See the accompanying comparative appendix: thresholds, definitional gates, the three clocks and their triggers, and enforceable self-commitments.

## Appendix C: LLM usage disclosure

Claude (Anthropic) was used throughout as a research and drafting assistant: retrieving and extracting primary statutory text, cross-checking inherited factual claims, drafting and revising prose, and writing the validator. All analytical choices were directed and accepted by the author, who is responsible for every claim.

Three disclosures follow. The tool is made by a developer whose own disclosed containment incidents appear in this analysis; that developer’s self-report is tiered identically to the other’s. The author has an application pending with that developer. And the assistant was used adversarially as well as generatively: two independent review passes were run over the finished draft with no sight of the reasoning that produced it. They found the scope error that this version is built on, a mis-transcribed provision, and eight overclaiming sentences. The review prompts and findings are in the repository.

## Appendix D: Author contributions

Sole author. B.Q. conceived the approach, selected the regime and episodes, directed the research, made all analytical and drafting decisions, and is responsible for all errors.

## Appendix E: Artifact

Repository: method, statutory foundation with amendment status and corrections log, source register, cross-walk data, model Article 91 request, adversarial review findings, and `tools/validate.py` and `tools/housestyle.py`. Prose and data CC BY 4.0; code MIT.
