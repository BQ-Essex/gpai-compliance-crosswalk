# Statutory Foundation: verified against primary source

**Provenance**: extracted from the EUR-Lex consolidated text of Regulation (EU) 2024/1689, CELEX `02024R1689-20260727`, consolidation date **27 July 2026** (incorporating Regulation (EU) 2026/1744, the Digital Omnibus on AI). Recitals are absent from the consolidated version and come from the authentic Official Journal text, CELEX `32024R1689`. Extracted 11 September 2026; scope provisions re-extracted and corrected the same day following adversarial review.

`amended_by_omnibus` is read from the EUR-Lex change markers (`▼M1` amended, `▼B` base), not inferred from commentary.

> Citation convention: the Act’s own—“Article 55(1), point (c)”; “Article 3, point (49)(b)”.

---

## 0. Corrections log

Nineteen errors have been found in this analysis. Four came from adversarial review of the finished draft; the fifth from a checker written afterwards; the sixth from reading a cross-referenced directive instead of a summary of it; the seventh from a pre-print’s version history rather than its title page; the eighth from reading the amending act rather than inferring from its footprints; the ninth from reading a document rather than its landing page; the tenth from reading Article 52 rather than assuming its shape; the eleventh from counting this table instead of quoting a sentence about it; the twelfth from searching a document this project had held since the first day; the
thirteenth from checking quotations in the register, which had never been checked; and the fourteenth from taking a reviewer’s word for what a provision says; and the fifteenth from describing that reviewer as a lawyer; and the sixteenth from marking its citations unverified instead of verifying them; and the seventeenth from a comparative appendix that cited two foreign statutes and registered neither; and the eighteenth from holding the incident record as files for the first time; and the nineteenth from an appendix contradicting this project’s own register. **Fourteen of the nineteen are the same failure: characterising a source without opening it**—and the twelfth is its close cousin, opening a source for one question and never asking it a second. The tenth, part of the eleventh, and the whole of the thirteenth and fourteenth are the ones the tooling caught before any human read the sentence. All are recorded rather than silently fixed.

