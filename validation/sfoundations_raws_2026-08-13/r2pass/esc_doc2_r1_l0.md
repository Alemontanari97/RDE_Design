# ESCALATION REFUTATION — DOC-2 (phaseD_meanswirl_formalization.md), ROUND 1, LENS 0
# (hyperbolic-systems / functional-analytic rigor)

Date: 2026-08-18 (S-FOUNDATIONS-C escalation window, until-dry round 1).
TARGET: the r4 escalation-repair text ONLY — E-3 (leg 6, Definition D.18:
restated FIRST CLAUSE, n_m = 0 singular-leg case, L0-5/L1-4/L1-5 amendment
landings, G-f spec additions, class/gamma/falsifier updates, §6-quinquies
ledger) and A-1 (leg 7, D.2 H-CVX parenthetical). Marked "(r4)" per the
revision log; verified against `r2pass/VERDICT_r2pass.md` §2.1/§4(b)/§4(c)
and the full objection texts `r2pass/refute_r2batch_l0.md` (L0-3..L0-6),
`r2pass/refute_r2batch_l1.md` (L1-3..L1-6).

DEDUP RULE APPLIED: no objection below re-raises a dispositioned finding
unless the disposition itself fails; each finding states its novelty. All
quotes verified verbatim against the r4 file (grep + line read).

MANDATE CHECK (discharge verification, per the brief): for each of the
eight sustained IDs answered by r4 I verified (a) the judge's §4(c) repair
spec item, (b) the landed text, (c) the ledger row. Results are folded into
the findings and the CONFIRMED register below.

==============================================================================
## PART A — OBJECTIONS (4 findings: 1 BREAKS-THE-LEG, 1 REPAIR-NEEDED, 2 AMENDMENT)

------------------------------------------------------------------------------
**ESC-L0-1 — BREAKS-THE-LEG. The r4-completed SECOND IFF is still FALSE in
the ⟹ direction as printed: the per-front dichotomy of the conclusion
display is refuted by an in-class MIXED front, and the r4 "COMBINING"
bridge plus the r4 completeness claim do not deliver it.**

Verbatim quotes (the attacked r4 passages, with the conclusion display they
claim to establish):

> "COMBINING the two cases: jumps vanish at every front point with
> n_φ ≠ 0, whether n_m ≠ 0 or n_m = 0. A connected front component with
> n_φ ≡ 0 contains the φ-direction in its tangent space everywhere, hence
> is a union of φ-circles — a φ-INVARIANT (meridional × S¹) surface; its
> one-sided limits are φ-independent by the a.c. leg. Degenerate
> axisymmetric operation follows."

> "the second iff's proof is complete AS WRITTEN under H-NC + H-WR (+ arc
> H-CVX on the n_m = 0 strata, r4)"

establishing (conclusion display, D.18):

> "K = 0 AS A DISTRIBUTION iff the operation is DEGENERATE AXISYMMETRIC
> (r3 conclusion, strengthened and made true): all fields φ-independent
> off fronts, AND every front is either jump-free (removable) or a
> φ-INVARIANT (meridional × S¹, n_φ ≡ 0) surface with φ-independent
> one-sided limits."

Derivation-level attack. The r4 pass proves a PER-POINT statement (jumps
vanish at every front point with n_φ ≠ 0 — I re-derived both cases and
confirm them, see Part B) and then leaps to a PER-FRONT dichotomy
quantified over the declared front hypersurfaces. The leap is false on an
in-class witness:

WITNESS (mixed front). Declared front F = one connected C¹ wave-steady
hypersurface, parametrized (s, φ) ↦ (X, R)(s, φ) with (X, R)(s, φ) = C(s)
for s ≤ s₁ (φ-invariant portion) and (X, R)(s, φ) = C(s) + δ(s)η(φ) for
s > s₁, δ ∈ C¹, δ(s₁) = δ′(s₁) = 0, δ > 0 beyond, η nonconstant — helical
(n_φ ≠ 0) wherever δη′ ≠ 0. Field V: φ-independent everywhere; a genuine
meridional shock (meridional RH satisfied pointwise, strength tapering
C⁰-to-zero at the ends — the standard shock-tip geometry) across
C′ × S¹ ⊂ {s ≤ s₁} interior; V C¹ across all of F ∖ (C′ × S¹). Hypothesis
check: H-NC/H-WR satisfiable (generic w_rel bounded away from 0 and c up
to traces); arc H-CVX moot (the jumping stratum has n_m ≠ 0, and the
γ(T)-exact closure discharges it anyway). Then: V solves the exact 3-D
system distributionally (2.5-D solution, φ-independent, meridional RH on
the essential set); K = 0 as a distribution — a.c. parts vanish (all
∂_φF_φ,rel = 0), front atoms vanish (n_φ[F_φ,rel]: the jump is zero
wherever n_φ ≠ 0, and n_φ = 0 wherever the jump is nonzero). LHS of the
iff TRUE. RHS FALSE: the single connected declared front F is NEITHER
jump-free (it carries the C′ × S¹ jump) NOR a φ-invariant n_φ ≡ 0 surface
(it is helical over the δη′ ≠ 0 zone). The ⟹ direction of the printed
biconditional fails.

