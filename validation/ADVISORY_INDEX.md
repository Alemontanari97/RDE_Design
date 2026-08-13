# ADVISORY_INDEX — validation/ record-layer navigation (L7)

Session: S-ORDINE (census R32), T2 step S3. Date: 2026-08-13.
Built from `validation/sordine_raws_2026-08-13/inventory_seg3_advisories.md`,
`inventory_seg4_advisories.md`, `inventory_seg5_logs.md`,
`inventory_seg8_supplement.md` (per-file status adjudications, carried) and
`ADVISORY_SORDINE_plan_2026-08-13.md` §1/§2. This file is THE machine-checked
navigation layer for `validation/` (lint group (xx),
`tests/test_advisory_index.py`, coming): bijection files<->rows over every
validation-tree `.md` file, raws dirs as block rows.

## Purpose + plan-anchor navigation spine

`validation/` stays FLAT (index-not-move; supersession is a STATUS, not a
LOCATION). This index is the taxonomy that makes the flat directory
navigable without moving or renaming a single carrier/gate file. Every row's
`plan-anchor` cell answers "why does this file exist, and what does it feed"
via the navigation spine of record (P1-4/P2-3/P3-3 convergent, REF-20):

```
D6 phase / census row (NEED)
  -> registry or index row (TYPED OBJECT)
    -> of-record document (ADJUDICATION)
      -> carrier/gate (SOTA PROOF)
```

A row with no nameable D6-phase/census-row anchor is not silently absorbed:
its `plan-anchor` cell carries the literal token `ORPHAN-FLAGGED` plus the
best available nameable-need description, so the lint can count it and a
human can see it without reading the full file.

## Status enum of record (plan §2)

Core statuses (one per document; index row + in-file banner where
applicable):
- **OF-RECORD** — current authority for its content class; sub-tag
  `(living)` for files that legitimately mutate (PROGRESS, indices,
  registries).
- **SUPERSEDED-BY:\<path-or-id\>** — authority transferred; dated banner at
  head naming the successor; full text preserved.
- **CONSUMED** — order/prompt/dispatch fully executed; pointer to consumer
  required. Variant **CONSUMED-with-residue:\<pointer\>** when named rows
  remain live (consumption is per-row).
- **RAW** — agent working output whose adjudicated verdicts live in a judged
  advisory; never normative, never deleted; raws dirs indexed as block rows.
- **DERIVED** — regenerable by a named owner (not applicable to any `.md`
  row in this index; reserved for `.log`/`.pyc`/extract-class artifacts,
  which this index does not row-list per the S3 brief).
- **PENDING-CONTRACT** — live prompt for a future session (may not be
  archived or altered).
- **UNRESOLVED** — an honest state where a ratification/execution status is
  recorded nowhere. UNRESOLVED rows are session duties, never archive
  candidates.

Qualifiers (orthogonal, combinable): **LECTURE-ERA** (pre-program V&V
corpus, anchored to `repo-sota-standard`, not a D6 phase — still
OF-RECORD/frozen); **AT-RISK:\<ledger-id\>**; **UNTRACKED-SINGLE-COPY**.

## Tie-break of record

**This INDEX is authoritative for STATUS. The file itself is authoritative
for CONTENT.** Banner and index row are redundant by design (human-first /
machine-first); the coming lint checks agreement between them.

## Verification (measured fresh, this run, 2026-08-13)

- `ls validation/*.md` (fresh, not inherited): **90** files. Table rows
  below (excluding the 2 RAW block rows): **90**. Bijection: MATCH.
- `ls validation/sordine_raws_2026-08-13/ | wc -l` (fresh): **26** files ->
  block row.
- `ls validation/sota_gapmap_raws_2026-08-12/ | wc -l` (fresh): **17**
  files -> block row.
- Total table rows (90 file rows + 2 block rows): **92**.
- ORPHAN-FLAGGED rows: **1** (`ADR_panel_2026-07-16.md` — the one true
  orphan pending UD-4). Ratcheted 5 -> 1 on 2026-08-13 (literature-
  window handoff): `ADVISORY_moc_zucrow_fidelity` and
  `LEDGER_dubbi_moc` anchored to F2 rows, `ADVISORY_sota_definition`
  to S-CERT MC8, `ASSESSMENT_methodology_position` to P-1 positioning
  + S-CERT ingestion.