| Error | Correction |
|---|---|
| Article 73(4) recorded as “immediately” for incidents involving death | **“not later than 10 days”**. Tiering is 15 days / two days / 10 days, with “immediately” as the floor in each, not the limit |
| “Critical infrastructure” said to turn on Member State designation | Designation attaches to **‘critical entity’** (CER Art. 2(1)). The Act imports CER Art. 2(**4**), which is **functional** |
| **Scope treated as settled; Articles 2(8), 3(3) and 3(63) never consulted** | See §1. The research/development exclusion sits inside the definition of ‘general-purpose AI model’ itself |
| **Scope then treated as resolved in the provider’s favour; Recital 97, Article 2(1)(a), Article 3 points (9)–(11) and the Commission’s Q&A never consulted** | See §1.5–1.7. Recital 97 deems a model integrated into the provider’s own system put into service to be placed on the market, and its internal-use exception is expressly unavailable to models with systemic risk. **The obligations attach.** The live question is factual: does the model exceed 10²⁵ FLOP? |
| **A verdict cell carried a conclusion of law while keeping a permitted opener** | The threshold row read “On the provider’s own account, this appears met: the obligations attach”. The three registers make claims about a *disclosed record*; whether Chapter V reaches these facts is not something a record can establish. The record verdict and the conclusion of law are now separate fields, and `tools/validate.py` refuses the formulation. Found by a checker, not by review. |
| **CER Article 5 said to require Member States to identify essential services within the Annex sectors** | It requires no such thing. CER Article 5(1) empowers **the Commission** to establish a **non-exhaustive** list of essential services by delegated act; Member States use it for risk assessments and then identify **critical entities** under CER Article 6. The Annex’s third column lists **categories of entities**, not services. Third error on this same limb, and the second of the designation/function kind. Found by reading the Directive rather than a summary of it. |
| **A cited pre-print declared mis-identified, on a reading of its own title block** | The register dated Pistillo December 2025 while holding a document whose title block read “Submitted: May 2026”, then concluded from that mismatch that the arXiv identifier could not belong to it. The identifier was always right. The work has **four versions**—5 December 2025, 26 January 2026, 20 May 2026, 10 August 2026—and the copy held is v4, identified by byte size. A submission date is not a posting date. Both the original error and the correction of it were published before this was caught. |
| **Amendment status derived from change markers alone, and one flag wrong because of it** | Article 60 was recorded as unamended. Regulation (EU) 2026/1744, instruction (24), replaces Article 60(1)’s first subparagraph and the whole of Article 60(2). The method was at fault, not just the flag: status had been read from the nearest preceding change marker in the consolidated text, and the phrase used to locate Article 60 is also its own heading, so the search matched the heading. Status is now taken from the amending act’s own list of instructions. The same pass found that Article 56 had been deleted from the register as uncited, when Article 56(6) is the one Chapter V provision the Omnibus amended; it is reinstated. |
| **A document’s contents characterised from its landing page** | The register stated that the Commission’s 1 August 2025 opinion on the Code was “expressed in general terms rather than by reference to particular provisions”, and carried a negative-search note to match. The opinion is C(2025) 5361 final and names Articles 53 and 55 throughout, concluding in terms that the Code “adequately covers the obligations provided for in Articles 53 and 55”. The note flagged that the document had not been read, and the inference was drawn anyway. Retracted, and the document is now in the register. |
| **The Article 52(2) rebuttal said to answer a Commission designation** | A draft stated that where the Commission designates a model under Article 51(1), point (b), “Article 52(2) then places the burden on the provider”. Article 52(2) is available to a provider whose model meets point (a) and is presented “with its notification”: it answers the compute presumption, not a designation. `citecheck.py` flagged Articles 52(2) and 52(3) as cited but absent from the register; adding them meant reading them, and reading them corrected the claim. |
| **A count of this log, quoted in five other files, drifted from it—and one of the quotations had never been right** | The log grew from six entries to ten while README, the report’s §3.2 and three tool docstrings went on saying “nine errors”, “six of the nine” and “three of the six”. The last was not merely stale: **two** recorded errors came from reading a summary of the CER Directive, never three, so a claim about this table had been made without counting it. `housestyle.py` now treats the table’s own row count as canonical and sweeps prose **and tool docstrings** for any sentence that disagrees; on its first run it also caught README claiming twelve argumentative steps against a register of seventeen. The same sweep found the report citing an **Appendix F** it never bound in, the forms appendix having been written as its own file; that is now checked too, a cross-reference being a claim that something exists |
| **A document held from the first day, searched for one question and never for another** | The Commission’s GPAI Guidelines, C(2025) 7719 final, were read for the scope question and never searched for ‘serious incident’. Paragraph (100) answers it, and answers it in the **enforcement** section rather than anywhere definitional: the AI Office reads Article 55(1), point (c) as covering “serious cybersecurity breaches related to the model or its physical infrastructure, including the (self-)exfiltration of model parameters and cyberattacks”, anchored in Article 55(1), points (b) and (d); and otherwise treats a serious incident as any incident or malfunctioning of a model that “directly or indirectly leads to” an Article 3(49), points (a) to (d) event. Two consequences: the five-day cybersecurity route no longer depends on reading Commission Opinion ¶33 as construing the Act, and the bridging gap is bridged—**in guidance**, which is the Recital 97 pattern again |
| **Quotations in the source register had never been checked, and two of them were paraphrases** | `quotecheck.py` read Markdown a line at a time, which is right for prose and wrong for YAML, where a quotation is wrapped across a block scalar so its two ends never share a line. The register’s quotations were therefore invisible to it for as long as it had existed. Found by planting a wrong word in a quotation and watching nothing happen. With coverage extended, the first two defects it reported were paraphrases written minutes earlier inside quotation marks—“establishment of a causal link” for the Act’s “has established a causal link”, and “Article 55(1)(c)” for the guidance’s “Article 55 (1)(c)”—and a third entry that had capitalised its own emphasis inside the quotation marks. Checked quotations went from 103 to 139 |
| **A reviewer’s assertion about an enacted provision, acted on without checking it** | An adversarial review of the instrument said paragraph 12 misquoted Article 101(1), point (b), which the draft rendered “a request for a document or for information”, and that the enacted text read “documents or information”. It does not; the draft was right. The correction was applied anyway, because the review had been right about eighteen other things. `quotecheck.py` rejected it on the next run, roughly two minutes later. **A review is evidence and not authority**, which is the same lesson as entries two, six and nine in the other direction: the text is the text, and the only way to know what it says is to open it |
| **A language model prompted into a role, described as a lawyer** | The adversarial review at `docs/instrument-review.md` was produced by a language model told to read the draft as a senior lawyer in the AI Office. **No lawyer was consulted and nobody real was contacted.** The file did not say so, and the commit that added it was titled “Have a lawyer read the instrument, and publish what they said”, which asserts a consultation that never happened. **Caught by the author, not by the tooling**, and it is entries two, six and nine wearing the costume of a job title: a source described as something it is not. The file now states its provenance in its first paragraph and marks its case-law citations as unverified, none having been read. The commit message stays in the history as part of the record |
| **Five case-law citations marked unverified when verification was one request away** | Having corrected the reviewer’s job title, this register marked its citations to *Orkem*, *AM & S*, *Akzo Nobel*, *Nilsson* and *Deutsches Milch-Kontor* as unverified, on the reasoning that confabulated case law is a known failure of the tool that produced them. That reasoning is sound and it was **standing in for a check**. EUR-Lex serves all five. Read on 13 September 2026, **every one is accurate** as to name, number, date, court and proposition. This is the same failure as the day the GitHub API returned 403 and a summariser was accepted in place of `git ls-remote`: a precaution is not a finding, and “unverified” is a statement about the register’s effort, not about the source. Reading them also produced two things the flag never would: **Akzo Nobel contradicts the review’s own use of it** on in-house privilege, which changes the instrument in the Commission’s favour; and **Deutsches Milch-Kontor ¶32 is the strongest verified authority against this report’s own scope finding**. All five now sit in `data/provisions.yaml` under `case_law`, with the paragraph quoted, and `quotecheck.py` checks quotations against them |
| **A comparative appendix citing two foreign statutes with no source entry for either** | `docs/comparative-regimes.md` and §4.8 of the report cited nine provisions of California SB 53 and described the New York RAISE Act. `data/sources.yaml` held **no entry for either**. Not an unverified entry—none at all, in a method whose third step is to tier every source by its relationship to the claim, and `citecheck.py` was skipping them silently, so a clean board read the same whether a citation had been checked or deliberately excluded. Reading the California text found a **substantive error**: `docs/appendix-forms.md` said the definition of a critical safety incident “expressly includes unauthorised access to or exfiltration of model weights”, where §22757.11(d)(1) qualifies that limb with “that results in death or bodily injury”—so on these facts it is not engaged. `comparative-regimes.md` had carried the qualifier correctly all along; the appendix had taken the point from memory of that file rather than from the text. Two quotation defects with it: “Evading the control of its frontier developer” had lost “or user”, and “outside evaluation contexts” was a paraphrase in quotation marks. California is now registered as reproduction-sourced and marked unverified against the enacted text; **New York remains unregistered and the appendix says so**; citecheck reports the exemption on every run |
| **A characterisation carried inside quotation marks, and attributed to a source that does not say it** | The worked example stated that the deployed model’s cyber classifiers were “intentionally disabled for the cyber evaluations”, marked **[T3]**. On 13 September 2026 the six incident-record documents were held as files for the first time and `quotecheck.py` could not find the phrase in any of them. No held source says “disabled”: the provider says it estimates maximal capability “by running this evaluation without production classifiers”, and the second provider says its models “did not have the classifiers and monitoring we usually implement”. **“Disabled” is a stronger word than “run without”**, and it is the facts and characterisation line this project polices everywhere else, crossed inside quotation marks and dressed in a tier marker. Found with it: “across” spliced inside a quotation of the victim’s rotation statement. Until this day every statutory quotation was verified against primary text and every quotation of what the parties actually said was verified against nothing—the evidentiary core was the least checked material in the project |
| **An appendix saying no report had been filed, while the register recorded the Commission confirming receipt of one** | `docs/appendix-forms.md` marked field 10 of the serious-incident template *cannot fill* on the ground that “no filing is public, so no submitter is”, and the report’s Appendix F repeated it. `data/sources.yaml` and `data/crosswalk.yaml` had recorded since 12 September that the Commission’s spokesperson confirmed receipt of the provider’s report on the wiki episode while declining to give the date or contents. The appendix was written from memory of the situation rather than from the register—the same failure as the California qualifier, and the source characterised without being opened was again this repository’s own. **The correction strengthens the finding**: a report exists, the regulator has it, the regulator will not give the date, and the form has no field for the date of awareness or of submission. The instrumentation gap is not a hypothetical about an unused form; it describes the only filing anyone knows about |

