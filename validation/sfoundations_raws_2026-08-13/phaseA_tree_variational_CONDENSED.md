# CONDENSED (mechanical slice; authority = phaseA_tree_variational.md, line refs cited)

[L128] **FORK-1: How is J_exact related to the computable objective?**
  - **Recommendation.** **O1 as optimizer objective + O4 as the
    declared relation + O3 at the final candidate(s)** (this is FF-1
    with an FF-2 verification tier). Grounds: (v) demands a *bound*,
    not an expansion; at marginal St only a computed carrier is honest
    (Proof P6); optimizing O3 throughout buys accuracy the bracket may
    show is unnecessary, at 10²–10⁴× cost.

[L173] **FORK-2: Thrust bookkeeping — which control surface, and how does
      Pa enter?**
  - **Recommendation.** **O3.** Grounds: the invariance lemma is a
    two-line divergence-theorem argument in the continuum and its
    discrete violation is a free, derived error indicator feeding
    FORK-31 tolerances. Pa enters only through (p − Pa) on the closed
    surface — this makes F gauge-invariant to ambient pressure on
    closed surfaces and defines the free-boundary condition p = Pa
    consistently (FORK-11).

[L204] **FORK-3: Which statistic of the cycle is optimized?**
  - **Recommendation.** **O1**, with the μ-sensitivity of J and of the
    active-phase set reported as part of certificate (v); adopt O4
    only if measured δμ (from H-DATA monitoring) times the computed
    μ-gradient exceeds the globality gap δ. Grounds: do not silently
    change the declared objective; robustness pressure is real but
    belongs in the error-bar/constraint layer here.

[L238] **FORK-4: Discretization of the phase space (Ξ, μ).**
  - **Recommendation.** **O1 upgraded to O2 with a measured
    ξ-modulus**, and the quadrature error entered as a named term in
    the (v) budget and in the constraint-covering certificate
    (FORK-23). Grounds: one-dimensional periodic Ξ; the only threat is
    loss of ξ-regularity, which O2 detects by construction.

[L277] **FORK-5: The idealization ladder for the state model.**
  - **Recommendation.** **R1s as the optimization state** (swirl is
    part of the given data and enters at zero extra dimensionality),
    R0 for bound generation, R2 as a structural cross-check of the
    quasi-steady picture (it is the exact steady object under H-DATA
    — a rare gift; use it to calibrate the FORK-1 bracket), R3 at
    candidates, Rv only through g_sep. Grounds: each certificate gets
    the cheapest honest carrier; R2 is this problem's special
    structure and should not be left unused.

[L317] **FORK-6: Solution concept for the per-phase multi-D Euler state.
      (HW-2 lives here.)**
  - **Recommendation.** **O1 as the certified-design class, O2 as the
    fallback class where shocks are unavoidable, with the class
    boundary itself made a design constraint** (a shock-formation
    margin monitor analogous to g_sep). O3 only as the *numerical
    realization* of O1/O2 with an a posteriori check that the computed
    state is in the declared class (front-detection + smoothness
    indicators), never as the definition. Grounds: (i) an optimal
    thrust nozzle should be shock-free where possible on performance
    grounds anyway (shock = entropy = thrust loss; classical
    supersonic nozzle variational theory — Guderley–Hantsch 1955,
    Rao 1958, Shmyglevskii/Kraiko school — lives in O1); (ii) O1/O2
    are the only options passing criterion (a)+(b) today.

[L373] **FORK-7: Per-phase non-uniqueness of the *flow configuration*
      (hysteresis) and the selection principle.**
  - **Recommendation.** **O1 + O4**: continuation defines the branch;
    a fold-margin monitor (distance of the cycle path to the fold set,
    via the measured inf_ξ σ_min of the linearized steady operator)
    joins the certification oracle. Grounds: single-valued F with a
    computable exclusion boundary beats averaging over an undeclared
    branch choice; O2 is kept as the referee when O1's anchor is
    ambiguous.

[L408] **FORK-8: Closure where the axial inflow on Γ_d is subsonic.**
  - **Recommendation.** **O4 where the data family permits; else O1
    with the incoming set derived from s(ξ) and the closure stated as
    hypothesis H-CLOSURE alongside H-DATA**, monitored by comparing
    the reflected invariant computed by the solver against the data
    family's implied one. Grounds: O1 is the unique closure that is
    both well-posed by construction and honest about what is assumed.

[L446] **FORK-9: Thermally-perfect γ(T) thermodynamics — exact treatment
      vs surrogates.**
  - **Recommendation.** **O2/O4 (they are the same decision at
    different smoothness) with certified interpolation error and AD-
    differentiable evaluation; O3 rejected as the state model**
    (γ-variation across an RDE cycle is a first-order thrust effect,
    and the brief pins γ ≠ const) **but retained as the bound-factory
    thermodynamics (R0 rung)** where its error is absorbed into the
    bound's slack. Grounds: exactness where certificates live,
    closed forms where only bounds live.

