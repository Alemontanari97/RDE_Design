# S25-bis DEDICATED ADVERSARIAL REFUTATION — engine-speed diff (M5c / H3 / H4 / M6 + instruments)

- **Scope**: commits `1806ae2` (four levers: M5c per-column executor, H3 rung-boundary
  dedup, H4 tail-to-derive + code identity, M6 batched value_and_grad) and `18b4e0f`
  (findings registry + lint, numeric-lint ratchet tier), audited default-REFUTE against
  the diffs `ad5c48e..1806ae2`, the session log
  `validation/PROGRESS_2026-08-12_S25bis_speed.md`, the probe logs
  `validation/s25bis_m6locus.log` / `validation/s25bis_m6fix.log`, and the CURRENT tree.
- **HEAD audited**: `ea8143c` (verified: the six RECORD_PATH_MODULES are byte-identical
  between `1806ae2` and HEAD, worktree clean on all six).
- **Dedup authority consulted**: `docs/findings_registry.yaml` (17 entries read in full).
  Registered rows are CITED, never re-minted: `record-path:cert-verdict-recorder-dependence`
  (yaml:131-139), `engine:vmap-hessian-adjoint-divergence` (yaml:140-148),
  `engine:cross-lowering-gradient-floor` (yaml:149-157), `engine-core:F5-underived-factors`
  (yaml:35-43, spans K_RICH at a1_ideal_march_jax.py:195-205),
  `test-suite:numeric-lint-scope-hole` (yaml:86-94), `bench:speed-measurement-variance`
  (yaml:158-166).
- Probe-number re-verification performed: locus rows (2.179e-2 / 8.226e-2 / 6.047e-2 /
  2.855e-2, s25bis_m6locus.log:5-8) and corrected-form rows (dH 2.063e6, H 4.175e7,
  rel 4.94e-2, asym 1.229e6, 1.68x, bound 4x1.229e6 = 4.916e6, permutation BITWISE,
  s25bis_m6fix.log:5-7) all match the log/registry claims — arithmetic exact.

---

## RF-1 — H4 derive artifact of record is STALE at its own commit; campaign carrier blocked at HEAD
**Severity: HIGH — Verdict: REFUTES-THE-EDIT** (the delivery claim; the refusal mechanism itself works as designed)

**Attack**: recompute `code_identity()` (sha256 chain over the 6 modules of
`def_twin_falsifier.py:144-148`, per `def_twin_falsifier.py:150-155`) at HEAD and compare
with the committed artifact.

**Evidence**: HEAD identity = `ea5cd2ffe5e9…`; committed tail carries
`fcd5e61ae111…` (`validation/s24_deftw_derive.json:76`). The six modules are
byte-identical between `1806ae2` and HEAD (0 diff lines each) and the worktree is clean —
so the artifact was committed ALREADY STALE inside `1806ae2` itself. Mechanism visible in
the session log: stage_derive last ran in chain 1 (PROGRESS…S25bis_speed.md:212-217,
"derive PASS"), then the M6 default flip + sequential guards edited
`a1_toc_variational_jax.py` (a record-path module; lines 1608-1625, 1687-1700, 1742-1751)
and the FINAL re-chain re-ran only "m12gate + h3gate" (log:339-345) — derive never
re-stamped. Consequence at HEAD: `stage_campaign` hits `check_tail_code` at open
(`def_twin_falsifier.py:1042-1044`, raise at :162-168) and REFUSES — the pre-registered
F3/F7 references (:1330-1332, :1409-1410) are unusable; the [X-DEFTW] campaign stage
cannot run until derive re-runs. The commit-message claim "derive re-run EXIT 0
REPRODUCES the S24 tail numbers exactly" and the STEP-15 Class-A row "H4 (reproduces the
S24 tail numbers exactly + seeded stale-code refusal)" (log:423-425) describe a state the
committed tree does not have. Neither the closing suite (20/20) nor the ONDEMAND
staleness tier caught it: the C4 git-backed staleness link cannot see intra-commit
ordering (artifact regenerated mid-session, code edited after, same commit).