---

## 1. Scope: the threshold question, and the one the analysis must answer first

### 1.1 Article 3, point (63): the exclusion is inside the defined term

> ‘general-purpose AI model’ means an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks regardless of the way the model is placed on the market and that can be integrated into a variety of downstream systems or applications, **except AI models that are used for research, development or prototyping activities before they are placed on the market**;

On the face of it, a model used for research, development or prototyping before market placement is **not a ‘general-purpose AI model’ within the meaning of the Regulation**—not exempted from particular obligations, but outside the term on which Chapter V operates. Note what the enacting text does **not** say: there is no “sole purpose” qualifier, and no condition about internal processes or systemic risk. Recital 97 and the Commission’s guidance supply all three. See §1.6.

And the omission reads as deliberate rather than careless, because the formula was to hand. **Article 2(6)** excludes AI systems and models “specifically developed and put into service **for the sole purpose of** scientific research and development”. The drafters used the qualifier where they wanted it, two paragraphs from the scope provision that governs this analysis, and did not use it in Article 3, point (63). A reader who supplies it from Recital 97 is supplying a term the enacting text declined.

### 1.2 Article 2(8): the operative scope exclusion, and its one way back in

> This Regulation does not apply to any research, testing or development activity regarding AI systems or AI models **prior to their being placed on the market or put into service**. Such activities shall be conducted in accordance with applicable Union law. **Testing in real world conditions shall not be covered by that exclusion.**

The final sentence is the only route back into the Regulation for anything occurring at the development stage. It is a defined term.

### 1.3 Article 3, point (57): and why the route back does not open

> ‘testing in real-world conditions’ means the **temporary** testing of an **AI system** **for its intended purpose** in real-world conditions **outside a laboratory or otherwise simulated environment**, with a view to gathering reliable and robust data and to assessing and verifying the conformity of the AI system with the requirements of this Regulation, and it does not qualify as placing the AI system on the market or putting it into service within the meaning of this Regulation, provided that all the conditions laid down in Article 57 or 60 are fulfilled;

Every element describes a **deliberate, conditioned, elected** activity: temporary, for the system’s intended purpose, conducted outside a laboratory by design, subject to the conditions in Articles 57 or 60.

**A model that reaches the real world by escaping a simulated environment satisfies none of it.** The escape was not temporary testing, not for an intended purpose, and not a modality anyone elected. The exception is drafted for exposure that is *chosen*; it does not reach exposure that *occurs*.

**And there is a further step, which the definition makes and the commentary generally does not.** The defined term is the temporary testing of an **AI system**, and the conditions it defers to are those of Article 57 or Article 60. Article 57 establishes national regulatory sandboxes that Member States operate and providers enter. Article 60 is titled “Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes”, and its first paragraph confines it to “providers or prospective providers of **high-risk AI systems** listed in Annex III or covered by Union harmonisation legislation listed in Section A of Annex I”. Neither reaches a general-purpose AI model.

So Article 2(8)’s single carve-back has no purchase on a model at all. On the enacting text, pre-market development of a general-purpose AI model sits outside the Regulation with no relevant exception—a stronger version of the textual reading than the one this analysis first ran, and one that has to be answered rather than dismissed.

**It is answered, and the answer says something about how the Regulation is built.** Recital 97 does not carve an exception out of Article 2(8). It relocates the moment of placement: a model integrated into its provider’s own system put into service *is* placed on the market, so the development was not activity “prior to [its] being placed on the market”, and Article 2(8) never engages. The recital is not overriding the enacting text; it is fixing the point in time from which the enacting text runs. That is a structural job, and the observation worth making is that the Act leaves it to a recital to do.

### 1.3a Recital 25: the research exclusion has two halves, and only one is an exclusion

