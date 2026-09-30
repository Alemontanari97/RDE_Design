# Digest: NPAC — Nozzle Performance Analysis Code (NASA CR-204129)

**Source PDF:** `c:\Users\amont\Claude\Projects\Presentazione RDE CVA\rde-lecture-code\NASA_STUFF_Nozzle_Inlet\19970024876.pdf` (82 PDF pages; printed report pages 1–81).
**Page convention in this digest:** "p. N" = printed report page number (printed p. 1 = PDF page 3; offset +2 through the report body). All 82 PDF pages were read, including Appendices I–III and the Report Documentation Page.

---

## 1. Bibliographic identity, purpose, scope

- **Title:** NPAC — Nozzle Performance Analysis Code.
- **Author:** Paul J. Barnhart, NYMA, Inc., Engineering Services Division, Brook Park, OH 44142 (Supervisor, Aerospace Analysis Section).
- **Report:** NASA Contractor Report 204129, July 1997. Prepared for Lewis Research Center under Contract NAS3-27186; work unit WU-522-41-43; NYMA report E-10798; Project Manager Paul F. Senick, Propulsion Systems Analysis Office, NASA Lewis (RDP, p. 81 / PDF p. 82). Unclassified–Unlimited, Subject Category 07. 81 pages.
- **Purpose (Abstract, p. 1):** a "simple and accurate nozzle performance analysis methodology" with minimal, flexible geometry modeling, coupling continuity, momentum, energy, state and other relations for "fast and accurate calculations of nozzle gross thrust." The control-volume and internal-flow analyses account for: over/under expansion, flow divergence, wall friction, heat transfer, and mass addition/loss across surfaces.
- **Scope (pp. 1–2):** on- and off-design performance prediction for **axisymmetric or two-dimensional (symmetric or asymmetric), convergent and convergent-divergent** nozzle geometries; also usable for preliminary nozzle system design followed by performance analysis. Nozzle performance is framed by three quantities: accepted engine airflow W7, gross thrust coefficient C_FG, and aerodynamic drag coefficient C_D (the report itself computes W7 and C_FG; drag is not modeled here).
- **Architecture (pp. 2–3):** three-pass solution strategy:
  1. **First pass** — isentropic 1-D stream-tube march (mass conservation only).
  2. **Second pass** — skin friction and heat transfer computed from first-pass solution via boundary-layer theory (uncoupled).
  3. **Third pass** — fully-coupled 7×7 system per volume element tying together all effects (friction, heat transfer, mass addition), marched downstream.
  Gross thrust is then obtained by integrating forces on a control volume around the nozzle (Eq. 57 form, with divergence correction).

---

## 2. Complete method inventory

### 2.1 Geometry model (pp. 2, 23 Fig. 1; App. I pp. 33–34)

- Nozzle geometry specified by two boundaries: **surface i** (upper/outer) and **surface j** (lower/inner), each a series of **straight-line segments** defined by (x, r) coordinate end points. Recommended: shared x-coordinates; required: same number of segments on i and j. Axisymmetric geometries defined in a half plane and mirrored automatically.
- **Implied surface k** closes the finite volume between i and j: sidewalls for 2-D nozzles, side-planes for *partially circular* axisymmetric nozzles; k requires no direct coordinate specification (p. 2).
- Flow stations: **7 = nozzle entrance, 8 = throat, 9 = exit**; for convergent nozzles stations 8 and 9 coincide (p. 2).
- Inputs beyond geometry: P_T7, T_T7, ambient P_0. Either (a) W7 specified → geometry **re-scaled** (length scaling factor, shape-preserving) to give the correct throat area at the specified throat Mach number; or (b) A8, M8 specified → W7 computed. Specifying both W7 and throat area is inconsistent (pp. 2, 4).
- Discretization: each segment subdivided (npts, default 51; examples use 101) into 1-D volume elements; cubic-spline "data enrichment" (nspl, default 50) used in the numerical integration of control-volume surface integrals (App. I, pp. 31, 34).

### 2.2 Basic one-dimensional relations (pp. 3, 16; Eqs. 1–10)

- Eq. 1 (p. 16): C_FG = F_G / F_GI (actual/ideal gross thrust).
- Eq. 2: **F_G = ṁ9·V9 + (P9 − P0)·A9** — 1-D momentum + pressure-area gross thrust; last term vanishes for perfect expansion.
- Eqs. 3–5: F_GI = ṁ9 V9 = γ P0 M9² A9 = γ (P0/P_T8)(A9/A8) M9² P_T8 A8 (ideal, fully-expanded).
- Eq. 6: normalized ideal thrust F_GI/(P_T8 A8) = γ M9² (A9/A8)/(P_T8/P0).
- Eq. 7: (P_T8/P0) = (P_T9/P9) — statement of no internal loss with perfect expansion to ambient.
- Eq. 8: ideal exit Mach from NPR: M9 = sqrt{ (2/(γ−1)) [ (P_T9/P9)^((γ−1)/γ) − 1 ] }.
- Eq. 9: A9/A8 = 1 for M9 ≤ 1 (convergent); Eq. 10: isentropic area–Mach relation for M9 > 1 (convergent-divergent). Refs: Stitt NASA RP 1235 (ideal thrust); NACA Report 1135 (compressible relations).
- All Eq. 8–10 quantities are **idealizations**, not physical states of the actual nozzle (p. 3).

