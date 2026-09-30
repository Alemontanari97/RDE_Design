# Stage A — De-novo derivation tree, LENS = hyperbolic conservation laws / supersonic nozzle gas dynamics

Inputs read: `PROBLEM_STATEMENT_agnostic.md`, `DERIVER_BRIEF_agnostic.md` (nothing else).
Knowledge tags: [KNOWLEDGE: author/year, depth]. Rigor classes: THEOREM / THEOREM* (under declared closure) / 
SCHEMA / CONJECTURE / PRACTICE.
Notation: f = wave passage frequency at a fixed station, n = wave count, ω = 2πf/n = angular speed of the 
rotating pattern; (x,r,θ) cylindrical; φ = θ − ωt; a(T) = frozen sound speed of the thermally-perfect 
mixture; u = (u_x,u_r,u_θ) absolute velocity; w_θ = u_θ − ωr relative azimuthal velocity; Pa ambient; 
F̄ = time-mean axial thrust; ṁ̄ = time-mean mass flow.

---

## 0. Lens theses (structural facts this lens contributes; all used below)

- **L1 (traveling-wave reduction, THEOREM under the single-mode pin).** If the interface data are a pure 
rotating wave, Q(r,θ,t) = Q(r,θ−ωt), and the nozzle is fixed and axisymmetric, then any solution of the 
form U(x,r,θ−ωt) satisfies the STEADY system in (x,r,φ):
  ∂_x F_x + (1/r)∂_r(r F_r) + (1/r)∂_φ(F_φ − ωr U) + S_geom(U) = 0,
  with absolute-velocity fluxes and the ordinary cylindrical geometric sources (r- and θ-momentum only). The 
unsteady axisymmetric-nozzle problem with rotating inflow is a steady 3D problem. Time means = φ-means 
(ergodic identity; the limit in (O-a) exists, no liminf/limsup needed on the pin). Caveat (falsifiable): the 
unsteady problem may also have non-traveling-wave solutions (instability of the rotating pattern, mode 
change) — that is exactly the pin monitor (SP7, SP5).
- **L2 (thrust is a steady boundary functional, THEOREM under L1).** The axial-momentum equation has no 
geometric and no rotating-frame source; hence the φ-mean axial momentum flux (thrust) is the same through 
EVERY enclosing surface, and F̄ = φ-mean wall pressure force + interface momentum flux. The unsteady 
adjoint (checkpointing, periodic adjoint) is NOT needed on the pin: a steady 3D adjoint delivers dF̄/dS.
- **L3 (rothalpy; unsteady energy redistribution).** Along rotating-frame streamlines h₀ − ωr u_θ is 
conserved (Euler turbine identity): the rotating pressure field exchanges stagnation enthalpy BETWEEN 
particles (no net exchange: the φ-mean total-enthalpy flux is conserved because the wall is fixed). Since 
u_ideal ∝ √(h₀ − h(s,Pa)) is concave in h₀, redistribution is a pure LOSS (Jensen) of relative size 
≈ ε²/8 with ε = spread of h₀/mean h₀. Scaling: ε ≈ ωr Δu_θ/h₀; with ωr ~ 2–3 km/s, Δu_θ 
~ 0.2–0.3 km/s, h₀ ~ 5 MJ/kg → ε ~ 0.1–0.2 → loss 0.15–0.5 %. This is one of the only two 
nozzle-side loss terms that are unsteady-SPECIFIC (the other is the entropy production of the data-borne 
oblique shock reflecting in the nozzle, L7). Dry consequence: the unsteady-attributable pool is of the order 
of the thrust-stand band — Q0 at objective (O-a) is intrinsically MARGINAL and must be MEASURED with a 
difference-resolving protocol (SP8/SP9), never argued.
- **L4 (ceiling bound, THEOREM* — hypotheses H1 Euler frozen thermally-perfect; H2 entropy nondecreasing 
along particle paths; H3 pin L1; H4 fixed impermeable wall; H5 an enclosing exit surface exists on which u_x 
≥ a at every phase, with, on overexpanded portions, u_x ≥ a(Pa)ρ(Pa)/ρ(p)).** Pointwise lemma: for a 
particle crossing an axial plane with u_x ≥ a, the thrust per unit mass flow u_x + (p−Pa)/(ρu_x) ≤ 
u_id(h₀,s) := √(2(h₀ − h(s,Pa))) (proof: for p > Pa, h(s,p) − h(s,Pa) − (p−Pa)/ρ = ∫∫ 
dp'dp''/(ρa)² ≥ (p−Pa)²/(2ρ²a²) because ρa increases along an isentrope with p; then (u_x + 
B/u_x)² ≤ u_x² + 2ΔH iff ΔH − B ≥ B²/(2u_x²), which holds for u_x ≥ a; the case p < Pa needs 
the stronger condition of H5). Then Jensen in h₀ (concave) and monotonicity in s give
  **F̄ ≤ J_ceil := ṁ̄ · √(2(⟨h₀⟩_ṁ − h(s_min, Pa)))**, evaluable from class-B data in 
seconds. J_ceil − J[S] decomposes EXACTLY into computable pointwise defects on the evaluated field: 
expansion (p≠Pa), divergence (u_x<|u|), Jensen (h₀ spread), entropy (s>s_min), evaluated on the exit 
surface. This is the (R-i) gap certificate and the loss budget.
- **L5 (type classification / marching legality indicators).** The steady system of L1 is hyperbolic in x 
where u_x > a (space-marching legal; sequence of 2D (r,θ) problems, periodicity in θ automatic) and 
hyperbolic in φ where |u_θ − ωr| > a (θ-marching legal; a period-map fixed-point problem, cost of a 2D 
unsteady solve). Near the axis r < r* := (a + |u_θ|)/ω the φ-direction is NOT time-like (the pattern is 
subsonic relative to the gas: azimuthal communication smears the wave). Numbers: ωr ≈ D_wave at the 
annulus radius (1.8–2.5 km/s) vs a ≈ 1.0–1.3 km/s → r*/R_annulus ≈ 0.4–0.7: a full bell (flow 
reaching the axis) always contains a non-θ-hyperbolic core; an annular (plug / shrouded-plug / E-D) nozzle 
with r_min > r* is fully θ-hyperbolic. Both indicators are computable from data + a first solve and are the 
NON-HARDCODED solver selectors.
- **L6 (characteristic-count audit of the interface, THEOREM, textbook).** On Γ_d the number of boundary 
conditions equals the number of incoming characteristics: 5 where u_n > a, 4 where 0 < u_n < a [KNOWLEDGE: 
Hirsch 1990, vol. 2, full]. Class-B data (M, angle, s, swirl, i.e. 5 quantities) OVER-DETERMINE any 
axially-subsonic patch: one quantity (the outgoing acoustic invariant, in practice p) must be released to the 
interior. Causal separation (§3) is a THEOREM only where u_n > a on Γ_d at every phase; elsewhere it is 
violated unless an impedance closure (class G) is supplied. The audit = the per-phase, per-point count, with 
loud reject of over-determined data.
- **L7 (discontinuity inventory).** RDE exhaust carries (i) the oblique shock trailing the detonation 
(data-borne, crosses Γ_d, steady in the rotating frame, its trajectory design-dependent) [KNOWLEDGE: Schwer 
& Kailasanath 2011, abstract]; (ii) contact/slip surfaces (entropy/composition stratification, linearly 
degenerate); (iii) for plug-type solids, the free plume boundary (p = Pa streamsurface); (iv) design-induced 
internal shocks (characteristic coalescence) — to be EXCLUDED by constraint in the design class, detected 
by the same-family characteristic-spacing indicator. Design derivatives must pass through (i)–(iii) 
explicitly (SP3).
- **L8 (2D-slice defect is a measurement, not an estimate).** The "axisymmetric unsteady slice" (drop the 
θ-flux) solves L1 with ∂_φ(F_φ − ωrU) replaced by −ω∂_φU: its defect in the 3D steady equations 
is r_θ = (1/r)∂_φF_φ evaluated on the slice solution (exact residual, computable); the first-order 
effect on F̄ is ⟨λ, r_θ⟩ with the 3D adjoint λ; the second-order remainder is checked by one 3D 
solve. The slice neglects the azimuthal pressure gradient's generation of swirl (the L3 mechanism), so it is 
uncontrolled for O(1) cycle amplitude unless measured.

