# Session log 2026-10-01 — F2 CLOSE, session 5 of 6 (census R45)

Plain rules for this log: short sentences, one fact per line, physics before method.

## Opening (R2, R8)
- Phase F2, the closing session. Prompt: `ADVISORY_F2CLOSE_prompt_2026-10-01.md` (checked against the plan's F2 text,
  the derived roadmap, PROGRESS and the F2.ENGINE log; its E4 table is the list of record).
- Consumer: the owner, and the session that opens F3 after F2.
- Exit criteria: the prompt's E1-E4 (decisions on file; CFD-2 written; the methods-freeze page; F2 closed in the
  record or the exact remaining item named with its owner). Owner's order 2026-10-01 ~19:00: "chiudi F2"; with
  P-F2-1 rejected (12:45), the four bell-driver duties are done here, before the closing commit.
- Orchestration: 0 subagents. Budget: one session, no decisive optimisation campaign.
- E1 DONE: the owner's answers of 12:30-12:45 are on file (prompt, section "Owner's answers"; F2.ENGINE log, 12:30).

## Order 0 (d) — X-O32's negative control

### Diagnosis (19:01; `RDE/handoff/plug_2026-09-29/f2close_2026-10-01/o32_foot_probe.py`, log `o32_foot_probe.log`)
- The foot-coefficient (first-order) TOC march at W*, levels r = 1..4, with the typed first-offender abort: EVERY
  level is refused at its FIRST interior cell (cell 0) with certification ratio inf. Not a coarse-level instability.
- Cause, read in the code: the foot unit process takes every coefficient at the segment's foot, including the
  axisymmetric source term delta c^2 v / y. The first interior cell's C- foot is the axis point (y = 0, v = 0):
  0/0 = NaN at every resolution. The production unit process averages its coefficients with the head point
  (y > 0) and never meets the singular quotient.
- So the control could never run on a march that starts from the axis; the "environment-induced" hypothesis of
  carriers:x-o32-negative-control-uncertifiable-on-current-tree is replaced by this mechanism.

### Gates declared BEFORE authoring the re-form (R8)
- Re-form: in the foot unit processes ONLY the factor 1/y of the axisymmetric source is taken at the segment
  midpoint (y_foot + y_head)/2 -- the one term singular at the axis; every characteristic coefficient (the slopes,
  the q and r coefficients, and c^2 v of the source) stays at the foot. The local error stays O(h^2) per step, the
  scheme FIRST order: still the explicit-Euler control, now finite at the axis.
