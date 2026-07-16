# From per-streamline thrust to a shape functional: the cycle-averaged variational nozzle problem for RDEs

> SUPERSESSION NOTICE (2026-07-16). This note is kept as historical
> record. Definitions, theorem statements and novelty claims are
> superseded by the D1-D4 deliverables:
> `docs/rde_nozzle_problem_book.md` (D1), `docs/rde_nozzle_literature_map.md`
> (D2), `docs/rde_nozzle_theorem_ledger.md` (D3),
> `docs/rde_nozzle_claims_verdict.md` (D4). Known corrections vs this
> note (see D4 §1): T1 is a definition+conjecture, not a theorem; the
> averaged transversality (**) must be the weighted form (**'); "Rao
> verbatim in 3-D" is an overclaim; §5.1b measured numbers were
> unverifiable in-repo until 2026-07-16 — now re-derived and CORRECTED
> INLINE below (A0.3: examples/gamma_cycle_probe.py; eps* shift is
> -0.56%, not -1.9%); "Mo, Huang" was a bibliographic conflation,
> corrected inline below; T0 strengthens to instantaneous constancy.

Status: RESEARCH NOTE (theory + program). Not V&V of shipped code; the
theorems below are stated with hypotheses and proof sketches at the rigor
level of `validation/bell_optimality_proof.md`, and every claim that can be
made executable is flagged as such.

Companion assets in this workspace:
- Stechmann-Heister-Harroun (S-H) model, as implemented and proved:
  `src/thrust/st_core.py`, `src/thrust/stechmann_nozzle.py`,
  `validation/bell_optimality_proof.md` (Lemma dF/dA_e = Pe - Pa;
  Theorem 1 bell NPR(eps*) = <Pc>_t/Pa; Theorem 2 spike knee
  NPR(eps*) = Pmax/Pa; Theorem 3 vacuum).
- GENO (Rao variational machinery): thrust functional over a free control
  surface with mass (lambda_2) + length (lambda_3) multipliers, optimal
  surface = characteristic, first integral f2 = V cos(theta -/+ alpha)/cos(alpha)
  = const, corner/transversality condition Rao Eq. [14]
  (`GENO/src/lib/Rao_m.f90`: boundaryfunction_solve :30-56, marching
  :59-121, mass termination :417, corner conditions `Types_m.f90:379-391`
  and plug corner `Rao_m.f90:762-764`); non-uniform steady-inflow hooks:
  `read_ivl_from_file` (`IO_m.f90:620-776`) and the annular inlet with
  specified (Mi, theta_i) (`InitialValues_m.f90:146-226`).

------------------------------------------------------------------------------
## 0. The question, and the short answer

S-H optimizes ONE scalar (the area ratio eps) by averaging the quasi-steady
thrust of each cycle instant - each "streamtube" of the blowdown - over the
detonation cycle. Rao/GENO optimizes the FULL contour, but for one steady
uniform inflow. The research question:

> If each streamline (cycle phase) carries its own variational thrust
> problem, can a TOTAL functional be defined as the integral of the
> per-streamline functionals over the cycle, and can Euler-Lagrange /
> Rao-type optimality conditions be derived for the whole contour shape?

Short answer, in five statements proved/argued below:

1. YES, and on a footing stronger than an ad-hoc ensemble average: for a
   single steadily rotating wave the cycle-averaged thrust IS the exact
   steady thrust of one steady flow in the wave-fixed frame (Theorem T0).
   The averaged functional is therefore a genuine steady thrust functional,
   and Rao's control-surface framework applies to it verbatim (in 3-D).
2. In the S-H factorized limit the total functional is literally the double
   integral - over cycle phases, and per phase over Rao's control surface -
   of per-streamline thrust integrands (Theorem T1), and the full
   stationarity system exists: per-phase Rao conditions with a
   FUNCTION-VALUED mass multiplier lambda_2(xi), plus one new object, the
   PHASE-AVERAGED wall condition and phase-averaged transversality
   (corner) condition (Theorem T2).
3. There is a sharp structural dichotomy. For any FIXED-WALL, full-flowing
   nozzle the averaged problem COLLAPSES exactly to the classical Rao
   problem at the time-mean chamber pressure (Theorem T3, a no-go /
   null-result theorem): within the strict S-H idealization the optimal RDE
   bell is the Rao bell designed at <Pc>_t, and nothing more can be
   extracted. The repo's Theorem 1 is the 1-DOF shadow of this.
4. For FREE-BOUNDARY nozzles (plug/aerospike) the collapse NEVER happens.
   The ideal untruncated plug solves the averaged problem by simultaneous
   optimizability - the per-phase optimal sets are nested, and the optimum
   is the Rao plug designed at the PEAK pressure P_CJ (Theorem T4); the
   repo's knee theorem is its 1-DOF shadow. The first genuinely open,
   genuinely cycle-averaged shape problem is the TRUNCATED plug (and the
   shrouded plug), where no single-phase design is optimal.
5. Therefore the real research content lives exactly in the channels that
   break the collapse hypotheses (Section 6: N1-N6) - separation, free
   boundaries, phase-dependent inlet nonuniformity, thermochemistry,
   unsteadiness O(St), and 3-D swirl - and each channel has a concrete
   tool already half-built in this workspace.

To our knowledge (targeted search, July 2026: RDE-nozzle MOC design with
nonuniform inflow; aerospike-RDE optimization; multipoint/adjoint nozzle
design; trajectory-averaged dual-bell work) the cycle-averaged VARIATIONAL
formulation - T0-T4 and the averaged Rao conditions - has not been
published. Existing RDE nozzle work designs on time-averaged flow
quantities (Li-Xu-Huang, J. Prop. Power 38(5):849-865 (2022): MOC on the
time-averaged state — NOT "Mo, Huang", which conflated it with the
scramjet nonuniform-inflow MOC of Mo et al., Acta Astronautica 108:92
(2015); correction of record, D2 §b1) or optimizes parametrically with
CFD; none of it states the shape-functional problem, and none of it
contains T3, which incidentally EXPLAINS why "design on the time-averaged
flow" heuristics work as well as they do (they are exact precisely under
the S-H hypotheses).