---

## Level 0 — SP0 STRATEGIES (open enumeration; tuples = objective / time / space / solver+information / 
search+guarantee / decisive result)

Fields per strategy: Q answered; cost; generality; pins needed / relaxable; falsifier; time-to-number; rank; 
ABANDON measurement; pre-registered decisive result.

### S1 — Practice of today: steady design at a representative mean state, unsteady check afterwards
Tuple: (O-a proxy: steady thrust at a mean state / time collapsed to ONE mixed-out state / 2D axisymmetric 
steady / MoC or steady Euler, Rao-type variational contour [KNOWLEDGE: Rao 1958, full] with legacy oracle / 
1–2 parameter family (length, exit angle) or none, PRACTICE guarantee / decisive: the unsteady check "does 
not show a problem").
Q: a narrowing (steady surrogate performance). Cost: days; no new theory. Generality: bell native; plug via 
MoC free-boundary [KNOWLEDGE: Zucrow & Hoffman 1977, full]; data class A–C (needs only a mean state). Pins 
needed: none beyond frozen gas; relaxable: single-mode (uses only means). Falsifier: exact-on-pin evaluation 
(L1) of its design shows a loss budget with unsteady-specific terms > band. Time-to-number: 1 session. Rank: 
baseline (comparator, SP-CARM), rank 9 as an answer to Q0. ABANDON: a measured J_true[S1] below J_true of any 
other design by > 1 % of F. Decisive: none of its own — it IS the control.

### S2 — Conservative cycle-averaged surrogate inflow → steady design; exact-on-pin evaluation (hybrid)
Tuple: (O-a / time collapsed to the FLUX-averaged state (mass, momentum, energy fluxes matched) / 2D 
axisymmetric steady design, 3D rotating-steady evaluation / steady adjoint / gradient local optimum, PRACTICE 
for the surrogate step / decisive: J_true[S2] − J_true[S1-tuned]).
Q: narrowing (is a better single state enough?). Dry argument: a flux-averaged state reproduces the linear 
conserved fluxes but the thrust map is nonlinear; the surrogate error is a quadratic form in the cycle 
variance, O((Δp/p)²) with Δp/p = O(1) in RDE exhaust → uncontrolled; only measurement (via L8-type 
defect) can rescue it. Cost: low. Generality: all configs; classes A–C. Pins: single-mode not needed. 
Falsifier: surrogate-predicted J differs from exact J by > band on the same design. Time: 2 sessions. Rank 6. 
ABANDON: |J_surrogate − J_exact| > 1 % F on S1's design. Decisive: gain over S1-tuned on the exact 
evaluator, ≥ band.

### S3 — Quasi-steady phase ensemble (small-Strouhal limit): duty-weighted steady snapshots, per-snapshot 
adjoint
Tuple: (O-a / time = K frozen phases with weights w_k = Δφ_k/2π; residence ratio St = fL/u must be ≪ 1 / 
2D axisymmetric steady per phase / steady MoC or FV + adjoint per phase, summed / gradient SQP, local KKT / 
decisive: J_true gain over S1-tuned, with the O(St) reduction error measured).
Q: Q0 restricted to St ≪ 1. Dry estimate: the neglected term ∂_tU vs ∂_xF_x scales as St × (cycle 
amplitude); error in J = O(St·A). Measurement: since f is a PARAMETER, run the exact evaluator at f, 2f, 4f 
and fit the exponent (rejector: exponent ≠ 1 kills the reduction). Cost: K× a steady solve; K derived from 
the waveform's resolution (K such that the trapezoidal φ-quadrature error of the flux integral < band/4, by 
Richardson in K). Generality: all configs; classes B–F (weights). Pins: single-mode used only through 
weights. Falsifier: the fitted exponent test; or St measured > 0.3 at the instance. Time: 3 sessions. Rank 3 
(the natural DESIGN-LOOP engine when St is small; must be paired with an exact evaluator). ABANDON: measured 
St > 0.3 or J error scaling exponent < 0.8. Decisive: as S11.

### S4 — Rotating-frame steady 3D Euler (exact on pin) for BOTH design and evaluation
Tuple: (O-a / time = exact via L1 / 3D steady in (x,r,φ) / x-marching where u_x > a, θ-marching where 
|w_θ| > a, 3D pseudo-time elsewhere; discrete adjoint of the marching scheme (backward marching) / gradient 
trust-region SQP; local KKT + L4 gap certificate / decisive: gain over S1-tuned, exact evaluator, plus 
fraction of the L4 gap recovered).
Q: Q0 on the pin, exactly. Cost: solver build 2–3 sessions; per solve: marching = N_x·N_r·N_θ (minutes 
in vectorized numpy for 200×100×200 = 4·10⁶ cells if fully marching); pseudo-time 3D on the same grid 
≈ 10³–10⁴ sweeps → hours per solve → design loop exceeds the 3-h window unless the marching branch 
applies. Generality: all configs (annular configs are the cheap ones, L5); classes B–G. Pins NEEDED: 
single-mode (L1 is void for counter-rotating pairs — a sum of two traveling waves is steady in no frame); 
frozen gas (variable γ native: a(T), h(T) enter only through the EOS calls in flux Jacobians and 
compatibility relations [KNOWLEDGE: Zucrow & Hoffman, full]). Falsifier: a time-accurate 3D run started from 
the steady rotating solution drifts (pattern unstable) → pin fails for that design. Time: 5–7 sessions. 
Rank 2 (the EVALUATOR of record; too expensive as the design engine when the marching branch is not legal). 
ABANDON: time-accurate drift > band on the practice design (then no pinned answer exists). Decisive: as S11.

