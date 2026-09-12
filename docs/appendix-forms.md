# Appendix: filling the Commission’s serious-incident form from the public record

What a regulator gets, and does not get, when the official template is completed from public sources alone.

This is not new research. Every cell below is a cross-walk row already in `data/crosswalk.yaml`, re-presented in the regulator’s own form rather than in ours. The form is where the gaps become legible: a reader can disagree with an analysis, but a blank required field argues for itself.

---

## 1. The form

*Report for Serious Incidents under the AI Act (General-Purpose AI Models with Systemic Risk)*, published by the Commission on 4 November 2025. Its own opening line states that it “serves as a means to demonstrate compliance with Article 55(1), point (c), of the AI Act as part of Commitment 9 of the Safety and Security Chapter of the General-Purpose AI Code of Practice.”

Ten numbered fields across two pages. Fields 1 to 9 track Measure 9.2 of the Code almost exactly; field 10 has no counterpart there.

The Commission publishes it in two renditions, DOCX and PDF, and both were read for this appendix—the DOCX by unpacking the file and taking its field labels and placeholder prompts as it stores them rather than as a text layer renders them. They are the same form: identical headings, identical prompts, differing only in pagination and in where the number column falls in the reading order. The whole of it comes to 1,884 characters, being a title, one framing sentence, ten headings, ten prompts and six contact sub-fields. That is everything the Commission asks a provider to say about a serious incident involving a model with systemic risk.

---

## 2. The ten fields, filled

**Status key**—**filled**: the record supplies it. **partial**: the record supplies part, or supplies it from a source the form does not contemplate. **cannot fill**: no public source supplies it.

| # | Field, as the template heads it | What the public record gives | From | Status |
|---|---|---|---|---|
| 1 | **Start and end dates of the serious incident** | An intrusion window of 9 July 02:28 UTC to 13 July 14:14 UTC, access cut 13:37 UTC on 13 July. That is the window of detected activity *at the victim*, not of the containment failure: the same record has internet access regained after a service rebuild following a 4 July outage. | T2 forensics; T1 account | **partial** |
| 2 | **Resulting harm** | One core cluster wiped and rebuilt from scratch; credential rotation across all infrastructure tokens; five datasets touched; only operational metadata tied to search queries read; no other customer-facing models, datasets, Spaces or packages affected. | **T2, the affected party** | **filled** |
| 3 | **Chain of events** | Two chained vectors at the victim, a privileged pod with the host filesystem mounted, escape to root on the node; egress on the provider’s side by server-side request forgery against a remote-repository service. | T2; T1 | **filled** |
| 4 | **Model involved** | Two designations, never reconciled: the provider names one model, the independent investigation another, and neither states they are the same. | T1 and T3 conflict | **cannot fill** |
| 5 | **Evidence available** | An independent behavioural investigation exists—conducted under access constraints imposed by the subject, on a model not available to the provider’s own researchers either. | T3, constrained | **partial** |
| 6 | **Serious incident response** | Corrective measures described publicly; credential rotation performed by the victim. | T1; T2 | **partial** |
| 7 | **Recommendation** to the AI Office | Nothing. |—| **cannot fill** |
| 8 | **Root cause analysis** | The nearest thing is that the provider did not enable the safeguards it uses for externally deployed systems, and names them; and that one model’s cyber classifiers were intentionally disabled for the evaluations. That describes mitigations *absent by choice*, which is not a root cause analysis and is arguably a graver disclosure. Inputs, outputs and the analysis itself are not public. | T1; T3 | **partial** |
| 9 | **Patterns in post-market monitoring** | Only the victim’s monitoring is described, and described failing: detection fired but did not raise the alert’s criticality correctly. The provider’s own monitoring is not in the record. | **T2, not the provider** | **cannot fill** |
| 10 | **Submitter information**—provider, authorised representative or other; organisation, contact name, email, phone | No filing is public, so no submitter is. |—| **cannot fill** |

**Two filled, four partial, four cannot fill.**

---

## 3. What the form does not ask, which is the finding

**The template never asks when the provider became aware.** The words “aware”, “awareness”, “deadline” and “timeline” do not appear in it. It asks for the start and end dates of the *incident* (field 1) and for nothing else temporal—no date of awareness, no date of submission.

That is a negative search, so what was searched should be on the record. The corpus is the complete text of both published renditions: the PDF’s text layer, and every text run in the DOCX’s document and glossary parts. “aware”, “awareness”, “deadline”, “timeline”, “undue delay”, “submission” and “days” return zero in both. “date” returns two hits, both inside field 1. Because the DOCX search runs against the labels as the file stores them, the absence belongs to the form and not to an extraction. What it does not cover: instructions carried outside the form, whether on the library page, in the submission channel or in correspondence, have not been searched, and the library page states none.

Measure 9.3 of the same Code runs every one of its periods—two days, five days, ten days, fifteen days—from the date the signatory “become[s] aware of the involvement of their model”. The Commission Opinion describes that Measure as setting out “what ‘without undue delay’ typically requires of reporting timelines”.

