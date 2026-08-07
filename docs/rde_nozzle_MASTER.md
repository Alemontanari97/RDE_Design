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
[Legend extension of record, S14 (PAN-S14 F-CLASSES, dated
supersession per the S9 convention): THEOREM* = proof complete modulo
the conditional-entry IDs in the registry `inherits` field — declared
model closures (C-HT4/C-IGMIX/C-O33), numeric residuals, or the named
ANALYTIC conditionals (C-D25U/C-MAJDA); the closure-conditional vs
analysis-conditional distinction lives in the L4 ledger
(docs/rde_nozzle_conditionals.md). "THEOREM* at statement level" is
sanctioned usage when the remaining analysis is itself a registered
conditional (instance: S-P4F with C-P4RZ).]

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

[D-DOM] D2.1 (Domain and constraint). Reactive compressible Euler (viscous
closure = declared model layer) in Omega(S) = E \ S, E an envelope
cylinder downstream of the annulus, S the SOLID SET (design variable)
with attachment at the chamber lip(s) and uniform cone condition.
Configurations (bell / plug / shrouded / E-D / ...) are the topology
sectors of S — outputs, not inputs. Working class A: spline manifolds
in uniform C^{1,1} per sector.

[D-JEX] D2.2 (Exact objective). J_exact[S] = lim_{T->inf} (1/T) Int_0^T F_S(t)dt,
F_S(t) = Int_S [rho u_x (u.n) + (p - Pa) n_x] dA on any enclosing
axisymmetric control surface; requires an attractor with invariant
measure (statistical stationarity — the weakest standing hypothesis)
and a solution concept (D2.5). Pa constant.
[S14 additions (PAN-S14 addendum, 2026-08-04; ME-1 + a-Jexact-fallback,
both team/arbiter-confirmed): (1) FALLBACK TARGET (definition): if no
invariant measure exists, the declared objects are J_exact^-/J_exact^+
[S] := liminf/limsup_{T->inf} (1/T) Int_0^T F_S(t)dt (always defined);
"only bounds ship" means certified brackets of [J_exact^-, J_exact^+],
collapsing to J_exact under the standing hypothesis. (2) SCOPE
DISCHARGE: within the declared periodic scope the hypothesis
discharges exactly (D3 remark (1), "no Birkhoff limits"); outside it
the OBSERVABLE failure channel is running-average non-convergence /
realization dependence — not the non-existence of an invariant
measure, which is non-exhibitable (Krylov-Bogolyubov where "attractor"
is well-posed). The D-JEX falsifier is re-pointed accordingly.
(3) WORDING NOTE, dated 2026-08-05 (PAN-S14 §8 residue PP-3,
second-lens verified): 'attractor with invariant measure' =>
realized-orbit stationarity additionally presumes the invariant
measure is the PHYSICAL (SRB-type) one for the observed data — a
DECLARED hypothesis, not a theorem; 'weakest standing hypothesis'
reads 'weakest DECLARED hypothesis', operationally subsumed by the
running-average monitor of (2).
(4) UPPER WALL, dated 2026-08-06 (S16, [S-GBE]): the fallback targets
now carry a certified geometry-free upper wall — J_exact^+ <=
F_env(mean interface fluxes) under bounded storage + axially-sonic
exhaust + admissibility (docs/rde_nozzle_GB_ergodic.md): the "only
bounds ship" clause has its bound.]

[D-MU] D2.3 (Operating measure and averaged objective). mu = pushforward of
normalized cycle time under t -> xi; averaged (rung-2) objective
J[Sigma] = Int F[Sigma; s(xi)] dmu(xi), with F the steady per-state
thrust (wall form or Rao control-surface form; equal by the momentum
theorem in the S1 class).
[Scope note, dated 2026-08-05 (PAN-S14 §8 residue ME-2, second-lens
verified): mu and the rung-2 integrand are declared WITHIN the
standing pure-periodic single-mode scope (fixed wave count n;
monitor = T0 flatness, VI.4bis): a phase containing a MODE
TRANSITION (n changes) has no steady per-state F and is OUTSIDE
this definition — it violates H-A1 (D1 §9) and is routed to the
robust layer (VI.4bis(v), A6/PB-5), never silently averaged.]

[D-CONTRACT] D2.4 (Design interface Gamma_d). A fixed axisymmetric surface
downstream of all heat release carrying the data family s(xi); the
CONTRACT is (Gamma_d, data class, validity): R1 causal separation;
R2 well-posed data (full state only on axially supersonic patches —
see L4; subsonic patches: incoming invariants + impedance closure or
choking closure, decision tree in D1 §4.3bis); R3 measurability.
Idealization ladder: I0 coupled bilevel / I1 wave-frame steady field /
I2 per-phase meridional profiles / I3 sonic family (P0,T0)(xi) /
I4 single mean state.
[L4-DEFAULT OF RECORD, dated 2026-08-06 (S16 [RIGOR/B], ledger pass 2
[PAP-D9HL] §4 items 1-2): the certified interface DEFAULT is the L4
class — every patch of Gamma_d axially supersonic with margin. On
the default: mdot-independence is EXACT ([T-TH0] L4 note, no choking
assumption) and mean upstream influence is EXCLUDED BY THEOREM
([T-NSW]) — the former hypotheses H2/H-I2 are DISCHARGED there.
Subsonic patches remain admissible as a DECLARED CASE-CLASS (D1
§4.3bis options O1-O4) whose closures carry H2/H-I2 as class
assumptions with the existing monitors (choking margin, R2
characteristic-direction audit) and the documented Verdict
downgrades. This names the class the certified apparatus already
lives on (the u_x - c >= delta margin is the standing certificate);
no theorem's scope changes.]

[D-S1] D2.5 (Solution classes). S1: piecewise-smooth MOC-regular (finitely
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
DECLARED conditional (backed by Majda stability of the fitted fronts [C-MAJDA]),
not a theorem — ledger-grade honesty, consistent with the panel's
refutation of relative-entropy certificates for shocked orbits.
[BVP-NATIVE UPGRADE, dated 2026-08-05 (S15 [RIGOR/A], [T-XWS]
docs/rde_nozzle_cauchy_bvp_transfer.md, carrier X-XBVP): the
shock-free weak-strong citation above is TIME-formulation (its Cauchy
datum = the whole field at t = 0, which presupposes the solution);
the transfer to the steady BVP is now WRITTEN — relative entropy in
x-as-time with the pair (-rho u g(S), -rho v g(S)): sonic bijection
[T-XSON] (THEOREM, abstract EOS), slip-wall relative-entropy flux
annihilation [T-XWALL] (THEOREM, abstract EOS, every g: the slip flux
perturbation is isentropic at constant mass flux), convexity from the
AXIAL margin [S-XCONV] (SCHEMA, instance-certified; sonic line =
exact definiteness boundary), assembling to weak-strong uniqueness on
the BVP [T-XWS] (THEOREM* inheriting [C-XBVP](a,b), ledger §1bis):
with a C^1 margin solution present, shocked alternatives on the same
inflow data are excluded BY THEOREM in the class. Canonicity across
fronts stays with C-MAJDA, now cleanly separated.]
[FRONT-CHAIN COMPLETION, dated 2026-08-06 (S16 [RIGOR/A],
[S-D25U-U34] docs/rde_nozzle_D25U_U3U4.md, carrier X-U3BD): the
C-D25U component -a estimate chain (U1 smooth + U2 wall + U3 front +
U4 composition) is now WRITTEN at whole-class level with the
Lipschitz constant explicit in the five-constant certificate; and
C-MAJDA is SHARPENED in-class to a single scalar condition (U3-H1:
the 1-D Lopatinskii-Schur scalar of the bordered front solve,
nonvanishing on the compact certified front set — instance-certified
s_L = 1.8685, uniformity by compactness once pointwise). Declared
inventory: same-front-topology stratum (cross-topology = census/RK-G
layer), wall-attachment reading (front count DERIVED from the
entropy budget), origination clause, genuine nonlinearity for the
entropy floor. Shift-C^1 of the map (-c/U5) untouched.]
[A-CONTRACTION ROUTE, dated 2026-08-06 (S16 T2, [S-ACFR] docs/
rde_nozzle_acontraction_attack.md, probe X-ACFR): the "shift/
a-contraction (Vasseur-Krupa line)" partial support named above is
now TRANSPLANTED to the x-as-time BVP frame as a named route:
extremal fronts only (structural), walls free by T-XWALL, shift =
the fitted-front dof, entropy family -rho u g(S) on the certified
convexity box (CONFINEMENT CLAUSE load-bearing). The front
obstruction reduces to a balance-set condition, INSTANCE-FEASIBLE at
the certified oracle with weight window r = a_-/a_+ ~ [3.2, 47]
(probe, not certificate; reversed front infeasible for every r —
the condition discriminates). Route ADOPTED-AS-NAMED, completion
gated on bricks B1-B3 (interval certification over K_delta;
assembly; g-scan). No C-MAJDA discharge claimed.] S2:
entropy weak — non-unique in multi-D (convex integration), never used
as a constraint. S3: statistical — roof definition only.

[D-P] D2.6 (THE PROBLEM OF RECORD (P) — canonical fusion of Part II + Part IV).
GIVEN: envelope E (axisymmetric, L_E, R_E), attachment set Λ, constant
Pa > 0; interface contract (Gamma_d, D, mu) with the stage-A admission
audits passed (characteristic completeness on axially supersonic
patches per Lemma 4; Crocco compatibility; per-phase spacelikeness
margin; declared closure O1/O2/O3 on subsonic patches); constraint
vector c = (L, eps_max, L_p, curvature/angle bounds, symmetry class).
[PROXY NOTE, dated 2026-08-05 (PAN-S14 §8 residue PP-4, second-lens
verified): industrial heat-load and mass constraints enter (P) at
rung 2 ONLY through these geometric c-slots as declared PROXIES
(L/L_p/eps_max bound wetted length and size); no flux-level thermal
or mass model is a c-slot today — declared upgrade path: a dedicated
c-slot with its own multiplier, same pattern as the side-load CVaR
disposition below.]
[SIDE-LOAD DISPOSITION, dated 2026-08-05 (S15, [T-SLRW]): the rotating
side load is a DECLARED SECONDARY OUTPUT, not a c-slot — inside the
certified n >= 2 pure-periodic scope it is zero BY THEOREM (a slot
would carry a structurally-zero multiplier), and the m = 1 wall trace
lives in the D2 azimuthal residual channel that rung-2 states cannot
evaluate; data-level impurity metric rides the T0 flatness monitor's
m = 1 line; declared upgrade path to a CVaR c-slot at the A6 robust
layer (mode transitions) — full grounds in
docs/rde_nozzle_side_load.md §4.]
PER-PHASE STATE CONSTRAINT (addendum 2026-07-21, S12, [D-GSEP]):
the constraint set also carries the separation-margin state
constraint g_sep(S; s(xi)) <= 0 for mu-a.e. xi (criterion class R2,
declared empirical closure; runtime detector = the S1 boundary-
function monitor): certified optima keep EVERY phase attached, the
active-set multiplier is the marginal value of the attachment
margin, and the temporal dual-bell question (N1) becomes a decidable
active-set question at rung 2; deliberately separated designs exit
the certified class (separation reopens the subsonic feedback
channel and carries its own non-rotating dynamics — out of the
single-mode scope by physics, not only by declaration).
[Alignment note, dated 2026-08-05 (PAN-S14 §8 residue ME-4,
second-lens verified): the reading of record is mu-a.e. — 'every
phase' means every xi up to a mu-null set; the readings coincide on
the atomic/empirical measures and quadrature nodes actually audited
(mu-hypotheses of Lemma 2 / T-O2, ME-3), and the D-GSEP falsifier's
'any phase' is read on supp(mu) accordingly.]
ADMISSIBLE SET: A_gen(c) = {S ⊂ E compact solid: uniform cone condition
(h0, omega); attachment on Λ; g_i(S) <= c_i}, with its FINITE topology-
sector decomposition (configurations = outputs) and working spline
class A_h per sector.
[ATTACHMENT-QUANTIFIER PIN PENDING, dated 2026-08-05 (D8 §8 residue
s1, second lens): the clause 'attachment on Λ' (and D2.1's
'attachment at the chamber lip(s)') does not fix the quantifier over
connected components — permissive (only lip-touching components
constrained; detached D-family admissible) vs strict (every component
anchored) is undecidable from the present text: census advisory open
point O1, sibling carrier question O9
(validation/PANEL_topology_census_2026-07-22.md §7, ADVISORY). USER
PIN + census-lemma session required (PROGRESS NEXT: "decisioni A_gen
(utente)"); until pinned, no sector-count or D-family claim may
silently assume a reading.]
[PINS SINCE DECIDED — note added 2026-08-06: the census thread closed
with ALL pins decided 2026-08-02 (advisory §7pin + memory bridge
topology-census-pins): CEN-O1 = PERMISSIVE (bare annulus in;
detached members via anchor classes/strut bands/tournament filter).
The D2.1/D2.6 amendments the pins imply are QUEUED to the
census-lemma rigor session (after brick 2, census sequencing) — this
note is a state pointer, not the amendment.]
[SECTOR-FINITENESS STATUS, dated 2026-08-05 (D8 §8 residue s6,
second lens): "FINITE" here carries NO declared rigor class at this
site of record. Current grounds: problem book §5 sector decomposition
(SCHEMA) + the two-clause counting theorem of the census advisory
(THEOREM-sketch, conditional on O1/O2/O3/O9;
validation/PANEL_topology_census_2026-07-22.md §3 — ADVISORY, not of
record). Class label + proof owed to the census-lemma session
(global-maximum dossier Card 4; PROGRESS NEXT).]
[SINCE 2026-08-06: the counting theorem's pin-conditionals are now
DECIDED (census §7pin, 2026-08-02): O1 permissive, O10 NONBLOCK+,
O11 lip circles; the old O2/O9 are DISSOLVED by the Omega-side
Chenais cone-carrier pin. Headline of the advisory: the classical
taxonomy collapses to ONE clopen sector S0 + the detached family
D(m,n); P(h)/BR empty. Still ADVISORY until the census-lemma session
promotes it (ratification = user lock).]
STATE (mu-a.e. xi): the unique S1 solution U_xi of steady Euler in
E \ S with data s(xi), slip walls, supersonic outflow; S1 membership
certified a posteriori (boundary-function margin >= delta_S1 > 0
uniformly in xi); canonicity per D2.5 (exact shock-free, declared
conditional across fronts).
OBJECTIVE: J[S] = Int_Xi F[S; s(xi)] dmu(xi), legitimacy chain
Theorem 0 -> T0 -> P4.
PROBLEM (P): find the PAIR (S*, delta) such that
 (i)   S* ∈ argmax_{A_h(c)} J (existence; P7 = function-class target
       with monitored failure boundary);
 (ii)  S* satisfies the averaged system T7: per-phase closed-form
       adjoint (Rao/Kraiko) conditions + mu-averaged wall condition +
       WEIGHTED transversality (**') + active-constraint
       complementarity with multipliers = marginal values;
 (iii) reduced Hessian ⪯ 0 on the active tangent cone;
 (iv)  GLOBALITY, certified: a declared mechanism M1-M5 delivering
       J[S*] >= sup_{A_gen(c)} J - delta with delta COMPUTED
       (delta = B - J[S*], B = min of the bound ladder: int-max,
       sonic-capped J_ideal, B_EK), and delta = 0 PROVEN in the
       structured classes (M1 duality-gap zero: T4, numerically
       attained on the supercritical rows; M2 pointwise T3 transfer —
       valid for EVERY S in the sector, not only stationary ones;
       M3 unimodality: the 1-DOF theorems);
 (v)   declared bars: |J_exact - J[S*]| <= St|J1| + D2 residual + DWR.
[BAR-CLASS NOTE, dated 2026-08-05 (PAN-S14 §8 residue PP-5,
second-lens verified): the (v) bars are ESTIMATED/ASYMPTOTIC
indicators — St|J1| is the first-order [J-CT1] term (it does not by
itself bound the remainder, T3QS §3 B3) and DWR is an estimate —
NOT certified bounds; certified brackets ship only via the D2.2
fallback targets [J_exact^-, J_exact^+].]
"Search for the global optimum of the defined problem" = compute
(S*, delta) with the least available delta; "global optimum PROVEN"
<=> delta = 0.
MAXIMALITY (why this is the strongest truthful form): (a) no
admissible-set-free version exists (vacuum theorem: sup unattained —
the Pa -> 0 limiting instance, outside (P)'s Pa > 0 GIVEN; at Pa > 0
the class is needed for existence itself: uniform cone condition +
envelope compactness, the P7/Chenais route of Part IV [anchor
corrected S14, PAN-S14 addendum, arbiter-confirmed]);
(b) no solution-concept-free version exists (multi-D non-uniqueness);
(c) unconditional global optimality on nonconvex infinite-dimensional
shape sets with PDE constraints exists for NO ONE (J non-concave —
deflation can exhibit multiple stationary contours; no convexification
known; G13/G17 verified open) — the certified-(S*, delta) form is
maximal w.r.t. the provable state of the art, achieves delta = 0
exactly where structure exists (T3/T4/unimodal), and is designed to
absorb future progress on the named residues (R5-R8, G12) without
changing form.

==============================================================================
PART III — THEOREMS WITH PROOFS

------------------------------------------------------------------------------
[T-TH0] THEOREM 0 (the definition chain of RDE thrust — why the phase integral
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
T3-QS SWEEP-PROTECTION REMARK (2026-07-21, S12, [T-T3QS]; carrier
X-T3QS, suite group (xvi); full statement docs/rde_nozzle_T3QS.md):
within the P4 first-order framework, on a T3 RAY family (Pc-only
cycles; EOS-general) the first-order term of the quasi-steady error
VANISHES on the smooth part of the cycle — flux Jacobians and the
thrust-adjoint source are invariant along the conservative ray, so
the sweep acts as a pure phase shift and the mean is unchanged; the
entire first-order correction concentrates at the wave-passage jump
(the physics the fitted inherited sheet represents), and off-ray
cycles contribute a computable AREA (hysteresis) term. The collapse
class is thus SECOND-ORDER protected ON SMOOTH RAY CYCLES; on the
canonical blowdown sawtooth (T-O2) the first-order residue
<psi_hat, Z>[k]_jump is jump-localized, and its absorption by the
fitted inherited sheet is the pre-registered O5 prediction P-ii
(conjectural until measured) [status restatement S14, PAN-S14
F-T3QSHEAD] — the quantitative reason the
field's quasi-steady practice outperforms naive St estimates. This
remark does not weaken the paragraph above: the storage bookkeeping
is untouched; T3-QS refines the FLUX-factorization error only.

------------------------------------------------------------------------------
[T-O1] PROPOSITION 1 (O1 — objective equivalence at frozen choked feed). THEOREM.
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
[T-O2] LEMMA 2 (O2 — log-uniform measure). THEOREM.
For the exponential blowdown Pc(xi) = P_CJ · PR^(-xi), xi ~ U[0,1):
xi = -ln(Pc/P_CJ)/ln PR, so dmu_P = dPc/(Pc ln PR) on [P_CJ/PR, P_CJ]:
the engine's canonical operating measure is LOG-UNIFORM in pressure.
QED. (Any measured cycle simply replaces mu_P; the theory is
measure-agnostic WITHIN the declared mu-hypotheses [scope note S14,
PAN-S14 addendum ME-3]: mu a probability measure; the mu-a.e. audits;
switch phases mu-NULL (T7 standing hypothesis) — the last must be
RE-VERIFIED for every imported measure, trivially but obligatorily
for ATOMIC/empirical measures, which can charge a switch phase; for
atomic mu the cycle quadrature becomes the exact weighted sum, not
Gauss panels.)

------------------------------------------------------------------------------
[T-T0] THEOREM 3 (T0 — wave-frame exactness, strengthened). THEOREM.
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
transfer Rao's 2-D closed-form machinery to 3-D swirl (N6). N6 STATUS
UPGRADE (2026-07-16, [F1/N6-S1], docs/rde_nozzle_N6_swirl.md +
machine-verified carrier): the boundary is now THEOREM-grade SHARP —
(i) the swirl STRUCTURE theorems hold (meridional Mach lines
unchanged, swirl = triple streamline transport, kernel laws
identical: N6-1 [T-N6-1], symbolic-sufficient); (ii) Rao's machinery DOES
extend verbatim to FREE-VORTEX swirl (uniform r·u_theta, h0, s) with
W = meridional speed (N6-2 [T-N6-2], THEOREM); (iii) beyond free vortex the
pointwise control-surface closure fails by an exact obstruction
identity (N6-3 [T-N6-3]) — field-level (five-field/AD) machinery NECESSARY;
the five-field optimality system is the named SCHEMA [S-5F].
TRANSVERSE COMPANION (added 2026-08-05, S15 [RIGOR/A], [T-SLRW]
docs/rde_nozzle_side_load.md, carrier X-SLRW in suite group (xiii)):
T0 classifies the AXIAL line (m = 0: constant in t); the rotating
side-load lemma classifies the TRANSVERSE lines — the transverse
force/moment resultants on any surface of revolution read ONLY the
m = 1 azimuthal harmonic of the trace (kinematic proof, no EOS, jumps
admitted), so n >= 2 identical equally-spaced co-rotating waves give
IDENTICALLY ZERO transverse load density (every station, every
instant: no side force, no shear, no bending), while n = 1 gives a
constant-modulus vector rotating rigidly at Omega (zero mean, but
undiminished magnitude — bearing duty, never "averages away");
pressure exerts NO axial torque on a surface of revolution (M_x == 0,
only shear can torque the wall). Together the two lemmas classify all
six rigid-load resultants of a rotating pattern. Breakage channels
(counter-rotating admixture, unequal waves, mode transitions) are the
T0-flatness impurity channels — a measured side load on a nominally
n >= 2 engine is a mode-impurity detector with a theorem behind it.

------------------------------------------------------------------------------
[T-NSW] LEMMA 4 (N-SW — spacelikeness is frame-invariant; the swirl audit). THEOREM.
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
[T-T3] THEOREM 5 (T3 — the collapse, fixed wall). THEOREM.
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
the linearity) [PRECEDENT DUTY, 2026-07-22 S13: the trajectory-
averaged variational instance is Kraiko-Osipov PMM 34(6) 1970,
page-verified; see the T7 precedent note; mandatory citation]; (C3) oracle O1: any ensemble machinery run under
H1-H4 MUST return Rao-at-<Pc> with Delta-Isp = 0.
Sharpness [T-T3-CE]: two-phase two-gamma counterexample — J = (1/2)[a(g1)Pc1 +
a(g2)Pc2] - Pa b is not of the collapsed form; first-order closure
gamma_eff = <Pc gamma>/<Pc> (~ gamma_CJ under blowdown weighting: the
S-H freeze-at-CJ choice retro-justified); design penalty second order
(envelope theorem). For genuinely reacting gas the closed-form corner
DIES (Hoffman 1967 Eq. 78: multiplier-field condition E = 0 replaces
it) — the N4 ladder: frozen ⊂ gamma(T) (fails in principle, small in
practice, E4 oracle pending) ⊂ finite-rate (adjoint-level mandatory).

------------------------------------------------------------------------------
[T-T4] THEOREM 6 (T4 — plug simultaneous optimizability). THEOREM* (under the
ideal-adaptation closure [C-HT4]: wall pressure clamps to Pa downstream of each
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
caveat (page-verified, S14 PAN-S14 F-PB2FIRST): Kraiko-Osipov PMM
34(6) 1970 already poses TIME-AVERAGED endpoint conditions for a
length-capped nozzle with base pressure on the end face (their (1.4)
and (3.2) cont., transl. pp. 1007-1008; (4.4), p. 1011) — trajectory
measure in place of the cycle measure; "first" is program-internal
wording: first CYCLE-averaged instance for the RDE plug, not first
averaged shape problem tout court; K-O 1970 mandatory citation here
too (cross-ref the T7 precedent note). Precedent
duty: the ideal-adaptation closure is published as a BOUND for
detonation cycles (Kraiko-Egoryan) — cite next to the closure.

------------------------------------------------------------------------------
[T-GB] PROPOSITION 7 (G-B — geometry-free upper bound) and COROLLARY (global
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
GAMMA-PURGE INSTANCE OF RECORD (2026-07-16, [F1/OP-0-gamma], session
S6; src/thrust/bounds_gamma.py + tests group (xi); strengthened
gamma directive). The ceiling's executable PRIMARY route is now
EOS-GENERAL: V_id = sqrt(2[h0 - h(s, Pa)]) and the sonic cap evaluated
on the Cantera frozen-CJ-products isentrope (frozen-composition
gamma(T) rung of the N4 ladder; cap located exactly by inverting the
monotone w(P) = h + c^2/2 at w(P*) = h0), with the closed forms of
this proposition DEMOTED to declared oracles. The cap criterion is
executably RE-VERIFIED at gamma(T): a scan of all admissible exits
never beats the capped formula (within measured table-noise bars),
and on the four subcritical Table-1 rows the naive uncapped form
strictly LOSES at the deepest subcritical phase — the g = 1.15
counterexample generalized beyond calorically perfect gas. Known-
answer rejector: a constant-cp synthetic gas through the same route
reproduces the closed forms to 4.7e-7 (derived tol 1e-6) and a
corrupted route is rejected. MEASURED PURGE DELTA of record: on the
12 finite-Pa rows the real gamma(T) ceiling sits 4.4-7.9% BELOW the
frozen-gamma_s closed-form oracle (bars ~0.002%, all significant) —
the price of the caloric idealization at ceiling level, now a number
with a rejector instead of a hypothesis. Vacuum rows: T-floor (200 K)
truncated LOWER-BOUND instruments, declared. Residual (declared S7):
DISCHARGED 2026-07-17 (session S8 operativa, [F1/OP-0-gamma tail]) by
the REAL-ROUTE DIAGRAM INSTANCE below and its equilibrium bracket.
REAL-ROUTE DIAGRAM INSTANCE OF RECORD (2026-07-17, [F1/OP-0-gamma
tail], session S8; src/thrust/phase_diagram_real.py + tests group
(xii) + data/phase_diagram_real.{json,md}). The OP-11-eps phase
diagram itself is now re-derived on the EOS-general primary route
(same 90-cell grid, same anchor; closed forms NOWHERE in the primary
computations): (i) the executable quasi-1D reduction of T7 (b)-(c)
acquires its first EOS-GENERAL carrier — eps* solves the weighted
condition <P_E(eps; xi)>_mu = Pa by inverting the REAL area-ratio map
per phase (the closed form NPR(eps*) = <Pc>/Pa is demoted to its
gamma = const oracle); real eps* = 3.49-3.52 across the grid vs the
oracle's value at gamma_s (numbers of record in the JSON); (ii) the
real adaptation knee sits BELOW the closed-form knee (10.38 vs ~12.9
at PR = 90 — the caloric idealization overestimates the envelope the
peak design needs, of record with bars); (iii) the map STRUCTURE is
CONFIRMED at gamma(T): tie column at PR = 1, capped band, no bell
cell, M1 attainment at eps_max >= knee_real on all 41 knee-fitting
cells INCLUDING the 11 subcritical ones — the M1 duality-gap-zero
extension is now certified EOS-GENERALLY, not only in closed forms;
(iv) the naive-adaptation instrument never beats the cap and loses
STRICTLY beyond the bar at the deepest-spread cells (two-level metric,
PR = 90 gap 1.9e-2 s vs bar 1.4e-2 s) — the subcritical artifact
generalized to the diagram level. EQUILIBRIUM BRACKET [T-EQBR] of record (same
instance): the shifting-equilibrium ceiling (SP-equilibrate isentrope,
Gibbs solver; eq sound speed from c^2 = dP/drho along the table)
sits +6.3..+7.0% ABOVE the frozen ceiling on every PR (bars <= 0.003
s; constant-cp known-answer through the eq machinery PASS, corrupted
route rejected): the pair [frozen, equilibrium] is the executable
MODEL BRACKET of the caloric closure at ceiling level (THEOREM*
within the ideal-gas mixture closure pair [C-IGMIX]; the frozen rung of the N4
ladder now carries its upper companion). Winner semantics UNCHANGED
(closures, never hardware — D3 §10quater(5) applies verbatim to the
real-route diagram).
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
[M1-WITNESS ADMISSIBILITY, dated 2026-08-05 (D8 §8 residue s5, second
lens): the untruncated peak-designed plug closes on the axis; whether
an axis-closing tip satisfies the uniform cone condition (h0, omega)
of A_gen is the unpinned census question O2
(validation/PANEL_topology_census_2026-07-22.md §5/§7, ADVISORY: full
spike in-class iff O2 resolves tip-admissible, else a
class-boundary/ceiling object). This corollary is hereby
O2-CONDITIONAL as an IN-CLASS attainment statement; as a bound
statement (ideal-as-bound discipline) it is unaffected. Pin owed to
the census-lemma session.]
[SINCE 2026-08-06: the O2 question is DISSOLVED at pin level — the
Omega-side Chenais cone-carrier pin (census §7pin, 2026-08-02)
places tangent tips / sharp TEs IN class: the full-spike M1 witness
is admissible under the pinned carrier. The in-record proof (cone
condition on the fluid side at an axis-closing tip) lands with the
census-lemma session; until then the attainment statement is
pin-decided, record-proof pending.]
[T-OP11e] EPS-LEVEL INSTANCE OF RECORD (2026-07-16, [F1/OP-11-eps];
src/thrust/phase_diagram.py + rejector tests + data/phase_diagram.json
+ figs/phase_diagram_op11.png; full statement D3 §10quater). The OP-11
interpolation is COMPUTED AND CERTIFIED at the eps rung (90-cell
eps_max x PR grid at fixed <Pc>, blessed CH4/O2 anchor, OP-0 ladder
embedded per cell). Two THEOREM-grade additions: (i) under the
SONIC-CAPPED adaptation closure (this proposition's cap applied to the
T4/H-T4 closure) the plug family weakly dominates the fixed bell
POINTWISE — no strict bell region exists at eps level; (ii) at
eps_max >= knee the capped plug coincides pointwise with the per-phase
argmax and ATTAINS the capped ceiling: M1 gap-zero on every Pa > 0
cycle INCLUDING subcritical ones — the supercritical hypothesis is
needed only by the NAIVE closure, which loses strictly on subcritical
tails and, at the sonic-annulus cap eps_max = 1, even inverts the
bell/plug ranking (executable artifact, test-rejected). Tie region
characterized: eps_max <= eps*(Pc_min) ⇒ the plug never releases and
equals the bell as a member (plus the PR = 1 column, T3, and the
vacuum no-optimum sweep, both asserted as oracles). Duty splitting is
not expressible with the single shared eps DOF: at contour level OP-11
remains CONJECTURE.
SCOPE (non-transfer to (P), D2.6 — remark of record, full form D3
§10quater(5)): the diagram's winners rank CLOSURES at equal eps_max,
not hardware sectors of the constrained problem; the released capped
plug IS the per-phase relaxation, so its dominance prices the
ADAPTATION PREMIUM and does not decide (P) — the topology of S*(c) is
the output of the finite sector tournament at the true constraint
vector c (not a priori {bell, plug, shrouded}), and bell-winning
regions of (P) are EXPECTED at contour level once truncation/base-
pressure/length losses bite. Each cell certifies toward (P) the
geometry-free PREMIUM_BOUND = Isp_ideal(capped) − Isp_bell (THEOREM,
up to the bell surrogate's C4 bar): any certified non-bell loss band
exceeding it closes that cell for the bell with delta-certificate per
D2.6(iv) — the tournament device that PB-2's empirical truncation
band will arm.

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
predate this theory; no circularity). The FULL-FIDELITY version of
this check, with phi re-optimized per column as they do, already
exists in-repo: the 18/18 Table-1 validation reproduces their JOINT
(phi, eps) optima via `phi_opt` (certified 0.01-lattice search with
strict-neighbor certificate and global unimodality scan — no closed
form exists in phi since Isp(phi) passes through Cantera equilibrium
states) × `bell_opt` (closed form). Formal placement of phi: an OUTER,
non-variational design parameter of the DATA GENERATOR — it moves the
family s(xi; phi) and the measure mu(phi), not Sigma; the joint problem
is NESTED, max_phi max_Sigma J, with T3/T4 valid at each fixed phi and
the outer loop certified by the lattice — not to be confused with the
bilevel PB-4 (shape-to-chamber feedback).
The formalization therefore EXPLAINS the paper's empirical
regularities (its three nozzle findings are corollaries, now checked
NUMERICALLY, not only structurally), CLOSES its two flagged gaps
(timescale license = Theorem 0 + P4; fair-metric question = the bound
ladder), and inherits its comparison protocol (equal cycle mass +
throat area) as the frozen-family normalization. Together with the EAP
remark above, this is the second citable bridge for paper P-1 (target
venue: JPP class).

------------------------------------------------------------------------------
[T-T7FS] THEOREM-SCHEMA 8 (T7/T2 — the averaged stationarity system). SCHEMA.
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
TRAJECTORY-AVERAGED PRECEDENT (page-verified 2026-07-22, S13):
Kraiko-Osipov PMM 34(6):1067-1075 (1970) derive, for the TRAJECTORY
instance of this structure (aircraft flight conditions in place of
the cycle), the time-integrated weighted wall condition (their
(3.2), weight = trajectory-adjoint W(t)), multiplier fields on the
flow characteristics with jump relations, and the collapse of the
averaged conditions to the classical single-state family with
time-averaged weight under invariant dimensionless inlet (their §§4-5:
§4 = the averaged-weight collapse under inlet similarity; §5, transl.
p. 1012, = the degenerate second case — plane "short" nozzle, uniform
supersonic inlet, straight generatrix — where the FIRST of their
conditions (3.2) holds at every instant: stationarity-level partial
ancestor of T4's simultaneous-optimality mechanism [S14, PAN-S14
F-KO5])
— the 1970 ancestor of (b), of the weighted structure of (c), and
of T3's averaged-family reading. Not present there: the cycle
measure, exactness (T0), the priced O(St) step, the sharpened
pointwise collapse with proven boundary, certificates, and the
adjoint identification of P-2. Mandatory citation.
Non-smoothness: topology-switch phases are mu-measure-zero with F
continuous across them: Leibniz survives moving switches (boundary
terms cancel); persistent kinks: Clarke subdifferentials.
Named rigor gaps: [T-P3] P3 (lambda2 in L^2(dmu)) — UPGRADED 2026-07-16:
THEOREM* [C-D25U] in the shock-free S1 class (lambda2(xi) = -f2(lip data),
unique by scalar CQ, measurable + L^inf by margins; proof of record
docs/rde_nozzle_P3_multipliers.md; residues R-P3.1/R-P3.2 named
there; across fitted shocks it inherits the D2.5 conditional [C-MAJDA]);
T7 ITSELF UPGRADED same day ([F1/T7-FS],
docs/rde_nozzle_T7_P7_functionspace.md §1): differentiation under the
cycle integral is now THEOREM* — per-phase derivatives exist
(classical + G12-S1), are measurable (P3 composition) and uniformly
dominated by the audited margins, so dJ = Int F' dmu and the wall
condition + (**') are genuine L^1(dmu) statements (conditionals
R-T7.1/2 named: the shared D2.5 uniform-estimate conditional [C-D25U]).
[T-P7S1] P7 EXISTENCE attacked same day (same doc §2, THEOREM*): argmax exists
on every margin-certified level set A_h^delta (finite-dim compactness
+ closed margins + continuity via R-P7.1 [C-D25U]); the monitored failure
boundary of record IS the boundary of those level sets;
[T-G12S1] G12 (multi-D fitted-shock shape derivative: theorem only in 1-D
[Bressan-Marson; Ulbrich]; quasi-1D design rigor [Cliff-Heinkenschloss-
Shenoy]; 2-D practice [Baeza et al.]) — ATTACKED 2026-07-16
([F1/G12-S1], docs/rde_nozzle_G12_S1.md): within the S1 marching
class the gap REDUCES to the 1-D-in-time theory via the x-as-time
reading (Lemma G12-L1, eigenstructure machine-verified EOS-general:
det A_p ∝ u^2(u^2-c^2), pencil factorization, Mach-line roots) plus
the front brick (Lemma G12-L2, machine-verified with rejectors:
linearized RH nonsingular strictly inside Lax, degeneration EXACTLY
at characteristic fronts = the Prop. A2 kernel law); THEOREM G12-S1
(THEOREM*, residues R-G12.1..3 named: D2.5-inherited regularity
conditional [C-D25U], shift-differentiability citation TO-VERIFY, mesh limit
= Lemma B clause with target now stated). Carrier:
validation/g12_shock_linearization.py, PASS with derived equilibrated
tolerances.
[T-T7RED] Executable reduction (verified in-repo): quasi-1D, only exit-area DOF:
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
| chaotic / mode-hopping | bounds + robust surrogates ONLY (shadowing refused: hypotheses fail across shocks) | honest refusal of certificates [S14 note, arbiter-confirmed: the ladder's upper wall (Prop. G-B) is PROVEN in the steady per-streamtube setting only — its transfer to the ergodic average [J_exact^-, J_exact^+] (targets per D2.2) is a NAMED MISSING LEMMA (Birkhoff + bounded momentum route) or the bound de-rates to SCHEMA on this row; cf. D5 Step 5(f) quasi-steady-only labeling] [RESOLVED 2026-08-06 (S16 T4, [S-GBE] docs/rde_nozzle_GB_ergodic.md, carrier X-GBE): the lemma is WRITTEN — under declared hypotheses (bounded storage; axially-sonic exhaust surface; admissibility) J_exact^+ <= F_env(mean interface fluxes), with the OP-0 sonic cap re-derived as the exact constrained sup (the axial margin is what makes a pointwise ceiling exist) and NO Birkhoff needed (finite-T Cesàro + bounded storage suffice — the named route was stronger than necessary). The upper wall's quasi-steady-only label is LIFTED; lower rungs (attainability) stay steady-setting; the ergodic wall is Jensen-looser than the per-phase wall where phases exist (gap reportable).] |
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
RUNG 3a-LITE (B-lite) — addendum of record (2026-07-21, S12,
[S-BLITE]): on the NOZZLE-ONLY domain with certified axial margin
u_x - c >= delta > 0 (interface data class I1, Omega an INPUT from
the data), Lemma 4's condition C2 is SATISFIED and the exact
wave-frame field is computable by 3-D helical SPACE-MARCHING (fitted
sheet as per-station unknown, Lax in the x-as-time reading = G12-L2)
at marching cost — no Newton-Krylov global solve, no camera, no
Omega eigenvalue; the adjoint lifts verbatim by Lemma B
(x-block-triangular march => reverse-AD = transposed sweep). B-lite
is the cheap exact meter of the rung-2 sweep/D2 residual; the FULL
anchor of this Part remains necessary exactly where the camera
enters (Omega as output, subsonic pockets, reaction, R10). Named
brick to verify first: the 3-D axial-flux eigenstructure
(G12-L1-3D, symbolic carrier candidate). "Marches nothing" (Lemma 4)
remains true for the camera-included anchor; B-lite is C2 exercised
in 3-D, not an exception to it.

==============================================================================
PART VI — IMPLEMENTATION FORMULATION (what the coder builds)

VI.1 CycleFamily (contract C1): {P0, T0, thermo handle gamma(.;xi) |
M_in(y;xi), theta_in(y;xi), s(y;xi), [vorticity]} + mu weights +
provenance + stage-A audit results (characteristic completeness; Crocco
residual; spacelikeness margin min(M_x - 1) per phase; H-I2/choking
margins; projection norm if applied; T0 flatness/harmonic-decay
certificate [S14 F-FLAT: carrier + derived threshold = plan item D6
§6.5-bis; field named here so the contract cannot ship without it]). Generators: matched-cycle (case
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
VI.4bis Algorithmic consequences of the standing scopings (2026-07-16,
S5/S6 directives; AMENDED same day on user clarification: the
periodicity assumption describes the EXPECTED DATA and sets theory
priorities — it must NOT condition the algorithm, which stays FULLY
GENERAL; periodic structure is EXPLOITED AT RUNTIME when certified,
never assumed structurally. The skeleton of VI.1-VI.7 is UNCHANGED —
these pin down choices inside it):
 (i)  QUADRATURE IN xi: the GENERAL rule of VI.4 (Gauss panels +
      mandatory switch-splits at xi*(Sigma)) is the baseline for
      arbitrary mu; WHEN the data are certified periodic and smooth
      (T0 flatness certificate + harmonic-decay audit) the layer MAY
      switch opportunistically to trapezoid-on-the-circle (spectral
      accuracy), still composed with the switch-splits. Data-driven
      selection, never a structural assumption.
 (ii) O(St) CORRECTOR: BOTH routes live in the pipeline — the general
      route (unsteady comparison, O5) always available; the steady
      sweep-perturbation solve on the wave-frame anchor (one
      linearized solve, C-T1 periodic re-scoping D3 §3) engaged WHEN
      T0 applies (certified single/k-wave mode). The cheap route is a
      licensed specialization, not a replacement.
 (iii) GAMMA DIRECTIVE (unconditional): thermo backend EOS-general
      (Cantera h(s,P) class) mandatory; the gamma=const corner<->eps
      bijection is FORBIDDEN as a solver step (enforce f2 = const
      actively; E4/G2 oracle gates any closed-form shortcut).
 (iv) ROTATIONAL DATA (unconditional): per-phase adjoint at the FIELD
      level (reverse-AD of the fitted march = discrete adjoint sweep,
      Lemma B); the two-field closed form (Prop. A3) serves as
      ORACLE/INITIALIZER only; cheap per-phase certificates: f2-drift
      and Hoffman-E residual along each phase's terminal
      characteristic, lambda2(xi) = -f2(lip data) as the closed-form
      multiplier initializer (P3 theorem).
 (v)  ROBUST LAYER (CVaR/DRO over the mode measure): PART OF THE
      GENERAL ARCHITECTURE, engaged whenever the data warrant it
      (multistability declared, or the flatness monitor rejects mode
      purity); idle — not absent — on certified-periodic data. The
      flatness monitor itself is mandatory in every data contract.

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

G0 DECISION AND DUAL-CODE EXERCISE OF RECORD (2026-07-17, [F2/G0],
session S10; work-layer, registry [DIR-G0]; D6 gate G0 = DECIDED):
the tool choice above is now DECIDED — JAX primary (custom_vjp +
implicit rules), Julia+Enzyme declared alternate, GENO-Fortran the
independent dual-code reference. The dual-code interop that this
section asserts is now EXERCISED, not deferred: GENO was built
(WSL gfortran 11.4.0, CMake, Cantera/Sundials/Tecio OFF, LAPACK from
the host conda env — GENO never modified/committed) and the TOC case
tocnoz regenerated; the design contour reproduces the committed
reference to 1e-10 (printed precision, toolchain-invariant), while the
full-precision field dumps differ only by the documented toolchain md5
convention (N-36) — same physics. The FLOWFIELD cross-code oracle
[X-GENOXC] certifies that GENO's Fortran MoC nodes satisfy OUR
EOS-general second-order axisymmetric (u,v) unit process within the
derived per-cell truncation band (100% of the clean supersonic core;
two negative controls reject) — i.e. the differentiable engine's cell
map and the Fortran reference discretize the SAME continuum. Full
decision dossier: docs/rde_nozzle_G0_decision.md. Consequence: Phase
A1 (differentiable per-phase engine) OPENS, with [X-GENOXC] as its
standing cross-code regression.

A1 BRICK 1 OF RECORD (2026-07-20/21, [F2/A1], session S11;
work-layer; registry [X-A1IM], standing directive [DIR-THERMOTAB]):
the PROFILE-GENERATION MACHINERY exists and is certified. The
assembled differentiable MoC march (validation/a1_ideal_march_jax.py)
GENERATES the ideal-nozzle contour end-to-end — Sauer IVL ->
characteristic fan -> circular-arc throat expansion (inverse-wall unit
process with GENO's chord-foot search and void-row bookkeeping,
wall-angle refinement to axis M = Me) -> uniform-exit region with the
WALL AS THE BOUNDING MASS-FLOW STREAMLINE — as the twin of GENO
nozzle_type 0, with every cell an implicit custom_vjp unit process
(implicit-function rule, never unrolled), so reverse-mode AD of the
assembled march IS the Lemma-B discrete adjoint sweep, executably.
Verdict of record (reduced case NI = 21, da = 0.5 deg, Ne = 41,
eps = 4, CH4/O2 frozen): generated contour vs the GENO WSL run inside
the derived two-resolution Richardson band at 62/62 samples with
max |dy| = 7.6e-9 (band 4.5e-3; median err/band 0.000) — agreement at
GENO's own predictor-corrector tolerance, far below truncation;
achieved Me twin-identical to 8.4e-9; O3.1 dot-product over the
ENTIRE march |<w,Jv> - <J^T w,v>| = 2.7e-10 vs derived tolerance
5.1e-8 (replay fidelity 1.6e-13); per-cell UNIT-CONSISTENT Newton
certification in z-space (2756 cells, worst step/tol 1.4e-2);
negative controls reject (corrupted source cannot reproduce GENO,
corrupted whole-march vjp breaks O3.1, corrupted thermo table and
corrupted gamma rejected). THERMO BACKEND PIN of record (standing
user directive S11, [DIR-THERMOTAB], strengthening VI.4bis(iii)):
JAX engines READ TABLES (the GENO backend-1 / ATLAS-FLINT model) —
the march consumes interpolated (h, s0, cp)(T) tables with derived
table-density floors; CANTERA is the SOLE PRODUCTION table generator
(the GENO NASA-polynomial generator is confined to declared
cross-code oracle instances; gamma = const tables only as declared
known-answer oracles). Consequence: DIR-G0's honest scope guard ("no
JAX-generated contour exists yet") is DISCHARGED for the ideal
(direct-march) nozzle type; the VARIATIONAL TOC brick — thrust
objective + {eps, L, lip} constraints with the (**')/corner
transversality imposed through the dJ/dSigma gradient, never a
hard-coded outer loop — is the NEXT A1 brick; the G0 loop-speed
falsifier stays armed (production-scale march not re-adjudicated).

A1 BRICK 2 OF RECORD (2026-08-06, [F2/A1], sessions S17-S18;
work-layer; registry [X-TOCV], policy [DIR-RKG]; logs S17 steps 4-11
+ S18 steps 3-7): the VARIATIONAL TOC ROAD EXISTS END-TO-END and is
certified. The specified-wall TOC march (design vector W = attachment
angle theta_B + clamped-spline wall nodes; arc-kernel geometry rtu/
rtd as fixed inputs, GENO-twin contract) is recorded adaptively with
per-cell Newton certification AND the per-cell AXIAL-MARGIN rejector
(u_x - c > floor — the x-as-time causality the L-DoD truncation
lemma requires; instance floor delta = min_margin(base)/K_RICH =
0.1202 m/s on the reduced twin case), replayed by the bucketed
whole-loop-jit production engine (bit-level equivalence to the
certified replay; O3.1 transpose identity = the Lemma-B guarantee,
executably), and optimized by scipy trust-constr under the RK-G
segmentation policy with measured Jacobi scaling + a measured full
Hessian at every segment base (freshly measured per stratum — no
curvature carry-over, DIR-RKG-conformant). VERDICT OF RECORD
(reduced twin case, C^1 quintic closure primary): from a 1.5%
PERTURBED start the optimizer RECOVERS AND EXCEEDS the
GENO-projected seed (J* = 2.7761688e+07, +1.06e+04) and reaches
in-stratum stationarity KKT = 7.745e-02 <= derived gtol 1.156e-01 —
the TRANSVERSALITY INSTANCE: the Rao optimality conditions REACHED
VIA THE GRADIENT, never imposed by an outer loop; the optimum
contour agrees with the INDEPENDENT classical route (GENO type-2
Mrao/eps bisection) at 91/91 samples inside the derived cross-code
band (GENO cross-resolution + spline-class representation +
reference-resampling terms, neighborhood-enveloped; max|dy| =
1.861e-03, median err/band 0.102), with the N3 wrong-design
discriminator firing. DECLARED GOVERNANCE RESIDUE: the T2
practicality falsifier FIRED on the twin case (121.6 s vs 35.9 s;
decomposition = curvature measurement + RK-G re-record cost, NOT
language throughput — T1 = 1.593 and T2a = 0.116 s vs 1.197 s both
PASS with margin) => G0 re-decision review queued per the D6 flip
clause; named levers for scale: second-order implicit rules (exact
Hessian-vector products), colored/sparse FD Hessians, benign-flip
refinement of DIR-RKG (each a declared future brick, none executed
silently). CONSEQUENCE: D6 item 9 CLOSES; **O3.3 IS UNLOCKED** (the
pre-registered bench protocol P2_outline §5, untouched, becomes
executable against this engine — P-2's numeric half).

O3.2/O3.3 CAMPAIGN OF RECORD (2026-08-06, [F1/P-2], session S19;
carriers [X-O32], [X-O33B]; full numbers and the honest residues in
P2_lemmaA §3.7 and the S19 log). Class of the campaign: PRACTICE
(measurement) — it discharges numeric conditionals, it does not by
itself move a rigor class.
 THE LOCUS, first, because the campaign got it wrong before it got it
right: Rao's control surface is the C+ through the lip traced BACK and
STOPPED AT THE KERNEL BOUNDARY (the last C- emitted by the fixed
throat arc), not the whole C+ down to the axis. Measured on the full
chain, f2 drifts 2.9e-01 and identification (ii) looks falsified;
measured on the classical surface it is constant to 9.5e-03. The wrong
number is recorded alongside the right one because it is the one a
reader repeating the experiment would otherwise reproduce.
 WHAT THE BENCH ESTABLISHED. (1) f2 = -lambda2 is constant along the
control surface for the S18 converged design (2665.38, drift 9.5e-03)
AND for GENO's own Rao contour marched by the same engine (2666.03,
drift 8.0e-03), the two Rao CONSTANTS agreeing to 2.4e-04 — an order
of magnitude inside either drift, so the residual is the instance's
discretization, common to both designs. (2) The adjoint compatibility
relation of the classical corpus cancels to 1.6e-04 (C+) and 2.3e-04
(C-) in the Prop. A3 gauge on our field, and saturates at exactly 1.0
with the wrong sign per family — the sharpest rejector in the bench.
(3) THE PRIMARY KILL CRITERION PASSED: on a feasible family around the
optimum the AD directional derivative and the classical Rao residual
vanish at the SAME design inside the derived bar. (4) The corner
identity of identification (iii), dJ/dy_lip = 2 pi y_E [p_E - (1/2)
rho W^2 sin(2 theta) tan(alpha)], holds to 6.6e-02 on the 8-node
design — MESH-INDEPENDENT — and to 2.0e-02 on a faithful Rao wall at
the same mesh, falling further under refinement there: an identity of
the CONTINUUM optimum, converging in both limits, NOT confirmed at a
Richardson band on a finite-dimensional instance. [C-O33] stays open
with its residual quantified and its dominant term identified as the
DESIGN CLASS.
 THE HONEST RESIDUES. (i) The adjoint's convergence EXPONENT is not
measurable on a refinement ladder: refinement cannot hold the march
topology fixed, which is exactly clause LB-c2 of [S-LBML]; a
fixed-topology experiment is owed. (ii) The ideal twin's rows are
capped IN PART by a mirrored GENO algorithmic constant (the
|M - Me| < 1e-5 exit test) acting as an accuracy FLOOR on the achieved
exit Mach — critical-list item 3, now measured rather than suspected.
Its PRE-DECLARED diagnostic ran (hypothesis and test committed before
any four-level rate existed): tightening the constant 100x collapses
|dMe| from 1.5e-05 to 1.1e-08 and makes it monotone, so the floor is
REAL; but the rows do NOT recover (primal dp_tot 2.12 -> 1.46, still
non-conclusive; adjoint still not usable), so the constant is
ATTRIBUTED as a floor and EXONERATED as the binding cause, leaving the
topology mechanism of (i) as the only candidate standing for the ideal
twin too. No band was amended in either direction. (iii) The
design class (8 uniformly spaced nodes, natural cubic spline) is
instance-tuned and is what limits the corner row; its discharge is an
adaptive error-driven knot construction, not more uniform nodes.
(iv) Two data defects of GENO's profile output, found while consuming
it: the exit wall point is emitted twice 3.8e-6 apart in x (poisons
any spline fit at the lip), and the ATTACHMENT angle is not the
maximum wall angle (16.90 deg vs a peak of 18.83 deg) — the S18 seed
recipe took the peak.

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
 D8 `rde_nozzle_panel_2026-07-22.md` — S14 convergence panel of record
    [PAN-S14]: 16 team verdicts (§5), workflow-1b addendum + R4-bis
    register + declared residue (§8). [row added 2026-08-05, S15,
    D8 §8 residue]
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
