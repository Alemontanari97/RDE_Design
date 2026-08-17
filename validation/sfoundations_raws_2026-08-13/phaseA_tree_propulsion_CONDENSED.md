# CONDENSED (mechanical slice; authority = phaseA_tree_propulsion.md, line refs cited)

[L105] ### FORK-1 — What exact object does the computable objective approximate?
  - **Recommendation**: Two-tier anchor: optimize under O1, CERTIFY the
    averaging error against O2 (and/or O4 with demonstrated N_h
    convergence) at the incumbent design(s). Declare O3 only as the
    opposing bracket end for the (v) error bar discussion. Grounds: the
    optimality machinery (ii)–(iv) is only affordable on O1; O2 is the
    unique zero-debt truth model this problem happens to possess —
    refusing to use it as the anchor would be malpractice.

[L156] ### FORK-2 — Where does the quasi-steady per-phase model break at marginal St?
  - **Recommendation**: O2 as default carrier of the (v) unsteadiness
    term, promoted to O3 if the measured spectral decay is slow.
    Grounds: at marginal St a pure O1 claim is indefensible (the brief
    says so implicitly by declaring St marginal), while O4-everywhere
    destroys the optimization budget; O2/O3 keep steady machinery and
    produce a NAMED, EVALUABLE correction — exactly what (v) demands.

[L210] ### FORK-3 — Existence of the time-average limit and the liminf/limsup fallback
  - **Recommendation**: O1 inside the certified class, with the H-DATA
    monitor as an explicit certificate precondition; O2 brackets
    reported whenever the monitor flags marginal behavior. Grounds: the
    brief pins H-DATA as declared-and-monitorable; physics says mode
    count is bistable/hysteretic (documented in Anand & Gutmark 2019),
    so the monitor is load-bearing, not decorative.

[L234] ### FORK-4 — Objective robustness: deterministic μ vs uncertainty in the data family
  - **Recommendation**: O1 + reported dJ/d(data) norms as a mandatory
    certificate line; escalate to O2 only if that sensitivity times the
    measured data bar rivals δ. Keep the μ-a.e. separation constraint
    HARD (not chance-constrained): separation is a cliff (side loads,
    RSS transition — Frey & Hagemann 2000), not a graceful degradation.

[L269] ### FORK-5 — Placement of Γ_d: where is "downstream of all heat release" real?
  - **Recommendation**: O2 with O3 as the always-on residual accounting.
    Grounds: thrust is first-order sensitive to heat addition in
    supersonic flow (Rayleigh: heat addition at M>1 raises stagnation
    temperature but costs stagnation pressure); silently absorbing it
    falsifies the frozen-gas pin too (FORK-14).

[L299] ### FORK-6 — Causal separation: nozzle→combustor back-reaction (the contract's weakest premise)
  - **Recommendation**: O1-check first (it may simply hold for a
    well-placed Γ_d — detonation products expand quickly to supersonic
    axial Mach); else O2 with a rig-calibrated band, with O3 declared as
    the escalation path in the certificate's preconditions. Grounds:
    this is the fork where a mathematically flawless optimum can be
    physically meaningless — an optimum that changes the engine's wave
    mode has invalidated its own input data.

[L339] ### FORK-7 — Closure for subsonic-axial patches on Γ_d
  - **Recommendation**: O2. Grounds: p0/T0/angle are the quantities a
    combustor model or rig measures most robustly (Kiel/impact probes
    survive unsteadiness better in mean; total quantities are the
    physically transported invariants along particle paths in the
    frozen model); characteristic counting is textbook-clean; it also
    matches how the causal-separation impedance band (FORK-6 O2) is
    phrased.

[L368] ### FORK-8 — Dimensional fidelity of s(ξ): full radial profiles + swirl vs reduced data
  - **Recommendation**: O1 as the contract of record, O3 as the
    computational carrier with stated truncation error. Grounds: plug
    and E-D sectors specifically exploit the inner/outer radius states
    differently (FORK-18); collapsing radius biases the TOPOLOGY
    decision, which is the least reversible decision in the program.

[L392] ### FORK-9 — Swirl accounting (azimuthal momentum in an axisymmetric design)
  - **Recommendation**: O1, mandatory. Grounds: swirl is not a
    correction, it is a first-order term in both thrust bookkeeping and
    radial equilibrium (it changes wall pressure distributions and hence
    the OPTIMAL CONTOUR, not just the objective value); it also alters
    the separation margin (swirl stabilizes/destabilizes the adverse
    pressure gradient response of the near-wall flow).

