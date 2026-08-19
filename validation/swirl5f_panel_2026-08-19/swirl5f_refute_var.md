# Adversarial refutation of `swirl5f_var.md` (lens: VAR)

REFEREE ARTIFACT (scratchpad, 2026-08-19). Target read in full; record
sources re-read independently (M0 440-560 + T-T3-MAP/T3-CONTROL
722-825 + VI.4bis/VI.5 1406-1465; T3QS full; N6_swirl full; carrier
`validation/n6_fivefield_adjoint.py` line-by-line; phaseD D.1-D.6,
D.8-D.14 slices, D.17-D.20, S.22; VERDICT §3.2 full table; problem
book §8 St anchors; choice_ledger C51). Machine check
`swirl5f_adjoint_check.py` RE-RUN by me: VERDICT PASS, EXIT 0,
rejector fires (verified, not taken on faith).

METHOD: I re-derived from scratch (i) the full mechanical transpose of
all five columns of the r-weighted (A, B, M), (ii) the advective-form
reduction mod E1, (iii) the θ-momentum adjoint row and the invariant
form (★), (iv) the boundary concomitant (BT), (v) the exit-datum
linear solve INCLUDING its sonic degeneration (kernel + compatibility,
which the target got wrong), (vi) the wall/sliver/Hadamard chain,
(vii) the Green-row sign, (viii) the §8 sign structure. Diffs below.

==============================================================================
## §1 Independent re-derivation of the core (what I CONFIRM)

### 1.1 Transpose of the θ-momentum column (the lens duty)

Column j = 3 (δw) of the r-weighted linearization has the only
nonzero entries A[3,3] = rρu, B[3,3] = rρv, M[2,3] = −2ρw,
M[3,3] = ρv. Hence

  (L*ψ)₃ = −∂_x(rρu ψ₄) − ∂_r(rρv ψ₄) − 2ρw ψ₃ + ρv ψ₄
         = −rρ Dψ₄ − ψ₄·[∂_x(rρu) + ∂_r(rρv)] − 2ρwψ₃ + ρvψ₄
         = ρ(−r Dψ₄ + vψ₄ − 2wψ₃) − ψ₄·E1row .

This is EXACTLY the target's adv₃ with coeff₃ = −ψ₄: (A-w)
Dψ₄ = (vψ₄ − 2wψ₃)/r CONFIRMED, including the sign of the
centrifugal transpose coupling (−2ρwψ₃ from M[2,3] = ∂(−ρw²/r)/∂w
· r = −2ρw — sign re-derived, matches). Invariant form: with
Dr = v,

  D(ψ₄/r) = Dψ₄/r − ψ₄v/r² = (vψ₄ − 2wψ₃)/r² − vψ₄/r²
          = −(2w/r²)ψ₃ = −(2Γ/r³)ψ₃              (★)  CONFIRMED.

### 1.2 The other four advective rows

I re-derived (A-ρ), (A-u), (A-v), (A-p) by hand from the transpose;
all four match the target's displays with the declared E1
coefficients (0, −ψ₂, −ψ₃, −ψ₄, −ψ₅/ρ). In particular for (A-u):
column entries A[0,1] = rρ, A[1,1] = rρu, B[1,1] = rρv, M[0,1] =
∂_x(rρ), M[1,1] = rρu_x, M[2,1] = rρv_x, M[3,1] = rρw_x,
M[4,1] = r(p_x − c²ρ_x) give, mod (−ψ₂)·E1,

  Dψ₂ = −∂_xψ₁ + u_xψ₂ + v_xψ₃ + w_xψ₄ + (p_x − c²ρ_x)ψ₅/ρ ,

and w_x = Γ_x/r at fixed r: the swirl-gradient forcing (Γ_x/r)ψ₄
CONFIRMED with sign +. Same for (A-v) with ρΓ_rψ₄ → +(Γ_r/r)ψ₄.
For (A-p) the E1 bookkeeping requires ∂_x(ru) + ∂_r(rv) =
(E1row − rDρ)/ρ, which produces exactly the target's
(Dρ)(1/ρ − c²_p)ψ₅ term — CONFIRMED. On-shell (A-ρ)′ substitution
CONFIRMED (two lines, as claimed).

### 1.3 Boundary concomitant, exit datum, wall BC, sliver identity

(BT) re-derived row-by-row: CONFIRMED as displayed. Exit matching at
n = e_x gives the five conditions as displayed; solving:
ψ₂ = 1 − uψ₅, ψ₁ = u(1 + uψ₅), and the δρ row then forces

  ψ₅ (u² − c²) = 0 ,                                  (E-solve)

