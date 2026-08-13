# ADVISORY — ENGINE SPEED AUDIT (S-SPEED parallel session, 2026-08-12)
# The adjudicated plan of record for the S25 "ENGINE SPEED SESSION":
# 5-20x at EQUAL certification, determinism, R5, REQ-NONSTALL, rejectors.
# Untracked ADR-pattern deliverable. Companion:
# DISPATCH_Sspeed_to_S25_2026-08-12.md (execution order, converged-only).

LABEL OF RECORD: **judge-adjudicated in one round; Form-3 red-team verdict
ABSORB-WITH-REPAIRS (10 issues: 2 high, 3 medium, 5 low — all 7 textual
repairs APPLIED in this document); generality+SOTA gauntlet repairs
V1-V12 + 2 mechanism-level SOTA amendments APPLIED.** Never quote the raw
judge text against this document — this text supersedes it.

ADDENDUM AT CLOSE (same day): during this audit the repo HEAD advanced
8761dce -> 589cc56 — **S24 CLOSED of record** (F1b twin EXECUTED, recorded
branch F4 margin-inactive/cert-limited, EQ-v2 = CONJECTURE + H-CLASS;
closing suite 15/15). Read per the mandate's newer-HEAD rule. Consequences
checked: (i) the S24 closure's own NEXT row already names S25 = C4-first ->
ENGINE SPEED SESSION ingesting THIS dispatch (+ the parallel gap-map +
choice ledger) — placement identical to §"Placement" of the dispatch;
(ii) the S24 decisive process has ENDED, so M0's clean-host precondition is
now satisfiable; (iii) every contention declaration in this document
remains accurate for the time the benches ran; (iv) nothing in the S24
closure contradicts any lever, gate, or number herein (the recorded
cert-limited branch is exactly the walk shape this plan's rejection-path
economics price). No other text of this advisory changes.

## 0. Session frame, method, declared deviations

- Parallel READ-ONLY session per validation/ADVISORY_Sspeed_prompt_2026-08-12.md.
  No commit, no edit to any tracked file; S24 perimeter untouched (the S24
  decisive campaign, PID 44192 = def_twin_falsifier.py, RAN THROUGHOUT this
  audit — every bench number below was measured under DECLARED CONTENTION
  (pycount 2-6 recorded per bench); interleaved A/B repetitions and medians;
  RATIOS are the evidence, absolutes are indicative until the M0 clean-host
  re-baseline).
- Method: Form-1 find->verify (wf_3ef63212-0ad: 6 dual-lens finders + 6
  default-REFUTED adversarial verifiers, 12 agents, 0 errors) -> session-lead
  code-level cluster map + dispute ledger (D1-D4) -> Form-2 panel
  (wf_7deab19c-be2: 3 position authors engine/policy/arith + dedicated
  refuter + judge) -> Form-3 red-team over the judge layer + an independent
  generality+SOTA gauntlet (dual lens: directive generality-nonhardcoded-
  procedures; directives repo-sota-standard + sota-library-survey-directive).
- Finding statistics: 50 findings produced (declared drops: 25 more were
  cut by the max-N/noise rules), 43 CONFIRMED / 7 REFUTED after adversarial
  verification with real microbenchmarks (march/scan/driver/env/campaign/
  costmodel subsystems).
- Env of record (measured live): Python 3.13.14 win64, numpy 2.5.1 (PyPI
  latest 2.5.2), scipy 1.18.0 (latest), jax+jaxlib 0.11.0 (PyPI LATEST),
  CPU-only, Windows 11; persistent XLA cache LIVE in campaign carriers via
  the o33_bench import side-effect (dir %TEMP%/jax_cache_rde, 180 entries
  written by the running S24).
- DECLARED DEVIATIONS: (i) several finder/verifier/position artifacts landed
  under <repo>/sspeed/ instead of the session scratchpad (untracked;
  relocated to the scratchpad at session close; no tracked file touched);
  (ii) the ENGINE position author reported cluster_map.md not found at its
  resolved path and worked from 5/6 finding-pairs — caught by refuter ATT-2,
  judge discounted its campaign-blind claims accordingly (adjudicated,
  no residue); (iii) all bench absolutes contended (above).

## 1. Baseline corrections OF RECORD (surfaced by verification)

1. **The "~2 s replay" baseline is the LINEAR-closure replay.** The
   production C1 replay is ~6.5x that (3.269 s measured, eps=4 twin;
   defnoz-class ~13 s derived). Every number in this plan is C1-priced
   (ENV-F1). Post-fusion C1 replay ~1.2 s measured at eps=4.
2. **Campaign carriers already inherit the persistent XLA compile cache**
   via an import side-effect (o33_bench.py module-level config;
   def_twin_falsifier.py:107, margin_governor.py:132). Standalone entry
   points are NOT covered; TWO disjoint cache dirs exist (jax_cache_rde vs
   rde_jax_cache). Arming the env var in carriers is NOT a speed lever
   (MARCH-F8 refuted); unification is hygiene + standalone-class gain.
3. **The S18 "67 evals" ledger line is untruthful**: true compiled-eval
   count ~102-108 (g_np and the 18 preconditioning evals uncounted; the
   n_eval += n+1 line double-counts Hessian evals: 67 = 50 Hessian + 17
   walk); the T2 lhs prices each eval at t_solve+t_grad while reality is
   ONE value_and_grad (~0.5-1.0 s). Feeds the queued G0/T2 review (§7.1).
4. scipy 1.18.0 trust-constr calls fun and grad as SEPARATE user callbacks
   at the same x (verified in installed source _differentiable_functions.py:
   391-401) — each of ours runs a full value_and_grad and discards half.

