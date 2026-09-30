// S-REVIEW Stage B — CONVERGE + JUDGE + VERIFY (versioned artifact; 2026-09-05)
// args = { items: [{id, seed: null|'FALSE'|'TRUE'}] (definitions READ by the agents from stageB_items.json),
//          judges: [{id, persona, item_ids: [..]}], canaries: [{id, verdict_file, must: 'REJECT'|'CONFIRM'}] }
// Asserts of record: rounds <= 3 (loop bound); DEAD (null/empty) = FAILURE never dry; exit enum DRY/CAP/DEAD;
// seeds run blind in the same refuter format; dominance rejector = pure code (no agent).
export const meta = {
  name: 'sreview-stageB-converge',
  description: 'S-REVIEW Stage B: agreed falsifier first, advocate<->refuter until-dry (cap 3), independent judges, verifiers + canaries',
  phases: [{ title: 'Converge', detail: 'advocate A0 -> refuter R1 -> A1 -> R2 -> A2 -> R3 (until DRY/CAP/DEAD)' },
           { title: 'Judge', detail: 'independent judges, dominance criterion scored with anchors' },
           { title: 'Verify', detail: 'one verifier per verdict + blind canaries; unagreed-falsifier verdict = REJECTED' }],
}
const RAWS = 'validation/sreview_raws_2026-08-31'
const MAX_ROUNDS = (args.max_rounds || 3)            // ceiling amendment 2026-09-05: 2 for non-road items when the boundary rule fires
const ROAD_ROUNDS = (args.road_rounds || 3)
const RULES = `SESSION RULES (binding): repository root = current directory (Windows, forward slashes); read files, never summaries; write ONLY the file named for you; never install packages; never touch GENO/; never run git. LITERATURE ON DISK (binding, user order 2026-09-05): docs/literature_registry.yaml indexes 178 rows (paths under literature/, literature_review/, GENO/literature; statuses READ-INTEGRAL / READ-PARTIAL / UNREAD / WANTED). Every [KNOWLEDGE] claim that is LOAD-BEARING for a position, an attack or a verdict MUST be checked on the PDF on disk when the registry row has a path (cite the page; Read supports PDF pages), and otherwise quoted UNVERIFIED with an explicit PROCUREMENT ASK (paper identity + why needed) — never inflated; the litreview tiers [IO] (read at the page) / [REP] (reported by a secondary source) / [APERTO] apply to every citation. A claim above the depth actually held is a defect the verifier rejects. Rigor classes THEOREM / THEOREM* / SCHEMA / CONJECTURE / PRACTICE are used as in the record. Scope rule: an argument counts only if it changes the credibility or the cost of answering Q0 ("how to optimize an RDE nozzle") by the road under review, including that road's own decisive experiment.`
const REF_SCHEMA = { type: 'object', required: ['file_written', 'falsifier_agreed', 'falsifier_text', 'new_objections', 'objections', 'kill', 'kill_reason'],
  properties: { file_written: { type: 'string' }, falsifier_agreed: { type: 'boolean' }, falsifier_text: { type: 'string' },
    new_objections: { type: 'integer', description: 'count of objections NOT already raised in earlier rounds (0 = DRY)' },
    objections: { type: 'array', items: { type: 'string' } }, kill: { type: 'boolean', description: 'true iff the position is REFUTED on its agreed falsifier or on a defect the advocate cannot repair' }, kill_reason: { type: 'string' } } }
const ADV_SCHEMA = { type: 'object', required: ['file_written', 'falsifier_proposed', 'falsifier_accepted', 'conceded', 'rebutted', 'position_summary'],
  properties: { file_written: { type: 'string' }, falsifier_proposed: { type: 'string' }, falsifier_accepted: { type: 'boolean' },
    conceded: { type: 'array', items: { type: 'string' } }, rebutted: { type: 'array', items: { type: 'string' } }, position_summary: { type: 'string' } } }
const JUDGE_SCHEMA = { type: 'object', required: ['file_written', 'verdicts'],
  properties: { file_written: { type: 'string' }, verdicts: { type: 'array', items: { type: 'object',
    required: ['item', 'exit_state_seen', 'verdict', 'new_reasons', 'agreed_falsifier', 'priced_cost', 'pilot', 'changes_credibility_or_cost', 'disagreement_with_refuter'],
    properties: { item: { type: 'string' }, exit_state_seen: { type: 'string', enum: ['DRY', 'CAP', 'DEAD'] },
      verdict: { type: 'string', enum: ['CONFIRM', 'CONFIRM-WITH-REPAIRS', 'FLIP', 'PILOT', 'UNSETTLED-AT-CAP', 'PENDING-USER'] },
      new_reasons: { type: 'array', items: { type: 'string' } }, agreed_falsifier: { type: 'string' }, priced_cost: { type: 'string' },
      pilot: { type: 'string', description: 'one case, kill criterion, owner step, window, cost — or "none"' },
      changes_credibility_or_cost: { type: 'string' }, disagreement_with_refuter: { type: 'string' },
      cred_scores: { type: 'object', additionalProperties: { type: 'integer' } }, cost_scores: { type: 'object', additionalProperties: { type: 'string' } },
      dominance_claimed: { type: 'string' } } } } } }