**Repair**: re-run `stage_derive` on HEAD and commit the re-stamped artifact (the tail
numbers should reproduce byte-identically — the post-derive edits are default-env reads,
comments and opt-in guard code); AND add the missing cheap rejector: a suite/ONDEMAND row
asserting `tail["code_id"] == code_identity()` on the committed tree, so a stale artifact
can never be committed silently again (same channel class as the C4 staleness link).

## RF-2 — H3 preplan contract "all carried by the memo key" is overstated; the key does not carry solver content or the active recorder
**Severity: MEDIUM — Verdict: HOLDS-WITH-CAVEAT**

**Attack**: pass a preplan recorded under DIFFERENT solvers (or under the other recorder)
with same-looking cfg — does the key refuse?

**Evidence**: the docstring claims the argument-identical contract ("same
tab/cfg/state_fn/solvers/class knobs, all carried by the memo key",
a1_toc_variational_jax.py:1308-1311). But `record_ctx_tag` hashes solvers as
`type(solvers).__name__` only (:1208) — `"dict"` for every solver set, so solver CONTENT
(closure tag, factory) is NOT keyed; and neither `_mkey` (:1370-1379) nor the ctx carries
the active recorder flag `A1_COLEXEC`, despite the registered recorder-dependence
(registry `record-path:cert-verdict-recorder-dependence`, yaml:131-139: records can
differ between recorders at marginal designs; "never mix" is declared discipline, not
key-enforced). The preplan is keyed by the CALLEE's own context (:1394-1399), so a
wrong-provenance preplan key-matches trivially. What actually gates it is the M1
first-hit probe (:1443-1472): default-armed but env-disablable (`A1_MEMO_PROBE=0`,
:1384-1385), and its compare set is wall-bitwise + cert_worst + (N,Nv) only — seeds,
min_margin, cert_n, cols are not compared. Pre-H3 this hole was unreachable ("fixed by
scope" inside one walk, record_ctx_tag's own docstring :1196-1200); H3 is exactly the
edit that makes records CROSS the walk boundary. In-tree call sites pass the same
`solv` object and the same ambient recorder, so no live corruption today.

**Repair**: extend the key (solver closure tag content or `id(solvers)` for the
same-process contract; + the colexec flag), or narrow the docstring to state the real
contract ("gated by the first-hit probe when armed; caller must pass the same objects");
consider probing min_margin/cert_n too.

## RF-3 — M6 batched path (opt-in) is WEAKER than the new guarded sequential path on persistent nonfinite lanes
**Severity: MEDIUM — Verdict: HOLDS-WITH-CAVEAT** (opt-in only today; adoption-blocking input for F2)

**Attack**: make both the batched lane and its sequential fallback nonfinite; trace the
propagation.

**Evidence**: `vg_batch_rows` never re-checks the fallback result
(a1_toc_variational_jax.py:1228-1234): if `val_grad` is also nonfinite the NaN is kept,
counted once. Downstream, the BATCHED precond branch has NO `bad_j` floor (:1673-1683)
while the sequential branch floors and counts (:1697-1700); the BATCHED Hessian branch
(:1728-1738) lacks the per-component `g_base` substitution the sequential branch has
(:1742-1751). Under `A1_VMAP_HESS=1` a persistently bad lane therefore poisons
`Dv`/`Hw` silently — the exact silent-masking REQ-NONSTALL forbids. The docstring "never
weaker than the sequential block it replaces — which had NO nonfinite guard" (:1219-1221)
is literally true vs the OLD block but false vs the SHIPPED default sequential. Secondary
unenforced contract: `vg_batch=True` "REQUIRES the args engine" (:886) yet under
`A1_PLAN_ARGS=0` the code silently builds the constants-baked batched entry
(:1131-1134) — the churn class M4 deleted, no raise.

**Repair**: after the fallback loop, apply the same floor/substitution semantics on the
batched results (or raise on double-nonfinite); add `if vg_batch and A1_PLAN_ARGS==0:
raise`. Both must land before any F2 adoption (registry row
`engine:vmap-hessian-adjoint-divergence` owner clause).

## RF-4 — h3gate covers only the driver preplan arm; the campaign carry sites are ungated
**Severity: LOW — Verdict: HOLDS-WITH-CAVEAT**

**Attack**: find an executable A/B that exercises the def_twin/margin_governor reuse
sites bitwise. There is none.

**Evidence**: h3gate (engine_speed_bench.py:958-1049) A/Bs `run_trsqp` preplan only. The
landed reuse sites — def_twin `st_carry` (def_twin_falsifier.py:1074-1088, 1193, 1262),
rung-end `cs_stats(pre=)` consume (:1147-1154), margin_governor `rec_carry`
(margin_governor.py:495-505, 623) and O4-log `last_cert` consume (:550-557) — are gated
only by in-line `np.array_equal(W)` (+ `"cols" in lc["out"]`) conditions and by
code-reading argument-identity (same process, same engine objects, class knobs fixed in
scope — verified in this audit: campaign sets the class once, the MG walk runs inside
`design_class(xi)` at margin_governor.py:520-524, and no mutation of the carried
out/plan dicts was found in driver or consumers; the M1 stash even deep-copies,
a1_toc:1831-1834, while `last_cert` holds declared read-only refs :1318-1319). The "3
records/rung -> 1" claim (log:179-180) therefore rests on same-process determinism
(m12gate-class evidence) plus conservative fallbacks, not on an executable campaign-level
A/B.

**Repair**: one cheap control: a def_twin campaign debug mode (or one-rung gate) that
re-records fresh at a carried reuse and asserts bitwise equality — the M1-probe pattern
lifted to the campaign carries; or declare the coverage limit at the h3gate docstring.

## RF-5 — H4 code identity omits the ENVIRONMENT; the live numpy decision is the named vector
**Severity: LOW — Verdict: HOLDS-WITH-CAVEAT**

**Attack**: change jax/jaxlib/numpy (BLOCCATO 8: numpy 2.5.2 decision pending at session
boundary) — `check_tail_code` still passes, tail references consumed under a different
lowering environment.

**Evidence**: `code_identity()` hashes only the 6 repo modules
(def_twin_falsifier.py:144-155); no jax/jaxlib/numpy version, no x64 flag, no platform.
The registered cross-lowering floor (yaml:149-157) proves lowering sensitivity is real on
gradients (~1e-8 rel); tail VALUES are value-class (~1e-15 rel) and consumed against
bands of order 1e-2 (bar_f2d) and K_RICH x |J_def - J_def16| — so the quantitative
exposure today is negligible, which is why this is LOW and not MED. But the tail's
"reproduces exactly" claim is environment-conditional and nothing refuses on an env
change; `record_ctx_tag`'s own persistence rule (:1196-1200) names code identity only.

**Repair**: stamp `(jax.__version__, jaxlib, numpy, x64)` into the tail and WARN (not
refuse) on mismatch — refusal stays code-keyed, the env delta becomes visible instead of
silent.

## RF-6 — A1_FUSED_CERT=0 no longer selects the legacy interior dispatch when A1_COLEXEC=1 (default)
**Severity: LOW — Verdict: HOLDS-WITH-CAVEAT**

**Attack**: set only `A1_FUSED_CERT=0` (the M5a arbitration arm) and ask which path
interior cells take.

**Evidence**: `fused_on` and `colexec_on` are independent (a1_toc:348-349); the per-cell
`cell()` honors `fused_on` (:401-414) but the column executor unconditionally inlines the
FUSED entry `solvers["interior"][3]` (:236-252). With defaults, `A1_FUSED_CERT=0` yields
a MIXED path: interior cells fused-in-scan, wall/axis cells 2-dispatch legacy — the
legacy arbitration arm now requires BOTH flags. The gates are correct (m5gate pins
`A1_COLEXEC=0`, engine_speed_bench.py:578; m0/m12gate pin both, :253, :316), but the
interplay is undeclared for any other consumer of the arbitration env.

**Repair**: one docstring line at :348-349 declaring the interplay, or make `chain()`
defer to the per-cell branch when `fused_on` is false.

## RF-7 — Recorder decision-flip class extends beyond the cert verdict (truncation, wall_search, margin-floor); instance-gated at two nets only
**Severity: LOW — Verdict: HOLDS-WITH-CAVEAT** — cites registry row `record-path:cert-verdict-recorder-dependence` (yaml:131-139); NOT re-minted

**Attack**: find a decision quantity compared against a threshold using recorder-dependent
z: truncation `float(z[0]) > float(L)` on the colexec z (a1_toc:602-608), wall_search
`float(zt[0]) > float(pt1[0])` (:566-570, host in both paths but fed by ulp-shifted prev
columns), margin-floor raise on trace-m vs host-m (:394-399 with m from :246 vs :335-346).
A cell within the Newton floor of its threshold can flip the DECISION between recorders —
the same mechanism the registry row records for the cert verdict (measured 3.757 vs
0.585 at Wp). m5cgate proves dec-vector bitwise identity at exactly TWO nets
(engine_speed_bench.py:687, :737) and the near-seam pair at derived +/-dlt (:798-821) —
instance evidence, not a proof; at a third design a flip is possible and then plans
differ between recorders. Under the row's declared semantics (ACTIVE recorder =
authority) this is acceptable-by-declaration; the residual is that the row's text names
the cert VERDICT while the class covers every thresholded decision.