### S5 — Time-spectral / harmonic-balance in the absolute frame
Tuple: (O-a / time = K harmonics of f [KNOWLEDGE: Hall, Thomas & Clark 2002, full; McMullen & Jameson 2006, 
abstract] / 2D slice or 3D / coupled K-harmonic steady adjoint / gradient local / decisive: gain over 
S1-tuned).
Dry rejection on this lens: the waveform carries a discontinuity (the oblique shock crosses Γ_d): Fourier 
truncation error is O(1/K) in L¹ and O(1) in L∞ (Gibbs) at the front; K needed for band-level flux 
accuracy ~ 10²; the coupled system then costs ≥ the θ-marching of S4, which is exact. Also, on the pin, 
S5 in 3D IS S4 in a Fourier basis in φ — nothing gained. Rank 8. Falsifier/ABANDON: K-convergence of F̄ 
slower than K⁻¹ measured. Time: 4 sessions. Pins: single-mode (periodicity). Decisive: as S11 but not 
recommended.

### S6 — Full unsteady 3D time-accurate solver with unsteady adjoint (checkpointed) — the horizon
Tuple: (O-a / time-accurate over ≥ several periods, periodic adjoint or long-window adjoint [KNOWLEDGE: 
Griewank & Walther 2000 revolve, abstract] / 3D / shock-capturing FV, adjoint / gradient local / decisive: 
same gain measured with no reduction at all).
Q: Q0 without the pin. Cost: HPC-class (10⁷ cells × 10⁵ steps × checkpointed adjoint); NOT executable 
on the stated budget; theory clean. Generality: everything incl. multi-mode (class F relaxations). Pins: none 
needed. Falsifier: n/a (it is the reference). Time: > 10 sessions + HPC. Rank 7 as a road; rank 1 as the 
horizon anchor: ONE short time-accurate 3D run (no adjoint) at the decisive design point is affordable 
(hours) and is used as the pin monitor and cross-code anchor (SP8/SP9). ABANDON: n/a. Decisive: the drift 
test of S4.

### S7 — Derivative-free / surrogate-assisted search on a low-dimensional contour family, exact evaluation
Tuple: (O-a / exact via L1 / 3D rotating-steady / no derivatives; Bayesian optimization or CMA-ES on 5–10 
parameters / global-in-family heuristic, no KKT / decisive: gain over S1-tuned).
Cost: ~10²–10³ exact evaluations → only affordable in the marching branch. Generality: any config; no 
discontinuity-derivative issue (the honest attraction of this road). Guarantee: none beyond sampling; the L4 
gap still applies. Rank 5 (a fallback if SP3 fails its rejectable tests; also the natural engine for the 
1–2 parameter TUNED PRACTICE comparator). Falsifier/ABANDON: the gradient road's KKT design beats S7's best 
by > band at equal budget (then S7 is dominated); or S7 finds a design beating the KKT point by > band (then 
the gradient road's local optimum is exposed as poor — a useful global check). Time: 4 sessions. Decisive: 
as S11.

### S8 — Objective change: operability-first (O-c) with performance as a constraint
Tuple: (O-c: maximize the minimum per-phase separation margin / exact via L1 (per-phase = per-φ wall 
pressure) / 3D rotating-steady / adjoint of a KS-aggregated max / gradient local / decisive: envelope of Pa 
over which the design stays attached, vs S1).
Q: a DIFFERENT question (not mean performance). Argument for: L3 says the mean-thrust pool is ~band-sized, 
whereas the per-phase wall-pressure swing is O(1) — attachment at every instant is where the unsteadiness 
is first-order and where the practice (mean-state design) is blind. Cost: same solver as S4; the criterion is 
a model layer (SP2). Generality: all; classes D–E natural. Pins: single-mode. Falsifier: URANS/experiment 
shows separation inside the certified margin. Time: same as S4 + 1. Rank 4 — and the PRE-REGISTERED PIVOT 
if the (O-a) decisive result is negative. ABANDON: per-phase wall pressure ratio p_w/Pa never approaches the 
separation criterion across the mission envelope (then O-c is not binding either). Decisive: altitude-band 
(Pa range) of attached operation gained over S1 at equal length, measured on the exact evaluator, band = 
spread of the criteria family.

### S9 — Design-variable change: MoC-native design (contour as OUTPUT of an exit-characteristic 
distribution)
Tuple: (O-a / mean state or phase ensemble / 2D steady / MoC kernel + turning region, contour = streamline; 
Rao/Guderley–Hantzsche transversality on the exit characteristic [KNOWLEDGE: Guderley & Hantzsche 1955, 
abstract; Rao 1958, full] / calculus of variations (necessary conditions), local / decisive: the same as S3 
with a shock-free-by-construction contour class).
Q: narrowing to steady-per-phase. Value: contours never generate internal shocks (regular net), and the 
necessary conditions are explicit (R-ii). Loss: the construction has no 3D rotating counterpart; only usable 
inside S3's design loop. Generality: bell and plug (free boundary handled by MoC). Rank 5-bis (as the 
PARAMETRIZATION option 4 of SP6 for S3, not as a stand-alone road). ABANDON: measured St > 0.3. Time: 2 
sessions given the legacy oracle. Decisive: as S11.

