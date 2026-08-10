# HANDOFF — S15 [F2/A1] Brick 2 step 1: thrust functional + gradient
# (host s2, 2026-07-25 → 2026-07-28; written to be resumable cold)

## 0. One-paragraph orientation

The program's declared NEXT-1 ("A1 brick 2", plan D6 item 9) is being
built: turning the validated differentiable MoC march (Brick 1) into a
profile OPTIMIZER. Step 1 is DONE and certified: the march now has a
scalar objective (thrust J, computed by two independent routes whose
agreement is a momentum-theorem test) and an exact reverse-mode
gradient dJ/dP (verified against finite differences in derived bands).
8/8 PASS. No optimizer has run yet — that is the next step.

## 1. What exists after this session (all on host s2)

NEW / MODIFIED (uncommitted — see §4):
  validation/a1_thrust_functional.py   NEW carrier, 8/8 PASS (390 s).
  validation/a1_ideal_march_jax.py     ADDITIVE only: run_march also
                                       returns wall_u, wall_v (states it
                                       already computed). Brick 1
                                       numerics untouched; its own suite
                                       re-run on s2: VERDICT PASS.
  docs/rde_nozzle_A1_brick2_thrust.md  tight assume-nothing explainer
  docs/rde_nozzle_A1_brick2_thrust.pdf   (user wants the PDF; 3 pages)
  docs/build_pdf_a1_brick2.py          md -> pdf builder (fpdf2; s2 has
                                       NO latex/pandoc). Re-run after
                                       every md edit.
  docs/rde_nozzle_PROGRESS.md          S15 ORA entry prepended.

ENVIRONMENT (s2, not portable):
  .venv-a1/                jax 0.10.2 + cantera 3.2.0 + fpdf2
                           (python 3.11; CPU jax is fine at this scale)
  GENO -> RDE/codes/GENO   symlink, READ-ONLY use (thermo tables).
  gfortran 12.2.1 + cmake  PRESENT on s2: the old G0/O3.4 toolchain
                           blocker is removable here (GENO not yet
                           rebuilt — deliberate, next steps).

## 2. Results of record (details in docs/rde_nozzle_A1_brick2_thrust.pdf)

  J(vacuum gauge)      1.2552079e+08   (twin case NI=21 da=0.5 Ne=41 eps=4)
  R_mom fine           +2.85e+03  vs derived Richardson band 4.01e+04
  coarse/fine ratio    4.52  (~4 expected: 2nd order confirmed)
  gauge delta          3.35e-08   vs allowed 1.78e-06
  dJ/dP                [ +2.4886597e+08, +1.4502984e+06,
                         -8.4257e+01,    +3.4038139e+06 ]  (yt,rtu,rtd,eps)
                       all 4 inside FD Richardson bands
  rejectors            R1 (wall sign), R2 (dropped peAe), R3 (permuted
                       grad): all correctly REJECTED.

Incident worth remembering: the FIRST referee version left a sliver of
wall uncovered between the IVL top node and the first wall-polyline
node (control surface not closed). The GAUGE TEST caught it exactly as
designed; fix = prepend the IVL top node (ivl_top()) to the wall
integral. R_mom tightened once the sliver stopped hiding inside it.

## 3. How to resume (commands, from the repo root on s2)

  .venv-a1/bin/python validation/a1_ideal_march_jax.py     # Brick 1, ~8 min
  .venv-a1/bin/python validation/a1_thrust_functional.py   # step 1, ~6.5 min
  .venv-a1/bin/python docs/build_pdf_a1_brick2.py          # rebuild PDF

Gotchas that cost time this session:
  * jit compilation dominates runtime; give background runs >= 600 s.
  * the harness shell cwd can RESET between commands — use absolute
    paths or re-cd every command (one patch was silently lost to this).
  * fpdf2 markdown: "--" means UNDERLINE; the builder maps em-dashes to
    " - " (do not reintroduce "--" in the md prose).
  * carrier quirk: ivl_flux reads CASE["NI"]; the refined-referee calls
    temporarily mutate A1.CASE["NI"] (save/restore pattern in main()).
    Tolerable at this size; refactor to a parameter when touched next.
  * s4 of Brick 1 SKIPs (declared): no WSL on s2; GENO binary not built.

## 4. NOT COMMITTED — this tree is not a git checkout

