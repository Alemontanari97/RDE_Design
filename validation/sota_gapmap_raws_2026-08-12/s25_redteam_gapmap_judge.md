# FORM-3 RED-TEAM — JUDGE LAYER OF ADVISORY_S24_sota_gapmap_2026-08-12

- **Date**: 2026-08-12 (S25 window). READ-ONLY pass: no tracked file
  edited, no code executed; this report is the only artifact written.
- **Target**: `validation/ADVISORY_S24_sota_gapmap_2026-08-12.md`
  (judge synthesis, 1037 lines, self-labeled "judge-adjudicated in one
  round").
- **Ground truth**: the 12 raw facet files in
  `validation/sota_gapmap_raws_2026-08-12/` (6 finders `s24_gap_*.md`,
  6 verifiers `s24_gapv_*.md`), ALL read in full, including the two
  second-pass/superseding verifications (mesh-amr: independent re-check,
  ZERO corrections, verdict table unchanged; driver-nonsmooth: SUPERSEDES
  an interrupted draft, header declares "changing two verdicts (G4,
  G5b)"). Record docs opened at source for every §3 pointer and every
  spot-checked §6 status (list under RT-14).
- **Standing rule applied**: before absorbing any one-round artifact,
  red-team the judge synthesis for the S21-precedent failure modes —
  judge-ADDED claims, manufactured unanimity, incomplete absorption,
  silent wording weakenings, header totals never reconciled with the
  body.

---

## VERDICT ROWS

### RT-1 — COUNTS, §1 header vs raw files: **PASS**
Recounted from the raws:
- Finder findings 47 = 8+8+8+8+8+7 (mesh F1-F8, cell F1-F8, param
  F1-F8, driver G1-G8 with G5 = one heading (a/b halves), constraints
  G1-G8, thermo G1-G7). Exact.
- Verifier verdicts 26 CONFIRMED / 18 DOWNGRADED / 3 REFUTED-outright:
  mesh 1/5/2 (gapv "COUNTS: confirmed 1, downgraded 5, refuted 2";
  second pass "SUMMARY/VERDICT TABLE UNCHANGED") + cell 4/3/1 + param
  5/3/0 + driver 6/2/0 (the gapv's own per-finder-heading convention:
  "6 CONFIRMED..., 2 DOWNGRADED (G4; G5...), 0 REFUTED") + constraints
  6/2/0 + thermo 4/3/0 = 26/18/3. Exact.
- The 3 outright refutations (mesh F4, mesh F8, cell F6) all land in §3
  (AC1, AC5, AC7), consistent with the declared method.
- §1's named refuted-sub-claims list checks out (G5a crash, thermo
  G1/G5 novelty, mesh F5 headline, param F8 magnitude, param F5) —
  EXCEPT the driver-G4 "never surveyed" refutation, which is absent
  from §1, §4 AND contradicted in §3/§6 (see RT-5).

### RT-2 — COUNTS, body enumeration: **PASS**
Map = 36 entries: 5 HIGH (GAP-1..5), 23 MEDIUM (GAP-6..28), 8 LOW
(GAP-29..36). Already-covered = 16 rows (AC1-AC16). Quarantine = 10
rows (Q1-Q10). Every one of the 47 finder findings is accounted for in
at least one of map/AC/Q (full trace performed; no dropped finding).
The 5-HIGH tier carries all 6 verifier-HIGH verdicts (driver G1 +
constraints G7 merged into GAP-1, labeled).

### RT-3 — §3 provenance framing: **FINDING, LOW**
- EVIDENCE: §3 title "(refuted-because-covered; ...)" and §1 "refuted-
  because-already-covered items go to the coverage ledger". True for
  only 3/16 rows (AC1/AC5/AC7). AC2 descends from mesh-F1 DOWNGRADED
  MEDIUM, AC6 from cell-F1 DOWNGRADED MEDIUM, AC8 from cell-F3
  CONFIRMED LOW (moved via labeled Q1 adjudication), AC10 from driver-G4
  DOWNGRADED, AC3/AC4/AC12/AC13/AC14/AC15 from refuted/covered HALVES of
  downgraded findings, and AC16 from a finder DROP (never a finding).
  No content is lost (residues went to the map or the delta column), but
  the ledger's self-description misstates row provenance.
