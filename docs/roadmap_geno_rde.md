# GENO-RDE: program plan for a certified optimal-contour tool for RDE nozzles

Status: PROGRAM PLAN (execution roadmap). Third document of the set:
- `docs/cycle_averaged_variational_nozzle.md` - engineering formulation
  (T0-T4, averaged Rao system (*)-(**), novelty channels N1-N6, ladder).
- `docs/mathematical_foundations_rde_nozzle.md` - rigorous formalization
  (solution concepts, relative-equilibrium/freezing, P1-P7, oracles O1-O5).
- THIS - who builds what, in which order, with which kill criteria.

Goal statement (the tool): given (a) propellant/chamber specs or a
measured/simulated cycle family s(xi) with its operating measure mu, and
(b) constraints (length, eps_max/annulus, truncation, ambient profile,
axisymmetry class), GENO-RDE returns the OPTIMAL CONTOUR (bell, plug,
shrouded plug) for cycle-averaged performance, shipping with:
  1. a certificate of stationarity (the averaged optimality system
     residuals, dual-route agreement),
  2. an O(St) unsteadiness error bar on the predicted Isp,
  3. mode-robustness flags (spectrum-based operability information),
  4. full V&V records (oracle results, regression cases) - repo culture.

------------------------------------------------------------------------------
## 0. The strategic spine (why this order and no other)

The critical path runs through RUNG 2 (averaged variational with
per-phase MOC physics), because:
- it is where ALL the identified novel physics (N1-N4) is computable at
  characteristic precision without CFD;
- its two known degenerate limits (T3 collapse, T4 knee) provide FREE,
  closed-form, executable oracles - no other rung has this;
- its per-phase ingredient is solved mathematics (Rao/Kraiko + classical
  MOC), so the engineering risk concentrates in ONE new object (the
  cycle layer), which is cheap to iterate.

Rung 3 (wave-frame exact / HB) enters as an ANCHOR (a few expensive
truth points quantifying rung-2 model error), not as the tool engine.
The bilevel chamber coupling enters as a REDUCED differentiable response
map, not as a coupled reacting adjoint. Things deliberately NOT on the
critical path (documented temptations): 3-D URANS adjoint from day one;
discrete adjoints of shock-capturing CFD (adjoint-consistency trap,
foundations note Sec. 4.2); the full MPEC/bilevel formulation; any
non-axisymmetric design before P5 says it can pay.

------------------------------------------------------------------------------
## 1. Team (roles, not headcount; one person can hold two hats)

R1 VARIATIONAL ANALYST: owns T0-T4, P1-P7, the averaged system (*)-(**),
   the St expansion; writes the hypothesis ledger and referees every
   claimed gain against it.
R2 MOC/HYPERBOLIC NUMERICIST: owns the per-phase engine (unit processes,
   shock fitting, free-boundary marches, transonic inflow interface);
   GENO doctrine keeper (dual-backend/dual-code equivalence discipline).
R3 AUTODIFF/OPTIMIZATION ENGINEER: owns the differentiable stack,
   gradients, spline shape space, SQP/trust-region + Sobolev metric,
   the collocation BVP solver.
R4 DETONATION/COMBUSTION MODELER: owns the cycle-family generator
   (matched-cycle chain, CEA/Cantera states, per-phase gamma), the
   chamber response map, the mode measure calibration, URANS anchors.
R5 V&V ENGINEER (part-time role, full-time mindset): owns oracles O1-O5,
   regression baselines, certificates, the validation records.

------------------------------------------------------------------------------
## 2. Workpackages

### WP0 - Problem book and interface contracts (weeks 0-4)

In: the two theory notes. Out:
- PROBLEM BOOK: frozen notation, the HYPOTHESIS LEDGER (every model
  assumption H*/D* with its violation channel N* and its oracle),
  acceptance criteria for every WP below.
