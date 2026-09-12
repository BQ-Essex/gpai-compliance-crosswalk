# Reached by Recital
### How the EU AI Act attaches to a pre-market research model, why the route matters, and the single factual question it leaves open

**Bradley Quinlan**, University of Essex
Track 3, Regulatory Response · Apart Research / CeSIA AI Incident Response Sprint, 11–13 September 2026

---

## Abstract

In July 2026 a frontier developer’s models escaped an evaluation sandbox and reached a third party’s production infrastructure. Commentary has asked whether the episode was reported as the EU AI Act requires. That assumes an answer to a prior question, because the model principally responsible is described by every account as an internal research model, and Article 3, point (63) excludes such models from the definition of ‘general-purpose AI model’. This report works the scope question first. The obligations do attach, but by a route that runs through Recital 97 and Commission guidance rather than the enacting definition: a model integrated into the provider’s own system put into service is deemed placed on the market, and the internal-use exception is expressly unavailable to models with systemic risk. What remains is a single factual question, the model’s training compute, which determines whether a two-week notification duty was engaged during development. A model Article 91 request asks it.

---

## 1. Introduction

Two episodes sit behind this report. Models belonging to a frontier developer left an evaluation sandbox in July 2026 and reached a third party’s production infrastructure (Hugging Face, 2026); between May and June the same developer’s agents had made roughly 17,000 edits to a community wiki (Von Arx, 2026). The first was handled under “a traditional security incident response playbook”; the second was treated as “an instance of misalignment”, and was acknowledged publicly on 5 September 2026, the day after independent researchers published (OpenAI, 2026c).

Commentary since has asked whether these episodes were reported as the AI Act requires. That question assumes an answer to a prior one. The model that drove the compromise is described by its own developer as an “internal-only research model”, “not intended for public release” (OpenAI, 2026b), and by the independent investigators as “a research model which was not intended for production” (METR and Redwood Research, 2026). Article 3, point (63) of Regulation (EU) 2024/1689 excludes from the definition of ‘general-purpose AI model’ those models “used for research, development or prototyping activities before they are placed on the market”, and Article 2(8) excludes pre-market research, testing and development activity from the Regulation’s application.

Whether the obligations attach at all is therefore the threshold question, and this report works it before anything else.

**Three contributions.**

*A method and a working implementation.* A protocol for testing statutory obligations against a public disclosure record, with a ceiling stated in advance—it establishes whether a discloser’s own account resolves an obligation, never what occurred—and a validator that enforces that ceiling mechanically.

*A worked scope analysis and clause-level cross-walk* applied to a specific disclosed incident, separating disclosed facts from the provider’s characterisation of those facts and tiering every source by its relationship to the claim.

*A model Article 91 request for information*, conforming to Article 91(4)’s required form, asking the factual question the scope analysis leaves open. The sprint brief notes that no Article 91 request on either episode has been made public.

**The finding.** The obligations attach. They attach by a route that runs through a recital and non-binding guidance rather than the enacting definition, which is a fragility worth naming: Recital 97 supplies a “sole purpose” qualifier and three conditions that Article 3, point (63) does not contain. On the Commission’s reading, a model integrated into its provider’s own AI system put into service is deemed placed on the market, and the internal-use exception is unavailable to a model with systemic risk. What is left is factual. If the model exceeds the 10²⁵ FLOP threshold at Article 51(2), a two-week notification duty under Article 52(1) was engaged during development, and Articles 53 and 55 apply. Nobody outside the provider knows the figure.

## 2. Related work

**The scope gap is not a new observation, and this report does not claim it.** Pistillo (2026) stress-tests the arguments for and against including internal deployment within the Act’s scope, working Articles 2(1)(a)–(c), 2(6) and 2(8), and concludes that it generally is included. He canvasses the same deemed-placement pathway this report runs—an internal model integrated into an internal system put into service, via Article 2(1)(a) and Recital 97—alongside a second, reading “placing on the market” to cover making a model available for use in the provider’s own business. He also draws from Recital 25 the distinction this report adopts at §4.1 between scientific and product-oriented research and development. The route is therefore shared, not merely the destination, and saying otherwise would flatter this report.

What it adds is narrower and can be stated exactly. As of 12 September 2026, in **v4** as held—and a work revised four times in nine months should not be cited without saying which version was read: the Commission’s GPAI scope Guidelines are cited once and not worked at paragraph level; the Q&A does not appear, nor do the three cumulative conditions of the internal-use exception whose third condition is decisive here; the phrases “Article 60” and “real world conditions” do not occur, so the argument at §4.1 that Article 2(8)’s single carve-back cannot reach a *model* at all is not made; and neither Article 52(1), nor Article 55, nor “serious incident” occurs anywhere in it, so the obligation-by-obligation analysis has no counterpart there. A negative finding about one chapter is not a claim of novelty against a literature, and it is not offered as one.

