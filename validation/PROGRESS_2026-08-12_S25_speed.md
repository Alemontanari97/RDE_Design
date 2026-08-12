# SESSION LOG — S25 "C4-FIRST + ENGINE SPEED" (2026-08-12)
# Branch rde-nozzle-program, opening HEAD 589cc56 (verified, no foreign
# commits); GENO HEAD fca273a on main (verified, independent repo,
# NEVER committed from here). One session; decisive-run wall-clock cap
# 3 h; STOP-WHEN-MET rule of the S-SPEED dispatch binding.

## STEP 1 — OPENING (R2) + THE PRE-EXECUTION GATE (logged verdict)

RESTART DECLARATION: S25 opens post-F1b (S24 CLOSED 1/1), pre-F2.
Plan placement: inter-phase service session named by the S24 closure
NEXT row — (i) C4 mechanical closure [census R3c, written S24
placement, third migration FORBIDDEN], (ii) ENGINE SPEED SESSION
[census R22, executes DISPATCH_Sspeed_to_S25_2026-08-12 order
M0->M1->M2->M4->M3->M5->M6 + H3/H4], (iii) G0/T2 review consumed
[census R7c, queued since S18], (iv) CHOICE LEDGER absorption [census
R25], then NEXT = F2 GENERAL ENGINE opening.

MANDATORY READINGS PERFORMED (opening): memories s24-f1b-def-twin,
choice-adjudication-convergence, never-postpone-resolvables,
agentic-orchestration-forms (rule 7 + workflow-stall lesson),
s18-brick2-closed, generality-nonhardcoded-procedures,
scope-pins-frozen-thermally-perfect; M0 Part VI [S24 REGISTRATION
BLOCK]; PROGRESS ORA + census R1-R27; D6 F1b STATUS OF RECORD;
DISPATCH_Sspeed_to_S25 (full) + ADVISORY_engine_speed_audit (full,
constraints (1)-(7) read verbatim from ADVISORY_Sspeed_prompt:66-79);
panel S24 residual conditions C-A..C-D + C7/O5 (from M0 S24 block).

R26 GAP-MAP STATE DECLARATION (landing rule executed — transcript
read, NOT relaunched blind): workflow wf_ab766057-afd transcript dir
found (S24 session dir, 16 agents, journal.jsonl present). STATE:
INTERRUPTED MID-VERIFY at S24 close (~10:00) — 6/6 finder files
COMPLETE on the S24 scratchpad (cell-cert, mesh-amr, constraints,
driver-nonsmooth [round-2], parametrization, thermo-bands); verifier
stage 4/6 COMPLETE (thermo-bands, parametrization, cell-cert
journaled + constraints written-on-disk at 10:00:26 but unjournaled);
2/6 verifiers (mesh-amr, driver-nonsmooth) NEVER produced output;
NO synthesis stage ran -> ADVISORY_S24_sota_gapmap_2026-08-12.md and
the CHOICE LEDGER annex were NEVER produced. The census token
"resume w3a9j6ie4" resolves to NO transcript dir on this machine
(declared: dead token; the transcript dir above is the state of
record). ACTION TAKEN: (a) all 12 raw artifacts copied from the
VOLATILE S24 scratchpad to validation/sota_gapmap_raws_2026-08-12/
(untracked ADR pattern — artifacts-to-files rule); (b) the two
missing verifications relaunched as 2 background agents
(hand-authored continuation per the resume-not-relaunch fallback:
cross-session resumeFromRunId is unavailable, journal consumed
instead); synthesis + annex will be authored at T4 from the 6+6
on-file raws WITH the binding dedup rule vs the S-SPEED
dispatch/advisory (one row per item, double evidence = stronger).

PRE-EXECUTION GATE VERDICT (standing directive gate-pre-esecuzione):
- Plan adherence: every duty this session maps to a census row (R3c,
  R22, R7c, R25, R26) or a dispatch item — no orphan step (R1). PASS.
