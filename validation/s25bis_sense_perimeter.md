# S25-bis PERIMETER SENSE-REVIEW (R29) — algorithmic-choice adjudication

- **Reviewer role**: expert perimeter sense-review (numerical analysis /
  JAX-XLA compilation semantics / adjoint methods / nonlinear
  optimization). Question of record: does each S25-bis choice make deep
  sense for THIS problem, and is it the state-of-the-art choice against
  its genuine alternatives? (Implementation fidelity is the refuter's
  jurisdiction, not re-done here.)
- **Tree**: HEAD `ea8143c` (S25-bis closure); levers diff
  `ad5c48e..1806ae2`; instruments `18b4e0f`.
- **Perimeter (only)**: (1) M5c per-column compiled executor;
  (2) H3 preplan/last_cert reuse; (3) H4 code-identity persistence;
  (4) M6 batched FD Hessian + cross-lowering floor; (5) named
  single-author instruments (validation ratchet, findings registry).
- **Dedup authorities consulted (cited, never re-minted)**:
  `docs/findings_registry.yaml` (17 rows; rows cited below by id);
  `validation/ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md`
  (whole-pipeline review, converged — its §4.4 half-nit repairs were
  verified landed and are NOT re-adjudicated here).
- **Evidence base read**: `validation/a1_toc_variational_jax.py`
  (M5c 190-670, engine 845-1162, driver/FD 1216-1930);
  `validation/a1_ideal_march_jax.py` (653-693 predictor twin, 417-518
  implicit solver); `validation/def_twin_falsifier.py` (144-169 H4,
  904-975 derive tail, 1042-1078/1147-1158/1193/1262 H3);
  `validation/margin_governor.py` (485-560);
  `validation/engine_speed_bench.py` (m5cgate 654-844, m6gate 847-955,
  h3gate 958-1049); logs `s25bis_m5cgate_run2.log`,
  `s25bis_m6gate_run1.log`, `s25bis_m6diag.log`, `s25bis_m6locus.log`,
  `s25bis_m6fix.log`; `validation/PROGRESS_2026-08-12_S25bis_speed.md`
  steps 3, 5-6, 10, 13, 15; `tests/test_numeric_lint.py`,
  `tests/test_findings_registry.py`,
  `validation/numeric_lint_baseline_validation.json`.

Verdict labels: **ADOPT-AS-IS** / **ADOPT-WITH-CAVEAT** /
**RECOMMEND-CHANGE** (priced) / **OPEN-QUESTION** (with settling
experiment). All statements below are measured or derived; no
superlatives are load-bearing.

---

## Object 1 — M5c per-column compiled executor

### Finding 1 — scan-of-while_loop with the inlined fused solver is the
### correct primitive here; the named alternatives lose either semantics
### or compute. **ADOPT-AS-IS**

Code: `validation/a1_toc_variational_jax.py:227-258` (`_col_executor`:
one `jax.lax.scan` whose body calls the jitted `solve_cert` =
`validation/a1_ideal_march_jax.py:490-502`, itself wrapping the damped
Newton `while_loop` at `:431-473`); in-trace seeds by the traced
predictor twin `validation/a1_ideal_march_jax.py:653-693`.

Adjudication against the stated alternative set:

- **`lax.scan` vs `jax.lax.map`**: not a real alternative — the column
  is a recurrence (each cell's solution is the next cell's carry,
  `run_col` body at `:240-246`); `map` has no carry and cannot express
  it. Disqualified structurally, not by preference.
- **while_loop Newton vs bounded-unroll `fori_loop(K)`**: the
  while_loop terminates on the certification metric itself
  (`a1_ideal_march_jax.py:444-448`: `step > NEWTON_TOL_FACTOR*EPS*sc`,
  cap `N_NEWTON=30`). A fixed-K loop would (i) keep polishing past the
  certification bound, so `z` and the certification `step` would differ
  from the per-cell path at floor level — destroying the design
  property that the executor dispatches the *identical jitted
  `solve_cert` object* the per-cell path uses (identity, not
  similarity, is what makes the m5cgate dec-vector comparison
  meaningful); (ii) pay up to 30 trips x 6 damped trials per
  already-converged cell — the record path replays near-converged
  seeds, where the metric-terminated loop exits in O(1) trips (the S18
  amendment of record, docstring `:433-441`). The classic objection to
  while_loop — no reverse-mode rule — is void on this path: the record
  executor is host-consumed only; AD lives in the replay's
  `custom_vjp solve` (`:504-517`). fori_loop would buy differentiability
  nobody consumes at the price of semantics the gate requires.