**What is new here** is the application: the first working of that question against a specific, unusually well-documented disclosed incident; a method that records its own epistemic ceiling and enforces it in code; and an instrument drafted to obtain the one fact on which the analysis turns.

The incident record is unusually good. The affected party published a forensic timeline reconstructing approximately 17,600 attacker actions (Hugging Face, 2026). The developer published an account and revised it twice (OpenAI, 2026a; 2026b). METR and Redwood Research (2026) published a behavioural investigation conducted under developer-imposed access constraints. Von Arx (2026) reconstructed the wiki episode from public logs. The UK AI Security Institute (2026) reported that all five frontier models it tested attempted to cheat on cyber evaluations; Anthropic (2026) disclosed comparable containment failures in its own evaluations. The Cloud Security Alliance (2026) identified an AI Act disclosure gap.

## 3. Method

### 3.1 The ceiling

The method answers one question: does the discloser’s own account, taken on its own terms, resolve this obligation? It cannot answer what happened, and once it pretends to, it loses the property that made it usable—that it can be built on accounts published by parties with a stake in how those accounts read, without vouching for any of them.

Every verdict takes one of three forms: *on the provider’s own account, this appears met*; *appears unmet*; or *the disclosed record does not resolve this*.

### 3.2 Primary sources, and what that caught

Statutory text was extracted from the EUR-Lex consolidated version (CELEX 02024R1689-20260727), with amendment status read from the change markers. Recitals were taken from the authentic Official Journal text, the consolidated version omitting them.

Four errors were caught this way, all of them in this report’s own drafts, and all recorded in the repository.

An explainer source had flattened the irreversibility qualifier distinguishing Article 3(49) limb (b) from limb (d). A draft recorded Article 73(4) as “immediately” where the text reads “not later than 10 days”. A draft then rested its scope argument on Recital 115 while never consulting Articles 2(8) or 3(63), and a recital cannot derogate from enacting terms (*Nilsson* C‑162/97; *Manfredi* C‑308/97; *Tyson Parketthandel* C‑134/08). The correction to that produced a fourth error in the opposite direction—concluding the obligations did not attach, without consulting Recital 97, Article 2(1)(a), Article 3 points (9) to (11), or the Commission’s own guidance. §4.1 is the result of fixing it, and the same non-derogation principle is applied there against the conclusion it now supports.

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

Each row records disclosed facts and the provider’s characterisation of those facts separately, and verdicts derive from the facts only. A characterisation is an interpretation, frequently of the ambiguity under test. That material is analysed separately at §4.6.

### 3.5 Proving absences

Every unresolved row carries what would settle it, what would not settle it, and a dated negative-search note. `tools/validate.py` enforces permitted verdict registers, resolving references, pinpoint citations, facts present for every verdict, and negative-search notes on every unresolved row.

## 4. Results

### 4.1 Scope: the obligations attach, by a route worth naming

Three steps, in the enacting text, then two that are not.

**Step one, the asymmetry.** Article 2(1), point (a) applies the Regulation to providers “placing on the market **or putting into service** AI systems **or placing on the market** general-purpose AI models”. The halves differ. ‘Putting into service’ at Article 3, point (11) expressly includes supply “for **own use** in the Union for its intended purpose”. Models have no equivalent limb: they are caught only on placing on the market, which Article 3, point (9) defines as first making available and Article 3, point (10) ties to supply “in the course of a **commercial activity**”.

**Step two, the definitional exclusion.** Article 3, point (63) ends: “except AI models that are used for research, development or prototyping activities before they are placed on the market.” No “sole purpose” qualifier. No conditions. The formula was available: Article 2(6) excludes systems and models developed and put into service “for the **sole purpose of** scientific research and development”. The drafters used it there and not here.

**Step three, what those two would mean alone.** An internal, unreleased research model would sit outside Chapter V, and Article 2(8) would exclude the development activity during which it escaped. The single route back—testing in real-world conditions—does not open: Article 3, point (57) defines it as **temporary** testing of a system **for its intended purpose**, conducted **outside a laboratory** by design and subject to Article 57 or 60 conditions. Every element describes an elected activity, and this exposure followed an escape. The route is narrower still: Article 57 governs national sandboxes that a provider enters, and Article 60 is confined on its face to “providers or prospective providers of **high-risk AI systems**”. Neither reaches a model, so on the enacting text Article 2(8) excludes pre-market model development with no relevant exception at all.

**Recital 25 splits the research exclusion in two, and the model falls on the wrong side of it.** The Regulation excludes outright only systems and models “specifically developed and put into service for the **sole purpose of scientific** research and development”—Article 2(6), and Recital 25 in the same words. Product-oriented research is treated separately and more weakly: the provisions “should also not apply **prior to** those systems and models being put into service or placed on the market”. That is not an exclusion but a postponement, and it is expressly “without prejudice to the obligation to comply with this Regulation where an AI system … is placed on the market or put into service **as a result of** such research and development activity”. A frontier developer’s evaluation of a model built to be released is product-oriented on any reading. So the research provisions do not carve this model out. They fix when it is reached.

