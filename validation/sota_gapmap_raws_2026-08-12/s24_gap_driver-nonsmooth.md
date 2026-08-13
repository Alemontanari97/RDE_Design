# FACET 4 — OPTIMIZER/DRIVER AT THE NONSMOOTH FRONTIER
## Finder position, S24 gap census — key `driver-nonsmooth`

**Scope of record.** TR-SQP driver `run_trsqp` (a1_toc_variational_jax.py:844-1229)
with measured full Hessian per RK-G segment, scipy `trust-constr` engine
(kickoff §4bis decision of record, docs/rde_nozzle_brick2_kickoff.md:299-411),
binary P4 certification gate outside the KKT system, reject-and-shrink with
ratcheted radius cap. Measured pathology (not remeasured, per mandate):
KKT closes at mild instances (S18: 7.7e-2 <= derived gtol) and stays OPEN at
frontier/deep-DEF instances (S24 runs 1-2: pinned ~1.6e6, then 1.417e6 at the
returned certified base — validation/PROGRESS_2026-08-12_S24_f1b.md steps
12-13), with radius-ratchet exhaustion at TR_FLOOR = 1e-3 as the de-facto
stationarity test (a1_toc_variational_jax.py:1000-1023). Third measured
instance of the class-construction certifiability frontier (S20, S22 mild;
S24 deep-DEF), margin (val) constraint INACTIVE throughout — the binding
family is march CERTIFICATION at healthy val.

**Honesty frame.** Per-cell certification, rejectors, derived tolerances and
RK-G determinism are non-negotiable. Every proposal below ADDS structure
(gradient visibility, certificates, derived constants); none weakens a gate.
The binary P4 gate stays as the verifier of record in every formulation.

**Probes declared.** Three probes were run, total < 5 s CPU, pure
python/scipy in the scratchpad, zero interaction with the running S24
campaign:
- **Probe A** (`probe_A_stopiteration.py`, 0.4 s): decision-flip comparator
  crash reproduction — **CONFIRMED**.
- **Probe B** (`probe_B_frontier_kkt.py`, 2.9 s): 2-D analytic toy, binary
  gate outside vs KS-max surrogate inside the KKT system — Arm 1 exits at
  the radius floor with `res.optimality = 1.0` (KKT OPEN, distance 7.1e-2
  from the true frontier optimum); Arm 2 closes KKT to 4.6e-11 with
  multiplier mu = 0.709 > 0, lands 2.9e-3 from the true optimum (inside the
  KS conservatism offset), and the binary gate never fires on any accepted
  iterate (conservative side held). **The formulation claim is demonstrated
  end-to-end on a problem with a closed-form answer.**
- **Probe C** (inline, < 1 s): installed scipy 1.18.0 source read
  programmatically — `minimize_trustregion_constr.py:403-406`:
  `if canonical.n_ineq == 0: method = 'equality_constrained_sqp' else:
  method = 'tr_interior_point'`. **CONFIRMED** on the installed version.

---

## G1 — The certifiable-set frontier is invisible to the KKT system; the
## C1 field-level rejector, mathematically specified
**Classification: INCOMPLETE** (the F2-owned named item; also NOT-SOTA in
the narrow sense that the repo's own [X-MGOV] machinery already shows the
correct pattern and it is not applied to the binding family).

**Citations.** P4 binary gate at the segment base:
a1_toc_variational_jax.py:935-938 (`raise RuntimeError("P4 gate: ...")`);
P3(ii) binary gate at accepted iterates: :1158-1161; the traced per-cell
certification ratio field ALREADY EXISTS on the replay path
(`cert_diag=True` returns `jnp.maximum(jnp.max(fanW), jnp.max(wallW))`,
:807-809, per-lane ratios via `_ratio`/`_chain_ratios` :682-700) but is
consumed only as a diagnostic hard max, never as a constraint. The margin
governor constraintifies the val field with derived KS machinery
(margin_governor.py:19-50, 166-203) — but S22/S24 measured that val is NOT
the binding family; the binding family (Newton certification ratio) has no
constraint. D6's own tool matrix names "proximal-bundle (nonsmooth)" for
optimization (docs/rde_nozzle_development_plan.md:738) — never built; the
outcome-II branch was declared instead (adaptive_knot_optimize.py:484-501).