so ψ = (u, 1, 0, 0, 0) uniquely iff u² ≠ c² — claim 7 CONFIRMED
(note for §2/D1: the right-hand side of (E-solve) is EXACTLY ZERO,
not O(1)). Wall BC (W) CONFIRMED. The compressible sliver identity:
wall-fitted divergence of E1 at u_ν = 0 gives rρ(∂_νu)·ν =
−∂_s(rρu_τ) (curvature term dies with u_ν, Lamé h_s = 1 at the
wall), and with the standard linearized slip u̇_ν = (δn)′u_τ −
δn(∂_νu)·ν,

  rρu̇_ν = (δn)′rρu_τ + δn ∂_s(rρu_τ) = ∂_s(rρu_τ δn) ,

CONFIRMED independently; the boxed gradient formula and the endpoint
term follow by parts. G = rρu_τ∂_sψ₁ form-invariance CONFIRMED: my
derivation also produces NO explicit centrifugal boundary term
(flag F1 is honest and, per my re-derivation, resolved in the
target's favor for the exit-plane functional).

### 1.4 Anchors audit

Verbatim/content checks all PASS except where flagged in §2: N6-2
scope note (swirl → no direct axial flux), 5F.1-5F.4 (carrier read
line-by-line; the gauge l(n) swirl-zero claim is in the code at
lines 127-143 with the rank-4 minor certificate), D.2(iii), D.3(c),
D.4 curved clause m_n, D.5(iii) M_tot hazard, D.6/D.9/D.10 (θ-halves
exhibit, TWIN-B prohibition, E_θ definition), D.12 empirical vacuum,
D.13 contract wording "the evaluator carries Γ as its transport
row", D.14 OBS 1/y_min² weighting (phaseD lines 1118-1127), D.17,
D.18 SIX K rows with K_Γ = ρ(w_rel/r)∂_φΓ + ∂_φp, D.19(i)-(ii),
D.20 rothalpy + contact clause, S.22 g2b contact wall, T3QS §2 quote
("D(W) at swirl-free data splits into exactly two mechanisms" —
verbatim), T3QS B2 choked-dam, VI.4bis(i)/(ii)/(iv)/(v), VI.5
sector tournament, problem book St_n O(0.1-1). Judge labels quoted
from VERDICT §3.2 are quoted correctly (D.14 SCHEMA licensing leg
gated on G-b1; D.18 iffs THEOREM* modulo G-f; D.6 THEOREM*).

==============================================================================
## §2 DEFECTS (numbered, severity, fault location, correction)

### D1 [MAJOR — claim 14 + §3.2 remark (ii) + §5 R-4: REFUTED]
CLAIM AT FAULT: "the exit datum ... BLOWS UP like 1/(u² − c²)"
[labeled PROVEN-HERE]; "the adjoint inherits the primal's
sonic-exit fragility in its DATA".
THE ERROR: the solve does NOT blow up. The determinant of the
(ψ₁, ψ₂, ψ₅) core is indeed u² − c² (I verified: det[[1,0,−c²],
[1,u,0],[0,1,u]] = u² − c²), but the Cramer NUMERATOR for ψ₅
vanishes IDENTICALLY: det[[1,0,u],[1,u,2u],[0,1,1]] = −u + u = 0.
Equivalently (E-solve): ψ₅(u² − c²) = 0 with an EXACT zero RHS. The
solution (u, 1, 0, 0, 0) is independent of u − c and extends
CONTINUOUSLY through the sonic point: no quantity in the datum grows
like 1/(u² − c²).
WHAT ACTUALLY HAPPENS AT u = c (my derivation): the system stays
CONSISTENT and acquires a one-parameter solution family
  ψ = (u, 1, 0, 0, 0) + ψ₅·(c², −u, 0, 0, 1),
and the direction (c², −c, 0, 0, 1) ∝ (1, −1/c, 0, 0, 1/c²) is —
after the declared diag(1, r, r, r, r) multiplier dictionary —
EXACTLY the record's terminal gauge l(n) = (1, −rn_x/c, −rn_r/c, 0,
r/c²) at n = e_x (carrier 5F.4). Consistency is guaranteed
structurally: solvability of K(n)ᵀψ = g needs g ⊥ ker K(n); at
u_n = c, ker K(e_x) is the acoustic eigenvector r⁻ = (ρ, −c, 0, 0,
ρc²) (N6-1(c)), and for the thrust covector g = r(u², 2ρu, 0, 0, 1),
  ⟨g, r⁻⟩ = rρ(u² − 2uc + c²) = rρ(u − c)² → 0 at u = c,
