# S24 GAP POSITION — FACET 1: MARCH MESH / ERROR CONTROL (key: mesh-amr)

FINDER position, 2026-08-12. Scope: uniform NI/Nw/da vs local AMR; Richardson
two-resolution banding validity; the DWR upgrade named-never-built; Sauer
start-line accuracy at extreme rtu/rtd; axis (y->0) treatment; where local
refinement would change verdicts. Sources read whole or in relevant part:
validation/a1_ideal_march_jax.py (1360 ll), a1_march_scan.py (946 ll),
a1_toc_variational_jax.py (header + mesh sections), def_twin_falsifier.py +
o33_bench.py (band machinery), docs/rde_nozzle_theorem_ledger.md §10bis,
docs/rde_nozzle_development_plan.md (§0/§4/item 9), M0 anchors, session logs
S20/S21/S23/S24. HONESTY FRAME: nothing below proposes weakening per-cell
certification, rejectors, derived tolerances, or RK-G determinism; every gap
is about what is MISSING or SUBOPTIMAL on top of that stack.

PROBES RUN THIS SESSION (declared; pure-python numpy, <1 s CPU each, no JAX,
no march — the running S24 campaign untouched): scratchpad/probe_mesh_amr.py.
P-A (Sauer magnitudes) and P-B (axis coefficient bias), results quoted in
F5/F6. All march-consuming probes REGISTERED for S25, not run.

FINDINGS: 8 (cap). DROP COUNT: 4 (listed at end).

---------------------------------------------------------------------------
## F1 — Uniform-everywhere characteristic net; no local refinement of the
##      march despite a MEASURED spatial localization of the goal residual
CLASS: NOT-SOTA (+ EFFICIENCY-GAP).
ANCHORS: a1_ideal_march_jax.py:723-724 (IVL rows uniform: `y_ivl = yt*(1 -
jj/(NI-1))`), :800-801 (arc wall stations uniform in angle: `wall_angle =
da * n_arc`), :936 (exit-line columns uniform: `dxe = (xe-K_pt[0])/(Ne-1)`);
a1_toc_variational_jax.py:33-34 + :337 + :509 (contour stations `x4 = xB +
(L-xB)*k/Nw`, "count Nw frozen", uniform); o33_bench.py:172-176 (refine() =
global joint scaling, the ONLY refinement operation in the repo).
THE GAP: every mesh knob (NI, da, Nw, Ne) is uniform per run and refinable
only globally. Yet the repo ALREADY measured that the goal residual is
spatially concentrated: S20 closure (validation/PROGRESS_2026-08-07_S20_
adaptive.md, step 10) records 41.8% of the optimality residual in the FIRST
post-attachment interval. [X-AKNO] responded on the DESIGN-CLASS side (knot
insertion); the MARCH mesh cannot respond at all — the cells near the
attachment point B, the D' seam, and the terminal characteristic get the
same density as the benign mid-arc. Cost scales O(NI^2)-ish per column
count, so global refinement to sharpen one local band is quadratically
wasteful (record 111 s at 7818 cells, baseline given).
SOTA REFERENCE: output-based (goal-oriented) local mesh adaptation —
Venditti-Darmofal (JCP 2000/2002), Fidkowski-Darmofal (AIAA J 49(4) 2011
review); classical MoC lineage: characteristic point insertion/deletion by
local step-size control (Zucrow-Hoffman, Gas Dynamics Vol. 2, unit-process
step control). Note MoC nets are constrained (points live on
characteristics), so the correct AMR primitive is column-local insertion of
C- lines / wall stations, not cell-splitting — compatible with the
record/replay DAG because insertion happens at RECORD time (RK-G P2 site).
EXTREMAL CASES: (a) eps -> 100+ (defnoz eps=30 already): long straightening
region, D'-seam gradients under-resolved while thousands of benign exit
cells burn budget; (b) thB steep / very short L (deep-DEF): the 41.8%-type
concentration at attachment sharpens, uniform Nw=60 leaves 1-2 stations in
the active interval; (c) NI large with y->0: uniform IVL wastes rows near
the wall where the Sauer data is smooth. EVERYDAY: the eps=4 twin case —
same band quality reachable at fewer cells (loop-speed falsifier pressure,
docs/rde_nozzle_G0_decision.md §4).
PROBE: registered for S25 (needs a march): non-uniform Nw experiment —
geometric clustering of stations toward xB at fixed count vs uniform, band
comparison at the S19 corner row. Not runnable in 30 s.

