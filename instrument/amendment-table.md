# Amendment table: putting the Recital 97 test in the enacting text

*Companion to the report’s recommendations. Drafted by an external researcher for the Apart Research / CeSIA AI Incident Response Sprint; not a document of any Union institution and not a legislative proposal. Each amendment lifts its added words from a recital, a Commission act or an enacting provision that is held and verified in this repository, and says which. The drafting is offered in the form a legislator works in—current text, amended text, source, justification—so that disagreement can be with a word rather than with a recommendation.*

The problem the three amendments answer is stated at §4.1 of the report: the deemed-placement rule, its internal-use exception and its systemic-risk carve-out all sit in Recital 97 and in guidance that disclaims its own authority, and a preamble cannot be relied on “for interpreting those provisions in a manner clearly contrary to their wording” (*Deutsches Milch-Kontor*, C-136/04, ¶32). Amendments 1 and 2 move the rule into the enacting terms. Amendment 3 gives the model-level reporting obligation the period the Commission Opinion says the Code already supplies. Amendment 4 is not to the Regulation at all; it is to a form, and it is delivered as a file.

## Amendment 1: Article 3, point (9), ‘placing on the market’—the deeming rule

| | Text |
|---|---|
| **Current** | ‘placing on the market’ means the first making available of an AI system or a general-purpose AI model on the Union market; |
| **Amended** | ‘placing on the market’ means the first making available of an AI system or a general-purpose AI model on the Union market; **a general-purpose AI model shall be considered to be placed on the market where its provider integrates it into its own AI system that is made available on the market or put into service in the Union, unless the model is used for purely internal processes that are not essential for providing a product or a service to third parties and the rights of natural persons are not affected; that exception shall not apply to a general-purpose AI model meeting the condition referred to in Article 51(1), point (a);** |
| **Source of the added words** | Recital 97: “When the provider of a general-purpose AI model integrates an own model into its own AI system that is made available on the market or put into service, that model should be considered to be placed on the market”; “The obligations laid down for models should in any case not apply when an own model is used for purely internal processes that are not essential for providing a product or a service to third parties and the rights of natural persons are not affected”; “the general-purpose AI models with systemic risk should always be subject to the relevant obligations under this Regulation”. The words “in the Union” are Article 3, point (11)’s. |
| **Justification** | The rule is the one the Commission already applies (Guidelines ¶54 reproduces the recital; ¶51 lists essential internal use as an example of placing; the Q&A states the three conditions). Enacting it removes the *Milch-Kontor* objection and settles the own-use limb, which is the limb the enacting text’s “supply” wording does not obviously cover. The carve-out is expressed by reference to the condition in Article 51(1), point (a) rather than the defined term ‘general-purpose AI model with systemic risk’, because a model outside the definition of ‘general-purpose AI model’ cannot be inside the narrower one; the reference to the condition avoids that circularity. “In the Union” is added because the recital is silent on territory and Article 2(1), point (a) is not. |

## Amendment 2: Article 3, point (63), ‘general-purpose AI model’—the research exclusion

| | Text |
|---|---|
| **Current** | … except AI models that are used for research, development or prototyping activities before they are placed on the market; |
| **Amended** | … except AI models that are used, before they are placed on the market, **for the sole purpose of** research, development or prototyping activities, **without prejudice to the obligation to comply with this Regulation when, following such activities, a model is placed on the market**; |
| **Source of the added words** | Recital 97: “The definition should not cover AI models used before their placing on the market for the sole purpose of research, development and prototyping activities … without prejudice to the obligation to comply with this Regulation when, following such activities, a model is placed on the market.” The “sole purpose” formula is already enacting text at Article 2(6). |
| **Justification** | The recital states the exclusion with a qualifier and a proviso that the definition does not carry. A model in development toward placement is then reached through Amendment 1 and through the lifecycle reading at Guidelines ¶22, and a model developed for research alone stays outside, which is what Recital 25 says the exclusion is for. This amendment does not by itself bring an internal research model into scope; it ensures the exclusion protects a model never placed, not the development phase of one that is. |

## Amendment 3: Article 55(1), point (c)—a determinate period

| | Text |
|---|---|
| **Current** | keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures to address them; |
| **Amended** | keep track of, document, and report, without undue delay **and in any event not later than [15] days after the provider becomes aware of the involvement of its model in the incident**, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures to address them; |
| **Source of the added words** | The trigger is Measure 9.3 of the Code’s Safety and Security Chapter, whose periods run from the date “the Signatories become aware of the involvement of their model in the incident”. The form “without delay and in any event within two weeks” is Article 52(1)’s own. The number is a policy choice and is bracketed; Measure 9.3 tiers it at two, five, ten and fifteen days by category, and Article 73(2) to (4) uses fifteen, two and ten for high-risk systems. |
| **Justification** | Article 55(1), point (c) fixes no period, where Article 73(2) to (4) and Article 52(1) in the same Regulation each fix one. The Commission Opinion C(2025) 5361 final, at paragraph (33), describes Measure 9.3 as setting out “what ‘without undue delay’ typically requires of reporting timelines”, so the period exists in practice for Signatories and not in law for anyone. Article 55(2) makes the Code a means of demonstrating compliance, not an obligation, so a provider that does not adhere has no period at all. The amendment takes the Code’s trigger and the Chapter’s own drafting form. Tiering by category, as Measure 9.3 does, is possible but would import the Article 3, point (49) limbs into a provision the AI Office reads (Guidelines ¶100) as reaching cybersecurity breaches without them. |

## Amendment 4: the serious-incident template—two fields

Delivered as `model-amended-serious-incident-template.docx`, built from the Commission’s own DOCX of 4 November 2025 with every existing field unchanged and two added:

| Field | Label | Prompt |
|---|---|---|
| **1a** | Date on which the provider became aware of the involvement of its model in the serious incident | The date on which the provider became aware of the involvement of its model in the serious incident, in format YYYY-MM-DD, and, where different, the date on which the provider established or suspected with reasonable likelihood a causal relationship between its model and the incident. This is the date from which the reporting timelines in Measure 9.3 of the Safety and Security Chapter run. |
| **1b** | Date of submission of this report | The date of submission of this report, in format YYYY-MM-DD, and the type of report: initial, intermediate or final (Measure 9.3). |

**Source.** The high-risk draft template’s section 1.2 asks for “Date of report submission” and “Manufacturer awareness date of reportability” in “format YYYY-MM-DD”; the trigger wording is Measure 9.3’s; the report-type cycle is Measure 9.3’s initial, intermediate and final reports. **Justification.** Fields 1 to 9 of the published template transcribe Measure 9.2, which lists what a report contains and not when the clock started; without 1a a completed form cannot show whether the initial report was timely, and without 1b it cannot show it even to the recipient’s own file. Nothing in Article 55(2) or the Code prevents the form asking for more than Measure 9.2 lists. This is the amendment that needs no legislator: the template is the Commission’s to change.

---

*Provisions quoted are from `data/provisions.yaml`, verified against CELEX 02024R1689-20260727; recitals from CELEX 32024R1689; the Code, the Opinion, the Guidelines and both templates are held in `_sources/` and hashed in `data/sources.yaml`.*
