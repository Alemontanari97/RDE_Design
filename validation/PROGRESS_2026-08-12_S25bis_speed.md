# SESSION LOG — S25-bis "M5c + M6 + CAP PROTECTION" (2026-08-12)
# Branch rde-nozzle-program, opening HEAD ad5c48e (the S25
# post-closure addendum — verified mine/expected; no foreign
# commits). Census row R30. One session; decisive-run cap 3 h;
# STOP-WHEN-MET at the pessimistic end of the MEASURED band.

## STEP 1 — OPENING (R2) + PRE-EXECUTION GATE (logged verdict)

RESTART DECLARATION: S25-bis opens post-S25 (C4 closed; M0-M5a/b
gate-accepted; record 100.84 -> 32.09 s; honest counter SEGMENT
~46 s NOT-MET without M5c / CAMPAIGN 18-23 min MET-central), the
NAMED completion session of the speed program (census R30), before
F2 GENERAL ENGINE.

MANDATORY READINGS PERFORMED: memories s25-engine-speed,
pipeline-sense-expert-review (incl. 3-bis convergence-mandatory),
orchestration-weight-sota, choice-adjudication-convergence,
never-postpone-resolvables, agentic-orchestration-forms; S25 log
(full); PROGRESS ORA + census DELTA S25 (R28-R31, BLOCCATO 8);
DISPATCH_Sspeed_to_S25 + ADVISORY_engine_speed_audit §4 (M5/M6) +
§5 + §6 (verbatim); CONVERGENCE PACKAGE verified ON DISK:
ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md read in full —
the judge had ALREADY been run in the post-closure window (commit
ad5c48e), so T1(a) reduces to absorption; repairs (1b) verified AT
SOURCE ([S25-REPAIR] x7 in the gap map, R6 exact comment at
thermotab:670, C-A edge scoping at :534-546, zero bare asserts in
the bench).

WORKING-TREE NOTE: data/q_mapping.{json,md} carry a pre-existing
regenerated-timestamp-only diff (2026-07-16 -> 2026-08-12, content
identical) — NOT ours, NOT committed (declared, left in place).

PRE-EXECUTION GATE VERDICT (gate-pre-esecuzione): every duty maps to
R30/R28/R31 or a CONVERGED §6 row (R1 no orphan step) — PASS.
Binding terms re-declared: baseline = the COMMITTED [X-SPDB]
artifacts (no re-baseline; pycount discipline holds); M5c/M6 =
DECLARED version changes gated on their executable gates + O3.1 +
the closing suite; triple proof per lever; every consumer run
EXIT-code gated, redirect-only; FREEZE on tracked-file edits while
a consumer chain runs (S25 lesson — held all session, enforced
twice); fallback M5c -> H2 -> N1 at cost caps.

## STEP 2 — T1 ABSORPTIONS (pre-executed in the addendum window;
## verified + absorbed here)

Per-claim rows of the CONVERGED verdict absorbed as filed: sliver =
ONE fused object == audit row objective-omits-throat-panel (MEDIUM,
gradient-axis magnitude governs, [OBJ-DOM] F2-entry owner);
R1 adopted-weakened; R2 ceiling carrier ADOPTED -> named F2-entry
row (NOT built here, per mandate); R3 rescoped ([T3-QS] carrier
exists; Q3(a-c) -> F5-entry); R4 refuted-as-filed -> partition of
record; impl 0-MISMATCH ratified; [G1-DISC] adopted (F2). Open rows
all owner+trigger — nothing to relitigate. The residual S25-bis
micro list executed this session: invert_h K_NEWT fallback fence
(thermotab), NOTE-5 get_solver 4-tuple docstring repair (A1);
optional m12-F4 def_twin wiring DECLINED (option, not duty —
declared).

## STEP 3 — T2 M5c THE CENTERPIECE: per-column compiled record
## executor — ACCEPTED FIRST-PASS ON BOTH NETS

DESIGN (advisory M5c F6-AMENDED verbatim, all pins honored):
- A1.predict_interior_t: TRACED expression-twin of the host
  predictor (in-trace seeds; np.tan/hypot vs XLA lowering = DECLARED
  ulp-class divergence; y2=0 GENO guard as double-where).
- Driver _col_executor: hoisted module-level jit of a lax.scan over
  the column's interior cells — the fused solve_cert INLINED
  (expressions verbatim), per-cell (z, step, scale, margin) returned
  as stacks; engine cache id-keyed with strong refs (M4 pattern;
  interior cells read NO class global — class enters through the
  operands).