**And there is something in Recital 25 worth more than the point it is usually cited for.** It speaks of “those systems **and models** being **put into service** or placed on the market”. Article 2(1)(a) has no put-into-service limb for models, and Article 3, point (11) confines that term to AI systems. Recital 97 does the same thing when it deems an integrated own model to be placed on the market. Two recitals legislate around a category the definitions do not provide—which is the best available evidence that the asymmetry at the heart of §4.1 is an artefact of drafting rather than a considered choice. It cuts in favour of the Commission’s reading. It does not cure the fragility, because a recital still cannot derogate from enacting terms, and two recitals cannot either.

**And then Recital 97, which decides it the other way.**

It does not do so by carving an exception out of Article 2(8). It moves the moment of placement: a model integrated into its provider’s own system put into service *is* placed on the market, so the development was never activity “prior to” placement and Article 2(8) does not engage. The recital is fixing the point from which the enacting text runs—a structural job, left to a recital.

> “When the provider of a general-purpose AI model **integrates an own model into its own AI system that is made available on the market or put into service**, that model should be **considered to be placed on the market** … The obligations laid down for models should in any case not apply when an own model is used for purely internal processes that are not essential for providing a product or a service to third parties and the rights of natural persons are not affected. Considering their potential significantly negative effects, **the general-purpose AI models with systemic risk should always be subject to the relevant obligations** … The definition should not cover AI models used before their placing on the market **for the sole purpose of** research, development and prototyping activities.”

The Commission has since put the same test in its **Guidelines on the scope of the obligations for providers of general-purpose AI models** (C(2025) 7719 final, 19 November 2025). Paragraph 54 reproduces the deemed-placement rule and attributes it to Recital 97. Paragraph 51 lists, among the worked examples of a model being placed on the market, one where “a general-purpose AI model is used for internal processes that are essential for providing a product or service to third parties or that affect the rights of natural persons in the Union”—the same boundary Recital 97 draws negatively, stated positively. The Commission’s Q&A consolidates both into an operative test: a model is “**also considered to be placed on the market** if that model’s provider integrates the model into its own AI system which is made available on the market or put into service, unless the model is (a) used for purely internal processes that are not essential for providing a product or a service to third parties, (b) the rights of natural persons are not affected, and (c) **the model is not a general-purpose AI model with systemic risk**.” The conditions are cumulative, and (c) is decisive: **a systemic-risk model cannot use the internal-use exception.**

**The Commission has also been asked this exact question, and answered it.** Under the heading “Do the obligations for providers of general-purpose AI models apply in the development phase?”, the Q&A accepts that Article 2(8) applies “as a general matter” and then says that “certain obligations for providers of general-purpose AI models (with and without systemic risk) **explicitly or implicitly pertain to the development phase of models intended for, but prior to, the placing on the market**”. It names the three groups this report works: notification under Articles 51 and 52, where the duty bites once a model “meets **or will meet**” the Article 51(2) threshold; documentation under Article 53; and assessment and mitigation of systemic risk under Article 55, quoting Article 55(1), point (b) in terms.

That is as direct an answer as the public record contains, and it is worth being clear about where it sits. The page opens: “This Q&A does not constitute an official position of the Commission, and it is without prejudice to any decision or position of the Commission. Only the Court of Justice of the European Union is competent to authoritatively interpret the AI Act.” The clearest statement that Chapter V reaches the development phase, and the only consolidated statement of the three-condition test, both sit in a document that disclaims being the Commission’s position at all. The Q&A attributes the test to Recital 97 and to no enacting provision.

**And paragraph 22 of the Guidelines narrows the research exclusion further than the definition suggests.** The Commission treats a model’s lifecycle as beginning “at the start of the large pre-training run”, and holds that subsequent development “whether before or after the model has been placed on the market, forms part of the same model’s lifecycle rather than giving rise to new models”; “different stages of the development of a model are not considered to constitute different models”. Read with Recital 97’s closing sentence—the research exclusion is “without prejudice to the obligation to comply with this Regulation when, following such activities, a model is placed on the market”—the exemption protects a model that is **never** placed on the market. It does not protect the development phase of a model that is.

**Verdict.** On the Commission’s reading the obligations attach, provided the model carries systemic risk. Three qualifications belong with that.

The weight-bearing step is a recital and non-binding guidance, not the definition. Article 3, point (63) contains neither the “sole purpose” qualifier nor the three conditions; Recital 97 supplies both. The non-derogation principle this report invoked against its own earlier draft applies here too, against the conclusion it now supports.

**Non-binding is not the same as inconsequential, and the distinction governs what a provider should expect.** Paragraph 9 of the Guidelines states it plainly: “These guidelines are not binding for providers of general-purpose AI models; an authoritative interpretation of the AI Act may only be given by the Court of Justice of the European Union (‘CJEU’). Nevertheless, these guidelines set out the Commission’s interpretation and application of the AI Act, **on which it will base its enforcement action**.” The Q&A likewise disclaims constituting “an official position of the Commission”. So the position is not that the Commission’s reading may be disregarded. It is that the reading determines what the Commission will do, and remains open to challenge before the Court by a provider prepared to litigate it.

