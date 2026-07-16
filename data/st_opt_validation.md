# Stechmann Table 1 - nozzle optimization validation

Model: `src/thrust/stechmann_nozzle.py` (Eqs. 4-15 of the paper; equilibrium
CJ/HP chemistry, gamma frozen through the nozzle, mass-weighted cycle
Isp, matched mass flow and throat area, Ti = 200 K).
Optimizer: 241-pt geometric sweep + golden-section, tol 1e-3 (5e-3 at
200 atm) on eps; bell optimum cross-checked against the exact model
identity NPR(eps_opt) = mean_t(Pc)/Pa; aerospike optimum = saturation
knee NPR(eps_opt) = Pmax/Pa (closed form, plateau verified on sweep).
Vacuum ("N/A") rows use the paper-fixed eps (15 / 150), no optimization.

PASS: |dIsp| <= 5% (det and CP), eps within 10% (or 0.25 abs),
benefit within 3 points.

| Prop | Pcp | Nozzle | Pa | Isp_det pap/mod (d%) | eps_det pap/mod | Isp_cp pap/mod (d%) | eps_cp pap/mod | benefit pap/mod (d pt) | status |
|---|---|---|---|---|---|---|---|---|---|
| H2 | 20 | Bell | 1 | 394 / 394.3 (+0.1%) | 3.8 / 3.80 | 362 / 361.9 (-0.0%) | 3.6 / 3.60 | 9.0 / 8.94 (-0.06) | PASS |
| H2 | 20 | Aerospike | 1 | 406 / 406.0 (-0.0%) | 9.2 / 9.19 | 362 / 361.9 (-0.0%) | 3.6 / 3.60 | 12.2 / 12.17 (-0.03) | PASS |
| H2 | 20 | N/A | 0 | 497 / 496.5 (-0.1%) | 15.0 / 15.00 | 460 / 460.5 (+0.1%) | 15.0 / 15.00 | 7.9 / 7.82 (-0.08) | PASS |
| H2 | 200 | Bell | 1 | 475 / 475.2 (+0.0%) | 21.2 / 21.16 | 440 / 440.2 (+0.0%) | 20.6 / 20.60 | 8.0 / 7.95 (-0.05) | PASS |
| H2 | 200 | Aerospike | 1 | 483 / 482.8 (-0.0%) | 55.6 / 55.64 | 440 / 440.2 (+0.0%) | 20.6 / 20.60 | 9.7 / 9.67 (-0.03) | PASS |
| H2 | 200 | N/A | 0 | 545 / 544.7 (-0.1%) | 150.0 / 150.00 | 508 / 508.1 (+0.0%) | 150.0 / 150.00 | 7.2 / 7.20 (+0.00) | PASS |
| CH4 | 20 | Bell | 1 | 286 / 285.9 (-0.0%) | 4.0 / 3.98 | 274 / 274.0 (-0.0%) | 3.9 / 3.92 | 4.4 / 4.36 (-0.04) | PASS |
| CH4 | 20 | Aerospike | 1 | 299 / 298.9 (-0.0%) | 11.4 / 11.39 | 274 / 274.0 (-0.0%) | 3.9 / 3.92 | 9.2 / 9.11 (-0.09) | PASS |
| CH4 | 20 | N/A | 0 | 365 / 365.4 (+0.1%) | 15.0 / 15.00 | 353 / 353.2 (+0.1%) | 15.0 / 15.00 | 3.5 / 3.46 (-0.04) | PASS |
| CH4 | 200 | Bell | 1 | 358 / 358.1 (+0.0%) | 23.2 / 23.30 | 345 / 345.1 (+0.0%) | 23.4 / 23.46 | 3.7 / 3.78 (+0.08) | PASS |
| CH4 | 200 | Aerospike | 1 | 366 / 366.8 (+0.2%) | 71.6 / 72.07 | 345 / 345.1 (+0.0%) | 23.4 / 23.46 | 6.2 / 6.29 (+0.09) | PASS |
| CH4 | 200 | N/A | 0 | 415 / 415.3 (+0.1%) | 150.0 / 150.00 | 402 / 402.7 (+0.2%) | 150.0 / 150.00 | 3.0 / 3.12 (+0.12) | PASS |
| RP-1 | 20 | Bell | 1 | 273 / 275.7 (+1.0%) | 3.9 / 3.94 | 262 / 265.1 (+1.2%) | 3.9 / 3.91 | 4.0 / 4.01 (+0.01) | PASS |
| RP-1 | 20 | Aerospike | 1 | 287 / 290.5 (+1.2%) | 12.2 / 12.27 | 262 / 265.1 (+1.2%) | 3.9 / 3.91 | 9.6 / 9.58 (-0.02) | PASS |
| RP-1 | 20 | N/A | 0 | 348 / 352.0 (+1.2%) | 15.0 / 15.00 | 338 / 341.6 (+1.1%) | 15.0 / 15.00 | 3.0 / 3.06 (+0.06) | PASS |
| RP-1 | 200 | Bell | 1 | 342 / 345.4 (+1.0%) | 22.8 / 22.69 | 331 / 334.6 (+1.1%) | 23.2 / 23.17 | 3.3 / 3.23 (-0.07) | PASS |
| RP-1 | 200 | Aerospike | 1 | 351 / 355.0 (+1.1%) | 75.7 / 75.81 | 331 / 334.6 (+1.1%) | 23.2 / 23.17 | 6.2 / 6.09 (-0.11) | PASS |
| RP-1 | 200 | N/A | 0 | 396 / 399.6 (+0.9%) | 150.0 / 150.00 | 386 / 390.0 (+1.0%) | 150.0 / 150.00 | 2.5 / 2.45 (-0.05) | PASS |