### S10 — Robust / envelope objective (O-b) as the primary question
Tuple: (O-b: expected or worst-case thrust over Pa-mission and throttle / exact per operating point via L1 / 
3D rotating-steady / adjoint per point / multi-point gradient or min-max / decisive: envelope-averaged gain 
vs S1 at a mission).
Q: a broadening. Cost: N_points × S4. Rank 6-bis: legitimate second study once the single-point decisive 
result exists; alone it inherits the marginality of L3 and multiplies the cost. Classes D–F needed. 
ABANDON: single-point gain already < band (then the envelope gain is < band too unless the practice design 
separates somewhere — which is S8's question).

### S11 — RECOMMENDED: bracket-then-certify hybrid (design loop on a reduced engine, evaluation on the 
exact-on-pin engine, difference-resolving certification)
Tuple: (objective O-a with O-c as per-phase constraint / time: design loop on S3 (St small) or on S4-marching 
(annular or axially-supersonic interface), evaluation on S4 exact / spatial: designer 2D-per-phase or 3D 
marching, evaluator 3D rotating-steady + one 3D time-accurate anchor / information: discrete adjoint 
(backward marching) verified by rejectable tests; the reduced-vs-exact defect measured via L8-type residuals 
/ search: trust-region SQP on B-spline control points, multistart, KKT with multipliers, L4 gap certificate; 
invalid states rejected inside the search by the per-solve validity checks / decisive: THE LOSS BUDGET of the 
tuned practice design on the exact evaluator, in thrust-stand units, followed by the fraction of the 
unsteady-specific pool recovered by S*).
Stage 0 (1 session): audit Γ_d (L6), compute St, r*, M_x maps, J_ceil (L4) and the loss budget of the 
practice design on the exact evaluator. GATE: if the unsteady-specific pool (Jensen + data-shock entropy 
terms) < β_stand·F̄ with β_stand = 0.01 (the reference class of §8, not a chosen constant), Q0 at (O-a) 
is answered NEGATIVELY at near-zero cost and the program pivots to S8 — a publishable answer. Otherwise 
proceed.
Q: Q0 on the pin, with a measured price for every reduction. Cost: 7–9 sessions if a marching branch is 
legal (L5); +3 sessions and 3-h-window violations if 3D pseudo-time is needed for the design loop (then the 
design loop falls back to S3 with the exact evaluator only at the decisive point). Generality: bell 
(x-marching if u_x > a on Γ_d), annular configs (θ-marching), plug base via SP-PB band; classes B 
(decisive), C (calibration of weights), F (band). Pins needed: single-mode (evaluator), frozen (both); 
relaxable at the evaluator: multi-mode only via S6 (priced). Falsifier: (a) designer-predicted J and 
evaluator J disagree by > designer band on S* (the reduced engine is rejected); (b) L1 drift test fails; (c) 
adjoint fails its rejectable tests. Time-to-number: Stage 0 gate = 1 session; full = 7–9. Rank 1. ABANDON: 
the Stage-0 loss budget shows the unsteady-specific pool < band (then the road is not worth building; the 
answer is negative and cheap) OR the exact evaluator cannot be validated (R-iv) on the practice design within 
the compute window. Decisive: SP9.

### S12 — Negative-result road: certify the bracket only (no optimization)
Tuple: (O-a / exact via L1 / 3D rotating-steady / no adjoint / no search; only J_ceil, J[S1-tuned], loss 
budget / decisive: "the pool is below the band").
Q: Q0's negative branch only. This is Stage 0 of S11 as a stand-alone; kept separate so the omission rule is 
honored: it is a complete road if the gate closes. Rank 1-bis (executed first inside S11). Cost: 1–2 
sessions. ABANDON: pool > 2× band (then optimize).

### S13 — Data-driven surrogate / ML emulator of the flow map for optimization
Rejected for a stated reason: no certificate class in R-iv/R-v (an emulator cannot be REJECTED as a solution 
of the declared model), and the training set would have to come from S4 anyway. Rank 10. Falsifier: n/a (no 
claim).

### S14 — Geometric-topology-as-output (level-set over E, configuration discovered by the optimizer)
Tuple: (O-a / exact / 3D / adjoint level-set Hamilton–Jacobi / topological local / decisive: a discovered 
sector beats all fixed-configuration optima).
Rejected as the decisive road for a stated reason: the design derivative through a topology change (plug 
termination, shroud appearance) is not defined in the piecewise-smooth Euler class (L7-iv changes 
discontinuity inventory); price = cannot discover E-D from bell. Replaced by a SECTOR TOURNAMENT (each 
configuration = separate instance, compared on the exact evaluator; SP6). Rank 8-bis.

### Ranking (recommendation order)
1 S11 (with S12 = its Stage-0 gate) · 2 S4 (evaluator of record) · 3 S3 (design engine at small St) · 4 S8 
(pre-registered pivot) · 5 S7 / S9 (fallback engine / parametrization) · 6 S2, S10 · 7 S6 (horizon, 
priced) · 8 S5, S14 · 9 S1 (control) · 10 S13.

---

## Level 1 — SUB-PROBLEM TREES (for S11; deviations for other strategies noted)

### SP-OBJ — Objective (LOAD-BEARING)
Options: (1) O-a mean thrust at a design point; (2) O-a mean Isp (same as (1) at fixed ṁ̄ — ṁ̄ is 
data, fixed by Γ_d: identical on the pin); (3) O-b envelope-weighted; (4) O-c operability as objective; (5) 
O-d cost proxies; (6) lexicographic: O-a subject to O-c constraint and O-d bounds.
Recommendation: (6). Grounds: a propulsion referee accepts time-mean thrust at a design point as THE number 
(it is what a thrust stand measures, hence the accuracy class of §8 is defined for it); attachment is a hard 
constraint not a trade; length/area are constraints c. Is the nozzle the lever? Dry: classical nozzle losses 
(divergence + expansion) ~1–3 % of Isp [KNOWLEDGE: Sutton & Biblarz textbook, full]; RDE combustor-side 
losses (deflagration fraction, mixing, azimuthal/radial kinetic energy in the exhaust) are reported at 
several % [KNOWLEDGE: Anand & Gutmark 2019 review, abstract] — so the nozzle-side pool is second-order, and 
the UNSTEADY-specific part of it is ~0.3–1 % (L3). Decision criterion: the Stage-0 loss budget (L4) on the 
practice design — it says in thrust-stand units what is on the table, term by term. Falsifier: loss budget 
pool < β_stand F̄ → (O-a) is not the lever; pivot to (4) as primary (S8). Options count 6.

### SP1 — Time (LOAD-BEARING)
Measurement of the residence ratio: St = f·τ_res with τ_res = ∫ dx/u_x along the mass-weighted mean 
streamline of the first solve; second indicator M_Ω = ωr/a (θ-hyperbolicity, L5); third: the BL-response 
ratio δ/(u_τ T) for the attachment criterion (SP2). All measured per instance, none assumed.
Options for the DESIGN loop: (1) single mixed-out state [S1/S2]; (2) quasi-steady K-phase ensemble, error 
O(St·A) with A = cycle amplitude of the fluxes, K from Richardson-in-K [S3]; (3) exact traveling-wave steady 
3D [S4]; (4) harmonic balance (penalized: Gibbs at the data shock, S5); (5) time-accurate [S6]; (6) mean 
state + first-order unsteady correction (linearized about the mean; invalid at O(1) amplitude — rejected by 
the same argument as S2).
Options for the EVALUATION of competing designs: (3) always; (5) once, as pin monitor and cross-code anchor.
Recommendation: design (2) if St < 0.3 measured, else (3) in its marching branch; evaluation (3)+(5). 
Decision criterion: exponent test (J_exact − J_qs ∝ St^p, p ≥ 1 measured on f, 2f, 4f — a rejector) 
and the L8 defect. Falsifier: designer/evaluator disagreement > designer band. Options count 6 + 2.

