# S29 — Re-adjudication of the free-form spike (S22/S23) with the amended instruments, and the closing of the S28 night (2026-09-16, continuation of S28 after midnight)

Tag [F3/A1][S29] (brick-2 plug line, branch `brick2-plug`). Written in
its own log because the claims lint's staleness link binds a carrier's
pass-of-record date to the last commit touching its `doc`: the S28 log
(`PROGRESS_2026-09-15_S28_ourworld.md`, four rows stamped 2026-09-15) is
FROZEN as committed in 5105457; everything after midnight lives here.
Read the S28 log addenda A/B first (the measured attribution of the
SQP-return P3 failure, the v3 instrument, the (121,101) sweep, the fold
finding); the 20:23 chain is described there and closed here.

## 1. S22 v2 — the amended carrier's run of record (closed 2026-09-15 23:57)

`validation/a1_plug_adaptive.py` amended (declared in its docstring):
every rung of the A-8/A-9 ladders is a measurement only if BOTH marches
certify; an uncertified rung makes the ladder VOID and the verdict FAIL
by discipline; artifact dir configurable (`PAKN_ART`). Run of record
`validation/_plug_adaptive/rerun_S22_2026-09-15b.log` (12834 s, same
posing as the 18:28 re-run: PAKN_M0 10, K 61, N 51, 3 cycles, 2
insertions, ITERS 30, CONTROL 1; artifacts in `_plug_adaptive_v2/`,
removed after the check below): **11/13** —
- DETERMINISM: `design` and `class0` identical to the 18:28 re-run
  (checked field by field by `regen2_driver.sh`: True). The design of
  record is therefore the m 12 design of 18:28 (`design.json` /
  `design_m10_k61_n51.json`, J 1.16199981e8 at (61,51), knots 0.4037 +
  0.4575 + 10 uniform), committed here.
- A-8 THE VERDICT: FAIL, **ladder VOID** — rung (121,101) adaptive
  cert 3.25e11 (the first-column edge cell, S28 addendum B), rung
  (241,201) INCUMBENT cert 1.59 (marginal: the margin degradation S23
  had booked for rungs >= 4 reaches rung 3 for the streamline); the
  printed gain +0.429 % (band 1.04 %) is not trusted.
- A-9 THE CONTROL: FAIL, ladder VOID — the uniform m 12 control's
  rung (241,201) cert 16.7.
- A-1..A-7 PASS as before (A-4 certifies the design at its own
  resolution only — that is the gap the fold finding exposes).
Reading of record: with the gate in place the S22 carrier says what it
could only imply before — its ladder cannot grade these designs,
because the designs it produces leave the march's certified class
(compression corner at the foot, tangled net downstream; S28 addendum
B). [X-PAKN] re-stamped from this run; the 08-10 log stays as history.

## 2. S23 re-adjudication — in flight at the time of writing

`validation/a1_plug_gain_resolve.py` amended (R-2c: the warm start must
certify at the fine instrument, else the declared fallback; see S28
addendum B). Chain `regen2_driver.sh` (20:23): S23 default 5/5; fineopt
warm start FELL BACK to the fan streamline on the S22 knots (cycle-2 m 12
cert 3.25e11, cycle-1 m 11 cert 4.17 at (121,101), both printed), then
TR-SQP at (121,101) with PGRS_ITERS 40 — at 00:12 at segment 26, J
1.15809e8 -> 1.16280e8 (+0.41 %), radius ~4e-3, converging. Then rungs
4-6 x inc/fine (six parallel processes), verdict, design_fine, figures,
build. Outcome, the fold census of the fine optimum and the re-stamp of
[X-PGRS] go in Sec. 4 below when the chain closes.

