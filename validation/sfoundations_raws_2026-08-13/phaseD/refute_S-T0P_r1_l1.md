# REFUTATION [S-T0P]/[T-T0P] — round 1, lens 1 (hyperbolic-PDE structure)

Target: validation/sfoundations_raws_2026-08-13/phaseD/phaseD_stop_proof.md
(read in full). Cross-references consulted this window:
docs/rde_nozzle_cauchy_bvp_transfer.md ([S-XCONV], [T-XRED], [T-XWALL],
[T-XWS], [C-XBVP] declaration), docs/rde_nozzle_MASTER.md [S-T0P] site.
Role: adversarial proof refuter, until-dry loop, round 1.
Lens: characteristics, admissibility, front conditions, symmetry/group
action correctness, physics of the reduction; plus the binding attack
axes (statement truth, step validity, hypothesis completeness, rigor
LABEL, variable-gamma status, falsifier rejection power, ABSENCE).

VERDICT (this round): REPAIRABLE. The two-half architecture
(equivariance x uniqueness) is sound and the hard algebra (L-XWALL3
5-component slip solve, L-XC3D closed form h_ww = g'/(theta rho u),
L-COMPAT transfer, L-XSON3 parity factorization) checks out line by
line — I re-derived all four by hand and found no algebraic error.
But the document as written contains: one PROPOSITION whose statement
is FALSE as labeled (F1), one unnamed load-bearing hypothesis inside a
THEOREM* (F2), one unjustified analytic step that neither this doc nor
the inherited 2-D conditional actually covers as declared (F3), one
inheritance claim with a real domain-coverage hole carrying a concrete
number (F4), plus lower-grade statement/step/citation defects and one
literature-absence finding. None of these breaks the main route; all
of them break "SOUND-AS-LABELED".

==============================================================================
## F1 [P-HB3(i)] — STATEMENT FALSE AS WRITTEN; THEOREM over-label
Severity: HIGH (a labeled THEOREM with concrete counterexamples).
Axis: statement truth + hypothesis completeness + label.

The claim (§6, [P-HB3](i)): at a mode transition (wave count n changes
during the observation window) "the data are invariant under NO
nontrivial element of G_full on any window containing the transition
(no periodicity, no rotating-wave form)". Labeled THEOREM ("assembly
of record-level facts").

Counterexample 1 (common-divisor transitions — physically the MOST
relevant transition class). Take a transition n = 2 -> n = 4 (mode
doubling; a standard, experimentally documented RDE transition path).
Let the pre-phase data be exactly pi-rotation symmetric (any exact
n=2 rotating wave is), the post-phase data exactly pi-rotation
symmetric (any exact n=4 wave is), and the transient constructed
pi-symmetric — admissible, since H2 prescribes the data freely, and
dynamically natural, since an equivariant evolution from a
Z_2-symmetric state stays Z_2-symmetric. Then g_{pi,0} in G_full is a
NONTRIVIAL element leaving the data invariant on EVERY window
containing the transition. (i) is false. Same for any transition
n1 -> n2 with gcd(n1, n2) = d >= 2: the data retain Z_d.

Counterexample 2 (periodic mode-switching). RDEs exhibit recurrent
periodic mode-hopping. Data executing a periodic switching cycle of
period T_sw are invariant under the pure time translation
g_{0, T_sw} — a nontrivial element of G_full — on any window, while
H3 fails (no rotating-wave form). This kills the parenthetical "no
periodicity" claim even for coprime wave counts. Note this case is
not exotic: by [P-HB1] the surviving symmetry then TRANSFERS
(t-periodic solution), so the boundary statement misdescribes exactly
the structure the monitor line would see.

