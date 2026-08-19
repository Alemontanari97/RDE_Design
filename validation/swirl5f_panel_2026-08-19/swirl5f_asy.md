# Asymptotic structure of the five-field per-phase reduction
# (nondimensional groups, residual ordering, removed-vs-retained errors,
#  ray-cancellation at five fields, and the definitive escape list)

Status: DERIVATION ARTIFACT (scratchpad, 2026-08-19). NOT a repo
document; written as input of record for the next stage of the
five-field (2.5-D swirl) upgrade adjudication. Author: subagent,
asymptotics brief. Every claim carries one label from
{PROVEN-HERE, PROVEN-IN-RECORD, SCALING-ESTIMATE, HYPOTHESIS, OPEN}.

SOURCES READ IN FULL (anchors used throughout):
- M0 `docs/rde_nozzle_MASTER.md` 440–560: [T-T0], [S-T0P], [T-NSW],
  N6 status block (N6-1/2/3, [S-5F]).
- `docs/rde_nozzle_T3QS.md`: D(W), [T-T3QS] P1–P6, §2 mechanism
  anatomy, §3 boundaries B1–B4.
- `docs/rde_nozzle_problem_book.md` §8 (St_n definition, two-scale
  structure), §9 (hypothesis ledger).
- `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
  (D.1–D.20, S.22; esp. D.2, D.6, D.10, D.13, D.17, D.18, D.19, D.20).
- `validation/sfoundations_raws_2026-08-13/phaseD/VERDICT_phaseD_proofs1.md`
  §3.2 (judge labels; D.18 iffs = THEOREM*/SCHEMA modulo G-f).
- `docs/rde_nozzle_N6_swirl.md` (N6-1/2/3, five-field adjoint §4).
- `docs/choice_ledger.yaml` C51 (azimuthal marching alternative).

MEASURED NUMBERS OF RECORD used as inputs (program frame): ε_θ =
u_θ/(Ωr) ≈ 0.15–0.20; tangential energy fraction f_θ ≈ 3–6%;
fluctuation ratio σ/μ ≈ 0.70; St_n ≈ 0.1–1 (problem book §8:
f = 3–30 kHz, τ_n = 20–150 μs). Working thermodynamic values for
magnitude evaluation (labeled SCALING-ESTIMATE where used): γ ≈ 1.2
(frozen detonation products), M_x ≈ 1.2–2.0 on the march (L4 class),
annulus slenderness α_gap = H/R_m ≈ 0.1–0.3 (geometry class,
HYPOTHESIS — instance-dependent).

INHERITANCE DECLARATION (honest): the residual object list K of §2
is D.18's six-row list, whose COMPLETENESS against the exact 3-D
system stands at SCHEMA (gap G-f) with the two D.18 iffs at
THEOREM*/SCHEMA per the judge (VERDICT §3.2, downgrades of record).
Everything in §2 therefore inherits the G-f conditional: if the G-f
independent re-derivation ever finds a seventh residual row, the
census here extends; nothing here narrows K below its record
definition. No claim below exceeds its record certification status.

==============================================================================
## §1 Nondimensionalization of the exact wave-frame system

### 1.1 The system

Exact reference object (D.17, PROVEN-IN-RECORD as DEFINITION): all
fields F(x, r, φ), φ = θ − Ωt, absolute velocity components
(u, v, w), solving unsteady 3-D Euler with ∂_t → −Ω ∂_φ. In
advective form, with the relative azimuthal velocity
w_rel := w − Ωr and the relative streamline derivative
D_rel := u ∂_x + v ∂_r + (w_rel/r) ∂_φ:

  (W1) mass      ∂_x(ρu) + (1/r) ∂_r(r ρ v) + (1/r) ∂_φ(ρ w_rel) = 0
  (W2) x-mom     ρ D_rel u + ∂_x p = 0
  (W3) r-mom     ρ D_rel v + ∂_r p = ρ w²/r
  (W4) Γ-row     ρ D_rel Γ + ∂_φ p = 0        (Γ := r w)
  (W5) entropy   D_rel s = 0

Consistency with the record: (W4) is D.19(i) (D_rel Γ = −(1/ρ)∂_φp,
machine-verified C1); the energy consequence D_rel h0 = −(Ω/ρ)∂_φ p
is D.19(ii) (C2); the rothalpy I = h0 − ΩΓ satisfies D_rel I = 0
(D.20, C3). Striking every ∂_φ term gives exactly the per-phase
2.5-D system (E1)–(E5) of D.1; the struck content is exactly the
six-row residual K of D.18. [PROVEN-IN-RECORD — D.1/D.17/D.18/D.19/
D.20 with their carriers.]

### 1.2 Scales and the master operator formula

Scales: axial length L (meridional march length), gap H, mean radius
R_m, cell angle Δφ_cell = 2π/n; velocities u ~ U = M_x c, v ~ U H/L
(meridional slenderness), w ~ u_θ = ε_θ Ω R_m; thermodynamic scales
ρ_ref, p_ref = ρ_ref c²/γ; per-field fluctuation amplitudes
a_q := σ_q/μ_q (a_p ≈ 0.70 of record; other fields carry their own
a_q — see G2). Nondimensional variables: x = L x̃, φ = (2π/n) φ̃,
u = U ũ, w = u_θ w̃, etc. Then, using τ_n ≈ L/U (the record's
convective residence time; problem book Def. 8.1, exact form
τ_n = ∫dx/u — equal at O(1)):

  (w_rel/r) ∂_φ = −Ω (1 − ε_θ w̃ (R_m/r)) ∂_φ
                = −(U/L)·St_n·(1 − ε_θ w̃ R_m/r) ∂_φ̃ ,

since Ω (n/2π) = St_n·U/L by St_n := nΩτ_n/2π. Hence the MASTER
FORMULA [PROVEN-HERE — the two displayed lines]:

  D_rel = (U/L) [ ũ ∂_x̃ + ṽ ∂_r̃  −  St_n (1 − ε_θ w̃ R_m/r) ∂_φ̃ ]
           \______________________/   \___________________________/
             retained (2.5-D)            struck by the reduction

The struck operator splits EXACTLY into
  SWEEP  −St_n ∂_φ̃              (the lab-frame ∂_t in disguise)
  DRIFT  +St_n ε_θ w̃ (R_m/r) ∂_φ̃  (self-swirl azimuthal advection)
which is the problem-book §8 split (D1 vs the residual D2 content),
now with the drift coefficient MEASURED: ε_θ = 0.15–0.20.

### 1.3 The group census

Every group: definition / derivation of magnitude on record numbers /
physics it controls. Primary groups are mutually independent;
derived groups are named because they are the coefficients that
actually appear in the ordered residual.

PRIMARY GROUPS
--------------
G1. St_n := n Ω τ_n / 2π  — per-wave Strouhal = swept fraction of
    one wave cell per nozzle transit.
    Magnitude: 0.1–1 [PROVEN-IN-RECORD, problem book §8 honest
    numbers]. Controls: the entire sweep residual (every K row);
    the transit-integrated smallness factor of the S.22 bound (g3:
    the swept angle per transit IS the small parameter, ∂_φV is
    O(1)); the width of the wave-passage window where fitting takes
    over (T3QS (i)).

G2. a_q := σ_q/μ_q — per-field fluctuation amplitude around the
    cycle (the azimuthal modulation depth of field q).
    Magnitude: a_p ≈ 0.70 of record (P-M); other fields carry their
    own a_q, unmeasured of record [HYPOTHESIS: a_ρ, a_u ~ a_p to
    within O(1); a_s, a_h0 possibly smaller on nearly-isothermal
    blowdown data — flagged as the K_h0 weighting caveat in §2].
    Controls: multiplies EVERY residual term (K ≡ 0 on axisymmetric
    data: K is fluctuation-driven); a² ≈ 0.5 is the second-moment /
    covariance weight (D.10: "FIRST-ORDER, not cosmetic").

G3. ε_θ := u_θ/(Ω r) — swirl-to-wheel ratio.
    Magnitude: 0.15–0.20 [MEASURED, program frame]. Controls: the
    drift/sweep ratio (master formula); every CROSS (sweep×swirl)
    term is O(ε_θ) relative to its sweep parent; enters M_rel =
    M_Ω(1 − ε_θ) and the torque weight β_τ.

G4. M_x := u/c — axial (meridional-normal: m_n form on curved Γ_d,
    D.4) Mach; margin m_n = M_n − 1 > 0 on the L4 class.
    Magnitude: 1.2–2.0 working [record class; instance-audited].
    Controls: spacelikeness/marchability (D.4), the finite domain
    of dependence, hence the Gronwall constant of the S.22 target.

G5. M_Ω := Ω r / c — WHEEL MACH NUMBER. ⚠ NOT NAMED AS A GROUP IN
    THE RECORD (the record speaks of D_CJ and w_rel ≈ −D_CJ,
    [T-NSW], but never nondimensionalizes the wheel speed).
    Magnitude [SCALING-ESTIMATE, derived from record concordance]:
    δ = ε_θ M_Ω / M_x (identity, see D1 below) with δ = 0.17–0.25
    measured via f_θ and ε_θ = 0.15–0.20 gives M_Ω/M_x ≈ 0.9–1.7,
    i.e. M_Ω ≈ 1.5–2.5 on the march; working value 2.0. (Physically
    Ωr ≈ D_CJ ≈ 2000–2500 m/s against product sound speeds
    1100–1300 m/s — consistent.) Controls: converts between the
    three swirl measures (M_θ = ε_θ M_Ω, δ = ε_θ M_Ω/M_x); sets the
    torque and work weights β_τ, β_w; sets M_rel.

G6. γ(T) — 1.15–1.25 for products [standard; the γ(T)-exact closure
    of record]. Controls: all thermodynamic conversion factors.

G7. α_gap := H/R_m — annular slenderness.
    Magnitude: 0.1–0.3 [HYPOTHESIS — geometry-class, instance
    value from the design]. Controls: the gap-integrated
    centrifugal pressure shift (γ M_θ² α_gap); curvature spread of
    the 1/y² weights in the N6-3 obstruction/OBS; the H-ANN bound.

G8. ε_g := H/L — meridional aspect (with the wall slope). Controls:
    v/u scale; standard axisymmetric-nozzle slenderness; retained
    by both 4F and 5F models — listed for completeness, plays no
    role in the 4F→5F delta.

(G9. N_ξ — number of phase samples; a DISCRETIZATION group, not a
    flow group. Controls the sampling-resolution escape E6 of §5.)

DERIVED GROUPS (the coefficients of the ordered residual)
---------------------------------------------------------
D1. δ := u_θ/u_x = ε_θ M_Ω / M_x — swirl-to-axial velocity ratio.
    [PROVEN-HERE, one line: u_θ/u = (u_θ/Ωr)(Ωr/c)(c/u).]
    Magnitude: measured independently through the tangential energy
    fraction f_θ = u_θ²/|u⃗|² ≈ δ² (v² small): f_θ = 3–6% ⟹
    δ = 0.17–0.25. CONCORDANCE CHECK [PROVEN-HERE]: the two record
    measurements (ε_θ = 0.15–0.20 and f_θ = 3–6%) are mutually
    consistent through M_Ω/M_x ≈ 0.9–1.7 — the record's numbers
    cohere; no tension. Controls: swirl loading of the meridional
    dynamics; exit swirl angle arctan δ ≈ 10–14°; the E_θ booking
    error class (O(δ²)).

D2. M_θ := u_θ/c = ε_θ M_Ω — swirl (centrifugal/acoustic) Mach.
    Magnitude: 0.23–0.50, working 0.35; M_θ² ≈ 0.05–0.25, working
    0.12. Controls: the radial-equilibrium pressure shift
    Δp_RE/p = γ M_θ² α_gap (§3 R1); the swirl-cooling state shift
    (γ−1)M_θ²/2 (§3 R3, D.5(ii)); the total-Mach hazard margin gap
    (D.5(iii)).

D3. M_rel := |w_rel|/c = M_Ω (1 − ε_θ) at the interface scale.
    Magnitude: 1.2–2.1. THE RECORD NAMES THE LOCUS, NOT THE GROUP
    ([T-NSW]: relative sonic locus = CJ surface). Controls:
    hyperbolicity of the φ-direction (the C51 azimuthal-marching
    condition |u_θ − Ωr| > c is M_rel > 1); the H-NC hypothesis
    (empty interior of {M_rel = 1}); distance to the lock-in
    kernel (escape E7).

D4. Λ := n L / (2π R_m) = St_n · M_x / M_Ω — HELIX PITCH of the
    swept pattern through the duct = azimuthal-to-axial pressure-
    gradient ratio: (∂_φ p / r)/(∂_x p) ~ a_p Λ / a_p = Λ per unit
    fluctuation. ⚠ NEW-NAMED (not in the record).
    [PROVEN-HERE: (1/r)∂_φ p ÷ ∂_x p ~ (p n/2π r)/(p/L) = nL/2πR_m;
    and nL/2πR_m = (nΩL/2πU)(U/Ωr) = St_n M_x/M_Ω.]
    Magnitude: 0.75·St_n working, i.e. 0.05–0.9. Controls: the
    inter-sector azimuthal push relative to the axial push (T3QS
    mechanism (b) at strength); the obliquity of inherited helical
    sheets, n_φ/n_x ~ Λ·(Δx_s/L) (escape E5).

D5. χ := Ω Γ / h0 = ε_θ M_Ω² (γ−1) (h/h0) — ROTHALPY-SPLIT GROUP.
    ⚠ NEW-NAMED (the record has the identity I = h0 − ΩΓ, D.20,
    but no dimensionless measure of the split).
    [PROVEN-HERE: ΩΓ/h0 = (Ωr)u_θ/h0 = ε_θ(Ωr)²/h0 and
    (Ωr)² = M_Ω² c² = M_Ω²(γ−1)h for the γ(T) closure at working
    γ.] Magnitude: with h/h0 ≈ 0.7–0.8 (M_x = 1.2–2 march):
    χ ≈ 0.06–0.20, working 0.10. Controls: the h0 misbooking per
    unit fractional Γ error — EXACT relation Δh0/h0 = χ·(ΔΓ/Γ)
    from Δh0 = Ω ΔΓ (D.19 pumping pair / D.20 split); the
    magnitude of escape E3.

D6. β_w := p/(ρ h0) = (γ−1)h/(γ h0) — work-term weight in K_h0.
    Magnitude: ≈ 0.10–0.13. [PROVEN-HERE: p/ρ = R_g T =
    (γ−1)h/γ at working γ.]

D7. β_τ := p/(ρ Ω r u_θ) = 1/(γ M_Ω² ε_θ) — torque-to-sweep weight
    in K_Γ. Magnitude: 1/(1.2·4·0.175) ≈ 1.2 (range 0.5–2.5).
    [PROVEN-HERE: p/(ρΩr u_θ) = (c²/γ)/(Ωr·u_θ) = 1/(γ M_Ω M_θ)
    = 1/(γ M_Ω² ε_θ).] Controls: whether in-duct torque or carried
    swirl dominates the Γ budget (β_τ ≈ 1: they are COMPARABLE at
    record numbers; β_τ → ∞ as ε_θ → 0: generation dominates on
    swirl-poor data — T3QS §2(b) recovered quantitatively).

FLAG-1 (discrepancy check, mild — refinement not contradiction).
Problem book §8 justifies D2 with "|u_θ| ≪ Ω_w r for detonation
products". The measured ε_θ = 0.15–0.20 makes the drift 15–20% of
the sweep — one order down, but NOT asymptotically negligible: at
a = 0.7, St_n = 1 the drift residual a ε_θ St_n ≈ 0.10–0.14 exceeds
any few-% design tolerance. The "≪" wording overstates the
suppression; the quantified statement is the entry O(a ε_θ St_n) in
§2. No other source conflict was found; the concordance check D1
POSITIVELY cross-validates the record's two independent swirl
measurements.

==============================================================================
## §2 Ordering the residual operator R(W) = K

The residual is D.18's six-row K (a.c. part + front atoms;
distributional reading of record). Ordering convention: each a.c.
row is normalized by the RETAINED meridional advection of the SAME
row (magnitude ρU·q/L for a row transporting q), evaluated at the
scales of §1.2. Under this convention the ratio for any ∂_φ term is
its coefficient times a_q St_n [PROVEN-HERE via the master formula:
Ω(n/2π) = St_n U/L converts every ∂_φ against every ∂_x].

### 2.1 Row-by-row derivation (a.c. part)

K_ρ = (1/r) ∂_φ(ρ w_rel) = −Ω ∂_φ ρ + (1/r) ∂_φ(ρ w)
  [identity: w_rel = w − Ωr, ∂_φ(Ωr) = 0 at fixed r]
  • sweep −Ω∂_φρ:  ratio = a_ρ St_n
  • drift (1/r)∂_φ(ρw): ~ a ρ u_θ n/(2π r) ÷ ρU/L = a ε_θ St_n
    [PROVEN-HERE: u_θ n L/(2π r U) = ε_θ (Ωr) nL/(2π r U) = ε_θ St_n]

K_u = ρ (w_rel/r) ∂_φ u = −ρΩ∂_φu + ρ(w/r)∂_φu
  • sweep: a_u St_n     • drift: a_u ε_θ St_n

K_v = ρ (w_rel/r) ∂_φ v : same structure —
  • sweep: a_v St_n     • drift: a_v ε_θ St_n
  (normalized against the retained r-row, which includes the
   retained centrifugal source ρw²/r — the source itself is NOT
   residual: D.18 r2 pin, "every curvature/metric term is RETAINED;
   ONLY ∂_φ terms are dropped").

K_Γ = ρ (w_rel/r) ∂_φ Γ + ∂_φ p
  • sweep of Γ: a_Γ St_n     • drift of Γ: a_Γ ε_θ St_n
  • TORQUE ∂_φ p, against the retained Γ advection ρUΓ/L:
      ∂_φ p ÷ (ρUΓ/L) ~ (a_p p n/2π)(L/ρU r u_θ)
      = a_p St_n · p/(ρ Ω r u_θ) = a_p St_n β_τ = a_p St_n/(γ M_Ω² ε_θ)
    [PROVEN-HERE, using n/2π = St_n U/(ΩL)]. At record numbers
    β_τ ≈ 1.2: torque ≈ sweep-of-Γ — the in-duct generation and the
    carried-swirl rearrangement are CO-LEADING in the Γ budget.
    Against the AXIAL momentum scale the same torque is
    (1/r)∂_φp ÷ ∂_x p = a_p Λ = a_p St_n M_x/M_Ω ≈ 0.5 a_p St_n —
    bounded; the apparent 1/ε_θ divergence of β_τ only says that on
    swirl-poor data the torque OWNS the Γ budget (swirl generation
    from swirl-free data, T3QS §2(b), now with its coefficient).

K_s = (w_rel/r) ∂_φ s :  a_s St_n (1 + O(ε_θ))

K_h0 = (w_rel/r) ∂_φ h0 + (Ω/ρ) ∂_φ p
  • sweep of h0: a_h0 St_n (1 + O(ε_θ))
  • WORK term (Ω/ρ)∂_φp against (U/L)h0:
      (Ω a_p p n/2πρ) ÷ (U h0/L) = a_p St_n · p/(ρ h0) = a_p St_n β_w
      ≈ (0.10–0.13) a_p St_n  [PROVEN-HERE].
    CAVEAT: if the data class has a_h0 ≪ a_p (nearly-uniform T0
    blowdown), the WORK term dominates K_h0 despite its small
    weight — the h0 residual is then pressure-fluctuation-driven,
    order 0.1 a_p St_n absolutely. [HYPOTHESIS on a_h0; the a_p
    number is the measured one.]

### 2.2 Order table (a.c. part, record numbers: a = 0.7,
###     ε_θ = 0.175, M_Ω = 2, M_x = 1.5, γ = 1.2, St_n = 0.1–1)

| Residual piece | Order (exact groups) | Numerical range |
|---|---|---|
| SWEEP of ρ, u, v, Γ, s, h0 (six rows) | a_q · St_n | 0.07 – 0.7 |
| DRIFT (sweep×swirl cross) in all rows | a_q · ε_θ · St_n | 0.012 – 0.12 |
| TORQUE ∂_φp in K_Γ (vs Γ budget) | a_p St_n / (γ M_Ω² ε_θ) | 0.08 – 0.83 |
| TORQUE ∂_φp in K_Γ (vs axial ∂_x p) | a_p · Λ = a_p St_n M_x/M_Ω | 0.05 – 0.53 |
| WORK (Ω/ρ)∂_φp in K_h0 (vs h0 advection) | a_p · St_n · β_w | 0.007 – 0.09 |

All entries [PROVEN-HERE as scale ratios / SCALING-ESTIMATE as
numbers]. K vanishes identically at a_q ≡ 0 (axisymmetric data):
every residual is fluctuation-driven — the honest ordering
parameter of the reduction is the PRODUCT a·St_n, refined by ε_θ
(cross terms) and by β_τ, β_w, Λ (thermo/geometry conversions).

### 2.3 Cross-term (sweep × swirl) census — exhaustive over the
###     record K list

An interaction term = a residual term whose existence requires BOTH
the sweep (Ω) and the swirl (w or Γ). Census over D.18's six rows
[PROVEN-HERE by inspection of the displayed rows; inherits G-f on
completeness of the row list itself]:
 (i)   the five DRIFT pieces (w/r)∂_φ(ρ, u, v, Γ, s) — O(a ε_θ St_n);
 (ii)  the SWEEP-of-Γ piece −Ω∂_φΓ — O(a_Γ St_n) on the Γ budget
       (exists only with carried swirl);
 (iii) the TORQUE/WORK PAIR (∂_φp in K_Γ; (Ω/ρ)∂_φp in K_h0) — ONE
       mechanism, not two: D_rel h0 = Ω·D_rel Γ (D.19; D.20 split of
       I = h0 − ΩΓ). Book once: the h0 pumping is the Γ pumping read
       through χ. Orders: a_p St_n β_τ (Γ budget) and a_p St_n β_w
       (h0 budget), consistency identity χ · (a_p St_n β_τ) =
       a_p St_n β_w [PROVEN-HERE: χ β_τ = ε_θM_Ω²(γ−1)(h/h0) ·
       1/(γM_Ω²ε_θ) = (γ−1)h/(γh0) = β_w — the group algebra closes].
No further products arise: the centrifugal ρw²/r and geometric
−ρvw/r couplings are RETAINED by the 2.5-D operator (D.18 r2 pin)
and are therefore NOT part of R(W).

### 2.4 The singular part (front atoms)

Per D.18 (distributional definition of record): on each wave-steady
front, K carries an atom of surface density n_φ·[F_φ,rel] per row —
the difference between the full 3-D RH and the meridional RH the
per-phase sections impose. Ordering:
 • The atom is NOT small in any group pointwise: jumps are O(1) at
   the wave and O([p]/p) on the inherited sheet; n_φ is set by the
   sheet obliquity, n_φ/n_x ~ Λ·(∂x_s/∂φ)/L on a helical sheet
   x = x_s(φ) [PROVEN-HERE: the normal of x = x_s(φ) is
   ∝ (1, 0, −x_s′/r)].
 • Its TRANSIT-INTEGRATED thrust content is the T3QS jump-localized
   residue ⟨ψ̂, Z⟩·[k]_jump: first order, concentrated in the
   wave-passage ξ-window of width ~St_n, and its absorption by the
   FITTED inherited sheet is the pre-registered O5 prediction P-ii —
   CONJECTURAL until measured (T3QS B3/B4). [PROVEN-IN-RECORD for
   the structure; the absorption claim stays at its record class.]

### 2.5 Reconciliation with S.22 (g3) — no discrepancy

S.22 (g3, r1-reformulated) insists ∂_φV is O(1) and K pointwise
LARGE, with the smallness ONLY in transit-integrated form. The §2.2
ratios are consistent: they are RATIOS OF SCALES, and the ratio of
the struck azimuthal advection to the retained meridional advection
IS the swept-cell-fraction per transit — numerically O(a·St_n),
which at St_n → 1, a = 0.7 is O(1), i.e. "pointwise large" in
exactly g3's sense. The formal smallness statement remains the
transit-integrated (Gronwall-in-x within the u > c domain of
dependence) form targeted by S.22; §2.2 is the coefficient table
that the transit integration multiplies by O(St_n). [PROVEN-HERE
reading; no conflict with the record.]

==============================================================================
## §3 Four-field vs five-field: what the upgrade removes, at what
##    order — and what it cannot touch

Setting: 4F = current design engine's per-phase meridional model,
fields (ρ, u, v, p), w ≡ 0 in the state (swirl absent from fluxes,
sources, and energy). 5F = D.1's 2.5-D system: Γ = r u_θ as a third
streamline invariant (D.2), centrifugal feedback ρw²/r in (E3),
u_θ²/2 inside h0.

### 3.1 The exact error decomposition

For identical interface data, and per D.18's unconditional operator
identity (exact-residual = 2.5D-residual + K, as distributions):

  Err(4F vs exact 3-D) = [4F − 5F]  +  [5F − exact 3-D] ,

where the second bracket is governed ENTIRELY by K (its bound is
S.22's target) and the FIRST bracket is what the upgrade removes.
[PROVEN-HERE as a decomposition; the K-governance of the second
bracket inherits D.18's THEOREM*/SCHEMA status per VERDICT §3.2.]

### 3.2 REMOVED errors (each derived with its order)

R1 — RADIAL-EQUILIBRIUM PRESSURE SHIFT: SOLVED, NOT INCONSISTENT.
The 4F r-momentum lacks ρw²/r. The true gap-integrated radial
pressure rise at fixed x is
  p(r_out) − p(r_in) ⊇ ∫ ρ u_θ²/r dr = ρ̄ ū_θ² ln(r_out/r_in),
so the 4F pressure field is biased by
  Δp_RE / p = γ M_θ² ln(r_out/r_in) ≈ γ M_θ² α_gap
            ≈ 1.2 × (0.05–0.25) × (0.1–0.3) ≈ 0.6–9 %  (working ~1.5–4 %).
[PROVEN-HERE derivation; SCALING-ESTIMATE magnitude.] Note the
CONSISTENCY reading: the interface data (chamber generator) contain
the chamber's swirl-supported radial equilibrium; a 4F march then
evolves p under a DIFFERENT radial momentum law — the interior is
inconsistent with its own BC at O(M_θ² α_gap) from the first step.
5F restores one law throughout. The shift is SINGLE-SIGNED (outward)
and PHASE-COHERENT: it survives every μ-average at full order, and
redistributes ρu across the gap (mass-flux distribution the contour
optimization sees) at the same order.

R2 — SWIRL-KE (E_θ) RESOLVED PER CONTOUR, BOOKED, NOT MISASSIGNED.
4F either drops u_θ²/2 from h0 (energy under-booked) or folds it
into meridional KE (axial exit velocity overestimated). With Γ(ψ)
transported (D.2) and h = h0(ψ) − W²/2 − Γ(ψ)²/(2r²) (D.2(iii)),
5F computes E_θ per contour and books it unrecoverable within the
vaneless axisymmetric class (D.10 + N6-2 scope note). The removed
axial-velocity/thrust bias:
  V_ax = √(2(h0 − h_exit) − u_θ,exit²)  ⟹  ΔV/V ≈ −δ_exit²/2
       ≈ −(1.5–3) %   [PROVEN-HERE one line; magnitudes = the
  measured f_θ/2 = 1.5–3 % of record]. POSITIVE-DEFINITE (E_θ > 0
  strictly on through-flow, D.10 THEOREM): no cancellation ever
  protects a 4F model from it.

R3 — STATE-RECOVERY AND MARGIN BIAS REMOVED.
Dropping u_θ²/2 from the static-enthalpy recovery biases T by
  ΔT/T = −u_θ²/(2 c_p T) = −(γ−1) M_θ²/2 ≈ −(0.5–2.5) %
[PROVEN-HERE: c_p T = c²/(γ−1)], hence c biased by half that and the
spacelikeness margin audit biased by ΔM_x/M_x ≈ +(γ−1)M_θ²/4
≈ 0.3–1.3 % (direction per D.5(ii): swirl cools, margin rises; the
4F audit UNDERSTATES the true margin — conservative, but wrong, and
against a thin margin m_n ~ 0.2 the relative mis-statement reaches
several % of the margin itself). 5F computes the exact γ(T) state
(D.13 recovery THEOREM: unique T for ALL Mach under AUD-cp +
AUD-c2T, existence under AUD-hRANGE). [PROVEN-HERE + PROVEN-IN-
RECORD for the D.5(ii)/D.13 legs.]

R4 — THE N6-3 STRUCTURAL OBSTRUCTION REMOVED (license, not just
magnitude). The 4F design machinery consumes the pointwise closure
p = p(W, y), which FAILS beyond free-vortex swirl by the exact
obstruction identity dh/dW|_y = −W + (h0′ − ΓΓ′/y²)dψ/dW (N6-3,
machine-verified): on generic (non-uniform-triple) data the 4F/Rao
route is structurally unlicensed — the OBS monitor exists precisely
to block it (D.14). The 5F field-level route ([S-5F]/reverse-AD)
needs NO pointwise closure: the entire licensing question (G-b1
sensitivity gap included) is BYPASSED, not merely satisfied.
[PROVEN-IN-RECORD: N6-3 THEOREM + D.14/D.15.]

R5 — EXIT SWIRL PROFILE COMPUTED. Γ(ψ)/r_exit gives the exit swirl
angle arctan δ_exit ≈ 10–14° and its profile — an O(δ) kinematic
output simply absent at 4F (needed for momentum bookkeeping,
downstream integration, any thrust-vector accounting). [PROVEN-
HERE trivially from D.2.]

SUMMARY OF REMOVED ORDERS: R1 = O(γ M_θ² α_gap) coherent in p;
R2 = O(δ²) coherent in thrust/Isp (measured 3–6 % of KE flux);
R3 = O((γ−1)M_θ²/2) in T; R4 = structural license; R5 = O(δ)
kinematic output. All are STEADY, SINGLE-SIGNED, PHASE-COHERENT
biases — present at every phase, surviving every average, protected
by NO cancellation mechanism.

### 3.3 UNCHANGED errors (everything in R(W) = K)

The 5F per-phase model still strikes every ∂_φ term: ALL of §2
survives the upgrade verbatim — sweep O(a St_n), drift
O(a ε_θ St_n), torque/work pair (in-duct swirl generation and h0
pumping), front atoms, and the rothalpy split (5F transports h0 and
Γ as TWO invariants where the exact flow transports only
I = h0 − ΩΓ; the split error IS the torque/work pair already
counted — D.20). Honest reading: 5F does not SHRINK K by one term;
what it does at the K level is make the swirl rows MEANINGFUL and
MONITORABLE (K_Γ, K_h0 pump fields the 4F model does not even
carry; D.14/D.16 audit them), and make the comparison target S.22
well-posed for the actual field content. Also unchanged: interface-
data fidelity, mode purity (H-A1/T0-flatness), μ-measure knowledge,
the EOS pin, and every §5 escape. [PROVEN-HERE by the §3.1
decomposition.]

### 3.4 The protection asymmetry — the quantified value of the
###     upgrade

 (i) The UNCHANGED error class (sweep) is MEAN-PROTECTED at first
     order on ray cycles: J_1 = 0 exactly on smooth periodic ray
     cycles, jump-localized residue on the sawtooth ([T-T3QS] P6)
     — and §4 below PROVES this protection survives at five fields.
 (ii) The REMOVED error classes R1–R3 are positive-definite /
     single-signed coherent biases with NO protecting mechanism:
     they hit the cycle objective at FULL order δ² ≈ 3–6 %
     (thrust-level 1.5–3 % from R2 alone, plus the O(1–4 %)
     pressure-distribution bias R1).
CONSEQUENCE [PROVEN-HERE assembly on record components]: at record
numbers the 4F model's LARGEST UNPROTECTED error is exactly the
class the 5F upgrade removes; after the upgrade the per-phase chain
is "sweep-limited" — its leading residual is the O(a St_n) class
that (a) first-order-cancels in the mean on-ray, (b) concentrates
at the wave-passage jump, (c) is priced by the corrector/S.22
program. This is the precise sense in which the upgrade buys a
rung: it removes 1.5–6 %-class coherent design biases at the cost
of one field, one transport row, and one adjoint row (N6 §4
counting), while leaving the (differently-protected) sweep physics
exactly where the record says it lives.

==============================================================================
## §4 The corrector at five fields: ray-cancellation with Γ in the
##    family

QUESTION: does [T-T3QS] survive when the per-phase family is the
five-field system (Γ transported, centrifugal source, u_θ²/2 in
h0)? ANSWER: YES — PROVEN-HERE below, at the same algebraic grade
as the record theorem, with ONE new hypothesis surfaced (H3-w).

### 4.1 Statement

THEOREM (5F ray protection; algebraic core; EOS-general: thermally
perfect p = ρR_gT with ARBITRARY caloric e(T) — same generality as
[T-T3QS]). On a T3 ray family of five-field per-phase states —
phases differing only by the scale k(ξ) = Pc(ξ)/Pc_ref at fixed
(u, v, w, T) fields, i.e. H3 EXTENDED by
  (H3-w) the interface swirl profile w(y) (equivalently ε_θ(y)) is
  PHASE-INVARIANT in shape,
properties (P1)–(P6) of [T-T3QS] hold verbatim for the five-field
system, and the first-order sweep correction J_1 vanishes exactly
on smooth periodic ray cycles and concentrates at the wave-passage
jump on the blowdown sawtooth.

### 4.2 Proof

P1 (ray linear in conservative variables). U := (ρ, ρu, ρv, ρΓ,
ρE), E = e(T) + (u²+v²+w²)/2. At fixed (u, v, w, T), ρ → kρ maps
U → kU exactly — the swirl components scale with the same k because
Γ = rw is held fixed and only the density factor scales. ∎

P2 (degree-1 homogeneity of ALL five-field fluxes, sources, RH).
Velocities are degree-0 functions of U (ratios: u = U₂/U₁,
w = U₄/(rU₁)); e = U₅/U₁ − |u⃗|²/2 is degree-0; hence T = T(e) is
degree-0 and p = U₁R_gT(e) is degree-1 — for ARBITRARY caloric
e(T). Every flux entry is (density factor)×(degree-0) or p:
  F_x = (ρu, ρu²+p, ρuv, ρuΓ, u(ρE+p)),
  F_r = (ρv, ρuv, ρv²+p, ρvΓ, v(ρE+p)) — all degree-1.
Sources: conservation-form r-row source p + ρw² = p + U₄²/(r²U₁):
degree-1; advective centrifugal ρw²/r and geometric −ρvw/r:
degree-1. The RELATIVE azimuthal flux (the sweep operator's
content, D.18 conventions):
  F_φ,rel = (ρw_rel, ρu w_rel, ρv w_rel, ρw w_rel + p,
             w_rel(ρE+p) + Ωr p)
— every entry degree-1 (ρw_rel = U₄/r − ΩrU₁ is even LINEAR).
RH relations are differences of degree-1 fluxes (the θ-row jump
[ρu_n w] = 0 included): degree-1, so the zero-set — the fitted-
sheet position — is k-invariant. MACHINE CHECK: all entries of
F_x, F_r, F_φ,rel, and all three sources verified degree-1 with
abstract T(e) (scratchpad script `swirl5f_ray_check.py`, this
window: FAILS: NONE). ∎

P3 (one linearized operator along the ray). Euler's theorem:
F(kU) = kF(U) differentiated in U gives DF(kU) = DF(U) — all flux
Jacobians AND source Jacobians (sources degree-1 by P2) are
invariant along the ray: the per-phase linearized five-field
operator — including the centrifugal/geometric couplings that
populate the zeroth-order matrix M of the five-field adjoint
structure (N6 §4(a), machine-derived of record) — is ONE operator.
MACHINE CHECK: every Jacobian entry of all three flux families
verified invariant under U → kU (same script: PASS). ∎

P4 (one adjoint field). The thrust objective integrand ρu² + p −
Pa n_x is degree-1-homogeneous minus a constant; its W-gradient is
degree-0 = ray-invariant. Swirl adds NO content to the thrust
trace (the axial momentum flux has no w-term; N6-1 kernel laws /
N6-2 scope note: swirl KE is not axial thrust flux). With the
T3-class BC structure — H3 + (H3-w): geometry and ALL profile
shapes (M, θ, w) phase-invariant — the adjoint problem has
phase-independent operator (P3), source (this step), and BC
structure; uniqueness of the linear adjoint solve (S1 apparatus +
the five-field Lagrange identity certified in N6 §4(c)) forces ONE
fixed field ψ̂. [The uniqueness leg inherits exactly the T3QS/S1
function-space conditional — nothing new assumed.] ∎

P5 (sweep factorization). The five-field azimuthal coupling
operator is D(W) = (1/r)∂_φ[F_φ,rel(W)]. On the ray family
W_A(·;ξ) = k(φ(ξ))·Ŵ with Ŵ phase-independent (H3 + H3-w) and
φ(ξ) affine (D.9(ii)):
  D(W_A) = (1/r) ∂_φ[F_φ,rel(k(φ)Ŵ)] = (1/r) ∂_φ[k(φ) F_φ,rel(Ŵ)]
         = k′(ξ) · Z ,   Z := (1/r) F_φ,rel(Ŵ) a FIXED field,
using P2's homogeneity for the second equality. MACHINE CHECK: the
factorization verified symbolically entry-by-entry (same script:
PASS). ∎

P6 (jump localization). J_1 = −∫⟨ψ_J(ξ), D(W_A(·;ξ))⟩dξ
= −⟨ψ̂, Z⟩ ∫k′(ξ)dξ by P4 + P5:
  = 0 EXACTLY on smooth periodic cycles (∮k′ = 0);
  = ⟨ψ̂, Z⟩·[k]_jump on the blowdown sawtooth — the ENTIRE
    first-order sweep correction concentrates at the wave-passage
    jump, exactly as at four fields. QED.

### 4.3 Rejector branches (each fires)

R1′ non-ray direction (T scaled along with ρ): p picks up k², P2
breaks. MACHINE CHECK: fires (script: rejector_fired = True).
R2′ H3-w violation (phase-dependent swirl shape ŵ(y;ξ)): Ŵ becomes
ξ-dependent, P5 breaks — D(W_A) ≠ k′Z. [PROVEN-HERE by inspection
of the P5 step; the record's R2 (theta-dependent Ŵ) generalizes.]
R3′ non-affine objective: breaks P4 (inherited verbatim).

### 4.4 Verdict, new boundary, and carrier duty

VERDICT: the ray-cancellation theorem SURVIVES with Γ in the
family — J_1 remains jump-localized on ray cycles at five fields.
Label: PROVEN-HERE (finite algebraic identities, pen algebra above
+ scratchpad symbolic check `swirl5f_ray_check.py`, all PASS with
the non-ray rejector firing). The scratchpad script is NOT a
committed carrier: per house discipline (R5) the identities need a
committed carrier with rejectors before any repo document cites
this at THEOREM; the carrier duty is hereby NAMED (an extension of
X-T3QS's battery by the five-field rows — natural F2-window item).

NEW HONEST BOUNDARY (beyond the record's B1–B3): with swirl the
per-phase data loop lives in a HIGHER-dimensional space
(Pc, T0-profile, w-profile). Real cycles violating H3-w leave the
ray, and the off-ray first-order residue is the AREA term of the
enlarged data loop: the swirl-profile cycle variation a_w opens an
O(a_w · St_n) hysteresis channel that the four-field bookkeeping
never had to price. Since the record's own expectation is that real
data generically FAIL profile uniformity (D.14 expectation clause),
H3-w should be expected to fail at some a_w > 0 on real data:
[HYPOTHESIS — a_w unmeasured; the channel's order is
SCALING-ESTIMATE O(a_w St_n) by the same area-term mechanism as
T3QS B1]. The wave-passage jump content now also includes the Γ and
E_θ jump fluxes in [k]_jump — same structure, more rows.

==============================================================================
## §5 The definitive "what still escapes" list

Every physical effect NOT captured by the five-field per-phase
model EVEN WITH PERFECT INTERFACE DATA, each with controlling
group(s) and magnitude on record numbers. (E1–E3 are the a.c. K
content; E4–E5 the singular content; E6 discretization; E7–E11
structural/scope.)

E1. IN-DUCT SWIRL GENERATION (inter-sector azimuthal pressure
    coupling; K_Γ's ∂_φp). Hot sectors push on cold sectors INSIDE
    the duct; the per-phase slice is a closed universe and cannot
    receive torque. Per-transit magnitude [SCALING-ESTIMATE,
    derived §2.1]:
      Δε_θ ≈ a_p St_n/(γ M_Ω²) ≈ 0.15 a_p St_n ≈ 0.01–0.10
      (wheel-fraction; comparable to the CARRIED ε_θ = 0.15–0.20
      at St_n → 1);  ΔΓ/Γ ≈ a_p St_n β_τ ≈ 0.08–0.83.
    Groups: a_p·St_n, β_τ = 1/(γM_Ω²ε_θ). The generated swirl is
    generically NON-free-vortex (T3QS §2(b)) — it feeds the N6-3
    obstruction downstream of wherever it is generated.

E2. INTERIOR PHASE LAG (sweep transport of ρ, u, v, s). Each parcel
    samples a phase interval Δξ ≈ St_n, not one phase; the interior
    lags the inlet phase by the local transit time. Pointwise state
    error O(a St_n) = 7–70 % of the fluctuation scale; MEAN-thrust
    effect protected: O(St_n²) on smooth ray cycles, first-order
    jump-localized residue on the sawtooth (§4 = the protection at
    five fields), area-term hysteresis off-ray (incl. the new
    H3-w/a_w channel, §4.4). Groups: a·St_n; off-ray loop area.
    [PROVEN-IN-RECORD structure + §4 PROVEN-HERE extension.]

E3. h0 PUMPING / ROTHALPY SPLIT (K_h0's work term; D.19(ii)+D.20).
    The wave does unsteady work on parcels at rate Ω per unit
    Γ-pumping-rate; the 5F model transports h0 and Γ as separate
    invariants where the truth transports only I = h0 − ΩΓ.
    Per-transit magnitude [SCALING-ESTIMATE]:
      Δh0/h0 = χ·(ΔΓ/Γ) = a_p St_n β_w ≈ 0.007–0.09  (0.7–9 %).
    Groups: χ ≈ 0.10 (rothalpy-split group, new-named), a_p St_n,
    β_w. Diagnostic gift (record): on contact-free uniform-I
    bundles Δh0 = Ω ΔΓ is a free audit row (D.20(a)).

E4. FRONT PUMPING WITHIN THE SWEEP (entropy/state jumps at wave
    passage; the K front atoms). Parcels whose transit STRADDLES
    the wave passage see genuinely different physics, not a delayed
    copy: s is pumped at fronts only (D.19(iii)), production m[s]
    lives in the atoms. O(1) jumps on a ξ-window of width ~St_n;
    the fitted inherited sheet represents the steady shadow of this
    physics, and its absorption of the first-order jump residue is
    the pre-registered, still-CONJECTURAL P-ii (T3QS B3/B4). The
    SUB-WINDOW relaxation structure escapes at any N_ξ. Groups:
    St_n (window), jump amplitudes [p]/p, [s].

E5. HELICAL GEOMETRY OF INTERIOR SHEETS (D.18 example (β)). The
    per-phase family computes a per-phase standoff x_s(ξ) with
    MERIDIONAL RH; the true object is the helical surface
    x = x_s(φ) with n_φ ≠ 0, whose 3-D RH differs from the imposed
    meridional RH by the n_φ[F_φ,rel] atom — invisible to the
    sections AT ANY SAMPLING RESOLUTION (it is a normal-direction
    error, not a resolution error). Obliquity scale: n_φ/n_x ~
    Λ·(Δx_s/L). Magnitude: needs the standoff modulation Δx_s per
    dataset — OPEN (measurable); the standing adjacent estimate is
    the acoustic-lag ratio 0.1–1 for subcritical phases (T3QS B2).
    Groups: Λ, Δx_s/L; St_n through Λ.

E6. SUB-PHASE SAMPLING RESOLUTION (second-moment structure vs N_ξ).
    The per-phase family at N_ξ samples IS a discretization of φ;
    smooth-cell content converges, but the sawtooth jump degrades
    unsplit μ-quadrature to first order O(a/N_ξ); split/fitted-
    window quadrature restores high order EXCEPT within the
    wave-passage window, where the physics itself is E4. The
    second-moment content carries weight a² ≈ 0.5 (D.10:
    first-order, not cosmetic) — so quadrature sloppiness here is a
    first-order error channel, not a refinement detail. Groups: a²,
    N_ξ, St_n. [PROVEN-HERE (standard quadrature theory) +
    PROVEN-IN-RECORD for the a² weight.]

E7. AZIMUTHAL ACOUSTICS STATIONARY IN THE WAVE FRAME (the H-NC
    kernel). At |w_rel| = c (the CJ locus, [T-NSW](a)) the K = 0
    constraint has a genuine one-parameter kernel — azimuthal
    acoustic disturbances steady in the wave frame (∂_φρ free,
    ∂_φw, ∂_φp slaved; D.18 proof text): the lock-in/resonance
    boundary. The per-phase model cannot represent them (they live
    entirely in the struck operator). Controls mode stability /
    lock-in, not the design state. Group: M_rel − 1 (distance to
    the CJ locus); magnitude: structural (a kernel, not a size).
    [PROVEN-IN-RECORD.]

E8. CONTACT/SLIP-SHEET 3-D STRUCTURE. Per-phase slices carry slip
    CURVES (C-fronts; [w], [Γ], [h0] free across them, D.2); the
    true objects are helical vortex SHEETS whose stability is only
    weakly/neutrally stable with instability windows
    (Coulombel–Secchi), and whose roll-up/mixing has no per-phase
    representation. Worse, the comparison bound itself is
    KNOWN-BROKEN there (S.22 g2b: convex-integration non-uniqueness
    kills the relative-entropy route on contact data): this escape
    is currently not only unresolved but UNPRICEABLE on the named
    route — the T-RED owner must fit the contacts or declare a
    slip-line-free sub-scope. Group: none small — structural.
    [PROVEN-IN-RECORD.]

E9. MODE IMPURITY / NON-Z_n OPERATION (unequal waves, counter-
    rotation, modulation, mode transitions). Outside T0/H-A1
    entirely; the per-phase machinery is a wave-frame quotient and
    has no channel for it. Monitored (T0-flatness; [T-SLRW]
    side-load channel as a mode-impurity detector; ¬H-AM1 aperiodic
    storage exit). Group: outside the census — hypothesis-class
    boundary, not an ordered term. [PROVEN-IN-RECORD.]

E10. SWIRL-KE RECOVERY BEYOND THE VANELESS CLASS. E_θ is booked
    unrecoverable BY DESIGN-CLASS SCOPE (D.10 r1 scope repair;
    N6-2 note): any vaned/diffusing recovery hardware lies outside
    the class — a scope boundary the five-field model inherits, not
    an error inside it. Group: f_θ = 3–6 % (the ceiling of what
    such hardware could ever chase). [PROVEN-IN-RECORD scope.]

E11. NON-MODEL CHANNELS: viscous/turbulent wall+plane torque
    moments, parasitic deflagration/afterburning (H-R1), discrete-
    orifice torque (D.8 channel (1)), injection swirl (J_inj).
    Declared-budget rows (H-AM2/H-AM4, D.16 audit), never resolved
    physics. The D.6 accounting pins what the CYCLE MEAN of the
    duct's angular-momentum flux can be (= declared inputs only);
    nothing in the per-phase model computes these inputs. Group:
    per-dataset declared budgets. [PROVEN-IN-RECORD, THEOREM* with
    (c1)/(c2) conditionals.]

==============================================================================
## §6 Claim register

| # | Claim | Label | Where |
|---|---|---|---|
| 1 | Master operator formula: struck operator = −St_n(1−ε_θw̃R_m/r)∂_φ̃ against a retained O(1) meridional operator | PROVEN-HERE | §1.2 |
| 2 | Group census: primary {St_n, a_q, ε_θ, M_x, M_Ω, γ, α_gap, ε_g}; derived {δ, M_θ, M_rel, Λ, χ, β_w, β_τ} with magnitudes | PROVEN-HERE (definitions/identities) + SCALING-ESTIMATE (magnitudes) + HYPOTHESIS (a_h0, α_gap instance values) | §1.3 |
| 3 | New-named groups: M_Ω (wheel Mach), Λ (helix pitch / azimuthal-to-axial gradient ratio), χ (rothalpy-split), β_τ, β_w | PROVEN-HERE | §1.3 |
| 4 | Concordance: ε_θ = 0.15–0.20 and f_θ = 3–6 % mutually consistent through M_Ω/M_x ≈ 0.9–1.7 | PROVEN-HERE | §1.3 D1 |
| 5 | FLAG-1: problem book §8 "\|u_θ\| ≪ Ωr" overstates drift suppression (measured ratio 0.15–0.20; drift residual up to 0.10–0.14) | PROVEN-HERE (flag) | §1.3 |
| 6 | Residual ordering: sweep O(a St_n); drift cross-terms O(a ε_θ St_n); K_Γ torque O(a_p St_n β_τ) on the Γ budget = O(a_p Λ) on the axial budget; K_h0 work O(a_p St_n β_w) | PROVEN-HERE (scale ratios; inherits G-f on K-list completeness) | §2.1–2.2 |
| 7 | Cross-term census exhaustive over the record K list; torque/work = ONE mechanism (χ·β_τ = β_w closes) | PROVEN-HERE (modulo G-f) | §2.3 |
| 8 | Front atoms pointwise O(1), transit-integrated = T3QS jump residue; fitted-sheet absorption = P-ii CONJECTURE | PROVEN-IN-RECORD | §2.4 |
| 9 | §2 ordering consistent with S.22 g3 (pointwise-large, transit-integrated smallness) | PROVEN-HERE (reading) | §2.5 |
| 10 | Error decomposition Err(4F) = [4F−5F] + [5F−3D], second bracket = K | PROVEN-HERE (inherits D.18 record status) | §3.1 |
| 11 | R1 removed: radial-equilibrium shift, Δp_RE/p = γM_θ²α_gap ≈ 0.6–9 %, single-signed, BC-interior inconsistency at 4F | PROVEN-HERE + SCALING-ESTIMATE | §3.2 |
| 12 | R2 removed: E_θ booking, thrust bias δ²/2 ≈ 1.5–3 %, positive-definite (D.10) | PROVEN-HERE + PROVEN-IN-RECORD (D.10) | §3.2 |
| 13 | R3 removed: state/margin bias (γ−1)M_θ²/2 in T, D.5(ii) direction | PROVEN-HERE + PROVEN-IN-RECORD | §3.2 |
| 14 | R4 removed: N6-3 pointwise-closure obstruction bypassed (license) | PROVEN-IN-RECORD | §3.2 |
| 15 | Unchanged: ALL of K, verbatim; 5F makes K_Γ/K_h0 nameable, does not shrink K | PROVEN-HERE | §3.3 |
| 16 | Protection asymmetry: removed errors coherent+unprotected, retained errors mean-protected/jump-localized ⟹ 5F removes the largest unprotected bias class; post-upgrade chain is sweep-limited | PROVEN-HERE (assembly) | §3.4 |
| 17 | Five-field ray-cancellation: P1–P6 hold with Γ in the family under H3+(H3-w); J_1 jump-localized at five fields; machine-checked (scratchpad), non-ray rejector fires | PROVEN-HERE (algebraic core; committed-carrier duty NAMED for any repo citation; adjoint-uniqueness leg inherits the S1 conditional) | §4 |
| 18 | H3-w is a NEW hypothesis; its violation opens an O(a_w St_n) off-ray hysteresis channel | HYPOTHESIS (a_w unmeasured) + SCALING-ESTIMATE (order) | §4.4 |
| 19 | Escape list E1–E11 with groups and magnitudes (E1: Δε_θ ≈ 0.15 a_p St_n; E3: Δh0/h0 ≈ 0.7–9 %; E5 magnitude OPEN pending Δx_s data) | as marked per item (E5 magnitude OPEN) | §5 |
| 20 | Everything above inherits the G-f conditional on K-list completeness and the VERDICT §3.2 judge labels for D.18 | PROVEN-IN-RECORD (inheritance declared) | §0 |

ARTIFACTS OF THIS DERIVATION (scratchpad only, no repo file touched):
- this file: `swirl5f_asy.md`
- symbolic check: `swirl5f_ray_check.py` (sympy 1.14.0, pinned env,
  no installs; output: "FAILS: NONE — all homogeneity/Jacobian/P5
  checks PASS; Non-ray rejector fired: True")
