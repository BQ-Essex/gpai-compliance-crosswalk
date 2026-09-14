# Statutory foundation, second run

The statutory register is the first run’s, copied by `tools/new-incident.py` and carrying the date of its last verification against the consolidated text. Nothing in it was changed for this run; the provisions relied on are Articles 2(1), point (a), 2(8), 3 points (9), (49) and (63), 51, 55(1) and (2), and Recital 97, all of which were verified there.

## 0. Corrections log

In total, two errors have been found in this analysis, both within one session of the first row being written, and both the first run’s failure: a source characterised without being opened.

| Error | Correction |
|---|---|
| **The fourth incident dated to the wrong month, from a fetch summary of a press report** | The first version of row `g2-art55-1c-timing` said the fourth incident was “discovered in July 2026” and “disclosed on 10 September 2026”, on the strength of a fetch tool’s summary of The Hacker News. The primary, Anthropic’s assessment of 9 September, held two hours later, says it was identified “in August while assembling transcripts to share with METR” and is itself dated 9 September. The awareness date is the one fact the timing question turns on, and it was wrong by a month, from a summary of a secondary. The row now cites the primary. |
| **Five of six sources characterised through a fetch tool’s summary rather than opened** | The first `sources.yaml` held one document and registered five by URL with `establishes:` lines written from what a summarising tool said about each. The first run’s log has fourteen entries for this failure and the method’s first rule forbids it; the run did it anyway under time pressure, and said so in the register. All ten documents are now held, hashed and quoted against. What opening them added is in `docs/run-report.md` §3: the provider’s own revision of its July account, the personal-data fact in the fourth incident, the harness/environment split, the three-provider reach of one evaluator, and a refusal on the record. None of it was in the summaries. |

## 1. Working

The working for this run is short because the first run did it. Three things differ and are set out in `docs/run-report.md`: one model is plainly placed on the market, so the scope question falls away for it; the scaffolding was a third party’s, so the attribution objection arrives at full strength; and the date of awareness is public, so the timing question can be put with a date in it.
