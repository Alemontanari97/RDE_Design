# LAB-WF — the laboratory frame against the wave frame, 3-D (2026-10-05)

Plain rules: short sentences, physics before method. One page. Check of record: `validation/labwf_check.py` [X-LABWF].

## Why
In the frame that turns with the detonation wave the RDE outflow stands still: ONE steady 3-D run replaces a long
time-accurate run. That is what makes the 3-D CFD affordable as the twin's judge. Amendment A-REPR of the twin protocol
admits it as the evaluator of record only if a laboratory-frame run of one plug gives the same wall thrust within one
third of the thrust-stand band (0.17 percent). PILOT-WF (2026-09-30) had compared the wave frame with 12 frozen
pictures, not with the laboratory frame. The owner asked for the laboratory-frame run on 2026-10-05.

## The pair: everything identical but the frame
- Plug: Rao's plug on the methane case (RaSDT: CH4/O2 phi 1, 20 atm mean, 12-phase blowdown, 87 mm, 0.5 atm outside).
- Same mesh (`RDE/Nozzle/MESH/wf3d_RaSDT.dat`, 30 blocks, 2-degree columns), kit, the 12 sector states, far field (406),
  CFL 0.4, scheme (RK2, HLLC, MUSCL-minmod), binary (MOSE_open dcc627d8). The boundary files are identical record by
  record except the 5760 inlet faces.
- Wave frame: the run of record `wf_RaSDT_phases` (rotating frame at 6364.5 Hz, inlet 405 standing still, 1 ms).
- Laboratory frame: new, job 304078 (1 ms = 6.4 turns). Inlet = BC 410, a periodic table: the face at azimuth theta takes,
  at time t, the sector state at theta + Omega t (181 samples per turn). Checked before the run: at t = 0 the table equals
  the 405 states to 3e-16; at T/12 the pattern has moved 30 degrees the right way.
- The readers were checked on the wave field turned by 30 degrees: thrust, sectors and the whole field to 1e-12.

## Result
| quantity | laboratory | wave frame | difference |
|---|---|---|---|
| wall C_F (12 phases), turns 2-6 | 1.406303 (flat to 1.8e-5) | 1.407115 | -0.058 % (line 0.17 %: PASS) |
| of which the walls (plug + cowl pushes) | | | -0.0065 % |
| of which the inlet data | | | -0.051 % |

- The -0.051 percent is the INLET DATA, not the frame. MOSE_open interpolates each primitive linearly in time between the
  table's samples; across a sector jump the columns in transition carry less momentum flux. From the table alone:
  -5.4e-4 of the inlet term at 180 samples per turn, halving with every doubling (first order, to zero). Prediction
  -0.050 percent of C_F against the -0.051 measured.
- Sector by sector (walls only): sectors 1-11 agree within 5e-4 in C_F units; sector 0, just behind the front, is 3 percent
  lower in its own wall term. In the laboratory the front crosses the cells; in the wave frame it stands still.
- Wall probes (5 on the plug, 2 on the cowl): time means within -0.66..+0.30 percent; instantaneous median error 0.35-0.67
  percent. With the opposite turning sense: 29-90 percent (the control).

## What it means
For the wall thrust the two frames are equivalent to 0.007 percent once the inlet momentum is the same. The 3-D
wave-frame CFD passes the A-REPR gate: it is the evaluator of record of F3.TWIN.

## What is not shown
- The base and the plume. The far field (406) acts differently in the two frames (in the wave frame the still air is a
  Mach-8 cross flow): the exhaust field differs by 2-6 percent (median) outside the nozzle, and the base probe by 26
  percent. The base is not judged in either frame.
- One plug, one case, one grid (2 degrees), frozen chemistry, Euler.
- A laboratory run with a finer inlet table (nt >= 1440 brings the inlet term under 0.01 percent).

Data: `validation/_labwf/` (lab_post.json, wave_post.json, compare_lab_wave.json, the two case.json, the 8 probe files,
labwf_spec.json); the tools that made them, filed as text with their md5 in `validation/_labwf/tools/`: labframe_case.py
08e404bf, waveframe_case.py 9818292d, post_labframe.py ee6308d3, post_waveframe.py 2fa30df6, compare_lab_wave.py 21eaf769,
lab_run.sbatch d1080112, lab_collect.sh 6dc6c1b2. Session log: `validation/PROGRESS_2026-10-05_F3TWIN.md` section 1.
