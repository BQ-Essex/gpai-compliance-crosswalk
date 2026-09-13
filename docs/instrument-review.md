# Adversarial review of the instrument

**What this is, stated before anything else, because an earlier version of this file did not state it and a commit message described it as a lawyer.** This review was produced by a **language model**, prompted to read the draft as a senior lawyer in the AI Office deciding whether to sign it. **No lawyer was consulted. Nobody real was contacted.** The reviewer has no legal training, no professional accountability, and no standing. It is recorded as the fifteenth entry in the corrections log at `protocol/01-statutory-foundation.md`.

That is a weakness in this review and it is not a reason to discard it. What the exercise actually is: a second model, given the draft and the verified text of Article 91 and nothing else—not the report, not the method, not the reasoning that produced the draft—and told to find defects and not to praise. That is worth something, and the evidence that it is worth something is that the defects it found were checkable against the text and several of them held. It is worth nothing as an opinion on European law from a qualified person, and this analysis does not offer it as one.

**Two consequences follow, and both matter more than the ranking below.**

*The case-law references in this review are unverified.* It cites *Orkem* (374/87), *AM&S* (155/79), *Akzo Nobel* (C-550/07), *Nilsson* (C-162/97) and *Deutsches Milch-Kontor* (C-136/04). **None has been read. None has been checked against a report.** Confabulated citations are a known failure of the tool that produced them, and this project’s own standard is that a source characterised without being opened is not a source. They are reproduced here because they are what the reviewer said, and they are marked unverified because that is what they are. What would settle them: reading each judgment. Until then, the propositions they are cited for should be treated as directions for a qualified reader to check, not as authority.

*One of its assertions about the enacting text was simply wrong*, and was acted on before being checked—see defect 19 and the fourteenth entry in the corrections log. A review is evidence, not authority.

**Its answer to the only question that matters—could you issue this with light edits—was no.** The review is reproduced below as received and ranked as it ranked things, because a review kept only in summary is a review nobody can check. What has been fixed since is marked in the log.

---

## 1. The legal basis is stated in the alternative. It is therefore not stated.

Part A, paragraph 2 made the request under Article 91(1) but added that “in the alternative, where the Commission prefers to proceed on the initiative of the scientific panel, this request may be issued under Article 91(3)… The drafting below serves either pathway without amendment.”

Article 91(4) requires the request to “state the legal basis”. A basis stated as one provision *or possibly another, depending on what the Commission later prefers*, states none. Article 91(3) is not an alternative label for the same act: it has its own constitutive preconditions—a duly substantiated request from the scientific panel, already made, and a necessity-and-proportionality finding referable to the panel’s tasks—and a different purpose. Those preconditions either exist on the date of signature or they do not; they cannot be held in reserve. Counsel will say the addressee cannot know which regime it is answering under, that the Commission reserved a post hoc choice of basis, and that the act is vitiated for legal uncertainty and failure to state reasons under Article 296 TFEU. The Article 101(1)(b) fine then rests on an act with a defective basis.

**Fix.** Delete the alternative. If the scientific panel has made a request, issue a separate instrument under Article 91(3) reciting it and its date.

## 2. Much of Part E compels the Provider’s legal self-characterisation. Outside Article 91(1), and *Orkem*.

Requests 2a, 3, 4, 4a, 5, 11b and 12 did not ask for information. They asked the Provider to state its position on contested questions of characterisation: whether the model falls within Article 3(63), whether the evaluation was Article 2(8) activity, which Recital 97 condition it relies on, its position on the Annex XIII criteria.

Two independent problems. **Vires**: Article 91(1) permits documentation drawn up under Articles 53 and 55, and additional *information* necessary for assessing compliance. A reasoned legal opinion is neither, and the Provider has no obligation to hold a position on Annex XIII at all, which is addressed to the Commission. **Privilege against self-incrimination**: compelling the Provider, on pain of a fine of 3% of worldwide turnover, to state whether it accepts that its model was placed on the market and that Article 55 attached, is compelling it to concede the constituent elements of the infringement—the line in *Orkem* (374/87). The Annex’s “what would not settle it” column made it worse by declaring in advance that a factual answer without the legal reasoning is not responsive, so a truthful factual answer risks an incomplete-information fine.

