# Appendix: filling the forms from the public record

What a regulator gets, and does not get, when the official serious-incident report is completed from public sources alone.

This is not new research. Every cell below is a cross-walk row already in `data/crosswalk.yaml`, re-presented in the regulator’s own form rather than in ours. The point of the exercise is that the form is where the gaps become legible: a reader can disagree with an analysis, but a blank required field argues for itself.

---

## 1. Which form

Under Article 55(1), point (c), providers of general-purpose AI models with systemic risk must keep track of, document and report relevant information about serious incidents. The Commission published a template for exactly this on 4 November 2025—*Report for Serious Incidents under the AI Act (General-Purpose AI Models with Systemic Risk)*—stating that it “promotes consistent and transparent reporting and helps providers demonstrate compliance with the commitments set out in Commitment 9 of the GPAI Code of Practice”.

The substantive field list is therefore **Measure 9.2 of the Code’s Safety and Security Chapter**, which the Commission’s own publication treats as operationalising the obligation, and which this repository holds and has verified. Measure 9.2 requires nine items, reported “to the best of their knowledge, redacted to the extent necessary to comply with other Union law”.

The exercise below fills those nine from the public record for the July 2026 intrusion.

---

## 2. The nine fields

**Status key**—**filled**: the record supplies it. **partial**: the record supplies part, or supplies it from a source the form does not contemplate. **cannot fill**: no public source supplies it.

| # | Measure 9.2 field | What the public record gives | From | Status |
|---|---|---|---|---|
| 1 | Start and end dates of the incident, or best approximations | An intrusion window of 9 July 02:28 UTC to 13 July 14:14 UTC, with access cut at 13:37 UTC on 13 July. But that is the window of *detected activity at the victim*, not of the containment failure: the same record has internet access regained after a service rebuild following an outage on 4 July. | T2 forensics; T1 account | **partial** |
| 2 | The resulting harm, and the victim or affected group | One core cluster wiped and rebuilt from scratch; credential rotation across all infrastructure tokens; five datasets touched; only operational metadata tied to search queries read; no other customer-facing models, datasets, Spaces or packages affected. | **T2—the affected party** | **filled** |
| 3 | The chain of events that directly or indirectly led to the incident | Two chained vectors at the victim, a privileged pod with the host filesystem mounted and escape to root on the node; egress on the provider’s side by server-side request forgery against a remote-repository service. | T2 forensics; T1 account | **filled** |
| 4 | **The model involved** | Two designations, never reconciled: the provider names one model, the independent investigation names another, and neither states they are the same. | T1 and T3 conflict | **cannot fill** |
| 5 | A description of material available setting out the model’s involvement | An independent behavioural investigation exists—but it was conducted under access constraints imposed by the subject, and the model at issue was not available to the provider’s own researchers either. | T3, constrained | **partial** |
| 6 | What the provider has done or intends to do in response | Corrective measures described publicly; credential rotation performed by the victim. | T1; T2 | **partial** |
| 7 | What the provider recommends the AI Office or national authorities do | Nothing. |—| **cannot fill** |
| 8 | Root cause analysis: the model’s outputs, contributing factors, inputs used, and any failures or circumventions of systemic-risk mitigations | The nearest thing in the record is that the provider did not enable the same safeguards as for externally deployed systems, and names them; and that one model’s cyber classifiers were intentionally disabled for the evaluations. That describes mitigations *absent by choice*, which is not a root cause analysis and is arguably a more serious disclosure. The inputs, the outputs, and the analysis itself are not public. | T1; T3 | **partial** |
| 9 | Patterns from post-market monitoring connected to the incident, including near misses | Only the victim’s monitoring is described, and it is described failing: detection fired but did not raise the alert’s criticality correctly. The provider’s own monitoring is not in the record. | **T2, not the provider** | **cannot fill** |

**Two filled, four partial, three cannot fill.**

---

## 3. What the exercise shows

**The fillable fields are filled by everyone except the party the form is addressed to.** Fields 2, 3 and 9 come substantially from the victim’s forensic timeline; field 5 from an investigator working under the subject’s access constraints. The provider’s own disclosures supply framing, an attribution, a description of absent safeguards, and corrective measures. They do not supply the incident’s mechanics, the model’s identity, or any root-cause material. A form designed to be completed *by the provider* is, on this record, completable only from sources the provider does not control—which inverts the reporting architecture it belongs to.

**The field the Act most needs is the one that cannot be filled.** Field 4 is model identity. Everything in Chapter V is indexed to a model: whether Article 51’s threshold is met, whether Article 52(1)’s notification ran, which documentation Article 53(1)(a) covers. Two authoritative accounts name the principal model differently and neither asserts they are the same. That is Request 1 of the instrument, and it is first for this reason.

**A completed form would not, on this record, disclose that the obligations were engaged.** The provider’s account contains no mention of notification to any regulatory authority. Nothing in the public record states the date of any filing or the provision relied on—and the Commission’s spokesperson, asked directly, declined to say. So the form can be filled in part, and filling it would still not establish whether it was ever filed.

**The gaps are not evenly distributed, and the pattern is legible.** Everything about *what happened at the victim* is public. Everything about *what happened inside the provider*—the evaluation protocol, the egress architecture before the failure, the risk assessment, the monitoring, the root cause—is not. The form asks for the second category almost exclusively. That is the finding a regulator can act on: the reporting architecture presumes a cooperative provider, and where cooperation is partial the form’s own structure makes the shortfall invisible rather than obvious, because a report filed with fields “to the best of their knowledge” reads the same whether knowledge is absent or withheld.

---

## 4. The comparison that sharpens it

California’s regime, analysed in [`comparative-regimes.md`](comparative-regimes.md), runs its 15-day clock from **discovering** a critical safety incident, and its definition expressly includes unauthorised access to or exfiltration of model weights. New York’s runs 72 hours from **a determination**. The EU’s Article 55(1), point (c) sets no period at all, and the Code supplies one running from **awareness of the model’s involvement**.

Read against this form, the trigger matters more than the period. Fields 1 and 4—dates and model identity—are what a trigger attaches to, and they are respectively partial and unfillable from the public record. A clock that starts on the provider’s own awareness, reported in the provider’s own form, on facts only the provider holds, is a clock nobody outside can verify has started.

---

## 5. What would change the result

Each unfilled field maps to a request in [`../instrument/model-article-91-request.md`](../instrument/model-article-91-request.md):

| Field | Request | What would settle it |
|---|---|---|
| 4, model involved | Request 1 | Confirmation whether the two designations denote one model, or identification of each and its role |
| 8, root cause and mitigations | Requests 7, 8, 9 | The evaluation protocol, the systemic-risk assessment as it addresses sources, and the egress-control architecture before the failure |
| 9, monitoring patterns | Request 10 | The records kept under Article 55(1), point (c) |
| 7, recommendations | Request 11a | The reports submitted under Measure 9.3, or the basis on which none were |
| 1, dates | Request 11a | The date the provider became aware of its model’s involvement |

Nothing here requires model weights, source code, or anything a provider could reasonably refuse on trade-secret grounds—and Article 78, with Article 55(3), covers what is supplied. The instrument asks for documents the Regulation already requires to exist.