## 3. Declared
- The S22 log of 08-10 and the S23 log of 08-11 are HISTORY (their
  designs were produced by the pre-S23 driver and are not reproducible;
  the record's design vectors are lost since the 09-04 deletion); the
  runs of record for the amended carriers are the 2026-09-15/16 logs.
- `_plug_adaptive/design.json` and `design_m10_k61_n51.json` are the
  same design (the carrier writes the tagged name, `make_figures.py`
  reads the legacy one); both committed, duplication declared.
- The rerun logs of the first pass (`rerun_S22_2026-09-15.log`,
  `rerun_S23_*_2026-09-15.log`: the un-amended instruments, the crash
  at fineopt) are committed as the evidence trail of addendum B.

## 4. Closing of the chain

### 4.1 S23 fineopt closed (01:51, 19682 s): 3/5 — and the fine optimum is OUT OF CLASS

R-2b FAIL and R-2c FAIL as declared (the S22 design of record cert
3.25e11 at (121,101); cycle-1 4.17): warm start = the fan streamline on
the S22 knots (m 12). TR-SQP at (121,101), 29 segments (PGRS_ITERS 40;
bases rejected uncertified at 1.5-1.6 toward the end): fine optimum
J(121) = 1.16287610e8 = +0.4135 % over the warm start, cert 0.484 (R-3
PASS), adjoint vs FD at nodes 0/11 inside band (R-4 PASS). Fresh
3-rung ladder: gains +0.50064 / +0.41352 / +0.25064 %; the incumbent
extrapolates at r +0.509 (first order, limit 1.160274e8), the fine
design does NOT contract (r -0.732) — the paired route is refused
by the S23 rule.

**Fold margin of the fine optimum (02:00, scratch port `mport/
fine_margin_2026-09-16.log`, same instrument and constants as Sec.
5.2):** wall angle at the first station −12.04 deg at (61,51) and
−14.93 deg at (121,101) against the incoming −26.66 deg — the same
compression corner as the S22 designs (W_fine − W_inc: +0.012 at the
first knot, monotonically to −0.068 at the tip: the spike is raised at
the foot and lowered downstream); margin min cell **−0.8166** (61,51)
and **−0.9687** (121,101), KS the same, against the incumbent's +0.524 /
+0.523 on the same bucket — INFEASIBLE at every floor of the ladder
(0.262 .. 0.033). The re-adjudicated fine optimum is a folded march:
its +0.41 % and whatever the rungs 4-6 verdict says are numbers taken
from a multi-valued solution and are NOT quoted as a gain. Reading of
record: the S23 instrument, unconstrained, reproduces the S22
mechanism from a clean start — the optimizer leaves the shock-free
class as soon as it is allowed to; the verdict of the re-adjudication
is "OUT OF CLASS", which is what [X-PGRS] is re-stamped with when the
chain closes (Sec. 4.2).

### 4.2 The chain closed (05:40): six rungs, the verdict, and the fold census of the fine optimum (session resumed 12:10 from the handoff)

Rungs 4-6 x inc/fine ran as six parallel processes 01:51 -> 05:39
(rung 6 3h11m under CPU contention, s2 load ~57):
J_inc = 1.15969318e8 / 1.15996055e8 / 1.16009419e8 (cert 0.320 /
0.419 / 0.160; 908 / 3506 / 13682 s), J_fine = 1.16094544e8 /
1.16016071e8 / 1.15970977e8 (cert 0.489 / 0.282 / 0.310; 916 / 3525
/ 13332 s), every rung certified; with rungs 1-3 the
paired ladder is +0.50064 / +0.41352 / +0.25064 / +0.10798 / +0.01726
/ -0.03314 percent, diff ratios 1.870, 0.876, 0.636, 0.555
(R-5'a PASS: settling toward the march order 0.5), rung 6 predicted
-0.04044 percent and measured -0.03314 (miss 7.3e-5 vs step 5.0e-4,
R-5'b PASS), J_inc limit 1.16022773e8; gain limit -0.09609 percent
(previous window -0.14124), band 0.18058 percent > BAR 0.0400 ->
**V FAIL: UNRESOLVED**, final stage 2/3
(`validation/_plug_gain/rerun_S23_final_2026-09-15b.log`,
`verdict.json`). design_fine.json written; the five figures
regenerated and `build.sh` passed (PDF 99 pp).

FOLD CENSUS OF THE FINE OPTIMUM, the step the handoff required
before any number is quoted (`scratch_s2_2026-09-15/
fold_census_2026-09-16.log`, the column-wise y-monotonicity probe
of 2026-09-15 re-run with `fineopt.npz` on disk, three rungs), read
with the margin of Sec. 4.1 / 5.2:
- S23 fine (warm_from = fan streamline on the S22 knots): folded
  columns **59/62 (61,51), 120/122 (121,101), 240/242 (241,201)**,
  first fold at column 4/3/3; wall angle at the first station
  -12.04 / -14.93 / -19.85 deg against the incoming -26.66; cert
  0.052 / 0.484 / 0.550 (certified at every rung: the certification
  is blind to the fold, as stated);
- the S22 designs, identical to the 09-15 census (59-60/62,
  120/122, 240/242; -11.36/-18.14 deg); the incumbent 0/62, 11/122,
  40/242 (the free-jet row-growth cells only, Sec. 5.1);
- margin (Sec. 4.1): min cell -0.8166 / -0.9687 unfloored,
  -0.772 / -0.888 with the station-spacing floor (Sec. 5.2 (c)),
  against +0.524 / +0.523 (unfloored) and +0.080 / +0.057 (floored)
  for the incumbent on the same bucket.
Reading of record: the re-adjudicated S23 optimum is OUT OF THE
SHOCK-FREE CLASS at every resolution of the ladder, and the ladder's
limit is a number taken from a folded march. It is NOT quoted as a
gain.

REGISTRY: [X-PGRS] re-stamped (ondemand pass=2026-09-16; scope
prefixed "RE-ADJUDICATED 2026-09-16 (...) || ORIGINAL RECORD";
statement prefixed "RE-ADJUDICATED 2026-09-16: OUT OF CLASS (...)
|| ORIGINAL RECORD (2026-08-11, HISTORY)"; falsifier: R-2b/R-2c
FAILING as declared, BAR FIRING, and the gap named — class
membership is not among its gates, the next carrier makes it a
constraint). [X-PAKN] statement annotated in the same sense (its
"RESOLVED BY X-PGRS" tail is history); its doc untouched, pass
2026-09-15 stands.

DOCUMENT (R4, same session): `docs/brick2_doc_src/ch_spline.tex`
gains Sec. "Re-adjudication (2026-09-15/16): the optimum leaves the
class" (label `sec:readjudication`, after "The gain, resolved"):
the loss and the re-run declared, the S22 v2 run (m 12, ladder
VOID), the compression corner + folded march with the census
numbers (attributed to the session probes, to be carried by the
margin carrier), the S23 re-run from a certified start, the
six-rung ladder and why its number is not a gain, and what comes
next (the M0 Part VI margin-constrained problem, [X-MGOV], the port).
The 08-10/11 numbers in Secs. "adaptive" and "gain, resolved" stay
as HISTORY with the declaration at the head of the new section.
Captions of the three regenerated figures (`fig:spikedesigns`,
`fig:s23ladder`, `fig:workedexample`) say they are drawn from the
re-adjudication runs and carry the re-adjudicated numbers.
`make_figures.py` (out of the numeric-lint scope): the hard-coded
labels of `fig_spike_designs` (m = 11, "tail drops 87 mm", one
inserted knot) and `fig_s23_ladder` ("onto the same limit", "ZERO
within band") now READ THE ARTIFACT (m and tail drop from
design.json, every inserted knot of the history; the ladder box
prints UNRESOLVED when verdict.json says so, the transient label
follows the sign of the limit) — regenerated on s2
(`scratch_s2_2026-09-15/refig_2026-09-16b.log`); caption numbers
from `caption_numbers_2026-09-16.log` (adaptive m 12: bulge +13.4
mm at x 0.420, tail -107.5 mm; uniform m 12: +15.6 mm at 0.545,
-79.8 mm). `fig_s23_driver` reads the surviving 08-11 record log
(`run_of_record_S23_fineopt.log`) and is unchanged in content.
OBSERVATION, not diagnosed: panel (b) of `fig_worked_example`
(the mesh scatter of the fresh `_example_run.npz`, 5610 points)
renders with an empty band between the wall bands and the free-jet
triangle although the points there exist (886 in the box x 1.5-3.0,
y 1.3-2.2, finite speeds); the figure's own design, pre-existing,
not touched here.

### 4.3 The staleness link and [X-PSPL]: the carrier re-run of record (12:19 ->)

Editing `ch_spline.tex` today makes the row whose `doc` it is —
[X-PSPL], pass 2026-08-11 — STALE under the claims-lint link (rule
(i) of the handoff). The remedy the discipline prescribes is the
carrier re-run, not a placement trick: `a1_plug_spline_opt.py`
re-run on s2 at the S21 step-11 posing of record (PSPL_M 10, K 61,
N 51, ITERS 30) then the step-5 default (m 6, (81,61), 10),
`scratch_s2_2026-09-15/pspl_rerun_2026-09-16.sh`, logs
`validation/_plug_spline/rerun_S21_{prod,default}_2026-09-16.log`
(npz untracked by convention). Expected: NOT bit-identical to the
S21 record (the march is post-W-5; S22's class-0 J is already
1.15739891e8 against S21's 1.15739431e8) -> the row is RE-ADJUDICATED
like X-PAKN/X-PGRS, its S21 numbers history. Also to be measured on
its optimum, since the S22 class-0 start already sits 90 mm below the
streamline at the tail: the wall angle at the first station and the
fold census (is the S21 optimum in class?). Result in Sec. 4.4.

### 4.4 [X-PSPL] re-run of record (12:19-13:14 production; default posing after): the S21 optimum was never in the class either

Production posing (m 10, (61,51), ITERS 30; log
`validation/_plug_spline/rerun_S21_prod_2026-09-16.log`, 3320 s):
**7/8** — C-1 (basis density 86.6x over 10 -> 80 knots), C-3 (mass
on the march's own quadrature), C-2/C-2b (adjoint vs FD), C-4
(certified 0.129, descends 1.5025 -> 0.8297 m, clears the axis), C-5
(no loss), R-1 (sign-flipped minimiser 1.14203042e8 away from the
maximiser) PASS; **C-6 FAIL as in the record**: J 1.15588925e8 ->
1.15739891e8 = +0.1306 % over the streamline (record 08-09/11:
+0.1302 %), refined (121,101) +0.0834 % (record +0.0820 %), band
derived at the carrier's own resolution 0.1889 % (record 0.1930 %) >
gain. NOT bit-identical to the S21 record (the march is post-W-5:
S21's optimum was J 1.15739431e8) — but IDENTICAL at printed
precision to the S22 v2 class-0 start (1.15739891e8, sec. 1): the
line is self-consistent on the rebuilt tree. 30 records, 19 segments.

CLASS MEMBERSHIP of the re-run optimum (probe `mport/pspl_margin.py`,
log `mport/pspl_margin_2026-09-16.log`, the floored instrument of
sec. 5.2 (c), Wf - W0 = +12.4 / -3.2 / -11.5 / ... / -90.0 mm):
- (61,51): wall angle at the first station **-24.70 deg** against the
  incoming -26.66 (a 2.0 deg compression corner — an order of
  magnitude milder than S22's 15 deg), and yet **60/62 columns
  folded** (first at column 3), floored margin min cell **-0.673**
  (KS -0.673) against the incumbent's +0.080 (m_ref; mu0_1 0.040);
  cert 0.129 (blind, as before);
- (121,101): -25.59 deg, **120/122 folded**, margin **-0.731** vs
  +0.058; J +0.0834 % as C-6 prints.
Reading of record: the S21 optimum — the mildest design of the line,
the +0.13 % that started the three campaigns — is OUT OF THE
SHOCK-FREE CLASS at both resolutions. The fold scale measured in
sec. 5.2 (c) (the margin crosses mu0_1 at ~2-3 mm along +grad J) is
exactly why: +12 mm on the first knot is four times the scale. S21,
S22 and S23 are therefore ALL "unconstrained class, superseded" by
measurement, not by declaration; the margin-constrained re-run is
the first search of the class, not a refinement of a result.

REGISTRY: [X-PSPL] re-stamped from this run (ondemand pass
2026-09-16; scope "RE-ADJUDICATED 2026-09-16 (...) || ORIGINAL
RECORD"; statement prefixed OUT OF CLASS; falsifier: C-6 FAILING as
in the record, class membership named as the gap) — the doc it
binds (`ch_spline.tex`) is edited in this commit, and the staleness
link is satisfied by the run, not by a placement trick.

DEFAULT POSING (m 6, (81,61), ITERS 10; log
`validation/_plug_spline/rerun_S21_default_2026-09-16.log`, 2166 s):
**8/8 PASS**, C-6 PASS at this posing as in the S21 step-5 record —
J 1.15697414e8 -> 1.15790927e8 = +0.0808 % (record +0.0908 %),
refined (161,121) +0.0771 %, band 0.0151 % (the record quoted the
inherited 0.0094 %); 10 records, 7 segments; R-1 PASS. CLASS
MEMBERSHIP (probe `mport/pspl_margin_m6.py`, log
`mport/pspl_margin_m6_2026-09-16.log`; m_ref derived on the
incumbent at each resolution, KS not derived in this probe — min
cell only): Wf - W0 = -0.8 / -21.5 / -40.2 / -60.3 / -79.5 / -96.9 mm
(the first free knot sits at x 0.708 m, no knot near the foot); wall
angle at the first station -26.62 deg (81,61) / -26.64 (161,121) =
the flow; **0/82 and 0/162 folded columns; floored min cell +0.0911
/ +0.0916 against the incumbent's m_ref 0.0919 / 0.0952 -> IN CLASS
at both resolutions** (certified 0.092 at (81,61); NOT certified at
(161,121), worst 1.837 — the resolution lottery, declared; J there
1.15947360e8 vs incumbent 1.15858086e8). READING (observation, no
ladder walked): the two levers of the free-form spike separate by
class — the TAIL DROP (surrender radius at the tip, -97 mm) keeps
the march shock-free and its gain is resolution-stable (+0.0808 ->
+0.0771 %, ratio 0.95), the FOOT RAISE (+12 mm at x 0.565 in the m
10 posing, the direction 0.97 of grad J) folds the march and its
gain collapses under refinement (S23's ladder). The margin-
constrained search should find the first lever and refuse the
second; that is now a prediction the campaign can falsify. The two
logs are force-added (`validation/_plug_spline/` is gitignored as a
run cache; the npz stay out, the logs are the evidence of record —
declared).

## 5. NEXT (decided with the owner 2026-09-16 00:40; PROGRESS
## NEXT-PARALLELO 1-bis)

The repo already answers interior coalescence, and the plug line never
used it: M0 (Part VI, S20 block) poses the design problem as max J
s.t. g = 0 AND fold margin m(W) >= mu_0 (KKT multiplier mu) and expects
the length-constrained optimum to be MARGIN-ACTIVE ("its fold touching
the domain only at D'"); D6 REQ-NONSTALL requires the margin as a
constraint WITH GRADIENT (steer, never stall, never let through); F4b
fitted fronts are for data-borne / boundary-entering shocks only ("NO
interior-shock birth-fitting"; emergent coalescence EXCLUDED by class).
Executable on the bell tier-0 instance: `validation/margin_governor.py`
[X-MGOV] (KS aggregate of the val field over every W-dependent cell,
derived rho = K_RICH ln N / mu_0_min, floor ladder mu_0_k = m_ref / 2^k,
G1 finite-negative surrogate, `run_trsqp margin_factory` as a scipy
NonlinearConstraint). `a1_plug_march` has no val field, no fold guard,
no margin — the brick-2 admissibility (Newton-certified, descends,
clears the axis) is not class membership, which is how S21-S23 walked
through the fold (addendum B of the S28 log).

Plan, in order:
1. (this night, automatic) close the S23 re-adjudication: verdict, FOLD
   CENSUS of its fine optimum (signed-area cells, the incumbent's
   free-edge ripples as the derived tolerance) before any number is
   quoted, [X-PGRS] re-stamp, figures/PDF, ch_spline.tex paragraph.
2. PORT X-MGOV INTO THE PLUG (new carrier, tag [F3/A1]): margin field
   on the plug cells (signed cell area of the recorded net, or the
   local Lambda-form validity as in the governor — decide by measuring
   both on tonight's designs: the margin must be negative exactly on
   the folded designs and positive with a healthy m_ref on the
   incumbent), KS with rho and the floor ladder derived as in the
   governor, NonlinearConstraint in `a1_plug_spline_opt.run_trsqp`
   (formulation entry, driver policy untouched), rejector = the S22 m
   12 design must be INFEASIBLE at every rung of the floor ladder.
3. S21 -> S22 -> S23 re-run MARGIN-CONSTRAINED (the same carriers with
   the margin on): the claim becomes "free-form optimum IN the
   shock-free class at L = 2.5 m"; mu reported (mu > 0 = M0's
   margin-active prediction confirmed on the plug); S21-S23 of record
   declared "unconstrained class, superseded".
4. Then the queue of record: tournament-grade A/B at the NOMINAL
   ambient (GENO member at exact PA — GENO protocol N-75 — or the
   declared 0.5 percent residual), Rao-vs-spline at L 5.926 from the
   GENO cut (now margin-constrained too), Table-1 oracle bands on our
   world, stratified instance (F3 EXIT).
5. Cheap residuals: a larger perturbation for the v3 motion test (one
   discriminating direction at 1.5 percent); findings rows for
   [X-RAOIS]/[X-RAOWD]; the Italian document (sec. vsrao to the rao_val
   member); push as AlexFalco5 once the remote allows it.

### 5.1 Step 2 started (01:10-01:15): the margin field, measured before any code

Not the governor's `val` (that is Sternin / Rao-Beck Eq. (4), "can a
control surface advance through this state" — a pointwise STATE
criterion, legitimately negative on certified DEF fields per M0, and
healthy on every rejected bell design of the S20 standoff): M0's
definition, "distance from same-family characteristic coalescence",
measured directly on the recorded net. Candidate: for every interior
point (jnew, i) the TRUE net cell [(jprev-1, i-1), (jprev, i-1),
(jnew, i), (jnew-1, i)] with jprev = jnew + jsrc0 - 2 from the recorded
`wfoot` (row consumption at the wall — the 2026-09-15 fold census used
index-aligned quadrilaterals, wrong under consumption; its column-wise
y-monotonicity census did not depend on it and stands), and
m = signed area / (mean C+ leg x mean C- leg) — the local Jacobian of
the net as a sine of the angle between the families; healthy reference
sin(2 alpha) at the cell's state; zero = coalescence; negative = fold.
Measured (`scratch_s2_2026-09-15/plug_margin_probe_2026-09-16.log`):
- KNOWN ANSWER: incumbent median m 0.667 = median sin(2 alpha) 0.667 at
  both (61,51) and (121,101); no cell <= 0 at (61,51) (3123 cells);
  m_ref = min over the interior bucket 0.652 / 0.651 (stable across
  the rungs);
- REJECTOR: the S22 designs are deeply infeasible — interior min
  -0.802 / -0.826 at (61,51) (m 12 / m 11), -0.975 / -0.931 at
  (121,101); negative interior cells 200 / 299 -> 818 / 1166 under
  refinement (a converged feature), argmin at columns 3-5 (x 0.49-0.89,
  right after the corner);
- EDGE BUCKET: the incumbent at (121,101) has 19 cells <= 0, all within
  the top 15 percent of rows (argmin col 12, row fraction 0.89, x
  2.825, y 2.319: the thin row-growth cells at the free jet), interior
  min +0.651. The lane bucket is therefore the INTERIOR (the free-edge
  band excluded, its depth derived from the incumbent's own field at
  the working ladder and declared), as the governor's design-wall
  bucket excludes what the margin is not about.
Port design (to land after the S23 chain closes — the shared modules
are imported fresh by its later stages): (i) `plug_march(...,
margin_diag=True)`: the cell's four corners are all in G when the
point is solved, so m is computed in-loop and KS-aggregated ONLINE
(logaddexp, no mesh stack — the S23 compile lesson), returned as a
traced scalar in play mode; (ii) `a1_plug_spline_opt.run_trsqp(...,
margin=)` NonlinearConstraint entry via a margin_factory as in
X-MGOV; (iii) carrier `a1_plug_margin.py` [F3/A1]: derive stage
(R-KS bounds on the incumbent field, R-GRAD AD vs FD ladder, R-G1
finite negative on the m 12 design, REJECTOR: the m 12 design
infeasible at every rung of the floor ladder mu_0_k = m_ref / 2^k,
rho = K_RICH ln N / mu_0_min) then campaign (S21 posing, L 2.5,
margin-constrained; mu reported with the B-stationarity wording).

### 5.2 Derive stage EXECUTED on a scratch port (01:17-01:40; `scratch_s2_2026-09-15/mport/`: copies `plug_march_m.py`, `plug_spline_opt_m.py`, `margin_derive.py` + log — the shared modules untouched while the S23 chain runs)

- D0 CONSISTENCY: the in-loop margin (true net cell, corners from G
  at solve time, online logaddexp KS) reproduces the numpy census on
  the same record EXACTLY (min 0.524210 both, diff 0.0; 2433 = 2433
  bucket cells); orientation of the net measured (median negative in
  the A->B->C->D traversal -> orient -1, applied).
- D1 DERIVATION on the incumbent (61,51), m 10 knots, bucket = cells
  with rows_from_top > f_edge x column height, f_edge = K_RICH/2 x
  the measured 0.11 = 0.22 (declared), jmin 2 (wall cells included):
  m_ref = 0.5242 (median 0.678 = sin 2 alpha), floors mu0_k = m_ref/2^k
  = 0.262, 0.131, 0.0655, 0.0328; rho = K_RICH ln N / mu0_4 = 951.9;
  R-KS PASS (vmin - lnN/rho 0.51602 <= KS 0.52412 <= vmin 0.52421).
- D2 R-GRAD PASS: AD margin gradient vs a 3-step FD ladder on the
  frozen schedule, two random directions: |diff| 4.8e-8 and 2.8e-8
  against bands 1.0e-5 / 4.6e-6 — the margin is exactly
  differentiable through the replay (155 s incl. compile).
- D3 REJECTOR PASS: the S22 designs are INFEASIBLE at every floor
  (m 12: KS -0.802; m 11: KS -0.826) with FINITE margin (-1.06 /
  -1.09 with the G1 surrogate) and finite gradients (|g| 24 / 7.4).
- D4 (REQ-NONSTALL walk), three attempts, each a measurement:
  (a) 01:45 CRASH inside trust-constr ("array must not contain infs or
  NaNs" at the normal step): instrumented re-run (`d4_debug`) — at a
  trial point 1-2 cm off the first three knots (a compressive kink)
  BOTH J and the margin have finite values (J 1.2033e8 = a "+4 percent"
  from a folded net, m = -1.19) and ALL-NaN gradients; the margin's G1
  guard zeroed its gradient (counted), the OBJECTIVE had no guard ->
  the bell's f_np/g_np REQ-NONSTALL contract (S21 C2) added to the plug
  driver when a margin is present (non-finite J -> 1e30, non-finite
  grad J -> zeroed, both COUNTED and printed per segment).
  (b) 02:12-02:50 guarded walk (`d4_debug2`): no crash, 2 segments,
  counters reported (grad_nonfinite 2, gm_nonfinite 2), multipliers
  mu = +0.127 / +0.252 (the constraint is ACTIVE: grad J points into the
  fold) — but NO progress: the interior-point trial points at radius
  5 cm land deep in the fold, the zeroed gradients poison the segment
  model, trials rejected. (c) THE FOLD SCALE MEASURED along grad J
  (dominated 0.97 by the FIRST knot): with the unfloored sine the
  margin is +0.524 up to 2 mm and -0.67 at 3 mm — the drop is 8 cells
  of 2 mm legs at x 3.9, y 2.3 (row fraction 0.78: the free-jet region)
  whose C+ legs run BACKWARD: the coalescence of the corner's weak
  compression (0.35 deg) at the far end of the C+ lines — physical
  (adjacent rays a row apart cross after ~dy0/d(lambda) ~ 1-2 m, inside
  the 3 m columns), but a 2 mm cell weighed like a 30 cm fold because
  the sine is scale-free. FIX, derived and declared: the leg product
  is floored at the station spacing squared (ell2 = ((L - X0)/(K-1))^2
  — a fold counts when its inverted cells are resolved; the criterion
  tightens under refinement with the ladder). Re-measured: incumbent
  m_ref 0.0801 (61,51) / 0.0571 (121,101) (the smallest RESOLVED
  healthy cells set it now), S22 m 12 / m 11 / S23 fine: -0.754 /
  -0.714 / -0.772 at (61,51), -0.897 / -0.863 / -0.888 at (121,101)
  (still deeply infeasible: the discrimination is O(1)); along grad J
  the margin now reads +0.062 (2 mm), -0.037 (3 mm, the ripples),
  -0.529 (5 mm: a resolved fold), -0.68 .. -0.87 beyond, while J rises
  only +0.05 percent to 12 mm then falls. READING: the shock-free class
  at this length admits almost no concentrated compression at the
  foot — the optimizer's lever IS the forbidden direction; the
  constrained optimum must find its gain elsewhere or be the streamline
  (M0's margin-active prediction, now with numbers).
  (d) 03:12 walk relaunched with the floors from m_ref 0.0801 (0.040 ..
  0.005, rho 6240) and the trust radius DERIVED from the fold scale
  (tr0 = h*/K_RICH = 6e-4 m, h* = 2.5 mm where the margin crosses
  mu0_1 along grad J), 4 segments x 12 iterations — result in Sec. 5.3.

### 5.3 The first margin-constrained walk (03:12-05:00, `mport/d4_walk_2026-09-16.log`, 6506 s): M0's margin-active prediction, with numbers, on the plug

S21 posing (L 2.5 m, theta_E 0, m 10 uniform knots, (61,51)), start =
the fan streamline (J 1.15588925e8), floors from m_ref 0.0801 (mu0_1 =
0.0401, rho 6230), tr0 6.25e-4 m derived from the fold scale, 4
segments x 12 trust-constr iterations:
- 3 segments walked (the 4th: trial worse at the 1e-3 radius floor ->
  converged), 4 records, every accepted base certified (final cert
  0.052);
- J 1.15588925e8 -> 1.15619582e8 = **+0.02652 percent** over the
  streamline (the unconstrained instruments' "+0.52 percent" at this
  resolution was a folded net);
- the constraint is ACTIVE at the returned base: KS - mu0 = +0.0009,
  min cell +0.0410 = mu0_1; multiplier of the last segment mu =
  2.70e5 (N per unit margin; B-stationarity wording, O1 open) — the
  measured shadow price of shock-freeness on the plug;
- the design: first knot +3.7 mm, second +0.8, third -1.3, the rest
  below 1 mm; wall angle at the first station -26.24 deg (a 0.42 deg
  compression corner: the fold scale itself);
- REQ-NONSTALL counters over the walk: gm_nonfinite 3, grad_nonfinite
  2 (trial points inside the fold, counted, none accepted; the bases'
  gradients finite: |grad J| 8.2e6 at the returned base).
Reading (working resolution only, one start, no ladder yet): at fixed
length the free-form spike's optimum in the shock-free class sits ON
the class boundary (margin-active, mu > 0) with a gain three orders
below the unconstrained artifact and inside the S21 band (0.19
percent at this resolution) — the streamline is optimal within band
for the RIGHT reason, and the price of staying shock-free is measured.
What the carrier must add before any of this is quoted as a result:
the floor ladder mu0_k (activity monotone in mu0), the resolution
ladder (m_ref 0.057 at (121,101): the criterion tightens), more than
one start, the active-cusp census, and the [D1]-constrained corner
metric where applicable.

### 5.4 Phase C in the SHARED modules (14:05-14:40): the port, its gate, the carrier [X-PMRG], the derive stage of record

PORT (after commit 2b, no run importing the modules): the scratch
changes of `mport/plug_march_m.py` / `plug_spline_opt_m.py` applied
ADDITIVELY to `validation/a1_plug_march.py` (`plug_march(...,
margin=None)`: in-loop `cell_margin` on the true net cell at the
moment the point is solved, online logaddexp KS, `margin_ks/min/n`
in `out`) and `validation/a1_plug_spline_opt.py` (`march_record(...,
margin=)`, `margin_replay`, `margin_and_grad`, `run_trsqp(...,
margin=None, tr0=0.05)`: NonlinearConstraint with value/gradient
memo, G1 surrogate, REQ-NONSTALL on the objective with the finite
fallback `J_NONFINITE = sqrt(float max)` DERIVED from the machine
range — no new literal: both files keep their ratchet counts 50 /
25). GATE (`mport/port_gate.py`, log `port_gate_2026-09-16.log`):
with `margin=None` the record march, the C-2 objective/gradient
(J 1.1558892465e8, |grad| 1.059703e7, cert 0.257) and the first
unconstrained TR-SQP segment (seg 1 J 1.15680509e8 cert 0.307)
reproduce the pre-port [X-PSPL] re-run of 12:19 at printed
precision; the margin fields are inert (None/None/0). `constraints=[]`
is scipy's default `()` after `standardize_constraints` (read at
source): the same code path.

CARRIER `validation/a1_plug_margin.py` [X-PMRG] (0 non-trivial
literals — every constant derived or from derive.json; stages
`derive` / `campaign`, env `A1_PMRG_STAGE`, `PMRG_SEGS/ITERS/STARTS/
RUNGS/LADDER/ART`). DERIVE OF RECORD (`validation/_plug_margin/
run_derive_2026-09-16.log`, 963 s, **11/11 PASS**; constants in
`derive.json`, committed):
- D0 orient -1 (median -0.526 over 3121 whole-column cells);
- D1 bucket depth MEASURED at (121,101): 14 non-positive cells of
  12468, deepest at row fraction 0.095 (column 12) -> f_edge =
  K_RICH/2 x 0.095 = 0.190 (the scratch had 0.22 from an unfloored
  0.11); R-D0 in-loop == numpy: min 0.080084 both, diff 0.0, 2533 =
  2533 cells; m_ref 0.0801 (median 0.526), floors 0.0400 / 0.0200 /
  0.0100 / 0.0050, rho 6263.1, gap 1.25e-3; R-KS PASS;
- D2 R-GRAD: AD vs 3-step central FD (steps ell/4^k, k = 3..5 =
  0.56 / 0.14 / 0.035 mm, derived below the fold scale) in two
  random directions |diff| 5.2e-10 and 9.6e-8 inside bands 3.3e-7 /
  3.7e-6; the corrupted control (largest component doubled) FAILS
  the same check (3.0e-2) as required;
- D3 R-G1 REJECTOR: S22 m 12 KS -0.7535, S22 cycle-1 m 11 -0.7136,
  S23 fine m 12 -0.7719 — infeasible at all four floors, margins
  finite (-0.79 / -0.75 / -0.81 with the surrogate), gradients
  finite (|g| 4.4 / 2.2 / 4.7);
- D4 R-FSC: along +grad J (0.97 on the first knot) the margin reads
  +0.0795 at h 1.12 mm (J +0.0098 %, theta st.1 -26.62) and +0.0386
  < mu0_1 at 2.24 mm (J +0.0185 %, -26.44): bracket [1.12, 2.24] mm,
  h* = 1.58 mm, **tr0 = h*/K_RICH = 0.396 mm** (the scratch walk had
  used 0.625 mm from an eyeballed 2.5 mm; the derived radius is
  tighter and the class boundary closer than the unfloored census
  suggested: the floor mu0_1 is crossed before the first inverted
  cell appears).
REGISTRY: row X-PMRG minted (carrier, ondemand pass 2026-09-16, doc =
this log, proof = the carrier); statement scoped to the derive stage
+ the class discrimination; the campaign declared BUILT AND
SMOKE-TESTED, NOT of record. Lint: numeric 105 files 0 ratchet
violations (new file 0 literals, no birth row needed).

CAMPAIGN SMOKE TESTS (artifacts in a scratch dir `pmrg_smoke/`, never
of record), each a measurement that changed the code:
- 1 x 2 and 1 x 4 iterations (`pmrg_smoke_2026-09-16.log`, 527 s;
  `pmrg_smoke2_...`, 708 s): 4/4 PASS, the whole path exercised
  (constraint + memo, counters, multipliers, census, C-1..C-4, json)
  but NO MOTION — structural: `run_trsqp` returns the best CERTIFIED
  base, and with one segment the segment endpoint is never recorded,
  so the answer is the start. The monotonicity stop had read that as
  "inactive at the tightest floor -> ladder vacuous": WRONG inference
  from a walk that did not move -> guard added (the stop fires only
  after a walk that moved; a no-motion rung is declared, not
  adjudicated).
- 2 x 6 iterations (`pmrg_smoke3_2026-09-16.log`): the walk moves —
  seg 1 base J 1.15623000e8 (+0.0295 %), cert 0.068 — and its margin
  reads **KS - mu0 = -0.0152 (min cell +0.0249 < mu0_1 0.0400)**: a
  certified, improving base PAST THE FLOOR, accepted because the
  driver's acceptance test knew only J and certification.
  trust-constr is a barrier method with slacks (c(x) - s = 0 holds
  at convergence, not at every iterate): a segment cut short by its
  budget returns an iterate on the infeasible side (the scratch walk
  of record, 12 iterations, returned +0.0009). "Never let through"
  -> FEASIBILITY GATE in `run_trsqp` (margin path only, no new
  literal — it reuses the revert-and-shrink branch of a worse
  trial): a base with KS - mu0 < -tol (tol = the aggregation gap
  ln N / rho, carried in the margin dict by the carrier) is REJECTED
  and COUNTED (`infeasible_base`); the margin=None path is untouched
  (the flag is False there). Verdict of that smoke (2367 s): **4/5,
  C-4 FAIL** on the returned base — J +0.02948 % over the streamline,
  cert 0.068, W - W0 = +4.0 / +1.5 / -0.3 / ... / -1.4 mm (the first
  knot again, the class-breaking lever), wall angle -26.21 deg (a
  0.45 deg corner), KS - mu0 -0.0152 -> ACTIVE, mu 7.4e4
  (B-stationarity), active-cusp census 4 cells <= mu0 + gap in
  columns 13-16 (x 0.78-0.89 m, row 31; one cluster; argmin (14,31)
  m 0.0249): the constraint binds DOWNSTREAM of the corner, where the
  C+ lines of the foot's weak compression coalesce first — the fold
  scale's own geometry (sec. 5.2 (c)). The gate turns this base into
  a rejected trial.
- 2 x 6 with the gate (`pmrg_smoke4_2026-09-16.log`, 1348 s): 4/4,
  the infeasible base REJECTED and counted (`infeasible_base` 1) —
  and the walk ENDED on that rejection: "trial INFEASIBLE at the
  radius floor -> converged, stop". Cause: the driver's radius floor
  is a policy constant of the unconstrained walk (1 mm; `max(1e-3,
  tr/2)` on rejection, "converged" when a trial at <= 1.01 mm fails)
  and the derived tr0 (0.396 mm) sits BELOW it, so the first
  rejection is already "at the floor" and the walk cannot retry with
  a smaller radius. FIX, measured then made: `run_trsqp(...,
  tr_floor=None)` — with None the code uses the SAME two literals as
  before (bit-identical for every existing caller: R-BIT gate re-run
  after the change, `mport/port_gate2_2026-09-16.log`, C-2 and seg 1
  identical at printed precision); the carrier passes tr_floor =
  tr0 / K_RICH (0.099 mm, derived), so a rejected trial halves the
  radius down to the floor before the walk is declared converged.
  Numeric-lint: the four duplicated floor literals collapsed into the
  two definitions -> the file's count fell 25 -> 21 and the ratchet
  baseline was lowered to 21 (the permitted direction; never raised).
- 2 x 6 with gate + derived floor (`pmrg_smoke5_2026-09-16.log`,
  1264 s): 4/4 — the same infeasible endpoint (J +0.0295 %, KS - mu0
  -0.0152) is REJECTED through the worse-trial branch and the radius
  HALVES to 2.97e-4 m (no longer "at the floor"); the 2-segment
  budget ends there (a retry needs SEGS >= 3), so the returned base
  is the start, declared NO MOTION, C-4 PASS. Every branch the
  campaign will take at 4 x 12 has now been executed once on the
  shared modules: constraint + memo, counters, multipliers, census,
  the no-motion guard, the feasibility gate, the derived floor.

The full campaign (4 floor rungs x 4 segments x 12 iterations from
the streamline, the resolution ladder (121,101)/(241,201), a second
start) is a multi-hour leg on s2 — prepared, launched only on the
owner's word.
