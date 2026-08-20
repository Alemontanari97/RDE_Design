# R22-F REFUTATION — ROUND 3, LENS L2 (asymptotics / measure-and-scaling)

Session: S-FOUNDATIONS-C4, Blocco 1 v2, 2026-08-20. Target:
`phaseD/phaseD_r22f_centerpiece.md` REVISION 3 ([REV2-r1-0..21] +
[REV2-r2-0..8] passes, 1537 lines, read [FULL] including §§9-11).
Numbering continues across rounds: last L2 id = R22F-L2-17, this round
starts at R22F-L2-18.

LENS SCOPE HONORED: 3-6% swirl-energy scaling use; M-RED band derivations
(zero magic constants); epsilon-orders of the 2-epsilon transfer;
degenerate limits; forchetta evidence-class honesty ([SE] labels, CT-6,
definitional guards). RIGHT-SIZING RULE (addendum_c4 (b) / SR-C4-13)
APPLIED: no finding below demands a closed-form gradient bound; the
§2.2-bis SCHEMA + named derivers is accepted as delivered; L2-19 attacks
the SOUNDNESS of a printed instantiation identity in a VALUE-level
lemma, which is attackable per the rule's own terms.

READ-DEPTH DECLARATIONS (this window):
- BRIEF_blocco2_phaseD.md [FULL]; BRIEF_blocco2_phaseD_addendum_c4.md
  [FULL]; phaseD_r22f_centerpiece.md rev-3 [FULL] (1537 lines).
- ALL SIX prior v2 refutation files [FULL] this window:
  phaseD_r22f_refute_r1_l{0,1,2}.md, phaseD_r22f_refute_r2_l{0,1,2}.md
  (machine summaries cross-checked against the draft §§10-11 disposition
  tables — feeds L2-21).
- swirl5f_FINAL_report.md [SLICE :436-437] RE-VERIFIED at source this
  window (grep, content read): "single-digit-% total PLAUSIBLE on
  ray-like sawtooth cycles with a good fitted sheet; >10% NOT EXCLUDED
  on ..." — load-bearing for L2-20.
- No paper read or re-read this window (no L2 finding needs one); all
  other round-1/2 source verifications stand and are not re-litigated.

PROBES (pinned env, numpy only; run PASS this window):
- `r22f_v2_probe_r3_l2_epsU_pointwise.py` (feeds L2-19)
Measured commands of this window (SR-12): §11 typed-row counts via
`sed -n '1509,1526p' ... | grep -c` → 1 BREAK row, 5 REPAIR rows,
7 AMENDMENT rows (feeds L2-21).

MANDATE-COVERAGE DUTY (round 3): channel (vi) row PRESENT with the
delta/mu schema ((vi) row :1155 — a-posteriori delta/mu form, licensed
forms (T)/(C) per [REV2-r2-3](A), O1-gated carrier, delta UNDERIVED with
derivers named; §2.2-bis :509-665) — brief :112-126 satisfied; Fig. 18
per-term disposition PRESENT (§2.3 exhibit :667-676 + disposition table
:717-723 with the [REV2-r1-9] joint-nullity readings + [REV2-r1-10]
per-instance carriage). No coverage finding.

==============================================================================
## PRIOR-FINDINGS VERIFICATION (all 4 actionable L2 round-2 findings)

### R22F-L2-18 — NOTE (resolution ledger; each disposition verified at
### its edited site, not from the §11 table alone)
- L2-13 (routed-mass eps determinacy) → RESOLVED: [REV2-r2-5](b)(c)
  (:998-1023) adopts BOTH proposed branches coherently — PRIMARY
  mu_routed = 0 with declared exclusion/re-scope, FALLBACK eps on the
  marched sector with mu(marched)/mu(total) reported and the
  routed-sector booking as a DECLARED EXCLUSION LINE in the BAND RULE
  (band algebra exhaustive again); §3.5 reading scoped per-family on
  the marched sector. The [REV2-r1-14] routing sentence is superseded
  by the MARGIN-EXCLUDED-PHASES bucket (Xi_sub not overloaded).
  Determinate as published. (One residual wording inconsistency inside
  the new text → L2-22, AMENDMENT, new finding not a persisting count.)
