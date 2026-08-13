# S24 GAP POSITION — FACET 3: DESIGN PARAMETRIZATION
FINDER key: `parametrization`. Date 2026-08-12. Scope: the tier-0 design
class (clamped-left/natural-right interpolating cubic spline, uniform
abscissae, heights-as-dofs, [X-AKNO] adaptive insertion) vs SOTA
control-point classes; conditioning, local support, oscillation risk;
hierarchical enrichment as the outer loop.

HONESTY PREAMBLE. Nothing below proposes weakening any rejector, derived
tolerance, or certification gate. The free-knot rejection (D6 item 9,
Jupp-1978 lethargy + RK-G cost) is ADJUDICATED and not relitigated here.
The D6 rejection of a control-point basis switch is treated as what its
text says it is: an adjudication of the CONDITIONING + revalidation-cost
axis only — the oscillation / shape-constraint / local-support axis is
the unadjudicated question this facet addresses.

PROBES RUN (declared; all pure-python analytic, replicating
`TV.spline_coeffs`/`spline_eval` math exactly; total cost ~1.2 s CPU):
- P1 cardinal functions, 9 uniform nodes: max undershoot 0.166; nonlocal
  influence decays ~0.243/interval (never zero; B-spline control point:
  exactly zero beyond 2 intervals).
- P1b' monotone straight-taper + clamped-slope mismatch: interpolant
  VALUES stay monotone up to thB = 40 deg on this instance, BUT
- P5 the knot curvatures M alternate in sign 7/8 from the clamped end
  (ratio M1/M0 = -0.2679 = -(2-sqrt(3)), amplitude prop. to slope
  mismatch: M0 = -0.689 @18.85 deg, -2.375 @30 deg on a LINEAR taper
  whose true curvature is 0) — the measured mechanism of the S17
  "taper seed -> spline oscillation at the attachment -> compression ->
  uncertified cell + NaN gradient" chain (S17 log step 10(ii);
  a1_toc_variational_jax.py:1337-1343).
- P2 natural-right BC vs not-a-knot on a contour with nonzero lip
  curvature: last-interval sup error 6.9e-04 vs 6.7e-16 (exact-quadratic
  control) and 8.5e-04 vs 1.1e-05 (76x) on a non-polynomial contour.
- P3 warm-start nestedness: insertion + re-interpolation reproduces the
  incumbent spline to 6.7e-16 sup on a dense grid — EXACT
  (Boehm-equivalent) by nested-space uniqueness.
- P4' adjacent-knot-ratio ladder: cond(A) saturates at ~6 for ratio
  10..1000 while the max cardinal amplitude grows ~linearly: 2.2 (@10),
  17.5 (@100), 170.7 (@1e3) — the SOLVE never degrades; the
  INTERPOLATION OPERATOR does.
Scripts: scratchpad/probe_parametrization.py, probe_parametrization2.py
(+ inline M-sign probe). No march launched; the S24 campaign untouched.

---

## FINDING 1 — Interpolation-vs-control-point: the adjudication itself
is MISSING, and the interpolating class has a structural oscillation
channel the S17 record already measured.
- CLASS: NOT-SOTA (unadjudicated basis-class choice on the axis that is
  actually failing).
- CITE: docs/rde_nozzle_development_plan.md:922-926 (rejection rationale
  = "knot PLACEMENT, not parametrization conditioning" + stack
  revalidation cost — conditioning axis only);
  a1_toc_variational_jax.py:1337-1343 (S17 oscillation of record);
  adaptive_knot_optimize.py:12-14 ("basis class UNCHANGED").
