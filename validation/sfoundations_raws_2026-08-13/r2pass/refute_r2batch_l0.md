# ADVERSARIAL REFUTATION — batched r2 pass, LENS l0
# (hyperbolic-systems / functional-analytic rigor)

Refuter: LENS l0 — function spaces, trace/energy arguments, weak-solution
structure, quantifier discipline, gap accounting.
Date: 2026-08-17. Brief: `r2pass/BRIEF_refuters_r2batch.md` (read in full).
Targets: the 18 delta legs of DOC-1 (`phaseD/phaseD_stop_proof.md` r3),
DOC-2 (`phaseD/phaseD_meanswirl_formalization.md` r3),
DOC-3 (`phaseD_L4_implies_R1.md` r2). All three documents were read IN FULL
(DOC-1 lines 1-2683, DOC-2 lines 1-2001, DOC-3 lines 1-1528), with the
on-file round files consulted for dedup (`refute_S-T0P_r2_l0.md`,
`refute_SWIRL-2D_r4_l0.md` in particular). Objection IDs: L0-<n>.
Label discipline: this is a content pass; no judge-certified rigor class is
re-litigated. Where an objection attacks a disposition, the consumed finding
ID is cited per the brief's dedup rule.

Independent verifications executed at pen grade during this pass (recorded
because they are the strongest attacks that FAILED): the G_fund closed form
1 + (γ−1)(γ+Tγ′)/(2γ) re-derived from ds = c_v dT/T − R dρ/ρ (agrees); the
D.20 mass-crossing identity m[I] = (−σ_n + Ω r n_θ)[p] = 0 re-derived from
the unsteady lab-frame RH (agrees); the L-STD countable-dense/eps_n argument
re-run step by step (sound); Lemma 1.4's shrinkage-flux sign convention
re-derived (sound); Lemma 3.2's bracketing g(p_1) < 0 < g(p_d) re-checked
against the standard wave-curve conventions (sound); the D.18 singular-leg
jump algebra re-run at n_m ≠ 0 (sound there — see L0-4 for where it is not).

==============================================================================
## DOC-1 — phaseD/phaseD_stop_proof.md (revision 3)

------------------------------------------------------------------------------
### Leg 1 — [L-INC] (new lemma, both strata uses)  [§5, ~lines 1333-1377]

**CONFIRMED.** Strongest attacks tried and why they fail:
(a) *Circularity of citing G2 for the (B)-half* — the lemma must PROVE the S1
element satisfies H7', and its stratum-(B) trace clause cites the same G2
items the competitor class assumes. Fails as an attack: G2 is a named
conditional about DM-trace facts, not a class-membership assumption; citing
it makes the (B)-half of the inclusion conditional on the same gap, which is
exactly what the lemma's rigor line declares ("complete modulo the SAME
G2/G9 — no new gap is minted"). Coherent gap accounting, not circularity.
(b) *Sign of the per-front contribution* — I re-derived
−|N_sp| m [g(S)] ≤ 0 for both signs of m from entropy admissibility (S
nondecreasing along particle paths): if m > 0 then [g(S)] ≥ 0; if m < 0 then
[g(S)] ≤ 0; the product −m[g(S)] ≤ 0 either way. Holds; the m = 0 exclusion
(G9) is correctly identified as load-bearing.
(c) *Unverified weak-solution clause* — the proof list ((a) EI-x, (b) traces,
(c) T-periodicity) does not separately verify that q is a weak solution of
(EU); fails as an objection because RH-consistency across every front is an
H6' membership clause, and piecewise-C¹ + RH is classically equivalent to
the weak formulation — the clause is part of the hypothesis, not owed.
(d) *(d2) equality for state-trace fields* — checked: a piecewise-C¹ field
attaining s at Sigma_0 in one-sided trace satisfies the entropy-flux trace
identity with equality; the automaticity note holds.

------------------------------------------------------------------------------
### Leg 2 — [L-STD] final no-topology pointwise argument  [§2.2, ~lines 541-619]

**CONFIRMED.** The full chain was re-executed: (i) mollify in t, per-tau
Fubini spatial null set E_tau, continuity in t upgrading a.e.-t to all-t;
(ii) countable-dense closure: for X off the countable union E, the continuous
function t ↦ Q_eps(X,t) is invariant under a dense translation set, hence
constant (correct: fix t0, the orbit t0 − D is dense and f is constant on it,
continuity finishes); (iii) eps_n union bookkeeping and the L¹_loc-limit
identification of Q_bar as a time-independent field (the constant-in-t fields
form a closed subspace of L¹_loc, so the limit identification is sound);
(iv) the pointwise refinement: the essential discontinuity set N is an
a.e.-class invariant (essential oscillation is preserved by bi-Lipschitz
measure-class-preserving maps composed with the state-space isometry R_phi),
so g_tau N = N; at x off N both q and g_tau q are continuous AT x, and
approximating x by points of the full-measure equality set passes the
equality to the point — no openness of the complement, no closedness of N,
consumed anywhere, exactly as claimed. Strongest attack tried: making the
zero-jump-sheet excision fail (a sheet where the jump vanishes on a dense but
not full subset) — fails because H6' transversality gives nonzero jump on a
relatively open dense subset of genuine sheets and the excision argument
only needs the removable-discontinuity direction. The locally-finite
sheet-family statement (countably many T-translates, finitely many per
compact slab) is correct on the torus count.

------------------------------------------------------------------------------
### Leg 3 — the periodization step  [§4 proof head, ~lines 1166-1176]