### 2.3 Governing control-volume analysis (pp. 3–4, 16; Eqs. 11–12)

- Eq. 11 (p. 16): exact gross thrust from exit-plane integrals: F_G = ∬9 Vx ρ (V⃗·n̂) dA + ∬9 (P − P0) n̂x dA. Correct but requires detailed exit-field knowledge (experiment or CFD) (p. 3).
- Eq. 12 (p. 16): momentum theorem applied over the CV bounded by entrance (station 7) and surfaces i, j, k:
  F_G = −∬7 Vx ρ(V⃗·n̂)dA − ∬7 (P−P0)n̂x dA − Σ_i ∬ Vx ρ(V⃗·n̂)dA − Σ_j … − Σ_k … (mass fluxes crossing surfaces) − Σ_i ∬ (P−P0) n̂x dA − Σ_j … − Σ_k … (pressure forces) − Σ_i ∬ τx dA − Σ_j … − Σ_k … (shear forces),
  with summations over the N_i, N_j, N_k surface segments. **Functionally equivalent to Eq. 11 but computationally advantageous** (p. 4): if entrance flow is 1-D the first two integrals are trivial, and only per-segment fluxes/forces are needed — "avoids the necessity to accurately compute the entire internal nozzle flow field"; relatively simple internal-flow models give adequate surface-integral quantities.

### 2.4 1-D compressible mass flow relations (pp. 4, 17; Eqs. 13–20)

- Eqs. 13–15: ṁ = ρVA; V = M√(γRT); ρ = P/(RT) — ideal gas.
- Eqs. 16–19: build-up to the compressible mass-flow function; Eq. 19: ṁ = A √(γ/R) (P_T/√T_T) M [1 + (γ−1)/2 M²]^(−(γ+1)/(2(γ−1))).
- Eq. 20: same in **weight-flow** form W = A √(γg/R) (P_T/√T_T) M [...]^(−(γ+1)/(2(γ−1))), noted "for air R = 53.35 ft·lb/lbm·°R" (p. 17). Eq. 20 is the starting point of the whole analysis: throat sizing or W7 determination (p. 4).

### 2.5 1-D compressible stream-tube relations — first pass (pp. 5–6, 17; Eqs. 21–25)

- Volume element (Fig. 2, p. 24): only geometric data needed = A1, A2 (upstream/downstream areas) and total lateral surface area S (partitioned among i, j, k contributions). Flow constant across the element normal to the axis; 7 states per boundary: U, P, T, ρ, M, P_T, T_T.
- Eq. 21: ṁ1 = ṁ2. Eq. 22: A1 (P_T1/√T_T1) M1 [1+(γ−1)/2 M1²]^(−(γ+1)/(2(γ−1))) = same at 2 — area–Mach marching relation also carrying P_T, T_T changes.
- Eq. 23: iterative residual form (A1/A2) − (P_T2/P_T1)√(T_T1/T_T2)(M2/M1)[(1+(γ−1)/2 M2²)/(1+(γ−1)/2 M1²)]^(−(γ+1)/(2(γ−1))) = 0, solved by single-variable Newton–Raphson; terms deliberately normalized ≈ O(1) for convergence robustness (pp. 5–6). First pass: isentropic (P_T, T_T constant), march entrance → exit; entrance Mach found by applying Eq. 23 between entrance and throat areas with throat M as downstream value (p. 6).
- Mass addition/loss in the mass balance: Eq. 24: ṁ1 + δṁ = ṁ2; Eq. 25: iterative form with factor [1 + δṁ/ṁ1](A1/A2) − ... = 0. **Constraint stated:** δṁ must be small vs ṁ or the 1-D volume-element assumptions break down (p. 6).

### 2.6 Compressible turbulent skin-friction model — second pass (pp. 6–7, 18; Eqs. 26–36)

