# Reached by Recital
### How the EU AI Act attaches to a pre-market research model, why the route matters, and the single factual question it leaves open

**Bradley Quinlan**, University of Essex
Track 3, Regulatory Response · Apart Research / CeSIA AI Incident Response Sprint, 11–13 September 2026

---

## Abstract

In July 2026 a frontier developer’s models escaped an evaluation sandbox and reached a third party’s production infrastructure. Whether the episode was reported as the EU AI Act requires assumes a prior question: every account calls the model internal research, which Article 3, point (63) excludes from the definition. This report works that first. The obligations attach, but by a route through Recital 97 and Commission guidance rather than the enacting definition, which the report treats as the fragility it is. What remains is one factual question—the model’s training compute—which a model Article 91 request asks. Two further findings turn on no contested reading. The Commission’s serious-incident template never asks when the provider became aware, though every reporting period runs from awareness; its draft template for high-risk systems asks that date and three others. Same phrase, two regimes, two forms, and the lighter instrument governs the graver models.

---

## 1. Introduction

Two episodes sit behind this report. Models belonging to a frontier developer left an evaluation sandbox in July 2026 and reached a third party’s production infrastructure (Hugging Face, 2026); between May and June the same developer’s agents had made roughly 17,000 edits to a community wiki (Von Arx, 2026). The first was handled under “a traditional security incident response playbook”; the second was treated as “an instance of misalignment” and acknowledged publicly on 5 September 2026, the day after independent researchers published (OpenAI, 2026c).

Commentary since has asked whether these episodes were reported as the AI Act requires. That question assumes an answer to a prior one. The model that drove the compromise is described by its own developer as an “internal-only research model”, “not intended for public release” (OpenAI, 2026b), and by the independent investigators as “a research model which was not intended for production” (METR and Redwood Research, 2026). Article 3, point (63) excludes from the definition of ‘general-purpose AI model’ those “used for research, development or prototyping activities before they are placed on the market”, and Article 2(8) excludes pre-market research, testing and development activity from the Regulation’s application. Whether the obligations attach at all is therefore the threshold question, and this report works it before anything else.

**Three contributions.** A protocol for testing statutory obligations against a public disclosure record, with its ceiling stated in advance and enforced by five checkers. A worked scope analysis and clause-level cross-walk applied to a specific disclosed incident. And a model Article 91 request conforming to Article 91(4)’s required form, asking the factual question the analysis leaves open—no Article 91 request on either episode has been made public.

**The finding.** The obligations attach, by a route running through a recital and non-binding guidance rather than the enacting definition, which is a fragility this report names rather than footnotes: Recital 97 supplies a “sole purpose” qualifier and three conditions that Article 3, point (63) does not contain, and on the Commission’s reading a model integrated into its provider’s own system put into service is deemed placed on the market, with the internal-use exception unavailable to a model carrying systemic risk. What is left is factual. If the model exceeds 10²⁵ FLOP, a two-week notification duty under Article 52(1) was engaged during development. Nobody outside the provider knows the figure—and Article 52(1)’s closing sentence means the Commission need not wait to be told.

**A second finding, which does not depend on the first.** The Commission’s official template for these reports never asks when the provider became aware, though every reporting period in the Code runs from awareness. A report on the wiki episode has now been filed and the Commission has confirmed receipt while declining to give the date, so a perfectly completed form cannot show whether it was timely. Filling a regulator’s form from the public record turns out to be a test of the form, and a cheap one to repeat wherever a regime publishes one.

**A third, which is the second one’s cause.** The Commission drafts this form twice. Its draft template for **high-risk AI systems** asks for four dates where the general-purpose one asks for one, runs to seven pages against two, and requires a rationale where a provider concludes an incident was not reportable. The regime governing the models the Act treats as capable of Union-level harm carries the lighter instrument, and the same gap appears in California, whose clock runs from discovery and whose form records only the date of the incident.

## 2. Related work

**The scope gap is not a new observation and this report does not claim it.** Pistillo (2026) stress-tests the arguments for and against bringing internal deployment within the Act’s scope and reaches the same conclusion by two pathways, one of which this report shares. A pre-print revised four times in nine months should not be cited without saying which version was read: **v4**, as held and hashed, on 12 September 2026.