- **Batched-cell (wavefront/vmap-across-columns) formulations**: would
  require re-expressing adaptivity (truncation, wall_search, aborts) as
  traced masks — the eager `cell_scan`-class pattern already REJECTED
  of record (PROGRESS step 3; `a1_toc_variational_jax.py:200-203`). Not
  re-adjudicated here (dedup); I note only that the rejection is
  consistent with the measured outcome: the win was dispatch-count
  (~7,900 host dispatches to ~500 on the full net), and per-column
  granularity already captures it (measured 17.5-18.1 s -> 5.66-5.91 s
  warm, 3.07-3.16x, `s25bis_m5cgate_run2.log:11,26`) with decisions
  still host-auditable.
- **In-trace seeds (traced predictor twin) vs host seeds**: without
  in-trace seeds the scan operand would need the seed stack, which only
  the host predictor could produce cell-by-cell — reintroducing the
  per-cell host loop the lever deletes. The twin's ulp-class divergence
  is DECLARED at the definition site (`a1_ideal_march_jax.py:655-660`)
  and adjudicated by the gate at the right level: decisions bitwise,
  values in the derived Newton-floor band (measured z dev 1.5-1.7e-10
  seeds / 1.2-1.9e-11 wall vs band 6.5-7.4e-10 — 4-30x margin;
  first-offender localization exact, 208 = 205+3). This is the correct
  equivalence class for a floor-noise quantity; demanding bitwise z
  across lowerings would contradict the session's own cross-lowering
  floor finding (registry `engine:cross-lowering-gradient-floor`).

### Finding 2 — tail-repeat padding in the record executor vs P_DUM
### certified dummies in the M4 replay: the inconsistency is principled
### (padding policy tracks the consumer), and tail-repeat is close to
### the only well-posed data-only choice. **ADOPT-AS-IS**

Code: `validation/a1_toc_variational_jax.py:422-451` (`chain`:
`P[n:] = arr[-1]`, rows computed and discarded host-side, never through
`account()`); M4 dummies at `:930-944` (P_DUM certification-verified at
build, consumed by safe-where inside the differentiated replay).

The two paddings serve different consumers:

- M4 replay pads lanes INSIDE a graph that is differentiated in W;
  safe-where semantics require both branches finite under AD (O3.1 is
  the NaN-leak detector) — hence a FIXED, pre-certified,
  gradient-disconnected dummy problem. Correct there.
- M5c pads a host-discarded stack on a never-differentiated path. A
  fixed certified dummy is not even well-defined here: the scan carry
  is data-dependent, so pad row k solves
  `interior(carry = z_pad(k-1), pt2 = p_last)` — no fixed dummy operand
  can be pre-certified against an arbitrary carry. The genuine
  alternatives are (i) masking the scan body with an act-mask operand
  (`where` per cell: an extra traced branch + operand for zero semantic
  gain on a discarded region), or (ii) tail-repeat. Tail-repeat is
  minimal and safe by three checkable properties: pads sit at the TAIL
  so garbage carries cannot reach real rows; the damped Newton is
  NaN-safe by construction (`t=0` trial keeps iterates finite,
  `a1_ideal_march_jax.py:418-424`; non-finite steps read as stalled
  metric, `:455-463`), so a non-convergent pad costs at most the
  N_NEWTON cap; and discarded rows never reach `account()` or the plan
  (asserted in the docstring and enforced by the loop bounds
  `:489-496/593-608`).

Measured cost accepted with eyes open: padded frac 0.75 on both nets
(full: 7,586 real vs ~22,800 padded inner solves — ~4x redundant cell
compute) to hold single-bucket-per-phase with ZERO growth events. That
trade (compile events over compute) was adjudicated at M4
(V1b/SCAN-F3 single-bucket discipline — cited, not re-minted), and the
measured record times confirm dispatch, not compute, was the cost
(PROGRESS step 3: "padded compute = noise"). If record time ever comes
under pressure again, a second design-phase bucket is the named lever —
today there is no target pressure (M-D/M-E both MET).

### Finding 3 — host-side wall_search/axis/truncation + derived
### case-level buckets: right altitude, and the bucket bounds are
### verifiably exact. **ADOPT-AS-IS**

