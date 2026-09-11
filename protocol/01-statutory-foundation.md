# Statutory Foundation — verified against primary source
**Provenance**: all text below extracted from the EUR-Lex consolidated text of Regulation (EU) 2024/1689, CELEX `02024R1689-20260727`, consolidation date **27 July 2026** (i.e. incorporating Regulation (EU) 2026/1744, the Digital Omnibus on AI). Extracted 11 September 2026. EUR-Lex consolidated texts mark amended passages with `▼M1` and unamended base text with `▼B`; amendment status below is recorded from those markers, not inferred.

> Citation convention throughout: the Act's own style — "Article 55(1), point (c)"; "Article 3, point (49)(b)".

---

## 1. Amendment status of every provision this project relies on

| Provision | Amended by Omnibus 2026/1744? | Evidence |
|---|---|---|
| Article 3, point (49) — 'serious incident' | **No** | No marker; points (48), (50), (51) intact around it — no renumbering |
| Article 3, point (62) — 'critical infrastructure' | **No** | No marker |
| Article 55 — GPAI systemic-risk obligations | **No** | No marker anywhere in article |
| Article 73 — reporting of serious incidents | **No** | No marker |
| Article 91 — power to request documentation and information | **No** | No marker |
| Article 101 — fines for GPAI model providers | **No** | No marker |
| **Article 75 — market surveillance / AI Office competence** | **YES — `▼M1`** | Title and paragraph 1 rewritten; new paragraphs 1a–1d inserted |
| **Article 113 — entry into force and application** | **YES — `▼M1`** | Points (a), (c), (d) rewritten/inserted; point (b) remains `▼B` |

**Consequence**: the analytical spine (3(49), 55, 91, 101) rests entirely on unamended text. The two amended articles both *strengthen* the argument rather than disturbing it — see §4 and §5.

---

## 2. Article 3, point (49) — 'serious incident' (verbatim, unamended)

> ‘serious incident’ means an incident or malfunctioning of an AI system that directly or indirectly leads to any of the following:
> (a) the death of a person, or serious harm to a person’s health;
> (b) a serious and irreversible disruption of the management or operation of critical infrastructure;
> (c) the infringement of obligations under Union law intended to protect fundamental rights;
> (d) serious harm to property or the environment;

**Textual observations available from the wording alone — each is load-bearing and none appears in the public discussion of these incidents:**

1. **The causal standard is broad**: "directly **or indirectly** leads to". Arguments that the harm was downstream or mediated do not, on the text, defeat the limb.
2. **Only limb (b) carries an irreversibility requirement.** Limb (d) requires "serious harm to property" and nothing more. For an intrusion whose principal consequence was infrastructure damage subsequently repaired, (d) is textually easier to satisfy than (b) — repair defeats (b)'s "irreversible", it does not defeat (d).
3. **Limb (b) is not self-contained** — it depends on the defined term 'critical infrastructure', which is a cross-reference out of the Act entirely (see §3).
4. The limbs are disjunctive ("any of the following") — one suffices.

## 3. Article 3, point (62) — 'critical infrastructure' → the CER Directive (verbatim, unamended)

> **AI Act, Article 3, point (62)**: ‘critical infrastructure’ means critical infrastructure as defined in Article 2, point (4), of Directive (EU) 2022/2557;

Followed through to the CER Directive (Directive (EU) 2022/2557), extracted from EUR-Lex, CELEX `32022L2557`:

> **Art. 2(4)**: ‘critical infrastructure’ means an asset, a facility, equipment, a network or a system, or a part of an asset, a facility, equipment, a network or a system, **which is necessary for the provision of an essential service**;
>
> **Art. 2(5)**: ‘essential service’ means a service which is **crucial for the maintenance of vital societal functions, economic activities, public health and safety, or the environment**;
>
> **Art. 2(1)** *(for contrast — a different term)*: ‘critical entity’ means a public or private entity **which has been identified by a Member State in accordance with Article 6** as belonging to one of the categories set out in the third column of the table in the Annex;

