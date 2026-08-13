# APPARATUS BRIEF — the cycle-averaged variational nozzle program (record state)

Sources of record: `docs/rde_nozzle_MASTER.md` (M0), `docs/rde_nozzle_P2_lemmaA.md`,
`docs/rde_nozzle_theorem_ledger.md` (D3), `validation/ADVISORY_generality_litmap_2026-08-12.md`,
`validation/ADVISORY_litmap_extension_2026-08-13.md`, `docs/rde_nozzle_PROGRESS.md`.
Rigor legend used verbatim from M0: THEOREM / THEOREM* (proof inside a declared model closure,
`inherits` a named conditional) / SCHEMA (correct structure, rigor gap named) / CONJECTURE
(precise + falsifier) / PRACTICE (instrumented, no theorem). Anything not stated in the documents
is marked NOT ESTABLISHED rather than filled in.

---

## (A) THEORETICAL LEVEL

**The object.** An RDE feeds a *fixed* nozzle with a periodic family of interface states: at each
azimuthal station the products' state (P, T, M, flow angle, composition) sweeps a cycle as the wave
passes. The program defines the objective as a phase integral over that cycle and derives Rao-type
stationarity for the *shared* contour.

**The problem (P)** (M0 D2.6, "canonical fusion" of Parts II and IV). GIVEN: an axisymmetric envelope
E (L_E, R_E), attachment set Λ, constant Pa > 0; an interface contract (Γ_d, D, μ) with stage-A
admission audits passed (characteristic completeness on axially supersonic patches; Crocco
compatibility; per-phase spacelikeness margin; a declared closure O1/O2/O3 on subsonic patches); a
constraint vector c = (L, ε_max, L_p, curvature/angle bounds, symmetry class). ADMISSIBLE SET
A_gen(c) = compact solid sets S ⊂ E with uniform cone condition (h0, ω), attachment on Λ, g_i(S) ≤ c_i,
decomposed into finitely many *topology sectors* — configurations (bell / plug / shrouded / E-D) are
**outputs, not inputs** — with a working spline class A_h per sector. A per-phase state constraint
g_sep(S; s(ξ)) ≤ 0 holds μ-a.e. (separation margin, empirical closure). STATE: the unique S1 solution
per phase. OBJECTIVE: J[S] = ∫_Ξ F[S; s(ξ)] dμ(ξ).
(P) asks for the **pair (S*, δ)**: (i) argmax over A_h(c) (existence P7); (ii) the averaged
stationarity system T7; (iii) reduced Hessian ⪯ 0 on the active tangent cone; (iv) *certified
globality*: J[S*] ≥ sup_{A_gen(c)} J − δ with δ = B − J[S*] COMPUTED (B = min of the bound ladder:
int-max, sonic-capped J_ideal, B_EK) and δ = 0 PROVEN in structured classes (mechanisms M1 duality-gap
zero, M2 T3 pointwise transfer, M3 unimodality, M4 deflated enumeration, M5 certified global search);
(v) declared bars |J_exact − J[S*]| ≤ St|J1| + D2 residual + DWR — declared ESTIMATES, not certified
bounds (only the D2.2 fallback brackets [J_exact^-, J_exact^+] ship as certified).
Maximality argument of record: no admissible-set-free version (vacuum: sup unattained), no
solution-concept-free version (multi-D non-uniqueness), and unconditional global optimality on
nonconvex infinite-dimensional PDE-constrained shape sets exists for nobody.

**The measure μ** (D2.3). μ = pushforward of normalized cycle time under t ↦ ξ; the theory is
measure-agnostic *within* declared μ-hypotheses (probability measure; μ-a.e. audits; **switch phases
μ-null** — must be re-verified for every imported measure, non-trivially for atomic/empirical ones).
Lemma 2 (T-O2, THEOREM): for exponential blowdown Pc(ξ) = P_CJ·PR^(−ξ), ξ ~ U[0,1), the operating
measure is **log-uniform in pressure**, dμ_P = dPc/(Pc ln PR). Scope note: a phase containing a MODE
TRANSITION has no steady per-state F and is outside D2.3 — routed to the robust layer, never averaged.

