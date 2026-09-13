# The Method
*Abstracted from the worked example, so it can be run on the next incident rather than only this one.*

---

## The claim, and its ceiling

The method answers one question: **does the discloser’s own account, taken on its own terms, resolve this statutory obligation?**

It does not answer what happened. It cannot, and the moment it pretends to, it loses the property that made it worth doing—that it can be built on accounts published by parties with a stake in how those accounts read, without vouching for any of them.

This ceiling is the method. Everything below is machinery for not exceeding it.

## Why an outsider can run this at all

Compliance analysis from public records is ordinary work in other sectors—civil society, journalism, academic audit—and it does not require standing, access, or a practising certificate. What it requires is that the analyst be scrupulous about the difference between *the record does not resolve this* and *this did not happen*, and that the difference be visible to the reader rather than held privately by the author.

## Step 0: Settle scope before anything else

The most expensive error available in this kind of work is to analyse obligations that never attached. It is expensive because everything downstream looks rigorous: the clause-level reasoning can be correct, the citations exact, the evidence properly tiered, and the whole edifice still rests on a regime that does not reach the subject.

This project made that error. It worked a notification duty with a fixed statutory deadline, in detail, against a model that the regulation’s own definition appears to exclude—and did not consult the scope provisions until an adversarial reviewer asked. The scope argument it *did* make rested on a recital, which in EU law cannot derogate from enacting terms.

Before any obligation is analysed, answer three questions from the enacting text:

1. **Does the instrument’s central defined term actually cover the subject?** Exclusions live inside definitions as often as they live in scope articles. Read the definition to its last clause; that is frequently where the carve-out sits.
2. **Is there an operative scope provision?** Find it and read it, rather than inferring scope from the obligations themselves.
3. **Does the duty-bearer definition fit?** A duty binding “providers” does nothing if the subject is not a provider as defined.

And then: where a scope exclusion has an exception, **read the exception’s own defined terms**. An exception drafted for conduct that is *elected* will not reach conduct that merely *occurs*, and that distinction is often the whole case.

Where scope resolves against coverage, the analysis is not over. Look for obligations on a *covered* party that reach the excluded activity by their own wording—a duty to assess risk arising from a phase is not the same as a duty attaching to conduct in that phase, and the first can survive where the second does not.

## Step 0b: Read the regulator’s own guidance before reasoning from the text

This is the lesson that cost most to learn, and it is the one most likely to transfer.

The scope question in the worked example was answered wrongly twice from the enacting text alone. The first attempt never reached the scope provisions. The second reached them, read them carefully, reasoned correctly from what they said, and still landed in the wrong place—because the regulator had already published an operative test that the text does not contain, and the analysis had not looked.

Careful reading does not substitute for checking what the supervising body has said. In an EU context that means, in order:

1. **The enacting text**, from the consolidated version, with amendment markers read.
2. **The recitals**, from the authentic publication, remembering that they interpret and cannot derogate.
3. **The regulator’s guidelines and Q&A.** These often consolidate scattered recitals into a test with conditions and thresholds that appear nowhere in the articles.
4. **Specialist commentary**, which is also how you discover whether your finding is novel—see Step 0c.

**Then hold two things apart.** Non-binding guidance still determines enforcement. The Commission’s guidelines say they are not legally binding and that only the Court may authoritatively interpret the Act, and in the same breath that they represent the interpretation “on which it will base its enforcement action”. Both halves are true and a competent analysis reports both: what the regulator will do, and what a regulated party could still argue.

Where guidance and enacting text diverge, **that divergence is usually the finding**. It tells you where the instrument is doing work its drafters did not write down, which is exactly where a clarifying-language recommendation has purchase.

## Step 0c: Check whether the finding is already in the literature

Before writing that something is unnoticed, search for it. A methodology that claims epistemic discipline cannot afford an unchecked novelty claim, and novelty is the cheapest thing in any paper for a reader to falsify.

In the worked example the scope argument had been published nine months earlier by a specialist writing for a scholarly commentary, reaching the same destination by a different route. Finding that did not weaken the work. It moved the contribution from “here is an unnoticed gap” to “here is where that argument’s weight actually sits, applied to a case that makes it bite”—which is a smaller claim, and a true one.

State plainly what is yours and what is not.

## Step 1: Establish the statutory foundation from primary sources

Explainer sites are a research aid, not a citation. Two failures follow from citing them:

1. **Amendment drift.** An explainer may predate an amending act. Pull the consolidated text and read the change markers directly—EUR-Lex marks amended passages `▼M1` and base text `▼B`. Record amendment status per provision, as `data/provisions.yaml` does.
2. **Lost structure.** Summaries flatten things that carry the argument. In the worked example, the summary of one limb of the serious-incident definition dropped an irreversibility qualifier that appears in one limb and not its neighbour—which turned out to determine which limb the incident actually fell under.

Consolidated texts typically **omit recitals** and carry a notice that they have no legal effect. Take recitals from the authentic publication and say so once in the citation note.

Follow every cross-reference out of the instrument and into whatever it points at. In the worked example a definition resolved into a different directive, where the defined term turned out to be **functional** rather than designation-based—the opposite of what the summary implied, in the direction that mattered.

**Then close the loop mechanically, because the register will drift from the prose.** A statutory register is built early and consulted selectively; the argument goes on acquiring citations for days afterwards, and nothing announces when a sentence starts leaning on a provision nobody verified. Extract every citation from the finished prose and check it against the register. Running this for the first time on a draft that had been through two adversarial reviews produced twenty-three unbacked citations, among them the single provision the scope analysis turns on. `tools/citecheck.py` is the implementation.

Two things it will not do. It cannot tell whether a citation is *apposite*—verified text can still be the wrong provision for the proposition—and it should skip citations belonging to other instruments and spans of bare article numbers, which name a body of provisions rather than a piece of text. Say which exclusions you made and why, because an exclusion is where a checker quietly stops checking.

**Then check the quotations, not just the citations.** A resolving citation beside a wrong sentence is the most durable error available, because every automatic check passes and the prose still misstates what the source says. Hold the documents, extract their text, and verify every quotation against the document it is attributed to. Tolerate what a PDF does to a sentence—hyphenation, quotation marks, footnote numbers extracted inline, an editorial bracket—and nothing else.

Report coverage rather than a pass, and count what cannot be checked. A quotation from a source you hold only as a URL is not a defect and is not verified either, and a tool that conflates those two is telling you a comfortable story. Where something genuinely cannot be checked, write it down with a reason in a file someone reviews. `tools/quotecheck.py` is the implementation; six of this project’s nine recorded errors are the failure it exists to catch.

**Mark how each entry was obtained.** Not every provision will come from the same place; access fails, sources go dark mid-project, and the honest response is a provenance field rather than a uniform-looking register. Where a weaker source is all there is, record what would confirm it, and check whether an authority quotes the same wording—a Commission document reproducing a definition is corroboration a reader can follow.

## Step 2: Build the gating logic before populating anything

Obligations are not independent rows. Some gate others; some are unconditional. Draw the tree first, because it determines which questions are even askable and which incident each belongs to.

The structural insight worth transplanting: **find the obligations that do not depend on the contested classification.** A report staking everything on a disputed threshold inherits the dispute. Obligations that bite regardless—evaluation duties, risk-assessment duties, security duties, documentation duties—produce findings that stand however the contested question resolves. Build those first. They are the ones that cannot be argued away.

Look also for obligations with **determinate deadlines**. Vague standards (“without undue delay”) produce arguable findings; fixed periods (“within two weeks”) produce resolvable ones. A single resolvable question is worth more than several arguable ones, and the resolvable question is often in a neighbouring article rather than the obvious one.

## Step 3: Tier the evidence by relationship, not prestige

| Tier | Relationship to the claim |
|---|---|
| T1 | The party whose conduct is in question, on its own conduct |
| T2 | The affected party’s forensic account |
| T3 | An investigator operating under access constraints imposed by the subject |
| T4 | An independent third party |

A verdict resting only on T1 must read more hedged than one corroborated at T4, and the table should make that visible rather than leaving the reader to work it out.

Tier attaches to the source’s position, not its reputation. **Apply this symmetrically.** Where more than one party’s self-report appears, all sit at T1 and all carry the same reservations. A register that quietly treats one organisation’s self-account as more reliable than another’s has stopped being a method.

T3 deserves particular care: an investigation commissioned or access-scoped by its subject is not independent, however capable the investigators, and its own stated caveats about what it could not see belong in the record alongside its findings.

## Step 4: Split facts from characterisation

Every row records two things separately:

- **Disclosed facts**—counts, dates, mechanics, what the record says occurred
- **The provider’s characterisation**—how the discloser *labelled* those facts