Code: wall_search retry loop
`validation/a1_toc_variational_jax.py:548-571`; axis cells `:624-635`;
sub-crossing discard `:602-608`; derived bounds `:469-475`.

- **Tracing wall_search** would move the (N, Nv) partner-revision
  decisions — precisely the objects the plan records and m5cgate gates
  BITWISE — into traced comparisons with data-dependent trip counts and
  dynamic gathers. The decisions would leave the audit surface; a
  decision flip would become invisible at column granularity. The
  repo's plan/replay architecture (record emits plan; replay is
  plan-fixed) requires decisions host-side; this is a structural
  argument, not taste.
- **Amdahl accounting** (full net): post-M5c host compiled dispatches
  ~ 173 chains + ~153 wall (+retries) + <=173 axis ≈ 500, vs ~7,900
  pre-M5c. The remaining host share is minority and the segment targets
  are MET with 1.5-2x margin (PROGRESS steps 4, 11). Tracing axis/wall
  cells buys no measurable target progress; it would cost the retry
  semantics.
- **Derived bounds** — I verified the arithmetic independently: fan
  column i has `len(prev) = 2i-3` partners (prev grows by exactly 2 per
  fan column from length 1), so the fan maximum `2*NI-3` is achieved,
  not merely bounded; the design bound follows from the growth
  invariant `len(newcol) <= len(prev)+1` (wall + prev[1:Nv] + cells +
  axis, `:584-643`) from the fan exit length `2*NI-1` over `n_B+Nw`
  stations. Full-net check: NI=21, n_B=93, Nw=60 -> Lpad 39/193 = the
  logged engine entries. ZERO growth events measured on both nets. The
  alternative (running-max buckets) re-triggers compilation mid-walk on
  first exceedance — the exact churn class M4 deleted; in a
  wall-clock-capped campaign, compile events are the expensive tail.
  Derived-static-bound bucketing is the standard XLA discipline, here
  with the uncommon property that the bound is proved, not padded by
  guess.

---

## Object 2 — H3 preplan/last_cert record reuse

### Finding 4 — bitwise-keyed reuse riding the M1 memo is control
### inheritance, not a coupling smell; the alternatives are strictly
### worse on this reuse pattern. **ADOPT-AS-IS**

Code: driver preplan load
`validation/a1_toc_variational_jax.py:1394-1399` under the M1 key
`_mkey` `:1370-1379` (ctx = content hash of tab arrays + cfg + closure
identity + class knobs AT REQUEST TIME, `:1191-1213`); first-hit
controls consumed on the preplan hit `:1443-1469`; `last_cert`
`:1393,1598-1599`; consumers `def_twin_falsifier.py:1080-1088`
(st_carry), `:1147-1158` (last_cert -> `cs_stats(pre=)` with bitwise
adjudication at call site and fresh-record fallback, `:602-623`);
`margin_governor.py:493-560` (same three fixes). Gate: h3gate
(`engine_speed_bench.py:958-1049`) — bit-identical (W, J, n_segments),
fresh B = fresh A - 1, cached B = cached A + 1, controls fired on the
preplan consume, last_cert bitwise with cols.

- **vs re-record-always** (pre-H3): pure waste at 5.6-8.3 s/record
  post-M5c; measured 3 records/rung -> 1 in both campaign carriers.
  No rigor is bought by recomputing a deterministic quantity whose
  reuse is gated by an empirical bitwise control.