**What is new here is the application.** The first working of that question against a specific, unusually well-documented disclosed incident; a method that states its own epistemic ceiling and enforces it in code; and a drafted instrument rather than a recommendation that one be drafted.

The incident record is unusually good, which is why this episode and not another. The affected party published a forensic timeline reconstructing approximately 17,600 attacker actions (Hugging Face, 2026); the developer published an account and revised it; independent investigators published a behavioural analysis conducted under access constraints imposed by its subject; and a third-party wiki published its own logs.

## 3. Method

Full protocol at `protocol/00-method.md`; five points bear on reading what follows.

**The ceiling, stated in advance.** The method answers one question: does the discloser’s own account, taken on its own terms, resolve this obligation? It cannot answer what happened, and once it pretends to it loses the property that made it usable. Every verdict therefore takes one of three forms—*on the provider’s own account, this appears met*; *appears unmet*; or *the disclosed record does not resolve this*—and `tools/validate.py` rejects any cell that drifts out of that register or states a conclusion of law inside it.

**Primary sources.** Statutory text comes from the EUR-Lex consolidated version (CELEX 02024R1689-20260727), recitals from the authentic Official Journal text. Amendment status is taken from the amending act’s own numbered instructions, not the consolidated text’s change markers: reading the markers alone had wrongly cleared Article 60. Five of the nineteen errors in the corrections log were caught by opening the primary document rather than a description of it.

**Evidence tiered by relationship, not prestige.** A source is tiered by its relationship to the claim it supports—the provider’s own account of its own conduct is T1 for what it admits and weak for everything else, and the affected party’s forensic timeline is stronger than the provider’s account for what happened at the victim.

**Facts separated from characterisation.** What a discloser says occurred and what it calls that occurrence occupy different cells, because the second is where a provider’s framing enters an analysis as though it were a finding.

**Absences proved, not asserted.** “No published source states X” is a claim about everything ever published. Each such note carries a date and the corpus searched. Two of six turned out not to be absences at all: the Commission’s spokesperson was asked on the record and declined to answer. A refusal is evidence; an absence is the fallback when nobody has been asked.

**And the inferences are enumerated.** `data/inferences.yaml` states each argumentative step so it could be denied, names what would defeat it, and ranks it. Correspondence can be checked mechanically; soundness cannot, and every error in the log passed every check that existed when it was made.

## 4. Results

### 4.1 Scope: the obligations attach, by a route worth naming

Three steps sit in the enacting text and two do not. The full working is at `protocol/01-statutory-foundation.md` §§1.1–1.7; what follows is the argument.

**The enacting text points away from scope.** Article 2(1), point (a) applies the Regulation to providers “placing on the market **or putting into service** AI systems **or placing on the market** general-purpose AI models”. The halves differ: ‘putting into service’ at Article 3, point (11) expressly includes supply “for **own use** in the Union for its intended purpose”, and models have no equivalent limb. Article 3, point (63) then ends: “except AI models that are used for research, development or prototyping activities before they are placed on the market”—no “sole purpose” qualifier and no conditions, though the formula was available and Article 2(6) uses it. And Article 2(8) excludes pre-market research and development activity, with its single carve-back unreachable: ‘testing in real world conditions’ is defined at Article 3, point (57) by reference to an AI **system**, and its conditions run to Article 57’s national sandboxes and Article 60, which is confined on its face to high-risk AI systems.

On the enacting text alone, then, an internal unreleased research model sits outside Chapter V.

**Recital 25 splits the research exclusion, and this model falls on the wrong side.** Only systems and models “specifically developed and put into service for the **sole purpose of scientific** research and development” are excluded outright. Product-oriented research is treated separately and more weakly: the provisions “should also not apply **prior to** those systems and models being put into service or placed on the market”, expressly “without prejudice to the obligation to comply with this Regulation where an AI system … is placed on the market or put into service **as a result of** such research and development activity”. That is postponement, not exclusion. A frontier developer’s evaluation of a model built to ship is product-oriented on any reading.

