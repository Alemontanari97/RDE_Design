# Worked solution — mission-constrained design & head-to-head verdict
**Course capstone (deck slide 60).** All numbers reproduce with `python examples/example_design_study.py` and `python examples/example_headtohead.py` (assert-guarded; ≈30–60 s total). Model validation pedigree: CJ ≤0.1% vs literature; SK ±0.2% (axial) vs its Table 1; Stechmann 18/18 rows; cycles 99/99 (see `validation/`).

## 1. Problem statement
**Mission** (ground static demonstrator): thrust **F = 600 N at sea level**, ambient **P_a = 101.325 kPa constant** (no trajectory); envelope **OD ≤ 110 mm × L ≤ 100 mm** (usable bore 90 mm ⇒ exit D_e ≤ 100 mm); propellant **C₂H₄/O₂, φ = 1, T₁ = 300 K**; **feed equivalence**: same mean chamber pressure **P_cp = 10 atm** for both engines (= same specific pump work; injector drop not modelled).

**Formal optimization, each engine independently:**
max over (ε, ṁ) of Isp(ε), subject to F = ṁ·g₀·Isp, D_e(ε) ≤ 100 mm; CP combustor: L_chamber = L*·A_t/A_c within envelope (L* = 0.9 m, LOX/HC class); RDE: detonability (cell criteria) and cycle choking as referees.
Bell optimum: analytic condition NPR(ε\*) = P̄_c/P_a (from dC_F/dε = (P_e−P_a)/P_c with ṁc\* = P_cA_t), verified by golden-section (|Δε| ≤ 10⁻³). Aerospike optimum: saturation knee NPR(ε\*) = P_max/P_a (Eq. 12 validity limit).

## 2. Assumptions & applicability (per step)
CJ state: **equilibrium** Hugoniot, sonic in a_eq (proof: deck B12). SK thrust: γ_e = ρ₂a²_eq/p₂, Term II with u_c = 300 m/s; **upper bounds** (mixing losses not modelled). Expansion: equilibrium isentrope = upper bound; frozen-from-CJ −10.0% on Isp_f here; Bray throat-freeze −0.2…−2% (deck B13). Stechmann: CEA-equilibrium products, γ const along nozzle, **mass-weighted** cycle Isp; no separation model; late-cycle choke margin 0.64 → assumption 3 retained exactly as the paper does on its own 20-atm hydrocarbon rows.

## 3. Part 1 — RDE design chain (C₂H₄/O₂)
**(a) CJ state (SD Toolbox):** U_CJ = 2373.5 m/s, p_CJ/p₁ = 33.18, T_CJ = 3934 K, γ_e = 1.1387 (γ_fr = 1.2365).
**(b) Geometry from detonability (λ-criteria, deck slide 26):** λ ≈ 29·Δᵢ = 0.62 mm (Δᵢ = 0.021 mm); Bykovskii l_cr = (12±5)λ = 7.5 [4.4–10.6] mm. Chosen annulus R̄ = 45 mm, gap 5 mm, L = 80 mm ⇒ checks: l_fill/λ ≈ 34 ≥ 12±5 ✓, gap/λ ≈ 8 ≥ ~2.4 ✓, D̄/λ ≈ 150 ≥ 28–40 ✓ (≥2× margin everywhere).
**(c) Mass flow from thrust — declare the configuration.** The SK pair are both **nozzle-less** control volumes: they bracket the *chamber-only* sizing, ṁ = 600/1979 ≈ **0.303 kg/s** (pressure-history, Term I 1679.1 + Term II 300.0 = 15.2%) to **0.315 kg/s** (axial-flow, 1904.7 m/s). Either CV is equally legitimate — they are the two faces of the same engine and their ~4% spread is the model uncertainty. With the step-(f) nozzle the specific thrust rises to g₀·245.3 = 2406 m/s ⇒ **mission ṁ = 249 g/s**; the SK bracket remains the nozzle-less bound and cross-check. CJ state is ṁ-independent: the chain scales linearly.
**(d) Fill & wave count (Wolański):** u_fill = 168 m/s, l_fill = 20.1 mm/rev (25% of L); W = l_fill/l_cr = 2.69 [1.90–4.61] ⇒ **2–3 co-rotating heads** (band 1–4).
**(e) Cycle context:** η_FJ = 0.2042 (fuel-O₂ dissociation penalty; fuel-air would reach ~0.30) vs Brayton at π_c = 1: 0 — the ideal-cycle gap that Part 2 converts into a realizable ΔIsp.
**(f) Nozzle (Stechmann matched cycle at P_cp = 10 atm):** P_CJ = 37.0 atm from a 10-atm feed (the EAP logic of pressure gain), PR = 33.4, DC = +2.4%; **bell ε\* = 2.44 → 233.6 s; aerospike ε\* = 6.27 → 245.3 s** (+5.0% over the fixed bell). Frozen-composition bound: −10.0% (know it, quote equilibrium).