[L429] ### FORK-10 — Phase discretization: quadrature over Ξ
  - **Recommendation**: O3 with O1 on the smooth part. Grounds: cycle
    data from a detonation ARE kinked; pretending otherwise puts an
    uncontrolled O(Δξ^1) error inside a program that promises derived
    tolerances.

[L450] ### FORK-11 — H-DATA violation monitor (mode detection as part of the design)
  - **Recommendation**: O3 primary (it is the exact hypothesis), O1 as
    the cheap online tripwire. Falsifier for the monitor itself: inject
    synthetic two-mode data at small secondary amplitude; monitor must
    fire before the (v) bound degrades by its own tolerance (rejector
    calibration).

[L474] ### FORK-12 — Per-phase solution class: smooth / fitted fronts / captured weak
  - **Recommendation**: O2 as the certificate class, O3 as the
    exploration/fallback solver, O1 inside proven-supersonic-smooth
    patches (it is faster and its optimality theory is the classical
    backbone). Non-uniqueness handling: restrict certificates to the
    piecewise-smooth class with entropy-admissible fronts and declared
    front topology; treat topology changes as certification-boundary
    events (FORK-33). The wild non-uniqueness of multi-D weak Euler
    solutions (De Lellis–Székelyhidi) is fenced out BY CLASS FIAT,
    declared openly: certificates are class-relative.

[L514] ### FORK-13 — Sonic region treatment (per phase)
  - **Recommendation**: O2 where pockets are localized and smooth, O3
    otherwise; never silently O1. Grounds: the low-axial-Mach phase
    right behind the wave is precisely the thrust-poor,
    separation-prone phase — mis-modelling it biases both J and the
    binding constraint.

[L537] ### FORK-14 — Gas model: frozen thermally-perfect γ(T) — where it matters, where it fails
  - **Recommendation**: O1 + O2 mandatory, O3 once per engine class.
    Grounds: for stoichiometric H2–air detonation products the
    frozen/equilibrium Isp spread through a large-ratio expansion is
    a few percent — likely LARGER than any claimed δ; a certificate
    that does not carry the bracket as a named model-form bar is
    physically hollow even if mathematically tight.

[L574] ### FORK-15 — Viscous layer and the separation criterion
  - **Recommendation**: O2 in-loop as g_sep carrier (with derived margin
    from its own validation scatter vs O3), O1 retained only as a
    tripwire cross-check, O3 at every incumbent, O4 once to set the
    margin's unsteadiness safety term. Grounds: an optimizer WILL find
    the contours where a correlation lies; the constraint must be built
    from local physics it cannot game.

[L614] ### FORK-16 — Aggregation of the per-phase attachment constraint
  - **Recommendation**: O2 in-loop + O3-style adaptive phase refinement
    near convergence so the certificate is issued against the TRUE
    semi-infinite constraint, not the smoothed one. Falsifier: post-hoc
    fine-phase sweep finds a violating phase between quadrature nodes →
    certificate void; refine and re-issue (this sweep is a mandatory
    certificate step).

[L639] ### FORK-17 — Topology treatment: emergent vs enumerated sectors
  - **Recommendation**: O2 with the enumeration-completeness lemma +
    O3-style low-fidelity hunt as insurance. Grounds: certificates
    (ii)–(iv) are sector-local anyway (the admissible set is
    disconnected across sectors: no continuous admissible path removes
    a shroud); globality (iv) is then a finite max over sector
    champions, each with its own δ — clean.

[L685] ### FORK-18 — Configuration physics: who should win under cycle-varying inflow, and why
  - **Recommendation**: seed the search with O2 and O1 both at full
    effort; treat O3 as envelope-bound-triggered; keep O4 as the
    mandatory baseline. Grounds: DP-6 (below) plus the experimental
    record.

[L748] ### FORK-19 — Contour parametrization within a sector
  - **Recommendation**: O2 as the certificate-class (with knot-
    refinement studies as the enrichment ladder), O1 as the analytic
    spine to (ii)'s stationarity conditions (the averaged Rao system is
    what (ii) should REPRODUCE in the smooth supersonic case — a
    powerful cross-check: single-phase limit must recover Rao's
    control-surface conditions exactly), O5 confined to the topology
    hunt.

[L790] ### FORK-20 — Plug truncation and base pressure (the Euler-uncertifiable zone)
  - **Recommendation**: O2 with O4-grade calibration for the champion,
    and O1 evaluated whenever constraints admit it (the certificate is
    cleanest there). Grounds: pretending Euler covers the base is the
    one place this program could ship a certified number that a thrust
    stand would flatly contradict.