- cell()/account() refactor: ONE shared host accounting (cert ratio,
  abort first-offender, argmax/margin bookkeeping, raise sites) for
  BOTH record paths — the per-column path host-checks the stacks
  with the SAME bound, semantics and ordering (cert before margin).
- Python keeps EVERY adaptive decision at column granularity:
  wall_search, axis cells, truncation, all raises host-side;
  sub-crossing discards computed speculatively and DISCARDED (never
  accounted, never in the plan). Eager cell_scan stays REJECTED.
- Bucketing: single bucket per phase at DERIVED case-level bounds
  (fan 2NI-3 exact; design 2NI-2+n_B+Nw from the column growth
  invariant) — ZERO running-max growth events, churn tied to
  (NI, Nw, n_B) exactly like the M4 engine (V1b honored); padded
  lanes tail-repeat the last real partner (data-only).
- A1_COLEXEC=0 = legacy per-cell arbitration path; axial-margin
  raise text now carries the offending cell index (additive schema
  note, needed by the seam control).
- attribution pins added: m0/m12gate pin A1_COLEXEC=0 (their
  committed baselines/properties are per-cell-path); m5gate pins it
  too (host-dispatch doctored control).

GATE m5cgate (NEW bench mode; can REJECT -> H2 -> N1) — **EXIT 0,
FIRST PASS, BOTH NETS** (s25bis_m5cgate_run1.log, artifact
s25_spdb_m5c.json):
- dec-vector BITWISE identity (n_B, per-fan n, per-design
  (N, Nv, n, has_axis), cert_n) on defnoz-mild AND defnoz-full —
  every wall_search / truncation / axis decision identical,
  truncated columns included;
- z inside the driver Newton-floor band: wall dev 1.18e-11 (mild) /
  1.91e-11 (full) vs band 6.52e-10; seeds 1.70e-10 / 1.48e-10 vs
  7.4e-10; min_margin dev 2.4e-11 / 0.0;
- certification VERDICT agrees (mild 0.686 vs 0.701; full 0.404 vs
  0.423 — the ratio itself is floor-noise, reported not gated);
- doctored-cell THROUGH the executor stacks: typed refusal with
  first-offender localization EXACT (aborted_at_cell 208 ==
  chain-start 205 + row 3);
- near-seam margin-floor pair (derived delta): floor_hi -> SAME
  raise cell (0 == 0) in both recorders; floor_lo -> both complete.
- measured: full record per-cell 17.54 s -> colexec 5.66 s warm
  (3.10x; first incl. compile 10.19 s); 173 chains, 7586 cells,
  padded frac 0.75 (padded compute = noise, dispatch was the cost).

## STEP 4 — MEASURE M-D = STOP CHECK 1: **SEGMENT MET**

bench md (defaults ON, clean host pycount=1, artifact
s25_spdb_md.json): record fresh median 5.58 s [5.50, 5.58, 8.30]
(vs M0 100.84 = 18.1x; vs M-C 32.09 = 5.8x); C1 replay steady
0.236 s; val_grad steady 0.449 s; Hessian block estimate 4.5 s;
segment synthesis post-M1: **central 11.8 s / pessimistic-end
14.9 s vs target <= 30 s -> MET AT THE PESSIMISTIC END** (margin
2.0x, worst-rep criterion). Campaign projection (§5 shapes,
21-segment rung): segments ~4.1-5.2 min + boundary (H3) + tail (H4)
+ compile set -> **<= 25 min MET across the band**. The advisory
counterfactual "callback record alone > 30 s without an L5-class
lever" is now CLOSED by M5c (the F6-amended executor IS the
L5-class lever; N1 not triggered).

## STEP 5 — M6 ADJUDICATION OF RECORD (two rulings, honest sequence)

