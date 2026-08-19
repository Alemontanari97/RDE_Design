# The five-field per-phase adjoint: explicit derivation, well-posedness,
# hidden-hypothesis ledger, certification-claims analysis, and the
# optimization landscape with swirl

STATUS: subagent derivation artifact (scratchpad, 2026-08-19), input to
the next stage of the 2.5D five-field upgrade analysis. NOT a repo
file; nothing here is "of record" until absorbed under R4 with its own
refutation pass. Repo sources read in full before deriving: M0
[T-T0]/[S-T0P]/[T-NSW]/N6 status block (`docs/rde_nozzle_MASTER.md`
440-560), `docs/rde_nozzle_T3QS.md`, `docs/rde_nozzle_problem_book.md`
§8-§9, `docs/rde_nozzle_N6_swirl.md` §§1-5,
`validation/n6_fivefield_adjoint.py` (PASS 6/6, read line-by-line),
`validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
(D.1-D.20, S.22, r5 text) with the judge labels of
`VERDICT_phaseD_proofs1.md` §3.2, M0 [T-T3-MAP](c) + PROTOCOL
T3-CONTROL (722-825), M0 VI.4bis, `docs/choice_ledger.yaml` C51.

MACHINE CHECK OF THIS DOCUMENT: `swirl5f_adjoint_check.py` (same
scratchpad; sympy 1.14.0 pinned env, nothing installed), OVERALL PASS:
(C1) r-weighted linearization zero leftover; (C2) every advective-form
adjoint row below == the mechanical transpose modulo an explicit
declared multiple of the continuity row; (C3) the exit adjoint datum
reproduces the thrust-integrand variation exactly; (C4) the Γ-row
multiplier invariant; (C5) free-vortex decoupling of the new
couplings; (R1) rejector — a sign-flipped centrifugal transpose
coupling BREAKS (C2). The rejector fires: the check can reject.

LABEL DISCIPLINE (binding, per the task): every claim carries one of
{PROVEN-HERE, PROVEN-IN-RECORD (anchor), SCALING-ESTIMATE (derivation
shown), HYPOTHESIS, OPEN}. Discrepancies with record sources are
FLAGGED in §10 — none is silently adopted.

==============================================================================
## §0 Setting, notation, conventions

Per-phase five-field state V = (ρ, u, v, w, p) on the meridional
domain D(ξ) ⊂ {(x, r) : r > 0}, phase ξ sampling the wave-frame
azimuth φ = θ − Ωt (D.17 ξ ↔ φ identification, DEFINITION of record).
Swirl invariant Γ := r w; meridional speed W := (u² + v²)^{1/2};
meridional streamline derivative

    D := u ∂_x + v ∂_r .

Gas model: γ(T)-exact thermally perfect closure of record (phaseD §0);
everything below that needs only c² = c²(p, ρ) as a free positive
symbol is marked EOS-general, matching the record's status rule. The
S1 function class with H-ANN (r_min > 0 on annular geometry) and the
declared front set (T-fronts / C-fronts) is inherited from phaseD §0.

PRIMAL SYSTEM (D.1 of record, r-WEIGHTED normalization — every row
multiplied by r so that the Lagrange boundary flux is directly the
physical r-weighted surface density; the carrier
`n6_fivefield_adjoint.py` weights only the continuity row, and the two
conventions differ by the invertible diagonal diag(1, r, r, r, r),
multipliers related by ψ_i^{carrier} = r ψ_i^{here} for i = 2..5 —
declared, checked at (C1)):

  (E1)  ∂_x(r ρ u) + ∂_r(r ρ v) = 0
  (E2)  r [ ρ D u + ∂_x p ] = 0
  (E3)  r [ ρ D v + ∂_r p − ρ w²/r ] = 0
  (E4)  r [ ρ D w + ρ v w / r ] = 0
  (E5)  r [ D p − c² D ρ ] = 0        (entropy transport, (p,ρ) form)

E4 is equivalent to the record's Γ-transport row: ρ D Γ = r·(E4-row)/r
identically (ρDΓ = ρ(rDw + vw) = r[ρDw + ρvw/r]); the contract's
"evaluator carries Γ as its transport row" (D.13) is the same row up
to the factor r, multiplier dictionary in §2.4. The objective is the
per-phase axial thrust through the fixed exit surface S_e (a plane
x = x_e of the marched domain; 2π factor dropped throughout):

  J(ξ) = ∫_{S_e} [ ρ u (u n_x + v n_r) + (p − Pa) n_x ] r dl
       = ∫_{S_e} r (ρ u² + p − Pa) dr        (n = e_x).

Note the integrand does NOT read w: swirl contributes no axial
momentum flux directly (PROVEN-IN-RECORD, N6-2 scope note). Everything
swirl does to J it does through the state and through the couplings
derived below.

==============================================================================
## §1 Linearization: the (A, B, M) structure

Fréchet derivative at V in direction δV = (δρ, δu, δv, δw, δp):
L δV = A ∂_x δV + B ∂_r δV + M δV, machine-extracted with zero
leftover (check C1; the unweighted twin is carrier check 5F.1 of
record). Rows i = residual rows, columns j = state components.

  A = r · ⎡ u      ρ      0      0      0   ⎤
          ⎢ 0      ρu     0      0      1   ⎥
          ⎢ 0      0      ρu     0      0   ⎥
          ⎢ 0      0      0      ρu     0   ⎥
          ⎣ −c²u   0      0      0      u   ⎦

  B = r · ⎡ v      0      ρ      0      0   ⎤
          ⎢ 0      ρv     0      0      0   ⎥
          ⎢ 0      0      ρv     0      1   ⎥
          ⎢ 0      0      0      ρv     0   ⎥
          ⎣ −c²v   0      0      0      v   ⎦

  M = ⎡ ∂_x(ru)+∂_r(rv)   ∂_x(rρ)   ∂_r(rρ)      0        0          ⎤
      ⎢ r Du               rρu_x     rρu_r        0        0          ⎥
      ⎢ r(Dv − w²/r)       rρv_x     rρv_r      −2ρw       0          ⎥
      ⎢ r(Dw + vw/r)       rρw_x     ρ(rw_r+w)   ρv        0          ⎥
      ⎣ −r c²_ρ Dρ         r(p_x−c²ρ_x)  r(p_r−c²ρ_r)  0   −r c²_p Dρ ⎦

(c²_ρ := ∂c²/∂ρ|_p, c²_p := ∂c²/∂p|_ρ.) The swirl-specific entries
are boxed by inspection:
 * M[2,3] = −2ρw — the CENTRIFUGAL coupling (∂(ρw²/r)/∂w, r-weighted);
   this is the entry whose corruption the record rejector R1 (carrier)
   and my rejector (R1, check script) both catch;
 * M[3,1] = rρw_x = ρΓ_x and M[3,2] = ρ(rw_r + w) = ρΓ_r — the
   BASE-SWIRL-GRADIENT couplings (the linearized advection of w by
   δu, δv), which are exactly ρ∇Γ;
 * M[3,0], M[2,0] carry w²/r and vw/r in the density column.
Everything else is the meridional (u,v) structure. [PROVEN-HERE +
PROVEN-IN-RECORD: the unweighted (A,B,M) is carrier content 5F.1; the
r-weighted extraction is check C1.]

==============================================================================
## §2 The adjoint system

### 2.1 Transpose

Formal adjoint (Lagrange identity, carrier 5F.3 of record, EXACT
divergence):

  L* ψ = −∂_x(Aᵀψ) − ∂_r(Bᵀψ) + Mᵀψ ,     ψ = (ψ₁, ψ₂, ψ₃, ψ₄, ψ₅)

with ψ_i the multiplier of primal row i (mass, x-mom, r-mom,
w-transport, entropy/pressure). Interior adjoint equation L*ψ = 0
(the thrust objective is a pure boundary functional; no interior
source).

### 2.2 Advective form (the derived, machine-checked display)

Expanding the transpose and using ONLY product rule plus, where
marked, the primal continuity row (E1) (the exact bookkeeping
Lstar_j = ADV_j + coeff_j·E1 with coeff = (0, −ψ₂, −ψ₃, −ψ₄, −ψ₅/ρ)
is what check (C2) verifies identically — no on-shell substitution
other than E1 is used):

  (A-ρ)   r D ψ₁ = ∂_x(r c² u ψ₅) + ∂_r(r c² v ψ₅)
                   + r (Du) ψ₂ + r (Dv − w²/r) ψ₃
                   + r (Dw + vw/r) ψ₄ − r c²_ρ (Dρ) ψ₅

  (A-u)   D ψ₂ = −∂_x ψ₁ + u_x ψ₂ + v_x ψ₃ + (Γ_x/r) ψ₄
                   + (p_x − c² ρ_x) ψ₅ / ρ                    [uses E1]

  (A-v)   D ψ₃ = −∂_r ψ₁ + u_r ψ₂ + v_r ψ₃ + (Γ_r/r) ψ₄
                   + (p_r − c² ρ_r) ψ₅ / ρ                    [uses E1]

  (A-w)   D ψ₄ = ( v ψ₄ − 2 w ψ₃ ) / r                        [uses E1]

  (A-p)   D ψ₅ = −(1/r)[ ∂_x(r ψ₂) + ∂_r(r ψ₃) ]
                   + (Dρ) (1/ρ − c²_p) ψ₅                     [uses E1]

[PROVEN-HERE, machine-checked (C2).]

On-shell simplifications (substituting the primal equations into
(A-ρ)): Du = −p_x/ρ, Dv − w²/r = −p_r/ρ, Dw + vw/r = 0, Dρ = Dp/c²,
so

  (A-ρ)'  r D ψ₁ = ∂_x(r c² u ψ₅) + ∂_r(r c² v ψ₅)
                   − (r/ρ)(p_x ψ₂ + p_r ψ₃) − r (c²_ρ/c²)(Dp) ψ₅ ,

i.e. ON SOLUTIONS the mass-adjoint row has IDENTICALLY the meridional
form: the explicit centrifugal entry −w²/r ψ₃ of the transpose is
absorbed by the swirl part of the base radial pressure gradient, and
the geometric pairing (Dw + vw/r)ψ₄ vanishes because its coefficient
is the primal w-residual. [PROVEN-HERE, two-line substitution shown.]

Also note (p_x − c²ρ_x, p_r − c²ρ_r) = (∂p/∂s)_ρ ∇s: the ψ₅ couplings
in (A-u)/(A-v) vanish on homentropic base flow — the classical
Giles-Pierce structure, unchanged by swirl. [PROVEN-HERE, one line
from dp = c²dρ + (∂p/∂s)_ρ ds.]

### 2.3 The swirl-adjoint transport and its invariant form

(A-w) rewritten:

  D ( ψ₄ / r ) = − (2 w / r²) ψ₃ = − (2 Γ / r³) ψ₃ .        (★)

[PROVEN-HERE, machine-checked (C4).] Reading: define ψ_Γ := ψ₄/r —
this is EXACTLY the multiplier of the record's Γ-transport row (the
row dictionary of §0: Γ-row = r × w-row, so its multiplier is ψ₄/r).
Then:

  THE ADJOINT SWIRL VARIABLE ψ_Γ IS TRANSPORTED ALONG MERIDIONAL
  STREAMLINES, BACKWARD FROM THE EXIT, PUMPED BY A SINGLE SOURCE:
  THE CENTRIFUGAL PAIRING −(2Γ/r³) ψ₃.

This is the exact adjoint mirror of the primal structure (primal: Γ
streamline-invariant, feeding r-momentum through ρΓ²/r³; adjoint: ψ_Γ
streamline-transported, fed BY the r-momentum multiplier through
2Γ/r³). It is also the precise dual statement of D.19's pumping
identities (primal 3-D: Γ pumped by ∂_φp only; per-phase adjoint: ψ_Γ
pumped by centrifugal pairing only) — a structural rhyme, not an
identity between the two.

### 2.4 What is NEW relative to the meridional (u,v) adjoint

The meridional adjoint of record is the transpose of the 4-field
(ρ, u, v, p) system (the current engine's reverse-AD march, VI.4bis
(iv)). Diffing §2.2 against it:

 (N1) ONE NEW ADJOINT FIELD ψ₄ (equivalently ψ_Γ = ψ₄/r) with its own
      backward streamline transport (A-w)/(★). It needs NO boundary
      condition at wall, axis, or inflow (§3); its exit datum is 0
      (§3.2). [PROVEN-HERE]
 (N2) THE CENTRIFUGAL TRANSPOSE COUPLING −2ρwψ₃ (M[2,3]ᵀ): the only
      source of ψ₄. Vanishes iff wψ₃ ≡ 0. [PROVEN-HERE]
 (N3) THE SWIRL-GRADIENT FORCINGS (Γ_x/r)ψ₄ in (A-u) and (Γ_r/r)ψ₄
      in (A-v): the only feedback of ψ₄ into the meridional block.
      They vanish IDENTICALLY on the free-vortex class Γ ≡ const
      (machine-checked, C5) — the adjoint-side reproduction of N6-2
      (Rao machinery verbatim on free vortex, no swirl multiplier
      needed) and of the N6-3 obstruction (the couplings are alive
      exactly when ΓΓ′ ≠ 0, the obstruction's Γ-leg). [PROVEN-HERE;
      consistency anchor PROVEN-IN-RECORD N6-2/N6-3.]
 (N4) OFF-SHELL centrifugal/geometric entries in the mass-adjoint row
      that CANCEL ON SOLUTIONS ((A-ρ)′): the ρ-row keeps the
      meridional form on-shell. An implementation transposing
      mechanically (reverse-AD) carries them automatically; a
      hand-coded adjoint that drops them is correct ONLY on exact
      solutions — a dual-consistency trap on unconverged iterates.
      [PROVEN-HERE]
 (N5) COEFFICIENT (STATE) SHIFTS: every c², T, ρ coefficient is
      evaluated at the swirl-shifted state h = h0 − W²/2 − Γ²/(2r²)
      (D.2(iii)); swirl cools the state and raises the meridional
      margin at fixed (h0, s, u, v, r) (PROVEN-IN-RECORD, D.5(ii)).
 (N6) THE GRADIENT AND BC STRUCTURE ARE FORM-INVARIANT: wall BC,
      exit datum shape, and the Hadamard gradient density (§4) have
      the same FORM as meridional; all new swirl content of dJ/dΣ
      flows through (N1)-(N3). No explicitly new boundary term
      appears. [PROVEN-HERE; reconciliation flag §10-F1.]
 (N7) A NEW DATA-SENSITIVITY ROW at the inflow: dJ/d(w-data) pairs
      with ρ u_n ψ₄ on Γ_d (§3.4) — the adjoint prices the swirl
      measurement bar (consumed by hypothesis (d) of §6). At a
      swirl-free base state ψ₄ ≡ 0, so ∂J/∂(swirl amplitude) = 0 at
      zero swirl: the thrust debit is quadratic in swirl amplitude —
      consistent with E_θ ∝ u_θ² (D.10). [PROVEN-HERE, from (N2) +
      uniqueness of the backward transport solve.]

==============================================================================
## §3 Adjoint boundary terms

Lagrange identity (carrier 5F.3, exact divergence):
∫_D [ψᵀLδV − δVᵀL*ψ] dx dr = ∮_{∂D} ψᵀ K(n) δV dl, K(n) := A n_x +
B n_r, n outward. Expanding rows (u_n := u n_x + v n_r, δu_n := δu n_x
+ δv n_r):

  ψᵀK(n)δV = r { ψ₁ (u_n δρ + ρ δu_n)
               + ρ u_n (ψ₂ δu + ψ₃ δv + ψ₄ δw)
               + (ψ₂ n_x + ψ₃ n_r) δp
               + ψ₅ u_n (δp − c² δρ) } .                       (BT)

### 3.1 Wall Σ (slip, u_n = 0)

At a fixed wall δu_n = 0 (linearized slip), so
BT|_Σ = r (ψ₂n_x + ψ₃n_r) δp. Since J does not read the wall, the
adjoint wall BC is

  ψ₂ n_x + ψ₃ n_r = 0   on Σ                                   (W)

— identical in form to the meridional adjoint slip condition. The
swirl row contributes ρu_nψ₄δw = 0 automatically: THE SWIRL ADJOINT
NEEDS NO WALL BC, mirroring the primal fact that the wall is a
streamline and Γ-transport never crosses it. [PROVEN-HERE]

### 3.2 Exit S_e (spacelike plane, M_x > 1)

At a supersonic (spacelike, D.4) exit the primal needs no BC, so δV is
free there and the adjoint must absorb δJ entirely:
δJ = ∫ r(u²δρ + 2ρuδu + δp) dr must equal BT|_{S_e} for all δV. With
n = e_x this forces five conditions (all five adjoint characteristics
leave backward through S_e — a full Cauchy datum, count consistent
with D.3/D.4 read backward):

  δρ: ψ₁ − c²ψ₅ = u ;  δu: ψ₁ + uψ₂ = 2u ;  δv: ψ₃ = 0 ;
  δw: ψ₄ = 0 ;         δp: ψ₂ + uψ₅ = 1 .

Solving (uniquely iff u² ≠ c²):

  ψ|_{S_e} = ( u, 1, 0, 0, 0 ) .                               (X)

[PROVEN-HERE; machine-checked (C3): (X) reproduces the thrust
integrand variation exactly.] Remarks: (i) the datum is identical to
the meridional thrust adjoint datum extended by ψ₄ = 0 — swirl is
invisible AT the exit and enters only upstream through (N2)/(N3);
(ii) the solve divides by (u² − c²): AT A SONIC EXIT THE DATUM
DEGENERATES — §5 risk R-4; (iii) for the wall-pressure form of the
thrust functional the wall BC (W) becomes inhomogeneous instead
(ψ₂n_x + ψ₃n_r = −n_x) and (X) homogenizes; the two forms differ by
the CV momentum balance and give the same gradient — standard, not
re-derived here [PRACTICE].

### 3.3 Axis r = 0 (bell family only; annular class has H-ANN)

Under meridional reflection r → −r of a smooth axisymmetric field:
(ρ, u, p) even, (v, w) odd. The residual rows then have parities
(odd, odd, even, even, odd), and the adjoint system maps
even↔odd solutions accordingly; the symmetric adjoint branch has
(ψ₁, ψ₂, ψ₅) even and (ψ₃, ψ₄) odd. Hence the axis conditions

  ψ₃ = ψ₄ = 0 ,  ∂_rψ₁ = ∂_rψ₂ = ∂_rψ₅ = 0  at r = 0 ,

and BT → 0 with the r-weight. Consistency: parity check of (A-w):
LHS D(odd) is odd; RHS (vψ₄ − 2wψ₃)/r = (even − even)/odd is odd. ✓
[PROVEN-HERE, parity argument as displayed. The DATA-side axis
constraint (Γ = O(r²)) is a separate model hypothesis — §6(f′).]

### 3.4 Inflow Γ_d (spacelike, full Cauchy data)

All primal characteristics enter ⟹ primal carries 5 data rows
(the D.13 contract); backward, all ADJOINT characteristics leave ⟹
the adjoint needs NO condition on Γ_d: the backward march simply ends
there, and the concomitant delivers the Green identity

  δJ|_data = ∮_{Γ_d} ψᵀ K(n) δV_data dl                        (G)

(n outward = against the inflow). Component of record for the new
row: the w-column of (G) is

  dJ/dw(y;ξ) = − r ρ u_n ψ₄ |_{Γ_d}(y)    (sign: n outward, u_n < 0
                                            at an inflow)

— the measurement-uncertainty weight for the contract's swirl row
(w(y;ξ) row of D.13). [PROVEN-HERE from (BT); consumed in §6(d).]

### 3.5 Interior fronts (fitted sheets, contacts)

Across fitted T-fronts the linearized RH conditions and their
transposes ride the existing front brick (K_p(n) 5×5, det ∝
u_n³(u_n² − c²), nonsingular inside Lax — PROVEN-IN-RECORD, N6-1 /
G12-S1 extension); the adjoint inherits front-interface conditions
from the transposed linearized RH plus the front-position multiplier
row. NOT re-derived here; the C-front (contact) case is a named risk
(§5 R-5, record anchor S.22 g2b). [PROVEN-IN-RECORD for the
structure; OPEN for the contact-crossing calculus.]

==============================================================================
## §4 Shape derivative / transversality with swirl

### 4.1 Hadamard derivation

Speed method: wall displaced along its outward normal ν (fluid →
solid) by δn; deformation field vanishes on S_e, Γ_d, axis. Since
E(V) = 0 pointwise in smooth regions, the domain-transport term of
the Lagrangian vanishes and

  dJ[δn] = − ∮_Σ ψᵀ K(ν) V̇ dl                                  (4.1)

with V̇ the local shape derivative of the flow. At the wall
(u_ν = 0), by (BT):
ψᵀK(ν)V̇ = r[ ρ ψ₁ u̇_ν + (ψ₂ν_x + ψ₃ν_r) ṗ ]; the adjoint wall BC (W)
kills the unknown ṗ, leaving dJ = −∮ r ρ ψ₁ u̇_ν dl.

Linearized slip on the displaced wall (normal-geodesic extension of
(ν, τ): ∂_νν = 0; s = arclength):

  u̇_ν = (δn)′ u_τ − δn (∂_ν u)·ν .

Continuity at the wall in wall coordinates (Lamé h_s = 1 + κn; at
u_ν = 0 the curvature term dies): rρ(∂_νu)·ν = −∂_s(rρu_τ). Hence

  r ρ u̇_ν = (δn)′ rρu_τ + δn ∂_s(rρu_τ) = ∂_s( r ρ u_τ δn )

— the compressible sliver/transpiration identity, derived, not
assumed. Integrating by parts along Σ:

  ┌──────────────────────────────────────────────────────────────┐
  │  dJ[δn] = ∮_Σ  ( ∂_s ψ₁ )  r ρ u_τ  δn  dl                  │
  │           − [ ψ₁ r ρ u_τ δn ]_endpoints                      │
  └──────────────────────────────────────────────────────────────┘

[PROVEN-HERE, full chain displayed. Scope: smooth wall segments;
front-foot and corner points excluded from the smooth formula.]

THE GRADIENT DENSITY IS G = rρu_τ ∂_sψ₁ — THE SAME FORM AS THE
MERIDIONAL ADJOINT. Every swirl effect enters through ψ₁'s coupling
to ψ₄ via (N2)/(N3) and through the swirl-shifted coefficients (N5).
No explicit Γ²/r³ boundary term appears; the centrifugal content of
the shape gradient is INTERIOR (routed through the adjoint solve).
See flag §10-F1 for reconciliation with the N6 §4 SCHEMA wording.

### 4.2 Endpoint / transversality terms

At the fixed upstream attachment δn = 0. At a free exit lip the
endpoint term −ψ₁rρu_τδn|_lip combines with the variation of the exit
integral's extent (the lip drags the S_e boundary): the assembled lip
condition is the swirl generalization of the Rao corner condition.
Two record facts pin its structure: (i) at a terminal meridional Mach
front (u_n = c) the transposed-symbol kernel is one-dimensional with
gauge direction l(n) = (1, −rn_x/c, −rn_r/c, 0, r/c²) whose SWIRL
COMPONENT IS ZERO (PROVEN-IN-RECORD, carrier 5F.4): the swirl
multiplier does not enter the terminal gauge, so the Hoffman-style
count of corner conditions is UNCHANGED by swirl; (ii) on the
free-vortex class the whole system collapses to Rao-with-W-meridional
(PROVEN-IN-RECORD, N6-2), so the assembled corner condition must
collapse to (L.15). The explicit assembled lip/corner formula beyond
these two pins: OPEN (it is the "corner conditions" leg of the [S-5F]
SCHEMA; this section supplies the endpoint identity it assembles
from).

### 4.3 Consistency checks of the formula

 (i) w → 0: couplings (N2)/(N3) vanish; (A-w) becomes homogeneous
     with datum 0 ⟹ ψ₄ ≡ 0; the system and dJ collapse EXACTLY to
     the meridional adjoint and its gradient. [PROVEN-HERE]
 (ii) free vortex (Γ ≡ Γ₀): (N3) ≡ 0 (machine-checked C5): the
     meridional adjoint block closes by itself (with swirl-shifted
     coefficients); ψ₄ is a passive functional of ψ₃. dJ/dΣ needs no
     swirl multiplier — the adjoint-side statement of N6-2.
     [PROVEN-HERE + PROVEN-IN-RECORD]
 (iii) beyond free vortex: (N3) alive exactly when ∇Γ ≠ 0, i.e.
     exactly where the N6-3 obstruction kills the pointwise closure —
     the adjoint derivation and the record's necessity theorem agree
     on WHERE field-level machinery is mandatory. [PROVEN-HERE +
     PROVEN-IN-RECORD N6-3]

==============================================================================
## §5 Well-posedness and numerical risks of the five-field adjoint

R-1 CHARACTERISTIC STRUCTURE VS PRIMAL. The adjoint pencil equals the
  primal pencil exactly: det(B − λA) = r ρ³ (v − λu)³ [(v − λu)² −
  c²(1 + λ²)] and transposition preserves it (PROVEN-IN-RECORD,
  carrier 5F.2). Adjoint information flows BACKWARD: the backward
  x-march is well-posed under the same spacelikeness criterion
  M_n > 1 (D.4 curved clause), with the same margin m_n(ξ); Γ never
  enters the criterion (D.3(c)). Swirl COOLS the state at fixed
  (h0, s, u, v, r), so at equal meridional data the margin RISES
  (D.5(ii)); the TOTAL-MACH HAZARD stands: any monitor using M_tot
  overstates the margin and can license an ill-posed adjoint march
  exactly as a primal one (D.5(iii)). All PROVEN-IN-RECORD; the
  backward-reading is PROVEN-HERE (trivial: transposition +
  time-reversal of the march direction).

R-2 AXIS BEHAVIOR (bell family). Adjoint side: benign — ψ₃ = ψ₄ = 0
  at the axis by parity (§3.3), all coefficients of (A-w) bounded
  when the DATA are axis-regular (w = O(r), Γ = O(r²)). The risk is
  DATA-side: a contract row with Γ ↛ 0 on the inner streamtube makes
  w = Γ/r and the source ρΓ²/r³ blow up — a model-class violation,
  not an adjoint pathology. Meter: a contract audit row
  sup_y |Γ(y)|/y² < ∞ near the axis for bell-family phases.
  [PROVEN-HERE (parity, orders); PRACTICE (meter).]

R-3 Γ²/r³ STIFFNESS NEAR AN INNER BODY (spike/centerbody).
  Primal: centrifugal-to-inertia ratio along the wall,
    (ρΓ²/r³)/(ρW²/L_x) = (u_θ/W)² · (L_x/r).
  With the record scales (tangential energy fraction 3-6% ⟹
  (u_θ/W)² ≈ 0.03-0.065) and L_x/r ≈ 5-20 near a spike tip, the
  ratio is 0.15-1.3: the source reaches O(1) — first-order, not
  perturbative — and its r-sensitivity ∂_r(Γ²/r³) = −3Γ²/r⁴ scales
  the local Lipschitz constant like r_min⁻⁴ (step control ∝ r_min).
  Adjoint: the couplings are ONE power milder (2Γ/r³ in (★), ∇Γ/r in
  (N3)), but backward integration through the tip region amplifies
  ψ_Γ by up to exp(∫ 2u_θ/(rW) ds) ≈ exp(2(u_θ/W)(Δs/r)); with
  u_θ/W ≈ 0.17-0.25 and Δs/r ≈ 3-10 the factor is exp(1-5): worst
  case O(10²) amplification on the innermost streamtube.
  [SCALING-ESTIMATE, derivations displayed; consonant with the
  record's 1/y_min² weighting of the OBS estimator (D.14).]
  Mitigation (PRACTICE): integrate the invariant form (★) in ψ_Γ
  (one bounded source), not raw ψ₄; z-space unit-consistent Newton
  certification (A1-brick practice) extended to the swirl row.

R-4 SONIC-LINE DEGENERACY. Interior: same locus, same multiplicity as
  meridional — the pencil is Γ-independent (D.3(c)); at u_n = c the
  transposed symbol has a ONE-dimensional kernel with the swirl-free
  gauge direction (5F.4): no NEW degeneracy channel from swirl
  [PROVEN-IN-RECORD]. NEW precise statement: the exit datum (X)
  solves a linear system with determinant ∝ (u² − c²); at a sonic
  exit point (u → c on S_e, e.g. a marginally choked tip streamtube)
  the thrust-adjoint datum BLOWS UP like 1/(u² − c²) — the adjoint
  inherits the primal's sonic-exit fragility in its DATA, not its
  operator. Meter: exit-plane margin ess inf (M_x − 1) declared per
  phase (already the L4/m_n discipline). [PROVEN-HERE]

R-5 CONTACTS (C-fronts) FROM ALTERNATING-Γ DATA. In-slice, a jump of
  Γ (or s, h0) at an interior ψ-level evolves as a contact curve
  (D.13 class-adequacy note). On it, the coupling coefficient
  Γ_r/r in (A-v) is a MEASURE (atom on the contact): ψ₃ develops a
  transverse kink, and classical backward integration across the
  contact is out of the smooth calculus. The primal comparison
  theorem already owns this wall (S.22 g2b, record); the ADJOINT
  version (transposed contact conditions, gradient continuity when a
  contact foot moves with the shape) is OPEN — named residue, same
  owner class as g2b. Practical exposure: alternating-sign Γ data
  GENERICALLY carry such contacts (sector boundaries); a smooth-
  calculus adjoint code will show grid-dependent gradient noise
  concentrated on contact feet. Meter: dot-product (O3.1-class) test
  run on a deliberately contact-carrying datum vs a mollified twin;
  divergence localizes the defect. [OPEN, meter named.]

R-6 BACKWARD CANCELLATION STIFFNESS. ψ_Γ is pumped by −(2Γ/r³)ψ₃
  with Γ alternating in ξ across the family but FIXED in sign within
  one phase slice along a streamline; within-slice integration is
  cancellation-benign, but the FAMILY assembly dJ = ∫dJ(ξ)dμ pairs
  large near-tip ψ_Γ values of opposite signs across phases:
  family-level quadrature must resolve the ξ-alternation (trapezoid-
  on-circle licensing per VI.4bis(i)). [PRACTICE, consequence of
  (★) + alternating data; no new theorem content.]

R-7 DISCRETE-ADJOINT DUALITY. The route of record is reverse-AD of
  the fitted march (VI.4bis(iv)), which transposes (N1)-(N4)
  automatically — INCLUDING the off-shell entries (N4) that a
  hand-simplified continuous adjoint drops. Risks: (i) unconverged
  per-cell Newton solves break the implicit-function transpose
  hardest where the source is stiffest (R-3 region); (ii) the swirl
  row must enter the O3.1-class dot-product oracle and an R1-class
  corruption rejector (both exist at carrier level: 5F.3-R1 and my
  check-script R1 — neither yet wired into the ENGINE's oracle
  suite). [PRACTICE; instruments named.]

==============================================================================
## §6 Hidden physical hypotheses of the five-field model AS A MODEL OF
##    THE TRUE FLOW (the ledger)

Each row: hypothesis / violation channel / error direction where
derivable / meter-falsifier.

### (a) Frozen inviscid Γ transport, zero mixing

HYPOTHESIS (E4/E5 exact: Γ and s streamline-invariant; the
alternating-sign Γ(y;ξ) pattern advects unmixed to the exit).
Real flows mix turbulently (adjacent sectors/annuli with opposite Γ
exchange momentum; swirl KE → turbulence → heat).

DIRECTION OF THE ISP ERROR — derived, two channels:

 (a-1) ENERGY CHANNEL [PROVEN-HERE under the named hypotheses].
  Within the vaneless axisymmetric class the frozen model writes off
  the exit swirl KE entirely: debit E_θ = Σ ṁ_i Γ_i²/(2r_{e,i}²)
  (D.10, positive-definite, unrecoverable-in-class). Mixing instead
  dissipates swirl KE q per unit mass to heat AT LOCAL PRESSURE p_m
  and the heated stream then expands to p_e. Gibbs (dh = Tds + dp/ρ):
  dissipation at p_m adds ds = q/T_m; isentropic continuation to the
  SAME p_e shifts exit enthalpy by δh_e = T_e δs = q T_e/T_m; exit
  KE gains q − qT_e/T_m = q(1 − T_e/T_m) > 0. So EVERY unit of swirl
  KE mixed upstream of the exit returns the positive fraction
  (1 − T_e/T_m); the frozen model returns 0.
  ⟹ ON THE ENERGY CHANNEL, FROZEN TRANSPORT OVERSTATES THE SWIRL
  DEBIT AND UNDERSTATES Isp: the five-field prediction is
  CONSERVATIVE (a lower bound on the swirl-channel recovery), with
  bias bounded by E_θ(1 − T_e/T_m)/2 per unit KE flux. Numbers
  (record scales): E_θ/KE = 3-6%, (1 − T_e/T_m) ≈ 0.3-0.6 for
  typical p_m/p_e ⟹ δIsp/Isp ≈ ½·(0.03-0.06)·(0.3-0.6) ≈ 0.5-2%.
  [Sign PROVEN-HERE (Gibbs two-liner displayed); magnitude
  SCALING-ESTIMATE. Hypotheses consumed: mixing completed at
  p_m > p_e; vaneless class; matched exit pressure per streamtube;
  wall friction excluded (separate row).]

 (a-2) RADIAL-EQUILIBRIUM (PRESSURE-REDISTRIBUTION) CHANNEL
  [SCALING-ESTIMATE, sign family-dependent]. Killing u_θ also kills
  the radial pressure gradient ∂p/∂r = ρu_θ²/r that swirl maintains:
  the swirled flow holds inner surfaces BELOW and outer surfaces
  ABOVE the mass-mean pressure. Mixing therefore RAISES pressure on
  a centerbody/spike (inner wall) and LOWERS it on a shroud/bell
  outer wall, at magnitude Δp ~ ρu_θ² × O(annulus geometry) — the
  same formal order as (a-1).
  ⟹ PLUG/SPIKE FAMILY: both channels have the SAME sign — the
  frozen model UNDERSTATES Isp unambiguously (overstates the debit).
  BELL/SHROUD FAMILY: (a-2) opposes (a-1); the NET direction is
  OPEN pending a computed twin (falsifier below). Note the family
  asymmetry of the ERROR mirrors the record's recovery asymmetry
  (swirl physics concentrates against inner bodies) — consistent,
  not coincidental: same Γ²/r-weighting.

 METERS / FALSIFIERS: (i) two-station swirl-KE flux audit — A4
  computed at Γ_d AND at S_e on any ingested 3-D dataset: the DECAY
  between stations is the direct mixing meter (frozen model predicts
  zero decay along Euler-clean streamtubes); (ii) the D.16 R_AM row
  CANNOT see mixing (turbulent exchange is internal torque; the
  flux-weighted mean Γ is conserved) — do not cite R_AM as a mixing
  audit [PROVEN-HERE, one line: mixing stresses are internal to the
  CV]; (iii) pre-registrable prediction: a RANS/LES twin at matched
  contract data must show Isp ≥ the five-field prediction on
  plug-family geometry (violation kills (a-1)'s hypothesis set or
  the model class); (iv) pattern-persistence meter: sector wavelength
  / turbulent diffusion length ratio at record scales decides
  whether mixing completes in-nozzle.

### (b) Vaneless axisymmetric class

HYPOTHESIS (wetted surfaces are surfaces of revolution; no vanes,
struts, MHD — H-AM3/H-AM5 of record). Violation channel: any static
structure exerting torque converts the "unrecoverable" E_θ verdict
into a design variable (turning vanes recover swirl KE; the D.10 r1
scope repair says exactly this). Meters: D.6/D.16 torque bookkeeping
(a vaned CV must declare its torque or fail R_AM); geometry census.
[PROVEN-IN-RECORD (D.10 scope note, H-AM3); nothing new here — the
row is listed because the five-field ADJOINT inherits it: the
gradient formula of §4 is derived on a slip surface of revolution
and is FALSE on a vaned wall.]

### (c) In-slice steadiness (∂_φ = 0 within the slice)

HYPOTHESIS (the per-phase reduction itself). The dropped objects are
EXACTLY the six K-rows of D.18 — now with LIVE swirl content: K_Γ =
ρ(w_rel/r)∂_φΓ + ∂_φp and K_h0 both nonzero on swirl-carrying data.
St_n ~ 0.1-1 of record: MARGINAL, not small (problem book §8).
Violation channel: everything S.22 prices (sweep transport, azimuthal
pressure coupling); the T3QS ray-cancellation protection was proven
at SWIRL-FREE data (T3QS §2 "D(W) at swirl-free data splits...") —
its extension to Γ-carrying ray families is NOT of record (§10-F2):
until extended, the smooth-cycle J₁ = 0 protection MAY NOT be
invoked for the five-field upgrade. Meter: the J₁ sweep bar (one
linearized solve per VI.4bis(ii)) — irreducible, §7; T0-flatness
monitor. [HYPOTHESIS, with the protection-gap FLAGGED.]

### (d) Measurability of the contract field w(y;ξ)

HYPOTHESIS (the D.13 contract row can be FILLED: per-phase swirl
profiles at the interface exist as data). The record's empirical
vacuum is total (D.12: NO published time-mean tangential profile in
the read corpus — and per-phase is strictly harder than time-mean).
Violation channel: rows filled from a CFD generator inherit the
generator's provenance class; the design gradient then differentiates
a modeled boundary condition. NEW INSTRUMENT FROM THIS DERIVATION:
the Green row (§3.4) dJ/dw(y;ξ) = −rρu_nψ₄|_{Γ_d} PRICES the needed
measurement accuracy — the acceptable swirl-data error is
δw ≤ tol_J / ∮|rρu_nψ₄|, computable per campaign from the adjoint
solve itself (derived bars, no magic constants). Meter: G-e window
(first dataset: F1-F4 + A4); falsifier of the vacuum: exhibit a
published per-phase (or even time-mean) tangential profile.
[HYPOTHESIS; instrument PROVEN-HERE as a formula, PRACTICE as a
protocol.]

### (e) Front pumping of Γ lives in the residual

HYPOTHESIS (all Γ structure is inherited from Γ_d; no in-nozzle
pumping). The exact 3-D flow pumps Γ along relative streamlines at
rate D_relΓ = −(1/ρ)∂_φp (D.19(i), THEOREM model-internally): in the
per-phase model this pumping sits ENTIRELY in K_Γ (residual), i.e. it
is dropped, not represented. Since the interface value u_θ/(Ωr) ≈
0.15-0.2 IS accumulated pumping (upstream of Γ_d), the in-nozzle
increment over one transit scales as the SAME mechanism × St_n ×
(downstream ∂_φp decay factor): fractional Γ drift O(St_n · decay) —
potentially tens of percent at St_n ~ 0.5 with slow decay, vanishing
where the wave's azimuthal pressure signature dies at the throat
(choked-dam argument, T3QS B2). [SCALING-ESTIMATE, honest spread
declared: the decay factor is data-dependent and unmeasured.]
Violation channel: designs whose gradient credits Γ conservation on
streamtubes that actually gain/lose Γ in the divergent section.
Meter: PER-PHASE two-station Γ(ψ) comparison on a 3-D dataset (the
cycle-MEAN audit D.16 is blind to this by ∮∂_φp dφ = 0 — the mean
flux nullity D.6 survives pumping [PROVEN-HERE, one line]; only the
phase-RESOLVED comparison sees it). Falsifier: measured per-phase
exit Γ(ψ) differing from inflow Γ(ψ) beyond quadrature bars on
Euler-clean data kills the frozen-inheritance hypothesis at the
measured level.

### Unlisted hypotheses surfaced by this derivation

 (f) H-REACH/H-FIB streamtube topology (D.2): every streamline meets
   Γ_d exactly once — consumed by Γ(ψ), s(ψ), h0(ψ) AND by the
   adjoint transport (★) (ψ_Γ is only determined by backward
   transport if streamlines reach the exit). Violation: recirculation
   at a spike base / separation bubble. Meter: through-flow guard
   δ_tf + streamline census (record). [PROVEN-IN-RECORD as a primal
   hypothesis; PROVEN-HERE that the ADJOINT consumes it too.]
 (f′) axis-regularity of swirl data for bell-family phases
   (Γ = O(r²)): §5 R-2. [HYPOTHESIS; meter named there.]
 (g) Mode purity / Z_n identical waves: the ξ ↔ φ identification
   (D.17) that DEFINES the per-phase family consumes strict T0; the
   whole five-field upgrade lives inside the pin. Meter: T0-flatness
   + the side-load lemma channel (n = 1 rotating side load as
   impurity detector, [T-SLRW]). [PROVEN-IN-RECORD]
 (h) Frozen composition, thermally perfect (scope pin 2026-08-11):
   swirl-KE dissipation (row (a)) raises T; if it re-crosses ignition
   thresholds the H-R1 causal-separation row is violated
   (afterburning). Meter: H-R1's energy-flux conservation residual
   row (problem book §9). [PROVEN-IN-RECORD row; the (a)-(h) coupling
   surfaced here.]
 (i) h0 CONVENTION with swirl: the contract's h0(y;ξ) must include
   u_θ²/2 (h0 = h + (u²+v²+w²)/2, D.1); probe data reporting
   meridional stagnation quantities under-book the swirl energy by
   exactly the E_θ fraction. Violation channel: silent convention
   mismatch at ingestion. Meter: contract provenance audit row
   (declare which stagnation convention the generator uses); the
   D.20 rothalpy diagnostic (Δh0 = Ω ΔΓ linkage) fires on
   convention-inconsistent data. [HYPOTHESIS, meter of record.]

==============================================================================
## §7 Claims analysis: which certification instruments RETIRE at five
##    fields, which REMAIN irreducible

### RETIRE (function moves inside the solve/gradient)

 1. WORST-CASE E_θ DEBIT BAR → COMPUTED RESIDUAL. At five fields,
    E_θ(ξ) = ∫_{S_e} ρu_n u_θ²/2 dA is an OUTPUT of every per-phase
    solve. The T3-CONTROL input (5) ("E_θ debit reported beside the
    TWIN-C twin") stops being an externally estimated worst-case bar
    and becomes a computed, phase-resolved residual with quadrature
    bars. What retires is the PRICING role (worst-case hand bar);
    the REPORTING row survives verbatim (it is how cross-code
    comparisons stay honest). [PROVEN-HERE at the definition level.]
 2. FAMILY-LEVEL RECOVERY-ASYMMETRY ADJUDICATION → IN-GRADIENT.
    The T-T3-MAP(c) clause ("recovery asymmetry signs AGAINST the
    plug family", per-streamline THEOREM* on the free-vortex class)
    was an EXTERNAL argument adjudicating swirl's family-level tilt.
    §8 verifies the same sign content is CONTAINED in dJ/dΣ through
    (N2)/(N3): WITHIN a family the tilt is now a gradient component
    the optimizer follows; ACROSS families it is a computed ΔJ
    between sector-tournament branches, no longer an a-priori
    argument. What retires is the adjudication-by-asymmetry-argument;
    what remains is the tournament itself (families are disconnected
    topology sectors — a gradient cannot cross them). [PROVEN-HERE
    (§8) + PROVEN-IN-RECORD (tournament, VI.5).]
 3. THE D.14 LICENSING LEG'S DESIGN-BLOCKING ROLE (partial). The OBS
    monitor's job of record is to license the N6-2 CLOSED FORM;
    VI.4bis(iv) already mandates field-level machinery for rotational
    data, and the five-field engine IS that machinery: for DESIGN,
    nothing needs the closed-form license anymore, so the unproven
    G-b1 sensitivity lemma stops BLOCKING the design route. It
    remains live for the ORACLE role (N6-2 as initializer/oracle
    needs the license to be trusted as a check). [PROVEN-HERE at the
    role level; G-b1 itself untouched — it does not close, it
    de-scopes.]

### REMAIN irreducible (and why five fields cannot absorb them)

 4. THE J₁ SWEEP BAR. Five fields refine the IN-SLICE physics; they
    do not touch the ∂_φ coupling — the K-rows (D.18) are dropped by
    the five-field model exactly as by the meridional one, and now
    carry MORE live content (K_Γ, K_h0 nonzero on swirl data).
    J₁ = −∫⟨ψ_J, D(W_A)⟩dξ remains the mandatory first-order bar
    (VI.4bis(ii)); moreover the T3QS smooth-cycle cancellation is
    NOT licensed on swirl-carrying families until X-T3QS is extended
    (flag §10-F2) — with swirl the bar must be COMPUTED, not argued
    away. [PROVEN-IN-RECORD + flag PROVEN-HERE.]
 5. TWIN DISCIPLINE FOR CROSS-ENGINE COMPARISONS. TWIN-C
    (flux-consistent) fairness and the TWIN-B prohibition are
    statements about DATA aggregation conventions, not about model
    resolution: a five-field engine fed by per-phase data still
    needs the declared matching when compared to any steady/averaged
    calculation. D.10's twin clauses survive verbatim. Note
    ironically the five-field engine RETIRES TWIN-A for internal use
    (it can just carry the swirl), which strengthens, not weakens,
    the discipline for external comparisons. [PROVEN-IN-RECORD,
    role-shift PROVEN-HERE.]
 6. MODE-PURITY PIN. The entire per-phase construction (ξ ↔ φ,
    D.17; the exact quotient, S-T0P stage 1) consumes strict T0.
    Five fields inherit the pin unchanged; T0-flatness monitoring
    stays mandatory in every data contract (VI.4bis(v)).
    [PROVEN-IN-RECORD]
 7. D.16 R_AM ANGULAR-MOMENTUM AUDIT. Ingestion integrity of the
    Γ data row: five fields make the audit MORE load-bearing (the
    engine now consumes Γ quantitatively), and §6(a) shows R_AM
    cannot be replaced by model-internal checks (blind to mixing).
    [PROVEN-IN-RECORD + PROVEN-HERE (blindness).]
 8. NEW IRREDUCIBLE ROW (from §6(a)): the FROZEN-TRANSPORT DIRECTION
    BOUND + two-station A4 decay meter — a five-field engine cannot
    audit its own zero-mixing hypothesis; the meter is external by
    construction. [PROVEN-HERE]

==============================================================================
## §8 Optimization landscape with swirl

### 8.1 Sign structure of the new gradient content: outward- vs
###     inward-turning perturbations

Per-streamtube primal computation (PROVEN-HERE; hypotheses: fixed
per-tube (ṁ, h0, s, Γ), exit pressure matched at p_e, vaneless
class). Exit axial KE per unit mass:
u_e² = 2[h0 − h(p_e, s)] − v_e² − Γ²/r_e². A contour perturbation
that migrates the tube's exit radius by δr_e at fixed p_e:

  δ(ṁ u_e) = ṁ (Γ² / (u_e r_e³)) δr_e .                       (8.1)

OUTWARD migration (δr_e > 0: bell/shroud-ward turning) of a
swirl-carrying streamtube RAISES its thrust contribution at rate
Γ²/r³; INWARD migration (plug-ward concentration) debits it at the
same rate. This is exactly the record's recovery-asymmetry content —
"Γ²/(2r²) decays outward, concentrates inward, signs AGAINST the
plug family" (T-T3-MAP(c), per-streamline THEOREM* on free vortex) —
REPRODUCED: (8.1) restricted to the free-vortex class is the same
per-streamline statement, and the sign favors outward-turning
perturbations. VERIFIED, no flag.

IN-GRADIENT verification: the derived dJ/dΣ (§4.1) equals the
directional derivative of J by the Lagrange identity
(machine-verified exact divergence, 5F.3 + C2); on the migration
family above the directional derivative is (8.1); hence dJ/dΣ
CONTAINS (8.1)'s sign content — via the chain: outward δn → sliver
mass term ∂_s(rρu_τδn) → ψ₁ whose upstream structure is coupled to
ψ₄ by (N3) (∇Γ ≠ 0) and ψ₄ to ψ₃ by (N2). The identification is by
DUALITY, not term-by-term; the free-vortex corner where (N3) dies is
exactly where (8.1) reduces to the record's N6-2 statement.
[PROVEN-HERE, with the duality step carried by the machine-verified
Lagrange identity; the record statement PROVEN-IN-RECORD.]
Consonant external anchor (declared, not load-bearing): the
unexplained Paxson–Miki shroud-shift observation (record litreview
F6) has exactly this sign.

### 8.2 New nonconvexity?

 (i) SMALL-SWIRL REGIME: by (N7), ∂J/∂(swirl amplitude) = 0 at zero
   swirl and the debit is quadratic (E_θ): swirl adds a smooth
   quadratic penalty near Γ = 0 — NO new small-amplitude
   nonconvexity or bifurcation of stationary points. [PROVEN-HERE]
 (ii) FINITE SWIRL, WITHIN-FAMILY: the swirl contribution to J along
   the radial-migration direction behaves like −Γ²/(2r_e²)·(recovery
   weight): first derivative +Γ²/r³ > 0 (outward pull), second
   derivative −3Γ²/r⁴ < 0 — CONCAVE in the migration coordinate.
   For a MAXIMIZATION problem a concave reward adds no new local
   maxima by itself; what it does add is strong curvature ANISOTROPY
   near an inner body (Hessian entries scaling r_min⁻⁴, §5 R-3):
   ILL-CONDITIONING of the reduced Hessian, not nonconvexity. The
   characteristic geometry is Γ-independent (D.3(c)), so no new
   sonic-cap-type discontinuity mechanism is introduced by swirl.
   [PROVEN-HERE for the displayed derivatives; the global
   no-new-stationary-points statement is NOT claimed — composed with
   pressure/area trade-offs the landscape statement remains OPEN.]
 (iii) FAMILY-LEVEL (bell vs spike): the families are disconnected
   topology sectors adjudicated by tournament (VI.5) — already a
   discontinuous choice WITHOUT swirl. Swirl adds a systematic
   family-level OFFSET (the spike family holds streamtubes at
   smaller r, hence carries the larger debit at equal data, (8.1)
   integrated): it WIDENS the bell-spike gap in J, it does not
   create a new discontinuity in dJ/dΣ within either family.
   [PROVEN-HERE (offset sign, from (8.1)); magnitude
   SCALING-ESTIMATE: ΔJ_swirl/J ~ (E_θ/KE)·⟨1 − (r_bell/r_spike)²⟩
   ~ 1-4% between families at record scales.]
 (iv) HONEST CAVEAT: with alternating-Γ DATA carrying contacts, the
   gradient's dependence on the DATA has BV (kinked) structure at
   contact ψ-levels (§5 R-5): the map (contour) ↦ dJ is smooth, but
   the map (data) ↦ dJ has corners — family-level optimization over
   uncertain data inherits nonsmoothness from the data side. [OPEN,
   S.22 g2b anchor.]

==============================================================================
## §9 Claim register (labels on every claim of this document)

| # | Claim | Label | Anchor/check |
|---|---|---|---|
| 1 | (A,B,M) of the r-weighted five-field linearization as displayed §1 | PROVEN-HERE | check C1; unweighted twin = carrier 5F.1 (PROVEN-IN-RECORD) |
| 2 | Advective adjoint rows (A-ρ)...(A-p) equal the mechanical transpose mod declared E1 multiples | PROVEN-HERE | check C2 (+R1 rejector fires) |
| 3 | ψ_Γ = ψ₄/r transported with single source −(2Γ/r³)ψ₃ (★) | PROVEN-HERE | check C4 |
| 4 | On-shell meridional form of the mass-adjoint row (A-ρ)′ | PROVEN-HERE | substitution displayed §2.2 |
| 5 | New-vs-meridional term list (N1)-(N7) | PROVEN-HERE | §2.4; C5 for the free-vortex decoupling |
| 6 | Adjoint wall BC ψ_m·ν = 0; no wall/axis/inflow BC for ψ₄ | PROVEN-HERE | §3.1, §3.3, §3.4 |
| 7 | Exit adjoint datum ψ = (u,1,0,0,0), unique iff u² ≠ c² | PROVEN-HERE | check C3 |
| 8 | Inflow Green row dJ/dw = −rρu_nψ₄ on Γ_d | PROVEN-HERE | §3.4 from (BT) |
| 9 | Axis parity conditions ψ₃ = ψ₄ = 0 | PROVEN-HERE | §3.3 parity argument |
| 10 | Shape-gradient density G = rρu_τ∂_sψ₁ + endpoint terms; sliver identity rρu̇_ν = ∂_s(rρu_τδn) derived | PROVEN-HERE | §4.1 full chain (smooth segments; fronts/corners excluded) |
| 11 | Terminal-gauge swirl component zero; corner COUNT unchanged | PROVEN-IN-RECORD | carrier 5F.4; N6 §4 |
| 12 | Assembled lip/corner condition with swirl | OPEN | [S-5F] SCHEMA leg; pins in §4.2 |
| 13 | Adjoint pencil = primal pencil; backward march licensed by same m_n; M_tot prohibited | PROVEN-IN-RECORD (+trivial backward reading PROVEN-HERE) | 5F.2; D.3(c), D.4, D.5(iii) |
| 14 | Sonic-EXIT datum blow-up 1/(u²−c²) | PROVEN-HERE | §3.2/§5 R-4 |
| 15 | Centrifugal/inertia ratio 0.15-1.3 near spike tip; adjoint amplification exp(1-5); Lipschitz r_min⁻⁴ | SCALING-ESTIMATE | derivations §5 R-3 |
| 16 | Contact-crossing adjoint calculus & gradient noise at contact feet | OPEN | §5 R-5; record wall S.22 g2b |
| 17 | Frozen mixing — energy channel: five-field UNDERSTATES Isp (overstates debit); bias 0.5-2% Isp | Sign PROVEN-HERE, magnitude SCALING-ESTIMATE | §6(a-1) Gibbs derivation |
| 18 | Frozen mixing — radial-equilibrium channel: plug family reinforces (net direction unambiguous), bell family opposes (net OPEN) | SCALING-ESTIMATE + OPEN (bell net) | §6(a-2) |
| 19 | R_AM is blind to mixing; two-station A4 decay is the mixing meter | PROVEN-HERE (blindness) + PRACTICE (meter) | §6(a) |
| 20 | Ledger rows (b)-(e), (f)-(i) with violation channels and meters | HYPOTHESIS rows, meters as marked | §6 |
| 21 | Mean flux nullity survives in-nozzle pumping (∮∂_φp dφ = 0); only phase-resolved audits see it | PROVEN-HERE | §6(e) |
| 22 | In-nozzle Γ pumping fraction O(St_n × decay) | SCALING-ESTIMATE (spread declared) | §6(e) |
| 23 | Retiring instruments: E_θ worst-case bar → computed residual; recovery-asymmetry adjudication → in-gradient; D.14 licensing leg de-scoped for design | PROVEN-HERE (role level) | §7.1-3 |
| 24 | Remaining irreducible: J₁ bar, TWIN-C discipline, mode-purity pin, R_AM, mixing meter | PROVEN-IN-RECORD + PROVEN-HERE as marked | §7.4-8 |
| 25 | Recovery asymmetry reproduced in-gradient; sign favors outward turning, against plug | PROVEN-HERE (8.1 + duality) matching PROVEN-IN-RECORD T-T3-MAP(c) | §8.1 — VERIFIED, no flag |
| 26 | No new small-swirl nonconvexity; finite-swirl adds concave migration reward + r_min⁻⁴ anisotropy; family gap widens ~1-4% | PROVEN-HERE (derivatives) + SCALING-ESTIMATE (magnitudes); global landscape OPEN | §8.2 |
| 27 | T3QS smooth-cycle J₁ = 0 protection NOT licensed on swirl-carrying families | flag; see §10-F2 | T3QS §2 scope |

==============================================================================
## §10 Discrepancy / reconciliation flags (loud, none silent)

F1 (RECONCILIATION, not a contradiction). N6 §4's SCHEMA list expects
  "wall transversality with the centrifugal contribution". The
  derivation of §4.1 yields a gradient density with NO explicit
  centrifugal boundary term: G = rρu_τ∂_sψ₁, form-identical to
  meridional, with the centrifugal contribution routed ENTIRELY
  through the interior couplings (N2)/(N3) into ψ₁. If the eventual
  [S-5F] write-up expects an explicit Γ²/r³ wall term, this document
  says it does not exist in the exit-functional formulation (it
  would appear only in a wall-pressure-functional bookkeeping, where
  (X)/(W) swap inhomogeneity). To be reconciled at absorption, not
  silently merged.

F2 (SCOPE GAP FLAG). T3QS/T-T3QS proves the ray-cancellation
  (smooth-cycle J₁ = 0) with its physical reading anchored at
  SWIRL-FREE data ("D(W) at swirl-free data splits into exactly two
  mechanisms", T3QS §2). The five-field upgrade puts Γ-carrying data
  in scope; the P1-P5 homogeneity algebra plausibly extends (the
  θ-flux and Γ row are degree-1 homogeneous in conservative
  variables, and the ray scaling W → kW leaves w and Γ profiles
  fixed), BUT the H3-class invariance must then include the Γ
  profile and the carrier X-T3QS never exercised a swirl instance.
  Until an extended carrier passes, the smooth-cycle protection MUST
  NOT be cited for five-field families — the J₁ bar is computed,
  never argued away. (This is a gap in LICENSE, not a found error.)

F3 (WORDING GUARD). D.13 declares "the evaluator carries Γ as its
  transport row"; this document's primal row is the w-row (carrier
  convention), with the exact dictionary Γ-row = r × w-row and
  ψ_Γ = ψ₄/r (§0, §2.3). Any absorption must pick ONE convention and
  carry the dictionary — a silent mix flips r-powers in (N2)/(N3)
  and would be caught by the R1-class rejector (which is exactly why
  the rejector must ride along into the engine's oracle suite,
  §5 R-7).

==============================================================================
END. Machine check: swirl5f_adjoint_check.py — VERDICT PASS (C1-C5 +
R1 rejector). This file is the deliverable of record for the next
stage; nothing in it modifies any repo file.
