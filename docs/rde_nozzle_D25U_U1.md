# D2.5-U step U1, written for real — smooth-region semiglobal estimates
# (Li-Yu instantiation with wall; the cost-claim test)

Status: RIGOR ATTACK OF RECORD (2026-08-05, S15 deep-foundations
campaign, [RIGOR/A]; S14 panel recommendation 7 executed: "Write U1
once, actually — tests the C-D25U cost claim at one-session price").
This document executes step U1 of the D2.5-U proof architecture
(ledger docs/rde_nozzle_remaining_conditionals.md §1; namespace:
D2.5-U U1, NOT 10bis U1) at the smooth-region-with-wall level, and
returns the VERDICT on the cost claim (-a/-b = "bounded: classical
2-variable bookkeeping"). Registry: [S-D25U-U1].

Audit line: [Class: SCHEMA (function-space estimates, proof written
at full detail below; no symbolic carrier by the sufficiency
discipline — declared) | Falsifier: the C-D25U falsifier (certified
family with blowing Lipschitz constant at healthy margins) plus the
NEW h_min channel of §7 | Carrier: none (function space); the
eigenstructure algebra it rests on is machine-verified in X-G12/X-N6
| Gamma: EOS-general (only the eigenstructure and Gibbs relations
enter; both verified at abstract c^2)].

VERDICT UP FRONT (for the reader of record): the cost claim is
CONFIRMED WITH ONE DISCOVERY — the work is classical and bounded, no
new mathematics is needed, BUT the certified-set definition
D(delta, L_x, C_geo, C_dat) is INCOMPLETE as stated: the estimates
require a DUCT-WIDTH FLOOR h_min > 0 (else the acoustic bounce count
is unbounded and the composed constant blows up). Amendment executed
this session (ledger §1 + registry C-D25U scope). Details in §7.

------------------------------------------------------------------------------
## §1 Setting and normalization

Smooth region between consecutive fronts (or the whole shock-free
domain): Omega = {0 <= x <= L_x, w_-(x) <= y <= w_+(x)}, planar
steady 2-D Euler, EOS-general, U = (rho, u, v, S), axially
supersonic with margin: u - c >= delta > 0 on Omega. Certified-set
bounds: walls ||w_+-||_{C^2} <= C_geo; inflow data ||U(0,.)||_{C^1}
<= C_dat; AMENDED (this session): width floor
w_+(x) - w_-(x) >= h_min > 0.

Domain normalization (standard, needed for the two-solution estimate
where walls differ): yhat = (y - w_-(x)) / h(x), h = w_+ - w_-, maps
Omega to the strip [0, L_x] x [0, 1]. The transformed system is
quasilinear hyperbolic in (x, yhat) with coefficients depending on
(U, w_+-, w'_+-, h); coefficient C^1 bounds involve C_geo and 1/h_min
— the FIRST appearance of the width floor, already at the bookkeeping
level.

------------------------------------------------------------------------------
## §2 Characteristic form (the machinery U1 runs on)

Eigenstructure of the x-evolution (machine-verified algebra: X-G12
A-part for the pencil, X-N6 A2 for the factorization with the same
meridional structure): the pencil det(B - lambda A) factors as
(v - lambda u)^2-type streamline factor times the acoustic bracket;
on u - c >= delta the four characteristic slopes are real and finite:

  lambda_0 = v/u  (multiplicity 2: transports S and H),
  lambda_+- = tan(theta +- mu),  tan mu = c / sqrt(q^2 - c^2),

q^2 = u^2 + v^2, theta = flow angle. The margin gives the two
UNIFORM transversality facts everything below uses:
 (T1) |lambda_i| <= Lambda(delta, C_dat) < infinity (no vertical
      characteristics: u >= c + delta bounds tan mu and theta);
 (T2) the acoustic families are uniformly NON-GLANCING at the walls:
      the wall slope is w' (bounded by C_geo), the streamline family
      is tangent (slip: lambda_0 = w' at the wall), and
      lambda_+- - w' = tan(theta +- mu) - tan(theta) is bounded away
      from 0 by a function of delta and the angle bounds — the Mach
      lines meet the wall at angles >= angle_min(delta, C_geo, C_dat)
      > 0.
      [SHARPENED 2026-08-05, U2 brick EXECUTED ([T-U2RG]/[X-U2RG]):
      at slip walls glancing is IMPOSSIBLE outright — the acoustic
      bracket at lambda = w' on the slip manifold equals
      -c^2(1+w'^2) != 0 at abstract EOS, so the wall is
      non-characteristic wherever c > 0, with NO (C_geo, C_dat)
      input: a hypothesis-input REDUCTION vs the sufficient statement
      above. The reflection-SOLVE degeneracy sits elsewhere: exactly
      at total-sonic q = c (T-U2RG P3) — excluded on the axial branch
      by the same single margin. R_0 is now the closed form
      |R| = |(1+w'lambda_+)/(1+w'lambda_-)|, finite by the axial
      margin alone.]

Complete left eigenvector set l_0a, l_0b, l_+, l_- (G12-L1 structure;
diagonalizable including the double family: S and H are independent
transported quantities). Characteristic (Li-Yu normalized) form: with
v_i := l_i(U) . U-increments,

  d/dx_i [v_i] := (d_x + lambda_i d_yhat)[v_i] = F_i(U, grad-coeffs),

where d/dx_i is differentiation along the i-th characteristic and
the right sides F_i are C^1 functions of U and the normalization
coefficients, with |F_i|, |DF_i| <= K_0(delta, C_geo, C_dat, 1/h_min)
on the certified set. [Li Ta-tsien & Yu Wen-ci, "Boundary Value
Problems for Quasilinear Hyperbolic Systems", Duke Univ. Math. Ser. V
(1985), Ch. 1 for the normalized characteristic form; page-level
theorem numbers = ACQUISITION IOU (G5-class), no numbers invented
here — the argument below is self-contained and classical.]

Wall boundary condition in characteristic variables: at yhat = 1
(upper wall), slip v = w'_+ u. The outgoing family there is the one
with lambda_i < w' relative slope... orientation fixed by (T2): ONE
acoustic family is incoming at each wall (the reflected one), the
streamline family is tangent (carries no boundary condition), and
slip determines the incoming acoustic variable as a C^1 function of
the outgoing one and the wall slope:

  v_in = G(v_out, U_tangential; w')     with |DG| <= R_0(delta,
                                        C_geo, C_dat)  (reflection
                                        bound; well-defined BY (T2)),

the classical reflection relation. (Solvability degenerates exactly
at glancing — excluded by (T2); this is where a future symbolic
brick could sit: the degeneracy locus of the reflection solve.
Named as candidate, not built: see §8.)

------------------------------------------------------------------------------
## §3 C^0 estimate (Gronwall along characteristics)

Integrate each characteristic equation from the inflow or from the
last wall reflection to (x, yhat):

  |v_i(x)| <= |v_i(start)| + Int_{path} |F_i| <= |v_i(start)|
              + K_0 Int_0^x (1 + max_j sup_{yhat} |v_j|)(s) ds.

Every backward characteristic path terminates on x = 0 (datum,
bounded by C_dat) or on a wall reflection point, where |v_in| <=
R_0 (|v_out| + C_geo-terms). Let V(x) := max_i sup_yhat |v_i|. A
backward path from x can undergo at most

  N_b(x) <= Lambda x / h_min + 1        [bounce count — the
                                        DISCOVERY constant]

wall reflections (each wall-to-wall traverse of an acoustic
characteristic consumes x-length >= h_min / Lambda by (T1) and the
normalization). Composing the reflection bound per bounce and the
integral bound along each leg (standard telescoping over the <= N_b
legs) gives

  V(x) <= R_0^{N_b} (C_dat + C_geo-terms) e^{K_1 x}
       =: C^0-BOUND(delta, L_x, C_geo, C_dat, h_min),

finite and EXPLICIT on the certified set, uniform over solutions.
QED (C^0). [If R_0 <= 1 (non-amplifying reflections) the bounce
factor is harmless; R_0 > 1 is possible in converging geometry and
is exactly why h_min must be named — see §7.]

------------------------------------------------------------------------------
## §4 C^1 estimate

Differentiate the characteristic equations along yhat (the standard
Li-Yu move: the derivative components z_i := d_yhat v_i satisfy a
LINEAR system along the SAME characteristics):

  d/dx_i [z_i] = sum_j a_ij(U) z_j z-linear + b_i(U, z) ,

with |a|, |b| <= K_2(delta, C_geo, C_dat, 1/h_min) by the C^0 bound
of §3 (coefficients are C^1 functions evaluated on a bounded set).
Wall condition for derivatives: differentiate the reflection
relation ALONG the wall: z_in = DG . z_out + (curvature term w''),
|w''| <= C_geo — the C^2 wall bound enters HERE and only here (the
reason C_geo is a C^2 bound in the certified-set definition:
confirmed as stated, no gap). Same bounce-count composition as §3:

  Z(x) := max_i sup_yhat |z_i| <= R_1^{N_b} (C_dat + C_geo)
          e^{K_3 x} =: C^1-BOUND(delta, L_x, C_geo, C_dat, h_min).

x-derivatives recovered algebraically from the equations (d_x U =
-(A^{-1}B) d_y U + ..., bounded since det A is bounded away from 0 by
the margin — [T-XSON]/G12-L1). QED (C^1).

------------------------------------------------------------------------------
## §5 Two-solution Lipschitz estimate (the -a deliverable, smooth level)

Let (U, w_+-) and (Utilde, wtilde_+-) be two certified solutions
(both in D with the SAME margins). Normalize BOTH to the strip
(§1); the difference DU := U - Utilde (strip variables) satisfies a
LINEAR hyperbolic system along the characteristics of U with
 (i)  coefficients bounded by the §3/§4 bounds of BOTH solutions,
 (ii) source terms bounded by K_4 ( |DU| + ||w - wtilde||_{C^2} )
      (the wall difference enters through the normalization
      coefficients and the reflection relations — C^2 because the
      derivative-level reflection carries w''),
 (iii) inflow datum DU(0,.) = data difference.
The §3-§4 Gronwall/bounce machinery applied verbatim to the linear
difference system yields

  ||U - Utilde||_{C^0([0,L_x] x strip)}
    <= LIP(delta, L_x, C_geo, C_dat, h_min)
       ( ||data - datatilde||_{C^1} + ||w - wtilde||_{C^2} ),

with LIP explicit (same structure: R^{N_b} e^{K L_x}). This is the
solution-map Lipschitz estimate of C-D25U component -a ON SMOOTH
REGIONS, constants uniform over D and never solution-dependent. The
C^1-level Lipschitz estimate (needed by -c, not -a) is NOT claimed:
it is exactly where the shift-C^1 subtlety lives (fronts move), and
it stays with U5/-c as priced by the panel. QED (-a, smooth level).

------------------------------------------------------------------------------
## §6 What -b gets for free

Uniqueness/well-definedness on smooth regions: two solutions with
the SAME data and walls give, by §5 with zero right side,
DU == 0 — the -b component at the smooth level is a corollary of -a,
as the S14 component note anticipated ("-b is discharged BY the S1-U
assembly, which uses only -a"). Nothing new needed. (Consistent
with, and now redundant to, the x-as-time weak-strong route [T-XWS]
on the shock-free class — two INDEPENDENT uniqueness mechanisms now
exist at smooth level: Gronwall-on-differences and relative entropy;
they cross-check each other.)

------------------------------------------------------------------------------
## §7 The discovery: h_min, and the amended certified set

WHAT THE WRITING FOUND (the reason "write it once, actually" was the
right order): the composed constants of §3-§5 carry the factor
R^{N_b} with N_b <= Lambda L_x / h_min + 1. Without a width floor:
 - N_b is unbounded as h -> 0 (characteristics bounce arbitrarily
   often per unit x);
 - with reflection bound R > 1 (possible in converging geometry),
   R^{N_b} blows up: the "constants depend only on (delta, L_x,
   C_geo, C_dat)" claim of the ledger §1 STATEMENT is FALSE as
   literally written — a sequence of certified nozzles with
   h_min -> 0 and all four named constants fixed breaks the uniform
   Lipschitz bound.
AMENDMENT OF RECORD (executed this session, dated): the certified
set is D(delta, L_x, C_geo, C_dat, h_min) with the width floor a
NAMED constant; ledger §1 statement annotated; registry C-D25U scope
string updated. Physical cost: none (real nozzles have h_min > 0:
throat height); honesty cost: one more constant in every C-D25U-
derived statement. This is hypothesis-minimization working as
intended (axis B): the missing hypothesis was found by EXECUTING the
proof, priced (harmless), and named — not discovered later inside a
referee report or, worse, a certified-but-wrong Verdict.

COST-CLAIM VERDICT (the S14 open question this doc answers):
 - U1 (-a/-b smooth level): CONFIRMED bounded — everything above is
   classical two-variable hyperbolic bookkeeping (one session, as
   priced); no new mathematics.
 - The panel's pricing asymmetry (-c research-grade vs -a/-b
   bounded) SURVIVES the test: nothing in §3-§5 touches linearized
   well-posedness of the MAP or quadratic remainders.
 - One structural correction (h_min) — the kind of finding that
   justifies the campaign's "write it for real" standard.

------------------------------------------------------------------------------
## §8 Residue (named, honest)

 - U2 full reflection estimate: the reflection relation and its
   derivative-level use are EXERCISED here (§2, §4) at the level U1
   needs; the standalone uniform reflection lemma (all regimes in D,
   sharp R_0(delta, C_geo, C_dat)) remains a named step. CANDIDATE
   SYMBOLIC BRICK (not built, declared): the degeneracy locus of the
   reflection solve == glancing locus, at abstract EOS — X-G12-class
   carrier, seconds-scale, would make (T2) machine-verified.
   [EXECUTED 2026-08-05 (reopened segment): [T-U2RG] with carrier
   [X-U2RG] (suite group (xiii)), VERDICT PASS 8/8 — with a
   DISCOVERY correcting the candidate's own conjecture: the
   degeneracy locus is NOT glancing (glancing at slip is impossible,
   P1) but the TOTAL-SONIC line q = c (P3); slip-hypothesis
   necessity exhibited by counterexample (off-slip glancing state,
   R2). (T2) is now machine-verified at abstract EOS with reduced
   hypothesis inputs; the remaining U2 residue is only the composed
   ESTIMATE bookkeeping inside U3/U4.]
 - U3 (fronts) and U4 (composition): untouched, as scoped.
   [EXECUTED 2026-08-06 (S16): docs/rde_nozzle_D25U_U3U4.md
   ([S-D25U-U34], carrier [X-U3BD]) — component -a chain complete at
   class level; conditional inventory c1-c4 declared there (U3-H1
   Lopatinskii scalar = sharpened C-MAJDA; topology stratum;
   origination; genuine nonlinearity).]
 - U5 / -c: untouched, priced research-grade, lead unchanged
   (Bressan-Guerra/Ulbrich + Breitkopf-Ulbrich arXiv:2509.22076,
   acquisition pending).
 - Li-Yu page-level theorem anchors: ACQUISITION IOU (the book is
   not in literature/); the §3-§5 arguments are self-contained, so
   nothing above CITES an unverified theorem number (radical
   citation honesty: book-level reference only).