---------------------------------------------------------------------------
## F2 — Two-resolution Richardson banding with NO observed-order /
##      asymptotic-range verification, and a standing counterexample datum
CLASS: RIGOR-GAP.
ANCHORS: a1_ideal_march_jax.py:88-93 ("both codes are 2nd order on the same
construction ... K = 4 (two-level Richardson safety, covers the cross-code
constant)" — ASSERTED, never measured), :146 (K_RICH = 4), :1099-1117
(contour_compare band = K*(e(x)+floor)); def_twin_falsifier.py:63-67
(every F-branch band built on the same two-resolution estimate);
o33_bench.py:96-105 (S21 honesty rewrite — bands DECLARED Richardson).
COUNTEREXAMPLE DATUM OF RECORD: the f2 drift GROWS under mesh refinement at
fixed design, 9.4809e-03 (r=1) -> 1.4155e-02 (r=2) (validation/PROGRESS_
2026-08-11_S21_order.md step 5; docs/rde_nozzle_P2_outline.md:23-25; M0
:1898-1899). The repo handled it honestly (band widened because of it), but
it is direct evidence that at these instances some functionals are NOT in
the asymptotic range at (h, h/2) — and the same two-mesh machinery is used
for every other band with the asymptotic premise unchecked. A two-mesh
difference outside the asymptotic range is not an error ESTIMATE, only an
error INDICATOR; K=4 covers a constant, not a wrong exponent. The corner
row is already recorded as "converging in BOTH the design-class and mesh
limits but NOT confirmed at a Richardson band" (dev plan :866-868, ledger
:460) — exactly the signature this gap predicts.
SOTA REFERENCE: observed-order verification + GCI — Roache (Grid
Convergence Index, J. Fluids Eng. 1994); Celik et al. / ASME V&V 20-2009
five-step procedure: THREE meshes, observed p = ln((f3-f2)/(f2-f1))/ln(r),
asymptotic-range check via GCI ratio ~ r^p, factor of safety tied to
whether p is observed or assumed.
EXTREMAL CASES: (a) deep-DEF defnoz (eps=30): the D' landing-window and
dtheta quantization put a NON-mesh noise floor under the two-mesh
difference — observed order will reveal where the floor bites; (b) m_stop-
dominated regime (see F3): refine until truncation < 1e-5 on Me — the
two-mesh delta then measures the fixed floor and the "band" stops meaning
discretization error; (c) M near table edge (T_TAB_LO/HI): interp-linear
tables inject a first-order component that breaks the assumed p=2.
EVERYDAY: the eps=4 twin S3/S4 band (62/62 in-band verdict) — almost surely
fine, but its asymptotic premise has never been demonstrated even once.
PROBE: registered for S25: three-mesh triplet (NI=11/21/41 or r=1/2/4 via
o33_bench.refine) reporting observed p for wall y(x), Me, f2-drift, corner
row. Each rung is minutes-scale (record ~111 s baseline at production;
reduced case less) — not runnable under the 30 s cap while the campaign
runs.

