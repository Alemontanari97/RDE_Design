# ADVISORY — DEEP MATHEMATICAL SENSE OF THE ALGORITHMIC PIPELINE
## Cycle-averaged variational RDE nozzle program: global coherence + per-stage structure

Date: 2026-08-12. Plan tag: [S25/PREP] (F1b closed, F2 not yet opened;
standing user directive `pipeline-sense-expert-review`, first instance).

**LABEL OF RECORD: single-expert review, one pass — not a converged
panel.** No code executed (read-only). Findings marked [NEW] are this
review's; findings that coincide with the registered SOTA/rigor map are
CITED as GAP-n / choice-ledger row Cnn of
`validation/ADVISORY_S24_sota_gapmap_2026-08-12.md` and are NOT
re-minted (dedup duty honored).

Sources read in full or in the load-bearing parts: M0
(`docs/rde_nozzle_MASTER.md`, Parts I–VII incl. the A1 bricks and the
S20/S21/S22/S23/S24 registration blocks); `validation/a1_ideal_march_jax.py`;
`validation/thermotab_c1_jax.py`; `validation/a1_toc_variational_jax.py`
(wall class, objective, jitted replay, RK-G TR-SQP driver);
`validation/margin_governor.py`; `validation/def_twin_falsifier.py`
(DE-bucket machinery); the S24 gap map (all 36 rows + quarantine +
45-row choice ledger); D6 phase spine F0–F6.

---

## §1 GLOBAL COHERENCE VERDICT

### §1.1 The composed object, stated as mathematics

The executed pipeline computes, per instance:

    data:      Sauer transonic IVL at one frozen (P0, T0) +
               frozen thermally-perfect tabulated isentrope closure
               q -> (T, p, rho, c, gamma) on a single (s, h0) leaf;
    state map: W = (theta_B, y_1..y_m)  |->  U(W) = the axisymmetric
               irrotational-homentropic MoC field, marched x-as-time,
               every cell an implicit midpoint unit process solved by
               damped Newton and CERTIFIED (one-extra-step metric at
               the roundoff floor) with the per-cell causality
               rejector u_x - c > floor;
    objective: J(W) = 2*pi * trapz( p*y dy ) over the design wall
               (vacuum-equivalent at fixed (eps, L): the Pa term is
               constant on the feasible set);
    gradient:  reverse AD of the FROZEN-PLAN replay (custom_vjp
               implicit-function rule per cell) = the Lemma-B discrete
               adjoint of the branch;
    search:    TR-SQP (scipy trust-constr) on strata of constant plan
               under RK-G (record adaptive / replay differentiable),
               eps as linear equality, optionally the margin
               constraint  KS_rho(val on the DE-side bucket) >= mu_0;
    terminal:  outcome-I (KKT closed at derived gtol) or outcome-II
               (certifiability-limited, KKT reported OPEN), wrapped in
               the Verdict format (derived bands, K_RICH = 4
               two-resolution Richardson, oracles, negative controls).

