# PROGRESS — [F3/A1] S26: Rao's world, dual-code ("Modo 1") + the rebase (2026-08-26/27)

**Carriers:** `rao1961_oracle.py` [X-RAOTB], `rao1961_control_surface.py`
[X-RAOCS], `rao1961_our_functional.py` [X-RAOFN], `rao1961_ideal_spike.py`
[X-RAOIS], `rao1961_world.py` [X-RAOWD], `rao1961_twin.py` [X-RAOTW],
`o31_rot.py` [X-O31R]. Handoff: `HANDOFF_2026-08-27_S26_rao_twin.md`.
**Opening (R2):** memory + M0 + PROGRESS read; restart = the brick-2 plug
line (`brick2-plug`, S24 handoff + W-5 CLOSED at 0d536c6) with the
13-14 August work UNCOMMITTED and UNLOGGED (the R3 gap this log closes).
Plan position: F3 GEOMETRY CLASSES, entry leg "single-oracle status
(Rao 1961 Table 1) declared" — the spike-level plug de-risk the plan
authorizes parallel to F2; item [X-O31R] is F2b (adjoint on the
stratified march).

## 1. The rebase (2026-08-26)

`origin/rde-nozzle-program` moved a021fdd -> 6be51b9 (S-ORDINE R32,
F-SERVICE, S-CERT R33, S-FOUNDATIONS R35 parts 1/C/C2/C3/C4, S-PRES
sessions 1-2). `brick2-plug` rebased: 6be51b9 + 15 commits (the 14
brick-2 commits replayed with `--committer-date-is-author-date`, plus
c1498ee = the six typed `ondemand` lines the 2026-08-13 merge had added,
carried as its own commit). Registry verified entry-by-entry against the
clean three-way merge; local `rde-nozzle-program` fast-forwarded. Three
measured traps, now in memory: the registry conflicts must be resolved
per-entry (a tail block duplicates 35 upstream ids); the ignored `.npz`
caches block the replay of the commit that re-adds them; the claims
lint's staleness link reads the COMMITTER date (%cs). Previous tip
ee17bd0 kept in the reflog.

## 2. Verdicts measured this window (all commands quoted in the carriers)

| carrier | result | the number |
|---|---|---|
| rao1961_oracle | PASS 18/18 | Rao 1961 tables usable as oracle (F3-entry leg) |
| rao1961_control_surface | PASS 6/6 | optimum from his Eqs. (6)-(7): p_a/P_c 0.0355, eps 3.81, X_D 1.164, C_F 1.58, terminus to 0.05 deg |
| rao1961_our_functional | PASS 3/3 | our J on his surface: eps 1.5e-4, C_F 2.5e-4 |
| rao1961_ideal_spike | FALSIFIER FIRED (4 FAIL/1 PASS) | planar-fan streamline stops at y = R_T/(1+R_T) (0.4772/0.4962, 3e-5), never closes |
| rao1961_world | FALSIFIER FIRED | cert 5e-2 / 5e10 / 1e11 / 32 at x0 0.30/0.20/0.10/0.05: non-monotone |
| rao1961_twin (legacy field) | **PASS 6/6** | cert 2.6e-2/0.36/0.55; 0 nonfinite; 97.1% within q 1e-3, 95.8% within theta 1.5e-3 rad |
| rao1961_twin (2-constraint field) | FAIL (P1 seam) | P2 PASS 97.0%/96.3%; P1 edge cells 1.17/1.36 at x0 0.20/0.10 — named residual |
| o31_rot | PASS 6/6 | adjoint through the clamped stratified march 9.2e-8 rel, 35x inside the 3.2e-6 floor |

## 3. "Modo 1": GENO's field as our start line

GENO `bin/GENO` (2026-08-09, RELEASE=-O0, matches the uncommitted RaoPlug
source) ran `CASES/raoplug_gamma123` on s2: the 2-constraint run matches
its README (eps 3.3706, L 0.93873, mdot deficit -1e-4 %); the LEGACY
p_b=0 corner-stop run — Rao's own rule, listed as broken pre-fix —
runs and reproduces Rao's Table 1 at mean 2.44e-3 over 16/16 points.
Run dirs `GENO/CASES/raoplug_run{,_legacy}` (READMEs; outputs ignored).

The twin as drafted (2026-08-14, never run) had three defects, fixed in
place and re-registered in its header: **D1** default gconst gas on
GENO's dimensional field (cert 1e16) -> gas identified FROM the field
(Rg 415.7255, p0 6.00818e6, T0 3500); **D2** jet speed read at the
max-y point (near-sonic lip, 1304 m/s) -> q_at_pa(0.0355 p0) = 2688.5
m/s; **D3** the RaoPlug field is the KERNEL bounded above by the C-
control surface ED (p 3.3e6 -> 4.0e5), not a p=p_a jet — our march adds
a jet edge and solves a different, well-posed problem above ED; since
same-family characteristics do not cross, the two problems coincide
below ED, so the wedge below ED is graded (EDGE_FILL=6 spans the
fictitious cut-top fan). Verdict of record (legacy field): P1 3/3, P2
3/3, VERDICT PASS; log `validation/_rao1961_twin/run_of_record_legacy_2026-08-26.log`.

