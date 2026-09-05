// S-REVIEW Stage A — DIFF (versioned artifact; 2026-09-05). args = { trees: [file paths], judges: [ {id,title,brief_extra} ] }
export const meta = {
  name: 'sreview-stageA-diff',
  description: 'S-REVIEW Stage A diff: one judge per sub-problem classifies the de-novo trees vs the record (CONFIRM-candidate / DIVERGENT / NEW) with weight on Q0',
  phases: [{ title: 'Diff', detail: '13 diff judges (SP0 ROAD, SP-OBJ, SP1..SP9(+VAL), SP-PB, SP-CARM), record-aware, files written by the agents' }],
}
const RAWS = 'validation/sreview_raws_2026-08-31'
const TREES = args.trees
const JUDGES = args.judges
const SCHEMA = {
  type: 'object',
  required: ['subproblem', 'file_written', 'incumbent_summary', 'incumbent_adjudication_class', 'verdicts', 'panel_recommendation', 'proposed_falsifier', 'branch_ledger_rows', 'adjacent_field_prior_check', 'knowledge_rows', 'delta_sweep_done'],
  properties: {
    subproblem: { type: 'string' },
    file_written: { type: 'string' },
    incumbent_summary: { type: 'string' },
    incumbent_adjudication_class: { type: 'string', enum: ['DECIDED-genuine-advocate', 'DECIDED-constructional', 'MIXED', 'SINGLE-AUTHOR', 'NEVER', 'DECLARED-AXIOLOGY', 'NO-ROW'] },
    verdicts: { type: 'array', items: { type: 'object',
      required: ['approach', 'from_lenses', 'classification', 'weight_on_Q0', 'weight_reason', 'changes_credibility_or_cost', 'record_anchor'],
      properties: {
        approach: { type: 'string' }, from_lenses: { type: 'array', items: { type: 'string' } },
        classification: { type: 'string', enum: ['CONFIRM-candidate', 'CONFIRM-candidate-NAMED', 'DIVERGENT', 'NEW', 'ORCHESTRATOR-SEEDED'] },
        weight_on_Q0: { type: 'string', enum: ['high', 'medium', 'low', 'zero'] },
        weight_reason: { type: 'string' }, changes_credibility_or_cost: { type: 'string' }, record_anchor: { type: 'string' } } } },
    panel_recommendation: { type: 'string', enum: ['FULL-PANEL', 'DELTA-SWEEP-ONLY', 'CONFIRM-BY-DIFF', 'OUT-OF-SCOPE'] },
    proposed_falsifier: { type: 'string', description: 'the falsifier the Stage-B parties would have to agree on (measurement or argument that would kill the incumbent)' },
    branch_ledger_rows: { type: 'array', items: { type: 'object', required: ['branch', 'status', 'reason'],
      properties: { branch: { type: 'string' }, status: { type: 'string', enum: ['EXPANDED', 'PRUNED', 'DEFERRED'] }, reason: { type: 'string' } } } },
    adjacent_field_prior_check: { type: 'array', items: { type: 'object', required: ['item', 'considered_by_trees', 'note'],
      properties: { item: { type: 'string' }, considered_by_trees: { type: 'boolean' }, note: { type: 'string' } } } },
    knowledge_rows: { type: 'array', items: { type: 'object', required: ['identity', 'why_needed', 'procurement_owner'],
      properties: { identity: { type: 'string' }, why_needed: { type: 'string' }, procurement_owner: { type: 'string' } } } },
    delta_sweep_done: { type: 'boolean' },
    three_questions: { type: 'object', properties: { q1_is_Q1_right_sharpening: { type: 'string' }, q2_does_Q2_answer_Q0: { type: 'string' }, q3_separate_rungs_designer_evaluator: { type: 'string' } } },
    pin_table_per_road: { type: 'array', items: { type: 'object', properties: { road: { type: 'string' }, pins_needed: { type: 'string' }, pins_relaxed: { type: 'string' } } } },
  },
}
phase('Diff')
const results = await parallel(JUDGES.map(j => () => agent(
`You are the DIFF JUDGE for sub-problem ${j.id} "${j.title}" of the S-REVIEW session (agnostic review of the foundations at the F2-entry milestone; repository root = current directory; Windows, use forward slashes). You are NOT agnostic: you know the record. Persona: the JPP referee who will judge the decisive number ("why not X?") + the PM ("is this the shortest credible path?").
INPUTS (read all, integrally): the four de-novo trees ${TREES.join(', ')} (written by derivers who saw ONLY the agnostic statement ${RAWS}/PROBLEM_STATEMENT_agnostic.md and the brief ${RAWS}/DERIVER_BRIEF_agnostic.md — read those two as well); the record pointers for your sub-problem in ${RAWS}/INCUMBENT_pointers.md (follow every cited anchor into the sources: docs/rde_nozzle_MASTER.md, docs/choice_ledger.yaml, docs/rde_nozzle_pipeline_decision_map.md, registries, TWIN protocol, D6); the prior de-novo trees of 2026-08-17 (validation/sfoundations_raws_2026-08-13/phaseA_tree_*_CONDENSED.md + phaseB_tree_diff.md) as prior independent evidence; the measured scoping number ${RAWS}/st_scoping_number_run.log. ${j.brief_extra}
INDEPENDENCE CAVEAT OF RECORD (LOG-4b): the harness auto-loads the project memory INDEX into every subagent's system context; the derivers were instructed to read only two files and their outputs carry no repo ids (lint 0 hits), and one deriver (hyperbolic) explicitly declared the injection and its non-use. Treat every tree convergence as independent MODULO that exposure: for each CONFIRM-candidate say whether the tree DERIVES the choice (argument, lemma, cost estimate present in the tree) or merely NAMES it — a merely-named convergence is classified CONFIRM-candidate-NAMED and weighs less. You must NOT read the memory files yourself.
TASK: for EVERY approach the trees propose for your sub-problem (and every road family for SP0), classify it against the incumbent of record: CONFIRM-candidate (independently re-derives our choice — cite the record anchor AND the tree location), DIVERGENT (recommends against the incumbent), NEW (no record home). Give weight_on_Q0 = the effect on the credibility or the cost of answering Q0 by the road under review, including that road's own decisive experiment (zero = cannot change either -> not eligible for Stage B). State the incumbent's adjudication class from the ledger (DECIDED with a genuine advocate -> you perform the 2026 DELTA-SWEEP inline now and say so; declared-axiology / NEVER / single-author / no-row -> FULL-PANEL recommended). Propose the falsifier the Stage-B parties must agree on. Emit BRANCH LEDGER rows for every branch you saw (EXPANDED / PRUNED with reason / DEFERRED with trigger + owner) — "not analysed" does not exist. ADJACENT-FIELD PRIOR CHECK (mandatory): verify whether the trees considered the SOTA practice of periodically unsteady flows (turbomachinery: steady rotating frame; harmonic-balance / time-spectral methods with adjoints) and of steady adjoint-based shape optimization; each such item you cite enters as a [KNOWLEDGE] row (identity, why needed, procurement owner) — NEVER as evidence. Every [KNOWLEDGE] claim of the trees you rely on must be quoted UNVERIFIED unless a literature-registry row (docs/literature_registry.yaml) covers it.
WRITE your full judgement to ${RAWS}/stageA_diff_${j.id}.md (create it; a table of approaches with the columns of the schema; then the prose reasons with anchors; ~120-300 lines). Then return the structured index (it must not contradict the file). Do not modify any other file; never install packages; never run git.`,
  { label: `diff:${j.id}`, phase: 'Diff', schema: SCHEMA, effort: 'high' })))
const dead = JUDGES.filter((j, i) => !results[i]).map(j => j.id)
if (dead.length) log(`DEAD judges (FAILURE): ${dead.join(', ')}`)
log(`judges returned: ${results.filter(Boolean).length}/${JUDGES.length}`)
return { judges: JUDGES.map(j => j.id), dead, results }