- Eq. 26: τw = C_f · ½ ρe Ue² with boundary-layer-edge quantities = first-pass solution.
- **White & Christoph flat-plate compressible turbulent C_f** (Ref. 3: White, *Viscous Fluid Flow*, 1974, pp. 637–648), Eqs. 27–30 (p. 18):
  - Eq. 27: C_f ≈ 0.455 / { Ω² ln²[ (0.06/Ω) Re_L (μe/μw) √(Te/Tw) ] }
  - Eq. 28: Ω = √(Taw/Te − 1) / { sin⁻¹[(2a²−b)/√(b²+4a²)] + sin⁻¹[b/√(b²+4a²)] }
  - Eq. 29: a = √[ ((γ−1)/2) Me² (Te/Tw) ]; Eq. 30: b = Taw/Tw − 1.
- Eq. 31: adiabatic wall temperature Taw = Te (1 + r (γ−1)/2 Me²); Eq. 32: recovery factor **r = Pr^(1/3)** (turbulent). Tw can be specified per surface segment, or adiabatic-wall used for no-heat-transfer (p. 6).
- Eq. 33: Re_L = ρe Ue L / μe. Eq. 34 (p. 18): the length L is **not physical** but built by dimensional argument from the truncated-cone approximation of each element: L = (1/√π) Σ_{n=2..N} S_n / (√A_{n−1} + √A_n) + L0, i.e., a running effective length plus an entrance offset L0 fixed by the user-specified **nozzle entrance Reynolds number** (default rei = 1.0E+7) via Eq. 33 (pp. 6–7; App. I p. 31).
- Eq. 35: Sutherland viscosity μ(T) ≈ μs (T/Ts)^{3/2} (Ts + Cs)/(T + Cs); gas-dependent constants (defaults for air: xmus = 3.584E-7 lb·s/ft², ts = 491.6 R, cs = 198.6 R; App. I p. 32).
- Eq. 36 (p. 18): **Mangler transformation / "turbulent cone rule"** for axisymmetric surfaces i, j: same White formula with **Re_L/2** inside the log: C_f ≈ 0.455 / {Ω² ln²[(0.06/Ω)(Re_L/2)(μe/μw)√(Te/Tw)]}. Surface k and all 2-D surfaces use flat-plate Eq. 27 (p. 7).

### 2.7 Heat transfer (pp. 7, 18; Eqs. 37–39)

- Eq. 37: **Reynolds analogy** C_h ≈ C_f / (2 Pr^{2/3}) — "heat transfer coefficient is approximately one half the skin friction coefficient" (p. 7).
- Eq. 38: q_w = C_h ρe Ue c_p (Taw − Tw), per surface segment, apportioned by each surface's share of element area S.
- Eq. 39: c_p = γR/(γ−1) (ideal gas). Heat transfer occurs only where a wall temperature is specified (p. 7).

### 2.8 Fully-coupled 1-D stream-tube flow model — third pass (pp. 7–8, 19; Eqs. 40–46)

Per volume element: 7 unknown downstream quantities (U2, P2, T2, ρ2, M2, P_T2, T_T2) from 7 known upstream ones plus source terms (τ̄w, q̄w, δṁ), solved simultaneously by **multi-variable Newton–Raphson**; first-pass solution is the initial guess (p. 7). Each equation normalized by upstream quantities so leading terms are O(1) (p. 8). P̄, τ̄w, q̄w are arithmetic averages of upstream/downstream values. Formulation credit: Shapiro Vol. I, pp. 219–260 (Ref. 4) — i.e., the influence-coefficients/generalized 1-D flow chapter (p. 8).

- Eq. 40 (state): (ρ2/ρ1)(P1/P2)(T2/T1) − 1 = 0.
- Eq. 41 (mass): [ρ2 U2 A2 − ρ1 U1 A1 − δṁ]/(ρ1 U1 A1) = 0.
- Eq. 42 (momentum): [(ρ1 U1 A1 + δṁ)U2 − ρ1 U1² A1 + P2 A2 − P1 A1 − P̄(A2 − A1) + τ̄w S − u_a δṁ]/[(P1 + ½ρ1 U1²)A1] = 0. (Wall-pressure term P̄(A2−A1); wall shear τ̄w S; injected-stream axial momentum u_a δṁ.)
- Eq. 43 (energy): [q̄w S − c_p T_T2 ρ2 U2 A2 + c_p T_T1 ρ1 U1 A1 + (c_p T_Ta + ½V_a²) δṁ]/(c_p T_T1 ρ1 U1 A1) = 0.
- Eq. 44: total-temperature definition ratio; Eq. 45: total-pressure definition ratio (isentropic-form definitions linking static and total via M); Eq. 46: velocity–Mach consistency (U2/U1)(M1/M2)√(T1/T2) − 1 = 0. (All p. 19.)

### 2.9 Mass addition / mass loss models (pp. 8, 19; Eqs. 47–54; Fig. 3 p. 25)