const VER_SCHEMA = { type: 'object', required: ['file_written', 'verdict_file', 'agreed_falsifier_present', 'reproduction', 'result', 'reason'],
  properties: { file_written: { type: 'string' }, verdict_file: { type: 'string' }, agreed_falsifier_present: { type: 'boolean' },
    reproduction: { type: 'string', description: 'the anchors you RE-READ and the checks you re-did, not prose judgement' },
    result: { type: 'string', enum: ['CONFIRMED', 'REJECTED'] }, reason: { type: 'string' } } }

function dominates(cred, cost, credI, costI) { // pre-registered criterion (refuter §B); pure code
  const strict = (cred > credI) || (cost.hi < costI.lo - 1)
  return cred >= credI && cost.hi <= costI.lo - 1 && strict
}

phase('Converge')
const converged = await pipeline(args.items,
  async (item) => {
    const files = []
    let state = 'DEAD', rounds = 0, falsifier = null, lastRef = null
    if (!item.seed) {
      const a0 = await agent(`${RULES}\nYou are the GENUINE ADVOCATE of the ALTERNATIVE in Stage-B item ${item.id}. FIRST read your item definition = the entry with id "${item.id}" in ${RAWS}/stageB_items.json (fields: title, question, incumbent, alternative, advocate_persona = YOUR persona, refuter_persona, pointers) and then every pointer it names. ADVERSARIAL COLLABORATION: before arguing, PROPOSE the falsifier both sides must agree on ("which measurement or argument would make the program change road/choice"), then argue the alternative at its genuine best with anchors, cost, generality, and how it changes credibility or cost of answering Q0. Write ${RAWS}/stageB_${item.id}_A0.md (create; ~100-250 lines).`,
        { label: `B:${item.id}:A0`, phase: 'Converge', schema: ADV_SCHEMA, effort: 'high' })
      if (!a0) return { item: item.id, state: 'DEAD', rounds: 0, files, falsifier: null }
      files.push(a0.file_written); falsifier = a0.falsifier_proposed
    } else {
      files.push(`${RAWS}/stageB_${item.id}_A0.md`)
    }
    const maxR = (item.id === 'ROAD') ? ROAD_ROUNDS : MAX_ROUNDS
    for (let r = 1; r <= maxR; r++) {
      const ref = await agent(`${RULES}\nYou are the REFUTER in Stage-B item ${item.id}. FIRST read your item definition = the entry with id "${item.id}" in ${RAWS}/stageB_items.json (fields: title, question, incumbent, alternative, advocate_persona, refuter_persona = YOUR persona, pointers), then ALL prior files of this item in order: ${files.join(', ')}, then every pointer the definition names. Round ${r} of at most ${maxR}. FIRST settle the falsifier: state whether you AGREE with the advocate's proposed falsifier (or amend it — the agreed text is binding for the judge). THEN attack the position on its agreed falsifier and on every defect (hypotheses, anchors, costs, [KNOWLEDGE] claims without registry cover). Count new_objections = objections NOT already raised in earlier rounds (0 means you are DRY: nothing new to say). Set kill = true only if the position is refuted on its agreed falsifier or on an unrepairable defect. Attack the INCUMBENT too where it is weaker than the alternative — you serve the truth, not the incumbent. Write ${RAWS}/stageB_${item.id}_R${r}.md (create; ~80-200 lines).`,
        { label: `B:${item.id}:R${r}`, phase: 'Converge', schema: REF_SCHEMA, effort: 'high' })
      rounds = r
      if (!ref) { state = 'DEAD'; break }
      files.push(ref.file_written); lastRef = ref
      if (ref.falsifier_agreed) falsifier = ref.falsifier_text
      if (ref.new_objections === 0) { state = 'DRY'; break }
      if (item.seed) { if (ref.kill || r >= 2) { state = 'DRY'; break } else continue }
      if (r === maxR) { state = 'CAP'; break }
      const adv = await agent(`${RULES}\nYou are the GENUINE ADVOCATE of the ALTERNATIVE in Stage-B item ${item.id} (round ${r} reply). FIRST read your item definition = the entry with id "${item.id}" in ${RAWS}/stageB_items.json (advocate_persona = YOUR persona), then ALL prior files of this item in order: ${files.join(', ')}, then the pointers the definition names. Accept or amend the refuter's falsifier text (falsifier_accepted), CONCEDE what is right, REBUT what is wrong with anchors, and update your position. Write ${RAWS}/stageB_${item.id}_A${r}.md (create; ~60-180 lines).`,
        { label: `B:${item.id}:A${r}`, phase: 'Converge', schema: ADV_SCHEMA, effort: 'high' })
      if (!adv) { state = 'DEAD'; break }
      files.push(adv.file_written)
      if (adv.falsifier_accepted) falsifier = falsifier || adv.falsifier_proposed
    }
    log(`item ${item.id}: exit ${state} after ${rounds} refuter round(s)`)
    return { item: item.id, state, rounds, files, falsifier, seed: item.seed || null, kill: lastRef ? lastRef.kill : null }
  })
