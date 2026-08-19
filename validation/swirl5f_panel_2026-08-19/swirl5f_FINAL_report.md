# FINAL FUSED REPORT — five-field (2.5-D swirl) per-phase upgrade panel
# Presiding judge, 2026-08-19. Scratchpad artifact of record for the next
# stage; NO repo file modified.

INPUTS FUSED (all read in full): derivations `swirl5f_pde.md` (882 ln),
`swirl5f_asy.md` (778), `swirl5f_var.md` (903), `swirl5f_fun.md` (735);
refutations `swirl5f_refute_pde.md`, `swirl5f_refute_asy.md`,
`swirl5f_refute_var.md`, `swirl5f_refute_fun.md`. Record sources re-read by
this judge at the cited anchors: M0 440-560, T3QS full, PB §8-§9, phaseD
D.1/D.2/D.6/D.10/D.13/D.17/D.18/D.19/D.20/S.22, VERDICT_phaseD_proofs1 §3.2,
r2pass/VERDICT_r2pass.md 235-262 (J-r2p-2/3 verified at source THIS window),
N6 doc full, choice_ledger C51.

LABEL DISCIPLINE: every claim carries one of {PROVEN-HERE (= proven inside
this panel: deriver + independent refuter re-derivation, judge-checked),
PROVEN-IN-RECORD (anchor), SCALING-ESTIMATE (derivation named),
HYPOTHESIS, OPEN}. "JV" marks steps this judge re-executed personally.

HEADLINE VERDICTS (details in the numbered sections):
- Residual census: the six-row K list is COMPLETE at the advective level
  within the pinned gas model — three independent derivations (pde deriver
  from the lab equations; pde refuter from scratch; asy refuter by machine
  with an independent symbol set) found NO seventh row. Completeness against
  an independent div-form symbol set remains the record's G-f gap (SCHEMA).
- The upgrade's value claim, repaired: 5F removes the largest QUANTIFIED
  unprotected coherent bias class (1.5-6%-class, single-signed, surviving
  every average); the retained sweep class is mean-protected on-ray at
  first order — protection now PROVEN at five fields under one new
  hypothesis (H3-w) — but its unprotected remainder is unquantified of
  record and nominally comparable at St_n -> 1: the net-value claim is
  St_n-CONDITIONAL pending P-ii / S.22.
- The five-field adjoint/optimality system is BUILDABLE: the response +
  gradient core is derivation-complete at pen+machine grade (two
  independent hand transposes + two machine checks with firing rejectors);
  OPEN legs are the lip/corner assembly, the contact-crossing calculus,
  and the semiglobal function-space import ([C-D25U]) — each named with a
  workaround. The anti-spike asymmetry emerges in-gradient STRUCTURALLY;
  the printed "verified, no flag" was an overclaim, repaired to
  consistency-check grade.
- Cycle-mean thrust = mu-integral of per-phase thrusts: an EXACT identity
  half (theorem-grade, four-step proof, candidate mint) + ONE substitution
  (for the five-field model) whose error is exactly the adjoint-paired
  K-integral; "the error could be large" CANNOT be refuted by theory today
  — theory pins the mechanism and the protections, O5-lite pins the number.

==============================================================================
## §1 RESIDUAL-TERM INVENTORY (the definitive table)

Setting: Err(4F engine vs exact 3-D) = [4F - 5F] + [5F - exact 3-D], an
exact decomposition (PROVEN-HERE, asy §3.1; rests only on D.18's
DEFINITIONAL operator identity exact-residual = 2.5D-residual + K, which
all four lenses re-derived independently — never on the D.18 iffs, which
are SCHEMA of record per J-r2p-2/3). The second bracket is governed by
R(W) = K (six rows, a.c. + front atoms); the first bracket is what the
upgrade removes.

Groups (asy §1.3, refuter-confirmed): St_n = nΩτ_n/2π ~ 0.1-1;
a_q = σ_q/μ_q (a_p ≈ 0.70 measured; a_Γ, a_h0 HYPOTHESIS ~ a_p);
ε_θ = u_θ/(Ωr) ≈ 0.15-0.20; M_x ≈ 1.2-2.0; M_Ω = Ωr/c ≈ 1.5-2.5
(new-named; concordance-derived); γ ≈ 1.2; α_gap = H/R_m ≈ 0.1-0.3;
derived: δ = ε_θM_Ω/M_x ≈ 0.17-0.25; M_θ = ε_θM_Ω ≈ 0.23-0.50;
M_rel = M_Ω(1∓ε_θ) ([H-sgn]); Λ = St_n M_x/M_Ω ≈ (0.59-1.11)·St_n;
χ = ΩΓ/h0 ≈ 0.06-0.20 (judge-adjudicated value, §5 C1);
β_w = p/(ρh0) ≈ 0.10-0.13; β_τ = 1/(γM_Ω²ε_θ) ≈ 0.5-2.5 (working 1.2);
closure χ·β_τ = β_w EXACT (machine-checked).

### PART A — the residual R(W) = K (UNCHANGED by the upgrade)

| # | Term | Physics | Order (groups) | Magnitude (record numbers) | Priced today by | Captured by 5F? |
|---|---|---|---|---|---|---|
| A1 | K_ρ sweep −Ω∂_φρ | lab-frame ∂_t of mass in disguise: each slice fed the frozen inlet phase, reality feeds the phase lagged by transit time | a_ρ·St_n | 0.07-0.7 of the fluctuation scale per transit | J₁ corrector bar (VI.4bis(ii)); T3QS ray protection (5F extension PROVEN-HERE under H3-w, committed carrier still owed); S.22 bound = SCHEMA | NO |
| A2 | K_ρ drift (1/r)∂_φ(ρw) | self-swirl azimuthal advection of mass (lab drift) | a_ρ·ε_θ·St_n | 0.012-0.12 | same as A1 | NO (5F names it; still dropped) |
| A3 | K_u, K_v sweep+drift ρ(w_rel/r)∂_φ(u,v) | phase-lag transport of meridional momentum; late-arriving streamline curvature | a·St_n·(1+O(ε_θ)) | 0.07-0.7 | J₁ bar; on-ray mean-protection (first-order cancellation) | NO |
| A4 | K_Γ sweep ρ(w_rel/r)∂_φΓ | azimuthal drift of the swirl stratification across phases | a_Γ·St_n on the Γ budget (needs a_Γ ~ a_p, surfaced) | 0.07-0.7 if a_Γ~a_p | D.14 TRIPLE spread monitor; phase-resolved two-station Γ(ψ) audit (var §6(e) — NOT yet armed, G-e vacuum) | NO — and only NAMEABLE at 5F (4F carries no Γ at all) |
| A5 | K_Γ torque ∂_φp | INTER-SECTOR PRESSURE TORQUE = in-duct swirl generation; generated swirl generically non-free-vortex (N6-3 entry point) | a_p·St_n·β_τ (Γ budget); a_p·Λ (axial budget) | ΔΓ/Γ ≈ 0.08-0.83 per transit; Δε_θ ≈ 0.21·a_p·St_n ≈ 0.015-0.15 wheel-fraction (corrected, asy defect 7a) | D.19 mechanism row; D.16 R_AM is BLIND to it in the cycle mean (D.6 nullity survives pumping); only phase-resolved audits see it | NO |
| A6 | K_s sweep (w_rel/r)∂_φs | entropy stratification (hot/cold sector interleaving) arriving phase-lagged | a_s·St_n | data-dependent | J₁ bar; front content in A9 | NO |
| A7 | K_h0 sweep (w_rel/r)∂_φh0 | azimuthal enthalpy transport across sector boundaries | a_h0·St_n·(1+O(ε_θ)) | possibly ≪ a_p on near-uniform-T0 blowdown (HYPOTHESIS) | J₁ bar | NO |
| A8 | K_h0 work (Ω/ρ)∂_φp | wave-rotor unsteady work (lab ∂_t p through the wave frame); with A5 ONE mechanism — rothalpy split D_rel h0 = Ω·D_rel Γ, booked once via χβ_τ = β_w | a_p·St_n·β_w | Δh0/h0 ≈ 0.007-0.09 (0.7-9%) per transit | D.20 Δh0 = ΩΔΓ diagnostic row (contact-census caveat); J₁ bar | NO (already dropped by 4F too — var D13) |
| A9 | Front atoms n_φ[F_φ,rel] per row | difference between full 3-D RH and the imposed meridional RH on helical sheets (x = x_s(φ), n_φ ≠ 0): [I]=0 split into [h0],[Γ] ∝ n_φ[p]; s-production m[s] on azimuthal sheets | pointwise O(1); transit-integrated = jump-localized first-order residue; obliquity n_φ/n_x ~ Λ·(Δx_s/L) | percent to TENS of percent before fitted-sheet absorption ([k]_jump ~ 1 − PR⁻¹ = O(1)) | fitted inherited sheet (steady representation) + P-ii absorption prediction (CONJECTURE, pre-registered O5); invisible at ANY phase-sampling resolution | NO (partially represented by the fitted sheet; the n_φ error is normal-direction, not resolution) |

