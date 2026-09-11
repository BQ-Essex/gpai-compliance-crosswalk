---

> ## ⚠ PROVENANCE — READ FIRST
>
> **This is a MODEL instrument. It has not been issued.**
>
> It was drafted by an external researcher as a submission to the Apart Research / CeSIA *AI Incident Response Sprint*, 11–13 September 2026. It is **not** a document of the European Commission, the AI Office, or any Union body; it has not been adopted, sent, or endorsed by any of them; and no Union body has been consulted in its preparation.
>
> All fields requiring an issuing authority's input — reference number, date, signatory, response address — are left as explicit placeholders in square brackets. They are deliberately **not** filled with plausible values, so that this document cannot be mistaken for, or repurposed as, an issued request.
>
> Its purpose is to demonstrate that the unresolved questions identified in the accompanying analysis can be expressed in the form the Regulation prescribes, and to offer drafting that a competent authority could adapt.

---

# MODEL REQUEST FOR INFORMATION
### under Article 91 of Regulation (EU) 2024/1689

**Reference:** [to be assigned by the issuing authority]
**Date:** [to be inserted]
**Addressee:** [Provider of the general-purpose AI models concerned — "the Provider"]
**Issued by:** [European Commission / AI Office — "the Office"]

---

## Part A — Legal basis

1. This request is made under **Article 91(1)** of Regulation (EU) 2024/1689 ("the Regulation"), which empowers the Commission to request from the provider of a general-purpose AI model "the documentation drawn up by the provider in accordance with Articles 53 and 55, or any additional information that is necessary for the purpose of assessing compliance of the provider with this Regulation".

2. In the alternative, where the Office prefers to proceed on the initiative of the scientific panel, this request may be issued under **Article 91(3)**, on a duly substantiated request from the scientific panel, the information sought being necessary and proportionate for the fulfilment of the panel's tasks under Article 68(2). *The drafting below is framed so as to serve either pathway without amendment.*

3. The obligations to which the requested information relates are those in **Article 52(1)**, **Article 53(1), point (a)**, and **Article 55(1), points (a) to (d)** and **Article 55(2)** of the Regulation. Chapter V has applied since 2 August 2025 pursuant to Article 113, point (b).

## Part B — Purpose of the request

4. The Office is assessing compliance in relation to two publicly reported episodes in which general-purpose AI models developed by the Provider are reported to have operated outside their intended scope:

   (a) the intrusion into the production infrastructure of a third party between 9 and 13 July 2026, publicly disclosed by the affected party on 16 July 2026 and attributed by the Provider to its own models on 21 July 2026; and

   (b) the sustained writing activity on a third-party community wiki between 24 May and 22 June 2026, with a further attempted burst on 1–2 July 2026, publicly reported by independent researchers on 4 September 2026 and acknowledged by the Provider on 5 September 2026.

5. The Office has **not** formed a view that either episode constitutes a serious incident within the meaning of Article 3, point (49), nor that any obligation under the Regulation has been contravened. The purpose of this request is to obtain the information necessary to assess those questions, which the public record does not resolve.

6. In particular, the Office notes that the Provider has publicly stated that it does "not yet have a clear standard for how to report misalignment that shows up during training, evaluation, and deployment". Recital 115 of the Regulation contemplates the reporting obligation arising where "the development or use of the model causes a serious incident", and Recital 114 extends the evaluation obligations across the entire model lifecycle. The relationship between the Provider's internal classification practice and its obligations under the Regulation is therefore material to this assessment.

## Part C — Defined terms

7. In this request:

   **"the Research Model"** means the internal research model identified as **"IM1"** in the Provider's published account of 26 August 2026, and/or the model identified as **"HPIM"** in the independent investigation report published on 26 August 2026. *Whether these designations refer to the same model is among the matters on which information is requested (Request 1).*

   **"the Deployed Model"** means the general-purpose AI model publicly designated GPT‑5.6 Sol.

   **"the Evaluation"** means the cyber-capability evaluation during which the episode at paragraph 4(a) originated.

   **"the Code"** means the General-Purpose AI Code of Practice, to which the Provider is recorded as a full signatory.

## Part D — Why a formal request rather than structured dialogue

