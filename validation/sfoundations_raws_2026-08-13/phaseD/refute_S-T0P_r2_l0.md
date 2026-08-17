# FILE STRUCTURE NOTE (2026-08-17, appended pass — nothing-lost discipline):
# this file now contains TWO passes. PART 1 (immediately below, findings
# r2-F1..r2-F11) targets REVISION 1 and is PRESERVED VERBATIM — it is the
# unconsumed/OWED object referenced by the target document's §11 honesty note.
# PART 2 (appended at end of file, findings r2b-F1..r2b-F6) is the NEW-LOOP
# round-2 lens-0 pass against REVISION 2; it repeats nothing from any prior
# list on disk (r1_l0, r1_l1, Part 1 below, r2_l1, r3_l0, r3_l1).

# ADVERSARIAL REFUTATION — [S-T0P]/[T-T0P] proof document, ROUND 2, LENS 0
# (functional-analytic rigor: spaces, operators, traces, compactness, quantifiers)

Target: validation/sfoundations_raws_2026-08-13/phaseD/phaseD_stop_proof.md
(revision 1, post round-1 disposition §10). Round-1 objections (l0-F1..F12,
l1-F1..F10) are NOT repeated; every finding below is genuinely new, i.e. it
attacks either (a) text INTRODUCED by revision 1, or (b) a defect the round-1
sweep missed. Each finding states: the claim attacked, the defect, why it is
not a round-1 duplicate, severity, and the repair route. Verdict at end.

Convention: "the doc" = the target file; line references are to the revision-1
text; DM = divergence-measure field (Chen-Frid); "normal trace" = the DM-sense
normal-trace functional; "state trace" = a full 5-component pointwise (a.e. on
the boundary) limit of the field itself.

==============================================================================
## r2-F1 — LABEL INCONSISTENCY (over-label, stratum (A) THEOREM*): the doc's
## OWN downgrade criterion for stratum (B) applies verbatim to (A)