------------------------------------------------------------------------------
## 1. Notation and the two pillars

Cycle phase xi = t/tc in [0,1]; blowdown Pc(xi) = P_CJ PR^(-xi) (Eqs. 13-14
of S-H), stagnation temperature isentropic (Eq. 15), gamma and M frozen
(assumption 2), choked throat mdot = Pc A_t / c* (Eq. 6). Per-cycle
specific impulse (Eq. 4):

    Isp = Int[mdot CF c* dt] / (g0 Int[mdot dt]).

Shape: Sigma denotes the nozzle contour (bell wall, or plug + cowl lip, or
shroud + plug), in an admissible class A (Lipschitz generator, fixed
attachment at the throat/lip, optional length/area constraints).

Per-phase problem: steady axisymmetric Euler flow U_xi in the domain
bounded by Sigma, inflow state s(xi) (sonic line at stagnation
(P0(xi), T0(xi)) in the S-H limit; more generally a supersonic IVL with
(M_in(xi), theta_in(xi)) profiles), slip on Sigma. Per-phase thrust
F[Sigma; s(xi)]: wall form

    F = F_throat(xi) + Int_Sigma (p_xi - Pa) n_x dA,

or equivalently Rao's control-surface form on any permeable surface,
which is where the per-streamline structure is explicit:

    F = Int_CS [ (p - Pa) + rho V^2 sin(phi-theta) cos(theta)/sin(phi) ] 2 pi y^delta dy.

Objective functional (definition; legitimacy in T0/T1):

    J[Sigma] = Int_0^1 F[Sigma; s(xi)] dxi.

Weighting lemma (why the weight is unity). Maximizing cycle Isp at matched
feed is equivalent to maximizing J: the denominator g0 Int[mdot dt] is
fixed by the common choked throat and the Sec.-III mass matching,
independent of the divergent geometry; and the numerator Int[mdot CF c* dt]
= Int[F dt] identically (thrust is thrust). No mass-weighting ambiguity
survives at the shape level - the same collapse that
`bell_optimality_proof.md` obtains from mdot c* = Pc A_t holds here by
construction.

------------------------------------------------------------------------------
## 2. Theorem T0 (wave-frame exactness): the averaged functional is a
##    single steady thrust functional

Hypotheses: one detonation wave (or an N-fold symmetric wave set) rotating
at constant angular speed Omega = 2 pi / tc about the engine axis x; the
flow is exactly periodic, q(x, r, theta, t) = q~(x, r, theta - Omega t);
control surface S fixed in the lab frame, axisymmetric.

Claim: the time-averaged axial thrust over one period equals the steady
axial-momentum-flux integral of the steady field q~ evaluated in the
rotating frame:

    <F>_t = Int_S [ rho~ u~_x (u~ . n) + (p~ - Pa) n_x ] dA,

with NO Coriolis or centrifugal contribution.

Proof sketch. (i) Pattern ergodicity: for a rotating pattern, the time
average at fixed theta equals the azimuthal average at fixed t; both equal
the full surface integral of q~. (ii) Frame forces: with Omega along x,
the Coriolis acceleration -2 Omega e_x x u has zero axial component and the
centrifugal term is radial; the axial momentum balance in the rotating
frame is therefore identical to the inertial one, and the steady
control-volume balance of q~ gives exactly the lab-frame time-averaged
thrust. QED (sketch).

Consequences.
- J is not a fiction built from fictitious quasi-steady problems: it IS the
  thrust functional of one steady (swirling, azimuthally nonuniform) flow.
  Rao's variational framework - whose only structural requirements are
  steadiness and the conservation laws on a control surface - applies to
  the RDE nozzle EXACTLY, as a 3-D problem in the wave frame. The cycle
  integral Int dxi is the azimuthal integral Int dtheta'/2pi: the phases
  ARE the azimuthal coordinate, and "integral of per-streamline
  functionals" becomes literally ONE surface integral over one 3-D control
  surface crossed by helical streamlines.
- Failure modes, declared: counter-rotating wave pairs, longitudinally
  pulsed or mode-hopping operation break the steady-pattern hypothesis;
  then only the quasi-steady route (T1) or full URANS remains.

------------------------------------------------------------------------------
## 3. Theorem T1 (factorization): when J is an integral of independent
##    per-streamline functionals

Hypotheses (the S-H limit, made explicit):
D1 (quasi-steady). St = tau_n / tc -> 0, where tau_n is the nozzle
   residence time. Each phase xi then supports a steady flow at frozen
   inflow s(xi).
D2 (meridional decoupling). Azimuthal fluxes between neighboring sectors
   are negligible downstream of the inflow plane (long azimuthal
   wavelength / weak swirl): each sector expands in its own meridional
   plane against the SHARED wall Sigma.
D3 (regularity). Each per-phase flow is MOC-regular (shock-free,
   supersonic exit), so F[Sigma; s(xi)] is well-defined and smooth in
   Sigma away from topology switches.

Claim: under D1-D3,

    J[Sigma] = Int_0^1 dxi F[Sigma; s(xi)],

with each F given by Rao's per-phase control-surface streamline integral;
the exit state of streamtube xi depends only on its own inflow state and
on Sigma (Lagrangian decoupling), and the double integral structure
(phases x streamlines) is exact.

