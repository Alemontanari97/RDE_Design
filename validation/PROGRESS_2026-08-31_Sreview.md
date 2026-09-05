# SESSION LOG — S-REVIEW (agnostic review of the FOUNDATIONS at the F2-entry milestone) — EXECUTED 2026-09-05 on the carrier dated 2026-08-31 (file names carry the carrier date; every act date in this log = 2026-09-05, measured `date` at open: Sat Sep 5 10:01 2026)

Carrier of record: `validation/ADVISORY_SREVIEW_prompt_2026-08-31.md`
(PENDING-CONTRACT at open; sections A-F executed integrally; status flips
to CONSUMED at R3 close). Session chain: F2-B0 (R39, commits
4798713/127dfdd) -> **S-REVIEW (this session, out-of-phase review at the
F2-entry milestone)** -> F2.REPR (carrier
`validation/ADVISORY_F2REPR_prompt_2026-08-31.md`, consumes the ASSESSMENT)
-> F2.ENGINE -> F2.M-RED -> F2.CFD-2 -> F3.* -> F3.TWIN.
User order of record (2026-09-05, this session's opening message): execute
the carrier integrally, sections A-F; Fable; act dates = today, measured;
ceiling ratified-or-changed at T1 (exceeding = user decision, never silent);
explicit opt-in: deterministic Workflows in the derive/diff/converge/verify
phases (adaptive fan-out, until-dry with dead-agent = failure, dual-seed),
landing ALWAYS inline; artifacts on file immediately; resume never relaunch;
consumption reported at R3 (SR-9); env pinned; GENO read-only; git add by
pathspec only; no theory re-derivation; no numerical campaign; ONE session;
GO/NO-GO mandatory; "CONFIRM on everything" is an acceptable outcome.

Raws directory: `validation/sreview_raws_2026-08-31/`.

## R2 OPENING DECLARATION (protocol executed before any authoring)

Readings performed in order (SR-12: every count below re-measured in this
window): `docs/START_HERE.md` -> project memory (s-f2b0-closed,
s-roadmap-closed, s-foundations-design, s-foundations-c4-closed,
fservice-scert-double-session, agnostic-milestone-review-directive,
choice-adjudication-convergence, s20-adaptive-obstruction,
s22-f1-governor-o4, agentic-orchestration-forms, orchestration-weight-sota)
-> M0 Parts I-II integral (:25-408, the axioms: D-DOM, D-JEX, D-MU,
D-CONTRACT + L4-CERT, D-S1, D-P) + Part VI core (:3052-3200, VI.1-VI.7 +
VI.4bis + G0) + the F2-B0 registration block (:4250-4299) + Part VII
(:4301-4340) -> D1 problem book §9 hypothesis ledger + §10 problem
statements (:481-575), heading map §1-§10 -> D6 plan v3 spine F0-F6
(:21-280), gates §5 (:751-818), Annex B (:1133-1157), DATED ADDENDUM
2026-09-05 (:1159-1213) -> pipeline decision map integral (stages 1-8, §9
edges, §10 machine summary, §11 refuter disposition) -> PROGRESS
(ORA/NEXT/BLOCCATO/census) -> TWIN protocol §1-9 integral -> F2.REPR
carrier integral -> F2-B0 log (R2/R8 declaration, touchpoint register,
LOG-10c closing-refuter lessons) -> S-FOUNDATIONS Phase-A precedent
(phaseA_problem_brief.md integral = the agnostic-brief template of record;
fork lists of the 4 condensed trees; phaseB_tree_diff.md header) ->
roadmap regenerated.

Roadmap regeneration + lint (xxiv), MEASURED IN THIS WINDOW:

```
$ python tools/roadmap_derive.py; python tests/test_roadmap_coverage.py
wrote docs\ROADMAP_critical_path.md (16 steps, 96 overrides, 65 OUT, 370 atlas mentions)
  seeded rejector [planted orphan node]: REJECTED (as required)
  seeded rejector [critical finding forced OUT]: REJECTED (as required)
  seeded rejector [doctored ROADMAP body]: REJECTED (as required)
  seeded rejector [dead manifest path]: REJECTED (as required)
  roadmap coverage lint (S-ROADMAP, derived not authored) PASS (16 steps; 8 phases, 7 gates, 79 nodes, 62 ledger, 210 OPEN findings [48 critical], 22 BLOCCATO [3 critical], 37 open-class claims of 163, 370 atlas mentions; 96 overrides, 65 OUT; manifest 30 entries; 0 violations)
```

Other measurements at open: HEAD 127dfdd, commit count 302 (`git rev-list
--count HEAD`); ledger 62 = 12 DECIDED / 38 MIXED / 10 NEVER / 2
SINGLE-AUTHOR (`grep status: docs/choice_ledger.yaml | sort | uniq -c`;
the decision map's own tally 12/36/12/2 is the 2026-08-21 snapshot, C57/C60
left NEVER at F2-B0 — reconciled, not a defect); findings path: 48
critical / 118 non-critical / 44 paper; env measured: Python 3.13.14,
numpy 2.5.2, scipy 1.18.0, jax 0.11.0 -> envfp **e100f996** (same as the
F2-B0 stamps: no env drift at open); ADVISORY_INDEX 252 lines with the
S-REVIEW and F2.REPR carriers at rows :250-251 (PENDING-CONTRACT).

DECLARED START POINT: session **OUT OF PHASE** at the **F2-entry
milestone** (D6 F2 opened, "F2 session 1/6" consumed by F2-B0; this
session does NOT consume an F2 session counter — it is a review act
decided by the user at the F2-B0 close, T6); ROADMAP step gated = **F2.REPR**
(row NEXT, path critical, BLOC override B-SREVIEW placed at F2.REPR by
F2-B0 repair R6); path **critical** — this session's GO / NO-GO /
GO-CON-PILOT verdict gates F2.REPR and F2.ENGINE. No F2 engine code is
touched here (the review finds gaps, re-orders, pre-registers pilots).

## R8 GATE-FIRST DECLARATION (on file, before authoring)

(i) CONSUMER / exact persona (CONSECUTIO D1): **the JPP referee who will
judge the decisive number** (skeptic: asks "why not X?" at every
foundational choice, asks which control / band / second number would
convince them) **+ the PM who asks "is this the shortest credible path to
that number?"**. Every verdict in the ASSESSMENT is written to those two
readers; no generic listener. The F2.REPR orchestrator is the downstream
CONSUMER of the assessment (its carrier §A), not its persona.

(ii) EXIT CRITERIA (carrier §E, measurable):
- E1 agnostic problem statement on file with the agnosticity lint PASS
  (0 registry ids / 0 carrier-ledger names, machine-measured, rejector
  seeded).
- E2 BASE-HYPOTHESES table per pipeline stage (data -> contract -> march
  -> certificates -> optimizer -> cycle layer -> Verdict -> claim): every
  hypothesis with rigor class, falsifier, carrier or a NAMED GAP; gap =
  findings row with `path:`.
- E3 COMPLETENESS table per stage: built / proven / measured / missing,
  today and for the next steps; every "missing" with an owner.
- E4 for EVERY foundational sub-problem: CONFIRM (new reasons) / FLIP
  priced / PILOT pre-registered, with an AGREED falsifier and an
  independent verifier; level 2 complete, level 3 per T2.
- E5 RABBIT-HOLE census: boundary declared, one alternative frame per
  obstruction, estimated cost; no entry without "how it changes the
  decisive comparison".
- E6 GO / NO-GO / GO-CON-PILOT for F2.REPR and F2.ENGINE in the
  ASSESSMENT of record; D6 amendments PROPOSED (never applied) at the
  touchpoint; red team of the decisive number with outcome; dual-seed
  canary reported; SR-9 consumption reported; plain suite green; commit;
  PROGRESS NEXT = F2.REPR.
- Plus the six grade levers F1-F6 of carrier §F (cadence rule R9 as a
  PROPOSAL; minimum viable engine perimeter; anchors-by-id census +
  progress_counts; certification stability as a foundational requirement;
  priced engineering plan; orchestration upgrades).

(iii) ORCHESTRATION CEILING — TOUCHPOINT T1, decided here under the user's
explicit delegation ("ratificalo o cambialo al touchpoint T1"): the
carrier's proposal is RATIFIED WITH ONE AMENDMENT OF UNIT. Under the user's
until-dry order every round is a FRESH agent call (workflow agents do not
keep context between rounds), so the honest unit is the agent CALL, not
the role; the ceiling is stated in both.

| stage | roles | calls (expected / MAX) | notes |
|---|---|---|---|
| order 1: refuter on the carrier | 1 | 1 / 1 | Fable, high effort |
| Stage A derive: de-novo derivers | 4 | 4 / 6 | 4 lenses; a leaked (non-agnostic) output is DISCARDED and its lens re-run once (max 2 re-runs) |
| Stage A diff: judges per sub-problem | 8 | 8 / 8 | 9 sub-problems, SP5 (frame) + SP6 (parametrization) merged (same objects); Fable |
| Stage B converge: advocate + refuter per selected item | 2 x <= 6 | 24 / 36 | per item max 3 refuter rounds (calls: A0, R1, A2, R3, A4, R5); a null/dead agent = FAILURE (never "dry") |
| Stage B dual-seed refuter lot | 2 | 2 / 2 | one known-FALSE position (refuter must kill) + one known-TRUE position (refuter must not kill) |
| Stage B judges (independent persona, not the orchestrator) | 2 | 2 / 2 | one judge per 3 items (merge-when-coverage-allows) |
| red team of the decisive number | 1 | 1 / 1 | parallel to Stage B |
| verify: one verifier per verdict + dual-seed canary + red-team verifier | <= 9 | 8 / 9 | verifiers read FILES, never summaries |
| closing refuter on the assessment | 1 | 1 / 1 | delta-audit vs E1-E6 |
| **TOTAL** | **~38 roles** (carrier: 25-35) | **~51 / 66 calls** | token ceiling **10M subagent tokens** (carrier expectation 5-8M) |

Exceeding 66 calls or 10M subagent tokens = STOP and ask the user (never
silent). Model Fable everywhere (memory model-pinned-fable); effort tiers:
judges/refuters/verifiers high, derivers high (the tree IS the value),
mechanical stages low. Resume-never-relaunch (workflow scriptPath +
resumeFromRunId). Consumption reported at R3 (SR-9) with shape + rounds +
tokens per stage.

(iv) RABBIT-HOLE BOUNDARY (declared): every Stage-B item, red-team point
and rabbit-hole census entry must state HOW it changes the credibility or
the cost of the decisive comparison (the truncated-plug head-to-head at
~1% Isp); an item that changes neither is OUT OF SCOPE by declaration.
Time box per Stage-B item = 3 refuter rounds. One alternative frame per
obstruction. NO theory re-derivation (S-FOUNDATIONS did it, 2026-08-17/21),
NO numerical campaign (F2). The prior de-novo trees of S-FOUNDATIONS Phase A
(validation/sfoundations_raws_2026-08-13/phaseA_tree_*.md, 141 forks,
brief = formulation-level) are INPUTS to this session's diff judges as
prior independent evidence; this session's derivers attack the
PIPELINE-level sub-problems the 2026-08-17 brief did not pose
(certification stability across versions/recorders/env, data ingestion,
the decisive experiment itself, cost/generality/risk per approach).

## TOUCHPOINT REGISTER (T1-T4; decided at open by the orchestrator under the carrier's defaults and the user's delegation; user ratification at the next touchpoint — recorded in PROGRESS BLOCCATO B-SREVIEW at close)

| id | decision | grounds | consequence in-window |
|---|---|---|---|
| T1 | **RATIFIED WITH AMENDMENT OF UNIT** (table above: ~38 roles, ~51/66 calls, 10M tokens hard ceiling) | the carrier's 25-35 "agents" cannot hold an until-dry loop with fresh calls per round; stating calls + tokens makes the ceiling checkable | ceiling enforced in the workflow scripts as asserts (max rounds, dead-agent = failure); consumption per stage in LOG-SR9 |
| T2 | **level 2 (paradigm) ALWAYS; level 3 (physical pins) = YES, RELEVANCE-SCAN ONLY** | the pins (pure periodic single-mode wave; frozen thermally-perfect mixture; no two-phase; case-A specs-only data for the decisive comparison) are USER pins; the carrier asks yes/no "per rilevanza sul TWIN" — cheap, in scope, and exactly the referee's question | derivers receive the pins as DECLARED-STATUS scope pins (free to state what they would relax); the SP7 diff judge + the red team classify each pin as BEARS / DOES-NOT-BEAR on the decisive number with a stated reason; a pin that BEARS = findings row `path: critical`, owner = user (no re-adjudication of a user pin here) |
| T3 | **PILOT executor = F2.ENGINE as a duty with carrier (carrier default)**, EXCEPT a pilot whose kill criterion gates the GO itself -> GO-CON-PILOT with the pilot as the FIRST act of the gated step (F2.REPR entry or F2.ENGINE entry, named per pilot) | anti-meta cadence: seven meta sessions since 2026-08-13 — no dedicated post-review session; a pilot is a build act | every PILOT verdict carries: one case, kill criterion, owner step, window, cost |
| T4 | **YES** — the decisive number itself is in the red team's perimeter (carrier default) | the JPP-referee persona's first question is about the experiment, not about the machinery | red-team brief = TWIN protocol §1-9 + agnostic statement; outcome = dated PROPOSED amendments to the protocol (never applied here) or CONFIRM with reasons |

## SESSION PLAN (carrier §C order; step 1 BLOCKING for the deliverables' final form)

1. REFUTER on the carrier (single-author F2-B0) -> PROMPT-n rows; corrections applied to the plan/statement BEFORE the Stage-A launch. [1 agent]
2. AGNOSTIC PROBLEM STATEMENT (`sreview_raws_2026-08-31/PROBLEM_STATEMENT_agnostic.md`) + machine lint (`lint_agnostic.py`, rejector seeded) -> E1.
3. STAGE A (Workflow `derive` + `diff`): 4 de-novo derivers (statement-only briefs, agnosticity lint on outputs) -> 8 diff judges -> classification CONFIRM-candidate / DIVERGENT / NEW with weight on the decisive comparison -> inline TRIAGE on file (cap 6).
4. STAGE B (Workflow `converge`) on the triaged items: agreed falsifier first -> advocate <-> refuter until-dry (dead = failure) -> independent judges -> CONFIRM (new reasons) / FLIP priced / PILOT pre-registered. Dual-seed refuter lot.
5. RED TEAM of the decisive number (parallel to 4).
6. VERIFY (Workflow `verify`): one verifier per verdict, files not summaries; dual-seed canary; unagreed-falsifier verdicts REJECTED.
7. LANDING inline: findings rows with `path:`, ledger status/note deltas with the authority chain to the VERDICT files, claims classes touched, D6/TWIN PROPOSED amendments (dated, DA RATIFICARE), tables E2/E3/E5, levers F1-F6, the ASSESSMENT with GO / NO-GO / GO-CON-PILOT.
8. R3 + R7: PROGRESS, lints (vii)(xv)(xix)(xx)(xxii)(xxiii)(xxiv), plain suite (never `-X utf8`), ADVISORY_INDEX, memory, closing refuter, commit by pathspec + hash micro-commit, HANDOFF to F2.REPR.

## SESSION LOG ENTRIES

## R8 AMENDMENT — USER ADDENDUM §G RECEIVED IN-SESSION (2026-09-05, before any Stage-A launch; appended to the carrier append-only as section G)

LEVEL 0 = THE ROAD (Q0 "how does one optimize an RDE nozzle") is added ABOVE
the paradigm level: Q1 (design on the cycle family beats design on the mean)
is OUR sharpening of Q0; Q2 (the truncated-plug head-to-head) is OUR decisive
experiment. Both are INCUMBENTS to be compared, never premises. Consequences
applied to the plan of this log (each traceable to §G items 1-5):
- §G.1 -> the agnostic statement is posed at Q0 (candidate objectives: mean
  Isp/thrust, envelope robustness, operability, cost; data classes A-G;
  constraints; certification requirement; budget) and the agnosticity lint
  gains a CONSTITUTION-TERM class (cycle-averaged, per-phase, TWIN,
  quasi-steady, plus the method names MoC/adjoint) — zero hits required in
  the statement. Exit criterion E1 reads through this.
- §G.2 -> Stage A gains sub-problem SP0 = the ROAD TREE for Q0 with at least
  roads (a)-(h) as listed in §G; per road: the question it really answers,
  cost to a credible answer, generality (sectors, data classes),
  falsifiability, time-to-number. The derivers' schema carries SP0 first.
- §G.3 -> a dedicated Stage-A diff judge for SP0 (the ROAD judge) reads M0
  Parts I-II, VI.4bis(ii), the [S-BLITE] block, D6 G3 :783, the
  [T-DISC]/[T-RED]/M-RED chain, C51/ROUTE-B, U3', TWIN §4 and answers three
  explicit questions: (i) is Q1 the right sharpening of Q0? (ii) does Q2
  answer Q0 or only Q1? (iii) must the representation rung (per-phase /
  O(St) / wave-frame) be chosen SEPARATELY for the designer and the
  evaluator? Judge count Stage A: 8 -> 9 calls (ceiling table amended:
  Stage A diff 9/9; totals ~52 / 67 calls; token ceiling unchanged 10M).
- §G.4 -> the ROAD is the DEFAULT load-bearing Stage-B item (slot 1 of the
  cap 6, priority over every other sub-problem if time runs short); its
  agreed falsifier is of the form "which measurement would make us change
  road"; the red team of the decisive number is extended from Q2 to Q0.
- §G.5 -> landing adds PROPOSED level-0 choice-ledger rows (optimization
  road; objective definition; decisive experiment; data class of the
  decisive test) DA RATIFICARE; the GO/NO-GO for F2.REPR/F2.ENGINE becomes
  CONDITIONAL on the road verdict: GO if our road is CONFIRM or is the
  PILOT-arm of a hybrid road; NO-GO/RE-PLAN if an alternative road
  dominates on credibility x cost with an agreed falsifier.
Consumer persona unchanged (JPP referee + PM); the referee now also asks
"why this road?". Order 1 (refuter on the carrier) runs on the carrier
INCLUDING §G.

## R8 AMENDMENT 2 — USER ADDENDUM §H RECEIVED IN-SESSION (2026-09-05, before the Stage-A launch; appended to the carrier as section H)

- §H.1 BRANCH LEDGER -> new deliverable `sreview_raws_2026-08-31/BRANCH_LEDGER.md`:
  every branch seen (road / choice / sub-branch) gets a row with status
  EXPANDED / PRUNED (reason) / DEFERRED (trigger + owner); "not analysed"
  does not exist. Depth criterion = value of information: a branch is
  expanded only if its resolution can CHANGE the GO/NO-GO or the road.
  Breadth complete at levels 0 (road) and 1 (sub-problems); depth where
  diff x weight justifies. The Stage-A judges emit candidate rows; the
  orchestrator owns the ledger (inline landing).
- §H.2 SCOPING NUMBER St -> a committed carrier with rejector
  (`validation/st_scoping_number.py`, arithmetic on RECORD data, no
  campaign): for the class-A family (wave count, D_CJ from the recorded
  Cantera chain, annulus radius, nozzle length, mean axial velocity)
  St = f_wave * L / u with a band over the envelope of the recorded
  parameters; consumes finding `problem-statement:st-marginal-numbers-
  uncarried` (path paper); declares which rung the number licenses
  (frozen-time / first-order unsteady corrector / wave-frame); the number
  is a MEASURED input of the level-0 ROAD item and of the red team. If
  St = O(1), the level-0 verdict must say that the frozen-time road alone
  is not defensible.
- §H.3 ADJACENT-FIELD SOTA PRIOR, diff phase only: each diff judge checks
  that the de-novo trees considered the SOTA of periodically unsteady
  flows (turbomachinery: steady rotating frame; frequency-domain
  harmonic-balance / time-spectral methods with adjoints) and of steady
  adjoint-based shape optimization; every such item enters as [KNOWLEDGE]
  -> literature census row with a procurement owner (litreview protocol),
  NEVER as evidence. The agnosticity lint stays on the statement and on
  the derivers' outputs only (the judges' briefs are NOT agnostic by
  design and are not linted).