### SP2 — Flow model and solver (LOAD-BEARING)
Options: (1) quasi-1D unsteady (no divergence/shock geometry; only an initializer); (2) 2D axisymmetric MoC 
steady with shock/contact fitting and free boundary (legacy-oracle class) [KNOWLEDGE: Zucrow & Hoffman, 
full]; (3) 2D axisymmetric shock-capturing FV (HLLC with thermally-perfect EOS — HLLC needs only wave-speed 
estimates, no γ constant) [KNOWLEDGE: Toro textbook, full]; (4) 3D x-space-marching in (x,r,φ) of the L1 
system where u_x > a (2D (r,φ) Cauchy sweep per station; pressure at the wall from the compatibility 
relation) [KNOWLEDGE: Kutler et al. 1973 space-marching, abstract]; (5) θ-marching of the L1 system where 
|w_θ| > a, period-map fixed point (the traveling-wave form of a 2D unsteady solve); (6) 3D pseudo-time 
relaxation of L1 (mixed type, always legal, expensive); (7) 3D time-accurate absolute-frame FV (anchor); (8) 
high-order DG with entropy-stable fluxes [KNOWLEDGE: Tadmor 2003, abstract] (for entropy-production checks); 
(9) hybrids: (4) in the supersonic region + (6) in the axis core.
Selection rule (non-hardcoded): compute u_x/a and |w_θ|/a maps from a first (6) or (3)-ensemble solve; use 
(4) wherever u_x > a on the whole (r,φ) plane at that station; (5) if r_min > r*; (6) elsewhere; the 
designer uses the cheapest legal engine, the evaluator uses a DIFFERENT scheme family ((7) or (6) with a 
different flux) for independence.
Embedded discontinuities: fit (i) the data-borne oblique shock and (ii) contacts in the marching engines 
(floating discontinuities in the marching plane, Rankine–Hugoniot enforced), capture them in the evaluator 
(independent treatment = a cross-check of the fitting).
Attachment constraint (per-phase = per-φ): inviscid Euler never separates; a criterion is a MODEL LAYER, 
options: (a) p_w/Pa ≥ 0.4 (Summerfield-type) [KNOWLEDGE: Summerfield et al. 1954, abstract]; (b) Schmucker 
p_sep/Pa = (1.88 M_w − 1)^(−0.64) [KNOWLEDGE: Schmucker 1984, abstract; Frey & Hagemann 1998 review of 
criteria, abstract]; (c) Stratford-type turbulent criterion with an integral boundary layer marched along the 
wall on the Euler pressure [KNOWLEDGE: Stratford 1959, abstract]; (d) RANS/URANS as falsifier only. 
Recommendation: (b) as constraint g_sep = max_{wall,φ}(p_sep(M_w) − p_w) ≤ −m, with the margin m 
derived as the spread between (a),(b),(c) on the same field (criterion-family band, not a chosen constant); 
enforced via KS aggregation with ρ_KS ≥ ln(N_wall N_φ)/(m/4) so that the aggregation error is ≤ m/4. 
Quasi-steady BL validity: δ/(u_τ T) measured (expected ~10⁻²); falsifier: an unsteady BL calculation 
showing lag > m.
Truncated base: SP-PB. Options count 9 + 4.
Falsifier of the whole SP2 choice: R-iv checks (below) reject the evaluator's solution on the practice design.

### SP3 — Information for the optimizer (LOAD-BEARING)
Options: (1) discrete adjoint of the marching engine = backward marching (cheap, exact for the discrete J); 
(2) continuous adjoint with internal adjoint conditions at fitted discontinuities [KNOWLEDGE: Giles & Pierce 
2001, full; Jameson 1988, full]; (3) forward tangent / complex-step (cost ∝ #parameters; the rejector for 
(1)); (4) finite differences on J (noisy with captured shocks; only as a rejector); (5) derivative-free (S7).
Behaviour across discontinuities (dry): in 1D the functional is shift-differentiable (the derivative carries 
a term = jump × shock displacement) [KNOWLEDGE: Ulbrich 2002, abstract; Bressan & Marson 1995, abstract]; 
with FITTED discontinuities in the marching engine, the displacement is an explicit variable and (1) is 
exact; with CAPTURED ones, the discrete adjoint gradient converges to the true gradient only under 
refinement, with an O(h⁰) spurious term possible at the shock unless the adjoint is kept continuous there 
[KNOWLEDGE: Giles & Pierce 2001, full]. Contacts (linearly degenerate) contribute a jump in ρu_x² at the 
exit integral → the shift term exists but is first-order convergent under capture. Free plume boundary: a 
fitted p = Pa streamsurface; its displacement derivative is explicit in MoC.
Recommendation: (1) on fitted discontinuities; (2) only as an analytic cross-check of the internal conditions.
Rejectable tests (all with derived tolerances): (T-a) tangent/adjoint duality ⟨λ, A v⟩ = ⟨Aᵀλ, v⟩ 
to within N_ops·ε_mach·‖λ‖‖A‖‖v‖ (measured N_ops); (T-b) directional derivative vs 
complex-step (tolerance = complex-step round-off ~ ε_mach·|J|/h with h chosen by the round-off/truncation 
balance, i.e. h = √ε_mach·scale for FD, any h ≪ 1 for complex-step); (T-c) discontinuity-displacement 
test: perturb the design so the fitted shock/contact moves by δ, compare ΔJ with the adjoint prediction, 
reject if the residual is not O(δ²) (measured exponent ≥ 1.8); (T-d) gradient grid-convergence with 
observed order ≥ 1 (a drop to order 0 at a captured discontinuity rejects the captured-adjoint variant). 
Load-bearing: yes. Falsifier: any of T-a..T-d failing → fall back to S7 for the design loop. Options count 
5.

### SP4 — Search strategy (LOAD-BEARING for R-i/R-ii, local for the number itself)
Options: (1) trust-region SQP with adjoint gradients and BFGS Hessian, KKT with multipliers (length, area 
ratio, slope, curvature, attachment, envelope) reported; (2) multistart of (1) from k initial contours 
(conical, Rao-optimum, ideal-truncated, one per topology sector); (3) global heuristics (CMA-ES/BO) in a 
low-dim family (S7); (4) branch-and-bound on the L4 bound (a certified gap needs a design-dependent upper 
bound sharper than J_ceil; not available → the gap is J_ceil − J[S*], a valid but loose certificate); (5) 
continuation in f (St) and in the cycle amplitude from the steady optimum (physics-informed homotopy: the RDE 
optimum is a deformation of the Rao optimum as amplitude grows).
Recommendation: (1)+(2)+(5); guarantee class = local KKT point, plus the L4 gap, plus the multistart spread 
as evidence. Handling of non-validatable states inside the search: a design whose solve fails a validity 
check (R-iv list in SP8) is not silently penalized: the step is rejected and the trust region shrunk (the 
failure is a constraint violation of the declared solution class — e.g. characteristic coalescence 
indicator > 0, marching type change, RH residual above tolerance — and it is logged as such). Second-order 
check: the BFGS Hessian's projected eigenvalues on the active set (reported with sign, R-ii). Stopping: 
‖∇_red J‖ ≤ η·(band/‖typical step‖) — derived from the band, not a magic number. Falsifier: a 
multistart or S7 run finding J higher by > band. Options count 5.

