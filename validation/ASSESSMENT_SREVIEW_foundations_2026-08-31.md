# ASSESSMENT OF RECORD — S-REVIEW: agnostic review of the FOUNDATIONS at the F2-entry milestone (EXECUTED 2026-09-05 on the carrier dated 2026-08-31)

> STATUS: IN AUTHORING — §0, §1, §3 (Stage-B cells), §6, §8-§10 are filled from the Stage-B VERDICT + VERIFY files at landing; nothing here is quotable until the closing refuter's delta-audit is logged in `validation/PROGRESS_2026-08-31_Sreview.md`. Every claim below cites its file; the files under `validation/sreview_raws_2026-08-31/` are the authority.

Consumer (R8): the JPP referee who will judge the decisive number ("why not X?"; "why this road?") + the PM ("is this the shortest credible path?"). Downstream consumer: the F2.REPR session (carrier `validation/ADVISORY_F2REPR_prompt_2026-08-31.md`), which opens ONLY on GO / GO-CON-PILOT.

Comparison stage: F2-B0 close (commits 4798713/127dfdd; ledger 62 = 12 DECIDED / 38 MIXED / 10 NEVER / 2 SINGLE-AUTHOR; OPEN 210 = 48 critical / 118 / 44; BLOCCATO 22 [3 critical]; measured at open by `tools/progress_counts.py`). Consumption arc: this assessment -> F2.REPR (GO/NO-GO + representation frame + the evaluator-role branch) -> F2.ENGINE -> F2.M-RED -> F2.CFD-2 -> F3.* -> F3.TWIN; on NO-GO -> a RE-PLAN session.

Method of record (SR-9 detail in §9): order-1 refuter on the carrier (24 FAIL repaired/flagged) -> agnostic problem statement at level Q0 (lint PASS, 0 hits) -> measured St carrier -> 4 de-novo derivers (statement-only briefs; independence caveat §9) -> 13 record-aware diff judges -> triage on file -> Stage B (agreed falsifier first; advocate <-> refuter; independent judges; verifiers; dual-seed + canaries) -> red team of the decisive number -> this landing.

## 0. VERDICT (E6) — filled last

| gate | verdict | conditioning road outcome | NEXT |
|---|---|---|---|
| F2.REPR | (pending Stage B) | (pending) | (pending) |
| F2.ENGINE | (pending Stage B) | (pending) | (pending) |

## 1. Level 0 — THE ROAD (Q0): the three questions (§G.3), the dominance scoring, the verdict

(filled from `stageA_diff_SP0.md`, `stageB_ROAD_*.md`, `stageB_JUDGE_J1.md`, `stageB_VERIFY_*.md`; the pre-registered dominance criterion and GO map are in the session log LOG-2.)

Facts already of record from Stage A (`stageA_diff_SP0.md`): all four blind lenses DERIVE the wave-frame steadification ([T-T0]) and rank the SAME road first — a HYBRID whose design loop is the per-phase axisymmetric engine and whose EVALUATOR of the decisive delta is the exact steady rotating-frame 3-D field, with a bracket/ceiling screen before any optimizer runs and a tuned classical comparator; the ROAD judge classifies it as the 4/4 DERIVED top pick, NOT orchestrator-seeded ("NONE of (a)-(h) was absent from the trees"). No lens recommends road (b) as the stand-alone carrier of the decisive number (V rank 2, H rank 3 "must be paired with an exact evaluator", O rank 4, P rank 5). Three questions: (q1) PARTLY — Q1 is the right sharpening ON the plug sector where the collapse theorem does not decide, not where operability is the lever; (q2) Q2 = Q1 on the plug; Q0 needs Q2 + the screen + the ceiling arm + the O-c branch; (q3) YES — designer rung ≠ evaluator rung, all four derived. The user's two questions at the boundary (cost fork per-phase adjoint vs designing directly on the 3-D march; mesh/adjoint cost tiers) are inside the ROAD item's agreed falsifier (session log LOG-7b/7c).

## 2. The measured scoping number St ([X-STSC]) and what it licenses