**Verdicts derive from the facts column only.** A characterisation is an interpretation, frequently of the very ambiguity under test; feeding it into a verdict re-derives the provider’s conclusion under new letterhead.

The characterisation column is not discarded. It is analysed separately, and it is often where the sharpest finding lives—a classification choice that determines which statutory pathway engages is itself the phenomenon worth reporting.

## Step 5: Write verdicts in one of three registers, and nothing else

> “On the provider’s own account, this appears **met**, because…”
> “On the provider’s own account, this appears **unmet**, because…”
> “The disclosed record **does not resolve** this; it would require…”

Repetitive on purpose. The repetition is what makes the discipline auditable instead of aspirational, and it is checked mechanically by `tools/validate.py` rather than trusted.

**And keep conclusions of law out of the cell entirely, which is harder than it sounds.** The registers make claims about a disclosed record. Whether the law reaches the facts is a different kind of claim, and it cannot be established by a record at all. A row may say what the record shows about the facts a legal question turns on; the legal question is argued in the analysis and recorded in a field of its own, so a reader can see which of the two they are being offered.

The failure mode is not a verdict that breaks register. It is a verdict that keeps register while carrying a legal conclusion inside it—“this appears met: the obligations attach”—which borrows the record’s authority for an argument the record does not support. This analysis wrote exactly that sentence, kept it through a rebuild, and found it only when the checker was given a blocklist of legal-conclusion formulations to sit alongside its allowlist of openers. An allowlist tells you how a sentence starts. It says nothing about what the sentence goes on to do.

## Step 6: Prove absences rather than asserting them

Any unresolved row carries:

- **what would settle it**—the specific artifact or answer
- **what would not settle it**—the plausible non-answer, named in advance
- **a dated negative-search note**—*“as of [date], no source in [X] states [Y]”*
- **a description of [X]**—which sites, registers and search terms were actually used

The third matters most. Without it, “the record is silent” means only “we did not find it,” and a request that asks for something already public is the fastest way to lose a reader who knows the material. Write these **as you go**; by hour twenty nobody remembers which searches were actually run.

Naming the non-answer in advance is what converts a request from a question into an instrument: it closes the obvious evasion on the face of the document.

**And prefer a refusal to an absence.** “No published source states X” is the weakest form of the point and the one to fall back on when nobody has been asked. If the body that knows was asked and declined to say, that is evidence rather than its lack—a fact about the record, attributable, dated, and far harder to displace than a survey of what you happened not to find. This project had that evidence in its source register for a day before its negative-search notes used it: a Commission spokesperson who declined, on the record, to give the filing date, the provision relied on, or whether the episode qualified. Look for the refusal before you write the absence.

**Name the corpus, or the absence means nothing.** “No published source states X” is a claim about everything ever published and nobody is in a position to make it. What can honestly be said is that a stated set of sources, searched on stated terms on a stated date, did not contain X. The difference is not pedantry: an unbounded absence cannot be checked, cannot be repeated, and cannot be falsified, which puts it outside the register of claims this method permits everywhere else.

This project ran for two days before noticing. Six of its negative-search notes were written as unbounded claims, and the corpus actually searched was never logged, so it cannot now be reconstructed—those notes carry a field saying so rather than a corpus invented after the fact. `tools/validate.py` now refuses a negative-search note without one.

## Step 6b: Enumerate the inferences, and rank them by weakness

Citations resolving and quotations matching say nothing about whether a step follows, and a step that does not follow is the error that survives everything. It survives because prose hides it: an unsound inference reads exactly like a sound one when both are sentences in a paragraph whose conclusion the reader has already accepted.

So enumerate them. Each argumentative step gets an entry: the claim stated so it could be denied, the premises it rests on as ids that must resolve, what it depends on, **what would defeat it**, and how contestable its author believes it is. What can then be checked mechanically is real—dangling premises, missing defeaters, circular dependency, a load-bearing step that appears nowhere in the prose—and what cannot be checked is at least visible.

Two disciplines make this more than bookkeeping. **Name a defeater or drop the claim**: an author who cannot say what would show a step wrong has usually not tested it. And **rank your own steps by weakness, then publish the ranking weakest first**. That feels like handing over the soft point, and it is. The alternative is a reader who attacks the easiest claim rather than the most important one, which is worse for everybody, and an analysis that would rather be attacked well should say where to aim.

## Step 6c: Fill the regulator’s own form, if one exists

