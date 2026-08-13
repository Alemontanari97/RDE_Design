# S25 M4 ADVERSARIAL REFUTATION — plan-as-args engine + engine cache + H6 cache unification

Source-only refuter pass (no Python/jax executed; clean-host measurement running,
executable half owned by [X-SPDB] m4gate). Target = the UNCOMMITTED working-tree
edit on `validation/a1_toc_variational_jax.py`, `a1_ideal_march_jax.py`,
`o33_bench.py`, `o32_mesh_convergence.py`, `a1_loopspeed_bench.py` (companion
uncommitted edits noted in F14). Date 2026-08-12.

TARGET CLAIM: the M4 edit preserves the algorithm (same march, same certification
metric, same adaptive semantics) within its DECLARED gates (Newton-floor
equivalence; bitwise NOT promised), the engine cache can NEVER return a wrong
engine, and the H6 cache unification is behavior-safe.

Verdict codes: REFUTED-THE-EDIT / HOLDS / HOLDS-WITH-CAVEAT.

---

## F1 — Engine-cache key omits `TV.KNOT_XI` / `TV.M_NODES`: a same-shape knot change returns a WRONG engine — VERDICT: REFUTED-THE-EDIT (the "can never return a wrong engine" half). SEVERITY: HIGH

**Claim attacked**: "its engine cache can never return a WRONG engine."

**Evidence**:
- `a1_toc_variational_jax.py:886-887` — ekey = `(id(tab), id(state_fn),
  id(solvers), mode, NI, Nw, yt, rtu, rtd, L)`. Nothing else.
- `a1_toc_variational_jax.py:176-179` — `wall_geometry` (closed over by the
  jitted body via `run` line 728) reads the MODULE GLOBALS `KNOT_XI` and
  `M_NODES` at TRACE time: `if KNOT_XI is None: xi = jnp.arange(1, M_NODES+1)/M_NODES
  else: xi = jnp.asarray(KNOT_XI)`. The knot vector is baked into the compiled
  executable as a constant; it is in neither the ekey nor the operand pytree.
- The repo's STANDARD pattern mutates exactly these globals around make calls:
  `adaptive_knot_optimize.py:127-135` (`design_class.__enter__` sets
  `TV.KNOT_XI = self.xi`), used at `adaptive_knot_optimize.py:228-232`
  (`grad_and_J` builds the engine INSIDE `design_class(xi)`);
  `o33_bench.py:452-454` (`march_design` forces `KNOT_XI = None` around a
  cached make at :461) while `o33_bench.py:582-584` sets the AMBIENT class to
  an ADAPTIVE artifact xi in the same process; `margin_governor.py:264-267`
  (`baseline_val_stats` under `design_class(xi, ...)`);
  `def_twin_falsifier.py:451/575/951/1249/1261` (set/restore pairs).

**Failure mechanism**: two `make_run_toc_scan_jit` calls with the same
(tab, state_fn, solvers, mode, NI, Nw, geometry) ids but DIFFERENT `KNOT_XI`
of the SAME length (or None vs an array whose length equals the current
M_NODES) produce the same ekey AND the same jax abstract signature (W shape
(M+1,), same ops shapes) → cache hit, NO retrace → the returned engine
evaluates the wall spline on the FIRST call's knots. Silent: no churn row
(sig unchanged), and the poisoned call sites (`grad_and_J`, `march_design`
grad branch, `baseline_val_stats`) never compare replay vs record — the
record-fidelity monitor lives only in `run_trsqp` (line 1233). The stale
gradient feeds VERDICT-BEARING rows ([D1] corner row via `goal_metric`,
governor val lanes).

**Why today's carriers survive by accident**: every in-process class change
observed either changes len(W) (knot INSERTION grows M → new W shape →
retrace re-reads the globals → correct) or uses distinct tab/solvers ids.
Uniform-vs-adapted comparisons at EQUAL node count in one process (o33
ambient-adaptive + march_design(n_nodes) with n_nodes == len(W_STAR)-1, or
any future fixed-M knot MOVE — the S24 "joint mesh+knot refinement" named
conditional is exactly a knot-move workload) hit the hole. The legacy path
(`A1_PLAN_ARGS=0`, fresh jit per make, line 881-884) is immune, so the
declared m4gate A/B cannot see it either (the gate never exercises a
same-shape class change: `engine_speed_bench.py:379` pins one class).