**What the C1 field-level rejector SHOULD be, mathematically.** Within one
RK-G stratum (frozen plan P), each real lane i carries the traced,
AD-differentiable certification ratio r_i(W) = ||one extra Newton step|| /
(NEWTON_TOL_FACTOR * eps * scale) — piecewise-smooth in W on the stratum.
The certifiable set on the stratum is C_P = {W : max_i r_i(W) <= 1}. The
correct constraint object is the smooth CONSERVATIVE over-approximation of
the max (KS-max / log-sum-exp upper form, dual to the KS-min already
derived at margin_governor.py:19-29):

    KSmax_rho(r) = r_max + (1/rho) ln( sum_i exp(rho (r_i - r_max)) )
    with the THEOREM-level bounds  max_i r_i <= KSmax_rho(r) <= max_i r_i + ln(N)/rho.

Enforcing **KSmax_rho(r(W)) <= 1 - s**, s = ln(N)/rho, is SUFFICIENT for
per-cell certification (max r_i <= KSmax <= 1 - s + ln(N)/rho = 1); rho is
DERIVED exactly as the governor derives it (rho = K_RICH ln(N) / s_min with
s_min the smallest enforcement resolution — no tuned constant). At a
frontier-pinned point the KKT system then reads grad J = lambda grad g +
mu_c grad KSmax with mu_c > 0: **the frontier is priced, the residual can
close, and outcome-II becomes a representable stationary point instead of a
ratchet exhaustion.** Validity is stratum-local by construction (the ratios
are replay objects on the frozen plan): at every re-record the surrogate is
rebuilt with the new plan — the identical contract the objective already
obeys (P1/P2), and the identical slot the margin_factory already occupies
(a1_toc_variational_jax.py:1179-1182 shows the wiring is a ~5-line append).
The binary P4/P3(ii) record-path gates REMAIN as the verifiers (record-mode
certification is the truth; the surrogate is the optimizer's gradient-visible
inner approximation, and any accepted iterate that fails record
certification still rejects — defense in depth, nothing weakened).

**SOTA reference.** KS constraint aggregation (Kreisselmeier–Steinhauser
1979; Martins lineage — Poon–Martins SMO 2007), already surveyed and partly
adopted for the margin (margin_governor.py:75-85); MPCC/vanishing-constraint
smoothing (Scholtes regularization; Fischer–Burmeister) as the alternative
lineage if the ratio field must stay nondifferentiable at lane activation;
proximal-bundle methods (Kiwiel; named in D6:738) as the fallback engine if
constraintification is rejected.

**Extremal cases.** (E1) Deep-DEF eps = 30, L = 8 (S24 measured: 19-21
segments fencing the frontier, trial cert_worst 1e1..1e7 — a surrogate
constraint with those magnitudes visible in the model would have priced the
frontier at segment 1). (E2) Nearly-degenerate knots after [X-AKNO]
insertion (spline second-derivative solve ill-conditioning drives r_i up
smoothly BEFORE the binary gate trips — exactly the gradient information
the KKT never sees today). (E3) rho -> huge in KS-max: exp overflow unless
the shifted form is used (it is, above) and gradient mass concentrates on
the argmax lane — conditioning must be watched (the governor's derived-rho
discipline transfers). **Everyday case:** the S18 mild instance
(cert_worst ~ 0.5 at optimum): the surrogate constraint is strictly
inactive, mu_c = 0, and the walk is bit-comparable to today's — the
formulation costs nothing where the frontier is far.

**Probe run:** Probe B (above, 2.9 s) — decisive on the analytic toy.
**Registered for S25:** [P-CERTKS] build the KS-max ratio constraint on the
small TCASE instance (eps = 4, NI = 21, Nw = 60, cert_diag lanes), R-GRAD
spot on d(KSmax)/dW vs FD Richardson band, then one short constrained walk
vs the recorded S18 walk (est. minutes-scale, engine session work).

