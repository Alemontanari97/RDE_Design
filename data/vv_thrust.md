# V&V - analytical thrust models (PH / axial / Stechmann)

Pipeline: scripts/thrust_models.py -> data/thrust_models_all.json (16 cases: 12 std @ 1 atm/300 K + 4 SKREP @ 0.15 MPa/255 K, A6).
No number is reported without a cross-check; verdicts below.

## Checks

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | U_CJ vs results_main.json (9 validated combos, <0.5%) | **PASS** | max +0.19% (n=9 combos, threshold 0.5%) |
| 2 | CJ state vs SK Table 2 literature (5 mixtures) | **PASS** | live max errU 0.1% (<0.5), errP 1.7% (<2.0), 5 mixtures (sk_tables.json comp) |
| 3a | SK Table-1 replica: model INPUTS (U_CJ, P_CJ, gamma_e, rho_c, Y_f) | **PASS** | live max on 4 cases: |dU| 0.023% (<0.2), |d g_e| 0.0004 (<0.005), |dP| 0.12% (<2.0), |d rho_c| 0.18% (<0.5, direct at the 0.15 MPa SK fill, A6), |d Y_f| 0.0002 (<0.002) |
| 3b | Axial-flow Isp_f vs SK Table 1 (4 cases) | **PASS** | all 4 within 0.1% (<1.0) |
| 3c | Pressure-history Isp_f vs SK Table 1 (4 cases) | **PASS*** | 3/4 within 4.2%; the one failure IS the documented C2H4-O2 anomaly (published 704 s vs our 936 s, +33%) - see A1 |
| 4 | Axial internal: Pm/P2 range, CJ sonicity (sonic-vs-matched span reported) | **PASS** | Pm/P2 in [0.218,0.234] vs SK ~0.22-0.25 (+-0.005 reading margin => [0.215,0.255]); CJ sonic residual <= 0.0016 (<0.005); sonic-vs-matched span +2.1..+17.1% (reported) |
| 5 | Stechmann internal: CP-collapse, mass- vs time-weighting, choking | **PASS** | CP-collapse rel.err 2.1e-11; mass-weighted > time-averaged for 6/6; choked fraction 81-85% of cycle |
| 6 | Cross-model coherence PH / axial / Stechmann (fuel-O2) | **PASS** | PH vs axial-sonic vs Stechmann(eps=1,SL) total-mass Isp spread 4.4-9.0% (6 fuel-O2 combos; 12% budget = the three closures differ by design: K-fit tail vs sonic-exit vs blowdown average, each ~5% class, see A3/A4) |

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

## Check 3 detail - SK Table-1 replica (0.15 MPa / 255 K, u_c = 300 m/s, Pa = 1 atm)

| Case | rho_c me/SK | Y_f me/SK | U_CJ d% | P_CJ d% | Isp_f PH me/SK (d%) | Isp_f AX me/SK (d%) |
|---|---:|---:|---:|---:|---:|---:|
| H2-air | 1.48 / 1.48 | 0.0285 / 0.0285 | +0.02 | -0.1 | 4694 / 4706 (-0.3%) | 5384 / 5383 (+0.0%) |
| C2H4-air | 2.04 / 2.04 | 0.0638 / 0.0638 | +0.00 | -0.1 | 1953 / 1975 (-1.1%) | 2281 / 2280 (+0.1%) |
| C2H4-O2 | 2.19 / 2.19 | 0.2262 / 0.2260 | +0.01 | +0.1 | 936 / 704 (+32.9%) | 911 / 911 (-0.0%) |
| C3H8-O2 | 2.41 / 2.41 | 0.2161 / 0.2160 | +0.02 | -0.0 | 973 / 1016 (-4.2%) | 952 / 952 (+0.0%) |

## Anomalies and limitations

**A1 - SK Table 1, C2H4-O2 pressure-history value (704 s) is not reproducible.** Our faithful implementation gives 936 s. Proof of anomaly: C2H4-O2 and C3H8-O2 have near-identical model inputs (U_CJ 2402/2383 m/s, gamma_e 1.142/1.137, Y_f 0.226/0.216, P_CJ 5.97/6.46 MPa), so the PH model cannot produce Isp_f differing by 44% (704 vs 1016 s); our pair (936/973 s) has the physically required ratio. The same-row axial value (911 s) IS reproduced at -0.0%, so the implementation is not at fault. The published 704 coincides with the CFD value (700): plausible transcription/erratum in the report table, or an undocumented case-specific alpha (~0.93 instead of 0.65). Also internally inconsistent in the report: Mdot = 1.91 kg/s with H = 15.1 mm and rho_c = 2.19 implies channel width W = 24 mm, vs W = 10 mm for the other three cases (Eq. 15).

**A2 - kerosene surrogate.** Kerosene = n-C12H26 (as in the existing deck). The Reitz mechanism contains no NOx species at all, so kerosene/AIR equilibrium would miss NO: we grafted NO/N/N2O/NO2 NASA thermo from GRI-3.0 into the reduced equilibrium set (Tad check: 2279 K, X_NO = 0.0025 - textbook values). Kerosene/air IS feasible: U_CJ = 1795.9 m/s, T_CJ = 2836 K. Thermo polynomials valid to 5000 K (no extrapolation).

**A3 - K calibration domain.** K = 1.02 (air) / 1.54 (O2) were fitted by SK on C2H4-air / C2H4-O2 injector-face pressure traces of S&K (2013); following SK Table 1 practice we extend them to all same-oxidizer mixtures. K for other fuels is an assumption of the method, not a measured value.

**A4 - Stechmann at 1-atm fill.** With Pinit = Pa = 1 atm the choked-at-all-times assumption fails in the last ~15-19% of the cycle (Pc/Pa < critical); values there follow the ideal choked formulas (Stechmann himself runs 20-200 atm chambers, where the assumption holds). His published Table-1 Isp (200 K, optimized phi, 20/200 atm) is therefore NOT directly comparable; V&V for this model is the CP-collapse test, the mass-vs-time weighting inequality, and cross-model coherence (checks 5-6).

**A6 - SK Table-1 fill convention (discovered 2026-07-15, RESOLVED by re-bless 2026-07-16).** SK Table 1 quotes rho_c consistent with a 0.15 MPa (1.5 bar) fill, not the 1.5 atm the replica historically ran: densities rescaled by 150000/151987.5 reproduced all four quoted rho_c to 3 s.f. The SKREP cases are NOW computed directly at 0.15 MPa / 255 K (sk_models.py); check 3a compares rho_c directly (live max 0.18%). The former +1.32% offset on P-linked quantities is gone; U_CJ, gamma_e and the Isp_f ratios were never affected (<0.2%).

**A5 - correction to the existing deck numbers.** results_main.json FovM/Ispf used the FROZEN gamma at CJ (~1.22-1.25) in place of the equilibrium gamma_e (~1.13-1.17) required by SK Eq. 19-20, and omitted term II: e.g. H2/air Isp_f 3203 s (deck) -> 4268 s (faithful PH I+II at the same conditions). Slide tables built from results_main.json should be updated with data/thrust_models_all.json.

Ambient/units: Pa = 101325 Pa, g0 = 9.80665; all Isp fuel-based unless noted. Generated by src/thrust/tables.py.
