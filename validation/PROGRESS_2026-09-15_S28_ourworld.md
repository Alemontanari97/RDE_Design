# PROGRESS — [F3/A1] S28: the line re-verified after the rebuild, the ideal-spike baseline in OUR world (2026-09-15)

**Carriers (new):** `ourworld_geno.py` (world adapter), `ourworld_twin.py`,
`ourworld_o33.py`, `ourworld_sqp_return.py`. **Re-executed:** `rao1961_o33`,
`rao1961_sqp_return`. **GENO:** `CASES/raoplug_ch4o2/` (README there) +
the scratch C- step probe `RDE/handoff/recovery_brick2_2026-09-06/
scratch_s2_2026-09-15/geno_dxtest/` (never to be committed).
**Opening (R2):** memory + S27 reconstruction log + S26 PROGRESS/HANDOFF
read; `origin/rde-nozzle-program` fetched: still 6be51b9 (our base),
`origin/main` still 2d2fdbc (2026-07-16) — no rebase. User order of the
day: (3) regenerate the artifacts the deletion took, then (1) the
axisymmetric ideal-spike baseline -> the full-expansion Rao-vs-spline A/B.

## 1. The rebuilt line holds at the level the SQP consumes (measured)

The S27 reconstruction had re-run the six short rao1961 carriers, not
the two the plug licence rests on. Both re-executed today on s2 from the
rebuilt tree against the S26 records:

| carrier | record 2026-08-27 | re-run 2026-09-15 | log |
|---|---|---|---|
| rao1961_o33 v2 x0=0.30 | 7/7 PASS, 262 s | **7/7 PASS, 228 s — every printed number identical** | `_rao1961_twin/rerun_o33_v2_x030_2026-09-15.log` |
| rao1961_sqp_return v2 + SEG_R1=14 | 6/6 PASS, 2910 s | **6/6 PASS, 2949 s — every printed number identical** (return 1.069e-4 vs band 2.397e-4, \|grad\| 7.8e5 -> 86, J* = J_fit + 0.32 N, rejector 1.088e-2) | `_rao1961_twin/rerun_sqpret_2026-09-15.log` |

## 2. Regeneration of the lost artifacts (item 3) — running, NOT bit-identical by construction

Driver `scratch_s2_2026-09-15/regen_driver.sh` (log `regen_2026-09-15.log`
there): data npz (`data_rao_walls.npz` from the S21 GENO cases
`rao_val`/`rao_run`, which SURVIVE in the s2 scratchpad of session
92be2bd8 and are now copied to NFS; `data_s24_rot.npz` from the
recovered `gen_s24_data.py`) DONE; S22 adaptive production run
(PAKN_M0=10 K=61 N=51, cold start as the record was) -> S23 selftest /
fineopt / rungs 4-6 x 2 / final -> `design_fine.json` -> the five
figures -> `build.sh`, in flight (~7 h). Outputs are named `rerun_*`,
never `run_of_record_*`.