**T7 (T-T7FS, SCHEMA) — the averaged stationarity system**, three parts:
(a) per a.e. ξ, the per-phase adjoint Euler system; in the **irrotational–homentropic** subclass of S1
it reduces to the classical closed form (optimal control surface = the phase's characteristic; first
integral f2 = −λ2(ξ)). The S21 audit C1 scoping is binding: on rotational S1 members the identification
survives only at FIELD level.
(b) shared wall: ∫_Ξ G_ξ(x) dμ + λ_L g_L(x) = 0 a.e. on the wall, G_ξ the phase Hadamard density —
**no phase satisfies its own wall condition; the μ-average does.**
(c) shared endpoint, the **weighted transversality (\*\*')**: ∫_Ξ (∂F/∂s_E)[Σ; s(ξ)] dμ(ξ) = 0, which
factorizes as R(ξ)·w(ξ) with R the classical corner residual and w > 0 a geometric-kinematic weight.
w is phase-independent EXACTLY in the T3 class; **everywhere else the naive average of corner
conditions is WRONG.**
Upgrades of record: differentiation under the cycle integral is THEOREM* (dominated by audited
margins); P3 (λ2 ∈ L²(dμ)) is THEOREM* [C-D25U] in the shock-free class, inheriting [C-MAJDA] across
fitted shocks; P7 existence is THEOREM* on margin-certified level sets. Non-smoothness: switch phases
are μ-null with F continuous (Leibniz terms cancel); persistent kinks → Clarke subdifferentials.

**T-T3 (THEOREM 5, THEOREM) — the collapse, fixed wall.** Under H1 (one frozen γ common to all
phases), H2' (fixed wall, full-flowing, supersonic exit every phase — ambient-blind interior), H3
(phase-independent nondimensional inflow shape; phases differ only through (P0, T0)(ξ)), H4 (per-phase
uniqueness), Pa constant, shared constraints: **J[Σ] = F[Σ; ⟨Pc⟩_μ] POINTWISE on shape space** — the
cycle-optimal fixed wall is exactly the classical contour designed at the mean pressure. Proof =
Lemma A (pressure-scaling similarity; valid for γ(T) and ACROSS transversal shocks; **thermal pin of
record: thermally-perfect ideal gas p = ρRT with FROZEN composition, not relaxable, fails for
co-volume/virial/tabulated real-gas EOS**) + Lemma B_T3 (stagnation-temperature similarity; REQUIRES
calorically perfect gas — this is where the collapse boundary sits) + Lemma C (affinity
F = a[Σ]·Pc − Pa·b[Σ]). Sharpness [T-T3-CE]: a two-phase two-γ counterexample breaks the collapsed
form; the first-order closure is γ_eff = ⟨Pc γ⟩/⟨Pc⟩; design penalty is second order (envelope
theorem). Corollaries: per-phase optima DO move with Pc; Pa enters linearly (trajectory-average and
cycle-average are one mathematics); oracle O1.
Extensions of record: **T-T3-SI** (tier 1 THEOREM / tier 2 THEOREM*) — on the p-only scaling class with
vacuum objective and geometry-only constraints, F and ṁ both scale by k(ξ), so Isp is phase-constant
and **Isp_cycle is identical for EVERY admissible measure**; matched-ṁ and matched-⟨p⟩ degenerate.
**T-T3-MAP** (SCHEMA container, per-clause classes) is the adjudicated breaker map: T3-as-stated is
UNBROKEN by five breakers, while the *general* claim "cycle-averaged optimum = matched-ṁ steady
optimum" is REFUTED as a general theorem and proved only on the tier-1+vacuum corner. Named breakers:
Pa ≠ 0 (average-of-ratios Isp collapses at the HARMONIC mean, strictly below ⟨Pc⟩); outside H1/H3 the
mixture form J = a_eff⟨Pc⟩ − Pa b with a_eff = ⟨aPc⟩/⟨Pc⟩; swirl (twin fairness, E_θ swirl-KE debit,
recovery asymmetry signs AGAINST the plug); subsonic patches (J as written is UNDEFINED when
μ(Ξ_sub) > 0 — the two-regime contract is load-bearing; collapse-in-form survives only under H3-cl,
"certified phase-independent closure patch pattern", expected to fail on migrating patterns);
conventions/matching (invariance is THEOREM on the p-only class only). PROTOCOL T3-CONTROL (PRACTICE,
rejector-gated) is mandatory alongside any decisive cycle-averaged-vs-steady comparison.

**T-T4 (THEOREM 6, THEOREM\* under closure [C-HT4], ideal adaptation).** Per phase, F[Σ_l; s(ξ)] is
nondecreasing in plug extension l and exactly constant for l ≥ l(ξ), with l(ξ) increasing in Pc(ξ);
argmax sets are nested half-lines, so max_Σ ∫F dμ = ∫ max_Σ F dμ, attained by the **peak-phase design**:
untruncated plug at NPR = P_CJ/Pa (capped by ε_max). Sharpness: a length cap L < l(ξ_peak), a
base-pressure model, or non-ideal adaptation break the nesting; then max∫ < ∫max STRICTLY and the
optimum satisfies T7 with the μ-averaged plug corner condition.

**PB-2** = the truncated plug under a length cap: **the first genuinely averaged shape problem** of the
program. Two caveats of record ride the word "first": Kraiko–Osipov PMM 34(6) 1970 already poses
time-averaged endpoint conditions for a length-capped nozzle with base pressure (trajectory measure in
place of cycle measure — mandatory citation), and since 2026-08-13 also the ISABE-2003-117 /
Bogdanov-Kraiko-Pyankov-Tillyaeva 2002 caveat (variational maximum-AVERAGE-thrust contouring under
time-dependent stagnation parameters; full text UNREAD).

**EQ-v2** (S21 registration block; supersedes the unqualified EQ, which is REFUTED and non-citable).
Scope: fixed (ε, L) in the DEF regime, bell single-wall, homentropic–homoenergetic core, perfect gas on
the classical side. **Direction A [CONJECTURE on SCHEMA footing]**: the classical Rao–Beck DEF
construction (single PM jump landing on the validity boundary at D', E fixed by DE↔BD mass equality)
is, in the joint continuum limit (h→0, KS ρ→∞, μ_0→0; limit order = obligation O5), a **margin-active
KKT point of the direct problem**, its fold touching the *construction surface* only at D' (clause
corrected at constant content in S24). **Direction B [CONJECTURE]**: the converse holds only under
H1 (single active cusp, nondegenerate Danskin derivative), H2 (cusp on the open terminal characteristic
strictly between axis and lip), H3 (MFCQ via jump-depth direction + strict complementarity μ>0),
H4 (matched admissible classes), H5 (genuine-margin protocol excluding budget/table artefacts),
H6 (local uniqueness of the classical DEF at the given (ε,L), unproven), **plus H7-SEL**
(selection/global-max among margin-active KKT points, red-team-restored), and it speaks of the DEF
*construction*, not its optimality (declared weakening pending O2/O3). Component **S4 is THEOREM**.
S24 added **H-CLASS** (the design class/mesh can approach the (G) boundary before losing
certifiability), which MEASURABLY FAILS at the tier-0 9-dof class on the deep-DEF instance.

**Declared rigor classes / pins / exclusions.** Solution classes: S1 piecewise-smooth MOC-regular
(canonicity EXACT in shock-free regions via weak–strong uniqueness, Brenier–De Lellis–Székelyhidi CMP
305:351-361 (2011); across transversal fronts a DECLARED conditional backed by [C-MAJDA], sharpened
in-class to the single scalar U3-H1 with instance value s_L = 1.8685; BVP-native transfer [T-XWS] is
THEOREM*); S2 entropy-weak never used as a constraint; S3 statistical, roof definition only.
User scope pins: **P1 frozen thermally-perfect mixture** (finite-rate chemistry contained
STRUCTURALLY but deliberately NOT instantiated; priced by the [T-EQBR] frozen/equilibrium bracket,
+6.3..+7.0% above the frozen ceiling), **P2 no two-phase / gas-particle**, anti-overengineering.
Interface default of record = the **L4 class** (every patch axially supersonic with margin), on which
ṁ-independence is EXACT and mean upstream influence is EXCLUDED BY THEOREM [T-NSW]. **γ-variable status
(E4)**: the closed-form stationarity system is EOS-general in primitive variables (THEOREM audit,
P2_lemmaA §3); the true γ = const boundaries are (a) the corner↔ε closed-form BIJECTION used by
implementations — risk **E4**, oracle Scofield–Hoffman 1971 Table 2 Case 1, frozen thrust 2290 lbf, gate
G2; (b) T3's Lemma B_T3; (c) the S-H ε-rung closed forms. Standing directive: γ = const may appear only
as a declared oracle or demoted corollary, never load-bearing.

---

## (B) FORMAL LEVEL — the exact mathematical objects

**Route A (control-surface / check-contour; Nikol'skii → Guderley-Hantsch → Shmyglevskii → Rao →
Rao-Beck).** On the terminal control surface from kernel point C to lip E, with q := 2π y^δ,
ψ := φ − θ, α := arcsin(1/M):
- thrust integrand f1 = [(p − pa) + ρW² sin(φ−θ)cos θ / sin φ] q; mass integrand f2^i =
  [ρW sin(φ−θ)/sin φ] q; length integrand f3 = cot φ; augmented density f = f1 + λ2 f2^i + λ3 f3, with
  λ2 (mass) and λ3 (length) CONSTANT multipliers. The Euler–Lagrange system is ALGEBRAIC:
  ∂f/∂φ = ∂f/∂θ = ∂f/∂W = 0.
- **Surface = characteristic (a RESULT, not an assumption)**: tan²ψ = 1/(M²−1) ⇒ φ = θ + α (bell/shroud,
  C+) or φ = θ − α (plug/spike, C−). [= Rao 1958 Eq. (11)]
- **First integral f2**: f2 := W cos(θ ∓ α)/cos α = **−λ2**, constant along the terminal characteristic;
  sign selected by characteristic FAMILY. [= Rao Eq. (12)]
- **Second first integral**: q ρ W² sin²θ tan α = **−λ3**. [= Rao Eq. (13)] NAMING CAUTION of record:
  the corpus table calls *this* quantity "f1" (f1 = y^δ ρW² sin²θ tan α = −λ3), while in the Lagrangian
  above f1 denotes the thrust integrand; the 2π is absorbed in λ3 — a declared convention, not a
  discrepancy.
- **Corner / endpoint transversality**: the augmented density vanishes at the free endpoint,
  (f1 + λ2 f2^i + λ3 f3)|_E = 0, giving (p − pa) − ½ρW² sin(2θ_E) tan α = 0, i.e.
  **pa = p − ½ρW² sin(2θ) tan α** (CSTR_PA, bell/shroud) and the '+'-sign mirror with base pressure p_b
  (CSTR_PB, plug). [= Rao Eq. (14) / Rao 1961 Eq. (6)]
- Convention of record: Rao/Rao-Beck name C+ what Zucrow-Hoffman/GENO name C−; this repo follows GENO.
  Declared classical limits of Route A (Shmyglevskii 1980): exhausted by the complete conservation-law
  sets; cannot carry constraints not expressible on the check contour; **no check surface exists in 3-D**;
  dies for dissipative/reacting flow.

**Λ-form validity margin (G)** — both bounds ADOPTED, S4 THEOREM:
val = [Λ·B·(A+B) − (A−B)] / [1 + Λ·(A+B)], A = tan(θ−α), B = tan α, Λ = V dα/dV on the isentrope;
val > 0 = valid side; val = 0 is a POLE of the reduced DE-march ODE (dθ/dR ~ 1/val). With the
perfect-gas Λ it reduces EXACTLY to Rao-Beck 1994 Eq. (4) (hand proof + independent judge re-derivation
+ machine identity [X-VMON] at the roundoff floor over a 247-point grid). BOUND (a): EOS-general but
NOT data-general — homentropic–homoenergetic (single-isentrope α(V)) data only; the stratified (q; s, h0)
extension is owned by F2. BOUND (b): GENO's implementation magics (dV_pert = 1.0, |den| < 1e-10 fold
guard, PM landing window) are PRACTICE, tracked, not adopted.