Remarks.
- D1 honestly quantified: for representative rocket RDEs f ~ 3-30 kHz
  (tc ~ 30-300 us) and tau_n ~ 20-150 us, so St = O(0.1-1): MARGINAL.
  This is the single largest physical caveat of the whole S-H edifice,
  and it is why T0 matters: T0 needs no quasi-steadiness at all. The
  first-order-in-St correction is a well-posed research object (Section 6,
  N5), computable with nozzle transfer-function methods (Marble-Candel
  type) applied to the blowdown's entropy/pressure wave content.
- D2 is what "per-streamline" secretly assumes. Violation (shock
  diffraction between sectors, azimuthal secondary expansion) does not
  destroy J - it destroys its FACTORIZATION; one then retreats to T0's
  3-D functional.

------------------------------------------------------------------------------
## 4. Theorem T2 (master stationarity system: the phase-averaged Rao
##    problem)

Setting: maximize J[Sigma] = Int dxi F(Sigma, U_xi) subject to
(i) per-phase steady Euler constraints E(U_xi, Sigma) = 0 - one adjoint
field psi_xi per phase; (ii) per-phase mass-flow constraints (each phase's
mdot(xi) is fixed by the choked inlet) - a function-valued multiplier
lambda_2(xi), the direct generalization of Rao's scalar lambda_2;
(iii) SHARED geometric constraints (length L, exit radius, lip position) -
scalar multipliers (lambda_L, ...), shared across phases because the wall
is shared.

Claim (structure of the first variation). Because the per-phase problems
are mutually independent GIVEN Sigma (T1), the variation splits:

  (a) Stationarity in U_xi, for a.e. xi separately: the per-phase adjoint
      Euler system; in the MOC-regular case this reduces to Rao's
      conditions ON THAT PHASE'S terminal characteristic: the optimal
      per-phase control surface is a characteristic, and the first
      integral f2 = V cos(theta -/+ alpha)/cos(alpha) = -lambda_2(xi)
      holds phase-by-phase with its own multiplier.
  (b) Stationarity in Sigma: the PHASE-AVERAGED wall condition

          Int_0^1 dxi G_xi(x) + lambda_L g_L(x) = 0   for a.e. x on Sigma,   (*)

      where G_xi is the phase-xi Hadamard shape gradient (computable by
      per-phase adjoint or, in the Rao frame, by that phase's
      characteristic relations). This equation is the genuinely NEW
      object: no single phase satisfies its own Rao wall condition;
      their weighted sum vanishes instead.
  (c) Stationarity in the shared endpoint (lip/exit corner): the
      PHASE-AVERAGED transversality condition. With Rao's Eq. [14]
      residual R(xi) = (p_E(xi) - Pa) - (1/2) rho_E V_E^2 sin(2 theta_E) tan(alpha_E)
      (sign conventions as in GENO `Types_m.f90:379-391`),

          Int_0^1 R(xi) dxi = 0.                                            (**)

Reduction check (executable): in quasi-1D, where the only shape DOF is the
exit area, (*)-(**) degenerate to <p_e(xi)>_t = Pa, i.e.
NPR(eps*) = <Pc>_t/Pa - EXACTLY Theorem 1 of
`validation/bell_optimality_proof.md`; and with the ideal-plug closure the
one-sided version of (*) gives the knee, Theorem 2. Both shipped identities
are the rank-1 projections of (*)-(**).

Non-smoothness, handled: at phases where the flow topology switches (the
spike's exit-area-limited/adapted switch at tsw, separation onset,
characteristic-corner collisions) F(Sigma, .) is only Lipschitz. The
switch set is measure-zero in xi and F is CONTINUOUS across it, so the
xi-integral is differentiable and Leibniz applies (same structure as the
np.where switch inside `cycle_isp`); where a genuinely persistent kink
appears, (*) holds in the Clarke-subdifferential sense. Existence of a
maximizer over A follows in restricted (finite-dimensional spline /
uniform-cone Lipschitz) contour classes by compactness + continuity of
Sigma -> U_xi for MOC-regular flows; global existence in the unrestricted
class is deliberately NOT claimed.

------------------------------------------------------------------------------
## 5. The dichotomy: collapse for fixed walls, genuine averaging for free
##    boundaries

### 5.1 Theorem T3 (collapse / no-go for the fixed-wall bell)

Hypotheses (ALL load-bearing; each one that fails opens a channel in Sec. 6):
H-T3.1 gamma frozen AND common to all phases (calorically perfect gas with
       one gamma - exactly S-H assumption 2). NOT satisfied by a
       thermally-perfect gamma(T) gas model: see 5.1b.
H-T3.2 fixed wall, FULL-FLOWING (no separation - S-H hypothesis H4),
       supersonic exit at every phase, so the ambient state cannot
       propagate upstream and the interior problem is ambient-blind.
H-T3.3 choked inlet whose nondimensional state distribution (sonic-line
       shape, or more generally the inflow Mach/angle profiles) is
       phase-independent; phases differ only through (P0(xi), T0(xi)).
H-T3.4 per-phase flows MOC-regular, unique.

Claim: pointwise on shape space,

    J[Sigma] = F[Sigma; <Pc>_t]        (not merely equal argmax),

so the cycle-optimal fixed-wall contour is exactly the classical Rao
contour designed at the time-mean chamber pressure, under identical
geometric constraints. Nothing about the cycle survives except its mean.

PROOF (full, three lemmas + assembly).