### SP5 — Spatial representation (LOAD-BEARING)
Options: (1) quasi-1D; (2) 2D axisymmetric steady mean; (3) 2D axisymmetric unsteady slice (θ-flux dropped); 
(4) 3D rotating-frame steady (exact on pin); (5) 3D time-accurate (horizon); (6) 3D steady in a Fourier basis 
in φ (= S5).
What each loses vs the rotating 3D field, MEASURED: (2),(3): the residual r_θ of L8 evaluated on the reduced 
solution, and the first-order effect ⟨λ₃D, r_θ⟩ — followed by one (4) solve: the MEASUREMENT is 
|J₄ − J₃| on the same design; the residual-adjoint estimate is only its predictor and its effectivity 
index is recorded. (4) loses nothing on the pin (THEOREM L1) except pattern stability, MEASURED by the drift 
of a (5) run initialized on the (4) field over N periods (N derived: until the drift growth rate is resolved 
above the discretization noise of (5)). Designer ≠ evaluator: yes — designer (2)-ensemble or 
(4)-marching, evaluator (4) with an independent scheme + one (5) anchor. Falsifier: |J₄ − J_designer| > 
designer's band. Options count 6.

### SP6 — Geometry as design variable (local for the number, LOAD-BEARING for R-i existence and for 
admissibility certificates)
Options: (1) B-spline r_w(x), degree ≥ 3 (C²: Lipschitz slope guaranteed), control points in a box 
[KNOWLEDGE: de Boor 1978, full]; (2) CST class-shape functions [KNOWLEDGE: Kulfan 2008, abstract]; (3) 
Hicks–Henne bumps on a Rao baseline [KNOWLEDGE: Hicks & Henne 1978, abstract]; (4) MoC-native (S9): 
exit-characteristic distribution, wall = streamline (shock-free by construction; steady only); (5) level-set 
free-form (S14, rejected for the derivative reason); (6) sector tournament: configuration as INPUT per 
instance (bell / plug (truncation fraction as a variable) / shrouded plug / E-D), compared on the exact 
evaluator — the price: no discovery of a sector not enumerated.
Recommendation: (1) with (6); (4) as the initializer of the bell sector. Admissibility certificates: slope 
and curvature bounds via the convex-hull property of B-spline derivatives (divided differences of control 
points bound r_w′ and r_w″ — conservative THEOREM-level certificates); attachment on Λ by clamping the 
first control point; envelope by the box. Number of control points N: derived — increase N until J* changes 
by less than the band (Richardson-in-N rejector), lower-bounded by the resolution of the characteristic 
reflection scale at the wall (L/Δx_char).
As-built tolerance class δ (from the manufacturing spec, an INPUT): first-order robustness |ΔJ| ≤ 
‖∇J‖₁δ + ½δ²‖H‖ with ‖H‖ measured from gradient differences at ±δ; the attachment 
margin must satisfy m ≥ ‖∇g_sep‖₁δ (derived margin); a design failing this is not certified.
Existence: discrete problem — compact box × continuity of the discrete map on the class where the marching 
type does not change (the shock-free-in-marching-region class with indicator) → maximizer exists (THEOREM 
in the discrete problem). Continuum: CONJECTURE, with the uniform-cone/Lipschitz class as the natural 
compactness device [KNOWLEDGE: Chenais 1975, abstract] and continuity of multi-D Euler weak solutions in the 
domain being the named gap. Falsifier: J* keeps changing with N beyond the band (representation not 
converged). Options count 6.

### SP7 — Data (LOAD-BEARING through the weights and the pin magnitudes)
Entry of each class: A — model chain: ZND/CJ + Taylor expansion per cycle [KNOWLEDGE: Fickett & Davis 
textbook, full] or a reduced RDE flow model producing periodic interface profiles [KNOWLEDGE: Fievisohn & Yu 
2017 MoC-based RDE model, abstract; Braun et al. 2013, abstract; Paxson 2014, abstract; Nordeen et al. 
thermodynamic model, abstract]; its uncertainty (class F by construction) enters the band. B — direct 
interface profiles, audited by L6 and by the pin monitor (periodicity residual of the data: ‖Q(θ,t) − 
Q(θ−ωt′,t′)‖ over the record, tolerance = data noise floor measured on the record). C — 
calibration of the model chain's free parameters (fill fraction, deflagration fraction) and of the phase 
weights against pressure traces, f and n. D/E — additional operating points (S10). F — bands propagated 
by adjoint sensitivities dJ/d(data) (one adjoint solve per design gives the whole sensitivity field). G — 
impedance closure on the subsonic patches of Γ_d (L6): replaces the released quantity by a response map.
Audits with loud reject: (i) characteristic count per point per phase (L6); (ii) causal separation: reject if 
any patch is axially subsonic without a class-G closure; (iii) periodicity residual (pin monitor); (iv) 
conservation consistency of the data (φ-mean mass/energy flux vs specs of class A).
Weights: for the exact engine the weights are implicit (φ-mean); for S3, w_k = Δφ_k/2π (time weights — 
thrust is a time mean; mass weighting is only correct for collapsing to a single state, where it is still 
O(A²) wrong). Propagation: dJ/dw_k from the per-phase functionals.
Pin magnitudes (provenance = the estimates below, to be replaced by measurement): single-mode → 
counter-rotating pair: L1 void; effect on thrust reported at the few-% level in the literature [KNOWLEDGE: 
RDE mode literature, abstract] and above the band; cost of relaxing = S6 (HPC). Frozen → 
equilibrium/finite-rate: absolute Isp shift of order 1–4 % for hot dissociated products [KNOWLEDGE: Sutton 
& Biblarz, full], ABOVE the band for the absolute number but largely common to both compared designs; the 
effect on the DIFFERENCE Δ is bracketed by running both designs with the frozen and the equilibrium quasi-1D 
expansion along the mean streamline (cheap); if the bracket width exceeds band/4 the pin must be relaxed at 
the evaluator (finite-rate source terms are a standard addition to the FV evaluator). Single phase: zero 
effect for gaseous propellants (statement of scope); for condensed products a two-phase lag model would be a 
new solver layer. Falsifier of SP7: audit (i)–(iv) failing on the decisive data set. Options count: 7 
classes × entry + 4 audits.

