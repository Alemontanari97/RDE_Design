# ADVERSARIAL REFUTATION — SWIRL-2D, round 2, lens 1 (hyperbolic-PDE structure)

TARGET: `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
AT REVISION r1 (the §6-bis disposition ledger consumed
`refute_SWIRL-2D_r1_l0.md` + `refute_SWIRL-2D_r1_l1.md`; this round
attacks the REPAIRED text). Read in full, lines 1–1173.

FILE-NAMING NOTE (of record, per the parallel-sessions / nothing-lost
discipline): the launching brief named this deliverable
`refute_SWIRL-2D_r1_l1.md` and called it "round 1". That file EXISTS,
is of record, and is CONSUMED by the target's §6-bis ledger;
overwriting it would destroy the audit trail of a consumed artifact.
The document is at r1 and `refute_SWIRL-2D_r2_l0.md` (the other lens's
round 2) already exists on disk. This deliverable is therefore ROUND 2
of the until-dry loop for lens 1, filed at the round-correct name.

LENS: characteristics, admissibility, front conditions,
symmetry/group-action correctness, physics of the reduction.
STANDARD: the binding brief — statement truth, every proof step,
hypothesis completeness, rigor-label accuracy (over-label = finding),
variable-gamma status, falsifier rejection capability, ABSENCE.

METHOD OF THIS ROUND (all evidence measured in-window; nothing
inherited from round 1 beyond the ledger's own claims, which were
treated as claims to re-confute):
- Carrier `phaseD_meanswirl_symcheck.py` READ AT SOURCE line-by-line
  and RE-RUN LIVE this window: OVERALL PASS (C1, C2, C3, C4 ×7, R1
  fires with residual 2(w−Ωr)vw/r ≠ 0). Per the target's own r1
  doctrine this re-run is a REPRODUCTION, not a rejector; it verifies
  only that the doc's PASS claim is TRUE.
- M0 anchor for H-NC verified at source: `docs/rde_nozzle_MASTER.md`
  534–535 — "The relative sonic locus |w| = c attached to the wave IS
  the Chapman-Jouguet surface" — the [T-NSW](a) citation is accurate.
- Independent hand re-derivations executed this round (results in §C):
  D.5(ii) full derivative chain; D.18's second-iff kernel algebra
  including the K_h0-automatism; D.20's wave-steady-front rothalpy
  jump from the UNSTEADY lab-frame RH conditions (the doc's pen leg,
  re-proved from scratch); D.9(i); the D.6 CV assembly with explicit
  orientation bookkeeping (this found N-2); the D.13 class-adequacy
  uniqueness claim under AUD-c2T; OBS dimensional consistency and the
  TV majorization directions; the D.15 cancellation-family ODE.

VERDICT (this round): **REPAIRABLE.** No core theorem falls; the r1
repairs held up under independent re-derivation (§C). Round 2 finds
TWO substantive defects — a load-bearing hypothesis (w_rel ≠ 0) still
buried in a proof parenthetical of a THEOREM-classed clause, the exact
defect pattern r1 itself corrected twice elsewhere (O12/O-9e, O-1);
and an undeclared normal-orientation convention that makes D.6's
stated balance disagree in SIGN with its own proof's divergence-
theorem convention, with polarity consequences for the D.16 audit row
— plus four precision/consistency findings. The loop is APPROACHING
DRY: nothing here breaks a statement's truth in-scope; everything is
one-declaration or one-hypothesis repairs.

------------------------------------------------------------------------------
## §C CONFIRMED THIS ROUND (independent re-derivations; loop-dryness evidence)

C-i. D.5(ii): re-derived. With h = h(T), h′ = c_p: ∂T/∂Γ|_{h0,s,u,v,r}
  = −Γ/(r²c_p); ∂M_x/∂Γ = −(u/c²)(dc/dT)(∂T/∂Γ) =
  +uΓ(dc²/dT)/(2c³r²c_p). EXACT match, including both sign clauses
  (u > 0 hypothesis and the u < 0 flip). γ(T)-EXACT label correct.

C-ii. D.18 second iff under H-NC: the whole chain re-derived by hand —
  K_u=K_v=K_s=0 ⟹ ∂_φ(u,v,s)=0 (GIVEN w_rel ≠ 0, see N-1);
  K_ρ ⟹ ρ∂_φw = −w_rel∂_φρ; K_Γ ⟹ ∂_φp = w_rel²∂_φρ; ∂_φs=0 ⟹
  ∂_φp = c²∂_φρ; compatibility (w_rel²−c²)∂_φρ = 0; density of
  {|w_rel|≠c} under H-NC + continuity of ∂_φρ in smooth regions ⟹
  ∂_φρ ≡ 0; and the K_h0-automatism re-verified two independent ways
  (via ∂_φp = −ρw_rel∂_φw and via ∂_φp = w_rel²∂_φρ, both give
  K_h0 = 0 identically). The r1 repair is mathematically sound —
  modulo the hypothesis-line defect N-1.

C-iii. D.20 front leg [I] = 0 (the THEOREM* pen leg): PROVED
  independently this round from the unsteady lab-frame RH conditions.
  With m := ρ(u·n − σ_n) continuous, σ_n = front normal speed:
  energy RH gives m[E] + [p u·n] = σ_n[p]·0-corrected form; computing
  m[h0] = m[E] + [p(u·n − σ_n)] = −σ_n[p]; θ-momentum RH gives
  m[Γ] = −r n_θ[p]; for a front steady in the wave frame
  σ_n = Ω r n_θ, hence m[I] = m[h0] − Ω m[Γ] = −Ωr n_θ[p] +
  Ωr n_θ[p] = 0, so [I] = 0 whenever m ≠ 0. The doc's claim is TRUE
  and its conditional (G-a symbolic check) is DISCHARGEABLE by
  absorbing this five-line derivation; the THEOREM* label is honest
  (conservative) as it stands.

C-iv. D.6 assembly: local conservation ∂_t(ρΓ) + ∇·(ρΓu) + ∂_θp = 0
  re-derived from the cylindrical θ-momentum row (the r-weighting
  absorbs the ρu_ru_θ/r metric term exactly); ∂_θp = ∇·(p r e_θ)
  verified, so the ∮ p r n_θ boundary term is correct; [T-SLRW] wall
  disposal (n ∝ (−R′,1,0)) correct. The assembly is sound EXCEPT the
  orientation declaration, N-2.

C-v. D.9(i) two-line algebra: exact. The r1 integrated-form repair
  (∮⟨ρu_x⟩⟨Γ⟩dA = −∮cov dA, "nonzero SOMEWHERE") is correct and its
  contrapositive (⟨Γ⟩ ≡ 0 forces ∮cov = 0) matches falsifier F2.

C-vi. D.13 class-adequacy note "state recovery on supersonic patches
  is UNIQUE under AUD-c2T": re-derived — solving M² = W²/c² with
  W² = 2(h0 − h(T)) − w² for T: numerator strictly decreasing
  (c_p > 0), and 1/c² strictly decreasing iff dc²/dT > 0 = AUD-c2T,
  so the map T ↦ W²/c² is strictly monotone: uniqueness holds as
  claimed. The r1 addition is correct.

C-vii. D.14 OBS: dimensionally consistent (all three numerator legs
  are specific energies; division by W_ref² is dimensionless); the
  triangle-inequality direction TV(Γ²/2) ≤ sup|Γ|·TV(Γ) is the
  CONSERVATIVE direction, consistent with the declared over-blocking
  design and the D.15 safety note; W_ref > 0 is DELIVERED by the
  through-flow guard (u_n is meridional on an axisymmetric Γ_d, so
  W ≥ |u_n| ≥ δ_tf/ρ_max): the definition is well-posed on its
  licensed domain.

C-viii. D.15 cancellation family: d(Γ²)/dψ = 2y²h0′ integrates to the
  displayed Γ² = Γ₀² + 2∫y²h0′dψ; solvability for any (h0, y) needs
  only Γ₀ large enough to keep Γ² ≥ 0 — the exhibit stands.

C-ix. Lens sweep for missed literature routes (absence axis): the g2b
  convex-integration citation class (Chiodaroli–De Lellis–Kreml) and
  the fitted-front alternative (Majda; Coulombel–Secchi supersonic
  vortex sheets, weakly/neutrally stable with instability windows)
  are correctly characterized at the level used; the r1 admission of
  C-fronts + the S.22 g2 split covers the slip-line obstruction this
  lens flagged in round 1. No NEW ignored route found at the
  statements' actual strength this round.

------------------------------------------------------------------------------
## N-1 [MEDIUM-HIGH — D.18 second iff; hypothesis completeness + label accuracy]
### The THEOREM-classed clause "K ≡ 0 iff ∂_φ ≡ 0 under H-NC" silently
### consumes w_rel ≠ 0; H-NC does NOT imply it, and at w_rel = 0 the
### kernel is LARGER than the CJ-locus kernel the r1 repair was minted for.

The r1 repair states the second iff "under (H-NC) |w_rel| ≠ c on every
open subset" and classes it THEOREM (statement, register row, and G-f
rejector spec all say "under H-NC" only). But the proof's first move is
"with w_rel ≠ 0 (standing scope): K_u = K_v = K_s = 0 force
∂_φu = ∂_φv = ∂_φs = 0" (target ~878–879). That inference DIVIDES BY
w_rel. H-NC excludes open patches of |w_rel| = c; it says NOTHING about
w_rel = 0.

The degeneracy at w_rel = 0 is not smaller than the one at
|w_rel| = c — it is strictly larger. On any open patch where
w_rel ≡ 0 (local co-rotation, w = Ωr: solid-body lock to the wave):
K_u = K_v = K_s = K_ρ-sweep all carry the factor w_rel and are
IDENTICALLY ZERO regardless of ∂_φ(u, v, s, ρ, w); K_Γ = ∂_φp and
K_h0 = (Ω/ρ)∂_φp force only ∂_φp = 0. Hence K ≡ 0 admits a
FOUR-function kernel (∂_φρ, ∂_φu, ∂_φv, ∂_φw free, with ∂_φs slaved
to ∂_φρ through the EOS at fixed p... in fact ∂_φs is also free since
K_s vanishes identically; only ∂_φp = 0 is forced). Compare the
CJ-locus kernel the r1 round found: ONE free function with two slaved.
The pointwise implication K = 0 ⟹ ∂_φ = 0 fails at w_rel = 0 far more
violently than at the locus H-NC was minted to name.

WHY THIS SURVIVES THE IN-SCOPE DEFENSE: yes, the standing scope has
|w_rel| ≈ D_CJ at the interface and the H-NC justification note claims
|w_rel| > c on the marching domain, which implies w_rel ≠ 0 there. But
that is exactly the structure the document's OWN r1 discipline rejects
twice over: (a) O12/O-9e forced u > 0 out of D.5(ii)'s prose and into
the hypothesis line for precisely this reason; (b) O-1 forced the
|w_rel| = c degeneracy out of an unstated assumption and into the
NAMED hypothesis H-NC. The w_rel = 0 degeneracy is the third instance
of the same pattern and got left in a parenthetical. A THEOREM label
whose proof consumes an unstated hypothesis is an over-label per the
binding standard ("an over-label is a finding"), even when the
hypothesis is in-scope-true.

CONSEQUENCE FOR THE G-f REJECTOR SPEC: the queued kernel-instance
rejector ("the kernel family above must satisfy K = 0 at w_rel² = c²
and must FAIL K = 0 for w_rel² ≠ c²") tests ONLY the CJ-locus kernel.
As specified it would PASS on a carrier that wrongly believed
K = 0 ⟹ ∂_φ = 0 wherever w_rel ≠ ±c — i.e. the spec cannot reject the
very error this objection names. The w_rel = 0 kernel instance
(∂_φp = 0, all else free) must be added to the G-f rejector list.

REPAIR ROUTE (full rigor available, no downgrade needed): state the
clause as "under H-NC AND (H-WR) w_rel ≠ 0 throughout each smooth
region" (or: |w_rel| ≥ c ε on the marching domain, citing [T-NSW](a)
as the in-scope justification — the SAME citation currently doing
double duty for H-NC alone); record the w_rel = 0 kernel family next
to the CJ-locus one; extend the G-f rejector spec with the w_rel = 0
instance; update the register row and §6-bis-successor ledger.

FALSIFIER OF THIS OBJECTION: exhibit a derivation of ∂_φu = 0 from
K_u = ρ(w_rel/r)∂_φu = 0 that does not use w_rel ≠ 0. (There is none:
K_u vanishes identically at w_rel = 0.)

------------------------------------------------------------------------------
## N-2 [MEDIUM — D.6 / H-AM4 / H-AM2 / D.16; proof-step orientation + audit polarity]
### The orientation of n in J_inj is UNDECLARED, and under the outward
### convention used by the proof's own divergence-theorem display the
### stated balance has the WRONG SIGN on J_inj.

The proof of D.6 (target ~377–392) writes the CV balance with the
divergence theorem in the standard OUTWARD-normal convention:
  d/dt∫_CV ρΓ dV = −∮_∂CV ρΓ(u·n)dA − ∮_∂CV p r n_θ dA + τ_w + …
and is visibly careful about orientation at the stations ("on S(x_i),
n = ±e_x … the flux term is ∓∮ρu_xΓ dA"). H-AM4 defines
  J_inj := ⟨∮_{S_inj} ρΓ(u·n)dA + ∮_{S_inj} p r n_θ dA⟩
with NO declaration of which way n points on S_inj. Bookkeeping the
assembly explicitly (done by hand this round, CV between S_inj and
S(x), outward n throughout, cycle-averaged storage = 0):
  ⟨∮_{S(x)} ρu_xΓ dA⟩ = −J_inj^{outward} + τ_w .
The STATED balance "= J_inj + τ_w,decl(x)" is therefore true iff
H-AM4's n is the INWARD normal (into the CV) — the opposite of the
convention the display two lines above just used, and nothing in the
text says so. The prose "on S_inj the flux + pressure-torque sum is
the declared J_inj" silently equates an outward-convention RHS
contribution (−∮ − ∮) with a quantity defined by (+∮ + ∮).

WHY THIS MATTERS BEYOND PEDANTRY: J_inj is the declared value of the
"physically weakest hypothesis" (the doc's own words, channel (3)),
and it enters D.16's audit residual R_AM = |flux − J_inj^decl −
τ_decl| LINEARLY IN SIGN. For any dataset with swirled injection
(J_inj ≠ 0) a polarity mismatch between the declarer's convention and
the auditor's convention shifts the residual by 2|J_inj| — enough to
flip PASS/FAIL in either direction. The idealized class (J_inj = 0)
masks the defect, which is exactly why it survived r1. Note also that
the D.16 arming-test falsifier ("a synthetic dataset with an injected
known torque must move R_AM by the known amount") does NOT catch a
convention error that is COMMON-MODE between the synthetic injector
and the audit implementation — the [X-O31CS]/G-f lesson, recurring
here at the audit-row level.

SECONDARY (same repair window): H-AM2's τ_w := ∮_{Σ_w} r(τ·n)_θ dA
also leaves n and the traction convention undeclared; under the
standard continuum reading (n = CV-outward, τ·n = traction exerted on
the fluid by the exterior) the +τ_w sign in the balance is correct,
but the audit row should not depend on the reader supplying the
standard reading.

REPAIR ROUTE: one sentence in H-AM4 ("n = inward unit normal on
S_inj, so J_inj > 0 for wave-ward injected angular momentum") + one in
H-AM2 (traction-on-fluid, CV-outward n); add a SIGNED cross-check to
the D.16 arming test: the injected-torque synthetic must be declared
in the H-AM4 convention by an agent OTHER than the audit implementer,
or the sign convention must be independently derivable from the
dataset (e.g. a case where the physically correct verdict is known).

FALSIFIER OF THIS OBJECTION: exhibit a line in the target that fixes
the orientation of n on S_inj. (Search-proven absent this round:
the only orientation declarations are for S(x_i) and Σ_w geometry.)

------------------------------------------------------------------------------
## N-3 [LOW-MEDIUM — S.22 (g1); schema honesty: the CANDIDATE norm pair
### cannot close, for a reason the hyperbolic lens can name now]

S.22 names as candidate norm pair "weighted L² on sections vs L² of K
over the section's MERIDIONAL domain of dependence". For the 3-D side
of the comparison this is structurally wrong, not merely unfixed: the
bicharacteristics of the 3-D wave-frame system through a point of the
section φ = φ₀ are WOUND in azimuth — over a meridional march of
length L they sweep exactly Δφ_transit ~ (w_rel/r)(L/W) = O(St), the
document's own g3 quantity. The 3-D solution on the section therefore
depends on K over an azimuthally THICKENED domain of thickness O(St)
about φ₀, not over the section's own meridional domain of dependence.
An estimate with the K-norm taken on the section alone would be
refuted by any instance with K supported off-section inside the wound
cone (K there alters V₃D on the section; the candidate RHS is blind
to it). The correct candidate must integrate K over the wound
domain — pleasingly, this is CONSISTENT with g3's transit-integrated
form (the azimuthal thickness IS the O(St) factor's geometric origin)
and makes g1 and g3 the same repair rather than two.

This does not break the SCHEMA label (g1 declares the norm pair open)
— but the schema standard here is "route + named gaps", and a named
CANDIDATE that is already refutable by a nameable mechanism should
carry that mechanism. One-sentence repair inside g1.

FALSIFIER OF THIS OBJECTION: a finite-speed-of-propagation argument
confining the 3-D dependence of section values to the section itself
— impossible unless the azimuthal characteristic speed w_rel is zero,
which contradicts the standing O(1)-large w_rel.

------------------------------------------------------------------------------
## N-4 [LOW — Remark 4.1 (+ D.8 body); the document violates its own
### every-statement rule, the exact defect class r1 fixed as O-9a]

The preamble rule is "EVERY statement carries a VARIABLE-GAMMA STATUS
and a FALSIFIER", and r1 enforced it against D.17 (O-9a). Remark 4.1
is classed THEOREM, has a register row, has a falsifier — and has NO
gamma status, in body or register (the register cell is "—"). It is
not gamma-neutral by inspection either: its content ("per-phase h0 is
CONSTANT in y by construction (single scalar T0 closes the state)")
uses h0 = h(T0), i.e. the thermally-perfect h(T) closure — the honest
status is γ(T)-EXACT (for the h0-recovery step; the vacuity logic
itself is EOS-free). Secondarily, D.8's body carries no gamma line
(the register says EOS-FREE — body/register consistency wanted).
One-line repairs; flagged because an every-statement rule with one
silent exception is no longer a rule an auditor can lean on.

------------------------------------------------------------------------------
## N-5 [LOW — D.9(ii); proof-step precision under n > 1]

The proof of (ii) says "the t-average at fixed θ traverses φ exactly
once per period (n times for n waves) with uniform speed Ω". Under
§0's definition t_c = cycle period, which at a fixed lab point for n
identical waves is 2π/(nΩ), the traversal over one t_c covers a
φ-interval of length 2π/n — NOT once around S¹. The equality with the
FULL frozen-t azimuthal mean then needs the 2π/n-periodicity of the
field in φ (the "n identical waves" hypothesis), a step the proof
does not state; the parenthetical "(n times for n waves)" instead
suggests t_c = 2π/Ω, contradicting §0's t_c. The STATEMENT is true as
labeled (THEOREM under strict T0 with n identical waves); the proof
step is imprecise exactly where the group action (Z_n symmetry vs
full rotation) does the work — the group-action axis of this lens.
Two-line repair: average over 2π/(nΩ), invoke 2π/n-periodicity, done.

------------------------------------------------------------------------------
## N-6 [LOW — D.14 self-containedness + one register inconsistency]

(a) OBS uses y_min, which is never defined in D.14 (nor anywhere in
the target; §0's H-ANN remark alludes to "the 1/y_min² OBS term" but
defines only r_min on the meridional domain). Presumably
y_min := ess inf_y R(y) on Γ_d — but a DEFINITION-classed object of
record must not require the auditor to presume. One line.
(b) D.18's preamble says "carrier C4, seven rows, zero leftover" while
the §6 register row says "K (6 rows)". Both are defensible readings
(7 C4 checks = 6 row-gaps + 1 equivalence check; 6 K objects) but the
mismatch is exactly the kind of count claim SR-12 wants measured, and
the carrier's own PASS line ("C4 x7") is the measured truth: say
"six K rows, seven C4 checks" in both places. Cosmetic.

------------------------------------------------------------------------------
## Round-dryness assessment

Round 2 finds no statement whose TRUTH fails in-scope and no rigor
class that must fall a full level. The two substantive findings (N-1,
N-2) are hypothesis-declaration and convention-declaration defects —
both instances of defect patterns the document itself already
prosecutes (buried load-bearing parentheticals; common-mode-blind
arming tests). If r2 repairs land at the stated routes, this lens
expects round 3 to be at or near dry: the remaining attack surface
would be the named gaps (G-a, G-f, G-g, G-b constant, S.22 g1–g4),
which are honestly labeled as such and are attackable only by
executing them.

DISPOSITION REQUEST (for the r2 ledger): N-1 FIX (hypothesis line +
kernel family + G-f rejector extension); N-2 FIX (two convention
sentences + signed arming clause); N-3 FIX (one sentence in g1,
merging its mechanism with g3); N-4/N-5/N-6 FIX (line-level).
