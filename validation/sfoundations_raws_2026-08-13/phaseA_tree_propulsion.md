# PHASE-A ATTACK TREE — PROPULSION PHYSICS / NOZZLE AERODYNAMICS LENS

Derived INDEPENDENTLY from `phaseA_problem_brief.md` alone (frozen formal
statement) plus open literature. No project document consulted. Author
lens: rocket/airbreathing nozzle design, supersonic nozzle theory, RDE
wave dynamics and exit-plane physics, thrust accounting,
experimental/CFD validation practice.

Notation: J_exact = true time-averaged axial thrust; J = cycle-averaged
surrogate; St = f·τ_res (wave frequency x nozzle residence time, MARGINAL
per the brief); Γ_d = interface; Ξ, μ = phase set and measure; S = solid
set; A(c) = admissible class.

---

## 0. THE PHYSICAL SITUATION, STATED BLUNTLY

What an RDE actually delivers at a nozzle entrance (open literature:
Schwer & Kailasanath 2011/2013; Braun, Lu, Wilson et al. 2013; Rankin,
Schauer et al. 2017; Fotia, Hoke, Schauer 2016–2018; Bennewitz, Bigler,
Hargus et al. 2019; Anand & Gutmark 2019 review; Raman, Prakash,
Gamba 2023 review):

- Per cycle at a fixed azimuth: a pressure spike (factor ~3–10 over the
  cycle mean) as the detonation passes, followed by an expansion tail;
  an oblique secondary shock attached to the wave; a slip line / hot
  contact from the previous cycle; possible deflagrative afterburning
  of leaked propellant.
- Substantial AZIMUTHAL velocity (swirl) with a nonzero cycle mean for
  a single co-rotating wave; exit flow angles swinging ±10–30° over a
  cycle in published simulations.
- Radial stratification across the annulus (center-body wake, wall
  cooling films if any).
- Axial Mach at combustor exit is MIXED over the cycle: subsonic
  patches behind the wave, supersonic in the expansion tail. This is
  exactly why the brief's H-DATA well-posedness clause exists.
- Timescales: period 1/(n f) ~ 50–300 μs; nozzle residence
  L_noz/u ~ 100–300 μs. Hence St ~ O(1): the brief's "MARGINAL" is the
  physically honest statement, and it is the single most dangerous
  fact in the whole problem.
- Back-pressure feedback is REAL: throat area ratio and nozzle
  back-pressure are experimentally documented to change RDE wave
  count, direction, and stability (e.g., Fotia et al. 2016 aerospike
  RDE tests; Anand & Gutmark 2019). The brief's "causal separation" is
  a premise that real hardware can violate — the audit is not optional
  bookkeeping, it is where the physics can kill the formulation.

Everything below is organized so that the forks that can silently
invalidate the whole program (averaging legitimacy, causal separation,
swirl/3D data contract, topology treatment) come first in the order of
battle.

---

## 1. FORMULATION FAMILIES (the viable overall shapes of the attack)

