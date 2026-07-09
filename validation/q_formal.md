# Where q comes from — conservation equations, standard-state definition, Cantera verification

*Generated with `scripts/q_formal.py` on 2026-07-09 (Cantera 3.2, `gri30.yaml`; CJ states via SD Toolbox `PostShock_eq` at the stored U_CJ of `data/cycles_ws.json`). Numbers in `data/q_formal.json`. Companion documents: `data/q_mapping.md` (q̃ normalizations, mixture map, M_CJ inversion) and `data/cycles_validation.md` note 7 (ZND geometry of `fig_cycles_pv`). Slide-ready; speaker notes at the end.*

*Rigor revision 2026-07-09 (requested by the lecturer): the formal definition is now anchored to the **standard state** T_ref = 298.15 K (it was previously left at a generic reference, with T_ref = T₁ offered as a convenient gauge). The exact relation between q° and the calorimetric difference at (T₁,p₁) is stated and verified numerically at T₁ = 300 K and T₁ = 700 K.*

## 1. The conservation equations contain no q

Steady planar combustion wave, wave-fixed frame, velocities w (for the CJ wave of the cycle, w₁ = U_CJ). The Rankine–Hugoniot system is

- mass:      ρ₁ w₁ = ρ₂ w₂
- momentum:  p₁ + ρ₁ w₁² = p₂ + ρ₂ w₂²
- energy:    **h°₁ + w₁²/2 = h°₂ + w₂²/2**

where h° is the **absolute (total) specific enthalpy** of the mixture — chemical + sensible:

h°(T, Y) = Σᵢ Yᵢ hᵢ(T),  hᵢ(T) = Δh°f,i(T_ref) + ∫_{T_ref}^{T} c_p,i(T′) dT′,  T_ref = 298.15 K.

The energy equation is *identical* for an inert shock and for a detonation: **no heat-addition term q appears anywhere**. The wave is adiabatic and does no external work; what a flame or detonation "releases" is bookkept *inside* h° by the composition change Y₁ → Y₂ at fixed elemental content.

## 2. The formal definition: q° at the standard state

Split h° into chemical and sensible parts, h° = h_chem + h_s with h_chem(Y) ≡ Σᵢ Yᵢ Δh°f,i(T_ref) and h_s(T,Y) ≡ Σᵢ Yᵢ ∫_{T_ref}^{T} c_p,i dT′. The energy equation becomes h_s,1 + q° + w₁²/2 = h_s,2 + w₂²/2 (exact for any T_ref), with the **standard-state heat release**

**q° ≡ Σᵢ Y_i,1 Δh°f,i(T_ref) − Σᵢ Y_i,2 Δh°f,i(T_ref),  T_ref = 298.15 K.**

Three points of rigor:

1. **q° is not a heat flux.** It is the formation enthalpy converted into sensible enthalpy + kinetic energy by the recomposition Y₁ → Y₂. The "heat-addition" picture of the one-γ model (Eqs. A18/A21, B2) is this bookkeeping, not an energy source.
2. **q° is a number only once Y₂ is specified.** Inside the reaction zone the composition varies continuously, so the *released-so-far* q°(x) = Σᵢ [Y_i,1 − Y_i(x)] Δh°f,i(T_ref) grows from 0 at the frozen post-shock (von Neumann) state to its CJ-plane value — exactly the progress-variable heat release λ(x)·q of the ZND model, i.e. the descent of the Rayleigh line vN → CJ shown in `fig_cycles_pv`.
3. **Why the *standard* state, and not the initial T₁.** The Δh°f,i are tabulated at 298.15 K: anchoring the definition there makes q° a pure thermochemical constant of the reaction Y₁ → Y₂, independent of the operating point. Defining "q" with enthalpies evaluated at a generic T₁ instead folds a **sensible-enthalpy mismatch** ∫(c_p,react − c_p,prod)dT into a nominally chemical quantity — invisible at T₁ ≈ 300 K but already percent-grade at a preheated T₁ = 700 K, *with a mixture-dependent sign* (§4). (Formally any T_ref gives a consistent split and identical observables, since the sensible terms compensate; but the *number called q* changes with T_ref, so the definition is fixed at the standard state and flagged by the ° superscript.)