**One-line repair**: fold the class into the key and the memo tag — e.g.
`ekey += (int(TV.M_NODES), None if TV.KNOT_XI is None else
np.asarray(TV.KNOT_XI, float).tobytes())` (and add the same two fields to
`record_ctx_tag`, see F10); alternatively pass `xi` as a traced operand in
`ops` (shape-covered by construction, V2-consistent).

---

## F2 — kk/n_B → kkf association drift: quantified entry and gate coverage — VERDICT: HOLDS-WITH-CAVEAT. SEVERITY: LOW (as gated)

**Claim attacked**: the declared Newton-floor gate genuinely covers the
last-ulp association change.

**Where the drift enters** (only replay-side):
- Old jit body (committed): `th = thB*kk/n_B`, `x4c = xB + (L-xB)*kk/Nw` —
  fl(fl(a·k)/n). New body (`a1_toc_variational_jax.py:814,818`):
  `th = thB*kkf`, `x4c = xB + (L-xB)*kkf` with `kkf = fl(k/n)` precomputed
  (`plan_operands`, :592-595) — fl(a·fl(k/n)). Generic disagreement 1-2 ulp
  of th/x4 (exact only when n_B, Nw are powers of two; at k=n the new form
  gives exactly thB while the old could be 1 ulp off).
- Propagation: station (x4,y4,sl) → `spline_eval` → wall-cell problem `p_w`
  → `s_wal` Newton solve → wall row → `thrust_J` / O3.1 / F-branch bands.

**Decision path is BIT-PRESERVED**: the wall search (N, Nv) and n_B live
ONLY in `run_toc_record` (:332-341, :220), which is UNTOUCHED and keeps the
old association — so "same adaptive semantics" holds bitwise; no (N,Nv)
near-tie can flip from this edit. The eager `run_toc_scan` (:506,511) also
keeps the old association (see F13).

**Verdict-bearing sub-band consumers checked**:
- `run_trsqp` monitor (i) (:1233-1238) and main() jit-fidelity row
  (:1687-1692) and m4gate "args replay fidelity vs record"
  (`engine_speed_bench.py:403-405`): all compare NEW-replay vs OLD-record
  with band `NEWTON_TOL_FACTOR·EPS·scale·10 = 1000·EPS·scale`
  (NEWTON_TOL_FACTOR=100, `a1_ideal_march_jax.py:181`). Station-coordinate
  drift ~2 ulp relative (~4e-16·scale) and the solved-u drift through the
  certified Newton (Lipschitz·ulp) sit ≥2-3 orders below the band. These
  rows are live rejectors: if the estimate is wrong they FIRE.
- O3.1 dot-product rows: FD and AD both run through the SAME kkf engine —
  drift is common-mode, cancels.
- [D1]/F7/oracle bands are Richardson/two-resolution-derived (e.g.
  `o33_bench.py` R3 band, F7 band K_RICH·|J_M − J_2M|) — 6-12 orders above
  ulp drift.

**The caveat (the honest residue)**: trust-constr accept/reject near-ties
CAN flip on an ulp of J/g → a DIFFERENT walk trajectory than the committed
baseline. No gate compares walks pre-edit vs post-edit (m12gate A/Bs memo
on/off on the SAME engine; m4gate compares single evaluations). This is
inside the DECLARED scope ("bitwise NOT promised") and every landed design
re-certifies independently — but trajectory-level reproducibility of the
committed S24 numbers is finished the moment this lands. State it in the
adoption record. **Repair**: one sentence in the M4 registration block
declaring trajectory non-reproducibility vs pre-edit; optionally fold kkf
into `run_toc_record`'s station loop too so record and replay share one
association again (removes the record-vs-replay ulp asymmetry entirely).

---