Where the regime publishes a reporting template, fill it from the public record before drafting anything. Two things come out of it, and the second was not expected.

The first is a presentation. A cross-walk row is an analysis a reader may disagree with; the same row in the regulator’s own form, with the field left blank, argues for itself. A form completed from public sources shows at a glance which of the regime’s own questions the record can answer and which it cannot, and who the answers come from—which in this project turned out to be everyone except the party the form addresses.

The second is a test of the form. A template encodes what the regulator believes it needs to know. Set it against the obligation it says it evidences, field by field, and ask what the obligation requires that no field captures. Here the answer was the date of awareness: every initial-report period in the Code runs from it, the form has no field for it—because the Code’s own list of contents, which the form transcribes, has none—and so a perfectly completed report cannot show whether the initial report was late. That finding did not come from the analysis. It came from trying to fill the form and running out of boxes.

Two rules make it reliable.

1. **Read every rendition the regulator publishes.** Where a form is issued as both an editable document and a PDF, read the document’s stored field labels rather than a text layer’s rendering of them. Otherwise an absence you report is a property of your extraction rather than of the form, which is the first thing a drafter will say.
2. **Bound the negative search as Step 6 requires.** “The form does not ask X” is a claim about a document you hold, which makes it the cheapest negative search in the method to state properly: the corpus is the form. Then say what was *not* searched—accompanying guidance, the submission channel, correspondence—because a requirement carried outside the form would answer the point.

## Step 7: Let the instrument fall out of the unresolved rows

Every unresolved row is already a question with a settlement condition attached. Drafting the request is then assembly rather than invention.

Two drafting rules earn their place:

1. **Operative voice.** Write the document the authority could send, not a memo recommending they send one. The first is usable with light edits; the second is commentary from outside the machinery.
2. **Follow the instrument’s own required form.** Most information-gathering powers specify what a valid request must contain. Meeting that specification exactly is most of what “usable with light edits” means in practice.

And state plainly, in the instrument, that no finding has been made. A request premised on an unproven conclusion is one a lawyer rejects on sight; a request that asks is one they can act on.

## Step 7b: Keep a corrections log, and publish it

Every correction the method catches goes into a dated log that ships with the work, recording what was wrong, what the text actually says, and what changed as a result.

Two reasons, and the second is the one that matters. It is the honest thing to do. And a method whose entire claim is that it catches its own drift has no way to evidence that claim except by showing the catches—a clean record proves nothing, because it is indistinguishable from a record that was never kept.

The instinct to tidy the log before publication should be resisted. It is the most persuasive artifact the method produces.

## Step 8: Mark provenance so the draft cannot be mistaken for the real thing

An instrument written in operative voice reads like an issued document, because that is the point. Therefore: an unmissable provenance header, no letterhead, no signature block, and **explicit placeholders rather than plausible values** for reference number, date and signatory.

Beyond the obvious reason, this is better craft. An authority adapting the draft wants to see exactly which fields are theirs to complete.

---

## Running this on something else

The structure is regime-agnostic. To apply it to a different instrument or a different incident:

1. Replace `data/provisions.yaml` with the target regime’s provisions, extracted from primary sources with amendment status recorded.
2. Redraw the gate tree—the gating relationships are specific to each regime, and this is the step that cannot be skipped or inherited.
3. Rebuild `data/sources.yaml`, tiering by relationship to the claim.
4. Populate rows, unconditional obligations first.
5. Fill the target regime’s own reporting form, if it publishes one, and record what it does not ask.
6. Run `python3 tools/check.py`. It is regime-agnostic; it checks the discipline, not the law.
7. Draft the instrument from the unresolved rows, in the form the target regime’s own procedural provision specifies.

The checkers are the portable part, and there are five of them behind one command. `validate.py` polices the verdict discipline. `citecheck.py` resolves every citation in the prose against whatever `provisions.yaml` holds. `quotecheck.py` matches every attributed quotation against the documents you hold, and reports coverage rather than pretending to completeness. `infercheck.py` checks that the inference register’s premises resolve, that each step names a defeater and that the graph is acyclic, and `--attack` prints the load-bearing steps weakest first. `housestyle.py` is the only one that knows anything about this project, and even there the checks for a repeated paragraph and for a count that has drifted from the register it describes carry over unchanged.

The law changes; the failure modes—dangling citations, unproven absences, verdicts that drift into assertion, a count nobody rechecked, a cross-reference to something that was never written, a provider’s framing smuggled in as a finding—do not.