The reading fork, prosecuted both ways: (READING 1, declared fronts — the
document's own: the dichotomy's "jump-free (removable)" branch only makes
sense for DECLARED surfaces, since a component of the essential
discontinuity set is never jump-free; §0 makes fronts class data) — the
statement is a false mathematical display, exactly the L0-3 severity class
of this pass ("the display of record is a false mathematical statement:
BREAKS", VERDICT_r2pass §2.1, even when "repair is a one-line
restatement"). (READING 2, fronts = components of the essential
discontinuity set) — the statement becomes true but the written proof has
a hole the r4 bridge does not close: the "connected front component with
n_φ ≡ 0" sentence covers only PURE components; for an essential component
carried by a MIXED declared front (the witness's C′ × S¹, a
surface-with-boundary), the needed lemma is that the φ-circle through an
essential point stays in the essential set — provable (sketch: if the
circle exits the front, the front sweeps a one-sided meridional zone as φ
varies; V is continuous across the swept helical crossings by the
per-point result, forcing the two adjacent regions' φ-independent values
to agree on the swept zone, which propagates by trace continuity to kill
the jump — contradiction), but appearing NOWHERE in the document. On
either reading the r4 completeness claim ("complete AS WRITTEN") is
refuted. Classed BREAKS-THE-LEG by the pass's own precedent (false printed
display + attached completeness certification); the repair is in reach:
restate the dichotomy over the essential discontinuity set (with the
jump-free branch dropped as vacuous there) or per-point, AND write the
circle-invariance step; alternatively quantify the dichotomy per front
POINT. Note honestly: labels are already held at SCHEMA per J-r2p-3, so no
label motion is implied — but the E-3 escalation cannot be adjudicated
"second iff now fully proved" while this stands.

NOVELTY / DEDUP: no prior round (r1_l0..r4_l0, N1-N9, V-1..V-5,
L0-*/L1-*) raises mixed fronts or the per-front vs per-point
quantification; the r2pass lenses confirmed the n_φ ≡ 0-component branch
for PURE components only (refute_r2batch_l1.md leg-6 confirmation half),
and L0-4 attacked a different stratum (n_m = 0). The L0-4 disposition
itself is NOT re-raised — its discharge is verified in Part B; this is a
new defect in the combined bridge.

------------------------------------------------------------------------------
**ESC-L0-2 — REPAIR-NEEDED. The stale provenance tag "(r3 conclusion,
strengthened and made true)" survives the r4 repair unannotated, and "made
true" is refuted EOS-generally by the r4 text's own pricing.**

Verbatim quote:

> "K = 0 AS A DISTRIBUTION iff the operation is DEGENERATE
> AXISYMMETRIC (r3 conclusion, strengthened and made true)"