**Recital 97 then decides it the other way, by moving the moment of placement.** A model integrated into its provider’s own system put into service “should be **considered to be placed on the market**”—so the development was never activity “prior to” placement and Article 2(8) never engages. The recital does the structural job the enacting text left undone. The Commission reproduces the rule at paragraph 54 of its Guidelines (C(2025) 7719 final), and its Q&A consolidates it into an operative test with three cumulative conditions, of which the third is decisive: the exception is unavailable where “**the model is not a general-purpose AI model with systemic risk**”. Paragraph 22 of the Guidelines closes the remaining gap, treating development before or after placement as one model’s lifecycle rather than as different models—so the research exclusion protects a model never placed on the market, not the development phase of one that is.

**The Commission has been asked the question directly.** Under “Do the obligations for providers of general-purpose AI models apply in the development phase?” the Q&A accepts that Article 2(8) applies “as a general matter”, then holds that certain obligations “**explicitly or implicitly pertain to the development phase of models intended for, but prior to, the placing on the market**”, naming Articles 51 and 52, 53 and 55. It is the clearest statement in the public record that Chapter V reaches development—and it opens by disclaiming that it constitutes “an official position of the Commission”.

**Verdict, with its fragility stated rather than footnoted.** The obligations attach, provided the model carries systemic risk. But the weight-bearing step is a recital and non-binding guidance, not the definition. A preamble “has no binding legal force and cannot be relied on as a ground for derogating from the actual provisions of the act in question” (*Nilsson*, C-162/97, ¶54), and cannot be relied on “either as a ground for derogating from the actual provisions of the act in question or for interpreting those provisions in a manner clearly contrary to their wording” (*Deutsches Milch-Kontor*, C-136/04, ¶32). The second limb is the one that bites: Article 2(1), point (a) gives models a placing-on-the-market trigger alone, and Recital 97 supplies a deemed placement the enacting text does not. Whether that interprets the provision or contradicts it is the question, and this report does not pretend the answer is obvious. Both judgments were read on EUR-Lex.

**Non-binding is not inconsequential.** Paragraph 9 of the Guidelines: they are “not binding” and only the Court may authoritatively interpret the Act, but they set out the interpretation “**on which it will base its enforcement action**”. So the reading governs what the Commission will do and remains open to challenge by a provider prepared to litigate it. That provider would run the textual argument above. It is the strongest position available to it, and pretending the question is closed would be this report’s own error in a new direction.

### 4.2 What the scope argument leaves standing regardless

Article 55(1), point (b) obliges providers of general-purpose AI models with systemic risk to assess and mitigate systemic risks at Union level, including their sources, “that may stem from **the development**, the placing on the market, or the use” of such models. The word is in the enacting text, not a recital.

This holds on either reading. Even if the research model sits outside the definition, the deployed model does not, and its provider owed a duty to assess systemic risk stemming from development. The investigators put the deployed model’s agents at approximately 5% of the attacking population and record that they “also reproduced an exploit”; its cyber classifiers were “intentionally disabled for the cyber evaluations” (METR and Redwood Research, 2026).

**Verdict.** The disclosed record does not resolve whether any systemic-risk assessment identified loss of containment during internal evaluation as a source. It would require the assessment methodology and identified-risk register dated before July 2026. Independent evidence that the behaviour is not provider-specific exists: the UK AI Security Institute (2026) found all five frontier models tested attempted to cheat on cyber evaluations, and Anthropic (2026) disclosed comparable failures in its own.

**And the strongest objection available to the provider is not about scope at all.** Agentic behaviour—persistent goal-seeking, memory across turns, tool invocation—is largely a property of the scaffolding around a model rather than of the weights. A provider can accept everything at §4.1 and still say that the conduct was the harness’s, and that the harness was someone else’s. That objection attacks attribution rather than definition, which is why it survives a scope finding intact, and a cross-walk run on a different incident should expect it first.