which is precisely the record's kernel law ⟨grad g, r⁻⟩ =
ρ(u_n − c)(u − c n_x) — the record ALREADY contained the disproof
of the blow-up claim, in a source the target itself cites (N6-1 via
§3.5). CORRECTED STATEMENT: at a sonic exit point the thrust-adjoint
datum suffers GAUGE NON-UNIQUENESS along l(n) (the Hoffman-counting
direction), not magnitude blow-up; the numerical hazard is 0/0
cancellation noise in a generic linear solve near u = c (an
ill-conditioning of the SOLVE, curable by solving in the quotient
mod l(n)), and the loss of the "δV free at exit" premise itself.
The exit-margin meter survives, but its justification must be
rewritten; claim 14's label PROVEN-HERE is refuted as stated.
(Note the target's §4.2 quotes 5F.4 for the corner count and never
connects it to its own R-4 — the two paragraphs are mutually
inconsistent.)

### D2 [MAJOR — claim 25 / §8.1: over-label; GAP-NAMED]
CLAIM AT FAULT: "recovery asymmetry REPRODUCED in-gradient ...
[PROVEN-HERE (8.1 + duality)] ... VERIFIED, no flag", consumed by
§7.2's retirement claim ("§8 verifies the same sign content is
CONTAINED in dJ/dΣ").
THE GAP: (8.1) is an ISOLATED-STREAMTUBE estimate under fixed
per-tube (ṁ, h0, s, Γ), fixed p_e, and (unstated) fixed v_e. The
duality step ("on the migration family above the directional
derivative is (8.1)") requires that a wall perturbation δn EXISTS
whose actual flow response holds every other tube and each migrated
tube's exit pressure fixed. It generically does NOT: at finite swirl
the exit plane carries the radial-equilibrium gradient ∂p/∂r =
ρu_θ²/r ≠ 0 (the target's own §6(a-2) mechanism), so migrating a
tube outward CHANGES its p_e along the equilibrium profile, and mass
conservation redistributes the neighboring tubes. The Lagrange
identity guarantees dJ·δn = δJ for the ACTUAL response — not for the
idealized migration family. So the chain proves only: (a) dJ/dΣ is
the true derivative (machine-backed), and (b) the record's
per-streamline THEOREM* sign (T-T3-MAP(c), free-vortex class)
matches (8.1)'s sign — a CONSISTENCY check, not an in-gradient
reproduction. CORRECTION: relabel claim 25 to SCALING-ESTIMATE
(sign, per-streamtube, hypotheses incl. δv_e = 0 and per-tube p_e
frozen) + PROVEN-IN-RECORD (T-T3-MAP(c) on free vortex); "VERIFIED,
no flag" must go. §7.2's retirement survives on its STRUCTURAL leg
(within-family tilt is inside dJ by construction; across-family is a
computed ΔJ) but its "verified sign content" sentence inherits the
gap. Also note the unsurfaced hypothesis δv_e = 0 in (8.1) even as
a streamtube statement.

### D3 [MINOR — §3.4 display (G): sign inconsistency]
The Lagrange identity gives 0 = ∮_{∂D}ψᵀK(n)δV = δJ|_{S_e} +
0|_Σ + ∮_{Γ_d}, hence δJ|_data = −∮_{Γ_d}ψᵀK(n)δV dl. The display
(G) omits the minus sign, while the component row two lines later
(dJ/dw = −rρu_nψ₄, correct — my re-derivation agrees) carries it:
the two displays contradict each other; (G) as printed is wrong,
the load-bearing component formula is right. Fix the sign in (G).

### D4 [MINOR — §2.4 N5 + §5 R-1: record hypothesis dropped]
"Swirl COOLS the state ... margin RISES (D.5(ii))" is quoted WITHOUT
the record's u > 0 through-flow hypothesis and AUD-c2T audit
condition. D.5(ii) of record states explicitly that for u < 0 the
sign FLIPS (margin falls) — and that qualifier exists because its
omission was an r1 defect there. Quoting the theorem shorn of the
hypothesis re-creates the repaired defect. Correction: carry
"(u > 0, AUD-c2T)" at both cites.

### D5 [MINOR — §0 / §2.3 / F3: multiplier dictionary
self-inconsistent]
The target's OWN r-weighted E4 = r[ρDw + ρvw/r] = ρ(rDw + vw) =
ρDΓ, i.e. THIS document's fourth row already IS the advective
Γ-transport row — so the multiplier of "the Γ-row" in that
normalization is ψ₄ itself, not ψ₄/r. The dictionary ψ_Γ = ψ₄/r is
correct only against D.1's CONSERVATION-form row ∂_x(rρuΓ) +
∂_r(rρvΓ) = rρDΓ (= r × E4^{here} on solutions of E1). The §0
sentence "ρDΓ = r·(E4-row)/r identically" is a tautology as
printed and pins nothing. Given F3's own warning that "a silent mix
flips r-powers in (N2)/(N3)", the document must pin WHICH record row
the dictionary is against (answer: the D.1 divergence row). The
(★) identity itself is normalization-independent and unaffected.

### D6 [MINOR — §5 R-1: pencil display in the wrong convention]
"det(B − λA) = rρ³(v − λu)³[...]" is the CARRIER's identity
(weights r, ρ, ρ, ρ, 1; 5F.2). For the target's own r-weighted
(A, B) = diag(1, r, r, r, r)·(A, B)_carrier the determinant carries
an extra r⁴: det = r⁵ρ³(...). Criterion unaffected (r > 0), but the
displayed equality is false in the document's own convention —
exactly the r-power bookkeeping class F3 warns about.

### D7 [MINOR — §8.2(iii)/claim 26: inverted ratio in the displayed
scaling]
ΔJ_swirl/J ~ (E_θ/KE)·⟨1 − (r_bell/r_spike)²⟩ is NEGATIVE on its
own premise (spike tubes at SMALLER r ⟹ r_bell/r_spike > 1). With
debit ∝ Γ²/r_e², gap = spike − bell = E_θ,spike·⟨1 −
(r_spike/r_bell)²⟩ > 0: the ratio is upside-down. The 1-4% band is
unaffected in magnitude; the display must be corrected.