---

## G2 — No B-stationarity certificate at outcome-II: radius-ratchet
## exhaustion is the de-facto stationarity test and the reported "KKT
## OPEN" number is the residual of the wrong problem
**Classification: RIGOR-GAP.**

**Citations.** Exhaustion exit: a1_toc_variational_jax.py:1000-1023
("reject-and-shrink EXHAUSTED at the radius floor ... KKT reported OPEN");
TR_FLOOR = 1e-3 declared, not derived (:897); the S24 record quotes "KKT
OPEN at 1.417e6" for the returned base (PROGRESS_2026-08-12_S24_f1b.md step
13c) — that number is ||grad f + A^T v|| of the problem WITHOUT the
certification constraint, which at a frontier-pinned point measures nothing
about optimality (Probe B Arm 1: the same architecture reports optimality
1.0 forever at a point 7.1e-2 from a true constrained optimum whose true
KKT residual is 0). The S18 seam-pinned discriminator (:1084-1086, flips
persisting at tiny radius) is an honest heuristic, not a certificate.

**What is missing.** At the returned certified base W_c the honest object
is a **B-stationarity certificate over the stratification**: no feasible
descent direction within the certified set, i.e. for the piecewise-smooth
frontier, min_{||d||<=1, d in T(W_c)} max_P grad_P J . d >= -tol_derived,
where T(W_c) is the tangent cone of the certifiable set and P ranges over
the adjacent strata (plans) at W_c. Executably: (i) with G1's surrogate in
the system, scipy's own optimality IS the B-stationarity surrogate residual
and closes (Probe B Arm 2); (ii) without G1, a manifold-sampling check —
sample the plans of the rejected neighbors (already persisted:
`rejected_designs`, :904-912 + s22_rejected_designs.json precedent), assemble
their stratum gradients, and solve the small convex program 0 in
conv{gradients} + normal directions within a derived band. Today outcome-II
cannot distinguish "pinned at a genuine frontier optimum" from "TR machinery
failure at an interior point" — the S24 EQ-v2 H-CLASS qualification (step
14) leans on this distinction and currently rests on the ratchet heuristic
alone.

**SOTA reference.** B-stationarity for MPCCs (Scheel–Scholtes 2000);
gradient/manifold sampling for nonsmooth optimization (Burke–Lewis–Overton
gradient sampling; Larson–Menickelly–Wild manifold sampling, SIOPT 2018);
Clarke-stationarity tests in nonsmooth trust-region frameworks
(Conn–Gould–Toint, Trust-Region Methods §11).

**Extremal cases.** (E1) True frontier optimum exactly ON a stratum seam
(two plans meet): single-stratum gradients are both nonzero yet the point is
B-stationary — today's report calls it "KKT OPEN", indistinguishable from
failure. (E2) Two rejector families crossing (Newton certification + axial
margin rejector, :269-274): the frontier has a nonsmooth corner; a
one-family surrogate certificate is insufficient and the convex-hull test is
the only honest object. (E3) eps -> 100+ frontier instances where J scale
~1e8 makes the raw KKT number ~1e7 "look" catastrophic while the RELATIVE
residual is ~0.1 — cross-instance comparisons (7.7e-2 vs 1.6e6) conflate
scales without a normalized report. **Everyday case:** mild S18 instance —
KKT closes, certificate trivially passes, zero cost.

**Probe run:** Probe B Arm 1 (2.9 s). **Registered for S25:** [P-BSTAT]
assemble the convex-hull stationarity test from the S24 run's persisted
rejected designs + returned base (pure numpy on existing JSON artifacts;
est. < 60 s, but requires re-recording ~5 rejected designs at ~110 s each =
engine session).

---

## G3 — The margin inequality silently moved every constrained walk OFF the
## adjudicated Byrd-Omojokun TR-SQP path onto tr_interior_point; the barrier
## restarts cold at every RK-G segment
**Classification: NOT-SOTA / INCOMPLETE (adjudication).**

