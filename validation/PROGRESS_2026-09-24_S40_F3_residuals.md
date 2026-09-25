# S40 — The F3 residuals on the owner's word: the finder at the nominal ambient, the two-wall stretch and its DUTY-11, the X-PTRN row, the truncation pointer (2026-09-24/25 night, [F3/A1])

Owner's direction after the S39 closure: "facciamo (1) e (2). Per il troncamento (3), il modello
non è una scelta banale, abbiamo visto che vari modelli non vanno d'accordo (tra l'altro abbiamo
una nuova reference con la tesi di Fiore in geno literature) perciò la scelta non è banale. Quella
riga (4) se è utile al progetto la scriviamo." Read as: run residual R-F3-1 (the tournament's
finder campaign at the nominal ambient from the far start, the second and last decisive campaign
D6 ISS-4 allows the plug instance) and R-F3-2 (the two-wall stretch with its entry duty DUTY-11);
leave R-F3-3 (the truncation / T-GB shape falsifier) OPEN with the new reference recorded; coin
R-F3-4 (the X-PTRN registry row) because the finder results need a row to live in. F3 stays
CLOSED (S39): this is residual work after the phase, no session counter. Session mose-a1, main
tree `rde-nozzle-program`. Communication in Italian; this log in English (CLAUDE.md).

## 1. R-F3-1: the finder at the nominal ambient, class in region R -- NEGATIVE within budget
Carrier `validation/a1_plug_tournament.py` [X-PTRN], additive S40 mode `PTRN_CLASS=R` (docstring
paragraph "CLASS IN REGION R"): the fold class graded over Humphreys' region R (the S34
criterion) instead of S29's bucket, start E added (the square-root ramp toward the planar
streamline) and the FINDER readings F-1 / F-2 for every non-A start.

Derive of record in R mode (81,41), `_plug_tournament/k81n41_R/run_derive_R_2026-09-24.log`,
12/12: m_ref 0.0871 over the member's 426 R cells, floors 0.0435 / 0.0218 / 0.0109 / 0.0054, rho
4448.9, gap 1.361e-3, h* 2.442e-2 m -> tr0 6.106e-3 m, radius floor 1.526e-3 m. MEASURED FIRST: the
S29 rejector R-G1 (a 2 deg compression corner at the foot) FAILED as a rejector in R mode (KS in R
+0.0856, feasible) because its fold lies above the exit characteristic, outside R, where the thrust
does not depend on it (first log kept as `run_derive_R_v1_2026-09-24.log`, 11/12); the R
criterion's rejector is R-G1R, the 1.5-percent alternating perturbation, which folds INSIDE R (KS
-0.7300) and is infeasible at every floor; R-G1 is reported, not graded, in R mode.

Campaign `PSPL_FAN=axi PTRN_K=81 PTRN_N=41 PTRN_CLASS=R A1_PTRN_STAGE=campaign PTRN_SEGS=24
PTRN_ITERS=8 PTRN_STARTS=4 PSPL_BACKTRACK=4`, `PTRN_ONLY=C` and `=E` in parallel, launched
2026-09-24 23:46 (A skipped: its value is certified by [X-OWNM]; B folds in R). Logs
`run_campaign_R_{C,E}_2026-09-24.log`, reports `campaign_s24_i8_st4_{C,E}.json`:

| start | wall distance to the member, start -> landing | J gap to the member, start -> landing | landing class | F-1 shape | F-2 value (paired) | wall-clock |
|---|---|---|---|---|---|---|
| C (ramp to the planar streamline) | 0.841 -> 0.836 m | -4.441e5 -> -2.930e5 N | in R, min cell +0.0587, not active | FAIL (band 0.0122 m) | FAIL (|gap| 2.93e5 > 1.54e5) | 4280 s |
| E (square-root ramp) | 0.841 -> 0.850 m | -3.437e5 -> -1.756e5 N | in R, min cell +0.0533, not active | FAIL | PASS, UNSOUND (see below) | 4217 s |

