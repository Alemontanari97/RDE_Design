# How to cite

This package implements, verbatim at equation level, models from the following
sources. If you use the code or the shipped data, cite the papers whose
equations you rely on (module → paper map in `README.md`).

## Source papers (models implemented here)

**Wintenberger & Shepherd — cycle analysis** (`src/cycles/`)
- E. Wintenberger, J. E. Shepherd, "Thermodynamic Analysis of Combustion
  Processes for Propulsion Systems", AIAA paper 2004-1033, 42nd AIAA Aerospace
  Sciences Meeting, Reno, 2004. (Paper **A**: Eqs. A19–A60 as cited in code.)
- E. Wintenberger, J. E. Shepherd, "Thermodynamic Cycle Analysis for
  Propagating Detonations", *Journal of Propulsion and Power* 22(3):694–698,
  2006. doi:10.2514/1.12775 (Paper **B**: Eqs. B1–B3.)

**Shepherd & Kasahara — analytical thrust models** (`src/thrust/sk_models.py`)
- J. E. Shepherd, J. Kasahara, "Analytical Models for the Thrust of a Rotating
  Detonation Engine", GALCIT Report FM2017.001, California Institute of
  Technology, 2017.

**Stechmann, Heister & Harroun — RDE rocket performance** (`src/thrust/st_core.py`,
`stechmann_nozzle.py`)
- D. P. Stechmann, S. D. Heister, A. J. Harroun, "Rotating Detonation Engine
  Performance Model for Rocket Applications", *Journal of Spacecraft and
  Rockets* 56(3):887–898, 2019. doi:10.2514/1.A34313

**CFD anchors used in the V&V** (`validation/vv_thrust.md`)
- D. A. Schwer, K. Kailasanath, "Fluid dynamics of rotating detonation
  engines with hydrogen and hydrocarbon fuels", *Proceedings of the Combustion
  Institute* 34(2):1991–1998, 2013. doi:10.1016/j.proci.2012.05.046

## Shock & Detonation Toolbox (vendored in `sdtoolbox/`)

- S. Browne, J. Ziegler, N. Bitter, B. Schmidt, J. Lawson, J. E. Shepherd,
  "Numerical Solution Methods for Shock and Detonation Jump Conditions",
  GALCIT Report FM2006.006 — R3 (2018 revision), and
  "SDToolbox: Numerical Tools for Shock and Detonation Wave Modeling",
  GALCIT Report FM2018.001, California Institute of Technology, Explosion
  Dynamics Laboratory (2023 report; vendored modules verified line-by-line against the official release 'Updated April 2026', audit 2026-07-09).
  https://shepherd.caltech.edu/EDL/PublicResources/sdt/
  (Vendored subset and one documented performance patch: see
  `sdtoolbox/PROVENANCE.md`.)

## Software and thermochemistry

- Cantera (validated with 3.2.0): D. G. Goodwin, H. K. Moffat, I. Schoegl,
  R. L. Speth, B. W. Weber, *Cantera: An object-oriented software toolkit for
  chemical kinetics, thermodynamics, and transport processes*.
  doi:10.5281/zenodo.14455267
- GRI-Mech 3.0: G. P. Smith et al., http://www.me.berkeley.edu/gri_mech/
- n-dodecane (kerosene/RP-1 surrogate): thermo subset of the Reitz n-dodecane
  mechanism with GRI-3.0 NOx species grafted for air equilibria
  (`data/dodecane_eq_thermo.yaml`, see `data/README.md`).

## Reference values

- CJ reference states: Caltech Detonation Database / CEA values as tabulated
  in Shepherd & Kasahara FM2017.001 Table 2 (`data/sk_tables.json`).