Attack. The r4 pass rewrote the hypothesis chain immediately upstream
(inserting arc H-CVX) and priced, in its own words, "EOS-FREE this closure
is UNPROVABLE: without a convexity/admissibility ingredient an ISENTROPIC
nontrivial jump satisfying the mass/momentum/energy RH is not excluded."
That pricing does not merely make the r3 conclusion unproven — it makes it
FALSE as an EOS-general statement at the same construction grade as the
document's own examples (α)/(β): for a Menikoff–Plohr non-convex EOS
admitting an isentropic nontrivial normal-shock pair, mount the pair as a
locally azimuthal sheet with per-side φ-independent states (locally, the
same grade at which (α) mounts "two constant states across a helical
front"): all conservation-row atoms vanish (full RH minus zero meridional
part), the s-row atom is m[s] = 0, the a.c. parts vanish — K = 0 with a
nontrivial n_φ = ±1 front, i.e., NOT degenerate axisymmetric. So without
the r4 hypothesis the r3 conclusion display is false, and "made true" —
an r3 self-certification sitting directly on the display the r4 escalation
repaired — needed an r4 annotation of record under the document's own
annotate-never-erase discipline (compare: the "(bookkeeping, now true)"
certification was explicitly retracted in-statement at r4; this twin tag
was left standing). Repair: annotate the tag "(r3; superseded r4 — true
only under the r4 hypothesis line incl. arc H-CVX on n_m = 0 strata)".
Classed REPAIR-NEEDED rather than AMENDMENT because the tag is a standing
truth-certification on a display that is false without the r4 hypothesis —
the same defect species (miscertification in-statement) the pass just
prosecuted at L0-3, though here the certified statement is at least true
under the full r4 hypothesis set modulo ESC-L0-1.

NOVELTY: no prior ID touches the provenance tag; the r4 revision header
and ledger retract the r3 completeness FRAME but not this in-display tag.

------------------------------------------------------------------------------
**ESC-L0-3 — AMENDMENT. The two-of-three rule's direction-count gloss is
false and its witness citation does not cover the {2.5D-residual, K} pair.**

Verbatim quote (r4 restated first clause):

> "equivalently the TWO-OF-THREE RULE: any two of
> {exact-residual = 0, 2.5D-residual = 0, K = 0} imply the third,
> and NO pairwise biconditional holds unconditionally — each fails
> in one direction, with (w1)/(w2) the counterexamples of record."

Attack, at derivation level. The rule itself is true (trivial from the
per-row operator identity), and "NO pairwise biconditional holds
unconditionally" is true. But: (a) "each fails in one direction" is false
on the natural reading (one direction fails, the other holds): ALL THREE
pairwise biconditionals fail in BOTH directions — A⟺B (A = exact = 0,
B = reduced = 0): A⟹B fails by (w1), B⟹A fails by example (β) (sections
solve, K ≠ 0 front atom, exact = K ≠ 0); A⟺C: A⟹C fails by (w1), C⟹A
fails by any φ-independent smooth field NOT solving the 2.5-D system
(K = 0 trivially, exact = reduced ≠ 0); B⟺C: B⟹C fails by (β), C⟹B by
the same φ-independent non-solution. (b) The citation "(w1)/(w2) the
counterexamples of record" cannot certify the B⟺C failure at all: at both
(w1) and (w2) the conjuncts B and C are BOTH false, so B⟺C is SATISFIED
at those instances; the on-file witness for B⟺C is (β) (and the trivial
φ-independent non-solution for the converse), neither cited. Repair: one
sentence — "each pairwise biconditional fails in both directions;
witnesses (w1)/(w2) for the pairs anchored at exact = 0, example (β) and
any φ-independent non-solution for the {2.5D, K} pair."

NOVELTY: the two-of-three sentence is r4-minted; no prior coverage.

------------------------------------------------------------------------------
**ESC-L0-4 — AMENDMENT. Witness (w1) is quantified "any" with a false
"by definition" certification; the document's own w_rel = 0 kernel refutes
the definitional claim.**

Verbatim quote (r4 restatement block):

> "(w1) any smooth genuinely φ-dependent exact wave-frame solution — the
> document's CENTRAL OBJECT — has K ≠ 0 by definition of the a.c. rows,
> LHS true, RHS conjunct false"

Attack. "By definition of the a.c. rows" is false: K ≠ 0 for φ-dependent
fields is NOT definitional — it is precisely the nontrivial content of the
second iff, valid only under H-NC + H-WR. The document's OWN second kernel
family (recorded in the same definition, r2): on any open subset of
{w_rel = 0}, K_ρ = K_u = K_v = K_s = 0 identically, K_Γ = 0 forces only
∂_φp = 0, and ∂_φρ, ∂_φu, ∂_φv, ∂_φs remain ALL free — a genuinely
φ-dependent smooth field with every displayed row (and every div-form flux
∂_φF_φ,rel: ρw_rel, ρuw_rel, ρvw_rel, ρww_rel + p, ρsw_rel, ρw_rel h0 +
Ωrp all φ-independent there) vanishing. Whether such pointwise kernels
integrate to exact SOLUTIONS on open sets is unsettled in-document (the
r-momentum obstruction kills the pure co-rotation column, but the general
case is exactly what the iff adjudicates), so the universally quantified
(w1) is uncertified as printed — while a single witness suffices for the
restatement's purpose and (w2) alone already carries it. Repair: "e.g. the
standing RDE wave-frame flow (w_rel bounded away from 0 and c, [T-NSW])"
in place of "any ... by definition of the a.c. rows". (The l1 original had
"e.g."; the r4 transcription strengthened it into a false universal.)