> **Recital 25 (extracts)**: … It is therefore necessary to exclude from its scope AI systems and models specifically developed and put into service **for the sole purpose of scientific research and development**. … As regards **product-oriented** research, testing and development activity regarding AI systems **or models**, the provisions of this Regulation should also not apply **prior to those systems and models being put into service or placed on the market**. That exclusion is **without prejudice to the obligation to comply with this Regulation where an AI system falling into the scope of this Regulation is placed on the market or put into service as a result of such research and development activity** …

Scientific research and development is excluded outright, on a **sole purpose** test, by Article 2(6) and this recital together. Product-oriented research is not excluded at all: the Regulation simply does not reach it *before* placement or putting into service. A frontier developer’s pre-release evaluation of a model it intends to ship is product-oriented on any reading, so this half of the recital postpones rather than exempts.

**Then note the drafting.** The recital speaks of “those systems **and models** being **put into service** or placed on the market”. Article 2(1)(a) gives models no put-into-service limb, and Article 3, point (11) defines the term by reference to an **AI system** alone. Recital 97 does the same when it deems an integrated own model placed on the market. Two recitals presuppose a category the enacting definitions withhold. That is the strongest evidence available that the asymmetry at §1.5 is an artefact rather than a choice—and it still does not cure it, because the principle that a recital cannot derogate from enacting terms is not weakened by there being two of them.

Note also the closing “without prejudice” clause, which names only “an **AI system** falling into the scope of this Regulation”. Even here, where the recital is at its most expansive, the asymmetry survives.

### 1.4 Article 3, point (3): ‘provider’ is tied to market placement

> ‘provider’ means a natural or legal person, public authority, agency or other body that develops an AI system or a general-purpose AI model or that has [one] developed **and places it on the market** or puts the AI system into service under its own name or trademark, whether for payment or free of charge;

Article 52(1) binds “the relevant **provider**”. The *temporal trigger* in Article 52(1) is capability (“or it becomes known that it will be met”); **standing** is not. A developer may not be a provider of a model it never places on the market.

### 1.5 The asymmetry in Article 2(1), point (a), and why it is not the end of the matter

> **Article 2(1)(a)**: This Regulation applies to: providers **placing on the market or putting into service AI systems** or **placing on the market general-purpose AI models** in the Union …

The two halves differ, and the difference is in the enacting text. AI *systems* are caught by placing on the market **or putting into service**—and ‘putting into service’ at Article 3, point (11) expressly includes supply “**for own use** in the Union for its intended purpose”. General-purpose AI *models* are caught **only** on placing on the market, which Article 3, point (9) defines as first making available, and Article 3, point (10) ties to supply “in the course of a **commercial activity**”.

Read alone, that asymmetry plus Article 3(63) would put an internal, unreleased research model outside Chapter V. **It does not survive Recital 97 or the Commission’s own guidance.**

### 1.6 Recital 97 and the deemed-placement rule, which decides it

> **Recital 97 (extracts)**: … It should be understood that the obligations for the providers of general-purpose AI models should apply **once the general-purpose AI models are placed on the market**. **When the provider of a general-purpose AI model integrates an own model into its own AI system that is made available on the market or put into service, that model should be considered to be placed on the market** and, therefore, the obligations in this Regulation for models should continue to apply in addition to those for AI systems. The obligations laid down for models **should in any case not apply when an own model is used for purely internal processes that are not essential for providing a product or a service to third parties and the rights of natural persons are not affected**. Considering their potential significantly negative effects, **the general-purpose AI models with systemic risk should always be subject to the relevant obligations** under this Regulation. The definition should not cover AI models used before their placing on the market **for the sole purpose of** research, development and prototyping activities …

The Commission’s own Q&A on general-purpose AI models consolidates this into an operative test:

> “a general-purpose AI model is **also considered to be placed on the market** if that model’s provider **integrates the model into its own AI system which is made available on the market or put into service**, unless the model is (a) used for purely internal processes that are not essential for providing a product or a service to third parties, (b) the rights of natural persons are not affected, and (c) **the model is not a general-purpose AI model with systemic risk**.”

The three conditions are cumulative, and condition (c) is decisive: **the internal-use exception is unavailable to a model with systemic risk.**

The same Q&A states that obligations “explicitly or implicitly pertain to the **development phase**”, naming the duty to “notify the Commission that their general-purpose AI model **meets or will meet** the training compute threshold” (Articles 51–52), to “document information about training and testing” (Article 53), and to “assess and mitigate systemic risk” (Article 55).

### 1.7 The Commission’s Guidelines, at paragraph level

*Commission Guidelines on the scope of the obligations for providers of general-purpose AI models established by Regulation (EU) 2024/1689*, C(2025) 7719 final, Brussels, 19 November 2025. Obtained as the published English text; paragraph numbers are the Guidelines’ own.

**Status, paragraph 9**—the sentence that governs how everything else here should be read:

> “These guidelines are not binding for providers of general-purpose AI models; an authoritative interpretation of the AI Act may only be given by the Court of Justice of the European Union (‘CJEU’). Nevertheless, these guidelines set out the Commission’s interpretation and application of the AI Act, **on which it will base its enforcement action**.”

Not binding, and enforcement-determining. Both halves are operative.

**Internal use as placing on the market, paragraph 51.** Among the Guidelines’ worked examples of a model being placed on the market:

> “a general-purpose AI model is used for **internal processes that are essential for providing a product or service to third parties or that affect the rights of natural persons in the Union**.”