Lemma A (pressure-scaling similarity; holds even for thermally-perfect
gamma(T)). Fix Sigma, fix T0. Let (u, T, p, rho) solve steady Euler with
inflow stagnation (P0, T0). Then for kappa > 0, (u, T, kappa p, kappa rho)
solves the same problem with inflow (kappa P0, T0).
Proof: continuity and energy are homogeneous in (rho) and untouched by
p-scaling at fixed (u, T); momentum contains p only through grad(p)/rho,
invariant under joint scaling; the thermal EOS rho = p/(R T) is preserved;
entropy s(T) - R ln p shifts by the constant -R ln kappa, so isentropes map
to isentropes; slip BC and the sonic-line BC (a Mach condition) are
p-scale-free; by H-T3.2 no downstream ambient datum enters. Uniqueness
(H-T3.4) makes this THE solution. Hence M(x), theta(x), T(x) are
phase-independent and p_xi(x) = Pc(xi) PI(x; Sigma) for one fixed field PI.

Lemma B (T0-similarity; REQUIRES frozen gamma, this is where gamma(T)
dies). For a calorically perfect gas, at fixed P0, changing T0 -> T0'
rescales u by sqrt(T0'/T0) and leaves M(x), theta(x), p(x), and T(x)/T0
invariant (the isentrope p = P0 (1 + (g-1)/2 M^2)^(-g/(g-1)) ties p to M
alone). Consequently the thrust - wall-pressure integral plus throat
momentum flux (rho u^2 + p) A_t = P0 A_t (g M_t^2 + 1)(...) - contains T0
nowhere: CF is T0-blind, the classical fact, here per phase.
For a thermally-perfect gas cp(T) is not a power law, no similarity
variable exists in T, and the gamma-path along the expansion depends on
T0(xi): Lemma B FAILS. (See 5.1b.)

Lemma C (affinity). By Lemmas A-B, per phase:

    F[Sigma; s(xi)] = a[Sigma] Pc(xi) - Pa b[Sigma],
    a[Sigma] = Int_wall PI n_x dA + throat-momentum coefficient,
    b[Sigma] = A_e[Sigma] - A_t   (projected wall area),

with a, b the SAME functionals for every phase (they depend only on the
phase-independent PI field and the geometry).

Assembly. J[Sigma] = Int dxi [a Pc(xi) - Pa b] = a[Sigma] <Pc>_t
- Pa b[Sigma] = F[Sigma; <Pc>_t]. The two objectives are the same
function on the same feasible set (shared constraints, shared
multipliers), hence identical stationary points, identical optima. QED.

Two remarks that dissolve the apparent paradoxes:

(R1) "Each phase re-run through Rao gives a DIFFERENT optimal contour -
how can the average collapse?" Both statements are true simultaneously.
The per-phase optimum argmax_Sigma {a[Sigma] Pc - Pa b[Sigma]} moves with
Pc, because Pa/Pc reweights a against b (this is also exactly where Pc
enters Rao's machinery: ONLY through the corner/transversality condition
and the exit multiplier balance - the interior characteristic equations
are Pc-blind by Lemma A). So the family of per-phase Rao contours is
genuinely a nontrivial family - AND its average objective is again a
member of the same affine family, with coefficient <Pc>. The collapse is
a statement about the average of an affine family, not about the
coincidence of its per-phase maximizers. The high nonlinearity of Rao's
PROCEDURE lives entirely in Sigma -> (a, b); it is untouched and
irrelevant to the argument.

(R2) Consistency check inside Rao's own formalism: the phase-averaged
corner condition (**) collapses too. With Lemma A, p_E(xi) = Pc(xi) Pi_E
and rho_E V_E^2 = gamma p_E M_E^2 = Pc(xi) gamma Pi_E M_E^2, so

    <R(xi)> = Pi_E <Pc> - Pa - (1/2) gamma Pi_E M_E^2 sin(2 theta_E)
              tan(alpha_E) <Pc> = R evaluated at Pc = <Pc>.

The averaged transversality condition IS the single-phase corner
condition at the mean pressure - the master system (*)-(**) degenerates
coherently, as it must.

### 5.1b Sharpness of T3: the variable-gamma correction (measured)

Under a per-phase gas model - each point of the detonation wave feeding
the nozzle with its own (Pc(xi), T0(xi)) and its own isentropic exponent
gamma(xi), or a thermally-perfect gamma(T) expansion - Lemma B fails and
the correct statement is

    F[Sigma; s(xi)] = a[Sigma; gamma-path(xi)] Pc(xi) - Pa b[Sigma],
    J[Sigma] = < a[Sigma; .] Pc >_t - Pa b[Sigma]  =/=  F[Sigma; <Pc>_t].

The collapse is FALSE in principle. To first order in the gamma
excursion, a is linear in gamma and

    J ~ a[Sigma; gamma_eff] <Pc> - Pa b[Sigma],
    gamma_eff = <Pc gamma>_t / <Pc>_t      (PRESSURE-WEIGHTED mean gamma),

so the leading correction replaces "design at <Pc> with gamma_CJ" by
"design at <Pc> with the Pc-weighted gamma". Because the blowdown's
pressure weighting is concentrated at the early, high-Pc phases,
gamma_eff sits very close to gamma(CJ) - which retroactively identifies
S-H assumption 2 (freeze gamma AT THE CJ STATE, not at some cycle-mean
state) as the correct first-order closure of the averaged problem, not an
arbitrary convenience.

Measured magnitude (CORRECTED INLINE 2026-07-16, A0.3: the original
scratch probe was never committed; the numbers below are the in-repo
re-derivation of record — `examples/gamma_cycle_probe.py`,
`tests/test_gamma_probe.py`, `data/gamma_cycle_probe.json` — CH4/O2
phi = 1.64, Pcp = 20 atm, PR = 49.2, blessed Table-1 state):
- equilibrium isentropic exponent along the blowdown stagnation states:
  gamma_s = 1.1537 (xi=0, T0=3727 K) -> 1.2093 (xi=1, T0=2228 K), with
  a single shallow interior minimum at xi ~ 0.1 (depth 4e-4);
  thermally-perfect frozen-composition gamma_tp = 1.2223 -> 1.2286
  (the old "1.244" endpoint was wrong);
- per-phase CF deviation from the frozen-gamma closure at eps*_fr:
  < 0.3% over the thrust-dominant early half-cycle, ~1.3% at xi = 0.75,
  formally unbounded only across the late-cycle zero-crossing of the
  overexpanded frozen CF (Pc-weighted mean 0.36%);
- induced shift of the quasi-1D bell optimum: eps* moves by -0.56%
  (3.980 -> 3.958). The old "-1.9%" is STRUCK: the pressure-weighted
  gamma_eff = 1.1577 reproduces the true shift (-0.57%), while the
  UNWEIGHTED mean gamma gives -2.39% — the wrong-averaging class the
  stale figure most plausibly came from, now rejected by test;
- the Isp penalty of designing with frozen gamma under the
  variable-gamma truth: -0.00028% (second order, envelope theorem:
  penalty 2.8e-6 <= shift^2 = 3.1e-5; the old "-0.001%" overstated it).

Verdict on this channel (N4): real but SMALL - the collapse is falsified
in principle and robust in practice, because (i) the Pc-weighting
suppresses the late-cycle phases where gamma drifts most, and (ii) any
optimum-shift penalty is second order in the shift. The first-order
breakers of T3 remain N1 (separation: a kink, not a perturbation) and
N3 (phase-dependent inlet Mach/angle profiles, which enter a[Sigma; .]
at first order with no small parameter). Caveat: the numbers above are
quasi-1D (eps-level); the contour-level confirmation with the gamma(T)
MOC backend is exactly Phase C item (iv).

Consequences - this theorem cuts BOTH ways:
- Corollary 1: repo Theorem 1 (NPR(eps*) = <Pc>_t/Pa), now promoted from
  the eps-line to ALL of shape space.
- Corollary 2 (duality with altitude averaging): Pa also enters F
  linearly, so trajectory-averaged fixed-bell design collapses to the
  trajectory-mean Pa the same way - and the dual-bell literature exists
  precisely because SEPARATION breaks that linearity. The RDE cycle
  average and the classical altitude average are the same mathematics
  with the measure on Pc instead of Pa.
- Corollary 3 (null-result trap, and a free verification oracle): a naive
  "ensemble MOC shape optimization" with frozen gamma and no separation
  model MUST return the Rao-at-<Pc> contour to numerical tolerance, with
  Delta-Isp exactly zero vs. the classical design. Published as a
  computation, that would be an empty result; used as an EXECUTABLE TEST,
  it is the perfect end-to-end oracle for any ensemble-optimization
  machinery built in Phase C below (repo culture: the test can REJECT a
  broken implementation, not merely confirm a working one).

### 5.2 Theorem T4 (plug: simultaneous optimizability; the knee at shape
###     level)

Hypotheses: ideal-adaptation closure for the free boundary (the S-H
Eqs. 10-12 idealization lifted to contours): on the portion of the plug
contour downstream of phase xi's full-expansion point, the wall pressure
is clamped to Pa (zero incremental thrust); upstream of it the field obeys
the same scaling as in T3.

Claim: per phase, F[Sigma_l; s(xi)] is nondecreasing in the contour
extension l and exactly constant for l >= l(xi), where l(xi) - the
phase-xi design length - is increasing in Pc(xi). The per-phase argmax
sets are the nested half-lines [l(xi), infinity); their intersection is
attained at the PEAK phase:

    max_Sigma Int dxi F = Int dxi max_Sigma F,

and the maximizer is the Rao plug designed at NPR = P_CJ/Pa (capped by
the annulus geometric limit eps_max where it binds). No Pareto conflict
exists: the cycle problem is solved by ONE single-phase design - the peak
one - which is precisely why S-H's eps-level analysis found
NPR(eps*) = Pmax/Pa (repo Theorem 2), and why the aerospike is the
natural RDE nozzle: its free boundary absorbs the entire cycle excursion
at zero functional cost.

Sharpness - where T4 dies and the genuinely averaged problem is born:
impose a length/weight constraint L < l(xi_peak), or a base-pressure
model at a truncation plane, or real (non-ideal) adaptation. The nested
structure breaks, max Int < Int max strictly, and the optimum satisfies
the averaged conditions (*)-(**) with the PLUG corner condition
(GENO `Rao_m.f90:762-764`, base pressure p_b) replaced by its phase
average. THE TRUNCATED CYCLE-AVERAGED PLUG IS THE FIRST CONCRETE, OPEN,
GENUINELY VARIATIONAL RDE NOZZLE PROBLEM - it does not reduce to any
single-phase design, at any pressure.

------------------------------------------------------------------------------
## 6. Where the novelty actually lives: the six collapse-breaking channels

T3 is a conservation law for research effort: any genuine gain over
"Rao at <Pc> / plug at peak" must enter through a violated hypothesis.
Taxonomy, with mechanism, expected sign, and the tool at hand:

N1. SEPARATION (fixed wall). Overexpanded phases separate instead of
    running full: F_xi becomes piecewise (capped loss) - nonlinear in Pc.
    The average no longer collapses; because separation truncates the
    LOSS side, the optimal contour shifts to larger expansion than
    Rao-at-<Pc>, and contours with deliberate separation control
    (inflection / dual-bell-like) enter the stationary set. Conjecture:
    the optimal separated RDE bell is a "temporal dual-bell" - the cycle
    plays the role altitude plays for the classical dual-bell
    (Corollary 2 duality). Tool: per-phase MOC/quasi-1D + a
    Summerfield/Schmucker criterion; the repo already prints the
    overexpansion collapse (Fig. 8 replica) that sizes the stake.
N2. FREE BOUNDARIES: plug truncation + base pressure (T4-sharpness),
    slipstream/shroud interaction. Tool: GENO plug machinery (types 5/8)
    + the averaged corner condition (Section 7, C-step iii).
N3. PHASE-DEPENDENT INLET NONUNIFORMITY. The real RDE exit is not a
    clean sonic line at varying P0: per phase it carries (M_in(xi),
    theta_in(xi)) - supersonic patches, the oblique-shock sector, swirl.
    This breaks the phase-independent PI(x) invariance directly (the
    strongest structural violation after N1). Tool, already built:
    GENO's `read_ivl_from_file` (ORION .tec IVL import) and the annular
    inlet with prescribed (Mi_ann, theta_i_ann); the general MoC solver
    is Zucrow-Ch.17 ROTATIONAL, so nonuniform IVLs propagate correctly.
    Feed the family s(xi) from the repo's detonation chain (CJ +
    fill/blowdown states) or from URANS slices.