### D8 [MINOR — claim 21 / §6(e): proof insufficient as displayed +
label inflation]
"Mean flux nullity survives pumping [PROVEN-HERE, one line:
∮∂_φp dφ = 0]". The zero azimuthal mean of the pumping SOURCE does
not by itself control the mass-flux-weighted mean of Γ at a station
(the weighted mean reads the ρu_x–Γ correlation built up by
transport of the pumped field; a zero-mean source can produce
nonzero flux-weighted correlation). The conclusion HOLDS, but
because D.6's CV balance never used pumping-freeness at all — and
D.6 is THEOREM* (conditionals c1: assembled-balance check queued
G-a; c2: H-AM0). Correct label: PROVEN-IN-RECORD (D.6, THEOREM*,
conditionals inherited), not a one-line PROVEN-HERE.

### D9 [MINOR — §8.2(i): unsurfaced hypothesis]
"NO new small-amplitude nonconvexity or bifurcation of stationary
points" consumes nondegeneracy of the swirl-free reduced Hessian at
the base optimum (a regular-perturbation premise). The proven
content is only ∂J/∂(amplitude) = 0 + smoothness of the quadratic
penalty. Surface the hypothesis or trim the bifurcation clause.

### D10 [MINOR — hypothesis ledger omission]
The whole boundary treatment assumes the census ∂D = Σ ∪ S_e ∪ Γ_d
(∪ axis): NO free (constant-pressure jet) boundary. For the
spike/plug family that §8 discusses, external-expansion
configurations carry a free boundary requiring its own adjoint BC
and shape calculus; the wall-bounded-march assumption is a real
model-class hypothesis of the gradient formula and belongs in §6
(same class as (b) vaneless).

### D11 [MINOR — §2.4 N1 vs §3.3: internal wording tension]
N1: ψ₄ "needs NO boundary condition at wall, axis, or inflow"; §3.3
then imposes ψ₄ = 0 AT THE AXIS (parity/regularity). For a
bell-family solver that IS an enforced boundary condition (of
regularity type). Reword N1 ("no DATA needed; axis condition is a
parity/regularity constraint, §3.3") — as printed the two sections
disagree.

### D12 [OBSERVATION — §5 R-3: amplification exponent uses one leg
of a two-leg loop]
exp(∫2u_θ/(rW)ds) treats the (★) source at loop gain 1 (ψ₃ ~ ψ₄).
The actual feedback closes through (N3): coupled rates
(2u_θ/(rW·r))·r and (∇Γ/(rW)) give closed-loop exponent
~√(2·u_θ/r · Γ_r/r)/W · Δs ≈ √2·(u_θ/W)(Δs/r) for ∇Γ ~ Γ/r —
SMALLER than displayed (0.85-2.8 vs 1-5). Acceptable at
SCALING-ESTIMATE as an upper envelope, but the loop-closure
assumption should be stated; the displayed number is the worst case
of an undeclared worst case.