Note the polarity. Recital 97 states the carve-back negatively (obligations do not apply to purely internal processes *not* essential to third-party provision where rights are *not* affected); the Guidelines state the same boundary positively, as an example of placement. Paragraph 52 adds that the examples “require case-by-case assessment” and are to be read with the Blue Guide and Articles 3(9) and (10) and Recital 97.

**Deemed placement, Section 3.1.3, paragraph 54**, quoting Recital 97 as its authority:

> “First, as specified in recital 97 AI Act, ‘[w]hen the provider of a general-purpose AI model integrates an own model into its own AI system that is made available on the market or put into service, that model should be considered to be placed on the market and, therefore, the obligations in this Regulation for models should continue to apply in addition to those for AI systems.‘”

**Lifecycle, paragraph 22—the most consequential paragraph for this analysis, and the least obvious:**

> “the Commission considers the lifecycle of a general-purpose AI model to **begin at the start of the large pre-training run**. Any subsequent development of the model downstream of this large pre-training run performed by the provider or on behalf of the provider, **whether before or after the model has been placed on the market, forms part of the same model’s lifecycle** rather than giving rise to new models … A model is thus considered to be **the same model along its entire lifecycle**, i.e. throughout its development, market availability, and use. In particular, **different stages of the development of a model are not considered to constitute different models**.”

Read with the closing sentence of Recital 97—the research exclusion “is without prejudice to the obligation to comply with this Regulation when, following such activities, a model is placed on the market”—this narrows the Article 3(63) exemption considerably. A model in development is not a different model from the one later released. **The exemption protects a model that is never placed on the market; it does not protect the development phase of a model that is.**

**Enforcement timing, paragraph 112**, corroborating the Article 113 derivation at §8 from the Commission’s own account: “In the first year from 2 August 2025 onwards, the Commission cannot take any enforcement actions because its enforcement powers only enter int[o application on 2 August 2026]”.

**What the Guidelines do not do.** They quote the Article 3(63) research exclusion when reproducing the definition (paragraph 13) and nowhere condition it, gloss it, or add the “sole purpose” qualifier. That qualifier appears only in Recital 97. The phrase “sole purpose of research” does not occur in the Guidelines at all.

### 1.8 Where that leaves scope, stated precisely

**The obligations attach**, on the Commission’s reading, provided the model is one with systemic risk. The route runs: model integrated into the provider’s own AI system put into service → deemed placed on the market (Recital 97) → internal-use exception unavailable because the model carries systemic risk → Chapter V applies, including the development-phase duties the Q&A names.

**The live question is therefore factual, not legal**: does the model exceed the 10²⁵ FLOP threshold at Article 51(2)? If it does, Article 52(1)’s two-week notification duty was engaged during development, and Articles 53 and 55 apply.

**Three qualifications belong in any honest statement of this.**

1. **The route runs through a recital and non-binding guidance, not the enacting definition.** Article 3(63) excludes research models with no “sole purpose” qualifier and none of the three conditions; Recital 97 supplies both. The principle that a recital cannot derogate from enacting terms (*Nilsson* C‑162/97; *Manfredi* C‑308/97; *Tyson Parketthandel* C‑134/08) cuts against relying on a recital to create coverage the definition withholds, just as it cut against the earlier draft’s attempt to rely on Recital 115.
2. **The Q&A disclaims its own authority**: “This Q&A does not constitute an official position of the Commission … Only the Court of Justice of the European Union is competent to authoritatively interpret the AI Act.”
3. **A provider could run the textual argument.** It is the strongest position available to it, and the analysis should say so rather than pretend the question is closed.

### 1.8a The independent hook, which needs none of the above

**Article 55(1), point (b)** obliges providers of general-purpose AI models with systemic risk to assess and mitigate systemic risks at Union level, including their sources, “that may stem from **the development**, the placing on the market, or the use” of such models. **“Development” is in the enacting text, not a recital.**

This matters because it holds whichever way the scope argument goes. Even on the provider-favourable reading—research model outside the definition—the *deployed* model is indisputably within it, and its provider owed a duty to assess systemic risk stemming from development. A containment failure during internal evaluation is squarely a **risk source** that duty reaches.

### 1.9 A bridging problem to state rather than paper over

‘Serious incident’ at Article 3, point (49) is defined by reference to an **AI system** (Article 3(1)). Article 55(1)(c) binds providers of **models**. Article 3, point (66) defines ‘general-purpose AI system’ separately as a system based on such a model. The Act does not expressly bridge the two for the purposes of Article 55(1)(c), and the analysis should record this as unresolved rather than assume it away.

---

## 2. Article 3, point (49): ‘serious incident’ (unamended)

> ‘serious incident’ means an incident or malfunctioning of an AI system that directly or indirectly leads to any of the following:
> (a) the death of a person, or serious harm to a person’s health;
> (b) a serious and irreversible disruption of the management or operation of critical infrastructure;
> (c) the infringement of obligations under Union law intended to protect fundamental rights;
> (d) serious harm to property or the environment;

- Causal standard is broad: “directly **or indirectly**”.
- Limbs are disjunctive.
- **Only limb (b) carries an irreversibility requirement.** Limb (d) does not.
- Limb (b) is not self-contained—see §2.1.

### 2.1 Article 3, point (62) → Directive (EU) 2022/2557

> **AI Act, Art. 3(62)**: ‘critical infrastructure’ means critical infrastructure as defined in Article 2, point (4), of Directive (EU) 2022/2557;
>
> **CER Art. 2(4)**: an asset, a facility, equipment, a network or a system, or a part [thereof], **which is necessary for the provision of an essential service**;
> **CER Art. 2(5)**: ‘essential service’ means a service which is crucial for the maintenance of vital societal functions, **economic activities**, public health and safety, or the environment;
> **CER Art. 2(1)** *(different term, for contrast)*: ‘critical entity’ means an entity **identified by a Member State in accordance with [CER] Article 6** …