Totals 3/6 (C) and 4/6 (E): C-1 certified, C-2 finite, C-3 in class PASS; C-4 "no loss to the
incumbent" FAIL; F-1 FAIL. The walks recover 34 percent (C) and 49 percent (E) of the thrust gap
but do not move toward the member in shape, and they do not coincide with each other (1.17e5 N
apart). THE STALL, read in the logs: both climb until the base sits in class with about 0.015
of slack above the floor, then every trial -- the TR step, the backtracked halves, the projected
ascent -- lands in a deep fold inside R (KS - mu0 -0.83 for C), the radius falls to its floor
1.526e-3 m and the walk stops (C from segment 11, E from segment 12; 43 backtracking probes each,
2+1 and 1+1 accepted). The fold cliff lies closer than the smallest step the driver treats as a
measurement. F-2 of E is NOT a certificate: its paired band comes from the gap's change between
(81,41) and (161,81), and the MEMBER's march at (161,81) is not certified in this reading (cert
1.320 > 1; the landing's is 0.038), so the doubled rung the band rests on is not a certified
number.
VERDICT: the finder test at the nominal ambient is NEGATIVE within this budget -- the direct
machinery, class in region R, does not find the plug optimum from a far start; it stalls at a fold
cliff 0.15-0.25 percent of J below the member. The plug optimum of record stays certified in VALUE
only ([X-OWNM]) plus the re-obtentions from near starts; no finder claim is made. This spends the
second and last decisive campaign D6 ISS-4 allows the plug instance (wall-clock 71 min per
start, the two in parallel).

## 2. R-F3-2: the two-wall design on Migdal's pair, and what it took to make the optimiser work
New carrier `validation/a1_twowall.py` + `twowall_cases.json` [X-TWOP]: both walls of Migdal's
perfect annular nozzle (the [X-MGDL] posing, GENO nozzle_type 9, A_e/A_i 4, (140,31)) as design
variables of the certified march, the vacuum C_F in jax (start points closing the polylines),
the record driver `a1_plug_spline_opt.run_trsqp` through the posing hooks. The march needed one
additive change: `a1_plug_march.py` now accepts a TRACED shroud in the replay (a concrete shroud
keeps the numpy path; the exact-channel stage of [X-TWMU] re-run into scratch reproduces its record
field by field, 6/6), plus an opt-in per-cell margin output for censuses (off by default).

### 2.1 First posing (8 knots per wall, free start): the machinery right, the optimiser wrong
Stage derive (`_twowall/run_derive_m8_2026-09-25.log`): G-1 the reference (GENO's walls at the
knots) certified, C_F 1.579580 vs 1-D 1.579594; G-2 replay = record to the last digit; G-3 the
adjoint of both walls against the FROZEN-schedule difference ladder (the practice of record, steps
1e-4 .. 1e-6: the driver's 1e-6 .. 1e-8 sit below this replay's measured noise, probe
`RDE/handoff/f3_2026-09-24/twop_fd_probe.log`) PASS -- the record differences are a reading: at
1e-4 the record already re-takes its wall-foot and shroud-segment decisions. MEASURED FIRST, then
corrected: a 1-percent alternating "stationarity control" was uncertified (cert 7.5e15) and was
dropped; the pointwise AD Hessian was unfit (section 3).
The walks WITHOUT a class constraint (12 x 8, backtracking): from the reference C_F climbs
1.579580 -> 1.581194, ABOVE the 1-D ideal, the walls 5.5 / 11 mm off Migdal's, the gradient never
falling (0.19 .. 0.31); from the chord (79 / 62 mm off) C_F 1.571502 -> 1.574110 with no motion in
shape, stopped at the radius floor. Diagnosis (probes in `RDE/handoff/f3_2026-09-25/`):
- the whole-net fold census (the [X-PMRG] cell margin over wedge + internal channel + after the
  lip): GENO's exact walls on the twin's stations have NO negative cell (min +0.0113); the 8-knot
  reference has 1006 after the lip (strips one cell wide along both families: rows 32-40, the first
  shroud reflections created in the start-up wedge, pass through one point -- a C- coalescence --
  and the cells beyond pair with the backward root); the unconstrained landing adds 72 in the
  internal channel: THE OPTIMISER HARVESTED FOLDS, as the single-wall plug did in S21-S23;
