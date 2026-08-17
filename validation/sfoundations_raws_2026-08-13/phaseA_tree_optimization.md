# ATTACK TREE — Numerical Optimization / Computational Design lens

Deliverable per §7 of `phaseA_problem_brief.md`. Independent derivation:
no project document consulted other than the frozen brief. Open-literature
citations given by author-year; all are standard, checkable references.

Author lens: nonlinear programming, PDE-constrained and shape/topology
optimization, derivative computation and verification, semi-infinite and
nonsmooth programming, surrogate/derivative-free/global methods,
error control and tolerance derivation, global-optimality certificates.

---

## 0. Reading of the problem in optimization-theoretic terms

The problem is, structurally, the composition of SIX hard sub-structures.
Naming them first fixes the vocabulary of every fork below.

1. **PDE-constrained shape-AND-topology optimization**: design variable is a
   compact solid set S in a cone-condition class; topology sectors (bell,
   plug, E-D, shrouded plug) are *outputs*. So the design space is not a
   single Banach manifold of contours; it is a union of strata of different
   topology, plus the representation must either span the union or the
   search must enumerate strata.
2. **Averaged (ensemble) objective**: J[S] = ∫_Ξ F[S; s(ξ)] dμ — a
   many-phase average of per-phase steady Euler functionals sharing ONE
   design. This is the "common design, many operating points" structure of
   multipoint aerodynamic optimization (Drela 1998; Kenway–Martins 2016) and
   simultaneously a sample-average / stochastic-programming structure
   (Shapiro–Dentcheva–Ruszczyński 2009).
3. **Semi-infinite state constraint**: g_sep(S; s(ξ)) ≤ 0 for μ-a.e. ξ —
   an infinite (or many-) constraint family indexed by phase: semi-infinite
   programming (SIP; Hettich–Kortanek 1993) or its discretized/aggregated
   surrogates.
4. **Nonsmooth / potentially discontinuous objective map**: per-phase Euler
   solutions contain shocks; topology changes and constraint-activity
   changes create kinks; the certification boundary (designs whose state
   cannot be certified) creates a *hidden-constraint* region where J is
   simply not returned (Le Digabel–Wild 2024 taxonomy).
5. **Certificate stack**: the deliverable is not argmax alone but
   (existence, KKT, second-order, globality gap δ computed, error bars).
   That stack is itself an optimization-verification pipeline and drives
   choices that a pure "find a good design" run would not need (e.g. dual
   consistency, Hessian-vector machinery, upper-bound mechanisms).
6. **Objective-ladder error control**: J is a surrogate of J_exact; the
   bracket |J_exact − J| must be carried as a named, evaluable term — a
   multifidelity / model-error-control structure (Peherstorfer–Willcox–
   Gunzburger 2018), not an afterthought.

Decision-theoretic consequence used throughout: **every fork is decided by
(a) what the certificate stack (i)–(v) demands, then (b) cost, then (c)
convenience.** A method that finds better designs but cannot feed the
certificates is dominated at this problem.

---

## 1. FORMULATION FAMILIES

Four viable overall formulations (each internally consistent end-to-end);
the forks then select within and across them.

**FAMILY A — Certified reduced-space nonlinear program (recommended
backbone).** Represent the wetted contour(s) in a smooth, hierarchical
function class inside each topology sector; per-phase steady Euler solved
by a solver whose solution class is certified (fitted discontinuities
where present); discrete-adjoint (or dual-consistent) gradients; SQP/TR
Newton reduced-space optimizer; semi-infinite separation constraint via
exchange + aggregation; DWR error bars; globality via physical upper
bound B + sector-wise multistart evidence; unsteady bracket via a
harmonic-balance rung of the ladder. This is the only family that natively
serves all of (i)–(v).