## 2. Dispute resolutions (D1-D4, on the on-file evidence)

**D1 — traced cert_diag screen: DEAD AS A GATE; the compiled record moots
it; shadow-mode instrumentation only.** The costmodel bench is decisive on
the population that matters: on the 5 persisted S22 rejected designs the
frozen-plan screen catches 1/5 AND its control FAILS (the healthy certified
base screens at 1.165 > 1). Metric FORMULA identity is line-verified and
DRIVER-F2's 132.4x per substituted event is measured — but frozen-plan
replay iterates and fresh-adaptive-record cells are DIFFERENT VERDICT
OBJECTS exactly on the cert-limited rejection population: "same verdict,
cheaper" may not be claimed (constraint 5 violation as deployed; false
rejects change the walk). Post-plan a rejected probe costs ~6-9 s from the
compiled record AT THE RECORD'S OWN METRIC, so the screen's residual value
does not justify a verdict-object risk. Ships: shadow-mode logging only
(O1), never gates; deployment = named conditional N2 (owner F2; trigger =
material rejected-probe share after the mandatory set AND measured shadow
agreement >= its own derived bound). Gauntlet V11 binds: any screen ever
deployed opens in shadow mode per campaign (no transferred calibration),
counters print for its whole life.

**D2 — persistent-cache coverage: three process classes, three answers.**
Campaign carriers: residual gain 0 (already armed — booked at zero).
Standalone/diagnostic/restart launches: real, measured 8.1x compile+first
(168.0 -> 20.8 s cross-process). Production hot path ACROSS plans: the
cache cannot hit — plan arrays are baked constants, every plan is a new
HLO (measured: different plan 91.2 s, ZERO absorption). The minutes live
in plan-as-args (M4); the cache is the cross-process backbone.

**D3 — the single target arithmetic of record** is §5, with the refuter
repairs (ATT-1/16/17/18) and the red-team arithmetic repairs applied.
Headline (red-team-corrected wording): campaign <= 25 min **MET across the
band** — ~7-15 min with H3+H4 landed (pessimistic-end margin ~1.6x),
~10-20 min on the mandatory set alone (margin ~1.3x); the campaign-layer
items are insurance and cap-protection, not arithmetic necessities.
Segment <= 30 s **MET at the central estimate (16-26 s), razor-thin
(~29-32 s) at the declared band top** — adjudicated empirically at the
M-D/M-E checkpoints under the pessimistic-end standard, with sequenced
insurance (H2 residue, O4, N8) if thin.

**D4 — the "L3" label, once, cleanly.** DEAD: the dispatch-amortization
mechanism (each FD-Hessian eval is one ~3 s compiled call with ~1 ms
dispatch) and ANY bitwise-preservation claim (measured max|dg| 3.125e-07,
floor-order). ALIVE: (i) batched compiled FD gradients — measured 0.381
batched/sequential (2.6x) and 3.54x at K=10 — a DECLARED version change
gated on KAT re-run + O3.1 re-pass, BINDING order after plan-as-args (fresh
vmap compile 30.86 s is a net loss otherwise); (ii) P5 colored FD only as
N8 after the sparsity-derivation duty (Q1) — the gauntlet's V7 procedure
is the mechanism of record (measured pattern, eval count = OUTPUT);
(iii) shard_map optional multiplier (O4). jacfwd exact Hessian =
adjudication-only (N5, trajectory-changing).

## 3. Refuter + red-team ledger (dispute ledger of record)

- Refuter: **18 attacks (ATT-1..ATT-18: 5 major — ATT-1/2/3/8/16 — 13
  minor, 0 fatal; the refuter's own header undercount corrected here of
  record). All 18 ABSORBED** by name in the judge layer; the load-bearing
  ones: ATT-1 (engine-only counterfactual re-priced with the compiled
  record carried through the campaign layer — position_arith/refuter "M2"
  = this plan's M5; this plan's M2 is the fun+jac memo), ATT-6 (colored FD
  not booked without sparsity evidence), ATT-13 (C1-honest record pricing),
  ATT-16 (mandatory-set partition repaired), ATT-11 (screen-band holdout
  control), ATT-12 (shadow fixture tolerance bands).
