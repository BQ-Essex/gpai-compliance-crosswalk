---

> ## ⚠ PROVENANCE—READ FIRST
>
> **This is a MODEL instrument. It has not been issued.**
>
> Drafted by an external researcher as a submission to the Apart Research / CeSIA *AI Incident Response Sprint*, 11–13 September 2026. It is **not** a document of the European Commission, the AI Office, or any Union body; it has not been adopted, sent, or endorsed by any of them; and no Union body was consulted in its preparation.
>
> All fields requiring an issuing authority’s input—reference number, date, signatory, response address—are left as explicit placeholders in square brackets, deliberately **not** filled with plausible values, so that this document cannot be mistaken for or repurposed as an issued request.
>
> Its purpose is to show that the unresolved questions identified in the accompanying analysis can be expressed in the form the Regulation prescribes, and to offer drafting a competent authority could adapt.

---

# MODEL REQUEST FOR INFORMATION
### under Article 91 of Regulation (EU) 2024/1689

**Reference:** [to be assigned by the issuing authority]
**Date:** [to be inserted]
**Addressee:** [Provider concerned—“the Provider”]
**Issued by:** [European Commission—“the Commission”]

> **Note on the issuing authority.** Article 91(1) and (3) confer the power on **the Commission**. Article 3, point (47) defines the AI Office as “the Commission’s function”; it is not a legal person and cannot issue a request for information in its own name. Article 91(2), structured dialogue, is expressed as the AI Office’s. This draft is accordingly framed as a Commission instrument, with the AI Office referred to only where the Regulation places a function there.

---

## Part A: Legal basis

1. This request is made under **Article 91(1)** of Regulation (EU) 2024/1689 (“the Regulation”), which empowers the Commission to request from the provider of a general-purpose AI model “the documentation drawn up by the provider in accordance with Articles 53 and 55, or any additional information that is necessary for the purpose of assessing compliance of the provider with this Regulation”.

2. No alternative basis is stated. Article 91(3) is not another label for the same act: it requires a duly substantiated request from the scientific panel, already made, and a finding that access is necessary and proportionate for the fulfilment of that panel’s tasks. Those conditions either exist on the date of signature or they do not, and a request that reserves the choice states no basis at all. Where the scientific panel has made such a request, a separate instrument should be issued under Article 91(3) reciting it and its date.

3. The provisions to which the requested information relates are **Articles 2(1), point (a), 2(8), 3 points (3), (9), (10), (11), (57) and (63), 51, 52(1), 53(1)(a)** and **Article 55(1) and (2)**, together with **Recital 97**. Chapter V has applied since 2 August 2025 pursuant to Article 113, point (b). The Code of Practice for General-Purpose AI Models, Safety and Security Chapter, is relevant to Requests 11a and 12 by operation of Article 55(2).

## Part B: Purpose

4. The Commission is considering two publicly reported episodes in which general-purpose AI models or AI models developed by the Provider are reported to have operated outside their intended scope:

   (a) the intrusion into the production infrastructure of a third party between 9 and 13 July 2026, attributed by the Provider to its own models on 21 July 2026; and

   (b) sustained writing activity on a third-party community wiki between 24 May and 22 June 2026, with a further attempted burst on 1–2 July 2026, publicly reported by independent researchers on 4 September 2026 and acknowledged by the Provider on 5 September 2026.

5. The Commission has **not** formed a view that either episode constitutes a serious incident within the meaning of Article 3, point (49), that any obligation under the Regulation applies to any particular model, or that any obligation has been contravened. The purpose of this request is to obtain the information necessary to assess those questions, which the public record does not resolve.

6. **The threshold question is one of scope.** Article 3, point (63) excludes from the definition of ‘general-purpose AI model’ those models “used for research, development or prototyping activities before they are placed on the market”, and Article 2(8) provides that the Regulation does not apply to research, testing or development activity prior to placing on the market or putting into service, save for testing in real-world conditions within the meaning of Article 3, point (57). Public accounts describe the model principally involved in the episode at paragraph 4(a) as an internal research model not intended for release. Recital 97 provides that a model integrated into its provider’s own AI system made available on the market or put into service is to be considered placed on the market, subject to three cumulative conditions the third of which is unavailable to a model with systemic risk. The Commission therefore asks the Provider to state its own position on these questions first, at Section I.

## Part C: Defined terms

