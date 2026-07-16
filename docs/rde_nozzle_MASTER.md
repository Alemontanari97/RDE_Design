# MASTER REFERENCE — The cycle-averaged variational nozzle problem for RDEs
# Idea, formalization, proofs, global optimality, implementation (M0)

Status: MASTER DOCUMENT OF RECORD (2026-07-16). Self-contained,
thesis-grade reference for all program phases. In case of conflict with
any other document, THIS + the D-deliverables win over the historical
notes. Depth per topic lives in the deliverables (map in Part VII);
the proofs of the core theorems are IN FULL here.

Rigor legend: THEOREM (proof here, verified line-by-line this session);
THEOREM* (proof within a declared model closure); SCHEMA (correct formal
structure, rigor gap named); CONJECTURE (precise + falsifier);
PRACTICE (no theorem, instrumented).

==============================================================================
PART I — THE IDEA (and why it is new)

A rotating detonation engine feeds its nozzle with a PERIODIC family of
states: at each azimuthal station the products' state (P, T, M, flow
angle, composition) sweeps a cycle as the wave passes. The nozzle is ONE
and FIXED. Classical nozzle optimization (Rao 1958; Guderley-Armitage;
the Kraiko school) designs for ONE steady inflow state; RDE practice
either averages the flow first and designs classically, or sweeps
parameters with CFD. The idea: define the total thrust functional as the
integral of per-state (per-phase) thrust functionals over the cycle
measure,

    J[Sigma] = Int_Xi F[Sigma; s(xi)] dmu(xi),

and derive Rao-type stationarity for the SHARED contour: per-phase
classical conditions coupled by mu-averaged wall and endpoint conditions.
Three structural discoveries organize everything:
 (1) STEADIFICATION IS EXACT for a single rotating mode (T0): the
     averaged functional is a genuine steady 3-D thrust functional in
     the wave frame — indeed the instantaneous thrust is CONSTANT.
 (2) A COLLAPSE DICHOTOMY: for fixed full-flowing walls under pressure-
     scaling similarity the averaged problem collapses EXACTLY to the
     classical design at the mean pressure (T3) — explaining why the
     field's "design on the averaged flow" works; for free boundaries
     the ideal plug is optimal at the PEAK pressure (T4); the first
     genuinely averaged problems are the truncated plug and the
     shroud/plug duty split.
 (3) THE MEASURE SELECTS THE TOPOLOGY (OP-11): in the configuration-free
     formulation the optimal nozzle TYPE (bell / plug / shrouded) is an
     output — a phase diagram over (constraints) x (spread of mu), whose
     limits are theorems (T3, T4, the geometry-free bound).
Novelty: verified query-bounded by three independent adversarial passes
(six-strand web survey; 16-agent red-teamed panel; page-level read of
the classical corpus). Every component is prior art in isolation; the
constructive certificate-bearing composition is unpublished. Residual
due diligence: Kraiko-1979/PMM human pass (gate G5) before submission.

==============================================================================
PART II — FORMAL DEFINITIONS

D2.1 (Domain and constraint). Reactive compressible Euler (viscous
closure = declared model layer) in Omega(S) = E \ S, E an envelope
cylinder downstream of the annulus, S the SOLID SET (design variable)
with attachment at the chamber lip(s) and uniform cone condition.
Configurations (bell / plug / shrouded / E-D / ...) are the topology
sectors of S — outputs, not inputs. Working class A: spline manifolds
in uniform C^{1,1} per sector.

D2.2 (Exact objective). J_exact[S] = lim_{T->inf} (1/T) Int_0^T F_S(t)dt,
F_S(t) = Int_S [rho u_x (u.n) + (p - Pa) n_x] dA on any enclosing
axisymmetric control surface; requires an attractor with invariant
measure (statistical stationarity — the weakest standing hypothesis)
and a solution concept (D2.5). Pa constant.

D2.3 (Operating measure and averaged objective). mu = pushforward of
normalized cycle time under t -> xi; averaged (rung-2) objective
J[Sigma] = Int F[Sigma; s(xi)] dmu(xi), with F the steady per-state
thrust (wall form or Rao control-surface form; equal by the momentum
theorem in the S1 class).

D2.4 (Design interface Gamma_d). A fixed axisymmetric surface
downstream of all heat release carrying the data family s(xi); the
CONTRACT is (Gamma_d, data class, validity): R1 causal separation;
R2 well-posed data (full state only on axially supersonic patches —
see L4; subsonic patches: incoming invariants + impedance closure or
choking closure, decision tree in D1 §4.3bis); R3 measurability.
Idealization ladder: I0 coupled bilevel / I1 wave-frame steady field /
I2 per-phase meridional profiles / I3 sonic family (P0,T0)(xi) /
I4 single mean state.

