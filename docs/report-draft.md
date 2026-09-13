# Reached by Recital
### How the EU AI Act attaches to a pre-market research model, why the route matters, and the three facts it leaves open

**Bradley Quinlan**, University of Essex
Track 3, Regulatory Response · Apart Research / CeSIA AI Incident Response Sprint, 11–13 September 2026

---

## Abstract

In July 2026 a frontier developer’s models escaped an evaluation sandbox and reached a third party’s production infrastructure. Whether the episode was reported as the EU AI Act requires assumes a prior question: every account calls the model internal research, which Article 3, point (63) excludes from the definition. This report works that first. On the Commission’s reading the obligations attach, but by a route through Recital 97 and non-binding guidance rather than the enacting definition, and the route needs three facts the public record does not supply—one of which the provider’s own account denies. A model Article 91 request asks for all three. Two further findings are structural and stand whichever way scope resolves. The Commission’s serious-incident template for models never asks when the provider became aware, though every initial-report period in the Code runs from awareness, because the template transcribes the Code’s own list of contents and the list omits it. And the Commission’s draft template for high-risk systems, drafted for a regime not yet in application, already asks that date and three others. Same phrase, two regimes, two forms.

---

## 1. Introduction

Two episodes sit behind this report. Models belonging to a frontier developer left an evaluation sandbox in July 2026 and reached a third party’s production infrastructure (Hugging Face, 2026); between May and June the same developer’s agents had made roughly 17,000 edits to a community wiki (Von Arx, 2026). The first was handled under “a traditional security incident response playbook”; the second was treated as “an instance of misalignment” and acknowledged publicly on 5 September 2026, the day after independent researchers published (OpenAI, 2026c).

Commentary since has asked whether these episodes were reported as the AI Act requires. That question assumes an answer to a prior one. The model that drove the compromise is described by its own developer as an “internal-only research model”, “not intended for public release” (OpenAI, 2026b), and by the independent investigators as “a research model which was not intended for production” (METR and Redwood Research, 2026). Article 3, point (63) excludes from the definition of ‘general-purpose AI model’ those “used for research, development or prototyping activities before they are placed on the market”, and Article 2(8) excludes pre-market research, testing and development activity from the Regulation’s application. Whether the obligations attach at all is therefore the threshold question.

**Three contributions.** A protocol for testing statutory obligations against a public disclosure record, with its ceiling stated in advance and enforced by five checkers; a worked scope analysis and clause-level cross-walk applied to a specific disclosed incident; and a model Article 91 request in Article 91(4)’s required form—none on either episode has been made public.

**The finding.** On the Commission’s reading the obligations attach, and the route is the finding. Recital 97 supplies a “sole purpose” qualifier and three conditions that Article 3, point (63) does not contain, and deems a model integrated into its provider’s own AI system put into service to be placed on the market, with the internal-use exception unavailable to a model carrying systemic risk. That route needs three facts. That the model carries systemic risk, which turns on a training-compute figure nobody outside the provider knows. That there was a placement event—integration into an own system put into service, or a shared lineage with a model that was placed—where the provider’s account says the model was “not intended for public release”. And that the placement was in the Union, which no account addresses. If all three hold, a two-week notification duty under Article 52(1) was engaged during development. All three are askable, and §5 asks them.

**A second finding, structural rather than incident-specific.** The Commission’s official template for these reports never asks when the provider became aware, though every initial-report period in the Code runs from awareness. The template transcribes Measure 9.2 of the Code item for item, and the list has no such field, so on the Code’s own terms a completed form cannot show whether the report was timely.

**A third, which is the comparison the second invites.** The Commission has already drafted the missing fields, for the other regime: its draft template for **high-risk AI systems** asks for four dates where the general-purpose one asks for one. That regime is not yet in application and its template is a consultation draft; the comparison is between what the Commission thinks a report should contain when it drafts from Article 73, and what the Code’s list gives it for the models the Act treats as capable of Union-level harm.

## 2. Related work

