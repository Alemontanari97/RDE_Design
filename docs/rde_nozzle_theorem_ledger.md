# Theorem ledger: formal statements, verified proofs, counterexamples, open problems (D3)

Status: DELIVERABLE D3 of the 2026-07-16 formalization/survey session.
Every item carries a CLASS tag:

  THEOREM      — statement + proof verified line-by-line in this session;
  THEOREM*     — proof verified within a declared model closure (the
                 closure itself is a modeling assumption, not mathematics);
  SCHEMA       — correct formal structure, rigor gap named and isolated;
  CONJECTURE   — precise statement, no proof, falsifiable criterion given;
  HEURISTIC    — organizing idea, not yet a precise statement;
  WEAKENED     — the internal notes' version was too strong; corrected here.

Cross-references: PB-n and ledger rows from `docs/rde_nozzle_problem_book.md`
(D1); literature verdicts from `docs/rde_nozzle_literature_map.md` (D2);
survival verdicts on the internal notes in `docs/rde_nozzle_claims_verdict.md`
(D4). Notation as in D1 §1.

------------------------------------------------------------------------------
## 1. Elementary pillars (verified)

### O1 — Objective equivalence at frozen, choked feed. THEOREM.
Hypotheses: (i) frozen family (H-F1): the cycle {Pc(t), c*(t)}, t_c, and
A_t do not depend on the divergent shape Σ; (ii) H2: ṁ(t) = Pc(t)A_t/c*(t).
Claim: Isp_cycle[Σ] and J[Σ] = (1/t_c)∫F dt have the same maximizers, and
the Isp numerator equals ∫F dt exactly.
Proof. ṁ c* = Pc A_t for any c*-law, so ∫ṁ CF c* dt = ∫Pc A_t·F/(Pc A_t) dt
= ∫F dt; the denominator g0∫ṁ dt is Σ-independent by (i)+(ii). QED.
Verified: the algebra is the same "pivot" as bell_optimality_proof.md step 2;
checked independently.
Failure channels: bilevel coupling (PB-4) breaks (i); unchoked tail breaks
(ii). Under coupling, thrust-max and Isp-max are DIFFERENT problems.
Falsifier: recompute both objectives under the matched-cycle response map;
divergence of the two argmax is the measure of coupling strength.

### O2 — Log-uniform operating measure. THEOREM (one line).
For Pc(ξ) = P_CJ·PR^(−ξ), ξ ~ U[0,1]: ξ = −ln(Pc/P_CJ)/ln PR gives
dμ_P = dPc/(Pc ln PR) on [P_CJ/PR, P_CJ]. QED. (Blowdown exponential is
S-H Eqs. 13-14; any other measured cycle just replaces μ_P.)

------------------------------------------------------------------------------
## 2. T0 — wave-frame exactness. THEOREM, and STRENGTHENED.

Hypotheses: (a) rotating-pattern flow q(x,r,θ,t) = q̃(x,r,θ−Ω_w t) (fields
piecewise smooth, discontinuities transversal, cylindrical components);
(b) S a fixed axisymmetric surface; (c) Pa constant.

Claim (strengthened vs the internal note, which stated only the mean):
 (i)  F_S(t) = ∫_S [ρu_x(u·n) + (p−Pa)n_x] dA is CONSTANT in time, hence
      trivially equal to its cycle mean. The single-mode RDE has steady
      thrust through every axisymmetric surface — the unsteadiness of the
      thrust is entirely a multi-mode/modulation diagnostic.
 (ii) F_S equals the same integral evaluated with the wave-frame steady
      fields and relative velocity w: with Ω_w ∥ e_x, w_x = u_x and, on
      axisymmetric S (n_θ = 0), w·n = u·n since (Ω_w e_x × x)·n = Ω_w r e_θ·n
      = 0. The lab and rotating expressions are the SAME integrand.
 (iii) The steady control-volume balance in the rotating frame closes with
      no frame-force contribution to the axial component: e_x·(−2Ω_w e_x×w)
      = 0 (Coriolis ⊥ axis), centrifugal Ω_w²r e_r ⊥ axis. Hence the
      wave-frame steady wall-pressure integral reproduces the lab thrust.

Proof of (i) (verified). At fixed (x,r), the integrand is g(θ−Ω_w t); for
an axisymmetric S the θ-integral of g(θ−Ω_w t) over [0,2π) is invariant
under the shift Ω_w t. So each annular strip of S contributes a
t-independent amount. QED. (ii),(iii): computations above, checked. QED.

Scope and honest limits (unchanged): H-A1 single steady mode; mode-hop,
counter-rotating pairs, longitudinal pulsation break (a). WEAKENED claim
imported from the internal note: T0 makes J a steady 3-D functional; it
does NOT make Rao's closed-form machinery applicable "verbatim" — that
machinery is 2-D; the 3-D swirling variational/adjoint theory is open (N6,
gap b4-C1: nearest precedents are spiral-wave response functions
[Biktasheva et al., PRE 79:056702 (2009)] and the freezing formulation
[Beyn-Thümmler, SIADS 3:85 (2004)], neither of which does shape design).

Executable check: any URANS single-mode run — the axial-thrust time trace
through any axisymmetric plane must be constant to the pattern-rotation
tolerance; deviation measures mode impurity (cheap diagnostic, new).

