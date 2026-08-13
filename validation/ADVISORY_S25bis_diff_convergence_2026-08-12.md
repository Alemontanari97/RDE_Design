# ADVISORY — S25-bis diff review: FUSED CONVERGENCE (corrigendum of record)

**Form-2 converged round 1 (narrow agenda); judge layer subject to the
standing Form-3 rule — inline check at absorption.**

- **Positions adjudicated (full text, no slices)**:
  - A = adversarial refuter, `validation/s25bis_refute_diff.md`
    (12 findings: 1 refutes / 9 caveats / 2 holds);
  - B = perimeter sense-review (R29), `validation/s25bis_sense_perimeter.md`
    (13 findings: 8 adopt / 3 caveats / 2 changes / 0 open).
- **Authorities**: `docs/findings_registry.yaml`;
  `validation/PROGRESS_2026-08-12_S25bis_speed.md` (STEP 15 map);
  code at HEAD, spot-verified where contested.
- **Tree of adjudication**: HEAD = `56baed1` (a post-closure prompt/
  registry commit AFTER `ea8143c`, which both positions audited).
  Verified here: the six RECORD_PATH_MODULES and
  `validation/s24_deftw_derive.json` are byte-identical
  `1806ae2..HEAD` (empty `git diff --stat`) and worktree-clean — every
  file:line anchor in both positions transfers to the current tree
  unchanged.
- **Registry count of record (R5)**: 19 rows committed on disk
  (grep `^- id:` = 19, worktree clean). The positions read 17 — correct
  at their audit HEAD `ea8143c`; `56baed1` added
  `structure:monolithic-driver-module` (yaml:167) and
  `infra:scheduled-ci-multiplatform` (yaml:176). The tasking note's
  "21 rows" is NOT reproduced by the machine count; 19 is the number
  of record. Dedup below is checked against the 19.
- **Verdict labels**: ADOPTED / ADOPTED-WEAKENED (final wording here) /
  REFUTED-with-evidence / OPEN-with-owner+trigger. No new positions are
  minted; arithmetic checks and source spot-verification only.

---

## §1 — PRIORITY ADJUDICATION: RF-1 (the refuter's REFUTES row), verified at source by the judge

**Verification protocol executed independently** (not trusted from A):

1. Recomputed `code_identity()` exactly per
   `validation/def_twin_falsifier.py:150-155` (outer sha256 updated
   with each module file's sha256 digest, tuple order of
   `RECORD_PATH_MODULES` at `:144-147`, binary reads) on the HEAD
   worktree: **`ea5cd2ffe5e9b8ddd076c46389deb8fcf4e82bacd54ec4d4d00f0d32e799c0a3`**
   — bit-exact match with the refuter's reported digest (`ea5cd2ffe5e9…`).
2. Committed artifact `validation/s24_deftw_derive.json:76` carries
   `tail.code_id = fcd5e61ae11143105ef2ad994611ce81b8fd6790bed6a2d4cd8e1954d1e7bb0c`
   — **MISMATCH**.
3. `git show 1806ae2:validation/s24_deftw_derive.json` carries the SAME
   `fcd5e6…` code_id, and the six modules are byte-identical
   `1806ae2..HEAD` with a clean worktree ⇒ **the artifact was committed
   ALREADY STALE inside `1806ae2` itself**, exactly as A states.
4. Mechanism confirmed against the session's own log: `stage_derive`
   last ran in chain 1 (PROGRESS STEP 7, "derive PASS"); the M6 default
   flip + sequential nonfinite guards then edited
   `a1_toc_variational_jax.py` (a record-path module; the M6 block at
   `:1607-1625`, guards `:1693-1700`, `:1746-1751`); the final re-chain
   re-ran only "m12gate re-run + h3gate re-run" (PROGRESS STEP 12) —
   derive never re-stamped.
5. Channel hole confirmed: `grep code_identity|deftw_derive tests/` =
   **zero matches** — no suite/ONDEMAND row compares
   `tail["code_id"]` with `code_identity()` on the committed tree; the
   C4 git-backed staleness link is cross-commit by construction and
   cannot see intra-commit ordering.

**VERDICT: RF-1 ADOPTED — the refutation stands, dual-verified.**
Consequence at HEAD: `stage_campaign` refuses at open
(`def_twin_falsifier.py:1042-1044`, raise `:162-168`); the
pre-registered F3/F7 references are unusable; the [X-DEFTW] campaign
carrier is BLOCKED until derive re-runs. The refusal itself is the H4
mechanism working as designed (A concedes this; the judge confirms:
what fires at HEAD is precisely the designed loud refusal, not silent
consumption).

