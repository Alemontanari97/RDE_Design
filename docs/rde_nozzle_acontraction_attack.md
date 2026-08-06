# The a-contraction attack on C-MAJDA/U3 — shifted relative entropy
# in the x-as-time frame (attack of record, followed to where it leads)

Status: RIGOR ATTACK OF RECORD (2026-08-06, S16 deep-foundations
campaign second tranche, T2 [RIGOR/A]). Mandate: follow the
a-contraction / shifted-relative-entropy line (the "Vasseur-Krupa
line, essentially 1-D" already named as partial support in M0 D2.5)
into the program's own frame, to wherever it leads; honest verdict
either way; classes declared; no numbers without a carrier.
Registry: [S-ACFR] (the derived front condition + assembly schema),
[X-ACFR] validation/acontraction_front_probe.py (sampling PROBE —
declared: probe, not certificate; suite group (xiii)).

Audit line: [Class: SCHEMA (the balance-set reduction §3 is derived
self-containedly; the assembly §5 has named gaps; nothing here is
cited as proven from external literature — the "Vasseur-Krupa line"
is a METHOD-LINE pointer of record, no theorem attributions, no
equation numbers, G5-class novelty/priority sweep = declared IOU) |
Falsifier: the carrier's rejectors + the named certification brick
B1 (§6) | Carrier: X-ACFR | Gamma: EOS-general structure; probe =
declared perfect-gas instance with g(S) = S].

VERDICT UP FRONT: the line TRANSPLANTS, and the known crux — the
front term — is INSTANCE-FEASIBLE at the certified reference with an
explicit weight window (r = a_-/a_+ in approx. [3.2, 47], best
margin at r about 6.8; carrier-backed §4), while the probe
DISCRIMINATES: the reversed, entropy-violating front is infeasible
for every weight. The method's price in this frame is ONE structural
clause (competitor confinement to the certified convexity box) plus
bookkeeping already priced elsewhere (C-XBVP(b)-class traces). What
a completed a-contraction would buy is EXACTLY what U3/U4 could not:
stability of SHOCKED S1 references against ARBITRARY weak in-box
competitors — the cross-topology gap (U3/U4 clause c2) and the
canonicity license of C-MAJDA at the weak level. Not closed here:
the class-level certification of the front condition is a NAMED
brick on the shared interval substrate (§6). This is a POSITIVE
verdict with declared distance-to-goal — not a discharge.

------------------------------------------------------------------------------
## §1 The transplant (method ingredient -> program object)

| a-contraction ingredient | x-as-time BVP object | status |
|---|---|---|
| 1-D system, x as time | steady 2-D Euler read as y-line evolution (G12-L1, x-as-time of record) | STRUCTURAL MATCH |
| extremal Lax shock | fitted acoustic front: the acoustic families ARE the extreme eigenvalues (lambda_- < lambda_0 = lambda_0 < lambda_+; the streamline double family is linearly degenerate — contacts, not shocks) | STRUCTURAL MATCH (the method's positive territory is extremal shocks; intermediate-family obstructions do not arise in this class) |
| convex entropy | the x-entropy family eta = -rho u g(S): strictly convex in the x-flux m on the certified (M, V) box — CERTIFIED (X-IVXC + T-XRED, every (rho, S)) | MATCH ON THE BOX (the confinement clause, §2 H3) |
| shift X(t) | the front graph sigma(x) perturbation: the fitted-front free-boundary dof IS the shift — the method's artificial device is this program's native unknown | STRUCTURAL GIFT |
| weight a(x) piecewise constant | a(y) jumping at the shifted front | AS IN METHOD |
| boundary terms | slip walls: relative-entropy flux vanishes IDENTICALLY, every g, abstract EOS ([T-XWALL] of record) | STRUCTURAL GIFT (the BVP version is boundary-FREE — cleaner than the Cauchy setting) |
| competitor class | weak entropy solutions of the SAME BVP data (inflow + walls), confined to the certified box | THE PRICE (§2 H3) |

------------------------------------------------------------------------------
## §2 Method hypotheses vs the certified class (each priced)

 H1 (frame) 1-D hyperbolic with x as time: HOLDS on the axial-margin
    class (u - c >= delta; T-XSON bijection, G12-L1). SATISFIED.
 H2 (entropy pair) (eta, q) = (-rho u g(S), -rho v g(S)) is a genuine
    entropy pair of the x-as-time system: dq/dU = Deta . dgy/dU
    MACHINE-VERIFIED at machine precision (X-ACFR P0). SATISFIED
    (instance g = S; the g-family freedom is a program lever, §6 B3).
 H3 (convexity/confinement) eta strictly convex in m ONLY on the
    axial-supersonic set; certified on the (M, V) box [1.15, 3] x
    [-0.8, 0.8] (X-IVXC). The method therefore compares against
    competitors CONFINED to the certified box — a REAL class
    restriction (a weak competitor with a subsonic pocket exits the
    convexity domain and the relative entropy loses coercivity).
    PRICED: this is the a-contraction analogue of the C-XBVP(b)
    weak-side scoping; stated as the CONFINEMENT CLAUSE of every
    statement in this line. [Honesty: T-XWS carries the same
    in-class scoping; nothing new is lost, but nothing is gained on
    escape-from-class either.]
 H4 (front term sign with weights + shift) THE CRUX — reduced in §3
    to a finite-dimensional condition and probed in §4. OPEN at
    class level (named brick B1), FEASIBLE at instance.
 H5 (interior/trace bookkeeping) entropy inequality in x for the
    weak competitor, strong traces at the front and x-slices:
    Dafermos-class bookkeeping = C-XBVP(b) territory, already priced
    in the ledger §1bis. PRICED (inherited, not new).
 H6 (data terms) same inflow data => the x = 0 term of the relative
    entropy vanishes; the outflow term has the dissipative sign on
    the margin class (flux convexity). SATISFIED (margin class).

------------------------------------------------------------------------------
## §3 The front term, derived (self-contained; the balance-set reduction)

Setting: reference = certified S1 solution with one front y =
sigma(x) (upstream side above, states -> V_-; downstream below, ->
V_+); competitor u = weak entropy solution, same data, in-box (H3);
weight a(y) = a_- above / a_+ below the SHIFTED interface Y(x);
functional

    E(x) = Int_{wall_-}^{Y} a_+ eta(u | ref_+) dy
         + Int_{Y}^{wall_+} a_- eta(u | ref_-) dy .

Differentiate in x; use the competitor's entropy inequality
(d_x eta_rel + d_y q_rel <= interior remainder — H5), the wall
annihilation ([T-XWALL] — no boundary terms), and collect the
interface contributions at Y (the competitor trace u = u(Y) is the
same from both sides a.e. in x; the x-set where the competitor
carries its own front exactly at Y is handled by the shift choice —
bookkeeping, declared). With eta^± := eta(u|V_±), q^±_rel :=
q_rel(u; V_±) (relative pair built on the m-gradient of eta at V_±):

    FRONT TERM  FT = a_+ [ Y' eta^+ - q^+_rel ]
                   + a_- [ q^-_rel - Y' eta^- ]   , need FT <= 0.

FT is LINEAR in the shift velocity Y' with slope (a_+ eta^+ -
a_- eta^-). Wherever the slope is nonzero, Y' can be chosen to make
FT <= 0 pointwise (the shift absorbs the front term — the method's
engine, and in this frame Y' is literally a front-graph slope
perturbation, bounded choices sufficing away from the balance set).
The UNREMOVABLE obstruction is the BALANCE SET where the slope
vanishes:

    B_r = { u in box : eta(u|V_+) = r * eta(u|V_-) },  r = a_-/a_+,

on which FT = a_- q^-_rel - a_+ q^+_rel independently of Y'. Hence:

  THE FRONT CONDITION (the H4 crux, finite-dimensional):
    there exists r > 0 such that
    psi_r(u) := q_rel(u; V_+) - r * q_rel(u; V_-)  >=  0
    for ALL u in B_r (intersected with the certified box).

This is a condition on (V_-, V_+, sigma'-free!) and the box only —
NOTE the front slope drops out on the balance set (the Y'-terms
cancel there exactly); sigma' re-enters only through which pairs
(V_-, V_+) are RH-connected. DERIVATION HONESTY: this reduction was
derived here from scratch (the first attempted two-sided quadratic
localization was WRONG — the balance set does not pass near V_±, the
condition is inherently non-perturbative at O(1) front strength;
deviation declared, the failed route not used).

------------------------------------------------------------------------------
## §4 Instance verdict (carrier-backed; the only numbers in this doc)

Carrier [X-ACFR] (validation/acontraction_front_probe.py, VERDICT
PASS, deterministic seed, derived floors; PROBE: sampled balance
sets, min over samples — NOT an inf-certificate):
 - P0 pair compatibility: worst relative residual 1.65e-16 (machine
   precision) — (eta, q) is a genuine entropy pair of the frame.
 - P1 convexity cross-check: eta_rel >= 0 at all 20000 in-box
   samples wrt both V_- and V_+ (min scaled 5.8e-04 / 9.6e-04 > 0) —
   consistent with the X-IVXC certificate.
 - P3 THE SCAN at the certified oracle front (M1 = 2.5, beta = 40
   deg; the X-G12/X-U3BD reference): the front condition is
   FEASIBLE on a weight window — infeasible for r <~ 3 (min psi < 0,
   e.g. -2.0e-01 scaled at r = 0.68), feasible for r in approx.
   [3.2, 47] (6 of 16 sampled r-values; best margin +4.33e-02 scaled
   at r = 6.8). The upstream side must be weighted MORE (a_- > a_+)
   — a definite, reproducible structural signature.
 - R1 DISCRIMINATION: the reversed front (V_+ upstream = entropy-
   violating expansion shock) is INFEASIBLE for EVERY r — the
   condition genuinely separates admissible from inadmissible
   fronts (a probe that passed both would be vacuous; this one does
   not).
 - R2: the m-gradient correction term in q_rel is live (corrupting
   it shifts the landscape by 6.0e-01 scaled).

------------------------------------------------------------------------------
## §5 What a completed a-contraction buys — and what is still missing

BUYS (the reason this attack matters): a weighted-contraction
inequality E' <= C E for the shocked reference against ARBITRARY
in-box weak competitors of the same data gives stability/uniqueness
of the SHOCKED S1 solution in the weak class — i.e. exactly the two
things the linearized chain cannot reach:
 (i)  the CROSS-TOPOLOGY gap: U3/U4's two-solution estimate is
      within-stratum (clause c2 of [S-D25U-U34]); the a-contraction
      competitor is topology-free (any in-box weak solution);
 (ii) S1 CANONICITY ACROSS FRONTS: the C-MAJDA licensing at the weak
      level (D2.5's declared conditional), for which the linearized
      U3-H1 scalar is the infinitesimal shadow.
It is COMPLEMENTARY to T-XWS (which covers shock-free references)
and to U3-H1 (linearized): three instruments, three regimes.

STILL MISSING (named, honest):
 M1 class-level front condition: psi_r >= 0 on B_r for all certified
    RH pairs in K_delta with a UNIFORM weight window — a
    finite-dimensional certification job (brick B1, §6).
 M2 assembly: Gronwall of the interior remainders (reference smooth
    parts vary), multiple fronts (weights compose per front — the
    U4 counting lemmas apply verbatim), trace bookkeeping (H5).
    Function-space, U1-grade bookkeeping — bounded, none research-
    grade ON THE MARGIN CLASS.
 M3 the confinement clause (H3) is load-bearing and NOT removable by
    this method alone (relative entropy needs convexity); escape
    from the box stays with the census/monitor layer.
 M4 the g-lever: the probe ran g(S) = S; the certified entropy is a
    FAMILY (every g with the record's monotonicity). Whether g-choice
    widens the weight window or the feasible front set is UNPROBED
    (brick B3) — a genuinely program-specific degree of freedom the
    literature line does not have.

------------------------------------------------------------------------------
## §6 Verdict of record + named next bricks

VERDICT: the a-contraction line is VIABLE-IN-CLASS at instance level
and structurally BETTER-POSED in this frame than in its native
Cauchy setting (walls free by T-XWALL; shift = native dof; extremal
fronts only). It is hereby ADOPTED AS A NAMED ROUTE (not a result):
no claim of C-MAJDA discharge is made; the route's completion is
gated on:
 B1 CERTIFICATION BRICK (decisive, interval substrate): certify
    psi_r >= 0 on B_r over the certified front set K_delta with a
    uniform r-window — same outward-rounded machinery as X-IVXC
    (Card-1 method record applies: reformulation beats budget);
    THIRD payoff of the shared substrate investment if executed.
 B2 ASSEMBLY LEMMA (function-space, bounded): FT + interior
    Gronwall + multi-front composition via the U4 counting lemmas.
 B3 g-SCAN (cheap): X-ACFR extension over a g-family; report
    whether the window widens (axis-B content: hypothesis
    minimization via entropy choice).
QUERY DUTY (novelty honesty): "a-contraction / shifted relative
entropy for steady supersonic Euler BVP / spatial evolution" is a
G5-class query IOU — transplant novelty is NOT claimed pending that
sweep; the derivation §3 is recorded as self-contained regardless.

------------------------------------------------------------------------------
## §7 Claim register

| Claim | Class | Carrier / falsifier |
|---|---|---|
| Transplant table §1 (frame, extremal, entropy, shift, walls) | THEOREM-grade per cited record IDs (G12-L1, T-XSON, T-XWALL, X-IVXC/T-XRED) | existing carriers |
| Pair property of (eta, q) in x-as-time | instance THEOREM (machine) | X-ACFR P0 |
| Balance-set reduction of the front term (§3) | SCHEMA (derived; trace/shift bookkeeping declared) | B2 falsifies if assembly fails |
| Front condition feasibility at the oracle, weight window r ~ [3.2, 47] | PROBE FINDING (declared: sampled, not certified) | X-ACFR P3/R1/R2; B1 supersedes |
| Route adoption (viable-in-class, gated on B1-B3) | PRACTICE (dossier-style card) | B1 VERDICT gates it |