D2.5 (Solution classes). S1: piecewise-smooth MOC-regular (finitely
many transversal fronts, no wall-shock formation): classically
well-posed (Li Ta-tsien semi-global framework), membership checkable a
posteriori (Sternin/Rao-Beck boundary function). CANONICITY (corrected,
precision pass 2026-07-16): in SHOCK-FREE (locally Lipschitz) regions
and regimes, weak-strong uniqueness (Dafermos relative entropy;
measure-valued version Brenier-De Lellis-Székelyhidi, Comm. Math.
Phys. 305:351-361 (2011), doi:10.1007/s00220-011-1267-0 — VERIFIED)
makes the classical solution THE solution of every admissible concept.
ACROSS transversal shocks the strong comparison solution is not
Lipschitz and the general multi-D weak-strong property is OPEN;
partial support: 1-D uniqueness of BV/piecewise-smooth solutions
(Bressan school) and shift/a-contraction shock stability (Vasseur-
Krupa line, essentially 1-D). S1 canonicity WITH shocks is therefore a
DECLARED conditional (backed by Majda stability of the fitted fronts),
not a theorem — ledger-grade honesty, consistent with the panel's
refutation of relative-entropy certificates for shocked orbits. S2:
entropy weak — non-unique in multi-D (convex integration), never used
as a constraint. S3: statistical — roof definition only.

==============================================================================
PART III — THEOREMS WITH PROOFS

------------------------------------------------------------------------------
THEOREM 0 (the definition chain of RDE thrust — why the phase integral
is legitimate). THEOREM (exact links) + one declared choice + one
priced approximation.
DEFINITION (mechanical thrust): F_wall(t) = Int_W (p - Pa) n_x dA over
the wetted surfaces W (+ declared viscous layer); legitimate gauge
reference since constant Pa integrates to zero over a closed surface.
This — the force on the structure — is the definition; everything else
must be derived.
IDENTITY (unsteady momentum theorem, fixed control volume V bounded by
W and a fixed control surface S):
    F_wall(t) = Int_S [rho u_x (u.n) + (p - Pa) n_x] dA
                + d/dt Int_V rho u_x dV.
Instantaneously, wall force and flux DIFFER by the axial-momentum
STORAGE term — not small in an RDE at kHz.
CLAIM (mean equality — exact). For T-periodic flow with bounded
contained momentum: <F_wall>_T = <F_S>_T for EVERY fixed S.
PROOF: the storage term is the time derivative of a bounded periodic
function; its period integral is Q(T) - Q(0) = 0 exactly. Average the
identity. S-independence: apply between any two surfaces. QED.
(Quasi-periodic/chaotic: Birkhoff averaging, Q(T)/T -> 0 under bounded
momentum — same conclusion in the limit sense.)
STRENGTHENING (single rotating mode): the wall pressure on an
axisymmetric wall is p(x, r_w, theta - W t), whose theta-integral is
shift-invariant: F_wall(t) itself is CONSTANT and the storage term is
identically zero — in the nominal regime mechanical thrust ≡ flux ≡
steady wave-frame value with no averaging needed (consistent with, and
feeding, Theorem 3).
DECLARED CHOICE: the mission objective is the MEAN <F_wall> by scale
separation (kHz cycle vs vehicle dynamics: the vehicle responds to
impulse); fluctuations leave the OBJECTIVE and enter CONSTRAINTS
(side loads / fatigue — CVaR tail objectives of the robust layer).
Isp relation: Proposition 1 (O1).
THE ONLY APPROXIMATION in the chain: representing the exact mean as a
sum of STEADY per-phase thrusts,
    <F_wall> = Int_Xi F_steady[Sigma; s(xi)] dmu(xi) + O(St),
is the quasi-steady (rung-2) step — exact as St -> 0, priced by the P4
corrector, with Theorem 3 as the nonperturbative backstop. All
approximate content of the formulation lives in this one link (ledger
row D1).
DO NOT CONFLATE the two "unsteady" objects: (1) the STORAGE term
dQ/dt = d/dt Int_V rho u_x dV in the exact thrust identity — pure
bookkeeping (momentum borrowed and returned each cycle), instantly
large at kHz, EXACTLY zero in the mean by periodicity, identically zero
for a single rotating mode (volume integral of a function of
theta - W t is shift-invariant); it introduces NO approximation.
(2) the O(St) QUASI-STEADY error — a genuine modeling error living in
the per-phase steady factorization of the (exact) mean flux, NOT in the
momentum balance. "Storage averages to zero" does NOT imply the
quasi-steady step is exact, and "kHz unsteadiness" does NOT imply the
mean thrust needs unsteady corrections at the balance level.

------------------------------------------------------------------------------
PROPOSITION 1 (O1 — objective equivalence at frozen choked feed). THEOREM.
Hypotheses: (i) the cycle family, period and A_t are Sigma-independent
(frozen family H-F1); (ii) mdot(t) = Pc(t) A_t / c*(t) (choked feed H2).
Claim: argmax_Sigma Isp_cycle = argmax_Sigma J, and the Isp numerator
equals Int F dt identically.
PROOF. mdot c* = Pc A_t for ANY c*(t) law, hence
Int mdot CF c* dt = Int Pc A_t · F/(Pc A_t) dt = Int F dt. The
denominator g0 Int mdot dt is Sigma-independent by (i)+(ii). QED.
Failure channels: bilevel coupling breaks (i) — then thrust-max and
Isp-max are DIFFERENT problems (N-O1±); unchoked tails break (ii);
axially subsonic interface patches can make mdot Sigma-dependent.
Note: with a fully axially supersonic data interface (L4), (i) and the
mdot-independence hold EXACTLY without invoking upstream choking.

