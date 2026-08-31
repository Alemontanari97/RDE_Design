# START HERE — rde-lecture-code / RDE nozzle program (read FIRST, every session)

**Objective (one line):** a formally optimal, certified cycle-averaged nozzle design
methodology for RDEs; decisive number = the head-to-head TWIN (per-phase design vs
classical design on I4 at identical constraints, truncated plug, ~1% Isp stop rule).
Critical path = `docs/ROADMAP_critical_path.md` (DERIVED by `tools/roadmap_derive.py`,
lint (xxiv); never hand-edited — no "path complete" claim is citable without its PASS).

## Where things live (layer map of record: `docs/rde_nozzle_SCAFFOLD.md` §1/§6)
| what | where | note |
|---|---|---|
| Rules of work (R1-R8) | `CLAUDE.md` | R2 opening order, R3/R7 closing, R8 gate-first |
| Theory of record (M0) | `docs/rde_nozzle_MASTER.md` | wins over every other doc; proofs Part III, implementation Part VI, map Part VII |
| Depth by topic (D1-D8) | `docs/rde_nozzle_{problem_book,literature_map,theorem_ledger,claims_verdict,general_scheme_panel,development_plan,pipeline_audit,panel_2026-07-22}.md` | D6 = WORK index (phases F0-F6, gates G0-G6) |
| Pipeline decision map | `docs/rde_nozzle_pipeline_decision_map.md` | cite-only navigation, 79 nodes / 45 edges |
| Atlas (13 chapters) | `docs/atlas/` (`ATLAS_TREE.md` = walk) | indexed BY OBJECT; D6 is indexed BY PHASE — the roadmap tool is the join |
| Typed registries (lint-gated) | `docs/claims_registry.yaml` (xv), `findings_registry.yaml` (xix, `path:` triage), `choice_ledger.yaml` (xix-f), `literature_registry.yaml` (xxii), `glossary.yaml` (xxiii), `flag_registry.yaml` (xx) | the INDEX of the truth; content lives in the cited docs |
| Living state | `docs/rde_nozzle_PROGRESS.md` (ORA table / NEXT / BLOCCATO table / census R1-R38) | history verbatim in `docs/rde_nozzle_PROGRESS_ARCHIVE.md` (append-only) |
| Validation record layer | `validation/` flat; `validation/ADVISORY_INDEX.md` (xx) | advisories, panels, session logs `PROGRESS_<date>_*.md`, raws dirs |
| Suite + lints | `tests/run_all.py` (groups i-xxiv) | a claim without a committed script + rejector is not a number (R5) |
| Papers | `docs/rde_nozzle_P1_skeleton.md` + P1_sections_*, `docs/rde_nozzle_P2_*`, `docs/paper/P1_outline.md` | G5 human pass before ANY submission |
| Memory (harness) | `~/.claude/projects/.../memory/` (`MEMORY.md` index) | recall = background; structure wins over recall |
| GENO | `GENO/` independent repo, READ-ONLY here | never `git add` it; its health = BLOCCATO B-GENO |

## The six standing directives (memory files carry the why/how)
1. **navigation-first** — answer from registries/index/glossary, never from recall; absence claims only search-proven.
2. **claim-dual-proof** — every claim = theoretical counter-proof at convergence + implemented case with rejectors.
3. **doubts-to-convergence** — every doubt investigated to convergence; "undecidable statically" only with a named, scheduled experiment.
4. **never-postpone-resolvables** — postponing is legitimate only if structurally gated (owner + trigger named); cheap = now.
5. **model-pinned** — Fable everywhere; never change model without a user order; on quota limit STOP and ask.
6. **R8 gate-first** (CLAUDE.md) — every session opens by declaring consumer, exit criteria, orchestration ceiling; closes with measured counts.

## The query command
```
python tools/record_query.py "<regex>" [--kind md|yaml|all] [--max N]   # path:line | anchor | class | text
python tools/record_query.py --manifest                                # fixed manifest resolves? (lint xxiv)
python tools/roadmap_derive.py                                          # regenerate the derived roadmap
python tests/run_all.py --fast                                          # lints + fast tier
```
Opening protocol (R2): this file → memory → M0 (depth) → PROGRESS → D6 → ROADMAP (regenerated) → declare phase + step.