- REPAIR: retitle ("covered items and covered halves") or add a
  per-row provenance tag.

### RT-4 — GAP-18 verdict + ownership infidelity (driver G5b): **FINDING, HIGH**
- EVIDENCE: verifier of record (`s24_gapv_driver-nonsmooth.md`, the
  SUPERSEDING pass): G5b = "**DOWNGRADED (owned)** ... severity MEDIUM
  ... this IS speed-dispatch named conditional **N6 — 'benign-flip
  segment merge. Touches constraint 7 (redefines the RK-G P2 segment
  boundary); needs its own panel. Flagged, never traded'** ...
  [P-FLIPMAT] would EXECUTE a constraint-7-touching change without the
  N6 panel — **not licensable as registered** ... 'sharpens N6', not a
  new mint". N6 verified real at
  `ADVISORY_engine_speed_audit_2026-08-12.md:443-444` (verbatim).
  Advisory: GAP-18 header = "[driver-nonsmooth G5b — **CONFIRMED**
  MEDIUM]"; ownership = "F2 entry (G0/T2 review input)"; §5 item 7
  registers [P-FLIPMAT] as an S25 probe. The token "N6" appears NOWHERE
  in the advisory; no judge-adjudication label marks the deviation.
- Mitigating nuance (declared for fairness): D6's G0-review clause
  itself names "benign-flip policy refinement" among the review's scale
  levers (D6 ~:884-886), so the G0/T2 routing is not invented — but the
  specific, later, binding ownership adjudication (N6: own panel, never
  traded) is silently dropped, the verdict label is silently upgraded
  DOWNGRADED→CONFIRMED, and a probe the verifier ruled not-licensable is
  registered unconditioned.
- REPAIR: relabel GAP-18 "DOWNGRADED MEDIUM (owned — duplicate of speed
  conditional N6)"; add N6 as owner-of-record (G0/T2 may stay as a
  labeled judge routing for the materiality-metric input); condition §5
  item 7 on the N6 panel.

### RT-5 — AC10 + C32 re-assert a verifier-REFUTED sub-claim (driver G4): **FINDING, HIGH**
- EVIDENCE: verifier of record: "REFUTED SUB-CLAIM: 'quasi-Newton carry
  that preserves RK-G determinism was never surveyed'. The S-SPEED audit
  of record ALREADY adjudicated the curvature-policy alternatives: §7.3
  survey row S1 registers 'HVP DECLINE-as-default (= N5); quasi-Newton
  reuse OUT by policy'; the dispatch carries N5, N8, M6, and the DEAD
  ROW 'dispatch-amortization Hessian story' ... [P-QNCARRY] must be
  re-routed through the S1 survey row's re-opening trigger, not run as a
  free probe." S1 verified real at
  `ADVISORY_engine_speed_audit_2026-08-12.md:600-602` (verbatim).
  Advisory: AC10 delta ends "**survey absence noted**
  (sota-library-survey directive)" — the refuted claim restated as fact;
  AC10's covered-by cites census row 7 + D6:880-881 but OMITS the
  S-SPEED ownership set (S1/N5/N8/M6/dead row) the verifier listed; §6
  row C32 status = "single-author (R-3 cites no alternatives; **survey
  NEVER**)" — the refuted claim again; §5 item 8 registers [P-QNCARRY]
  "(AC10 input)" without the S1-re-opening-trigger condition; and this
  is the ONLY verifier refutation absent from the §1 list and from §4.
- MECHANISM (shared with RT-4): the driver gapv file's superseding
  header states its second pass added three ownership hits and "chang[ed]
  two verdicts (**G4, G5b**)" — exactly the two places the advisory
  deviates. The judge evidently consumed the interrupted draft, not the
  superseding verification. (The raws on disk are the ground truth; the
  advisory must match them regardless.)
- REPAIR: in AC10, strike "survey absence noted" → "policy-bound-vs-
  theorem-bound distinction as input to the owned review; survey row of
  record = S-SPEED §7.3 S1 (re-open trigger applies)"; add S1/N5/N8/M6 +
  dead row to AC10's covered-by; fix C32's status (the survey EXISTS of
  record; open axis = theorem-bound justification/review, not survey
  absence); condition [P-QNCARRY] on the S1 re-opening trigger.