**Fixed-ε transversality bookkeeping**: at fixed (ε, L) Rao's free-endpoint Eq. (14) is REPLACED by the
lip-constraint multiplier λ_e = dJ/dy_lip; the classical reading pa/p_E need not vanish — it equals the
constraint's shadow price (measured cross-design agreement 2.803e-03).

**Route B (multiplier fields / whole-region functional; Guderley-Armitage, Sirazetdinov, Kraiko,
Hoffman, Scofield-Hoffman, HTH, JOTA 1972, Johnson-Thompson-Hoffman, Kraiko-Osipov).** Every flow PDE
is adjoined pointwise with a multiplier FIELD; the first variation yields adjoint PDEs **hyperbolic with
the SAME characteristics as the flow** (streamlines + Mach lines); the exit surface's Mach-line character
is DERIVED (anti-overspecification / Miele transversality, JOTA 1972 Eq. (25)); optimality =
one redundant boundary condition turned into a **residual** — **Hoffman 1967 Eq. (78):
E = y·h1 − (u y' − v)·h3 on the boundary condition**, with Scofield-Hoffman Eq. (43) the wall form and
C&F 1974 Eqs. (19)/(29) the rotational forms. The key classical unlock was Kraiko's **discontinuous
multipliers** (jumps along characteristics with derived jump conditions; Kraiko-Osipov Eq. (3.8)) — the
classical ancestor of the program's **F4b fitted-front adjoint jump conditions**. In (P), Route B IS the
field-level limb of T7(a).

**Lemma B (adjoint = reverse-AD).** NAME COLLISION of record: "Lemma B" denotes two distinct objects —
(i) T3's stagnation-temperature similarity lemma (calorically perfect), and (ii) the discrete-adjoint
lemma used throughout the implementation: *the x-block-triangular structure of the fitted march implies
reverse-mode AD of the assembled march IS the transposed (discrete adjoint) sweep*. Reading (ii) is the
one meant by "Lemma-B guarantee". Its machine witness is the **O3.1 transposition identity**:
|⟨w, Jv⟩ − ⟨Jᵀw, v⟩| measured over the ENTIRE march = 2.7e-10 against derived tolerance 5.1e-8 (replay
fidelity 1.6e-13); a corrupted whole-march vjp breaks it (negative control fires).

**Hoffman-E residual as certificate (M0 VI.3)**: alongside f2-drift, the Hoffman E-residual is required
→ 0 along optimized contours, evaluated along each phase's terminal characteristic; λ2(ξ) = −f2(lip
data) serves as the closed-form multiplier initializer (P3 theorem).