- **Mass addition** (Eqs. 47–51): injected flux assumed to expand completely to the element's upstream pressure: P_a = P1 (Eq. 47); M_a from P_Ta/P_a isentropically (Eq. 48); T_a from T_Ta and M_a (Eq. 49); V_a = M_a√(γRT_a) (Eq. 50); axial component u_a = V_a cos(θ − φ) (Eq. 51), θ = injection angle relative to the surface segment, φ = segment inclination to axis (Fig. 3, p. 25). P_Ta, T_Ta are methodology inputs (per segment: ratios Pt/pt7, Tt/tt7; App. I p. 30).
- **Mass loss** (Eqs. 52–54): flow leaves at local conditions: T_a = T1, V_a = U1, u_a = V_a cos(θ + φ).
- Mass added/lost per segment is a user input, distributed **evenly over the segment** (p. 8). `waddi/waddj` inputs = total mass-addition fraction crossing each surface **ahead of the throat**, needed for correct throat sizing (App. I pp. 31, 34).

### 2.10 Divergence loss model (pp. 8–9, 20; Eqs. 55–59)

- Eq. 55: F_G = λ ṁ9 V9 + (P9 − P0) A9 — divergence factor λ multiplies the **momentum term only**.
- Eq. 56: integral counterpart, λ on the exit momentum-flux integral only.
- Eq. 57 (p. 20): the **final governing control-volume equation** replacing Eq. 12: F_G = −λ{ [all Eq.-12 CV surface integrals: entrance momentum + pressure, segment mass-flux, pressure, shear sums] } + (1−λ) ∬9 (P − P0) n̂x dA. (Algebraic rearrangement so the CV form carries the divergence correction; note the residual (1−λ) exit pressure-integral term.)
- λ from **Berton** (Ref. 5: NASA TM 105176, 1991, "Divergence Thrust Loss Calculations for Convergent-Divergent Nozzles: Extensions to the Classical Case"):
  - Axisymmetric, Eq. 58: λ = ½(sin ψi + sin ψj)² / [ (ψi + ψj) sin ψj + cos ψj − cos ψi ].
  - Two-dimensional, Eq. 59: λ = (sin ψi + sin ψj)/(ψi + ψj).
  - ψ = inclination of the **last** nozzle surface segment to the axial direction, per surface (p. 9). This generalizes the classical single-cone-angle λ to independent inner/outer terminal angles.

### 2.11 Iteration and linear-algebra machinery (pp. 9–10, 20–22; Eqs. 60–85)

- Single-variable Newton–Raphson: Eqs. 60–66; residual f(x)=0, convergence |f| < ε, derivative by central finite difference with step δ = εx (Eqs. 63–64), update x ← x − f/(∂f/∂x).
- Multi-variable Newton–Raphson: Eqs. 67–76; Jacobian [A] by numerical differencing; [A][Δx] = [f].
- LU decomposition with forward/backward substitution: Eqs. 72–85 (p. 21–22); "diagonally-dominant" systems presumed; Ref. 6 = Press et al., *Numerical Recipes in Pascal*, 1986.
- Control parameters (App. I p. 32, 35): eps = 1.0E-3 (differencing factor), tol = 1.0E-6 (single-variable convergence), con = 1.0E-6 (multi-variable convergence), del = 1.0E-2 (allowed |M−1| band at throat).

### 2.12 Additional non-dimensional performance parameters (pp. 10, 22; Eqs. 86–90)

- Eq. 86–87: discharge coefficient **C_d = W8/(W8)_ideal**, ideal from Eq.-20-type expression at station 8 with P_T7, T_T7 (M8 = 1 choked, < 1 unchoked).
- Eq. 88–89: velocity coefficient **C_V = V9/(V9)_ideal**, denominator M9 √[γR T_T7/(1 + (γ−1)/2 M9²)] with M9 the ideally-expanded exit Mach.
- Eq. 90: expansion coefficient **C_e = (P9 − P0)/(P9 − P0)_ideal**; numerator from the fully-coupled model, denominator from the loss-free 1-D stream-tube model; denominator ≠ 0 except at perfect expansion (p. 10).

### 2.13 Gas model / gamma treatment

- **Calorically-perfect ideal gas throughout**: single constant γ, R, Pr, and Sutherland constants per run (Eqs. 14–15 "ideal gas assumption is inherent," p. 4; App. I p. 32, 35: gamma = 1.4, rgas = 53.35, pr = 0.72 defaults for standard air; "can be changed to model other gasses or air at high temperatures").
- Real-gas effects handled only by **surrogate constant properties**: for the rocket validation, gas properties "approximating the combustion products" were computed with the CEC code of Gordon & McBride (Ref. 12, NASA SP 273, 1971) from test conditions of Ref. 11 (pp. 11–12). Appendix III uses gamma = 1.30, rgas = 113.3, tt7 = 6589 R, pt7 = 2.699E+5 psf (p. 66).

---