**Claims corrected of record (named verbatim)**:
- Commit `1806ae2`/`ea8143c` line: "derive re-run EXIT 0 REPRODUCES the
  S24 tail numbers exactly f2 1.4972e-02 < bar 2.0137e-02" — TRUE as a
  chain-1 event (`s25bis_derive_h4_run1.log` exists), FALSE as a
  description of the committed artifact's validity against the
  committed code.
- PROGRESS STEP 15 Class-A row: "H4 (reproduces the S24 tail numbers
  exactly + seeded stale-code refusal)" — see §4 for the explicit
  demotion statement.

**Repair (exact, sized)**: repair-list items R7-R9 + rejector R8 in §5
— all record-path edits batched BEFORE one `stage_derive` re-run;
artifact and code committed together; a new committed-tree staleness
check closes the channel class. Expected outcome declared: tail numbers
reproduce byte-identically (post-derive edits were default-env reads,
comments, and opt-in guard code); any moved number = STOP and
adjudicate as a fresh finding.

---

## §2 — CONVERGENCE TABLE (all 25 findings; merges declared)

| # | Finding | Merged with | Converged verdict | Disposition |
|---|---------|-------------|-------------------|-------------|
| RF-1 | H4 artifact stale at HEAD | — | **ADOPTED** (judge-verified) | Repair R7-R9 + rejector R8; registry NEW row (§6.1); §4 demotion |
| RF-2 | H3 preplan key contract overstated | B-F4, B-F5(i) [MERGE-2] | **ADOPTED-WEAKENED** | §3.1: colexec flag into ctx (R4) + docstring narrowing (R4) + probe forced on preplan consume (R5); solver-CONTENT keying declined |
| RF-3 | batched-path guard asymmetry | — | **ADOPTED** | R1 (consumer-side guard parity) + R2 (vg_batch × A1_PLAN_ARGS=0 raise); registry owner note (§6.2c) |
| RF-4 | h3gate campaign-carry coverage | — | **ADOPTED-WEAKENED** | §3.4: declared-limit line R12 now; campaign fresh-vs-carried A/B deferred with owner (§7) |
| RF-5 | H4 env identity omitted | B-F7 [MERGE-1] | **ADOPTED** (its WARN form prevails) | §3.2; repair R7 |
| RF-6 | FUSED×COLEXEC interplay undeclared | — | **ADOPTED** | R3 (docstring line; the chain()-defer alternative declined as an unforced version change); feeds the S-ORDINE flag-matrix registry (existing row yaml:167-175, cited not re-minted) |
| RF-7 | decision-flip class wider than cert verdict | — | **ADOPTED** | R11b (widen wording INSIDE the existing registry row `record-path:cert-verdict-recorder-dependence` — no new row); spot-verified at `a1_toc:566,602,621,394-399` |
| RF-8 | registry-lint spans never resolved | B-F13 [MERGE-5] | **ADOPTED** | R13 (existence + line-range resolution + rejector, seed re-pointed); span-less coarse dedup + symbol/snippet anchors = seeding-sweep duty (§7) |
| RF-9 | ratchet escapes; one-armed rejector; 621/622 | B-F12 [MERGE-4] | **ADOPTED** | R10 (three missing rejector directions + skip-dir visibility + docstring 622) + R11a (yaml 621→622 + declared residual); baseline re-summed by the judge: 622/33 confirmed |
| RF-10 | M6 criterion blind spots (symmetric error, max-norm) | B-F8, B-F11(iii) [MERGE-3] | **ADOPTED-WEAKENED** | §3.3: absorbed into the re-formed m6gate spec at adoption (R11c); no pre-adoption code change |
| RF-11 | M5c core equivalence — six attacks failed | B-F1/F2/F3 [MERGE-6] | **ADOPTED** (HOLDS ratified) | M5c implementation + design both stand; no repair |
| RF-12 | gate constructions sound | [MERGE-7] | **ADOPTED** (HOLDS ratified) | m5cgate/h3gate/m6gate constructions stand; m6gate band derivation ratified by B-F8's independent noise-propagation closure |
| B-F1 | M5c scan-of-while_loop + in-trace seeds | RF-11 [MERGE-6] | **ADOPTED** | No repair |
| B-F2 | tail-repeat padding vs P_DUM: principled | RF-11(iii) | **ADOPTED** | Cost accepted with the named lever (second design bucket) if pressure returns |
| B-F3 | host decisions + derived exact buckets | RF-11(v) | **ADOPTED** | Bounds independently re-derived by B, concordant with A's proof |
| B-F4 | H3 memo piggyback = control inheritance | RF-2 [MERGE-2] | **ADOPTED** | Mechanism adopted; its control-inheritance evidence is what defeats RF-2's key-extension branch (§3.1) |
| B-F5 | (i) probe-disarm × preplan; (ii) last_cert live refs | RF-2 [MERGE-2] | **ADOPTED** | (i) R5, force-controls option selected; (ii) R6 deepcopy |
| B-F6 | H4 file-hash granularity + numbers-not-blobs | — | **ADOPTED** | GAP-29 datum disqualifies bytecode/AST identity; unchanged |
| B-F7 | env fingerprint + module-closure check | RF-5 [MERGE-1] | **ADOPTED-WEAKENED** | §3.2: stamp + WARN (not refuse) + env-adoption re-stamp duty + named upgrade trigger; closure-rule line R7c |
| B-F8 | M6 acceptance criterion right; TR-step + norm pin | RF-10 [MERGE-3] | **ADOPTED** | Derivation arithmetic re-checked by the judge (2.2e-2 → ~2.1e6 vs measured 1.229e6; 7.583e6 = 1.13e-1/1.49e-8; 1.99e6 vs 2.06e6; 1.68x; 4.92e6 bound): closes | 
| B-F9 | ~1e-8 floor numerically expected; controls exclude defects | — | **ADOPTED** | Three scaling experiments → one line on the owned row (R11d) |
| B-F10 | pin-one-lowering + B-shape clause | — | **ADOPTED** | B-shape clause → one line on the owned row (R11d) |
| B-F11 | sequential default; route facts for F2 | RF-10 [MERGE-3, part (iii)] | **ADOPTED** | Route facts VERIFIED at source: `solve` is `@jax.custom_vjp` + `defvjp` only (`a1_ideal_march_jax.py:504-517`) ⇒ jacfwd blocked as written, true N5 price = implicit custom_jvp rule; central differences non-route (noise-dominated budget). Absorbed into R11c |
| B-F12 | ratchet = strict standard pattern; 621/622 nit | RF-9 [MERGE-4] | **ADOPTED** | R10/R11a |
| B-F13 | findings-registry schema sound; span-drift liability | RF-8 [MERGE-5] | **ADOPTED** | R13 now; anchor policy at seeding (§7) |