Ceiling unchanged (the St carrier is orchestrator work, 0 agents).

### LOG-1 — §H.2 St SCOPING NUMBER carrier landed and executed (orchestrator work, 0 agents)
Carrier `validation/st_scoping_number.py` [X-STSC] (record arithmetic: matched cycle CH4/O2 20 atm of `data/st_nozzle_opt.json` with the record CJ solver re-run for U_CJ, annuli of record 140 mm / 45 mm, the S18 W* TOC contour of record, quasi-1D u with the rigorous-in-class bracket [L/u_e, L/a*]); run log `sreview_raws_2026-08-31/st_scoping_number_run.log`, EXIT 0, rejectors R1-R4 all REJECTED-as-required. MEASURED (2026-09-05):
- bell TOC (L = 4 yt), envelope over annuli x n in {1,2,3} x cycle T0: St_n in [0.153, 0.679]; at the RECORD head count (n = 3 at 10 kN, n = 2 at 600 N): St_n in [0.347, 0.599] -> MARGINAL: the first-order unsteady corrector is MANDATORY, wave-frame backstop (problem book §8 band, declared rule).
- PLUG class (L_ideal(1-trunc), trunc 0.20-0.40, R_lip ~ R_bar): St_n in [0.268, 1.415]; worst (n = 3, end-of-cycle T0, 20% truncation) St_n = 1.41 >= 1 -> on the decisive experiment's OWN sector the frozen-time rung ALONE IS NOT DEFENSIBLE at the record head count (wave-frame / unsteady rung required or the corrector must be shown to hold at St ~ 1). This number is the MEASURED input of the level-0 ROAD item and of the red team (§H.2 clause fulfilled: "se St risulta O(1), la strada per-fase da sola non è difendibile e la voce L0 lo deve dire").
- acoustic compactness He = f L / a_mean in [0.31, 1.39] (bell): the nozzle is NOT acoustically compact at the record head count.
Declared caveats: quasi-1D u (PRACTICE, bracket printed); wave speed = U_CJ (a velocity deficit LOWERS St, one-sided); plug lip radius ~ mean annulus radius; the certified-march tau_n stays the F2.ENGINE instrumentation upgrade. Registry landing at order 8: claims row [X-STSC] (kind carrier, env=cantera -> ondemand grammar extended, declared), finding problem-statement:st-marginal-numbers-uncarried -> DOWNGRADED with the residue named (certified-march tau_n + f-range citation).

