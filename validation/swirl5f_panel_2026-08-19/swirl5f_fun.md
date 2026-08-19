# The functional identity "cycle-mean thrust = mu-integral of per-phase
# thrusts": exact half, approximation half, honest error magnitude,
# and the value-bound transfer
#
# Artifact of record for the next stage (S-FOUNDATIONS-C swirl-upgrade line).
# Written 2026-08-19 by the derivation subagent; NO repo file modified.
# Discipline: every claim carries exactly one label from
# {PROVEN-HERE, PROVEN-IN-RECORD, SCALING-ESTIMATE, HYPOTHESIS, OPEN}.
# Sources read in full or at the cited anchors:
#   M0 docs/rde_nozzle_MASTER.md ([T-TH0] ~341-410, [T-O1] 413-426,
#     [T-O2] 428-439, [T-T0]+[S-T0P] 442-527, [T-NSW] 530-551,
#     [T-T3] 554-621, [T-T3-SI] 623-685)
#   docs/rde_nozzle_T3QS.md (whole file)
#   docs/rde_nozzle_problem_book.md (SS2, SS3, SS4.4, SS8, SS9)
#   docs/rde_nozzle_theorem_ledger.md SS3 (C-T1 + P4-periodic system)
#   docs/rde_nozzle_development_plan.md (G2 rows, lines 282-290, 488-490, 776-778)
#   docs/rde_nozzle_N6_swirl.md (whole file)
#   validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md
#     (D.9, D.10, D.11, D.12, D.17, D.18, D.19, D.20, S.22)
#   validation/sfoundations_raws_2026-08-13/phaseD/VERDICT_phaseD_proofs1.md SS3.2
#   docs/choice_ledger.yaml C51

------------------------------------------------------------------------------
## SS0 Notation and standing objects