NOVELTY: r4-minted sentence; the kernel family it collides with was
absorbed at r2 (N-1) but never confronted with (w1), which did not exist
then.

==============================================================================
## PART B — CONFIRMED passages (strongest attack tried, each)

**B-1. The six triangular recombination identities (L1-5 landing) —
CONFIRMED.** Strongest attack: full independent re-derivation of all six.
(1/r)∂_φ(ρw_rel) = K_ρ; (1/r)∂_φ(ρuw_rel) = K_u + uK_ρ (likewise v);
(1/r)∂_φ(ρw_rel Γ + rp) = K_Γ + ΓK_ρ; (1/r)∂_φ(ρsw_rel) = ρK_s + sK_ρ;
(1/r)∂_φ(ρw_rel h0 + Ωrp) = ρK_h0 + h0K_ρ — all CHECK, including the ρ
factors on the per-unit-mass s/h0 rows (the "sharper than the objection's
gloss" claim is TRUE: l1's gloss wrote "(u, v, Γ, h0)·K_rho" without the ρ
factors). Secondary attack: "ρ bounded away from 0" — holds in the
piecewise-C¹ class on cl(D) (min > 0 per closed piece); invertibility and
the K = 0 equivalence of the two readings follow. Judge spec E-3 item
"state the recombination in the definition and in the G-f rejector spec":
BOTH landed (definition display + falsifier item (b) with the executor
rule). L1-5 DISCHARGED.

**B-2. The n_m = 0 case's RH system — CONFIRMED.** Strongest attack:
independent re-derivation of every row from the −Ω∂_t → flux absorption.
Energy flux: −Ω∂_θ(ρE) + ∇·(ρuH) = 0 gives θ-flux ρwh0 − Ωrρ(h0 − p/ρ)
= ρw_rel h0 + Ωrp — matches; g[h0] + Ωr[p] = 0 with the θ-row
g[w] + [p] = 0 gives [I] = 0, and with [u] = [v] = 0, [Ω²r²/2] = 0 the
rothalpy reads [h + w_rel²/2] = 0 — CHECK; with [g] = 0 and
[ρw_rel² + p] = 0 this is exactly the 1-D normal-shock RH in
(ρ, w_rel, p). Secondary attack (tangency points where n_m = 0 is isolated
and the "sheet is INVISIBLE to the sections" motivation fails): the
argument is pointwise algebra on the exact RH at n = ±e_φ and never
consumes invisibility — holds at isolated tangencies too. The a.e.→
everywhere step ([u] = 0 a.e. from g ≠ 0 a.e. under the H-WR front-trace
reading) closes by trace continuity of piecewise-C¹ fields.

**B-3. The K_s-atom argument (K = 0 forces [s] = 0 on the stratum) —
CONFIRMED.** Strongest attack: basis-dependence of the atom (displayed
per-unit-mass K_s vs div-form s-row). The div-form s-row atom is
n_φ[gs] = g[s] (g continuous by the mass row), = ±m[s]; the meridional
s-part vanishes identically at n_m = 0, so the K-atom equals the FULL
production atom exactly as claimed, and K = 0 ⟹ m[s] = 0 ⟹ [s] = 0
(m ≠ 0). Consistent with the L1-4-scoped conservation-row sentence, which
the s row correctly bypasses via the operator identity.

