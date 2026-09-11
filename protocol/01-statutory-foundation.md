# Statutory Foundation: verified against primary source

**Provenance**: extracted from the EUR-Lex consolidated text of Regulation (EU) 2024/1689, CELEX `02024R1689-20260727`, consolidation date **27 July 2026** (incorporating Regulation (EU) 2026/1744, the Digital Omnibus on AI). Recitals are absent from the consolidated version and come from the authentic Official Journal text, CELEX `32024R1689`. Extracted 11 September 2026; scope provisions re-extracted and corrected the same day following adversarial review.

`amended_by_omnibus` is read from the EUR-Lex change markers (`▼M1` amended, `▼B` base), not inferred from commentary.

> Citation convention: the Act’s own—“Article 55(1), point (c)”; “Article 3, point (49)(b)”.

---

## 0. Corrections log

Three errors were found by adversarial review of the finished draft and are recorded rather than silently fixed.

| Error | Correction |
|---|---|
| Article 73(4) recorded as “immediately” for incidents involving death | **“not later than 10 days”**. Tiering is 15 days / two days / 10 days, with “immediately” as the floor in each, not the limit |
| “Critical infrastructure” said to turn on Member State designation | Designation attaches to **‘critical entity’** (CER Art. 2(1)). The Act imports Art. 2(**4**), which is **functional** |
| **Scope treated as settled; Articles 2(8), 3(3) and 3(63) never consulted** | See §1. The research/development exclusion is inside the definition of ‘general-purpose AI model’ itself, and it changes which obligations can attach at all |

---

## 1. Scope: the threshold question, and the one the analysis must answer first

### 1.1 Article 3, point (63): the exclusion is inside the defined term

> ‘general-purpose AI model’ means an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks regardless of the way the model is placed on the market and that can be integrated into a variety of downstream systems or applications, **except AI models that are used for research, development or prototyping activities before they are placed on the market**;

A model used for research, development or prototyping before market placement is **not a ‘general-purpose AI model’ within the meaning of the Regulation**. Not exempted from particular obligations—outside the term on which the whole of Chapter V operates. Articles 51, 52, 53 and 55 cannot attach to it, and Article 91 cannot reach its documentation.

### 1.2 Article 2(8): the operative scope exclusion, and its one way back in

> This Regulation does not apply to any research, testing or development activity regarding AI systems or AI models **prior to their being placed on the market or put into service**. Such activities shall be conducted in accordance with applicable Union law. **Testing in real world conditions shall not be covered by that exclusion.**

The final sentence is the only route back into the Regulation for anything occurring at the development stage. It is a defined term.

### 1.3 Article 3, point (57): and why the route back does not open

> ‘testing in real-world conditions’ means the **temporary** testing of an **AI system** **for its intended purpose** in real-world conditions **outside a laboratory or otherwise simulated environment**, with a view to gathering reliable and robust data and to assessing and verifying the conformity of the AI system with the requirements of this Regulation, and it does not qualify as placing the AI system on the market or putting it into service within the meaning of this Regulation, provided that all the conditions laid down in Article 57 or 60 are fulfilled;

Every element describes a **deliberate, conditioned, elected** activity: temporary, for the system’s intended purpose, conducted outside a laboratory by design, subject to the conditions in Articles 57 or 60.

**A model that reaches the real world by escaping a simulated environment satisfies none of it.** The escape was not temporary testing, not for an intended purpose, and not a modality anyone elected. The exception is drafted for exposure that is *chosen*; it does not reach exposure that *occurs*.

### 1.4 Article 3, point (3): ‘provider’ is tied to market placement

> ‘provider’ means a natural or legal person, public authority, agency or other body that develops an AI system or a general-purpose AI model or that has [one] developed **and places it on the market** or puts the AI system into service under its own name or trademark, whether for payment or free of charge;

Article 52(1) binds “the relevant **provider**”. The *temporal trigger* in Article 52(1) is capability (“or it becomes known that it will be met”); **standing** is not. A developer may not be a provider of a model it never places on the market.

### 1.5 The gap this produces

Read together, Articles 2(8), 3(63) and 3(3) mean the Regulation assumes a model is either:

- in pre-market research and development, and **excluded**; or
- placed on the market, and **covered**;

and assumes real-world exposure arises only through **deliberate** testing in real-world conditions under Articles 57 or 60.

**A model that reaches third-party production infrastructure by escaping containment during excluded development activity occupies a category the Regulation does not contemplate.** It is not in the market-facing regime, and the exception that would pull development-stage activity back in is drafted for elected exposure.

### 1.6 What survives, and it is the right hook

**Article 55(1), point (b)** obliges providers of marketed systemic-risk models to assess and mitigate systemic risks at Union level, including their sources, “that may stem from **the development**, the placing on the market, or the use” of such models. **“Development” is in the enacting text, not a recital.**

So: the development *activity* is outside the Regulation by Article 2(8); the duty to assess systemic risk *stemming from* development is inside it by Article 55(1)(b), for any provider of a marketed systemic-risk model. A containment failure during internal evaluation is therefore not reachable as an *incident*, but is squarely relevant as a **risk source** the provider was obliged to have assessed.

### 1.7 A bridging problem to state rather than paper over

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
> **CER Art. 2(1)** *(different term, for contrast)*: ‘critical entity’ means an entity **identified by a Member State in accordance with Article 6** …

The imported term is **functional**; designation attaches to ‘critical entity’. But the functional test is not at large either: CER Article 5 requires Member States to identify essential services within the Annex sectors, where “digital infrastructure” covers IXPs, DNS and TLD registries, cloud providers, data centres, CDNs and trust services. **And Article 3(49)(b) requires disruption of “the management or operation of” that infrastructure**, which is a further step. Limb (b) is arguable, not comfortable, and fails independently on “irreversible” where the affected systems were rebuilt.

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

## 6. Article 101, point (b): fines (unamended)

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
