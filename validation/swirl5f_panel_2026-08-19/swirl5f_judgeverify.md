# ADVERSARIAL JUDGE-VERIFICATION (convergence round) — full work record
Verifier: independent expert agent, 2026-08-19. Target: JUDGE-ORIGINAL (JV)
content of `swirl5f_FINAL_report.md`. Method: own algebra FIRST (committed in
`swirl5f_jv_check.py`, run before reading the judge's §5/§5-bis/§5-ter text),
then comparison. Machine: sympy in the pinned env, nothing installed.
Companion script: `swirl5f_jv_check.py` (this directory) — 11/12 checks PASS;
the single "FAIL" is a string-form artifact (−w³(c−w)(c+w) ≡ w³(w²−c²)),
content PASS. Supplementary sympy runs are transcribed inline below.
No repo file touched.

==============================================================================
## ITEM 1 — §5 C1: the χ = ΩΓ/h0 adjudication

### 1.1 My own algebra (pre-commitment)
- EXACT identities (sympy PASS):
  χ = ΩΓ/h0 = ε_θ M_Ω² (γ−1)(h/h0)   [under c² = (γ−1)h]
  χ = (2 f_θ/ε_θ)(KE/h0)              [EOS-FREE, f_θ := u_θ²/q², KE := q²/2]
  ⟹ the pde-doc's "(2 f_KE)/ε_θ ≈ 0.3–0.8" is exactly the KE/h0 = 1
  degeneration, i.e. the h0-normalized reading of "3–6%".
- DISCRIMINATING TEST re-executed: KE-reading ⟹ M_Ω = δM_x/ε_θ ≈ 1.04–3.3
  (working 1.5–2.5) ⟹ Ωr = M_Ω·c ≈ 1650–3250 m/s ≈ D_CJ 2000–2500 ✓.
  h0-reading ⟹ M_θ = √(2f/((γ−1)h/h0)) ≈ 0.61–0.93 ⟹ M_Ω ≈ 3.1–6.2 ⟹
  Ωr ≈ 3400–8000 m/s: impossible for a CJ-locked wheel ✗. Judge quotes
  (3.6–6; 4300–7500) — same conclusion, interior of my envelope. SOUND.
- χ value: physical envelope (Ωr = 1800–3200, ε_θ = 0.15–0.20, c = 1100–1300,
  γ = 1.15–1.25, h/h0 = 0.7–0.8) gives 0.03–0.34 with concordant central band
  0.06–0.20. The adjudicated 0.06–0.20 CONFIRMED; 0.3–0.8 REFUTED for the
  record class.
- CLOSURE χ·β_τ = β_w: sympy PASS, and STRONGER than printed — it is exact
  at the DEFINITION level, EOS-FREE, no γ identity needed:
  χβ_τ = (ΩΓ/h0)·p/(ρΩr u_θ) = p/(ρh0) = β_w  since Γ = r u_θ.  (The asy
  derivation routed it through c² = (γ−1)h; unnecessary.)
- REPAIRED ORDER a_p·St_n·β_w: β_w = (γ−1)h/(γh0) ∈ [0.091, 0.160] envelope,
  0.10–0.13 central; ×0.7×(0.1–1) = 0.007–0.09 ✓ CONFIRMED.
- A4 NORMALIZATION FLAG: h0-normalized swirl-KE fraction = u_θ²/(2h0) =
  ε_θχ/2 = 0.0045–0.02 ⟹ A4 reads ≈ 0.45–2% at concordant numbers (judge:
  0.3–2.5%). The unit-mismatch trap is REAL and the flag CONFIRMED.

### 1.2 Spike-core bound — the one REFUTED number
- FORMULA: r_core/R_int = √(f_θ·KE_int/(h0 − h_min − q_m²/2)) — sympy PASS
  (numerator is f_θ·KE_int = u_θ,int²/2, NOT f_θ·h0: the pde error correctly
  identified). Lower bound √(f_θ·KE_int/h0) valid given h_min ≥ 0 ✓.
- EXACT internal-consistency identity (new here):
      √(f_θ·KE_int/h0) = √(ε_θ·χ/2).
  With the judge's OWN adjudicated χ = 0.06–0.20 and ε_θ = 0.15–0.20 this is
  0.067–0.141. Physical anchors (u_θ = ε_θΩr = 270–640 m/s over √(2h0) =
  3900–4900 m/s): 0.066–0.133.
- The printed "≈ 0.10–0.19" needs KE_int/h0 ≈ 0.33–0.60, i.e. interface Mach
  ≈ 2.4–3.9 — OUTSIDE the record class M = 1.2–2.0 (which caps KE_int/h0 at
  ≈ 0.13–0.29 for γ = 1.15–1.25). Equivalently 0.10–0.19 is what one gets by
  silently halving the denominator (remaining enthalpy = h0/2) — an unstated
  extra hypothesis.
- VERDICT: formula CONFIRMED; numeric band REFUTED AS PRINTED. Corrected
  band: r_core/R_int ≳ √(ε_θχ/2) ≈ 0.065–0.14 (record class), reaching ~0.2
  only in a declared little-enthalpy-remaining regime. The qualitative
  conclusion (not negligible; weaker than the old wrong 0.17–0.25) STANDS.

ITEM 1 VERDICT: CONFIRMED on the adjudication, the discriminating test, the
exact closure (strengthened to EOS-free), the repaired work-term order, and
the A4 flag; REFUTED with corrected algebra on the spike-core numeric band
(0.10–0.19 → 0.065–0.14; formula unchanged).

==============================================================================
## ITEM 2 — §5 C3 / §4: sonic-exit datum

My own 5×5 solve (sympy, pre-committed; var-doc r-weighted convention,
n = e_x, δJ integrand r(u²δρ + 2ρuδu + δp)):
  δρ: ψ₁u − c²uψ₅ = u²;  δu: ρψ₁ + ρuψ₂ = 2ρu;  δv: ρuψ₃ = 0;
  δw: ρuψ₄ = 0;  δp: ψ₂ + uψ₅ = 1.
- det = ρ³u³(u−c)(u+c) ✓.
- Cramer numerator for ψ₅ ≡ 0 IDENTICALLY (sympy PASS): the solve reads
  ψ₅(u²−c²) = 0 with EXACT-zero RHS. CONFIRMED.
- Generic solution (u, 1, 0, 0, 0); it STILL SATISFIES all five equations at
  u = c (sympy PASS): the datum extends continuously, NO blow-up — the
  deriver's 1/(u²−c²) claim was rightly refuted.
- Kernel at u = c: span{(c², −c, 0, 0, 1)} (sympy nullspace) ✓. Under the
  declared multiplier dictionary (carrier weights: ψ_i^carrier = rψ_i^here,
  i = 2..5), the record terminal gauge l(e_x) = (1, −r/c, 0, 0, r/c²)
  (carrier 5F.4) maps to (1, −1/c, 0, 0, 1/c²) ∝ (c², −c, 0, 0, 1) — sympy
  PASS. The kernel direction IS the terminal gauge. CONFIRMED.
- N6-1(c) citation checked at source (N6 doc §1(c)): r⁻ = (ρ, −cn_x, −cn_r,
  0, ρc²), swirl component zero; ⟨grad g, r⁻⟩ = ρ(u_n−c)(u−cn_x) → ρ(u−c)²
  at n = e_x — vanishes quadratically at u = c, the compatibility the judge
  cites. Consistent with my direct solvability check.
- Hazard re-typing (0/0 conditioning of a generic solve near u = c; loss of
  the "δV free at exit" premise; quotient-mod-l(n) cure; margin meter
  retained): the correct reading.

ITEM 2 VERDICT: CONFIRMED in full.

==============================================================================
## ITEM 3 — §5-bis: normalization chain, operator dictionary, K̄ = 0

### 3.1 D(W) ≡ div-form K row (EXACT)
Sympy PASS, row-for-row: with U = (ρ, ρu, ρv, ρΓ, ρE) and lab azimuthal
fluxes F_θ = (ρw, ρuw, ρvw, ρwΓ + rp, (ρE+p)w):
  F_θ(U) − Ωr·U = (ρw_rel, ρuw_rel, ρvw_rel, ρw_relΓ + rp, ρw_rel h0 + Ωrp)
= F_φ,rel exactly (energy row: ρEw_rel + pw = ρh0w_rel + Ωrp). CONFIRMED.

### 3.2 J₁^K = St·J₁^ledger
Ledger of record (theorem_ledger.md:168–176): N(U;St) = N_0(U) + St·S_sweep(U),
J₁^ledger = −⟨ψ_J, S_sweep(U_0)⟩. K-convention: J₁^K = −∫⟨ψ_ξ, K⟩dμ with
K = N − N_0 = St·S_sweep ⟹ J₁^K = St·J₁^ledger, and T3QS's J₁ (D(W) with St
absorbed) = J₁^K. The chain is a definitional convention-pin, consistent
with all three sources; "ledger normalizes S_sweep to O(1)" is the correct
gloss. FOOTNOTE (no error): the ledger's inline "S_sweep = −Ω_w r ∂_θ'" is
the swirl-free sweep shorthand; the pin S_sweep := K/St is what makes the
chain exact — precisely the F-5 hazard the panel resolves. CONFIRMED.

