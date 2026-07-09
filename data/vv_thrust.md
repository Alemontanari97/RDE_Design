# V&V - analytical thrust models (PH / axial / Stechmann)

Pipeline: scripts/thrust_models.py -> data/thrust_models_all.json (16 cases: 12 std @ 1 atm/300 K + 4 SKREP @ 1.5 atm/255 K).
No number is reported without a cross-check; verdicts below.

## Checks

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | U_CJ vs results_main.json (9 validated combos, <0.5%) | **PASS** | max +0.19% (n=9 combos, threshold 0.5%) |
| 2 | CJ state vs SK Table 2 literature (5 mixtures) | **PASS** | max errU 0.1 pct, errP 1.7 pct (5 mixtures, precomputed sk_tables.json) |
| 3a | SK Table-1 replica: model INPUTS (U_CJ, P_CJ, gamma_e, rho_c, Y_f) | **PASS** | U_CJ<=0.05 pct, gamma_e exact to 3 dp, P_CJ<=1.5 pct on all 4 cases |
| 3b | Axial-flow Isp_f vs SK Table 1 (4 cases) | **PASS** | all 4 within 0.2% |
| 3c | Pressure-history Isp_f vs SK Table 1 (4 cases) | **PASS*** | 3/4 within 4.2 pct; C2H4-O2 published 704 s NOT reproducible (we get 937 s) - documented anomaly |
| 4 | Axial internal: Pm/P2 range, CJ sonicity, exit-pressure insensitivity | **PASS** | Pm/P2 in [0.218,0.234] (SK: ~0.22-0.25); CJ sonic residual <= 0.0016; sonic-vs-matched +2.1..+17.3% |
| 5 | Stechmann internal: CP-collapse, mass- vs time-weighting, choking | **PASS** | CP-collapse rel.err 2.1e-11; mass-weighted > time-averaged for 6/6; choked fraction 81-85% of cycle |
| 6 | Cross-model coherence PH / axial / Stechmann (fuel-O2) | **PASS** | PH vs axial-sonic vs Stechmann(eps=1,SL) total-mass Isp spread 4.4-9.0% (6 fuel-O2 combos) |

## Check 1 detail - U_CJ vs results_main.json

| Mixture | U_CJ new [m/s] | U_CJ results_main [m/s] | d% |
|---|---:|---:|---:|
| C12H26/O2 | 2341.0 | 2336.5 | +0.191 |
| C2H2/O2 | 2424.8 | 2424.8 | -0.000 |
| C2H4/O2 | 2373.5 | 2373.5 | -0.000 |
| C2H4/air | 1823.9 | 1823.9 | -0.000 |
| C3H8/O2 | 2357.3 | 2357.3 | +0.000 |
| CH4/O2 | 2390.3 | 2390.3 | -0.000 |
| CH4/air | 1803.1 | 1803.1 | +0.000 |
| H2/O2 | 2836.4 | 2836.4 | +0.000 |
| H2/air | 1969.0 | 1969.0 | +0.000 |

C12H26/O2 differs by +0.19% because the new run uses the reduced 20-species equilibrium-thermo mechanism (full 100-species Reitz kinetics are irrelevant for CJ equilibrium; reduction validated by this very check). C2H2/air, C3H8/air, C12H26/air are new combos with no prior in-project reference: anchored by the same validated pipeline + physical ordering U_CJ(C2H2)>U_CJ(C2H4)>U_CJ(CH4)~U_CJ(C3H8)~U_CJ(C12H26) for air, satisfied.

## Check 3 detail - SK Table-1 replica (1.5 atm / 255 K, u_c = 300 m/s, Pa = 1 atm)

| Case | rho_c me/SK | Y_f me/SK | U_CJ d% | P_CJ d% | Isp_f PH me/SK (d%) | Isp_f AX me/SK (d%) |
|---|---:|---:|---:|---:|---:|---:|
| H2-air | 1.50 / 1.48 | 0.0285 / 0.0285 | +0.04 | +1.2 | 4702 / 4706 (-0.1%) | 5395 / 5383 (+0.2%) |
| C2H4-air | 2.06 / 2.04 | 0.0638 / 0.0638 | +0.02 | +1.2 | 1957 / 1975 (-0.9%) | 2285 / 2280 (+0.2%) |
| C2H4-O2 | 2.22 / 2.19 | 0.2262 / 0.2260 | +0.04 | +1.4 | 937 / 704 (+33.1%) | 912 / 911 (+0.1%) |
| C3H8-O2 | 2.44 / 2.41 | 0.2161 / 0.2160 | +0.04 | +1.4 | 974 / 1016 (-4.1%) | 953 / 952 (+0.1%) |

## Anomalies and limitations

**A1 - SK Table 1, C2H4-O2 pressure-history value (704 s) is not reproducible.** Our faithful implementation gives 937 s. Proof of anomaly: C2H4-O2 and C3H8-O2 have near-identical model inputs (U_CJ 2402/2383 m/s, gamma_e 1.142/1.137, Y_f 0.226/0.216, P_CJ 5.97/6.46 MPa), so the PH model cannot produce Isp_f differing by 44% (704 vs 1016 s); our pair (937/974 s) has the physically required ratio. The same-row axial value (911 s) IS reproduced at +0.1%, so the implementation is not at fault. The published 704 coincides with the CFD value (700): plausible transcription/erratum in the report table, or an undocumented case-specific alpha (~0.93 instead of 0.65). Also internally inconsistent in the report: Mdot = 1.91 kg/s with H = 15.1 mm and rho_c = 2.19 implies channel width W = 24 mm, vs W = 10 mm for the other three cases (Eq. 15).

**A2 - kerosene surrogate.** Kerosene = n-C12H26 (as in the existing deck). The Reitz mechanism contains no NOx species at all, so kerosene/AIR equilibrium would miss NO: we grafted NO/N/N2O/NO2 NASA thermo from GRI-3.0 into the reduced equilibrium set (Tad check: 2279 K, X_NO = 0.0025 - textbook values). Kerosene/air IS feasible: U_CJ = 1795.9 m/s, T_CJ = 2836 K. Thermo polynomials valid to 5000 K (no extrapolation).

**A3 - K calibration domain.** K = 1.02 (air) / 1.54 (O2) were fitted by SK on C2H4-air / C2H4-O2 injector-face pressure traces of S&K (2013); following SK Table 1 practice we extend them to all same-oxidizer mixtures. K for other fuels is an assumption of the method, not a measured value.

**A4 - Stechmann at 1-atm fill.** With Pinit = Pa = 1 atm the choked-at-all-times assumption fails in the last ~15-19% of the cycle (Pc/Pa < critical); values there follow the ideal choked formulas (Stechmann himself runs 20-200 atm chambers, where the assumption holds). His published Table-1 Isp (200 K, optimized phi, 20/200 atm) is therefore NOT directly comparable; V&V for this model is the CP-collapse test, the mass-vs-time weighting inequality, and cross-model coherence (checks 5-6).

**A5 - correction to the existing deck numbers.** results_main.json FovM/Ispf used the FROZEN gamma at CJ (~1.22-1.25) in place of the equilibrium gamma_e (~1.13-1.17) required by SK Eq. 19-20, and omitted term II: e.g. H2/air Isp_f 3203 s (deck) -> 4268 s (faithful PH I+II at the same conditions). Slide tables built from results_main.json should be updated with data/thrust_models_all.json.

Ambient/units: Pa = 101325 Pa, g0 = 9.80665; all Isp fuel-based unless noted. Generated by src/thrust/tables.py.