- GAP: C^2 interpolation through prescribed heights has (i) no
  variation-diminishing property, (ii) no convex-hull bound, (iii) a
  clamped-end alternating-curvature Green's function (P5: sign-flip
  wave, ratio -0.268, amplitude prop. to the slope mismatch and growing
  as 1/h as knots refine) — so ANY warm start whose data slope
  disagrees with tan(thB) injects a convex/concave oscillation exactly
  at the attachment, where 41.8% of the [X-AKNO] indicator mass already
  lives (M0:1498-1506). A control-point class (B-spline control
  polygon) bounds wall and slope by the polygon (convex hull +
  variation diminishing), and — decisive for the certifiability
  program — makes slope positivity / monotone-turn admissibility a set
  of LINEAR inequalities on W, i.e. converts part of the
  Known-Unrelaxable-Simulation-NONQUANTIFIABLE certifiability
  constraint (M0:1624-1637, Le Digabel-Wild) into cheap polyhedral
  constraints checked BEFORE paying a march.
- SOTA REFERENCE: B-spline control-point parametrization (de Boor,
  A Practical Guide to Splines; Boehm 1980 insertion; IGA shape
  optimization lineage Cottrell-Hughes-Bazilevs); CST (Kulfan 2008)
  and Hicks-Henne (1978) as the industrial global alternatives —
  named, but both are GLOBAL-support and would not fix locality;
  the serious contender is the B-spline control polygon.
- EXTREMAL CASES: (E1) deep-DEF/short-L, thB steep: warm-start slope
  mismatch maximal at the clamped end -> curvature wave amplitude
  ~ mismatch/h -> compression cell at the attachment (the S17 chain);
  (E2) post-[X-AKNO] graded knots + a height jump between adjacent
  close knots: P4' cardinal amplitude 17-170x -> in-between overshoot
  breaks slope admissibility invisibly to the node values.
  EVERYDAY: any non-GENO-seeded start (the S17 attempt-1 case
  verbatim) — today the engine is feasible-seed-dependent because the
  class oscillates on innocent data.
- FAIR NOTE (both ways): nodal-height dofs give a well-conditioned
  geometry map, and the D6 claim that conditioning was NOT the defect
  is measured-supported (kappa_diag 3.5-5.4 post-Jacobi). The gap is
  the missing adjudication of the OTHER axis, with the S17 oscillation
  as standing measured evidence. A zero-behavior-change first step
  exists: exact change of basis to B-spline control points POST-solve
  for certificates only (convex-hull bounds on y, y') — no stack
  revalidation, the optimization variables untouched.

## FINDING 2 — Natural right BC (y''(L) = 0) biases the class exactly
at the lip, where the [C-O33] goal quantity is measured.
- CLASS: RIGOR-GAP.
- CITE: a1_toc_variational_jax.py:148 (`natural right: M_{n-1}=0`);
  goal metric = corner mismatch AT the lip
  (adaptive_knot_optimize.py:242-250); lip interval carries 17.6% of
  indicator mass (M0:1501); S19 residual wording "converging in BOTH
  the design-class and mesh limits but NOT confirmed at a Richardson
  band" (D6:889-891).
- GAP: a Rao/TOC bell has nonzero curvature at the lip; the class
  imposes y''(L) = 0 at EVERY m, so the representation error at the lip
  is O(h^2) instead of O(h^4) and does not vanish by knot insertion
  elsewhere. P2 measures 76x last-interval error vs a not-a-knot end on
  a curved-lip contour. This is a named, unexcluded ALTERNATIVE
  EXPLANATION for the [C-O33] corner-row residual: the mismatch
  |dJ/dy_lip - corner density| is evaluated on a class that cannot
  curve at the very node being differentiated. No carrier measures the
  BC-induced representation floor at the lip.
- SOTA REFERENCE: not-a-knot end condition (de Boor 1978; the
  scipy/FITPACK default lineage) or free-end B-spline control points.
- EXTREMAL CASES: (E1) deep-DEF defnoz instance (Dtheta = -9.98 deg,
  S24): strong lip curvature -> BC bias maximal; (E2) eps = 30, L = 8
  DEF-wall tier-0 class (M0:2064) — long last interval, h^2 penalty
  large. EVERYDAY: the eps = 4 twin case itself — the goal of record is
  measured at this biased node today.
- REGISTERED PROBE (S25, needs marches, > 30 s): not-a-knot twin of
  `spline_coeffs` (one row changed), re-measure the r=1/r=2 corner
  mismatch at W*8; if the 6.6295e-02 baseline moves materially, the
  design-class diagnosis gains/loses a named mechanism. Rejector-form:
  the twin must NOT move the GENO-oracle band checks (same wall data).

## FINDING 3 — The insertion degeneracy guard protects the wrong
object: it is mesh-derived (station spacing), not operator-derived
(knot ratio).
- CLASS: RIGOR-GAP (tolerance not derived from the failure mode it
  guards — R5 discipline applied to a geometry tolerance).
- CITE: adaptive_knot_optimize.py:209-213 (`dx_loc = median station
  spacing; skip if closer than dx_loc to a knot`), header 39-42 ("a
  degenerate interval poisons the spline solve" — the GENO double-point
  lesson).
- GAP: P4' shows the spline SOLVE is insensitive (cond(A) ~ 6 at knot
  ratio 1000) while the interpolation OPERATOR grows ~linearly in the
  adjacent-knot ratio (cardinal amplitude 2.2/17.5/170 at 10/100/1e3):
  the guard's stated rationale (solve poisoning) is not the actual
  failure mode, and its scale dx_loc SHRINKS with march refinement
  (r=2 -> Nw=120 halves it) — so the admitted knot ratio degrades with
  the mesh while the true admissibility bound (operator growth) is
  mesh-independent. Repeated cycles inserting into the SAME
  mass-carrying interval (mass is persistent: 41.8% first interval)
  produce geometric knot clustering that the guard progressively
  stops guarding.