The imported term is **functional**; designation attaches to ‘critical entity’. But the functional test is not at large either, and the way it is bounded is not what an earlier draft of this section said.

**CER Article 5(1), as enacted**: “The Commission is empowered to adopt a delegated act, in accordance with [CER] Article 23, by 17 November 2023 to supplement this Directive by establishing a **non-exhaustive list of essential services** in the sectors and subsectors set out in the Annex. The competent authorities shall use that list of essential services for the purpose of carrying out a risk assessment … by 17 January 2026 … The competent authorities shall use Member State risk assessments for the purpose of **identifying critical entities in accordance with [CER] Article 6**”.

Three things follow, and each cuts against the earlier phrasing. It is **the Commission**, not the Member States, that establishes the list. The list is **non-exhaustive**, so a service absent from it is not thereby outside CER Article 2, point (5). And what Member States identify under CER Article 6 is **critical entities**, not essential services—which is the same designation/function distinction this analysis has already corrected once, resurfacing one layer down.

The **CER Annex** compounds it. Its third column is headed **“Categories of entities”**, not services. For sector 8, digital infrastructure, those categories are providers of internet exchange points; DNS service providers, excluding operators of root name servers; top-level-domain name registries; providers of cloud computing services; providers of data centre services; providers of content delivery networks; trust service providers; and providers of public electronic communications networks. That tells you which entities a Member State may designate in this sector. It does not tell you what counts as an essential service, and it is not a list this analysis can read as though it did. **And Article 3(49)(b) requires disruption of “the management or operation of” that infrastructure**, which is a further step. Limb (b) is arguable, not comfortable, and fails independently on “irreversible” where the affected systems were rebuilt.

---

## 3. Articles 51, 52 and 53

> **Art. 51(1)**: … classified as a GPAI model with systemic risk if … (a) it has high impact capabilities …; (b) based on a decision of the Commission, ex officio or **following a qualified alert from the scientific panel** …
> **Art. 51(2)**: … **presumed** to have high impact capabilities … when the cumulative amount of computation used for its training … is **greater than 10²⁵** [FLOP].
> **Art. 52(1)**: Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission **without delay and in any event within two weeks** after that requirement is met or **it becomes known that it will be met**. … If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, **it may decide to designate it** as a model with systemic risk.
> **Art. 53(1)(a)**: … draw up and keep up-to-date the technical documentation of the model, **including its training and testing process and the results of its evaluation** … for the purpose of providing it, **upon request, to the AI Office** …

Article 52(1) is the only determinate period in the chapter (**two weeks**), and it is forward-looking. **But it binds a ‘provider’ (Art. 3(3)) in respect of a ‘general-purpose AI model’ (Art. 3(63))**—and §1 is why neither term can be assumed for a model used in pre-market research.

The qualified-alert pathway referenced at Article 51(1)(b) is governed by **Article 90**.

---

## 4. Article 55 and Recitals 114–115 (unamended)

> **55(1)(a)** perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and **documenting** adversarial testing of the model …;
> **55(1)(b)** assess and mitigate possible systemic risks at Union level, **including their sources**, that may stem from **the development**, the placing on the market, or the use …;
> **55(1)(c)** **keep track of, document, and report**, without undue delay, to the AI Office …, relevant information about serious incidents **and possible corrective measures to address them**;
> **55(1)(d)** ensure an adequate level of cybersecurity protection for the … model … and the physical infrastructure of the model.
> **55(2)** … may rely on codes of practice … until a harmonised standard is published. … Providers who do not adhere … **shall demonstrate alternative adequate means of compliance for assessment by the Commission**.
> **55(3)** Any information or documentation obtained pursuant to this Article, **including trade secrets**, shall be treated in accordance with … Article 78.

- **55(1)(c) is three verbs**, separately testable, and extends to corrective measures.
- **55(1)(c) supplies no period**—only “without undue delay”.
- **55(2) guarantees a requestable artifact on either branch.**
- **55(3) forecloses the trade-secret objection**: confidentiality is handled on receipt.

**And the Omnibus added a duty on the other side of that branch.** Article 56(6), as replaced by Regulation (EU) 2026/1744, now requires that the Commission, taking utmost account of the Board’s opinion, “shall assess whether the codes of practice **cover the obligations provided for in Articles 53 and 55**, and shall regularly monitor and evaluate the achievement of their objectives. The Commission shall **publish** its assessment of the adequacy of the codes of practice.” A provider on the Code branch is therefore relying on an instrument whose adequacy the Commission is under a standing duty to assess and to publish on. Whether such an assessment exists, and what it says about Article 55 coverage, is a question the public record can answer and this analysis has not yet put to it.

**The searching has been done, and the documents have now been read.** They are stronger than this analysis first assumed, and they correct it.

**Commission Opinion C(2025) 5361 final, 1 August 2025**, concludes at paragraph (57) that “the General-Purpose AI Code of Practice **adequately covers the obligations provided for in Articles 53 and 55** of the AI Act and meets the aims according to Article 56 of the AI Act”. At paragraph (38) it finds specifically that “the Safety and Security Chapter of the Code adequately covers the obligations provided for in **Article 55(1)**”. The Conclusion of the AI Board of the same week agrees—“the Code covers the obligations provided for in Article 53 and Article 55”—while adding a reservation the Commission does not: the Board “nonetheless recommends closely monitoring the effectiveness of these measures”.