N4. THERMOCHEMISTRY ACROSS THE CYCLE: gamma_s and T0 drift along the
    blowdown (recombination); frozen-vs-equilibrium path differences.
    F_xi = a[Sigma; gamma(xi)] Pc(xi) - ... : an averaged-kernel problem
    breaking T3 in principle; MEASURED small in practice (Sec. 5.1b,
    corrected in-repo numbers: gamma_s 1.1537 -> 1.2093 over the cycle,
    eps* shift -0.56%, Isp penalty of the frozen-gamma design
    -0.00028%, second order). First-order
    closure: design at gamma_eff = <Pc gamma>/<Pc> ~ gamma_CJ. Tool:
    GENO gamma(T) backend + per-phase CEA states from the repo's CJ/HP
    chain (contour-level confirmation pending, Phase C iv).
N5. UNSTEADINESS AT FINITE St (D1 marginal: St = O(0.1-1)). First-order
    correction to J via nozzle admittance / transfer functions
    (Marble-Candel) driven by the blowdown's pressure-entropy wave
    content; the T0 wave-frame formulation is the exact nonperturbative
    backstop. This channel decides whether the whole quasi-steady
    optimization is trustworthy - it must be quantified, not assumed.
N6. 3-D SWIRL / AZIMUTHAL GRADIENTS (D2 violated): the full T0 problem -
    Rao on a 3-D control surface crossed by helical streamlines in the
    rotating frame. Virgin territory; practical route is ensemble/
    steady-rotating-frame adjoint RANS rather than 3-D MOC.