------------------------------------------------------------------------------
## 3. T1 — factorization. DEFINITION + CONJECTURE (demoted from "Theorem").

The internal note labels T1 a theorem; it is honestly a DEFINITION of the
rung-2 model plus a CONVERGENCE CONJECTURE:

Definition (rung-2 objective): J_avg[Σ] = ∫_Ξ F[Σ; s(ξ)]dμ(ξ) with
per-phase steady meridional problems (D1 §4.4, interface I2/I3).

Conjecture C-T1 (the O(St) bridge = P4). Under s ∈ C^k in ξ, per-phase
S1-regularity uniform in ξ, and St_n → 0:
    J_exact = J_avg + St·J_1 + O(St²),
with J_1 a cell-problem corrector expressible through per-phase linearized
nozzle transfer functions (Marble-Candel class) driven by the cycle's
pressure/entropy wave content. STATUS: open; the rigorous frame is
two-scale limits for quasilinear hyperbolic boundary data — the
literature has the linearized building blocks (D2 §b6) but no theorem of
this form (gap b6-C1/C2, pending final b6 verdict).

Sharpened parameter structure (correction, D1 §8): D1(quasi-steady) and
D2(azimuthal decoupling) are NOT independent; the sweep term −Ω_w r ∂_θ′
is the O(St_n) term, and the residual lab-frame drift u_θτ_n/r is
generically smaller. One parameter (St_n) governs the bridge at leading
order; D2 survives as a subdominant profile-mixing condition.

Falsifier (oracle O5): direct unsteady quasi-1D/2-D simulation of a
designed nozzle under the blowdown vs J_avg + St·J_1.

------------------------------------------------------------------------------
## 4. T2 — averaged stationarity system. SCHEMA, with one CORRECTION.

Setting: maximize J_avg over Σ ∈ A (restricted spline/C^{1,1} class),
per-phase constraints: steady Euler E(U_ξ, Σ) = 0 (adjoint ψ_ξ per phase),
per-phase mass flow fixed by the choked inlet (multiplier λ₂(ξ) in the
control-surface formulation ONLY — in the wall formulation the mass
constraint is intrinsic to PDE+BC and no λ₂ appears; the two formulations
are equivalent where both are defined), shared geometric constraints
(multipliers λ_L, ...).

