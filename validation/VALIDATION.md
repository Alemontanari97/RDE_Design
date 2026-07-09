# Validation report — Presentazione_CVA

Every model and script behind the lecture was validated on three independent pillars. All computations use Cantera 3.2 (GRI‑Mech 3.0; n‑dodecane for kerosene), following the SD Toolbox equilibrium‑Hugoniot method.

## Pillar 1 — Comparison with published reference values (`validate.py`, 33 checks, all pass)

Chapman–Jouguet state vs. the Caltech Detonation Database / CEA (1 atm, 300 K, φ = 1):

| Mixture | U_CJ computed | U_CJ ref | error | T₂ err | p₂/p₁ err |
|---|---|---|---|---|---|
| H₂/air | 1969 m/s | 1971 | 0.10 % | 0.11 % | 0.73 % |
| H₂/O₂ | 2836 m/s | 2836 | 0.01 % | 0.04 % | 1.23 % |
| CH₄/air | 1803 m/s | 1804 | 0.05 % | 0.12 % | 0.75 % |
| C₂H₄/air | 1824 m/s | 1825 | 0.06 % | 0.06 % | 0.89 % |
| C₂H₂/O₂ | 2425 m/s | 2424 | 0.03 % | 0.07 % | 0.78 % |
| C₃H₈/O₂ | 2357 m/s | 2360 | 0.12 % | 0.13 % | 0.07 % |

Also verified: von Neumann p_vN/p_CJ ≈ 1.8; Fickett–Jacobs efficiency 0.28–0.30 (fuel–air) / 0.18–0.22 (fuel–O₂) matching Wintenberger–Shepherd (fuel–O₂ *lower* due to dissociation); cycle ordering η_det ≳ η_Humphrey > η_Brayton; Brayton closed form; standing‑detonation total‑pressure loss p_t2/p_t1 ≈ 0.014.

## Pillar 2 — Internal consistency & cross‑method checks (`validate_v2.py`, 22 checks)

Each model proves itself, independent of any reference table:

- **CJ tangency:** the equilibrium‑sonic condition M₂,eq = 1.000 holds for all 8 gas‑phase mixtures (the *defining* CJ property).
- **von Neumann:** the frozen post‑shock state satisfies mass, momentum and energy jump conditions to machine precision (residuals ~10⁻¹⁴) for every mixture.
- **ZND integration:** the energy invariant h + U²/2 is conserved along the whole reaction zone to 6×10⁻⁶ %; the kinetic endpoint converges to the independently‑computed equilibrium CJ temperature (two methods agree < 1 %); T_vN matches the frozen‑shock value exactly.
- **Cycles:** Humphrey energy‑balance = closed form; the detonation cycle at π_c = 1 reproduces the Fickett–Jacobs one‑γ formula (0.2531).
- **Entropy split:** Δs_min + Δs_irr = Δs_total (identity).
- **Shepherd–Kasahara:** the exact form F_I/Ṁ = ΔP_CJ·K/(ρ_c U_CJ) and the approximation K·U_CJ/(γ_e+1) agree within 3 %.

## Pillar 3 — Independent expert audit (fresh‑eyes subagent)

The CJ/von Neumann/ZND code and the five key deck equations (Shepherd–Kasahara pressure‑history and axial‑flow, Fickett–Jacobs efficiency, Stechmann thrust and mass‑weighted I_sp) were audited line‑by‑line against the source PDFs. **No physics errors found** — the enthalpy Hugoniot form, frozen‑vs‑equilibrium states, Rayleigh speed, thermicity, and ZND eigenvalue equation are all correct, and every equation faithfully reproduces its paper.

## Bug caught and fixed during validation

The first draft mis‑applied the Fickett–Jacobs efficiency formula (real Cp/q_c with the one‑γ M_CJ, which are mutually inconsistent), giving η ≈ 0.5–0.8. Recomputed correctly as the realistic cycle work (h₁ − h₅)/q_c, giving η ≈ 0.28/0.20 in agreement with the paper. The deck was corrected.