- Lab frame cylindrical (x, r, theta, t); wave-frame azimuth
  phi := theta - Omega t (Omega = Omega_w, the wave angular speed;
  the phaseD docs write phi, T3QS writes theta' — same object).
- Strict T0 / H-A1 (HYPOTHESIS, surfaced; ledger row H-A1 of record):
  the flow is a pure rotating pattern with n identical equally spaced
  waves, q(x,r,theta,t) = q~(x,r,phi), q~ 2pi/n-periodic in phi,
  piecewise-C^1 with finitely many transversal wave-steady fronts
  (S1 class, problem book SS6).
- S: a fixed axisymmetric control surface enclosing the engine;
  meridional trace C_S parametrized by arc length l, radius r(l),
  outward normal n with n_theta = 0; dA = r dl dtheta. Pa constant.
- Flux integrand (problem book Def. 3.1):
      G(l, phi) := [rho u_x (u.n) + (p - Pa) n_x](l, phi),
  evaluated on the wave-frame fields (legitimate on axisymmetric S:
  w.n = u.n and w_x = u_x, [T-T0](ii), PROVEN-IN-RECORD M0:442-459).
- Cycle: t_c = 2pi/(n Omega); phase xi := t/t_c in Xi = [0,1);
  mu = pushforward of normalized time Lebesgue measure under
  t -> xi (problem book Def. 3.4) = Lebesgue on [0,1).
- J_exact := lim_{T->inf} (1/T) Int_0^T F_S(t) dt,
  F_S(t) = Int_S G dA (Def. 3.1).
- J_avg := Int_Xi F[Sigma; s(xi)] dmu(xi) (rung 2, (AVG), problem
  book SS3.5), F[Sigma; s] the steady thrust of the per-phase problem
  (Def. 4.4). We write F_2D(xi) := F[Sigma; s(xi)] regardless of
  whether the per-phase model is the meridional (u,v) system or the
  2.5-D five-field system (D.1) — SS2.1 distinguishes them.
- K = the reduction-residual (azimuthal commutator) vector of D.18
  [MS-DEF-KRES]; "div-form K" = the rows (1/r) d_phi F_phi,rel per
  conservation row, with front atoms n_phi [F_phi,rel]
  (distributional reading of record, D.18 r3/r4). The relation
  div-form row = advective K row + coefficient * K_rho (triangular
  recombination) is part of D.18's DEFINITION.
  IMPORTANT SCOPE NOTE: everywhere below we use ONLY the
  DEFINITIONAL content of D.18 (residual := exact row - reduced row;
  div-form display; recombination identities) — never the two iff
  clauses (judge-downgraded THEOREM*/SCHEMA modulo G-f, VERDICT
  SS3.2). The specific displayed row expressions inherit the G-f
  completeness conditional; the STRUCTURAL facts we use (the residual
  is an exact d_phi of a single-valued periodic quantity, per
  conservation row) hold by construction of "strike all d_phi in
  divergence form" and are robust to G-f.

------------------------------------------------------------------------------
## SS1 THE EXACT HALF: the sector-decomposition identity

### 1.1 Hypotheses

(E1) Strict T0 (H-A1 above). (E2) S fixed axisymmetric, Pa constant
([T-T0] hypotheses). (E3) G in L^1(S): satisfied in the S1 class
(bounded fields on a finite-area surface; front traces on S are
1-D curves, measure zero). Nothing else — no Euler equations beyond
what H-A1 already encodes, no smallness, no expansion.

### 1.2 Proposition 1 (sector decomposition of the exact mean — IDENTITY)

**Claim.** Under (E1)-(E3), with
    F_sect(phi; S) := Int_{C_S} G(l, phi) r(l) dl        (per-radian sector flux)
    F_true(xi; S)  := 2pi F_sect(phi(xi); S),            (total-thrust-normalized)
    phi(xi)        := phi_0 - (2pi/n) xi   (affine dictionary),
we have the IDENTITY
    J_exact = Int_Xi F_true(xi; S) dmu(xi)     for EVERY admissible S.
**Label: PROVEN-HERE.** (Every ingredient is either reproved below or
is [T-T0], PROVEN-IN-RECORD M0:442-459.)

**Proof.**
Step A (steadiness of the flux; = [T-T0](i), reproved for closure).
    F_S(t) = Int_0^{2pi} Int_{C_S} G(l, theta - Omega t) r dl dtheta.
At each fixed t, substitute theta -> theta + Omega t: the map is a
rotation of S^1, measure-preserving, so F_S(t) = F_S(0) for all t.
Hence the ergodic limit is trivial: J_exact = F_S(0). (This uses
only (E1)-(E2); the storage term never appears because we started
from the flux surface — the wall-form equality is [T-TH0]'s exact
mean-equality claim, PROVEN-IN-RECORD M0:356-362.)

Step B (Fubini). By (E3) and Tonelli-Fubini on the product
C_S x S^1:
    J_exact = Int_0^{2pi} F_sect(phi; S) dphi.
This is the azimuthal SECTOR decomposition: an additivity statement,
exact for any L^1 integrand.

Step C (Z_n reduction). By (E1), G(l, .) is 2pi/n-periodic in phi
(n identical waves = invariance under the Z_n rotation action; this
is exactly the group step D.9(ii) makes explicit, PROVEN-IN-RECORD
phaseD_meanswirl SS3 D.9), so
    Int_0^{2pi} F_sect dphi = n Int_{cell} F_sect dphi,
cell = any interval of length 2pi/n.

Step D (change of variables phi -> xi; emergence of mu). At a fixed
lab point the pattern is traversed at the CONSTANT angular rate
Omega; over one cycle t_c = 2pi/(n Omega) the wave-frame azimuth
sampled is phi(xi) = phi_0 - (2pi/n) xi: an AFFINE bijection of
[0,1) onto one fundamental cell (D.17's xi <-> phi dictionary,
PROVEN-IN-RECORD as DEFINITION + D.9(ii) proof). Affine change of
variables with |dphi| = (2pi/n) dxi:
    n Int_{cell} F_sect dphi = n (2pi/n) Int_0^1 F_sect(phi(xi)) dxi
                             = 2pi Int_Xi F_sect(phi(xi)) dmu(xi).
The measure mu ENTERS here as the pushforward of normalized time —
and because the traversal rate is constant (rigid rotation), mu is
exactly Lebesgue on Xi. Any non-uniformity (the log-uniform mu_P of
[T-O2]) lives in the pushforward under the DATA map xi -> s(xi),
never in the xi-measure itself. Combining Steps A-D and the
definition of F_true proves the claim. QED.

### 1.3 Remarks (each labeled)

(R1.1) **Type-check of the normalization. PROVEN-HERE.** If the flow
is degenerate axisymmetric (all fields phi-independent), then
F_true(xi; S) = F_S = the total thrust, for every xi. So F_true
carries the same normalization as F_2D(xi) = F[Sigma; s(xi)] (the
per-phase solve's thrust integrates its meridional flux over the
full 2pi). The comparison F_true vs F_2D in SS2 is therefore
well-typed: both are "the thrust the engine would have if the whole
annulus were in the state this azimuth carries".

(R1.2) **F_true is S-DEPENDENT; its mu-mean is not. PROVEN-HERE.**
Write the exact wave-frame x-momentum row in divergence form
(D.17: d_t -> -Omega d_phi, absolute components retained):
    d_x(rho u_x^2 + p) + (1/r) d_r(r rho u_x u_r)
      + (1/r) d_phi(rho u_x w_rel) = 0,   w_rel := u_theta - Omega r.
Integrate over the meridional wedge domain D between the traces of
two admissible surfaces S, S' (choose them so the wedge meets no
wall, e.g. two stations in the plume; otherwise the standard
wall-pressure bookkeeping of the wall-form/flux-form dictionary is
added on both sides) with the meridional weight r dx dr, at fixed
phi. The meridional divergence integrates to the difference of
per-radian sector fluxes; the azimuthal term survives as a
phi-derivative of a single-valued quantity:
    F_sect(phi; S) - F_sect(phi; S') = - d_phi M(phi),
    M(phi) := Int_D rho u_x w_rel dx dr
(the wedge's RELATIVE azimuthal transport of axial momentum). So
the per-sector flux genuinely varies with station — the variation
IS the theta-coupling — while its phi-mean is station-independent,
because Int_{S^1} d_phi M dphi = 0 exactly (M single-valued and
periodic; atoms of the distributional derivative included, since
the total mass of the derivative of a periodic BV function over the
circle is zero). Consistency check: Int F_true dmu = J_exact is
S-independent, as [T-TH0] requires. This remark is the exact,
nonperturbative form of "the sweep redistributes axial momentum
between phases; it cannot create it in the mean".

(R1.3) **What Proposition 1 does NOT say. PROVEN-HERE (scope).**
It does NOT say F_true(xi) equals, or is close to, any 2-D
per-phase thrust: F_true is a functional of the exact 3-D field.
It does NOT require the per-phase problems to be well-posed, or
even defined. It is pure measure theory on the exact flux integral
under the rotating-pattern hypothesis. Every gram of approximation
in the program's chain therefore lives strictly downstream of this
identity — which is exactly where [T-TH0] places it.

(R1.4) **Atomic / empirical mu. PROVEN-IN-RECORD** ([T-O2]
measure-agnostic note, M0:428-439): for atomic mu the cycle
quadrature is the exact weighted sum; Proposition 1's mu is the
uniform time measure, and any imported measure must re-verify the
switch-phase mu-null hypothesis. No change to the identity.

------------------------------------------------------------------------------
## SS2 THE APPROXIMATION HALF: the single substitution

### 2.1 The substitution, surgically

The rung-2 objective replaces, under the mu-integral of
Proposition 1,
    F_true(xi; S)  --->  F_2D(xi) := F[Sigma; s(xi)],
i.e. "the sector flux of the exact 3-D field at azimuth phi(xi)"
by "the thrust of an INDEPENDENT steady per-phase solve with data
s(xi)". This is the ONE substitution — with a surgical caveat about
which per-phase model:

(a) **Five-field target (proposed upgrade).** If the per-phase model
is the 2.5-D five-field system (D.1: rho, u_x, u_r, u_theta, p with
Gamma = r u_theta a streamline invariant, centrifugal u_theta^2/r,
u_theta^2/2 inside h0), then by CONSTRUCTION of D.18 the per-phase
operator is "the exact wave-frame operator with all d_phi struck",
and the entire discrepancy between the restricted exact field and
the per-phase solution is driven by the residual K alone (SS2.3).
Substitution count: ONE. **PROVEN-HERE** (given D.18's definitional
decomposition; see the SS0 scope note).

(b) **Current engine (meridional (u,v) solves).** Two additional,
SEPARATE commitments are made TODAY: (i) CONTRACT TRUNCATION — if
the interface data carry swirl (measured u_theta/(Omega r) ~
0.15-0.2 of record), the (u,v) engine cannot ingest u_theta: the
data error enters as a BOUNDARY term, not through K (see SS2.3,
term (II)); (ii) MODEL ROWS DROPPED — the Gamma-transport row, the
centrifugal source rho u_theta^2/r, and the u_theta^2/2 share of h0
are struck IN ADDITION to the d_phi terms. On synthetic swirl-free
H3 data (the T3 oracle row) the two models coincide (u_theta = 0
exactly propagates); on real data they do not, and the moved
channels are priced of record: tangential energy fraction 3-6%,
covariance weight (sigma/mu)^2 ~ 0.5 (D.10, PROVEN-IN-RECORD as
THEOREM + measured PRACTICE). **PROVEN-IN-RECORD** (D.10, N6-2/N6-3
for where the closed-form machinery survives).

So: the claim "a SINGLE substitution makes it rung 2" is EXACT for
the five-field per-phase model, and exact-modulo-two-declared-
channels for the current engine. This precision is FLAG F-3 in SS5.

### 2.2 Corollary 2.1 (exact error representation — IDENTITY)

    J_exact - J_avg = Int_Xi [ F_true(xi; S) - F_2D(xi) ] dmu(xi),
for every admissible S. **PROVEN-HERE** (subtract (AVG) from
Proposition 1; no hypotheses beyond (E1)-(E3) and F_2D mu-integrable).
Note each summand is S-dependent (R1.2) while the integral is not.

### 2.3 Exact adjoint-weighted representation, and its first-order form

Fix xi; write V_3D(xi) := the exact wave-frame field restricted to
the section phi(xi), and V(xi) := the per-phase solution. Let
N_0(.) denote the per-phase (five-field) operator with its BC
(interface data, slip on Sigma, supersonic outflow), and F(.) the
thrust functional (flux form on S, identically the form used in
F_true — same integrand G, R1.1).

By the D.18 definitional decomposition, the restricted exact field
satisfies the per-phase system with residual source:
    N_0(V_3D(xi)) = -K(xi)          in D,
    (interface data of V_3D(xi))  =  s_3D(xi) := trace of the exact
                                     field on Gamma_d at phi(xi),
while N_0(V(xi)) = 0 with data s(xi). Define dV := V_3D(xi) - V(xi).

**Hypotheses for the exact representation** (each surfaced):
  (H-DATA)  s(xi) = s_3D(xi): the contract family equals the exact
            trace. HYPOTHESIS — this is precisely what the
            data-contract apparatus (D.13 row, TRIPLE monitor D.14,
            G6 gate) audits; under the current engine with
            swirl-carrying data it is FALSE by truncation (SS2.1(b)).
  (H-SEG)   The segment-averaged linearization
            L~ := Int_0^1 DN_0(V(xi) + tau dV) dtau is boundedly
            invertible on the per-phase class with homogeneous BC.
            HYPOTHESIS (smooth S1 slices; for front-carrying slices
            the very objects require shift-derivative calculus and
            the S.22 (g2a)/(g2b) obstructions apply — OPEN there).
  (H-UNIQ)  Per-phase uniqueness (ledger H4/D3). HYPOTHESIS.

**Exact representation. PROVEN-HERE under (H-DATA), (H-SEG).**
By the fundamental theorem of calculus,
N_0(V_3D) - N_0(V) = L~ dV, so L~ dV = -K(xi) with ZERO interface
data (H-DATA) and homogeneous wall/outflow conditions. Similarly
F(V_3D) - F(V) = <dF~, dV> with dF~ := Int_0^1 dF[V + tau dV] dtau.
Let psi~_xi solve the segment adjoint problem L~* psi~_xi = dF~
(adjoint BC per the N6-1/five-field adjoint structure,
PROVEN-IN-RECORD docs/rde_nozzle_N6_swirl.md SS4 (c): the Lagrange
identity is exact-divergence, machine-verified). Then
    F_true(xi) - F_2D(xi) = <dF~, dV> = <psi~_xi, L~ dV>
                          = - <psi~_xi, K(xi)>,
and by Corollary 2.1
    J_exact - J_avg = - Int_Xi <psi~_xi, K(xi)> dmu(xi)        (ER)
EXACTLY — no remainder. All the difficulty is hidden in (H-SEG):
psi~ is not computable (it needs the exact field), and on
front-carrying slices (H-SEG) is not established (OPEN; the
weak-vs-weak wall (g2a) and the contact non-uniqueness wall (g2b,
Chiodaroli-De Lellis-Kreml class) are PROVEN-IN-RECORD as named
obstructions, S.22).

**First-order form (the corrector of record). PROVEN-IN-RECORD
at the frame level, with the frame's own named residues.** Replacing
psi~_xi by the computable per-phase adjoint psi_xi (linearize at
V(xi)) commits an O(||dV||^2) error, and (ER) becomes
    J_exact - J_avg = - Int_Xi <psi_xi, K(xi)> dmu(xi) + O(K^2)
                    = St . J_1 + O(St^2)
in the two-scale ordering. This is EXACTLY the record's corrector:
J_1 = -<psi_J, S_sweep(U_0)> (theorem ledger SS3, P4-periodic
first-order system, THEOREM* at statement level with residues (i)
Fredholm invertibility and (ii) quantitative IFT remainder NAMED and
OPEN) = -Int <psi_J(xi), D(W_A(.;xi))> dxi (T3QS SS1), with the
dictionary
    D(W) = (1/r) d_theta'[F_theta(W) - Omega r W]  ==  div-form K row
(F_theta - Omega r W is the relative azimuthal flux F_phi,rel; the
identification is exact), and W_A = the composite of per-phase
solutions laid out in azimuth. If (H-DATA) fails (current engine on
swirl-carrying data), (ER) acquires a second term:
    (II) := - <adjoint interface trace, s_3D(xi) - s(xi)>_Gamma_d,
the CONTRACT-TRUNCATION error — additive at first order, separately
monitorable (D.14). **PROVEN-HERE** (same Lagrange-identity
integration by parts, keeping the boundary term).

### 2.4 Is it "the ONLY approximation in the chain"? (cross-check)

The record's claim ([T-TH0] M0:374-380; [S-T0P] stage 2 M0:486-489)
is CONFIRMED with the following exact hypothesis list — under
(E1)-(E3) plus:
  (H-a) strict T0 — else Proposition 1 itself is unavailable and
        J_exact reverts to the ergodic object (D2.2 fallback);
  (H-b) = (H-DATA) — else the contract error (II) is a SECOND
        approximation (declared in the record via D.13/D.14/G6, but
        it is a distinct link, not part of rung 2 proper);
  (H-c) exact per-phase solves — discretization is a THIRD layer,
        separately gated (G1 oracle gate, absolute);
  (H-d) the same thrust functional on both sides (flux form on the
        same S; the wall-form dictionary holds per steady momentum
        balance for the per-phase field, and for the exact field in
        the mean by [T-TH0]);
  (H-e) per-phase uniqueness (H4) — else F_2D is branch-ambiguous.
Under (H-a)-(H-e) and the five-field model, the ENTIRE discrepancy
J_exact - J_avg is the K-driven term (ER): the record's sentence is
correct, read as "the only approximation AT THE FORMULATION LEVEL,
in the five-field per-phase chain". **PROVEN-HERE** (assembly of
SS1-SS2.3). For the current meridional engine the sentence needs the
SS2.1(b) caveat (FLAG F-3).

------------------------------------------------------------------------------
## SS3 CAN THE ERROR BE LARGE? Both sides, honestly

### 3.1 (a) The a-priori bound structure and its constant

**Derivation of the structure. SCALING-ESTIMATE (with the scaling
derived; the missing pieces named as OPEN).** Start from (ER):
|F_true - F_2D|(xi) <= ||psi~_xi||_{X*} ||K(xi)||_X for a norm pair
X to be fixed (this is S.22's design fork g1: split
transit-integrated L^1_x L^2 + front-strength norm, or a
negative-order/dual-Lipschitz pair — PROVEN-IN-RECORD as the named
candidate class, SCHEMA). The K-content scales as follows
(advective rows; div-form differs by bounded triangular
recombination, D.18): with |w_rel|/r ~ Omega (1 + O(u_theta/Omega r)),
u_theta/(Omega r) ~ 0.15-0.2 measured, and d_phi V ~
Delta_cell V / (2pi/n) with Delta_cell V the O(1) data variation
across one cell,
    K ~ rho Omega (n/2pi) Delta_cell V     pointwise (O(1): the wave
                                           IS the azimuthal structure),
    Int_transit K dt ~ rho (Omega tau_n) (n/2pi) Delta_cell V
                     = rho St_n Delta_cell V,
i.e. the PER-TRANSIT accumulated residual impulse is
O(St_n) x (cycle data variation) — the transit-integrated reading
in which S.22 (g3) locates the smallness (PROVEN-IN-RECORD: g3
r1-reformulated; the pointwise-small reading is REFUTED of record).
A Gronwall/energy estimate marching in x under the spacelikeness
margin m_n > 0 (finite domain of dependence, D.4 THEOREM;
Gamma-independence of the symbol, D.3 THEOREM, means the swirl-free
estimate machinery applies with two extra transport rows) then gives
the bound STRUCTURE
    |J_exact - J_avg| <= C . St_n . V_data,                      (B)
    V_data := TV_mu(data cycle) + (front strength x front measure),
with
    C = C(  min m_n along the march;            [blows up ~ 1/m_n]
            ||grad V_3D|| (base-flow gradients); [Gronwall exponent]
            S1 front count and strengths;        [adjoint jumps,
                                                  shift terms]
            ||psi||, osc_mu(psi) (thrust-adjoint size and its
                                  phase-oscillation, cf. SS3.2);
            geometry (r_min through the 1/r factors; wound
            domain-of-dependence thickness, S.22 (g1)/(g3)) ).

**Why C is NOT provably small at St_n ~ 0.1-1.** Six independent
reasons, each labeled:
  R-1 St_n is not asymptotic there: the expansion J_avg + St J_1 +
      O(St^2) has NO proven radius of convergence; C-T1 is
      CONJECTURE and the quantitative IFT remainder is a NAMED,
      unwritten residue (theorem ledger SS3 (ii)). PROVEN-IN-RECORD
      (status), hence the bound (B) with a KNOWN C is OPEN.
  R-2 C contains exp(Gronwall over the transit): the coupling
      coefficient scales with base-flow gradients over the margin;
      the margin is SMALLEST exactly where the march starts (sonic/
      near-sonic interface, problem book SS4.3bis; the L4 pin is a
      floor, not a smallness certificate). No proof makes
      exp(O(1)) small. PROVEN-HERE (structure), OPEN (value).
  R-3 On the general in-scope class NO FINITE C IS PROVEN AT ALL:
      per-phase references generically carry fronts (SS0 admits
      them; detonation-fed scope), making the comparison
      weak-vs-weak — no multi-D L^1 stability theory exists (g2a),
      and on contact/slip data the relative-entropy route is
      KNOWN-BROKEN (convex-integration non-uniqueness, g2b). The
      T-RED owner must fit fronts or declare a slip-line-free
      sub-scope. PROVEN-IN-RECORD (S.22 g2a/g2b as named
      obstructions).
  R-4 The distributed error term is controlled by the ADJOINT
      OSCILLATION across phases (SS3.2), which off-ray is O(1):
      measured data fluctuation sigma/mu ~ 0.70; two-parameter
      (P0,T0)(xi) content at gamma(T) leaves the T3 ray (T3QS B1).
      PROVEN-IN-RECORD (mechanism) + measured scales.
  R-5 The jump term is first-order x O(1) jump: [k]_jump ~
      1 - PR^{-1} is NOT small (PR = several); its absorption by
      the fitted inherited sheet is the pre-registered O5
      prediction P-ii — CONJECTURAL UNTIL MEASURED (T3QS B4(i),
      status restatement of record). PROVEN-IN-RECORD (status).
  R-6 (current engine only) The swirl channels moved out by the
      five-field upgrade constitute a separately-committed floor:
      tangential energy fraction 3-6%, covariance weight ~0.5
      (D.10). Mapping energy fraction to thrust error is
      channel-dependent; treat as a few-percent-class floor.
      SCALING-ESTIMATE (record numbers, derived mapping not
      claimed).

### 3.2 (b) The protection mechanisms, derived, and their breaking

**Proposition 3.2 (mean-zero / covariance decomposition of the
first-order error). PROVEN-HERE within the [J-CT1] first-order
frame** (i.e., all statements here are about J_1; the frame itself
carries the R-1 caveat).

Setup: J_1 = - Int_Xi <psi_xi, K_xi> dmu with K_xi := div-form
K(W_A)(., ., phi(xi)) (SS2.3 dictionary), W_A the azimuth-composite
of the per-phase family, periodic in xi. Define the mu-means
psi_bar := Int psi_xi dmu, K_bar := Int K_xi dmu (Bochner). Then,
algebraically,
    J_1 = - <psi_bar, K_bar>
          - Int_Xi <psi_xi - psi_bar, K_xi - K_bar> dmu(xi).    (P)

(i) **Row-wise mean-zero of div-form K. PROVEN-HERE.** At each
interior point (x,r), the pairing weight r dx dr cancels the 1/r:
<psi, K_row> = IntInt psi d_phi F_phi,rel dx dr. Since F_phi,rel is
a single-valued, periodic (BV in phi) quantity, the total mass of
its distributional phi-derivative over the circle is ZERO — front
atoms included. Hence: if the composite data cycle xi -> W_A(xi) is
CONTINUOUS (BV, no data-cycle jump), K_bar = 0 pointwise and
    J_1 = - Cov_mu(psi, K):
the first-order error is EXACTLY the covariance of the per-phase
adjoint variation with the residual variation. The naive triangle
bound |J_1| <= ||psi|| ||K|| ignores this cancellation; the true
bound is |J_1| <= osc_mu(psi) . ||K||-content.

(ii) **Ray recovery (= T-T3QS P5-P6). PROVEN-HERE, agreeing with
the record.** On a T3 ray family W_A(.;xi) = k(xi) W_hat: degree-1
homogeneity of the fluxes (T3QS P2, PROVEN-IN-RECORD,
symbolic-sufficient, EOS-general) gives F_phi,rel(W_A) =
k(xi) F_phi,rel(W_hat), so K_xi = k'(xi) Z_hat with Z_hat fixed
(P5); Jacobian and adjoint-source invariance (P3-P4) give psi_xi =
psi_hat constant. Then the covariance term in (P) vanishes
IDENTICALLY, and
    - smooth periodic cycle: K_bar = 0 too, J_1 = 0 EXACTLY
      (second-order protection);
    - blowdown sawtooth: the corrector legitimately prices only the
      a.c. part of the cycle (at the data jump the neighboring
      phases differ O(1) and the linearized frame is invalid there
      — T3QS B3, PROVEN-IN-RECORD); the a.c. part has
      Int^{ac} k' dxi = -[k]_jump, whence
      J_1 = <psi_hat, Z_hat> [k]_jump:
      the ENTIRE first-order residue concentrates at the
      wave-passage jump. Identical to T3QS P6 (up to its Z
      normalization). The derivation route here (periodicity of the
      div-form flux) is INDEPENDENT of T3QS's factorization route
      and confirms it.

(iii) **General cycles. PROVEN-HERE (formula), with each term's
smallness OPEN.** For a cycle with jumps,
    J_1 = <psi_bar, (jump content)> - Cov^{ac}_mu(psi, K),
i.e. exactly TWO first-order channels:
    (J) the JUMP term — mean adjoint paired with the front/data-jump
        content; localized in a xi-window of width ~St_n (parcels
        whose transit straddles the wave passage); the physics the
        fitted inherited sheet represents steadily; absorption =
        P-ii, CONJECTURAL;
    (H) the HYSTERESIS term — the covariance, T3QS's off-ray "area
        of a non-exact 1-form over the data loop"; computable per
        cycle, provably zero only on ray families.

**Breaking conditions** (all PROVEN-IN-RECORD as rejectors/
boundaries; assembled here):
    - off-ray two-parameter cycles ((P0,T0)(xi) at gamma(T)): kills
      adjoint constancy (T3QS R1) -> (H) generically nonzero;
    - phase-dependent profile shapes (H3 violation, T3QS R2): same;
    - non-affine objective (T3QS R3): kills source invariance;
    - cap-binding subsonic phases: off-ray BY CONSTRUCTION (family
      structure changes; T3QS B2), and they carry the acoustic-lag
      channel tau_ac/T ~ O(0.1-1) that rung 2 misses;
    - strong theta-coupling / St_n -> O(1): the first-order FRAME
      degrades (B3): (P) still holds as a statement about J_1, but
      J_1 no longer approximates the error — the O(St^2) remainder
      is uncontrolled (R-1).

### 3.3 (c) The sharpest honest conclusion, and the measurement that pins it

**Tier 1 — what is PROVEN.** (i) The decomposition error is EXACTLY
the mu-integral of the adjoint-paired residual (ER), under
(H-DATA)/(H-SEG); (ii) at first order it splits into jump term +
covariance term (Prop. 3.2), the covariance vanishing on ray
families and the jump term concentrating in the wave-passage
window; (iii) NO finite numerical bound on |J_exact - J_avg| exists
in the record at St_n ~ 0.1-1 (C-T1 CONJECTURE; S.22 SCHEMA), and
on the general front/contact-carrying class no bound is proven at
ANY St (g2b). Therefore: **the standing fear "the committed error
could be LARGE" CANNOT be refuted by theory available today.**
Theory narrows the MECHANISM, not yet the NUMBER.

**Tier 2 — SCALING-ESTIMATE (each scaling derived above).**
Plugging the measured scales of record into the proven structure:
    - jump channel (J): ~ St_n x [k]_jump x (normalized adjoint
      pairing) — with St_n ~ 0.1-1 and [k] ~ O(1): PERCENT TO TENS
      OF PERCENT before fitted-sheet absorption; few-percent class
      IF P-ii holds (conjectural);
    - hysteresis channel (H): ~ C_G St_n (sigma/mu-weighted data
      variation) x (adjoint oscillation fraction) — few percent to
      >10% on strongly off-ray cycles; second-order (unquantified
      constant) on ray-like smooth cycles;
    - swirl channels (current engine only): few-percent floor
      (3-6% energy fraction, covariance weight 0.5) removed by the
      five-field upgrade.
Honest net statement: single-digit-percent total error is PLAUSIBLE
on ray-like sawtooth cycles with a good fitted sheet; >10% is NOT
EXCLUDED on off-ray, jump-heavy, cap-binding cycles. Anyone quoting
a hardware number from rung 2 without an St error bar is out of
contract (problem book SS8, of record — confirmed here).

**Tier 3 — the O5-lite pin (which quantity, which comparison).**
One certified instance (unsteady axisymmetric-forced or 3-D
wave-frame solve on committed data) suffices for the number:
    (1) QUANTITY: mean axial thrust through a FIXED S (flux form),
        plus the xi-RESOLVED sector flux F_true(xi; S) (computable
        from the 3-D field by the Proposition-1 integrand — this is
        the new, directly comparable object this derivation adds);
    (2) COMPARISONS: (A) J_exact vs J_avg — measures eps directly
        (feeds SS4); (B) J_exact vs J_avg + St J_1 (one extra
        linear adjoint solve, M0 VI.4bis(ii) pin) — tests the
        first-order frame; (C) F_true(xi) vs F_2D(xi) pointwise in
        xi — LOCALIZES the error (jump window vs distributed:
        discriminates channel (J) from (H)); (D) an St-SWEEP (vary
        Omega or nozzle length on a ray cycle): fitted error
        exponent must approach 2 (ray protection) — exponent 1
        with nonzero area coefficient on an off-ray control;
        (E) fitted-sheet ON/OFF ablation in the jump window — tests
        P-ii.
    (3) REJECTORS: error not decreasing under St -> 0 kills C-T1;
        exponent 1 on a smooth ray cycle kills T-T3QS's carrier
        assumptions for that instance; (C) showing distributed O(1)
        mismatch outside the jump window on a ray cycle kills the
        localization claim.
This matches and sharpens the record's O5 targeting (T3QS B4(iii),
D6 Phase A4); item (C) is the addition licensed by Proposition 1.

