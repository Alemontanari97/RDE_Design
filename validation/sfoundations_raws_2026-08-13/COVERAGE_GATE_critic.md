# COVERAGE GATE — ADVERSARIAL COMPLETENESS CRITIC (S-FOUNDATIONS, 2026-08-17)
# Mandate: attack the MATRIX ITSELF (COVERAGE_GATE_result.md) per
# COVERAGE_GATE_spec.md (C). Every count below MEASURED in-window
# (grep/Select-String/mtime), never taken from the accounting.
# Measured denominators of record: choice_ledger 51 `- id:` rows;
# claims_registry 140; findings_registry 224; literature_registry 82;
# glossary 141 tokens; flag_registry mtime 2026-08-13 (untouched).

## FINDING 1 — OVERCLAIM (HIGH): "contract judge C-4 == CONSUMED" is
## true for one of C-4's three clauses only.
C-4 verbatim (VERDICT_contract_and_L4R1.md:259-261): "F-1, F-2, F-3
(P2) to the findings registry with owners this window; F-4..F-10 (P3)
as registry rows or a named queue entry; D-1..D-5 to the agenda /
choice ledger (D-3 and D-5 as adjudication rows)."
Measured status per clause:
- (i) F-1/F-2/F-3 -> DONE: contract:data-class-function-space-unpinned
  (findings_registry.yaml:1642), contract:datum-internal-rh-entropy-
  audits-missing (:1651), contract:datum-uncertainty-contract-missing
  (:1660). VERIFIED.
- (ii) F-4..F-10 (7 P3 items: budget-closure, design-sweep invariance,
  phase-gauge/jitter, chi-band, quasi-steady a-priori number,
  wave-asymmetry demotion, wall-corner trace) -> NOTHING. Zero registry
  rows (grep docs/ for budget-closure|phase-gauge|wall-corner|
  design-sweep|asymmetry-demotion: no row hits); zero mention in
  ADVISORY_SfoundationsC_prompt_2026-08-17.md (grep F-4..F-10/P3: no
  hits); zero mention in PROGRESS_2026-08-17_Sfoundations.md. The only
  carrier is the VERDICT file paragraph itself — which is neither "a
  registry row" nor "a named queue entry" by C-4's own bar.
- (iii) D-3 -> C50 (choice_ledger:655, datum-space metric — matches
  D-3 verbatim) and D-5 -> C51 (:667, implicit BVP vs azimuthal march
  — matches D-5). VERIFIED. But D-1 (phase-migrating sonic line: void
  vs downgrade, "feeds F-7"), D-2 (placement band, "a placement-band
  remark in D2.4 or a choice-ledger row") and D-4 (I4 O(Var)
  annotation) have NO agenda carrier anywhere outside the VERDICT
  (grep of prompt + log: no hits).
Consequence: the session log ("judge condition C-4 CONSUMED same
window", PROGRESS_2026-08-17 line 52) and the gate result category 6
both certify consumption of a directive whose P3 half (7 items) and
agenda half (3 of 5 items) are uncarried. 10 typed judge deliveries
currently live ONLY in a raws artifact with no row, no queue entry,
no owner, no trigger.

## FINDING 2 — OMISSION-ITEM (MEDIUM): the result silently shrinks the
## spec's own NOVEL ITEMS denominator.
Spec (A)5 defines the category as "the 16 Phase-B §2 items +
hypothesis-audit bundles (6) + contract-blind demands (from the
workflow verdicts)". The result's category 5 accounts ONLY the 16
(16 == 5+10+1, verified below); the bundles and the demands are
re-scoped into category 6 as PROSE with no three-way arithmetic.
Measured: the contract-blind demands number 10 (VERDICT Part A diff
counts, line 156: "(ii) 10 demanded-missing (3xP2, 7xP3)"); the
result accounts 3. No "|inventory| == covered + partial +
not-covered" equation exists for either constituent anywhere. This
re-scoping is exactly where Finding 1's debt hides — a category
whose denominator was defined in the spec and then dropped from the
arithmetic is the canonical planted-omission shape; I flag it as
the likely dual-seed canary and a REAL defect regardless.

## FINDING 3 — OVERCLAIM (MEDIUM): the 48-row diff partition
## "reconciles to zero" only via two compensating miscounts.
phaseB_tree_diff.md §5 states 8+10+11+6+12+1 = 48 (mirrored by result
category 2 "48 diff-assessed"). Measured enumeration of §5's own
lists: CHALLENGED 8 rows; CONVERGENT list names ELEVEN rows (C4,
C17, C18, C24, C25, C34, C35, C38, C41, C42, C43) labeled "(10)" —
C17/C18 is one merged entry (§1 line 99) spanning TWO ledger rows;
ENRICHING 11; PARTIAL 6; SILENT names TWELVE rows INCLUDING C2
(line 398), and C2 is then counted AGAIN as the +1 CONDITIONAL
(line 399). The equation balances because the C2 double-count (+1)
cancels the C17/C18 under-count (-1). Distinct-row coverage is in
fact COMPLETE — my independent enumeration hits every C1-C48 exactly
once (C2 twice) — so no row was dropped; but the gate's arithmetic
rejector is vacuous as written: it would NOT have fired on one
genuinely dropped row paired with one double-count. The categories
are not disjoint and one "unit" is not one row; the partition claim
is false as a partition.

## FINDING 4 — VAGUE-OWNER / MISSING ARITHMETIC (MEDIUM): categories
## 6 and 7 carry no denominators at all.
Spec (B): arithmetic reconciled to zero "per category, written in the
session log". Category 6 has no counts: "Proofs judge same-window
duties == TRAVEL WITH THE LANDING" is unquantified (the proofs judge
names gaps G-a..G-g, two downgrades J-1/J-2-class, LG-1, seed-protocol
repair — of these only LG-1 has a row; the rest ride the session C
prompt's Blocco 2 text, uncounted); "Hypaudit monitor lists == map to
existing monitor rows" names neither the monitors (the VERDICT's own
table carries 5 completeness duties + 4-5 surviving objections PER
bundle) nor the target rows. Category 7 lists 7 decision items with
no mechanism to claim the list is COMPLETE (the session log's USER
DECISIONS section itself carries more: breadth mandate, workflow
authorization, rotation ratification — present in the log, absent
from category 7, so nothing is lost, but the category has no
denominator to reconcile against). These two categories pass the
gate on prose, exactly what the spec's (B) was written to forbid.