- Upstream rigor: ALL S-SPEED bench absolutes are DECLARED CONTENDED
  (measured under the running S24 campaign) -> M0 clean-host
  re-baseline is a HARD precondition to every acceptance verdict of
  T2; ratios quotable, absolutes indicative until M0. PASS with this
  binding order.
- R5 pre-declarations binding this session: no number without a
  committed carrier + test; every adopted DECLARED version change
  (M3, M6) gated on KAT + O3.1 re-pass and logged per R3/R4; derived
  tolerances only; constraints (1)-(7) verbatim binding; suite/lint
  verdicts gated on EXIT CODE, redirect-only, NEVER pipes; each
  M-item stops at its cost cap and routes to its NAMED fallback
  (M4 overrun -> M4 IS the cut; M5c gate reject -> H2 -> N1).
- Terms: S14-S24 verdicts NOT re-litigated (thermo survey KEEP
  quintica — M3 FUSES it, never replaces; panel C1-C10 stand);
  GENO/ never committed from here; sspeed/ = parallel-session
  perimeter, consultable, not a deliverable; env pins numpy 2.5.1 /
  jax 0.11 / scipy 1.18 (O5 = numpy 2.5.2 [RIGOR] at session
  boundary only).
GATE: PASS — execution order T1 (C4) -> T2 (M0..) as dispatched.

## STEP 2 — T1: C4 MECHANICAL CLOSURE (pre-declaration)

Written S24 placement (S24 log:41-43, 66-68): "env-conditional tier +
typed ondemand field + staleness link in run_all.py"; audit row
test-suite:ondemand-carrier-exclusion (CONFIRMED high) is the
finding of record; the honest annotation in run_all.py falls ONLY at
complete closure.

DESIGN OF RECORD (general, registry-driven, no hardcoded lists —
generality directive):
1. Registry: new TYPED field `ondemand` REQUIRED on kind: carrier
   entries (FORBIDDEN elsewhere): `no` for in-suite carriers, else a
   strict-syntax spec "env=<jax|gfortran|jax+geno>;
   pass=YYYY-MM-DD; suite=<none|argv...>" (pass = the dated
   PASS-of-record of the LAST full manual run recorded in
   scope/session logs; suite = an affordable self-check invocation
   or `none` for decisive-run-scale carriers).
2. Lint (test_claims_lint.py): the substring bypass (`ONDEMAND in
   scope`) is DELETED; suite-membership exemption keys ONLY on the
   typed field; spec parsed with a strict regex (violation on any
   malformed spec / unknown env token / missing field); STALENESS
   LINK: for every ondemand carrier, last git commit date touching
   the carrier file must be <= pass date, else VIOLATION (fires
   loud); git-absent host -> declared SKIP note (env-conditional by
   nature). Seeded rejector demo EXTENDED with a 4th seed (stale
   pass date in-memory) that MUST be rejected every run.
3. run_all.py: new ONDEMAND tier (full runs, skipped by --fast),
   registry-driven: per ondemand carrier, env availability check
   (jax importable / gfortran on PATH / + GENO tree for jax+geno);
   carriers with suite != none AND env available run as subprocess
   gated on exit 0; others print an accounted row (env-missing or
   manual-only) with pass date. Tier verdict PASS iff no stale
   carrier and every executed subprocess exits 0.
4. The run_all.py honest annotation is REPLACED by the new honest
   scope statement (closure complete in this session).
5. Verification: full suite green on EXIT CODE (redirect, no pipe).
Suite argv wiring: only carriers with a MEASURED-affordable
self-check get suite != none at landing (candidates X-VMON, X-CDKAT
— wired only if measured in-session; else none). Everything else
stays manual-only + staleness-linked (honest; graduating a carrier
later is a one-field edit).

T1 EXECUTED (this step):
- Registry migrated (scripted): typed `ondemand` on all 46 carrier
  entries — 29 in-suite "no", 17 on-demand specs env=jax(12) /
  gfortran(1) / jax+geno(4); pass dates initialized = last git
  commit date per carrier file (R5 commit-discipline rationale in
  the header; day-granular, declared); header SCHEMA block extended.
