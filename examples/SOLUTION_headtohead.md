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
**(c) Mass flow — set by choking, not by the divergent.** The annulus exit is the sonic throat (SK axial: w = a_eq there; Stechmann: ṁ(t) = P_c(t)·A_t/c\*(t), mass-weighted). **At fixed A_t, adding the divergent does not change ṁ — it raises F.** Two rigorous closures: (i) *minimum propellant*: ṁ = F/(g₀·245.3) = **249 g/s** ⇒ A_t from the choked relation (smaller throat); at that ṁ the chamber (SK, nozzle-less, per-unit-mass hence ṁ-independent) contributes 249·1979 = **493 N** and the divergent the remaining **107 N (18%)** — a clean physical decomposition of the two models on the *same* hardware; (ii) *nozzle-less engine* (larger throat): ṁ = 303–315 g/s from the two SK CVs (PH 1979.1 m/s, Term I 1679.1 + Term II 300.0; axial 1904.7 m/s — their ~4% spread is the model uncertainty) also meets 600 N, with more propellant. The reproducible chain uses the ṁ = 0.30 kg/s workhorse; at the 249 g/s closure the detonability checks still pass (l_fill = 16.7 mm, W = 2.23 → ~2 heads).
**(d) Fill & wave count (Wolański):** u_fill = 168 m/s, l_fill = 20.1 mm/rev (25% of L); W = l_fill/l_cr = 2.69 [1.90–4.61] ⇒ **2–3 co-rotating heads** (band 1–4).
**(e) Cycle context:** η_FJ = 0.2042 (fuel-O₂ dissociation penalty; fuel-air would reach ~0.30) vs Brayton at π_c = 1: 0 — the ideal-cycle gap that Part 2 converts into a realizable ΔIsp.
**(f0) Who is who among the three pressures (read before f).** P_cp = 10 atm exists nowhere in the RDE at any instant: it is the *equivalent steady chamber* of the reference CP engine — the pump/feed-system class and, by construction of the matching, the cycle-MEAN mass flux. At a fixed azimuthal station the local pressure over one lap does: wave passage (1.11 → 37 atm CJ jump, injectors momentarily blocked/reversed — Wolański Fig. 31) → exponential blowdown → injectors reopen below manifold pressure and the fresh layer accumulates during the LOW-pressure tail → the next wave finds that layer at **P_init = 1.11 atm** (the pre-detonation static state, i.e. state 1 of the CJ jump; periodicity closes the cycle exactly there, P_c(t_c) = P_init). The matching is where 10 atm enters: mean of ṁ(t) over the 37→1.11 exponential = the 10-atm steady engine through the same throat (indeed P̄_c ≈ 10.2 atm, DC +2.4%). The 1.1→37 atm swing from a 10-atm-class feed IS the pressure gain in the EAP sense; injector drop not modelled (declared).

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
Same procedure at F = 10 kN, P_cp = 20 atm, envelope OD ≤ 320 × L ≤ 260 mm (`examples/example_design_10kN.py`): CJ 2390.3 m/s, γ_e = 1.1307; ṁ set by choking at the annulus-exit throat: mission closure 3.66 kg/s (spike config) ⇒ chamber share (SK) 7.3 kN + divergent 2.7 kN; a nozzle-less design would need 5.01 kg/s; annulus R̄ = 140 mm, gap 15 mm, L = 180 mm with λ = 2.5 mm ⇒ l_fill/λ = 38 ✓, gap/λ = 6 ✓, D̄/λ = 112 ✓, **W = 3.14 [2.2–5.4] → ~3 co-rotating heads** (multi-wave operation is the norm at this scale). RDE: bell ε\* = 4.04 → 268.0 s; **aerospike ε\* = 10.64 → 278.4 s**; choke margin 1.39 (fully choked cycle — contrast with 0.64 at 10 atm). CP at ITS optimum: ε\* = 4.04 (same, structural), **261.2 s**, ṁ = 3.90 kg/s, L_chamber ≈ 91 mm (+ nozzle) on a 220-mm bore. **Verdict: +6.6% Isp, −6% propellant at the same pump** — the advantage persists at scale; the higher P_cp narrows the spike-vs-bell gap (blowdown swing relatively smaller), exactly the Table-1 trend.
