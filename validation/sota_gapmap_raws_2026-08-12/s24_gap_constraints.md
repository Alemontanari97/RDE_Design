# FACET 5 — CONSTRAINT MACHINERY: gap position (S24 finder)

Finder: constraints facet. Sources read whole: `validation/a1_toc_variational_jax.py`,
`validation/margin_governor.py`, `validation/def_twin_falsifier.py` (constraint sections),
`validation/PROGRESS_2026-08-12_S24_f1b.md` (steps 1-15), anchors in `docs/rde_nozzle_development_plan.md`,
`docs/rde_nozzle_theorem_ledger.md`, `validation/o33_bench.py`.
HONESTY FRAME: nothing below proposes weakening the per-cell certification, the rejector
discipline, derived tolerances, or RK-G determinism. Every gap is missing/suboptimal machinery
AROUND that non-negotiable core. Probes P1-P3 RUN (pure numpy, analytic, < 5 s total, declared
below; no jax, no marches — the running S24 campaign untouched). Probes R1-R3 REGISTERED for S25.

**Findings: 8 kept, 5 dropped** (drop list at end).

---

## G1 — KS rho derived from conservativeness only: at rho = 5.75e4 the "smooth" aggregate is a hard min to machine precision (gradient one-hot, curvature ~ rho/4)

**Anchors**: derivation `validation/margin_governor.py:25-29` (rho = K_RICH ln(N)/mu_0_min) and
`:281-283`; instance value `validation/def_twin_falsifier.py:756-757` + PROGRESS S24 step 9
(rho = 5.7518e4, N = 45, m_ref = 4.2357e-3); the adopt-or-declare survey that dismissed
adaptive-rho `margin_governor.py:75-85`; KS gradient path `margin_governor.py:195-198`,
`def_twin_falsifier.py:643-646`.

**Classification**: NOT-SOTA (secondarily RIGOR-GAP on the smoothness premise).

**The gap.** rho is derived to pin the conservativeness gap ln(N)/rho below the enforcement
resolution — correct and honest. But nothing in the derivation controls the *other* two things
rho does: (i) the KS gradient is the softmax weight vector w_i = e_i/Σe; (ii) the KS curvature
along the min lane is rho·w(1-w) ≤ rho/4. **Probe P1 (RUN, numpy, <1 s)** at the recorded S24
values: with lane spacing ~8.7e-4, w2/w1 = 2.28e-22 — exactly ONE lane of 45 carries weight
above 1e-12, i.e. the constraint gradient the SQP consumes is the hard-min one-hot gradient;
when two lanes tie within 1e-6 the gradient l_inf-JUMPS by 2.9e-2 across the argmin swap (vs
gtol-scale quantities), so the constraint is C^0-but-effectively-nonsmooth exactly where the
active-cusp census says multiple cusps matter (F6 semantics). Curvature scale rho/4 = 1.44e4
(times |∇_W val|²) enters the Lagrangian Hessian. At S22-mild (rho = 766.83) the same probe
gives 18/3059 weighted lanes — the derivation is instance-sensitive in a way never declared:
mild instances get a genuine smooth aggregate, deep-DEF gets a hard min. The survey's
NOT-ADOPTED reason (`:79-85`, "adaptive rho tunes accuracy under budget; ours is derived")
answers the *accuracy* attack but not the *conditioning* one — the wrong theorem was cited
against the right technique.

