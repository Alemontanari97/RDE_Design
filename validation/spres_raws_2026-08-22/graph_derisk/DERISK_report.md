# S-PRES W-A slot A6 — WALKABLE-GRAPH DE-RISK REPORT (G-9, emend. v2.1 §6a)

**Consumption arc (artifact-connectedness):** (1) deck authoring — the
graph build script of the deck pipeline consumes `extract_graph.py` +
`pipeline_graph.json` as the asserted node/edge source (GRAPH_VIZ_SPEC
RENDER MECHANISM: extracted, never hand-typed); (2) storyboard v3 —
visual-feasibility verdicts below (stage-name pt budget, Stage-6 panel
split, L0 composition) bind the L0/L1 slide plans.
**Comparison stage:** `docs/rde_nozzle_pipeline_decision_map.md`
(refereed, 0 BREAK / 0 REPAIR) + `GRAPH_VIZ_SPEC.md`.
Window: 2026-08-23. Env: PINNED (nothing installed; matplotlib 3.10.8
already present, verified `python -c "import matplotlib"`).

## 1. Measured counts (SR-12 — commands run THIS window)

| Quantity | Measured | Command (this window) | Record |
|---|---|---|---|
| Stages | 8 | `grep -c '^## STAGE' docs/rde_nozzle_pipeline_decision_map.md` = 8; parser agrees | 8 (spec + machine summary) — CONFIRMED |
| Ledger nodes | 62 = 61 stage-table rows + C46 (note_C46, deliberately not stage-placed) | `python validation/spres_raws_2026-08-22/graph_derisk/extract_graph.py` (prints the measurement); independent: `grep -c "^- id: C" docs/choice_ledger.yaml` = 62 | 62 — CONFIRMED |
| Non-ledger nodes | 17, roster set-matched vs machine summary | same script (assert A5/A6) | **"17" CONFIRMED against the source**: the map's §10 machine summary states `nonledger_nodes: 17` with the exact roster; parser measures the same 17 from the ⊘ table rows. No discrepancy. |
| Edge entries | 45 (44 edges + 1 declared anti-edge E34; E33/E37/E40 absent by design) | `grep -c '^- E' docs/rde_nozzle_pipeline_decision_map.md` = 45; parser id-set-matches §9 vs §10 roster | 45 — CONFIRMED |
| Cluster surfaces | 4 (A engine, B contract, C ship-gate, D external expansion) | same script (assert A12) | 4 (spec L0) — CONFIRMED |
| Status tally | 12 DECIDED / 36 MIXED / 12 NEVER / 2 SA, per-id rosters matched | same script (asserts A14/A15) | CONFIRMED |
| Dual-stage-face nodes | C55 (St.1+7), R22-CFD (St.2+8), counted once | same script (assert A13) | as declared in machine summary — CONFIRMED |

## 2. Asserts: 18/18 PASS

`extract_graph.py` run of record (pinned env, exit 0): A1 stages=8 ·
A2 table-ledger=61 · A3 ledger=62 · A4 id set exactly C1..C62 ·
A5/A6 non-ledger 17 + roster match · A7 nodes_total 79 · A8 edges 45 ·
A9 edge-id roster match · A10 E34 = the single anti-edge · A11
E33/E37/E40 absent · A12 surfaces=4 · A13 dual-face {C55, R22-CFD} ·
A14 tally 12/36/12/2 · A15×4 per-status id rosters vs machine summary.
Every assert compares MEASURED (tables/§9) vs the map's OWN §10
machine summary vs the record constants — a map edit breaks the build
on any of the three legs. Output: `pipeline_graph.json` (79 nodes, 45
edges, 4 surfaces, per-stage tallies; committed beside this report).

## 3. Discrepancies found (spec vs source — for the spec owner)