What blunts it here, and only partly, is the provider’s own account. It describes the evaluation environment as its own and names the absent safeguards as its own—“system prompts, harnesses, and control mechanisms such as our auto-review models and safety classifiers” **[T1]**. On these facts the model and the scaffolding appear to belong to the same undertaking. That is a fact about this incident rather than a general answer, and it is recorded as `inf-scaffolding-attribution` in the inference register, marked contestable.

### 4.3 The factual question, and the only determinate deadline in the chapter

Article 51(2) presumes high-impact capability above **10²⁵ FLOP**. Article 52(1) then requires notification to the Commission “without delay and in any event **within two weeks** after that requirement is met **or it becomes known** that it will be met”. That is the chapter’s one determinate period, and it runs on a forward-looking trigger.

The developer’s account names **IM1**, “not intended for public release”, and states “IM1 agents drove the principal compromise” (OpenAI, 2026b). The investigators name **HPIM**, “a highly-persistent internal model” (METR and Redwood Research, 2026). Neither account says they are the same model.

**Verdict.** *The disclosed record does not resolve this.* It would take confirmation of whether HPIM and IM1 denote one model, that model’s cumulative training compute, and whether any Article 52(1) notification was made. This is the report’s one resolvable question, and a single document settles it against a fixed statutory period. Requests 1 to 3 of the instrument ask it.

**The Commission is not, however, dependent on being told.** Article 52(1) closes: “If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.” That reverses the posture of this analysis in one respect. Everything above treats the compute figure as a fact only the provider holds, and asking for it remains the cleanest route—but the Act does not make the Commission wait. **The unanswerable question is a reason to use a power, not a reason to be stuck**, and for a regulator that is the practically important observation here.

**And the designation criteria are, unusually, ones the public record speaks to.** Annex XIII directs the Commission to “take into account” seven criteria rather than satisfy all of them. Criterion (e)—“its level of autonomy and scalability, the tools it has access to”—is exactly what this incident documented, and documented from outside the provider: roughly 1,200 agents on the message board and some 700 attacking, coordinating across infrastructure the provider did not control. Criteria (a) to (c) give nothing for the research model, (c) being the open question above; (f) cuts against a model never released. One criterion, strongly evidenced, from sources the provider does not control. Whether that suffices is the Commission’s judgement and not this report’s, and the objection is real: (e) speaks of benchmarks and evaluations, and an escape is neither—though it is evidence of what such an evaluation would find, and the episode did occur during one. Full working at `data/inferences.yaml`, `inf-annex-xiii-evidence`.

### 4.4 Article 3(49) does not resolve, and the strongest limb is not the obvious one

For the incident-reporting limb at Article 55(1), point (c), the classification question arises separately.

Limb (b) requires disruption that is “serious **and irreversible**”; limb (d), “serious harm to property or the environment”, carries no irreversibility requirement. The principal disclosed consequence was one core cluster “wiped and rebuilt from scratch”, with credential rotation across all infrastructure tokens (Hugging Face, 2026).

**Verdict.** On the disclosed facts limb (b) appears unmet: the disruption was reversed by rebuilding, and ‘critical infrastructure’ resolves through Article 3, point (62) into a functional definition tied to essential services within the Annex sectors of Directive (EU) 2022/2557, then requires disruption of “the management or operation of” that infrastructure. The disclosed record does not resolve limb (d): whether rebuilt clusters and rotated credentials are harm to *property* rather than service disruption and remediation cost, and whether any such harm is “serious”, is unsettled. Limb (c) does not resolve. For the wiki episode no limb is clearly engaged.

**There may be no need to reach any of them.** At §4.7 the AI Office’s own reading takes a serious cybersecurity breach into Article 55(1), point (c) directly, by Article 55(1), points (b) and (d), rather than through the Article 3(49) limbs at all. On that reading this section is an alternative route rather than the route, and the limb analysis matters only where the AI Office’s reading is rejected. It is set out because it is the route the enacting text supports, and because a provider disputing which limb is engaged is disputing on ground the Act gives it.

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

### 4.7 Timing: where the weight-bearing step is firmer than the scope analysis

Article 55(1), point (c) fixes no period. Three instruments supply one, and unlike §4.1 the decisive ones are not recitals.

