# Mathematical foundations of RDE nozzle shape optimization: rigorous formalization and the SOTA toolbox

> SUPERSESSION NOTICE (2026-07-16). This note is kept as historical
> record. Superseded by the D1-D4 deliverables (`docs/rde_nozzle_problem_book.md`,
> `docs/rde_nozzle_literature_map.md`, `docs/rde_nozzle_theorem_ledger.md`,
> `docs/rde_nozzle_claims_verdict.md`). Known corrections vs this note
> (see D4 §2): the P1 corollary "sensitivity well-posed ⟺ spectrally
> robust" is FALSE as a biconditional (corrected to P1a/P1b in D3 §7);
> P2's "never written down" is weakened — the quasi-1D version is
> published (Giles-Pierce JFM 426:327 (2001)); Wasserstein-DRO shape
> optimization already exists (Dapogny et al. 2023) and must be cited
> as method when used.

Status: RESEARCH NOTE (mathematical foundations). Companion to
`docs/cycle_averaged_variational_nozzle.md` (engineering formulation:
T0-T4, averaged Rao system, three-rung ladder). This note goes one level
deeper: what the optimization problem IS as a mathematical object, which
parts of it are theorems, which are open problems of current PDE/dynamics
research, and which SOTA tools attack which sub-problem. Attributions are
from the literature as known to the author; a systematic review belongs
to the theory paper (Phase A).

------------------------------------------------------------------------------
## 1. The constraint: what equation, what solution concept

### 1.1 The physical constraint

Reactive compressible flow in Omega(Sigma) subset R^3 (annular chamber +
nozzle), conservation form

    dU/dt + div F(U) = S(U),
    U = (rho, rho u, rho E, rho Y_k),

inviscid (Euler) backbone; viscous/turbulent closure as a modeling layer,
not as the mathematical foundation. Boundaries: injection face Gamma_in
(injector impedance / choked-feed model), walls Gamma_w(Sigma) (slip),
outflow Gamma_out (supersonic a.e.). The design variable Sigma moves
Gamma_w.

### 1.2 The solution-concept problem (deeper than it looks)

The honest first question of a rigorous formalization is not "which
optimizer" but "constrained by WHAT solutions". Three regimes:

(S1) MOC-REGULAR PIECEWISE-SMOOTH CLASS. Steady (or wave-frame steady)
     supersonic flow, piecewise C^1 with finitely many transversal
     shocks/contact surfaces. Here solutions are CLASSICAL between
     discontinuities: per-phase Goursat/characteristic problems for the
     2x2 (planar) or 3x3 (axisymmetric rotational) hyperbolic systems
     are well-posed in the classical sense in domains of determinacy
     (the Li Ta-tsien school's semi-global classical solution theory is
     the reference framework). This is GENO's world and the world where
     Rao/Kraiko variational theory is literally true. Everything
     provable in this note is provable here first.

(S2) ENTROPY WEAK SOLUTIONS (multi-D Euler). The mathematically honest
     inviscid setting - and a minefield: multi-D well-posedness is open,
     and worse, convex-integration constructions (De Lellis-Szekelyhidi;
     compressible variants by Chiodaroli-De Lellis-Kreml) show
     NON-UNIQUENESS of entropy weak solutions. Rigorous consequence for
     us: "J[Sigma] = thrust of THE solution" is not well-defined in (S2)
     without an extra selection principle. The current SOTA repairs:
     (a) statistical / measure-valued solutions
     (Fjordholm-Kaeppeli-Mishra-Tadmor: entropy measure-valued and
     statistical solutions, computed as K-convergent ensemble limits of
     entropy-stable schemes) - the objective becomes an average against
     a solution MEASURE, which composes perfectly with the operating
     measure mu of the engineering note; (b) retreat to (S1) whenever the
     flow is MOC-regular; (c) accept a dissipative surrogate (RANS/LES
     closure) as the constraint and treat its model error explicitly.
     Optimization constrained by statistical solutions is essentially
     virgin mathematical territory - flagged as far frontier, not as a
     dependency of the program.