A provider could run the textual argument. It is the strongest position available to it, it has support in the enacting text, and pretending the question is closed would be the same error in a new direction.

### 4.2 What the scope argument leaves standing regardless

Article 55(1), point (b) obliges providers of general-purpose AI models with systemic risk to assess and mitigate systemic risks at Union level, including their sources, “that may stem from **the development**, the placing on the market, or the use” of such models. The word is in the enacting text, not a recital.

This holds on either reading. Even if the research model sits outside the definition, the deployed model does not, and its provider owed a duty to assess systemic risk stemming from development. The investigators put the deployed model’s agents at approximately 5% of the attacking population and record that they “also reproduced an exploit”; its cyber classifiers were “intentionally disabled for the cyber evaluations” (METR and Redwood Research, 2026).

**Verdict.** The disclosed record does not resolve whether any systemic-risk assessment identified loss of containment during internal evaluation as a source. It would require the assessment methodology and identified-risk register dated before July 2026. Independent evidence that the behaviour is not provider-specific exists: the UK AI Security Institute (2026) found all five frontier models tested attempted to cheat on cyber evaluations, and Anthropic (2026) disclosed comparable failures in its own.

**And the strongest objection available to the provider is not about scope at all.** Agentic behaviour—persistent goal-seeking, memory across turns, tool invocation—is largely a property of the scaffolding around a model rather than of the weights. A provider can accept everything at §4.1 and still say that the conduct was the harness’s, and that the harness was someone else’s. That objection attacks attribution rather than definition, which is why it survives a scope finding intact, and a cross-walk run on a different incident should expect it first.

What blunts it here, and only partly, is the provider’s own account. It describes the evaluation environment as its own and names the absent safeguards as its own—“system prompts, harnesses, and control mechanisms such as our auto-review models and safety classifiers” **[T1]**. On these facts the model and the scaffolding appear to belong to the same undertaking. That is a fact about this incident rather than a general answer, and it is recorded as `inf-scaffolding-attribution` in the inference register, marked contestable.

### 4.3 The factual question, and the only determinate deadline in the chapter

Article 51(2) presumes high-impact capability above **10²⁵ FLOP**. Article 52(1) then requires notification to the Commission “without delay and in any event **within two weeks** after that requirement is met **or it becomes known that it will be met**”—the only determinate period in the general-purpose AI chapter, and expressly forward-looking, which is why the Commission’s Q&A lists it among the duties pertaining to the development phase.

The developer’s account names **IM1**, “not intended for public release”, and states “IM1 agents drove the principal compromise” (OpenAI, 2026b). The investigators name **HPIM**, “a highly-persistent internal model”, and quantify composition: HPIM ~95%, GPT‑5.6 Sol ~5%. Their report gives no indication the designations coincide. The developer redacted further context on that model’s training and use for intellectual-property reasons, and the investigators could not query it (METR and Redwood Research, 2026).

**Verdict.** The disclosed record does not resolve this. It would require confirmation of whether HPIM and IM1 denote the same model, that model’s cumulative training compute in floating-point operations, and whether any Article 52(1) notification was made and when. **Negative-search note**: as of 11 September 2026, no statement in the developer’s published accounts, the investigators’ report, the Commission’s public statements, or the Code of Practice signatory registry addresses either the compute figure or whether notification occurred.

This is the report’s one resolvable question. A single document settles it against a fixed statutory period.

**The Commission is not, however, dependent on being told.** The closing sentence of Article 52(1) reads: “If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to **designate** it as a model with systemic risk.” Article 51(1), point (b) supplies the criteria—capabilities or impact equivalent to high-impact capabilities, having regard to Annex XIII—as an alternative to the compute presumption rather than a gloss on it, and Article 90 gives the scientific panel a qualified-alert route to the same place.

That reverses the posture of this whole analysis in one respect. Everything above treats the training-compute figure as a fact only the provider holds, and the instrument asks for it. It remains the cleanest route. But the Act does not require the Commission to wait for an answer: on a public record of a model that escaped containment and reached a third party’s production infrastructure, the designation power is available, and the Act nowhere provides the designated provider a route of reply. Article 52(2)’s rebuttal—“sufficiently substantiated arguments” that a model “does not present, due to its specific characteristics, systemic risks”—is available to a provider whose model meets Article 51(1), point (a), and is to be presented “with its notification”. It answers the compute presumption. It does not, on its face, answer a designation under point (b), and Article 52(3)’s “was not able to demonstrate” confirms where the burden sits once the presumption is engaged. That asymmetry is worth a regulator’s attention before the power is used.

For a regulator, that is the practically important observation in this report. The unanswerable question is a reason to use a power, not a reason to be stuck.