### 3.3 K̄ = 0 fiberwise UNCONDITIONALLY on periodic BV composites
My re-derivation: fix (x,r); K(x,r,·) = (1/r)∂_φ[F_φ,rel(W_A(x,r,·))] with
F single-valued, 2π/n-periodic, BV in φ (bounded S1 fields, finitely many
in-slice-front crossings + finitely many data-cycle jumps ⟹ BV). The
distributional derivative of a periodic BV function over one period has
total SIGNED mass zero — a.c. + Cantor + ATOMS included: Df((φ₀, φ₀+P]) =
f(φ₀+) − f(φ₀+) = 0. Hence the μ-mean of the K-distribution vanishes
fiberwise with NO continuity hypothesis — the strengthening over the fun
deriver's conditional statement is CORRECT. (Numeric witness in the script:
sin(3φ) + two-atom step, total mass 0 to machine zero.) The judge's
G-f-robustness note is right: only the 1-D-in-φ definitional div-form is
consumed, no front-surface measure. The consequence bookkeeping is also
consistent: with total K̄ = 0, moving the atom mass to the (J) channel gives
J₁ = ⟨ψ̄, atom content⟩ − Cov^{ac}, and the channel VALUES are indeed
convention-dependent — the a.c.-only/ψ̄-pairing pin is necessary and
correctly carried. CONFIRMED (strengthening verified).