FF-1 **Quasi-steady phase-ensemble family** (the brief's surrogate J):
per-phase steady axisymmetric Euler solves, averaged by μ. Cheap,
adjoint-friendly, certificate-friendly. Its legitimacy is entirely a
St→0 statement; at marginal St it needs a declared correction with a
bound (requirement (v)). Selects itself only if FORK-2/3 deliver a
computable bound.

FF-2 **Wave-frame steady family** (exactness anchor): if the flow is an
exact rotating wave (H-DATA), the FULL 3D flow is STEADY in the frame
rotating at the wave speed, and the time-averaged axial thrust equals
the steady wave-frame thrust integral exactly (dry proof DP-2 below).
One steady 3D Euler problem replaces the unsteady limit. Expensive per
design, but it is the truth-model against which FF-1's error bar is
measured, and a legitimate optimization vehicle itself at reduced
design counts.

FF-3 **Full unsteady family**: time-resolved URANS/LES of
combustor-coupled nozzle, thrust averaged over converged limit cycle.
The validation gold standard (with FF-2) but not an optimization
vehicle at certificate level: gradient noise, limit-cycle convergence,
and cost make (i)–(iv) unreachable. Retained as falsifier tier.

FF-4 **Reduced/spectral family**: harmonic balance / time-spectral
methods (Hall, Thomas & Clark 2002; McMullen & Jameson 2006) — the
periodic unsteady problem solved as a coupled set of N_h steady-like
problems in the frequency domain. Sits exactly between FF-1 and FF-3:
captures O(St) unsteadiness at a small multiple of FF-1 cost. The
natural CARRIER of the unsteady correction term in (v).

FF-5 **Surrogate/derivative-free global family**: DOE + Kriging/BO
(Jones et al. EGO 1998; Forrester & Keane 2009), CMA-ES (Hansen),
GA/NSGA — geometry campaigns over any of FF-1/2/4 as evaluators. Not a
certificate producer by itself (no (ii)–(iv)), but the correct GLOBAL
exploration layer across topology sectors and the correct fallback
where gradients are polluted (captured shocks, topology changes).

Selection criteria across families: (a) can it state and bound its
distance to J_exact (requirement (v))? (b) does it admit an adjoint /
optimality system (requirement (ii))? (c) cost-per-design vs number of
designs needed by the globality mechanism (iv)? Recommended
architecture: FF-1 as workhorse + FF-4 as correction carrier + FF-2 as
exactness anchor at candidate optima + FF-5 as sector-level global
layer + FF-3 as final falsifier. Every fork below refines this.

---

## 2. FAMILY A — LEGITIMACY OF CYCLE-AVERAGED DESIGN (load-bearing)

### FORK-1 — What exact object does the computable objective approximate?
- **Q**: Choose the exactness anchor relating J_exact to something a
  steady solver can touch.
- **Options at their best**:
  - O1 *Quasi-steady ensemble* (FF-1): J_exact ≈ Σ μ-weighted steady
    thrusts. Exact only as St→0; the entire per-phase machinery
    (adjoints, MoC, certificates) becomes available.
  - O2 *Wave-frame steady anchor* (FF-2): under H-DATA the unsteady
    problem IS a steady 3D problem; J_exact is computed, not
    approximated. Cost: 3D steady Euler with strong azimuthal
    nonuniformity; adjoint still available (steady!).
  - O3 *Mixed-out mean-state design*: average the DATA first (mass/
    momentum/energy-consistent mixed mean à la turbomachinery
    averaging, Cumpsty & Horlock 2006), design one steady nozzle for
    the mean state. The St→∞ limit; discards cycle structure.
  - O4 *Harmonic balance* (FF-4): finite Fourier set in cycle phase;
    converges to the unsteady answer with N_h.
  - O5 *Direct unsteady average* (FF-3).
- **Decision criterion**: DP-2 (below) shows O2 is EXACT under H-DATA
  with zero modelling debt; the choice is then economic: how many
  designs the optimizer needs vs 3D steady cost. The St→0 and St→∞
  limits (O1, O3) bracket the physics qualitatively but neither is
  controlled at marginal St WITHOUT a measured correction; O4 measures
  precisely that correction.
- **Recommendation**: Two-tier anchor: optimize under O1, CERTIFY the
  averaging error against O2 (and/or O4 with demonstrated N_h
  convergence) at the incumbent design(s). Declare O3 only as the
  opposing bracket end for the (v) error bar discussion. Grounds: the
  optimality machinery (ii)–(iv) is only affordable on O1; O2 is the
  unique zero-debt truth model this problem happens to possess —
  refusing to use it as the anchor would be malpractice.
- **Falsifier**: at a candidate optimum, |J_wave-frame − J_ensemble|
  exceeds the claimed (v) bound → O1-as-workhorse is rejected for that
  regime and the program moves to O4 or O2 as the optimization vehicle.

**DP-2 (dry proof — wave-frame steadiness and thrust invariance).**
Hypotheses: (a) H-DATA holds — the entire flow field is a rotating
wave q(r, θ − Ω_w t, x) with constant angular speed Ω_w = 2πf/n; (b)
the solid S and envelope E are axisymmetric. Then in the frame
rotating at Ω_w the flow is steady by construction. The frame rotation
axis is the nozzle axis x; Coriolis (−2Ω×u) and centrifugal
(−Ω×(Ω×r)) accelerations are both ⟂ e_x (Ω ∥ e_x ⇒ (Ω×v)·e_x = 0
for any v; centrifugal is radial). Hence the AXIAL momentum balance is
form-identical in both frames and the axial-thrust surface integral
F = ∫[ρu_x(u·n) + (p−Pa)n_x]dA is frame-invariant. Steadiness ⇒ the
time average is the steady value: J_exact = F_waveframe exactly. ∎
Consequence: "does averaging represent the real unsteady thrust" is
NOT a hypothesis at the level of the flow — it is exact in the wave
frame; the only approximation debt is carried by the AXISYMMETRIC
PER-PHASE decomposition (FORK-2), plus H-DATA itself.

### FORK-2 — Where does the quasi-steady per-phase model break at marginal St?
- **Q**: The ensemble J treats each phase ξ as an independent steady
  axisymmetric nozzle flow. What is discarded, and in which regime is
  each discard fatal?
- **Options at their best**:
  - O1 *Accept quasi-steady as-is* with an a-posteriori bound: valid
    when a fluid parcel transits the nozzle seeing an essentially
    frozen phase (St ≪ 1). Parcel-phase drift per transit = St cycles.
  - O2 *First-order St correction*: retain the leading unsteady terms
    (∂_t of stored mass/momentum evaluated from the phase-family's
    known cycle dependence) as a computable correction functional —
    a deferred-correction, still on steady solves.
  - O3 *Harmonic balance with N_h chosen by spectral decay* — the
    systematic version of O2; N_h is measured, not asserted.
  - O4 *Wave-frame 3D steady* (no discard; azimuthal transport terms
    kept exactly).
  - O5 *Mixed-out design* (St≫1 end): correct only if in-nozzle
    azimuthal/temporal mixing homogenizes the cycle before the throat
    — physically implausible for supersonic-dominated transit but
    it is the honest opposite bracket.
- **Decision criterion**: measure, per the brief's instruction that St
  is a parameter: (a) spectral content of s(ξ) (how many harmonics
  carry thrust-relevant amplitude); (b) the azimuthal-transport
  residual: evaluate the wave-frame azimuthal flux divergence terms ON
  the quasi-steady solution family — a computable defect that needs no
  new solve. If defect·(sensitivity) ≪ target error bar, O1/O2
  suffice; else escalate O3→O4.
- **Recommendation**: O2 as default carrier of the (v) unsteadiness
  term, promoted to O3 if the measured spectral decay is slow.
  Grounds: at marginal St a pure O1 claim is indefensible (the brief
  says so implicitly by declaring St marginal), while O4-everywhere
  destroys the optimization budget; O2/O3 keep steady machinery and
  produce a NAMED, EVALUABLE correction — exactly what (v) demands.
- **Falsifier**: O3 correction fails to converge with N_h, or the O2
  first-order term is not small relative to itself iterated (series
  non-asymptotic at the measured St) → quasi-steady family rejected;
  program pivots to O4 as the optimization vehicle (fewer, costlier
  iterations; FF-5 global layer becomes primary).

**DP-3 (dry scaling — the parcel-phase drift argument).** A parcel
entering at phase ξ0 exits having experienced phases spanning
Δξ = f·τ_res(streamline) = St. The per-phase steady functional error
for that parcel is ≤ Lip_ξ(state) · St in the state metric; thrust
error inherits this with the thrust-sensitivity Lipschitz constant.
This gives the FORM of the (v) unsteadiness term:
|J_exact − J| ≤ C_1·St + o(St), with C_1 evaluable from the phase
family's ξ-derivative (data-supplied) and the per-phase adjoint
(already computed for (ii)) — i.e., the adjoint field gives the thrust
sensitivity to inflow-state perturbations along the transit; no new
machinery. Hypotheses: smooth ξ-dependence between front passages;
the front passage itself contributes a separately-bounded impulsive
term (finite jump × passage measure), which must be carried
explicitly, not hidden in C_1.

### FORK-3 — Existence of the time-average limit and the liminf/limsup fallback
- **Q**: When is lim_{T→∞}(1/T)∫F dt guaranteed, and what is declared
  when it is not?
- **Options**: O1 assume periodicity (H-DATA) ⇒ limit trivially exists
  = one-period average. O2 almost-periodic/multi-mode flows: declare
  liminf/limsup brackets, monitor bracket width. O3 stochastic-process
  model of mode-hopping (measured transition statistics; objective =
  ergodic average under a Markov mode model). O4 worst-case over
  observed modes (robust design).
- **Decision criterion**: H-DATA monitor output (FORK-12). If the
  engine holds one mode for the mission envelope, O1. If it
  mode-hops, the DESIGN QUESTION changes (multi-mode robust nozzle) —
  that is a different problem and must be declared as such, not
  patched.
- **Recommendation**: O1 inside the certified class, with the H-DATA
  monitor as an explicit certificate precondition; O2 brackets
  reported whenever the monitor flags marginal behavior. Grounds: the
  brief pins H-DATA as declared-and-monitorable; physics says mode
  count is bistable/hysteretic (documented in Anand & Gutmark 2019),
  so the monitor is load-bearing, not decorative.
- **Falsifier**: monitored data shows mode transitions within the
  operating point used for μ → the certificate for that operating
  point is void by its own precondition; re-scope to O3/O4.

### FORK-4 — Objective robustness: deterministic μ vs uncertainty in the data family
- **Q**: μ and s(ξ) are measured objects with error. Optimize the
  nominal average, or a robust/stochastic variant?
- **Options at their best**:
  - O1 *Nominal deterministic* J with post-optimality sensitivity
    (adjoint gives dJ/d(data) nearly free).
  - O2 *Distributionally robust*: min over an ambiguity ball around μ
    (Wasserstein/moment-based; Rahimian & Mehrotra 2019 survey) of the
    average — protects against measurement bias in the cycle weighting.
  - O3 *Chance-constrained separation*: g_sep enforced with
    probability 1−ε rather than μ-a.e. (Nemirovski & Shapiro 2006).
  - O4 *Multi-point weighting* (classical multi-design-point nozzle
    practice): a small set of pinned worst/best phases with tuned
    weights — the aerospace-industrial standard at its best
    (transonic-airfoil multipoint lesson: single-point optima are
    brittle, Drela 1998).
  - O5 *Full stochastic programming / polynomial-chaos propagation of
    data uncertainty* (Ghanem, Najm; OUU as in Alexanderian et al.).
- **Decision criterion**: measured data-uncertainty magnitude vs the
  claimed δ and (v) bars. If data bars ≥ claimed optimality gap, a
  nominal certificate is physically meaningless — robustness is
  forced.
- **Recommendation**: O1 + reported dJ/d(data) norms as a mandatory
  certificate line; escalate to O2 only if that sensitivity times the
  measured data bar rivals δ. Keep the μ-a.e. separation constraint
  HARD (not chance-constrained): separation is a cliff (side loads,
  RSS transition — Frey & Hagemann 2000), not a graceful degradation.
- **Falsifier**: dJ/d(data)·(data bar) > δ at the incumbent → nominal
  optimum indistinguishable from its neighbors within data error;
  certificate must be re-issued in the O2 sense or δ inflated.

---

## 3. FAMILY B — INTERFACE SURFACE AND DATA CONTRACT (load-bearing)

### FORK-5 — Placement of Γ_d: where is "downstream of all heat release" real?
- **Q**: The brief pins Γ_d downstream of all heat release. Real RDEs
  afterburn (leaked deflagration, contact-surface burning). Where can
  Γ_d legally sit, and how is the pin audited?
- **Options**: O1 combustor exit lip plane (maximizes nozzle design
  authority; heat-release pin most likely violated). O2 a surface
  displaced downstream until a measured heat-release proxy (e.g.,
  total-enthalpy-flux settling; OH* in experiments) drops below a
  declared threshold (design authority shrinks; premise honest). O3
  keep O1 but carry a declared source-term residual layer (heat
  addition downstream of Γ_d as a bounded model defect entering the
  (v) budget). O4 make Γ_d placement itself a (discrete) design/audit
  variable with the audit as constraint.
- **Decision criterion**: the audit IS the criterion: compute the
  cycle-resolved total-enthalpy flux through a one-parameter family of
  candidate surfaces from the data source (rig or high-fidelity sim);
  Γ_d = first surface where d(enthalpy flux)/dx is below threshold
  with margin. Threshold DERIVED from the (v) budget: allowed thrust
  error per unit unaccounted heat release (Rayleigh-flow sensitivity
  estimate gives the conversion factor).
- **Recommendation**: O2 with O3 as the always-on residual accounting.
  Grounds: thrust is first-order sensitive to heat addition in
  supersonic flow (Rayleigh: heat addition at M>1 raises stagnation
  temperature but costs stagnation pressure); silently absorbing it
  falsifies the frozen-gas pin too (FORK-14).
- **Falsifier**: measured enthalpy-flux settling never occurs inside
  the envelope E → the frozen-downstream-of-Γ_d model class is
  rejected for this engine; the problem must be re-posed with a
  reacting layer (declared model-class change).

### FORK-6 — Causal separation: nozzle→combustor back-reaction (the contract's weakest premise)
- **Q**: RDE experiments show nozzle/throat back-pressure changes wave
  mode, count, even direction. Under what conditions is "no upstream
  influence of the design on the data" defensible, and what is the
  audit design?
- **Options at their best**:
  - O1 *Supersonic screen*: if the axial flow at Γ_d is supersonic for
    μ-a.e. ξ (all phases), characteristics cannot travel upstream;
    causal separation is a THEOREM, not a premise. Verify on data.
  - O2 *Impedance-band constraint*: for data with subsonic patches,
    constrain admissible designs to present the same acoustic/mean
    back-pressure impedance at Γ_d as the rig that measured the data
    (a new constraint g_imp(S) ≤ tol added to c) — causal separation
    holds to first order within the band.
  - O3 *Fixed-point outer loop*: optimize → install/simulate the
    optimum coupled to the combustor → re-measure s(ξ), μ → re-optimize;
    certificate claims only the converged pair (data, design).
    (This is the only honest handle when the feedback is strong; cf.
    coupled-plenum effects in Fotia et al. 2016, Anand & Gutmark 2019.)
  - O4 *Co-simulation* (couple a reduced combustor model — e.g., the
    Kaemming–Paxson RDE performance model or a 2D unrolled-annulus
    surrogate — to the nozzle in the loop): removes the premise
    entirely at heavy cost and new model debt.
- **Decision criterion**: the data themselves: fraction of (ξ, points
  on Γ_d) with subsonic axial Mach, and measured sensitivity of the
  combustor mode to back-pressure (rig sweep: vary a dummy throat
  area ±x%, watch mode). If mode is robust over the band spanned by
  candidate designs → O2 suffices; if not → O3 mandatory.
- **Recommendation**: O1-check first (it may simply hold for a
  well-placed Γ_d — detonation products expand quickly to supersonic
  axial Mach); else O2 with a rig-calibrated band, with O3 declared as
  the escalation path in the certificate's preconditions. Grounds:
  this is the fork where a mathematically flawless optimum can be
  physically meaningless — an optimum that changes the engine's wave
  mode has invalidated its own input data.
- **Falsifier**: coupled verification (O3 first iterate or O4 spot
  check) shows wave-mode or >band mean-pressure shift with the
  optimized nozzle installed → certificate void; the O3 loop becomes
  the formulation.

### FORK-7 — Closure for subsonic-axial patches on Γ_d
- **Q**: Where axial flow is subsonic, complete data over-determines
  the state; which closure is declared?
- **Options**: O1 characteristic-based: impose incoming Riemann
  invariants from data, let the outgoing one float (locally
  one-dimensional characteristic BC, Poinsot–Lele/Thompson style
  generalized to steady Euler). O2 stagnation-state + flow-angle
  closure (classical subsonic-inlet BC: p0(ξ), T0(ξ), angles from
  data; static pressure floats) — turbomachinery standard. O3
  mass-flux pinned closure (fix ρu from data; thermodynamic state
  floats). O4 impedance closure (couple to a declared upstream
  acoustic model — pairs naturally with FORK-6 O2.
- **Decision criterion**: which floated quantity the DATA measure
  worst (assign the free variable to the largest measurement bar), and
  well-posedness of the per-phase steady problem (characteristic
  counting must be exact — one incoming invariant subsonic-out, four
  pinned... sign conventions per local normal Mach).
- **Recommendation**: O2. Grounds: p0/T0/angle are the quantities a
  combustor model or rig measures most robustly (Kiel/impact probes
  survive unsteadiness better in mean; total quantities are the
  physically transported invariants along particle paths in the
  frozen model); characteristic counting is textbook-clean; it also
  matches how the causal-separation impedance band (FORK-6 O2) is
  phrased.
- **Falsifier**: per-phase solves show closure-choice sensitivity of J
  above the (v) discretization bar (swap O2↔O1 on a sample of phases;
  if ΔJ exceeds bar, the subsonic-patch closure is a live model term
  and must enter the (v) budget explicitly, not implicitly).

### FORK-8 — Dimensional fidelity of s(ξ): full radial profiles + swirl vs reduced data
- **Q**: Is s(ξ) a full field on Γ_d (radial profiles of P, T, M,
  both flow angles) or a reduced representation?
- **Options**: O1 full radial×phase table (the honest contract; the
  annulus is stratified: center-body wake, wall films). O2
  radial-averaged per phase (mixed-out per phase — mass/momentum/
  energy-consistent, Cumpsty–Horlock; loses radial work of the
  contour against stratification, e.g., plug designs feed off the
  inner-radius state). O3 modal reduction (POD/few radial modes ×
  Fourier in phase) — compresses with measured truncation error. O4
  parametric analytic profile family fitted to data (fast, but bias).
- **Decision criterion**: evaluate thrust-sensitivity of a
  representative nozzle to radial moments of the inflow (adjoint gives
  this): if sensitivity × measured stratification > (v) bar, O1/O3
  required.
- **Recommendation**: O1 as the contract of record, O3 as the
  computational carrier with stated truncation error. Grounds: plug
  and E-D sectors specifically exploit the inner/outer radius states
  differently (FORK-18); collapsing radius biases the TOPOLOGY
  decision, which is the least reversible decision in the program.
- **Falsifier**: sector winner flips between O1 and O2 data on the
  same optimizer settings → any certificate issued on O2-grade data is
  void for topology claims.

### FORK-9 — Swirl accounting (azimuthal momentum in an axisymmetric design)
- **Q**: Single-direction rotating waves leave net swirl at Γ_d. Keep
  u_θ in the state or neglect it?
- **Options**: O1 axisymmetric-with-swirl Euler per phase (still a 2D
  meridional problem; u_θ advected with radial-equilibrium coupling
  — standard). O2 neglect swirl, book a loss estimate. O3 treat swirl
  as recoverable via the contour (FALSE for axisymmetric inviscid
  walls — see DP-4; listed to be rejected for stated reason). O4 add
  de-swirl vanes = non-axisymmetric solid — OUTSIDE the brief's
  symmetry class; rejected as out-of-scope but NAMED (it is the only
  physical mechanism that converts swirl to thrust; its absence is a
  bound on B, FORK-28).
- **Decision criterion**: DP-4 + measured swirl magnitude. Swirl angle
  α at Γ_d: axial-kinetic-energy fraction lost ≈ tan²α; published RDE
  simulations put mean exit swirl angles up to ~10–20° pre-nozzle
  (Schwer & Kailasanath; Braun et al.) → tan²(15°) ≈ 7% — far above
  any credible δ.
- **Recommendation**: O1, mandatory. Grounds: swirl is not a
  correction, it is a first-order term in both thrust bookkeeping and
  radial equilibrium (it changes wall pressure distributions and hence
  the OPTIMAL CONTOUR, not just the objective value); it also alters
  the separation margin (swirl stabilizes/destabilizes the adverse
  pressure gradient response of the near-wall flow).
- **Falsifier**: data show μ-mean swirl angle below the angle whose
  tan² is under the (v) bar AND per-phase swirl excursions similarly
  small → O2 becomes admissible with the booked estimate.

**DP-4 (dry proof — swirl irrecoverability under axisymmetry).** On an
axisymmetric solid with inviscid slip, the surface normal has no e_θ
component, so pressure exerts zero torque about the axis; body forces
absent ⇒ the flux of angular momentum ∫ρ r u_θ (u·n) dA is conserved
between Γ_d and exit. With mass flow fixed, exit u_θ r-distribution
cannot be annihilated by any admissible S; the associated kinetic
energy ½u_θ² is unavailable for axial acceleration (energy budget:
h0 fixed, axial KE ≤ total KE − swirl KE). Hence swirl enters the
availability upper bound B (FORK-28) as a strict debit. ∎

### FORK-10 — Phase discretization: quadrature over Ξ
- **Q**: How many/which phases, and what quadrature on μ?
- **Options**: O1 uniform-in-cycle-time trapezoid (spectrally accurate
  for smooth periodic integrands). O2 adapted quadrature clustered at
  the front passage (the integrand has near-discontinuous phase
  dependence at the detonation/oblique-shock passage: uniform rules
  lose orders). O3 split-measure: front-passage impulsive contribution
  integrated separately (measure decomposition μ = μ_smooth + μ_front)
  — pairs with DP-3's impulsive term. O4 sparse/Gauss rules on a
  smooth reparametrization of the cycle. O5 Monte-Carlo/QMC on μ (only
  if μ becomes empirical-noisy; otherwise wasteful).
- **Decision criterion**: measured regularity of ξ ↦ F[S; s(ξ)] on a
  probe design: spectral decay ⇒ O1; localized kinks ⇒ O3.
- **Recommendation**: O3 with O1 on the smooth part. Grounds: cycle
  data from a detonation ARE kinked; pretending otherwise puts an
  uncontrolled O(Δξ^1) error inside a program that promises derived
  tolerances.
- **Falsifier**: quadrature-refinement study shows the split is
  unnecessary (observed order ≥ 2 without it) → simplify to O1
  (record the study as the tolerance derivation).

### FORK-11 — H-DATA violation monitor (mode detection as part of the design)
- **Q**: What detects "not a single-mode rotating wave" in data/rig?
- **Options**: O1 azimuthal transducer array + cross-spectral phase
  fit (wave count n and direction from inter-sensor phase slopes —
  standard RDE diagnostics, Bennewitz et al. 2019 mode-identification
  methodology). O2 time-frequency spectrogram criteria (mode hops =
  frequency ladder jumps). O3 wave-frame residual monitor: transform
  candidate data to the fitted wave frame; residual unsteadiness norm
  above threshold = violation (directly tests the DP-2 hypothesis, not
  a proxy). O4 surrogate-based novelty detection on s(ξ) (ML outlier
  flag; useful as tripwire, uncertifiable alone).
- **Decision criterion**: the monitor must test the hypothesis the
  CERTIFICATE consumes — which is wave-frame steadiness, not merely
  "one dominant frequency".
- **Recommendation**: O3 primary (it is the exact hypothesis), O1 as
  the cheap online tripwire. Falsifier for the monitor itself: inject
  synthetic two-mode data at small secondary amplitude; monitor must
  fire before the (v) bound degrades by its own tolerance (rejector
  calibration).

---

## 4. FAMILY C — STATE MODEL AND SOLUTION CONCEPT

### FORK-12 — Per-phase solution class: smooth / fitted fronts / captured weak
- **Q**: In what class do per-phase steady Euler solutions live, and
  how is membership certified?
- **Options at their best**:
  - O1 *Shock-free smooth class via MoC* (thermally-perfect MoC is
    classical: Zucrow & Hoffman Vol. II): valid in fully supersonic
    subdomains; membership certified by construction (characteristics
    do not cross); the historical thrust-optimum machinery
    (Guderley–Hantsche 1955; Rao 1958; Shmyglevsky/Kraiko school)
    lives here.
  - O2 *Piecewise-smooth with FITTED discontinuities*: oblique shocks
    /slip lines as explicit unknowns with Rankine–Hugoniot enforced;
    the only class where shock sensitivities are clean (Giles &
    Pierce 2001 adjoint-at-shock analysis).
  - O3 *Captured weak solutions* (FV/DG with limiters): robust for
    arbitrary topology; membership certified only by convergence
    studies; sensitivities polluted by smeared shocks (spurious
    adjoint oscillations; known pathology).
  - O4 *Weak-class agnostic with entropy-measure certificates*
    (a-posteriori entropy-production bounds): honest but immature for
    certification-grade claims in 2D axisymmetric+swirl.
- **Decision criterion**: does the per-phase flow at candidate optima
  actually contain embedded shocks? (TOP-style contours generate
  internal shocks by design intent; truncated plugs generate lip
  shocks and recompressions.) If yes anywhere in the search region, O1
  alone is inadmissible.
- **Recommendation**: O2 as the certificate class, O3 as the
  exploration/fallback solver, O1 inside proven-supersonic-smooth
  patches (it is faster and its optimality theory is the classical
  backbone). Non-uniqueness handling: restrict certificates to the
  piecewise-smooth class with entropy-admissible fronts and declared
  front topology; treat topology changes as certification-boundary
  events (FORK-33). The wild non-uniqueness of multi-D weak Euler
  solutions (De Lellis–Székelyhidi) is fenced out BY CLASS FIAT,
  declared openly: certificates are class-relative.
- **Falsifier**: a captured-solver solution at a certified design
  shows a front topology absent from the fitted model (e.g., a Mach
  disk the fitted class did not admit) → class membership claim fails;
  design exits the certified set.

### FORK-13 — Sonic region treatment (per phase)
- **Q**: The per-phase problem may contain transonic patches (subsonic
  pockets behind the wave phase); how is the sonic surface handled?
- **Options**: O1 assume supersonic-everywhere per phase (verify on
  data; if true, pure MoC). O2 transonic solver with sonic-surface
  as internal free boundary (classical throat transonics:
  Sauer/Hall expansions for nozzle throats; valid for smooth
  accelerating patches). O3 full subsonic-supersonic FV solve per
  phase (no structural assumption; ties to O3 of FORK-12). O4
  hodograph/characteristic hybrid (elegant, brittle, rejected for
  fragility under data-driven inflow: hodograph methods require
  special boundary structure).
- **Decision criterion**: per-phase axial Mach maps from the data
  (FORK-6 O1 check produces exactly this).
- **Recommendation**: O2 where pockets are localized and smooth, O3
  otherwise; never silently O1. Grounds: the low-axial-Mach phase
  right behind the wave is precisely the thrust-poor,
  separation-prone phase — mis-modelling it biases both J and the
  binding constraint.
- **Falsifier**: O2/O3 disagreement on pocket extent above
  discretization bar → O2's expansion hypotheses void; O3 becomes
  the class for those phases.

### FORK-14 — Gas model: frozen thermally-perfect γ(T) — where it matters, where it fails
- **Q**: Consequences and audit of the pinned gas model.
- **Options (as audit layers, since the pin is given)**:
  - O1 accept pin; implement h(T), cp(T) via NASA-9 polynomials /
    tables; MoC and FV both handle thermally-perfect cleanly (Zucrow &
    Hoffman). γ swings ~1.14→1.30 across a detonation-product
    expansion — a calorically-perfect γ would misplace the throat
    characteristic net, area ratios, and P–M angles by design-relevant
    amounts (several % in exit pressure): the pin against γ=const is
    physically right.
  - O2 bracket runs: frozen vs shifting-equilibrium end-members
    (CEA-style). Classical result: frozen underpredicts, equilibrium
    overpredicts performance; the truth (finite-rate recombination,
    H+OH→H2O, CO+O→CO2 for H2/C-H2 detonation products at T0 ~
    2800–3500 K) lies between (Bray sudden-freezing analysis 1959).
    The bracket width IS the model-form error carrier for (v).
  - O3 finite-rate 1D audit along representative streamtubes
    (recombination Damköhler along the expansion): locates WHERE
    freezing actually occurs; if the freeze point is inside the
    nozzle, the frozen-from-Γ_d pin misbooks a recoverable enthalpy
    share.
  - O4 condensed-phase / two-phase audit — out of scope by pin
    (single phase); named because metallized or rich-hydrocarbon
    products would break it; monitor = product composition.
- **Decision criterion**: bracket width (O2) and freeze-point location
  (O3) vs δ and the (v) budget.
- **Recommendation**: O1 + O2 mandatory, O3 once per engine class.
  Grounds: for stoichiometric H2–air detonation products the
  frozen/equilibrium Isp spread through a large-ratio expansion is
  a few percent — likely LARGER than any claimed δ; a certificate
  that does not carry the bracket as a named model-form bar is
  physically hollow even if mathematically tight.
- **Falsifier**: O3 shows recombination heat release comparable to the
  (v) bar inside the nozzle → frozen pin's declared-absence claim for
  reaction residuals is false; model layer must be added or bars
  widened.

### FORK-15 — Viscous layer and the separation criterion
- **Q**: Euler core + what viscous accounting; which detachment
  criterion instantiates g_sep?
- **Options at their best**:
  - O1 *Pure Euler + empirical wall-pressure-ratio criteria*:
    Summerfield (p_w/Pa ≈ 0.35–0.4), Schmucker, Stark's criterion
    (p_w/Pa ≈ 1/(1.88·M_w − 1), validated over cold/hot subscale data,
    Stark & Wagner 2009). Cheap, differentiable, calibrated on
    steady bell nozzles.
  - O2 *Integral boundary-layer coupled* (compressible integral BL
    with displacement feedback; incipient separation at H_k or
    equivalent shape-factor threshold — Stratford-type criteria
    generalized; Drela-style viscous-inviscid coupling): predictive
    rather than correlational, still cheap, differentiable, sensitive
    to the ACTUAL wall pressure gradient the optimizer creates
    (correlations extrapolate badly to novel contours — the exact risk
    in a shape-optimization loop).
  - O3 *RANS audit tier* (SA/SST) at incumbents: not in-loop;
    validates O2 fields, catches shock-induced separation
    (FSS/RSS distinction, Frey & Hagemann 2000) that pressure-ratio
    correlations miss on TOP-like contours with internal shocks.
  - O4 *Unsteady separation physics audit*: under periodic forcing at
    marginal St, separation onset exhibits hysteresis/lag relative to
    quasi-steady criteria (dynamic-stall analogy; low-frequency
    breathing of separation documented in nozzle flows, Olson & Lele
    2013): a quasi-steady μ-a.e. margin can be either conservative or
    anticonservative — measured, not assumed.
- **Decision criterion**: O2 vs O3 agreement on incumbent designs
  (field-level, not verdict-level); O4 dedicated URANS study fixes the
  sign of the unsteady correction to the margin.
- **Recommendation**: O2 in-loop as g_sep carrier (with derived margin
  from its own validation scatter vs O3), O1 retained only as a
  tripwire cross-check, O3 at every incumbent, O4 once to set the
  margin's unsteadiness safety term. Grounds: an optimizer WILL find
  the contours where a correlation lies; the constraint must be built
  from local physics it cannot game.
- **Falsifier**: O3 finds separation (or RSS) on a design O2 certifies
  attached, beyond O2's declared scatter → g_sep carrier rejected;
  loop must ingest O3-grade physics (cost re-plan).

### FORK-16 — Aggregation of the per-phase attachment constraint
- **Q**: g_sep(S; s(ξ)) ≤ 0 for μ-a.e. ξ is semi-infinite; how is it
  imposed?
- **Options**: O1 worst-case discrete (max over quadrature phases;
  nonsmooth). O2 KS/p-norm smooth aggregation (Kreisselmeier–
  Steinhauser; standard in aerostructural practice; conservative side
  controllable). O3 exact semi-infinite programming (local reduction /
  adaptive phase-grid refinement at active phases — Hettich & 
  Kortanek 1993). O4 chance-constrained (rejected here: separation is
  a cliff — see FORK-4). O5 phase-augmented state: track the
  argmax-phase as an unknown with complementarity (MPCC) — sharp but
  fragile.
- **Decision criterion**: number and mobility of active phases along
  the optimization path (measured); KS conservatism vs δ.
- **Recommendation**: O2 in-loop + O3-style adaptive phase refinement
  near convergence so the certificate is issued against the TRUE
  semi-infinite constraint, not the smoothed one. Falsifier: post-hoc
  fine-phase sweep finds a violating phase between quadrature nodes →
  certificate void; refine and re-issue (this sweep is a mandatory
  certificate step).

---

## 5. FAMILY D — CONFIGURATION AND GEOMETRY (the topology question)

### FORK-17 — Topology treatment: emergent vs enumerated sectors
- **Q**: Brief says configurations are OUTPUTS (topology sectors of
  S). How is the sector space actually searched?
- **Options at their best**:
  - O1 *Free topology optimization*: level-set (Allaire, Jouve,
    Toader 2004; Osher–Sethian) or density/SIMP-like with flow
    penalization (Borrvall–Petersson lineage) over Ω(S). Genuinely
    topology-agnostic; but density methods are alien to supersonic
    Euler with slip walls (no honest porous-medium relaxation of a
    slip BC at M>1), and level-set with Euler+shocks+adjoint is
    research-grade, not certificate-grade.
  - O2 *Enumerated sector optimization*: optimize within each named
    sector (bell; full plug; truncated plug; shrouded plug/E-D;
    annular-bell) with sector-appropriate parametrization, then
    compare champions with matched certificates. Complete for
    axisymmetric single-passage nozzles IF the enumeration is complete
    — and for compact axisymmetric solids attached on Λ the sector
    list is finite and classical (the topology of Ω(S) is set by the
    number of solid components and their attachment: center-plug
    present/absent, shroud present/absent...).
  - O3 *Hybrid*: coarse free-topology exploration (O1 at low fidelity,
    or FF-5 global search over a topology-capable parametrization) to
    HUNT for unenumerated sectors; certificates only via O2 within the
    winning sector(s).
  - O4 *Graph/skeleton parametrization* (medial-axis representation of
    S; topology changes = discrete graph moves inside a GA/BO outer
    loop): the most credible "non-classical" carrier of topology moves
    for this problem.
- **Decision criterion**: is there a plausible sector OUTSIDE the
  classical list for an axisymmetric attached compact solid under a
  cone condition? Enumerate by attachment count and connectivity: the
  cone condition + compactness + Λ-attachment cap the count at low
  numbers; a short combinatorial lemma can make O2's enumeration
  PROVABLY complete up to a component bound — that lemma is worth
  writing (it converts "topology as output" into a finite certified
  disjunction).
- **Recommendation**: O2 with the enumeration-completeness lemma +
  O3-style low-fidelity hunt as insurance. Grounds: certificates
  (ii)–(iv) are sector-local anyway (the admissible set is
  disconnected across sectors: no continuous admissible path removes
  a shroud); globality (iv) is then a finite max over sector
  champions, each with its own δ — clean.
- **Falsifier**: the O3 hunt finds a design outside every enumerated
  sector beating a champion by more than its δ → enumeration lemma's
  component bound was wrong; redo with raised bound.

### FORK-18 — Configuration physics: who should win under cycle-varying inflow, and why
- **Q**: Physical priors on bell vs plug vs shrouded plug vs E-D for
  RDE exhaust — needed to seed sector search and sanity-check the
  optimizer.
- **Options (each at its best)**:
  - O1 *Bell (TIC/TOP)*: maximum internal-expansion efficiency at a
    single design pressure ratio; shortest path to the classical
    thrust-optimum theory (Rao 1958; truncated ideal contours,
    Ahlberg et al.; modern practice Hagemann et al. 1998 review).
    Weakness here: the CYCLE sweeps the effective per-phase pressure
    ratio and inflow angle over a wide band; a fixed bell is
    single-point machinery facing a distribution.
  - O2 *Full/truncated plug (aerospike)*: external expansion
    self-adjusts to instantaneous pressure ratio — the classical
    ALTITUDE-compensation argument (Angelino 1964; Hagemann et al.)
    transposes to CYCLE compensation: with Pa fixed but the per-phase
    jet state swinging, the free outer boundary re-forms the expansion
    fan phase-by-phase instead of forcing a fixed-wall mismatch
    (overexpansion shocks / underexpansion losses alternating over the
    cycle in a bell). This is a genuinely load-bearing physical
    argument FOR plug-type sectors in RDE service, and it is why
    experimental RDE work gravitated to aerospikes (Fotia et al.
    AFRL tests; Harroun & Heister RDRE aerospike studies).
    Weaknesses: swirl interacts with the plug's radial pressure
    balance; truncation demands a base-pressure model (FORK-20);
    plug surface sees the harshest per-phase heat/pressure spikes.
  - O3 *Shrouded plug / expansion-deflection*: internal-external
    compromise; E-D keeps envelope short at high area ratio; base/
    pintle wake physics (open/closed wake regimes) adds a second
    uncertifiable-by-Euler zone; historically loses to bell at fixed
    Pa unless envelope-bound binds (Conley/Aerojet E-D studies).
  - O4 *Annular bell without centerbody* (direct annular-to-round
    transition duct + bell): the "do nothing clever" baseline; its
    losses (dump/transition mixing of the annular jet) are the
    reference the others must beat.
- **Decision criterion**: sector champions under IDENTICAL data,
  constraints and certificates (FORK-17); the per-phase compensation
  argument predicts the plug's margin GROWS with cycle pressure-ratio
  swing amplitude — a testable monotonicity.
- **Recommendation**: seed the search with O2 and O1 both at full
  effort; treat O3 as envelope-bound-triggered; keep O4 as the
  mandatory baseline. Grounds: DP-6 (below) plus the experimental
  record.
- **Falsifier**: sector comparison at matched certificates shows the
  bell champion within δ of the plug champion at the measured cycle
  swing → the compensation argument is not load-bearing for this
  engine class; drop the plug-first prior (and say so).

**DP-6 (dry sketch — cycle-compensation inequality).** For a fixed
bell, per-phase mismatch loss ≈ k·(p_e(ξ) − Pa)²-type penalty
(quadratic near match by expanding the thrust coefficient about
p_e = Pa at fixed contour); averaging over a cycle with swing σ²
books a loss ∝ σ². An ideal external-expansion surface re-attains
near-matched expansion each phase (loss ∝ σ² but with a much smaller
constant, bounded by fan re-adjustment residuals at marginal St plus
truncation/base debits). Hence there exists a swing amplitude σ*
above which plug-sector champions dominate bell champions, provided
base+viscous debits are sub-σ² — σ* is COMPUTABLE from the data and
cheap models before any optimization. Hypotheses: quasi-steady fan
adjustment (St-limited: the fan re-forms on an acoustic timescale
~R/a, faster than the cycle by construction of St marginal — must be
checked), attached flow both sectors. ∎

### FORK-19 — Contour parametrization within a sector
- **Q**: Function class for ∂S: what does the optimizer actually move?
- **Options at their best**:
  - O1 *MoC-native families*: Rao/thrust-optimized contours
    parametrized by their control-theory data (throat expansion angle,
    exit angle, length; per-phase generalization: solve the averaged
    control problem directly — the Rao method IS an optimality system,
    not a parametrization, and generalizes to averaged objectives).
  - O2 *B-splines/Bézier on the meridional wall* (industry standard;
    smoothness by construction; cone/curvature constraints are linear
    or SOC-representable in control points — clean for (iii)/(iv)).
  - O3 *CST (Kulfan)*: compact, global support (good conditioning,
    poor localization).
  - O4 *Free-node polyline + regularization*: maximal freedom, needs
    explicit curvature/cone constraint machinery; risk of optimizer-
    driven oscillation (the classical "sawtooth wall" pathology —
    exactly what the uniform cone condition exists to kill).
  - O5 *Level-set / implicit* (topology-capable; pairs with FORK-17
    O1/O3 only).
  - O6 *FFD volumes* (overkill for axisymmetric meridional curves;
    rejected: adds parameters without adding expressible shapes).
  - O7 *PARSEC-style engineering parametrizations* (interpretable,
    too rigid for optimal-contour fine structure near the throat).
- **Decision criterion**: (a) can the class express the known optimal
  structures (throat curvature discontinuity at the attachment of the
  expansion; TIC/TOP-type downstream behavior; plug lip Prandtl–Meyer
  anchoring)? (b) do the admissibility constraints (cone (h0, ω),
  curvature, angle bounds) become certifiable constraints on the
  parameters? (c) mesh-independence of the OPTIMUM as the class is
  enriched (parametrization-refinement study — mandatory).
- **Recommendation**: O2 as the certificate-class (with knot-
  refinement studies as the enrichment ladder), O1 as the analytic
  spine to (ii)'s stationarity conditions (the averaged Rao system is
  what (ii) should REPRODUCE in the smooth supersonic case — a
  powerful cross-check: single-phase limit must recover Rao's
  control-surface conditions exactly), O5 confined to the topology
  hunt.
- **Falsifier**: enrichment study shows J still climbing at the
  richest affordable knot set with the gradient not collapsing →
  class is expressively binding; the certificate's δ must absorb the
  measured parametrization gap or the class is upgraded.

### FORK-20 — Plug truncation and base pressure (the Euler-uncertifiable zone)
- **Q**: Truncated-plug sectors introduce a base region whose pressure
  is set by viscous wake dynamics. Euler cannot certify it. What is
  the handle?
- **Options**: O1 full-length (untruncated) spike only — stays inside
  Euler-certifiable class; cost: length/mass constraints likely bind,
  and the sharp tip violates cone condition (h0, ω) unless the class
  is opened — check: a cone condition with small h0 admits
  near-sharp tips; the interplay is a real constraint-design item.
  O2 truncate + declared base-pressure model layer (open/closed wake
  correlation ladder: p_b correlations from Angelino-era and modern
  aerospike test data, e.g., Rommel/Hagemann plug studies, Tomita et
  al.; carried as a NAMED model residual in (v) with its validation
  scatter as the bar). O3 truncate + base bleed as a design variable
  (secondary flow smooths base pressure; adds a mass-flow debit and a
  new model layer). O4 RANS-anchored base model (surrogate for p_b
  trained on a RANS DOE over truncation fraction and NPR; the modern
  practice; verification tier explicit).
- **Decision criterion**: sensitivity dJ/dp_b × base area vs (v)
  budget; if base thrust share is material (it is, at 20–40%
  truncation: order 1–3% of thrust), the base model's validation
  scatter directly caps the certifiable δ.
- **Recommendation**: O2 with O4-grade calibration for the champion,
  and O1 evaluated whenever constraints admit it (the certificate is
  cleanest there). Grounds: pretending Euler covers the base is the
  one place this program could ship a certified number that a thrust
  stand would flatly contradict.
- **Falsifier**: RANS/experiment base pressure outside the correlation
  band used → base layer's declared bar was wrong; certificates for
  truncated champions void pending recalibration.

### FORK-21 — Lip and attachment treatment on Λ
- **Q**: Physics and representation of the chamber-lip anchoring
  (sharp lip fixes the expansion-fan origin; per-phase incoming flow
  angle swings move the fan structure).
- **Options**: O1 sharp lip as a fixed singular point with per-phase
  Prandtl–Meyer fan (thermally-perfect P–M function — γ(T) version,
  computed by integrating the characteristic ODE, not the γ-const
  closed form); O2 rounded lip within curvature bounds (regularizes
  the corner singularity for the adjoint; slightly de-optimizes
  expansion initiation); O3 lip as design-active (position on Λ set(s)
  if Λ has freedom). 
- **Decision criterion**: adjoint regularity at the corner (corner
  singularity strength enters gradient accuracy) vs the thrust cost
  of rounding (classically small: lip radii ≪ throat radius cost
  ~0.1% class).
- **Recommendation**: O2 with radius at the curvature-bound floor:
  buys certifiable adjoint regularity for negligible thrust. 
- **Falsifier**: rounding-radius sweep shows thrust sensitivity above
  the claimed class → corner physics is design-active for this data
  (strong per-phase angle swings can do this); revert to O1 with a
  corner-aware adjoint treatment.

---

## 6. FAMILY E — THRUST BOOKKEEPING

### FORK-22 — Control surface, ambient term, and what counts as nozzle thrust
- **Q**: Which control volume defines F, and is the (p−Pa) bookkeeping
  invariant to the choice?
- **Options**: O1 wetted-surface integral (thrust = ∫(p−Pa)n_x dA over
  all wetted solid + base surfaces; the "what the structure feels"
  definition). O2 exit-plane/far-field flux form (momentum theorem
  form as in the brief's F_S). O3 impulse-function bookkeeping at Γ_d
  plus wall contribution (splits combustor-delivered impulse from
  nozzle augmentation: the right way to report NOZZLE merit ΔF vs the
  O4 baseline of FORK-18). O4 far-field enclosing surface including
  entrained ambient (relevant only with external flow; here ambient
  is quiescent by the problem statement).
- **Decision criterion / dry proof DP-1**: for EXACTLY time-periodic
  flow, average the momentum balance over one period on the volume
  between any two enclosing surfaces: the stored-momentum term
  (1/τ)∫d/dt(∫ρu_x dV)dt telescopes to zero exactly. Hence the
  TIME-AVERAGED F is control-surface independent — bookkeeping
  invariance is a THEOREM under H-DATA, needing no St smallness. ∎
  (Instantaneous F is NOT surface-independent; any claim about
  peak/instantaneous thrust must name its surface.)
- **Recommendation**: O2 for the objective (matches the brief), O1
  computed ALWAYS as the redundancy check (equality within
  discretization bar = a free integral-identity rejector on every
  solve), O3 for reporting nozzle merit. Grounds: DP-1 makes the
  choice safe; the O1≡O2 check is the cheapest strong audit in the
  whole program.
- **Falsifier**: O1 vs O2 gap above the derived discretization bar on
  any accepted solve → that solve's certificate is void (this is a
  per-solve rejector, not a one-time study).

### FORK-23 — Phases outside the certified class inside the average
- **Q**: J integrates F over ALL phases; what if some phase ξ fails
  certification (separated, unstarted, ambiguous front topology) at a
  candidate S?
- **Options**: O1 hard class-exit (design leaves certified set the
  moment any μ-positive phase fails — matches the brief's separation
  clause read strictly). O2 phase-measure tolerance (allow failures on
  μ-measure ≤ ε with F bounded by a declared pessimistic model on the
  failed set; ε enters δ). O3 penalty/barrier shaping in the optimizer
  ONLY (certificate still O1; the barrier is a navigation device, not
  a claim). O4 constraint-aggregated feasibility restoration
  (filter-SQP style: feasibility restored before optimality claimed).
- **Decision criterion**: the brief's own language ("designs that
  separate exit the certified class") fixes the CLAIM level at O1; the
  fork is really about the SEARCH mechanics.
- **Recommendation**: O1 claims + O3 mechanics + O4 restoration.
  Falsifier: optimizer converges ON the class boundary with active
  barrier (margin → 0 at optimum): then the certificate must include
  the boundary-activity statement and the margin's own error bar —
  a boundary optimum with margin bar straddling zero is NOT
  certifiable; report as such.

---

## 7. FAMILY F — OPTIMALITY MACHINERY

### FORK-24 — Optimize-then-discretize vs discretize-then-optimize
- **Q**: Which order, given embedded fronts and an averaged objective?
- **Options**: O1 OTD (continuous adjoint + shape calculus; Hadamard
  form gives wall-normal gradient density; clean stationarity
  structure for (ii), including the averaged-wall condition; risk:
  discrete inconsistency — computed gradient is not the gradient of
  the computed J). O2 DTO (discrete adjoint/AD; gradient exact for
  the discrete J; risk: at captured shocks the discrete adjoint
  converges to wrong continuous sensitivities (Giles–Pierce), and
  limiter nondifferentiability injects noise). O3 dual-consistent
  discretizations (SBP-SAT / dual-consistent DG: both orders agree in
  the limit; the modern resolution). O4 fitted-front OTD (shock
  position as explicit unknown with its own adjoint jump conditions —
  the only regime where shock sensitivities are POINTWISE clean).
- **Decision criterion**: presence of captured fronts in the
  certificate class (FORK-12 chose fitted for certificates → O4
  aligns); demand the standard three-way gradient audit (continuous
  vs discrete vs FD/complex-step) to close below a derived bar.
- **Recommendation**: O4/O1 on the fitted certificate class + O2 on
  the captured exploration solver, with O3-grade dual consistency
  wherever FV/DG is used near certificates. The (ii) deliverable
  (averaged stationarity system: per-phase adjoints, SHARED-contour
  averaged wall condition Σ-form, transversality at endpoints,
  multiplier meaning) is an OTD object — derive it continuously,
  then verify discretely.
- **Falsifier**: three-way gradient audit fails to close at the
  derived bar on refined meshes → the active order is rejected on
  that solver; certificates suspended until closed.

### FORK-25 — Derivative computation and its verification
- **Q**: Adjoint/AD/FD/complex-step — which, and how verified?
- **Options**: O1 hand-derived continuous adjoint (+ shape
  derivative); O2 discrete adjoint by reverse AD (dominant modern
  practice; memory managed by checkpointing); O3 tangent/forward AD
  (cheap for few parameters — sector studies with O(10) parameters
  sit exactly here); O4 finite differences (verification only —
  step-size dilemma disqualifies it as primary); O5 complex-step
  (machine-precision directional derivatives, no subtraction error —
  the verification gold standard where the solver is complexifiable);
  O6 hyperdual/second-order AD for (iii) Hessian-vector products.
- **Decision criterion**: parameter count per sector (O3 vs O2
  crossover), solver complexifiability (O5 feasibility), and the
  mandatory closure audit of FORK-24.
- **Recommendation**: O2 primary + O5 verification on unit problems +
  O4 sanity on the full J + O6 for reduced-Hessian actions. Every
  gradient used in a certificate carries a closure record
  (dot-product test / adjoint-consistency residual) — the adjoint
  identity ⟨λ, R_u v⟩ = ⟨J_u, v⟩ tested to a derived tolerance is a
  per-build rejector.
- **Falsifier**: dot-product test drift beyond bar after any solver
  change → gradients quarantined; certificates depending on them
  suspended (the test is cheap; run it in CI-fashion).

### FORK-26 — Structure of the averaged stationarity system (the (ii) deliverable)
- **Q**: What form must first-order conditions take for a SHARED
  contour maximizing a μ-average with per-phase PDE constraints?
- **Options / structure (this is less a choice than a derivation with
  choice points)**: O1 per-phase adjoint λ_ξ each solving the steady
  Euler adjoint with thrust right-hand side; wall condition: the
  AVERAGED shape-gradient density vanishes — ∫_Ξ G(x; ξ) dμ = 0 on
  the free contour, with G the per-phase Hadamard density (pressure-
  adjoint boundary combination). The single-phase limit MUST collapse
  to the classical Rao control-surface conditions (mass-flow/Mach
  angle relations along the control characteristic) — a hard
  regression anchor. O2 endpoint/transversality: free exit-lip
  position ⇒ averaged transversality (the Rao exit-angle condition in
  μ-mean); length/envelope constraints active ⇒ complementarity with
  multipliers = marginal thrust per unit constraint (report them: they
  are the trade-study currency the program owes the engineer). O3
  state-constraint (attachment) multipliers: measure-valued on the
  active phase-set (semi-infinite KKT — Hettich–Kortanek); the
  certificate must state the active set and its multiplier measure.
  O4 nonsmooth phases (front-passage kink in ξ): Clarke/measure
  decomposition of the μ-integral consistent with FORK-10's split.
- **Decision criterion**: internal-consistency anchors: (a) Rao limit;
  (b) multiplier sign/meaning checks (marginal values verified by
  finite constraint perturbation runs); (c) symmetry checks (data
  symmetries must reflect into G).
- **Recommendation**: derive O1–O4 in full as the (ii) artifact; the
  Rao-limit regression and the marginal-value multiplier audit are
  its two falsifiers, both cheap.
- **Falsifier**: single-phase reduction disagrees with Rao/TIC theory
  on a textbook case (γ const, uniform inflow) → the averaged
  optimality derivation is wrong somewhere upstream; nothing built on
  (ii) stands until fixed.

### FORK-27 — Optimizer class and globalization (search mechanics)
- **Q**: What actually moves the design, and how is stagnation vs
  convergence adjudicated?
- **Options at their best**:
  - O1 SQP/interior-point with trust region on the smooth
    parametrized problem (SNOPT/IPOPT-class; the certificate-grade
    local machinery; handles the KS-aggregated constraints and box/
    SOC-representable admissibility cleanly).
  - O2 Trust-region with adaptive-fidelity models (per-phase mesh /
    quadrature fidelity managed by TR ratio tests — first-order
    consistent multifidelity: Alexandrov et al.; natural fit to the
    expensive-average structure).
  - O3 CMA-ES / evolutionary / GA (NSGA-II for constraint-trade
    exploration): derivative-free global probes; immune to gradient
    pollution; certificate-blind. Right role: sector-level seeding and
    parametrization-basin discovery, never the closer.
  - O4 Bayesian optimization / EGO with GP surrogates on sector
    parameter spaces (Jones 1998; constrained EI variants): the
    correct tool for the EXPENSIVE wave-frame-anchored evaluations
    (FF-2) at low parameter counts; provides its own (statistical,
    not certified) global gap estimate.
  - O5 DOE + polynomial/Kriging response surfaces (classical industry
    campaigns): superseded by O4 in sample efficiency; retained for
    screening and sensitivity ranking (Morris/Sobol) to fix
    parametrization dimension.
  - O6 ML-surrogate-in-the-loop (NN surrogate of per-phase solves with
    verification tier): admissible ONLY as a proposal generator; every
    surrogate-proposed step re-evaluated by the true solver before
    acceptance (surrogate error otherwise enters the certificate
    unbounded).
  - O7 Multistart + basin bookkeeping over O1 (deterministic global
    layer with measured basin coverage).
- **Decision criterion**: role assignment by certificate obligation:
  anything touching (ii)–(iv) must end in O1/O2 convergence with KKT
  residuals below DERIVED tolerance; global layers (O3/O4/O7) are
  judged by coverage-per-cost measurements, not preference.
- **Recommendation**: O2 (with O1 inner) as the closer; O4 across
  sector parameter spaces; O3 only if multimodality is DEMONSTRATED
  (basin study), O5 for initial screening, O6 excluded from the
  certified path. 
- **Falsifier**: multistart/BO finds a basin whose champion beats the
  incumbent by > δ → the globality mechanism (FORK-28), not just the
  optimizer, failed; both must be revisited.

### FORK-28 — The globality certificate: how δ is actually COMPUTED
- **Q**: Requirement (iv): J[S*] ≥ sup J − δ with δ computed. By what
  mechanism?
- **Options at their best**:
  - O1 *Physical availability upper bound B* (the propulsion-native
    mechanism): for each phase, the thrust deliverable through ANY
    exit is bounded by expanding the Γ_d-delivered mass/enthalpy flux
    isentropically (frozen gas) to the best admissible exit state:
    axial momentum ≤ total momentum (swirl debit per DP-4 subtracted
    as a theorem, not an estimate), exit static pressure ≥ the
    admissible-envelope area-bound Prandtl–Meyer limit, wall pressure
    ≤ stagnation. Average the per-phase bounds over μ: δ = B − J[S*].
    Every ingredient is a 1D/availability computation on the DATA —
    design-independent, cheap, rigorous. Its slack (B is not tight —
    it ignores multidimensionality) is the honest price.
  - O2 *Structure-exploiting exact δ=0 zones*: in the smooth
    supersonic MoC regime with fixed length, the classical
    thrust-optimum theory (Guderley–Hantsche; Rao; Shmyglevsky;
    Kraiko's general-gas extensions) characterizes the GLOBAL optimum
    within the smooth class via the control-surface method — where its
    hypotheses certify (per-phase smooth flow, exhaustive control
    surface family), the averaged analog can yield PROVEN δ=0 within
    the sector-and-class, which is exactly the brief's "δ = 0 proven
    wherever structure permits".
  - O3 *Convex/moment relaxations* (Lasserre hierarchy on
    polynomialized reduced models; SDP bounds): rigorous but scales
    only to heavily reduced surrogates of this problem; admissible as
    a bound on the REDUCED model + declared reduction error — chain of
    custody must be explicit or it proves nothing about J.
  - O4 *Branch-and-bound over the sector parameter box* with rigorous
    interval/Lipschitz bounds on J (needs certified Lipschitz
    constants for the PDE-functional — obtainable from adjoint bounds
    on compact parameter boxes, expensive but finite-dimensional).
  - O5 *Statistical gap estimates* (BO posterior bounds, multistart
    coverage): reportable, NEVER certificate-grade (wrong epistemic
    type for (iv)); listed to be rejected with that stated reason.
- **Decision criterion**: δ from O1 vs the design-improvement scale
  seen in optimization (if B − J[S*] is dominated by B's own slack,
  tighten B with additional theorems — swirl debit, angularity debit
  (Malina-type divergence factor bound), base-pressure ceiling —
  before buying O3/O4 complexity).
- **Recommendation**: O1 always-on (it also independently audits every
  J evaluation: any J > B is an instant solver-bug rejector), O2
  pushed hard in the smooth sectors (it is this problem's real chance
  at δ=0), O4 reserved for the final champion's parameter box at
  coarse rigor, O3 only on reduced certified surrogates, O5 reported
  but flagged non-certificate.
- **Falsifier (for O1)**: any certified solve exceeding B falsifies
  the bound derivation (or the solver) — a deliberately dual-purpose
  rejector; (for O2) exhibit a piecewise-smooth admissible design
  beating the smooth-class optimum by more than the discretization
  bar → the δ=0 claim's class hypothesis was binding, downgrade to
  class-relative δ=0 with the class named.

### FORK-29 — Second-order conditions (iii) in verifiable form
- **Q**: How is "reduced Hessian ⪯ 0 on the active tangent cone" made
  checkable?
- **Options**: O1 dense reduced Hessian by O(n) Hessian-vector
  products (adjoint-of-tangent / hyperdual), eigen-decomposition on
  the active-cone projector; O2 Lanczos extremal-eigenvalue probe
  (cheap, gives the certificate-relevant top of the spectrum + a
  residual bound); O3 quasi-Newton curvature accumulation (BFGS
  spectrum as proxy — rejected for certificates: secant information
  is history-dependent, not the Hessian); O4 directional sampling
  along constraint-null directions with FD curvature (verification
  layer only).
- **Decision criterion**: parameter dimension after sector reduction;
  the certificate needs the MAXIMUM eigenvalue on the cone plus a
  numerical-error bar smaller than its distance to zero.
- **Recommendation**: O2 with O1 fallback at low dimension, O4 as the
  independent cross-check; report eigenvalue + bar + mesh-refinement
  stability (curvature must be mesh-converged or it is discretization
  curvature, not physics).
- **Falsifier**: top cone-eigenvalue's bar straddles zero after
  refinement → (iii) is UNDECIDED at achievable resolution; the
  certificate must say so (flat-top optimum — physically common when
  a constraint plateau dominates).

---

## 8. FAMILY G — NUMERICS AND ERROR CONTROL

### FORK-30 — Per-phase discretization scheme
- **Q**: MoC vs FV vs DG for the per-phase solves feeding J and its
  gradient.
- **Options**: O1 thermally-perfect MoC (Zucrow–Hoffman lineage) on
  supersonic smooth patches: spectral-quality accuracy per cost,
  natural fitted fronts, natural shape-calculus interface — but
  needs transonic patching (FORK-13) and swirl-augmented
  characteristic relations (axisymmetric-with-swirl characteristics
  are classical but implementation-error-prone: verify against
  manufactured rotating-flow solutions). O2 finite-volume
  (MUSCL/approximate-Riemann): robust workhorse; entropy-fix and
  carbuncle audits mandatory at strong fronts; gradient pollution at
  captured fronts (FORK-24). O3 high-order DG with shock fitting or
  subcell limiting: best convergence-per-DOF in smooth+fitted
  regime; implementation cost high; dual-consistency available
  (FORK-24 O3). O4 spectral/collocation on mapped smooth domains
  (only if front-free per phase — decided by data, not hope).
- **Decision criterion**: the certificate class chose fitted fronts
  (FORK-12): O1/O3-fitted qualify; O2 remains the exploration and
  cross-check solver. Two INDEPENDENT discretizations agreeing within
  bars on champions is itself a certificate line (code-error
  rejector).
- **Recommendation**: O1 (certificate, smooth/supersonic) + O2
  (exploration, transonic pockets, cross-check); O3 adopted only if
  O1's transonic patching proves fragile.
- **Falsifier**: cross-solver disagreement above combined bars on a
  champion → at least one solver's error model is wrong there;
  champion quarantined.

### FORK-31 — Mesh/refinement policy and error estimators
- **Q**: How are discretization errors estimated, driven, and turned
  into certificate bars?
- **Options**: O1 goal-oriented adjoint (DWR — Becker & Rannacher
  2001; Venditti & Darmofal 2002 for aero functionals): estimates
  error IN J directly; drives adaptation where thrust cares;
  effectivity must be MEASURED on a refinement ladder, and the
  safety factor DERIVED as (observed worst effectivity)⁻¹ × margin —
  this is how "no magic constants" is honored for meshes. O2
  Richardson/GCI (Roache): model-agnostic, order-verified; the
  cross-check on O1's effectivity. O3 residual-based indicators
  (drive-only; no certificate value). O4 uniform refinement ladders
  (expensive truth anchor at champions).
- **Decision criterion**: DWR effectivity stability across the ladder
  and across phases (front-passage phases will stress it).
- **Recommendation**: O1 driving + O2 certifying + O4 at champions;
  per-phase error budgets summed with μ-weights into the (v)
  discretization bar.
- **Falsifier**: measured effectivity outside its assumed band on any
  accepted solve → that solve's bar is void; ladder re-run (again a
  per-solve rejector, automated).

### FORK-32 — Tolerance derivation, error budget, and stopping
- **Q**: How are all tolerances derived and when does the program
  STOP?
- **Options / structure**: O1 top-down budget: fix the target
  total bar Δ_tot for |J_exact − J[S*]| at the level the VALIDATION
  instrument can adjudicate (thrust-stand class ~0.5–1%; there is no
  scientific content in bars finer than any conceivable test can
  check — this anchors the whole cascade in physics, not preference);
  partition Δ_tot across the named terms of (v): unsteadiness (FORK-2
  carrier), model-form (gas bracket FORK-14, base model FORK-20,
  viscous margin FORK-15), data closure (FORK-7), quadrature
  (FORK-10), discretization (FORK-31), optimization residual
  (KKT-to-J conversion via a local curvature bound). Optimizer stops
  when its residual term is ≤ its allocation AND further optimization
  gain estimate (gradient norm × trust radius) < its allocation. O2
  bottom-up (sum what you achieve): honest reporting mode when O1's
  target proves unreachable — the certificate then states the
  achieved Δ_tot rather than a target. O3 asymptotic-only tolerances
  (machine-precision chasing): rejected — cost without adjudicable
  content.
- **Recommendation**: O1 with O2 as the declared fallback posture.
  Falsifier: any single (v) term measured above its allocation with
  others unable to compensate → budget re-partitioned openly or the
  headline bar widened; silent overdraft is the failure mode this
  fork exists to kill.

### FORK-33 — Handling the certification boundary in the loop
- **Q**: The optimizer will be driven TOWARD designs whose state
  certification degrades (incipient separation phases, front-topology
  changes, transonic pocket growth). Loop mechanics?
- **Options**: O1 hard reject (trust-region step rejection on
  certification failure; robust, may stall on the boundary). O2
  margin-constraint formulation (certifiability margins — front
  residuals, continuation distance, pocket-Mach margins — become
  explicit constraints with their own gradients; the boundary becomes
  navigable instead of a wall). O3 fidelity escalation at the
  boundary (ambiguous designs re-solved at higher fidelity before
  verdict; pairs with FORK-27 O2's TR logic). O4 surrogate
  classification of certifiable region (ML classifier proposes,
  never disposes — same epistemic fence as FORK-27 O6).
- **Recommendation**: O2 primary + O3 adjudication + O1 as the outer
  guard. Grounds: experience across constrained aero-optimization —
  optima live ON boundaries; a formulation that cannot take gradients
  of its own certifiability will grind or lie.
- **Falsifier**: champion's certifiability margins at optimum sit
  inside their own error bars → the certificate is boundary-ambiguous
  and must say so (equivalently FORK-23's boundary clause fires).

---

## 9. FAMILY H — VALIDATION AND FALSIFICATION OF THE CERTIFIED-OPTIMUM CLAIM

### FORK-34 — Evidence hierarchy for a real engine
- **Q**: What experimental/computational evidence VALIDATES or
  FALSIFIES "S* is the certified optimum, with bars", for hardware?
- **Options / the hierarchy at its best (all tiers named, cheapest
  rejectors first)**:
  - V0 *Internal cross-checks* (already mandated above): O1≡O2 thrust
    bookkeeping identity (FORK-22), J ≤ B availability audit
    (FORK-28), Rao-limit regression (FORK-26), cross-solver champion
    agreement (FORK-30).
  - V1 *Wave-frame steady 3D Euler solve at S\** (FF-2): adjudicates
    the (v) unsteadiness bar with the SAME physics model — the
    cleanest single falsifier of the averaging step. Pass criterion:
    |J_wf − J| within the claimed unsteadiness allocation.
  - V2 *Unsteady CFD (URANS→LES ladder) of nozzle with rig-measured
    inflow*: adjudicates viscous margin + unsteady separation sign
    (FORK-15 O4) + base pressure (FORK-20).
  - V3 *Coupled combustor+nozzle simulation OR rig test*: adjudicates
    causal separation (FORK-6) — does the wave mode survive S*?
    This is the tier that can kill the certificate non-locally.
  - V4 *Cold-flow / surrogate-cycle experiments*: phase-swept nozzle
    flow via rotating-valve or fluidic actuation at matched St and
    swing amplitude; PIV/schlieren/BOS for attachment verification
    per phase; wall pressure taps vs per-phase predictions (validates
    the g_sep carrier where instrumentation is easy).
  - V5 *Hot-fire differential thrust test*: S* vs the FORK-18 O4
    baseline (annular-bell) AND vs a deliberately perturbed S*±
    (the curvature check made physical): the claim "S* is optimal"
    predicts a measurable ORDERING with predicted gaps; thrust-stand
    uncertainty (~0.5–1% with high-frequency load-cell + drift
    control; RDE stands documented in Fotia et al., Bennewitz et al.)
    must be below the predicted gaps or the test is void BY DESIGN
    (pre-register the power calculation).
  - V6 *Mode/H-DATA field monitoring* in every hot test (FORK-11
    instruments): any mode change with S* installed = FORK-6
    falsification, supersedes all thrust comparisons.
- **Decision criterion**: each tier maps to a NAMED term of the (v)
  budget or a named premise (H-DATA, causal separation, attachment);
  a tier passes only if its measured discrepancy fits inside that
  term's allocation.
- **Recommendation**: V0 continuous; V1 at every champion; V2+V3 at
  the final champion; V4 if a rig exists before metal; V5+V6 as the
  program's terminal claim test, pre-registered (prediction-first,
  with the ordering and gaps published before the test).
- **Falsifier of the whole program**: V5 measures the perturbed
  design S*± above S* beyond combined bars, with V6 clean → the
  certified-optimum claim is FALSE for the real engine; the autopsy
  order is: FORK-6 (data contract) → FORK-2 (averaging) → FORK-15/20
  (viscous/base) → FORK-14 (gas model), which is exactly the (v)
  budget read backwards.

---

## 10. ORDER OF BATTLE (dependency order + load-bearing designation)

Stage 0 — **Contract physics (LOAD-BEARING, everything downstream is
hostage)**: FORK-6 (causal separation audit design) → FORK-5 (Γ_d
placement audit) → FORK-8/9 (data fidelity: profiles + swirl) →
FORK-7 (subsonic closure) → FORK-11 (H-DATA monitor). A wrong call
here poisons every certificate regardless of mathematical quality.

Stage 1 — **Averaging legitimacy (LOAD-BEARING)**: FORK-1 (anchor
architecture; DP-2 written down as a theorem with hypotheses) →
FORK-2/3 (correction carrier + limit fallback) → FORK-10 (quadrature
split). Decides whether the entire per-phase machine is admissible
and what its (v) term looks like.

Stage 2 — **State-model layer (load-bearing for the constraint,
local for the objective)**: FORK-12/13 (solution class + sonic
treatment) → FORK-14 (gas bracket, run early — it may already cap
achievable bars) → FORK-15/16 (separation carrier + aggregation).

Stage 3 — **Bookkeeping locks (cheap, do immediately after Stage 1)**:
FORK-22 (DP-1 + the O1≡O2 per-solve rejector) → FORK-23 (class-exit
semantics) → FORK-28 O1 (availability bound B armed as an always-on
audit; also the first honest δ).

Stage 4 — **Design space (LOAD-BEARING at FORK-17/18, local at
19–21)**: FORK-17 (sector enumeration + completeness lemma) →
FORK-18 (sector physics priors, DP-6 σ* computed from data) →
FORK-19 (parametrization + enrichment ladder) → FORK-20/21
(truncation/base model; lip).

Stage 5 — **Optimality machine**: FORK-24 (order-of-differentiation
policy) → FORK-25 (derivative builds + closure rejectors) → FORK-26
(the (ii) averaged stationarity derivation + Rao-limit regression) →
FORK-27 (search mechanics) → FORK-29 ((iii) machinery).

Stage 6 — **Error control shell (wraps everything)**: FORK-31
(estimators + derived safety factors) → FORK-30 (solver pairing) →
FORK-32 (the (v) budget and stopping — note Δ_tot is anchored by
FORK-34's instrument realities, so Stage 7 feeds back here by
design) → FORK-33 (certification-boundary navigation).

Stage 7 — **Falsification program**: FORK-34 tiers V0→V6, with V0
armed from Stage 3 onward and V1 at every champion.

**Load-bearing forks (a wrong early choice poisons everything)**:
FORK-6 (causal separation — can invalidate the input data themselves),
FORK-1/2 (averaging anchor and its correction — the problem's central
legitimacy question at marginal St), FORK-8/9 (3D/swirl data fidelity
— biases the topology verdict irreversibly), FORK-17/18 (topology
treatment — disconnected admissible set, no continuation across
sectors, decisions effectively final), FORK-24 (differentiation order
— silent wrong gradients corrupt (ii)–(iv) invisibly), FORK-32 (bar
anchoring — bars finer than any instrument make the certificate
unfalsifiable, i.e., unscientific). All others are local: wrong
choices cost time and are caught by the named rejectors.

---

## 11. HARD OBSTRUCTIONS (named, with state-of-the-art handles)

1. **Marginal St has no small parameter**: neither quasi-steady nor
   mixed-out is controlled. Handle: wave-frame exactness anchor
   (DP-2) + harmonic-balance correction with measured N_h convergence
   (Hall et al. 2002; McMullen & Jameson 2006).
2. **Nozzle→combustor feedback** breaks the data contract for subsonic
   phases. Handle: supersonic-screen check; impedance-band constraint;
   fixed-point re-measurement loop (FORK-6); experimental precedent
   for the danger: throat-restriction mode shifts (Fotia et al. 2016;
   Anand & Gutmark 2019).
3. **Shock sensitivities in the optimization loop**: captured-shock
   adjoints are wrong in the limit (Giles & Pierce 2001). Handle:
   fitted-front certificate class + dual-consistent discretizations
   for exploration solvers.
4. **Base pressure is not an Euler observable** (truncated plug
   sectors). Handle: declared base-model layer with RANS/experiment-
   calibrated scatter entering (v); or untruncated-spike class.
5. **Multi-D weak-solution non-uniqueness** (De Lellis–Székelyhidi
   wild solutions). Handle: class-relative certificates in the
   piecewise-smooth fitted class, topology-change events treated as
   certification boundaries (FORK-12/33).
6. **Semi-infinite attachment constraint with a moving active
   phase-set**. Handle: KS-smoothing in-loop + adaptive-phase local
   reduction at certificate time (Hettich–Kortanek).
7. **Swirl is unrecoverable under axisymmetry** (DP-4) — a hard
   physical debit no optimizer can undo; must live in B and in the
   reported performance, not be optimized away by wishful modelling.
8. **Globality for a PDE-constrained shape problem is generically
   undecidable at scale**. Handle: availability bound B (physics),
   classical control-surface global theory where its hypotheses hold
   (Guderley–Hantsche/Rao/Kraiko — the δ=0 zones), finite sector
   disjunction (FORK-17), and honest δ elsewhere.
9. **Frozen-gas model-form error may exceed achievable δ**. Handle:
   frozen/equilibrium bracket as a mandatory named bar (Bray-type
   sudden-freezing audit locates the freeze point); the certificate
   is then explicitly model-class-relative.
10. **Instrument-limited falsifiability**: thrust-stand bars ~0.5–1%
    cap the adjudicable claim. Handle: anchor Δ_tot to the instrument
    (FORK-32), pre-registered differential tests with power
    calculation (FORK-34 V5) — differential comparisons partially
    cancel systematics and are the strongest affordable test.

---

## 12. SELECTED REFERENCES (open literature, propulsion lens)

- Rao, G.V.R., "Exhaust Nozzle Contour for Optimum Thrust," Jet
  Propulsion 28(6), 1958. — thrust-optimum control-surface method.
- Guderley & Hantsche, 1955 — earliest exact nozzle thrust-optimum
  formulation.
- Kraiko, A.N., school of exact variational gasdynamics (incl.
  general-gas extensions of optimal contours).
- Zucrow & Hoffman, *Gas Dynamics* Vols. I–II, 1976–77 — thermally
  perfect MoC, axisymmetric characteristics with swirl.
- Angelino, G., "Approximate Method for Plug Nozzle Design," 1964;
  Hagemann, Immich, Nguyen, Dumnov, "Advanced Rocket Nozzles," J.
  Propulsion & Power 14(5), 1998 — plug/E-D/altitude compensation.
- Frey & Hagemann, "Restricted Shock Separation in Rocket Nozzles,"
  JPP 16(3), 2000; Stark & Wagner, flow-separation criteria, 2009;
  Summerfield, Foster & Swan 1954; Schmucker 1974.
- Hall, K.C., Thomas & Clark, "Computation of Unsteady Nonlinear
  Flows in Cascades using a Harmonic Balance Technique," AIAA J.
  40(5), 2002; McMullen & Jameson, time-spectral methods, 2006.
- Giles & Pierce, "Analytic adjoint solutions for the quasi-1D Euler
  equations with shocks" (and companion adjoint theory), 2001.
- Becker & Rannacher, DWR a-posteriori error control, Acta Numerica
  2001; Venditti & Darmofal, output-based adaptation, JCP 2002;
  Roache, GCI, 1997.
- Allaire, Jouve, Toader, level-set shape/topology optimization, JCP
  2004; Osher & Sethian 1988; Borrvall & Petersson, flow topology
  optimization, 2003.
- Jones, Schonlau, Welch, "Efficient Global Optimization," 1998;
  Forrester & Keane, surrogate-based optimization review, 2009;
  Hansen, CMA-ES; Deb, NSGA-II.
- Hettich & Kortanek, semi-infinite programming review, SIAM Rev.
  1993; Kreisselmeier & Steinhauser 1979.
- Chenais, D., "On the existence of a solution in a domain
  identification problem," JMAA 1975 — cone-condition compactness.
- De Lellis & Székelyhidi, wild weak solutions of Euler, 2009–2013.
- Schwer & Kailasanath, RDE numerical studies (AIAA/Combust. Flame,
  2011–2013); Braun, Lu, Wilson et al., RDE exit-condition/nozzle
  integration studies, 2013; Rankin, Schauer et al., OH*
  chemiluminescence RDE, 2017; Fotia, Hoke, Schauer, RDE performance
  with nozzles/aerospikes, JPP 2016–2018; Bennewitz, Bigler, Hargus
  et al., RDE mode identification, 2019; Anand & Gutmark, RDE review,
  PECS 2019; Raman, Prakash, Gamba, RDE physics review, Annu. Rev.
  Fluid Mech. 2023; Kaemming & Paxson, RDE thermodynamic performance
  modelling, 2017; Harroun & Heister, aerospike nozzles for RDE,
  2019–2021; Stechmann, Heister et al., RDE design/performance
  analyses; Paxson, RDE reduced modelling, NASA.
- Bray, K.N.C., "Atomic recombination in a hypersonic wind-tunnel
  nozzle," JFM 1959 — sudden-freezing analysis; Gordon & McBride,
  NASA CEA, 1994/96.
- Cumpsty & Horlock, "Averaging Nonuniform Flow for a Purpose," J.
  Turbomach. 2006.
- Drela, M., "Pros and Cons of Airfoil Optimization," 1998 —
  multipoint brittleness lesson.
- Rahimian & Mehrotra, distributionally robust optimization survey,
  2019; Nemirovski & Shapiro, chance constraints, 2006.
- Alexandrov et al., first-order-consistent multifidelity trust
  regions, 1998–2001.
- Olson & Lele, separated nozzle-flow unsteadiness, 2013 (and the
  side-load literature: Östlund & Muhammad-Klingmann review 2005).

— END OF TREE —
