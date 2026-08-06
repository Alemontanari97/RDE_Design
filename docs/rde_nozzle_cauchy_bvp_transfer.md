# The Cauchy->steady-BVP transfer — relative entropy in x (T-XWS)

Status: RIGOR ATTACK OF RECORD (2026-08-05, S15 deep-foundations
campaign, [RIGOR/A]; PROGRESS NEXT-1 item "lemma Cauchy->BVP
(entropia relativa in x)"). Closes the declared analytic soft spot of
shock-free canonicity (D2.5): the corpus cited TIME-formulation
weak-strong uniqueness (Dafermos; Brenier-De Lellis-Székelyhidi), but
for a steady BVP the time-Cauchy datum is the WHOLE field at t = 0 —
which presupposes the solution. The right frame is x-as-time, where
the datum is the inflow section only and the walls become "moving
boundaries" of the x-evolution. That transfer was PLAUSIBLE and
unwritten (S14 panel, PDE lens); it is written here.
Carrier: [X-XBVP] `validation/xbvp_entropy_transfer.py` (VERDICT PASS:
P1/P2 symbolic at ABSTRACT EOS, P3/P4 ideal-gas instance, rejectors
R1/R2). Registry: [T-XSON], [T-XWALL], [S-XCONV], [T-XWS], [C-XBVP],
[X-XBVP].

Audit line: [Class: mixed — T-XSON THEOREM, T-XWALL THEOREM (both
symbolic-sufficient, machine-verified at abstract EOS), S-XCONV
SCHEMA (structure symbolic, definiteness instance-certified), T-XWS
THEOREM* inheriting C-XBVP | Falsifiers: per-brick, see §8 |
Carrier: X-XBVP (suite group (xiii)) | Gamma: EOS-general throughout
(abstract p(rho,S), e(rho,S) with Gibbs closure e_rho = p/rho^2,
e_S = theta; ideal gas used ONLY as declared instance/oracle for the
definiteness samples)].

NOVELTY STATUS (radical honesty): NOT claimed novel. Relative-entropy
weak-strong uniqueness is Dafermos-DiPerna technology; steady-frame
(x-as-time) applications exist in the steady-supersonic literature.
A query-bounded novelty sweep for the WALL LEMMA of §4 (slip-wall
relative-entropy flux annihilation, abstract EOS) is REQUIRED before
any paper claim: candidate queries logged in §8. Until then the
lemma's value here is INTERNAL (it closes our named soft spot).

------------------------------------------------------------------------------
## §1 Setting: the x-as-time system and its hyperbolic branch

Steady 2-D Euler in a nozzle domain Omega = {(x, y): 0 <= x <= L,
w_-(x) <= y <= w_+(x)} (planar; axisymmetric extension declared in
§8), state U = (rho, u, v, S), EOS-general:

    d_x m(U) + d_y n(U) = 0,
    m = (rho u, rho u^2 + p, rho u v, rho u H),
    n = (rho v, rho u v, rho v^2 + p, rho v H),

p = p(rho, S), c^2 = p_rho|_S, H = e + p/rho + (u^2+v^2)/2.
On the axially supersonic branch u > c (the [T-NSW] spacelikeness
condition, frame-invariant) this is a hyperbolic system of four
conservation laws with x as the evolution variable and m as the
conserved "state".

[T-XSON] LEMMA (sonic bijection). det(dm/dU) vanishes IDENTICALLY at
u = c and at u = 0, at ABSTRACT EOS (carrier P1, symbolic); on the
branch u > c > 0 the map U -> m is a local diffeomorphism (numeric
nonvanishing on the sampled branch, carrier). Hence "m as state" is
legitimate exactly where the march is legitimate: the sonic line is
simultaneously the marching boundary AND the state-space fold — one
margin (u - c >= delta) buys both.

------------------------------------------------------------------------------
## §2 The entropy structure in x

For ANY g(S), the pair

    eta = -rho u g(S),      q = -rho v g(S)

is an entropy pair of the x-system: on smooth solutions
d_x(rho u g) + d_y(rho v g) = 0 (S-transport), and across admissible
fronts the physical entropy condition (S nondecreasing along
particle paths crossing the front, mass flux positive) gives
d_x eta + d_y q <= 0 in D' for g' > 0. The carrier verifies the pair
identity D_U q = D_m eta . D_U n on the branch (P3, 40 random states,
machine precision).

[S-XCONV] SCHEMA (convexity from the supersonic margin). CLAIM
(target THEOREM): with g(S) = S, eta = -rho u S is STRICTLY CONVEX as
a function of m on the axially supersonic branch, uniformly on
compacts with margin u - c >= delta; convexity FAILS (indefinite
Hessian) for u < c, and the sonic line u = c is EXACTLY the
definiteness boundary.
EVIDENCE OF RECORD (carrier, ideal-gas instance gamma = 1.4):
 - P4a: 200/200 randomized states on the declared margin box
   (rho in [0.5, 2], S in [-0.5, 0.5], u/c in [1.15, 3],
   |v| <= 0.8 c): pushforward Hessian positive definite
   (lambda_min_worst 1.36e-4 in the sampled scaling).
 - FINDING of record: definiteness held with the AXIAL margin alone —
   |v| up to 0.8c never broke it: the convexity condition tracks
   u_x > c ([T-NSW] spacelikeness), NOT total-speed supersonicity
   |u| > c. (Consistent with the x-evolution reading; recorded as an
   instance-level observation, not a theorem.)
 - R1: 60/60 subsonic-in-x states INDEFINITE — no convex extension
   across the sonic line exists for this eta.
 - R2 (sonic pincer): at u = (1 +- eps)c, eps = 1e-2, 1e-3, three
   base states: definite above, indefinite below — the boundary is
   the sonic line to the resolution tested.
STATUS: structure symbolic, definiteness instance-certified =>
SCHEMA; the discharge to THEOREM (a proof over the whole certified
compact, interval-arithmetic candidate) is component (a) of [C-XBVP].
[STATUS UPGRADE, dated 2026-08-05 (S15 reopened segment): the
interval candidate EXECUTED — [X-IVXC] certifies strict definiteness
over the WHOLE declared (M, V) box, and by the [T-XRED] reduction
below for EVERY (rho, S): C-XBVP(a) DISCHARGED at the ideal-gas
instance level (43199 boxes, deterministic budget, VERDICT PASS;
declared libm assumption in the carrier). The abstract-EOS statement
remains the schema residue.]

[REDUCTION LEMMA, dated 2026-08-05 (S15 reopened segment, [T-XRED],
carrier X-IVXC P4/P5 — the substrate brick's own discovery): on the
ideal-gas instance the definiteness of H_m(eta) is a function of the
MACH PAIR (M, V) = (u/c, v/c) ALONE. Proof: two scaling groups act
on the state — s_alpha (pressure-density scaling at fixed c:
rho -> alpha rho, S -> S - (gamma-1) ln alpha) gives m -> alpha m
and eta -> alpha eta + (gamma-1)(ln alpha) m_1; s_beta
(velocity-sound scaling: u,v -> beta u, beta v, S -> S + 2 ln beta)
gives m -> diag(beta, beta^2, beta^2, beta^3) m and eta ->
beta eta - 2 (ln beta) m_1. In both cases eta gains only a term
LINEAR in m (zero m-Hessian), so H_m(eta) transforms by POSITIVE
DIAGONAL CONGRUENCE — definiteness invariant along both orbits,
which sweep all (rho, S) at fixed (M, V). Both identity sets are
machine-verified symbolically (X-IVXC P4/P5, corrupted-diagonal
rejector R4). CONSEQUENCES: (i) the §2 instance FINDING
("definiteness tracks u_x > c, not |u| > c") is now EXPLAINED — the
invariant content lives in the Mach pair; (ii) the C-XBVP(a)
certification domain collapses from the 4-D box to its 2-D
(M, V)-slice at one representative (rho, S) = (1, 0) — measured to
be the difference between an infeasible and a feasible interval
certificate (method record in the carrier docstring).]

------------------------------------------------------------------------------
## §3 Boundary inventory for the BVP

The x-evolution on the nozzle domain has three boundary types:
 (i)   INFLOW x = 0 (the interface Gamma_d data, axially supersonic
       by the stage-A audits): the x-Cauchy datum; equal for the two
       solutions being compared — contributes zero relative entropy.
 (ii)  WALLS y = w_+-(x), slip (u.n = 0, i.e. v = w' u): "moving
       boundaries" of the x-evolution — the soft spot the time
       formulation never faces. Handled by the WALL LEMMA (§4).
 (iii) OUTFLOW x = L: no condition needed (the estimate integrates
       up to any x <= L; supersonic outflow radiates nothing back —
       exactly the H2' ambient-blindness).

------------------------------------------------------------------------------
## §4 The wall lemma (the decisive brick)

[T-XWALL] LEMMA (slip-wall relative-entropy flux annihilation;
THEOREM, EOS-general, every g). Let U (strong) and V (any state with
the same slip condition at the same wall y = w(x)) lie on the
hyperbolic branch. The relative-entropy flux through the wall,

    W := [q - w' eta](V) - [q - w' eta](U)
         - D_m eta(U) . [ (n - w' m)(V) - (n - w' m)(U) ],

vanishes IDENTICALLY.

PROOF (two halves, both verified in the carrier at abstract EOS):
(1) The direct fluxes: q - w' eta = -g(S) (rho v - w' rho u) =
    -g(S) rho u (v/u - w') = 0 for EVERY state satisfying slip —
    both direct terms vanish separately.
(2) The cross term. At slip, the boundary flux of the conservation
    system reduces to pure pressure:
       (n - w' m)|_slip = (0, -w' p, p, 0) = p (0, -w', 1, 0):
    mass and energy rows vanish (both are rho(v - w'u)-multiples),
    momentum rows leave the pressure. So the difference is
    (p_V - p_U)(0, -w', 1, 0) — ONE direction d, fixed by the wall
    geometry. Solve J dU = d for the induced state increment
    (J = dm/dU): the first row gives d(rho u) = 0 (mass flux frozen);
    energy row then gives dH = 0; the momentum rows combine with
    dh = theta dS + dp/rho to
       theta dS = (w' u - v)/(rho u) = 0   at slip.
    Hence D_m eta . d = -g(S) d(rho u) - rho u g'(S) dS = 0 for
    EVERY g and EVERY EOS. QED.
    (Carrier P2 solves J dU = d symbolically at abstract EOS and
    confirms dS == 0 and d(rho u) == 0 on the slip locus.)

READING: the admissible flux perturbation at a slip wall is
ISENTROPIC AT CONSTANT MASS FLUX — and every g(S)-based entropy is
blind to exactly that combination. The wall costs NOTHING in the
relative-entropy budget: the x-transfer of the Dafermos argument is
boundary-clean. This is the analytic reason slip walls do not
obstruct canonicity — previously a plausibility, now a lemma.

------------------------------------------------------------------------------
## §5 The transfer theorem

[T-XWS] THEOREM* (weak-strong uniqueness in x; canonicity of the
shock-free supersonic-margin solution; inherits [C-XBVP]).
HYPOTHESES: U a C^1 solution of the steady system on Omega with
uniform axial margin u - c >= delta > 0 and slip walls; V an entropy
weak solution of the x-system on Omega (values in a compact K of the
hyperbolic branch on which S-XCONV definiteness holds, entropy
inequality d_x eta + d_y q <= 0 for the §2 pair, slip trace on the
walls, x-slice normal traces per C-XBVP(b)) with THE SAME inflow
data at x = 0.
CLAIM: V = U a.e. on Omega.
PROOF (Dafermos computation transplanted; each step names its
ingredient). Set the relative entropy/flux
   eta(V|U) := eta(V) - eta(U) - D_m eta(U)(m_V - m_U),
   q(V|U)   := q(V) - q(U) - D_m eta(U)(n_V - n_U).
Integrate the entropy inequality of V against 1, subtract the smooth
identities of U, and use the C^1 regularity of U to write, for a.e.
x1 in (0, L]:
   Int_{y} eta(V|U)(x1) dy
     <= Int_{y} eta(V|U)(0) dy                          [= 0: same data]
      + Int_0^{x1} [walls: q - w' eta relative flux] dx  [= 0: T-XWALL]
      - Int_0^{x1} Int_y  dD_m eta(U) : Q(V, U)  dy dx,
where Q collects the standard quadratic commutator
(F(V) - F(U) - DF(U)(V-U) paired against derivatives of U). On the
compact K: strict convexity (S-XCONV) gives
c_K |m_V - m_U|^2 <= eta(V|U) <= C_K |m_V - m_U|^2, and the flux
Lipschitz bounds give |Q| <= C'_K |m_V - m_U|^2 <= (C'_K / c_K)
eta(V|U). With ||dU||_inf =: G (the C^1 bound of the strong
solution), Gronwall in x yields
   Int eta(V|U)(x1) <= e^{G C x1} Int eta(V|U)(0) = 0,
hence m_V = m_U a.e., hence V = U by T-XSON (bijection on the
branch). QED (modulo the two C-XBVP components: (a) definiteness on
all of K proven, not sampled; (b) the trace/regularity technicalities
of the weak side).

CONSEQUENCE (the canonicity payoff, stated for the record): if the
certified class contains a C^1 shock-free solution with margin, then
NO OTHER entropy solution — INCLUDING SHOCKED ONES — exists with the
same inflow data in the class of the theorem: shocked alternatives
are excluded BY THEOREM, not by declaration. The D2.5 sentence
"weak-strong uniqueness makes the classical solution THE solution"
now has a BVP-native proof skeleton with named residuals, replacing
the time-formulation citation whose Cauchy datum (the whole field at
t = 0) presupposed the solution.

------------------------------------------------------------------------------
## §6 The named conditional

[C-XBVP] (stated ONCE in the ledger, docs/
rde_nozzle_remaining_conditionals.md §1bis; components):
 (a) S-XCONV discharge: strict convexity of eta(m) on the whole
     certified compact K with margin (instance-certified now;
     interval-arithmetic proof over the box = the natural discharger,
     connects to the T4 global-maximum toolbox).
 (b) weak-side technicalities: x-slice normal traces and wall traces
     for the entropy solution class (Dafermos-class bookkeeping;
     strong traces available in BV; the strong side is C^1 and free).
Neither component touches the ALGEBRAIC content (T-XSON, T-XWALL,
pair identity): those are THEOREM now, at abstract EOS.

------------------------------------------------------------------------------
## §7 Consequences for the corpus

 - D2.5 CANONICITY (shock-free): upgraded from "cited time-frame
   weak-strong" to "BVP-native transfer theorem T-XWS with named
   residuals C-XBVP(a,b)" — the S1-boundary risk concentration of
   the S14 panel is REDUCED on its shock-free flank (the -c/U5 flank
   of C-D25U is untouched: that is STABILITY of the map, not
   uniqueness of the solution — different objects, both needed).
 - The margin delta buys THREE things with one hypothesis (axis-B
   economy): marching legitimacy (T-NSW), state-space bijection
   (T-XSON), and entropy convexity (S-XCONV) — the certified-set
   margin is not bureaucracy, it is the single load-bearing constant.
 - The instance FINDING that definiteness tracks u_x > c (not
   |u| > c) sharpens the physical reading: the swirl-heavy RDE
   wave-frame flow (strongly helical, [T-NSW]) still has the convex
   x-entropy wherever the AXIAL margin holds — the transfer frame is
   compatible with the program's interface contract as declared.
 - Relation to [C-MAJDA]: T-XWS speaks only where the strong
   comparison solution is C^1; canonicity ACROSS fitted fronts
   remains the declared conditional backed by Majda stability —
   unchanged, and now cleanly separated from the shock-free question.

------------------------------------------------------------------------------
## §8 Honesty ledger (scope, falsifiers, acquisitions)

NOT claimed: existence (P7/D-S1 territory); canonicity across fronts
(C-MAJDA); 3-D/swirl transfer (the x-system here is planar 2-D);
uniqueness outside the branch-valued class K; any novelty (§0 note).
DECLARED extension: axisymmetric annulus — geometric source terms
s(U)/y with y >= r_in > 0 are Lipschitz on K; they enter the Gronwall
constant and NOTHING else (the wall algebra and the pair identity are
pointwise and source-free); writing it out is bookkeeping, declared
not done.
FALSIFIERS: T-XSON/T-XWALL — carrier symbolic checks (a nonzero
dS_slip at any EOS instance kills T-XWALL); S-XCONV — R1/R2 (a
definite subsonic Hessian or an indefinite margin-box state kills
the schema); T-XWS — a certified numerical BVP case (A1 engine) with
two distinct entropy solutions on identical inflow data inside K
would kill the theorem and with it the class architecture (executable
once A1 runs capturing-mode controls, X1 design).
ACQUISITION QUERIES (novelty bound, to run with G5-class sweeps):
"steady supersonic Euler relative entropy weak-strong"; "convex
entropy steady supersonic flow x hyperbolic"; "slip wall relative
entropy boundary term"; Dafermos Hyperbolic Conservation Laws (4th
ed.) §5.3 context check.