**B-4. The arc H-CVX closure ([s] = 0 pins the trivial jump) —
CONFIRMED.** Strongest attacks tried: (i) two-branch monotonicity through
the Hugoniot center — under G_fund > 0 on the arc + M-P weak conditions,
ds/dp ≥ 0 along the Hugoniot vanishing only at the center (cubic contact
s − s₀ ~ G(Δp)³), strict monotonicity through zero strength follows; the
expansion branch has s < s₀ strictly, so [s] = 0 pins Δ = 0 on either
branch. (ii) Connectedness presupposition of "the Hugoniot arcs connecting
the one-sided traces" — absorbed by "Hugoniot well-defined (Menikoff–Plohr
weak conditions)", the identical package D.2 consumes, which survived two
adversarial lenses at r2pass leg 7; any residual doubt belongs to the D.2
package, not to the r4 delta. (iii) Operating-range caveat on the γ(T)
discharge — inherited verbatim from the confirmed D.2 discharge with the
same pricing; no new exposure. The honest EOS-pricing sentence ("EOS-FREE
this closure is UNPROVABLE") is correct — Menikoff–Plohr's non-convex
class supplies the isentropic-jump obstruction.

**B-5. L0-4 discharge adequacy — CONFIRMED (the r4 route is SHARPER than
the objection's own).** L0-4's suggested entropy-circulation argument
consumes Lax admissibility of the azimuthal sheets ("consumes the class's
Lax/H-CVX admissibility"), which the exact-solution class does not impose
— it would fail on non-admissible in-class jumps. The r4 K_s-atom +
Hugoniot-monotonicity route needs NO admissibility (monotonicity along the
Hugoniot is admissibility-free), only arc H-CVX, honestly priced in the
hypothesis line, gamma status, register row, and header. The judge's
either/or (write the case or exclude the stratum) is met on the stronger
horn, with the exclusion option correctly rejected (it would gut the
azimuthal-normal-dominated detonation front of record). DISCHARGED.

**B-6. The restated first clause: operator identity + conditionals
(i)/(ii) — CONFIRMED.** Strongest attack: the section-wise vs
global-distributional gap ("the sections solve" vs "reduced-residual = 0
on D × S¹"). For piecewise-C¹ fields the 2.5-D residual is (function off
fronts) + (section-curve atoms); φ-disintegration is licit (the residual
contains no ∂_φ), a.e.-φ upgrades to every section by per-piece
continuity, and locally azimuthal sheets generate NO meridional atoms
(their normal has n_x = n_r = 0), so the two readings coincide — both
conditionals follow from exact = reduced + K by substitution. The
retraction mechanics (prior display quoted, "(bookkeeping, now true)"
retracted in-statement, never erased; grep confirms no stale uncontested
copy of the phrase) match the judge's E-3 spec exactly. L0-3/L1-3
DISCHARGED as to the restatement itself (the two glosses attacked in
ESC-L0-3/ESC-L0-4 are defects in the new text's certifications, not in the
identity or the conditionals).

**B-7. L0-5 landing — CONFIRMED.** The parenthetical now reads "FIXED IN
THE G-f COMPUTATION" with the defect recorded (grep: "declared
surface-measure" survives only inside the defect annotation and the ledger
row); the Jacobian identity (|n_m| · dS-factor = section-curve factor) is
named in the definition, falsifier item (c), and the (G-f) gap entry —
all three anchors verified. Strongest attack: the singular leg CONSUMES
the deferred cancellation identity (n_m ≠ 0 case), so deferral could
under-price the second iff — but the Class line prices exactly this ("the
singular-density row-by-row bookkeeping, including the r4-named
measure-normalization Jacobian identity, rides G-f at the same grade") and
both iff clauses are held at SCHEMA per J-r2p-2/3: no claim above
certification status. DISCHARGED.

**B-8. L1-4 landing — CONFIRMED.** The vanish-sentence is scoped to
conservation-form rows; the s-row atom is taken from the operator
identity; the scoped fact is exactly what the n_m = 0 case consumes.
Strongest attack: whether K = 0 forces atoms and a.c. parts separately —
yes (function + surface measure are mutually singular). DISCHARGED.

**B-9. A-1 landing in D.2 — CONFIRMED.** The parenthetical now reads
"i.e. genuinely nonlinear WITH the convex (compressive-shock)
orientation", explicitly demoted to a gloss with the displayed inequality
named operative and the false-equivalence mechanism recorded in-statement
— matching VERDICT_r2pass A-1 verbatim. Strongest attack: is the new gloss
itself exactly G_fund > 0? "GN with the convex orientation" is the
standard reading of G_fund > 0 for both acoustic families, and the text
forecloses the attack by declaring the inequality, not the gloss,
operative. Grep: no stale "equivalently"-form copy anywhere (the two other
hits are the r3-repaired H-FIB and S.22 items, already dispositioned).
L0-6/L1-6 DISCHARGED.

**B-10. G-f falsifier additions (a)/(b)/(c) — CONFIRMED.** (a) the
azimuthal-sheet instance fires on the in-model γ(T) EOS (nontrivial shock
⟹ m[s] > 0 ⟹ K ≠ 0) and its refutation/out-of-hypothesis split is
logically correct (arc-H-CVX EOS with an isentropic nontrivial sheet
refutes; a non-convex isentropic jump does not); (b) carries the executor
rule; (c) names the Jacobian check. Strongest attack: none survived — the
spec items are well-posed rejectors, queued not executed, consistent with
the commit-gated carrier discipline and honestly declared in the ledger
residue paragraph.

**B-11. §6-quinquies ledger + header + register row — CONFIRMED.** All
eight sustained IDs for legs 6/7 have rows matching the judge's verdicts
and severities; out-of-scope sustained IDs (legs 3/5/14/17) are named with
owners, not consumed; the D.18 register row, gamma line, Class line, and
r4 header all carry the SCHEMA holds (J-r2p-2/3), the escalation-pending
status, and the §1 seed-layer gate language ("nothing in this revision may
be cited as layer-certified"; Blocco-2 gate CLOSED propagated to §7).
Strongest attack: hunting a self-upgrade or a gate leak — none found.

==============================================================================
## SUMMARY TABLE

| ID | Target (r4 passage) | Class | One-line |
|----|---------------------|-------|----------|
| ESC-L0-1 | second-iff COMBINING bridge + conclusion dichotomy + "complete AS WRITTEN" | BREAKS-THE-LEG | per-front dichotomy false on in-class mixed front; per-point result proven, per-front leap unclosed on either reading |
| ESC-L0-2 | "(r3 conclusion, strengthened and made true)" tag | REPAIR-NEEDED | stale truth-certification; "made true" refuted EOS-generally by r4's own pricing; needs annotation of record |
| ESC-L0-3 | two-of-three rule gloss | AMENDMENT | biconditionals fail in BOTH directions; (w1)/(w2) cannot witness the {2.5D, K} pair |
| ESC-L0-4 | witness (w1) | AMENDMENT | false universal + false "by definition"; collides with the document's own w_rel = 0 kernel |

Discharge verdicts on the eight answered IDs: L0-3/L1-3 DISCHARGED
(restatement; two new glosses defective per ESC-L0-3/4); L0-4 DISCHARGED
(case written, sharper route, honestly priced); L0-5, L1-4, L1-5
DISCHARGED; L0-6/L1-6 (A-1) DISCHARGED. The E-3 escalation as a whole is
NOT yet closable: ESC-L0-1 stands between the r4 text and any "second iff
fully proved" adjudication.

==============================================================================
## SELF-FALSIFIERS (what kills each objection)

- ESC-L0-1 dies if: (i) an in-class exclusion of mixed declared fronts is
  exhibited in §0/§5 (e.g., a requirement that declared fronts be jump-
  carrying a.e. or that the front set be the essential discontinuity set —
  my read of §0 lines 139-162 and the conclusion's own "jump-free
  (removable)" branch found the opposite); or (ii) the witness fails —
  e.g., a proof that a tapering meridional shock with a C¹ mixed carrier
  violates piecewise-C¹ or wave-steadiness; or (iii) the circle-invariance
  lemma is shown to already follow verbatim from a passage I missed.
- ESC-L0-2 dies if "made true" is shown to have been scoped, at r3, to a
  hypothesis set under which the display was already true (it was not:
  the r3 hypothesis line had no H-CVX and the r4 text itself prices the
  EOS-free closure as unprovable), or if the isentropic-sheet construction
  is shown out-of-class at the grade at which (α) is in-class.
- ESC-L0-3 dies if a reading of "each fails in one direction" is exhibited
  under which the sentence is true AND (w1)/(w2) witness all three pairs —
  in particular a derivation that B⟺C is refuted AT (w1) or (w2)
  (impossible: both conjuncts are false there, the biconditional holds).
- ESC-L0-4 dies if K ≠ 0 is derived for EVERY genuinely φ-dependent smooth
  exact solution WITHOUT H-NC/H-WR — i.e., a proof that the w_rel = 0
  kernel family admits no exact-solution realization on any open set (that
  proof would itself be new content the document does not contain).

Round-1 lens-0 totals: 4 objections (1 B / 1 R / 2 A), 11 passages
CONFIRMED with strongest attacks recorded. Nothing else in the r4 delta
withstood less than the attacks listed.
