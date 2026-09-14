# GPAI Compliance Cross-Walk

A method for testing a frontier model provider’s obligations under the EU AI Act against a **public disclosure record**, a worked example, and an **enforcement pack**: a model Article 91 request, an issuing note, an answer matrix, the Commission’s serious-incident template rebuilt with the two fields it lacks, and three amendments to the Regulation in drafted form.

> **Start here, if you have twenty minutes.** Read `instrument/cover-note.md` (one page), then `instrument/model-article-91-request.md` (the deliverable), then `instrument/answer-matrix.md` (what each answer does). Then the report’s §1 to §4 at `docs/report-draft.md`. Everything else is the working behind those four things, and `python3 tools/check.py` is how you check the working without reading it.

---

## The enforcement pack

Everything in `instrument/` is in the form its addressee would issue or adopt, and every word traces to text held and verified here. In reading order:

1. **`cover-note.md`**—one page to the AI Office: what the record establishes, what it does not, the one request that settles it, the one form change that fixes the next incident.
2. **`model-article-91-request.md`**—the request, in Article 91(4)’s required form, issued in the Commission’s name. It asks three facts first: whether the research model was ever integrated into an own AI system put into service; whether it shares a large pre-training run with a model already placed on the market, or was intended for placement; and its training compute. Without those three, Chapter V does not reach the model on the Commission’s own reading.
3. **`issuing-note.md`**—for the AI Office, not the addressee: why each request is asked and what would leave it open. Kept out of the request so the request does not pre-grade answers.
4. **`answer-matrix.md`**—for each answer the provider could give, where it puts the model and what the Commission does next. Every cell is a held provision.
5. **`model-amended-serious-incident-template.docx`**—the Commission’s template of 4 November 2025, every field unchanged, with a date of awareness and a date of submission added in the wording of its own high-risk draft. Without them a completed report cannot show whether it was timely. This is the Commission’s form to change and needs no legislator.
6. **`amendment-table.md`**—three amendments in current-text/amended-text form, every added word traced to the recital, Commission act or provision it is lifted from.
7. **`what-the-provider-will-say.md`**—the load-bearing steps weakest first with the objection against each, rendered from the inference register.
8. **`filled-template.docx`**—the amended template filled from the public record, each field carrying its status.
9. **`docx/`**—every document above as DOCX, because light edits happen in Word. The Markdown is the source of truth and is what the checkers read.

None of it has been issued, adopted or sent. The provenance header on the request says so, and the placeholders are explicit rather than plausible.

---

## Running it yourself

```bash
pip install -r requirements.txt
python3 tools/check.py            # six checks, one command, exit code the worst of them
```

Every tool explains what it checks if you ask it: `python3 tools/<name>.py --help`. Read the last three lines of `check.py`‘s output every time—they say what a clean board does *not* mean.

**On a new incident**, in order:

1. `python3 tools/new-incident.py ../next-incident`—stands up a repository with the checkers, the verified statutory register, the method and empty registers, and runs the checks over it. Then `python3 tools/reverify.py --pdf <consolidated.pdf> --stamp` with a freshly downloaded consolidated text; it finds every register entry in the text layer and dates each one it finds. Its first run here found four extracts that were not verbatim in a register that said they were.
2. **Hold the record before characterising it.** Every document the analysis will cite goes in `_sources/` with its SHA-256 in `data/sources.yaml`. **[`docs/holding-a-source.md`](docs/holding-a-source.md) is the two-minute procedure**, and `tools/hold-source.py` does the half of it a tool can. Twenty of this project’s twenty-nine errors were a source characterised without being opened, and `tools/validate.py` now refuses a fact whose source is not held.
3. **Tier by relationship, not prestige.** T1 the party whose conduct is in question, T2 the affected party’s forensics, T3 an investigator under the subject’s constraints, T4 independent. Two providers’ self-reports sit at the same tier.
4. **Work scope first.** For an internal or research model the three facts in the request are the questions: placement event, Union nexus, systemic risk. `protocol/02-decision-tree.md` and `instrument/answer-matrix.md` are written for that fact pattern generally; only their cells are this incident’s.
5. **One row per obligation**, facts apart from characterisation, the verdict in one of three permitted forms, a `would_settle` and a `would_not_settle`, and a dated, corpus-bounded negative-search note for every absence claimed. `tools/validate.py` will refuse anything else.
6. **Enumerate the inferences** as you go, each with a defeater. `python3 tools/infercheck.py --attack` prints them weakest first, and that list rather than the report is what an adversarial reader should be handed.
7. **Fill the regulator’s form from the record** before writing anything about the form: one entry per field in `data/form-fill.yaml`, then `python3 tools/formfill.py`. That is where the awareness-date finding came from, and it is cheap wherever a regime publishes a template.
8. **Draft the request from the cross-walk.** `python3 tools/draft-request.py` assembles Article 91(4)’s required parts and one request per unresolved row from that row’s own `would_settle`; a person edits from there. `python3 tools/render-pack.py` renders the pack to DOCX.
9. **Log every error** in `protocol/01-statutory-foundation.md` §0 rather than fixing it silently.

A second run exists at `runs/anthropic-cyber-evals-2026/`, stood up by the scaffold and filled in one evening; its run report at `runs/anthropic-cyber-evals-2026/docs/run-report.md` says what transferred, what the change of incident produced, and the two errors the run made in its first hour.

Continuous integration is at `.github/workflows/check.yml`. A green badge there means the citations resolve, the inference register is sound, the verdicts hold their register and no count has drifted—**not** that the quotations are accurate, because `_sources/` is cited by hash rather than redistributed and a clean checkout holds none of it.

---

## Layout

| | |
|---|---|
| `instrument/` | the enforcement pack, above |
| `docs/` | the report, the worked example, the forms appendix, the comparative regimes, the review records, and `holding-a-source.md` |
| `protocol/` | `00-method.md` the method · `01-statutory-foundation.md` the statutory working **and the corrections log** · `02-decision-tree.md` the analytical spine |
| `data/` | `provisions.yaml` 47 provisions, 7 imported CER provisions, 4 recitals, 5 judgments, each verified against the primary text · `sources.yaml` every source, tiered, hashed · `crosswalk.yaml` one row per obligation · `inferences.yaml` every argumentative step with what would defeat it |
| `tools/` | six checkers and six generators; `check.py` runs the checks |
| `runs/` | the same method on a second incident |
| `_sources/` | gitignored. The documents, cited by URL and hash rather than redistributed |

---

## What this is, and what it is not

It **is** a way for an outsider with no access and no practising certificate to say something defensible about whether a law reached a particular thing, and to hand a regulator the document that would settle it.

It is **not** a legal opinion, not a finding that anyone contravened anything, and not an account of what happened. Every claim is about a disclosed record assembled by interested parties. It contains no aggregated exploit detail and no operational security advice: the method’s ceiling is stated in its first line and enforced in code, and advice from a non-practitioner would break it.

**The corrections log is the evidence for all of that.** Twenty-nine errors found during the work, each recorded with what was wrong, what the text actually says, and what changed—fourteen of them the same failure in different clothes. A method whose claim is that it catches its own drift cannot evidence that with a clean record, because a clean record is indistinguishable from one nobody kept. The log is also what told us which checks to write.

---

## Status and licence

Written for the Apart Research / CeSIA AI Incident Response Sprint, regulatory track, September 2026. Bradley Quinlan, University of Essex. The record is live and every negative-search note is dated accordingly; the analysis is contested at the points `docs/report-draft.md` §7 names.

Prose, data and the model instrument are CC BY 4.0; the code is MIT. See `LICENSE` and `CITATION.cff`.
