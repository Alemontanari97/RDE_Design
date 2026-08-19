# Adversarial referee report — lens 'pde' — on swirl5f_pde.md
# (independent re-derivation of the residual split and the marching
#  condition; defect list; per-claim verdicts)

Referee: hyperbolic-PDE adversarial subagent, 2026-08-19.
Target: scratchpad/swirl5f_pde.md (read in full, 883 lines).
Record sources re-read independently BEFORE deriving: M0 440-560
([T-T0]/[S-T0P]/[T-NSW]) + [S-BLITE] block (M0 1351-1366); T3QS full;
PB §8/§9; phaseD_meanswirl_formalization.md D.1-D.5 (221-580) and
D.17-D.20 + S.22 (1314-1957) verbatim; VERDICT_phaseD_proofs1.md §3.2
full; N6 doc full; choice_ledger C51 row.
Discipline: every verdict below rests on my own algebra, shown. Labels
per the binding set {PROVEN-HERE, PROVEN-IN-RECORD, SCALING-ESTIMATE,
HYPOTHESIS, OPEN}.

==============================================================================
## §R1 Independent re-derivation 1: the exact wave-frame system and the split

### R1.1 Lab system, substitution, relative fluxes (done from scratch)

Lab-frame unsteady Euler, cylindrical, r-weighted conservative form
(standard; each row ∂_t(rU) + ∂_x(rF_x) + ∂_r(rF_r) + ∂_θ(F_θ) = r·S):

    mass:   ∂_t(rρ)   + ∂_x(rρu)        + ∂_r(rρv)        + ∂_θ(ρw)        = 0
    x-mom:  ∂_t(rρu)  + ∂_x(r(ρu²+p))   + ∂_r(rρuv)       + ∂_θ(ρuw)       = 0
    r-mom:  ∂_t(rρv)  + ∂_x(rρuv)       + ∂_r(r(ρv²+p))   + ∂_θ(ρvw)       = p + ρw²
    Γ-row:  ∂_t(rρΓ)  + ∂_x(rρuΓ)       + ∂_r(rρvΓ)       + ∂_θ(ρwΓ + rp)  = 0
    energy: ∂_t(rρE)  + ∂_x(rρu h0)     + ∂_r(rρv h0)     + ∂_θ(ρw h0)     = 0