------------------------------------------------------------------------------
LEMMA 2 (O2 — log-uniform measure). THEOREM.
For the exponential blowdown Pc(xi) = P_CJ · PR^(-xi), xi ~ U[0,1):
xi = -ln(Pc/P_CJ)/ln PR, so dmu_P = dPc/(Pc ln PR) on [P_CJ/PR, P_CJ]:
the engine's canonical operating measure is LOG-UNIFORM in pressure.
QED. (Any measured cycle simply replaces mu_P; the theory is
measure-agnostic.)

------------------------------------------------------------------------------
THEOREM 3 (T0 — wave-frame exactness, strengthened). THEOREM.
Hypotheses: rotating-pattern flow q(x,r,theta,t) = q~(x,r,theta - W t)
(W := Omega_w; piecewise-smooth, transversal fronts); S fixed
axisymmetric; Pa constant.
Claims:
 (i)  F_S(t) is CONSTANT in time (not merely mean-equal): the single-
      mode RDE has steady thrust through every axisymmetric surface.
 (ii) F_S equals the identical integral of the wave-frame steady fields
      with relative velocity w = u - W e_x x r: on axisymmetric S,
      w_x = u_x and w.n = u.n.
 (iii) The rotating-frame steady momentum balance closes with zero
      axial frame forces.
