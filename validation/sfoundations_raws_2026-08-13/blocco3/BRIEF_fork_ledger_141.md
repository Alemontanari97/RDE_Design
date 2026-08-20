# BRIEF — FORK-SIDE LEDGER OF THE 141 PHASE-A FORKS
# S-FOUNDATIONS-C4 Blocco 2 item (1). Ratified Sonnet slot: MECHANICAL
# EXTRACTION ONLY — any judgment call is out of scope and must be
# flagged, never made. Launched concurrently with Blocco 1 (declared:
# file-disjoint, no content seam — inputs are the SETTLED trees/diff/
# ledger; Blocco-1 landings do not change fork->home identity).

## TASK
Produce the per-fork accounting that closes COVERAGE GATE category 4
(DE-NOVO FORKS; spec = validation/sfoundations_raws_2026-08-13/
COVERAGE_GATE_spec.md §(B)): one typed row per fork of the four
Phase-A condensed attack trees.

## INPUTS (read in full; cite by file:line)
- validation/sfoundations_raws_2026-08-13/phaseA_tree_variational_CONDENSED.md
- validation/sfoundations_raws_2026-08-13/phaseA_tree_hyperbolic_CONDENSED.md
- validation/sfoundations_raws_2026-08-13/phaseA_tree_optimization_CONDENSED.md
- validation/sfoundations_raws_2026-08-13/phaseA_tree_propulsion_CONDENSED.md
- validation/sfoundations_raws_2026-08-13/phaseB_tree_diff.md (the
  ledger-side assessment §§1-5; §5 = the ledger-verdict grouping)
- docs/choice_ledger.yaml (58 rows of record)
- docs/findings_registry.yaml (for homes that are findings rows)

## OUTPUT FILE (the only file you write)
validation/sfoundations_raws_2026-08-13/blocco3/FORK_LEDGER_141.md

One row per fork, markdown table(s) per tree, columns:
| fork-id | fork statement (one line, faithful compression) |
| disposition | anchor(s) |
- fork-id = <tree-letter><n> (V/H/O/P + the fork's number in its
  condensed table).
- disposition ∈ COVERED / PARTIAL / NOT-COVERED, per the coverage
  spec: COVERED(anchor) = the fork's question was adjudicated or
  consumed by the chain (diff §, choice-ledger row C<n>, registry
  row id, workflow verdict file); PARTIAL(named) = touched, missing
  half NAMED with owner+trigger already on record (cite the row that
  names it); NOT-COVERED = no home found by mechanical search.
- anchor(s) = the exact citations (file:line or row id).
- AMBIGUITY RULE (binding): where the mapping requires a judgment
  (two plausible homes, unclear whether an owner row covers the
  fork), do NOT decide: mark disposition AMBIGUOUS-FOR-FABLE and
  list the candidate anchors. Zero silent judgments.

## ARITHMETIC (rejector; at EOF, measured in your window)
- Per-tree fork counts measured from the condensed tables; expected
  total 141 (prior measurement 34+41+32+34 — if your count differs,
  REPORT the difference, do not force it).
- Tally: |forks| == COVERED + PARTIAL + NOT-COVERED +
  AMBIGUOUS-FOR-FABLE, per tree and total.
- MACHINE SUMMARY at EOF: counts per disposition per tree, list of
  NOT-COVERED ids, list of AMBIGUOUS-FOR-FABLE ids.

## RULES
Env pinned (no installs). Write only your output file. No number
without a measured command or a cited anchor. Faithful compression:
never paraphrase a fork into a different claim. Read-then-quote.