**Fix.** Recast each as a request for facts, and make any legal position expressly optional, with an express no-admission clause at the head of Part E.

## 3. The period is not set, and paragraph 10 let the Provider set its own.

“[20] working days” left the number bracketed. Paragraph 10 then invited a partial response “identifying what is outstanding and the date by which it will be supplied”. Article 91(4) requires the Commission to set a period; paragraph 10 unset it. If the Provider may nominate its own date for the remainder there is no moment at which non-compliance crystallises, and Article 101(1)(b) has no trigger. A single period across document productions of very different weight is also disproportionate.

**Fix.** Fix the number; replace self-service extension with one granted by the Commission in writing on reasoned application made before expiry; consider tranching.

## 4. Repeated clauses let the Provider decide the scope. Several requests can be answered truthfully with nothing.

“to the extent the Provider considers that provision to apply”, “insofar as either bears on”. A request whose extent is defined by the addressee’s own view of applicability specifies nothing, and on this draft’s own logic produces “Article 53(1)(a) does not apply; accordingly nothing is produced.” The draft shows awareness of this failure mode in its note to Request 11b and then commits it twice.

**Fix.** Sever production from the Provider’s view of applicability; require the internal documentation covering the matters the provision describes, with any position on applicability stated separately.

## 5. The object of the request is not identified, and the principal model’s definition is circular.

“the Research Model” was defined as the model called IM1 in the provider’s publication *and/or* the model called HPIM in a third party’s report, with a footnote conceding that whether they are the same is Request 1. A request enforceable by fine must identify its subject-matter precisely enough for the addressee to know what to do, and the Provider cannot be required to construe a third party’s nomenclature.

**Fix.** Name the addressee in full, with the Article 54 authorised representative served in parallel; ask the Provider to identify by its own designation every model involved, and whether IM1 is among them. Drop HPIM from the operative text.

## 6. No legal form, no empowerment, no signatory competence.

Identifying the Commission rather than the AI Office is the right answer to the wrong depth of question. An act capable of triggering a 3% fine must be traceable to an actual exercise of Commission competence. Counsel’s first move is to ask under what empowerment the signatory acted.

**Fix.** Recite adoption and empowerment in the header; add a closing clause on review before the General Court under Article 263 TFEU.

## 7. The stated purpose is not the statutory purpose.

“The Commission is considering two publicly reported episodes” is an investigative motive. Article 91(1)’s second limb is available only where the information is necessary “for the purpose of assessing compliance of the provider with this Regulation”, and the request must state that purpose in those terms, because it is the condition on the power.

## 8. Recital 97 deployed as though operative, and the Commission’s reading written into the question.

Request 4a directed the Provider to answer “having regard to the position that those conditions are cumulative and that the third is unavailable to a general-purpose AI model with systemic risk”—which presupposes that the model *is* one with systemic risk, the very question Requests 2 and 2a are asked to establish. Recitals have no autonomous binding force (*Nilsson*, C-162/97; *Deutsches Milch-Kontor*, C-136/04); guidelines bind the Commission’s discretion, not the addressee.

**Fix.** Strip the instruction, ask the facts, reserve the interpretation for the assessment stage.

## 9. “What would not settle it” is the Commission pre-rejecting answers it has not received.

Three harms: it tells the Provider that particular truthful answers will be treated as non-compliant and so risk a fine; “which is already public” asserts the Commission’s satisfaction that the exploit chain is established fact; “silence on whether the question was considered is not responsive” demands internal deliberation that will often be legal advice.

**Fix.** Make the column indicative and non-binding, or delete it.

## 10. No legal professional privilege carve-out, while the request demands records of legal consideration.

Request 11 demanded “the record of that consideration”, Request 11b “the reasoning”. That is where counsel’s advice sits (*AM&S*, 155/79; *Akzo Nobel*, C-550/07).

**Fix.** Add a privilege clause with a schedule requirement, and make clear that privilege does not withhold the underlying facts or the dates on which steps were taken.