### SP8 — Proof (LOAD-BEARING)
Per-solve validity checks (R-iv, each a rejector with a derived tolerance): (1) conservation defect of 
φ-mean mass, axial momentum, energy between Γ_d and exit ≤ the discretization band of the flux integral 
(measured by Richardson); (2) Rankine–Hugoniot residual at every fitted discontinuity ≤ the same band; 
(3) Lax entropy condition at every fitted shock (reject if violated) and non-negative discrete entropy 
production everywhere (captured evaluator, entropy-stable flux or explicit entropy-residual check); (4) 
contact conditions: pressure and normal velocity continuous; (5) marching-type integrity: u_x > a 
(x-marching) or |w_θ| > a (θ-marching) on the whole marching plane at every step (a type change = solve 
rejected); (6) characteristic-coalescence indicator ≤ 0 (no design-induced shock in the marching class); 
(7) attachment g_sep ≤ −m at every φ; (8) traveling-wave stability (drift test, one time-accurate run at 
the decisive point).
Non-uniqueness of multi-D weak solutions: acknowledged [KNOWLEDGE: De Lellis & Székelyhidi 2010, abstract; 
Chiodaroli, De Lellis & Kreml 2015, abstract]; our declared class = piecewise-smooth with Lax-admissible 
discontinuities, selected as the limit of the marching/pseudo-time scheme; uniqueness is a THEOREM in 
shock-free smooth regions (weak–strong uniqueness by relative entropy [KNOWLEDGE: Dafermos 1979, full]; 
classical Cauchy uniqueness for the supersonic marching problem [KNOWLEDGE: Courant & Friedrichs 1948, full]) 
and a SCHEMA where discontinuities are present; the two independent engines (fitted marching vs captured FV) 
agreeing within band is the operational uniqueness evidence, and their disagreement beyond band is the 
rejector.
A-posteriori error on J: (a) Richardson extrapolation with observed order p on 3 grids, ε_disc = |J_h − 
J_{h/2}|/(2^p − 1) [KNOWLEDGE: Roache 1998, full]; (b) dual-weighted residual ⟨λ, R_h⟩ [KNOWLEDGE: 
Becker & Rannacher 2001, full] with its effectivity index η measured against (a); (c) rigorous 
relative-entropy a-posteriori bounds exist only for smooth solutions of 1D systems [KNOWLEDGE: Giesselmann, 
Makridakis & Pryer 2015, abstract] — named as out of reach in 3D with shocks; (d) validated (interval) 
numerics — rejected for cost/wrapping (stated reason). Recommendation (a)+(b), with the safety factor s = 
max(1, 1/η_min) measured, never chosen.
Difference-resolving protocol: the decisive quantity is Δ = J[S*] − J[S_c]; compute BOTH on the same grid 
family and apply Richardson to Δ itself (correlated discretization errors cancel to first order; the band on 
Δ is measured, typically ≪ the band on J). Uncertainty budget: ε_tot = s·ε_disc(Δ) + ε_red 
(designer/evaluator gap, measured) + ε_data (adjoint × class-F band) + ε_base (SP-PB) + ε_rep. Claim 
rule: Δ is claimable iff Δ > max(β_stand·F̄, ε_tot) with β_stand = 0.01 (the reference class of §8).
Reproducibility across (version, check, environment): a result = the triple; at each change of any element 
the canonical suite (the 8 checks above on the practice design + the decisive Δ) is re-run; ε_rep := the 
maximum spread of the suite across the environments actually exercised (measured, re-measured at every 
change); a result is QUOTABLE iff every decision inequality holds with margin ≥ ε_rep; a non-reproducing 
result is declared FAILING with its triple recorded, kept in the record (never re-stamped) until the full 
suite passes on the new triple, and the discrepancy is owned as a finding. Falsifier of SP8: the two engines 
disagree by > band on the practice design. Options count 8 checks + 4 estimators.

### SP9 — The decisive result (LOAD-BEARING)
Pre-registration:
- Configuration: the first of [bell with axially-supersonic interface (u_x > a on Γ_d at every phase → 
x-marching legal everywhere, axis included), full-length annular nozzle with r_min > r* (θ-marching legal, 
no base region)] for which the Stage-0 audits (L5, L6) pass; a TRUNCATED plug is excluded from the decisive 
run (SP-PB band) and kept as a secondary study.
- Data class: B, with the class-F band of the wave-structure model propagated by adjoint; class C used only 
to calibrate f, n and the weights if available.
- Comparator (why strongest): the TUNED PRACTICE — a Rao-type contour designed at the flux-averaged state 
by the legacy oracle, with its 1–2 free parameters (length fraction / exit angle, i.e. the family a 
competent designer already sweeps) tuned by S7 ON THE EXACT EVALUATOR; this removes the objection "the gain 
is the evaluator's, not the method's". A competent designer already averages duty (SP-CARM), so the 
mean-state design IS duty-averaged.
- Metric: F̄ (time-mean thrust) from the exact evaluator, at equal ṁ̄ (data), equal length bound and 
equal exit area bound; reported also as the fraction of the unsteady-specific pool (L4 budget) recovered.
- Accuracy class: thrust-stand 0.5–1 %; bands per SP8; the number is quotable only if Δ > max(0.01·F̄, 
ε_tot).
- Outcomes: (P) Δ > band → the methodology buys Δ at (config, St, amplitude); the generalization claim is 
scoped to the (St, amplitude) point, extended to a CURVE by the f-sweep (f is a parameter: f/2, f, 2f; 3 more 
evaluator runs); (N) Δ ≤ band → negative answer: on the pinned family, tuned practice is within the 
thrust-stand band of the certified optimum; program pivots to S8 (O-c) where the unsteady effect is 
first-order; (I) invalid: an SP8 check fails on S* or S_c → no number is quoted, the failure is the result.
- Kill criterion of the road: (N) with the Stage-0 pool itself < band (nothing was ever on the table) → the 
road is not the way to optimize an RDE nozzle at (O-a).
- Sensitivity: ∂Δ/∂w (weights/waveform) from the two adjoints; ∂Δ/∂p_b = 0 by configuration choice 
(bell / full-length annular); reported as bands.
- External anchors: (i) J_ceil (L4) — both designs must lie below it and the loss budget must sum exactly 
(a conservation identity, checkable by hand from the exit field); (ii) legacy Fortran oracle on each frozen 
phase of the interface data for the practice design (agreement within ε_disc or reject); (iii) cross-code: a 
time-accurate absolute-frame 3D FV run (independent flux, independent discontinuity treatment) at S* and S_c, 
agreeing with the rotating-steady evaluator within band, and serving as the drift test; (iv) reference 
accuracy class: thrust-stand (no experiment guaranteed; the number is anchored computationally, and the claim 
says so).
- WHICH MEASUREMENT WOULD MAKE ME CHANGE ROAD: the Stage-0 loss budget showing the unsteady-specific terms 
(Jensen + data-shock entropy) below 0.5 % of F̄ on the tuned practice design — then no (O-a)-road can 
produce a claimable number and the question moves to (O-c)/(O-b). Second: the drift test failing on the 
practice design (no pinned answer exists; road S6).
Falsifier: as the outcomes. Options count: 2 configs × 3 outcomes pre-registered.