## 4. Deviations DECLARED

- **P2 gate rederived.** The first in-window gate compared the wedge
  gap to the reference-RECONSTRUCTION band (full vs subsampled cloud,
  5e-6): the measured gap (5.0e-4 mean, resolution-stable over N
  41/61/81) sits 101x above it. That band bounds the instrument's
  floor, not the two codes' discretization gap — which the S8 twin
  finding places ABOVE both truncations. Gate of record = the S8
  DECLARED thresholds (q 1e-3, theta 1.5e-3 rad, coverage >= 0.95);
  the reconstruction band is reported as floor, never gated on.
- **P3 not observed as pre-registered**: the wedge gap does not improve
  with an upstream cut (6.9e-4 at x0 0.10) — reported, not gated.
- **Second instance** (2-constraint field) fails P1 at the kernel-top
  seam (edge 1.17/1.36): NAMED residual, EDGE_FILL not retuned.
- **PROGRESS.md (census) not edited**: upstream-owned in this parallel
  line (S21-S25 precedent, "sessioni parallele: file disgiunti");
  state carried by this log + handoff.
- **Findings rows** for the two fired falsifiers (planar fan as field;
  planar start on a wide cut) = PENDING-DECLARED (SR-6): the lessons are
  registered in the carriers' rows [X-RAOIS]/[X-RAOWD] and in the GENO
  theory doc; the findings-registry mint rides the next R3 window.
- **R4 delta**: the corner-fan lesson (centred fan = point relation in
  axisymmetric flow; GENO's treatment; measured drifts; the planar
  R_T/(1+R_T) closure) is written in the GENO theory document, ch. 7.2
  "The lip fan in axisymmetric flow" (GENO repo, untracked doc source,
  figures from `CASES/plugnoz_axi`). The brick-2 LaTeX document (Italian
  translation, stash@{0}) is NOT updated: owner decision pending (it must
  now state W-5 CLOSED 9/9 and this chain).

## 5. Hygiene closed in-window (R7)

- numeric-lint ratchet (R28): 30 birth rows for the brick-2 line's
  validation carriers (never baselined: the ratchet was frozen upstream
  on 2026-08-12 while the line lived on its branch), counts measured by
  the lint; PASS 97 files / 0 violations, seeded rejectors REJECTED.
- advisory index (xx): rows for the 9 brick-2 .md files without one
  (S15-S24 handoffs/logs) + this log + the S26 handoff.
- claims registry (xv): 7 carrier rows, typed ondemand pass=2026-08-26.
- Known environmental red: findings lint (xix) DEAD PATH rows for
  literature PDFs absent on s2 (fails identically on pure upstream).

## 6. Closing suite (measured, SR-12)

Runs of record re-executed 2026-08-27 for the pass stamps (all eight
verdicts identical to 2026-08-26; logs in `validation/_rao1961_twin/`):
oracle 18/18, control-surface 6/6, functional 3/3, ideal-spike 1/5
(falsifier), world 1/4 (falsifier), o31_rot PASS, twin legacy PASS 6/6,
twin 2-constraint FAIL 4/6 (P1 seam).

`python tests/run_all.py` on the final pre-commit tree, 2026-08-27
16:12-16:15: **14/23 groups PASS in 161 s, EXIT 1.** The nine FAILs,
each attributed by its own output: (xiii), (xiv), (xvi), (xviii) =
`ModuleNotFoundError: sympy` (pinned s2 env, install forbidden);
(xix), (xxii), (xxiii) = DEAD PATH literature PDFs absent on s2 (the
glossary's 52 unresolved tokens == its baseline 52: this window minted
none); (xv), (xvii) = the seven new carrier rows citing this log, which
had "no committed history" before commit — cleared by the first commit
of the window (post-commit confirmation below).