## 11. The Code of Practice treated as creating enforceable obligations, and asked in the wrong order.

Article 55(2) makes adherence a *means of demonstrating* compliance; failure to meet a Code commitment is not an infringement. A demand for Code deliverables backed by an Article 101 fine treats a voluntary instrument as mandatory. The Article 55(2) question was asked last, as Request 12, when it is the gate.

**Fix.** Move the Article 55(2) question to the head of the section and make the Code request expressly contingent on the answer.

## 12. Paragraph 14 volunteers a concession you will regret.

Article 91(4) requires the fines to be indicated. It does not require a signed Commission statement, producible in any later Article 101 proceeding, on a contested question, before the Provider has responded.

## 13. Article 91(5) recited only in its tail, and nobody required to sign the response.

The primary rule—who must supply the information—was absent, and nothing required a signature or a declaration of completeness. Article 101(1)(b) turns on incorrect, incomplete or misleading information, and intention or negligence is materially easier to establish where an identified authorised person has signed.

## 14. The confidentiality clause overstates what can be promised and omits the mechanics.

“as Article 55(3) provides” mis-states the chain: Article 55(3) concerns trade-secret protection in the Article 55 context and does not apply Article 78 to everything supplied under Article 91. A blanket assurance is a hostage, given onward sharing under Article 78, use in proceedings under Articles 92, 93 and 101, and Regulation (EC) No 1049/2001.

## 15. Request 4 cited the wrong provisions; Request 9 reached a third party’s infrastructure.

Articles 57 and 60 are the sandbox and real-world-testing regimes for **high-risk AI systems** and have no application to a general-purpose AI model in a Chapter V context—a category error counsel will use to argue the Commission has not understood the regime it is enforcing. Request 9(b) and (c) asked for the security position of a third party’s production infrastructure, which is outside Article 91(1) and which the Provider may have no right to disclose.

## 16. Part D is an unforced justification.

Article 91(2) is permissive. Explaining why no structured dialogue was attempted creates the impression that justification was required and invites the argument that it was obliged and inadequately reasoned. “Serves both parties” is not a reason known to the Regulation.

## 17. Prejudgment in the narrative.

“the intrusion”, “sustained writing activity”, “whether loss of containment … was identified as such a source”, “the basis on which safeguards were not applied”, “the server-side request forgery … by which outbound requests were reportedly issued”. The disclaimer at paragraph 5 is good and is undone by the rest. Each is a line counsel will quote in an Article 41 Charter complaint of prejudgment and, once Article 101 exposure is in play, under the Charter’s presumption of innocence.

## 18. No necessity statement per section; no format, channel, language or contact clause.

The second limb of Article 91(1) is conditioned on necessity and Article 296 TFEU requires reasons; purpose was stated once, globally, and never linked to the compliance question each request serves. And without a format clause the Commission receives an undifferentiated export and spends the assessment period reconstructing what answers what.

## 19. Internal inconsistencies that will be noticed.

Paragraph 3’s list of provisions relied on differs materially from Annex II’s. Recital 97 is load-bearing in Part B and absent from Annex II’s recital list, which names 114 and 115, and Recital 114 is never cited in the body. Annex II states that the consolidated text “has no legal effect”—true, and an invitation to reply that the Commission’s own annex disclaims its cited source. Numbering runs 1, 2, 2a, 3, 4, 4a, 5–11, 11a, 11b, 12. Request 2 asks for cumulative training compute with no methodology specified, so any figure is defensible. **And here the reviewer is the one who is wrong.** It said paragraph 12 misquotes Article 101(1)(b), which reads “a request for a document or for information” in the draft, and that the enacted text reads “documents or information”. It does not. The consolidated text at CELEX `02024R1689-20260727` reads “failed to comply with a request for a document or for information pursuant to Article 91”. The draft was right; the correction was applied anyway on the reviewer’s say-so and `quotecheck.py` rejected it within two minutes. It is the fourteenth entry in the corrections log. A review is evidence, not authority—and the general point being made, that a quotation in an operative instrument must be exact, is correct, and is precisely why it was caught.