(S3) THE DETONATION WAVE ITSELF: a ZND-type reacting shock with a sonic
     (CJ) locus. Its multi-D stability/bifurcation theory (Erpenbeck's
     normal-mode analysis; Lee-Stewart; the Evans-function framework of
     Zumbrun and coworkers; galloping/cellular bifurcations, e.g.
     Texier-Zumbrun; reduced models of the Faria-Kasimov type) is the
     rigorous language for the EXISTENCE and SPECTRUM of the spinning
     wave. This is not background: Section 3 shows the design-sensitivity
     operator and the detonation-stability operator are the same object.

### 1.3 The transonic degeneracy

The sonic surface (RDE "throat") is where the steady operator changes
type (mixed elliptic-hyperbolic; Keldysh/Tricomi-type degeneracy).
Steady transonic rigorous theory (Morawetz's program; Chen-Feldman
transonic-shock results) is among the hardest corners of PDE analysis,
and in the RDE the sonic surface is azimuthally structured (steady but
non-planar in the wave frame). Design sensitivity THROUGH a degenerate
surface is an open analytical problem; the classical workaround - and
the rigorous content of Sauer/Kraiko-type throat analyses - is to
prescribe a regular sonic line as inflow datum and prove sensitivity
downstream of it. The program adopts this: the degeneracy is confined
inside the (given or reduced-model) inflow map, and all shape calculus
happens in the strictly supersonic region. Declared, not hidden.

------------------------------------------------------------------------------
## 2. The objective: an ergodic average over an attractor, not a state
##    functional

### 2.1 Honest definition

For fixed Sigma, after transients the flow settles onto an attractor
A(Sigma) carrying a physical (statistical) invariant measure mu_Sigma.
The objective is the ergodic average

    J[Sigma] = Int F_thrust dmu_Sigma,

i.e. SHAPE OPTIMIZATION OF A STATISTIC OF AN INVARIANT MEASURE. This
single sentence is what places the problem mathematically: it couples
shape calculus (Section 4) with ergodic/linear-response theory
(Section 3) - an intersection essentially unpopulated in the
literature.

### 2.2 The attractor hierarchy (and the tool switching with it)

(A1) RELATIVE EQUILIBRIUM (single spinning wave, axisymmetric wall):
     A(Sigma) is a rotating wave - a group orbit of the SO(2) azimuthal
     symmetry. mu_Sigma is supported on one orbit; J is the steady
     wave-frame thrust (engineering note, Theorem T0). Simplest and
     nominal case.
(A2) RELATIVE PERIODIC / QUASI-PERIODIC ORBITS (wave + longitudinal
     acoustics, injector coupling, modulated spin): mu on a torus;
     harmonic-balance representation natural.
(A3) CHAOTIC (unstable multi-wave regimes): mu an SRB-type measure;
     differentiability of J in Sigma is now the domain of Ruelle's
     linear-response theory - valid under uniform hyperbolicity,
     delicate beyond it - and the numerical counterpart is shadowing
     (least-squares shadowing of Wang; NILSS/NILSAS) precisely because
     the naive unsteady adjoint diverges at the Lyapunov rate.
(A4) MULTISTABILITY (coexisting 1-, 2-, N-wave and counter-rotating
     attractors with hysteresis - experimentally documented in RDEs):
     mu_Sigma is NOT unique; J[Sigma] is set-valued. The well-posed
     formulations are (i) expectation over a mode measure pi(Sigma)
     calibrated on operability maps, (ii) worst-case, or (iii) a risk
     measure (CVaR) - Section 6.

The mathematical program lives on (A1)-(A2) and treats (A3)-(A4) by
robust/risk formulations rather than by pretending smoothness.

------------------------------------------------------------------------------
## 3. The nominal case as a relative equilibrium: freezing, spectra, and
##    the sensitivity theorem that organizes everything

### 3.1 Freezing formulation (Beyn-Thuemmler)

In the co-rotating frame at unknown rate Omega, the spinning-wave state
solves

    0 = -Omega d(U~)/dtheta + L(U~; Sigma),          (RE)
    0 = <d(U~_ref)/dtheta, U~ - U~_ref>              (phase condition),

