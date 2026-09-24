# GENO RaoPlug posed on Humphreys 1971's Rao nozzle (their Table 3)

`input.ini` is the input of the GENO RaoPlug run (nozzle_type 8) whose field is THEIR start for
the plug march in Rao's world. It is used by `rao1961_twin.py`, `rao1961_o33.py` and
`rao1961_sqp_return.py` through `RAO_GENO_RUN` (the run directory), together with
RAO_PA_PC = 14.7/500 and RAO_PB = the Veen base pressure below. It plays the role that
`GENO/CASES/raoplug_run_legacy` plays for Rao 1961.
GENO is an independent repository and is never committed here.

Run: in a directory containing this input.ini, execute `<GENO>/bin/GENO` (the build of
2026-08-09). The thermo paths in the file point to `RDE/codes/GENO/thermo`. The run is
bit-identical on rerun.

How the numbers in input.ini were obtained (2026-09-24; the working record is in
RDE/handoff/throat_2026-09-23/geno_rao_humphreys/):
- **Rao's own method**, not the literal -58.5 deg:
  - lip radius y_E = 8.33 in (0.211582 m);
  - Rao's lip transversality condition set to p_a = 14.7 psia (pa = p0 * 14.7/500);
  - `Me_fixed` found by a secant so that D sits at x_D = 11.51781 in from the lip (their last
    Table 3 row);
  - `theta_i_plug` is GENO's fan parameter: theta_E plus the one-step fan turn at Mi_plug 1.05.
- **Base**: their Eq. (12), Veen, p_b = 0.846 p_D / M_D^1.3 on the state at D, iterated as a
  fixed point outside GENO. The converged value is pb = 96914.7 Pa = 0.0161304 p0 (8.065 psia),
  consistent to 1.1e-4 with the closure on the final corner state.
- **Gas**: the gamma = 1.23 thermo of GENO. Pressures are posed as ratios to p0 (500 psia -> p0);
  the geometry and the thrust coefficient do not depend on R and T0 at fixed gamma. cstar_plug is
  the true c* of that gas.

Reproduction of their Table 3: stage `raogeno` of `a1_humphreys_twin.py` reads the run's wall.
Findings of the posing, as readings:
- their "approximately -58.5 deg" injection angle is not Rao's sonic-line direction of the
  matching design (-55.84 deg). It brackets the mean flow direction along the lip's first
  characteristic (-57.9 deg).
- the printed angle -28.40556 deg at x 3.03421 repeats the digits of its own y (4.40556). It is
  0.145 deg off the run, while every other row is within 0.011 deg: probably a second misprint.