### LOG-2 — Order 1 CONSUMED: refuter on the carrier (§A-G) + the log's opening declarations; repairs applied BEFORE the Stage-A launch
Refuter: 1 Fable agent, read-only, **237,086 subagent tokens, 39 tool uses, 17.7 min**; report `sreview_raws_2026-08-31/REFUTER_prompt.md` = 52 rows, **24 FAIL / 15 PASS / 13 NOTE**. Anchors and counts of the carrier and of this log are SOUND (PROMPT-4..8, 10, 40, 49, 50 PASS, re-measured by the refuter three ways). Defects = decidability, agnosticity-by-construction, ceiling feasibility, two phase/step facts. Disposition (every FAIL repaired or flagged; nothing silent):

**Applied before Stage A (blocking class):**
- PROMPT-28/44/37 statement: labels (C1)..(C7) -> (R-i)..(R-vii) consumer-level requirements only ("delta computed", "membership certificate and margin", "Verdict" DELETED — the certificate-first constitution is an incumbent, not a premise); class A = "generated from the specs by a model chain of the road's choosing"; configuration = input OR output, priced; admissible set = a compactness/regularity condition of the road's choosing; budget as a total (7-10 sessions); comparator left open ("why it is the strongest"); "is MARGINAL" replaced by the arithmetic range f·L/u ~ 0.05-5 with provenance. Re-lint after repairs: `lint_agnostic.py --statement` -> **0 hits PASS** on statement AND brief (measured 10:26). Drafts' pre-refuter timestamps declared (PROMPT-46): statement/lint 10:06-10:09, refuter report 10:23, repairs 10:24-10:26.
- PROMPT-43/41/39/11-14/22/15: deriver brief v2 = the refuter's neutral wording §D (SP0 = OPEN enumeration of strategies as TUPLES: objective; time treatment; spatial representation; solver + information; search + guarantee; decisive result — distinct = differs in >= 1 entry); the (a)-(h) list REMOVED from the deriver brief and moved to `COVERAGE_CHECKLIST_roads.md` (ROAD judge only, applied AFTER Stage A; seeded roads marked "orchestrator-seeded", weight reported separately); new sub-problems SP-OBJ, SP-PB, SP-CARM, SP-VAL (SP-VAL folded into SP9 "external anchor" in the brief, own judge merged with SP9); SP6 UN-MERGED from SP5 (own judge); SP2 gains state-constraint enforcement; SP7 pins return a MAGNITUDE with provenance, not yes/no; SP9 gains sensitivity to data weights + base model + generalization scope.
- PROMPT-27: the ROAD judge receives the pin table (COVERAGE_CHECKLIST §pins) and states per road which pins it needs / relaxes.
- PROMPT-36/31: SCOPE RULE (iv)/E5 RE-WORDED: in scope = "changes the credibility or the cost of answering Q0 by the road under review, including that road's own decisive experiment" (the level-0 item is in scope by construction).
- PROMPT-18/17/19/20/21/47/52: ceiling table v2 below (sub-ceilings per stage, degradation order, typed exit states, dual-seed shape, canary authorship, independent Stage-B judge persona); workflow scripts saved as versioned artifacts in `sreview_raws_2026-08-31/workflow_*.js` BEFORE each launch (F6), with the asserts named in the table.
- PROMPT-5: reading-range note: M0 :3197-3250 (G0 decision block + [DIR-THERMOTAB] pin :3242) read at 10:27 (LOG-2b).