unknowns (U~, Omega). (RE) + phase condition is the "freezing method"
formulation of equivariant dynamics: the rotation symmetry produces a
zero eigenvalue (the group mode d(U~)/dtheta), and the phase condition
removes it, making the pair (U~, Omega) locally unique. Omega is an
EIGENVALUE-LIKE unknown: exactly the structure of continuation of
relative equilibria in large-scale dynamical systems (Newton-Krylov +
matrix-free Arnoldi, timestepper-based bifurcation analysis in the
Tuckerman-Barkley/Sanchez tradition).

### 3.2 Organizing theorem target (P1): well-posed design sensitivity at
###     a spectrally stable wave

CLAIM to prove. Let (U~, Omega) solve (RE) with: (i) piecewise-smooth
U~ with finitely many transversal shocks satisfying Majda's uniform
stability condition; (ii) the linearization of (RE) about U~ (with
shock-displacement unknowns included, i.e. linearized Rankine-Hugoniot
on each front) having spectrum off the imaginary axis except the single
group zero removed by the phase condition. Then, in a neighborhood of
Sigma in a W^{k,infty} shape manifold: (a) the map Sigma -> (U~, Omega)
is Frechet differentiable (implicit function theorem in the freezing
formulation, with Majda-type front linearization); (b) J[Sigma] is
differentiable with a Hadamard boundary representation of dJ; (c) the
adjoint problem - linearized (RE) transposed, with adjoint shock
conditions of Giles-Pierce type on each front and an adjoint phase
variable dual to Omega - is well-posed, and

    dJ[Sigma; V] = Int_Gamma_w g (V.n) dA,

with g assembled from (U~, adjoint state, adjoint of the phase
condition).

STRUCTURAL COROLLARY (the unification): the linear operator whose
invertibility is hypothesis (ii) IS the multi-D detonation stability
operator of the annulus (Evans-function object of (S3)). Hence:

    design sensitivity is well-posed  <=>  the operating mode is
    spectrally robust,

and the sensitivity dOmega/dSigma (how the wave speed responds to the
nozzle) comes from the same Evans-function machinery as the stability
margin. Design and operability are not two analyses; they are one
operator studied twice. To our knowledge this has never been stated for
RDEs, and it is the single most consequential structural fact of the
formalization: the optimizer inherits, for free, exactly the stability
information the engine designer needs anyway.

### 3.3 The symmetry trichotomy (why axisymmetric design is a theorem,
###     not a habit)

The wall is fixed in the LAB frame; the pattern rotates. Consequences:

- AXISYMMETRIC wall: the wall is invariant in the co-rotating frame;
  the relative-equilibrium structure (RE) survives; everything in 3.1-3.2
  applies; the problem is steady.
- NON-AXISYMMETRIC wall (amplitude delta > 0): the wall BREAKS SO(2);
  no frame makes the flow steady. The rotating wave generically becomes
  a modulated rotating wave / forced time-periodic solution (frequency
  locking between wave and wall harmonics is possible). The correct
  machinery jumps to Floquet theory and harmonic-balance adjoints; J is
  still differentiable in delta near delta = 0 under Floquet
  non-degeneracy, with dJ/ddelta expressible via the periodic adjoint.
- DISCRETE wall symmetry C_m (m-fold pattern, e.g. m struts or m
  modules): interacts with the wave number n; resonance conditions
  (m | n couplings) organize which wall harmonics do work on the wave.

This gives a THEOREM-SHAPED design principle: axisymmetry is exactly
the class in which the problem is a steady (cheap, well-posed) one;
leaving it costs one rung of the ladder (steady -> periodic). Any claim
that a non-axisymmetric RDE nozzle is better must pay that analytical
price - and P5 (Section 7) is the controlled way to evaluate it
perturbatively before paying it.

------------------------------------------------------------------------------
## 4. Shape calculus and existence: the honest state of the art

### 4.1 Design space and derivative structure