Carrier `validation/st_scoping_number.py` (committed 612c206; claims row [X-STSC], env=cantera; run log `sreview_raws_2026-08-31/st_scoping_number_run.log`; rejectors R1-R4 fire). Record arithmetic only: matched cycle CH4/O2 at 20 atm (φ 1.66 and 1.00; U_CJ 2655 / 2439 m/s from the record's own CJ solver, PR/TCJ/gamma reproducing the cache to ≤ 3e-4), annuli of record 140 mm (10 kN example, A_t 32.4 cm², ~3 heads) and 45 mm (600 N workhorse, A_t 4.3 cm², ~2 heads), the S18 W* TOC contour of record (L = 4 throat radii, ε = 4) with a quasi-1D isentropic velocity (PRACTICE) bracketed rigorously by [L/u_e, L/a*], T0 at the two extremes of the blowdown; plug class via L_ideal(1 − trunc), trunc 0.20-0.40.

| class | St_n envelope (n ∈ {1,2,3} × cycle T0) | at the record head count | license (declared rule = problem book §8 band) |
|---|---|---|---|
| bell TOC | 0.153-0.679 | 0.347-0.599 | MARGINAL: first-order corrector MANDATORY; wave-frame backstop |
| truncated plug | 0.268-1.415 | 0.73-1.41 (worst n = 3, end-of-cycle T0, 20% truncation) | NOT DEFENSIBLE alone at St ≥ 1: wave-frame / unsteady rung required or a declared re-pin |
| acoustic compactness He | 0.31-1.39 (bell) | — | the nozzle is NOT compact at the record head count |

Declared caveats: quasi-1D u; wave speed = U_CJ (a deficit LOWERS St, one-sided); R_lip ≈ R̄ for the plug; certified-march τ_n = the F2.ENGINE upgrade (finding `problem-statement:st-marginal-numbers-uncarried` DOWNGRADED with this carrier). Consequence of record: on the decisive sector the frozen-time rung ALONE is not defensible at the record head count — this converts the evaluator-rung question (q3) from a preference into an obligation and is the measured input of the ROAD item and of the red team (RT-7 / amendment A-7).

## 3. Level 1 — sub-problem verdicts (E4, two classes)

See `sreview_raws_2026-08-31/ASSESSMENT_section3_draft.md` (merged here at landing): Stage-B VERDICT class = ROAD (SP0 + SP1 + SP5-evaluator), EXP (SP9 + SP-CARM), PB (SP-PB + SP2 cluster), SEARCH (SP4), PROOF (SP8), DATA (SP7); CONFIRM-BY-DIFF class = SP-OBJ (objective form; Stage-0 screen as a NEW landing duty), SP3 (the discrete AD-adjoint STANDS — the user's explicit question; falsifier = whole-march primal-independent gradient test), SP6 (control-polygon migration direction stands), SP2/C49 (fitted march stands); DEFERRED = SP5's ladder census to F2.REPR with three injections.

## 4. Red team of the decisive number (Q2 -> Q0): proposed TWIN amendments DA RATIFICARE

`sreview_raws_2026-08-31/RED_TEAM_decisive_number.md` (RT-1..RT-10; verdict **AMEND**): the tuple (truncated plug / class A / per-phase vs classical / cycle-averaged Isp / thrust-stand band / both outcomes) is CONFIRMED as the arena of the break theorem and no alternative dominates it under the pre-registered criterion; AS WRITTEN the number is NOT referee-proof (CRED 1/5: only q4). Amendments A-2..A-11 (table copied to `TWIN_amendments_PROPOSED.md`, none applied): uncertainty budget BEFORE any run (the base-pressure term alone = 0.75-2.3% Isp, threshold-sized; a row without producer caps the outcome at INTERMEDIATE); arm C* = the classical family's best-on-mu member (the mean-state arm is a straw man: T4 says the plug wants the peak; the field already sweeps); St discipline per arm; external anchors (arm-C cross-code; F2.CFD-2 prediction-first; thrust-level anchor declared ABSENT); second instance with predicted ordering; value stack + operability rows; reproducibility hash set + both recorders + ≥ 2 starts; SMALL branch co-reported with the bound gap; Q0 embedding as the plug-sector row of the two-sector tournament (+1-2 sessions, at the budget ceiling — USER decision); provenance row + plume certificate. The one question the record cannot answer today: the base pressure of a truncated plug under a rotating-detonation cycle (no measurement exists anywhere; the closure moves the argmax by O(1)). Verifier of the red team: (pending, verify stage).

## 5. Tables E2 (base hypotheses by stage) and E3 (completeness by stage)

`sreview_raws_2026-08-31/TABLE_E2_hypotheses_by_stage.md` (27 rows: every hypothesis with class, falsifier, carrier or GAP with owner; four NEW level-0 rows) and `TABLE_E3_completeness_by_stage.md` (10 stage rows: built / proven / measured / missing today / missing for the decisive number, each with owner); checker `check_tables.py` PASS with the seeded rejector (doctored table REJECTED).

## 6. Rabbit-hole census (E5) and the BRANCH LEDGER (§H.1)

`sreview_raws_2026-08-31/BRANCH_LEDGER.md`: 9 orchestrator rows (levels 0-1) + 299 rows from the 12 structured judge returns + SP0's rows (file §8); every branch EXPANDED / PRUNED (reason) / DEFERRED (trigger + owner). Rabbit-hole census (filled at landing with the Stage-B outcomes): each entry states the boundary, the alternative frame and how it changes the credibility or cost of answering Q0.

## 7. Levers F1-F6 (carrier §F)

`sreview_raws_2026-08-31/LEVERS_F1-F6_draft.md`: F1 cadence rule R9 PROPOSAL (baseline 15 META sessions since 2026-08-13, 0 BUILD); F2 minimum viable engine (M1-M8 + the deferrable generality: the three-family stratified march is NOT on the class-A path); F3 anchors-by-id (MEASURED 318-321 line anchors vs 1481 stable; 4 dead repaired; `tools/anchor_census.py`, `tools/progress_counts.py` in place; migration plan); F4 [CERT-STAB] requirement + pre-registered cross-version protocol (the SP8 judge's text supersedes the draft; Stage-B PROOF verdict pending); F5 priced engineering table; F6 orchestration (independent judges, versioned workflows with asserts, dual-seed + canaries, KPI).

## 8. Proposed level-0 choice-ledger rows and D6 / TWIN amendments (DA RATIFICARE — nothing applied)

`LEVEL0_ledger_rows_PROPOSED.md` (C63 road / C64 objective / C65 decisive experiment / C66 data class), `D6_amendments_PROPOSED.md` (P-D6-1..8), `TWIN_amendments_PROPOSED.md` (A-2..A-11 + the Stage-B additions). Status cells filled at landing.

## 9. Orchestration report (SR-9), independence caveat, dual-seed canaries

(filled at landing; running total before Stage B = 5,551,235 subagent tokens incl. 877,009 lost to the usage crash; ceiling amended by the user to 12.5M at the Stage-B boundary.) Independence caveat of record: the harness auto-loads the project memory index into every subagent's context (LOG-4b); outputs carry no repo ids; judges graded DERIVED vs NAMED. Literature use measured: 0 PDF reads by derivers (by design), judges and red team (registry only); the Stage-B roles are bound to the on-disk PDFs (LOG-6b).

## 10. HANDOFF to F2.REPR (or RE-PLAN)

(filled at landing.)
