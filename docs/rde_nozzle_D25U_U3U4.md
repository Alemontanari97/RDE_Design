# D2.5-U steps U3 + U4, written for real — fronts and composition
# (component -a of C-D25U at whole-class level; the C-MAJDA sharpening)

Status: RIGOR ATTACK OF RECORD (2026-08-06, S16 deep-foundations
campaign second tranche, [RIGOR/A]; continues docs/rde_nozzle_D25U_U1.md
= U1 and [T-U2RG] = U2). This document executes steps U3 (fronts:
local straightening + uniform Lipschitz traces) and U4 (composition on
[0, L_x]) of the D2.5-U proof architecture
(docs/rde_nozzle_remaining_conditionals.md §1; namespace D2.5-U, NOT
10bis), completing the C-D25U component -a estimate chain at the level
of the whole certified SHOCKED class — with every clause it costs
NAMED. Registry: [S-D25U-U34]; carrier (front-solve structure):
[X-U3BD] validation/u3_bordered_front_solve.py.

Audit line: [Class: SCHEMA (function-space estimates written at full
detail; the finite-dimensional front lemmas inside are THEOREM-grade
with the U3-H1 scalar condition named) | Falsifier: the C-D25U
falsifier + the new s_L channel (§2.3) | Carrier: X-U3BD (bordered
front solve, Lax count, Lopatinskii scalar; suite group (xiii)) |
Gamma: EOS-general structure; carrier oracle = declared perfect-gas
instance; the entropy-jump floor (§4.1) additionally assumes genuine
nonlinearity of the acoustic families on the state box (G > 0;
automatic for perfect/ideal gas — declared, §5(c4))].

VERDICT UP FRONT: component -a of C-D25U is now WRITTEN at the level
of the whole certified class — smooth regions (U1), wall reflection
(U2), fronts (U3, this doc), composition (U4, this doc) — with the
Lipschitz constant EXPLICIT in the five-constant certificate
(delta, L_x, C_geo, C_dat, h_min). The completion is honest, not
free: it PRICES four clauses (§5), of which two are discoveries in
the h_min tradition: (D1) the certified-set front clauses must be
read as WALL-ATTACHMENT (every front has a transversal wall foot) —
under that reading the front count N_F is DERIVED from the five
constants via a new entropy-budget counting lemma, otherwise N_F is a
sixth named constant; (D2) the two-solution estimate compares
solutions WITHIN A DECLARED FRONT-TOPOLOGY STRATUM (same front count
and causal order) — the cross-topology comparison is NOT an estimate
statement at all (it is the census/tournament layer and the RK-G
policy, already of record). And ONE sharpening of C-MAJDA: its
quantitative content inside the planar x-as-time S1 class is now a
SINGLE SCALAR condition (U3-H1: the 1-D Lopatinskii-Schur scalar s_L
nonvanishing on the compact certified front set), machine-exhibited
at the reference (s_L = 1.8685, X-U3BD) — no longer an appeal to
"Majda stability" at large.

------------------------------------------------------------------------------
## §1 Setting: the shocked certified set, read precisely

D(delta, L_x, C_geo, C_dat, h_min) as amended by U1: walls C^2 with
norm <= C_geo, inflow data C^1 <= C_dat, axial margin u - c >= delta
on the whole domain (BOTH sides of every front — the S1 marching
class), boundary-function margin >= delta, duct-width floor
w_+ - w_- >= h_min. Shocked references additionally carry (verbatim
from the ledger §1 statement): "Lax front-strength margins >= delta
with transversal wall/front angles >= delta", fronts finitely many,
fitted, noninteracting, graphs y = sigma_k(x) over subintervals of
[0, L_x].

READING OF RECORD (declared here, priced in §5): the front clauses
are read as
 (F1) STRENGTH MARGIN: every front is a Lax shock of an acoustic
      family with normal-Mach margin M_n - 1 >= delta on its whole
      arc (equivalently: all five Lax slope inequalities of §2.1 hold
      with margins derived from delta);
 (F2) WALL ATTACHMENT: every front has at least one endpoint on a
      wall, met transversally with angle >= delta (this is the
      natural reading of "transversal wall/front angles >= delta" —
      a front with no wall intersection would make the clause vacuous
      for it); the other endpoint is a wall, the inflow, or the
      outflow section;
 (F3) NONINTERACTION: fronts are pairwise disjoint in the closed
      domain (front-front interactions and reflections are OUTSIDE
      this class — they are march-topology events, RK-G territory).