## 3. Inputs/outputs, operating envelope, stated limitations

### Inputs (Appendix I, pp. 30–35)
Namelist `&npac ... &end`; multiple stacked namelists allow parameter sweeps (variables persist between sets, p. 32). Key inputs:
- Geometry: ni/nj segment counts; xri/xrj arrays with per-point: x, r, variable-geometry flag (**not implemented**, p. 33), surface-type flag (no-slip = 1, slip = −1, symmetry = 0), flow-station id (0/7/8/9), wall temperature (Tw/tt7 or −1 = adiabatic), mass-addition fraction w/w7, Pt/pt7, Tt/tt7, injection angle (deg); waddi/waddj (pre-throat mass-addition totals).
- Discretization: npts (default 51), nspl (default 50).
- Dimensionality: idim = 1 axisymmetric, 2 symmetric 2-D, −2 non-symmetric 2-D; ar = aspect ratio (entrance width/height; 1.0 = square 2-D or full-circular axisymmetric); scale = length scale factor.
- Flow: w7 (lb/s; 0 → computed from geometry, else geometry re-scaled), pt7 (psf), tt7 (R), xm8 (default 1.0), rei (entrance Reynolds number, default 1.0E+7).
- Ambient: p0 > 0 → psf; p0 < 0 → interpreted as −NPR; **p0 = 0 → perfect-expansion ambient pressure computed** (p. 32, 35).
- Gas: gamma, rgas, pr, xmus, ts, cs. Iteration: eps, tol, con, del.

### Outputs (pp. 33; App. II–III examples pp. 42–60, 66–79)
- Tabular data file (`table=`): NPR, C_FG, expansion area ratio, C_d, C_V, divergence factor λ, C_e (p. 33).
- Main output (iout-controlled): geometry echo/check, stream-tube data, inviscid solution, viscous fully-coupled solution (x, M, P, T, ρ, U, P_t, T_t at every march point), per-segment momentum-flux / pressure·area / shear·area contributions on surfaces i, j, k, station 7/8/9 one-dimensional summaries (area, M, P, T, ρ, U, P_T, T_T, mass flux, momentum flux, pressure·area), divergence factor, gross thrust, ideal gross thrust, thrust coefficient (e.g., p. 53). Additional files *.geo and *.1d are always written (p. 33).

### Stated limitations / envelope
- **No flow separation modeling**: "The analyses developed within the NPAC methodology do not permit flow separation, and thus for low pressure ratio nozzles the resulting gross thrust calculations will be significantly lower than those measured in actual nozzles" (p. 11). Over-expansion is captured only as attached-flow pressure loss; the separation-induced thrust recovery at low NPR is missed (Fig. 5 lowest-NPR point). Agreement "very good" for this geometry at **NPR ≥ 10** (p. 11).
- **1-D internal flow**: quantities uniform across the nozzle normal to the axis (p. 10); adequacy argued because Eq. 57 needs only surface-integral-adequate averages (p. 11).
- **Ideal (calorically perfect) gas**; non-ideal high-temperature combustion gas handled only via surrogate constants — cited as a limitation explaining part of the ~5% rocket-case deviation (p. 12).
- δṁ must be small relative to ṁ (p. 6).
- Variable-geometry input flag reserved but **not implemented** (p. 33).
- No aerodynamic (external) drag coefficient computation; C_D named as a performance quantity (p. 1) but not modeled.
- Straight-segment geometry only (curved walls approximated by segments + npts subdivision).
- Steady flow only; no shocks inside the divergent section are modeled (the marching relations are shock-free; over-expansion appears only through the exit pressure term).

---

## 4. Validation content (pp. 10–12; Figs. 4–6, pp. 26–28)

1. **2-D test model nozzle vs NPARC2D full Navier–Stokes** (Fig. 4, p. 26; pp. 10–11):
   - Grid: 200×100, exponential wall packing, INGRID2D (Ref. 7, AEDC-TR-86-49); NPARC codes = enhanced multi-block PARC (Ref. 8, AEDC-TR-89-15), RANS ideal gas, Baldwin–Barth one-equation turbulence model (Ref. 9, NASA TM 1002847, 1990).
   - Finding: significant differences between upper-surface and centerline pressure distributions in the CFD; the NPAC 1-D pressure distribution "is observed to be a very adequate average of the two distributions" (p. 11). Justification: gross thrust needs only the pressure integral over CV surfaces (Eq. 57).