s2 hosts a COPY of the repo (git lives on the user's WSL machine).
Porting checklist (user action, or next session on WSL):
  1. copy the five files of §1 into the WSL checkout;
  2. re-run both carriers there (expect identical verdicts; jax pinned
     0.10.2, cantera 3.2.0);
  3. commit with tag [F2/A1], message naming the carrier and the
     additive Brick-1 change; PROGRESS entry is already written.

## 5. Next steps, in order (with entry points)

  [UPDATE 2026-07-28, same session, steps 2-3 DONE:]
  * validation/a1_corner_instrument.py  5/5 PASS (82 s) — corner meter
    L.15 at the lip + f2 controls; vacuum theorem read off the meter;
    sign == dJ/deps. PENDING declared: f2-const positive control on a
    real TOC (needs GENO build).
  * validation/a1_driver_eps.py  4/4 PASS (231 s, 13 marches,
    json-checkpointed) — FIRST OPTIMIZATION: blind golden on eps lands
    at 5.15512 vs closed-form 5.150634; p_e==pa at the optimum within
    derived band; corner meter certifies; corrupted objective rejected.
  * docs/rde_nozzle_A1_brick2_thrust.md/.pdf updated (4 pages) with an
    executive summary + steps 2-3; PROGRESS S15 entry extended.
  * march timing on s2: ~20 s per adaptive march (much faster than the
    early estimate — searches are cheap; only AD compiles are minutes).

  [UPDATE 2, same session, step 4 DONE:]
  * validation/a1_wall_march.py — PRESCRIBED-WALL MARCH (the structural
    inversion). Twin stage 5/5: J_wall(new engine on Brick 1's own
    contour) == J_exit within Richardson band (rel 1.3e-3); mass through
    last column == mdot; min wall M 1.20; corrupted wall rejected by
    march failure. Grad stage 2/2: envelope identity |AD-secant| 29 vs
    band 109 after separating curvature (J''=-7.3e7) from TABLE RIPPLE
    (0.010% of grad, 1.2e-8 of J) caused by piecewise-LINEAR EOS table
    interpolation. LESSON OF RECORD: pointwise AD-vs-FD is ill-posed on
    tabulated thermo; certify the envelope. Cubic interpolation would
    remove it at source. Applies to the CFD-adjoint track too.
  * What remains of "prescribed wall": spline control-point vector +
    TR-SQP driver (plumbing on the verified scalar path), then the GENO
    TOC oracle (O3.3/C-O33), then the cycle layer + T3 zero-gain.

  [UPDATE 3, same session, GENO REBUILT + ORACLES LIVE:]
  * GENO rebuilt on s2 (gfortran 12.2.1, out-of-tree build; bin/GENO
    REPLACED — old binary needed libgfortran.so.4, unrunnable). tocnoz
    regenerated (backup of pre-s2 fields in scratchpad).
  * O3.4 cross-code oracle VERDICT PASS (218/218, 95% reproduction,
    84x feet discrimination). G0's toolchain residual closed on s2.
  * Brick 1 S4 LIVE: contour vs s2-GENO 62/62 in band, max err 7.6e-9.
    No SKIPs left in Brick 1.
  * f2 POSITIVE control landed (closes X-A1CI pending): true type-2
    TOC (eps=4, xtronc=5.5 < L_id=7.3409): f2 const to 4.0e-3 on the
    terminal characteristic vs 0.60 along the wall (149x). NOTE the
    physics lesson: a TRUNCATED TOC (tocnoz, xtronc=10) does NOT
    contain its control surface — first diagnostic correctly found no
    constancy there.
  * NOW UNBLOCKED: O3.3 — our optimizer rediscovers the type-2 contour
    (discharges C-O33). Scratch cases: scratchpad/toc_eps4_full (TOC
    reference), scratchpad/a1_geno_ideal_ni21 (reduced twin, used by
    A1_GENO_CASE env var).

  [UPDATE 4: O3.3 EXECUTED, 9/9 PASS — validation/a1_o33_toc.py]
  * Part 1 (integrals): f2/lambda2 cross-code on GENO's terminal
    characteristic (level match 9e-5 rel); lambda3 profile match;
    wall rejector 158x. Part 2 (stationarity): interior AD grads
    1000x below lip, 40x below perturbed-wall; AD==FD ~1%; J(TOC) >
    J(perturbed). C-O33 numerical content DONE; formal registry
    discharge at WSL commit time. Follow-ups declared: exact terminal-
    characteristic trace (lambda3 constancy proper); optimize OUR J
    from the TOC start (strict-zero stationarity).
  * New carriers/cases: a1_o33_toc.py; scratchpad toc_eps4_full,
    o33_march_{21,41}.npz, o33_*.log.

  [UPDATE 5: CYCLE LAYER DONE — a1_cycle_layer.py]
  * T3 ZERO-GAIN ORACLE 5/5 (blind cycle opt == design-at-mean, gain
    -475/1.16e8 in band; corrected peak design loses 4.8e6; Lemma A
    live: per-phase walls identical to 8.9e-16). Bugs caught: enthalpy
    zero-point offset (relative stagnation construction + scaling-law
    rejector); pressure-blind peak design (fixed-Me variant).
  * MOCK RDE (user-posed, P+T exponential in theta) 6/6: cycle optimum
    eps=5.1395; pressure-weighted mean-state design (<PT>/<P>) is the
    best one-number closure (derived comparison, corpus lesson at
    engine level), its penalty 2.5e-6 rel (second order, gamma-probe
    scale); peak design -4% J. TABLE-RANGE TRAP: first run exceeded
    T_TAB_HI and np.interp clamped SILENTLY — range rejector added;
    check table bounds for any measured-cycle input.
  * Cached cycles in validation/_cycle_ckpt.json; figure
    figs_a1/cycle_layer.png; PDF now 10 pages (7 figures, equations).

  [UPDATE 6, 2026-08-05: TRANSVERSALITY METER + PLUG STARTED]
  * a1_cycle_corner.py 8/8: T7(c) executable on both cycles — votes
    monotone, one sign change, mean ~0 in band, no phase individually
    satisfied (the theorem measured); peak design flagged. Bands from
    the scales present (arbitrary 10x multipliers corrected).
  * a1_freejet_unit.py 6/6: free-pressure-boundary unit cell (ANGLE
    parameterization — modulus form had a clamped spurious root on
    compressing edges, caught+reformulated); PM known answer at
    machine precision on gconst tables. Plug assembly = next: columns
    with mirrored-family inverse-wall (spike below) + this cell above,
    no axis; twin vs GENO plug path (needs RaoPlug S1/S2 fix).

  [UPDATE 7: PLUG ASSEMBLY IN PROGRESS — a1_plug_march.py]
  * Certified pieces: freejet cell 6/6; wallbot cell (y-parameterized
    foot — vertical-chord div0 caught by cert localizer); mirrored
    bottom-up interior cell; planar exact-field oracle harness (PM
    corner jet, RK4 exact streamline spike, exact start line).
  * Two measured structural lessons: (1) edge fed from the previous
    column -> degenerate zero-step root on straight edges => bottom-up
    sweep, edge fed from ITS OWN column top; (2) fixed-row
    quasi-vertical columns TANGLE downstream => need Brick-1-style
    characteristic-aligned columns WITH row insertion (bell's j2+=1).
  * ROUNDS 2-3: aligned columns + row growth (M+=1/col) + CHARACTERISTIC
    PACING (dx = gap/|lm|; lesson 3: the C- family flattens, feet escape
    adjacent columns) -> wall 22%->55%, failure reproducible at the same
    station both resolutions. NAMED DEFECT (probe): wall angles exact to
    4 decimals, wall SPEEDS decay monotonically (spurious subsonic at
    stn 19) once pacing clamps at 0.30 — midpoint compatibility over
    0.3-long C- segments through the fan gradient is systematically
    biased. FOOT-ADJACENCY vs STEP-ACCURACY conflict under one-column
    chords.
  * NEXT BUILD (fresh session, fully specified): MULTI-COLUMN FOOT
    SEARCH in the wallbot cell (C- foot on the stored near-wall
    polyline across previous columns — plug analogue of the bell's
    wall_search); keep short paced steps. Then GENO plug twin (after
    RaoPlug S1/S2 fix); then truncated-plug cycle. Figures votes.png +
    plug_oracle.png added to the PDF (12 pp).

  [UPDATE 8: DOC OVERHAUL] The PDF is fully restructured in a didactic
  format (Question/Idea+drawing/Built/Results/Lessons per step); new
  schematics module docs/build_schematics_a1.py (5 drawings incl. the
  three plug lessons); plots refined (votes, jeps inset, plug_oracle
  reframed — a diverged mesh point had stretched the y-axis to 8000,
  caught on visual check); builder supports ###, ---, $$, images.
  Regenerate chain: build_figs -> build_schematics -> build_pdf.

  Remaining, in order:

  1. (DONE) CORNER INSTRUMENT: evaluate Rao's endpoint condition (L.15 of
     docs/rde_nozzle_P2_lemmaA.md: sin(2 theta_E) = (p-pa) cot(alpha) /
     (rho W^2 / 2)) at the lip from out[wall_*]; plus f2(y) along the
     terminal characteristic with its NEGATIVE control (f2 must NOT be
     constant on this type-0 nozzle; it must be constant on a GENO
     type-2 TOC).
  2. (DONE, 1-DOF golden variant) DRIVER: bounded quasi-Newton over P=[yt,rtu,rtd,eps] with a length
     constraint (scipy in the venv) — first optimized profiles within
     the four-knob family. Cheap: gradient already verified.
  3. (DONE at single-parameter level, X-A1WM) PRESCRIBED-WALL MARCH: wall spline as INPUT,
     flow computed on it via the existing inverse-wall unit process;
     TR-SQP + corner condition. The one structural change to Brick 1.
  4. GENO BUILD on s2 (toolchain present; Cantera/Sundials/Tecio OFF,
     see validation/g0_geno_crosscode.py header for the S10 recipe) →
     regenerate CASES/tocnoz → type-2 TOC oracle contour. Recovering it
     from a perturbed start = O3.3, discharges registry C-O33.
  5. CYCLE LAYER: T3-class phase family, J = Int F dmu, mu-weighted
     wall + WEIGHTED transversality (w(xi) — never the naive average),
     T3 zero-gain oracle (must return Rao-at-<Pc> with EXACTLY no gain).

## 6. Wider context decided in this conversation (memory files exist)

  * CFD route (project_cfd_adjoint_route.md): SU2 first then port to
    MOSE; BOTH adjoints cross-checked; shock-free cases first. The MOC
    harness being built here is the oracle bank that CFD work will be
    judged against (Rao oracle, T3 zero-gain).
  * GENO is generator + referee, NEVER differentiated or modified
    (standing user decision S5).
  * Explainer web artifact (whole-theory companion, updated through
    this conversation):
    https://claude.ai/code/artifact/5dc49aca-4c92-420d-844b-e6bf46d5dbf0

## Update 9 (2026-08-05) — doc pipeline moved to LaTeX (GENO-doc format)

User: "some plots are non sensical in what they show. Be more clear as
in the GENO explanation PDF. Also use the same format of that previous
document." The reference is `GENO/docs/GENO_theory_and_implementation.pdf`
(LaTeX report, pdfTeX). Done:

- NEW doc source of record: `docs/brick2_doc_src/` (preamble/main/8
  chapter .tex files, same report-class format as the GENO doc;
  bibliography Rao/Zucrow/GENO/theory). `build.sh` compiles with
  tectonic (installed at `/data10/falco/bin/tectonic`, self-contained,
  caches its bundle in `~/.cache/Tectonic`; s2 has NO TeX Live) and
  installs to the SAME path `docs/rde_nozzle_A1_brick2_thrust.pdf`
  (now 24 pp). The old fpdf2 builder `docs/build_pdf_a1_brick2.py` is
  RETIRED (md carries a superseded-note).
- Figures rebuilt in GENO-doc style by `docs/brick2_doc_src/
  make_figures.py` -> `figs/*.pdf` (vector). Two figures were
  redesigned on DATA grounds, not just style:
  1. cycle figure: the old zigzag was REAL data mixing — the cycle
     checkpoint holds (a) stale phase families from earlier NXI/T0
     constructions and (b) TWO march-resolution families (13-pt survey
     vs golden-search trajectory, parallel curves ~1% apart in J).
     Fix: accept an eps only if all 5 keys of the CURRENT phase
     construction exist, then keep the survey family only
     (J >= 0.995 Jmax); search results enter as vertical lines. Two
     panels (T3 | mock), each normalized by its own optimum,
     y = (J/Jmax-1)*1e4.
  2. plug figure: panel (b) is now the P-2 meter itself (wall p/pa,
     marched vs closed form) from a cached fresh coarse march
     (figs/_plug_march.npz). NOTE the current-state truth: wall
     speeds are biased HIGH from the first paced column (2875 vs 1823
     m/s) and decay while the exact solution accelerates; pressures
     sit several p_a low. The md's "spuriously subsonic by station
     19" was the probe's reading on the fine run of the pacing round;
     the figure/caption now state only what the plotted data shows.
- jeps inset: no more matplotlib offset notation (deviation axis
  (J/Jmax-1)*1e5); f2 figure is 3 panels (location | invariance
  contrast | cross-code zoom); stationarity bars labeled by bump
  center (0.20L..0.85L, lip); votes annotations decollided.
- Schematics (two_routes/inversion/freejet/plug_lessons) kept as PNG;
  the pipeline schematic is now native TikZ in ch_intro (style key
  renamed box/ — `step/` collides with a TikZ built-in).
- Rebuild: `docs/brick2_doc_src/build.sh` (uncomment the
  make_figures line inside it to refresh figures first).

## Update 10 (2026-08-05) — figures 7.2/7.3 redrawn (user: "make no sense")

- Fig 7.2 (plug lessons) is no longer an abstract dot sketch: rebuilt as
  `fig_plug_lessons.pdf` in make_figures.py, three panels drawn IN the
  oracle world (same lip/spike/edge/fan). Panel 3 uses the REAL
  geometry: integrating dy/dx = tan(theta-mu) from a wall station in
  the exact field shows the arriving C- is EXACTLY a straight ray
  through the lip (checked: passes (0,2) to machine precision; state
  constant along it, M=1.78 the whole way) — so the midpoint bias is
  interpolation ACROSS rays on the column, over one long
  adjacency-forced chord. That's the cleanest statement yet of why the
  multi-column foot search is the fix. sch_plug_lessons.png retired
  from the doc.
- Fig 7.3(a): the interior-mesh scatter is REMOVED deliberately (255
  points, no two share a column — no structure to show) and replaced
  by the marched free-edge trajectory vs the exact edge: it holds
  p=pa exactly (speed = closed form 2405) but lands upstream of the
  start line and hugs the spike. Caption states the omission and why.
- C- trace cached at docs/brick2_doc_src/figs/_cm_path.npy.

## Update 11 (2026-08-05) — MoC primer added (user: "suppose i don't
## know how the code computes characteristics and new points")

New Section 1.3 "The solver in one page: characteristics, cells,
columns" + fig_moc_primer.pdf (3 panels: two characteristics per
point / the interior cell with midpoint closure + Newton / columns,
sweep and the wall-cell foot). Defines every term the later chapters
lean on (cell, column, foot, compatibility, midpoint rule,
Newton-certified) assuming zero MoC background; the free-jet edge is
introduced as the position-free/pressure-fixed dual of the wall
cell. Cross-referenced from ch. 4 (inverse-wall) and ch. 7 (the
three plug lessons are re-stated as statements about these objects).
Doc now 25 pp.

## Update 12 (2026-08-05) — fan-singularity figure + clarity pass on
## the problem figures