CLAIM ATTACKED: audit line + §4 rigor-class block: "(A) THEOREM* — complete
modulo the NAMED conditionals ... [C-XINJ] = G7 (NEW, minted here) ...
[C-XBVP](a') = G8 (NEW, minted here)".

DEFECT. The doc justifies the (B) SCHEMA downgrade by a REGISTRATION
criterion, stated explicitly in §4(B) rigor class: "NOT THEOREM*: the consumed
front conditional is new and unregistered, so 'complete modulo named CITED
conditionals' is not available until its registry row exists and its content
is certified". By that exact criterion, stratum (A) cannot be THEOREM* either:
[C-XINJ] (G7) and [C-XBVP](a') (G8) are, per the doc's own header, "PROPOSED
here, pending registry rows per SR discipline — no silent mint". A proposed,
unregistered, undischarged conditional is not a CITED conditional of record.
The house THEOREM* definition (STANDARD block of the task, and the corpus
convention) reads "complete modulo named cited conditionals": "cited" is doing
work — it means an object with a registry row and a falsifier of record, not a
label minted in the same breath as the proof that consumes it. The doc applies
this reading to G3 and silently exempts G7/G8.

WHY NEW: round-1 (l0-F2/l0-F3/l0-F4, l1-F3) forced the MINTING of these
conditionals; no round-1 objection addressed the resulting LABEL algebra of
revision 1 — the inconsistency is a revision-1 artifact.

SEVERITY: high (this is exactly the "over-label is a finding" class; the
audit line, §5 header, §7, and §8 M0-delta instructions all propagate the
THEOREM* label).

REPAIR (two admissible routes, pick one and say so):
 (r1) Uniformize on registration: stratum (A) = SCHEMA until the G7/G8
      registry rows exist AND their content is discharged (r-b interval
      certificate for G7; r1/r2/r3 for G8); then THEOREM* by upgrade note.
 (r2) Uniformize on content: restate the (B) criterion honestly — (B) is
      SCHEMA not because G3 is unregistered but because G3 is
      counterexample-adjacent OPEN mathematics (the doc says so itself in the
      G3 pricing), while G7/G8 are certifiable finite checks. Then (A) may
      keep THEOREM* — but the §4(B) sentence must be rewritten, because as
      printed it states a criterion that kills (A) too.
Either way the current pair of labels is not derivable from a single stated
criterion: the document is internally inconsistent at the level of its
headline labels.

==============================================================================
## r2-F2 — WALL TERM: state-level lemma applied to trace-level objects at a
## CHARACTERISTIC lateral boundary; H7' "slip wall traces" is not well-defined
## for L^inf competitors, and the needed structural clauses are not in G2

CLAIM ATTACKED: §4 proof of (A), wall line "Int_0^{x1} Int_{walls x T_t}
W_rel [= 0: L-XWALL3]", together with H7' ("slip wall traces") and the G2
itemization (b2) ("wall traces").

DEFECT. [L-XWALL3] is a POINTWISE STATE identity: its hypotheses are "let U
(strong) and V (any K-valued STATE) both satisfy slip u.n = 0 at the same
wall point", and its proof evaluates eta(V), p_V, and the full flux vector at
that state. For an H7' competitor V in L^inf, NO full state trace at the wall
exists in general. What exists, and all that exists, are DM normal-trace
FUNCTIONALS: each conservative component of (EU) is divergence-free in
space-time, and the entropy quadruple has measure divergence by (EI-x), so
the normal traces of n.F(V) (5 components) and of the entropy spatial flux
exist as bounded functionals on the wall (Chen-Frid). The wall budget
therefore consists of three trace functionals, and L-XWALL3 says NOTHING
about them unless the traces have state structure. Concretely:

 (i)  "slip wall traces" for an L^inf field can only mean: the normal trace
      of the MASS flux vanishes on Gamma_w. That is a well-defined clause.
 (ii) The direct wall term for V is the normal trace of the ENTROPY spatial
      flux (q_y, q_z components against (n_y, n_z) plus n_x eta). At state
      level it factors as -g(S) rho (u.n) and vanishes by (i). At trace
      level THERE IS NO FACTORIZATION: the normal trace of rho g(S) u.n
      is not a function of the normal trace of rho u.n. Zero mass-flux
      trace does NOT imply zero entropy-flux trace for a DM field. This
      implication is exactly what the budget consumes and it is an
      ASSUMPTION, not a technicality.
 (iii) The cross term needs the momentum/energy flux normal trace of V to
      have the pure-pressure form p_V (0, n_x, n_y, n_z, 0) — again a state-
      structure statement with no DM-trace analogue absent a state trace.

Worse, the wall is a CHARACTERISTIC boundary of the x-evolution: at slip
states the boundary matrix n_y A_y + n_z A_z has u.n = 0 in its transport
eigenvalues — this is the uniformly characteristic IBVP regime (Secchi
class), which is precisely where boundary trace regularity is WEAKEST and
where strong-trace theorems fail (Vasseur-type strong-trace results are
scalar and genuinely-nonlinear only; nothing of the kind exists for 3-D
Euler systems at a characteristic boundary). H7''s hedge "strong traces
available in BV_loc" concedes the point for BV competitors but the class is
L^inf. G2's item (b2) "wall traces" prices this as bookkeeping regularity;
findings (ii)-(iii) are NOT regularity — they are structural hypotheses on
the VALUES of the traces, of the same epistemic kind as an extra admissibility
condition on the class, and they are nowhere named.

ABSENCE COMPONENT: the characteristic-boundary IBVP literature (uniformly
characteristic hyperbolic BVPs; loss of normal derivative control; slip/
impermeable walls as THE standard example) is unengaged, although it is the
standard-reference frame for exactly this step. No novelty query in §9
covers "divergence-measure field normal trace characteristic boundary".

WHY NEW: round-1 touched (b)-class only as l1-F10(d) (Gauss-Green against
Lipschitz tests — a different consumption, now G2(b4)) and generic
itemization. The state-vs-trace category error in the wall annihilation, the
characteristic-boundary aggravation, and the ill-definedness of H7''s slip
clause for L^inf fields were not raised.

SEVERITY: high (the wall term is one of the three legs of the §4 budget; as
priced, G2 understates the load: for L^inf competitors the wall annihilation
is CONDITIONAL on unnamed structural trace hypotheses).

REPAIR: restate H7' wall clause as explicit per-field normal-trace
conditions: (w1) mass-flux normal trace = 0; (w2) entropy-flux normal trace
= 0 (or with the favorable sign) on Gamma_w x T_t; (w3) flux normal trace in
span{(0, n, 0)} + (w1)-multiples; note (w2)/(w3) hold automatically for BV
competitors with strong traces and for any state-trace field, and are the
DECLARED price of admitting bare L^inf; add them to G2 as (b2') with the
honest "structural, not regularity" flag — or restrict H7' to BV_loc
competitors and say the L^inf statement is open.

==============================================================================
## r2-F3 — INFLOW ANCHOR: the trace contract at Gamma_d is unstated; the
## entropy-flux inflow inequality is missing; and G7 is consumed at the
## boundary at a THIRD, uncited point

CLAIM ATTACKED: §4 budget line "Int_{Sigma_0} eta(V|U) dA dt [= 0: same
trace s]", with H2/H7' ("inflow trace s on Gamma_d").

DEFECT. For a DM competitor, "inflow trace s" can be given a trace-level
meaning in exactly one good way: the normal trace of F_x(V) at {x = 0}
equals F_x(s) (the x-flux IS the normal flux at an x-slice — this is the one
place the x-as-time framing is trace-friendly, and the doc never exploits
it). But the budget needs MORE than the flux trace:

 (i)  eta(V)|_{x=0} in the budget is the normal trace of the ENTROPY x-flux,
      a separate DM object. Even granting flux-trace = F_x(s), the equality
      eta(V)-trace = eta(s) does not follow: there is no state to factor
      through. What the Dafermos slab argument actually needs is the
      INEQUALITY  (entropy-flux normal trace at Sigma_0) <= eta(s) — the
      x-as-time analogue of "the initial entropy is attained from above" —
      and this clause appears NOWHERE (not in H2, not in H7', not itemized
      in G2(b1), which says only "x-slice normal traces" exist).
 (ii) Alternatively one recovers eta(V)-trace from the flux trace via the
      state reconstruction M -> U — but that is GLOBAL branch injectivity,
      i.e. [C-XINJ]. The doc cites G7 at exactly two consumption points
      ("(EU-x) single-valuedness, §4 endgame", per the G7 ledger row). The
      inflow anchor is a THIRD consumption point, uncited. The ledger row
      "Consumed at:" is therefore incomplete — the same accounting defect
      class the doc's §10 claims was FIXED by l0-F10.

WHY NEW: round-1 never touched the Sigma_0 term; l1-F10(b) was about which
g, not about the trace contract; l0-F10 was about the gap LIST, not this row.

SEVERITY: medium-high (the "= 0" annotation on the inflow term is the anchor
of the whole Gronwall argument; as stated it is not a theorem about the
declared class but about an undeclared subclass).

REPAIR: state the inflow contract as (d1) DM normal trace of F_x(V) at
Sigma_0 equals F_x(s) a.e.; (d2) entropy-flux normal trace at Sigma_0 <=
eta(s) a.e.; note both are automatic for BV/strong-trace competitors; update
the G7 row's "Consumed at" list to include the inflow reconstruction IF the
(d2) route is replaced by reconstruction; itemize (d1)/(d2) inside G2(b1).

==============================================================================
## r2-F4 — [P-HB1] HAS A DANGLING HYPOTHESIS and (i'') IS OVER-LABELED:
## H8' references H3's period after H3 is deleted; for one-shot transitions
## the transfer machinery is vacuous exactly where (i'') advertises it

CLAIM ATTACKED: [P-HB1] "Under H1-H9 minus H3, for ANY data s ..."; [P-HB3]
(i'') "THEOREM (transfer by [P-HB1] given the named symmetry ...)" and its
monitor-signature reading.

DEFECT (two layers).
 (a) FORMAL: H8' (a member of the [P-HB1] hypothesis list) is defined as
     "ALL elements of C(s) are T-periodic in t with the data period T of
     H3". Delete H3 (as [P-HB1] does) and the symbol T is undefined; for
     aperiodic data no finite common period exists and H8' is unsatisfiable
     — the hypothesis set "H1-H9 minus H3" is not a well-formed hypothesis
     set. The parenthetical "(any fixed common multiple works)" in H8'
     presupposes periodicity of the data and does not save it.
 (b) SUBSTANTIVE: (i'') is sold as a MONITOR SIGNATURE at mode transitions:
     "a surviving Z_d in the field is diagnostic of a commensurate
     transition". But the transfer of a surviving symmetry to the FIELD goes
     through [P-HB1], whose S1-anchored uniqueness hypothesis is delivered
     (per this doc) only by [T-T0P-U], which consumes H8' (t-periodic class)
     and H5' (margin). A genuine one-shot transition window has aperiodic
     data (H8' dead by (a)) and, by the doc's OWN (iii), a threatened L4
     margin. So on precisely the windows where the signature is advertised,
     the transfer has no theorem behind it; only the periodic-switching
     subcase (g_{0,T_sw}, data T_sw-periodic) is covered. Labeling (i'')
     "THEOREM" with the annotation "transfer by [P-HB1] given the named
     symmetry" hides that the uniqueness hypothesis is unavailable-in-
     principle on the aperiodic-transition class: the honest label is
     THEOREM for periodic switching schedules, SCHEMA/remark for the Z_d
     one-shot case (or restate (i'') as a conditional whose hypothesis
     includes the uniqueness property AND its own availability caveat).

WHY NEW: round-1 (l0-F1/l1-F1) attacked the FALSITY of old (i) and forced
the (i')/(i'') split; nobody audited the hypothesis algebra of the NEW
[P-HB1] quantifier "H1-H9 minus H3" or the availability of the transfer on
transition windows — both are revision-1 artifacts.

SEVERITY: medium (a THEOREM label on a statement whose hypothesis set is
ill-formed; a monitor-design line consuming a vacuous-in-context transfer).

REPAIR: [P-HB1]: replace the hypothesis list by "H1, H2, H4-H7', H9, H10 +
[H8'-gen]: all elements of C(s) are T'-periodic for SOME common T' > 0" (and
note the aperiodic case is open pending G5); (i''): split the label as above
and re-point the monitor note to the periodic-switching case, with the Z_d
case flagged as heuristic until G5 lands.

==============================================================================
## r2-F5 — [P-HB3](i'): the core predicate "wave count on sub-windows" is
## UNDEFINED at the stated function-space level, and the sigma = t/b
## substitution is not covered by the invoked closure

CLAIM ATTACKED: (i') statement ("the azimuthal wave count takes two
different values n1 != n2 on sub-windows") and its proof ("choose
sig = t/b: s(theta, t) = s(theta - (a/b) t, 0)"; "the a.e. bookkeeping is
the same countable-dense closure as L-STD").

DEFECT (two parts).
 (a) DEFINITIONAL: s is an element of L^inf(Gamma_d x R_t). "Wave count on a
     sub-window" is never defined for such an object. For H3-data it is the
     minimal azimuthal period of s_hat; off H3 (which is the entire habitat
     of (i')) no definition is on file. A THEOREM whose statement contains
     an undefined predicate is not a theorem; the proof's two cases secretly
     SUPPLY a definition (wave count of an exact rotating wave := count of
     its profile; axisymmetric := count 0) but that definition only covers
     the two terminal cases, not the hypothesis "takes two different values
     on sub-windows". Minimum repair: define wave count of s on a window as
     the largest n such that rho_n s = s a.e. on that window (Z_n-invariance
     order), or via the azimuthal Fourier support lattice; then re-verify
     the two case computations against the chosen definition.
 (b) PROOF STEP: from invariance a.e. for every sig, the step "choose
     sig = t/b" evaluates the null-set-infected identity along the graph
     {(theta, t, sig): sig = t/b} — a null set of the (theta, t, sig)
     product. The countable-dense closure of L-STD does NOT license this:
     L-STD's mechanism (mollify in t, Fubini, dense orbit, continuity) must
     be re-run here (mollify jointly in (theta, t) along the group orbit),
     and the conclusion is that s has a REPRESENTATIVE of the form
     s_hat(theta - OM t) — an a.e. statement. The proof as written performs
     a pointwise change of variables on an a.e. identity; the L-STD citation
     is a gesture, not an argument. (Same defect class the round-1 l0-F6
     found in L-STD itself — but at a NEW site created by the revision; the
     round-1 sweep predates this proof.)

WHY NEW: (i') and its proof exist only in revision 1.

SEVERITY: medium (a revision-1 THEOREM label on a statement with an
undefined predicate + an unproven measure-theoretic step; both repairable).

REPAIR: as in (a); for (b) either import L-STD verbatim on the data space
(the interface is 2-D + time — the identical mollification argument runs) or
state (i') for continuous-representative data and add the a.e. class as a
corollary.

==============================================================================
## r2-F6 — [T-T0P-E] FALSIFIER (revision-1 restatement) CANNOT REJECT: the
## printed exhibit does not refute L-STD

CLAIM ATTACKED: §2.3 FALSIFIER: "the theorem itself is killed by an S1 field
q with g_tau q in C(s) for all tau and q not of the form (STD) — which would
refute L-STD".

DEFECT. False implication. L-STD's hypothesis is q = g_tau q a.e. for every
tau. The printed exhibit hypothesizes only g_tau q IN C(s) (class
membership), NOT g_tau q = q. If the S1-anchored uniqueness property FAILS
for C(s), an S1 field q with g_tau q in C(s), g_tau q != q, and q not of
the form (STD) is perfectly consistent with L-STD, with L-EQV3, and with
[T-T0P-E] itself (whose conclusion is conditional on the uniqueness
property). So the printed falsifier, executed successfully, kills NOTHING:
not the theorem (hypothesis unmet), not L-STD (hypothesis unmet), not
L-EQV3 (unchallenged). A falsifier that cannot reject the labeled claim
violates R5. The correct two-target statement is:
 (t1) kill L-STD: a field q with q = g_tau q a.e. for ALL tau and q not of
      the form (STD) — the genuine measure-theoretic target;
 (t2) kill L-EQV3: an S1 q in C(s) with g_tau q NOT in C(s) — as the doc
      already states.
The theorem, being a conditional assembly, is killable only through its
lemmas or by refuting the assembly logic — say so.

WHY NEW: round-1 l0-F12(c) asked for target LABELING and was marked FIXED;
the revision's new wording introduced a logically inadequate implication
that did not exist before (the round-0 falsifier had a different defect).

SEVERITY: medium (R5-class: rejection power).

REPAIR: replace the first clause by (t1) above.

==============================================================================
## r2-F7 — H5' REPAIR IS INCOMPLETE: the box-compatibility clause covers the
## transverse coordinate only; the AXIAL Mach range of K is not tied to the
## certified box

CLAIM ATTACKED: H5' ("... q_perp <= V_max c ... with it, the rotated state
lies INSIDE the certified planar (M, V) box of [X-IVXC]/[T-XRED]") and the
same sentence inside L-XC3D(i) and the G1 ledger row.

DEFECT. The l1-F4 repair added a bound on the TRANSVERSE Mach coordinate
V_eff = q_perp/c and declared box membership achieved. But the certified
[X-IVXC] box is a compact box in BOTH Mach-pair coordinates (M, V): it has a
finite AXIAL Mach range (the P4a range of the transfer doc). H5' as restated
imposes u - c >= delta and compactness of K but NO clause tying sup_K (u/c)
(nor inf, beyond 1 + delta/c) to the certified M-range. A K whose axial Mach
reaches above the box ceiling reproduces, in the M-coordinate, exactly the
domain hole the revision fixed in the V-coordinate: the rotated state's
Mach pair falls OUTSIDE the certificate and the L-XC3D "CONSEQUENTLY"
inheritance fails at those states. The sentence "the rotated state lies
INSIDE the certified planar (M, V) box" is therefore FALSE as a consequence
of H5' as written; it is true only under an additional clause.

WHY NEW: l1-F4 raised (and the revision fixed) only the q_perp/Euclidean
coordinate; the axial coordinate hole is untouched and newly load-bearing
because the revision now claims box membership follows.

SEVERITY: medium (same class as l1-F4; the repair claims completeness it
does not have).

REPAIR: add to H5' the two-sided clause "(M, V_eff)(K) subset B_cert", with
B_cert the [X-IVXC] Mach-pair box of record, checked a posteriori per
instance alongside the existing margin check (the doc's own instance-check
sentence extends verbatim).

==============================================================================
## r2-F8 — [L-XREC] "IF AND ONLY IF" IS FALSE AS STATED (THEOREM label
## breaks on the reverse implication); the r-b check design inherits the bug

CLAIM ATTACKED: L-XREC: "F_x is injective on the K-branch IF AND ONLY IF,
for every (m1, m2, H_pl) arising from K, the 1-D triple has AT MOST ONE
solution with u > c".

DEFECT. The forward implication (root one-sidedness => injectivity) is
proven. The REVERSE is false as stated: suppose some triple arising from K
has two supersonic solutions, one of which reconstructs to a state OUTSIDE
K (violating rho >= rho_min, the delta-margin, or the q_perp clause). Then
F_x remains injective ON THE K-BRANCH while the right-hand side of the
equivalence fails — the biconditional is refuted. The correct equivalence
is: F_x injective on the K-branch <=> no triple arising from K has two
supersonic solutions BOTH of whose reconstructed states lie in K. Since the
lemma carries a THEOREM label and the equivalence is its entire content,
this is an over-label by falsity of one direction. Consequence downstream:
the G7 discharge route r-b ("certified 1-D root-count over K") as designed
would reject [C-XINJ] on a spurious out-of-K second root — the interval
check must test K-membership of both reconstructed states, or it is a
rejector for the WRONG statement (an R5 defect in the planned carrier).

WHY NEW: L-XREC exists only in revision 1 (minted as the l0-F3 repair).

SEVERITY: medium-low mathematically (one-directional use in §4 only needs
the forward implication), medium procedurally (the planned [X-T0P] check
inherits a wrong acceptance criterion).

REPAIR: restate the equivalence with the both-roots-in-K clause; annotate
r-b accordingly.

==============================================================================
## r2-F9 — H8' STRONG-SIDE "PER-INSTANCE DISCHARGE BY THE H3 MONITOR" IS A
## CATEGORY ERROR: a data-purity monitor cannot certify interior
## t-periodicity of a solution

CLAIM ATTACKED: H8': "For the S1 element the hypothesis is discharged
per-instance by the same monitor line that verifies H3."

DEFECT. The T0-flatness/H-DATA monitor line (as characterized by this very
document in §5's falsifier discussion and in §9's falsifier table) tests the
DATA hypothesis: purity of the interface trace on Gamma_d. H8' for the S1
element is a statement about the SOLUTION on the interior slab
Omega_march x R: q(., t + T) = q(., t). No monitor of the interface trace
can certify an interior property of an arbitrary S1 element of C(s) — data
periodicity implies solution periodicity only via a uniqueness theorem,
i.e. via [T-T0P-U] itself, whose hypothesis H8' is; taking the monitor as
discharge is therefore either circular (assumes the theorem to discharge its
own hypothesis) or a category error (certifies the wrong object). What IS
true: for the engine-CONSTRUCTED wave-frame-steady object, t-periodicity
holds by construction — but that is a statement about one instance-built
representative (Cor 5.2's U*), not about "the S1 element" of the class, and
it should be said in exactly those words.

WHY NEW: round-1 (l0-F5/l1-F2) forced H8' to bind the strong side; the
DISCHARGE-ROUTE sentence is revision-1 text and its validity was never
audited.

SEVERITY: medium (an instance-certification claim that cannot be executed
as described; touches the R5 discipline on what the monitor can reject).

REPAIR: replace by: "for the constructed U* (Cor 5.2), H8' holds by
construction; for a general S1 element, H8' is a hypothesis (lifted by G5)"
— and mirror this in the §8 M0-delta instruction.

==============================================================================
## r2-F10 — STRATUM-(A) "IMMUNE to the convex-integration obstruction" IS AN
## OVER-ASSERTION: classical weak-strong is initial-value-anchored and is
## not available on the t-periodic slab; the immunity is exactly as
## conditional as G2/G7/G8

CLAIM ATTACKED: §4(B): "Stratum (A) itself is IMMUNE to the
convex-integration obstruction: weak-strong uniqueness against a C^1 strong
side is exactly the regime where relative entropy beats convex integration
(the wild solutions attach to non-smooth data)."

DEFECT. The classical statement gestured at (Dafermos/DiPerna weak-strong
uniqueness in the admissible class against a C^1 solution) is a theorem
about the INITIAL-value problem: the relative entropy is anchored at t = 0
and propagated by Gronwall in t. The present setting has NO initial slice —
t lives on the torus T_t and the anchoring is at the inflow x-slice, i.e.
the immunity of stratum (A), IN THIS DOCUMENT, is delivered only by the §4
x-march argument, which is conditional on G2 (trace package, including the
r2-F2/r2-F3 clauses), G7, G8, H8', H9. Unconditional "IMMUNE" is thus not
available from any theorem on file: t-periodic problems are a known blind
spot of the weak-strong mechanism (no initial anchor; uniqueness of
t-periodic solutions does NOT follow from IVP weak-strong uniqueness — an
IVP-unique flow can still carry multiple t-periodic orbits through
different Cauchy data, which is precisely why the doc must anchor at x = 0).
The sentence, sitting inside the (B) discussion but making a claim about
(A), reads as an unconditional mathematical fact and would be quotable as
such — the same quotability defect class as l1-F5 (which the revision fixed
for L-SPACE by moving the strong reading to an attributed remark; the same
surgery is owed here).

WHY NEW: the immunity sentence is revision-1 text (introduced by the
l0-F8/l1-F9 disposition); the round-1 objections asked for the
convex-integration ENGAGEMENT, not for an audit of the new sentence.

SEVERITY: medium-low (no proof step consumes it; but it is a label-adjacent
over-claim inside a document whose currency is label honesty).

REPAIR: "immune" -> "covered by the CONDITIONAL x-march weak-strong argument
of this section (G2/G7/G8, H8'/H9): relative entropy against a C^1 strong
side excludes wild competitors WITHIN the class and modulo the named stack;
no unconditional immunity is claimed on the t-periodic slab".

==============================================================================
## r2-F11 — [L-STD] POINTWISE REFINEMENT: the "closed null set N" hypothesis
## is NOT satisfied by the application the lemma itself names

CLAIM ATTACKED: L-STD refinement clause: "If moreover q is continuous off a
CLOSED null set N with g_tau N = N ... (STD) holds POINTWISE off N", and the
application paragraph "take N to be the ESSENTIAL discontinuity set ... For
an S1 representative (H6'), N is contained in the front set AFTER EXCISION
of zero-jump sheets".

DEFECT. Two mismatches between the stated hypothesis and the named
application:
 (a) The essential discontinuity set of a function is an F_sigma (the
     continuity set of any representative is a G_delta); it need not be
     closed. For the S1 application the doc itself proves N is the
     nonzero-jump SUBSET of the front hypersurfaces — a RELATIVELY OPEN
     subset of the fronts (jumps vanish on a closed subset of each sheet;
     the doc's own excision argument says zero-jump points are continuity
     points). A relatively open subset of a hypersurface is generically NOT
     closed in the ambient space: its closure adds the zero-jump boundary
     points. So the lemma's "closed null set" hypothesis FAILS for exactly
     the N the doc instructs us to take, and the pointwise conclusion as
     chained is unproven.
 (b) The final argument "two continuous functions equal a.e. on an open set
     are equal everywhere on it" needs the complement of N to be OPEN —
     same failure. The repair is easy and should be written: continuity of
     both fields AT a point x plus a.e. equality on a NEIGHBORHOOD of x
     gives equality at x (approximate x by points of the full-measure
     equality set); this needs only that q and g_tau q are both continuous
     at x, i.e. x off N and (by g_tau N = N) g_{-tau} x off N — no openness
     and no closedness of N anywhere. Additionally, the mollification limit
     at the end of the main proof quietly fixes one eps-sequence: the
     exceptional spatial set E depends on eps, so the final identification
     Q = Q_bar needs eps_n -> 0 countable and the union of the E^(eps_n) —
     one sentence, currently absent, in a lemma whose §10 disposition
     claims "proof COMPLETED".

WHY NEW: round-1 l0-F6/l1-F7 attacked the tau-null-set closure and the
unproven g_tau N = N — both fixed. The closedness/openness mismatch and the
eps-union are residual defects of the REVISED text, not repetitions.

SEVERITY: low-medium (fully repairable in-place; but the refinement is
consumed by [T-T0P](i) "pointwise off N", so the defect propagates into the
main theorem's statement as printed).

REPAIR: replace "closed null set" by "null set", run the continuity-at-a-
point argument, add the eps_n sentence.

==============================================================================
## SURVIVED (checked, no new objection): items re-verified sound this round

- L-EQV1/L-EQV2 (frame-indifference computation; dyadic momentum identity).
- L-INV (pure shift computation).
- L-EQV3 items (i)-(viii) as pointwise/measure verifications (given r2-F2's
  caveat that (v) preserves the trace PACKAGE — composition with rigid
  motions does preserve DM structure and normal traces; no new defect).
- L-SPACE as re-scoped (speeds computation correct; (iii) is used only
  motivationally after the l1-F5 surgery; the glancing-ray issue is
  immaterial to any consumed conclusion).
- L-COMPAT Steps 1-2 including the Kato-Majda gradient-arbitrariness device
  and the identity D_M eta = D_W E (checked against the displayed algebra).
- L-XSON3 parity/rotation factorization det J_5 = (rho u) det J_4.
- L-XWALL3 AS A STATE-LEVEL LEMMA: the 5-component slip solve (dH = 0,
  d(rho u) = 0 => theta dS = -p'(u.n)/(rho u) = 0) is correct at abstract
  EOS; the objection r2-F2 is to its APPLICATION, not its content.
- L-XC3D (KEY) computation re-derived line by line this round: mass/
  momentum/energy differentials, the exact cancellation, S''(0) =
  -1/(theta m1^2), h_ww = g'/(theta rho u) — all correct; parity argument
  for the block decomposition correct.
- The §4 Gronwall skeleton GIVEN the G7/G8 and the r2-F2/r2-F3 trace
  clauses; the a.e.-x1 integral form is fine.
- P-HB2 core (linearity of continuous one-parameter subgroups + Fourier
  line-by-line constraint; the "differentiating" wording is harmless since
  a continuous 2piZ-valued function vanishing at 0 vanishes identically).
- The two-tier falsifier architecture and G10 gating (given l1-F8, no new
  defect found in the tiering itself).
- Gamma table: checked per statement; the single gamma-restricted
  ingredient claim ([X-IVXC] at gamma = 1.4 via G1) is consistent with the
  proofs as long as r2-F7's box clause is added (the gamma CLAIM itself is
  correct as stated).
- §7 two-stage structure and the honest-boundaries block.
- §10 disposition table accurately reflects what the revision did (modulo
  the new findings above, which are about the revision's own text).

==============================================================================
## VERDICT

REPAIRABLE. No finding above breaks the architecture: the equivariance half
survives intact (modulo r2-F6's falsifier rewording and r2-F11's refinement
repair), and the uniqueness half's defects are label algebra (r2-F1),
missing trace-contract clauses that BV-restriction or explicit hypotheses
absorb (r2-F2, r2-F3), quantifier hygiene on revision-1 statements (r2-F4,
r2-F5, r2-F8), an incomplete box clause (r2-F7), and two over-assertions
(r2-F9, r2-F10). But the document is NOT sound as labeled: stratum (A)
THEOREM* is inconsistent with the doc's own downgrade criterion while G7/G8
are unregistered (r2-F1); H7' as written does not define a class for which
the §4 proof runs (r2-F2/r2-F3); [L-XREC]'s biconditional and [P-HB3](i'')'s
THEOREM label are false/over-broad as printed. A revision-2 pass executing
the named repairs (all local, no new mathematics except the (w)/(d) trace
clauses, which are declarations) restores label integrity.

Lens: functional-analytic rigor (l0). Round: 2. New objections: 11.


==============================================================================
==============================================================================
# PART 2 — NEW-LOOP ROUND 2, LENS 0 (2026-08-17, target = REVISION 2)
# (functional-analytic rigor: spaces, operators, traces, quantifiers, every
#  claimed rigor label; absence of known literature routes is a finding)

Target: validation/sfoundations_raws_2026-08-13/phaseD/phaseD_stop_proof.md
at REVISION 2 (post the §11 disposition of the r3 refuter pair). DEDUP SET
for this pass (nothing below repeats any of them): the brief's do-not-repeat
list = r3_l0 (r3-F1..F5) + r3_l1 (l1r3-F1..F5), PLUS everything already on
disk: r1_l0 F1-F12, r1_l1 F1-F10, PART 1 above (r2-F1..F11, still unconsumed
per the target's §11 — repeated here by REFERENCE only, never re-raised),
r2_l1 F1-F9. Every finding below attacks text INTRODUCED by revision 2, or a
defect no prior list raised. Convention: notation as in the target; "the
doc" = the target file at revision 2.

==============================================================================
## r2b-F1 — G8 DISCHARGE ROUTE r2 ("Dafermos device in W-variables") IS
## MISPRICED AS STATED: W-convexity of E fixes the commutator/upper estimates
## and the relative entropy E(V|U) — NOT the load-bearing LOWER sandwich,
## which is on the relative x-FLUX; the hull obstruction reappears verbatim
## in W-space, and the "removes the G7 consumption" claim rides the same
## conflation. Consequence: the document currently names NO viable
## abstract-EOS G8 route, and the revision-2 gamma accounting rests on one.

CLAIM ATTACKED (all revision-2 text): §9 G8 row, route "(r2) Dafermos device
in W-variables — the CLASSICAL route the field would use ...: E = -rho g(S)
is GLOBALLY convex in the conservative variables W ... which kills the hull
problem at its root — all comparison segments in W-space stay in the convex
physical region; the M-reading survives at flux level only, and this route
also removes the G7 consumption from the endgame. The ONLY named G8 route
that keeps the chain abstract-EOS"; plus the audit-line and §9 gamma-table
sentences that price the abstract-EOS surface of [T-T0P-U]/[T-T0P] on r2's
viability ("route r2 is the ONLY named G8 route keeping the chain
abstract-EOS").

DEFECT (functional analysis of the §4 budget). The Gronwall quantity at the
slice Sigma_{x1} is Int eta(V|U), where eta = -rho u g(S) is the x-FLUX
component Q_x of the classical entropy pair (E, Q). In W-variables the same
object reads (identically, by the doc's own L-COMPAT identity
D_M eta = D_W E):

    Q_x(V|U) := Q_x(V) - Q_x(U) - D_W E(U) . (F_x(V) - F_x(U)).

Set G_U(W) := Q_x(W) - D_W E(U) . F_x(W). Classical compatibility
(D_W Q_x = D_W E . A_x) gives D_W G_U(W_U) = 0, so along the W-segment
W_s = (1-s) W_U + s W_V:

    Q_x(V|U) = Int_0^1 (1-s) D^2 G_U(W_s)[DeltaW, DeltaW] ds,
    D^2 G_U(W_s) = D^2 Q_x(W_s) - Sum_j (D_W E(U))_j D^2 (F_x)_j (W_s).

Convexity of E controls D^2 E, which appears NOWHERE in this expression.
What r2 genuinely delivers: (i) E(V|U) >= c |DeltaW|^2 with segments inside
the convex physical region ({rho >= rho_min} IS convex in W since rho is a
linear coordinate — this half of the pricing is correct); (ii) smoothness of
all fluxes on that convex hull, hence the UPPER commutator bounds along
W-segments. What it does NOT deliver: the LOWER sandwich
c |DeltaW|^2 <= Q_x(V|U) — the inequality the endgame (Int = 0 => DeltaW = 0
a.e.) and the Gronwall absorption actually consume at every slice.
Definiteness of the two-point field (U, W_s) -> D^2 G_U(W_s): at s = 0 it is
CONGRUENT to the M-Hessian of eta at U (D^2_M eta = A_x^{-T} D^2 G_U
A_x^{-1}, the change-of-variables identity through M = F_x(W)); hence by the
doc's own [S-XCONV] R1 it is INDEFINITE at subsonic states. And the
supersonic set {u > c} is NOT convex in W-coordinates: u = m1/rho is a
mediant under convex combination and c moves with (rho, S) — two supersonic
states can average to a subsonic one. So the comparison W-segment can cross
states where the integrand loses definiteness: the hull problem is not
"killed at its root"; it TRANSFERS to the x-flux Hessian along W-segments,
in exactly the two-point/segment form G8 names in M-space. The G7-removal
claim is conditional on the same missing bound: with a valid
Q_x(V|U)-sandwich the endgame would indeed conclude W_V = W_U without any
M-inversion (that inference is right), but the sandwich IS the open piece —
r2 removes G7 only after solving a G8-equivalent problem.

CONSEQUENCE FOR THE ACCOUNTING (the load-bearing part): revision 2's gamma
table and audit line rest on "route r2 is the ONLY named G8 route keeping
the chain abstract-EOS". With r2 unsound as priced, the doc names NO viable
abstract-EOS G8 route: r1 is feasibility-gated by its own row (possibly
infeasible IN PRINCIPLE), r3 is a gamma = 1.4 instance certificate, and r2
as printed contains an unjustified coercivity transfer from E(V|U) to
Q_x(V|U). The honest audit line is: the abstract-EOS status of the
[T-T0P-U](A)/[T-T0P] chain is OPEN AT THE ROUTE LEVEL — not
route-dependent-with-one-clean-route.

ABSENCE. The cited authorities (Harten; Godlewski-Raviart) prove t-EVOLUTION
facts: convexity of E in W for the initial-value relative-entropy device. No
published x-as-time / spacelike-direction weak-strong theorem runs on
W-convexity of E; the classical relative-entropy device taken in a spacelike
direction requires convexity of the FLUX entropy in the evolution direction
— exactly the in-house M-condition r2 claims to bypass. The §9 novelty query
added for r2 ("entropy convexity conservative variables Euler thermodynamic
stability") searches the IVP fact and cannot surface this mismatch; the
missing query is of the form "relative entropy spacelike direction flux
convexity weak-strong".

WHY NEW: route r2's content, the "kills the hull problem at its root"
sentence, the G7-removal claim, and the only-abstract-EOS-route status are
all revision-2 text (l0r3-F2(c) asked only for the ABSENCE of the W-route to
be repaired — it did not audit the route's validity); r3-F5/r2_l1-F6
concerned gamma COUNTING, not route soundness.

SEVERITY: HIGH (a discharge-route pricing of record is false as stated; the
gamma accounting and the audit line inherit it; F2 would be dispatched onto
a route that cannot work as described).

REPAIR: rewrite the r2 row: "r2 dissolves the hull problem for the
upper/commutator estimates and for E(V|U); the lower sandwich on the
relative x-flux Q_x(V|U) remains a two-point segment condition equivalent in
difficulty to (a') (subsonic indefiniteness transfers by congruence; the
supersonic set is non-convex in W)"; demote r2 from "the classical route the
field would use" to a partial reduction; restate the gamma table's
route-dependent sentence; add the corrected novelty query.

==============================================================================
## r2b-F2 — STRATUM (B): even granting ALL named conditionals, the printed
## inheritance cannot reach the printed target — the revision-2 class
## specification makes [C-MAJDA-3DT] a strong-vs-strong (H^s) uniqueness
## statement, while the (B) target quantifies over L^inf H7' competitors;
## the weak-vs-fronted-strong ingredient is load-bearing and UNNAMED, so the
## SCHEMA label's own contract ("proof route with named gaps") is violated.

CLAIM ATTACKED: §4 (B) "the conclusion of (A) is the TARGET, modulo the NEW
conditional [C-MAJDA-3DT] (G3)" together with the G3 row's revision-2
SOLUTION-CLASS SPECIFICATION ("the conditional is stated in the
front-solution class of the cited technology — piecewise weighted-
anisotropic Sobolev H^s ... (Majda; Metivier; Coulombel-Secchi)"); §5
[T-T0P](ii) on stratum (B); the §8 registry instruction for G3.

DEFECT. The (A) conclusion — declared to be the (B) target — is: V = U a.e.
for EVERY H7' competitor V, an L^inf/divergence-measure class. Revision 2
pinned G3's content to uniqueness/stability WITHIN the piecewise-H^s front
class. These quantifiers do not compose:
 (a) uniqueness within H^s says nothing about an L^inf competitor that is
     not an H^s front solution — the overwhelming majority of the H7' class;
 (b) the declared bridge g3-b certifies the STRONG side into H^s on
     instances; no bridge can move the whole H7' competitor class into H^s —
     that would be a regularity theorem for arbitrary admissible weak
     solutions, which the doc's own convex-integration discussion shows is
     FALSE in general (wild solutions are not H^s fronts).
Hence the route as printed reaches, at best, "the S1 element is unique among
H^s front solutions" — a strong-vs-strong statement. To reach the printed
target one needs IN ADDITION weak-strong uniqueness against L^inf
competitors when the strong side carries a shock: the known technology is
the shifted-front / a-contraction relative-entropy method (the in-house
[S-ACFR] transplant), which the doc names ONLY as an "alternative discharge
route" for G3 — i.e. as a substitute for G3, not as the required EXTRA
ingredient alongside it. A SCHEMA is "a proof route with named gaps": here a
load-bearing gap (the weak-vs-fronted-strong comparison) has no name, no
row, no owner, no falsifier, and the §8 registry instruction would mint G3
as if it closed the stratum.

WHY NEW: created by the revision-2 class specification (the l1r3-F3 repair):
before it, G3's class ambiguity masked the quantifier mismatch. r3_l1-F3
attacked the under-specification itself; r2_l1-F2 the front GEOMETRY of the
route; neither raised the target-vs-class quantifier mismatch or the missing
weak-strong-with-shock conditional.

SEVERITY: MEDIUM-HIGH (label-adjacent: (B) stays SCHEMA, but the gap list —
the thing the SCHEMA label certifies — is incomplete; the M0 delta would
export a wrong inheritance list for the front stratum).

REPAIR: split the (B) inheritance into (G3 = KL stability + H^s-class
uniqueness) PLUS a NEW named conditional (e.g. [C-WSF]: weak-strong
uniqueness across an admissible fitted front in the x-march class; discharge
route = [S-ACFR] transplant; falsifier = the a-contraction weight/shift
inequality failing numerically on a certified front instance), promoting
[S-ACFR] from "alternative" to "primary for the weak-vs-strong half"; or
restate the (B) target honestly as strong-vs-strong.

==============================================================================
## r2b-F3 — the revision-2 "EXECUTABLE rejectors" for [P-HB2] and
## [P-HB3](i') still have (near-)zero rejection power: the lattice sweep
## tests the trivial arithmetic of the DERIVED line constraints, never the
## invariance=>constraints step it claims to guard; the sampled random
## profiles never enter the check; and a lattice of group ELEMENTS cannot
## witness a one-parameter SUBGROUP either way.

CLAIM ATTACKED: §6 [P-HB2] FALSIFIER ("randomized two-line sweep — sample
(k1, k2) and OM_{k1} != OM_{k2} with random profiles, sweep (a, b) over a
lattice with a continuity bound on the two line constraints
k_i (a - OM_{k_i} b) = 0; the proposition is REFUTED if any nontrivial
(a, b) survives both constraints. This CAN fire — if the Fourier-uniqueness
algebra above is wrong, a surviving pair appears"); the [P-HB3](i')
falsifier ("swept over the (a, b) lattice as in the [P-HB2] rejector"); the
§9 falsifier-table rows and the §11 l0r3-F4 disposition row ("both CAN
fire").

DEFECT (three layers).
 (a) WRONG OBJECT. The check evaluates the two LINEAR constraints
     k_i (a - OM_i b) = 0 over an (a, b) lattice. For OM_1 != OM_2 and
     k_i != 0 that pair has only (0, 0) as solution — by elementary linear
     algebra, independently of anything the proposition asserts about DATA.
     The load-bearing content of [P-HB2] is the IMPLICATION "invariance of s
     under the subgroup => those constraints" (Fourier uniqueness in
     (theta, t) + the linearity clause). If THAT step were wrong, invariance
     could hold WITHOUT the constraints holding — and the sweep, which
     checks constraints and never evaluates invariance, would find nothing:
     the advertised firing mode ("if the Fourier-uniqueness algebra above is
     wrong, a surviving pair appears") is logically FALSE. The sampled
     "random profiles" are dead weight — no quantity computed from s enters
     the check at any point.
 (b) SPURIOUS-FIRE MODE. With a numerical "continuity bound" (tolerance),
     near-degenerate draws (|OM_1 - OM_2| small relative to the tolerance)
     produce surviving nontrivial (a, b) that refute NOTHING: the rejector
     can fire only as a tolerance artifact.
 (c) ELEMENT-VS-SUBGROUP. [P-HB2]'s claim is about one-parameter SUBGROUPS.
     Individual nontrivial group elements with exact invariance LAWFULLY
     exist — the discrete residual subgroup the proposition itself names
     ({(phi, tau) : k_i(phi - OM_i tau) in 2pi Z}). Any faithful invariance
     check at lattice POINTS therefore fires on lawful elements; only a
     check along LINES {(a sig, b sig) : sig in R} addresses the claim. Read
     as "= 0 constraints" the design never fires on true errors (layer (a));
     read as "invariance at lattice points" it fires on the lawful discrete
     subgroup — there is NO reading under which it rejects the labeled
     claim. The defect transfers verbatim to the [P-HB3](i') rejector, which
     inherits the design by reference.

WHY NEW: attacks text that exists only in revision 2 (the sweeps replaced
the round-1 "impossible by the proof" lines); r3-F4 raised the zero-power
defect of the OLD lines and asked for executable rejectors — it did not
audit the delivered design.

SEVERITY: MEDIUM (R5 class: the l0r3-F4 disposition row is marked FIXED of
record, but the repair re-introduced the same defect in executable clothing;
two §9 falsifier-table rows and one §11 row are wrong as printed).

REPAIR (one sentence each, faithful to the claims): [P-HB2]: sample s from
the stated two-line class; for each nontrivial lattice DIRECTION (a, b),
compute the invariance defect D(a, b) := max over a sig-grid (finite and
certified via a Lipschitz-in-sig bound) of
||s o g_{a sig, b sig} - s||_{L^2(Gamma_d x [0, T_obs])}; the proposition is
refuted iff some nontrivial direction has D ~ 0 uniformly on the grid.
[P-HB3](i'): the same defect functional on the synthetic transition data.
Both genuinely can fire (a wrong Fourier-uniqueness step would surface as a
flat defect along some direction), and neither fires on the lawful discrete
elements (a LINE through a discrete element has D > 0 away from isolated
parameter values).

==============================================================================
## r2b-F4 — the G8 falsifier and its feasibility gate are declared
## "executable now" but are well-defined only MODULO G7 plus a declared
## branch-continuation rule: every evaluation of eta, u - c, or the Hessian
## at an interior segment/hull point of M-space requires SELECTING a
## supersonic preimage — an undeclared instrument-dependency edge
## (G8-falsifier -> G7 r-b machinery), with the same table-enclosure
## requirement on the standing gamma(T) model.

CLAIM ATTACKED: §9 G8 row, FALSIFIER paragraph ("... numeric line-search
over the certified box, [X-T0P]-class, executable now") and FEASIBILITY GATE
paragraph ("interval lower bound of u - c over the segment hull of the
certified box in M-space (decidable, cheap ...)"); the §9 falsifier-table
sentence "now INCLUDING (rev 2) the G8 segment line-search falsifier, the
G8 feasibility gate ...".

DEFECT. Interior points of the segment [M_U, M_V], and points of conv(K_M),
are NOT of the form F_x(known state): to evaluate u - c or Hess(eta) there,
one must invert F_x — i.e. solve the L-XREC 1-D triple and SELECT a
supersonic root. (i) If G7 is false at such a point (two supersonic roots),
eta is multivalued and both the "loses definiteness" check and the u - c
interval bound are ill-posed as printed: the falsifier's verdict depends on
an undeclared selection rule. (ii) Even where G7 holds, executing the check
requires exactly the G7/r-b certified root-count instrument — and, on the
standing gamma(T) tabulated model, its certified table-interpolation
enclosures, a requirement revision 2 states for r-b but NOT for the G8
falsifier/gate that consume the same solve. So "executable now" over-prices:
the honest status is "executable once the r-b instrument exists; well-posed
modulo G7 or an explicit continuation rule (e.g. continuation of the
supersonic root from a segment endpoint, with continuation FAILURE itself
reported as a branch-departure verdict)". The gap-graph discipline the doc
itself instituted this window (the G5 -> G8 edge, l0r3-F3) requires this
edge (G8-falsifier -> G7-instrument) to be declared and exported with the §8
delta like the others.

WHY NEW: the G8 falsifier and feasibility gate exist only in revision 2
(minted in response to r3-F2); r3-F3's edge finding concerned G5 -> G8; no
prior list audited the new falsifier's own well-definedness.

SEVERITY: LOW-MEDIUM (accounting/instrument design; no label change, but
two "executable now" claims of record are conditional and a gap-graph edge
is missing from the ledger the §8 delta exports).

REPAIR: add the edge and the continuation rule to the G8 row; bundle the
falsifier/gate execution with the r-b instrument in the [X-T0P] battery
plan; state the table-enclosure requirement once for all three consumers
(r-b, G8 falsifier, G8 gate).

==============================================================================
## r2b-F5 — G4 (tilted-interface branch) is still ONE CLAUSE SHORT after
## revision 2: the remap to a spacelike foliation with SPATIALLY VARYING
## normal destroys conservation form — the remapped system and entropy
## quadruple acquire O(|grad n|) source terms, the relative-entropy identity
## gains FIRST-order terms in the state difference, and their absorption
## consumes the G8 segment constants: missing clause (g4-d) and missing
## gap-graph edge G4 -> G8 on the general branch.

CLAIM ATTACKED: H9 GENERAL CASE + §9 G4 row (three clauses g4-a/b/c, priced
as instance certificate + open condition + per-direction box re-check;
"L-XWALL3 is the one brick already direction-general").

DEFECT. All §3 bricks are stated and proven for the FIXED coordinate
direction e_x: (EU-x) is a conservation-form evolution precisely because e_x
is constant. Remapping to a foliation {chi(x, r) = const} with varying
downstream normal n(p) gives an evolution operator whose flux
F_n = n_x F_x + n_r F_r has variable coefficients: written in
foliation-adapted variables the system is conservation form PLUS
zeroth-order sources in grad n (turning of the marching direction /
curvature of the leaves) — terms that are NOT divergences. Consequences the
three printed clauses do not cover:
 (a) the quadruple compatibility (L-COMPAT) holds leafwise, but the
     space-time divergence of the remapped quadruple picks up source terms
     ~ |grad n| x (flux differences), FIRST order in M_V - M_U — not
     quadratic;
 (b) the §4 budget then closes only via Young's inequality against the
     quadratic lower sandwich — consuming the G8 constants c_K on the
     GENERAL branch and adding a foliation-curvature constant
     ||grad n||_inf to the Gronwall rate: an un-named certificate input
     (=> gap-graph edge G4 -> G8, exactly parallel to the declared
     G5 -> G8);
 (c) the wall lemma's application must be re-verified in the remapped
     frame: the wall stays static, but its normal acquires a component
     along the new marching direction unless the foliation is compatible
     with Gamma_w — a compatibility clause nowhere stated.
None of (a)-(c) is a "re-instantiation of an existing certificate": they
change the STRUCTURE of the budget on the general branch. The primary
(cross-section) case remains untouched, as declared.

WHY NEW: l1r3-F1 (consumed) established g4-a/b/c (normal Mach, foliation
existence, per-direction box); the conservation-form loss, the first-order
source terms, the Young/G8 consumption, and the wall-compatibility clause
appear in no prior list.

SEVERITY: LOW-MEDIUM (general branch only, primary case vacuous; but G4's
pricing of record is incomplete and the missing G4 -> G8 edge belongs to
the same gap graph the §8 delta exports).

REPAIR: add clause (g4-d) to H9/G4: "foliation-adapted formulation — source
terms bounded and absorbed: requires a ||grad n||_inf certificate + the G8
sandwich on the general branch (edge G4 -> G8) + wall-foliation
compatibility"; keep the primary-case vacuity statement.

==============================================================================
## r2b-F6 — write-up gap, held to the document's OWN "one line, but the line
## must be WRITTEN" standard: the §4 budget integrates (EI-x) — a
## D'(Omega_march x R_t) inequality against compactly supported nonnegative
## tests — against the constant test function on the t-TORUS; the
## periodization step is consumed unstated.

CLAIM ATTACKED: §4 proof of (A), first display ("Integrate (EI-x) for V
against 1 over {0 < x < x1} x Sigma", Sigma = Omega_x x T_t), with H7'
declaring (EI-x) "in D'" (i.e. on the R-line in t).

DEFECT. (EI-x) is minted as a distributional inequality on
Omega_march x R_t; the constant-in-t test on the torus is not an admissible
D'(R)-test. For an H8'-periodic field the torus inequality FOLLOWS — sum a
partition of unity subordinate to {(kT - T, kT + T)}_k: each term is a
legitimate D'(R) pairing and the sum telescopes by T-periodicity of V and of
the quadruple composed with V — but this is a (short) LEMMA about the class,
not a notational identity, and it is exactly the class of one-line gap the
revision itself refuses to leave implicit in [L-INC](a). Without it, the
first display of the (A) proof is unjustified as printed. (Alternative
repair: state (EI-x) in H7' directly on Omega_march x T_t and derive the
R-line version; H6' rev-2 already counts fronts on the torus, so the
per-front verification of [L-INC](a) reads naturally there.)

WHY NEW: no prior list touches the D'(R)-vs-torus test-space mismatch
(Part 1's r2-F3 concerned the Sigma_0 trace CONTRACT; l1-F10(d)/G2(b4)
concerned Lipschitz tests non-compact in (y, z)).

SEVERITY: LOW (pure write-up; no label change — but it sits at the head of
the (A) proof).

REPAIR: one displayed periodization lemma, or restate (EI-x)/H7' on the
torus.

==============================================================================
## RE-VERIFIED SOUND THIS PASS (no new objection)

- [L-INC] statement and per-clause proof STRUCTURE (its trace clauses
  inherit Part 1's unconsumed r2-F2/r2-F3 objections by reference — no NEW
  defect found in the lemma itself; the (B)-half's per-front sign
  -|N_sp| m [g(S)] <= 0 re-checked against the entropy condition: correct).
- H6' torus-slab front count and its rationale (interacts correctly with
  L-STD: a T-periodic field has a T-periodic essential discontinuity set;
  countably many sheets on the R-line remain Lebesgue-null).
- H9 primary-case restatement and both revision-2 inline-arithmetic
  exhibits, re-computed: 0.8 sqrt(2) = 1.131...; 1.2 cos 20deg - 0.8 sin
  20deg = 1.1276 - 0.2736 = 0.854 — both correct as declared.
- The G5 -> G8 dependency edge as declared (content matches the §4 REMARK).
- The §11 disposition table: each row accurately describes the repair it
  claims, and the honesty note on the unconsumed r2 files (Part 1 above +
  r2_l1) is accurate; gating the §8 M0 delta on that owed pass is correct
  and is REAFFIRMED by this pass (r2b-F1/r2b-F2 add to what the delta must
  not enshrine).
- L-XREC's forward implication and the §4 endgame's one-directional use of
  it (Part 1's r2-F8 biconditional objection stands unconsumed; nothing new).

==============================================================================
## VERDICT (Part 2)

REPAIRABLE. No finding breaks the architecture: the equivariance half is
untouched this pass, and stratum (A)'s proof skeleton survives modulo the
already-declared stack plus r2b-F6's one-line periodization lemma. But the
document is NOT sound as labeled at revision 2 on three axes of record:
(1) the G8/r2 pricing sentence and the derived "only abstract-EOS route" /
gamma-table accounting are FALSE as stated (r2b-F1) — the abstract-EOS
status of the chain is open at the route level; (2) stratum (B)'s SCHEMA
gap-list is incomplete — a load-bearing weak-vs-fronted-strong conditional
is unnamed (r2b-F2); (3) the §6 rejectors marketed as the l0r3-F4 FIX have
no reading under which they reject the labeled claims (r2b-F3), an R5
defect in a disposition row marked FIXED. r2b-F4/F5 are ledger/edge
completeness; r2b-F6 is write-up. All repairs are bounded and executable
in-session EXCEPT the substantive halves of r2b-F1/r2b-F2, which are
honest-repricing moves (rewrite the r2 row; mint the missing (B)
conditional), not new mathematics. The §8 M0 delta must additionally not
land before these two repricings and the owed Part-1/r2_l1 consumption
pass.

Lens: functional-analytic rigor (l0). New-loop round: 2. New objections: 6.