- Lint: substring bypass DELETED; typed-spec parse (strict regex,
  unknown env token = violation); STALENESS LINK enforced via
  memoized git last-commit dates (uncommitted carrier file =
  violation outright; git-absent host = declared skip); seeded
  rejector demo #4 (stale pass date) added — REJECTED every run.
  Standalone lint EXIT 0 (three runs during the work; the staleness
  rejector also fired FOR REAL on the uncommitted X-SPDB entry —
  parked to re-enter with the M0 commit; violation text of record
  in this log).
- run_all.py: ONDEMAND tier added (registry-driven, full runs only)
  = tests/test_ondemand_carriers.py — staleness re-check + env
  detection (jax importable / gfortran on PATH / jax+geno = jax +
  GENO/ + wsl) + subprocess execution gated on exit 0 for suite !=
  none carriers; the S21 carrier-exclusive annotation REPLACED by
  the closure-complete honest-scope block (the C4 annotation falls
  WITH this closure, as written).
- MEASURED wiring decisions: X-VMON default run 8.7 s EXIT 0 ->
  suite=default, pass re-dated 2026-08-12 (fresh PASS this session);
  X-CDKAT measured 352.0 s EXIT 0 (fresh PASS this session, VERDICT
  PASS retro-validation line intact) -> suite=none (decisive-ish
  scale; the measured number is the declared reason; graduating it
  later = one field edit).