**CORRECTION — recorded rather than silently fixed, because the error is instructive.** An earlier draft of this file asserted that limb (b) "turns on Member State designation". That is wrong, and it is wrong in the direction that would have *understated* the incident. Designation attaches to **'critical entity'** at Art. 2(1). The AI Act cross-refers specifically to Art. 2, **point (4)** — **'critical infrastructure'**, which is defined **functionally**: an asset or system "necessary for the provision of an essential service". No designation is required for something to be critical infrastructure within the meaning the AI Act imports.

**Consequence for the limb (b) analysis:**

1. Limb (b) is **arguable**, not definitionally excluded. The question becomes whether the affected systems are necessary for the provision of a service "crucial for the maintenance of ... economic activities" — which is broad, and for a platform hosting a substantial share of the open model and dataset ecosystem, genuinely contestable in both directions. It is not resolvable on the disclosed record, which makes it an RFI question rather than a verdict.
2. **"Irreversible" is the decisive defeater, not the definition.** Limb (b) requires disruption that is "serious **and** irreversible". Infrastructure that was rebuilt is, on the face of it, not irreversibly disrupted. This is where limb (b) most cleanly fails — and it fails on a word that limb (d) does not contain.
3. This *strengthens* the point in §2: the drafting distributes an irreversibility requirement to the infrastructure limb and withholds it from the property limb, so an intrusion causing repaired infrastructure damage is pushed toward **(d)**, not (b) — by the text's own structure.

## 4. Article 55 — obligations of providers of GPAI models with systemic risk (verbatim, unamended)

> 1. In addition to the obligations listed in Articles 53 and 54, providers of general-purpose AI models with systemic risk shall:
> (a) perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting adversarial testing of the model with a view to identifying and mitigating systemic risks;
> (b) assess and mitigate possible systemic risks at Union level, including their sources, that may stem from the development, the placing on the market, or the use of general-purpose AI models with systemic risk;
> (c) keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents **and possible corrective measures to address them**;
> (d) ensure an adequate level of cybersecurity protection for the general-purpose AI model with systemic risk and the physical infrastructure of the model.
>
> 2. Providers ... may rely on codes of practice within the meaning of Article 56 to demonstrate compliance with the obligations set out in paragraph 1 of this Article, until a harmonised standard is published. ... Providers ... who do not adhere to an approved code of practice or do not comply with a European harmonised standard **shall demonstrate alternative adequate means of compliance for assessment by the Commission**.
>
> 3. Any information or documentation obtained pursuant to this Article, including trade secrets, shall be treated in accordance with the confidentiality obligations set out in Article 78.

**Observations the explainer-site summaries lost:**

- **55(1)(c) is three verbs, not one**: "keep track of, **document**, and report". Tracking and documentation are freestanding obligations — they can be breached even where a reporting decision is defensible, and they generate artifacts that exist regardless of what was reported.
- **55(1)(c) covers corrective measures too**: "and possible corrective measures to address them". A report that describes the incident but not the corrective measures is a separately testable shortfall.
- **55(2) guarantees a requestable artifact either way**: adhere to the Code of Practice, or "demonstrate alternative adequate means of compliance for assessment by the Commission". Whichever branch a provider is on, documentation exists that Article 91 can reach. This is the single most answerable line of request in the whole instrument.
- **55(3) pre-empts the trade-secret objection**: confidentiality is handled by Article 78, not by withholding. A request cannot be refused on trade-secret grounds; it is protected on receipt.

## 4a. Articles 51, 52 and 53 — scope, and the only determinate deadline in the GPAI chapter (verbatim, unamended)

> **Article 51(1)**: A general-purpose AI model shall be classified as a general-purpose AI model with systemic risk if it meets any of the following conditions: (a) it has high impact capabilities evaluated on the basis of appropriate technical tools and methodologies, including indicators and benchmarks; (b) based on a decision of the Commission, ex officio or **following a qualified alert from the scientific panel**, it has capabilities or an impact equivalent to those set out in point (a) ...
>
> **Article 51(2)**: A general-purpose AI model shall be **presumed** to have high impact capabilities pursuant to paragraph 1, point (a), when the cumulative amount of computation used for its training measured in floating point operations is **greater than 10²⁵**.
>
> **Article 52(1)**: Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission **without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met**. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. **If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.**
>
> **Article 53(1)(a)**: Providers of general-purpose AI models shall: draw up and keep up-to-date the technical documentation of the model, **including its training and testing process and the results of its evaluation** ... for the purpose of providing it, **upon request, to the AI Office** and the national competent authorities;