------------------------------------------------------------------------------
## SS4 VALUE-BOUND TRANSFER: the 2-eps suboptimality lemma

### 4.1 Lemma (2-eps transfer). PROVEN-HERE.

**Hypotheses.** A = the feasible design class, IDENTICAL for both
functionals; both J_exact, J_avg: A -> R are defined on A with the
SAME frozen data family s(.) and measure mu (this presupposes H-F1:
the frozen family — under bilevel coupling the two objectives are
not even comparable pointwise without the reduced response map,
PB-4). UNIFORMITY hypothesis (exact form needed):
    (U)  sup_{Sigma in A} | J_exact[Sigma] - J_avg[Sigma] |  <=  eps.
Let Sigma* be any maximizer of J_avg over A (attainment assumed;
else see the eta-variant).

**Claim.** J_exact[Sigma*] >= sup_A J_exact - 2 eps.

**Proof.** For every Sigma in A:
    J_exact[Sigma*] >= J_avg[Sigma*] - eps          (by (U) at Sigma*)
                    >= J_avg[Sigma]  - eps          (optimality of Sigma*)
                    >= J_exact[Sigma] - 2 eps       (by (U) at Sigma).
Take sup over Sigma. QED.

**Sharpness. PROVEN-HERE.** A = {Sigma_1, Sigma_2}, J_avg == 0 on A,
J_exact(Sigma_1) = -eps, J_exact(Sigma_2) = +eps: both satisfy (U);
Sigma* = Sigma_1 is a legitimate argmax selection and is exactly
2 eps suboptimal. So the constant 2 cannot be improved without
extra structure.