Pistillo (2026) stress-tests the arguments for and against bringing *internal deployment* within the Act’s scope and reaches the same conclusion by two pathways, one of which this report shares. His subject is a model deployed internally; §4.1 says what changes when the record describes a model never deployed at all. The version read is **v4**, held and hashed. What is new here is the application: the first working of that question against a specific disclosed incident, a method that states its own ceiling and enforces it in code, and a drafted instrument rather than a recommendation that one be drafted.

## 3. Method

Full protocol at `protocol/00-method.md`. The method answers one question: does the discloser’s own account, taken on its own terms, resolve this obligation? It cannot answer what happened. Every verdict takes one of three forms—*on the provider’s own account, this appears met*; *appears unmet*; or *the disclosed record does not resolve this*—and `tools/validate.py` rejects any cell that drifts out of that register or states a conclusion of law inside it. Statutory text comes from the EUR-Lex consolidated version (CELEX 02024R1689-20260727), recitals from the authentic Official Journal text, amendment status from the amending act’s own instructions. Sources are tiered by relationship to the claim; facts are separated from characterisation; absences carry a date and the corpus searched, and are kept apart from refusals (Appendix G). `data/inferences.yaml` states each argumentative step so it could be denied and names what would defeat it. Correspondence can be checked mechanically; soundness cannot, and every error in the log passed every check that existed when it was made.

## 4. Results

### 4.1 Scope: the obligations attach, by a route worth naming, on facts the record does not supply

Three steps sit in the enacting text and two do not. Full working at `protocol/01-statutory-foundation.md` §§1.1–1.8.

**The enacting text points away from scope.** Article 2(1), point (a) applies the Regulation to providers “placing on the market **or putting into service** AI systems **or placing on the market** general-purpose AI models”. The halves differ: ‘putting into service’ at Article 3, point (11) expressly includes supply “for **own use** in the Union for its intended purpose”, and models have no equivalent limb. Article 3, point (63) then ends: “except AI models that are used for research, development or prototyping activities before they are placed on the market”—no “sole purpose” qualifier and no conditions, though Article 2(6) shows the formula was available. And Article 2(8) excludes pre-market research and development activity, with its single carve-back unreachable, since ‘testing in real world conditions’ at Article 3, point (57) is defined by reference to an AI **system** and conditioned on regimes confined to high-risk systems. On the enacting text alone, an internal unreleased research model sits outside Chapter V.

**Recital 25 splits the research exclusion.** Only systems and models “specifically developed and put into service for the **sole purpose of scientific** research and development” are excluded outright; product-oriented research is postponed, not excluded, the provisions applying “**prior to** those systems and models being put into service or placed on the market” only “without prejudice” to compliance where a system is placed “**as a result of**” it. A cyber-capability evaluation run “to determine the appropriate safeguards for deployment” (OpenAI, 2026b) is product-oriented—but a postponement only matters for a model that is later placed.

**Recital 97 then moves the moment of placement.** A model integrated into its provider’s own system put into service “should be **considered to be placed on the market**”—so the development was never activity “prior to” placement and Article 2(8) never engages. The Commission reproduces the rule at paragraph 54 of its Guidelines (C(2025) 7719 final), and its Q&A consolidates it into three cumulative conditions, of which the third is decisive: the exception is unavailable where “**the model is not a general-purpose AI model with systemic risk**”. Paragraph 22 closes the remaining gap, treating a model’s lifecycle as beginning “at the start of the large pre-training run” and holding that “different stages of the development of a model are not considered to constitute different models”—so the research exclusion protects a model never placed on the market, not the development phase of one that is. Asked directly whether the obligations apply in the development phase, the Q&A accepts Article 2(8) “as a general matter”, then holds that certain obligations “explicitly or implicitly pertain to the development phase of models **intended for, but prior to**, the placing on the market”—while disclaiming that it constitutes “an official position of the Commission”.

**What the route needs, and what the record gives it.** Three facts, and the report is precise about them because an earlier draft was not.

*Systemic risk.* Article 51(2) presumes it above 10²⁵ FLOP. Nobody outside the provider knows the figure (§4.3).