- INTERFACE CONTRACTS (the load-bearing engineering decision):
  (C1) `CycleFamily`: s(xi) = {P0, T0, gamma-law or thermo handle,
       M_in(y), theta_in(y), vorticity/entropy profiles} + measure mu
       (weights); serialization format; two generators from day one:
       S-H matched-cycle (exists in repo) and file-based (URANS/exp).
  (C2) `Design`: contour class (bell | plug | shrouded), spline DOFs,
       constraint set (L, eps_max, truncation, lip), symmetry class.
  (C3) `Verdict`: contour + performance + certificate + error bar +
       oracle record. No number leaves the tool outside a Verdict.
Acceptance: both theory notes' claims mapped 1:1 to ledger entries.

### WP1 - The per-phase engine: differentiable MOC evaluator (months 1-6)

The workhorse. ANALYSIS mode (given contour + given inflow -> field +
thrust + wall pressures), planar/axisymmetric, rotational (Zucrow-Ch.17
class), gamma(T) via thermally-perfect backend, nonuniform IVL.

- 1a LANGUAGE DECISION (gate G0, week 4): default RECOMMENDATION:
  Python/JAX (or Julia) re-implementation of the unit processes, with
  GENO-Fortran as the independent verification reference (dual-code
  equivalence discipline GENO already practices). Fallback: Fortran +
  Tapenade on GENO itself (proven in the HB-adjoint literature) if the
  re-implementation cost is judged too high. Criteria: gradient
  fidelity, iteration speed of the research loop, team skills.
- 1b GRADIENTS: reverse-mode autodiff through the characteristic march
  = per-phase adjoint, exact to machine precision. Care points:
  iterative unit-process solves (implicit-function-theorem custom
  rules, not unrolled loops); shock fitting (differentiate the fitted
  front, never the captured smear); switch points (one-sided rules).
- 1c NEW UNIT PROCESSES (the real numerics risk, front-load it):
  (i) free-boundary/jet-boundary march for PLUG OFF-DESIGN analysis
  (a designed plug evaluated at non-design NPR) - validated against
  Angelino/GenoPlug cases and limiting behaviors; (ii) prescribed
  nonuniform rotational IVL ingestion (GENO `read_ivl_from_file`
  semantics); (iii) separation criterion hook on wall-pressure
  distributions (Summerfield/Schmucker, pluggable).
- 1d VALIDATION: GENO regression set (ideal/TIC/TOC/plug cases,
  md5-frozen baselines) reproduced in analysis mode; thrust and contour
  agreement to stated tolerances.

Milestone M1 (month ~6): differentiable per-phase evaluator, validated
vs GENO, dot-product test (oracle O3) at machine precision.

### WP2 - The cycle layer: averaged functional, optimizer, oracles,
###        first science (months 4-12, overlaps WP1)