**SOTA**: adaptive-KS (Poon–Martins, SMO 2007); induced-exponential / induced-power aggregates
with bounded curvature and two-sided estimates (Kennedy–Hicken, CMAME 2015, "Improved
constraint-aggregation methods"); classic KS lineage Kreisselmeier–Steinhauser 1979 with the
Raspanti et al. 2000 smoothing-error bound. A derived TWO-CONSTANT rule (rho from the gap AND a
declared curvature/weight-support budget, taking the max-feasible not the min-necessary
smoothing) keeps R5 intact.

**Extremal cases**: (E1) deeper ladder or smaller m_ref — rho ∝ 2^k/m_ref: a k = 6 ladder at
m_ref ~ 1e-4 gives rho ~ 1e7, curvature 2.5e6; (E2) two DE lanes tied within 1e-6 near the
crossing (geometrically expected: neighbouring chain nodes straddling val = 0 have nearly equal
val), argmin swap per optimizer step = gradient chatter the TR attributes to model error →
radius collapse indistinguishable from the certification fencing signature; (E3-everyday)
eps = 4, N = 3059: 18 weighted lanes, healthy — the everyday case HIDES the defect, which is why
it survived S22 green.

**Probe**: P1 RUN (declared above). R3 REGISTERED for S25: count argmin-lane swaps along the
recorded S24 walk from the persisted rejected/accepted designs (needs replay, not runnable now).

---

## G2 — Rung-frozen chain mask: granularity provably wrong at deep-DEF (drift 14 nodes, drift_val > mu0), and the fix is already in the codebase's own semantics (segment-level re-freeze at RK-G P2), with a differentiable parametrization as the F2-grade upgrade

**Anchors**: freezing declaration `validation/def_twin_falsifier.py:487-490`; rung-frozen build
`:945-954`; C3 gate `:1000-1028`; measured firing PROGRESS S24 step 12 (i_cross 96 → 82 =
**14 nodes**, 2.465e-1 in position, frozen-vs-rederived val_min delta **9.188e-3 vs
mu0 = 2.1178e-3**); budget consequence step 12 ("the C3 repeat is COUNTED AS DECISIVE RUN 2 of
the max-2 budget").

**Classification**: INCOMPLETE (granularity) + RIGOR-GAP (gradient/enforcement inconsistency is
detected only per-rung, after up to ~76 min of walking on a stale mask).

**The gap.** The enforced constraint is m_frozen(W) = KS over mask(W_rung-start) lanes, while the
adjudicated object is m_true(W) = KS over DE(W). The AD gradient is exact for m_frozen — but
m_frozen ≠ m_true as soon as the crossing moves, and S24 run 1 measured the divergence at
**4.3x the enforcement floor** (drift_val 9.188e-3 vs mu0 2.118e-3): for 21 segments the SQP
priced a floor that was semantically stale by more than the floor itself. C3 caught it — the
rigor culture worked — but the repair granularity (repeat the whole rung once, else CONFOUNDED)
cost one of two decisive runs. The codebase already re-freezes the *plan* at every RK-G P2
segment boundary (`a1_toc_variational_jax.py:41-48`, callback re-record `:1135-1176`); the mask
is the ONLY W-dependent frozen object excluded from that rhythm. Segment-level re-freeze (rebuild
mask from the fresh record at each accepted-iterate re-record; the record is already computed —
marginal cost ≈ one chain walk, milliseconds) makes the drift detector's window one segment
instead of one rung, and the C3 drift budget per window shrinks with the trust radius, i.e. it
inherits the excursion-bound semantics the driver already has. The differentiable alternative —
replace the boolean DE mask with a smooth gate σ(val/ε_gate) with ε_gate derived from the KS gap
(so the gate transition lives inside the band already declared unresolvable) — removes the
frozen-mask object entirely and puts the crossing's W-sensitivity INTO the gradient; it is the
F2-grade formulation, not driver surgery (it edits `make_margin_fn_cs` only).

**SOTA**: smoothed Heaviside projection (Guest–Prévost–Belytschko, IJNME 2004, topology
optimization lineage — exactly the "differentiably parametrized mask" technique); implicit
differentiation of the crossing location as a root of val along the chain (implicit-function
lineage, Griewank–Walther; modern statement Blondel et al. 2022 "Efficient and modular implicit
differentiation"); freezing-granularity-matched-to-stratum = Conn–Gould–Toint trust-region
semantics the driver already follows for the plan.

**Extremal cases**: (E1) deep-DEF rung 1 — MEASURED (14-node drift, run-budget consumed); (E2)
crossing within STENCIL_RADIUS of the lip end: DE bucket = 2-3 lanes, a 1-node drift is a 30-50%
bucket change and KS over N = 2 has gap ln2/rho ≈ 1.2e-5 — the C3 node-count gate
(drift > STENCIL_RADIUS) is then TOO LOOSE relative to the bucket it protects (gate constant is
absolute, bucket-relative would be derived); (E3-everyday) mild eps = 4, no crossing: mask
degenerates to the whole registered CS, freezing is vacuously correct — again the everyday case
hides the defect.

**Probe**: none runnable ≤ 30 s (needs marches). R1 REGISTERED for S25: replay the recorded run-1
segment bases (persisted W sequence) through `cs_stats` and measure i_cross per SEGMENT to
establish whether the 14-node drift accumulated smoothly (segment re-freeze would have tracked
it) or jumped in one segment (needs the differentiable gate).

---

## G3 — Mask shape-adaptation crop can silently DROP enforced lanes: the event is counted, the enforcement loss is not

**Anchors**: `validation/def_twin_falsifier.py:618-625` (crop/pad: `mm[:r,:c] = mask[:r,:c]`);
frac_bad denominator recomputed on the CROPPED mask `:640,648`; 16 shape adaptations counted in
decisive run 2, PROGRESS S24 step 13(a).

**Classification**: RIGOR-GAP (narrow but real: a counted event is not a bounded event).

**The gap.** When the replay lane grid is smaller than the frozen mask's grid, True mask entries
beyond the overlap are discarded. A discarded True lane is neither enforced (not in the KS) nor
penalized (frac_bad's denominator n_sel = mloc.sum() is the CROPPED count, so the lane vanishes
from both numerator and denominator). The counter `mask_shape_adapt` records that *an* adaptation
happened, not *whether enforcement shrank*: 16 adaptations in run 2 are declared, but the number
of True-lanes lost per adaptation is unmeasured — it could be 0 every time (likely: the DE chain
sits at low k/i indices) but "likely" is not the repo's standard; every other masked reduction in
this codebase carries an invariant (C5 mapping identity, C4 lane-count declaration). One line
fixes it: count `mask.sum() - mloc.sum()` per adaptation and make nonzero loss verdict-bearing
like the nonfinite counters (`margin_governor.py:47-50` pattern).

**SOTA**: this is the repo's own counted-events discipline applied one level deeper
(conservation-of-enforcement invariant); no external lineage needed — the nearest named pattern
is the C4/C5 gate family from the S24 panel advisory itself
(`validation/ADVISORY_S24_DEbucket_panel_2026-08-12.md:222` context).

**Extremal cases**: (E1) plan-topology change that shortens the lane grid rows below the largest
DE k-index — deep-DEF truncation (DoD rule, `a1_toc_variational_jax.py:340-348`) removes trailing
columns exactly where the DE chain lives (lipward = high k): the crop then eats DE lanes
preferentially; (E2) [X-AKNO] knot insertion changing M_NODES between derive and a later rung —
column/lane counts change wholesale and the overlap heuristic is untested there; (E3-everyday)
run 2's 16 adaptations at fixed class — loss almost surely 0, but unmeasured.

**Probe**: R1' REGISTERED (S25, piggybacks on G2's R1 replay): log lost-True-lane count per
adaptation over the recorded run. Not runnable now without marches.

---

## G4 — Lip equality kept as a LinearConstraint row instead of eliminating one variable: pays a Byrd–Omojokun normal step every iteration for a constraint that is a coordinate pin, and takes lambda_e from the solver when AD would give it exactly

**Anchors**: `validation/a1_toc_variational_jax.py:887-888` (A row: single 1 in the last column),
`:1072` (`lip_eq = LinearConstraint(A * Dv[None,:], [yL], [yL])`), docstring `:16-17`
(y_m carries the eps equality); multiplier consumption `:1603-1612` (lambda from res.v[0] feeds
the Pa_impl instance reading) and `margin_governor.py:415-419` ([D1]-constrained metric).

**Classification**: EFFICIENCY-GAP (minor per-iteration cost) with a RIGOR upside forgone
(multiplier provenance).

**The gap.** The equality y_m = yL fixes ONE coordinate. Passing it to trust-constr forces the
equality-constrained SQP path (normal/tangential decomposition) at every iteration of every
segment, for all campaigns, forever — for a constraint whose null space is "delete one column".
Eliminating y_m (optimize over W' = W minus the lip dof, substitute yL) shrinks the problem,
removes the constraint row, and — the rigor half — yields lambda_e = dJ*/dy_L directly by AD as a
post-optimality sensitivity (evaluate ∂J/∂y_m at the optimum with the lip dof re-inserted): the
multiplier of record would then come from the SAME adjoint machinery as every other gradient in
the repo, with an O3.1-style FD check, instead of from scipy's internal estimate whose convention
needed a source-read session (S24-T1) to close. The S24-T1 verdict stands and is correct — this
gap is about not needing it. Note the margin NonlinearConstraint keeps the SQP machinery when
armed, so elimination does not trivialize the driver; it removes exactly the always-on row.

**SOTA**: variable elimination / null-space reduction for linear equalities (Nocedal–Wright,
Numerical Optimization, §15.3); post-optimality sensitivity lambda = dJ*/d(rhs) (Fiacco 1983,
sensitivity analysis lineage).

**Extremal cases**: (E1) eps → 100: yL = 10·yt makes the pinned coordinate's scale dominate the
Dv row; the scaled constraint row A·Dv is then the largest row in the KKT system and conditions
the normal step (elimination is scale-exempt); (E2) nearly-degenerate knot at the lip after
adaptive insertion (x_{m-1} → L): the spline system couples y_{m-1} strongly to the pinned y_m,
and the projected Hessian in the (kept) full space carries that near-singular coupling through
the constraint projection each iteration — in the eliminated space it appears once, in the data;
(E3-everyday) eps = 4, 9 dof: one wasted dof and one constraint row per iteration — measurable
but small; the gap is structural, not a hot spot.

**Probe**: none needed (structural; costs nothing to verify at next driver touch — owner F2, the
only phase licensed for driver surgery per the S21 pin).

---

## G5 — No independent multiplier rejector: res.v is consumed raw; a derived complementarity band + LSQ re-estimate would have flagged the S24 barrier artifact automatically

**Anchors**: `validation/a1_toc_variational_jax.py:1603` (lam = res.v[0], raw); `margin_governor.py:536-544`
(mu_est from res.v, try/except pass — extraction failure is SILENT None); `def_twin_falsifier.py:1032-1040`
(mu = -res.v[-1][0], S24-T1 convention, correct); PROGRESS S24 step 13(d): mu = +4.8582e4 read at
an INACTIVE margin (min DE val 7.31e-2, 33x the floor) — recognized by hand as an interior-point
barrier estimate and demoted to information-only.

**Classification**: RIGOR-GAP.

**The gap.** The convention is closed (S24-T1, of record); what is missing is the *rejector* the
repo's own R5 culture requires for any consumed number: every multiplier that feeds a
verdict-adjacent quantity ([D1]-constrained rel_c via mu_use `margin_governor.py:556-558`;
Pa_impl ratio) is read from scipy internals with no machine check. Two derived checks exist for
free: (i) **complementarity band** |mu·m| ≤ tol_comp with tol_comp derived from gtol × constraint
scale — **Probe P2 (RUN, arithmetic)**: at the recorded S24 stop |mu·m| = 3.55e3 (KKT-consistent
value at an inactive constraint: 0; even relative to J ~ 4.05e7 it is 8.8e-5 » gtol-scale) — the
rejector fires loudly on exactly the case that was caught by hand; (ii) **LSQ re-estimate**:
solve min_v ||∇f + Σ J_iᵀ v_i|| from the repo's own AD gradients at the returned point and
require agreement with res.v within a derived band — this uses only quantities already computed
(g_n, gmv, the lip row) and makes the multiplier a repo-verified object instead of a
solver-trusted one. Also: the `except Exception: pass` at `margin_governor.py:542-543` silently
converts extraction failure into mu_est = None, which downstream becomes mu_use = 0.0 — a silent
zero in the [D1]-constrained metric; the nonfinite-counter pattern (`:47-50`) should apply.

**SOTA**: LSQ multiplier estimates (Gill–Murray–Wright, Practical Optimization, 1981 — standard
SQP practice); three-part KKT termination (stationarity + feasibility + complementarity) as in
IPOPT (Wächter–Biegler, Math. Prog. 2006): the driver currently checks the first two
(`res.optimality`, `res.constr_violation`, `a1_toc:1203-1207`) and never the third.

**Extremal cases**: (E1) certifiability-limited stop — MEASURED (barrier mu 4.86e4 at inactive
constraint; the complementarity rejector is the automatic version of the hand demotion); (E2)
lip-end binding design where ∇g (lip row) and ∇m (margin gradient concentrated on the lip-adjacent
lane by G1's one-hot collapse) become near-parallel: LICQ degradation makes res.v ill-conditioned
with NO warning from scipy — only the LSQ residual detects it; (E3-everyday) the mild S18 optimum
lambda reading feeding the Pa_impl/p_lip ratio 0.???: currently uncheckable against anything.

**Probe**: P2 RUN (declared, arithmetic only). LSQ re-estimate on recorded S18/S24 gradients
REGISTERED (R2', needs the stored artifacts + one adjoint eval each — S25 engine session).

---

## G6 — Missing constraint classes (slope positivity, curvature bounds, manufacturability): declared monitors only, while probe P3 shows they are LinearConstraint rows at fixed thB — the machinery to enforce them is already imported

**Anchors**: `validation/a1_toc_variational_jax.py:18-20` ("Lip/class monitors (slope positivity,
supersonic wall) are DECLARED monitors at instance, not active constraints"); the R-G1 broken
design that must be caught by march failure instead of feasibility `margin_governor.py:331-334`
(gross non-monotone wall as the deliberate beyond-frontier probe); S24 fencing record (PROGRESS
step 12: rejected trial records at worst 1e1..1e7 — trial walls bad enough to fail Newton
certification were PROPOSED and priced by full records).

**Classification**: INCOMPLETE.

**The gap.** The design class admits walls no certified march can accept (non-monotone,
curvature-spiked at the attachment), and the only mechanisms that exclude them are (a) the P4
record gate — a full adaptive march per rejection — and (b) the G1 margin surrogate. Neither is a
*feasibility* statement the SQP can use predictively; both are a-posteriori. **Probe P3 (RUN,
numpy, < 1 s)**: reimplemented the exact clamped-left/natural-right tridiagonal solve of
`spline_coeffs` (`a1_toc:131-150`) and verified that wall slope AND second derivative at any
station are AFFINE in W[1:] at fixed thB (affinity residuals 2.7e-15 / 1.4e-13 = machine floor).
Consequence: slope positivity y' ≥ 0 (or ≥ tan θ_min), curvature bounds |y''| ≤ κ_max
(manufacturability: minimum tool radius; structural: attachment stress), and monotonicity at a
derived station set are ROWS OF A LinearConstraint in (W[1:] | thB fixed) — the exact class
already used for the lip. The thB coupling (one variable) makes them bilinear at worst; a
conservative linearization about the segment base (re-derived per RK-G segment, the established
rhythm) keeps them honest. These would have converted part of the S24 fencing from
"propose → full record → reject → shrink" into "never proposed", without touching the P4 gate
(which remains the adjudicator — the constraint is a cheap outer approximation, the gate stays
absolute). The known SOTA framing of the fencing problem is exactly this: give the optimizer a
priori feasibility structure where it exists, reserve the expensive oracle for what only it can
decide. Note D6's free-knot rejection (`docs/rde_nozzle_development_plan.md:909-916`) is about
knot placement, not about shape-constraint rows — no prior adjudication covers this.

**SOTA**: CST parametrization with class-function bounds (Kulfan, J. Aircraft 2008); B-spline
control-polygon linear constraints via the convex-hull property (parametrization benchmark:
Masters et al., AIAA J. 2017) — note the interpolating natural cubic spline LACKS the convex-hull
property, which is itself a NOT-SOTA data point for the class (B-spline control points would make
slope/curvature bounds sufficient conditions, not station-sampled ones); linear curvature
constraints on splines = standard in structural/aero shape optimization (Haftka–Gürdal lineage).

**Extremal cases**: (E1) deep-DEF walk — MEASURED: 19-21 segments dominated by certification
fencing, trial worsts to 3.4e5, radius ratcheted to floor: some fraction of those trials violate
slope/curvature sanity that a linear row excludes for free; (E2) nearly-degenerate knots after
[X-AKNO] insertion: cubic overshoot between close knots violates slope positivity BETWEEN nodes
while node values look sane — station-sampled linear rows (or the B-spline hull) catch it,
node-value monitors cannot; (E3) thB steep (46.3° defnoz): attachment curvature spike is the
measured representation-error saturation site (PROGRESS step 9: 5.679e-3 → 5.595e-3 M → 2M —
node count doesn't fix it, a curvature-bounded class reallocates dofs there); (E4-everyday)
eps = 4, 9 dof: all such rows inactive at the optimum, cost = a few dot products per iteration.

**Probe**: P3 RUN (declared). Pilot wiring at eps = 4/NI = 21 REGISTERED (R2, S25 engine session —
needs marches).

---

## G7 — The certification frontier is invisible to the KKT system while a TRACED differentiable surrogate of exactly that quantity already exists in the codebase (cert_diag worst) and is consumed only by diagnostics

**Anchors**: binary gate outside the SQP: `a1_toc_variational_jax.py:935-938` (P4 base gate),
`:1158-1161` (P3(ii) accepted-iterate gate), outcome-II return `:1000-1023`; the traced per-lane
certification ratio ALREADY IN THE JIT REPLAY: `:682-700` (`_ratio`, `_chain_ratios`) and
`:807-809` (cert_diag returns traced worst); measured consequence: three campaigns end
certifiability-limited with KKT OPEN (S20 walk; S22 branch (c); S24 runs 1-2, KKT 1.4-1.6e6,
19-21 segments of frontier fencing — PROGRESS steps 12-13); F4 verdict names "the binding
frontier is march CERTIFICATION at healthy val" as the third measured instance.

**Classification**: INCOMPLETE (the highest-leverage gap of this facet; owner F2 by the S21
"no driver work" pin and the F2 mandate that already owns the near-axis mechanism + C1 rejector).

**The gap.** The de-facto binding constraint of the whole program at frontier instances is
cert(W) ≤ 1 — and it appears in the optimization problem ONLY as a non-differentiable outside
gate, so the KKT system is structurally incapable of closing there (outcome-II is not a solver
failure; it is the problem statement omitting its own active constraint). The repo already
possesses every ingredient of the fix: (i) a traced, W-differentiable per-lane ratio
(`_ratio` — smooth in W through the Newton-step norm wherever the solve converges); (ii) the KS
aggregation machinery with derived rho (G1's caveats apply); (iii) the margin_factory slot in
run_trsqp that accepts exactly one more NonlinearConstraint with zero driver surgery
(`:1179-1182`). A surrogate row KS(1 - ratio_lanes) ≥ delta_cert (delta derived from the measured
worst-vs-radius correlation along recorded walks — the rejected_designs artifacts persist exactly
this data, `:904-911`) would let the SQP price the frontier and either close the KKT against it
(outcome-I with a certification multiplier — a NEW measurable object: the shadow price of
certifiability, exactly the language the H-CLASS qualification of S24 needs) or demonstrate
measured infeasibility. THE GATE STAYS: P4/P3(ii) remain absolute adjudicators; the surrogate is
steering, never certification — same contract as the G1 margin surrogate
(`margin_governor.py:41-50`), which is the repo's OWN precedent for "smooth surrogate inside,
hard rejector outside".

**SOTA**: hidden/unrelaxable-constraint taxonomy (Le Digabel–Wild, "A taxonomy of constraints in
black-box simulation-based optimization", Optim. Eng. 2023 — cert(W) is currently treated as a
hidden constraint, the taxonomy's worst class, when it is quantifiable-relaxable-a-posteriori,
the best tractable class); filter line-search SQP (Wächter–Biegler 2006) for eval-failure
handling; the surrogate-inside/gate-outside pattern is the repo's own [X-MGOV] G1 lineage.

**Extremal cases**: (E1) deep-DEF S24 — MEASURED (two decisive runs spent fencing; KKT open at
1.4e6; the F4 operative verdict itself); (E2) S20 frontier crawl — certdiag 8/8 GENUINE
non-convergence (not trip-cap), i.e. the frontier is real physics/geometry and the surrogate's
gradient carries actual design information there; (E3-everyday) mild eps = 4 S18: frontier never
approached, surrogate row inactive, KKT closes at 7.7e-2 exactly as of record — zero cost, zero
semantic change.

**Probe**: R2 REGISTERED (S25 engine session): pilot at eps = 4, NI = 21, Nw = 60 — build
cert_diag KS row, one short constrained walk, compare segment count vs the S18 record. Not
runnable now (marches; campaign running).

---

## G8 — Margin NonlinearConstraint ships exact jac but NO hess: scipy silently BFGS-estimates the constraint curvature (~rho/4 · |∇val|² when active) that the policy elsewhere insists on MEASURING

**Anchors**: `a1_toc_variational_jax.py:1181-1182` (`NonlinearConstraint(m_np, 0.0, np.inf,
jac=gm_np)` — no `hess=`, scipy default = BFGS()); contrast with the objective's measured exact
Hessian, R-3 activation block `:1074-1097` ("MEASURED FULL HESSIAN ... POLICY-CONFORMANT");
fresh-BFGS-per-segment policy `:861-862`; factories `margin_governor.py:206-233`,
`def_twin_falsifier.py:654-681`.

**Classification**: NOT-SOTA / INCOMPLETE (second-order treatment inconsistent across the
Lagrangian).

**The gap.** The S18 R-3 finding of record was precisely that BFGS-quality curvature stalls this
driver (KKT plateau → measured exact H, Newton-quality steps). That repair was applied to the
objective HALF of the Lagrangian only. When the margin is active, the Lagrangian Hessian gains
mu·∇²m, whose scale is rho·w(1-w)·|∇val|² + KS-weighted ∇²val — with rho/4 = 1.44e4 (P1) this
term can dominate the measured H, and it is re-learned from scratch by a fresh BFGS every
segment (policy-bound), i.e. the exact S18 plateau mechanism re-created on the constraint side.
JAX gives the exact margin HVP for free (forward-over-reverse `jax.jvp(jax.grad(margin_W))`), and
scipy's NonlinearConstraint accepts a hess callable; alternatively the same forward-difference-of-
exact-gradient recipe already used for H (`:1088-1094`) applies verbatim to ∇m. Zero policy
change: measured-per-segment-base, frozen within the segment — the R-3 pattern extended to the
whole Lagrangian.

**SOTA**: exact Lagrangian Hessian in SQP (Nocedal–Wright §18-19); second-order adjoints / HVP
via forward-over-reverse AD (standard JAX practice; Griewank–Walther, Evaluating Derivatives);
scipy trust-constr constraint-hess interface.

**Extremal cases**: (E1) margin-active rung at rho = 5.75e4: constraint curvature ~1e4x the
objective's measured diag |H| band — BFGS starts at identity each segment, TR collapses on model
misprediction exactly as pre-R-3; (E2) argmin-lane swap mid-segment (G1-E2): true constraint
curvature jumps discontinuously, the stale BFGS estimate is not even wrong-sign-safe; (E3-everyday)
margin inactive (S24 measured): term absent, gap invisible — again only frontier instances pay.

**Probe**: folded into R2 (the S25 pilot arms hess= alongside the surrogate row; measuring
segments-to-close with/without is one flag).

---

## Dropped (5, declared)

1. `jnp.maximum(jnp.sum(e), 1e-300)` log-floor (`margin_governor.py:198`): undeclared constant,
   but unreachable when n_fin > 0 (min lane contributes exp(0) = 1) and the n_fin = 0 branch is
   discarded by the where; both branches finite → no NaN leak. Cosmetic, not a finding.
2. frac_bad penalty scale K_RICH·m_ref coupling across instances (m_ref 0.68 vs 4.2e-3): the C4
   lane-count-drop declaration already names it an adjudication item; no independent defect.
3. Monotonicity-stop derivation (activity monotone in mu0): checked — correct for a lower-bound
   ladder; no gap.
4. LinearConstraint row scaling A·Dv under the Jacobi change of coordinates: checked against the
   S24-T1 source-read — multiplier scale-invariant as declared; no gap.
5. G1 surrogate continuity at frac_bad = 0 (claimed "exact KS recovered bit-for-bit"): verified
   by inspection of the where-structure; holds.

## Probe declaration (cost ledger)

- P1 (KS conditioning), P2 (complementarity), P3 (spline affinity): ONE script,
  `scratchpad/probe_constraints.py`, pure numpy, total < 5 s CPU. RUN. No jax import, no march,
  no interaction with the running S24 campaign.
- R1/R1' (mask drift per segment + lost-lane count on recorded run), R2 (cert-surrogate + hess
  pilot at eps = 4, NI = 21, Nw = 60), R2' (LSQ multiplier re-estimate on recorded gradients),
  R3 (argmin-swap census on the recorded walk): REGISTERED, named for the S25 engine session —
  each needs marches or replay machinery, none fits the 30 s cap.
