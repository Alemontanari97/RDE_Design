# Expert read — Liu et al. 2022, aerospike nozzle for RDE

**Reader role:** convergence review, one-to-one comparison against the record apparatus
(`literature_review/reports/00_APPARATUS_BRIEF.md`).
**Date:** 2026-08-13.
**File on disk:** `literature_review/liu_2022_aerospike_rde_ga_gradient_optimization.pdf`

---

## 0. Citation (verified from the PDF itself)

Xiang-Yang Liu, Miao Cheng, Yun-Zhen Zhang, Jian-Ping Wang (corresponding, wangjp@pku.edu.cn),
**"Design and optimization of aerospike nozzle for rotating detonation engine"**,
*Aerospace Science and Technology* **120** (2022) **107300**, 14 pp.
Center for Combustion and Propulsion, CAPT & SKLTCS, Department of Mechanics and Engineering
Sciences, College of Engineering, Peking University, Beijing 100871, China.
Received 8 October 2021; received in revised form 14 December 2021; accepted 18 December 2021;
available online 22 December 2021. Communicated by Y. Yanxing.
DOI printed on p. 1: `https://doi.org/10.1016/j.ast.2021.107300`. ISSN 1270-9638.
Funding: National Natural Science Foundation of China, Grant No. 91741202.

## 1. Read coverage

**14 / 14 pages read in full** with the Read tool (single call, pages 1-16 requested, 14 returned),
**bibliography included** (refs [1]-[58], pp. 13-14).
Independently cross-checked by full-text extraction (`pypdf`, 58 454 characters over 14 pages) used
only for keyword census and verbatim quotation — extraction fidelity confirmed against the rendered
pages on positive controls (`Angelino` 2, `isentropic` 39, `time-averaged` 18, `truncat` 16, …).
**Nothing was left unread.** No supplementary material is referenced by the paper.

---

## 2. What the paper actually does

| Item | Content |
|---|---|
| **Problem** | Thrust performance of a kerosene(Jet-A)/air RDE with an annular chamber fitted with four different aerospike/plug nozzle configurations; secondary question = pressure gain in the combustor as a function of throat constriction. |
| **Formulation** | **Not an optimization problem.** The "optimal" ramp is produced by the *closed-form* Angelino [35] approximate plug-nozzle construction (Eqs. (5)-(9), pp. 4-5) evaluated on **time-averaged** chamber parameters; the four resulting geometries are then simulated and compared. |
| **Unknowns (design)** | Effectively **zero continuous design degrees of freedom**. The whole ramp is the image of four scalars — NPR (= 24.9), γ (= 1.26), throat area A_t, lip radius R_lip (= 13.6 mm) — through Eqs. (5)-(9). The only variations explored are the **discrete label** of the configuration: Case A flat ramp ε = 100 %, Case B flat ramp ε = 87.3 %, Case C isentropic (Angelino) ramp ε = 87.3 %, Case D the same ramp truncated to 40 % (Table 4, p. 5). |
| **Constraints** | Constriction ratio ε = A_t/A_c held at 87.3 % across B/C/D (Table 4); design condition "flow at nozzle exit parallel to chamber axis", imposed as ω_t = ω(M_e) = 50.47° (p. 5, text between Eqs. (7) and (8)); truncation length L_s = 13.60 mm in Case D; ambient pressure fixed, P_a = 0.36 atm (Fig. 15 caption, p. 11). |
| **Flow model** | 3-D unsteady compressible **RANS** (k-ω SST) + **PaSR** turbulence-chemistry, multi-species with mass-conservation equations per species — Eqs. (1)-(4), p. 3, including the viscous stress tensor τ and thermal conduction ∇·(λ∇T). Jet-A surrogate C₁₂H₂₃, reduced mechanism of Ajmani et al. [43]: **21 species, 37 irreversible reactions** (Table 1, p. 3); NASA-polynomial thermo with two temperature ranges (Table 2, p. 4). Finite-rate chemistry, viscous, turbulent — i.e. **strictly outside** our frozen-thermally-perfect inviscid Euler scope. |
| **Solver** | In-house `rhoHLLCFoam` on OpenFOAM; HLLC Godunov convective flux, second-order central viscous discretization, second-order Crank-Nicolson time integration. Cartesian trimmed unstructured mesh, ≈ **12 million cells**, Δ_min = 0.125 mm (chamber) / 0.25 mm (nozzle) / 1.0 mm (far field), Δt ≈ 5 × 10⁻⁹ s, physical duration 1500 μs (3 × 10⁵ steps) — §3.2, p. 6. **No optimizer, no sensitivity, no adjoint, no design loop of any kind.** |
| **Verification** | (i) 1-D planar detonation vs. Chapman-Jouguet: Table 3, p. 5 — U, p, T errors within −1.49 % … +1.18 % over φ = 0.6-1.6; (ii) detonation velocity vs. Austin-Shepherd [47] experiment and NASA CEA [48] (Fig. 2, p. 4); (iii) grid independence on three grids Δ = 0.0625 / 0.125 / 0.25 mm (Fig. 6, p. 6); (iv) Smirnov [52] error-accumulation step bound cited as satisfied. **No verification of the design method itself against any variational reference contour.** |
| **Headline results** | Pressure gain η = (P_c − P₀)/P₀: A −7.4 %, B +8.9 %, C +13.2 %, D +13.1 % (Table 5, p. 10). Thrust F: A 144.11 N, B 150.49 N, C 166.36 N, D 164.15 N (Table 6, p. 12). I_sp: 2384.5 / 2536.1 / 2826.2 / 2792.8 s; nozzle efficiency δ = C_F/C_F,ideal: 81.3 / 81.2 / **85.8** / 84.8 % (Table 7, p. 12). |

