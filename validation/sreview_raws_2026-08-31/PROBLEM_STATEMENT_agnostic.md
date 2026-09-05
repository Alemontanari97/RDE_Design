# PROBLEM STATEMENT — how to optimize the nozzle of a rotating detonation engine (agnostic, self-contained)

You are given a design-optimization problem. Everything you need is in this
statement. Do not consult any repository files, project documents, prior
write-ups, logs or registries about this problem: your value lies in an
INDEPENDENT attack from this statement alone. Open-literature knowledge is
welcome and must be marked [KNOWLEDGE] with author/year where you rely on
it. Every recommendation must name its hypotheses and a FALSIFIER (a test
that could reject it); every numerical tolerance must be DERIVED, never a
magic constant.

## 0. The research question (Q0)

**How does one optimize the nozzle of a rotating detonation engine (RDE)?**

Not "how does one adapt a classical steady-nozzle design method to an RDE",
and not "how does one prove a particular method beats the classical one":
those are candidate ROADS to Q0, to be weighed against the others. The
deliverable of the program that poses Q0 is (i) a design METHODOLOGY with
certificates, (ii) ONE decisive, referee-proof number or experiment that
establishes what the methodology buys, and (iii) a publishable answer
either way (a negative result is a valid answer to Q0).

## 1. Physical setting

An RDE burns propellant in an annular combustor in which one or more
detonation waves rotate continuously at kilohertz-order frequency f (treat
f, wave count n, and every timescale as PARAMETERS, not asserted values).
The engine exhausts through ONE FIXED axisymmetric nozzle. Because the
wave rotates, the nozzle inflow is not steady: at each azimuthal station
the product-gas state (pressure, temperature, Mach number, flow angle,
composition handle, swirl) sweeps a cycle as the wave passes; the whole
inflow pattern rotates with the wave. The ratio of the gas residence time
in the nozzle to the wave period (a Strouhal-type number) is a PARAMETER
to be measured per instance, never assumed: for kilohertz waves (f ~ 1-30
kHz [KNOWLEDGE: RDE literature, order of magnitude]) and nozzles of
decimetre length (L ~ 0.05-0.3 m) with product velocities of 1.5-3 km/s,
the arithmetic f·L/u spans roughly 0.05-5 — it can be small, marginal or
large depending on wave count, engine size and nozzle length.

Gas model (scope pin, declared status: USER PIN, may be challenged only by
showing it changes the decisive answer): downstream of the combustor the
products are a FROZEN (chemically non-reacting), THERMALLY PERFECT gas
mixture — fixed composition, temperature-dependent caloric properties
h(T), cp(T), so the ratio of specific heats varies with temperature and is
NOT a constant; single phase (no condensed phase); the core state model is
compressible Euler, with viscous effects a declared model layer. Constant
ambient pressure Pa > 0 at each operating point.

Wave-structure pin (declared status: USER PIN with a monitor): the nominal
data family is a PURE PERIODIC ROTATING WAVE of a single mode (fixed wave
count n, no mode transitions inside the family). Real engines exhibit
mode hopping, counter-rotating pairs and modulation; how to DETECT
violations and what to do about them (robust layer) is part of the
problem, but the certified nominal answer is posed on the pinned family.

## 2. Candidate objectives (what "optimize" may mean — you must choose and defend)

Q0 admits several objectives; part of the problem is to say which one a
skeptical referee in propulsion would accept as THE question, and to show
how the chosen road serves it:

- (O-a) time-mean axial thrust, or specific impulse, of the UNSTEADY flow
  at a design operating point:
    J_true[S] = lim_{T→∞} (1/T) ∫_0^T F_S(t) dt,
    F_S(t) = ∫ [ρ u_x (u·n) + (p − Pa) n_x] dA
  over any enclosing axisymmetric control surface (liminf/limsup variants
  if the limit is not known to exist — then only certified brackets ship);
- (O-b) robustness of that performance over an OPERATING ENVELOPE
  (ambient pressure along a mission, throttle, wave count / mode);
- (O-c) OPERABILITY: attached flow at every instant of the cycle (a
  separation margin as a state constraint), bounded side loads, no
  feedback from the nozzle that destabilizes the combustor wave;
- (O-d) COST / manufacturability: length, mass and heat-load proxies,
  tolerance to as-built geometric errors.

The engine designer's first-order practice today is to design the nozzle
for a representative mean inflow state with a classical steady method and
to check the unsteady behaviour afterwards. Whether, when and by how much
any other road beats that practice — on which objective, which nozzle
configuration and which data richness — is exactly what Q0 asks.

