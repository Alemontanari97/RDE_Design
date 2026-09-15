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

(Addenda A and B at the end of this log: A = the SQP-return verdict,
B = the regeneration chain's outcome.)

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

## Addenda to Sec. 5 (written after the runs closed, 2026-09-15 evening)

### Addendum A (19:26) — SQP-return in OUR world: 5/6, VERDICT FAIL — the P3 falsifier of [X-RAOSQ] fired (P3 failing with P2 passing)

Run of record `validation/_ourworld/run_sqpret_2026-09-15.log` (10051 s;
x0 1.50, K 161, M 8, PERT 1.5 %, FREEZE 0.35, SEG 12, SEG_R1 14, tip cut
0.01 y_E; the [X-RAOSQ] v2 instrument verbatim on the [X-OWTW] posing).

**Numbers.** S1: e_rep 4.863e-4 (Rao's world 4.8e-5 — TEN times: the
same 8 knots on a spike 2.2x longer in lip radii, and the member curves
harder toward the axis); W_fit cert 0.231; J_fit 6.44496391e7 (K 161)
vs 6.44831602e7 (K 321), |dJ| 3.35e4; gradient floor |g(W_fit)|inf
1.53e4 -> gtol 6.12e4. S2: start 6.099e-3 from GENO = 2.9x band_W
(Rao's world: 20.8x — the band is wider here, the same 1.5 % kick is not),
J_p = J_fit − 5.9e3 N, |grad| 7.68e5; c_hat 3.18e8 -> g/c 4.81e-5;
band_W = K_RICH (e_rep + g/c) = 2.138e-3; band_J 1.34e5. S3: 12 segments
(3 trials rejected as worse, 1 base rejected uncertified 1.5e10 ->
revert, radius 3.75e-2; worst accepted cert 0.364): J* 6.44496571e7 =
J_fit + 18.0 N = J_p + 5.93e3 N; |grad|inf 368 = 0.6 % of gtol and 2.4 %
of the floor itself; dist to GENO 2.494e-3. Checks: P1 PASS, **P2 PASS
(368 <= 6.12e4)**, **P3 FAIL (2.494e-3 > band_W 2.138e-3: 1.17x the
band, from a start at 2.9x)**, P4a PASS (+5.93e3 N), P4b PASS (18 N <=
1.34e5). S4/R1: the sign-flipped driver walks to 5.52e-2 (9x the start),
J_p − J = 5.63e5 N, PASS.

**Attribution, first pass (from the log's own numbers; W* is not saved
by the v2 instrument).** In VALUE the return is complete: J* − J_fit =
+18 N on 6.4e7 (3e-7 relative, 7000x inside band_J) and the gradient
closes to a fortieth of its measured floor. In LOCATION the residual
2.49e-3 costs nothing measurable in J: had it lain along the direction
c_hat measures, W* would sit ½ c_hat d² = 9.9e2 N BELOW the maximum,
and it sits 18 N above J_fit instead (the log bounds the linear term by
|g|_1 · |d|inf = 2.27e4 · 2.49e-3 = 57 N, so ½ dᵀH d <= 39 N along the
residual: at least 25x softer than c_hat). c_hat is by construction the
curvature along the ALTERNATING perturbation — the stiffest direction of
a 7-dof spline — and band_W's location floor g/c_hat = 4.8e-5 is
therefore the floor of the stiff direction only.

**Attribution, MEASURED (20:13-20:20; `recovery_brick2_2026-09-06/
scratch_s2_2026-09-15/hess_wfit_2026-09-15.{py,log,npz}`).** AD Hessian
of the replayed J at W_fit on its frozen record (7 x 7, 118 s;
asymmetry 4.5 % rel — the replay is piecewise smooth):
- KNOWN-ANSWER: the curvature along the alternating perturbation from
  the Hessian is 2.87e8 (wall metric) vs c_hat 3.18e8 measured by the
  run from the finite 1.5 % step: 10 %, and the predicted J_fit − J_p =
  5.33e3 N vs 5.92e3 N run. The Hessian is right where v2 looked.
- SPECTRUM (wall-metric curvature, location floor g/c, band K(e_rep +
  g/c)): 9.87e6 / 1.55e-3 / 8.15e-3; 1.95e7 / 7.9e-4 / 5.09e-3; 4.72e7 /
  3.2e-4 / 3.24e-3; 8.79e7 / 1.7e-4 / 2.64e-3; 1.55e8 / 9.9e-5 /
  2.34e-3; 2.04e8 / 7.5e-5 / 2.25e-3; 2.63e8 / 5.8e-5 / 2.18e-3. The
  softest direction is **32x softer than c_hat** (v = [−0.08 −0.17 −0.29
  −0.40 −0.52 −0.54 −0.40]: a smooth lowering/raising of the whole
  spike, weighted downstream) and its location floor alone, 1.55e-3, is
  32x the 4.8e-5 that v2 declared. The gradient floor itself sits at the
  last free knot (g = −1.53e4 there, the other components 2e2..3e3).
- FD-of-gradient along the softest direction: AD 2.98e6 vs FD 2.44e6 /
  2.41e6 / 2.42e6 (h 1e-3, 1e-4, 1e-5: stable, so not truncation) —
  the AD Hessian overestimates the softest curvature by ~20 % (the
  cells' custom derivative rules are exact to first order, their
  second derivatives are not the exact ones); by the FD value the
  softest direction is 40x softer than c_hat, not 32x. Along the
  perturbation direction AD 8.3e7 vs FD 9.3e7 (−11 %). A K_RICH = 4
  band absorbs both, declared; the saved spectrum allows re-grading
  with FD curvatures.
Reading of record, now measured: NOT a second maximum (the value
coincides with the fit) but a LOCATION FLOOR UNDER-DECLARED — v2 used
one scalar curvature, measured along the stiffest direction of a
7-dimensional design space. In Rao's world the same defect was
invisible (floor terms e_rep 4.8e-5, |g| 6.3e3; return 0.45x band_W).

**Instrument v3 (declared 20:25, code committed with this addendum):**
the return is graded PER EIGEN-DIRECTION — band_k = K_RICH (e_rep +
g_floor / c_k) against the residual's component along v_k in wall
units (the scalar band with c_min would be 8.1e-3 > the start's 6.1e-3:
a sup-norm test cannot discriminate once the soft direction is
admitted, the per-direction one can — the start lies outside its band
in the stiff directions); the sup-norm distance and the v2 band are
printed, not graded; W_fit, W_p, W*, W_r and the spectrum are saved
(`sqpret_v3_designs_<date>.npz`) so the residual can be read by
direction. Rao's world is RE-RUN with v3 and must reproduce every v2
number and pass (its row [X-RAOSQ] is re-stamped by that run; the code
change makes the 08-27 stamp stale by the lint's own rule); our world
is re-run with v3 as the run of record of the motion half. Both
launched 20:23 (`sqp_v3_chain.sh`; logs `_rao1961_twin/
run_sqpret_v3_2026-09-15.log`, `_ourworld/run_sqpret_v3_2026-09-15.log`).
The v2 log stays the record of the fired falsifier ([X-OWSQ]).

**Rao's world, v3 run of record (21:13, 3032 s): 6/6 PASS** — every v2
number reproduced line by line (e_rep 4.782e-5, floor 6.27e3, start
4.975e-3 = 20.8x band_W(v2), 12 records, J* − J_fit +0.317 N, |grad|
86.06, return 1.069e-4 = 0.45x band_W(v2), R1 walks to 1.088e-2 with
the same 14-record trace); v3 spectrum: c along the perturbation from
the Hessian 3.61e8 vs c_hat 5.18e8 (−30 %: the finite 1.5 % step's
nonlinearity plus the AD Hessian's custom-rule second derivatives —
inside K_RICH, declared), softest c 1.44e7 (36x softer; v = a smooth
raising of the whole spike again), bands 1.94e-3 (soft) .. 2.9e-4
(stiff); the start lies outside its band in 4 of 7 directions (worst
18.4x), the return's worst component is 0.07 of its band (direction
6); curvature along the actual residual 3.9e7. [X-RAOSQ] re-stamped
from this run (its proof file changed). Post-run hygiene, declared: the
numeric-lint ratchet refused the three literals v3 had introduced
(probe step 1e-3 x2, a 1e-300 guard); replaced by a UNIT probe step
(stations() is linear in W) and a d_s > 0 branch — the committed code
reproduces the run-of-record spectrum to 1e-13 relative (lambda
identical, dw 9e-14, bands 1.2e-13; `scratch_s2_2026-09-15/
spectrum_recheck_2026-09-15.log`), so the log stands as the run of
record of the committed file.

**Our world, v3 run of record (23:13, 10192 s): 6/6 PASS** — the
driver's walk is the v2 walk to the digit (J* = J_fit + 18.0 N,
|grad| 368, sup-norm distance 2.494e-3 = 1.17x band_W(v2), R1 to
5.52e-2); graded by direction the residual is 0.18 and 0.19 of the
band in the two SOFTEST directions (1.51e-3 and 9.79e-4 in wall units)
and 0.08, 0.03, 0.01, 0.00, 0.00 in the others — the curvature along
the actual residual is 7.3e6 (below the softest eigen-curvature, as a
sup-norm metric allows for a combination). So the v2 P3 failure was
the scalar test reading the soft-direction floor as a miss, exactly as
the Hessian predicted before W* was known. Limit, declared: at the 1.5
percent perturbation the start lies outside its band in ONE direction
(the stiffest, 2.8x), so the motion test discriminates start from
return in that direction only; the return there is 1.1e-5 = 0.00 of
the band. Row [X-OWS3] minted; [X-OWSQ] stays the record of the fired
v2 falsifier. The motion half of the plug-sector O3.3 licence holds on
our world at the v3 posing.

### Addendum B (18:32 chain end; certification measured 20:04) — regeneration chain: S22 re-adjudicates, S23 CANNOT proceed (the regenerated design is uncertified at (121,101)); figures 3/5, no PDF

Master log `RDE/handoff/recovery_brick2_2026-09-06/scratch_s2_2026-09-15/regen_2026-09-15.log`
(`##### ALL DONE 18:32:45`). Stage outcomes: A1/A2 data npz EXIT 0
(committed 1b6f11d); B S22 adaptive EXIT 1 = **12/13, A-8 FAIL as in the
record** (log `validation/_plug_adaptive/rerun_S22_2026-09-15.log`,
12946 s; `design_m10_k61_n51.json` written); C1 S23 default EXIT 0 (5/5,
analysis refuses the paired route on mixed modes); **C2 S23 fineopt EXIT 1
— `RuntimeError: record not certified (worst 3.249e+11)` at the FIRST
record of `run_trsqp`, i.e. the warm start itself**; C3 rungs 4-6 x 2,
C4 final, D design_fine: EXIT 1 by cascade (`fineopt.npz` absent); E
figures EXIT 0 with 3/5 written (`fig_spike_designs`, `fig_s23_driver`,
`fig_s24_rotational`; `fig_s23_ladder` needs `verdict.json`,
`fig_worked_example` needs `design_fine.json`); F build.sh EXIT 1
(`ch_spline:742: Unable to load fig_s23_ladder.pdf`). Nothing of the
chain is committed (the three figures stay untracked: the build did not
pass).

**What differs from the record, and why (measured).**
1. The S22 driver of record STOPPED at cycle 2 ("[seg 0] no motion ->
   stop", one record, dJ/J -1.3e-16; best design = cycle 1, m 11, the
   0.4575 knot only). Today's driver RETRIES at half radius on a
   no-motion segment — logic added by the S23 commit 1374361 (2026-08-11),
   AFTER the S22 record — so the rerun's cycle 2 walks 20 segments / 30
   records (two bases rejected uncertified, 3.8e14 and 2.3e18) and
   accepts m 12 (knots 0.4037 + 0.4575) at J 1.16199981e8, +0.20 % over
   cycle 1 at (61,51), cert 0.258. The march changes after S22 (S24
   rotational port, S25 W-5 clamp) explain the certificate values (0.257
   vs 0.111 at class-0 seg 0), not the design: the design divergence is
   the DRIVER.
2. That design is NOT Newton-certified at (121,101) — and the failure
   is RESOLUTION-SPECIFIC, not monotone: measured this evening
   (`recovery_brick2_2026-09-06/scratch_s2_2026-09-15/cert_rungs_2026-09-15.log`,
   `cert_where_2026-09-15.log`), adaptive design cert_worst 0.258 at
   (61,51), **3.249e11 at (121,101)** (n 13082, worst cell tag
   ('edge', 0) = the free-jet edge cell of the FIRST marched column),
   0.235 at (241,201); the incumbent fan streamline 3.7e-2 / 0.334 /
   0.418. Geometry: the 12th knot sits at x 0.4037, 1.5 station spacings
   (K 61) past x0 0.35, and the wall slope at the first stations is
   -0.20 (K 61) / -0.26, -0.20 (K 121) / -0.36, -0.26, -0.21 (K 241)
   against the streamline's uniform -0.50 — a shoulder at the foot,
   flatter than the incoming flow. SWEEP around (121,101) (20:13-20:25,
   `scratch_s2_2026-09-15/col0_attrib_2026-09-15.{py,log}`): the same
   design certifies at (121,103) 0.34, (119,101) 0.34, (123,101) 0.37,
   (161,101) 0.59, (181,151) 0.38, is marginal at (121,81) 1.39 and
   fails at (121,101) 3.2e11 and (121,99) 1.2e12 — always the edge cell
   of the FIRST marched column. The record's knot set does not escape
   it either: the re-run's cycle-1 design (m 11, knots 0.4575 + 10
   uniform, J 1.15965416e8) certifies at (61,51) 0.119 and fails at
   (121,101) with 4.17 (edge cell 75). Reading of record: a (K,N)
   PAIRING LOTTERY of the plug march's start-up (first column, free-jet
   edge cell, EDGE_FILL wedge) for these walls — design-dependent (the
   incumbent passes everywhere), not the under-resolution of a sharp
   feature (241, 161, 181 certify); the march-contract item is booked,
   the cause inside the edge cell (which root the free-jet Newton takes
   when the first column's top lands near the fictitious cut-top fan) is
   NOT dissected tonight.
3. INSTRUMENT DEFECT, S22 A-8 (`gain_ladder`): the rungs read J from
   `march_record` without gating `cert_worst` (A-4 certifies the design
   at its OWN resolution only). The rerun's rung-2 gain +0.429 % is
   therefore the J of an uncertified march — not evidence — so the
   3-point ladder (+0.521 / +0.429 / +0.261 %) has no valid middle rung
   and its band (1.04 %) and the "gain collapses slower than the record"
   reading (record +0.313 / +0.186 / +0.080 %) are void as a ladder;
   what survives is two certified rungs, +0.521 % at (61,51) and
   +0.261 % at (241,201), which say nothing about the limit on their
   own. The record's rung 2 happened to certify (S23 fineopt seg 0: cert
   0.477); its rung 3 was never checked. [X-PGRS] gates certification at
   rungs 1-3 (R-3) and REPORTS it at rungs >= 4; [X-PAKN]'s A-8 gates
   nothing.