**Repair**: widen the registry row's wording to "any thresholded record decision"
(cheap edit within the existing row — no new row needed), keeping the m5cgate dec-vector
as the per-instance gate.

## RF-8 — Findings-registry lint: code dedup keys are format-checked but NEVER resolved; the anti-re-mint channel is narrow
**Severity: LOW — Verdict: HOLDS-WITH-CAVEAT**

**Attack**: construct entries that should violate but pass. Three constructions succeed:
(a) re-mint with a typo/nonexistent path — `_spans` only regex-parses
(tests/test_findings_registry.py:55-66) and check() never verifies file existence or
line range (:99-101); the lint's own seed entry uses fictitious `x.py:1-2` (:124-127)
and is treated as valid; (b) re-mint with a nudged ADJACENT span (e.g. 523-530 next to
the demonstrator's 516-522) — overlap requires intersection on the SAME file
(:109-118); (c) re-mint of any `code: []` row — five rows today (yaml:109, 118, 127,
172 class) sit entirely outside the machine channel ("may be empty" is declared,
docstring :19, but the consequence — span-less findings are unprotected by check (c) —
is not). Spans also drift silently as files are edited (no range-vs-file check).

**Repair**: resolve code keys (file exists, l2 <= line count) with a seeded rejector;
add a mechanism+file coarse dedup pass for span-less OPEN rows; accept span drift as a
declared limit or pin spans to anchor strings.

## RF-9 — Ratchet tier: skip-dir and scope-boundary escapes; only the increase direction is rejector-armed; magnitude drift 621 vs 622
**Severity: LOW — Verdict: HOLDS-WITH-CAVEAT** — cites registry row `test-suite:numeric-lint-scope-hole` (yaml:86-94); NOT re-minted

**Attack**: move literal debt where the ratchet cannot see it. Results: rename/delete
inside validation/ FAILS correctly (missing-baseline-row check,
tests/test_numeric_lint.py:201-202 — attack died); NEW file FAILS (:187-190 — died);
within-count swap passes (DECLARED limit, :34-36). What survives: (a) any `.py` under a
dir matching `sota_gapmap*` is skipped by prefix (:160-166) — future code there escapes
entirely; (b) relocation OUT of validation/ (to tests/, scripts/, repo root — in neither
src/ lint nor validation/ ratchet) fires the missing-row violation ONCE, whose printed
repair "remove it" (:202) then legalizes the escape permanently; (c) only the +1-bump
direction has a seeded rejector (:230-240) — decrease/new-file/missing-row rely on
unexercised code, against the R5 rejector standard; (d) the registry magnitude-of-record
says 621 literals (yaml:89) and the module docstring says 621 (:27) while the regenerated
committed baseline sums 622 (verified by summation; the +1 declared at log:342-345) —
the machine registry contradicts the machine baseline by one.

**Repair**: seed rejectors for the other three directions (trivial in-memory doctoring);
log-and-require an explicit allow row for skip-dirs; fix 621 -> 622 in yaml:89 and the
docstring; declare the outside-scope residual in the registry row's magnitude.

## RF-10 — M6 corrected-form acceptance criterion: the asymmetry yardstick is blind to symmetric error; max-norm is structure-blind
**Severity: LOW — Verdict: HOLDS-WITH-CAVEAT** — adoption-input; cites registry rows `engine:vmap-hessian-adjoint-divergence` (yaml:140-148) and `engine:cross-lowering-gradient-floor` (yaml:149-157); NOT re-minted

**Attack**: accept a dH inside `K_RICH x max(scheme asyms)` that still flips a TR-walk
decision. Two structural blind spots survive scrutiny: (a) "scheme asymmetry" measures
only the ANTISYMMETRIC error component — the symmetrization `Hw = 0.5*(Hw + Hw.T)`
(a1_toc:1753) cancels exactly what the yardstick sees, while a cross-lowering bias with a
SYMMETRIC component passes unmeasured; the fix-probe validated common-mode cancellation
(permutation BITWISE, s25bis_m6fix.log:6) but that control is within-batch, not
batch-vs-sequential-symmetric; (b) the comparison is max-norm global — a perturbation
concentrated on small-|H| entries governing a near-zero curvature direction can move a
TR-model eigen/step decision at magnitudes the global bound admits. Mitigations already
in place: adoption is DEFERRED with owner+trigger (yaml:147-148), default stays
sequential, and decisions inside scheme-noise are chance-level under BOTH schemes
(noise-parity logic — attacked and survived: an at-band gradient deviation equals the
scheme's own g-round-off propagation, so the m6gate band construction at
engine_speed_bench.py:911 is derivationally sound).

**Repair**: when the m6gate is re-formed at adoption (per the registry owner clause),
add one consumer-level invariance control (TR step/decision A/B over a short walk, or a
jacfwd cross-check — already a named F2 route) beside the dH bound.

## RF-11 — M5c core equivalence: all six attacks FAILED
**Severity: LOW — Verdict: HOLDS**

Attacks executed and their outcomes, for the record:
(i) `account()` refactor — the bookkeeping block is verbatim-moved (diff-context
verified); the only ordering change is `pt = pt_of_z(z)` hoisted before the abort raise
(a1_toc:416 vs legacy post-abort) — pt_of_z lambdas are pure, no observable difference;
abort still precedes argmax, cert precedes margin (:360-399); the margin-raise index is
additive schema only (:394-399).
(ii) partner slice `prev[Nv:]` — PROVED equivalent to the legacy j-loop in BOTH has_axis
cases: legacy j-1 runs Nv..len(prev)-1 with has_axis=True (n_avail=len(prev)-1, bound
+1+1, :586, :610-611) and with has_axis=False (n_avail=len(prev), bound +1) — both are
exactly `prev[Nv:]` (:590-591); empty-slice edges fall to the (empty) legacy loop.
(iii) tail-repeat padding — padded lanes sit AFTER all real lanes in a sequential
`lax.scan` carry chain (:239-247), so they cannot influence a real lane; the host reads
only rows [:n] (:489, :593) and padded rows never reach account() or the plan; a
non-convergent padded cell costs at most N_NEWTON=30 trips (the while_loop cap,
a1_ideal_march_jax.py:448) — no pathological slowdown; NaN in the condition exits the
loop.
(iv) executor cache `(id(solvers), id(state_fn), Lpad)` — strong refs pinned (:252-254)
make id-reuse impossible for the cache lifetime; the traced body reads NO design-class
module global (predict_interior_t/_foot_t read only args + module `state_q`, faithful to
the host `_foot`, a1_ideal:611-618 vs :653-665, including the y2==0 guard :633 vs
:686-687); `ta` flows as an operand. The one residual — in-process monkeypatching is
invisible to id-keys — is already DECLARED as a test-only hazard (log:265-268).
(v) bucket bounds — PROVED: fan runs NI-1 columns (:480), len grows +2/column from 1, so
the last fan chain sees exactly 2NI-3 partners (Lpad_fan exact, :474) and fan exit is
2NI-1; design columns number n_B+Nw (:526-535), `len(newcol) <= len(prev)+1` (wall_pt +
prev[1:Nv] + cells + axis, :584-643), Nv >= 1 and monotone (init :524, only incremented
:567-571), so partners <= 2NI-2+n_B+Nw with a step to spare (Lpad_des, :475); an
overflow would crash loudly on the shape assignment (:431-432), never corrupt.
(vi) `_COLEXEC_DOCTOR` — module default None (:224), read-only guard in chain
(:439-440), the only setter is m5cgate under try/finally (engine_speed_bench.py:774-782);
no production leak path exists.

## RF-12 — Gate constructions (m5cgate / h3gate / m6gate): vacuous-pass and arithmetic attacks FAILED
**Severity: LOW — Verdict: HOLDS**

(a) m5cgate: dec-vector covers n_B, per-fan n, per-design (N, Nv, n, has_axis), cert_n
(engine_speed_bench.py:697-703 class, check :737) — truncation/axis/wall_search flips
all surface through n/has_axis/cert_n; bands inherit the m4gate derived construction
(:741 = :185/:425 verbatim); the doctored control CANNOT pass vacuously — a never-matching
ctx leaves `fired=None` and fails the first check, and `exp = cert_n_at_chain + row`
(:786) is exact by the account() increment order (rows 0..row-1 accounted, abort at
cert n = start+row); a row landing in padding would produce NO refusal and FAIL the gate.
The near-seam dlt is band-derived (:798). (b) h3gate: counter arithmetic is exact
(preplan B == 1 at :1025, fresh B == A-1 at :1027, cached B == A+1 at :1029, probe-fired
at :1031); with memo off the preplan is ignored and `record_preplan==1` fails — not
vacuous; the probe's own fresh
re-record is uncounted in BOTH arms by declaration (a1_toc:1360-1363), so the +/-1
bookkeeping is honest. (c) m6gate: the band sqrt(EPS)*g_scale (:911) equals the FD
scheme's own g-round-off propagation into H (noise parity — derivation sound, see
RF-10); the corrupted-lane control asserts bitwise sequential recovery + count
(:932-937); the <= 8 s row is deliberately NOT in `ok` (:942 — a MEASURE input,
declared); and the gate demonstrably CAN fire — it did (the M6 rejection of record,
log:308-325).