The document half-knows this: the falsifier line appends "the claim
is for genuine wave-count changes with generic profiles" — but
"generic" appears NOWHERE in the statement or hypotheses, is
undefined, and in the equivariant setting the symmetric transition
data of Counterexample 1 are not a measure-zero pathology (symmetric
subspaces are dynamically invariant). Under the binding standard
(explicit hypothesis list; over-label = finding), [P-HB3](i) as
stated is refuted; honest label for the (i) claim as stated: FALSE;
for a repaired claim: THEOREM only after adding the hypothesis "no
common nontrivial subgroup of the per-phase symmetry groups and no
exact temporal recurrence of the switching schedule", or downgrade
to the correct residual statement "Sym(s) contains no ONE-PARAMETER
subgroup, and H3 fails" (which is what (ii)/(iii) actually need).
(ii) and (iii) are unaffected. The [P-HB3] falsifier as printed
("exhibit a transition window with an exact nontrivial data
symmetry") is EXECUTABLE AND FIRES — my Counterexample 1 satisfies
it verbatim. A falsifier that the document's own boundary class
satisfies is a self-rejection, not a defense.

Repair: restate (i) as "Sym(s) contains no one-parameter subgroup,
and generically no nontrivial element; the Z_gcd and periodic-
switching residues are named and inherited by [P-HB1] transfer";
re-label the strengthened version accordingly.

==============================================================================
## F2 [T-T0P-U]/(A) and [T-T0P] — UNNAMED HYPOTHESIS: T-periodicity
of the STRONG side. THEOREM* label incomplete as written.
Severity: HIGH (label violation: THEOREM* = "complete modulo NAMED
conditionals"; this conditional is consumed but not named).
Axis: hypothesis completeness + step validity + label.

The proof of (A) works on the slab Sigma_x = Omega_x x T_t with
T_t = R/(T Z) and says "(H8: both solutions T-periodic, so the
t-integrals below are over a compact circle — no boundary terms in
t)". But H8 as WRITTEN declares T-periodicity of the COMPETITORS
only ("Competitors are T-periodic in t..."), and H6 (the strong S1
class) says piecewise C^1 on cl(Omega) x R with NO temporal
structure. Two distinct consumptions of the unnamed hypothesis:

 (a) The entropy IDENTITY of U integrated over T_t produces no
     t-boundary terms only if U is T-periodic. Otherwise the slab
     computation is not even well-formed for U (you cannot quotient
     a non-periodic function to the circle).
 (b) G := ||D U||_inf over cl(Omega) x [0, T] is declared "finite:
     C^1 on a compact slab by H6-A + H8" — the compactness in t IS
     the periodicity of U. For a merely-C^1-on-cl(Omega) x R strong
     side, sup over R of |DU| has no stated bound.

Downstream, §5 applies (A) with the arbitrary S1 element q as strong
side and g_tau q as competitor: BOTH uses require q T-periodic,
which is hypothesized nowhere. This is not vacuous circularity —
T-periodicity is strictly weaker than co-rotating steadiness
(standing oscillations are T-periodic, as the doc itself notes at
H8) — but it IS a class hypothesis on the object of the main
theorem, and [T-T0P](i) ("every S1-class solution q in C(s)")
silently ranges only over T-periodic q. The M0 sentence being
upgraded ("the certified solution is a steady co-rotating pattern")
does not carry that restriction; the upgrade as labeled therefore
proves LESS than the M0 schema statement it claims to discharge,
without saying so.

The G5 remark does NOT cover this: it explicitly lifts
"the t-periodicity assumption on the COMPETITOR, comparing on
backward cones resting on Gamma_d". In fact the cone-localized
argument (finite transverse speeds by L-SPACE, cone-slope constants
from c_K, C'_K) removes the periodicity of BOTH sides — the strong
side only needs C^1 on each compact cone — so the repair is cheap:
either (i) extend H8 to all class members (and say so at H6, and
accept that [T-T0P] is conditional on it until G5 is written), or
(ii) write G5 once, for both sides. Until one of these lands, the
inheritance list of [T-T0P-U]/[T-T0P] is incomplete and the
THEOREM* label is formally violated (an over-label per the binding
standard).

==============================================================================
## F3 Quadratic sandwich from pointwise convexity — UNJUSTIFIED STEP;
the inherited conditional as DECLARED does not deliver what the
proof CONSUMES.
Severity: MEDIUM-HIGH (a proof step of the load-bearing estimate,
unjustified in this doc AND not covered by the cited (a)/(b) text).
Axis: step validity + hypothesis completeness (+ inherited-claim
accuracy: "no new analytic conditional is created", §0/§3).

The Gronwall proof uses
    c_K |M_V - M_U|^2 <= eta(V|U) <= C_K |M_V - M_U|^2,
    |Q_rel| <= C'_K |M_V - M_U|^2,
citing "strict convexity (L-XC3D + [C-XBVP](a) block)" and "flux
smoothness on the branch (L-XSON3 diffeo + smooth EOS)". Both bounds
are TAYLOR statements along the SEGMENT joining M_U(x,y,z,t) and
M_V(x,y,z,t) in M-space. But eta(M), F_mu(M), W(M) are defined only
on the IMAGE under F_x of the branch compact K (through the local
diffeomorphism of L-XSON3): off that image, F_x^{-1} does not exist.
Nothing stated anywhere guarantees the image F_x(K) is CONVEX; the
segment between two branch images can in principle leave the image
(the sonic locus det J_5 = 0 is exactly where the parametrization
degenerates, and the 2-D record itself proves indefiniteness on the
other side of it — [S-XCONV] R1: 60/60 subsonic states INDEFINITE,
so no convex extension across the sonic line exists for this eta).
Pointwise Hessian definiteness ON K — which is precisely what
[C-XBVP](a) declares and what [X-IVXC] certifies ("strict
definiteness over the WHOLE declared (M, V) box") — does NOT imply
the displayed sandwich for pairs of points whose segment exits the
region. The same gap sits in the 2-D [T-XWS] proof ("On the compact
K: strict convexity (S-XCONV) gives c_K|m_V - m_U|^2 <= ..."), so it
is arguably INHERITED — but then the §0/§3 claim "the extension
inherits EXACTLY [C-XBVP](a,b) — no new analytic conditional is
created" is accurate only if the hull/segment condition is read INTO
(a) or (b); as (a) and (b) are DECLARED in the transfer doc §6
((a) = definiteness on K; (b) = trace/regularity bookkeeping),
neither names it. Under the binding standard ("every step justified
or explicitly flagged as gap") this is an unflagged gap in a
THEOREM*-labeled proof.

Standard repairs exist and should be NAMED, not assumed: (r1) show
F_x(K') is geodesically convex for a slightly enlarged branch
compact K' and take segments there; (r2) replace segment-Taylor by
the Dafermos device of extending eta to a globally defined convex
function of the CONSERVATIVE state and running the relative entropy
in W-variables with the M-reading only at the flux level; (r3) prove
the sandwich directly on pairs (doubling constant) via the [T-XRED]
Mach-pair reduction — the (M, V)-box is 2-D and an interval
certificate over PAIRS is feasible. Any of these closes F3; until
then the honest formulation is a named sub-conditional (a').

==============================================================================
## F4 [L-XC3D] CONSEQUENTLY-clause — DOMAIN-COVERAGE HOLE in the
"inherits EXACTLY [C-XBVP](a)" claim, with a concrete number.
Severity: MEDIUM-HIGH (the inheritance claim is quantitatively wrong
for the natural 3-D box unless an unstated hypothesis is added).
Axis: hypothesis completeness + statement truth of the consequence.

The rotation congruence (i) reduces definiteness of H_5 at a 3-D
state (rho, u, v, w, S) to definiteness at the ROTATED planar state
(rho, u, q_perp, 0, S) with q_perp = sqrt(v^2 + w^2). Hence the
planar block is consumed at transverse speed q_perp — the EUCLIDEAN
NORM of the two transverse components. The certificate being
inherited, [X-IVXC], is declared over the planar box with
|v| <= 0.8 c (transfer doc §2, P4a box; [T-XRED] collapses it to the
(M, V) slice with V = v/c in the certified range). Now take the
natural 3-D margin box built per-component from the same bounds:
|v| <= 0.8 c, |w| <= 0.8 c. Then q_perp reaches 0.8 * sqrt(2) c
=~ 1.13 c — OUTSIDE the certified V-range. On that corner of the
3-D box the planar 4-block's definiteness is simply NOT certified
(and the transfer doc's own R1 result shows definiteness is not free
— it genuinely fails somewhere). So "strict convexity of eta on the
3-D margin box holds IFF it holds on the planar (M, V)-box" is true
ONLY under the unstated box-compatibility hypothesis: the
q_perp-shadow of the 3-D K must lie inside the certified planar
V-range. The CONSEQUENTLY clause states no such hypothesis and the
3-D box is never defined in the document (H5 constrains only rho_min
and the axial margin — it puts NO bound on q_perp at all beyond
K-compactness, so as written even 0.8c is not guaranteed).

Repair (cheap, must be written): define the 3-D certified box with
the EUCLIDEAN transverse-Mach bound q_perp/c <= V_max inherited from
the planar certificate, and add one sentence to H5. Note the [T-XRED]
Mach-pair reduction makes this the RIGHT formulation anyway (the
invariant content is (M, V_eff) with V_eff = q_perp/c). Also note
the unfinished text in the positivity line of (iii): "rho u in
[rho_min c_min? , ...]" — a literal dangling "?" inside a
THEOREM-labeled proof; the bound is true (rho u >= rho_min
(c_min + delta) on K, c_min > 0 by compactness and c^2 = p_rho > 0)
but the line as committed is not a proof sentence. SOTA-rigor ding.

==============================================================================
## F5 [L-SPACE] — statement overreach: determinacy claim not proven
by the ray argument; walls ignored in the "complete Cauchy datum"
sentence.
Severity: MEDIUM (statement truth of a THEOREM-labeled lemma; core
spacelikeness is correct).
Axis: statement truth + step validity (characteristics lens).

The characteristic algebra is right: speeds u.xi (x3) and u.xi +- c;
ray x-components in [u - c, u + c] u {u}; all >= delta on K; {x =
const} noncharacteristic and spacelike; transverse slopes dy/dx,
dz/dx, dt/dx bounded on K. Correct, and the falsifier is executable.

The overreach: "the domain of dependence of any point pulls back to
a COMPACT subset of the interface Gamma_d ... the interface trace
for all t is the complete Cauchy datum of the x-evolution". In the
annular engine domain backward bicharacteristics generically hit the
WALLS Gamma_w before reaching Gamma_d and REFLECT: the backward
genealogy of a point includes wall interactions, and the pullback
onto {x = 0} alone is not the domain of determinacy in the pure-
Cauchy sense. The x-evolution is an IBVP (lateral boundary = walls
with homogeneous slip), not a Cauchy problem. The conclusion that
interface data alone determine the solution is TRUE in the certified
class — but it is proven by the WALL LEMMA inside the relative-
entropy argument (§4, L-XWALL3: walls cost nothing), i.e., by
[T-T0P-U], NOT by the ray geometry of L-SPACE. As written, a
THEOREM-labeled lemma asserts a determinacy statement its own proof
does not reach (the proof text only delivers transversality + finite
transverse speeds + compact pullback OF THE REFLECTED GENEALOGY).
Circularity risk is real: if L-SPACE's "complete Cauchy datum" were
consumed by the uniqueness half as an input, the argument would be
circular; fortunately the Gronwall proof never uses it. Repair:
re-scope L-SPACE to (i) spacelikeness/noncharacteristicity and (ii)
bounded transverse speeds (both proven), and move "interface data
are the complete data" to a REMARK that cites [T-T0P-U] + L-XWALL3
as its proof. No mathematical loss; the label then matches content.

==============================================================================
## F6 Discrete rotation rho_n — cited lemma does not cover it.
Severity: LOW-MEDIUM (step/citation defect; trivially repairable,
but as-written the n-fold-symmetry chain is formally unproven).
Axis: step validity / group action correctness.

[T-T0P-E] proves the discrete claim by "rho_n q in C(s) by L-EQV3
(tau = 0 case) + L-INV". But L-EQV3 is STATED for the maps g_tau of
(HEL) only: g_tau = g_{OM tau, tau}. Its "tau = 0 case" is
g_0 = identity — it says nothing about rho_n = g_{2pi/n, 0}, which
lies on a DIFFERENT one-parameter family (pure rotations). The
general-(phi, tau) version of L-EQV3 is exactly what [P-HB1]'s proof
later asserts in passing ("L-EQV3 holds for every (phi, tau) — it
nowhere used H3"), which is true of the PROOF but not of the
STATEMENT. A theorem chain in a SOTA-rigor document may not cite a
lemma outside its stated scope and discharge the mismatch two
sections later inside a different proposition's proof. Repair: state
L-EQV3 for arbitrary g_{phi,tau} in G_full from the start (the proof
already is); rho_n and P-HB1 then both cite it legitimately.

==============================================================================
## F7 [L-STD] — mollification step: tau-dependent null sets not
handled.
Severity: LOW (genuine gap in the written proof; standard repair).
Axis: step validity (measure theory).

"For each tau, a.e.-invariance survives convolution EXACTLY, and
Q_eps is continuous in t; hence Q_eps(., t) = Q_eps(., 0) for ALL t."
Non sequitur as written: for each FIXED tau, Q_eps(x, t) =
Q_eps(x, t - tau) holds for a.e. x (all t by continuity), but the
exceptional x-null set DEPENDS ON tau, and the conclusion quantifies
over all tau. Missing (standard) bridge: take the union of the null
sets over RATIONAL tau (still null), conclude t-constancy of
Q_eps(x, .) on the rationals' orbit closure by continuity in t, hence
for all t, for a.e. x. With that inserted the lemma is sound (the
rest — L^1_loc limit, bi-Lipschitz Phi, pointwise refinement off the
invariant closed null set N — checks out). Also note: in the
application the hypothesis "g_tau N = N" of the pointwise refinement
is discharged only if N is taken to be the ESSENTIAL discontinuity
set of q (intrinsic, hence invariant once q = g_tau q a.e.), not the
a-priori S1 front set of a particular representative; one sentence
should say so. Repair: two sentences total.

==============================================================================
## F8 Falsifier rejection power — the main falsifier cannot fire
inside the current toolchain.
Severity: MEDIUM on the R5 axis (rejection power), LOW mathematically.
Axis: falsifier ability to actually reject.

The [T-T0P] falsifier of record: "an L4-certified pure-periodic-data
instance whose certified solution is NOT a steady co-rotating
pattern (T0-flatness monitor fires with data purity verified)". But
the certified apparatus CONSTRUCTS wave-frame-steady solutions by
design (the I1 idealization; Cor 5.2 says exactly this): every
object the toolchain can certify is steady-co-rotating BY
CONSTRUCTION, and no certified unsteady 3-D solver exists in the
corpus that could ever EXHIBIT a non-steady class member. The
monitor line tests DATA purity (H-DATA), i.e., the hypothesis — not
the conclusion. So within the present toolchain the falsifier is
structurally unfireable against the theorem: it can reject the PIN,
never the PROPAGATION. The same holds for the inherited two-
solutions falsifier ([T-XWS] §8 line) unless a second, independent
solution-producing mechanism (capturing-mode unsteady run) is
actually scheduled — it is named ("A1 engine, capturing-mode
controls, X1 design") but no such run exists or is planned in this
document's carrier plan. What IS genuinely executable is the
symbolic [X-T0P] battery (compatibility identities, det J_5
factorization, 5-component slip solve, Hessian entry) — those
falsifiers are real and would reject the LEMMAS. Repair per R5:
either (i) declare honestly that the theorem-level falsifier is
CONDITIONAL on a future capturing-mode capability (owner + trigger,
per the never-postpone-resolvables discipline), or (ii) add one
executable theorem-level check: e.g., a t-DNS/capturing twin on one
certified instance is the only test that can actually reject
steadification — name it as the falsifier's carrier and its gate.

==============================================================================
## F9 ABSENCE — convex-integration non-uniqueness literature not
confronted; stratum (B)'s conditional is counterexample-grade, not
bookkeeping-grade.
Severity: MEDIUM (absence of a known literature route that calibrates
how much load [C-MAJDA] carries).
Axis: absence + admissibility (lens).

The document treats [C-MAJDA] as a named conditional of the same
"technicality" flavor as (b). The hyperbolic literature says
otherwise: for multi-D compressible Euler, ADMISSIBLE (entropy-
inequality-satisfying) L^inf weak solutions are non-unique in
nearby settings — De Lellis–Szekelyhidi wild solutions, and
specifically Chiodaroli–De Lellis–Kreml (2-D Riemann problems whose
self-similar solution contains a SHOCK admit infinitely many
admissible L^inf solutions). That is: for strong sides that are
piecewise-C^1 WITH FRONTS — exactly stratum (B) — weak-strong
uniqueness against a bare entropy-inequality class is provably FALSE
in general. Uniqueness on stratum (B) therefore survives only
through the EXTRA structure of the class: the uniform margin
u - c >= delta (the wild constructions live at transonic/subsonic
shear states and plausibly cannot maintain a uniform axial
supersonic margin), the fixed full-state supersonic inflow trace,
and the fitted-front/Majda-stability package. The document nowhere
cites this literature nor argues which class hypothesis excludes the
wild constructions. Consequences: (1) the honest pricing of G3
should say "known counterexamples exist just outside the class;
[C-MAJDA] + margin is what excludes them — not yet proven to"; (2)
the §9 novelty-sweep query list should add "non-uniqueness
admissible weak solutions compressible Euler convex integration
Riemann shock" so the paper claim cannot collide with it; (3) the
shock-free stratum (A) is genuinely immune (Dafermos weak-strong
needs only the C^1 strong side + convex entropy — wild solutions do
not break weak-STRONG with smooth strong side), and the document is
entitled to say so explicitly as the reason stratum (A) is safe.
This finding does not lower the [T-T0P-U] label (the conditional IS
named) but the surrounding prose ("same class of bookkeeping",
"cleanly confined") under-prices it, and the absence of the
citation is a defect under the claim-dual-proof standard.

==============================================================================
## F10 Minor statement-hygiene items (grouped; each LOW).
Axis: statement truth / hypothesis completeness.

 (a) Uniqueness domain: (A) concludes "V = U a.e. on Omega x R" with
     Omega from H1 = the WHOLE engine gas domain; the estimate
     controls only the region marched from Gamma_d, i.e.,
     {0 < x < L} downstream of the interface (H2 puts Gamma_d
     downstream of all heat release, so upstream-of-Gamma_d Omega
     points exist and are not controlled). Restate on
     Omega_march := Omega intersect {0 < x < L}.
 (b) H7 says "(EI-x) for the §3 entropy quadruple" — §3 defines a
     quadruple for EVERY g with g' > 0. The proof needs it for the
     specific certified g ([X-IVXC] certifies g(S) = S). Fix the
     ambiguity: one certified g suffices; say which.
 (c) [T-T0P-E]'s hypothesis is the FULL pairwise uniqueness property
     of C(s), but §5 verifies only S1-anchored weak-strong
     uniqueness. The application is fine because the elements
     compared (q, g_tau q) are both S1 — but then [T-T0P-E] should
     be stated with the weaker hypothesis it actually gets
     ("uniqueness against S1 elements"), or §5 should note the
     specialization. Cosmetic given F2's repair, but as written the
     hypothesis verified is not the hypothesis stated.
 (d) §4 (A) "Integrate (EI-x) for V against 1 ... and integrate by
     parts": the relative-entropy identity also consumes the WEAK
     FORM OF THE EQUATIONS for V tested against the non-compactly-
     supported Lipschitz function D_M eta(U); this is a distinct
     consumption of (b)-class trace machinery from the entropy-
     inequality integration and should be named as such inside G2
     (it is a different functional-analytic statement: Gauss-Green
     for DM fields against Lipschitz test functions on a domain
     with corners, C^{1,1} per sector).

==============================================================================
## What SURVIVED round 1 (explicit, for the loop's bookkeeping)

- L-EQV1/L-EQV2 (frame indifference, dyadic momentum-flux congruence,
  scalar EOS entry): checked, correct, abstract EOS. THEOREM stands.
- L-INV: correct.
- L-XSON3 parity/rotation factorization det J_5 = rho u det J_4 at
  w = 0: re-derived, correct.
- L-COMPAT both steps (Kato-Majda gradient-arbitrariness device;
  D_M eta = D_W E identity): re-derived, correct; the identity is
  indeed the algebraic heart and its P3 carrier instance is the
  right check to extend.
- L-XWALL3 5-component slip solve: re-derived line by line
  (d(rho u) = 0, dH = 0, theta dS = -p'(u.n)/(rho u) = 0); correct
  for every g and abstract EOS; the pressure-only slip flux identity
  is correct (mass/energy rows are rho(u.n)-multiples).
- L-XC3D (KEY) cancellation theta dS = -dbeta: re-derived, exact at
  abstract EOS; h_ww = g'/(theta rho u) confirmed, including the
  eta(eps) = -m1 g(S(eps)) frozen-m1 observation. (Modulo F4 on the
  inheritance domain and the dangling-"?" line.)
- [P-HB1], [P-HB2]: proofs correct (Fourier differentiation argument
  checked; the same-speed multiplicity note is right and valuable).
  One scope note on P-HB2: the ansatz assigns ONE frequency per
  wavenumber (omega_k = k OM_k); data with two frequencies on the
  SAME k also kill the one-parameter subgroup but sit outside the
  stated class — the proposition covers what it states, no defect,
  but the class restriction deserves one sentence.
- Variable-gamma declarations: audited per statement; honest. The
  single gamma-restricted ingredient really is the [X-IVXC]
  certificate, exactly as the §9 table declares. No gamma finding.
- The two-stage honesty structure (§7) and the H10 existence
  disclaimer: clean, no over-claim found there.

## Round-1 verdict

REPAIRABLE. No objection above severs the main route: F1 repairs by
restatement (the correct residual claim is exactly what (ii)/(iii)
need), F2 by extending H8 or writing G5 for both sides (cheap), F3
by naming the hull/segment sub-conditional or switching to the
W-variable Dafermos device, F4 by defining the 3-D box with the
Euclidean transverse-Mach bound, F5-F7, F10 by re-scoping/wording,
F8 by declaring the falsifier's conditional carrier, F9 by citation
+ one pricing paragraph. But as COMMITTED the document contains one
false labeled THEOREM ([P-HB3](i)), one THEOREM* consuming an
unnamed hypothesis ([T-T0P-U]), and one unflagged analytic gap in
the load-bearing estimate — SOUND-AS-LABELED is not available at
round 1.