- NEW §7.2 paragraph "Why the lip fan cannot be marched through" +
  NEW fig_fan_singularity.pdf (Fig 7.1, 3 panels in the oracle
  world): (a) the lip as singular point (uniform M1 / fan / uniform
  M2, one point carrying every state), (b) what breaks for an
  ordinary cell (midpoint averages across the whole jump; C- rays
  meet at one point so the crossing degenerates; quotes the measured
  cert 8.9e9), (c) the cure (fan seeded as exact PM data, ordinary
  cells resume between rays; oracle start line downstream).
- sch_freejet.png RETIRED: redrawn as fig_freejet.pdf (Fig 7.2) in
  document style — (a) the cell with p=pa fixing |q| and the angle
  free, (b) the modulus-form sign trap vs the angle fix.
- fig_plug_lessons sharpened: panel 1 now SHOWS the stagnation
  pile-up (repeat hollow circles at pt3), panel 2 draws the
  cross-family segments tangling through the fixed rows (with x
  marker), panel 3 renders the closure chord as a translucent
  orange band over the blue ray so chord and characteristic are
  distinguishable. Doc now 26 pp; figure numbers in ch. 7 shifted
  (oracle-vs-march is now Fig 7.4).

## Update 13 (2026-08-05) — "why would the free jet not advance?"

New §7.4 paragraph "Lesson 1 in full: why the edge could not
advance": pt4=pt3 is not a Newton accident but the UNIQUE root of
the old stencil — streamline condition trivially satisfied by a zero
step, p=pa already holds at pt3, and on a straight edge the C+ from
the previous column's interior crosses the edge exactly once, at
pt3 (where it was built). Underneath: domain of dependence — the
previous column's characteristic cone tops out at pt3, so that
stencil holds no information about the edge beyond it; curvature
masked the bug (linearized streamline admits a slightly advanced
root) until the edge ran straight. Bottom-up sweep feeds the edge
from its own column, whose C+ crosses the edge downstream.

## Update 14 (2026-08-05) — lesson-1 mechanism corrected (user probe)

User: "if pt3 belongs to the previous column, how can the
characteristics of that column end up on pt3 for the next step?" —
caught an imprecision in the Update-13 paragraph (it implied pt1's
C+ "built" pt3 directly). Corrected formulation now in §7.4: in a
characteristic mesh the ROWS ARE the C+ lines; pt3 is the previous
column's TOP node, built one step earlier as the exit of the top
row's C+ polyline through the edge; the previous column's top
interior point is the preceding station of that SAME line, so
re-drawing "the C+ from pt1" re-finds the recorded exit (a straight
line crosses a straight edge once) → pt4=pt3. Consequence stated:
each edge point CONSUMES one characteristic line; the next edge
point needs the NEXT line below, whose last interior station is the
CURRENT column's top — lessons 1 (feed from own column) and 2 (grow
a row per column) are two halves of one bookkeeping: one
characteristic in, one edge point out.

## Update 15 (2026-08-05) — lesson-1 geometry figure + mechanism
## wording finalized

User probe #2 ("how can the C+ of an interior point of the same
column as pt3 intersect pt3?") caught that the Update-14 "rows are
the C+ lines" phrasing was an over-specific reconstruction. Final
formulation (in §7.4 + NEW Fig 7.5, fig_edge_root_geometry.pdf):
pt3 exists in the mesh ONLY as the recorded exit of a C+ segment
launched from the previous column's top data, so a sender from
there lies on pt3's own characteristic (exactly where flow/edge are
straight — discrete segments lie exactly on straight
characteristics; O(h^2) misfit where curved, which is what masked
the bug); re-drawing that line can only re-find its recorded exit.
The WORKING cell never asks its C+ to hit pt3: it must cross the
STREAMLINE through pt3 (slope tan(th), shallower than the C+'s
tan(th+al)), which a steeper line from below catches strictly
downstream. Fig 7.5: (a) broken feed re-finding the recorded exit,
(b) the two-slopes advance geometry. Doc 27 pp.

## Update 16 (2026-08-05) — PLUG MARCH CERTIFIED 5/5 + document
## reformat (full explanations, bugs to appendix)

THE ORACLE PASSES. Two fixes landed in validation/a1_plug_march.py:

1. MULTI-COLUMN FOOT SEARCH (replaces characteristic pacing): march
   at the fine PRESCRIBED stations; the wall cell scans the whole
   previous column (up to 3 columns back) for the segment bracketing
   its arriving C- (bracketing f_j = (y4-y_j) - lm_j(x4-x_j),
   positive at the previous wall, first sign change = foot segment;
   choices recorded in sched key "wfoot" for replay). Chords shrink
   0.30 -> station spacing. Effect: P-2 55% -> 98% in band (max dev
   4.7pa -> 9.8e-3 pa), P-1 edge angle in band (3.2e-4 vs band
   4.5e-3).
2. ROW CONSUMPTION at the wall (the 4th measured lesson): with fine
   stations a near-wall row's C- terminates on the wall BETWEEN
   stations; prolonging it leaves only the BACKWARD Newton root — a
   converged, certified, wrong-branch crossing — and a ghost mesh
   limb grows below the spike carrying the M1 state (409 points,
   mass +9%, INVISIBLE to P-1/P-2/cert: only the mass balance saw
   it). Fix: rows below the new wall foot are retired and the column
   re-indexed (jsrc0 = jf+1) — the dual of the edge adding one row
   per column. Mass closes to 0.026% (2.33 vs band 26).
   plug_march(..., consume=False) is kept as a diagnostic switch to
   reproduce the regression (used by the appendix figure).

VERDICT OF RECORD: 5/5 PASS, 64 s. cert coarse 0.019 (n=1253) /
fine 0.017 (n=4870); P-1 angle 0.41809 vs dnu 0.41777; P-2 98%;
P-3 |d|=2.33 (band 26); R-1 fires (20x out of band).

FIGURE-DRIVER BUG FOUND while regenerating: the old fig_plug driver
fed the start line INVERTED (edge-first; carrier expects row 1 =
wall) — all previous plug FIGURE renders showed a bogus march, not
the oracle's failing run (the failure looked similar, so it hid).
Fixed in docs/brick2_doc_src/make_figures.py (_plug_data now
wall->edge and runs the real carrier; caches _plug_march.npz and
_plug_march_noconsume.npz; the stale _plug_march_before.npz deleted).

DOCUMENT REFORMAT (user): main chapters now "explain it whole" (a
"How it works, in full" section per step), ALL bugs/traps/lessons
moved to Appendix A (ch_appendix.tex): sliver, f2 rejector, table
ripple, 3 cycle traps, sign trap, plug lessons 1-4 (incl. the new
ghost-rows lesson + fig_plug_before from consume=False).
ch_plug rewritten around the CERTIFIED march; pipeline box + status
table + abstract updated; fig_plug now shows the certified mesh.

## Update 17 (2026-08-05) — P-4 momentum closure + STAGE=axi 5/5 +
## GENO-twin gate scoped

- P-4 wired into the planar oracle (declared in the docstring since
  day one, never implemented): pa-gauge momentum theorem, F_out =
  F_in - wall push, free edge = 0 by construction (p=pa exact).
  Helpers col_fluxes / wall_push_poly (module level, delta-aware:
  w = 2*pi*y for axi). ORACLE NOW 6/6 PASS: closure 6.9e3 on F_in
  2.0e7 (3.4e-4 rel, band 7.2e4, coarse/fine ratio 3.6 = 2nd order).