**Citations.** Kickoff §4bis read-the-source finding (1): "ANY inequality
or bounds switches to 'tr_interior_point' — the brick-2 driver therefore
passes ... the single LINEAR equality ... to stay on the TR-SQP path of
record" (docs/rde_nozzle_brick2_kickoff.md:335-341). The S22 margin entry
appends `NonlinearConstraint(m_np, 0.0, np.inf)` (a1_toc_variational_jax.py:
1179-1182) — Probe C confirms on installed scipy 1.18.0
(minimize_trustregion_constr.py:403-406) that this switches the method.
Measured consequence already in the record: the S24 multiplier extraction
res.v = +4.8582e4 at an INACTIVE constraint, adjudicated "interior-point
barrier estimate, INFORMATION-ONLY" (PROGRESS_2026-08-12_S24_f1b.md step
13d). So every margin-constrained walk since S22 — including both S24
decisive runs — ran an engine whose §4bis adjudication (Byrd-Omojokun
semantics, callback/state contract, status meanings) was performed for the
OTHER path. The interior-point path was never re-adjudicated at source
level; and because each RK-G segment is a FRESH minimize() call (:1184-1190),
the barrier parameter and slacks restart cold every segment — a known
interior-point warm-start pathology, compounding G4's churn (19-21 segments
= 19-21 cold barrier restarts). Note G1's certification constraint is also
an inequality: adopting it makes tr_interior_point (or a replacement) the
PERMANENT engine, so this re-adjudication is on the critical path of the F2
mandate.

**SOTA reference.** The survey's own named alternatives: filter line-search
interior point (Wächter–Biegler, IPOPT lineage) with documented warm-start
extensions; filter/funnel SQP (Fletcher–Leyffer filter SQP; Uno/Argonot,
kickoff:378-381) which handles inequalities in true SQP form and has no
barrier to restart; SLQP (Byrd–Gould–Nocedal–Waltz). Minimum bar: a §4bis-
grade read-the-source adjudication of `tr_interior_point.py` (barrier update
law, what `optimality` measures on that path, status semantics, multiplier
sign/order in res.v — the S24 res.v convention read covered the extraction,
not the engine).

**Extremal cases.** (E1) A margin-ACTIVE rung (never yet reached): the
barrier's central-path iterates keep strictly-feasible margin — interacting
with reject-and-shrink radius caps in an unadjudicated way (TR radius and
barrier parameter shrink on different logic; livelock analogue of the S20
sticky-shrink defect is untested on this path). (E2) rho -> huge in the KS
margin: the constraint Jacobian concentrates, the barrier Hessian becomes
near-singular, and tr_interior_point's inner CG behavior at a cold restart
is unexamined. (E3) G1 adopted: cert constraint active at EVERY frontier
segment — cold barrier restarts exactly where warm information matters
most. **Everyday case:** derive-stage short walk (margin_governor.py:
359-379, R-G1d) — already runs tr_interior_point today, PASSES, but under
the wrong adjudication label.

**Probe run:** Probe C (< 1 s, source read). **Registered for S25:**
[P-IPADJ] §4bis-grade source adjudication of tr_interior_point (LLM-side,
no compute); optional A/B: one S18-mild walk with the margin constraint vs
the recorded unconstrained walk to measure barrier-restart overhead.

---

## G4 — Curvature policy: fresh full FD Hessian (n+1 gradient evals) per
## segment, with segments averaging ~one productive step — the measured
## dominant cost, and quasi-Newton carry that preserves RK-G determinism
## was never surveyed
**Classification: EFFICIENCY-GAP** (with the T2 practicality falsifier
already FIRED of record on exactly this decomposition).