**Pre-registered before Stage B (written here now, binding):**
- PROMPT-42 DOMINANCE CRITERION (verbatim from the refuter §B, adopted): for the road item the independent Stage-B judge scores every road R (incumbent I included) on two pre-declared scales, each score justified by a file anchor and contestable by the refuter: **CRED(R) in {0..5}** = number of the referee's five questions R can answer with a NAMED deliverable inside the remaining plan budget — (q1) external truth anchor; (q2) strongest classical opponent; (q3) uncertainty budget below the materiality threshold; (q4) reproducibility / version-stability of the certificate; (q5) generalization beyond n = 1. **COST(R)** = sessions-to-first-credible-number from record anchors (ISS-4 caps; measured precedents) with a declared band [lo, hi]. **R DOMINATES I iff** CRED(R) >= CRED(I) AND COST_hi(R) <= COST_lo(I) − 1 session AND at least one strict inequality AND R's agreed falsifier has NOT fired in Stage B AND the verifier confirms both scores from the files. Seeded rejector (scripted in the verify stage): a fictitious road with CRED equal and COST higher must NOT dominate; one with CRED+1 and COST_hi <= COST_lo(I) − 1 MUST dominate.
- PROMPT-38/32 EXHAUSTIVE GO MAP (adopted): incumbent CONFIRM (new reasons) or CONFIRM-with-repairs -> **GO**, NEXT = F2.REPR; incumbent = PILOT-arm of a hybrid tuple -> **GO-CON-PILOT** (pilot: one case, kill criterion, owner step, window, cost), NEXT = F2.REPR (pilot first act where named); alternative DOMINATES per the criterion with agreed falsifier and verifier PASS -> **NO-GO / RE-PLAN**, NEXT = RE-PLAN session (carrier written in this window; F2.REPR carrier SUSPENDED by dated note); alternative better on CRED or COST but not dominating, or dominance without agreed falsifier -> **GO-CON-PILOT** with the alternative as the pilot arm (kill criterion = the measurement named by its falsifier); road item UNSETTLED-AT-CAP / DEAD / verifier-REJECTED -> **PENDING-USER** (default if unanswered at close = GO-CON-PILOT, anti-meta cadence; never CONFIRM, never silent GO).
- PROMPT-30 E4 TWO-CLASS READING: every sub-problem carries EITHER a Stage-B verdict (selected items: agreed falsifier + independent verifier) OR the class **CONFIRM-BY-DIFF** (unverified: the diff judge's falsifier + an owner for the delta-sweep); the ASSESSMENT prints the two classes separately; CONFIRM-BY-DIFF is never quoted as CONFIRM. PROMPT-51: delta-sweeps of DECIDED rows are done INLINE by the diff judge (its brief says so).
- PROMPT-19 EXIT STATES per Stage-B item (typed field `new_objections:int` on every refuter round): **DRY** (0 new objections), **CAP** (3 refuter rounds, not dry) -> class UNSETTLED-AT-CAP mapping only to PILOT or PENDING-USER, never CONFIRM; **DEAD** (null / empty / missing typed field) = FAILURE, never a dry round. Script assert on the enum.

**Flagged PENDING-USER (not decided here; recorded in BLOCCATO B-SREVIEW at close):**
- PROMPT-1 **T0**: does S-REVIEW consume an F2 session (ISS-4 precedent: the G0/T2 review was COUNTED, D6 :160)? Provisional default per the plan's own precedent = COUNTED (F2.REPR would become "F2 session 3/6"); dated correction to the F2.REPR carrier once decided.
- PROMPT-24 **T2**: the carrier gives NO default -> PROVISIONAL (relevance scan with MAGNITUDES, the cheap branch), PENDING-USER; on NO the level-3 rows are dropped from the judges' outputs.
- PROMPT-23 **T1** relabelled: **CHANGED (INCREASED)**: 56 / 72 calls, 10M tokens vs the carrier's 5-8M; the F2-B0 ceiling overrun (5 agents vs 4 declared, F2B0 log :460-462) is PENDING-USER ratification (not this session's to grant).

**Record corrections queued for landing (order 8):** PROMPT-2 (B-SREVIEW is homed at F2.ENGINE by `CARRY_FORWARD` in the tool — the "BLOC override at F2.REPR" wording of this log's R2 and of the F2-B0 log R6 is FALSE as derived: landing = declared BLOC override B-SREVIEW -> F2.REPR in the tool + regeneration + lint (xxiv) + dated correction appended to the F2-B0 log); PROMPT-7 (C57/C60 quoted "MIXED" tokens normalized); PROMPT-9 baselines: **F1 ratio baseline = 15 meta sessions since 2026-08-13** (12 logs + 3 S-PRES sub-logs, measured by the refuter), **F6 KPI baseline = 1,276,374 tokens / ~34 verified corrections (~37k per correction)**; PROMPT-33 definition: **BUILD session** = its closing commit adds or re-stamps an executable carrier or engine code under validation/*.py, src/ or tools/*.py; META otherwise (this session is META even though it lands three tools + one carrier — declared, because its deliverable is a verdict); PROMPT-34 F4 re-scoped: the S-REVIEW deliverable = the REQUIREMENT text (M0-ready) + the PRE-REGISTERED cross-version protocol (design set, band, recorder pin, pass/fail rule, seeded rejector), owner F2.ENGINE first act — no run here; PROMPT-29 `check_tables.py` for E2/E3 (no empty cells, GAP ids resolve, owners present, seeded doctored table FAILS); PROMPT-10 map stale tally line -> owner F2.REPR first touch; PROMPT-3 gate authority level = PROGRESS/carrier, not D6 (a D6 note only PROPOSED if GO-CON-PILOT alters F2.REPR's ENTRY); PROMPT-45 red-team brief gains the uncertainty budget vs 1%, the n = 1 generalization scope, "is nozzle Isp the RDE lever at all", and the rule that every [KNOWLEDGE] claim entering a Stage-B verdict carries a literature-registry tier tag or is quoted UNVERIFIED (protocol H3).

**CEILING TABLE v2 (supersedes the R8 table above; in agent CALLS, expected / MAX, with token SUB-CEILINGS):**

