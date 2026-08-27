# HANDOFF — [F3/A1] S26 (2026-08-27)

**READ THIS FIRST when resuming the nozzle optimizer.** Supersedes the
S24 handoff (`HANDOFF_2026-08-11_S24_general_inlet.md`, which stays
authoritative for the S21-S24 narrative and GENO). Narrative:
`PROGRESS_2026-08-27_S26_rao_modo1.md`.

## 1. State

- Branch `brick2-plug` = `origin/rde-nozzle-program` 6be51b9 (S-PRES
  session 2) + the brick-2 line + this session's commits. Push is
  read-only; upstream keeps moving (S-PRES session 3 in flight, then F2
  block 0): expect another rebase — recipe in memory
  `project_rde_design_rebase_gotchas` (per-entry registry resolver,
  park the ignored .npz, `--committer-date-is-author-date`).
- W-5 CLOSED (3e98c72). Adjoint through the stratified march CERTIFIED
  ([X-O31R] 6/6).
- F3 ENTRY, Rao 1961 leg: tables oracle PASS, control-surface
  reconstruction PASS, objective identity PASS, **dual-code twin PASS
  6/6 on GENO's legacy p_b=0 field** ([X-RAOTW]). Two constructions
  falsified and registered as such: the planar-fan ideal spike
  ([X-RAOIS]) and the planar start line on a wide cut ([X-RAOWD]).
- **PLUG-SECTOR O3.3 PASS 7/7 at two cuts ([X-RAOO3], same day):**
  Rao's optimum is stationary for our functional under our march;
  the tip-moving gradient equals Rao's base-term counterweight
  2 pi y_D p_a to 0.5 percent; Eq. (9) closes at D. First posing 4/6
  was an instrument zone next to the start line (attributed by moving
  the cut), re-posed and declared.
- **SQP-RETURN PASS 6/6 ([X-RAOSQ], run of record 2910 s):** from 20
  bands off, the [X-PSPL] driver on an 8-knot spline returns to Rao's
  contour (1.07e-4 vs band 2.4e-4, |grad| 7.8e5 -> 86, J* = J_fit +
  0.3 N); the sign-flipped driver walks away once its budget reaches
  radius ~1.2e-2 (SEG_R1 = 14 calibrated by a probe). The plug sector
  now holds both halves of the bell's O3.3 licence.

## 2. Numbers of record

Twin, legacy field (Rao's rule, Table 1 at 2.44e-3): cert 2.6e-2 /
0.36 / 0.55 at x0 0.30/0.20/0.10; wedge below ED 97.1% within q 1e-3,
95.8% within theta 1.5e-3 rad; gap 5.0e-4 mean = 101x the
reconstruction floor; 0 nonfinite. 2-constraint field: P2 97.0%/96.3%,
P1 seam residual 1.17/1.36 (x0 0.20/0.10).

## 3. Traps (new; the S24 list still holds)

1. **A centred fan is a point relation in axisymmetric flow**, never a
   field: S ~ sin(theta)/y drifts the state along every ray (GENO
   phase-1 rays: 0.1 in M, 3.6 deg over 2.4 y_E). Never pose planar-fan
   states on a cut of finite width; a planar ideal spike ends at
   y = R_T/(1+R_T).
2. **Feeding a dimensional reference field to our march requires ITS
   gas**: identify Rg/p0/T0 from the field (else cert 1e16 with a
   perfectly sane start line).
3. **The jet speed is q_at_pa(p_a), never the max-y field state** (the
   RaoPlug field's top is the sonic lip / control surface).
4. **GENO's RaoPlug field is the kernel under ED**: our free-jet edge
   solves a different problem above ED; grade below ED only; the
   cut-top fictitious fan needs `edge_fill`.
5. **Cross-code gates**: the reference-reconstruction band is the
   instrument floor, not the expected gap; gate at the S8 declared
   thresholds + coverage (precedent [X-GENOP-class]).
6. Repo hygiene on a parallel line: numeric-lint baseline and advisory
   index do not follow your files — add rows in-window (R7).
7. **The first ~0.35 L after a Cauchy start line is not gradable by
   the frozen replay** (wall foot search consuming start rows: AD
   values that follow the cut, FD bands 1e8). Keep design-variation
   support out of it, or the near-cut direction poisons every
   reference-scaled control. Second instance: a spline knot whose
   cardinal function reaches into that zone raised the gradient floor
   on Rao's own wall 60x (3.7e5 vs 6.3e3) and stalled the return.
8. **A rejector that does not move is undecided, not fired.**
   Thrust-minimizing steps leave the certifiable class first (records
   at 1e15..1e16); the reject-and-shrink driver needs enough segments
   for the radius to reach the scale where a certifiable descent
   exists (~1.2e-2 here). Budget it, and read "no motion" as FAIL only
   at the radius floor.

## 4. Open queue

(1) axisymmetric ideal-spike baseline (GENO theta_E=0 member or corner
march) -> Rao-vs-spline A/B at L ~ 5.825 (`PSPL_L` promoted, x_end
extended); (3) findings rows for [X-RAOIS]/[X-RAOWD] (pending-declared);
(4) Italian document: W-5 closed + this chain (stash@{0}); (5) L-sweep
and suboptimal theta_i sweep; (6) [X-FMTR] 1% residual; (7) O3.3 locus;
(8) swirl + stratification; (9) rotational-inlet twin (GENO
final_plug=3).

## 5. Owner decisions

Push access or fork; GENO blessing (RaoPlug N-65/N-66 + the legacy-run
fixes, CTest N-75) and whether to commit `CASES/raoplug_gamma123` +
`plugnoz_axi` + the theory-doc source; the Italian document.