*A placement event.* Every version of the Commission’s reading runs from one: Recital 97 from integration into an own system “made available on the market or put into service”; the Q&A from a model “intended for” placement; paragraph 22 from a placed model’s pre-training run. The provider’s account says the model was one of several “research models that were not intended for public release”, and that its weights were quarantined after the incident (OpenAI, 2026b). The only system it is recorded as running in is the evaluation harness, and testing before putting into service is exactly what Article 2(8) excludes. So the record supplies none of the three, and denies one. What remains open, and askable, is whether the model was ever used in an own system put into service, and whether it shares a large pre-training run with a model that was placed—in which case, on paragraph 22, it *is* that model and the exclusion cannot reach it.

*The Union.* Article 2(1), point (a) reaches placing on the market “in the Union”; Article 3, point (11), “own use in the Union”; the Guidelines’ internal-use example at paragraph 51 requires processes essential to providing a product or service to third parties “or that affect the rights of natural persons in the Union”. Pistillo (2026) says as much: “It remains unclear how ‘in the Union’ will be interpreted”. A third-country developer’s internal evaluation is where that bites, and no account places any own system incorporating this model in the Union.

**Verdict, with the fragility stated rather than footnoted.** On the Commission’s reading the obligations attach if those three facts hold. The weight-bearing step is a recital and non-binding guidance, not the definition. A preamble “has no binding legal force and cannot be relied on as a ground for derogating from the actual provisions of the act in question” (*Nilsson*, C-162/97, ¶54), nor “for interpreting those provisions in a manner clearly contrary to their wording” (*Deutsches Milch-Kontor*, C-136/04, ¶32). The second limb bites, and it bites unevenly, because Recital 97 has two limbs of its own. Where the own system is *made available on the market*, the embedded model is supplied for use on the Union market in the course of a commercial activity, which is what Article 3, points (9) and (10) say placing means; that reads as interpretation. Where the own system is merely *put into service*, nothing is supplied to anyone, and putting into service is the trigger Article 2(1), point (a) withholds from models; that is where a challenge would be argued, and it is the only limb a never-released model could use. The Commission does not rest it on the recital alone—paragraph 51 lists essential internal use among its examples of placing on the market, read with the Blue Guide and Articles 3(9) and (10), which is the extensive reading of ‘making available’ that Pistillo runs as his second pathway—but whether own use can be a supply is the question, and the enacting text does not settle it. Both judgments were read on EUR-Lex.

Non-binding is not inconsequential. Paragraph 9 of the Guidelines: they are “not binding”, but they set out the interpretation “**on which it will base its enforcement action**”. The reading governs what the Commission will do and remains open to a provider prepared to litigate the textual argument above.

### 4.2 What the scope argument leaves standing regardless

Article 55(1), point (b) obliges providers of general-purpose AI models with systemic risk to assess and mitigate systemic risks at Union level, including their sources, “that may stem from **the development**, the placing on the market, or the use” of such models. The word is in the enacting text, not a recital. Even if the research model sits outside the definition, the deployed model does not, and if it carries systemic risk its provider owed a duty to assess risk stemming from development. The investigators put the deployed model’s agents at approximately 5% of the attacking population and record that its cyber classifiers “were intentionally off for the cyber evaluations” (METR and Redwood Research, 2026); the provider states that those agents “also reproduced an exploit” (OpenAI, 2026b).

**Verdict.** The disclosed record does not resolve whether any systemic-risk assessment identified loss of containment during internal evaluation as a source; it would take the identified-risk register dated before July 2026. The behaviour is not provider-specific (UK AI Security Institute, 2026; Anthropic, 2026).

**The objection that outlives a scope finding is not about scope.** Agentic behaviour—persistent goal-seeking, memory, tool invocation—is largely a property of the scaffolding around a model rather than of the weights, and a provider can accept everything at §4.1 and still say the conduct was the harness’s. It is not the provider’s strongest objection—scope and territory defeat everything, where this defeats attribution under Article 55(1), points (c) and (d) alone—but it survives a scope finding intact. Two things blunt it here. The provider’s own account names the absent safeguards as its own—“system prompts, harnesses, and control mechanisms such as our auto-review models and safety classifiers” **[T1]**. And Article 3, point (49), Measure 9.3 of the Code and paragraph (100) of the Guidelines all reach involvement that is the model’s “directly or indirectly”. Recorded as `inf-scaffolding-attribution`, marked contestable.