Rigorous options, in increasing generality: (i) graph contours
y_w in C^{1,1} with uniform bounds - the MOC/Rao native class;
(ii) method of mappings (Murat-Simon): Omega(Sigma) = images of a
reference domain under W^{k,infty} diffeomorphisms, shape derivative =
directional derivative along vector fields V, with the Hadamard
structure theorem giving dJ = Int_Gamma g (V.n) when J is shape
differentiable; (iii) oriented-distance / finite-perimeter frameworks
(Delfour-Zolesio) if topology change is ever on the table (it is not,
for now). Numerically, the SOTA counterpart of (ii) is Riemannian shape
optimization: Steklov-Poincare / Sobolev metrics as preconditioners
(shape gradients are distributions; smoothing them is not a hack but a
metric choice), quasi-Newton on the shape manifold.

### 4.2 What can break differentiability (and what to do)

- SHOCKS: the state is discontinuous; shape derivatives of the state
  contain shock-displacement distributions. The rigorous calculus in
  1-D conservation laws is shift-differentiability
  (Ulbrich; Bressan-Marson generalized tangent vectors): INTEGRAL
  functionals (thrust is one) are directionally differentiable with
  well-defined adjoints carrying interior conditions on shocks
  (Giles-Pierce). Multi-D theory is incomplete - an open problem the
  program inherits and states, working in (S1) where transversal-shock
  linearization (Majda) suffices.
- TOPOLOGY SWITCHES of the flow (separation onset, shock entering the
  nozzle, spike regime switch): J is locally Lipschitz, one-sidedly
  differentiable; the phase-average smooths switch phases of measure
  zero (engineering note, Sec. 4); persistent kinks are handled with
  Clarke subgradients and bundle/trust-region methods - mature
  non-smooth optimization, not improvisation.
- DISCRETE-ADJOINT TRAP (practical, sharp): the discrete adjoint of a
  shock-capturing scheme need not converge to the correct continuous
  adjoint at shocks (adjoint consistency fails for non-entropy-consistent
  discretizations). Mitigations: entropy-stable discretizations with
  proven adjoint consistency where available, shock-fitted formulations
  in (S1), and mandatory dot-product + oracle tests (T3/T4 collapse
  oracles of the engineering note).

### 4.3 Existence of optimal shapes

The generic obstruction: minimizing sequences of shapes can oscillate;
hyperbolic state maps Sigma -> U are not weakly continuous (shocks
appear/disappear), so direct methods fail in the unrestricted class.
Honest positions available:
(i) restricted compact classes: uniform cone condition (Chenais) or
uniform C^{1,alpha} bounds -> compactness; continuity of Sigma -> U
inside the MOC-regular regime by classical characteristic ODE theory ->
existence of a maximizer in the restricted class (P7). The failure
boundary is precisely loss of MOC-regularity along a maximizing
sequence - a meaningful, checkable mechanism, not an abstract fear.
(ii) finite-dimensional (spline) design spaces: existence trivial,
upper semicontinuity across topology switches to be respected.
(iii) the Newton's-problem tradition (Buttazzo-Kawohl) as the model
program: thrust-type shape functionals, existence restored by convexity
constraints, and the CAUTIONARY precedent that optimal bodies broke the
expected symmetry - the rigorous reason to treat axisymmetry via
Section 3.3 rather than by assumption.

------------------------------------------------------------------------------
## 5. The two-scale bridge: quasi-steady averaging as homogenization,
##    with an error bar

The averaged (rung-2) functional of the engineering note is the formal
St -> 0 limit of the exact (rung-3) objective, St = tau_n/tc. The
rigorous frame is homogenization in time of a fast-oscillating boundary
datum (two-scale convergence in the Allaire sense;
Bensoussan-Lions-Papanicolaou for the classical parabolic/oscillating
setting - the hyperbolic-boundary-datum variant is itself a research
item):

    J_exact = J_avg + St J_1 + O(St^2),