Measure-theoretic remark (pretty, and useful for N1): the exponential
blowdown makes the pushforward of uniform time onto pressure LOG-UNIFORM:
dmu(Pc) = dPc / (Pc ln PR) on [P_CJ/PR, P_CJ]. "Design an RDE nozzle" =
"design a nozzle optimal in mean over a log-uniform NPR ensemble" - the
canonical operating measure of the engine. The whole theory holds for any
operating measure mu; the RDE fixes mu physically where multipoint
aerodynamic design must posit it.

------------------------------------------------------------------------------
## 7. Conjecture C1 (the shrouded plug - the RDE question proper)

GENO's Veen decomposition F = F_shroud + F_plug + F_kernel (causally
separable, two independent variational DOF) meets the T3/T4 dichotomy
head-on: the SHROUD is a fixed wall (its per-phase thrust is linear in Pc
-> collapses to design-at-<Pc>, and it is the component exposed to
overexpansion loss at low phases), while the PLUG is a free boundary
(T4 -> wants the peak). Conjecture C1: in the S-H limit the optimal
cycle-averaged shrouded plug shifts expansion duty maximally from shroud
to plug - short shroud sized by peak containment (the shape-level meaning
of S-H's eps_max cap), plug carrying the excursion - and the optimal
DUTY SPLIT (shroud exit area vs plug length), under real constraints
(length, base pressure, heat load), is a genuinely cycle-averaged
quantity satisfying (*)-(**) with mixed corner conditions (CSTR_PA
averaged on the shroud lip, plug corner averaged at the truncation).
This - "how much of the RDE expansion belongs to a wall and how much to a
free surface, given the cycle measure mu" - is, in one sentence, the
optimal-RDE-nozzle-shape question, and it is well-posed here for the
first time.

------------------------------------------------------------------------------
## 8. The general problem, mathematically SOTA: a three-rung ladder

Sections 2-7 live inside the S-H idealization and its immediate
violations. The GENERAL problem - what "optimal RDE nozzle shape" means
with no collapse assumed anywhere - is best organized as a ladder of
three formulations of decreasing exactness and increasing tractability,
with THEOREM-GRADE bridges between rungs. The innovation is the ladder
itself: the RDE nozzle literature has none of the three rungs formalized,
and the bridges are where the new mathematics sits.

### Rung 3 (exact): shape optimization of a LIMIT CYCLE

The honest objective is the long-time-average thrust of the time-periodic
(limit-cycle) solution of reactive compressible Euler/Navier-Stokes in
the Sigma-dependent domain:

    J[Sigma] = lim_(T->inf) (1/T) Int_0^T dt Int_S (rho u_x (u.n)
               + (p - Pa) n_x) dA,   subject to the unsteady PDE limit
               cycle in Omega(Sigma).

The design variable moves an ORBIT, not a steady state. This class is
where modern unsteady-adjoint mathematics lives:

  (3a) WAVE-FRAME STEADIFICATION (Theorem T0): when a single steadily
       rotating mode exists, the orbit is a relative equilibrium
       (traveling wave) and the problem becomes STEADY 3-D shape
       optimization with swirl in the rotating frame - well-posed
       adjoint, standard cost. The genuinely new mathematical ingredient:
       the rotation rate Omega is an UNKNOWN of the solution (the
       eigenvalue of the traveling wave), and Omega depends on Sigma.
       The stationarity system therefore needs a phase condition and the
       sensitivity dOmega/dSigma - the adjoint of a periodic orbit /
       relative equilibrium in the dynamical-systems sense, not a plain
       steady adjoint. To our knowledge this has never been written for
       an RDE (or any combustor) shape problem.
  (3b) HARMONIC-BALANCE ADJOINT: when no exact co-moving frame exists
       (multi-mode, counter-rotating pairs, injector-coupled
       oscillations), expand in Fourier modes locked to the base
       frequency and its harmonics; the HB system is mathematically
       steady, so the adjoint is well-posed and cheap. This is
       established SOTA in turbomachinery shape design (discrete HB
       adjoints, monolithic one-shot HB optimization, quasi-periodic
       extensions) and has NEVER been applied to an RDE nozzle. The RDE
       is an unusually good HB customer: a dominant frequency with a
       handful of energetic harmonics.
  (3c) SHADOWING-TYPE ADJOINTS (LSS/NILSS) only if operation is
       genuinely aperiodic/chaotic - the expensive last resort.

Discrete-mode caveat, intrinsic to RDEs: the wave COUNT and direction
are discrete states; the map Sigma -> mode is piecewise constant, so
J[Sigma] is potentially DISCONTINUOUS across mode boundaries. The clean
formulation is robust: optimize the expectation or a risk measure (CVaR)
over a probability measure on modes, or the worst case over the
plausible mode set - shape optimization under model-form uncertainty,
with the mode measure calibrated from operability maps.

### Rung 2 (averaged variational): the ensemble-Rao system, done right

The T1/T2 system of Section 4, now stated as the general mid-fidelity
formulation with NO collapse assumed: maximize Int F[Sigma; s(xi)] dmu(xi)
with per-phase MOC-grade physics (nonuniform, rotational, gamma(T) per
phase) and the function-valued mass multiplier lambda_2(xi). Two facts
make this rung stronger than it looked from inside S-H:

  - The PER-PHASE optimality theory for nonuniform and highly ROTATIONAL
    inflow already exists: the Kraiko school's generalized variational
    contouring (nonuniform minimal-section 1982; highly rotational
    supersonic nozzle 1994; plug with nonuniform transonic inflow 2002;
    spike contouring 2007). The per-phase ingredient is NOT the novelty;
    the phase-averaged wall/corner system COUPLING those per-phase
    theories through one shared contour is. Concretely: plug Kraiko-type
    per-phase conditions into (*)-(**) and the entire N3 channel
    (phase-dependent inlet Mach/angle/vorticity) becomes computable at
    characteristic precision, no CFD.
  - Two structurally new solution strategies, both unexplored:
      (i)  DIRECT COLLOCATION OF THE AVERAGED EULER-LAGRANGE SYSTEM:
           discretize the phase family (quadrature in xi), unknowns =
           shared contour + per-phase terminal characteristics +
           lambda_2(xi) samples + shared geometric multipliers, equations
           = per-phase Rao/Kraiko conditions + averaged wall condition
           (*) + averaged transversality (**) + constraints; solve as one
           boundary-value problem (Newton). This solves the optimality
           system directly instead of nesting optimize-around-average -
           the analogue of collocation methods for optimal control, never
           done for nozzle families.
      (ii) DIFFERENTIABLE MULTI-PHASE MOC: reimplement the per-phase
           evaluator (GENO's unit processes are clean ODE marches) in an
           autodiff framework; reverse-mode differentiation of the
           characteristic march IS the per-phase adjoint, exact to
           machine precision, and the gradient of the phase-quadrature
           of J costs one backward sweep per phase. This turns the whole
           averaged problem into a smooth NLP with exact gradients on a
           spline contour space - SOTA optimization hygiene (trust-region
           SQP, shape-Sobolev preconditioning) with MOC physics.

  Bridge 2<->3 (rigor): two-timescale/homogenization expansion in
  St = tau_n/tc of the fast-oscillating inlet boundary condition:
  J_exact = J_averaged + St J_1 + O(St^2), with J_1 expressible through
  nozzle transfer functions (Marble-Candel type) driven by the cycle's
  pressure/entropy wave content. This gives the averaged rung an ERROR
  BAR - the missing license that all quasi-steady RDE nozzle work
  implicitly assumes.

### Rung 1 (collapsed limits): oracles, not recipes

T3 and T4 (and the S-H eps-identities) are NOT design procedures for the
general problem - inside the general attack they are demoted to
FALSIFIABLE LIMITING TESTCASES: any rung-2 or rung-3 machinery, run with
frozen gamma / full-flowing / uniform inflow, MUST reproduce
Rao-at-<Pc> and plug-at-peak to tolerance, or it is wrong. (Executable
verification culture, repo-style: the oracle can reject a broken
implementation.) Conversely their FAILURE modes (N1-N6) enumerate what
the general machinery must contain to be worth its cost.

### The coupling layer (deepest, and RDE-specific)

Everything above treats the inflow family/measure s(., mu) as given.
In reality Sigma feeds back on the wave: nozzle back-pressure and exit
impedance shift the fill height, the wave speed Omega, and the mode
count - i.e. s = s(xi; Sigma) and mu = mu(Sigma). The general problem is
BILEVEL:

    max_Sigma J[Sigma; s(.; Sigma), mu(Sigma)],
    s, mu = response of the chamber limit cycle to Sigma.

Tractability ladder: (a) frozen family (weak coupling - everything
above); (b) reduced chamber response map (the repo's matched-cycle
machinery generalized into a differentiable map Sigma -> (PR, Omega,
fill) - cheap, and the natural next use of the S-H apparatus);
(c) full coupled adjoint through the reacting chamber (differentiable
detonation - the research frontier, currently immature). The
mode-multiplicity caveat of rung 3 lives here too: the robust (measure/
CVaR) formulation is the mathematically sound way to keep the bilevel
problem well-posed across mode boundaries.

### What is genuinely new at each level (claim map)

- Rung 3a: adjoint of a rotating relative equilibrium with unknown
  Omega(Sigma), applied to thrust-shape design: NEW.
- Rung 3b: HB-adjoint applied to an RDE nozzle: NEW application of an
  established method.
- Rung 2: the phase-averaged wall + transversality system (*)-(**)
  coupling per-phase Rao/Kraiko theories through one contour; direct
  collocation of that system; differentiable multi-phase MOC: all NEW.
- Bridge 2<->3: O(St) error bar for quasi-steady RDE nozzle design via
  transfer functions: NEW.
- Rung 1: T3/T4 as executable oracles: NEW (and cheap).
- Coupling (b): differentiable chamber response map from the S-H
  matched-cycle: NEW.

------------------------------------------------------------------------------
## 9. Research program (phases, deliverables, existing gaps)

PHASE A - Theory paper (no new code). T0-T4 with full proofs; the
averaged conditions (*)-(**); the mu-measure formulation; N1-N6 taxonomy;
positioning vs. the RDE-nozzle and multipoint-design literature. The
collapse theorem T3 alone is a publishable clarification: it is the
missing justification AND the delimitation of every "design on the
time-averaged flow" recipe in the RDE literature.

PHASE B - Executable pilot in THIS repo (quasi-1D+, cheap, rigorous).
Extend `st_core.py` from the eps-line to a minimal contour family:
conical/bell/dual-bell parametrizations with a divergence factor
lambda_d = (1+cos(alpha_e))/2 and a separation criterion (N1), plus the
truncated-plug closure with a base term (N2). Deliverables:
  (i)  executable T3 check: with separation OFF, the family optimum must
       sit at the Rao/<Pc>-equivalent member (oracle test, T1c-style
       discrimination);
  (ii) first quantitative Delta-Isp of a cycle-designed vs
       mean-designed separated bell, and of a cycle-designed vs
       peak-designed truncated plug, on the Table-1 states (18 rows,
       states already cached in `data/st_nozzle_opt.json`);
  (iii) tests in the style of `tests/test_bell_optimality.py` (reject
       wrong averaging, certify stationarity).

PHASE C - GENO ensemble mode (the real machine). Gaps and steps:
  (i)   OFF-DESIGN ANALYSIS MODE: GENO designs contours; the averaged
        problem needs F[Sigma; s(xi)] for a GIVEN contour under an inflow
        family. The rotational MoC core (`MoC_Gen_m`) + `read_ivl_from_file`
        already march given fields; missing is a driver that fixes the
        wall and sweeps s(xi) (for plugs: a free-boundary off-design
        march - new unit process, moderate effort).
  (ii)  T3 ORACLE: run the ensemble driver on a frozen-gamma full-flowing
        bell family; certify collapse to Rao-at-<Pc> (this is Corollary 3
        as a CTest).
  (iii) AVERAGED CORNER CONDITION, minimally invasive: in `raocore_solve`
        / `boundarycurve_solve` the corner/constraint residual used by the
        bisection is replaced by its mu-weighted phase average (a sum of
        the same residual evaluated on the phase family). This SINGLE
        change turns the existing Rao/RaoPlug/Veen machinery into a
        cycle-averaged designer within its own doctrine (two multipliers,
        f2 marching intact per phase). Prerequisite for RaoPlug: fix the
        documented S1/S2 1-DOF gap (mass multiplier not enforced).
  (iv)  N3/N4: per-phase IVLs from the repo detonation chain via the
        annular inlet and .plt-per-phase thermo; quantify the inlet-
        nonuniformity contribution against the clean-blowdown baseline.

PHASE D - Validation and the exact problem. URANS/experiment anchors
(Harroun-Heister JPP 2021 nozzle study and successors); St-correction
(N5) via transfer functions; long-term: T0's 3-D rotating-frame problem
by steady rotating-frame adjoint RANS (N6). Success metric throughout:
Delta-Isp of cycle-designed vs best single-phase-designed contour, per
channel, on the Table-1 configurations - so every claimed gain has an
S-H-comparable number.

------------------------------------------------------------------------------
## 10. Honest limits

- T0 assumes one steadily rotating mode; real engines mode-hop.
- The S-H chamber abstraction itself (uniform annulus, exponential
  blowdown, choking marginal in the 20-atm hydrocarbon tails - margins
  0.97/0.65 documented in the validation) bounds everything built on T1.
- MOC regularity (D3) fails where secondary shocks enter the nozzle; the
  variational structure survives (adjoint Euler), the closed-form
  characteristic conditions do not.
- St = O(0.1-1) means N5 is not optional: the quasi-steady optimum must
  carry an unsteadiness error bar before any hardware conclusion.
- Novelty is claimed on a targeted-search basis (no cycle-averaged
  variational formulation found); a systematic review belongs to Phase A.