---------------------------------------------------------------------------
## F3 — Fixed accuracy floors (m_stop = 1e-5, refinement cap 30) are NOT
##      coupled to the mesh, and joint refine() cannot attribute error
CLASS: RIGOR-GAP (+ INCOMPLETE).
ANCHORS: a1_ideal_march_jax.py:862-872 — the code ITSELF declares m_stop
"an ACCURACY FLOOR on the achieved exit Mach, hence a candidate ceiling on
any measured convergence order" (S19 parameterization; default 1e-5 GENO-
mirrored); :883 (it_ref > 30 cap, surfaced by C2-F4 but constant);
o33_bench.py:172-176 (refine(r) scales NI, Nw, da JOINTLY — one knob).
THE GAP: (i) under refinement the truncation error crosses the fixed 1e-5
floor at some r* which has never been located; past r*, Richardson bands on
Me-derived quantities (exit state, straightening region, J) quietly degrade
to floor-noise measurements — the declared "candidate ceiling" was
registered but never MEASURED. (ii) joint refinement confounds the three
error directions (IVL rows, arc angle, contour/exit stations): a band that
fails to shrink cannot be attributed (mesh vs class vs floor), which is
precisely the F1/F4 falsifier logic of def_twin_falsifier.py:47-54 — a
per-direction refinement would make those branches sharper rejectors.
SOTA REFERENCE: multi-parameter grid-convergence decomposition (ASME V&V
20-2009 multiple-discretization-parameter GCI; Eca-Hoekstra, J. Comput.
Phys. 262 (2014) least-squares GCI with independent parameters); floor
scheduling: tie the stop tolerance to the mesh scale (m_stop ~ C*da^2 with
C derived), standard in iterative-error vs discretization-error separation
(same V&V 20 chapter: iterative error two orders below discretization).
EXTREMAL CASES: (a) r=4 ladder at deep-DEF: floor crossover near-certain on
Me; (b) eps -> 100: Me large, the interp exit refinement (GENO linear
wall-angle interpolation, :906-909) operates on a steep M(angle) curve —
cap-30 exits become more likely exactly where the floor matters (C2-F4
surfaces them but the BAND does not absorb them); (c) da -> very small at
fixed m_stop: arc columns proliferate, exit test |M-Me|<1e-5 hit by a
different column — contour topology changes discontinuously vs mesh.
EVERYDAY: every r=2 band in [X-O33B]/def_twin.
PROBE: registered for S25 (march-consuming): m_stop sweep {1e-5, 1e-6,
1e-7} at r={1,2} on the reduced case; report where refined-Me delta stops
scaling. (Pre-authorized by the S19 knob — no carrier edit needed.)