## 4. Part 2 — conventional CP engine at ITS own optimum (same mission, same feed)
**(a) Chamber state** (`cp_state`, HP-equilibrium at 10 atm): γ_s = 1.1247, c\* = 1746 m/s.
**(b) Nozzle optimum:** matched exit, ε\* = 2.44 (NPR\* = 10), C_F = 1.2771 ⇒ **Isp = 227.4 s**; ṁ = 600/(g₀·227.4) = **269 g/s**.
**(c) Combustor feasibility (the realistic CP constraint):** A_t = ṁc\*/P_c = 4.64 cm²; V_c = L*·A_t = 417 cm³; on the 90-mm usable bore: **L_chamber ≈ 66 mm — it fits** the 100-mm envelope. State it honestly: at 600-N scale, compactness is *margin*, not knockout; it becomes decisive at larger F (V_c ∝ ṁ, while the RDE heat-release zone stays at cell scale).

## 5. Verdict (each at its own optimum)
| | CP engine | RDE bell | RDE aerospike |
|---|---|---|---|
| Sea level, ε\* | 2.44 | 2.44 | 6.27 |
| **Isp [s]** | **227.4** | 233.6 (+2.7%) | **245.3 (+7.9%)** |
| ṁ for 600 N [g/s] | 269 | 262 | **249 (−7%)** |
| Vacuum, ε = 15 (envelope-capped) | 329.6 | 335.2 | 335.2 (+1.7%) |

The ε\* coincidence (2.44 = 2.44) is structural: the bell optimum obeys NPR\* = P̄_c/P_a and the det cycle is *matched* on the same mean pressure — it is the **aerospike riding the blowdown swing** that escapes to 6.27 and collects +7.9%. In vacuum at envelope-capped ε the aerospike has no ambient to adapt to (collapses onto the bell) and the det advantage shrinks to the mass-weighted cycle gain (+1.7%). **The RDE advantage depends on the operating point — the verdict is computed, not assumed.**

## 6. Sensitivities & what could flip the verdict
λ band ×[0.7–1.4] → W ∈ [1.9–4.6] (mode-jump risk, not a performance flip). Frozen-expansion bound applies to both engines comparably (−7…−10% class) — the *relative* det gain survives. L* ∈ [0.8–1.0] m → L_chamber 59–73 mm (still fits). Choke margin 0.64: tail below choking, retained as in the source paper. Nothing inside the validated bounds flips the sea-level sign; the vacuum case already shows the honest lower end (+1.7%).

## 7. Reproducibility
```
python examples/example_design_study.py    # Part 1 chain (asserts on every step)
python examples/example_headtohead.py      # Part 2 verdict, SL + vacuum (asserts)
```
Expected key outputs: 2373.5 m/s · W 2.69 · 1979.1/1904.7 m/s · 233.6/245.3 s · CP 227.4 s @ ε\*2.44 · L_ch 66 mm · VAC 329.6/335.2 s.

## 8. Scaling case — 10 kN, CH₄/O₂ (LOX/methane class)
Same procedure at F = 10 kN, P_cp = 20 atm, envelope OD ≤ 320 × L ≤ 260 mm (`examples/example_design_10kN.py`): CJ 2390.3 m/s, γ_e = 1.1307; mission ṁ = 3.66 kg/s (nozzle config; SK nozzle-less bracket 5.01 kg/s — bases declared); annulus R̄ = 140 mm, gap 15 mm, L = 180 mm with λ = 2.5 mm ⇒ l_fill/λ = 38 ✓, gap/λ = 6 ✓, D̄/λ = 112 ✓, **W = 3.14 [2.2–5.4] → ~3 co-rotating heads** (multi-wave operation is the norm at this scale). RDE: bell ε\* = 4.04 → 268.0 s; **aerospike ε\* = 10.64 → 278.4 s**; choke margin 1.39 (fully choked cycle — contrast with 0.64 at 10 atm). CP at ITS optimum: ε\* = 4.04 (same, structural), **261.2 s**, ṁ = 3.90 kg/s, L_chamber ≈ 91 mm (+ nozzle) on a 220-mm bore. **Verdict: +6.6% Isp, −6% propellant at the same pump** — the advantage persists at scale; the higher P_cp narrows the spike-vs-bell gap (blowdown swing relatively smaller), exactly the Table-1 trend.
