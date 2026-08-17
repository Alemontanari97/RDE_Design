# ATTACK TREE — variational / optimal-control / shape-optimization lens

Deliverable for the frozen problem brief (`phaseA_problem_brief.md`).
Author lens: calculus of variations, optimal control, PDE-constrained
shape optimization. Written from the brief alone plus open literature;
no project documents consulted.

Notation. E = envelope cylinder; S = solid, Ω(S) = E \ S; Γ_d = data
interface; Λ = attachment circles; (Ξ, μ) = phase space; s(ξ) = inflow
state; F[S; s(ξ)] = per-phase steady thrust; J[S] = ∫ F dμ; J_exact =
long-time-averaged unsteady thrust; St = residence-time/period ratio
(marginal); c = geometric constraint vector; A(c) = admissible class
(uniform cone (h0, ω), attachment on Λ, g_i(S) ≤ c_i).

---

## 0. Reading of the problem from this lens

This is a **shape optimization problem with an averaged (ensemble)
objective**: one design, a μ-parametrized family of steady
compressible-Euler states, pointwise-in-parameter state constraints
(attachment), and a five-part certificate obligation (existence,
first-order, second-order, global δ-optimality, model-error bars).
Structurally it is a **semi-infinite, PDE-constrained, nonconvex,
nonsmooth program over a set variable**, with four known hard walls:

- **(HW-1) Existence:** geometric compactness of A(c) is classical
  (uniform cone ⇒ compactness, Chenais 1975), but *continuity of the
  Euler state map under domain convergence* is open for multi-D
  compressible flow. Existence must be packaged as a conditional
  theorem with a monitored failure boundary. (FORK-15, Proof P3.)
- **(HW-2) Non-uniqueness of multi-D weak solutions:** entropy
  admissibility does NOT select a unique solution for multi-D
  compressible Euler (De Lellis–Székelyhidi, Ann. Math. 2010;
  Chiodaroli–De Lellis–Kreml, CPAM 2015: non-uniqueness even from
  Riemann data). "The" state must be defined by a *certified solution
  class*, not by the PDE alone. (FORK-6.)
- **(HW-3) Nonsmoothness at the certification boundary:** J is at best
  directionally differentiable where shocks form/detach, where the
  active phase-set of the attachment constraint changes, and where
  the certification oracle flips. Multipliers of pointwise state
  constraints are measures (Casas 1986). (FORK-19/22/32.)
- **(HW-4) Marginal Strouhal:** neither the quasi-steady limit
  (St → 0) nor a frozen/scattered limit (St → ∞) is valid a priori;
  the surrogate error must be *bounded by a computed carrier*, not by
  an asymptotic series assumed convergent. (FORK-1/33, Proof P6.)

The tree below is organized as: formulation families (§1), forks in
seven layers A–G (§2), dry-level proofs P1–P8 (§3), order of battle
(§4).

---

## 1. FORMULATION FAMILIES

**FF-1 — Certified quasi-steady program (the spine).**
Per-phase steady Euler in a *certified* solution class (smooth or
piecewise-smooth with fitted fronts, membership checked by an oracle);
objective J = ∫ F dμ; shape calculus + per-phase adjoints coupled
through the shared contour (averaged Hadamard condition); globality by
certified upper bounds (interchange bound P1 + duality/relaxation);
|J_exact − J| bounded by a measured-St carrier evaluated at the
candidate optimum. Selects when: per-phase states certifiable on the
optimizer's path, and the St-carrier bound is small enough to be
useful. This is the recommended spine.

**FF-2 — Full time-periodic unsteady optimization.**
Optimize J_exact directly: time-periodic (rotating-frame) unsteady
Euler as the state, time-periodic adjoint (Nadarajah–Jameson-type
unsteady adjoint; the flow is periodic, not chaotic, so no shadowing
pathology — least-squares shadowing (Wang et al. 2013) not needed).
Gold standard for (v); cost is 10²–10⁴× FF-1 per design; existence
and adjoint well-posedness for time-periodic multi-D Euler are
strictly harder than steady. Role: **verification tier at candidate
optima only**, and the carrier for the (v) bound. Selects as primary
only if FF-1's St-carrier bound is demonstrated O(1)-large.

**FF-3 — Relaxation / convexification family.**
Replace the set variable by a relaxed object (designs as measures /
characteristic functions with convexified constraints; occupation-
measure or moment-SOS lifts of low-dimensional model rungs, Lasserre
2001; homogenization-style relaxation, Bendsøe–Kikuchi 1988) to get
*upper bounds* B ≥ sup J, hence computed δ. Not a design generator
here (no relaxation theory for compressible Euler topology
optimization exists); it is the **bound factory** for requirement
(iv). Selects always, but only in that role.

**FF-4 — Robust / risk-averse programming family.**
Replace the mean by worst-case over Ξ, CVaR_α, or distributionally
robust versions over ambiguity sets around μ (Ben-Tal–El Ghaoui–
Nemirovski 2009; Rockafellar–Uryasev 2000; Wasserstein-DRO,
Mohajerin Esfahani–Kuhn 2018). The brief fixes the mean as the
objective, so FF-4 enters (a) for the *attachment constraint*, which
is already worst-case over supp μ ("μ-a.e."), and (b) as a hedge if
H-DATA monitoring reveals data uncertainty. Selects for constraints
and for sensitivity reporting, not for J itself.

**FF-5 — Derivative-free / surrogate global family.**
Evolutionary and swarm searches (CMA-ES, Hansen 2001; differential
evolution, Storn–Price 1997; NSGA-II, Deb 2002), DIRECT (Jones et
al. 1993), design-of-experiments + kriging (EGO, Jones–Schonlau–
Welch 1998; Forrester–Sóbester–Keane 2008), Bayesian optimization
with GP posteriors (GP-UCB regret bounds, Srinivas et al. 2010; EI
consistency, Bull 2011), machine-learned surrogates (PINNs, Raissi
et al. 2019; DeepONet, Lu et al. 2021; FNO, Li et al. 2021). None of
these produces a certificate against the *continuum* problem: regret
bounds hold for the surrogate/sampled problem under GP-prior
hypotheses that cannot be verified for this physics. Role: **global
exploration layer feeding FF-1's certified local machinery and
seeding sector comparisons** (FORK-26). Selects never as the
certificate carrier; rejected in that role for a stated reason at
each relevant fork below, per the breadth requirement.

Selection criterion across families: (1) can it carry the
certificates (i)–(v)? (2) cost per certified design; (3) exposure to
HW-1..4. Only FF-1 passes (1) at acceptable (2); FF-2/FF-3 are
subordinated as the verification tier and the bound factory; FF-4/
FF-5 are subordinated as constraint-shaping and exploration.

---

## 2. FORKS

### Layer A — Objective and averaging

---

**FORK-1: How is J_exact related to the computable objective?**

- **Q.** What object does the optimizer actually maximize, and what
  is its declared relation to J_exact at marginal St?
- **Options (each at its best).**
  - **O1. Pure quasi-steady surrogate J = ∫ F dμ.** Exact in the
    St → 0 limit; cheapest; every certificate in §6 of the brief is
    natural for it.
  - **O2. Corrected surrogate J + St·J₁ with J₁ from linearized
    unsteady response.** Two-scale/averaging expansion (Sanders–
    Verhulst averaging) about the quasi-steady cycle; captures the
    first finite-St effect; still steady-adjoint-compatible if J₁ is
    treated as a frozen correction re-evaluated outside the design
    loop.
  - **O3. Optimize J_exact directly (FF-2).** No surrogate gap at
    all; time-periodic unsteady state+adjoint per design.
  - **O4. Certified-bracket objective: maximize J while carrying
    [J_exact^lo, J_exact^hi] = J ± Δ(S) with Δ a computed unsteady-
    residual bound.** Honest at marginal St where the expansion in O2
    has no smallness parameter; decision-grade because designs are
    compared with overlapping-bracket logic.
  - **O5. Statistical/ensemble objective on measure-valued or
    statistical solutions (Fjordholm–Mishra–Tadmor 2017):** treat the
    unsteady flow's time-average as an expectation over a statistical
    solution. Principled under HW-2, but no practical thrust
    calculus exists yet.
- **Criterion.** Measured magnitude of the unsteady correction at
  representative shapes: compute Δ(S) (O4 carrier) at 2–3 designs
  spanning the sectors; if Δ/J ≪ target δ/J, O1+O4 suffices; if Δ/J
  is comparable to inter-design differences, escalate to O2; if O2's
  remainder is not demonstrably smaller than its leading term
  (marginal St ⇒ plausible), escalate to O3 at candidates only.
- **Recommendation.** **O1 as optimizer objective + O4 as the
  declared relation + O3 at the final candidate(s)** (this is FF-1
  with an FF-2 verification tier). Grounds: (v) demands a *bound*,
  not an expansion; at marginal St only a computed carrier is honest
  (Proof P6); optimizing O3 throughout buys accuracy the bracket may
  show is unnecessary, at 10²–10⁴× cost.
- **Falsifier.** A single verified unsteady computation at a
  quasi-steady optimum showing J_exact outside the computed bracket
  (bound wrong) or a re-ranking of two candidate designs by O3 that
  O1's brackets declared separated (surrogate not decision-valid).

---

**FORK-2: Thrust bookkeeping — which control surface, and how does
Pa enter?**

- **Q.** F is defined on "any enclosing control surface"; which one
  is the *variational* definition, and is the choice immaterial?
- **Options.**
  - **O1. Near-field (wetted-surface) form:** F = pressure+shear
    integral on solid walls plus interface momentum flux; natural for
    Hadamard shape calculus (the design appears explicitly).
  - **O2. Far-field/exit-plane momentum-flux form:** robust to wall
    singularities (lips, corners); natural for the unsteady J_exact.
  - **O3. Arbitrary surface with a proven invariance lemma** (Proof
    P2): div(ρu⊗u + (p−Pa)I) = 0 for steady Euler ⇒ F is
    surface-independent among homologous enclosing surfaces; then use
    O1 for derivatives, O2 for evaluation, and the *difference as a
    conservation-error estimator*.
- **Criterion.** Whether the discrete state conserves momentum to a
  quantifiable residual (it decides how big the O1–O2 discrepancy
  monitor is).
- **Recommendation.** **O3.** Grounds: the invariance lemma is a
  two-line divergence-theorem argument in the continuum and its
  discrete violation is a free, derived error indicator feeding
  FORK-31 tolerances. Pa enters only through (p − Pa) on the closed
  surface — this makes F gauge-invariant to ambient pressure on
  closed surfaces and defines the free-boundary condition p = Pa
  consistently (FORK-11).
- **Falsifier.** Discrete O1 vs O2 evaluations differing by more than
  the derived conservation-residual bound on a certified state.

