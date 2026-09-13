#!/usr/bin/env python3
"""Check the cross-walk against the discipline the method claims to follow.

The method's whole defensibility rests on a limit: it can produce self-consistency
claims about a disclosed record, and it cannot produce claims about what happened.
That limit is easy to state once in a Methods section and easy to lose in a tired
sentence at hour forty. This script is the limit made executable, so that "we
maintained a verdict-register discipline" is something a reader can verify by
running a command rather than something they have to take on trust.

Sole dependency is PyYAML, because hand-rolling a YAML parser to avoid one import
would trade a well-tested dependency for a fragile one.

Usage:
    python3 tools/validate.py              # check, print findings
    python3 tools/validate.py --quiet      # exit code only, for CI

Exit codes:
    0  everything holds
    1  at least one breach of the discipline
"""

import sys
import re
from pathlib import Path

import yaml

# The three permitted verdict openers. Nothing else is allowed to start a verdict.
# Repetitive by design: the repetition is what makes the discipline auditable
# rather than aspirational.
PERMITTED_OPENERS = (
    "On the provider's own account, this appears met",
    "On the provider's own account, this appears unmet",
    "The disclosed record does not resolve this",
)

# A verdict matching this is one that admits it settles nothing, and therefore
# owes the reader both a route to settlement and proof we actually looked.
UNRESOLVED_OPENER = "The disclosed record does not resolve this"

# The openers are an allowlist. This is the matching blocklist, and it guards a
# different failure: a verdict that stays in register while smuggling a
# CONCLUSION OF LAW into a cell whose whole warrant is that it only describes a
# record. Whether obligations attach is a question of law; a row can only say
# what the record establishes about the facts that question turns on. The list is
# explicitly not exhaustive and is not meant to be — it catches the formulations
# this analysis actually reached for, having caught itself using one.
LEGAL_CONCLUSIONS = (
    "the obligations attach",
    "the obligations do not attach",
    "obligations therefore attach",
    "is within scope",
    "is outside scope",
    "falls outside the regulation",
    "is not a general-purpose ai model within the meaning",
    "was infringed",
    "infringed the",
    "is unlawful",
    "is in breach",
)

VALID_TIERS = {"T1", "T2", "T3", "T4"}

DATA = Path(__file__).resolve().parent.parent / "data"


def gather_the_evidence():
    """Load the three data files and hand back their parsed contents.

    Returns a tuple of (provisions, sources, crosswalk) as plain dicts. Any file
    that will not parse stops the run immediately, because every later check
    assumes all three are readable.
    """
    loaded = []
    for name in ("provisions.yaml", "sources.yaml", "crosswalk.yaml"):
        path = DATA / name
        if not path.exists():
            sys.exit(f"Can't find {name} — expected it at {path}. Nothing to check yet.")
        with path.open(encoding="utf-8") as handle:
            loaded.append(yaml.safe_load(handle))
    return tuple(loaded)


def known_identifiers(provisions, sources):
    """Collect the ids a cross-walk row is permitted to point at.

    Returns (provision_ids, recital_ids, source_ids) as sets. Cross-walk rows cite
    provisions and sources by id; anything not in these sets is a dangling
    reference, which in a legal document is the failure mode that matters most.
    """
    provision_ids = {p["id"] for p in provisions.get("provisions", [])}
    recital_ids = {r["id"] for r in provisions.get("recitals", [])}
    source_ids = set(sources.get("sources", {}) and
                     {s["id"] for s in sources.get("sources", [])})
    return provision_ids, recital_ids, source_ids


# Tiers that name an interested party writing about its own conduct, or an
# investigator working under that party's constraints. These must be pinned: the
# analysis claims only to report what a disclosed record says, and a record that can
# be edited after the fact cannot be checked by anyone who reads this later. T4 is
# exempt because an independent source is not the one with a motive to revise.
FIXING_REQUIRED = {"T1", "T2", "T3"}


def is_fixed(entry) -> bool:
    """A source is fixed when a copy of it exists that the register can name: a SHA-256
    of a held file (top-level or under `documents:`) or a Wayback capture."""
    return bool(entry.get("sha256") or entry.get("archived_url")
                or any(d.get("sha256") for d in (entry.get("documents") or []) if isinstance(d, dict)))