---

## Convergence table

| Finding | Verdict | Needs judge? |
|---|---|---|
| RF-1 H4 artifact stale at HEAD | REFUTES-THE-EDIT | no — mechanical (hash-verified); needs the repair run, not adjudication |
| RF-2 preplan key contract | HOLDS-WITH-CAVEAT | yes — key-extension vs docstring-narrowing is a contract decision |
| RF-3 batched-path guard asymmetry | HOLDS-WITH-CAVEAT | no — mechanical repair, pre-adoption |
| RF-4 h3gate campaign-carry coverage | HOLDS-WITH-CAVEAT | no — right-size decision (control vs declared limit) |
| RF-5 env identity in H4 | HOLDS-WITH-CAVEAT | yes — env-stamp policy ties to the BLOCCATO-8 user decision |
| RF-6 FUSED/COLEXEC interplay | HOLDS-WITH-CAVEAT | no |
| RF-7 decision-flip class scope | HOLDS-WITH-CAVEAT | no — one-row wording widen in the existing registry row |
| RF-8 registry-lint span resolution | HOLDS-WITH-CAVEAT | no — mechanical |
| RF-9 ratchet escapes + 621/622 | HOLDS-WITH-CAVEAT | no — mechanical |
| RF-10 M6 acceptance criterion | HOLDS-WITH-CAVEAT | yes — input to the re-formed m6gate at F2/adoption |
| RF-11 M5c core equivalence | HOLDS | no |
| RF-12 gate constructions | HOLDS | no |

## Declared drops
**7 candidates dropped** (attacked, judged not worth a row): (1) the 3.4 walk-evals
coefficient in the M-D/M-E synthesis (pre-diff S25 advisory shape, anchored at
engine_speed_bench.py:215-221); (2) the Dv all-lanes-nonfinite division edge at
a1_toc:1701-1703 (pre-existing class, precondition implausible past a certified base;
the new guard did not introduce it); (3) "column dropped to zero curvature" comment vs
per-component substitution code (:1746-1751, wording nit); (4) m5cgate/h3gate DT.CASE
mutation without crash-restore (one-mode-per-process by main() dispatch); (5) `_resolve`
substring-anchor weakness (works as documented); (6) rejected-designs persistence under
field_records (checked: `_persist_rejected` serializes W/seg/error only — no cols leak);
(7) engine-cache in-process monkeypatch aliasing as a separate row (already declared as
a test-only hazard, log:265-268; noted inside RF-11(iv)).

## Summary
**12 findings: 1 refutes / 9 caveats / 2 holds**
