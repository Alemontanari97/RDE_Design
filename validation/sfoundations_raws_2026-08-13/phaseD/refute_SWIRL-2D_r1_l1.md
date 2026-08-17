# ADVERSARIAL REFUTATION — SWIRL-2D, round 1, lens 1 (hyperbolic-PDE structure)

TARGET: `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
(read in full). LENS: characteristics, admissibility, front conditions,
symmetry/group-action correctness, physics of the reduction.
STANDARD: SOTA rigor per the binding brief — statement truth, every proof
step, hypothesis completeness, rigor-label accuracy (over-label = finding),
variable-gamma status, falsifier rejection capability, ABSENCE.

METHOD OF THIS ROUND (all evidence measured in-window, nothing inherited):
- Carrier `phaseD_meanswirl_symcheck.py` RE-RUN LIVE: OVERALL PASS
  (C1, C2, C3, C4 x7, R1 fires) — the doc's PASS claim is TRUE.
- `validation/n6_swirl_kernel.py` READ AT SOURCE (Parts A and B3) to audit
  what "machine-verified" actually covers.
- M0 anchors read: [T-NSW] (530–551), the O(St) quasi-steady block
  (368–391), [C-MAJDA] usage; greps for "contact/slip/vortex sheet" in the
  target doc AND M0: ZERO hits (absence claim below is search-proven).
- D.20's front-leg RH algebra, D.5(ii)'s derivative chain, D.3's
  determinants, D.9(ii), R3.1, and the D.1 divergence forms were
  independently re-derived by hand (results in §"CONFIRMED" below).

VERDICT (this round): **REPAIRABLE.** No core theorem falls. But two
HIGH-severity findings (an unproven iff with a degeneracy hole exactly on
the program's own CJ locus; an over-labeled "machine-verified iff"
contradicted by the doc's own falsifier line), two MEDIUM-HIGH absences
(slip lines / weak-strong failure for vortex-sheet data), and a schema
scaling premise that contradicts the document's own O(1) statements.

------------------------------------------------------------------------------
## O-1 [HIGH — D.18, statement truth + hypothesis completeness]
### The clause "K ≡ 0 iff ∂_φ(fields) ≡ 0" is unproven, and its pointwise
### algebraic version is FALSE exactly on the relative-sonic locus |w_rel| = c
### — which M0 itself names as the CJ surface.

D.18 asserts: "The per-phase family solves the exact 3-D wave-frame system
iff K ≡ 0 iff ∂_φ(fields) ≡ 0 (degenerate axisymmetric operation)." The
FIRST iff is C4-covered (machine-verified bookkeeping). The SECOND iff is
neither proved nor machine-checked — and it has a genuine kernel:

Work pointwise with w_rel ≠ 0 (the standing scope). K_u = K_v = K_s = 0
force ∂_φu = ∂_φv = ∂_φs = 0. The remaining rows leave a NONTRIVIAL
one-parameter kernel:

  K_ρ = 0  ⟹  ρ ∂_φw = −w_rel ∂_φρ
  K_Γ = 0  ⟹  ∂_φp = w_rel² ∂_φρ          (substituting K_ρ)
  ∂_φs = 0 ⟹  ∂_φp = c² ∂_φρ              (isentropic φ-variation)

Compatibility: (w_rel² − c²) ∂_φρ = 0. And K_h0 imposes NOTHING new:
with ds = 0, ∂_φh = ∂_φp/ρ = −w_rel ∂_φw, so ∂_φh0 = (w − w_rel)∂_φw
= Ωr ∂_φw, giving K_h0 = Ω w_rel (∂_φw + w_rel ∂_φρ/ρ) = 0 automatically
by K_ρ. Hence: at any point where **w_rel² = c²**, there exist nonzero
φ-variations (∂_φρ free, ∂_φw and ∂_φp slaved as above) annihilating ALL
six K rows. The pointwise implication K = 0 ⟹ ∂_φ = 0 fails there.

This locus is not exotic: M0 [T-NSW](a) (READ, lines 533–539) states "The
relative sonic locus |w| = c attached to the wave IS the Chapman-Jouguet
surface." The kernel elements are azimuthal acoustic disturbances
stationary in the wave frame — lock-in/resonance modes — a structurally
meaningful boundary, not a technicality. In the nozzle domain the scope
plausibly gives |w_rel| > c throughout ([T-NSW](a): hyperbolic where
|w| > c, "the sweep HELPS"), so the repair is cheap, but it must be SAID.

Aggravating: this iff sits inside a block classed DEFINITION ("+
machine-verified bookkeeping"), has no falsifier of its own (the C4
falsifier tests the K-LIST's completeness, not this iff), and no rigor
class. An unlabeled, unproven, and (pointwise) false-as-stated biconditional
inside a DEFINITION is a label-discipline violation on top of the math.

REPAIR: add the hypothesis |w_rel| ≠ c a.e. (no open subset of the
degeneracy locus), citing [T-NSW](a) for in-scope justification; prove the
implication under it (the argument above IS the proof once the locus is
excluded — one paragraph), and give the clause its own class (THEOREM
after repair) and falsifier (the kernel family above is the rejector: it
must satisfy K = 0 symbolically at w_rel² = c² and fail for w_rel² ≠ c²).

------------------------------------------------------------------------------
## O-2 [HIGH — D.15, over-label + internal contradiction]
### "The identity and the iff are machine-verified finite algebra" is an
### over-claim: the carrier verifies the identity and the IF direction only,
### and the doc's own falsifier line admits the ONLY-IF is a SCHEMA.

n6_swirl_kernel.py Part B3 (READ at source, lines 177–194) checks exactly
two things: (a) `extra != 0` as a symbolic expression (the term is not
identically zero — this is NOT a proof that it is nonzero for every
nontrivial profile); (b) substituting h0′ = Γ′ = 0 kills it (the IF
direction). The ONLY-IF direction — vanishing forces Γ′ = h0′ = 0 — is
NOT machine-verified anywhere. D.15's class line claims "the identity and
the iff are machine-verified finite algebra": FALSE as to the only-if.

The document CONTRADICTS ITSELF on this point: D.15's own falsifier says
an alternative reduction "would also discharge the N6-3 strong-only-if
SCHEMA" — i.e. the author knows the strong only-if is SCHEMA-grade
elsewhere, while the class line here books it as machine-verified THEOREM
content.

The only-if also needs a QUANTIFIER the doc never states. The obstruction
term is (h0′(ψ) − Γ(ψ)Γ′(ψ)/y²)·dψ/dW. On a single control surface,
where y = y(ψ) is a fixed curve, the CANCELLATION FAMILY

    h0′(ψ) = Γ(ψ) Γ′(ψ) / y(ψ)²      (choose any Γ; integrate for h0)

makes the obstruction vanish SURFACE-LOCALLY with a non-uniform triple.
"Vanishes identically iff Γ′ = h0′ = 0" is true only when vanishing is
demanded on an OPEN (W, y) set (ψ-level curves sampling a range of y at
fixed ψ, so the 1 and 1/y² powers separate) — an argument absent from the
doc, requiring its own genericity hypothesis on ψ.

WHAT SURVIVES (stated for fairness): the headline false-licensing
conclusion is UNTOUCHED — the exhibit (Γ ≡ const, h0′ ≠ 0) is explicit
and machine-covered; and the D.14 OBS monitor is SAFE against the
cancellation family (it sums absolute values, conservative — it would
BLOCK, not license, on the cancellation family; over-blocking is the
declared design). The defect is the iff's label and quantification, not
the theorem's job.

REPAIR: split D.15 — false-licensing part stays THEOREM (it is); the
minimality/iff clause becomes THEOREM* conditional on the open-set
quantifier + ψ-genericity (or restate with the quantifier and prove the
power-separation step), reconciling with the N6-3 strong-only-if SCHEMA
label the doc itself cites.

------------------------------------------------------------------------------
## O-3 [MEDIUM — D.6/D.7/D.16, statement precision]
### "for every station x, independent of x" is false in the shear-declared
### limb: τ_w,decl is cumulative in x.

τ_w,decl is the wall torque over the wetted surface of the CV from S_inj
to S(x): it GROWS with x for any dissipative dataset. The displayed
balance ⟨∮_{S(x)} ρ u_x Γ dA⟩ = J_inj + τ_w,decl is correct PER CV, but
the gloss "independent of x" holds only in the inviscid limb (τ_w = 0).
As written, the THEOREM*-labeled statement is internally inconsistent for
the H-AM2 shear-declared branch it explicitly includes. Downstream
consequence: D.16's "≥2 stations" audit inherits this — for viscous data
each station carries its OWN cumulative declared budget τ_decl(x), which
the row's definition does not say (it shows a single τ_decl).

REPAIR: write the flux as J_inj + τ_w,decl(x_inj → x), state
station-independence as the inviscid corollary, and index the D.16 budget
per station. No content loss; pure statement repair.

------------------------------------------------------------------------------
## O-4 [MEDIUM — D.9(i) consequence clause, statement truth]
### "zero net flux FORCES the plain time-mean swirl to be nonzero wherever
### the covariance is signed" — non sequitur as a pointwise claim.

D.6 pins ONE scalar per section (the area-integrated flux). Pointwise,
⟨u_θ⟩ = ⟨u_θ⟩_ṁ − cov(ρu_x, u_θ)/⟨ρu_x⟩, and ⟨u_θ⟩_ṁ is NOT pointwise
constrained: at any given point ⟨u_θ⟩_ṁ can equal cov/⟨ρu_x⟩, giving
⟨u_θ⟩ = 0 with cov ≠ 0 — directly contradicting "wherever". The correct
(and provable) statement is INTEGRATED: if ∮ cov(ρu_x, r u_θ) dA ≠ 0
(e.g. single-signed covariance) then, under zero net flux, ⟨u_θ⟩ ≢ 0
SOMEWHERE on the section — because ⟨u_θ⟩ ≡ 0 forces
∮⟨ρu_x⟩⟨r u_θ⟩ dA = 0 = −∮ cov dA. Note the doc's OWN falsifier (F2:
A2 ≈ −A3, integrated quantities) tests the integrated statement, not the
"wherever" prose — the claim overreaches beyond its own falsifier, an R5
smell. The labeled THEOREM (the identity (i)) is fine; the consequence
sentence is the defect.

REPAIR: replace "wherever the mass-flux/swirl covariance is signed" with
"somewhere on any section whose area-integrated covariance is nonzero
(in particular for single-signed covariance)". The final clause ("ONE
scalar per cross-section") already points the right way — the fix makes
the sentence agree with it.

------------------------------------------------------------------------------
## O-5 [MEDIUM — D.2(ii), proof-step gap under THEOREM label]
### Fiber connectedness of ψ is assumed, not proved.

The proof line "invariants constant on connected level sets of a C¹ ψ
with ∇ψ ≠ 0 (W > 0)" silently upgrades to "there exist functions q(ψ)
with q(x,r) = q(ψ(x,r)) on G". That step needs every level set of ψ in G
to be CONNECTED. Simple connectivity of G plus ∇ψ ≠ 0 does NOT give this:
a regular function on a planar simply connected domain can have
disconnected fibers (slit-domain example: G = plane minus a boundary-
reaching ray, ψ = x — fibers {x = c, c ≥ 0} have two components; more
generally, branching arc-foliations with non-Hausdorff leaf space need no
critical point). If a fiber is disconnected, q(ψ) is ill-defined (two
components can carry different invariant values) and (ii) FAILS as
stated. The statement is rescuable — for ψ ∈ C¹ up to a connected
boundary with no interior critical points, disconnected regular fibers
force boundary-trace extrema patterns that force interior critical points
(Poincaré–Hopf on the gradient), and the physical slip-wall/no-source
structure separates ψ-ranges across splitters — but NONE of that argument
is in the proof. A THEOREM label under the binding SOTA standard requires
the lemma or an added hypothesis (e.g. ψ proper with connected level-set
boundary trace; or "G chosen so that ψ-fibers are connected", which is
how the monitor actually uses it via the D.14 bijection precondition).

REPAIR: one lemma or one hypothesis; also note D.14's through-flow guard
already enforces the needed monotonicity ON THE INTERFACE — the gap is
only in the interior-region theorem as stated.

------------------------------------------------------------------------------
## O-6 [MEDIUM-HIGH — D.1/D.2/D.13, ABSENCE: contact discontinuities /
### slip lines are silently excluded and never mentioned]

Search-proven absence: "contact", "slip line", "vortex sheet" have ZERO
hits in the target doc (the only "slip" is wall slip) and ZERO hits in
M0. Yet:

1. The S1 field class admits only TRANSVERSAL (Lax/Majda,
   non-characteristic) fronts. A slip line is a CHARACTERISTIC front
   (u_n = 0, [p] = 0, [w], [Γ], [s], [h0] free) — excluded by fiat.
2. Per-phase RDE fields generically CONTAIN slip surfaces: the
   fill/product interface and the oblique-shock/triple-point shear layer
   are the canonical wave-frame structures; in the steady per-phase
   meridional flow they appear as streamlines carrying jumps in exactly
   the triple (s, h0, Γ) this document is about.
3. The D.13 contract class explicitly admits BV data rows with jumps in
   y. Data with a jump in s or Γ at interior ψ₀ evolves downstream as a
   slip line — a solution OUTSIDE the declared S1 field class. The
   contract admits data the state class cannot carry: a class-adequacy
   inconsistency between §4 and §0, never declared.
4. D.2's front clause ("[Γ] = 0, [h0] = 0") is TRUE only for
   mass-crossing fronts (the proof uses u_n ≠ 0); the contact case —
   [Γ] jumps freely, the triple still transported because particles do
   not cross — is simply missing. For a document whose stated job is
   "what the reduction transports", omitting the one front type across
   which Γ is NOT continuous is a hypothesis-completeness defect.

REPAIR: (a) add the contact clause to D.2 (three lines: u_n = 0 case,
[p] = 0, tangential jumps free, invariants per-side); (b) either extend
the S1 class with finitely many characteristic contact curves (then §2's
symbol analysis is untouched — contacts ride the triple streamline
characteristic — but S.22 g2 must own them, see O-7) or declare
slip-line-free scope EXPLICITLY as a standing limitation with the
routing consequence (the D.14 monitor's BV data may then carry jumps the
evolution class disowns).

------------------------------------------------------------------------------
## O-7 [MEDIUM-HIGH — S.22 gap (g2), ABSENCE: weak-strong uniqueness is
### KNOWN to fail for vortex-sheet data — "not new" mislabels a fatal
### obstruction as a routine conditional]

g2 says front handling in the comparison is "weak-strong beyond
Lipschitz — the standing D2.5 conditional, not new". The literature the
author ignored: for multi-D compressible Euler, relative-entropy /
weak-strong uniqueness FAILS in the presence of contact/vortex-sheet
data — admissible weak solutions are non-unique by convex integration
(Chiodaroli–De Lellis–Kreml-class results; wild solutions for shear-type
initial data; the failure is structural, not a technical gap awaiting
better estimates). If per-phase data contain slip lines (O-6: generic in
scope), the NAMED ROUTE of S.22 (energy/relative-entropy with K as
source) is not "conditional" in that regime — it is known-broken, and no
constant C(m_x, data) exists along that route. The alternatives that DO
exist (fitted-front stability: Majda shocks + Coulombel–Secchi supersonic
vortex sheets, which for 2-D relative Mach > √2·(sound-speed factor) are
only WEAKLY (neutrally) stable, with their own instability windows) are
a different machinery with different hypotheses, and none is cited.

REPAIR: split g2 into (g2a) shocks — standing D2.5 conditional, fair;
(g2b) contacts/slip lines — EITHER excluded by declared scope (then say
so, consistently with O-6) OR handled by fitted-front machinery with the
weak-stability caveat named. As stated, the schema's gap list fails its
own "named gaps" standard: the sharpest known obstruction on its route is
unnamed.

------------------------------------------------------------------------------
## O-8 [MEDIUM — S.22 gap (g3), physics of the reduction: the scaling
### premise contradicts the document's own O(1) statements]

g3 asserts "smallness enters only through the azimuthal-derivative factor
(∂_φ of the fields, O(St) in the sweep scaling)". But:

- Per-phase states differ O(1) across the cycle — THIS DOCUMENT says so
  (D.10/D.12: "per-phase O(1) swirl"; the whole point of phases), and
  φ(ξ) is AFFINE (D.17/D.9(ii)), so ∂_φV = (dξ/dφ)∂_ξV = O(1). The
  azimuthal pressure gradient ∂_φp is the wave's own structure — O(1) at
  minimum near the interface.
- Internal contradiction: D.19 says ∂_φp pumps the TRIPLE spread, and
  D.14's EXPECTATION OF RECORD is that real data will GENERICALLY FAIL
  triple-uniformity — i.e. the pumped spreads are O(1)-significant. If
  ∂_φ fields were uniformly O(St)-small, the D.19-integrated spreads
  would be O(St)-small and the monitor would generically LICENSE. The
  document asserts both. Both cannot hold with St small.
- The M0-consistent resolution (O(St) block, M0 368–391: quasi-steady
  error "exact as St → 0") locates the smallness NOT in ∂_φV but in the
  SWEPT ANGLE PER MERIDIONAL TRANSIT: Δφ_transit ~ (w_rel/r)(L/W) =
  O(St). K is pointwise LARGE (the doc admits this for w_rel but not for
  ∂_φV); the bound can only be nonvacuous in TRANSIT-INTEGRATED
  (Gronwall-along-x, finite domain of dependence under u > c) form,
  where the x-integration contributes the O(St) factor. The chamber
  accumulates many transits (hence O(1) spreads, consistent with D.14's
  expectation); the nozzle march is one short transit (hence O(St)
  error) — that reconciliation is available and is NOT what g3 says.

REPAIR: restate g3 — the small parameter is the swept angle per transit;
the bound must be stated in transit-integrated form with ∂_φ-weighting of
the DATA at the interface, else vacuous or self-contradictory. This is a
schema-internal repair (S.22 is SCHEMA-classed; the finding is that its
named-gap list mis-locates the smallness, which would send the T-RED
owner down a wrong route).

------------------------------------------------------------------------------
## O-9 [LOW — label discipline, falsifier capability, gamma status minors]

(a) D.17 carries NO gamma status and NO falsifier (register row "— / —"),
    violating the doc's own preamble rule ("Every statement carries a
    VARIABLE-GAMMA STATUS and a FALSIFIER"). DEFINITIONs elsewhere in the
    doc (D.1, D.13, D.14, D.16, D.18) all comply; D.17 alone does not.
    Cheap falsifier exists: the ξ ↔ φ identification is refuted by any
    strict-T0 dataset where the time-mean ≠ frozen-t azimuthal mean
    beyond bars (D.9(ii)'s own test doubles for it).
(b) D.12's class "adjudication of record" is OFF the declared house scale
    (THEOREM/THEOREM*/SCHEMA/CONJECTURE/PRACTICE). It functions as
    PRACTICE (a prohibition, rejector = the vacuum falsifier); label it.
(c) D.19(iii) names "reaction zones" as entropy sources — out of the
    frozen-composition gas model of record (§0). Either flag as
    out-of-model physics carried for orientation, or strike.
(d) Carrier rejector coverage is THIN: R1 arms only the C3 chain. C1/C2
    and the C4 family have no dedicated rejector; four of the seven C4
    rows (cont, xmom, rmom, s — and h0 with h0 as free field) are
    chain-rule tautologies whose only failure mode is a K-list
    transcription typo. That IS their declared job (list completeness),
    but "C4 ×7 rows" overstates independent content; the load-bearing
    checks are C1, C2, C3, C4-gamrow-equiv. Cheap upgrade: corrupt one K
    term (e.g. drop ∂_φp from K_Γ) and require C4-gamma to FAIL — one
    more rejector line, arms the bookkeeping claim.
(e) D.5(ii) implicitly assumes u > 0 (sign of ∂M_x/∂Γ flips for u < 0);
    harmless in the M_x > 1 audit context, should be stated.
(f) D.3's "det A_p = u³(u²−c²)" holds for the SPECIFIC normalization in
    the carrier (momentum rows pre-divided by ρ, pressure-row combination
    ρc²·u); for the unnormalized primitive form the determinant carries a
    ρ³ prefactor. Criterion unaffected (ρ bounded away from 0); the doc
    should say "primitive form normalized as in the carrier" for the
    identity to be literally true. Pedantic, but the label is THEOREM.

------------------------------------------------------------------------------
## CONFIRMED UNDER ATTACK (for the loop's record — these held)

- Carrier PASS re-verified live this window (C1–C3, C4×7, R1 fires with
  residual 2·v·w·w_rel/r ≠ 0 — genuinely nonzero, not a simplify
  artifact).
- D.20 front leg re-derived independently: for a wave-steady front with
  s_n = Ωr n_θ, m[h0] = −s_n[p] and m[Γ] = −r n_θ[p] give [I] = [h0] −
  Ω[Γ] = 0 exactly. The pen leg is CORRECT; THEOREM* with the queued
  check is honest (an under-label if anything).
- D.5(ii): ∂T/∂Γ = −Γ/(r²c_p) and ∂M_x/∂Γ = +uΓ(dc²/dT)/(2c³r²c_p)
  re-derived exact, including γ′ = −R_g c_p′/(c_p−R_g)². The
  state-vs-solution scope disclaimer is exemplary R5 practice.
- D.5(iii) exhibit checked: (0.9c, 0, c) gives M_tot = √1.81 ≈ 1.345,
  u < c, W < c. The total-Mach hazard theorem stands.
- D.3(a)/(b) determinants re-checked against the carrier matrices; the
  Γ-independence of the symbol (sources leave the pencil) is correct and
  is the round's soundest structural pillar (it also carries D.4, D.5(i),
  and S.22's "swirl-free machinery applies" clause).
- D.4 frame invariance: correct (u_x and c frame-invariant under uniform
  rotation; Coriolis/centrifugal enter sources only, symbol untouched).
- D.6's local conservation form, wall-torque nullity on surfaces of
  revolution (n_θ = 0), plane-station n_θ = 0, and the H-AM1 cycle-
  average kill of storage: all re-checked, correct. The THEOREM* label
  with the named mechanical promotion task is honest.
- R3.1 (instantaneous balance under strict T0): correct one-liner.
- D.9(ii) equality of the three means under strict T0: correct.
- D.10 positivity and unconstrainedness (equal-mass-flux-halves exhibit):
  correct; the TWIN-B refutation is sound at the stated flux level.
- D.1 divergence-form rows re-checked (r-row source p + ρw², x-row
  sourceless, Γ and H rows conservative): correct.
- Gamma statuses audited line-by-line: every EOS-GENERAL claim indeed
  uses only dh = T ds + dp/ρ with c² free; γ(T)-EXACT flags (D.5(ii),
  s-term of D.14) are correctly placed; no γ=const-only statement hides
  in the document. The gamma-status discipline is CLEAN this round
  (except D.17's missing declaration, O-9a).

------------------------------------------------------------------------------
## ROUND-1 VERDICT

**REPAIRABLE.** The load-bearing structure (symbol Γ-independence, triple
transport, flux nullity, pumping/rothalpy pair, monitor design) survives
adversarial re-derivation. The document must repair: the D.18 iff
(degeneracy at |w_rel| = c — the CJ locus its own M0 names), the D.15
"machine-verified iff" over-label (internal contradiction with its own
N6-3 strong-only-if citation + missing quantifier), D.6's "independent of
x" gloss, D.9(i)'s "wherever" overreach, D.2(ii)'s fiber-connectedness
gap, the slip-line absence (class adequacy + front clause + S.22 g2
mislabel of a known weak-strong failure), and S.22 g3's misplaced small
parameter. None is fatal; all are named with repairs; several are
one-paragraph fixes. An absorption into M0 BEFORE these repairs would
propagate two over-labels (D.15, D.18) into the document of record.