## 3. Exact relation to the calorimetric difference at (T₁, p₁)

Evaluating reactants and products at the *same* state (T₁,p₁) and using the split of §2 (fixed product composition Y₂):

**h₁(T₁,p₁) − h_prod(T₁,p₁) = q° + ∫_{T_ref}^{T₁} (c_p,react − c_p,prod) dT′.**

This is an identity, not an approximation: the left side adds to q° exactly the mismatch of the two sensible enthalpies between T_ref and T₁. Consequences:

- The cycle analysis (Paper B Eq. 1; `data/q_mapping.json`) uses q_c ≡ h₁(T₁,p₁) − h₆(T₁,p₁), state 6 = **equilibrium** products at the initial (T₁,p₁). That q_c is the left side above (equilibrium composition ≡ major products to ≤ 10⁻¹⁰ relative for T₁ ≤ 700 K, verified in §4): **q_c(T₁) = q° + ∫_{T_ref}^{T₁}(c_p,react − c_p,prod)dT′.**
- At the project's initial state T₁ = 300 K the integral term is **negligible but conceptually distinct**: |∫| = 0.26 kJ/kg (H₂–air) and 0.06 kJ/kg (CH₄–air), i.e. **< 0.01 % of q°** — it is sensible heat-capacity mismatch over 1.85 K, not chemistry. So q_c(300 K) ≅ q° and all 300 K values used project-wide are unaffected.
- At T₁ = 700 K the same term is +53.9 kJ/kg (+1.58 %) for H₂–air and −8.2 kJ/kg (−0.30 %) for CH₄–air: at preheated initial states the distinction q° vs h₁ − h_prod(T₁) is numerically real, and only the standard-state q° remains a mixture constant.
- Convention: H₂O stays vapour (gas-phase equilibrium; X_H₂O = 0.35/0.19 exceeds p_sat/p ≈ 0.035 at 300 K, i.e. state 6 is a supersaturated ideal-gas state). q° is therefore the lower-heating-value heat of combustion per kg of mixture; the LHV basis is used consistently across the project, so no condensation enthalpy enters q_c or η.

## 4. Cantera verification (φ = 1, p₁ = 1 bar, gri30.yaml)

Route (q°): Σᵢ (Y_i,1 − Y_i,2) Δh°f,i(298.15 K) with the mechanism's own formation enthalpies and **major products** (H₂–air → H₂O + N₂; CH₄–air → CO₂ + 2 H₂O + N₂); computed both as h_react(298.15) − h_majors(298.15) and as the explicit per-species sum (agreement < 1 J/kg). Calorimetric routes at T₁ ∈ {300, 700} K: frozen majors, h₁(T₁) − h_majors(T₁), and equilibrium products, h₁(T₁) − h_eq(T₁) (HP → TP equilibration; the `q_mapping`/`cycles_ws` definition at 300 K). The sensible integral I(T₁) = ∫_{T_ref}^{T₁}(c_p,react − c_p,prod)dT′ is obtained from the identity I = [h₁ − h_majors](T₁) − q° **and** cross-checked by direct 201-node quadrature of the c_p difference (agreement < 1 J/kg).

| mixture | q° (298.15 K) [MJ/kg] | h₁−h_prod (300 K) [MJ/kg] | I(300 K) [kJ/kg] (% of q°) | h₁−h_prod (700 K) [MJ/kg] | I(700 K) [kJ/kg] (% of q°) |
|---|---|---|---|---|---|
| H₂–air  | 3.42134 | 3.42160 | +0.26 (+0.0076 %) | 3.47523 | +53.89 (**+1.58 %**) |
| CH₄–air | 2.76073 | 2.76067 | −0.06 (−0.0023 %) | 2.75251 | −8.23 (**−0.30 %**) |