The theory of record legitimizes the single-phase instance as the
cycle-averaged problem's corner: T0 (exact steadification) -> T3 /
T-T3-SI (collapse on the tier-1 corner) -> the S24 five-line hypothesis
audit (H-OBJ, H1-T, H2', H3-p degenerate, H4 instance).

### §1.2 What composes correctly (verified line-by-line this pass)

These are positive findings, stated because a sense review must also
certify what is right:

1. **Two-tier error architecture is clean.** Per-cell certification
   bounds the ALGEBRAIC error at the roundoff floor (z-space metric —
   correct choice, the residual rows mix units); the two-resolution
   Richardson band then measures the TRUNCATION error alone. The
   separation is real: no band ever absorbs an unsolved cell, and an
   unsolved cell can never masquerade as discretization error. This is
   the correct factorization of the discrete error and most codes do
   not have it.

2. **The adjoint is verified at both levels that matter.** O3.1
   (transpose identity over the whole march, FD tolerance derived by
   two-step Richardson + roundoff floor) checks that reverse AD is THE
   discrete adjoint of the discrete march; the O3.3 bench (f2 =
   -lambda2 constant on the CORRECT classical locus, corner identity,
   compatibility relation saturating at exactly 1.0 with the wrong
   sign per family as rejector) checks that the discrete adjoint
   carries Rao's optimality structure. Only the pair makes
   "transversality reached via the gradient" a meaningful claim; the
   pair exists.

3. **The objective identity is exact.** 2*pi*Int p y dy is the exact
   axial pressure force on a surface of revolution, and the Pa-drop at
   fixed (eps, L) is theorem-level on the feasible set (both endpoint
   areas fixed), so the vacuum-equivalent objective is a
   simplification, not an approximation. (One small omission at the
   arc start — §2.4 [NEW], LOW.)

4. **The margin object is a faithful classical translation.** The
   chain (G)/Lambda-form == Rao-Beck Eq. (4) is S4 THEOREM (hand proof
   + independent re-derivation + machine identity at the roundoff
   floor); the S24 construction-surface correction (val is a criterion
   of the CONSTRUCTION SURFACE, not a field-validity criterion; DE-side
   bucket strictly lipward of the last val = 0 crossing = the direct
   D'-analog) matches the page-verified classical placement of the
   discontinuity AT D' (dispatch A5), and the mild-instance degeneration
   to the whole-field bucket reconciles the S22 record at its own
   instance. The S22 -> S24 sequence (wrong bucket -> measured
   empty-feasible-set discovery -> corrected bucket, panel-ratified) is
   the audit machinery working as designed, and should be counted as
   evidence FOR the program's method, not against it.

5. **The steady proxy is used only where it is a theorem.** No executed
   result leans on the O(St) step outside its priced scope; the S24
   audit says exactly which hypotheses are degenerate (H3-p) and keeps
   the +0.04% twin agreement capped as a corner measurement. The
   quasi-steady risk is fully in the future (F5), not in the record.

### §1.3 The seams — ranked structural risks

**R1 — The binding feasible set is solver-defined and has no continuum
object behind it** [sense layer NEW; discrete side = GAP-1, GAP-2;
measured base: S20/S22/S24 outcome-II, bridge K_disc ~ A_0 FALSIFIED,
H-CLASS added to EQ-v2]. At frontier instances the pipeline maximizes
J over K = {W : the adaptive record passes every gate} — a set defined
by the algorithm's own convergence behavior. The program's honest
formalization (tier ladder, margin-multiplier KKT) intended K to proxy
the physical set A_0; the measurement says it does not (certification
degrades at val 0.61–0.86, nowhere near 0; three instances). The
consequence, stated as mathematics: **outcome-II points are certified
VALUE data on a set with no known continuum limit; no theorem — and
currently no conjecture with a falsifier — connects them to any (P_t)
as h -> 0**, because H-CLASS fails measurably at tier-0 (S24: margin
never activates, 33x floor at the stop). Coherent-by-honesty (the
wording of record never overclaims), incomplete-as-formulation (GAP-1's
in-KKT surrogate and the C7 refine/enriched-class conditional are the
two named exits; §3 Q1 is the program-level restatement).

**R2 — The globality half of the contract is dormant at the engine
rung** [NEW; no GAP row covers it — grep-verified: no
J_ideal/bound-ladder reference exists in any `validation/*.py`]. The
problem of record (D2.6) is the PAIR (S*, delta), delta = B - J[S*]
against the bound ladder; Part IV declares this the maximal truthful
form precisely because it absorbs partial results. The pair is
exercised end-to-end ONLY at rung 1 (`src/thrust`: OP-0 capped
ceilings, OP-11-eps diagram, premium bound). The 2-D engine instances
(S18, S20, S24 — the program's most expensive certified numbers) ship
KKT residuals, bands and oracles but NO delta row: nothing evaluates a
per-instance upper bound at the marched instance. An executable
composition exists cheaply: at fixed (eps, L), vacuum objective, the
brick-1 IDEAL march at the same eps and thermo is a certified
exit-area-capped ceiling for the truncated problem (truncation only
loses; the classical dF/dA argument on the supersonic branch), i.e.
outcome-II could ship as (value, delta) TODAY with existing bricks.
Until then, "search for the global optimum" is numerically
substantiated only at rung 1, and the engine-rung Verdicts are
locally-certified numbers with no distance-to-global field.

**R3 — Theory-to-code asymmetry on the measure** [NEW as a ranked
risk; the plan knows the sequencing, F5]. The operating measure mu —
the program's defining object — enters executed code only at rung 1.
The genuinely averaged optimality structure (T7(b) mu-averaged wall
condition, the weighted transversality (**'), VI.4 switch-splits,
VI.4bis quadrature) has NO executable carrier; every certified 2-D
result is a single-phase instance licensed by the collapse corner.
This is planned, but the structural risk is COMPOSITIONAL and is
nowhere named: the certified feasible set of the averaged problem is
an intersection over supp(mu) of per-phase certifiable sets K(xi),
each with its own plan topology, its own frontier, its own D'-analog
bucket; the frontier phenomenology that produced three outcome-II
records at a SINGLE phase will be multiplied by the phase family, and
none of the margin/bucket machinery is xi-indexed. §3 Q3 states the
three sub-questions that should be answerable before F5 opens.

**R4 — One model-class mismatch, twelve symptoms** [symptoms = GAP-4,
13, 14, 15, 16, 17, 19, 27, 31, 33 + C31-C38; the unification is this
review's reading]. The driver machinery assumes a C^2 NLP per stratum
(trust-constr, BFGS-estimated constraint curvature, smooth aggregate);
the measured problem is piecewise-smooth (plan seams), with a hard-min
constraint at derived rho ~ 5.7e4 (one-hot gradient), a
solver-bounded feasible set, and optima that pin on seams or on the
frontier. Every driver-side gap row is a symptom of this ONE mismatch.
Consequence for repair order: the coherent fix is the problem-class
upgrade (GAP-1 in-KKT certification surrogate + GAP-2 B-stationarity
certificate, together), after which most of the incremental hardening
rows become either moot or cheap; hardening first would spend sessions
on symptoms.

**R5 — Derived-at-the-leaf, convention-at-the-composition** [= GAP-7,
9, 10 + C41-C43; K_RICH role reuse C42; stated here as the sense
boundary]. Every leaf tolerance this review checked is genuinely
derived (constants budgets, Newton floors, Hermite remainders,
contraction counts, FD Richardson). The COMPOSITION of bands (sum vs
max, topology-conditioning, the asymptotic-range hypothesis at band
sites that the o32 campaign honestly could NOT verify under moving
march topology) is convention. The honest statement — already mostly
the wording of record — is that a two-resolution band at a band site
is an ESTIMATE with an unverifiable hypothesis, not a certificate;
the discipline to keep is that no Verdict promotes it.

### §1.4 Global verdict

The composed pipeline is a **coherent certified-evaluation protocol
and falsification instrument** — the strongest of its kind this
reviewer knows of in the nozzle-design literature — whose composition
is currently **weaker than its own mathematics allows** at four named
seams: no continuum object behind the binding feasible set (R1), no
globality field in the engine-rung Verdicts (R2), no executable
carrier for the averaged structure that makes the program novel (R3),
and a driver model class one rung below the measured problem class
(R4). None of the seams is hidden by the record; R2 is the cheapest to
close and R1 is the deepest.

---

## §2 PER-STAGE VERDICTS

### §2.1 Sauer IVL start line + axisymmetric MoC march + per-cell certification — **SOUND-WITH-CAVEAT**

The mathematical structure is right for the role:

- The (u,v) two-equation compatibility system with the q -> state
  closure on a single isentrope is EXACTLY the
  irrotational-homentropic subclass of S1 — the same subclass in which
  T7(a)'s closed forms live. The scope is consistent end-to-end:
  the engine, the f2 oracle layer, and the (G) monitor all live on the
  same manifold, and the stratified extension is owned (F2) with the
  data guard REJECTING out-of-class data loudly (verified in the TOC
  main). No silent scope leak found.
- The midpoint-implicit unit process is the fixed point of GENO's
  predictor-corrector, solved to roundoff: the discrete system is
  well-defined independently of iteration count — the precondition for
  the implicit-function adjoint rule to be exact at the solution.
- The per-cell axial-margin rejector u_x - c > floor is the correct
  DISCRETE surrogate of the T-NSW spacelikeness theorem (axial
  interface spacelike iff u_x > c, frame-invariant): causality is
  checked per cell, never assumed. The S17 finding it encodes (Newton
  can certify a causally wrong cell) is exactly the failure mode a
  pure algebraic certificate cannot see; the pipeline sees it.

Caveats (all registered): conditioning/branch qualification of the
certificate absent — false-fail and false-pass both reachable near
folds (GAP-3 HIGH; C20); the shared Sauer IVL has no accuracy rejector
and the cross-code band is structurally blind to it (GAP-6; C12); the
axis process is verification-free at march level while being the exit
read point (GAP-8; C13/C14).

[NEW, sense note, LOW]: the IVL error is a COMMON data perturbation
(the kernel is W-independent), so the march solves exactly a
nearby-data problem; by the envelope argument the ARGMAX inherits the
IVL bias only at second order while absolute J inherits it at first
order. Current practice only ever quotes J design-to-design or
code-to-code (where the bias cancels) — this discipline should be
stated once in M0 VI so it cannot erode when absolute Isp numbers
start shipping (F5/P-3).

### §2.2 Frozen thermally-perfect tabulated thermo, quintic-Hermite C1 closure — **SOUND**

The strongest stage of the pipeline, and an instance of theory-driven
code: the C^1-in-coefficients requirement comes from the C-D25U
uniform-estimate machinery and the implicit-function differentiation
of cells (state Jacobians must not jump at table knots); the closure
exists BECAUSE the variational layer needs it, and it is exactly what
it claims:

- `derived_newton_trips` is a correct scalar Kantorovich-style bound:
  seed error via T''(h) = -cp'/cp^3 with h-spacing cp*dT; contraction
  constant M = max|cp'| / (2 min cp) — the standard quadratic-
  convergence constant for a monotone scalar Newton; the trip count is
  derived per table, refusing loudly when contraction cannot be
  certified. Verified algebraically this pass.
- The C-A oracle argument is correct and of the strongest kind
  (identity, not band): in the joint-free window NASA cp is quartic,
  hence h exactly quintic, hence the quintic-Hermite closure with a
  4th-order cp' estimator reproduces the FIT itself at the roundoff
  floor. An exactness oracle beats any convergence test.
- The grid-uniformity rejector licensing the O(1) floor index, and the
  monotonicity/G > 0 audits with Lipschitz-from-data margins, are
  correctly scoped as grid audits (declared, not interval
  certificates).

Caveats: the table-box coverage hypothesis ("contains every
march-realized state") is enforced nowhere per run (GAP-11; C25/C26);
the closure hard-codes the homentropic-homoenergetic manifold — right
for the declared class, and the F2 (q; s, h0) extension will have to
rebuild the p-closure, not merely extend it (the entropy-form
p = PREF exp((s0(T)-s0)/Rg) is leaf-bound by construction).

### §2.3 Design class: clamped/natural cubic spline wall, heights + theta_B — **SOUND-WITH-CAVEAT — and the measured binding element of the whole pipeline**

The chart itself is coherent: heights at frozen abscissae + attachment
angle is a well-posed finite-dimensional chart of the C^{1,1} sector
class; C^1 attachment is enforced exactly through the clamped slope
tan(theta_B); eps enters as a LINEAR equality (lip node); L by
construction. The knots-not-dofs decision is adjudicated (S20 survey).

Caveats, all registered and all HIGH-leverage: the natural right BC
biases curvature at the LIP — the exact node where the open [C-O33]
goal quantity dJ/dy_lip is differentiated (GAP-5 HIGH; C2); the
oscillation axis of the interpolation basis is unadjudicated (GAP-21;
C1, quarantine Q2); knot abscissae silently migrate with theta_B
(GAP-34; C5).

Sense reading [the fact is of record; the emphasis is this review's]:
three independent instances (S20 mild, S22 mild, S24 deep-DEF) show
the CLASS — not the physics, not the certification tolerance — is the
active boundary of the search; the program has correctly promoted this
to a named hypothesis (H-CLASS) inside EQ-v2. That makes the design
class the single highest-leverage object in the program: the C7
refine/enriched-class conditional and the GAP-5/GAP-21 adjudications
are not hygiene, they are the difference between "the falsifier's
decisive content is reachable" and not (§3 Q1).

### §2.4 Objective + whole-loop adjoint — **SOUND**

- The objective is the exact axial-projection identity discretized at
  the march's own order; Pa-drop valid on the feasible set (§1.2.3).
- The frozen-plan replay + custom_vjp implicit rule per cell means the
  gradient is the EXACT gradient of the branch J_plan — the correct
  object for stratified optimization under RK-G; plan flips end
  segments, accepted iterates re-record, replay fidelity is checked at
  the base at the Newton floor. The stop_gradient on recorded seeds is
  correct (seeds select the root, they do not parametrize it — the
  implicit rule differentiates the ROOT).
- The safe-where padding of masked lanes solves a FIXED recorded dummy
  problem with no gradient path to W, and the dummy is
  certification-verified at build time — the NaN-leak channel through
  where-branches is closed and O3.1 doubles as its detector. Correct
  construction (the standard where-of-where trap is avoided).

Caveats: prefix-exactness of `_chain_ratios` unstated as a lemma
(GAP-30); the adjoint's convergence EXPONENT is not measurable under
moving march topology — the honest LB-c2 residue, which caps what any
band at a band site can claim (GAP-9; C43).

[NEW, LOW] The wall integral starts at the FIRST arc station theta_1 =
theta_B/n_B, omitting the fixed-arc sliver [0, theta_1) whose upper
endpoint MOVES with the design variable (d theta_1/d theta_B = 1/n_B
within a segment, plus a ceil-seam when n_B flips across records).
Since p on the arc is W-independent, the omission is a deterministic
tilt in dJ/d theta_B of order p_t * 2*pi * y_t * rtd * sin(theta_1)/n_B
— order-of-magnitude 1e-4 relative to J at the twin instance, below
every current discrimination band (and invisible to the contour oracle
by construction), but it is a BIAS, not noise, and it is not covered by
any GAP row. One-line closure: extend the trapezoid to theta = 0 with
the throat point (y = yt), making the omitted area W-independent
exactly; or declare the coded J as the object of record and note the
argmax tilt bound. Either is fine; silence is the only wrong option.

### §2.5 Driver (segmented TR-SQP under RK-G) + margin constraint — **SOUND-WITH-CAVEAT; structurally weak exactly at frontier instances, by the program's own record**

What is structurally right:

- RK-G record/replay is the mathematically correct resolution of
  adaptivity-vs-differentiability: optimize a smooth branch, re-record
  on acceptance, detect flips, never differentiate a decision. The
  reject-and-shrink with ratcheted cap is standard TR semantics
  (Conn-Gould-Toint) correctly extended to record gates, and the S20
  livelock fix (the cap must RATCHET) is the right repair.
- The margin governor derivations are clean: KS-min bounds are
  standard log-sum-exp THEOREM; rho is derived to pin the
  conservativeness gap below the enforcement resolution, on the
  CONSERVATIVE side (KS <= min, so KS >= mu_0 implies min >= mu_0 —
  the inequality direction that a certificate needs); the floor ladder
  is pre-registered; the G1 surrogate is finite-negative everywhere
  with counted zeroing (REQ-NONSTALL as declared, with rejectors that
  fire).
- The DE-side bucket is the faithful classical object (§1.2.4), and
  the C3 mask self-consistency gate + drift folding (panel conditions)
  give it instance-level integrity.

Caveats — the twelve symptoms of R4, cited not re-minted: TR_FLOOR
underived on a verdict exit (GAP-4; C34); outcome-II stationarity
declaration (GAP-2; C38); IP path never source-adjudicated, cold
barrier restarts per segment (GAP-15; C31); missing constraint Hessian
silently BFGS-estimated, recreating the S18 plateau mechanism on the
constraint side (GAP-19; C33); measured objective Hessian without
rejector or band (GAP-16; C32); Dv measured once, objective-only
(GAP-17; C36); hard-min aggregate at derived rho with one-hot gradient
(GAP-27; C27); rung-frozen mask granularity and crop bounds (GAP-13,
GAP-14; C29/C30); flip-event undercount (GAP-31); multiplier
provenance res.v raw (GAP-12; C39).

[NEW, minor] The G1 surrogate margin is DISCONTINUOUS in W across
lane-failure boundaries (frac_bad jumps by 1/n_sel when a lane crosses
finite/nonfinite): continuity is declared, correctly, only at
frac_bad = 0. Inside trust-constr this is a modeled cliff the TR
machinery tolerates but nothing prices; it lives on the same
problem-class axis as GAP-1/GAP-2 and is subsumed by their repair —
worth one clause in the surrogate's declaration so the C^2 assumption
violation is explicit.

Sense verdict for the mandate's question "is
certification-as-outside-gate vs the variational formulation a
coherent object?": as a PROTOCOL, yes — surrogate-inside/gate-outside
(the [X-MGOV] precedent) keeps adjudication absolute while steering is
smooth. As a VARIATIONAL PROBLEM, not yet: the binding constraint has
no in-KKT representation (GAP-1), so at frontier instances first-order
theory is structurally silent — which is R1, the program's deepest
seam, and is exactly what the three outcome-II records measure.

### §2.6 Verdict layer (derived tolerances, Richardson bands, frontier semantics) — **SOUND-WITH-CAVEAT**

- The rejector culture (negative controls that MUST fail, corrupted
  route/gradient/table/inverse controls sized to their own detection
  floor — the R6 epsD derivation in [X-THC1] and the S24 R-GRAD
  re-scaling are model examples) is real, pervasive, and is the
  pipeline's strongest rigor asset. A reviewer can trust a PASS here
  more than in any comparable tool known to this reviewer.
- Outcome-II ("certifiability-limited, KKT reported OPEN") is a
  mathematically meaningful terminal object AS A VALUE CERTIFICATE
  plus an honest refusal — and NOT as a stationarity statement: the
  reported optimality residual is the residual of the problem WITHOUT
  the binding constraint (GAP-2), and the exit resolution is an
  underived floor in instance-dependent scaled units (GAP-4). The
  wording of record already respects this boundary; the missing piece
  is the certificate that would upgrade it (GAP-2's convex-hull /
  B-stationarity test).
- [NEW — the R2 composition] The Verdict format has no globality
  field at engine-rung instances. D2.6(iv) declares delta; rung-1 code
  computes delta-type gaps; the 2-D Verdicts never do. The
  (value, delta) composition is executable with existing bricks
  (ideal-march ceiling at the same (eps, thermo) as the fixed-(eps,L)
  upper bound) and would give outcome-II points the global meaning
  they currently lack.
- Band-composition conventions and K_RICH role reuse: GAP-10, C41,
  C42; asymptotic-range honesty at band sites: GAP-9, C43 (the o32
  NON-CONCLUSIVE verdict is the honest ceiling here and its
  non-propagation to band consumers is the registered residue).

---

## §3 THE THREE DEEPEST QUESTIONS THE PROGRAM SHOULD BE ABLE TO ANSWER AND CURRENTLY CANNOT

**Q1 — Of which continuum problem is an outcome-II point an
approximate solution?** Sharp form: exhibit a sequence (h_k, class_k,
mu_0k) and certified designs W_k such that W_k converges to a KKT
point of (P_t) for SOME tier t — or prove no such sequence exists in
the current class family. Today: the bridge conjecture K_disc ~ A_0 is
falsified by its own named test; H-CLASS fails measurably at tier-0
(the mu_0 -> 0 limit set of margin-active KKT points is EMPTY along
the executed ladder); the two candidate exits are named (C7
refine/enriched class; GAP-1's in-KKT certification surrogate) but
neither has yet produced a boundary-reaching sequence. Until Q1 has an
answer, every frontier result is a lower bound plus falsification
data, EQ-v2 Direction A is untestable (S24 says this), and the
tier-ladder's "measured mu prices shock-freeness" clause has no
measurable mu. This is R1 restated as the question the program's
mathematics must eventually answer.

**Q2 — What is delta for the S18 / S24 optima?** The problem of
record is (S*, delta), yet the program's most expensive certified
numbers ship with no distance-to-global field (R2). The executable
path exists with committed bricks: at fixed (eps, L), vacuum
objective, the brick-1 ideal march at the same eps and thermo is a
certified upper bound (truncation only loses on the supersonic
branch); T-GB with the sonic cap gives the geometry-free roof at
instance data. One carrier would turn outcome-II into (value, delta)
Verdicts and make the globality contract live at the engine rung.
Until it exists, the program cannot answer "how far from optimal is
the design you certified?" precisely where it spends its compute.

**Q3 — Does the certified apparatus commute with the cycle
integral?** Three sub-questions, none currently answerable, all
cheaper to name now than to discover at F5 with S20-style surprise:
(a) is the averaged problem's feasible set — the intersection over
supp(mu) of per-phase certifiable sets K(xi) — nonempty and stable
under the optimizer's motion, and is its boundary the mu-essential
supremum of the per-phase frontiers (so that ONE phase's frontier
pins the whole averaged walk)? (b) do the per-phase margin buckets
(the D'-analog moves with xi) compose into a jointly measurable
margin field admitting a KS-type aggregate in (lane, xi) with the
same conservative-side theorem, and what replaces the rung-frozen
mask when the crossing index is xi-dependent? (c) does the weighted
transversality (**') survive branch gradients when the plan topology
is xi-dependent — i.e., is the mu-integral of per-phase branch
gradients the branch gradient of the mu-integral, and at which seam
structure does that fail? The F5a T3-CONTROL protocol governs the
physics-side comparisons but not this composition mathematics; R3 is
the risk statement, Q3 is its test form.

---

*Single-expert review, one pass — not a converged panel. Findings
[NEW] herein are candidates for the standing registries only after
their own adversarial pass; every coincidence with the S24 gap map is
cited above in place of re-minting (dedup duty).*
