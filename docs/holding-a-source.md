# Holding a source

Every factual claim in this project cites a document that is **held**: a copy sits in `_sources/`, its SHA-256 is in `data/sources.yaml`, and `tools/validate.py` refuses to let the register say a source establishes anything until it is. This is the one step that is partly manual, so it is written out.

It takes about two minutes per document.

---

## The five steps

**1. Archive the page first.** Open [web.archive.org/save](https://web.archive.org/save), paste the URL, wait for the capture. Do this *before* anything else.

**2. Open the archived copy, not the live page.** The capture has a timestamped URL—`web.archive.org/web/20260912161640/https://…`. That URL is what goes in the register as `archived_url`.

> Why this order, and it is not fussiness: a page revised in place after you quote it is a page your quotation no longer matches, and nobody can tell whether you misquoted it or the publisher edited it. Two entries in the corrections log started exactly there. A capture fixes the page at a moment you can name.

**3. Print the archived copy to PDF, into `_sources/`.** Cmd-P → Save as PDF. The filename does not matter—the tools read the hash, not the name. Do not rename it afterwards to something tidier: eight register entries once named files that had been tidied into fiction, and a reader following the register could not find any of them.

**4. Draft the entry.**

```bash
python3 tools/hold-source.py --draft "your-file.pdf"
```

That prints a `data/sources.yaml` entry with the filename, the hash and today’s date already filled in. Paste it into `data/sources.yaml`, then fill in the four fields it cannot know: `id`, `tier`, `date` (the date the *document* bears), `url` and `archived_url`.

**5. Say what it establishes—and only after reading it.**

`establishes:` is the register characterising the document. It is the only part no tool can write, and it is where this project has gone wrong most often: **twenty of twenty-eight recorded errors were a source described without being opened.** Quote the document’s own words where the words matter.

Then:

```bash
python3 tools/hold-source.py --text     # cache the text layer so quotecheck can read it
python3 tools/check.py                  # all six checks
```

---

## Choosing the tier

The tier is about the source’s **relationship to the claim**, not its prestige. A company’s own account is the best possible source for what that company admits, and a weak one for anything else.

| | |
|---|---|
| **T1** | the party whose conduct is in question, writing about its own conduct |
| **T2** | the affected party’s own forensics |
| **T3** | an investigator working under access constraints the subject set |
| **T4** | independent of both |

T1, T2 and T3 must carry `archived_url` as well as a hash—those are the parties with a reason to revise, and a claim drawn from an editable page is only checkable while the page stays as it was.

---

## Checking what you already hold

```bash
python3 tools/hold-source.py
```

Reports three things, and only the first two are failures:

- **registered and missing**—a citation a reader cannot follow;
- **registered and hashes differently**—the document changed under a claim made about it, which is the reason hashes are recorded at all. Re-read it before touching the hash; the quotation may no longer be in it;
- **present and unregistered**—untidy rather than wrong. A file waiting for an entry.

This runs as the first of the six checks in `tools/check.py`, before anything that reads those documents.

---

## When the page will not archive

Some pages refuse the Wayback Machine, sit behind a subscription, or block automated retrieval. Then:

- Print the **live** page to PDF, and record `retrieved:` with the date and time you printed it.
- Say so in the entry. `provenance: reproduction` with a `provenance_note` is the shape used for California’s statute, which was read in a published reproduction because the Legislature’s own site disallows automated retrieval, and for the newsletter that relays Euractiv rather than being Euractiv.
- Record **what would settle it**—the primary document, read by hand.

An unverified source recorded honestly is worth more than a verified-looking one that quietly is not.