### RT-6 — Choice-ledger reading line not reconciled with its own table: **FINDING, MED**
- EVIDENCE: §6 closing line claims "**8 rows CONVERGED ... 14
  single-author, 23 NEVER**". Recount of the 45 status cells: pure
  CONVERGED 5 (C3, C4, C15, C23, C24); mixed 3 (C29, C31, C39);
  single-author 12 (C1, C6, C11, C12, C13, C17, C18, C19, C27, C32,
  C44, C45); NEVER 25 (all others). 8 CONVERGED is reachable only by
  counting all 3 mixed rows as CONVERGED — which leaves 12/25, not
  14/23. NO assignment of the mixed rows produces 14 single-author + 23
  NEVER. This is the S21-precedent failure mode verbatim (header totals
  never reconciled with the body). NOTE: the 8/14/23 triple has already
  propagated into the rewritten PROGRESS census (R25 row) — the repair
  must touch both. Minor adjunct: the preamble declares status values
  "CONVERGED-panel / single-author / NEVER" while the table also uses
  CONVERGED-measured / CONVERGED (constructional) / split statuses.
- REPAIR: recount and correct the reading line (and the PROGRESS R25
  echo), or state the convention that yields 14/23; align the preamble
  vocabulary with the labels actually used.

### RT-7 — C4 status class overstated ("CONVERGED-panel" without a panel): **FINDING, MED**
- EVIDENCE: C4 (knot placement law / free-knot rejection) claims
  "CONVERGED-panel; evidence: D6 item 9". The deciding event of record
  is D6's "S20 RESIDUE-(a) **SURVEY DECISION** (2026-08-07, per the
  standing survey + generality directives; log S20 step 3)" — adopted
  [X-AKNO], REJECTED free-knot (Jupp-1978 lethargy + RK-G cost) with
  declared reasons and read-the-source findings (D6 ~:906-944). An
  adjudicated survey decision of record — no panel sat. Contrast the
  other panel claims, which check out: C23 (speed audit = Form-2 panel
  + Form-3 red-team + gauntlet, label of record, audit :7-9, :38-41),
  C24 (thermo survey = instances I1-I3 + [JUDGE] dispute table), C29
  (DE-bucket panel C3, advisory :219-226, judge-merged :175).
- REPAIR: C4 status → "CONVERGED-survey (adjudicated decision of
  record)" or equivalent; reserve "-panel" for actual panel events.