| stage | calls exp / MAX | token sub-ceiling | script asserts / notes |
|---|---|---|---|
| order 1 refuter | 1 / 1 (CONSUMED: 237k) | 0.3M | — |
| A-derive: 4 de-novo derivers (lenses: variational/optimal-control; hyperbolic-PDE numerics; numerical-optimization/UQ; propulsion-test engineer) | 4 / 6 | 0.8M | output lint (ids/codenames) inline; leaked lens re-run once; null = DEAD logged |
| A-diff: 13 judges (SP0 ROAD, SP-OBJ, SP1, SP2, SP3, SP4, SP5, SP6, SP7, SP8, SP9+SP-VAL, SP-PB, SP-CARM) | 13 / 13 | 2.7M | typed classification enum; branch-ledger rows; [KNOWLEDGE] prior check (§H.3) |
| B-converge: cap 6 items (road = slot 1), advocate/refuter rounds | 24 / 36 | 4.3M | `assert rounds <= 3`; `new_objections:int` typed; DEAD = failure; exit enum DRY/CAP/DEAD |
| B dual-seed refuter lot (blind, same format) | 2 / 3 | (in 4.3M) | known-FALSE must be KILLED (2nd round if not), known-TRUE must survive |
| B judges (2, independent persona, never the SP0 diff persona; disagreement rate reported) | 2 / 2 | (in 4.3M) | dominance criterion scored with file anchors |
| red team of the decisive number (Q2 -> Q0) | 1 / 1 | 0.3M | mandatory questions per PROMPT-45 |
| verify: 1 verifier per Stage-B verdict + red team + 2 canaries (orchestrator-authored, blind) | 8 / 9 | 1.2M | reads FILES; unagreed-falsifier verdict = REJECTED; dominance rejector seeded |
| closing refuter | 1 / 1 | 0.4M | delta-audit vs E1-E6 |
| **TOTAL** | **56 / 72 calls (~44 roles)** | **10.0M HARD** | at each stage boundary: if running total + next sub-ceiling > 10.0M -> apply the DEGRADATION ORDER before asking: (1) verifiers 2-per-call for CONFIRM items; (2) cap 6 -> 5 -> 4 dropping lowest-weight items, never the road; (3) third rounds only for the road; only then STOP-and-ask |

### LOG-2b — reading-range closure (PROMPT-5): M0 :3197-3250 read at 10:27 (G0 decision block + A1 brick 1 + [DIR-THERMOTAB] pin :3242: Cantera sole production table generator; JAX engines read tables). No change to the plan.