**eta-variant. PROVEN-HERE.** If Sigma* is only an eta-maximizer of
J_avg, the same chain gives 2 eps + eta.

**Weakened uniformity. PROVEN-HERE.** Only two evaluations of (U)
were used: at Sigma* and at the comparator. Hence it suffices to
have |J_exact - J_avg| <= eps_1 at Sigma* and <= eps_2 on an
eta-argmax set of J_exact, giving eps_1 + eps_2 + eta. This matters
operationally: certifying eps on the SINGLE designed contour plus a
neighborhood of the exact optimum is weaker than class-wide
uniformity — but the exact optimum's location is unknown, so in
practice (U) over the searched class is what an audit can consume.

### 4.2 Is uniformity over the design class plausible/provable?

Route (named, standard): eps(Sigma) = C(Sigma) St_n(Sigma) V_data
from (B), then uniformize:
    - A compact in the Chenais/uniform-cone topology
      (PROVEN-IN-RECORD as the sector-decomposition SCHEMA, problem
      book SS5, with the user's cone/Chenais pins);
    - Sigma -> C(Sigma) finite and upper-semicontinuous under
      (i) a uniform margin floor m_n >= m_0 > 0 along the march,
      (ii) UNIFORM S1-regularity (front count bounded, no wall-shock
      formation on A) — HYPOTHESIS, known to fail at the P7 failure
      boundary, and (iii) solution-map continuity (P7 apparatus);
    - note St_n(Sigma) varies with Sigma through tau_n (longer
      nozzles = larger St): on length-bounded classes sup St_n is
      finite.
Under (i)-(iii) compactness gives sup_A eps(Sigma) < inf.
**Status: OPEN, twice over.** First, the pointwise bound eps(Sigma)
itself is unproven (S.22 SCHEMA; g2a/g2b obstructions on
front-carrying references — on the general class not even
finiteness is proven, R-3). Second, its Sigma-uniformization rests
on uniform S1 — an assumption the record itself prices (ledger row
D3, P7 boundary). The route is standard and I see no structural
obstruction ON A SHOCK-FREE-REFERENCE SUB-SCOPE (S.22 g2a's own
auditable sub-scope: smooth transonic-free marches on L4 data) —
there, landing (B) with an explicit C and then (U) by compactness is
a credible F2-window theorem target. On the general class, (U) is
OPEN and possibly requires the fitted-front machinery
(Majda/Coulombel-Secchi) with its own instability windows.

**Operational consequence for G2 (value gate).** The gate's honest
reading is: a rung-2 design gain Delta over a baseline certifies an
exact-world gain only NET OF 2 eps:
    certified gain >= Delta - 2 eps,
with eps either measured (O5-lite, SS3.3 Tier 3) or bounded (future
(B)+(U)). With eps unmeasured, every G2 verdict is CONDITIONAL. See
FLAG F-4.

------------------------------------------------------------------------------
## SS5 RECORD CROSS-CHECKS AND FLAGS

Cross-checks performed against: [T-TH0]/[T-O1]/[T-O2]/[T-T0]/[T-NSW]
/[T-T3](+SI) (M0:341-685), theorem ledger SS3 (C-T1, P4-periodic),
T3QS (whole), problem book SS3/SS8/SS9, phaseD D.9/D.17/D.18/D.19/
D.20/S.22 with the VERDICT SS3.2 judge labels, N6 doc, D6 G2 rows,
C51.

**Confirmations (no discrepancy):**
- [T-TH0]'s storage-vs-flux disambiguation is exactly reproduced by
  SS1: the identity half introduces NO error; the modeling error
  lives entirely in the F_true -> F_2D link. CONFIRMED.
- The corrector dictionary D(W) == div-form K == S_sweep type-checks
  across T3QS SS1, theorem ledger SS3, and D.18. CONFIRMED (SS2.3).
- Prop. 3.2(ii) re-derives T-T3QS P5-P6 by an independent route
  (div-form periodicity instead of ray factorization); results
  agree, including the sawtooth jump term. CONFIRMED.
- The T-O1/T-T3 assembly (J = Int(a Pc - Pa b) dmu = F[Sigma;<Pc>])
  is internal to rung 2 (it manipulates J_avg); nothing here touches
  it, and nothing in it presumes the bridge. CONFIRMED, no
  overclaim found in the assembly itself.
- C-T1's CONJECTURE status and its two named residues (Fredholm
  invertibility; quantitative remainder) are exactly the two places
  my SS2.3/SS3.1 derivations had to stop. The ledger is honest.
  CONFIRMED.