## F3 — The A/B "args-vs-constants" arbitration CANNOT arbitrate the arithmetic drift — VERDICT: HOLDS-WITH-CAVEAT. SEVERITY: MEDIUM

**Claim attacked**: `A1_PLAN_ARGS=0` is the arbitration path of the M4 gate.

**Evidence**: the legacy branch (`a1_toc_variational_jax.py:881-884`)
rebuilds THE SAME `run` body with ops CLOSED OVER — including `arc_kkf`.
`plan_operands` runs before the env check (:689). So both m4gate arms
(`engine_speed_bench.py:385-390`) share the NEW association; their
"Newton-floor equivalence" row (:396-402) measures ONLY the
args-vs-constants mechanism (trace/fusion differences), NOT the kk→kkf
change. The drift is covered solely by the fidelity-vs-record rows (F2).
Anyone reading "legacy" as "pre-edit numerics" is misled: the pre-edit
association survives nowhere runnable — only in git.

**Repair**: rename the flag's docstring ("legacy CONSTANTS-BAKED variant of
the NEW body; pre-edit arithmetic is git-only") — one comment line; the
fidelity-vs-record row stays the drift gate of record.

---

## F4 — "~37-90 s/segment recompile deleted" is over-claimed for the walk driver: jit-under-jit does not reuse the cached engine executable — VERDICT: HOLDS-WITH-CAVEAT (speed claim, measurement-owned). SEVERITY: MEDIUM

**Claim attacked**: "same-shape plans REUSE the compiled engine across
segments … the measured ~37-90 s/segment recompile deleted" (comment,
`a1_toc_variational_jax.py:679-688`).

**Evidence**: in `run_trsqp` the engine is consumed in two ways per segment:
(a) DIRECT call — monitor (i) `runj(jnp.asarray(W))` (:1233): true
executable reuse, recompile genuinely deleted; (b) UNDER AN OUTER TRACE —
`val_grad = jax.jit(jax.value_and_grad(scalar_J))` (:1241-1243), rebuilt
EVERY segment, where `runj(Wv)` is traced INTO the outer graph: the inner
pjit's compiled executable is NOT executed under tracing; `ops_j` enter the
outer jaxpr as CONSTANTS. The outer forward+backward XLA compile (the
expensive one) recurs per segment unless (i) jax's constant handling hoists
large consts out of the serialized module AND (ii) the H6 persistent cache
hits on the then-plan-independent module. Both are jax-version-contingent
(pinned jax 0.11 per the H6 comment) and NOT establishable from this source.
Same structure in `make_margin_factory` (margin_governor.py:213) and
def_twin's factory.

**Coverage that exists**: `engine_speed_bench.py` mode_mbwalk + md/me
STOP-WHEN-MET rows measure walk segment time against the ≤30 s target — the
residual val_grad recompile, if present, will show there and the gate can
fire. **Repair**: scope the source comment to "the REPLAY-path per-segment
recompile" and let mbwalk/md-me carry the walk-level claim; if the residual
recompile survives measurement, the next lever is passing `ops` as
ARGUMENTS through `scalar_J`/`val_grad` too (same M4 pattern one level up).

---

## F5 — `id(tab)` keying vs in-place tab mutation — VERDICT: HOLDS-WITH-CAVEAT. SEVERITY: LOW (today), latent

**Claim attacked**: id-keying + pinned strong refs make stale closures
impossible.

**Evidence**: dealloc-reuse collisions are genuinely closed — the cache pins
`(tab, state_fn, solvers)` (`a1_toc_variational_jax.py:890-893`), so a dead
id can never be re-issued while the entry lives. The remaining hole is
IN-PLACE CONTENT mutation (same id, new content): the ONLY writer in the
tree is `prep_tab` — `a1_ideal_march_jax.py:1052` `tab["_as"] = float(q)` —
which is deterministic-idempotent from tab's own (gammamedio, Rg, ts)
(80 fixed Newton trips), so re-calling it cannot change content; no carrier
mutates `gammamedio`/`Rg`/`ts`/array leaves after build (grep: the negative
controls copy first, `thermotab_c1_jax.py` R1/R5 use `dict(tab_n)`).
Closure constants `gm`, `as_`, `ta` (:711-713, :665) therefore stay valid.
But the contract is IDENTITY-based while the M1 memo one file down uses a
CONTENT hash (`record_ctx_tag`, :930-945) — two standards; one future
in-place table edit (e.g. a gamma-sweep reusing one dict) poisons every
cached engine silently. **Repair**: assert-freeze (hash tab leaves at first
build, cheap re-check per make under a debug env) or document the
no-in-place-mutation contract next to `_SCAN_ENGINES`.