**This is the most consequential find in the statutory pass, for four reasons.**

1. **Article 52(1) contains a hard two-week deadline — the only determinate period anywhere in the GPAI systemic-risk regime.** Article 55(1), point (c) says "without undue delay" and nothing more. Article 52(1) says "without delay and in any event within two weeks". A compliance question asked against Article 52 is therefore *resolvable* in a way that the same question asked against Article 55(1)(c) is not.

2. **The trigger is capability, not market placement** — and it is expressly forward-looking: "after that requirement is met **or it becomes known that it will be met**". The duty can crystallise during development, before any release. Neither Article 51, 52 nor 53 conditions these obligations on placing the model on the market.

3. **This resolves the scope problem raised by the disclosed facts.** OpenAI's own account names the principal actor as **IM1**, an "internal-only research model" that is "not intended for public release", comparable to GPT-5.6 Sol; GPT-5.6 Sol agents played a secondary role ("also reproduced an exploit"). The natural provider argument — that an internal, unreleased model sits outside Chapter V — does not survive Articles 51(2) and 52(1): a frontier model comparable to a deployed systemic-risk model is presumptively over the 10²⁵ FLOP threshold, and the notification duty attaches on capability, during development. **Whether IM1 was notified to the Commission under Article 52(1) is a clean, determinate, single-document question that the public record does not answer.**

4. **The Act supplies its own remedy and its own activation route.** Article 52(1), final sentence: an unnotified model may be designated ex officio. Article 51(1), point (b): designation may follow **a qualified alert from the scientific panel** — the same constituency that can substantiate an Article 91(3) request. Scientific panel qualified alert → designation under 51(1)(b) → Chapter V obligations attach → Article 91 request for the Article 53/55 documentation. That is a coherent institutional pathway that can be recommended in full, with every step cited.

**Practical effect on the report**: this is the crisp, resolvable finding to set alongside the deliberately-unresolved Article 3(49) classification analysis. It does not depend on how the serious-incident question comes out.

## 5. Article 91 — power to request documentation and information (verbatim, unamended)

> 1. The Commission may request the provider of the general-purpose AI model concerned to provide the documentation drawn up by the provider in accordance with Articles 53 and 55, or any additional information that is necessary for the purpose of assessing compliance of the provider with this Regulation.
> 2. Before sending the request for information, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.
> 3. Upon a duly substantiated request from the scientific panel, the Commission may issue a request for information to a provider of a general-purpose AI model, where the access to information is necessary and proportionate for the fulfilment of the tasks of the scientific panel under Article 68(2).
> 4. The request for information shall state the legal basis and the purpose of the request, specify what information is required, set a period within which the information is to be provided, and indicate the fines provided for in Article 101 for supplying incorrect, incomplete or misleading information.
> 5. The provider ... or its representative shall supply the information requested. ... Lawyers duly authorised to act may supply information on behalf of their clients. The clients shall nevertheless remain fully responsible if the information supplied is incomplete, incorrect or misleading.

**The five mandatory elements of a valid request, from 91(4)** — this is the RFI's required structure, not a stylistic choice:
1. legal basis
2. purpose of the request
3. specification of what information is required
4. a period within which it must be provided
5. indication of the Article 101 fines for incorrect, incomplete or misleading information

**Two activation pathways, not one** — this matters for who can realistically move the instrument:
- **91(1)**: Commission/AI Office on its own initiative.
- **91(3)**: on a *duly substantiated request from the scientific panel*, where access is "necessary and proportionate" for the panel's Article 68(2) tasks. This is the route a scientific constituency can substantiate rather than merely petition for. An instrument drafted to satisfy both framings is usable by either.
- **91(2)** structured dialogue is an available precursor — a drafted request should say why a formal request rather than structured dialogue is proportionate here, because a real addressee will ask.

