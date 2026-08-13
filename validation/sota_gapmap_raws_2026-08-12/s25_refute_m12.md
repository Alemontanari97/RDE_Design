# ADVERSARIAL REFUTATION — S25 M1+M2 "bit-transparent memos + truthful counters"

Date: 2026-08-12. Refuter: source-only (NO Python/jax executed; the executable
half of the proof is owned by the committed gates — this document attacks the
SOURCE of the claim). Target: the uncommitted working-tree edits in
`validation/a1_toc_variational_jax.py` (M1 record memo + failed-record memo,
M2 `_vg` memo, T2 pricing repair), `validation/margin_governor.py` and
`validation/def_twin_falsifier.py` (m+gm memos), read against
`validation/engine_speed_bench.py` (m12gate), the S-SPEED dispatch/advisory
pre-registration, and every repo consumer of the touched quantities.

TARGET CLAIM: the M1+M2 edits are BIT-TRANSPARENT (they change WHO computes,
never WHAT) and their counters are truthful.

Verdict grammar: REFUTED-THE-EDIT / HOLDS / HOLDS-WITH-CAVEAT. Line numbers
are the CURRENT working tree (post-edit).

---

## Findings

### F1 — Counter-reconciliation identity is NOT an invariant of the edit
- **Claim attacked**: "counters reconciled … trajectory record events
  reconcile (ON fresh + cached + failmemo == OFF fresh)" — run_trsqp
  docstring (a1_toc:988-994) + the m12gate check
  (engine_speed_bench.py:336-338).
- **Attack**: a `failmemo` hit replays a record failure of EITHER kind, but
  the two kinds ledger differently. (i) CERT-type (record SUCCEEDS, gate
  raises): OFF pays callback fresh (a1_toc:1367-1371) + segment-top fresh
  (1118-1122) = 2; ON pays callback fresh 1 + failmemo 1 = 2. Identity holds.
  (ii) MARCH-type (run_toc_record RAISES internally: axial-margin rejector
  a1_toc:271-276, wall_search no-land 362-363): the `fresh` increment sits
  AFTER the call at BOTH sites, so OFF counts 0 for the episode while ON
  counts failmemo = 1 → `sum(ON) == OFF_fresh + 1`. The gate check fires a
  FALSE FAIL on a perfectly transparent memo.
- **Verdict**: REFUTED-THE-EDIT (the reconciliation identity as claimed and
  as gated; the individual counters are honest event counts).
- **Evidence**: a1_toc_variational_jax.py:1077-1122 (top), 1365-1404
  (callback), engine_speed_bench.py:336-338; march-failure reachability:
  a1_toc:271-276 (live path — S20/S21 rejected-designs history).
- **Severity**: MEDIUM — false-negative direction only (the gate can wrongly
  REJECT, never wrongly accept; the short certified-start gate walk is
  unlikely to exercise it, so the unsoundness is latent), but the docstring
  states the identity unconditionally.
- **Repair**: split the counter (`failmemo_cert` when `fail_slot["worst"]`
  is not None vs `failmemo_march`), gate identity =
  `ON(fresh + cached + failmemo_cert) == OFF(fresh)`; or count a raising
  record ATTEMPT in a dedicated counter in both arms.

### F2 — Record-memo key omits the module globals the record depends on
- **Claim attacked**: "Inside one run_trsqp walk these are fixed by scope —
  the tag makes the invariant EXPLICIT" (record_ctx_tag docstring,
  a1_toc:930-946).
- **Attack**: `run_toc_record` output depends on `TV.M_NODES` / `TV.KNOT_XI`
  (wall_geometry, a1_toc:176-179) and on `A1.N_NEWTON` (cell certification
  cap). None is hashed into the tag, and `ctx` is computed ONCE at walk
  start (1042), so even extending the tag would not catch a MID-WALK
  mutation. Today every caller mutates the class only AROUND run_trsqp
  (def_twin:450-463, 574-581, 950-951/1117; adaptive_knot_optimize design
  class ctx-mgr:117-134; engine_speed_bench:121-128, 150-151, 287-288) —
  transparency HOLDS on the current call graph by scope, not by key. The
  S24-named pre-authorized "joint mesh+knot refinement" session is exactly
  the future in-walk mutator that would make the memo serve a stale record
  SILENTLY (the first-hit probe fires once per walk, likely before the
  mutation).