So the Article 56(6) assessment exists, it names the provisions, and it was published a year before the Omnibus wrote that duty into the enacting text.

**And paragraph (33) does something more.** Describing Commitment 9, the Commission says it sets out “what **‘without undue delay’ typically requires** of reporting timelines (Measure 9.3)”. That is the Commission stating what the statutory phrase in Article 55(1), point (c) typically requires, and pointing at the two/five/ten/fifteen-day scheme. The earlier conclusion in this document—that Article 55(1), point (c) “supplies no period at all”—is true of the Act and misleading about the regime. The Act fixes no period; the Commission has published what it takes the Act’s phrase to require; and for these facts that is **five days from awareness**.

Paragraph (35) adds that the Article 55(1) obligations “are not isolated but complement and feed into each other”: evaluations under point (a) and serious incident reporting under point (c) are “an essential part of” systemic risk assessment under point (b), and cybersecurity under point (d) “limits the scenarios that could lead to” incidents. On that reading a containment failure is not merely a reporting event; it is evidence going to the adequacy of the assessment and the cybersecurity protection.

Article 56 is also the **only** provision inside Chapter V that the Omnibus touched. Articles 51 to 55—every obligation analysed here—stand as enacted in 2024.

**Recital 114** extends evaluation obligations to testing “in particular prior to its first placing on the market” and across “the entire model’s lifecycle”.

**Recital 115** contemplates the duty arising where “**the development or use** of the model causes a serious incident”, and enumerates what cybersecurity protection must “duly consider”: *accidental model leakage, unauthorised releases, **circumvention of safety measures**, defence against cyberattacks, unauthorised access, model theft*; facilitated by securing “model weights, algorithms, **servers**, and data sets … **cyber and physical access controls**”.

> **Weight of the recitals.** Recital 115 is an interpretive aid and cannot derogate from the enacting terms—settled law (*Nilsson* C-162/97; *Manfredi* C-308/97; *Tyson Parketthandel* C-134/08). It cannot be used to overcome the Article 2(8) exclusion or the Article 3(63) carve-out. It remains good authority for reading the **content** of obligations that do attach, which is how §4 uses it.

---

## 5. Article 91: power to request documentation and information (unamended)

> 1. **The Commission** may request the provider of the general-purpose AI model concerned to provide the documentation drawn up by the provider in accordance with Articles 53 and 55, or any additional information that is necessary for the purpose of assessing compliance …
> 2. Before sending the request for information, **the AI Office** may initiate a structured dialogue with the provider …
> 3. Upon a duly substantiated request from the scientific panel, **the Commission** may issue a request for information … where the access to information is necessary and proportionate for the fulfilment of the tasks of the scientific panel under Article 68(2).
> 4. The request for information shall **state the legal basis and the purpose** of the request, **specify what information is required**, **set a period** within which the information is to be provided, and **indicate the fines provided for in Article 101** for supplying incorrect, incomplete or misleading information.
> 5. The provider … or its representative shall supply the information requested. … The clients shall nevertheless remain fully responsible if the information supplied is incomplete, incorrect or misleading.

**The power is the Commission’s.** Article 3, point (47) makes the AI Office “the Commission’s function”; it is not a legal person and cannot issue an Article 91 request in its own name. Only paragraph 2 (structured dialogue) is expressed as the Office’s. A draft instrument issued in the Office’s name is ultra vires on its face.

*Drafting note: the cross-reference in Article 91(3) to “Article 68(2)” is a known artefact—the scientific panel’s tasks sit in Article 68(3). Reproduce the reference as enacted, and note it.*

---

## 5a. The Code of Practice supplies the period Article 55(1), point (c) does not

Article 55(1), point (c) requires reporting “without undue delay” and fixes no period. The Safety and Security Chapter of the GPAI Code of Practice does fix periods, and a provider on the Article 55(2) Code branch has undertaken them.

**Commitment 9, Serious incident reporting**, states its own legal basis as “Article 55(1), and recitals 114 and 115 AI Act”, and commits Signatories to keeping track of, documenting and reporting relevant information “without undue delay ... **along the entire model lifecycle**”.

**Measure 9.3, Reporting timelines.** An initial report covering points (1) to (7) of Measure 9.2 is due, running from the date the Signatory becomes aware of the involvement of its model:

| Trigger | Period |
|---|---|
| Serious and **irreversible** disruption of the management or operation of critical infrastructure | **2 days** |
| **A serious cybersecurity breach, including the (self-)exfiltration of model weights and cyberattacks** | **5 days** |
| A death of a person | 10 days |
| Serious harm to health, infringement of Union-law fundamental-rights obligations, or serious harm to property or the environment | 15 days |

Three things follow.

**The second trigger has no counterpart in Article 3, point (49).** The Act’s four limbs are death or serious health harm, serious and irreversible disruption of critical infrastructure, infringement of fundamental-rights obligations, and serious harm to property. A serious cybersecurity breach is not among them. The Code adds it, and a model escaping containment and reaching a third party’s production infrastructure sits inside it far more comfortably than inside limb (d).

**That reverses the tiering problem this analysis recorded earlier.** An earlier draft proposed importing the Article 73(4) tiering and found the proposal self-defeating, because the facts sat in the property limb and so attracted the slowest tier. On the Code’s own scheme they sit in the cybersecurity limb, and the period is **five days**.

**The threshold for starting the clock is low.** Each period runs where the Signatory establishes “**or suspect[s] with reasonable likelihood**” the causal relationship between its model and the event—not where it concludes one.

Intermediate reports follow at least every four weeks while an incident is unresolved, a final report within 60 days of resolution, and documentation is retained at least five years (Measures 9.3, 9.4).