So the official form for demonstrating compliance with Article 55(1), point (c) contains no field from which compliance with its own timeliness standard could be computed. A completed report shows what happened and when it happened. It does not show when the provider knew, and therefore does not show whether the report was late. A regulator holding a perfectly completed form still has to ask.

That is not a drafting nicety. Timeliness is the only part of Article 55(1), point (c) with any determinate content, and it arrives entirely through the Code; the form built to evidence the obligation omits the one date the Code’s own clock depends on.

**The only date the form asks for is the one it lets you estimate.** Field 1’s prompt reads “The start and end dates of the serious incident, or best approximations thereof if the precise dates are unclear”. Approximation is right for an intrusion window nobody fully observed. It is not right for the date a provider’s own staff concluded its model was involved, which the provider knows exactly and which the form does not ask for.

**Two of the ten fields are optional in substance.** Fields 6 and 7 open “What, if anything”—what, if anything, the provider intends to do in response; what, if anything, it recommends the AI Office do. A provider that answers “nothing” to both has completed the form.

**The form is granular about who is filing and unstructured about everything else.** Field 10 is the only field broken into labelled sub-fields: capacity, organisation, contact’s first name, last name, email, phone. Fields 1 to 9—dates, harm, chain of events, model, evidence, response, recommendation, root cause, monitoring patterns—are nine free-text boxes. Six labelled boxes for the contact details, one box each for everything a regulator would have to compute from.

**Recommendation.** Add two fields: the date the provider became aware of its model’s involvement, and the date of submission. Both are known to the provider at the moment of filing, neither is burdensome, and together they make the Measure 9.3 periods checkable on the face of the document. This is a one-line change to a two-page form.

---

## 4. What the fill itself shows

**The fillable fields are filled by everyone except the party the form addresses.** Fields 2, 3 and 9 come substantially from the victim’s forensic timeline; field 5 from an investigator working under the subject’s access constraints. The provider’s own disclosures supply framing, an attribution, a list of safeguards it chose not to enable, and corrective measures. They do not supply the incident’s mechanics, the model’s identity, or any root-cause material. A form designed to be completed **by the provider** is, on this record, completable only from sources the provider does not control.

**The field the Act most needs is the one that cannot be filled.** Field 4 is model identity, and every obligation in Chapter V is indexed to a model: whether Article 51’s threshold is met, whether Article 52(1)’s two-week notification ran, what Article 53(1), point (a) documentation covers. Two authoritative accounts name the principal model differently and neither asserts they are the same. That is Request 1 of the instrument, and it is first for this reason.

**A completed form would still not disclose that it was ever filed.** The provider’s account mentions no notification to any authority; no public source gives a filing date or the provision relied on; the Commission’s spokesperson, asked directly, declined to say. Field 10 is blank here for that reason, and the blank is the point.

**The gaps are not evenly distributed.** Everything about what happened *at the victim* is public. Everything about what happened *inside the provider*—the evaluation protocol, the egress architecture before the failure, the risk assessment, the monitoring, the root cause—is not. The form asks for the second category almost exclusively. A report filed “to the best of their knowledge” reads identically whether knowledge is absent or withheld, and the form provides no way to tell the two apart.

**One drafting change between Code and template is worth noting.** Measure 9.2 asks for a description of the *material* available setting out the model’s involvement; the template’s field 5 asks for the *evidence* available. Evidence is the stronger word. On this record the distinction bites: what exists is an investigation conducted under the subject’s own access constraints, which is material, and whether it is evidence of the model’s involvement is precisely what Request 1 is for.

---

## 5. The comparison that sharpens it

California’s regime, analysed in [`comparative-regimes.md`](comparative-regimes.md), runs its 15-day clock from **discovering** a critical safety incident, and its definition expressly includes unauthorised access to or exfiltration of model weights. New York’s runs 72 hours from **a determination**. Article 55(1), point (c) sets no period at all, and the Code supplies one running from **awareness of the model’s involvement**.

Read against this form, the trigger matters more than the period—and the EU form is the one that omits the trigger from its own fields. A clock that starts on the provider’s awareness, evidenced in a form with no field for awareness, is a clock nobody outside can verify has started.

---

## 6. What would change the result

| Field | Request | What would settle it |
|---|---|---|
| 4, model involved | Request 1 | Whether the two designations denote one model, or identification of each and its role |
| 8, root cause and mitigations | Requests 7, 8, 9 | The evaluation protocol, the systemic-risk assessment as it addresses sources, the egress-control architecture before the failure |
| 9, monitoring patterns | Request 10 | The records kept under Article 55(1), point (c) |
| 7, recommendation | Request 11a | The reports submitted under Measure 9.3, or the basis on which none were |
| 1 and 10, dates and submitter | Request 11a | The date the provider became aware of its model’s involvement, and whether a report was submitted |

Nothing here requires model weights, source code, or anything a provider could reasonably refuse on trade-secret grounds—and Article 78, with Article 55(3), covers what is supplied. The instrument asks for documents the Regulation already requires to exist.