**Declared:** the S22 re-run reproduces the record's J values but NOT
its certificates (0.257 vs 0.111 at seg 0) and diverges in the driver's
decisions from seg 4: the plug march changed after S22 (S24 rotational
port, S25 W-5 transport clamp), so today's code is not the code that
produced the S22 record. Consequence: the S23 selftest R-2b (fresh
rung-1/2 J's vs the committed S22 log at 5e-8) will fail on the "opt"
half. The chain runs through regardless; the S22 log stays as the
historical record with this note.

## 3. The ideal-spike baseline in OUR world (item 1): what GENO gives, measured

`CASES/raoplug_ch4o2/` — our world (CH4/O2 frozen gas, p_c 2.53e7,
T_c 3739.9, p_a 7.614420e5, y_t 1, lip 2.2695010468, theta_i 26.659177,
M_i 2.0), three posings on the committed 2026-08-09 binary:

| posing | result |
|---|---|
| mass + ambient (`constraint2 = pa`, the S21 `rao_pa` posing behind the documented L 5.825 / eps 5.148 / theta_E 0.025 deg) | **does not close**: "no sign change among FEASIBLE theta_E samples", window [0.16, 25.7] deg — the root at ~0.02 deg falls in the hole of the 21-point scan. The S21 number came from the 19:42 build, before the 21:42 rebuild with the valid-window filter; **NOT reproducible today** |
| validation mode `Me_fixed = 2.8020` (= S21 `rao_val`) | **reproduced bit-identically** (run_val_repro): theta_E −0.01991 deg, L 5.92567, eps 5.15063 = y_E^2, curve reaches the axis (exit_reason 4 at y 3.8e-4), mdot 4.23202e4 (−0.37 % vs p_c A_t/c*), lip ambient 7.575953e5 (−0.5 % vs nominal) |
| `Me_fixed` 2.8013 / 2.80134 (theta_E = 0.000), and the true-ideal `mass_match=.false.` | **NaN in the phase-1 fan** (solve_T_from_entropy): GENO's fan holds only for theta_E slightly negative |

**The −0.37 % is posing, not numerics (measured two ways).** (a) NI
101/201/401: every number identical. (b) C- step probe: a scratch copy of
GENO with the hard-coded step `dx = y_E/200` exposed as env
`GENO_CMINUS_DIV` (and the 5000-step cap raised), built with the record
flags (-O0), **gate: the gamma123 oracle case reproduces the committed
binary's log line for line at divisor 200**; then the rao_val posing at
200/400/800:

| divisor | n_pts | mdot on C- | deficit | L | exit |
|---|---|---|---|---|---|
| 200 | 525 | 4.232020e4 | −155.3257 | 5.92567 | 4 (non-finite at y 3.8e-4) |
| 400 | 1058 | 4.232020e4 | −155.3244 | 5.92654 | 4 |
| 800 | 2091 | 4.232021e4 | −155.3161 | 5.92907 | **2 (reached the axis)** |

The mass on the C- curve equals the IVL mass (4.23202e4, printed by
GENO before any curve) to 1e-6 at every step; L moves by 1.5e-4 then
4e-4 relative (the terminal cell changes as the curve gets closer to the
axis). So the deficit sits between GENO's inlet ray and the target
p_c A_t/c* with OUR c* — the cross-code POSING of the inlet (lip radius,
inlet angle, start Mach, thermo evaluation), the same class of mismatch
the S8/S15 twins quantify. Rungs 1600/3200 stopped by design (hours).

**Decision (user, 2026-09-15): baseline = rao_val (L 5.926), and the A/B
posed in twin mode** — GENO's own start line fed to our march, so mass,
gas and ambient coincide by construction — i.e. the [X-RAOTW]/[X-RAOO3]/
[X-RAOSQ] instruments transported from Rao's world to ours. This IS the
F3-EXIT leg "certified plug optimum + oracle on OUR world".

## 4. The our-world instruments (new carriers)

`ourworld_geno.py`: world = `build_tab_nasa` (GENO's own thermo files,
the a1_config_compare gas) — the gas is **verified against the field**
(Rg 5.1e-7, s0 2.6e-6, h0 1.6e-4 max rel over 20000 nodes), not
identified; ambient = the member's lip ambient from
`raoplug_performance.dat` (7.575953e5 = 0.9949 of the nominal PA; the
analogue of Rao's Eq. (8)); `install()` re-points a rao1961 carrier
module's world names (A1 proxy for the table builder, `gas_from_field`,
`PA_PC`, `load_geno`) so `rao1961_sqp_return`'s driver, spline, bands
and checks run verbatim. Scales: cuts 1.50/1.00/0.50 (the Rao-world
0.30/0.20/0.10 as fractions of x_D), K 161 (twice 81: the spike is 2.2x
longer in lip radii), bump amplitudes x 5.04 (length ratio).

**Twin, first run (no tip cut): 5/6.** Field agreement BETTER than in
Rao's world — wedge gap 1.6e-4 mean (Rao's world 5.0e-4), 99.5 % within
q 1e-3, 97.4 % within theta 1.5e-3 rad, 0 nonfinite, floor 3e-6 (51x
below the gap). The one FAIL: certification 7.8e11 / 4.7e11 at the LAST
wall station in 2 of 6 marches — the member closes on the axis (y_D
3.8e-4 m) and the plug march has no axis cell; its wall-foot solve at
y ~ 1e-3 m (source ~ sin(theta)/y) is at the edge of its validity.
**Re-posing DECLARED before the second run:** `OW_YCUT = 0.01` — the
marched wall ends where GENO's contour drops below 0.01 y_E = 0.0247 m
(x_end 5.6102 of 5.9257); the excluded needle carries (p − p_a) pi y^2
~ 1e2 N of 1.16e8 N (1e-6, below every band used here). Same class as
GENO's own truncation at D; the tip is pinned there in O3.3/SQP-return.
For the axis-closing member the Rao-world N1 (tip gradient NONZERO) and
P4 (Eq. (9) corner relation) are N/A and not posed; the tip direction
is REPORTED against 2 pi y_D p_a.

## 5. Verdicts (filled as the chain completes)

(see the addenda below)

## Deviations DECLARED
- Tip cut 0.01 y_E (above), posed after the first twin run's P1 finding.
- The GENO C- step probe lives in a scratch copy; the committed GENO
  source and binary are untouched (md5 of `bin/GENO` unchanged, gate
  identical).
- `CASES/raoplug_ch4o2/` is a new GENO case folder (untracked, like
  `raoplug_gamma123`): owner blessing pending, as before.
- The S21 documented full-expansion numbers (L 5.825, eps 5.148,
  theta_E 0.025 deg) are NOT reproducible with the binary of record;
  `ch_spline.tex` §vsrao must be amended to the rao_val member (L 5.926,
  theta_E −0.020 deg) when the document is next built.

## BLOCCATO
Push read-only (unchanged). GENO owner protocol for the fan at
theta_E >= 0 (NaN) and the C- step knob (if ever wanted in the committed
code). Document build waits on the regeneration chain.