const items = converged.filter(Boolean)
const seedReport = items.filter(x => x.seed).map(x => ({ id: x.item, seed: x.seed, kill: x.kill, ok: x.seed === 'FALSE' ? x.kill === true : x.kill === false }))
log(`dual-seed: ${JSON.stringify(seedReport)}`)

phase('Judge')
const real = items.filter(x => !x.seed)
const judged = await parallel(args.judges.map(j => () => agent(`${RULES}\nYou are an INDEPENDENT JUDGE (persona: ${j.persona}; you are NOT the orchestrator and NOT any Stage-A diff judge). Items assigned: ${j.item_ids.join(', ')}. For each item read EVERY file of its Stage-B exchange (listed here: ${JSON.stringify(real.filter(x => j.item_ids.includes(x.item)).map(x => ({ item: x.item, exit_state: x.state, files: x.files, agreed_falsifier: x.falsifier })))}) plus the item's pointers in ${RAWS}/stageB_items.json. Verdict per item: CONFIRM (incumbent stands, with NEW reasons not inherited from the record) / CONFIRM-WITH-REPAIRS / FLIP (priced: cost of rewrite vs gain on Q0) / PILOT (pre-registered: one case, kill criterion, owner step, window, cost) / UNSETTLED-AT-CAP (exit CAP, not dry -> never CONFIRM) / PENDING-USER (DEAD or undecidable). A verdict without an AGREED falsifier is not allowed: write PENDING-USER and say why. For the ROAD item apply the PRE-REGISTERED DOMINANCE CRITERION verbatim from ${RAWS}/../PROGRESS_2026-08-31_Sreview.md (LOG-2, "PROMPT-42 DOMINANCE CRITERION"): score CRED(R) in 0..5 (q1 external truth anchor, q2 strongest classical opponent, q3 uncertainty budget below threshold, q4 reproducibility/version-stability, q5 generalization beyond n = 1) and COST(R) = sessions-to-first-credible-number as a band "lo-hi" for the incumbent and every alternative, each score with a file anchor; state dominance_claimed. Report your disagreement rate with the refuter. Write ${RAWS}/stageB_JUDGE_${j.id}.md (create).`,
  { label: `B:judge:${j.id}`, phase: 'Judge', schema: JUDGE_SCHEMA, effort: 'high' })))
const judgeOut = judged.filter(Boolean)
// dominance rejector (pure code, pre-registered): fictitious roads
const rej1 = dominates(3, { lo: 6, hi: 8 }, 3, { lo: 4, hi: 6 })   // equal CRED, higher cost -> must NOT dominate
const rej2 = dominates(4, { lo: 2, hi: 3 }, 3, { lo: 4, hi: 6 })   // CRED+1, cost_hi <= cost_lo(I)-1 -> MUST dominate
log(`dominance rejector: equal-CRED-higher-cost dominates=${rej1} (must be false); CRED+1-cheaper dominates=${rej2} (must be true)`)

phase('Verify')
const verdictFiles = judgeOut.map(j => j.file_written)
const toVerify = [...verdictFiles.map(f => ({ kind: 'judge', file: f })), ...(args.canaries || []).map(c => ({ kind: 'canary', file: c.verdict_file, id: c.id }))]
const verified = await parallel(toVerify.map(v => () => agent(`${RULES}\nYou are an INDEPENDENT VERIFIER. Verify the verdict file ${v.file}: re-read every file and anchor it cites (the Stage-B exchange files under ${RAWS}/stageB_*.md, the record anchors), check that EVERY verdict rests on an AGREED falsifier stated in the exchange (a verdict without one -> REJECTED), that "new reasons" are genuinely new relative to the cited record anchors, that priced costs cite anchors, that CRED/COST scores (if any) are supported by the files, and that no exit state CAP was turned into CONFIRM. Return CONFIRMED or REJECTED with the reproduction field listing what you re-read and re-checked. Write ${RAWS}/stageB_VERIFY_${v.kind}_${(v.id || v.file.split('/').pop().replace('.md', ''))}.md (create).`,
  { label: `B:verify:${v.kind}:${v.id || v.file.split('/').pop()}`, phase: 'Verify', schema: VER_SCHEMA, effort: 'high' })))
const canaryReport = (args.canaries || []).map((c, i) => { const r = verified[verdictFiles.length + i]; return { id: c.id, must: c.must, got: r ? r.result : 'DEAD', ok: r ? ((c.must === 'REJECT') === (r.result === 'REJECTED')) : false } })
log(`canaries: ${JSON.stringify(canaryReport)}`)
return { items: items.map(x => ({ item: x.item, state: x.state, rounds: x.rounds, files: x.files, falsifier: x.falsifier, seed: x.seed, kill: x.kill })),
         seedReport, judges: judgeOut, dominance_rejector: { rej1_must_be_false: rej1, rej2_must_be_true: rej2 }, verified: verified.filter(Boolean), canaryReport }