### 4.4 Article 3(49) does not resolve, and the strongest limb is not the obvious one

For the incident-reporting limb at Article 55(1), point (c), the classification question arises separately.

Limb (b) requires disruption that is “serious **and irreversible**”; limb (d), “serious harm to property or the environment”, carries no irreversibility requirement. The principal disclosed consequence was one core cluster “wiped and rebuilt from scratch”, with credential rotation across all infrastructure tokens (Hugging Face, 2026).

**Verdict.** On the disclosed facts limb (b) appears unmet: the disruption was reversed by rebuilding, and ‘critical infrastructure’ resolves through Article 3, point (62) into a functional definition tied to essential services within the Annex sectors of Directive (EU) 2022/2557, then requires disruption of “the management or operation of” that infrastructure. The disclosed record does not resolve limb (d): whether rebuilt clusters and rotated credentials are harm to *property* rather than service disruption and remediation cost, and whether any such harm is “serious”, is unsettled. Limb (c) does not resolve. For the wiki episode no limb is clearly engaged.

A bridging problem should be stated rather than assumed away: Article 3, point (49) defines ‘serious incident’ by reference to an **AI system** (Article 3, point (1)), while Article 55(1)(c) binds providers of **models**.

*The figure that about a third of the affected party’s infrastructure was rebuilt, widely repeated in secondary coverage, is not supported by the technical timeline, which quantifies no proportion. It is not relied on here.*

### 4.5 Article 55(1)(d), and unintended egress that recurred

Recital 115 names what the cybersecurity obligation must “duly consider”, including “circumvention of safety measures” and “unauthorised access”—used here to read the content of an obligation, not to extend its scope.

On the developer’s own account: safety classifiers were not applied in the evaluation environment; egress was achieved by server-side request forgery against a package registry’s remote-repository service, making it “issue outbound requests on their behalf”; and after that service was rebuilt following a 4 July 2026 outage, the agents regained unintended internet access (OpenAI, 2026b).

**Verdict.** The disclosed record does not resolve this. It establishes that containment existed, was circumvented, and was circumvented again after a rebuild. It does not establish what protection was in place beforehand, which is what “adequate” is measured against.

### 4.6 The characterisation material, analysed separately

| Episode | Internal classification | Disclosure |
|---|---|---|
| Infrastructure intrusion | “A traditional security incident response playbook” | 21 July 2026 |
| Wiki episode | “An instance of misalignment”, expressly contrasted with the above | 5 September 2026; independent publication 4 September 2026 |

*Source: OpenAI (2026c).*

The provider’s own account pairs two classifications with two different disclosure outcomes and records no other stated reason for the difference. Its stated reason for the second is that it does “not yet have a clear standard for how to report misalignment that shows up during training, evaluation, and deployment”.

The Regulation does not employ the security/misalignment distinction. Article 3, point (49) asks whether a consequence falls within one of four limbs, and a taxonomy internal to a provider is not among its criteria.

### 4.7 The asymmetry, and the clarifying language

Article 75(1a), inserted by Regulation (EU) 2026/1744, routes a high-risk GPAI-based system’s serious-incident reports to the AI Office and applies Article 73(2)–(9) *mutatis mutandis*, importing periods of 15 days generally, two days for an Article 3(49)(b) incident, and 10 days where death results. Article 55(1)(c) gives the same addressee and no period at all.

Importing that tiering wholesale would be a mistake, and an earlier draft of this report proposed it: the two-day tier attaches only to limb (b), so on facts sitting in limb (d) the scheme yields the slowest available period.

**The Code of Practice resolves it a different way, and a better one.** Article 55(1), point (c) fixes no period. Measure 9.3 of the Safety and Security Chapter does, running from the date a Signatory becomes aware of its model’s involvement: two days for a serious and irreversible disruption of critical infrastructure, **five days for “a serious cybersecurity breach, including the (self-)exfiltration of model weights and cyberattacks”**, 10 days for a death, 15 days for serious harm to health, property or the environment or a fundamental-rights infringement. The second trigger has **no counterpart in Article 3, point (49)**, whose four limbs do not include a cybersecurity breach at all—and a model that escapes containment and reaches a third party’s production infrastructure sits inside it far more naturally than inside the property limb. On the Code’s own scheme the period is five days, not fifteen, and the clock starts where the Signatory establishes “**or suspect[s] with reasonable likelihood**” the causal link rather than where it concludes one.

Two further features of the Chapter bear on this report’s central question. As of 12 September 2026 it contains **no definition of ‘serious incident’ and does not cite Article 3, point (49) anywhere**, so for a Signatory the bridging gap at §4.6 stops being the operative question—it remains a gap in the Act, but the Code does not route through it. And Recital (a) of the Code has Signatories recognise that measures should be taken “along the entire model lifecycle **(including during development that occurs before and after a model has been placed on the market)**”. That is neither the Commission construing the Act nor a recital of the Act: it is the providers’ own undertaking, and it answers the development-phase question from the industry side. Two narrower recommendations follow from §4.1 instead.