## 3. Given data (data classes, by richness — the road must say which class it needs)

- Geometry: an envelope cylinder E (length L_E, radius R_E) downstream of
  the combustor exit; the attachment set Λ (the chamber lip circle(s))
  where solid surfaces may be anchored.
- An interface surface Γ_d, fixed and axisymmetric, downstream of all heat
  release, on which the inflow is specified. Admissibility premises on the
  data are to be AUDITED, never assumed silently: causal separation (the
  design does not influence the data through the interface), well-posed
  boundary data (complete state only where the flow through the interface
  is supersonic; where it is subsonic, an explicit closure must be
  declared), measurability of the family. The audit design is part of the
  problem.
- Data classes:
  - class A — SPECS ONLY: propellant, equivalence ratio, mean chamber
    pressure, annulus geometry, ambient pressure. Everything else (the
    time-resolved states over the period, their probability weights) must
    be GENERATED from the specs by a model chain of the road's choosing —
    a fully predictive tool with no measured input beyond the specs;
  - class B — A + a WAVE-STRUCTURE MODEL producing time-resolved profiles
    across the interface (Mach number, flow angle, entropy/composition
    handle, swirl as functions of radius and cycle time);
  - class C — A/B + PARTIAL EXPERIMENT (pressure traces, thrust, wave
    frequency and count) for calibration of the model chain and of the
    time weights;
  - class D — + a mission profile of ambient pressure;
  - class E — + a throttle envelope (several operating points with
    weights);
  - class F — + DECLARED UNCERTAINTY on waveform, pressure ratio and mode
    count (distributional or set-valued);
  - class G — + a CHAMBER-COUPLING request: the nozzle back-reacts on the
    combustor (pressure ratio, fill, wave speed) through a reduced
    response map.
- A legacy classical steady-nozzle design code (Fortran, characteristic-
  based, contour optimization for a single inflow state) is available
  READ-ONLY as an independent cross-check oracle; it is not the method.

## 4. Design variable, admissible set, constraints

The design variable is the SOLID SET S ⊂ E (a compact axisymmetric solid);
the flow domain is Ω(S) = E \ S. Nozzle configurations — bell, plug /
aerospike, shrouded plug, expansion-deflection — may be treated as an
INPUT (a chosen configuration) or as an OUTPUT (topology sectors of S
selected by the optimization): state which, and price what the choice
loses. Admissible set:
  A(c) = { S ⊂ E compact solid : a compactness / regularity condition of
           the road's choosing (existence of a maximizer must be addressed);
           attachment on Λ; g_i(S) ≤ c_i for the constraint vector c }.
Constraint vector c: overall length bound L; exit radius / envelope bound
and area ratio (fixed or bounded); for plug-type solids a truncation
fraction and a base region whose pressure needs a closure model; curvature
and slope bounds; symmetry class; as-built tolerance class (the certified
design must remain admissible and near-optimal under manufacturing
perturbations of a declared size); heat-load and mass limits enter through
geometric proxies at this modelling level. Per-instant STATE CONSTRAINT:
certified designs keep the flow ATTACHED at every instant of the cycle (a
separation margin g_sep ≤ 0 with an explicit detection criterion); designs
that separate leave the certified class. How to parametrize S for
computation (function class, discretization, regularity) is YOUR choice to
derive and defend; the regularity class of the wetted contour must be
stated (e.g. continuously differentiable with Lipschitz slope).

## 5. State model

For the flow evaluation: the compressible Euler equations (unsteady in
general; steady in whatever reduced frame the road declares) in Ω(S) with
the interface data on Γ_d, slip on the wetted solid, supersonic outflow
where achieved, ambient pressure on free portions of the control boundary;
the gas of §1. Which solution class to work in (smooth / piecewise-smooth
with tracked discontinuities / weak / statistical), how to certify
membership a posteriori, and what to do about the non-uniqueness of
multidimensional weak solutions are YOUR calls. Embedded discontinuities
(shocks, contact/slip surfaces carrying the stratification of RDE exhaust,
the free plume boundary of plug-type solids) must be addressed
explicitly, including how derivatives with respect to the design pass
through them.

## 6. The requirement: what a referee can check (consumer-level requirements only)

