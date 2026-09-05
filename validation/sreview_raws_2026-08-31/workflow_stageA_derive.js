// S-REVIEW Stage A — DERIVE (versioned artifact of the launched Workflow script; 2026-09-05)
export const meta = {
  name: 'sreview-stageA-derive',
  description: 'S-REVIEW Stage A derive: 4 agnostic de-novo derivers write strategy + sub-problem trees from the problem statement only',
  phases: [{ title: 'Derive', detail: '4 lens-distinct derivers, statement-only briefs, files written by the agents' }],
}
const RAWS = 'validation/sreview_raws_2026-08-31'
const LENSES = [
  { key: 'variational', persona: 'a mathematician of variational methods and optimal control of PDE-constrained shape problems (existence, optimality systems, adjoint/sensitivity theory, guarantees)' },
  { key: 'hyperbolic', persona: 'a computational gas-dynamicist specialized in hyperbolic conservation laws, supersonic nozzle flows, shock/contact treatment, marching and shock-capturing solvers, a-posteriori error control' },
  { key: 'optimization', persona: 'a numerical-optimization and uncertainty-quantification engineer (gradient-based and derivative-free search, surrogates and Bayesian optimization, robust design, verification and reproducibility of computational results)' },
  { key: 'propulsion', persona: 'a rocket-propulsion test engineer who has designed, fired and measured nozzles on thrust stands, knows RDE test practice, and reviews for a propulsion journal (the strongest competing practice, base-pressure reality, what a referee accepts as proof)' },
]
const SCHEMA = {
  type: 'object',
  required: ['lens', 'file_written', 'strategies', 'top_strategy', 'subproblems', 'order_of_battle', 'knowledge_claims_count', 'independence_declaration'],
  properties: {
    lens: { type: 'string' },
    file_written: { type: 'string' },
    independence_declaration: { type: 'string', description: 'state explicitly that ONLY the two brief files were read; list any other file you opened (must be none)' },
    strategies: { type: 'array', items: { type: 'object',
      required: ['name', 'tuple', 'question_answered', 'cost_to_credible_answer', 'generality', 'pins_needed', 'pins_relaxed', 'falsifier', 'time_to_number', 'rank', 'abandon_measurement', 'decisive_result'],
      properties: {
        name: { type: 'string' },
        tuple: { type: 'object', required: ['objective', 'time_treatment', 'spatial_representation', 'solver_and_information', 'search_and_guarantee', 'decisive_result'],
          properties: { objective: { type: 'string' }, time_treatment: { type: 'string' }, spatial_representation: { type: 'string' }, solver_and_information: { type: 'string' }, search_and_guarantee: { type: 'string' }, decisive_result: { type: 'string' } } },
        question_answered: { type: 'string' }, cost_to_credible_answer: { type: 'string' }, generality: { type: 'string' },
        pins_needed: { type: 'array', items: { type: 'string' } }, pins_relaxed: { type: 'array', items: { type: 'string' } },
        falsifier: { type: 'string' }, time_to_number: { type: 'string' }, rank: { type: 'integer' },
        abandon_measurement: { type: 'string' }, decisive_result: { type: 'string' } } } },
    top_strategy: { type: 'string' },
    subproblems: { type: 'array', items: { type: 'object',
      required: ['id', 'load_bearing', 'recommendation', 'decision_criterion', 'falsifier', 'options_count'],
      properties: { id: { type: 'string' }, load_bearing: { type: 'boolean' }, recommendation: { type: 'string' }, decision_criterion: { type: 'string' }, falsifier: { type: 'string' }, options_count: { type: 'integer' } } } },
    order_of_battle: { type: 'array', items: { type: 'string' } },
    knowledge_claims_count: { type: 'integer' },
  },
}
phase('Derive')
const results = await parallel(LENSES.map(l => () => agent(
`You are ${l.persona}. You are one of several INDEPENDENT derivers attacking a design-optimization problem from scratch.
READ EXACTLY TWO FILES and nothing else: (1) ${RAWS}/PROBLEM_STATEMENT_agnostic.md (the problem), (2) ${RAWS}/DERIVER_BRIEF_agnostic.md (your deliverable). HARD RULE: do not open, grep, list or read ANY other file, directory, registry, log or source of this repository — your value is independence; an output showing project-internal names or decisions is discarded. Open-literature knowledge is welcome, tagged [KNOWLEDGE] with author/year and a read-depth marker [full]/[abstract]/[title]; never inflate.
Work through the brief completely: Level 0 (strategies as tuples, open enumeration, the practice of today included, hybrids included, each with cost/generality/pins/falsifier/time-to-number/rank/abandon-measurement/decisive result) and Level 1 (every sub-problem SP-OBJ, SP1..SP9, SP-PB, SP-CARM with the full 2026 option space, recommendation, decision criterion, falsifier, load-bearing flag, order of battle). Give dry-level arguments where a fork is decidable by a short argument.
WRITE your complete tree as structured markdown to the file ${RAWS}/stageA_tree_${l.key}.md (create it; number every option; ~300-600 lines; the file is authoritative). Then return the condensed index in the required structured form (it must not contradict the file). Do not modify any other file; never install packages; never run git.`,
  { label: `derive:${l.key}`, phase: 'Derive', schema: SCHEMA, effort: 'high' })))
const dead = LENSES.filter((l, i) => !results[i]).map(l => l.key)
if (dead.length) log(`DEAD derivers (FAILURE, not dry): ${dead.join(', ')}`)
log(`derivers returned: ${results.filter(Boolean).length}/${LENSES.length}`)
return { lenses: LENSES.map(l => l.key), dead, results }