---

## F6 — `da_deg` and the full cfg-field enumeration — VERDICT: HOLDS

**Claim attacked**: cfg carries more keys than the ekey covers (da_deg
wrong-engine reuse).

**Evidence**: the jit make reads EXACTLY `NI, Nw, yt, rtu, rtd, xtronc`
(:674-676) — all in the ekey. `da_deg` is consumed ONLY by
`run_toc_record:213,220` where it fixes `n_B` → plan shapes → OPERANDS +
sig; the engine body never sees it (it "never consumes n_B", kkf
pre-divided). Two cfgs differing only in da_deg correctly SHARE an engine
and differ in operands/signature. Closure enumeration of `run` verified
complete: ta/s_*/st_* (solvers, keyed by id), gm/as_/ta (tab, keyed by id,
F5), P_geom/L/NI/Nw (keyed), mode flags (keyed), module constants
EPS/NEWTON_TOL_FACTOR (never mutated; the certdiag N_NEWTON mutation at
:1152-1157 goes through a DIFFERENT solvers cache key, hence a different
ekey) — the ONLY unkeyed closure inputs are the F1 globals.

---

## F7 — H6 unification: import-order, min_compile 0.0, unbounded dir — VERDICT: HOLDS-WITH-CAVEAT. SEVERITY: LOW-MEDIUM (ops hygiene)

**Claims attacked**: (a) every entry point that relied on the o33/o32/
loopspeed blocks still gets the cache; (b) disk growth quantified; (c) no
carrier assumes min_compile 1.0.

**Evidence**:
- (a) HOLDS: the canonical block lives at `a1_ideal_march_jax.py:156-168`
  (import side effect). All consumers import A1 (or TV→A1) before any
  compile: margin_governor:130, def_twin:103, adaptive_knot:97,
  engine_speed_bench:62, loopspeed:76, o33/o32 import TV above their
  retired blocks. The o33-comment references at margin_governor:132 /
  def_twin:107 are the `import o33_bench` lines — both AFTER A1. No
  entry point orphaned.
- (c) HOLDS: no remaining `min_compile_time`/`min_entry_size` writer or
  reader outside the canonical block (grep clean); nothing asserts 1.0.
- (b) CAVEAT: with the LRU line REMOVED (filelock catch — honestly
  declared, named conditional) the dir is unbounded, and the declared cap
  arithmetic ("~7.9 MB × ~64 signatures × ~4 campaigns ≈ 2 GiB") assumes
  entry count ∝ SIGNATURES. If F4's outer val_grad modules embed plan
  constants, every SEGMENT of every walk writes a fresh multi-MB entry with
  ~zero future hit probability → growth ∝ cumulative segments, not
  signatures, and min_compile 0.0 (was 1.0 in o33/o32) now persists every
  sub-second compile as well (entry-count churn). **Repair**: until the
  filelock decision, add the measured dir size to the mbwalk/md/me artifact
  rows (one `du` per bench) so the growth LAW (segments vs signatures) is a
  datum, not an assumption.

---

## F8 — Padding/safe-where semantics under operands — VERDICT: HOLDS

**Claim attacked**: padded rows read differently as operands than as baked
constants.