**FLAGS (discrepancies / over- and under-claims, loudly):**

F-1 (mild OVERCLAIM in presentation, M0 [T-TH0] line ~376-377). The
    inline "= Int F_steady dmu + O(St)" typographically asserts an
    O(St) bound whose status is C-T1 CONJECTURE (no proven remainder
    at any St, and second-order refinement on ray cycles). M0's own
    T3-QS remark and the problem book SS8 ("NOT self-licensing") are
    honest; the one-line form should carry an inline [C-T1] tag so
    the equation cannot be quoted detached from its status.

F-2 (UNDERCLAIM / missing citable statement). The EXACT half —
    Proposition 1, the sector-decomposition identity J_exact =
    Int F_true dmu — exists NOWHERE in the record as a numbered
    statement: the record holds [T-T0] (steadiness) and D.9(ii)
    (pointwise mean equality) and then books the ENTIRE bridge to
    J_avg inside C-T1. But the measure-theoretic half is
    theorem-grade with a four-step proof (SS1.2); C-T1's genuinely
    open content is ONLY the F_true -> F_2D substitution. Candidate
    mint for the R4 window (with R1.2's S-dependence remark and the
    R1.1 type-check as companion remarks); it also licenses the new
    O5-lite comparison (C) of SS3.3.

F-3 (precision needed on "the only approximation in the chain",
    [S-T0P] stage 2 / [T-TH0]). The sentence is EXACT for the
    five-field per-phase target; for the CURRENT meridional (u,v)
    engine it holds only modulo the two declared swirl commitments
    (contract truncation of u_theta; dropped Gamma/centrifugal/
    swirl-KE rows), which are separately priced (D.10) but are NOT
    part of K. Recommended wording of record: "the only
    approximation in the FIVE-FIELD chain; the meridional engine
    commits in addition the N6/D.10 swirl channels until the
    upgrade lands." This is also the cleanest statement of what the
    proposed 2.5-D upgrade BUYS: it shrinks the committed content
    of the approximation half from {theta-coupling + swirl
    channels + contract truncation} to {theta-coupling} alone.