- 2a QUADRATURE in xi over `CycleFamily` (Gauss on the log-uniform
  measure; convergence documented like the repo's NQ=4001 discipline).
- 2b OPTIMIZER: spline contour DOFs, trust-region SQP with exact
  gradients, Sobolev/Steklov-Poincare shape metric, constraint handling
  (L, eps_max, lip). Non-smooth guard: bundle fallback near topology
  switches.
- 2c ORACLES FIRST (gate G1, the machinery certificate):
  O1: frozen-gamma, full-flowing, uniform-inflow ensemble MUST return
      the Rao-at-<Pc> contour with Delta-Isp = 0 vs single-phase design
      (T3); O2: ideal untruncated plug MUST return the peak design (T4);
  O3: per-phase dot-product identities. FAIL -> stop, fix, no science
  on an uncertified machine. Fallback if autodiff route fails G1
  irreparably: GENO + finite differences (slower, still sufficient for
  WP2d at reduced DOF counts).
- 2d FIRST SCIENCE (the paper-2 numbers), switching on ONE collapse-
  breaker at a time against the certified baseline, on the Table-1
  matched-cycle states (already cached in the lecture repo):
  N1: separated bell - cycle-designed vs mean-designed contour,
      Delta-Isp + contour morphology (does a temporal dual-bell emerge?);
  N2: TRUNCATED PLUG at fixed length - cycle-optimal vs peak-designed
      vs mean-designed: the first genuinely averaged optimum nobody has
      computed;
  N3: per-phase nonuniform inlet (M, theta profiles from the detonation
      chain): gain/loss vs clean-blowdown assumption;
  N4: per-phase gamma(T): contour-level confirmation of the quasi-1D
      -0.001% estimate (expected null; publishes as a bound).
  Each number ships with its hypothesis-ledger row and oracle record.

Milestone M2 (month ~12): certified first-of-their-kind quantitative
results; go/no-go data for gate G2.

### WP3 - Dual-route certification: direct collocation of the averaged
###        optimality system (months 8-14)

Discretize the phase family; unknowns = shared contour + per-phase
terminal characteristics + lambda_2(xi) samples + shared multipliers;
equations = per-phase Rao/Kraiko conditions + averaged wall condition
(*) + averaged transversality (**); Newton BVP solve. Cross-check the
WP2 NLP optimum: TWO INDEPENDENT ROUTES TO THE SAME CONTOUR (the repo's
golden-section-vs-analytic-identity discipline, one level up).
Milestone M3: dual-route agreement to stated tolerance on all WP2d
cases; the residuals of (*)-(**) become the tool's stationarity
CERTIFICATE.

### WP4 - The St bridge: error bars (months 10-16)

Per-phase linearized unsteady response (Marble-Candel-type transfer
functions, computed numerically on the per-phase base flows) -> the
corrector J_1 -> every design ships Isp +/- St|J_1| (+O(St^2) caveat).
Validation (oracle O5): one direct unsteady quasi-1D/2-D simulation of
a designed nozzle under the blowdown; measured vs predicted J_1.
Gate G3 lives here.
Milestone M4: error-barred outputs; the quasi-steady license quantified.

### WP5 - Wave-frame anchor (rung 3a) (months 12-22, parallel track)

Purpose: quantify what rung 2 cannot see (D2 azimuthal coupling, swirl),
NOT to replace it.
- 5a: 2-D unrolled-annulus rotating-frame model (reactive Euler with
  moving-frame source terms; freezing formulation with unknown Omega +
  phase condition; Newton-Krylov continuation). Cheap testbed for the
  P1 machinery and for dOmega/dSigma (oracle O4: adjoint vs finite
  differences of continued waves).
- 5b: 3-D steady rotating-frame RANS on 2-3 designs from WP2d;
  time-averaged thrust cross-check; D2-error quantification.
Milestone M5: rung-2 model error bounded on real designs; P1 pipeline
demonstrated on the reduced model.

### WP6 - Chamber coupling + robustness (months 16-24)

- 6a: differentiable reduced response map Sigma -> (PR, Omega, fill)
  built on the matched-cycle machinery (weak bilevel; the repo's
  Sec.-III fixed point generalized and differentiated).
- 6b: mode measure pi from operability maps (literature + any available
  data); expected-value and CVaR objectives wired into WP2's optimizer;
  spectrum-based operability flag from the WP5a stability solve (the
  P1 corollary made a product feature: performance and stability from
  one operator).

### WP7 - Productization (months 18-26)

CLI + API around C1-C3 contracts; contour classes bell/TOP/plug/
shrouded (shrouded = the C1 conjecture study becomes a tool mode:
optimal duty split shroud-vs-plug under constraints); config files;
docs; full regression suite (oracles + GENO cases + WP2d cases as
frozen baselines); versioned validation records. Prerequisite fix
imported from GENO: RaoPlug S1/S2 (mass multiplier / 2-DOF) if the
GENO-side designer is kept as an independent reference.

### WP8 - Theory/publication stream (continuous, gated by results)

Paper 1 (formulation): T0-T4, averaged system, collapse + oracles,
ladder. Submit after M1 (machinery exists -> claims executable).
Paper 2 (results): WP2d numbers + dual-route certificates (after M3).
Paper 3 (bridge): O(St) corrector + validation (after M4).
Paper 4 (mathematics): P1 (sensitivity=stability) + P2 (Rao=adjoint)
on the WP5a reduced model (after M5).

------------------------------------------------------------------------------
## 2bis. Solver hierarchy: what is exact where (correcting a shortcut)

The "modified raocore" idea (phase-averaged corner residual inside the
existing Rao bisection) is NOT the general engine. Its exact scope, and
the general machinery, form a three-level hierarchy; the tool uses all
three, each where it is licensed.

LEVEL A - STRUCTURE-EXPLOITING (Rao-native construction). Valid iff the
averaged Euler-Lagrange system retains CHARACTERISTIC STRUCTURE: the
per-phase interior stationarity is satisfied automatically (the
pressure-scaling class of Theorem T3, where the phase state enters the
optimality system ONLY through the endpoint/corner condition and the
multiplier balance), so the whole phase dependence collapses onto the
shared transversality condition. Then, and only then, the Rao marching
construction (kernel -> f2-invariant terminal characteristic ->
streamline wall) applied to a reference field, with the corner residual
replaced by its mu-average, produces the EXACT solution of the averaged
problem - because the averaged system is, by T3-type structure, a
single-phase Rao system in disguise. Outside this class (separation,
strongly phase-dependent inlet profiles, free boundaries with
truncation) the constructed wall satisfies (**) but NOT the interior
averaged wall condition (*): Level A degrades to a first-order
approximation, useful as a SEED and as a cheap design-space scan, never
as the certified answer. Theorem P2 (Rao = closed-form adjoint) is the
precise statement of Level A's license: raocore is a special-purpose
analytic adjoint solver; "reusing raocore" = using the closed-form
adjoint exactly where it exists.

LEVEL B - GENERAL SMOOTH ENGINE (two dual routes, cross-certifying):
  B1 REDUCE-THEN-OPTIMIZE (NLP on shape space): per-phase state solves
     (classical Goursat/characteristic well-posedness); gradients by
     per-phase ADJOINT - either the continuous adjoint Euler system
     with Giles-Pierce shock conditions, discretized adjoint-
     consistently, or reverse-mode AD of the shock-FITTED MOC march
     with implicit-function custom rules for iterative unit processes
     (the discrete adjoint of a convergent fitted scheme converges to
     the continuous adjoint - the adjoint-consistency requirement is a
     gate, not a footnote). Note the structural fact that makes this
     natural: the adjoint of a characteristic march is a characteristic
     march backwards along the SAME Mach lines with transposed data
     flow - reverse-mode AD of MOC computes exactly the discrete
     adjoint characteristic sweep, which is WHY Rao's conditions exist
     in closed form (P2). Shape space: spline manifold with
     Sobolev/Steklov-Poincare metric (Riesz representation of the
     gradient, not smoothing-as-hack); optimizer: trust-region SQP on
     exact KKT residuals; near topology switches: Clarke-stationarity
     bundle safeguard.
  B2 OPTIMIZE-THEN-DISCRETIZE (direct collocation of the optimality
     system): the averaged E-L system (*) + (**) + per-phase
     Rao/Kraiko conditions + the multiplier function lambda_2(xi),
     discretized by phase quadrature and solved as one Newton BVP
     (pseudospectral/collocation optimal-control technology).
     Multiplicity handling: deflation (deflated continuation) to
     enumerate stationary contours - uniqueness is NOT guaranteed and
     is not assumed.
  The two routes do not commute in general (discretize-then-optimize
  vs optimize-then-discretize); their AGREEMENT on the same contour to
  tolerance is the certification, and their disagreement is a bug
  detector (WP3 = exactly this).

LEVEL C - EVALUATION/CERTIFICATION of a candidate optimum (design and
evaluation are different acts):
  (i)   a-posteriori first-order certificate: averaged shape gradient
        recomputed on an INDEPENDENT discretization -> residual bound;
  (ii)  second-order test: reduced-Hessian spectrum on the constraint
        tangent space via Hessian-vector products (second-order adjoint
        / forward-over-reverse AD), Arnoldi;
  (iii) oracle limits O1/O2 (the machinery must reproduce T3/T4);
  (iv)  O(St) error bar (WP4 corrector);
  (v)   model-error anchor: wave-frame steady solve (freezing +
        Newton-Krylov) of the final design (WP5);
  (vi)  multistart + deflation record: which other stationary contours
        exist and why the reported one dominates.

------------------------------------------------------------------------------
## 3. Decision gates (kill/pivot criteria - a rigorous plan says when
##    it is wrong)

G0 (wk 4): language/stack for WP1. Criteria in WP1a.
G1 (M1+): ORACLE GATE. O1/O2/O3 pass or no science downstream.
    Irreparable autodiff failure -> GENO+FD fallback (reduced ambition,
    program survives).
G2 (M2): VALUE GATE. If ALL of N1-N4 yield < ~1% Isp at contour level:
    the "shape gains" value proposition dies honestly; PIVOT the tool to
    (i) certification + error bars + operability (still unique in the
    field), (ii) the shrouded-plug duty-split mode (C1) and N3 inlet-
    nonuniformity studies, which carry independent design value.
    (Current evidence: N4 measured tiny; N1/N2/N3 sized by the Fig.-8
    CF collapse and the S-H spike-vs-bell gaps at 3-12% - expectation
    is PASS, but the gate is real.)
G3 (M4): UNSTEADINESS GATE. If St|J_1| = O(several %) on realistic
    engines, quasi-steady contours are not shippable as-is -> elevate
    WP5 from anchor to correction loop (design at rung 2, correct at
    rung 3, iterate); the ladder was built for exactly this.
G4 (M5): DECOUPLING GATE. If D2 (azimuthal-coupling) error dominates
    all N-channels, rung 2 keeps the optimizer role but the objective
    is re-based on wave-frame evaluations (surrogate-corrected).

------------------------------------------------------------------------------
## 4. Risk register (top items)

RK1 Plug off-design free-boundary march (WP1c-i): riskiest numerics on
    the critical path. Mitigate: front-load month 1-3; validate against
    Angelino limits; fallback closure = S-H ideal-adaptation model
    (loses N2 fidelity, keeps program alive).
RK2 Autodiff through iterative/shock-fitted MOC: mitigate with implicit
    custom rules + O3 gating; fallback FD (G1).
RK3 Multi-D shock calculus has no complete theory (foundations note):
    mitigate by staying shock-FITTED in (S1); document the boundary.
RK4 Mode-measure data scarcity (WP6b): mitigate with literature
    operability maps + sensitivity-to-pi reporting (DRO framing).
RK5 Team bus-factor on the variational core: the problem book (WP0) and
    executable oracles ARE the mitigation.
RK6 Scope creep toward full URANS adjoint: the spine section exists to
    be pointed at.

------------------------------------------------------------------------------
## 5. First 90 days (concrete)

1. WP0 problem book + C1-C3 contracts drafted and frozen v0.        (R1,R5)
2. G0 stack decision spike: JAX prototype of ONE unit process
   (interior point + inverse-wall) with reverse-mode gradient checked
   against central differences and against GENO on one TOC case.    (R2,R3)
3. Plug off-design jet-boundary march: formulation note + prototype
   on the Angelino baseline (RK1 front-load).                       (R2)
4. CycleFamily generator v0 from the lecture-repo matched-cycle
   states (Table-1 rows as the canonical test set).                 (R4)
5. Oracle harness skeleton: O1/O2 specified as executable tests
   BEFORE the optimizer exists (test-first, repo culture).          (R5)
6. Paper-1 outline circulated (WP8).                                (R1)

------------------------------------------------------------------------------
## 6. What success looks like

- v1.0 tool: certified cycle-averaged optimal bell/plug/shrouded
  contours with stationarity certificates, O(St) error bars, and
  operability flags, on user cycle families - nothing comparable
  exists.
- 3-4 papers staking the formulation, the first averaged optima, the
  error-bar bridge, and the sensitivity=stability mathematics.
- The negative results (N4 bound, any G2 nulls) published as bounds -
  they are load-bearing for the field precisely because T3 explains
  them.
