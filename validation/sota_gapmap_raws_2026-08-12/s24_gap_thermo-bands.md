# S24 GAP MAP — FACET 6: THERMO CLOSURE + TOLERANCE/BAND CULTURE
**Finder key**: thermo-bands · **Date**: 2026-08-12 (S24 window) · **Status**: finder position for the verify pass

## 0. Standing verdict KEPT (not relitigated)
The [X-THC1] quintic C1 closure verdict of `validation/ADVISORY_S24_thermo_closure_survey_2026-08-12.md`
(KEEP; NASA-direct = oracle only per C-A; dCp-ingest gated by C-B; joint census C-C; box-exit rejector C-D)
is taken as FRESH of record. Every finding below is about the REMAINING band/tolerance culture, or sharpens
C-D with new measurement. Nothing here proposes weakening per-cell certification, rejectors, derived
tolerances, or RK-G determinism.

## 0bis. Probes run (declared, all on the small instance / pure analytics; no march, no optimizer)
- **P1** `probe_box_clamp.py` — table analytics only (build_tab_nasa + closures, jax.grad on scalars).
  1 run, **32.8 s wall**. No competition with the running S24 campaign (no march, no jit of the engine).
- **P2** `probe_band_models.py` — pure numpy, <1 s. Run 3 times: the first two parameterizations failed
  to reach the cancellation regime (my parameter error, declared — those runs are NOT evidence of safety);
  the third is the run of record.
- Probe scripts live in this scratchpad; every number below marked (P1)/(P2) is from these runs.

---

## G1 — Box exit is silent in BOTH closures and the C1 closure fails WORSE than the clamp (C-D sharpened)
- **Where**: `validation/a1_ideal_march_jax.py:350-353` (`jnp.interp` endpoint clamp -> T frozen, dT/dq = 0);
  `validation/thermotab_c1_jax.py:144` (`jnp.clip(searchsorted...)` -> edge-interval polynomial
  EXTRAPOLATES outside the box) + `:189-197` (`invert_h`: Newton, fixed 8 trips, on that extrapolated
  quintic). Prior anchor: `validation/AUDIT_agnostic_2026-08-07.md:386-398` (C-D, linear clamp only).
- **Measured (P1)**: at q = 1.05·q_max(box): linear closure returns T = T_TAB_LO exactly with
  **dT/dq = -0.0** (silent clamp, zero gradient — the known C-D). The C1 quintic closure returns
  **T = 863.2 K** (187 K below the box floor) with **dT/dq = +0.545** — wrong magnitude AND wrong SIGN
  (physical slope at the edge: -1.94, measured at q/q_max = 0.999). At q/q_max = 1.02: T_c1 = 854.3 K,
  dT/dq = -0.12 (16x too shallow). The C1 branch is *worse than the clamp*: it feeds plausible-looking,
  smoothly-varying, WRONG states and gradients into the march and the adjoint, so a frozen-T detector
  built for the linear route would NOT catch it.
- **Class**: RIGOR-GAP (C-D is an open declared residual; the C1-branch extrapolation mode is a NEW datum
  not in the audit text — the traced box-exit rejector must cover BOTH failure modes).
- **SOTA**: domain-guarded table evaluation with a traced out-of-range flag checked like `cert_worst`
  (lineage: CoolProp TTSE bounds errors; SU2/Fluent look-up-table out-of-bounds policy = clamp+WARN at
  minimum), plus the repo's own rejector pattern (NaN-poisoning or verdict-bearing counter, as in the
  margin governor's masked-lane counters).
- **Extremal cases**: (a) eps -> 100+ (P1: eps_box = 102.8 — the whole case leaves the box);
  (b) deep-DEF / short-L instance whose Newton iterates transiently overshoot q_max during damping
  (trial candidates evaluate state_q OUTSIDE the box even when the solution is inside — the C1
  extrapolation then feeds the damped-trial norm comparison); (c) hotter propellant with T0 above
  3865 K entering at q -> 0 (top-of-box exit in the subsonic seed region).
  **Everyday case**: eps = 4 twin — exit T margin 1276.8 K (P1), safely inside; nothing fires today,
  which is exactly why the rejector must be traced, not situational.