F-4 (gap in the G2 framing, D6:286/489/776). G2's "theorem-grade:
    bound-ladder gap per channel" is rung-2-INTERNAL (it compares
    channel gains within J_avg). The transfer of a rung-2 gain to
    an exact-world claim needs the 2-eps lemma (SS4.1) and hence a
    UNIFORM eps — currently neither measured nor proven. No false
    statement in D6, but the F5a Verdict template should carry
    "gain net of 2 eps, eps = <measured/assumed>" explicitly;
    otherwise the gate can certify a Delta smaller than the
    unpriced bridge error.

F-5 (normalization hazard, not a discrepancy). The record carries
    the corrector in two conventions: St explicit (ledger:
    J_avg + St J_1) and St absorbed into D (T3QS SS1). S.22 (g4)
    already names the double-pricing risk for the corrector vs the
    K-bound; the same care applies between the two J_1 conventions.
    One normalization of record should be pinned when T-RED lands.

**Reliance on judge-downgraded material (declared):** this document
uses D.18 ONLY at its DEFINITION level (residual decomposition,
div-form display, recombination identities) — not the two iff
clauses (SCHEMA pending E-3/G-f). The row-display specifics inherit
the G-f completeness conditional; Propositions 1 and 3.2 and the
representation (ER) are robust to G-f because they consume only
"residual = exact - reduced = d_phi content in divergence form",
which is definitional. If G-f finds a transcription error in a
specific row, the row display changes; no statement here does.

