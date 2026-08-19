# ESCALATION REFUTATION — DOC-3 r3.2 repair text, until-dry ROUND 2, lens l0

Lens: hyperbolic-systems / functional-analytic rigor. Date: 2026-08-19.
Target: `validation/sfoundations_raws_2026-08-13/phaseD_L4_implies_R1.md`,
ATTACK SCOPE STRICTLY = the NEWEST revision-log entry's edited passages —
the r3.2 (until-dry ROUND 2) repairs to the E-4 leg-14 text (Proposition
1'': (cl-C), (cl-F), the eps_1' threading, the STEP-2 checklist completion,
the (D-coll) Lipschitz clause, the (H-UP-fam) quantifier restriction, the
re-attributed "why this does not prove too much" paragraph, the corrected
"Which (H-UP) form" block, the pinned mid-face falsifier trigger + window
arithmetic, Status (a) insertions, register-row/log mirrors) and to the
leg-17 amendment A-2 chain (Remark 1.5.5, F-6 gap wording + log-row
annotation).

**FILENAME/ROUND DEVIATION, DECLARED.** The launching brief named "ROUND 1"
and output file `esc_doc3_r1_l0.md`. On disk, round 1 is already consumed:
`esc_doc3_r1_l0.md` (ESC-L0-1..7) and `esc_doc3_r1_l1.md` (F-1..F-6) exist
(2026-08-18) and are cited IN FULL by the target's r3.2 revision-log entry —
the very repair text this brief mandates attacking ("the newest revision-log
entries name the edited passages"). Overwriting the cited of-record round-1
carrier would falsify the audit chain (SR-6/SR-10 class violation). This
refutation is therefore the ROUND-2 lens-l0 output, written to
`esc_doc3_r2_l0.md`; nothing else in the brief is deviated from.

Specs consumed: `r2pass/VERDICT_r2pass.md` §2.1 (L0-7/L1-7 SUSTAINED-BREAKS,
L1-8 SUSTAINED-AMENDMENT), §3 (A-2), §4(c) (E-4), §5 (falsifiers incl. the
proves-too-much test). Full objection texts consumed:
`refute_r2batch_l0.md` L0-7, `refute_r2batch_l1.md` L1-7/L1-8 (the original
sustained set), and `esc_doc3_r1_l0.md` / `esc_doc3_r1_l1.md` in full (the
round-1 set whose r3.2 dispositions this round verifies).

DEDUP DECLARATION: no dispositioned objection is re-raised at its own
content. L0-7/L1-7/L1-8 and ESC-L0-1..7 / F-1..F-6 are engaged ONLY through
discharge verification (§1), EXCEPT ESC-L0-3, whose r3.2 disposition is
attacked AS FAILED under the brief's rule ("unless the disposition itself
fails — cite the ID and say why"): see ESC2-1/ESC2-2. Every other objection
below targets r3.2-NEW text with zero prior adversarial coverage.

==============================================================================
## §1 DISCHARGE VERIFICATION (r3.2 repairs vs the objections they answer,
## chained back to the sustained originals)

**L0-7(a) / L1-7(i) (quantifier order) — remains DISCHARGED at r3.2,
re-verified at pen grade.** eps_1 := d_0/(2 lambda_max) is a (D-coll)
constant; the r3.2 cap eps_1' := min(eps_1, T_f − t*) > 0 (t* < T_f) keeps
the window in-domain WITHOUT re-introducing any subdomain dependence:
lambda_max(t − t*) ≤ lambda_max·eps_1' ≤ lambda_max·eps_1 = d_0/2 < d_0, so
R with lambda_max(t − t*) < R < d_0 exists at every window time. CHECK.

**L0-7(b) / L1-7(ii) (trace ON the source face) — remains DISCHARGED.** The
only concluded trace is on Gamma_mid, at fixed distance ≥ d_0 from both
data-carrying faces; delivered by Lemma 1.4 frusta based AT Gamma_mid with
R < d_0. Unchanged by r3.2; re-checked with the eps_1' window. CHECK.

**ESC-L0-1 (solution class / t*-slice) — DISCHARGED by (cl-C).**
Re-derivation: U ∈ C([0,T_f]; L^2_loc(Omega_up)) gives (i) slices exist;
(ii) if t_n ↑ t* with U == 0 on [0, t_n] then U(·,t*) = lim U(·,t_n) = 0 in
L^2_loc — the sup-set is closed under left limits, so t* belongs to it and
U(·,t*) = 0 on Omega_up ("left-closed" as used); (iii) on C_h the clause
indeed follows from (H1.4) (C^1 on closure ⟹ C-in-time into L^2_loc);
(iv) STEP 3's class membership is now hypothesized with the delegation to
NG-9 declared in the Claim itself, exactly ESC-L0-1's named repair route.
Strongest attack tried: circularity of hypothesizing membership in a class
that is itself NG-9's unwritten burden — fails to break: the delegation is
explicit, the label of record is SCHEMA, and "THEOREM modulo (H-UP-fam)"
absorbs the class by (H-UP-fam)'s own formulation clause. CHECK.

**ESC-L0-2 = F-1 (same-forcing clause) — DISCHARGED at all three sites.**
(cl-F) in the Claim (with Theorem 1's parenthetical restored and F-1's
refuting interior-source pair recorded in the superseded-wording
annotation); "SAME interior forcing" + "(same forcing on Omega_int^s)" in
(H-UP-fam); "same-interior-problem pairs" in Status (a); register row 1'
mirrors ((cl-F)/(cl-C) named). Strongest attack tried: hunt for a fourth
consumable enumeration still lacking the clause — Section 5 clause (i) and
3.4(3)(a) cite Proposition 1''/(H-UP-fam) BY NAME without re-enumerating
hypotheses, so no consumer transcribes a false statement. CHECK.

**ESC-L0-5 = F-3 (window overrun) — DISCHARGED.** Both UNION cases
re-derived: t* + eps_1 ≤ T_f ⟹ eps_1' = eps_1, sup ≥ t* + eps_1 > t*,
contradiction; t* + eps_1 > T_f ⟹ eps_1' = T_f − t*, U == 0 on [0, T_f],
sup = T_f, contradicting t* < T_f. Boundary case t* + eps_1 = T_f falls in
case 1 with eps_1' = eps_1 — no gap. eps_1' is threaded through STEPs 1-3
and (MID-TRACE) as claimed. CHECK.

**ESC-L0-6 (STEP 2 checklist) — DISCHARGED.** "(H1.4) on C_{h/2} by
restriction" added; the checklist now carries all four numbered hypotheses
+ (D''), verified against Theorem 1''s statement. CHECK.

**ESC-L0-7 (Lipschitz Omega_int^s) — DISCHARGED.** (D-coll) now stipulates
Omega_int^{h/2} Lipschitz per (D'') with the failure mode named
(Gamma_mid tangent to Gamma_w); the family form carries "both C_s and
Omega_int^s ... Lipschitz domains per (D'')"; Status (a) cites the clause
at its (EI) run. CHECK.

**F-2 (family quantifier) — DISCHARGED.** Quantifier now "every s in (0, h)
FOR WHICH a (D-coll)-class split is given"; endpoint s = h dropped (d_0(h)
= 0 re-checked: Gamma^coll_h = Gamma_in^coll gives dist 0); the consumed
instance s = h/2 is (D-coll)'s content; the defective r3 quantifier is
retained as annotation per house discipline. CHECK.