Claim (structure of stationarity; verified at the formal level):
 (a) per a.e. ξ: the per-phase adjoint Euler system; in the S1 class it
     reduces to the classical conditions on that phase's terminal
     characteristic (control surface = characteristic; first integral
     f₂ = V cos(θ∓α)/cos α = −λ₂(ξ) phase-by-phase).
 (b) shared wall: ∫_Ξ G_ξ(x) dμ(ξ) + λ_L g_L(x) = 0 for a.e. x ∈ Σ, with
     G_ξ the phase-ξ Hadamard density. The genuinely new object: no phase
     satisfies its own wall condition; the μ-average does.
 (c) shared endpoint (lip/corner): CORRECTED STATEMENT. The internal
     note's (**) ∫R(ξ)dμ = 0 (unweighted average of Rao's Eq.-14 residual)
     implicitly assumes the endpoint-sensitivity WEIGHT is phase-
     independent. The safe general form is

         ∫_Ξ (∂F/∂s_E)[Σ; s(ξ)] dμ(ξ) = 0,      (**')

     i.e. the μ-average of the FULL one-sided endpoint derivative, which
     factorizes as R(ξ)·w(ξ) with w(ξ) > 0 a geometric-kinematic weight.
     w is phase-independent exactly in the T3 similarity class (where
     M_E, θ_E, α_E are phase-invariant) — there (**) and (**') coincide,
     and remark (R2) of the internal note survives verbatim. Outside that
     class, (**) is an unjustified simplification: USE (**').
     [Same correction applies to the plug corner condition with p_b.]

Non-smoothness: phases where the flow topology switches contribute a
measure-zero set in ξ across which F(Σ,·) is continuous; Leibniz applies
even though the switch location moves with Σ (the boundary terms cancel
by continuity of F — verified). Persistent kinks: Clarke subdifferential
version of (b)-(c).

Rigor gaps, named (this is why SCHEMA): (1) existence/regularity of
λ₂(·) ∈ L²(dμ) — measurable selection + phase-wise constraint
qualification (P3, open); (2) shape-differentiability of ξ ↦ F[Σ; s(ξ)]
uniform in ξ in the S1 class — the multi-D shift-differentiability gap
(D2 §b3 C1: rigorous only in 1-D [Bressan-Marson 1995; Ulbrich SICON 41:740
(2002)]; quasi-1D design-with-shock rigor exists [Cliff-Heinkenschloss-
Shenoy, JOTA 94:273 (1997)]; 2-D is practice-without-theorem
[Baeza-Castro-Palacios-Zuazua, AIAA J 47:552 (2009)]).

Reduction check (executable, verified in-repo): quasi-1D with only the
exit-area DOF: (b)-(c) degenerate to ⟨p_e(ξ)⟩ = Pa, i.e. NPR(ε*) = ⟨Pc⟩/Pa
— exactly Theorem 1 of `validation/bell_optimality_proof.md` (test
`tests/test_bell_optimality.py`, incl. the T1c wrong-averaging rejector).

------------------------------------------------------------------------------
## 5. T3 — the collapse (fixed wall). THEOREM. Verified, and sharpened.

### 5.1 Statement and verified proof

Hypotheses H-T3.1-4 (D1 ledger): one frozen γ for all phases; fixed wall,
full-flowing, supersonic exit at every phase (ambient-blind interior);
phase-independent nondimensional inflow shape, phases differ only through
(P0(ξ), T0(ξ)); per-phase solutions unique in their class; Pa constant.

Claim: J_avg[Σ] = F[Σ; ⟨Pc⟩_μ] POINTWISE on shape space (equality of
functions, not merely of maximizers), ⟨Pc⟩_μ = ∫Pc dμ. Hence the
cycle-optimal fixed wall is the classical contour designed at the
μ-mean chamber pressure, under identical constraints.

Proof (re-verified line-by-line this session).
Lemma A (pressure-scaling similarity). At fixed Σ, T0: if (u, T, p, ρ)
solves the steady problem with stagnation (P0, T0), then (u, T, κp, κρ)
solves it with (κP0, T0). Verified for smooth regions (grad p/ρ invariant;
continuity/energy untouched; EOS preserved; entropy shifts by −R ln κ so
isentropes map to isentropes) — AND, sharpening the internal note, ACROSS
TRANSVERSAL SHOCKS: the Rankine-Hugoniot fluxes are homogeneous of degree
one in (ρ, ρu, ρE) at fixed (u, T) (mass κ, momentum κ, energy κ since
ρe = ρe(T)·κ), and the entropy-jump condition is κ-invariant (jump of s
unchanged by the common shift). Lax/Majda transversality is κ-free. So
Lemma A holds in the full S1 class WITH shocks, and also for thermally
perfect γ(T) (e = e(T) arbitrary). Consequence: M(x), θ(x), T(x) phase-
independent; p_ξ(x) = Pc(ξ)·Π(x;Σ) for one fixed field Π.
Lemma B (T0-similarity; REQUIRES calorically perfect gas). At fixed P0,
T0 → T0′ rescales u by √(T0′/T0), leaves (M, θ, p, T/T0) invariant; CF is
T0-blind. Dies for γ(T) (no similarity variable in T). Verified.
Lemma C (affinity). F[Σ; s(ξ)] = a[Σ]·Pc(ξ) − Pa·b[Σ], a from the Π-field
wall integral + throat momentum coefficient, b = projected wall area.
Verified: both integrals scale as stated.
Assembly. ∫(a Pc(ξ) − Pa b)dμ = a⟨Pc⟩ − Pa b = F[Σ; ⟨Pc⟩]. QED.

Remarks (R1) (per-phase optima move, the average of the affine family is
again a member) and (R2) (the averaged corner condition collapses to the
single-phase corner at ⟨Pc⟩) — both re-verified; (R2) additionally
justified now because the endpoint weight w(ξ) of §4(c) is phase-
independent in this class, so (**) = (**') here.

Corollaries (verified): (1) repo Theorem 1 is the rank-1 shadow;
(2) Pa enters F linearly too ⇒ the same collapse for trajectory-averaged
fixed-bell design at ⟨Pa⟩ — the RDE cycle average and the classical
altitude average are one mathematics with the measure moved from Pa to
Pc; the dual-bell literature exists precisely because SEPARATION breaks
the linearity (D2 §b5: the altitude-collapse statement is engineering
folklore, never published as a theorem — gap b5-C2);
(3) the null-result oracle O1: frozen-γ full-flowing ensemble machinery
MUST return Rao-at-⟨Pc⟩ with ΔIsp = 0, else it is broken.

### 5.2 Sharpness. The γ-channel counterexample. THEOREM (in principle) +
###     measured magnitude DOWNGRADED to UNVERIFIED-IN-REPO.

Minimal counterexample (executable, quasi-1D): a two-phase cycle, phases
(Pc₁, γ₁), (Pc₂, γ₂), γ₁ ≠ γ₂ frozen per phase. Then F_ξ = a(γ_ξ)Pc_ξ −
Pa b and J = ½[a(γ₁)Pc₁ + a(γ₂)Pc₂] − Pa b, which is NOT of the form
a(γ)⟨Pc⟩ − Pa b for any single γ evaluable independently of the measure:
the collapse fails in principle; first-order closure γ_eff =
⟨Pc γ⟩/⟨Pc⟩ (pressure-weighted). This retro-identifies S-H "freeze γ AT
CJ" as the correct first-order closure, since the Pc-weighting
concentrates on early phases. VERIFIED as mathematics.
MEASURED IN-REPO (2026-07-16, A0.3 closed: examples/gamma_cycle_probe.py
+ tests/test_gamma_probe.py + data/gamma_cycle_probe.json, on the blessed
det|CH4|20|1.64 state, equilibrium SP family anchored at CJ):
γ_s = 1.1537 (ξ=0, T0 = 3727 K) → 1.2093 (ξ=1, T0 = 2228 K), with a
single shallow interior minimum at ξ ≈ 0.1 (depth 4e-4); frozen-
composition γ_tp = 1.2223 → 1.2286. The stale note numbers are hereby
CORRECTED: "γ_s → 1.210" confirmed to its own rounding (1.209);
"ε* shift −1.9%" is STRUCK — the measured shift of the bell optimum is
−0.56% (ε* 3.980 → 3.958), and the γ_eff = ⟨Pc γ⟩/⟨Pc⟩ closure
(γ_eff = 1.1577) reproduces it to −0.57%, its first executable
confirmation; the UNWEIGHTED mean γ gives −2.39% — the wrong-averaging
class the stale −1.9% most plausibly came from, now rejected by test.
"Isp penalty −0.001%" corrected in magnitude: measured −0.00028%
(second-order, envelope theorem: penalty 2.8e-6 ≤ shift² = 3.1e-5 —
the structure itself is now a test gate). Per-phase CF deviation from
the frozen closure at ε*_fr: < 0.3% over the thrust-dominant early
half-cycle, ~1.3% at ξ = 0.75, formally unbounded only across the
late-cycle zero-crossing of the overexpanded frozen CF (Pc-weighted
mean 0.36%).
Classical support for the channel's structure (in-house corpus, D2 §b0):
Hoffman 1967 p.676 PROVES that for genuinely reacting (finite-rate) gas
the algebraic corner bijection is no longer sufficient — the optimality
condition becomes E = 0 on the multiplier fields (Eq. 78). Hence the N4
ladder is: frozen γ (T3 exact) ⊂ γ(T) frozen-composition (collapse fails
in principle, γ_eff closure, E4 validation risk open — only known-answer
oracle: Scofield-Hoffman 1971 Table 2, frozen thrust 2290 lbf) ⊂
finite-rate (closed-form corner DEAD, adjoint-level formulation
mandatory). Scofield-Hoffman's freeze-at-throat design recommendation is
the classical twin of the γ_eff-at-CJ closure.

------------------------------------------------------------------------------
## 6. T4 — plug simultaneous optimizability. THEOREM* (under closure).

Closure H-T4 (ideal adaptation): downstream of phase ξ's full-expansion
point the wall pressure is clamped to Pa (zero incremental thrust);
upstream, T3-class scaling. Under H-T4: per phase, F[Σ_l; s(ξ)] is
nondecreasing in plug extension l, exactly constant for l ≥ l(ξ), l(ξ)
increasing in Pc(ξ). The per-phase argmax sets are nested half-lines
[l(ξ), ∞); their intersection is attained by the PEAK-phase design:
max_Σ ∫F dμ = ∫ max_Σ F dμ, maximizer = plug designed at NPR = P_CJ/Pa
(capped by ε_max where binding). Verified (monotone + nested-argmax
argument is elementary and correct; repo Theorem 2 is its 1-DOF shadow).
Sharpness: length cap L < l(ξ_peak), base-pressure model at a truncation
plane, or non-ideal adaptation break the nesting; then max∫ < ∫max
STRICTLY and the optimum satisfies §4(a)-(c) with the plug corner
condition (GENO `Rao_m.f90:762-764`) replaced by its μ-averaged (**')
form. THE TRUNCATED PLUG IS THE FIRST GENUINELY AVERAGED SHAPE PROBLEM
(PB-2). Caveat, declared: H-T4 is an engineering closure — the theorem's
physical content is only as good as ideal adaptation, and the OFF-DESIGN
plug march (WP1c-i) is what replaces it with computed truth.

------------------------------------------------------------------------------
## 7. P1 — sensitivity at a spinning wave. SCHEMA, WEAKENED (corrected).

Freezing formulation (Beyn-Thümmler): 0 = −Ω_w ∂U/∂θ′ + L(U;Σ) + phase
condition; unknowns (U, Ω_w). Target: Fréchet differentiability of
Σ ↦ (U, Ω_w) and a Hadamard representation of dJ with an adjoint phase
variable dual to Ω_w, under (i) piecewise-smooth wave with transversal
fronts satisfying Majda's uniform stability, (ii) linearization (with
front-displacement unknowns) FREDHOLM AND INVERTIBLE after removing the
group zero mode by the phase condition.

CORRECTION of the internal note's "design sensitivity well-posed ⟺ mode
spectrally robust": the implicit-function theorem needs ONLY hypothesis
(ii) — no eigenvalue AT ZERO beyond the group mode. Spectral STABILITY
(no spectrum in the right half-plane) is neither necessary (an unstable
relative equilibrium has perfectly well-defined shape sensitivity as a
stationary solution) nor sufficient for physical relevance by itself.
The defensible statements are:
 (P1a) sensitivity degenerates exactly at NEUTRAL modes — i.e. at
       bifurcation/mode-boundary points of the operating map; there
       dΩ_w/dΣ and dJ/dΣ blow up or become one-sided; and
 (P1b) the operator whose spectrum decides (P1a) IS the multi-D
       detonation stability operator of the annulus (Evans-function
       object), so the optimizer's Jacobian and the operability analysis
       are one object studied twice — with the PHYSICAL license of the
       gradient (J as attractor statistic) additionally requiring
       stability of the wave.
Survey verdict feeding this item (D2 §b4): no published shape-design
adjoint of a rotating relative equilibrium with unknown Ω was found
(b4-C1 NOT FOUND; strong methodological precedents: spiral-wave response
functions = adjoint eigenfunctions at λ = 0, ±iω used for drift, not
design; freezing method; HB adjoints with IMPOSED frequency). The
"sensitivity=stability" framing was NOT FOUND as an explicit theorem
(b4-C3) — it is a legitimate novelty target in the corrected form
(P1a)+(P1b).
Falsifier (oracle O4): dΩ_w/dΣ from the freezing adjoint vs finite
differences of continued relative equilibria on the 2-D unrolled-annulus
model (WP5a).

------------------------------------------------------------------------------
## 8. P2 — "Rao = closed-form adjoint". PARTLY KNOWN + SCHEMA.

Corrected status after survey (D2 §b3, §b0): THREE banks of the bridge
are published, none crossing it. (1) Classical side, in-house corpus:
HOFFMAN 1967 (AIAA J 5(4):670) already formulates the reacting-flow
optimality system as Lagrange-multiplier FIELDS λ₁..λ₅ satisfying PDEs
along the SAME characteristics as the flow — a continuous adjoint avant
la lettre, with the a-posteriori optimality residual E (Eq. 78) as the
ancestor of the Level-C certificate; the homentropic-irrotational
specialization degenerates the fields to constants and recovers
f₂ = const. (2) Quasi-1D modern side: Giles-Pierce JFM 426:327 (2001),
analytic adjoints incl. shock interior condition and sonic-throat log
singularity. (3) 2-D modern side: Lozano-Ponsin, Aerospace 12(6):494
(2025), analytic supersonic adjoints with characteristic structure — no
mention of Rao/Guderley/Kraiko/Hoffman. What remains genuinely unwritten:
the EXPLICIT identification (Rao/Kraiko conditions ≡ closed-form adjoint;
multipliers ≡ adjoint boundary data) and the statement reverse-mode AD of
a shock-fitted MOC march ≡ discrete adjoint characteristic sweep. SCHEMA
with high confidence; publish as a bridge lemma citing all three banks.
Falsifier (oracle O3): dot-product identities of the differentiable-MOC
march at machine precision, then term-by-term match with Rao's conditions
on one TOC case — plus Hoffman's E-residual computed along a
GENO-optimized contour (must vanish).

------------------------------------------------------------------------------
## 9. P3-P7 — status after this session

P3 (averaged multiplier existence, λ₂ ∈ L²(dμ), system (a)-(c) with
   (**')): OPEN; route: phase-wise Zowe-Kurcyusz constraint qualification
   + measurable selection; no blocking obstruction identified. SCHEMA.
P4 (O(St) expansion with transfer-function corrector): OPEN; see C-T1.
   The b6 survey (pending completion) has so far found the linear
   building blocks only. CONJECTURE with falsifier O5.
P5 (symmetry trichotomy, perturbative δ ≠ 0): SCHEMA; Floquet
   non-degeneracy hypothesis; machinery exists (HB adjoints, D2 §b4);
   the RDE application is new (b4-C2 NOT FOUND).
P6 (quantitative stability of the collapse): SCHEMA; the natural route is
   the envelope theorem around the T3 point + explicit violation
   measures (separation measure of the cycle, inlet-profile amplitude,
   γ excursion); its "first measured instance" is now IN-REPO (§5.2:
   ε* shift −0.56%, penalty −0.00028% ≤ shift², γ_eff closure confirmed
   — examples/gamma_cycle_probe.py, tests/test_gamma_probe.py).
P7 (existence in uniform C^{1,α} ∩ uniform-MOC-regular classes): SCHEMA;
   compactness (Chenais-type, verified available in D2 §b5) + continuity
   of Σ ↦ U_ξ in the S1 class uniform in ξ + dominated convergence; the
   declared failure boundary is loss of S1-regularity along a maximizing
   sequence. The survey (b5-C3) confirms NO existing theorem covers an
   integral over a μ-family of hyperbolic states sharing one boundary —
   P7 would be new even in restricted classes. CLASSICAL ANCHOR (in-house
   corpus, D2 §b0): the valid/invalid-region boundary of Sternin 1962
   (closed form in Rao-Beck 1994 Eq. 4) is the single-phase ancestor of
   P7's failure boundary, and is ALREADY IMPLEMENTED, γ-free, as
   `boundaryfunction_solve` (GENO Rao_m.f90:30-56): the per-phase
   S1-regularity monitor exists in code; the μ-uniform version (inf over
   ξ of the boundary-function margin) is the P7 monitor.

------------------------------------------------------------------------------
## 10. New items produced by this session's verification

N-T0′ (instantaneous thrust constancy) — THEOREM, §2(i): free diagnostic
   (thrust-trace flatness = mode purity monitor).
N-D1D2 (parameter collapse D1 ⊃ D2) — THEOREM-level observation, D1 §8:
   one Strouhal governs the bridge; simplifies the ledger and P4.
N-(**′) (weighted transversality) — CORRECTION, §4(c): removes a latent
   wrong-equation risk in every future implementation of the averaged
   corner condition (WP2/WP3 must implement (**'), not (**)).
N-O1± (objective split under coupling) — WARNING, §1: thrust-vs-Isp
   equivalence dies with chamber coupling; PB-4 must pick its objective.
N-SW (swirl audit, second pass) — LEMMA + CORRECTION, D1 §4.3bis: an
   axial plane is spacelike iff u_x > c, FRAME-INVARIANTLY (the sweep
   tilts the Mach cone azimuthally but w_x = u_x): the relative Mach
   |w|/c governs only the operator TYPE, never axial data prescription.
   Corollary of substance: the relative sonic locus at the wave IS the
   CJ surface — the wave-frame causal firewall grounding H-F1, with
   chamber-nozzle coupling confined to the unshielded sectors (fill,
   deflagration, oblique shock). Rung-3a must be an implicit BVP (no
   marching); the huge wave-frame swirl never enters rung 2 — it IS the
   O(St) sweep term.

------------------------------------------------------------------------------
## 10bis. Method upgrades from the adversarial self-review (2026-07-16,
##        second pass — "is this the best the SOTA allows?")

U1 (BOUND LADDER — new pillar). Alongside lower bounds (computed optima),
   report RIGOROUS UPPER BOUNDS by relaxation at every stage:
   (i) shared-wall relaxation: max_Σ ∫F dμ ≤ ∫ max_Σ F dμ — the right side
   is pure per-phase Rao/Kraiko, cheap and exact in S1; (ii) ideal-
   adaptation bounds (Efremov-Kraiko 2004 integral-flux bound;
   Kraiko-Egoryan instantaneously-adapted limit; Paxson's notional-ideal).
   The RELAXATION GAP bounds the value of each collapse-breaking channel
   BEFORE its machinery is built, and turns the roadmap's G2 value gate
   into a theorem-grade kill criterion: gap < threshold ⇒ channel closed
   by bound, not by failed experiment. STATUS: elementary consequences of
   T2-T4 structure; assemble as Proposition B1 (bound chain) — LOW effort,
   HIGH governance value.
U2 (P4 AS Γ-CONVERGENCE). The O(St) bridge as stated controls VALUES, not
   MAXIMIZERS. Upgrade the target: on the compact admissible class A of
   P7, prove epi/Γ-convergence J_St → J_avg (with equi-coercivity from
   the class bounds), which transfers convergence of argmax and design
   stability. This is the correct variational phrasing of the
   quasi-steady license; the expansion of §3 becomes its quantitative
   corollary. STATUS: new target P4', strictly stronger than P4.
U3 (DWR ERROR CONTROL in Level C). Add goal-oriented dual-weighted-
   residual estimates (Becker-Rannacher) on J: the per-phase adjoints are
   already available, so the DISCRETIZATION error bar on the certificate
   is nearly free. Every Verdict then carries: physical bar (St·J₁) +
   numerical bar (DWR) + stationarity residual + oracle record.
U4 (COMPUTER-ASSISTED EXISTENCE, optional). On the 2-D unrolled-annulus
   reduced model, discharge P1's existence/spectrum hypothesis by
   rigorous-numerics (computer-assisted proof for the rotating wave):
   upgrades P1 from conditional schema to unconditional theorem on the
   reduced model. Mature technology for traveling waves/periodic orbits.
U5 (S1 BEYOND MOC: implicit shock tracking). The method's commitment is
   to the SOLUTION CLASS S1 (fitted fronts, piecewise-smooth state), not
   to the characteristic-marching algorithm. MOC is S1's optimal
   algorithm in steady 2-D supersonic flow (its reverse sweep = the
   closed-form adjoint, P2). Where the regime exceeds MOC — the 3-D
   wave-frame problem, mixed-type regions with subsonic pockets — the
   same philosophy continues as HIGH-ORDER IMPLICIT SHOCK TRACKING /
   shock-fitted FEM (Zahr-Persson line): front-aligned discretizations
   whose discrete adjoints are consistent BY CONSTRUCTION, avoiding the
   Giles-Ulbrich negative theorem for captured shocks. Rung-3a solves
   (WP5) should use this class, not shock capturing. Rationale of
   record: weak-strong uniqueness (D1 §6) makes S1 canonical — inside
   S1 every admissible solution concept agrees — so tracking the fronts
   is not a numerical taste but the discretization of the only class
   where the optimization chain is theorem-grade.
C1 (CONTINGENCY, documented decision): direct rung-3 3-D rotating-frame/
   HB adjoint as the ENGINE (not anchor) is compute-feasible today
   (turbomachinery routinely runs 3-D HB adjoints); it is deliberately
   NOT the spine because it forfeits the closed-form oracles (no T3/T4
   rejection tests), faces mode discontinuities, and inherits the
   shock-captured adjoint-consistency trap. Gate G4 promotes it if the
   D2-decoupling error dominates — a reversible, instrumented decision.

------------------------------------------------------------------------------
## 10ter. The global-optimality program (the "like Rao, but global" ideal,
##         made precise)

Premise correction: Rao 1958 proved FIRST-ORDER NECESSARY conditions
under strong hypotheses — no existence, no sufficiency, no globality
(the existence region came only with Sternin 1962). The achievable ideal
here is strictly stronger, and "without hypotheses" is excluded by
theorem, not by laziness: (i) without an admissible class no maximizer
exists (vacuum Theorem 3; unbounded length/radius ⇒ sup unattained);
(ii) without a solution concept J is undefined (multi-D non-uniqueness);
(iii) without a measure the averaged objective is undefined. Hypotheses
ARE the definition of the problem; the ledger instruments them.

Target statement (the program's formal-optimality contract): for the
problem defined by (A, S1, μ, ledger):
  EXISTENCE (P7)  +  NECESSARY (T2 with (**'))  +  SECOND-ORDER
  SUFFICIENT (reduced-Hessian)  +  GLOBALITY by one of the five
  mechanisms below — every delivered Σ* states which mechanism applies
  and at what strength.

Global-optimality mechanisms, strongest first, with where they bite:
  M1 DUALITY-GAP ZERO: J(Σ*) attains the bound-ladder upper bound ⇒
     GLOBAL, certified. T4 is already an instance (max∫ = ∫max attained
     ⇒ peak-design plug globally optimal under the closure). Operating
     rule: every Verdict reports the gap; gap = δ > 0 ⇒ "within δ of
     global", certified.
  M2 COLLAPSE TRANSFER: T3 is a POINTWISE equality of functionals ⇒
     globality of the cycle problem ≡ globality of the classical
     problem at ⟨Pc⟩; anything global proved classically is inherited.
  M3 MONOTONE/UNIMODAL STRUCTURE (low-rank DOF): repo Theorems 1-3 are
     already GLOBAL (single sign change / plateau / vacuum). Concrete
     target: unimodality of the truncated-plug duty variable — if it
     holds, PB-2 ships with proven globality, not mere stationarity.
  M4 EXHAUSTIVE STATIONARY-POINT ENUMERATION (finite-dim spline space):
     deflated continuation (B2) enumerates stationary contours; direct
     comparison + bound gap = practical-globality certificate with the
     beaten-competitor list in the Verdict.
  M5 CERTIFIED DETERMINISTIC GLOBAL SEARCH (2-4 DOF): Lipschitz/
     branch-and-bound with rigorous per-region bounds — proven global
     on the discretized problem for {ε, L}, duty-split, truncation
     studies; asymptotic-only for 10-20-DOF splines (declared).

Status: M1/M2/M3 partially THEOREM already (T4, T3, repo 1-DOF); M3-PB2
CONJECTURE with executable check; M4/M5 engineering with certificates.
This section is the precise content of the informal ideal "prove the
solution is THE optimum": global optimality FOR THE DEFINED PROBLEM,
with the definition instrumented — strictly more than the classical
canon ever established.

------------------------------------------------------------------------------
## 10quater. The configuration-free problem and the total-optimum
##            structure ("the measure selects the topology")

Setting: the general admissible set A_gen of D1 §5 (solid set in an
envelope; configurations = topology sectors; total optimum = finite
tournament of sector optima).

Prop. G-B (geometry-free upper bound — THEOREM-grade). For ANY S in ANY
topology, under choked frozen feed: J[S] ≤ J_ideal =
∫ F_id(s(ξ); Pa) dμ(ξ), with F_id the thrust of complete isentropic
per-streamtube expansion of phase ξ to Pa (shocks only lower exit
velocity at given (ṁ, h0, s) per tube; misalignment only loses axial
projection). Weaker published relaxation (integral inlet fluxes,
redistribution allowed): Efremov-Kraiko 2004 — B_EK ≥ J_ideal ≥ J.
J_ideal depends only on (cycle family, Pa): the ceiling of the bound
ladder, independent of shape AND of topology.

SHARPENING OF RECORD (2026-07-16, OP-0 executable ladder:
src/thrust/bounds.py, tests/test_bounds.py, data/bounds_ladder.json).
As stated, F_id (complete isentropic expansion to Pa) is the streamtube
supremum ONLY where the phase clears the critical pressure ratio,
Pc/Pa ≥ ((γ+1)/2)^(γ/(γ−1)). For 1 < Pc/Pa < critical the exit that
matches Pa is SUBSONIC, and moving from the sonic exit toward it along
the subsonic branch loses thrust monotonically (dF/dA_e = Pe − Pa < 0
there; the jet-matching condition Pe = Pa is enforceable only at the
endpoint): the sonic exit strictly beats naive full expansion —
executable counterexample γ = 1.15, Pc/Pa = 1.3, ΔCF = +0.0070. The
correct per-streamtube ceiling is complete expansion CAPPED AT THE
SONIC STATE; with the cap, at ε level, int-max == ceiling exactly
(quasi-1D exhaustiveness; dual-route agreement ≤ NQ·ε_mach in the
ladder), and the naive form is REJECTED by test on the four subcritical
Table-1 rows (choke_margin < 1: CH4/RP-1 at 20 atm, sea level — cycle-
level violation small, 2e-7…7e-3 s, but structural). G-B, the
Efremov–Kraiko comparison and the T4/H-T4 closure (whose S-H spike form
uses the naive branch, hence attains the naive value, NOT the capped
ceiling, on subcritical tails) inherit "min-cycle NPR ≥ critical" as an
explicit hypothesis, or carry the cap.

Cor. G-T4 (global-over-topologies optimality in the generous-envelope
limit). Under the ideal-adaptation closure and unbounded envelope, the
untruncated free-boundary (plug) family ATTAINS J_ideal (T4 + duality-
gap zero, mechanism M1): the peak-designed plug is globally optimal
over ALL topologies, not merely within its sector. This is the precise
sense in which a "total optimum independent of the shape category"
exists: at generous constraints its VALUE is J_ideal and the maximizer
type (free boundary) emerges from the theorem.

Known limits of the phase diagram (each with status):
  - spread(μ) → 0 (single state): sectors TIE at the Rao value (T3
    exactness for the fixed wall; the plug's adaptation earns nothing at
    one point) — simplest/lightest sector wins on secondary criteria.
    THEOREM-level within the S-H idealization.
  - generous envelope, ideal adaptation: free boundary attains J_ideal
    (Cor. G-T4). THEOREM* (closure-conditional).
  - vacuum: no finite optimum in any sector (repo Theorem 3); ε is a
    specification. THEOREM.
  - tight length + large spread: mixed duty-split region (C1) —
    CONJECTURE.

OP-11 (PHASE-DIAGRAM CONJECTURE — the general design question). In the
plane (envelope constraints) × (spread of μ), the maximizer over A_gen
transitions: fixed-wall sector (spread ~ 0) → mixed duty-split →
free-boundary-dominated (generous envelope, large spread), with sector
boundaries = topology transitions of the optimum. The RDE's cycle
measure (log-uniform over a factor ~PR) physically FIXES the point in
this diagram: "which nozzle does an RDE want" = reading a provable map.
Executable now at the ε-level: S-H closed forms for bell/plug(/shrouded
cap) on the Table-1 states trace the quasi-1D phase diagram immediately
(the repo's measured spike-vs-bell 3-12% gaps are points of this map);
contour-level points via the sector tournament with certificates M1-M5.
PB-2 (truncated plug) and PB-3 (duty split) are SECTIONS of this
diagram, not standalone categories — reclassification of record.

OP-11-ε RESULT OF RECORD (2026-07-16, [F1/OP-11-eps]:
src/thrust/phase_diagram.py, tests/test_phase_diagram.py,
data/phase_diagram.{json,md}, figs/phase_diagram_op11.png). The ε-level
instance is now COMPUTED AND CERTIFIED on the blessed CH4/O2 20-atm
anchor: 90 cells (ε_max × PR at fixed ⟨Pc⟩, PR = 1 … 90) + vacuum
sweep, the OP-0 ladder embedded per cell (chain C re-verified cell by
cell; at PR = 1 the degenerate strictness signature of check_chain is
asserted EXACTLY, not skipped). Statements, with rigor classes:
 (1) THEOREM (ε-level closed forms; carriers = the executable dominance
     check + rejector tests): under the CAPPED-adaptation plug closure
     (S-H Eqs. 10-12 with the free branch replaced by the sonic-capped
     per-phase ideal of the Prop. G-B sharpening), the plug family
     weakly DOMINATES the fixed bell pointwise in every phase, hence in
     every μ-average: NO cell of the ε-level diagram has a strict bell
     winner. Mechanism: below release the two candidates coincide as
     members (same ε, Theorem-1 unimodality orders the bell branch);
     after release the capped ideal is the per-phase argmax (int-max
     rung), pointwise ≥ any fixed member.
 (2) THEOREM (same carriers): at ε_max ≥ knee the capped plug equals
     the int-max relaxation POINTWISE, hence ATTAINS the capped
     ceiling — M1 duality-gap-zero on EVERY Pa > 0 cell, INCLUDING
     subcritical cycles (9 such cells in the record). This EXTENDS the
     OP-0 attainment (8 supercritical Table-1 rows) to the whole capped
     class: the "min-cycle NPR ≥ critical" hypothesis is needed by the
     NAIVE/published closure only, not by the capped one.
 (3) Artifact of record (executable, REJECTED as a topology verdict):
     the PUBLISHED S-H spike closure is strictly suboptimal wherever
     the cycle has subcritical phases (30 strip cells in the record),
     and at the sonic-annulus cap ε_max = 1 it INVERTS the bell/plug
     ranking (bell "wins" by 1.7e-2 s at PR = 90): the OP-0 sonic-cap
     discovery surfacing at topology level. tests/test_phase_diagram.py
     detects the flip and check_cell rejects it (negative control among
     eight, incl. explicit T3/T4 controls).
 (4) Structure of the computed map (record): tie region = {PR = 1}
     ∪ {ε_max = 1} ∪ {ε_max ≤ ε*(Pc_min): the capped plug never
     releases and coincides with the capped bell AS A MEMBER}; a
     cap-bound plug band with gap > 0 (the genuinely averaged regime —
     PB-2's section); the M1 region ε_max ≥ knee. The duty-split /
     mixed region of the general conjecture is NOT expressible at the
     ε rung (one shared ε DOF cannot encode duty splitting): OP-11 at
     contour level remains CONJECTURE.

------------------------------------------------------------------------------
## 11. Falsifiable-criterion index (one line each)

| Item | Executable falsifier |
|---|---|
| O1 | argmax(J) vs argmax(Isp) under response map — split ⇒ coupling matters |
| T0/N-T0′ | URANS thrust trace flat for single mode |
| C-T1/P4 | O5: unsteady sim vs J_avg + St·J₁ |
| T2/(**′) | quasi-1D reduction ⇒ NPR(ε*) = ⟨Pc⟩/Pa (repo tests, exists) |
| T3 | O1-oracle: ensemble optimizer returns Rao-at-⟨Pc⟩, ΔIsp = 0 |
| T3-sharpness | two-γ counterexample: collapse fails, γ_eff = ⟨Pcγ⟩/⟨Pc⟩ |
| T4 | O2-oracle: ideal-plug machinery returns peak design |
| P1 | O4: freezing-adjoint dΩ_w/dΣ vs FD of continued waves |
| P2 | O3: AD-MOC dot-product + term match with Rao conditions |
| P5 | sign of dJ/dδ at δ=0 decides if non-axisymmetry can ever pay |
| P7 | S1-regularity monitor along optimization iterates |
