# ESCALATION REFUTATION — DOC-2 (phaseD_meanswirl_formalization.md), ROUND 2, LENS 0
# (hyperbolic-systems / functional-analytic rigor)

Date: 2026-08-19 (S-FOUNDATIONS-C escalation window, until-dry round 2).
TARGET: the r5 escalation-repair text ONLY — the answers to the round-1
escalation refutations `r2pass/esc_doc2_r1_l0.md` (ESC-L0-1..4) and
`r2pass/esc_doc2_r1_l1.md` (ESC-1..4), i.e. every passage marked "(r5)"
per the revision-log header block (lines 98–134) and §6-quinquies ROUND 2
(lines 2410–2445): the (w1) correction (~1489–1503), the two-of-three
rider correction (~1523–1539), the H-CVX connected-adiabat rewording
(~1574–1601), the JUMP-SET-FORM conclusion (~1602–1635), the closure edit
(~1712–1717), the three-step ASSEMBLY (~1730–1776), the proof-state /
class block (~1802–1841), falsifier (d) (~1876–1883), the register row
(2135), the G-f entry (~2192–2194). Leg-7 / A-1 scope: grep-verified that
NO r5 marker touches D.2 — the A-1 landing is re-checked for regression
only (Part B, C-13). Adjudication of record consumed:
`r2pass/VERDICT_r2pass.md` §2.1 / §4(b) / §4(c) (E-3 spec, J-r2p-2/3);
full round-1 objection texts read in full.

DEDUP RULE APPLIED: no dispositioned objection is re-raised unless the
disposition itself fails — where that is claimed (ESC2-L0-3, ESC2-L0-4)
the prior ID is cited and the failure of the disposition is stated
explicitly. All quotes verified verbatim against the r5 file (line reads).

MANDATE CHECK (discharge verification): for each of the eight round-1 IDs
answered by r5 I verified (a) the round-1 finding's own repair spec,
(b) the landed r5 text, (c) the §6-quinquies ROUND 2 row. Verdicts:

| Round-1 ID | r5 delivery | DISCHARGE VERDICT |
|---|---|---|
| ESC-L0-1 (BREAKS) | per-front dichotomy dropped; JUMP-SET form; witness recorded as PASSING; "complete AS WRITTEN" retracted; falsifier (d) minted | DISCHARGED as to the dichotomy itself — but the restated conclusion display carries one underived clause (ESC2-L0-1 below) and a fresh "proved as written" certification rides on it |
| ESC-L0-2 (REPAIR) | stale "made true" tag retracted by annotation, mechanism recorded, quotation preserved | DISCHARGED (Part B, C-8) |
| ESC-L0-3 + ESC-3 (AMEND) | rider replaced: ALL SIX directions fail, witnesses re-attributed ((β) + φ-independent non-solution adopted) | DISCHARGED (Part B, C-9 — all six directions independently re-verified) |
| ESC-L0-4 (AMEND) | (w1) re-scoped to existential instance with a.c.-leg derivation | PARTIALLY DISCHARGED — the adopted instance certificates are themselves refuted by the document's own [T-NSW](a) record (ESC2-L0-3 below; the round-1 suggested wording was defective and r5 transcribed it) |
| ESC-1 (REPAIR) | assembly rewritten in three steps; component-quantified branch eliminated; distributional-∂_φ closure is exhaustive by construction | DISCHARGED as to exhaustiveness (the round-1 gap is genuinely closed — no case analysis over strata remains in the closure) — new defects in the rewritten steps are ESC2-L0-1/ESC2-L0-2 |
| ESC-2 (AMEND) | a.e.→everywhere bridge written as step (1) | PARTIALLY DISCHARGED — the bridge as written asserts blanket trace continuity, false at in-class front crossings (ESC2-L0-2 below) |
| ESC-4 (AMEND) | H-CVX reworded to connected-adiabat form; closure cites the supplied segment; in-model nil exposure recorded | PARTIALLY DISCHARGED — the rewording was NOT propagated to falsifier (a), which still runs the vacuously-satisfiable arc form as its refutation trigger (ESC2-L0-4 below) |

