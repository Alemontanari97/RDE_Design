# PHASE A ATTACK TREE — HYPERBOLIC CONSERVATION LAWS / CHARACTERISTICS / COMPRESSIBLE-FLOW LENS

Author: independent deriver, lens = hyperbolic PDE, method of characteristics
(MoC), shock fitting vs capturing, well-posedness of steady supersonic BVPs,
transonic structure, weak-solution theory, front stability, high-accuracy
marching. Input consumed: `phaseA_problem_brief.md` ONLY. All citations are
open literature.

Notation: per-phase state U = (rho, u_x, u_r, u_theta, p) (or entropy form),
axisymmetric coordinates (x, r); q_m = meridional speed (u_x^2+u_r^2)^{1/2};
a = a(T, composition) frozen sound speed; M_m = q_m/a meridional Mach number;
Omega = 2*pi*f/n wave angular speed; phi = theta - Omega*t co-rotating angle;
Gamma_circ = r*u_theta streamline angular momentum; H = h(T) + |u|^2/2 total
enthalpy; S entropy. "Front" = codimension-1 discontinuity (shock or contact).
"Spacelike" (for steady marching) = initial-value surface crossed with
supersonic normal velocity, u·n > a (Courant–Friedrichs; Zucrow–Hoffman).

---

## 0. LENS READING OF THE PROBLEM

From the hyperbolic standpoint this problem is FOUR nested well-posedness
problems wearing an optimization coat:

1. An EXACTNESS problem: J_exact is a time average of an unsteady 3D
   hyperbolic flow; the surrogate J is an ensemble of steady axisymmetric
   solves. The bridge is not asymptotic (Strouhal marginal); it must be
   STRUCTURAL. The structure available: under H-DATA the unsteady data is a
   single traveling wave in (theta - Omega*t), so the exact flow is a
   candidate STEADY flow in the co-rotating frame. This collapses the
   "unsteadiness correction" into a computable 3D-vs-axisymmetric commutator
   plus a downstream-stability (front/shear-layer stability) question.
2. A SOLUTION-CONCEPT problem: multi-D weak solutions of compressible Euler
   are catastrophically non-unique (convex-integration "wild" solutions,
   De Lellis–Székelyhidi 2010; Chiodaroli–De Lellis–Kreml 2015 even for
   Riemann data). Certification is only meaningful in a class where
   uniqueness and continuous dependence are theorems or at least certifiable
   monitors: piecewise-smooth solutions with finitely many admissible,
   uniformly stable (Majda) fronts on domains of determinacy.
3. A MARCHING problem: per phase, where the flow is supersonic in the
   marching sense, the steady BVP is a Cauchy/Goursat problem solvable to
   high accuracy by characteristics; every failure of that structure
   (subsonic patch, sonic surface, embedded strong shock, axis, free
   boundary, corner) is a named special region with its own contract.
4. A DERIVATIVE-FIDELITY problem: every state-model choice (fitted vs
   captured, limiter class, front topology changes in design space and in
   phase xi) propagates into whether dJ/dS exists, what it contains
   (front-motion delta terms), and whether the adjoint computes it.

The tree below is organized so that the four structural decisions above are
taken FIRST (they are load-bearing); everything else is local.

---

## 1. FORMULATION FAMILIES (the ladder, and what selects among them)

- FF-A  QUASI-STEADY PHASE ENSEMBLE, FITTED/CHARACTERISTIC INSTRUMENT.
  Per mu-a.e. xi: steady axisymmetric (with swirl) rotational Euler in
  Omega(S), solved by characteristic marching with FITTED primary fronts
  (rotational MoC / shock-fitting marching a la Salas SEAGULL). Objective
  J = integral over xi. Highest per-solve accuracy and the cleanest adjoint;
  restricted to certifiable (piecewise-smooth, marching-compatible) states.
- FF-B  QUASI-STEADY PHASE ENSEMBLE, CONSERVATIVE CAPTURED WORKHORSE.
  Same ensemble, states solved by entropy-stable shock-capturing steady
  solver (pseudo-time or space-marching where spacelike). Sector-agnostic,
  robust near certification boundary; lower per-solve fidelity, adjoint
  needs front-consistency care.
- FF-C  CO-ROTATING-FRAME 3D STEADY REFERENCE. One steady 3D solve in the
  frame rotating at Omega with Coriolis/centrifugal sources; under H-DATA
  this is the EXACT flow if stable. Used as rung for requirement (v), not
  as the design loop engine (cost).
- FF-D  TIME-PERIODIC UNSTEADY REFERENCE (harmonic balance / time-spectral,
  Hall–Thomas–Clark 2002; Gopinath–Jameson 2005). Validates FF-C when
  rotating-frame steadiness is doubted; top rung of the ladder.