### SP-PB — Base region (local for the decisive run by configuration choice; LOAD-BEARING if a truncated 
plug is ever the decisive config)
Options: (1) p_b = Pa (open base, low altitude); (2) Korst-type mixing-layer base-pressure model [KNOWLEDGE: 
Korst 1956, abstract]; (3) empirical base-pressure correlations for truncated plugs [KNOWLEDGE: Hagemann et 
al. 1998 advanced nozzle review, abstract]; (4) set-valued: p_b ∈ [p_min, p_max] from the spread of 
(1)–(3), shipped as a band; (5) per-phase base pressure from the rotating-frame evaluator with a 
recirculation closure (a model layer, Euler cannot set it).
Materiality (dry): ε_base/F̄ ≈ (δp_b/Pa)·(A_b/A_t)·(Pa/p_c)/C_F; with δp_b ~ 0.5 Pa, A_b/A_t ~ 2, 
p_c/Pa ~ 20, C_F ~ 1.5 → ≈ 3 % ≫ 1 %: the band swamps the decisive difference unless both designs share 
the same base (they don't — A_b differs). Recommendation: (4) always shipped; decisive run on a base-free 
configuration (SP9); the truncated plug enters as a secondary study whose Δ is quoted with the base band, 
and a claim is made only if Δ > ε_base + ε_tot (typically it will not resolve — pre-registered). 
Falsifier: a measured base pressure (class C) narrowing the band below band/4 makes the plug 
decisive-eligible. Options count 5.

### SP-CARM — Strongest competing practice (LOAD-BEARING for the credibility of Δ)
Options for the comparator: (1) Rao contour at the time-mean state (arithmetic means of p, T, M); (2) Rao 
contour at the FLUX-averaged (mixed-out) state — the turbomachinery mixing-plane practice [KNOWLEDGE: 
Denton 1992 loss mechanisms / mixing-plane practice, abstract]; (3) (2) with 1–2 parameters tuned on the 
exact evaluator (TUNED PRACTICE); (4) multi-phase Rao: one contour per phase, pick the best on the exact 
evaluator; (5) conical/ideal-truncated nozzle of equal length (weaker; used only as a second control); base 
treatment for plug comparators: (1) of SP-PB with the band.
Recommendation: (3) as THE comparator, (4) as a second control (it is what a designer with a phase model 
would do). Does a competent designer already average duty? Yes: flux-averaging is standard where the inflow 
is nonuniform; RDE nozzle studies design for time-averaged exit conditions and check unsteady behaviour with 
CFD [KNOWLEDGE: RDE nozzle experiments, e.g. AFRL aerospike studies, Fotia et al. 2016, abstract]. Decision 
criterion: (3) must be given the same evaluator, the same constraints c and the same base treatment as S*. 
Falsifier of the comparator choice: an S7 sweep of the practice family finding a member within band of S* 
(then the "method" gain is nil — which is outcome (N), not a failure of the protocol). Options count 5.

---

## Order of battle (dependency order, load-bearing first)

1. SP7 audits (L6 characteristic count, periodicity monitor, conservation consistency) on the decisive data 
set — nothing downstream is defined otherwise.
2. SP1 indicators: St, M_Ω map, r*, u_x/a map from a first solve; fixes the legal engines (SP2 selection 
rule) and the design-loop engine (S3 vs S4-marching).
3. SP-OBJ gate via L4: J_ceil and the loss budget of the tuned practice design on the exact evaluator (needs 
SP2 evaluator + SP-CARM comparator + SP8 checks 1–8 on that single design). GATE: pool < band → negative 
answer, pivot to S8.
4. SP2 evaluator validated (SP8 checks) + cross-code drift anchor on the practice design (one time-accurate 
run).
5. SP3 adjoint of the design engine with T-a..T-d passed (else S7 fallback).
6. SP6 parametrization with certificates; N by Richardson-in-N.
7. SP4 search (multistart + continuation in amplitude) → S*, KKT report with multipliers.
8. SP5 measurement of the designer/evaluator gap on S* (L8 defect + one exact solve).
9. SP9 decisive Δ with the difference-resolving protocol, budget, f-sweep, anchors; SP-PB secondary study.
10. SP8 reproducibility suite frozen with the triple; quotability margin recorded.

Deviations for other strategies: S3 replaces step 2's engine and adds the exponent test; S4-only skips step 
8; S7 skips step 5; S8 replaces the objective in step 3 by the criterion-family margin and the f-sweep by a 
Pa-sweep.

---

## Knowledge claims (tagged, with depth) — 33
K1 Rao 1958 [full] · K2 Zucrow & Hoffman 1977 [full] · K3 Courant & Friedrichs 1948 [full] · K4 Toro 
(Riemann solvers textbook) [full] · K5 Giles & Pierce 2001 [full] · K6 Hall, Thomas & Clark 2002 [full] · 
K7 McMullen & Jameson 2006 [abstract] · K8 Dafermos 1979 [full] · K9 De Lellis & Székelyhidi 2010 
[abstract] · K10 Chiodaroli, De Lellis & Kreml 2015 [abstract] · K11 Ulbrich 2002 [abstract] · K12 Bressan 
& Marson 1995 [abstract] · K13 Becker & Rannacher 2001 [full] · K14 Giesselmann, Makridakis & Pryer 2015 
[abstract] · K15 Chenais 1975 [abstract] · K16 Kulfan 2008 [abstract] · K17 de Boor 1978 [full] · K18 
Schmucker 1984 [abstract] · K19 Summerfield et al. 1954 [abstract] · K20 Stratford 1959 [abstract] · K21 
Sutton & Biblarz textbook [full] · K22 Fickett & Davis textbook [full] · K23 Schwer & Kailasanath 2011 
[abstract] · K24 Fievisohn & Yu 2017 [abstract] · K25 Anand & Gutmark 2019 [abstract] · K26 Denton 1992 
[abstract] · K27 Kutler et al. 1973 [abstract] · K28 Korst 1956 [abstract] · K29 Roache 1998 [full] · K30 
Hicks & Henne 1978 [abstract] · K31 Jameson 1988 [full] · K32 Guderley & Hantzsche 1955 [abstract] · K33 
Hirsch 1990 [full]; plus lower-depth mentions folded into the above: Braun et al. 2013, Paxson 2014, Nordeen 
et al. (thermodynamic RDE model), Griewank & Walther 2000, Tadmor 2003, Frey & Hagemann 1998, Hagemann et al. 
1998, Fotia et al. 2016, RDE mode literature — all [abstract]. Total distinct tagged claims: 42.

## Independence declaration
Only `PROBLEM_STATEMENT_agnostic.md` and `DERIVER_BRIEF_agnostic.md` were opened. No other file, directory, 
log, registry or source of the repository was read, listed or searched. The harness injected a project memory 
summary into the system context without any action of mine; nothing from it was used — every construct 
above (L1–L8, the strategies, the option spaces) is derived from the statement and from open literature.
