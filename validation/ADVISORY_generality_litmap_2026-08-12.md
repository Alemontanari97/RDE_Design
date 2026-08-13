# ADVISORY — Deep review of record: the cycle-averaged variational
# framework as a generalization of the classical variational nozzle
# corpus (ALL approaches in GENO/literature + root literature/)
# (2026-08-12, user-ordered review; [RIGOR/generality-ledger] thread,
# advisory pattern — does NOT touch the S24 F1b carrier)

STATUS: advisory (untracked, ADR/PANEL pattern). Refuter pass:
appended in §9 (verdict recorded before circulation). Sources: 8
parallel reader agents, page-level extraction of 24 PDFs (every
variational paper read IN FULL; handbooks/theses triaged and read at
the declared depth); internal side = M0 read integrally this session
+ ADVISORY_def_equivalence_proof + Sgauntlet generality ledger + D2
b0/b2. Rigor classes per claim as marked; nothing here promotes any
registry class by itself (R4 duties listed in §8).

## 0. The claim under review, stated honestly

CLAIM (as reviewed): the program's problem of record (P) (M0 D2.6)
with the averaged stationarity system T7 (**'), the tier ladder
(P_t) with margin vector, and the operating measure mu, CONTAINS —
as special cases under named hypotheses — every variational
maximum-thrust nozzle formulation present in the GENO/literature
corpus and the root literature/ classical papers, for every profile
family treated there (bell/TOC, TOP, spike/plug, fixed-inlet plug,
shrouded plug, annular, DEF, reacting/rotational variants), AND
both classical derivation ROUTES (control-surface and
multiplier-field). VERDICT OF RECORD (refuter-corrected, §9): the
containment holds for each formulation's INVISCID-EULER,
EXOGENOUS-MEASURE CORE under the named hypotheses of §3-§5 — the
eight §3 rows that supply an actual restriction of (P) all
survived adversarial attack. It is NOT a universal quantifier:
two STRUCTURAL non-containments are named — (i) Kraiko-Osipov's
coupled trajectory-adjoint weight (endogenous measure; (P)'s mu
is exogenous contract data — only the fixed-program restriction
is contained, §6(g)) and (ii) BL-terms-in-the-functional (§6(c))
— plus the instantiation-level boundaries of §6, all
already-declared scope pins (P1/P2, N4 ladder, F-phase owners).
The containment is therefore of the same kind as the one (P)
itself declares: hypotheses are the problem's definition.

## 1. Corpus census (what was actually read)

GENO/literature (20 files, all identified):
 - RAO.pdf = Rao, Jet Propulsion 28(6):377-382 (1958) [bell TOC]
 - Rao_1961_review.pdf = Rao, ARS J 31(11):1488-1494 (1961) [survey]
 - Rao_1961_spike.pdf = Rao, Ballistic Missile & Space Tech. v2,
   92-101 (1961) [spike/plug] — DUAL-VENUE identity note (refuter
   C4): the same Pergamon text with identical pagination is the D2
   b2 correction-of-record citation Planet. Space Sci. 4:92-101
   (1961), doi:10.1016/0032-0633(61)90125-8; cite either with the
   identity stated (D-D duty)
 - migdal.pdf = Migdal, JSR 9(1):3-6 (1972) [annular, non-variational]
 - design-of-maximum-thrust-plug-nozzles-for-fixed-inlet-geometry
   = Humphreys-Thompson-Hoffman, AIAA J 9(8):1581-1587 (1971)
 - hoffman-2012-... = Hoffman, AIAA J 5(4):670-676 (1967) [reacting]
 - scofield-hoffman-2012-... = Scofield-Hoffman, AIAA J
   9(9):1824-1832 (1971) [noneq dissociating + rotational]
 - Allman_Hoffman_1981.pdf = AIAA J 19(6):750-751 (1981, synoptic)
   [direct method]
 - rao-beck-2012-... = Rao-Beck, AIAA 94-3264 (1994) [DEF]
 - rao-et-al-2012-... = Rao-Beck-Booth, AIAA 99-2584 (1999) [DEF,
   equilibrium/frozen chemistry]
 - BF00934730.pdf = Hoffman-Scofield-Thompson, JOTA 10(3):133-159
   (1972) [BL-in-the-loop]
 - 1-s2.0-0045793074900127-main.pdf = Johnson-Thompson-Hoffman,
   Computers & Fluids 2:173-190 (1974) [variable-inlet plug,
   rotational, a = a(p,P,H)]
 - Veen.pdf = Vander Veen-Gentry-Hoffman, AIAA J 12(9):1193-1197
   (1974) [shrouded plug]
 - ADA455494.pdf = Onofri et al., RTO-TR-AVT-007 / AIAA 2002-0584
   [plug survey, non-variational]
 - NASA_RP1104 (1983) [truncated-perfect curves, non-variational]
 - NASA_SP8120 (1976) [design criteria; institutional failure-
   boundary statement]
 - Johnson_Boney_1975 = NASA TM X-3243 [real-gas tabulated MoC,
   uniform-exit design, NON-variational — reclassified, see §7.6]
 - Zucrow_Hoffman_Gas_Dynamics_Vol2 (1977) [16-4(c) Rao; 17-5(c)
   rotational max-thrust lineage statement]
 - tesi_viviano.pdf = Viviano, Sapienza 2023 (rel. Nasuti) [TIC/TOC/
   DEF/TOP, frozen thermally-perfect; MoC.f90]
 - thesis_valeriani.pdf = Valeriani, Sapienza 2019/20 (rel. Nasuti)
   [plug; GENO v3.0/3.1/3.2 lineage; Rao plug outside perfect-gas]
Root literature/ (variational line):
 - 0021-8928(70)90164-4 = Kraiko-Osipov PMM 34(6) (1970)
 - 0041-5553(80)90091-9 = Shmyglevskii, USSR CMMP 20(5):113-127
   (1980) ["Variational problems of gas dynamics" — the survey
   Rao-Beck cite as their Ref. 4 "1981"; see §7.1]
 - dan25254.pdf = Sternin, DAN SSSR 139(2):335-336 (1961) [Russian
   ORIGINAL of the boundary paper; the 1962 Sov. Phys. Dokl. is its
   translation; see §7.1]
 - s0045-7930(01)00072-x = Moretti, C&F 31:719-723 (2002)
   [shock-fitting retrospective, non-variational; F4b support]

## 2. The two classical derivation routes, and where each lives in
## the program (the taxonomy is Shmyglevskii's own, 1980 §1-§2)

ROUTE A — CHECK-CONTOUR / CONTROL-SURFACE (Nikol'skii 1950 ->
Guderley-Hantsch 1955 -> Shmyglevskii 1957 -> Rao 1958/1961 ->
Rao-Beck 1994/1999; Veen 1974 composes two of them): thrust and
constraints written as line integrals on a control surface crossing
the exit flow; two constant multipliers (mass lambda2, length
lambda3); first variation delivers (i) surface = characteristic
(RESULT, not assumption; Rao Eq. [11]; Guderley's extra multiplier
h = 0 in retrospect), (ii) two first integrals (Rao [12]-[13] =
GENO f2/f1 invariants), (iii) endpoint transversality = corner
condition (Rao [14]; spike: TWO conditions, one per free endpoint,
with p_a at the lip and p_b at the truncation). Its DECLARED limits
(Shmyglevskii 1980, verbatim positions): exhausted by the complete
conservation-law sets; cannot carry constraints not expressible on
the check contour; NO check surface exists in 3-D; properties on
the surface must be functions of speed only => dies for
dissipative/reacting flows (Hoffman 1967 p. 670 states the same).
 IN THE PROGRAM: Route A is the per-phase CLOSED FORM of T7(a),
scoped to the irrotational-homentropic subclass (S21 audit C1
scoping), used as oracle/initializer (VI.4bis(iv)); its objects are
carried executably: f2 = -lambda2 measured constant to 9.5e-03 with
cross-design agreement 2.4e-04 ([X-O33B]); corner condition = the
lambda_e lip-multiplier bookkeeping at fixed (eps, L) (S21 block);
surface-characteristic condition = the classical locus of the
O3.2/O3.3 campaign ("stopped at the kernel boundary").

ROUTE B — MULTIPLIER FIELDS / WHOLE-REGION FUNCTIONAL (Guderley-
Armitage 1962; Sirazetdinov 1963; Kraiko PMM 28(2) 1964 + book
1979; Hoffman 1967; Scofield-Hoffman 1971; HTH 1971; JOTA 1972;
Johnson-Thompson-Hoffman 1974; Kraiko-Osipov 1970): every flow PDE
adjoined pointwise with a multiplier FIELD; first variation yields
adjoint PDEs that are hyperbolic WITH THE SAME CHARACTERISTICS as
the flow (streamlines + Mach lines); the exit control surface's
Mach-line character is DERIVED (Hoffman 1967's anti-overspecification
argument; JOTA 1972 Eq. (25) via Miele transversality); optimality
= ONE redundant boundary condition turned into a residual (Hoffman
1967 Eq. (78) E = y h1 - (u y' - v) h3 on BC; Scofield-Hoffman Eq.
(43) on the wall; C&F 1974 Eq. (19)/(29)); the KEY UNLOCK for the
general theory was Kraiko's DISCONTINUOUS multipliers (jumps along
characteristics with derived jump conditions — Shmyglevskii 1980
§2; Kraiko-Osipov Eq. (3.8)).
 IN THE PROGRAM: Route B IS the field-level half of T7(a)
("FIELD-LEVEL adjoint conditions otherwise") and its executable
form is the Lemma-B discrete adjoint: reverse-AD of the fitted
march = adjoint characteristic sweep (M0 VI.3/VI.4bis(iv), O3.1
transpose identity as the machine guarantee, Hoffman-E residual
listed among the VI.3 certificates). The multiplier-jump machinery
of Kraiko is the classical ancestor of the F4b fitted-front adjoint
jump conditions ([S-D25U-U34]/G12 line). The P2/G14 bridge (Rao =
adjoint, explicitly identified and measured) remains ours: none of
the three banks (Hoffman 1967; Giles-Pierce 2001; Lozano-Ponsin
2025) cites the others (D2 b2, confirmed).

## 3. The containment map — per approach, with named hypotheses
## (format: approach -> restriction of (P) that reproduces it ->
## program carrier/theorem -> honest delta)

3.1 RAO 1958 BELL (TOC). Restriction: mu atomic (single phase);
fixed-wall full-flowing sector; per-phase data irrotational-
homentropic, gamma = const; constraints (mdot, L); tier-0
shock-free class. Under these, T7(a) closed form = Rao [11]-[14]
verbatim (f2 invariant, f1 invariant, corner condition), and the
S18/S19 carrier reached the SAME optimum through the gradient with
the classical route agreeing at 91/91 samples ([X-TOCV]). Moreover
the cycle-averaged problem with a nondegenerate mu COLLAPSES to
Rao-at-<Pc> pointwise under H1-H4 (T-T3, THEOREM) — i.e. classical
Rao is not merely contained: it is the THEOREM-level collapse point
of the averaged theory, and oracle O1 enforces it executably.
Delta: Rao's own formulation omits the flow PDEs (legitimized a
posteriori by the compatibility check [15]); the program's Route-B
engine does not need that a-posteriori step. Dual-optimality
((L,p_a) <-> (L,eps), Rao's own remark) = the constraint-pair
equivalence already registered in D2 b0.

3.2 GUDERLEY-HANTSCH 1955 / GUDERLEY-ARMITAGE 1962. Same solution
as Rao (Guderley 1959, acknowledged in the 1961 review; h = 0);
G-A's whole-region functional is Route B's origin; both contained
exactly as 3.1 + §2 Route B. Delta: G-H's "single contour for all
lengths" claim was WRONG (Rao 1958 Fig. 5 refutes it) — a classical
precedent for family-vs-member confusion, the exact error class the
T-T3 remark R1 ("per-phase optima DO move; the average of an affine
family is a member") guards against.

3.3 RAO 1961 SPIKE / PLUG. Restriction: mu atomic; plug sector
(external expansion, lip-centered PM fan); C- control surface; TWO
free endpoints -> two transversality conditions (lip with p_a,
truncation with p_b); p_b assumed contour-independent (Rao himself
declares this generally FALSE). Contained as the free-boundary
per-phase brick; at the AVERAGED level the plug is where the
program goes strictly BEYOND the corpus: T-T4 (peak-phase design,
nested argmax, THEOREM* under [C-HT4]) has NO classical
counterpart (D2 gap G3, NOT-FOUND; Kraiko-Egoryan's
instantaneously-adapted bound is a BOUND, not a shape theorem), and
the truncated plug under a length cap is the first genuinely
averaged shape problem (PB-2, with the K-O 1970 precedent caveat
already of record). Delta/flag: the PRINTED endpoint labels in Rao
1961 Eqs. (8)/(9) appear swapped vs the physics (p_b at E, p_a at
D as printed) — reported verbatim by the reader; GENO's
CSTR_PA/CSTR_PB implements the physically correct pairing; keep the
flag for any future citation of those equation numbers (§8 duty).

3.4 HUMPHREYS-THOMPSON-HOFFMAN 1971 (FIXED-INLET PLUG). Their
change vs Rao: fixing lip radius y_E, injection angle beta, and
everything upstream of characteristic BT converts lip
transversality into identically-satisfied conditions (NO new
multiplier — variations suppressed), the general isoperimetric
Int g(eta, etadot, p) dx with constant lambda4 replaces
fixed-length-only, and the lip optimum moves to an OUTER PARAMETRIC
loop; Rao recovered exactly at g = 1, tau = delta* = 0 (their Eqs.
(23)-(28)). Containment: (P) expresses fixed inlet as the
attachment/contract data (Lambda attachment set + Gamma_d interface
with fixed upstream data) and the fixed-(eps,L) corner bookkeeping
is exactly the S21 lambda_e re-reading (constraint shadow price
instead of free-endpoint vanishing); their outer parametric loop is
the program's nested outer design parameter pattern (M0's phi
placement: outer, non-variational, moving data family and measure).
Their start-line finding of record ("for compatible start lines the
two techniques yield the same results"; transonic model criticality)
is a 1971 precedent for the program's interface-contract discipline
(stage-A audits; GENO IVL twin checks in [X-A1IM]) — see §7.4.

3.5 HOFFMAN 1967 (CHEMICALLY REACTING, MULTIPLIER FIELDS).
NOT a restriction of (P) (refuter A2): a reacting state (species
PDEs + sources) is outside (P)'s S1 steady-Euler frozen state
class — this row is the Route-B/T7(a) PATTERN instantiated on the
reacting system, containment structural per §6(a); its structural
content (adjoint PDEs on flow characteristics; g_i = 0 on the exit
characteristic; E-residual Eq. (78); derived Mach-line surface) is
contained in the program's field-level T7(a) + Lemma-B adjoint
(structure), and its E-residual is already a VI.3 certificate.
HONEST BOUNDARY (unchanged by this review): the program's
INSTANTIATED thermo class is frozen thermally-perfect (user pin P1)
— finite-rate chemistry is contained STRUCTURALLY (the adjoint
route does not care about source terms; Scofield-Hoffman
demonstrate it) but deliberately NOT instantiated; it is priced by
the [T-EQBR] frozen/equilibrium bracket and the N4 ladder, and
Hoffman 1967 p. 676 (corner bijection dies for reacting gas; E = 0
on fields replaces the algebraic corner) remains the classical
proof of exactly where the closed-form boundary sits (already in
D2 b0 item 2; M0 T-T3-CE cites it).

3.6 SCOFIELD-HOFFMAN 1971 (NONEQ SIMPLE DISSOCIATING + ROTATIONAL
FROZEN/EQUILIBRIUM, BL IN OBJECTIVE, CLOSED-FORM RELAXATION).
Adds to 3.5: rotational per-phase data (per-streamline H, S — the
program's F2 stratified (q; s, h0) duty is exactly this data class);
tabular state relations admitted ("need not be restricted to
thermally perfect gases") — the classical precedent for the
[DIR-THERMOTAB] table-reading backend; the closed-form wall-slope
update etadot = lambda3/[lambda2 - (1 + ddelta/deta)(eta+delta)^nu]
is the classical ancestor of gradient-driven wall relaxation (the
program's TR-SQP on spline DOFs generalizes it to arbitrary
constraint activity). Their SCIENTIFIC finding — noneq optima lie
CLOSER TO FROZEN contours; "frozen flow designs ... should be
employed if actual nonequilibrium designs are not performed" — is
the classical twin of the program's freeze-at-CJ gamma_eff closure
(already D2 b0 item 5) and now carries equation-level provenance.

3.7 HOFFMAN-SCOFIELD-THOMPSON JOTA 1972 (BL IN THE LOOP). General
isoperimetric slots (length / exit radius / surface area) =
instances of the program's constraint vector c with multipliers
reported as marginal values (VI.5); their measured verdict — BL
inclusion in the optimization recovers <= 1.32% of a 0.6-2.3%
friction loss, i.e. <= 0.018% of thrust, "truly insignificant" —
is the classical evidence FOR the program's declared viscous-
closure layering (D-DOM: viscous closure = declared model layer;
optimize inviscid + correct a posteriori). The design equations'
EOS-generality statement ("other equations of state could have been
used") anticipates the program's EOS-general directive VI.4bis(iii).

3.8 JOHNSON-THOMPSON-HOFFMAN, C&F 1974 (VARIABLE-INLET PLUG,
ROTATIONAL, a = a(p, P, H)). The most general classical plug
brick: frozen-or-equilibrium mixture, per-streamline (P, H),
free lip radius AND free base radius as outputs, general
isoperimetric g, Bolza problem, simultaneous wall+lip relaxation.
Containment: the F3 plug-sector instance of (P) with rotational
per-phase data (F2 engine) + the lip/attachment constraint slots;
their transversality at the lip lambda1_E = -(p - p_a)/(rho u)|_E
is the classical form of the lip corner density the program
measures as dJ/dy_lip ([X-O33B] R3). Their declared limits (p_a > 0
required — lip radius diverges as p_a -> 0 with their base model;
lengths > ~20% of perfect plug) are classical instances of the
program's vacuum no-optimum theorem (Part IV (i): sup unattained at
Pa = 0) and of the N2 base-closure band. Their sensitivity verdict
(thrust insensitive to +/-25% base-model constant, GEOMETRY quite
sensitive) sharpens the program's DUTY-10 framing.

3.9 ALLMAN-HOFFMAN 1981 (DIRECT METHOD). A 2-parameter polynomial
class + NLP, motivated by exactly the maintenance cost the indirect
route imposes; measured price <= 0.2% (vacuum) / up to 0.66% (with
backpressure) vs Rao. Containment is TWOFOLD and exact: (i) the
program's driver IS a direct method (TR-SQP on spline DOFs) — with
the S18 verdict "the Rao optimality conditions REACHED VIA THE
GRADIENT, never imposed by an outer loop" the program executes the
direct route while keeping the indirect conditions as
CERTIFICATES/oracles, resolving the classical direct-vs-indirect
trade rather than picking a side; (ii) their finding that the
polynomial class limits achievable thrust at backpressure is the
classical instance of the program's DESIGN-CLASS diagnosis of
record (S19/S20: the residual's dominant term is the class; the
discharge is adaptive knots, not more uniform nodes).

3.10 RAO-BECK 1994 / RAO-BECK-BOOTH 1999 (DEF). Already the
subject of the program's own EQ-v2 adjudication; this review adds
the page-level cross-checks: (i) the 1994 Eq. (4) boundary and the
1999 gamma-free boundary function Eq. (6) are both contained in
the program's (G)/Lambda-form margin (S4 THEOREM: (G) with
perfect-gas Lambda IS Eq. (4); the 1999 Eq. (6) finite-difference
form corresponds to the Lambda-form with FD Lambda — GENO's own
implementation, bound (b) bands derived in [X-MGOV]); (ii) the
1999 paper's finding "the upper limit of vacuum performance for a
given length coincides with the boundary of the valid region" is
the classical statement of margin-ACTIVITY at the optimum — the
classical statement CORRESPONDING TO the content of Direction A's
margin-constrained KKT reading (Direction A itself stays
CONJECTURE, no promotion here); (iii) EQUATION-NUMBERING TRAP of record:
"Eq. (4)" in 1999 is dR/dX = tan(theta+alpha); the boundary
relation there is UNNUMBERED (perfect gas) or Eq. (6) (general).
Any citation "Rao-Beck Eq. (4)" must name the 1994 paper (M0/
advisory citations do — verified consistent). Jump location: at D'
on the chosen right Mach line, kernel-side end of the control
surface, landing ON the boundary — matches the program's S24
DE-side bucket construction (lipward chain of the last val = 0
crossing as the direct D'-analog).

3.11 VEEN 1974 (SHROUDED PLUG). Two DECOUPLED Rao problems (C+
shroud, C- plug) sharing one kernel + base-pressure matching;
family-array inversion (every kernel point -> a member; corner
conditions read backwards give the (p_a, p_b) each member is
optimal for). Containment: the shrouded topology sector of (P);
the duty-split question the averaged theory poses (PB-3) has no
classical counterpart. The GENO implementation bugs of record
(S4/S5/S6: masses over-imposed, Eq. 9 dropped, coupled modes
under-constrained) and the base-model unreliability finding (§7.5)
stand unchanged.

3.12 KRAIKO-OSIPOV 1970 (TRAJECTORY-AVERAGED). The structural
ancestor, already adjudicated (mandatory citation, T7 precedent
note; PB-2 "first" wording program-internal). CONTAINMENT
STATEMENT (refuter-corrected, A1a): (P) contains ONLY the
FIXED-PROGRAM restriction of K-O — prescribed trajectory =>
exogenous weight measure; K-O's full problem carries an
ENDOGENOUS weight W(t) = lambda2 k/m (the trajectory adjoint,
coupled through the flight-ODE multipliers of their (3.1)),
i.e. a coupled nozzle+trajectory co-optimization that (P)'s
exogenous-mu contract does NOT express — structural
non-containment §6(g). This review's
page-level additions: their §4 mechanism is precisely "average the
ADJOINT weight, not the flow" — time-invariant dimensionless inner
field => averaged multiplier W-mean satisfies the same optimality
system => optimum belongs to the classical family with only member
SELECTION carrying the average; this is the exact analogue of the
T-T3 collapse (and their inlet-similarity hypothesis is the
trajectory twin of H3). Their §5 short-nozzle case (first condition
holding at EVERY instant) is the stationarity-level T4 ancestor
(already registered, S14 F-KO5). Their machinery is Route B WITH
discontinuous multipliers and closed forms on the closing
characteristic — the same objects GENO/the program carry. NOT
present there (verified at page level): cycle measure, T0
exactness, O(St) pricing, certificates, margin governance, the
collapse DICHOTOMY (their §4 collapse has no T4-side companion
theorem), measure-selects-topology.

3.13 SHMYGLEVSKII 1980 SURVEY. Contains: the Route A/B taxonomy
(absorbed in §2); rotational data in Route A (H(psi), S(psi)) —
NB: Route A is NOT irrotational-only in the Soviet line; the
program's C1-audit scoping of the CLOSED FORM to
irrotational-homentropic data remains correct for the Rao-form f2
invariant (single isentrope alpha(V)), while the Soviet
two-sided-extremum equations (2) carry per-streamline entropy —
containment via the F2 stratified extension owns this (exit-gate
duty, unchanged); the Legendre-type rejection condition (6) (1962)
and Fedorov 1975's general-point version — see §7.2 (candidate
identity with the Lambda-form boundary); the SECOND SCHEME
(discontinuous shockless solutions: shock + contact OUTSIDE the
determining triangle, corner conditions (7)) with the Fig. 4
COMPLETENESS map ("three schemes give the optimum for ALL nozzle
dimensions", ideal gas) — the classical optimality statement for
the discontinuous regime that the O3 ledger obligation needs (see
§7.1, now page-verified); entropy-as-control explored and found
unrealizable; SWIRL: Naumova-Shmyglevskii 1967 "thrust can be
increased by twisting the flow" — classical precedent to file next
to the mean-swirl panel's recovery-asymmetry adjudication (§8
duty); 3-D general-method nozzle solved (Borisov-Mikhailov) — the
classical existence proof that Route B survives in 3-D exactly
where Route A dies, consonant with the program's B-lite/F6 route
being field-level; the accuracy-discipline quote ("0.3% of thrust
is extremely important") as classical support for the program's
certificate bars.

3.14 STERNIN 1961 (DAN ORIGINAL). The boundary derivation
(dy/dalpha = 0 on the pencil characteristic; explicit gamma=const
boundary Eq. (4); "shockless solutions of the variational problem
are impossible left of C0") — the classical object the program's
A_t margin/certifiability boundary generalizes, and the ancestor
Rao-Beck cite. Now read in the ORIGINAL (see §7.1). Transcription
cautions on the scanned Eq. (4) middle terms are declared in the
reader notes; the S4 THEOREM equivalence chain (Lambda-form ==
Rao-Beck Eq. (4)) does not depend on this transcription.

3.15 NON-VARIATIONAL CORPUS (Migdal 1972; Angelino/Lee via Onofri;
TIC/Landsbaum line; TOP parabola; conical/Malina; NASA RP-1104;
NASA SP-8120; Johnson-Boney 1975; Moretti 2002; the semiempirical
family flagged by Rao's 1961 review). COVERAGE BY ROLE, not
containment (refuter B6: these members are non-variational and
outside the §0 claim): they are constructions/surrogates/closures, and the
program assigns each its slot — ideal/TIC = baselines and oracles
(GENO types 0/1); TOP = documented geometric surrogate (PB-1 scan
family); conical = divergence-factor closure; Angelino plug =
ideal-adaptation closure carrier (T4's H-T4, with Onofri's
planar-only validity caveat now page-anchored); Migdal = the
two-wall design-space geometry (max area ratio at zero base
height; truncation freedoms) whose optimization he himself defers
to Rao; RP-1104's graphical truncation tangency = the classical
cheap surrogate the bound ladder prices; Johnson-Boney = the
tabulated-real-gas MoC backend pattern ([DIR-THERMOTAB]'s
classical ancestor), reclassified non-variational (§7.6); Moretti
= F4b fitted-front methodological support. SP-8120 carries two
statements of record: the institutional FAILURE-BOUNDARY figure
(Fig. 6, gamma-dependent, "the design method fails for nozzle
lengths less than some minimum") — the handbook-level echo of
Sternin's boundary, useful for P-1 framing — and the
plug-optimization GAP declaration ("a method for directly
optimizing truncated aerospike or plug nozzles has not been
developed"; bell procedure only at p_b = 0 and then BEATEN by
truncated-ideal with base included) — the institutional record
that the truncated-plug problem the averaged theory poses (PB-2,
T4 sharpness) was open at handbook level.

3.16 THE TWO SAPIENZA THESES (the GENO lineage itself). Viviano
2023: implements TOC/DEF/TOP in gamma=const AND frozen
thermally-perfect form; carries the explicit generality claim (p.
82) that the Euler+transversality conditions are
fluid-independent while the closed-form loci are gamma=const-bound
— the thesis-level statement of exactly the program's
closed-form-as-oracle vs field-level split; his boundary function
psi (4.27-4.28) is the finite-difference Lambda-form (the GENO
boundaryfunction lineage); his DEF reading ("suboptimal by
construction") sits in tension with Shmyglevskii's completeness
map — see §7.3. Valeriani 2019/20: documents GENO v3.x lineage;
executes Rao's plug outside its perfect-gas hypotheses with the
honest caveat ("stressing the results of Rao outside the
hypotheses"); PSO/fminsearch wrappers = direct-method instances.
Both are contained as per-phase instances; neither contains any
averaged/cycle content (verified: zero RDE/detonation content).

## 4. What the framework adds that is in NO corpus member
## (novelty status unchanged; anchored to the existing
## query-bounded adjudications G2/G3/G6/G14, D2)

 (1) The cycle measure mu as a first-class object with the
 averaged objective J = Int F dmu and its hypotheses audited
 (D-MU; T-O2 log-uniform; atomic-measure discipline).
 (2) T0 exact steadification (instantaneous thrust CONSTANT for a
 single rotating mode) — used tacitly as a fact by the EAP
 doctrine, proved as a theorem here.
 (3) The collapse DICHOTOMY with proven boundaries: T-T3 pointwise
 collapse (fixed wall) + T-T4 peak-design (free boundary) +
 sharpness counterexamples + the breaker map (T-T3-MAP) — the
 corpus has the trajectory-affine instance (K-O §4) and the bound
 precedent (K-E), never the dichotomy nor the cycle instance.
 (4) The WEIGHTED transversality (**') with the theorem that the
 naive average of corner conditions is wrong outside the T3 class
 — with the K-O 1970 trajectory precedent stated inline (their
 (3.2)/(4.4) time-integrated endpoint conditions are the weighted
 structure's ancestor, per the T-T7FS precedent note): the
 unfound object is the CYCLE instance + the R(xi)·w(xi)
 factorization + the naive-average-is-wrong THEOREM.
 (5) Margins/certificates as first-class: the Lambda-form validity
 margin as an EOS-general monitored field (S4), the margin-
 constrained KKT with mu pricing shock-freeness (mu under the O1
 B-stationarity qualifier of record until discharged), REQ-NONSTALL/G1,
 the tolerance-ball backoff [X-TBAK] — the corpus states
 boundaries (Sternin; SP-8120 Fig. 6) but never carries them as
 constraints with multipliers and rejectors.
 (6) The Rao=adjoint identification MEASURED (O3.1/O3.2/O3.3),
 bridging Route A and Route B executably — absent from all three
 published banks.
 (7) Measure-selects-topology (OP-11) and the sector tournament —
 the corpus optimizes within a topology fixed a priori (Veen's
 shroud+plug is composed, not selected).

## 5. Both classical ROUTES are contained — the precise statement

The program's T7(a) is a two-limb statement: closed-form limb
(Route A, irrotational-homentropic subclass, oracle/initializer)
and field-level limb (Route B, general S1 data, executably the
reverse-AD discrete adjoint). This review verified at page level
that the corpus itself ALREADY adjudicated the relation between
the limbs: Hoffman 1967 (Route B) proves Route A's corner
bijection dies beyond frozen data; JOTA 1972 derives Route A's
surface-characteristic condition FROM Route B transversality;
HTH 1971 recovers Rao exactly as the g = 1 inviscid special case;
Shmyglevskii 1980 declares Route A exhausted and Route B general.
The program therefore did not invent the subordination of Route A
to Route B — it inherited it from the corpus's own verdicts and
made it EXECUTABLE (AD adjoint with certificates) and AVERAGED
(the mu-integral with (**')). That is the honest formulation of
"generalizes all variational approaches".

## 6. Honest non-containments (all pre-declared; none new)

 (a) Finite-rate chemistry INSTANTIATION — structural containment
 only; excluded by user pin P1, priced by [T-EQBR]; Hoffman 1967 /
 Scofield-Hoffman remain the classical references the field-level
 engine would follow if the pin ever moves (N4 ladder).
 (b) Two-phase / gas-particle (Kliegel; Sternin's later books;
 Hoffman's gas-particle companions) — declared exclusion P2;
 DUTY-2 architecture warning stands.
 (c) BL-IN-THE-FUNCTIONAL (JOTA 1972; Scofield-Hoffman tau,
 delta*) — STRUCTURAL non-containment (refuter A1b): it modifies
 the objective AND the effective state model, while (P)'s state is
 pinned to the S1 steady-Euler solution; the program's viscous
 closure is a declared model layer, NOT carried in the functional.
 The classical corpus itself measured the in-loop gain to be
 insignificant (<= 0.018% thrust) — evidence FOR the layering,
 not a containment.
 (d) 3-D classical solutions (Borisov-Mikhailov) — the program's
 3-D is F6/B-lite, unexecuted; no containment claim is made.
 (e) Base-flow PHYSICS — the corpus's p_b closures are declared
 crude by their own authors; the program prices them (N2 band,
 DUTY-10) and inherits no better model.
 (f) Off-design/self-adjustment content of the 1961 review (plug
 altitude compensation narrative) — performance analysis, not
 variational; contained only as the (Pa-linearity) Corollary C2
 altitude duality where applicable.
 (g) KRAIKO-OSIPOV COUPLED TRAJECTORY-ADJOINT WEIGHT — STRUCTURAL
 non-containment (refuter A1a): K-O's weight measure is ENDOGENOUS
 (the trajectory adjoint lambda2(t), coupled to the nozzle through
 the flight ODEs), while (P)'s mu is exogenous contract data;
 contained only in the fixed-program restriction (§3.12). The
 program's own bilevel frontier (PB-4, chamber-nozzle coupling)
 is the analogous coupled object on the RDE side and has its
 declared owner; no claim of containment of the coupled K-O
 problem is made.

 [ADDED BY NAME 2026-08-13, D-03 of the confrontation review
 (user-ratified window F-SERVICE); the claim-18 containment
 statement is re-enunciated BELOW with this extended list.]
 (h) DESIGN VARIABLE INSIDE THE ELLIPTIC REGION => MIXED-TYPE
 ADJOINT (KT2015, abstract p.181 "including its subsonic part";
 Eq. (3.3) p.188 "elliptic for V<1, hyperbolic for V>1"): (P)
 answers elliptic patches with O1, which FREEZES the wall upstream
 of the new interface — i.e. cancels exactly the question the
 paper poses. Owner: F2 / future research; declared non-goal under
 the L4 pin. (Judge-verified: problem_book O1 freezes the wall;
 this §6 previously listed only (a)-(g).)
 (i) ENDOGENOUS-CYCLE FAMILY — two members of one family:
 Kraiko-Osipov (endogenous trajectory WEIGHT, (g) above) and
 Zahr-Persson (periodicity imposed as a STATE constraint
 u^(0) = u^(Nt), whose formal signature is one term: the adjoint
 acquires lambda^(0) in the terminal condition and ceases to be a
 backward evolution, becoming a two-point linear BVP; their Eqq.
 (6), (23), (30)). In K-O the endogeneity is in the WEIGHT, here
 in the STATE. WORDING CORRECTION of record: (P) couples the
 phases through the SHARED DESIGN (T7(b), T7(c)) — the correct
 formulation is "no STATE coupling between phases", never "no
 coupling".
 (j) VECTORIAL THRUST CRITERION / PARETO SELECTION (Kraiko 2016
 p.122: optimization of the pair (R_x, |tan alpha|) with selection
 on the Pareto front). Preferred and recommended defense:
 SCALARIZE — "thrust-direction constraint / vectorial thrust" is
 added explicitly to the constraint vector c of A_gen(c), which is
 the defense the paper itself de facto operates (direction used as
 a THRESHOLD on the front). If not scalarized, this is conceded as
 a third non-containment.

 CLAIM 18 RE-ENUNCIATED OF RECORD (2026-08-13): no work in the
 reviewed corpus is a variational maximum-thrust nozzle
 formulation whose core is not a restriction of (P), WITH the
 non-containments (a)-(j) above declared BY NAME (the (h)/(i)/(j)
 additions are pre-emptive declarations, not falsifications:
 KT2015's subsonic-part design, the endogenous-cycle family, and
 vectorial-thrust selection are answered by O1-freeze, exogenous-mu
 contract, and scalarization respectively).

## 7. NEW FINDINGS OF RECORD from this review (each with its class)

7.1 O3 LEDGER OBLIGATION — BOTH SOURCES NOW PAGE-VERIFIED
[MEASUREMENT/provenance; touches PROGRESS BLOCCATO-2 and M0 S20
block CITATION STATUS]. The M0 text of record says Sternin 1962
and "Shmyglevskii 1981" are cited VIA Rao-Beck only, queued for
acquisition. THIS REVIEW ESTABLISHES: (i) dan25254.pdf IS Sternin's
Russian ORIGINAL (DAN SSSR 139(2):335-336, 1961; the 1962 Sov.
Phys. Dokl. citation is its translation) and it was read in full;
(ii) the file 0041-5553(80)90091-9.pdf IS Rao-Beck's Ref. 4
(Shmyglevskii "Variational Problems of Gas Dynamics", USSR CMMP
Vol. 20 No. 5, pp. 113-127 — Rao-Beck print "1981", the journal
issue is 1980; translation-year discrepancy, same pages, same
title) and it was read in full. CONSEQUENCE: the acquisition duty
is DISCHARGED at document level; the O3 obligation's content
question (classical jump-depth optimality) now has its primary
text: the 1980 survey's second scheme + Fig. 4 completeness map IS
a classical optimality claim for the discontinuous regime (ideal
gas, corner conditions (7)). The O3 hard gate can move from
"acquire and verify" to "adjudicate the found text against the
EQ-v2 claims" (F1b/F4b owner unchanged). Bibliographic correction
duty: "Shmyglevskii 1981" -> "Shmyglevskii 1980 (USSR CMMP 20(5):
113-127; transl. printed 1981)" wherever cited.

7.2 CANDIDATE IDENTITY: SHMYGLEVSKII'S REJECTION CONDITION (6) vs
THE (G)/LAMBDA-FORM BOUNDARY [QUESTION -> named duty; NOT a claim].
Shmyglevskii 1980 §1 derives a Legendre-type "rejection" condition
(Eq. (6), 1962: theta-range bounded via Lambda-like quantity
arctg[sin 2alpha/(cos 2alpha - w alpha_w tg alpha)], alpha_w =
partial alpha/partial w — note the structural similarity to
Lambda = V dalpha/dV) whose violation triggers the discontinuous
second scheme. The program's (G) boundary (S4) was derived from
degeneracy of the surface march (Rao-Beck route). Whether (6) ==
(G) (i.e. the Soviet second-order rejection condition and the
Anglo-American first-order solvability boundary are the same locus
in different coordinates) is NOT established here and would be a
clean rigor lemma: if true, the Lambda-form margin acquires a
second, independent classical derivation (second-order/Legendre
provenance) and the "Rao-vs-Zucrow naming inversion" translation
table extends to the Soviet convention. Proposed owner: F4b theory
WP (with O1-O3 cluster). Falsifier: symbolic comparison at gamma =
1.4 where tractable, else machine identity on the [X-VMON]
247-point grid at derived tolerance (refuter C3 wording).

7.3 DEF-OPTIMALITY TENSION OF RECORD (three-way) [ADJUDICATION
INPUT for F1b/O3; no side taken here]. (i) Viviano p. 50-55
declares DEF "suboptimal by construction" (the back-turning
stretch is not the result of optimization); (ii) Rao-Beck 1994
measure a slight thrust ADVANTAGE at equal length (1.7596 vs
1.7591) and Rao-Beck-Booth 1999 state the given-length optimum
lies ON the validity boundary; (iii) Shmyglevskii's Fig. 4
completeness map claims the discontinuous scheme delivers THE
optimum in its region (for the ideal gas, with the shock+contact
OUTSIDE the determining triangle — a construction NOT identical to
Rao-Beck's PM-jump-at-D'). These three are statements about THREE
different objects (an admissibility-restoration construction; a
boundary-active family; a genuinely optimal discontinuous scheme)
and their precise relation is exactly the EQ-v2 Direction A/B +
O3 adjudication the plan already owns. This review's contribution
is the page-verified statement of all three positions and the
observation that the Soviet second scheme (jump from VARIATIONAL
corner conditions (7)) is a STRONGER classical object than the
Rao-Beck jump (admissibility restoration landing on the boundary)
— the F1b/O3 adjudication should compare the program's
margin-active KKT points against BOTH. NAMED OPEN ITEM (refuter
B4): the Soviet second scheme carries a CONTACT discontinuity
(hm), and the tier-1 certificate list of record (RH + entropy +
Lax + Lopatinskii) is shock-shaped — a certificate class for
linearly-degenerate (contact) fronts is a named F4b open item
before the second scheme can be claimed structurally contained
in tier 1.

7.4 START-LINE / INTERFACE-CONTRACT PRECEDENT [provenance for D1].
HTH 1971's controlled experiment (Rao's linear-sonic-line
assumption vs their transonic model: 34,373 vs 34,375 lbf once
start lines are made compatible; contour differences otherwise) is
the classical, page-verified precedent for the program's
interface-contract discipline (Gamma_d + stage-A audits): the
optimum is conditional on the interface DATA, not only on the
method. Candidate one-line citation in D1 §contract rationale.

7.5 BASE-PRESSURE MODEL UNRELIABILITY, INSTITUTIONAL [provenance
for N2/DUTY-10]. The Veen constants (0.846, M^1.3) reappear as
Onofri Eq. (5.1) and are there reported UNRELIABLE against WG10
data (best modern alternative still [+19%, -15%]); C&F 1974's
sensitivity split (thrust insensitive, geometry sensitive to the
base constant) completes the picture. Strengthens the existing N2
band discipline; no action beyond citation.

7.6 JOHNSON-BONEY RECLASSIFICATION [hygiene]. NASA TM X-3243 is a
uniform-exit-flow MoC design method with tabulated real-gas
thermodynamics and a gamma-sensitivity study — NOT a variational
paper. Its role in the corpus is the classical ancestor of the
table-reading backend pattern ([DIR-THERMOTAB]) and the
gamma-sensitivity evidence (length ratio ~80x across gamma
1.1->1.667 in 2-D). Any internal text implying it carries
optimization content should be corrected (none found in M0; D2 b0
lists it without class — add the label).

7.7 SWIRL-THRUST CLASSICAL PRECEDENT [cross-ref duty]. Naumova-
Shmyglevskii 1967 (constant-circulation twisted-flow nozzle
optimization; "thrust can be increased by twisting") is a
classical variational SWIRL result that should be cited next to
the mean-swirl panel adjudication (TWIN-C fairness, recovery
asymmetry) and checked against N6-2's free-vortex extension scope
(the classical result is Route A with swirl — consonant with
N6-2's "Rao machinery extends verbatim to free-vortex swirl").

7.8 THE 1961 REVIEW'S OWN GAP LIST AS T3-NOVELTY SUPPORT
[provenance for P-1]. Rao 1961 names as UNSOLVED: optimization
with irreversibility (shocks) — the program's tier ladder/DEF/
fitted-front line; side-force parameters — [T-SLRW]; two-phase —
P2 exclusion; E-D base pressure — N2/DUTY-10. A 1961 gap list
that maps 1:1 onto the program's declared structure is clean
introductory material for P-1 (and constrains novelty claims:
the GAPS were named classically; the program's novelty is the
averaged/certified machinery, per §4).

## 8. R4 / PROGRESS DUTIES PROPOSED (advisory pattern — execution
## belongs to the owning sessions; none executed here)

 D-A (PROGRESS BLOCCATO-2 + M0 S20 block CITATION STATUS): record
 the §7.1 page-verification of Sternin (original) + Shmyglevskii
 1980; re-point the O3 obligation from acquisition to
 adjudication; fix the 1981->1980 citation. Owner: next session
 touching PROGRESS (cheap, in-window per never-postpone: it is a
 TEXT edit, but it touches M0/PROGRESS which the S24 carrier
 session owns — flagged for the S24 R3 close).
 D-B (F4b theory WP): the §7.2 (6)-vs-(G) identity lemma, with
 the [X-VMON]-grid falsifier.
 D-C (F1b/O3 adjudication): ingest §7.3 three-way tension; the
 comparison set for O3 is Rao-Beck jump AND Soviet second scheme;
 carries the §7.3 contact-front certificate-class open item
 (F4b).
 D-D (D2 litmap): add the b0 entries/labels from §1 census
 (Johnson-Boney non-variational label; Sternin DAN 1961 original
 identity; Onofri base-model unreliability; SP-8120 Fig. 6
 boundary statement; Naumova-Shmyglevskii 1967 swirl row; HTH
 start-line precedent) + TWO refuter additions: (i) fix the b0
 source-basis PHANTOM line "Sternin 1962 Sov. Phys. Dokl." listed
 among GENO/literature primary PDFs — no such file exists there;
 the original is dan25254.pdf in root literature/ (contradicts
 M0's own "cited VIA Rao-Beck only" honesty statement, now
 superseded by §7.1); (ii) the spike DUAL-VENUE reconciliation
 (BMST v2 = Planet. Space Sci. 4:92-101, same Pergamon text) +
 annotate G6's "never shared-wall averaging" clause against the
 page-verified K-O (3.2)/(4.4) endpoint conditions (pre-existing
 tension, not caused by this advisory). Owner: next D2 hygiene
 window (session class: any [RIGOR] or R3-close window).
 D-E (P-1): §7.8 gap-list framing + §4 novelty phrasing.
 D-F (flag): Rao 1961 spike Eqs. (8)/(9) printed-label swap —
 cross-check against GENO CSTR_PB before any equation-number
 citation of the spike endpoint conditions.

## 9. REFUTER VERDICT (adversarial pass, executed 2026-08-12;
## corrections ABSORBED in the text above, each marked "refuter")

Default-REFUTED pass, ~20 attacks in 6 classes (overclaim,
containment-gap, misattribution, novelty, consistency, duty
hygiene); the refuter independently opened primaries (Rao-Beck
1994 incl. reference list; Shmyglevskii front matter; Sternin
dan25254 both pages; Rao 1961 spike pp. 94-95; Rao 1958 p. 382;
M0; D2 b0/b2; both directory listings).

TALLY: 1 KILLED — the original §0 verdict as a universal
quantifier (restated above: inviscid-Euler exogenous-measure core;
K-O coupling and BL-in-functional named structural
non-containments §6(g)/(c)); 7 WEAKENED with exact fixes (all
absorbed: §3.5 pattern-not-restriction; §3.10(ii) no-promotion
wording; §3.15 coverage-by-role; §7.3 contact-certificate open
item; §4(4) K-O precedent inline; §4(5) O1 B-stationarity
qualifier; §1 spike dual-venue); 16 SURVIVE, of which 5 UPGRADED
to independently page-verified by the refuter itself: §7.1(i)
Sternin DAN 139(2):335-336 (1961) identity; §7.1(ii) Rao-Beck
Ref. 4 = the on-disk Shmyglevskii file ("© 1981 Pergamon",
journal issue 1980, pages/title/volume exact); §3.3/D-F spike
Eqs. (8)/(9) printed-label swap CONFIRMED at p. 94 vs the
functional (3) and Rao's own §4 usage (the D-F verification half
is hereby discharged; the flag stays for citation hygiene);
§3.2's G-H single-contour refutation (Rao 1958 p. 382 verbatim);
§3.10(iii) Eq.(4) numbering consistency in M0. TWO NEW findings
produced by the pass and absorbed into D-D: the D2 b0 phantom
"Sternin 1962" source line; the G6-vs-K-O annotation duty.
DECLARED RESIDUE (refuter E4): a short list of digest-only
quotes (Scofield-Hoffman etadot update + tabular-EOS quote; C&F
1974 lip formula; Viviano p. 82 claim; JOTA friction-loss
figures; Shmyglevskii "functions of speed only" position) is
consistent with everything checked but rests on reader digests —
spot-check before any PRINT citation (folded into D-E).

OVERALL: FIT FOR CIRCULATION AFTER CORRECTIONS — corrections
executed in this same document, same session. The eight §3 rows
supplying an actual restriction of (P) all hold; the honest form
of the generality claim is the §0 restatement, which is exactly
what §5 already argued.