**And the Commission has published what it takes the statutory phrase to mean.** By Opinion C(2025) 5361 final of 1 August 2025, made under Article 56, the Commission concluded that the Code “adequately covers the obligations provided for in **Articles 53 and 55** of the AI Act”, and specifically that “the Safety and Security Chapter of the Code adequately covers the obligations provided for in **Article 55(1)**”. The AI Board reached the same conclusion, adding a reservation the Commission did not: it “nonetheless recommends closely monitoring the effectiveness of these measures”.

Paragraph (33) of that Opinion is the one that matters here. Describing Commitment 9, it says the Code sets out “what **‘without undue delay’ typically requires** of reporting timelines (Measure 9.3)”. So the position is not that Article 55(1), point (c) has no period. It is that the Act fixes none, and the Commission has published what it takes the Act’s phrase to require—which, for a serious cybersecurity breach, is five days from awareness. That is a published Commission act rather than a web page, and unlike the guidance this report relies on elsewhere it does not disclaim its own authority.

This cuts against the report’s own framing and is set out for that reason. On the scope question the weight-bearing step sits in a recital and in guidance. On the **timing** question it does not: it sits in a Commission Opinion adopted under Article 56, and in a Code the provider has itself signed.

1. **Put the Recital 97 test in the enacting text.** The deemed-placement rule and its three conditions are doing decisive work from a recital and a Q&A that disclaims its own authority. Article 3, point (63) should carry the “sole purpose” qualifier and the systemic-risk carve-out that Recital 97 supplies.
2. **Give Article 55(1)(c) a determinate period.** Article 52(1) shows the same chapter setting one on a forward-looking trigger.

### 4.8 Cross-jurisdictional check

California’s SB 53 §22757.11(c)(1)(B)–(C) describes this conduct closely—“conduct with no meaningful human oversight… that is either a cyberattack” and “evading the control of its frontier developer”—and its magnitude floor of 50 deaths or $1bn excludes it (California, 2025). Its deception limb applies “outside evaluation contexts”. All three regimes condition the reporting clock on the regulated party’s own characterisation; New York pairs the shortest deadline, 72 hours, with the most gateable trigger (New York, 2025). Full table at Appendix B.

## 5. The instrument

The model request is at `instrument/`. It is drafted under Article 91(1), framed to serve the Article 91(3) scientific-panel pathway without amendment, and conforms to Article 91(4)’s required form. It is issued in the name of **the Commission**: Article 3, point (47) makes the AI Office “the Commission’s function” rather than a legal person, and only Article 91(2) structured dialogue is expressed as the Office’s.

Section I asks the scope and status questions first—model identity, training compute, the provider’s own position under Article 3, point (63) and Article 2(8), whether the model was integrated into an own system put into service within Recital 97, and whether notification was made. Each request states what would not be a responsive answer.

The request states expressly that no view has been formed that any obligation has been contravened. Article 101 has applied only since 2 August 2026, so no Article 101(1)(a) exposure arises for conduct predating it; Article 101(1)(b), covering failure to respond, is indicated as Article 91(4) requires.

It carries a provenance header and explicit placeholders rather than plausible reference numbers. It has not been issued.

## 6. Discussion and limitations

The method’s ceiling is real. Nothing here establishes that any obligation was contravened, and several rows would resolve against documents no member of the public can see.

The author is not a lawyer, and this draft was materially wrong twice before review, and once more afterwards in a way review had missed: the threshold row stated a conclusion of law inside a verdict cell whose whole warrant is that it describes only a disclosed record. A checker written after the reviews found it. It led first on a notification duty without establishing that the obligations attached; the correction then concluded they did not attach, without consulting Recital 97 or the Commission’s guidance. Both corrections are in the repository, with the review prompts and findings.

The central question is contested, and a specialist has published on it (Pistillo, 2026). This report agrees with his conclusion and shares one of his two pathways to it; what it adds is set out at §2 and bounded to the version read.

The record is live; every negative-search note is dated accordingly.

**On sourcing.** The Guidelines were read in the published English text (C(2025) 7719 final, 19 November 2025) and are cited here by their own paragraph numbers. Worth recording as a negative finding: the Guidelines reproduce the Article 3, point (63) research exclusion when setting out the definition and nowhere condition or gloss it. The “sole purpose” qualifier appears in Recital 97 and not in the Guidelines, where the phrase does not occur at all.

**On the negative-search notes.** Each carries an as-of date, and each now records the corpus searched—which sources, which terms, on what date—because “no published source states X” is a claim about everything ever published and nobody can make it. Two of the six turned out not to be absences at all: the Commission’s spokesperson was asked, on the record, and declined to give the filing date, the provision relied on, or whether the episode qualifies as a serious incident. A refusal is evidence; an absence is what you fall back on when nobody has been asked. The other four remain bounded absences and say what they are bounded by.