- Per-status tallies (90 file rows; corrected 2026-08-13 lint step:
  G5_pmm_toc_sweep re-filed CONSUMED -> OF-RECORD per its in-file
  "Status: RECORD"): OF-RECORD (incl. `(living)` and
  LECTURE-ERA-qualified variants) = **73**; CONSUMED = **9**;
  CONSUMED-with-residue = **2**; SUPERSEDED-BY = **1**;
  PENDING-CONTRACT = **2**; UNRESOLVED = **1**; RAW (`.md` rows) = **2**.
  73+9+2+1+2+1+2 = 90. MATCH.
  Block rows (RAW, not in the 90): **2**.
- LECTURE-ERA-qualified rows: **14** (the 2026-07-08/09/10 pre-program V&V
  corpus per `inventory_seg5_logs.md` §B; note the SORDINE plan's §0.2
  narrative figure of "17" does not reconcile against the segment-5
  inventory's own explicit tag list — flagged here per SR-12
  measure-before-stating rather than silently inherited; `interface_audit.md`
  predates the program by date but is filed CONSUMED, not LECTURE-ERA,
  matching the segment-5 table's own choice).
- UNTRACKED-SINGLE-COPY-qualified rows: **1**
  (`PROGRESS_2026-08-12_S24_f1b.md`, per plan §0.2 GT-1: the only one of
  the 27 pre-S-ORDINE session logs left untracked).

---

## Index table (sorted alphabetically; `file` relative to `validation/`)

| file | class | status | plan-anchor | note |
|---|---|---|---|---|
| ADR_panel_2026-07-16.md | advisory (ADR panel) | UNRESOLVED | ORPHAN-FLAGGED — pre-dates D6 phase spine; anchors repo-sota-standard + lecture-package/P-2 freeze lineage; nameable need = "lecture-package hardening + ADR pattern precedent" | UD-4 (user decision pending): ratified-in-practice vs still-pending; in-file ">>> OPEN QUESTION FOR USER" (600N headline 242.5 vs 245.3; truncation 0.20 vs 0.25-0.30) -> BLOCCATO row until user adjudicates |
| ADVISORY_S21_addendum_prompt_2026-08-11.md | session-prompt | CONSUMED | F0 order+instrumentation (plan v3); R4 pre-absorption correction duty | banner of record -> `PROGRESS_2026-08-11_S21_order.md`; full text preserved |
| ADVISORY_S21_prompt_2026-08-07.md | session-prompt | CONSUMED | F0 of plan v3 (D6); R2/R3 protocol instance | banner -> `PROGRESS_2026-08-11_S21_order.md` |
| ADVISORY_S24_DEbucket_panel_2026-08-12.md | advisory (panel verdict) | OF-RECORD | F1b (DEF twin, S24); [C-EQV2]; choice-adjudication-convergence directive | C1-C10 conditions landed in S24 M0 block; C7 refine-stage conditional still F2-live |
| ADVISORY_S24_sota_gapmap_2026-08-12.md | advisory (six-facet census, S25-REPAIRED) | OF-RECORD (living) | census R25/R26; R31 findings-as-code (largest seeding corpus, F2 first duty) | 36 GAP + 16 AC + 11 Q + 45-row choice-ledger annex; ~90-91 rows still unseeded into `findings_registry.yaml` |
| ADVISORY_S24_thermo_closure_survey_2026-08-12.md | advisory (survey + judge/refuter) | OF-RECORD | DIR-THERMOTAB; thermo-tabulated-backend directive; C-A/C-B/C-C owners F1b/F2 | C-A executed with M3 in S25; C-B/C-C open, full spec text only here |
| ADVISORY_S25_pipeline_impl_fidelity_2026-08-12.md | advisory (one-pass expert review) | OF-RECORD | R29 pipeline-sense directive, pair B first instance | corrigendum = `ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md` where they diverge (R6 wording) |
| ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md | advisory (Form-2 converged verdict) | OF-RECORD | R29 (convergence-mandatory 3-bis); [OBJ-DOM]/delta-carrier/[G1-DISC] F2-entry; Q3 F5-entry | authoritative wording where it diverges from the two one-pass reviews (impl-fidelity, sense-math) |
| ADVISORY_S25_pipeline_sense_math_2026-08-12.md | advisory (one-pass expert review) | OF-RECORD | R29 directive, pair A first instance; F2/F5 entry rows | corrigendum = CONVERGED file (R1-R3 adopted weakened, R4 refuted-and-repartitioned) |
| ADVISORY_S25_prompt_2026-08-12.md | session-prompt | CONSUMED | census R22/R25/R26/R30 window | banner -> `PROGRESS_2026-08-12_S25_speed.md` |
| ADVISORY_S25bis_diff_convergence_2026-08-12.md | advisory (Form-2 converged verdict) | OF-RECORD | R29 (perimeter review consumed); R31 registry dedup; F2-entry deferred rows | FLAG: execution status of repair list R1-R13 unverified by the seg3 reader against ea8143c/56baed1 (RF-1 staleness fact) — top NOTHING-LOST item for the loss-hunter |
| ADVISORY_S25bis_prompt_2026-08-12.md | session-prompt | CONSUMED | census R30, R28, R31, R25; BLOCCATO-8 | banner -> `PROGRESS_2026-08-12_S25bis_speed.md` |
| ADVISORY_SORDINE_plan_2026-08-13.md | advisory (Phase-4 fused-judge plan) | OF-RECORD | census R32 (S-ORDINE itself); successor of Phase-1/2/3 | THIS session's own execution plan; T2 (14-step S0-S13) in progress at the time of this row |
| ADVISORY_Fservice_Scert_prompt_2026-08-13.md | session-prompt (pending) | PENDING-CONTRACT | chain update of record (PROGRESS commit 1e188a9): F-SERVICE ratification window + S-CERT in one session with HARD BOUNDARY; wraps (never alters) the Scert contract | user-ratified 2026-08-13; scope pinned (D-01/C31/C30, R4 batch REV-3-adopted, 5 REFUTE_C carrier fixes under SR-11, named exclusions, A2 decision at boundary) |
| ADVISORY_Scert_prompt_2026-08-12.md | session-prompt (pending) | PENDING-CONTRACT | census R33; agnostic-milestone-review directive; sequenced R32 -> R33 -> F2 | may not be archived or altered; precondition "S-ORDINE CHIUSA" before it opens; ORDERED BY the Fservice_Scert wrapper prompt (2026-08-13) with opening hooks 2a-2e |
| ADVISORY_Scollapse_prompt_2026-08-11.md | session-prompt | CONSUMED | G2/T3/T0 theory line; parallel-session non-interference protocol | banner -> `ADVISORY_Scollapse_verdict_2026-08-11.md` |
| ADVISORY_Scollapse_verdict_2026-08-11.md | advisory (Form-2+Form-3 discharge-verified verdict) | OF-RECORD | M0 [T-T3-SI]/[T-T3-MAP]/[X-T3CTRL] registrations; carriers dispatched F2/F2a/F3/F5a/F5b/F6 | §6 M0/registry deltas EXECUTED 2026-08-11; §7/§8 clause register + open-items list authoritative only here |
| ADVISORY_Sgauntlet_generality_ledger_2026-08-11.md | advisory (horizontal gauntlet ledger + red-team + ratification appendix) | OF-RECORD | D6 §0-pre absorption addendum; user scope-pins memory; F2a/F3/F4b/F5a/F5b/F6 duty owners | delta-execution half CONSUMED 2026-08-11; 34-row ledger + DUTY texts + user pin verbatim text authoritative only here |
| ADVISORY_Sgauntlet_prompt_2026-08-11.md | session-prompt | CONSUMED | POST-S21 window census; claim-dual-proof-standard directive | banner -> `PROGRESS_2026-08-11_Sgauntlet.md` + `ADVISORY_Sgauntlet_generality_ledger_2026-08-11.md` |
| ADVISORY_Sordine_prompt_2026-08-12.md | session-prompt (active) | OF-RECORD (living) | census R32 (S-ORDINE); absorbs first duty of R31 | becomes CONSUMED at S-ORDINE closure; self-referential, session-owned, not yet banner-updated |
| ADVISORY_Sspeed_prompt_2026-08-12.md | session-prompt | CONSUMED | census rows feeding S25; G0/T2 review consumption | delivered `ADVISORY_engine_speed_audit_2026-08-12.md` + `DISPATCH_Sspeed_to_S25_2026-08-12.md` |
| ADVISORY_claims_to_code_2026-08-07.md | advisory (claims-to-code traceability table) | OF-RECORD | F0/S21 (P0 verifiers); F1b (C-3 twin); G1 gate (REQ-NONSTALL surrogate) | partially consumed (G1/C-1 landed S21, C-3 twin S24); C-4/C-5/C-6 open with owners — per-claim consumption map still due |
| ADVISORY_def_equivalence_panel_2026-08-07.md | advisory (panel verdict) | OF-RECORD | F1b DEF twin (S24); O1-O5 obligations; H-CLASS/EQ-v2 CONJECTURE row | red-team-corrected in place (RT-1..RT-6); THE authority for EQ-v2 wording; full hypothesis structure only here |
| ADVISORY_def_equivalence_proof_2026-08-07.md | advisory (hand proof of record) | OF-RECORD | S4 THEOREM in EQ-v2; (G) Lambda-form margin monitor; gamma-variable-generality directive | panel-verified, ratified at S21; GENO hygiene-caveat list unique here |
| ADVISORY_engine_speed_audit_2026-08-12.md | advisory (adjudicated plan of record) | CONSUMED-with-residue:self§N1-N8/DEAD-list/§7.2/§7.3-SOTA-survey/Q1-Q6 | census R22/R30 lineage; G0/T2 review row; sota-library-survey + orchestration-weight-sota directives | S25/S25-bis executed the plan to target-MET; standing rows not yet re-homed into a registry |
| ADVISORY_generality_litmap_2026-08-12.md | advisory (refuter-passed literature containment map) | OF-RECORD | memory generality-litmap-review; D2 litmap b0/b2; O3/F4b/F1b/P-1 duty owners D-A..D-F | 24 PDFs page-read; companion `DISPATCH_S24_generality_findings_2026-08-12.md` carries the S24-ingestion split; partially superseded-in-depth by `ADVISORY_litreview_confrontation_2026-08-13.md` (cross-file note not yet applied in either file) |
| ADVISORY_litmap_extension_2026-08-13.md | advisory (Form-1, 4 adversarial web auditors) | OF-RECORD | PB-2 novelty caveat; D2 gap G3; triggers `literature_review/` acquisition + litreview_confrontation | extends `ADVISORY_generality_litmap_2026-08-12.md` (105 queries, 2 near-miss; handoff 2026-08-13); partially superseded in depth by `literature_review/` + `ADVISORY_litreview_confrontation_2026-08-13.md`; RDE-nozzle-SOTA 2020-2026 census + Kraiko-school genealogy remain authoritative only here |
| ADVISORY_litreview_confrontation_2026-08-13.md | advisory (Form-2+ fused-judge verdict, REV3) | OF-RECORD | R4 retro-propagation (NOT yet discharged into M0/D-docs); R31 seeding (~101 unseeded objects); F2-entry rows (H-EXO, cone-form T7(c), R22 disentanglement) | CAVA NON RATIFICATA (handoff 2026-08-13): 39 grafts A1-A39 + 33 corrections C1-C33 + 29 residuals R1-R29; owner = F-SERVICE ratification window post-S-ORDINE/pre-S-CERT. 0 theorems falsified, 2 claims rewritten; §8 52 duties D-01..D-52 NONE verified executed |
| ADVISORY_mean_swirl_panel_2026-08-11.md | advisory (panel verdict) | OF-RECORD | F2a contract deltas (F-swirl-1/2, MASTER VI.1 CycleFamily); [T-SLRW]; POST-S21 census row | 3 mandatory F2a deltas un-absorbed (F2 not yet open); full spec home only here |
| ADVISORY_moc_zucrow_fidelity_2026-08-13.md | advisory (GENO-side MoC fidelity campaign) | OF-RECORD | F2 rows — the "engine <-> GENO <-> Zucrow triangulation" feeds the F2 general-engine window (anchor assigned per handoff 2026-08-13); [X-A1IM]/[X-TOCV] engine-fidelity carriers; moc-critical-independent-invariants memory | PARTIALLY CLOSED campaign state (R-1/R-2/R-4 closed, R-3 open pending an instrumented run; moved out of the status cell 2026-08-13, lint step — campaign state is note content, not a section-2 status); 28 MOC-01..28 findings + a new rank-2-of-3 dependence proof for Zucrow (16.43)/(16.44); P0 wall-thrust double-count measured on committed output; zero registry seeding; companion `LEDGER_dubbi_moc_2026-08-13.md` + a raw GENO-side patch (not `.md`, not row-listed here) |
| ADVISORY_plan_v2_draft_2026-08-07.md | advisory (plan draft) | SUPERSEDED-BY:ADVISORY_plan_v3_panel_2026-08-07.md | D6 plan-amendment lineage (v2 -> v3 -> S21 ratification) | banner of record (2026-08-13, S-ORDINE); front taxonomy verbatim carried into v3/D6 |
| ADVISORY_plan_v3_panel_2026-08-07.md | advisory (adjudicated plan of record) | OF-RECORD | D6 plan of record (F-phase spine); gates G0-G6 -> F mapping | normative content RATIFIED into D6 at S21; hypothesis-coverage map (~27 rows) richer than the D6 amendment summary — consult with `ADVISORY_redteam_2026-08-11.md` ISS list together |
| ADVISORY_rde_choking_2026-08-11.md | advisory (literature census + corrections of record) | OF-RECORD | T3-novelty support (P-1); U3' extraction contract (F2a/F5); F-swirl-1/2 flags; D6 literature-map misquote-fix duty | 5 primary sources page-anchored; misquote-of-record correction (Harroun); `VERIFICATION_FABLE` Stage-4 (seg8) revises 3 items here — propagation not yet applied |
| ADVISORY_redteam_2026-08-11.md | advisory (Form-3 red-team raw verdicts) | OF-RECORD | agentic-orchestration-forms standing rule (founding execution); S21 F0 ingestion row | RT-1..RT-6 absorbed in-place; plan-v3 ISS-1..ISS-6 + audit-refuted issues consumption UNEVEN, verify at T2 |
| ADVISORY_sota_definition_2026-08-13.md | advisory (methodology-definition rubric, v2) | PENDING-CONTRACT | S-CERT MC8 (plan-adherence meta-claim rubric input); claim-dual-proof-standard + agnostic-milestone-review directives (anchor assigned per handoff 2026-08-13) | DORMANT-DECLARED (handoff 2026-08-13): non-converged v2, never re-attacked; NOT citable as a metric. Refuter closed round 1 `converged: false`; operationally the methodology `ADVISORY_litreview_confrontation_2026-08-13.md` actually ran on, though never cited by it — a plan-adherence gap named by the seg8 reader |
| ADVISORY_use_case_interface_2026-08-07.md | advisory (use-case stress test + duties) | OF-RECORD | F5 entry (U1 owner); F2a (U2); F4b (U2 fitted option); D1 canonical consumption pattern | input to S21 F0 ratification (U1-U3 add to plan text + D1); ratification status to verify at T2; survey sources not page-verified |
| ASSESSMENT_methodology_position_2026-08-13.md | advisory (single-analyst methodology/SOTA-ness assessment) | OF-RECORD | P-1 positioning + S-CERT MC8 ingestion; G5 human-pass gate adjacency (anchor assigned per handoff 2026-08-13) | OF-RECORD; MANDATORY INGESTION by the next chain session BEFORE S-CERT (handoff 2026-08-13). Executive top-level verdict across the whole `literature_review/` campaign; un-cross-referenced by `ADVISORY_litreview_confrontation_2026-08-13.md` (loose end) |
| AUDIT_agnostic_2026-08-07.md | advisory (agnostic full-codebase audit, 277 KB) | OF-RECORD | F0 ingestion (plan v3 ABSORBS lists); R31 seeding (THE named first T2 duty); census P2-remainder duty | 94 findings (82 CONFIRMED/12 REFUTED); ~90-91 of 94 rows have NO registry row yet — THE R31 seeding backlog of record |
| DISPATCH_S24_generality_findings_2026-08-12.md | advisory (dispatch, converged-findings-only companion) | CONSUMED-with-residue:seg4§15(A3-Table2-exact-numbers,A5-jump-location-crosscheck-wording) | F1b/O3 adjudication (A2/A3); S24 DE-bucket cross-check (A5); D2 hygiene duties (A1/A4/A6) | S24 ingested at R3 (memory s24-f1b); full grounds live in `ADVISORY_generality_litmap_2026-08-12.md` |
| DISPATCH_Sspeed_to_S25_2026-08-12.md | advisory (dispatch, execution-order companion) | CONSUMED | S25 census placement row; G0/T2 review consumption | banner of record; content fully redundant with `ADVISORY_engine_speed_audit_2026-08-12.md` (declares itself the superseding authority) |
| G5_dispatch_email.md | doc-plan (dispatch) | OF-RECORD | F0/G5 (A0.5) | ready-to-send Italian ILL email for Kraiko 1979 + PMM DD; awaiting user send (BLOCCATO-side) |
| G5_kraiko_pmm_commission.md | doc-plan (commission) | OF-RECORD | F0/G5; D4 §3; D6 gate G5 | G5 human library-pass commissioning text of record |
| G5_pmm_toc_sweep_1957-1990.md | doc-record | OF-RECORD | F0/G5-2a | in-file "Status: RECORD (2026-07-16)"; the CONSUMED thing is commission Item 2a of `G5_kraiko_pmm_commission.md`, discharged BY this sweep — the sweep itself is the query-bounded deliverable of record; its reading list feeds Item 2b (still open human task). Status corrected CONSUMED -> OF-RECORD 2026-08-13 (S-ORDINE lint step, mirrors the in-file status) |
| INDEX.md | doc-index | OF-RECORD (living) | R3 audit trail; S-ORDINE R32 direct input | one-line index of all session logs, "never normative"; KEPT SEPARATE from this file per plan §1 CF-7 (this file remains authoritative for its own PROGRESS-log listing CONTENT; ADVISORY_INDEX governs repo-wide STATUS) |
| LEDGER_dubbi_moc_2026-08-13.md | advisory (companion doubt-tracking ledger) | OF-RECORD (living, open buckets B/D) | F2 rows — the executable-now doubts D1-D13 land in the F2/GENO coordination window (anchor assigned per handoff 2026-08-13); never-postpone-resolvables directive; same GENO-fidelity lineage as `ADVISORY_moc_zucrow_fidelity_2026-08-13.md` | 5 buckets (A closed-with-proof 9, B in-verification 11, C stopped 2, D executable-now 13, F retractions 2); F-R1/F-R2 retractions are LOAD-BEARING corrections that must travel with the moc-zucrow advisory |
| PANEL_topology_census_2026-07-22.md | advisory (panel deliverable, Round 2/2bis/2ter) | OF-RECORD | D2.1 [D-DOM]/D2.6 [D-P] amendment duties; F3 geometry classes; standing memory topology-census-pins | promotion via the S15-census-lemma session STILL QUEUED; formal-convergence criterion honestly UNMET; 11 CEN pins + user 2026-08-02 decisions authoritative only here |
| PROGRESS_2026-07-16_S4_G5venue.md | session-log | OF-RECORD | F0/G5(A0.5)+F1/P-2 venue; R3 | S4: G5 dispatch + P-2 venue decision (AIAA J primary) |
| PROGRESS_2026-07-16_fase0_OP0.md | session-log | OF-RECORD | F0/A0.3, OP-0; R3 | Fase-0 closure + OP-0 eps-ladder session |
| PROGRESS_2026-07-16_fase1_OP11.md | session-log | OF-RECORD | F1/OP-11-eps, F1/P-2, F0/G5; R3 | OP-11-eps phase diagram + P-2 outline + G5 commissioning |
| PROGRESS_2026-07-16_fase1_P1.md | session-log | OF-RECORD | F1/P-1, F1/P-2, F2-prep/G0; R3 | P-1 skeleton + P-2 Lemma A + G0 spike |
| PROGRESS_2026-07-16_fase1_S7.md | session-log | OF-RECORD | F1/P-2, F1/OP-0-gamma, F0/G5-2a; R3 | Lemma B + P-A1 + OP-0-gamma + G5-2a TOC sweep |
| PROGRESS_2026-07-16_fase1_S8.md | session-log | OF-RECORD | F1/P-1, F2-prep/G0; R3 | P-1 §2/§4 + G0 spike axisym extension + OP-0-gamma tail |
| PROGRESS_2026-07-16_rigore_G12.md | session-log | OF-RECORD | F1/G12-S1; R3 | Rigor S8: G12-S1 fitted-shock x-as-time attack |
| PROGRESS_2026-07-16_rigore_PA.md | session-log | OF-RECORD | F1/P-2 (P-A1/P-A2), F1/P3; R3 | Rigor S6: P-A1/P-A2/P3 discharge |
| PROGRESS_2026-07-17_S9_ordine.md | session-log | OF-RECORD | F1/SCAFFOLD-M, PIANO/D6; R3 | SCAFFOLD migration M-1..M-5; `claims_registry.yaml` born (80 entries) |
| PROGRESS_2026-07-17_fase2_S10.md | session-log | OF-RECORD | F2/G0, F1/P-1; R3 | G0 formal decision + GENO cross-code criterion + P-1 §5-§7 |
| PROGRESS_2026-07-20_fase2_S11.md | session-log | OF-RECORD | F2/A1 brick 1; R3 | A1 brick 1 (profile-generation machinery [X-A1IM]) |
| PROGRESS_2026-07-21_S12_rigoreR4.md | session-log | OF-RECORD | R4 rule itself; F4-prep/T3QS, F2-prep/A5, PIANO/D6 | R4 back-prop of the review conversation (T3-QS, D-GSEP, S-BLITE, GV row) |
| PROGRESS_2026-07-21_S13_leads.md | session-log | OF-RECORD | F0-coda/D2 leads, G6/G14, D4 §3; R3 | literature page-verify; Kraiko-Osipov 1970 read in full, D4 contingency adjudicated |
| PROGRESS_2026-07-22_S14_panel.md | session-log | OF-RECORD | PIANO/panel (D7-class); memory s14-panel-verdict; R3 | reading-queue completion + 16-persona convergent panel (D8 of record) |
| PROGRESS_2026-08-04_S15_fondazioni.md | session-log | OF-RECORD | RIGOR/A campaign (s15-foundations-campaign); R3 | deep-foundations tranche 1 (T-SLRW/T-XWALL/T-XWS/U1/U2/X-IVXC, ledger p1) |
| PROGRESS_2026-08-06_S16_fondazioni2.md | session-log | OF-RECORD | RIGOR/A-B; C-D25U, C-MAJDA/U3-H1; R3 | foundations tranche 2 (U3+U4, S-ACFR, S-GBE, S-LBML, ledger p2) |
| PROGRESS_2026-08-06_S17_brick2.md | session-log | OF-RECORD | F2/A1 brick 2 (D6 item 9); R3 | brick-2 re-adjudication + kickoff ([X-TOCV], DIR-RKG, X-SCANM, X-LSG0, X-THC1) |
| PROGRESS_2026-08-06_S18_brick2run.md | session-log | OF-RECORD | F2/A1 brick 2 closure, T2a gate; R3 | production levers P1-P4 + end-to-end run — BRICK 2 CLOSED, O3.3 unlocked |
| PROGRESS_2026-08-06_S19_o33.md | session-log | OF-RECORD | F1/P-2 oracles O3.2/O3.3; [C-O33]; R3 | campaign O3.2/O3.3 (bench PASS, C-O33 quantified) |
| PROGRESS_2026-08-07_S20_adaptive.md | session-log | OF-RECORD | F1/P-2 + F2/A1 ([C-O33] discharge attempt); R3 | adaptive knot class [X-AKNO], certifiability-boundary crawl, tier-ladder formalization |
| PROGRESS_2026-08-11_S21_order.md | session-log | OF-RECORD | F0 of plan v3; R3 | F0 order+instrumentation (ratification, P0 rejectors, [X-CDKAT]/[X-VMON] armed) |
| PROGRESS_2026-08-11_S22_governor.md | session-log | OF-RECORD | F1 of plan v3; R3 | F1 governor [X-MGOV] + [X-LOCD] retro-diagnosis + decisive campaign A' + O4 discharge |
| PROGRESS_2026-08-11_S23_f1close.md | session-log | OF-RECORD | F1 close; R3 | F1 early-close decision, P-2 dated freeze, [X-TBAK] DUTY-6(i), C1 conditional |
| PROGRESS_2026-08-11_Sgauntlet.md | session-log | OF-RECORD | Standing directive claim-dual-proof; `ADVISORY_Sgauntlet_prompt_2026-08-11.md`; R3 | parallel adversarial generality-ledger session (advisory-pattern, path-limited) |
| PROGRESS_2026-08-12_S24_f1b.md | session-log | OF-RECORD, UNTRACKED-SINGLE-COPY | F1b of plan v3; R3 | F1b DEF twin falsifier [X-DEFTW] executed, EQ-v2 adjudication, DE-bucket — the one session log among the pre-S-ORDINE 27 that is still untracked (plan §0.2 GT-1) |
| PROGRESS_2026-08-12_S25_speed.md | session-log | OF-RECORD | Census R30-prep / S-SPEED dispatch; F-SERVICE; R3 | C4-first + engine speed M-CHAIN (M0-M5ab), [X-SPDB] |
| PROGRESS_2026-08-12_S25bis_speed.md | session-log | OF-RECORD | Census R30/R31; F-SERVICE; R3 | M5c/M6/H3/H4 + GAP-29 + notaknot twin + findings registry; STEP 15 = the convergence map (named input of THIS S-ORDINE session) |
| PROGRESS_2026-08-13_Sordine.md | session-log (live) | OF-RECORD (living) | R3 (session closure/continuity discipline); census R32 | THE live S-ORDINE session log; restart map for a session-limit death; this session owns it — structure-only row per task brief |
| README.md | doc-index | OF-RECORD, LECTURE-ERA | repo-sota-standard; top-level README badges | frozen-reports contract for lecture-era validation (regenerate into `data/`, never overwrite here) |
| REPO_VV.md | doc-validation | OF-RECORD, LECTURE-ERA | repo-sota-standard | adversarial V&V of the repo as a teaching/design tool (2026-07-10, verdict PROMOSSA) |
| SOTA_AUDIT.md | doc-audit | OF-RECORD, LECTURE-ERA | repo-sota-standard | two adversarial multi-agent audits: 490 claims/518 verdicts + 8 design exercises |
| VALIDATION.md | doc-validation | OF-RECORD, LECTURE-ERA | repo-sota-standard | lecture-era 3-pillar validation report (33 CJ checks vs Caltech DB/CEA) |
| bell_optimality_proof.md | doc-theory | OF-RECORD, LECTURE-ERA | repo-sota-standard; cited context for M0 "bell~0 in-hypothesis" correction | formal optimality theorems for area-ratio in the Stechmann model |
| cycles_validation.md | doc-validation | OF-RECORD, LECTURE-ERA | repo-sota-standard | W-S cycles V&V, 99/99 PASS |
| dof_audit.md | doc-audit | OF-RECORD, LECTURE-ERA | repo-sota-standard (ancestor of R5 numeric discipline) | DOF/input provenance audit ("no magic parameter hides") |
| gamma_audit.md | doc-audit | OF-RECORD, LECTURE-ERA | repo-sota-standard | gamma frozen-vs-equilibrium audit of SK/Stechmann thrust models |
| gamma_phase_audit.md | doc-audit | OF-RECORD, LECTURE-ERA | repo-sota-standard | per-phase gamma audit of W-S cycles (round 2, complements gamma_audit) |
| interface_audit.md | doc-audit | CONSUMED | repo-sota-standard | banner of record (2026-08-13, S-ORDINE) -> `src/common/`; pre-refactor AS-IS interface/convention snapshot (git a986717) kept as frozen provenance. Date added to this row 2026-08-13 (lint step, mirrors the in-file banner) |
| q_formal.md | doc-theory | OF-RECORD, LECTURE-ERA | repo-sota-standard | formal definition/verification of q (standard-state anchored) |
| s25bis_refute_diff.md | raw-agent-output | RAW | R30; claim-dual-proof-standard directive; pipeline-sense R29 | S25-bis dedicated adversarial refutation of commits 1806ae2/18b4e0f; verdicts absorbed in the S25-bis session log |
| s25bis_sense_perimeter.md | raw-agent-output | RAW | Standing directive pipeline-sense-expert-review (R29); choice-adjudication-convergence | S25-bis perimeter sense-review (R29 expert adjudication of each choice); verdicts absorbed in the S25-bis session log/registry |
| sdt_official_audit.md | doc-audit | OF-RECORD, LECTURE-ERA | repo-sota-standard | official Caltech SDToolbox zip vs vendored stack audit |
| sdt_thrust_demos.md | doc-audit | OF-RECORD, LECTURE-ERA | repo-sota-standard | SDT official impulse demos vs course thrust models census |
| **sordine_raws_2026-08-13/** (block row) | raw-block | RAW | census R32 (S-ORDINE) | RAW block: 26 files, adjudicated verdicts live in `ADVISORY_SORDINE_plan_2026-08-13.md` (+ this session's own synthesis) |
| **sota_gapmap_raws_2026-08-12/** (block row) | raw-block | RAW | census R26 (gap-map) / R29 (pipeline-sense) | RAW block: 17 files, adjudicated verdicts live in `ADVISORY_S24_sota_gapmap_2026-08-12.md` + `ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md` |
| st_opt_validation.md | doc-validation | OF-RECORD, LECTURE-ERA | repo-sota-standard | Stechmann Table 1 nozzle-optimization validation |
| vv_thrust.md | doc-validation | OF-RECORD, LECTURE-ERA | repo-sota-standard | analytical thrust models V&V (PH/axial/Stechmann, 16 cases) |