**Evidence**: `plan_operands` reproduces the old constant construction
verbatim (zeros for n=0 arc columns :585-587, fan zero-padding :571-573,
ax_fill dummy substitution :599-600, P_DUM/Z_DUM/PT_DAX/SD_DAX exact
recorded problems :596-603); `PAD` is still the build-time CERTIFIED dummy
cell solution, per make call, now shipped as an operand (:693-701) — the
eager dummy certification rejectors run on EVERY make, cache hit or not.
All mask paths (`act = ksF/ksA < n_i`, `hax` where-pairs, `isarc` select)
consumed scan operands ALREADY in the old code — no constant-folding
semantics were available to lose. Both where-branches remain finite by the
same dummy-problem construction. dtypes stable (bool/int32/float64) →
stable jit signatures.

---

## F9 — rowsF/rowsT/ksF/ksA as int32 operands; statics recovered from shapes — VERDICT: HOLDS

**Evidence**: `WF/WT/nmaxF/nmaxA` are recovered as PYTHON ints from operand
SHAPES (:723-726) — static under jit; every former static use stays static:
clip bounds `WT-1`/`nmaxA-1` (:824,830,837), `jnp.tile(..., (WF-1,1))`
(:774), `(WT-WF,1)` (:807), the `if shifted.shape[0] < WF` Python branch
(:785). The arange arrays themselves were jnp constants inside the old
trace and are now equal-valued operands — no shape polymorphism introduced.

---

## F10 — M1 record memo: purity, one-slot staleness, failure-path divergence — VERDICT: HOLDS-WITH-CAVEAT. SEVERITY: LOW

**Claims attacked**: cache-hit wrongness, stale slot, typed-raise fidelity.

**Evidence**:
- Soundness: key = (ctx, W bytes) with ctx = CONTENT hash of cfg+tab+
  closure/solver names (:930-945); `run_toc_record` is a pure function of
  exactly (W, tab, cfg, state_fn, solvers) PLUS the F1 class globals —
  fixed in-walk by scope (docstring's own argument), so key equality ⇒
  value correctness even for a STALE un-consumed slot that matches a later
  W (determinism, probe-verified once per walk at :1093-1116). Slot
  consumed-at-most-once (:1091), deep-copied at stash (:1386-1389).
- CAVEAT 1: `record_ctx_tag` does NOT include `M_NODES`/`KNOT_XI` — same
  omission as F1; harmless in-walk only because of the scope convention.
  Repair shared with F1.
- CAVEAT 2 (declared-gate friction): in the failed-record path the memo
  replays the CALLBACK message + " [replayed callback record failure, M1
  memo]" (:1087-1088) where the legacy loop-top would raise the "P4 gate:
  record at segment base not certified" text (:1125-1127) — the
  `rejected[].error` strings (persisted via A1_REJ_SAVE) and `re_records`
  differ between memo-ON and memo-OFF on failing walks. The m12gate A/B
  compares W/J/n_segments/counters (engine_speed_bench:321-348), not
  rejected[].error, so it passes — but the "bit-transparent" wording is
  falsifiable on that string. Repair: one sentence in the M1 registration
  declaring the failure-path message/counter delta, or replay the P4-form
  message instead.
- `worst_seen` reconstruction from `fail_slot["worst"]` matches legacy
  numerically (both = callback cert_worst when the record succeeded, NaN
  when it did not) — verified :1083-1084 vs :1123.

---

## F11 — M2 fun+jac memo bit-transparency — VERDICT: HOLDS

**Evidence**: one slot per segment (fresh `vg_slot`, :1255), key = physical-W
product bytes — scipy calls fun/grad at the SAME u so `u*Dv` is bitwise
identical (same Dv object per walk); hit returns the same float and a
`.copy()` of the same array (:1260-1268); g_np's `g*Dv` allocates fresh —
no aliasing. Nonfinite counting stays per-REQUEST in f_np/g_np exactly as
legacy. n_eval → n_vg_exec is the DECLARED ledger truth repair with the T2
consumer updated in main() (:1868-1651ff) and the legacy double-priced
figure printed alongside; external consumers checked: margin_governor:397
(`n_eval > 0` — still true, Hessian rows alone give ≥ n+1 executions),
engine_speed_bench m12gate (expects ON < OFF). The same one-slot pattern is
replicated verbatim in the two margin factories (margin_governor.py:219-236,
def_twin_falsifier.py:666-683).