---------------------------------------------------------------------------
## F4 — DWR error bars on J: named in the ledger as "nearly free",
##      consumed by plan §0/C2 and the tool matrix, never built for the march
CLASS: INCOMPLETE.
ANCHORS: docs/rde_nozzle_theorem_ledger.md:681-685 (10bis U3: "the per-phase
adjoints are already available, so the DISCRETIZATION error bar on the
certificate is nearly free. Every Verdict then carries: physical bar +
numerical bar (DWR) + stationarity residual + oracle record"); dev plan
:432 (C2 certificates include "DWR discretization bars") and :717 (tool
matrix row "Error control ... DWR goal-oriented estimates ... all");
M0:312 ("declared bars: |J_exact - J[S*]| <= St|J1| + D2 residual + DWR");
docs/rde_nozzle_claims_verdict.md:217. What EXISTS instead: [X-AKNO]'s
f2-drift indicator adjudicated "DWR-conformant" (adaptive_knot_optimize.py
:16, M0:1507-1509, dev plan :886) — but that object drives KNOT insertion
in the DESIGN class; no adjoint-weighted DISCRETIZATION bar on J for the
MARCH mesh has ever been assembled, so every shipped Verdict carries a
Richardson band where M0:312 promises a DWR term.
THE VALUE: the whole-march vjp exists and is O3.1-verified ([X-A1IM] S6,
[X-SCANM], [X-TOCV] O1) — the dual weights are literally one vjp call; the
primal cell residuals are already computed per cell (certification metric).
A per-cell eta_i = |psi_i . R_i(interpolated solution)| estimator would
(i) give the missing J-bar, (ii) decide the S19 "mesh is not the carrier"
attribution CELL-LOCALLY instead of via the global drift-grows-with-mesh
argument, (iii) furnish the marking field F1's AMR needs.
SOTA REFERENCE: DWR a-posteriori (Becker-Rannacher, Acta Numerica 2001);
output-based adaptation for hyperbolic marching (Venditti-Darmofal JCP
2002); Hartmann-Houston (SIAM J. Sci. Comput. 2002, hyperbolic DWR).
EXTREMAL CASES: (a) frontier/deep-DEF outcome-II instances (KKT open at
1.6e6, certifiability-limited): DWR weights localize WHICH cells dominate
the J-error while KKT cannot close — the S20 crawl needed exactly this
(instrumentation gap named at S20 step 9(a)); (b) eps -> 100: J integral
dominated by lip region, DWR would show exit-line cells' negligible weight
=> licensed coarsening (F1 economy); (c) near-degenerate knots after
[X-AKNO] insertion: design-class refinement without mesh response —
DWR bar detects when mesh error re-dominates. EVERYDAY: the eps=4 P-2
freeze numbers — a DWR bar on J would upgrade the freeze's two-knob
wording.
PROBE: registered for S25: one-off DWR assembly at the reduced twin case
(one extra vjp + per-cell residual dot; est. << 1 campaign) with rejector =
sum(eta_i) vs measured two-mesh J-delta within K_RICH.

---------------------------------------------------------------------------
## F5 — Sauer start line: the transonic series is OUTSIDE its
##      small-perturbation regime already at the record case, gamma=const,
##      with a mirrored magic offset — and no start-line rejector exists
CLASS: RIGOR-GAP (+ NOT-SOTA at extremes).
ANCHORS: a1_ideal_march_jax.py:719-727 (alpha, c1, c2, eshift; `x_raw =
c1*y_ivl**2 + 0.000001` — the 1e-6 is a GENO-mirrored magic constant, the
only underived literal on the IVL); :662+:719 (gm = tab["gammamedio"]: the
IVL is gamma=CONST while the march is EOS-general — declared as the twin
DATA CONTRACT, :37-40, but it is also an accuracy statement); same formulas
duplicated a1_march_scan.py:334-341 and a1_toc_variational_jax.py (IVL
block). DECLARED at :38-40 that this "is the shared DATA CONTRACT ... not a
solver step" — fine for the GENO twin comparison, NOT fine as the sole
start-line for verdicts at other (rtu, rtd).
PROBE P-A RUN (this session, pure python from the code's own formulas,
<1 s, scratchpad/probe_mesh_amr.py): wall-row velocity-perturbation
magnitude of the Sauer expansion u/as = 1 + alpha*x + c2*y^2:
  rtu=1.5 (record twin/defnoz): total u-perturbation = 0.50 (50% of a*!)
  rtu=0.5:  1.50 (series formally meaningless)
  r=0.1 (the S24 panel's Rao-Beck Table-1 throat r_down=0.1): 7.50
  rtu=4.0:  0.19
So the "first-order transonic approximation" carries a 50%-of-critical-
speed perturbation at the wall row of every record case, and the panel's
own pre-registered extreme instance (r=0.1) is beyond any perturbative
license. The march downstream is certified per-cell, but the DATA it
certifies against are start-line-model-limited, and NO rejector measures
this: there is no start-line invariance test (re-run with the IVL displaced
downstream via a few marched columns; contour must move < band) and no
higher-order start to difference against. The Richardson band does NOT
cover it: both resolutions use the SAME Sauer model, so the IVL model error
is invisible to e(x) by construction — a systematic error the band
machinery structurally cannot see (same blind spot the docstring itself
notes for the thermo route, but never stated for the IVL).
SOTA REFERENCE: higher-order transonic start — Kliegel-Levine (AIAA J 7(7)
1969, toroidal-coordinate expansion, built for small normalized throat
radius, standard in TDK/Rao-lineage codes); Hall (QJMAM 15(4) 1962,
axisymmetric throat series to higher order); start-line invariance as the
rejector (displaced-IVL consistency check — MoC folklore, e.g.
Zucrow-Hoffman IVL sensitivity discussion).
EXTREMAL CASES: (a) rtu -> 0.5 or the panel r=0.1 case (compact RDE
throats): Sauer invalid, contours would be model-limited not mesh-limited;
(b) eps -> 100 / deep-DEF: mdot from Simpson over the Sauer u_ivl fixes Me
via leggeAree — the start-line model error propagates INTO the exit-Mach
target itself, hence into D' localization; (c) rtu large (gentle): the
everyday-safe direction. EVERYDAY: rtu=1.5 twin — cross-code agreement
7.6e-9 vs GENO proves twin FIDELITY, not start-line ACCURACY (both share
the model; the docstring says exactly this for thermo constants).
PROBE: registered for S25: displaced-start-line invariance rejector at the
reduced case (march 3 columns, restart from marched data, compare contour
to band) — march-consuming.

---------------------------------------------------------------------------
## F6 — Axis (y->0): formally consistent but VERIFICATION-FREE at march
##      level, while the program's open "near-axis mechanism" residual
##      (owner F2) sits exactly there
CLASS: INCOMPLETE.
ANCHORS: a1_ideal_march_jax.py:488-499 (resid_axis: source coefficient from
um, vm, ym = 0.5*(u1+u4), 0.5*v1, 0.5*y1 => the v/y ratio equals the FOOT
value v1/y1); :566 (predict_interior GENO guard `v1/y1 if y2 == 0.0 else
v2/y2`); :853 (axis M is the EXIT-CONDITION read point: `Max` from the axis
cell feeds the m_stop decision); exit Mach measured ONLY at the axis =>
axis-cell accuracy gates the whole exit topology. Program context: the
near-axis mechanism is a DECLARED OPEN residual, owner F2 (S23 close commit
6225969; PROGRESS_2026-08-12_S24 line 78/98 "near-axis mechanism = F2");
S20 step 9(a): stalling-cell localization was an instrumentation gap.
PROBE P-B RUN (this session, pure python, <1 s): for smooth v(y) = a*y +
b*y^3, the scheme's axis coefficient (foot ratio a + b*y1^2) vs the true
midpoint ratio (a + b*y1^2/4): bias = 0.75*b*y1^2, measured bias/y1^2 =
1.5 = const across y1 = 0.5 -> 0.0625. VERDICT OF THE PROBE: the axis
treatment is formally CONSISTENT (O(h^2) coefficient bias -> no order
break) — I explicitly do NOT claim an order defect. The gap is that this
is a hand argument, not a march-level verification: there is NO axis-local
known-answer oracle at march level (the gconst march oracle is inherited
from planar/spike level, :69-72 "not duplicated here"), no MMS/manufactured
axisymmetric solution exercising the y->0 cells, and no axis-only
refinement isolating axis error from the joint refine(). Meanwhile mu =
arcsin(1/M) and the razor-thin near-sonic cells (:544-546) make the axis
column the numerically hardest row, and every deep-DEF verdict reads Me
there.
SOTA REFERENCE: MMS order verification (Roache, "Code Verification by the
Method of Manufactured Solutions", J. Fluids Eng. 2002) specialized to the
axis cell; axis unit-process treatment with the L'Hopital limit v/y ->
dv/dy carried as a derived quantity (Zucrow-Hoffman, Gas Dynamics Vol. 2,
axis-of-symmetry point process — their discussion is the lineage the GENO
guard descends from).
EXTREMAL CASES: (a) NI large: first off-axis ring y ~ yt/(NI-1) -> 0, the
foot ratio v1/y1 becomes 0/0-adjacent in float; (b) deep-DEF defnoz: the
terminal characteristic and the focus K live at the axis — Me_ach error =
axis-cell error, feeding D' and F1/F2 branch bands; (c) corrupted-source
N1 direction (delta flipped) shows the axis source dominates rejection —
its accuracy is verdict-load-bearing. EVERYDAY: eps=4 base march (axis
cells pass Newton certification — ALGEBRAIC convergence, which says nothing
about the DISCRETIZATION order at the axis; the two are distinct layers and
only the first is instrumented).
PROBE: registered for S25: march-level gconst axis oracle — compare axis
M(x) against the closed-form characteristic solution on the gconst backend
at two NI; cost = 2 reduced marches.

---------------------------------------------------------------------------
## F7 — D'-localization and the F1/F2 falsifier bands are grid-cell-limited;
##      LOCAL refinement at the D' seam is the named lever nobody holds
CLASS: EFFICIENCY-GAP (+ INCOMPLETE toward the F1b verdict sharpness).
ANCHORS: def_twin_falsifier.py:296 (position bands from local |dval/ds|
around D'), :350 (`band_v = K_RICH*dval_ds*cell + LAND_WIN`), :380-384
(D'12 agreement band = K_RICH * max cell), :404 (`band_dprime = K_RICH *
max(dp["cell"], ds_land)` — the D' band is FLOORED BY THE GRID CELL),
:1120-1127 (combined F1 band inherits it), :1146-1147 (F2 band likewise);
:16-17 + :321-325 (GENO side at NI=401/2001 and halved — global only, and
the halved direction already trips a GENO outer-TOC quirk at NI=201).
THE GAP: the branches that adjudicate EQ-v2 (F1, F2) carry bands whose
floor is the LOCAL grid cell at the D' seam. Under the ONLY available
refinement (global r -> 2r) the cell shrinks linearly while cost grows
~quadratically, and the GENO leg cannot even refine freely (NI=201 quirk).
Column-local insertion of C- lines in the terminal-characteristic /
D'-seam region would shrink band_dprime at ~linear cost and could flip a
"gap <= band" PASS into a discriminating verdict (or a genuine FIRE) —
i.e. local refinement here CHANGES VERDICT SHARPNESS, which is the facet
question. Same logic applies to the S19 corner row (only mesh-limit
convergence shown, never in-band confirmation — dev plan :866-868): local
refinement at the corner/control-surface junction is the cheapest path to
the missing in-band confirmation.
SOTA REFERENCE: feature-targeted local refinement driven by a-posteriori
indicators (Bank-Weiser residual indicators lineage; for goal quantities,
the DWR marking of F4 — Becker-Rannacher); in MoC specifically,
characteristic insertion near limiting characteristics (Rao-lineage TDK
practice of clustering mesh at the control surface).
EXTREMAL CASES: (a) deep-DEF defnoz eps=30 (the LIVE S24 instance): D'
band floored at the NI=401 cell on the GENO leg; (b) very short L /
steep thB: D' migrates toward the corner, cell size at the seam grows
relative to the feature; (c) dtheta_pm quantization (-0.001 step): at
extreme instances ds_land dominates cell — local mesh refinement then
provably CANNOT help (the band is landing-window-limited), which the
current machinery cannot distinguish; an explicit cell-vs-window
attribution print is a 3-line upgrade. EVERYDAY: the eps=4 twin F1/F2
rows.
PROBE: registered for S25 (the attribution print + a seam-clustered Nw
experiment); nothing 30 s-safe exists (every leg is a march or a GENO WSL
run).

---------------------------------------------------------------------------
## F8 — K_RICH = 4: one asserted safety constant reused across
##      heterogeneous roles, including NON-Richardson ones
CLASS: RIGOR-GAP (mild, hygiene-grade).
ANCHORS: a1_ideal_march_jax.py:92-93 ("K = 4 ... covers the cross-code
constant" — coverage asserted, never derived or measured); reuse OUTSIDE
Richardson semantics: a1_toc_variational_jax.py:196+:1403 (P4 instance
margin floor `delta_inst = min_margin/K_RICH` — a mesh-band safety factor
repurposed as a margin-floor divisor), def_twin_falsifier.py:757 (KS
aggregation sharpness `rho = K_RICH*log(N)/ladder` — K_RICH as a KS
parameter scale), :647-668 (padding constants -K_RICH*m_ref).
THE GAP: R5 demands DERIVED tolerances; K_RICH=4 in the Richardson role is
a defensible convention (Roache's two-grid factor-of-safety Fs=3 is the
comparable SOTA number — the repo is conservative), but (i) it is tied to
an ASSUMED p=2 (F2: once observed order is measured, the factor should be
conditioned on it, exactly as GCI does: Fs=1.25 with observed p, 3 without)
and (ii) its reuse as a margin-floor divisor and a KS sharpness scale
carries no derivation linking those roles to two-level Richardson safety —
same numeral, three meanings. Each reuse is declared in-code (honest), but
declared-not-derived is precisely the R5 boundary.
SOTA REFERENCE: GCI factor-of-safety methodology (Roache 1994; ASME V&V
20-2009: safety factor conditional on observed-vs-assumed order); for KS
sharpness, the standard derivation ties rho to the constraint-field
Lipschitz scale (Kreisselmeier-Steinhauser 1979; Poon-Martins, Struct.
Multidisc. Optim. 2007 adaptive-rho), not to a mesh-band constant.
EXTREMAL CASES: (a) rho -> huge in KS (the facet's own extremal): with rho
= K_RICH*log(N)/ladder, a tiny measured ladder blows rho up — conservatism
flips side; (b) observed p < 2 at deep-DEF (per F2): K=4 no longer covers
even the Richardson role; (c) margin-floor role at a barely-certified
optimum (min_margin small): /4 is arbitrary exactly where the floor gates
P4. EVERYDAY: every band in every carrier (the constant is global).
PROBE: none needed to establish the finding (it is structural); the F2
triplet probe (S25) supplies the observed-p input the fix consumes.

---------------------------------------------------------------------------
## DROPPED (4, declared per mandate):
D1 linear mass-flow crossing interpolation for the bounding-streamline wall
   point (a1_ideal:985-988) — O(h^2)-consistent with the scheme order, no
   gap survives analysis. D2 Simpson IVL mass flow requires NI odd
   (weights :739-741) — a usability constraint, parity never checked, but
   sub-verdict-grade. D3 arc NT-limit 4000 hard cap (:797) — mirrored GENO
   constant, raises loudly (honest refusal), not a rigor gap. D4 the
   it_ref<=30 / interp-exit interplay — already surfaced and rejector-gated
   by C2-F4 (S21); residual risk lives inside F3's floor-coupling finding.

## S25 PROBE REGISTRY (named, march-consuming, NOT run this session):
P-S25-1 three-mesh observed-order triplet (F2/F8) — wall y, Me, f2-drift,
        corner row at r=1/2/4.
P-S25-2 m_stop sweep {1e-5,1e-6,1e-7} x r={1,2} floor-crossover map (F3).
P-S25-3 one-off DWR assembly + sum(eta) vs two-mesh J-delta rejector (F4).
P-S25-4 displaced-start-line invariance rejector (F5).
P-S25-5 march-level gconst axis oracle at two NI (F6).
P-S25-6 D'-band cell-vs-landing-window attribution print + seam-clustered
        Nw experiment (F7, F1).

## PROBES RUN THIS SESSION (cost ledger):
P-A Sauer perturbation magnitudes — pure numpy, <1 s CPU.
P-B axis coefficient bias order — pure numpy, <1 s CPU.
Script: scratchpad/probe_mesh_amr.py (committed to scratchpad only).
No JAX import, no march, no GENO run: the running S24 campaign was not
touched.
