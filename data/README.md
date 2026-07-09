# data/ — validated results and inputs (provenance)

Every JSON here is a **build artifact of this repo's own code**, produced and
validated during the lecture build (project_build, 2026-07), then shipped
frozen. Ownership: the module listed regenerates the file bit-compatibly
(up to run dates in `meta.updated`).

| file | owner module | contents / provenance |
|---|---|---|
| `cycles_ws.json` | `src/cycles/cycles.py` | one-γ analytic anchors, 12-mixture Fickett–Jacobs states (Cantera 3.2 + SD Toolbox, shifting equilibrium), 3-cycle π_c sweeps (C3H8-air paper anchor + CH4-air display), p–v loop paths, vN state. Validated by the 99-check suite (`validation/cycles_validation.md`). |
| `q_mapping.json` | `src/cycles/q_mapping.py` | formal q/q̃ definitions, per-mixture q_c, q_thermo, q_eff, Fig. A22 family traceability. Derives from `cycles_ws.json`. Running the module also writes the slide-ready `q_mapping.md` here. |
| `thrust_models_all.json` | `src/thrust/sk_models.py` (+ meta by `tables.py`) | CJ states and Shepherd–Kasahara PH/axial + Stechmann results for 12 combos at 1 atm/300 K + 4 SKREP replicas at 1.5 atm/255 K. Validated by the 8-check suite (`validation/vv_thrust.md`). |
| `st_nozzle_opt.json` | `src/thrust/stechmann_nozzle.py` | matched detonation/CP chamber states and converged bell/aerospike area-ratio optima for all 18 Stechmann Table-1 rows (+CH4 φ=1 anchors, quadrature checks). Validated 18/18 (`validation/st_opt_validation.md`). |
| `znd_sdt.json` | `src/detonation/znd_profiles.py` | ZND reaction-zone profiles (T, p, thermicity, M vs x) for H2/air, H2/O2, CH4/O2, C2H4/O2; induction/exothermic lengths; vN state. Official SD Toolbox `zndsolve`. |
| `results_main.json` | *(input, frozen)* | legacy validated CJ/thrust summary of the first build (33-check suite of `validation/VALIDATION.md`); kept as the cross-check reference for V&V check 1 in `src/thrust/tables.py`. |
| `sk_tables.json` | *(input, frozen)* | Shepherd & Kasahara FM2017.001 Tables 1–2 literature values (digitized), used as anchors by `src/thrust/tables.py`. |
| `dodecane_eq_thermo.yaml` | *(input, frozen)* | kerosene surrogate mechanism: 16-species Reitz n-dodecane thermo + NO/N/N2O/NO2 NASA7 thermo grafted from GRI-3.0; equilibrium-only reduced set, validated to +0.19 % on U_CJ vs the full mechanism (`validation/vv_thrust.md`, A2). |
| `gri30_CHO_eq.yaml` | *(input, frozen)* | GRI-3.0 C/H/O subset (no N chemistry) used by the Stechmann model for fuel/O2 equilibria — identical equilibria, ~3× faster. |
| `q_formal.json` | `src/cycles/q_formal.py` | standard-state heat-release verification (q°, sensible-shift identity, CJ-plane release fraction) for H2/air and CH4/air; quoted by `validation/q_formal.md`. |

Generated on demand by the modules (not shipped): `sweep_sdt.json`
(`cj_sweeps.py`), `q_mapping.md`,
`thrust_tables.md`, `vv_thrust.md`, `cycles_validation.md`,
`st_opt_validation.md` (regenerated reports carry their run date; the frozen
reviewed copies live in `validation/`).

Conditions unless stated otherwise: φ = 1, T₁ = 300 K, p₁ = 1 atm (`cycles_*`
use 1 bar where stated), ambient 1 atm, g₀ = 9.80665 m/s².