- L2-14 ((vi) BEST plausibility clause) → RESOLVED: [REV2-r2-6](a)
  replaces the clause with the value-route sqrt bound as SCHEMA
  ([REV2-r2-3](F), :651-665), superseded fragment quoted verbatim; the
  Theta(sqrt(eps)) rate is stated in the cell (:1155) and the
  gradient-route named as the only tightener; no [SE] tag remains on a
  gradient-level-void clause (joint fix with L1-10 confirmed). Repair
  branch (i) adopted as offered. (The adopted lemma's PREMISE
  INSTANTIATION carries a defect my round-2 repair wording itself
  seeded → L2-19, REPAIR, new finding on new text, self-origin
  declared.)
- L2-15 (at-site propagation markers) → RESOLVED: [REV2-r2-2] site
  pointer at §2.2(i) (:487-491) + [REV2-r2-4] at-site marker at §2.5
  (:853-858) — both sites now carry the SBV conditional adjacently.
- L2-16 (in-cell "P-A 4% miss" numeral) → RESOLVED: [REV2-r2-6](d) —
  the (vi) WORST cell now reads "P-A design-point miss (numeral
  confined to [GRAFT-G07])" (:1155, verified in the cell text); the
  numeral lives only in the notes block under the ceiling banner.
PERSISTING PRIOR FINDINGS: 0 (L2-12/L2-17 were NOTES, no action owed).

==============================================================================
## NEW FINDINGS (round 3, on revision-3 text)