**Counts: 21 ADOPTED / 4 ADOPTED-WEAKENED / 0 REFUTED / 0 OPEN.**
No finding of either position is refuted; the four weakenings are
final-wording narrowings, each with its reason in §3.

---

## §3 — JUDGE DECISIONS WHERE THE POSITIONS DIVERGE (the corrigendum where it matters)

### §3.1 RF-2 × B-F4/B-F5(i) — the H3 preplan contract (A flagged needs-judge)
The docstring claim "all carried by the memo key"
(`a1_toc:1308-1311`) is overstated — verified: `record_ctx_tag` hashes
`type(solvers).__name__` only (`:1208`) and neither ctx nor `_mkey`
(`:1370-1379`) carries the active-recorder flag, while records are
recorder-dependent of record (registry yaml:131-139). A's two repair
branches were key-extension vs docstring-narrowing. **Decision: split
by cost/consumer.** (i) The RECORDER flag ENTERS the key (R4, 1-2
lines): it is measured verdict-bearing (3.757 vs 0.585) and the
registered "never mix" discipline becomes key-enforced at zero cost.
(ii) Solver-CONTENT keying is DECLINED: B-F4's verified
control-inheritance holds — the first-hit control does not trust the
contract, it re-records W fresh once and compares bitwise
(`:1443-1461`), so wrong-provenance preplans are caught empirically at
first consume; all in-tree callers pass the same `solv` object
(A verified); machinery for zero present consumers. The docstring is
narrowed instead (R4). (iii) The genuine residual hole was B-F5(i):
`A1_MEMO_PROBE=0` (declared use = capped campaigns, `:1289-1293`, the
exact H3 population) would leave the preplan consume UNGATED. Repair
R5 selects B's force-controls option over refuse-on-disarm: the probe
tax is one record per walk — exactly the record the preplan saved, so
the combination is never net-negative (B's own pricing, adopted).

### §3.2 RF-5 × B-F7 — environment in the H4 identity (A flagged needs-judge; the one true divergence: WARN vs REFUSE)
Both positions agree the environment must be STAMPED and that the
6-module closure rule needs a declared check. They diverge on
semantics: B would hash `(jax, jaxlib, numpy, x64)` INTO
`code_identity()` (env change ⇒ refusal); A would stamp-and-WARN,
keeping refusal code-keyed. **Decision: A's WARN form prevails;
B weakened — with B's silent-pass concern discharged structurally, not
dismissed.** Grounds: (i) the tail's consumption semantics are
band-based, not bitwise (B's own Finding 6 calls this "the correct
consumption semantics for floor-noise quantities"); refusal-grade
identity is reserved for inputs with MEASURED flip capability — code
constants have one (GAP-29 flip of record), the environment has none
on any tail quantity (values value-class ~1e-15 across re-lowerings;
f2 consumed at 34% headroom under `bar_f2d` — arithmetic checked:
2.0137e-2 / 1.4972e-2 = 1.345). Hashing env into identity would encode
an unmeasured severity as a hard refusal, against the R5
derived-not-magic discipline. (ii) B is right that a VERSION upgrade
lies outside the measured same-version re-lowering class — so the
delta must become VISIBLE and the re-stamp must become a NAMED duty:
env changes are already structurally gated (BLOCCATO 8 / O5 = user
decision at a session boundary, adoption-with-rejector class), and R7
adds "derive re-stamp of `s24_deftw_derive.json`" as an explicit item
of that env-adoption checklist. (iii) Named upgrade trigger (the
promotion path B's position earns): the first MEASURED env-driven
excursion of any tail quantity beyond its consuming band promotes
WARN → refuse (env enters `code_identity()`). The module-closure rule
("any module the tail path imports must be listed") lands as a
declared comment at `RECORD_PATH_MODULES` (R7c); B's closure trace
(TV/O33/A1/SC/TH feed the tail; locus_diagnosis/margin_governor/
adaptive_knot_optimize do not) is accepted as the evidence of record
that the list is correct today.

### §3.3 RF-10 × B-F8/B-F11(iii) — the M6 acceptance criterion (A flagged needs-judge)
No factual conflict: B derives that the budget is noise-dominated and
the asymmetry yardstick measures the irreducible floor (arithmetic
re-checked by the judge — every number closes within 2x); A shows the
yardstick is blind to a SYMMETRIC cross-lowering bias component and
that max-norm is structure-blind. B's derivation itself bounds A's
exposure (for decorrelated entry noise the symmetric part is
same-order; K_RICH = 4 covers it with ~2x spare) — so A's caveat is
real but bounded, and its repair coincides with B's caveat.
**Decision: one merged spec for the re-formed m6gate at adoption
(R11c), no pre-adoption code change**: in-batch base mandatory;
dH bound = K_RICH × max(scheme self-asymmetries) with the NORM pinned
in the gate text; the corrupted-lane control kept; PLUS one
consumer-level invariance control (one-shot TR-step agreement at
matched radius — one subproblem solve, both positions' shared
prescription); the symmetric-component residual named in the gate
text as the declared limit the TR-step check covers. RF-10 is
ADOPTED-WEAKENED only in that its "passes unmeasured" is recorded as
a bounded declared limit, not an open defect.

### §3.4 RF-4 — h3gate coverage of the campaign carry sites
A's own audit found the consume-site gating real (bitwise
`np.array_equal(W)` + fresh fallback at both consumers; M1 stash
deep-copies; no mutation found) — the residual is that carried-content
reuse rests on same-process determinism rather than an executable
campaign A/B. **Decision: right-size per A's second option** — R12
declares the coverage limit in the h3gate docstring NOW; the one-rung
fresh-vs-carried bitwise A/B is DEFERRED with owner+trigger (§7,
first campaign window), which is structurally-gated postponement
(a campaign-mode control needs a campaign window), not a dropped
resolvable.

---

## §4 — CROSS-CHECK AGAINST THE SESSION'S OWN CLAIMS (PROGRESS STEP 15)

**Does any finding DEMOTE a Class-A (proof-total) claim? YES — exactly
one, partially; stated explicitly:**

- **DEMOTED (partial)** — Class-A row "H4 (reproduces the S24 tail
  numbers exactly + seeded stale-code refusal)" (PROGRESS:424-425).
  Split of record: the H4 MECHANISM (stale-code refusal + seeded
  rejector at every campaign open) REMAINS Class A — it is precisely
  what fires at HEAD, dual-verified. The H4 ARTIFACT-OF-RECORD at HEAD
  fails its own gate: the committed tree does not carry a consumable
  derive artifact, and [X-DEFTW] is blocked. Corrigendum: "H4
  artifact-of-record at HEAD" moves **A → C (open-with-owner)** until
  the R7-R9 re-stamp lands; the `1806ae2`/`ea8143c` commit claim named
  in §1 is corrected of record. The session-closure claim "session
  complete, nothing dropped silently" acquires this one exception: the
  drop was silent at commit time (no channel existed to see it — the
  channel is built by R8).

- **NOT demoted — checked row by row**: M1+M2 (untouched), M4
  (untouched), M5a (untouched), M5b (untouched), M5c dec-vector
  (RF-11: all six attacks failed; both positions concordant), H3
  bit-identical arms + M1 controls (h3gate proof intact; RF-2/RF-4 are
  contract/coverage caveats absorbed by R4/R5/R12), M6
  lane-permutation control (bitwise as scoped; RF-10's within-batch
  scoping recorded in the adoption spec), C4 tier (RF-1 exposes a
  channel OUTSIDE C4's declared cross-commit scope — a new channel is
  added by R8, the C4 claim itself stands), H6 cache, R28 ratchet (the
  seeded +1 rejector claim is literally true; RF-9's three unarmed
  directions are a coverage gap repaired by R10, not a false claim),
  R31 lint (the 4 seeded rejectors fire as claimed; RF-8 narrows the
  channel's REACH, repaired/priced by R13 + seeding).

- **Class B rows**: (2) recorder-dependence — RF-7 WIDENS the declared
  class (truncation/wall_search/margin-floor thresholds share the
  mechanism; spot-verified at source), no contradiction; (3)/(6)
  cross-lowering floor — B-F9 ratifies the convergence claim and adds
  the three scaling experiments to the already-owned F2 derivation
  candidate; (5) GAP-29 — untouched.

- **Class C rows**: consistent; M6 adoption gains the enriched gate
  spec (R11c); R31 corpus seeding gains the anchor-policy duty; "R29
  perimeter sense-review of the S25-bis touch → next window" is
  CONSUMED by this very review (B is that review; this advisory closes
  its convergence).

- **The FINAL SPEED COUNTER OF RECORD (segment M-D 14.9 s / M-E 20.1 s
  pessimistic vs <= 30; campaign ~10-14 min vs <= 25; record 18x) is
  NOT moved by any converged finding.** A's drop (1) declared the
  synthesis coefficient out of scope; B-F2/B-F3 ratify the measured
  cost structure; the M-D/M-E spread stays owned by
  `bench:speed-measurement-variance` (yaml:158-166).

---

## §5 — REPAIR LIST (in-window micro-commit; each item ≤ ~15 lines; ORDER IS LOAD-BEARING)

Sequencing rule (from RF-1's mechanism): every edit to a record-path
module re-stales the H4 artifact ⇒ ALL record-path edits (R1-R7) land
BEFORE the single derive re-run (R9); code + re-stamped artifact commit
TOGETHER; the new rejector (R8) then holds the channel.

**Phase 1 — record-path module edits**

- **R1** `validation/a1_toc_variational_jax.py:1673-1683` and
  `:1728-1738` (batched branches, opt-in path): guard parity with the
  shipped sequential blocks. (a) After `h = …` in the batched precond
  branch, replicate the `bad_j` floor block of `:1697-1700`
  (`bad_j = ~np.isfinite(h); h = np.where(bad_j, 0.0, h)`) WITHOUT
  re-incrementing `hess_lane` (the lane was already counted in
  `vg_batch_rows`) + one comment line. (b) Before forming `Hw` in the
  batched Hessian branch, substitute any residually nonfinite row of
  `_gsh` with `g_base` (mirror of `:1746-1751`), same no-recount rule.
  ~8 lines total. (RF-3; closes the REQ-NONSTALL asymmetry under
  `A1_VMAP_HESS=1`.)
- **R2** `validation/a1_toc_variational_jax.py:1131` (before the
  `A1_PLAN_ARGS=0` constants-baked return):
  `if vg_batch: raise RuntimeError("vg_batch requires the args engine
  (A1_PLAN_ARGS=1): a constants-baked batched entry re-bakes the plan
  per segment — the churn class M4 deleted")`. ~3 lines. (RF-3(b),
  enforcing the declared contract at `:886-888`.)
- **R3** `validation/a1_toc_variational_jax.py:348-349`: one comment
  declaring the interplay — `A1_FUSED_CERT=0` is honored by per-cell
  sites only; the column executor always inlines the fused entry
  (`:237,242`); the legacy arbitration arm requires BOTH flags 0 (as
  m0/m12gate/m5gate pin). ~2 lines. (RF-6.)
- **R4** `validation/a1_toc_variational_jax.py:1191-1213`
  (`record_ctx_tag`): add the active-recorder flag to the hash
  (`h.update(b"colexec:%d" % int(colexec-env-read))`), ~2 lines; AND
  narrow the H3 docstring at `:1308-1311`: solvers enter the key by
  TYPE NAME only — content identity rests on the first-hit probe plus
  same-process object discipline. ~2 lines. (RF-2 final wording.)
- **R5** `validation/a1_toc_variational_jax.py:1443`: force the
  first-hit controls on a preplan consume regardless of the probe env —
  condition becomes
  `if (probe["armed"] or rec_counts["preplan"]) and probe["eq"] == 0:`.
  1 line + 1 comment (tax = the one record the preplan saved).
  (B-F5(i).)
- **R6** `validation/a1_toc_variational_jax.py:1599`: deep-copy the H3
  return slot
  (`last_cert.update(W=W.copy(), out=copy.deepcopy(out_rec),
  plan=copy.deepcopy(plan))`) and update the `:1318-1320` docstring
  "refs, read-only contract" → "deep-copied". ~2 lines. (B-F5(ii);
  microseconds against a 5.6 s record.)
- **R7** `validation/def_twin_falsifier.py`: (a) stage_derive tail
  gains `env = dict(jax=…, jaxlib=…, numpy=…, x64=…)` beside
  `code_id`; (b) campaign open WARNs loudly (print, non-raise) on env
  mismatch with the stamped values — refusal stays code-keyed; (c) one
  comment at `RECORD_PATH_MODULES:144-147` declaring the closure rule
  ("any module the tail path imports must be listed"; closure traced
  2026-08-12: rung_logs/cs_stats → TV/O33/A1/SC/TH only). ~10 lines.
  (MERGE-1 final form, §3.2; upgrade trigger registered in §6.1.)

**Phase 2 — the derive re-run (the RF-1 repair proper)**

- **R8** NEW committed-tree staleness check (suite, group (xix)
  vicinity or its own function): load
  `validation/s24_deftw_derive.json`, import
  `def_twin_falsifier.code_identity`, assert
  `tail["code_id"] == code_identity()`; seeded rejector = doctored
  code_id must mismatch. Declared scope: the closing suite runs on the
  committed tree (R3 discipline), so this is exactly the channel RF-1
  proved missing (grep of record: zero existing references). ~12-15
  lines.
- **R9** RUN `stage_derive` on the final Phase-1 tree (EXIT-gated,
  redirect-only) → re-stamps `tail.code_id` (+ new `env` field).
  EXPECTED: tail numbers byte-identical to the S24 figures
  (f2_geno 1.4972280462197103e-02 < bar 2.013701802534313e-02,
  J_def 40262478.941368885, J_def16 40263824.53075551, cert_n_g2
  30643); ANY moved number = STOP, new finding, no commit. Commit
  Phase-1 code + artifact + R8 in ONE commit.

**Phase 3 — instruments and registry (non-record-path)**

- **R10** `tests/test_numeric_lint.py`: (a) docstring `:27` "621" →
  "622" with the STEP-12 regen note (+1 = the m6gate mode's own code);
  (b) seed the three unarmed rejector directions next to `:230-240`
  (in-memory doctoring: `bumped[rel0] -= 1` → decrease row;
  fake `validation/__seed_new__.py: 1` in a counts copy → NEW FILE row;
  fake baseline row → missing-file row); (c) 2-3 visibility lines in
  `iter_validation_scope()` printing skipped dirs matching
  `VAL_SKIP_DIRS` (`:160-166`) with their `.py` count. ~15 lines
  total. (MERGE-4.)
- **R11** `docs/findings_registry.yaml` edits (dedup-honoring — all
  INSIDE existing rows except (e)): (a) `test-suite:numeric-lint-scope-hole`
  magnitude "621" → "622" + declared residual clause (skip-dirs
  `sota_gapmap*` and relocation outside `validation/` sit outside the
  ratchet channel); (b) `record-path:cert-verdict-recorder-dependence`:
  widen the class wording to "any thresholded record decision (cert
  verdict; truncation `float(z[0])>L` a1_toc:602/:621; wall_search
  revision :566; margin-floor raise :394-399) — per-instance gate =
  the m5cgate dec-vector"; (c) `engine:vmap-hessian-adjoint-divergence`
  owner: append the re-formed m6gate spec (in-batch base mandatory;
  dH ≤ K_RICH × max scheme self-asymmetry with the NORM pinned;
  corrupted-lane control kept; one-shot TR-step-agreement spot check;
  symmetric-component residual declared) + route facts (jacfwd blocked:
  `solve` is custom_vjp-only, true N5 price = implicit custom_jvp
  rule; central differences non-route in a noise-dominated budget) +
  "R1/R2 guards landed" note; (d) `engine:cross-lowering-gradient-floor`
  owner: append the B-shape clause ("one lowering = one compiled
  executable AND one batch shape") + the three scaling experiments
  (N-ladder / margin / float32). Each edit ≤ ~4 lines. (e) NEW row §6.1.
- **R12** `validation/engine_speed_bench.py` (h3gate docstring,
  ~`:958`): declared-limit lines — h3gate A/Bs the driver preplan arm;
  def_twin/margin_governor carry sites are gated at consume by
  bitwise-W checks + fresh fallback; the campaign-level
  fresh-vs-carried A/B is a registered option at the first campaign
  window. ~3 lines. (RF-4 final form.)
- **R13** `tests/test_findings_registry.py`: resolve code spans —
  file must exist under ROOT and `l2` ≤ its line count (extend
  `check()` near `:99-101`); seeded rejector with a nonexistent-path
  entry; re-point the demo seed's `code` from fictitious `x.py:1-2`
  (`:124-127`) to a real span so demo predicates stay clean.
  ~12-15 lines. (MERGE-5 in-window half.)

**Phase 4 — gates and suite (EXIT-gated, redirect-only)**: h3gate
re-run (R4/R5/R6 touch the memo/preplan machinery — expected: same
counters, controls fire on the preplan consume), m12gate re-run
(driver touched), the two lint groups (vii)/(xix) with all seeded
rejectors (now 4+3 ratchet directions, +1 registry-resolution, +1
staleness check), full closing suite. O3.1 not re-required (replay
math untouched; R1/R2 live on the opt-in batched path, R3-R7 are
comments/bookkeeping/host-side).

**13 items.** Not in this list (deliberately): any change to the M5c
executor, the M6 default, the m6gate band, the H4 hash granularity, or
any record-path numeric — all adjudicated ADOPT as-is.

---

## §6 — FINDINGS-REGISTRY DELTAS (dedup-checked against the 19 committed rows)

### §6.1 ONE new row (no existing row spans `def_twin_falsifier.py`; no OPEN-span overlap — machine rule checked)

```yaml
- id: persistence:derive-artifact-intra-commit-staleness
  status: CONFIRMED        # -> DISCHARGED when R7-R9 + R8 land (evidence = re-stamped artifact + staleness check green in the closing suite)
  severity: high
  magnitude: "committed tail.code_id fcd5e61ae111... vs committed-tree code_identity ea5cd2ffe5e9... (recomputed independently twice, bit-identical results); six record-path modules byte-identical 1806ae2..HEAD, worktree clean => artifact stale INSIDE 1806ae2; [X-DEFTW] stage_campaign REFUSES at open (loud, fail-safe direction); mechanism = derive ran chain 1, a1_toc edited after (M6 default flip + guards), final re-chain m12gate+h3gate only; C4 git-backed link is cross-commit and cannot see intra-commit ordering; zero suite references to code_identity (grep of record)"
  source: "validation/ADVISORY_S25bis_diff_convergence_2026-08-12.md#RF-1"
  code: ["validation/def_twin_falsifier.py:144-168"]
  mechanism: intra-commit-staleness
  owner: "in-window micro-commit (repair list R7-R9 + R8 of the convergence advisory); WARN->refuse upgrade trigger for the env stamp = first measured env-driven excursion of any tail quantity beyond its consuming band"
  trigger: "immediate — the [X-DEFTW] campaign carrier is blocked until the re-stamp"
```

### §6.2 Row edits (inside existing rows — NEVER re-minted)
As specified in R11(a-d): `test-suite:numeric-lint-scope-hole`
(magnitude 622 + residual), `record-path:cert-verdict-recorder-dependence`
(class widened), `engine:vmap-hessian-adjoint-divergence` (re-formed
gate spec + route facts), `engine:cross-lowering-gradient-floor`
(B-shape clause + scaling experiments).

### §6.3 Explicitly NOT minted (dedup verdicts)
- RF-6/flag-matrix → cited row `structure:monolithic-driver-module`
  (yaml:167-175) already owns the flag-matrix registry at S-ORDINE
  T2-bis(b).
- RF-9 speed/variance adjacencies → `bench:speed-measurement-variance`
  (yaml:158-166) untouched.
- M6/floor content → the two engine rows (yaml:140-157) absorb
  everything via R11(c,d); no third row.
- B-F5/RF-2/RF-4 H3 caveats → repaired in-window (R4-R6, R12); no row
  (a finding repaired with gated evidence in the same window needs no
  OPEN row; this advisory is the record).

---

## §7 — DEFERRED ROWS WITH OWNER (structurally-gated; none generic)

| Deferred item | Owner | Trigger |
|---|---|---|
| M6 adoption decision (candidate ADOPTION-READY; re-formed m6gate per R11c spec incl. TR-step check + norm pin) | F2 entry / session boundary (M3 precedent) | one-flag flip + re-formed gate + walk-gate re-chain |
| Full corpus seeding of the registry + anchor policy (symbol/snippet anchors for high-value rows; coarse mechanism+file dedup for span-less OPEN rows) — MERGE-5 residual | F2 FIRST duty (R31, named) | next session open; corpus now includes BOTH position files + this advisory |
| Per-file classification of the 622 baselined literals | F2-entry hygiene window (existing row) | F2 entry; touched file classifies its own literals |
| Campaign-level fresh-vs-carried one-rung bitwise A/B (RF-4 residual) | first campaign window ([X-DEFTW]/[X-MGOV]) | first campaign anomaly implicating a carried record, or the window itself |
| NTF derivation; GAP-5 consequence adjudication; delta-carrier; [OBJ-DOM] | F2 (existing rows, unmoved by this review) | as registered |
| Flag-matrix registry (A1_COLEXEC × A1_FUSED_CERT × A1_PLAN_ARGS × A1_VMAP_HESS × memos), fed by R3's declared interplay | S-ORDINE T2-bis(b) (existing row) | S-ORDINE session |
| Three-level SOTA trace consuming this convergence (MC8 class) | S-CERT | S-CERT session (this advisory + both positions are inputs) |
| Env decisions (numpy 2.5.2 / filelock) + the NAMED derive re-stamp duty on any env flip | user, session boundary (BLOCCATO 8 / O5) | user ratification |
| Cross-lowering floor: formal chain-amplification derivation + the three scaling experiments | F2 (existing row, R11d) | as registered |

---

## §8 — INSTRUMENT WEIGHT (orchestration-weight report)

Shape: **2 positions + 1 fused judge, exactly 1 round** (B requested no
judge round; A flagged 3 needs-judge rows — RF-2, RF-5, RF-10 — all
adjudicated in §3; no relaunches, no ritual rounds). Position-side
token/effort weights: **UNRECORDED** (per R5 — no measured counts exist
in either artifact; declared, not estimated). Judge-side weight: full
ingestion of 2 positions + 2 authorities; 10 targeted source reads; 2
verification commands (independent `code_identity` recompute — digest
bit-identical to A's, giving the REFUTES row dual independent
verification — and the baseline re-sum 622/33); 1 output file (this).
Merges collapsed 25 findings into 18 adjudication objects; zero
findings required a second position pass.

---

**FINAL**: 21 adopted / 4 adopted-weakened / 0 refuted / 0 open;
repair list = 13 items (R1-R13, phase-ordered, all ≤ ~15 lines each,
one derive re-run). One partial Class-A demotion declared (§4, H4
artifact-of-record at HEAD → C until re-stamp); the speed counter of
record and every other STEP-15 class assignment stand. This document
is the corrigendum of record where the positions diverged (§3.1-§3.4).
