> **STATUS — CONSUMED (2026-08-13, S-ORDINE) -> validation/PROGRESS_2026-08-12_S25_speed.md.** Dispatch fully absorbed by S25 (M-chain landed; content redundant with the speed-audit advisory + S25 log, seg4-inventory verified). Full text preserved (R4).

# DISPATCH — S-SPEED -> S25 "ENGINE SPEED SESSION" (2026-08-12)
# Converged findings ONLY + the execution plan. Full adjudication record,
# dispute ledger, survey rows and quarantine:
# validation/ADVISORY_engine_speed_audit_2026-08-12.md (the advisory
# SUPERSEDES any raw panel text). Untracked ADR-pattern deliverable.

ADDENDUM AT CLOSE: S24 CLOSED during this audit (HEAD 589cc56); its
closing NEXT row independently names S25 ingesting this dispatch alongside
the parallel gap-map and the choice ledger — placement below confirmed
against the S24 closure text. The S24 decisive process has ended: M0's
clean-host precondition is satisfiable from S25's opening.

## Placement (unchanged from the S24 census)
S25 opens with the C4-first item (written placement of record, S24 log
step 3 row 3), then THIS dispatch; before full F2 opening. S25 also
consumes the queued G0/T2 review — the truthful ledger is in the advisory
§7.1 (true evals ~102-108 not 67; T2 pricing convention; verdict: the S18
cost line is STRUCTURAL — records + curvature — not language throughput).

## Targets and the rule
Segment <= 30 s and decisive campaign <= 25 min at defnoz, AT EQUAL
certification. Verdict of record: campaign MET across the band (7-15 min
with H3+H4, margin ~1.6x pessimistic; 10-20 min mandatory-only, ~1.3x);
segment MET central (16-26 s), razor-thin at band top (29-32 s) —
adjudicated ONLY at the M-D/M-E checkpoints, pessimistic end of the
MEASURED band. STOP-WHEN-MET: once met, remaining SPEED items are NOT
implemented; [RIGOR] rows execute regardless; conditionals stay named.

## Execution order of record (dependency graph; gates can FIRE and reject)

0. **M0** Clean-host re-baseline (post-S24 ONLY — the decisive run must
   have ENDED; never touch PID 44192) + C1-baseline re-declaration +
   G0/T2 ledger handoff. [RIGOR]
1. **M1** Segment-boundary record dedup + failed-record memo (driver,
   ~35-55 LoC). Key = canonical (W.tobytes, sorted-JSON cfg, table-content
   hash, closure id [, code id if persisted]); one-slot/per-rung stores.
   Control: fresh-record equality probe at stage boundaries + perturbed-W
   miss. Gain ~2x on record events today; the "base record -> 0 s" row.
2. **M2** fun+jac / m+gm one-slot memo (3 sites) + n_eval truth repair
   [RIGOR half regardless]. Bit-identical; ~5-15 s/segment.
   -> **MEASURE M-A** (attribution snapshot).
3. **M4** Plan-as-args + fixed-shape padding + generated signature
   (registered-pytree plan; NO quantization grid at landing — existing
   per-phase-max discipline; churn counter decides later, PRACTICE-tagged)
   + ONE canonical cache block (built-in LRU cap
   jax_compilation_cache_max_size, derived; check_contents at campaign
   open). Gates per signature: Newton-floor equivalence + O3.1 +
   warm-path args-vs-constants band. ~3.5-7 min/rung of recompile deleted;
   BINDING enabler for M5c/M6. The heaviest refactor (1-2 sessions).
   -> **MEASURE M-B** (signature churn rate = Q3 unblock).
4. **M3** Fused/floor-index C1 closure (SESSION-BOUNDARY adoption, fresh
   record): per-table DERIVED Newton count K (never a literal), per-table
   uniformity rejector + node-tie-amended index control; [X-THC1] C1-C7 +
   R1-R4 re-run. MEASURED 2.72x on the C1 replay, 2.0x on compile;
   multiplies every compiled event.
   -> **MEASURE M-C** (incl. A-G val_grad gain = Q2 unblock; if < 1.5x the
   segment band widens to ~18-33 s — declared falsifier consequence).