with the corrector J_1 given by a CELL PROBLEM in the fast variable =
the per-phase LINEARIZED unsteady nozzle response to the cycle's
pressure/entropy wave content. The classical combustion-instability
transfer functions (Marble-Candel nozzle admittances) are exactly the
physical realization of that corrector: the bridge is not a metaphor,
it is a computable formula. Deliverable P4: state and prove the
expansion under smoothness of s(xi) and MOC-regularity uniform in xi,
and compute J_1 for the S-H blowdown - the first quasi-steady RDE
nozzle result with an attached error bar. Note St = O(0.1-1) in real
engines: J_1 is not decoration; it decides whether rung 2 is licensed.

------------------------------------------------------------------------------
## 6. Uncertainty, multistability, and the bilevel coupling

- OPERATING MEASURE: J = Int F dmu with mu the cycle measure (canonical
  and LOG-UNIFORM in Pc for the exponential blowdown). Robustness to
  misspecified mu: distributionally robust optimization over a
  Wasserstein ball around the nominal cycle measure - directly
  meaningful physically (uncertain PR, uncertain waveform).
- MODE MULTISTABILITY (A4): expectation / worst-case / CVaR
  (Rockafellar-Uryasev) over the mode measure pi(Sigma); CVaR is the
  right shape for "avoid catastrophic separated/side-load phases"
  objectives too (tail-thrust and side-load functionals from the HB
  representation).
- CHAMBER-NOZZLE COUPLING: s = s(xi; Sigma), mu = mu(Sigma) - a BILEVEL
  problem whose lower level is the chamber limit cycle. SOTA frames:
  optimistic/pessimistic bilevel programming, Mordukhovich-type
  variational analysis for the nonsmooth lower-level map; if mode
  selection is modeled by a complementarity system, the problem is an
  MPEC. The tractable middle rung: a DIFFERENTIABLE REDUCED RESPONSE
  MAP Sigma -> (PR, Omega, fill) built from the repo's matched-cycle
  machinery, with the full coupled adjoint (differentiable detonation)
  kept as the declared frontier.

------------------------------------------------------------------------------
## 7. Theorem targets (the proof program)

P1. Well-posed sensitivity at a spectrally stable spinning wave
    (Sec. 3.2): freezing + IFT + Majda front linearization +
    Giles-Pierce adjoint shock conditions. The organizing theorem.
P2. RAO = ADJOINT. In the MOC-regular class, the classical
    Rao/Guderley-Armitage/Kraiko optimality conditions are exactly the
    closed-form solution of the steady adjoint Euler problem for the
    thrust functional (adjoint characteristics = Rao's control-surface
    conditions; the two multipliers = the adjoint boundary data). This
    is folklore-adjacent but apparently never written down; it welds the
    classical variational lineage to modern adjoint machinery and makes
    GENO a special-purpose adjoint solver avant la lettre.
P3. AVERAGED OPTIMALITY SYSTEM. Existence of the function-valued
    multiplier lambda_2(xi) (in L^2(dmu)) and validity of the averaged
    wall + transversality system (*)-(**) of the engineering note,
    under per-phase MOC-regularity, via Zowe-Kurcyusz-type constraint
    qualification applied phase-wise + measurable selection.
P4. O(St) EXPANSION with transfer-function corrector (Sec. 5).
P5. SYMMETRY TRICHOTOMY, perturbative version: near an axisymmetric
    design, J is differentiable in the non-axisymmetric amplitude delta
    under Floquet non-degeneracy, with dJ/ddelta via the periodic
    adjoint; sign conditions decide whether leaving axisymmetry can
    EVER pay before committing to rung-3b machinery.
P6. STABILITY OF THE COLLAPSE. Quantitative version of T3: the distance
    between the cycle-optimal shape and the Rao-at-<Pc> shape is
    bounded by (and generically comparable to) explicit measures of the
    hypothesis violations (separation measure of the cycle, inlet
    nonuniformity amplitude, gamma excursion). Turns "is mean design
    wrong?" from a binary into a perturbation estimate - and the
    gamma-channel probe (engineering note Sec. 5.1b: eps* shift -1.9%,
    Isp penalty -0.001%) is its first measured instance.