### R22F-L2-19 — REPAIR (epsilon-premise honesty; executable): the
### value-route lemma's printed instantiation "eps_U = M-RED measured
### per-family eps" is UNSOUND read literally — a per-family/pointwise
### eps does not instantiate the uniform-on-basin premise, and the
### violation factor is unbounded
ANCHORS: [REV2-r2-3](F) :651-665, the parenthetical :655-656 ("a
(U_G)-type premise — exactly M-RED's measured per-family eps, eps_U")
and :664 ("eps_U = M-RED duty §3.6"); (vi) BEST cell :1155 ("VALUE-ROUTE
bound available a-posteriori [SCHEMA]: |argmax shift| ≤ 2·sqrt(eps_U/mu)
with eps_U = M-RED measured per-family eps"); CELL RULES :1112-1116
("NO cell above its held evidence class"); the draft's OWN correct
pattern at [T-DISC-3] HYPOTHESES :275-278 ("on its current status the
consequence holds with eps read as the measured/assumed value per
family, not as a certified class constant").
DEFECT: the lemma's premise — correctly stated in (F) as "a uniform
VALUE-error premise on the certified basin", i.e. sup over the designs
the shift ball explores of |J_true(S) − J_red(S)| ≤ eps_U — is then
IDENTIFIED ("exactly", "=") with M-RED's per-family measured eps(F).
But eps(F) (§3.1) is the value error of ONE data family at the executed
design instance(s): a POINT sample of the design-indexed error, not its
sup over the basin. The identity licenses an executor to plug a single
measured family eps into 2·sqrt(eps_U/mu) — and that bound is FALSE
under the literal reading. EXECUTABLE COUNTEREXAMPLE (probe
`r22f_v2_probe_r3_l2_epsU_pointwise.py`, RUN, all asserts PASS;
synthetic 1-D strongly-concave model, mu = 1, CT-6 clean): J_red =
J_true + a·(s − s0) + e0 has per-family (pointwise, at the measured
design s0) error |e0| while the argmax shift is a, independent of e0 —
at e0 = 1e-8, a = 0.1 the literal bound 2·sqrt(e0/mu) = 2e-4 is
violated 500x; the factor grows without bound as e0 → 0 (5000x at
1e-10; at e0 = 0 the literal bound is 0 against a finite shift). The
SUP-premise form stays true in all cases and on 200 random draws (the
lemma itself is SOUND — my round-2 verification of the sqrt rate
stands; the defect is ONLY the instantiation identity).
SELF-ORIGIN DECLARED (zero inflation both ways): the wording "eps_U =
M-RED measured per-family eps" originates in MY round-2 repair branch
(i) (r2_l2 :176-181), adopted verbatim by the reviser. The round-3
probe shows the literal reading unsound; the sharpening is mine to
ask for. The reviser applied the round-2 fix faithfully — this is a
new defect in new text, not a disposition failure.
REPAIR (one sentence, the draft's own [T-DISC-3] declaring move; no
gradient bound demanded — value-level throughout, all quantities
already named): state at (F) and read into the cell: eps_U is the
UNIFORM value-error level on the basin the shift explores; its measured
instantiation = the SUP over the M-RED value legs (A)-(B) sampled
ALONG THE DESIGN SWEEP of the §3.6 rider (sweep coverage declared per
family, beside the mu(marched)/mu(total) line) — a single-family eps
does NOT discharge the premise; until the sweep sup is measured, the
uniformity premise is OPEN and declared, exactly as [T-DISC-3] declares
(U). Optionally also point "eps_U = M-RED duty §3.6" to the value legs
(§3.2 (A)-(B) along the sweep) rather than the gradient rider alone.
The a-posteriori check list for the value route then carries: (sqrt
bound ≤ certified basin radius, R-12 deriver) + (sweep-sup coverage
declared) — mirroring condition (1)'s own discipline.

### R22F-L2-20 — AMENDMENT (citation fidelity at a third site): the §5.1
### HEADLINE claims "the licensed phrasing, nothing stronger" while
### dropping the load-bearing fitted-sheet condition
ANCHORS: §5.1 HEADLINE :1307-1310 ("HEADLINE OF RECORD (the licensed
phrasing, nothing stronger): — BEST: on-ray, corpus-swirl, in-class
geometry — the gap is plausibly SINGLE-DIGIT PERCENT ..."). SOURCE
(re-verified this window, swirl5f_FINAL_report.md :436-437): the
licensed phrasing is "single-digit-% total PLAUSIBLE on ray-like
sawtooth cycles WITH A GOOD FITTED SHEET; >10% NOT EXCLUDED ...".
[REV2-r1-7] (:479-486, fixing my round-1 L2-8) restored the qualifier
at §2.2(i) and — via [REV2-r1-18](a) — at the (ii) BEST cell, declaring
it "load-bearing (it is exactly what M-RED leg (E) tests)"; the §5.1
headline is a THIRD site carrying the same shortened phrasing,
untouched by either fix and never previously anchored (new finding,
not persisting). DEFECT: "on-ray" alone is not the licensed condition
set; dropping the fitted-sheet clause makes the headline STRICTLY
STRONGER than the license while claiming "nothing stronger" — on the
most user-facing lines of the bracket of record. WHY AMENDMENT (not
REPAIR): same defect class and same one-phrase fix as round-1 L2-8
(AMENDMENT precedent); the WORST headline line and the [SE] tag are
correct. FIX: "...the gap is plausibly SINGLE-DIGIT PERCENT (on
ray-like cycles WITH A GOOD FITTED SHEET — M-RED leg (E) tests it),
..." — one phrase, consistent with the two already-fixed sites.

### R22F-L2-21 — AMENDMENT (disposition bookkeeping; measured): the
### round-2 disposition count "6/6 AMENDMENTS" is wrong at three sites —
### the measured count is 7/7
ANCHORS: [REV2-r2-0] header :27-28 ("1/1 BREAK FIXED, 5/5 REPAIRs
FIXED, 6/6 AMENDMENTS APPLIED"); §11 preamble :1504 ("all six were
clearly-right and applied"); §11 COUNTS :1528-1529 ("AMENDMENTS applied
6/6"). MEASURED THIS WINDOW (command declared in the header block): the
§11 table itself (:1509-1526) carries SEVEN rows typed AMENDMENT —
L0-13, L0-14, L1-8, L1-9, L1-10, L2-15, L2-16 — all disposed APPLIED;
cross-checked against the three round-2 machine summaries at source
(r2_l0 :329 "amendments = 2"; r2_l1 :275 "amendments: 3"; r2_l2 :255
"AMENDMENTS: 2"; 2+3+2 = 7). DEFECT: the count line contradicts the
table it summarizes at three sites; the closure judge consumes these
counts. No disposition is missing or wrong — every one of the seven is
in the table with its edit — so this is arithmetic only. (Round-1
counts at :18 and :1486 are CORRECT: round 1 really had 6 amendments;
verified against the three round-1 files this window.) Side remark,
same fix window: §11 includes the three NOTE rows L0-15/L1-11/L2-17 as
courtesy but omits NOTE L2-12 (the round-2 resolution ledger) — either
drop the courtesy rows or add L2-12; harmless, but the table's
inclusion rule should be one or the other. FIX: 6/6 → 7/7 and "all
six" → "all seven" at the three sites (append-only marker; the stale
numerals never land).

### R22F-L2-22 — AMENDMENT (internal consistency of [REV2-r2-5]):
### "trivially checkable at synthesis time" contradicts the same
### block's a-posteriori interior-margin check
ANCHORS: [REV2-r2-5](c) :1011-1013 ("PRIMARY RULE — mu_routed = 0 per
family, a CONSTRUCTION property of the in-house synthesized families
F-a..F-d, trivially checkable at synthesis time"); [REV2-r2-5](a)
:982-997 (m0 = MARCHED-DOMAIN margin floor, "checked A POSTERIORI from
the march output (one scan)"; interior dips excluded-and-booked).
DEFECT: under the (a) re-declaration, membership in the routed bucket
includes INTERIOR-margin violations, which are knowable only from the
march output — so mu_routed = 0 is NOT checkable at synthesis time;
only the ENTRY-margin half is. The two adjacent clauses of the same
revision block disagree on when the check can fire. The load-bearing
content (primary rule + declared exclusion + fallback) is untouched —
the probe-backed determinacy of L2-13's fix survives on either timing —
this is wording accuracy in a spec whose execution discipline is the
point. FIX (one line): "a CONSTRUCTION property targeted at synthesis
time (entry margin checkable there) and CONFIRMED by the (a) one-scan
a-posteriori domain check (interior); a family failing the scan is a
DECLARED exclusion/re-scope, never a silent booking."

### R22F-L2-23 — NOTE (verified-green ledger, round 3; zero credit
### inflation): revision-3 chains that SURVIVED L2 attack this window
(a) [REV2-r2-3](F) sqrt-lemma algebra re-checked: strong concavity +
uniform sup-premise gives (mu/2)·d^2 ≤ 2·eps_U hence d ≤ 2·sqrt(eps_U/
mu) — exact, constant right; probe control leg (200 random draws)
confirms; the TIGHTNESS statement (Theta(sqrt(eps))) matches my round-2
probe of record. Only the instantiation identity is defective (L2-19).
(b) [REV2-r2-5] degenerate-limit control re-run mentally at m0 → 0+:
the routed bucket empties, PRIMARY rule becomes vacuous-true, FALLBACK
reporting reduces to mu(marched)/mu(total) = 1 — no discontinuity; the
round-2 defect stays closed. (c) [REV2-r2-6](d) CT-6 sweep over ALL
revision-3 insertions: no P-A..P-D numeral inside any table cell,
bound, band, or schema; the [GRAFT-G03/G04/G05] numerals remain
confined to the notes blocks under the ceiling banner; definitional
guards (G-04 stronger form [REV-NRS-2], film-cooling caveat
[REV-NRS-3], RMSD_theta never-booked rule) intact and unedited. (d)
[REV2-r1-15] addendum-(c) declaration unchanged in place; delivery-
check item still met. (e) (vi) row honesty spine intact: WORST cell
still asserts NO argmax-shift number at any grade; value-route clause
carries [SCHEMA] not [SE]; O1 gate named in-cell; brief :126
never-value-for-optimum sentence carried. (f) §2.2(i)/§2.5 SBV site
pointers verified in place ([REV2-r2-2]/[REV2-r2-4]). (g) B-1 ≥4-point
ladder, B-2 dmdot measure, B-3 window-complement mass, B-4 domain-
margin license — all read as published, executable, zero magic
constants (BAND RULE + declared exclusion line exhaustive). (h) §10
round-1 disposition counts re-verified correct against the three
round-1 files (1/15/6) — the arithmetic defect is round-2 only
(L2-21).

==============================================================================
## COUNTS (this round, this lens)
BREAKS: 0. REPAIRS: 1 (L2-19). AMENDMENTS: 3 (L2-20, L2-21, L2-22).
NOTES: 2 (L2-18, L2-23).
PERSISTING PRIOR FINDINGS RE-COUNTED: 0 (all 4 actionable round-2 L2
findings verified RESOLVED at their edited sites).
DRY VERDICT AT THIS LENS: NOT DRY (1 REPAIR sustained; 0 BREAKS).

## PAPERS NEEDED
NONE. (No L2 finding requires a source not already on disk.)
