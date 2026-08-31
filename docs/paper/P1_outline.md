# P-1 OUTLINE — skeleton only (S-ROADMAP U7, 2026-08-31; no prose here)

Status: OUTLINE OF RECORD for the assembly pass of P-1 (target venue JPP,
D6 §3). It does NOT supersede `docs/rde_nozzle_P1_skeleton.md` (claim map
C1-C26, acceptance rules (a)-(e)) nor the full-text sections of record
(`rde_nozzle_P1_sections_2_4.md`, `_5_7.md`, `_1_3_8_9.md`); it is the
JOIN paper-section -> atlas chapter -> registries -> carriers that the
assembly pass and the referee persona consume. Every row cites; nothing
is asserted here.

**Consumer (declared, CONSECUTIO D1 rule):** the JPP REFEREE persona —
an RDE propulsion reviewer who asks "which of your 'proven' are
theorems, which number is measured, what is the falsifier" — exact
persona, one listener per wave, delta-audit never full repeats.

## Conventions binding on every draft pass
- **Theorem-status scale L1/L2/L3** (HARVEST_LOTB_S4 H-1, refuter-passed
  98 rows, zero upgrades): L1 "proven (hypotheses stated)" = THEOREM;
  L2 "proven, within stated limits" = THEOREM*; L3 "proof laid out,
  completion in progress" = SCHEMA. Ceiling = the class in the claims
  registry; "provably" only at >= L2; identical wording wherever the
  stamp appears.
- **Numbers rule** (HARVEST H-4 + CONSECUTIO D5): every number travels
  with (i) the exact quantity (e.g. optimum AREA RATIO, not "the
  optimum"), (ii) its scope (rung, cases, bench with rejector),
  (iii) its caveat (Humphreys: mobile argmax at flat value = pattern,
  not the general case). Magnitude + scope + caveat, or no number.
- **Novelty = query-bounded** (guard 9 of the S-PRES guard checklist;
  D4 §3 contingency Kraiko-Osipov 1970 armed; lineage pin H-2: "closest"
  belongs to the Fievisohn/wave-frame line, K-O 1970 = "the ancestor we
  always cite"). No "first" without the query list and the near-misses
  (Kraiko-Tillyaeva 2015, ISABE-2003-117, Levin-Manuilovich-Markov 2010).
- **Gate G5** (Kraiko 1979 / PMM human pass) before SUBMISSION, never
  before the writing (D6:289; BLOCCATO B-G5).
- **Evidence-stage tag** on every engine-level claim (findings row
  `claims:engine-level-staged-evidence-hierarchy-missing`, P34): V0
  verification / per-champion validation / pre-registered prediction.
- **Public adequacy claims** stay GATED (D-44; forchetta = bracket with
  provenance, never demonstrated adequacy) until the TWIN + M-RED numbers
  exist (ROADMAP steps F2.M-RED, F3.TWIN).

## Section map (paper section -> atlas chapter -> registries -> carriers)
| § | section (skeleton title) | atlas chapter(s) | registry objects (ids) | carriers / data of record |
|---|---|---|---|---|
| 1 | Introduction: the periodic-feed nozzle problem; practice = average-then-design | CH1 formulation ladder; CH5 literature positioning; LINEAGE_LEDGER | lit registry rows (Rao 1958 IAC abstract-bounded; K-O 1970; Fievisohn line); findings `methodology:lineage-recognition-gap` | — (expository; every historical claim cited per D2) |
| 2 | Formulation: interface contract, measure, cycle-averaged functional (P) | CH10 data contract; CH7 averaging edifice; CH2 | claims T-T0 (L1), [S-T0P]/[T-T0P-E], D2.x definitions; choice C59 (temporal form canonical-inside-the-pin) | full text of record `P1_sections_2_4.md` §2 |
| 3 | Exact steadification + collapse dichotomy (T3/T4), swirl boundary N6 | CH2 averaged optimality; CH7 | T3/T4 theorems (class per registry), [T-T3-SI]/[T-T3-MAP], [T-N6-2]/[T-N6-3] | suite groups (vi)/(x)/(xii); T3-CONTROL protocol |
| 4 | Per-phase structure: quotient, fiber separation, reduction residual | CH3 reduction physics; CH7 | [T-DISC], [T-RED], [R22F-FORCHETTA] (bracket, not adequacy), OPTSHIFT (SCHEMA-licensed only) | M-RED campaign (F2, pre-registered both-outcomes) — numbers NOT yet of record |
| 5 | Optimality system + certification (adjoint bridge, certificates, bands) | CH9 certification; CH4 machine choices | P-2 Lemma A/B ids, [X-O33B]/[X-O32], NTF block, CLG, C11/C9 estimator rows | full text `P1_sections_5_7.md` §5; O3.1 dot-product carriers |
| 6 | Bound ladder, phase diagram, real-thermo route | CH6 value honesty | OP-0 ladder ids, [T-EQBR], eps*_real group (xii) | `src/thrust/bounds.py`, `data/bounds_ladder.*`, phase-diagram carriers |
| 7 | Results: certified quasi-1D instances; in-class datum +0.51% (with class caveat); the TWIN slot | CH6; CH8 design space | F1b [X-DEFTW] datum (recorded-consistent, not re-executable: findings `provenance:f7-design-vector-irrecoverable`); TWIN = ROADMAP F3.TWIN (EMPTY until executed) | s24_deftw_* artifacts; twin protocol (F2-B0 pre-registration) |
| 8 | Containment bridges (EAP, S-H), related work, lineage | CH5; CH_REF | litmap rows; findings `litreview:residue-r1-r2…` (blocks further novelty strengthening) | `P1_sections_1_3_8_9.md` §8 |
| 9 | Limits, declared industrial gaps (RK-E no experimental anchor; RK-F compute), outlook | CH6 §7; D6 §7 risk register | findings `atlas:flight-context-coverage-gap`, DUTY rows F5/F6 | — |
| A | Appendices A1-A7: proof imports from M0 (one location per proof) | — | claims registry `proof:` anchors | M0 Part III |

## Claim gate before submission (checklist, all machine-checkable)
1. Every claim id in the text resolves in `docs/claims_registry.yaml` (lint xv orphans).
2. Every number has a carrier row (suite group or persisted data) — R5.
3. `path: paper` findings consumed one by one (44 rows at 2026-08-31, `python tools/record_query.py "path: paper" --kind yaml`).
4. Consumption trace of the draft (TRACE method of S-PRES: claim -> anchor -> class) with the referee persona as listener.
5. G5 pass recorded in PROGRESS BLOCCATO B-G5.