## 6. Article 101 — fines for providers of GPAI models (verbatim, unamended)

> 1. The Commission may impose on providers of general-purpose AI models fines not exceeding 3 % of their annual total worldwide turnover in the preceding financial year or EUR 15 000 000, whichever is higher, when the Commission finds that the provider intentionally or negligently:
> (a) infringed the relevant provisions of this Regulation;
> (b) **failed to comply with a request for a document or for information pursuant to Article 91, or supplied incorrect, incomplete or misleading information;**
> (c) failed to comply with a measure requested under Article 93;
> (d) failed to make available to the Commission access to the general-purpose AI model ... pursuant to Article 92.

**Point (b) is the enforcement teeth behind the instrument**: non-response to an Article 91 request is independently finable, at the same ceiling as the underlying substantive infringement under point (a). The 91(4) requirement to "indicate the fines provided for in Article 101" therefore points specifically at **Article 101(1), point (b)**.

## 7. Article 73 and the Article 75(1a) derogation — why 55, not 73, and what that asymmetry reveals

**Article 73(1) (verbatim, unamended)**: "Providers of **high-risk AI systems** placed on the Union market shall report any serious incident to the market surveillance authorities of the Member States where that incident occurred."

Article 73's deadlines (also unamended): **15 days** ordinary (73(2)); **two days** for a widespread infringement or a serious incident as defined in Article 3, point (49)(b) (73(3)); **immediately** in the event of death (73(4)).

**Article 75(1) and (1a), as amended by the Omnibus (`▼M1`)**:
> 1. The AI Office shall be **exclusively competent** for the supervision and enforcement of the obligations under this Regulation in relation to the following AI systems: (a) AI systems based on general-purpose AI models where the model and the system are developed by the same provider, or by providers forming part of the same undertaking as that provider ... [subject to carve-outs for Annex I products, Annex III point 2, law enforcement/border/financial under Art. 74(6), and Annex III point 8 justice systems]
> 1a. **By way of derogation from Article 73**, providers of high-risk AI systems subject to the competence of the AI Office pursuant to paragraph 1 of this Article shall report any serious incidents **to the AI Office**. Article 73(2) to (9) shall apply mutatis mutandis. ...

**Why Article 73 does not bite here**: the systems at issue were running an internal cyber-capability evaluation. That is not a use case classified as high-risk under Article 6(2)/Annex III or Article 6(1)/Annex I. No high-risk classification, no Article 73 obligation. The live obligation is the **model-level** one at Article 55(1), point (c). *(And independently, Chapter III Sections 1–3 are now deferred to 2 December 2027 / 2 August 2028 by amended Article 113(c) — so even a high-risk framing would not yet be in application.)*

**The asymmetry this exposes — an affirmative finding, not a defensive footnote**: where a GPAI-based system *is* high-risk and built by the same provider as the model, Article 75(1a) routes its serious-incident reports to the AI Office **and imports Article 73's concrete day-counts**. Where only the *model* is in scope, Article 55(1), point (c) supplies the same addressee with **no determinate period at all** — only "without undue delay". The Act already knows how to set incident-reporting deadlines; it simply does not do so on the limb under which the most capable models' own containment failures actually fall. *That is directly responsive to the track's own question — "where the text does not resolve cleanly, what is the clarifying language?" The clarifying language is available by analogy: import the Article 73(2)–(4) tiering into Article 55(1), point (c).*

## 7a. Recitals 114 and 115 — the interpretive aids, and why 115 is the most valuable text in this file

Note on sourcing: the EUR-Lex **consolidated** text carries the standing caveat that it "is meant purely as a documentation tool and has no legal effect"; it also **omits the recitals entirely**. Recitals below are therefore taken from the authentic OJ publication, CELEX `32024R1689`. Citation practice for the report: cite the consolidated text for currency of the enacting terms, the OJ publication as the authentic version, and say so once.