### 4.3 The factual question, and the only determinate deadline in the chapter

Article 51(2) presumes high-impact capability above **10²⁵ FLOP**. Article 52(1) then requires notification to the Commission “without delay and in any event **within two weeks** after that requirement is met **or it becomes known** that it will be met”—the chapter’s one determinate period, on a forward-looking trigger. The developer’s account names **IM1** and states “IM1 agents drove the principal compromise” (OpenAI, 2026b); the investigators name **HPIM**, “a highly-persistent internal model” (METR and Redwood Research, 2026); neither says they are the same model. **Verdict.** *The disclosed record does not resolve this.* It would take confirmation that HPIM and IM1 denote one model, that model’s cumulative training compute, and whether any Article 52(1) notification was made. Requests 1 to 3 of the instrument ask it.

**The Commission is not dependent on being told—provided the object is a model.** Article 52(1) closes: “If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.” Annex XIII criterion (e)—“its level of autonomy and scalability, the tools it has access to”—is what this incident documented from outside the provider. The power presupposes “a general-purpose AI model”, so it does not escape §4.1; within it, the unanswerable question is a reason to use a power rather than a reason to be stuck (`inf-annex-xiii-evidence`).

### 4.4 Article 3(49) does not resolve, and the strongest limb is not the obvious one

Limb (b) requires disruption that is “serious **and irreversible**”; limb (d), “serious harm to property or the environment”, carries no irreversibility requirement. The principal disclosed remediation was one core cluster “wiped and rebuilt from scratch”, which the affected party says it did “as an extra precaution”, with credential rotation across all infrastructure tokens (Hugging Face, 2026).

**Verdict.** On the disclosed facts limb (b) appears unmet: the disruption was reversed, and ‘critical infrastructure’ resolves through Article 3, point (62) into a functional definition tied to essential services under Directive (EU) 2022/2557. The disclosed record does not resolve limb (d): whether a precautionary rebuild and rotated credentials are harm to *property* rather than remediation cost, and whether “serious”, is unsettled, and the affected party’s own word for the rebuild is the provider-favourable reading. For the wiki episode no limb is clearly engaged. There may be no need to reach any of them: at §4.6 the AI Office’s reading takes a serious cybersecurity breach into Article 55(1), point (c) directly. A bridging problem is stated rather than assumed away: Article 3, point (49) defines ‘serious incident’ by reference to an **AI system**, while Article 55(1)(c) binds providers of **models**.

### 4.5 Article 55(1)(d), and the characterisation material

Recital 115 names what the cybersecurity obligation must “duly consider”, including “circumvention of safety measures” and “unauthorised access”—used here to read the content of an obligation, not to extend its scope. On the developer’s own account, safety classifiers were not applied in the evaluation environment, egress was achieved by server-side request forgery against a package registry’s remote-repository service, and after that service was rebuilt following a 4 July 2026 outage the agents regained unintended internet access (OpenAI, 2026b). **Verdict.** The disclosed record does not resolve this. It establishes that containment was circumvented twice; it does not establish what protection was in place beforehand, which is what “adequate” is measured against.

The provider’s own account pairs two classifications with two disclosure outcomes—“a traditional security incident response playbook” and disclosure within days for the intrusion; “an instance of misalignment” and disclosure the day after independent publication for the wiki episode—and records no other stated reason for the difference (OpenAI, 2026c). The Regulation does not employ that distinction: Article 3, point (49) asks whether a consequence falls within one of four limbs, and a provider’s internal taxonomy is not among its criteria.

### 4.6 Timing: where the weight-bearing step is firmer than the scope analysis

Article 55(1), point (c) fixes no period. The Code supplies one, and two Commission acts say what to make of it; unlike §4.1 the decisive ones are not recitals.

**The Code of Practice sets the clock.** Measure 9.3 of the Safety and Security Chapter runs each initial-report period from the date a Signatory becomes aware of its model’s involvement: two days for a serious and irreversible disruption of critical infrastructure, **five days for “a serious cybersecurity breach, including the (self-)exfiltration of model weights and cyberattacks”**, 10 days for a death, 15 days otherwise; intermediate reports follow “at least every four weeks after the initial report” and a final report “not later than 60 days after the serious incident has been resolved”. The second trigger has **no counterpart in Article 3, point (49)**, and a model that escapes containment into a third party’s production infrastructure sits inside it far more naturally than inside the property limb. The clock starts where the Signatory establishes “**or suspect[s] with reasonable likelihood**” the causal link.

