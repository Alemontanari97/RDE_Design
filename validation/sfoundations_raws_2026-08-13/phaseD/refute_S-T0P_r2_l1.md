# REFUTATION — [S-T0P]/[T-T0P] proof document, ROUND 2, LENS 1
# (hyperbolic-PDE structure: characteristics, admissibility, front
#  conditions, symmetry/group-action correctness, physics of the
#  reduction)
#
# REISSUE OF RECORD (2026-08-17): the original round-2 lens-1 pass
# below (sections A-C, findings F1-F9) targeted REVISION 1 and is
# declared UNCONSUMED by the target's own §11 preamble. This reissue
# (a) preserves F1-F9 VERBATIM (they remain the owed round-2 content;
# the target's §11 cites this file as "F1-F9"), (b) re-verifies each
# of F1-F9 against REVISION 2 (section B0 status table — one item,
# F6, is consumed-in-substance by the declared l0r3-F5 overlap),
# and (c) appends the genuinely NEW objections of the reissue pass
# (section D, F10-F14), deduped against: the round-1 lists
# (refute_S-T0P_r1_l0.md F1-F12, refute_S-T0P_r1_l1.md F1-F10), the
# round-3 lists consumed by revision 2 (r3_l0 r3-F1..F5, r3_l1
# F1..F5 = l1r3-F1..F5), and F1-F9 below. Verdict updated in
# section E.

Target: validation/sfoundations_raws_2026-08-13/phaseD/phaseD_stop_proof.md
(original pass: revision 1, post round-1 disposition per its §10;
reissue pass: revision 2, post round-3 disposition per its §11).
Method: full re-read of the revised document; independent re-derivation
of every load-bearing algebraic step; dedup against BOTH round-1 lists
(refute_S-T0P_r1_l0.md F1-F12, refute_S-T0P_r1_l1.md F1-F10) — every
objection below is checked NEW against those 22 items, and most attack
text that EXISTS ONLY IN REVISION 1 (so they could not have been raised
before). Standard applied: the binding SOTA-rigor contract of the Phase
D brief (labels must match proof content; every claim falsifiable;
variable-gamma status accurate; absence of known literature routes is a
finding).

==============================================================================
## A. RE-VERIFIED SOUND (for the record — no objection)

[REISSUE NOTE: A1-A7 re-checked against revision 2; all still hold.
The revision-2 additions to the algebraic core (the [L-INC] per-clause
proof on stratum (A); the H9 tilt arithmetic u.n ~ 0.854c at 20 deg /
0.28c at 45 deg with u = 1.2c, u_r = -0.8c admissible in K; the
0.8 sqrt(2) c ~ 1.13c box arithmetic) were independently recomputed
and are CORRECT as printed.]