Notes to Part A: (i) drift census is SIX pieces — mass-row drift
(1/r)∂_φ(ρw) plus (w/r)∂_φ(u,v,Γ,s,h0) — the "five" of the asy artifact
is REPAIRED (asy defect 2; order impact nil). (ii) The advective rows above
and the conservative/div-form rows differ by the invertible triangular
recombination over K_ρ (R_row = K_row + coeff·K_ρ; ρ-factors on s/h0):
part of D.18's DEFINITION, re-derived independently by both pde sides;
a transcriber mixing the two readings builds a checker that fails on
correct fields. (iii) K ≡ 0 on axisymmetric data: every residual is
fluctuation-driven; honest ordering parameter = a·St_n. (iv) Coriolis/
centrifugal terms appear NOWHERE in R in either frame formulation
(PROVEN-HERE, both pde sides; the (B)-residual maps by
r·R_θ^(B) + Ωr²·K_ρ = R_Γ^(A), R_E^(B) = R_E^(A) − Ω·R_Γ^(A) — corrected
identities, pde D2).

### PART B — the [4F − 5F] bracket (REMOVED by the upgrade)

| # | Term | Physics | Order | Magnitude | Priced today by | Captured by 5F? |
|---|---|---|---|---|---|---|
| B1 | Radial-equilibrium pressure shift ∫ρu_θ²/r dr | 4F r-momentum lacks the centrifugal source: interior inconsistent with its own swirl-supported BC from step one; mass-flux redistribution across the gap | γ·M_θ²·α_gap | 0.6-9% of p (working 1.5-4%); single-signed (outward), phase-coherent, survives EVERY μ-average | nothing in-solve today; TWIN-C declared-residual reporting only | YES |
| B2 | Swirl-KE booking E_θ | u_θ²/2 in h0 / exit-KE misbooking. TWO VARIANTS (asy defect 3, repaired): FOLD (4F spends total h0 meridionally): ΔV/V = −δ²_exit/2, single-signed; DROP (meridional-only h0 handed): bias (δ_int²/2)(1 − r_in²/r_exit²) with δ_int = interface value (verifier pin R-B: exact only at δ = δ_int), geometry-signed, ≈0 at r_exit ≈ r_in. WHICH variant = the generator's h0-convention (var ledger (i)) — a D.13 contract fact to be pinned at ingestion | δ²/2 | 1.5-3% thrust (fold); |bias| ≤ δ_int²/2, and ≤ fold value iff r_exit ≤ √2·r_in (verifier R-B: the unconditional ≤-fold clause is FALSE on bell tubes beyond √2·r_in) | D.10 E_θ worst-case bar + TWIN discipline; D.20 linkage fires on convention-inconsistent data | YES (computed per contour; E_θ becomes a phase-resolved output) |
| B3 | State-recovery / margin bias | u_θ²/2 dropped from static-enthalpy recovery: T, c, and the spacelikeness audit biased | (γ−1)M_θ²/2 in T | 0.5-2.5% in T; margin understated 0.3-1.3% (direction: swirl cools, margin RISES — under u > 0 + AUD-c2T, hypothesis restored per var D4; state-sensitivity part only, D.5(ii) scope) | D.13 recovery audits | YES |
| B4 | N6-3 structural license | pointwise closure p = p(W,y) FAILS beyond free vortex (exact obstruction identity); 4F/Rao route structurally unlicensed on rotational data | structural (not a magnitude) | blocking | OBS monitor / D.14 blocks the route; G-b1 sensitivity gap gates its licensing leg | YES (bypassed: field-level route needs no closure; G-b1 de-scopes to the oracle role) |
| B5 | Exit swirl profile | Γ(ψ)/r_exit kinematic output (thrust-vector/downstream bookkeeping) | O(δ) | exit swirl angle 10-14° | absent at 4F | YES |

All B-rows are STEADY, SINGLE-SIGNED (B2-fold), PHASE-COHERENT biases with
NO protecting cancellation — the precise asymmetry against the A-rows,
which are mean-protected on-ray at first order. Value claim of record
(REPAIRED form, asy defect 4): 5F removes the largest QUANTIFIED
unprotected bias class; the post-upgrade chain is sweep-limited; the
absolute "largest unprotected class" form is NOT available because the
retained class's unprotected remainder (jump residue P-ii, off-ray area
incl. a_w, torque feed-through χ·ΔΓ/Γ up to ~9% in h0 at St_n → 1) is
unquantified of record. St_n-conditional, pending P-ii / S.22.

==============================================================================
## §2 HYPOTHESIS LEDGER of the five-field per-phase model

Every row: hypothesis (explicit or previously hidden) / violation channel
/ meter or falsifier. Consolidated from all four lenses + refuters; rows
marked ● were SURFACED BY THIS PANEL (not previously in a record ledger).