**THE FINDING BEHIND THE LOTTERY (20:30-20:45, fold census;
`scratch_s2_2026-09-15/fold_census_2026-09-15.{py,log}`).** A column of
the plug march is a C+ characteristic from the wall foot to the free
edge; if its points are not strictly increasing in y the characteristics
of the family have CROSSED — a shock the isentropic march cannot
represent, and which its certification (a Newton residual per cell)
cannot see. Census at the working resolution (61,51): the fan
streamline (incumbent) 0 of 62 columns folded; the re-run's adaptive
design (m 12) **59 of 62** (first fold at column 4), the re-run's
cycle-1 design (m 11 = the record's knot set) **60 of 62** (first at
column 3). The lever is the wall angle at the first station: the
streamline turns the flow by 0 there (−26.66 deg = the incoming flow),
the m 12 design imposes −11.36 deg and the m 11 design −18.14 deg — a
COMPRESSION CORNER of 15 and 8.5 deg at the foot, whose waves coalesce
within two or three columns. WHERE THE "ADAPTIVE GAIN" IS BOOKED
(measured 21:31, `lever_check_2026-09-15.log`, (61,51)): NOT at the
corner — the wall pressure doubles at the first station (1.97x the
streamline's, p/PA 8.8 vs 4.5) and then drops BELOW it (0.78-0.98x at
stations 3-6), so the first 0.4 m of wall LOSE thrust (−4.3e4 N for
m 12, −1.1e5 N for m 11 against the streamline) and the whole gain
comes from the wall DOWNSTREAM of x 0.75 m (+6.4e5 N and +4.7e5 N;
totals +6.0e5 / +3.7e5 N = the +0.52 / +0.32 % of the ladders'
first rung), i.e. from wall pressures that the march computes through
the tangled part of its net (the inverted cells sit mid-field at
x 1.7-2.1). The coarse "gain" is therefore a number taken from a
multi-valued solution, not a local compression effect — which is also
why S23 saw it evaporate under refinement. (My first reading, "a
higher wall pressure right after the corner", was wrong and is
retracted here.) At rungs 2-3: the S22 designs cross in 120/122 columns at (121,101) and 240/242 at (241,201), worst crossing depth 0.15-0.32 m at mid-column (refined census `fold_census2_2026-09-15.log`, crossings dy < -1e-9 only, no duplicate-y rows anywhere); the incumbent crosses in 0/62, 11/122, 40/242 columns with worst depth 7e-4 m at row fraction ~0.9 near x 2.9, y 2.36 — the free-edge top, the EDGE_FILL fictitious cut-top fan zone, three orders shallower and a different object. Reading of record: the S22 designs (both the
regenerated m 12 and the record's m 11 knot set) are OUTSIDE the
shock-free class the march is certified for; A-4's admissibility
(descends, clears the axis, Newton-certified) never asked — the
march's `certify` is the Newton step relative to its tolerance, no
geometric check anywhere (`a1_plug_march.py`). An independent
criterion agrees (`fold_area`/`lever_check` logs, 21:30): signed cell
areas of the mesh quadrilaterals — the S22 designs carry 6-11 % of
INVERTED cells (m 12: 208 of 3276 at (61,51), 965 of 12893 at
(121,101); m 11: 332 / 1358), the incumbent 0 and 9 (the free-edge
ripples) — so "folded" means a tangled band across the columns, not
a whole-mesh collapse. NOT the same thing: the (121,101) certification
failure sits in the FIRST column's edge cell, UPSTREAM of the first
crossing (column 3-4): the corner alters the first C+ column's path
to the free edge (adaptive: the column reaches the edge at x 1.89
with theta 22 deg; incumbent x 2.72, 3.6 deg) and which (K,N) trips
the edge cell's Newton there is the lottery — related to the corner,
not the fold itself. The S23 re-adjudication running tonight will be
graded by the same census on its fine optimum before any number of
its verdict is quoted. INFERENCE, not measurement (the record's design
vector is lost): the record's [X-PGRS] "gain zero within band" stood on
a design of this class too — same knot set, same driver, J within
3e-5 of tonight's m 11, whose march folds; its fine optimum was
warm-started from it. What follows for the carriers: a FOLD DETECTOR
belongs in A-4 (S22) and R-3 (S23) — an admissibility condition, i.e.
a change of the design class, hence an owner decision; tonight it is
measured and declared, not enforced.

**Consequence for the regeneration (item 3 of the S27 list):** with
today's code the S22->S23 chain does not reproduce the record and could
not run to a verdict from the regenerated design (S23's working
instrument IS (121,101): `run_trsqp` raises on an uncertified first
record, by design); the lost S23 artifacts of 08-11 are NOT regenerable
as such — the chain is a RE-ADJUDICATION with today's code, which is
what the owner's "incomplete" (20:00) asked to be finished. Two
instrument amendments, both declared in the carriers' docstrings and
committed with this addendum:
- S22 `a1_plug_adaptive.py`: every rung of the A-8/A-9 ladders is
  gated on certification of BOTH marches; an uncertified rung makes the
  ladder VOID and the verdict FAIL by discipline (certs printed per
  rung). Artifact dir configurable (`PAKN_ART`) so a re-run can live
  beside the 18:28 artifacts.
- S23 `a1_plug_gain_resolve.py`: R-2c reports whether the S22 design of
  record certifies at the fine instrument; if not, the warm start FALLS
  BACK to the newest S22 cycle checkpoint that certifies at (121,101)
  and, failing all, to the fan streamline on the S22 knots — the
  verdict is about the FINE optimum's gain, not about where the walk
  began; the knot set travels with the design into `fineopt.npz`
  (`warm_from` recorded). With tonight's certs (cycle 2 3.2e11, cycle 1
  4.17) the fallback will be the streamline on the m 12 knots; the fine
  driver then has to climb the ~+0.2 % itself (PGRS_ITERS 40).
Launched 20:23 (`scratch_s2_2026-09-15/regen2_driver.sh`, master log
`regen2_2026-09-15b.log`): S23 default -> fineopt (R-2c fallback) ->
rungs 4-6 x inc/fine as SIX PARALLEL processes -> final -> design_fine
-> figures -> build, and IN PARALLEL S22 v2 with the amended ladder into
`_plug_adaptive_v2` (determinism check against the 18:28 design at its
end). Expected: S22 v2 ~00:00 (A-8 VOID at rung 2, A-9 likewise if the
uniform control's rungs fail to certify), S23 verdict ~01:30, PDF after.
The S22 log of 08-10 and the S23 rows [X-PAKN]/[X-PGRS] are re-stamped
from these runs when they close (numbers of record replaced, the 08-10/11
logs kept as history with this note).