**FAMILY B — One-shot / full-space (SAND) KKT solve.** State, adjoint and
design updated simultaneously (Ta'asan 1991; Biros–Ghattas 2005;
Hazra–Schulz 2004). Best cost-per-optimum when a single tightly coupled
solver exists; strained here by (a) many phases sharing one design (block
structure of size #phases), (b) the certification requirement that each
per-phase state be individually certified (partial-convergence states are
uncertifiable), (c) hidden constraints. Kept as an accelerator inside
Family A (§FORK-15), not as the backbone.

**FAMILY C — Relaxed topology formulation.** Level-set / topological-
derivative or density relaxation over E so that sectors emerge without
enumeration (Allaire–Jouve–Toader 2004; Sokolowski–Żochowski 1999;
Borrvall–Petersson 2003 for fluids). Genuine best: no sector prior, and
the relaxation can furnish RELAXATION UPPER BOUNDS for δ (the relaxed
optimum bounds the unrelaxed sup if the relaxation is proven to be one).
Weaknesses: Euler flow through gray/immersed geometry is hard to certify;
slip-wall accuracy on non-fitted boundaries degrades exactly the
quantities (wall pressure → thrust, separation margin) we must certify.
Kept as (1) the δ-bound auxiliary and (2) the sector-discovery scout.

**FAMILY D — Surrogate/global outer loop.** BO/CMA-ES/GA over a modest
parametrization with the PDE as a black box, optionally multifidelity
(EGO: Jones–Schonlau–Welch 1998; MFEGO; CMA-ES: Hansen–Ostermeier 2001).
Genuine best: robust to nonsmoothness, hidden constraints, multimodality;
gives global *evidence* and priors. Cannot by itself deliver (ii)/(iii)
(no stationarity residual to machine-verify) nor tight δ (GP bounds are
model-trust statements, not certificates unless a Lipschitz constant is
PROVEN, which no one can prove for this map). Kept as the exploration
layer feeding Family A starts.

**Selection criterion across families**: (i)–(v) are hard requirements ⇒
the backbone must produce a discrete KKT residual, a reduced-Hessian
test, a computed δ, and error bars with named carriers. Only A does all
four natively; B, C, D are subordinated as accelerator, bound-provider,
and explorer respectively. Falsifier of the family choice: if the
per-phase Euler map proves so nonsmooth in the design (e.g. certified
class boundary is dense in the useful region) that gradient-based
convergence fails on honest tests, the backbone flips to D with A demoted
to local polishing — this is testable early (FORK-9/21 verification
gates).

---

## 2. FORKS

Schema: FORK-k: question → options at their best → decision criterion →
recommendation + grounds → falsifier.

### Group A — Objective ladder and the phase average

---

**FORK-1 — Relation of J_exact to the computable objective (the
idealization ladder).**

*Question.* What computable object is optimized, and how is
|J_exact − J| carried (requirement (v)) at a MARGINAL Strouhal number St
(neither ≪1 nor ≫1, value a measured parameter)?

*Options (full space).*
1. **Quasi-steady cycle average J** (the brief's surrogate): per-phase
   steady solves, μ-average. Exact in the St→0 limit; error term is
   O(St)–O(St²) depending on the structure of the leading unsteady
   correction, with unknown constant at marginal St.
2. **Harmonic balance / time-spectral (HB/TS)** intermediate rung
   (Hall–Thomas–Clark 2002; Gopinath–Jameson 2005): solve the periodic
   unsteady problem with K temporal harmonics; K=0 recovers option 1;
   convergence in K measures the unsteady correction directly. Adjoints
   exist for HB (Mader–Martins 2012; Huang–Ekici 2014).
3. **Full unsteady URANS/UE (unsteady Euler) time marching** with
   long-time averaging: the reference; cost ≫ (windowed averages, LCO of
   the mean, and — for optimization — unsteady adjoints with backward-
   in-time storage or checkpointing (Griewank–Walther revolve 2000);
   chaotic-sensitivity risk is LOW here (periodically forced, not
   chaotic, under H-DATA), so LSS/shadowing (Wang–Hu–Blonigan 2014) is a
   contingency, not a need.
4. **Optimize a corrected surrogate** J + C(St): asymptotic correction in
   St derived analytically (unsteady thin-layer / acoustic correction),
   optimized as the objective. Best if the correction has a closed form;
   at marginal St an asymptotic series is uncontrolled — the "correction"
   is then a model, needing its own error bar.
5. **ML surrogate of the unsteady map** (neural operator / LSTM-ROM)
   trained on unsteady runs, optimized in the loop, with verification
   runs. Rejected as *objective carrier*: unverifiable extrapolation in
   design space; admissible only as a preconditioner/explorer (FORK-31).

*Decision criterion.* Requirement (v) demands a NAMED, EVALUABLE bound,
not an asymptotic claim at marginal St. The only mechanism in the option
space that MEASURES (rather than models) the surrogate gap at finite St
is the HB ladder: |J_HB(K) − J_HB(K−1)| decaying in K gives an evaluable
(heuristic-tail, declarable) bracket, and J_HB(K→∞) = periodic-flow
average under H-DATA. The existence question for J_exact (liminf/limsup)
collapses under H-DATA + stable periodic response to the well-defined
period average.

*Recommendation.* Optimize J (option 1) as the working objective;
carry (v) via option 2 evaluated AT CANDIDATE OPTIMA (K-ramp at S*, few
designs), with option 3 as a single confirmatory run at the final S*.
Grounds: cost isolation — the expensive rungs price the *bar*, not every
iterate; HB is the only measuring instrument for the gap at marginal St.
Optionally, if the K-ramp shows the gap has a stable low-order-in-St
structure across designs, switch late to option 4 with the measured
coefficient (then the correction is calibrated, not assumed).

*Falsifier.* (a) HB fails to converge in K at marginal St (period-
doubling / non-periodic response ⇒ H-DATA monitor fires; the objective
falls back to liminf/limsup brackets from option 3 windows — declared
failure boundary). (b) The measured gap |J_HB − J| at optima exceeds the
optimization gains between competing designs ⇒ the quasi-steady rung is
the wrong optimization variable; promote HB(K small) to the in-loop
objective (adjoint-capable).

---

**FORK-2 — Discretization of the phase average (quadrature over Ξ).**

*Question.* How many per-phase solves per objective evaluation, placed
where, with what error control?

*Options.*
1. **Fixed trapezoidal/rectangle rule in cycle time** (uniform in the
   pushforward variable). For a PERIODIC integrand, trapezoid is
   spectrally accurate if the integrand is analytic/smooth in ξ
   (Trefethen–Weideman 2014) — see dry proof P1.
2. **Gauss/Clenshaw–Curtis quadrature** in ξ: superior only on
   non-periodic smooth integrands; on a periodic cycle it forfeits the
   trapezoid's spectral advantage. Rejected for the periodic core;
   retained if Ξ is re-parametrized non-periodically (e.g. split at a
   shock passage where F(·;s(ξ)) has a kink in ξ).
3. **Adaptive quadrature with per-phase error estimates**: place nodes
   where F varies fastest (near the detonation-front passage the state
   family s(ξ) traverses its extreme states). Best when the integrand
   has localized ξ-structure; costs adaptivity logic and complicates the
   SHARED-adjoint bookkeeping (weights vary per design ⇒ extra term in
   the gradient unless weights frozen per outer iterate).
4. **Monte Carlo / randomized quadrature (SAA / stochastic gradient)**:
   sample ξ_i ~ μ; unbiased gradients; enables stochastic-approximation
   optimizers (SGD/Adam-class, or stochastic trust region, e.g. STORM:
   Chen–Menickelly–Scheinberg 2018). Best when |Ξ| is effectively
   high-dimensional (it is 1-D here) or when per-phase cost must be cut
   per iterate. In 1-D periodic, MC's N^{-1/2} is dominated by
   trapezoid's spectral rate — rejected as primary; retained as the
   variance-reduction frame if H-DATA is later relaxed to a measure over
   modes (then Ξ is no longer 1-D).
5. **Sparse/low-rank phase compression**: cluster phases by state-space
   proximity, solve representatives, correct by sensitivity transport
   (∂F/∂s known from the adjoint). A principled cost-cutter; adds a
   model-error term that must be carried in (v).

*Decision criterion.* Smoothness of ξ ↦ F[S; s(ξ)]: measure it (FFT decay
of F over one cycle at a reference design). If spectral decay is
observed, option 1 wins outright at ~10–40 nodes; kinks in ξ (phase
where a shock enters/leaves the domain, or the sonic topology changes)
⇒ split-domain option 2/3.

*Recommendation.* Option 1, N_ξ chosen by a measured tail criterion:
double N_ξ until |J_{2N} − J_N| < derived tolerance (FORK-25 chain);
that difference IS the phase-quadrature carrier for (v). Freeze nodes
during each outer optimization phase so the discrete objective is a
FIXED smooth function (no adaptivity noise into the optimizer);
re-audit nodes at trust-region resets.

*Falsifier.* Measured FFT of F over the cycle shows algebraic decay
(integrand kink) ⇒ switch to split trapezoid at the located kink; if
kink location is design-dependent, the kink phase becomes an internal
variable with its own sensitivity (kink tracking, same machinery as
shock-fitting in ξ).

*Dry proof P1 (trapezoid spectral accuracy).* If g is 2π-periodic and
analytic in a strip |Im θ| < a, then the N-point trapezoid error is
≤ C e^{−aN} (standard contour-integral estimate; Trefethen–Weideman
2014, Thm 3.2). Hypotheses: analyticity in ξ of the composed map
ξ ↦ s(ξ) ↦ F — plausible away from per-phase topology changes; exactly
what the FFT probe tests. Decides FORK-2 in favor of option 1 whenever
the probe shows geometric decay.

---

**FORK-3 — Nominal vs robust treatment of μ and H-DATA.**

*Question.* Optimize against the given μ (nominal), or against an
ambiguity set (robust/DRO), and how is H-DATA violation monitored?

*Options.*
1. **Nominal SAA on given μ** — cheapest; certificate conditioned on
   H-DATA; monitor is external.
2. **Distributionally robust (DRO)**: max_S min_{μ' ∈ U(μ)} J with U a
   Wasserstein or moment ball (Mohajerin Esfahani–Kuhn 2018). Best when
   the data measure is itself uncertain (mode jitter, wave-count
   uncertainty). Costs an inner sup and typically nonsmooth coupling.
3. **Multi-mode weighted robust**: finite set {μ_n} for candidate wave
   counts n, worst-case or weighted — the classical multipoint robust
   design (Huyse–Lewis 2001) — the discrete, tractable face of 2.
4. **Chance/CVaR treatment of the separation constraint only** (see
   FORK-18) with nominal objective — decouples robustness in the
   constraint (where it is safety-critical) from the objective.

*Decision criterion.* The brief PINS H-DATA as a declared, monitorable
hypothesis with the design conditioned on it; the certificate stack is
per-hypothesis. Robustness beyond H-DATA is scope growth unless the
monitor's own falsifier needs it.

*Recommendation.* Option 1 for the certified object, plus option 4's
margin-hardening on g_sep (a deterministic margin η > 0 derived from the
measured phase-interpolation error of s(ξ), not a probabilistic model).
Monitor design (part of the problem per the brief): a cycle-spectral
residual — project measured/asserted interface data on the single-mode
rotating-wave ansatz s(θ − 2πft·n); H-DATA monitor statistic = relative
L² residual + wave-count Fourier concentration; threshold derived from
the sensitivity |∂J/∂s| (adjoint-based data sensitivity: the SAME
adjoint fields give ∂J/∂(interface data) for free — use them to convert
data-residual to objective-error, giving the H-DATA term of (v) an
evaluable carrier).

*Falsifier.* If the adjoint-based data sensitivity shows ∂J/∂s · (mode-2
contamination) comparable to design-to-design J differences at realistic
contamination levels, nominal design is not robust-representative ⇒
escalate to option 3 with measured mode weights.

---

### Group B — Design representation (the design space itself)

---

**FORK-4 — Geometry representation family.**

*Question.* In what computational class does S live?

*Options (full open-literature space).*
1. **Explicit contour parametrization per sector**: B-splines/NURBS
   (Braibant–Fleury 1984), Bézier, CST (Kulfan 2008), Hicks–Henne bumps
   (1978), PARSEC-type engineering bases; for nozzles specifically:
   arc + polynomial/spline bell (Rao-inspired but as *initialization
   only*, not as class restriction). Best: smooth, low-dimensional,
   exact wall representation for fitted solvers, constraints (curvature,
   angles, cone condition) expressible in control-point space, mature
   sensitivity chain.
2. **Free-form deformation (FFD)** of a baseline (Sederberg–Parry 1986;
   Kenway–Kennedy–Martins 2010): deforms any topology it is given; best
   for wrapping existing shapes; weak here because there is no canonical
   baseline per sector and FFD does not natively enforce cone/curvature
   admissibility.
3. **CAD-native (parametric feature tree) with CAD sensitivities**
   (Xu–Jahn–Müller 2014): best for manufacturing hand-off; sensitivity
   robustness across rebuilds is fragile; unnecessary at this modelling
   level.
4. **Level-set representation** φ: E → R, S = {φ ≤ 0} with Hamilton–
   Jacobi transport (Allaire–Jouve–Toader 2004): topology-capable,
   natural for the union-of-sectors design space; needs immersed or
   cut-cell flow discretization (accuracy of wall pressure/slip is the
   certified quantity — the weak point), and the cone condition must be
   imposed via constraints on φ (nontrivial).
5. **Density/porosity relaxation (SIMP-for-fluids)** (Borrvall–Petersson
   2003): compressible-Euler porosity penalization is uncertifiable at
   the wall (spurious boundary layers of the penalization, slip not
   exactly represented). Rejected as carrier; admitted as the FAMILY-C
   scout/bound device only if a proven relaxation inequality is
   established (see FORK-28).
6. **Neural implicit geometry (SDF networks / INRs)**: differentiable,
   topology-capable, compact; verification of admissibility (cone
   condition, curvature bounds) only by sampling — no certificate;
   rejected as carrier FOR A STATED REASON: admissibility must be
   provable per design, and sampled checks cannot certify a continuum
   condition without a Lipschitz bound on the network that would be
   loose by orders of magnitude. Admitted inside the explorer (FORK-29)
   where only evidence, not certificates, is produced.
7. **Morphable component / geometry projection (MMC/GPM)** (Guo et al.
   2014; Norato et al. 2015): explicit components with topology change;
   interesting middle ground; less mature for compressible slip-wall
   external/internal flow than 1+sector logic; kept as fallback if
   sector enumeration proves too coarse.

*Decision criterion.* Which representation lets EVERY certificate be
computed: (a) exact wall geometry for the fitted, certified state solves
(FORK-9/10); (b) admissibility A(c) checkable/provable per design;
(c) smooth design-to-objective map inside each sector for (ii)/(iii);
(d) topology handled somewhere (FORK-5).

*Recommendation.* Option 1 (B-spline contours, sector-structured) as the
certified carrier, with FORK-5 handling topology by enumeration+scout,
and option 4 as the scout representation. Grounds: only explicit smooth
contours give simultaneously exact slip-wall solves, provable
admissibility (spline curvature/angle bounds are computable exactly on
each polynomial segment — Bernstein-coefficient bounds give SUFFICIENT
certificates: a Bernstein-form bound on κ(t) over a segment certifies
the curvature constraint WITHOUT sampling), and a smooth reduced
objective. This is also the representation with a provable existence
link (FORK-30): spline classes with bounded control polygons are compact
in the right topology, and cone conditions can be enforced by linear
constraints on control points (offset conditions), giving A(c)-membership
by construction.

*Falsifier.* If optimized sector shapes press against the spline class
(objective still improving under knot insertion without saturation,
FORK-6 criterion), the class is biasing the optimum ⇒ enrich (FORK-6) or
re-open option 7. If the level-set scout finds a topology no sector
covers (e.g. multi-lip shrouded hybrid) with better relaxed J, sector
list was incomplete ⇒ add sector, re-run carrier.

---

**FORK-5 — Topology handling (sectors as outputs).**

*Question.* How does the optimization span the union of topology sectors?

*Options.*
1. **Sector enumeration**: fixed finite list (bell; plug/aerospike;
   shrouded plug; expansion–deflection; possibly annular-bell hybrids),
   each optimized in its own smooth chart; compare certified optima.
   Best: every sector's optimum is fully certified; globality across
   sectors = max over finitely many certified values (+ per-sector δ).
   Risk: unlisted topologies.
2. **Level-set with topological derivative** (Sokolowski–Żochowski 1999;
   Amstutz–Andrä 2006): nucleate holes/bodies where the topological
   gradient indicates; discovers sectors. Certification weak in-flight
   (immersed walls), so use as SCOUT: run at moderate fidelity, harvest
   the topology, hand to a sector chart.
3. **Simultaneous relaxed formulation (FAMILY C proper)**: one relaxed
   problem whose optimum is post-processed ("thresholded") into a solid.
   Rejected as carrier: the threshold step loses the certificate chain
   (the thresholded design's J can drop unpredictably; the relaxed J is
   an upper bound only if relaxation is proven — that role is kept in
   FORK-28, deliberately separated from design production).
4. **Evolutionary topology search** (GA over graph-grammar or
   constructive geometry encodings): maximal breadth, no certificates,
   high cost; admitted only as a background explorer at low fidelity if
   compute is idle. Rejected as a primary for stated reason: evidence
   without certificates duplicates option 2 at higher cost.

*Decision criterion.* Does a mechanism exist to BOUND what unlisted
topologies could gain? Yes — the FORK-28 physical upper bound B is
topology-blind (it bounds J over ALL of A(c)); therefore enumeration's
incompleteness risk is absorbed into δ = B − J[S*] rather than being a
silent hole. This is the decisive point: with a topology-blind B,
option 1's certificate is honest even if the list is short.

*Recommendation.* Option 1 as carrier + option 2 as scout. Order:
scout first (cheap, discovers candidate sector list), then per-sector
carrier runs. δ reported globally against B, not per sector.

*Falsifier.* Scout topology beats all sector optima at scout fidelity by
more than the scout's own (declared, estimated) fidelity error ⇒ the
sector list was load-bearing-wrong; add the sector. B − max_sector J
large while sector optima cluster tightly ⇒ either B is loose (improve
FORK-28) or a topology is missing (rerun scout wider).

---

**FORK-6 — Design-space dimension and adaptive refinement.**

*Question.* Fixed parametrization or adaptively enriched, and by what
criterion?

*Options.*
1. **Fixed dimension chosen a priori** (engineering practice): simplest;
   risks class-bias (optimum of the class, not of A(c)).
2. **Hierarchical knot insertion / degree elevation on demand**
   (progressive parametrization; Anderson–Aftosmis 2015; Han–Zingg
   2014): optimize coarse, insert knots where a refinement indicator
   fires, re-optimize warm-started. Nested spaces ⇒ monotone improvement
   of the class optimum; the sequence of class optima is a certified
   LOWER staircase converging (if saturating) toward the A(c) optimum.
3. **A-priori fine parametrization + regularization** (many DOFs from
   the start, Sobolev-smoothed gradients to tame ill-conditioning;
   Jameson-style): avoids refinement logic; conditioning and noise
   handled by FORK-7; risks optimizer wandering in near-null directions.
4. **Adjoint-based design-space error indicator**: the refinement signal
   is the projection of the continuous shape gradient onto the orthogonal
   complement of the current basis — computable from the SAME adjoint
   (the continuous shape-derivative density along the wall, e.g. the
   Hadamard form dJ = ∫ G(x) V·n ds, restricted-minus-projected). This
   turns "is the class biasing me" into a measured residual:
   ‖(I − Π_class) G‖ vs ‖G‖.
5. **Basis learned from snapshots (POD of shapes / active subspaces**,
   Constantine 2015): compression of an already-explored space; useful
   for the explorer and for reducing FORK-28's bound dimension; not a
   carrier (bias by construction).

*Decision criterion.* Requirement (i)/(iv) interplay: the certified
argmax is over A(c), not over a spline class; so either the class limit
is reached (indicator ↓ 0) or the class bias must appear as a NAMED term.
Option 4's indicator is exactly that named term.

*Recommendation.* Option 2 driven by option 4's indicator, stopping when
the indicator falls below the derived tolerance at which further class
gain is smaller than the (v) error bars (no point refining the design
space below the noise floor of the objective — see FORK-25 chain).
Report final ‖(I−Π)G‖ as the "representation residual" carrier in the
certificate.

*Falsifier.* Staircase of class optima not saturating while indicator
is small ⇒ indicator is blind (e.g. optimum at a class boundary /
constraint-active kink where the Hadamard form is invalid) ⇒ switch
indicator to finite-difference class-enrichment probes (insert one knot,
measure ΔJ directly, at a few adjoint-suggested locations).

---

**FORK-7 — Conditioning and regularity of the design map (gradient
smoothing / metric choice).**

*Question.* In what inner product is the design gradient taken, and is
regularization a penalty or a metric?

*Options.*
1. **Euclidean gradient in control-point coordinates**: standard;
   mesh/knot-dependent scaling; high-frequency shape noise amplified as
   DOFs grow (classical shape-optimization pathology).
2. **Sobolev (H¹/H²) gradient smoothing** (Jameson 1995-lineage;
   implicit smoothing = Laplace–Beltrami preconditioning of the shape
   derivative): reinterpret regularization as a change of metric — the
   OPTIMUM is unchanged, the PATH is preconditioned. Cheap (1-D solve
   along the contour).
3. **Shape-Hessian symbol preconditioning** (Arian–Ta'asan 1999; the
   Euler shape Hessian is pseudo-differential of known order — smoothing
   order matched to the symbol): best asymptotic conditioning; symbol
   known for model problems, only estimated here.
4. **Tikhonov penalty on shape irregularity** (adds λ‖κ‖² to J): changes
   the optimum; every λ is a magic constant unless derived — REJECTED at
   this problem for stated reason: the brief bans undeclared knobs, and
   curvature control already lives in A(c) as HARD constraints; a soft
   duplicate distorts the certificate (KKT of the wrong functional).
5. **Trust region in a shape metric** (TR radius measured in H¹ of the
   normal displacement): couples with FORK-17.

*Decision criterion.* Metric choices that leave the optimum invariant
are free (pure preconditioning); anything that shifts the optimum needs
a derivation the brief does not license.

*Recommendation.* Option 2 with smoothing order matched to a MEASURED
Hessian symbol (probe the reduced Hessian's action on high-frequency
shape modes via Hessian-vector products, FORK-23; fit the decay
exponent; set the smoothing order to flatten it — a derived, not magic,
smoothing parameter). Option 5's metric aligned with the same H^s.

*Falsifier.* If measured symbol order varies strongly over the contour
(mixed sub/supersonic wall regions have different orders), a single
global smoothing order mis-preconditions ⇒ spatially varying smoothing
(variable-order 1-D operator), still optimum-invariant.

---

**FORK-8 — Imposition of geometric admissibility A(c).**

*Question.* How are cone condition (h0, ω), curvature/angle bounds,
length/radius/wetted-size proxies, and attachment on Λ imposed?

*Options.*
1. **By construction in the basis** (linear inequalities on control
   points ⇒ admissible for ALL parameter values in a polytope): strongest
   — feasibility is certificate-free (always true); available for
   attachment (interpolation end conditions), cone/monotonicity (control
   polygon conditions), angle bounds (control-leg slopes). Conservative
   for curvature (sufficient, not necessary, via Bernstein bounds).
2. **As NLP constraints** g_i(S) ≤ c_i with exact evaluators + gradients:
   sharp; needs constrained optimizer (already have one); infinitely many
   pointwise constraints (κ(t) ≤ κ_max ∀t) become semi-infinite — same
   machinery as FORK-18 (Bernstein-certified sufficient check + exchange
   on violating t*).
3. **Projection/repair operators** (project iterates onto A(c)):
   composable with any optimizer incl. derivative-free; projection onto
   curvature-constrained spline sets is itself a nonconvex program —
   costly, nonsmooth kinks at projection boundaries.
4. **Penalty/augmented Lagrangian on violations**: soft; tolerable
   in-flight, but FINAL certificate needs hard feasibility — so at best a
   globalization aid.

*Decision criterion.* Certificates: final design must be PROVABLY in
A(c). Only 1 (by construction) and 2-with-certified-check deliver proof.

*Recommendation.* Hybrid: attachment, symmetry, envelope, length by
construction (option 1: linear); curvature/angle by option 2 with
Bernstein sufficient certificates and exchange refinement where the
sufficient check is too conservative (subdivide the Bernstein form —
converges to sharp by de Casteljau subdivision, a certified branch-and-
bound on the constraint itself). Cone condition: enforce via a linear
sufficient condition on control-point offsets (uniform cone with axis
data fixed per sector); dry check: a C¹ contour with slope bounded by
tan ω and minimal feature size ≥ h0 satisfies the (h0, ω) cone condition
— provable per segment from Bernstein slope bounds.

*Falsifier.* Optimizer persistently rides the conservative Bernstein
boundary (multiplier positive) while sampled true curvature is slack ⇒
conservatism is costing thrust; deepen subdivision (measured gap
Bernstein-bound vs sampled max decides depth).

---

### Group C — State model, solution concept, and the constraint g_sep

---

**FORK-9 — Solution concept and embedded-discontinuity treatment
(decides differentiability of everything downstream).**

*Question.* Shock-capturing, shock-fitting, or smooth-class solves — and
what does each do to dJ/dS?

*Options.*
1. **Shock-capturing finite-volume/DG with limiters**: robust, general;
   BUT the design-to-solution map is nonsmooth at the cell scale;
   pointwise sensitivities oscillate O(1/h) at captured shocks while
   INTEGRATED functionals and their adjoints converge under
   entropy-consistent schemes (Giles–Pierce 2001; Ulbrich 2002 for
   scalar laws) — see P4. Limiter nonsmoothness injects gradient noise
   with magnitude that must be measured (FORK-25).
2. **Shock-fitting / front-tracking** (Moretti lineage; modern revival:
   Bonfiglioli–Paciorri 2014): discontinuities are internal boundaries
   with Rankine–Hugoniot enforced; solution is PIECEWISE SMOOTH by
   construction; design map smooth as long as the shock topology is
   fixed; sensitivities exact incl. shock-position derivative. Certifies
   the solution class natively (the brief demands class certification).
   Cost: topology bookkeeping; a shock appearing/disappearing across
   designs is a nonsmooth event of the OPTIMIZATION (handled as a
   declared regime boundary, cf. FORK-19).
3. **Method of characteristics (MoC)** in fully supersonic subdomains:
   spectral-quality smooth solves where valid; cannot cross embedded
   subsonic pockets; the classical nozzle tool — use as the
   supersonic-subdomain engine inside option 2's decomposition and as an
   independent cross-check oracle.
4. **Smooth-class-only solves** (assume shock-free flow, monitor for
   violation): cheapest and cleanest IF optimal nozzles at these
   pressure ratios are shock-free internally (well-designed nozzles
   avoid internal shocks; plug/E-D sectors may carry lip expansions and
   possible weak fish-tail shocks external to the wetted wall). Cannot
   be assumed — must be MONITORED (a shock detector as certification
   constraint: if the certified-class solve's smoothness monitor fires,
   the design exits the smooth class and option 2 takes over).
5. **Space-time / interior-penalty stabilized FEM with adjoint
   consistency** (Hartmann 2007 adjoint-consistent DG): best dual
   consistency story for DWR (FORK-24); still capturing-class w.r.t.
   smoothness.

*Decision criterion.* The certificate stack: (ii)/(iii) need a
differentiable (or at least semismooth-with-known-structure) reduced
map; (v) needs DWR-quality error estimates; the brief explicitly makes
solution-class certification the designer's duty. Option 2 (+3 inside)
uniquely delivers class certification AND smooth sensitivities; option 1
delivers robustness and is the industry default.

*Recommendation.* Two-tier: option 1 (adjoint-consistent capturing,
option 5 flavor) as the EXPLORATION-tier solver (robust on arbitrary
intermediate designs), option 2/3 composite as the CERTIFICATION-tier
solver on candidate optima and final KKT/Hessian verification. The two
tiers cross-validate (independent-oracle principle): |J_capture −
J_fitted| at same design is itself a measured model-residual carrier
for (v).

*Falsifier.* If fitted-tier finds a different shock topology than
capturing-tier at the same design (beyond grid-artifact level), the
class certification fails ⇒ non-uniqueness alarm (FORK-11) and the
design is flagged uncertifiable (FORK-20 handles the optimizer's
response).

*Dry proof P4 (capturing sensitivities).* For 1-D Burgers with a
parameter-dependent shock at x_s(α), the pointwise derivative ∂u/∂α
contains δ(x − x_s) x_s'(α); a captured (smeared) shock represents this
as an O(1/h)-tall, O(h)-wide spike: pointwise wrong, but its integral
against smooth test functions converges — hence J' converges for
integrated J while pointwise sensitivity diverges. Hypotheses: single
isolated shock, entropy-consistent scheme, J an integral functional
(thrust IS one). Consequence: capturing-tier gradients are usable for
integrated J but pointwise-constraint gradients through shocks (e.g.
g_sep evaluated AT a point near a shock foot) are NOT trusted from the
capturing tier — route those through the fitted tier or aggregate
(FORK-18) before differentiating.

---

**FORK-10 — Per-phase solver architecture and state certification.**

*Question.* How is each steady per-phase solve produced and certified?

*Options.*
1. **Global implicit steady solve** (Newton–Krylov with pseudo-
   transient continuation, PTC; Kelley–Keyes 1998): general (mixed
   sub/supersonic), quadratic terminal convergence ⇒ machine-residual
   states (certifiable residual norm); the workhorse.
2. **Space marching** where axial flow is everywhere supersonic (the
   classical nozzle regime): O(N) cost, no global solve; INVALID across
   subsonic pockets/recirculation — validity itself is checkable
   (marching well-posedness monitor: axial eigenvalue sign field).
3. **Homotopy/continuation in phase**: use φ_{k} solution to warm-start
   φ_{k+1}; the cycle is a natural continuation loop (states are close);
   near-free 2–10× cost reduction on the N_ξ family.
4. **Anderson-accelerated / nonlinear multigrid FAS**: cost-tier
   options, orthogonal to certification; adopt as available.
5. **Certified a-posteriori bounds on the state** (residual-based bounds
   for conservation laws are weak in general; for steady Euler no sharp
   general theory) — honest statement: state "certification" here means
   (a) residual to derived floor, (b) discrete conservation exactness,
   (c) solution-class monitors (shock detector, positivity,
   supersonic-outflow check), (d) cross-tier agreement (FORK-9), NOT a
   mathematical enclosure. Declare this as the certification meaning —
   rigorous enclosures for 2-D Euler are an open problem (name it, don't
   fake it).

*Decision criterion.* Cost dominates (N_ξ solves per objective), but the
per-phase certification list (5) is non-negotiable for (i)/(v).

*Recommendation.* 1 with 3's phase-continuation as the default; 2 as the
fast path when its validity monitor passes (many nozzle phases will be
fully supersonic); certification = the declared list in 5.

*Falsifier.* Phase-continuation seeding produces hysteresis (different
converged states depending on sweep direction) ⇒ direct evidence of
per-phase non-uniqueness (FORK-11 fires); continuation is then run from
independent cold starts on the disagreeing phases.

---

**FORK-11 — Non-uniqueness of the per-phase weak solution.**

*Question.* Multi-D steady Euler weak solutions are not known unique
(convex-integration wild solutions; multiple steady states, e.g. dual
transonic solutions). What is the operational selection principle and
its monitor?

*Options.*
1. **Numerical-viscosity selection + declared solver family**: define
   the certified state as the vanishing-viscosity-limit candidate the
   scheme family selects; monitor by grid- and scheme-diversity (two
   dissipation mechanisms agree ⇒ evidence of a stable selected branch).
2. **Entropy-rate / physical admissibility filters**: check entropy
   inequality cellwise; excludes expansion shocks; does not resolve
   genuine dual branches (both entropic).
3. **Stability-based selection**: accept a steady state only if it is
   the long-time limit of the unsteady solver from the physical initial
   condition (the phase-sweep history) — the operationally meaningful
   branch for a rotating cycle is the one the unsteady flow ACTUALLY
   visits; FORK-1's HB/unsteady rung provides exactly this check at
   candidate optima.
4. **Enumerate branches** (deflation techniques, Farrell et al. 2015):
   find MULTIPLE steady states deliberately; per-phase J becomes
   set-valued; optimize worst-case over branches (robust) — the honest
   but expensive treatment if dual branches are found in-envelope.

*Decision criterion.* Empirical: does branch multiplicity OCCUR in the
design/phase range? Probe with 4 (deflated solves) at extreme phases on
representative designs, early (order of battle, §4).

*Recommendation.* 1+2 always-on (cheap monitors); 3 at candidate optima
(rides FORK-1's runs for free); 4 as an early one-off probe and again
at the final design. If multiplicity found: worst-case-over-branches
objective for the certificate (declared), option 3's dynamic selection
for the reported value.

*Falsifier.* Deflation finds distinct entropic branches with ΔJ above
the (v) error bar at any visited design ⇒ single-valued J is dead;
certificate re-scoped to the branch-robust value (this is a REGIME
declaration, not a failure).

---

**FORK-12 — Sonic set / choking treatment.**

*Question.* The throat/sonic surface controls mass flow and the validity
of downstream marching; how is it treated in solve and sensitivity?

*Options.*
1. **Nothing special** (capturing tier resolves transonic smoothly if
   scheme is transonic-capable): adequate for exploration.
2. **Fitted sonic line in the certification tier** (transonic
   characteristic decomposition; classical transonic-nozzle analysis):
   sonic line as internal boundary, smooth sensitivities of the mass-flow
   split; consistent with FORK-9 option 2.
3. **Choking as an explicit constraint/monitor**: per-phase mass flow
   m(ξ; S) is data-determined when Γ_d is supersonic-axial; where the
   interface has subsonic portions (brief: closure must be declared),
   the closure declaration IS the choking model — the audit hook for
   the brief's admissibility premises. The subsonic-inflow closure
   (e.g. specified stagnation state + flow angle, mass flux emergent)
   must be declared as part of the problem data audit, and its
   sensitivity contribution flows through the same adjoint.

*Decision criterion.* Where Γ_d data are already supersonic-axial
(detonation products at the interface), the sonic-set question is
interior or absent; MEASURE the fraction of phases with subsonic axial
inflow — the fork's weight is proportional to it.

*Recommendation.* 1 for exploration; 2 within certification tier; 3's
closure declaration mandatory in the data audit regardless.

*Falsifier.* Sensitivity of J to the declared subsonic closure
(computable by adjoint against closure parameters) exceeding (v) bars ⇒
the closure is load-bearing physics, not bookkeeping — escalate to the
model layer above (out of this lens's scope, but the number forces it).

---

**FORK-13 — The separation criterion g_sep: functional form for
optimization.**

*Question.* Separation is viscous; the core model is Euler. What
computable, differentiable g_sep with declared detection semantics?

*Options (criterion families).*
1. **Wall-pressure-ratio criteria** (Summerfield p_w/Pa ≥ α_S ≈ 0.35–0.4;
   Kalt–Badal; nozzle-flow-separation correlations of Stark 2010:
   p_w/Pa ≈ 1/(1+M_w) family): algebraic in wall state ⇒ smooth,
   adjoint-cheap; empirically calibrated on bell nozzles — coefficient
   validity per sector must be declared (plug/E-D differ).
2. **Adverse-pressure-gradient / Stratford-type integral criteria**:
   integral of the wall pressure recovery; more physics, still
   correlation-class; smooth.
3. **Coupled boundary-layer module** (integral BL: Thwaites/Head/Green;
   e.g. quasi-simultaneous viscous-inviscid interaction, Veldman 2001)
   with separation = BL criterion (H ≥ H_sep or c_f ≤ 0): the declared
   "viscous model layer" of the brief made computational; differentiable
   until separation onset (where VII coupling itself becomes singular —
   the criterion is evaluated at margin, before singularity).
4. **RANS verification tier**: not in the loop; at candidate optima only,
   as the empirical falsifier of whichever criterion is adopted.
5. **Learned separation classifier** (trained on RANS/experiment):
   rejected as certificate carrier (unverifiable extrapolation);
   admissible as an explorer-tier prefilter.

*Decision criterion.* The brief requires an EXPLICIT criterion with
margin semantics; the optimization needs g_sep smooth in (S, ξ) near
the boundary g_sep = 0 (for (ii)/(iii) and aggregation in FORK-18);
the certificate needs a declared validity domain and an empirical
falsifier tier.

*Recommendation.* g_sep from option 3 (integral BL margin) as the
certified criterion — it is the least-magic option whose coefficient
is a model, not a tuned constant — with option 1 as the cheap in-loop
proxy during exploration (both computed; proxy calibrated against BL
margin on the fly: measured offset+slope, giving the proxy a derived
tolerance). Option 4 at final designs.

*Falsifier.* RANS tier contradicts the BL-margin sign at any candidate
optimum within its own declared accuracy ⇒ criterion invalid in that
sector's regime; certificate re-issued conditional on the RANS-corrected
margin (and the correlation constant becomes a measured, per-sector
quantity).

---

### Group D — Optimality framework and optimizer

---

**FORK-14 — Optimize-then-discretize (OD) vs discretize-then-optimize
(DO) vs dual-consistent both.**

*Question.* Which optimality system is the object of record?

*Options.*
1. **DO (discrete adjoint of the discrete residual)**: gradients exact
   for the COMPUTED J to machine precision ⇒ optimizer sees a consistent
   finite-dimensional NLP; KKT residual is checkable to floor (the
   (ii) certificate is a NUMBER). Discrete adjoint may converge to a
   wrong continuous adjoint if the discretization is not dual-consistent
   (Hartmann 2007) — affects DWR and continuous interpretation, not the
   NLP's internal consistency.
2. **OD (continuous adjoint, then discretize)**: cleaner continuous
   optimality structure (the (ii) derivation the brief asks for —
   per-phase adjoints coupled through the shared contour, averaged wall
   condition, transversality at endpoints, multiplier meaning);
   discretized gradients are inconsistent with discrete J at O(h^p) ⇒
   optimizer stalls at gradient-inconsistency floor; certificates
   asymptotic, not checkable at fixed h.
3. **Dual-consistent DO (the both-limits option)**: choose the
   discretization (adjoint-consistent DG/SBP-SAT; Hicken–Zingg 2011)
   so the discrete adjoint IS a convergent approximation of the
   continuous one ⇒ one adjoint serves the NLP certificate (exact
   discrete KKT) AND the continuous derivation (ii) AND DWR (FORK-24).

*Decision criterion.* The certificate stack needs BOTH a checkable
discrete KKT residual and the continuous optimality derivation named in
(ii); only option 3 makes them the same object.

*Recommendation.* Option 3. Where the certification-tier solver
(shock-fitted composite) lacks an off-the-shelf dual-consistent
discretization, enforce dual consistency at the interface conditions
(R–H internal boundary adjoint conditions derived by hand — the fitted
analog of adjoint consistency; the continuous derivation of (ii) then
doubles as the implementation spec). LOAD-BEARING: this fork fixes the
meaning of every downstream tolerance.

*Falsifier.* Adjoint-consistency verification (FORK-22's tests on
manufactured duals + superconvergence check of functionals: dual-
consistent schemes superconverge J at rate 2p; measured rate < 2p ⇒
inconsistency located) fails after repair attempts ⇒ retreat to DO
(option 1) + separate hand-derivation of (ii) with an explicit
consistency-gap term carried in (v).

---

**FORK-15 — Reduced-space (NAND) vs full-space (SAND / one-shot).**

*Options.*
1. **Reduced-space (nested analysis and design)**: optimizer sees only
   design DOFs; each iterate = N_ξ converged solves + adjoints. Cost
   per iterate high; every iterate CERTIFIABLE (converged states —
   matters for FORK-20's boundary and for trusting g_sep values);
   quasi-Newton on ~10²–10³ design DOFs is mature.
2. **Full-space one-shot**: iterate on (u_ξ, λ_ξ, S) simultaneously
   (Biros–Ghattas LNKS; Hazra–Schulz): 3–8× cheaper to the optimum in
   benign problems; here the Jacobian blocks over N_ξ phases share only
   the design coupling ⇒ block-bordered KKT, good structure; but
   intermediate iterates have UNCONVERGED states ⇒ g_sep and
   certification meaningless in-flight, hidden-constraint region
   invisible until late; globalization of one-shot on transonic Euler
   with topology-varying designs is research-grade fragile.
3. **Hybrid**: reduced-space until trust region localizes, then one-shot
   polishing to machine KKT (the certificate wants a tiny KKT residual;
   one-shot terminal phase is the cheap way to grind it down).

*Decision criterion.* Certification-in-flight need + robustness beats
raw cost here; terminal KKT grinding favors full-space locally.

*Recommendation.* 1 as backbone, 3's terminal polish adopted if the
terminal KKT residual (FORK-26) proves expensive to reach by NAND alone.

*Falsifier.* Measured wall-clock share of state solves > ~80% with
quasi-Newton iteration count not decreasing under better curvature
(FORK-17) ⇒ NAND is the binding cost ⇒ revisit one-shot with the
phase-block preconditioner.

---

**FORK-16 — Optimizer class (the full menu, per the breadth
requirement).**

*Options, each at its best.*
1. **SQP (active-set or line-search; SNOPT/filterSQP-class)**: best
   constraint handling for smooth NLP with few hundred DOFs and
   expensive functions; active-set identification gives exactly the
   multiplier/complementarity structure that (ii) wants to exhibit.
2. **Interior-point (IPOPT-class)**: robust for many inequality
   constraints (N_ξ separation constraints if not aggregated); barrier
   smears activity identification (multiplier meaning for (ii) less
   crisp until μ→0 ramp done carefully).
3. **Trust-region Newton-CG with exact Hessian-vector products** (via
   second-order adjoints; Steihaug-CG): the (iii) certificate machinery
   REUSED as the optimizer's curvature engine; negative-curvature
   directions exploited (escapes saddles — relevant since (iii) must
   distinguish max from saddle anyway).
4. **Quasi-Newton (L-)BFGS with Sobolev metric**: default cheap
   curvature; damped/limited-memory; pairs with FORK-7.
5. **CMA-ES** (Hansen): best derivative-free local-global searcher in
   10²-dim; invariant to monotone transforms; handles noise and mild
   discontinuity; ~10³–10⁴ evaluations — affordable ONLY at
   explorer fidelity.
6. **MADS with progressive barrier (NOMAD; Audet–Dennis 2006/2009)**:
   the rigorous derivative-free constrained framework; Clarke-
   stationarity guarantees on nonsmooth problems; the reference method
   for HIDDEN constraints (FORK-20) — its role here.
7. **DIRECT / Lipschitz global** (Jones 1993): certificate-flavored
   global search but only with a KNOWN Lipschitz constant (unavailable;
   see FORK-28's rejection of Lipschitz certificates); useful on ≤10-dim
   subspaces (e.g. sector-level coarse variables).
8. **Bayesian optimization (GP-EI/UCB; SMAC/BoTorch-class)**: best
   sample-efficiency ≤ ~20-dim; feeds the explorer and the multistart
   seeding (FORK-29); its "regret bounds" assume GP-truth — evidence,
   not certificate.
9. **Genetic/evolutionary (NSGA-II etc.)**: population diversity over
   topology-mixed encodings; dominated by 5/8 for continuous shape
   refinement (stated reason: order-of-magnitude worse sample
   efficiency in smooth regimes); retained only if the design encoding
   becomes mixed discrete-continuous (sector flags + shape) in the
   explorer.
10. **Stochastic-gradient / SAA methods (Adam, STORM, stochastic TR)**:
    relevant only if FORK-2 had chosen sampled phases; with fixed
    quadrature the objective is deterministic ⇒ not applicable as
    primary (stated reason), kept for a future measure-valued Ξ.
11. **Nonsmooth solvers (bundle methods, gradient sampling;
    Burke–Lewis–Overton 2005)**: the fallback if FORK-19 declares the
    reduced map genuinely nonsmooth at scale (min over branches, sector
    boundaries): certified Clarke-stationarity machinery.

*Decision criterion.* Smooth certified tier (FORK-9 tier-2 + FORK-14)
⇒ the certificate optimizer must expose active sets, multipliers, exact
curvature: 1 or 3. Exploration tier tolerates nonsmoothness/hidden
constraints ⇒ 5/6/8.

*Recommendation.* Certificate tier: SQP (1) with TR-Newton-CG (3) as
the terminal phase (multiplier clarity + curvature certificate in one).
Explorer tier: 8 (≤20-dim sector coarse spaces) seeding 5 (full shape
space at low fidelity), with 6 as the wrapper wherever hidden
constraints are dense. All explorer results are SEEDS, never claims.

*Falsifier.* If the certificate tier repeatedly converges to points the
explorer strictly dominates (beyond error bars), the smooth tier's
basin structure is deceiving (nonsmooth ridges) ⇒ elevate 11 to the
certificate tier (Clarke-KKT replaces KKT in (ii), declared).

---

**FORK-17 — Globalization and curvature policy.**

*Options.*
1. **Line search (Wolfe) + BFGS**: cheap, standard; Maratos-prone near
   active constraints; curvature quality decays in noisy gradients.
2. **Trust region (TR) in the H^s shape metric (FORK-7)** with
   Steihaug-CG on exact Hessian-vector products: handles indefiniteness
   natively (this problem is a MAXIMIZATION with expected saddle
   structure across sector-interior geometry modes); TR radius gives the
   natural coupling to model-error management (FORK-31: TRMM).
3. **Filter globalization** (Fletcher–Leyffer): avoids penalty
   parameters (aligned with the no-magic-constants rule — penalty
   weights are exactly the kind of undeclared knob the brief bans).
4. **Cubic regularization (ARC)**: best worst-case complexity; per-step
   subproblem cost similar to TR; adopt if TR heuristics (radius update
   constants) are challenged as magic — ARC's parameters are also
   constants, but its σ adapts by the same measured principle; tie.

*Recommendation.* 2 + 3 (TR-filter SQP): trust region in the derived
shape metric, filter instead of penalties, CG-truncated Newton with
second-order adjoints; radius-update constants DERIVED from the
measured actual/predicted-reduction statistics (accept thresholds set
where the measured ρ-histogram separates model-valid from model-broken
steps — a data-derived, declared constant).

*Falsifier.* Persistent TR collapse (radius → noise floor of FORK-25
without KKT progress) ⇒ gradient noise dominates: drop to the noise-
robust explorer or raise per-phase solver tolerance floor (re-derive
chain).

---

**FORK-18 — Aggregation of the per-phase separation constraint
(semi-infinite structure).**

*Question.* g_sep(S; s(ξ)) ≤ 0 for μ-a.e. ξ: how imposed finitely?

*Options.*
1. **Discretize-all**: impose at all N_ξ quadrature phases: N_ξ
   constraints; exactness only at nodes; between-node violation bounded
   only if a ξ-Lipschitz bound on g_sep is measured (computable: the
   phase-adjoint gives ∂g_sep/∂ξ along the cycle; max over cycle of the
   measured derivative × node spacing = derived inter-node margin η).
2. **KS aggregation** (Kreisselmeier–Steinhauser; Martins–Poon 2005):
   KS_ρ = max + (1/ρ)ln Σ e^{ρ(g_i−max)}; single smooth constraint;
   conservative side controllable — see P3; ρ ramped, not magic:
   choose ρ from the derived bound so that aggregation error <
   inter-node margin η (both derived).
3. **p-norm / induced aggregates**: same family, worse conditioning at
   high p; rejected in favor of KS (stated reason: KS's error bound is
   additive and explicit, P3).
4. **Exchange / Blankenship–Falk SIP**: keep a working set of active
   phases; solve, find the cycle's most-violating phase by a cheap 1-D
   global search in ξ (the inner problem is 1-D! — this is the
   structural gift of the problem), add, repeat; finite convergence
   under mild assumptions (Blankenship–Falk 1976). The 1-D inner
   problem makes classical SIP genuinely cheap here.
5. **Chance/CVaR relaxation** (allow separation on a μ-measure ε set):
   changes the ENGINEERING meaning (intermittent separation each cycle
   = unsteady side loads); rejected for the certified class as the
   brief demands a.e. attachment; retained as a diagnostic scalar
   (CVaR profile of margins tells WHERE the cycle binds).
6. **Exact-penalty/NCP reformulation of the a.e. constraint**
   (∫ max(g,0)²dμ = 0): degenerate multipliers at solutions (violates
   the multiplier-meaning requirement of (ii)); rejected, stated
   reason: destroys the marginal-value interpretation.

*Recommendation.* 4 wrapped around 2: exchange method on the true 1-D
inner problem for exactness, KS within the working set for smoothness;
inter-node certification via option 1's measured Lipschitz margin.
Multipliers: the exchange multipliers at convergence approximate the
measure-valued multiplier of the continuous SIP (the density of the
binding-phase measure) — this is precisely the "multipliers carrying
marginal-value meaning" of (ii): dJ/dc_sep = −∫ λ(ξ) d(binding measure).

*Falsifier.* Binding set turns out to be a nontrivial ARC of phases
(not isolated points): exchange working set grows without saturation ⇒
switch to a continuous binding-arc parametrization (free-boundary
formulation of the binding set: treat arc endpoints as variables with
their own transversality — this is the (ii) endpoint condition
surfacing in ξ-space).

*Dry proof P3 (KS bounds).* max_i g_i ≤ KS_ρ(g) ≤ max_i g_i + ln(m)/ρ,
directly from monotonicity of ln Σ exp. Hypotheses: none beyond
finiteness. Consequence: given target aggregation error η_KS, ρ =
ln(m)/η_KS is DERIVED. Decides the "is ρ magic" objection.

---

**FORK-19 — Nonsmooth events of the reduced map (activity changes,
sector boundaries, shock birth).**

*Options.*
1. **Ignore (treat as smooth, let TR absorb kinks)**: works when events
   are codimension-≥1 and optima are interior to smooth pieces; verify
   a-posteriori that S* is not ON an event surface.
2. **Event-constrained formulation**: add explicit constraints keeping
   the iterate inside a declared regime cell (no shock birth, fixed
   active topology), optimize per cell, compare across cells — the
   piecewise-smooth (PC¹) treatment; certificates valid per cell;
   cross-cell optimality by enumeration + boundary check (a boundary
   optimum shows a Clarke-stationarity condition combining adjacent
   cells' gradients).
3. **MPCC machinery**: if any regime condition is naturally a
   complementarity (e.g. attached-or-separated switching entering the
   model), regularize (Scholtes) with a DERIVED regularization path and
   MPCC-tailored stationarity (C-/M-stationarity; Scheel–Scholtes
   2000); only if such a structure actually enters (currently the
   certified class EXCLUDES separated designs, so no complementarity
   is active in the carrier — noted to keep the option honest).
4. **Full nonsmooth solver** (FORK-16 opt. 11) — the sledgehammer.

*Recommendation.* 2 as the doctrine (regime cells = certified classes;
matches FORK-9's fitted-topology bookkeeping), 1 in the explorer.

*Falsifier.* Certified optimum sits at a cell boundary with combined-
gradient stationarity (detected by cell-boundary Clarke check) ⇒ the
boundary is load-bearing physics (e.g. optimal design rides shock
birth) ⇒ promote the event to an explicit smooth constraint with its
own multiplier (its marginal value then REPORTS the cost of the
regime boundary — informative, not pathological).

---

**FORK-20 — Certification boundary as hidden constraint (designs whose
state cannot be certified).**

*Question.* Some S ∈ A(c) yield uncertifiable states (solver
divergence, class-monitor failure, non-unique branches). The optimizer
must navigate a domain with holes it cannot see analytically.

*Options.*
1. **Extreme barrier** (J := −∞ on failure; Audet–Dennis): simple;
   kills line-search/TR smooth methods (gradient undefined at the
   wall); native in MADS.
2. **Progressive barrier / filter on a certification-violation measure**
   (Audet–Dennis 2009): needs a graded violation signal — we HAVE one
   (residual stagnation level, monitor margins) ⇒ build h(S) =
   certification-violation aggregate; treat as a constraint with
   values, not a boolean.
3. **Classification surrogate of the certifiable region** (GP/SVM
   classifier updated online; "expensive-to-evaluate feasibility",
   Basudhar et al. 2012): explorer-tier tool to avoid wasting solves;
   never a certificate.
4. **Trust-region backtracking on failure with anisotropic radius
   shrink** (treat failure as model invalidity): keeps the smooth tier
   running; risks crawling along the boundary.
5. **Design the certified region to be known-in-advance** (a-priori
   sufficient conditions on S for solvability, e.g. monotone area ratio
   + angle bounds per sector): strongest when available — a PROVABLE
   inner approximation of the certifiable set; likely conservative;
   worth deriving per sector because inside it the hidden constraint
   VANISHES (the certificate-tier optimum should be sought inside the
   provable region first, with the boundary-riding case handled only if
   the inner optimum presses against it).

*Recommendation.* 5-first doctrine: derive per-sector sufficient
solvability conditions (dry-level: for a monotonically expanding
supersonic sector with wall angles below the Prandtl–Meyer margin to
vacuum and above the compression-coalescence bound, the marching
solution exists and is smooth — classical characteristics argument);
optimize inside; if the optimum is interior, hidden constraints never
fired and the certificate is clean. Outside the provable region:
smooth tier with 2's graded violation + 4; explorer with 1/3.

*Falsifier.* Inner-region optimum presses the provable boundary with
positive multiplier ⇒ the conservatism is costing thrust; then the
graded-barrier campaign (2) across the true boundary is REQUIRED and
the certificate must carry the boundary-riding caveat (Clarke-type
condition at the certification frontier — declared).

---

### Group E — Derivatives and their verification

---

**FORK-21 — Derivative computation.**

*Options.*
1. **Discrete adjoint via reverse-mode AD of the residual** (dolfin-
   adjoint-style or hand-assembled Jacobian-transpose with AD locals):
   exact to roundoff for the discrete map; N_ξ adjoint solves per
   gradient (one per phase — embarrassingly parallel); the ONLY option
   whose gradient error is a floor, not a model.
2. **Continuous adjoint hand-derived**: cheaper memory, physics
   transparency (needed anyway for (ii)); inconsistency at fixed h
   (FORK-14) unless dual-consistent pairing.
3. **Forward AD / tangent**: O(n_design) cost — only for verification
   columns and for the ξ-derivative (∂g/∂ξ, 1 tangent).
4. **Finite differences with DERIVED steps**: never primary (n_design
   solves per gradient, subtractive cancellation); verification-only,
   with the step h* derived, not guessed — see P2.
5. **Complex-step** (Squire–Trapp 1998; Martins et al. 2003): exact to
   machine precision without subtraction; requires complex-analytic
   code path — limiters/abs/max/branching break analyticity: valid on
   the FITTED smooth tier (which avoids limiters by construction!) —
   a happy structural alignment; verification gold standard there.
6. **Second-order adjoints (Hessian-vector)**: forward-over-reverse;
   needed by FORK-17/23; cost ≈ 2–4 gradient equivalents per product.

*Recommendation.* 1 (with dual-consistent pairing per FORK-14) as
production; 5 on the fitted tier and 4-with-derived-step on the
capturing tier as verification; 3 for ξ-tangents; 6 for curvature.

*Falsifier.* Dot-product test (FORK-22) fails at > 100× roundoff floor
after debugging ⇒ some component is not the true adjoint of the
implemented residual (usually: BC or limiter branch) — the test
localizes it by operator splitting (test each operator's transpose
separately).

*Dry proof P2 (derived FD step and noise floor).* For central
differences with objective evaluation noise ε_J (measured, FORK-25),
error(h) ≈ M₃h²/6 + ε_J/h with M₃ = |∂³J| scale ⇒ h* = (3ε_J/M₃)^{1/3},
error* ≈ (ε_J²M₃)^{1/3}·const. Both ε_J (Moré–Wild ECNoise estimator,
2011: measured from J along a short design ray) and M₃ (from three
Hessian-vector products or a spline fit along the ray) are MEASURED ⇒
h* is derived, and the achievable FD verification tolerance is KNOWN
BEFORE the test — the test can therefore REJECT (adjoint vs FD gap
exceeding derived error* = failure, not "close enough").

---

**FORK-22 — Derivative verification protocol (the rejector battery).**

*Options / components (all adopted; the fork is which are mandatory).*
1. **Dot-product (transpose) test**: ⟨Av, w⟩ = ⟨v, Aᵀw⟩ to roundoff for
   every linearized operator; mandatory, per-operator.
2. **Taylor-remainder ramp**: |J(S+hV) − J − h dJ[V]| = O(h²) with
   measured slope 2.00±derived band over a decade bracketing h*
   (P2 gives the valid decade); mandatory on the full chain.
3. **Complex-step cross-check** on the fitted tier: |∂J_CS − ∂J_adj|
   < derived floor; mandatory where analyticity holds.
4. **Adjoint-consistency / superconvergence check** (FORK-14 falsifier):
   functional convergence at 2p ⇒ dual consistency confirmed;
   mandatory once per discretization family.
5. **Green's-identity residual for the continuous adjoint** (OD side):
   consistency of hand-derived (ii) with discrete adjoint fields on a
   sequence of meshes: ‖λ_h − λ_cont‖ → 0 at expected rate.
6. **Randomized probes** (Hutchinson-style random V draws) vs
   worst-case directions (high-frequency shape modes — the ones
   FORK-7 says are dangerous): both; the high-frequency probes are the
   ones that catch smoothing/metric bugs.

*Decision criterion / recommendation.* All six; each with a DERIVED
pass band (from P2's ε_J and the roundoff floor κ(A)·ε_mach scaling).
Any failure is a stop-the-line event (poisons every certificate
downstream).

*Falsifier of the protocol itself.* A battery-passing gradient that
still mispredicts measured ΔJ on a finite step (TR ρ-statistics
systematically ≠ 1 on small steps) ⇒ noise model wrong (ε_J
underestimated) ⇒ re-run ECNoise with longer rays; if persistent,
suspect non-deterministic solver paths (parallel reduction order) —
enforce deterministic reductions in the certificate tier.

---

**FORK-23 — Second-order machinery for certificate (iii).**

*Options.*
1. **Hessian-vector products via second-order adjoint + Lanczos**
   extreme-eigenvalue estimation of the reduced Hessian projected on
   the active tangent cone: verifiable form of (iii) — report
   λ_max(P H P) ≤ 0 within derived eigenvalue error (Lanczos residual
   bounds are computable — Kaniel–Paige theory gives certified
   brackets from the tridiagonal).
2. **Dense reduced Hessian by n forward-over-reverse sweeps**: exact
   spectrum; affordable if n_design ≲ 200 at the terminal design only.
3. **Quasi-Newton (BFGS) Hessian as evidence**: rejected as certificate
   (secant approximations carry no sign guarantee; stated reason),
   retained as optimizer curvature.
4. **Directional sampling (random probes of curvature)**: probabilistic
   evidence only.

*Recommendation.* 1 for in-flight and the certificate; 2 once at S*
if n permits (also feeds FORK-28's local-globality radius). Active
tangent cone assembled from the SQP active set with multiplier
sign-checks (strict complementarity verified numerically; if
degenerate multipliers appear, report the weak-(iii) form on the
critical cone — declared).

*Falsifier.* Lanczos finds λ_max > 0 within brackets on the tangent
cone at "converged" S* ⇒ S* is a saddle: restart along the certified
ascent direction (this is the (iii) certificate doing its job, i.e.
REJECTING the stationarity claim).

---

### Group F — Error control, tolerances, stopping

---

**FORK-24 — Mesh/estimator policy for objective error bars.**

*Options.*
1. **Goal-oriented DWR** (Becker–Rannacher 2001; Fidkowski–Darmofal
   2011 survey for CFD): η_J = Σ_K |⟨R(u_h), λ_h⟩_K|; drives adaptation
   AND furnishes the (v) discretization carrier; needs the dual-
   consistent adjoint we already have (FORK-14 synergy); estimate, not
   bound — effectivity must be MEASURED on a mesh sequence (declared
   safety factor = measured worst effectivity × margin derived from
   its variance, not a magic 2).
2. **Richardson extrapolation / GCI (Roache)**: model-free rate-based
   bars; valid only in the asymptotic range — verify observed rate
   before trusting; use as the CROSS-CHECK of DWR effectivity (two
   independent estimators agreeing = the error bar's own certificate).
3. **Residual-based (non-goal) estimators**: adapt where the SOLUTION
   is rough, not where J cares; rejected as primary (stated reason:
   thrust is a boundary functional — DWR localizes to what feeds it).
4. **Uniform refinement studies only**: the brute-force fallback;
   pays N_ξ × mesh-family cost; kept for the FINAL design only.
5. **Anisotropic metric-based adaptation** (Loseille–Alauzet): best
   cost-per-accuracy for shocked flows; compose with DWR (goal-oriented
   metric); adopt in capturing tier.

*Recommendation.* 1 (+5 in capturing tier), cross-checked by 2 at
candidate optima and by 4 at the final S*. Per-phase bars combined into
the J-bar by the quadrature weights (plus FORK-2's phase-truncation
term) — the (v) "discretization error" carrier is the weighted sum
with measured effectivity band.

*Falsifier.* DWR effectivity drifting with refinement (not settling
near 1) ⇒ dual not converging (adjoint inconsistency at shocks —
known failure mode) ⇒ fitted-tier duals take over the estimate near
discontinuities.

---

**FORK-25 — The tolerance chain (every tolerance derived).**

*The chain (this fork is a design, options are per-link).* Machine ε →
(a) linear-solver tolerance → (b) nonlinear per-phase residual floor →
(c) objective evaluation noise ε_J → (d) gradient noise ε_g →
(e) optimizer step/KKT tolerances → (f) certificate bands.

*Per-link derivation.*
- (b): converge Newton until residual stagnates at the measured
  roundoff plateau (plateau detection: residual-drop slope < derived
  threshold from κ(J_F)·ε_mach); the plateau VALUE is measured per
  phase, not asserted.
- (c): ε_J by ECNoise (Moré–Wild 2011) along design rays — the honest
  noise of the whole pipeline (incl. adaptivity if any, which is why
  FORK-2/24 freeze adaptivity inside optimization phases).
- (d): ε_g from the adjoint analog: gradient evaluations along a ray,
  variance about a smooth fit; relation ε_g ≈ ε_J/ℓ_corr checked.
- (e): terminate when ‖P∇J‖ ≤ ν·ε_g with ν derived from the desired
  false-positive rate of "stationary" declarations under measured
  noise (a hypothesis test, not a threshold guess): see P8.
- (f): each certificate band = RSS or sum (declared which, per
  correlation argument) of the measured link contributions.

*Dry proof P8 (noise-floor stopping).* If measured gradient noise is
ε_g (std), then observing ‖∇J_computed‖ ≤ ν ε_g rejects "true gradient
norm > (ν+z_α)ε_g" at confidence α by Chebyshev/Gauss bounds on the
n-dim noise ball; choosing α (declared, e.g. the same α used across
all certificates) DERIVES ν. Hypotheses: unbiased noise (checked by
the ray-fit residuals' symmetry). Consequence: "converged" is a
statistical statement with stated power — it can REJECT.

*Falsifier of the chain.* Any downstream band observed violated in
cross-checks (e.g. FD-vs-adjoint gap exceeding its derived band,
FORK-22) invalidates the upstream measurement it depended on — the
chain is re-measured from that link down (the chain's DAG is the
audit map).

---

**FORK-26 — Outer stopping and the KKT certificate number.**

*Options.* (1) fixed KKT tolerance (magic — banned); (2) noise-floor
stopping per P8 (recommended, with the KKT residual reported WITH its
noise band); (3) budget stopping with declared incompleteness (the
honest fallback: certificate reports "KKT residual reached r at budget
B", no stationarity claim). Recommendation: 2, with 3 as the declared
degraded mode. Falsifier: stationarity claimed at P8's α, then a
restart from a perturbed point finds ΔJ > combined bands ⇒ the noise
model lied; escalate per FORK-25's chain audit.

---

**FORK-27 — Assembly of the (v) error bar (named carriers).**

*The bar is a SUM of measured terms, each with its own falsifier:*
1. Unsteadiness: |J_HB(K*) − J| + HB tail estimate (FORK-1); falsified
   by the confirmatory unsteady run disagreeing beyond the claimed sum.
2. Phase quadrature: |J_{2N_ξ} − J_{N_ξ}| tail (FORK-2).
3. Discretization: DWR-with-measured-effectivity (FORK-24), summed
   over phases.
4. Model residuals: capture-vs-fitted tier gap (FORK-9), subsonic-
   closure sensitivity (FORK-12), separation-criterion band (FORK-13),
   H-DATA data-sensitivity term (FORK-3).
5. Optimization incompleteness: δ from FORK-28 (reported separately —
   it bounds suboptimality, not J error — but listed so nothing hides).
Declared absences: viscous-loss modelling beyond the g_sep layer
(declared model scope), 3-D non-axisymmetric effects (excluded by the
brief's axisymmetric frame — named as an absence, not silently).

---

### Group G — Globality, existence, exploration

---

**FORK-28 — The globality mechanism: computing δ (requirement (iv)).**

*Question.* J[S*] ≥ sup_{A(c)} J − δ with δ COMPUTED. The load-bearing
certificate. What upper-bound mechanisms B exist?

*Options (full space, each at its best).*
1. **Physical/variational upper bound (recommended primary)**: bound
   the thrust functional over ALL admissible flows regardless of
   geometry: for each phase, the axial momentum + pressure integral of
   any exhaust flow fed by the interface mass/momentum/energy flux is
   bounded by the IDEALLY EXPANDED axial-uniform flow at ambient
   pressure — see P5. B = ∫_Ξ F_ideal(s(ξ)) dμ is computable by
   per-phase 1-D/algebraic calculations with the true h(T) caloric
   model (quadrature over T of the caloric integrals — no closed γ
   form needed). Topology-blind (covers all sectors, FORK-5), and
   TIGHT in the frictionless limit as L → ∞: δ then MEASURES the
   finite-length/envelope cost — an honest, interpretable gap.
   Refinements: (a) constrain the bound by the envelope (finite
   expansion ratio bounds achievable exit pressure per phase →
   tighter B via a 1-D bounded-area ideal expansion); (b) subtract
   provable divergence-loss lower bounds (minimum non-axiality forced
   by the cone condition and length bound — a calculus-of-variations
   mini-problem per sector, giving B a second-order sharpening).
2. **Convex relaxation / duality of the design problem**: for PDE-
   constrained design with nonconvex state constraints, no known
   computable dual with zero or certified gap (the state equation's
   nonconvexity enters the Lagrangian bilinearly); moment/SOS
   hierarchies (Lasserre) on a polynomialized reduced model: dimension
   ~10 max, works only on a surrogate whose surrogate-error would need
   its own certificate — rejected as primary (stated reason:
   certificate would be conditional on an unverifiable surrogate),
   retained as a sector-level coarse-variable cross-check.
3. **Lipschitz/DIRECT-type global bounds**: require a PROVEN global
   Lipschitz constant of ξ-averaged J over A(c); no mechanism to prove
   one for an Euler-constrained functional (only measured local ones)
   — rejected as certificate, stated reason: measured Lipschitz
   constants can be exceeded (silent failure mode).
4. **Branch-and-bound with interval/Bernstein arithmetic on the
   REDUCED polynomial parametrization + verified surrogate bounds**:
   sound only where a verified enclosure of J(design) exists — blocked
   by FORK-10 option 5's honest admission (no rigorous 2-D Euler
   enclosures). Named as THE hard obstruction: rigorous global
   optimization over PDE states of this class is beyond current
   verified-computation reach (state of the art: verified enclosures
   exist for elliptic/parabolic model problems — Plum, Nakao
   frameworks — not for steady 2-D gas dynamics with shocks).
5. **Statistical/multistart evidence** (multistart + BO posterior
   "probability of missed basin"): evidence, never δ — reported
   alongside, labeled as evidence (feeds FORK-29).
6. **Relaxation bound from FAMILY C**: IF a proven inequality
   J_relaxed ≥ sup_{A(c)} J is established for a specific relaxation
   (e.g. a convexified/porosity-free relaxed class containing all
   characteristic functions of A(c) sets), the computed relaxed
   optimum bounds δ. The PROOF of the containment+upper-semicontinuity
   is the hard step; possible for the geometric part, hard for the
   state part (relaxed-state thrust must be proven ≥ any classical-
   state thrust — plausible via the P5 mechanism applied to the
   relaxed fluxes: route the proof through interface-flux bounds
   rather than through the relaxed PDE). Kept as the second bound,
   pursued only if its containment lemma closes.

*Decision criterion.* A bound is admissible as certificate iff every
step of its evaluation is itself certified (measured caloric
integrals, quadrature bars). Only 1 (and conditionally 6) meet this.

*Recommendation.* Option 1 with refinements (a),(b): δ = B_refined −
J[S*], each term carrying its own (v)-style bar. Report option 5's
evidence separately. Where structure permits δ = 0 (the brief's ask):
only in degenerate sub-cases (e.g. if the envelope permits full ideal
expansion at every phase and the cone condition admits the ideal
contour — then S* achieving B within bars proves δ ≤ bars); state
this as the δ→0 mechanism and its (rare) trigger condition.

*Falsifier.* Any certified design found with J > B (beyond bars)
⇒ the bound proof is wrong (audit P5's hypotheses — most likely a
neglected interface-flux term, e.g. swirl momentum contributing to
axial thrust via pressure redistribution); the bound is repaired, not
patched numerically.

*Dry proof P5 (per-phase ideal-expansion bound — sketch).* Fix phase
ξ; the steady control-volume identity gives F = ∫_exit [ρu_x(u·n) +
(p−Pa)n_x] dA + (interface terms fixed by s(ξ)). Over all exit
states compatible with the interface's mass flux ṁ, total-enthalpy
flux Ḣ, and entropy flux ≥ interface value (entropy cannot decrease
in the frozen Euler evolution; shocks only increase it), the axial
momentum integrand is maximized by a uniform axial stream at p = Pa:
maximize ṁ·u_x + (p−Pa)A subject to h(T) + u²/2 = Ḣ/ṁ, s(T,p) ≥
s_in, mixture state equation; Lagrange conditions give p = Pa,
u = u_x (no transverse/swirl), s = s_in (isentropic), i.e. the ideal
fully-expanded state; concavity of the reduced integrand in the
remaining variable (checked with h(T), cp(T) real — requires cp > 0,
which holds) makes it the global max. Hypotheses NAMED: steady per
phase; entropy-flux monotonicity (theorem for entropy solutions);
exit measure finite; swirl at the interface reduces, never raises,
the bound (its energy is unavailable to axial momentum without
work input — enters via Ḣ split; keep the swirl term explicitly in
the bound if s(ξ) carries flow angle). Then B = ∫ F_ideal dμ bounds
J over ALL S since every admissible design produces some compatible
exit flow. This bound is the δ engine.

---

**FORK-29 — Global exploration layer (evidence generation).**

*Options.* (1) structured multistart (Latin hypercube over sector
coarse variables + per-sector physics-informed seeds); (2) BO on
≤20-dim sector spaces (best sample efficiency); (3) CMA-ES on full
shape spaces at explorer fidelity (best basin coverage in 10²-dim);
(4) GA/NSGA-II on mixed sector+shape encodings (only if the mixed
encoding materializes); (5) level-set scout (FORK-5). Recommendation:
2→3 cascade per sector + 5 across sectors; all results labeled
evidence; basin census reported (how many distinct KKT points found,
their J spread — feeds the honesty of option-5-in-FORK-28's
statistical statement). Falsifier: a certificate-tier polish from a
late random seed beating all census basins ⇒ census insufficient ⇒
widen explorer budget (the δ certificate is UNAFFECTED — that is why
δ rides the bound, not the census).

---

**FORK-30 — Existence structure (i) and its discrete shadow.**

*Options for the existence proof skeleton.*
1. **Cone-condition compactness (recommended)**: the class of domains
   satisfying a uniform (h0, ω) cone condition is compact in the
   Hausdorff-complementary topology, and geometric functionals of the
   type in c are l.s.c./continuous along it (Chenais 1975;
   Henrot–Pierre, *Variation et optimisation de formes*, 2005). The
   load-bearing missing link — NAMED, not faked: continuity (or upper
   semicontinuity) of S ↦ J[S] along Hausdorff-converging cone-
   condition domains for steady Euler flows with shocks is NOT a
   theorem in the literature; it must be either (a) proven in the
   certified smooth/fitted class (piecewise-smooth solutions with
   stable shock topology: continuity plausible via linearized
   stability of the fitted configuration — a per-sector THEOREM* to
   attempt), or (b) declared as the monitored failure boundary the
   brief explicitly allows (existence certified in the closed spline
   subclass instead — which IS compact finite-dimensional, where
   existence is elementary (continuous J on compact parameter
   polytope), with the class-bias term of FORK-6 carrying the gap to
   A(c)).
2. **Relaxation existence** (existence in a relaxed class + no-gap
   theorem): the standard escape when classical existence fails;
   the no-gap step shares FORK-28-6's hard lemma.
3. **Γ-convergence of discrete optima**: prove the discrete (spline,
   mesh-h) problems Γ-converge to the continuous one ⇒ cluster points
   of discrete optima are continuous optima; gives the principled
   meaning to "the computed S* approximates a true argmax"; needs the
   same continuity brick as 1(a).
*Recommendation.* 1(b) NOW (finite-dimensional certificate,
unconditional) + 1(a) as the theory target, with the FORK-6 indicator
quantifying what the subclass certificate leaves on the table.
*Falsifier of 1(a)-attempts.* A constructed sequence of cone-condition
domains whose fitted shock topology changes in the limit with a jump
in J (a counterexample candidate: shock birth at the limit domain) —
if found, existence over full A(c) genuinely needs relaxation (2).

---

**FORK-31 — Surrogates and multifidelity management (in-loop use).**

*Options.* (1) none (all solves full fidelity); (2) trust-region model
management (TRMM, Alexandrov et al. 2001) with first-order-corrected
low-fidelity models (coarse mesh / fewer phases / capture-tier as the
low model of the fitted tier): PROVABLY convergent to high-fidelity
optima (the only surrogate framework with a convergence certificate);
(3) GP/kriging mid-loop (EGO-style): no convergence-to-truth
certificate in-loop — explorer only; (4) POD/ROM per-phase state
surrogates with error indicators: adopt only with dual-based ROM
error bounds (rare for Euler; otherwise explorer-only); (5) neural
operators: explorer-only (stated reason: no verifiable error bound
class available). Recommendation: 2, with low model = (coarse mesh,
N_ξ/2 phases), corrections re-verified each TR cycle (the β/ρ
consistency checks of TRMM double as ongoing gradient verification).
Falsifier: TRMM ρ-statistics show low-model correction failing
persistently near optima (correction radius → 0) ⇒ drop to full
fidelity for the terminal phase (budget re-planned, certificate
unaffected).

---

**FORK-32 — Warm starts, continuation, and the outer loop schedule.**

*Options.* (1) cold everything (maximal independence, maximal cost);
(2) phase-chain warm starts (FORK-10.3) + design-step warm starts
(previous state as initial guess: valid while TR step ≪ state
sensitivity radius — monitored by Newton iteration count spikes);
(3) full continuation in a design homotopy (from a solvable seed
sector design): best against the FORK-20 boundary (stay-in-basin);
(4) simultaneous phase-block Krylov recycling (share Krylov subspaces
across adjacent phases; deflation of common modes). Recommendation:
2+4, with a periodic cold-start audit (every K-th accepted step,
one phase re-solved cold; disagreement beyond (b)-floor ⇒ hysteresis
alarm → FORK-11). Falsifier: warm-started optimizer path differs from
cold-audit path beyond bands ⇒ warm starts are biasing branch
selection — cold starts become mandatory on the certificate tier.

---

## 3. HARD OBSTRUCTIONS (named precisely, with state-of-the-art handles)

1. **No rigorous solution enclosures for steady 2-D Euler with
   shocks** ⇒ no fully rigorous global branch-and-bound (FORK-28.4)
   and state "certification" is a monitor bundle, not an enclosure
   (FORK-10.5). Handle: fitted-class certification + cross-tier
   oracles; watch verified-computation literature (Plum/Nakao-style
   methods are advancing toward hyperbolic problems).
2. **Shape-continuity of J over cone-condition domains for shocked
   Euler flow is an open lemma** ⇒ existence over full A(c) is
   conditional (FORK-30). Handle: unconditional finite-dimensional
   certificate + declared gap indicator; attempt the per-sector
   THEOREM* in the smooth/fitted class.
3. **Weak-solution non-uniqueness** (convex integration; dual
   transonic branches) ⇒ J possibly set-valued (FORK-11). Handle:
   deflation probes, dynamic-selection tier, worst-case-over-branches
   certificate re-scope if triggered.
4. **Separation is extra-model physics** for the Euler core ⇒ g_sep is
   a modelled criterion, its constant a calibrated quantity
   (FORK-13). Handle: integral-BL layer as declared model, RANS
   falsifier tier, per-sector validity statements.
5. **Marginal Strouhal** ⇒ no asymptotic regime for the unsteady
   correction (FORK-1). Handle: HB ladder as measuring instrument;
   the correction is measured, not expanded.
6. **δ = 0 "where structure permits" is rare**: the honest generic
   product is δ = B_refined − J[S*] with interpretable gap terms;
   claiming more requires the FORK-28.6 containment lemma or the
   degenerate full-expansion case.

---

## 4. ORDER OF BATTLE (dependency order; load-bearing marked ★)

Stage 0 — foundations that poison everything if wrong:
1. ★FORK-14 (dual-consistent DO): fixes the meaning of gradients,
   KKT numbers, DWR — decide FIRST, verify via FORK-22.4.
2. ★FORK-9 (solution concept, two-tier): decides differentiability
   and certification semantics for every phase solve.
3. ★FORK-4/5 (representation + sector doctrine): the design space
   itself; wrong class biases every optimum silently (mitigated only
   by FORK-6's indicator, which must therefore stand up with it).
4. FORK-25 chain bootstrap (measure floors/noise on the phase-0
   pipeline): tolerances precede any claim.

Stage 1 — machinery build-out (parallelizable):
5. ★FORK-21/22 (adjoint + rejector battery): no optimization before
   the battery passes; battery bands from the Stage-0 chain.
6. FORK-2 (phase quadrature, FFT probe), FORK-10 (solver arch),
   FORK-8 (admissibility-by-construction), FORK-13 (g_sep layer).
7. FORK-11 early deflation probe (branch census on representative
   designs/phases) — cheap now, catastrophic late.

Stage 2 — optimization campaigns:
8. FORK-20.5 (provable solvable region per sector), then FORK-16/17/
   18 campaigns (SQP-TR-filter + exchange-KS) per sector inside it;
   FORK-31 TRMM active; FORK-29 explorer runs concurrently at low
   fidelity; FORK-6 refinement staircase per sector.
9. FORK-26 stopping per noise-floor statistics.

Stage 3 — certificates at candidate optima:
10. FORK-23 (reduced-Hessian Lanczos, (iii)); FORK-24 (DWR bars +
    Richardson cross-check); FORK-1 HB ladder at S* ((v) unsteady
    term); FORK-27 assembly.
11. ★FORK-28 (bound B computation + refinements, δ): can be developed
    in parallel from Stage 1 (it is design-independent!) — compute B
    EARLY to know the available headroom; final δ at S*.
12. FORK-30 existence write-up (unconditional subclass form +
    conditional A(c) form), FORK-3 monitor deployment, FORK-27 final
    error-bar assembly.

Load-bearing summary: FORK-14, FORK-9, FORK-4/5, FORK-21/22, FORK-28.
A wrong choice at any of these five invalidates downstream work
wholesale; every other fork is locally repairable (its falsifier
triggers a bounded rework).

---

## 5. Compact fork index

| # | Topic | Recommendation (one line) |
|---|-------|---------------------------|
| 1 | Objective ladder | Quasi-steady J in-loop; HB ladder prices the unsteady bar at optima |
| 2 | Phase quadrature | Periodic trapezoid, N_ξ by measured tail; freeze in-loop |
| 3 | μ robustness / H-DATA | Nominal + derived g_sep margin; adjoint-based data-sensitivity monitor |
| 4 | Geometry representation | Sector-structured B-splines; Bernstein-certified admissibility |
| 5 | Topology | Sector enumeration carrier + level-set scout; δ absorbs unlisted sectors |
| 6 | Design-space refinement | Knot insertion driven by projected-gradient residual indicator |
| 7 | Design metric | Sobolev smoothing with measured Hessian-symbol order (optimum-invariant) |
| 8 | Geometric constraints | By-construction linear + Bernstein-sufficient with subdivision sharpening |
| 9 | Solution concept | Two-tier: adjoint-consistent capturing (explore) / shock-fitted+MoC (certify) |
| 10 | Per-phase solver | Newton-Krylov+PTC, phase continuation; certification = declared monitor bundle |
| 11 | Non-uniqueness | Deflation probes early; dynamic selection at optima; branch-robust re-scope if hit |
| 12 | Sonic/choking | Fitted sonic line in cert tier; subsonic-inflow closure declared and sensitivity-priced |
| 13 | g_sep form | Integral-BL margin (certified) + pressure-ratio proxy (in-loop), RANS falsifier tier |
| 14 | OD vs DO | Dual-consistent DO: one adjoint serves KKT number, (ii) derivation, DWR |
| 15 | NAND vs SAND | Reduced-space backbone; one-shot terminal polish if KKT grinding is dear |
| 16 | Optimizer class | SQP + TR-Newton-CG certify; BO→CMA-ES (+MADS for hidden constraints) explore |
| 17 | Globalization | TR-filter in derived shape metric; constants from measured ρ-statistics |
| 18 | Phase-constraint aggregation | Exchange SIP on the 1-D inner problem, KS inside working set (ρ derived) |
| 19 | Nonsmooth events | Regime-cell piecewise-smooth doctrine; Clarke check at cell boundaries |
| 20 | Certification boundary | Provable solvable inner region first; graded violation barrier outside |
| 21 | Derivatives | Discrete adjoint (dual-consistent); complex-step & derived-step FD verify |
| 22 | Verification | Six-test rejector battery with derived pass bands; stop-the-line on failure |
| 23 | Second order | Second-order-adjoint Lanczos with Kaniel–Paige brackets on the tangent cone |
| 24 | Mesh/estimator | DWR + anisotropic metric; Richardson cross-check; measured effectivity |
| 25 | Tolerance chain | Measured DAG: plateau → ECNoise → gradient noise → statistical stopping |
| 26 | Outer stopping | Noise-floor hypothesis test (derived ν, declared α); budget mode declared |
| 27 | Error-bar assembly | Named-carrier sum; declared absences listed |
| 28 | Globality δ | Physical ideal-expansion bound B (envelope-refined); δ = B − J[S*] |
| 29 | Exploration | BO→CMA-ES cascade + scout; evidence label; basin census reported |
| 30 | Existence | Unconditional spline-class certificate now; cone-condition THEOREM* target |
| 31 | Multifidelity | TRMM (provably convergent) with coarse-mesh/half-phase low model |
| 32 | Warm starts | Phase+design warm starts with periodic cold audits (hysteresis alarm) |