Label discipline verified: both iff clauses at SCHEMA (J-r2p-2/3) in the
class block, register row, §6-quinquies; layer/gate caveat carried; no
label self-upgrade. (The PROSE self-certification "proved as written" is
a different matter — see ESC2-L0-1.)

==============================================================================
## PART A — OBJECTIONS (4 findings: 0 BREAKS-THE-LEG, 1 REPAIR-NEEDED, 3 AMENDMENT)

------------------------------------------------------------------------------
**ESC2-L0-1 — REPAIR-NEEDED. The r5 conclusion display and assembly step
(3) assert "Ṽ piecewise-C¹ meridional" with zero supporting argument; the
clause is not one line, its natural proof routes hit genuine C¹-grade
obstructions (one of them Sard-type, contradicting the assembly's own
"Sard-free" virtue if prosecuted that way), and the fresh completeness
certification "is proved as written" is refuted by the gap — the third
consecutive round in which the assembly carries an over-certification.**

Verbatim quotes (conclusion display, ~1629–1632; assembly step (3),
~1767–1772; class block, ~1820–1823):

> "and V coincides a.e. with a piecewise-C¹ MERIDIONAL field Ṽ(x, r),
> so all one-sided limits are φ-independent and the essential jump set
> is a rotation-invariant (meridional-curve × S¹) set."

> "Hence ∂_φ V = 0 as a distribution on D × S¹_φ; a distribution with
> vanishing φ-derivative on compact S¹ fibers is φ-independent, so
> V = Ṽ(x, r) a.e. with Ṽ piecewise-C¹ meridional: all one-sided limits
> are φ-independent and the essential jump set is a rotation-invariant
> (meridional-curve × S¹) set."

> "the second iff, in its r5 JUMP-SET form, is proved as written under
> H-NC + H-WR (+ connected-adiabat H-CVX on the n_m = 0 strata)"

Derivation-level attack. The fiber-averaging fact delivers ONLY
Ṽ ∈ L¹_loc with V = Ṽ∘π a.e. The upgrade to "Ṽ piecewise-C¹ meridional"
— in the §0 sense the document itself minted at r1 ("finitely many C¹
curves, off which V is C¹ with one-sided limits at each curve", lines
206–209) — is a genuine theorem with no proof in the document, and its
natural routes obstruct at exactly the C¹ front grade of the class:

(i) SECTION ROUTE (Ṽ = V(·, ·, φ′) for a good φ′): needs the φ′-section
of the C¹ front hypersurfaces to be a finite family of C¹ curves, i.e.
a regular-value/Sard step for the C¹ function φ|_F. Sard for
f: ℝ² → ℝ requires C² (Whitney's C¹ counterexample: a C¹ function
critical on an arc of non-constant values) — at the class's C¹ front
grade this route is UNAVAILABLE, and consuming it would falsify the
assembly's own claim "No transversality or Sard-type genericity is
consumed anywhere in this assembly" (~1758–1759).

(ii) FRONT-FREE-SECTION ROUTE (the sharpest in-class argument I could
build, supplied here so the repair is a transcription): for
(x₀, r₀) ∈ D whose fiber {(x₀,r₀)} × S¹ is NOT fully contained in the
(closed) front set, there exist a ball B ∋ (x₀,r₀) and φ′ with
B × {φ′} front-free; then Ṽ|_B = V(·, ·, φ′) ∈ C¹. Hence
Ṽ ∈ C¹(D ∖ S) with S := {(x, r) : fiber ⊆ front set}, closed. But the
route delivers NO §0-grade structure for S: S × S¹ sits inside finitely
many C¹ 2-surfaces, and a single C¹ front can contain an UNCOUNTABLE
(Cantor-parametrized) family of φ-circles — e.g. the graph front
x = f(r, φ), f ∈ C¹, with f_φ = 0 exactly on C × S¹ for a Cantor set
C of radii — so the tube-neighborhood argument bounds S only by
countable 1-rectifiability (H¹-finite images of C¹ maps with possibly
vanishing derivative), NOT by "finitely many C¹ curves with one-sided
limits". The clause as printed is therefore UNPROVEN, and not by an
omitted one-liner: closing it needs either added front regularity or a
structure theorem for S that the document does not state.

