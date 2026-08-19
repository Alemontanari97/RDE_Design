# ESCALATION REFUTATION — DOC-2 (phaseD_meanswirl_formalization.md) r4
# escalation text, ROUND 1, LENS 1 (gas dynamics / physics, RH algebra,
# counterexamples)

Date: 2026-08-18 (S-FOUNDATIONS-C escalation window). Until-dry round 1
on the r4 REVISION of
`validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
— scope per brief: ONLY the escalation-repair text for leg 6 (D.18,
escalation E-3) and the leg-7 amendment A-1 (D.2 H-CVX), i.e. every
passage carrying an "(r4)" marker plus the passages those markers edit
(header r4 block ~69–96; D.18 recombination display ~1349–1373;
singular-density/Jacobian passage ~1374–1399; FIRST-CLAUSE restatement
~1442–1476; hypothesis line ~1499–1518; L1-4 scope repair ~1544–1558;
case split ~1559–1575; CASE n_m = 0 ~1576–1612; combining ~1613–1618;
class/label block ~1644–1668; falsifier additions ~1686–1703; register
row D.18 ~1955; G-f entry ~1996–2019; §6-quinquies ~2187–2226; D.2
parenthetical ~272–286). Adjudication of record consumed:
`r2pass/VERDICT_r2pass.md` §2.1 rows L0-3/L1-3, L0-4, L0-5, L1-4, L1-5,
L0-6/L1-6 and §4(b)/(c) E-3 spec + A-1; full objection texts
`r2pass/refute_r2batch_l0.md`, `r2pass/refute_r2batch_l1.md` read at the
attacked legs. DEDUP DISCIPLINE: no dispositioned objection re-raised;
prior-round files grep-checked (r3_l0/r3_l1/r4_l0 + both r2pass lenses)
for the component-exhaustiveness and a.e.-bridge attack classes — no
prior coverage found; every finding below targets r4-NEW text or the
r4-touched combining/rider sentences. Attacks are derivation-level only.

SELF-DECLARED STANDARD: every attacked passage = verbatim quote + attack
+ class {BREAKS-THE-LEG, REPAIR-NEEDED, AMENDMENT}; every examined
passage I could not break = CONFIRMED with the strongest attack tried.

==============================================================================
## §1 Discharge audit — do the r4 repairs discharge the sustained
##    objections they answer? (VERDICT_r2pass §4(c) E-3 spec + A-1)

| Sustained obj | E-3/A-1 spec item | r4 delivery | DISCHARGE VERDICT |
|---|---|---|---|
| L0-3 + L1-3 (BREAKS) | restate the first iff: unconditional identity exact = reduced + K + the two true conditionals, or the quantifier prefix | Delivered MORE than spec: identity + conditionals (i)/(ii) + two-of-three rule; prior false display quoted in-statement, never erased; "(bookkeeping, now true)" retracted | DISCHARGED — modulo one rider defect in the two-of-three sentence (ESC-3 below, AMENDMENT; the load-bearing restatement itself survives my strongest attacks, §3.1) |
| L0-4 (REPAIR → J-r2p-3) | write the n_m = 0 case (entropy/admissibility argument) or exclude the stratum by hypothesis | Case WRITTEN via the K_s-atom route (m[s] production atom + arc H-CVX Hugoniot entropy monotonicity) — a legitimate entropy argument per spec, and STRONGER than L0-4's proposed circulation route (no admissibility consumed); price stated honestly (leg no longer blanket EOS-free) | DISCHARGED ON THE NAMED STRATUM — the RH algebra of the new case is verified row-by-row (§3.2). BUT the ⟹ chain's case ASSEMBLY now has a distinct uncovered stratum of its own (ESC-1, REPAIR-NEEDED) and the arc hypothesis admits a vacuous reading (ESC-4, AMENDMENT): the leg-level ⟹ direction is still not complete as written |
| L0-5 (AMENDMENT) | fix the "declared normalization" parenthetical; NAME the measure-normalization Jacobian identity as a G-f check | Parenthetical reworded exactly as the objection specified ("fixed in the G-f computation", defect recorded); Jacobian identity named in the definition, falsifier (c), and the (G-f) gap entry | DISCHARGED (structure of the named identity independently checked, §3.4) |
| L1-4 (AMENDMENT) | scope the atoms-vanish sentence to conservation-form rows | Sentence scoped (mass, momenta, energy); s-row atom taken from the operator identity — exactly what the n_m = 0 case consumes | DISCHARGED (§3.5) |
| L1-5 (AMENDMENT) | state the triangular recombination in the definition and in the G-f rejector spec | All six identities stated IN the definition with the ρ factors on the s/h0 rows (sharper than the objection's gloss, and CORRECT — §3.3); executor rule + one-line sympy checks in falsifier (b) and G-f | DISCHARGED (all six identities verified by direct expansion, §3.3) |
| L0-6 + L1-6 = A-1 | replace the "equivalently: genuinely nonlinear along the arc" parenthetical with "i.e. genuinely nonlinear WITH the convex (compressive-shock) orientation" | Landed VERBATIM per the judge's specified wording; false-equivalence mechanism recorded in-statement; displayed inequality named operative | DISCHARGED (§3.7 — no covert equivalence survives; strongest attack fails) |

Label discipline verified: both iff clauses held at SCHEMA per
J-r2p-2/J-r2p-3 in the class block, the register row, and §6-quinquies;
no self-upgrade; layer-unproven caveat carried in the r4 header and the
ledger residue. §6-quinquies rows match the VERDICT rows 1:1.

==============================================================================
## §2 FINDINGS (4: 1 REPAIR-NEEDED, 3 AMENDMENT, 0 BREAKS-THE-LEG)

------------------------------------------------------------------------------
**ESC-1 — REPAIR-NEEDED: the r4 case assembly is not exhaustive — the
combining step has no case for front points with n_φ = 0 on a component
that is NOT globally φ-invariant; the printed conclusion is true but the
written proof does not reach it.**

Verbatim quote (D.18 proof, the r4 combining step, ~1613–1618):
> "COMBINING the two cases: jumps vanish at every front point with
> n_φ ≠ 0, whether n_m ≠ 0 or n_m = 0. A connected front component with
> n_φ ≡ 0 contains the φ-direction in its tangent space everywhere,
> hence is a union of φ-circles — a φ-INVARIANT (meridional × S¹)
> surface; its one-sided limits are φ-independent by the a.c. leg.
> Degenerate axisymmetric operation follows."

Attack (derivation level). The two written cases are pointwise on
{n_φ ≠ 0} (split by n_m); the third branch is component-wise on
{n_φ ≡ 0}. These do NOT exhaust the front set: a MIXED component —
n_φ ≠ 0 somewhere, but with an interior patch where n_φ = 0 — is
in-class and falls through all three. Explicit in-class instance
(gas-dynamically ordinary, no azimuthal-sheet exotica needed): the C²
graph front x = H(r) + ε χ(φ) with χ ≡ 0 on an open φ-arc and χ′ ≠ 0
elsewhere; its normal ∝ (1, −H′, −εχ′/r) has n_m ≠ 0 EVERYWHERE and
n_φ = 0 exactly on the arc. On the arc-patch interior: case 1 needs
n_φ ≠ 0 — not applicable; case 2 needs n_m = 0 — not applicable; the
n_φ ≡ 0 branch is component-quantified and the component has n_φ ≢ 0 —
not applicable. So NOTHING written forces the jump to vanish there,
while the conclusion display ("every front is either jump-free
(removable) or a φ-INVARIANT (meridional × S¹, n_φ ≡ 0) surface with
φ-independent one-sided limits") asserts a component-level dichotomy
this configuration would violate if the patch carried a jump.

The conclusion is nevertheless TRUE — the gap is closable in-class by an
argument the document does not write (stated here so the repair is a
transcription): fix (x*, r*) with x* just downstream of the patch
position H(r*) and inside the sweep of εχ; the φ-circle through
(x*, r*) meets the front only at transition points where n_φ ≠ 0 (for
a.e. x* the crossings are transversal), where the jumps are ZERO by the
proved cases; between crossings ∂_φV = 0 (a.c. leg) makes V constant on
each arc; hence V is constant on the WHOLE circle, so the patch's
downstream trace equals the upstream state, and letting x* ↓ H(r*)
kills the patch jump. (This is the state-continuity sibling of L0-4's
proposed φ-circle entropy-circulation argument, applied at the n_φ = 0
patches instead of the n_m = 0 sheets.) Points of {n_φ = 0} in the
CLOSURE of {n_φ ≠ 0} close by trace continuity instead.

Why this is a fresh objection and not dedup: L0-4 (dispositioned
FIXED-BY-CASE-WRITTEN) attacked the stratum where the case-1 chain's
n̂ = n_m/|n_m| is 0/0; this attacks the r4-NEW assembly sentence
("COMBINING the two cases ... whether n_m ≠ 0 or n_m = 0" — text that
did not exist before r4) for exhaustiveness over the OTHER uncovered
stratum, int{n_φ = 0} on non-φ-invariant components. Grep of r3_l0,
r3_l1, r4_l0 and both r2pass lenses: no prior coverage.

Class: **REPAIR-NEEDED** (same defect pattern the judge classed REPAIR
for L0-4: a named, recoverable case gap in the ⟹ chain; not a break —
the statement is true and the closing argument is one paragraph from
in-document ingredients). Repair: write the φ-circle argument above as
the n_φ = 0-patch case of the combining step (or restate the conclusion
over the jump set: "the jump set of every front is contained in the
φ-invariant part, with φ-independent one-sided limits"). Consistent with
the leg's SCHEMA holding label; this row should ride the E-3
adjudication.

------------------------------------------------------------------------------
**ESC-2 — AMENDMENT: "jumps vanish at every front point" is concluded
from hypotheses that hold only a.e. on the front; the one-line
a.e.-to-everywhere continuity bridge is consumed unstated.**

Verbatim quotes: (case n_m = 0, ~1582–1584) "mass [g] = 0 with
g := ρ w_rel continuous and ≠ 0 a.e. by the H-WR front-trace reading";
(combining, ~1613–1614) "jumps vanish at EVERY front point with
n_φ ≠ 0, whether n_m ≠ 0 or n_m = 0" (emphasis mine).

Attack. H-WR's front-trace reading delivers w_rel± ≠ 0 only a.e. (front
surface measure); both cases divide by g on the pointwise chain, so the
proved statement is "jumps vanish a.e. on {n_φ ≠ 0}". The pointwise
"every front point" conclusion (which the component dichotomy then
consumes) needs the bridge: one-sided traces of a piecewise-C¹ field
are continuous on the front, {g ≠ 0} ∩ {n_φ ≠ 0} is dense in the open
set {n_φ ≠ 0}, hence jump ≡ 0 on its closure. True, one line, unwritten
— and the r4 combining sentence is where the a.e.-grade input is
silently upgraded to pointwise grade. (The r3 n_m ≠ 0 case carried the
same grain, but the "at every front point" quantifier is the r4
sentence; in-scope.) Class: **AMENDMENT** — write the bridge line where
the combining step consumes it.

------------------------------------------------------------------------------
**ESC-3 — AMENDMENT: the two-of-three rider "each fails in one
direction, with (w1)/(w2) the counterexamples of record" is misleading
as printed and mis-attributes its witnesses.**

Verbatim quote (~1473–1476):
> "equivalently the TWO-OF-THREE RULE: any two of {exact-residual = 0,
> 2.5D-residual = 0, K = 0} imply the third, and NO pairwise
> biconditional holds unconditionally — each fails in one direction,
> with (w1)/(w2) the counterexamples of record."

Attack (two defects, same sentence). (a) "each fails in one direction"
reads naturally as "fails in one direction (and holds in the other)" —
FALSE for all three pairs: ALL SIX pairwise implications fail
unconditionally. Exact ⇏ K = 0 (w1); K = 0 ⇏ exact (any φ-independent
non-solution field: K ≡ 0, exact-residual = 2.5D-residual ≠ 0);
exact ⇏ 2.5D (w1 again); 2.5D ⇏ exact (the document's own example (β):
sections solve, 3-D RH violated); 2.5D ⇏ K = 0 ((β): nonzero front
atom); K = 0 ⇏ 2.5D (the φ-independent non-solution again). Only the
weak reading "fails in AT LEAST one direction" is true, and that reading
is strictly less than what the sentence appears to certify. (b) The
attribution "with (w1)/(w2) the counterexamples of record" is
incomplete: (w1)/(w2) both witness only the directions emanating from
exact = 0; the four remaining failing directions need (β) and the
trivial φ-independent non-solution, neither cited. Class: **AMENDMENT**
— reword to "no pairwise implication among the three holds
unconditionally; witnesses: (w1)/(w2) for the exact-side directions,
(β) and any φ-independent non-solution field for the rest". The
two-of-three rule itself and conditionals (i)/(ii) are correct (checked
against the identity; §3.1) — only the rider sentence is defective.

------------------------------------------------------------------------------
**ESC-4 — AMENDMENT: the arc-H-CVX hypothesis as consumed by the
n_m = 0 closure admits a vacuous reading (detached Hugoniot branch)
under which the "[s] = 0 pins the zero-strength point" step does not
run.**

Verbatim quotes: (hypothesis line, ~1511–1514) "(H-CVX, ARC FORM, as
minted in D.2): on the n_m = 0 front strata the Hugoniot arcs
connecting the one-sided traces lie in the G_fund > 0 region, Hugoniot
well-defined (Menikoff–Plohr weak conditions)."; (closure, ~1598–1604)
"along the Hugoniot through the upstream trace, G_fund > 0 on the arc
makes s STRICTLY MONOTONE in shock strength ... so [s] = 0 pins the
zero-strength point".

Attack. Any RH pair lies on the Hugoniot LOCUS {H(·; upstream) = 0},
but for a non-convex EOS that locus can have a component DETACHED from
the branch through the upstream state (the Menikoff–Plohr
phase-transition regime; note R4-0-adjacent history: the r4_l0 R4-2
text itself records that GLOBAL single-valuedness of the Hugoniot needs
subsidiary conditions — Bethe's Γ_G > −2 — beyond convexity). For a
downstream trace on a detached component there IS no "Hugoniot arc
connecting the one-sided traces": the quantifier "the arcs connecting
the traces lie in the G_fund > 0 region" is then VACUOUSLY satisfied,
strict monotonicity along a connecting arc is available on no arc, and
[s] = 0 pins nothing — an isentropic nontrivial azimuthal sheet on a
detached branch would pass the hypothesis as worded and refute the
closure's conclusion, exactly the quantifier-hole defect class the r2→r3
H-CVX repair itself prosecuted (endpoint vs arc), one notch further out.
NOT dedup of R4-2/V-1 (dispositioned FIXED: endpoint→arc quantification
on connected arcs); this is the existence presupposition of the
connecting arc itself, raised against the r4 REUSE where vacuity first
becomes load-bearing (in D.2 the clause conditions a monotonicity
claim; here it must EXCLUDE a state, so vacuity = failure).
Honest scope: IN-MODEL this is harmless — the γ(T)-exact closed form
G_fund > 1 at every table state makes the shock adiabat globally
p-monotone and connected in range, so no detached branch exists where
the model is defined; the defect is in the EOS-general wording of the
hypothesis. Class: **AMENDMENT** — reword to "the downstream trace lies
on the connected shock adiabat through the upstream trace (existence/
connectedness per the Menikoff–Plohr weak conditions and, where needed,
the Γ_G > −2 single-valuedness condition), with G_fund > 0 at every
state of the segment between the traces", or record the detached-branch
configuration as out-of-hypothesis in the falsifier note. The falsifier
(a) sentence ("a non-convex EOS admitting an isentropic nontrivial jump
is the expected out-of-hypothesis exhibit, not a refutation") already
gestures at this and survives under the reworded hypothesis.

==============================================================================
## §3 CONFIRMED passages (strongest attack tried, each)

**§3.1 FIRST-CLAUSE restatement (~1442–1476), core.** CONFIRMED (minus
the ESC-3 rider). Strongest attacks tried: (i) product-vs-section
subtlety — is "the azimuthal sections solve ... distributionally"
equivalent to 2.5D-residual = 0 as a distribution on D × S¹_φ, given
that n_m = 0 sheets are invisible to sections? Yes: the product
residual's atoms carry density [F_m·n_m], which vanishes identically on
n_m = 0 sheets, so both readings ignore them alike; a.c. parts match by
Fubini; the given of (i) and the conclusion of (ii) are therefore
well-typed and the conditionals follow from the identity in one line
each. (ii) I attempted to break conditional (i) with a field whose
sections solve for a.e. but not every φ — the a.e. granularity is
inherited from the r3 distributional definition, not r4 text, and does
not disturb either conditional. (iii) The retraction bookkeeping
(prior display quoted, not erased; "(bookkeeping, now true)" withdrawn)
matches the judge's annotation-of-record requirement exactly.

**§3.2 CASE n_m = 0 RH algebra (~1576–1612).** CONFIRMED — this is the
escalation's centerpiece and I attacked it hardest, re-deriving every
flux independently:
- azimuthal relative fluxes at n = ±e_φ: mass ρw_rel ✓; x-mom ρuw_rel
  (no pressure term, Π_xφ off-diagonal) ✓; r-mom ρvw_rel ✓; Γ-row
  ρΓw_rel + rp, giving r(g[w] + [p]) with r continuous ✓; energy
  ρw_rel h0 + Ωrp — INDEPENDENTLY VERIFIED from the lab-frame energy
  equation under ∂_t → −Ω∂_φ: F = ρwh0 − Ωr(ρE) = ρw_rel h0 + Ωrp
  using ρE = ρh0 − p ✓.
- [I] = 0 chain: g[h0] = −Ωr[p], g[w] = −[p] ⟹ [h0] = Ωr[w] ⟹
  [h0 − ΩΓ] = 0 ✓; with [u] = [v] = 0 and r continuous,
  w²/2 − Ωrw = w_rel²/2 − Ω²r²/2 gives [h + w_rel²/2] = 0 ✓. The
  system {[ρw_rel] = 0, [ρw_rel² + p] = 0, [h + w_rel²/2] = 0} IS the
  1-D normal-shock RH system — exact, as claimed.
- K_s-atom step: full s-row atom [ρ s u_rel·n] = n_φ g[s] = m[s] ✓
  (production, mass RH consumed); meridional s-part ≡ 0 at n_m = 0 ✓;
  K = 0 ⟹ m[s] = 0 ⟹ [s] = 0 given m ≠ 0 ✓ (a.e. grain → ESC-2).
- Closure: strict s-monotonicity along a G_fund > 0 Hugoniot arc
  (Bethe–Weyl; the base-point third-order tangency [s] ~ (Δp)³ does not
  break STRICT monotonicity through zero strength) pins the trivial
  jump; [w] = [w_rel] via r continuous ✓; [h0] = 0 from the energy row
  ✓. Attack tried and failed: admissibility is NOT needed — any RH
  pair (Lax or not) with [s] = 0 on a convex arc is trivial, which
  makes the route STRONGER than L0-4's circulation proposal. Residual
  exposure is only the connecting-arc presupposition (ESC-4).
- "the sheet is INVISIBLE to the meridional sections — it appears in
  no section as a front curve": correct (n = ±e_φ ⟹ sheet locally in a
  meridional plane; one section contains it as a region, measure zero
  in φ, no section crosses it as a curve).
- The EOS-free-unprovability parenthetical: correct — without
  convexity, Hugoniot–isentrope re-intersection (G sign change) admits
  isentropic nontrivial RH jumps; Menikoff–Plohr class as cited.

**§3.3 Triangular recombination identities (~1349–1373).** CONFIRMED.
All six verified by direct expansion of (1/r)∂_φF_φ,rel:
mass = K_ρ ✓; x: (1/r)∂_φ(ρuw_rel) = K_u + uK_ρ ✓; r likewise ✓;
Γ: (1/r)∂_φ(ρΓw_rel + rp) = K_Γ + ΓK_ρ ✓; s: (1/r)∂_φ(ρsw_rel)
= ρK_s + sK_ρ ✓; h0: (1/r)∂_φ(ρw_rel h0 + Ωrp) = ρK_h0 + h0K_ρ ✓ —
the ρ factors on the per-unit-mass rows are exactly right and sharper
than L1-5's own gloss, as the ledger claims. Strongest attacks tried:
(a) distributional products (coefficients u, v, Γ, h0 are discontinuous
where K_ρ has atoms — the products are ill-defined THERE): fails,
because the identities are stated for the a.c. parts off fronts, where
all factors are C¹, and the atoms are defined once via the div-form —
the text's scoping ("per row, (1/r)∂_φF_φ,rel off fronts") is exactly
the sound scoping; (b) the invertibility line consumes "ρ bounded away
from 0" — piecewise-C¹ ρ with positive one-sided traces on a compact
closure delivers it; and pointwise ρ ≠ 0 already suffices for the
"K = 0 equivalent in the two readings" claim. No defect worth a
finding.

**§3.4 L0-5 repair: normalization parenthetical + named Jacobian
identity (~1374–1393, falsifier (c), G-f entry).** CONFIRMED. The
rewording matches the objection's own specified text; the named
identity (|n_m|·dS-factor = section-curve factor) was checked
structurally: slicing the front by φ, the coarea factor is
dS = r dℓ dφ/|n_m| (|∇^S φ| = |n_m|/r), so |n_m|·dS = r dℓ dφ = the
r-weighted section-curve measure × dφ — the identity is exactly the
right check target, correctly a G-f item rather than a proof here.
Attack tried: does the n_m = 0 case secretly consume the normalization
(where the section-assembled measure degenerates)? No — it consumes
only "atom = 0 ⟹ density = 0", normalization-free.

**§3.5 L1-4 scope repair (~1544–1558).** CONFIRMED. The scoped sentence
quantifies over exactly the five conservation-form rows (mass, three
momenta — angular momentum ρΓ IS a conservation law of the exact
wave-frame system — and energy), where exact-solution atoms vanish;
the s-row atom is routed through the operator identity, valid for
arbitrary piecewise-C¹ fields. Attack tried: is the Γ-row genuinely
conservation-form in the wave frame (no torque source at a shock)? Yes
— the θ-momentum divergence form has no geometric source in the atom
bookkeeping; [F·n] = 0 across exact-solution shocks holds for it.
"the scoped fact is exactly what the new n_m = 0 case consumes" —
verified: the case uses conservation-row RH (n = ±e_φ) plus the s-row
atom, nothing else.

**§3.6 Falsifier additions (a)/(b)/(c) (~1686–1703).** CONFIRMED.
(a) the azimuthal-sheet instance must FAIL distributional K = 0 via the
m[s] atom — sound rejector, and the stated refutation asymmetry
(arc-H-CVX EOS + [s] = 0 nontrivial sheet refutes; non-convex EOS
exhibit does not) is the correct hypothesis-boundary test, modulo the
ESC-4 rewording; (b) executor rule for the recombination identities —
the transcription trap it guards is real (a checker built on advective
rows as div-form parts fails on correct fields; verified against §3.3);
(c) the named Jacobian check — see §3.4.

**§3.7 A-1 / D.2 parenthetical (~272–286).** CONFIRMED. The judge's
specified wording landed verbatim; "i.e." now glosses rather than
asserts equivalence, and the in-statement record names the mechanism
(GN ⟺ G_fund ≠ 0; all-arc BZT EOS genuinely nonlinear yet excluded)
correctly. Strongest attacks tried: (i) does "genuinely nonlinear WITH
the convex (compressive-shock) orientation" still overstate? No — with
the arc quantifier inherited from the host sentence it is exactly
G_fund > 0 on the arc; (ii) "compressive-shock orientation" as a gloss
of G > 0 is the standard convex-EOS admissibility orientation — sound;
(iii) I re-checked the surviving closed form independently via the
(∂T/∂ρ)_s route: G_fund = 1 + (γ−1)(γ + Tγ′)/(2γ) — agrees (this is
now a fourth agreeing pen derivation across the loop's records).

**§3.8 Header r4 block, register row D.18, gamma-status line,
§6-quinquies ledger.** CONFIRMED for internal consistency: sustained-ID
lists match VERDICT §2.1; label bindings (both iff clauses SCHEMA,
J-r2p-2/3, E-3 pending, G-f restoration path) present at all four
sites; gamma status correctly split (singular leg EOS-free EXCEPT the
n_m = 0 case: EOS-general GIVEN arc H-CVX, γ(T)-exact discharged);
layer-unproven / Blocco-2-gate-closed caveat carried in header AND
ledger residue. Attack tried on the γ(T) discharge phrasing
("discharged unconditionally"): the operating-range qualifier lives in
the cited D.2 sentence ("on every Hugoniot arc inside the operating
range") and "in-model" carries it — not elevated to a finding.

==============================================================================
## §4 Summary

| ID | Target (r4 passage) | Class |
|---|---|---|
| ESC-1 | combining step ~1613–1618: no case for int{n_φ = 0} patches on non-φ-invariant components; conclusion true, proof gap; φ-circle repair supplied | **REPAIR-NEEDED** |
| ESC-2 | "at every front point" from a.e.-grade H-WR inputs; continuity bridge unwritten | AMENDMENT |
| ESC-3 | two-of-three rider: "each fails in one direction" misleading; (w1)/(w2) attribution incomplete | AMENDMENT |
| ESC-4 | arc-H-CVX as consumed by the n_m = 0 closure: connecting-arc existence presupposed; detached-branch vacuous reading; in-model harmless | AMENDMENT |

BREAKS-THE-LEG: 0. Total findings: 4. Everything else examined:
CONFIRMED with strongest attack recorded (§3.1–§3.8). Discharge audit:
all six sustained-objection repairs and A-1 LANDED per the E-3 spec;
L0-4's discharge is stratum-complete but the leg's ⟹ direction is not
yet assembly-complete (ESC-1) — consistent with, and a reason for, the
SCHEMA holding labels.

## §5 Self-falsifiers for THIS refutation

- ESC-1 dies if the written text is shown to cover int{n_φ = 0} patches
  of non-φ-invariant components (e.g. a reading of "connected front
  component with n_φ ≡ 0" that quantifies over patches, refuted by the
  text's own "connected front component" wording), or if the mixed
  graph front x = H(r) + εχ(φ), χ ≡ 0 on an arc, is shown out-of-class
  under §0's front declaration (judge act (v) found no such exclusion).
- ESC-2 dies if H-WR's front-trace reading is shown to hold pointwise
  (not a.e.) on every front in the declared class, or if the
  a.e.-to-everywhere bridge is located verbatim in the r4 text.
- ESC-3 dies if "each fails in one direction" is shown to be the
  intended and unambiguous weak reading AND some cited witness covers
  the K = 0 ⇏ exact and 2.5D = 0 ⇏ exact directions.
- ESC-4 dies if the Menikoff–Plohr weak conditions are shown (at
  citation grade) to exclude detached Hugoniot branches without the
  Γ_G > −2 subsidiary condition, making the connecting arc's existence
  automatic under the hypothesis as worded.
- The §3 confirmations die by exhibiting an error in any of my
  re-derivations (each is reproducible: the six recombination
  expansions, the energy-flux identity ρwh0 − Ωr·ρE = ρw_rel h0 + Ωrp,
  the [I] = 0 chain, the coarea factor |∇^S φ| = |n_m|/r, the G_fund
  closed form).

END — machine summary: {objections: 4, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc2_r1_l1.md}