- STAGE=axi IMPLEMENTED and 5/5 PASS (39 s): delta=1 on NASA
  real-gas tables; start data = tables-consistent corner fan
  (dtheta = sqrt(M^2-1)/q dq on the tables' own M(q), turn 0.4395);
  spike = streamline of that data; checks A-1 cert (0.017/0.022) /
  A-2 mass 2*pi*y (505 on 1.085e5, band 986) / A-3 momentum closure
  (-2.4e6 on 2.4e8, in band) / A-4 SOURCE-ALIVE control (same data
  at delta=0 differs 156 m/s = 9x band — guards a silently-planar
  axi mode) / A-5 corrupted-spike rejector (5x band).
- GENO PLUG TWIN SCOPED AND GATED: GENO PROGRESS shows RaoPlug
  (type 8) at ~80% with open defects N-42/N-43 (mass match + 2nd
  DOF of Rao's 2-constraint solve) and OPEN OWNER DECISION D1
  (2-constraint fix — changes the contour — vs documented 1-DOF);
  GENO's roadmap assigns it a dedicated session (WS-C order
  Angelino->Migdal->RaoPlug). NOT a side quest for this carrier:
  needs the owner's D1 call first. Recorded in ch_status item 1.
- Doc updated: ch_plug §7.2.4 (P-4) + §7.2.5 (axi stage), results
  6/6 + 5/5, status table, pipeline box, intro; 32 pp.

## Update 18 (2026-08-06) — GENO RaoPlug session (owner D1 = "do it"):
## two-constraint solve LANDED + oracle recalibration

Executed as a dedicated GENO-side session (repo /data10/falco/RDE/
codes/GENO, 4 files modified, NOT committed — GENO's "commit after
CTest PASS" gate is unsatisfiable on s2, see below; everything
documented in GENO's CHANGELOG [Unreleased] S8 + PROGRESS ORA +
MASTER_PLAN N-65/66/74/75 + CASES/raoplug_gamma123/).

WHAT LANDED (GENO side):
- N-65 mass termination: boundarycurve_cminus_solve(mdot_target,
  exit_reason); curve stops where accumulated mass = pc*pi*yt^2/c*
  (bell backtracking pattern); default ON for type 8, opt-out
  mass_match=.false.
- N-66 second DOF: mass-set truncation D; corner condition at D
  returns pb_implied; constraint2=pb now meaningful ({mass, pb}).
- 4 rigor fixes, all measured on the gamma=1.23 synthetic gas:
  fixed-point hangs (absolute tolerances at machine-noise: 1e-8 on
  q = 5e-12 rel); 40-step valid-region scan = silent window edge
  (Rao members unreachable); validation-mode silent bracket clamp;
  corner-stop |res|<tol window-miss -> sign-change detection with
  backtracking (the historical NaN path: the curve marched past its
  own corner into the singular tail).

ORACLES (the certified content):
- DUALITY: mass-stop (exit 3) -> pb_implied 1.432443e5; legacy
  corner-stop at that pb reproduces the truncation to ~2e-5
  (L 0.93873/0.93875, eps 3.37062/3.37067, mdot 2419.69/2419.73).
- PLANAR EXACT LIMIT: curve = straight uniform characteristic
  (theta/q spread bitwise 0.0; slope spread 2.2e-7).
- INDEPENDENT INTEGRATOR (python: our certified _coef compatibility
  + f2+ invariance, Radau rtol 1e-10): member (2.4, -8.25) agrees
  with GENO 3-4 digits (eps 3.3712 vs 3.3706). f2+ conserved 0.0 in
  GENO's own curve — NOTE: f2+ conservation is an IDENTITY of the
  dq-dtheta coupling (holds for ANY dtheta) — the planar limit and
  the cross-check are what validate the source term.

ORACLE RECALIBRATION (GENO N-74): the registry's "Rao 1961 Tab.1"
numbers (eps=3.81, X_D/R_E=1.164, C_F=1.58 at M_E=2.4,
th_E=-8.25) are UNVERIFIABLE (the 1961 spike paper is not in
literature/ — only the review) and INTERNALLY INCONSISTENT (CF/eps
impossible as a gamma=1.23 vacuum pair; the (2.4,-8.25) member is
3.37/1.24/1.42 by two agreeing codes). OWNER ACTION: procure Rao
1961 "Spike Nozzle Contour for Optimum Thrust" to recover the true
table pairing.

CTEST ON S2 (GENO N-75): 17/26 md5 FAILs are PRE-EXISTING
environment mismatches (stash-test: identical verdicts on pristine
HEAD; idealnoz fails pristine; plugnoz broken by missing
thermo_plug.dat). OWNER ACTION: regenerate baselines on s2 or move
to tolerance-based comparison. Our 4-file change does not alter any
verdict.

GOTCHAS for resumption: GENO builds out-of-tree ONLY (in-tree
build/ has a stale MKL-2024 config); fresh configure with ifx
2023.1.0, USE_{CANTERA,SUNDIALS,TECIO,MPI}=OFF; binary lands in
repo bin/GENO. The one-step PM fan means theta_i must absorb the
fan discretization (35.33373 for the (2.4,-8.25) member at
Mi=1.10; near-sonic Mi hangs pre-fix). Oracle thermo:
thermo/thermo_gamma123.dat + gamma123.plt (committed-ready).

NEXT: the full-field twin — our plug march on GENO's Phase-1 spike
contour (now produced cleanly, rc=0) with a start line from GENO's
lip states; then truncated plug under the cycle.

## Update 19 (2026-08-06) — STEP 10 CERTIFIED: the truncated plug
## under the cycle (T-T4 + Remark 4.9), 5/5 + 9/9 PASS

NEW CARRIER validation/a1_plug_cycle.py + doc chapter 8 +
fig_plug_cycle. The theory's "first genuinely averaged shape
problem" measured end to end.

THE STRUCTURE THAT MAKES IT CHEAP: for a FIXED spike, one
full-spike march per phase yields J(l) for EVERY truncation l in
closed form (supersonic domain of dependence: removed wall cannot
affect upstream; free edge = 0 in the pa gauge; base at pb=pa = 0).
5 phases x 2 resolutions = the whole study.

THE WORLD: axi, NASA tables; lip (0,2); Mi=1.2 at theta_i=-25 deg;
per-phase tables-consistent lip fan to shared pa; spike = mean-field
streamline (fixed hardware); start line poses shared (M,theta)(y)
profile with per-phase thermodynamics. POSING LESSONS (both
measured): (1) PA_M too high (2.35) -> fan turn +40 deg -> "spike"
climbs above the lip (valley, garbage); PA_M=1.95 -> theta_E ~ 0 =
classic plug design condition, descending spike. (2) THE PLUG FEELS
pa (free edge; the bell does not): the PR=10 certified cycle puts
low phases 6x overexpanded = SHOCKED regime -> edge cells blow up
and garbage descends to the wall; shock-free posing bounds the
cycle: PR_PLUG=2.5.

RESULTS OF RECORD:
- t3 (pressure-only) 5/5: Lemma A at 4.7e-15 on the DERIVED
  pa-shielded wall region (x<0.81, edge C- traced) and breaking
  beyond = adaptation localized; ANTI-COLLAPSE: cycle l*=2.103 >>
  mean design 1.280, <= peak design 2.336 (the plug does NOT
  average — T3 belongs to fixed full-flowing walls; first stage
  drafts wrongly transplanted the bell collapse oracle and the
  "FAIL" was the theory working); nesting order l(xi) = 2.336/
  2.061/1.125/1.047/1.006 monotone in P0.
- mock (P,T) 9/9: nesting order again; NON-IDEAL ADAPTATION
  MEASURED (per-phase loss past own l(xi): 1.6e-4..2.0e-3 rel — the
  C-HT4 clamp does not hold); Remark 4.9 STRICT BREAK resolved:
  INTmax - maxINT = 1.07e4 N = 2.3e-4 of J (beyond band);
  peak-design penalty 2.2e-4 (beyond band); mu-averaged corner
  condition holds at l* (vote mean +1.8e4 Pa vs band 3.1e5, votes
  up to +-1.4e6); optimum = strict interior compromise; corrupted-pa
  rejector 2.3x out.
- NEW MEASURED PHYSICS: plug corner votes OSCILLATE (fan reflects
  off the free edge onto the wall): the bell's monotone vote
  structure does NOT transfer; only the mu-averaged balance and the
  compromise structure survive = exactly Remark 4.9's claim. First
  vote-monotonicity checks failed for this reason and were replaced
  by theorem-faithful ones (spread + interior compromise).

Doc: ch_plugcycle.tex (ch. 8), status table row, pipeline box,
reproduction; 36 pp. Remaining list: GENO full-field twin, swirl,
measured cycle, TR-SQP.

---------------------------------------------------------------------
UPDATE 20 (2026-08-07, session S18): STEP 11 — GENO FULL-FIELD PLUG
TWIN CERTIFIED 8/8 (validation/a1_geno_plug_twin.py, ch. 9 of the
PDF; fig_geno_twin). Also: step-10 posing-lesson appendix A.7 +
cartoon figure fig_plug_posing (Figure A.4) added on user request.

WORLD: GENO gamma123 two-constraint case re-run (bin/GENO of
2026-08-06, CASES/raoplug_gamma123/input.ini with absolute thermo
paths); outputs decoded: inf.sol = spike wall (4632 pts, 15-col
wrapped records), raoplug_cminus.dat = phase-0 IVL (196), plug_diag
= (phase,iter,j) field — phase 1 = 2488 C- member curves (the
design field), phases 2/3 = x<0 throat region. ref.npz extracted to
validation/_geno_twin/ (untracked, N-36 convention; extractor in
the carrier; provenance ini+performance copied).

POSING: all data GENO's own. Gas identified from the field: gamma =
recipe, Rg = 415.7255 (std 8.7e-9), EFFECTIVE isentrope p0 =
6.008172e6 != nominal 6e6 (uniform 1.1e-4); GENO gas is ANALYTIC
cp=const (Types_thermo_sm backend 0) — its field noise (h0 2.0e-5,
s 4.7e-6 R, p0 1.1e-4) is MoC-integration noise = the derived G-1
floors. Start = vertical Cauchy cut x0=0.15 through the 410 phase-1
curves crossing it (curve-wise interp, cross-checked 1e-5); wall =
GENO contour, slopes tan(theta_w) (tangency 1.6e-5); above-IVL
free-jet strip blended IVL-state -> last-member edge state
(domain-of-dependence-immune for wall+sub-IVL; blend-vs-uniform
null measured). Flux quadrature calibrated on the full IVL: mdot
2.4e-7, F 2.3e-7 vs printed — GENO's F is the ABSOLUTE-p integral.

VERDICT 8/8: G-1 gas twin in derived floors; G-2 cert both res;
G-3 wall p 100% within declared 3e-3 (median 1.9e-3, max 2.5e-3);
G-4 settled field (x>0.35) 97.7% within (q 1e-3, th 1.5e-3), meds
3.8e-4/7.9e-5; G-5 IVL mass 1.2e-3; G-6 IVL thrust 1.1e-3; R-1
gamma*1.01 -> 31%; R-2 wall*1.005 -> 0%. Thresholds DECLARED (not
truncation-derived) at the S8 3-4-digit cross-code level, >=2x
margin, provenance in docstring+ch.9.

THE FINDING (central): a measured cross-code gap ABOVE both codes'
truncation, characterized: (a) start transient near the cut
(mid-heights, |dth| to 1.1e-2 rad, dies by x~0.35, moves with the
cut = cut-ingestion artifact of near-lip fan curvature,
resolution-stable); (b) settled UNIFORM drift +4e-4 rel in q across
the whole column, LINEAR in marched length (x0 sweep 0.70/0.50/
0.30/0.15 -> 6.6e-5/1.9e-4/2.7e-4/3.0e-4 at fixed wall window).
FORENSICS (all excluded by measurement): gas (1e-8 equiv), wall
(1.6e-5), cut (1e-5 two routes; polyline 1e-4->5e-6 with N, drift
unchanged), strip (blend null + DoD), GENO discretization
(DIAGNOSTIC GENO build, DTHETA_COARSE/FINE + Rao dx HALVED:
self-shift 3.5e-6 = step-converged; sources REVERTED, bin/GENO
RESTORED md5 77da0dd2..), our K/N (dev moves <10% of itself).
Route-B residual audit run on BOTH meshes: 1e-8..1e-9 = the two
discrete systems are algebraically EQUIVALENT — and the audit is
TAUTOLOGICAL for accuracy (each code solves its own relations; it
cannot see slow bias; O3.4's real content = equivalence).
Wedge-from-a-C--curve test is DEGENERATE by construction (a
characteristic is not Cauchy data — lesson-1 geometry). Scale:
drift = 0.5% of the axisym source contribution (-5.4% of wall q,
delta=0 control). ATTRIBUTION OPEN: candidates live in what
refinement does not vary (GENO phase-1 backward-march re-interp
bookkeeping vs our foot-chord interp). OWNER ACTION: file the
GENO-side question (N-76 candidate) — this session did NOT land any
GENO change (diagnostic build only, tree verified clean).

Doc: ch_geno_twin.tex (ch. 9), status table row, reproduction line,
"what remains" rewritten (GENO thread CLOSED end-to-end; remaining:
swirl, measured cycle, TR-SQP); 41 pp. Caches: _geno_twin/
{ref.npz, blend_K81/161, bad_gamma_K81, bad_wall_K81, provenance}.

---------------------------------------------------------------------
UPDATE 21 (2026-08-07, session S18 cont.): STEP 12 — FREE-VORTEX
SWIRL MARCH CERTIFIED 9/9 (validation/a1_swirl_march.py, ch. 10 of
the PDF, fig_swirl; 44 pp). Also: (a) the mu-average-vs-mean-pressure
clarification folded into ch. 8 as "Averaging the problem is not
averaging the condition" (bell = linear in phase pressure -> averaging
commutes -> collapse legitimate; plug = free edge saturates to a FIXED
shared pa -> nonlinear -> mean-of-votes != vote-at-mean; measured
1.280 vs 2.103); (b) USER DIRECTIVE (durable, in memory): explain
concepts in PLAIN LANGUAGE, corpus tags (T3/T7/T-T4/Remark 4.9/
C-HT4...) only as one-time parenthetical citations — swept across all
chapters + in-figure texts.

SWIRL PHYSICS (derived + verified): free vortex y*w = Gamma ->
azimuthal momentum identically satisfied; Crocco forces meridional
irrotationality; EXACTLY two changes: state h = h0 - qm^2/2 -
G^2/(2y^2) (implemented via augmented speed qeff = sqrt(qm^2+G^2/y^2)
through the UNTOUCHED certified isentrope machinery, meridional M
rebuilt) + source c^2 v/y -> (c^2+G^2/y^2) v/y. Edge keeps the angle
parameterization: p=pa fixes TOTAL speed -> qm(y) explicit law.

SEAM: plug_march(cells=, q_edge=) additive (defaults = certified
path); oracle 6/6 + axi 5/5 re-run PASS after the seam.

MEASURED NUMERICAL LESSON (fixed): mixed O(1) geometry / O(u^2)
compatibility rows make the monotone-norm damped Newton STALL one
step short of the root (captured live: full step raises the
norm-dominating compat rows while fixing an O(1e-7) position error;
argmin damping rejects every candidate; cert_worst 2105-2563 vs 1;
manual undamped Newton from the same point converges to machine in 3
its; NOT a table-kink issue — gconst reproduces it). FIX: compat rows
nondimensionalized by the z-CONSTANT parent speed scale (pure row
scaling, root unmoved) -> cert 0.009.

VERDICT 9/9: W-1 Gamma->0 regression 2.1e-13 (band 1e-9); W-2 exact
radial-equilibrium duct (du/dy=0 exact result) preserved to 1e-15 in
u, v, wall p, edge y (Richardson bands); W-3 mass + pa-gauge AXIAL
momentum close on the expansion world (centrifugal is radial — axial
theorem unchanged, checked); W-4 swirl-alive 8.6x band + source-alive
12x band (the duct CANNOT see the source: v=0 multiplies it away —
that's why the expansion world exists); R-1 corrupted Gamma^2 x1.10
leaves bands by 12 orders. World: NASA tables, w/u=0.35 at y1,
M_m 1.71-1.73.

SPIRAL-PHASE QUESTION (user): answered + documented in ch. 10
Sec. "What this is, and is not" — the free vortex is the TIME-MEAN
azimuthal velocity; the helical constant-phase surfaces are a
DISTINCT unsteady-3D effect the quasi-steady cycle closure sets
aside (zero-reduced-frequency limit; RDE reduced frequency is O(1) —
honest stated limit; time-average partially insensitive: the spiral
reshuffles WHEN not WHAT; full physics = the CFD track, THOR-class).

Remaining queue: measured-cycle input, TR-SQP spline driver.

---------------------------------------------------------------------
UPDATE 22 (2026-08-07, session S18 cont.): DOCUMENT REWORKED FOR A
ZERO-BACKGROUND READER (owner directive: "very clear, do not assume
anything to be known; images must feature axis variables clear and
deeply connected to physics and how the program works" + "add images
to make concepts clearer"). 44 -> 65 pp.

CONTRACT: docs/brick2_doc_src/STYLE.md (binding) — audience
definition, hard rules (define-before-use; no registry tags as
explanations; numbers sacred; chapter opens plain-language;
self-contained captions with axes+units), the notation table, and a
per-figure axis plan. All chapter rewrites were executed against it.

NEW FRONT MATTER (4 chapters, ~20 pp, assume nothing):
- ch_intro (rewritten): what the document is, who it is for, the two
  ground rules, the referee principle, the road map, pipeline fig
  updated through twin+swirl.
- ch_nozzle (NEW): the machine; choked throat = mass-flow constraint;
  stagnation state; area ratio; thrust balance; WHY an optimum exists
  (p_e = p_a) incl. the vacuum case; three nozzle families (ideal /
  Rao TOC / plug) with altitude compensation; the RDE and the cycle;
  what a gradient/adjoint buys.
- ch_moc (NEW): the method of characteristics from zero — Mach cone,
  the two families, compatibility, the cell (midpoint = 2nd order),
  Newton certification, columns, the three boundary cells (axis,
  prescribed wall + FOOT, free jet), why centered fans are
  constructed not marched, real gas + AD.
- ch_method (NEW): rule 1 (derived bands, Richardson, K_RICH=4, the
  declared-threshold exception named), rule 2 (rejectors), reporting
  conventions (m/n PASS, Newton-certified, result of record, oracle,
  internal closure, alive control), + FULL SYMBOL TABLE tab:notation.

NEW FIGURES (all from real run data unless labelled schematic):
- fig_nozzle_primer: (a) the machine [m,m]; (b) M and p [bar] along
  the real marched wall; (c) eps vs p_e [bar] crossing p_a (driver
  cache) = the optimum, starred.
- fig_bell_vs_plug: (a) bell (Brick-1 contour); (b) plug = GENO's
  REAL spike + our marched plume boundary + base; (c) altitude
  compensation COMPUTED: p_a [bar] vs plume angle theta_E [deg] via
  PM on the twin's own gas.
- fig_rde_cycle: (a) annulus + rotating wave; (b) phase vs P0 [bar] /
  T0 [K] (the actual mock cycle); (c) per-phase perfectly-matched eps
  via CL.eps_star_at_pa = the compromise problem, spread 3x.
- fig_method: (a) EVERY check of the document as measured/its-own-band
  (log) with rejectors on the same axis and the threshold at 1 —
  the whole method in one picture; (b) where a band comes from.

AXIS REWORK (binding plan in STYLE.md sec.4): every figure now
dimensional — pressures in bar (plug, plug_cycle, posing, twin,
swirl, votes), thrust in MN/kN (jeps, cycle, plug_cycle b: was
normalized ratios), speeds in m/s (twin b/c: were relative), gradient
in N/m (ripple, stationarity), arclength in m (f2: was normalized),
coordinates x,y in m everywhere (was x/y_t or bare $x$). fig_swirl(c)
replaced: cartoon -> real w(y) profile + spin energy share.

CHAPTER REWRITES: 4 agents under the contract (score/firstopt/
wallinput; referee/cycle; plug/plugcycle; twin/swirl/status/appendix).
Each chapter now opens plain-language, defines every term at first
use, captions self-contained. Verified: no stale sec:primer refs, no
missing figure files, no stale normalized-axis caption language, no
undefined LaTeX refs; numbers/PASS counts/labels preserved.

---------------------------------------------------------------------
UPDATE 23 (2026-08-07): STEP 13 — CONFIGURATION COMPARISON
(validation/a1_config_compare.py). Owner asked for bell vs plug vs
truncated vs swirled at one RDE-like operating point. Suite reports
7/10 — the three failures are REAL and are the result; they were NOT
tuned away.

COMMON BASIS (the hard part, and it is right): same NASA tables, same
chamber (P0 2.53e7 Pa, T0 3739.9 K), same p_a 7.6144e5, same MASS
FLOW 4.2476e4 kg/s -> hence same A_t (choked throat), hence C_F and
Isp directly comparable; plus same ENVELOPE radius 2.2695 m (the
bell optimum's own exit radius). Thrust for BOTH sides is the
ambient-gauge momentum flux through a surface enclosing all hardware
— for the plug F_in(x0) already contains everything upstream because
the free edge contributes exactly zero in the gauge.

NUMBERS OF RECORD (this run):
  bell (area-ratio optimum)   F 116.474 MN  C_F 1.46540  Isp 279.62  L 7.34
  plug, full spike            F 116.148 MN  C_F 1.46131  Isp 278.84  L 6.00
  plug, truncated             F 116.148 MN  C_F 1.46131  Isp 278.84  L 3.69
  plug, truncated + swirl     F 111.839 MN  C_F 1.40709  Isp 268.49  L 2.56

MEASURED DEFECT THAT BOUNDS THE CONCLUSION: the plug marches carry a
+1.5% MASS NON-CLOSURE (out vs in). Forensics: NOT accumulation (same
1.46-1.48% at X_END 1.2 as at 6.0), NOT discretization (1.47/1.38/
1.37% at K,N = 61/41, 121/81, 181/121 — barely moving), NOT cell
aspect ratio (1.47-1.67% across dx/dy from 0.63 to 5.05). LOCALIZED:
column-by-column trace shows mass jumps +1.454% in the FIRST marched
column and is then flat to the end (+1.464% at the last). The free
edge leaps y 2.2695 -> 2.3398 in one step (slope ~1.5 where the
edge should be horizontal, theta_E = 0 exactly by construction).
=> a free-edge START-UP inconsistency between the posed start line
and the free-jet cell, in THIS world (the certified plug worlds put
the start line inside a fan with a much shorter domain). NEXT: dump
pt1/pt3 and the solved (x4,y4,th4) of the first edge cell; suspect
the start line's top row being posed exactly AT the jet boundary.

CONSEQUENCES FOR THE ANSWER (stated, not hidden):
- bell vs plug differ by 0.28%, which is BELOW the 1.5% error floor
  => NOT RESOLVED. No claim may be made about which is better here.
- swirl costs 4.0% (C_F 1.4654 -> 1.4071), ABOVE the floor => real.
- J(l) is MONOTONE at a single design point: wall pressure never
  reaches p_a inside the domain, so the "truncation optimum" is the
  domain end, not an interior maximum. That is the ideal-adaptation
  result: at ONE operating point truncation only costs thrust, and
  you truncate for weight. The interior optimum measured in the
  truncated-plug-under-cycle chapter is a CYCLE effect, not a
  single-point one. Worth stating in the doc.
- M_i is NOT free (new C-0 check): at M_i = 1.2 the tables fan turn
  is 54.5 deg, which puts the first fan ray at -111 deg (pointing
  UPSTREAM) — geometrically impossible. M_i = 2.0 gives rays -56.7
  to -20.9 deg. The first run of this carrier was invalid for that
  reason and the check now catches it.
Cache: validation/_config_cmp/.

---------------------------------------------------------------------
UPDATE 24 (2026-08-08): STEP 13 DEFECT DIAGNOSED, FIX DIRECTION
VALIDATED, NOT YET CLOSED.

MECHANISM (established, not conjectured). A march COLUMN is a
characteristic; the start line posed in a1_config_compare is a
VERTICAL cut. The free edge must therefore bridge from vertical to
characteristic geometry in ONE chord — measured on this world: the
edge advances 2.35 m in a single step (row 42 of column 2 lands at
x = 2.695 while the start line's edge is at x = 0.350), closed by one
midpoint-angle chord. Mass jumps +1.454% in that one column and is
then flat (+1.464% at the last column, 120 columns later). Column-by-
column dump is in the session log.

FIX DIRECTION, MEASURED: pose the start data ON A CHARACTERISTIC so
the first column is geometrically like every other one. Tested by
tracing a C+ through the analytic fan and posing on it:
  mass closure 1.47e-2 -> 7.5e-4 (N=41) and 4.8e-4 (N=81)
i.e. a 25x improvement AND it now CONVERGES with resolution, which
the vertical-start version did not (1.47/1.38/1.37% over three
resolutions).

WHY IT IS NOT YET CLOSED: a C+ launched from the spike at x0 exits
the analytic fan's validity region before it reaches the free edge.
Checked geometrically: the fan's last ray reaches y = 2.0 at
x = 0.71, while the C+ from (0.35, 1.52) needs x ~ 1.6 to climb
there. So the analytic fan CANNOT supply data on that characteristic,
and the char-start test above carries wrong data above the fan (its
mass level is 4.02e4 vs the true 4.25e4 — 5% off — precisely because
of that).

THE ACTUAL FIX (specified, not built): a TWO-STAGE start. March the
fan region itself with the certified cells from a short vertical cut
very close to the lip (where the fan IS valid across a thin strip),
then hand the resulting characteristic column to the main march as
its start data. Plumbing for this is DONE: plug_march now accepts
x0 as a scalar (historical, vertical) or an ARRAY of per-row
stations. Additive; oracle re-runs 6/6 PASS and axi 5/5 PASS.

CAUTION FOR WHOEVER PICKS THIS UP: a mass-through-vertical-cuts
probe of the marched field gave +1.7/+3.3/+4.9/+5.2/+2.0% at
x = 0.5..2.4. Do NOT treat those as measurements of the field: the
scattered-mesh interpolation drops 2-7% of the sample points near
the boundaries and the trapezoid then runs over a gappy grid. The
trustworthy meters remain start-line-vs-last-column (both proper
control surfaces) and the momentum closure.

ALSO NOTE: the certified axi stage has the SAME first-edge-step
magnitude (jet height / tan(mu) ~ 2.4 m) and closes at 0.47%, so
step size alone does not explain the 1.5%; the config world differs
in marching 2.4 characteristic-crossings of domain versus ~0.8.
That comparison is the next thing to settle.

---------------------------------------------------------------------
UPDATE 25 (2026-08-08): THE STEP-13 DEFECT ISOLATED TO ONE VARIABLE —
AND IT EXPOSES A CERTIFICATION GAP.

Update 24's "vertical-vs-characteristic start line" story is SUPERSEDED
as the root cause (the first-column jump is real, but it is a symptom).
A controlled world-bisection settles it.

BISECTION (certified axi world -> config world, one change at a time,
mass closure of the march):
  certified axi (reference)            -3.4e-3
  + Mach range 2.0->2.8                -4.7e-3
  + thin annulus (y_sp 1.5)            +9.6e-4
  + long domain (x_end 6)              +6.8e-4
  + more rows (N=41)                   -1.6e-3
  + config lip/spike radii             -1.8e-3
=> NONE of geometry, Mach range, domain length, annulus height or
resolution explains the 1.5%. All close at 0.1-0.5%.

THE ONE VARIABLE THAT DOES (same geometry, only the sign of the fan
turn changed):
  wall RISES  (theta_i = 0, flow turns outward)   K=80/N=41  -2.3e-3
                                                  K=160/N=81 -2.5e-3
  spike DESCENDS (theta_i = -dnu, true plug)      K=80/N=41  +2.1e-2
                                                  K=160/N=81 +1.7e-2
=> 9x worse, and it barely converges under refinement.

THE CERTIFICATION GAP: EVERY certified plug world in this program has
a RISING wall — the plug oracle, the axi stage, and the bisection
reference all pose theta_i = 0 with the flow turning outward, so the
"spike" rises. A real plug turns the flow INWARD and the spike
DESCENDS toward the axis. The descending configuration was never
mass-checked: the plug-march suite's mass checks (P-3, A-2) run on
rising worlds, and the plug-cycle suite (step 10), which DOES use a
descending spike, has no mass check at all — its checks are Lemma-A
collapse, nesting order, votes and the corner condition. Step 13's
mass meter is the first time a descending spike was weighed.

MECHANISM: still open. RULED OUT: row depletion — row counts per
column are similar in both cases (41 -> ~30 -> 72 rising, 41 -> ~30 ->
79 descending), so the wall is not eating the mesh. LEADING CANDIDATE:
the descending spike drives the flow toward the axis (y_wall 1.695 ->
0.863) where the axisymmetric source ~ 1/y is strongest, while the
rising wall moves away from it (1.695 -> 3.521). Source strength
roughly doubles vs halves. That is a factor 2 against a factor 9, so
it may not be the whole story.

CONSEQUENCE FOR STEP 10 (truncated plug under cycle): its marches use
a descending spike, so they carry this error too. Its published
results are RATIOS and ORDERINGS between phases marched on the SAME
hardware (nesting order, anti-collapse, vote balance), which a common
multiplicative bias does not overturn — but that argument should be
made explicitly, not assumed, and a mass check should be added to
that suite.

NEXT: add a mass check to the plug-cycle suite; then attack the
descending-spike accuracy (candidates: station clustering where y is
small, or a source-term treatment near small y). plug_march's per-row
start-station support (Update 24) stays — it is useful plumbing and
both suites re-PASS with it (oracle 6/6, axi 5/5).

---------------------------------------------------------------------
UPDATE 26 (2026-08-08): THE STEP-13 DEFECT IS A CONSISTENCY ERROR IN
THE AXISYMMETRIC SOURCE, NOT A RESOLUTION ERROR. Fully characterized.

TURN SWEEP (fixed geometry, M2=2.8, x_end=6, K=80, N=41; mass closure)
  turn[deg]   RISING        DESCENDING
    3.06      +3.5e-4       +1.5e-3
    9.43      +7.3e-4       +5.1e-3
   16.12      +3.7e-4       +9.9e-3
   26.66      -2.3e-3       +2.06e-2
Rising is FLAT in turn; descending grows ~linearly with it.

DECOUPLING turn magnitude from axis proximity (all descending, turn
26.66 deg, same annulus height 0.575):
  baseline      lip 2.2695  spike 1.695   err +2.06e-2  y_end  0.863
  far from axis lip 10.00   spike 9.430   err +3.2e-3   y_end  8.604
  very far      lip 40.00   spike 39.43   err +1.1e-3   y_end 38.604
  similarity x4 lip 9.078   spike 6.780   err +2.063e-2 y_end  3.451
  PLANAR d=0    lip 2.2695  spike 1.695   err +3.3e-4   y_end  0.863
=> The SOURCE is the error: kill it (planar) and the error drops 63x;
weaken it (far from the axis, source ~ 1/y) and it drops 20x. The
similarity-x4 control reproduces the baseline to FOUR DIGITS, so the
scheme is correctly scale-invariant — this is not a length-scale bug.

IT DOES NOT CONVERGE (this is the key point):
  uniform K,N doubled     2.06e-2 -> 1.70e-2   (ratio 1.21, order 0.28)
  rows only  N 41/81/161  2.063e-2 / 2.016e-2 / 2.004e-2  (FLAT)
  stations clustered where y is small (dx ~ y): WORSE, 2.43e-2
=> Refining rows does nothing at all; refining stations barely helps;
source-aware clustering makes it worse. That is the signature of a
CONSISTENCY error, not a discretization error. Refinement will not
fix it and neither will re-gridding.

SCOPE: interior cells are shared with the certified (rising) worlds
and those close at 1e-3, so the defect is most likely in a BOUNDARY
cell's source treatment under inward-turning flow (v < 0) with y
decreasing — wallbot (the descending spike) is the prime suspect, the
free-jet edge second.

NEXT TEST (specified): build an EXACT axisymmetric oracle with v < 0.
Converging radial source flow (flow along rays toward a point, q=q(r))
is an exact solution of the axisymmetric equations and puts v < 0 with
y decreasing — precisely the untested regime. March it and compare
against the closed form. That localizes the defect to a cell instead
of another parameter sweep. Do NOT run more world sweeps: the
parameter space is exhausted, the answer is in a unit test.

STANDING CAVEAT unchanged: step 10 (truncated plug under cycle) marches
descending spikes and therefore carries this error; its results are
ratios/orderings across phases on identical hardware, which a common
bias does not overturn, but that argument must be written down and the
suite needs a mass check.

---------------------------------------------------------------------
UPDATE 27 (2026-08-08): OWNER DIRECTIVE — theta_i BECOMES A DESIGN
VARIABLE; RDE INPUT POSED AS A STRAIGHT LINE.

Directive (standing, from now on):
 1. the initial turning angle theta_i is PART OF THE OPTIMIZATION,
    not a posed constant — it is the angle at which the RDE delivers
    the flow (the inclination of the annular chamber-exit slot);
 2. the RDE INPUT is given as a STRAIGHT LINE — the inlet is a
    straight segment in the meridional plane between the spike start
    radius and the cowl lip, not a curved surface;
 3. outward-turning aerospikes are excluded: they cannot beat
    inward-turning ones.

(3) QUANTIFIED (the owner is right by a wide margin): an outward
plug leaves its ENTIRE exhaust at theta_E = +dnu, so thrust collects
only cos(theta_E):
    dnu  9.43 deg -> 1.35% of momentum lost
    dnu 16.12 deg -> 3.93%
    dnu 26.66 deg -> 10.63%
against 0.00% for an inward design with theta_E ~ 0. For scale, the
whole bell-vs-plug gap in step 13 is 0.28%, the swirl penalty 4.0%,
a 15-deg cone's divergence 1.70%. Outward turning was never a
candidate design — it was a test fixture, which is exactly why every
certified axisymmetric suite happens to sit in it.

CONSEQUENCE — THE DEFECT IS NOW BLOCKING, NOT INCIDENTAL. The new
design space (theta_i free, spanning inward turning) lies ENTIRELY
inside the regime carrying the ~2% consistency-level mass non-closure
(Update 26). Optimizing theta_i on those numbers would be optimizing
on contaminated data. Order of work is therefore FORCED: build the
converging-radial-source oracle (exact axisymmetric solution with
v < 0), localize and fix the cell defect, THEN open theta_i.

BUILT-IN ORACLE FOR THE NEW VARIABLE: the divergence argument
predicts the theta_i optimum near theta_E ~ 0, i.e. theta_i ~ -dnu.
A blind optimization landing there is a known-answer check. Exact
coincidence is NOT expected: truncation length and the wall-pressure
distribution trade against pure divergence, so a small offset is
physical and must be explained, not tuned away.

IMPLEMENTATION NOTES for when it opens:
 - a1_config_compare currently PINS th_i = -dnu (line ~175) to force
   theta_E = 0. That pin becomes the initial guess, not the value.
 - the inlet straight line = the segment from (0, y_sp0) to the lip
   (0, R_MAX); the flow crosses it at (M_i, theta_i). The lip fan
   stays constructed analytically (it is singular) and the march
   still starts at x0 > 0 — theta_i is a property of the INPUT line,
   not of the march start.
 - the annulus sizing (mass match) must be redone at each theta_i,
   since the axial mass flux through the inlet scales with
   cos(theta_i).
 - C-0 (fan geometry valid: every ray downstream) must be evaluated
   per candidate theta_i — it already caught the M_i = 1.2 posing.

---------------------------------------------------------------------
UPDATE 28 (2026-08-08): STEP 14 — THE RADIAL-FLOW ORACLE, 6/6 PASS.
THE DEFECT IS LOCALIZED TO THE FREE-JET EDGE CELL.

CARRIER: validation/a1_source_flow_oracle.py. Exact axisymmetric
solution: spherical radial flow, rho(q) q r^2 = const with the
program's own tables. Putting the singular point UPSTREAM gives a
diverging flow (v > 0, the certified regime); putting it DOWNSTREAM
gives a converging flow (v < 0, the untested regime) — one formula,
so the two cases differ in nothing but the sign the equations see.
Streamlines are rays, so a cone is an EXACT wall and the
prescribed-wall cell is exercised against a closed form.

THE DESIGN POINT: the free edge is EXCLUDED BY CONSTRUCTION. Only
mesh points below a rigorous dependence bound are compared — a
straight line from (X0, Y_TOP) at the steepest C- slope present in
the field (min tan(theta-mu)), which no influence from above can
outrun. S-0 verifies the bound clears the wall (margin +0.053 m).
So the comparison depends on INTERIOR and WALL cells only.

RESULT (median error vs the closed form, fine grid):
                        converging(v<0)  diverging(v>0)   ratio
   wall pressure           7.91e-4         5.18e-4        1.5x
   interior |dq|/q         3.43e-4         1.84e-4        1.9x
   interior |dtheta|       5.08e-4         2.9e-4         ~1.8x
=> The interior and prescribed-wall cells are CLEAN for v < 0. They
do NOT degrade by the 9x seen in the plug worlds; both regimes sit at
the 1e-4..1e-3 level.

CONCLUSION: the inward-turning defect is NOT in the interior cells and
NOT in the prescribed-wall cell. By elimination it is in the FREE-JET
EDGE cell — the only piece this test excludes. That is consistent with
the step-13 column dump, where the mass jump coincided exactly with
the free edge leaping 2.35 m in a single chord.

TWO HARNESS LESSONS WORTH KEEPING:
 1. The obvious rejector is VOID here: in radial flow EVERY cone is an
    exact streamline, so perturbing the cone angle just produces a
    different exact solution and cannot reject. The valid rejector
    CURVES the wall off the ray (breaking the ray property): 1%
    curvature -> wall error 1.51e-2 vs 5.18e-4 clean, a 29x
    separation. Fires as designed.
 2. Tracing the dependence boundary by integrating a C- was fragile
    and gave inconsistent regions between the two cases. The straight
    conservative bound at the field's steepest C- slope is rigorous,
    trivial, and case-independent — use that pattern again.

NEXT: attack the free-jet edge cell. Its certified unit tests
(a1_freejet_unit, 6/6) are CELL-level on exact data; what they do not
cover is the cell embedded in a long march where the edge chord grows
to metres. Suspects, in order: (i) the streamline condition closed by
one midpoint-angle chord over a very long segment; (ii) the row-growth
bookkeeping leaving an uncovered wedge between the topmost interior
and the edge (measured in step 13: a 0.51 m gap with no mesh points);
(iii) the edge's own source treatment. A targeted test: march a case
whose free boundary has a KNOWN shape and compare — e.g. a uniform
parallel jet at p_a (edge must stay straight, and the swirl suite's
W-2 already shows the machinery preserves that to 1e-15 for a RISING
duct; run the same with the jet converging).

---------------------------------------------------------------------
UPDATE 29 (2026-08-09): CORRECTION — THE DEFECT IS IN THE MASS METER,
NOT IN THE FLOW. Updates 26 and 28 are SUPERSEDED.

Update 26 called it "a consistency error in the axisymmetric source".
Update 28 localized it "by elimination to the free-jet edge cell".
Both are wrong. The evidence:

 1. FREE EDGE EXONERATED. The mass flux THROUGH the marched free edge
    — which must vanish, the edge being a streamline — is 4.06e-11,
    i.e. machine zero, on the very world that shows a 1.47% imbalance.
    Segment by segment the largest edge leak is 1e-11. The edge cell
    maintains its streamline condition perfectly.
 2. WALL NEARLY EXONERATED. Flux through the wall polyline: -6.8 kg/s,
    0.016% of the through-flow.
 3. INTERIOR + WALL CELLS EXONERATED against an EXACT solution (step
    14): median error 3e-4 in BOTH v>0 and v<0, no degradation.
 => No boundary leaks and no field defect. Yet mass in vs mass out
    differ by 1.47%. The imbalance is therefore in the MEASUREMENT.

THE MEASUREMENT IS THE PROBLEM. The mass meter integrates over the
LAST COLUMN, which is a characteristic, not a vertical plane, and its
segment lengths are wildly uneven because of the structural wedge
between the topmost interior point and the free edge:
      RISING     max segment 0.0976 m, mean 0.0319, ratio  3.1x -> err 2.3e-3
      DESCENDING max segment 0.8439 m, mean 0.0640, ratio 13.2x -> err 2.1e-2
The trapezoid error over a segment goes like (ds)^2 * curvature of
rho*u*2*pi*y, so a segment 8.6x longer contributes ~74x more error.
That quantitatively explains BOTH the 9x rising-vs-descending gap and
the non-convergence: refinement does not remove the wedge, so the
longest segment — and its quadrature error — persists.

WHAT THIS MEANS FOR STEP 13 (important). The THRUST numbers do NOT
use the jagged column. J = F_in + integral of (p_w - p_a) along the
WALL: both the start line and the wall polyline are well resolved
(mean segment 0.06 m, no wedge). The checks that failed were exactly
the ones whose instrument is the last column (C-4, the momentum
closure); C-1, on the start line, PASSED. So the +-1.5% error bar I
attached to the bell-vs-plug comparison was a property of the METER,
not of the thrust, and it was wrong. A defensible thrust error bar
is the pointwise field accuracy measured in step 14, of order 1e-3
relative — which would make the 0.28% bell-vs-plug gap marginal but
close to resolvable, instead of hopeless.

DO NOT re-report the step-13 table until the meter is fixed and the
thrust has its own derived error bar. The figure fig_config_compare
currently shades a +-1.5% band that is now known to be the wrong
quantity.

FIX FOR THE METER (next): measure conservation on a control surface
that is not jagged. Options, in order of preference:
  (a) a VERTICAL cut through the marched field, densely sampled by
      2-D interpolation of the mesh (an earlier attempt failed only
      because the scattered-hull interpolation dropped 2-7% of points
      near the boundaries and the trapezoid then ran over a gappy
      grid — mask and clip properly);
  (b) subdivide the column's long segments using neighbouring mesh
      points (NOT linear interpolation along the segment, which
      reproduces the same trapezoid value);
  (c) integrate along the column with a higher-order rule fitted to
      the actual point spacing.
Then re-derive the step-13 bands and re-run.

METHOD LESSON WORTH KEEPING: a conservation meter is only as good as
the surface it integrates over. This one was trusted for four
sessions because it is "just" a flux integral; it was in fact the
least accurate object in the pipeline. Any future conservation check
must report the geometry of its own control surface (max/mean
segment) alongside the number.

---------------------------------------------------------------------
UPDATE 30 (2026-08-09): THE METER IS FIXED AND VALIDATED — AND IT
PARTLY REVERSES UPDATE 29. There IS a real ~2% mass excess for
inward turning; the meter explains the non-convergence, not the whole
number.

NEW MODULE: validation/a1_flux_meter.py. Fluxes through a VERTICAL
cut, sampled densely and uniformly in y between wall and edge, with
the two end strips (where a scattered interpolation has no support)
filled from the states known exactly there. Every result reports its
own surface (sample count, end-fill fraction) — the discipline this
whole episode produced.

METER VALIDATED on the uniform annular duct, where the mass is known
in closed form:
    exact                4.73782283e+04
    new meter, 3 cuts    identical to 6.7e-16, end-fill 0.0%
So the instrument is sound wherever the mesh covers the cut.

WHAT IT SAYS ON THE PLUG WORLDS (well-covered cuts only):
    RISING     (outward)  x=3,4,5 -> +0.03%, -0.12%, -0.22%
    DESCENDING (inward)   x=3,4,5 -> +1.62%, +1.81%, +2.29%
=> The inward-turning excess SURVIVES a validated meter. Update 29's
claim that the whole 1.5-2% was a measurement artifact is WRONG. The
correct statement is narrower:
  * the OLD meter is genuinely unreliable on a jagged control surface,
    and that explains the NON-CONVERGENCE and part of the 9x
    rising-vs-descending ratio (segment spread 3.1x vs 13.2x);
  * but a real ~2% mass excess remains for inward turning.

WHERE IT IS NOT: free edge (streamline flux 4e-11, machine zero);
wall (0.016%); interior and wall cells against an exact axisymmetric
solution (3e-4, both regimes, step 14).

LEADING SUSPECT NOW: MESH COVERAGE. The new meter reports the fraction
of each cut it had to fill because no mesh point supports it:
    RISING     at x=1.0 -> 34.5% of the cut unfilled by the mesh
    DESCENDING at x=1..5 -> up to 4.3%
i.e. in the start-up region the marched mesh does not span the
wall-to-edge gap at all. That is the same structural wedge seen in
the step-13 column dump (a 0.51 m stretch with no mesh points between
the topmost interior and the edge). A region no cell computes cannot
conserve anything, and the edge is placed from the topmost interior
across that hole.

NEXT (concrete): measure the coverage hole directly — for each column,
the gap between the topmost interior point and the edge point — and
test whether closing it (inserting rows at the edge faster than one
per column, i.e. a row-insertion rule driven by the gap rather than a
fixed +1) removes the 2%. That is a bookkeeping change to the driver,
not a cell change, which is consistent with every cell having now been
individually exonerated against exact solutions.

STATUS OF THE STEP-13 CONCLUSION, restated once more, carefully:
the thrust integral uses the start line and the WALL polyline, neither
of which is jagged and both of which are well covered; the 2% mass
excess is measured on cuts, not on those surfaces. So the thrust
numbers are probably better than 2% but they still have NO derived
error bar. Do not re-report the table until one exists.

---------------------------------------------------------------------
UPDATE 31 (2026-08-09): THE STEP-13 COMPARISON IS RESOLVED. The block
was never the flow — it was using the wrong error estimate.

1. THE START-UP WEDGE IS CONFIRMED AND QUANTIFIED. Per-column gap
   between the topmost interior point and the free edge:
        RISING     col 2: 0.99 m = 26x the mean row spacing
        DESCENDING col 2: 1.31 m = 39x
        every other column: 0.5-1.0x
   ONLY the first marched column has a hole, exactly where the mass
   jumps (+1.454%, flat for the following 120 columns). Cause as in
   Update 24: a column is a characteristic, a vertical start line is
   not, so the first column alone must bridge the two geometries.

2. FILLING IT (new plug_march(edge_fill=n), additive; oracle 6/6 and
   axi 5/5 still PASS) does NOT remove the offset but COLLAPSES THE
   CUT-TO-CUT SPREAD:
        RISING      spread 0.253% -> 0.015%
        DESCENDING  spread 0.653% -> 0.015%   (40x better)
   i.e. the hole was making the meter disagree with itself. The
   remaining offset (+0.5% rising, +2.0% descending) is a genuine,
   reproducible non-conservation of the scheme — MoC is not a
   conservative method, so this is a truncation statement, not a bug.
   NOTE: edge_fill inserts INTERPOLATED points, which are not
   solutions; keep it as a DIAGNOSTIC, do not adopt as default. A
   principled version would compute those rows with cells.

3. THE ACTUAL ANSWER, obtained by doing the obvious thing — Richardson
   on the THRUST itself instead of inferring it from mass:
        K,N =  61/41   J = 1.161610e8
        K,N = 121/81   J = 1.161481e8
        K,N = 181/121  J = 1.161454e8
        successive differences 1.287e4 then 2.737e3, ratio 4.70
        => SECOND ORDER confirmed; DERIVED band = 1.09e4 N = 0.0094%
   bell J 1.164737e8, plug J 1.161454e8, gap 3.283e5 N = 0.282% of
   the bell = 30x the derived band.
   => RESOLVED: at this operating point the BELL produces 0.282% more
   thrust than the plug, and the plug matches it in half the length.

   The +-1.5% error bar reported earlier was a property of a mass
   meter integrating over a jagged surface and was never a property of
   the thrust. fig_config_compare has been corrected to the derived
   band and its caption/title updated.

METHOD LESSON (the real one): when a quantity of interest has a
derived band available directly, derive it directly. Four sessions
were spent inferring the thrust's uncertainty from a conservation
meter that measured something else. The program's own rule — run the
same computation at two resolutions and let it measure its own error —
answers it in one run.

STILL OPEN (unchanged): the ~2% inward-turning non-conservation is
real and uncharacterized as to source; it does not contaminate the
thrust (which converges cleanly at second order) but it should be
understood before conservation is used as an acceptance instrument on
descending spikes. Also still open: the plug-cycle suite has no mass
check, and step 12/13/14 are not yet in the document.

---------------------------------------------------------------------
UPDATE 32 (2026-08-09): STEP 15 — THE INLET ANGLE OPENED AS A DESIGN
VARIABLE (owner directive). DOC BROUGHT UP TO DATE: 72 pp.

CARRIER: validation/a1_inlet_angle_opt.py. theta_i is now a design
variable; the RDE input is a STRAIGHT annular inlet between the spike
start radius and the cowl lip, and its inclination is what is
optimized. Since the lip fan turn dnu is fixed by the expansion
(M_i -> p_a) and does not depend on theta_i, the exhaust angle is
simply theta_E = theta_i + dnu, and the sweep is reported in theta_E.
Basis = step 13's, with one addition: the axial mass flux through an
inclined inlet scales with cos(theta_i), so the annulus is RE-SIZED at
every candidate to hold the reference mass flow; thrust is compared at
a FIXED length so length is not silently traded against angle.

RESULT — THE ORACLE IS RECOVERED, NOT IMPOSED. The blind sweep lands
at theta_E = 0.0 deg, exactly the divergence prediction, C_F 1.45976
(theta_i = -26.66 deg). Measured penalty vs the cos(theta_E) model:
   thE   measured    model
   -6    -0.365%    -0.548%
   -4    -0.153%    -0.244%
   -2    -0.031%    -0.061%
    0     best        ---
   +2    -0.068%    -0.061%
   +4    -0.224%    -0.244%
   +8    -0.799%    -0.973%
  +12    -1.753%    -2.185%
Two readings: (i) the measured penalty is consistently SMALLER than
pure divergence, because the wall-pressure distribution partially
compensates — the trade the closed-form model does not contain;
(ii) the curve is ASYMMETRIC — turning inward past the optimum costs
less than turning outward by the same angle, which is the
quantitative form of the owner's premise that outward-turning
aerospikes are not competitive.
WINDOW BOUNDED BY GEOMETRY, NOT PREFERENCE: at theta_E = -8 deg the
spike descends to y = 0.32 m and the march loses certification
(worst residual 1.4e10) as the flow runs into the axis. That case is
excluded by the T-0 geometric test and reported, not hidden.

DOC (docs/rde_nozzle_A1_brick2_thrust.pdf, 65 -> 72 pp):
 - NEW ch. 14 "Comparing configurations, and the inlet angle":
   the common basis and why comparability is the whole problem; the
   corrected results table with the DERIVED thrust band (bell wins
   0.282% = 30x band); the thermodynamic-ceiling section explaining
   why all matched nozzles converge; the outward-vs-inward
   certification gap; the radial-flow oracle (step 14, 6/6); the
   "instrument, not the flow" section with the method lesson; and the
   inlet-angle sweep.
 - fig_config_compare (band corrected), fig_turn_direction and
   fig_rao_construction all now wired in (fig_rao_construction into
   ch. 8, the referee chapter, where the construction is explained).
 - status table + reproduction list updated with steps 14 and 15.

REMAINING (unchanged): the ~2% inward-turning non-conservation is real
and uncharacterized as to source (it does NOT touch the thrust, which
converges at second order); the plug-cycle suite still has no mass
check; the spline/TR-SQP free-form driver is still the one piece of
the ORIGINAL brick-2 goal not built.