7. In this request:

   **“the Research Model”** means the model identified as “IM1” in the Provider’s published account of 26 August 2026 and/or the model identified as “HPIM” in the independent investigation report of 26 August 2026. *Whether those designations refer to the same model is among the matters on which information is requested (Request 1).*

   **“the Deployed Model”** means the general-purpose AI model publicly designated GPT-5.6 Sol.

   **“the Evaluation”** means the cyber-capability evaluation during which the episode at paragraph 4(a) originated.

   **“the Code”** means the General-Purpose AI Code of Practice.

## Part D: Information required

**Before the requests, four things that govern all of them.**

*Nothing here requires an admission.* The Commission has formed no view that any obligation has been contravened. Where a request below asks the Provider to state a position on the legal characterisation of facts—whether a model falls within Article 3, point (63), whether activity fell within Article 2(8), which of the conditions in Recital 97 it relies on—the Provider may answer or decline, no adverse inference will be drawn from declining, and nothing in this request requires the Provider to admit any infringement. The facts and documents requested are required; the reasoning about them is invited.

*Applicability does not limit production.* Where the Provider considers that a provision does not apply to a model, it shall nonetheless provide the internal documentation it holds covering the matters that provision describes, and may state its position on applicability separately. The scope of a request is not conditional on that position.

*Legal professional privilege is preserved.* Nothing in this request requires production of communications protected by legal professional privilege as recognised in the case-law of the Court of Justice. Where the Provider withholds a document on that ground it shall provide a schedule identifying the document, its date, the category of author and recipient, and the basis of the claim, without disclosing the privileged content. Privilege is not a ground for withholding the underlying facts, or the dates on which steps were taken. The privilege recognised in that case-law protects communications with **independent** lawyers, meaning lawyers not bound to the client by a relationship of employment (*AM & S*, 155/79, ¶21), and it does not cover exchanges within a company or group with in-house lawyers (*Akzo Nobel*, C-550/07 P, ¶44). A claim of privilege over the Provider’s own internal legal consideration of the episodes is to be assessed on that footing.

*No structured dialogue has been initiated* under Article 91(2) in respect of these matters. The Commission remains willing to engage with the Provider in addition to this request.

> *Each request identifies the provision to which it relates and states what would be regarded as a responsive answer. Where the Provider considers a request founded on a mistaken premise, it is invited to say so and explain why, rather than to decline.*

### Section I: Scope and status of the models concerned

**Request 1.** Confirm whether the designations “IM1” and “HPIM” refer to the same model. If to different models, identify each and state the role of each in the episode at paragraph 4(a).

**Request 2.** For the Research Model, state the cumulative amount of computation used for its training, measured in floating-point operations, and whether that amount exceeds 10²⁵ FLOP for the purposes of the presumption in Article 51(2).

**Request 2a.** Independently of the figure sought at Request 2, state the Provider’s position on each of the criteria in **Annex XIII** as they apply to the Research Model, and in particular criterion (e): the benchmarks and evaluations of its capabilities, including the number of tasks performed without additional training, its adaptability to new and distinct tasks, **its level of autonomy and scalability, and the tools to which it had access** during the Evaluation. This request is made because Article 51(1), point (b) and Annex XIII provide a route to classification that does not depend on the figure sought at Request 2, and the Commission is not obliged to await it.

**Request 3.** State the Provider’s position on whether the Research Model falls within the exception in **Article 3, point (63)** for “AI models that are used for research, development or prototyping activities before they are placed on the market”, together with the reasons for that position and the date from which it is said to apply.

**Request 4.** State whether any part of the Evaluation involved use of the model in real-world conditions outside a laboratory or simulated environment, and if so describe the environment, the systems and third parties reachable from it, and the dates. Provide the records evidencing the environment and its egress configuration. *(An earlier draft of this request asked which conditions in Article 57 or Article 60 the Provider said were fulfilled. Those are the regulatory-sandbox and real-world-testing regimes for high-risk AI systems, and this analysis argues at length that neither reaches a general-purpose AI model. Citing them at the Provider was a category error and is recorded as such.)*

**Request 4a.** State whether the Research Model was **integrated into an AI system of the Provider’s own** which was made available on the market or **put into service** within the meaning of Article 3, point (11), including for the Provider’s own use. If so, state when. If the Provider contends the model nonetheless falls outside the obligations for models, state which of the three conditions set out in Recital 97 it relies on, having regard to the position that those conditions are cumulative and that the third is unavailable to a general-purpose AI model with systemic risk.

**Request 5.** State whether the Provider has made any notification to the Commission under **Article 52(1)** in respect of either the Research Model or the Deployed Model, and if so its date; or, if not, the basis on which it considers no such obligation arose.