Whatever the road, the answer must deliver a design S* and a decisive
number with the following properties, each stated so that a skeptical
referee can CHECK it:
 (R-i)   OPTIMALITY CLASS DECLARED WITH EVIDENCE: what kind of optimum S*
         is (local / global / within a computed gap of the best possible /
         best-effort), with the evidence that supports the class and the
         honest statement of what is out of reach (nonconvex shape
         optimization under PDE constraints has no unconditional global
         guarantee for anyone);
 (R-ii)  VERIFIABLE OPTIMALITY CONDITIONS: whatever first- and second-order
         conditions the road uses, reported with the multipliers of active
         constraints (marginal values), never assumed;
 (R-iii) ERROR BARS A REFEREE CAN CHECK: |J_true − J[S*]| bounded by named,
         evaluable terms (unsteadiness / reduction error; model residuals;
         data uncertainty; discretization error), each with an explicit
         computable term or a declared absence — and an UNCERTAINTY BUDGET
         showing whether the decisive difference of §9 is resolvable above
         the sum of those terms;
 (R-iv)  VALIDITY OF EVERY FLOW SOLUTION USED: for each value, derivative
         or constraint the road consumes, an a-posteriori check that the
         computed flow is a legitimate solution of the declared model
         (solution class, discontinuity treatment, attachment), with a
         test able to REJECT an invalid one;
 (R-v)   REJECTABLE TESTS for every derivative, estimator and data audit
         (a test that cannot fail proves nothing);
 (R-vi)  REPRODUCIBILITY ACROSS VERSIONS AND ENVIRONMENTS: a result is a
         property of (code version, checking procedure, execution
         environment); the road must say how results stay valid when any
         of the three changes, what margin makes a result quotable, and how
         a non-reproducing result is owned (never silently re-stamped);
 (R-vii) FULL PROVENANCE: every quoted number carries its hypotheses,
         bands, checks and data provenance.

Rigor classes to be declared for every claim: THEOREM (full proof) /
THEOREM under a declared model closure / SCHEMA (correct structure, rigor
gap named) / CONJECTURE (precise + falsifier) / PRACTICE (instrumented, no
theorem).

## 7. Generality pins (declared; a road that violates one must say what it loses)

- variable ratio of specific heats: every step must hold for the
  thermally-perfect mixture, and any constant-gamma shortcut must be
  named as an oracle or initializer, never a solver step;
- NON-HARDCODED procedures: no case-dependent node counts, bases,
  iteration caps or tolerances; every such quantity derived from the
  problem data or from a measured indicator;
- configurations bell / plug / shrouded plug / expansion-deflection are
  all in the admissible set and are outputs; the road must handle the
  truncated plug with base region and free plume boundary, not only the
  full-flowing bell;
- data classes A-G all admissible; the road states which class its
  decisive answer needs and what changes with richer data;
- full three-dimensional (azimuthally resolved) treatment is the declared
  HORIZON: the road must state what its reduced representation loses
  relative to the rotating three-dimensional field, and how that loss
  would be MEASURED, not only estimated;
- honesty pins: no number without a committed, re-runnable script and a
  rejector; claims of novelty bounded by a stated literature query.

## 8. Budget and resources (constraints on the road, not on the science)

- Compute: a single workstation-class machine; Python scientific stack
  with PINNED versions (no installs; an environment change is a declared
  decision); no GPU or HPC assumed for the decisive answer (an HPC-class
  road must say so and price it); the read-only legacy Fortran oracle.
- Time: about 7-10 working sessions in total to the decisive number, each
  session with at most ~3 hours of wall-clock for decisive runs; a road
  whose decisive answer needs more must say so and price the extension.
- Experimental access: none guaranteed; the reference accuracy class for
  ANY claim about thrust or specific impulse is the thrust-stand class
  (0.5-1% of thrust) — a computed difference smaller than that band cannot
  be claimed as an advantage; a road must therefore say what accuracy its
  decisive number can reach and how the bands are derived.
- People: one researcher plus automated assistants; the method must be
  executable and re-runnable by one person.

## 9. What a referee will ask (the decisive answer)

The road must name, before building, ONE decisive computed or measured
result — with control, bands and a KILL criterion — that would convince a
skeptical propulsion referee that the road is the right way to optimize an
RDE nozzle: which configuration and data class, which comparator and why it
is the STRONGEST competitor a competent designer would field, which
metric, which accuracy class, which pre-registered outcomes (including the
negative one), what each outcome implies for the program, and what the
number is anchored to outside the road's own machinery. "Which measurement
would make you change road" is a mandatory field of every road
recommendation.