- **Verdict**: HOLDS-WITH-CAVEAT (transparent today; the EXPLICITNESS claim
  of the docstring is false as stated — the invariant lives in caller
  discipline, not in the key).
- **Evidence**: a1_toc:176-179, 930-946, 1042, 1077, 1387; certdiag's own
  N_NEWTON x10 mutation (1151-1172, restored in finally, memo untouched —
  verified safe).
- **Severity**: MEDIUM (latent staleness channel with a NAMED future
  consumer).
- **Repair** (~3 lines): build the key as
  `(ctx, int(TV.M_NODES), (None if TV.KNOT_XI is None else
  np.asarray(TV.KNOT_XI, float).tobytes()), int(A1.N_NEWTON), W.tobytes())`
  re-read AT EACH key construction (both sites), not once per walk.

### F3 — Replayed failures diverge textually from the OFF arm (messages + artifacts)
- **Claim attacked**: "bit-transparent … acceptance evidence = bit-identical
  walk" (a1_toc:986-989).
- **Attack**: on a replayed CERT-type failure the ON arm raises
  "P3(ii): accepted iterate not certified … [replayed callback record
  failure, M1 memo]" (1087-1088 replaying 1378-1380) where the OFF arm's
  segment top raises "P4 gate: record at segment base not certified …"
  (1124-1127). On MARCH-type replays only the suffix differs. These strings
  land in `rejected_designs[].error` (1129-1140 → A1_REJ_SAVE JSON) and in
  the console `[seg %d] base REJECTED (%s)` line (1183-1185) → the A/B
  artifacts are NOT bit-identical on failure trajectories. Grep of every
  consumer: def_twin:753 prints `str(err)[:80]`; margin_governor:516 stores;
  locus_diagnosis parses W/m_nodes/knot_xi, never `error` — NO consumer
  parses the text, so behavior is unaffected.
- **Verdict**: HOLDS-WITH-CAVEAT (numeric transparency intact; the
  bit-transparency claim must be SCOPED to numeric outputs — logs and the
  T5 rejected-designs artifact diverge ON vs OFF).
- **Evidence**: a1_toc:1087-1088, 1124-1127, 1129-1140, 1183-1185,
  1378-1380; consumers def_twin_falsifier.py:753,
  margin_governor.py:510-516, locus_diagnosis.py (no error-string reads).
- **Severity**: LOW.
- **Repair**: one registration line scoping the claim; optionally stash the
  would-be P4 text for cert-type replays.

### F4 — Probe tax is real wall-clock on cap-bounded campaigns, undeclared
- **Claim attacked**: "they change WHO computes, never WHAT" — read against
  the BY-RULE wall-clock cap semantics of the decisive campaigns.
- **Attack**: `A1_MEMO_PROBE` defaults ON (1046-1047); every ON walk with at
  least one cached hit executes one EXTRA full record (o2, 1094-1096),
  uncounted (declared structural). def_twin's decisive campaign runs one
  run_trsqp per rung-ATTEMPT (def_twin:1001, plus C3 re-frozen repeats,
  1044-1049) and nothing sets A1_MEMO_PROBE=0; at the twin net a record is
  ~17-18 s of record (X-LSG0), so a 4-6 rung ladder pays ~+1-2 min against
  the 2 h BY-RULE cap and the S-SPEED "campaign <= 25 min" target. Values
  are untouched, but under a BY-RULE cap stop, wall-clock changes WHICH
  rungs complete — the campaign TRAJECTORY of record is not
  time-transparent. The probe cost is absent from the advisory §5 segment
  synthesis rows.
- **Verdict**: HOLDS-WITH-CAVEAT (value-transparent; time-tax undeclared
  where time is verdict-bearing).
- **Evidence**: a1_toc:1046-1047, 1093-1096; def_twin_falsifier.py:1001,
  1044-1049, 1098-1102 (the cap-motivated .partial dump);
  engine_speed_bench.py:216-224 (synthesis rows, no probe term).
- **Severity**: LOW-MEDIUM.
- **Repair**: after m12gate acceptance, set A1_MEMO_PROBE=0 inside the
  campaign entry (or add the probe seconds to the declared budget).

### F5 — Probe cadence weakened vs the pre-registration (V12)
- **Claim attacked**: "first-hit controls … V12 cadence: once per walk,
  structural" (a1_toc:1034-1037).