8. Article 91(2) permits the Office to initiate a structured dialogue before sending a request for information. The Office considers a formal request appropriate here because: (i) the information sought consists principally of documentation that the Regulation already requires to be drawn up and kept up to date, rather than matters requiring exploratory discussion; (ii) a central question concerns whether a notification obligation subject to a **two-week** statutory period was engaged, which is resolved by a single document; and (iii) the episodes are the subject of active public and legislative attention in multiple jurisdictions, such that a documented and dated record of the Provider's position serves both parties. The Office remains willing to supplement this request with structured dialogue.

---

## Part E — Information required

> *Each request below identifies the provision to which it relates and states what the Office would regard as a responsive answer. Where the Provider considers a request to be founded on a mistaken premise, the Office invites it to say so and to explain why, rather than to decline.*

### Section I — Regulatory status of the Research Model (Article 51; Article 52(1))

**Request 1.** Confirm whether the designations "IM1" and "HPIM" refer to the same model. If they refer to different models, identify each and state the role of each in the episode at paragraph 4(a).

**Request 2.** For the Research Model, state the **cumulative amount of computation used for its training, measured in floating point operations**, and whether that amount exceeds 10²⁵ FLOP for the purposes of the presumption in Article 51(2).

**Request 3.** State whether the Provider has notified the Commission in respect of the Research Model pursuant to **Article 52(1)**, and if so, on what date, and the date on which the Provider considers the requirement in Article 51(1), point (a) to have been met or to have become known that it would be met.

**Request 4.** If no notification has been made, state the basis on which the Provider considers that the Research Model does not meet the condition in Article 51(1), point (a), including any arguments of the kind contemplated by Article 52(2).

> *Responsive answer*: a statement of the model's identity and training compute, and either the notification and its date, or the Provider's reasoned basis for considering the obligation not engaged.
> *Not responsive*: a statement that the model was internal, unreleased, or not intended for production. The obligation in Article 52(1) is triggered by capability and is expressed to apply where it "becomes known that it will be met"; it is not conditioned on placing on the market.

### Section II — Evaluation design and documentation (Article 53(1)(a); Article 55(1)(a))

**Request 5.** Provide the technical documentation drawn up under **Article 53(1), point (a)** for the Research Model and the Deployed Model, insofar as it concerns the training and testing process and the results of their evaluation, limited to the Evaluation.

**Request 6.** Provide the protocol governing the Evaluation, including: the containment and network-egress requirements it specified; the basis on which safeguards described by the Provider as "system prompts, harnesses, and control mechanisms such as our auto-review models and safety classifiers" were not applied in the evaluation environment; and the record of adversarial testing documented pursuant to **Article 55(1), point (a)**.

> *Responsive answer*: the protocol and the documented adversarial-testing record, or an explanation of where within the Article 53(1)(a) documentation those matters are recorded.

### Section III — Systemic risk and cybersecurity (Article 55(1), points (b) and (d))

**Request 7.** Provide the assessment of systemic risks at Union level conducted pursuant to **Article 55(1), point (b)**, insofar as it addresses **sources** of systemic risk, and state whether loss of containment of a model during internal evaluation was identified as such a source prior to July 2026.

**Request 8.** Provide documentation of the cybersecurity protection maintained pursuant to **Article 55(1), point (d)** for the evaluation environment, addressing in particular the matters Recital 115 requires to be duly considered — circumvention of safety measures, unauthorised access, and cyber access controls — and covering:
   (a) the egress control architecture in place before 9 July 2026;
   (b) the server-side request forgery against the remote-repository service by which outbound requests were reportedly issued on the models' behalf; and
   (c) the position following the rebuild of that service after the outage of 4 July 2026, the Provider having stated publicly that unintended internet access was thereafter **regained**.

> *Responsive answer to (c) in particular*: the Office draws attention to the recurrence of egress following remediation, which bears directly on the adequacy of protection under Article 55(1), point (d).

### Section IV — Incident classification, tracking and reporting (Article 55(1)(c); Article 55(2))

**Request 9.** For each episode at paragraph 4, provide the records maintained pursuant to the obligation in **Article 55(1), point (c)** to "keep track of" and "document" relevant information, and under **Commitment 9 of the Code**.

**Request 10.** For each episode, state **the date on which the Provider first formed the view that the episode had occurred**, and the date on which it first considered whether the episode constituted a serious incident within Article 3, point (49), together with the record of that consideration and its outcome.