### 2.1 The design equations, verbatim in structure (pp. 4-5)

- Eq. (5): `M_e = sqrt( 2/(γ−1) [ (P_c/P_a)^((γ−1)/γ) − 1 ] ) = sqrt( 2/(γ−1) [ NPR^((γ−1)/γ) − 1 ] )`
- Eq. (6): area-Mach relation `A = (A_t/M) sqrt{ [ 2/(γ+1) (1 + (γ−1)/2 M²) ]^((γ+1)/(γ−1)) }`
- Eq. (7): Prandtl-Meyer function `ω = sqrt((γ+1)/(γ−1)) arctan sqrt((γ−1)/(γ+1) (M²−1)) − arctan sqrt(M²−1)`
- Eq. (8): `R = R_lip sqrt( 1 − (A/A_e) · M · sin(α + ω_t − ω) )`
- Eq. (9): `L = (R_lip − R) / tan(α + ω_t − ω)`, with `α = arcsin(1/M)`

Closure condition stated in words on p. 5: *"the inclination of tangent OT at cowl lip (ω_t in Fig. 3b)
should be equal to the deflection angle when the flow accelerates from M = 1.0 to M_e, that is
ω_t = ω(M_e)"*. Design values: γ = 1.26, NPR = 24.9, M_e = 2.69, A_e = 581.08 mm², R_lip = 13.6 mm,
ω_t = 50.47°, R_base = 4.11 mm.

### 2.2 Thrust bookkeeping (pp. 10-11)

- Eq. (16): `F_exit = ṁ W_exit + (P_exit − P_a) A_exit`
- Eq. (17): `F_ramp = ∫_ramp (P_w − P_a) dA_ramp`
- Eq. (18): `F_base = ∫_base (P_w − P_a) dA_base`
- Eq. (19): `F = F_exit + F_ramp + F_base + F_fric`
- Eq. (20)-(23): `I_sp = F/(ṁ_f g₀)`, `C_F = F/(P_c A_t)`, ideal `C_F,ideal`, efficiency `δ = C_F/C_F,ideal`.

Component split (Table 6, p. 12): Case C — F_exit 134.64, F_ramp 34.45, F_base 0, F_fric −2.73 N;
Case D — F_exit 133.18, F_ramp 33.97, **F_base −1.07**, F_fric −1.93 N.