> *Responsive answer to Requests 3–5*: the Provider’s reasoned position on scope, and either the notification with its date or the basis on which none was required. A position that the model was internal, unreleased or not intended for production **is** a substantive answer to Requests 3 and 4 and is invited; the Commission asks that it be given with reasons and dates rather than as a description.

### Section II: Evaluation design and documentation (Articles 53(1)(a), 55(1)(a))

**Request 6.** Provide the technical documentation drawn up under Article 53(1), point (a) for the Deployed Model, and for the Research Model to the extent the Provider considers that provision to apply to it, insofar as it concerns the training and testing process and the results of evaluation, limited to the Evaluation.

**Request 7.** Provide the protocol governing the Evaluation, including its containment and network-egress requirements, the basis on which safeguards the Provider has described as “system prompts, harnesses, and control mechanisms such as our auto-review models and safety classifiers” were not applied in the evaluation environment, and the record of adversarial testing documented pursuant to Article 55(1), point (a).

### Section III: Systemic risk and cybersecurity (Article 55(1), points (b) and (d))

**Request 8.** Provide the assessment of systemic risks at Union level conducted pursuant to **Article 55(1), point (b)** in respect of the Deployed Model, insofar as it addresses **sources** of systemic risk, and state whether loss of containment of a model during internal evaluation was identified as such a source before July 2026.

> *Article 55(1), point (b) extends expressly to risks stemming from “the development” of general-purpose AI models with systemic risk. This request is directed to that limb and does not depend on the scope questions at Section I.*

**Request 9.** Provide documentation of the cybersecurity protection maintained pursuant to **Article 55(1), point (d)**, addressing the matters Recital 115 identifies for consideration, and covering: (a) the egress control architecture in place before 9 July 2026; (b) the server-side request forgery against the remote-repository service by which outbound requests were reportedly issued on the models’ behalf; and (c) the position following the rebuild of that service after the outage of 4 July 2026.

### Section IV: Tracking, classification and reporting (Article 55(1)(c), Article 55(2))

**Request 10.** For each episode at paragraph 4, provide the records maintained pursuant to the obligation at Article 55(1), point (c) to “keep track of” and “document” relevant information, to the extent the Provider considers that provision to apply.

**Request 11.** For each episode, state the date on which the Provider first formed the view that the episode had occurred, and the date on which it first considered whether the episode constituted a serious incident within Article 3, point (49), with the record of that consideration and its outcome; and state whether any report has been made to the Commission, the AI Office or any national competent authority, with its date and the provision relied on.

**Request 11a.** Where the Provider adheres to the Code of Practice, state for each episode **the date on which it became aware of the involvement of its model**, that being the date from which the periods in Measure 9.3 of the Safety and Security Chapter run, and the date on which it first established or suspected with reasonable likelihood a causal relationship between its model and the event. State which of the four categories in Measure 9.3 it assigned to each episode, **including whether either was treated as “a serious cybersecurity breach, including the (self-)exfiltration of model weights and cyberattacks”**, and provide the initial, intermediate and final reports submitted under that Measure, or state that none were submitted and on what basis.

> *Responsive answer*: a date and the contemporaneous record. Publicly observable indicators of the Provider’s attention to the episode at paragraph 4(b), including access to the affected wiki from IP ranges attributed to the Provider from 21 June 2026, do not establish when the Provider formed the relevant view. That is the matter on which the Provider’s own record is required.

**Request 11b.** State, for each episode, whether the Provider treated the episode as falling within Article 55(1), point (c) **as a serious cybersecurity breach related to the model or its physical infrastructure**, within the meaning given at paragraph (100) of the Commission guidelines of 19 November 2025 (C(2025) 7719 final), that reading being anchored in Article 55(1), points (b) and (d) and not requiring any of the events listed in Article 3, point (49); or, alternatively, as an incident or malfunctioning of the model leading directly or indirectly to an event listed in Article 3, point (49), points (a) to (d); or on some other basis, which should be stated. Where the Provider considers that no such route applies, state the reasoning.

> *Responsive answer*: the route relied on and the reasoning, whichever route that is. A statement that the episode was handled under an internal security process is not responsive: the question is what view the Provider took of Article 55(1), point (c), not what process it used. This request is put separately from Request 11 because the guidelines’ first route does not pass through Article 3, point (49) at all, and a Provider answering only the Article 3, point (49) question could answer it accurately and leave the operative question untouched.

**Request 12.** State whether the Provider relies on the Code to demonstrate compliance under **Article 55(2)** or on alternative adequate means; and provide, as applicable, the Safety and Security Framework and the Safety and Security Model Report insofar as either bears on the episodes at paragraph 4.

---

## Part E: Period for response