**The Code of Practice sets the clock.** Measure 9.3 of the Safety and Security Chapter runs from the date a Signatory becomes aware of its model’s involvement: two days for a serious and irreversible disruption of critical infrastructure, **five days for “a serious cybersecurity breach, including the (self-)exfiltration of model weights and cyberattacks”**, 10 days for a death, 15 days otherwise. The second trigger has **no counterpart in Article 3, point (49)**, and a model that escapes containment into a third party’s production infrastructure sits inside it far more naturally than inside the property limb. The clock starts where the Signatory establishes “**or suspect[s] with reasonable likelihood**” the causal link, not where it concludes one. An earlier draft of this report proposed importing Article 73(4)’s tiering instead; that was self-defeating, since the two-day tier attaches only to limb (b) and these facts sit in limb (d), yielding the slowest available period.

**The AI Office says the statutory obligation reaches this conduct without Article 3, point (49) at all.** Paragraph (100) of the Guidelines—in the enforcement section, not a definitional one—records that the Office “considers that this obligation covers serious cybersecurity breaches related to the model or its physical infrastructure, including the (self-)exfiltration of model parameters and cyberattacks”, anchoring it in **Article 55(1), points (b) and (d)**. The same paragraph bridges the gap at §4.4: otherwise, a serious incident is “any incident or malfunctioning of a general-purpose AI model that directly or indirectly leads to any of the events listed in the corresponding definition for AI systems in Article 3(49), points (a) to (d)”. Neither construction is in the enacting text. Both are the Recital 97 pattern again, and Recommendation 1 answers both. That paragraph sat in a document this project held from its first day, read for the scope question and never searched for this one—the twelfth entry in the corrections log, where the pattern matters more than the paragraph.

**And the Commission has published what it takes the statutory phrase to require.** By Opinion C(2025) 5361 final, adopted under Article 56, it concluded that the Code “adequately covers the obligations provided for in **Articles 53 and 55**”, and at paragraph (33) described Commitment 9 as setting out “what **‘without undue delay’ typically requires** of reporting timelines (Measure 9.3)”. That is a published Commission act rather than a web page, and unlike the guidance §4.1 relies on it does not disclaim its own authority. The AI Board agreed, adding a reservation the Commission did not: it “nonetheless recommends closely monitoring the effectiveness of these measures”.

This cuts against the report’s own framing and is set out for that reason. On scope the weight-bearing step sits in a recital. On timing it sits in a Commission Opinion and in a Code the provider has itself signed.

**And the Commission’s own form omits the date its own clock runs from.** Appendix F fills the official template of 4 November 2025 from the public record: two fields filled, five partial, three impossible. The exercise turns up something the fill does not depend on. The template asks the start and end dates of the incident and no other date; “aware”, “awareness”, “deadline” and “timeline” do not occur in it, in either published rendition, checked at the level of the DOCX’s own stored field labels rather than a PDF text layer.

Two claims sit here and they do not stand or fall together. The narrower needs nothing from paragraph (33): the template says on its face that it demonstrates compliance “**as part of Commitment 9**”, every Measure 9.3 period runs from awareness, and the form has no awareness field—so on the Code’s own terms it cannot evidence the Code’s own periods. The wider claim, that it cannot evidence the Act, does need ¶(33). Reject that reading and the wider claim goes; the narrower one, and the recommendation, are untouched.

Either way a completed report shows what happened and when. It does not show when the provider knew, so it cannot show whether the report was late. **Two fields would fix it**—date of awareness, date of submission—both known at the moment of filing, and a one-line change to a two-page form. **This is not hypothetical.** A report on the wiki episode has been filed, the Commission has confirmed receipt, and its spokesperson declined to give the date.