### 2.3 Averaging conventions actually used

- The design inputs are *time-averaged* field quantities (p. 5, §3.1: *"All the input parameters are
  time-averaged values"*).
- Eq. (14), p. 9: `P_c = P_t · (1 + (γ−1)/2 M_t²)^(γ/(γ−1))` where **P_t is the time-averaged static
  pressure at the throat and M_t the time-averaged throat Mach number**, set to M_t = 1.0 because
  *"For all cases in present study, the exhaust flow is congested at nozzle throat which means
  M_t = 1.0"*. So the stagnation pressure of record is `f(⟨p⟩, ⟨M⟩)`, **not** `⟨f(p, M)⟩`.

---

## 3. Hypotheses

### 3.1 Declared

1. Time-averaged RDE plume is quasi-steady and equivalent to a classic axisymmetric under-expanded
   supersonic jet (p. 5, §3.1, citing [49-51]; p. 2 citing Jourdaine [26]).
2. Between throat and exit the expansion is **isentropic** and the fan is a **single centered
   Prandtl-Meyer fan at the cowl lip** (p. 4, §3: *"the expansion process from nozzle throat to exit
   is assumed as isentropic axis centered, isentropic supersonic flow. A series of lip centered,
   isentropic expansion waves occur at the cowl lip of nozzle"*).
3. **Constant γ = 1.26** for all design and reduction formulas (p. 10: *"The specific heat ratio of
   detonation products is about γ = 1.26"*; p. 5: *"According to formulas from Eq. (5) to (9) with
   γ = 1.26"*).
4. Choked throat, M_t = 1.0, in all four cases (p. 9).
5. Ambient pressure constant, P_a = 0.36 atm.
6. Premixed Jet-A/air injection through converging micro-nozzles with a three-branch inlet model
   (no injection / subsonic / sonic), Eqs. (10)-(13), p. 7; inlet P₀ = 8 atm, T₀ = 1000 K.
7. Reduced 21-species / 37-reaction kinetics is adequate for Jet-A/air detonation (validated §2.2).

### 3.2 Undeclared but necessary

8. **The Angelino construction is the "optimal thrust" contour.** Asserted, never proved and never
   compared to any variational contour. The intro states as fact (p. 2): *"In traditional rocket
   engine with an annular combustor, a circular aerospike nozzle used for optimal thrust is composed
   by two parts: an inward-bend cowl lip and a curved isentropic ramp surface."* No optimality
   argument, no reference to any optimal-nozzle theory.
9. **Commutation of the nonlinear design map with time-averaging.** Eqs. (5)-(9) and (14) are
   nonlinear in (p, M); applying them to time-averaged inputs silently assumes the Jensen gap is
   negligible. Never stated, never bounded.
10. **Phase-independence of the inflow profile shape.** The 1-D reduction requires the chamber-exit
    state to be characterized by scalars; the paper's own §4.4 conclusion acknowledges this fails
    ("non-uniformity of exhaust flow at chamber exit on a time slice"), but the design method never
    accounts for it.
11. **Uniform, purely axial-plus-radial (swirl-free) treatment in the design.** The 1-D relations carry
    no azimuthal velocity component; the simulated field manifestly has one (rotating wave). Swirl is
    never mentioned, never measured, never debited.
12. **Steady-jet equivalence of the mean is sufficient for a *design* criterion**, not merely for
    *performance analysis*. Jourdaine [26], the cited authority, supports only the weaker statement
    (*"sufficient for thrust performance analysis"*, p. 2); the paper upgrades it to a design
    principle without argument.
13. **Comparability of the four cases at fixed ṁ is not enforced** — Table 7 shows ṁ_f varying
    (6.17 / 6.06 / 6.01 / 6.00 g/s) across cases, so the I_sp comparison mixes a mass-flow change with
    the geometry change. No matched-ṁ control.
14. Perfect-gas closed forms (Eqs. (5)-(9), (14), (22)) with γ = 1.26 coexist with a
    variable-c_p NASA-polynomial CFD (Table 2). The inconsistency is never reconciled.

---

## 4. Findings — three-level comparison

### TEORICO

**F1 — CORRECTION (ALTA). The list rationale for this file is factually wrong: there is no
optimizer in this paper.**
The paper contains **no genetic algorithm, no gradient-based optimization, no multi-objective
formulation, no parabolic spike parameterization, and no design variables**. Evidence: full-text
extraction of all 14 pages (58 454 chars) returns **zero** occurrences of `genetic`, `gradient`,
`objective`, `Pareto`, `surrogate`, `Kriging`, `design variable`, `Bezier`, `spline`, `parabol`,
`adjoint`, `optimality`. The stem `optimiz` occurs exactly **5 times**, all rhetorical: the title;
the abstract (*"To optimize the nozzle configuration for thrust generation, the current work
investigates the performance of RDE combined with various types of aerospike nozzles"*, p. 1); the
intro (*"the aerospike nozzles adopted in above researches are not optimally designed"*, p. 2);
and twice in the conclusions (*"compared to the unoptimized nozzle (Case A/B)"*; *"the nozzle
structures will be further optimized and verified in RDE flight tests"*, p. 12). The word
"optimization" in the title denotes a **four-point discrete comparison** (Table 4, p. 5), i.e. a
configuration trade study.
*Consequence for the record:* the filename
`liu_2022_aerospike_rde_ga_gradient_optimization.pdf` and any litmap row crediting this paper as
"the only formal optimizer of the RDE corpus" must be **corrected**. Either the intended
GA+gradient paper is a *different* document not on disk, or the attribution was never verified.
**Claim #8 (empty niche) is strengthened, not threatened**, by this correction.

**F2 — GAP-CONFIRMS (ALTA), claim #7 / D2 gap G3.** The averaging is justified **a posteriori and
empirically**, never variationally. The entire warrant is p. 5, §3.1: *"the time-averaged plume
field is quasi-steady, which is similar to a classic axis-symmetric under-expanded supersonic jet
as shown in Ref. [49-51]. Therefore, the traditional aerospike nozzle design method could still be
employed with the time-averaged parameters"*; and its upstream source, p. 2: *"Jourdaine et al.
[26] showed that the time-averaged exhaust plume field of RDE was similar to the axis-symmetric
supersonic jets ... The averaged solution of RDE plume field was sufficient for thrust performance
analysis. This suggests that the traditional nozzle design methods in rocket engine could be
employed with the time-averaged parameters for RDE nozzle design."* The chain is
*observation → similarity → therefore design at the mean*. There is **no measure**, no objective
functional over a family of inflow states, no stationarity condition, no counterpart of our (\*\*')
transversality. The paper even advertises this as its own contribution: *"The applicability of
one-dimensional isentropic relationships used in traditional aerospike nozzle design with the
time-averaged parameters of highly transient flow in RDE has been proved"* (p. 2) — where "proved"
means "two configurations were simulated and performed well". **G3 is real and this paper is
positive evidence for it**, from the most recent journal-grade RDE aerospike design paper in the
corpus.

**F3 — GAP-CONFIRMS (ALTA), claim #2 / T-T3 hypothesis set.** The paper *practises* the T-T3
conclusion (design the fixed wall at the mean chamber condition) without any of its hypotheses, and
then **measures the penalty and names its cause**. p. 12, §4.4: *"The maximum value of nozzle
efficiency is δ = 85.8 % in Case C. The efficiency loss may be caused by the high frequency nature
of rotating detonation waves. **The non-uniformity of exhaust flow at chamber exit on a time slice
makes the nozzle deviate from the design point deduced in terms of the time-averaged parameters**
which causes the decrease of δ. Besides, the irreversible processes caused by the oblique shock
waves extending outside the combustor will also reduce the nozzle efficiency. These two factors ...
cannot be cleaned."* Read against T-T3: the deviation they observe is precisely a **failure of H3**
(phase-independent nondimensional inflow shape — here the azimuthal non-uniformity on a time slice)
and of the constant-γ / calorically-perfect footing of Lemma B_T3. This is an *external, independent*
demonstration that the collapse theorem's hypothesis set is the load-bearing part of T-T3, and that
"design at the mean" is a heuristic with a measurable 14.2 % gap in a real RDE — exactly the regime
our T-T3-MAP breaker list is built for. It does **not** falsify T-T3 (their instance satisfies
neither H1, H2', H3, nor the inviscid closure).

**F4 — CONTAINED (ALTA).** The paper's design problem is a **zero-DOF restriction of (P)**: fixed
topology sector (plug/aerospike with inward-bend cowl lip), fixed ε and L, constant P_a, choked feed,
supersonic full-flowing exit, and an admissible set of **cardinality four** (Table 4, p. 5:
Cases A/B/C/D). Under H2' (fixed wall, full-flowing, supersonic exit), constant P_a = 0.36 atm,
H1 (single frozen γ = 1.26 — which they impose by fiat), and the collapse of the measure to the
point mass at ⟨·⟩, our J[S] = ∫F dμ degenerates to F[S; ⟨P_c⟩] and their design rule *is* the T-T3
corollary. Their contour is then the classical construction at that single condition. The
containment is exact **at the design-rule level**; it does **not** extend to their evaluation model
(viscous, turbulent, finite-rate, with F_fric in the functional), which is a declared structural
non-containment of our Route A (brief §(D)18, boundary-layer-terms-in-the-functional, §6(c)).

**F5 — GAP-CONFIRMS (ALTA), choking advisory.** Choking is *asserted from observation and then used
as a closure*: p. 9, *"For all cases in present study, the exhaust flow is congested at nozzle throat
which means M_t = 1.0"*, immediately feeding Eq. (14) to produce the pressure-gain numbers of
Table 5 — including for **Case A, which has ε = 100 %, i.e. no geometric constriction at all**
(p. 7: *"The exhaust flow is congested at nozzle throat in both cases with Mach number at throat
M_t = 1.0"*, of Cases A and B). This is a textbook instance of the pattern recorded in
`ADVISORY_rde_choking_2026-08-11`: choking is never a derived result nor a monitored margin, it is
an **assumption folded into the reduction**, and the headline pressure-gain figure (13.2 %) inherits
it. Our two-regime contract and the L4 default (every patch axially supersonic *with margin*) are
confirmed as the discriminating discipline.

**F6 — THREAT (MEDIA), value-proposition level, claims #7/#8 as *motivation*.** Honest statement of
the referee risk: a closed-form 1-D design at time-averaged parameters, costing essentially zero
design effort, delivers **+15.4 % thrust and +18.5 % I_sp over the flat-conical baseline and reaches
δ = 85.8 %** of ideal (Tables 6-7, p. 12). A hostile reader can ask what a certified cycle-averaged
variational contour buys over that. **Pre-loaded answer, from the paper itself:** (i) the baseline
is a *straight conical flat ramp* (Cases A/B), never a Rao/variational contour, so the paper measures
the **conical-vs-Angelino** gap, not the **Angelino-vs-optimal** gap — the quantity that matters to
us is not measured anywhere in this paper; (ii) the residual 14.2 % is declared by the authors to
"[be] caused by the inherent characteristics of rotating detonation waves and cannot be cleaned"
(p. 12) — an *assertion*, with no bound, no mechanism decomposition and no attempt at a design that
accounts for the non-uniformity, which is exactly the object of (P); (iii) their own Case C ramp
carries a below-ambient drag tail (see F8), so the contour is demonstrably not stationary. The threat
is to *rhetoric*, not to any theorem.

### FORMALE

**F7 — CONTAINED (ALTA), degenerate corner of Route A.** Eqs. (5)-(9) + the closure ω_t = ω(M_e) are
the Angelino [35] construction: the ramp is the **streamline of a single centered Prandtl-Meyer fan
issuing from the cowl lip**, with the lip-to-ramp straight characteristic drawn explicitly in
Fig. 3b (p. 5, labelled *"Straight characteristic line"*), and the endpoint fixed by requiring the
exit flow to be axial. In Route-A language this is the maximally degenerate member: γ = const,
homentropic-homoenergetic, **one** characteristic family, the "control surface" reduced to the single
straight lip characteristic, and — decisively — **no transversality condition of any kind**. Our
augmented density f = f₁ + λ₂f₂ⁱ + λ₃f₃ and its free-endpoint condition
(f₁ + λ₂f₂ⁱ + λ₃f₃)|_E = 0 (CSTR_PB in the plug case) have **no counterpart**: the endpoint is
pinned by the kinematic condition ω_t = ω(M_e), not by stationarity. Containment holds under
γ = const + homentropic + single-fan + fixed (ε, L) + M_t = 1; the paper's construction is then the
"design surface" object our EQ-v2 Direction A discusses, not a KKT point.

**F8 — GAP-CONFIRMS (ALTA), claim #16 / corner conditions.** The paper supplies **measured evidence
that its own contour violates the classical endpoint condition**. p. 11: *"On ramp surface, anyplace
where the pressure is lower than ambient pressure will produce drag for the engine. In Case B, P_w is
less than P_a at axial position z > 0.72 cm causing a total drag of −5.54 N. In Case C, P_w is less
than P_a at z > 2.0 cm causing a total drag of −0.095 N."* Figs. 15a-b (p. 11) plot P_w against the
dashed P_a line and show the crossing explicitly. A plug contour satisfying CSTR_PB —
(p − p_a) + ½ρW² sin(2θ) tan α = 0 at the free endpoint, with the base-pressure mirror — cannot carry
an extended p < p_a tail at first order; the design has simply run the PM fan to M_e and stopped.
This is a clean corpus datum that **the 1-D isentropic RDE aerospike design is not variationally
stationary**, and that the discrepancy is *measurable in newtons on a published case*. It supports
claim #16's spirit (the endpoint condition is where the naive constructions fail) and reinforces
#8's empty niche at the formal level.

**F9 — ADOPT (MEDIA), convention register for T-T3-MAP / T-T3-SI.** Eq. (14), p. 9:
`P_c = P_t (1 + (γ−1)/2 M_t²)^(γ/(γ−1))` with **P_t = time-averaged static pressure at the throat and
M_t = time-averaged throat Mach**. This is a *state-averaged stagnation reconstruction*:
`P_c := f(⟨p⟩, ⟨M⟩)` rather than `⟨f(p, M)⟩` — a distinct, named, and widely used convention whose
Jensen gap is never bounded here, and which propagates into **every** headline number of the paper
(NPR = 24.9 → M_e = 2.69 → the whole contour; η = 13.2 %; C_F = F/(P_c A_t); δ = C_F/C_F,ideal).
*Where it grafts:* add "state-averaged stagnation reconstruction (Liu 2022 Eq. (14))" as an explicit
row in the declared convention list exercised by **PROTOCOL T3-CONTROL** and by the **T-T3-SI**
convention-spread measurement, alongside matched-ṁ and matched-⟨p⟩. It gives us a third, externally
sourced convention whose spread we can measure on certified tier-1 data — turning claim #3's
falsifier into a test with a real corpus convention rather than only self-generated ones.

**F10 — CORRECTION (MEDIA), internal γ inconsistency of the E4 class.** The paper runs a
variable-c_p NASA-polynomial thermodynamics in the CFD (Table 2, p. 4: seven coefficients on two
temperature ranges for C₁₂H₂₃) while every design and reduction closed form — Eqs. (5)-(9), (14),
(22) — is evaluated with a single frozen γ = 1.26 (pp. 5, 10). This is exactly the boundary our **E4**
names: the γ = const dependence lives in the *closed-form corner↔ε bijection*, not in the governing
equations. The paper never reconciles the two, never states which γ it means (frozen? equilibrium?
mass-weighted?), and never bounds the induced contour error. *Record use:* this is a corpus-side
instance justifying our standing directive that γ = const may appear only as a declared oracle,
never load-bearing — and it is a concrete external example to cite when defending E4's framing.

### ALGORITMICO

**F11 — GAP-CONFIRMS (ALTA), claim #8 (empty niche).** At the algorithmic level the paper's design
pipeline is: *evaluate four closed-form geometries → run four 3-D unsteady CFD cases → compare
tables*. There is **no design loop, no sensitivity, no derivative, no parameterization, no
convergence criterion on any design metric**. Twelve million cells and 3 × 10⁵ time steps per case
(§3.2, p. 6) are spent entirely on **analysis**, not on **design**. Confirmation is structural, not
merely lexical: the paper has no §"optimization", the geometry table (Table 4) has four rows fixed
before any simulation, and the conclusions defer optimization to future experiments (*"the nozzle
structures will be further optimized and verified in RDE flight tests"*, p. 12). Combined with F1,
this is strong evidence that in 2022 the RDE aerospike literature had **no formal shape optimizer at
all** — the niche "keep the variational MoC formulation and swap in a modern optimizer" is not merely
unoccupied, the weaker niche "run *any* optimizer on an RDE nozzle contour" is unoccupied here too.

**F12 — ADOPT (ALTA), T-T4 / PB-2 diagnostics and an external base-pressure datum.** Two adoptable
items, both with numbers:
(a) **Sixteen-segment ramp-thrust decomposition.** Fig. 15c-d, p. 11: *"The ramp domain is divided
into sixteen segments to get the thrust distribution"*, with per-segment F_ramp bars and the
integrated conclusion *"almost all of the F_ramp is provided by the first 40 % of the aerospike"*
(gross ramp thrust 34.45 N in Case C, 7.24 N in Case B). This is the executable, *empirical*
counterpart of **T-T4's monotone-then-flat structure in the plug extension l** — the saturation our
theorem states as "exactly constant for l ≥ l(ξ)" is here *measured* as a thrust-density profile.
*Where it grafts:* adopt the segmented ramp-thrust density as a **standard Verdict diagnostic** for
every PB-2 / T-T4 instance, reported alongside the corner residual; it makes the nesting structure
visible per-instance and is cheap on our fitted march (integrate (p − p_a) per wall panel, which we
already compute for the Hadamard density G_ξ).
(b) **A quantified T-T4 sharpness datum.** Case D (40 % truncation) loses only **1.2 % of I_sp**
(2826.2 → 2792.8 s, Table 7) and 2.21 N of thrust (166.36 → 164.15 N, Table 6), while paying an
explicit **base drag F_base = −1.07 N** on a base of radius R_base = 4.11 mm (*"the average pressure
on base surface is about 0.16 atm"*, p. 12, vs. P_a = 0.36 atm). T-T4's sharpness clause says a base
-pressure model breaks the nesting and forces the genuinely averaged corner condition; here is an
external, published, order-of-magnitude quantification of that breaker (base drag ≈ 0.65 % of total
thrust, and the base pressure sits at 44 % of ambient). *Where it grafts:* cite as the empirical
anchor for the PB-2 base-pressure model's magnitude, and as the "the breaker is real but small at
40 % truncation" calibration point in the D-doc T-T4 sharpness remark.

---

## 5. Bibliography inspection (record datum)

58 references, pp. 13-14, read in full.

**Classical optimal-nozzle line — ALMOST ENTIRELY ABSENT.**
- **Rao: ABSENT.** Zero occurrences of "Rao" in the full text (verified by extraction).
- **Guderley: ABSENT. Hantsch: ABSENT. Shmyglevskii: ABSENT. Kraiko: ABSENT. Hoffman: ABSENT.**
  (Caution against a false positive: "Hoke" appears four times — J. Hoke, the AFRL RDE
  experimentalist, in refs [19], [25], [30]; this is not Hoffman.)
- The **only** two nozzle-theory references in the whole paper are:
  - **[35] G. Angelino, "Approximate method for plug nozzle design", AIAA J. 2 (10) (1964)
    1834-1835** — the sole design-method source, and, as its own title says, *approximate*;
  - **[36] G. Hagemann, H. Immich, T.V. Nguyen, G.E. Dumnov, "Advanced rocket nozzles",
    J. Propuls. Power 14 (5) (1998) 620-634** — a survey, cited for "the aerospike nozzle design
    method has been fully-developed based on the theory of one-dimensional isentropic steady flow".

**Modern adjoint / shape-optimization line — ENTIRELY ABSENT.**
No Lions, no Pironneau, no Jameson, no Giles, no Ulbrich, no Lozano, no Nadarajah, no Zahr/Persson,
no Schmidt/Schulz. There is **not a single optimization-theory or sensitivity-analysis reference in
the paper**, of any school.

**RDE-side references overlapping our corpus (already held or worth holding):**
[25] Fotia, Kaemming, Codoni, Hoke, Schauer, AIAA SciTech 2019 (aerospike plug-nozzle thrust
sensitivity); [26] Jourdaine, Tsuboi, Ozawa, Kojima, Hayashi, Proc. Combust. Inst. 37 (3) (2019)
3443-3451; [27] Goto et al., J. Propuls. Power 35 (1) (2019) 213-223; **[28] Harroun, Heister, Ruf,
J. Propuls. Power (2021) 1-14** (already on disk); [30] Fotia, Schauer, Kaemming, Hoke,
J. Propuls. Power 32 (5) (2016) 674-681; **[33] Miki, Paxson, Perkins, Yungster, AIAA Propulsion and
Energy 2020, p. 3872** (already on disk as `miki_2020_rde_nozzle_design_methodology.pdf`);
[34] Kurita, Jourdaine, Tsuboi, Ozawa, Hayashi, Kojima, AIAA SciTech 2020, p. 0688;
[52] Smirnov et al., Acta Astronaut. 117 (2015) 338-355 (error-accumulation bound);
[56] Bach, Stathopoulos, Paschereit, Bohon, Combustion and Flame 217 (2020) 21-36;
[57] Ruf & McConaughey, AIAA 97-3218 (aerospike plume physics); [58] Verma,
J. Propuls. Power 25 (3) (2009) 783-791 (conical aerospike with freestream).

**New litmap candidate identified by this read:**
**[39] Y. Zhu, K. Wang, Z. Wang, M. Zhao, Z. Jiao, Y. Wang, W. Fan, "Study on the performance of a
rotating detonation engine with different aerospike nozzles", Aerosp. Sci. Technol. 107 (2020)
106338** — cited on p. 2 as the *precedent* for the very method Liu et al. use: *"Zhu et al. [39] has
used the one-dimensional isentropic relations based on time-averaged parameters for aerospike nozzle
design in RDE experiments."* If we want the earliest corpus instance of "design the RDE plug at the
time-averaged condition", Zhu 2020 — not Liu 2022 — is the citation to chase. **Not on disk.**

---

## 6. Bottom line for the program

1. **This paper is not an optimizer paper.** The record must be corrected (F1). Whatever
   GA + gradient + five-objective aerospike RDE study motivated the entry in the reading list, it is
   **not** the file on disk.
2. It is, however, a **high-quality confirming witness** for three of our gaps: the averaging is
   justified a posteriori (F2), the design-at-the-mean heuristic is used without hypotheses and its
   penalty is measured but not explained (F3), choking is assumed rather than certified (F5).
3. Its formal content is the **Angelino degenerate corner of Route A** with **no transversality
   condition** (F7), and it hands us a measured violation of the classical endpoint condition on its
   own best case (F8).
4. Three things to take: the **state-averaged stagnation convention** into the T3-CONTROL convention
   register (F9), the **segmented ramp-thrust density** as a Verdict diagnostic (F12a), and the
   **base-drag / truncation calibration numbers** as an external anchor for the T-T4 sharpness clause
   and for PB-2 (F12b).
5. The one genuine pressure on us is rhetorical (F6): a zero-effort 1-D design reaches δ = 85.8 %.
   The rebuttal is already inside the paper — its baseline is a cone, not an optimal contour, and its
   own Case C carries a below-ambient drag tail.