P7. EXISTENCE in uniform C^{1,alpha} graph classes with uniform
    MOC-regularity (Sec. 4.3), with the failure boundary identified as
    loss of regularity (wall shock formation).

------------------------------------------------------------------------------
## 8. The placement claim (where this problem lives in mathematics)

The problem sits at the - currently empty - intersection of six mature
fields:

1. EQUIVARIANT DYNAMICS / PATTERN FORMATION: rotating waves, freezing
   method, relative equilibria continuation (Beyn-Thuemmler;
   Golubitsky-Stewart; large-scale continuation a la
   Tuckerman/Sanchez). Supplies: the steady formulation, Omega as
   unknown, the trichotomy of Sec. 3.3.
2. HYPERBOLIC CONSERVATION-LAW CONTROL AND CALCULUS: shift-
   differentiability and adjoints with shocks (Ulbrich, Bressan-Marson,
   Giles-Pierce, Majda stability); boundary controllability of
   quasilinear hyperbolic systems (Li Ta-tsien school - wall design IS
   boundary control of a quasilinear hyperbolic system, and their
   constructive MOC proofs parallel GENO's marching). Supplies: the
   derivative concept and the adjoint at shocks.
3. SHAPE OPTIMIZATION: Murat-Simon, Delfour-Zolesio, Hadamard
   structure, Riemannian/Steklov-Poincare shape metrics, Newton's
   problem existence program (Buttazzo-Kawohl, Chenais). Supplies:
   design-space rigor and existence technology.
4. ERGODIC OPTIMIZATION / LINEAR RESPONSE: Ruelle response, shadowing
   (LSS/NILSS) - reserved for the chaotic regimes; harmonic-balance
   adjoints (turbomachinery SOTA) for the periodic ones. Supplies: the
   objective's very definition beyond the nominal mode.
5. HOMOGENIZATION / TWO-SCALE ANALYSIS: oscillating-data averaging with
   correctors; Marble-Candel admittances as the physical corrector.
   Supplies: the licensed bridge between averaged and exact objectives.
6. OPTIMIZATION UNDER UNCERTAINTY / BILEVEL AND VARIATIONAL ANALYSIS:
   CVaR, Wasserstein-DRO, MPEC/bilevel frameworks (Rockafellar-Uryasev;
   Mordukhovich). Supplies: well-posedness against multistability and
   the chamber coupling.

Classical variational gasdynamics (Rao 1958-61; Guderley-Armitage;
Sternin; the Kraiko school through the 1982-2007 nonuniform/rotational
generalizations) is the exactly-solvable core that every rung must
reproduce - the role the harmonic oscillator plays in quantum
mechanics. The RDE contributes the three genuinely new structural
features on top of it: (i) the objective is an invariant-measure
statistic with an SO(2) relative-equilibrium nominal case; (ii) the
optimality system couples a CONTINUUM of exactly-solvable per-phase
problems through one shared boundary (the averaged Rao system, with its
function-valued multiplier); (iii) the design couples back to the wave
through an eigenvalue (Omega) and a discrete mode variable - stability
and performance analyzed by the same operator (Sec. 3.2). Those three
features, not any single tool, are the thesis of the program.

------------------------------------------------------------------------------
## 9. Verification discipline (inherited from this repo's culture)

Every rung ships with executable falsifiers:
- oracle O1: frozen-gamma full-flowing ensemble machinery must collapse
  to Rao-at-<Pc> (T3);
- oracle O2: ideal-plug machinery must return the peak design (T4);
- oracle O3: adjoint/dot-product identities per phase to machine
  precision (differentiable-MOC route) or to discretization order
  (adjoint-consistent CFD route);
- oracle O4: dOmega/dSigma from the freezing adjoint cross-checked by
  finite differences of continued relative equilibria;
- oracle O5: the O(St) corrector J_1 cross-checked against direct
  unsteady simulation on one configuration.

A rung that cannot pass its oracles has no standing to report gains -
the same discipline as `validation/bell_optimality_proof.md`, one level
up.