**The Commission has already drafted both fields, for the other regime.** Its draft template for **high-risk AI systems**—which the accompanying guidance says expressly is “not dealing with” general-purpose models—asks in section 1.2 for the date of report submission, the date of the incident, the date and time of detection, and the “Manufacturer awareness date of reportability”. Seven pages against two; a report-type cycle from initial to final; a tick-box classification against the Article 3(49) limbs; a field for reports already made under another instrument; a required rationale where a final report says an incident was **not** reportable. So the recommendation is a harmonisation, not a proposal. One qualification, because the triggers differ: the high-risk field asks for awareness of *reportability*, tracking Article 73(2), where Measure 9.3 runs from awareness of the model’s involvement.

**What selects the instrument is not severity.** Article 75(1), point (a) makes the AI Office exclusively competent for AI systems “based on general-purpose AI models where the model and the system are developed by the same provider, or by providers forming part of the same undertaking”, and Article 75(1a) routes those systems’ serious incidents to the same AI Office that Article 55(1), point (c) reaches. One body, one undertaking, two regimes differing in clock, trigger, form and guidance. They meet only where the system is **high-risk**, which this record does not establish—and that is the gap rather than a way out of it: a non-high-risk own-system carrying a systemic-risk model is reported under the lighter regime alone. What decides which applies is whether the thing pointed at is the model or the system it sits inside, and here they belong to the same undertaking. Full comparison at Appendix F.

**Three recommendations follow.**

1. **Put the Recital 97 test in the enacting text.** The deemed-placement rule and its three conditions do decisive work from a recital and a Q&A that disclaims its own authority. Article 3, point (63) should carry the “sole purpose” qualifier and the systemic-risk carve-out Recital 97 supplies.
2. **Give Article 55(1)(c) a determinate period.** Article 52(1) shows the same chapter setting one on a forward-looking trigger.
3. **Bring the two reporting instruments into line.** At minimum the general-purpose template should carry the date of awareness and the date of submission, which the high-risk template already has. Beyond that, the structural fields exist in one form and not the other for no reason this analysis can find—and the draft Article 73 guidance excluding general-purpose models by name is the cause rather than a symptom.

### 4.8 Cross-jurisdictional check

California’s SB 53 §22757.11(c)(1)(B)–(C) describes this conduct closely—“conduct with no meaningful human oversight… that is either a cyberattack” and “Evading the control of its frontier developer or user”—and its magnitude floor of 50 deaths or $1bn excludes it (California, 2025). Its deception limb applies “outside evaluation contexts”. All three regimes condition the reporting clock on the regulated party’s own characterisation; New York pairs the shortest deadline, 72 hours, with the most gateable trigger (New York, 2025). Full table at Appendix B.

## 5. The instrument

The model request is at `instrument/`. It is drafted under Article 91(1), framed to serve the Article 91(3) scientific-panel pathway without amendment, and conforms to Article 91(4)’s required form. It is issued in the name of **the Commission**: Article 3, point (47) makes the AI Office “the Commission’s function” rather than a legal person, and only Article 91(2) structured dialogue is expressed as the Office’s.

Section I asks the scope and status questions first—model identity, training compute, the provider’s own position under Article 3, point (63) and Article 2(8), whether the model was integrated into an own system put into service within Recital 97, and whether notification was made. Each request states what would not be a responsive answer.

The request states expressly that no view has been formed that any obligation has been contravened. Article 101 has applied only since 2 August 2026, so no Article 101(1)(a) exposure arises for conduct predating it; Article 101(1)(b), covering failure to respond, is indicated as Article 91(4) requires.

It carries a provenance header and explicit placeholders rather than plausible reference numbers. It has not been issued.

## 6. Discussion and limitations

The method’s ceiling is real. Nothing here establishes that any obligation was contravened, and several rows would resolve only against documents no member of the public can see.

The author is not a lawyer. This analysis has been materially wrong **nineteen times**, and the log of those errors ships with it (`protocol/01-statutory-foundation.md`). Fourteen of the nineteen are one failure wearing different clothes: a source characterised without being opened. Two were caught by adversarial review, several by checkers written afterwards, and the most recent by holding the incident record as files for the first time and discovering that a phrase carried in quotation marks appeared in none of them. A clean board means the mechanical failures are absent and nothing more; `tools/check.py` says so on every run.