## G2 — The table box is not DERIVED from the case: no q-range margin certificate exists
- **Where**: `validation/a1_ideal_march_jax.py:142-143` (`N_TAB = 8192`, `T_TAB_LO, T_TAB_HI = 1050, 3900`
  — literals); `validation/thermotab_c1_jax.py:32-33` claims the declared box "contains every
  march-realized state" — a hypothesis with no per-run check anywhere (grep: no assert on realized T/ht
  vs the box in run_march / run_scan / run_toc_record).
- **Measured (P1)**: stagnation margin T_TAB_HI - T(q->0) = **34.8 K** (undeclared; ~100 table intervals);
  cold-side: q_max(box) = 3467.4 m/s = M 5.006; exit-T margin above T_TAB_LO: 1276.8 K at eps=4,
  454.5 K at eps=25, 216.3 K at eps=50, **8.34 K at eps=100** (~24 intervals). The margins are FINE at
  the current instances — but no committed number says so, and no rejector notices when they stop being fine.
- **Class**: INCOMPLETE (the generality directive says procedures must be case-independent: the box should
  be derived from the case envelope + declared margin, or at minimum certified against it per run).
- **SOTA**: envelope-driven table generation with declared margin factor (CEA/CoolProp practice: build the
  table from the case's state envelope; REFPROP tabulation guidance), unified with the advisory's C-C
  joint-census machinery (same ingest path, same certificate): per-run realized-(T,ht) census -> box-margin
  row in the Verdict.
- **Extremal cases**: (a) eps = 100+ frontier scan instance (8 K margin, one governor continuation step
  from the edge); (b) high-T0 case: any table regenerated for T0 within ~35 K of today's stagnation
  silently exits at the TOP of the box — the subsonic branch near q -> 0 clamps FIRST (interacting with
  the near-sonic Newton damping of G1(b)). **Everyday case**: defnoz-class eps ~ 10-25 (margins 200-500 K,
  comfortable — and unrecorded).

## G3 — K_RICH = 4: derived in ONE role, reused as a universal constant in at least SEVEN
- **Where (role census, file:line)**:
  1. Two-level Richardson safety (the ORIGINAL role, with a rationale): `a1_ideal_march_jax.py:145,1110`;
     allowlist note `validation/numeric_allowlist.json:754` ("covers the 1/3 Richardson factor with margin").
  2. FD dot-product band scaling incl. the roundoff floor: `a1_ideal_march_jax.py:1338-40`,
     `a1_toc_variational_jax.py:1480-82`.
  3. KS aggregation sharpness rho = K_RICH ln(N)/mu0_min: `margin_governor.py:27-29` (here it is a
     DERIVED requirement ratio — legitimate, but the 4 is the same unexamined numeral).
  4. Lipschitz measured-sup surrogate L_TB = K_RICH * max(two-point sups): `margin_tolerance_backoff.py:147`.
  5. Instance margin floor delta = min_margin/K_RICH: `a1_toc_variational_jax.py:1403`,
     `adaptive_knot_optimize.py:362`.
  6. Locus threshold m_ref/K_RICH: `locus_diagnosis.py:276`.
  7. Cost gate K_prac = 4: `docs/rde_nozzle_brick2_kickoff.md:270-278` ("the SAME two-level safety
     constant — reused, not invented").
  Grid-Lipschitz G-floor (thermotab_c1_jax.py:359) is the same pattern in an 8th role.
- **Derivation status**: only role 1 has a quantitative rationale, and it is exact for p = 2 only.
  **Measured (P2a)**: under the model f_h = f* + C h^p, band/true-error(fine) = 4(2^p - 1): 12.0x at p = 2,
  4.0x at p = 1, 1.66x at p = 0.5, and **UNDER-COVERS iff p < log2(1+1/4) = 0.3219**. So the constant is
  honest protection down to p ~ 0.32 *when the power-law model holds* — a derivable, per-context coverage
  statement that exists nowhere in the docs. Roles 4-7 have NO bracketing theorem at all (a two-point sup
  times 4 bounds no Lipschitz constant; min_margin/4 as a floor has no stated failure model).
- **Class**: RIGOR-GAP — and ALREADY A REGISTERED OPEN ROW: `docs/rde_nozzle_PROGRESS.md:249`
  ("universalita' K_RICH=4 (F2 audit)"). This finding SHARPENS the open row with the role census and the
  p-threshold; it does not mint it.
- **SOTA**: Grid Convergence Index with observed order (Roache 1994; Celik et al., J. Fluids Eng. 2008
  five-step procedure): Fs = 1.25 with a THREE-grid observed-p, Fs = 3 for two-grid fixed-p — i.e. SOTA
  ties the safety factor to whether the order was measured; per-role derived constants elsewhere
  (Lipschitz roles -> interval/Bernstein bounds, see drop list).
- **Extremal cases**: (a) any band site with local observed order p < 0.32 — plausible exactly at
  frontier/deep-DEF instances (outcome-II, KKT open at 1.6e6) where field regularity degrades at the
  limiting characteristic; (b) deep-DEF margin floor: min_margin -> 0 makes delta = min_margin/4
  meaningless as a floor (divides a vanishing number by a constant). **Everyday case**: eps = 4 contour
  band — `contour_compare` prints median err/band, the measured slack that a per-role coverage statement
  would formalize.

## G4 — Two-resolution POINTWISE bands are invalid across plan-topology flips (and collapse at crossing points)
- **Where**: `a1_ideal_march_jax.py:1099-1117` (`contour_compare`: per-x band K*(e(x)+floor),
  e(x) = |y_h(x) - y_h2(x)|); `a1_toc_variational_jax.py:1415-1427` (band_u, same construction on the wall
  speed); `o33_bench.py` field bands (same recipe per the S21 honesty rewrite, `o33_bench.py:96-106`).
  The repo KNOWS refinement cannot hold the march topology fixed — the LB-c2 topology monitor exists in
  `o32_mesh_convergence.py:545-557` — but NO band row checks topology consistency of its own (h, h/2) pair.
- **Measured (P2b)**: with a level-dependent stratum offset comparable to the smooth h^2 term (the
  flip model: wall-search index re-records / a column gains an axis cell between the two resolutions),
  the pointwise band under-covers at **11.2% of points, worst true-err/band = 1853x**, because e(x)
  CANCELS against the smooth difference (min e = 8.3e-7 -> band collapses to the roundoff floor at
  cancellation abscissae). Control with no flip: 0/2001 out-of-coverage. Even without a flip, e(x) has
  sign-crossing zeros where the band collapses to floor while the true error need not vanish —
  a standard pathology of two-grid pointwise estimates.
- **Class**: RIGOR-GAP (the bands of record passed 62/62 and 0/98-out — but nothing certifies those
  pairs were topology-consistent, so the PASS is conditional on an unchecked hypothesis).
- **SOTA**: (i) topology-conditioned banding: assert plan-census invariance between the two resolutions
  (the o32 LB-c2 monitor wired INTO every band row — machinery already exists); (ii) least-squares
  multi-grid uncertainty robust to non-monotone convergence (Eça & Hoekstra, J. Comput. Phys. 2014);
  (iii) DWR goal-oriented a-posteriori (Becker & Rannacher, Acta Numerica 2001) — already NAMED in
  D4 `docs/rde_nozzle_claims_verdict.md:217`, M0 `docs/rde_nozzle_MASTER.md:1297`, and the open choice
  row "mesh AMR/DWR (F2)" `docs/rde_nozzle_PROGRESS.md:247` — never built; adjoints are already available,
  the marginal cost is the point of the D4 line.
- **Extremal cases**: (a) [X-AKNO] nearly-degenerate knots: the insertion-site skip rule
  (`adaptive_knot_optimize.py:39-42`) sits exactly at a plan-flip boundary — one resolution inserts,
  the refined one skips; (b) deep-DEF / very short L: wall-search indices re-record between resolutions
  (the S23 defnoz lesson class). **Everyday case**: eps = 4 twin contour band (S4 row of record) —
  passes today with no topology attestation attached.

## G5 — Newton-floor constants are conventions, not derivations (and the z-scale mixes units)
- **Where**: `a1_ideal_march_jax.py:145-147` (`C_FLOOR = 8.0`, `NEWTON_TOL_FACTOR = 100.0`; the only
  stated basis is "spike factor convention", :85-86); `thermotab_c1_jax.py:85` (`C_OPS = 100.0`,
  "repo convention"); ad-hoc x10 escalations at `a1_toc_variational_jax.py:1434`, `a1_march_scan.py:842`.
  C_FLOOR = 8 in the FD floor `C_FLOOR * EPS^(2/3) * scale` (a1:1338-40) has NO derivation note anywhere
  (grep over validation/ + docs/). Prior anchor: `AUDIT_agnostic_2026-08-07.md:418-426` flagged this
  cluster and prescribed a halved-constants sensitivity test — never executed. Structural addition
  beyond the audit: the certification scale `sc = max(1, max|z|)` (`a1_ideal_march_jax.py:393`) is a
  SINGLE scale over unit-mixed z (u ~ 2e3 m/s vs x,y ~ 1 m), so position components are certified
  against a bound inflated by ~3 orders relative to their own magnitude.
- **Class**: RIGOR-GAP (already flagged, unresolved; the unit-mixing point is additional).
- **SOTA**: backward-error certification with op-count constants gamma_n = nu/(1-nu) and componentwise
  Oettli-Prager residual tests (Higham, *Accuracy and Stability of Numerical Algorithms*, 2002);
  FD-floor constants from noise estimation (More & Wild ECNoise, SIOPT 2011; Gill-Murray-Wright FD
  interval selection) instead of a fixed 8.
- **Extremal cases**: (a) very short L / few-cell march: per-cell floor 100*eps*sc with sc pinned by u
  can exceed the entire y-signal of a boundary cell — a wrong y at the 1e-13 level certifies; (b) KS
  margin gradients at rho ~ 5.75e4 (`ADVISORY_S24_DEbucket_panel:53`): the FD dot-product floor constant
  was never revalidated at that gradient scale. **Everyday case**: every O3.1 row (tol_dp) and every
  replay-fidelity row (x10). **Probe NOT run** (requires carrier re-runs, > 30 s):
  **REGISTER for S25** — "halved-constants sensitivity sweep + component-scaled z-metric" exactly per
  AUDIT:426, one flag per constant, PASS->FAIL flips name the load-bearing tolerances.

## G6 — Band composition has no declared rule: sum, max, and heterogeneous mixes coexist
- **Where**: SUM composition K*(A + B): `a1_ideal_march_jax.py:1338-40`, `a1_toc_variational_jax.py:1480-82`
  (note: K_RICH multiplies the roundoff floor too — the floor is not a Richardson estimate; conservative
  but category-mixing, undeclared). MAX composition: `def_twin_falsifier.py:380-381`
  (band12 = K_RICH * max(cell_r1, cell_r2)) and `:404` (band_dprime = K_RICH * max(cell, ds_land)).
  Heterogeneous unweighted sums mixing K-scaled Richardson terms, raw residuals, and Newton floors:
  `def_twin_falsifier.py:1122-1124, 1147, 1167-68`. No doc states WHEN each form applies or what
  correlation between components is assumed.
- **Measured (P2c)**: for two comparable independent components (a = 1.0, b = 0.9), K*max covers the
  worst case a+b by only **2.11x** — the intended 4x safety is silently halved exactly when both error
  mechanisms contribute; K*sum keeps 4.0x; GUM RSS gives 2.83x.
- **Class**: RIGOR-GAP.
- **SOTA**: GUM composition rules (JCGM 100:2008: RSS for independent components, linear sum when
  correlation is unknown = conservative); ASME V&V 20-2009 validation-uncertainty composition
  u_val = sqrt(u_num^2 + u_input^2 + u_D^2). The fix is a one-paragraph declared policy + a pass over
  the max sites, not new machinery.
- **Extremal cases**: (a) def_twin D' band with cell ~ ds_land (deep-DEF landing near a cell boundary:
  both terms comparable, max under-covers by 2x); (b) floor-dominated band (tiny Richardson difference):
  K x floor inflates a machine floor 4x and can mask a genuine small signal — the o33 "band collapses and
  K_RICH x ~0 protects nothing" comment (`a1_toc_variational_jax.py:1708`) already noticed the dual of
  this. **Everyday case**: O3.1 tol_dp at the eps = 4 twin (sum form, benign).

## G7 — Every two-level band assumes asymptotic range; the repo's OWN order measurement is NON-CONCLUSIVE there
- **Where**: the S19 O3.2 row of record: p_fine = 2.5347, dp_tot = 0.6704 -> **NON-CONCLUSIVE at the
  pre-registered 0.5 cap** (`o32_mesh_convergence.py:72-75, 241-255`); meanwhile every two-resolution band
  (G4 sites) presumes the h^p model at r = 1 vs 2 — COARSER than the ladder that failed to certify
  asymptotic range. The bands' justification (K covers the 1/3 factor) is a p = 2 asymptotic statement.
- **Honest datum (P2a)**: the K = 4 slack protects down to observed p ~ 0.32 under the power-law model,
  so this is a missing DECLARATION + missing per-site order check, not a measured failure.
- **Class**: RIGOR-GAP (mild, coherence): a band whose site is out of asymptotic range should say so —
  the o32 NON-CONCLUSIVE verdict does not propagate to the band rows that share its hypothesis.
- **SOTA**: observed-order verification at band sites (Celik et al. 2008; Roache): three-level check with
  the estimator ALREADY BUILT in `o32_mesh_convergence.py:151-192` — reuse, not new code; NON-CONCLUSIVE
  propagation rule (site fails order check -> band carries the degraded-p coverage factor 4(2^p - 1)).
- **Extremal cases**: (a) frontier/deep-DEF instance (outcome-II, KKT 1.6e6): regularity loss at the
  limiting characteristic degrades local p; (b) near-axis y -> 0 cells (c^2 v / y source): local order
  loss the registered-norm exclusion hides from o32 but NOT from the pointwise contour band, which has no
  exclusion. **Everyday case**: the r = 1,2 pair at eps = 4 — the only two levels any band actually uses.
- **Cheap S25 lever (register)**: a THIRD resolution in contour_compare/band_u (r = 3 exists in the o32
  ladder machinery) upgrades every two-level band to observed-order GCI at ~1 extra march per row.

---

## Drop count: 3 dropped (named, with reasons)
1. **G-floor grid audit is not an interval certificate** (`thermotab_c1_jax.py:31-35, 354-366`) — TRUE but
   already DECLARED in the file itself with a named upgrade substrate (PAP-GMAX); restating a declared
   conditional is not a finding. (Bernstein-form/interval range bounding remains the named SOTA if c4
   becomes load-bearing.)
2. **q-scan supersonic-seed flux-window silent fallback** (`AUDIT_agnostic_2026-08-07.md:454`) — real, but
   it is Newton seeding, outside this facet (band/tolerance culture), and already audited with a suggested
   test; the box-derived q_max of G2 is its natural fix and is credited there.
3. **o33 structural discriminators (20x, 0.5, 1e-4)** — already honestly reclassified by the S21 rewrite
   (`o33_bench.py:96-106`) as declared-not-derived with a P2-scheduled derivation row; relitigating a
   declared, scheduled item adds nothing.

## Summary table
| # | Finding | Class | Probe | S25 registration |
|---|---|---|---|---|
| G1 | Box exit silent; C1 closure extrapolates with sign-flipped gradient (C-D sharpened) | RIGOR-GAP | P1 RUN (32.8 s) | traced box-exit rejector covering BOTH modes (C-D owner F2) |
| G2 | Table box literals; no per-case margin certificate (35 K hot margin undeclared) | INCOMPLETE | P1 RUN | per-run realized-state census -> box-margin Verdict row |
| G3 | K_RICH=4 universal across >=7 roles; derived in 1 | RIGOR-GAP | P2a RUN | per-role coverage statements (sharpens open PROGRESS:249 row) |
| G4 | Pointwise 2-res bands invalid across plan-topology flips; crossing collapse | RIGOR-GAP | P2b RUN (11.2% out, 1853x worst) | wire LB-c2 monitor into band rows; Eça-Hoekstra / DWR (open PROGRESS:247 row) |
| G5 | NEWTON_TOL_FACTOR/C_FLOOR/C_OPS/x10 conventions; unit-mixed z-scale | RIGOR-GAP | not run (>30 s) | halved-constants sweep + component-scaled metric (AUDIT:426) |
| G6 | No band-composition rule; max halves the safety when components comparable | RIGOR-GAP | P2c RUN | declared GUM-style composition policy + pass over max sites |
| G7 | Asymptotic-range hypothesis undeclared at band sites; o32 NON-CONCLUSIVE not propagated | RIGOR-GAP (mild) | P2a RUN (analytic) | third resolution -> observed-order GCI per band row |