**OBJECTION L0-1.** Target: leg 3. Classification: **REPAIR-NEEDED**
(mechanism valid; the written line does not contain the one cancellation
that carries the content, and its literal reading is divergent). This
attacks the adequacy of the r2b-F6 disposition (disposition row §12,
"PERIODIZATION STEP written into the §4 proof head") — the step transcribes
the refuter's own sketch, and the sketch's gap survives transcription.

Verbatim quote (the attacked text):
> "pairing (EI-x) with a partition of unity subordinate to
> {(kT - T, kT + T)}_{k in Z} — each term a legitimate D'(R_t) pairing —
> and summing telescopes by periodicity to the same inequality on
> Omega_march x T_t."

Derivation-level attack. Let μ := d_x eta + d_y q_y + d_z q_z + d_t q_t ≤ 0
in D'(Omega_march × R_t), ψ ≥ 0 a T-periodic torus test, and χ_k = χ_0(·−kT)
the partition. Because V, the composed quadruple, and ψ are all T-periodic,
the pairings ⟨μ, ψχ_k⟩ are EQUAL for all k. "Summing" them over k ∈ Z
therefore produces ±∞ unless the common value is zero — the literal sum
cannot be the mechanism, and nothing "telescopes" among identical terms. The
valid derivation is: (1) a SINGLE window pairing ⟨μ, ψχ_0⟩ ≤ 0 (one
legitimate D'-pairing with a nonnegative test); (2) the periodization
identity ∫_R h(t) χ_0(t) dt = ∫_0^T h(t) dt for T-periodic h (from
Σ_k χ_k ≡ 1), applied to the field terms; and (3) the cutoff-derivative
term ∫_R (q_t∘V) ψ χ_0′ dt, which equals ∫_0^T (q_t∘V) ψ (Σ_k χ_k′) dt = 0
because Σ_k χ_k′ ≡ 0 — THIS cancellation is the entire nontrivial content
of the step (it is what converts the window pairing into the torus pairing),
and the written line does not mention the χ′ term at all. The same
periodization is also silently needed for the EQUALITY pairing of the weak
form of (EU-x) against D_W E(U) in the same display (the text periodizes
only (EI-x)). Held to the document's own "one line, but the line must be
WRITTEN" standard — the standard under which this step was minted — the
line as printed is not the proof. Repair: replace "summing telescopes by
periodicity" by the three-line argument above (single window + Σχ_k ≡ 1 +
Σχ_k′ ≡ 0), and state that the equality case for U rides the same identity.
No statement changes; no label changes.

------------------------------------------------------------------------------
### Leg 4 — [P-HB3] (i') data-space mollification proof  [§6, ~lines 1617-1656]

**CONFIRMED.** Attacks tried:
(a) *Window-edge effects* — the invariance identity on a bounded window
references shifted times outside the window; fails as an attack because the
mollified function's constancy on the window needs only WITHIN-window
comparisons under a dense shift set (for t1, t2 in the window pick τ ≈
t1 − t2 in D), which the L-STD mechanism delivers; the transplant is
legitimate (the co-moving change of variables ξ = θ − OM t is bi-Lipschitz
on the sheared window, and with a = OM b the action becomes pure
t-translation, b ≠ 0 making the translation set all of R).
(b) *Window-independence of the wave count* — checked: for s =
s_hat(θ − OM t) a.e., rho_n s = s a.e. on Gamma_d × I iff s_hat is
2π/n-periodic, for ANY interval I of positive length (the map (θ,t) ↦
θ − OM t pushes full-measure subsets of Gamma_d × I onto full measure in
the ξ-circle). Window-independent as claimed.
(c) *Degenerate case b = 0* — invariance under {a·sig mod 2π : sig ∈ R} is
invariance under ALL rotations (not merely a dense set), so count = ∞ by
the stated convention on every sub-window; no gap.
(d) *sup-definition pathologies of count* — the set {n : rho_n s = s} is
lcm-closed, so the sup is the gcd-order of the azimuthal Fourier support and
an unbounded invariance set forces axisymmetry; the "equivalently" clause is
correct.

------------------------------------------------------------------------------
### Leg 5 — the G8/r2 repricing (gap accounting for [C-XBVP](a'))  [§9 G8 row, ~lines 2024-2063]

**OBJECTION L0-2.** Target: leg 5. Classification: **AMENDMENT/wording**
(two supporting sub-claims are imprecise as printed; the repricing verdict
itself — r2 partial, coercivity OPEN, no named viable abstract-EOS route —
is conservative and SURVIVES, indeed strengthens, under the correction).
This attacks the transcription fidelity of the r2b-F1 disposition.

Verbatim quote (the attacked text):
> "the segment-Taylor integrand D^2 G_U(W_s) is at s = 0 CONGRUENT to the
> M-Hessian of eta (change of variables through M = F_x(W)), hence
> INDEFINITE at subsonic states by [S-XCONV] R1; and the supersonic set
> {u > c} is NON-convex in W (u = m1/rho is a mediant under convex
> combination; two supersonic states can average subsonic): the hull
> obstruction TRANSFERS verbatim to W-space."