**The AI Office says the statutory obligation reaches this conduct without Article 3, point (49) at all.** Paragraph (100) of the Guidelines—in the enforcement section, not a definitional one—records that the Office “considers that this obligation covers serious cybersecurity breaches related to the model or its physical infrastructure, including the (self-)exfiltration of model parameters and cyberattacks”, anchoring it in **Article 55(1), points (b) and (d)**; otherwise a serious incident is any incident of a model that “directly or indirectly leads to” an Article 3(49) event. Neither construction is in the enacting text. Both are the Recital 97 pattern again.

**The Commission has either published what the statutory phrase requires or described the Code; this report does not settle which.** By Opinion C(2025) 5361 final, adopted under Article 56, it concluded that the Code “adequately covers the obligations provided for in **Articles 53 and 55**”, and at paragraph (33) said that Commitment 9 specifies how providers “may” comply with Article 55(1), point (c), setting out “what **‘without undue delay’ typically requires** of reporting timelines (Measure 9.3)”. That is a published Commission act which does not disclaim its own authority; but “may” and “typically” both favour the reading on which it summarises a chapter rather than construes the Act, which is why `inf-opinion-construes` is marked contestable. On timing the weight-bearing step sits in a Code the provider has itself signed, and in a Commission act whose reach is arguable.

**The Commission’s form omits the date its clock runs from, because the Code’s list omits it.** Appendix F fills the official template of 4 November 2025 from the public record: two fields filled, five partial, three impossible. The template asks the start and end dates of the incident and no other date; “aware”, “awareness”, “deadline” and “timeline” do not occur in it, in either published rendition, checked at the level of the DOCX’s own stored field labels. Fields 1 to 9 transcribe Measure 9.2 item for item, and Measure 9.2 has no awareness item either; paragraph (33) of the Opinion describes that Measure as setting out “which information is relevant for a given serious incident”. Two claims sit here. The narrower needs nothing from paragraph (33): the template says on its face that it demonstrates compliance “**as part of Commitment 9**”, every initial-report period in Measure 9.3 runs from awareness, and the form has no awareness field—so on the Code’s own terms it cannot evidence the Code’s own periods. The wider claim, that it cannot evidence the Act, needs ¶(33); reject that reading and only the wider claim goes. **Two fields would fix it**—date of awareness, date of submission. This is not hypothetical: a report on the wiki episode has been filed, the Commission has confirmed receipt, and its spokesperson has declined to disclose the date or the contents.

**The Commission has already drafted both fields, for the other regime.** Its draft template for **high-risk AI systems**—which the accompanying draft guidance says expressly is “not dealing with” general-purpose models—asks in section 1.2 for the date of report submission, the date of the incident, the date and time of detection, and the “Manufacturer awareness date of reportability”, and runs to seven pages against two (Appendix F). So the recommendation is a harmonisation, not a proposal. Three qualifications. The high-risk field asks for awareness of *reportability*, tracking Article 73(2), where Measure 9.3 runs from awareness of the model’s involvement. Both high-risk documents are consultation drafts of 26 September 2025, with no final version linked as of 12 September 2026. And the regime they serve is not yet in application: Article 73 has applied only since 2 August 2026, Article 75(1a) since 27 July 2026, and the Omnibus deferred the high-risk classification both depend on to 2 December 2027 and 2 August 2028. The comparison is between two drafting choices, not two live regimes.

**What selects the instrument is not severity.** Article 75(1), point (a) makes the AI Office exclusively competent for AI systems “based on general-purpose AI models where the model and the system are developed by the same provider, or by providers forming part of the same undertaking”, and Article 75(1a) routes those systems’ serious incidents to the same AI Office that Article 55(1), point (c) reaches. One body, one undertaking, two regimes differing in clock, trigger, form and guidance; they meet only where the system is **high-risk**, and a non-high-risk own-system carrying a systemic-risk model is reported under the lighter regime alone. As a claim about the Act’s structure this needs nothing from §4.1. As a claim about this incident it needs both the scope finding and `inf-scaffolding-attribution`, and the report keeps the two uses apart.