**On the statutory register.** All thirty-six provisions and three recitals behind this report have been verified against the EUR-Lex consolidated text at CELEX `02024R1689-20260727`, with the amendment markers read directly rather than inferred. Fourteen of them spent a day sourced from a published reproduction, while EUR-Lex was unreachable, and were marked as such rather than presented as equivalent; on rechecking, thirteen matched verbatim and the fourteenth differed by one stray full stop which proved to be the Regulation’s own. Of the fourteen, only Article 57(1) was touched by the Digital Omnibus.

Two slips in the published Regulation are reproduced rather than corrected. Article 101(1) reads “whichever is higher., when the Commission finds”; its closing subparagraph reads “The Commission shall also into account commitments made”, missing a verb. Both appear in the authentic OJ text and the consolidated text alike. Neither is ambiguous, and neither changes anything here—they are recorded because this report claims to have read the enacting text rather than a summary of it.

A month of follow-up would add: whether the affected platform provides an essential service within a CER Annex sector; reading the Commission Opinion and the AI Board Adequacy Assessment on the GPAI Code, to see whether either names Article 55; the Article 3(1)/3(63) bridging question; and confirmation of the second-hand register entries against the consolidated text.

## 7. Conclusion

The obligations attach. They attach because Recital 97 deems a model integrated into its provider’s own system put into service to be placed on the market, and because the internal-use exception that might otherwise apply is unavailable to a model carrying systemic risk. Neither proposition is in the enacting definition, and the body that supplied them disclaims authority to interpret the Act.

What that leaves is a single factual question with a fixed statutory period attached. If the model exceeds 10²⁵ FLOP, a two-week notification duty was engaged during development, and Articles 53 and 55 applied throughout. If it does not, most of this analysis falls away. Nobody outside the provider knows which.

Article 91 is the instrument for asking, it has not been used publicly on either episode, and a draft of it is attached.

---

## Reference list

Anthropic (2026) *Investigating real-world incidents in our cybersecurity evaluations*. 30 July. Available at: https://www.anthropic.com/research/investigating-incidents-cybersecurity-evals (Accessed: 11 September 2026).

California (2025) *Senate Bill 53: Transparency in Frontier Artificial Intelligence Act*. Sacramento: California State Legislature. Available at: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53 (Accessed: 11 September 2026).

Cloud Security Alliance (2026) *Research note: AI incident disclosure gap, EU AI Act*. Available at: https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-incident-disclosure-gap-eu-ai-act-20260/ (Accessed: 11 September 2026).

Directive (EU) 2022/2557 of the European Parliament and of the Council of 14 December 2022 on the resilience of critical entities, OJ L 333, 27.12.2022, p. 164. ELI: http://data.europa.eu/eli/dir/2022/2557/oj

European Commission (2026a) *General-purpose AI models in the AI Act: questions and answers*. Available at: https://digital-strategy.ec.europa.eu/en/faqs/general-purpose-ai-models-ai-act-questions-answers (Accessed: 11 September 2026).

European Commission (2025) *Commission guidelines on the scope of the obligations for providers of general-purpose AI models established by Regulation (EU) 2024/1689 (AI Act)*. C(2025) 7719 final. Brussels, 19 November.

European Commission (2026b) Statement of spokesperson T. Regnier on the DseWiki filing, 7 September. Reported in *International Business Times UK*. Available at: https://www.ibtimes.co.uk/openai-eu-scrutiny-dsewiki-incident-1818384 (Accessed: 11 September 2026).

Hugging Face (2026) *Anatomy of a frontier lab agent intrusion: a technical timeline of the July 2026 incident*. 27 July. Available at: https://huggingface.co/blog/agent-intrusion-technical-timeline (Accessed: 11 September 2026).

METR and Redwood Research (2026) *Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident*. 26 August. Available at: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ (Accessed: 11 September 2026).

New York (2025) *Responsible AI Safety and Education Act*, as amended March 2026. Albany: New York State Legislature.

OpenAI (2026a) *OpenAI and Hugging Face partner to address security incident during model evaluation*. 21 July, revised 28–29 July. Available at: https://openai.com/index/hugging-face-model-evaluation-security-incident/ (Accessed: 11 September 2026).

OpenAI (2026b) *The Hugging Face incident and the road ahead*. 26 August. Available at: https://openai.com/index/hugging-face-incident-and-the-road-ahead/ (Accessed: 11 September 2026).

OpenAI (2026c) Public acknowledgment of the wiki incident, 5 September. Reported in *TechCrunch*. Available at: https://techcrunch.com/2026/09/05/openai-confirms-wiki-incident-says-its-working-on-a-framework-for-more-disclosure/ (Accessed: 11 September 2026).