**S1 boundary function (the a-posteriori membership monitor)**, γ-free closed form:
val = [Λ·B·(A+B) − (A−B)] / [1 + Λ·(A+B)] with A = tan(θ−α), B = tan α, Λ = V dα/dV — the same object as
the Λ-form above, used as the S1 / Sternin-boundary monitor.

**Tier ladder and margin-constrained KKT.** (P_t): max J(Σ) s.t. g(Σ)=0 (ε, L), Σ ∈ C_m ∩ A_t(μ_0),
A_t(μ_0) = {Σ : P(Σ) has a solution in tier t's class with margin vector m(Σ) ≥ μ_0 > 0}, the margin
vector collecting the FOLD margin (Eq. (4)/Sternin at the junction), the CAUSALITY margin u_x − c, and
the uniform constants of the certified class. Tiers S_0 (shock-free) ⊂ S_1 (finitely many FITTED fronts
under RH + entropy + Lax + Lopatinskii certificates) ⊂ …; nesting THEOREM. At a boundary-active optimum
first-order optimality is **∇J = λ∇g + μ∇m, μ ≥ 0**, and the measured μ **prices shock-freeness**. μ is
under a **B-stationarity qualifier** until obligation O1 (Danskin/Clarke cusp derivative) is discharged.
KS aggregation: v_min − ln(N)/ρ ≤ KS ≤ v_min [THEOREM], with ρ DERIVED = K_RICH·ln(N)/μ_0_min.
Tolerance-ball ship gate [X-TBAK]: min over ‖δW‖_∞ ≤ δ of m ≥ m(W) − L1_sup·δ [THEOREM, m C¹]; measured
L_TB = 4.321067e+01 per unit ball radius on the bell tier-0 9-dof class.

**Jump / discontinuity conditions (F4b, open).** Fitted-front adjoint jumps inherit the Kraiko
discontinuous-multiplier structure; G12-L2 (machine-verified) gives linearized RH nonsingular strictly
inside Lax with degeneration EXACTLY at characteristic fronts. Named open item: the tier-1 certificate
list (RH + entropy + Lax + Lopatinskii) is **shock-shaped**, and a certificate class for
linearly-degenerate (CONTACT) fronts is required before Shmyglevskii's second scheme can be claimed
structurally contained.

---

## (C) ALGORITHMIC LEVEL — the executable pipeline

**Data contract (VI.1).** CycleFamily: {P0, T0, thermo handle γ(·;ξ) | M_in(y;ξ), θ_in(y;ξ), s(y;ξ),
[vorticity]} + μ weights + provenance + stage-A audits (characteristic completeness; Crocco residual;
spacelikeness margin min(M_x − 1) per phase; H-I2/choking margins; **T0 flatness / harmonic-decay
certificate**). Generated data passes the same audits as imported data.

**Per-phase evaluator (VI.2).** Rotational MoC (Zucrow Ch.17 class; GENO MoC_Gen semantics), γ(T)
backend, **FITTED inherited sheet** (RH on the front), plug off-design free-boundary march,
separation-criterion hook, S1 boundary-function monitor, unit processes O(h²). Implemented as a
differentiable JAX march in which every cell is an **implicit custom_vjp unit process** (implicit-function
rule, never unrolled) — so reverse-mode AD of the assembled march IS the Lemma-B discrete adjoint sweep,
executably. Certified against GENO: generated ideal contour inside the derived two-resolution Richardson
band at 62/62 samples, max|dy| = 7.6e-9 (band 4.5e-3), achieved Me twin-identical to 8.4e-9.

**Per-phase gradient (VI.3).** Closed-form adjoint where smooth (f2 invariant + CSTR_PA/CSTR_PB corner
residuals); reverse-mode AD of the fitted march elsewhere; **differentiate the fitted front, never a
captured smear** (captured-shock adjoints rejected per Giles-Ulbrich/Lozano). Certificates: O3.1
dot-product to machine precision; Hoffman-E residual → 0.

**Cycle layer (VI.4 / VI.4bis).** Locate switch phases ξ*(Σ) (separation onset, adaptation, sheet entry)
by root-finding and **SPLIT the Gauss panels there** (else O(1/N) and a noisy outer gradient — the
practical convergence trap); trapezoid-on-the-circle only opportunistically when the T0 flatness +
harmonic-decay certificates pass. Unconditional pins: EOS-general thermo backend mandatory, the
γ = const corner↔ε bijection **FORBIDDEN as a solver step**; rotational data ⇒ field-level adjoint,
closed form is oracle/initializer only; the robust CVaR/DRO layer is part of the architecture (idle, not
absent, on certified-periodic data).

**Driver (VI.5).** TR-SQP / trust-constr on spline DOFs (design vector = attachment angle θ_B + clamped
spline wall nodes), gradients Riesz-represented in a Sobolev/Steklov–Poincaré metric for
mesh-independence; active-set constraints {L, ε_max, lip, truncation} with multipliers reported as
MARGINAL VALUES; RK-G segmentation policy with freshly measured Jacobi scaling and full Hessian per
segment base (no curvature carry-over); bundle safeguard near kinks; deflated continuation for
stationary-point enumeration; sector tournament for topology; seeds Rao-at-⟨Pc⟩ (bell) and peak design
(plug), never affecting the certified result. Record verdict (brick 2, reduced twin case): from a 1.5%
perturbed start the optimizer recovers and exceeds the GENO-projected seed (J* = 2.7761688e+07) at
in-stratum KKT = 7.745e-02 ≤ derived gtol 1.156e-01 — **the Rao optimality conditions REACHED VIA THE
GRADIENT, never imposed by an outer loop**; agreement with the independent classical route at 91/91
samples inside the derived cross-code band (max|dy| = 1.861e-03).

**Certificate stack / oracles (VI.6).** Per Verdict: KKT + (\*\*') residuals; reduced-Hessian spectrum;
dual-route agreement (B1 NLP vs B2 collocation of the optimality system); **oracles O1** (T3-family in ⇒
Rao-at-⟨Pc⟩ out, ΔIsp = 0), **O2** (ideal plug ⇒ peak design), **O3** (dot-product / transpose identity),
**O4** (freezing-adjoint dΩ/dΣ vs FD of continued waves), **O5** (unsteady sim vs J_avg + St·J1); DWR
discretization bars; bound-ladder gap + globality mechanism; O(St) and D2 physical bars; data provenance
and margins. **Nothing ships outside a Verdict.**

**Thermo backend (DIR-THERMOTAB).** JAX engines READ TABLES (GENO backend-1 / ATLAS-FLINT model): the
march consumes interpolated (h, s0, cp)(T) tables with derived table-density floors; **Cantera is the sole
production table generator**; γ = const tables only as declared known-answer oracles. Survey of record:
in the working window [1050, 3900] K the NASA fit has quartic cp ⇒ quintic h, exactly reproduced by the
quintic-Hermite closure (in-window the closure is an exact re-representation); the ATLAS dCp column is
NOT analytic (measured 1-K backward difference); FLINT (GENO backend-2) interpolates linear-C0.

**Tooling.** JAX primary (custom_vjp + implicit rules), Julia/Enzyme declared alternate, GENO-Fortran the
independent dual-code reference; Newton-Krylov + Arnoldi for the wave-frame anchor; implicit shock
tracking (HOIST class). Cross-code oracle [X-GENOXC] certifies GENO's Fortran MoC nodes satisfy the
repo's EOS-general second-order axisymmetric unit process within the derived per-cell truncation band.

**Program state (PROGRESS, 2026-08-12).** F0 complete; F1 CLOSED (campaign 1/2, session 2/3;
certifiability-limited branch, margin inactive); F1b DEF twin CLOSED (EQ-v2 stays CONJECTURE + H-CLASS);
S25/S25-bis speed program MET (segment record 100.84 s → 5.58 s = 18×). Ratified NEXT chain: **S-ORDINE
(R32) → S-CERT (R33) → F2 general engine**.

---

## (D) CLAIMS OF RECORD, ATTACKABLE — one falsifiable sentence each

1. **P2/G14 (Rao = adjoint bridge).** No published work identifies the classical multiplier field of
   variational nozzle design with the continuous adjoint of modern shape optimization (Rao's optimality
   residual = the adjoint gradient); FALSIFIED by exhibiting a paper that states that identification —
   the closest adjacent artifact found is the Russian school's internal "сопряжённая задача" terminology
   (Kraiko–Tillyaeva, J. Math. Sci. 208:181-198, 2015), which is terminology only, query-bound 2026-08-13.
2. **T-T3 (collapse, THEOREM).** Under H1–H4 + H2' + constant Pa, J[Σ] = F[Σ; ⟨Pc⟩_μ] POINTWISE on shape
   space; FALSIFIED by any instance satisfying all five hypotheses whose cycle-averaged optimum differs
   from the classical design at ⟨Pc⟩_μ beyond the derived bar.
3. **T-T3-SI (tier-1 scale invariance, THEOREM).** On the p-only scaling class with vacuum objective and
   geometry-only constraints, Isp_cycle is identical for EVERY admissible measure; FALSIFIED by a
   measured nonzero convention spread beyond its derived bar on certified tier-1 data.
4. **T-T3-MAP (breaker map).** The general claim "cycle-averaged optimum = matched-ṁ steady optimum" is
   FALSE as a general theorem and true only on the tier-1+vacuum corner; FALSIFIED by a proof of the
   general statement, or (converse direction) by a tier-1+vacuum instance where the two disagree.
5. **T-T4 (plug simultaneous optimizability, THEOREM\* under [C-HT4]).** Under ideal adaptation the
   per-phase argmax sets are nested half-lines and the peak-phase (untruncated, NPR = P_CJ/Pa) plug
   attains ∫max; FALSIFIED by an instance under the closure where max∫ < ∫max, or by showing the
   monotonicity/nesting fails without breaking the closure.
6. **PB-2 (truncated plug = first genuinely averaged shape problem).** No prior work poses the
   length-capped plug as a genuinely averaged (non-collapsing) shape-optimization problem; FALSIFIED by
   Kraiko–Osipov 1970 for the trajectory measure (caveat already carried) or by ISABE-2003-117 /
   Bogdanov 2002 once read — the "first" is program-internal wording for the CYCLE instance.
7. **D2 gap G3 (no averaged shape theorem in the corpus).** No published variational nozzle theory
   derives optimality conditions for a shape shared across a *family* of inflow states weighted by a
   measure, with a T4-type free-boundary counterpart; FALSIFIED by exhibiting such a derivation —
   qualified since 2026-08-13 to *spatially nonuniform traveling/rotating-wave inflow with genuinely
   unsteady dynamics in the constraint*, the quasi-steady uniform-inflow near-miss being ISABE-2003-117.
8. **Empty-niche claim (generality).** "Keep the variational MoC formulation and swap in a modern
   optimizer" is occupied by no one, in any school (verified by dedicated sweep 2026-08-13); FALSIFIED by
   one paper doing exactly that on the thrust-optimal problem.
9. **EQ-v2 Direction A [CONJECTURE].** The classical Rao–Beck DEF construction is, in the joint limit
   (h→0, ρ→∞, μ_0→0), a margin-active KKT point of the direct problem with its fold touching the
   construction surface only at D'; FALSIFIED by a converged margin-active direct optimum whose cusp
   structure or D'-location disagrees beyond the derived band — currently UNREACHED because H-CLASS
   measurably fails at the tier-0 9-dof class (min DE val 7.31e-2 = 33× the tightest pre-registered floor).
10. **EQ-v2 Direction B [CONJECTURE].** The converse holds only under H1–H6 + H7-SEL and speaks of the
    DEF *construction*, not its optimality; FALSIFIED by exhibiting a margin-active KKT point satisfying
    all seven hypotheses that does not coincide at first order with the classical DEF construction.
11. **S4 [THEOREM].** The (G)/Λ-form boundary with the perfect-gas Λ reduces EXACTLY to Rao–Beck 1994
    Eq. (4); FALSIFIED by a state where the two zero sets differ beyond the roundoff floor.
12. **E4 (γ-variable boundary).** The classical stationarity system (L.6)–(L.16) is EOS-general in
    primitive variables, and the only γ = const dependence in the implementations is the corner↔ε
    BIJECTION (plus T3's Lemma B_T3 and the S-H ε-rung closed forms); FALSIFIED by exhibiting a
    homentropic frozen-γ(T) state where any of (L.6)–(L.16) fails, or by the Scofield–Hoffman 1971
    Table 2 Case 1 oracle (frozen thrust 2290 lbf) failing at gate G2.
13. **O3.1 / Lemma-B guarantee.** Reverse-mode AD of the assembled fitted march equals the transposed
    discrete adjoint sweep, measured |⟨w,Jv⟩ − ⟨Jᵀw,v⟩| = 2.7e-10 vs derived tolerance 5.1e-8 over the
    entire march; FALSIFIED by any march configuration where the identity exceeds its derived tolerance
    without a seeded corruption.
14. **T-T0 (wave-frame exactness, THEOREM).** For a single rotating mode the instantaneous thrust through
    every axisymmetric surface is CONSTANT (not merely mean-equal); FALSIFIED by a measured non-flat
    thrust trace on a certified single-mode field (the flatness monitor is the executable falsifier).
15. **T-GB / M1 (geometry-free bound).** For ANY solid set in ANY topology under choked frozen feed,
    J[S] ≤ ∫F_id dμ with F_id CAPPED AT THE SONIC STATE; FALSIFIED by an admissible design exceeding the
    capped ceiling (the uncapped form is already rejected on four subcritical Table-1 rows).
16. **(\*\*') weighted transversality.** The naive μ-average of per-phase corner conditions is WRONG
    outside the T3 class, where w(ξ) is phase-independent; FALSIFIED by a non-T3 instance where the naive
    average and (\*\*') select the same stationary contour beyond coincidence.
17. **K_disc ≈ A_0 bridge — ALREADY FALSIFIED (state of record).** The discrete certifiable set does NOT
    approximate the physical validity set on the S20/S22 instance: certification degrades at val
    0.61–0.86, nowhere near 0; any future bridge claim must carry a per-instance monitor test.
18. **Containment claim (generality litmap, refuter-corrected).** (P) + T7 + the tier ladder contains, as
    special cases under named hypotheses, the inviscid-Euler exogenous-measure CORE of every variational
    maximum-thrust nozzle formulation in the read corpus (both Route A and Route B); FALSIFIED by a
    corpus formulation whose core is not a restriction of (P) — two structural non-containments are
    already DECLARED: Kraiko–Osipov's endogenous trajectory-adjoint weight (§6(g)) and
    boundary-layer-terms-in-the-functional (§6(c)).
19. **In-class F7 surplus datum (S24, MEASUREMENT, capped).** Within the tier-0 certified 9-dof class at
    (ε = 30, L = 8) the DEF-wall class representative is NOT the J-argmax — a certified margin-inactive
    design exceeds it by +2.0407e5 (+0.51%) vs a pre-registered band 5.38e3; the claim cap is binding:
    this is an IN-CLASS statement, NEVER a statement about the true DEF construction's optimality
    (O3-gated).
20. **Novelty bound discipline.** Every novelty claim above is QUERY-BOUNDED, not absolute; named blind
    spots of record include ISABE-2003-117 / Bogdanov 2002 full texts, Kraiko–Tillyaeva 2015 reference
    list, Russian full-text corpora (eLibrary/Math-Net/TsAGI-CIAM), Chinese-language journals, restricted
    JANNAF, paywalled AIAA/ScienceDirect full texts, and the absence of a Scopus/WoS forward
    citation-graph sweep of Rao 1958 / Hoffman 1967 / Guderley-Hantsch 1955 filtered by "adjoint".
    Residual human-pass gate G5 (Kraiko-1979/PMM) blocks SUBMISSION, not work.