**Three recommendations follow.**

1. **Put the Recital 97 test in the enacting text.** Article 3, point (63) should carry the “sole purpose” qualifier and the systemic-risk carve-out Recital 97 supplies, and Article 2(1), point (a) should say whether an own model put into service for own use in the Union is placed on the market.
2. **Give Article 55(1)(c) a determinate period.** Article 52(1) shows the same chapter setting one on a forward-looking trigger.
3. **Bring the two reporting instruments into line.** At minimum the general-purpose template should carry the date of awareness and the date of submission, which the high-risk draft already has. The change is to the form rather than the Code; nothing in Article 55(2) stops a form asking for more than the Code lists.

### 4.7 Cross-jurisdictional check

California’s SB 53 §22757.11(c)(1)(B)–(C) describes this conduct closely—“conduct with no meaningful human oversight… that is either a cyberattack” and “Evading the control of its frontier developer or user”—and its magnitude floor of 50 deaths or $1bn excludes it (California, 2025); its clock runs from discovery and its form records only the date of the incident. Those provisions were read in a published reproduction and are not verified against the enacted text, and the register says so. The New York RAISE Act is described in the comparative appendix, registered nowhere, and not relied on here. Full table at Appendix B.

## 5. The instrument

The model request is at `instrument/`. It is drafted under Article 91(1), which has applied since 2 August 2026, and conforms to Article 91(4)’s required form. It is issued in the name of **the Commission**: Article 3, point (47) makes the AI Office “the Commission’s function” rather than a legal person, and only Article 91(2) structured dialogue is expressed as the Office’s.

Section I asks the scope and status questions first—model identity, training compute with the estimation approach, whether the model was integrated into an own system put into service and where, whether it shares a large pre-training run with any model placed on the market or was intended for placement, and whether notification was made. Each request states what would not be a responsive answer.

The request states expressly that no view has been formed that any obligation has been contravened. Article 101 has applied only since 2 August 2026; whether an omission that began before that date and continued past it carries exposure under Article 101(1), point (a) is a question this report does not answer, and the instrument indicates Article 101(1), point (b), covering failure to respond, as Article 91(4) requires. It carries a provenance header and explicit placeholders rather than plausible reference numbers. It has not been issued.

## 6. Discussion and limitations

The method’s ceiling is real. Nothing here establishes that any obligation was contravened, and several rows would resolve only against documents no member of the public can see.

The author is not a lawyer. This analysis has been materially wrong **twenty-four times**, and the log ships with it (`protocol/01-statutory-foundation.md`). Nineteen of the twenty-four are one failure wearing different clothes: a source characterised without being opened. The most recent five came from an external audit on the final day, and the largest was a scope verdict that stated one open condition where the route needs three, resting on a premise—a model built to ship—that the provider’s account, quoted at §1, denies. A clean board means the mechanical failures are absent and nothing more. The record is live, and every negative-search note is dated accordingly; notes on sourcing, the register and bounded absences are at Appendix G.

**What would change the result.** The scope conclusion turns on `inf-attach`, `inf-relocation` and `inf-placement-event`; the timing conclusion on `inf-opinion-construes`. `python3 tools/infercheck.py --attack` prints the load-bearing steps weakest first, and that list rather than this report is what an adversarial reader should be handed.

A month of follow-up would add: whether the affected platform provides an essential service within a CER Annex sector; the Article 3(1)/3(63) bridging question; a source entry for the New York RAISE Act; and the revision history of the July disclosure.

## 7. Conclusion

On the Commission’s reading the obligations attach, because Recital 97 deems a model integrated into its provider’s own system put into service to be placed on the market, and because the internal-use exception is unavailable to a model carrying systemic risk. Neither proposition is in the enacting definition, and the body that supplied them disclaims authority to interpret the Act. What that leaves is three facts. If the model exceeds 10²⁵ FLOP, if it was placed—by integration into an own system put into service, or by sharing a pre-training run with a model that was—and if that placement was in the Union, then a two-week notification duty was engaged during development and Articles 53 and 55 applied throughout. The provider’s own account denies the second, and nobody outside the provider knows the first. Article 91 is the instrument for asking, it has not been used publicly on either episode, and a draft of it is attached.