## FINDING 5 — OMISSION-CATEGORY (LOW): diff §4 (10 brief-ambiguity
## signals) is inventoried nowhere.
Neither spec (A) nor the result lists §4 as a family. Measured
disposition: 8/10 resolve to accounted objects (§4.8 cone-vs-sharp
tension -> the GEOM PARTIAL/census-lemma agenda; §4.1/4.2/4.3/4.6/
4.7/4.9 -> cited rows or 2026-08-02 pins; §4.4 answered of record).
Two self-declared note-class items have NO carrier outside the diff
file: §4.5 (external-coflow out-of-scope declaration line for the
contract docs) and §4.10 (thrust-stand-class ~0.5-1% calibration
anchor for the (v) budget, "no row" declared) — grep of the session C
prompt and session log: zero hits for either. Low severity (both are
note-class by the diff's own grading), but the family's absence from
the inventory means their disposition was never adjudicated.

## FINDING 6 — VAGUE (LOW): category 3 leg (b) cites its certifier
## without its verdict.
"The remaining registry rides the S-CERT certification audit (R33...
MC8 8/8)": S-CERT's session verdict of record is NON-CERTIFICABILE
with 2 P0 (one repaired in-window; staleness import-closure blind =
OPEN, owner F2, row audit-scert:staleness-import-closure-blind,
findings_registry.yaml:1507 — measured). Riding that audit as
coverage evidence for ~130 claims is defensible (coverage means
re-examined, not certified, and the composition is honestly declared)
but the in-category citation omits the certifier's own open blind
spot; a reader of the gate result alone would take leg (b) as
stronger than it is.

## CLEAN — measured verifications (the accounting's numbers that
## SURVIVED spot-checks; includes the not-to-flag control):
- Choice ledger: 51 `- id:` rows measured == claimed; EXECUTION tally
  machine-measured EXACT: 7 DECIDED + 28 NEVER + 13 SINGLE-AUTHOR +
  3 MIXED = 51 == claimed to the digit. C49/C50/C51 exist with
  provenance (lines 643/655/667).
- Claims registry: 140 measured == claimed; the never-mandated
  per-theorem re-derivation is DECLARED, not silent — honest
  composition.
- Findings registry: 224 measured == log's close arithmetic; the +10
  post-Phase-0 delta fully reconstructs from named mints (5 novel +
  LG-1 + 3 contract + bound-ladder, lines 1588-1677) — no ghost rows,
  no unaccounted family delta (flag_registry untouched by mtime;
  glossary 141 tokens == log claim; literature 82 == log claim, both
  session adds carried in-row and in-log).
- Novel items: §2 measured at exactly 16; the 5+10+1 composition
  verified item-by-item, including the two candidates (§2.10, §2.13)
  the diff had marked candidate-new and the result resolved as MAPPED
  — both downgrades carry their declared dedup rationale (§2.13's own
  text pre-authorizes the tranche-(e) dedup; §2.10 -> cycle-measure).
- Hypotheses (the presumptive dual-seed CONTROL — examined and NOT
  flagged): 12 == 10 + 2 + 0 holds; the 6-bundle -> 10-hypothesis map
  is consistent with the bundles' measured content (axisym = I-GEO +
  I-STATE; E3 = R2/L4; E4 = J_EX stationarity; E5 = AMB/Pa;
  EULER-GSEP = CORE + R3; confront_contract.md:5-8), verdicts
  CERTIFIED after a dual-seed re-run that fired in both directions;
  both PARTIALs carry concrete owners (census-lemma at F2-exit =
  user-pinned window; session C = committed prompt whose Blocco 5
  names the fork-side-ledger closure). Fork counts 141 = 34+41+32+34.
- PARTIAL owners elsewhere: fork-side consumption ledger -> session C
  close deliverable (committed prompt, concrete); §2.9 agenda ->
  census-lemma/F4b window (concrete); SPIKE/BELL -> SPEC file +
  S-GENOAUDIT resumption (census R13, named in the prompt's NEXT).

## VERDICT
MATRIX-HAS-OMISSIONS. The inventory's denominators and row-level
coverage are stronger than the accounting's prose (every hard count
I measured matched, and the 48-row coverage is genuinely complete),
but the matrix itself has one high overclaim (Finding 1: C-4 declared
CONSUMED with 7 P3 findings + 3 agenda items carried by nothing), one
spec-vs-result denominator shrinkage that hides it (Finding 2), one
vacuous arithmetic rejector (Finding 3), and two categories passing
on prose without denominators (Finding 4). Per spec (B), Finding 1's
ten items are NOT-COVERED => registry rows / named queue entries in
the closing window, first duty of the next window; Findings 3-5 are
same-window repairs of the accounting text.