---

**FORK-3: Which statistic of the cycle is optimized?**

- **Q.** Mean thrust ∫ F dμ is declared; does anything force a
  risk-shaped or multi-objective reformulation?
- **Options.**
  - **O1. Mean (as briefed).**
  - **O2. Worst-phase max-min:** maximize ess-inf_ξ F; protects
    against phase-localized collapse; Danskin calculus available
    (Proof P4).
  - **O3. CVaR_α of thrust over μ** (Rockafellar–Uryasev 2000):
    interpolates O1–O2; smooth reformulation with an auxiliary
    scalar.
  - **O4. Distributionally robust mean** over an ambiguity ball
    around μ (Wasserstein-DRO): hedges H-DATA violations (mode
    transitions shift μ).
  - **O5. Multi-objective (mean, phase-variance) Pareto front**
    (NSGA-II-style or scalarized): reports the trade
    structure instead of a single design.
- **Criterion.** The brief pins O1 as the objective; O2–O5 are
  selected only as *diagnostics or constraint devices* unless the
  H-DATA monitor (FORK-34) shows μ itself is uncertain at a level
  that moves the optimum (sensitivity ∂J/∂μ · δμ compared to δ).
- **Recommendation.** **O1**, with the μ-sensitivity of J and of the
  active-phase set reported as part of certificate (v); adopt O4
  only if measured δμ (from H-DATA monitoring) times the computed
  μ-gradient exceeds the globality gap δ. Grounds: do not silently
  change the declared objective; robustness pressure is real but
  belongs in the error-bar/constraint layer here.
- **Falsifier.** Measured cycle-data drift δμ with |∂J/∂μ[δμ]| > δ
  at the certified optimum — then O1's certificate is about the
  wrong problem and O4 must be promoted.

---

**FORK-4: Discretization of the phase space (Ξ, μ).**

- **Q.** J and the μ-a.e. constraint must be computed from finitely
  many phases; how are phases chosen and the quadrature error
  carried?