### LOG-3 — Stage A launched; red team launched in parallel; §H.2 carrier landed in the registries (micro-commit); levers F3/F6 artifacts on file
- **Stage A DERIVE launched 10:31** as Workflow run `wf_83726ec6-3a7` (script versioned at `sreview_raws_2026-08-31/workflow_stageA_derive.js`; 4 derivers, lenses variational / hyperbolic / optimization / propulsion; brief = statement + deriver brief v2 only; typed return schema; null = DEAD logged). Diff script versioned at `workflow_stageA_diff.js`, judge roster (13) at `stageA_judges.json` (ROAD judge gets the coverage checklist + pin table + the three §G.3 questions; every judge does the §H.3 adjacent-field prior check and the inline delta-sweep of DECIDED rows).
- **RED TEAM of the decisive number launched 10:33** (1 Fable agent, brief `RED_TEAM_brief.md`: RT-1..RT-10 incl. the refuter's PROMPT-45 questions — uncertainty budget vs 1%, strongest opponent, external anchor, n = 1 generalization, "is nozzle Isp the lever", Q2 vs Q0, the St number on the plug sector, reproducibility, the negative outcome; output = proposed TWIN amendments DA RATIFICARE or CONFIRM with reasons).
- **[X-STSC] LANDED**: claims row (kind carrier, `env=cantera; pass=2026-09-05; suite=none; envfp=e100f996`; the ondemand grammar of `tests/test_claims_lint.py` extended with `cantera` — declared lint amendment, honest env naming), finding `problem-statement:st-marginal-numbers-uncarried` -> DOWNGRADED (severity low; carrier + residue: certified-march tau_n, f-range citation, deficit band; owner F2.ENGINE first march touch + P-1 claim gate). The closure-aware staleness gate refuses an UNCOMMITTED carrier ("no committed history") -> micro-commit **612c206** by pathspec (carrier + 2 registries + lint grammar), then lint (xv) **PASS 0 violations**, lint (xix) **PASS 262 entries / 210 open / 0 violations** (measured 10:38).
- Lever F3 artifacts: `tools/progress_counts.py` (PROGRESS ORA numbers by command; selftest PASS; output `sreview_raws_2026-08-31/progress_counts_open.txt`) and `tools/anchor_census.py` (MEASURED: **320 line-number anchors vs 1481 stable anchors** across registries/tools/core docs; **4 dead line anchors** after the resolver fix: findings registry cites `D25U_U3U4.md:61` and `conditionals.md:93` without the `rde_nozzle_` prefix (unresolvable as written), decision map cites `docs/rde_nozzle_PROGRESS.md:390` and `:395` = the PRE-slimming PROGRESS (121 lines today) -> genuinely dead; output `anchor_census_2026-09-05.txt`). Migration plan = ASSESSMENT lever F3.
- E2/E3 checker `check_tables.py` (PROMPT-29) PASS with seeded rejector after every GAP cell received an explicit owner.

### LOG-4 — Stage A DERIVE landed: 4/4 trees on file; agnosticity lint on outputs PASS (lint v2, refinement declared)
- Trees landed 10:41-10:43: `stageA_tree_variational.md`, `_hyperbolic.md`, `_optimization.md`, `_propulsion.md` (sizes in LOG-4b). Independence declarations in the structured returns (LOG-4b when the workflow result lands).
- Agnosticity lint on the four outputs: first run FAILED with 108 hits, ALL false positives of the lint itself (measured): the derivers' own strategy labels S1..S14 matched the session-name pattern `S\d`, the label `[RECOMMENDED]` matched the bracket-R id pattern, the public library names (Cantera, JAX, scipy) and the generic phrase "of record" matched CODENAME. Lint v2 (declared refinement, no leak class removed): bracket-R ids require a digit after R (repo forms [R22F-...]); session names only in the unambiguous forms `session S<n>` / `S<n>bis`; public libraries + "of record" allowed in OUTPUT mode only (still leaks in the STATEMENT mode). Selftest (dual seed) PASS after v2; statement + brief re-linted PASS; all four trees **0 hits PASS** (10:43). No tree names a repo id, codename, document, session or decision.

### LOG-4b — INDEPENDENCE CAVEAT OF RECORD (discovered from the hyperbolic deriver's declaration)
The hyperbolic tree's independence declaration (stageA_tree_hyperbolic.md :583-587) states: only the two brief files were opened, BUT "the harness injected a project memory summary into the system context without any action of mine; nothing from it was used". Reading: the harness auto-loads the project MEMORY INDEX (one-line-per-memory pointers, incl. session names and paradigm words) into every subagent launched in this project directory — a leak channel NOT of the deriver's making and NOT caught by the output lint (the outputs carry no repo ids: 0 hits). The other three derivers declared plain independence without mentioning the injection (they received the same system context). Consequence of record: Stage-A convergences are "independent MODULO the memory-index exposure"; every diff judge is instructed (script amended before launch) to classify a CONFIRM-candidate as DERIVED (argument present in the tree) vs merely NAMED, and the Stage-B refuters are told. Finding to mint at landing (method class, path non-critical, owner F6/orchestration): future de-novo derivers must run in a context WITHOUT the project memory index (e.g. a working directory outside the project path, or a harness option) — until then, the derived/named split is the mitigation. This caveat is printed in the ASSESSMENT §1 and §9.

### LOG-4c — Stage A DERIVE workflow CONSUMED (SR-9) and the level-0 headline
Workflow `wf_83726ec6-3a7`: 4 agents / 4 done / 0 dead / 0 empty; **465,831 subagent tokens, 24 tool uses, 16.0 min** (sub-ceiling 0.8M: under). Independence declarations: 3 plain ("only the two brief files were read"), 1 (hyperbolic) with the harness memory-index injection declared and non-use asserted (LOG-4b). Trees: variational 15 strategies / 12 sub-problems / 34 [KNOWLEDGE] claims; hyperbolic 14 / 12 / 42; optimization 14 / 12 / 26; propulsion 15 / 12 / 38. Load-bearing sub-problems flagged by >= 3 lenses: SP-OBJ, SP1, SP2, SP3, SP5, SP7, SP8, SP9, SP-CARM (SP4/SP6/SP-PB by 2-3).
HEADLINE (to be judged, not yet a verdict): **all four lenses rank a HYBRID first** — design loop on a cycle-weighted frozen-time (quasi-steady multipoint) axisymmetric engine with a discrete adjoint; EVALUATION of every competing design on an exact rotating-frame steady 3-D evaluator (each lens re-derives the time-independence of the thrust through an axisymmetric surface under the single-mode pin — the record's [T-T0]); a bracket/ceiling SCREEN first (ideal isentropic bound / Jensen screen / interface characteristic-count audit); a TUNED classical comparator (flux-consistent mean state, designer's sweep) as the strongest opponent; the reduction loss MEASURED (Omega-sweep) not assumed; both outcomes pre-registered. Variational: S0.4; optimization: S7 (with an L2 Jensen screen and a bound-only negative-result road as mandatory control); propulsion: H-1 (decisive test on bell AND fixed-base truncated plug, class B+F data, comparator = SP-CARM tuned design); hyperbolic: S11 "bracket-then-certify" (Stage-0 gate: characteristic-count audit, St / theta-hyperbolicity indicators, ceiling bound, loss budget of the tuned practice design on the exact evaluator). This coincides with the user's road (h) of §G.2 — the ROAD judge must say whether each tree DERIVES it (argument present) or NAMES it (memory-index exposure caveat).

### LOG-5 — INFRASTRUCTURE FAILURE of the diff run + relaunch on user order (SR-9 accounting)
- Diff workflow `wf_cca1f4cc-fa5` launched 10:46: **13/13 judges DEAD** within 52 s on the harness usage limit ("You've hit your session limit"), **0 outputs**, **877,009 subagent tokens consumed and LOST** (155 tool uses: the agents read the trees and record before dying). Per the model-pinned rule the orchestrator did not downgrade or retry silently; the user ordered at 10:49: "riprendi e se è crollato qualcosa, rilancialo, abbiamo di nuovo usage" -> relaunch (resume via scriptPath was refused by the tool's path check; the script is byte-identical, the run cache was empty, so a relaunch IS the resume). The lost 877k count against the diff sub-ceiling (2.7M) as a declared infrastructure loss; if the relaunch pushes the stage past 2.7M the degradation order applies at the NEXT stage boundary only.
- Red team: report `RED_TEAM_decisive_number.md` landed 10:49 (36 KB); the agent is finishing its return (alive at 10:49). Consumption in LOG-6 when its notification lands.

### LOG-6 — RED TEAM of the decisive number CONSUMED (order 6; Q2 -> Q0)
1 Fable agent, **274,420 subagent tokens, 50 tool uses, 19.4 min** (sub-ceiling 0.3M: under); report `sreview_raws_2026-08-31/RED_TEAM_decisive_number.md` (345 lines; RT-1..RT-10 each with the five mandatory fields; amendment table A-2..A-11, ALL PROPOSED / DA RATIFICARE, none applied; disclosure: one read-only `git status --porcelain` on the raws dir, no side effect, declared by the agent against the brief's "never run git" — accepted as harmless, recorded).
VERDICT: **AMEND** — the tuple (truncated plug / class A / per-phase vs classical / cycle-averaged Isp / thrust-stand band / both outcomes pre-registered) is CONFIRMED as the sector where the break theorem lives and no alternative dominates it under the pre-registered §B criterion; but AS WRITTEN the number is NOT referee-proof (CRED 1/5 by the red team's reading — only q4 answered; 5/5 reachable with A-2..A-9 at ~+1 session plus hours). Largest-effect amendments: **A-2 uncertainty budget BEFORE any run** (four of five band terms have no number on the decisive sector; base-pressure term alone = base force 5-12% of thrust x WG10 closure band 15-19% = 0.75-2.3% Isp = threshold-sized; a branch is quotable only if invariant under evaluation-only sweeps; a row without producer caps the outcome at INTERMEDIATE); **A-7 St discipline** ([X-STSC] St_n 0.73-1.41 on the plug at the record head count vs the program's own license rule; no J_1 exists; print St_n per arm, corrector mandatory at 0.5-1, refuse any rung-2 branch at St >= 1 without a wave-frame forward evaluation of both fixed designs or a declared re-pin); **A-3 arm C\*** (arm C at the mean state is a straw man: T4 says the plug wants the peak, the field's practice is already a cycle-averaged sweep — add the classical family's best-on-mu member at identical constraints; read the rule on delta*). Also: A-4 external anchors (arm-C cross-code via the RaoPlug fix or declared single-oracle; F2.CFD-2 as prediction-first field anchor; thrust-level anchor declared ABSENT with procurement path), A-5 second instance with predicted ordering, A-6 value stack + operability rows, A-8 reproducibility (hash set, both recorders, >= 2 starts), A-9 SMALL branch co-reported with the bound gap, A-10 Q0 embedding: TWIN as the plug-sector row of the two-sector tournament at the true c (+1-2 sessions, at the §8 ceiling — USER decision), A-11 provenance row + R-TWIN-7 plume certificate. RT-6: the TWIN answers Q1 (N2), not Q0; REPLACE not warranted because the two-sector tournament CONTAINS it (embedding, not replacement). RT-9: the SMALL branch is not publishable as written (argument from silence). RT-5: nozzle Isp is a lever at configuration scale (Paxson-Miki 58-71% of ideal; base ~12% of gross thrust), not demonstrably at the in-class contour scale where the TWIN lives. **The one question the record cannot answer today: the base pressure of a truncated plug under a rotating-detonation cycle** (no measurement anywhere; the only hot-fire source judges every classical closure inappropriate; closure moves the argmax by O(1)) — the sign of delta can be bracketed from inside the record (A-2) but not certified until a CTAP-class measurement on a truncated plug exists. Landing: amendments -> ASSESSMENT §4 + TWIN §9 PROPOSED block (dated, DA RATIFICARE); the red-team verdict gets its own verifier in the verify stage.

### LOG-6b — LITERATURE USE MEASURED (user question 11:00) and the Stage-B clause
Measured (grep of the agent transcripts for PDF Read calls): derivers 0/4 (by design — independence), diff judges 0/13 so far (brief points to the registry, not to the PDFs), red team 0 (used the harvests + registry depths; three primary sources quoted UNVERIFIED). Corpus on disk: 178 registry rows (52 READ-INTEGRAL / 33 READ-PARTIAL / 4 UNREAD / 80 WANTED; 169 with a path: literature/ 42 PDF, literature_review/ 26, GENO/literature 20). Correction applied BEFORE the Stage-B launch (user order): the Stage-B RULES block now binds advocates, refuters, judges and verifiers to check every LOAD-BEARING [KNOWLEDGE] claim on the PDF on disk when the registry has a path (page cited, litreview tiers [IO]/[REP]/[APERTO]) and to quote it UNVERIFIED with a procurement ask otherwise; the red-team verifier gets the explicit order to open the PDFs behind the three UNVERIFIED-at-primary sources; the judges' knowledge_rows become literature-registry rows with procurement owners at landing (§H.3).

### LOG-7 — Stage A DIFF CONSUMED (SR-9) + TRIAGE on file + the STAGE-B BOUNDARY RULE FIRES (user decision requested at 11:13)
- Diff run `wf_22e23154-f77` (relaunch): 13 agents, **12 structured returns + 1 error** (SP0 ROAD judge: its FILE `stageA_diff_SP0.md` is COMPLETE, 347 lines §0-§10; the typed index failed on a transient harness "Not logged in" error at the return step — the file is the authority, the index is not needed for triage); **3,696,889 subagent tokens, 552 tool uses, 19.4 min**. Literature use measured: 0 PDF reads by the judges (registry only) — LOG-6b clause binds Stage B.
- TRIAGE (rules pre-declared 10:59, table filled 11:11 in `TRIAGE.md`): 13 judges -> FULL-PANEL on SP0, SP1, SP2, SP4, SP5, SP7, SP8, SP9, SP-PB, SP-CARM; DELTA-SWEEP-ONLY / CONFIRM-BY-DIFF on SP-OBJ, SP3, SP6. Merges by object: SP1 + SP5(evaluator half) -> ROAD; SP2(base/plume) -> PB; SP9 + SP-CARM -> EXP. Selected (cap 6): **ROAD, EXP, PB, SEARCH (SP4 PILOT-CB), PROOF (SP8 A11/A9b), DATA (SP7)**; SP5's ladder census DEFERRED to its owner F2.REPR with three injections; SP3 = CONFIRM-BY-DIFF (the user's explicit adjoint question: the discrete AD-adjoint STANDS by diff; falsifier = whole-march primal-independent gradient test, pre-registered F2.ENGINE duty). Items file `stageB_items.json` (+ seeds XA/XB, canaries CANARY1/2, judges J1/J2 independent personas).
- Headline of the diff (to be judged in Stage B, not yet a verdict): the ROAD judge finds the hybrid (per-phase design loop + exact wave-frame evaluator of the decisive delta + screen first + tuned comparator) the **4/4 DERIVED top pick, not orchestrator-seeded** ("NONE of (a)-(h) was absent from the trees"); NO lens recommends road (b) as the stand-alone carrier of the decisive number; q1 PARTLY (Q1 right on the plug sector; not where operability is the lever), q2 "Q2 = Q1 on the plug; Q0 needs Q2 + screen + ceiling arm + the O-c branch", q3 YES (designer ≠ evaluator by construction, all four derived). SP4: the record has NO certified outcome-I optimum on any sector, so "the decisive test as posed measures the certification frontier of the search, not cycle vs mean" -> PILOT-CB pre-registration. SP8: the S22 base already shows a cross-triple cert_worst ratio 6.6 > K_RICH = 4 -> A-1's numeral questioned (F-1). SP-CARM: arm C at the mean state = single-author; design-phase sweep + bound screen proposed (A-CARM). SP-PB: p_b band protocol = precondition of quotability. SP7: four blind lenses derive the decisive answer on class B; class A = predictive extension with a MEASURED N3 price.
- **BOUNDARY RULE (LOG-2, pre-declared) FIRES**: consumed **5,551,235** subagent tokens (refuter 237k + derive 466k + red team 274k + diff dead 877k + diff live 3,697k); remaining under the 10.0M hard ceiling 4,449k; the pre-declared Stage-B shapes (6 items ~4 calls each + ROAD 6 + seeds; 2 judges; 5 verifiers; closing refuter) need ~6.69M -> projected **12.24M**. Degradation order applied on paper: cap 5 + rounds 2 (ROAD 3) -> 11.52M; cap 4 (ROAD, EXP, PB, PROOF) -> 10.80M; cap 3 (ROAD, EXP, PB) -> 9.93M (no margin). Even the full degradation order exceeds the ceiling unless the cap drops to 3 -> per the rule, STOP-AND-ASK: user decision requested 11:13 (options: raise the ceiling to ~12.5M and run the 6 items at rounds 2/ROAD 3; or cap 4 at ~10.8M; or cap 3 inside 10M). The Stage-B script now takes `max_rounds` / `road_rounds` as args (versioned copy updated).

### LOG-7b — user question at the boundary (11:16) folded into the ROAD item BEFORE launch
User: "ma se devo fare CFD, che senso ha fare adjoint per fase?" — answered on file (this log + the ROAD item): the evaluator is a STEADY 3-D solve in the wave frame (T0), used a few times, not a general unsteady CFD; the per-phase adjoint is the cheap SEARCH engine (hundreds of gradients) only if the argmax shift is measured small; the trees priced road (d) (3-D adjoint design) at 10-20 sessions assuming a pseudo-time FV solver, but the record's UNMEASURED claim that B-lite is helical space-marching "at marching cost" with a Lemma-B adjoint would promote road (d) above the hybrid and retire the per-phase adjoint to oracle/initializer. The ROAD item now carries this COST FORK as a second alternative with its measurement (one B-lite solve + adjoint vs K per-phase family solves on the record instance; the flipping K derived from the loop's gradient count; owner F2.REPR C51 / F2.ENGINE first act). Ceiling decision still PENDING-USER (11:13 question re-posed).

### LOG-7c — user question 2 at the boundary (11:19): "CFD with adjoint = mesh parametrization etc.?" — answered on file, folded into the ROAD item
Yes for a 3-D FV/DG adjoint road: mesh deformation/regeneration, mesh-sensitivity chain, adjoint consistency with mesh motion, non-differentiable shock capturing, plume + base pocket in the domain (the trees' 10-20-session tier; the 'adjoint in moving mesh' axis never adjudicated in the ledger). NOT for the record's B-lite helical space-marching (no volume mesh; the march generates its grid; adjoint by Lemma B) — but the 3-D unit process is UNBUILT and the march is illegal on the plug base pocket. The HYBRID avoids mesh adjoints entirely (the 3-D evaluator is adjoint-free, values only, a few times) — its main economic argument. The ROAD item now carries the three cost tiers explicitly; the agreed falsifier must separate them by measurement.

### LOG-8 — CEILING AMENDMENT (user decision 11:21) and Stage-B launch
User decision at the boundary (AskUserQuestion, 11:21): **"Alza il tetto a 12,5M, 6 voci"** -> hard ceiling 10.0M -> **12.5M subagent tokens** (T1 amended by the user, recorded; SR-9 reports against 12.5M from here), Stage B with the six items ROAD / EXP / PB / SEARCH / PROOF / DATA, refuter rounds capped at 2 for non-road items and 3 for ROAD (`max_rounds`/`road_rounds` args), verify = one verifier per judge file + 2 canaries + red-team verifier, closing refuter. Two user questions folded into the ROAD item before launch (LOG-7b cost fork; LOG-7c mesh/adjoint cost tiers). Script `workflow_stageB_converge.js` (versioned) amended so every agent READS its item definition from `stageB_items.json` (the file is the authority; args carry only ids/roles). Launch follows this entry.

### LOG-9 — Stage B LAUNCHED (11:24) + Stage-A extractions on file
- Stage B run `wf_83c30268-aeb` via scriptPath (versioned `workflow_stageB_converge.js`; the file needed CR-stripping — 99 CR bytes — before the harness accepted it; content otherwise identical), args: max_rounds 2 / road_rounds 3; items ROAD, PB, DATA, EXP, SEARCH, PROOF + seeds XA (known-FALSE) / XB (known-TRUE); judges J1 {ROAD, SEARCH, PROOF} / J2 {EXP, PB, DATA}; canaries CANARY1 (must CONFIRM) / CANARY2 (must REJECT). Every agent reads its item definition from `stageB_items.json` (authority) + the on-disk literature clause (LOG-6b).
- Extracted from the 12 structured judge returns (journal wf_22e23154-f77): `TRIAGE_measured.md` (per-SP incumbent class / panel recommendation / delta-sweep flag / verdict class counts / high-weight counts + the 77 adjacent-field prior checks), `KNOWLEDGE_rows_from_judges.md` (114 [KNOWLEDGE] rows with procurement owners — literature-census candidates, NEVER evidence), `BRANCH_LEDGER.md` (+299 rows from the judges; SP0's rows read from its file §8: EXPANDED 1-4, 9-18; PRUNED 5, 6, 7, 19, 20 + 3 named; DEFERRED 8, 17-coupling, S14, H S9). Measured: SP-OBJ 18 verdicts (11 CONFIRM-candidate), SP3 18 (9 CONFIRM-candidate, CONFIRM-BY-DIFF), SP6 22 (DELTA-SWEEP-ONLY), SP9 21 (6 DIVERGENT, 9 high-weight), SP-CARM 14 (3 DIVERGENT + 3 NEW, 6 high).
- The ROAD judge's pin table (§5): road (d)/(h)-evaluator need P-WAVE STRICTLY (the wave-frame lemma is VOID for counter-rotating pairs); road (b) needs P-WAVE + the O(St) corrector for its bar; road (a) needs none of the wave pins but answers a narrower question; road (f) relaxes P-WAVE to a mode measure. T2 relevance scan (PENDING-USER): P-WAVE BEARS on the decisive number through the evaluator's exactness; P-GAS bears on the absolute value (record [T-EQBR] +6.3..+7.0% ceiling) but second-order on the DIFFERENCE (SP7); P-DATA class A bears (four lenses derive class B; DATA item).

### LOG-9b — TIMESTAMP CORRECTION (SR-12; measured `date` at 18:37 and 18:39)
The entries LOG-7b, LOG-7c, LOG-8 and LOG-9 carry inferred times (11:16-11:24). MEASURED facts: the last clock read before the ceiling question was 11:11 (12/13 judge indices in the journal); the harness was then suspended on the usage/login limit (the diff's SP0 index failed on "Not logged in"; the limit message named a 3:20pm reset); the user's three answers (two questions + the ceiling decision "12,5M, 6 voci") arrived after the resume; the Stage-B script CR-strip is timestamped **18:35**, the Stage-B agents' meta files **18:36:09-10**, the first `date` after the resume **18:37**. So Stage B was LAUNCHED AT 18:36, not 11:24; the user's decision is dated 2026-09-05 (afternoon, exact minute not measured). Nothing else changes: all artifacts are on file and the run is alive (8 agents, transcripts growing at 18:39: 6 item advocates A0 + 2 seed refuters R1).

## LOG-10 — SAFE SUSPENSION CHECKPOINT (user order 2026-09-05 18:54: "interrompiamo tutto ora in maniera safe per riprendere un'altra volta"; executed 18:55)

STATE AT THE STOP (measured): Stage-B workflow `wf_83c30268-aeb` STOPPED at 18:55 with **12 cached agent results** in its journal; on disk: advocate positions A0 for ALL six items (ROAD, EXP, PB, DATA, SEARCH, PROOF), refuter round 1 for ROAD / EXP / PB (agreed falsifiers with amendments; kill = false on all three), both dual seeds COMPLETE (XA known-FALSE: KILLED on its agreed falsifier, 9 objections; XB known-TRUE: SURVIVED two rounds, kill = NO twice — the refuter's two error types are both measured as zero on the seeds), canaries CANARY1/2 on file (unverified: the verify phase did not run). NOT yet run: R1 for DATA / SEARCH / PROOF (killed in flight), round 2 (and 3 for ROAD), the two independent judges, the verifiers, the red-team verifier, the closing refuter, the landing (order 8), R3/R7.

HOW TO RESUME (resume-never-relaunch; the cached calls replay for free):
1. Open per R2 (START_HERE -> memory `s-sreview-checkpoint` -> this log LOG-1..LOG-10 -> `validation/sreview_raws_2026-08-31/TRIAGE.md` + `stageB_items.json` -> `docs/rde_nozzle_PROGRESS.md`); regenerate the roadmap + lint (xxiv).
2. Re-measure the counts (`python tools/progress_counts.py`) and the env fingerprint (must be e100f996, else declare drift).
3. Resume Stage B with EXACTLY: `Workflow({scriptPath: "validation/sreview_raws_2026-08-31/workflow_stageB_converge.js", resumeFromRunId: "wf_83c30268-aeb", args: <the JSON printed in LOG-9 / below>})` — args: `{"max_rounds": 2, "road_rounds": 3, "items": [{"id":"ROAD","seed":null},{"id":"PB","seed":null},{"id":"DATA","seed":null},{"id":"EXP","seed":null},{"id":"SEARCH","seed":null},{"id":"PROOF","seed":null},{"id":"XA","seed":"FALSE"},{"id":"XB","seed":"TRUE"}], "judges": [{"id":"J1","persona":"an applied-mathematics referee (PDE-constrained optimization, hyperbolic conservation laws, numerical certification) who has never seen the program's narrative, reads only the exchange files and the cited anchors, and scores the pre-registered dominance criterion with file anchors","item_ids":["ROAD","SEARCH","PROOF"]},{"id":"J2","persona":"a propulsion-journal associate editor who decides what gets published: quotability, uncertainty budgets, data classes, strongest comparator, base-pressure reality","item_ids":["EXP","PB","DATA"]}], "canaries": [{"id":"CANARY1","verdict_file":"validation/sreview_raws_2026-08-31/stageB_JUDGE_CANARY1.md","must":"CONFIRM"},{"id":"CANARY2","verdict_file":"validation/sreview_raws_2026-08-31/stageB_JUDGE_CANARY2.md","must":"REJECT"}]}`. The script and the items file must stay byte-identical for the cache to hit (do not edit them before the resume; the script has LF line endings — a CR re-introduction breaks the harness check). If the harness refuses the resume, a relaunch with the same script + args is the fallback (declare it; the six A0 files and three R1 files on disk are then INPUTS the new agents read — the script's advocate prompt writes A0 afresh only if the item has no A0: NOT implemented -> on a relaunch, pass the items whose A0 exist as seeds? NO: simplest honest fallback = relaunch everything and count the tokens as an infrastructure loss).
4. After the workflow completes: fill `TRIAGE.md` Stage-B columns, `ASSESSMENT_section3_draft.md` cells, ASSESSMENT §0/§1/§3/§6/§8/§9/§10; land the drafts on file: `findings_rows_DRAFT.yaml` -> `docs/findings_registry.yaml` (finalize statuses from the verdicts), `literature_wanted_rows_DRAFT.yaml` -> `docs/literature_registry.yaml`, `LEVEL0_ledger_rows_PROPOSED.md` / `D6_amendments_PROPOSED.md` / `TWIN_amendments_PROPOSED.md` = PROPOSED blocks (never applied), the index rows (already added at this checkpoint), PROGRESS ORA/NEXT/BLOCCATO/census, lints (vii)(xv)(xix)(xx)(xxii)(xxiii)(xxiv), plain suite (never `-X utf8`), closing refuter (delta-audit vs E1-E6), memory, commit by pathspec + hash micro-commit, HANDOFF to F2.REPR (or RE-PLAN on NO-GO).
5. Pending USER decisions to re-present at the resume: T0 (does S-REVIEW consume an F2 session counter; provisional COUNTED), T2 (level-3 relevance scan; provisional YES-as-scan), the F2-B0 ceiling overrun ratification (5 agents vs 4), P-D6-5 (two-sector tournament as critical-path override, +1-2 sessions), R9 cadence rule (P-D6-6), level-0 ledger rows C63-C66.

SR-9 AT THE CHECKPOINT: 5,551,235 subagent tokens measured before Stage B (order-1 refuter 237,086; A-derive 465,831; red team 274,420; A-diff dead run 877,009 LOST to the usage crash; A-diff live 3,696,889) + Stage B PARTIAL (12 calls cached; the stopped workflow reports no token total — to be read from its resume notification, which reports the cumulative usage). Ceiling of record: 12.5M (user amendment at the boundary). Agents so far: 4 derivers + 13 judges (x2 launches) + 1 refuter + 1 red team + 12 Stage-B calls.

PROVISIONAL READING (orchestrator, NOT a verdict; the judges have not sat): the foundations hold (T0/T3/T4, the certified class, the AD adjoint, the objective form, the spline geometry are all independently re-derived); the ROAD as the carrier of the decisive number needs an AMENDMENT (evaluator rung chosen separately; screen first; stronger comparator; St discipline) — the ROAD refuter's own round-1 reading is CONFIRM-WITH-REPAIRS -> GO with LEG A (bell, F2.M-RED) as the pilot's kill criterion and the plug-sector 3-D evaluator escalating only if the F6-class demonstrator is budgeted or the instance cannot be re-pinned below St_n = 1; no dominance either way on the pre-registered criterion. Likely E6 outcome: GO-CON-PILOT for F2.REPR and F2.ENGINE. Quotable only after Stage B + verify + closing refuter.

Checkpoint commit follows this entry (pathspec, never -A, never GENO/): session log, ASSESSMENT (IN AUTHORING), raws dir, carrier (§G/§H), tools (progress_counts, anchor_census, roadmap_derive BLOC override), regenerated roadmap, registries (prefix repairs, token normalization), decision map (MAP-AM-9), ADVISORY_INDEX rows, PROGRESS checkpoint.