Frozen-majors and equilibrium routes coincide at both temperatures (relative difference ≤ 8·10⁻¹¹; largest non-major mole fraction 7·10⁻¹⁸/8·10⁻²⁰ at 300 K, 3·10⁻¹¹/2·10⁻¹¹ at 700 K), so h_prod is unambiguous here.

**Reading.** At T₁ = 300 K the calorimetric difference reproduces q° to < 0.01 % — the residual is exactly the 298.15 → 300 K sensible shift (mean c_p mismatch +140 / −34 J kg⁻¹K⁻¹ over 1.85 K), not a composition effect. By T₁ = 700 K the sensible term has grown to +1.58 % (H₂–air) / −0.30 % (CH₄–air) of q° — *opposite signs*: c_p,react − c_p,prod > 0 for H₂–air (H₂ has an enormous specific heat) and < 0 on average for CH₄–air. A "q defined at T₁" would therefore drift with preheat and even change direction of drift with the fuel, while q° stays fixed; this is why the formal definition is anchored at 298.15 K and the T₁-dependence is carried *explicitly* by the integral term. The equilibrium definition q_c = h₁ − h₆ remains the correct calorimetric quantity at any T₁ (it is the left side of the §3 identity); at 300 K it coincides with q° for all practical purposes.

## 5. q_eff vs q_thermo: dissociation, and why the one-γ q̃ is calibrated on M_CJ

The q_c of §3 at 300 K (call it **q_thermo = q_c ≅ q°**) presumes *complete* recombination — products brought back to (T₁,p₁). At detonation temperatures the equilibrium composition is far from the major set: part of the formation enthalpy is still stored in radicals and CO/H₂ at the CJ plane, and is returned only along the recombining (shifting-equilibrium) expansion. Same script, same states:

| mixture | T_CJ [K] | p_CJ [bar] | released at CJ plane [MJ/kg] | fraction of q_c | withheld mainly in (X at CJ) |
|---|---|---|---|---|---|
| H₂–air  | 2943 | 15.5 | 2.85 | **83.2 %** | H₂ 0.031, OH 0.018, O₂ 0.008, NO 0.008, H 0.006 |
| CH₄–air | 2777 | 17.0 | 2.33 | **84.2 %** | CO 0.024, O₂ 0.010, OH 0.009, H₂ 0.008, NO 0.007 |

Consequences:

- **q_eff < q_thermo where dissociation persists.** In fuel–O₂ mixtures (T_CJ ≈ 3700–4200 K) the withheld fraction is much larger and partly never recovered within the cycle: q_eff/q_c = 0.63–0.84 (`data/q_mapping.md`, mixture table) — the papers' mechanism for the poor fuel–O₂ η_FJ. For fuel–air, q_eff/q_c ≈ 1.2 instead *exceeds* one: not physics but referencing — M_CJ is measured against the frozen reactant sound speed (γ₁ ≈ 1.39–1.40) while the one-γ model implies a₁ = √(γ R T₁) with the products' γ (see `data/gamma_phase_audit.md`).
- **Why calibrate q̃ on M_CJ.** The one-γ model admits a single (q̃, γ) pair, and *every* observable of its detonation branch — jump ratios (A19–A20), entropy rise (A22), the FJ efficiency closed form (A57 = B3) — is a function of M_CJ alone. B2 inverts exactly: q̃ = (M_CJ² − 1)²/(2(γ+1)M_CJ²) (`data/q_mapping.md`, items 3–4). Feeding the model the thermochemical q̃ = q_c/(c_p T₁) would misplace M_CJ and *every* downstream number; feeding it the q̃ inverted from the physical M_CJ reproduces the wave dynamics by construction, at the price of an *effective* heat release that silently absorbs dissociation and the sound-speed referencing. That is the declared convention of the lecture's one-γ figures (`fig_cycle_family`), with the mixture-by-mixture map in `data/q_mapping.md`.

## 6. Slide box (verbatim)