18/18 rows PASS.

## Qualitative anchors (CH4/O2, phi = 1, Pcp = 20 atm, Ti = 200 K)

- Bell detonation gain at fixed phi: **+2.6%** (paper: +2-3%, Fig. 9).
- Aerospike detonation gain at fixed phi: **+7.3%** (paper: "upward of 7%", Fig. 10).
- Optimum aerospike/CP area-ratio growth: **2.86x** (paper: ~3x; largest tabulated benefit 12.2%).

## Honest-model statement

- No flow-separation model (paper choice, replicated): the fixed-eps
  bell is allowed to run deeply overexpanded late in the cycle
  (Fig. 8); real bells would separate and lose less, so the tabulated
  bell penalty is a worst case within the ideal framework.
- Channel choking (assumption 3): min(Pc)/Pa relative to the sonic
  threshold ((g+1)/2)^(g/(g-1)) is reported per case. Minimum margin
  over the sea-level rows: H2 1.69, CH4 0.97, RP-1 0.65;
  the low-mass-flux tail of the 20-atm hydrocarbon cycles therefore
  dips marginally below choking. The paper retains assumption 3
  there, and this model replicates that choice.
- RP-1 is modeled as gaseous n-dodecane (H/C 2.17 vs ~1.95; NASA7
  thermo extrapolated 300 K -> 200 K): the coarsest surrogate here.
- Quadrature: |Isp(n=4001) - Isp(n=16001)| = 5.5e-06 / 7.0e-06 s
  (bell / aerospike, H2 20 atm case).

## Full-DOF optimization (Step 7): joint (phi, eps), nothing inherited from Table 1

Outer phi on the 0.01 lattice (auto-extending bracket -> seed-
independent; parabolic seed; hill-climb; certificate: both 0.01-
neighbours lower). Inner eps closed form (Step-5 identities).
Paper (phi, eps, Isp) enter ONLY as targets; superiority
Isp(phi*_model) >= Isp(phi_paper) checked per row.
PASS adds |dphi| <= 0.10 to the Step-6 criteria.