(i) At M-D the STOP-WHEN-MET rule fired: segment MET -> M6 (a
speed-only item by the advisory's own words) NOT implemented BY
RULE — declared, not dropped.
(ii) USER ORDER (in-session, 2026-08-12): "non droppare ciò che è
realmente SOTA implementativo... tutto ciò che è overengineering ok
tenerlo fuori, ma tutto il resto implementiamolo se è realmente
miglioria, generalizzazione, efficienza" -> M6 RE-ADJUDICATED and
RE-ENTERED on the merits: prerequisite (M4) landed; measured gain
class known (2.6x); a REAL RIGOR co-benefit (the sequential FD
block had NO nonfinite-lane guard — the batched path adds per-lane
fallback + counter, REQ-NONSTALL strengthened); concrete scaling
consumer (F2 richer classes grow n; the batch pattern is H5's and
multistart's template). The remaining items stay OUT with named
owners exactly BECAUSE the user's criterion excludes
overengineering: H2 (fallback role moot after M5c acceptance;
trigger = measured wall_search share if ever thin), H5 (consumer +
band inputs are F2's falsifier families), O1/O2/O4/N8 (named
triggers not fired), O5 (env change = session-boundary user
decision, BLOCCATO class). NOTHING lost: every row keeps its
owner+trigger in the census/advisory/findings registry.

M6 IMPLEMENTATION (declared version change): vg_batch=True entry in
make_run_toc_scan_jit — jit(vmap(value_and_grad)) of the thrust
objective with plan arrays as broadcast OPERANDS (in_axes=(0,None)),
cached in the SAME M4 engine cache (mode "vgb") => zero per-segment
recompile (a constants-closed vmap wrapper would have re-baked the
plan per segment — the exact churn class M4 deleted; binding order
honored). Driver: Jacobi 2n block + measured-Hessian n block run as
ONE batched dispatch each (same stencil, same derived steps, same
symmetrization — WHO executes changes); module-level vg_batch_rows
helper with per-lane nonfinite fallback to the sequential compiled
eval + hess_lane counter; separate honest ledger row
n_eval_batch_lanes (a B-lane batch is ONE dispatch, never folded
into n_eval); A1_VMAP_HESS=0 = sequential arbitration path
(verbatim legacy loops).

## STEP 6 — T4 H3 + H4 (cap protection, BINDING pre-campaign)

H3 (campaign rung-boundary dedup, 3 files):
- driver run_trsqp: preplan=(out, plan) pre-loads the M1 memo slot
  (the seg-0 duplicate record becomes a memo hit; the EXISTING M1
  first-hit controls — fresh-record bitwise equality + perturbed-W
  miss — ARE the H3 "bitwise on reuse" gate); field_records=True
  makes in-walk records carry cols; result gains last_cert =
  dict(W, out, plan) (refs, read-only) + record_preplan counter.
- def_twin stage_campaign: C3 repeat and next-rung reuse st_new as
  st_cur (bitwise-keyed on W, fallback = fresh record); the walk
  consumes st_cur as preplan; rung-end cs_stats reuses the walk's
  last certified field-record (cs_stats gains pre=).
- margin_governor campaign: same three fixes (rung-start carry,
  preplan, O4-log reuse) — 3 records/rung -> 1.
GATE h3gate (NEW bench mode) — **EXIT 0**: bit-identical (W, J,
n_segments) between the preplan and no-preplan arms; record_preplan
== 1; fresh B == fresh A - 1; cached B == cached A + 1; M1
first-hit controls fired on the preplan consume; last_cert bitwise
at the returned W with cols.

H4 (tail-to-derive + CODE-IDENTITY persistence):
- def_twin: code_identity() = sha256 over the 6 record-path modules;
  stage_derive now computes and PRE-REGISTERS the ladder-invariant
  tail (F3 GENO-side f2 refs from the EXISTING st0 — intra-tail W0
  duplicate KILLED; J_def replayed from st0's own plan — no fresh
  record; W16 records ONCE in derive; bar_f2d) into the derive
  artifact under tail.code_id; stage_campaign consumes the refs
  ONLY under check_tail_code (stale code = LOUD RuntimeError
  refusal) with the SEEDED stale-code rejector (corrupted code_id
  MUST refuse) run at every campaign open — the S24 C5
  staleness-by-code scenario replayed as the acceptance control;
  pre-H4 artifacts = declared legacy fallback (tail in-campaign).
- DECLARED right-sizing (orchestration-weight): raw (plan, record)
  BLOB persistence across processes intentionally NOT built — a
  post-M5c record costs 5.6 s while the blob machinery would add
  its own staleness surface; H3's last_cert/preplan IS the
  (plan, record) persistence within a process; the pre-registered
  tail numbers ARE the cross-stage persistence that protects the
  cap.
EXERCISE — **stage_derive EXIT 0** (s25bis_derive_h4_run1.log): the
pre-registered tail REPRODUCES the S24 in-campaign numbers exactly
(f2_geno 1.4972e-02 vs bar 2.0137e-02 — the S24 record's own
figures), J_def 4.0262479e+07 / J_def16 4.0263825e+07, code_id
stamped; [X-DEFTW] derive-stage exercised fresh on today's tree.

## STEP 7 — FROZEN-CODE RE-CHAIN 1 + the TWO honest catches

Chain (sequential, redirect-only, EXIT-gated): h3gate PASS ->
m5cgate PASS -> m12gate **FAIL (real catch #1)** -> m4gate PASS ->
m5gate PASS -> notaknot **FAIL (real catch #2)** -> gap29 PASS ->
derive PASS.

CATCH #1 — cert-verdict RECORDER DEPENDENCE at a marginal design
(finding of record, registry row
record-path:cert-verdict-recorder-dependence): walk_start ran with
the DEFAULT recorder (colexec) while the gate arms pin the per-cell
path; at the cert-MARGINAL Wp (mild net) the recorders land on
OPPOSITE sides of the bound — per-cell 3.757 (FAILS, exactly as in
S25: "Wp NOT certified at this net") vs per-column 0.585 (passes).
NO legacy regression (per-cell behavior unchanged vs S25); ulp seed
differences amplified through the damped-trial selection of a
near-non-convergent cell. REPAIR: attribution pins moved BEFORE
walk_start (start selection uses the SAME recorder as the arms);
SEMANTICS OF RECORD declared in the driver docstring: the ACTIVE
recorder is the certification authority, a walk never mixes
recorders, cross-path adjudications pin ONE recorder.

CATCH #2 — my first notaknot rejector was MIS-FORMED and its own
firing refuted it (the R6/R-GRAD control-re-derivation lesson,
third instance): demanding corner-density invariance is wrong
because cd is computed ON the design and the BC change moves the
lip state BY THE MECHANISM UNDER TEST (8.2% shift = the mechanism
datum). RE-FORMED: two-resolution DELTA-STABILITY rejector
(|delta_r1 - delta_r2| <= K_RICH x max arm spread — a
resolution-unstable delta = mesh artifact = REJECT) + the
artifact-fixed GENO reference untouched by construction.

## STEP 8 — T5 RIGOR PROBES: two measured DATA of record

GAP-29 halved-constants sweep (AUDIT:426 EXECUTED at last; 4
subprocess arms base/ntf50/cfloor4/cops50; s25bis_gap29_sweep.json)
— **1 FLIP of record**: NEWTON_TOL_FACTOR/2 flips the mild-net
record cert_verdict (the factor-2 margin is LOAD-BEARING on
certification -> the derivation duty is LIVE, owner F2 per ledger
C18); C_FLOOR/2 and C_OPS/2: NO flip on any row (>= 2x measured
headroom documented); derived K_NEWT responds to its floor input as
designed (expected behavior, not a flip).

GAP-5 notaknot-twin (one-row BC twin at W*8, re-formed rejector;
s25bis_notaknot_twin.json) — **the corner residual of record is
mostly BC bias**: baseline reproduces the S19 figure to 5 digits
(6.629466e-02 vs 6.6295e-02 — the M3 closure left it intact), the
not-a-knot row drops it to 1.166e-02 (r=1, -82%) / 9.775e-03 (r=2);
delta two-resolution stable; cd (lip-state) shift 8.2% = the
mechanism datum. CONSEQUENCE ADJUDICATION = F2 (incumbent BC
untouched, gap-map rigor note honored) — but the "design-class
limit" reading of the S19/S20 corner residual now has a CONFIRMED
named alternative mechanism carrying ~5.7x of the signal.
DECLARED HAZARD caught while building the twin: a monkeypatched
spline is INVISIBLE to the M4 engine-cache key (code identity
covers processes, not in-process patching) — caches cleared between
arms in the probe; noted as a test-only hazard.

## STEP 9 — T5-bis R31 FINDINGS-AS-CODE + R28 RATCHET (landed)

R31: docs/findings_registry.yaml (strict-subset schema shared with
the claims registry) + tests/test_findings_registry.py = run_all
group (xix). 14 seeded entries hand-verified (the throat-panel
demonstrator with its re-mint note; GAP-29/GAP-5 with today's
measured magnitudes; [G1-DISC]; C-A + R6 + C4 DISCHARGED with
evidence; scope-hole; filelock + [P-TRFLOOR] conditionals;
delta-carrier + Q3 F-entries; recorder-dependence; GAP-30 twin).
Lint enforces: status/severity enums, per-status required fields
(OPEN => owner+trigger, CLOSED => evidence), source anchors RESOLVE,
and the RE-MINT rule (two OPEN entries overlapping one code span =
violation) — 4 seeded rejectors fire every run. DECLARED SPLIT
(budget honesty): the full corpus seeding (audit 94, gap-map
36/16/10, ledger 45, refuter/red-team) = THE NAMED FIRST DUTY of
the next session (mechanical find->verify, low-effort agents) —
never generic.

R28: test_numeric_lint gains the validation/ RATCHET TIER — per-file
frozen baseline (numeric_lint_baseline_validation.json: 33 files,
621 legacy literals MEASURED and declared), any count INCREASE
fails (a new magic number cannot enter validation/ silently), any
decrease fails until the baseline ratchets DOWN (baseline == reality
always), unbaselined file fails; seeded +1-bump rejector fires every
run. DECLARED LIMIT: within-count literal swaps pass — the ratchet
is a CHANNEL guard; per-file classification stays the F2-entry
hygiene duty (registry row). Both lints PASS with all rejectors
firing.

## STEP 10 — CHAIN 2: THE M6 GATE FIRES (the honest rejection of
## record) + repairs verified

CHAIN 2 (sequential): m6gate FAIL -> m12gate re-run PASS (pinned
walk_start repair works: Wp refused by the arm recorder, W0
fallback, gate green end-to-end) -> notaknot re-run PASS (re-formed
delta-stability rejector: |d1 - d2| = 1.95e-3 <= 7.52e-3; the -82%
datum stands) -> bench me PASS.

**M6 GATE VERDICT (m6gate FAIL = the gate doing its job)**:
per-lane batched grad dev 1.130e-01 vs FD-truncation band 2.98e-02
(values bitwise-class: 2.0e-07 on J ~ 4e7); corrupted-lane control
PASS (recovery bitwise + counted); O3.1 PASS; speed 2.14x measured
(4.69 -> 2.19 s). CONSUMER-LEVEL DIAGNOSTIC (s25bis_m6diag.log,
bounded — no unbounded debugging): dH(batched vs sequential) =
7.6e6 = **18% of the Hessian scale = 5-6x the scheme's OWN
asymmetry error** (1.23e6) — the batched adjoint through the
replay's implicit-solve chain (batched 4x4 linalg in the custom_vjp
backward) is NOT FD-Hessian-grade. ADJUDICATION (per the user's own
criterion — real improvement yes, overengineering no, and NEVER
correctness for un-needed speed): **M6 REJECTED AS DEFAULT**;
sequential stays the path of record (block 4.5-7.0 s <= 8 target);
the candidate stays runnable (A1_VMAP_HESS=1) with the F2
re-adjudication routes named (adjoint-divergence source isolation;
jacfwd N5); the RIGOR half is KEPT regardless — nonfinite-lane
guard + hess_lane counter added to the SEQUENTIAL FD blocks (which
had none). Registry row engine:vmap-hessian-adjoint-divergence.

## STEP 11 — MEASURE M-E = STOP CHECK 2 (bench me, pycount=1)

record median 8.30 s [8.18, 8.30, 8.87]; replay 0.24 s-class;
Hessian estimate 7.0 s; segment synthesis post-M1: central 18.1 s,
**pessimistic-end 20.1 s vs <= 30 -> MET** (second checkpoint; the
M-D/M-E spread 14.9 vs 20.1 is declared — same-day host variance,
both clean-host, both inside target with margin). FINAL SPEED
COUNTER OF RECORD: **SEGMENT MET (M-D 14.9 s, M-E 20.1 s
pessimistic-end vs <= 30); CAMPAIGN MET across the band (~10-14 min
pessimistic vs <= 25, §5 shapes with H3/H4 landed)**. N1 never
triggered; H2 never consumed (fallback role moot).

## STEP 12 — FINAL RE-CHAIN ON THE DEFINITIVE TREE + CLOSURE (R3)

After the M6 default flip (sequential) + sequential nonfinite
guards: m12gate re-run + h3gate re-run on the FINAL tree (verdicts
below); ratchet baseline regenerated to the final tree (33 files,
622 literals — the +1 is the m6gate mode's own code, correctly
caught by the regen); both new lints PASS with all seeded rejectors
firing. Recorders: PROGRESS ORA + census DELTA S25-bis (R30
CONSUMED, R28 consumed-as-channel, R29 next-perimeter named, R31
landed-with-declared-split, R25 ledger delta incl. the three NEW
choice rows declared at commit); memory s25bis-speed-complete;
commits path-limited (git log -3 + status first, hunk audit after);
closing FULL suite EXIT-gated after the code commit (verdict
appended below).

DECLARED NON-ITEMS (never silently): mbwalk not re-run (MEASURE
row, not a gate; its committed artifact stands, the walk-level
M-D/M-E rows supersede it for speed accounting); m12-F4 def_twin
A1_MEMO_PROBE wiring declined (option, not duty, per the CONVERGED
reading); O5 numpy 2.5.2 = session-boundary user decision
(BLOCCATO class), presented at close; data/q_mapping.* timestamp
diff left untouched (not ours).

## STEP 13 — M6 ROOT CAUSE CLOSED TO CONVERGENCE (user order:
## "grave se non abbiamo capito cio' che non e' andato a buon fine")

LOCUS EXPERIMENT (s25bis_m6locus.log, pre-registered 3 rows):
(a) B=1 vmap vs sequential: dg 2.2e-02 — diverges ALREADY at B=1;
(b) B=9 lane0(=W) vs sequential 8.2e-02, and vs B=1 6.0e-02 — the
lowering changes with B; (c) **sequential eager vs sequential
jitted: 2.9e-02 — the SAME order of divergence lives INSIDE the
sequential path itself**. VERDICT OF MECHANISM: the adjoint through
the replay's ~250 implicit 4x4 solves carries an intrinsic
CROSS-LOWERING variability floor ~1e-8 relative on the gradient
(values at 1e-15) — ANY re-lowering (jit boundary, vmap, batch
size) moves g at that floor, and the FD Hessian amplifies it ~7
orders. The sequential FD Hessian works because it uses ONE fixed
lowering — the bias is common-mode and CANCELS in differences. My
first M6 form MIXED lowerings (batched rows vs separate base): the
bias did not cancel -> dH 18%. The defect was MY FORMULATION, not
the batching.

CORRECTED-FORM PROBE (s25bis_m6fix.log): base IN-BATCH (B = n+1,
lane 0 = W, one lowering): **dH drops 5-6x -> 1.68x the scheme
asymmetry** (2.06e6 vs asym 1.23e6; 4.9e-2 rel), INSIDE the derived
acceptance bound K_RICH x max(scheme asyms) = 4.9e6; the batched
scheme's own self-asymmetry (7.6e5) is BETTER than the
sequential's (1.2e6 — one lowering across all lanes);
LANE-PERMUTATION CONTROL: **BITWISE invariant** — lane content
fully determines the result, validating the common-mode
cancellation logic at the bit level. CONVERGED ADJUDICATION OF
RECORD: the corrected in-batch-base form is ADOPTION-READY (its
derived bound is met, measured); adoption = a declared version
change at a session boundary / F2 entry with m6gate RE-FORMED on
the corrected criterion (in-batch base mandatory; dH bound = K_RICH
x max scheme asyms) + the walk-gate re-chain — per the M3
session-boundary precedent, NOT rushed into this closure; the
registry row is updated to mechanism = mixed-lowering-adjoint-bias,
status adoption-ready-with-owner. Nothing about M6 is un-understood
anymore: three convergent evidences, one bitwise control, a
corrected form measured against a derived bound.

## STEP 14 — CLOSING SUITE OF RECORD

**20/20 test groups PASS in 282 s, SUITE_EXIT=0** (redirect-only;
includes the two NEW groups: (xix) findings-registry lint with its
4 seeded rejectors and the (vii) numeric lint with the validation/
ratchet tier); ONDEMAND tier: X-VMON executed PASS, all rows fresh
(pass 2026-08-12 >= last commit), 0 stale. Commits of record:
1806ae2 (M-chain S25-bis: M5c/M6/H3/H4 + probes + artifacts),
18b4e0f (R31 findings-as-code + R28 ratchet), closure = (this).
Session complete; nothing dropped silently.

## STEP 15 — CONVERGENCE MAP OF RECORD (user order: "vanno mappati
## quelli senza convergenza e vanno dimostrati" — the M6 episode
## proves gate-accepted != mechanism-isolated; this map closes the
## gap for EVERY S25 + S25-bis point, three classes, no silent rows)

CLASS A — PROOF-TOTAL (bitwise/exact gates: no unexplained residual
exists BY CONSTRUCTION):
  M1+M2 memos (bitwise A/B + in-walk fresh-equality control firing
  every walk); M4 plan-as-args (wall BITWISE args-vs-constants);
  M5a fused solve_cert (BITWISE); M5b abort (doctored
  first-offender exact); M5c dec-vector (BITWISE on every adaptive
  decision, both nets); H3 reuse (bit-identical arms + M1
  controls); H4 (reproduces the S24 tail numbers exactly + seeded
  stale-code refusal); M6 lane-permutation control (BITWISE); C4
  tier / H6 cache / R28 ratchet / R31 lint (mechanical with seeded
  rejectors).

CLASS B — MECHANISM UNDERSTOOD AND MEASURED at class level,
residuals bounded by DERIVED bands (with the named cheap
demonstration duties where per-cell isolation is still owed):
  (1) M5c z-floor deviations (1e-11 vs band 6.5e-10, 30x margin):
  ulp predictor-lowering seeds -> Newton-floor class; per-cell
  decomposition NOT needed (decisions bitwise) — declared.
  (2) cert-verdict recorder dependence at MARGINAL designs:
  mechanism = damped-trial path flip at a near-non-convergent cell;
  per-cell isolation = REGISTERED demonstration duty (registry row,
  next window, cheap).
  (3) M6 cross-lowering gradient floor: CLOSED TO CONVERGENCE this
  session (3 probes + bitwise control + corrected form vs derived
  bound) — registry rows mixed-lowering-adjoint-bias +
  cross-lowering-gradient-floor.
  (4) M3 cert_worst shift (0.475 -> 0.404 at adoption): the closure
  itself is mechanism-PROVEN by the C-A NASA-direct exactness
  oracle (h/cp at roundoff); the shift is the cert-noise-floor
  class demonstrated by (2) — cert_worst is a noise-scale quantity,
  verdict-neutral here (both sides certified); declared, no duty.
  (5) GAP-29 flip mechanism DEMONSTRATED NUMERICALLY this step:
  naive x2 prediction FAILS (measured 1.033 vs 1.402) because
  halving NTF also tightens the termination bound: denominator x2
  coupled with residual x0.74 -> net 1.47x -> the worst cell's
  achievable residual floor lies INSIDE (50, 100) x EPS x sc — the
  factor-2 margin is load-bearing, with the two coupled effects
  separated on the sweep data. NTF derivation duty unchanged (F2).
  (6) replay-fidelity band class (3e-11 vs 1e-15 floor: chain
  amplification ~1e4): same seed-perturbation class as (1)-(3);
  formal amplification bound never derived — accepted-empirical
  under the K_RICH band + the PERMANENT per-segment monitor
  rejector; folded into the cross-lowering registry row's F2
  derivation candidate.

CLASS C — OPEN WITH OWNER (by design or honest limit, all
registered):
  GAP-5 post-BC residual 1.17e-2 (what remains of the corner
  signal) -> F2 adjudication; NTF derivation -> F2; M6 adoption
  decision (READY, evidence complete) -> session boundary / F2;
  M-D/M-E pessimistic spread 14.9 vs 20.1 s (undiagnosed host
  variance, BOTH MET with 1.5-2x margin) -> registry row
  bench:speed-measurement-variance, next clean-host measure;
  choice-ledger NEVER/single-author rows (~25/12 recount) -> F2
  windows (carried, pre-existing); R31 corpus seeding -> FIRST duty
  next session; perimeter sense-review of the S25-bis touch (R29)
  -> next window.

VERDICT OF THE MAP: no point of S25/S25-bis is silently
un-converged — every row is either proof-total (A), mechanism-
demonstrated with bounded residual (B), or open-with-owner+trigger
in the machine registry (C). The M6 lesson is now STRUCTURAL: the
findings registry carries the demonstration duties as rows the lint
enforces, not as intentions.

## STEP 16 — SESSION TAIL: THE DIFF DRIVEN TO FULL CONVERGENCE
## (user order "chiudere in modo SOTA con orchestrazione agentica
## ogni punto"; Form-2: 2 positions + 1 fused judge, 1 round)

INSTRUMENT (weight reported): adversarial refuter (default-refute,
12 findings: 1 REFUTES / 9 caveats / 2 holds) + perimeter
sense-review R29 (13 findings: 8 adopt / 3 caveats / 2 changes) in
parallel -> fused judge (full-text, 3 needs-judge rows adjudicated)
-> validation/ADVISORY_S25bis_diff_convergence_2026-08-12.md =
**21 ADOPTED / 4 ADOPTED-WEAKENED / 0 REFUTED / 0 OPEN; repair
list 13 items**. The R29 perimeter-review duty for the S25-bis
touch is CONSUMED by this convergence. Judge liveness verified by
DISK SIGNAL (advisory mtime), not assurances — the 0-byte
transcript red-herring adjudicated against the completed agents'
own 0-byte transcripts (user skepticism honored, S25 lesson).

**RF-1 (HIGH, dual-verified: refuter + judge independently
recomputed the hash, bit-identical)** — THE REAL CATCH:
s24_deftw_derive.json was committed ALREADY STALE inside 1806ae2
(derive ran chain 1; the M6 default flip then edited a record-path
module; the final re-chain re-ran m12gate+h3gate only — never
re-derive). FAIL-SAFE direction: the session's own H4 mechanism
REFUSES loudly at campaign open — availability damage only, zero
correctness damage, no number consumed. NEW FAILURE CLASS named:
INTRA-COMMIT staleness (C4's git link is cross-commit and blind to
it; zero suite references to code_identity existed = the channel
hole). CLASS-A DEMOTION declared per the judge: the H4
ARTIFACT-of-record moved A -> C until re-stamp (the H4 MECHANISM
stays class A — it is what fired); the 1806ae2 commit-message
claim "derive re-run reproduces the S24 numbers" corrected of
record (true as a chain-1 event, false of the committed artifact).
ALSO corrected: my "21 registry entries" in commit 2d3661b's
message — machine count was 19 (judge's grep of record).

**REPAIRS R1-R13 ALL EXECUTED IN-WINDOW (phase-ordered per the
judge: record-path edits FIRST, ONE derive re-run, instruments,
gates)**: R1 batched-branch guard parity (RF-3) + R2 vg_batch x
A1_PLAN_ARGS=0 raise + R3 FUSED x COLEXEC interplay declared + R4
ACTIVE-RECORDER INTO THE MEMO KEY (never-mix now key-enforced) +
docstring key-coverage narrowing (RF-2 wording of record) + R5
first-hit controls FORCED on preplan consume even under
A1_MEMO_PROBE=0 (B-F5i; tax = the record the preplan saved) + R6
last_cert DEEP-COPIED (B-F5ii) + R7 env fingerprint stamped beside
code_id, WARN-grade at campaign open (judge §3.2: refusal stays
code-keyed; promotion trigger = first measured env-driven band
excursion; closure rule declared at RECORD_PATH_MODULES) + **R8
NEW MACHINE CHANNEL in group (xix): committed derive artifact vs
committed-tree code identity (jax-free AST parse of the module
list, hash replicated verbatim), doctored-code_id seeded rejector**
+ **R9 derive RE-RUN EXIT 0: ALL FIVE tail numbers BYTE-IDENTICAL
to the S24 figures (f2 1.4972280462197103e-02 < bar
2.013701802534313e-02; J_def 40262478.941368885; J_def16
40263824.53075551; cert_n 30643) — the judge's expected outcome
verified; new code_id 063fb796... + env stamp; [X-DEFTW]
UNBLOCKED** + R10 ratchet rejectors on ALL FOUR directions
(+1/-1/new-file/baseline-orphan) + skip-dir visibility + 622
docstring truth + R11 registry deltas (622+residual; recorder
class WIDENED to every thresholded record decision; re-formed
m6gate spec + jacfwd-blocked route facts on the vmap row; B-shape
clause + 3 scaling experiments on the floor row; NEW row
persistence:derive-artifact-intra-commit-staleness born DISCHARGED
with its evidence) + R12 h3gate declared coverage limit + R13
registry-lint SPAN RESOLUTION (file exists + range fits) with
seeded rejector, demo seeds re-pointed to real spans.

LINTS POST-REPAIR: findings (xix) PASS — 20 entries, 16 open,
0 violations, H4 channel FRESH (063fb796 == 063fb796), 6 seeded
rejectors firing; numeric (vii) PASS — 622 baselined, 4 ratchet
directions REJECTED, skip scope printed. SELF-IMPROVEMENT AT
CONVERGENCE (standing directive applied, not announced): frozen-
code re-chain rule EXTENDED of record — "the re-chain includes
re-stamping every code-identity artifact whose modules were
touched"; recorder-in-the-key discipline; judge-liveness by disk
signal. Post-repair gates + closing suite verdicts appended below.

POST-REPAIR VERDICTS OF RECORD: h3gate EXIT 0 (R4 recorder-in-key +
R5 forced controls + R6 deepcopy hold; controls fired on the preplan
consume) -> m12gate EXIT 0 -> closing FULL suite **20/20 PASS in
295 s, SUITE_EXIT=0** (incl. the (xix) group with the NEW H4
artifact channel FRESH and the (vii) ratchet with 4 firing
directions; ONDEMAND 0 stale). Tail commits: record-path + restamped
artifact + R8 channel in one commit; instruments + registry + log in
the second. SESSION S25-bis FULLY CLOSED — every point of the diff
driven to convergence (21/4/0/0), every repair gated, nothing open
without owner. NEXT = S-ORDINE (R32, committed prompt), then S-CERT
(R33), then F2.
