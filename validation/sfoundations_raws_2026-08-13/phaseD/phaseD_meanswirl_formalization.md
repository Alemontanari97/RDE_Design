# Phase D — The per-phase steady axisymmetric-with-swirl (2.5-D) state
# model: formalization of record (landing draft)

STATUS: S-FOUNDATIONS Phase D raw (R35 chain, written 2026-08-17
window; untracked advisory-class until absorption). This document is
the LANDING DRAFT of the mean-swirl panel verdict
(`validation/ADVISORY_mean_swirl_panel_2026-08-11.md`, judge statement
of record P1–P5), which was never landed verbatim in M0. Absorption
targets are listed in §7. INPUTS OF RECORD: the panel advisory (read
in full); M0 `docs/rde_nozzle_MASTER.md` — [T-SLRW] transverse
companion (~511–527), [T-NSW] (530–551), T-T3-MAP clause (c) swirl
accounting (722–775), PROTOCOL T3-CONTROL input (5) (777–825), VI.1
CycleFamily (1371–1380), D2.3 [D-MU], D2.4 [D-CONTRACT], D2.5 [D-S1];
`docs/rde_nozzle_N6_swirl.md` §§1–5 with carriers
`validation/n6_swirl_kernel.py` (PASS 16/16),
`validation/n6_fivefield_adjoint.py` (PASS 6/6).

NEW CARRIER (this document, executed this window):
`validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_symcheck.py`
— sympy 1.14.0 (pinned env, nothing installed), OVERALL PASS
(C1, C2, C3, C4 ×7 rows, rejector R1 fires on a corrupted geometric
coupling). It machine-verifies the §5 reduction-residual identities.

REVISION r1 (2026-08-17, this window): the round-1 refutations
(`refute_SWIRL-2D_r1_l0.md`, `refute_SWIRL-2D_r1_l1.md`) are
APPLIED IN PLACE. Repairs, downgrades and newly named gaps are
marked "(r1)" at the point of change; the per-objection disposition
ledger is §6-bis. Nothing was silently dropped: every objection is
either fixed at full rigor, honestly label-downgraded, or a named
gap with owner.

REVISION r2 (2026-08-17, this window): the ROUND-2 objection list
(R3-1..R3-7b, N-1..N-6, raised against the r1 text) is APPLIED IN
PLACE. Changes are marked "(r2)" at the point of change; the
per-objection disposition ledger is §6-ter. All thirteen objections
were fixable at full rigor in-document (several by minting the
hypothesis/convention the proof already consumed); no rigor label
was lowered this round and no new named gap was needed — the G-f
rejector SPEC was extended (H-WR kernel instance, N-1) within the
existing gap. [r3 CORRECTION OF RECORD, R4-0: "the ROUND-2
objection list" here denotes the two ABSORBED files only
(`refute_SWIRL-2D_r3_l0.md` R3-1..R3-7b, `refute_SWIRL-2D_r2_l1.md`
N-1..N-6); the on-file `refute_SWIRL-2D_r2_l0.md` (N1-N9, raised
against r1, on disk BEFORE this revision) was cited by NO ledger
and its non-coincident objections remained LIVE in the r2 text —
this paragraph's completeness frame was false as a file-level
claim. Consumed at r3, §6-quater.]