[L481] **FORK-10: Sonic set / throat treatment.**
  - **Recommendation.** **O4 if the data support it (check first —
    cheapest fork-kill available); else O3 with the sonic surface as a
    fitted internal boundary and O1's non-degeneracy monitor as part
    of certification.** Grounds: fitted free boundaries keep the
    shape calculus classical (transmission conditions), and choking
    non-degeneracy is exactly what protects differentiability of F in
    both S and ξ.

[L522] **FORK-11: Plume / free-jet boundary ("ambient pressure on free
      portions").**
  - **Recommendation.** **O2 by default with a per-phase certificate
    of exit supersonicity; automatic escalation to O1 in sectors where
    that certificate fails.** Grounds: pay the free-boundary cost only
    where the topology sector demands it; the escalation trigger is
    itself a computable monitor.

[L557] **FORK-12: Separation margin g_sep — which detection model?**
  - **Recommendation.** **O3 in the loop (IBL margin: physical,
    cheap, adjoint-capable), O1 retained as an outer conservative
    envelope (two-sided: certified designs must pass both), O4 as the
    checkpoint falsifier-carrier.** Grounds: a pure O1 threshold makes
    the *constraint boundary* a modeling artifact with O(1) crudeness
    exactly where multipliers must carry marginal-value meaning.

[L605] **FORK-13: Representation of the solid set S.**
  - **Recommendation.** **Two-tier: O2 (level-set on E) as the
    *sector-discovery* tier with the cone/curvature constraints
    enforced by constrained redistancing; then O1/O4 (spline graph +
    transformation calculus) as the *certificate* tier within each
    discovered sector.** Grounds: the brief makes topology an output
    (needs O2-or-O3-type freedom) but certificates (ii)–(iii) need
    the smooth parametric calculus (O4's function-space structure);
    no single representation serves both today — this is a genuine
    two-tier fork, not a compromise.

[L662] **FORK-14: Topology sectors — enumerate, or let the representation
      discover them?**
  - **Recommendation.** **O1 as the floor (declared sector list =
    hypothesis of the globality claim), O3/O4 as proposers that can
    only *add* sectors, O5 to prune sectors cheaply.** Grounds: an
    explicit, falsifiable hypothesis ("the optimum lies in one of the
    listed sectors, or the proposers would have found otherwise")
    beats an unprovable claim of representation completeness.

[L707] **FORK-15: Existence framework and its monitored failure boundary.
      (HW-1 lives here.)**
  - **Recommendation.** **O1 primary + O4 as the discrete shadow.**
    Concretely: Theorem (conditional): compact A(c) + certified-class
    state stability (hypothesis H-STAB, provable in the shock-free
    supersonic-marching subclass via a priori C¹ characteristic
    bounds uniform over A(c); conjectural across sonic surfaces and
    fitted shocks) ⇒ maximizer exists. Monitored failure boundary:
    (a) certification oracle failing along a maximizing sequence
    (state leaves the class ⇒ H-STAB inapplicable); (b) boundary
    oscillation at scale h0 (cone constraint active everywhere ⇒
    compactness marginal); both are computable flags.

[L762] **FORK-16: Encoding the constraint vector c (curvature, angle,
      envelope, wetted length) in the working representation.**
  - **Recommendation.** **O2 for the certificate tier (with O1's
    convex-hull bounds used as a feasible-start/trust region), O4 for
    the discovery tier.** Grounds: marginal values of L, R_E, angle
    bounds are themselves deliverables (they price the envelope).

[L798] **FORK-17: Optimize-then-discretize (OtD) vs discretize-then-
      optimize (DtO).**
  - **Recommendation.** **O3: dual-consistent DtO whose limit is the
    OtD system, with the continuous KKT residual evaluated a
    posteriori as a certificate** (the discrete optimum is fed into
    the continuum optimality system and the residual is a named error
    term). Grounds: this is the only option where (ii) and the
    computation certify each other.

[L841] **FORK-18: Form of the shape derivative.**
  - **Recommendation.** **Derive O3 as the master object; obtain O2
    for computation and O1 by integration by parts *when the state is
    certified-smooth near the wall*, and state (ii) in the O1 form.**
    Grounds: standard equivalence chain, each link used where valid;
    the O2→O1 integration by parts fails exactly where certification
    fails, which keeps the certificate honest.

[L875] **FORK-19: Differentiability across embedded discontinuities.
      (HW-3, part 1.)**
  - **Recommendation.** **O3 as the target class + O1 machinery
    implemented for transit and for sectors where fronts are
    unavoidable (e.g., E-D pluming); O2 rejected as a certificate
    gradient (P7) but allowed in the discovery tier; O4 held for the
    certification boundary itself (FORK-32).**

[L918] **FORK-20: Adjoint construction and the averaged optimality system.**
  - **Recommendation.** **O2 for computation, O1 as the certificate
    statement (the averaged wall condition + FORK-8 dual closure +
    adjoint front conditions where FORK-19 O1 is active).**

[L958] **FORK-21: Transversality / endpoint conditions.**
  - **Recommendation.** **O1+O2+O3 derived once in the transformation
    calculus (FORK-18 O3 gives them mechanically as boundary terms),
    each stated in μ-averaged form.**

[L995] **FORK-22: Machinery for the attachment state constraint. (HW-3,
      part 2.)**
  - **Recommendation.** **O2 wrapped in O1 path-following (standard
    state-constraint practice), with O4 only as the optimizer's
    early-phase smoother and its aggregation error carried
    explicitly.**

[L1036] **FORK-23: Aggregation over phases — certifying "μ-a.e." from
      finitely many phases.**
  - **Recommendation.** **O1+O2 combined:** exchange to find the
    binding phases, covering to certify between them; margin m becomes
    a *derived* safety factor (L_ξ measured, Δξ chosen to make m ≤
    budget).

[L1074] **FORK-24: Second-order conditions and their verification.**
  - **Recommendation.** **O1 with derived tolerance (Lanczos residual
    + discretization error model on the Hessian), O3 as an
    independent cross-check, O2 on the R0 rung.** The nonsmooth
    caveat: where the active set of phases changes, the correct
    object is a second-order condition on the *critical cone* of the
    semi-infinite program — state it in that form.

[L1113] **FORK-25: The certified upper-bound mechanism for δ.**
  - **Recommendation.** **O1 as the primary δ-carrier (it is exact in
    structure, and its slack is physically interpretable as the
    cycle-compromise cost), sharpened per-phase by O3 on the R0 rung
    and by the classical exact contours on R1; O2/O4 opportunistic.**
    Also report the *lower* branch: δ = 0 proof attempt via the
    invariance criterion above.

[L1165] **FORK-26: The global search layer (candidate generation).**
  - **Recommendation.** **O6 + O1 as the backbone (continuation from
    classical exact optima is the highest-information start), O3 in
    the discovery tier, O2 for expensive-regime refinement; O4/O5
    opportunistic. All behind the verification firewall.**

[L1207] **FORK-27: Discretization of the per-phase state.**
  - **Recommendation.** **O1/O4 in the certified-smooth supersonic
    regions (MoC as the reference organism, spectral/high-order DG
    as the workhorse), O3 where fronts are certified, O2 as the
    discovery-tier and cross-check solver.** Two independent
    discretizations (MoC vs DG) at candidates = a structural
    falsifier for solver bugs.

[L1246] **FORK-28: Mesh/refinement policy and error estimation.**
  - **Recommendation.** **O1+O4 in production, O2 at checkpoints as
    the effectivity referee; every safety factor traced to the
    measured effectivity distribution (no magic 1.25).**

[L1276] **FORK-29: Derivative computation and its verification battery.**
  - **Recommendation.** **O2 as production (consistent with FORK-17
    O3), verified by the battery: O5 duality identity (transpose
    test), O3 directional referee at randomized directions/designs
    per release, O1-vs-O2 kernel comparison on certified-smooth cases
    (doubles as the FORK-18 O1/O2 consistency check), all with
    derived tolerances from conditioning estimates.** Special
    obligations: verify *at* a fitted front (FORK-19 O1 terms) and
    *at* an active g_sep phase (constraint Jacobians), not only at
    interior smooth points.

[L1311] **FORK-30: Optimizer class and globalization.**
  - **Recommendation.** **O1 with error-aware (inexact) trust-region
    acceptance tied to FORK-28's bars, switching to O3 when the
    active inequality set is large; O2 only inside certified-smooth
    basins as an accelerator.**

[L1346] **FORK-31: Stopping criteria and tolerance derivation.**
  - **Recommendation.** **O1 for the inner loop, O4 for the program:
    the run ends when |Δδ| and |Δbars| over a window are below their
    own measurement noise (all measured).**

[L1373] **FORK-32: Handling the certification boundary in the loop.
      (HW-3, part 3.)**
  - **Recommendation.** **O2 as the doctrine (certification
    conditions = first-class constraints with margins and
    multipliers), O1 as the backstop for monitors that resist
    differentiable-margin form, O4 in the discovery tier.** This is
    the fork that turns "certified class" from a filter into a
    *priced constraint surface* — arguably the most distinctive
    structural choice of the whole formulation.

[L1419] **FORK-33: Structure of the unsteady correction bound
      (requirement (v), HW-4).**
  - **Recommendation.** **O2 at candidates as the primary carrier +
    O3 as its independent bound-form cross-check + O4 as the
    bookkeeping frame; O1 relegated to explaining the measured Δ's
    parametric trend in St (measured, per the brief).** Note the R2
    rung (co-rotating steady 3D) makes O2 cheaper than generic
    unsteady: under H-DATA, J_exact equals the R2 steady thrust
    (Proof P8), so the (v) gap is computable steady-to-steady.

[L1471] **FORK-34: H-DATA monitoring and the data-admissibility audit.**
  - **Recommendation.** **All five, cheap and always-on, with the
    failure→consequence map published as part of certificate (v);**
    O2 is the primary (assumption-free) H-DATA monitor, O1 its
    diagnostic refinement.