1. **Spec's "Stage 6 has 20 ledger nodes" is WRONG: measured 24**
   (C31 C60 C57 C58 C48 C16 C32 C33 C34 C35 C36 C37 C39 C40 C27 C29
   C30 C62 + design-basis C1-C8; parser per-stage output of record).
   The spec's prescribed 2-panel split (engine-core vs design-basis
   C1-C8) yields **16 + 8**, and 16 > the spec's own ≤12-cards-per-
   slide rule. Consequence for authoring: Stage 6 L1 needs **3 panels**
   (e.g. engine cluster+driver 8-9 / numerics-tolerances 7-8 /
   design-basis C1-C8) or a tighter sub-clustering; the spec line
   "Stage 6 has 20 ledger nodes -> split into 2 panels" must be
   amended. (The "17" the mandate flagged, by contrast, checks out.)
2. **C46 is count-bearing but not stage-placed** (map padding policy,
   note_C46). Any L0 render that sums per-stage counts shows 61, not
   62 — the prototype carries an explicit footnote; the deck must too
   (or the map owner stage-places C46 at Stage 6).

## 4. Layout risks measured on the L0 prototype (render_L0_prototype.png, 1920×1080)

- **P1 (main risk) — the 20 pt stage-name floor is INFEASIBLE with 8
  equal-width boxes on 16:9.** Box width = 1.42 in; auto-fit measured
  (script prints it): Stage 2 "REPRESENTATION" and Stage 4
  "CERTIFICATES & QUALIFICATION" fit only at **9 pt**; St.7 11 pt;
  St.3/5/6 14 pt; St.1 15 pt; St.8 18 pt. Options for storyboard v3:
  (a) short display names ≤10 chars/line with full names spoken/in
  subtitle, (b) two-row ribbon 4+4 (breaks the left-to-right pipeline
  read), (c) drop per-box subtitles and widen boxes (gap −30% buys
  ~1 pt). Recommendation: (a) — keeps the ribbon, meets 20 pt.
- **P2 — Stage 7 has ZERO ledger nodes** (5 ⊘ + the C55 second face):
  its status mini-bar is empty and the L0 "honesty" encoding goes
  silent exactly on the honesty stage. Authoring should render ⊘
  statuses (LANDED/ARMED/...) as a neutral grey bar or count badge.
- **P3 — single-stage cluster arcs (B, C, D) degenerate**: an arc over
  one box reads as decoration, and D's label collides with the frame
  edge at Stage 8 (fixed in prototype by edge-clamping). Consider
  brackets/tinted halos for B/C/D and reserve the arc for A (4↔6).
- **P4 — count-line overflow at Stage 8**: "1 scelte + 4 ⊘ (+R22-CFD)"
  touches the box edge; dual-face annotations need a compact glyph
  (e.g. a small "2-faces" chain icon) instead of inline text.
- Color-blind pairing: shape channel (square/half/circle/diamond)
  still to be implemented in the mini-bars — bars currently encode by
  color+fill only; L1 node cards must carry the shape glyphs.

## 5. What remains for authoring (not de-risked here)

- L1 stage-zoom template (node cards, in-stage edges, stub arrows with
  target-stage numbers) and the Stage-6 3-panel decision (see §3.1).
- L2 node cards: populate from `pipeline_graph.json`
  choice/conditions/open_duty fields for the Q&A-mapped nodes
  (verbatim-compressed ≤40 words/field — fields are longer than that
  in the JSON: compression is an authoring step, cite-only).
- MIXED half-fill and NEVER owner-window tags in the L0 mini-bar
  (prototype uses solid amber / plain open box).
- Integration into the build_deck.py pipeline (assert-on-build wiring;
  the extractor is already assert-gated and ready to be imported).
- E9/E28/E29 long-range edges: not drawn at L0 (spec draws surfaces
  only) — L1 stub-labeling must carry them.

Files: `extract_graph.py` (stdlib-only parser + 18 asserts),
`pipeline_graph.json` (extracted graph of record),
`render_L0_prototype.py`, `render_L0_prototype.png` (1920×1080).