ITEM 3 VERDICT: CONFIRMED in full (all three legs).

==============================================================================
## ITEM 4 — §5-ter: azimuthal-march spacelikeness and the D.18 loci

- Leaf symbol: det factor on ζ = e_θ is w_rel³(w_rel² − c²) (sympy PASS).
  Spacelikeness of θ' = const (ray cone one-sided) ⟺ |w_rel| > c —
  verbatim C51's regime condition |u_θ − Ωr| > a (choice_ledger.yaml C51
  checked at source). CONFIRMED.
- Degeneracy loci: advective kernel {w_rel = 0} (multiplicity 3) and
  acoustic locus {|w_rel| = c}. Record D.18 second iff (phaseD file, lines
  1542–1561) hypotheses checked at source: H-NC = {|w_rel| = c} has empty
  interior; H-WR = {w_rel = 0} has empty interior. The identification
  "march degeneracy loci = H-NC/H-WR kernel loci, literally" is EXACT.
  CONFIRMED. The two carried caveats are correct refinements: {w_rel = 0}
  lies strictly inside the dead band |w_rel| < c (one regime boundary, not
  two), and "CJ" names the azimuthal-scalar locus only approximately
  ([T-NSW]'s CJ surface is |w_vec| = c on the relative VECTOR; they
  coincide only where (u,v)-relative content is negligible).
- Dependence-arc extent: re-derived. Advective winding per transit
  Δθ'_adv = Ω∫dx/u·(1 − O(ε_θ)) = St_n(2π/n)(1 − O(ε_θ)); acoustic-ray
  winding bound |dθ'/dx| ≤ (|w_rel|+c)/(r(u−c)); ratio to the advective
  scale = (1−ε_θ)(1 + c/|w_rel|)·u/(u−c) ≤ (1 + c/|w_rel|)·u/(u−c).
  Bracket [1 − O(ε_θ), (1+c/|w_rel|)u/(u−c)]·St_n·(2π/n) CONFIRMED as the
  EXTENT from the section to the far edge (numeric spot-checks in script:
  ratio ≤ upper at the three class corners, equality at the corner —
  bound tight). The C7 repair (extent, NOT width) is necessary and correct:
  literal arc width 2c(W+u)/(u²−c²)·(scale) → 0 as c → 0 while the extent
  stays ~St_n — I reproduced this failure mode independently before reading
  the judge's resolution.

ITEM 4 VERDICT: CONFIRMED in full (with the wording repair load-bearing).

==============================================================================
## ITEM 5 — Spot-check of 3 MAJOR repairs (fix correctness, not plausibility)

Chosen (distinct from items 2–3, which already cover var-D1 and
fun-DEF-1/2): asy-D2, asy-D3 (B2), var-D2. Bonus: pde-D2, asy-D7.

### 5.1 asy-D2 (drift census 5 → 6) — CONFIRMED
K_h0 = (w_rel/r)∂_φh0 + (Ω/ρ)∂_φp splits under w_rel = w − Ωr into
−Ω∂_φh0 + (w/r)∂_φh0 + (Ω/ρ)∂_φp: the sixth drift piece (w/r)∂_φh0 exists
at O(a_h0·ε_θ·St_n); the mass-row drift is the full (1/r)∂_φ(ρw). Census
SIX is right; order impact nil. Fix CORRECT.