[L821] ### FORK-21 — Lip and attachment treatment on Λ
  - **Recommendation**: O2 with radius at the curvature-bound floor:
    buys certifiable adjoint regularity for negligible thrust.

[L847] ### FORK-22 — Control surface, ambient term, and what counts as nozzle thrust
  - **Recommendation**: O2 for the objective (matches the brief), O1
    computed ALWAYS as the redundancy check (equality within
    discretization bar = a free integral-identity rejector on every
    solve), O3 for reporting nozzle merit. Grounds: DP-1 makes the
    choice safe; the O1≡O2 check is the cheapest strong audit in the
    whole program.

[L877] ### FORK-23 — Phases outside the certified class inside the average
  - **Recommendation**: O1 claims + O3 mechanics + O4 restoration.

[L903] ### FORK-24 — Optimize-then-discretize vs discretize-then-optimize
  - **Recommendation**: O4/O1 on the fitted certificate class + O2 on
    the captured exploration solver, with O3-grade dual consistency
    wherever FV/DG is used near certificates. The (ii) deliverable
    (averaged stationarity system: per-phase adjoints, SHARED-contour
    averaged wall condition Σ-form, transversality at endpoints,
    multiplier meaning) is an OTD object — derive it continuously,
    then verify discretely.

[L932] ### FORK-25 — Derivative computation and its verification
  - **Recommendation**: O2 primary + O5 verification on unit problems +
    O4 sanity on the full J + O6 for reduced-Hessian actions. Every
    gradient used in a certificate carries a closure record
    (dot-product test / adjoint-consistency residual) — the adjoint
    identity ⟨λ, R_u v⟩ = ⟨J_u, v⟩ tested to a derived tolerance is a
    per-build rejector.

[L956] ### FORK-26 — Structure of the averaged stationarity system (the (ii) deliverable)
  - **Recommendation**: derive O1–O4 in full as the (ii) artifact; the
    Rao-limit regression and the marginal-value multiplier audit are
    its two falsifiers, both cheap.

[L989] ### FORK-27 — Optimizer class and globalization (search mechanics)
  - **Recommendation**: O2 (with O1 inner) as the closer; O4 across
    sector parameter spaces; O3 only if multimodality is DEMONSTRATED
    (basin study), O5 for initial screening, O6 excluded from the
    certified path.

[L1033] ### FORK-28 — The globality certificate: how δ is actually COMPUTED
  - **Recommendation**: O1 always-on (it also independently audits every
    J evaluation: any J > B is an instant solver-bug rejector), O2
    pushed hard in the smooth sectors (it is this problem's real chance
    at δ=0), O4 reserved for the final champion's parameter box at
    coarse rigor, O3 only on reduced certified surrogates, O5 reported
    but flagged non-certificate.

[L1087] ### FORK-29 — Second-order conditions (iii) in verifiable form
  - **Recommendation**: O2 with O1 fallback at low dimension, O4 as the
    independent cross-check; report eigenvalue + bar + mesh-refinement
    stability (curvature must be mesh-converged or it is discretization
    curvature, not physics).

[L1115] ### FORK-30 — Per-phase discretization scheme
  - **Recommendation**: O1 (certificate, smooth/supersonic) + O2
    (exploration, transonic pockets, cross-check); O3 adopted only if
    O1's transonic patching proves fragile.

[L1144] ### FORK-31 — Mesh/refinement policy and error estimators
  - **Recommendation**: O1 driving + O2 certifying + O4 at champions;
    per-phase error budgets summed with μ-weights into the (v)
    discretization bar.

[L1166] ### FORK-32 — Tolerance derivation, error budget, and stopping
  - **Recommendation**: O1 with O2 as the declared fallback posture.

[L1192] ### FORK-33 — Handling the certification boundary in the loop
  - **Recommendation**: O2 primary + O3 adjudication + O1 as the outer
    guard. Grounds: experience across constrained aero-optimization —
    optima live ON boundaries; a formulation that cannot take gradients
    of its own certifiability will grind or lie.

[L1218] ### FORK-34 — Evidence hierarchy for a real engine
  - **Recommendation**: V0 continuous; V1 at every champion; V2+V3 at
    the final champion; V4 if a rig exists before metal; V5+V6 as the
    program's terminal claim test, pre-registered (prediction-first,
    with the ordering and gaps published before the test).