2. **2-D test model nozzle vs experiment** (Fig. 5, p. 27; p. 11): gross thrust coefficient over NPR ≈ 5–40, normalized by max experimental value at design NPR; data = "NASA-Lewis Research Center test data provided by Pratt & Whitney" (Ref. 10). "Excellent agreement ... over most of the range"; deviation at the lowest NPR (NPAC ≈ 0.76 vs data ≈ 0.88 normalized) attributed to unmodeled separation; **very good agreement for NPR ≥ 10** (p. 11).
3. **Axisymmetric rocket nozzle vs experiment** (Fig. 6, p. 28; pp. 11–12): two high-area-ratio bell nozzles, **expansion area ratios 1025 and 440**, oxygen–hydrogen combustion at high pressure/temperature, various O/F ratios (data: Jankovsky, Kazaroff & Pavli, NASA TP 3576, 1996, Ref. 11). Gas surrogate properties from CEC (Ref. 12). Result: **F_G(NPAC)/F_G(data) within approximately 5% over the entire O/F range for both area ratios** (p. 12); Fig. 6 shows ratios ≈ 0.94–1.02 over O/F ≈ 3.9–6.1, with a mild downward trend at higher O/F. Appendix III example = the 440 area-ratio nozzle at greatest O/F (farthest-right point of Fig. 6).

---

## 5. Numbers-of-record worth citing

- White–Christoph C_f constants: **0.455** numerator, **0.06** inside the log (Eqs. 27, 36, p. 18); source: White, *Viscous Fluid Flow*, 1974, pp. 637–648.
- Mangler/turbulent-cone-rule: axisymmetric C_f uses **Re_L/2** in the log argument (Eq. 36, p. 18).
- Turbulent recovery factor r = **Pr^{1/3}** (Eq. 32); Reynolds analogy C_h = C_f/(2 Pr^{2/3}) (Eq. 37).
- Effective-length rule: L = (1/√π) Σ S_n/(√A_{n−1} + √A_n) + L0 (Eq. 34) — truncated-cone dimensional argument, L0 set by input entrance Reynolds number (default 1.0E+7).
- Berton divergence factors, Eqs. 58–59 (p. 20) — two-angle generalization of the classical λ (classical single-angle axisymmetric λ = (1+cos α)/2 is the ψj → 0 specialization; the report itself only gives the two-angle forms).
- Rocket validation accuracy: **≈ 5%** in gross thrust for ε = 440 and 1025 O2/H2 nozzles across O/F (p. 12). 2-D nozzle: excellent C_FG agreement for NPR ≥ 10; separation-dominated error at NPR ≈ 5 (p. 11, Fig. 5).
- Example numbers (App. II, 2-D test nozzle, NPR = 27.136, A9/A8 = 3.5): λ = 0.9917, F_G = 2116 lbf, F_GI = 2145 lbf, C_FG = 0.9866 (p. 53); C_FG across NPR 10–40 ranges 0.9347–0.9866 (pp. 53–60; Fig. II.5 p. 41).
- Example numbers (App. III, rocket nozzle, γ = 1.30, R = 113.3, pt7 = 2.699E5 psf, tt7 = 6589 R, ideal-expansion NPR = 2.699E+9 computed, A9/A8 = 440.16): M9 = 6.966, λ = 0.9746, F_G = 2689 lbf, F_GI = 2882 lbf, **C_FG = 0.9332** (pp. 66, 78–79).
- Defaults of record: npts = 51, nspl = 50, rei = 1.0E+7, gamma = 1.4, rgas = 53.35 ft·lbf/(lbm·R), pr = 0.72, xmus = 3.584E-7 lb·s/ft², ts = 491.6 R, cs = 198.6 R, eps = 1E-3, tol = 1E-6, con = 1E-6, del = 1E-2 (App. I pp. 31–32).

---

## 6. CONNECTIONS to the host program (flagging only; not adjudicated)

### C-1. CV gross-thrust identity as an independent integral oracle for F2 (STRONG)
Eq. 11 ≡ Eq. 12 ≡ Eq. 57 (pp. 16, 20) is an exact momentum-theorem identity: exit-plane flux integral = entrance flux + wall pressure + wall shear integrals. For the F2 general stratified-data MoC march, the MoC field furnishes *both* sides independently (exit-plane integral vs wall-pressure integral along the computed contour). Checking Eq. 11-vs-Eq. 12 closure on an MoC solution is a **derived, non-empirical rejector-style certificate** (an integral residual with a derivable tolerance from quadrature error), independent of NPAC's own 1-D internals. This is the cleanest single import: the identity is exact physics, not a model.

### C-2. Quasi-1D performance bookkeeping layer for F5 (STRONG)
The report is precisely the "quasi-1D performance bookkeeping" named for F5: C_FG (Eq. 1), C_d (Eqs. 86–87), C_V (Eqs. 88–89), C_e (Eq. 90), station-7/8/9 accounting, and per-segment momentum/pressure/shear ledgers (output format, p. 53). The station-7/8/9 + ideal-reference normalization scheme (Eqs. 3–10) is a ready-made, literature-anchored definition set for reporting RDE cycle-averaged C_FG/Isp. Caveat: all references are γ = const idealizations (Eqs. 8–10); for stratified inflow the "ideal" denominators need re-derivation (mass-flow-weighted ideal thrust over s(ψ), h0(ψ) profiles) — the *structure* transfers, the formulas do not.