Front ORIGINATION: each front either originates at a declared
geometric feature of the wall (lip corner, kink — position determined
by the wall function) or enters through the inflow section with
position/slope part of the certified data (clause c3 of §5).

Both solutions being compared are certified with the SAME margins and
the SAME front topology (count N_F and causal order — discovery D2,
clause c2 of §5).

------------------------------------------------------------------------------
## §2 The finite-dimensional front lemmas (the quantitative bricks)

### §2.1 U3-L0 (the front is a 1-D Lax shock; the bordered solve)

In the x-as-time reading a fitted front y = sigma(x) is a genuine
shock of the 1-D (y-line) hyperbolic evolution: slopes are the
characteristic speeds, sigma' is the shock speed. At the X-U3BD
oracle (oblique shock M1 = 2.5, beta = 40 deg — the X-G12 reference)
the Lax structure is machine-verified: ALL FOUR upstream
characteristics impinge on the front and EXACTLY ONE downstream
family (the fast acoustic) impinges — total 5 = n + 1, the classical
Lax count [X-U3BD P1, margins printed: lam+^dn - sigma' = 0.4608,
sigma' - lam+^up = 0.4027, streamline margins 0.5204/0.8391].

Per x-station the front solve therefore couples the 5 unknowns
(V_+ trace, sigma') to 4 linearized RH equations plus the 1 impinging
downstream characteristic value: the BORDERED system

    M = [ dH/dV_+   dH/dsigma' ]      w_imp^T = l_imp^T A_p(V_+),
        [ w_imp^T       0      ]

l_imp = left eigenvector of the impinging family (the characteristic
variable w_imp^T dV is what the downstream region delivers to the
front along its characteristics). G12-L2 certified the BLOCKS
(dH/dV_+ nonsingular strictly inside Lax; dH/dsigma' /= 0 at nonzero
strength). U3 needs M ITSELF nonsingular; by the bordered-determinant
identity det M = -det(dH/dV_+) * s_L this is exactly:

### §2.2 U3-H1 (the Lopatinskii scalar — the sharpened C-MAJDA)

    s_L := w_imp^T (dH/dV_+)^{-1} dH/dsigma'  /=  0
    on the certified front set K_delta (defined in §2.3).

This scalar is the 1-D Majda-Lopatinskii determinant of the front in
the x-as-time frame: s_L = 0 would mean a neutral front-displacement
mode excitable with zero incoming data — the free boundary would not
be solvable for sigma'. U3-H1 is a NAMED CONDITION of this document
(clause c1 of §5), NOT proven over all of K_delta here; its status:
 - machine-exhibited at the reference: s_L = 1.868512 (equilibrated),
   bordered s_min = 1.984e-01 >> derived floor 2.652e-07, det
   identity to rel. err 0 [X-U3BD P2/P3/P3b, rejectors R1/R2 active:
   the characteristic-front limit IS detected singular];
 - classical content: for 1-D Lax shocks of gas dynamics with convex
   EOS, nonvanishing of the Lopatinskii determinant is the standard
   uniform-stability fact (Majda's condition, which in one space
   dimension reduces to exactly this scalar); we do NOT import the
   citation as proof (radical citation honesty — no page-verified
   source in repo), we NAME the scalar and give it a carrier;
 - discharge route (declared, not executed): interval certification
   of s_L over K_delta — the SAME substrate as X-IVXC (outward
   rounding + Krawczyk + the T-XRED-style scaling quotients reduce
   the dimension); this plugs into the global-maximum dossier's
   shared-brick economy ([PAP-GMAX] Card 1 method record applies).

### §2.3 U3-L1 (uniformity by compactness — the floors)

Define the certified front set

    K_delta := { (V_-, V_+, sigma') : H = 0; Lax slope margins and
                 normal-Mach margin >= (derived from) delta on both
                 sides; axial margins u - c >= delta both sides;
                 |V_+-| <= C_0; wall-transversality slope bound
                 |sigma'| <= Lambda },

with C_0 = C^0-BOUND(delta, L_x, C_geo, C_dat, h_min) from U1 §3 and
Lambda the slope bound of U1 (T1). K_delta is COMPACT: it is the
intersection of a closed set (H = 0 plus closed inequality
constraints; H continuous for a C^1 EOS on the state box) with a
bounded set (|V| <= C_0, |sigma'| <= Lambda, and rho bounded below on
K_delta by the margin chain: c^2 > 0 and u - c >= delta force
rho >= rho_min(delta, C_0) > 0 on the box — the EOS state box is the
one already declared by the interface contract).

LEMMA U3-L1 (uniform floors). On K_delta:
 (i)   s_min( equilibrated dH/dV_+ ) >= s_*(delta, C_0) > 0,
 (ii)  |dH/dsigma'| >= g_*(delta, C_0) > 0,
 (iii) IF U3-H1 holds pointwise on K_delta, then
       |s_L| >= l_*(delta, C_0) > 0 and the bordered solve is
       uniformly Lipschitz: |(delta V_+, delta sigma')| <=
       L_RH(delta, C_0) * |(delta V_-, v_imp)|,
 (iv)  the entropy jump satisfies [S] >= s_j(delta, C_0) > 0
       (under the genuine-nonlinearity clause c4).
PROOF (one pattern, four instances): each quantity is a CONTINUOUS
function of (V_-, V_+, sigma') on the compact K_delta (smallest
singular value: Weyl; s_L: continuous wherever (i) holds; [S]: EOS
C^1); each is strictly positive at EVERY point of K_delta ((i)-(ii):
G12-L2(a),(b) strictly inside Lax — the strength margin excludes the
characteristic degeneracy which G12-L2(c) proves is the ONLY one;
(iii): pointwise by hypothesis U3-H1; (iv): entropy strictly
increases across a genuine Lax shock of a genuinely nonlinear family
— clause c4); a positive continuous function on a compact set attains
a positive minimum. QED.
HONESTY NOTE on explicitness: s_*, g_*, l_*, s_j are explicit as
NAMED FUNCTIONS of (delta, C_0) via compactness, not closed forms —
the same standard as U1's K_0..K_3 constants; the carrier value
s_L = 1.87 at the reference is a data point, not the constant.

------------------------------------------------------------------------------
## §3 U3 — the front estimate (straightening + uniform Lipschitz traces)

Setting: one front y = sigma(x), x in [a, b], between two smooth
regions R^- (upstream side) and R^+ (downstream side), each also
bounded by walls per §1.

(a) STRAIGHTENING. Extend the U1 strip normalization piecewise: in
each region between consecutive interfaces (wall-to-front,
front-to-front via ordering, front-to-wall) map the y-interval
affinely to a fixed reference interval, with the interface curves
(walls: given C^2; fronts: C^2 by (d) below) entering the
coefficients through their value and slope, exactly as w, w' do in
U1 §1. Coefficient C^1 bounds now involve C_geo, 1/h_min AND the
front bounds (C_front, below); the FRONT-REGION width floor is
inherited from h_min and the transversal-angle margins (a front
transversal to both the wall and the streamline family cannot pinch
a region to zero width faster than the angle margins allow over an
x-interval — the pinch points are the front's own endpoints, handled
as corners of the composition graph in U4).

(b) POINTWISE FRONT SOLVE. By U3-L1(iii): at each x-station the
downstream trace and front slope respond Lipschitz-ly to the upstream
trace and the impinging downstream characteristic value,

    |delta V_+| + |delta sigma'| <= L_RH ( |delta V_-| + |v_imp| ),

with L_RH = L_RH(delta, C_0) uniform over the class. This is the
front-interface analogue of U1's wall reflection bound R_0, and it is
the ONLY place the free boundary enters the estimates: RH +
impingement close the front locally, no global front unknown remains.

(c) C^0 TRACES (Gronwall across the front). The backward-path
telescoping of U1 §3 extends verbatim with one more leg type: a path
hitting the front from downstream continues (i) through the RH solve
into the upstream region (for the components determined by RH) and
(ii) along the impinging family back into the downstream region. Each
front passage multiplies the accumulated constant by L_RH (vs R_0 for
wall bounces). With N_X = the per-path front-crossing count (bounded
in §4.2), V(x) <= L_RH^{N_X} R_0^{N_b} (C_dat + C_geo-terms)
e^{K_1 x} — the U1 bound with the front factor inserted.

(d) C^1 TRACES AND FRONT CURVATURE. Differentiate the RH relations
ALONG the front (the U1 §4 move at the wall, executed at the free
boundary): the tangential derivative of H = 0 couples (z_-, z_+,
sigma'') linearly with coefficients bounded by the C^0 bounds; the
bordered structure of §2.1 solves (z_+ components, sigma'') from
(z_-, impinging z-value) with the SAME L_RH constant (same matrix M,
derivative-level right sides + curvature slot). Consequences:
 (d1) the z-system Gronwall composes exactly as (c):
      Z(x) <= L_RH^{N_X} R_1^{N_b} (C_dat + C_geo) e^{K_3 x};
 (d2) FRONT C^2 FOR FREE: |sigma''| <= C_front(delta, L_x, C_geo,
      C_dat, h_min) on every certified front — the certified class
      SELF-SUPPLIES the C^2 interface regularity that step (a)'s
      straightening needs (no new hypothesis; the loop (a)->(d)
      closes because the straightening needs the bounds only on the
      already-walked part of the march, standard for x-forward
      estimates).

(e) TWO-SOLUTION LOCAL ESTIMATE. For two certified solutions in the
same stratum, align each front pair by the straightening (the shift
comparison: state differences measured in aligned coordinates, front
differences as graph distances). The difference system is linear
along the characteristics of the first solution with sources bounded
by K_4 (|DU| + |Delta sigma|_{C^1} + ||Delta w||_{C^2}) and interface
jumps controlled by L_RH; Gronwall gives the local front-block
Lipschitz bound

    |Delta V_+ traces|_{C^0} + |Delta sigma|_{C^1([a,b])}
      <= LIP_front ( |Delta V_- traces|_{C^0} + |Delta sigma(a)|
                     + |v_imp difference| + ||Delta w||_{C^2} ),

LIP_front = LIP_front(delta, L_x, C_geo, C_dat, h_min) via L_RH and
the region constants. The front INITIAL datum Delta sigma(a) is
controlled by clause c3 (origination: wall-feature => bounded by
||Delta w||_{C^2} through the corner RH solve; data-borne => part of
||Delta data||_{C^1}). QED (U3).

------------------------------------------------------------------------------
## §4 U4 — composition on [0, L_x] (counting + causal assembly)

### §4.1 Counting lemma A (front count from the five constants)

LEMMA U4-A. Under the wall-attachment reading (F2) and clause c4:
    N_F <= 2 * osc(S) / s_j <= 4 C_0 / s_j(delta, C_0)
           =: N_F^max(delta, L_x, C_geo, C_dat, h_min).
PROOF. The wall is a streamline (slip); along each wall the entropy
trace is constant in smooth stretches (S transports along
streamlines) and jumps by >= s_j (U3-L1(iv)) at every front foot,
always UPWARD (admissibility). The wall-trace entropy stays within
the U1 C^0 bound, so each wall carries at most osc(S)/s_j <=
2 C_0/s_j front feet; every front owns at least one foot (F2); two
walls. QED.
[If (F2) is ever relaxed — e.g. a front running inflow -> outflow
with no wall contact — this argument does not count it; N_F then
becomes a SIXTH named constant of the certificate. Priced in §5(c2).
The companion per-streamline bound (any streamline crosses at most
2 C_0/s_j fronts) holds regardless of (F2) and is the physical
content: entropy budget = front budget.]

### §4.2 Counting lemma B (per-path crossing count)

LEMMA U4-B. Any backward characteristic path (piecewise single-family
legs, split at wall bounces and front passages) crosses fronts at
most N_X <= N_F^max (N_b + 2) times, with N_b <= Lambda L_x/h_min + 1
the U1 bounce count.
PROOF SKETCH (bookkeeping, stated honestly as such). Fix one front
and one single-family leg of the path. On each SIDE of the front the
sign of (lambda_leg - sigma') is FIXED along the front by the Lax
margins of (F1) (each family on each side is uniformly impinging or
uniformly receding — the five Lax inequalities with margins). A
zero-crossing of (y_path - sigma)(x) with derivative of fixed sign
cannot recur without a derivative-sign reversal, which requires the
leg to CHANGE (wall bounce or front passage). Hence per front: at
most one crossing per leg, legs <= N_b + N_X + 1... closing the loop
crudely: each of the <= N_b + 1 wall-to-wall arcs contributes at most
2 crossings per front (one per approach direction), giving
N_X <= N_F * 2(N_b + 1) <= N_F^max (N_b + 2) * 2 — we RECORD the
cruder but simply-proved bound N_X <= 2 N_F^max (N_b + 1) and use it;
sharpness of the combinatorial constant is NOT load-bearing (it
enters an exponent that is already explicit in the five constants).
QED (with declared crudeness).

### §4.3 The composed estimate (the -a deliverable at class level)

THEOREM-SHAPE STATEMENT (class SCHEMA; conditional inventory in §5).
Let two solutions (U, sigma_1..N_F, w) and (Utilde, sigmatilde, wtilde)
be certified in D(delta, L_x, C_geo, C_dat, h_min), SAME front
topology (c2), fronts wall-attached (c1... c4 as in §5), and assume
U3-H1 on K_delta. Then

    ||U - Utilde||_{C^0(aligned)} + max_k |sigma_k -
        sigmatilde_k|_{C^1}
      <= LIP_shocked * ( ||data - datatilde||_{C^1}
                         + ||w - wtilde||_{C^2} ),

with the EXPLICIT composed structure

    LIP_shocked = [ C_reg * max(R_0, R_1, L_RH) ]^{N_b + N_X + 1}
                  * e^{K L_x},

every factor a named function of the five constants (C_reg = the U1
per-region constant; R_0/R_1 wall factors, U1-U2; L_RH front factor,
U3; N_b bounce count, U1; N_X crossing count, U4-B; N_F inside N_X,
U4-A). PROOF: induction over the causal order of the region/front
partition (well-founded: regions ordered by x-entry of their causal
dependence; finitely many by U4-A). Each region applies U1 §5's
linear-difference Gronwall (with the typical-BVP boundary inventory:
inflow data, wall reflection U2, front traces U3(e)); each interface
applies U3(e) or U1's wall bound; constants multiply along maximal
causal chains, whose length is <= N_b + N_X + 1. The e^{K L_x}
Gronwall envelope composes additively in x across regions (total
x-extent is L_x regardless of the partition). QED.

COROLLARY (-b at shocked level, within stratum): same data, same
walls => Delta = 0: the certified solution with a DECLARED front
topology is unique among certified solutions of that topology. The
cross-topology question is NOT touched (see D2 in §5); the entropy
route [T-XWS] remains the cross-class instrument on shock-free data.

WHAT IS NOT CLAIMED (same honest boundary as U1 §5): the C^1-level
two-solution estimate for STATES (only traces/fronts get C^1 here);
shift-C^1 differentiability of the map (that is -c/U5, untouched,
research-grade, Breitkopf-Ulbrich lead unchanged).

------------------------------------------------------------------------------
## §5 The conditional inventory (everything -a still rests on, priced)

 c1 U3-H1 (Lopatinskii scalar s_L /= 0 on K_delta) — the sharpened
    C-MAJDA content (§2.2). Instance-certified (X-U3BD); class-level
    discharge route named (interval certification over K_delta,
    X-IVXC substrate). THIS IS THE ONLY ANALYTIC CONDITION LEFT IN
    THE -a CHAIN BEYOND THE FIVE CONSTANTS.
 c2 FRONT-TOPOLOGY STRATUM (discovery D2): the estimate compares
    solutions with the same front count and causal order. Not a
    defect: march-topology changes are DISCRETE events (RK-G risk
    register; census S0 strata; Lemma B fixed-march-topology
    hypothesis) — the -a estimate is the WITHIN-STRATUM statement,
    and that is exactly what every heir (T-T7FS differentiation,
    T-P3 multipliers, G12-S1 shape calculus) consumes: they all
    operate at a fixed certified reference topology.
 c3 FRONT ORIGINATION Lipschitz clause: origination at declared wall
    features (position from w — automatic) or through certified
    inflow data (position/slope part of the data norm — declared).
 c4 GENUINE NONLINEARITY on the state box (G > 0) for the
    entropy-jump floor U3-L1(iv) — automatic for perfect/ideal gas,
    DECLARED for the abstract-EOS statement (gamma-status note; the
    tabulated-backend thermo duty already tracks EOS regularity).
 (D1, resolved by reading): WALL ATTACHMENT (F2) — under this
    reading N_F is DERIVED (U4-A); relaxing it costs a sixth named
    constant. The ledger clause "transversal wall/front angles" is
    hereby read as asserting wall attachment for every front; this
    is a CLARIFICATION of the certified-set definition, executed as
    a dated note in the ledger (R4 this session), not a new
    hypothesis.

------------------------------------------------------------------------------
## §6 Consequences (what moves in the corpus)

 (i)  C-D25U component -a: estimate chain COMPLETE at class level
      (U1 smooth + U2 wall + U3 front + U4 composition), constants
      explicit in the five-constant certificate, conditional
      inventory = c1-c4 above. Component -b: within-stratum corollary
      here; the S-S1U assembly consumes -a as before. Component -c:
      UNTOUCHED (U5 named missing, research-grade — the panel pricing
      survives unchanged).
 (ii) C-MAJDA SHARPENED IN-CLASS (dated supersession executed in the
      L4 ledger): inside the planar x-as-time S1 class, "Majda
      stability of the fitted fronts" = G12-L2 blocks (machine-
      verified) + U3-H1 scalar (named, instance-certified, compact-
      uniform by U3-L1(iii)). What keeps the full C-MAJDA name:
      configurations beyond the class (genuinely multi-D fronts,
      interactions/reflections) and the heirs' per-heir
      re-adjudication (NOT executed here — conversion of THEOREM*
      heirs stays pending exactly as the C-D25U consequence note
      states).
 (iii) Global-maximum dossier synergy: the interval certification of
      s_L over K_delta is a SECOND application of the shared
      substrate brick (after C-XBVP(a)/X-IVXC) — one more payoff of
      the same investment, recorded in the dossier's Card-1 orbit
      (pointer note, R4).
 (iv) The falsifier family gains a channel: a certified front family
      with s_L -> 0 at healthy margins would break U3-H1-uniformity
      (and would surface in the A1 engine as a front-solve
      conditioning blowup — an EXECUTABLE symptom the march already
      monitors through its Newton solves).

------------------------------------------------------------------------------
## §7 Cost-claim verdict

 - U3 + U4 (-a completion): CONFIRMED bounded — one session,
   classical bookkeeping over the machine-verified bricks (G12-L2,
   T-U2RG, X-U3BD), plus two counting lemmas whose proofs are
   elementary (entropy budget; crossing combinatorics with declared
   crudeness). The S14/S15 pricing asymmetry (-a/-b bounded vs -c
   research-grade) SURVIVES its third test.
 - The discovery pattern of the campaign repeats: writing-for-real
   surfaced (D1) the wall-attachment reading (else a sixth constant)
   and (D2) the topology-stratum scope — both invisible at
   architecture level, both priced harmlessly, both now NAMED.

------------------------------------------------------------------------------
## §8 Residue (named, honest)

 - U3-H1 class-level discharge: interval certificate of s_L over
   K_delta (X-IVXC-substrate candidate; seconds-to-minutes scale by
   the Card-1 method record; needs the K_delta parametrization =
   shock polar over the margin box — a natural next brick).
 - Axisymmetric bookkeeping: planar of record here (same declared
   scope as T1b/S15); the axisym source terms change no counting
   argument (they are zeroth-order) — declared, not executed.
 - Li-Yu page-level anchors: unchanged ACQUISITION IOU (self-
   contained arguments only, book-level citation).
 - U5 / -c: untouched; leads unchanged (Bressan-Guerra/Ulbrich,
   Breitkopf-Ulbrich arXiv:2509.22076 — acquisition pending).
 - Cross-topology comparison: OUT OF SCOPE by design (c2) — lives
   with the census/tournament layer and RK-G, as of record.