**F-4 (attribution) — DISCHARGED as to the attribution itself.** The
corrected block states: construction = both-lens convergence, FORM consumed
= L0-7's family-of-depths restatement, (r-b) ingredients consumed / lens
geometry not, (r-a) not consumed — F-4's demanded wording. The log row
L1-7 is annotated in place. (A NEW defect in the same block's added
parenthetical is ESC2-3 below — it does not re-open F-4.) CHECK.

**ESC-L0-4 = F-5 (falsifier trigger) — DISCHARGED as to the trigger.** The
trigger is pinned to "the field on ALL of Omega_up — collar C_h INCLUDED";
register row 1''s falsifier cell mirrors it verbatim in condensed form.
(The r3.2-NEW window-arithmetic sentence added alongside carries ESC2-4
below — a defect of the new justification, not of the pinned trigger.)
CHECK.

**F-6 / A-2 chain (leg 17) — DISCHARGED, re-verified by direct spectrum
computation.** At u·n = 0 the spectrum is {−c, 0(×3), +c}; at u·n = −c it
is {−2c, −c(×3), 0}: adjacent distinct-eigenvalue gaps = c-bar, all pairwise
separations ≥ c-bar, extreme acoustic pair 2c-bar — the r3.2 wording is now
exactly true, the false "mutual ... equal to c-bar" is annotated of record
in Remark 1.5.5 and in the log's L1-8 row, and the load-bearing fact
(minimum distinct-gap ≥ c-bar ⟹ no collision, no projector degeneracy) is
correctly isolated. The multiplicity pattern (1,3,1) is CONSTANT through
both loci, so eigenprojector regularity holds with margin; Lemma 0.2's
eigenvectors are u·n-independent. Conclusion and scoping of the Remark
unchanged, per the A-2 spec. CHECK — A-2 fully landed.