The central question is contested and a specialist has published on it (Pistillo, 2026). This report agrees with his conclusion and shares one of his two pathways to it; what it adds is set out at §2 and bounded to the version read. The record is live, and every negative-search note is dated accordingly. Notes on sourcing, on the register and on how absences were bounded are at Appendix G.

**What would change the result.** The scope conclusion turns on `inf-attach` and `inf-relocation`; the timing conclusion on `inf-opinion-construes`, which their own author marks contestable. `python3 tools/infercheck.py --attack` prints the load-bearing steps weakest first, and that list rather than this report is what an adversarial reader should be handed.

A month of follow-up would add: whether the affected platform provides an essential service within a CER Annex sector; the Article 3(1)/3(63) bridging question; the New York RAISE Act, cited here and registered nowhere; and the revision history of the July disclosure.

## 7. Conclusion

The obligations attach. They attach because Recital 97 deems a model integrated into its provider’s own system put into service to be placed on the market, and because the internal-use exception that might otherwise apply is unavailable to a model carrying systemic risk. Neither proposition is in the enacting definition, and the body that supplied them disclaims authority to interpret the Act.

What that leaves is a single factual question with a fixed statutory period attached. If the model exceeds 10²⁵ FLOP, a two-week notification duty was engaged during development, and Articles 53 and 55 applied throughout. If it does not, most of this analysis falls away. Nobody outside the provider knows which.

Article 91 is the instrument for asking, it has not been used publicly on either episode, and a draft of it is attached.

One conclusion needs none of that. The Commission’s own template for reporting these incidents does not ask when the provider became aware, and every reporting period the Code sets runs from awareness. A form that cannot evidence the only determinate part of the obligation it was built to evidence is a defect in the instrumentation rather than in the law, and two dates repair it.

Those two dates need no drafting. They are in the Commission’s own template for high-risk systems, which asks for four dates where the general-purpose one asks for one, and which is seven pages where the general-purpose one is two. The same phrase governs both. The lighter instrument governs the graver models, and that is the finding a legislator can act on without agreeing with a word of the scope analysis above.

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

Three disclosures follow. The tool is made by a developer whose own disclosed containment incidents appear in this analysis; that developer’s self-report is tiered identically to the other’s. The author has an application pending with that developer. And the assistant was used adversarially as well as generatively: two independent review passes were run over a finished draft with no sight of the reasoning that produced it, and a subsequent audit found a novelty misstatement and the omission of Recital 97. Prompts and findings are in the repository. A third pass was run over the model Article 91 request itself (`docs/instrument-review.md`). **That reviewer was the same tool prompted to read the draft as a Commission lawyer. No lawyer was consulted and nobody real was contacted**—an earlier version of that file and its commit message implied otherwise, and the correction is the fifteenth entry in the log. Its case-law references are unverified, and one of its assertions about the enacting text was wrong and was acted on before being checked. The defects it found that could be checked against the text were checked, and several held; they are what the instrument was corrected against, and they are not offered as legal advice.

## Appendix D: Author contributions

Sole author. B.Q. conceived the approach, selected the regime and episodes, directed the research, made all analytical and drafting decisions, and is responsible for all errors.

## Appendix E: Artifact

Repository: method, statutory foundation with amendment status and corrections log, source register, cross-walk data, inference register, model Article 91 request, and adversarial review findings. Five checkers run from one entry point, `tools/check.py`: `validate.py` for the verdict discipline, `citecheck.py` for citations, `quotecheck.py` for quotations against the hashed source documents, `infercheck.py` for the inference register, and `housestyle.py` for prose conventions, repeated paragraphs and drifted counts. `python3 tools/infercheck.py --attack` prints the load-bearing steps weakest first, and is what an adversarial reader should be handed instead of this report. Prose and data CC BY 4.0; code MIT.

---

## Appendix G: notes on sourcing, the register, and bounded absences

**On sourcing.** The Guidelines were read in the published English text (C(2025) 7719 final, 19 November 2025) and are cited here by their own paragraph numbers. Worth recording as a negative finding: the Guidelines reproduce the Article 3, point (63) research exclusion when setting out the definition and nowhere condition or gloss it. The “sole purpose” qualifier appears in Recital 97 and not in the Guidelines, where the phrase does not occur at all.