**Citations.** Full Hessian by forward differences of the exact adjoint
gradient at every segment base: a1_toc_variational_jax.py:1087-1096 (n+1
evals, :1095); driver note (i): "one RK-G segment ~ one productive step, and
the segment cap IS the iteration budget" (:848-852); T2 indicator FIRED with
"cost decomposition: curvature measurement + RK-G re-records dominate"
(:1641-1648). At the S24 frontier: 19-21 segments x (n+1 = 10) gradient
evals for curvature alone, plus a full adaptive re-record (~record-scale,
111 s at 7818 cells baseline) per segment. The policy line "no
Hessian/multiplier carry-over across strata" (kickoff:396-399) is
POLICY-BOUND, not theorem-bound: P2 requires the MODEL be rebuilt on the new
stratum's replay, but a quasi-Newton matrix updated ONLY from accepted
(recorded, certified) iterate pairs is a deterministic pure function of the
walk history — replaying the walk replays the matrix bit-for-bit, so RK-G
determinism and the excursion-bound semantics survive. What breaks across a
stratum is the VALIDITY of old curvature where decisions flipped — which is
localized (the flipped columns), not global.

**SOTA reference.** SR1 trust-region quasi-Newton (Conn–Gould–Toint;
Nocedal–Wright ch. 6 — SR1 is the TR-native update and tolerates
indefiniteness); compact limited-memory representations
(Byrd–Nocedal–Schnabel 1994); structured secant updates that invalidate
only rows touched by changed structure (Dennis–Walker structured
quasi-Newton lineage). A middle policy consistent with the repo's rigor: carry
the quasi-Newton matrix across segments, RE-MEASURE the full FD Hessian only
when the S18 stale-model symptom fires (status-2 xtol collapse with KKT
open, already detected at :1208-1218), and VERIFY the carried matrix against
one measured directional second difference per segment (a rejector, G6).

**Extremal cases.** (E1) Enriched class after [X-AKNO] insertions (m = 10,
12, ...): curvature cost grows linearly per segment in n while segment
count stays frontier-driven — the walk cost scales n x segments x
record-scale. (E2) Deep-DEF 19-21 segment walks (measured, S24: 76 min +
117 min for two rungs — the majority in re-records + Hessian evals at 2 s
each plus per-segment record 111 s-scale). (E3) xtol collapse churn: status
2 with KKT open triggers a FRESH segment including a fresh Hessian even when
zero decisions flipped (:1208-1218) — pure curvature re-measurement of an
unchanged stratum. **Everyday case:** S18 mild 9-dof walk — 10 extra
gradient evals per segment on ~17 segments = ~170 evals for a walk whose
productive steps number ~17.

**No probe runnable at <= 30 s** (needs the engine). **Registered for
S25:** [P-QNCARRY] A/B on the S18 recorded walk: fresh-FD-per-segment vs
SR1-carry-with-rejector; identical-walk determinism check (two runs
bit-compare) + segment-count/eval-count comparison.

---

## G5 — Decision-flip machinery: (a) comparator crashes on length-only plan
## changes (CONFIRMED); (b) any single (N,Nv) flip ends the segment with no
## materiality test
**Classification: (a) RIGOR-GAP (latent crash on the record path);
(b) EFFICIENCY-GAP.**

**Citations.** (a) `first_diff=next(i for i, (a, b) in enumerate(zip(
dec_base, dec_new)) if a != b)` with no default
(a1_toc_variational_jax.py:1169-1173). `dec_*` lists have length n_B + Nw
where n_B = max(1, ceil(thB/da)) is recomputed at every record (:218) and
thB = W[0] is a DESIGN DOF: when an accepted step crosses a multiple of
da = 0.5 deg, the lists change LENGTH; if every overlapping pair is equal
(zip truncates), `dec_new != dec_base` arms the branch and `next()` raises
StopIteration inside the scipy callback — an uncaught crash of the whole
walk, neither a rejection nor a segment end. **Probe A reproduces the exact
expression's failure and shows the one-line repair** (default =
min(len(a), len(b))). Today's instances sit at thB ~ 20-46 deg where a
0.5-deg crossing under radius <= 0.25 is entirely reachable. (b) The
comparator ends the segment on ANY (N,Nv) difference — even one whose
effect on the wall is below the Newton floor — forcing full re-record +
fresh Hessian (G4); measured: "a decision flip fires at almost every
accepted step" (:849-851), "flips growing at small radius" (S24 step 12).
There is no flip-materiality band (e.g., re-record and compare the wall
against the replay's own fidelity tolerance before declaring a stratum
change; a flip that moves nothing measurable is the SAME quadratic model to
within the band).

