# S41 — The two-wall DESIGN posing, step 1: the initial arc decided by the optimiser (2026-09-25/26, [F3/A1])

Owner's direction (2026-09-25, after the Migdal confirmation of S40): "andiamo con la tua proposta"
-- 1) the initial arc as a design variable with the ends still pinned; 2) the objective at the
operating ambient with the constraints; 3) the free jet after the lip; 4) the truncation. Two
precisions: the LENGTH constraint will probably be ONE cap for plug and shroud, each free to end
where it wants under it; for the truncation, a base-pressure CONVENTION applied identically to every
profile, so that profiles compare on equal footing even if the absolute base pressure is wrong --
and a documented physical model (Chapman-Korst) is admissible ("la fisica non e' mai rigettata se
documentata"); Fiore 2019 sec. 6.1 gives the regime criterion (where the lip's last wave lands
against the reattachment E and the sonic point S). This log is step 1. F3 stays closed; no session
counter. Session mose-a1, main tree `rde-nozzle-program`. Communication in Italian; log in English.

## 1. The arc posing (carrier `validation/a1_twowall.py`, `TWOP_KERNEL=arc`, artifacts `_twowall_arc/`)
Each wall's initial stretch is a circular arc tangent to the axial inlet whose END abscissa x_a and
end slope t_a = |tan theta_a| are design variables (radius R = (x_a - x_0) sqrt(1 + t_a^2) / t_a);
downstream, the spline of the kernel posing clamped to the arc's end, its 12 knots at FIXED
FRACTIONS of [x_a, end] (they move with the arc's end); the lip and the tip pinned at Migdal's; the
vacuum C_F. Design vector 11 + 11 knot heights + (x_a, t_a) per wall = 26. The reference = Migdal's
arcs (GENO's arc ends 0.0729 / 0.0646 m, end angles 21.4 / 18.9 deg: R 0.2000 / 0.2000 m). The
owner's argument, which this posing tests: circular arcs with the ends pinned leave few degrees of
freedom, so the thrust should pick the best arc (the free-KERNEL family of S40 was the family of
ALL initial stretches, not of circular arcs).
- Stage class (`run_class_2026-09-25.log`, 3/3): the reference in class (worst cell +0.0113 = GENO's
  exact walls, 0 folded), KS brackets the minimum, the unconstrained first move (0.33 mm along
  +grad J) infeasible (KS -0.042). The gradient at Migdal's arcs is NOT zero in the arc ends:
  dC_F/dx_a = +0.021 (plug), -0.016 (shroud) per metre; the thrust prefers a different arc pair.
- The generic start R: each arc's radius x 1.5 (0.30 m) at the reference's end angles, the
  downstream wall the cubic Hermite from the arc's end to the pinned end (axial exit). In full it
  folds (493 cells, KS -0.10); the walk takes the largest in-class ramp toward it: 0.5 (R ~0.25 m,
  7.8 / 5.9 mm off the reference, C_F 2.2e-4 below).

## 2. DUTY-11 on the arc posing, and the identifiability floor corrected
First derive (`run_derive_2026-09-25.log`, 6/6, the S40 criterion): the two softest directions are
almost purely the two arc END SLOPES (t_a of the plug, curvature 0.032; t_a of the shroud, 0.19),
called "near-null" against the GLOBAL floor K_RICH x the Hessian's asymmetry = 1.23 -- yet G-5a
verifies those curvatures by J's own second difference to 8.5e-4 and 1.4e-3: they are measured,
not noise; the global floor was far too crude for a design that mixes knot heights, arc ends and end
slopes. CORRECTED (S41): identifiability PER DIRECTION -- each eigenvalue against K_RICH x its own
verified error (G-5a) plus the rounding floor; the shape band quoted in design units AND as the wall
displacement it makes; the global floor stays a reading. Both derives re-run with the corrected
criterion (arc and kernel posings, 2026-09-26; the kernel posing's "1 near-null" of S40 is expected
to become identifiable: its curvature 0.80 was verified to 2.1e-4). RE-RUN (2026-09-26, both
6/6): ARC posing (`_twowall_arc/run_derive_2026-09-26.log`) 26 of 26 directions identifiable at
their own verified floors (the global floor would have called 3 near-null), condition 4.6e3; the two
softest directions are the arcs' end slopes -- the plug's resolved to 0.175 deg of end angle
(curvature 0.032, floor 3.4e-3), the shroud's to 0.06 deg (0.19, floor 5.6e-3) -- and the widest
shape band is 2.35e-4 m of wall; the Newton step from Migdal's arcs in the identifiable subspace is
2.1 cm (arc ends) for a predicted gain 5.6e-5 of C_F (430 x delta), the gradient's share outside
the identifiable subspace zero. KERNEL posing (`_twowall/run_derive_kernel_2026-09-26.log`) 22 of
22 identifiable (the S40 "1 near-null" was the global floor's artefact), widest band 7.3e-5 m of
wall -- the [X-TWOP] statement is corrected in this session's registry edit. So: circular arcs with
the ends pinned are IDENTIFIED by the thrust (the owner's argument holds at the level of the
curvature); whether the thrust's preferred arc is Migdal's is the walks' question.

## 3. The walks, and the cause of the lost walks isolated
Three walks of the arc posing were lost to "LLVM compilation error: Cannot allocate memory" (the
failure that took the Euclidean walk H of S40 at 04:04): A at segment 4 (16:26, its base already at
C_F 1.579918, +3.8e-5 over Migdal's arcs, in class), R at segment 1 (16:05), and R again at 01:01
after the first mitigation (MALLOC_ARENA_MAX=2). CAUSE ISOLATED (2026-09-26 01:02, measured on the
live processes): the walk process had 32742 memory mappings after two segments against the kernel's
per-process cap of 65530 (vm.max_map_count), the derive processes 5200-5800; a walk accumulates
COMPILED EXECUTABLES -- every march has its own cell count, every count is a new set of array shapes
in the vectorised margin, every shape a new compilation kept in jax's cache -- and dies at the cap.
Not a machine-wide memory event (the page cache was 90-100 GB, available ~100 GB throughout). Fix,
declared: the walk runs the driver one chunk of segments at a time (TWOP_CHUNK), writes a
checkpoint after every chunk (the landing, the Newton metric T, the radius) and CLEARS the
compilation caches (jax.clear_caches) between chunks, reporting the mapping count before and after;
TWOP_RESUME=1 restarts from the checkpoint with the metric read back (no second Hessian). The radius
restarts at tr0 each chunk (declared). Logs of the lost walks kept trimmed
(`run_walk_{A,R}N_oom_2026-09-25.log`, `run_walk_RN_oom2_2026-09-26.log`).
THE GAIN OVER MIGDAL'S ARCS UNDER GRID REFINEMENT, first reading (probe
`RDE/handoff/f3_2026-09-25/twop_refine_probe.py`, log `twop_refine_probe_ckptA.log`, on walk A's
checkpoint after 6 segments, C_F 1.579906467 at (140,31), in class): PAIRED on the same grid the
design beats Migdal's arcs by +2.61e-5 at (140,31) and by +1.22e-6 at (280,61) -- a ratio 0.05 on
one doubling. The preference for a different arc pair is the march's DISCRETISATION (the coarse grid
overshoots the 1-D ideal by +2.9e-4, the fine by +6.1e-5; both designs converge to the same fine
value within 1.2e-6), as the S30 foot-knot gain was; both designs are fold-free on both grids. THE LANDINGS (Newton metric, 12 x 8, backtracking, checkpointed; `run_walk_{A,R}N_2026-09-26.log`,
records `walk_{A,R}N_2026-09-26.json`; grade `run_grade_2026-09-26.log`):

| walk | start | C_F landing (140,31) | gap to Migdal's arcs | plug arc x_end / R / angle | shroud arc x_end / R / angle | |grad|inf | in class |
|---|---|---|---|---|---|---|---|
| Migdal (reference) | -- | 1.579880408 | 0 | 0.0729 / 0.2000 / 21.37 deg | 0.0646 / 0.2000 / 18.85 deg | -- | yes |
| A | Migdal's arcs | 1.579930741 | +5.0e-5 | 0.0761 / 0.2088 / 21.36 | 0.0633 / 0.1960 / 18.85 | 4.1e-3 | yes (KS +0.0118) |
| R | arcs R 0.30 (ramp 0.5: ~0.25) | 1.580100554 | +2.2e-4 | 0.0847 / 0.2313 / 21.47 | 0.0812 / 0.2511 / 18.86 | 1.4e-1 (budget out) | yes (KS +0.0144) |

On the coarse grid the two landings do NOT coincide (RE-1 FAIL: 1.7e-4 apart in C_F, the arcs
2.3 / 5.5 cm apart in radius) and R keeps climbing when its 12 segments end: the coarse-grid thrust
prefers larger arcs, and the more the arcs grow the more it gains. Whether that is physics or the
discretisation preference measured on A's checkpoint (ratio 0.05 on one doubling) is the paired
fine-grid check on both landings (`twop_refine_probe_landings.log`, the same designs re-marched at
(280,61), reference 1.579655122 there):

| design | paired gain at (140,31) | paired gain at (280,61) | ratio | fold census at (280,61) |
|---|---|---|---|---|
| A landing | +5.03e-5 | +1.78e-5 | 0.35 | 0 / 33632, min +0.0099 |
| R landing | +2.20e-4 | -1.65e-4 | -0.75 | 238 FOLDED / 33166, min -0.606 |

VERDICT OF STEP 1: on the (140,31) instrument the arc optimiser does not re-obtain Migdal's arcs,
and its departures are the instrument's, not the flow's -- A's gain falls by 2/3 on one doubling
(a residue +1.8e-5 not resolved at one rung), and R's design, in class on the coarse net, FOLDS on
the fine one (the coarse fold class missed a coalescence the finer net resolves) and is 1.6e-4 WORSE
than Migdal's arcs there. The coarse grid overshoots the 1-D ideal by 2.9e-4 and the fine by 6.1e-5:
the differences the arc question turns on (1e-5 .. 1e-4) sit inside the coarse grid's own error,
and the fold class must be judged where folds resolve. Migdal's arcs are NOT beaten at this
resolution; the owner's expectation ("la spinta indica il miglior raccordo") is TESTABLE only with
the finer instrument: a two-rung posing (the class and the paired value both read at (280,61), or
Richardson-paired on the ladder), which costs ~25 min per march at (280,61) against 30 s -- the
walk budget must be re-planned (the Newton metric's 52 gradient evaluations alone are ~24 h at
that rung). Findings row twowall:arc-design-coarse-instrument-unfit.

## 4. What is measured about the base-pressure convention (for step 4)
Fiore 2019 sec. 6.1 (after Nasuti & Onofri 2012): open wake when the lip's last expansion wave
lands on the separated region behind the base (the base feels p_a); closed wake when it lands
downstream of the sonic point S on the axis (the base is isolated; p_b set by the flow at the
corner); a weak transition band between the reattachment E and S; "there still is no clear
definition of the transition point". Sec. 6.2 lists the closed-wake correlations on the corner
state (mean, conical, cylindrical, Rocketdyne, Sapienza, Chutkey) -- the same family S30 measured
in disagreement by 2-3 x the truncation loss. For Migdal's shrouded plug the lip flow is M 3.11,
the Mach lines from the lip 18.8 deg, reaching the axis 3.5 m behind the lip: the closed wake is
the natural regime unless a strong over-expansion puts a steep shock at the lip (figure
`_twowall/figs/22_wake_regimes_schematic.png`, generator `RDE/handoff/f3_2026-09-25/
wake_schematic_fig.py`; the pocket, E, S and the shock angles are schematic). Convention proposed,
not yet posed: the regime by Fiore's criterion (with S approximated in an inviscid march, declared),
p_b = p_a in the open branch, ONE closed-wake closure for every profile (a correlation or the
Chapman-Korst balance, documented), and a ranking that flips between closures declared unresolved.

## 5. Budget
No F3 counter (the phase is closed; this is the design posing's step 1 on the owner's word). Runs:
class 4 min; derives 106 + 90 min (arc, kernel, the corrected criterion); walks A 92 + 19 min and
R 150 min after three lost walks (~3 h of machine time lost to the mapping cap); refinement probes
50 + 60 min. Nothing of the plug instance's campaign budget is touched.

## 6. Conformity
- Branch `rde-nozzle-program`, main tree; identity AlexFalco5; explicit pathspecs; GENO never
  added; push on the owner's standing word.
- R1: `[F3/A1][S41]`. R3: this log; PROGRESS residual block (the S40 line extended with step 1's
  verdict) + archive; D6 note; the handoff section 9. R4: M0 LINE ADDENDUM S41 (two items).
- R5 / SR-2: X-TWOP's statement corrected (per-direction identifiability, 22 of 22; the arc posing
  as a reading with its verdict), pass 2026-09-26 = the kernel derive re-run today; findings:
  twowall:arc-design-coarse-instrument-unfit minted, twowall:design-posing-open updated (step 1
  taken, its lesson), numerics row unchanged. SR-1: the index row.
- Code: `a1_plug_spline_opt.run_trsqp` gains the additive `on_segment` callback (default None,
  bit-identical); `a1_twowall.py` gains the arc posing (TWOP_KERNEL=arc), the per-direction
  identifiability, the Newton metric's checkpoint/resume with cache clearing, the arc readout in the
  grade. Records: `_twowall_arc/` (class, derive, walks, grade), `_twowall/derive_2026-09-26.json`
  + log (the kernel derive re-run), the probes in RDE/handoff/f3_2026-09-25/.
- Measured on the tree of the commit (2026-09-26 ~05:50): numeric lint PASS (128 files, 0 ratchet
  violations); claims lint PASS (0 violations; X-TWOP fresh, pass 2026-09-26 >= last commit of its
  doc); advisory index PASS (133 rows); findings lint 0 violations on its rows (259 entries, 213
  open; the H4 channel and families e+f red at HEAD as before); FULL suite 16/23 = the seven
  environmental reds, 117 s; data/phase_diagram.*, data/q_mapping.* and figs/phase_diagram_op11.png
  restored with git checkout before the commit. One commit: the registry rows edited here cite the
  S40 log as their doc (unchanged), so the ordering rule does not apply.