def check_the_sources(sources):
    """Confirm every source carries the metadata the tiering depends on.

    A source without a tier can't support a tiered verdict; a source without a date
    can't support a claim about what was known when; a source without a URL can't be
    checked by a reader. And a source at T1, T2 or T3 that is not fixed in place can't
    support anything at all for long: the tiers name interested parties writing about
    their own conduct, and an interested party can edit its own page. Returns a list of
    complaint strings.
    """
    complaints = []
    for entry in sources.get("sources", []):
        sid = entry.get("id", "<unnamed source>")
        tier = entry.get("tier")
        if tier not in VALID_TIERS:
            complaints.append(
                f"[{sid}] tier is {tier!r} — it needs to be one of {sorted(VALID_TIERS)}, "
                f"since the whole point of tiering is that a T1 claim reads differently from a T4 one."
            )
        # The method's first rule, made executable on 13 September 2026 after the second
        # run broke it twice in an hour: a source nobody holds may be registered - by
        # URL, so the next reader can go and hold it - but it may not be said to
        # establish anything. `establishes:` is the register characterising a document,
        # and characterising a document you have not opened is fourteen of the first
        # run's twenty-five errors and both of the second run's first two.
        if not is_fixed(entry) and entry.get("establishes"):
            complaints.append(
                f"[{sid}] is not held or captured, yet the register says it establishes "
                f"{len(entry['establishes'])} thing(s). Hold it (sha256) or capture it "
                f"(archived_url), or move those lines to `would_establish:` until you have."
            )
        # A hash with nothing naming the file it hashes cannot be checked by anyone: a
        # reader has to guess which document in _sources/ it belongs to, and guessing is
        # the thing this register exists to remove. Two entries carried a bare sha256 for
        # a day, both of them Commission acts and one the source of the single most
        # load-bearing quotation in the timing analysis. Both hashes proved correct, which
        # is why this is a documentation check and not an integrity one.
        if entry.get("sha256") and not entry.get("document"):
            complaints.append(
                f"[{sid}] records a sha256 and does not name the file it hashes. Add "
                f"`document:`. A hash a reader cannot attach to a document is not a "
                f"citation, it is a number."
            )
        if tier in FIXING_REQUIRED and not is_fixed(entry):
            complaints.append(
                f"[{sid}] is {tier} and carries no fixed capture. Add archived_url (a "
                f"Wayback timestamp) or sha256 (a local copy). The tier says this is a "
                f"party writing about its own conduct; a verdict drawn from it is only "
                f"checkable for as long as the page stays as it was, and nobody but that "
                f"party decides how long that is."
            )
        if not entry.get("date"):
            complaints.append(f"[{sid}] has no date. Timing claims lean on these.")
        url = entry.get("url", "")
        if not url:
            complaints.append(f"[{sid}] has no URL, so a reader can't check it.")
        elif re.fullmatch(r"https?://[^/]+/?", url):
            # Pinpoint citation discipline: a bare domain sends the reader hunting.
            complaints.append(
                f"[{sid}] cites a bare domain ({url}). A pinpoint link is what lets "
                f"someone verify the specific claim rather than the whole site."
            )
    return complaints