- **vs content-hash multi-entry stores**: capacity above one is never
  demanded by the reuse pattern (the only reuse is "the just-computed
  design at a rung boundary"); a store that outlives the process would
  then be governed by the H4 code-identity rule (`record_ctx_tag`
  docstring `:1197-1200` already says so) — machinery and a staleness
  surface for zero present consumers. Right-sized as one slot.
- **The piggyback question**: pre-loading the M1 slot is the mechanism
  that makes the reuse GATED rather than trusted. The decisive detail:
  the first-hit control does not check the caller's contract on paper —
  it RE-RECORDS W fresh once and compares bitwise
  (`:1443-1461`), plus the perturbed-W key-miss control. A preplan
  produced under different engine objects/class would be caught
  empirically at first consume (and h3gate proves the controls fire on
  exactly that consume). Reuse inheriting an existing, already-refuted
  control pair is better design than a parallel new gate; the coupling
  is to a DECLARED invariant (the memo key), not to an accident.

### Finding 5 — two latent gaps in the reuse contract: probe-disarm
### combines badly with preplan, and last_cert is live references.
### **RECOMMEND-CHANGE** (priced: ~5 lines + h3gate re-run)

- (i) `probe["armed"]` honors `A1_MEMO_PROBE=0`
  (`a1_toc_variational_jax.py:1384-1385`), whose declared use is
  precisely wall-clock-capped campaigns after their first covered stage
  (`:1289-1293`) — the same campaigns H3 targets. In that combination
  the preplan consume would be UNGATED (trust-the-caller), silently
  weaker than the h3gate-covered default. Today no committed caller
  sets `A1_MEMO_PROBE=0` (grep: only the driver reads it), so this is
  latent, not live. Change: when `rec_counts["preplan"] == 1`, run the
  first-hit controls on that consume regardless of `A1_MEMO_PROBE` (the
  probe tax is one record per walk — exactly the record the preplan
  just saved, so the combination is never net-negative), or refuse
  `preplan is not None` with a disarmed probe.
- (ii) `last_cert` is returned as live refs under a comment-level
  read-only contract (`:1318-1320`). Both extant consumers adjudicate
  bitwise on W and fall back fresh (`def_twin_falsifier.py:1147-1152`,
  `margin_governor.py:547-556`), so the residual exposure is content
  mutation at equal W by a future consumer. One `copy.deepcopy` at
  walk exit (cost: microseconds against a 5.6 s record) closes it, or
  keep refs and register the contract as a registry row so the next
  consumer inherits the duty. Low severity; the change is cheaper than
  the recurring review cost of the open edge.

---

## Object 3 — H4 code-identity persistence

### Finding 6 — module-file sha256 granularity and
### numbers-not-blobs are the right points on their curves; the
### repo's own GAP-29 datum disqualifies the finer alternatives.
### **ADOPT-AS-IS**

Code: `validation/def_twin_falsifier.py:144-169`
(`RECORD_PATH_MODULES` 6 files, `code_identity`, `check_tail_code`
LOUD refusal); derive-side tail pre-registration `:917-975` (f2 refs,
bar, J_def/J_def16 + code_id); campaign-open gate + seeded stale-code
rejector run EVERY campaign `:1042-1055`.

- **vs function-bytecode identity**: disqualified by measurement, not
  style — GAP-29 (this session) proved `NEWTON_TOL_FACTOR/2` FLIPS
  `cert_verdict` (PROGRESS step 15, class B row 5): module constants
  are verdict-load-bearing, and constants are referenced by name from
  bytecode, so a constant edit would FALSE-ACCEPT under bytecode
  hashing. A staleness identity that cannot see the one knob a
  measured flip hangs on is unsound for this codebase.
- **vs AST-normalized hash**: would spare a derive re-run on
  comment-only edits of 6 files. Price of the current choice: minutes
  of re-derive per comment edit; price of the alternative: a
  normalizer + a new subtle failure class in the identity itself. The
  repo's declared error-preference (loud false refusal over any silent
  false accept, the S24 C5 scenario) makes false-refusal the CHEAP
  error; right-sized as-is.