**ESC-L0-3 (proves-too-much attribution) — NOT DISCHARGED.** The r3.2
disposition row says FIXED; the delivered body text mis-transcribes the
finding's mechanism and fails on the finding's own sharpest instance. See
ESC2-1 and ESC2-2.

**Residue:** the leg-14 derivation (two-face proof, STEPs 1-3 + UNION, with
(cl-C)/(cl-F)/eps_1') survives this lens's strongest attacks — see C-block.
The surviving defects are in the r3.2 honesty paragraph, one audit-trail
parenthetical, the new falsifier arithmetic, and one Status-(a) scoping —
none touches a proof step; the SCHEMA-per-J-r2p-1 label discipline is
intact and correct.

==============================================================================
## §2 OBJECTIONS (r3.2 text; verbatim quote + attack + class)

------------------------------------------------------------------------------
**ESC2-1 — class REPAIR-NEEDED. The r3.2 re-attribution of the
proves-too-much exclusion names the WRONG FACE: the disposition of
ESC-L0-3 fails on its own text (dedup rule invoked: the disposition is
attacked, not the original finding).**

Quote (Section 1.6, "Why this does not prove too much", r3.2):
> "The operative exclusion is STEP 3's DOMAIN ENLARGEMENT: the coupling
> face Gamma_mid is INTERIOR to the domain on which (H-UP-fam)'s input
> pair solves the PDE — the pair fed to it in STEP 3 consists of solutions
> on all of Omega_up (clauses (cl-F)/(cl-C)), so the hypothesis quantifies
> only over pairs solving the PDE ACROSS the face, and that cross-face
> solvability IS the transmission content a bare coupling lacks. A bare
> transmission coupling of two subdomains with no transmission condition
> supplies no class of states solving anything across its face, so the
> STEP-3 hypothesis has nothing to consume and the argument does not run."

Attack (derivation level, three convergent prongs).
(1) *Wrong face.* ESC-L0-3's mechanism — which this r3.2 text purports to
land — was: "(H-UP-fam) at depth h/2 places the coupling face
**Gamma_in^coll** in the INTERIOR of its domain Omega_int^{h/2}". The r3.2
body names **Gamma_mid** instead, and — because Gamma_mid is the BOUNDARY
of Omega_int^{h/2}, not interior to it — silently swaps the anchoring
domain from "(H-UP-fam)'s domain" to "the domain on which the input pair
solves the PDE" (= Omega_up). The give-away is in the document itself: the
r3.2 revision-log disposition row for ESC-L0-3 says "the coupling face is
INTERIOR to (H-UP-fam)'s domain" (true only of Gamma_in^coll); the body
contradicts its own log row.
(2) *The printed sentence fails to exclude the cited instance.* The
annotation credits "ESC-L0-3's strengthened bare-coupling instance" — two
subdomains joined at **Gamma_in^coll** with no transmission condition, the
collar side W^{1,infinity} with a margin far face, the interior-side
hypothesis own-side-only. For that instance the glued pair (U_B on
Omega_int^h, U_A on C_h) IS C^1 across Gamma_mid (Gamma_mid lies inside
C_h, where U_A alone lives): "solving the PDE across [Gamma_mid]" is
SATISFIED by the bare-coupled pair, so the Gamma_mid-based exclusion as
printed does not bite. What actually blocks the instance is that the
bare interior hypothesis lives on Omega_int^h (stopping AT Gamma_in^coll)
and cannot be applied on the enlarged Omega_int^{h/2} ∋ Gamma_in^coll —
i.e. exactly the Gamma_in^coll-interiority mechanism the r3.2 text failed
to transcribe. Equivalently at the argument level: without the enlargement
one would need the TRACE ON Gamma_in^coll, and frusta based there sit at
distance zero from the data-carrying coupling face — defect (b) verbatim.
(3) *False quantifier claim.* "The hypothesis quantifies only over pairs
solving the PDE ACROSS the face [Gamma_mid]" is false of (H-UP-fam) as
printed: its solutions live on Omega_int^{h/2}, take the Gamma_mid trace as
DATA, and are required to solve across Gamma_in^coll (interior to the
domain), NOT across Gamma_mid. The inference offered for it ("the pair fed
to it in STEP 3 consists of solutions on all of Omega_up, so the
hypothesis quantifies only over...") is a non sequitur — what the fed pair
satisfies is not what the hypothesis quantifies over; and if the exclusion
were really "inputs must solve on all of Omega_up", it would be a property
of the CLAIM's quantifier that the r2 setup possessed identically while
its argument proved too much — destroying the paragraph's stated thesis
that the exclusion is STEP 3's enlargement.
Repair (content, one paragraph): state the mechanism face-correctly and
face-dependently — the enlargement places the r2/bare coupling face
Gamma_in^coll in the INTERIOR of (H-UP-fam)'s domain, so the hypothesis's
states solve the PDE across THAT face (the transmission content a bare
coupling across it lacks), and the enlargement removes any need to control
the Gamma_in^coll trace (defect (b)'s locus); for a coupling across a face
interior to C_h (e.g. Gamma_mid itself), the operative exclusion is STEP
1's requirement of certified two-sided regularity across the face (Lemma
1.4's frusta straddle it) — in sum, every face of the decomposition is
crossed by a certified structure, and a bare coupling's face is crossed by
nothing. Not BREAKS: no proof step consumes this paragraph, and the
conclusion (the derivation does not prove too much) is TRUE — I verified
it through exactly the face-dependent argument above. But this is the
judge's own §5 falsifier applied in-document, it is the SECOND consecutive
wrong mechanism at the same paragraph, and the E-4 adjudicator will re-run
it: statement-level content must change. REPAIR-NEEDED.

------------------------------------------------------------------------------
**ESC2-2 — class AMENDMENT. The retirement annotation's universal "the
exclusion was never Step 1" is false by instance.**

Quote (same paragraph, r3.2 annotation):
> "*(r3.2 annotation of record: the r3 sentence "Step 1 is unavailable:
> there is no OVERLAP region ..." is RETIRED — refuted by ESC-L0-3's
> strengthened bare-coupling instance, for which Step-1/Step-2 analogues
> genuinely run; the exclusion was never Step 1.)*"

Attack. For a bare coupling ACROSS GAMMA_MID (subdomains C_{h/2} and
Omega_int^{h/2}, no transmission condition — squarely inside the
paragraph's quantifier "a bare transmission coupling of two subdomains"),
the glued object solves no PDE across Gamma_mid, so Lemma 1.4 on O = C_h
(which straddles Gamma_mid) has no solution to act on: STEP 1 is EXACTLY
the operative exclusion there, and (MID-TRACE) — STEP 3's same-trace input
— never becomes available. Note the interior-side object of this coupling
is a perfectly good (H-UP-fam)-class state (it solves across Gamma_in^coll,
interior to its domain), so the quoted closing sentence "the STEP-3
hypothesis has nothing to consume" is ALSO false for this instance. The r3
sentence was wrong as a universal in one direction; the r3.2 retirement is
wrong as a universal in the other. Fix: replace "the exclusion was never
Step 1" with "the exclusion is face-dependent: Step 3's enlargement for
couplings across Gamma_in^coll; Step 1's two-sided-regularity requirement
for couplings across faces interior to C_h" (rides ESC2-1's rewrite).
AMENDMENT.

------------------------------------------------------------------------------
**ESC2-3 — class AMENDMENT. "nothing straddles any face" in the corrected
"Which (H-UP) form" block is literally false: STEP 1's frusta straddle
Gamma_mid — and that is the step's mechanism, not an accident.**

Quote (Section 1.6, "Which (H-UP) form", r3.2-corrected block):
> "(r-b) as written is a two-sided lens-shaped energy argument STRADDLING
> the face — that lens geometry is NOT used (the r3 frusta live wholly
> inside C_h; nothing straddles any face)."

Attack. The frusta of STEP 1 are based on balls B(x_0, R) CENTERED AT
points x_0 in Gamma_mid: they extend on both sides of Gamma_mid inside
C_h — they straddle the mid-collar face, which is moreover THE coupling
face of the two-face decomposition (STEPs 2 and 3 couple across it). The
true and honest statement is sharper: nothing straddles a DATA-CARRYING
face (Gamma_in^coll or Gamma_I) — that is what distinguishes the r3
construction from (r-b)'s lens across Gamma_in^coll — while the frusta DO
straddle Gamma_mid precisely because Gamma_mid carries no data: its trace
is STEP 1's OUTPUT, produced from two-sided collar regularity, never an
input. As printed the sentence obscures the mechanism inside the very
block whose F-4 purpose is attribution precision, and it feeds the same
Gamma_mid/Gamma_in^coll conflation as ESC2-1. Fix: "nothing straddles a
data-carrying face; the frusta straddle only Gamma_mid, whose trace is
Step 1's output, not an input". AMENDMENT.

------------------------------------------------------------------------------
**ESC2-4 — class AMENDMENT. The r3.2 window-arithmetic sentence of the
mid-face falsifier leg consumes a speed bound OUTSIDE the domain where
lambda_max is defined — in the very run whose exterior is deliberately
roughened — and quantifies over a t_p case its own pinned trigger
excludes.**

Quote (Section 1.6, falsifier, r3.2):
> "Window arithmetic of record: any contaminant above the bound at t_p
> lives downstream of Gamma_I or upstream of Gamma_in^coll, hence at
> distance >= d_0 from Gamma_mid, and travels at speed <= lambda_max —
> arrival time >= d_0/lambda_max = 2x the probed window."

Attack (executor level — the class the judge sustained as L1-5, and the
falsifier-correctness discipline of R5).
(i) lambda_max := sup_{C_h x [0,T_f]}(|u-bar| + c-bar) is a COLLAR
constant. Upstream of Gamma_in^coll the base state is deliberately
ROUGHENED in this run and carries no hypothesized or monitored bound —
(H1.1') and the (G3)-box clause are collar-only by construction, and the
device-class interior is exactly where global bounds fail. "Travels at
speed <= lambda_max" applied to the exterior path segment is therefore
unjustified as printed; an executor who implements arrival-time = (total
distance)/lambda_max with exterior propagation faster than the collar sup
would derive a wrong (too-late) arrival bound and could mis-certify. The
correct derivation — which rescues the identical conclusion — routes
through the terminal collar segment: any influence path from
Gamma_in^coll ∪ Gamma_I to Gamma_mid has length >= d_0 INSIDE closure(C_h)
(by (D-coll)'s distance bound), where the speed bound lambda_max is a
theorem-grade constant; hence arrival >= (collar entry time)
+ d_0/lambda_max >= t_p + 2x window, regardless of exterior speeds.
(ii) "Any contaminant above the bound AT t_p ... upstream of
Gamma_in^coll" is vacuous under the r3.2-pinned trigger, which requires
the field at the scheme bound on ALL of Omega_up (the interior included)
at t_p: at t_p no such contaminant exists in Omega_up. The operative case
the arithmetic must (and, via (i), does) cover is post-t_p growth in the
uncontrolled exterior entering the collar during the window. As printed
the sentence still reasons from the WEAKER trigger the r3.2 repair itself
retired. Conclusion (2x window) is correct under both fixes; the recorded
justification is the wrong derivation of the right window and must be
restated (mirror in register row 1''s condensed cell, which repeats
"speed <= lambda_max"). AMENDMENT.

------------------------------------------------------------------------------
**ESC2-5 — class AMENDMENT. Status (a)'s "IS a theorem of this document"
is now unconditionally quantified over a solution class the r3.2 text
itself made formally free (the NG-9 delegation), while the backing (EI)
run exists only for the (H1.4)-grade class.**

Quote (Section 1.6, Status of (H-UP-fam), case (a), with r3.2 insertions):
> "(a) If W-bar is W^{1,infinity} on all of Omega_up, (H-UP-fam) IS a
> theorem of this document at every depth with a given (D-coll)-class
> split: for same-interior-problem pairs (same forcing on Omega_int^s —
> r3.2, ESC-L0-2 = F-1, so the difference solves the homogeneous system)
> the energy identity (EI) closes on Omega_int^s ..."

Attack (hypothesis accounting; the interaction is r3.2-NEW: (cl-C)/the
(H-UP-fam) formulation clause made the solution class an explicit free
parameter "part of this hypothesis's own formulation ... DELEGATED to
NG-9"). (H-UP-fam)'s uniqueness property is a statement WITHIN that
delegated class. Case (a) asserts the full hypothesis — class included —
is a theorem of this document; but the (EI) run it sketches is available
for C^1-grade pairs (the (H1.4) class; the divergence-theorem package on
the (D'')-Lipschitz Omega_int^s), and beyond C^1 only via the 1.5.3
mollification extension, which is THEOREM* with the corner residual NG-3 —
and Omega_int^s has NEW corner curves where Gamma_mid meets Gamma_w that
1.5.3 never inventoried. If NG-9 instantiates the class any wider than
(EI)-admissible (e.g. L^2-weak), case (a) as printed is unproven. One
clause scopes it: "IS a theorem ... for pairs of (H1.4)-grade (C^1)
members of the class (H^1 members via 1.5.3, THEOREM* modulo NG-3,
corner set now including Gamma_mid ∩ Gamma_w)". Load-bearing only for the
smooth-base sanity reduction (case (b) delegates everything to NG-9), so
AMENDMENT, not REPAIR.

==============================================================================
## §3 CONFIRMED passages (strongest attack tried, each)

**C2-1 — (cl-C) + proof-head left-closedness machinery: CONFIRMED.**
Attacks tried: (α) is C([0,T_f]; L^2_loc) enough for the maximality engine
— yes, re-derived (left-limit closure of the sup-set; slice-wise reading
declared); (β) mismatch between L^2_loc slices and STEP 1's pointwise zero
— fails: on C_h, (H1.4) gives C^1, and a.e.-zero + continuity gives
pointwise zero on B(x_0,R) ∩ C_h; (γ) circularity of the NG-9-delegated
class — fails, delegation declared in the Claim and absorbed by the
SCHEMA label and by (H-UP-fam)'s formulation clause; (δ) does STEP 3's
trace input exist for a merely-(cl-C) interior restriction — yes: Gamma_mid
lies interior to C_h where U is C^1, so the restriction's Gamma_mid trace
is the pointwise value, zero by (MID-TRACE).

**C2-2 — (cl-F) and its three-site threading: CONFIRMED.** Attacks tried:
a consumable statement still lacking the forcing clause (none — §1); the
"forcing free downstream of Gamma_I" parenthetical against "differing
arbitrarily downstream" (consistent); whether the F-1 counterexample
annotation is faithfully recorded (it is, verbatim in content).

**C2-3 — eps_1' definition and threading + UNION two-case closure:
CONFIRMED.** Attacks tried: boundary case t* + eps_1 = T_f (lands in the
contradiction case); positivity at t* → T_f⁻ (eps_1' > 0 exactly from
t* < T_f); whether STEP 1's R-choice survives the cap (it does:
lambda_max·eps_1' ≤ d_0/2).

**C2-4 — STEP 2 completed checklist: CONFIRMED.** Attack tried: any
FIFTH consumable ingredient beyond (H1.1')/(H1.2)/(H1.3)/(H1.4)/(D'') —
Theorem 1''s statement consumes exactly these plus the data agreement,
supplied by U(·,t*) = 0 and (MID-TRACE).

**C2-5 — (D-coll) Lipschitz clause + family inheritance: CONFIRMED.**
Attack tried: a consumer of Omega_int^{h/2}'s Lipschitz-ness not covered
by the clause's declared consumers (Status (a) (EI) run; the family split
class) — none found; the tangency failure mode is honestly named.

**C2-6 — (H-UP-fam) restricted quantifier + endpoint drop (F-2
disposition): CONFIRMED.** Attacks tried: d_0(h/2) consistency with
(D-coll) (equal by definition); whether the "given split" restriction
weakens the proof's consumption (no — s = h/2 is supplied by (D-coll),
which the Claim assumes); whether the retained r3 annotation misstates
F-2 (it does not).

**C2-7 — F-4 attribution content: CONFIRMED** (modulo ESC2-3's new
parenthetical). Attack tried: re-reading L1-7's (r-b) text against the
corrected block — the correction now matches L1-7's actual words
("two-sided lens-shaped energy argument straddling the face"), and the
log-row annotation mirrors it.

**C2-8 — pinned falsifier trigger (ESC-L0-4 = F-5 disposition):
CONFIRMED** as a trigger: under the Omega_up-inclusive reading the leg is
exactly the (MID-TRACE) prediction; register row 1' mirrors the pinned
wording. (The appended arithmetic sentence carries ESC2-4.)

**C2-9 — leg-17 r3.2 text (Remark 1.5.5 + log-row F-6 annotation):
CONFIRMED — A-2 fully landed.** Strongest attacks tried: (α) "adjacent
spectral gaps equal to c-bar" at the loci — exact (spectra {−c, 0(×3), +c}
and {−2c, −c(×3), 0}: adjacent distinct gaps c-bar, extreme pair 2c-bar);
(β) multiplicity jump hunt — the (1,3,1) pattern is constant through both
loci, so no projector degeneracy claim is even at risk; (γ) the
"all pairwise separations ≥ c-bar" clause — true (c, c, 2c); (δ) whether
any consumer still cites the retired "mutual = c-bar" phrase unannotated —
none (the Remark and the log row both carry the r3.2 correction).

**C2-10 — r3.2 revision-log entry bookkeeping: CONFIRMED.** Re-counted:
13 IDs = 7 + 6; dedup pairs ESC-L0-2 = F-1, ESC-L0-5 = F-3, ESC-L0-4 = F-5
match the round-1 files' own cross-declarations; 10 distinct findings =
2 REPAIR + 8 AMENDMENT, 0 BREAKS — matches both round-1 summary tables;
"every finding FIXED" is accurate as a disposition-table claim (this
round finds one of those FIXED claims inadequate: ESC2-1).

**C2-11 — the two-face proof core at r3.2 state (STEPs 1-3 + UNION with
(cl-C)/(cl-F)/eps_1'): CONFIRMED.** Strongest attacks tried this round:
(α) exactness of the cover Omega_up = Omega_int^{h/2} ⊔ Gamma_mid ⊔
C_{h/2} (holds — the remaining boundary pieces lie in ∂Omega_up); (β) a
trace-notion mismatch between STEP 1's pointwise (MID-TRACE) and
(H-UP-fam)'s "same trace" (fails — C^1 across Gamma_mid); (γ) λ_max
consistency between the proof head and Lemma 1.4's per-region constant
(the C_h × [0,T_f] sup majorizes); (δ) re-run of the retracted-proof
defects against the new text (no analogue of either). The delivered
strength remains THEOREM modulo (H-UP-fam), label of record SCHEMA per
J-r2p-1 — the discipline is intact at every consumer site checked
(Section 1.6, 3.4(3)(a), Section 5 clause (i), register row 1', NG-9).

==============================================================================
## §4 Summary table

| ID | Passage (r3.2 text) | Class |
|---|---|---|
| ESC2-1 | proves-too-much re-attribution: wrong face (Gamma_mid for Gamma_in^coll); fails on ESC-L0-3's own instance; ESC-L0-3 disposition NOT discharged | REPAIR-NEEDED |
| ESC2-2 | retirement annotation "the exclusion was never Step 1" — false universal (Gamma_mid-coupling instance) | AMENDMENT |
| ESC2-3 | "nothing straddles any face" — STEP 1's frusta straddle Gamma_mid by design | AMENDMENT |
| ESC2-4 | falsifier window arithmetic: collar λ_max applied to the roughened exterior; t_p case vacuous under the pinned trigger | AMENDMENT |
| ESC2-5 | Status (a) "IS a theorem" unscoped over the NG-9-delegated class | AMENDMENT |

Totals: 5 objections = 0 BREAKS-THE-LEG + 1 REPAIR-NEEDED + 4 AMENDMENT.
Discharge verdicts (§1): L0-7(a)/(b) = L1-7(i)/(ii) remain DISCHARGED;
L1-8/A-2 fully landed (F-6 closed); round-1 dispositions ADEQUATE for
ESC-L0-1, ESC-L0-2 = F-1, ESC-L0-5 = F-3, ESC-L0-6, ESC-L0-7, F-2, F-4
(modulo ESC2-3's new sentence), ESC-L0-4 = F-5 (modulo ESC2-4's new
sentence), F-6; INADEQUATE for ESC-L0-3 (ESC2-1/ESC2-2). No finding
touches a step of the two-face proof; the SCHEMA label discipline is
correct as printed and no label motion is proposed by this round.

==============================================================================
## §5 Self-falsifiers (what kills each finding)

- ESC2-1 dies if Gamma_mid is shown INTERIOR to Omega_int^{h/2} (it is not
  — Omega_int^{h/2} := Omega_up \ closure(C_{h/2}) and Gamma_mid ⊂
  closure(C_{h/2})), or if ESC-L0-3's strengthened bare-coupling instance
  (coupled at Gamma_in^coll) is shown EXCLUDED by the printed
  Gamma_mid-based sentence — i.e. if its glued pair is shown NOT to solve
  the PDE across Gamma_mid (it does: the collar-side member is a single
  C^1 solution on C_h ⊃ Gamma_mid).
- ESC2-2 dies if the Gamma_mid bare coupling is shown outside the
  paragraph's quantifier "a bare transmission coupling of two subdomains
  with no transmission condition", or if its exclusion is derived WITHOUT
  Step 1 failing (note its interior-side member is (H-UP-fam)-admissible,
  so the STEP-3-has-nothing-to-consume route is closed).
- ESC2-3 dies if the STEP 1 frusta are shown not to straddle Gamma_mid —
  refuted by the construction itself (balls centered at x_0 ∈ Gamma_mid).
- ESC2-4 dies if a bound "exterior propagation speed ≤ lambda_max" is
  exhibited among the run's hypotheses/monitors (the run's exterior is
  deliberately roughened and (H1.1')/(G3)-box are collar-only), or if the
  pinned trigger is shown to permit an above-bound contaminant inside
  Omega_up at t_p.
- ESC2-5 dies if the NG-9-delegated class is pinned of record to
  (EI)-admissible members (e.g. the (H1.4) class), making case (a)'s
  unconditional quantification sound as printed.

END — machine summary: {objections: 5, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc3_r2_l0.md}