def check_the_verdicts(crosswalk, provision_ids, source_ids, source_entries=None):
    """Check every cross-walk row against the register discipline.

    Enforces, per row: the verdict opens with a permitted opener; the provision it
    cites exists; every source it cites exists; facts are present to derive a verdict
    from; and an unresolved verdict carries both a route to settlement and a
    negative-search note proving the absence was looked for rather than assumed.

    Returns a list of complaint strings.
    """
    complaints = []
    for row in crosswalk.get("rows", []):
        rid = row.get("id", "<unnamed row>")

        verdict = (row.get("verdict") or "").strip()
        if not verdict:
            complaints.append(f"[{rid}] has no verdict at all.")
            continue

        if not verdict.startswith(PERMITTED_OPENERS):
            complaints.append(
                f"[{rid}] verdict opens with {verdict[:60]!r}...\n"
                f"      That's outside the three permitted openers. This is the check that "
                f"matters most — a verdict that drifts into asserting what happened "
                f"retroactively undoes the method it rests on."
            )

        lowered = verdict.lower()
        for formula in LEGAL_CONCLUSIONS:
            if formula in lowered:
                complaints.append(
                    f"[{rid}] verdict contains {formula!r}, which is a conclusion of law.\n"
                    f"      A row says what the disclosed record establishes. Whether the "
                    f"law reaches these facts is argued in the analysis and recorded in "
                    f"the row's conclusion_of_law field, where a reader can see it is "
                    f"reasoning rather than evidence."
                )

        col = (row.get("conclusion_of_law") or "").strip()
        if col and not verdict:
            complaints.append(
                f"[{rid}] states a conclusion of law with no verdict beside it. The two are "
                f"separate claims and the row needs both: what the record establishes, and "
                f"what the law makes of it. A conclusion standing alone reads as a finding."
            )

        provision = row.get("provision")
        if provision and provision not in provision_ids:
            complaints.append(f"[{rid}] points at provision {provision!r}, which isn't in provisions.yaml.")

        # Facts are the only permitted input to a verdict. A row with a verdict but
        # no facts has derived it from something — most likely the characterisation,
        # which is exactly the circularity the split exists to prevent.
        facts = row.get("facts") or []
        if not facts:
            complaints.append(
                f"[{rid}] states a verdict with no facts recorded. Verdicts come from the "
                f"facts column only — if this one came from the characterisation, that's "
                f"the provider's conclusion wearing our letterhead."
            )

        for fact in facts:
            for sid in fact.get("sources", []) or []:
                if sid not in source_ids:
                    complaints.append(f"[{rid}] cites source {sid!r}, which isn't in sources.yaml.")
                elif source_entries and not is_fixed(source_entries[sid]):
                    complaints.append(
                        f"[{rid}] rests a fact on {sid!r}, which nobody holds or captured. A "
                        f"verdict is derived from facts, and a fact from a document not opened "
                        f"is the failure this method exists to stop. Hold it, capture it, or "
                        f"move the claim to the negative-search note as an absence."
                    )

        if verdict.startswith(UNRESOLVED_OPENER):
            if not (row.get("would_settle") or "").strip():
                complaints.append(
                    f"[{rid}] is unresolved but doesn't say what would settle it. "
                    f"An unresolved row without a route to settlement is just a shrug."
                )
            negative = row.get("negative_search") or {}
            if not negative.get("statement"):
                complaints.append(
                    f"[{rid}] is unresolved but has no negative-search note. Without one we're "
                    f"claiming the record is silent when we've only shown we didn't find it."
                )
            elif not negative.get("as_of"):
                complaints.append(
                    f"[{rid}] has a negative-search note with no as-of date. The record moves; "
                    f"an undated absence goes stale without anyone noticing."
                )
            if not negative.get("corpus"):
                complaints.append(
                    f"[{rid}] has a negative-search note with no corpus. \"No published "
                    f"source states X\" is a claim about everything ever published, which "
                    f"nobody can make. Record what was actually searched - which sites, "
                    f"which registers, which terms - so the absence is bounded and "
                    f"someone else can repeat it."
                )
    return complaints


def report_back(complaints, row_count, quiet=False):
    """Print the outcome in a form that's useful to a person, and set the exit code.

    Kept deliberately undramatic: this script exists to catch drift, and drift is
    ordinary rather than shameful.
    """
    if quiet:
        return 1 if complaints else 0

    if not complaints:
        print(f"All {row_count} rows hold to the discipline. Verdict registers intact, "
              f"references resolve, unresolved rows carry their negative-search notes.")
        return 0

    print(f"{len(complaints)} thing(s) to look at across {row_count} rows:\n")
    for complaint in complaints:
        print(f"  - {complaint}")
    print("\nNone of this is fatal — it's the list of places the discipline slipped, "
          "which is exactly what this script is for.")
    return 1


def main():
    """Run every check and exit with a code CI can read."""
    quiet = "--quiet" in sys.argv

    provisions, sources, crosswalk = gather_the_evidence()
    provision_ids, _recital_ids, source_ids = known_identifiers(provisions, sources)

    complaints = check_the_sources(sources)
    entries = {s.get("id"): s for s in sources.get("sources", [])}
    complaints += check_the_verdicts(crosswalk, provision_ids, source_ids, entries)

    row_count = len(crosswalk.get("rows", []))
    sys.exit(report_back(complaints, row_count, quiet=quiet))


if __name__ == "__main__":
    main()