- the cause is the REPRESENTATION: Migdal's walls are a circular-arc kernel (dtheta/dx ~5.1 rad/m)
  ending in a curvature jump (shroud x 0.0646, plug x 0.0729, measured on GENO's walls), and a
  cubic spline rings there (angle error 3.6 deg at 8 knots; negative cells 1006 / 794 / 404 / 189 /
  171 / 0 at m = 8 / 12 / 16 / 24 / 32 / 40, `twop_rep_census*.log`);
- at 40 knots the reference is fold-free but the gradient sits 94 percent on the first knot of
  each wall and two knots at the arc's end: a step of 0.33 mm along it bumps one knot and folds
  the net (the free-kernel posing's class stage, `run_class_m40_free_2026-09-25.log`, 3/4);
- and the problem itself is DEGENERATE with a free kernel: every perfect nozzle between the pinned
  ends attains the same 1-D thrust whatever its initial expansion, so the two-wall optimum is a
  FAMILY (DUTY-11's near-nullspace, in its physical form).

### 2.2 The posing that works: the kernel as data, the fold class, a start-local radius
- KERNEL POSING (twowall_cases.json posing.kernel): GENO's arcs up to their curvature jump are data;
  each wall downstream is a spline clamped to the arc-end point and slope through 12 knots (last
  pinned). Measured: representation error 2.7e-4 / 1.9e-4 m, the reference fold-free with the
  exact walls' worst margin +0.0113, C_F 1.579881. With the kernel fixed, the optimum is the
  straightening contour of THIS kernel -- an instrument posing, declared (a tournament of kernels
  is another problem).
- THE FOLD CLASS on two walls (stage class, `run_class_2026-09-25.log`, 3/3): the margin over the
  whole net, m_ref +0.0113, floors m_ref/2^k, rho 50926, gap 1.77e-4; C-R the unconstrained
  ascent's first move (0.33 mm along +grad J) is infeasible at every floor (KS -0.365); reading:
  the 8-knot unconstrained landing on these knots folds (KS -0.998). Re-run on the file as
  committed: every field identical.
- DUTY-11 on the kernel posing (stage derive, `run_derive_kernel_2026-09-25.log`, 6/6): the
  functional is smooth now -- the decisions' J jump at 1 mm is 1.26e-8 (it was 1.8e-4 at 8 knots);
  the secant Hessian (1 mm, checked at 0.1 mm; asymmetry 0.04, scale change 0.28, floor 1.12) has
  eigenvalues 0.80 .. 146, every one confirmed by second differences of the frozen replay and of the
  record; the two walls DECOUPLE (every eigen-direction is a pure plug or a pure shroud mode): no
  channel-translation mode; ONE near-null direction (a plug mode, 0.80 below the floor), 21
  identifiable with shape bands 1.3e-5 .. 1.3e-4 m. The Newton step from the reference in the
  identifiable subspace is 0.22 mm for a predicted +2.3e-6 of C_F. DUTY-11 disposition: the
  near-nullspace of the two-wall problem is the kernel family; fixing the kernel removes it; what
  remains is identifiable except one soft plug mode (reported, never graded).
- THE WALKS, class-constrained, radius from the class scale along +grad J at the walk's OWN start
  (at the reference the gradient is dominated by knot-scale zig-zags that fold within 0.33 mm):
  from the reference (A, `run_walk_A_2026-09-25.log`, 10 records, 84 min) C_F 1.579880616 ->
  1.579883029 (+2.4e-6, the predicted Newton gain), |grad| 2.3e-2 -> 4.9e-5, in class, the walls
  0.22 / 0.24 mm from the reference: the constrained optimiser converges to the discrete optimum
  next to Migdal's pair. The generic start: the chord from the arc ends folds at every ramp (even a
  quarter of the way, KS -0.63); the cubic Hermite from the arc ends to the pinned ends with an
  axial exit (posing data only) folds in full (539 cells, 1.2 cm off) and is in class halfway (6 /
  5 mm off, C_F -3.0e-4): around Migdal's straightening the fold-free class is narrow -- a generic
  contour 1 cm off carries coalescing compressions (an embedded shock, which a characteristic march
  excludes). The Euclidean walk from that start (radius 0.117 mm) climbed 4e-5 in 5 segments and
  was killed at 04:04 by a machine-wide allocation failure (log kept,
  `run_walk_H_euclid_oom_2026-09-25.log`).
- THE NEWTON METRIC (walk stage, TWOP_METRIC=start; the `Metric` adapter of the carrier): the walk
  runs in z with W = W_s + T z, T from the secant Hessian AT ITS OWN START (1 mm, 22 x 22, 1393 s;
  eigenvalues 0.82 .. 146, floored at K_RICH x its asymmetry 0.23; no reference information). Along
  the Newton direction the class holds to 10.6 mm and gives +2.63e-4 of C_F -- the class scale is
  15 mm there against 0.47 mm along the raw gradient: the raw gradient's knot-scale zig-zags were
  the obstacle, not the class. From the Hermite start (`run_walk_HN_2026-09-25.log`, 12 records,
  117 min): C_F 1.579581108 -> 1.579879 at segment 1 -> 1.579883030 at segment 2, |grad| 2.5e-2 ->
  2.2e-5, in class, the walls 0.23 / 0.24 mm from the reference (they started 5.9 / 4.6 mm off).
- RE-1 GRADE (stage grade, `run_grade_2026-09-25.log`, 3/3): RE-0 both landings certified and in
  class; RE-1 VALUE |C_F(HN) - C_F(A)| 5.1e-10 <= K_RICH x delta 5.0e-8 (the start was 3.0e-4
  below); RE-1 SHAPE every one of the 21 identifiable directions within 0.01 of its band (the
  non-identifiable plug mode came back too, 3.2e-5 from 1.1e-2); the two landings 13 um apart on
  the plug and 0.3 um on the shroud. THE TWO-WALL OPTIMISER RE-OBTAINS MIGDAL'S STRAIGHTENING FROM
  A GENERIC START (declared scope: the kernel posing -- the initial arcs as data, 12 + 12 knots,
  (140,31), vacuum C_F, the lip and the tip pinned).
- THE START LINE IS NOT THE CAUSE (the owner's question, probe `twop_startline_probe.log`): GENO's
  exact walls give NO folded cell at every start-up wedge density (30 / 16 / 11 / 6 columns) and at
  N 61; the 8-knot spline folds at all of them (1006 / 591 / 399 / 265, and 1949 at N 61 with the
  same depth -0.61): the fold belongs to the wall shape. Two start-up facts recorded: the wedge
  packs the first 30 shroud reflections into x < 0.23 m (8 mm apart against 30 mm downstream) and
  the spline's worst angle error (x ~0.066) falls inside it; and thinning the wedge is not free --
  with the exact walls C_F rises to 1.5806 / 1.5813 / 1.5866 at 16 / 11 / 6 columns against the
  1-D 1.579594 (the skipped rows partner with the start line), so the start-up keeps one column per
  row.
- Figures (confirmation, generators in `RDE/handoff/f3_2026-09-25/`): `_twowall/figs/
  20_twowall_optimizer.png` (twop_fig.py), `_twowall/figs/21_kernel_posing.png` (twop_kernel_fig.py).
- NOT DONE, the owner's next question (2026-09-25): the kernel and the ends as design variables
  ("far decidere all'ottimizzatore" the initial stretch; how the plug end and the shroud end are
  decided). The kernel posing is the Migdal confirmation; the design posing needs the arcs as
  variables, an objective at the operating ambient, the constraints that fix the ends, and the
  march's external expansion after the lip -- findings row twowall:design-posing-open.

## 3. A defect of record found on the way: the pointwise AD Hessian
DUTY-11 asked for the two-wall Hessian; `jax.hessian` of the replayed march (forward mode over the
cell solver's custom_vjp reverse, the instrument of `rao1961_sqp_return.spectrum_at`) came back
30 percent asymmetric on the two-wall posing, and it is NOT the functional's curvature:
- on the two-wall posing, the first-shroud-knot diagonal reads -404 by `jax.hessian`, -1195 / -1214
  by central differences of the exact reverse gradient on the frozen record at 1e-5 / 1e-6, and
  -92184 when the cells' forward tangent is made exactly implicit (a zero-valued correction
  z + (w - sg(w)), w = -sg(J)^-1 r, that keeps the thrust and the gradient BIT-IDENTICAL -- scratch
  experiment): near-singular cells (the start-up wedge's crowding) dominate any POINTWISE second
  derivative there;
- a one-cell test is exact (jax.hessian against the gradient's differences 1e-10, symmetric
  1e-13), so the error enters through the march, not through the solver rule alone; mechanism
  NOT isolated beyond that (declared);
- on the S37 walk world ([X-RAOPO]) the audit probe `RDE/handoff/f3_2026-09-24/hess_audit_raopo.py`
  (log beside it) rebuilt the spectrum of record exactly (asymmetry 5.8e-2 relative) and compared
  it with the SECANT spectrum (central differences of the exact gradient at 1 mm and 0.1 mm,
  asymmetry 4.7e-4, verified by second differences of J to 0.2 percent, the two scales within
  0.5 percent): every AD eigenvalue is 16-27 percent LOW. Rebuilt with the carrier's own band
  formulas, the landings of record move from 0.20 / 0.48 to 0.22 / 0.57 of band and the
  coincidence from 0.38 to 0.46: [X-RAOPO]'s verdict HOLDS. [X-RAOSQ] v3 and [X-OWS3] were not
  re-measured: their returns sit at 0.07 and 0.19 of band, inside by margin (a band 27 percent
  narrower keeps them under 0.3) -- inferred, declared.
Instrument of the two-wall carrier: the secant Hessian (G-5), verified by second differences of J
(G-5a); the pointwise AD Hessian is kept as a reading. Findings row
numerics:ad-hessian-forward-over-custom-vjp (owner: the next session that runs spectrum_at).

## 4. R-F3-4: the X-PTRN row, coined
The row the S30 log announced and never wrote is coined in this session's second commit: kind
carrier, `ondemand: "env=jax+geno; pass=2026-09-25; suite=none"` (its oracle reads GENO's member),
doc = this log, proof = `validation/a1_plug_tournament.py`. Its statement carries the derives of
record (bucket 10/10 at (81,41) and (161,81), S30; region R 12/12 at (81,41), S40), the member's
campaign (S30: no resolved gain, the foot knot's discretisation) and the finder's NEGATIVE result
at the nominal ambient (section 1). The pass-of-record date is the re-run of the region-R derive
on the committed carrier (2026-09-25, section 7), so the staleness link binds to a run of the code
as committed. Findings row f3-exit:x-ptrn-registry-row-missing DISCHARGED.
Pass of record, measured: the region-R derive re-run on the committed carrier (6af2076) is 12/12
and its derive.json equals the record field by field (57 fields; only the wall-clock differs), log
`_plug_tournament/k81n41_R/run_derive_R_rerun_committed_2026-09-25.log`. Second commit: the rows
X-PTRN and X-TWOP; claims lint PASS, both rows fresh in the on-demand staleness check.

## 5. The truncation residual (R-F3-3) stays open; the new reference
The owner's word: the base-pressure model is not a trivial choice, the classical members disagree
(measured S30 section 6.4: at every length cap the spread among the closures is 2 to 3 times the
truncation loss they are meant to correct), and a new reference has arrived:
`GENO/literature/Thesis_Fiore.pdf` (M. Fiore, MSc thesis, Sapienza, A.Y. 2018/19, advisor
F. Nasuti, co-advisor D. Bianchi: "Analysis of friction, heat loads and spike truncation impact
on the performance of an annular plug nozzle designed for a launcher upper stage"). Read at
declared depth (abstract and contents only, this session): an LM10-MIRA CH4/O2 upper-stage
annular plug -- the same propellant family as our world's tables -- with RANS of the internal
and external expansion including friction and wall heat flux (chapters 4-5, variable-gamma runs
in 4.7) and a truncation chapter (6: base-flow regimes 6.1, empirical base-pressure models 6.2
compared with the RANS base pressure in 6.4). Its abstract states that in vacuum the wake is
closed and the RANS solver UNDERESTIMATES the base pressure against the empirical models even
with a compressibility correction. Recorded, not used: the thesis is an input to the owner's
BLOCCATO 20 (i) choice (Panov-Shvets on the ambient or on the state at D) and to the R-F3-3
shape falsifier's base closure, and its heat-flux chapters are an input to DUTY-1(b) at F5 entry
(R-F3-5). Literature registry: new row `thesis_fiore_2019` (READ-PARTIAL(triaged), this section
the where-read anchor); the row `thesis_valeriani_2019` re-pointed to the file's current name on
disk (`Thesis_Valeriani.pdf`, arrived 2026-09-23 with Fiore's; the lower-case path of record no
longer exists, measured `ls`).

## 6. Budget
- F3 is closed: no session counter. The finder campaign is the SECOND and last decisive campaign D6
  ISS-4 allows the plug instance (the first: S30's overnight leg); 71 min per start, C and E in
  parallel. The two-wall runs are the stretch's own (derives 70 min, class 4 min, walks 84 and
  117 min; the Euclidean walk from the Hermite start lost at 04:04 to a machine-wide allocation
  failure, 5 segments).
- Runs of record and their code: the tournament's derive and campaigns ran on the carrier as
  committed except its docstring (text only); the two-wall stages ran on functions unchanged since
  their launch (later edits: the grade stage, the class stage's rounding tolerance -- the class
  stage re-run on the committed file reproduces every field of its record -- and the Newton
  branch, additive, which walk A does not take).

## 7. Conformity
- Branch `rde-nozzle-program`, main tree; identity AlexFalco5; explicit pathspecs; GENO never
  added; push on the owner's standing word (the two-wall tool re-obtains its optimum).
- R1: `[F3/A1][S40]` (residuals after the closure, no counter). R3: this log; PROGRESS residual
  block and BLOCCATO 20 (i) edited in place, the outgoing text verbatim in the archive under the
  2026-09-25 (S40) banner; D6 S40 note after the F3 CLOSED paragraph; the handoff
  RDE/handoff/F3_HANDOFF_2026-09-24.md section 8.
- R4: M0 Part VI LINE ADDENDUM S40, three items with classes.
- R5 / SR-2: two claims-registry rows in the second commit (X-PTRN, X-TWOP; the ordering rule: this
  log lands first); findings: f3-exit:finder-at-nominal-not-run, f3-exit:two-wall-stretch-not-taken,
  f3-exit:x-ptrn-registry-row-missing DISCHARGED; minted f3-residual:finder-stalls-at-fold-cliff,
  numerics:ad-hessian-forward-over-custom-vjp, twowall:design-posing-open,
  twowall:wedge-thinning-spurious-thrust. Literature: thesis_fiore_2019 new, thesis_valeriani_2019
  re-pointed. SR-1: the index row.
- Measured on the tree of the first commit (2026-09-25 ~14:45): numeric lint PASS (128 files, 0
  ratchet violations; the new carrier has no unclassified literal); claims lint PASS (0
  violations); advisory index PASS (132 rows, 0 violations); findings lint 0 violations on its rows
  (258 entries, 212 open; H4 channel and families e+f red at HEAD already: the H4 artifact's
  code_id 25c173fc3f77 against the tree's 81dae40b85da identical at HEAD and in this tree, the
  77 dead literature paths of record); literature lint 81 violations, environmental (the untracked
  roots absent on this machine), one fewer than before (the Valeriani path); FULL suite 16/23 = the
  seven environmental reds (xiii, xiv, xvi, xviii, xix, xxii, xxiii), 106 s; data/phase_diagram.*,
  data/q_mapping.* and figs/phase_diagram_op11.png restored with git checkout before the commit.