Derivation-level attack, two parts.
(a) *The s = 0 congruence proves the wrong thing.* At s = 0 the base point is
W_U with U ∈ K — SUPERSONIC, on the certified branch — so the congruence
D²G_U(W_U) = A_x^T Hess_M(eta)(U) A_x yields the certified DEFINITE block,
not an indefinite one; "indefinite at subsonic states" can never be
instantiated at s = 0 in this chain. The actual failure mechanism for
segment coercivity lives at INTERIOR segment points W_s, where the integrand
D²eta(W_s) − D_W E(U)·D²F_x(W_s) is a TWO-POINT object (U ≠ W_s) that is
congruent to no M-Hessian at all — there is simply no certificate for it,
on or off the branch. As printed, the sentence attaches [S-XCONV] R1 to a
point where it cannot apply and omits the true (and stronger) reason the
lower sandwich is open.
(b) *The mediant clause cannot carry the non-convexity claim.* u = m1/ρ
being a mediant gives u_avg ∈ [min(u_1,u_2), max(u_1,u_2)] — BETWEEN two
supersonic velocities, hence bounded below by the smaller one; subsonicity
of the average requires the SOUND SPEED to rise at the averaged state
(c depends on (ρ, S), and S is not affine in W), which the sentence no
longer says: the source refuter text (refute_S-T0P_r2_l0.md, line ~621) had
"u = m1/rho is a mediant under convex combination AND c moves with
(rho, S)" — the load-bearing second clause was dropped in transcription,
leaving a non-sequitur. The non-convexity claim also has no exhibited pair
(two K-states whose W-average is subsonic), so as stated it is a claim
without falsifier inside a gap row whose function is pricing.
Repair (wording only): restate (a) as "along the segment the integrand is a
two-point object with no definiteness certificate at any s > 0, and at
subsonic W_s even the one-point congruent object is indefinite by [S-XCONV]
R1"; restore the "c moves with (ρ,S)" clause in (b) and either exhibit a
pair or mark the non-convexity as expected-not-exhibited (it is not needed
for the OPEN verdict: the burden of proof is on r2's coercivity, which no
one has). The route-level OPEN conclusion, the audit line, and the gamma
table need no change.

Balance of the leg, CONFIRMED: the falsifier/gate well-definedness
(preimage selection through the G7 r-b instrument, branch-continuation rule,
failure = branch-departure verdict), the G8-falsifier → G7-instrument edge,
the table-enclosure single statement for the three consumers, the dependents
edges G5 → G8 and G4 → G8, and the conditional status of the "removes G7"
claim (correct: with a valid Q_x-sandwich the endgame concludes W_V = W_U
without inversion) are all coherent and correctly priced.

==============================================================================
## DOC-2 — phaseD/phaseD_meanswirl_formalization.md (r3)

------------------------------------------------------------------------------
### Leg 6 — D.18 singular leg: both iff displays + singular-density bookkeeping  [~lines 1299-1499]

Highest-suspicion target, per the brief. Three objections.