------------------------------------------------------------------------------
## SS6 Claim register

| # | Claim | Label | Where |
|---|-------|-------|-------|
| 1 | J_exact = Int_Xi F_true(xi;S) dmu — identity, any admissible S | PROVEN-HERE (Prop. 1; ingredients [T-T0], D.9(ii), D.17 PROVEN-IN-RECORD) | SS1.2 |
| 2 | mu emerges as pushforward of time; uniform in xi because the traversal is rigid rotation; non-uniformity lives only in s(xi)/mu_P | PROVEN-HERE (Step D) + PROVEN-IN-RECORD ([T-O2]) | SS1.2 |
| 3 | F_true carries total-thrust normalization; F_true vs F_2D well-typed | PROVEN-HERE | SS1.3 R1.1 |
| 4 | F_true(xi;S) is S-dependent; the dependence is exactly the azimuthal redistribution term whose phi-mean vanishes | PROVEN-HERE | SS1.3 R1.2 |
| 5 | J_exact - J_avg = Int [F_true - F_2D] dmu — identity | PROVEN-HERE (Cor. 2.1) | SS2.2 |
| 6 | Exact adjoint representation (ER): error = -Int <psi~_xi, K_xi> dmu, no remainder, under (H-DATA)+(H-SEG) | PROVEN-HERE; (H-SEG) on front-carrying slices OPEN (g2a/g2b) | SS2.3 |
| 7 | First-order form = the J_1 corrector of record; dictionary D(W) == div-form K == S_sweep exact | PROVEN-IN-RECORD (ledger SS3 THEOREM* frame; T3QS) + PROVEN-HERE (dictionary) | SS2.3 |
| 8 | Contract-truncation error (II) is additive at first order and distinct from K | PROVEN-HERE | SS2.3 |
| 9 | "Only approximation in the chain" holds under (H-a)-(H-e) for the five-field model; needs the swirl-channel caveat for the current engine | PROVEN-HERE (assembly) + FLAG F-3 | SS2.4 |
| 10 | Bound structure |J_exact - J_avg| <= C St_n V_data; per-transit K impulse ~ St_n x cell variation | SCALING-ESTIMATE (scaling derived; norm pair + constant OPEN, S.22 fork) | SS3.1 |
| 11 | C not provably small at St_n ~ 0.1-1; on front/contact classes not provably FINITE | PROVEN-IN-RECORD (C-T1 CONJECTURE, S.22 g2a/g2b) + PROVEN-HERE (R-2 structure) | SS3.1 |
| 12 | J_1 = -<psi_bar,K_bar> - Cov_mu(psi,K); div-form K has zero phi-mean (atoms included) | PROVEN-HERE (Prop. 3.2, within the [J-CT1] frame) | SS3.2 |
| 13 | Ray recovery: J_1 = 0 smooth ray cycles; = <psi_hat,Z>[k]_jump on sawtooth — independent re-derivation of T-T3QS P5-P6, agreeing | PROVEN-HERE + PROVEN-IN-RECORD (T3QS) | SS3.2 |
| 14 | Exactly two first-order channels: jump (J) and hysteresis (H); breaking conditions as listed | PROVEN-HERE (formula) + PROVEN-IN-RECORD (rejectors R1-R3, B1-B3) | SS3.2 |
| 15 | Jump absorption by the fitted sheet | HYPOTHESIS (= pre-registered P-ii, conjectural until measured — record status confirmed) | SS3.2-3.3 |
| 16 | Error magnitude: single-digit % plausible on protected cycles; >10% not excluded on unprotected ones; no theory-only refutation of "large" exists today | Tier 1 PROVEN (status); Tier 2 SCALING-ESTIMATE | SS3.3 |
| 17 | O5-lite protocol: quantities (J_exact, F_true(xi;S)) and comparisons (A)-(E) with rejectors; (C) newly licensed by Prop. 1 | PROVEN-HERE (design) anchored to record targets (T3QS B4, D6 A4) | SS3.3 |
| 18 | 2-eps lemma with exact uniformity hypothesis (U); sharpness of the constant 2; eta-variant; two-point weakening | PROVEN-HERE (Lemma 4.1) | SS4.1 |
| 19 | Uniformity over the class: named compactness route (Chenais + margin floor + uniform S1); status | OPEN (twice: pointwise bound OPEN, uniformization contingent on uniform S1 HYPOTHESIS); shock-free sub-scope = credible theorem target | SS4.2 |
| 20 | G2 verdicts must net out 2 eps; currently conditional | PROVEN-HERE (consequence of 18) + FLAG F-4 | SS4.2, SS5 |
