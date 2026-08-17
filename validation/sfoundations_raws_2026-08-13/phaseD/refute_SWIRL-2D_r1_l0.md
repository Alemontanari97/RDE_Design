# REFUTATION — SWIRL-2D formalization, Round 1, Lens l0 (functional-analytic rigor)

TARGET: `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
(read in full, all 807 lines). Carrier
`phaseD_meanswirl_symcheck.py` INDEPENDENTLY RE-RUN this window:
OVERALL PASS (C1, C2, C3, C4 x7, R1) reproduced — the machine-verified
legs are as claimed. `n6_swirl_kernel.py` Part B3 inspected (negative
control: general Γ(ψ), h0(ψ) break closure; extra term vanishes at
free vortex). RH-in-rotating-frame pen leg of D.20 independently
re-derived by this refuter (it checks out: m[H] = −Ω r n_θ[p] and
m[Γ] = −r n_θ[p] give [I] = 0) — noted for the record because it
CONFIRMS the author's own THEOREM* labeling, not a finding.

LENS DISCIPLINE: spaces, operators, traces/regularity, every
quantifier, label audit, falsifier rejection power, absence.
Each objection: SEVERITY (P0 = breaks the labeled claim as stated /
P1 = over-label or unproved load-bearing step / P2 = quantifier,
hypothesis-completeness, or falsifier-power defect), anchor lines,
and the repair burden.

VERDICT UP FRONT: **REPAIRABLE**. No core mechanical content dies
(the machine-verified identities, the CV assembly route, the hazard
exhibits all stand), but there are two P1 over-labels on THEOREM-class
items (D.2(ii), D.15's iff), one P1 proof-gap-with-counterexample-
mechanism (D.2(ii) level-set connectedness), one P1 monitor
ill-posedness on its own declared data class (D.14 OBS), a P1
falsifier that cannot actually reject what it claims to test (D.18/C4),
and a family of P2 hypothesis-completeness holes (unsteady-flow
function space in §3; contacts in D.2's front clause; axis distance
in §0; D.9(i) "wherever"; D.19's consequently-overreach).

------------------------------------------------------------------------------
## O1 [P1 — proof gap with counterexample mechanism; over-label]
## D.2(ii) [MS-T-TRANSPORT]: "there exist functions s(ψ), h0(ψ), Γ(ψ)"
Anchor: lines 104–135 (statement (ii), proof line 124–125:
"invariants constant on connected level sets of a C¹ ψ with
∇ψ ≠ 0 (W > 0)").

The proof step is a non sequitur as written. What is proved:
q is constant on each CONNECTED COMPONENT of each level set of ψ.
What is claimed: q = q(ψ), i.e. q single-valued as a function of the
LEVEL. The bridge requires every level set {ψ = c} ∩ G to be
connected, and this is asserted nowhere and does NOT follow from the
stated hypotheses (G simply connected, ψ ∈ C¹, ∇ψ ≠ 0).

Explicit geometric counterexample to the bridge: on the simply
connected strip G = {(x, r): |x| < 2, r₀ < r < r₀ + δ} take
ψ = x² − r. Then ∇ψ = (2x, −1) ≠ 0 everywhere, yet every level
c > −r₀ has a DISCONNECTED trace in G (the parabola r = x² − c has
its vertex below the strip: two arcs, x > 0 and x < 0). Simple
connectivity of G plus absence of critical points does not give
connected level sets — full stop; the cited justification is false
as a lemma.

Worse, the invariance-only conclusion (i) genuinely does not imply
(ii) in this geometry even for SMOOTH fields: levels c ≤ −r₀ are
connected (vertex inside the strip, arcs joined through x = 0),
levels c > −r₀ are disconnected, and near the whole segment x = 0
only connected levels appear. So one may assign s = f₁(ψ) on the
x < 0 branches and s = f₂(ψ) on the x > 0 branches with f₁ ≡ f₂ for
c ≤ −r₀ and f₁ ≠ f₂ for c > −r₀ (C^∞-matched at c = −r₀): the
resulting s field is globally C^∞ on G, constant on every
streamline, and NOT a function of ψ. Whether this field extends to a
full S1 solution of (E1)–(E5) is an existence question (for the
incompressible avatar, ψ = x² − r has constant vorticity Δψ = 2, so
the base flow is a legitimate steady Euler flow; the two-valued
stratification is a Grad–Shafranov-type compatibility question) —
but the burden is on the THEOREM: it quantifies over ALL S1
solutions with W > 0 on simply connected smooth G, so the proof must
EXCLUDE this mechanism, and it currently does not even mention it.

ABSENCE leg: this is the classical caveat of the Bragg–Hawthorne /
Squire–Long reduction (functional dependence H(ψ), Γ(ψ) fails on
level branches not connected to the reference inflow; standard in
the vortex-breakdown literature, e.g. Batchelor §7.5-class
treatments, Keller's columnar-flow analyses). The document cites no
anchor for step (ii) and reproduces the folklore gap verbatim.

Downstream contamination: (iii) (the Bernoulli form
h = h0(ψ) − W²/2 − Γ(ψ)²/2r²) inherits the same gap; D.14's monitor
PRECONDITION (through-flow ρ u_n ≥ δ_tf on the interface, ψ ↦ y
bijective) happens to be exactly the kind of hypothesis that
repairs it — but D.2 is stated on an arbitrary simply connected G,
NOT under the D.14 guard.

REPAIR (named): add to D.2 the hypothesis "every level set of ψ in
G is connected" (equivalently: G is a streamtube region fibered by
its streamlines over a transversal arc — the duct/interface
geometry actually used downstream), or restate (ii) per level-set
component. With the hypothesis, THEOREM is correct; without it, the
label THEOREM is an over-label of record.

------------------------------------------------------------------------------
## O2 [P2 — hypothesis completeness] D.2 front clause: contacts
Anchor: lines 113–118, 126–129.

"[ρ u_n] = 0 and u_n ≠ 0 gives [w] = 0 hence [Γ] = 0": the
u_n ≠ 0 premise appears only inside the proof, never in the
statement, and the S1 class (§0, lines 61–71) admits RH-satisfying
discontinuities with u_n = 0 — contact/slip surfaces, across which
[w] ≠ 0 and [Γ] ≠ 0 are RH-legal (only [p] = 0, [u_n] = 0 are
forced). Steady meridional Euler fields in the piecewise-C¹ class
generically contain slip lines (triple points, merging streams).
The particle-path reading of the theorem survives (particles do not
cross a contact), but the front clause as WRITTEN ("across a
transversal front ... [Γ] = 0") is false on contacts unless
"transversal" is DEFINED to mean u_n ≠ 0 (mass-crossing). If
[C-MAJDA] transversality already excludes characteristic fronts,
the statement must say so explicitly — hypothesis-completeness
defect in a THEOREM. Repair: one sentence ("front with u_n ≠ 0;
contacts carry arbitrary [w] and are handled by the particle-path
clause"). Falsifier of my objection: exhibit the definition of
"transversal" in [C-MAJDA] pinning u_n ≠ 0; then this demotes to a
citation-explicitness nit.

------------------------------------------------------------------------------
## O3 [P1/P2 — missing function space; census exhaustiveness]
## §3 preamble + D.6 + D.8
Anchor: lines 230–236 (§3 setting), 272–304 (D.6 proof), 339–358 (D.8).

(a) [P2] The §3 flow is "the UNSTEADY 3-D inviscid ... flow in the
lab frame" with NO declared function space. §0 declares the S1 class
for per-phase meridional fields and for 3-D WAVE-FRAME (φ-steady)
fields only (lines 67–69). H-AM1 (periodicity) is not a regularity
hypothesis. The D.6 proof needs: ρΓ u and p with well-defined
boundary traces on ∂CV (divergence theorem for a piecewise-smooth
vector field with moving discontinuity hypersurfaces), L(t) finite,
and the RH-cancellation of the moving-front surface terms — i.e. an
unsteady analogue of S1 (piecewise C¹ in (x, t) with finitely many
C¹ front hypersurfaces, fields in L∞, RH in the unsteady weak form).
None of this is stated. The THEOREM* label names ONE conditional
("the assembled symbolic check") and asserts "no physical
conditional remains" (line 304) — but a missing function-space
hypothesis is a mathematical conditional that no symbolic check on
smooth synthetic fields will discharge. Under-declared conditional
inside a starred label = label defect.

(b) [P1] D.8's exhaustiveness ("any breakage must negate a
hypothesis", THEOREM* line 354) inherits (a): a periodicity-
preserving REGULARITY breakdown — energy/momentum concentration on
lip singularities of the faceplate orifices, measure-valued fronts
in the vanishing-viscosity limit, non-integrable corner behavior at
the CV's re-entrant edges — breaks the divergence-theorem step
while negating NONE of H-AM1..H-AM5. That is a fifth channel absent
from the census, and it is not exotic: orifice lips are exactly
where real RDE injector data are least smooth. The census is
exhaustive RELATIVE TO an unstated H-AM0 (regularity/integrability
class). Repair: mint H-AM0 explicitly and re-close the census over
{¬H-AM0, ¬H-AM1..¬H-AM5}; channel (¬H-AM0) is auditable (quadrature
convergence of the flux integrals under grid refinement).

------------------------------------------------------------------------------
## O4 [P2 — quantifier defect inside a THEOREM] D.9(i) "wherever"
Anchor: lines 364–369.

The identity (i) is correct (two-line algebra, verified). The
"Consequently" sentence is not: "zero net flux ... FORCES the plain
time-mean swirl to be nonzero WHEREVER the mass-flux/swirl
covariance is signed" is a POINTWISE claim, but D.6 constrains one
scalar per section (as the very next clause admits). Pointwise,
⟨u_θ⟩ = ⟨u_θ⟩_ṁ − cov/⟨ρ u_x⟩ forces ⟨u_θ⟩ ≠ 0 at a point only
where the pointwise flux-weighted mean ⟨ρ u_x u_θ⟩ vanishes —
which zero AREA-INTEGRATED flux does not give at any single point.
Counterexample: ⟨ρu_x u_θ⟩(r) = cov(r) ≠ 0 pointwise with
∮⟨ρu_x r u_θ⟩ dA = 0 and ⟨u_θ⟩ ≡ 0 is algebraically consistent at
every point where ⟨u_θ⟩_ṁ = cov/⟨ρu_x⟩ — i.e. everywhere, by the
identity itself, whenever ⟨u_θ⟩ ≡ 0; the identity then just SAYS
⟨u_θ⟩_ṁ = cov/⟨ρu_x⟩, and the section constraint is compatible
with that. The sentence contradicts its own trailing hedge. Repair:
replace "wherever the covariance is signed" with the integrated
form: "forces ∮⟨ρu_x⟩⟨Γ⟩ dA = −∮cov(ρu_x, Γ) dA: the plain-mean
swirl weighted by the mean mass flux is pinned to minus the
covariance integral, hence nonzero whenever the SECTION covariance
integral is" (that is what panel F2's A2 ≈ −A3 tests, line 390 —
the falsifier is already the correct integrated object; the prose
overshoots it).

------------------------------------------------------------------------------
## O5 [P1 — monitor ill-posed on its own declared data class] D.14 OBS
Anchor: lines 512–549; data class lines 66–67, 477–479.

The interface data class of record is BV ∩ L∞ in y, "piecewise C¹
sufficient" (jumps allowed — indeed EXPECTED: fill stratification,
parasitic-deflagration h0 spread are the doc's own motivating
examples, lines 495–497, 568–569). On ANY row with a jump,
sup_ψ |dh0/dψ| = +∞ (the distributional derivative has an atom), so
OBS(ξ) = +∞ identically on the very data the monitor exists to
route. Consequences: (a) the license rule "OBS ≤ tol" is vacuous on
in-class data with jumps — the monitor is not a measurement there,
it is a constant; (b) the osc-based spreads Δ_Γ, Δ_h0, Δ_s defined
at lines 512–514 (which ARE finite on BV) are defined and then
NEVER USED by the estimator — dead definitions; (c) the declared
SCHEMA gap (label-scale bound) does not cover this: it concerns
|dψ/dW|, not the sup-vs-TV defect of the h0/Γ/s legs. Sharpening
of the (G-b) gap itself: if dψ/dW is an along-surface derivative,
|dψ/dW| = +∞ at any interior extremum of W(y) (generic data have
one), so the "pending" bound |dψ/dW| ≤ Ψ/W-scale is not an
uncomputed constant, it is FALSE in form; the repair must change
the functional form (integrated/TV pairing), not fill in a number.
REPAIR (named): state OBS in total-variation form,
OBS = [ ∫|dh0'| + ∫|Γ||dΓ'|/y_min² + ∫T|ds'| ] / W_ref²
(TV of the ψ-parametrized rows — finite exactly on BV, reduces to
the sup·Ψ form on C¹ rows by the mean value inequality, and is the
natural pairing for an obstruction that enters INTEGRATED along the
march). Label consequence: as written, "DEFINITION + named SCHEMA
gap" under-declares — the DEFINITION leg itself (the measured
object) is partial (undefined/infinite on declared-class data), a
rejector-discipline (R5) issue since a monitor that returns ∞ on
its target class cannot discriminate.

------------------------------------------------------------------------------
## O6 [P1 — over-label: "machine-verified iff" that is not] D.15
Anchor: lines 551–578, register line 765.

Two defects in the THEOREM label:

(a) "the identity and the iff are machine-verified finite algebra"
(lines 570–571). Inspected: n6_swirl_kernel.py Part B3 verifies the
IDENTITY plus ONE vanishing instance (free vortex) and ONE breaking
instance (general Γ(ψ), h0(ψ)). An "iff over function classes"
(vanishes identically ⟺ Γ' = h0' = 0) is a statement quantified
over all admissible (Γ, h0, s, variations) and cannot be, and was
not, machine-verified as finite algebra. The only-if direction is
proved (if at all) by the prose argument, not the carrier.

(b) The literal iff is FALSE at fixed geometry without the
variation quantifier: the obstruction factor is
h0'(ψ) − Γ(ψ)Γ'(ψ)/y², and on the data surface y = y(ψ) (bijective
under the D.14 guard), the CANCELLATION FAMILY
   Γ(ψ)Γ'(ψ) = y(ψ)² h0'(ψ),  h0' ≢ 0
makes the factor vanish identically ALONG THE SURFACE with neither
Γ' nor h0' zero. (One-parameter solvable ODE family: given any
h0(ψ) and y(ψ), Γ² = Γ₀² + 2∫y²h0' dψ.) The exclusion of this
family requires quantifying over ALL admissible variations — under
variation the map y(ψ) deforms while Γ(ψ), h0(ψ) are transported,
breaking the fine-tuned relation — and THAT argument appears only
as a parenthetical aimed at a different clause ("genericity of
dψ/dW ≠ 0 ... not load-bearing", lines 571–574). For the iff it IS
load-bearing. The headline conclusion (Γ-only monitoring falsely
licenses: Γ ≡ const, h0' ≠ 0 leaves residual h0'·dψ/dW) SURVIVES
this objection untouched; what does not survive as stated is (i)
the "vanishes identically iff Γ' = h0' = 0" sentence, and (ii) the
"TRIPLE is the MINIMAL sufficient spread set" claim, whose
sufficiency direction needs the same explicit quantifier (uniform
triple ⟹ obstruction vanishes for ALL variations — true, but by
the trivial direction; minimality needs the cancellation family
dismissed BY the variation quantifier, in the text). Repair: state
the iff as "for all admissible variations of the surface" and
demote the machine-verified attribution to the identity + the two
B3 controls; then THEOREM is sustainable.

------------------------------------------------------------------------------
## O7 [P1 — falsifier cannot reject what it claims to test] D.18/C4
Anchor: lines 624–654; carrier lines 87–147; register line 768.

The completeness claim ("zero leftover — ONLY ∂_φ terms are
dropped") is tested by C4, and D.18's falsifier says "any
additional term found dropped by the 2.5-D operator (nonzero C4
leftover) refutes ... this is exactly what C4 tests." It is not.
Structural fact (verified by reading the carrier and re-running
it): for five of the seven C4 checks (cont, xmom, rmom, s, h0) the
"exact" row, the "2.5-D" row, and the K term are all built from the
SAME in-file operator (`D`, `Dm`, and K := the ∂_φ part of D by
construction), so row_gap = exact − reduced − K ≡ 0 is an algebraic
tautology of the transcription: those checks CANNOT fail unless the
file itself is mistyped, and in particular they CANNOT detect a
term that the shared operator itself mis-derives or omits (e.g. a
metric term wrong in BOTH the "exact" and "2.5-D" transcriptions
simultaneously). A common-mode transcription error passes C4
silently. The independent content in the carrier is exactly:
C4-gamrow-equiv (field-form Γ row vs an independently written
θ-momentum row), C1–C3 (nontrivial identities), and R1 (which
guards the C1–C3 chain only — corrupting, say, the continuity
metric term would not fire anything). This is the same common-mode
failure class the program has already documented at engine level
([X-O31CS] CS4 negative control: transpose-consistent-but-wrong
passes the self-check) — the ABSENCE finding is that the author
knew this pattern of record and did not apply it here. REPAIR:
derive the "exact" rows INDEPENDENTLY — write unsteady 3-D Euler in
cylindrical divergence form from scratch (independent symbol set,
∂_t → −Ω ∂_φ substitution at the end), and diff THAT against
2.5-D + K; add a rejector that corrupts one metric term in the
continuity/r-momentum transcription and demands a C4-class check
fire. Until then, D.18's "DEFINITION + machine-verified
bookkeeping" over-states: verified is the INTERNAL CONSISTENCY of
one transcription, not the completeness of the K list against the
exact system. (C1–C3 and gamrow-equiv are genuinely verified; the
K-list completeness claim is the part left uncovered.)

------------------------------------------------------------------------------
## O8 [P2 — scope overreach in the "Consequently" bridge] D.19
Anchor: lines 656–677.

The identities (i)–(iii) are machine-verified for the SMOOTH,
FROZEN-COMPOSITION, INVISCID wave-frame flow (and I re-derived them
by hand: correct, including D = D_rel on wave-frame fields). The
bridge sentence — "the per-phase TRIPLE spreads MEASURED BY D.14
are the downstream shadows of EXACTLY the dropped commutator
content" — quantifies over D.14's inputs, which are REAL datasets,
and for those the pumping census is not exhaustive: (a) s and h0
are pumped at fronts and in reaction zones (the doc's own (iii)),
which are NOT commutator content; (b) real chamber data carry
viscous/turbulent and DEFLAGRATIVE h0/s sources entirely outside
the frozen-Euler model in which D.19 is a theorem — the doc itself
uses "parasitic deflagration" as the motivating h0-spread mechanism
(R4.1, line 496), which is a ¬(frozen Euler) source, not a K-term
shadow. Note "reaction zones" (line 663) is itself outside the gas
model of record (frozen composition, §0) — the model in which s
can be pumped by reaction is never declared. So "EXACTLY" is true
only model-internally; as a statement about the monitor's measured
object on data it is PRACTICE-grade interpretation, not part of the
THEOREM. Repair: scope the Consequently paragraph to the model
class ("within frozen-Euler wave-frame flow ...") and add the named
non-model channels (reaction, shear) as the D.20(a) diagnostic
already implicitly does. One-sentence fix; without it the THEOREM
label covers prose it does not prove.

------------------------------------------------------------------------------
## O9 [P2 — falsifier power / wording] D.3
Anchor: lines 148–167.

(a) "det A_p = u³(u² − c²): x-marching invertibility ⟺
u ∉ {0, ±c}" — invertibility of A_p is neither necessary nor
sufficient for a well-posed x-march; marchability additionally
needs all pencil roots real (W > c) and spacelikeness needs u > c
(one-sided Mach cone). D.4 gets this right; D.3(a)'s label
"x-marching invertibility" invites reading the algebraic
invertibility as the marching criterion, which D.5(iii) then has to
warn against. Rename to "symbol invertibility".
(b) "FALSIFIER: re-run of the carrier" — a deterministic re-run of
a passing symbolic check in a pinned environment can never fail;
that is a reproduction, not a rejector. The second clause ("any
algebra system exhibiting a nonzero difference") is the real
falsifier; the re-run clause should be struck or demoted, here and
in D.19/D.20 where the same "carrier re-run" formula appears. R5
requires falsifiers that CAN reject; a re-run of frozen code
cannot. (The R1 rejector inside the carrier is a genuine rejector;
the FALSIFIER lines should point at independent recomputation +
R1-style corruption tests, not at re-running.)

------------------------------------------------------------------------------
## O10 [P2 — domain/axis hypothesis; class definition] §0
Anchor: lines 61–71; D.14 line 517 (y_min).

(a) "bounded Lipschitz meridional domain D ⊂ {(x, r): r > 0}" does
not bound r away from 0 on cl(D): a Lipschitz D ⊂ {r > 0} may have
closure touching the axis, where the sources ρw²/r, −ρvw/r, the
1/y_min² term in OBS, and the Stokes-ψ normalization all degenerate.
Every §1–§2 pointwise statement silently needs inf_cl(D) r > 0
(annular geometry). One hypothesis line fixes it; as stated, the
quantifier "on D ⊂ {r>0}" does not deliver the uniformity the
proofs use. (b) "piecewise C¹" is never defined: the intended
meaning (C¹ off the declared front set, one-sided limits at fronts,
continuous across nothing else) must be stated, else "in smooth
regions" (line 70) is ambiguous about whether non-front
discontinuities are admitted (cf. O2: if they are, contacts are
in-class; if not, say so). This is the root of the O2 ambiguity.

------------------------------------------------------------------------------
## O11 [P2 — unproven rider inside a THEOREM-classed block] D.10
Anchor: lines 404–407.

"the swirl-KE debit E_θ (positive-definite, UNRECOVERABLE as axial
thrust ...)" — positivity is proved; "unrecoverable" is a
thermodynamic/design claim proved nowhere in this document and not
true unconditionally (turning vanes/diffusive recovery are excluded
only by scope, and partial pressure-recovery of swirl KE in a
converging annulus is a known effect). The clause leans on an "N6-2
scope note" citation; if that note proves it, cite it as the
carrier; if it scopes it, the word here must be scoped identically
("unrecoverable within the vaneless axisymmetric nozzle class of
record"). As written, a PRACTICE-grade clause rides inside the
THEOREM sentence. One-line repair.

------------------------------------------------------------------------------
## O12 [P2 — sign hypothesis] D.5(ii)
Anchor: lines 193–205.

∂M_x/∂Γ = +uΓ(dc²/dT)/(2c³r²c_p): the "+" and the conclusion
"M_x nondecreasing in |Γ|" require u > 0 (and the strictness
requires uΓ ≠ 0). u > 0 is implicit in the marching context but
D.5(ii) is stated as a pure state-sensitivity claim at fixed
(h0, s, u, v, r) — for u < 0 the margin FALLS with |Γ|. Add
"u > 0 (through-flow orientation)" to the hypothesis list. The
derivation itself was independently re-checked at this lens
(T = T(h) via h' = c_p > 0; γ' = −R_g c_p'/(c_p−R_g)²; both
displayed formulas correct): the finding is hypothesis
completeness, not truth.

------------------------------------------------------------------------------
## Label audit summary (the over-label table)

| Item | Claimed | This lens says | Why |
|------|---------|----------------|-----|
| D.2 | THEOREM | THEOREM only after added hypothesis (level-set connectedness / streamtube G; u_n ≠ 0 in the front clause) | O1, O2 |
| D.6 | THEOREM* (one named mechanical conditional, "no physical conditional remains") | THEOREM* with TWO named conditionals (add: unsteady function-space hypothesis H-AM0) | O3a |
| D.8 exhaustiveness | THEOREM* | THEOREM* only relative to H-AM0; as stated, not exhaustive | O3b |
| D.9(i) consequence sentence | inside THEOREM | integrated form only; pointwise "wherever" false | O4 |
| D.14 | DEFINITION + named SCHEMA gap | DEFINITION is itself partial on the declared data class (OBS = ∞ on BV jumps); second gap (sup-vs-TV) unnamed; (G-b) bound false in form, not pending | O5 |
| D.15 | THEOREM ("identity and iff machine-verified") | THEOREM only with the explicit all-variations quantifier; "iff machine-verified" retracted (carrier verifies identity + 2 instances) | O6 |
| D.18 | DEFINITION + machine-verified bookkeeping (completeness) | machine-verified = internal consistency of one transcription; completeness UNVERIFIED (common-mode hole, [X-O31CS] pattern) | O7 |
| D.19 Consequently-bridge | inside THEOREM | model-internal only; data-facing reading is PRACTICE | O8 |
| D.10 "unrecoverable" | inside THEOREM sentence | unproven rider; scope or cite | O11 |

Variable-gamma statuses: audited item by item — all CORRECT as
declared (D.5(ii)'s γ(T)-EXACT with AUD-c2T is right, and the
γ=const inheritance claim checks out since dc²/dT = γR_g > 0; the
EOS-GENERAL claims use only dh = Tds + dp/ρ as asserted; no
γ=const-only smuggling found). No finding on this axis.

Falsifier audit: F1–F4/A4 are honest but ALL await a dataset (the
doc itself declares the vacuum, G-e) — acceptable as declared. The
non-rejecting "carrier re-run" falsifiers (D.3/D.18/D.19/D.20) are
the O9(b)/O7 findings. D.16's arming test is a genuine rejector
design. D.14's falsifier (a)-limb is genuine; its (b)-limb depends
on the O5 repair to be evaluable at all on real data.

------------------------------------------------------------------------------
## What survives this round untouched (for the judge's ledger)
- C1/C2/C3/R1 and gamrow-equiv: verified, re-run, and re-derived
  by hand at this lens. D.20 smooth part + front pen leg: correct
  (independently re-derived), THEOREM* honestly labeled.
- D.4 (spacelikeness ⟺ M_x > 1, frame invariance): correct as
  labeled given [T-NSW] (M0:530, checked to exist as THEOREM).
- D.5(iii) total-Mach hazard: exhibit checked (√1.81 = 1.345…),
  conclusion sound.
- D.9(ii) equality of means: proof correct including the n-wave
  period bookkeeping (Ωt_c = 2π/n traversal = one F-period).
- D.10 positivity/unconstrainedness: proofs and exhibit correct.
- Remark 3.1, R4.1 (vacuity), D.13 recovery (uniqueness under
  AUD-c2T — worth ADDING as a stated condition, noted in passing),
  D.12 query-bounded vacuum claim, S.22's honesty about g1–g4.

VERDICT: REPAIRABLE. Nothing here is BROKEN beyond repair; every
objection has a named, bounded fix. But D.2, D.15, D.18 as
currently LABELED do not meet the house THEOREM/machine-verified
bar, D.14's measured object fails on its own declared data class,
and D.6/D.8 carry an undeclared function-space conditional — these
must land before absorption into M0 (§7 targets 1–3 would
otherwise import the over-labels into the document of record).