- SOTA REFERENCE: local-mesh-ratio admissibility for spline
  interpolation (de Boor's local-ratio bounds; Schoenberg-Whitney
  conditions, FITPACK knot-placement discipline).
- EXTREMAL CASES: (E1) refined run Nw = 240 + max_ins = 3 into one
  interval over 4 cycles -> adjacent ratios O(10^2) admitted; (E2)
  nearly-degenerate knots (the mandate's own extremal): height noise
  between two close knots amplified 17-170x between nodes -> slope
  admissibility broken between stations, invisible at stations.
  EVERYDAY: cycle 2 inserting next to cycle 1's knot at Nw = 60.
- FIX SHAPE (additive): derive the guard from the measured cardinal
  amplitude or a declared max adjacent-knot ratio (mesh-independent),
  keep the station-spacing check as the secondary bound.

## FINDING 4 — Warm-start exactness is provable and measured
machine-zero, but the code disclaims it and wields a print instead of
a rejector.
- CLASS: INCOMPLETE (an armable invariant left unarmed).
- CITE: adaptive_knot_optimize.py:44-48 ("NOT claimed
  geometry-preserving (interpolation is not Boehm insertion): the
  representation deviation is MEASURED and printed"), 434-451 (dev_warm
  print-only).
- GAP: since T_old is a subset of T_new, thB (hence xB and the clamped
  slope) is unchanged, and both ends share BCs, the incumbent spline
  lies in the refined space and re-interpolation reproduces it UNIQUELY
  — P3 measures 6.7e-16 sup deviation. So (i) the class enrichment IS
  exactly Boehm-equivalent (a THEOREM-grade property under-claimed as
  "measured deviation"), and (ii) dev_warm above a derived roundoff
  floor is a DEFECT DETECTOR (knot remap or BC inconsistency), which
  today would print and pass. R5 culture: tests must be able to
  reject — this one cannot.
- SOTA REFERENCE: Boehm (1980) knot insertion exactness; Oslo algorithm
  (Cohen-Lyche-Riesenfeld 1980) — nested-space refinement as an exact
  operation, standard in every spline library.
- EXTREMAL CASES: (E1) insertion at a near-degenerate site (ratio 1e3):
  exactness still holds (P4' cond ~ 6) but a naive tolerance would need
  the operator-growth factor — the derived floor must be
  K * eps * cardinal-amplitude, itself measurable; (E2) steep-thB clamp
  (large slope0): r[0] scale grows, floor must scale with it.
  EVERYDAY: the S20 two-knot cycle (8 -> 10 dofs) — arm the rejector
  there first.
- FIX SHAPE: dev_warm <= K_RICH * eps * (measured cardinal amplitude)
  * scale as a check() row; promote the nestedness statement to the
  M0 block with class THEOREM (elementary uniqueness argument).

## FINDING 5 — The outer loop is insertion-only: no knot removal, no
coarsening, no multilevel correction — dof economy is declared load-
bearing but unenforced.
- CLASS: INCOMPLETE (vs the AFEM lineage the loop cites for itself).
- CITE: adaptive_knot_optimize.py:6-14 (AFEM/FITPACK skeleton,
  insertion only), 56-59 (stop rules: improvement/rise/empty/budget —
  none remove a knot); D6:938-939 ("dof economy is part of correctness
  here"); D6:893-894 (residue (a): "not more uniform nodes").
- GAP: the cited AFEM lineage achieves instance-optimal complexity only
  with a coarsening/removal leg (mark-refine-AND-coarsen); [X-AKNO]
  ratchets dofs monotonically — a knot inserted on a residual that a
  later optimum flattens stays forever, and every retained dof taxes
  ALL later cycles at n+1 gradient evals per segment-Hessian (header
  32-34 names this budget pressure explicitly, then caps insertions
  instead of removing dead dofs). The exact nestedness of Finding 4
  makes removal cheap to TEST: project to the candidate-coarser class
  and measure the representation deviation against a derived band.
- SOTA REFERENCE: knot removal (Lyche-Morken 1987, CAGD); AFEM
  optimality with coarsening (Binev-Dahmen-DeVore 2004); multilevel/
  progressive-enrichment shape optimization (Desideri et al.,
  hierarchical parametrization lineage).
- EXTREMAL CASES: (E1) oscillating indicator (mass alternating between
  two intervals across cycles): monotone dof growth, stagnant goal,
  budget exhausted with the class polluted; (E2) goal-ROSE stop
  (adaptive_knot_optimize.py:567-570): the incumbent best is kept but
  the CLASS of the returned state has the failed knots — a certlim
  restart from it inherits them. EVERYDAY: the default 4-cycle,
  3-insert run: 8 -> up to 20 dofs with no audit that each survivor
  still carries mass.

## FINDING 6 — The parametrization makes the measured Hessian
structurally dense and the spline solve O(n^3)-unrolled: the T2 cost
firing has a basis-locality component nobody priced.
- CLASS: EFFICIENCY-GAP.
- CITE: a1_toc_variational_jax.py:1087-1095 (measured FULL Hessian,
  n+1 gradient evals per segment base); adaptive_knot_optimize.py:32-34
  (each new dof adds n+1 evals — the declared reason for the insertion
  cap); S18 log step 7 (T2 FIRED of record, "curvature measurement +
  RK-G re-records dominate"); a1_toc_variational_jax.py:131-150
  (spline_coeffs: dense (n,n) matrix built by a Python loop of .at[]
  sets + jnp.linalg.solve for a TRIDIAGONAL system); D6:880-881
  ("colored Hessians" already named as a future lever, never built).
- GAP: with global-support cardinal functions (P1: decay 0.243/interval,
  never zero) the W-space Hessian has no exploitable sparsity, so the
  n+1-eval full measurement is forced and scales linearly with
  enrichment — the exact term named dominant when the T2 practicality
  falsifier fired. A local-support basis gives a banded H measurable in
  O(bandwidth) evals via coloring, INDEPENDENT of m. Separately, the
  unrolled dense solve grows the jit trace and pays O(n^3) per
  evaluation; at m = 8 it is noise, at m ~ 30 (4 cycles x 3 insertions
  + baseline) it is not, and it sits inside EVERY traced evaluation.
- SOTA REFERENCE: graph-colored FD Hessians (Curtis-Powell-Reid 1974;
  Gebremedhin-Manne-Pothen 2005); banded/tridiagonal spline solves
  (Thomas algorithm; de Boor BSPLVB/banded collocation lineage).
- EXTREMAL CASES: (E1) m = 30 after full enrichment at a frontier
  instance walking ~100 segments: ~3100 gradient evals of pure
  curvature measurement; (E2) deep-DEF certlim walks (record 111 s vs
  replay 2 s at 7818 cells): each segment base re-records AND pays n+1
  replays — the product is the wall-clock killer. EVERYDAY: the current
  10-dof class pays 11 evals per segment, ~5 segments per cycle, every
  cycle.
- HONEST BOUND: coloring requires the basis switch (Finding 1) or an
  adjudicated band-truncation of the cardinal coupling (decay 0.243 =>
  |H_ij| falls ~2 decades by 3 intervals — a MEASURABLE truncation with
  a derived bar, no basis switch needed). Registered S25 probe: measure
  |H_ij| vs |i-j| at W*8 (n+1 evals, ~30 s at the small instance) and
  compare with the cardinal-decay prediction.

## FINDING 7 — Declared class monitors (slope positivity, supersonic
wall) are not computed anywhere: shape admissibility is discovered only
by paying a march.
- CLASS: INCOMPLETE (claims-to-code gap, the AUDIT_claims_to_code
  genre).
- CITE: a1_toc_variational_jax.py:18-21 ("Lip/class monitors (slope
  positivity, supersonic wall) are DECLARED monitors at instance, not
  active constraints") — grep of the carrier finds no slope-positivity
  computation on any path (only the docstring and the unrelated margin
  check at 1395); M0:1624-1637 (the taxonomy text: the recognized
  remedy is to QUANTIFY before violation).
- GAP: wall slope y'(x) is CLOSED-FORM in W (spline_eval line 162-164:
  linear in ys, M — and M is linear in ys), so per-interval slope
  bounds are an analytic pre-march check costing microseconds; today an
  inadmissible trial wall (slope wiggle from Finding 1's curvature
  wave) is detected only by the axial-margin rejector MID-march, at
  full record cost, and lands in the rejected_designs ledger as a
  certifiability event when it was a GEOMETRY event — conflating the
  two pollutes the active-constraint diagnosis of record (the S20
  "crawl along the certifiability frontier" reading rests on rejections
  being physics, not representable-in-closed-form geometry).
- SOTA REFERENCE: a-priori geometric admissibility constraints in shape
  optimization (linear control-point constraints, IGA practice; CST
  class-function positivity by construction; cubic-spline interval
  slope extrema in closed form).
- EXTREMAL CASES: (E1) eps -> 100 long bell: near-zero slope sections
  where a trial step flips sign between stations (stations sample at
  Nw points; the analytic minimum lives between them); (E2) trial steps
  at tr_cap after enrichment near the frontier: the optimizer probes
  the largest geometry excursions exactly where marches are most
  expensive. EVERYDAY: every TR trial evaluation in every segment —
  currently marched blind.
- FIX SHAPE (additive, no gate weakened): closed-form per-interval
  slope extrema check as a pre-march monitor + a REJECTED-BY-GEOMETRY
  vs REJECTED-BY-CERTIFICATION tag in rejected_designs; the march
  rejectors stay untouched as the verdict layer.

## FINDING 8 — Insertion sites are chosen in physical x on the current
design, but the class stores normalized xi: knots silently migrate when
thB moves at the next re-optimization.
- CLASS: RIGOR-GAP (small, but unmonitored and in the mass-carrying
  region).
- CITE: adaptive_knot_optimize.py:424-425 (xi_new = (sites - xB)/(L -
  xB) at the CURRENT thB), a1_toc_variational_jax.py:176-179 (xs = xB +
  (L - xB) * xi at the LIVE thB); S18 record: thB moved 18.85 -> 15.55
  deg in one optimization (xB 0.145 -> 0.121, a ~17% shift of
  near-attachment knot positions).
- GAP: the indicator attributes residual mass to PHYSICAL wall stations;
  the knot is stored as xi and re-anchored to whatever xB the next
  optimum picks — so the dof lands away from the station it was
  inserted to resolve, worst exactly where mass concentrates (first
  interval after the attachment, 41.8%). No monitor measures the
  drift |x_knot(thB_new) - x_site| against the local interval, so a
  cycle can insert, migrate, and re-mark the SAME interval — reading as
  indicator persistence when it is anchor drift.
- SOTA REFERENCE: arc-length/feature-anchored knot parametrization
  (curvature-anchored knots, CAGD standard; FITPACK re-runs placement
  per fit rather than carrying normalized knots across geometry
  changes).
- EXTREMAL CASES: (E1) thB near its class boundary (ideal eps=4 max
  wall angle 11.44 deg, S17): enrichment cycles that trade thB against
  nodes move xB per cycle -> cumulative knot migration across cycles;
  (E2) short-L deep-DEF: (L - xB) small, so d(x_knot)/d(xB) = 1 - xi
  amplified relative to interval width. EVERYDAY: any cycle whose
  re-optimization moves thB by ~1 deg (~0.008 in xB, ~15% of the first
  uniform interval at m=8).
- FIX SHAPE (additive): print + band the per-cycle knot drift; if it
  exceeds the marked interval's width fraction, re-derive xi from the
  NEW xB before the next indicator pass.

---

## DROP COUNT AND DROPPED CANDIDATES (declared)
4 dropped: (i) CST/Hicks-Henne/FFD as standalone findings — folded into
Finding 1 (CST/H-H are global-support: no locality win; FFD solves a
2D/3D embedding problem the 1D wall does not have — same reasoning the
D6 survey applied to THB, extended); (ii) uniform-x abscissae vs
curvature-based abscissae — superseded: [X-AKNO] is the adopted,
adjudicated remedy for placement; (iii) xs_of knot-recompute duplication
between adaptive_knot_optimize.py:324-331 and TV.wall_geometry (code
smell, no measured consequence); (iv) kappa_diag attribution
(diagonal-only conditioning evidence) — folded into Findings 1/6 as the
registered off-diagonal-decay probe.

## REGISTERED S25 PROBES (each > 30 s or march-bearing; named cases)
- S25-P1 `notaknot-twin`: one-row spline_coeffs twin, corner mismatch
  r=1/r=2 at W*8 vs the 6.6295e-02 baseline (Finding 2).
- S25-P2 `hess-decay`: |H_ij| vs |i-j| at W*8 (n+1 replays) vs the
  0.243/interval cardinal-decay prediction (Findings 1/6).
- S25-P3 `warmstart-rejector`: arm dev_warm as a derived-floor check on
  the live [X-AKNO] cycle incl. a near-degenerate insertion negative
  control (Findings 3/4).
- S25-P4 `geom-vs-cert tag`: closed-form slope pre-check on the S20
  rejected_designs ledger — how many of the five frontier rejections
  were geometry-representable (Finding 7; touches the S20 reading of
  record, so rejector-grade design first).

## ONE-PARAGRAPH POSITION
The tier-0 class is rigorously BUILT but was adjudicated on one axis
(conditioning — correctly cleared: kappa_diag 3.5-5.4 post-Jacobi,
physics-dominated) while the failing axis is representational: a
C^2 INTERPOLATING basis oscillates in curvature on innocent data
(measured: alternating M-wave, ratio -0.268, the S17 chain), cannot
curve at the lip by construction (natural BC — a named alternative
mechanism for the open [C-O33] corner residual), hides admissibility
between nodes (cardinal amplitude grows ~linearly in knot ratio while
the solve stays benign), and makes every Hessian measurement dense.
None of this requires weakening a gate: the cheapest moves are
certificates and rejectors the class already licenses (exact-nestedness
rejector, closed-form slope pre-check, operator-derived insertion
guard, not-a-knot twin), and the one structural decision — control
points vs interpolation — deserves the same survey-and-adjudicate
treatment free-knot got, this time on the correct axis.