- **Attack**: the advisory's M1 constraint (5) declares "fresh-record
  equality probe, cadence per V12 (once per STAGE BOUNDARY, structural not
  counted)" (ADVISORY_engine_speed_audit_2026-08-12.md:194-195). The
  implementation probes ONCE PER WALK (`probe["eq"] == 0`, a1_toc:1093).
  Per-boundary probing would nullify M1's gain (the probe IS a record), so
  the weakening is defensible — but the code comment silently REWRITES the
  registered cadence instead of declaring the interpretation.
- **Verdict**: HOLDS-WITH-CAVEAT (registration hygiene; the m12gate A/B
  covers the equality property wholesale).
- **Evidence**: a1_toc:1034-1037, 1093;
  ADVISORY_engine_speed_audit_2026-08-12.md:194-195;
  DISPATCH_Sspeed_to_S25_2026-08-12.md:37-38.
- **Severity**: LOW.
- **Repair**: one registration line in the M1 block declaring
  once-per-walk as the adopted V12 reading (rationale: probe = one record).

### F6 — M2's pre-registered negative controls are not implemented anywhere
- **Claim attacked**: M2 counters truthful + "acceptance evidence" complete.
- **Attack**: the advisory M2 acceptance names "bitwise-equality assert on a
  KAT segment; 1-ulp perturbed u misses (negative control)"
  (ADVISORY_engine_speed_audit_2026-08-12.md:200-209). Neither exists:
  `_vg` (a1_toc:1257-1269), `_mvg` (margin_governor.py:226-238,
  def_twin_falsifier.py:668-687) carry NO first-hit control, and the
  m12gate checks only A/B bit-identity + `n_eval ON < OFF` + M1's probe
  rows (engine_speed_bench.py:321-348). The A/B walk subsumes end-to-end
  value equality, but the M2 memo has no in-driver key-collision rejector
  of its own (M1 got one; M2 did not). Note also the m12gate docstring
  promises bit-identical "(W, J, n_segments, wall)" (engine_speed_bench:26)
  but no wall comparison is implemented (321-328) — implied by W identity +
  determinism, yet the promised check is absent.
- **Verdict**: HOLDS-WITH-CAVEAT (pre-registered controls dropped without a
  declaration; transparency itself unrefuted).
- **Evidence**: as cited above.
- **Severity**: LOW-MEDIUM.
- **Repair**: mirror the M1 pattern once per walk in `_vg` (fresh recompute
  + bitwise compare + `nextafter` key-miss), or register the A/B gate as
  the superseding control.

### F7 — n_eval semantic break vs the normative T2 text (R4 delta pending)
- **Claim attacked**: "n_eval … the S18 ledger truth repair of record" with
  no consumer breakage.
- **Attack**: code consumers survive (margin_governor.py:397 uses `> 0`,
  always true since precond/Hessian execute fresh; def_twin never reads
  n_eval; bench artifacts self-labeled; a1_toc:1786 print is reporting).
  BUT the T2 falsifier of record is normative TEXT elsewhere:
  docs/rde_nozzle_brick2_kickoff.md:268-272 prices
  "N_TR x (solve_JAX + grad_JAX)" and the claims map row
  (AUDIT_agnostic_2026-08-07.md:567, ADVISORY_claims_to_code) quotes
  "N_eval x (t_solve + t_grad)". The code now computes
  `lhs_T2 = opt["n_eval"] * t_grad` (a1_toc:1880). The repair is
  pre-adjudicated in ADVISORY_engine_speed_audit §7.1 (581-588, "not 67",
  one value_and_grad per eval) and the legacy double-priced figure is
  printed alongside (1886-1889) — good continuity — but per R4 the
  normative T2 statement in the kickoff/claims docs must receive the same
  session's delta or the claim-of-record and its verifier disagree.
- **Verdict**: HOLDS-WITH-CAVEAT (repair coherent and pre-adjudicated;
  R4 retro-propagation to the normative docs still open in-session).
- **Evidence**: a1_toc:1868-1889; docs/rde_nozzle_brick2_kickoff.md:268-272;
  AUDIT_agnostic_2026-08-07.md:567;
  ADVISORY_engine_speed_audit_2026-08-12.md:581-588.