### D13 [OBSERVATION — §6(c)/§7.4 wording]
"K_Γ, K_h0 nonzero on swirl data": true, but K_h0 = (w_rel/r)∂_φh0
+ (Ω/ρ)∂_φp is generically nonzero ALREADY at swirl-free data (the
work term) — the meridional model drops it too. The genuinely NEW
live content at five fields is the ∂_φΓ sweep leg of K_Γ. Sharpen
to avoid implying the meridional residual had K_h0 = 0.

==============================================================================
## §3 Per-main-claim verdicts

| Target claim (its §9 #) | Verdict |
|---|---|
| 1 (A,B,M) r-weighted linearization | CONFIRMED (hand + machine) |
| 2 advective rows == transpose mod E1 | CONFIRMED (all 5 re-derived by hand) |
| 3 (★) ψ_Γ single-source transport | CONFIRMED; dictionary sentence self-inconsistent (D5) |
| 4 on-shell (A-ρ)′ | CONFIRMED |
| 5 (N1)-(N7) | CONFIRMED except N1 wording (D11), N5 hypothesis drop (D4) |
| 6 wall/axis/inflow BC structure | CONFIRMED |
| 7 exit datum (u,1,0,0,0), unique iff u²≠c² | CONFIRMED |
| 8 Green row dJ/dw = −rρu_nψ₄ | CONFIRMED (final formula); (G) display sign wrong (D3) |
| 9 axis parity | CONFIRMED (parity table re-derived) |
| 10 shape gradient G = rρu_τ∂_sψ₁ + sliver identity | CONFIRMED (independent re-derivation) |
| 11 terminal gauge swirl-zero, corner count | CONFIRMED (carrier read) |
| 12 lip/corner OPEN | CONFIRMED as OPEN |
| 13 pencil/margin/M_tot | CONFIRMED mod D4 (u>0 dropped) + D6 (convention prefactor) |
| 14 sonic-exit 1/(u²−c²) blow-up | **REFUTED** (D1): gauge non-uniqueness along l(n), compatibility exact by the N6-1(c) kernel law; no blow-up |
| 15 R-3 scalings | CONFIRMED at SCALING grade (D12 caveat) |
| 16 contact calculus OPEN | CONFIRMED |
| 17 mixing energy-channel sign + 0.5-2% | CONFIRMED under its stated hypotheses (Gibbs two-liner checks) |
| 18 radial-equilibrium channel, family split | CONFIRMED as SCALING + OPEN (bell net) |
| 19 R_AM mixing-blindness | CONFIRMED (wall-shear exclusion declared) |
| 20 ledger rows (b)-(i) | CONFIRMED; ADD free-boundary census row (D10) |
| 21 nullity survives pumping | GAP-NAMED (D8): conclusion holds via D.6 THEOREM*; the one-line proof is insufficient and the label inflates |
| 22 pumping O(St·decay) | CONFIRMED as SCALING with declared spread |
| 23 retire/remain analysis | CONFIRMED at role level; §7.2's "verified sign content" leg inherits D2 |
| 24 irreducible rows | CONFIRMED |
| 25 asymmetry reproduced in-gradient | **GAP-NAMED** (D2): duality-realizability step unproven; downgrade to SCALING + record consistency; "VERIFIED, no flag" withdrawn |
| 26 landscape derivatives + anisotropy | CONFIRMED (derivatives) mod D7 (inverted ratio) + D9 (hypothesis) |
| 27 / F2 T3QS license gap | CONFIRMED (quote verified; cautious direction correct) |
| F1 no explicit centrifugal wall term | CONFIRMED by my independent derivation (reconciliation still owed at absorption, as the target says) |
| F3 dictionary must be carried | CONFIRMED — and the target itself trips on it (D5, D6) |

## §4 Bottom line

The analytical core — five-field transpose, advective reduction,
(★), exit datum, wall BC, sliver/Hadamard chain, Green row, parity,
free-vortex collapse — is SOUND: I reproduced every step
independently and the machine check passes with a firing rejector.
Two substantive failures survive refereeing: the sonic-exit
BLOW-UP claim (D1, refuted — the correct degeneration is the
record's own gauge structure, and the target contradicts a kernel
law it cites) and the PROVEN-HERE label on the in-gradient
asymmetry reproduction (D2, realizability gap). Neither breaks the
five-field adjoint itself; both must be repaired before absorption,
along with the sign/convention/hypothesis nits D3-D11.