### RT-8 — Quarantine completeness: one cross-verifier disagreement harmonized silently: **FINDING, MED**
- EVIDENCE: cell-cert verifier F8: "**No coverage found in
  D6/M0/advisories**" (constants cluster incl. NEWTON_TOL_FACTOR). Thermo
  finder+verifier G5: the cluster is REGISTERED — AUDIT F5
  (`AUDIT_agnostic_2026-08-07.md:416-428`) with the prescribed
  halved-constants test (:426; verified real this pass). The judge
  resolved the contradiction inside GAP-29/AC9 ("Constants cluster =
  AUDIT F5 registered ... the ladder/sufficient-decrease half is new")
  with no Q row and no judge-adjudication label — against the advisory's
  own method rule ("Disagreements between verifiers are NOT harmonized —
  they are quarantined") and asymmetric vs Q1, which labeled the exactly
  analogous cell-F3/AUDIT-F8 case. The resolution direction is almost
  certainly factually right (AUDIT F5 exists and covers the constants
  half); the broken piece is the declared process, not the content.
- REPAIR: add a Q row (or a "judge-adjudicated" label on GAP-29/AC9)
  recording the cell-F8-coverage vs thermo-G5/AUDIT-F5 split.
- Completeness sweep otherwise PASS: Q1 (cell-F3 vs AUDIT F8), Q2
  (constraints-G6 vs param-F1 B-spline tension), Q7 (GAP-9 severity
  split) are the other three genuine cross-file disagreements and all
  three are quarantined with labels; Q3-Q6/Q8-Q10 carry the verifiers'
  declared caveats faithfully (toy-measured, tuned-synthetic,
  unmeasured halves, corrected magnitudes, model-inferred wording).

### RT-9 — GAP-31 severity label: **FINDING, LOW**
- EVIDENCE: advisory header "DOWNGRADED **LOW-MEDIUM**"; verifier
  verdict table: G5a "DOWNGRADED | **LOW**". Placed and counted in the
  LOW tier (so §1 totals unaffected); the header inflates by half a
  notch. REPAIR: relabel LOW.

### RT-10 — GAP-1 spec: verifier caveat silently dropped: **FINDING, LOW**
- EVIDENCE: "Spec of record (finder F4, verifier-confirmed): enforce
  KSmax_rho(r(W)) <= 1 − ln(N)/rho, **sufficiency proven**". The
  inequality IS finder content (driver G1, verbatim) and the verifier
  confirmed the bounds — but ruled the finder's justification chain
  "**garbled** (it invokes the upper bound backwards)" and the
  −ln(N)/rho shift "**only redundant conservatism**" (KSmax >= max r_i
  alone already makes KSmax_rho <= 1 sufficient). Harmless per the
  verifier; the correction is nowhere in the advisory. REPAIR: one
  parenthesis noting shift-redundancy + corrected proof route.

### RT-11 — GAP-17 declared boundary dropped: **FINDING, LOW**
- EVIDENCE: verifier G8 declares a dead-row boundary — the speed
  dispatch's "Jacobi-precond removal" dead row "bounds this finding from
  the other side — G8 proposes refreshing, never removing ... M6's
  'precond batch' speeds the MEASUREMENT of the same frozen Dv, it does
  not refresh it". GAP-17 omits it. Cheap protective declaration lost.
  REPAIR: one line in GAP-17.

### RT-12 — Judge-added content: **PASS**
Every judge-side addition found is LABELED: §1 merge list; dedup labels
in the GAP-1/9/22/29 headers; AC8 "JUDGE-ADJUDICATED dedup, see Q1";
Q1/Q7 adjudication labels; §6 [J] rows C3 and C14. Sweep of every
number, formula, probe name and spec text in §2/§5/§6 against the raws
(incl. the KS-max inequality, TR_FLOOR = K_RICH·tol_dp/||g||, the
convex-hull B-stationarity test, [P-*]/[R*] probe names, 0.415
threshold, 19:1 D'-band datum, net 0.17/2.5 Sauer numbers, ratio
25/0.0, −(2−sqrt(3)), 6.7e-16, 2.2/17.5/170 amplitudes, 34.8 K/8.34 K
margins, 11.2%/1853x (Q4-fenced), 2.11x, i_cross 96→82, |mu·m|=3.55e3,
1/45 lanes (Q10-worded), 4.4%/1.4%): all trace to a finder or verifier
file. No unlabeled judge invention found. (One internal wobble: GAP-27
says "~20 weighted lanes" where Q10/verifier say ~21 at the corrected
N — trivial.)

### RT-13 — Verdict fidelity, full sweep of the 36 map entries: **PASS on 34/36**
All header verdict/severity labels match the verifier files exactly,
including honest merge/split declarations (GAP-1, GAP-9+Q7, GAP-22,
GAP-29) and the absorbed corrections of record (GAP-6 net-0.17/Q9,
GAP-25 AFEM attribution + E2 exclusion, GAP-26 partial ownership,
GAP-34 magnitudes/Q8, GAP-33 "verifier-strengthened", GAP-15 wording
correction, GAP-2 fairness annotation, GAP-3/Q3, GAP-7/Q4, GAP-28/Q5,
GAP-22/Q6, GAP-13 interface caveat, GAP-19 declared boundary, GAP-1
implementation caveats). Exceptions: RT-4 (GAP-18) and RT-9 (GAP-31).

### RT-14 — Coverage ledger AC1-AC16, pointers opened at source: **PASS 15/16** (AC10 = RT-5)
| AC | Verdict | Evidence (verified this pass) |
|---|---|---|
| AC1 | REAL | ledger 10bis U3 verbatim (`docs/rde_nozzle_theorem_ledger.md:681-685`); M0 BAR-CLASS note verbatim (`docs/rde_nozzle_MASTER.md:313-318`, dated 2026-08-05); PROGRESS R25 (verifier-quoted at S24 HEAD; row live today) |
| AC2 | REAL | PROGRESS "R18/R21 (C7/O5, S24+1 opzionale)"; 41.8% datum re-verified by mesh gapv second pass |
| AC3 | REAL | `validation/o32_mesh_convergence.py`: dp_model :58, NON-CONCLUSIVE rule :61-73, p_fine 2.5347 :245, first-order negative control :396-404, stage "mstop" :590 |
| AC4 | REAL | S19 log :49/:53 (diagnostic executed, numbers verbatim per gapv); S22 log :74-80 STIM-1; o32 mstop stage |
| AC5 | REAL | R25 "universalita' K_RICH=4 (F2 audit)" (double-verifier-quoted); 0.415 = thermo gapv correction |
| AC6 | REAL | AUDIT F3 :388-400 — BOTH modes incl. ":394 the quintic ... EXTRAPOLATES polynomially without bound"; thermo survey C-D restatement :253-255 IS clamp-only ("silent clamp at T_TAB_LO/HI with dT/dq = 0") — the spec correction is genuine |
| AC7 | REAL | speed audit H1 (:152-153 "early-abort HOOKS ... mandatory M5 chain", :280); prompt L2 :49 + "costa 111 s" :40-41; PROGRESS R22 |
| AC8 | REAL | AUDIT F8 :458-470, "[CONFIRMED | low]" — same unit-mixing finding, adjudicated LOW; Q1-labeled |
| AC9 | REAL | AUDIT F5 :416-428; halved-constants test :426; C_OPS "weakly derived" :428 |
| AC10 | POINTER REAL, CONTENT FAILS | R7c + D6 colored-Hessians real; delta re-asserts refuted "survey absence" and omits S-SPEED S1/N5/N8/M6/dead-row (RT-5) |
| AC11 | REAL | kickoff §4bis: "raising StopIteration terminates cleanly with status 3" (actual :354-356; cited :340-342 — drift inherited from the raws, content verbatim) |
| AC12 | REAL | panel advisory :269-270 verbatim: "a budget risk inside the [P4] cap, not an unsoundness (E3) — monitor wall time per rung" |
| AC13 | REAL | D6 :920-931: control-point switch rejected on stack-revalidation + "knot PLACEMENT, not parametrization conditioning" — no oscillation axis, exactly as Q2/GAP-21 state |
| AC14 | REAL | problem book duty verbatim (`docs/rde_nozzle_problem_book.md:292`); o32/P2_outline sonic-Sauer exclusion :229-233; in-code DATA CONTRACT :37-40 (also AUDIT SEED-A3: "the declaration exists, the quantification does not") |
| AC15 | REAL | R25; attribution print :405-408 re-verified by mesh gapv; GENO 801/4001 ran |
| AC16 | REAL | AUDIT F7 :444-456 (400-point window, silent fallback, box-derived-window fix :454 — the "credited under GAP-11" note matches the audit's own suggested fix); speed audit H2 :341 (+ bracket scan per-record per cell gapv :531-532) |

Hygiene note (no repair required): a few cites are off by 5-15 lines
against today's files (kickoff :340-342→:354-356; D6:738→:743;
D6:880-881→:884-886) — inherited from the raws; content verbatim-real
in every case.

### RT-15 — §6 status spot-checks beyond RT-7 (14 rows checked total): **PASS 12/14** (C4 = RT-7, C32 = RT-5)
- C15 CONVERGED-measured: SUPPORTED (S19 mstop diagnostic executed;
  S22 STIM-1; both of record).
- C23 CONVERGED-panel: SUPPORTED (speed audit = Form-2 panel + Form-3
  red-team + gauntlet, label of record :7-9/:38-41; H1 hooks made
  mandatory by red-team repair :280).
- C24 CONVERGED-panel: SUPPORTED (thermo survey = I1/I2/I3 + [JUDGE],
  dispute table D1-D3, "the measurement, not the vote, decides"; KEEP
  §8 with C-A..C-D).
- C29 CONVERGED-panel for rung-freeze: SUPPORTED (panel C3 :219-226,
  judge-merged :175; "alternatives NEVER considered" = constraints gapv
  verbatim).
- C31 CONVERGED eq-path / IP NEVER: SUPPORTED (§4bis :348-357: explicit
  eq-path decision; IP switch known, never adjudicated).
- C39 convention CONVERGED (T1) / verification NEVER: SUPPORTED (S24
  log :35 T1; constraints gapv: "T1 closed the CONVENTION only").
- C28 NEVER (successor absent): SUPPORTED (M0 :1618-1624: K~A_0 =
  CONJECTURE + named falsifier; falsified S22/S24 per both gapv files;
  no successor found by either verifier).
- C9/C42 NEVER (registered open row): SUPPORTED (R25 rows).
- C12 single-author (fidelity adjudicated, accuracy NEVER): SUPPORTED
  (AUDIT SEED-A3 + problem book :292).
- C45 single-author (registered): SUPPORTED (AUDIT F7 + speed H2).
- C3 [J] CONVERGED (constructional): labeled judge-added; no
  adjudication event exists and none is claimed — acceptable as
  labeled.

### RT-16 — Label discipline: **PASS**
The advisory self-labels "judge-adjudicated in one round" (header) and
closes "Judge synthesis performed in one round; quarantine items are
open." No internal text upgrades the artifact to converged/ratified/
unanimous; Q1 explicitly disclaims unanimity; every panel/ratification
reference points to a real external event (verified: DE-bucket C3,
thermo survey, speed audit, §4bis).

---

## FINAL VERDICT: **ABSORB-WITH-REPAIRS**

The synthesis is structurally sound: every §1 count reconciles exactly
with the raws (RT-1/RT-2), 34/36 map entries are verdict-faithful with
the verifiers' corrections and caveats absorbed (RT-13), all §3
pointers except one are real and content-matching (RT-14), judge
additions are labeled (RT-12), three of four cross-verifier
disagreements are properly quarantined (RT-8), and the one-round label
is honest throughout (RT-16). No manufactured unanimity, no invented
numbers.

**Required repairs before the map is cited as the SOTA gap map of
record** (owner: S25-bis repair row, per PROGRESS R30):
1. **[HIGH / RT-4]** GAP-18: relabel DOWNGRADED-owned (duplicate of
   speed conditional N6); add N6 ownership; condition §5 item 7
   ([P-FLIPMAT]) on the N6 panel.
2. **[HIGH / RT-5]** AC10: strike "survey absence noted", cite S-SPEED
   §7.3 S1 + N5/N8/M6 + dead row; fix C32's "survey NEVER" status;
   condition §5 item 8 ([P-QNCARRY]) on the S1 re-opening trigger; add
   the G4 refutation to the §1 refuted-sub-claims list.
3. **[MED / RT-6]** Fix the §6 reading line (8/14/23 vs actual
   5+3-mixed/12/25) and its echo in PROGRESS R25; align the preamble
   status vocabulary.
4. **[MED / RT-7]** C4: "CONVERGED-panel" → "CONVERGED-survey
   (adjudicated decision of record)".
5. **[MED / RT-8]** Add the missing quarantine row (or judge label) for
   the cell-F8 "no coverage" vs thermo-G5/AUDIT-F5 constants-cluster
   split.
6. **[LOW / RT-3, RT-9, RT-10, RT-11]** §3 provenance annotation;
   GAP-31 → LOW; GAP-1 shift-redundancy parenthesis; GAP-17 dead-row
   boundary line.

Root cause of both HIGH items (declared, evidence-backed): the judge
consumed the INTERRUPTED driver-verifier draft; the superseding file's
own header names G4 and G5b as exactly the two verdicts its second pass
changed. Absorption of the map is licensed once repairs 1-2 land; 3-6
ride the same edit.

*Red-team performed single-pass by one agent over all 12 raws + the
record docs; two auxiliary read-only verifications were dispatched but
not consumed (coordinator resume order: checks re-performed inline —
every AC/§6 evidence line above was opened directly by this pass).*