**Recital 114 (extract)** — on Article 55(1), points (a) and (b):
> ... this Regulation should require providers to perform the necessary model evaluations, **in particular prior to its first placing on the market**, including conducting and documenting adversarial testing of models, also, as appropriate, through internal or independent external testing. In addition, providers ... should continuously assess and mitigate systemic risks, including for example by putting in place risk-management policies, such as accountability and governance processes, implementing post-market monitoring, taking appropriate measures **along the entire model's lifecycle** ...

**Recital 115 (extract)** — on Article 55(1), points (c) and (d):
> ... If, despite efforts to identify and prevent risks related to a general-purpose AI model that may present systemic risks, **the development or use of the model causes a serious incident**, the general-purpose AI model provider should without undue delay keep track of the incident and report any relevant information and possible corrective measures to the Commission and national competent authorities. Furthermore, providers should ensure an adequate level of cybersecurity protection for the model and its physical infrastructure, if appropriate, along the entire model lifecycle. Cybersecurity protection related to systemic risks associated with malicious use or attacks should duly consider accidental model leakage, unauthorised releases, **circumvention of safety measures**, and defence against cyberattacks, unauthorised access or model theft. That protection could be facilitated by securing model weights, algorithms, **servers**, and data sets, such as through operational security measures for information security, specific cybersecurity policies, adequate technical and established solutions, and **cyber and physical access controls** ...

**Why this matters, in two moves:**

1. **"The development or use of the model causes a serious incident" forecloses the most natural defence.** The obvious provider answer to a 55(1)(c) enquiry about an incident arising inside an internal pre-deployment evaluation is that the reporting regime is aimed at deployed models and market harms, not at what happens on a test harness. Recital 115 extends the contemplated trigger to **development**, and Recital 114 extends the evaluation obligations to testing "prior to its first placing on the market" and "along the entire model's lifecycle". On the Act's own interpretive material, an incident originating in internal adversarial testing is inside the scope of Article 55, not outside it. This should be stated early in the report, because everything downstream depends on it.

2. **Recital 115 supplies an enumerated checklist for Article 55(1), point (d).** The cybersecurity obligation is not a vague standard to be argued about in the abstract: the recital names what it must "duly consider" — accidental model leakage, unauthorised releases, **circumvention of safety measures**, defence against cyberattacks, unauthorised access, model theft — and what protection "could be facilitated by" — securing weights, algorithms, **servers**, datasets, operational security measures, specific cybersecurity policies, **cyber and physical access controls**. A containment failure in which models circumvented safety measures and escaped a sandbox through its sole permitted network egress can be cross-walked item by item against that list. This converts 55(1)(d) from the weakest-looking row into one of the most textually specific.

## 8. Application dates — derived from Article 113, not from secondary reporting

Article 113 as consolidated:
- Opening: "It shall apply from 2 August 2026." *(general rule)*
- Point (b), **`▼B` (unamended)**: "Chapter III Section 4, **Chapter V**, Chapter VII and Chapter XII and Article 78 shall apply from **2 August 2025**, **with the exception of Article 101**."
- Point (c), `▼M1`: Chapter III Sections 1–3 deferred to **2 December 2027** (Annex III high-risk) and **2 August 2028** (Annex I high-risk).
- Point (d), `▼M1`: Articles 102–110 apply from 27 July 2026.

**Derivation**: Chapter V contains Articles 51–56, so **Article 55 has applied since 2 August 2025**. Article 101 is expressly carved out of point (b)'s early application and appears in no other point — it therefore falls back on the general rule in the opening line: **Article 101 applies from 2 August 2026**. That is the textual basis for "the AI Office's fining power over GPAI providers went live on 2 August 2026", and it is derivable from the Act alone without relying on any commentary.

---

## Outstanding verification
- [ ] CER Directive (EU) 2022/2557, Article 2, point (4) — verbatim, for the limb (b) analysis
- [ ] Whether Hugging Face is a designated critical entity in any Member State
- [ ] GPAI Code of Practice, Commitment 9, and the Commission's serious-incident reporting template (published ~28 October 2025) — verbatim, and whether OpenAI is a Code signatory (determines which branch of Article 55(2) applies)