(iii) The two clauses r5 hangs ON the regularity claim are in fact
derivable WITHOUT it — which is the repair's cheapest shape:
"all one-sided limits are φ-independent" follows from V = Ṽ∘π a.e.
plus a.e.-determination of one-sided traces on the locally φ-invariant
patches (whose local product structure the flow-invariance step already
supplies); "essential jump set = rotation-invariant (meridional-curve ×
S¹)" follows because an essential jump point carries its full φ-circle
(rotation invariance of the a.e. class), that circle lies in
int{n_φ = 0} (jump-set containment + invariance of the essential class),
and int{n_φ = 0} is locally a C¹-curve × φ-arc product by the step-(2)
graph argument — so the local curve structure of the ESSENTIAL jump set
is available directly, no global Ṽ-regularity needed.

CONSEQUENCE: the clause "with Ṽ piecewise-C¹ meridional" must be either
PROVED (with whatever added hypothesis it truly needs) or WEAKENED (e.g.
"V = Ṽ(x, r) a.e. with Ṽ ∈ C¹ off a closed rotation-invariant meridional
set", deriving the limits/jump-set clauses per (iii)); and the sentence
"is proved as written" (~1820–1823) is REFUTED as it stands — the same
species of assembly over-certification retracted at r4 ("complete AS
WRITTEN") and at r5 (the r4 retraction), now in its third consecutive
round, exactly what the r5 text itself flags as the honest price
("r5 is the SECOND consecutive round in which the assembly step needed
repair" — the counter must go to three).

Class: **REPAIR-NEEDED** (per the ESC-1 precedent: conclusion clause not
shown false — no constructed in-class counterexample; the other display
clauses stand; but a named, non-one-line proof gap sits inside the
conclusion of record with a completeness certification attached). NOT
BREAKS: the core conclusion ∂_φV = 0 + jump-set containment is proved,
and I could not construct an in-class witness against the clause (my
best attempt — derivative jumps supported on a Cantor circle family —
is KILLED in-class by openness of {[∇V] ≠ 0} wherever one-sided C¹
extensions exist; recorded in the self-falsifier).

NOVELTY/DEDUP: the Ṽ-regularity clause is r5-minted; no prior ID
(L0-*, L1-*, ESC-L0-1..4, ESC-1..4) touches the meridional
representative's regularity. ESC-1's disposition (assembly rewritten) is
NOT re-raised — its exhaustiveness fix is verified DISCHARGED above;
this is a new defect in the rewritten step's final clause.

------------------------------------------------------------------------------
**ESC2-L0-2 — AMENDMENT. Step (1)'s blanket trace-continuity sentence is
false in the declared multi-front class at front–front intersections —
which §0 itself names as generic in-class objects (triple-point shear
layers); the bridge and the closure survive, but the written line needs
its scope qualifier and the insensitivity note.**

Verbatim quote (assembly step (1), ~1748–1752):

> "One-sided traces of a piecewise-C¹ field are CONTINUOUS on each
> front, so the jump [V] is continuous there; {g ≠ 0} ∩ {n_φ ≠ 0} is
> dense in the relatively open set {n_φ ≠ 0} (n_φ continuous on a C¹
> front), hence [V] ≡ 0 on {n_φ ≠ 0} and, by continuity, on its
> closure."

Attack. The §0 class admits finitely many fronts with NO disjointness or
transversality restriction, and explicitly declares configurations where
fronts MEET: "per-phase RDE fields generically contain slip surfaces —
fill/product interfaces, triple-point shear layers" (§0, lines 216–218)
— a triple point IS a front–front intersection (detonation + transmitted
shock + slip line along one curve), the in-scope physical object. Where
front A meets front B, the side of A is split by B into two pieces of V
with different limits: the one-sided trace on A fails to exist as a
single value at the intersection curve (or, where it exists, fails
continuity across it). The blanket sentence is therefore FALSE as a
statement about "each front" in the declared class. The ARGUMENT
survives untouched, for two reasons the text should state: (a) points
where one-sided traces fail to exist are outside the jump set by
definition, and the intersection set is closed and H²-null on the front,
so density of {g ≠ 0} ∩ {n_φ ≠ 0} minus the intersection set still
delivers [V] ≡ 0 on {n_φ ≠ 0} off intersections and on the closure off
intersections; (b) step (3)'s atom argument integrates against H² and is
blind to H²-null sets, so the distributional conclusion ∂_φV = 0 is
unaffected. Repair: scope the sentence ("continuous on each front OFF
the closed H²-null set where it meets other fronts or its own edge") and
append the one-line insensitivity note. Class: **AMENDMENT** (per the
L1-4 precedent: scope a true-where-it-matters sentence; no conclusion
motion).

NOVELTY/DEDUP: ESC-2 demanded the bridge be written and is DISCHARGED as
to that demand; this attacks the r5-WRITTEN bridge's blanket
quantification — text that did not exist at round 1. No prior ID raises
front crossings; grep of both r2pass lenses and all esc files for
"triple point"/"crossing"/"intersection" on this doc: no prior coverage.

------------------------------------------------------------------------------
**ESC2-L0-3 — AMENDMENT. The r5-corrected witness (w1) carries instance
certificates refuted by the document's own record: the cited "standing
RDE wave-frame flow of record" is front-carrying (not smooth) and
attains |w_rel| = c on the in-scope CJ locus (not "bounded away from
c") — the ESC-L0-4 disposition transcribed a round-1 repair spec that
was itself defective, and the disposition fails to that extent.**

Verbatim quote (~1489–1493):

> "(w1) a smooth genuinely φ-dependent exact wave-frame solution with
> w_rel bounded away from 0 and c — e.g. the standing RDE wave-frame
> flow of record, [T-NSW] — has K ≠ 0 BY THE A.C. LEG of the second
> iff under H-NC + H-WR, which such a field satisfies"

Attack, from the document's own lines. (a) "smooth ... e.g. the standing
RDE wave-frame flow": the standing flow of record is the rotating
DETONATION flow — front-carrying by construction ("w_rel ≈ −D_CJ at the
interface", line 1354, presupposes the detonation front; the helical
detonation front is the declared in-scope instance per judge act (v)).
A front-carrying field is not a smooth solution on D × S¹: the "e.g."
instantiates a smooth-quantified witness with a non-smooth object.
(b) "w_rel bounded away from 0 and c": the H-NC hypothesis two
paragraphs below was REWORDED at r2 precisely because "the in-scope CJ
locus itself VIOLATES" the pointwise condition (~1544–1546), and
"[T-NSW](a) — the relative sonic locus IS the Chapman–Jouguet surface"
(~1548–1549): the standing flow ATTAINS |w_rel| = c on an in-scope
hypersurface, so it is not bounded away from c on its domain; [T-NSW](a)
certifies |w_rel| > c only ON THE MARCHING DOMAIN (~1560–1561), and
boundedness away from c holds only on subdomains compactly inside it.
The same document cannot host both sentences unannotated. The PAYLOAD
survives cleanly — the operative conditions really are H-NC + H-WR
(empty-interior form), which the standing flow satisfies (sonic locus =
hypersurface, co-rotation locus empty interior), and the a.c.-leg
contrapositive then yields K ≠ 0 from genuine φ-dependence OFF fronts
(of record: the D.19 pumping ∂_φp ≠ 0). Repair (one sentence): replace
the certificates with the operative ones — "an exact wave-frame solution
genuinely φ-dependent off fronts and satisfying H-NC + H-WR — e.g. the
standing RDE wave-frame flow of record, [T-NSW], or its restriction to
any subdomain compactly inside the marching region for a smooth
instance". Class: **AMENDMENT** (the witness's role is carried by (w2)
alone in any case, as the round-1 record already noted).

DEDUP DECLARATION (disposition failure named per the brief): ESC-L0-4 is
dispositioned FIXED (§6-quinquies row, 2432) by adopting the round-1
lens-0 suggested wording verbatim ("w_rel bounded away from 0 and c,
[T-NSW]"). The disposition fails ONLY in that the adopted spec — my own
lens's round-1 suggestion — was itself defective against [T-NSW](a) as
cited in-document; the re-scoping to an existential instance and the
removal of "by definition" are correct and stand. The failure is in the
transcribed certificate, not in the r5 reviser's execution.

------------------------------------------------------------------------------
**ESC2-L0-4 — AMENDMENT. The ESC-4 rewording was not propagated to
falsifier (a): the refutation trigger still runs on "arc H-CVX" — the
retracted, vacuously-satisfiable form — and against "the r4 closure",
so the printed rejector spec classifies the detached-branch isentropic
sheet as a REFUTATION while the r5 hypothesis excludes it, contradicting
the item's own parenthetical in exactly the configuration ESC-4
adjudicated.**

Verbatim quote (falsifier block, ~1863–1867):

> "and the n_m = 0 case's own falsifier: an EOS satisfying arc H-CVX
> together with a nontrivial azimuthal sheet carrying [s] = 0 would
> REFUTE the r4 closure (a non-convex EOS admitting an isentropic
> nontrivial jump is the expected out-of-hypothesis exhibit, not a
> refutation);"

Attack. After the r5 rewording, "arc H-CVX" names precisely the form the
hypothesis line RETRACTED as vacuously satisfiable: a Menikoff–Plohr
detached-branch EOS with an isentropic nontrivial azimuthal sheet
SATISFIES "arc H-CVX" (vacuously — no connecting arc exists) and
carries [s] = 0, so the printed trigger fires REFUTED; under the r5
connected-adiabat form the same exhibit is OUT-OF-HYPOTHESIS (the
downstream trace is not on the connected adiabat) and refutes nothing —
which is exactly what the item's own parenthetical says of it. The
sentence is thus internally contradictory post-r5 in the one
configuration the ESC-4 escalation was about, and a G-f executor
transcribing item (a) verbatim would mis-adjudicate the
hypothesis-boundary test (the L1-5 executor-misguidance defect class).
"the r4 closure" is likewise stale — the closure of record is the r5
one. Repair (one phrase each): "an EOS satisfying connected-adiabat
H-CVX (r5) together with a nontrivial azimuthal sheet carrying [s] = 0
would REFUTE the n_m = 0 closure". Class: **AMENDMENT**.

DEDUP DECLARATION: ESC-4 is dispositioned FIXED (row 2436) with the fix
enumerated as hypothesis line + closure step + in-model note — the
falsifier item is NOT in the enumeration, so this is an incompleteness
of the repair's propagation, not a re-raise of the repaired defect;
round-1 l1's remark that falsifier (a) "survives under the reworded
hypothesis" addressed the parenthetical only and did not adjudicate the
"satisfying arc H-CVX" trigger clause, which post-r5 points at a
retracted hypothesis form.

==============================================================================
## PART B — CONFIRMED passages (strongest attack tried, each)

**C-1. Jump-set-form conclusion display, core clauses (~1623–1635) —
CONFIRMED (minus the ESC2-L0-1 clause).** Strongest attacks: (i) the
"equivalently" bookkeeping — ∂_φV = 0 distributionally ⟺ {a.c. part ≡ 0
off fronts} + {n_φ[V] ≡ 0 on fronts} (mutually singular pieces), and
n_φ[V] ≡ 0 + trace continuity gives jump set ⊆ F ∖ cl{n_φ ≠ 0}
= int{n_φ = 0} (the decomposition F = cl{n_φ≠0} ⊔ int{n_φ=0} checked:
an open set disjoint from {n_φ≠0} is disjoint from its closure) — the
equivalence HOLDS with step (1) as the bridge; (ii) mixed-front
witness re-run against the new form: jump strictly inside the
φ-invariant part ⟹ jump set ⊆ int{n_φ=0} — PASSES, as the in-statement
record claims; (iii) hunting a reading under which "NO per-front
dichotomy is asserted" still smuggles a dichotomy — none: the display
quantifies over jump SETS, not fronts.

**C-2. Assembly step (1), density + closure logic (~1744–1753) —
CONFIRMED as an argument (modulo the ESC2-L0-2 scoping).** Strongest
attack: a.e.-to-dense — an H²-full subset of a relatively open subset of
a C¹ hypersurface is dense in it (relatively open sets have positive
H²); n_φ continuous on a C¹ front up to orientation sign, and
{n_φ ≠ 0} is sign-independent. The [V] ≡ 0-on-closure step is exactly
the continuity extension; no circularity with the case chains (they
prove [V] = 0 pointwise where g ≠ 0, feeding the density).

**C-3. Assembly step (2), flow-invariance at C¹ grade (~1754–1759) —
CONFIRMED.** Strongest attack tried: C¹-grade invariance failure
(tangency of a Lipschitz field on a merely-C¹ surface — the Bony–Brezis
/ Nagumo worry; a C¹ curve can touch a line on a closed set and leave
it). DISCHARGED elementarily: on the patch |n_m| = 1 (n_φ = 0, |n| = 1),
so the front is locally a C¹ graph over (r, φ) or (x, φ); n_φ = 0 on
the open patch reads f_φ ≡ 0 on an open parameter set, hence f locally
constant along φ — the φ-arc through each patch point stays in the
graph. No Sard/transversality consumed: the "Sard-free" claim is TRUE
for steps (1)–(3) as written (it would fail only on the ESC2-L0-1
clause's section route, which the assembly does not run).

**C-4. Assembly step (3), distributional closure (~1760–1772) —
CONFIRMED for the ∂_φV = 0 core.** Strongest attacks: (i) the
decomposition's φ-row: in Cartesian coordinates e_φ·∇u = (1/r)∂_φu and
∇u = {∇u} + [u] ν dH² for piecewise-C¹ u across C¹ interfaces, so the
atom density is EXACTLY n_φ[V] against Euclidean H² — pointwise
proportional to n_φ[V] under ANY equivalent normalization, so the
"normalization-free / L0-5 deferral not consumed" claim CHECKS; (ii)
fiber-averaging: ∂_φT = 0 on D × S¹ ⟹ T = (fiber mean) by testing with
ψ(x,r)·(χ − χ̄)(φ) antiderivatives — standard, one line as claimed;
(iii) the mutual-singularity split (function vs surface measure) —
holds. The residue is solely the Ṽ-regularity clause (ESC2-L0-1).

**C-5. The (⟸) re-read (~1773–1776) — CONFIRMED.** Strongest attack:
does the jump-set form still kill the atoms? [V] = 0 off the jump set
⟹ [F_φ,rel] = 0 there (fluxes continuous in state and geometry);
n_φ = 0 on the jump set; a.c. rows die off fronts by classical
∂_φV = 0 (a.e.-vanishing + per-piece continuity). Each front atom dies
pointwise. No H-CVX consumed in ⟸ — consistent with the hypothesis
line's "LOAD-BEARING ONLY ... singular leg" scoping.

**C-6. The r5 closure edit in the n_m = 0 case (~1712–1723) —
CONFIRMED.** Strongest attack: with the segment now SUPPLIED by
hypothesis, does strict s-monotonicity still need anything unstated?
Along a connected adiabat segment with G_fund > 0 at every state and
the M–P weak conditions (D.2's package), ds is one-signed with the
cubic contact only at zero strength — [s] = 0 pins the trivial jump on
either branch; the round-1 B-4 verification carries over verbatim to
the connected-adiabat form (strictly stronger hypothesis). Attack on
"the adiabat segment between the traces" (uniqueness if the connected
adiabat were non-simple): ANY connecting segment satisfying the G > 0
clause delivers the pin, so the definite article is harmless.

**C-7. H-CVX connected-adiabat wording + PRICE paragraph (~1574–1601) —
CONFIRMED.** Strongest attacks: (i) "plus, where needed, the Γ_G > −2
single-valuedness condition" as an uncheckable hedge — DISSOLVED on
reading: the hypothesis CONTENT is the geometric statement itself
("downstream trace lies on the CONNECTED shock adiabat ... G_fund > 0
at every state of the segment"); M–P/Bethe are cited as sufficient
conditions for it, not consumed as conditions; an executor checks the
geometric statement. (ii) In-model discharge: G_fund > 1 at every table
state ⟹ convex EOS ⟹ connected p-monotone adiabat (no detached branch
in range); the operating-range qualifier is carried by the cited D.2
sentence, as the round-1 l1 §3.8 attack already established. (iii)
Vacuity re-test: the reworded form cannot be vacuously satisfied — it
POSITS the connecting segment. ESC-4's hypothesis-side fix is sound;
the residue is the un-propagated falsifier (ESC2-L0-4).

**C-8. Stale-tag retraction (ESC-L0-2 discharge, ~1616–1623) —
CONFIRMED.** Mechanism re-derived: the isentropic nontrivial pair
mounted as a locally azimuthal sheet (n = ±e_φ ⟹ a meridional-plane
sheet, maximally non-axisymmetric) with per-side φ-independent states
has all conservation atoms zero (full RH), s-atom m[s] = 0, a.c. parts
zero ⟹ K = 0 with a non-axisymmetric front — the tag's falsity
EOS-generally is correctly recorded, at (α) construction grade as
claimed; quotation preserved; no stale uncontested copy (grep:
"strengthened and made true" survives only inside the retraction and
the ledger row).

**C-9. Two-of-three rider correction (~1523–1539) — CONFIRMED; ESC-L0-3
/ ESC-3 DISCHARGED.** All six directions independently re-verified with
the cited witnesses: exact ⇏ 2.5D and exact ⇏ K = 0 at (w2)=(α) (and
(w1) modulo ESC2-L0-3's certificate repair — the direction assignments
do not depend on it); 2.5D ⇏ exact and 2.5D ⇏ K = 0 at (β); K = 0 ⇏
exact and K = 0 ⇏ 2.5D at any smooth φ-independent non-solution (K ≡ 0
identically since every K row carries a ∂_φ; residuals equal and
nonzero). Strongest attack: hunting a seventh implicit implication
("any two imply the third" mis-stated?) — the rule is the exact
linear-identity consequence, correct.

**C-10. Falsifier (d), mixed-front instance (~1876–1883) — CONFIRMED.**
The instance's required verdicts are logically consistent and
discriminating: it PASSES K = 0 (checked round 1) and the r5 jump-set
conclusion (C-1 attack (ii)) while REFUTING the r4 dichotomy display —
exactly the one-instance separator claimed. Queued not executed,
commit-gated: consistent with standing discipline.

**C-11. §6-quinquies ROUND 2 table + reconciliation notes (98–134,
2410–2445) — CONFIRMED as bookkeeping, with two rows now carrying
downstream flags.** The interruption/resume reconciliation is
null=failure-clean (zero-marker measurement declared, per-ID
re-verification claimed and consistent with the landed text). Rows
ESC-L0-4 and ESC-4 say FIXED; findings ESC2-L0-3/ESC2-L0-4 above
establish PARTIAL fixes — the rows' enumerated deliveries are accurate
as enumerated (nothing claimed that was not done); the defect is in
what was left out, so the rows stand as written and the residue rides
this round's findings. No self-upgrade found; SCHEMA holds carried at
all four sites.

**C-12. Register row D.18 (2135) + gamma line (~1834–1841) —
CONFIRMED.** The r5 clauses in the row match the body (jump-set form,
no per-front dichotomy, connected-adiabat H-CVX, mixed-front falsifier);
gamma split correct (singular leg EOS-free except n_m = 0: EOS-general
GIVEN H-CVX, γ(T)-discharged). Attack tried: a claim-above-label leak —
none; the row says RESTATED, not proved (the "proved as written"
defect lives in the class block only, and is prosecuted at ESC2-L0-1).

**C-13. Leg-7 / A-1 (D.2 parenthetical) — CONFIRMED, no regression.**
No "(r5)" marker touches D.2 (grep); the r4-landed judge wording
("i.e. genuinely nonlinear WITH the convex (compressive-shock)
orientation") stands as confirmed by both round-1 lenses; the r5 H-CVX
work correctly cites D.2's closed form rather than editing it.

**C-14. Witness (w1) payload (~1489–1509) — CONFIRMED (modulo the
ESC2-L0-3 certificates).** The a.c.-leg derivation of K ≠ 0 for a field
genuinely φ-dependent off fronts under H-NC + H-WR is the correct and
non-definitional route — exactly what ESC-L0-4 demanded; the kernel
collision is recorded in-statement; "by definition" is gone; the r4
text preserved in quotation.

==============================================================================
## SUMMARY TABLE

| ID | Target (r5 passage) | Class | One-line |
|----|---------------------|-------|----------|
| ESC2-L0-1 | conclusion display + assembly step (3): "Ṽ piecewise-C¹ meridional"; class-block "proved as written" | REPAIR-NEEDED | clause underived; section route hits C¹-Sard (Whitney), front-free-section route yields only C¹ off a closed set without §0-grade curve structure; salvage of the two dependent clauses supplied; third consecutive over-certification |
| ESC2-L0-2 | step (1) blanket trace-continuity sentence | AMENDMENT | false at in-class front crossings (§0's own triple-point shear layers); scope + H²-null insensitivity note needed; argument survives |
| ESC2-L0-3 | (w1) instance certificates ("smooth", "bounded away from 0 and c") | AMENDMENT | refuted by in-document [T-NSW](a)/H-NC record (front-carrying flow; CJ locus attains |w_rel| = c); ESC-L0-4 disposition transcribed a defective round-1 spec; payload survives |
| ESC2-L0-4 | falsifier (a) trigger clause | AMENDMENT | still runs retracted "arc H-CVX" vs "the r4 closure"; misclassifies the detached-branch exhibit as refutation, contradicting its own parenthetical; ESC-4 fix not propagated |

BREAKS-THE-LEG: 0. Total findings: 4 (1 R / 3 A). Discharge verdicts:
ESC-L0-1, ESC-L0-2, ESC-L0-3/ESC-3, ESC-1 DISCHARGED; ESC-2, ESC-L0-4,
ESC-4 PARTIALLY DISCHARGED (residues = ESC2-L0-2/3/4 respectively).
The E-3 escalation is CLOSE to dry on this lens: no false display
survives; what stands between the r5 text and a "second iff proved as
written" adjudication is one underived regularity clause (with its
certification sentence) and three one-to-three-line amendments.

==============================================================================
## SELF-FALSIFIERS (what kills each objection)

- ESC2-L0-1 dies if: (i) a proof of "Ṽ piecewise-C¹ meridional" (§0
  sense) from C¹ fronts alone is exhibited — in particular a structure
  theorem forcing the fully-covered-fiber set S into finitely many C¹
  curves (my tube argument reaches only countable rectifiability; a
  Cantor-parametrized circle family inside one C¹ graph front blocks
  the naive finiteness claim); or (ii) "piecewise-C¹" is shown to be
  DEFINED more weakly for meridional fields somewhere in the document
  (my read of §0 lines 206–209 found one definition, the finite one);
  or (iii) my clause-(iii) salvage is shown circular — e.g. the local
  product structure of int{n_φ = 0} shown insufficient for the
  essential-jump-set curve claim. Partial kill: if the document's
  intended reading of the display clause is the weakened form, the
  finding drops to AMENDMENT (state the weakened clause), but the
  "proved as written" sentence still needs the edit.
- ESC2-L0-2 dies if §0 is shown to exclude front intersections (my
  read found the opposite: lines 216–218 admit triple-point shear
  layers) or if one-sided traces are shown continuous ACROSS
  intersection curves in the declared class (a two-front counterexample
  with distinct sector states refutes that in one line).
- ESC2-L0-3 dies if [T-NSW] is shown (at citation grade, M0) to define
  "the standing RDE wave-frame flow of record" as a SMOOTH object on a
  domain excluding both the detonation front and a CJ neighborhood with
  a uniform |w_rel| − c bound — then the certificates type-check and
  only my reading of "of record" fails.
- ESC2-L0-4 dies if "arc H-CVX" in falsifier (a) is shown to be a
  defined alias that r5 re-bound to the connected-adiabat form (grep
  found the binding retracted in the hypothesis line, and no
  re-binding), or if the detached-branch exhibit is shown NOT to
  satisfy the r4 arc wording vacuously (it does: the quantified arc
  set is empty).
- The Part B confirmations die by exhibiting an error in any recorded
  re-derivation (each reproducible: the F = cl{n_φ≠0} ⊔ int{n_φ=0}
  decomposition; the Cartesian atom density n_φ[V]·H²; the local-graph
  flow-invariance; the six-direction witness table; the connected-
  adiabat monotonicity pin).

Round-2 lens-0 totals: 4 objections (0 B / 1 R / 3 A), 14 passages
CONFIRMED with strongest attacks recorded. Nothing else in the r5 delta
withstood less than the attacks listed.

END — machine summary: {objections: 4, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc2_r2_l0.md}