| Prop | Pcp | Nozzle | phi_det pap/mod | Isp_det pap/mod (d%) | eps_det pap/mod | phi_cp pap/mod | Isp_cp pap/mod (d%) | eps_cp pap/mod | ben pap/mod | cert | status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H2 | 20 | Bell | 3.28 / 3.28 | 394 / 394.3 (+0.1%) | 3.8 / 3.80 | 2.54 / 2.54 | 362 / 361.9 (-0.0%) | 3.6 / 3.60 | 9.0 / 8.94 | Y | PASS |
| H2 | 20 | Aerospike | 3.15 / 3.14 | 406 / 406.0 (-0.0%) | 9.2 / 9.20 | 2.54 / 2.54 | 362 / 361.9 (-0.0%) | 3.6 / 3.60 | 12.2 / 12.17 | Y | PASS |
| H2 | 20 | N/A | 2.98 / 2.97 | 497 / 496.5 (-0.1%) | 15.0 / 15.00 | 2.25 / 2.25 | 460 / 460.5 (+0.1%) | 15.0 / 15.00 | 7.9 / 7.82 | Y | PASS |
| H2 | 200 | Bell | 2.70 / 2.67 | 475 / 475.2 (+0.0%) | 21.2 / 21.22 | 2.04 / 2.04 | 440 / 440.2 (+0.0%) | 20.6 / 20.60 | 8.0 / 7.95 | Y | PASS |
| H2 | 200 | Aerospike | 2.62 / 2.59 | 483 / 482.8 (-0.0%) | 55.6 / 55.90 | 2.04 / 2.04 | 440 / 440.2 (+0.0%) | 20.6 / 20.60 | 9.7 / 9.67 | Y | PASS |
| H2 | 200 | N/A | 2.44 / 2.41 | 545 / 544.7 (-0.1%) | 150.0 / 150.00 | 1.81 / 1.80 | 508 / 508.1 (+0.0%) | 150.0 / 150.00 | 7.2 / 7.20 | Y | PASS |
| CH4 | 20 | Bell | 1.66 / 1.66 | 286 / 285.9 (-0.0%) | 4.0 / 3.98 | 1.48 / 1.48 | 274 / 274.0 (-0.0%) | 3.9 / 3.92 | 4.4 / 4.36 | Y | PASS |
| CH4 | 20 | Aerospike | 1.64 / 1.64 | 299 / 298.9 (-0.0%) | 11.4 / 11.39 | 1.48 / 1.48 | 274 / 274.0 (-0.0%) | 3.9 / 3.92 | 9.2 / 9.11 | Y | PASS |
| CH4 | 20 | N/A | 1.60 / 1.60 | 365 / 365.4 (+0.1%) | 15.0 / 15.00 | 1.44 / 1.44 | 353 / 353.2 (+0.1%) | 15.0 / 15.00 | 3.5 / 3.46 | Y | PASS |
| CH4 | 200 | Bell | 1.47 / 1.47 | 358 / 358.1 (+0.0%) | 23.2 / 23.30 | 1.32 / 1.32 | 345 / 345.1 (+0.0%) | 23.4 / 23.46 | 3.7 / 3.78 | Y | PASS |
| CH4 | 200 | Aerospike | 1.46 / 1.46 | 366 / 366.8 (+0.2%) | 71.6 / 72.07 | 1.32 / 1.32 | 345 / 345.1 (+0.0%) | 23.4 / 23.46 | 6.2 / 6.29 | Y | PASS |
| CH4 | 200 | N/A | 1.43 / 1.43 | 415 / 415.3 (+0.1%) | 150.0 / 150.00 | 1.29 / 1.29 | 402 / 402.7 (+0.2%) | 150.0 / 150.00 | 3.0 / 3.12 | Y | PASS |
| RP-1 | 20 | Bell | 1.71 / 1.72 | 273 / 275.7 (+1.0%) | 3.9 / 3.94 | 1.55 / 1.54 | 262 / 265.1 (+1.2%) | 3.9 / 3.92 | 4.0 / 4.01 | Y | PASS |
| RP-1 | 20 | Aerospike | 1.70 / 1.71 | 287 / 290.5 (+1.2%) | 12.2 / 12.26 | 1.55 / 1.54 | 262 / 265.1 (+1.2%) | 3.9 / 3.92 | 9.6 / 9.58 | Y | PASS |
| RP-1 | 20 | N/A | 1.65 / 1.66 | 348 / 352.0 (+1.2%) | 15.0 / 15.00 | 1.51 / 1.51 | 338 / 341.6 (+1.1%) | 15.0 / 15.00 | 3.0 / 3.06 | Y | PASS |
| RP-1 | 200 | Bell | 1.53 / 1.53 | 342 / 345.4 (+1.0%) | 22.8 / 22.69 | 1.39 / 1.39 | 331 / 334.6 (+1.1%) | 23.2 / 23.17 | 3.3 / 3.23 | Y | PASS |
| RP-1 | 200 | Aerospike | 1.53 / 1.53 | 351 / 355.0 (+1.1%) | 75.7 / 75.81 | 1.39 / 1.39 | 331 / 334.6 (+1.1%) | 23.2 / 23.17 | 6.2 / 6.09 | Y | PASS |
| RP-1 | 200 | N/A | 1.49 / 1.49 | 396 / 399.6 (+0.9%) | 150.0 / 150.00 | 1.36 / 1.36 | 386 / 390.0 (+1.0%) | 150.0 / 150.00 | 2.5 / 2.45 | Y | PASS |

18/18 rows FULL-OPT PASS.