**Recorded as a negative finding**: as of 12 September 2026, the chapter contains no definition of ‘serious incident’ and does not cite Article 3, point (49) anywhere. Its triggers stand in their own terms. For a Signatory, that sidesteps the bridging problem at §5 rather than solving it—the gap in the Act remains, but it stops being the operative question.

**And the Commission has since bridged it, in guidance, which was found late.** Paragraph (100) of the guidelines of 19 November 2025 puts both propositions the Code leaves open. First, that Article 55(1), point (c) itself “covers serious cybersecurity breaches related to the model or its physical infrastructure, including the (self-)exfiltration of model parameters and cyberattacks”, anchored in Article 55(1), points (b) and (d)—so the cybersecurity trigger is not the Code’s alone, and the five-day route does not depend on reading the Commission Opinion at ¶33 as construing the Act. Second, that apart from cybersecurity the AI Office treats as a serious incident “any incident or malfunctioning of a general-purpose AI model that directly or indirectly leads to any of the events listed in the corresponding definition for AI systems in Article 3(49), points (a) to (d)”. Neither is in the enacting text. Both are supplied by the body that will enforce it, in a document whose own paragraph 9 disclaims authority to interpret the Act—which is the Recital 97 pattern exactly, and the reason the first recommendation exists.

The register records this as the twelfth error rather than as a find. The document had been held since the first day and was searched for the scope question only.

**And Recital (a) of the Code answers the scope question from the industry side.** Signatories recognise that providers “should continuously assess and mitigate systemic risks, taking appropriate measures along the entire model lifecycle **(including during development that occurs before and after a model has been placed on the market)**”. That is not the Commission interpreting the Act, and it is not a recital of the Act. It is the providers’ own undertaking, and for a Signatory it makes the development-phase question one of commitment rather than construction.

## 6. Article 101(1), point (b): fines (unamended)

> The Commission may impose … fines not exceeding **3 % of … annual total worldwide turnover … or EUR 15 000 000, whichever is higher**, when the Commission finds that the provider intentionally or negligently: … (b) **failed to comply with a request for a document or for information pursuant to Article 91**, or supplied incorrect, incomplete or misleading information;

**Non-retroactivity.** Article 101 has applied only since 2 August 2026 (§8). Both episodes predate that, so **no Article 101(1)(a) exposure arises for the underlying conduct** (Article 49(1) of the Charter). **Article 101(1)(b) is unaffected**, because a failure to respond to a request issued now would occur now.

---

## 7. Article 73 and Article 75(1a): why not Article 73

> **Art. 73(1)** *(unamended)*: Providers of **high-risk AI systems placed on the Union market** shall report any serious incident to the market surveillance authorities …
> **73(2)**: immediately after a causal link is established, and in any event **not later than 15 days** after becoming aware.
> **73(3)**: for a widespread infringement or a serious incident as defined in **Article 3, point (49)(b)**—immediately, and **not later than two days**.
> **73(4)**: in the event of the death of a person—immediately after establishing or suspecting a causal relationship, but **not later than 10 days** after becoming aware.

> **Art. 75(1)** *(`▼M1`)*: The AI Office shall be **exclusively competent** for supervision and enforcement in relation to … (a) AI systems based on general-purpose AI models where the model and the system are developed by the same provider …
> **Art. 75(1a)** *(`▼M1`)*: **By way of derogation from Article 73**, providers of high-risk AI systems subject to the competence of the AI Office … shall report any serious incidents **to the AI Office**. Article 73(2) to (9) shall apply mutatis mutandis. …

**Why Article 73 does not bite**, in order of strength: (i) Article 73(1) reaches systems **placed on the Union market**, and (ii) Article 2(8) excludes pre-market research, testing and development activity. The absence of an Annex I or Annex III classification is a third reason, not the first. Independently, Chapter III Sections 1–3 are deferred to 2 December 2027 and 2 August 2028 by amended Article 113(c).

**The asymmetry** *(restated correctly)*: where a GPAI-based system is high-risk and same-provider, Article 75(1a) routes reporting to the AI Office **with** Article 73’s tiering. The model-level duty at Article 55(1)(c) has the same addressee and **no period at all**.

> **Do not propose importing the Article 73 tiering wholesale.** The two-day tier attaches only to Article 3(49)**(b)**. On facts sitting in limb **(d)**, importing the tiering yields the **15-day** tier—the slowest available. Any drafting recommendation must specify the tier, not the scheme.

---

## 8. Application dates: derived from Article 113

- Opening: “It shall apply from **2 August 2026**.” *(general rule)*
- Point (b) **`▼B`**: “Chapter III Section 4, **Chapter V**, Chapter VII and Chapter XII and Article 78 shall apply from **2 August 2025**, **with the exception of Article 101**.”
- Point (c) `▼M1`: Chapter III Sections 1–3 deferred to **2 December 2027** (Annex III) and **2 August 2028** (Annex I).
- Point (d) `▼M1`: Articles 102–110 from 27 July 2026.

**Derivation**: Chapter V contains Articles 51–56, so **Article 55 has applied since 2 August 2025**. Article 101 is excepted from point (b) and appears nowhere else, so it falls back on the general rule: **Article 101 applies from 2 August 2026**. Derivable from the Act alone.

---

## Outstanding verification
- [ ] Whether the affected platform is an entity providing an essential service within a CER Annex sector
- [ ] GPAI Code of Practice Commitment 9 and the Commission’s serious-incident reporting template (~28 October 2025), verbatim
- [ ] Code of Practice signatory status from the Commission’s own register rather than a third-party registry