Comparison measured on a clean worktree at HEAD c1498ee (before this
window's edits), `run_all.py --fast`: 12/19 vs 13/19 on the final tree;
the only differences are (vii) numeric lint FAIL -> PASS and (xx)
advisory index FAIL -> PASS (both repaired here) and (xv) PASS -> FAIL
(the uncommitted-log staleness above). The five persistent reds are
identical on both trees: environmental, not of this window.

Post-commit confirmation (measured after commits 21ae689 / bbbe5f8 /
dc1e458): claims lint (xv) PASS 0 violations; on-demand tier (xvii)
PASS (32 accounted, all fresh); numeric lint (vii) PASS; advisory
index (xx) PASS. Suite side-effect DECLARED and reverted, not
committed: `run_all.py` regenerated `data/phase_diagram.{json,md}`,
`data/q_mapping.{json,md}` and `figs/phase_diagram_op11.png` with
platform round-off (1e-16 rel on `ek`, 1e-13 on `ideal_vs_ek`; s2 numpy
2.4.6 vs the pinned 2.5.2), timestamps and a re-rendered PNG — churn,
not content (`git checkout --` on the five files).

Commits of the window: 21ae689 (F3 entry Rao chain + twin + registry +
log/handoff), bbbe5f8 ([X-O31R]), dc1e458 (PSPL_L + s25 m0), and the
closing hygiene commit carrying this block.

## 7. Addendum 2026-08-27 (after the closing commit dc4b339): the plug-sector O3.3 [X-RAOO3]

The step the twin unblocked, executed the same day. `rao1961_o33.py`
mirrors `a1_o33_toc.py` STAGE=stationarity on the plug: our march from
GENO's legacy field at x0, GENO's (= Rao's) wall on [x0, x_D] with six
interior endpoint-pinned Gaussian bumps + a tip blip, one reverse pass
for the seven projected derivatives, FD-Richardson+ripple bands per
direction, a perturbed-wall control, Rao's corner relation Eq. (9) at
the marched end. Base pressure never modelled: for pinned ends the base
term is a constant; for the tip direction it yields a PREDICTION.

**First posing (bell-identical bump family from 0.20 L_r), x0 0.30:
4/6.** P1 cert 2.6e-2; P2 pass (dirs 2-5 at 1.7e2..5e2 vs bands
3e5..1e6; dirs 0-1 with FD bands 1e8 — vacuous); N1 pass with the tip
identity at **1.0046** of 2 pi y_D p_a; P3 pass (+1.9e3 N); N2 FAIL, P4
FAIL. Attribution run (x0 0.20): the near-cut direction FOLLOWS the cut
(9.2e4 -> 1.3e5, FD band 2e8), dirs 1-5 stay at 1e2..1e3, tip identity
0.9989 — the zone right after the start line, where the wall cell's
multi-column foot search consumes Cauchy rows, is not smooth under the
frozen replay: instrument, not physics; N2 failed only because that
value set the reference scale. P4's control (tip lift 0.02) was too
weak against a reference residual (5.4e-4) at the cross-code level.

**v2 (declared re-posing: bump support excluded from the first
0.35 L_r after the cut, corner control lift 0.05, tip identity promoted
to a gated check with its FD band): 7/7 PASS at x0 = 0.30 (run of
record) and 7/7 at x0 = 0.20.** Interior AD gradients 8e1..4e2 N/m
(perturbed wall 7e4..4.3e5: N2 ~1000x); J(Rao) - J(pert) = +2.1e3 N;
tip gradient 1.660e5 vs prediction 1.653e5 (band 2.9e3) and 1.651e5 vs
1.653e5 (band 2.4e3); Eq. (9) at D: 5.4e-4 / 6.5e-4 vs 1.6e-2 / 1.2e-2
on the tip-lifted wall. Logs: `_rao1961_twin/run_o33_posing1_x030`,
`run_o33_attribution_x020`, `run_of_record_o33_v2_x030`,
`run_o33_v2_x020` (all 2026-08-27). Numeric-lint birth row 17
(measured). Registry row [X-RAOO3], pass 2026-08-27; carried by the
fifth commit of the window.

What it means: the plug sector now has what the bell had since S19 —
the classical optimum is stationary for the very functional and
gradient the SQP consumes, and its live variable (the tip height) obeys
Rao's own base-term balance to 0.5 percent. Deviations declared: the
bump family was re-posed after attribution (near-cut instrument zone);
the tip identity was promoted from reported to gated after two
consistent measurements; P4's control amplitude was calibrated.

## NEXT (atomic)

The SQP-RETURN stage of the plug O3.3: a spline design vector on
[x0, x_D] in Rao's world (twin start line, [X-RAOO3] posing), TR-SQP
from a perturbed start, return to Rao's contour inside a band derived
from the spline representation error + the march ladder — the plug
analogue of [X-TOCV]'s "from a 1.5 percent perturbed start". Then the
axisymmetric ideal-spike baseline (GENO RaoPlug theta_E=0 member, or a
corner march) -> the full-expansion Rao-vs-spline A/B at L ~ 5.825 m
(`PSPL_L`, open-queue item 3).

## BLOCCATO

Push read-only (AlexFalco5 on Alemontanari97/RDE_Design): commits local.
GENO commits gated by GENO's own protocol (N-75 CTest env mismatches).
Italian brick-2 document: commit or hold (stash@{0}).