PROOF. (i) At fixed (x,r) the integrand is g(theta - W t); its
theta-integral over [0,2pi) is shift-invariant, so each annular strip
contributes a t-independent amount. (ii) The rotation adds only an
azimuthal velocity component W r e_theta; axisymmetric S has n_theta=0,
so (W e_x x r).n = 0 and w.n = u.n; trivially w_x = u_x. (iii) Coriolis
-2 W e_x x w is orthogonal to e_x; centrifugal W^2 r e_r is radial. QED.
Consequences: J_exact = steady 3-D wave-frame shape functional with W
an EIGENVALUE-like unknown (freezing formulation + phase condition);
thrust-trace flatness = executable mode-purity diagnostic (N-T0').
CAUTION (verified weakening): T0 steadifies the PROBLEM; it does NOT
transfer Rao's 2-D closed-form machinery to 3-D swirl (open, N6).

------------------------------------------------------------------------------
LEMMA 4 (N-SW — spacelikeness is frame-invariant; the swirl audit). THEOREM.
In the wave frame w_theta ~ u_theta - W r ~ -D_CJ: streamlines are
strongly helical. Distinguish:
 (a) TYPE: the steady operator is hyperbolic where |w| > c (real Mach
     cones) — the sweep HELPS. The relative sonic locus |w| = c
     attached to the wave IS the Chapman-Jouguet surface: the causal
     firewall (no downstream signal climbs into the reaction zone
     through it in CJ operation) — grounding H-F1 and locating the
     coupling channels in the UNSHIELDED sectors (fill, deflagration,
     oblique-shock tail).
 (b) DATA SURFACES: a plane x = const is spacelike iff the Mach cone
     from each of its points lies on one side: angle(w,e_x) + alpha
     < pi/2 with alpha = arcsin(c/|w|), i.e. cos(angle) > sin(alpha),
     i.e. w_x > c. Since w_x = u_x and c is frame-invariant:
         AXIAL INTERFACE SPACELIKE  <=>  u_x > c,  IN EVERY FRAME.
PROOF of (b): the chain of equivalences above; each step elementary. QED.
Consequences: CJ-sonicity licenses NO axial MOC (condition hierarchy
C1 hyperbolicity ⊅ C2 axial marching (u_x>c) ; C3 = any time-like
foliation, helical in the wave frame, never constructed = N6; C4 = CJ
type/firewall only). Rung-3a must be an implicit BVP (freezing +
Newton-Krylov), which marches nothing. The huge relative swirl never
enters rung 2: it IS the O(St) sweep term.

------------------------------------------------------------------------------
THEOREM 5 (T3 — the collapse, fixed wall). THEOREM.
Hypotheses: H1 one frozen gamma common to all phases; H2' fixed wall,
full-flowing, supersonic exit at every phase (ambient-blind interior);
H3 phase-independent nondimensional inflow shape (phases differ only
through (P0(xi), T0(xi))); H4 per-phase uniqueness in the class; Pa
constant; shared geometric constraints.
Claim: J[Sigma] = F[Sigma; <Pc>_mu] POINTWISE on shape space, where
<Pc>_mu = Int Pc dmu. Hence the cycle-optimal fixed wall is EXACTLY the
classical contour designed at the mean pressure.
PROOF.
Lemma A (pressure-scaling similarity; holds for gamma(T) and ACROSS
transversal shocks). Fix Sigma, T0. If (u,T,p,rho) solves the steady
problem at stagnation (P0,T0), then (u,T,kp,krho) solves it at
(kP0,T0), k>0: continuity/energy are untouched at fixed (u,T); momentum
contains p only through grad(p)/rho, invariant; EOS rho = p/(RT)
preserved; entropy s shifts by the constant -R ln k so isentropes map
to isentropes; slip and Mach-type inflow BCs are scale-free; by H2' no
ambient datum enters. ACROSS SHOCKS: the Rankine-Hugoniot fluxes are
degree-1 homogeneous in (rho, rho u, rho E) at fixed (u,T) (rho e =
rho e(T) scales by k), and the entropy-jump and Lax/Majda transversality
conditions are k-invariant. Uniqueness (H4) makes the scaled solution
THE solution. Hence M(x), theta(x), T(x) are phase-independent and
p_xi(x) = Pc(xi) · PI(x; Sigma) for one fixed field PI.
Lemma B (stagnation-temperature similarity; REQUIRES calorically
perfect gas; named "T0-similarity" in earlier notes — renamed here to
avoid collision with Theorem 3/T0). At fixed P0, T0 -> T0' rescales u
by sqrt(T0'/T0) and leaves (M, theta, p, T/T0) invariant; the thrust
contains T0 nowhere (CF is T0-blind). Dies for gamma(T): no similarity
variable in T — this is exactly where the collapse's boundary sits.
Lemma C (affinity). Per phase F[Sigma; s(xi)] = a[Sigma]·Pc(xi)
- Pa·b[Sigma]: the wall integral Int (p - Pa) n_x dA = Pc Int PI n_x dA
- Pa (A_e - A_t), and the throat momentum flux scales with P0.
Assembly. J = Int (a Pc - Pa b) dmu = a <Pc> - Pa b = F[Sigma; <Pc>].
Identical functions on the identical feasible set: identical stationary
points and optima. QED.
Remarks (verified): (R1) per-phase optimal contours DO move with Pc —
the average of an affine family is again a member, that is all;
(R2) the averaged corner condition collapses coherently because in this
class the endpoint weight is phase-independent (see T7).
Corollaries: (C1) the repo's 1-DOF Theorem 1 is the rank-1 shadow;
(C2) Pa enters linearly too: trajectory-averaged fixed-bell design
collapses to <Pa> — cycle average and altitude average are one
mathematics (the dual-bell literature exists because SEPARATION breaks
the linearity); (C3) oracle O1: any ensemble machinery run under
H1-H4 MUST return Rao-at-<Pc> with Delta-Isp = 0.
Sharpness: two-phase two-gamma counterexample — J = (1/2)[a(g1)Pc1 +
a(g2)Pc2] - Pa b is not of the collapsed form; first-order closure
gamma_eff = <Pc gamma>/<Pc> (~ gamma_CJ under blowdown weighting: the
S-H freeze-at-CJ choice retro-justified); design penalty second order
(envelope theorem). For genuinely reacting gas the closed-form corner
DIES (Hoffman 1967 Eq. 78: multiplier-field condition E = 0 replaces
it) — the N4 ladder: frozen ⊂ gamma(T) (fails in principle, small in
practice, E4 oracle pending) ⊂ finite-rate (adjoint-level mandatory).

------------------------------------------------------------------------------
THEOREM 6 (T4 — plug simultaneous optimizability). THEOREM* (under the
ideal-adaptation closure: wall pressure clamps to Pa downstream of each
phase's full-expansion point; upstream, T3-class scaling).
Claim: per phase, F[Sigma_l; s(xi)] is nondecreasing in plug extension l
and exactly constant for l >= l(xi), with l(xi) increasing in Pc(xi);
the per-phase argmax sets are nested half-lines [l(xi), inf); hence
    max_Sigma Int F dmu = Int max_Sigma F dmu,
attained by the PEAK-phase design: the untruncated plug at NPR =
P_CJ/Pa (capped by eps_max where binding).
PROOF. Monotonicity: on the exit-area-limited set the incremental
thrust of extension is (p_wall - Pa) dA_proj > 0; on the adapted set it
is zero by the closure. Constancy for l >= l(xi) likewise. l(xi)
increases in Pc because the full-expansion point moves downstream with
NPR (area-Mach monotonicity on the supersonic branch). Nesting: the
argmax set of phase xi is [l(xi), inf); the intersection over xi is
[l(xi_peak), inf), nonempty; on it every phase attains its max, so the
integral attains the integral of maxima, which is an upper bound by
monotonicity of the integral. Attainment/measurability: l(xi) is finite
for each xi (finite NPR), xi -> l(xi) is monotone in Pc(xi) hence
mu-measurable, and sup_xi l(xi) = l(xi_peak) is ATTAINED because Pc
attains its maximum on the (compact) cycle at the wave-passage phase.
QED.
Sharpness: a length cap L < l(xi_peak), a base-pressure model at a
truncation plane, or non-ideal adaptation break the nesting: then
max Int < Int max STRICTLY and the optimum satisfies the averaged
system (T7) with the mu-averaged plug corner condition. THE TRUNCATED
PLUG IS THE FIRST GENUINELY AVERAGED SHAPE PROBLEM (PB-2). Precedent
duty: the ideal-adaptation closure is published as a BOUND for
detonation cycles (Kraiko-Egoryan) — cite next to the closure.

------------------------------------------------------------------------------
PROPOSITION 7 (G-B — geometry-free upper bound) and COROLLARY (global
optimality over ALL topologies). THEOREM-grade / mechanism M1.
Claim: for ANY solid set S in ANY topology, under choked frozen feed:
    J[S] <= J_ideal = Int F_id(s(xi); Pa) dmu(xi),
F_id = thrust of complete isentropic per-streamtube expansion of phase
xi to Pa.
PROOF (sketch, rigorous). Hypotheses: adiabatic, inviscid, slip walls,
exhaust to quiescent ambient Pa. Fix a phase and a streamtube with data
(mdot, h0, s). Explicitly, F_id = mdot · V_id with
    V_id = sqrt( 2 [ h0 - h(s, Pa) ] )
(complete isentropic expansion to Pa, axially aligned). Any admissible
evolution can only increase entropy (shocks) and misalign momentum; at
given exit pressure Pa the axial momentum flux + pressure thrust is
maximized by the isentropic, axially aligned, fully expanded state:
entropy rise lowers exit velocity at fixed (h0, p_exit) since
dh/ds|_p = T > 0; misalignment loses the axial projection; incomplete/
over-expansion loses against full expansion by the classical
dF/dA_e = (P_e - Pa) sign argument on the supersonic branch. Integrate
over streamtubes and phases (measurability of xi -> F_id from R3).
QED (integral-flux relaxation: Efremov-Kraiko 2004, a weaker published
bound; axial-only energy variant = the EAP_i baseline, see Remark).
SHARPENING OF RECORD (2026-07-16, OP-0 ladder, src/thrust/bounds.py):
the dF/dA_e sign argument covers only the supersonic branch, so the
"complete expansion to Pa" form of F_id is the streamtube supremum only
for Pc/Pa >= ((g+1)/2)^(g/(g-1)). On subcritical phases
(1 < Pc/Pa < critical) the exit matching Pa is subsonic and the SONIC
exit strictly beats it (dF/dA_e = Pe - Pa < 0 along the subsonic branch
from the sonic point; jet matching Pe = Pa holds only at its endpoint):
executable counterexample g = 1.15, Pc/Pa = 1.3, dCF = +0.0070. F_id
must be CAPPED AT THE SONIC STATE; with the cap the bound is restored
and, at eps level, exactly attained by the per-phase relaxation
(int-max = ceiling, dual-route verified); the naive form is rejected by
tests/test_bounds.py on the four subcritical Table-1 rows
(choke_margin < 1). This proposition, the E-K comparison and the T4
closure (whose S-H spike form uses the naive branch on subcritical
tails) carry "min-cycle NPR >= critical" as an explicit hypothesis, or
the cap.
COROLLARY (mechanism M1: duality-gap-zero globality). Under the T4
closure with generous envelope, the untruncated peak-designed plug
ATTAINS J_ideal ⇒ it is GLOBALLY optimal over all topologies. This is
the precise sense in which a "total optimum independent of the shape
category" exists; at finite constraints the total optimum is the winner
of the FINITE SECTOR TOURNAMENT (cone condition ⇒ finitely many
topology sectors; per-sector existence P7; cross-sector comparison
licensed by shared constraints + this bound). The phase-diagram
conjecture OP-11 ("the measure selects the topology") interpolates the
proven limits: spread->0 ⇒ sectors tie at the Rao value (T3);
generous envelope ⇒ free boundary attains the ceiling (T4/M1);
vacuum ⇒ no finite optimum; tight length + large spread ⇒ duty split
(C1, open).

REMARK (relation to EAP — verified against Kaemming-Paxson, AIAA
2018-4567, NTRS 20180006890, full text read 2026-07-16). The industry's
Equivalent Available Pressure EAP_i is, verbatim from its Eqs. 1-8, the
PRESSURE-COORDINATE of J_ideal: each exit segment expanded
isentropically to ambient SEPARATELY (expand-then-average, never
mixed-out-then-expand), mass-flux-weighted specific quantities
(algebraically identical to our time-integrated fluxes, O1), computed
in the detonation frame where "area average = time average" — i.e. our
T0(i) used tacitly as a fact, proved here as a theorem. Deltas:
(1) baseline EAP_i declares non-axial energy unavailable (V_x only),
its +6% variant includes it: two adjacent ladder rungs,
EAP_i(axial) <= J_ideal(total); (2) EAP carries the quasi-steady and
azimuthal-decoupling hypotheses (our D1+D2) UNSTATED and UNPRICED —
the P4 corrector is, among other things, EAP's missing error bar;
(3) EAP is the combustor-alone CEILING: the program's bound gap
J_ideal - J(Sigma*) is the honest discount factor on advertised
pressure gain (cf. Paxson 2022: real truncated plug at 58-70% of the
notional ideal). The formalization CONTAINS and COMPLETES the EAP
doctrine rather than competing with it — a citable bridge for P-1.

REMARK (relation to the Stechmann-Heister-Harroun model — verified
against the full-text-derived granular spec, JSR 56(3):887-898 (2019),
doi:10.2514/1.A34313; local page renders + text in
`../project_build/tmp_st`, spec in `../project_build/specs/
stechmann_spec.md`; model mechanics independently validated in-repo
18/18 on Table 1). Concordances:
 (1) their Eq. (4) cycle Isp = total impulse / cycle propellant mass
     ≡ Def. 3.2 + Prop. O1: their mass-flux weighting of the
     instantaneous Isp is algebraically our time integral of F
     (numerator A_t Int Pc·CF dt via mdot·c* = Pc·A_t — the same pivot
     as the in-repo proof);
 (2) their F(t) = mdot·CF·c* is the PURE rung-2/I3 quasi-steady proxy;
     no momentum-storage discussion anywhere: Theorem 0 supplies the
     missing license, P4 the missing error bar — and their own flagged
     open item ("two timescales... the community has substantial work
     to do") is precisely what P4 answers;
 (3) their assumption list maps 1:1 onto the hypothesis ledger:
     asm 2 (M, gamma frozen) = H-T3.1; asm 3 (choked at all times,
     exit plane = thermal throat) = H2; asm 1 (exponential blowdown,
     complete fill) = the O2 measure generator; Eq. (9) validity
     (full-flowing bell) = H-T3.2; Eqs. (10)-(12) (ideal spike,
     Pe = Pa below max expansion) = the H-T4 closure verbatim;
 (4) THEIR NUMERICAL FINDINGS ARE INSTANCES OF THE THEOREMS HERE:
     bell eps_opt unchanged det-vs-CP (their Fig. 9, dotted optimum at
     the same eps in both panels) = the T3 collapse (repo Theorem 1);
     det aerospike sized by the PEAK with monotone-saturating Isp(eps)
     (Figs. 10/12: eps_opt 9.2-12.2 vs CP 3.6-3.9) = the T4 knee/
     plateau (repo Theorem 2); vacuum area ratios reported as "maximum
     values used in the simulation", not optima (Table 1 note) = the
     vacuum no-finite-optimum theorem (repo Theorem 3);
 (5) their Conclusion-7 loss ledger maps onto the violation channels:
     oblique-shock loss -> N3, gamma variation -> N4, off-design/
     separated nozzle -> N1, transient swirl -> N6, finite-rate
     kinetics -> the Hoffman boundary (N4 finite-rate rung).
QUANTITATIVE CONVERGENCE CHECK (executed 2026-07-16, closed-form,
one line per prediction): T3 predicts the bell optimum at
eps(NPR = <Pc>/Pa); T4 predicts the spike knee at eps(NPR = Pmax/Pa).
Against their Table 1 (Pcp = 20 atm, Ti = 200 K, Pa = 1 atm; peaks
from their Fig. 4, gamma back-computed 1.14/1.16, <Pc> = Pcp(1+DC)):
  H2/O2 : predicted bell 4.01 vs their 3.8; predicted spike knee 10.5
          vs their 9.2 (ratio 2.62 vs 2.42);
  CH4/O2: predicted bell 3.90 vs their 4.0; predicted spike knee 10.7
          vs their 11.4 (ratio 2.75 vs 2.85).
Agreement 3-5% (bell) and 6-14% (spike) — exactly the level warranted,
since their per-column optima re-optimize phi (changing PR and gamma
between columns) while the closed-form check holds phi fixed. Their
CEA-swept optima are thus reproduced by two one-line theorem
evaluations: independent numerical corroboration (their computations
predate this theory; no circularity).
The formalization therefore EXPLAINS the paper's empirical
regularities (its three nozzle findings are corollaries, now checked
NUMERICALLY, not only structurally), CLOSES its two flagged gaps
(timescale license = Theorem 0 + P4; fair-metric question = the bound
ladder), and inherits its comparison protocol (equal cycle mass +
throat area) as the frozen-family normalization. Together with the EAP
remark above, this is the second citable bridge for paper P-1 (target
venue: JPP class).

------------------------------------------------------------------------------
THEOREM-SCHEMA 8 (T7/T2 — the averaged stationarity system). SCHEMA.
Maximize J over Sigma in a restricted class, per-phase steady Euler
constraints (adjoint psi_xi per phase), per-phase mass flow fixed
(function-valued multiplier lambda2(xi) in the control-surface
formulation; intrinsic in the wall formulation), shared geometric
constraints (multipliers lambda_L, ...).
Stationarity structure (verified formally):
 (a) per a.e. xi: the per-phase adjoint Euler system; in S1 it reduces
     to the classical closed form — optimal control surface = the
     phase's characteristic; first integral
     f2 = V cos(theta -/+ alpha)/cos(alpha) = -lambda2(xi).
 (b) shared wall: Int_Xi G_xi(x) dmu + lambda_L g_L(x) = 0 a.e. on the
     wall, G_xi the phase Hadamard density — no phase satisfies its own
     wall condition; the mu-average does.
 (c) shared endpoint — THE WEIGHTED TRANSVERSALITY (**'):
         Int_Xi (dF/ds_E)[Sigma; s(xi)] dmu(xi) = 0,
     which factorizes R(xi)·w(xi) with R the classical corner residual
     and w > 0 a geometric-kinematic weight; w is phase-independent
     EXACTLY in the T3 class (there (**') reduces to the naive average
     — everywhere else the naive form is WRONG; every implementation
     must use (**')).
Non-smoothness: topology-switch phases are mu-measure-zero with F
continuous across them: Leibniz survives moving switches (boundary
terms cancel); persistent kinks: Clarke subdifferentials.
Named rigor gaps: P3 (lambda2 in L^2(dmu): measurable selection +
phase-wise constraint qualification — open, no obstruction known);
G12 (multi-D fitted-shock shape derivative: theorem only in 1-D
[Bressan-Marson; Ulbrich]; quasi-1D design rigor [Cliff-Heinkenschloss-
Shenoy]; 2-D practice [Baeza et al.]).
Executable reduction (verified in-repo): quasi-1D, only exit-area DOF:
(b)-(c) degenerate to <p_e(xi)> = Pa, i.e. NPR(eps*) = <Pc>/Pa — the
repo's Theorem 1 with its wrong-averaging rejector test.

==============================================================================
PART IV — THE GLOBAL-OPTIMALITY CONTRACT

"Without hypotheses" is excluded by theorem: (i) without an admissible
class no maximizer exists (vacuum: Isp strictly increasing in eps);
(ii) without a solution concept J is undefined (multi-D non-uniqueness);
(iii) without a measure the average is undefined. HYPOTHESES ARE THE
PROBLEM'S DEFINITION; the ledger instruments every one.
The contract for every delivered optimum Sigma*: EXISTENCE (P7:
Chenais compactness + S1-continuity uniform in xi + dominated
convergence; failure boundary = loss of S1-regularity, MONITORED by the
boundary function) + NECESSARY (T7 with (**')) + SECOND-ORDER
(reduced-Hessian) + GLOBALITY by a DECLARED mechanism:
 M1 duality-gap zero vs the bound ladder (J_ideal, Int-max, integral-
    flux) — certified global (T4 is an instance);
 M2 collapse transfer (T3 pointwise equality inherits classical
    globality);
 M3 monotone/unimodal structure (repo 1-DOF theorems are instances;
    target: unimodality of the truncated-plug duty variable);
 M4 exhaustive stationary-point enumeration (deflated continuation) +
    bound gap, finite-dimensional;
 M5 certified deterministic global search (Lipschitz/branch-and-bound)
    at 2-4 DOF.
Every Verdict states its mechanism and strength ("global", "within
delta of global, certified", "local + enumerated competitors").

==============================================================================
PART V — GENERALITY LADDER AND LICENSING LOGIC

The flow — not the method — selects the reduction, per design point:
| Flow class (census) | Machinery | Deliverable / rigor |
|---|---|---|
| single/k-wave rotating mode | T0 steadification (exact); rung 2 averaged + O(St) bar; wave-frame implicit BVP anchor | Sigma* + full certificate; per-phase THEOREMS, bridge CONJECTURE-with-falsifier |
| modulated / counter-rotating (RPO) | periodic BVP, unknown (Omega,T), doubly bordered adjoint; 2-D+t demonstrator | PRACTICE (space-time tracking 3-D absent) |
| multistable mode set | per-branch optimization + CVaR/DD-DRO outer layer over the mode measure | robust Sigma*; SCHEMA/PRACTICE |
| chaotic / mode-hopping | bounds + robust surrogates ONLY (shadowing refused: hypotheses fail across shocks) | honest refusal of certificates |
Licensing instruments: thrust-trace flatness (distance from
steadifiability); census refresh per accepted optimizer step (tier-flip
detection); St_n and drift numbers from the data (D1 ⊃ D2: one Strouhal
governs); mixed-interface decision tree (O1 move / O2 impedance +
mandatory coupling loop with measured q / O3 choking surrogate /
O4 anchor-always). Upstream-response model: AC part = admittance/
impedance ladder (compact linear -> O(He) -> full-frequency ->
compact-nonlinear -> state-space time-domain), exact for GRADIENTS by
definition of linearization; DC part = differentiated matched-cycle
response map; degrades declaredly at mode transitions (robust layer).

==============================================================================
PART VI — IMPLEMENTATION FORMULATION (what the coder builds)

VI.1 CycleFamily (contract C1): {P0, T0, thermo handle gamma(.;xi) |
M_in(y;xi), theta_in(y;xi), s(y;xi), [vorticity]} + mu weights +
provenance + stage-A audit results (characteristic completeness; Crocco
residual; spacelikeness margin min(M_x - 1) per phase; H-I2/choking
margins; projection norm if applied). Generators: matched-cycle (case
A, exists), wave-structure model (case B, the one new physics module),
calibrated/mission/DRO variants (cases C-F), file-based CFD.
GENERATED data passes the same audits as imported data.
VI.2 Per-phase evaluator: rotational MOC (Zucrow Ch.17 class; GENO
MoC_Gen semantics), gamma(T) backend, FITTED inherited sheet (RH on the
front), plug off-design free-boundary march, separation-criterion hook;
S1 monitor = closed-form boundary function
val = [Lam·B·(A+B) - (A-B)]/[1 + Lam·(A+B)], A = tan(theta-alpha),
B = tan(alpha), Lam = V dalpha/dV (gamma-free); unit processes O(h^2).
VI.3 Per-phase gradient: closed-form adjoint where smooth (= f2
invariant + corner residuals: shroud/bell CSTR_PA
p_a = p - (1/2) rho V^2 sin(2theta) tan(alpha); plug CSTR_PB with +
sign — the sign from the CHARACTERISTIC TYPE); reverse-mode AD of the
fitted march elsewhere (implicit-function custom rules on inner
iterations, never unrolled; differentiate the fitted front, never a
captured smear). Certificates: dot-product to machine precision (O3);
Hoffman E-residual -> 0 along optimized contours.
VI.4 Cycle layer: locate switch phases xi*(Sigma) (separation onset,
adaptation, sheet-entry) by root-finding; SPLIT Gauss panels there
(else O(1/N) + noisy outer gradient — the practical convergence trap);
Leibniz terms cancel by continuity of F (verified).
VI.5 Optimizer: TR-SQP on spline DOFs; gradients Riesz-represented in
a Sobolev/Steklov-Poincare metric (mesh-independence); active-set
constraints {L, eps_max, lip, truncation} with multipliers reported as
MARGINAL VALUES; bundle safeguard near persistent kinks; deflated
continuation for stationary-point enumeration; sector tournament for
topology; seeds: Rao-at-<Pc> (bell), peak design (plug) — provably
near-optimal for weak violations (P6), never affecting the certified
result (a-posteriori certification).
VI.6 Certificate stack per Verdict: KKT + (**') residuals; reduced-
Hessian spectrum; dual-route agreement (B1 NLP vs B2 collocation of the
optimality system); ORACLES (O1: T3-family in ⇒ Rao-at-<Pc> out with
Delta-Isp = 0; O2: ideal plug ⇒ peak design; O3 dot-product; O4
freezing-adjoint dOmega/dSigma vs FD of continued waves; O5 unsteady
sim vs J_avg + St·J1); DWR discretization bars; bound-ladder gap +
globality mechanism; O(St) and D2 physical bars; data provenance +
margins. NOTHING SHIPS OUTSIDE A VERDICT.
VI.7 Tooling: JAX (custom_vjp + implicit rules) or Julia/Enzyme;
GENO-Fortran as independent reference (dual-code); Newton-Krylov +
Arnoldi for the anchor; implicit shock tracking (HOIST class) for
wave-frame solves; known GENO prerequisites: RaoPlug S1/S2 fix (mass
multiplier + 2nd DOF) gated by the Rao-1961 spike Table-1 oracle
(M_E = 2.4, theta_E = -8.25 deg, gamma = 1.23 -> eps = 3.81,
X_D/R_E = 1.164, C_F = 1.58).

==============================================================================
PART VII — DOCUMENT MAP, PHASES, THESIS

Deliverables of record (depth per topic):
 D1 `rde_nozzle_problem_book.md` — definitions, interface contract +
    sonic-start + mixed-interface decision tree, hypothesis ledger.
 D2 `rde_nozzle_literature_map.md` — 17-gap analysis, six strands +
    in-house classical corpus (b0), all citations verified/flagged.
 D3 `rde_nozzle_theorem_ledger.md` — per-claim rigor classes,
    corrections of record, method upgrades (bounds, Gamma-convergence,
    DWR, shock tracking), global-optimality program, configuration-free
    total optimum.
 D4 `rde_nozzle_claims_verdict.md` — what survived/fell/weakened;
    ranked open problems OP-0..OP-11; repo actions.
 D5 `rde_nozzle_general_scheme_panel.md` — 16-agent panel scheme for
    the general (non-steadifiable) problem + prescribed-profile
    convergent pipeline (Annex A).
 D6 `rde_nozzle_development_plan.md` — certainty model C1-C4, phases
    A0-A7, tool matrix, gates G0-G6, 90 days, input taxonomy (Annex B).
 D7 `rde_nozzle_pipeline_audit.md` — per-step triple verdict, declared
    residues R1-R10, errors found-and-fixed E1-E7, decision matrix.
Work phases (operational plan): Fase 0 consolidation -> Fase 1
quasi-1D foundations (bound ladder OP-0, phase diagram OP-11-eps, paper
P-1) -> Fase 2 differentiable engine (gate G0, milestone M1, RaoPlug
fix) -> Fase 3 cycle layer + first science (gates G1 ORACLES-FIRST and
G2 value-by-bound-gap; papers P-2 fast-track, P-3) -> Fase 4 O(St)
license (G3) + wave-frame anchor (G4; papers P-4, P-5) -> Fase 5
robust/coupled/tool. Thesis mapping: Ch.1-2 = Parts I-III; Ch.3 =
Fase 1; Ch.4 = Fasi 2-3; Ch.5 = Fase 4A; Ch.6 = Fase 4B; Ch.7 =
horizon (OP list). External standing gates: G5 (Kraiko/PMM pass before
any submission). RESOLVED 2026-07-16: the weak-strong measure-valued
citation is VERIFIED (Brenier-De Lellis-Székelyhidi, CMP 305:351-361
(2011), doi:10.1007/s00220-011-1267-0) — with the Lipschitz caveat now
incorporated in D2.5 (canonicity conditional across shocks).
Target venue of record for P-1/P-3 (methodological + first results):
JPP class (Journal of Propulsion and Power), with the mathematics
papers (P-4/P-5) aimed at applied-mathematics venues.