### C-3. Cheap independent comparator engine for F2/F3 (MEDIUM-STRONG)
The three-pass 1-D marching model (Eqs. 21–25, 40–46) is trivially reimplementable (7×7 Newton per element) and validated to ~5% on ε = 440–1025 rocket nozzles (p. 12). As a **coarse cross-check** of MoC-computed thrust and station quantities (not of 2-D field structure), it is a genuinely independent comparator: different discretization, different physics closure level. Note the report's own demonstration (Fig. 4, p. 26) that a 1-D average tracks the between-walls average of a 2-D field — this is the argument for why a 1-D comparator is meaningful against the MoC engine at the integral level and *only* at the integral level.

### C-4. Berton two-angle divergence factor for F3 plug/aerospike (MEDIUM)
Eqs. 58–59 (p. 20) generalize λ to independent terminal angles ψi, ψj of outer and inner surfaces — directly the plug/cowl configuration of F3. Berton NASA TM 105176 (Ref. 5) is the primary source and a candidate acquisition for the program's literature registry. Anti-caveat: λ is a geometric exit-nonuniformity surrogate; the MoC engine computes the true divergence integral, so λ's role is comparator/sanity, not model.

### C-5. Mass addition/loss elements for F5 per-phase extraction-surface bookkeeping (MEDIUM)
Eqs. 24–25, 41–43, 47–54 (pp. 17, 19) give a complete, simple contract for a stream crossing a lateral surface: injected stream expands to local static pressure (Eq. 47), contributes u_a δṁ momentum and (c_p T_Ta + ½V_a²)δṁ energy; loss leaves at local state. For RDE cycle-averaged design, the "mass addition/loss across surfaces" formalism is structurally the same bookkeeping needed at a CFD-interface/extraction surface where cycle-averaged fluxes cross a control boundary. The δṁ ≪ ṁ smallness caveat (p. 6) marks the validity boundary.

### C-6. Friction + heat-transfer loss layer as F5 loss-accounting comparator (MEDIUM)
White–Christoph C_f (Eqs. 27–30) + Mangler axisymmetric correction (Eq. 36) + Reynolds analogy (Eqs. 37–38) is a self-contained, cheap viscous-loss estimate attachable to any inviscid core solution (NPAC attaches it to a 1-D core; the program could attach it to the MoC core the same way — second-pass-style, then optionally coupled). Useful for the F5 "friction, heat transfer" line items in gross-thrust bookkeeping. Rigor class: empirical correlation (see §7).

### C-7. Effective-length construction (Eq. 34) (WEAK but noteworthy)
The truncated-cone running-length rule with entrance-Reynolds offset L0 is a pragmatic device for Reynolds-number bookkeeping on segment-discretized geometry without an axial-length model. If the program ever attaches flat-plate-type correlations to MoC wall arcs, actual wall arc length is available and this surrogate is unnecessary — flag as *anti-pattern to avoid importing*: the MoC engine has the real geometry.

### C-8. Over/under-expansion treatment and separation gap (CONNECTION + ANTI-CONNECTION)
Over/under-expansion enters only through (P9 − P0)A9 (Eq. 2) and the CV form; the report documents the failure mode at low NPR from unmodeled separation (p. 11, Fig. 5). For the program's off-design adjudication this is both (a) a warning of the same modeling gap in any inviscid comparator, and (b) a quantified example of its sign and size (NPAC underpredicts C_FG when separation occurs — separation *raises* measured thrust by relieving over-expansion). No separation criterion is provided in NPAC — the program would need Summerfield/Schmucker-type criteria from elsewhere.

### Anti-connections (looks relevant, is not)
- **A-1. Gamma treatment:** NPAC is strictly γ = const per run; "real gas" in the validation means surrogate constant properties from CEC (p. 11–12). It contributes nothing to the program's variable-γ / tabulated-thermo machinery (gamma-variable-generality directive); any import must be re-derived for thermally-perfect tabulated cp(T).
- **A-2. Stratified inflow:** entrance flow assumed 1-D uniform (p. 4, "If the nozzle entrance flow is assumed to be one-dimensional then the first two integrals in Equation 12 become trivial"). NPAC has no s(ψ), h0(ψ), swirl capability; the entrance integrals in Eq. 12 would need full evaluation for stratified data — the identity survives, the "trivial" simplification does not.
- **A-3. Swirl:** no azimuthal momentum anywhere; the mass-addition angle θ is meridional (Fig. 3, p. 25). Nothing here for the program's swirl branch.
- **A-4. Numerical machinery (Eqs. 60–85):** generic 1986-era Newton/LU from Numerical Recipes; the program's JAX/adjoint stack supersedes it entirely. Historical interest only.
- **A-5. "Design" capability:** the abstract's "preliminary nozzle system design" means analyze-and-resize (throat-area rescaling, p. 4), not contour design; no variational or Rao-type content exists in this report.
- **A-6. Unsteadiness:** steady-flow code; no unsteady or cycle-averaged notions; any RDE use is strictly on already-cycle-averaged data.