| ID | Hypothesis | Violation channel | Meter / falsifier |
|---|---|---|---|
| H-A1/T0 | strict T0: pure rotating pattern, n identical waves; ξ↔φ affine (D.17) DEFINES the per-phase family | mode-hop, counter-rotation, modulation — the whole quotient dies, not degrades | T0-flatness monitor; [T-SLRW] side-load channel as impurity detector; ¬H-AM1 aperiodic storage |
| H-DATA | contract family = exact interface trace, s(ξ) = s_3D(ξ) | truncation (today: u_θ dropped entirely); generator provenance | D.13 audits + D.14 TRIPLE (G6); term (II) additive at first order, separately monitorable |
| H-F1 | frozen family: s(·), μ, Ω independent of Σ | back-pressure feedback → bilevel PB-4 | chamber response map (record row) |
| ● H-SEG | segment-averaged linearization boundedly invertible (needed for the EXACT error representation (ER)) | front-carrying slices: weak-vs-weak comparison (g2a), contacts (g2b) — OPEN there | S.22 route; front census per dataset |
| H4/D3 | per-phase uniqueness + S1 regularity | wall-shock formation, secondary shocks | S1 monitors; P7 boundary |
| L4/m_n | march margin m_n = ess inf(M_n − 1) > 0, meridional-normal form (curved Γ_d) | sonic approach: domain of dependence blows up ~1/m_n | m_n(ξ) declared per phase; M_tot PROHIBITED as audit quantity (D.5(iii)) |
| H-REACH/H-FIB | every streamline meets Γ_d exactly once (streamtube topology) — consumed by Γ(ψ),s(ψ),h0(ψ) AND by the adjoint transport (★) (panel: the ADJOINT consumes it too ●) | recirculation, separation bubble at spike base | through-flow guard + streamline census |
| H-ANN / axis | annular class r_min > 0; bell-family axis needs Γ = O(r²) (smooth) or O(r) (finite-h); spike tip with Γ_wall ≠ 0 admits NO regular solution (vortex-core obstruction) | tip singularity; core radius r_core/R_int ≳ √(f_θ·KE/h0) ≈ 0.065-0.14 (verifier-corrected band R-A via √(ε_θχ/2); §5 C1) — not negligible | contract audit sup_y Γ/y² near axis; declared core model otherwise |
| H-CVX (arc) | entropy admissibility along connected Hugoniot arcs | exotic EOS only; DISCHARGED unconditionally in-model: G_fund = 1 + (γ−1)(γ+Tγ′)/(2γ) > 1 | γ(T)-exact closed form (twice pen-re-derived of record) |
| AUD-cp/c2T/hRANGE | state recovery unique + in table range | table-edge data | recovery rejector flags, never extrapolates |
| ● H-VANELESS + no-free-jet | wetted surfaces = surfaces of revolution, slip; boundary census ∂D = Σ∪S_e∪Γ_d(∪axis) with NO free (constant-pressure jet) boundary — the §4 gradient formula is FALSE on a vaned wall and UNDERIVED for external-expansion plug flows (var D10) | vanes/struts (torque → design variable); truncated/external-expansion spike | D.6/D.16 torque bookkeeping; geometry census; free-boundary adjoint = named OPEN |
| ● H-FROZEN-Γ (zero mixing) | Γ, s advect unmixed to the exit (E4/E5 exact) | turbulent sector/annulus mixing; swirl-KE → heat | two-station A4 decay audit (R_AM is BLIND to mixing — internal torque); RANS/LES twin prediction: Isp ≥ 5F prediction on plug family (Gibbs-argument direction, PROVEN-HERE) |
| in-slice steadiness | ∂_φ = 0 within the slice — the reduction itself; drops exactly the six K rows | everything in §1 Part A; St_n ~ 0.1-1 MARGINAL | J₁ bar computed (never argued away on swirl data until the 5F-T3QS carrier lands); S.22; O5-lite |
| ● H3-w | interface swirl-profile SHAPE phase-invariant (the NEW hypothesis under which the 5F ray-cancellation P1-P6 holds) | real data expected to violate at some a_w > 0 (D.14 expectation) → O(a_w·St_n) off-ray hysteresis channel the 4F bookkeeping never had | measure a_w on first dataset; rejector R2′ (phase-dependent ŵ breaks P5) |
| ● [H-sgn] | ε_θ co-rotating (w > 0 wave-sense) in M_rel = M_Ω(1−ε_θ) and the drift coefficient | D.11 CONJECTURE expects counter-wave plain-mean swirl → M_rel = M_Ω(1+|ε_θ|) (conservative direction taken) | sign(A3) on first dataset (D.11's F3) |
| ● a_Γ ~ a_p, a_h0 ~ a_p | fluctuation amplitudes of Γ and h0 comparable to pressure's (load-bearing for "torque co-leading" and for K_h0 weighting) | phase-locked Γ profiles (a_Γ ≪ a_p): torque strictly dominant; uniform-T0 blowdown (a_h0 ≪ a_p): work term dominates K_h0 | per-field a_q measured at ingestion (G-e window) |
| ● h0-convention | contract h0(y;ξ) INCLUDES u_θ²/2 (D.1's h0); decides the B2 fold/drop variant | probe data reporting meridional stagnation under-book by exactly E_θ; silent convention mismatch | contract provenance row (declare the generator's convention); D.20 Δh0 = ΩΔΓ linkage fires on inconsistency |
| SC-8 / g2b | slip-line-free sub-scope declared, OR contacts carried as fitted tracked fronts | contact data: convex-integration non-uniqueness kills the relative-entropy route; supersonic vortex sheets only weakly/neutrally stable | front census per dataset; contact-crossing adjoint calculus = OPEN (§4) |
| H-AM0..5 | D.6 accounting regularity + declared torque budgets | injection swirl J_inj, orifice sidewall torque, viscous moments | D.16 R_AM row with derived tolerance; concentration tests |
| ● class-wide T0 | H-A1 holds for EVERY Σ in the design class (needed for the 2-ε transfer's uniformity route, fun DEF-7) | design-induced mode change (PB-5 boundary) | operability maps; add "(0) H-A1 uniformly on A" to the §4.2 uniformization list |
| frozen composition | no reaction downstream of Γ_d (H-R1); NEW coupling ●: swirl-KE dissipation heat could re-cross ignition thresholds | afterburning | H-R1 energy-flux residual row |

==============================================================================
## §3 WHAT STILL ESCAPES (closed list — no per-phase machinery, at ANY
##    sampling resolution, captures these)

E1. IN-DUCT SWIRL GENERATION (K_Γ torque). Controls: a_p·St_n, β_τ.
    Magnitude: ΔΓ/Γ ≈ 0.08-0.83/transit; Δε_θ ≈ 0.015-0.15 wheel-fraction
    (corrected coefficients). Slice = closed universe: cannot receive
    torque. Feeds N6-3 obstruction downstream of where it is generated.
E2. INTERIOR PHASE LAG (sweep of ρ,u,v,s). Controls: a·St_n. Pointwise
    state error 7-70% of the fluctuation scale; MEAN-thrust effect
    protected on-ray (O(St²) smooth cycles; jump-localized on sawtooth —
    protection proven at 5F under H3-w), area-term hysteresis off-ray.
E3. h0 PUMPING / ROTHALPY SPLIT (K_h0 work). Controls: χ ≈ 0.06-0.20,
    a_p·St_n·β_w. Magnitude Δh0/h0 ≈ 0.7-9%/transit. 5F transports h0 and
    Γ separately where truth transports only I = h0 − ΩΓ. Free diagnostic:
    Δh0 = ΩΔΓ on contact-free uniform-I bundles.
E4. FRONT PUMPING IN THE SWEEP WINDOW (wave-passage straddling parcels;
    s-production atoms). Controls: St_n (window width), [p]/p, [s] = O(1).
    Fitted sheet = steady shadow; absorption = P-ii, CONJECTURAL.
    Sub-window relaxation escapes at any N_ξ.
E5. HELICAL GEOMETRY OF INTERIOR SHEETS (per-phase standoff x_s(ξ) with
    meridional RH vs true helical surface with n_φ ≠ 0). Controls: Λ,
    Δx_s/L. A NORMAL-DIRECTION error, invisible at any sampling. Magnitude
    OPEN pending measured Δx_s; adjacent estimate: acoustic-lag ratio
    0.1-1 on subcritical phases.
E6. SUB-PHASE SAMPLING (quadrature of the ξ-family). Controls: a² ≈ 0.5,
    N_ξ, St_n. First-order channel if the sawtooth jump is unsplit;
    restorable by split/fitted-window quadrature EXCEPT inside E4's window.
E7. WAVE-FRAME-STATIONARY AZIMUTHAL ACOUSTICS (the H-NC kernel at
    |w_rel| = c). Controls: M_rel − 1. Structural (lock-in/resonance
    boundary), lives entirely in the struck operator. Same locus where the
    C51 azimuthal march degenerates (panel's structural identification).
E8. CONTACT/SLIP-SHEET 3-D STRUCTURE (helical vortex sheets, roll-up,
    instability windows). No small group — structural; currently
    UNPRICEABLE on the named route (g2b known-broken).
E9. MODE IMPURITY / NON-Z_n OPERATION. Outside the quotient entirely.
    Monitored, never captured.
E10. SWIRL-KE RECOVERY BEYOND THE VANELESS CLASS. Scope boundary, not an
    error: ceiling f_θ = 3-6% of KE.
E11. NON-MODEL CHANNELS (viscous/turbulent torque moments, parasitic
    deflagration, J_inj, discrete-orifice torque). Declared-budget rows
    (D.6/D.16); the model computes none of them.

FUSION NOTE (mechanism-to-ray-family map, pde §4-bis.4, refuter-verified):
E1/E3-per-its-work-part and the azimuthal acoustic content live on the
AZIMUTHAL APERTURE of the Mach cone (amputated by the slice); E2/E4 and
the sweep parts live on the ADVECTIVE HELIX (winding truncated to zero).

==============================================================================
## §4 ADJOINT / OPTIMIZATION VERDICT

BUILDABLE: YES. Status by component:

PROVEN (pen + machine, deriver + refuter independently, judge-sampled):
- Linearization (A,B,M), r-weighted, zero leftover; carrier dictionary
  diag(1,r,r,r,r) declared. The multiplier dictionary is pinned AGAINST
  D.1's CONSERVATION-form Γ-row: ψ_Γ = ψ₄/r (var D5 repaired; the
  advective ρDΓ row's multiplier is ψ₄ itself).
- Full advective adjoint system (A-ρ)..(A-p); the swirl-adjoint invariant
  form (★) D(ψ₄/r) = −(2Γ/r³)ψ₃: ψ_Γ streamline-transported backward,
  single centrifugal source — the exact adjoint mirror of the primal
  structure. New-term census (N1)-(N7) incl. the free-vortex decoupling
  (adjoint-side N6-2) and the dual-consistency trap (N4: off-shell entries
  a hand-simplified adjoint drops are wrong on unconverged iterates).
- Boundary structure: wall BC ψ₂n_x + ψ₃n_r = 0; exit datum
  ψ|_{S_e} = (u,1,0,0,0); axis parity ψ₃ = ψ₄ = 0 (a regularity-type
  boundary constraint, not free data — N1 wording repaired, var D11);
  Green row dJ/dw = −rρu_nψ₄|_{Γ_d} (display (G) carries the minus sign,
  var D3 repaired) — a NEW instrument: derived bars for the required
  swirl-data accuracy, δw ≤ tol_J / ∮|rρu_nψ₄|.
- Shape gradient: sliver identity rρu̇_ν = ∂_s(rρu_τδn) derived; gradient
  density G = rρu_τ∂_sψ₁ FORM-INVARIANT vs meridional — no explicit
  centrifugal wall term exists in the exit-functional formulation (flag F1
  RESOLVED in the deriver's favor by the refuter's independent
  derivation); all swirl content routes through (N2)/(N3) into ψ₁.
- Characteristic structure: adjoint pencil = primal pencil (Γ-free);
  backward march licensed by the SAME margin m_n; swirl margin-benign at
  fixed meridional data (u > 0, AUD-c2T).
- SONIC EXIT (REPAIRED — var D1, judge-verified by direct algebra): the
  datum does NOT blow up. The solve reads ψ₅(u² − c²) = 0 with EXACT-zero
  RHS (Cramer numerator vanishes identically); (u,1,0,0,0) extends
  continuously through u = c, where the datum acquires GAUGE
  NON-UNIQUENESS along (c²,−c,0,0,1) ∝ the record's terminal gauge l(n)
  (carrier 5F.4) with compatibility held exactly by the N6-1(c) kernel law
  ⟨g,r⁻⟩ = rρ(u−c)². Hazard re-typed: 0/0 conditioning of a generic
  linear solve near u = c (cure: solve in the quotient mod l(n)) + loss
  of the "δV free at exit" premise. Exit-margin meter retained.

SCALING-ESTIMATE (named): Γ²/r³ stiffness near an inner body
(centrifugal/inertia 0.15-1.3 at a spike tip; Lipschitz ~ r_min⁻⁴);
backward amplification of ψ_Γ — closed-loop exponent ≈ √2(u_θ/W)(Δs/r)
(var D12: the displayed single-leg exp(1-5) is an upper envelope);
family-level quadrature must resolve ξ-alternation of near-tip ψ_Γ.

OPEN (each with owner/workaround):
- Lip/corner assembled condition ([S-5F] SCHEMA leg). Pins: terminal gauge
  swirl-component zero (corner COUNT unchanged); must collapse to Rao
  (L.15) on free vortex.
- Contact-crossing adjoint calculus (transposed contact conditions,
  gradient continuity at moving contact feet) — same wall class as g2b;
  meter: dot-product test on a contact-carrying datum vs mollified twin.
  Workaround: slip-line-free sub-scope (auditable) or fitted contacts.
- Semiglobal-in-x well-posedness import: inherits D2.5/[C-D25U] via N6
  §4-§5 (the precise conditional — asy D12 repair), nothing new assumed.
- Free-boundary (external-expansion plug) shape calculus (var D10).

ANTI-SPIKE (RECOVERY-ASYMMETRY) MECHANISM — does it emerge in-gradient?
PARTIALLY, with the overclaim repaired (var D2):
- STRUCTURALLY YES: dJ/dΣ is the true derivative (machine-backed Lagrange
  identity); every swirl effect is inside it via (N2)/(N3); the
  free-vortex specialization reproduces the record's per-streamline
  THEOREM* sign (T-T3-MAP(c)); the within-family tilt is a gradient
  component the optimizer follows; across families it is a computed ΔJ in
  the tournament. The streamtube estimate (8.1) δ(ṁu_e) =
  ṁ(Γ²/(u_e r_e³))δr_e has the anti-spike sign.
- NOT YET VERIFIED AS PRINTED: the duality step assumed a wall
  perturbation realizing per-tube fixed (p_e, v_e) migration — generically
  unrealizable at finite swirl (the exit plane carries the
  radial-equilibrium gradient the model itself restores). Claim downgraded
  to SCALING-ESTIMATE (sign, per-streamtube) + record consistency.
  DECIDING INSTRUMENT: one computed 5F gradient on a swirl-carrying
  instance — dot-product (O3.1-class) test + sign of dJ against an
  outward-migration perturbation family; family-gap prediction with the
  CORRECTED ratio ΔJ_swirl/J ~ (E_θ/KE)·⟨1 − (r_spike/r_bell)²⟩ > 0
  (var D7 repaired; 1-4% band unchanged).
- Landscape: no new small-swirl nonconvexity GIVEN a nondegenerate
  swirl-free reduced Hessian (hypothesis surfaced, var D9); finite swirl
  adds concave migration reward + r_min⁻⁴ Hessian anisotropy
  (ill-conditioning, not nonconvexity); data-side BV kinks at contact
  ψ-levels (OPEN, g2b class).

INSTRUMENT DUTIES NAMED: swirl row wired into the O3.1 dot-product oracle
+ R1-class corruption rejector (exist at carrier level, not in the engine
suite); committed carrier for the 5F ray-cancellation battery (X-T3QS
extension); exit-margin per phase; contact-datum gradient-noise meter.

==============================================================================
## §5 CONTRADICTIONS BETWEEN LENSES / DERIVER vs REFUTER — each resolved

C1. χ = ΩΓ/h0: pde said 0.3-0.8; asy said 0.06-0.20 (working 0.10). BOTH
  refuters "confirmed" their own lens's arithmetic — a genuine cross-lens
  contradiction neither saw. JUDGE RESOLUTION (JV, own algebra): the two
  differ ONLY in the reading of "tangential energy fraction 3-6%". pde
  used u_θ² = 2f·h0 (fraction of TOTAL enthalpy); asy used f = u_θ²/|u|²
  (fraction of KINETIC energy). Test against the independently measured
  ε_θ = 0.15-0.20 and the physical wheel speed: KE-reading ⟹ M_Ω =
  δ·M_x/ε_θ ≈ 1.5-2.5 ⟹ Ωr ≈ 1.8-3.2×c ≈ D_CJ ≈ 2000-2500 m/s ✓;
  h0-reading ⟹ M_θ = √(f·h0/c²·2)… gives M_Ω ≈ 3.6-6 ⟹ Ωr ≈ 4300-7500
  m/s ✗ (physically impossible for the CJ-locked wheel). VERDICT: the
  KE-normalized reading stands; χ ≈ 0.06-0.20 OF RECORD for this panel;
  the pde (6b) order line (already the pde refuter's MAJOR D1) is doubly
  repaired: order = a_p·St_n·β_w ≈ 0.007-0.09, derived via ΔΓ/Γ =
  a_p·St_n·β_τ and the exact closure χβ_τ = β_w — which DISCHARGES the
  pde refuter's [H-TORQ] hypothesis into a group-quantified estimate
  (residual hypothesis: a_Γ ~ a_p, ledger row). CONSEQUENCE for pde
  §4.3(iii): spike-tip core bound weakens from √f ≈ 0.17-0.25 to
  r_core/R_int ≳ √(f_θ·KE_int/h0) = √(ε_θχ/2) ≈ 0.065-0.14 (verifier
  repair R-A: the judge's printed 0.10-0.19 was internally inconsistent
  with its own χ = 0.06-0.20; 0.19 needs interface Mach ≈ 3.9, outside
  the record class) — same conclusion (not negligible), corrected band. ⚠ FLAG TO THE PROGRAM FRAME (loud):
  "tangential energy fraction 3-6%" is normalization-UNPINNED in the
  frame; moreover the record's OWN instrument A4 = swirl-KE flux /
  (2·energy flux) is h0-normalized, so at concordant numbers A4 will
  measure ≈ 0.3-2.5%, NOT 3-6% — pin the convention before the first
  dataset ingestion or the A4 falsifier will "fire" on a unit mismatch.
C2. D.18 iff labels: pde, var, fun artifacts (and the var refuter's anchor
  audit) carried "THEOREM* (judge-downgraded) per VERDICT §3.2"; the asy
  refuter flagged supersession. JUDGE VERIFICATION AT SOURCE (JV, this
  window): r2pass/VERDICT_r2pass.md:247-261 — J-r2p-2 and J-r2p-3 hold
  BOTH D.18 iffs at SCHEMA (E-3 escalation processed in the formalization
  doc §6-quinquies; labels unchanged at SCHEMA; restoration = G-f
  battery). RESOLUTION: SCHEMA is the label of record; ALL FOUR lenses
  consume D.18 only at its DEFINITIONAL level (the unconditional operator
  identity + recombination + atom displays), independently re-derived by
  three of them — so the repair is label-hygiene, not content: no panel
  conclusion moves.
C3. Sonic-exit datum: var deriver "blows up like 1/(u²−c²)" vs var refuter
  "gauge non-uniqueness, no blow-up". JUDGE RESOLUTION (JV, algebra
  re-executed): refuter is RIGHT — the δρ/δu/δp system forces
  ψ₅(u²−c²) = 0 with exact-zero RHS; solution family at u = c is
  (u,1,0,0,0) + t(c²,−c,0,0,1), the kernel direction mapping to l(e_x)
  under the declared dictionary. Deriver's claim 14 REFUTED; repair in §4.
C4. "K_Γ, K_h0 nonzero on swirl data" (var) vs the 4F baseline: K_h0's
  work term is nonzero ALREADY at swirl-free data (4F drops it too); the
  genuinely NEW live content at 5F is the ∂_φΓ sweep leg (and a carried-Γ
  budget for the torque to be compared against). Resolved per var D13;
  wording carried into §1.
C5. Torque/work orders, pde vs asy: CONSISTENT — one mechanism, χβ_τ =
  β_w exact; pde's underived (6b) line is superseded by asy's derivation
  (see C1).
C6. T3QS protection on swirl families: var F2 ("MUST NOT be invoked until
  an extended carrier passes") vs asy §4 (5F ray-cancellation PROVEN-HERE
  under H3-w, machine-checked, refuter-re-verified with an independent
  transcription covering the author's common-mode hole). RESOLUTION: both
  stand at different levels — the MATHEMATICS now exists (two independent
  derivations + two machine checks + firing rejectors: the strongest
  panel-internal grade), but per house discipline (R5) the LICENSE to cite
  smooth-cycle J₁ = 0 on swirl families in any repo document waits for
  the committed carrier (X-T3QS battery extension, F2-window duty). Until
  then the J₁ bar is COMPUTED on swirl data, never argued away.
C7. Wound-cone "width": pde deriver's Δθ'_dom as "arc width" vs refuter
  D3: the bracket bounds the EXTENT from the section to the far edge
  (the right object for "data the slice never consults"); literal width
  → 0 as c → 0 while the advective OFFSET stays St_n. Wording resolved
  per refuter; claims 13/14 stand.
C8. "CJ locus" naming: {|w_rel| = c} (azimuthal SCALAR) vs [T-NSW](a)'s
  CJ surface on the relative VECTOR |w_vec| = c — they coincide only
  where the meridional relative component is negligible (near-interface).
  The kernel/marchability identification (pde claim 16) is EXACT on the
  azimuthal-scalar loci; the "CJ" NAME is approximate away from the front
  (record's own gloss does the same). FLAG carried, per pde D7.
C9. Error-bound status, fun vs asy: NO contradiction — both state
  pointwise-large K, transit-integrated O(St_n) structure, constant OPEN
  (C-T1 CONJECTURE), no finite C proven on contact classes.
C10. Nullity-survives-pumping label (var claim 21): conclusion holds via
  D.6 (THEOREM*, conditionals (c1)/(c2) inherited), NOT by the printed
  one-liner (a zero-mean source does not by itself control a flux-weighted
  correlation). Label repaired to PROVEN-IN-RECORD per var D8.
C11. M_rel sign: asy's M_rel = M_Ω(1−ε_θ) assumes co-rotation; record
  D.11 CONJECTURES counter-wave mean swirl (M_rel = M_Ω(1+|ε_θ|), farther
  from both the lock-in kernel and the C51 threshold). Conservative
  direction taken; [H-sgn] surfaced in the ledger (§2).

==============================================================================
## §5-bis FUNCTIONAL-IDENTITY VERDICT
##  ("cycle-mean thrust = μ-integral of per-phase thrusts")

EXACT HALF — status PROVEN-HERE (theorem-grade; independently re-derived
end-to-end by the fun refuter; judge-sampled):
  J_exact = ∫_Ξ F_true(ξ; S) dμ(ξ)   for EVERY admissible S,
  F_true(ξ;S) := 2π ∫_{C_S} G(l, φ(ξ)) r dl,  φ(ξ) affine,
under ONLY: strict T0, S fixed axisymmetric, Pa constant, G ∈ L¹.
Proof = 4 steps (rotation-invariance ⟹ F_S(t) constant; Fubini; Z_n
reduction; affine change of variables — μ emerges as the pushforward of
time, uniform BECAUSE the traversal is rigid rotation; all data
non-uniformity lives in ξ ↦ s(ξ), never in the ξ-measure). Companion
remarks proven: type-check (degenerate axisymmetric ⟹ F_true = total
thrust, so F_true vs F_2D is well-typed) and S-dependence
(F_sect(φ;S) − F_sect(φ;S′) = −∂_φM(φ), whose φ-mean vanishes — the
sweep REDISTRIBUTES axial momentum between phases, never creates it in
the mean; scope-restricted to no-wall wedges with the distributional
reading at fronts, fun DEF-6). This identity exists NOWHERE in the record
as a numbered statement (F-2, refuter-confirmed on the checked anchors):
CANDIDATE MINT for the R4 window. It also licenses the new O5-lite
comparison (C) below.

THE SINGLE SUBSTITUTION — F_true(ξ) → F_2D(ξ) (independent steady
per-phase solve with data s(ξ)). For the FIVE-FIELD model this is exactly
ONE substitution (by D.18's definitional decomposition); for the CURRENT
meridional engine it is one substitution PLUS two separately-committed
channels (contract truncation of u_θ — boundary term (II), additive at
first order; dropped Γ/centrifugal/swirl-KE rows — the §1 Part B content).
Cleanest statement of what the upgrade buys: it shrinks the committed
content of the approximation half from {θ-coupling + swirl channels +
contract truncation} to {θ-coupling} alone.

EXACT ERROR REPRESENTATION (no remainder), under (H-DATA) + (H-SEG):
  J_exact − J_avg = −∫_Ξ ⟨ψ̃_ξ, K(V_3D)(ξ)⟩ dμ(ξ)          (ER)
(ψ̃ = segment adjoint, not computable; on front-carrying slices (H-SEG)
is OPEN — g2a/g2b walls). FIRST-ORDER FORM (repaired per fun DEF-1/2):
THREE declared commitments — ψ̃ → ψ (O(‖dV‖²)); K(V_3D) → K(W_A)
(O(K·dV) = O(St²), previously silent); and ONE normalization pinned:
  J₁^K := −∫⟨ψ_ξ, K(W_A)(ξ)⟩dμ  =  the FULL first-order error
        =  St · J₁^{ledger}      (ledger normalizes S_sweep to O(1));
T3QS's J₁ is J₁^K. The operator dictionary D(W) ≡ div-form K row is
EXACT (thrice re-derived).

CAN THE ERROR BE LARGE? — the honest three-tier answer:
- PROVEN: bound STRUCTURE |J_exact − J_avg| ≤ C·St_n·V_data with C =
  C(margin, base gradients, front count, adjoint oscillation, geometry);
  C is not provably small at St_n ~ 0.1-1 (C-T1 CONJECTURE; no proven
  expansion radius), and on the general front/contact class NO FINITE C
  is proven at ANY St (g2a weak-vs-weak; g2b known-broken). THE FEAR
  "large" CANNOT BE REFUTED BY THEORY TODAY.
- PROTECTIONS (proven mechanics): K̄ = 0 fiberwise UNCONDITIONALLY on
  periodic BV composites (atoms and data-cycle jumps included —
  STRONGER than the deriver printed, fun DEF-5; and G-f-robust because
  the differentiation is 1-D in φ at fixed (x,r), no front-surface
  measure enters). Hence exactly TWO first-order channels:
  (J) jump term ⟨ψ̄, atom content⟩ — localized in the wave-passage
  window ~St_n, the physics the fitted sheet represents; absorption =
  P-ii, CONJECTURAL; (H) hysteresis term −Cov^{ac}_μ(ψ, K) — vanishes
  IDENTICALLY on T3 ray families (independent re-derivation of T-T3QS
  P5-P6, agreeing; NOW EXTENDED to five fields under H3-w). Channel
  VALUES are convention-dependent (a.c.-only/ψ̄-pairing pinned as the
  convention of record before O5-lite measures the split).
- BREAKING: off-ray two-parameter cycles; phase-dependent profiles
  (incl. H3-w violation, a_w-channel); non-affine objective; cap-binding
  subsonic phases (acoustic lag); St_n → 1 (frame degrades, O(St²)
  uncontrolled).
- MAGNITUDE (SCALING-ESTIMATE): single-digit-% total PLAUSIBLE on
  ray-like sawtooth cycles with a good fitted sheet; >10% NOT EXCLUDED on
  off-ray, jump-heavy, cap-binding cycles. Any hardware number from rung
  2 without an St error bar is out of contract (PB §8, confirmed).
- DECIDING MEASUREMENT (O5-lite, one certified instance): (A) J_exact vs
  J_avg; (B) vs J_avg + J₁^K (tests the frame); (C) F_true(ξ) vs F_2D(ξ)
  pointwise — LOCALIZES the error, discriminating (J) from (H) — the new
  comparison licensed by the exact half; (D) St-sweep exponent (→2 on-ray,
  →1 off-ray); (E) fitted-sheet ON/OFF in the jump window (tests P-ii).
  Rejectors: error not ↓ under St→0 kills C-T1; exponent 1 on a smooth
  ray cycle kills the carrier assumptions; distributed O(1) mismatch
  outside the jump window kills localization.

2-ε VALUE TRANSFER — PROVEN-HERE and sharp: if
sup_A |J_exact − J_avg| ≤ ε (U), any J_avg-maximizer is ≤ 2ε-suboptimal
for J_exact; constant 2 unimprovable (two-point example); η-variant and
two-point weakening (ε₁ + ε₂ + η) proven. UNIFORMITY STATUS: OPEN twice
over (pointwise bound OPEN per S.22; Σ-uniformization rests on uniform S1
— P7-priced) PLUS the panel's addition (0): class-wide H-A1 (no
design-induced mode change — PB-5), fun DEF-7. Credible theorem target on
the shock-free-reference sub-scope. G2 CONSEQUENCE: every rung-2 gain Δ
certifies an exact-world gain only NET OF 2ε; with ε unmeasured every G2
verdict is CONDITIONAL — the F5a Verdict template should carry "gain net
of 2ε, ε = <measured/assumed>".

==============================================================================
## §5-ter BICHARACTERISTIC SECTION CHECK

The pde lens DELIVERED the dependence-domain truncation analysis in full
(§4-bis, refuter-verified incl. an explicit counterexample-ray
computation); judge-confirmed adequate. Fused statement of record:

- 3-D symbol det ∝ (w_vec·ζ)³[(w_vec·ζ)² − c²|ζ|²], w_vec = (u, v,
  w_rel): advective rays = relative-streamline HELICES winding opposite
  the wave; acoustic rays = one-sided helical Mach cones where
  |w_vec| > c.
- Advective winding per meridional transit: Δθ'_adv/(2π/n) =
  St_n(1 − O(ε_θ)) — the GEOMETRIC MEANING OF St_n: swept sectors per
  transit (= PB §8 verbatim; FLAG-3 of record: PB's τ_n = ∫dx/u and
  S.22's (w_rel/r)(L/W) agree at scaling order, differ O(1) on strongly
  turned streamlines — one definition to be pinned by a future carrier).
- The full backward cone from an interior point meets Γ_d in an azimuthal
  arc at EXTENT (not width — repaired wording, pde D3) from the section
  bounded by [1 − O(ε_θ), (1 + c/|w_rel|)·u/(u−c)]·St_n·(2π/n): an O(1)
  margin-controlled factor degenerating only as u − c → 0.
- The frozen slice's rays have ZERO winding: the reduction replaces the
  true WOUND cone by its meridional section — St_n = truncated azimuthal
  width / sector angle. Quasi-steadiness IS ray-slice alignment; at
  St_n ~ 0.1-1 the misalignment is marginal-to-O(1): why rung 2 is not
  self-licensing.
- MECHANISM-TO-RAY-FAMILY MAP: sweep transport (K_u, K_v, K_s + sweep
  parts of K_ρ, K_Γ, K_h0) = phase-lag on the ADVECTIVE helix family;
  inter-sector pressure torque/work (∂_φp legs of K_Γ, K_h0) = the
  amputated AZIMUTHAL APERTURE of the acoustic cone (swirl-generation +
  wave-work channels; T3QS's B2 acoustic-lag channel in the unshielded
  sectors).
- NEW STRUCTURAL RESULT (verified correct, and new as far as the record
  search reaches): the azimuthal-march spacelikeness condition is
  |w_rel| > c (= C51's regime condition verbatim), and its two degeneracy
  loci — the advective kernel {w_rel = 0} (multiplicity 3) and the
  acoustic locus {|w_rel| = c} — are LITERALLY the H-WR and H-NC kernel
  loci of D.18's second iff: the reduction-residual kernel and the
  marchability boundary are ONE geometric object. ({w_rel = 0} lies
  strictly inside the dead band |w_rel| < c — one boundary, not two; and
  "CJ locus" names the azimuthal-scalar locus only approximately away
  from the front, §5 C8.)
- The general C3 helical-foliation leaf condition
  |w_rel cosχ + u sinχ| > c interpolates C2 (u_x > c) and C51; a global
  spacelike helical foliation with periodic closure remains OPEN (the N6
  open item). What a helical march would restore: all K terms
  (integrated, not dropped), the wound-cone causality, the UNSPLIT
  rothalpy invariant, helical fitted fronts, the periodic-orbit
  structure; it dies structurally at |w_rel| ≤ c.
- X-marching condition re-derived, not asserted: spacelike x = const ⟺
  u_x > c (Monge-cone soundness verified; hyperbolicity q_m > c does NOT
  march — explicit 0.5c/1.2c counterexample ray computed; M_tot licenses
  nothing); curved surface: u_m·n_m > c, margin m_n.

==============================================================================
## §6 PER-ITEM CONVERGENCE STATUS

Legend: CONVERGED = deriver + refuter agree, algebra independently
verified. REPAIRED = defect found and fixed (fix stated). DISPUTED-OPEN =
what decides it. EVERY MAJOR defect from all four refuters appears.

### PDE lens (11 claims; refuter: 0 critical / 1 major / 7 minor)
| Item | Status |
|---|---|
| Exact wave-frame system, both formulations, equivalence, rothalpy variable (cl. 1-3) | CONVERGED (full independent re-derivation; D5 garbled chains repaired presentationally) |
| Exact split, K rows, triangular recombination, no Coriolis in R (cl. 4-6) | CONVERGED; D2 REPAIRED: residual map is r·R_θ^(B) + Ωr²·K_ρ = R_Γ^(A), R_E^(B) = R_E^(A) − Ω·R_Γ^(A) (commuting recombination, not "frozen mass row") |
| Residual enumeration + orders (cl. 5/7) | REPAIRED (pde-D1 MAJOR): (6b) order line was underived with a dead √2 fragment; fixed by the asy derivation a_p·St_n·β_w via χβ_τ = β_w; [H-TORQ] discharged into ΔΓ/Γ = a_p·St_n·β_τ (residual hypothesis a_Γ ~ a_p in the ledger); χ value adjudicated 0.06-0.20 (§5 C1); D4 normalization column noted; D8 cross-ref to SC-9 (source-scaling ≠ solution-error bound) added |
| Symbol, marching u_x > c, curved M_n > 1 (cl. 6/9/10) | CONVERGED (cofactor + Monge cone + counterexample ray, all re-executed) |
| Axis/spike-tip core (cl. 11/7) | REPAIRED: h_min ≥ 0 convention stated; core bound corrected to ≳ √(f_θ·KE/h0) ≈ 0.065-0.14 (verifier R-A; §5 C1); tip-Γ level stays HYPOTHESIS |
| In-slice RH = n_φ → 0 limit of [I] = 0 (cl. 12) | CONVERGED; D6 REPAIRED: atom-density coincidence carries the record's surface-measure-normalization caveat (G-f check target) verbatim |
| Wound cone, winding, C_geo (cl. 13-14) | CONVERGED; D3 REPAIRED (extent, not width) |
| Mechanism-to-ray map (cl. 15) | CONVERGED |
| Azimuthal march ⟺ \|w_rel\| > c; loci = H-NC/H-WR kernels (cl. 16-17) | CONVERGED (new result verified); D7 REPAIRED ("CJ" naming caveat, §5 C8); global C3 foliation OPEN |
| Solution class SC-1..SC-9 (cl. 18) | CONVERGED as hypothesis list (labels match record certifications) |

### ASY lens (refuter: 0 critical / 4 major / 9 minor)
| Item | Status |
|---|---|
| Master formula, group census, concordance, FLAG-1 (PB §8 "≪" overstates drift suppression) | CONVERGED (machine-checked twice, independent symbol sets); Defect 5 REPAIRED ([H-sgn] surfaced); Defect 6 REPAIRED (γ = const conversion boundary named on χ, β_w — exact defs survive with local γ) |
| Residual ordering table | CONVERGED as scale ratios; Defect 2 (MAJOR) REPAIRED: drift census = SIX pieces incl. drift-of-h0 and the full mass-row drift (1/r)∂_φ(ρw); magnitudes unchanged |
| D.18 label inheritance | Defect 1 (MAJOR) REPAIRED + judge-verified at source: both D.18 iffs = SCHEMA per J-r2p-2/J-r2p-3 (r2pass VERDICT 247-261), E-3 processed, restoration = G-f; no load-bearing consumption anywhere in the panel (§5 C2) |
| 4F→5F removed errors R1-R5 | R1, R3 (with D.5(ii) scope caveat, Defect 9), R4, R5 CONVERGED; Defect 3 (MAJOR) REPAIRED: R2 split fold/drop variants, variant = h0-convention contract fact (fused with var ledger (i)); Defect 7 REPAIRED (coefficients recomputed: 0.208, 0.75·a_p·St_n, Λ = 0.59-1.11·St_n — verifier typo repair R-C) |
| Protection asymmetry / value claim 16 | Defect 4 (MAJOR) REPAIRED: claim of record = "largest QUANTIFIED unprotected class; St_n-conditional pending P-ii/S.22" (§1 Part B close) |
| 5F ray-cancellation P1-P6 under H3+(H3-w) | CONVERGED at the algebraic grade (independent transcription closed the common-mode hole); committed-carrier duty NAMED (license gate, §5 C6); Defect 12 REPAIRED (conditional = D2.5/[C-D25U] via N6 §4-§5); Defect 8 REPAIRED (a_Γ in ledger) |
| Escape list E1-E11 | CONVERGED in structure and groups; E1 coefficient and E5 notation repaired (Defects 7a, 11); Defect 10 REPAIRED (advective/div-form bridge stated in §1 note ii); E5 magnitude DISPUTED-OPEN: decided by measured standoff modulation Δx_s on the first dataset |

### VAR lens (refuter: 0 critical / 2 major / 9 minor + 2 obs)
| Item | Status |
|---|---|
| Five-field adjoint core: (A,B,M), transpose, advective rows, (★), wall BC, exit datum, Green row, parity, sliver/Hadamard chain, free-vortex collapse | CONVERGED (full independent hand transpose + machine re-run with firing rejector) |
| Sonic-exit datum blow-up (cl. 14, R-4) | REFUTED-AND-REPLACED (var-D1 MAJOR; judge re-executed the algebra): ψ₅(u²−c²) = 0 with exact-zero RHS; gauge non-uniqueness along l(n); compatibility by the N6-1(c) kernel law; hazard re-typed to 0/0 solve conditioning; exit-margin meter retained (§4) |
| Anti-spike asymmetry "reproduced in-gradient, VERIFIED no flag" (cl. 25, §7.2) | REPAIRED-BY-DOWNGRADE (var-D2 MAJOR): duality-realizability step unproven (radial equilibrium makes per-tube fixed-p_e migration generically unrealizable; δv_e = 0 unsurfaced); relabeled SCALING-ESTIMATE (sign) + record consistency; deciding instrument named (§4) |
| (G) sign; D.5(ii) hypotheses; multiplier dictionary; pencil convention; family-gap ratio; nullity label; Hessian nondegeneracy; free-boundary row; N1 vs axis-BC wording | ALL REPAIRED (D3-D11 as itemized: minus sign restored; u > 0 + AUD-c2T carried; dictionary pinned to D.1's conservation row; r⁵ρ³ in own convention; ⟨1 − (r_spike/r_bell)²⟩; PROVEN-IN-RECORD via D.6 THEOREM*; hypothesis surfaced; ledger row added; regularity-constraint wording) |
| R-3 amplification; K_h0-at-4F wording | REPAIRED per D12 (closed-loop exponent smaller; envelope declared) and D13 (§5 C4) |
| Mixing direction result (a-1): frozen 5F understates Isp, plug family unambiguous | CONVERGED (Gibbs two-liner checked under its stated hypotheses); bell-family NET direction DISPUTED-OPEN: decided by a RANS/LES twin at matched contract data |
| Lip/corner assembly; contact-crossing adjoint calculus | OPEN of record (owners named, §4) |

### FUN lens (refuter: 0 critical / 2 major / 5 minor)
| Item | Status |
|---|---|
| Prop. 1 exact half + μ-emergence + type-check + S-dependence remark | CONVERGED (re-derived end-to-end); DEF-3 REPAIRED (total SIGNED integral zero, not total mass); DEF-6 REPAIRED ((ER) S-scope; surface-source bookkeeping; R1.2 restricted to no-wall wedges, distributional reading at fronts) |
| Single-substitution census; (ER); contract term (II) | CONVERGED |
| First-order identification with the record corrector | REPAIRED (fun-DEF-1 + DEF-2, both MAJOR): normalization pinned J₁^K = St·J₁^ledger (T3QS's J₁ = J₁^K); the third commitment K(V_3D) → K(W_A) = O(St²) DECLARED; dictionary D ≡ div-form K itself EXACT (verified thrice) |
| Error magnitude: bound structure + six reasons C not small | CONVERGED; DEF-4 REPAIRED: 3-6% re-anchored to the literature/EAP corpus (D.10's measured content is σ/μ ≈ 0.70; A4 never computed — G-e); PLUS the panel's normalization flag: A4 will read ≈ 0.3-2.5% at concordant numbers (§5 C1) |
| Prop. 3.2 mean-zero/covariance + ray recovery | CONVERGED — and STRENGTHENED: K̄ = 0 UNCONDITIONAL (DEF-5 repaired; continuity needed only for J₁ = −Cov); (J)/(H) convention pinned (a.c.-only/ψ̄-pairing) before O5-lite measures the split |
| Honest conclusion + O5-lite protocol (A)-(E) | CONVERGED ((C) genuinely licensed by Prop. 1) |
| 2-ε lemma + sharpness + variants; uniformity | CONVERGED; DEF-7 REPAIRED (class-wide H-A1 added to the uniformization list); (U) itself OPEN twice over — decided by the shock-free-sub-scope theorem (F2 target) + measured ε (O5-lite) |
| Flags F-1..F-5 | CONVERGED (F-1 extended to M0:377; F-5 strengthened — committed by the deriver itself, now repaired); F-2 mint recommendation STANDS |

### Cross-lens items
| Item | Status |
|---|---|
| χ = ΩΓ/h0 value (pde vs asy) | REPAIRED by judge adjudication (§5 C1): 0.06-0.20; program-frame normalization FLAG raised |
| D.18 iff labels (three lenses vs asy refuter) | REPAIRED, judge-verified at source (§5 C2): SCHEMA |
| 5F protection license (var F2 vs asy §4) | CONVERGED at two levels (§5 C6): math proven in-panel; repo license gated on the committed carrier |
| B2 variant ↔ h0-convention (asy defect 3 ↔ var ledger (i)) | CONVERGED (one question, two lenses): pinned as a D.13 contract fact with the D.20 linkage as its rejector |

NOTHING DROPPED: all 4+13+8+13+7 = 45 refuter defect items are disposed
above (majors individually; minors itemized within their rows).

==============================================================================
## §7 CARRY-FORWARD LIST (duties this report creates for the next stage)

1. F-2 MINT: number the sector-decomposition identity (Prop. 1 + R1.1 +
   R1.2) in the R4 window.
2. COMMITTED CARRIER: X-T3QS five-field extension (P1-P6 + H3-w + RH rows
   + corrupted-source rejector) — unlocks the smooth-cycle protection
   license on swirl families.
3. ENGINE WIRING: swirl row into the O3.1 dot-product oracle + R1-class
   corruption rejector; sonic-exit quotient solve (mod l(n)).
4. CONTRACT PINS at first ingestion: h0 convention (fold/drop variant);
   tangential-energy-fraction NORMALIZATION (A4 vs literature 3-6% trap);
   per-field a_q (esp. a_Γ, a_h0, a_w); [H-sgn].
5. OPEN THEOREM TARGETS: S.22 bound on the shock-free sub-scope + (U)
   uniformization (with class-wide H-A1); lip/corner assembly; contact
   adjoint calculus; global C3 foliation.
6. MEASUREMENT PROGRAM: O5-lite (A)-(E) with the (J)/(H) convention
   pinned; two-station A4 decay (mixing); phase-resolved two-station
   Γ(ψ) (in-duct pumping); Δx_s standoff modulation (E5).
7. G2 template: "gain net of 2ε, ε = <measured/assumed>".

END OF FINAL FUSED REPORT.

==============================================================================
## §8 POST-JUDGE VERIFICATION ROUND (appended 2026-08-19; edits applied)

A separate adversarial verifier (sympy-backed; full work in
swirl5f_judgeverify.md + swirl5f_jv_check.py, this folder) re-executed
every judge-original (JV) step with algebra committed BEFORE reading the
judge's version. VERDICT: **CONVERGED-WITH-THREE-NAMED-EDITS** — no
structural conclusion moves; no further panel round needed.

CONFIRMED (own algebra): C1 KE-vs-h0 diagnosis via the exact EOS-free
identity χ = (2f_θ/ε_θ)·(KE/h0); the closure χβ_τ = β_w (STRONGER than
printed: exact at definition level, no γ identity needed); the repaired
torque/work order a_p·St_n·β_w; the A4 unit-mismatch flag (ε_θχ/2 ≈
0.45-2%); the full sonic-exit resolution (det = ρ³u³(u²−c²), exact-zero
Cramer numerator, kernel = dictionary-mapped l(e_x), N6-1(c) verified at
source); the D(W) ≡ div-form K dictionary row-for-row; the
J₁^K = St·J₁^ledger chain (with the S_sweep := K/St pin footnote); the
UNCONDITIONAL K̄ = 0 strengthening; the §5-ter loci identification
(checked at phaseD source lines 1542-1561) and extent bracket; spot-checked
MAJOR repairs asy-D2, var-D2, pde-D2, asy-D7 all CORRECT.

REFUTED-AND-REPAIRED IN THIS FILE (the three edits, applied above):
 R-A spike-core band 0.10-0.19 → 0.065-0.14 (= √(ε_θχ/2) at the judge's
     own χ; three sites: §2 H-ANN, §5 C1, §6 pde table).
 R-B B2 drop-variant: formula exact only at δ = δ_int; the unconditional
     "|bias| ≤ fold" clause FALSE beyond r_exit = √2·r_in — replaced by
     "|bias| ≤ δ_int²/2; ≤ fold iff r_exit ≤ √2·r_in" (§1 B2).
 R-C §6 asy-table typo Λ = 0.06-1.11·St_n → 0.59-1.11·St_n.

Verifier weight: 1 agent, ~236k tokens, 19 tool uses. Total panel weight
incl. verification: 10 agents, ~2.0M subagent tokens.