(Γ = rw; ρwh0 = (ρE+p)w; r∂_θp = ∂_θ(rp) since ∂_θ r = 0.)
Substitute fields F(x,r,θ'), θ' = θ − Ωt: ∂_t → −Ω∂_θ', ∂_θ → ∂_θ'.
Each row becomes ∂_x(rF_x) + ∂_r(rF_r) + ∂_θ'(F_θ − ΩrU) = r·S. The
five shifted azimuthal fluxes, computed by me:

    mass:   ρw − Ωrρ                    = ρ w_rel
    x-mom:  ρuw − Ωrρu                  = ρ u w_rel
    r-mom:  ρvw − Ωrρv                  = ρ v w_rel
    Γ-row:  ρwΓ + rp − ΩrρΓ             = ρ w_rel Γ + r p
    energy: ρw h0 − Ωr(ρh0 − p)         = ρ w_rel h0 + Ω r p

MATCH: identical, row for row, to the target's §1.1 and to the
record's F_φ,rel entries (phaseD D.18 singular display). [PROVEN-HERE]

Primitive form: D/Dt = ∂_t + u∂_x + v∂_r + (w/r)∂_θ maps to
D_rel = u∂_x + v∂_r + (w_rel/r)∂_θ'. My checks:
 - (P4)-Γ: ρD_rel Γ = rρD_rel w + ρwv = r(−(1/r)∂_θ'p − ρvw/r) + ρwv
   = −∂_θ'p.  MATCHES target (P4)/D.19(i). [PROVEN-HERE]
 - (P6): lab identity ρ Dh0/Dt = ∂_t p; substitution gives
   ρ D_rel h0 = −Ω ∂_θ' p.  MATCHES target (P6)/D.19(ii). (The
   target's chain "D_rel p − d_t p|lab-content" is garbled as printed
   — defect D5 below — but its result is exactly this.)
 - Rothalpy: subtract Ω×(P4)-Γ: ρD_rel I = −Ω∂_θ'p + Ω∂_θ'p = 0,
   I = h0 − ΩΓ.  MATCHES D.20. [PROVEN-HERE]

### R1.2 Formulation (B) checks (rotating frame)

Coriolis per unit volume: −2ρΩ e_x × u_rel with
e_x × u_rel = v e_θ − w_rel e_r, so the force is
+2ρΩ w_rel e_r − 2ρΩ v e_θ. MATCHES target §1.2. Radial r-weighted
sources: p + ρw_rel² + ρΩ²r² + 2ρΩr w_rel; and
w_rel² + 2Ωr w_rel + Ω²r² = (w_rel + Ωr)² = w². RESUM CONFIRMED.
Energy: I = h + |u_rel|²/2 − Ω²r²/2 = h + (u²+v²+w²)/2 − Ωrw
= h0 − ΩΓ. CONFIRMED; the (B) energy row ∇·(ρ u_rel I) = 0 is the
standard steady rotating-frame result (Coriolis workless, centrifugal
= −∇(−Ω²r²/2)). (A)−(B) energy link re-derived:
(A)-energy − Ω×(A)-Γ-row has azimuthal flux
ρw_rel h0 + Ωrp − Ω(ρw_relΓ + rp) = ρ w_rel I — the Ωrp work flux
cancels against Ω(rp) EXACTLY as the target says. [PROVEN-HERE]

Theta-row equivalence, my independent bookkeeping (the target's §1.3
is compressed; I redid it): with ρw_rel² + p = ρw_rel w − Ωrρw_rel + p
and ∂_r(Ωr²ρv) = Ωr∂_r(rρv) + Ωrρv,

  (B)-θ-row = (A)-linear-θ-row − Ωr·(mass row),

and in r-weighted Γ-form (verified by expanding both sides):

  r·(B)-θ-row + Ωr²·(mass row) = (A)-Γ-row.          (R1.2-1)

Both closings are exact; the Coriolis source −2ρΩrv is consumed by
the metric expansion ∂_r(Ωr²ρv) plus the absolute geometric source.
CONFIRMS target §1.3. [PROVEN-HERE]

### R1.3 The split and the K rows (derived from scratch, then diffed)

Frozen operator := strike ∂_θ'. Residual per unit volume per row:
R = (1/r)∂_θ'[F_θ − ΩrU]. Primitive struck terms, computed by me from
(P1)-(P6):

    K_ρ  = (w_rel/r)∂_θ'ρ + (ρ/r)∂_θ'w  = (1/r)∂_θ'(ρw_rel)
    K_u  = ρ(w_rel/r)∂_θ'u
    K_v  = ρ(w_rel/r)∂_θ'v
    K_Γ  = ρ(w_rel/r)∂_θ'Γ + ∂_θ'p
    K_s  = (w_rel/r)∂_θ's
    K_h0 = (w_rel/r)∂_θ'h0 + (Ω/ρ)∂_θ'p

Diff conservative-vs-primitive, each by product rule (I executed all
five; the two nontrivial ones displayed):

  (1/r)∂_θ'(ρw_relΓ + rp) = Γ·(1/r)∂_θ'(ρw_rel) + (ρw_rel/r)∂_θ'Γ + ∂_θ'p
                          = K_Γ + Γ K_ρ                              ✓
  (1/r)∂_θ'(ρw_rel h0 + Ωrp) = h0 K_ρ + ρ[(w_rel/r)∂_θ'h0 + (Ω/ρ)∂_θ'p]
                             = ρ K_h0 + h0 K_ρ                       ✓

plus R_x = K_u + uK_ρ, R_r = K_v + vK_ρ, R_ρ = K_ρ, and the entropy
form ρK_s + sK_ρ. IDENTICAL to the target's §2.2 table and to D.18's
r4 triangular-recombination display (including the ρ factors on the
per-unit-mass s/h0 rows). Triangular over K_ρ with bounded
coefficients and ρ bounded below: invertible. NO MISSING TERM found:
my row-by-row substitution in R1.1 transformed every ∂_t and every
∂_θ of the five lab rows; within the pinned single-(R_g, h(T)) gas
model no other θ-dependence exists in the system. [PROVEN-HERE.
Same honest boundary as the target: pen grade, common-mode with any
transcription error I share with the author; G-f battery remains the
carrier-grade discharge — I checked the target CLAIMS no more than
this.]

Rothalpy projection re-derived:
  K_h0 − Ω K_Γ/ρ = (w_rel/r)∂_θ'(h0 − ΩΓ) = (w_rel/r)∂_θ' I.
CONFIRMS target §3 row 6 / claim 8: pure sweep in I; torque and work
atoms cancel identically. [PROVEN-HERE]

VERDICT of re-derivation 1: the split, the residual list, the
recombination dictionary, and the rothalpy projection all REPRODUCE.
No missing residual piece, no Coriolis/centrifugal piece in R in
either formulation (the (B) frame sources carry no ∂_θ'). The
(A)/(B) residual MAP, however, is misstated in one parenthetical —
defect D2.

==============================================================================
## §R2 Independent re-derivation 2: symbol and marching condition

### R2.1 Five-field symbol

Rows (ρ^,u^,v^,w^,p^), u_n = u n_x + v n_r; my cofactor expansion:
θ-row gives ρu_n; remaining 4×4 gives u_n·ρ²u_n(u_n² − c²|n|²);
total

    det M(n) = ρ³ u_n³ (u_n² − c² |n|²).                      (R2.1-1)

CONFIRMS target §4.1 and record D.3 (with the ρ³-normalization remark
correctly carried). n = (−λ, 1) reproduces the pencil; Γ absent from
the symbol. [PROVEN-HERE]

### R2.2 Marching condition

Monge-cone argument, checked for soundness (this was my main
suspicion): the target uses the FULL circle {u_m + c ê} as "the ray
cone" although the actual bicharacteristic directions of the steady
2-D operator are only the two Mach directions u_m − c n̂ (u_m·n̂ = ±c)
plus the streamline. I verified the argument is nevertheless correct:
the dependence cone is the cone generated from the origin over the
disk {u_m + c ê, |ê| ≤ 1} (envelope description); when the origin is
outside the disk (q_m > c) that cone is the wedge spanned by the two
tangent (Mach) directions, and
  wedge ⊂ {x > 0}  ⟺  disk ⊂ {x > 0}  ⟺  min_ê (u + c ê_x) = u − c > 0.
Hence x-marching spacelikeness ⟺ u > c, and on a curved surface with
meridional unit normal n_m the same argument gives u_m·n_m > c, i.e.
M_n > 1. I also verified the target's counterexample state
u = 0.5c, v = 1.2c explicitly: q_m = 1.3c (hyperbolic), and the Mach
ray with n̂_x = 0.8857 (root of 1.69n_x² − n_x − 0.44 = 0 on
0.5n_x + 1.2n_r = 1, n̂ unit) has x-component (0.5 − 0.8857)c < 0:
the cone straddles x = const — no march. CONFIRMS target §4.2 =
record D.4/[T-NSW](b), and the hierarchy (hyperbolicity q_m > c ⊉
marchability u > c; M_tot forbidden per D.5(iii)). [PROVEN-HERE]

### R2.3 Azimuthal-march condition and the kernel-loci identification

3-D symbol re-derived (formulation (A) primitive, advective factor
w_vec·ζ = uζ_x + vζ_r + w_rel ζ_θ; pressure/dilatation couple through
the ABSOLUTE velocity components — the −ΩrU flux shift moves ONLY the
advective factor):

    det = ρ³ (w_vec·ζ)³ [ (w_vec·ζ)² − c² |ζ|² ].             (R2.3-1)

On ζ = e_θ: det ∝ w_rel³ (w_rel² − c²): zeros exactly at
{w_rel = 0} (multiplicity 3, advective) and {|w_rel| = c} (acoustic).
Spacelikeness of θ' = const ⟺ |w_rel| > c — C51's condition
verbatim ("|u_theta − Omega r| > a"). And the two zero sets are
LITERALLY the H-NC locus {|w_rel| = c} and the H-WR locus
{w_rel = 0} of D.18's second iff (both stated on the azimuthal
scalar w_rel; I re-checked D.18's kernel algebra — the compatibility
line (w_rel² − c²)∂_φρ = 0 and the w_rel = 0 sweep-factor kernel —
against the symbol factors: they are the same two polynomials).
Claim 10's structural identification is CORRECT and, as far as I can
find in the record, NEW. [PROVEN-HERE. One naming caveat = defect D7:
"CJ locus" for {|w_rel,θ| = c} repeats the record's own gloss;
[T-NSW](a) defines the CJ surface on the relative velocity VECTOR
|w_vec| = c — the two coincide only where the meridional relative
component is negligible.]

General leaf ν = cosχ e_θ + sinχ e_x: w_vec·ν = w_rel cosχ + u sinχ;
condition |w_rel cosχ + u sinχ| > c. CONFIRMS target §4-bis.5
interpolation formula. [PROVEN-HERE]

==============================================================================
## §R3 Spot-checks of the remaining load-bearing algebra

 - In-slice RH (target §4.4): [ρu_n] = 0, θ-row [ρu_n w] = m[w] = 0
   ⟹ [w] = 0 ⟹ [Γ] = 0 (r continuous on the front curve); energy
   m[h0] = 0 ⟹ [h0] = 0. D.20 general-front limit: with
   m[h0] = −σ_n[p], m[Γ] = −r n_θ[p], σ_n = Ωr n_θ (record display,
   quoted CORRECTLY by the target): n_θ → 0 kills both right sides
   separately. CONFIRMED. [PROVEN-HERE]
 - Axis/core (target §4.3): h = h0 − q_m²/2 − Γ²/(2r²) = h_min ⟹
   r_core = Γ_tip/√(2(h0 − h_min − q_m²/2)); with u_θ,int² = 2 f_KE h0
   and Γ_tip = R_int u_θ,int: r_core/R_int = √(f_KE h0/(h0 − q_m²/2
   − h_min)) ≥ √f_KE when the denominator ≤ h0 (needs h_min ≥ 0 —
   true for the table floor as an absolute enthalpy origin; note this
   sign convention is silently used). √0.03 = 0.173, √0.06 = 0.245:
   the quoted 0.17-0.25 checks. The tip-Γ level is flagged HYPOTHESIS
   in the target — properly surfaced. [PROVEN-HERE + SCALING-ESTIMATE]
 - Advective winding (target §4-bis.2): dθ'/dx = w_rel/(ru) along the
   relative streamline; ∫ = −Ωτ_n + ∫w/(ru)dx, τ_n = ∫dx/u; in sector
   units St_n(1 − O(ε_θ)) with the lab drift the ε_θ correction.
   CONFIRMS PB §8 "Δθ_sweep/(2π/n) = St_n" verbatim. Acoustic bound
   |dθ'/dx| ≤ (|w_rel|+c)/(r(u−c)) and the C_geo upper bracket
   (1 + c/|w_rel|)·u/(u−c) = [(|w_rel|+c)/(u−c)]/[|w_rel|/u]:
   arithmetic CONFIRMED. Geometry wording defect D3 below.
 - Order arithmetic (target §3): ΩΓ/h0 = (u_θ/(Ωr))⁻¹·u_θ²/h0
   = 2f_KE/ε_θ ∈ [0.06/0.2, 0.12/0.15] = [0.3, 0.8]: the NUMBER
   checks; the DERIVATION of why (6b)'s order is St_n × ΩΓ/h0 is
   absent — defect D1.
 - Record-quote audit (anchors checked at source): D(W) formula (T3QS
   §1) ✓; "the only content of F_theta at u_theta = 0" (T3QS §2(b))
   ✓ verbatim; D.18 six K rows ✓ symbol-for-symbol; D.19(i)/(ii) ✓;
   D.20 σ_n display ✓; D.3(a)-(c) incl. ρ³ remark ✓; D.4 m_n =
   ess inf(M_n − 1) ✓; D.5(ii) scope ("state-sensitivity, not
   flow-solution") respected by "at fixed meridional data" ✓;
   [T-NSW] C1/C2/C3 hierarchy ✓ verbatim; C51 regime condition ✓
   verbatim; [S-BLITE] "u_x − c ≥ δ > 0", "cheap exact meter" ✓;
   VERDICT §3.2 D.18 first/second iff = THEOREM* (judge-downgraded)
   ✓ — the target adopts, never exceeds; D.13 recovery THEOREM ✓;
   N6-1 front det ∝ u_n³(u_n²−c²) ✓; G_fund closed form ✓ matches
   D.2 r3 display. NO MISQUOTE FOUND. One adoption-caveat omission =
   defect D6.

==============================================================================
## §R4 DEFECT LIST (numbered, severity, locus, corrected version)

NO CRITICAL DEFECT FOUND. No missing residual term, no wrong marching
condition, no record misquote, no unsurfaced load-bearing hypothesis
that changes a verdict.

D1 — MAJOR (discipline breach + underived scaling). Locus: §3 ROW 6,
order line for (6b): "Order: (6b) St_n x (Omega Gamma / h0) with
Omega Gamma / h0 ~ 2 sqrt(f_KE / (2 f_KE)) ... honest version:
Omega Gamma / h0 = (Omega r / u_theta)(u_theta^2 / h0) x ... =".
Two faults: (i) the first fragment 2√(f_KE/(2f_KE)) = √2 is a dead
false expression independent of f_KE, left in the text; the "honest
version" chain contains a literal ellipsis "x ... =" — the artifact
ships an INCOMPLETE derivation where the binding discipline demands
the derivation of every SCALING-ESTIMATE. (ii) Substantively: the
identity ΩΓ/h0 = 2f_KE/ε_θ ~ 0.3-0.8 is correct (I verified), but
the step "(6b)'s transit-integrated order = St_n × ΩΓ/h0" is NEVER
derived. The clean derivation is: per transit,
Δh0|_(6b) = −∫(Ω/ρ)∂_θ'p dt = Ω·ΔΓ|_torque (D.20 proportional
pumping), so (6b)/h0 = (ΩΓ/h0)·(ΔΓ/Γ); the quoted order then REQUIRES
the additional data-dependent hypothesis ΔΓ/Γ ~ St_n per transit
(torque impulse ∫|∂_θ'p|dt/ρ ~ St_n·Γ), which is plausible at
σ/μ ~ 0.7 but is a HYPOTHESIS not surfaced in the ledger. CORRECTED
VERSION: label (6b)'s order "St_n × (ΩΓ/h0) = St_n × 2f_KE/ε_θ ~
(0.3-0.8)·St_n, GIVEN [H-TORQ] ΔΓ/Γ ~ St_n per transit (equivalently
Ω∫∂_θ'p dt/ρ ~ St_n·ΩΓ), surfaced as HYPOTHESIS" — or derive it
directly as Ωτ_n·δ_θ'(p/ρ)/h0 with the wave pressure contrast, which
gives the alternative form St_n·(2π/n)·(δp/(ρh0)).

D2 — MINOR (wrong parenthetical; conclusion unaffected). Locus:
§2.4(ii): "The (B)-residual maps onto the (A)-residual by the §1.3
recombination (using ONLY the frozen mass row, which the 2.5-D
operator carries)". FALSE as printed: the residual↔residual map uses
the mass RESIDUAL K_ρ, not the frozen mass row. My corrected
identities (from (R1.2-1), split into frozen and ∂_θ' parts — the
recombination coefficients (r, Ωr²; 1, −Ω) are θ'-independent so the
recombination COMMUTES with the frozen/residual split):
    frozen:   r·(B)-θ-frozen + Ωr²·(mass-frozen) = (A)-Γ-frozen
    residual: r·R_θ^(B) + Ωr²·K_ρ = R_Γ^(A)
    energy:   R_E^(B) = R_E^(A) − Ω·R_Γ^(A)   (no mass row at all).
The CONCLUSION (no Coriolis/centrifugal piece in either residual)
survives: Ωr²K_ρ is a sweep atom, not a frame force. The correct
one-line justification is the commuting property, not the frozen
mass row.

D3 — MINOR (geometry wording: width vs offset). Locus: §4-bis.2,
"the FULL backward cone from P meets Γ_d in an azimuthal ARC of
width Δθ'_dom = St_n × (2π/n) × C_geo". Under the margin with
|w_rel| > c all rays wind the SAME way: the arc [Δ_min, Δ_max] does
NOT contain the slice azimuth (Δ_min ≥ (|w_rel|−c)/(u+c)-winding
> 0), and its literal width Δ_max − Δ_min → 0 as c → 0 while the
advective OFFSET stays St_n — so "width ≥ St_n(1−O(ε_θ))" is false
if width means Δ_max − Δ_min. What the bracket
[1−O(ε_θ), (1+c/|w_rel|)u/(u−c)] correctly bounds is the EXTENT from
the slice section to the far edge of the arc (= Δ_max), which is
also the right object for "data the slice never consults".
CORRECTED VERSION: replace "arc of width" by "arc at azimuthal
distance/extent from the section bounded by"; claims 9 and 14 then
stand unchanged.

D4 — MINOR (normalization inconsistency in the order bookkeeping).
Locus: §3 preamble vs rows 4a/6b. The preamble fixes the convention
"contributes O(St_n) RELATIVE TO THE TRANSPORTED QUANTITY"; row 4a
then quotes "St_n eps_theta" (which is relative to the MOMENTUM-row
scale — relative to Γ itself it is plain St_n) and row 6b quotes the
ΩΓ/h0-weighted form. Each is individually defensible and the
reference scale is stated in the prose, but the summary-table
"order" column mixes normalizations without a column note.
CORRECTED VERSION: one sentence fixing per-row reference scales, or
two columns (relative to own row / relative to h0-momentum scale).

D5 — MINOR (garbled proof line; result correct). Locus: §1.1, the
(P6) justification "rho D_rel h0 = D_rel p - d_t p|_lab-content =
-Omega d_theta' p". Not a valid equation chain as printed (the middle
member is not defined). CORRECTED VERSION: "lab identity
ρ Dh0/Dt = ∂_t p (Crocco/energy, standard); under ∂_t → −Ω∂_θ' and
D/Dt → D_rel this reads ρ D_rel h0 = −Ω ∂_θ' p." Same for the §1.3
theta-row first line ("− Omega r d_x(r rho u)/1 ..."): dead fragment
before the correct "precisely:" restart.

D6 — MINOR (adoption caveat omitted). Locus: §2.3 RECORD OBJECT 3
and claim 8. The target adopts the D.18 front atoms n_θ'[F_φ,rel]
and asserts "the atom densities implied by my conservative split
coincide with the record's". The record (D.18 r4, L0-5) states the
atom density holds only "up to the surface-measure normalization
FIXED IN THE G-f COMPUTATION" and names the meridional-cancellation
JACOBIAN identity (|n_m|·dS-factor = section-curve factor) as an
explicit UNEXECUTED G-f check target. The target's coincidence claim
rides the same unfixed normalization and should carry the caveat
verbatim. No content change — the adoption is at THEOREM* and the
caveat is part of what THEOREM*-modulo-G-f means — but the
one-sentence caveat is owed.

D7 — MINOR (inherited record conflation; flag owed under the
target's own discipline). Locus: §4-bis.5 (and §4-bis.1). The locus
{|w_rel| = c} with w_rel the AZIMUTHAL scalar is named "the CJ
locus"; [T-NSW](a) defines the CJ surface as the relative sonic
locus of the relative velocity VECTOR (|w_vec| = c). The two
coincide only where the meridional relative component is negligible
(near-interface, |w_rel| ~ D_CJ — the record's own H-NC gloss makes
the same identification, so this is record-CONSISTENT). But a
document whose discipline is "flag discrepancies loudly" owed
FLAG-4 here: the kernel/marchability identification (claim 10) is
EXACT on the azimuthal-scalar loci; the "CJ surface" NAME for the
outer locus is approximate away from the front. Secondary note:
{w_rel = 0} lies strictly inside the already-dead band |w_rel| < c —
it is the advective (multiplicity-3) degeneracy of the azimuthal
symbol, not a second boundary of the marchable set; the target's
§4-bis.5 text is aware ("FAILS ... in the whole band") but claim 10's
"two degeneracy loci" wording invites the misreading.

D8 — MINOR (observation, no repair needed beyond a sentence). Locus:
claim 5 / §3 preamble "transit-integrated O(St_n)". What §4-bis
proves is the GEOMETRY (swept angle per transit = St_n sectors) and
what §3 estimates is the SOURCE-INTEGRAL scaling ∫K dt ~ St_n × ΔV;
neither is the SOLUTION-ERROR bound, which is exactly S.22's open
target (norm fork g1, g2a/g2b walls). The target's SC-9 says this
correctly ("nothing here upgrades it") — but claim 5's headline
"transit-integrated O(St_n)" would read as an error bound out of
context. One cross-reference from claim 5 to SC-9 suffices.

Hypothesis-ledger audit (task item (c)): all §5 SC hypotheses match
record objects; the only USED-but-unsurfaced hypotheses found are
[H-TORQ] inside D1 (ΔΓ/Γ ~ St_n per transit, load-bearing for the
6b order) and the h_min ≥ 0 sign convention inside the §4.3 core
bound (load-bearing for "lower-bounded by sqrt(f_KE)").

==============================================================================
## §R5 Per-main-claim verdicts (numbering = author's claim list)

| # | Claim (short) | Verdict | Basis |
|---|---|---|---|
| 1 | Exact system, both formulations, resum, rothalpy variable | CONFIRMED | §R1.1-R1.2 full re-derivation; D5 garbles are presentational |
| 2 | Exact split derived twice; triangular diff over K_ρ | CONFIRMED | §R1.3 independent product-rule executions, all rows |
| 3 | R = D(W) row-for-row; K = D.18 list; 3 flags; no discrepancy | CONFIRMED | §R3 anchor-by-anchor quote audit; no misquote found |
| 4 | No Coriolis/centrifugal in residual, either formulation | CONFIRMED (with D2 repair) | frame sources θ'-free; corrected residual map r·R_θ^(B) + Ωr²K_ρ = R_Γ^(A) |
| 5 | Residual enumeration with orders | GAP-NAMED | identities CONFIRMED (§R1.3); (6b) order underived + [H-TORQ] unsurfaced (D1); normalization mixing (D4); St_n is source-scaling not error bound (D8) |
| 6 | Symbol det; u_x > c marching; M_n > 1 curved; frame-invariant | CONFIRMED | §R2.1-R2.2 independent cofactor + Monge-cone soundness check + explicit counterexample ray computed |
| 7 | Axis regularity; vortex-core obstruction; r_core/R_int ≳ √f_KE | CONFIRMED | §R3 algebra + arithmetic; h_min ≥ 0 convention to be stated; tip-Γ HYPOTHESIS properly surfaced |
| 8 | In-slice RH [Γ]=[h0]=0; n_θ'→0 limit of [I]=0; atoms price the split | CONFIRMED (with D6 caveat) | §R3 jump algebra re-derived; adoption stays at record THEOREM* |
| 9 | Wound cone; winding = St_n(1−O(ε)); C_geo bracket; geometric meaning of St_n | CONFIRMED (with D3 wording repair) | §R3 winding integral re-derived; bracket = extent, not width |
| 10 | Azimuthal march ⟺ |w_rel| > c; degeneracy loci = H-NC/H-WR kernels | CONFIRMED | §R2.3: azimuthal symbol det ∝ w_rel³(w_rel²−c²) re-derived; same two polynomials as D.18's kernel algebra; D7 naming caveat on "CJ locus" |
| 11 | Solution class SC-1..SC-9 with g2b wall as class clause | CONFIRMED (as hypothesis list) | labels match record certifications item by item (VERDICT §3.2 cross-checked); no overclaim found |

OVERALL: the artifact SURVIVES adversarial re-derivation on every
load-bearing algebraic claim. Zero CRITICAL, one MAJOR (D1 — a
discipline breach with an unsurfaced hypothesis inside one scaling
line, repairable in-place), seven MINOR. The deadliest-class hunt
(missing terms) came back EMPTY after full independent
re-derivation of the split from the lab equations. The single
genuinely new structural result (claim 10) is verified correct.

END OF REFEREE ARTIFACT.