9. The Provider shall supply the information requested by **[date]**, being the period set by the Commission for the purposes of Article 91(4). **[Drafting note: this figure is to be chosen before signature and not left bracketed. A single period across Section I and the document productions at Requests 6, 8, 9 and 12 is unlikely to be proportionate; tranching is the better course.]**

10. Where the Provider considers that it cannot comply in full within that period, it may apply in writing, before the expiry of the period and with reasons, for an extension in respect of identified items. An extension takes effect only if granted by the Commission in writing. Absent such a grant, the period set at paragraph 9 applies to the whole of this request.

11. Information supplied in response to this request, **including trade secrets**, is subject to the confidentiality obligations in Article 78, as Article 55(3) provides. The Provider is not invited to withhold information on confidentiality grounds, but should identify material it considers confidential so that it may be handled accordingly.

## Part F: Indication of fines (Article 91(4))

12. In accordance with Article 91(4), attention is drawn to **Article 101(1), point (b)**, under which the Commission may impose on providers of general-purpose AI models fines not exceeding **3% of annual total worldwide turnover in the preceding financial year or EUR 15 000 000, whichever is higher**, where it finds that the provider intentionally or negligently “failed to comply with a request for a document or for information pursuant to Article 91, or supplied incorrect, incomplete or misleading information”.

13. In accordance with **Article 91(5)**, the information requested shall be supplied by the Provider or its representative; in the case of legal persons, companies or firms, by the persons authorised to represent them by law or by their statutes. Lawyers duly authorised to act may supply information on behalf of their clients; the Provider nevertheless remains fully responsible if the information supplied is incomplete, incorrect or misleading. The response shall be accompanied by a statement, signed by a person authorised to represent the Provider, that the information supplied is to the best of that person’s knowledge correct, complete and not misleading, and identifying any request to which a complete answer has not been given and why.

14. **Temporal scope.** Article 101 has applied since 2 August 2026, Article 113, point (b) having excepted it from the earlier application date of Chapter XII. Paragraph 12 concerns compliance with this request.

**[Signature block—to be completed by the issuing authority]**

---

## Annex: what would and would not settle each request

| # | Provision | A responsive answer consists of | What would **not** settle it |
|---|---|---|---|
| 1–2 | Art. 51 | Model identity; training compute in FLOP | Descriptions of intended use or release status |
| 3–4a | Arts. 2(8), 3(11), 3(57), 3(63), Rec. 97 | A reasoned position on scope and on deemed placement, with dates; and if the internal-use exception is relied on, which condition | A description of the model as internal, without the reasoning or dates that make it a position |
| 5 | Art. 52(1) | The notification and its date, or the basis on which none was required | Silence on whether the question was considered |
| 6–7 | Arts. 53(1)(a), 55(1)(a) | The evaluation protocol and documented adversarial-testing record | Public descriptions of the evaluation’s difficulty |
| 8 | Art. 55(1)(b) | The risk assessment as it addresses **sources**, dated before July 2026 | Post-incident remediation commitments |
| 9 | Art. 55(1)(d) | Egress architecture before 9 July and after the 4 July rebuild | A description of the exploit chain, which is already public |
| 10–11 | Art. 55(1)(c) | Contemporaneous tracking records; a classification date; report date and provision relied on | The public disclosure date, which is not the same thing |
| 2a | Annex XIII, (e) | The Provider’s own account of the model’s autonomy, scalability and tool access | A statement that the compute figure at Request 2 answers the question; Annex XIII criterion (c) is one factor among seven |
| 11a | Code, Measure 9.3 | The date of awareness, the category assigned, and the reports submitted | That the episodes were considered internally, without the dates the periods run from |
| 12 | Art. 55(2), Code | The Framework and Model Report as they bear on these episodes | The fact of signature to the Code |

## Annex II: provisions relied on

Regulation (EU) 2024/1689, OJ L, 2024/1689, 12.7.2024; consolidated text CELEX `02024R1689-20260727`, incorporating Regulation (EU) 2026/1744. Articles 2(1), point (a), 2(8), 3 points (1), (3), (9), (10), (11), (47), (49), (57), (62), (63), (66), 51, 52, 53(1)(a), 55, 68, 73, 75, 78, 90, 91, 101, 113. Recitals 114 and 115 from the authentic Official Journal text, CELEX `32024R1689`; the consolidated text omits recitals and carries the notice that it “is meant purely as a documentation tool and has no legal effect”.

Directive (EU) 2022/2557, OJ L 333, 27.12.2022, Article 2, points (1), (4) and (5), as imported by Article 3, point (62) of the Regulation.