- **Severity**: LOW (process/timing).
- **Repair**: land the T2-convention delta in the kickoff §5bis/claims map
  in the S25 R3/R4 close.

### F8 — "t_grad IS the measured whole value_and_grad wall" is an identification, not a measurement
- **Claim attacked**: the T2 repair comment (a1_toc:1876-1877).
- **Attack**: t_grad times `jax.jit(jax.grad(scalar_J))` (a1_toc:1770-1774),
  a DIFFERENT compiled object from the walk's
  `jax.jit(jax.value_and_grad(scalar_J))` (1243). jax.grad internally runs
  the full forward+backward so the walls coincide up to primal-output
  plumbing/DCE, but the identity is asserted without a band, in a repo
  whose standard is measured bands.
- **Verdict**: HOLDS-WITH-CAVEAT.
- **Evidence**: a1_toc:1770-1776 vs 1876-1880.
- **Severity**: LOW.
- **Repair**: time `val_grad` itself for the T2 constants (2 lines), or
  declare the grad≈value_and_grad identification.

### F9 — M2 one-slot lifecycle, key discipline, and consumers
- **Claim attacked**: `_vg` transparency across ALL five consumers; slot
  staleness across segments; in-place mutation of the returned gradient.
- **Attack ran dry**: `vg_slot` is created fresh per segment beside its own
  `val_grad` (a1_toc:1243, 1255) — no cross-segment leak is possible
  (closure-local); grep confirms NO residual direct `val_grad(` call site
  (definition and `_vg` body only), so `n_eval` misses nothing in its
  declared scope; precond/g_base/Hessian/f_np/g_np all route through `_vg`
  (1281-1282, 1308, 1314, 1323, 1333). No consumer mutates the returned
  gradient in place (f_np discards it; g_np/gm_np `g * Dv` allocates;
  Hessian/precond arithmetic allocates) — noted asymmetry: the FRESH path
  returns the possibly read-only `np.asarray` view of the jax buffer while
  the CACHED path returns a writable `.copy()` (1262 vs 1265); a future
  in-place consumer would crash on fresh and silently work on cached, i.e.
  loudly-or-correctly, never corrupting. Keying on PHYSICAL W bytes
  (`u * Dv`) instead of the advisory's `u.tobytes()` is BENIGN and strictly
  finer: the key IS the argument of the compiled function, so any u-space
  collision that collides in W_phys returns the value the legacy path would
  have computed for that identical compiled input. Nonfinite v/g replay the
  deterministic legacy handling with IDENTICAL nf_events increments per
  call (1324-1331, 1335-1343).
- **Verdict**: HOLDS (asymmetric-writability note only).
- **Severity**: none (informational).

### F10 — M1 stash aliasing / deepcopy
- **Claim attacked**: deepcopy of jax arrays; aliasing via plan reuse into
  make_run_toc_scan_jit / thrust_J / dec_base / margin factories.
- **Attack ran dry**: jax 0.11.0 (verified installed) supports
  copy/deepcopy of Array (and jax arrays are immutable regardless); the
  slot is consumed ONE-SHOT and cleared (1090-1091) so no two consumers
  ever share the stashed objects; downstream only READS plan (plan_operands
  copies into fresh numpy operands; dec_base builds tuples; margin
  factories close over jnp.asarray copies). A deepcopy failure would raise
  a non-RuntimeError → propagates loudly, never absorbed as a rejected
  design. Per-accepted-iterate deepcopy cost is O(plan bytes), noise vs a
  record.
- **Verdict**: HOLDS.
- **Severity**: none.

### F11 — Spurious AssertionError channels for the first-hit controls
- **Claim attacked**: the probe can fire on legit nondeterminism
  (wall-search tie-breaks, cert_worst float equality, NaN).
- **Attack ran dry**: run_toc_record is deterministic in-process for fixed
  (W, tab, cfg, state_fn, solvers, globals): the wall_search loop
  (356-376) is pure float comparison, no tie-break source; XLA CPU
  numerics are run-to-run deterministic for the same compiled fns;
  `cert_worst` can NEVER be NaN (nonfinite ratio is coerced to +inf,
  246-251) and an inf record fails the callback cert gate BEFORE the stash
  (1377-1381 precedes 1382-1389), so a cached record always has finite
  cert_worst and the `NaN == NaN` equality trap is unreachable; certified
  walls carry no NaN, so `np.array_equal` is safe. The probe leaves no
  state (o2/p2 discarded; no module writes; Wp_ is a copy — W is never
  mutated, a1_toc:1108-1109). AssertionError escapes every repo handler
  around the walk (def_twin:1005, margin_governor:510 are
  except-RuntimeError; the broad except-Exception sites are res.v
  extraction and bench fallbacks). CAVEAT: under `python -O` the asserts
  strip and `memo_probe_pass/miss` would still increment (1104-1113) —
  the counters would then claim controls passed that never executed; no
  repo runner uses -O, but the counter is truth-conditional on standard
  invocation.