**SOTA reference.** (a) defensive iterator use — plain correctness. (b)
Piecewise-smooth (PC^1) trust-region methods with active-set anticipation
(Scholtes, Introduction to PC^1 optimization; SLQP active-set prediction,
Byrd–Gould–Nocedal–Waltz 2004): the stratum is changed when the MODEL
changes materially, not when any discrete label changes; the repo already
owns the right materiality metric (replay-fidelity band, :1041).

**Extremal cases.** (E1) thB steep and drifting (deep-DEF seeds: S24 thB =
46.32 deg): every 0.5-deg crossing risks the length-change crash — at
frontier radii the walk lives exactly in dense small steps around such
crossings. (E2) Nw large / stations dense: (N,Nv) indices flip on
sub-band wall changes at almost every step — segment length degenerates to
1 and the driver becomes pure re-record churn (measured S18 note). (E3) A
flip in the LAST column only (lipward), with all upstream identical:
today's full stratum reset discards a Hessian that is exactly valid for
every dof but the lip. **Everyday case:** mild S18 walk — flips fire ~every
accepted step (measured), so (b) taxes every production run today.

**Probe run:** Probe A (0.4 s) — CONFIRMED + repair demonstrated.
**Registered for S25:** [P-FLIPMAT] materiality-gated segmentation A/B on
the S18 walk (flip -> re-record -> compare wall to replay band -> continue
same segment if within band): segment count and determinism comparison.

---

## G6 — The measured Hessian is the only verdict-adjacent measured quantity
## in the driver with no rejector and no derived band
**Classification: RIGOR-GAP.**

**Citations.** a1_toc_variational_jax.py:1087-1096: forward differences of
the exact gradient, step sqrt(eps)*scale (derived, fine), then
`Hw = 0.5 * (Hw + Hw.T)` (:1096) — the symmetrization AVERAGES AWAY the
asymmetry that is the natural error signal of a contaminated FD column, and
nothing checks the result (contrast: the gradient has O3.1 with FD
Richardson band + corrupted-gradient negative control, :1478-1496; the
margin gradient has R-GRAD, margin_governor.py:298-327; every tolerance in
R5 is derived). A wrong Hessian is silent: it degrades the TR model,
inflates rejected steps and radius shrink, and at the frontier is
OBSERVATIONALLY IDENTICAL to certifiability-limiting — i.e., it can
masquerade as the very pathology under study (outcome-II attribution).
Kink risk is real on this objective: `spline_eval` has `searchsorted`
branches (:155-157) and the replay has where-branches; an FD step of size
sqrt(eps)*|W_i| that crosses a knot/branch seam contaminates a full Hessian
column at O(1).