- Red-team (Form-3, over the judge layer): **ABSORB-WITH-REPAIRS**, 10
  issues. HIGH: (1) campaign margin overclaim (">=1.7x pessimistic" failed
  the judge's own rows — corrected to 1.6x/1.3x per tier set, §2-D3);
  (2) "engine-only ~9-14 min" adopted verbatim from ATT-1 — re-derived
  ~10-20 min (still HIT; corrected everywhere). MEDIUM: M2/M5 label
  collision (repaired with the equivalence clause above); 17-vs-18 attack
  totals (corrected); PART C vs PART G ordering contradiction (ONE order
  of record declared: the PART G graph — M4 before M3 — with binding
  constraints restated in §6). LOW: H4 tail residue unified to
  −50..−110 s post-M5; **early-abort HOOKS declared part of the mandatory
  M5 chain** (H1's opt-in flag + schema note remain the high-value half;
  rejected-segment band without H1 = ~10-16 s, campaign verdict
  insensitive); ATT-4/ATT-14 body sentences added (rung-level overhead
  ~75-85%: records 65-80%, Hessian ~7%, walk 7-15%; the pre-reconciliation
  union band was [9,23] min, superseded by the 7-15 min band); "without
  M1" counterfactual corrected to "band-top breaker post-M5, MISS pre-M5";
  CAMPAIGN-F2 post-M5 residual aligned at ~25-35 s/boundary. Red-team
  clean-sheet: no judge-invented claims, no manufactured unanimity.
- Generality+SOTA gauntlet: 12 violations (V1-V12), ALL repairs applied in
  §4 items; 2 mechanism-level SOTA amendments (built-in cache LRU; scipy
  group_columns coloring-only + measured-pattern rewording); 4 survey rows
  (§7.3). None refutes a measured gain.

## 4. THE PLAN (tiers; every item: mechanism / gain / rigor / risk /
## acceptance / cost / owner). Constraints (1)-(7) as in the S-SPEED
## mandate; STOP-WHEN-MET rule in §6.

### MANDATORY (the target-carrying set)

**M0 — Clean-host re-baseline + baseline re-declaration + G0/T2 ledger
[RIGOR].** One clean-host defnoz record + C1 replay + val_grad timing set
post-S24 (all current absolutes contention-inflated); re-declare the replay
baseline as C1 (~13 s class); hand G0/T2 the truthful ledger (§7.1).
Gain 0 (anchors every acceptance test). Risk none. Acceptance: baselines
quoted with provenance; repeat-spread inside a declared band. Cost <0.5
session. Owner: S25 item 1.

**M1 — Segment-boundary record dedup + failed-record memo (DRIVER-F1 +
MARCH-F9).** Stash the callback's (out, plan, xk) at toc:1162; reuse at
loop top (:930) on exact match; memo FAILED P3(ii) records (replay the
typed raise). Key per gauntlet V8: canonical tuple (W.tobytes(),
sorted-key-JSON cfg, CONTENT hash of the thermo table arrays, closure
identity, + carrier code identity for anything outliving the process);
in-process stores BOUNDED AND STRUCTURAL (one slot at the segment
boundary; per-rung dict cleared at rung close — no LRU constant).
Gain: one full record deleted per boundary on ~70-90% of transitions
(~2x on record events today, ~25-35 min off the 76-min rung; post-M5 the
absolute shrinks but the segment row "base record -> 0 s" DEPENDS on it).
License: constraint (2) — bitwise re-record equality MEASURED; the
driver's own invariant (toc:1024-1028) makes a mismatch a loud
contradiction. (1): cert computed+gated when made, reused never skipped.
(5): fresh-record equality probe, cadence per V12 (once per STAGE
BOUNDARY, structural not counted); perturbed-W must miss. (6): rows
record=fresh|cached(key); counters reconcile. Risk: in-place mutation
aliasing through the cache — deep-frozen copy. Cost ~35-55 LoC. Owner:
S25 item 2.

**M2 — fun+jac / m+gm one-slot memo + n_eval truth repair (DRIVER-F5 +
SCAN-F6) [RIGOR half executes regardless].** One-entry memo keyed
u.tobytes() shared by f_np/g_np (toc:1102-1126) AND m_np/gm_np
(margin_governor:215-229, def_twin:663-677); count actual compiled
executions. Gain: one compiled eval deleted per both-requested point,
1.5-2x on the fun+jac share (~5-15 s/segment), bit-identical. (6) improved
(honest n_eval feeds G0/T2). Acceptance: execution count drops by the
matched-point count; bitwise-equality assert on a KAT segment; 1-ulp
perturbed u misses (negative control). Cost ~30-45 LoC. Owner: S25 item 3.

**M3 — Fused/floor-index C1 closure (ENV-F1; ENV-F2 riding at 0 booked
speed) [session-boundary adoption].** Fused eval_f_fp(T) (one _locate, one
6-gather set, shared t-powers) in the invert_h body; fused post-loop
s0/cp; O(1) floor index on the uniform grid. Gauntlet V4 applied: the
Newton trip count K is COMPUTED PER TABLE inside build_c1 from that
table's own data (seed-error bound, contraction constant, the table's own
C6 roundoff floor, K_RICH-style margin) — never a literal; stored in the
c1 pack, printed in the table's cert artifact; valid for every table that
passes the [X-THC1] gates by construction. Gauntlet V5 applied: build-time
grid-UNIFORMITY rejector for EVERY accepted table (max deviation <= C_OPS
x eps x D, loud refusal naming the interval); the node-tie-AMENDED
index-identity control (off-node exact + node/±ulp value-band) runs PER
TABLE at build. Gain MEASURED: 2.72x on the production C1 replay (3.269 ->
1.202 s, wall_y within 2.5e-14); 6.6x closure eval; 2.0x whole-loop
compile; multiplies EVERY compiled event incl. the compiled record's
Newton bodies. (2): bits move => DECLARED version change at a session
boundary with fresh record (record and replay share the injected state_fn
— bit-identity holds by construction after adoption). (3) improved
(derived K replaces magic 8). (5): [X-THC1] C1-C7 + R1-R4 re-run;
corrupted-D control must fire (measured 17201 disagreements). Risk: A-G
unmeasured (gradient-pass share — Q2; falsifier consequence in §5). Cost
~100-150 LoC + cert re-runs; 1 session. Owner: S25 item 6 (order of
record: AFTER M4 per §6; before M5c's final gate baseline).

**M4 — Compile economy: plan-as-args + fixed-shape padding (SCAN-F2 +
DRIVER-F7 + CAMPAIGN-F9; SCAN-F3 guard-rail; H6 folded).** Module-level
jitted engine taking plan arrays as OPERANDS, keyed by the bucket-shape
signature. The scan verifier's three adoption conditions are DESIGN
REQUIREMENTS: (i) semantic last-row index becomes an operand under row
padding; (ii) valid_idx -> fixed-size act-masked wall output + mask-aware
thrust_J; (iii) trace-time booleans/ints stay static signature keys.
Gauntlet V1 applied: NO quantization grid at landing — bucket shapes
default to the EXISTING derived discipline (single bucket per phase,
padded to case-level per-phase maxima over recorded plans); a geometric
grid may be added ONLY if the logged churn counter measures >1
compile/rung, declared PRACTICE with the measured churn, re-adjudicated
against the SCAN-F3 padding bound. Gauntlet V2 applied: the signature is
GENERATED, never enumerated (canonical tuple of ALL static fields walked
programmatically from the plan schema + engine build flags), with a
property-test rejector (any static-field difference => different
signature; unseen topology => new signature by construction). SOTA
refinement adopted: carry the plan as a REGISTERED PYTREE (array leaves =
traced operands; aux_data = the static signature — mechanizes V2).
GUARD-RAIL (SCAN-F3): single-bucket-per-phase padding KEPT; multi-bucket
splitting REJECTED inside this item. Gain (post-M3 pricing): perturbed-
rebuild overhead (~37 s/segment class measured; 90 s contended
campaign-side) deleted from segment 2 on => ~3.5-7 min/rung of pure
recompilation; makes M6 and family-vmaps one-time-per-campaign; signatures
survive restarts via the cache (8.1x warm). (2): constants->operands can
change XLA folding — adopt per shape signature ONLY through the
Newton-floor equivalence rejector + O3.1 leak detector + the WARM-PATH
args-vs-constants band (this gate can FIRE and reject the lever). (5):
one-time bitwise A/B same-plan; the standing per-segment replay-fidelity
monitor stays the permanent rejector; jax_compilation_cache_check_contents
spot run = corruption rejector, cadence per V12 (once per campaign OPEN).
Folded H6 hygiene: ONE canonical cache block in a1_ideal_march_jax.py, ONE
dir, min_entry_size -1, min_compile_time_secs 0.0; **cache bounding via
the BUILT-IN jax 0.11 LRU `jax_compilation_cache_max_size`** (gauntlet
V3/S3 — never hand-rolled; cap = declared PRACTICE constant derived from
the live cache's measured median entry size x expected signatures x
campaigns retained, arithmetic written at adoption). Risk: signature
stability across production segments plausible but unmeasured (Q3) —
M-B reports the collision rate. Cost ~250-400 LoC, 1-2 sessions (the
heaviest refactor). Owner: S25 items 4-5.

**M5 — The compiled-record chain (MARCH-F3 -> abort hooks -> F6-AMENDED
per-column executor; MARCH-F4/F5 subsumed/riding).** Three rungs,
independently gated: (a) fused solve_cert third jitted entry (same newton
+ step_norm expressions + the axial-margin sound_of_q — removes a third
per-cell dispatch; ~10-15% standalone; prerequisite-shaped). (b) EARLY-
ABORT HOOKS — **part of the mandatory chain (red-team repair)**: typed
refusal at ratio>1 at BOTH cert sites (a1:695-707 AND toc:239-275),
margin-precedent raise pattern; the opt-in flag + schema note remain in
H1. (c) F6-AMENDED executor: HOISTED, module-level, jit-wrapped per-column
executor over BUCKETED PADDED shapes in M4's plan-as-args style; in-trace
seeds; per-cell (z, cert_step, cert_scale, margin) returned as stacks,
host-checked with the SAME bound and FAIL semantics; Python keeps EVERY
adaptive decision at column granularity; sub-crossing discards never enter
the plan. THE EAGER cell_scan PATTERN IS REJECTED AS MECHANISM OF RECORD
(measured 0.8x SLOWER + an 803 s per-shape compile-churn event). Gauntlet
V1b applied: record-path column buckets REUSE the replay's own bucketing
discipline (bucket count structural == phase count; compile count bounded
by phase count x running-max growth events, logged; cache absorbs
re-encounters). Gain: record 111 s -> ~13-16 s pre-M3 / **6-9 s post-M3
(declared band 5-12)** — the single biggest term. (1): same step_norm
expression in-trace, per cell, host-checked, same raise sites,
first-offender order preserved. (2): gate = X-SCANM-grade equivalence on
twin + defnoz-mild: dec-vector IDENTITY (bitwise) + z inside the
Newton-floor band + plan bit-identity; ANY plan difference = lever
REJECTED; legacy Python record retained behind an env flag as arbitration
path. (5): doctored-cell control fires at the right (column,row); seeded
near-seam design pair must produce the SAME wall-search flip in both
recorders; controls sized to the declared detection floor (S24 R-GRAD
lesson). (7): the record REMAINS the adaptive decision authority. Risk:
column-shape compile churn (the measured 803 s failure mode) — M4 is the
prerequisite. FALLBACK: H2 (>=1.86x measured) still leaves record
~50-60 s => segment target missed => N1 triggers. Cost: (a) ~60 LoC;
(c) ~300-500 LoC, 1-2 sessions — the centerpiece. Owner: S25 items 7-10.
MEASURE M-D = STOP CHECK 1.

**M6 — Vmapped FD Hessian + precond batch (DRIVER-F4/SCAN-F5; BINDING:
after M4).** jax.jit(vmap(value_and_grad)) over the (n+1, n) FD rows +
the one-time 2n Jacobi block; same stencil, same derived steps, same
symmetrization — WHO executes changes. Sequential fallback on nonfinite
lane + counter (the current sequential block has NO nonfinite guard — the
batched path is not weaker; REQ-NONSTALL). Gain MEASURED: 2.6x on the
Hessian rows (0.381 decisive; 3.54x at K=10) => block 20-40 s -> ~4.5-8 s
post-M3 (A-G-dependent). Campaign share ~1.05-1.15x — this item exists
for the SEGMENT target. (2)(6): NOT bitwise (3.125e-07, floor-order, 4-6
orders below derived gtol) => DECLARED version change gated on KAT re-run
+ O3.1 re-pass (S18 P1 precedent). Risk: fresh vmap compile 30.86 s per
rebuild => NET LOSS without M4 (binding); batch memory ~75-100 MB. 
Acceptance: per-lane vmap == sequential at Newton floor + bitwise report;
corrupted-lane control fires; measured block <= 8 s at defnoz. Cost
~60-100 LoC; 0.5 session. Owner: S25 item 11. MEASURE M-E = STOP CHECK 2.

### HIGH-VALUE (in order, budget/shortfall; H1 recommended in-session)

**H1 — Early-abort opt-in flag + schema (MARCH-F2 + DRIVER-F3).** The
hooks are mandatory in M5(b); H1 ships `abort_uncert=True` at driver/
campaign gate sites, default False at verdict/reporting sites (main()
unwrapped calls keep their PASS/FAIL rows — the constraint-6 regression
the verify caught). Gain: bit-zero on certifying records; ~2x uniform /
5-20x adversarial on the failing-record share (multiplier = Q4); rejected
segment 5-12 s with H1, ~10-16 s without (campaign verdict insensitive).
(1) gate condition unchanged, fires earlier never later; (5) doctored
solver output at cell k -> refusal AT k, first-offender index stable;
(6) declared schema note (cert_worst = first-offending ratio +
aborted_at_cell; cert-before-margin ordering declared; certdiag path
unchanged). Cost ~40-70 LoC. Owner: S25 item 8 (with M5's hooks).

**H2 — NumPy predictor twin + hygiene bundle (MARCH-F4 + MARCH-F5) — the
M5 fallback.** Host NumPy predictors + mirror of solved points; bracket-
scan vectorization (444x on its block, ~4.5 s/record, NOT subsumed by M5,
per-record); certify scale from host copy; stderr throttle. Gain: >=1.86x
whole-record MEASURED from _foot alone (gate demonstrated live: dec
identity 493/493, z 1.364e-11 inside 5.858e-11); ~2-2.5x full lever.
Under M5 survives only for eager wall_search cells (overlap declared);
standing FALLBACK if M5(c)'s gate rejects. (2): seed-class change —
X-SCANM-grade gate; the bracket scan's bitwise identity is FALSIFIED
(1.46e-11) so it rides the SAME gate (bit-zero claims rejected of
record). Cost ~80-120 LoC. Owner: S25 item 12 / M5-fallback.

**H3 — Campaign rung-boundary dedup (CAMPAIGN-F1 + F2, both carriers).**
C3 repeat reuses st_new as the repeat's st_cur (argument-identical,
verified stateless); run_trsqp returns its last certified (out, plan) +
accepts preplan=; rung-end/next-rung/seg-0 consume it; same fix in
margin_governor (3 records where 1 suffices). Gain: −1 record per
repeated rung + −2..−3 per boundary ≈ −220..−330 s/rung today, ~4-11
min/campaign at the S24 1-2-rung shape; post-M5 ~25-35 s/boundary — NOT
target-mandatory, near-free insurance; dominates the M5-rejected fallback
world. (2) reuse exact by measured bitwise determinism; (5) shares M1's
probe + control. Cost ~80-120 LoC, 3 files. Owner: S25 item 13.

**H4 — Tail-to-derive + stage persistence with the CODE-IDENTITY key
(CAMPAIGN-F5 + F10).** Ladder-invariant tail (cs_stats(W0), r=2 refined
march, J_def record — also killing the intra-tail W0 duplicate, W16
record) moves into stage_derive; F3/F7 reference quantities become
PRE-REGISTERED derive-artifact numbers. Persist (plan, record) across
stages keyed hash(W, class, cfg, CODE-IDENTITY of the record-path
modules); hash mismatch = LOUD refusal (the S24 C5 staleness-by-code
scenario must REFUSE — replayed as the acceptance control). Gain:
−630..−1270 s today (−50..−110 s post-M5, red-team-unified) out of the
2h-capped decisive window + the irreplaceable content: F1b fallback fires
BY RULE at cap exhaustion — every ladder-invariant second in-cap is
fallback risk bought for nothing. (6) strictly improves (pre-registered
references; persisted-record hash proves provenance). Cost ~180-280 LoC;
1 session. Owner: S25 item 14 — before the next decisive campaign.

**H5 — Derive-side candidate screen with the candidate-derived band
(CAMPAIGN-F3 as repaired; the family/L4 lever).** Record the MAXIMUM-
plan-mismatch member of the family FIRST (gauntlet V10: for amplitude
families the largest |a|; in general argmax of the declared mismatch
measure; no declarable ordering => derive at TWO extreme members, take
the max — "first in pre-registered order" was order-coincidental); band =
K_RICH x |m_record − m_screen| there; screen the rest via ONE vmapped
traced margin eval (measured 112x steady-state); skip only beyond-band
infeasibles in declared order; every non-skipped candidate still gets the
true record + certification. The seed-anchored band is DEAD (vacuous by
6700x, measured). Controls: recorded-infeasible fixtures must screen
infeasible or fall through; sign-flipped val must FAIL; ATT-11 holdout —
the band derived at the max-mismatch member must bound the measured error
at a SECOND recorded member (CAN fail). Gain: worst case 8 records ->
1-2 (−11..−13 min in derive); ~0 when candidate 1 passes; structural
payoff = falsifier families / multistart (N records -> 1 vmapped replay +
few records; SCAN-F4's 3.52x measured, behind its lane-k==sequential-k
rejector). Cost ~80-120 LoC. Owner: S25 item 15 / F2-window.

### OPTIONAL (polish; drop without regret)

**O1 — Shadow-screen instrumentation (D1 deliverable, never gates):**
(screen_worst, record_verdict, agree, population_tag) logged where a warm
build exists; pinned S22 fixture with TOLERANCE bands + re-baseline-at-
closure-version-change clause; sign-flipped val breaks the fixture;
gauntlet V9 rides here: the W-independence of every lane bucket EXCLUDED
from the traced margin gate is asserted per engine build mechanically
(perturb-W bit-identity probe on excluded buckets; a bucket that becomes
W-dependent forces its lanes into the gate or fails the build loudly —
owner F2, part of the cert/val exclusivity lift). ~30-60 LoC.
**O2 — Drift watch, reporting-only (CAMPAIGN-F8 corrected):** one traced
val_diag eval per accepted base; sign-migration PROXY on the frozen chain
(true i_cross needs a record); chain-geometry blind spot DECLARED per row;
mis-frozen mask must trip it. Builds N3's trigger data. ~50-80 LoC.
**O3 — Rung-start trace dedup + jax.eval_shape lane shapes (CAMPAIGN-F4):**
~35-60 s/rung attempt (same-plan duplicates are cache-absorbed ~17 s, not
90 s — finder's minutes-class claim revised down of record). ~40 LoC.
**O4 — shard_map over the Hessian/family batch (ENV-F4):** measured 1.65x
over vmap (proxy, contended); only if the segment is still thin after M6;
gauntlet V6 applied: ndev DERIVED at process start (min(batch, os.cpu_count
− declared reservation policy), never a literal 8); bitwise member-identity
control re-runs at every ndev actually used AND on the real replay.
**O5 — numpy 2.5.1 -> 2.5.2 [RIGOR row]:** adopt-with-rejector (carrier
suite green); the 2.2.6 pin binds the SEPARATE Cantera generator env.

### NAMED CONDITIONALS (owner + trigger; never default)

- **N1 — true L5 full compiled record (MARCH-F7).** Owner F2-engine.
  Trigger: measured segment shortfall after M1-M6 (e.g. M5c gate rejects
  and H2 leaves record ~50-60 s). Adjudication package: triple negative
  control incl. seeded near-seam flip-identity pair on BOTH recorders;
  Python record retained as sampled referee. Marginal 2-3x over M5c.
- **N2 — traced-screen deployment as a gate.** Owner F2. Trigger:
  material rejected-probe share after the mandatory set AND shadow (O1)
  agreement >= its own derived bound on the live population. V11 binding.
- **N3 — CAMPAIGN-F8 semantic half** (repeat restarts from last pre-drift
  certified base — touches the panel-conditioned C3 semantics, commit
  236422f). Owner: panel/declared-rule amendment. Trigger: one
  post-8761dce campaign artifact + O2 drift data.
- **N4 — stall-stop (CAMPAIGN-F7 class, REFUTED as stated).** Owner F2.
  Trigger: post-8761dce artifact + derivable trigger + segment-by-segment
  base-identity verification (J crept +0.13% during fencing — the
  equal-outcome premise is false in general).
- **N5 — jacfwd exact Hessian.** Adjudication-only (trajectory-changing).
- **N6 — benign-flip segment merge.** Touches constraint 7 (redefines the
  RK-G P2 segment boundary); needs its own panel. Flagged, never traded.
- **N7 — Python 3.14 / 3.14t.** DECLARE-NOT-ADOPT (jaxlib wheel is cp313
  GIL; interpreter gains land on the path M5 compresses structurally).
  Revisit trigger: M5 AND H2 both rejected.
- **N8 — P5 colored/sparse FD Hessian.** Owner F2 / S25-shortfall.
  Trigger: Q1 sparsity derivation lands AND segment still thin after M6.
  Mechanism of record = gauntlet V7 verbatim: pattern MEASURED at the
  first segment base of a (class, basis, n) triple via one full FD
  Hessian thresholded at the derived FD-noise floor; **colors = scipy
  group_columns on the measured pattern (S1: coloring ONLY — never
  approx_derivative, whose step machinery would replace the repo's
  derived steps = constraint-7 violation; private-module pin declared
  with the ~30-line CPR greedy fallback)**; eval count = OUTPUT
  (n_groups+1), degenerates gracefully to n+1 if dense; rejector = full-FD
  re-probe at every pattern-REUSE boundary (V12 cadence), off-pattern mass
  vs derived floor, exceedance => fall back + re-derive; pattern re-derived
  on any (n, basis, knots) change. NOT booked in the arithmetic.

### DEAD (do not resurrect; verdict rows of record)
Naive cert screen as a gate (D1); COSTMODEL-F4 dispatch-amortization;
COSTMODEL-F6 6x replay headroom (cross-engine artifact); COSTMODEL-F9
derive-batching premise (the DE derive accepted candidate 1; break at
def_twin:741); seed-anchored screen band (vacuous 6700x); eager cell_scan
record (0.8x measured); external interpolation/thermo libs + tabulated
inverse T(h) (DOA on C6 semantics; survey rows S2 close the constraint-7
duty with named candidates: interpax/diffrax DECLINED); L4 batching of
early-exit searches; Jacobi-precond removal; "arm the cache env var in
carriers" as a speed lever (already armed via import side-effect).

## 5. THE TARGET ARITHMETIC OF RECORD (red-team-repaired)

Named assumptions: C1-corrected baselines; 21-segment decisive rung 4560 s
(~10-11 accepted / ~10-11 P4-rejected, S24 step 12); record share 65-80%
after the duplicate-record correction; single-step segments; A-R: decisive
campaign = 1-2 S24-shape rungs (monotonicity stop); A-G: val_grad gain
~2x from M3 (UNMEASURED, Q2 — falsifier: if <1.5x the segment band widens
to ~18-33 s and M6 carries more weight); A-S: bucket-signature stability
(Q3). All projections CENTRAL-ESTIMATE with declared bands; STOP-WHEN-MET
adjudicates at the pessimistic end of the MEASURED band. Rung-level
overhead of record: ~75-85% (records 65-80%, Hessian ~7%, walk 7-15%).

Accepted segment (defnoz class), post mandatory set:

| Term | Today | Post-plan | Lever |
|---|---|---|---|
| Segment-base record | 111 s | 0 s | M1 |
| Callback record (plan/flip authority) | 111 s | 6-9 s (band 5-12) | M5 x M3 |
| Hessian block (n+1) | 20-40 s | 4.5-8 s (A-G) | M3 x M6 |
| Walk evals (~3.4/seg true) | 10-25 s | 4-7 s | M2 + M3 |
| Replay-fidelity monitor | ~13 s (C1) | 1-2 s | M3 |
| Engine rebuild/compile | ~37-90 s | ~0 warm | M4 |
| **Accepted segment** | ~217 s avg | **~16-26 s central; ~29-32 s band top** | |

Rejected segment: one record (failure memo kills the loop-top re-fail) x
abort fraction: **5-12 s with H1; ~10-16 s without (campaign verdict
insensitive)**.

Decisive campaign (compiled-record pricing carried THROUGH the campaign
layer — cs_stats IS run_toc_record, the refined march IS the A1 march):
21 segments ≈ 205-402 s + rung-boundary layer ~60-150 s with H3 (or
~150-300 s without) + adjudication tail ~0 in-cap with H4 (or ~50-110 s
post-M5 without) + first-launch compile set 3-6 min once (M3 halves it;
M4 makes it per-signature; 8.1x warm on re-runs).

**Verdicts of record:**
- **Campaign <= 25 min: MET across the band** — ~7-15 min with H3+H4
  (pessimistic-end margin ~1.6x); ~10-20 min mandatory-set-only (margin
  ~1.3x); engine-only counterfactual re-derived ~10-20 min (still HIT).
  The pre-reconciliation union band was [9,23] min, superseded by this
  arithmetic. H3/H4 are insurance + cap protection, not necessities.
- **Segment <= 30 s: MET at the central estimate (16-26 s); razor-thin
  (~29-32 s) at the declared band top** — declared MET only at M-D/M-E
  under the pessimistic-end standard; if thin: H2 residue, O4, N8 restore
  margin (already sequenced).
- Counterfactuals (what makes the mandatory set mandatory): without an
  L5-CLASS record compression (M5): callback record alone 111 s > 30 s
  and no-L5 campaign caps ~45-55 min — BOTH targets fail (the F6-amended
  executor QUALIFIES as the L5-class lever; true L5 stays N1). Without M3:
  segment ~50-59 s — MISS. Without a Hessian lever (M6): 22-39 s —
  straddles, not met of record. Without M1: band-top breaker post-M5,
  MISS pre-M5. Without M4: M6 is a net loss and M5 relapses into the
  measured 803 s churn — MISS. Campaign-items-only: ~43-55 min — MISS.

Stacking/overlap ledger (no gain double-counted): M3 multiplies every
compiled event — counted ONCE via post-M3 pricing of each row. M1 (record
COUNT) x M5 (record COST) orthogonal. M4 quoted post-M3. M2 independent
(matched-point count). solve_cert subsumed by M5c once landed; MARCH-F4
subsumed by M5's in-trace seeds except wall_search cells (fallback role);
bracket scan NOT subsumed (per-record). ENV-F2 = 0 speed. Cache env-var =
0 for campaign carriers. The dead screen would have overlapped H1+M5 on
the same event class. CAMPAIGN-F2 post-M5 residual ~25-35 s/boundary, not
additive with its today-priced headline.

## 6. Execution order of record + STOP-WHEN-MET

ONE order of record (red-team repair — the dependency graph, not the item
numbering):

```
M0 re-baseline + ledger
 ├─> M1 record dedup      ─┐ (free, zero numeric surface)
 ├─> M2 fun+jac memo      ─┤
 └─> (H6 folded in M4) cache unify (10 LoC)   [MEASURE M-A]
M4 plan-as-args + padding + cache block        [MEASURE M-B: signature churn]
M3 fused C1 closure (SESSION-BOUNDARY adoption) [MEASURE M-C incl. A-G]
M5a solve_cert -> M5b abort hooks (+H1 flag) -> M5c per-column executor
                                               [MEASURE M-D = STOP CHECK 1]
M6 vmapped Hessian (REQUIRES M4; declared version change)
                                               [MEASURE M-E = STOP CHECK 2]
H3 campaign dedup, H4 tail+persist (cap protection — before the next
   decisive campaign REGARDLESS of STOP)
H2 / H5 / O1-O4 only on measured shortfall or spare budget
[RIGOR rows execute regardless: M0, M2's n_eval, ENV-F2's derived K, O5]
```

Binding constraints restated: M4 before M6 (HARD, measured net-loss
otherwise); M4 before M5c (HARD, measured 803 s churn otherwise); M3
before M5c's final gate baseline (SOFT — gates run once on the adopted
closure and compile-heavy gates get 2x cheaper); M5a/M5b before M5c (the
executor inherits the abort semantics); M1 before everything that
re-prices records (attribution). H2 = the standing fallback branch of
M5c; its failure triggers N1.

STOP-WHEN-MET RULE: after each MEASURE checkpoint, measure the pinned pair
{one defnoz accepted-segment class, projected decisive campaign per §5} on
the post-S24 host (interleaved reps, medians, pycount declared; the S24
run must have ENDED). Targets declared MET only at the PESSIMISTIC end of
the measured band (the band is the margin — no magic margin constant).
Once met: remaining SPEED items are NOT implemented (anti-overengineering
pin); [RIGOR] rows execute regardless (never-postpone-resolvables); named
conditionals stay named. Rabbit-hole boundaries per item: each mandatory
item carries its session-cost cap from §4; a gate that REJECTS its lever
(M4 warm-path, M5c equivalence) routes to the named fallback (H2/N1),
never to unbounded in-session debugging.

## 7. Standing meta-rows

**7.1 — G0/T2 review inputs** (queued since S18; S25 consumes with M0/M2):
truthful lhs ~102-108 compiled evals (not 67); 67 = 50 Hessian + 17 walk
(double-count named); T2 pricing convention (one value_and_grad per eval,
true eval wall ~60-70 s — the 400 s ledger closes); the S18 cost is
STRUCTURAL (records + curvature), not language throughput (T1 1.593 /
T2a 0.116 vs 1.197 both PASS). Post-M2 n_eval counts actual compiled
executions.

**7.2 — Version/SOTA verdict of record (the user's self-limiting question,
CLOSED):** the stack is NOT self-limiting — jax+jaxlib 0.11.0 = PyPI
latest, scipy 1.18.0 latest, Python 3.13.14 current (verified live);
numpy 2.5.1 -> 2.5.2 = O5 adopt-with-rejector; Python 3.14/3.14t =
declare-not-adopt (N7, jaxlib cp313 GIL wheel). Feature-ledger declines
verified against installed source (donate_argnums, remat vs existing
custom_vjp, GPU-only autotune caches). No version chase is a plan item;
the 5-20x lives in structure.

**7.3 — SOTA survey rows (adopt-or-declare, registered):**
S1 Hessian coloring: scipy group_columns ADOPT (coloring only);
approx_derivative DECLINE (own step machinery = constraint-7 violation);
ColPack DECLINE (no maintained binding; ~0-1 eval delta at n~10); HVP
DECLINE-as-default (= N5); quasi-Newton reuse OUT by policy.
S2 external interpolation/thermo: interpax DECLINE (no structural
cp = dh/dT, no monotone-no-clamp certificate; re-opens [X-THC1] for less
than ENV-F1's measured in-house 6.6x); diffrax DECLINE (wrong object);
in-house quintic KEPT.
S3 compile-cache management: built-in jax_compilation_cache_max_size LRU
ADOPT (verified installed, config.py:1584-1594); hand-rolled pruning
DECLINE. check_contents corruption rejector verified settable.
S4 byte-exact memoization: hand one-slot/per-rung dict on exact bytes
ADOPT (jax deliberately does not memoize executions; scipy ScalarFunction
verified not to cover the f/g duplication); joblib.Memory / lru_cache
DECLINE.

**7.4 — R4/theory duties handed to their owners (none executable in this
read-only session):** none of the plan items changes theory content; the
speed plan touches M0/D-docs ONLY via (i) the G0/T2 review row (owner:
S25, existing queue), (ii) any adopted DECLARED version change (M3, M6)
being logged in the session log + PROGRESS per R3/R4 as usual at S25.

**7.5 — Parallel-session coexistence (declared):** a concurrent parallel
session is building a SOTA/rigor/completeness gap map of the whole
algorithm construction (mesh/AMR/DWR etc.). Perimeters are disjoint by
mandate (this audit: speed at equal rigor; that one: construction
completeness); both feed S25/F2. No dependency is taken here on its
output.

## 8. Quarantine (did not converge; the evidence that unblocks)

- **Q1** — P5 colored-FD sparsity structure: bandedness UNPROVEN (the
  "banded spline structure" claim conflates basis overlap with the
  field-coupled Hessian). Unblock: spline-DoF coupling derivation + one
  clean-host full-FD fill probe. Until then N8 conditional, nothing booked.
- **Q2** — A-G (M3's gain on the GRADIENT pass): measured share >= 0.85 is
  of the SOLVE. Unblock: M-C measurement. Falsifier consequence declared
  in §5.
- **Q3** — A-S (bucket-signature stability across production segments):
  measured only negatively (a large bump changed the signature at the
  reduced instance). Unblock: M-B churn-rate report; if signatures churn,
  M4's economy degrades toward cache-only and the compile budget grows
  (campaign target holds to ~5+ signatures/rung).
- **Q4** — H1's abort-fraction multiplier (2x vs 20x): first-uncertified-
  cell position never measured. Unblock: log read of the first
  post-8761dce ART_CAMP.partial (offline).
- **Q5** — stall-stop class: artifact absent; equal-outcome premise false;
  gain underivable. Unblock: post-8761dce artifact + base-identity
  verification; re-propose via pre-registration (N4).
- **Q6** — exact post-M5 campaign-layer residual: settled empirically at
  M-D; H3/H4 justified independently (cap protection, audit hardening).

— end of advisory —