---

## 7. Fidelity ledger (empirical/correlational vs derived)

| Item | Eqs. / page | Class | Notes |
|---|---|---|---|
| CV momentum theorem (gross thrust identities) | 11, 12, 55–57; pp. 16, 20 | **Derived (exact)** | Momentum theorem + algebra; λ insertion (56→57) is exact given λ's definition. |
| 1-D isentropic relations, mass-flow function | 3–10, 13–23; pp. 16–17 | **Derived** under ideal-gas, γ = const, 1-D | Textbook (NACA 1135); idealization boundary explicit (p. 3). |
| Fully-coupled 7×7 element equations | 40–46; p. 19 | **Derived** (1-D CV balances) with **modeling choices**: arithmetic averaging of P̄, τ̄w, q̄w across element; uniform-across-element assumption | Shapiro-type generalized 1-D flow; discretization choice unproven, no order-of-accuracy statement. |
| Mass-addition state (expand to P1) & mass-loss state (leave at local state) | 47–54; pp. 8, 19 | **Modeling assumption** (plausible, unproven) | Complete-expansion assumption stated, not validated separately. |
| White–Christoph compressible turbulent C_f | 27–30, 36; p. 18 | **Empirical correlation** | Flat-plate turbulent BL theory + calibration constants (0.455, 0.06); attached-flow, turbulent-only; no transition model. |
| Mangler/cone rule (Re_L/2) | 36; pp. 7, 18 | **Approximate transformation** ("approximate turbulent Mangler transformation") | Applied to surfaces i, j only in axisymmetric mode. |
| Recovery factor r = Pr^{1/3} | 32; p. 18 | **Empirical (turbulent BL)** | Standard turbulent recovery estimate. |
| Reynolds analogy C_h = C_f/(2Pr^{2/3}) | 37; pp. 7, 18 | **Empirical analogy** | "Approximately one half the skin friction coefficient." |
| Sutherland viscosity | 35; p. 18 | **Empirical fit** (gas-dependent constants) | Air defaults given; other gases = user's constants. |
| Effective length L (truncated-cone rule) + L0 from input Re | 33–34; pp. 6–7, 18 | **Heuristic/dimensional argument** | Explicitly "not a physical length"; entrance-BL state carried by a single user Reynolds number (default 1E+7 is a pure convention). |
| Berton divergence factor λ | 58–59; pp. 8–9, 20 | **Derived under model assumptions** (source-flow-type exit; Berton TM 105176) | Geometric; depends only on final segment angles; NPAC cites, does not re-derive. |
| Gas model (γ, R, Pr constant; CEC surrogate for combustion gas) | pp. 4, 11–12, 32, 35 | **Idealization**; surrogate-property practice is **procedural, uncertified** | Report itself attributes part of the 5% rocket-case error to it. |
| Validation claims (Figs. 4–6) | pp. 10–12, 26–28 | **Empirical evidence**, normalized presentations | Fig. 5 normalized to max experimental C_FG (absolute level not recoverable from figure); Fig. 6 is a thrust *ratio*; underlying data: proprietary P&W (Ref. 10) and NASA TP 3576 (Ref. 11). |
| Numerics (Newton, LU, tolerances) | 60–85; pp. 9–10, 20–22, 32, 35 | **Standard algorithms**; tolerances are conventional defaults, not derived | eps/tol/con/del are magic-number defaults by the program's R5 standard. |

### Key references carried by the report (p. 13)
1. Stitt, NASA RP 1235 (1990) — ideal thrust. 2. NACA Report 1135 (1953). 3. White, Viscous Fluid Flow (1974). 4. Shapiro Vol. I (1953), pp. 219–260. 5. **Berton, NASA TM 105176 (1991)** — divergence loss, candidate acquisition. 6. Press et al. (1986). 7. INGRID (AEDC-TR-86-49). 8. PARC (AEDC-TR-89-15). 9. Baldwin–Barth (NASA TM 1002847, 1990). 10. NASA-Lewis / Pratt & Whitney test data (unpublished). 11. **Jankovsky/Kazaroff/Pavli, NASA TP 3576 (1996)** — high-area-ratio rocket nozzle experiment, candidate acquisition. 12. Gordon & McBride, NASA SP 273 (1971).