- **Verdict**: HOLDS-WITH-CAVEAT (the -O clause only).
- **Severity**: LOW.
- **Repair**: replace the two asserts with `if not …: raise
  AssertionError(...)` (strip-proof, same type).

### F12 — Key material and byte semantics (tobytes attacks)
- **Claim attacked**: W.tobytes() on non-contiguous/differently-strided
  arrays; dtype/shape collisions; NaN/−0.0 keys; res.x-vs-state.x bytes;
  (W/Dv)*Dv round-trip.
- **Attack ran dry**: numpy `tobytes()` serializes the LOGICAL C-order
  values regardless of memory layout, so contiguity/strides cannot split
  or merge keys; every keyed array in the edit is 1-D float64 of fixed
  length within a walk (W = asarray(W0,float) 1013; res.x*Dv 1431;
  state.x*Dv 1362; u*Dv; W±e), so no cross-dtype/shape byte collision is
  constructible in-slot; −0.0 vs +0.0 and NaN payload differences produce
  at worst extra MISSES (both arms compute fresh — transparent); res.x
  carries the same float values as the last callback state.x → identical
  bytes → the intended boundary hit; a stalled segment's
  `(W/Dv)*Dv` round-trip non-identity yields only a miss (fresh in both
  arms). The OFF arm short-circuits every memo branch on `memo_on`/`vg_on`
  (1078, 1089, 1259-1260) — the `key=None == slot None` trap is guarded.
- **Verdict**: HOLDS.
- **Severity**: none.

---

## Side observations (adjacent, not the M1/M2 target)
- OBS-A: m12gate leaves `DT.CASE` mutated (engine_speed_bench:277-279,
  462-464, no restore) — safe ONLY because main() is single-mode-per-
  process; a future multi-mode run would leak the reduced net into the
  next mode.
- OBS-B (M4 counter, since counters are the target's theme): mbwalk's Q3
  churn datum sums `_SCAN_SIGSEEN` over ALL engines built in-process
  (engine_speed_bench:486), including the prelude's — sig/segment
  overcounts walk churn.
- OBS-C: record_ctx_tag's "closure/solver identity" is
  `__qualname__` + `type(solvers).__name__` (a1_toc:934-936) —
  the solver half is information-free (always "dict"). Harmless for the
  walk-local slot; MUST NOT be reused as-is for H3/H4 stores that outlive
  the walk (H4's code-identity rule is necessary but not sufficient:
  solver/closure CONTENT identity is also needed).

## Dry-attack ledger (imagination shown, no finding)
tobytes layout/strides; dtype-shape byte collisions; NaN/−0.0 keys;
NaN cert_worst in the probe equality; wall-search tie-break
nondeterminism; res.x vs state.x bytes; (W/Dv)*Dv round-trip; in-walk
tab/cfg in-place mutation (no sites); certdiag N_NEWTON temporary
mutation (restored, memo untouched, uncounted in both arms); deepcopy of
jax arrays on jax 0.11.0; one-shot consume aliasing; in-place mutation of
returned gradients; `import os` presence in both margin files
(margin_governor:121, def_twin:92); AssertionError absorption by broad
handlers (none around the walk); probe residue/state leakage (none);
stale-but-valid rec_slot surviving reject/revert (key-match ⟹ value-match
by determinism); rejected-designs error-string parsers (none);
R-G1d `n_eval > 0` robustness under the new semantics (precond/Hessian
always execute fresh).

## Count
12 findings: 1 REFUTED-THE-EDIT (F1) · 8 HOLDS-WITH-CAVEAT (F2, F3, F4,
F5, F6, F7, F8, F11) · 3 HOLDS with the attacks run dry documented
(F9, F10, F12), plus 3 side observations and the dry-attack ledger.