### 5.2 asy-D3 / §1 B2 (fold/drop variants) — MOSTLY CONFIRMED, one
### residual DEFECT IN THE FIX
Sympy: 4F-drop V² bias = u_θ,exit² − u_θ,int² = Γ²(1/r_exit² − 1/r_in²);
relative magnitude (r_exit > r_in) = (δ_int²/2)(1 − r_in²/r_exit²) —
EXACTLY the printed formula PROVIDED δ = δ_INTERFACE (sympy: difference 0
with δ_int; nonzero with δ_exit). Fold = δ_exit²/2 ✓. Geometry-signed,
≈ 0 at r_exit ≈ r_in ✓. The h0-convention pinning (fold/drop = a D.13
contract fact, D.20 linkage as rejector) is the right disposition ✓.
DEFECT (in both the refuter's correction and the judge's fusion): the
clause "|bias| ≤ fold value (drop, r_exit ≥ r_in)". Sympy:
  fold − |drop| = −Γ²(r_exit² − 2r_in²)/(2V²r_exit²r_in²),
nonnegative iff r_exit ≤ √2·r_in. For bell-family streamtubes migrating
beyond √2·r_in the drop bias EXCEEDS the fold value. (The inequality is
unconditional only under the δ = δ_exit reading — under which the drop
formula itself is off by the factor r_exit²/r_in².) ONE-LINE REPAIR:
pin δ = δ_int in the drop formula and either replace the bound by the
trivially true |bias| ≤ δ_int²/2, or state the √2·r_in validity boundary.
Headline magnitudes (1.5–3% fold; drop smaller near r_exit ≈ r_in)
unaffected in the typical annulus class.

### 5.3 var-D2 (anti-spike in-gradient downgrade) — CONFIRMED
(8.1) re-derived: u_e² = 2(h0 − h(p_e,s)) − v_e² − Γ²/r_e² ⟹ at fixed
(ṁ, h0, s, Γ, p_e, v_e): δ(ṁu_e) = ṁΓ²/(u_er_e³)δr_e ✓ anti-spike sign.
The refuter's objection is genuine: the duality step needs a wall
perturbation realizing per-tube migration at FIXED (p_e, v_e), while the
exit plane of the 5F solution carries ∂p/∂r = ρu_θ²/r ≠ 0 — the very
gradient the model restores — so the family is generically unrealizable at
finite swirl. Downgrade to SCALING-ESTIMATE (sign) + record consistency +
named deciding instrument (computed 5F gradient, dot-product + sign test)
is the correct disposition. Corrected family-gap ratio verified: spike
debit − bell debit per tube = (Γ²/2)(1/r_s² − 1/r_b²) > 0 ⟹
ΔJ_swirl/J ~ (E_θ/KE)·⟨1 − (r_spike/r_bell)²⟩ > 0 ✓ (the deriver's
original ⟨1 − (r_bell/r_spike)²⟩ was negative — sign error real, fix
correct). Fix CORRECT.

### 5.4 Bonus checks
- pde-D2 corrected residual-map identities: both EXACT by direct algebra:
  r·R_θ^(B) + Ωr²·K_ρ = ∂_φ(ρw_rel w + p) = R_Γ^(A)  ✓
  R_E^(A) − Ω·R_Γ^(A) = (1/r)∂_φ(ρw_rel(h0 − ΩΓ)) = (1/r)∂_φ(ρw_rel I)
  = R_E^(B)  ✓.
- asy-D7 coefficients: 1/(γM_Ω²) = 1/(1.2·4) = 0.208 ✓ (the original 0.15
  was arithmetic error); Δε_θ ≈ 0.146·St_n ⟹ 0.015–0.15 ✓; §1's
  Λ = (0.59–1.11)·St_n ✓ via the concordance ratio M_x/M_Ω = 0.9⁻¹–1.7⁻¹.
  TYPO in §6 asy row: "Λ = 0.06–1.11·St_n" should read 0.59–1.11.

==============================================================================
## OVERALL VERDICT

The fused report's structure, all load-bearing adjudications (C1 reading,
C2 label, C3 sonic exit, C6 license split, C7 extent, C8 CJ naming, §5-bis
chain, §5-ter identification), and 8 of the 9 MAJOR repairs sampled or
covered stand under independent re-derivation. THREE items need one more
(small, numeric/wording) repair pass; NO structural conclusion moves:

 R-A (§5 C1 tail + §2 H-ANN row + §6 pde row): spike-core band
     "≈ 0.10–0.19" → "≈ 0.065–0.14" (= √(ε_θχ/2) at the adjudicated χ;
     formula √(f_θ·KE_int/h0) unchanged; 0.19 requires interface Mach ~3.9,
     outside the record class).
 R-B (§1 B2): drop-variant: pin δ = δ_int; replace "|bias| ≤ fold value
     (r_exit ≥ r_in)" by "|bias| ≤ δ_int²/2; ≤ fold value iff
     r_exit ≤ √2·r_in".
 R-C (§6 asy row): typo 0.06 → 0.59 in the Λ band.

STATUS: CONVERGED-WITH-THREE-NAMED-EDITS (no further panel round needed;
the edits are one-line and carry their algebra above).