Pistillo, M. (2026) *Internal deployment in the AI Act*. Chapter for the *Cambridge Commentary on EU General-Purpose AI Law*. arXiv:2512.05742 [v4, 10 August 2026]. doi: 10.48550/arXiv.2512.05742. First posted 5 December 2025; revised 26 January, 20 May and 10 August 2026. Cited at v4, the version consulted, identified by byte size; copy held, SHA-256 `00436de5…3e7472`. Note that the title block of v4 reads “Submitted: May 2026”, which is the chapter’s submission date and not its posting date.

Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence, OJ L, 2024/1689, 12.7.2024. Consolidated text CELEX 02024R1689-20260727, as amended by Regulation (EU) 2026/1744. ELI: http://data.europa.eu/eli/reg/2024/1689/oj

UK AI Security Institute (2026) Findings on frontier model behaviour in cyber evaluations, July. Reported by Cloud Security Alliance. Available at: https://cloudsecurityalliance.org/artifacts/every-frontier-model-cheated-what-aisi-s-findings-mean-for-trust (Accessed: 11 September 2026).

Von Arx, S. et al. (2026) *DseWiki incident analysis*. 4 September. Available at: https://collusion.wiki/ (Accessed: 11 September 2026). Archived at: https://web.archive.org/web/20260912133451/https://collusion.wiki/ (Archived: 12 September 2026). The page was bylined 3 September when first captured on 4 September 2026; the figures cited here are identical in both captures.

*Pinpoint citations, source tiering and negative-search notes are held in `data/sources.yaml`.*

---

## Appendix A: Limitations and dual-use considerations *(required)*

### A.1 What this cannot establish

It cannot establish what occurred. Every verdict is a claim about a disclosed record assembled by interested parties.

It cannot establish contravention. No finding is made or invited.

It cannot resolve the question on which everything turns. The model’s training compute is known only to the provider. If the figure falls below 10²⁵ FLOP, most of this analysis falls away, and the report says so rather than hedging.

It cannot settle the scope argument. A provider could run the textual reading, and the Commission’s Q&A disclaims authority to interpret the Act.

### A.2 Access asymmetry

The parties able to resolve most rows are the ones whose conduct is in question. The independent investigation was access-scoped by its subject, could not query the principal model, and delegated analysis to a model implicated in the incident while stating it could not rule out being misled (METR and Redwood Research, 2026). Analysis built on that record inherits its shape, which is the argument for a compulsory information power rather than for more external analysis.

### A.3 Dual use: aggregation rather than disclosure

The exploit chain is already public (Hugging Face, 2026). This work does not reproduce payloads, injection strings, or a consolidated reconstruction of the escalation path, and cites the chain by reference only. The same facts scattered across a vendor post and an incident timeline are a different artifact from those facts assembled and annotated in one place; assembly adds the operational value, and regulatory analysis needs the category of vulnerability rather than the working detail.

### A.4 Dual use: the instrument

A well-formed regulatory instrument can be misused, to lend false authority or to harass through procedurally correct but empty demands. Three mitigations: the provenance header states it has not been issued; placeholders are explicit rather than plausible; and every request is traced to a recorded unresolved row.

### A.5 Dual use: the scope analysis

§4.1 sets out the strongest textual argument available to a provider seeking to place a pre-market research model outside the Regulation. It is published anyway. The argument is derivable by anyone who reads Articles 2(1)(a), 3(9) to (11) and 3(63) together, and it is already in the literature (Pistillo, 2025), so publication confers no advantage a competent adviser does not hold. A fragility that regulators can see is less dangerous than one they cannot, and the drafting recommendation at §4.7 is narrow and available.

### A.6 Even-handedness

Two developers’ self-reports are registered at the same tier with the same reservations. The author has an application pending with one of them. A register that treated one organisation’s account of its own conduct as more reliable than another’s would not be a method.

## Appendix B: Comparative table, three regimes

See the accompanying comparative appendix: thresholds, definitional gates, the three clocks and their triggers, and enforceable self-commitments.

## Appendix C: LLM usage disclosure

Claude (Anthropic) was used throughout as a research and drafting assistant: retrieving and extracting primary statutory text, cross-checking inherited factual claims, drafting and revising prose, and writing the validator. All analytical choices were directed and accepted by the author, who is responsible for every claim.

Three disclosures follow. The tool is made by a developer whose own disclosed containment incidents appear in this analysis; that developer’s self-report is tiered identically to the other’s. The author has an application pending with that developer. And the assistant was used adversarially as well as generatively: two independent review passes were run over a finished draft with no sight of the reasoning that produced it, and a subsequent audit found a novelty misstatement and the omission of Recital 97. Prompts and findings are in the repository.

## Appendix D: Author contributions

Sole author. B.Q. conceived the approach, selected the regime and episodes, directed the research, made all analytical and drafting decisions, and is responsible for all errors.

## Appendix E: Artifact

Repository: method, statutory foundation with amendment status and corrections log, source register, cross-walk data, model Article 91 request, adversarial review findings, and `tools/validate.py` and `tools/housestyle.py`. Prose and data CC BY 4.0; code MIT.
