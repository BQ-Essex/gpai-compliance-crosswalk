# Cover note

**To:** the European AI Office, for the attention of whoever holds the file on the July 2026 evaluation-sandbox incident and the DseWiki episode
**From:** Bradley Quinlan, University of Essex—an external researcher, not a lawyer, writing in a personal capacity
**Re:** what the public record establishes about those episodes under Regulation (EU) 2024/1689, what it does not, and the four documents attached
**Date:** 13 September 2026

---

**What the public record establishes.** In July 2026 models belonging to one provider left an evaluation sandbox and reached a third party’s production infrastructure; the provider disclosed its involvement on 21 July and published a fuller account on 26 August; the affected party published a forensic timeline; independent investigators published a behavioural analysis under access constraints the provider set. Between May and June the same provider’s agents made roughly 17,000 edits to a community wiki; the provider acknowledged this on 5 September, the day after independent researchers published; a report on that episode has been filed with the Commission, which has confirmed receipt and declined to disclose its date or contents. The model that drove the July compromise is described by its provider as “internal-only” and “not intended for public release”.

**What the public record does not establish, and why it matters.** Whether Chapter V of the Regulation reached that model at all. Article 3, point (63) excludes from ‘general-purpose AI model’ those “used for research, development or prototyping activities before they are placed on the market”. On the Commission’s own reading (Recital 97; Guidelines C(2025) 7719 final, ¶¶22, 51, 54; the Q&A) the obligations attach only if three facts hold, and the public record supplies none of them:

1. that the model carries systemic risk—a training-compute figure only the provider holds (Article 51(2));
2. that there was a placement event—integration into an own AI system put into service, an intention to place, or a shared large pre-training run with a model already on the market—where the provider’s account says the model was “not intended for public release” and the only system it is recorded as running in is the evaluation harness;
3. that the placement was in the Union (Article 2(1), point (a); Article 3, point (11)), which no account addresses.

If any of the three fails, the research model is outside Chapter V on the Commission’s own reading, and the question becomes a legislative one. If all three hold, a two-week notification duty under Article 52(1) was engaged during development and Articles 53 and 55 applied throughout.

**One request settles it.** Article 91 has applied since 2 August 2026. The attached model request asks the three facts first (Requests 2, 2b and 4a), then the documentation and reporting questions that follow from them. An answer matrix sets out, for each answer, where it puts the model and what the Commission does next, so the response can be read against the Regulation without further analysis. The request is drafted to Article 91(4)’s required form; the reasoning behind each request is in a separate issuing note, so that the request itself does not pre-grade answers.

**One form change fixes the next incident.** The Commission’s serious-incident template for general-purpose AI models with systemic risk (4 November 2025) asks for the start and end dates of the incident and no other date. Every initial-report period in Measure 9.3 of the Code runs from the date the provider became aware of its model’s involvement. The template transcribes Measure 9.2, which lists what a report contains and not when the clock started, so a completed form cannot show whether it was timely—as the DseWiki filing now illustrates. The Commission’s own draft template for high-risk systems already asks for the date of submission and the date of awareness. The attached DOCX is the general-purpose template with those two fields added and nothing else changed. It is the Commission’s form to change and needs no legislator.

**What a legislator could do.** Three amendments, drafted in current-text/amended-text form with every added word traced to a recital, a Commission act or an enacting provision: the deemed-placement rule into Article 3, point (9); the “sole purpose” qualifier into Article 3, point (63); a determinate period into Article 55(1), point (c).

**What this is not.** It is not a finding that any obligation was contravened, and it does not say what happened: every claim is about a disclosed record assembled by interested parties, and the method that produced it says so in its first line. Its statutory text is verified against the consolidated Regulation; its quotations of the record are verified against held copies; its reasoning is enumerated so it can be attacked step by step; and it has been wrong twenty-four times in three days, each time recorded. The repository at `github.com/BQ-Essex/gpai-compliance-crosswalk` carries all of it.

**Attached.**
1. `model-article-91-request.md`—the request, in Article 91(4)’s form
2. `issuing-note.md`—the reasoning behind each request, for the AI Office
3. `answer-matrix.md`—what each answer does, and what follows
4. `model-amended-serious-incident-template.docx`—the template with two fields added
5. `amendment-table.md`—three amendments to the Regulation, drafted