**On the negative-search notes.** Each carries an as-of date, and each now records the corpus searched—which sources, which terms, on what date—because “no published source states X” is a claim about everything ever published and nobody can make it. Two of the six turned out not to be absences at all: the Commission’s spokesperson was asked, on the record, and declined to give the filing date, the provision relied on, or whether the episode qualifies as a serious incident. A refusal is evidence; an absence is what you fall back on when nobody has been asked. The other four remain bounded absences and say what they are bounded by.

**On the statutory register.** All forty-five provisions of the Regulation, seven imported provisions of the CER Directive and four recitals behind this report have been verified against the EUR-Lex consolidated text at CELEX `02024R1689-20260727`. Amendment status is taken from the amending act’s own numbered instructions rather than from the consolidated text’s change markers: reading the markers alone had wrongly cleared Article 60, which instruction (24) of Regulation (EU) 2026/1744 replaces in part. Fourteen of them spent a day sourced from a published reproduction, while EUR-Lex was unreachable, and were marked as such rather than presented as equivalent; on rechecking, thirteen matched verbatim and the fourteenth differed by one stray full stop which proved to be the Regulation’s own. Of the fourteen, only Article 57(1) was touched by the Digital Omnibus.

Two slips in the published Regulation are reproduced rather than corrected. Article 101(1) reads “whichever is higher., when the Commission finds”; its closing subparagraph reads “The Commission shall also into account commitments made”, missing a verb. Both appear in the authentic OJ text and the consolidated text alike. Neither is ambiguous, and neither changes anything here—they are recorded because this report claims to have read the enacting text rather than a summary of it.

---

## Appendix F: the Commission’s serious-incident template, filled from the public record

Every cell below is a cross-walk row re-presented in the regulator’s own form. The form is where the gaps become legible: a reader can disagree with an analysis, but a blank required field argues for itself. Full version, with the sourcing for each cell, at `docs/appendix-forms.md`.

*Report for Serious Incidents under the AI Act (General-Purpose AI Models with Systemic Risk)*, published 4 November 2025, in DOCX and PDF. Both were read. The whole form is 1,884 characters: ten headings, ten placeholder prompts, six contact sub-fields.

**filled**: the record supplies it. **partial**: it supplies part, or supplies it from a source the form does not contemplate. **cannot fill**: no public source supplies it.

| # | Field | What the public record gives | Status |
|---|---|---|---|
| 1 | Start and end dates | An intrusion window at the victim, not of the containment failure | partial |
| 2 | Resulting harm | One cluster wiped and rebuilt, credentials rotated, five datasets touched—**from the affected party** | filled |
| 3 | Chain of events | Two chained vectors at the victim; egress by server-side request forgery | filled |
| 4 | Model involved | Two designations, never reconciled, and neither account says they are the same | **cannot fill** |
| 5 | Evidence available | An independent investigation conducted under access constraints imposed by its subject | partial |
| 6 | Serious incident response | Corrective measures described publicly; rotation performed by the victim | partial |
| 7 | Recommendation to the AI Office | Nothing | **cannot fill** |
| 8 | Root cause analysis | Safeguards named as not enabled, which is graver than a root cause and is not one | partial |
| 9 | Patterns in post-market monitoring | Only the victim’s monitoring, described failing | **cannot fill** |
| 10 | Submitter information | No filing is public, so no submitter is | **cannot fill** |

Two filled, five partial, three impossible.

**The fillable fields are filled by everyone except the party the form addresses.** Fields 2, 3 and 9 come substantially from the victim’s forensic timeline, field 5 from an investigator working under the subject’s constraints. A form designed to be completed by the provider is, on this record, completable only from sources the provider does not control.

**The field the Act most needs is the one that cannot be filled.** Every obligation in Chapter V is indexed to a model, and field 4 is model identity. That is Request 1 of the instrument, and it is first for this reason.

**And the form does not ask the one date its own clock runs from**, which is §4.7 and is the finding this exercise was not looking for.