**OBJECTION L0-3.** Target: leg 6 (FIRST IFF). Classification:
**BREAKS-THE-LEG** (the biconditional is FALSE in the ⟹ direction, and its
own recorded counterexample (α), two paragraphs above it, violates it).
This attacks the adequacy of the R4-1 disposition ("first iff restated as
distributional bookkeeping (TRUE)" — §6-quater row R4-1): the restatement
is still false in one direction.

Verbatim quote (the attacked text):
> "FIRST IFF (bookkeeping, now true): the wave-frame field solves the exact
> 3-D system DISTRIBUTIONALLY iff each azimuthal section solves the
> per-phase 2.5-D system distributionally (meridional RH included) AND
> K = 0 as a distribution — a.c. part and front atoms both."

Derivation-level attack. K is DEFINED by the decomposition
exact-row(V) = 2.5D-row(V) + K(V) ("Write each exact wave-frame equation as
the corresponding per-phase 2.5-D row PLUS a residual"). Hence, as
distributions, exact-residual(V) = 2.5D-residual(V) + K(V), and
"V solves exact" is equivalent to 2.5D-residual(V) = −K(V) — NOT to the
conjunction [2.5D-residual = 0 AND K = 0]. The ⟸ direction of the printed
iff is trivially true; the ⟹ direction is refuted by the document's OWN
example (α) (same subsection): two constant states across a helical
wave-steady front satisfying the full 3-D RH — the field solves the exact
system distributionally (LHS true), while "each meridional section carries a
front curve whose 2.5-D meridional RH is VIOLATED ... the sections do not
solve the per-phase system" and "in (α)/(β) the singular part is NONZERO"
(RHS false: both conjuncts fail, with the two residual atoms equal and
opposite: [F_m·n̂_m]-part = −n_φ[F_φ,rel]-part under the 3-D RH). A
biconditional whose ⟹ direction is falsified by an example recorded in the
same statement block is broken as printed. Repair (one line, and it is the
statement every consumer actually uses): EITHER state the unconditional
bookkeeping identity "exact-residual = 2.5D-residual + K" and derive from it
the two TRUE conditionals — "given the sections solve the per-phase system:
V solves exact iff K = 0" and "given V solves exact: the sections solve iff
K = 0" — OR keep the conjunction form with the quantifier "for a field
whose sections solve the per-phase system". The second iff is UNAFFECTED
(it already carries the prefix "for a field solving the exact 3-D
wave-frame system"). The register row D.18 ("THEOREM (both iffs as
restated, r3)") inherits the correction for the first iff.

**OBJECTION L0-4.** Target: leg 6 (SECOND IFF singular leg). Classification:
**REPAIR-NEEDED** (the removability algebra is valid only where the front's
meridional normal is nonzero; the pure-azimuthal case is in-class,
uncovered, and the printed chain cannot start there; the conclusion is
recoverable by an argument the document does not make).

Verbatim quote (the attacked text):
> "At a front point with n_φ ≠ 0: [F_φ,rel] = 0 for every row — ...
> Meridional rows (holding by the K = 0 reduction to meridional RH above):
> mass [ρ û] = û[ρ] = 0; momentum [ρ û u + p n̂_x] = u û[ρ] + n̂_x[p] = 0
> and the r-row likewise. CASE û ≠ 0: [ρ] = 0, hence [p] = 0 (n̂ is a unit
> vector ...). CASE û = 0: the momentum rows read n̂_x[p] = n̂_r[p] = 0
> directly, so [p] = 0."

Derivation-level attack. The chain consumes the unit meridional normal
n̂ = n_m/|n_m| and the section-imposed meridional RH. Both are unavailable
at front points with n_m = 0 — locally azimuthal sheets ({φ = const}-type
pieces), which are (i) in-class (§0/§5 admit ALL C¹ wave-steady front
hypersurfaces; nothing excludes n_m = 0), (ii) mass-crossing under the H-WR
front-trace reading (u_rel,n = w_rel± ≠ 0 there), i.e., genuine azimuthal
shocks with [p] ≠ 0, [ρ] ≠ 0, [w] ≠ 0 satisfying the full RH, and (iii)
INVISIBLE to the sections: such a sheet appears in no meridional section as
a front curve, so K carries no meridional atom there and "K = 0 forces the
meridional RH" is vacuous — n̂ is 0/0 and the CASE split cannot begin. At
such points [F_φ,rel] = 0 does follow directly from the exact 3-D RH
(n = ±e_φ), giving [u] = [v] = 0, [ρw_rel] = 0 and g[w] + [p] = 0 — but
this system does NOT close to zero jumps without the meridional rows: it is
exactly the RH system of a nontrivial azimuthal normal shock. The
dichotomy's conclusion ("removable where n_φ ≠ 0") is therefore UNPROVED on
the n_m = 0 stratum. The conclusion is nevertheless recoverable in-class:
off fronts the a.c. leg makes every state φ-independent per side, so
traversing the φ-circle the entropy s is piecewise constant with a strictly
monotone jump (of the sign of the common mass-flux direction — sign(w_rel)
cannot flip across a sheet since g = ρw_rel is continuous and nonzero)
across every admissible azimuthal shock; the circuit must close, so no such
sheet exists — an entropy-circulation argument that consumes the class's
Lax/H-CVX admissibility and appears nowhere in the document. Repair: either
(a) write that circulation argument as the n_m = 0 case of the singular
leg, or (b) exclude n_m = 0 front strata by hypothesis and say so in the
second iff's statement. Until one of these lands, the "THEOREM under
H-NC + H-WR" class of the second iff carries an unnamed case gap.

**OBJECTION L0-5.** Target: leg 6 (singular-density bookkeeping).
Classification: **AMENDMENT/wording**.

Verbatim quote:
> "(singular part) an atom on each front with surface density
> n_φ · [F_φ,rel] per row (up to the declared surface-measure
> normalization) — the n_φ-weighted jump of the relative azimuthal flux:
> exactly the DIFFERENCE between the full 3-D RH residual
> [F_m·n_m] + n_φ[F_φ,rel] and the meridional RH residual [F_m·n_m] that
> the per-phase 2.5-D sections impose."

Attack: no surface-measure normalization is in fact DECLARED anywhere in the
document — the parenthetical references a convention that does not exist.
The point is not cosmetic: the "difference" identity requires the meridional
parts of the two residuals to cancel EXACTLY, and they are born with respect
to DIFFERENT measures and different normal normalizations (the 3-D residual
atom has density [F·n] w.r.t. the r-weighted surface measure with the unit
3-D normal n = (n_m, n_φ); the section-assembled residual atom has density
[F_m·n̂_m] w.r.t. curve-measure × dφ with the unit 2-D normal
n̂_m = n_m/|n_m|); their cancellation is a Jacobian identity
(|n_m| · dS-factor = section-curve factor) that is precisely the content of
the "row-by-row singular-density bookkeeping ... rides the G-f independent
re-derivation". Riding G-f is honest — but the G-f spec extension should
NAME the measure-normalization identity as what must be checked (the front
instance currently specified would exercise it only implicitly), and the
"declared normalization" parenthetical should either point at an actual
declaration or be reworded to "up to the surface-measure normalization
fixed in the G-f computation". Wording repair only; the L0-3/L0-4 logic
above is normalization-independent (it needs only that the factor is a.e.
positive where n_m ≠ 0).

------------------------------------------------------------------------------
### Leg 7 — D.2 psi-existence three-step + H-CVX arc wording  [~lines 243-328]

**OBJECTION L0-6.** Target: leg 7. Classification: **AMENDMENT/wording**
(one parenthetical asserts a false equivalence; everything load-bearing in
the leg is sound).

Verbatim quote:
> "G_fund := 1 + ρ(∂c/∂ρ)_s/c is > 0 at every state of the Hugoniot locus
> joining the two end states (equivalently: the front's wave family is
> genuinely nonlinear along the connecting arc)"

Attack: genuine nonlinearity of the acoustic family is ∇λ·r ≠ 0, which is
equivalent to G_fund ≠ 0 — an EOS with G_fund < 0 along the whole arc is
also genuinely nonlinear there (that is exactly the anomalous/BZT regime the
same clause's r3 repair narrative invokes). "Equivalently" is therefore
false as an equivalence; the correct gloss is "the wave family is genuinely
nonlinear WITH THE CONVEX ORIENTATION (G_fund > 0)". This is the same
quantifier-gloss defect class the r2→r3 H-CVX repair itself prosecuted
(endpoint vs arc), one notch smaller. Repair: one word ("equivalently" →
"i.e. genuinely nonlinear with convex orientation"), no content change.

Balance of the leg, CONFIRMED after full re-derivation:
(1) *Closedness*: dω for the piecewise-C¹ field = (E1) off fronts + the
mass-RH jump row across both admitted front types (contacts give
[ρu_n] = 0 trivially) — distributionally closed, correctly invoking weak
(E1). (2) *Periods*: the period of ω around an internal boundary component
IS the encircled net mass flux; impermeability on the island + weak (E1) in
the intervening annulus kill it; for piecewise-C¹ fields the line integrals
over curves transversal to the finitely many front curves are classically
defined, so the distributional-form/period pairing is well-posed — the
strongest attack I had (period of a merely-distributionally-closed L∞ form
undefined) fails on this class. (3) *Regularity*: ω ∈ L∞ ⇒ ψ ∈ W^{1,∞}(D);
bounded Lipschitz domains ARE quasiconvex (standard), so
W^{1,∞}(D) ↪ C^{0,1}(cl(D)) and ψ is continuous across every front. The
H-CVX γ(T)-exact discharge was INDEPENDENTLY re-derived this pass
(isentrope slope (∂T/∂ρ)_s = (γ−1)T/ρ, dc²/dT = R_g(γ+Tγ′)):
G_fund = 1 + (γ−1)(γ+Tγ′)/(2γ), > 1 under AUD-cp + AUD-c2T — agrees with
the printed closed form at every step; the arc quantifier is then free
in-model exactly as claimed (the closed form holds at every table state).
The arc wording itself (G_fund > 0 along the connecting Hugoniot arc,
Menikoff–Plohr weak conditions, crossing conventions pinned to the
mass-flux direction) is the correct finite-amplitude hypothesis (Bethe/Weyl;
running-state control, not endpoint control) — the r3 repair changed
content, not words, exactly as its falsifier note claims.

------------------------------------------------------------------------------
### Leg 8 — D.16 gross normalizer  [~lines 1187-1203]

**CONFIRMED.** The r3 normalizer ⟨∮|ρ u_x Γ|dA⟩ (i) bounds the r2
denominator ⟨∮ρ u_x|Γ|dA⟩ from above POINTWISE in the integrand
(|u_x| ≥ u_x), hence after both integrations; (ii) coincides with it on
through-flow-only data (u_x > 0 a.e.); (iii) is cancellation-free (a
nonnegative integrand admits no backflow subtraction), so the r2
small-difference-of-two-gross-transports pathology is structurally gone;
(iv) degenerates to 0 only on Γ ≡ 0 data, which is exactly the case the
ε_gross floor guards. Strongest attack tried: the enlarged denominator
weakens the rejector on backflow data unless the tolerance derivation
normalizes its error terms by the SAME gross quantity — checked: tol_AM is
derived per dataset from residual sources and enters the SAME normalized
comparison, so numerator and threshold move together; no false-pass channel
opens. The backflow-bearing arming synthetic (r3) is precisely the
denominator-side test the r2 signed arming lacked — the arming battery is
now two-sided. No objection.

------------------------------------------------------------------------------
### Leg 9 — D.20 contact split (r3 two-line RH algebra)  [~lines 1543-1603]

**CONFIRMED.** Independent re-derivation executed: for a front rotating
rigidly at Ω (wave-steady), normal speed σ_n = Ω r n_θ; unsteady lab-frame
RH gives m[h0] = −σ_n[p] (energy row, using [p u·n] = σ_n[p] + m[p/ρ]) and
m[Γ] = −r n_θ[p] (θ-momentum row, r continuous at the front point); hence
m[I] = m[h0] − Ω m[Γ] = (−σ_n + Ω r n_θ)[p] = 0 — [I] = 0 whenever m ≠ 0,
with NO cancellation left to chance: the identity is exact for every jump
strength and every EOS (EOS-free flux algebra, as the register says).
Contact clause: m = 0 forces only [p] = 0 (momentum row [p]n = 0; the
energy row reads σ_n[p] = 0, nothing more), so [h0], [Γ], [I] free — the
r3 split is the correct per-type statement and the r2 all-fronts [I] = 0
claim was indeed false exactly on C-fronts. The corollary-(a) restriction
(contact-free bundles) and the two-hypothesis verdict text ("non-Euler OR
unbudgeted contact crossing") close the rejector-fires-for-the-wrong-reason
defect. Strongest attack tried: a wave-steady front whose normal speed is
NOT Ω r n_θ (deforming front) — fails: wave-steadiness in the co-rotating
frame is the class hypothesis, and rigid rotation is its lab-frame motion.

------------------------------------------------------------------------------
### Leg 10 — D.10 theta-halves exhibit (Γ-flux zeroing)  [~lines 869-878]

**CONFIRMED.** With ρu_x axisymmetric and u_θ = ±u_0 on θ-halves, the
Γ-flux integrand ρ u_x r u_θ integrates to zero on EVERY r-fiber
(∫_0^{2π} u_θ dθ = 0 at fixed r), so the net flux vanishes identically —
the r-weighting that killed the r1 equal-mass-flux-halves exhibit is now
inert by construction; E_θ = ½∮ρu_x u_0² dA > 0 with u_0 free. The Γ-flux
is LINEAR in u_θ, so superposing the exhibit on any base field shifts E_θ
by O(u_0²) while leaving the net Γ-flux unchanged — "for every value of the
flux-weighted mean ... arbitrarily large E_θ" follows. In-class check: the
two azimuthal discontinuity sheets are admitted front hypersurfaces
(C-fronts). Strongest attack tried: demanding the exhibit be an exact Euler
SOLUTION — fails as an attack: the claim being witnessed is functional
independence of E_θ from D.6's one-scalar constraint, and D.6 constrains
the flux functional, not the field construction; the exhibit's role is
correctly scoped.

------------------------------------------------------------------------------
### Leg 11 — D.8 plane-stress rewording ((0)-channel exhaustiveness)  [~lines 770-810]

**CONFIRMED.** The census is re-closed over {¬H-AM0..¬H-AM5} with channel
(2) now the FULL boundary deviatoric moment (τ_w + T_S + T_inj, typed cycle
means per the extended H-AM2); since D.6's balance carries exactly those
three stress entries as boundary terms of the same divergence-theorem
display, exhaustiveness-relative-to-the-hypothesis-set is tautologically
restored, and the R4-3 failure scenario (free-slip walls + O(1) modeled
plane stress ⇒ red audit with all hypotheses green) is closed: that dataset
now negates H-AM2's declaration clause and lands in channel (2). Strongest
attack tried: (a) partial cancellation of a plane-stress moment against a
wall torque falsely passing — closed by the SUM budget plus the "too clean"
flag; (b) "¬H-AM2" being ill-defined for a declaration-type hypothesis —
the channel is properly read as "stress moments absent from or mis-stated
in the declared budget", which the D.16 residual tests; a wording nicety,
not an objection.

==============================================================================
## DOC-3 — phaseD_L4_implies_R1.md (r2)

------------------------------------------------------------------------------
### Leg 12 — Theorem 1' (collar instantiation)  [§1.6, ~lines 534-544]

**CONFIRMED.** The verbatim-substitution claim was checked against every
consumption of the Theorem 1 proof: the energy identity (EI) is local to
the integration domain; Lemmas 1.1-1.3 are pointwise in n; the boundary
decomposition of ∂C_h = Gamma_I ∪ (Gamma_w ∩ ∂C_h) ∪ Gamma_in^coll is
covered by the same three cases (interface: Lemma 1.2 under (H1.3); wall:
Lemma 1.3 under (H1.2); collar face: zero difference under (ii), or good
sign under (ii')); the coefficients need Lipschitz regularity only on C_h
((H1.1′)); the divergence theorem needs only C_h Lipschitz ((D'')). Nothing
upstream of Gamma_in^coll is consumed — the localization is genuine, and
"no signal enters C_h through Gamma_I" is exactly (OUTFLOW-DISSIPATION) on
the collar. Strongest attack tried: a characteristic or wrongly-signed
collar face — fails: no sign is needed at Gamma_in^coll (the difference
vanishes there by hypothesis, or lies in a nonnegative subspace under
(ii′)); the face's characteristic type is irrelevant to the estimate.

------------------------------------------------------------------------------
### Leg 13 — Lemma 1.4 (finite speed; shrinking-frustum positivity)  [§1.5.2, ~lines 438-466]

**CONFIRMED.** The load-bearing inequality λ_max S + S A(ν) ≥ 0 for every
unit ν was re-derived: N := S^{1/2}A(ν)S^{-1/2} is symmetric (Lemma 1.1)
with spec N = spec A(ν) ⊂ [u·ν − c, u·ν + c] ⊂ [−λ_max, λ_max] on the (G3)
box, so λ_max I + N ≥ 0 and conjugation gives the claim — the Lemma 1.2
similarity argument applied as a lower bound, exactly as cited. The
moving-boundary bookkeeping is right: the shrinking sphere contributes
−λ_max⟨SU,U⟩ (domain-shrinkage flux) and the divergence theorem contributes
−⟨S A(ν_sph)U,U⟩ on the same portion; their SUM is what must be ≥ 0, and
is. ∂O portions: 0 on walls (Lemma 1.3), ≥ 0 on margin-interface portions
(Lemma 1.2 with δ ≥ 0) — the frustum hypothesis ("meets ∂O only in wall or
margin portions") is exactly what excludes uncontrolled faces. Gronwall
with E(t_0) = 0 closes. Strongest attack tried: differentiability of the
shrinking-domain energy when the sphere crosses wall corners — E(t) is
Lipschitz and the identity holds for a.e. t, which the integral form of
Gronwall consumes; no gap.

------------------------------------------------------------------------------
### Leg 14 — Proposition 1'' bootstrap (t* maximality, modulo (H-UP))  [§1.6, ~lines 549-577]

**OBJECTION L0-7.** Target: leg 14. Classification: **BREAKS-THE-LEG**
(the maximality step rests on evaluating a finite-speed conclusion AT the
coupling face, i.e., at distance zero, where it says nothing; the printed
proof does not close. The proposition is likely true and repairable with an
overlapping two-face decomposition — but the repair strengthens the
hypothesis's domain, so this is not a wording fix). This is r2-new text
(the R2-O2 repair) with zero prior adversarial coverage.

Verbatim quote (the attacked text):
> "by (H-UP) finite speed, support entering through Gamma_in^coll after t*
> needs positive time to reach any fixed interior point, so there is
> eps_1 > 0 with U == 0 on Omega_int' x [t*, t* + eps_1] for every
> compactly-contained Omega_int' — in particular the interior-side trace
> feeding Gamma_in^coll stays zero on [t*, t* + eps_1]."

Derivation-level attack, two independent defects in the quoted step.
(a) *Quantifier order*: the eps_1 furnished by finite speed depends on the
subdomain — eps_1(Omega_int') ~ dist(Omega_int', Gamma_in^coll)/λ_glob → 0
as Omega_int' exhausts Omega_int; "there is eps_1 > 0 ... for every
compactly-contained Omega_int'" is false as ordered.
(b) *The fatal one*: Gamma_in^coll is NOT compactly contained in Omega_int —
it is part of ∂Omega_int, at distance ZERO from itself. Finite speed
controls the solution at positive distance from the source face; it can
never control the TRACE ON the face, which is exactly what "in particular
the interior-side trace ... stays zero" asserts. The circularity is
structural: after t*, the collar-side estimate (Theorem 1') takes the
collar-face trace as input, and the interior-side estimate ((H-UP)) takes
the same trace as input — the bootstrap as printed feeds each side's output
into the other's input with no independent control of the trace itself, and
the contradiction with t*-maximality is never actually derived. Note the
sentence would prove too much: the same argument, verbatim, would "prove"
uniqueness for ANY pair of subdomains coupled through a transmission face,
with no transmission condition at all.
Repair route (named, using only ingredients already in the document, but
changing the (H-UP) statement): use TWO faces. For t slightly beyond t*,
Lemma 1.4 (valid on the collar, where (H1.1′) holds) shows U = 0 on the
mid-collar face Gamma^coll_{h/2} for t − t* < (h/2)/λ_max (frusta resting
on zero data at t*, contained in C_h, touching ∂O only at walls/Gamma_I).
Then (i) Theorem 1' on the half-collar C_{h/2} with zero face data gives
U = 0 there, and (ii) (H-UP) — restated on the ENLARGED interior domain
Omega_up \ cl(C_{h/2}), whose extra region (the outer half-collar) is
W^{1,∞} so the S1-class content of the hypothesis is unchanged — gives
U = 0 on the interior with zero face data on Gamma^coll_{h/2}; the union is
Omega_up on [t*, t* + h/(2λ_max)], contradicting maximality with a uniform
eps. The proposition survives; (H-UP) must be restated for the
half-collar-face decomposition (or for a family of collar depths), and the
proof rewritten — the current one is not a proof. Downstream: the "THEOREM
modulo (H-UP)" register row and the composite clause (i)'s Proposition-1''
limb carry this until repaired; Theorem 1' itself (leg 12) is untouched and
remains the unconditional content.

------------------------------------------------------------------------------
### Leg 15 — Lemma 3.2 (monotone intersection; uniform pure-pressurization scope)  [§3.3, ~lines 1078-1100]

**CONFIRMED.** The bracketing was re-derived in the standard wave-curve
convention (1-family through W_1: u_m = u_1 − f_1(p_m); 3-family through
W_d: u_m = u_d + f_d(p_m); f's strictly increasing, vanishing at their own
state pressures — the cited Menikoff–Plohr §V monotone parametrization,
correctly consumed as THEOREM*): with u_d = u_1, matching reads
g(p_m) := f_1(p_m) + f_d(p_m) = 0, g strictly increasing,
g(p_1) = f_d(p_1) < 0 (since p_1 < p_d), g(p_d) = f_1(p_d) > 0 — unique
root in (p_1, p_d), hence Pi_left < Pi_d. No vacuum subtlety can intervene
(the root is bracketed above p_1). The scope declaration is load-bearing
and honest: deceleration events (u_d < u_1 shifts g down, pushing the root
UP — the direction the falsifier's deceleration control tests) and
nonuniform propagation are correctly severed into NG-10, and the (M-b)
surrogate is gated on exactly this lemma's class. Strongest attack tried:
strict monotonicity of g on the rarefaction side of either curve (needed
for uniqueness of the root) — covered by the cited strict parametrization;
and the falsifier genuinely rejects (a single Pi_left ≥ Pi_d kills it).

------------------------------------------------------------------------------
### Leg 16 — Corollary 4 row-(a) in-class transport restatement  [§4, ~lines 1329-1342]

**CONFIRMED.** In the 1-D normal-incidence model class with u_0 > c_0 all
five characteristic speeds are positive; the full state prescribed at
x = 0 determines R_+, R_-, σ (and shear) by downstream constant-speed
transport; existence, uniqueness, continuous dependence are explicit; no
condition is admissible at x = L (zero incoming count, Lemma 1.2); nothing
propagates upstream — R1 ∧ R2 complete IN-CLASS, matching the quadrant's
THEOREM label. The r2 separation of the multi-D reading into a distinct
THEOREM* label (Friedrichs 1954 elliptic-regularization existence +
Lax-Phillips 1960 + Rauch 1985 for the uniformly characteristic wall, PLUS
the NG-3 corner residual, explicitly NOT covered by the in-class label) is
exactly the right quantifier hygiene — the r2 repair's content. Strongest
attack tried: whether "no admissible condition at x = L" secretly breaks
Hadamard well-posedness of the half-open BVP — fails: with zero incoming
characteristics the trivial condition IS the maximal nonnegative one and
the transport construction is the solution operator.

------------------------------------------------------------------------------
### Leg 17 — Remark 1.5.5 (ii') measurable-field restatement  [§1.5.5, ~lines 490-515]

**CONFIRMED.** The r2 restatement supplies exactly what the r1 version
consumed: (a) MEASURABILITY of x ↦ N(x) makes the hypothesis
"(U^(1)−U^(2))(t,x) ∈ N(x) a.e." meaningful, and the integrand
⟨S A(n)U,U⟩(t,x) is then measurable and a.e. ≥ 0 on Gamma_in, entering (EI)
with the good sign (−∫ ≤ 0) — the Gronwall argument is untouched; (b) the
characteristic-inflow scoping is correct and load-bearing: at grazing
(u·n = 0) or sonic-inflow (u·n = −c) points the incoming count jumps and
the acoustic eigenprojectors blow up (the 1/c-factor arithmetic of Lemma
0.2), so "prescribed incoming characteristic components" is pointwise
ill-defined there and the example is properly restricted to the
non-characteristic constant-multiplicity part; (c) the constructed wall
subspace {u′·n = 0} at u-bar·n = 0 is nonnegative by (BQ)
(⟨S A(n)U,U⟩ = (u·n)⟨SU,U⟩ + 2p′(u′·n) = 0) — the exhibit is right; (d)
"No consumer in this document uses (ii′) at a characteristic inflow point"
was verified against the consumers (Theorem 1', Prop 1'' consume (ii)/(ii′)
at the collar face and Gamma_in only). Strongest attack tried: survival of
(ii′) under the H^1 density extension — moot: the C¹ core is where (ii′)
is consumed, and the extension's corner residual is already NG-3.

------------------------------------------------------------------------------
### Leg 18 — the Lopatinskii display  [§4 Claim (i), ~lines 1298-1303]

**CONFIRMED.** At x = L the sole incoming mode is R_- (speed u_0 − c_0 < 0);
the boundary operator R_- − r R_+ = g, restricted to the incoming
amplitude, has coefficient identically 1 — the Lopatinskii determinant in
decoupled characteristic variables is the constant 1, r- and
frequency-independent, hence uniformly bounded away from zero: the display
is exactly the 1-D uniform Kreiss verification, and the document correctly
notes the explicit construction already suffices without invoking it (the
display is honest surplus, not load-bearing). Strongest attack tried:
whether r re-enters the determinant through the outgoing amplitude — it
does not: R_+ is data-side (determined by upstream transport) in the
normal-mode solve at x = L, exactly as the parenthetical says.

==============================================================================
## Summary table

| Leg | Target | Verdict |
|-----|--------|---------|
| 1  | [L-INC] both strata | CONFIRMED |
| 2  | [L-STD] no-topology pointwise + closures | CONFIRMED |
| 3  | periodization step | L0-1 (REPAIR-NEEDED) |
| 4  | [P-HB3](i') data-space mollification | CONFIRMED |
| 5  | G8/r2 repricing | L0-2 (AMENDMENT/wording) |
| 6  | D.18 singular leg + iffs + atoms | L0-3 (BREAKS-THE-LEG), L0-4 (REPAIR-NEEDED), L0-5 (AMENDMENT/wording) |
| 7  | D.2 psi-existence + H-CVX arc | L0-6 (AMENDMENT/wording); core CONFIRMED |
| 8  | D.16 gross normalizer | CONFIRMED |
| 9  | D.20 contact split | CONFIRMED |
| 10 | D.10 theta-halves exhibit | CONFIRMED |
| 11 | D.8 plane-stress rewording | CONFIRMED |
| 12 | Theorem 1' collar | CONFIRMED |
| 13 | Lemma 1.4 finite speed | CONFIRMED |
| 14 | Proposition 1'' bootstrap | L0-7 (BREAKS-THE-LEG) |
| 15 | Lemma 3.2 monotone intersection | CONFIRMED |
| 16 | Corollary 4 row-(a) in-class | CONFIRMED |
| 17 | Remark 1.5.5 (ii') | CONFIRMED |
| 18 | Lopatinskii display | CONFIRMED |

OVERALL: 7 objections, of which 2 BREAKS-THE-LEG.
(L0-3: DOC-2 D.18 first iff false in the ⟹ direction by its own recorded
example (α); L0-7: DOC-3 Proposition 1'' bootstrap evaluates finite speed
at the coupling face itself — the maximality contradiction is never
derived.)

Legs confirmed with no objection: 13/18 (legs 1, 2, 4, 8, 9, 10, 11, 12,
13, 15, 16, 17, 18).

## Falsifier for this pass (how to kill THIS refutation)

- L0-3 dies if, evaluating the document's own example (α) (helical
  wave-steady front satisfying the full 3-D RH, constant states), the
  printed biconditional's RHS is in fact TRUE — i.e. if the sections DO
  solve the per-phase system distributionally or K's singular part IS zero
  there. The document itself asserts the opposite of both in the same
  block; a symbolic instance check (the G-f front-instance rejector run on
  (α)) decides it mechanically.
- L0-7 dies if a proof is exhibited that finite propagation speed for the
  interior problem controls the boundary trace ON Gamma_in^coll itself for
  t > t* without the two-face/overlap construction — i.e. a derivation of
  "the interior-side trace stays zero on [t*, t*+eps_1]" from (H-UP) as
  literally stated. (A repair via the overlap argument CONFIRMS, not kills,
  the objection.)
- L0-1 dies if the literal sum Σ_k ⟨μ, ψχ_k⟩ is shown convergent and equal
  to the torus pairing WITHOUT the Σχ_k′ ≡ 0 cancellation; since the terms
  are equal by periodicity, this requires the common value zero — which is
  the conclusion, not a proof mechanism.
- L0-4 dies if an in-class exclusion of n_m = 0 front strata is exhibited
  in §0/§5 (none was found on a full read), or if the printed algebra is
  shown to run at n_m = 0 (it consumes n̂ = n_m/|n_m|, undefined there).
- L0-2, L0-5, L0-6 are wording objections; each dies by exhibiting the
  missing content in the current text (a declared surface-measure
  normalization; a subsonic-average pair claim carried by the mediant line
  alone; an equivalence proof of GN ⟺ G_fund > 0).
- Global: every verbatim quote above must match the target file exactly;
  any misquote invalidates the corresponding objection (grep-checkable).
