# BRIEF — WAVE-2 PANEL RECONCILE SLOTS (post quota-kill #5 relaunch)
# Cause of record: the 2026-08-19 session limit killed all three
# wave-2 panels AFTER they wrote on-disk files but BEFORE returning
# (checkpoint QUOTA KILL #5 block). Those files are UNVERIFIED
# partials (null=failure) — salvage follows the RECONCILE pattern of
# record (the revise-doc2/3-r2 precedent): verify + complete, never
# duplicate, never trust. BASE = validation/sfoundations_raws_2026-08-13.

## RECONCILE PANEL (one per cluster; your cluster in your task prompt)
On-disk partials (mtimes ~12:55-13:05, sizes at kill):
PANEL_C31TRIO.md ~15k (likely PARTIAL), PANEL_C1REP.md ~15k (likely
PARTIAL), PANEL_C2021.md ~48k (possibly near-complete).

ORDERS:
1. Read YOUR cluster's mandate IN FULL first:
   `BASE/blocco3/BRIEF_wave2_panels.md` §0 (by reference: wave-1 §0),
   §0-bis, §0-ter (ALL binding) + your cluster section, and
   `BASE/blocco3/VERDICT_wave1.md` for the wave-1 dependencies.
2. Read YOUR on-disk partial `BASE/blocco3/PANEL_<cluster>.md` as
   UNVERIFIED DRAFT INPUT — not as record. For every section present:
   VERIFY it against the mandate (citations spot-checked at the
   source; census claims at their stated read-depth; §0-ter query
   protocol / pre-registered criteria / materiality / steelman /
   axis-bearing present and honest). Keep what verifies; REPAIR what
   does not (declare each repair); COMPLETE what is missing.
3. Rewrite the file COMPLETE (same path, same output schema as the
   panels brief) and APPEND a `## RECONCILIATION DECLARATION` section:
   what was on disk (sections present at read time), what verified
   clean, what was repaired (per item), what was added; the partial's
   unverified status is thereby DISCHARGED for the rewritten file.
4. Everything else in the panels brief binds unchanged (no registry
   edits; PAPERS NEEDED section; machine summary JSON as final text;
   env pinned; GENO/ read-only; no git).

## REFUTERS + JUDGE
Unchanged: `BASE/blocco3/BRIEF_wave2_refuter_judge.md` binds verbatim
(refuter extra duty: check the RECONCILIATION DECLARATION's honesty —
a repair claimed but not applied, or a kept section that does not
verify, is a finding).