- **vs git commit identity**: disqualified twice — this workflow runs
  with dirty trees as the norm (the branch's standing git status), and
  whole-repo granularity would stale the tail on every doc edit.
- **Pre-registered NUMBERS vs record blobs**: the campaign consumes
  exactly six floats + cert_n (F3/F7 references); blob persistence
  would add MB-class artifacts, load/validate machinery, and its own
  staleness surface, against a 5.6 s re-record price (PROGRESS step 6
  declares this right-sizing with the price named). The tail comparisons
  run against instance-derived bars (`bar_f2d`, K_RICH bands), not
  bitwise floats, which is the correct consumption semantics for
  floor-noise quantities. The seeded rejector executed at EVERY
  campaign open (not once at landing) is the strong form of the
  mutation-test discipline. Verified: derive re-run reproduces the S24
  tail (f2 1.4972e-02 < bar 2.0137e-02, `s25bis_derive_h4_run1.log`).

### Finding 7 — the identity omits the ENVIRONMENT, and the module
### list is hand-declared with no closure check; the session's own
### centerpiece finding says the environment IS lowering identity.
### **RECOMMEND-CHANGE** (priced: ~4 lines + one derive re-run)

Quantitative argument: the cross-lowering floor row (registry
`engine:cross-lowering-gradient-floor`) measures that ANY re-lowering
of the same Python source moves gradients ~1e-8 rel and (at marginal
cells) flips verdict-class quantities
(`record-path:cert-verdict-recorder-dependence`: 3.757 vs 0.585 across
recorders). A jaxlib/XLA upgrade is a re-lowering of every kernel in
the record path with the SAME `code_identity`; a numpy change is an
ACTIVE named near-future event (BLOCCATO O5: numpy 2.5.2 decision at a
session boundary). The likely failure mode is the bad one: tail values
are value-class stable (~1e-15), and f2 sits at 34% headroom under its
bar — so an env flip would most plausibly pass SILENTLY with moved
numbers, which is exactly the staleness class H4 was built to refuse
(C5-by-code then; C5-by-environment next). Change:
`h.update(jax.__version__ / jaxlib version / numpy.__version__)` in
`code_identity()`, re-stamp with one derive run. Secondly: the 6-module
list is correct TODAY (I traced the tail closure: `rung_logs`/`cs_stats`
-> TV/O33/A1/SC/TH only; `locus_diagnosis`/`margin_governor`/
`adaptive_knot_optimize` are imported by def_twin but do not feed the
tail) — but nothing enforces the list tomorrow; a one-line assertion or
a registry note naming the closure rule ("any module the tail path
imports must be listed") converts a hand-invariant into a checked one.

---

## Object 4 — M6 batched FD Hessian + the cross-lowering floor

### Finding 8 — the acceptance criterion (dH <= K_RICH x max scheme
### self-asymmetry) is the right consumer-level semantics for a
### floor-dominated FD Hessian; the alternatives are either circular,
### state-dependent, or scale-blind. **ADOPT-WITH-CAVEAT**

Numbers of record (`s25bis_m6diag.log`, `s25bis_m6fix.log`): H scale
4.175e7; sequential self-asymmetry 1.229e6 (2.9e-2 rel); batched
7.582e5; mixed-base dH 7.583e6 (18.2%, 6.17x asym — gate-rejected);
corrected in-batch-base dH 2.063e6 = 1.68x asym, inside
K_RICH x max(asym) = 4 x 1.229e6 = 4.92e6.

Why the criterion is right HERE (a derived, not aesthetic, argument):
on this objective the FD Hessian error budget is NOISE-dominated, not
truncation-dominated. Check: the same-lowering evaluation noise between
neighboring stencil points is the input-decorrelated part of the
gradient floor, delta_g ~ 1.1e-8 x g_scale(2.0e6) ≈ 2.2e-2; the induced
per-entry Hessian noise ~ sqrt(2) x 2.2e-2 / h (h = sqrt(EPS) x scale ≈
1.49e-8) ≈ 2.1e6 — the measured sequential self-asymmetry 1.229e6 is
this same class (within 2x, norm-dependent). So `asym` is not a proxy
for truncation; it IS the empirically available measurement of the
irreducible floor of the scheme at this design, and the criterion reads
"the cross-scheme residual after common-mode cancellation must be
noise-class, not bias-class". The corrected form's 2.06e6 vs the SUM of
the two schemes' own asymmetries 1.99e6 confirms no anomalous excess
remains. Symmetrization removes exactly the antisymmetric error part;
for decorrelated entry noise the symmetric part is same-order, and
K_RICH = 4 covers it with ~2x to spare.

Alternatives adjudicated: (i) eigenvalue/spectral bounds — require a
reference Hessian better than FD, which does not exist on this path
(jacfwd is blocked, see Finding 11): circular; (ii) TR-step-agreement —
the most consumer-faithful test but state-dependent (radius, gradient,
active constraints), hence weak as a reproducible GATE; (iii)
Wolfe/rho model-quality ratios — measure model adequacy over a TR step,
which is dominated by the quadratic-approximation error orders above
this floor: scale-blind, would never discriminate. CAVEAT (the priced
half): at F2 adoption, add a one-shot TR-step-agreement spot check
(solve the TR subproblem once with each Hessian at matched radius,
compare steps against the radius scale) as addendum evidence — one
subproblem solve, no new machinery; and the re-formed m6gate must pin
the NORM of dH/asym (max-abs vs Frobenius) in its text. Note also that
K_RICH=4 is applied here by convention-reuse; GAP-29 just demonstrated
that inherited factors can be load-bearing — the registry's F2
derivation candidate (chain-amplification bound, row
`engine:cross-lowering-gradient-floor` owner) already covers this; no
new row needed.

### Finding 9 — the ~1e-8 rel cross-lowering floor is NUMERICALLY
### EXPECTED for this chain; the measured numbers close arithmetically,
### and the controls exclude the defect classes that could mimic it.
### **ADOPT-AS-IS** (adjudication of record sound; three cheap scaling
### experiments named for the already-owned F2 derivation row)

The expert quantitative argument, with the session's own numbers
(`s25bis_m6locus.log:5-8`, g_scale 2.002e6):

1. **Per-cell input**: across lowerings, each implicit solve's z is
   pinned only to the while_loop termination band
   `NEWTON_TOL_FACTOR x EPS x sc ≈ 2.2e-14 x sc`
   (`a1_ideal_march_jax.py:444-448`); at marginal cells even the trip
   count and damped-trial path may differ (mechanism demonstrated by
   the recorder-dependence catch, registry row, cert ratio 3.757 vs
   0.585 from ulp seeds — O(1) amplification of the METRIC at one
   near-non-convergent cell). Batched vs single 4x4 `linalg.solve` in
   `bwd_solve` (`:475-481`) adds reassociation at the same few-ulp
   class.
2. **Chain amplification**: the primal chain's measured amplification
   is ~1e4 (replay-fidelity class: 3e-11 wall dev from 1e-15 seeds —
   convergence-map class B row 6). Adjoint chains differentiate the
   amplifying coefficients (1/(u^2-c^2), tan(theta±mu) with 1/cos^2
   blowup near the axial-margin boundary), generically adding 1-2
   orders at near-margin cells over ~250 solves. Envelope: 1e-10..1e-7
   rel on g. Measured: base 1.09e-8, eager-vs-jit 1.43e-8, B=9-vs-B=1
   3.0e-8, perturbed lanes 5.6e-8 — inside the envelope, at its upper
   half, consistent with cert-marginal cells being present.
3. **Internal closure** (the overdetermination): FD amplification
   1/h ≈ 6.7e7 ("~7 orders" is exact arithmetic, not rhetoric);
   predicted mixed-base dH ≈ per-lane dev/h = 1.13e-1/1.49e-8 = 7.6e6
   vs measured 7.583e6; predicted corrected-form residual = the two
   schemes' decorrelated floors ≈ 1.99e6 vs measured 2.06e6; values at
   2.2e-7 on J ~ 4e7 = 5e-15 rel (value-class, as claimed). Every
   number closes to <2x through elementary error propagation.
4. **Defect exclusion**: the lane-permutation control BITWISE
   (`s25bis_m6fix.log:6`) kills cross-lane contamination — the genuine
   vmap defect class (batch-index leakage, in_axes errors). The
   eager-vs-jit datum (2.9e-2, SAME order with no vmap anywhere) kills
   vmap-specificity. Values at 5e-15 kill primal-side defects. What the
   A/Bs cannot exclude: a COMMON-MODE defect in the custom_vjp (e.g.
   the IFT adjoint's neglect of the residual of an inexactly-converged
   z) — but that term is bounded ~kappa_cell x NTF x EPS ≈
   1e-12..1e-10 rel, below the floor, identical in both arms (hence
   irrelevant to the batch-vs-sequential question), and absolute
   gradient truth is O3.1's jurisdiction, which re-passed
   (1.13e-2 <= 7.69e-2). The floor cannot plausibly hide a batching
   defect; the adjudication "the defect was the mixed-lowering
   FORMULATION, not the batching" is supported at every measured point.

Experiments that would settle "expected" to "derived" (they belong to
the registry row's existing F2 owner — sharpening, not re-minting):
(a) N-scaling: run the locus probe on truncated nets (NI/Nw ladder);
a rounding floor grows ~N^alpha, alpha in [1/2, 1]; (b)
margin-scaling: a design with larger min_margin should lower the
floor (tests the near-margin amplifier directly); (c) precision
scaling: under float32 the floor must scale ~1e8 x with u — a logic
defect would NOT scale. All three use existing knobs.

### Finding 10 — pin-one-lowering as standing discipline is the exact
### correlated-noise rule from noisy-FD practice, with one sharpening
### the data itself supplies. **ADOPT-AS-IS**

The corrected in-batch-base form (base = lane 0 of the SAME batch, one
compiled executable) implements structurally the classic rule for
differencing noisy computations: difference only evaluations sharing
the same noise realization structure (common-random-numbers principle;
noise-aware FD practice à la Moré-Wild). The m6locus (b2) datum — B=9
vs B=1 lane0 differ 6.0e-2 — supplies the sharpening the discipline
must carry: BATCH SHAPE is part of lowering identity, so "one
lowering" means one compiled executable AND one batch shape; the
in-batch-base form satisfies this by construction, a
"batched rows + separately-batched base" form would not. The registry
row (`engine:cross-lowering-gradient-floor`, owner text) already
states the discipline; the B-shape clause is worth one line there at
F2 corpus seeding.

### Finding 11 — sequential-with-guards as default, adoption deferred
### to a session boundary with the gate re-formed: correct under the
### version-change discipline; two route facts must be priced into F2
### so the re-adjudication buys the right lever. **ADOPT-WITH-CAVEAT**

The deferral is right on the numbers: the sequential block runs
4.5-7.0 s <= 8 s target (no pressure; STOP-WHEN-MET), the batched form
is a declared version change (batched XLA reduction order != sequential
at floor order), and the M3 precedent (adoption at session boundary
with the gate re-formed) is the repo's own ratified pattern. The rigor
half shipped regardless (nonfinite-lane guard + `hess_lane` counter on
the sequential blocks which had NONE,
`a1_toc_variational_jax.py:1693-1700, 1746-1752`; honest separate
ledger row `n_eval_batch_lanes` `:1388-1392` — correctly NOT folded
into n_eval) is a genuine REQ-NONSTALL strengthening independent of
adoption. Caveats for the F2 entry: (i) central differences are NOT an
upgrade path here — Finding 8 shows the budget is noise-dominated, and
central differencing halves truncation while leaving the floor intact
(it would double cost for no floor gain); (ii) the named jacfwd route
(N5, exact forward-over-reverse Hessian) is blocked as written:
`solve` is `custom_vjp`-only (`a1_ideal_march_jax.py:504-517`), and
custom_vjp functions are not forward-differentiable in jax — N5's true
price is writing the implicit-JVP rule (custom_jvp with the same
tangent solve), which should be stated in the F2 row so the route is
costed honestly; (iii) the re-formed m6gate must gate on the corrected
criterion (in-batch base mandatory; dH bound = K_RICH x max scheme
asym) and KEEP the corrupted-lane control — the current gate's
gradient-level band (sqrt(EPS) x g_scale) did its job (it fired) but is
superseded by the Hessian-level criterion for the corrected form.

---

## Object 5 — single-author instruments

### Finding 12 — the per-file two-sided count ratchet is the strict
### form of the standard lint-adoption pattern; the declared limit is
### real and correctly declared. **ADOPT-AS-IS** (one doc-count nit)

Code: `tests/test_numeric_lint.py:23-39` (tier docstring),
`validation/numeric_lint_baseline_validation.json` (33 files, sums to
622). Against the alternatives: full classification NOW of 622 legacy
literals would be either days of work displacing the session's
levers or a fake (bulk-allowlisting without provenance — worse than no
channel); suppress-lists (per-line pragmas) rot and make suppression
the path of least resistance. The ratchet closes the CHANNEL (no new
magic number enters `validation/` silently) at baseline == reality:
the two-sided form (a DECREASE also fails until the baseline is
lowered) is the strict variant — one-sided ratchets drift stale — and
the unbaselined-file rule closes the new-file hole. The +1-bump seeded
rejector firing every run is the right mutation-test. The declared
limit (within-count swaps pass) is honest: this is a channel guard,
not a classification; the classification stays the named F2 duty
(registry row `test-suite:numeric-lint-scope-hole` — cited, owned).
Nit: the docstring says 621 (`tests/test_numeric_lint.py:27`), the
baseline JSON sums 622 (matching the commit of record) — one-line doc
fix under R5 number discipline.

### Finding 13 — the findings-registry schema + machine anti-re-mint
### rule mechanize a failure mode this repo actually measured; the
### line-span anchors are the one maintenance liability.
### **ADOPT-WITH-CAVEAT**

Code: `docs/findings_registry.yaml` (17 rows);
`tests/test_findings_registry.py:1-60` (schema; per-status required
fields OPEN -> owner+trigger / CLOSED -> evidence; anchors MUST
resolve; overlap rule; 4 seeded rejectors). Lineage: the field set
(id/status/severity/magnitude/source-anchor/code-span/mechanism/
owner/trigger) is SARIF-class finding metadata plus the repo's own
structurally-gated-postponement directive encoded as lint (owner+
trigger REQUIRED on OPEN rows — the never-postpone-resolvables rule
made machine-checkable). The anti-re-mint overlap rule (two OPEN rows
on one code span = violation) has no mainstream lint counterpart I can
cite; its justification is measured, not aspirational: the throat-panel
sliver was re-coined with a contradicted magnitude and caught only by
a refuter's dedup clause (CONVERGED advisory §1 — the demonstrator).
Strict-subset schema shared with the claims registry = one parser,
reused. CAVEAT: `code:` line-ranges drift under refactor; the
must-resolve check catches file/anchor breakage but NOT silent line
drift (a span that still parses now covering different code would
false-negative the overlap rule). At the F2 corpus seeding (the named
first duty, ~180 rows incoming), prefer symbol anchors or short
content snippets for high-value rows; priced at the seeding pass
itself, zero extra sessions.

---

## Convergence table

| # | Finding | Verdict | Needs judge? |
|---|---------|---------|--------------|
| 1 | M5c scan-of-while_loop + in-trace seeds | ADOPT-AS-IS | no (structural + measured) |
| 2 | M5c tail-repeat vs P_DUM | ADOPT-AS-IS | no (consumer-tracked policy, derived) |
| 3 | M5c host decisions + derived buckets | ADOPT-AS-IS | no (bounds re-derived here, match logs) |
| 4 | H3 reuse mechanism via M1 memo | ADOPT-AS-IS | no (control-inheritance verified in code) |
| 5 | H3 probe-disarm x preplan; last_cert refs | RECOMMEND-CHANGE | no (mechanical, ~5 lines) |
| 6 | H4 file-hash granularity + numbers-not-blobs | ADOPT-AS-IS | no (GAP-29 datum disqualifies finer) |
| 7 | H4 environment fingerprint + closure check | RECOMMEND-CHANGE | no (mechanical, ~4 lines + re-derive) |
| 8 | M6 acceptance criterion | ADOPT-WITH-CAVEAT | no (derivation given; caveat absorbs the contestable half) |
| 9 | M6 floor expected | ADOPT-AS-IS | no (overdetermined by measured closure; experiments named on the owned row) |
| 10 | pin-one-lowering discipline | ADOPT-AS-IS | no (B-shape clause = one registry line) |
| 11 | M6 sequential default / deferred adoption | ADOPT-WITH-CAVEAT | no (route facts are checkable: custom_vjp is not fwd-differentiable) |
| 12 | validation count ratchet | ADOPT-AS-IS | no (pattern + rejector verified; 621/622 nit) |
| 13 | findings-registry schema + anti-re-mint | ADOPT-WITH-CAVEAT | no (span-drift priced at seeding) |

No judge round requested: every verdict is either measured-anchored or
priced-trivial (orchestration-weight right-sizing, declared).

## Declared drops (seen, deliberately not minted): 7

1. `invert_h` A5 fence + `get_solver` 4-tuple docstring — CONVERGED
   §4.4 half-nit repairs, verified landed; nothing to adjudicate.
2. GAP-29 sweep + notaknot twin design — rigor probes outside the
   four-lever + instruments perimeter; verdicts live in their registry
   rows.
3. m0/m12gate/m5gate `A1_COLEXEC=0` attribution pins — bookkeeping,
   correct by inspection.
4. Recorder-dependence semantics (ACTIVE recorder = authority) —
   registry row with a registered per-cell demo duty; cited, not
   re-adjudicated.
5. "bitwise-class" wording for M6 values (measured 5e-15 rel = few-ulp,
   not literally bitwise) — wording only; the logs carry exact numbers.
6. M-D/M-E variance (14.9 vs 20.1 s) — registry row
   `bench:speed-measurement-variance`, owned.
7. margin_governor H3 mirror — same mechanism as def_twin's, reviewed
   as one object (Finding 4), not double-counted.

---

**13 findings: 8 adopt / 3 caveats / 2 changes / 0 open**
