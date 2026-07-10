# sdtoolbox/ — provenance

Vendored subset of the **Shock & Detonation Toolbox** by the Explosion Dynamics
Laboratory, California Institute of Technology (J. E. Shepherd and coworkers):
GALCIT Report **FM2018.001**. Verified line-by-line against the official release 'Updated April 2026' (SDToolbox.zip, audit 2026-07-09: validation/sdt_official_audit.md - functional identity confirmed; single documented patch below).
https://shepherd.caltech.edu/EDL/PublicResources/sdt/

Modules vendored (only what the lecture code calls):

- `postshock.py` — `CJspeed` (equilibrium-Hugoniot minimum wave speed via
  density-ratio sweep + least-squares parabola), `PostShock_fr` /
  `PostShock_eq` (frozen / equilibrium post-shock states, Reynolds' iterative
  method), `FHFP`, `LSQ_CJspeed`.
- `znd.py` — `zndsolve` (ZND detonation-structure ODEs, thermicity-driven),
  `getThermicity`, `getTempDeriv`.
- `thermo.py` — `soundspeed_eq`, `soundspeed_fr`, `eq_state`, `state`.
- `config.py` — convergence tolerances (`ERRFT = ERRFV = 1e-4`,
  `volumeBoundRatio = 5`), unchanged.

## Documented patch (performance only, no physics change)

`thermo.soundspeed_fr` returns Cantera's built-in `gas.sound_speed` (the exact
frozen sound speed `sqrt(gamma*R*T/W)` for an ideal-gas mixture) instead of the
reference finite-difference SVX evaluation, which is kept verbatim as
`_soundspeed_fr_fd` for comparison. Rationale: identical result for ideal-gas
phases, ~100× faster inside the ZND integration loop. This is the only
functional deviation from the official modules (verified against the April 2026 release: equivalence 6-10e-5 on a_fr, <=0.02% end-to-end on ZND induction length); docstrings were
added. The patched toolbox passed the full validation stack (33-check
literature suite + 22-check internal-consistency suite, see
`validation/VALIDATION.md`; ZND energy invariant conserved to 6e-6 %).

## Citation

Cite the SD Toolbox as: S. Browne, J. Ziegler, N. Bitter, B. Schmidt,
J. Lawson, J. E. Shepherd, "SDToolbox: Numerical Tools for Shock and Detonation
Wave Modeling", GALCIT Report FM2018.001, California Institute of Technology
(2023 report; modules verified against the official release 'Updated April 2026'). See `../CITATION.md`.
