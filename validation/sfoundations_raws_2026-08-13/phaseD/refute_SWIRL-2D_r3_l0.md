# ADVERSARIAL REFUTATION — SWIRL-2D formalization, ROUND 3, lens l0
# (functional-analytic rigor: spaces, operators, compactness, traces,
#  every quantifier)

TARGET: `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
(revision r1, 2026-08-17 08:25, 1173 lines — read in full).

ORCHESTRATION STATE NOTE (measured in-window, SR-12 discipline; not
inherited from the launch brief). The launch brief for this agent said
"Round 1 ... write to refute_SWIRL-2D_r1_l0.md". That instruction is
STALE against the on-disk state, measured this window:
  refute_SWIRL-2D_r1_l0.md   08:09  (O1–O12, ABSORBED by the target's
                                     r1 revision, cited by §6-bis)
  refute_SWIRL-2D_r1_l1.md   08:13  (O-1..O-9, ABSORBED, cited)
  target revised to r1       08:25
  refute_SWIRL-2D_r2_l0.md   08:37  (N1–N9, ON FILE, NOT yet absorbed)
Overwriting r1_l0 would destroy the of-record source of the target's
own §6-bis disposition ledger — a provenance corruption, prohibited by
the repo's anti-entropy discipline. This document is therefore filed as
ROUND 3, lens l0. GROUND RULE: no objection below repeats O1–O12,
O-1..O-9 (absorbed) or N1–N9 (pending); each is NEW — it attacks
either (a) content untouched by r1, (b) the r1 repairs themselves, or
(c) an axis both prior lens audits explicitly declared clean.

EVIDENCE MEASURED THIS WINDOW (pinned env, nothing installed):
- Carrier `phaseD_meanswirl_symcheck.py` RE-RUN: OVERALL PASS
  (C1, C2, C3, C4 ×7, R1 fires with residual 2·v·w·w_rel/r ≠ 0) —
  the header's PASS claim remains true.
- The fundamental-derivative closed form used in R3-1 below was
  MACHINE-CHECKED (sympy, this window): for the §0 thermally-perfect
  closure, G_fund := 1 + (ρ/c)(∂c/∂ρ)_s = 1 + (γ−1)(γ+Tγ′)/(2γ)
  exactly, and dc²/dT = R_g(γ+Tγ′) (AUD-c2T's quantity) reconfirmed.
  Difference simplify → 0 on both.

------------------------------------------------------------------------------
## R3-1 [MED-HIGH — gamma-status over-label inside a THEOREM; the axis
##        both prior lens audits declared clean]
## D.2 front clause "s jumps upward (Lax)" is NOT EOS-GENERAL: entropy
## monotonicity across Lax fronts consumes EOS convexity (Bethe–Weyl,
## G_fund > 0), unstated — false at the statement's own declared
## generality; TRUE under the already-minted AUD-c2T within γ(T)-EXACT

STATEMENT ATTACKED: D.2 [MS-T-TRANSPORT], mass-crossing front clause:
"while s jumps upward (Lax): the triple is invariant along particle
paths EXCEPT s across mass-crossing fronts, which is monotone."
Gamma status of D.2 as declared: "EOS-GENERAL (only dh = T ds + dp/ρ
used)." Register row: EOS-GENERAL.

THE DEFECT. Round 1 lens l0 audited the gamma axis and reported "No
finding on this axis"; round 1 lens l1 reported "the gamma-status
discipline is CLEAN." Both missed this clause. The inference
"Lax-admissible mass-crossing front ⟹ [s] > 0" is NOT a consequence
of RH + Lax alone: it requires convexity of the EOS — positive
fundamental derivative G_fund = 1 + (ρ/c)(∂c/∂ρ)_s > 0 (plus the
standard Bethe subsidiary conditions), which is exactly the
Bethe–Weyl theorem (Bethe 1942; Weyl 1949; the modern of-record
treatment is Menikoff–Plohr, Rev. Mod. Phys. 61 (1989), whose
"anomalous wave" region is precisely G_fund < 0). At the EOS-GENERAL
level this document itself defines — "c² as a free positive symbol"
plus Gibbs — nothing constrains the sign of G_fund, and in a
G_fund < 0 region the entropy change across a weak Lax-compressive
front is NEGATIVE (Δs ∝ G_fund · (Δv)³ to leading order): the clause
is FALSE as quantified. The EOS-GENERAL label on D.2 therefore
over-covers: four of its clauses are genuinely EOS-general; this one
is not.

FALSIFIER MISALIGNMENT (aggravating, R5): D.2's own falsifier invites
"a symbolic counterexample to the mass-crossing front algebra within
RH + n_θ = 0 + u_n ≠ 0". A non-convex-EOS Hugoniot with a
Lax-admissible entropy-decreasing branch IS such a counterexample and
would REJECT the theorem as labeled — the falsifier is honest, the
statement class is wrong. A falsifier that can kill its own statement
on a legal member of the declared hypothesis class is the definition
of an over-label.

WHY THE REPAIR IS CHEAP (constructive leg, machine-checked this
window). For the pinned γ(T)-EXACT closure the fundamental derivative
has the closed form
    G_fund = 1 + (γ−1)(γ + Tγ′) / (2γ)
(sympy check: difference simplifies to 0; derivation: c² = γR_gT,
(∂T/∂ρ)_s = (γ−1)T/ρ for the ideal-gas isentrope, dc/dT =
R_g(γ+Tγ′)/(2c)). Since AUD-c2T is EXACTLY the condition
γ + Tγ′ > 0 (dc²/dT = R_g(γ+Tγ′), reconfirmed symbolically), and
γ > 1, one line gives
    AUD-c2T  ⟹  G_fund > 1 > 0 :
the SAME finite table audit already minted for D.5(ii) discharges
Bethe–Weyl convexity for the whole operating range. No new audit is
needed — only the honest re-scope.

REPAIR (named): re-scope the s-monotonicity clause: either
(a) "γ(T)-EXACT under AUD-c2T" with the one-line lemma
G_fund = 1 + (γ−1)(γ+Tγ′)/(2γ) > 1 recorded (recommended: it
strengthens AUD-c2T into a double-duty audit and costs three lines),
or (b) keep EOS-GENERAL but add the explicit hypothesis "convex EOS
(G_fund > 0, Bethe–Weyl)" as a named cited conditional (then that
clause is THEOREM*). Either way D.2's blanket "Gamma status:
EOS-GENERAL" line and the register row must carve out the clause. If
[C-MAJDA]'s statement already carries a convexity hypothesis, the
clause may instead cite it — but then it must SAY so, and the class
line becomes conditional on [C-MAJDA] for that leg too.

------------------------------------------------------------------------------
## R3-2 [MED-HIGH — S.22 (g1): the candidate norm pair is ILL-DEFINED
## on the declared class; ‖K‖_{L²} = +∞ on every front-carrying
## wave-frame solution — and g1 was not updated when g3 was (an r1
## repair-propagation failure of the same kind as N3)]

STATEMENT ATTACKED: S.22 [MS-S-KBOUND], gap (g1): "the norm pair to
be fixed (candidate: weighted L² on sections vs L² of K over the
section's meridional domain of dependence)".

THE DEFECT (traces/distributions — this lens's home ground). The K
rows (D.18) are ∂_φ-derivative expressions: K_ρ = (1/r)∂_φ(ρw_rel),
K_Γ ∋ ∂_φp, etc. The §0 3-D wave-frame class admits fields piecewise
C¹ with finitely many front hypersurfaces "both types admitted" — and
in the standing scope the PRIMARY front, the detonation wave itself,
has its normal predominantly AZIMUTHAL (the wave spans an
(x,r)-slice: p jumps in φ across it, O(1) per [T-NSW]). Across any
front not tangent to the φ-direction, ∂_φp in the distributional
sense carries a surface measure (an atom ∝ [p]·δ_front): K[V₃D] is a
MEASURE, not an L² function, and
    ‖K[V₃D]‖_{L²} = +∞
for EVERY in-scope wave-frame solution with a front. The candidate
right-hand side of the target inequality is identically infinite on
the entire nonempty part of the declared class, making the target
bound vacuously true and operationally useless — the same defect
class as the original OBS = +∞ on BV (O5), now sitting one level up,
in the Phase-D handoff contract itself.

INTERNAL INCONSISTENCY (repair-propagation): the r1 reformulation of
(g3) mandates the TRANSIT-INTEGRATED form ("K is pointwise LARGE, and
the bound is nonvacuous only in transit-integrated form"). The (g1)
candidate — a pointwise-in-φ L² norm of K on a meridional domain —
was left in the pre-r1 state and contradicts g3's own mandate: a
Gronwall-in-x estimate against an L²-in-section source norm does not
produce the O(St) factor g3 locates in the x-integration, and cannot
even be SET UP when the source is a measure. The same session that
split g2 and reformulated g3 left g1's candidate incoherent with
both.

WHY THIS MATTERS AT SCHEMA GRADE: S.22 is honestly SCHEMA — but a
schema's CONTENT is its named route, and this document's own stated
reason for repairing g3 was that a mis-located smallness "would send
the T-RED owner down a wrong route". The g1 candidate does exactly
that: the T-RED owner following it will attempt an estimate whose
right side is infinite on every datum of interest.

REPAIR (named): restate the candidate as a split norm —
(i) smooth part: L²(or L¹)-in-section of K restricted to the open
complement of the front set, transit-integrated per g3;
(ii) front part: the RH-content of K's atoms (the front-localized
jump terms), priced by the fitted-front machinery ALREADY named in
(g2b) — i.e. g1's front leg merges with g2, which is where front
handling was assigned. Alternatively a negative-order norm
(W^{−1,1} in φ, or measure-norm ‖K‖_{M} with the comparison run in
BV) — but then the left-side distance d(·,·) must be weakened to
match, and that trade-off must be recorded as part of g1, not
discovered by the owner. One of these must replace the current
candidate before the S.22 handoff is consumable.

------------------------------------------------------------------------------
## R3-3 [MED — H-AM0, the r1-minted hypothesis under-specifies exactly
## what the D.6 proof consumes: (a) "piecewise C¹ in t" admits jumps
## in L(t), breaking the storage-cancellation step; (b) "for EVERY
## station x" fails on fronts standing AT a station plane]

STATEMENT ATTACKED: H-AM0 ("L(t) := ∫_CV ρΓ dV is finite and
piecewise C¹ in t") and D.6's proof steps "Cycle-average over t_c:
the storage term integrates to (1/t_c)[L(t+t_c) − L(t)] = 0" and
"through EVERY cross-section".

DEFECT (a) — quantifier/regularity mismatch inside the r1 repair
itself. "Piecewise C¹ in t" is satisfied by functions with finitely
many JUMP discontinuities in t. The proof needs the fundamental
theorem of calculus over a full period: L(t+t_c) − L(t) =
∫ L′(τ)dτ, which requires L ABSOLUTELY CONTINUOUS (continuous +
piecewise C¹ suffices). With a temporal jump in L admitted by the
hypothesis as written, the divergence-theorem balance holds at a.e. t
yet the cycle average of dL/dt need NOT equal (1/t_c)ΔL — the
storage-cancellation line does not follow from the stated
hypothesis. The intended physics (no impulsive concentration) is in
H-AM0's spirit — its "no concentration on lower-dimensional sets"
clause is spatial and does not cover a temporal atom of dL. One-word
repair: "finite, CONTINUOUS, and piecewise C¹ in t" (equivalently:
dL/dt has no atoms).

DEFECT (b) — trace well-definedness at stations. The balance is
asserted "for every station x". If a front hypersurface CONTAINS a
patch of the station plane S(x₀) over a time interval — the standing
normal/oblique shock parked at a throat station is the in-scope
example, not a pathology — then ρu_xΓ has no single-valued trace on
a positive-measure subset of S(x₀) × [0, t_c], and the station
integral ⟨∮_{S(x₀)}·⟩ is ill-defined as written. For all OTHER x the
balance holds, so the content survives; the quantifier does not.
Repair: "for every x whose station plane meets the front set in a
set of surface measure zero for a.e. t" (automatic for a.e. x by
Fubini on the finitely-many-C¹-hypersurfaces class — state that
line), with the two-sided-limit convention declared for the
exceptional stations. D.16's "≥2 stations" audit row should inherit
a one-line "stations chosen off standing fronts" placement rule.

------------------------------------------------------------------------------
## R3-4 [LOW-MED — §0 gas model: c_p(T) > R_g is consumed everywhere
## and stated nowhere]

STATEMENT ATTACKED: §0 GAS MODEL ("h = h(T) with h′(T) = c_p(T) > 0
(table-backed, S11 backend), γ(T) := c_p/(c_p − R_g)").

THE DEFECT. γ(T) is defined, positive, and finite iff c_p(T) > R_g
(equivalently c_v = c_p − R_g > 0); c² = γR_gT > 0 needs the same;
AUD-c2T's γ′ formula divides by (c_p − R_g)²; R3-1's G_fund formula
divides by γ. The declared hypothesis c_p > 0 does NOT give
c_p > R_g, and a table row with c_p ≤ R_g would make γ ≤ 0 or
undefined — silently poisoning every γ(T)-EXACT statement
downstream (D.5(ii), D.14's s-term, D.13 recovery). Physically it
cannot happen for a real gas (c_v > 0 is thermodynamic stability),
but this document's own standard is that table-backed properties get
FINITE AUDITS, not physical folklore: AUD-c2T exists for exactly
this reason. Repair: strengthen the §0 line to
"h′(T) = c_p(T) > R_g on the operating range (table audit,
AUD-cp — same audit family as AUD-c2T)". Two additional lines close
the same family: (i) D.5(ii)/D.13 state recovery inverts h(T) — the
computed h = h0 − W²/2 − Γ²/(2r²) must LIE IN THE RANGE of the
tabulated h(·) for T to exist (existence, prior to the uniqueness
that N9(c) proved); on bounded tables this is a per-datum finite
check that the recovery rejector should name.

------------------------------------------------------------------------------
## R3-5 [LOW — D.9(i): "any integrable fields" is the wrong
## integrability class for a covariance]

STATEMENT ATTACKED: D.9(i) "(exact identity, any integrable fields)".

THE DEFECT. The identity divides by ⟨ρu_x⟩ (guarded) and consumes
⟨ρu_x·u_θ⟩, i.e. the PRODUCT must be integrable over the cycle.
ρu_x ∈ L¹ and u_θ ∈ L¹ do not give ρu_x u_θ ∈ L¹ (classical:
t^{−1/2}-type concentrations pair to a non-integrable product), so
"any integrable fields" is false as a hypothesis for the identity to
be a statement about finite numbers. The fix is free of charge: §3's
own H-AM0 already puts the unsteady fields in L∞, and L∞ × L¹ (or
L² × L²) closes it. Repair: replace "any integrable fields" with
"fields in the H-AM0 class (L∞ suffices)". A quantifier nit, but it
sits inside a labeled THEOREM whose whole content is the identity.

------------------------------------------------------------------------------
## R3-6 [LOW — D.2 contact clause: the domain on which the BV-in-ψ
## statement lives is never declared; H-FIB as stated does not
## quantify over it]

STATEMENT ATTACKED: D.2, contact clause: "under H-FIB the functions
s(ψ), h0(ψ), Γ(ψ) of (ii) remain single-valued in ψ but carry a JUMP
at the contact's ψ-value (BV in ψ rather than C¹)".

THE DEFECT. Statement (ii) and H-FIB are declared on "a simply
connected SMOOTH region G" — by §0's convention, smooth regions are
components of the open complement of the front set, so a contact
curve is NOT inside any G. The BV-in-ψ clause therefore speaks about
a function on a domain (G⁻ ∪ C ∪ G⁺, the union across the contact)
on which neither (ii) nor H-FIB has been stated: H-FIB's "every
level set of ψ in G is connected" says nothing about the level sets
of the UNION, and single-valuedness at ψ ≠ ψ₀ across the union is a
(true, easy) claim that currently has no stated hypothesis carrying
it (it needs H-FIB on the union minus the contact, plus continuity
of ψ across C — the latter is true, dψ's normal component is the
mass flux, continuous and zero at C, but is nowhere said). Repair:
two lines — "ψ extends continuously across C (zero mass flux on
both sides); H-FIB is imposed on G⁻ ∪ C ∪ G⁺'s levels; then q(ψ) is
single-valued off ψ₀ and BV with one jump at ψ₀." As written, the
clause is a correct statement proved on the wrong domain.

------------------------------------------------------------------------------
## R3-7 [MINOR CLUSTER — wording defects that change literal meaning]

(a) §0: "3-D wave-frame fields (§5) are the same class on D × S¹_φ,
    fronts = finitely many C¹ hypersurfaces STEADY IN φ". "Steady in
    φ" literally means φ-INDEPENDENT — which would exclude the
    detonation front itself (a surface with azimuthal normal is
    maximally φ-dependent). Intended meaning: steady in the wave
    frame (fixed in (x, r, φ)-coordinates). One-word fix; note R3-2
    reads the class with the intended meaning (the honest one for
    the scope).
(b) D.18 (H-NC): "|w_rel| ≠ c on every open subset of the domain" —
    literally, every point lies in some open subset, so this reads
    as the POINTWISE condition |w_rel| ≠ c everywhere, which is
    strictly stronger than the parenthetical's intent ("no open
    patch of the relative-sonic locus") and stronger than what the
    proof needs. Write "on no open subset is |w_rel| ≡ c" (empty
    interior of the locus). As stated, the hypothesis text and its
    own gloss disagree — and under the literal reading the CJ locus
    itself (a codimension-1 set in scope per [T-NSW](a)) would
    VIOLATE the hypothesis and void the theorem's applicability.
(c) D.7: "same conditional as D.6" (singular) — D.6 now carries TWO
    named conditionals after the r1 repair (c1 assembled check, c2
    H-AM0); D.7's inheritance line was not repropagated. Write
    "same two conditionals as D.6".

------------------------------------------------------------------------------
## Checks run that produced NO objection (round auditable per house
## discipline)

- Carrier re-run: OVERALL PASS reproduced exactly; R1 residual
  2vw·w_rel/r confirmed nonzero generically.
- D.18 second-iff chain re-derived under H-NC + w_rel ≠ 0: the
  elimination order (K_u,v,s → K_ρ → K_Γ → compatibility
  (w_rel²−c²)∂_φρ = 0 → density of the non-sonic set → back-
  substitution) is sound GIVEN N1's missing w_rel ≠ 0 hypothesis
  (already on file, not re-raised) and modulo N8's printed-prefactor
  error (already on file).
- D.5(ii) chain rule re-verified symbolically this window as a side
  effect of the R3-1 computation (dc²/dT = R_g(γ+Tγ′) confirmed).
- D.9(i) algebra and the r1 integrated consequence: correct (given
  R3-5's integrability class).
- D.14 TV-form OBS: dimensional consistency re-checked (all three
  legs scale as specific energy over W_ref² — dimensionless); the
  TV form is finite on the whole declared BV class as claimed.
- D.6 wall-torque geometric kernel, plane-station n_θ = 0, and the
  RH row [ρΓ(u_n−σ)] + [p r n_θ] = 0 from mass+momentum RH:
  re-derived, correct (given R3-3's station-transversality and
  L-continuity caveats).
- §6-bis ledger audited against both r1 refutation files: every
  round-1 objection has a disposition row; no silent drops found.
- Gamma statuses re-audited line by line UNDER the R3-1 lens:
  besides D.2's front clause (R3-1) no other EOS-GENERAL claim
  consumes convexity or any closure property beyond Gibbs; the
  γ(T)-EXACT markings remain correctly placed.

------------------------------------------------------------------------------
## VERDICT

REPAIRABLE. The r1 revision's core survives a third adversarial pass:
no machine-verified identity, no labeled proof chain, and no monitor
design falls. The genuinely new findings are: one gamma-axis
over-label inside a THEOREM (R3-1 — the axis two prior audits
declared clean; repair is three lines because AUD-c2T already
discharges convexity in-scope, closed form supplied and
machine-checked), one ill-defined candidate norm in the Phase-D
handoff schema (R3-2 — ‖K‖_{L²} = +∞ on every front-carrying
in-scope solution, plus a g1/g3 internal inconsistency left by the
r1 pass), one under-specification inside the r1-minted H-AM0 that
the D.6 proof outruns (R3-3), and three low-severity
hypothesis/quantifier defects (R3-4, R3-5, R3-6) plus a wording
cluster (R3-7) of which (b) — the H-NC phrasing that voids its own
applicability under literal reading — should be fixed with the N1
repair in the same touch. None is fatal; all have named, bounded
repairs; R3-1 and R3-2 should land before absorption (§7 targets 2
and the S.22 handoff would otherwise export, respectively, a false
EOS-GENERAL label into M0 and an unusable estimate contract to the
T-RED owner).