---

## F12 — Churn print and _SCAN_SIGSEEN growth — VERDICT: HOLDS

**Evidence**: the print (:895-899) is Python-level at make time, once per
NEW (ekey, sig) — never inside a traced context; in knot-insertion loops
each cycle changes shapes so it emits exactly the intended one M-B churn
row per topology. `_SCAN_SIGSEEN` holds small tuples bounded by distinct
shapes; `_SCAN_ENGINES` pins engines+tab/solvers forever (no eviction) —
bounded in practice by distinct (mode × mesh × case) tuples; the heavy
per-shape executables inside each engine are the intended reuse store.
Declare the no-eviction property in the M4 registration block (one line).

---

## F13 — Eager `run_toc_scan` left on the OLD association — VERDICT: HOLDS-WITH-CAVEAT. SEVERITY: LOW

**Evidence**: `run_toc_scan:506,511` keeps `thB*k/n_B` / `+(L-xB)*k/Nw`.
Its only consumer is main()'s per-column fidelity row (:1675-1681) compared
against the RECORD — same association on both sides, so that row is
UNAFFECTED; but the module now carries TWO replay implementations with
ulp-different station arithmetic. Any future consumer comparing eager-scan
vs jit-scan at bitwise/EPS level inherits the asymmetry. Repair: fold kkf
into run_toc_scan (3 lines) or comment the asymmetry at :503.

---

## F14 — Edit-surface honesty: companion uncommitted files — VERDICT: HOLDS-WITH-CAVEAT. SEVERITY: LOW (process)

**Evidence**: `git status` shows 8 modified files, not 5: also
`margin_governor.py`, `def_twin_falsifier.py` (M2 memo replicas — audited,
F11) and `thermotab_c1_jax.py` (+259: the M3 floor-index/fused/derived-K
closure — a DECLARED version change with its own adoption protocol and new
R5/R6 rejectors; no in-place tab mutation added: negative controls copy via
`dict(tab_n)`). M3 changes the state-function arithmetic (K_NEWT trips vs
the retired 8-trip literal) UNDER the same working tree the m4gate will run
on — the measured Newton-floor equivalences therefore gate the COMBINED
M3+M4 numerics, not M4 alone. Fine iff declared; the M4 verdict of record
should name the tree hash so attribution is not retroactively ambiguous.

---

## F15 — Buffer donation / ops_j sharing — VERDICT: HOLDS

**Evidence**: no `donate_argnums` anywhere in validation/ (grep clean);
each make returns a lambda closing its OWN `ops_j`; cache-hit lambdas share
only the engine, not operand buffers; jax default donation off — no
invalidated-buffer hazard. The mutual-exclusion rejector for
cert_diag+val_diag (:662-664) and `mode` in the key (:885-886) close
surface (10).

---

## COUNTS

- REFUTED-THE-EDIT: 1 (F1 — engine cache CAN return a wrong engine:
  KNOT_XI/M_NODES outside key and operands, same-shape class change,
  silent, unguarded at gradient-only call sites; the m4gate as designed
  cannot catch it).
- HOLDS-WITH-CAVEAT: 8 (F2 drift covered-but-trajectory-divergence
  declared; F3 arbitration flag does not restore pre-edit numerics; F4
  walk-level recompile-deletion unproven from source, measurement-owned;
  F5 identity-keyed tab vs latent in-place mutation; F7 H6 growth law
  optimistic + unbounded pending filelock; F10 M1 failure-path
  message/counter divergence + ctx-tag global omission; F13 eager-scan
  association asymmetry; F14 combined-tree gate attribution).
- HOLDS: 6 (F6 cfg enumeration incl. da_deg; F8 padding/safe-where; F9
  int32 operand statics; F11 M2 memo; F12 churn print/growth; F15
  donation/aliasing).

**Worst finding**: F1. The one-line repair (class globals into ekey +
record_ctx_tag, or xi as an operand) should land BEFORE the m4gate verdict
of record, because the gate's own instance (single fixed class) is
structurally blind to it.