REVISION r3 (2026-08-17, this window): TWO absorption debts cleared
in one pass. (1) THIS ROUND's refutations —
`refute_SWIRL-2D_r3_l1.md` (V-1..V-5 + orchestration finding,
first round against the r2 text) and `refute_SWIRL-2D_r4_l0.md`
(R4-0..R4-5) — APPLIED IN PLACE, marked "(r3)". (2) The PENDING
round-2 lens-0 refutation `refute_SWIRL-2D_r2_l0.md` (N1-N9,
raised against r1, never before cited by any ledger — the R4-0
audit-integrity finding) is hereby CONSUMED: each objection
applied, coincidence-landed, or dispositioned, marked "(r3, N*)".
The combined per-objection disposition ledger is §6-quater; prior
false-completeness claims are corrected IN PLACE BY ANNOTATION,
never erased (audit trail preserved). This round DOES lower one
claim where honesty requires it (D.14's "the FORM is no longer
the gap" RETRACTED — G-b split into two legs) and extends the
named-gap inventory (G-f rejector spec extended twice: front
instance, K_h0 elimination check). The §7 absorption pass is now
UNBLOCKED: no on-file refutation of this document remains
unconsumed (measured this window: r1_l0, r1_l1, r2_l0, r2_l1,
r3_l0, r3_l1, r4_l0 — all cited by §6-bis/§6-ter/§6-quater).

LABEL DISCIPLINE: statement labels `MS-*` below are DOCUMENT-LOCAL.
Registry/glossary minting happens at absorption (token-baseline
ratchet, lint (xxiii)); existing tokens (H-AM1..H-AM5, [T-SLRW],
[T-NSW], [T-N6-1/2/3], [S-5F], TWIN-A/B/C, C1 census guard) are
REUSED, never re-minted.

RIGOR CLASSES (house scale, R5): THEOREM = complete proof here or
machine-verified finite identity; THEOREM* = complete modulo named,
cited conditionals; SCHEMA = proof route with named gaps;
CONJECTURE; PRACTICE = operational rule, rejector-gated. Every
statement carries a VARIABLE-GAMMA STATUS and a FALSIFIER.

------------------------------------------------------------------------------
## §0 Standing conventions, gas model, function spaces

NOTATION. Meridional coordinates (x, r), r > 0; azimuth θ (lab),
φ := θ − Ω t (wave frame), Ω = wave angular velocity, n = wave count.
Absolute velocity components (u, v, w) = (u_x, u_r, u_θ); meridional
speed W := (u² + v²)^{1/2}; swirl invariant Γ := r w. Phase label
ξ ∈ Ξ with operating measure μ (D2.3 [D-MU], pushforward of
normalized cycle time). Interface Γ_d per D2.4 [D-CONTRACT], a fixed
axisymmetric surface with arc/radial coordinate y and radius R(y);
N6 usage y = radius on the control surface is retained. ψ = Stokes
stream function (dψ = ρ u r dr − ρ v r dx), normalized throughput
Ψ := ψ_max − ψ_min per phase. Cycle mean at a fixed lab point:
⟨f⟩ := (1/t_c)∫₀^{t_c} f dt, t_c = cycle period; for n IDENTICAL
waves (the Z_n scope of record, D.9(ii)) t_c = 2π/(nΩ) at every
fixed lab point — for UNEQUAL waves the period is 2π/Ω, so this
pin CARRIES the Z_n hypothesis (r3, V-5a: D.9(ii)'s r2 proof cited
this formula to §0, where it was never stated — a dangling anchor
carrying real content, now pinned here).

GAS MODEL OF RECORD (user scope pin 2026-08-11, M0 Lemma A thermal
pin): frozen-composition, thermally perfect mixture — p = ρ R_g T
with fixed R_g, h = h(T) with h′(T) = c_p(T) > 0 (table-backed,
S11 backend), γ(T) := c_p/(c_p − R_g), c² = (∂p/∂ρ)_s = γ(T) R_g T.
TWO FINITE TABLE AUDITS OF RECORD (r2 — previously consumed
unstated, an under-declaration):
 (AUD-cp) c_p(T) > R_g on the operating range (equivalently
   c_v = c_p − R_g > 0, γ > 1). Consumed by: the definition of
   γ(T) (nonzero denominator), c² > 0, AUD-c2T's denominator
   (c_p − R_g)² in γ′, and the H-CVX closed form of D.2 (r2). A
   finite audit of the AUD-c2T family, same table sweep.
 (AUD-hRANGE) every state-recovery step that INVERTS h = h(T)
   (D.5(ii) via T(h), D.13 recovery) carries the existence
   condition h ∈ h(range of the table): on BOUNDED tables
   invertibility (h′ = c_p > 0) does not give existence, and the
   recovery rejector must FLAG an out-of-range h, never
   extrapolate.
STATUS RULE: statements marked EOS-GENERAL use only dh = T ds + dp/ρ
(and c² as a free positive symbol) and hold beyond the pinned class;
statements marked γ(T)-EXACT use the thermally perfect closure;
γ=const-ONLY statements would have to say so — NONE below is
γ=const-only (Lemma-B territory is not used in this document).
FOURTH STATUS, defined at r3 (N9a — "EOS-FREE" has been carried by
register rows and statement bodies since r1 without a definition,
violating this document's own label discipline): EOS-FREE = the
statement consumes NO thermodynamic relation at all — not even the
Gibbs relation dh = T ds + dp/ρ — only kinematics, mass/momentum
conservation-form bookkeeping and geometry; STRICTLY STRONGER than
EOS-GENERAL (which consumes Gibbs).

FUNCTION-SPACE SETTING. Per-phase fields live in the S1 class (D2.5
[D-S1]): V = (ρ, u, v, w, p) piecewise C¹ on the closure of a
bounded Lipschitz meridional domain D ⊂ {(x, r): r > 0} with
  (H-ANN) inf_{cl(D)} r =: r_min > 0   (annular geometry — r1
  repair: "D ⊂ {r > 0}" alone does not bound r away from the axis
  on cl(D), and the sources ρw²/r, −ρvw/r, the 1/y_min² OBS term
  and the Stokes-ψ normalization all need the uniform bound; every
  pointwise statement of §§1–2 uses H-ANN),
and with a DECLARED front set consisting of (r1 definition —
"piecewise C¹" was previously undefined, root of the contact
ambiguity): finitely many C¹ curves, off which V is C¹ with
one-sided limits at each curve, and NO other discontinuities. Front
curves are of two admitted types:
 (T-fronts) MASS-CROSSING transversal fronts, u_n ≠ 0: RH holds
   with Lax/Majda transversality per [C-MAJDA] ("transversal" is
   hereby PINNED to mean u_n ≠ 0, mass-crossing);
 (C-fronts) CONTACT/SLIP curves, u_n = 0 (characteristic): RH
   forces only [p] = 0, u_n = 0; tangential jumps [w], [Γ], [s],
   [h0] are FREE. (r1 ABSENCE repair: per-phase RDE fields
   generically contain slip surfaces — fill/product interfaces,
   triple-point shear layers — and the D.13 BV data class admits
   rows whose evolution IS a slip line; the class now carries them
   explicitly. §2's symbol analysis is untouched — contacts ride
   the triple streamline characteristic — but the comparison
   theorem must own them: S.22 (g2b).)
ρ, p, T bounded away from 0. Interface data rows are BV ∩ L∞ in y
(piecewise C¹ sufficient for all monitors). 3-D wave-frame fields
(§5) are the same class on D × S¹_φ, fronts = finitely many C¹
hypersurfaces steady in φ (both types admitted). Whenever a
pointwise identity is asserted "in smooth regions", it is asserted
on the open complement of the front set; front behavior is stated
separately, per type.

------------------------------------------------------------------------------
## §1 The per-phase 2.5-D system

### Definition D.1 [MS-DEF-STATE] (per-phase 2.5-D state model)
For each phase ξ, the per-phase state is a steady axisymmetric-with-
swirl (2.5-D) Euler field V(·;ξ) = (ρ, u, v, w, p)(x, r; ξ) on
D(ξ), solving, in smooth regions,

  (E1) continuity   ∂_x(r ρ u) + ∂_r(r ρ v) = 0
  (E2) x-momentum   ρ(u ∂_x + v ∂_r)u + ∂_x p = 0
  (E3) r-momentum   ρ(u ∂_x + v ∂_r)v + ∂_r p = ρ w²/r
  (E4) θ-momentum   ρ(u ∂_x + v ∂_r)w + ρ v w/r = 0
  (E5) entropy      (u ∂_x + v ∂_r)s = 0

with the γ(T)-exact thermodynamic closure of §0, RH across fronts
(the θ-row jump is continuity of the mass-weighted Γ flux), slip on
walls, and interface data on Γ_d in the contract class of §4.
Conservation (divergence) form of record, used by the finite-volume
/ MOC unit processes and by the CV balances of §3:

  ∂_x(r ρ u) + ∂_r(r ρ v) = 0
  ∂_x(r(ρu² + p)) + ∂_r(r ρ u v) = p·0 + 0        (x-row, no source)
  ∂_x(r ρ u v) + ∂_r(r(ρv² + p)) = p + ρ w²       (r-row sources)
  ∂_x(r ρ u Γ) + ∂_r(r ρ v Γ) = 0                 (angular momentum)
  ∂_x(r ρ u H) + ∂_r(r ρ v H) = 0,  H := h + (u²+v²+w²)/2 =: h0.

Class: DEFINITION. Gamma status: system EOS-general; closure pinned
γ(T)-exact. Falsifier (consistency): the advective and divergence
forms must be algebraically equivalent under (E1) — a symbolic check
(θ-row instance already PASS: carrier check C4-gamrow-equiv).

### Theorem D.2 [MS-T-TRANSPORT] (triple transport; stream-function form)
Let V be an S1 solution of (E1)–(E5) with W > 0 in a simply
connected smooth region G, and assume additionally
 (H-FIB) every level set of ψ in G is CONNECTED. STATED SUFFICIENT
 FORM OF RECORD (r3, N7 — TWO defects inside the r1 wording are
 repaired here: (α) the r1 "equivalently" asserted an unproven
 converse — connected fibers ⟹ existence of a single global C¹
 transversal needs properness/completeness of the leaves (a
 non-proper leaf accumulating on the boundary admits no continuous
 global transversal), an argument never given and never classed;
 nothing downstream uses the converse, so it is DROPPED and
 replaced by a sufficiency; (β) the r1 clause "the D.14
 through-flow guard ... delivers H-FIB there" was a non sequitur
 as quantified — interface monotonicity of ψ says nothing about
 level sets in the INTERIOR of G without a reachability bridge;
 note also that fronts re-open the closed-streamline case that
 simple connectivity kills in the smooth setting, since the
 ∇ψ ≠ 0 argument on the enclosed disc fails if the disc meets a
 front):
  (H-REACH, sufficient for H-FIB) G is the STREAMTUBE OF Γ_d —
  every streamline of G meets Γ_d exactly once. Then Γ_d itself
  is the global transversal, the D.14 through-flow guard makes
  ψ ↦ y strictly monotone along it, and every ψ-level set of G is
  the single streamline through its unique interface point:
  H-FIB holds. H-REACH is what every downstream consumer (D.14's
  ψ-parametrization, N6-3) actually uses, and it is auditable
  (streamline census from the interface).
Then:
 (i) along meridional streamlines, the TRIPLE (s, h0, Γ) is
     invariant: (u∂_x + v∂_r)q = 0 for q ∈ {s, h0, Γ};
 (ii) with ψ the Stokes stream function, there exist functions
     s(ψ), h0(ψ), Γ(ψ) with q(x, r) = q(ψ(x, r)) on G. WITHOUT
     H-FIB only the per-component statement holds — q constant on
     each connected component of each level set — and a globally
     C^∞ streamline invariant that is NOT a function of ψ is
     constructible (r1: simple connectivity + ∇ψ ≠ 0 do NOT give
     connected fibers; explicit mechanism ψ = x² − r on a thin
     strip, every level c > −r₀ has two components; this is the
     classical Bragg–Hawthorne / Squire–Long caveat, previously
     unstated here);
 (iii) the meridional Bernoulli relation holds pointwise on G under
     H-FIB: h = h0(ψ) − W²/2 − Γ(ψ)²/(2 r²).
FRONT CLAUSES (per front type of §0 — the u_n ≠ 0 premise is part
of the STATEMENT, r1 repair). Across a MASS-CROSSING front
(u_n ≠ 0) steady in the meridional plane, RH transports (h0, Γ)
continuously along the mass flux ([ρ u_n] = 0 ⟹ [h0] = 0 from the
energy flux, [Γ] = 0 from the θ-row with n_θ = 0), while s jumps
upward across a compressive Lax front UNDER
 (H-CVX, r2; r3 ARC REWORD) Bethe–Weyl convexity of the EOS ALONG
 THE CONNECTING HUGONIOT ARC: the fundamental derivative
 G_fund := 1 + ρ(∂c/∂ρ)_s/c is > 0 at every state of the Hugoniot
 locus joining the two end states (equivalently: the front's wave
 family is genuinely nonlinear along the connecting arc), with
 the Hugoniot well-defined there (Menikoff–Plohr weak
 conditions).
 r2 REPAIR OF RECORD: entropy monotonicity across Lax fronts is
 NOT EOS-general — for a free EOS with dh = T ds + dp/ρ it can
 FAIL (Menikoff–Plohr anomalous region, G_fund < 0, is an
 in-class counterexample, and this theorem's own falsifier would
 have rejected the r1 label); the previous blanket EOS-GENERAL
 status silently consumed H-CVX.
 r3 REPAIR OF RECORD (R4-2/V-1, the SAME defect found
 independently by both lenses — repair adequacy of the r2 mint):
 the r2 wording "G_fund > 0 on the states crossed" quantified at
 the two END states only; but finite-amplitude entropy
 monotonicity is controlled by G_fund at the RUNNING state along
 the shock adiabat (Bethe 1942 / Weyl 1949; Menikoff–Plohr, Rev.
 Mod. Phys. 61 (1989)): an EOS convex at both endpoints
 straddling an anomalous G_fund < 0 pocket on the arc (van der
 Waals / BZT composite-wave regime) admits RH-satisfying fronts
 obeying the Lax inequalities with [s] < 0 — there Lax
 admissibility decouples from the entropy criterion and the
 Oleinik/Liu E-condition replaces it. The endpoint wording was
 therefore still under-hypothesized and ITS OWN falsifier fires
 on it; the arc wording is the consumed package's actual
 hypothesis. CROSSING-DIRECTION CONVENTIONS (r3, V-1 secondary —
 previously undefined): s is monotone ALONG THE MASS FLUX ([s]
 means downstream-of-the-mass-flux value minus upstream);
 "compressive" means [p] > 0 in that SAME direction. For the
 γ(T)-exact closure of record H-CVX is DISCHARGED in closed form:
   G_fund = 1 + (γ − 1)(γ + Tγ′)/(2γ) > 1,
 since γ + Tγ′ = (dc²/dT)/R_g > 0 under AUD-c2T (D.5) and γ > 1
 under AUD-cp (§0) — and the closed form holds at EVERY table
 state, hence on every Hugoniot arc inside the operating range:
 the arc condition is FREE in-model (r3). Closed form
 machine-checked this window (round-2 refuter record) and
 INDEPENDENTLY re-derived at pen grade TWICE this loop (r3_l1
 evidence block, isentrope route; r4_l0 no-objection block,
 (∂T/∂ρ)_s route — both agree); the carrier-grade independent
 recomputation remains queued with the G-f window per the
 commit-gated carrier discipline.
The triple is invariant along particle paths EXCEPT s
across mass-crossing fronts, which is monotone under H-CVX
(unconditionally in the γ(T)-exact closure). Across a CONTACT
(u_n = 0): only [p] = 0 is forced; [w], [Γ], [s], [h0] are FREE.
Particles do not cross a contact, so (i) holds per side; under
H-FIB the functions s(ψ), h0(ψ), Γ(ψ) of (ii) remain single-valued
in ψ but carry a JUMP at the contact's ψ-value (BV in ψ rather
than C¹) — the contact is a ψ-level, not a ψ-crossing.
 (r2 hypothesis-completeness repair: the BV-in-ψ statement lives
 on the UNION G⁻ ∪ C ∪ G⁺ across the contact, while (ii) and
 H-FIB were declared only on smooth front-free G — two consumed
 facts are now stated. (a) ψ EXISTS SINGLE-VALUED and IS
 CONTINUOUS ACROSS C, and across every front. FULL ARGUMENT OF
 RECORD (r3, R4-4/V-2 — the r2 line "ρ, u, v ∈ L∞ makes ψ
 Lipschitz on cl(D)" was a non sequitur as printed: boundedness
 of the 1-form bounds the gradient of a primitive IF one exists;
 EXISTENCE is a separate claim, and a field violating mass-RH on
 one curve keeps every L∞ bound while ψ jumps across it —
 the printed premise could not carry the conclusion):
  (1) CLOSEDNESS: the 1-form ω := ρ u r dr − ρ v r dx is closed
  DISTRIBUTIONALLY on D — in smooth regions this is (E1); across
  every admitted front it is the mass RH row [ρ u_n] = 0 (both
  front types). Weak (E1) including the mass-RH row is hereby
  INVOKED — true in-class, previously consumed unstated.
  (2) PERIODS: §0 declares D only bounded Lipschitz, never simply
  connected; on a multiply connected D (a meridional section with
  an internal island — strut/pylon — is the realizable instance)
  a closed 1-form admits a primitive only if its periods vanish.
  The period of ω around any internal boundary component equals
  the net mass flux through an encircling curve, which vanishes
  by wall impermeability (u·n = 0 on the island boundary) + weak
  (E1). Hence a single-valued primitive ψ exists on D.
  (3) REGULARITY: ω ∈ L∞ gives ψ ∈ W^{1,∞}(D); a bounded
  Lipschitz domain is QUASICONVEX (internal path metric
  comparable to Euclidean distance — a real property of the
  declared geometry class, silently used at r2, now stated), so
  W^{1,∞}(D) ↪ C^{0,1}(cl(D)): ψ is Lipschitz on cl(D), hence
  continuous across every front curve.
 The contact (u_n = 0) is moreover a single ψ-level curve. (b)
 H-FIB ON THE UNION: whenever the region contains contacts, H-FIB
 is hereby READ on G⁻ ∪ C ∪ G⁺ — every level set of ψ in the
 union is connected — which is the hypothesis the BV-in-ψ clause
 actually consumes.)
PROOF. (i): computed directly from (E4) (r3, V-5b: a dangling
unfinished clause that did not parse is deleted — the computation
below is the whole step): (u∂_x+v∂_r)(rw) = r[(u∂_x+v∂_r)w] + w v =
r(−vw/r) + wv = 0. (E5) is (i) for s. For h0: expand using
(E2)–(E4) and dh = T ds + dp/ρ with (E5): (u∂_x+v∂_r)h0 =
(1/ρ)(u∂_x+v∂_r)p + u(−p_x/ρ) + v(−p_r/ρ + w²/r) + w(−vw/r) = 0.
(ii): (E1) gives ψ; streamlines are level sets of ψ; invariants are
constant on each CONNECTED COMPONENT of a level set (∇ψ ≠ 0 by
W > 0 and H-ANN); H-FIB makes the level-to-value assignment
single-valued — this is exactly where H-FIB is load-bearing, and
without it the bridge fails (see the mechanism in (ii)).
(iii): definition of h0 with w = Γ/r. Mass-crossing front algebra:
the θ-row jump is [ρ u_n w] = 0, which with [ρ u_n] = 0 and
u_n ≠ 0 gives [w] = 0 hence [Γ] = 0. Contact algebra: with
u_n = 0 on both sides, mass and tangential-momentum rows read
0 = 0; normal momentum forces [p] = 0 only. QED.
Class: THEOREM (with H-FIB explicit; r1 of record: the previous
statement — no H-FIB, contacts unmentioned — was an over-label).
Gamma status (r2 split — the blanket EOS-GENERAL was false for one
clause): (i)–(iii), the mass-crossing (h0, Γ) transport and the
contact clause are EOS-GENERAL (only dh = T ds + dp/ρ used); the
s-MONOTONICITY clause is EOS-general only GIVEN H-CVX, and holds
γ(T)-EXACT unconditionally (H-CVX discharged by AUD-c2T + AUD-cp,
closed form above). Machine
anchor: the transport structure is the triple root of the N6-1(b)
pencil (machine-verified, n6_swirl_kernel.py Part A).
FALSIFIER: exhibit an S1 solution of (E1)–(E5) with W > 0, H-ANN
and H-FIB, and non-constant s, h0 or Γ along a smooth streamline
segment; or a symbolic counterexample to the mass-crossing front
algebra within RH + n_θ = 0 + u_n ≠ 0; or an in-class contact
carrying [p] ≠ 0; or (r3) an EOS instance satisfying ARC H-CVX
with a Lax front carrying [s] < 0 in the mass-flux direction
(would refute the s-monotonicity clause under its stated
hypothesis — NOTE OF RECORD: endpoint-convex/arc-anomalous BZT
instances are IN-hypothesis for the r2 endpoint wording and OUT
for the r3 arc wording; that asymmetry is the test that the r3
repair changed content, not words), or an independent
recomputation of the G_fund closed form exhibiting a nonzero
difference (executed at pen grade twice this loop, both AGREE;
carrier-grade execution queued, G-f).

REMARK 1.1 (what "2.5-D" means of record). The model is the
azimuthally-invariant (∂_φ ≡ 0) section of the 3-D wave-frame flow
carrying the FULL three-component velocity: swirl enters fluxes only
through its own transport row and geometry only through the sources
ρw²/r and −ρvw/r (N6-1, machine-verified). It is NOT a two-component
model with w = 0 (that is TWIN-A, §3), and NOT the 3-D model (§5
names exactly what is dropped).

------------------------------------------------------------------------------
## §2 Characteristic structure and the spacelikeness margin WITH swirl

### Theorem D.3 [MS-T-CHAR] (characteristic structure; Γ leaves the symbol)
For the quasi-linear primitive form A_p ∂_x V + B_p ∂_r V = S(V, r)
of (E1)–(E5), V = (ρ, u, v, w, p):
 (a) det A_p = u³(u² − c²) (primitive form NORMALIZED AS IN THE
     CARRIER: momentum rows pre-divided by ρ, pressure row the
     ρc²·u combination; the unnormalized primitive form carries a
     ρ³ prefactor — immaterial for the criterion since ρ is
     bounded away from 0, but stated so the identity is literally
     true — r1): SYMBOL invertibility ⟺ u ∉ {0, ±c}. Symbol
     invertibility is necessary for an x-march but NOT sufficient
     for marchability (r1 rename: the previous label "x-marching
     invertibility" invited conflation): real characteristics need
     W > c (b), and spacelikeness needs u > c (D.4);
 (b) det(B_p − λ A_p) = (v − λu)³[(v − λu)² − c²(1 + λ²)]:
     characteristics = the streamline family with multiplicity THREE
     (carrying the triple (s, h0, Γ) of Thm D.2) + meridional Mach
     lines identical to the swirl-free case; real Mach lines ⟺
     W > c (meridional supersonic);
 (c) the sources S (centrifugal ρw²/r, geometric −ρvw/r) do NOT
     enter the pencil: the symbol, and hence every characteristic
     and spacelikeness criterion, is Γ-INDEPENDENT at fixed
     (u, v, c). Swirl deforms SOLUTIONS through S and through the
     state (Thm D.5), never the characteristic geometry.
PROOF: finite algebraic identities, machine-verified
(n6_swirl_kernel.py Part A, PASS; symbolic check = proof per the N6
verification-sufficiency discipline). QED.
Class: THEOREM. Gamma status: EOS-GENERAL (c² free symbol).
FALSIFIER: INDEPENDENT symbolic recomputation of (a)–(b) — any
algebra system exhibiting a nonzero difference rejects. (r1
falsifier-power repair, here and wherever "carrier re-run"
appeared: a deterministic re-run of frozen passing code in a
pinned environment is a REPRODUCTION, not a rejector, and is not
claimed as one; the rejecting tests are independent recomputation
and R1-style corruption checks.)

### Theorem D.4 [MS-T-SPACE] (spacelikeness of the data surface; frame invariance)
PLANAR CLAUSE (the r1 statement, its scope now explicit — r3, N2):
a surface x = const is a spacelike (marchable) data surface for
(E1)–(E5) iff M_x := u/c > 1, in EVERY frame (lab, wave, any
uniformly rotating frame): w and the frame rotation rate enter the
criterion NOWHERE.
CURVED CLAUSE (r3, N2 — hypothesis-incompleteness repair of
record: the object the D.13(c) audit row instantiates this theorem
on is Γ_d, by its own §0 / M0 [D-CONTRACT] definition a GENERAL
axisymmetric surface with free profile R(y) — cones, bells,
generically NON-planar; the r1 text proved the planar case and the
audit silently consumed the planarity, a hole that could LICENSE
an ill-posed march by a geometric rather than kinematic route):
a C¹ axisymmetric initial surface with unit MERIDIONAL normal
n_m = (n_x, n_r) (azimuthal normal component zero by axisymmetry)
is spacelike at a data point iff the meridional velocity's normal
component exceeds c with the Mach-cone one-sidedness on the
marching side:
  M_n := (u n_x + v n_r)/c > 1.
The planar clause is the special case n_m = e_x. FRAME INVARIANCE
SURVIVES: any uniformly rotating frame about the engine axis
leaves n_m, u and v unchanged and c is frame-invariant, so M_n is
identical in every frame. IN-CLASS COUNTEREXAMPLE OF RECORD (why
M_x is NOT the criterion on a curved surface): u = 1.2c, v = 0.9c
(meridionally supersonic, M_x = 1.2 — an M_x audit reports a
healthy margin) on a surface element tilted with
n_m = (cos 50°, −sin 50°): u·n_m = c(1.2·0.643 − 0.9·0.766) =
0.082c < c — the element cuts INTO the Mach cone and carries no
march. The per-phase stage-A margin of record is therefore (r3)
  m_n(ξ) := ess inf_y (M_n(y; ξ) − 1) > 0,
computed from the MERIDIONAL data with c(T) exact and n_m the
meridional normal field of Γ_d; for planar Γ_d this is exactly the
r1 margin m_x, and every prior use of m_x in this document reads
as m_n instantiated on planar data surfaces.
PROOF. Planar: from D.3(a) marching needs u² > c² plus the
Mach-cone one-sidedness; [T-NSW](b) (M0, THEOREM): the cone
condition reads w_x > c in relative velocity, and w_x = u_x with c
frame-invariant, hence u > c in every frame. Curved: spacelikeness
of a surface element depends only on its normal and the local
state; apply the same [T-NSW](b) cone argument in meridional
coordinates aligned with n_m — the normal relative-velocity
component is u·n_m = u n_x + v n_r in every axis-rotating frame
(u, v, n_m all invariant under rotation about the axis), and the
condition is u·n_m > c with cone one-sidedness. QED.
Class: THEOREM (both clauses; inherits [T-NSW] + D.3). Gamma
status: EOS-GENERAL.
FALSIFIER: an instance with u·n_m < c < |u⃗| where a march off the
surface is well-posed (would refute the criterion), or a frame in
which the audit value of M_n differs; ADDITIONALLY (r3, audit
wiring rejector) the recorded tilted-element counterexample must
FAIL any implementation that audits M_x on curved Γ_d — an audit
passing it is refuted as wired.

### Theorem D.5 [MS-T-MARGIN] (how Γ modifies the margin; the total-Mach hazard)
Let the state be closed γ(T)-exact (§0) and let AUD-c2T denote the
table-audit condition dc²/dT = R_g(γ + Tγ′) > 0 on the operating
range, γ′(T) = −R_g c_p′(T)/(c_p − R_g)² (AUD-c2T holds identically
for γ = const, where dc²/dT = γR_g > 0; for tables it is a finite
audit). Then:
 (i) (criterion invariance) By D.3(c), Γ does not appear in the
     spacelikeness criterion: the audit quantity is M_x alone.
 (ii) (state sensitivity — swirl COOLS, margin RISES) At fixed
     (h0, s, u, v, r) with u > 0 (through-flow orientation — r1
     hypothesis-completeness repair: for u < 0 the sign of
     ∂M_x/∂Γ flips and the margin FALLS with |Γ|; strictness
     needs uΓ ≠ 0), the state is determined by
     h = h0 − W²/2 − Γ²/(2r²) (Thm D.2(iii)); then
       ∂T/∂Γ|_{h0,s,u,v,r} = −Γ/(r² c_p(T)) ,
       ∂M_x/∂Γ|_{h0,s,u,v,r} = + (u Γ / (2 c³ r² c_p)) · (dc²/dT),
     so under AUD-c2T and u > 0, M_x is nondecreasing in |Γ| at
     fixed meridional velocity: adding swirl at fixed
     (h0, s, u, v, r) strictly increases the margin when Γ ≠ 0. SCOPE: this is a
     STATE-sensitivity statement (thermodynamic closure only), not a
     flow-solution statement — across twins that hold other
     quantities fixed (mass flux, P0) the induced (u, v)
     readjustment is a solution property, priced by its own
     comparison, not by this formula.
 (iii) (the TOTAL-MACH HAZARD — the panel P4/TWIN-A clause, made a
     theorem) M_tot := (u² + v² + w²)^{1/2}/c ≥ M_x with strict
     inequality whenever (v, w) ≠ 0; there exist states with
     M_tot > 1 and M_x < 1 — e.g. (u, v, w) = (0.9c, 0, c) gives
     M_tot = 1.345…, u < c: NOT spacelike, and W < c: not even
     meridionally hyperbolic. Hence any audit or closure-class
     declaration using total Mach including w OVERSTATES the axial
     marching margin and can license an ill-posed march. Monitors
     MUST use M_x on planar station surfaces — M_n on curved Γ_d
     (D.4 curved clause, r3/N2) — and meridional W/c for
     hyperbolicity, never M_tot.
PROOF. (ii): chain rule through T(h) (h′ = c_p > 0 invertible) and
c²(T); the displayed derivatives are one-line computations. (iii):
the inequality is Pythagorean; the exhibit is explicit. QED.
Class: THEOREM (γ(T)-EXACT for (ii), with AUD-c2T a named finite
audit; (i), (iii) EOS-general). Gamma status: as marked; γ=const
inherits (ii) unconditionally.
FALSIFIER: (ii) numeric check on the table backend — finite-difference
∂M_x/∂Γ at fixed (h0, s, u, v, r) vs the formula, tolerance derived
from table interpolation error; (iii) the exhibited state fed to the
marching-invertibility check must reject.

------------------------------------------------------------------------------
## §3 The H-AM hypothesis block and the flux-nullity theorem
##    (panel P1–P3 landed as numbered formal statements)

Throughout §3 the flow is the UNSTEADY 3-D inviscid (or
shear-declared) flow in the lab frame, in a control volume CV
bounded by: wetted walls Σ_w, an injection/faceplate boundary S_inj,
and cross-sections S(x₁), S(x₂) (planes x = const). Axial angular
momentum density ℓ := ρ r u_θ = ρ Γ.
ORIENTATION CONVENTIONS (r2 — previously UNDECLARED, a common-mode
sign hazard the arming test was blind to): n denotes the OUTWARD
unit normal of ∂CV EVERYWHERE, S_inj included; τ·n is the traction
exerted ON THE FLUID across the boundary element with outward
normal n, so τ_w = ∮_{Σ_w} r (τ·n)_θ dA is the axial torque of the
wall ON the fluid (positive = torques the fluid toward positive
θ). Every signed flux below is stated in this convention.

### Hypothesis block (formal; panel wording preserved, quantified here)
 H-AM0 (unsteady regularity — the function-space hypothesis, MINTED
   at r1: §0 declares classes only for per-phase meridional and
   φ-steady wave-frame fields; the unsteady lab-frame flow had NO
   declared space, an under-declared mathematical conditional):
   the unsteady flow is piecewise C¹ on cl(CV) × [0, t_c] — fields
   in L∞, finitely many C¹ moving front hypersurfaces across which
   the unsteady RH conditions hold in the weak form, one-sided
   limits at fronts, and NO energy/momentum concentration on
   lower-dimensional sets (orifice lips, re-entrant CV corners,
   measure-valued fronts): all flux integrands have well-defined
   integrable boundary traces on ∂CV, and L(t) := ∫_CV ρΓ dV is
   finite, CONTINUOUS — absolutely continuous on [0, t_c], so the
   fundamental-theorem step ∫₀^{t_c} L′ dt = L(t_c) − L(0) holds —
   and piecewise C¹ in t (r2 repair: "piecewise C¹ in t" alone
   admits JUMPS in L(t), which would break D.6's
   storage-cancellation FTC step; continuity of L is exactly what
   moving-front RH without surface angular-momentum concentration
   delivers, and it is hereby part of the HYPOTHESIS, not
   folklore). AUDIT (r3 RE-SPEC, N6 — the r1 audit "quadrature
   convergence of the flux integrals under grid refinement" was a
   NON-REJECTOR: the datasets this block audits are
   finite-resolution CFD fields, on which the integrand is
   already tame at the data's own scale, so quadrature refinement
   ALWAYS converges — it audited the postprocessing, never the
   flow hypothesis; a concentration-carrying flow sampled on any
   fixed grid PASSED it — exactly the vacuous-monitor defect
   class Remark 4.1 prosecutes elsewhere in this document): H-AM0
   is audited by CONCENTRATION tests —
    (i) SOLVER-RESOLUTION SEQUENCE: the flux/torque integrals
    recomputed on the dataset family at increasing SOLVER
    resolution (not quadrature refinement) must be Cauchy in the
    BALANCE residual; divergence ⟹ H-AM0 red (matches how
    H-AM2's numerical budget is priced);
    (ii) COLLAR SCALING at named suspects (orifice lips,
    re-entrant CV corners): integrals of |ρΓu| over shrinking
    collars must scale with the collar measure — an atom shows
    as scale-independence.
   Where NEITHER test is available (single-resolution data, no
   local refinement), H-AM0 is ASSUMED-PER-DATASET — declared,
   unaudited — and D.6's conditional (c2) must be reported as
   such.
 H-AM1 (exact T0 periodicity): every field is t_c-periodic at every
   fixed lab point; equivalently the interface/chamber data are in
   the standing pure-periodic scope (T0-flatness monitor green).
   Violation channel: aperiodic storage (mode transitions) — routed
   OUT of this block (it is an H-AM1 exit, not a torque).
 H-AM2 (inviscid or deviatoric-stress-declared — r3 EXTENSION,
   R4-3: the r1/r2 form budgeted the WALL torque only, while the
   exact CV balance carries the deviatoric-stress angular-momentum
   moment over ALL of ∂CV; an in-scope LES/RANS dataset with
   free-slip walls (τ_w = 0 correctly declared) and O(1) modeled
   plane stress on the station sections would audit RED with
   every hypothesis green — the D.8 census exhaustiveness was
   FALSE for it — and partial cancellation of a plane-stress
   moment against a wall torque could falsely PASS): the
   deviatoric stress is either zero (inviscid model) or its FULL
   boundary angular-momentum moment is DECLARED — physical
   (molecular) + modeled (Reynolds/SGS) + NUMERICAL shear alike
   (refuter extension of record) — as THREE typed budget entries,
   all in the §3 conventions (traction-on-fluid, n outward):
     τ_w      := ⟨∮_{Σ_w} r (τ·n)_θ dA⟩   (wall torque),
     T_S(x)   := ⟨∮_{S(x)} r (τ·n)_θ dA⟩  (cross-plane stress
                 moment, per audited station; n = +e_x, the
                 outward normal of the CV ending at S(x), so the
                 integrand is r τ_xθ),
     T_inj    := ⟨∮_{S_inj} r (τ·n)_θ dA⟩ (faceplate stress
                 moment).
   AVERAGING TYPE (r3, V-4): every entry is the CYCLE MEAN ⟨·⟩ —
   the r2 text defined τ_w as an instantaneous integral while the
   cycle-averaged balance consumes its mean (J_inj carried ⟨·⟩ in
   H-AM4; τ_w did not — an untyped symbol that then flowed into
   D.16's τ_decl(x) budgets); under strict T0 the instantaneous
   integral is t-independent (same one-line argument as Remark
   3.1) and the distinction vanishes. NOTE: the RESOLVED
   fluctuation covariance is NOT part of this budget — it lives
   inside ⟨ρ u_x Γ⟩ itself; these entries are the
   modeled/molecular stress moments only.
 H-AM3 (axisymmetric wetted geometry): every wetted surface is a
   surface of revolution about the engine axis; the CV boundary and
   any non-axisymmetric faceplate features (discrete orifices,
   posts) are explicitly disposed of — either excluded via a flush
   CV at the orifice exit planes (admissible declared bookkeeping)
   or carried as the DISTINCT torque channel (1) of D.8 (the default
   listing of record, per the judge's adjudication: "purely axial
   injection" does NOT imply zero boundary Γ-flux, and silent
   folding hides the weakest hypothesis).
 H-AM4 (declared injection flux): the injected angular-momentum flux
   J_inj := −⟨∮_{S_inj} ρ Γ (u·n) dA + ∮_{S_inj} p r n_θ dA⟩
   (n OUTWARD per the §3 conventions; the minus sign makes J_inj
   the angular-momentum flux INTO the CV — r2 SIGN REPAIR: under
   the outward-normal convention used by the proof's own
   divergence-theorem display, the previous unsigned definition
   entered the balance with the WRONG SIGN on J_inj; the polarity
   feeds D.16's residual linearly, a 2|J_inj| shift that can flip
   PASS/FAIL on swirled-injection data) is
   DECLARED, INCLUDING wave-induced backflow episodes (sign changes
   of u·n within the cycle); J_inj = 0 for the idealized
   axial-injection class with axisymmetric S_inj.
 H-AM5 (no body torque): no azimuthal body force (no MHD, no swirl
   vanes inside the CV).

### Theorem D.6 [MS-T-FLUXNULL] (flux nullity / J_inj accounting). THEOREM*.
Under H-AM0–H-AM5, the cycle-averaged axial angular-momentum flux
through every ADMISSIBLE cross-section equals the declared inputs:
  ⟨∮_{S(x)} ρ u_x Γ dA⟩ = J_inj + τ_w,decl(x) + T_S,decl(x)
                          + T_inj,decl
(r3, R4-3: the cross-plane and faceplate deviatoric-stress moments
T_S, T_inj — silently zero in the r1/r2 balance — are now declared
budget entries per the extended H-AM2, all in the outward-normal
traction-on-fluid convention; in the inviscid limb all three
stress entries vanish and the r2 display is recovered)
for a.e. station x — precisely, for every station whose plane S(x)
is TRANSVERSAL to the front set for a.e. t: no front coincides
with the plane on a time set of positive measure (r2 repair:
"for EVERY station x" was ill-defined when a front stands AT a
station plane — in-scope instance: a shock parked at a throat
station — where the trace of ρ u_x Γ on S(x) is two-valued; there
the balance is asserted for the one-sided limits x → x₀^±, which
agree by the RH normal-flux continuity of ρΓ. All but finitely
many stations per dataset cycle are admissible (r3, V-5d: §3 is
the unsteady lab-frame setting — "per phase" had no declared
meaning here); D.16 carries the matching
station-placement rule) —
where τ_w,decl(x) is the declared wall torque on the wetted surface
BETWEEN S_inj AND S(x) — CUMULATIVE in x (r1 repair: the previous
gloss "independent of x" is true only in the inviscid limb
τ_w ≡ 0, where the flux is station-independent as a COROLLARY; in
the shear-declared limb the balance holds per CV with a per-station
budget, and D.16's audit carries per-station budgets accordingly).
In the idealized class (inviscid, J_inj = 0):
  ⟨∮_{S(x)} ρ u_x Γ dA⟩ = 0,
i.e. the area-integrated, MASS-FLUX-WEIGHTED cycle mean of Γ
vanishes exactly at every ADMISSIBLE station (r3, R4-5(b): this
sentence had dropped the a.e./transversality qualifier installed
two sentences upstream; at a parked-front station the assertion
holds for the one-sided limits).
PROOF (assembly; conditional legs named). Local conservation: the
θ-momentum row in conservation form is
  ∂_t(ρΓ) + ∇·(ρΓ u) + ∂_θ p = 0
(machine-verified equivalent: carrier checks C1 and C4-gamrow-equiv
verify ρ DΓ/Dt = −∂_θ p against the primitive θ-row, which is the
same identity in smooth regions; RH fronts conserve the normal flux
of ρΓ by construction of the weak form). Integrate over the fixed
CV and apply the divergence theorem — H-AM0 supplies the boundary
traces, the integrability of L(t), and the RH cancellation of the
moving-front surface terms (r1: this step consumed an undeclared
regularity hypothesis; it is now H-AM0):
  d/dt ∫_CV ρΓ dV = −∮_∂CV ρΓ (u·n) dA − ∮_∂CV p r n_θ dA
                     + τ_w + (body torque).
Boundary disposal: on Σ_w, u·n = 0 and n_θ ≡ 0 — the [T-SLRW]
geometric kernel, machine-verified: a surface of revolution r = R(x)
has outward normal ∝ (−R′, 1, 0) in (x, r, θ) components, so
inviscid pressure exerts ZERO axial torque on every axisymmetric
wall (converging throats, plugs, cones, annular faceplate rings
included); on S(x_i), n = ±e_x so n_θ = 0 (planes equally
torque-free) and the flux term is ∓∮ ρ u_x Γ dA; on S_inj the
OUTWARD flux + pressure-torque sum equals −J_inj by the H-AM4
inflow definition, so it contributes +J_inj to the rearranged
balance (r2: signs now close under the declared outward-normal
convention — previously the S_inj polarity was convention-
dependent and undeclared) (H-AM4; under the
distinct-channel default of H-AM3 the non-axisymmetric orifice
sidewall torque is channel (1) of D.8 and must be declared there —
it is NOT silently zero). Body torque = 0 (H-AM5); boundary
deviatoric-stress moments declared per H-AM2 — wall τ_w AND the
cross-plane/faceplate moments T_S(x), T_inj (r3, R4-3: the plane
terms were silently dropped from the r1/r2 assembly; they are
boundary terms of the SAME divergence-theorem display and enter
the balance additively). Cycle-average over t_c: the storage term
integrates to (1/t_c)[L(t + t_c) − L(t)] = 0 by H-AM1 exact
periodicity. Rearranging gives the station-independent balance. QED*
WHY THEOREM* AND NOT THEOREM (promotion condition, named): the
geometric kernel ([T-SLRW]) and the local conservation identity
(carrier C1/C4) are machine-verified; the ASSEMBLED CV balance is a
pen derivation, independently reproduced by all four panel positions
but not yet symbolically/quadrature-checked end-to-end. The queued
promotion task of record: a symbolic (or exact-quadrature synthetic
field) check of the assembled balance on a generic surface of
revolution. Until it lands, the class is THEOREM* — conditional on
TWO named legs (r1 repair of the previous "no physical conditional
remains" under-declaration): (c1) that mechanical check, and
(c2) H-AM0, a MATHEMATICAL regularity hypothesis that no symbolic
check on smooth synthetic fields can discharge — audited per
dataset by the H-AM0 concentration tests (r3, N6: the old
"quadrature convergence" audit was a non-rejector; where neither
concentration test is available H-AM0 is ASSUMED-per-dataset and
must be reported as such), never provable in the
abstract. No physical conditional beyond H-AM0–H-AM5 remains.
Gamma status: EOS-FREE (kinematics + momentum only; no
thermodynamic closure enters).
REMARK 3.1 (instantaneous form under strict T0 — expert-1 clause,
proved). For a PURE rotating wave (every field of the form
F(x, r, θ − Ωt)), the CV integral L(t) = ∫_CV ρΓ dV over any
axisymmetric CV is CONSTANT in t (the θ-integral of a function of
θ − Ωt over the full circle is t-independent). Hence the storage
term vanishes INSTANTANEOUSLY and the balance holds at every
instant, not only on cycle average. J_inj READING (r3, N9f —
previously the remark silently redefined a cycle-mean symbol):
H-AM4 defines J_inj as a cycle mean; in this instantaneous balance
J_inj is read INSTANTANEOUSLY — under strict T0 the instantaneous
S_inj integral is t-constant by the same one-line argument, so the
two readings coincide; outside strict T0 the instantaneous form is
not asserted. Class: THEOREM (one line, as
shown). Gamma status: EOS-FREE (r3, R4-5(a) — the every-statement
rule applied; kinematic content only). FALSIFIER (r3, R4-5(a) —
the register cell previously read "one-line proof", and a proof
is not a rejector): a strict-T0 dataset (T0-flatness monitor
green) on which L(t) = ∫_CV ρΓ dV varies beyond derived quadrature
bars refutes the instantaneous form. Outside strict T0 but within
H-AM1, only the averaged form
holds, with the aperiodic-storage residual (1/t_c)ΔL as the named
violation channel.
FALSIFIER (= panel F1, verbatim commitment): on one periodic
chamber-CFD dataset in the hypothesis class (≥2 axial stations),
compute A1(x) = ⟨∮ ρ u_x Γ dA⟩ normalized by the gross flux
⟨∮ |ρ u_x Γ| dA⟩ (r3, V-3: absolute value on the WHOLE integrand —
the u_x-signed form loses its gross-flux meaning on backflow
episodes); D.6 is REFUTED if |A1 − J_inj − τ_decl − T_S,decl −
T_inj,decl| exceeds a
DERIVED tolerance (measured periodicity residual + declared
boundary-stress budgets, wall AND plane moments, r3). A genuinely inviscid
axisymmetric-wall axial-injection setup with nonzero A1 refutes the
theorem outright.

### Corollary D.7 (non-channels — the THEOREM-level negative)
Under H-AM0–H-AM5, no interior dynamics and no axisymmetric-surface
mechanism can source net axial angular momentum: unequal wave
counts, counter-rotating wave admixture, deflagrative asymmetries,
and throat convergence are NON-channels (they alter fields, not the
balance's boundary terms). In particular "wave-count asymmetries"
must never be listed as a net-swirl mechanism (the correction to
ADVISORY_rde_choking §2-bis(ii)(d), already executed of record).
Class: THEOREM* (same conditional as D.6, of which it is the
contrapositive reading). Gamma status: EOS-free.
FALSIFIER: same as D.6 restricted to a dataset realizing the named
mechanism with all H-AM hypotheses audited green.

### Definition D.8 (torque-channel census — exhaustive of record)
The exhaustive list of mechanisms that CAN break flux nullity, each
the negation of one hypothesis (census re-closed over
{¬H-AM0, ¬H-AM1..¬H-AM5} at r1 — the previous list was exhaustive
only RELATIVE TO an unstated regularity hypothesis; the fifth
channel below was uncensused):
 (0) regularity breakdown (¬H-AM0): periodicity-preserving
     energy/momentum concentration — orifice-lip singularities
     (exactly where real RDE injector data are least smooth),
     measure-valued fronts in the vanishing-viscosity limit,
     non-integrable re-entrant CV corner behavior — breaks the
     divergence-theorem step while negating NONE of H-AM1–H-AM5.
     Not a torque but a breakdown of the accounting itself. AUDIT:
     H-AM0's concentration tests (solver-resolution Cauchy +
     collar scaling — r3, N6: the old quadrature-convergence
     check was a non-rejector on fixed-resolution data).
 (1) non-axisymmetric wetted geometry (¬H-AM3): discrete
     injector-orifice sidewalls, posts, slots; the traveling wave
     phase-locks pressure asymmetry to hole geometry — generically
     NONZERO in real hardware even with purely axial injected
     streams. DISTINCT channel of record (never folded into (3)).
 (2) boundary deviatoric stress — WALL torque AND cross-plane /
     faceplate stress moments (r3, R4-3); physical, turbulent,
     NUMERICAL (¬H-AM2 inviscid limb): any dissipative dataset
     must audit to its declared boundary-stress moment SUM
     (τ_w + T_S + T_inj), not to zero and not to the wall torque
     alone ("too clean" is itself diagnostic, D.16).
 (3) swirled / non-axial injection and backflow Γ-exchange (¬H-AM4
     with J_inj ≠ 0): the physically weakest hypothesis.
 (4) aperiodic storage during mode transitions (¬H-AM1): an exit
     from the block, not a torque.
Class: DEFINITION (exhaustiveness = THEOREM* under D.6, OVER THE
EXTENDED SET {¬H-AM0..¬H-AM5}: any breakage must negate a
hypothesis — including the regularity one — and H-AM5 exits are
excluded by scope; r1: without channel (0) the exhaustiveness label
was false as stated). Gamma status: EOS-FREE (r2 — the body line
was missing while the register carried it, violating the
preamble's every-statement rule).
FALSIFIER (= panel F4 for channel (1)): one wave passage over a
discrete-orifice faceplate; engine-axis pressure torque integrating
to zero within derived tolerance REFUTES the distinct channel.

### Theorem D.9 [MS-T-MEASURE] (measure identities; equality of means under T0)
Fix a station and a point (or radial bin) on it; let ⟨·⟩ be the
cycle mean, ⟨f⟩_ṁ := ⟨ρ u_x f⟩/⟨ρ u_x⟩ the mass-flux-weighted mean
(defined where ⟨ρ u_x⟩ ≠ 0), cov(a, b) := ⟨ab⟩ − ⟨a⟩⟨b⟩. Then:
 (i) (exact identity; integrability class stated at r2 — "any
     integrable fields" was the WRONG class: L¹ fields alone do
     not give the covariance a meaning; the identity needs the
     PRODUCT in L¹, i.e. ρ u_x u_θ ∈ L¹(0, t_c) alongside
     ρ u_x, u_θ ∈ L¹ — supplied e.g. by ρ u_x ∈ L², u_θ ∈ L², or
     by the L∞ bound of H-AM0, the standing case)
     ⟨u_θ⟩ = ⟨u_θ⟩_ṁ − cov(ρ u_x, u_θ)/⟨ρ u_x⟩.
     Consequently zero net flux (D.6 with J_inj = 0) forces the
     INTEGRATED statement: ∮⟨ρu_x⟩⟨Γ⟩ dA = −∮ cov(ρu_x, Γ) dA,
     so the plain time-mean swirl is nonzero SOMEWHERE on any
     section whose area-integrated covariance is nonzero (in
     particular for single-signed covariance). The constraint is
     ONE scalar per cross-section; a pointwise "nonzero wherever
     cov ≠ 0" does NOT follow (r1 repair: the previous pointwise
     wording was a non sequitur contradicting its own trailing
     hedge — pointwise ⟨u_θ⟩ can vanish with cov ≠ 0; the
     integrated form is exactly what falsifier F2's A2 ≈ −A3
     tests).
 (ii) (equality of means under strict T0) For a pure rotating wave
     F(x, r, θ − Ωt) with n identical waves: time mean at a fixed
     point = phase mean (μ of D2.3) = frozen-t azimuthal mean.
     PROOF (r2 repair of the traversal count): at fixed
     (x, r, θ), F(·, θ − Ωt) traverses φ at uniform speed Ω; over
     one cycle t_c = 2π/(nΩ) (§0) the sweep covers ONE FUNDAMENTAL
     φ-CELL of length 2π/n, NOT the full circle — the previous
     "traverses φ exactly once per period (n times for n waves)"
     contradicted the §0 period. Equality with the FULL frozen-t
     azimuthal mean is restored by the previously unstated Z_n
     step: "n identical waves" MEANS F is 2π/n-periodic in φ
     (invariance under the Z_n rotation action), so the mean over
     one fundamental cell equals the mean over S¹. Hence time mean
     = cell mean = full azimuthal mean; μ is the pushforward of
     normalized cycle time under t ↦ ξ and the traversal is
     affine. (The statement was true as labeled; the proof step
     lacked the group-action precision.) QED.
 (iii) (measure discipline) The program's μ is a TIME measure and is
     NOT the mass-flux measure constrained by D.6: every swirl
     statement must NAME its measure; conflation is a protocol
     violation (T3-CONTROL input (3)).
Class: (i) THEOREM (two-line algebra: expand cov); (ii) THEOREM
under the strict-T0 hypothesis (proof above; this document's proof
carries the panel's "THEOREM* under T0" to THEOREM-with-named-
hypothesis — same content, the conditional now IS the hypothesis);
(iii) DEFINITION/discipline. Gamma status: EOS-free.
FALSIFIER (= panel F2): on one dataset, compute the pointwise
⟨u_θ⟩ field and A3 = ∮ cov(ρu_x, r u_θ) dA; the genericity reading
is demoted for that regime if ⟨u_θ⟩ ≡ 0 below noise while per-phase
swirl is O(1), or if A2 = ∮⟨ρu_x⟩⟨r u_θ⟩ dA fails A2 ≈ −A3 within
derived bars.

### Theorem D.10 [MS-T-SKE] (swirl-KE flux: positive, first-order, unconstrained)
Let E_θ := ⟨∮_S ρ u_x u_θ²/2 dA⟩. On any station with through-flow
ρ u_x > 0 a.e. and u_θ ≢ 0: E_θ > 0 strictly. E_θ is NOT
constrained by D.6 under ANY measure: for every value of the
flux-weighted mean of Γ (including 0) there exist fields with
arbitrarily large E_θ (exhibit, r3/R4-5(d) — the r1 "equal-mass-
flux halves" did NOT deliver zero Γ-flux on all in-class splits:
the Γ-flux integrand carries the r-weighting r u_θ, so inner/outer
annulus halves of equal mass flux give net Γ-flux ≠ 0; the working
construction is θ-HALVES AT EACH RADIUS: with ρ u_x axisymmetric,
set u_θ = +u₀ for 0 ≤ θ < π and −u₀ for π ≤ θ < 2π — the Γ-flux
cancels r-fiberwise, and E_θ = ½⟨ρu_x⟩u₀² A > 0, u₀ free). At the
recorded fluctuation level σ/μ ≈ 0.70 (P-M p.5) the covariance and
KE terms carry weight (σ/μ)² ≈ 0.5: FIRST-ORDER, not cosmetic.
Consequently a zero-swirl steady twin (TWIN-A) is fair at the
net-flux level ONLY and misattributes four named mechanisms: the
swirl-KE debit E_θ (positive-definite; unrecoverable as axial
thrust WITHIN THE VANELESS AXISYMMETRIC NOZZLE CLASS OF RECORD —
r1 scope repair: "unrecoverable" is a design-class statement
carried by the N6-2 scope note, NOT proved here and not true
unconditionally (turning vanes / partial pressure recovery in a
converging annulus are excluded only by scope); the N6-2 note:
overestimates steady axial performance),
the mean radial-equilibrium pressure shift ρ⟨u_θ²⟩/r, the
covariance wedge between weighting conventions (D.9(i)), and the
closure class + spacelikeness margin (D.5(iii)). The fair real-data
twin of record is TWIN-C (flux-consistent: matched mass, axial
momentum, energy AND angular-momentum flux at its MEASURED value,
measure and matching convention declared, E_θ reported as a
declared residual); TWIN-B (pointwise-time-mean profiles as steady
inflow) is REFUTED as fair — it double-books the covariance and
injects spurious net Γ-flux, faking a conserved quantity. The T3
ORACLE row proper (synthetic swirl-free H3 data) is UNAFFECTED.
Class: positivity + unconstrainedness THEOREM (proofs above /
exhibit); first-order weight = measured record (P-M numbers,
citation-bound); twin clauses = PRACTICE of record (panel P4,
protocol T3-CONTROL inputs (2) and (5), binding). Gamma status:
EOS-free.
FALSIFIER (= panel A4): compute the swirl-KE flux fraction
A4 = ⟨∮ρ u_x u_θ²dA⟩/(2·energy flux) on the first ingested dataset;
A4 comparable to the claimed twin-equivalence gap while TWIN-A
comparisons are in use fires rejector limb (iv) of T3-CONTROL.

### Conjecture D.11 (covariance sign — counter-wave plain-mean swirl)
On RDE chamber data in the standing scope, cov(ρu_x, u_θ) > 0
wave-ward (the wave drags mass-flux peaks), hence by D.9(i) the
plain time-mean swirl is net COUNTER-wave. Class: CONJECTURE
(judge-adopted lower class per R5; PRACTICE-level plausibility from
Schwer–Kailasanath-type fields). Gamma status: EOS-free.
FALSIFIER (= panel F3): sign(A3) on the first dataset vs the
prediction; wrong sign refutes.

### Non-claim D.12 (the P2 demotion, recorded as a prohibition)
The statement "the time-mean interface state carries net Γ ≠ 0, a
first-order omitted mean-field term" is REFUTED of record at the
flux level (three independent ways: its own anchor denies it; D.6
pins the flux-weighted scalar to the declared torque sum; it
mislabels the physics — the first-order omitted objects are
per-phase O(1) swirl and covariance/second-moment structure, D.10).
It must NEVER be asserted by this program. What survives, demoted:
profile/second-moment structure per D.9–D.10. The pointwise folk
statement "the mean flow has no swirl" is equally unavailable: NO
time-mean tangential field, profile, or angular-momentum flux is
reported anywhere in the read corpus (empirical vacuum of record).
Class: PRACTICE (a prohibition, rejector-gated — r1 repair: the
previous class "adjudication of record" was off the declared house
scale; the adjudication provenance — panel P2, unanimous — is the
row's citation, not its class). Falsifier of the vacuum claim:
exhibit a published time-mean tangential-velocity profile for an
RDE chamber/nozzle in the read-corpus scope.

------------------------------------------------------------------------------
## §4 Contract-field specification (replacing the VI.1 [vorticity]
##    placeholder) and the TRIPLE monitor's formal object

### Definition D.13 [MS-DEF-CONTRACT] (CycleFamily swirl row — staged text)
The VI.1 CycleFamily contract row of record, replacing the
`[vorticity]` placeholder (staged replacement text for M0 VI.1;
this is the F-swirl-1 absorption the panel mandated):

  CycleFamily := {P0, T0, thermo handle γ(·;ξ) |
    M_in(y;ξ)  — MERIDIONAL Mach profile (declaration of record:
                 M_in is meridional, never total; D.5(iii)),
    θ_in(y;ξ)  — meridional flow angle,
    s(y;ξ),
    w(y;ξ)     — swirl velocity profile; equivalently
                 Γ(y;ξ) := R(y)·w(y;ξ), the transported invariant
                 (Thm D.2); the evaluator carries Γ as its
                 transport row (one more unknown/equation per unit
                 process, M0 VI.4bis(iv) / N6 §4 note),
    h0(y;ξ)    — stagnation-enthalpy profile (see Remark 4.1)}
  + μ weights + provenance + stage-A audits, EXTENDED by:
    (a) the TRIPLE spread monitor of D.14 (G6 rejector);
    (b) the angular-momentum audit row of D.16;
    (c) the spacelikeness margin declared as m_n(ξ) =
        ess inf_y (M_n − 1), M_n = (u n_x + v n_r)/c with n_m the
        meridional normal field of Γ_d (D.4 curved clause — r3,
        N2: the prior m_x form silently instantiated the PLANAR
        theorem on a generally curved Γ_d and could license an
        ill-posed march; m_x is recovered exactly when Γ_d is
        planar) from meridional data (D.4/D.5) — total
        Mach PROHIBITED as the audit quantity.
Data class: rows in BV ∩ L∞(y), piecewise C¹ sufficient; through-
flow sign convention declared (D.14 guard). Generators and imported
data pass the SAME audits (VI.1 clause unchanged).
CLASS-ADEQUACY NOTE (r1): a data row with a jump in s, Γ or h0 at
an interior ψ₀ evolves downstream as a CONTACT curve — now
explicitly admitted by the §0 extended S1 class (C-fronts) and
governed by the D.2 contact clause; the comparison theorem's
treatment of these curves is owned by S.22 (g2b). Previously the
contract admitted data the field class could not carry — an
undeclared inconsistency, closed here. State recovery is UNIQUE
under AUD-cp + AUD-c2T — for ALL Mach numbers, the "supersonic"
restriction being about marchability, not recovery (r3, N9c: this
was an unlabeled THEOREM-grade assertion with no proof and no
falsifier — the defect pattern r1 prosecuted in D.18. PROOF, two
lines: at fixed y the row data give (M, s, w, h0); T solves
F(T) := h(T) + M² c²(T)/2 = h0 − w²/2 with F′(T) = c_p +
M² (dc²/dT)/2 > 0 under AUD-cp + AUD-c2T, so T is unique; then
ρ, p follow from (s, T) via the γ(T) closure. Class: THEOREM,
γ(T)-EXACT; falsifier: a table instance with two distinct
recovered states matching the same row data. Independent
re-derivation of record: round-2 lens-1 §C-vi, different route —
monotonicity of T ↦ W²/c² — agrees) and EXISTS only under
AUD-hRANGE (§0,
r2: on bounded tables the recovered h must lie in the table's
h(T) range; the recovery rejector FLAGS out-of-range states,
never extrapolates).
Class: DEFINITION (contract). Gamma status: γ(·;ξ) handle exact.
FALSIFIER (contract-grade): a dataset in the declared class on
which state recovery (P0, T0, profiles → full V on supersonic
patches) fails or is non-unique refutes the class declaration;
the stage-A audits are the row's rejectors.

REMARK 4.1 (why h0(y;ξ) must be profile-grade — vacuity hazard,
formal). Under the pre-swirl contract {P0, T0 | profiles}, per-phase
h0 is CONSTANT in y by construction (single scalar T0 closes the
state). A monitor for Δ_h0 computed on a data class that cannot
represent Δ_h0 ≠ 0 is VACUOUS — rejector-incapable, an R5
violation: it would return 0 identically and falsely license the
reduction on exactly the data (real RDE: parasitic deflagration,
fill stratification) where h0 spread is expected. Hence the
contract delta includes promoting the stagnation handle to profile
grade (h0(y;ξ), or equivalently T0(y;ξ) with h0 recovered), with
the scalar T0 retained as the phase-aggregate handle. This remark
is the formal ground for the panel's "the surviving physics is not
yet ingestible" clause. Class: THEOREM (one-line: a functional
identically zero on its domain rejects nothing). Gamma status
(r2 — previously MISSING here and "—" in the register, the same
preamble-rule violation class as r1's O-9a): the vacuity argument
is EOS-free, but the premise "a single scalar T0 closes the
state, h0 constant in y" consumes h0 = h(T0) + KE through the
h = h(T) closure — status of record: γ(T)-EXACT. Falsifier:
exhibit a {P0, T0 | M, θ, s, w} state recovery with y-dependent h0.

### Definition D.14 [MS-DEF-TRIPLE] (the TRIPLE monitor — formal object)
For each phase ξ, on the recovered interface state:
 PRECONDITION (the C1 ψ-monotonicity/backflow guard, census C1;
 well-posedness, not a tolerance): through-flow
 ρ u_n(y;ξ) ≥ δ_tf > 0 for a.e. y (u_n = velocity normal to Γ_d),
 so that ψ: y ↦ ψ(y) is strictly monotone and streamline labeling
 is a bijection. If violated, the monitor is NOT LICENSED and the
 phase routes to the two-regime decomposition (D1 §4.3bis) — the
 monitor never runs on backflow data (its ψ-parametrization is
 ill-posed there).
 MEASURED OBJECT: with ψ normalized to [0, Ψ], the spreads
   Δ_Γ(ξ)  := osc_ψ Γ,   Δ_h0(ξ) := osc_ψ h0,   Δ_s(ξ) := osc_ψ s
 (osc = ess sup − ess inf; FINITE on the BV data class, jumps
 included) are the cheap reported diagnostics, and the OBSTRUCTION
 ESTIMATOR is their TOTAL-VARIATION refinement (dimensionless,
 derived from the N6-3 identity — the exact object whose vanishing
 licenses the closed form). r1 REPAIR OF RECORD: the previous
 sup-derivative form was +∞ on ANY in-class row with a jump — the
 distributional derivative has an atom exactly on the motivating
 stratified data (fill stratification, parasitic deflagration), so
 the license rule was vacuous there and the Δ_* spreads were
 defined but never consumed. TV form of record:
   OBS(ξ) := [ TV_ψ(h0) + sup_ψ|Γ| · TV_ψ(Γ) / y_min²
               + sup_ψ T · TV_ψ(s) ] / W_ref(ξ)² ,
 TV_ψ(q) := total variation of the ψ-parametrized row q on [0, Ψ]
 (= ∫|dq/dψ| dψ on C¹ pieces + Σ|jumps|; finite exactly on BV;
 reduces to the previous sup·Ψ form on C¹ rows by the mean value
 inequality), W_ref(ξ) := ess inf_y W(y;ξ), and (r2 — y_min was
 USED but never DEFINED anywhere in this document, a
 self-containedness defect) y_min := ess inf_y y = the minimum
 interface radius over Γ_d (y = radius on the control surface per
 the §0 N6 convention; y_min > 0 by H-ANN). Note Δ_q ≤ TV_ψ(q):
 the spreads LOWER-BOUND the TV legs (screen role); OBS is the
 licensing quantity. Rationale of the form: N6-3 (machine-verified)
 gives dh/dW|_y = −W + (h0′ − ΓΓ′/y²)·dψ/dW; the obstruction
 enters INTEGRATED along the surface/march, so the correct pairing
 is the ψ-integral of the obstruction content (a finite measure on
 [0, Ψ] for BV rows) against the transport scale 1/W_ref². The
 previous pointwise bound |dψ/dW| ≤ Ψ/W-scale is FALSE IN FORM
 (r1: dψ/dW is unbounded at any interior extremum of W(y) —
 generic on real data), not a pending constant: the repair changes
 the functional form to the displayed TV pairing, and the residual
 gap is the per-campaign sensitivity CONSTANT only (see G-b,
 reformulated). The s-term prices the isentrope-closure leg
 (dh = dp/ρ needs ds = 0 along the surface). The N6-2 closed
 form (Rao two-constant machinery with W = meridional speed) is
 LICENSED for phase ξ iff OBS(ξ) ≤ tol(ξ) with tol DERIVED per
 campaign from the target objective tolerance through the closure-
 error sensitivity (bars-b1–b4 discipline; never a reused numeric
 constant — no magic tolerances). Else the FIELD-LEVEL route
 (five-field system [S-5F] / reverse-AD march, M0 VI.4bis(iv)) is
 MANDATORY. Wired as a G6 REJECTOR: uniform ⟹ licensed; else
 blocked — never a warning.
Class: DEFINITION (the measured object — total-variation-grade
and FINITE on the whole declared BV class, r1 repair of a
definition-leg defect that made the previous monitor
rejector-incapable on its target data) + the LICENSING LEG is a
NAMED GAP at SCHEMA grade with TWO legs (r3, N5 — HONEST
DOWNGRADE OF RECORD: the r1 sentence "the FORM is no longer the
gap" was an OVER-CLAIM and is RETRACTED. The licensing direction
— OBS(ξ) ≤ tol ⟹ the N6-2 contour is within propagated tolerance
of the field-level optimum — requires an UNPROVEN sensitivity
lemma, |objective error| ≤ S[data] · OBS(ξ), i.e. that the
design-level error feels the closure defect only through its
ψ-INTEGRATED content. Concrete reason for doubt: at an interior
extremum of W(y) — "generic on real data", this document's own r1
words — dψ/dW → ∞, so the POINTWISE defect of the closure
p = p(W, y), which N6-2 uses pointwise to build the contour, is
UNBOUNDED while OBS stays small if TV is small; whether that
produces only an integrated-size objective error depends on how
the N6-2 construction consumes the closure — through
ψ-QUADRATURES, in which case integration-by-parts moves the
defect onto TV exactly, or through POINTWISE INVERSION at the
extremum, in which case the monitor needs a W-extremum guard
analogous to δ_tf. No lemma here or in N6 §5 decides it):
 (G-b1) the sensitivity FUNCTIONAL — prove or refute
   |objective error| ≤ S(W_ref, geometry) · OBS on the BV class,
   with the W-extremum case treated explicitly (route above);
 (G-b2) the per-campaign derived-tolerance CONSTANT, as before.
Until BOTH legs land, the monitor may only be used with a
campaign-derived tol, never a default; its BLOCKING verdicts are
of record (conservative direction, unaffected — see the D.15
SAFETY NOTE), while every LICENSING verdict carries the G-b1
conditional EXPLICITLY — the licensing direction is exactly the
direction R5 cares about. Gamma status: EOS-general (obstruction identity is), with
the s-term γ(T)-exact through T. EXPECTATION OF RECORD (unanimous,
panel): real RDE data will generically FAIL triple-uniformity and
route to the field-level machinery — the monitor's job is honest
routing, not blessing.
FALSIFIER: (a) well-posedness — a backflow dataset slipping past
the guard (δ_tf mis-declared) with the monitor still returning a
verdict refutes the guard wiring; (b) licensing — a phase with
OBS(ξ) ≤ tol whose N6-2-designed contour differs from the
field-level optimum by more than the propagated tolerance REFUTES
the derived-threshold chain (this is the monitor's own rejector).

### Theorem D.15 [MS-T-GAMONLY] (Γ-only monitoring falsely licenses the reduction)
CLAUSE 1 (false licensing — THEOREM). Vanishing swirl spread does
NOT license the N6-2 closed form: there exist data with Δ_Γ = 0
(indeed Γ ≡ 0) and Δ_h0 ≠ 0 (or Δ_s ≠ 0) for which the pointwise
closure p = p(W, y) FAILS. By the N6-3 obstruction identity
(machine-verified, n6_swirl_kernel.py Part B3):
   dh/dW|_y = −W + (h0′ − Γ Γ′/y²) · dψ/dW ,
setting Γ ≡ const, h0′ ≠ 0 leaves the residual term h0′ · dψ/dW,
nonzero for every variation with dψ/dW ≠ 0 at some surface point
(generic: any variation transporting mass across that point).
Hence a Γ-only uniformity monitor returns "uniform" on this class
and licenses a closed form whose defining closure is false — false
licensing, structurally. MACHINE COVERAGE, stated honestly (r1
retraction of the "iff machine-verified" attribution): Part B3
verifies the IDENTITY plus two controls — the free-vortex
vanishing instance (IF direction) and one generic breaking
instance (non-identical vanishing). That is all the carrier
proves; it fully carries Clause 1.

CLAUSE 2 (minimality / iff — SEPARATED at r1, different class).
The sharper claims "the obstruction vanishes identically iff
Γ′ = h0′ = 0 (with s uniform)" and "the TRIPLE (Γ, h0, s) is the
MINIMAL sufficient spread set" hold ONLY under an
ALL-ADMISSIBLE-VARIATIONS quantifier, which is LOAD-BEARING (r1:
previously buried in a non-load-bearing parenthetical): at FIXED
surface geometry y = y(ψ) the CANCELLATION FAMILY
   Γ(ψ) Γ′(ψ) = y(ψ)² h0′(ψ),  h0′ ≢ 0
(solvable for any h0, y: Γ² = Γ₀² + 2∫ y² h0′ dψ, PROVIDED
Γ₀² > 2 sup_ψ(−∫ y² h0′ dψ) so that Γ² stays positive — r3, N9e:
the existence claim carried this silent hypothesis; on BV ∩ L∞
rows the sup is finite, so a large enough Γ₀ always exists and
the family is nonempty as claimed) zeroes the
obstruction ALONG THE SURFACE with a non-uniform triple — the
literal fixed-geometry iff is FALSE. The exclusion argument —
under variation y(ψ) deforms while (Γ, h0) are transported, so the
1 and 1/y² powers separate on an open (W, y) set and break the
fine-tuned relation — is a genericity/power-separation step that
is NOT machine-verified and is the SAME open leg as the N6-3
strong-only-if SCHEMA of record (r1: the previous class line
booked it as machine-verified THEOREM content while the doc's own
falsifier called it a SCHEMA — an internal contradiction, resolved
by this split). Each of the three spreads DOES appear
independently in the obstruction + closure chain (Γ via ΓΓ′/y²,
h0 via h0′, s via the isentrope leg), and D.8/D.14 exhibit
in-class data violating each alone — necessity is exhibited;
minimality-as-iff awaits the quantified proof.
SAFETY NOTE (from the r1 record): the D.14 OBS monitor is
CONSERVATIVE against the cancellation family — it sums absolute
values and would BLOCK, not license, on it; over-blocking is the
declared design, so the monitor's rejector job does not depend on
Clause 2.
Class: Clause 1 THEOREM (identity machine-verified + explicit
exhibit); Clause 2 SCHEMA (route named: open-set variation
quantifier + power-separation; = the N6-3 strong-only-if leg).
Gamma status: EOS-GENERAL.
FALSIFIER: (Clause 1) exhibit an alternative pointwise reduction
that closes the control-surface derivation for Γ ≡ const,
h0′ ≠ 0; (Clause 2) exhibit an admissible-variation family under
which a cancellation-family datum keeps the obstruction ≡ 0 for
ALL variations with a non-uniform triple — this would refute
minimality and negatively discharge the N6-3 strong-only-if SCHEMA
(the falsifiers are deliberately the same object).

### Definition D.16 [MS-DEF-AMAUDIT] (angular-momentum audit row)
New contract audit row (BALANCE-RESIDUAL, never a zero-check), at
≥2 stations per dataset, EACH station carrying its OWN cumulative
declared budget (r1, from D.6's repaired statement: for
dissipative data τ_decl(x) = declared wall torque from S_inj to
S(x) GROWS with x; a single shared τ_decl is correct only in the
inviscid limb):
  R_AM(x) := | ⟨∮_{S(x)} ρ u_x Γ dA⟩ − J_inj^decl − τ_decl(x)
               − T_S,decl(x) − T_inj,decl |
             / max( ⟨∮_{S(x)} |ρ u_x Γ| dA⟩ , ε_gross )
(r3, R4-3: the declared budget now includes H-AM2's cross-plane
and faceplate stress moments; r3, V-3 NORMALIZER REPAIR: the r2
denominator ⟨∮ ρ u_x |Γ| dA⟩ was SIGNED in u_x — on H-AM4's own
admitted backflow episodes the time average subtracts backflow
transport from through-flow transport, so the denominator becomes
the small DIFFERENCE of two O(1) gross transports and can sit at
the ε_gross floor on data nowhere near the zero-swirl degeneracy,
inflating R_AM into a spurious FAIL; a rejector whose firing
threshold is modulated by a cancellation the tolerance derivation
does not model violates the derived-tolerance discipline as
directly as a false-pass would. The r3 form takes |·| on the WHOLE
integrand: it bounds the old denominator from above, coincides
with it on through-flow-only data — no recalibration on clean
cases — and is cancellation-free by construction.)
PASS iff R_AM ≤ tol_AM at every audited station, tol_AM DERIVED
per dataset from: measured
periodicity residual (H-AM1 audit) + declared boundary-stress
budget bars — wall AND per-station plane moments (H-AM2, r3) —
+ quadrature error of the flux integrals
— never a magic constant; ε_gross = derived floor guarding the
degenerate zero-swirl case. Rejector semantics IDENTICAL to
T0-flatness (a red row blocks ingestion, no downgrade-to-warning).
Two diagnostic clauses of record: (i) a raw zero-check would
falsely reject every viscous dataset and can falsely PASS on
cancelling torques — hence the declared-budget form; (ii) "TOO
CLEAN" is itself diagnostic: frictional data (e.g. a Q2D with
skin-friction sources) auditing far below its own declared friction
torque flags a bookkeeping error upstream, and the row must FLAG
(not pass silently).
STATION-PLACEMENT RULE (r2, mirroring D.6's a.e.-transversality
clause): audited stations are chosen with S(x) transversal to the
data-visible front set — never on a parked front (e.g. a standing
shock at a throat plane), where the flux trace is two-valued; the
placement is AUDITABLE (front-indicator scan on the dataset) and
a station failing the scan is MOVED, not waived.
SIGNED ARMING CLAUSE (r2): the arming test injects a known torque
of KNOWN SIGN and must move the SIGNED residual
⟨∮ρu_xΓdA⟩ − J_inj^decl − τ_decl(x) in the matching direction —
magnitude within bars AND polarity correct. A magnitude-only
arming test is BLIND to a common-mode orientation-convention
error (the N-2 class: outward-vs-inward normal on S_inj shifts
the residual by 2|J_inj| and can flip PASS/FAIL on
swirled-injection data, the block's own physically weakest
hypothesis); the polarity leg makes the row's rejector
convention-independent. All signs per the §3 conventions
(n outward, J_inj = inflow, τ = traction-on-fluid).
ARMING EXTENSION (r3, V-3): the arming battery includes ONE
BACKFLOW-BEARING synthetic — sign-reversing u_x within the cycle,
injected known torque — on which R_AM must still move by the
known amount within bars; the signed arming test alone is
NUMERATOR-side and structurally blind to denominator pathologies,
which is exactly how the r2 normalizer defect survived it.
Class: PRACTICE (rejector-gated per R5); the residual's target
value is THEOREM*-backed by D.6. Gamma status: EOS-free.
FALSIFIER: the row's own arming test — a synthetic dataset with an
injected known torque must move R_AM by the known amount within
bars (rejector proof), and a doctored dataset with a hidden swirl
injection must FAIL the row.

------------------------------------------------------------------------------
## §5 What 2.5-D DROPS: the 3-D wave frame and the reduction-residual
##    (azimuthal commutator) objects
##    CARRIER: phaseD_meanswirl_symcheck.py — ALL CHECKS PASS

### Definition D.17 [MS-DEF-3DWF] (the 3-D wave-frame system; ξ ↔ φ)
The exact reference object is the steady co-rotating 3-D flow: all
fields of the form F(x, r, φ), φ = θ − Ωt, solving unsteady 3-D
Euler with ∂_t → −Ω ∂_φ (absolute velocity components retained: no
Coriolis/centrifugal fictitious forces are introduced; the wave
frame enters ONLY through the independent variable). Under strict
T0 (pure rotating wave, n identical waves), the per-phase family of
D.1 is the family of azimuthal sections: V(·,·;ξ) = V₃D(·,·,φ(ξ)),
with ξ ↦ φ affine (D.9(ii)) and ∂_φ ↔ (dφ/dξ) ∂_ξ: the phase label
IS the wave-frame azimuth. Existence of the steady co-rotating
representation is the standing STAGE-1 exact-quotient claim of
record (M0 helical-symmetry route, SCHEMA-to-THEOREM* per its own
block; not re-adjudicated here). Class: DEFINITION.
Gamma status: EOS-FREE (kinematic frame identification; no
thermodynamic closure enters). FALSIFIER: any strict-T0 dataset on
which the time mean at a fixed lab point differs from the frozen-t
azimuthal mean beyond derived bars refutes the ξ ↔ φ
identification (D.9(ii)'s own test doubles for it). (Both added at
r1 — this DEFINITION alone violated the preamble's every-statement
rule.)

### Definition D.18 [MS-DEF-KRES] (the reduction-residual / commutator terms)
Write each exact wave-frame equation as the corresponding per-phase
2.5-D row (Definition D.1, all ∂_φ struck) PLUS a residual. With
w_rel := w − Ωr (relative azimuthal velocity; in the standing scope
w_rel ≈ −D_CJ at the interface — O(1) LARGE, [T-NSW]), the residual
vector is (carrier C4 — SEVEN CHECKS over the SIX K rows below,
the seventh check being C4-gamrow-equiv against the independently
written θ-momentum row; r2 count repair: the previous "seven
rows" collided with the register's measured six-row K list —
measured truth: six K rows, seven C4 checks; verification
status honestly stated below — in particular every
curvature/metric term −vw/r, ρw²/r is RETAINED by the 2.5-D
operator; ONLY ∂_φ terms are dropped):

  K_ρ  := (1/r) ∂_φ(ρ w_rel)                    (mass sweep)
  K_u  := ρ (w_rel/r) ∂_φ u                     (x-mom sweep)
  K_v  := ρ (w_rel/r) ∂_φ v                     (r-mom sweep)
  K_Γ  := ρ (w_rel/r) ∂_φ Γ + ∂_φ p             (Γ row: sweep + TORQUE)
  K_s  := (w_rel/r) ∂_φ s                       (entropy sweep)
  K_h0 := (w_rel/r) ∂_φ h0 + (Ω/ρ) ∂_φ p        (h0 row: sweep + WORK)

These are THE named reduction-residual objects — "the azimuthal
commutator terms" — that a later theorem will bound (S.22).

DISTRIBUTIONAL READING OF RECORD (r3, R4-1 — repairing an
r2-created TYPE MISMATCH and a front-scope hole in both iffs).
The displayed rows are CLASSICAL ∂_φ expressions, defined only on
the open complement of the front set; but §0 admits wave-steady
front hypersurfaces with generically NONZERO azimuthal normal
component n_φ (the detonation front is the in-scope instance —
S.22's own r2 text says so verbatim), and S.22 (r2) already
prices K as "a MEASURE with an atom on the front": the same
symbol was being read as two inequivalent objects in one
document. K is hereby DEFINED as a DISTRIBUTION on D × S¹_φ:
writing each exact wave-frame row in cylindrical divergence form
∂_x F_x + ∂_r F_r + (1/r)∂_φ F_φ,rel = S (the ∂_t → −Ω ∂_φ
substitution absorbed into the RELATIVE azimuthal flux F_φ,rel,
advective factor w_rel), the distributional residual of a
piecewise-C¹ field decomposes as
 (a.c. part)  the displayed smooth-region K rows, off fronts;
 (singular part)  an atom on each front with surface density
   n_φ · [F_φ,rel]   per row (up to the declared surface-measure
   normalization) — the n_φ-weighted jump of the relative
   azimuthal flux: exactly the DIFFERENCE between the full 3-D RH
   residual [F_m·n_m] + n_φ[F_φ,rel] and the meridional RH
   residual [F_m·n_m] that the per-phase 2.5-D sections impose.
These atoms ARE the objects S.22's split-norm candidate prices:
§5 and S.22 now type-check against each other. The row-by-row
singular-density bookkeeping is a pen computation of the same
grade as the a.c. transcription and RIDES the G-f independent
re-derivation; the G-f rejector spec is EXTENDED at r3 with a
FRONT instance (falsifier block below).

VERIFICATION STATUS (r1 downgrade, honest). What C4 verifies is
the INTERNAL CONSISTENCY of one transcription: for five of the
seven CHECKS (the cont, xmom, rmom, s, h0 K-row checks — count
per the r2 reconciliation above) the "exact" row, the "2.5-D"
row and K are all built from the SAME in-file operator, so
exact − reduced − K ≡ 0 is an algebraic tautology of the
transcription — it CANNOT detect a common-mode mis-derivation (a
metric term wrong in BOTH transcriptions passes silently; the
[X-O31CS] CS4 pattern of record, which should have been applied
here at authoring and was not — r1 absence finding accepted).
Independently verified content: C4-gamrow-equiv (field-form Γ row
vs an independently written θ-momentum row), C1–C3, and R1.
COMPLETENESS of the K list against the exact 3-D system is
therefore a NAMED GAP (G-f), class SCHEMA until its promotion
lands: derive the exact unsteady 3-D Euler rows in cylindrical
divergence form from an INDEPENDENT symbol set (∂_t → −Ω ∂_φ
substituted at the end), diff against 2.5-D + K, and arm two
rejectors — a metric-corruption check (corrupt one
continuity/r-momentum metric term; a C4-class check must FIRE) and
a K-corruption check (drop ∂_φ p from K_Γ; C4-gamma must FAIL).

EQUIVALENCE CLAUSE (given its own hypothesis, class and falsifier
at r1; RESTATED DISTRIBUTIONALLY at r3 — R4-1 of record: in the
classical smooth-region reading BOTH iffs were FALSE on the
declared front-carrying class, in both directions. In-class
counterexamples: (α) two constant states across a helical C¹
wave-steady front satisfying the full 3-D RH — every classical
∂_φ vanishes off the front, so classical K ≡ 0, yet each
meridional section carries a front curve whose 2.5-D meridional
RH is VIOLATED by the oblique jump data: the sections do not
solve the per-phase system; (β) conversely a family of meridional
normal shocks with phase-dependent standoff x_s(ξ): each section
solves the 2.5-D system exactly and classical K ≡ 0, yet read as
a 3-D field via ξ ↔ φ the helical front surface x = x_s(φ) has
n_φ ≠ 0 and violates the 3-D RH; and in both examples the old
conclusion "degenerate axisymmetric operation" was FALSE — the
front is helical, the operation genuinely 3-D and unsteady at
every fixed lab point. The DISTRIBUTIONAL K sees all of this: in
(α)/(β) the singular part is NONZERO — the front atom IS the
front-level difference between the two systems, invisible to the
classical reading.)
FIRST IFF (bookkeeping, now true): the wave-frame field solves
the exact 3-D system DISTRIBUTIONALLY iff each azimuthal section
solves the per-phase 2.5-D system distributionally (meridional RH
included) AND K = 0 as a distribution — a.c. part and front atoms
both. (By construction of K as the operator difference; the atom
identity is the singular-density display above.)
SECOND IFF: for a field solving the exact 3-D wave-frame system,
and under
  (H-NC — REWORDED at r2: the r1 phrase "|w_rel| ≠ c on every
  open subset" literally read as the pointwise-EVERYWHERE
  condition, which the in-scope CJ locus itself VIOLATES — the
  theorem would have been inapplicable to its own scope under the
  literal reading; the INTENT is now the text) the relative-sonic
  locus {|w_rel| = c} has EMPTY INTERIOR — there is no open
  subset on which |w_rel| ≡ c (in-scope justification:
  [T-NSW](a) — the relative sonic locus IS the Chapman–Jouguet
  surface, a hypersurface, and the marching domain of record sits
  in the hyperbolic region |w_rel| > c, where "the sweep HELPS"),
and under
  (H-WR — MINTED at r2; N-1 repair: w_rel ≠ 0 is LOAD-BEARING in
  the ⟹ direction but previously lived in a proof parenthetical
  ("standing scope"), not the hypothesis line, and H-NC does NOT
  imply it; r3 READING EXTENSION, declared: H-WR is read UP TO
  THE ONE-SIDED FRONT TRACES — w_rel± ≠ 0 a.e. on each front —
  which the singular leg below consumes; same in-scope
  justification) the co-rotation locus {w_rel = 0} has empty
  interior (in-scope justification: [T-NSW](a) gives
  |w_rel| > c > 0 on the marching domain),
K = 0 AS A DISTRIBUTION iff the operation is DEGENERATE
AXISYMMETRIC (r3 conclusion, strengthened and made true): all
fields φ-independent off fronts, AND every front is either
jump-free (removable) or a φ-INVARIANT (meridional × S¹, n_φ ≡ 0)
surface with φ-independent one-sided limits.
PROOF of the second iff under H-NC + H-WR (⟸ trivial; ⟹ was the
r1 hole). A.C. LEG (r1/r2, unchanged): off the co-rotation locus
(H-WR makes its complement
dense in each smooth region), K_u = K_v = K_s = 0 force
∂_φu = ∂_φv = ∂_φs = 0. K_ρ = 0 gives ρ ∂_φw = −w_rel ∂_φρ;
K_Γ = 0 then gives ∂_φp = w_rel² ∂_φρ; ∂_φs = 0 gives
∂_φp = c² ∂_φρ. Compatibility: (w_rel² − c²) ∂_φρ = 0, so
∂_φρ = 0 off the relative-sonic locus, hence everywhere in each
smooth region (continuity of ∂_φρ off fronts + empty interior of
both loci, H-NC and H-WR); all
remaining ∂_φ vanish by back-substitution. K_h0 adds nothing new:
with ds = 0 (hence ∂_φh = ∂_φp/ρ) and ∂_φp = w_rel² ∂_φρ,
K_h0 = (w w_rel/r)(∂_φw + w_rel ∂_φρ/ρ) = 0
automatically by K_ρ — r3, N8 PRINT CORRECTION of record: the
r1/r2 text displayed the prefactor as Ω w_rel, which equals the
correct w w_rel/r ONLY where w_rel = 0 or r → ∞ (via
w_rel/r + Ω = w/r); the conclusion was right, the printed
identity false — the elimination line is added to the G-f
rejector list as a one-line sympy check.
SINGULAR LEG (r3, new — the front-atom part): on an exact 3-D
solution the 3-D RH atoms vanish, so K's atoms reduce to minus
the meridional-RH residual; K = 0 as a distribution then forces
the meridional RH TOO, hence n_φ[F_φ,rel] = 0 row-by-row. At a
front point with n_φ ≠ 0: [F_φ,rel] = 0 for every row —
g := ρ w_rel is continuous ([ρ w_rel] = 0) and by H-WR (front-
trace reading) g ≠ 0 a.e.; then the azimuthal x- and r-rows
g[u] = 0 and g[v] = 0 give [u] = [v] = 0, so the meridional-
normal velocity û := u n̂_x + v n̂_r is continuous (n̂ = the unit
meridional normal). Meridional rows (holding by the K = 0
reduction to meridional RH above): mass [ρ û] = û[ρ] = 0;
momentum [ρ û u + p n̂_x] = u û[ρ] + n̂_x[p] = 0 and the r-row
likewise. CASE û ≠ 0: [ρ] = 0, hence [p] = 0 (n̂ is a unit
vector, n̂_x, n̂_r not both zero). CASE û = 0: the momentum rows
read n̂_x[p] = n̂_r[p] = 0 directly, so [p] = 0. Either way the
azimuthal θ-row g[w] + [p] = 0 gives [w] = 0; continuity of
g = ρ w_rel with [w] = 0 and w_rel ≠ 0 gives [ρ] = 0; the
remaining rows close [h0] = [s] = 0. ALL jumps vanish: the front
is REMOVABLE where n_φ ≠ 0. A connected front component with n_φ ≡ 0 contains the
φ-direction in its tangent space everywhere, hence is a union of
φ-circles — a φ-INVARIANT (meridional × S¹) surface; its
one-sided limits are φ-independent by the a.c. leg. Degenerate
axisymmetric operation follows. WITHOUT H-NC the implication FAILS
pointwise: at w_rel² = c² there is a genuine one-parameter kernel
(∂_φρ free; ∂_φw, ∂_φp slaved as above) — azimuthal acoustic
disturbances stationary in the wave frame, the lock-in/resonance
boundary; M0 [T-NSW](a) names this locus as the CJ surface, so the
hypothesis is load-bearing on a named in-scope object, excluded by
H-NC and never by algebra. WITHOUT H-WR the implication fails
DIFFERENTLY, with a LARGER kernel (r2, second kernel family of
record): on any open subset of {w_rel = 0} (local co-rotation,
w ≡ Ωr, hence ∂_φw = 0 there), every sweep term carries the
factor w_rel or ∂_φ(ρ w_rel) = w_rel ∂_φρ + ρ ∂_φw, so
K_ρ = K_u = K_v = K_s = 0 IDENTICALLY, K_Γ = 0 forces only
∂_φp = 0, and K_h0 = 0 follows; the kernel leaves ∂_φρ, ∂_φu,
∂_φv, ∂_φs ALL free — strictly larger than the one-parameter
|w_rel| = c kernel H-NC was minted against, and the r1 G-f
kernel-instance rejector (which tests only the |w_rel| = c
kernel) could NOT have rejected the H-WR omission. QED.

Identification with the standing decomposition: the K-terms ARE the
O(St) sweep of record ([T-NSW]: "the huge relative swirl never
enters rung 2: it IS the O(St) sweep term" — where the O(St)
smallness lives is made precise in S.22 (g3), r1-reformulated: the
swept angle per transit, NOT pointwise smallness of ∂_φV); STAGE 2
of the exact-quotient claim ("the 2-D per-phase marches discard the
θ-coupling — the only approximation in the chain") is hereby given
its precise object list.
Class: K list = DEFINITION (DISTRIBUTIONAL at r3) +
carrier-checked internal consistency of the a.c. part
(completeness = G-f, SCHEMA; the singular-density row-by-row
bookkeeping rides G-f at the same grade); first iff = THEOREM
(bookkeeping by construction, given the singular-density display);
second iff = THEOREM under H-NC + H-WR (front-trace reading, r3)
in the distributional reading — a.c. leg r1-supplied/r2-completed
(the r1 clause silently divided by w_rel), singular leg
r3-supplied (the r2 clause was FALSE on the front-carrying class,
R4-1).
Gamma status: EOS-general (K_h0 uses only dh = T ds + dp/ρ; the
kernel argument uses c² as a free positive symbol; the singular
leg is EOS-free algebra on the flux jumps).
FALSIFIER: (completeness) only the G-f independent re-derivation
can reject — the current C4 CANNOT reject a common-mode
transcription error, and a carrier re-run is a reproduction, not a
rejector (r1); (second iff) THREE one-instance symbolic rejectors,
queued with G-f (spec extended at r2 and r3): the |w_rel| = c
kernel family must satisfy K = 0 at w_rel² = c² and must FAIL
K = 0 for w_rel² ≠ c²; the w_rel = 0 kernel family (∂_φp = 0
only, ∂_φρ/∂_φu/∂_φv/∂_φs free) must satisfy K = 0 at w_rel = 0
and must FAIL K = 0 for w_rel ≠ 0 — the r1 spec tested only the
first kernel and could not reject the H-WR omission; AND (r3,
R4-1) a FRONT instance — the phase-dependent-standoff
meridional-normal-shock family (example (β)) must FAIL K = 0 in
the DISTRIBUTIONAL reading (nonzero front atom) while PASSING the
smooth-region-only check: the one-instance test that separates
the two readings and would have caught the r2 type mismatch at
authoring; PLUS (r3, N8) the K_h0 elimination identity
K_h0 = (w w_rel/r)(∂_φw + w_rel ∂_φρ/ρ) as a one-line sympy
check.

### Theorem D.19 [MS-T-PUMP] (pumping identities: what drives the TRIPLE spread)
For the exact smooth 3-D wave-frame flow, along RELATIVE streamlines
(D_rel := u∂_x + v∂_r + (w_rel/r)∂_φ):
  (i)  D_rel Γ  = −(1/ρ) ∂_φ p           (machine-verified, C1)
  (ii) D_rel h0 = −(Ω/ρ) ∂_φ p           (machine-verified, C2)
  (iii) D_rel s = 0 in smooth regions; s jumps only at fronts
        (reaction zones would also pump s, but reaction is OUTSIDE
        the frozen-composition gas model of record, §0 — named as
        out-of-model physics for orientation only, r1 flag).
Consequently, WITHIN THE FROZEN-EULER WAVE-FRAME MODEL CLASS (the
class in which (i)–(iii) are theorems), the per-phase TRIPLE
spreads are the downstream shadows of exactly the dropped
commutator content: the azimuthal pressure gradient of the wave is
the unique smooth-region source pumping BOTH Γ (as a torque) and
h0 (as unsteady work seen through the wave frame, at rate Ω per
unit Γ-rate), while s is pumped only at fronts. ON REAL DATA the
reading is PRACTICE-grade (r1 scope repair: the previous
"EXACTLY ... measured by D.14" quantified over D.14's inputs,
which are real datasets carrying NON-MODEL sources —
viscous/turbulent shear and parasitic-deflagration heat release —
so the monitor measures the commutator footprint PLUS the
non-model channels; the D.20(a) rothalpy diagnostic is precisely
the row that localizes the non-model part). Model-internally the
mechanism claim stands at THEOREM grade: this is WHY the monitor
is the right stage-A object and why Γ-only monitoring (blind to
the h0 and s legs) falsely licenses (D.15 gives the licensing-side
proof; this gives the mechanism).
Class: THEOREM for (i)–(iii) model-internally (machine-verified
identities C1/C2 from the wave-frame Euler rows; (iii) standard S1
transport); the data-facing bridge paragraph is PRACTICE
(declared, r1). Gamma status: EOS-GENERAL.
FALSIFIER: independent recomputation of (i)–(ii) in any algebra
system (a nonzero difference rejects; a carrier re-run is a
reproduction, not a rejector — r1); or a chamber dataset
exhibiting per-phase Γ spread with ∂_φ p ≡ 0 upstream AND the
non-model channels audited to zero (would require a non-Euler
source and refute the model-internal mechanism).

### Theorem D.20 [MS-T-ROTH] (rothalpy: the exact invariant the reduction splits)
Define the rothalpy I := h0 − Ω Γ. For the exact smooth 3-D
wave-frame flow: D_rel I = 0 (machine-verified, C3 = C2 − Ω·C1;
rejector R1: corrupting the retained geometric coupling −vw/r
breaks the identity — the check can reject). FRONT CLAUSES, PER
TYPE (r3, N3 — a REPAIR-PROPAGATION FAILURE of record: round 1
forced the mass-crossing/contact split into §0, D.2 and D.13, and
this clause was left in the pre-split state, asserting [I] = 0
across ALL wave-steady fronts from an inference valid only when
mass crosses; on a wave-frame-steady CONTACT — and the burnt/fill
interface and triple-point shear layers, §0's OWN examples of
generic per-phase slip surfaces, are precisely such under strict
T0 — RH forces only [p] = 0 and [I] = [h0] − Ω[Γ] is FREE: the r2
clause was false on the class's own C-fronts):
 MASS-CROSSING wave-steady fronts (u_rel,n ≠ 0): [ρ u_rel,n] = 0
 and the energy + θ-momentum jumps give [I] = 0 — I is
 transported across (pen leg, standard steady-rotating-frame RH
 algebra; TWO INDEPENDENT RE-DERIVATIONS OF RECORD this loop,
 both from the UNSTEADY lab-frame RH with front normal speed
 σ_n = Ω r n_θ: m[h0] = −σ_n[p] and m[Γ] = −r n_θ[p] give
 m[I] = m[h0] − Ω m[Γ] = 0, so [I] = 0 whenever m ≠ 0; the
 queued G-a symbolic check remains the carrier-grade discharge).
 Wave-frame CONTACTS (u_rel,n = 0 both sides): only [p] = 0 is
 forced; [h0], [Γ], hence [I], are FREE — I is a
 relative-streamline invariant PER SIDE, BV across the contact
 (mirroring D.2's contact clause).
CONSEQUENCE (the structural statement of record): the exact 3-D
flow does NOT transport h0 and Γ separately — it transports only
the combination I. The per-phase 2.5-D model transports BOTH
separately (Thm D.2): the reduction SPLITS one exact invariant into
two model invariants, and the splitting error is precisely the
pumping pair D.19(i)-(ii) (which are proportional: D_rel h0 =
Ω·D_rel Γ). Two corollaries: (a) on relative-streamline-connected
data NOT CROSSING A WAVE-FRAME CONTACT (r3, N3 — restriction of
record) the per-phase spreads are LINKED: Δh0 = Ω ΔΓ along any
relative streamline bundle with common upstream I (uniform-I
injection); a measured VIOLATION of Δh0 ≈ Ω ΔΓ on such data
localizes non-Euler sources (friction, reaction) OR an unbudgeted
CONTACT CROSSING (r3 — a perfectly Euler-legal wave-frame contact
with [I] ≠ 0 violates the linkage with ZERO non-Euler physics; as
previously specified the row could not distinguish the two — a
rejector firing for the wrong reason, an R5 defect; the
diagnostic row must therefore report the front census's contact
set alongside its verdict) — a free
diagnostic row; (b) uniform I with nonuniform Γ still fails
triple-uniformity (h0′ = ΩΓ′ ≠ 0): rothalpy uniformity does NOT
rescue the N6-2 license — no shortcut past D.14 exists.
Class: THEOREM in smooth regions (machine-verified); THEOREM*
across MASS-CROSSING wave-steady fronts (pen leg, named: standard
RH-in-rotating-frame, twice independently re-derived this loop,
symbolic check queued with the D.6 promotion task); contact
clause THEOREM (r3 — the same two-line jump algebra as D.2's
contact clause). Gamma
status: EOS-GENERAL. Classical anchor (declared, not load-bearing):
rothalpy invariance is the turbomachinery Euler-work theorem (Wu
1952 class); the derivation here is self-contained and machine-
verified. FALSIFIER: independent recomputation of the C3-class
identity + the R1-style corruption check (which CAN reject — it
fires on a corrupted geometric coupling; a plain carrier re-run is
a reproduction, not a rejector — r1); for (a): a frictionless
uniform-I synthetic dataset with CONTACT-FREE bundles (r3)
violating Δh0 = Ω ΔΓ beyond quadrature bars; for the contact
clause (r3): an in-class wave-frame contact carrying [p] ≠ 0, or
one across which [I] = 0 is FORCED by RH alone (either would
refute the r3 split).

### Schema S.22 [MS-S-KBOUND] (the reduction-residual bound — target statement)
TARGET (for the later theorem, named here as the Phase-D handoff):
for data in the standing scope (strict T0, L4 margin m_n > 0
(r3, N2 — the margin of record is the meridional-normal form; on
the planar mid-march stations it coincides with m_x),
through-flow guard), the per-phase family {V(·;ξ)} and the exact
3-D wave-frame solution V₃D satisfy
  d( V₃D(·,·,φ(ξ)), V(·;ξ) ) ≤ C(m_n, data) · ‖K[V₃D]‖
in a norm pair to be fixed. The r1 CANDIDATE ("weighted L² on
sections vs L² of K over the section's meridional domain of
dependence") is RETIRED at r2, refuted twice over: (i)
ILL-DEFINED ON THE DECLARED CLASS — K contains ∂_φ of
piecewise-C¹ fields, so across any front with nonzero azimuthal
normal component (the detonation front itself, the in-scope
object) K is a MEASURE with an atom on the front and
‖K‖_{L²} = +∞ on EVERY in-scope front-carrying solution: the
candidate RHS was infinite exactly on the data the bound exists
for, and it contradicted g3's own r1-reformulated
transit-integrated mandate (a repair-propagation failure); (ii)
GEOMETRICALLY BLIND — the 3-D bicharacteristics wind azimuthally
by O(St) per meridional transit, so section values depend on K
over an azimuthally THICKENED WOUND CONE, not the meridional
section alone; a section-supported RHS misses off-section K
inside the cone. The azimuthal thickness IS the origin of g3's
O(St) factor: g1 and g3 are ONE mechanism, merged at r2. The
candidate CLASS of record is now: SPLIT norms — the smooth part
of K in transit-integrated L¹_x L² over the azimuthally thickened
domain of dependence, PLUS a front term measuring the RH content
of the atoms (front-strength × front measure) — or ALTERNATIVELY
(r3, R4-5(c): the r2 "equivalently" asserted a FALSE equivalence
between inequivalent norm topologies — a split
strong-L¹-plus-atom functional and a negative-order weak norm
control different quantities even on the same K, and weakening
the LEFT side changes the theorem being targeted, not just the
RHS; the pair is a design FORK inside gap (g1), to be decided by
the T-RED owner) a measure-grade norm on K in W^{−1,q},
q < d/(d−1), or a dual-Lipschitz (Kantorovich–Rubinstein) norm
(r3: measures do NOT embed in W^{−1,1} in general — the r2 space
name was wrong), with the LEFT-side distance d
weakened to match (negative-order/weak norm on sections), so
that BOTH sides are finite on front-carrying in-scope data. With
C controlled by the spacelikeness margin (finite domain of
dependence under u > c, D.4) and the S1 front count. ROUTE NAMED:
energy/relative-entropy estimate for the hyperbolic system with K
as a source, marching in x (Li Ta-tsien semiglobal framework, D2.5
import — same conditional as G12-S1); the Γ-independence of the
symbol (D.3(c)) means the swirl-free estimate machinery applies
verbatim with the two extra transport rows. NAMED GAPS: (g1) the
norm pair and the constant's explicit margin dependence —
CONSTRAINED at r2 to the split/measure class displayed above
(the pointwise-L²-on-sections family is refuted, not pending) and
MERGED with g3: the norm choice and the transit-integrated O(St)
factor are one design decision, to be made together by the T-RED
owner;
(g2) front handling in the comparison, SPLIT at r1 (the previous
"weak-strong beyond Lipschitz — not new" mislabeled a KNOWN FATAL
obstruction as a routine conditional):
  (g2a) SHOCKS — RELABELED at r3 (N4: the r1 label "weak-strong
  beyond Lipschitz, fair as stated" MISLABELED the comparison.
  Weak-strong/relative-entropy machinery (Dafermos–DiPerna)
  compares a weak solution against a LIPSCHITZ reference, and the
  "beyond-Lipschitz" extensions (Chen–Frid–Li class) carry a
  shock on ONE side in specific geometries; here the REFERENCE
  V(·;ξ) is itself an S1 solution GENERICALLY CARRYING T-FRONTS —
  §0 admits them, D.2 has a clause for them, the detonation-fed
  standing scope makes them expected — so even in a
  slip-line-free sub-scope the comparison is WEAK-vs-WEAK: no
  multi-D Bressan-type L¹ theory exists, and relative entropy
  degenerates when BOTH sides jump, the shock-shift terms
  uncontrolled — a known structural obstruction was being booked
  as a routine conditional, the r1 lesson of g2b verbatim):
  weak-strong is FAIR only for SHOCK-FREE per-phase references
  (smooth transonic-free nozzle march on L4 data with margin —
  plausibly T-RED's actual use case; the sub-scope is AUDITABLE
  per dataset by the front census of the marched solution);
  shock-carrying references route to FITTED-FRONT machinery
  (Majda stability + Coulombel–Secchi) WITH (g2b);
  (g2b) CONTACTS/SLIP LINES — for multi-D compressible Euler,
  relative-entropy/weak-strong uniqueness is KNOWN TO FAIL on
  contact/vortex-sheet data: admissible weak solutions are
  non-unique by convex integration (Chiodaroli–De Lellis–Kreml
  class; the failure is structural, not an estimate gap), so the
  named relative-entropy route is KNOWN-BROKEN in that regime and
  no constant C(m_n, data) exists along it. The existing
  alternative is fitted-front machinery (Majda shock stability +
  Coulombel–Secchi supersonic vortex sheets — only WEAKLY/
  neutrally stable, with instability windows), a different toolset
  with its own hypotheses. Since per-phase data generically
  contain slip surfaces (§0 C-fronts; D.13 class-adequacy note),
  (g2b) is the sharpest known obstruction on the route and OWNS
  the contact case; the T-RED owner must either fit the contacts
  or declare a slip-line-free sub-scope for the bound;
(g3) REFORMULATED at r1 (the previous wording — smallness through
"∂_φ of the fields, O(St)" — contradicted this document's own O(1)
per-phase statements (D.10/D.12) and D.14's expectation of generic
triple-uniformity failure: both cannot hold with ∂_φV uniformly
small): ∂_φV is O(1) — the wave IS the azimuthal structure, and
φ(ξ) is affine (D.17/D.9(ii)) so per-phase O(1) variation = O(1)
∂_φ. The true small parameter is the SWEPT ANGLE PER MERIDIONAL
TRANSIT, Δφ_transit ~ (w_rel/r)(L/W) = O(St); K is pointwise
LARGE, and the bound is nonvacuous only in TRANSIT-INTEGRATED form
(Gronwall along x within the finite domain of dependence under
u > c), where the x-integration contributes the O(St) factor. This
also reconciles the pair the r1 refuter flagged: the chamber
accumulates many transits (O(1) spreads — consistent with D.14's
expectation), the nozzle march is one short transit (O(St) error)
— the M0-consistent location of the smallness (O(St) quasi-steady
block). Stating the bound in pointwise-∂_φ-weighted form would be
vacuous or self-contradictory; the transit-integrated form is the
target;
(g4) composition with the O(St) corrector row (M0 VI.4bis(ii)) so
the bound and the corrector price the SAME object once, never
twice. OWNER: the formal-first R22 line (T-DISC/T-RED/
M-RED, S-FOUNDATIONS Phase D centerpiece) — this schema is its
input contract. Class: SCHEMA (route + gaps named). Gamma status:
EOS-general route; γ(T) enters only through c in the margin.
FALSIFIER (of the schema's usefulness, per R5): a certified
axisymmetric-data instance (K ≡ 0) where the per-phase family and
a 3-D solve differ beyond solver bars would refute the K ≡ 0
degenerate case and kill the route before the general bound is
attempted.

------------------------------------------------------------------------------
## §6 Claim register

| # | Label | Statement (compressed) | Class | Gamma status | Carrier / falsifier |
|---|-------|------------------------|-------|--------------|---------------------|
| D.1 | MS-DEF-STATE | 2.5-D system, both forms | DEFINITION | EOS-gen; closure γ(T) | C4-gamrow-equiv PASS |
| D.2 | MS-T-TRANSPORT | (s,h0,Γ) streamline invariants, ψ-form under H-FIB (H-REACH sufficient form, r3; union reading across contacts, r2), Bernoulli; ψ existence PROVED (closedness + periods + quasiconvexity, r3); mass-crossing + contact front clauses; s-monotonicity under ARC H-CVX (r3) with mass-flux crossing conventions | THEOREM (H-FIB explicit, r1; H-CVX explicit r2, arc-quantified r3) | EOS-GEN except s-monotonicity: given ARC H-CVX, γ(T)-EXACT unconditional (arc free in-model, r3) | N6-1 carrier; counterexample falsifier; G_fund closed form (pen-executed 2×, carrier queued G-f) |
| D.3 | MS-T-CHAR | pencil/symbol dets (normalized form, r1); sources leave symbol | THEOREM | EOS-GENERAL | independent recomputation (re-run demoted, r1) |
| D.4 | MS-T-SPACE | planar clause: x=const spacelike ⟺ M_x>1; CURVED clause (r3, N2): general axisymmetric surface spacelike ⟺ M_n>1 (meridional normal); every frame; margin m_n (m_x = planar case) | THEOREM (both clauses) | EOS-GENERAL | [T-NSW]+D.3; tilted-element counterexample = audit-wiring rejector (r3) |
| D.5 | MS-T-MARGIN | (i) criterion Γ-free; (ii) swirl cools, margin rises (AUD-c2T, u > 0 — r1); (iii) total-Mach hazard | THEOREM | (ii) γ(T)-EXACT; rest EOS-gen | FD-vs-formula test; exhibit |
| D.6 | MS-T-FLUXNULL | cycle AM flux = J_inj + τ_decl(x) + T_S,decl(x) + T_inj,decl (plane-stress moments, r3; cumulative, r1; a.e.-transversal stations + outward-normal/J_inj-inflow conventions, r2); station-indep = inviscid corollary | THEOREM* (2 conditionals, r1: assembled check + H-AM0 incl. L ∈ AC, r2; H-AM0 audit = concentration tests, r3) | EOS-FREE | panel F1 (gross normalizer \|ρu_xΓ\|, r3); [T-SLRW]; C1/C4 |
| Rmk 3.1 | — | instantaneous balance under strict T0 (J_inj read instantaneously, r3; key renamed from "R3.1", r3/V-5c — collision with the §6-ter objection namespace R3-1..R3-7b) | THEOREM | EOS-FREE (r3) | strict-T0 dataset with L(t) varying beyond bars (r3 — a proof is not a rejector) |
| D.7 | — | non-channels (wave counts etc.) | THEOREM* (as D.6) | EOS-FREE | F1 on mechanism data |
| D.8 | — | torque-channel census (5 channels incl. ¬H-AM0, r1; channel (2) = full boundary deviatoric stress, wall AND cross-plane, r3; exhaustive over extended set) | DEFINITION (+THEOREM* exhaustiveness rel. H-AM0..5) | EOS-FREE | panel F4; H-AM0 concentration audit (r3 — quadrature audit was a non-rejector) |
| D.9 | MS-T-MEASURE | covariance identity (integrated consequence, r1; product-L¹ class + Z_n step, r2); means equal under strict T0; measure discipline | THEOREM (i,ii) | EOS-FREE | panel F2 |
| D.10 | MS-T-SKE | E_θ>0, first-order, unconstrained (exhibit = r-fiberwise θ-halves, r3/R4-5d); "unrecoverable" scoped to vaneless class (r1); TWIN rows | THEOREM + PRACTICE (twin rows) | EOS-FREE | panel A4; T3-CONTROL limb (iv) |
| D.11 | — | counter-wave plain-mean swirl sign | CONJECTURE | EOS-FREE | panel F3 |
| D.12 | — | P2 prohibition + empirical vacuum | PRACTICE (prohibition; r1 relabel on house scale) | EOS-FREE | exhibit a published mean-swirl profile |
| D.13 | MS-DEF-CONTRACT | CycleFamily swirl row w(y;ξ)/Γ, M_in meridional, audits (a)-(c) (margin = m_n on curved Γ_d, r3/N2); recovery uniqueness PROVED for all M (r3/N9c) | DEFINITION (+ THEOREM recovery-uniqueness clause, r3) | γ handle exact | stage-A audits = rejectors; two-recovered-states table instance (r3) |
| Rmk 4.1 | — | h0 must be profile-grade (vacuity of monitor otherwise; key renamed from "R4.1", r3/V-5c) | THEOREM | γ(T)-EXACT (r2 — h0 = h(T0) premise; cell was "—") | state-recovery exhibit |
| D.14 | MS-DEF-TRIPLE | TRIPLE monitor: C1 guard, OBS(ξ) in TV form (r1 — finite on BV; y_min defined, r2), derived tol, G6 rejector; licensing leg = 2-leg gap G-b1/G-b2 (r3 — "form no longer the gap" RETRACTED) | DEFINITION + named SCHEMA gap, TWO legs (sensitivity functional + per-campaign constant, r3/N5); blocking direction unaffected | EOS-gen (+γ(T) in s-term) | its own two-limb falsifier (limb (b) doubles as G-b1's) |
| D.15 | MS-T-GAMONLY | Clause 1: Γ-only falsely licenses; Clause 2: minimality/iff needs variation quantifier (cancellation family, r1) | Clause 1 THEOREM; Clause 2 SCHEMA (r1 split — "machine-verified iff" retracted) | EOS-GENERAL | exhibit alternative reduction / variation-surviving cancellation family |
| D.16 | MS-DEF-AMAUDIT | AM audit row, balance-residual (budget incl. plane-stress moments, r3), gross normalizer \|ρu_xΓ\| (r3/V-3 — backflow-cancellation-free), derived tol, too-clean flag; station-placement rule + signed arming (r2) + backflow arming synthetic (r3) | PRACTICE (rejector-gated) | EOS-FREE | signed arming test (r2) + backflow-bearing synthetic (r3) |
| D.17 | MS-DEF-3DWF | 3-D wave frame; ξ↔φ | DEFINITION | EOS-FREE (r1) | strict-T0 mean-equality test (r1) |
| D.18 | MS-DEF-KRES | commutator terms K — DISTRIBUTIONAL at r3 (a.c. rows + front atoms n_φ[F_φ,rel]; type-checks against S.22) (6 rows, 7 C4 checks — count reconciled r2); internal consistency verified; completeness = G-f; FIRST iff = distributional bookkeeping (r3 — classical reading was false both directions, helical-front counterexamples of record); second iff under H-NC (empty-interior wording, r2) + H-WR (co-rotation kernel r2; front-trace reading r3) with singular leg (r3); K_h0 elimination prefactor corrected w·w_rel/r (r3/N8) | DEFINITION (distributional) + SCHEMA (completeness, r1 downgrade); THEOREM (both iffs as restated, r3) | EOS-GENERAL (singular leg EOS-free) | G-f independent re-derivation + corruption rejectors; THREE kernel/front-instance rejectors (r2, r3) + K_h0 sympy check (r3) |
| D.19 | MS-T-PUMP | ∂_φp pumps Γ and h0 (rate Ω); s at fronts only; data-facing bridge = PRACTICE (r1 scope) | THEOREM model-internal + PRACTICE (bridge) | EOS-GENERAL | independent recomputation; audited-channels dataset test |
| D.20 | MS-T-ROTH | rothalpy D_rel I=0 (smooth machine-verified); front clauses SPLIT per type (r3/N3): [I]=0 mass-crossing only; contacts [I] FREE; corollary (a) restricted to contact-free bundles, verdict text "non-Euler OR contact crossing"; no rothalpy shortcut | THEOREM (smooth + contacts) / THEOREM* (mass-crossing fronts; 2 independent pen re-derivations, carrier queued G-a) | EOS-GENERAL | carrier C3+R1 (PASS, rejector fires); contact-clause falsifier (r3) |
| S.22 | MS-S-KBOUND | reduction-residual bound target; g2 split — g2a RELABELED weak-vs-weak, fair only for shock-free references (r3/N4); g2b = known weak-strong failure on contacts; g3 transit-integrated (r1); g1 candidate retired — split norms OR (fork, r3) W^{−1,q}/dual-Lipschitz, merged with g3 (r2) | SCHEMA | EOS-gen route | K≡0 degenerate-case test |

NAMED GAPS (consolidated; each with OWNER — r1 update): (G-a)
D.6/D.20-fronts promotion — the assembled CV balance +
rotating-frame RH symbolic check (queued of record, one task,
shared; OWNER: the D.6 promotion task, F2 window; r3 note: the
D.20 mass-crossing leg has now been independently pen-re-derived
twice this loop — the carrier-grade check remains the discharge);
(G-b) REFORMULATED at r1, SPLIT INTO TWO LEGS at r3 (N5 — the r1
claim "the FORM is no longer the gap" RETRACTED as an over-claim):
the r1 story stands for the MEASURED OBJECT (the label-scale bound
|dψ/dW| ≤ Ψ/W-scale was FALSE IN FORM — unbounded at interior W
extrema — and is replaced by the TV pairing inside D.14), but the
LICENSING chain needs, beyond it:
 (G-b1) the sensitivity FUNCTIONAL lemma — |objective error| ≤
 S(W_ref, geometry)·OBS on the BV class, W-extremum case treated
 explicitly (prove via ψ-quadrature integration-by-parts, or
 refute and add a W-extremum guard; OWNER: N6 §5 line, gate for
 any LICENSING use of the monitor);
 (G-b2) the per-campaign derived tolerance CONSTANT (SCHEMA leg
 inside a definition; monitor unusable without a campaign-derived
 tol — by design; OWNER: first licensing campaign);
(G-c) S.22 (g1)–(g4) — the reduction-residual bound
itself, with g2b (contacts: known weak-strong failure,
fitted-front alternative) and g3 (transit-integrated smallness)
r1-sharpened, g1 RE-CLASSED at r2 (the L²-on-sections
candidate refuted — atoms of K on fronts + wound-cone blindness;
split/measure-class norms mandated; g1 merged with g3), and at r3
g2a RELABELED (weak-vs-weak on shock-carrying references — N4;
shock-free sub-scope auditable by front census) with the norm
fork (split vs W^{−1,q}/dual-Lipschitz) recorded inside g1
(R4-5c) (OWNER:
R22-F/T-RED line); (G-d) [S-5F] five-field
optimality assembly — UNCHANGED, still the gate for certified
closed-loop design in the generic N6-3 class (honest OPEN of
record; OWNER: F2); (G-e) empirical vacuum — every §3 falsifier
(F1–F4, A4) awaits the first ingested periodic chamber-CFD
dataset; none has ever been computed in the read corpus (OWNER:
first dataset ingestion window); (G-f) NEW at r1, spec EXTENDED at r2 AND r3 — D.18 K-list
completeness: independent re-derivation of the exact 3-D rows
(independent symbol set) + metric-corruption and K-corruption
rejectors + the H-NC AND H-WR kernel-instance rejectors (r2 — the
r1 spec tested only the |w_rel| = c kernel and could not reject
the H-WR omission) + (r3, R4-1) the FRONT-instance rejector (the
phase-dependent-standoff normal-shock family must FAIL
distributional K = 0 and PASS the smooth-region-only check) and
the row-by-row singular-density bookkeeping of the r3
distributional definition + (r3, N8) the K_h0 elimination
identity as a one-line sympy check; the G_fund closed-form
independent recomputation of D.2's H-CVX discharge rides the same
carrier window (r3 note: pen-grade executions of it, two,
already AGREE); until it lands the
completeness claim is SCHEMA and the current C4 is internal
consistency only ([X-O31CS] common-mode pattern; OWNER: carrier
upgrade, same window class as G-a — a carrier edit, gated by the
pinned-env/commit discipline, hence queued not executed in this
doc-repair pass); (G-g) NEW at r1 — D.15 Clause 2
(minimality/iff): the open-set variation-quantifier +
power-separation proof (= the N6-3 strong-only-if SCHEMA leg;
OWNER: N6 doc §5 line, shared falsifier with Clause 2's).

------------------------------------------------------------------------------
## §6-bis Round-1 refutation disposition ledger (r1, 2026-08-17)

Sources: `refute_SWIRL-2D_r1_l0.md` (O1–O12), `refute_SWIRL-2D_r1_l1.md`
(O-1..O-9). Disposition classes: FIXED (repaired at full rigor) /
DOWNGRADED (rigor label honestly lowered) / NAMED-GAP (unfixed,
registered with owner).

| Obj | Item | Disposition |
|-----|------|-------------|
| O1 / O-5 | D.2(ii) fiber connectedness | FIXED — H-FIB hypothesis added (streamtube fibration), counterexample mechanism recorded in-statement; THEOREM retained under H-FIB |
| O2 | D.2 front clause u_n ≠ 0 | FIXED — "transversal" pinned to mass-crossing in §0; u_n ≠ 0 in the statement; contact clause added |
| O3(a) | §3 unsteady function space | FIXED — H-AM0 minted (auditable); D.6 relabeled THEOREM* with TWO named conditionals |
| O3(b) | D.8 exhaustiveness | FIXED — channel (0) ¬H-AM0 added; census re-closed over the extended set |
| O4 / O-4 | D.9(i) "wherever" | FIXED — integrated statement substituted (matches falsifier F2's A2 ≈ −A3) |
| O5 | D.14 OBS = ∞ on BV | FIXED — TV-form OBS (finite on BV; reduces to sup·Ψ on C¹); Δ_* given the screen role; G-b reformulated (form repaired, constant remains the gap) |
| O6 / O-2 | D.15 "machine-verified iff" | DOWNGRADED — split: Clause 1 (false licensing) THEOREM; Clause 2 (minimality/iff) SCHEMA with the load-bearing all-variations quantifier and the cancellation family recorded; machine attribution retracted to identity + 2 controls; → G-g |
| O7 | D.18/C4 common-mode tautology | DOWNGRADED + NAMED-GAP — completeness demoted to SCHEMA; verification restated as internal consistency; independent re-derivation + corruption rejectors = G-f (owner: carrier upgrade, queued — carrier not edited in this doc-repair pass) |
| O-1 | D.18 second iff, CJ-locus kernel | FIXED — H-NC hypothesis added with [T-NSW](a) citation; full proof supplied; kernel family recorded; clause classed THEOREM under H-NC with its own rejector (rejector execution rides G-f) |
| O8 | D.19 bridge overreach | DOWNGRADED — bridge scoped to frozen-Euler model class (THEOREM); data-facing reading declared PRACTICE; non-model channels named |
| O9(a) | D.3(a) marchability conflation | FIXED — renamed symbol invertibility, necessity-not-sufficiency stated |
| O9(b) | "carrier re-run" falsifiers | FIXED — re-run demoted to reproduction in D.3/D.18/D.19/D.20; rejecting tests named (independent recomputation, corruption checks) |
| O10 | §0 axis bound + piecewise-C¹ | FIXED — H-ANN (inf r > 0 on cl(D)); piecewise C¹ defined; front types defined |
| O11 | D.10 "unrecoverable" rider | FIXED — scoped to vaneless axisymmetric class, carried by the N6-2 note |
| O12 / O-9e | D.5(ii) u > 0 | FIXED — hypothesis added, sign-flip for u < 0 stated |
| O-3 | D.6 station-independence viscous | FIXED — τ_decl(x) cumulative; station-independence = inviscid corollary; D.16 per-station budgets |
| O-6 | contacts/slip lines absent | FIXED (class) + NAMED-GAP (comparison) — C-fronts admitted in §0; D.2 contact clause; D.13 class-adequacy note; comparison treatment owned by S.22 (g2b) |
| O-7 | S.22 g2 weak-strong mislabel | FIXED (as schema honesty) — g2 split; Chiodaroli–De Lellis–Kreml failure named; fitted-front (Majda/Coulombel–Secchi, weakly stable) named; owner T-RED |
| O-8 | S.22 g3 scaling contradiction | FIXED (as schema honesty) — small parameter relocated to swept angle per transit; transit-integrated (Gronwall-in-x) form mandated; internal contradiction resolved |
| O-9a | D.17 gamma/falsifier missing | FIXED — EOS-FREE status + strict-T0 mean-equality falsifier added |
| O-9b | D.12 off-scale class | FIXED — relabeled PRACTICE (prohibition, rejector-gated) |
| O-9c | D.19(iii) reaction zones | FIXED — flagged out-of-model (frozen composition), orientation only |
| O-9d | carrier rejector thinness | NAMED-GAP — the K/metric-corruption rejectors are specified inside G-f (owner: carrier upgrade; not executed here — carrier edits are commit-gated) |
| O-9f | D.3 det normalization | FIXED — "normalized as in the carrier" stated; ρ³ prefactor noted |

Unfixed residue total: two named gaps minted (G-f, G-g), both with
owner and specified promotion route; no objection dropped.

------------------------------------------------------------------------------
## §6-ter Round-2 refutation disposition ledger (r2, 2026-08-17)

Source: the round-2 objection list (R3-1..R3-7b, N-1..N-6),
raised against the r1 text. Disposition classes as in §6-bis.
All thirteen objections FIXED at full rigor in-document; no label
lowered this round (one gamma STATUS corrected, which is a label
repair, not a rigor downgrade); no new named gap minted — the
carrier-side executions (kernel rejectors, G_fund recomputation)
ride the EXISTING G-f window per the commit-gated discipline.

| Obj | Item | Disposition |
|-----|------|-------------|
| R3-1 | D.2 "s jumps upward (Lax)" EOS-GENERAL over-label | FIXED — H-CVX (Bethe–Weyl, G_fund > 0) made an explicit hypothesis; gamma status split (s-clause: EOS-general GIVEN H-CVX; γ(T)-EXACT unconditional via the closed form G_fund = 1 + (γ−1)(γ+Tγ′)/(2γ) > 1 under AUD-c2T + AUD-cp); Menikoff–Plohr counterexample recorded; falsifier extended |
| R3-2 | S.22 g1 norm pair ill-defined (K atoms ⟹ ‖K‖_L² = +∞) + g3 contradiction | FIXED (schema honesty) — r1 candidate RETIRED as refuted; split smooth/front-RH or measure/W^{−1,1} class mandated with matched left-side distance; repair-propagation failure named |
| R3-3 | H-AM0 under-specification (L(t) jumps; front AT a station) | FIXED — L ∈ AC on [0, t_c] now in H-AM0; D.6 restated for a.e./transversal stations with one-sided-limit clause; D.16 station-placement rule added |
| R3-4 | §0 c_p > R_g unstated; h-range existence | FIXED — AUD-cp and AUD-hRANGE minted as finite table audits; consumed at D.5(ii)/D.13 with flag-never-extrapolate rejector semantics |
| R3-5 | D.9(i) "any integrable fields" wrong class | FIXED — product-L¹ integrability class stated (L²×L² or H-AM0 L∞ suffice) |
| R3-6 | D.2 contact clause on the union unstated | FIXED — ψ-continuity across fronts proved (Lipschitz from L∞ fields); H-FIB-on-the-union declared as the standing reading |
| R3-7b | H-NC literal pointwise reading | FIXED (with N-1) — restated as empty interior of the sonic locus |
| N-1 | D.18 second iff divides by w_rel | FIXED — H-WR minted (empty-interior co-rotation locus, in-scope via [T-NSW](a)); w_rel = 0 kernel family recorded (larger kernel: only ∂_φp forced); class = THEOREM under H-NC + H-WR; G-f rejector spec extended with the second kernel instance |
| N-2 | S_inj normal orientation / J_inj sign undeclared | FIXED — §3 orientation conventions declared (n outward, traction-on-fluid); J_inj REDEFINED as inflow with explicit minus sign; proof sign bookkeeping closed; D.16 signed arming clause (polarity leg) added |
| N-3 | g1 candidate blind to wound-cone off-section K | FIXED — merged into the g1/g3 reformulation (azimuthally thickened domain of dependence; thickness = the O(St) origin) |
| N-4 | R4.1 gamma status missing (γ(T)-exact step); D.8 body gamma line missing | FIXED — R4.1 status γ(T)-EXACT in body + register; D.8 body line EOS-FREE added |
| N-5 | D.9(ii) traversal count vs t_c = 2π/(nΩ) | FIXED — fundamental-cell sweep corrected; Z_n-periodicity step made explicit (statement unchanged, true as labeled) |
| N-6 | y_min undefined; six-vs-seven count mismatch | FIXED — y_min defined in D.14 (ess inf interface radius, > 0 by H-ANN); D.18 preamble reconciled to six K rows / seven C4 checks |

Unfixed residue this round: NONE new; carrier-side executions
(H-NC/H-WR kernel rejectors, metric/K-corruption checks, G_fund
recomputation) remain inside G-f with owner and window unchanged.

r3 CORRECTION OF RECORD (R4-0, annotation not erasure): the claims
of this section — "All thirteen objections", "no objection
dropped", "NONE new" — were TRUE ONLY RELATIVE TO the absorbed
lists (R3-1..R3-7b = `refute_SWIRL-2D_r3_l0.md`; N-1..N-6 =
`refute_SWIRL-2D_r2_l1.md`). The on-file `refute_SWIRL-2D_r2_l0.md`
(N1–N9, raised against r1, on disk BEFORE the r2 revision per the
state notes of r3_l0/r3_l1/r4_l0) was cited by NO ledger, and its
non-coincident objections remained LIVE in the r2 text. As a
file-level completeness claim this section was FALSE. Consumed at
r3: §6-quater.

------------------------------------------------------------------------------
## §6-quater Round-3 disposition ledger (r3, 2026-08-17):
##   (A) the pending r2_l0 file (N1–N9) + (B) this round's
##   refutations (V-1..V-5, R4-0..R4-5) + orchestration items

Sources: `refute_SWIRL-2D_r2_l0.md` (N1–N9, vs r1 — the pending
file, consumed here per R4-0's precondition on §7);
`refute_SWIRL-2D_r3_l1.md` (V-1..V-5 + orchestration finding, vs
r2 — first round against the r2 text); `refute_SWIRL-2D_r4_l0.md`
(R4-0..R4-5, vs r2). Disposition classes as in §6-bis, plus
ALREADY-LANDED (fixed at r2 via coincidence with an absorbed
objection; verified against the r2 text, not assumed).

### (A) Pending r2_l0 objections N1–N9

| Obj | Item | Disposition |
|-----|------|-------------|
| N1 | D.18 second iff consumes w_rel ≠ 0; co-rotation kernel | ALREADY-LANDED at r2 (coincides with absorbed N-1: H-WR minted, kernel family recorded, G-f spec extended) — r3 adds only the front-trace reading of H-WR consumed by the new singular leg |
| N2 | D.4/D.13(c): planar theorem silently instantiated on curved Γ_d — could LICENSE an ill-posed march | FIXED — D.4 restated with PLANAR + CURVED clauses (M_n criterion, meridional normal; frame invariance re-proved; tilted-element counterexample recorded as audit-wiring rejector); margin of record now m_n (m_x = planar case); D.13(c) repointed; D.5(iii) monitor sentence updated; M0 absorption item added (§7 item 6 — the L4 "u_x − c" certificate is planar-only) |
| N3 | D.20 rothalpy front clause false on wave-frame contacts; corollary (a) mis-attributes contact jumps | FIXED — front clauses split per type ([I] = 0 mass-crossing only, twice independently re-derived; contacts: [I] free, I per-side invariant, BV across); corollary (a) restricted to contact-free bundles; diagnostic verdict text now "non-Euler source OR unbudgeted contact crossing" with the contact census reported |
| N4 | S.22 (g2a) weak-vs-weak, not weak-strong | FIXED (schema honesty) — g2a relabeled: weak-strong fair ONLY for shock-free per-phase references (front-census-auditable sub-scope); shock-carrying references route to fitted-front machinery with g2b |
| N5 | D.14 "form is no longer the gap" over-claims; missing sensitivity FUNCTIONAL | FIXED-BY-DOWNGRADE — the r1 sentence RETRACTED; G-b split into (G-b1) sensitivity-functional lemma (owner: N6 §5 line; gate for licensing use) + (G-b2) per-campaign constant; licensing verdicts carry G-b1 explicitly; blocking direction unaffected |
| N6 | H-AM0 quadrature audit is a non-rejector | FIXED — audit re-specced to concentration tests (solver-resolution Cauchy + collar scaling); ASSUMED-PER-DATASET fallback label mandated where unavailable; D.6 (c2) and D.8 channel (0) updated |
| N7 | H-FIB "equivalently" unproven; "delivers H-FIB there" non sequitur | FIXED — the equivalence DROPPED (nothing used the converse); H-REACH minted as the stated sufficient form (G = streamtube of Γ_d), which is what downstream consumers use; the fronts-reopen-closed-leaves caveat recorded |
| N8 | D.18 K_h0 elimination printed with wrong prefactor Ω·w_rel | FIXED — corrected to (w w_rel/r)(∂_φw + w_rel ∂_φρ/ρ) with the w_rel/r + Ω = w/r step shown; print-error note of record; identity added to the G-f rejector list as a sympy check |
| N9a | "EOS-FREE" status token undefined | FIXED — defined in §0 STATUS RULE as the fourth status (no thermodynamic relation consumed; strictly stronger than EOS-GENERAL) |
| N9b | seven-rows miscount | ALREADY-LANDED at r2 (coincides with absorbed N-6(b): six K rows / seven C4 checks reconciled) |
| N9c | D.13 recovery-uniqueness clause unlabeled, unproved | FIXED — two-line proof written (F(T) = h + M²c²/2, F′ > 0 under AUD-cp + AUD-c2T), valid for ALL M; classed THEOREM γ(T)-EXACT with falsifier; independent confirmation r2_l1 §C-vi cited |
| N9d | y_min undefined | ALREADY-LANDED at r2 (coincides with absorbed N-6(a): y_min defined in D.14) |
| N9e | cancellation family needs Γ₀² large enough | FIXED — proviso stated (finite sup on BV ∩ L∞, large Γ₀ always exists) |
| N9f | Remark 3.1 silently redefines J_inj instantaneously | FIXED — instantaneous reading declared; coincidence with the cycle mean under strict T0 proved by the same one-line argument |

### (B) This round: V-1..V-5 (r3_l1) and R4-0..R4-5 (r4_l0)

| Obj | Item | Disposition |
|-----|------|-------------|
| R4-0 / r3_l1-ORCH | r2 completeness claims coexist with the unconsumed r2_l0 file; §7 must not run before it is consumed | FIXED (audit integrity) — r2_l0 consumed in table (A) above; §6-ter and the r2 header corrected IN PLACE by annotation (never erased); the §7 absorption pass is now UNBLOCKED, with the file census measured this window in the r3 header |
| R4-1 | D.18 both iffs false on the front-carrying class; K read as smooth object in §5 and as measure in S.22 | FIXED — K DEFINED DISTRIBUTIONALLY (a.c. rows + front atoms n_φ[F_φ,rel]); both counterexamples (helical RH front; phase-dependent standoff) recorded in-statement; first iff restated as distributional bookkeeping (TRUE); second iff restated with the r3 SINGULAR LEG proved (removable-or-φ-invariant fronts; H-WR front-trace reading declared); G-f front-instance rejector added; §5/S.22 now type-check |
| R4-2 / V-1 | H-CVX endpoint quantifier insufficient (Hugoniot-arc convexity needed); crossing conventions undefined | FIXED — H-CVX reworded to the ARC form + Menikoff–Plohr weak conditions; mass-flux crossing-direction conventions declared; γ(T)-exact discharge noted arc-free in-model; falsifier updated with the in/out asymmetry test; BZT counterexample class recorded |
| R4-3 | cross-plane/faceplate deviatoric-stress AM flux in no hypothesis, channel, or budget | FIXED — H-AM2 extended to the full ∂CV moment (τ_w, T_S(x), T_inj typed entries); D.6 balance + proof updated; D.8 channel (2) reworded; D.16 residual + tol budget updated; free-slip failure scenario recorded in-hypothesis |
| R4-4 / V-2 | ψ single-valuedness consumed, not proved (closedness across fronts; periods on holes; quasiconvexity) | FIXED — full three-step existence argument written into D.2 clause (a): distributional closedness = weak (E1)/mass RH; vanishing periods via impermeability + weak (E1) on islands; quasiconvex embedding stated; THEOREM label stands |
| R4-5a | Remark 3.1: no gamma status/falsifier in body; register falsifier = "one-line proof" | FIXED — EOS-FREE status + dataset falsifier in body and register |
| R4-5b | D.6 idealized clause "every station" drops admissibility | FIXED — "every ADMISSIBLE station" with one-sided-limit note |
| R4-5c | S.22 "equivalently" false; W^{−1,1} wrong space | FIXED — "alternatively" + fork recorded in g1; W^{−1,q}, q < d/(d−1) / dual-Lipschitz named |
| R4-5d | D.10 equal-mass-flux-halves exhibit does not zero Γ-flux | FIXED — r-fiberwise θ-halves construction substituted |
| V-3 | D.16 normalizer signed in u_x; backflow deflation ⟹ spurious FAIL; arming blind | FIXED — normalizer ⟨∮\|ρ u_x Γ\|dA⟩ (bounds old from above, coincides on clean data); backflow-bearing arming synthetic added; D.6 falsifier normalizer aligned |
| V-4 | τ_w averaging type (instantaneous vs mean) | FIXED — all H-AM2 entries typed as cycle means; strict-T0 coincidence noted |
| V-5a | t_c = 2π/(nΩ) cited to §0 but absent there | FIXED — pinned in §0 notation with the Z_n scope content named |
| V-5b | garbled fragment in D.2 proof (i) | FIXED — deleted |
| V-5c | register key "R3.1" collides with objection namespace | FIXED — register keys renamed "Rmk 3.1" / "Rmk 4.1" |
| V-5d | "per phase" undefined in unsteady §3 | FIXED — "per dataset cycle" |

ORCHESTRATION ITEMS OF RECORD (from the two refuter files, carried
so nothing is lost): (i) r4_l0 reported one planned attack (D.20
contact front clause) dedup'd against pending N3 — correctly, and
N3 is now fixed above; (ii) r3_l1 reported one planned attack
KILLED BY ITS OWN VERIFICATION (KH-instability march ill-posedness
on C-fronts: the steady supersonic march across a linearly
degenerate contact is 1-D-contact-analog well-posed; KH is a
TEMPORAL phenomenon, excluded by the standing strict-T0/H-AM1
scope pin) — recorded here as a no-objection finding of record so
the negative result is not re-litigated; (iii) both refuters
RE-RAN the carrier in the pinned env (OVERALL PASS reproduced,
nothing installed) and both independently re-derived the G_fund
closed form (agree) — reproductions and pen-grade falsifier
executions, logged; carrier-grade checks remain queued in G-f/G-a.

Unfixed residue this round: NO new named gap minted; ONE honest
downgrade (D.14 licensing leg → G-b1/G-b2 split, N5); all other
objections fixed at full rigor in-document; carrier-side
executions (three kernel/front rejectors, metric/K-corruption
checks, K_h0 sympy check, G_fund recomputation, singular-density
bookkeeping) remain inside G-f/G-a with owner and window
unchanged. File census measured this window: NO on-file
refutation of this document remains unconsumed.

------------------------------------------------------------------------------
## §7 Absorption targets (for the session's R4 pass; this doc = staging)

1. M0 VI.1: replace `[vorticity]` with the D.13 row text (w(y;ξ)/Γ
   row + h0 profile promotion + audits (a)-(c)). [F-swirl-1 landed]
2. M0 Part III (or the T-T3-MAP swirl block's neighborhood): land
   the H-AM block + D.6/D.7/D.8 + D.9/D.10/D.11/D.12 as the
   flux-nullity record (panel P1–P4 verbatim landing) with the
   promotion task queued in the plan. [this was the never-landed
   content]
3. N6 doc §5 register: add D.15 cross-reference (false-licensing
   theorem consumes N6-3), D.19/D.20 (pumping/rothalpy — the
   mechanism layer above N6-3), and the D.14 monitor as the
   operational consumer of the obstruction identity.
4. D6 plan: register the D.16 audit row and the D.14 G6 rejector as
   contract rows; register carrier
   phaseD_meanswirl_symcheck.py (suite group assignment at commit;
   baseline row per lint (vii) discipline in the same window).
5. PROTOCOL T3-CONTROL: no change needed — input (5) (E_θ debit
   beside TWIN-C) is D.10's practice row, already of record; this
   doc supplies its theorem backing.
6. (r3, N2) M0 L4-DEFAULT / [D-CONTRACT] neighborhood: the
   standing certificate "u_x − c ≥ δ" is PLANAR-ONLY (D.4 curved
   clause): either pin Γ_d planar as a stated contract hypothesis
   in M0, or land the M_n meridional-normal margin form; the
   D.13(c) row staged here carries m_n and reduces to m_x on
   planar Γ_d — the M0 edit must keep the two consistent.
GATE NOTE (r3, R4-0): this absorption pass was BLOCKED until
`refute_SWIRL-2D_r2_l0.md` was consumed; that precondition is now
DISCHARGED (§6-quater table (A), file census measured in the r3
header) — §7 may run.