- VERIFICATION: FULL suite (fast+rigor+slow+ondemand) EXIT 0 —
  19/19 groups PASS in 2002 s; ONDEMAND tier row: 1 executed
  (X-VMON PASS), 16 accounted, 0 env-skipped, 0 STALE. Declared
  transient: the registry was edited mid-suite (X-SPDB added then
  parked when its own staleness rejector fired on the uncommitted
  file — "X-SPDB: ondemand carrier file validation/
  engine_speed_bench.py has no committed history"); group (xv) ran
  pre-edit and the final tree was re-linted standalone EXIT 0 +
  seen by the closing ONDEMAND tier — both endpoints green.
C4 CLOSURE = COMPLETE (census R3c consumed; third migration never
happened). COMMITTED 32459ca (path-limited: registry, lint, run_all,
new tier module; hunk audit clean — 46 ondemand lines + header, no
foreign content).

## STEP 3 — T2 ENGINE SPEED: M0 attempts + M1/M2/M4 implementation

GAP-MAP LANDING (mid-step, user-visible): the S24 gap-map advisory
ADVISORY_S24_sota_gapmap_2026-08-12.md LANDED complete (1037 lines:
47 findings -> 26 CONFIRMED/18 DOWNGRADED/3 REFUTED -> 36 deduped
entries, 5 HIGH; §3 coverage ledger AC1-AC16; §4 quarantine Q1-Q10;
§5 S25 probe registry 26 rows; §6 CHOICE LEDGER ANNEX C1-C45 = 8
CONVERGED / 14 single-author / 23 NEVER, every open row with owner).
Synthesized on the COMPLETE 6+6 verified set (incl. the two
verifications this session re-ran: mesh-amr 1C/5D/2R no-HIGH — F6
axis-verification gap = the one genuinely new row; driver-nonsmooth
6C/2D — G1/G2 HIGH sharpen census R10/R25, G5a crash claim REFUTED
at source [scipy catches callback StopIteration -> status 3],
surviving = silent P2 event-log undercount LOW). READ IN FULL this
session. Label "judge-adjudicated in one round" => Form-3 red-team
on the judge layer REQUIRED BEFORE absorption (T4 duty).

M0 RUN HISTORY (honest, all declared): attempt 1 (buffered) and
attempt 2 (unbuffered) OVERLAPPED for ~10 min (attempt 1 presumed
dead on a 0-byte probe + a broken pycount instrument — actually
alive) => BOTH CONTENDED, both artifacts DISCARDED for baseline use;
their indicative rows (attempt 2: record median 145.4 s, C1 replay
steady 6.97 s, val_grad steady 9.93 s at the defnoz class) are
quotable only as contended context. pycount instrument BUG found and
FIXED: interpreter image on this host is python3.13.exe, so the
tasklist IMAGENAME python.exe filter silently returned none — plain
tasklist substring count now (includes self: 1 = clean). Attempt 3
= THE baseline of record: clean host verified (0 foreign python),
legacy-engine pin A1_PLAN_ARGS=0 (pre-M4 anchor), running at this
step's close.

IMPLEMENTED (code, gates pending — commit AFTER gate evidence):
- M1 (driver a1_toc_variational_jax.run_trsqp): segment-boundary
  record memo (one-slot, deep-copied, consumed-once; key = (ctx tag,
  W bytes), ctx = record_ctx_tag = sorted-JSON cfg + thermo-table
  content hash + closure/solver identity per gauntlet V8) + FAILED-
  record memo (typed-raise replay); first-hit controls (fresh-record
  bitwise equality + perturbed-W key miss) raise AssertionError so
  they can NEVER be absorbed as a rejected design; counters
  record_fresh/cached/failmemo in the result dict; legacy path
  A1_RECORD_MEMO=0.
- M2 (driver + margin_governor factory + def_twin factory): one-slot
  fun+jac / m+gm memos keyed on physical-W bytes shared by EVERY
  val_grad consumer (precond, g_base, Hessian rows, f_np/g_np;
  m_np/gm_np at both margin sites with m_exec/m_dedup counters);
  n_eval TRUTH REPAIR [RIGOR]: result n_eval now = ACTUAL compiled
  value_and_grad executions (was: f_np calls + a double-counting
  n+1 line — the S18 "67 evals" ledger untruth of record, advisory
  §1.3/§7.1); n_eval_dedup_hits carries the dedup; legacy path
  A1_VG_MEMO=0.
- M4 (driver): plan_operands() extracts the plan as an OPERAND
  pytree (padding discipline UNCHANGED: single-bucket-per-phase,
  per-phase maxima — V1 no quantization grid; V2 signature =
  GENERATED, jax abstract shapes ARE it, churn rows printed);
  module-level engine cache keyed (tab/state_fn/solvers identity +
  diag mode + march-net statics + geometry floats) with strong refs;
  legacy constants-baked build of the SAME body via A1_PLAN_ARGS=0
  (arbitration); n_B eliminated from the trace via the kkf
  pre-divided station fraction (operand).
- H6 (folded in M4): THE canonical persistent-XLA-cache block moved
  to a1_ideal_march_jax (root import => standalone-launch class now
  covered, the measured 8.1x cross-process win); o33/o32 blocks
  RETIRED-deferring, loopspeed's disjoint rde_jax_cache env default
  RETIRED; min_entry -1, min_compile 0.0; LRU cap = built-in
  jax_compilation_cache_max_size (V3/S3, never hand-rolled) at
  2 GiB PRACTICE with adoption arithmetic (live dir 1.45 GiB/188
  entries -> median ~7.9 MB x ~64 signatures x ~4 campaigns).
- [X-SPDB] bench carrier validation/engine_speed_bench.py: modes m0
  (clean-host baseline, legacy pin), m12gate (M1/M2 acceptance A/B
  at declared reduced march net NI=11/Nw=30/da=1.0, LEGACY pin both
  arms for attribution purity), m4gate (Newton-floor equivalence +
  bitwise report + O3.1 through the args engine + warm-path
  args-vs-constants band derived K_RICH x measured spread + re-bind
  warmth + V2 property rejector), mbwalk (args-ON walk: churn
  Q3 datum + M4 walk attribution), ma..me (MEASURE snapshots).
  Registry entry X-SPDB drafted, PARKED until the file is committed
  (its own staleness rejector fired on the uncommitted file —
  correct behavior, of record).
GATE SEQUENCE NEXT: m0 (running) -> m12gate -> m4gate -> mbwalk ->
commit M0-M4 package (with pass re-dates carrying the gate evidence)
-> M3.

## STEP 4 — M0 OF RECORD + M1/M2 ACCEPTED + M3/M5ab landed

M0 RUN 3 DISCARDED TOO (honest): the H6 canonical block's LRU cap
(jax_compilation_cache_max_size) turned out to hard-require the
`filelock` package AT CACHE-READ time — with the cap set and
filelock absent, jax refuses EVERY persistent-cache entry read
(UserWarning per entry), i.e. the cap silently DISABLED the cache.
ADOPTION CATCH OF RECORD (the S-SPEED S3 row "verified settable"
covered config existence only): the cap is now a NAMED CONDITIONAL
pending the filelock env decision at a session boundary (env-pin
discipline — no mid-session dependency install, no workaround);
canonical block keeps dir+min_entry+min_compile, unbounded exactly
as since S18. Run 3 killed, declared.

**M0 BASELINE OF RECORD (run 4, clean: pycount = 1, legacy-engine
pin, artifact validation/s25_spdb_m0.json)**: RECORD fresh adaptive
march median 100.84 s [93.7, 100.8, 123.8] (the "111 s" class,
contention-free); C1 whole-loop replay compile+first 16.28 s /
steady 2.047 s (the advisory's DERIVED "~13 s defnoz C1 replay"
was a 6.5x overestimate — measured datum of record); val_grad
compile 32.66 s / steady 6.420 s; Hessian block (n+1 = 10) estimate
64.2 s; segment synthesis (advisory row shapes) 289.8 s. All
acceptance verdicts from here quote THIS baseline.

**M1+M2 ACCEPTED — [X-SPDB] m12gate EXIT 0 (artifact
s25_spdb_m12.json; declared reduced gate net NI=11/Nw=30/da=1.0;
recorded-Wp start NOT certified at this net -> DECLARED fallback to
the class representative)**: A/B bit-identity PASS (final W
bitwise, J = 4.0698369265e+07 identical, 3 segments identical,
per-segment J/KKT rows identical); record counters OFF (6,0,0) ->
ON (4 fresh, 1 cached, 1 failmemo) RECONCILED (6 == 6) — BOTH memo
classes exercised naturally (the seg-2 P3(ii) failure was REPLAYED
by the failmemo: "[replayed callback record failure, M1 memo]" in
the P4 revert row); honest n_eval 47 -> 43 (4 dedup hits);
first-hit controls fired (fresh-record bitwise equality PASS +
perturbed-W miss PASS); walltime 159.4 -> 82.8 s (~1.9x on the
short walk, probe record included). MEASURE M-A = this artifact +
the M0 rows.

IMPLEMENTED while gates ran: **M3** (thermotab_c1_jax: O(1)
floor-index locate LICENSED by a build-time grid-uniformity
rejector [loud refusal names the node]; fused (h, cp) evaluator —
expressions VERBATIM; per-table DERIVED Newton count K_NEWT [seed
bound + contraction + the table's own roundoff floor + 1 margin
trip; N_NEWT_INV=8 literal RETIRED to negative-control reference];
fused post-loop cp in state_q_c1; C-A NASA-DIRECT EXACTNESS ORACLE
in the carrier [h/cp at roundoff — h is EXACTLY quintic, a6 is
constant; s0 within its derived ln-remainder band]; node-tie
index-identity control [off-node exact + node/±ulp value-band];
NEW negative controls R5 [non-uniform grid REFUSED] + R6
[corrupted-D index control fires]) — DECLARED VERSION CHANGE,
session-boundary adoption, [X-THC1] C1-C7+R1-R6 re-run queued in
the gate chain. **M5a** (make_implicit_solver gains the FUSED
solve_cert 4th entry — one dispatch per record cell; index-based
consumers untouched) + **M5b/H1** (typed A1.UncertifiedCellError
early-abort, opt-in kwarg abort_uncert — armed at the driver's TWO
gate sites [loop-top P4 + callback P3(ii), where cert_worst > 1
raises ANYWAY: same condition, fired earlier]; verdict/reporting
sites keep full marches; schema addition aborted_at_cell in the out
dict + carried in the typed error; cert-before-margin ordering
preserved; legacy 2-dispatch path behind A1_FUSED_CERT=0). HONEST
SEQUENCE INCIDENT: the first m4gate launch crashed on the
HALF-LANDED M5a (4-tuple vs 3-unpack) — my sequencing error
(launched a gate while an edit was in flight), caught by the
gate's own crash, fixed, relaunched; no measurement consumed.
GATE CHAIN RUNNING: m4gate -> m5gate (fused-vs-legacy bitwise A/B +
doctored-cell first-offender control) -> mbwalk (Q3 churn) ->
[X-THC1] re-run (M3 adoption gate) -> bench mc (MEASURE M-C).

## STEP 5 — M4 + M5a/b ACCEPTED; refuter round 1 absorbed

**M4 ACCEPTED — m4gate EXIT 0 (s25_spdb_m4.json)**: args-vs-
constants wall BITWISE IDENTICAL (max|d| = 0.0 — stronger than the
required Newton-floor equivalence); args replay fidelity vs record
3.14e-11 <= 6.53e-10; O3.1 leak detector THROUGH the args engine
7.30e-04 <= 1.29e-01; warm-path band PASS (args 0.3816 s vs legacy
0.3906 s — args marginally faster; K_RICH x measured spread);
re-bind cost 0.0064 s + first re-bound call WARM 0.44 s (the
~37-90 s/segment recompile DELETED); V2 property rejector PASS
(arc-count change -> new signature). Engine signature of record at
defnoz full net: (fan 20, nmaxF 39, WF 41, arc 153, nmaxA 85,
WT 89, n_B 93).

**M5a+M5b ACCEPTED — m5gate EXIT 0 (s25_spdb_m5.json)**: fused-vs-
legacy record A/B — wall BITWISE identical, cert_worst identical
(4.040530e-01), plan dec-vectors identical; record walltime 30.49
-> 25.49 s (1.20x, the fused-dispatch share); M5b doctored-cell
control: typed refusal fired AT the doctored interior call
(interior dispatches == K+1 = 8, first-offender stability), carried
cert_worst = the doctored ratio 3.63e+19.

**M3 IS ALREADY BITING (measured, gate pending)**: the m5gate
legacy-path record at the FULL defnoz net = 30.49 s vs the M0
baseline 100.84 s — the derived K_NEWT (8 -> derived trips) + fused
(h, cp) inside every solver Newton body cut the per-cell closure
cost ~3.3x BEFORE M5a's own 1.20x; cert_worst moved 4.750e-01 ->
4.041e-01 = exactly the DECLARED M3 version change (adoption gated
on the [X-THC1] re-run in the chain + fresh records everywhere
after this session's boundary).

**REFUTER ROUND 1 (M1/M2) ABSORBED — s25_refute_m12.md (12
findings: 1 REFUTED-THE-EDIT, 8 HOLDS-WITH-CAVEAT, 3 HOLDS; sterile
attacks documented)**: F1 (MEDIUM, REFUTED) the counter
reconciliation identity was TRAJECTORY-CONDITIONAL — march-type
record failures (internal raises: axial-margin, wall-search
no-land) were counted in neither arm (increment post-call) so a
failmemo replay would read ON = OFF+1 = FALSE FAIL of the gate
(safe direction, but the invariant as stated was wrong) -> REPAIRED
(fresh = REQUEST count, pre-call, both sites); F2 the memo key was
BLIND to the design-class/solver module knobs (M_NODES/KNOT_XI/
N_NEWTON — transparent today only by caller discipline, the S24+1
joint-refinement leg is the named future mutator) -> REPAIRED
(_mkey reads the knobs AT REQUEST TIME; contiguity forced); F4
probe tax DECLARED in the docstring (one record/walk, A1_MEMO_PROBE
opt-out for BY-RULE-capped campaigns); F6 (M2 perturbed-u negative
control shares the record-memo mechanism — declared covered by
construction, control rides the record-memo probe) and F7 (kickoff
T2 normative text repricing) -> carried to the T3 review edit.
Remaining caveats = documentation-grade, absorbed in the docstring.

## STEP 6 — refuter round 2 (M4) absorbed; frozen-code re-chain; T3

**REFUTER ROUND 2 (M4) ABSORBED — s25_refute_m4.md (15 findings: 1
REFUTED HIGH, 8 HOLDS-WITH-CAVEAT, 6 HOLDS)**: F1 (HIGH, REFUTED)
the engine-cache key omitted the DESIGN-CLASS module globals
(M_NODES/KNOT_XI read at trace time inside wall_geometry) — a
same-length knot change (the S24+1 joint-refinement leg = the named
mutator) would have silently reused a stale-class engine, invisible
to churn rows and to the single-class m4gate -> REPAIRED (class in
ekey + in record_ctx_tag + a CLASS-KEY REJECTOR row added to
m4gate: same-length knot change MUST mint a new engine entry —
verified PASS 1 -> 2 on the frozen-code re-run). F2/F3 (kkf
last-ulp association drift): REPLAY-side only, the record/decision
path is untouched; covered by the live fidelity band with 2-3
orders of margin; near-tie trust-constr trajectory divergence vs
the pre-edit baseline = declared consequence of the DECLARED
version change (bitwise never promised). F4 (walk-level recompile
claim): "deleted" holds for the ENGINE; under val_grad (jit-of-jit
rebuilt per segment) full absorption depends on XLA constant
hoisting + the persistent cache — mbwalk/M-D adjudicate the
measured share (over-claim retracted to the measured row). F7 (H6):
import order verified on every entry point (A1 first); cache dir
UNBOUNDED pending the filelock conditional — growth arithmetic
re-derived at adoption. F10: the failmemo-replayed message text
differs from the legacy P4 text in rejected artifacts — DECLARED
schema note (it says what happened), not masked. F14: the edit
surface is 8 files (incl. the M2 margin-site replicas, verified
bit-transparent, and M3) — the acceptance verdicts name the
combined tree state (this commit's hash at landing).

**FROZEN-CODE RE-CHAIN (sequence discipline after TWO self-inflicted
mid-edit collisions — the m4gate 4-tuple crash and the mbwalk
inconsistent-module (6,0,0) counters, both declared)**: ALL gates
re-run on the frozen tree: m4gate PASS (incl. the new class-key
rejector), m5gate PASS, m12gate re-run (repaired request-semantics
counters), mbwalk (Q3 churn of record: first run measured 2
signatures / 3 segments — n_B moves with thB, churn REAL; the
engine cache + persistent cache are the absorption mechanism, M-D
adjudicates), [X-THC1] (M3 adoption gate; its FIRST run REJECTED my
undersized R6 control — corrupted-D 1e-6 below the 2.6e-5 detection
floor, the exact S24 R-GRAD error class, RESIZED derived from the
probe geometry: epsD = 2 x boundary-distance / (n-1)), bench mc
(MEASURE M-C).

**T3 G0/T2 REVIEW CONSUMED (census R7c)**: verdict of record
written to rde_nozzle_G0_decision.md §4 [S25 dated note]: the S18
T2 firing = STRUCTURAL (records+curvature), T1/T2a PASS => NO
language flip, G0 stands (Julia/Enzyme stays warm + unbenchmarked,
declared); ledger truth absorbed (~102-108 true evals, not 67; T2
lhs repriced to n_eval_actual x t_value_and_grad — [X-TOCV] line
edited, kickoff §3 normative addendum, D6 F2 row annotated
review-CONSUMED); the structural terms REPAIRED by the M-chain
(record 100.84 -> 25.49 s of record; M1/M2/M4 gated bit-level).

T4 CHOICE-LEDGER ABSORPTION (prepared; final after the red-team
report): annex C1-C45 -> census R25 becomes the LEDGER-CARRIED row
(the annex IS the ledger of record, 8 CONVERGED / 14 single-author
/ 23 NEVER each with owner; S25 delta rows: C4-suite closure landed
[this session], C23 = H1/M5b landed, C24 KEEP + C-A discharged
[this session], C17/C18 sweep = GAP-29 S25-bis; C34 [P-TRFLOOR]
blocked-with-named-cause on forfeited inputs, trigger = first
post-8761dce campaign artifact). NEW census row: the numeric-lint
SCOPE HOLE (audit test-suite:numeric-lint-scope-hole, CONFIRMED
medium, P2-scheduled, never placed): validation/ is NOT scanned by
the no-magic lint — the machine channel that would have rejected
the retired literals; owner = S25-bis/F2-entry hygiene window.

## STEP 7 — PACKAGE COMMITTED + T4/T5 CLOSURE

**COMMIT 07400a4** (19 files, 1694+/157-): the full M-chain + T3
annotations + [X-SPDB] registry entry + 8 carrier pass re-dates +
6 measured artifacts. Post-commit lint EXIT 0 (136 entries; the
pre-commit X-SPDB "no committed history" violation resolved by the
commit itself, as designed). Hunk audit clean (data/q_mapping.*
pre-existing changes NOT touched, not ours).

**MEASURE M-C / STOP-CHECK VERDICT OF RECORD** (s25_spdb_mc.json,
pycount = 1): record 32.09 s [28.9-34.4], replay steady 0.661 s,
val_grad steady 0.979 s, Hessian block 9.8 s, segment synthesis
77.9 s. Honest segment arithmetic with M1-M5ab landed: base record
0 (M1) + callback record 32.1 (M5c pending) + Hessian 9.8 + walk
evals ~3.3 + monitor 0.7 + rebuild ~0 => **~46 s central: segment
<= 30 s NOT-MET without M5c — the advisory counterfactual
("callback record alone > 30 s without an L5-class lever") HELD**.
Campaign shape (21-seg rung): ~16.1 min segments + boundary
~2-5 min (H3 pending, post-M3-priced) + tail ~3.5-7 min (H4
pending) + compile set ~2-3 min => **~18-23 min: campaign <= 25 min
MET at the central estimate, thin at the pessimistic top** — the
formal M-D/M-E STOP CHECKS (pessimistic-end standard) belong to
S25-bis where M5c/M6 land. STOP-WHEN-MET: NOT met on segment =>
speed items remain scheduled (never dropped): M5c + M6 = S25-bis
(census R30); H3 + H4 BINDING before any next decisive campaign.

T5 CLOSURE EXECUTED: PROGRESS ORA rewritten (S25 block + honest
counter); census DELTA S25 (R3c/R7c/R22/R23/R25/R26 consumed or
delta'd; NEW R28 numeric-lint hole, R29 pipeline-sense directive,
R30 S25-bis; BLOCCATO 8 = filelock conditional); memory
s25-engine-speed written + pipeline-sense-expert-review directive
memory; closing FULL suite launched (EXIT-code gated; (xv) PASS
136 entries confirmed mid-run; final tally appended below when the
run returns). IN-FLIGHT AT CLOSURE (landing rules declared):
(i) red-team gap-map judge-layer FINAL report (2 driver-facet
absorption failures already confirmed; artifact
s25_redteam_gapmap_judge.md) — landing rule: absorb at S25-bis/next
open BEFORE consuming any gap-map row it touches (GAP-18/N6, AC10);
(ii) the two pipeline-sense expert advisories
(ADVISORY_S25_pipeline_sense_math / _impl_fidelity) — landing rule:
READ BEFORE touching the algorithm next session (R29). Nothing
dropped silently.

CLOSING FULL SUITE OF RECORD: **19/19 PASS in 347 s, SUITE_EXIT=0**
(redirect-only). Unplanned measured datum: the SAME full suite ran
2002 s at the T1 closure (pre-M3) — the adopted fused/derived-K C1
closure accelerates the in-suite carriers too (CJ 257.2 -> 83.9 s,
X-IVXC 577.1 -> 80.4 s, live examples 672.4 -> 107.6 s, dual-route
293.5 -> 34.6 s; suite-level 5.8x). ONDEMAND tier: 1 executed
(X-VMON PASS), 17 accounted, 0 stale (18 rows incl. X-SPDB).