- D-1: the re-formed foot march certifies at every level r = 1..4 (no cell refused), with the axial margin > 0.
- D-2 (the rejector, must FIRE): on those levels the pre-registered h^2 band REJECTS the foot march: the row is
  conclusive and p_hat_fine < 2 - dp_tot (the carrier's own N1 check).
- D-3: S1-S3 unchanged against the 12:50 run (replay = record at every level; the production rows as there).
- Exit: X-O32 VERDICT PASS on this host -> fail= lifted, pass re-stamped; the finding DISCHARGED with this evidence.
  If D-2 does not fire (the measured order of the control is not resolved as below 2), the carrier stays fail= and
  the finding is re-owned with the measurement -- never a moved band.

### Result (d) (19:18; log `RDE/handoff/plug_2026-09-29/f2close_2026-10-01/X-O32_reformed.log`, development run)
- D-1 PASS: the re-formed foot march certifies at every level r = 1..4 (3933 / 15161 / 33695 / 59525 cells), axial
  margin positive (the ladder's assertions hold).
- D-2 PASS (fired): the h^2 band rejects it: p_hat 0.9925 (coarse) / 0.9970 (fine), dp_tot 0.0046, conclusive: rate
  claim killed. The control is first order, as built.
- D-3 PASS: S1-S3 equal the 12:50 run digit for digit (estimator; ideal Q rows; TOC Q_u, J and <dJ/dW, v> rows).
- X-O32's VERDICT stays FAIL, for a reason that is not the control: its production rows are NON-CONCLUSIVE at the
  pre-registered cap 0.5 (TOC J: p_fine 2.5347, dp_tot 0.6704; ideal Q: dp_tot 2.12). This is the S19 row of record,
  owned by the open finding mesh-amr:observed-order-not-at-band-sites (lever: a finer ladder). So: fail= kept (re-dated
  by the record run), the finding carriers:x-o32-negative-control-uncertifiable-on-current-tree DISCHARGED (its duty
  was the control; the control now runs and is rejected).

## Order 0 (c) — the Hessian's symmetry defect (finding driver-nonsmooth:hessian-no-rejector, duty [P-HESSREJ])

### Gates declared BEFORE authoring (R8)
Carrier `validation/hessian_symmetry_audit.py` [X-HSYM] on one S18 segment: the TOC posing of X-O32 S3 (W* = the S18
landing, C^1 quintic closure, the frozen-schedule replay), the driver's own Hessian (forward differences of the exact
adjoint gradient, step dH_j = sqrt(eps) max(|W_j|, 1)).
- The error model, MEASURED not assumed (Nocedal-Wright: a forward difference errs by O(dH) truncation plus
  rounding eps_g / dH): the same columns at dH/2; truncation of the dH column = 2 |H(dH) - H(dH/2)|; rounding
  2 eps_g / dH_j with eps_g = NEWTON_TOL_FACTOR eps N_cells max|g| (the accumulated certification floor, as X-O32's
  noise term). Band_ij = K_RICH (e_ij + e_ji), e = truncation + rounding.
- HS-1: the symmetry defect |H - H^T| BEFORE symmetrising lies inside the band, entrywise.
- HS-2 (the rejector, must FIRE): one column corrupted as a kink-straddling difference would be (scaled by 1.5): the
  defect leaves the band.
- HS-3: directional curvature: for 3 seeded unit directions, d^T H_sym d against the Richardson-extrapolated second
  difference of J along d (steps h and h/2, h = eps^(1/4) scale), inside K_RICH (|S(h) - S(h/2)| + d^T e d).
- HS-4 (a reading, the challenger): the quasi-Newton carry (BFGS from H_sym along a Newton step of declared length
  1e-3) against fresh differences at the new point, both scored by the directional Richardson curvature there.
- Driver: A1_HESSREJ=1 (unset = the code of record, bitwise) measures the half-step columns, counts and REFUSES a
  segment whose Hessian defect leaves the band (nf_events hess_rej; a typed error), never a silent symmetrisation.
- Exit: X-HSYM PASS (HS-1..HS-3, HS-2 firing) -> the finding DISCHARGED for the symmetry-defect band and the
  directional check; the "defect near a flip seam" half re-owned if not measured here.

### Result (c) (19:09; log `RDE/handoff/plug_2026-09-29/f2close_2026-10-01/X-HSYM.log`)
- HS-1 PASS: the driver's Hessian at the S18 landing (n 9, 3964 certified cells): max symmetry defect 2.15e6 against
  |H|max 4.78e8; the largest defect is 0.47 of its band.
- HS-2 PASS (fired): column 6 scaled by 1.5 leaves the band by a factor 106.
- HS-3 PASS: three directional curvatures agree with the Richardson second differences (relative differences 5e-6,
  1e-4, 4e-4; the tolerance, dominated by the gradient's worst-case rounding floor, is loose: 2-5 percent).
- HS-4 (reading): re-run for the printed digits.

## Order 0 (a) — the multipliers (finding constraints:multiplier-rejector-missing, duties [P-IPADJ], [R2'])
Gates written after the code and BEFORE its decisive run (declared ordering), carrier [X-MGOV] stage derive:
- The margin multiplier read in the S24 convention of record (mu = -v, scipy trust-constr T1); an extraction failure
  counted (counters mu_extract_fail), never a silent 0.
- C-1 (the rejector, must FIRE): complementarity tested on the RECORDED S24 stop (res.v +4.8582e4 at the inactive
  margin 0.0731, `validation/s24_multiplier_record.json`) against the derived band K_RICH x the objective's
  certification floor at W* (NEWTON_TOL_FACTOR eps N_cells |J|): |mu m| = 3.55e3 must leave it.
- C-2: a KKT-consistent inactive stop (|mu m| a quarter of the band) passes.
- The old inactive-margin row (mu forced to 0, then tested for 0: a tautology) is removed; the campaign now tests the
  recorded multiplier at every inactive-margin landing.
- L-1 (the [R2'] least-squares re-estimate, Gill-Murray-Wright): on the S18 landing W*, the multipliers of the lip row
  and of the margin row by least squares, residual and cond(R R^T) REPORTED; known-answer v = (2, -3) planted on the
  measured rows recovered to K_RICH eps cond; L-2 (rejector, must FIRE): two parallel rows give a condition number
  above 1/(K_RICH rel_g) (the gradient's relative floor): LICQ degradation flagged.
- Every existing X-MGOV row unchanged; exit: VERDICT PASS -> X-MGOV re-stamped, the finding DISCHARGED for
  [P-IPADJ] and the check rows; the S24 half of [R2'] (the S24 landing's gradients) re-owned if no S24 design record
  exists on this tree.

## Order 0 (b) — the objective domain (finding variational-driver:objective-omits-throat-panel; duties [OBJ-DOM-IMPL], [OBJ-DOM-AB], [OBJ-DOM-REBASE])

### Gates declared BEFORE authoring (R8; before any (b) code: objdom_ab.py was created at 19:30)
- The physics in one line: the bell objective adds up the wall push from the first arc station on; the strip of wall
  between the throat (theta = 0) and that station is left out. Its push is small and fixed in value, but it grows
  with the attachment angle theta_B, so it tilts the optimum.
- [OBJ-DOM-IMPL], in the bell carrier: A1_OBJDOM=A evaluates J_A = J_coded + the throat panel; unset = the coded
  objective, the code of record, bitwise. Rule P-1: (1) the panel pressure is the kernel flow sampled at both ends:
  p(0) at the theta = 0 station = the IVL wall point (plan-frozen, independent of W), p(theta_1) at the first arc
  station; (2) the quadrature is F-1 branch (i): the theta = 0 station prepended to the wall array, the same trapezoid
  as the rest. Engine key unchanged: the panel is a term after the replay; the replay and its plan are untouched.
- Carrier [X-OBJD] `validation/objdom_ab.py`, at W* = the S18 landing (the incumbent of record named by S20's design
  file; the advisory's constants thB 0.2007, n_B 23 are an illustration, not a design of this carrier: declared),
  the C^1 quintic closure, one frozen plan:
  - T-0: the theta = 0 station equals the record's IVL wall point, bitwise; the first arc station lies on the exact
    arc, y(theta_1) = yt + rtd (1 - cos theta_1), at round-off.
  - P-2: dJ/dW under both objectives through the same jitted replay (one plan, no re-record between A and B).
  - F-1(a) (OBJDOM-1(b)): the two gradients differ only in theta_B: on every contour degree of freedom the difference
    is below the march's accumulated floor eps_g = NEWTON_TOL_FACTOR eps N_cells max|g|.
  - F-1(b) (branch (i)): the theta_B component of the difference equals the branch-(i) closed form, with p'(theta_1)
    measured by central differences of the first station's pressure on the frozen replay (independent of the
    adjoint); bar = K_RICH (|pred(h) - pred(h/2)| + eps_g).
  - F-1 rejector (must FIRE): the exact-integral target (c) (no p' term; attained by no implemented rule) misses the
    measured difference by more than the bar: the check can tell the quadrature branches apart.
  - F-2: the tilt in the driver's own coordinates, |dJ_A/dtheta_B - dJ_B/dtheta_B| x Dv_thetaB (Dv measured at W* by
    the driver's Jacobi rule), against 10 gtol (gtol derived at W* by the X-TOCV O3.1 rule). Expected to FIRE (record:
    5.8e2 x). If it does not fire, the adjudication re-opens (declared, never a silent pass).
  - P-3: the driver's TR-SQP under A1_OBJDOM=A from W*, gtol unchanged: status 1 or 2, KKT optimality <= 10 gtol, no
    nonfinite event, the landing certified with its margin audit (as X-TOCV). Reading: the theta_B shift against
    tilt / curvature.
  - P-4 (value axis): J_A - J_B at W* equals the panel's closed form at round-off (discrete identity a.1); the panel
    against its exact-integral estimate (E_trunc declared, a scaling estimate); the panel on the ladder r = 1, 2
    (theta_1 halved) falls as theta_1^2 (ratio 4 within its Richardson bar).
  - The F7 band (S24 branch adjudication) is measured only by X-DEFTW, declared failing on this machine (a GENO case
    missing): its re-measure stays with that finding; the cancellation is argued, not measured.
  - Every recorded bell verdict re-read on J_A: one table (verdict; what it consumes: value, gradient or Pa; status).
- Exit: X-OBJD PASS -> the finding DISCHARGED for F-1, F-2, P-3, P-4; [OBJ-DOM-IMPL] landed as an opt-in; the switch of
  the default to J_A with the re-baseline of the recorded bell designs named with its owner.
- (c), driver half, declared now: A1_HESSREJ=1 measures the half-step columns at every segment base and raises the
  typed HessianDefectError when the symmetry defect leaves the band (counter hess_rej in the message); unset = the
  code of record, bitwise. HS-5 in X-HSYM: one driver segment at W* with the doctored column (x corrupt_scale) is
  REFUSED by the driver (must fire); the same segment undoctored proceeds (positive control).
- Cost declared: the bell carrier is imported by 35 on-demand checks; any edit makes every one of them older than the
  file (the claims lint, day resolution). The record runs therefore happen in one batch after the edit, all on the
  date of the closing commit; the runs before it are development runs.

### Result (a) (19:15; log `RDE/handoff/plug_2026-09-29/f2close_2026-10-01/X-MGOV.log`, development run): VERDICT PASS
- Every existing X-MGOV row passes as before (D1-D4, the S1/A37 dual clause and its rejector).
- C-1 PASS (fired): the recorded S24 stop, |mu m| = 3.551e3 against the complementarity band 9.774e-3 (K_RICH x the
  objective's certification floor at W*, J 2.776e7, 3964 cells): violated by 3.6e5 x. The S24 stop was not a KKT point
  for its margin multiplier; the interior-point reading of record (step 13 (d) of the S24 log) is confirmed as an
  artefact, now by a check row and not by hand.
- C-2 PASS: a KKT-consistent inactive stop (|mu m| 2.4e-3) passes.
- L-1 (reading) at the S18 landing W*: lip multiplier +1.054906e7, residual 2.36e-4 of |grad f| (lip row alone and
  with the margin row); margin multiplier mu = -32.8, i.e. zero to the scale of the lip row; cond(R R^T) 2.97, far below
  the LICQ limit 1/(K_RICH rel_g) = 2.84e9.
- L-1 known answer: v = (2, -3) planted on the measured rows recovered to 3.6e-16. L-2 PASS (fired): two parallel rows
  give cond 5.1e16, flagged.
- The S24 half of [R2'] is RE-OWNED: no S24 landing design is on file on this tree (the S24 stop exists only as log
  text, recorded in `validation/s24_multiplier_record.json`); owner = the next bell-driver walk that writes its landing
  design (the campaign now tests the recorded multiplier at every inactive-margin landing).
- Finding constraints:multiplier-rejector-missing: DISCHARGED for the check rows ([P-IPADJ]: band, counter, rejector
  fired on the record) and the S18 half of [R2']; the S24 half re-owned as above.

### Result (c), the driver half (19:35; log `RDE/handoff/plug_2026-09-29/f2close_2026-10-01/X-HSYM_dev.log`, development run): HS-5 FAILS
- HS-1..HS-3 as at 19:09; HS-4 digits: the BFGS carry misses the directional curvature by 6.8e-4 / 3.5e-4 / 9.6e-4
  (relative), fresh differences by 3.6e-4 / 1.3e-4 / 3.7e-4: fresh differences win, both are fine here.
- HS-5 control PASS: the undoctored driver segment passes its own check with max defect/band 0.471 (the same number as
  HS-1: the driver measures what the carrier measures).
- HS-5 rejector FAILS (did not fire): the driver segment with column 6 x 1.5 is NOT refused (max defect/band 0.183).
- Why, in one line: the band takes the truncation from the half-step columns, and a kink changes those columns too.
  A kink in the gradient at distance delta <= dH along column j moves the dH column by Dg/dH and the dH/2 column by
  2 Dg/dH (delta <= dH/2) or by 0 (dH/2 < delta <= dH): the measured truncation 2|H1 - H2| is then 2 Dg/dH, the band
  >= K_RICH 2 Dg/dH = 8 Dg/dH, the defect <= Dg/dH. The ratio stays <= 1/(2 K_RICH) = 1/8 for ANY kink (measured 0.18
  with the noise). The doctor of HS-5 scales the dH column only: a kink in (dH/2, dH]. HS-2 fired because its band was
  taken BEFORE the corruption, i.e. both steps equally wrong: a biased column, not a kink.
- Measured on the way: the half-step change of the columns is ~1e6 (|H| 4.8e8), i.e. a gradient noise ~0.01 J-units at
  the driver's step, ten times the certification-floor model eps_g 9.3e-4. A likely source: the C^1 thermodynamic
  closure (its second derivative jumps at the table knots; thousands of cells cross knots in any step): small kinks
  everywhere, by design. A kink rejector therefore needs a noise scale that the kink cannot move (an outlier rule over
  the columns, or the directional check against J values at a step above the noise with a band free of the half-step
  estimate). Not built here.
- So: the symmetry check rejects a BIASED column (a gradient path wrong at both steps); it cannot reject a kink. X-HSYM
  is declared FAILING on HS-5, owned by finding driver-nonsmooth:hessian-no-rejector, which stays OPEN for the kink
  half with this mechanism.
- Gate HS-5b, declared before its run (the run started 19:39): the same driver segment with column 6 x 1.5 at BOTH steps (a biased
  column) must be REFUSED by the driver. It shows the hook works for what it can see; it does not replace HS-5.

### Result (b) (19:39; log `RDE/handoff/plug_2026-09-29/f2close_2026-10-01/X-OBJD_dev.log`, development run): P-3 FAILS
- T-0 PASS: the theta = 0 station is the record's IVL wall point, bitwise; the first arc station is on the exact arc
  (difference 0). T-1 PASS: the driver's switch returns thrust_J unset and thrust_J_A under A1_OBJDOM=A, bitwise.
- The panel at the S18 landing: J_A - J_B = 1149.3 J-units = 4.1e-5 of J (J_B 2.776168784978e7, J_A 2.776283710724e7).
- F-1(a) PASS: the gradients differ ONLY in theta_B; on the 8 contour components the difference is exactly 0.
- F-1(b) PASS: the theta_B component, 8425.1616353 J-units/rad, equals the branch-(i) closed form 8425.1616355 (diff
  1.9e-7, bar 3.7e-3; p'(theta_1)/p = -2.39 per rad by central differences: the gas accelerates along the arc).
- F-1 rejector PASS (fired): the exact-integral target (c), 8381.19, misses by 44 = 1.2e4 bars. The quadrature term is
  0.5 percent of the tilt: the check tells the rules apart.
- F-2 PASS (fired, as the record expected): tilt 8425 J-units/rad, x Dv_thetaB 6.12 (the driver's Jacobi rule at W*) =
  5.16e4 against 10 gtol = 1.055 (gtol 0.1055 by the X-TOCV rule at W*): 4.9e4 x. Fallback reading 8.0e3 x (> 6). The
  adjudication of record stands: the tilt cannot be tolerated into the KKT band; fix-A is the right objective.
- P-3 FAILS: the driver's TR-SQP under J_A from W* ran its 12-segment cap: 12 segments, 12 wall-search decision flips
  (one per segment), 25 iterations, 163 evaluations, 301 s; KKT 1.4e3 to 2.1e4 against 10 gtol 1.055; J flat to
  +-3 J-units. Every accepted step re-records a different plan, so stationarity under J_A is not re-earned at the
  unchanged gtol. The landing is certified (worst 0.17, margin 0.48 >= 0.12 m/s). Physics: the J_A optimum is
  ~7e-4 rad (0.04 degree) of attachment angle away and worth ~ tilt^2 / (2 |H_00|) ~ 3 J-units = 1e-7 of J; the
  stationarity test is at 4e-9 of J. The bell driver's verdicts are sharper than its decisions are stable.
- P-4 PASS (identity a.1): J_A - J_B equals the panel's closed form to 1.8e-9 at r = 1 (1149.257) and r = 2 (n_B 63,
  297.987). Readings: the panel falls as theta_1^2 (ratio 3.857 against (63/32)^2 = 3.876; the rest is the end-pressure
  ratio 0.995). Between r = 1 and 2 the coded J changes by -1007 and J_A by -1858: the missing panel hid 46 percent of
  the level change of the objective (the panel's own change is -851).
- X-OBJD is declared FAILING on P-3, owned by the finding variational-driver:objective-omits-throat-panel, which stays
  OPEN for P-3 (stationarity under J_A blocked by decision flips) and for the switch of the default with the re-baseline
  of the other recorded bell designs.

### Every recorded bell verdict, re-read on J_A
| verdict (carrier) | what it consumes | on J_A |
|---|---|---|
| X-TOCV O1 / O3.1 (the gradient identity) | the gradient of the implemented J | unchanged in kind: the adjoint is exact for J_A too (F-1: the difference IS the panel's derivative) |
| X-TOCV OPT, O3 transversality at the S18 W* (KKT 7.7e-2 <= gtol 0.1156) | stationarity | MOVES: the tilt is 4.9e4 x the acceptance; NOT re-earned (P-3) |
| X-O33B (the O3.3 bench at W*) | characteristic compatibility on the field; rows that use dJ/dtheta_B | the field rows unchanged; any row using dJ/dtheta_B moves with the tilt |
| X-O32 (the J row of the ladder) | value differences between levels | changes: level difference -1007 (coded) against -1858 (J_A) at r = 1-2; the row is NON-CONCLUSIVE either way |
| X-AKNO (S20 adaptive knots; failing on record) | values per class, stationarity per class | values shift by the panel (4e-5 of J); stationarity moves as X-TOCV's |
| X-MGOV, X-TBAK (the margin) | the margin field, not J | unchanged |
| X-HSYM (the Hessian) | second differences of J | one extra term on the theta_B diagonal only; the symmetry defect unchanged |
| X-CDKAT, X-LOCD (the cell check) | certification, not J | unchanged |
| X-DEFTW (S24 F-branches, incl. the F7 band) | differences at the same cfg and theta_B | the panel cancels (same theta_B both sides) -- argued; X-DEFTW cannot run here (GENO case missing) |
| X-SPDB (speed) | timings | unchanged |
| the plug / two-wall line (X-TWOP, X-RDET, X-PSPL, ...) | their own objectives | not the bell objective; they import only the spline helpers |
- HS-5b PASS (19:41, `X-HSYM_dev.log`): the column wrong at both steps is refused by the driver (10 entries out of
  the band, max defect/band 103). HS-5 FAIL again (0.183), as derived. X-HSYM VERDICT FAIL on HS-5: declared failing,
  owned by driver-nonsmooth:hessian-no-rejector (kink half open).

## Orders 1-2 — CFD-2 and the methods freeze (20:00)
- E2: `validation/CFD2_paired_demo_2026-10-01.md` (one page): five plugs and the shrouded pair, each judged by the tool
  over the 12 phases, 2-D Euler per phase and 3-D Euler in the wave frame; the bands (tool against 2-D +0.10 to +0.14
  percent; frozen against rotating -0.38 to -0.55 percent, the offset cancelling between designs to 0.07 percent, 0.14 in
  the worst case); what is shown (the ranking survives every judge; the CFD catches the tool's undulation gain) and what
  is not (friction, heat, burning, the base, the chamber, optimality, an experiment). The matched pairs of the program's
  comparison (B24 against Sa24, J12 against Sj) are added when judged.
- E3: `validation/F2_methods_freeze_2026-10-01.md`: one section per method (march, gradient, certificates, monitors,
  family, judges) with its checks and dates, the M0 half checked (F2a block (1)-(6), Lemma B, the F2-B0 certificate
  block), and what is open with its finding.

## Order 3 — the close (E4)
- D6: dated note 2026-10-02, F2 CLOSED with named residuals (each with an owner): the layered fold margin and the GENO
  layered twin (PARKED); X-SWAV and X-ADMA failing on the THOR data, X-FRES's non-discriminating rejector; the two bell
  halves of today (X-HSYM kink, X-OBJD P-3 and the default switch); the 0.2 bar wave-frame pilot; the 406 far field
  (MOSE_open, the owner's code); CFD-1 (after F2).
- PROGRESS: ORA, NEXT (the program's comparison, then F3), census R45 CONSUMED, session rows.
- Roadmap: `tools/roadmap_derive.py` step status F2.ENGINE / F2.M-RED / F2.CFD-2 CLOSED 2026-10-02; the consumed F2
  steps carry their open objects to the next open step, F3.TWIN (F3.RK1 and F3.PLUG are closed on the plug line);
  B-CFD1 re-homed to F3.TWIN (owner's decision 4). Derived again: 16 steps; coverage lint PASS; open findings 241 (61
  critical: the two discharged today are off the list).
- Registries: findings (x-o32 control and the multipliers DISCHARGED; the Hessian and the objective domain re-owned with
  today's measurements); claims rows X-HSYM and X-OBJD (both declared failing, owned); flags A1_OBJDOM and A1_HESSREJ;
  the advisory index (this log, the CFD-2 page, the freeze page; the F2-close prompt CONSUMED).
- Lints on the tree before the record runs: numeric PASS (the driver's literal baseline ratcheted 31 -> 29: the IVL
  nudge named once), advisory index PASS, roadmap PASS, glossary and findings at their environmental reds (missing
  literature PDFs; the H4 derive artefact already stale at HEAD, X-DEFTW cannot run here), claims lint red only for the
  uncommitted closure files (cleared by the commit).

## The record runs (2026-10-02, after midnight)
The bell carrier is imported by 35 on-demand checks; the edits of today age all of them (and X-TBAK, X-SPDB through
margin_governor.py). They run again in four lanes from 00:00 (`RDE/handoff/plug_2026-09-29/f2close_2026-10-01/
run_cascade.sh`, settings of record as on 09-30 and 10-01; logs `cascade/`, summary `cascade_summary.txt`), so that every
pass date equals the date of the closing commit. The development runs of 10-01 are not the record.

## The program's comparison, evening of 10-01 (the design WITH the 12 phases against the classical mean-state design)
Owner's correction of the afternoon: same optimiser, same start (Rao), same rules, same budget; the mean-state walk is the control.
- Mean-state control, plug (walk `_plug_contest/SDT/AcowlB_sdt_fromRao`, 24 segments in all, design
  `RDE/handoff/plug_2026-09-29/sdt/design_sqpA24_sdt.json`, Sa24SDT): tool 1.425302 (mean state) / 1.427734 (12 phases);
  2-D level c over the 12 phases 1.425752 (mean state 1.423159; 4 phases unsteady, time scatter 1.9e-4); 3-D wave frame
  1.417995 / 1.417983 at 0.5 / 1.0 ms. Over Rao: +0.92 / +0.91 / +0.77 percent (tool / 2-D / 3-D). The frozen-to-rotating
  offset is -0.55 percent here against -0.38 to -0.45 for the four plugs of 09-30: the 3-D gain is 0.14 percent below
  the frozen one. Tip 39.27 mm (Rao 41.82).
- The 12-phase walk B (`BcowlB_sdt_fromRao`, the same start, budget 24 segments) at segment 13: 1.421589 over the 12
  phases (the A walk at its segment 13: 1.419454 at the mean state, ~1.4219 over the 12 phases): the two walks climb at
  the same rate per segment. Judged when it ends (`sdt/judge_B24.log`).
- Plug + cowl with the 12 phases (J12, `BcowlB_sdt_joint_fromSb`, from the 12-phase plug at segment 10, 10 segments):
  still in its first segment after an hour (27 variables x 12 phases); judged when it ends (`sdt/judge_J12.log`).
- Shrouded, smooth walls (cap 0.65, 133 mm; tool only, no CFD: gains this small are not worth a run, the owner's rule):
  the 12-phase walk (`shroud_cap065_smooth_B`, 5 smooth modes after the kernel arcs) 1.535034 -> 1.536326 over the 12
  phases (+0.084 percent; lip 1.3313 -> 1.3780, exit area ratio 4.69 -> 5.03; stopped by its resolution rule, |grad|
  0.1); the free-kernel mean-state walk (`shroud_cap065_smoothK`) 1.528976 -> 1.529293 at the mean state (+0.021
  percent); the mean-state smooth walk of the afternoon +0.04 percent over the 12 phases. The cut ideal nozzle stays
  within 0.1 percent of every smooth design found.
- READ 22:15 (both walks ended by budget, |grad| 0.44-0.53: lower bounds). Plug with the 12 phases (B24, 24 segments,
  `sdt/design_sqpB24_sdt.json`): 1.432445 over the 12 phases = +1.25 percent over Rao, against +0.92 for the mean-state
  control at the same budget (+0.33 percent for the phases, tool only); tip 38.19 mm (control 39.27, Rao 41.82): the
  12-phase plug expands more. Plug + cowl with the 12 phases (J12, 10 + 10 segments, `sdt/design_sqpJ12_sdt.json`):
  1.424022 = +0.66 percent, against +0.81 for the mean-state pair SjSDT (10 + 10): not decisive -- J12 started from the
  less advanced 12-phase plug (+0.36 against +0.45 percent at segment 10) and stalled two segments on the class limit;
  lip 67.06 mm (SjSDT 67.25).
- Owner, 22:20: no 3-D runs now. The B24 judge chain was stopped before it built its case (PID read from ps); the J12
  chain had submitted a broken 3-D job (its walls were not in the walls file: the chain adds only A24/B24 to its list):
  job 303751 ended in 25 s on a missing mesh, its cluster copy removed by literal path; the J12 walls, mesh and case were
  rebuilt (`RDE/Nozzle/plug_walls_sdt_J12.json`) and NOT submitted. The 2-D per phase on the 12-phase designs waits for
  the owner. The tool's 12-phase readings stand alone for B24 and J12.
- Owner, 22:25: "committa". The closing commit is made now, before the record runs: the claims lint is red at this commit
  ONLY for the age of the 35 checks importing the bell carrier (their stamps 2026-09-30 precede the carrier's commit);
  the record runs start at 00:00 and their stamps (2026-10-02) land in the next commit.
- 2026-10-05, the stamps: the four lanes ran 2026-10-02 00:00-02:11, every result as expected (no unexpected failure).
  30 rows stamped pass=2026-10-02 (29 run directly + X-IVLT through X-TPOS, the 09-30 rule, X-TPOS log equal to its
  record except timings); X-CHTW 8/9, X-HMPH 4/6, X-PAKN 12/14 fail the same rows as their records; X-HSYM, X-OBJD,
  X-O32 fail=2026-10-02 for their declared reasons. X-IVLT was missing from the cascade lists (27 stale rows, 26
  scheduled): covered by X-TPOS. Claims lint 0 violations, suite 17/24 (the 7 environmental reds of s2).