- **Options.**
  - **O1. Fixed Gauss/trapezoid quadrature in ξ** (periodic ⇒
    trapezoid is spectrally accurate for smooth ξ-dependence).
  - **O2. Adaptive quadrature driven by the measured ξ-modulus of
    continuity of F and g_sep** (add phases where the cycle is
    steep — the wave-passage front).
  - **O3. Sparse/low-discrepancy sampling (QMC)** if the effective
    phase-dimension exceeds one (e.g., mode mixtures — excluded by
    H-DATA but monitored).
  - **O4. Sample-average approximation with statistical error bars**
    (Shapiro's SAA theory): treats μ as data-driven samples; natural
    if s(ξ) arrives as measurements.
  - **O5. Multilevel/multifidelity phase sampling (MLMC-style,
    Mishra–Schwab):** cheap phases on coarse meshes, few fine
    correctors.
- **Criterion.** Smoothness of ξ ↦ (F, g_sep): if a detonation-front
  passage makes the map merely Lipschitz or piecewise-smooth with a
  moving kink, O1's spectral advantage dies and O2 wins; if s(ξ) is
  empirical, O4's bars are the honest carrier.
- **Recommendation.** **O1 upgraded to O2 with a measured
  ξ-modulus**, and the quadrature error entered as a named term in
  the (v) budget and in the constraint-covering certificate
  (FORK-23). Grounds: one-dimensional periodic Ξ; the only threat is
  loss of ξ-regularity, which O2 detects by construction.
- **Falsifier.** A phase-refinement study where J or the active
  constraint set fails to converge at the rate the assumed
  ξ-regularity predicts.

---

### Layer B — State model and solution concept

---

**FORK-5: The idealization ladder for the state model.**

- **Q.** Which model rungs are used where, and what residual does
  each rung declare against the next?
- **Options (as ladder rungs, all retained; the fork is which rung
  carries which certificate).**
  - **R0. Quasi-1D (area-averaged) per-phase flow** with γ(T):
    closed-form/ODE thrust; feeds bounds (FF-3) and sanity anchors.
  - **R1. Axisymmetric steady Euler without swirl.**
  - **R1s. Axisymmetric steady Euler with swirl** (u_θ ≠ 0; the
    brief's "flow angle" includes azimuthal components sweeping the
    cycle): adds the centrifugal term and swirl-modified
    characteristics; thrust and attachment are swirl-sensitive.
  - **R2. Steady 3D Euler on the rotating-wave helical symmetry:**
    the pure rotating wave is steady in the co-rotating frame — an
    *exact* reformulation of the unsteady problem under H-DATA
    (helical symmetry reduction), at 3D cost.
  - **R3. Unsteady axisymmetric/3D Euler:** the verification tier
    (FF-2).
  - **Rv. Declared viscous layer** (integral boundary layer or RANS
    correction) feeding only g_sep and a thrust-decrement residual.
- **Criterion.** Certificate assignment: the optimizer's state must
  be the *cheapest rung whose declared residual against the rung
  above is inside the (v) budget*. Swirl retention (R1 vs R1s) is
  decided by a one-shot comparison: |F_R1s − F_R1| and
  |g_sep,R1s − g_sep,R1| at representative phases vs the budget.
- **Recommendation.** **R1s as the optimization state** (swirl is
  part of the given data and enters at zero extra dimensionality),
  R0 for bound generation, R2 as a structural cross-check of the
  quasi-steady picture (it is the exact steady object under H-DATA
  — a rare gift; use it to calibrate the FORK-1 bracket), R3 at
  candidates, Rv only through g_sep. Grounds: each certificate gets
  the cheapest honest carrier; R2 is this problem's special
  structure and should not be left unused.
- **Falsifier.** R1s-vs-R2 thrust discrepancy at a certified design
  exceeding the declared quasi-steady bracket (would indict the
  per-phase decomposition itself, not just finite-St).

---

**FORK-6: Solution concept for the per-phase multi-D Euler state.
(HW-2 lives here.)**

- **Q.** In what class does "the" state live, given genuine
  non-uniqueness of entropy weak solutions in multi-D?
- **Options.**
  - **O1. Certified smooth (shock-free) class:** design constrained
    so each phase's flow is C¹ in Ω(S) (supersonic expansion without
    embedded shocks); uniqueness and stability by classical
    quasilinear hyperbolic theory in the supersonic (space-like
    marching) region; certification = a computable smoothness/
    characteristic-overlap monitor.
  - **O2. Piecewise-smooth with fitted fronts:** finitely many
    fitted shocks/contacts with Rankine–Hugoniot + Lax conditions;
    local uniqueness/stability via Majda's multi-D shock stability
    (Majda 1983; Métivier's refinements) under the uniform-stability
    condition; transonic-shock-in-nozzle rigidity results
    (Chen–Feldman, JAMS 2003 ff.) as structural anchors.
  - **O3. Entropy weak solutions (capturing):** what an FV/DG code
    computes; but HW-2 says the class does not pin the object —
    admissible only with an *added selection principle* declared.
  - **O4. Vanishing-viscosity selection:** define the state as the
    ν → 0 limit of Navier–Stokes; physically canonical, proven only
    in 1D (Bianchini–Bressan 2005); in multi-D it is a *declared
    conjecture-level selection*, monitorable by ν-refinement studies.
  - **O5. Measure-valued / statistical solutions (DiPerna 1985;
    Fjordholm–Mishra–Tadmor 2017):** embraces non-uniqueness;
    certificates become statements about statistics; shape calculus
    on these objects is unexplored.
  - **O6. Entropy-rate admissibility (Dafermos):** maximal entropy
    production selection; attractive but not proven selective in
    multi-D, and not computable as a certificate.
- **Criterion.** A solution concept is admissible only if (a) it
  supports a certification oracle (membership decidable from the
  computed state with derived tolerances), (b) it supports shape
  calculus (FORK-18/19), (c) uniqueness holds *within the class* or
  a selection is declared.
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
- **Falsifier.** An optimizer trajectory forced into states failing
  both O1 and O2 certification (e.g., unstable bifurcating shock
  patterns) on all sectors — would force O4/O5 research-grade
  machinery and downgrade certificate (i)–(iii) claims.

---

**FORK-7: Per-phase non-uniqueness of the *flow configuration*
(hysteresis) and the selection principle.**

- **Q.** Even within a certified class, steady nozzle flows admit
  multiple configurations for the same (S, s(ξ)) (shock position /
  separation hysteresis, over- vs under-expanded branches). Which
  branch defines F[S; s(ξ)]?
- **Options.**
  - **O1. Continuation in ξ:** the branch continuous along the cycle
    starting from a declared anchor phase; matches the physical
    quasi-steady sweep; makes F single-valued unless a fold is hit.
  - **O2. Unsteady-limit selection:** define the per-phase state as
    the long-time limit of the unsteady problem with frozen data;
    canonical but costs an unsteady solve per phase.
  - **O3. Performance-pessimal branch (min over branches):**
    conservative certificate.
  - **O4. Declare fold-crossing designs uncertifiable:** exclude
    from the certified class any design whose cycle path crosses a
    fold (branch jump) — hysteresis then never enters F.
- **Criterion.** Presence of folds inside A(c) ∩ {certified}: a
  continuation study in ξ at representative designs (monitor the
  state-Jacobian's smallest singular value along the cycle).
- **Recommendation.** **O1 + O4**: continuation defines the branch;
  a fold-margin monitor (distance of the cycle path to the fold set,
  via the measured inf_ξ σ_min of the linearized steady operator)
  joins the certification oracle. Grounds: single-valued F with a
  computable exclusion boundary beats averaging over an undeclared
  branch choice; O2 is kept as the referee when O1's anchor is
  ambiguous.
- **Falsifier.** A certified design where O1 and O2 select different
  branches at some phase (continuation not physical) — promotes O2
  to the definition at re-derived cost.

---

**FORK-8: Closure where the axial inflow on Γ_d is subsonic.**

- **Q.** Complete data is prescribed only where axial flow is
  supersonic; the brief demands an explicit closure elsewhere. Which
  closure?
- **Options.**
  - **O1. Characteristic-count closure:** prescribe exactly the
    incoming Riemann/characteristic variables per the sign structure
    of the axial characteristic speeds (4 incoming + 1 outgoing for
    subsonic-axial inflow in 3D Euler; the outgoing one — typically
    the upstream-running acoustic invariant — is *read from the
    interior solve*); the given s(ξ) supplies the incoming set.
  - **O2. Total-state closure:** prescribe (p₀, T₀ or h₀, angles),
    let static state float; classical, robust, but a *modeling
    choice* about what the combustor fixes.
  - **O3. Impedance/back-reaction closure:** a declared acoustic
    impedance of the combustor at Γ_d; most physical, but violates
    the causal-separation premise unless the impedance is part of
    the given data.
  - **O4. Push Γ_d downstream** until axial supersonicity holds for
    all ξ (re-cut the interface); dissolves the fork where the data
    allow it.
- **Criterion.** The causal-separation audit: the closure must not
  let the design influence the data (O3 fails unless impedance is
  data); well-posedness of the linearized per-phase problem with the
  chosen closure (energy/Kreiss condition check).
- **Recommendation.** **O4 where the data family permits; else O1
  with the incoming set derived from s(ξ) and the closure stated as
  hypothesis H-CLOSURE alongside H-DATA**, monitored by comparing
  the reflected invariant computed by the solver against the data
  family's implied one. Grounds: O1 is the unique closure that is
  both well-posed by construction and honest about what is assumed.
- **Falsifier.** Monitored mismatch of the outgoing invariant at Γ_d
  beyond derived tolerance across the cycle (closure inconsistent
  with the data family ⇒ causal separation broken or H-DATA false).

---

**FORK-9: Thermally-perfect γ(T) thermodynamics — exact treatment
vs surrogates.**

- **Q.** How do h(T), cp(T) enter the state solve, characteristics,
  jump conditions, and adjoints?
- **Options.**
  - **O1. Exact thermally-perfect relations throughout:** entropy/
    enthalpy integrals of cp(T)/T; speed of sound a² = γ(T) R T with
    local γ; Prandtl–Meyer and R–H relations generalized (numerical
    quadrature of the characteristic ODEs instead of γ-const closed
    forms).
  - **O2. Piecewise-polynomial (NASA-style) caloric fits with
    derived fit-error propagation** into F and g_sep.
  - **O3. Local-γ freeze per phase (γ evaluated at a reference T per
    ξ):** closed forms retained; a declared model residual per
    phase.
  - **O4. Tabulated equation-of-state with certified interpolation
    error** (monotone splines + error bound).
- **Criterion.** Propagated objective error: |∂F/∂(thermo)| times
  the surrogate's certified sup-error must sit inside the (v)
  budget; adjoint consistency requires the *same* thermodynamic
  callable (and its exact derivative) in state and adjoint.
- **Recommendation.** **O2/O4 (they are the same decision at
  different smoothness) with certified interpolation error and AD-
  differentiable evaluation; O3 rejected as the state model**
  (γ-variation across an RDE cycle is a first-order thrust effect,
  and the brief pins γ ≠ const) **but retained as the bound-factory
  thermodynamics (R0 rung)** where its error is absorbed into the
  bound's slack. Grounds: exactness where certificates live,
  closed forms where only bounds live.
- **Falsifier.** A γ-refinement study (fit order ↑) moving J by more
  than the declared thermo term in the (v) budget.

---

**FORK-10: Sonic set / throat treatment.**

- **Q.** The per-phase flow generically contains a sonic surface
  (choking) whose position moves with ξ; the steady operator changes
  type there. How is it treated analytically and numerically?
- **Options.**
  - **O1. Transonic-regular certification:** require each phase's
    sonic surface to be a regular space-like-to-time-like transition
    with nonvanishing streamwise acceleration (Sauer 1947 / Hall
    1962 local expansions as the certificate template); monitor the
    non-degeneracy quantity (∂M/∂arclength at M=1 bounded below).
  - **O2. Global elliptic-hyperbolic coupled solve** (transonic full
    potential/Euler with embedded type change; Chen–Feldman-type
    theory as the rigor anchor): no special certification, but the
    solver and the shape calculus must survive the type boundary.
  - **O3. Domain decomposition at a fitted sonic surface:** subsonic
    reservoir side solved elliptically, supersonic side by marching
    (MoC), matched at the fitted sonic line — the classical nozzle
    pipeline; sonic surface becomes an internal free boundary with
    its own shape calculus.
  - **O4. Supersonic-throughout restriction:** if the annular exit
    data are axially supersonic for all ξ (RDE exhausts often are),
    the sonic fork dissolves; certify *that* instead.
- **Criterion.** The data: measured min over ξ of the axial Mach on
  Γ_d. If ≥ 1 + margin, O4. Else the mover is differentiability:
  the design derivative must include sonic-surface motion terms;
  O3 makes them explicit, O2 buries them in the solver.
- **Recommendation.** **O4 if the data support it (check first —
  cheapest fork-kill available); else O3 with the sonic surface as a
  fitted internal boundary and O1's non-degeneracy monitor as part
  of certification.** Grounds: fitted free boundaries keep the
  shape calculus classical (transmission conditions), and choking
  non-degeneracy is exactly what protects differentiability of F in
  both S and ξ.
- **Falsifier.** A phase family where the sonic non-degeneracy
  margin → 0 inside A(c) (grazing choking): F becomes non-Lipschitz
  in ξ there, breaking FORK-4's quadrature certificate — the
  monitor firing is the falsifier and re-routes to O2.

---

**FORK-11: Plume / free-jet boundary ("ambient pressure on free
portions").**

- **Q.** Is the constant-pressure free boundary (p = Pa) part of the
  state problem (a free-boundary Euler problem), or truncated?
- **Options.**
  - **O1. Full free-boundary state:** jet boundary as unknown
    surface with p = Pa and kinematic condition; required for plug/
    aerospike sectors where the plume wets the design physics;
    shape calculus gains a free-boundary transmission term.
  - **O2. Truncation at the nozzle exit with supersonic-outflow
    extrapolation:** valid when the exit flow is axially supersonic
    everywhere (downstream influence nil); F evaluated on the exit
    plane (FORK-2 invariance makes this exact in the continuum).
  - **O3. Truncation + far-field sponge on E's outlet:** numerical
    convenience; introduces a declared, measurable reflection
    residual.
  - **O4. Hodograph/characteristic exact jet treatment (classical
    free-streamline theory):** exact for 2D; only partial tools for
    axisymmetric — use as verification anchors, not as the pipeline.
- **Criterion.** Sector-dependence: bell-type sectors with fully
  supersonic exits ⇒ O2 exact; plug/E-D sectors have subsonic
  pockets or base regions interacting with the plume ⇒ O1 becomes
  load-bearing.
- **Recommendation.** **O2 by default with a per-phase certificate
  of exit supersonicity; automatic escalation to O1 in sectors where
  that certificate fails.** Grounds: pay the free-boundary cost only
  where the topology sector demands it; the escalation trigger is
  itself a computable monitor.
- **Falsifier.** In a claimed-O2 sector, extending the domain and
  finding F changes beyond the discretization budget (downstream
  influence present ⇒ certificate was wrong).

---

**FORK-12: Separation margin g_sep — which detection model?**

- **Q.** The state model is inviscid, but attachment is a viscous
  phenomenon; the brief demands an *explicit criterion*.
- **Options.**
  - **O1. Inviscid pressure-based criteria:** wall-pressure ratio
    thresholds (Summerfield-type p_w/Pa bounds; Schmucker/Frey–
    Hagemann-refined criteria from the nozzle side-load literature,
    Östlund–Muhammad-Klingmann 2005 review) — algebraic in the Euler
    wall solution; crude but certifiable and differentiable.
  - **O2. Adverse-pressure-gradient integral criteria:** Stratford
    (1959) / Buri-type integral of the wall pressure gradient along
    the wetted contour; still Euler-computable, more physical
    ordering of designs.
  - **O3. Coupled integral boundary-layer (IBL) margin:** e.g.,
    Thwaites/Head or a compressible integral method marched on the
    Euler wall data; g_sep = min over arclength of a shape-factor
    margin; differentiable through the IBL ODE adjoint.
  - **O4. RANS-informed margin at checkpoints:** high-fidelity
    separation check at candidate designs only; not in the loop.
  - **O5. Data-driven separation classifier with conformal
    calibration:** ML margin trained on RANS/experiment with
    distribution-free error quantiles; per the breadth requirement —
    rejected in the certificate role because its validity domain
    cannot be tied to the design class by proof, admitted only as a
    cheap pre-screen.
- **Criterion.** Monotone consistency: the chosen g_sep must
  provably (or at least measuredly) order designs the same way the
  checkpoint tier (O4) does near the constraint boundary; plus
  differentiability (enters the KKT system with a multiplier
  carrying marginal-thrust-per-margin meaning).
- **Recommendation.** **O3 in the loop (IBL margin: physical,
  cheap, adjoint-capable), O1 retained as an outer conservative
  envelope (two-sided: certified designs must pass both), O4 as the
  checkpoint falsifier-carrier.** Grounds: a pure O1 threshold makes
  the *constraint boundary* a modeling artifact with O(1) crudeness
  exactly where multipliers must carry marginal-value meaning.
- **Falsifier.** An O4 checkpoint showing separation on a design
  with positive O3 margin (margin model unsafe ⇒ recalibrate or
  tighten the O1 envelope; the safety factor becomes *derived* from
  the measured O3-vs-O4 discrepancy population).

---

### Layer C — Design representation and admissible class

---

**FORK-13: Representation of the solid set S.**

- **Q.** Which mathematical description of S carries (a) the
  existence class, (b) the computation, (c) the shape calculus?
- **Options.**
  - **O1. Boundary graphs/splines per topology sector:** wetted
    contour as B-spline/monotone-parametrized curves; industry
    standard (Hicks–Henne bumps; CST, Kulfan 2008; FFD, Sederberg–
    Parry 1986); smallest search space; ties topology down.
  - **O2. Level-set representation** (Osher–Sethian 1988; Allaire–
    Jouve–Toader 2004): S = {φ ≤ 0}; topology-capable; Hadamard
    velocity fields drive evolution; needs reinitialization
    discipline; curvature/angle constraints become nontrivial
    functionals of φ.
  - **O3. Phase-field / density (SIMP-like) topology optimization**
    (Bendsøe 1989; fluids: Borrvall–Petersson 2003 for Stokes):
    porosity-penalized momentum sinks; per the breadth requirement —
    **rejected as certificate carrier** because a Brinkman-type
    penalization of *compressible Euler* has no convergence theory
    (slip walls and shocks vs porous smearing) and its intermediate
    densities are unphysical for gas dynamics; admissible only as a
    sector-discovery heuristic feeding FORK-14.
  - **O4. Diffeomorphism/transformation approach:** S = T_θ(S_ref),
    θ in a Banach/Hilbert space of displacement fields (Murat–Simon
    1976 framework); clean function-space optimization and Hessian
    calculus; fixed topology per reference.
  - **O5. Sets of finite perimeter (geometric measure theory):**
    maximal generality for existence; too weak for Euler trace
    theory (slip BC needs Lipschitz-or-better boundaries);
    rejected as the working class, retained as the ambient space in
    which the cone-condition class embeds.
  - **O6. Polynomial/algebraic boundaries (moment-friendly):**
    enables FF-3 SOS bounds on low rungs; not expressive enough as
    the primary class.
- **Criterion.** Compatibility triple: existence class (needs
  uniform cone ⇒ uniformly Lipschitz boundaries), state solver
  (needs fitted boundaries for certified classes — FORK-6), and
  shape calculus (needs at least C^{1,1} pieces for Hadamard forms
  with curvature terms). Plus: can the constraint vector c
  (curvature/angle bounds) be imposed *exactly*?
- **Recommendation.** **Two-tier: O2 (level-set on E) as the
  *sector-discovery* tier with the cone/curvature constraints
  enforced by constrained redistancing; then O1/O4 (spline graph +
  transformation calculus) as the *certificate* tier within each
  discovered sector.** Grounds: the brief makes topology an output
  (needs O2-or-O3-type freedom) but certificates (ii)–(iii) need
  the smooth parametric calculus (O4's function-space structure);
  no single representation serves both today — this is a genuine
  two-tier fork, not a compromise.
- **Falsifier.** A sector found by the O2 tier that cannot be
  realized inside the O1/O4 certificate tier within the constraint
  vector c (representation gap) — would force widening the
  certificate-tier class (e.g., NURBS with corner points and a
  corner calculus).

---

**FORK-14: Topology sectors — enumerate, or let the representation
discover them?**

- **Q.** Bell/plug/shrouded/E-D are outputs; how does the program
  traverse topology classes with certificates?
- **Options.**
  - **O1. A priori sector enumeration:** run the certificate tier in
    each classical sector (bell, plug, shrouded plug, E-D, annular),
    compare certified J values; globality over topology by
    exhaustion over the declared sector list.
  - **O2. Topological-derivative-driven insertion** (Sokolowski–
    Żochowski 1999; Novotny–Sokolowski): nucleate solid/void where
    the topological gradient indicates; principled but the
    topological derivative for *compressible Euler with slip walls*
    is not in the literature — would need derivation (a paper-sized
    lemma), and shock interaction with a nucleated obstacle is
    outside current theory.
  - **O3. Level-set free evolution (FORK-13 O2 tier)** with
    merging/pinching allowed: discovers sectors dynamically;
    no certificate that all relevant sectors are visited.
  - **O4. Evolutionary/global search over a topology-encoding
    genome** (graph grammars, constructive solid geometry genomes):
    breadth-required option; rejected for certificates (no
    guarantee of coverage or optimality) but strong as a sector
    *proposer* alongside O3.
  - **O5. Branch-and-bound over sectors with FF-3 upper bounds:**
    certify sector exclusion by bounding sup J within a sector below
    the incumbent's certified J (sector-restricted interchange
    bound, Proof P1 applied per sector).
- **Criterion.** Requirement (iv): globality must cover topology.
  Only O1+O5 produce sector-level certificates; O2/O3/O4 only
  produce candidates.
- **Recommendation.** **O1 as the floor (declared sector list =
  hypothesis of the globality claim), O3/O4 as proposers that can
  only *add* sectors, O5 to prune sectors cheaply.** Grounds: an
  explicit, falsifiable hypothesis ("the optimum lies in one of the
  listed sectors, or the proposers would have found otherwise")
  beats an unprovable claim of representation completeness.
- **Falsifier.** A proposer (O3/O4) producing an out-of-list sector
  whose certified J beats the incumbent — the sector-list hypothesis
  is refuted and the globality certificate re-issues on the enlarged
  list.

---

**FORK-15: Existence framework and its monitored failure boundary.
(HW-1 lives here.)**

- **Q.** What compactness + continuity structure makes argmax J
  exist over A(c), and what exactly can fail?
- **Options.**
  - **O1. Cone-property compactness + conditional state
    continuity:** A(c) with uniform cone (h0, ω) is compact for
    Hausdorff-complementary convergence (Chenais 1975; Henrot–
    Pierre); IF the certified-class state map S ↦ U(S; ξ) is
    continuous (in L¹_loc, say) along that convergence for μ-a.e. ξ
    with |F| dominated, THEN J is u.s.c. (or continuous) and a
    maximizer exists (Proof P3). The IF is the honest open part:
    prove it *within the certified class* via uniform characteristic
    estimates; monitor its failure.
  - **O2. Capacity-constraint frameworks (Šverák 1993, Bucur–
    Buttazzo):** designed for elliptic Dirichlet problems in 2D;
    wrong tools for hyperbolic slip-BC flow — rejected with that
    stated reason.
  - **O3. Relaxed existence (FF-3):** existence in a completed/
    relaxed class (measures, statistical states) is easy; but then
    S* may not be a set — acceptable only if a recovery theorem
    (relaxed optimum = classical set) is proven; none is available
    for Euler.
  - **O4. Existence by discretization + Γ-limit:** prove existence
    of discrete optima (finite-dimensional, trivial) and show
    Γ-convergence of discrete J to continuum J; converts HW-1 into
    a solver-consistency obligation; Γ-limit for shock-capturing
    schemes under domain variation is itself open, but *within the
    certified smooth class* it reduces to standard consistency +
    compactness — tractable.
  - **O5. No-existence stance:** optimize anyway, report sup as a
    limit of certified values; rejected because requirement (i)
    explicitly asks for the structure or the failure boundary — O5
    provides neither.
- **Criterion.** Which option yields a *theorem with checkable
  hypotheses* plus a *monitor* for the unprovable part.
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
- **Falsifier.** A maximizing sequence of certified designs whose J
  increases while the state-stability monitor diverges (Lipschitz
  constant of S ↦ U blowing up) — existence genuinely failing at
  the certification boundary; the program then reports the sup-value
  bracket instead of an argmax, as the brief's (i) permits.

---

**FORK-16: Encoding the constraint vector c (curvature, angle,
envelope, wetted length) in the working representation.**

- **Q.** Exact hard constraints, penalization, or projection?
- **Options.**
  - **O1. Hard constraints in the parametrization** (spline spaces
    engineered so bounds are linear/box constraints — e.g., B-spline
    hodograph control points bounding slope/curvature by convex
    hull): exact, optimizer-friendly, slightly conservative (convex-
    hull slack).
  - **O2. Nonlinear constraint functions g_i(S) with multipliers:**
    exact activity detection, marginal values (matches (ii)'s
    demand that multipliers carry meaning), needs constraint
    derivatives.
  - **O3. Penalty/augmented-Lagrangian:** simple; multiplier meaning
    recovered only in the AL limit; tolerance derivation awkward.
  - **O4. Projection onto A(c) each iterate** (e.g., constrained
    redistancing in the level-set tier): keeps every iterate
    feasible; projection nonsmoothness enters the convergence
    theory.
- **Criterion.** Certificate (ii) requires multipliers with
  marginal-value meaning for *active* geometric constraints; the
  encoding must expose them.
- **Recommendation.** **O2 for the certificate tier (with O1's
  convex-hull bounds used as a feasible-start/trust region), O4 for
  the discovery tier.** Grounds: marginal values of L, R_E, angle
  bounds are themselves deliverables (they price the envelope).
- **Falsifier.** Multiplier estimates failing the finite-difference
  marginal-value test dJ*/dc_i ≈ λ_i beyond derived tolerance.

---

### Layer D — Optimality system

---

**FORK-17: Optimize-then-discretize (OtD) vs discretize-then-
optimize (DtO).**

- **Q.** Is the KKT/adjoint system derived at the continuum level
  and then discretized, or is the discrete objective differentiated
  exactly?
- **Options.**
  - **O1. OtD (continuous adjoint):** the (ii) certificate *is* a
    continuum statement (averaged Hadamard/Rao-type wall condition,
    transversality at the lip); mesh-independent optimality
    language; risk: discrete gradient inconsistency (optimizer
    stalls at spurious points at fixed h).
  - **O2. DtO (discrete adjoint / AD):** exact gradients of the
    computed J to machine precision (Griewank–Walther; Giles–Pierce
    2000 duality); optimizer-consistent; risk: certifies optimality
    of the *discrete* problem — the continuum claim needs a
    separate consistency limit; also differentiates *through*
    limiters/shock capturing where the continuum derivative does
    not exist (HW-3).
  - **O3. Dual-consistent discretization (both at once):** choose
    discretizations (e.g., dual-consistent SBP/DG; Hicken–Zingg,
    Hartmann) whose discrete adjoint converges to the continuous
    adjoint; the two forks' answers coincide up to certified error.
  - **O4. Derivative-free optimization (no adjoint at all):** BO/
    CMA-ES on the certified evaluator; per breadth — rejected as
    primary because (ii) demands the optimality *system*, not just
    an optimum, and DFO scales poorly past ~50 parameters; retained
    inside FORK-26's exploration layer.
- **Criterion.** Requirement (ii) fixes the target language as
  continuum; requirement "every tolerance derived" demands the
  discrete-continuum gap be *measured*, which only O3 makes cheap.
- **Recommendation.** **O3: dual-consistent DtO whose limit is the
  OtD system, with the continuous KKT residual evaluated a
  posteriori as a certificate** (the discrete optimum is fed into
  the continuum optimality system and the residual is a named error
  term). Grounds: this is the only option where (ii) and the
  computation certify each other.
- **Falsifier.** Measured continuum-KKT residual at the discrete
  optimum not converging under mesh refinement at the scheme's
  design order (dual inconsistency in practice).

---

**FORK-18: Form of the shape derivative.**

- **Q.** Boundary (Hadamard) form, volume (distributed) form, or
  transformation derivative?
- **Options.**
  - **O1. Hadamard boundary form:** dJ[θ] = ∫_Γ_w G (θ·n) dA with a
    scalar kernel G on the wetted wall (Hadamard 1908; Delfour–
    Zolésio; for slip-wall Euler the kernel involves wall pressure
    adjoint terms — cf. Jameson 1988, Giles–Pierce): minimal
    information, exposes the *averaged wall condition* ∫_Ξ G_ξ dμ =
    (multiplier terms) demanded by (ii); needs boundary regularity
    (C^{1,1}) and smooth states near the wall.
  - **O2. Volume/distributed form:** dJ as a domain integral against
    ∇θ; weaker regularity requirements, better discrete accuracy
    (well-documented superiority under mesh nonsmoothness), but
    hides the wall condition.
  - **O3. Transformation (material-derivative) calculus on T_θ:**
    the clean route to *second* derivatives (FORK-24) and to
    function-space optimization structure.
- **Criterion.** Not exclusive — the fork is which form carries
  which certificate: (ii) wants O1's kernel explicitly; numerics
  wants O2; (iii) wants O3.
- **Recommendation.** **Derive O3 as the master object; obtain O2
  for computation and O1 by integration by parts *when the state is
  certified-smooth near the wall*, and state (ii) in the O1 form.**
  Grounds: standard equivalence chain, each link used where valid;
  the O2→O1 integration by parts fails exactly where certification
  fails, which keeps the certificate honest.
- **Falsifier.** O1-vs-O2 discrete gradient discrepancy exceeding
  the derived quadrature/regularity error model on certified
  designs.

---

**FORK-19: Differentiability across embedded discontinuities.
(HW-3, part 1.)**

- **Q.** If a certified state contains fitted shocks/contacts or a
  sonic free boundary, is J differentiable in S, and how is the
  derivative computed correctly?
- **Options.**
  - **O1. Shock-fitted linearization:** linearize state + front
    positions jointly; internal boundary (R–H) linearized
    conditions; adjoint carries an internal adjoint BC along the
    shock (Giles–Pierce adjoint shock condition; Baeza–Castro–
    Palacios–Zuazua 2009 for 2D Euler; 1D theory: shift-
    differentiability, Bressan–Guerra 1997; Ulbrich 2002/2003 for
    the adjoint framework in conservation laws). Restores genuine
    differentiability of F within the piecewise-smooth class.
  - **O2. Captured-shock AD gradients:** differentiate through the
    capturing scheme; known O(1) error against the true sensitivity
    at fixed resolution unless the scheme's numerical viscosity is
    itself convergent in the sensitivity sense (Proof P7 gives the
    scaling argument); usable only with demonstrated grid-
    convergence of gradients.
  - **O3. Avoid the issue (certified shock-free class only,
    FORK-6 O1):** derivative theory classical; restricts the design
    class.
  - **O4. Nonsmooth calculus:** treat J as directionally
    differentiable / Clarke-subdifferentiable at class-transition
    designs; bundle or semismooth methods.
- **Criterion.** Whether optimal certified designs actually contain
  fronts (measured on the optimizer path per sector). If shock-free
  optima dominate (classical thrust argument, FORK-6), O3 covers
  the endgame and O1 is needed only in transit.
- **Recommendation.** **O3 as the target class + O1 machinery
  implemented for transit and for sectors where fronts are
  unavoidable (e.g., E-D pluming); O2 rejected as a certificate
  gradient (P7) but allowed in the discovery tier; O4 held for the
  certification boundary itself (FORK-32).**
- **Falsifier.** A sector whose certified optimum retains an
  embedded front with active thrust contribution — then O1 is
  load-bearing there and its adjoint-shock implementation must pass
  the FORK-29 verification battery at the front.

---

**FORK-20: Adjoint construction and the averaged optimality system.**

- **Q.** One adjoint per phase, coupled through the shared shape —
  what exactly is the per-phase adjoint problem and the averaged
  wall condition?
- **Options.**
  - **O1. Per-phase continuous adjoint Euler:** for thrust, adjoint
    slip-type wall BC (adjoint velocity normal component tied to
    the thrust direction n_x), adjoint characteristics run
    *upstream* (well-posed marching in supersonic zones), adjoint
    outflow/inflow duals of FORK-8's closure; averaged optimality:
    ∫_Ξ G_ξ[S](x) dμ(ξ) + Σ_i λ_i ∂g_i/∂S(x) + ⟨η, ∂g_sep/∂S⟩ = 0
    on the free wall (η the attachment multiplier measure on
    Ξ × wall), i.e., **the classical Rao/Guderley–Hantsch wall
    condition holds only in μ-average** — the structural signature
    of this problem.
  - **O2. One adjoint of the μ-integrated Lagrangian:** identical in
    the continuum (linearity of ∫dμ), but discretely it fixes the
    quadrature *before* dualization — the DtO-consistent ordering;
    interchange justified by dominated convergence (Proof P5's
    hypothesis set).
  - **O3. Stochastic/sampled adjoint (SAA):** phases sampled,
    gradient = sample mean of per-phase adjoint gradients; variance
    bars by CLT; only relevant if FORK-4 chooses O4.
  - **O4. Reduced-order / surrogate adjoints (ML or POD):** breadth
    option; rejected for certificates (uncontrolled consistency),
    admitted as preconditioners.
- **Criterion.** Discrete-continuum commutation (FORK-17 O3 makes
  O1 and O2 agree to certified error); phase-count economics
  (adjoint cost scales with quadrature nodes — pairs with FORK-4).
- **Recommendation.** **O2 for computation, O1 as the certificate
  statement (the averaged wall condition + FORK-8 dual closure +
  adjoint front conditions where FORK-19 O1 is active).**
- **Falsifier.** Adjoint-gradient verification battery (FORK-29)
  failing at derived tolerance on any certified configuration; or
  the averaged-wall-condition residual not vanishing at optimizer
  convergence at the predicted rate.

---

**FORK-21: Transversality / endpoint conditions.**

- **Q.** What first-order conditions hold at the contour's free
  endpoints (nozzle lip, plug tip, free ends not pinned by Λ) and
  at the attachment set?
- **Options.**
  - **O1. Classical variable-endpoint transversality:** free lip
    position ⇒ natural boundary condition linking the endpoint
    kernel to the active length/envelope multipliers — the averaged
    generalization of Rao's lip condition (Rao 1958 derived exactly
    such an endpoint condition via control-surface transversality;
    Guderley–Hantsch equivalent). At Λ: pinned endpoints, no
    condition (constraint takes it).
  - **O2. Corner/kink conditions (Weierstrass–Erdmann analogues):**
    if the class admits corners (spline knots with angle activity),
    matching conditions on the kernel across the corner; needed the
    moment angle bounds go active.
  - **O3. Free-boundary endpoint at plume detachment:** where the
    wetted contour meets the p = Pa free boundary (plug sectors),
    a Young's-angle-like condition couples FORK-11 O1's
    transmission term with the endpoint kernel.
  - **O4. No endpoint conditions (fully pinned parametrizations):**
    simplest; forfeits part of (ii)'s content and can hide active
    optimality at the lip inside parametrization artifacts —
    rejected as the certificate form for that reason, allowed as an
    intermediate computational restriction.
- **Criterion.** Which endpoints are actually free in A(c) after Λ
  and c are imposed (a bookkeeping pass per sector).
- **Recommendation.** **O1+O2+O3 derived once in the transformation
  calculus (FORK-18 O3 gives them mechanically as boundary terms),
  each stated in μ-averaged form.**
- **Falsifier.** Numerical optimum with an endpoint kernel residual
  that refinement does not send to zero while the endpoint is
  declared free (missing condition, or hidden constraint activity).

---

**FORK-22: Machinery for the attachment state constraint. (HW-3,
part 2.)**

- **Q.** g_sep(S; s(ξ)) ≤ 0 for μ-a.e. ξ (and pointwise along the
  wall): a state constraint with measure multipliers — how is it
  imposed and dualized?
- **Options.**
  - **O1. Moreau–Yosida regularization** (Ito–Kunisch): smooth
    penalization with path-following in the penalty parameter;
    multiplier measure recovered in the limit; tolerance derivation
    clean (penalty ↔ feasibility residual).
  - **O2. Semismooth Newton / primal-dual active set**
    (Hintermüller–Ito–Kunisch 2002): mesh-independent local
    superlinear convergence; exposes the active set (which phases
    and wall stations bind) — exactly the marginal-value
    information (ii) wants.
  - **O3. Interior-point with state-constraint barriers:** robust
    globalization, multiplier meaning at the central-path limit.
  - **O4. Constraint aggregation (KS, Kreisselmeier–Steinhauser
    1979; p-norm, Kennedy–Hicken):** replaces the semi-infinite
    constraint with one smooth scalar; conservative with derived
    aggregation error; loses the resolved active set.
  - **O5. Exact semi-infinite programming (exchange/cutting-plane,
    Hettich–Kortanek 1993):** finite adaptive constraint sets with
    covering certificates — pairs with FORK-23.
- **Criterion.** (ii) demands multipliers with marginal-value
  meaning ⇒ the method must produce a convergent multiplier
  (measure) estimate; regularity of the multiplier (density vs
  singular part on the active set boundary — Casas 1986) decides
  O1-vs-O2 conditioning.
- **Recommendation.** **O2 wrapped in O1 path-following (standard
  state-constraint practice), with O4 only as the optimizer's
  early-phase smoother and its aggregation error carried
  explicitly.**
- **Falsifier.** Multiplier estimates oscillating without measure-
  convergence under refinement (regularity worse than assumed ⇒
  strengthen regularization, weaken the claimed multiplier
  regularity in (ii)).

---

**FORK-23: Aggregation over phases — certifying "μ-a.e." from
finitely many phases.**

- **Q.** The computed constraint holds at quadrature phases; the
  certificate must hold μ-a.e. How is the gap closed?
- **Options.**
  - **O1. Modulus-of-continuity covering:** measure a Lipschitz/
    Hölder bound of ξ ↦ g_sep (finite differences across refined
    phase grids, validated against the ξ-derivative from the
    unsteady-linearized solve), then finite phases + margin
    m ≥ L_ξ · Δξ/2 certify the continuum constraint.
  - **O2. Adaptive exchange method (FORK-22 O5):** add the measured
    worst phase (maximizer of g_sep found by 1D global search in ξ
    — cheap) until margin; the 1D search is certifiable by
    Lipschitz global optimization (Piyavskii–Shubert) with the same
    measured L_ξ.
  - **O3. Probabilistic guarantee (scenario approach, Calafiore–
    Campi):** sample phases, get P_μ(violation) ≤ ε with
    confidence; per breadth — rejected because "μ-a.e." is a hard
    constraint here (certified class exit), not a chance
    constraint; retained for reporting only.
  - **O4. Interval/Taylor-model enclosure of g_sep over ξ-cells:**
    rigorous but requires arithmetic-level access to the solver —
    disproportionate.
- **Criterion.** Whether a trustworthy L_ξ is measurable (FORK-10's
  sonic non-degeneracy and FORK-7's fold margin are exactly what
  keep ξ ↦ g_sep Lipschitz).
- **Recommendation.** **O1+O2 combined:** exchange to find the
  binding phases, covering to certify between them; margin m becomes
  a *derived* safety factor (L_ξ measured, Δξ chosen to make m ≤
  budget).
- **Falsifier.** A refined phase grid revealing a violation between
  certified phases larger than the covering margin (L_ξ
  underestimated ⇒ the modulus-measurement protocol is falsified
  and must be tightened).

---

**FORK-24: Second-order conditions and their verification.**

- **Q.** What is the verifiable form of "reduced Hessian ⪯ 0 on the
  active tangent cone"?
- **Options.**
  - **O1. Shape-Hessian eigen-analysis:** assemble/apply the reduced
    second shape derivative (transformation calculus, FORK-18 O3;
    mind the known non-symmetry of naive shape Hessians off
    criticality — at a critical point the Hessian is symmetric,
    which is itself a checkable diagnostic) and bound its largest
    eigenvalue on the discretized active tangent cone by Lanczos on
    Hessian-vector products (second-order adjoints).
  - **O2. SSC via coercivity constants:** prove a negative-
    definiteness estimate analytically in a neighborhood class
    (only plausible on low rungs R0/R1 — worth doing there as an
    anchor).
  - **O3. Sampling/probing (directional second differences):**
    cheap falsifier-grade check, not a certificate.
  - **O4. Interval or SOS certification of the Hessian form:** on
    polynomial proxy models (FF-3) only.
- **Criterion.** Cost of Hessian-vector products (2 linear solves
  each: tangent + second adjoint) × Lanczos iterations vs the
  eigenvalue-gap structure; the active cone must come from FORK-22
  O2's resolved active set.
- **Recommendation.** **O1 with derived tolerance (Lanczos residual
  + discretization error model on the Hessian), O3 as an
  independent cross-check, O2 on the R0 rung.** The nonsmooth
  caveat: where the active set of phases changes, the correct
  object is a second-order condition on the *critical cone* of the
  semi-infinite program — state it in that form.
- **Falsifier.** A probing direction (O3) with positive measured
  curvature inside the claimed-negative cone beyond tolerance.

---

### Layer E — Globality

---

**FORK-25: The certified upper-bound mechanism for δ.**

- **Q.** Where does B ≥ sup_{A(c)} J come from, with δ = B − J[S*]
  computed and δ = 0 proven where structure permits?
- **Options.**
  - **O1. Interchange bound (Proof P1):** B₁ = ∫_Ξ sup_{S∈A(c)}
    F[S; s(ξ)] dμ — per-phase optimal-nozzle bounds integrated over
    the cycle; the per-phase sup is a *classical* single-state
    optimal nozzle problem with a rich exact literature (Guderley–
    Hantsch 1955; Rao 1958; Shmyglevskii/Kraiko exact variational
    contours) and cheap certified over-bounds (e.g., ideal fully-
    expanded momentum with envelope-limited area, R0 rung).
    Tightness gap = the cycle-compromise cost; δ = 0 exactly when
    one shape is per-phase optimal for μ-a.e. ξ (structure-permits
    case, provable when s(ξ) varies only in a direction the optimal
    contour is invariant to).
  - **O2. Lagrangian/dual bounds:** weak duality of the semi-
    infinite program with the geometric constraints dualized; needs
    a tractable inner sup — realistic on R0/R1 rungs.
  - **O3. Moment-SOS/occupation-measure hierarchy (Lasserre 2001;
    occupation-measure lifts of ODE rungs):** certified bounds for
    the R0 (quasi-1D ODE) rung with polynomial-fitted
    thermodynamics; converging hierarchy; dimensionality confines
    it to low rungs — used to *sharpen* O1's per-phase sup bounds.
  - **O4. Branch-and-bound in design space with Lipschitz bounds:**
    needs a certified Lipschitz constant of S ↦ J — measurable but
    fragile near the certification boundary; retained for the
    sector-pruning role (FORK-14 O5).
  - **O5. Convex-relaxation of the design set (FF-3):** no known
    thrust-exact relaxation for Euler; rejected as unavailable, at
    its best it is O3 on proxies.
  - **O6. Heuristic-only globality (multistart/BO/EA "no better
    found"):** breadth option; rejected as the mechanism — it
    produces evidence, not δ; retained as the search layer
    (FORK-26).
- **Criterion.** A mechanism qualifies only if B is *computable
  with its own error bars* and dominates sup J by proof, not by
  optimization.
- **Recommendation.** **O1 as the primary δ-carrier (it is exact in
  structure, and its slack is physically interpretable as the
  cycle-compromise cost), sharpened per-phase by O3 on the R0 rung
  and by the classical exact contours on R1; O2/O4 opportunistic.**
  Also report the *lower* branch: δ = 0 proof attempt via the
  invariance criterion above.
- **Falsifier.** Any certified design with J > B₁ (bound
  implementation wrong — an absolute rejector); or measured
  cycle-compromise slack larger than inter-sector differences
  (bound too loose to select sectors ⇒ O3/O2 sharpening becomes
  load-bearing).

---

**FORK-26: The global search layer (candidate generation).**

- **Q.** How are good candidates found inside each sector, given
  nonconvexity, before certificates are attached?
- **Options (full breadth, per the brief).**
  - **O1. Multistart gradient-based (certified adjoint machinery
    from Layer D, random/space-filling starts).**
  - **O2. Bayesian optimization on the certified evaluator** (EGO/
    EI, Jones et al. 1998; GP-UCB, Srinivas et al. 2010) in the
    ≤ 20-parameter certificate tier; model-error caveat declared.
  - **O3. CMA-ES / differential evolution / NSGA-II:** robust
    derivative-free global search; best for the discovery tier's
    rougher landscape (level-set sector proposals, FORK-14).
  - **O4. DIRECT / Lipschitz global methods:** deterministic
    coverage in low dimension; pairs with measured Lipschitz
    constants for weak certificates on R0 rungs.
  - **O5. ML surrogates / operator-learning evaluators (FNO/
    DeepONet) with verification:** cheap landscape scans; every
    surrogate optimum must be re-evaluated by the certified solver
    before it exists officially (verification firewall).
  - **O6. Continuation/homotopy in physics or constraint
    parameters:** from γ-const analytic optima (Rao contours) to
    the γ(T) cycle-averaged problem — exploits the classical exact
    solutions as starting branches; uniquely available here.
- **Criterion.** Cost per certified-quality candidate; coverage
  evidence (does the layer keep finding the same basins?);
  firewall discipline (nothing enters the certified record without
  the full evaluator).
- **Recommendation.** **O6 + O1 as the backbone (continuation from
  classical exact optima is the highest-information start), O3 in
  the discovery tier, O2 for expensive-regime refinement; O4/O5
  opportunistic. All behind the verification firewall.**
- **Falsifier.** A basin found by any layer that O6+O1 repeatedly
  missed (coverage hypothesis broken ⇒ widen the search layer and
  re-issue the FORK-14 sector-list hypothesis).

---

### Layer F — Numerics and error control

---

**FORK-27: Discretization of the per-phase state.**

- **Q.** Which solver family realizes the certified classes of
  FORK-6 with certifiable error?
- **Options.**
  - **O1. Method of characteristics (MoC) in supersonic zones:**
    the classical exact-nozzle tool; error structure transparent
    (characteristic mesh), naturally shock-fitting; γ(T) via
    characteristic-ODE quadrature (FORK-9); limited to hyperbolic
    zones — pairs with FORK-10 O3 decomposition.
  - **O2. Entropy-stable finite-volume/DG shock-capturing**
    (Tadmor; Fisher–Carpenter; modern ES-DG): robust everywhere,
    provable entropy stability (the right stability ledger for
    certificates), dual-consistent variants exist (FORK-17 O3);
    fronts smeared unless fitted/tracked.
  - **O3. High-order DG with fitted fronts / front tracking:**
    marries O2's framework with FORK-19 O1's differentiability
    needs; implementation-heavy.
  - **O4. Spectral/collocation in smooth certified zones:**
    exponential convergence where the class guarantees smoothness —
    cheap certificates via spectral a posteriori decay monitors.
  - **O5. PINNs / neural solvers:** breadth option; rejected as
    state carriers (no a posteriori error certification at the
    required level) — allowed only inside FORK-26 O5 surrogates.
- **Criterion.** Certified-class alignment (the solver must
  *realize* the class: fitted fronts for O2-class states, smooth
  high-order for O1-class), dual consistency, and a posteriori
  error accessibility.
- **Recommendation.** **O1/O4 in the certified-smooth supersonic
  regions (MoC as the reference organism, spectral/high-order DG
  as the workhorse), O3 where fronts are certified, O2 as the
  discovery-tier and cross-check solver.** Two independent
  discretizations (MoC vs DG) at candidates = a structural
  falsifier for solver bugs.
- **Falsifier.** MoC-vs-DG certified-state discrepancy at a
  candidate exceeding the combined derived error bars.

---

**FORK-28: Mesh/refinement policy and error estimation.**

- **Q.** How are discretization errors in J, g_sep, gradients, and
  Hessian estimates measured and driven?
- **Options.**
  - **O1. Goal-oriented dual-weighted-residual (DWR) adaptivity**
    (Becker–Rannacher 2001; Venditti–Darmofal 2002; Fidkowski–
    Darmofal 2011): error in J and in g_sep estimated with the
    already-computed adjoints; effectivity monitored, not assumed.
  - **O2. Uniform refinement + Richardson extrapolation:** simple,
    also yields observed-order diagnostics (a rejector for
    asymptotic-range claims).
  - **O3. Anisotropic metric-based adaptation:** efficiency for
    fronts/boundary layers of the adjoint.
  - **O4. hp-adaptivity keyed to the certification map:** p-refine
    certified-smooth zones, h-refine near fronts/sonic surfaces.
- **Criterion.** The (v) budget needs *bars, not estimates*: DWR
  effectivity must be measured against O2 reference solves at
  checkpoints; safety factors on the estimator are then *derived*
  from the measured effectivity population (e.g., bar = estimate ×
  (1/min observed effectivity), with the population documented).
- **Recommendation.** **O1+O4 in production, O2 at checkpoints as
  the effectivity referee; every safety factor traced to the
  measured effectivity distribution (no magic 1.25).**
- **Falsifier.** An observed effectivity below the derived safety
  factor's floor at any checkpoint (bars invalid; refit the factor
  from the enlarged population and re-issue affected certificates).

---

**FORK-29: Derivative computation and its verification battery.**

- **Q.** Adjoint/AD/FD/complex-step — what mix, and what proves the
  gradients?
- **Options.**
  - **O1. Hand-derived continuous adjoint discretized** (classical
    aero practice, Jameson): insightful, error-prone.
  - **O2. Discrete adjoint by reverse AD of the solver** (Griewank–
    Walther): exact to roundoff w.r.t. the discrete J; memory
    managed by checkpointing (Griewank's revolve).
  - **O3. Complex-step directional checks (Squire–Trapp 1998;
    Martins et al. 2003):** 1e-14-grade directional derivatives
    without subtraction error — the referee of record.
  - **O4. Finite differences:** step-size-fragile; only as a
    coarse smoke test with derived step (Gill–Murray balance of
    truncation vs roundoff).
  - **O5. Tangent (forward) mode cross-check:** forward-vs-reverse
    duality identity ⟨g, v⟩ checks transposition bugs
    independently of physics.
- **Criterion.** The battery must be able to *localize* a failure
  (which operator, which BC, which front term), not just detect it.
- **Recommendation.** **O2 as production (consistent with FORK-17
  O3), verified by the battery: O5 duality identity (transpose
  test), O3 directional referee at randomized directions/designs
  per release, O1-vs-O2 kernel comparison on certified-smooth cases
  (doubles as the FORK-18 O1/O2 consistency check), all with
  derived tolerances from conditioning estimates.** Special
  obligations: verify *at* a fitted front (FORK-19 O1 terms) and
  *at* an active g_sep phase (constraint Jacobians), not only at
  interior smooth points.
- **Falsifier.** Any battery element failing at derived tolerance;
  by design each failure indicts a named component.

---

**FORK-30: Optimizer class and globalization.**

- **Q.** Which optimization algorithm consumes the certified
  gradients/Hessians under the constraint structure?
- **Options.**
  - **O1. Reduced-space SQP with trust region:** the default for
    PDE-constrained design; exploits FORK-24's Hessian products;
    active-set friendly (pairs with FORK-22 O2).
  - **O2. Full-space (one-shot/simultaneous) methods (Ta'asan;
    Bosse–Gauger–Griewank):** state+adjoint+design updated
    together; large speedups; fragile near certification
    boundaries where the state solve must be exact to know the
    design is admissible.
  - **O3. Interior-point NLP (IPOPT-class):** robust for many
    inequality constraints; multiplier trajectories well-behaved
    for the marginal-value certificates.
  - **O4. Nonsmooth/bundle methods:** reserved for certification-
    boundary phases (FORK-32) and max-type diagnostics.
  - **O5. Derivative-free (already adjudicated at FORK-17 O4 /
    FORK-26): not the certificate optimizer.**
- **Criterion.** Constraint mix (few geometric + semi-infinite
  attachment) and the need for clean multiplier convergence; also
  robustness to inexact (adaptively re-meshed) evaluations — trust
  regions with error-aware acceptance (retrospective/inexact TR
  frameworks) handle DWR-controlled inexactness with proof.
- **Recommendation.** **O1 with error-aware (inexact) trust-region
  acceptance tied to FORK-28's bars, switching to O3 when the
  active inequality set is large; O2 only inside certified-smooth
  basins as an accelerator.**
- **Falsifier.** Optimizer accepting a step on estimator-lying
  evaluations (caught by checkpoint referee) — the acceptance rule
  then tightens by the measured estimator failure, mechanically.

---

**FORK-31: Stopping criteria and tolerance derivation.**

- **Q.** When is the optimization declared converged, with which
  derived tolerances?
- **Options.**
  - **O1. Error-balance stopping:** stop when the optimality
    residual (continuum-KKT residual, FORK-17) is dominated by the
    sum of certified discretization + quadrature + model bars —
    further optimization would chase noise; every threshold is a
    *ratio* of measured quantities, not a constant.
  - **O2. Fixed tolerance (1e-6 style):** rejected — magic
    constant, violates the brief.
  - **O3. Statistical stopping (no-improvement tests):** for the
    search layer only.
  - **O4. Certificate-driven stopping:** stop when δ (FORK-25) plus
    the (v) bars stop improving — i.e., the *decision quantity*
    converged, not the iterate.
- **Criterion.** The brief's "every tolerance derived" plus
  decision-relevance.
- **Recommendation.** **O1 for the inner loop, O4 for the program:
  the run ends when |Δδ| and |Δbars| over a window are below their
  own measurement noise (all measured).**
- **Falsifier.** Post-stop refinement (mesh or phases) moving J by
  more than the declared total bar.

---

**FORK-32: Handling the certification boundary in the loop.
(HW-3, part 3.)**

- **Q.** The optimizer will step to designs whose state cannot be
  certified (class exit: shock formation, fold crossing, sonic
  degeneracy, separation). What does the algorithm do there, and
  what does the certificate say?
- **Options.**
  - **O1. Hard filter/rejection:** uncertifiable step rejected,
    trust region shrunk; simple; risks crawling along a nonsmooth
    boundary with no dual information.
  - **O2. Margin-constraint internalization:** convert each
    certification condition into an explicit inequality with margin
    (shock-formation margin, fold margin σ_min ≥ σ₀, sonic
    non-degeneracy, g_sep) and hand them to FORK-22's machinery —
    the boundary becomes ordinary constraints with multipliers;
    the certificate then *prices* certification (marginal thrust
    cost of staying certifiable — decision-grade information).
  - **O3. Extended objective (penalty on uncertifiability):**
    smooths the boundary but pollutes multipliers' meaning.
  - **O4. Two-phase: explore uncertified (discovery tier), then
    pull back to the certified set by projection along the margin
    gradients.**
- **Criterion.** (ii)'s multiplier semantics + optimizer stability;
  O2 requires each certification condition to have a computable,
  differentiable margin — the whole tree has been arranging exactly
  that (FORK-6/7/10/12 monitors were designed as margins).
- **Recommendation.** **O2 as the doctrine (certification
  conditions = first-class constraints with margins and
  multipliers), O1 as the backstop for monitors that resist
  differentiable-margin form, O4 in the discovery tier.** This is
  the fork that turns "certified class" from a filter into a
  *priced constraint surface* — arguably the most distinctive
  structural choice of the whole formulation.
- **Falsifier.** A margin functional whose zero level fails to
  coincide with actual certification failure (margin lies: e.g.,
  σ_min margin positive but continuation still jumps branches) —
  that margin is demoted to O1 filtering and the constraint set
  re-issued.

---

### Layer G — Error bars and monitoring

---

**FORK-33: Structure of the unsteady correction bound
(requirement (v), HW-4).**

- **Q.** What are the named, evaluable terms bounding
  |J_exact − J[S*]|, at marginal St?
- **Options.**
  - **O1. Asymptotic two-scale series with remainder estimate:**
    J_exact = J + St·J₁ + O(St²) — honest only if the remainder is
    *bounded*, which at marginal St is not automatic (Proof P6);
    at its best with a computable J₂-magnitude estimate to test
    series decay empirically.
  - **O2. Computed unsteady-residual bracket:** run the time-
    periodic unsteady solve (FF-2/R2–R3) at S* only; Δ := |J_exact
    − J| is then *measured* (plus its own discretization bars from
    FORK-28 applied in time); the (v) term becomes a computed
    number with bars, not a modeled one; cost confined to
    candidates.
  - **O3. A posteriori residual bound:** insert the quasi-steady
    cycle field into the unsteady equations, measure the residual
    r(t), and bound |J_exact − J| ≤ C·‖r‖ via a stability constant
    C of the linearized unsteady operator; C estimable (transient-
    growth/resolvent computation) — the only route that yields a
    *bound* without trusting a series, but C's own bars are the
    weak point.
  - **O4. Hierarchy bracketing:** monotone model chain (R1s ⊂ R2 ⊂
    R3) with measured inter-rung gaps as the declared bars —
    honest bookkeeping, no smallness claims at all.
  - **O5. Statistical closure of the limit:** if the T → ∞ limit is
    not shown to exist, report liminf/limsup from finite-T windows
    with window-convergence diagnostics (the brief's bracket
    fallback); under H-DATA periodicity the limit exists trivially
    (periodic average — a one-line lemma), so this option activates
    only on H-DATA violation.
  - **O6. Machine-learned unsteady-correction surrogate:** breadth
    option; rejected as a bar-carrier (uncertifiable), admitted for
    screening which designs merit O2.
- **Criterion.** A term qualifies for (v) only as bound-with-
  carrier or measurement-with-bars; series terms without remainder
  control do not qualify at marginal St.
- **Recommendation.** **O2 at candidates as the primary carrier +
  O3 as its independent bound-form cross-check + O4 as the
  bookkeeping frame; O1 relegated to explaining the measured Δ's
  parametric trend in St (measured, per the brief).** Note the R2
  rung (co-rotating steady 3D) makes O2 cheaper than generic
  unsteady: under H-DATA, J_exact equals the R2 steady thrust
  (Proof P8), so the (v) gap is computable steady-to-steady.
- **Falsifier.** O3's bound violated by O2's measurement (stability
  constant wrong); or R2-vs-R3 disagreement beyond bars (H-DATA or
  the co-rotating reduction misapplied).

---

**FORK-34: H-DATA monitoring and the data-admissibility audit.**

- **Q.** How are H-DATA (pure single-mode rotating wave) and the
  admissibility premises (causal separation, well-posed closure,
  measurability) monitored, as the brief demands?
- **Options.**
  - **O1. Spectral mode monitor:** azimuthal-temporal decomposition
    of the interface data; H-DATA holds iff energy outside the
    (n, f)-locked component is below a derived threshold (threshold
    from the sensitivity |∂J/∂data| times the residual mode
    amplitude vs the (v) budget — not magic).
  - **O2. Symmetry-residual monitor:** under H-DATA, data are a
    function of (θ − 2πnft) alone; measure the residual of that
    ansatz directly (nonparametric, catches mode transitions and
    drift).
  - **O3. Causal-separation test:** perturb the design (or use two
    designs' recorded interface data) and verify the data family is
    invariant within bars — an *experiment on the premise*, the
    only honest audit of causality.
  - **O4. Closure-consistency monitor (from FORK-8):** outgoing-
    invariant mismatch tracking.
  - **O5. Measurability/regularity audit:** ξ-continuity moduli of
    s(ξ) measured (feeds FORK-4/23 constants).
- **Criterion.** Each premise gets at least one monitor whose
  firing has a *declared consequence* (which certificates die:
  H-DATA failure kills the R2 equivalence and the μ-construction;
  causal-separation failure kills the whole per-phase
  decomposition).
- **Recommendation.** **All five, cheap and always-on, with the
  failure→consequence map published as part of certificate (v);**
  O2 is the primary (assumption-free) H-DATA monitor, O1 its
  diagnostic refinement.
- **Falsifier.** Each monitor is itself a falsifier of a named
  hypothesis; the meta-falsifier is an O3 test showing design-
  dependence of the data — the brief's premise, not the method,
  would be refuted, and the program must renegotiate the interface.

---

## 3. DRY-LEVEL PROOFS

**P1 (Interchange upper bound — carrier of FORK-25 O1).**
Claim: B₁ := ∫_Ξ sup_{S∈A(c)} F[S; s(ξ)] dμ(ξ) ≥ sup_{S∈A(c)} J[S],
and δ := B₁ − J[S*] ≥ 0 is a computed globality gap; δ = 0 iff some
single S is per-phase optimal for μ-a.e. ξ.
Sketch: for every S and μ-a.e. ξ, F[S; s(ξ)] ≤ sup_{S'} F[S'; s(ξ)];
integrate in μ (monotonicity), then take sup over S on the left.
Hypotheses: (a) per-phase sup finite for μ-a.e. ξ (guaranteed by the
envelope bound: F is bounded by fully-expanded momentum flux through
a disk of radius R_E — an explicit R0 computation); (b) measurability
of ξ ↦ sup_S F: A(c) compact metric (FORK-15) + F Carathéodory ⇒
measurable by the measurable-selection theorem (Castaing). Equality
case by inspection of the inequality chain. Note each per-phase sup
may itself be replaced by any certified upper bound (R0 ideal-thrust
bound, sharpened by classical exact contours or moment-SOS on R0) —
the inequality survives, only slack grows.

**P2 (Control-surface invariance of F — FORK-2).**
For a steady Euler state, div Π = 0 with Π = ρ u⊗u + (p − Pa) I
(subtracting the constant Pa changes Π by a divergence-free tensor).
For two enclosing surfaces Σ₁, Σ₂ bounding a flow region R (with the
wetted wall in between contributing wall pressure-force terms
consistently), the divergence theorem gives F_{Σ₁} = F_{Σ₂} + wall
terms, i.e., the near-field and far-field thrust bookkeepings agree
exactly; on weak solutions the same holds provided R–H conditions
hold on fronts (fluxes continuous across fronts by definition of
weak solution). Hypotheses: state in the certified class (weak form
holds); surfaces homologous in the flow region. Discrete violation
of P2 = conservation-error estimator (FORK-2 O3).

**P3 (Conditional existence — FORK-15 O1).**
Claim: If (H-GEO) A(c) has the uniform (h0, ω) cone property with
the g_i lower-semicontinuous for Hausdorff-complementary
convergence, and (H-STAB) along any A(c)-convergent sequence S_k →
S the certified per-phase states converge U_k(ξ) → U(ξ) in L¹_loc
for μ-a.e. ξ with U(ξ) certified for the limit domain and |F[S_k;
s(ξ)]| ≤ m(ξ) ∈ L¹(μ), then J attains its max on the certified
subset of A(c).
Sketch: Chenais's theorem gives compactness of the uniform-cone
class; take a maximizing sequence, extract a convergent subsequence;
(H-STAB) + dominated convergence pass F to the limit per phase and
then J; upper semicontinuity suffices for max.
Status of (H-STAB): provable in the shock-free axially-supersonic
subclass by uniform C¹ characteristic estimates (supersonic marching
is a Cauchy problem in x with domain-Lipschitz-continuous
coefficients; cone property gives uniform wall Lipschitz bounds);
OPEN across sonic surfaces and with fitted fronts — hence the
monitored failure boundary of FORK-15, which is exactly a runtime
check of (H-STAB) along optimizer sequences.

**P4 (Danskin for cycle-worst quantities — FORK-3 O2 / FORK-23).**
If Ξ is compact, g(S) := max_ξ g_sep(S; s(ξ)) with g_sep continuously
shape-differentiable jointly and continuous in ξ, then g is
directionally differentiable with g′(S; θ) = max over the active
phase set of d_S g_sep[θ] (Danskin 1966). Consequence: worst-phase
constraints and diagnostics have exact subgradient calculus; the
active-phase multipliers of FORK-22 are the μ-singular parts
concentrating there.

**P5 (Averaged first-order condition — FORK-20).**
Under: per-phase certified-smooth states, shape-differentiability of
F per phase with kernel G_ξ ∈ L¹(Γ_w) uniformly μ-integrable, the
map ξ ↦ G_ξ measurable — differentiation under the μ-integral is
licit (dominated convergence), so dJ[θ] = ∫_Ξ ∫_{Γ_w} G_ξ (θ·n) dA
dμ. KKT with the geometric multipliers λ and attachment multiplier
measure η on Ξ × Γ_w then reads: ∫_Ξ G_ξ dμ + Σ λ_i k_i +
∫ K dη = 0 on the free wall, plus endpoint conditions (FORK-21) and
complementarity. Structural corollary: the classical single-state
optimal-nozzle wall condition (Rao/Guderley–Hantsch: kernel ≡ 0)
holds only in μ-average — the cycle-averaged problem's signature
stationarity structure.

**P6 (Marginal-St obstruction to series-based bars — FORK-1/33).**
Two-scale expansion in ε := St of the unsteady solution about the
quasi-steady cycle yields J_exact = J + ε J₁ + ε² R(ε). The
remainder R involves the inverse of the linearized unsteady operator
acting on second-order commutators of the cycle; its norm is
controlled only by a stability constant that is O(1) at best — so
for ε neither small nor large, ε²R is not dominated by εJ₁ by any a
priori argument. Conclusion (decides the fork): at marginal St, only
*computed* carriers (measured Δ at candidates, or residual-times-
stability-constant bounds) qualify as (v) terms; truncated series do
not. Hypotheses: linearized stability of the quasi-steady cycle
(else even the expansion's first term is void — another monitor).

**P7 (O(1) contamination of captured-shock gradients — FORK-19).**
Scaling sketch: a capturing scheme smears a front over width w ~ h.
The discrete sensitivity of a front-position-dependent functional
splits into a smooth part plus a layer term = O(w) volume × O(1/w)
integrand-derivative = O(1), whose value depends on the limiter/
viscosity profile, not on the physics; it converges (if at all) only
weakly and slowly as h → 0. Corroborated in the conservation-law
sensitivity literature (Ulbrich 2002; adjoint shock analyses of
Giles–Pierce; Baeza et al. 2009). Consequence: certificate-grade
gradients at fronts require fitted linearization (FORK-19 O1) or
front-aware correction terms; raw AD-through-limiter gradients are
rejected as certificate carriers.

**P8 (Existence of J_exact under H-DATA; co-rotating reduction —
FORK-33).**
Under H-DATA, the inflow data are steady in the frame rotating at
Ω = 2πf/…(mode-locked rate); if the flow state is the (certified)
steady solution in that frame, all Eulerian time signals at fixed
axial stations are time-periodic with period 1/(nf), so
(1/T)∫₀^T F dt converges (periodic averaging) — the brief's liminf/
limsup bracket collapses to a limit, and J_exact equals the
co-rotating steady thrust (axisymmetric control surface ⇒ the
azimuthal average is exact). Hypotheses: existence + stability of
the co-rotating steady state (an R2-rung certification), H-DATA.
This is the structural bridge that makes FORK-33 O2 a steady-to-
steady comparison.

---

## 4. ORDER OF BATTLE

Dependency-ordered campaign; **[LB]** marks load-bearing forks (a
wrong early call poisons downstream certificates), local marks
contained ones.

**Stage 0 — Ground truth of the data and objective (kills cheap
forks first).**
1. FORK-34 monitors online (data admissibility audit) — everything
   is conditional on these premises. **[LB]**
2. FORK-10 O4 check (is the interface axially supersonic for all
   ξ?) — may dissolve the sonic fork and simplify FORK-8. Cheap,
   do first.
3. FORK-2 (thrust bookkeeping + P2) and FORK-1 provisional (declare
   the O1+O4+O3 ladder). **[LB]** (FORK-1: wrong averaging relation
   poisons the meaning of every optimization result.)

**Stage 1 — Solution concept and state pipeline.**
4. FORK-6 (certified classes) **[LB]** — the single most
   load-bearing call: it defines what "the state" means (HW-2),
   what the oracle certifies, and which derivative theory exists.
5. FORK-8 (closure), FORK-9 (thermo), FORK-7 (branch selection),
   FORK-11 (plume), FORK-12 (g_sep model) — local given FORK-6.
6. FORK-5 (ladder assignment incl. swirl decision; R2 rung stood
   up early because P8 makes it the (v) carrier). **[LB]** for (v).

**Stage 2 — Design class and existence.**
7. FORK-13 (two-tier representation) **[LB]** — wrong class either
   forfeits topology (output demanded by the brief) or forfeits
   certificates.
8. FORK-15 (existence packaging + H-STAB monitor) **[LB]** for
   certificate (i); FORK-16 local.
9. FORK-14 (sector doctrine) — depends on 7; feeds globality.

**Stage 3 — Optimality machinery.**
10. FORK-17 (dual-consistent DtO≡OtD) **[LB]** — decides the entire
    numerics/certificate interface; choose before writing any
    solver code.
11. FORK-18, FORK-20, FORK-21 (derivative forms, averaged system,
    transversality) — mostly mechanical once 10 is fixed; FORK-19
    **[LB]** if (and only if) certified optima retain fronts —
    resolve its conditional early by a pilot study per sector.
12. FORK-22 + FORK-23 (state-constraint machinery + phase
    covering) — local but with a derived-constant discipline that
    must be built in, not retrofitted.
13. FORK-29 (verification battery) — stood up *with* the first
    adjoint line of code, not after.

**Stage 4 — Search and globality.**
14. FORK-26 (search layer, continuation from classical optima
    first), FORK-30/31 (optimizer + stopping) — local.
15. FORK-25 (δ-carrier) **[LB]** for certificate (iv): the
    interchange bound B₁ should be computed in week one on the R0
    rung — it prices every subsequent decision (is the
    cycle-compromise slack big or small?) and is the cheapest
    strategic information in the whole program.
16. FORK-32 (certification boundary as priced constraints) —
    doctrine fork; decide before the optimizer first meets the
    boundary.

**Stage 5 — Second order, bars, closure.**
17. FORK-24 (Hessian verification), FORK-27/28 (discretization +
    bars) — FORK-28's measured-effectivity discipline is **[LB]**
    for every "derived tolerance" claim in the program.
18. FORK-33 (the (v) carrier at candidates; R2/R3 tier), FORK-3/4
    revisit (μ-sensitivity, phase quadrature finalization).

**The five most load-bearing forks, ranked:**
1. **FORK-6** (solution concept / certified classes — HW-2): every
   certificate quantifies over "the state"; without this call
   nothing downstream is even well-posed.
2. **FORK-1/33 pair** (surrogate↔exact relation at marginal St —
   HW-4): decides what the optimization *means* physically and what
   (v) can honestly say.
3. **FORK-17** (optimality-system discretization order): silently
   wrong here = certificates about a different problem than the one
   computed.
4. **FORK-25** (globality mechanism): without a computable B, (iv)
   is unfulfillable no matter how good the optimizer is; the
   interchange bound makes it fulfillable from day one.
5. **FORK-15** (existence packaging — HW-1): determines whether (i)
   is a theorem, a conditional theorem with monitors, or a bracket
   report; must be decided honestly, early, in writing.

---

*End of attack tree. 34 forks (FORK-1 … FORK-34), 8 dry-level
proofs (P1–P8), 5 formulation families (FF-1 … FF-5).*