5. **M5** Compiled-record chain: (a) fused solve_cert -> (b) early-abort
   hooks at BOTH cert sites (mandatory; H1's opt-in flag + schema note
   ride along) -> (c) F6-AMENDED hoisted per-column jitted executor over
   the replay's own bucketing discipline (eager cell_scan REJECTED of
   record, 0.8x measured). Gate: dec-vector bitwise identity + z at
   Newton floor + plan bit-identity on twin + defnoz-mild; ANY plan
   difference = REJECTED -> fallback H2, shortfall -> N1. Legacy record
   behind env flag as arbitration path. Record 111 s -> 6-9 s post-M3.
   -> **MEASURE M-D = STOP CHECK 1.**
6. **M6** Vmapped FD Hessian + precond batch (REQUIRES M4): measured 2.6x
   on the Hessian block; NOT bitwise (floor-order 3.1e-07) => DECLARED
   version change gated on KAT + O3.1 re-pass; sequential fallback +
   nonfinite counter (REQ-NONSTALL strengthened).
   -> **MEASURE M-E = STOP CHECK 2.**
7. **H3** Campaign rung-boundary dedup + **H4** tail-to-derive & stage
   persistence with the CODE-IDENTITY key — schedule BEFORE the next
   decisive campaign regardless of STOP (cap protection: −630..−1270 s
   today out of the 2 h decisive window; F1b fallback fires BY RULE at
   cap exhaustion). Stale-code load must REFUSE (S24 C5 scenario replayed
   as the acceptance control).
8. Shortfall/budget only: **H1** flag+schema (hooks already in), **H2**
   NumPy predictor twin (the M5c fallback, >=1.86x measured), **H5**
   derive screen with the max-mismatch candidate band + holdout control,
   **O1-O4** per the advisory. **O5** numpy 2.5.2 [RIGOR] at any session
   boundary.

## Binding orders (all measured, not stylistic)
M4 before M6 (vmap compile 30.86 s/rebuild = net loss otherwise); M4
before M5c (803 s per-shape churn measured otherwise); M3 before M5c's
final gate baseline (soft; gates run once on the adopted closure); M5a/b
before M5c; M1 before anything that re-prices records.

## Named conditionals (owner + trigger — never default)
N1 true-L5 compiled record (F2; M5c-rejected + H2-insufficient); N2
traced-screen as gate (F2; material probe share + shadow agreement bound);
N3 drift-repeat semantics (panel; post-8761dce artifact + O2 data); N4
stall-stop re-proposal (F2; artifact + base-identity); N5 jacfwd Hessian
(adjudication-only); N6 segment merge (own panel); N7 Python 3.14/3.14t
(M5+H2 both rejected); N8 colored FD via measured pattern + scipy
group_columns coloring-only (Q1 derivation + M6 shortfall).

## Quarantine (NOT dispatched; unblock evidence named)
Q1 Hessian sparsity derivation; Q2 A-G gradient-pass gain (M-C); Q3
signature stability (M-B); Q4 abort fraction (first post-8761dce
ART_CAMP.partial log read); Q5 stall-stop artifact; Q6 post-M5 campaign
residual (M-D). Details: advisory §8.

## Dead rows (do not resurrect)
Screen-as-gate; dispatch-amortization Hessian story; 6x replay headroom;
derive-batching premise; seed-anchored screen band; eager cell_scan
record; external interpolation libs / tabulated T(h) inverse; L4 on
early-exit searches; Jacobi-precond removal; cache env var as carrier
speed lever.

## Terms carried
Constraints (1)-(7) verbatim in the advisory §0/§4 preamble; S14-S24
verdicts not re-litigated; every adopted DECLARED version change (M3, M6)
logs per R3/R4 at S25; all current bench absolutes are contended —
M0 re-anchors before any acceptance verdict; anti-overengineering: each
item stops at its cost cap and routes to its named fallback, never into
unbounded in-session debugging.

— end of dispatch —