**SOTA reference.** Standard verification of measured curvature: (i)
symmetry-defect band — ||Hw - Hw^T|| BEFORE symmetrization vs a derived
FD-noise bound (Nocedal–Wright §8.1 error model), reject/re-measure on
breach; (ii) one directional second-difference Richardson check per segment
(v^T H v vs the two-step FD of g along v — the exact O3.1 pattern lifted one
derivative); (iii) noise-aware FD steps (Moré–Wild, "Estimating derivatives
of noisy simulations", ACM TOMS 2012) where the gradient carries replay
noise.

**Extremal cases.** (E1) W at a plan-flip seam (the frontier's habitat,
S24): central-difference stencils straddle the seam, H entries O(1) wrong,
TR model mispredicts, radius collapses — indistinguishable from genuine
certifiability-limiting without the rejector. (E2) Nearly-degenerate knots
post-[X-AKNO]: spline coefficient solve conditioning spikes, gradient kinks
sharpen, FD-of-gradient error blows through the unchecked band. (E3) y -> 0
axis cells / M near table edge: state_fn curvature stiffens locally and the
uniform sqrt(eps)*scale step is no longer optimal — a per-column noise-aware
step would be. **Everyday case:** baseline mild instance far from seams —
the check costs 2 gradient evals per segment and passes silently.

**No probe <= 30 s on the real objective** (needs jitted replay).
**Registered for S25:** [P-HESSREJ] symmetry-defect + directional-Richardson
rejector wired into one S18 segment; measure the defect distribution near
vs far from a known flip seam.

---

## G7 — Driver constants that function as verdict thresholds are declared,
## not derived: TR_FLOOR = 1e-3 (the exhaustion test's resolution), tr_cap
## = 0.25, tr0 = 0.05, xtol = 1e-10 at every call site
**Classification: RIGOR-GAP** (R5: "tolleranze derivate, non magiche" —
these are the driver's own tolerances and they gate outcome-II, a
verdict-bearing exit).

**Citations.** a1_toc_variational_jax.py:896-899 (tr0 = 0.05, TR_FLOOR =
1e-3, tr_cap = 0.25 — comments say "S18 clip", no derivation);
the exhaustion exit fires exactly when tr_cap ratchets to TR_FLOOR
(:992-999, 1000-1023), so **1e-3 IS the de-facto stationarity threshold of
outcome-II** (G2) and it lives in SCALED u coordinates whose physical
meaning changes per instance with the measured Jacobi Dv (:1064-1065,
median-normalized — so the floor's physical size depends on the instance's
curvature spread). xtol = 1e-10 hard-coded at margin_governor.py:365, :485
and adaptive_knot_optimize.py:464 — the [X-TOCV] opt stage DERIVED its xtol
("from the Newton floor on W scale", :1519-1521) but the call sites
inherited the literal, not the derivation. Cross-instance statements like
"exhausted at the floor" (S20/S22/S24) therefore compare different physical
resolutions.

**SOTA reference.** Noise-aware trust-region floors: the TR floor should sit
at the radius where the model's predicted decrease falls below the measured
gradient/objective noise (Cartis–Scheinberg probabilistic-model TR
convergence, Math. Prog. 2018; Moré–Wild noise estimation) — the repo
already MEASURES the right noise scale in tol_dp (the O3.1 FD Richardson
band, :1480-1482): a derived floor is TR_FLOOR = K_RICH * tol_dp / ||g||
in u coordinates, per instance, one line. xtol likewise from the Newton
floor on the u scale (derivation exists, propagate it).

**Extremal cases.** (E1) eps -> 100+: J and gradient scales grow ~1e2, Dv
spread widens, the fixed 1e-3 floor is reached at physically LARGER steps —
premature "exhaustion" declaring a false frontier (outcome-II
misattribution). (E2) Very short L / deep-DEF with tight node spacing: node
spacing in u can approach 1e-3, so the floor is coarser than the geometry's
own resolution — the ratchet can exhaust while certified descent still
exists below the floor. (E3) rho huge in the KS margin (or G1's cert
constraint): constraint curvature makes the accepted-step scale << 1e-3
near activity — a fixed floor then reads honest slow progress as
exhaustion. **Everyday case:** the 9-dof bell at eps = 4 — current
constants happen adequate (S18 closed KKT), which is exactly why the gap is
invisible until a frontier instance.

**No probe needed** (documentary). **Registered for S25:** [P-TRFLOOR]
derive-and-swap: recompute S24 run-2's exhaustion with the derived floor
from its own printed tol_dp/||g|| — pure arithmetic on logged numbers,
minutes, no reruns.

---

## G8 — The Jacobi scaling Dv is measured ONCE per walk, from OBJECTIVE
## curvature only, and never revalidated across 19-21 frontier segments or
## against constraint curvature
**Classification: EFFICIENCY-GAP** (conditioning = convergence rate on this
driver, by its own S18 finding).

**Citations.** `if Dv is None:` — measured at the FIRST segment base only
(a1_toc_variational_jax.py:1050-1070), from diagonal objective curvature
(2n gradient evals), then frozen for the whole walk. The S18 note itself
established that conditioning IS the convergence rate on this
fresh-model-per-segment driver (:858-867). At the frontier the walk
traverses 19-21 segments of designs where curvature has demonstrably changed
(the stale-Hessian symptom of :1208-1218 is the same physics); and with the
margin (or G1 cert) constraint appended, the scaled problem's conditioning
is set by objective AND constraint Jacobian rows, but Dv sees only the
objective — a KS constraint with rho ~ 5.75e4 (S24 derive of record)
contributes gradient rows orders of magnitude steeper than the objective's,
un-rescaled.

**SOTA reference.** Affine-invariant Newton/TR scaling refreshed at model
rebuild (Deuflhard, Newton Methods for Nonlinear Problems — affine
covariance); standard practice: refresh diagonal scaling whenever the model
is re-measured (Nocedal–Wright §4.4 scaling discussion); constraint-aware
scaling = equilibrate the KKT matrix rows, not the objective alone (Gill–
Murray–Saunders SNOPT scaling lineage). Since G4 already re-measures the
full H per segment, its diagonal is FREE — refreshing Dv from it costs
zero extra evaluations; the constraint-row scale is one already-computed
gm_np call.

**Extremal cases.** (E1) A margin/cert-constraint-active frontier walk with
rho huge: the interior-point (G3) inner solves see a KKT system with mixed
scales ~1e4-1e6 — inner CG stagnation indistinguishable from TR failure.
(E2) Long frontier walks (19-21 segments, S24): curvature at the returned
base vs the start differs by the same mechanism that makes the frozen
segment Hessian go stale within ONE segment (measured S18); the walk ends
with a scaling measured 20 segments ago. (E3) Post-[X-AKNO] warm start in
an enriched class: new dofs inherit no measured scale until the next walk's
first segment — mixed fresh/stale scaling in the very cycle that probes the
frontier. **Everyday case:** short mild walks (few segments, curvature
near-constant) — the frozen Dv is fine, which is why S18 never saw it.

**No probe <= 30 s.** **Registered for S25:** [P-DVREFRESH] refresh Dv from
each segment's measured diag(H) (zero extra evals) on the S18 walk; compare
segment count and KKT trajectory; determinism bit-check.

---

## Drop count and dropped candidates (declared)
**5 dropped** (mandate cap 8, ranked out or folded):
1. Scale-invariant KKT reporting (raw vs relative residual across
   instances) — folded into G2/G7.
2. MPCC/complementarity reformulation of the joint margin+certification
   frontier as a standalone finding — folded into G1 (alternative lineage)
   and G3 (engine choice).
3. Hessian symmetrization masking asymmetry as a standalone item — folded
   into G6.
4. maxiter_per_seg = 40 / max_segments = 100 as undived budget constants —
   folded into G7 (same class, lower stakes: they are budgets, not verdict
   thresholds).
5. Reuse of the persisted rejected-designs artifacts as an online frontier
   model (learning-flavored warm information for the ratchet) — speculative
   beyond the repo's current evidence standard; the artifacts already serve
   G2's certificate, which is the rigorous version of the same idea.

## Summary position (3 sentences)
The driver's frontier pathology is a FORMULATION gap, not an optimizer
defect: the binding constraint (per-cell Newton certification) exists as a
traced, differentiable field on the replay path but enters the problem only
as a binary outside-gate, so the KKT system provably cannot close at
frontier-pinned points and radius-ratchet exhaustion at an undived 1e-3
floor substitutes for a B-stationarity certificate (G1, G2, G7; Probe B
demonstrates both halves analytically). The engine adjudication has silently
lapsed — every margin-constrained walk since S22 runs scipy's
tr_interior_point, not the §4bis-adjudicated Byrd-Omojokun path, with cold
barrier restarts at every segment (G3, Probe C), while segment churn
(fresh n+1-eval Hessian per ~one-step segment, no flip-materiality test, a
CONFIRMED StopIteration crash on length-only plan changes) makes the
frontier walk pay record-scale costs per productive step (G4, G5 — Probe A;
T2 already FIRED on this decomposition). The fix set is additive to the
rigor culture: KS-max certification constraint with the binary gate kept as
verifier, a convex-hull B-stationarity certificate at outcome-II, derived
TR floor/xtol, quasi-Newton carry updated only from certified accepted
iterates (determinism-preserving), and a Hessian rejector — each named with
its SOTA lineage and an S25-registered probe.