- FF-E  VARIATIONAL DIRECT-DESIGN LAYER (Guderley–Hantsche 1955; Rao 1958;
  Shmyglevsky; Kraiko's variational gasdynamics school). Per-phase exact
  optimum via control-surface/characteristic reduction; in this problem it
  is NOT the optimizer (the shared contour breaks the reduction — FORK-35)
  but it IS the globality-bound generator (FORK-37).
- FF-F  NON-DETERMINISTIC SEARCH LAYER (GA/CMA-ES, Bayesian optimization,
  DoE, ML surrogates). Never certifying; admissible only as sector-census
  proposal generators feeding FF-A/B evaluations (FORK-36).

Selection criteria: (c1) certificate availability (can the family EMIT the
(i)–(v) certificates, not merely numbers); (c2) solution-class control (does
the family know which weak solution it computes); (c3) adjoint consistency;
(c4) cost per certified evaluation; (c5) sector generality. Recommended
architecture: FF-A as certifying instrument + FF-B as robust workhorse and
cross-oracle, FF-C/FF-D as the (v) ladder, FF-E as bound generator, FF-F
quarantined to proposals. Idealization ladder (each rung with a measured
defect carrier): quasi-1D -> per-phase axisymmetric ensemble (FF-A/B) ->
rotating-frame 3D steady (FF-C) -> time-periodic unsteady (FF-D).

---

## 2. FORKS

### GROUP A — OBJECTIVE STRUCTURE AND EXACTNESS LADDER

---

FORK-1: How is J_exact related to computable steady objects?
- Question: what exact structural bridge connects the long-time average
  J_exact to steady computations, given Strouhal is MARGINAL (no quasi-steady
  asymptotics allowed)?
- Options (full space):
  - (a) Quasi-steady limit St->0: classical, but the brief pins St marginal —
    an asymptotic bridge at its best is still an uncontrolled O(St) claim here.
  - (b) Co-rotating-frame steadiness: if data is a pure rotating wave
    (H-DATA), seek the steady solution in phi = theta - Omega*t. If it exists
    and is the attractor, J_exact EQUALS its thrust with NO Strouhal error.
  - (c) Time-periodic solve (harmonic balance/time-spectral): compute the
    periodic attractor directly, average over one period; exact under
    periodicity of the attractor, no rotating-frame assumption.
  - (d) Unsteady statistical bracketing: long-time LES-free unsteady Euler
    runs with liminf/limsup estimators and confidence bands; assumes nothing,
    certifies least, costs most.
  - (e) Linearized-unsteady correction about the phase ensemble (small
    perturbation in mode amplitude): perturbative in the WRONG parameter
    here (fluctuation is O(1) across the cycle) — usable only for the
    residual after (b).
- Decision criterion: existence + stability of the rotating steady solution
  (checkable: FF-C solve converges; front/shear-layer stability monitors of
  FORK-13 pass). If yes, (b) is EXACT: dry proof below. If FF-C solve fails
  or is unstable, fall to (c); if the attractor is not periodic (H-DATA
  violated downstream), fall to (d) brackets.
- Dry proof (exactness of (b)): let the exact flow be a traveling wave,
  U(t, x, r, theta) = V(x, r, theta - Omega*t). The thrust integrand on any
  axisymmetric control surface is G(x, r, theta - Omega*t); F_S(t) =
  int_0^{2pi} int G(x, r, theta - Omega*t) dl dtheta = int_0^{2pi} int
  G(x, r, phi) dl dphi, t-independent by periodicity of the theta-integral.
  Hence F_S(t) = const = J_exact; the limit exists trivially and equals the
  steady rotating-frame thrust. QED. Hypotheses: H-DATA; existence of V;
  V is the attractor (else FORK-3).
- Recommendation: (b) as the exactness anchor, with (c) as its falsifier
  rung and (d) as last-resort bracket. Grounds: it is the ONLY bridge that
  is exact at marginal Strouhal; it converts requirement (v) from an
  asymptotic apology into two measurable terms (FORK-39).
- Falsifier: an FF-D time-periodic solve whose period-average thrust differs
  from the FF-C steady value beyond derived discretization bands (would show
  the rotating steady state is not the attractor); or an H-DATA monitor trip.

---

FORK-2: What IS the per-phase steady problem of the surrogate?
- Question: J = int F[S; s(xi)] dmu needs a definition of the per-phase
  state problem; which one?
- Options:
  - (a) Axisymmetric steady Euler with xi-frozen data on all of Gamma_d
    (each phase sees a uniform-in-theta copy of its instantaneous state):
    the classical cycle-average surrogate; 2D meridional cost.
  - (b) 2D planar "unrolled" channel at fixed radius with the wave passing:
    best for combustor physics, wrong for nozzle area ratio and axis — no
    thrust fidelity.
  - (c) 3D rotating-frame steady (= FF-C): not a surrogate, the reference.
  - (d) Sectorized 3D: azimuthal wedge with phase-shifted periodic BCs
    (phase-lag methods, turbomachinery practice): intermediate cost,
    intermediate fidelity.
  - (e) Reduced-order/POD or ML emulator of the phase family: fast, no
    certificates; verification burden re-imports the full solves.
- Decision criterion: the surrogate must (i) admit per-phase certificates
  (well-posed axisymmetric BVP), (ii) make the xi-integral of gradients
  meaningful for ONE shared axisymmetric S, (iii) have a measurable defect
  against FF-C. Only (a) satisfies all three at ensemble cost.
- Recommendation: (a), with the (a)-vs-(c) commutator measured, not assumed
  (FORK-39): the defect of (a) is the azimuthal-flux commutator — the
  axisymmetric ensemble deletes the d/dtheta transport of axial momentum by
  cycle fluctuations, whose magnitude is set by the helix angle
  tan(alpha_h) = Omega*r/u_x (the geometric face of the marginal Strouhal).
- Falsifier: FF-C minus (a)-ensemble thrust difference exceeding the (v)
  budget line assigned to the commutator at candidate optima.

---

FORK-3: Existence of the time average; bracket policy when the exact flow
does not settle to the rotating wave.
- Question: what certifies lim_{T->inf} exists, and what is declared if not?
- Options:
  - (a) Assume ergodic/periodic attractor silently — forbidden by the brief.
  - (b) Rotating-wave stability certificate: linear stability of the steady
    FF-C solution (global modes) + front-stability monitors (FORK-13);
    if stable, FORK-1 dry proof gives existence.
  - (c) liminf/limsup brackets from finite-T unsteady runs with
    a-posteriori convergence-of-averages estimators (batch means /
    spectral variance of F_S(t)); statistical, honest, wide.
  - (d) Statistical-solution / measure-valued framing (Fjordholm–Mishra
    school): principled home for non-settling flows; certificates about
    observables' expectations, weakest link = no uniqueness theory.
- Decision criterion: cheapest certificate that closes: run (b); only on
  failure open (c); (d) only as the declared conceptual home of (c)'s
  brackets.
- Recommendation: (b) primary. Key lens fact: the plume free boundary is a
  vortex sheet against quiescent ambient; 2D compressible vortex sheets are
  linearly stable for relative convective Mach > 2*sqrt(2) (Miles 1958;
  Fejer–Miles 1963) and KH-unstable below; axisymmetric/finite-thickness
  corrections via convective Mach number Mc (Papamoschou–Roshko 1988). The
  certificate must therefore CHECK Mc phase-by-phase rather than assert
  stability. Downstream shear-layer instability need not destroy J-existence
  (it may only unsteady the far plume, outside the thrust domain of
  influence — FORK-21), so couple this fork to the control-surface fork.
- Falsifier: measured F_S(t) in an FF-D/unsteady rung showing non-decaying
  low-frequency drift (average non-Cauchy in T) while monitors claimed
  stability.

### GROUP B — STATE MODEL AND SOLUTION CONCEPT

---

FORK-4: Solution class for the per-phase state (THE state-model fork).
- Question: in what class do we claim the per-phase solution lives?
- Options (each at its best):
  - (a) Globally smooth (C^1) solutions: strongest theory (classical
    characteristics; uniqueness on domains of determinacy, Li Ta-tsien &
    Yu Wen-ci 1985); attainable only for shock-free phases and contours —
    real for well-designed nozzles at design-adapted phases, false across a
    whole RDE cycle (over/underexpanded phases WILL make lip shocks).
  - (b) Piecewise-C^1 with finitely many FITTED admissible fronts
    (shocks + contacts), each a Lipschitz surface with Rankine–Hugoniot +
    Lax conditions enforced exactly, smooth in between: the classical
    supersonic-gasdynamics class (Courant–Friedrichs; Gu Chaohao 1962 curved
    wedge; S. Chen; Majda 1983 stability); uniqueness and continuous
    dependence available locally in this class; the class in which
    certification is a finite list of checks.
  - (c) Entropy weak solutions computed by capturing: robust, sector-agnostic,
    but (multi-D) the entropy conditions do NOT select uniquely
    (De Lellis–Székelyhidi 2010; Chiodaroli et al. 2015): "the scheme picks
    one" is not a certificate; captured fronts also degrade thrust accuracy
    (O(h) smearing through pressure integrals) and adjoint fidelity (FORK-29).
  - (d) Vanishing-viscosity selection: conceptually right (and physically the
    declared viscous layer), no multi-D theorems; usable only as the DECLARED
    selection principle that (b)'s admissibility conditions proxy.
  - (e) Measure-valued / statistical solutions: right home for uncertifiable
    turbulent regimes; no per-phase design certificates; park at the (d)-rung
    of FORK-3 only.
- Decision criterion: which class supports ALL of: uniqueness-relevant
  certificates, high-accuracy thrust, differentiable-in-S structure with
  explicit front-motion terms, and an audit that a computed object IS in the
  class. Only (b) does; (c) is the fallback where (b)'s structure breaks.
- Recommendation: (b) as the CERTIFIED class, (c) as the exploration/fallback
  class with an explicit downgrade flag. Certified optima must have states
  IN (b), certified by FORK-23 monitors. Non-uniqueness policy: work where
  uniqueness is a theorem or a checked monitor, never rely on scheme
  selection (FORK-5).
- Falsifier: a phase/design in the optimization basin whose state develops
  structure outside (b) — e.g., an unsteadily shedding Mach-disk pocket —
  that the FORK-24 boundary handling cannot exclude without emptying the
  feasible set.

---

FORK-5: Admissibility and uniqueness selection inside the weak class.
- Question: which admissibility conditions are ENFORCED and what is claimed
  from them?
- Options: (a) Lax characteristic count per front; (b) Liu E-condition
  (needed if the EOS loses genuine nonlinearity); (c) entropy-inequality
  (Clausius–Duhem) per front; (d) vanishing-viscosity declared limit;
  (e) wild-solution agnosticism (claim nothing; report scheme-selected).
- Decision criterion: EOS structure audit (FORK-6): if the fundamental
  derivative Gamma_fund > 0 over the operating (T, p) range, Lax = Liu for
  genuinely nonlinear fields and (a)+(c) suffice; else (b) is mandatory.
- Recommendation: enforce (a)+(c) at every fitted front, with (d) as the
  declared selection principle; dry note: in the piecewise-smooth class on a
  domain of determinacy, local uniqueness follows from characteristic energy
  estimates (Li–Yu theory) + Majda front stability — the wild-solution
  pathology lives in the unconstrained weak class, not in (b) with Lax
  fronts. The certificate line is exactly: "state is in class (b) with all
  fronts Lax-admissible and uniformly stable"; uniqueness claims are scoped
  to that.
- Falsifier: audit finds Gamma_fund <= 0 somewhere in range (BZT-like zone
  from the h(T) tables) — then Lax is insufficient and the front logic must
  be upgraded (composite waves, split shocks).

---

FORK-6: Thermally-perfect gas structure: characteristic thermodynamics.
- Question: gamma(T) non-constant kills closed-form invariants; what
  replaces them, and what must be AUDITED about h(T), cp(T)?
- Options:
  - (a) Local effective gamma (frozen gamma at each point): simple, wrong at
    O(dgamma/dT * DeltaT) across strong expansions — silently biases fronts.
  - (b) Exact characteristic ODE integration: MoC needs only local slopes
    (mu = asin(a/q_m)) and compatibility ODEs with a(T) from the frozen
    mixture; no closed-form Riemann invariants needed; Prandtl–Meyer
    generalizes to the exact quadrature dnu = sqrt(M^2-1) dq/q with M(q)
    from h(T)+q^2/2 = H — exact to quadrature tolerance (Zucrow–Hoffman
    treat arbitrary h(T)).
  - (c) Table-driven thermodynamics with certified interpolation error
    bounds feeding (b): the practical form of (b); interpolation error is a
    NAMED carrier in the (v) budget.
  - (d) Polytropic-fit calibration per phase: a modeling shortcut; rejected
    for certified runs (uncontrolled bias), retained as a cheap screen.
- Decision criterion: does the option contribute a bounded, evaluable model
  residual? (b)/(c) yes; (a)/(d) only with an extra calibration error term.
- Recommendation: (b) realized as (c). Mandatory audits: monotonicity of
  h(T); a^2 = (dp/drho)_S > 0; fundamental derivative Gamma_fund =
  1 + (rho/a)(da/drho)_S > 0 over the reachable (T,p) set (cheap quadrature
  over the table range) — this single audit underwrites FORK-5's use of Lax
  conditions and Majda's stability hypotheses.
- Falsifier: cross-check of the exact-quadrature Prandtl–Meyer function and
  quasi-1D h(T)-integral solutions against the table pipeline outside
  derived interpolation bands.

---

FORK-7: Swirl in the per-phase state model.
- Question: RDE exhaust carries azimuthal velocity; does the axisymmetric
  per-phase model carry u_theta?
- Options: (a) drop swirl (pure meridional Euler): cheaper, one fewer
  invariant; deletes a real thrust debit and — critically — overstates the
  spacelike margin; (b) axisymmetric-with-swirl Euler (d/dtheta = 0,
  u_theta /= 0): standard rotational MoC with a third streamline invariant
  Gamma_circ = r*u_theta (Zucrow–Hoffman); meridional characteristics
  unchanged in form (Mach lines from M_m), swirl enters source terms and
  invariants; (c) swirl as perturbative correction on (a): uncontrolled at
  O(1) swirl angles.
- Decision criterion: measured swirl angle in the data family s(xi). If
  max_xi |u_theta|/q is not small, (b) is forced by two theorems of the
  lens: (i) the marching/spacelike condition uses u·n vs a — swirl kinetic
  energy consumes margin (a total-Mach>1 flow can be axially subsonic);
  (ii) angular-momentum conservation makes swirl energy unrecoverable by an
  axisymmetric wall, a REAL objective debit the bound of FORK-37 must see.
- Recommendation: (b), unconditionally (the cost delta is one ODE invariant).
- Falsifier: data audit showing u_theta identically ~0 across the cycle
  (then (a) is a legitimate simplification with a named absent carrier).

---

FORK-8: PDE formulation for computation (per phase).
- Question: which form of steady rotational Euler is discretized?
- Options:
  - (a) Characteristic (MoC) form: 2 meridional Mach lines (C+/C-) + triple
    streamline characteristic carrying (S, H, Gamma_circ); highest accuracy
    per DOF in smooth regions; natural fitted-front interfaces; needs
    spacelike marching everywhere it is used.
  - (b) Conservative space-marching in x (steady flux-vector form, x as
    "time"): Godunov-type marching (Godunov et al.; SEAGULL-class fitted
    marching, Salas 1976; PNS practice for the hyperbolic core, Vigneron):
    conservation-exact across captured secondary fronts, same spacelike
    requirement.
  - (c) Pseudo-time relaxation of steady Euler (global FV/DG): no spacelike
    requirement, handles subsonic pockets; cost and captured-front penalties.
  - (d) Stream-function / von Mises coordinates: elegant for channel flows;
    degenerates at reversed/stagnant flow and complicates free boundaries —
    rejected as primary, retained as an oracle transform on benchmark flows.
  - (e) Potential + Clebsch/vorticity split: rotational inflow with entropy
    gradients makes full-potential invalid (Crocco: grad S, grad H, swirl
    all nonzero); rejected for the state, admissible only as an
    initialization ansatz.
- Decision criterion: certified accuracy per cost in the class of FORK-4(b),
  + fallback coverage. (a) and (b) are the two spacelike-marching realizations
  (FF-A instrument and conservative twin); (c) is the FF-B fallback.
- Recommendation: (a) as the certifying instrument with (b) as its
  conservation-exact twin oracle (disagreement beyond derived bands rejects
  a run — agreement is NOT truth, only non-rejection); (c) for uncertifiable
  or sonic-pocket states and as sector-agnostic explorer.
- Falsifier: an in-basin design where (a)/(b) disagree persistently under
  refinement (indicates a front or region outside the marching contract —
  route to FORK-24).

### GROUP C — FRONTS

---

FORK-9: Front inventory and per-type fit-vs-capture policy.
- Question: which discontinuities does a per-phase solution contain, and
  which are fitted vs captured?
- Expected inventory (from the physics of the cycle): (1) lip
  shock (overexpanded phases) or lip centered expansion (underexpanded);
  (2) wall-compression shocks from contour concavity or over-turned design;
  (3) internal contact/entropy surfaces where s(xi)|_{Gamma_d} has radial
  jumps (injector/annulus wakes); (4) the free plume boundary (a free
  streamline against Pa, not an internal front); (5) possibly a Mach
  disk/reflected-shock system in strongly overexpanded plumes (subsonic
  pocket — breaks marching).
- Options: (a) fit ALL fronts (pure Moretti doctrine: fitting as BC problem);
  (b) capture all (pure capturing doctrine); (c) hybrid: fit primary,
  isolated, certifiable fronts (lip shock, main contacts); capture weak
  secondary acoustic structure below a derived strength threshold;
  (d) front tracking (Glimm–Grove school): fitted interfaces inside a
  capturing bulk solver, the modern hybrid.
- Decision criterion: thrust-accuracy and adjoint-fidelity per front:
  fronts crossing the wall or the control surface, and fronts whose motion
  carries O(1) gradient information, MUST be sharp (fitted or tracked);
  fronts of strength below the discretization-error floor may be captured
  with the smearing charged to the (v) budget.
- Recommendation: (c)/(d): fit the lip system and any wall-incident shock;
  fit contacts that carry entropy-layer thrust bias; capture the rest in the
  FF-B twin. Front-strength threshold DERIVED: fit any front whose
  contribution to the DWR error estimate exceeds the assigned budget line.
- Falsifier: refinement study where the captured-secondary policy leaves a
  thrust increment that does not converge under h-refinement (a
  mis-classified primary front).

---

FORK-10: Fitting technology.
- Question: how are fitted fronts represented and advanced?
- Options: (a) floating/em bedded fitting (Moretti; Salas "A Shock Fitting
  Primer" 2010): front as internal moving boundary in a smooth mapping, RH
  solved as BC on both sides — reference accuracy, brittle at topology
  change; (b) boundary/shock-aligned coordinates (front is a mesh line;
  SEAGULL): ideal for marching + one primary shock family; (c) front
  tracking (Glimm et al.): interface elements over a capturing bulk —
  survives interactions, heavier machinery; (d) fitted-interface DG/cut-cell
  (modern reincarnations: implicit shock tracking / MDG of Zahr–Persson,
  Corrigan et al. HOIST): the front is a solution unknown of an optimization
  problem — the state solve itself becomes an optimization; highest-order
  accuracy at fronts currently known; (e) level-set-represented fronts with
  ghost-fluid RH closure: flexible topology, weaker conservation bookkeeping.
- Decision criterion: marching compatibility + topology-change frequency in
  the design basin (measured, FORK-11) + adjoint transparency (explicit RH
  linearization available?).
- Recommendation: (b) within FF-A marching for the primary lip/wall shock
  families (one front family per marching strip); (d) as the modern upgrade
  path if front-interaction complexity grows; (c) reserved for the FF-C 3D
  reference if fitted fronts are wanted there. Grounds: (b) gives the RH
  Jacobians in closed form for the adjoint (FORK-29).
- Falsifier: measured topology-change rate in the optimizer's trust region
  high enough that (b) restarts dominate cost — flips the choice to (d).

---

FORK-11: Spontaneous shock formation and front-topology change.
- Question: shocks BORN mid-domain (characteristic envelopes from
  compressive contour segments) and front intersections: how detected and
  handled without breaking certification or differentiability?
- Options: (a) pre-declared front skeleton per sector (fit only what the
  sector census predicts): fast, blind to surprises; (b) envelope detection:
  monitor the Jacobian of the characteristic map (crossing C+ or C-
  characteristics of the same family => formation point at the envelope
  cusp), then INSERT a fitted front there: the classical, rigorous detector;
  (c) capture-then-identify: run FF-B, locate fronts a posteriori (Ducros/
  limiter-activity sensors), re-run FF-A with the identified skeleton:
  robust two-pass; (d) implicit tracking (FORK-10(d)) where the skeleton is
  an unknown: no detector needed, cost in the solver.
- Decision criterion: certification demands NO undetected front: detector
  completeness is the criterion. (b) is complete for same-family
  compressions within marching; (c) is complete up to capturing resolution;
  combination closes the gap.
- Recommendation: (b) inside the FF-A march (it is cheap: the characteristic
  net is already there) + (c) as the independent cross-check per certified
  design. Every insertion/removal event is LOGGED as a stratification
  boundary in (S, xi) space — these are exactly the loci where J loses
  classical differentiability (see FORK-33/29).
- Falsifier: an FF-B posterior front map showing a front the FF-A run never
  inserted (detector incompleteness => certificate void; automatic rejector).

---

FORK-12: Contacts, slip lines, entropy layers.
- Question: treatment of linearly-degenerate fronts (no entropy production,
  no self-steepening, carry (S, H, Gamma_circ) jumps)?
- Options: (a) fit as streamline interfaces (in MoC the contact IS a
  streamline characteristic — fitting is free); (b) capture (contacts smear
  worst — linear fields, O(h^{p}) but with constant growth in march length);
  (c) diffuse-interface modeling: wrong physics layer here (single phase).
- Recommendation: (a) in FF-A always (zero extra cost, exact transport of
  the three streamline invariants by construction); in FF-B accept smearing
  but charge it: the entropy-layer smearing bias on thrust is a named (v)
  carrier, measured by the FF-A/FF-B twin diff.
- Falsifier: twin-diff residual attributable to contact smearing exceeding
  its budget line despite refinement (would force fitted contacts in FF-B
  too, i.e., front tracking).

---

FORK-13: Front stability certification.
- Question: fitted-front calculus assumes the fronts are stable objects;
  what is checked?
- Options / checks (these compose, not compete):
  - (a) Majda uniform stability of each shock front (Majda 1983): for an
    ideal-like EOS with Gamma_fund > 0 and moderate strength, shocks are
    uniformly stable; the D'yakov–Kontorovich (DK) parameters computed from
    the h(T) tables certify no spontaneous-emission regime.
  - (b) Vortex-sheet/shear-layer stability at contacts and at the plume
    boundary: relative/convective Mach criteria (Miles 1958: 2D supersonic
    stabilization above Mc = sqrt(2) per stream ~ relative 2*sqrt(2);
    Papamoschou–Roshko Mc for the finite-thickness layer); axisymmetric
    m-modes checked by a 1D compressible Rayleigh solve on extracted
    profiles.
  - (c) Steadiness-of-the-fitted-front residual: the front's normal-velocity
    residual under marching perturbation (a numerical stability monitor).
- Decision criterion: certificates (a)+(b) are hypotheses of the uniqueness
  and continuous-dependence claims of FORK-4(b) and of the shape-derivative
  calculus (front position must be a differentiable function of S); they are
  cheap (algebraic in table data + 1D eigen-solves) and mandatory.
- Recommendation: all three as standing monitors in the certification list
  (FORK-23). Note the honest scope: (b) instability of the FAR plume shear
  layer does not void the thrust certificate if the control surface
  decouples it (FORK-21); it voids the FF-C exactness claim unless FORK-3(b)
  passes upstream of the control surface.
- Falsifier: DK parameters out of stable range anywhere in the reachable
  state set (kills the fitted-shock calculus assumptions; escalate to
  composite-wave handling).

### GROUP D — SONIC, SUBSONIC, TRANSONIC STRUCTURE

---

FORK-14: Subsonic patches on Gamma_d: policy + causal-separation audit.
- Question: the data contract allows subsonic-axial patches with "an
  explicit closure"; which closure, and is causal separation even tenable
  there?
- Dry argument (the audit's core): where u·n < a on Gamma_d, the UNSTEADY
  system has characteristics leaving Omega through Gamma_d (u - a < 0
  normal family): the design domain talks back to the data side. The
  premise "no upstream influence of the design on the data" is then NOT a
  property of the interface location but of the CLOSURE: it holds iff the
  closure presents a design-independent impedance (e.g., choked feed) or
  absorbs all upstream-running waves. This must be audited, not assumed.
- Options:
  - (a) EXCLUDE: certified class requires u·n > a mu-a.e. on Gamma_d
    (monitor: measured margin field); subsonic-patch phases exit the
    certified class => J carries a declared missing-mass term for them.
  - (b) Choked-plenum closure: model the patch as fed by a choked upstream
    throat (design-independent mass flux; reflection coefficient from
    quasi-1D impedance): explicit, auditable, classical combustor practice.
  - (c) Characteristic/non-reflecting closure: specify exactly the incoming
    characteristic variables, zero reflection of outgoing ones (steady
    analog of Thompson/Poinsot–Lele/Giles BCs): clean math; the physical
    truth of zero reflection is itself an H-DATA-level hypothesis.
  - (d) Elliptic-patch embedding: solve the subsonic pocket as a locally
    elliptic steady BVP (stagnation data + declared downstream matching)
    coupled to the marching region across the sonic interface: the honest
    mixed-type solve; cost + a transonic matching problem (FORK-15).
  - (e) Full upstream coupling to a combustor model: violates the brief's
    interface contract (Gamma_d is the data boundary); named and rejected
    for scope, flagged as the only fallback if the audit kills (a)-(d).
- Decision criterion: measured data: does the given family s(xi) actually
  contain subsonic-axial patches (compute u·n/a over Gamma_d x Xi)? If no:
  (a) costs nothing — take it. If yes on small measure: (a) + declared
  missing-measure bound. If yes on O(1) measure: (b) or (d), with (b)
  preferred when the patch is fed annularly (physically a choked feed) and
  (d) when the pocket is internal to the nozzle flow.
- Recommendation: (a) as the certified default with the margin monitor as a
  standing audit; (b) as the declared closure for data families that need
  it. Grounds: every other option imports an unauditable hypothesis or
  breaks the data contract.
- Falsifier: margin monitor firing on O(1) phase-measure (forces the (b)/(d)
  branch and re-opens the causal-separation audit).

---

FORK-15: Sonic surface / embedded transonic region treatment.
- Question: when a sonic surface exists (choked closure of FORK-14(b)/(d),
  or a decelerated pocket behind a strong shock), how is the mixed-type
  region solved and certified?
- Options:
  - (a) Analytic transonic-throat expansions (Sauer 1944; Hall 1962;
    Kliegel–Levine 1969 toroidal-throat series): generate the supersonic
    start data just downstream of the sonic surface; classical, cheap,
    certified by residual evaluation; valid for smooth choked throats with
    moderate wall curvature; needs generalization audit for gamma(T)
    (series coefficients from local EOS derivatives — doable, an audited
    derivation).
  - (b) Time-marching capture through the throat (solve unsteady Euler to
    steady state in a throat-neighborhood subdomain): robust, general,
    resolution-hungry near the sonic line; the modern default when (a)'s
    hypotheses fail.
  - (c) Global mixed-type solvers (type-dependent differencing, Murman–Cole
    lineage; or fully implicit steady Newton with entropy fix): historical
    for potential flow; for full Euler, (b) subsumes it.
  - (d) Rigorous transonic BVP theory (Morawetz; Chen–Feldman transonic
    shock results): supplies structure theorems (perturbation stability of
    transonic shocks in nozzles), not a solver; used to justify local
    well-posedness of the matching in (d) of FORK-14.
- Decision criterion: hypothesis check of (a) (smooth wall, curvature
  radius/throat radius within series validity, no incident front on the
  sonic bubble); else (b).
- Recommendation: (a) where its audit passes, (b) as fallback; either way
  the sonic region OUTPUT is only consumed through FORK-16's start surface.
- Falsifier: residual of the series solution (plugged into full Euler)
  exceeding derived tolerance on the start surface (auto-fallback to (b)).

---

FORK-16: Start-surface placement: the limiting-characteristic rule.
- Question: where may the supersonic march begin?
- Dry argument: data on the sonic line itself is NOT admissible marching
  data (the system is parabolic-degenerate there; the sonic line is a
  characteristic envelope locus). The correct initial-value surface must be
  (i) strictly spacelike (u·n > a pointwise with certified margin) and
  (ii) downstream of the LIMITING CHARACTERISTIC (the last C- that returns
  to the sonic bubble): data upstream of it is still coupled to the elliptic
  region, so its "initial data" is not free (classical: Hall; Kliegel–
  Levine; nozzle-MoC practice per Zucrow–Hoffman).
- Options: (a) start on Gamma_d directly when Gamma_d is certified
  spacelike (the supersonic-inflow contract case): cleanest — the data IS
  the start line; (b) start on a constructed surface downstream of the
  limiting characteristic fed by FORK-15 output (choked-closure case);
  (c) start upstream and "iterate out" the inconsistency: rejected — it
  silently converts a BVP mis-posing into an uncontrolled relaxation error.
- Recommendation: (a) for supersonic phases; (b) for choked closures, with
  the limiting-characteristic location COMPUTED (trace the C- family from
  the sonic-bubble edge), never assumed at the geometric throat.
- Falsifier: marching solution differences under start-surface displacement
  beyond derived bands (indicates residual elliptic coupling => surface was
  not downstream of the limiting characteristic).

---

FORK-17: Spacelike certification, including the swirl margin.
- Question: what certifies, pointwise and per phase, that marching is valid?
- Options: (a) total Mach check M > 1: WRONG (swirl and flow angle can
  make u·n < a at M > 1) — named to reject it; (b) normal-velocity check
  u·n > a on every marching front with a derived positive margin
  epsilon_sl, margin propagated into the step-size/mesh contract (the
  numerical domain of dependence must contain the analytic one — the steady
  CFL analog); (c) eigenvalue check of the marching Jacobian (fully general,
  what (b) is the closed form of).
- Recommendation: (b) implemented, (c) as its generality audit. The margin
  epsilon_sl is DERIVED: the smallest margin for which the truncation-error
  and front-position error bounds hold uniformly (the error constants blow
  up as (u·n/a - 1)^{-1/2} near sonic — the derivation names this constant).
- Falsifier: any interior point of a certified run with u·n <= a
  (immediate certificate void; the state must be re-routed to FF-B + FORK-15).

### GROUP E — MARCHING SPECIFICS

---

FORK-18: Lip/corner treatment at attachment set Lambda.
- Question: the chamber lip is a corner: centered waves originate there;
  how is the singularity handled?
- Options: (a) Prandtl–Meyer centered-fan insertion (exact local solution;
  for gamma(T): the exact quadrature of FORK-6(b)) with fan discretized in
  wave-angle: classical, spectral-quality local accuracy; (b) local mesh
  clustering + capturing: smears the fan origin, pollutes downstream
  characteristics; (c) corner-fitted mapping (unfold the corner by a local
  singular map): elegant, extra machinery.
- Recommendation: (a): insert the exact centered solution as internal data;
  it is simultaneously the lip-shock generator on overexpanded phases (fan
  of compression -> immediate coalescence => fitted lip shock per FORK-11(b)
  detector at the corner itself).
- Falsifier: grid-refinement study of the captured alternative agreeing to
  band with fan insertion at lower cost (would demote (a) — not expected).

---

FORK-19: Axis r = 0 treatment.
- Question: the axisymmetric source terms (rho*u_r/r etc.) are singular on
  the axis; also u_theta must vanish like r (regularity of swirl:
  Gamma_circ -> 0). How is the axis handled — and WHEN is it even in the
  domain (sector-dependent: plug/aerospike solids may cover the axis)?
- Options: (a) L'Hopital limit equations at r=0 (replace v/r by dv/dr):
  the classical MoC axis unit process; (b) series expansion in r near the
  axis matched to the interior (removes the odd/even parity errors);
  (c) offset half-cell / staggered FV (capturing practice); (d) map to
  Cartesian-regular variables (u_r/r, Gamma_circ/r^2) with proven parity.
- Recommendation: (a)+(b): axis unit process with a one-term parity-correct
  series; enforce Gamma_circ = O(r^2)... audit: swirling data families
  CANNOT reach the axis with nonzero circulation — a vortex-core structure
  or an on-axis solid (plug) is REQUIRED; make this an explicit sector
  certificate (a bell sector with swirling flow through the axis region
  must show the computed vortex-core resolution or be rejected).
- Falsifier: refinement study on a swirling benchmark (exact rotational
  conical/source flows) showing order loss at the axis under (a) alone.

---

FORK-20: Free plume boundary (p = Pa) treatment.
- Question: the free portion of the boundary is a free streamline at
  constant pressure (unknown position); how is it computed?
- Options: (a) MoC free-boundary unit process (impose p = Pa, boundary is a
  streamline; its position emerges from the march): classical, exact-order;
  (b) capture the plume against a modeled quiescent ambient (two-state
  Riemann at the edge): smears the vortex sheet, but robust when the sheet
  destabilizes; (c) fixed outer computational boundary with non-reflecting
  BC and Pa forcing: simplest, boundary-placement error enters (v);
  (d) free-boundary theory framing (Alt–Caffarelli–Friedman jets): theory
  for subsonic/irrotational jets — names the mathematical object, does not
  provide the rotational supersonic solver.
- Recommendation: (a) in FF-A (the free boundary is one more characteristic
  interface — cheap in marching); (b) in FF-B. The free-boundary position
  is part of the state vector for the adjoint (its linearization is the
  free-boundary shape derivative — FORK-29 must carry it).
- Falsifier: FF-A/FF-B twin diff on plume-influenced sectors (plug, E-D)
  exceeding band — indicates sheet instability or capture bias; route to
  FORK-13(b)/FORK-21.

---

FORK-21: Control-surface placement and the plume-decoupling certificate.
- Question: where is thrust evaluated, and how much plume must be SOLVED?
- Dry argument (domain of influence): if on a candidate exit surface
  Sigma_e every point is spacelike (u·n > a) and no wetted solid lies
  downstream of Sigma_e, then no state change downstream of Sigma_e can
  influence the flow on or upstream of Sigma_e (finite domain of influence
  of hyperbolic systems + steady spacelike separation). Thrust computed on
  (wetted wall) + Sigma_e is then EXACT regardless of plume fate — Mach
  disks, sheet instability, ambient mixing downstream are all outside the
  certificate's domain of dependence.
- Options: (a) exit-plane surface with certified spacelike property (bell
  sectors): minimal solve, maximal certificate; (b) extended control
  surface enclosing plug/E-D surfaces whose SOLID extends into the plume
  region: the wetted-wall integral needs the local plume solve; decoupling
  only downstream of the last wetted point; (c) far-field enclosing surface:
  needs the whole plume — reject except as an unsteady-rung consistency
  check (momentum bookkeeping).
- Recommendation: (a) with per-sector fallback (b); the decoupling
  certificate (pointwise spacelike check on Sigma_e + geometry check) is a
  standing monitor. This is what makes strongly-overexpanded phases with
  Mach disks CERTIFIABLE for bell sectors: the disk lives downstream of
  Sigma_e; the state upstream remains in class FORK-4(b).
- Falsifier: any wetted point downstream of a non-spacelike locus (e.g.,
  plug surface washed by a subsonic pocket): the certificate for (a)/(b)
  fails and the phase must be solved in FF-B with the pocket resolved.

### GROUP F — WELL-POSEDNESS AND CERTIFICATION

---

FORK-22: Per-phase BVP well-posedness framework.
- Question: on what theory does the claim "the per-phase problem is
  well-posed" stand?
- The characteristic-counting table (with-swirl steady system, 5 unknowns;
  meridional Mach lines C+/C- + triple streamline):
  - Spacelike inflow (Gamma_d, supersonic contract): ALL 5 characteristics
    enter => prescribe full state s(xi). Well-posed Cauchy data.
  - Solid wall (slip): streamline boundary; exactly ONE characteristic
    (the incident Mach line's reflection partner) leaves the boundary
    into the domain => exactly ONE condition (u·n_wall = 0). Count matches.
  - Free boundary (p = Pa): boundary is unknown; TWO conditions (pressure +
    streamline condition) against one incoming characteristic + one
    boundary-position DOF. Count matches (classical free-streamline BVP).
  - Supersonic outflow: zero incoming characteristics => zero conditions.
  - Subsonic-normal patch: counting fails (locally elliptic steady
    operator) => FORK-14's closure supplies the missing structure.
- Options for the theory shelf: (a) classical C^1 theory on domains of
  determinacy (Courant–Friedrichs; Li Ta-tsien & Yu Wen-ci: global classical
  solutions of quasilinear hyperbolic BVPs with characteristic boundaries);
  (b) piecewise-smooth existence/stability near fitted fronts (Gu Chaohao
  1962; Schaeffer; Majda 1983; S. Chen's supersonic-flow BVPs; Chen–Feldman
  for transonic patches); (c) small-BV multi-D theory: absent (state
  honestly: no global multi-D BV theory exists — certificates are LOCAL +
  monitored); (d) numerical well-posedness only (Kreiss/GKS-stable
  discrete BCs): necessary but not a substitute for (a)/(b).
- Recommendation: (a)+(b) as the theorem shelf with explicitly LOCAL scope,
  monitors (FORK-23) covering the gap to global claims; (d) enforced at the
  discrete level (GKS/SBP-SAT-style boundary implementations in FF-B).
- Falsifier: a certified-in-monitors state that fails continuous dependence
  in practice (two adjacent phases xi, xi' with certified states but O(1)
  thrust difference not explained by front-topology stratification —
  route to FORK-33's event detection or declare an ill-posedness boundary).

---

FORK-23: Solution-class membership certification (the monitor list).
- Question: what is CHECKED, per phase and design, to certify the state is
  in class FORK-4(b)?
- The list (each with derived tolerance; composition, not options):
  (m1) fitted-front RH residuals <= tol_RH (derived from DWR thrust budget);
  (m2) Lax count verified per front (characteristic families converge);
  (m3) entropy inequality strictly satisfied across each front;
  (m4) inter-front smoothness monitor (scaled derivative bounds vs mesh —
       no undetected front, cross-checked by FORK-11(c));
  (m5) spacelike margin field u·n/a - 1 >= epsilon_sl (FORK-17);
  (m6) numerical domain of dependence contains analytic (steady-CFL audit);
  (m7) front-stability certificates (FORK-13: Majda/DK, Mc at sheets);
  (m8) axis-regularity residual (FORK-19), corner-fan residual (FORK-18);
  (m9) twin-oracle non-rejection: |FF-A - FF-B| within derived band on J
       and on wall-pressure traces (agreement is only a non-rejection);
  (m10) attachment margin g_sep <= 0 (FORK-38) and plume-decoupling
       geometry (FORK-21).
- Recommendation: certificate = conjunction m1–m10, emitted as a machine-
  checkable record per (S, xi). NO state consumed by the optimizer or the
  averaging quadrature without its record (FORK-24).
- Falsifier: any monitor firing; additionally the monitor SET is falsified
  as insufficient if the FF-C/FF-D rungs reveal a bias not covered by any
  monitor's budget line (then the list grows — the list is versioned).

---

FORK-24: The certification boundary inside the optimization loop.
- Question: what does the optimizer do when a candidate design has phases
  whose state cannot be certified?
- Options: (a) hard rejection (infeasible point; filter/trust-region
  shrink): safe, can stall progress along the boundary; (b) certifiability
  as an explicit inequality constraint via its margins (min over monitors
  of signed margin >= 0, smoothly aggregated): lets the optimizer SEE the
  boundary and walk along it — margins m5, m7, m10 are differentiable
  fields, m1–m4 are residuals with derivative structure; (c) penalization/
  relaxation of certification: rejected — a certificate is not tradeable;
  (d) two-phase strategy: FF-B exploration ignoring certification, then
  certified FF-A polishing inside the certifiable set: pragmatic, risks
  polishing into a different basin.
- Recommendation: (b) primary with (a) as backstop for monitor classes
  without usable margins; the certified-class boundary becomes part of the
  active set in the KKT system (its multiplier prices "how much J is being
  held back by certifiability" — decision-relevant information the brief's
  (ii) explicitly wants multipliers to carry).
- Falsifier: optimizer trajectories that converge to boundary points where
  the margin gradients are degenerate (LICQ failure at the certification
  boundary) — forces the (a)/(d) fallback and flags the boundary structure
  for study.

### GROUP G — DISCRETIZATION

---

FORK-25: Primary discretization + oracle pairing (concretizing FORK-8).
- Question: which concrete schemes fill FF-A and FF-B?
- Options for FF-A (marching instrument): (a) classical 2nd-order
  predictor-corrector MoC network with fitted interfaces (Zucrow–Hoffman
  unit processes: interior, wall, axis, shock, free-boundary, fan): the
  reference craft; (b) higher-order characteristic marching (3rd+ order
  compatibility integration): more accuracy per point, more brittle at
  fronts; (c) conservative Godunov-type space marching with fitted primary
  shocks (SEAGULL-class): conservation-exact, robust.
  Options for FF-B (workhorse): (d) entropy-stable finite volume (Ismail–Roe
  / Chandrashekar fluxes, Tadmor framework) with smooth flux-limiting;
  (e) DG / flux-reconstruction high order with subcell shock capturing;
  (f) WENO finite difference; (g) residual distribution (Abgrall);
  (h) active flux (Eymann–Roe): elegant characteristics-native FV hybrid,
  younger verification base; (i) implicit shock tracking (HOIST/MDG —
  doubles as FORK-10(d)).
- Decision criterion: FF-A wants maximal smooth-region order with exact
  front interfaces and closed-form Jacobians (adjoint!); FF-B wants entropy
  stability + differentiability of the discrete map (FORK-28) + sector
  robustness.
- Recommendation: FF-A = (a) upgraded toward (c) for conservation aud its;
  FF-B = (d) (entropy-stable FV, smooth limiters) with (e) as the
  high-order upgrade path; (h)/(i) tracked as modern options, adopted only
  after oracle-suite qualification. Oracles for both: exact gamma(T)
  quadrature solutions (quasi-1D, Prandtl–Meyer, source/conical rotational
  flows integrated by ODE), plus manufactured solutions (MMS, Roache) for
  the axisymmetric-with-swirl operator including axis terms.
- Falsifier: order-verification on the oracle suite failing declared orders
  (scheme disqualified from certified duty).

---

FORK-26: Error estimation for the state and for J.
- Question: which error estimator carries the discretization term of (v)?
- Options: (a) goal-oriented adjoint-weighted residual (DWR,
  Becker–Rannacher; Venditti–Darmofal): estimates the THRUST error
  directly — matches the certificate need; needs the adjoint (have it
  anyway); (b) Richardson/GCI (Roache): geometric-refinement based,
  order-assumption fragile at fronts, cheap cross-check with MEASURED
  observed order; (c) characteristic truncation-error transport: lens-native
  (propagate local truncation along characteristics to the thrust surface):
  sharp in smooth marching regions, exotic machinery; (d) residual-based
  energy estimates: bounds in wrong norms for a thrust functional.
- Recommendation: (a) primary (it also drives adaptation, FORK-27, and
  supplies the derived tolerances of FORK-40); (b) as an independent
  cross-check with measured order; safety factors DERIVED from the ratio of
  estimated-to-realized error on the oracle suite (no magic 1.25).
- Falsifier: DWR estimate under-predicting true error on oracle problems
  outside its own stated band (estimator disqualified; fall to (b) with
  penalty in the budget).

---

FORK-27: Mesh / refinement policy.
- Question: how are points placed, per phase and design iteration?
- Options: (a) characteristic-net-native meshing (FF-A): the march inserts/
  removes characteristics to bound cell aspect and expansion spreading —
  the classical MoC policy, automatically front-aligned; (b) metric-based
  anisotropic adaptation driven by DWR (FF-B); (c) uniform-family
  refinement studies only (verification role); (d) moving-mesh/ALE
  r-adaptation to fronts: subsumed by fitting in FF-A; (e) design-frozen
  meshes with mesh-deformation across design steps: needed for gradient
  consistency (avoid remeshing noise in dJ/dS): mesh-morphing with occasional
  re-generation + gradient-consistency re-verification at re-generation
  events.
- Recommendation: (a) for FF-A, (b) for FF-B, (e) as the design-loop mesh
  contract, (c) as the verification harness.
- Falsifier: gradient-verification failures (FORK-31) traced to remeshing
  events (would tighten the (e) contract or force fully fixed topologies
  per trust region).

---

FORK-28: Captured-fallback differentiability: limiter and flux class.
- Question: FF-B must be differentiated (adjoint/AD); nonsmooth limiters
  and entropy fixes break that; what class is admissible?
- Options: (a) nondifferentiable classics (minmod, Roe with hard entropy
  fix): best shock crispness, kills gradient consistency; (b) smoothed
  limiters / C^2 flux functions (van Albada-type, smoothed |.|, Harten
  regularization) with the smoothing parameter DERIVED (tied to the local
  truncation floor, not magic); (c) entropy-stable smooth fluxes (Ismail–
  Roe, Chandrashekar) + subcell viscosity with smooth sensors; (d) treat
  nondifferentiability head-on: generalized/Clarke derivatives, shift-
  differentiability theory for conservation laws (Ulbrich 2002; Bouchut–
  James; Bressan–Marson L1 sensitivity): the rigorous frame in which
  captured-front sensitivities make sense at all — heavy, but it NAMES what
  the smoothed options approximate; (e) differentiate-the-physics only
  (continuous adjoint, ignore discrete nonsmoothness): inconsistent
  gradients at fixed mesh, self-consistent at convergence.
- Recommendation: (c)+(b) for FF-B, with (d) on the theory shelf as the
  justification and as the analysis of what error the smoothing introduces;
  FF-A largely sidesteps the issue (fitted fronts => piecewise-smooth
  discrete map).
- Falsifier: dot-product/complex-step tests (FORK-31) failing at fronts
  beyond the derived smoothing-error band.

### GROUP H — DERIVATIVES, ADJOINT, CURVATURE

---

FORK-29: Fronts in the derivative/adjoint calculus (THE fidelity fork).
- Question: dJ/dS contains front-motion terms; which formulation computes
  them correctly?
- Dry proof that naive capturing gets it wrong (1D archetype): J = int p dx
  on a shocked quasi-1D nozzle; perturb the design parameter alpha: the
  exact derivative contains -[p](x_s) * dx_s/dalpha (shock-motion delta
  term). A captured scheme differentiated naively at fixed mesh converges
  to the WRONG gradient (O(1) error persists as h->0 unless the adjoint
  satisfies an internal boundary condition at the shock and the linearized
  state carries the front-displacement Dirac). Giles–Pierce (JFM 2001,
  quasi-1D analytic adjoint) exhibit the correct adjoint: CONTINUOUS across
  the shock with an internal condition equivalent to linearized RH. In 2D
  the shock becomes a linearized-RH interface (Majda's linearization);
  fitted formulations impose it explicitly; captured ones approach it only
  with front-resolving refinement or shift-derivative machinery.
- Options: (a) fitted-front adjoint: linearize RH + front position as
  explicit unknowns; adjoint internal conditions in closed form; the
  free-boundary (plume) linearization rides the same machinery; exact
  front-motion gradient terms by construction; (b) captured adjoint +
  aggressive front refinement + smooth limiters: converges in the limit,
  cost blow-up at fronts, verified only statistically; (c) shift-
  differentiability calculus (Ulbrich; Bardos–Pironneau): rigorous
  captured-side sensitivity theory (1D solid, multi-D partial): the
  justification layer for (b); (d) continuous-adjoint with explicit shock
  treatment (Baeza–Castro–Palacios et al.): OtD twin of (a).
- Recommendation: (a) in FF-A as the gradient of record, (d) as its
  continuous twin for consistency checks, (b) only for FF-B exploration
  gradients (flagged non-certified). The averaged gradient is the
  mu-integral of per-phase adjoint wall tractions + front terms (the
  "averaged wall condition" of requirement (ii) emerges here).
- Falsifier: complex-step (or dual-number) differentiation of the whole
  FF-A marching code vs adjoint gradient disagreeing beyond derived
  round-off/truncation bands, on cases WITH moving fitted fronts.

---

FORK-30: Optimize-then-discretize vs discretize-then-optimize.
- Question: which side of the diagram is primary?
- Options: (a) DtO (discrete adjoint of the actual marching code, by
  hand-structured reverse or AD): gradients exactly consistent with the
  computed J (optimizer sees a true gradient of the evaluated function);
  the marching structure makes the discrete adjoint a BACKWARD march —
  lens remark: the adjoint of a spacelike-marching hyperbolic solve is
  itself a hyperbolic march in reversed direction (adjoint characteristics
  = reversed Mach cone), so the discrete adjoint is as cheap as the primal
  and needs NO stored global Jacobian, only the strip states (checkpointing
  along x); (b) OtD (continuous adjoint PDE + its own discretization):
  cleaner interface/front conditions, gradient of the CONTINUOUS J (may
  mismatch discrete J at coarse mesh, confusing line searches); (c) both,
  with the diff as an error estimator: the diff FF-A-DtO vs OtD is itself a
  discretization-error indicator on the optimality system.
- Recommendation: (c) operationally: DtO gradient feeds the optimizer; OtD
  twin computed at audit points; their difference must contract under
  refinement at the verified order (a standing rejector).
- Falsifier: non-contracting DtO/OtD diff (front condition or BC mis-
  linearized somewhere — halts certification).

---

FORK-31: Gradient mechanics and verification duties.
- Question: how are derivatives produced and PROVEN?
- Options (compose): (a) hand-structured discrete adjoint of the marching
  unit processes (closed-form Jacobians — feasible because unit processes
  are small algebraic solves); (b) reverse-mode AD of FF-B (with the
  FORK-28 smooth-flux contract); (c) complex-step / dual-number
  differentiation as the verification oracle (machine-precision tangents;
  valid because unit processes are analytic — table interpolants must be
  complex-safe / analytic splines); (d) finite differences: only as a
  coarse sanity ladder (step-size dilemma documented, derived steps).
- Verification duty (standing): per release and per new sector: tangent-
  adjoint dot-product identity to round-off; complex-step vs adjoint on
  full J including fitted-front motion and free-boundary terms; gradient
  order-of-agreement under mesh refinement.
- Recommendation: (a)+(c) for FF-A; (b)+(c) for FF-B; (d) demoted to
  smoke test.
- Falsifier: any duty failing beyond derived bands.

---

FORK-32: Second-order machinery for requirement (iii).
- Question: how is the reduced Hessian on the active tangent cone
  certified negative-semidefinite (max problem)?
- Options: (a) Hessian-vector products via tangent+second-adjoint pairs
  (exact, one extra linear march pair per product) + Lanczos extremal
  eigenvalue estimation on the active tangent cone: certificate =
  lambda_max(reduced Hessian on cone) <= 0 + derived resolution band;
  (b) BFGS-approximation curvature: optimizer-internal only, no
  certificate; (c) full dense reduced Hessian assembly: only for low-dim
  design bases (may be USED at the polishing stage if the certified basis
  is deliberately low-dimensional); (d) front-motion second-order terms:
  the Hessian carries second-order front terms (curvature of RH manifold);
  fitted formulation exposes them; captured Hessians at fronts are
  unreliable (square the FORK-29 pathology).
- Recommendation: (a) with (d) handled by the fitted linearization; (c) as
  cross-check when dim <= O(50).
- Falsifier: Hessian-vector products failing symmetry tests
  (<H v, w> = <v, H w>) beyond round-off band.

---

FORK-33: Phase quadrature and aggregation across xi.
- Question: J and dJ/dS are mu-integrals; F[S; s(xi)] is only PIECEWISE
  smooth in xi (front-topology events: lip shock appears/disappears at
  critical phases, Mach disk enters/leaves the decoupled zone): how to
  integrate certifiably?
- Options: (a) fixed Gauss quadrature over Xi: spectral on smooth
  integrands, silently wrong across kinks; (b) event-detected stratified
  quadrature: locate topology-event phases xi* (the FORK-11 logs give
  them), integrate smoothly within strata, sum: certifiable remainder;
  (c) adaptive quadrature with error control on both J and gradient
  integrals; (d) Monte Carlo / QMC over mu: needed only if mu is given as
  samples; variance-based bands; (e) SAA-style fixed sample set for
  optimization stability with a posteriori re-quadrature at certificates.
- Recommendation: (b)+(c): stratify at detected events, adapt within
  strata, quadrature error a NAMED (v) line; the gradient integral uses the
  same strata (dF/dS is discontinuous across events even where F is
  continuous). If mu arrives as data samples: (e) for the loop, (b) for the
  certificate.
- Falsifier: quadrature-refinement study moving J by more than its declared
  band (missed stratum boundary).

### GROUP I — DESIGN REPRESENTATION AND OPTIMIZATION

---

FORK-34: Design representation of the solid S.
- Question: how is S parametrized for computation, given topology sectors
  are OUTPUTS and the state solver wants clean walls?
- Options (full breadth):
  - (a) Per-sector body-fitted wall curves: splines/B-splines or Bezier with
    curvature/angle bound constraints; NURBS/isogeometric for exactness;
    CST (Kulfan) for aero-natural bases; Hicks–Henne bumps for increments.
    Best derivative behavior; sector topology fixed per branch.
  - (b) FFD/mesh-morphing boxes: representation-agnostic smooth deformations.
  - (c) Level-set representation of S (Allaire–Jouve–Toader; Osher–Santosa):
    topology changes free; but slip BCs on implicit boundaries force
    cut-cell/immersed treatment that degrades front fidelity and marching
    accuracy at the wall — a direct conflict with the FF-A instrument.
  - (d) Density/SIMP topology optimization (Bendsoe–Sigmund; Borrvall–
    Petersson flow variants): porous intermediate material has no meaning
    in slip-wall compressible Euler; rejected for the state model, noted as
    the field's TO default (rejected FOR A REASON: no admissible
    intermediate-density physics here).
  - (e) Phase-field: same objection as (d), smoother mathematically.
  - (f) Two-level representation: DISCRETE sector variable (bell / plug /
    shrouded plug / E-D / ...; the attachment set Lambda circles fix
    admissible anchors) x CONTINUOUS per-sector wall parametrization (a).
  - (g) ML-generative parametrizations (autoencoder shape spaces): compact,
    unverifiable admissibility; reject for certified loop, allow inside
    FF-F proposals.
- Decision criterion: the certified loop needs (i) exact wall geometry for
  slip + fitted fronts, (ii) uniform cone condition enforceable by
  constraint (min feature/angle bounds map to spline coefficient
  constraints), (iii) shape derivatives via Hadamard boundary form.
- Recommendation: (f) with (a) inside sectors ((b) as the mesh-motion
  carrier); (c) allowed ONLY in the FF-B exploration layer to DISCOVER
  sector candidates, whose output is re-instantiated as (f) before any
  certificate. Existence framing for (i): the class A(c) with uniform cone
  property is compact for Hausdorff-type convergence (Chenais 1975); J
  upper-semicontinuity along certified sequences is the part to prove/
  monitor (front-stable continuous dependence — FORK-13/22), with a
  declared failure boundary where certification is lost.
- Falsifier: a sector-census argument or FF-B/level-set exploration finding
  an in-envelope topology not expressible by the declared sector list
  (list is versioned; certificate re-issued).

---

FORK-35: Optimality framework: does the classical exit-characteristic
reduction survive averaging?
- Question: single-state maximum-thrust nozzle theory (Guderley–Hantsche;
  Rao 1958; Shmyglevsky; Kraiko school, incl. rotational and gamma(T)
  extensions) reduces optimality to conditions on ONE final characteristic
  (control surface) — does that survive the mu-average with a SHARED wall?
- Dry argument (collapse of the reduction): Rao's construction trades the
  wall for a control characteristic C- of THE flow, using that the flow
  between the last wall point and C- is determined by data on C-. With a
  shared wall and a family of flows {U_xi}, each phase has its OWN final
  characteristic C-(xi) (different slopes, different footprints); there is
  no single control surface on which all phases' data live => the
  variational problem cannot be reduced to one characteristic's data. The
  correct first-order system is: per-phase adjoint BVPs (each a backward
  characteristic march, FORK-30) + ONE averaged wall condition
  int_Xi [adjoint-traction_xi(wall point)] dmu = 0 along the free wall arc,
  + averaged transversality at free endpoints (lip/exit), + complementarity
  with multipliers on active constraints (length, envelope, curvature,
  separation, certifiability) carrying marginal values. Rao's condition is
  recovered exactly when mu is a Dirac (single phase) — a mandatory
  consistency oracle.
- Options: (a) averaged-adjoint KKT system as above (nested: solve states,
  solve adjoints, update shape); (b) one-shot / full-space KKT (all phases'
  states+adjoints+design in one Newton): cost-optimal at scale, fragile
  certification bookkeeping; (c) per-phase Rao designs + a-posteriori
  compromise (average of optimal contours): NO optimality claim for the
  average (named and rejected as a heuristic — retained as initializer);
  (d) bilevel/minimax variants (worst-phase design): different problem
  (robust), noted for the FORK-36 breadth.
- Recommendation: (a), with (c) as initializer and the Dirac-mu Rao oracle
  as a standing rejector of the whole optimality implementation.
- Falsifier: Dirac-mu run of the averaged machinery failing to reproduce
  the classical single-phase optimal contour (within derived bands) for a
  calorically-perfect benchmark.

---

FORK-36: Optimizer class and globalization (breadth fork).
- Question: which optimizer drives the certified loop, and what may the
  non-deterministic layer do?
- Options (full space, each at its best):
  - (a) SQP / trust-region gradient methods with the certified adjoint:
    the only class that consumes the certificates natively (KKT residual =
    stationarity certificate (ii)); trust region interacts cleanly with the
    certification boundary (FORK-24).
  - (b) One-shot Newton-KKT: fastest at scale; adopt after (a) matures.
  - (c) Globalized multistart of (a) over sector x seed space: the honest
    deterministic globalization.
  - (d) Evolutionary/GA/CMA-ES: derivative-free, sector-agnostic, strong on
    discrete sector variables; no certificates, expensive per gain;
    ADMITTED as sector-census explorer only (FF-F), outputs re-certified.
  - (e) Bayesian optimization / GP surrogates (EGO, Jones et al.): sample-
    efficient global search on low-dim design spaces (sector-level trades,
    e.g., plug truncation fraction); surrogate error is not a certificate —
    same quarantine.
  - (f) DoE + response surfaces: mapping the basin structure for FORK-33
    stratification and multistart seeding.
  - (g) ML surrogates of the state map with verification (operator
    learning): admissible only as PREconditioners/warm starts for FF-A/B
    solves (a verified-in-hindsight accelerator), never as the state of
    record — the verification cost of a certified surrogate equals the
    solves it saves (stated reason for rejection as primary).
  - (h) Simulated annealing / pattern search (Nelder–Mead, MADS): MADS has
    convergence theory to Clarke stationarity — the one DFO option with a
    certificate-shaped guarantee; still gradient-starved at this dimension;
    reserve for nonsmooth pockets of the certification boundary.
- Recommendation: (a) [trust-region SQP, exact penalties for the few
  nonsmooth constraint aggregates] + (c) for global coverage + (d)/(e)
  quarantined in FF-F for sector census; (b) as the scale-up path.
- Falsifier: multistart/census discovering a basin that (a)-from-seeds
  never reaches with J gain beyond the globality gap delta (indicts the
  seeding strategy, not the optimizer class; update census).

---

FORK-37: The globality certificate (requirement (iv)).
- Question: where does a COMPUTED delta = B - J[S*] come from?
- Options (full space):
  - (a) Physics upper bound by streamtube relaxation: bound F for ANY
    admissible nozzle by exhausting each streamtube of s(xi) isentropically
    to Pa with angular-momentum constraint (u_theta_exit = Gamma_circ/r_e,
    r_e <= R_E; u_x^2 <= 2(H - h(T_e)) - u_theta^2): a per-phase quadrature
    bound B_ideal(xi); average over mu. Computable from DATA ALONE (no
    state solves); honest but loose (ignores length/envelope constraints).
  - (b) Per-phase variational optimum bound (the shared-contour price):
    B_var = int_Xi F[S*_xi; s(xi)] dmu with S*_xi the UNSHARED per-phase
    optimal contour under the same c (computable by the classical
    variational method, FF-E — Rao/Kraiko machinery extended to gamma(T)
    and rotational inflow, which the Kraiko school documents); then
    delta = B_var - J[S*] prices exactly the "one fixed nozzle for the
    whole cycle" compromise. Tighter than (a) by construction; requires
    per-phase optimal solves (cheap: 1 phase each, classical method).
  - (c) Lagrangian-dual / relaxation bounds (convexification of the reduced
    problem, SDP-flavored): no known tractable convex structure in the
    Euler-constrained shape problem at this generality — named, and
    rejected until a structure theorem appears (this is the honest state of
    the art; do not fake convexity).
  - (d) Branch-and-bound over the sector tree with per-sector bounds from
    (b): converts the discrete sector variable's globality into a finite
    certified enumeration.
  - (e) Statistical globality claims from multistart/GA coverage: not a
    certificate; report as evidence only.
  - (f) delta = 0 structural proofs: available exactly where the classical
    theory gives sufficiency (e.g., single-phase Dirac mu, shock-free
    regular optimum, monotone-contour class: the variational solution is
    THE optimum in its class) — scope delta = 0 claims to those strata and
    prove them there; elsewhere report computed delta > 0.
  - Decision criterion: certificate must be evaluable and its hypotheses
    auditable. (a) always; (b) whenever FF-E extends to the data class
    (rotational + gamma(T): documented in the variational-gasdynamics
    literature); (d) organizes; (f) where structure permits (exactly the
    brief's language).
- Recommendation: report the CHAIN delta_a >= delta_b >= 0 with
  delta_b = B_var - J[S*] as the headline certificate, (d) closing the
  sector dimension, (f) proven on its strata; (c)/(e) explicitly declined
  with reasons.
- Falsifier: any certified evaluation exceeding a claimed bound
  (B violated => the bound's derivation or the state certificate is wrong —
  automatic audit trigger); (b)-side: an S found with J > B_var means the
  per-phase "optima" S*_xi were not optimal (FF-E machinery falsified by
  its own oracle).

### GROUP J — CONSTRAINTS, ERROR BARS, MONITORS

---

FORK-38: Separation/attachment constraint g_sep.
- Question: attached flow mu-a.e. with an explicit detector — but Euler
  cannot separate on smooth walls; what is the criterion and where does it
  live?
- Options: (a) wall-pressure-ratio incipient-separation criteria from the
  nozzle literature (Summerfield p_w/Pa ~ 0.35–0.4; Kalt–Badal; Schmucker;
  Stark's criterion p_w/Pa ~ (1.88 M_w - 1)^{-0.64}): cheap, empirical,
  auditable, phase-wise evaluable on the Euler wall trace; (b) Stratford-
  type adverse-pressure-gradient criteria on the Euler wall pressure:
  physics-closer, calibration-needy for supersonic nozzles; (c) coupled
  integral boundary layer (IBL) march on the Euler wall data with
  separation = Cf -> 0: the declared viscous model layer made
  quantitative; the lens-preferred DETECTOR (it is itself a parabolic
  march — same machinery family); (d) RANS overlay: outside the declared
  model layer at this level (cost; scope pin) — named, deferred to a
  higher rung; (e) shock-induced separation flag: any fitted wall-incident
  shock beyond a strength threshold triggers (c) locally.
- Aggregation across phases: hard per-phase constraint via smooth
  aggregation (KS / p-norm over xi-quadrature nodes) for the optimizer +
  EXACT per-stratum min-check at certificate time (aggregation smoothing
  never certifies; it only steers).
- Recommendation: (c) as detector of record with (a) as its cheap bound
  and cross-check; (e) wired into the front logs; margin g_sep and its
  adjoint contribution enter the averaged KKT system (multiplier = price
  of attachment, requirement (ii) semantics).
- Falsifier: IBL detector disagreeing with the (a)-band on benchmark
  nozzle separation data (criterion recalibration event, logged).

---

FORK-39: Error-bar architecture for requirement (v).
- Question: name the terms of |J_exact - J[S*]| with carriers.
- The decomposition (each term with its measurement/bound carrier):
  (t1) |J_exact - J_rot|: zero under H-DATA + rotating-wave stability
       (FORK-1 proof); carrier = FORK-3(b) stability certificate + FF-D
       spot audit; if unstable: replaced by the (c)-bracket width.
  (t2) |J_rot - J_ensemble|: the 3D-vs-axisymmetric commutator (helix-
       angle-weighted fluctuation covariances); carrier = FF-C solves at
       the optimum (and 1-2 perturbed designs) minus the FF-A ensemble;
       reported as measured, trend-modeled in tan(alpha_h).
  (t3) per-phase model residuals: EOS-table interpolation (FORK-6),
       frozen-flow assumption (declared scope pin — absence carrier),
       viscous layer (FORK-38's IBL displacement-thickness thrust
       correction as the carrier; or declared absence).
  (t4) discretization: DWR estimate summed over quadrature nodes (FORK-26),
       cross-checked by twin-oracle diff (m9).
  (t5) phase-quadrature remainder (FORK-33).
  (t6) optimization gap: g radient-residual-to-J bound via curvature
       estimate (FORK-40) — distinct from the globality delta (FORK-37),
       both reported.
- Recommendation: publish the budget as a table with measured values and
  derived bands per certified design; the budget PARTITION is itself
  derived (next fork).
- Falsifier: any rung-crossing audit (FF-C/FF-D) revealing error mass not
  covered by t1–t6 (budget structure falsified — version and extend).

---

FORK-40: Tolerance and stopping derivation (no magic constants).
- Question: how are all the tolerances in FORKs 9–38 set?
- Options: (a) global budget partition: fix the target certificate width
  delta_tot (a USER-level input — the single legitimate exogenous number),
  partition across t1–t6 by measured marginal cost ("spend tolerance where
  it is cheapest to tighten"): a small resource-allocation LP over measured
  cost-vs-tolerance curves; (b) equal-split partition: simple, wasteful;
  (c) fixed traditional tolerances (1e-6 etc.): forbidden by the brief.
- Derived stopping: optimizer stops when the certified bound
  |J(S) - J(S_stationary)| <= ||reduced gradient||^2 / (2 |lambda_min_est|)
  (trust-region model bound with measured curvature) drops below t6's
  budget line — a DERIVED stationarity tolerance, not a gradient-norm
  folklore number.
- Recommendation: (a); every tolerance in the certificate record carries
  its derivation hash (which budget line, which measured curve).
- Falsifier: a tolerance that cannot exhibit its derivation on audit
  (certificate void by construction).

---

FORK-41: H-DATA monitor design.
- Question: how are violations of the pure-single-mode hypothesis detected?
- Options: (a) spectral concentration test on any available time-resolved
  boundary signals: power fraction in the {k*n*f} comb >= threshold
  DERIVED from sensitivity dJ/d(contamination) (measured by perturbed-
  ensemble runs), flags mode transitions/competing modes; (b) loop-closure
  test on the family itself: s(xi) must trace a single closed curve in
  state space; a topological/cluster test on the data detects two-mode
  mixtures (figure-eight / bimodal residence); (c) rotating-frame residual:
  feed the data to an FF-C solve; a large steady-state residual localized
  at Gamma_d indicates data inconsistent with any single rotating wave;
  (d) mu-consistency: mu should be the pushforward of uniform cycle time —
  test measure-vs-arc-length consistency along the loop.
- Recommendation: all four are cheap; (b)+(d) run on every data delivery,
  (a) when signals exist, (c) as part of each FF-C rung audit. On ANY
  trip: t1 of FORK-39 switches from "zero (proved)" to the bracket branch,
  and the certificate downgrades explicitly — H-DATA is monitorable, so
  the certificate must MOVE when it fails, not die silently.
- Falsifier of the monitor suite: a synthetic two-mode dataset passing all
  four monitors at contamination levels that move J beyond t1's band
  (monitor suite insufficient; extend).

---

## 3. ORDER OF BATTLE

Phase 0 — Structural anchors (load-bearing; wrong choice poisons all):
 1. FORK-1/FORK-2 (exactness bridge + surrogate definition): fixes what J
    means and what (v) must contain. Do FIRST; everything is relative to it.
 2. FORK-4/FORK-5 (solution class + admissibility): fixes what "a solution"
    means; the certification list and the adjoint calculus inherit from it.
 3. FORK-14 + FORK-16/17 (data contract: subsonic patches, start surface,
    spacelike margins): fixes per-phase well-posedness; decides whether the
    marching instrument exists at all for the given data family. Requires
    ONE data audit pass (measure u·n/a and swirl over Gamma_d x Xi) before
    any solver is built.
 4. FORK-29/FORK-30 (front-aware adjoint + DtO/OtD policy): fixes gradient
    fidelity; retrofitting front terms into a captured-adjoint code later
    is a rewrite, not a patch.
 5. FORK-37 (globality mechanism): B_var machinery (FF-E) must be planned
    early because it doubles as the Dirac-mu oracle of FORK-35.

Phase 1 — Instruments (dependent on Phase 0):
 6. FORK-8/25 scheme pair + oracle suite; FORK-6 EOS audit; FORK-18/19/20
    unit processes; FORK-10/11/12 front machinery; FORK-13 stability
    monitors; FORK-23 certificate assembly.
 7. FORK-26/27/28 (error estimation, meshes, fallback differentiability).
 8. FORK-31 verification duties (gate before ANY optimization).

Phase 2 — Optimization shell:
 9. FORK-34 representation; FORK-35 averaged KKT; FORK-36 optimizer;
    FORK-24 certification boundary; FORK-33 quadrature; FORK-38 g_sep.
10. FORK-32 curvature; FORK-21 control surfaces per sector.

Phase 3 — Certificates and ladder:
11. FORK-39/40 budgets and tolerances (iterated with measurements);
    FORK-37 bounds computed; FORK-3/41 monitors armed; FF-C/FF-D rung
    audits at candidate optima.

LOAD-BEARING (top 6): FORK-1 (rotating-frame exactness), FORK-4 (solution
class), FORK-14 (subsonic-patch/causal-separation policy), FORK-16/17
(start-surface + spacelike contract), FORK-29 (front terms in the adjoint),
FORK-37 (computable globality bound). LOCAL (safe to revise late): FORK-18,
19, 27, 32, 33's quadrature detail, 38's specific criterion choice, 40's
partition weights.

---

## 4. HARD-OBSTRUCTION REGISTER (with SOTA handles)

- O-1 Multi-D weak-solution non-uniqueness (convex integration): handle =
  certified piecewise-smooth class + monitors (FORK-4/5/23); never claim
  uniqueness outside it.
- O-2 Marginal Strouhal (no quasi-steady asymptotics): handle = co-rotating
  steadiness exactness + measured commutator (FORK-1/2/39-t2).
- O-3 Shared-contour collapse of the classical exit-characteristic optimum
  reduction: handle = averaged-adjoint KKT, Rao as Dirac-mu oracle
  (FORK-35).
- O-4 Captured-shock adjoint inconsistency (missing front-motion delta):
  handle = fitted linearized-RH adjoint / Giles–Pierce internal conditions;
  shift-differentiability as theory shelf (FORK-29/28).
- O-5 Front-topology change in (S, xi): differentiability stratification;
  handle = event-detected stratified quadrature + logged insertion events
  (FORK-11/33); residual nonsmoothness handled by trust-region/MADS pockets
  (FORK-36(h)).
- O-6 Swirl-eroded spacelike margin (M > 1 but u·n < a): handle = normal-
  velocity margin monitor + with-swirl characteristic system (FORK-7/17).
- O-7 Subsonic-patch causal-separation breach: handle = margin audit +
  choked/impedance closure or exclusion (FORK-14).
- O-8 Mach-disk pockets at overexpanded phases: handle = domain-of-influence
  control-surface decoupling; FF-B elliptic-pocket fallback for wetted-
  downstream sectors (FORK-21/15).
- O-9 Vortex-sheet (plume) instability vs steadiness claims: handle =
  Miles/convective-Mach certificates scoped by the control surface
  (FORK-13/3/21).
- O-10 No tractable convex relaxation for certified global bounds: handle =
  physics/variational bound chain (streamtube relaxation, per-phase optima)
  + sector branch-and-bound; refuse fake convexity (FORK-37(c) declined
  with reason).
- O-11 gamma(T) loss of closed-form invariants: handle = exact quadrature
  characteristic thermodynamics + EOS convexity audit (FORK-6).
- O-12 Existence (i) for shape optimization over hyperbolic states: cone-
  property compactness (Chenais) is standard, but J-continuity along
  certified sequences is NOT free with fronts; handle = front-stability
  continuous-dependence scoped claims + declared monitored failure boundary
  (FORK-34/22/13).

---

## 5. AMBIGUITIES / UNDERDETERMINED POINTS IN THE BRIEF (as read)

- A-1 Whether s(xi) includes azimuthal (swirl) velocity: "flow angle, ..."
  is elliptical. Treated as swirl-present-by-default (FORK-7) since the
  physics demands it; if the data contract is meridional-only, FORK-7(a)
  becomes legitimate with a declared absent carrier.
- A-2 The ambient model on free boundaries: quiescent ambient at Pa
  assumed; external coflow would change the vortex-sheet stability and the
  free-BC count (FORK-20/13).
- A-3 "Supersonic outflow (where achieved)": the closure when NOT achieved
  is unspecified; resolved here via the control-surface decoupling
  certificate + FF-B pocket fallback (FORK-21), but the brief leaves the
  contract open.
- A-4 Attachment set Lambda "circle(s)": one lip vs two (inner/outer
  annulus lips) changes the sector census and whether center-bodies are
  anchorable (FORK-34(f) census is versioned for this reason).
- A-5 Regularity/parametrization of xi -> s(xi) and atoms of mu: needed for
  quadrature and measurable-selection arguments; assumed piecewise-smooth
  loop with finitely many events (FORK-33 detects, does not assume).
- A-6 Whether Gamma_d's geometry can place the axis inside the flow domain
  at the interface (annular vs full-disk data): affects FORK-19's
  vortex-core certificate for swirling data.

END OF TREE — 41 forks.