> **Energy across the wave (RH):** h°₁ + w₁²/2 = h°₂ + w₂²/2 — adiabatic: *no q in the physics*. Folding the chemistry into h° = h_s + Σᵢ Yᵢ Δh°f,i(T_ref), the jump reads h_s,1 + q° + w₁²/2 = h_s,2 + w₂²/2.
> **Definition (standard state):** q° ≡ Σ Y_i,1 Δh°f,i(T_ref) − Σ Y_i,2 Δh°f,i(T_ref), T_ref = 298.15 K — a thermochemical constant of Y₁ → Y₂, not tied to the operating T₁.
> **Exact link to the cycle's q_c = h₁ − h₆ (Paper B, Eq. 1):** h₁(T₁,p₁) − h_prod(T₁,p₁) = q° + ∫_{T_ref}^{T₁}(c_p,react − c_p,prod)dT′. At T₁ = 300 K the integral is +0.26/−0.06 kJ/kg (< 0.01 % of q°) — negligible, but conceptually distinct; at T₁ = 700 K it is +1.6 %/−0.3 %.
> **Cantera, φ = 1, 300 K, 1 bar: H₂–air 3.42, CH₄–air 2.76 MJ/kg** (q° and h₁ − h_eq agree to < 0.01 %).
> **At the CJ plane only ≈ 83–84 % of q_c is out** (rest stored in CO, H₂, OH, NO, …; recovered during the recombining expansion) → one-γ q̃ is calibrated on M_CJ, not on q_thermo.

## 7. Speaker notes

1. Start from the paradox: the detonation energy equation has no q. Write RH with total enthalpy; stress that the same three lines describe an inert shock — chemistry only changes which composition sits on each side.
2. Define q° by splitting formation from sensible enthalpy **at the standard state T_ref = 298.15 K, where the Δh°f are tabulated**; say explicitly "q° is a definition, not a source term — and it is a constant of the reaction, not of the operating point". If the audience knows ZND: the partial sums Σ(Y₁ − Y(x))Δh°f(T_ref) are the λq of ZND — this is precisely the descent of the Rayleigh line from the von Neumann point to CJ in the p–v figure (`fig_cycles_pv`).
3. Tie to the cycle number via the exact identity h₁(T₁,p₁) − h_prod(T₁,p₁) = q° + ∫_{T_ref}^{T₁}(c_p,react − c_p,prod)dT′: with products *equilibrated at the initial state* the left side is q_c = h₁ − h₆ of Wintenberger–Shepherd (their Eq. B1) — the denominator of every η in the lecture. At T₁ = 300 K the integral is 0.26/−0.06 kJ/kg, i.e. < 0.01 % — that is why q_c(300 K) and q° are used interchangeably; at T₁ = 700 K it is already +1.58 %/−0.30 % with opposite signs, so the two concepts must not be conflated at preheated inlet states.
4. Show the table: q° vs the calorimetric difference at 300 K and 700 K, two mixtures; identity cross-checked by direct quadrature of Δc_p; the equilibrium products at both temperatures are the textbook majors to 10⁻¹¹–10⁻¹⁸ — so "LHV" is not an assumption here, it is the computed equilibrium (H₂O vapour by gas-phase convention).
5. Anticipate the objection "then why does anyone speak of effective q?": at CJ temperatures ~16 % of q_c is still locked in dissociated species (second table); fuel–O₂ mixtures never give it all back — q_eff/q_c down to 0.63.
6. Close the loop with the one-γ model: single q̃, single γ ⇒ calibrate q̃ on the observable that fixes the whole branch, M_CJ (exact inversion of B2). This is why `data/q_mapping.md` reports both q_c and q_eff per mixture and why the family curves of `fig_cycle_family` are labelled by q_c/RT₁ with a mixture map rather than by raw heating values.
7. If asked about magnitudes: q°(H₂–air) > q°(CH₄–air) per kg of *mixture* (3.42 vs 2.76 MJ/kg) even though per kg of *fuel* hydrogen dominates (120 vs 50 MJ/kg) — the stoichiometric air dilution rescales everything; q̃ = q_c/c_pT₁ ≈ 4.0 vs 4.4 brings them back together (q_mapping table).