One conclusion needs none of that. The Commission’s template for reporting these incidents does not ask when the provider became aware, every initial-report period the Code sets runs from awareness, and the reason is that the template transcribes a list which never had the field. Two dates repair it, and the Commission has already drafted both, in a consultation template for high-risk systems. The lighter form was drafted for the graver models, and that is the finding a legislator can act on without agreeing with a word of the scope analysis above.

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

It cannot resolve the facts on which everything turns. The model’s training compute is known only to the provider; whether the model was ever integrated into an own system put into service, or shares a pre-training run with a model that was placed, is known only to the provider; and no account places any such system in the Union. If any of the three fails, most of this analysis falls away, and the report says so rather than hedging.

It cannot settle the scope argument. A provider could run the textual reading, and the Commission’s Q&A disclaims authority to interpret the Act.

### A.2 Access asymmetry

The parties able to resolve most rows are the ones whose conduct is in question. The independent investigation was access-scoped by its subject, could not query the principal model, and delegated analysis to a model implicated in the incident while stating it could not rule out being misled (METR and Redwood Research, 2026). Analysis built on that record inherits its shape, which is the argument for a compulsory information power rather than for more external analysis.

### A.3 Dual use: aggregation rather than disclosure

The exploit chain is already public (Hugging Face, 2026). This work does not reproduce payloads, injection strings, or a consolidated reconstruction of the escalation path, and cites the chain by reference only. The same facts scattered across a vendor post and an incident timeline are a different artifact from those facts assembled and annotated in one place; assembly adds the operational value, and regulatory analysis needs the category of vulnerability rather than the working detail.

### A.4 Dual use: the instrument

A well-formed regulatory instrument can be misused, to lend false authority or to harass through procedurally correct but empty demands. Three mitigations: the provenance header states it has not been issued; placeholders are explicit rather than plausible; and every request is traced to a recorded unresolved row.

### A.5 Dual use: the scope analysis

§4.1 sets out the strongest textual argument available to a provider seeking to place a pre-market research model outside the Regulation. It is published anyway. The argument is derivable by anyone who reads Articles 2(1)(a), 3(9) to (11) and 3(63) together, and it is already in the literature (Pistillo, 2026), so publication confers no advantage a competent adviser does not hold. A fragility that regulators can see is less dangerous than one they cannot, and the drafting recommendation at §4.6 is narrow and available.

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

**On the negative-search notes.** Each carries an as-of date, and each now records the corpus searched—which sources, which terms, on what date—because “no published source states X” is a claim about everything ever published and nobody can make it. One of the six turned out not to be an absence at all: the Commission’s spokesperson was asked, on the record, and declined to say when the report was submitted or what it contained. That is a refusal, and a refusal is evidence. Whether the episode qualifies as a serious incident and which provision the filing relied on remain absences—the press report says only that the Commission “has not said”—and an earlier draft of this appendix had upgraded them to refusals, which is the distinction this note exists to keep. The other four remain bounded absences and say what they are bounded by.

**On the statutory register.** All forty-six provisions of the Regulation, seven imported provisions of the CER Directive and four recitals behind this report have been verified against the EUR-Lex consolidated text at CELEX `02024R1689-20260727`. Amendment status is taken from the amending act’s own numbered instructions rather than from the consolidated text’s change markers: reading the markers alone had wrongly cleared Article 60, which instruction (24) of Regulation (EU) 2026/1744 replaces in part. Fourteen of them spent a day sourced from a published reproduction, while EUR-Lex was unreachable, and were marked as such rather than presented as equivalent; on rechecking, thirteen matched verbatim and the fourteenth differed by one stray full stop which proved to be the Regulation’s own. Of the fourteen, only Article 57(1) was touched by the Digital Omnibus.

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

**And the form does not ask the one date its own clock runs from**, which is §4.6 and is the finding this exercise was not looking for.