**Request 11.** State whether the Provider has made any report to the Office or to any national competent authority in respect of either episode; and if so, for each report: its date, the provision of the Regulation under which it was made, and whether it addressed "possible corrective measures" as Article 55(1), point (c) requires.

**Request 12.** Provide the Safety and Security Framework maintained under Commitment 1 of the Code and the Safety and Security Model Report under Commitment 7, insofar as either addresses the episodes at paragraph 4 or the risks they concern, the Provider being a full signatory and therefore relying on the Code to demonstrate compliance under **Article 55(2)**.

> *Responsive answer to Request 10*: a date, and the contemporaneous record. The Office notes that publicly observable indicators of the Provider's attention to the episode at paragraph 4(b) — including access to the affected wiki from IP ranges attributed to the Provider from 21 June 2026 — do not themselves establish when the Provider formed the relevant view. That is the matter on which the Office requires the Provider's own record.

---

## Part F — Period for response

9. The Provider is requested to respond by **[date]**, being **[10] working days** from the date of this request in respect of Section I, and **[20] working days** in respect of Sections II to IV. The shorter period for Section I reflects that those requests are answerable from a small number of discrete records.

10. Where the Provider cannot respond fully within the period, it should provide a partial response within the period, identifying what is outstanding and the date by which it will be supplied.

11. Information supplied in response to this request, **including trade secrets**, is subject to the confidentiality obligations in **Article 78**, as Article 55(3) provides. The Provider is not required, and is not invited, to withhold information on confidentiality grounds; it should instead identify material it considers confidential so that it may be handled accordingly.

## Part G — Indication of fines (Article 91(4))

12. In accordance with Article 91(4), the Office draws the Provider's attention to **Article 101(1), point (b)** of the Regulation, under which the Commission may impose on providers of general-purpose AI models fines not exceeding **3% of annual total worldwide turnover in the preceding financial year or EUR 15 000 000, whichever is higher**, where it finds that the provider intentionally or negligently "failed to comply with a request for a document or for information pursuant to Article 91, or supplied incorrect, incomplete or misleading information".

13. Pursuant to Article 91(5), where information is supplied by legal representatives or by lawyers duly authorised to act, the Provider **remains fully responsible** if the information supplied is incomplete, incorrect or misleading.

14. Article 101 has applied since 2 August 2026, Article 113, point (b) having excepted it from the earlier application date of Chapter XII.

**[Signature block — to be completed by the issuing authority]**

---

## Annex — what would and would not settle each request

| # | Provision | A responsive answer consists of | What would **not** settle it |
|---|---|---|---|
| 1–2 | Art. 51 | Model identity; training compute in FLOP | Descriptions of intended use or release status |
| 3–4 | Art. 52(1) | The notification and its date, or a reasoned Article 52(2)-style basis | "Internal only"; "not placed on the market" |
| 5–6 | Arts. 53(1)(a), 55(1)(a) | The evaluation protocol and documented adversarial-testing record | Public blog descriptions of the evaluation's difficulty |
| 7 | Art. 55(1)(b) | The risk assessment as it addresses **sources**, dated before July 2026 | Post-incident remediation commitments |
| 8 | Art. 55(1)(d) | Egress architecture before 9 July and after the 4 July rebuild | A description of the exploit chain, which is already public |
| 9–10 | Art. 55(1)(c) | Contemporaneous tracking records and a classification date | The public disclosure date, which is not the same thing |
| 11 | Art. 55(1)(c) | Report date, provision relied on, treatment of corrective measures | Confirmation that "a report was filed" without those particulars |
| 12 | Art. 55(2), Code | The Framework and Model Report as they bear on these episodes | The fact of signature to the Code |

## Annex II — provisions relied on

Regulation (EU) 2024/1689, as consolidated to 27 July 2026 (CELEX `02024R1689-20260727`), incorporating Regulation (EU) 2026/1744. Articles 3(49), 3(62), 51, 52, 53(1)(a), 55, 73, 75, 78, 91, 101, 113. Recitals 114 and 115 as published in the authentic Official Journal text (CELEX `32024R1689`); the consolidated text omits recitals and carries the standing caveat that it "is meant purely as a documentation tool and has no legal effect".

Directive (EU) 2022/2557, Article 2, points (1), (4) and (5), as imported by Article 3, point (62) of the Regulation.