The following were independently re-derived and CONFIRMED at abstract
EOS; round-2 raises no objection against them:

 A1. [L-XWALL3] solve. Cross-checked by a shorter independent route the
     document itself enables but does not use: by L-COMPAT's remark
     D_M eta = D_W E, the cross term is D_W E . d with
     d = (0, n_x, n_y, n_z, 0); computing D_W(-rho g) in conservative
     variables gives d(-rho g)/d(rho u_i) = g'(S) u_i / theta, hence
     D_W E . d = (g'/theta)(u.n) = 0 at slip — the lemma's conclusion,
     with dS = 0 never needed explicitly. The two routes agree; the
     lemma is solid (for STATE-form traces; see F5 below for what its
     APPLICATION to the weak side consumes).
 A2. [L-XSON3] parity/rotation factorization det J_5 = (rho u) det J_4
     at w = 0: recomputed entry-by-entry; correct.
 A3. [L-XC3D] (KEY): recomputed; in fact dp = -rho u du from the frozen
     momentum flux gives dp/rho + u du = 0 identically, so
     theta dS = -dbeta drops out in one line; h_ww = g'/(theta rho u)
     confirmed, off-diagonal parity zeros confirmed.
 A4. [L-COMPAT] both steps (chain rule through A_x^{-1}; the identity
     D_M eta = D_W E): confirmed.
 A5. [L-SPACE] characteristic x-speeds in [u-c, u+c] union {u} and the
     bounded-slope/compact-genealogy claims (including grazing/gliding
     rays at the wall: their x-speed is still >= u - c >= delta, so the
     backward genealogy exhausts the slab in bounded time): confirmed
     as re-scoped.
 A6. The per-front entropy-jump identity behind (EI-x): with spacetime
     front normal N = (N_sp, N_t) and front speed sigma = -N_t/|N_sp|,
     the quadruple jump equals -|N_sp| m [g(S)] with m the (RH-
     continuous) mass flux — so (EI-x) across admissible H6' fronts is
     indeed dimension- and t-inclusion-agnostic, AS LONG AS |m| >=
     m_min > 0 (the G9 scope). Confirmed.
 A7. [P-HB2]/[P-HB3](i') group algebra (linearity of continuous
     homomorphisms, discreteness of the residual constraint set):
     confirmed.

==============================================================================
## B0. STATUS OF F1-F9 AGAINST REVISION 2 (reissue verification)

 F1 (margin-obstruction conjecture false by Galilean boost)
    ...................................... STANDS, UNCONSUMED. The
    §4(B) sentence "no construction inside a uniform u - c >= delta
    box is known — NOT proven impossible" and the G3-row "VALUABLE
    CONJECTURE" line are UNCHANGED in revision 2; the boost
    counterexample applies verbatim.
 F2 (stratum-(B) x-persistent vs x-crossed front incoherence; split-
    falsifier defect inside G3) ........... STANDS, UNCONSUMED. The
    l1r3-F3 repair (regularity class, g3-b bridge) is ORTHOGONAL: the
    "front-crossing uniqueness" primitive, the vacuous "shock-free
    regions between fronts ... along the march" sentence, and the
    undefined "transversal" are all still in the revision-2 text.
 F3 (cheap C^1-vs-C^1 classical route for statement (i); time-periodic
    classical literature absent) .......... STANDS, UNCONSUMED. The
    revision-2 inheritance list still routes (i) through the full
    weak-strong machinery; the P. Qu / H. Yuan-school queries are
    still absent from §9.
 F4 (label-discipline asymmetry: (B)'s demotion criterion applies
    verbatim to (A)'s G7/G8 mints) ........ STANDS, UNCONSUMED. The
    §4 RIGOR CLASS rationale for (B) ("new and unregistered") and the
    (A) THEOREM* label with G7/G8 still PROPOSED-pending-rows are
    both unchanged in revision 2.
 F5 (nonlinear-trace commutation: pure-pressure wall-trace form and
    strong inflow attainment are unnamed STRUCTURAL hypotheses, not
    G2 bookkeeping) ....................... STANDS, UNCONSUMED. G2
    items (b1)-(b4) unchanged in revision 2; the two "[= 0]"
    annotations of the Gronwall chain still consume the unnamed
    structure.
 F6 (gamma accounting: [C-XINJ] a second gamma-restricted
    ingredient) ........................... CONSUMED-IN-SUBSTANCE by
    revision 2 (declared overlap: the l0r3-F5 repair was executed
    "TOGETHER with the G7 gamma count (the substance of unconsumed
    r2_l1-F6)", §11 preamble). The revision-2 audit line and §9
    gamma table now count G1, G7/r-b, G8/r1/r3 route-dependently and
    state the table-enclosure requirement. VERIFIED REPAIRED; no
    residue claimed. The owed disposition row should record F6 as
    consumed via that overlap.
 F7 ((i'') monitor-signature transfer consumes class survival exactly
    where (iii) says it has no standing) .. STANDS, UNCONSUMED.
    (i'') text and its THEOREM label unchanged in revision 2.
 F8 (H8' "discharged per-instance by the same monitor line" — the
    instrument cannot measure the hypothesis) STANDS, UNCONSUMED.
    The sentence is unchanged in revision 2 (H8' block).
 F9 (L-STD essential discontinuity set not closed; closure repair)
    ...................................... STANDS, UNCONSUMED — and
    the repair route needs an UPDATE against revision 2: see NEW
    finding F13 (the l1r3-F4 torus front count makes the sheet
    family countably infinite on the R-line, so the F9 repair's
    "finite union of closed sheets" justification must become
    LOCALLY FINITE union — local finiteness follows from the
    modulo-T count; the conclusion survives, the printed
    justification would not).

==============================================================================
## B. NEW OBJECTIONS (none repeats a round-1 item)

[Original round-2 pass, verbatim of record; status vs revision 2 in
B0 above.]

------------------------------------------------------------------------------
### F1 — The "margin obstruction" sentence and the G3 "valuable
### conjecture" are FALSE AS STATED: Galilean boost of the known wild
### solutions produces admissible fields with uniform u - c >= delta.

ATTACKED TEXT (both added in revision 1): §4(B) "the wild constructions
live at transonic/shear states and no construction inside a uniform
u - c >= delta box is known — NOT proven impossible"; §9/G3 "The
margin-obstruction statement ('no wild construction can maintain
u - c >= delta uniformly') is a VALUABLE CONJECTURE, named here, not
claimed."

OBJECTION. Compressible Euler (isentropic AND full) is Galilean
covariant, and every admissibility notion the document uses transforms
covariantly under boosts: the physical entropy inequality
d_t(rho g(S)) + div(rho u g(S)) >= 0 has S a Galilean scalar, and the
isentropic energy inequality transforms into itself plus exact multiples
of the mass and momentum EQUALITIES. Therefore: take any known
convex-integration wild family (Chiodaroli-De Lellis-Kreml isentropic;
Klingenberg-Markfelder full Euler — the document's own citations),
which are L^inf fields with rho bounded below and velocities bounded;
apply the boost u -> u + U_b e_x with U_b large. The result is an
infinite family of ADMISSIBLE weak solutions, defined on a slab
0 < x < L (restriction), with u - c >= delta > 0 UNIFORMLY (c depends
only on (rho, S), unchanged; u shifted by U_b). This is a "construction
inside a uniform u - c >= delta box", derivable in one line from the
cited literature — so "no construction ... is known" is false in every
useful sense, and the named conjecture is REFUTED as stated. The axial
supersonic margin ALONE is provably NOT an obstruction to wild
behavior: Galilean invariance makes it vacuous as an exclusion
mechanism.

WHAT ACTUALLY CARRIES THE EXCLUSION BURDEN (the repair): the boosted
wild solutions are (a) not t-periodic (they are compactly-perturbed
self-similar solutions of an initial-value problem), (b) not matched to
a FIXED full-state inflow trace s on {x = 0} for all t, and (c) not
wall-bounded. So the only candidate excluders are H8' (t-periodicity),
the H2/H7' fixed inflow trace, and the wall/trace package — NOT the
margin. The G3 pricing paragraph must be rewritten: delete the margin
conjecture or restate it WITH the slab structure quantified in ("no
wild construction with T_t-periodicity and a fixed K-valued full-state
inflow trace on a bounded-cross-section duct is known" — that version
is open and valuable); as printed the conjecture is dead on arrival,
and a falsifier for it (the boost construction) is exhibited HERE.
(Caveat recorded for honesty: the boost argument as given controls
u - c only; whether the boosted fields can also be arranged inside the
FULL H5' K including q_perp <= 0.8c depends on the oscillation
amplitude of the specific construction — but the attacked sentences
quantify only over the margin, so they fall regardless.)

SEVERITY: HIGH for the G3 pricing narrative (a named conjecture of
record is false as stated; the "which hypothesis excludes wild
solutions" discussion misdirects future work toward the margin).
Does not by itself change any theorem label (stratum (B) is already
SCHEMA), but G3's content and falsifier lines must be re-derived.
NEW: attacks revision-1 text; round 1 raised only the ABSENCE of the
convex-integration literature (l0-F8/l1-F9), not the falsity of the
margin-obstruction claims added in response.

------------------------------------------------------------------------------
### F2 — Stratum (B) route incoherence: RDE fronts are x-PERSISTENT,
### not x-crossed; "shock-free regions between fronts ... along the
### march" is vacuous for the class the theorem itself constructs, and
### "front-crossing uniqueness" is the wrong primitive.

ATTACKED TEXT: §4(B) "The shock-free regions between fronts are covered
by (A) restricted along the march"; the [C-MAJDA-3DT]/G3 formulation
"front-crossing uniqueness for the multi-D unsteady fitted front";
H6' "finitely many transversal C^1 front hypersurfaces" (transversal TO
WHAT is never stated in the document).

OBJECTION (physics of the reduction + front geometry). Apply the
theorem's OWN conclusion to a stratum-(B) element: [T-T0P](i) makes q a
steady pattern in the co-rotating frame, so its fronts are helical
sheets {theta - OM t in Phi(x, r)} — the physically generic RDE
downstream front system (trailing oblique shocks) — which EXTEND ALONG
x over finite x-intervals. Such a front crosses EVERY slab
Sigma_x = Omega_x x T_t in its x-range in a curve; it is never crossed
at an isolated x-station the way a time-evolution shock is crossed at
an isolated time. Consequences:
 (a) There are NO "shock-free regions between fronts" along the march:
     the strong side fails to be C^1 on Sigma_x for every x in the
     front's range, so "(A) restricted along the march" covers nothing
     on exactly the instances the theorem is for. The sentence
     describes the x-localized front picture (fronts of the form
     x = psi(y, z, t), like a normal shock), which is NOT the RDE
     geometry — and if H6'-B's undefined "transversal" is read so as
     to admit ONLY x-localized fronts, then stratum (B) silently
     EXCLUDES the physical oblique/helical shock system, an unnamed
     scope restriction of the same rank as G9.
 (b) "Front-crossing uniqueness" is the wrong primitive for an
     x-persistent front. The correct formulation (and the one Majda's
     own theory actually has: the shock as a PERSISTENT free boundary
     of the evolution, here x-as-time) is a two-sided coupled IBVP
     with the front as free lateral boundary, and the uniqueness
     mechanism is a per-slab FRONT DISSIPATION term with a sign (the
     a-contraction shift/weight technology), not a crossing event.
     The document's own "alternative discharge route" ([S-ACFR]
     a-contraction, extremal fronts) is in fact the ONLY named route
     whose shape matches the geometry; it should be the primary route,
     and the [C-MAJDA-3DT] statement should be re-expressed for
     x-persistent fronts (KL condition of the free-boundary x-IBVP,
     which IS well-defined for persistent fronts — the "crossing"
     language is the residue of the wrong picture).
 (c) FALSIFIER GAP inside G3 (R5 violation): [C-MAJDA-3DT] bundles TWO
     contents — uniform KL stability AND "front-crossing uniqueness" —
     but the declared falsifier (vanishing of the bordered Lopatinskii
     determinant on the certified front set) can reject only the KL
     half. The uniqueness half of the bundled conditional has NO
     falsifier; since (per the convex-integration discussion the
     document itself now carries) KL stability alone does NOT imply
     uniqueness in the weak class, the un-falsifiable half is exactly
     the load-bearing half. A conditional whose content is "uniqueness
     holds" with no independent test is not R5-compliant.

SEVERITY: HIGH for stratum (B): the SCHEMA label requires "a proof
route with named gaps"; the primary printed route mis-models the front
geometry of the target class, so the label currently rests entirely on
the one-line [S-ACFR] mention. REPAIR: restate H6'-B's transversality
(name the two front classes: x-localized vs x-persistent), rewrite the
(B) route around the persistent-front free-boundary IBVP with
a-contraction as primary, split [C-MAJDA-3DT] into its KL half (with
the determinant falsifier) and its uniqueness half (with its own
declared discharge route/falsifier), and either admit x-persistent
fronts explicitly or declare the exclusion as a G9-rank scope
restriction.
NEW: round 1 (l0-F2) attacked only the planar-steady -> 3-D-unsteady
dimension jump of the CONDITION; the front-geometry incoherence of the
ROUTE (crossing vs persistence, the vacuity of "between fronts along
the march", the split-falsifier defect) was never raised.

------------------------------------------------------------------------------
### F3 — MISSED CHEAP ROUTE with label consequences: statement (i) on
### stratum (A) needs only C^1-vs-C^1 uniqueness of the x-IBVP, which
### is classical — the printed proof over-conditions steadification on
### G2/G7/G8/H7', none of which that route consumes; the adjacent
### time-periodic classical literature is also absent from the sweep.

ATTACKED TEXT: [T-T0P-E] proof ("By the S1-anchored uniqueness property
applied to the pair (q, g_tau q) — BOTH S1"); [T-T0P] §5 inheritance
list; §9 novelty queries.

OBJECTION. The equivariance half consumes uniqueness ONLY for pairs
(q, g_tau q) in which BOTH members are S1 — on stratum (A), both are
C^1 on the compact slab. Uniqueness of C^1 solutions of a quasilinear
symmetrizable hyperbolic IBVP with identical data is CLASSICAL
technology (exactly the Li Ta-tsien semi-global framework the document
already cites for H6' membership: energy estimates for the x-march,
symmetrizable by u - c >= delta, slip wall = characteristic boundary of
constant multiplicity handled by standard characteristic-boundary
energy estimates a la Secchi) and consumes NONE of: [C-XINJ] (no need
for global M-inversion — work in U-variables), [C-XBVP](a)/(a') (no
relative-entropy convexity), [C-XBVP](b) (no DM traces — both sides
C^1), H7'. It still uses H5' (symmetrizability/margin), H8' or a
cone-localized version, H9, L-XWALL3's content in its classical
(boundary-dissipativity) form, and L-SPACE. Consequence: the
STEADIFICATION statement [T-T0P](i) on stratum (A) is provable at a
STRICTLY SMALLER conditional load than printed — plausibly THEOREM*
with only geometric/bookkeeping conditionals (G4-class) — while the
printed document forces (i) to inherit G7/G8/G2 through the
weak-strong detour, and the §8 M0 delta would propagate that
over-conditioning into the corpus of record. Mis-attributing
conditional load is a label defect in BOTH directions: the heavy
machinery is needed only for (ii) (canonicity against L^inf
competitors), and the document never separates the two consumptions.

ABSENCE (same finding, literature axis): the §9 sweep's only
time-periodic query is "relative entropy weak-strong time-periodic
supersonic duct" — which cannot surface the CLASSICAL-solutions line
that this cheap route lives in: time-periodic classical solutions of
quasilinear hyperbolic systems driven by time-periodic boundary data
(P. Qu's line; the H. Yuan school's temporal-periodicity results for
supersonic Euler flows in ducts/past wedges — existence, uniqueness
AND stability of time-periodic supersonic duct flows in the Li
framework). That literature is simultaneously (a) the natural
discharge technology for the C^1-vs-C^1 route above and for G5, and
(b) a direct novelty threat to the "internal value" claim for the
t-periodic-class uniqueness statement. Queries to add: "time-periodic
classical solutions quasilinear hyperbolic boundary data", "temporal
periodic supersonic Euler duct wedge stability uniqueness".

SEVERITY: MEDIUM-HIGH (no falsehood, but the main theorem's printed
conditional inheritance is not minimal, the M0 delta would enshrine
it, and the sweep as extended in revision 1 still cannot find the
closest known technology).
NEW: no round-1 item concerns the decomposition of the uniqueness
consumption (S1-vs-S1 sufficiency for (i)) or the classical
time-periodic literature; l1-F10(c) only aligned the hypothesis
wording with §5.

------------------------------------------------------------------------------
### F4 — Label-discipline inconsistency: the document's own stated
### criterion for denying THEOREM* to stratum (B) ("the consumed
### conditional is new and unregistered") applies verbatim to stratum
### (A)'s newly-minted [C-XINJ] and [C-XBVP](a').

ATTACKED TEXT: §4 RIGOR CLASS "(B) SCHEMA ... NOT THEOREM*: the
consumed front conditional is new and unregistered, so 'complete
modulo named CITED conditionals' is not available until its registry
row exists and its content is certified"; versus "(A) THEOREM* —
complete modulo the NAMED conditionals ... [C-XINJ] = G7 (NEW, minted
here) ... [C-XBVP](a') = G8 (NEW, minted here)"; header "Label minting
... is PROPOSED here, pending registry rows".

OBJECTION. G7 and G8 are exactly as new and exactly as unregistered as
G3: all three are "PROPOSED mints, pending registry rows", none has
certified content ([C-XINJ]'s r-b root-count not executed; (a')'s
hull certificate r1-r3 not executed). If "complete modulo named CITED
conditionals" requires an existing registry row and certified content
— the criterion the document states in its own voice to demote (B) —
then stratum (A) is NOT THEOREM* either until the G7/G8 rows land and
at minimum the cheap r-b/r1 certificates run; it is SCHEMA, or at best
"THEOREM* pending registration" (a status the label system does not
have). If instead THEOREM* only requires the conditional to be NAMED
in the document (the de-facto reading of (A)'s label), then the (B)
demotion rationale is mis-stated and the TRUE reason (B) is SCHEMA is
the counterexample-adjacency of G3's content — which the document
elsewhere says. Either horn is a defect: the split label's two halves
are graded by different rules, and the audit line inherits the
inconsistency. REPAIR (cheap): grade both strata by the content rule —
(A) THEOREM* with G7/G8 rows landed in the SAME session (SR
discipline makes this executable in-window; r-b is declared "cheap"
by the document itself), (B) SCHEMA for the content reason, with the
registration clause deleted from the rationale.

SEVERITY: MEDIUM (pure label discipline, but it is the document's
headline claim — "THEOREM* on the shock-free stratum" — and the M0
delta repeats it).
NEW: G7/G8 did not exist in round 0; no round-1 item could have raised
the asymmetry.

------------------------------------------------------------------------------
### F5 — The wall lemma is applied to the WEAK side through a
### nonlinear-trace commutation that L^inf/DM structure does not
### provide: the pure-pressure form of V's wall flux trace is a
### structural hypothesis, not a "technicality", and the inflow
### "= 0: same trace s" step consumes the same unnamed structure.

ATTACKED TEXT: §4 proof of (A), the line "[= 0: L-XWALL3]" for the
wall term; H7' "slip wall traces"; G2's classification of (b2) "wall
traces" as "trace/regularity technicalities ... same class as the 2-D
declaration".

OBJECTION. [L-XWALL3] is proven for STATES: both its direct-flux step
("-g rho(u.n) = 0 separately for every slip state") and its
pure-pressure step ("(n_x F_x + ...)|_slip = p(0, n, 0)") evaluate the
nonlinear fluxes AT a K-state satisfying u.n = 0. The §4 wall boundary
term for the competitor V, however, involves the DM-sense WEAK-*
NORMAL TRACES of the vector fields (eta, q_y, q_z)(V) and of the
flux rows of (EU) — functionals that for a bare L^inf field are NOT
given by evaluating anything at a boundary state. "Slip wall trace"
for such V can only mean: the normal trace of the MASS flux vanishes.
That does NOT imply (i) the normal trace of the ENERGY flux rho H u.n
vanishes, (ii) the normal trace of the entropy flux -rho g u.n
vanishes, or (iii) the momentum-flux normal trace is collinear with n
(pure-pressure form): these are traces of DIFFERENT nonlinear fields,
and nonlinear functions do not commute with weak-* traces (boundary
oscillation/concentration is precisely the mechanism — and precisely
what wild-class competitors exercise; note the connection to F1: the
exclusion burden the document shifts onto the trace package makes the
trace package load-bearing, so its content must be honest). Therefore
the application of L-XWALL3 to V's terms consumes an UNNAMED
structural hypothesis: "the wall normal trace of V's full 5-flux has
the slip-state form (0, p~ n, 0) and the entropy-flux wall trace
vanishes (or is <= 0, which suffices for the inequality's
direction)". The same issue sits at the inflow step "Int_{Sigma_0}
eta(V|U) = 0: same trace s": eta(V) and F_mu(V) at x = 0 are
nonlinear in the state, so "inflow trace s" must be defined as STRONG
(L^1) attainment of the full state trace, or the vanishing is
unjustified; H7'/H2 as written do not say which. In BV_loc all of
this is free (strong traces exist) — but H7' admits bare L^inf, and
G2 prices the whole package as bookkeeping "of the same class as the
2-D declaration". After revision 1's own G3 pricing lesson
(bookkeeping -> counterexample-adjacent), the identical honesty move
is owed here: (b2)/(b1) must be itemized as STRUCTURAL trace
hypotheses (b2': pure-pressure wall-trace form; b1': strong inflow
trace attainment), with the note that they are exactly what
oscillatory competitors violate — or H7' must be restricted to
strong-trace classes outright, which changes the advertised strength
of (ii).

SEVERITY: MEDIUM-HIGH: the Gronwall chain's two "[= 0]" annotations
are currently proven only for state-form traces; the named-gap
coverage of the (A) proof is incomplete as printed (a THEOREM*
completeness defect, same genus as round-1's l1-F10(d) but a DISTINCT
consumption: that item was about Gauss-Green against Lipschitz tests;
this one is about which OBJECT the boundary functionals are, i.e.
nonlinear-trace commutation — not raised in round 1).
REPAIR: extend G2 with (b1')/(b2') as above and re-derive the audit
line; or restrict H7' to classes with strong traces and say so in §5.

------------------------------------------------------------------------------
### F6 — Variable-gamma accounting is wrong at the header: [C-XINJ]
### is a SECOND gamma-restricted ingredient, since its discharge is
### classical ONLY at ideal gas, while the audit line and §9 gamma
### table still say "the ONLY ideal-gas instance dependence is
### [C-XBVP](a)".

[REISSUE STATUS: CONSUMED-IN-SUBSTANCE by revision 2 via the declared
l0r3-F5 overlap (§11 preamble of the target); the revision-2 audit
line and gamma table now count the gamma-restricted surface
route-dependently (G1, G7/r-b, G8/r1/r3) and state the certified
table-enclosure requirement. Retained verbatim below for the record;
the owed disposition row should mark it consumed.]

ATTACKED TEXT: audit line "Gamma: ... the ONLY ideal-gas instance
dependence is the inherited [C-XBVP](a) definiteness certificate
[X-IVXC] (gamma = 1.4), exactly as already declared in-house";
L-XREC "at IDEAL GAS it is the textbook statement"; §9 gamma table
("L-XREC's G7 residue: route r-a needs a named abstract-EOS
condition; route r-b is instance-level").

OBJECTION. The document's own G7 status makes the supersonic-root
one-sidedness DISCHARGED only at ideal gas and OPEN at abstract EOS.
The standing gas model of the program is gamma(T) thermally-perfect
tabulated — NOT ideal gas. Hence at the gas model the corpus actually
runs, the chain currently carries TWO instance-restricted ingredients:
[C-XBVP](a) (certified at gamma = 1.4 by [X-IVXC]) AND [C-XINJ]
(classical at gamma const; at gamma(T) it requires either the r-a
Bethe-Weyl-class monotonicity — for thermally-perfect gases the
fundamental derivative Gamma_fund > 0 is expected but is a THEOREM TO
CITE OR PROVE for the tabulated mixture (it can be stated via
cv(T) > 0 conditions), not a free fact — or the r-b interval
root-count, which on TABLES additionally needs certified interpolation
enclosures, a requirement route r-b does not state). The header
sentence "the ONLY ideal-gas instance dependence ... exactly as
already declared in-house" is therefore FALSE by the document's own
ledger: it under-counts the gamma-restricted surface by one
conditional, and the per-statement gamma table entry "L-XREC ...
abstract EOS" is misleading (the LEMMA is abstract-EOS, but the
STATEMENT CHAIN through G7 is not gamma-clean). Under the binding
standard ("variable-gamma status declared for every statement;
statements valid only at gamma = const must SAY so"), [T-T0P-U](A)
and [T-T0P] must declare: abstract EOS modulo G1 AND modulo G7's EOS
condition (r-a) or instance certificate (r-b).

SEVERITY: MEDIUM (accounting falsehood on a mandated axis; one-line
repair in three places: audit line, L-XC3D gamma note, §9 table —
plus adding the certified-enclosure clause to r-b).
NEW: G7 is a revision-1 object; its gamma accounting could not have
been attacked in round 1.

------------------------------------------------------------------------------
### F7 — [P-HB3](i'') as a "monitor signature" consumes the transfer
### mechanism exactly where the document's own (iii) says its
### hypotheses have no standing: the THEOREM label's hedge covers the
### symmetry, not the class survival.

ATTACKED TEXT: §6 (i'') "By [P-HB1] a surviving discrete symmetry
TRANSFERS to the solution: this is a checkable MONITOR SIGNATURE at
transitions"; RIGOR CLASS "(i'') THEOREM (transfer by [P-HB1] given
the named symmetry ...)".

OBJECTION. [P-HB1] transfers a symmetry only under "H1-H9 minus H3"
PLUS the S1-anchored uniqueness property. At a mode transition, the
document's own layer (iii) declares the L4 margin H5' to have "no
standing guarantee", and the transition data of the (i'') classes are
generically NOT T-periodic with any useful period on the transition
window unless the switching schedule is itself periodic (only ONE of
the two named residue classes), so H8' fails on the other; and the
S1-anchored uniqueness property on the transition window is exactly
the machinery whose hypotheses (H5'-dependent: spacelikeness,
nondegeneracy, convexity, wall solve — the document's own (iii) list)
are threatened. So the chain "(surviving data symmetry) => (field
symmetry)" — the entire content of the monitor-signature claim — holds
only on transition windows where the FULL class package survives,
which (iii) says is precisely not guaranteed. As printed, (i'') is
labeled THEOREM with the hedge "given the named symmetry", silently
absorbing "given H1-H9-minus-H3 + uniqueness through the transition"
— a hypothesis-completeness defect (the same genus as round-1 l1-F2,
but on a NEW revision-1 statement); and the monitor design line that
consumes (i'') would read the Z_d signature as diagnostic in exactly
the regimes where the transfer can fail silently (margin loss => no
transfer => absent signature does NOT imply absent commensurate
transition; the signature is one-directional even in-class).
REPAIR: relabel (i'') "THEOREM (conditional transfer: given the named
symmetry AND class survival through the window — H5'/H8'/uniqueness)";
add to the monitor-design consumption note that the signature is
sufficient-only and dies with the certificate.

SEVERITY: MEDIUM (over-label on a revision-1 statement + a
one-directional monitor claim presented as a diagnostic).
NEW: (i'') did not exist in round 0.

------------------------------------------------------------------------------
### F8 — H8' "discharged per-instance by the same monitor line that
### verifies H3" is unsupported for every S1 element except the one
### for which [T-T0P](i) is trivial.

ATTACKED TEXT: H8' "... For the S1 element the hypothesis is
discharged per-instance by the same monitor line that verifies H3."

OBJECTION. The H3 monitor line verifies DATA purity on Gamma_d.
T-periodicity of the S1 FIELD on Omega_march x R is a property of the
solution, not of the data; no data-side monitor can certify it. The
only S1 element whose T-periodicity is instance-checkable with the
current toolchain is the CONSTRUCTED wave-frame-steady object — which
is T-periodic BY CONSTRUCTION because it is already steady in the
rotating frame, i.e. exactly the element for which conclusion (i) is
vacuous (its content for that element reduces to (ii)). For any OTHER
S1 element — the ones statement (i) is FOR — verifying H8'
per-instance would require observing the field in time, i.e. the
capturing/unsteady twin, which the document itself declares
structurally gated (G10). So the printed discharge sentence is wrong
twice over: the named instrument cannot measure the hypothesis, and
the only measurable instance is the trivial one. This does NOT create
a circularity (the universally-quantified reading of (i) needs no
instance check — the document's non-circularity note stands), but the
sentence must be replaced by the honest statement: "H8' for the
strong side is a class hypothesis, instance-checkable only via the
G10-gated twin; for the constructed object it holds by construction."
Note the interaction with F3: on the cheap classical route, the
cone-localized version (G5) removes the issue for (i) entirely —
another reason that route is the right home for statement (i).

SEVERITY: LOW-MEDIUM (one false sentence inside a hypothesis block;
no label change, but it misstates what the instrumentation can do —
an R5-adjacent defect).
NEW: the sentence is revision-1 text (part of the l0-F5/l1-F2
repair); its discharge-claim overreach is a new defect introduced by
the repair, not a repeat of the repaired objection (which concerned
the QUANTIFIER, not the instrument).

------------------------------------------------------------------------------
### F9 — L-STD pointwise refinement: the essential discontinuity set
### need not be CLOSED, but the refinement's hypothesis requires a
### closed N; one-line repair (take the closure), currently a gap.

ATTACKED TEXT: L-STD "If moreover q is continuous off a CLOSED null
set N with g_tau N = N ..."; proof: "take N to be the ESSENTIAL
discontinuity set of q — the complement of the set of points at which
the precise representative ... is continuous."

OBJECTION. The set of continuity points of a fixed representative is
a G_delta but its complement (the discharge's chosen N) is an
F_sigma, NOT closed in general; for an S1 field, the essential
discontinuity set is a relatively open subset of the front sheets
(where the jump is nonzero) and omits the jump->0 boundary points of
each sheet, so it is genuinely non-closed exactly in the physically
generic case of a front dying out inside the domain (attenuating
oblique shock — the same geometry as F2). As written, the pointwise
refinement is applied with an N that fails its own closedness
hypothesis. REPAIR (one line, and it preserves both needed
properties): take N* = closure(essential discontinuity set); the
closure of a g_tau-invariant set under the homeomorphisms g_tau is
g_tau-invariant, and N* is still null because it is contained in the
finite union of the closed C^1 front sheets (each Lebesgue-null).
State it; as printed the proof consumes an unproven "closed".
[REISSUE NOTE: under revision 2's torus front count the sheet family
is countably infinite on the R-line — the repair's justification
must say LOCALLY FINITE union, not finite; see F13.]

SEVERITY: LOW (write-up gap with a stated repair; no label change).
NEW: this is residual slack in the REVISION-1 rewrite of L-STD; the
round-1 items on L-STD (l0-F6/l1-F7) concerned the countable-dense
closure and the g_tau N = N discharge, both of which are now present
— the closedness defect is in the new text.

==============================================================================
## D. ROUND-2 REISSUE — NEW OBJECTIONS AGAINST REVISION 2 (F10-F14)

Deduped against: r1 both lenses (22 items), r3 both lenses (10 items,
the reissue brief's forbidden list), and F1-F9 above. Each item names
the revision it attacks.

------------------------------------------------------------------------------
### F10 — [T-T0P-E]'s in-text falsifier fires on NON-instances: its
### premise "g_tau q in C(s) for all tau" is AUTOMATIC for every S1
### element (by the proof's own first step), so the printed exhibit
### condition rejects true claims; the §9 table states the same
### falsifier CORRECTLY, so the document contradicts itself.

ATTACKED TEXT (revision-1 text, repaired form of l0-F12(c), untouched
by revision 2): §2.3, "FALSIFIER (target labeled precisely per
l0-F12(c)): the theorem itself is killed by an S1 field q with
g_tau q in C(s) for all tau and q not of the form (STD) — which would
refute L-STD (a measure-theoretic construction, machine-checkable)".

OBJECTION (logic of the rejector — R5). Under the theorem's standing
hypotheses (H1-H9 + H3), the condition "g_tau q in C(s) for all tau"
is satisfied by EVERY S1 element of C(s) with NO uniqueness input:
that is literally the first step of the [T-T0P-E] proof (L-EQV3
full-group form + L-INV). Hence the printed exhibit condition is
equivalent to: "some S1 element of C(s) is not a steady co-rotating
pattern". Such an exhibit refutes NEITHER of the named targets:
 (a) not L-STD — whose hypothesis is q = g_tau q a.e. for EVERY tau,
     which the exhibit does not provide (and which, absent the
     uniqueness property, does not follow from g_tau q in C(s));
 (b) not [T-T0P-E] — which is CONDITIONAL on the S1-anchored
     uniqueness property; a class WITHOUT that property containing a
     non-steady S1 element is fully consistent with the theorem
     (vacuous instance) and with L-STD.
So the falsifier as printed has FALSE-POSITIVE rejection power: it
would fire on a benign non-unique class and "kill" a true THEOREM.
This is the mirror image of the r3-F4 defect (those falsifiers could
never fire; this one fires wrongly) — and it sits on the
THEOREM-labeled equivariance half, the document's only unconditional
headline. INTERNAL INCONSISTENCY, same document: the §9 FALSIFIER
TABLE states the correct version ("measure-theoretic construction
violating (STD) for an INVARIANT field (kills L-STD)") — the table
carries the missing invariance premise, the §2.3 in-text line does
not; two falsifier statements of record for the same claim disagree,
and the wrong one is the one at the claim site.
REPAIR (one line at §2.3): add the invariance premise — "an S1 field
q with q = g_tau q a.e. for all tau and q not of the form (STD)
refutes L-STD; an S1 field q in a class VERIFIED to have the
S1-anchored uniqueness property, with q not of the form (STD),
refutes the theorem" — matching the table.
SEVERITY: MEDIUM (falsifier design defect with false-positive power
on a THEOREM-labeled claim + internal inconsistency between the two
falsifier statements of record; the round-1 l0-F12(c) repair fixed
the TARGET labels but left the premise hole).
NEW: not in r1 (l0-F12(c) concerned target labeling, and the repair
introduced this text), not in r3 (r3-F4 is the opposite failure mode
on different propositions), not in F1-F9.

------------------------------------------------------------------------------
### F11 — "the wild solutions attach to non-smooth data" is FALSE in
### the literature: smooth-data non-uniqueness for compressible Euler
### exists (wildness enters at shock FORMATION, not at data
### regularity); the true immunity mechanism of stratum (A) is the
### H6'-A global C^1-persistence HYPOTHESIS, and the sweep has no
### query that can find the smooth-data line.

ATTACKED TEXT (revision-1 text, untouched by revision 2): §4(B),
"Stratum (A) itself is IMMUNE to the convex-integration obstruction:
weak-strong uniqueness against a C^1 strong side is exactly the
regime where relative entropy beats convex integration (the wild
solutions attach to non-smooth data)."

OBJECTION (admissibility/literature). The parenthetical is false as a
statement about the cited field: for multi-D isentropic compressible
Euler there are C^infinity (even compactly-supported-perturbation)
initial data admitting INFINITELY MANY admissible weak solutions —
the wild branching begins at the first shock-formation time, riding
the classical loss of C^1 in finite time, not any data-level
irregularity (Chiodaroli-Kreml line continued: non-uniqueness of
admissible weak solutions with SMOOTH initial data; the mechanism is
smooth data -> shock formation -> wild continuation). Weak-strong
uniqueness protects a smooth solution only ON ITS INTERVAL OF
C^1 PERSISTENCE — which is exactly why the honest immunity statement
for stratum (A) is: H6'-A HYPOTHESIZES that the strong side is C^1 on
ALL of cl(Omega_march) x R (equivalently the compact torus slab), i.e.
"shock-free" is a strong global-persistence CLASS HYPOTHESIS (no
shock formation anywhere in the marched slab, for all time), not an
inheritance from data regularity. Three consequences:
 (a) a false literature sentence of record in the (B)-stratum
     discussion — citable against the document;
 (b) mis-pricing of stratum-(A) MEMBERSHIP fragility: the smooth-data
     wild examples are precisely the warning that C^1 persistence is
     the entire dam — the moment it fails anywhere in the slab the
     instance falls to stratum (B) and the counterexample-adjacent
     G3 regime; the document nowhere says that the (A)/(B) split of a
     given instance is itself decided by a persistence question of
     exactly the kind the wild literature attacks;
 (c) ABSENCE (sweep gap): none of the §9 novelty/threat queries can
     surface this line — "non-uniqueness admissible weak solutions
     ... Riemann shock" and "wild solutions ... entropy inequality
     multi-dimensional" both miss the smooth-data papers; add
     "non-uniqueness smooth initial data compressible Euler" (and its
     'dense wild data' companion).
REPAIR: correct the parenthetical to the persistence-interval
statement; add one sentence to H6'-A or §4(A) naming C^1 persistence
on the slab as the load-bearing hypothesis (instance-checked by the
S1 membership certificate, already declared); add the query.
SEVERITY: MEDIUM-LOW (no label change — the hypothesis is declared,
so THEOREM* survives; the defects are a false literature claim of
record, an unpriced fragility, and a mandated-axis sweep hole).
NEW: r1 raised the convex-integration ABSENCE (l0-F8/l1-F9) and F1
above refuted the MARGIN conjecture by boost; neither touched the
data-regularity claim, which entered with the revision-1 repair.

------------------------------------------------------------------------------
### F12 — G9's breadth is unpriced: contact/slip sheets are the
### physically GENERIC front type of the RDE exhaust, so BOTH strata
### exclude the expected physical field structure — the class C(s)
### itself (H6'), not just the stratum-(B) machinery, omits the
### program's target flows, and Cor 5.1's "every certified solution"
### discharge is silently restricted to slip-free instances.

ATTACKED TEXT: H6' front-admissibility clause + G9 row ("Zero-mass-
flux fronts (contact/slip surfaces, including helical slip sheets)
are EXCLUDED ... declared scope restriction"); Cor 5.1 ("T-T0's
conclusions hold for every certified solution in the t-periodic
class"); §8 registry bullet (the H-DATA monitor consumption).

OBJECTION (physics of the reduction; pricing, not label). The
exclusion itself is declared (G9) — what is NOT declared is its
BREADTH for the program: the downstream field of a rotating
detonation generically carries ZERO-mass-flux sheets, because the
periodic wave sheds convected contact/shear interfaces (the burnt-gas
interface between consecutive cycles, slip lines from the
oblique-shock/detonation triple region) which are ADVECTED through
Gamma_d into Omega_march and, in the steady co-rotating pattern the
theorem concludes, become HELICAL SLIP SHEETS — exactly the excluded
class. In inviscid Euler such sheets do not decay; they persist
through the marched domain. Hence: an S1 candidate with the expected
physical structure fails H6' (both strata: (A) is C^1, (B) admits
only |m| >= m_min fronts) and the class C(s) the theorem quantifies
over EXCLUDES the physically expected pattern — the theorem then says
nothing about it, and the split-label headline ("fronts = SCHEMA")
reads as if the front stratum covered the physical front system when
its admissible-front class may be EMPTY of physical instances.
Downstream consequences, currently unstated:
 (a) Cor 5.1's in-class T-T0/T-SLRW discharge quantifies over
     slip-free instances only; if a certified instance's solution
     carries a contact sheet (e.g. inherited through the interface
     trace s itself, whose H3 profile s_hat may be discontinuous in
     theta — L^inf data admit exactly that), the discharge is vacuous
     for it;
 (b) the H-DATA monitor design line consuming these results inherits
     the same silent restriction;
 (c) the honest leverage note is absent: for contacts the [S-ACFR]
     a-contraction route does NOT apply either (a-contraction
     technology is for extremal SHOCKS; uniqueness with vortex
     sheets is open, and the 3-D vortex sheet is generically
     unstable — the document's own citation), so lifting G9 has no
     named route at all: it is not "new work, not declared" of the
     ordinary kind but a wall.
REPAIR (pricing paragraph, no label change): state next to G9 that
the excluded type is the generic physical one for this engine class;
add the slip-sheet caveat sentence to Cor 5.1 and the §8 monitor
bullet; either add an instance check ("certified solution slip-free")
to the S1 membership battery or declare the coverage conditional;
name the no-route status of the G9 lift honestly.
SEVERITY: MEDIUM-LOW (scope honesty on the theorem's physical
coverage; the M0 delta as instructed in §8 would export the
unrestricted-sounding Cor 5.1 sentence).
NEW: G9 was minted in revision 1 as a declared restriction; no prior
item priced its genericity or traced it into Cor 5.1/monitor
consumption. Distinct from F2 (geometry of SHOCK fronts) and from
r1 l0-F9 (which created G9).

------------------------------------------------------------------------------
### F13 — Revision-2 interaction: the l1r3-F4 torus front count makes
### the sheet family countably infinite on the R-line, so the owed
### F9 closedness repair (and any 'finite union of closed sheets'
### argument in L-STD's excision discussion) must be restated with
### LOCAL finiteness — as currently drafted the repair route would
### mint a false justification when consumed.

ATTACKED TEXT (revision-2 text): H6' "finitely many transversal C^1
front hypersurfaces IN cl(Omega_march) x T_t — i.e. finitely many
MODULO T-PERIODICITY"; its interaction with L-STD's pointwise
refinement (unchanged since revision 1) and with the still-owed F9
consumption.

OBJECTION (write-up trap, flagged before it can be consumed wrongly).
With the torus count, an S1 element's front set on the R-line is a
COUNTABLE union of closed C^1 sheets (the T-translates). Two
downstream arguments silently assumed finiteness on the R-line:
 (a) the F9 repair as drafted above ("N* is still null because it is
     contained in the FINITE union of the closed C^1 front sheets")
     — with countably many sheets, "finite union" is false; the
     correct statement is that the family is LOCALLY FINITE (finitely
     many sheets meet any compact slab, immediately from the
     modulo-T count), hence the union is closed and null and N* =
     closure(essential discontinuity set) is contained in it — the
     conclusion survives, the printed justification would not;
 (b) any reading of L-STD's excision sentence ("N is contained in the
     front set AFTER EXCISION of zero-jump sheets") that enumerates
     sheets must now enumerate modulo T. The document itself does not
     currently contain the false step — the defect is that the OWED
     round-2 consumption (F9) would, if executed against the
     revision-1 wording of the repair, land a justification falsified
     by revision 2's own H6'. One line fixes both.
SEVERITY: LOW (no current false statement in the target; a named trap
for the owed consumption pass, per the never-postpone discipline the
cheap fix should ride the same window).
NEW: created by the revision-2 change (l1r3-F4); could not exist
before it.

------------------------------------------------------------------------------
### F14 — G7 is over-consumed: the formulation-level citation
### ("single-valuedness for (EU-x)") is removable by stating the
### relative-entropy computation in state variables; the necessary
### consumption of [C-XINJ] is the §4 endgame ONLY (plus the branch-
### inverse-on-hull content already inside G8's own clause).

ATTACKED TEXT: §3 X-AS-TIME SYSTEM paragraph ("GLOBAL injectivity on
the K-branch — needed for W(M), F_y(M), F_z(M) to be single-valued
and for the §4 endgame — is the NAMED conditional [C-XINJ] (G7)");
§4 relative-entropy definitions ("These use W(M), F_mu(M) as
functions of M: single-valuedness on the branch = [C-XINJ], G7,
cited here"); G7 row ("Consumed at: (EU-x) single-valuedness, §4
endgame").

OBJECTION (conditional-load minimality — same genus as F3, distinct
consumption). The integrated §4 argument never needs the fluxes as
functions of M: define the relative quantities directly on STATES,
   eta(V|U) := eta(V) - eta(U) - D_W E(U) . (F_x(V) - F_x(U)),
   q_mu(V|U) analogously (using D_M eta(U) = D_W E(U), the L-COMPAT
   remark, which is a LOCAL-diffeo statement at the strong-side state
   only),
and (EU-x) tested against the Lipschitz field D_W E(U) is literally
the regrouped weak form of (EU) for V — no inversion anywhere. The
only place global injectivity is genuinely consumed is the endgame
M_V = M_U a.e. => V = U. (The segment Taylor estimates DO need the
branch inverse along the hull segments — but that is already inside
G8's own clause "staying on the branch", not a G7 consumption; no new
gap.) Consequences: (a) the printed double citation inflates G7's
surface — a reader prices [C-XINJ] as load-bearing for the
FORMULATION, when a one-paragraph restatement confines it to the
final identification; (b) the G7 row's "Consumed at" list and the §8
M0-delta inheritance narrative export the inflated surface; (c) the
r2-route note in G8 ("this route also removes the G7 consumption
from the endgame") then correctly describes the ONLY remaining
consumption — as printed it reads as removing one of two.
REPAIR: restate the §4 definitions in state form (three lines),
reduce G7's "Consumed at" to the endgame, keep L-XREC unchanged.
SEVERITY: LOW (no falsehood in the mathematics; conditional-load
accounting on a mint that the M0 delta will export).
NEW: not raised in any prior round; F3 concerns the (i)-vs-(ii)
split, this concerns the G7 surface within (ii) itself.

==============================================================================
## C/E. VERDICT AND LABEL CONSEQUENCES (updated at reissue)

Original round-2 verdict (vs revision 1), retained of record: the
revision-1 document is substantially harder to attack than round 0:
the algebraic core (§2 group action, §3 bricks) survives re-derivation
(section A), and the round-1 dispositions are real. Findings F1-F9 as
above.

REISSUE VERDICT (vs revision 2): REPAIRABLE. The unconsumed round-2
spine (F1-F5, F7-F9) still stands in full against revision 2 — in
particular the HIGH items F1 (margin conjecture refuted by boost) and
F2 (stratum-(B) route geometry) and the MEDIUM-HIGH items F3
(over-conditioned statement (i)) and F5 (structural trace hypotheses
behind both "[= 0]" steps) are untouched by the round-3 repairs; F6
alone is consumed-in-substance (declared l0r3-F5 overlap, verified).
The reissue adds: a false-positive falsifier on the THEOREM-labeled
equivariance half with an internal contradiction against the §9 table
(F10); a false literature sentence and unpriced persistence fragility
in the stratum-(A) immunity discussion plus a sweep hole (F11); the
unpriced physical breadth of G9 reaching into Cor 5.1 and the monitor
line (F12); a revision-2-induced trap for the owed F9 consumption
(F13); and an over-consumed G7 surface (F14). None of F10-F14 kills
the algebraic core or forces a label change BY ITSELF; but the
document's §8 gating is confirmed correct and MUST hold: the M0 delta
cannot land before the round-2 consumption pass, which now includes
F10-F14, and the F3/F4/F5 label-and-inheritance repairs remain the
blocking items for the exported THEOREM* sentence.
