# REWRITE FINAL — final act (C11, C17-pre, C17, C18, C19)

Converged version: REWRITE_v1 with EVERY repair from REFUTE_v1 applied.
Proposal only — of no effect until implemented in specs_c12.py / specs_c34.py,
assert-gate rebuilt, and user-gated (per BRIEF consumption arc).

## REPAIR LOG (all REFUTE_v1 findings consumed)
- C11 (9)(10)(11): three bullets trimmed to <=15 tokens, content unchanged.
- C11 (12): table cells trimmed (header "source | best | worst | how estimated";
  "Swirl thrust unmodelled"; "Designing the nozzle alone"; "Optimum shift").
  If the built slide still exceeds the ~100 budget, the honesty_table layout
  must be declared exempt in BUILD_LOG explicitly — never a silent overrun.
- C11 (13): script forward-pointer split — heel = derivation already laid out
  (NOT on the plan slide); optimum shift = measurement on the plan slide.
- C17-pre (5): three distances restored by name; no additivity claim; arc
  keeps the label "total (composition)".
- C17-pre (6): "three proven bounds" → "three exact results each close a piece
  of the model gap — its smooth part; none touch formulation."
- C17-pre (7): "the model gap wins" → "can win" (script: "can dominate").
- C17-pre (8): immunity claim removed — "the programme fails only if…", never
  "the method is wrong only if…" (F-12 trap disarmed).
- C17 (6): "confirmed" → "the error band closes" (Guard 6 / D-44: band, never
  adequacy).
- C17 (7): "run committed after step 1" → "commit decided after step 1";
  propagated verbatim to C18 card 1 (cross-slide note 2).
- C17 (10): card 3 and band 1 trimmed; card 4 "unsteady benchmark the field
  lacks" → "reference the field lacks" (script keeps "unsteady"). If the two
  slim bands are ruled outside the card budget, BUILD_LOG must say so.
- C18 (2): card 1 matches repaired C17 card 4 verbatim.
- C18 (6): band trimmed to 35 words ("screened on entry" implied by
  "rejected"; nothing anchored lost).
- C18 (7): script 5 ends at the admission; "we say that now rather than after
  the fact" deleted ("we say so" tic, F-8).
- C19 (1): title universal dropped → "What we discard is measurable —
  validation costs minutes, not weeks."
- C19 (8): closing band completeness claim dropped → "The method's limits are
  on these slides — each with a number, or the named way to get one"; "each"
  to be verified at build time against every stated limit.
- C19 (10): spoken "first" in the D-06 locked, query-bounded form. NOTE
  (conflict resolution, declared): REFUTE says "copy the exact A2 wording",
  but A2 as built (specs_a.py :42-67) is agenda-only and carries no spoken
  primacy sentence; the locked form is therefore rendered from the guard-9
  query-bounded formula of record (C19 notes: "'First' in D-06 locked form,
  query-bounded (guard 9)"). BRIEF is not violated; the repair's intent
  (bounded claim) is kept, its letter (copy from A2) is impossible and noted.
- C19 (12): eng bullet 3 trimmed to 9 words; residual ~66 net words > 60 and
  5 bullets vs <=3 — the summary layout's budget treatment MUST be declared
  in BUILD_LOG by the implementer (two-column record grammar), not inherited
  silently.

No repair conflicted with the BRIEF except as noted at C19 (10) — a letter-
level impossibility, resolved in the repair's own spirit. All repairs weaken
claims, restore register, or restore sense; none adds a claim or a number.

---

## SLIDE [41/C11] (position 42) — replaces "The residual error, channel by channel"

### TITLE
Where the remaining error lives, source by source

### ON-SLIDE
Table (layout `honesty_table`, header: **source | best | worst | how estimated**):

| source | best | worst | how estimated |
|---|---|---|---|
| Mean azimuthal residual | exactly 0 | exactly 0 | proven (hypotheses stated) |
| Swirl thrust unmodelled | 1.5% of thrust | 3% of thrust | order estimate |
| Input-data bias | 0.6% of pressure | 9% of pressure | order estimate + literature |
| Jumps at the wave fronts | no number yet — derivation planned | — | open |
| Designing the nozzle alone | ~1% | ~1% | literature, page-verified |
| Optimum shift | first campaign measures it | — | open |

Bullets (3):
- Sources do not add: best case single-digit %; with strong swirl, >10% not excluded.
- Largest adverse signal published: +13 points of ideal from a shroud, unexplained (Paxson & Miki 2022).
- No published benchmark separates this prediction from the true unsteady flow — we measure it ourselves.

### VISUAL
Keep the existing six-row table + bullets grammar. One change of emphasis:
the two "no number yet / open" rows get a visibly lighter fill than the four
numbered rows, so the admission is read directly off the table (fact, not
narration), and the "how estimated" column uses only the plain words above.
Full table stays in backup (s-60, to be built per F-3).

### SCRIPT
1. This is our error budget: every source of error we know, its best and worst case, and how each number was obtained — a theorem, an order estimate, or a published datum.
2. Start with the two rows that have no number yet: for the jumps at the wave fronts, the derivation that will produce the number is already laid out; for the shift of the optimum, the measurement is in the plan two slides ahead.
3. These sources do not add into a single figure — they are different physics at different confidence levels — so the summary is a band: best case, with weak swirl, single-digit percent overall is plausible; with strong swirl, more than ten percent is not excluded.
4. One computed case of ours gained +0.51 percent — and the uncertainty on that figure is about thirty percent of the value itself, so read it as roughly half a percent, not as a promise of more.
5. For scale: Rao's classical method is credited with 0.04 to 0.34 percent — their numbers, in their regime.
6. The largest published signal in the adverse direction: Paxson and Miki, 2022, add a shroud at fixed area ratio and the plug gains thirteen points of ideal — unexplained by the authors; if swirl content is doing that, it is exactly the worst row of this table.
7. And note what the literature does not contain: no published benchmark separates a phase-averaged prediction like ours from the true unsteady three-dimensional flow.
8. So nobody else can settle this table for us — the measurements that fill it are ours to make, and they come next.

### ANCHORS
- Table rows (all six, values unchanged) → notes [PROVENANCE] "Table cells -> CH3-feed-4 (classes per cell, forchetta §; CH7 PART 5 headline :1731-1743): mean channel THEOREM* (K-bar=0, perimeter H-RED-2); booking debt 1.5-3% [SE]; B1 0.6-9% p [SE]+lit; heel delta/L_H UNDERIVED -> CH3-feed-5 (SCHEMA + derivers named); sizing ~1% [REP]; optimum-shift no number (:1506)". Row relabels are plain-word renderings, no value changed: "booking debt" → "Swirl thrust unmodelled" (same 1.5–3% of thrust); "the heel" → "Jumps at the wave fronts" (same open status, derivation road named); "sizing level" → "Designing the nozzle alone" (same ~1%; substitution reading anchored by C17 card 3 "price of the substitution" + "~1% sizing stands", cross-consistent with C17 card 3 as repaired).
- Bullet 1 → current bullet "Channels do not sum. Best case: single-digit %; off-axis, >10% not excluded." ("off-axis" → "with strong swirl": weakened plain form; C12 notes identify the off-axis channel with swirl content).
- Bullet 2 → current bullet + C12 notes "[REP] page-verified (findings_registry:2026; M0:1345, 1350-1353)"; "at fixed area ratio" restored in script 6 (no strengthening).
- Bullet 3 + script 7 → notes "CT-3 STRICT form: no published referee THAT DISCRIMINATES the per-phase-averaged prediction against 3D-unsteady truth (restrictive clause binding for Q&A)" — restrictive clause kept on-slide ("this prediction … from the true unsteady flow").
- Script 2 (repaired) → heel road = derivation chain CH3-feed-5 (five-field → route-B → M-RED → R22-CFD), NOT on the C17 slide — no forward reference to C17 for the heel; optimum shift → C17 card 2 (head-to-head), the only row resolving there.
- Script 4 → notes "CH1-feed-9 (band-underinclusion declared)"; ±30% disambiguated as relative (script of record already reads "carries a thirty-percent uncertainty"). Weakened, not strengthened ("not a promise of more").
- Script 5 → notes "Rao 0.04-0.34% their numbers (CT-6)".
- Script 8 → notes "CH5-feed-10 + CT-3"; "close the bracket" metaphor dropped, content kept.
- Guard 6 / D-44 respected: slide shows a band, never claims adequacy.
- SENSE [41/C11] check: error budget with evidence classes ✓, single-digit best case ✓, +13-point marker on the table ✓, no external referee / we measure it ourselves ✓.

---

## SLIDE [42/C17-pre] (position 43) — replaces "Which gap dominates — the honest map"

### TITLE
Which gap dominates — and how we would find out

### ON-SLIDE
Three columns (layout `three_gaps`):
- **mean-state design** — designs to the time-averaged flow; never compared head-to-head, by anyone
- **our per-phase design** — this method
- **true 3D optimum** — incomputable, for anyone

Gaps caption: three distances: **formulation** (which problem you solve) · **model** (which physics you keep) · end to end, **the total** — the question is which dominates.

Band 1 (hypothesis + weak point, merged per F-11c):
Working hypothesis, testable: at fixed constraints the formulation gap dominates — three exact results each close a piece of the model gap (its smooth part); none touch formulation. Its weak point: the wave-front jumps carry no bound yet — if large, the model gap can win.

Band 2 (failure condition):
The programme fails only if two independent measurements both go against it: the head-to-head and the residual measurement.

### VISUAL
Keep the three-box chain with two gap arrows (mean-state → ours = formulation;
ours → 3D optimum = model) and a light end-to-end arc over both labeled
"total (composition)"; two full-width bands below (already merged to two per
F-11c). The arrows carry the words "formulation" / "model" directly — no bare
letters anywhere (gap-letters map, FD-4/CW-4).

### SCRIPT
1. Three designs on one axis: a design built on the time-averaged flow; ours, built phase by phase; and the true three-dimensional optimum, which nobody can compute.
2. Between them, two gaps in series — a formulation gap: you asked the wrong question of the flow; and a model gap: you kept the wrong physics — and the end-to-end distance to the truth is their composition, the third thing on the map.
3. The value question of the whole enterprise is which of these dominates.
4. Note the left comparison first: nobody has ever computed a time-averaged design against a phase-resolved one at equal constraints — us included; it is the first measurement on our plan.
5. Our working hypothesis — a hypothesis, not a theorem, and it can be proven wrong: at fixed constraints, the formulation gap dominates.
6. The grounds: three of the results you have already seen close pieces of the model gap on its smooth part — the exact change of coordinates, the vanishing mean equation, the cleared full-state average — while nothing yet bounds the formulation gap.
7. The weak point travels with the hypothesis, on the same slide: the jumps at the wave fronts are the one unbounded first-order piece of the model gap — if they turn out large, the model gap can dominate anyway.
8. And the programme fails only if two independent measurements both go against it — the head-to-head and the residual measurement; each of them is on the plan that follows.

### ANCHORS
- Three designs / three distances frame → notes "[PROVENANCE] Three designs / three gaps -> CH6-feed-1 (scope 'in the record', repair WB1-C3-14) + CH6-feed-2 (hierarchy hypothesis)". Third distance ("the total") restored by name per REFUTE (5); no additivity claim made anywhere — "composition" appears only as the arc label of record.
- "never compared head-to-head, by anyone" → current column text "which nobody has computed in this head-to-head, us included" (sentence case per F-22).
- "the programme" → "this method" (register repair; same referent).
- Band 1 sentence 1 → current "three suppression results" + record script smooth-part scope, both restored per REFUTE (6): "close a piece of the model gap — its smooth part" (no bound-on-the-gap claim); script 6 lists them exactly as the current script does (FD-5(ii) back-pointer kept).
- Band 1 sentence 2 → record "if large, the model gap CAN dominate" — possibility restored per REFUTE (7) ("can win" / "can dominate anyway").
- Heel co-presence on the SAME slide → notes "CH6-feed-3 (guard 1: hierarchy NEVER without the (J) heel — THIS slide is the enforcement site)": band 1 keeps hypothesis and weak point together.
- Band 2 → current death_line "Programme failure needs two independent misses — both measurable: head-to-head + residual measurement" — subject restored to THE PROGRAMME per REFUTE (8) (no method-immunity claim; F-12 trap disarmed) + notes "two-failure death -> CH6-feed-4".
- SENSE [42/C17-pre] check: three-gap frame (formulation/model/composition) ✓, formulation-dominates hypothesis stated as falsifiable ✓, weak point co-present ✓, two-independent-misses PROGRAMME failure condition ✓.

---

## SLIDE [43/C17] (position 44) — replaces "What tightens the bracket, in order — every outcome pre-registered"

### TITLE
Four measurements, in order — consequences fixed before the data

### ON-SLIDE
Four cards as ONE numbered left-to-right arrow sequence (F-11b):

1. **Residual** — how much the phase-averaged equations miss, on nozzles already solved. Small → error bars tighten; large → dominant source named. *First — cheapest.*
2. **Head-to-head** — our design vs time-averaged design, equal constraints; no such number exists yet. Either result publishable. *Machine ready — first campaign.*
3. **Coupled pair** — same nozzle with and without the combustor: the cost of designing alone. ~1% holds → estimate stands; exceeded → step 4 moves up. *After step 1.*
4. **Full 3D reference** — ~12M-cell reference the field lacks. Inside its band → the error band closes; outside → failing source named. *Route chosen now; commit decided after step 1.*

Band 1: Ours vs time-averaged: measurable in-house. The true 3D optimum: computable by no one — we bound it.

Band 2: Stop criterion: measured gain below ~1% Isp → effort pivots to certification and operability.

### VISUAL
Replace the 2×2 card grid with one numbered left-to-right arrow chain of four
compact cards (order IS the content, per F-11b), arrowheads between cards;
two slim full-width bands underneath (in-house vs bounded; stop criterion).
No Gap A / Gap B letters anywhere — the two distances are said in words in
band 1 (gap-letters map, FD-4/CW-4). Buildable with existing cards + arrows.
If the two slim bands are ruled outside the card word-budget, BUILD_LOG must
say so explicitly (REFUTE (10)) — no silent overrun.

### SCRIPT
1. This is the measurement plan, and the order is the content: four steps, each with its two possible outcomes and what each outcome triggers — fixed now, before any data arrive.
2. Step one, the cheapest: measure the residual — take nozzle families the machine has already solved and checked, put them back into the full phase-averaged equations, and read how much is missed.
3. Small residual: the error bars tighten and the family is promoted with a stated bar; large residual: it names which error source dominates — either outcome is informative, and it also builds the referee that the literature does not contain.
4. Step two, the head-to-head: our design against the time-averaged design at equal constraints — today no such number exists, on any side; a material gap pays for the method, a small gap proves standard practice right at that rank and we would be the first to prove it — both results are publishable.
5. Step three: a paired simulation of the same nozzle with and without the combustor coupled, on the kind of template the field already uses — it prices what we give up by designing the nozzle alone.
6. If the literature's roughly one-percent estimate holds, that row of the error table stands; if it is exceeded, the big reference run moves up the queue.
7. Step four, the largest: a twelve-million-cell unsteady reference simulation — the benchmark the field lacks; today we choose only how to procure it, partner or purchase — whether to commit the run is decided after step one.
8. One distance we can measure entirely in-house — ours against the time-averaged design; the other — the distance to the true three-dimensional optimum — no one can compute, so we bound it.
9. And the stop criterion is fixed in advance: if the measured gain falls below about one percent of Isp, we stop pushing performance and pivot to certification and operability.
10. The campaign has just opened: none of these results is promised as acquired.

### ANCHORS
- Order of the four steps → notes "[PROVENANCE] Roadmap order -> CH6-feed-9"; on-slide word "roadmap" dropped (forbidden), order kept.
- Card 1 → current card 1 ("measured residual bands, per certified family" → "on nozzles already solved" = plain weakened form; "small → promoted, with a bar; large → dominant channel named" → "error bars tighten / dominant source named"); referee-that-does-not-exist sentence in script 3 → current script "it builds the referee that does not exist in the literature".
- Card 2 → current card 2 + notes "[GATE DECISION WIRED] Twin (b): 'first campaign of the phase' — NOT 'if ordered'"; "twin kill-or-validate both-informative -> CH6-feed-4"; "no number exists on any side before it runs" (current script, verbatim content). No internal deadline (CKP-S3-5(b)): "first campaign" only.
- Card 3 → current card 3, trimmed per REFUTE (10) ("price of the substitution, on the field's template" → "same nozzle with and without the combustor: the cost of designing alone"; "bar holds → ~1% sizing stands" → "~1% holds → estimate stands", same number, C11 row 5 cross-consistent).
- Card 4 → current card 4 ("~12M-cell decider" kept as number; "inside → bracket closes" → "inside its band → the error band closes" per REFUTE (6), Guard 6 / D-44: band closure, never validation verdict; "today: channel, not commit" → "route chosen now; commit decided after step 1" per REFUTE (7) — the DECISION is reserved, no commitment promised; script 7 already consistent). "Unsteady" spoken in script 7, dropped from card per REFUTE (10).
- Band 1 → current gap_line with letters removed per notes "[GAP-LETTERS MAP - FD-4/CW-4] … in speech use the words, not bare letters"; trimmed per REFUTE (10).
- Band 2 → current kill_line; "declared" dropped (forbidden), content identical (G2 value gate → CH6-feed-6; armed-rejector, today undecidable → CH6-feed-7, D-44 gated).
- Script 10 → current script "The phase is JUST opened: no campaign result is promised as acquired" (word "phase" → "campaign").
- Title / script 1 ("consequences fixed before the data") → current closing "Every outcome is pre-registered: the decision rule is fixed before the data arrive" — same content, forbidden words removed; M-RED derived bands pre-registration → CH3-feed-6 (notes only).
- SENSE [43/C17] check: four derivers in order ✓, each with its rule ✓, stop criterion <~1% Isp → pivot ✓, outcomes fixed before data ✓.

---

## SLIDE [44/C18] (position 45) — replaces "Three asks — each one decision-ready"

### TITLE
Three requests: a reference simulation, engine data, publication support

### ON-SLIDE
Three cards (exactly three, per F-4):

1. **Reference 3D simulation** — What: ~12M-cell reference run, by collaboration or procurement. To decide: the route — partner or purchase; the commit is decided after the residual measurement. When: route now, run later.
2. **Engine test data** — What: high-speed pressure traces or hot-fire imaging. To decide: which rig, which instrumentation. When: starting now.
3. **Publication & access** — What: venues for the method papers; three key papers we cannot access. To decide: endorsement. When: at your convenience.

Band: "What input does the method need?" Specs suffice to design; each added measurement raises the confidence grade (scale in backup). Data outside the required class is rejected — not yet exercised on real data.

### VISUAL
Keep the three ask-cards with the What / To decide / When triplet (sentence
case, no ALL-CAPS), equal width — no fourth card (F-4). The reliability-ladder
mini-diagram moves to backup (F-4 option b); the band below the cards keeps
only the input question, the confidence-grade sentence with its backup
pointer, and the rejection + not-yet-exercised statement.

### SCRIPT
1. Three requests — for each: what we ask, what you would need to decide, and when.
2. First, the reference simulation: today we ask only for the route — a collaboration or a procurement; the decision to actually run it comes after the residual measurement, exactly in the order of the plan you just saw.
3. Second, engine test data in the class the method needs: high-speed pressure traces or hot-fire imaging, sufficient to verify that stagnation temperature is flat over a cycle and to read the cycle frequency.
4. One property to be aware of: the input screen decides, it does not bless — it is built to reject data outside that class, and we expect real data to exercise it.
5. That screening has not yet been tried on a real dataset.
6. Third: publication venues for the method papers, and three key papers we currently cannot access.
7. And the question every panel asks — what input does your method need: engine specifications alone are enough to produce a design; every additional measurement raises the confidence grade of the result, on a scale spelled out in the backup.

### ANCHORS
- Card 1 → current card 1 ("the channel" → "the route — partner or purchase": plain form of "collaboration or procurement"); "the commit is decided after the residual measurement" = verbatim propagation of the repaired C17 card 4 (REFUTE (2) + cross-slide note 2) — decision reserved, no commitment promised. No internal deadline (CKP-S3-5(b)).
- Card 2 → current card 2 verbatim content; "instrumentation window" → "which instrumentation" (register); stagnation-flatness + cycle-frequency detail in script 3 → current script verbatim content.
- Card 3 → current card 3 verbatim content.
- Band → current input_band, trimmed per REFUTE (6) to 35 words: "Specs suffice to design" ✓; "climbs a declared reliability ladder" → "raises the confidence grade (scale in backup)" (ladder itself to backup per F-4 option b); "Data is not fed in: it is admitted — and the entry gate can say no" → "Data outside the required class is rejected" (screening implied by rejection; courtroom metaphor removed, nothing anchored lost); "(A contract prediction — not yet exercised on real data.)" → "not yet exercised on real data" (F-8 terminal form, per spine repair).
- Script 5 → ends at the admission per REFUTE (7); the "we say that now rather than after the fact" clause deleted (the "we say so" tic, F-8 / BRIEF forbidden list — on-slide AND in script).
- Provenance of all band content → notes "[PROVENANCE] Specs-ladder Annex B -> CH10-feed-1 (stage P34 'prediction' declared — tag here, words on slide); G6 loud-reject never exercised -> CH10-feed-2; TRIPLE monitor -> CH7-feed-5" (script 4 "decides, does not bless" is the current script's own wording).
- Open-items remain OFF-slide in backup (F-4, current notes) — unchanged here.
- SENSE [44/C18] check: three concrete requests ✓ (reference-class run, engine data in the stated class, publication/procurement) + the data-admission answer to "what input does your method need" ✓ — all in engineering words.

---

## SLIDE [45/C19] (position 46) — replaces "A method you can audit — fast enough to validate economically"

### TITLE
What we discard is measurable — validation costs minutes, not weeks

### ON-SLIDE
**For the engineers**
- the first per-phase variational design method for RDE nozzles
- what the reduction discards is an explicit, measurable operator
- an error budget, source by source, each with its estimate

**For the decision-makers**
- validation in minutes, not weeks
- a stepwise plan with known costs, fixed consequences, and a stop criterion

Closing band: The method's limits are on these slides — each with a number, or the named way to get one.

Figure: pipeline reprise, legible height, stage names identical to the machine slide (s-38).

### VISUAL
Keep the two-column summary (engineers / decision-makers) over a single
closing band. Fix the layout defect: enlarge the pipeline miniature to a
legible height, reuse the machine slide's stage naming verbatim (F-2/F-23),
and clear it from the footer banner so nothing collides. This reprise is the
bookend: first slide of the machine, last slide of the talk, same picture.
Budget note (REFUTE (12)): the summary layout runs ~66 net words over the
60-word non-card cap and 5 bullets against the ≤3 rule — the two-column
record grammar is the mitigation; the implementer MUST declare the summary
layout's budget treatment in BUILD_LOG, never overrun silently.

### SCRIPT
1. Two things to retain.
2. For the engineers: this is, as far as our search of the literature has found, the first per-phase variational design method for RDE nozzles.
3. What the reduction throws away is not hand-waved — it is an explicit operator you can evaluate, so the approximation itself is measurable.
4. The error budget is stated source by source, each entry with how it was estimated — a theorem, an order estimate, or a published datum — and where there is no number yet, the way to get one is named.
5. For the decision-makers: the machine validates a design in minutes, not weeks — so testing this method is cheap.
6. The plan is stepwise, its costs are known, and the consequence of each possible outcome is fixed before the data arrive — including the point where we would stop: below about one percent of measured Isp gain, effort pivots to certification and operability.
7. How much better a nozzle designed this way will fly, nobody yet knows — no number exists, on any side, until the head-to-head runs; it is the first measurement of the campaign.
8. That number is what we came here to go and get. Thank you.

### ANCHORS
- Title → REFUTE (1) applied: universal "every approximation" dropped; anchored fusion of "what the reduction discards is an explicit, measurable operator" (record verbatim bullet) + "minutes, not weeks" (record verbatim); "audit" (forbidden) removed; "economic act(s)" dropped (F-21, per spine repair).
- Engineers bullets 1–2 → current eng_bullets 1–2 verbatim ("MEASURABLE" already to sentence case per F-22).
- Engineers bullet 3 → current bullet 3 "an honest error bracket, channel by channel, each cell with its evidence level" → "an error budget, source by source, each with its estimate" (REFUTE (12) trim; forbidden words removed; content identical, weaker if anything).
- Decision-makers bullet 2 → current prog_bullet 2 "an incremental plan, already priced, with pre-registered outcomes — and a declared stop criterion" → "a stepwise plan with known costs, fixed consequences, and a stop criterion" (three process words removed, content identical; stop-criterion wording consistent with position 44, per F-1 repair).
- Closing band → REFUTE (8) applied: completeness universal dropped ("Every limit … is on these slides" was falsified by the deck's own backup — open decisions live on the backup slide). Final form: "The method's limits are on these slides — each with a number, or the named way to get one." BUILD DUTY: "each" verified at build time against every stated limit (heel: road named ✓; optimum shift: campaign ✓; input screen: real data ✓; formulation gap: head-to-head ✓); the open-decisions backup slide is NOT claimed by the main slides. The "honesty is not a disclaimer" sentence is deleted, not translated: the band shows the property instead of naming it (notes provenance: instrumented honesty -> CH6-feed-10, D-44/P34/card discipline; dual takeaway -> MESSAGE_ARCHITECTURE).
- Script 2 → REFUTE (10) applied: "first" spoken in the D-06 locked, query-bounded form (guard 9): "as far as our search of the literature has found". Declared note: A2 as built carries no spoken primacy sentence to copy verbatim (specs_a.py :42-67, agenda-only per CKP-S3-2); the bounded formula above renders the guard-9 form of record — the implementer must reconcile the C19 notes pointer ("spoken as in A2") at build time.
- Script 7 → C17 notes/script "no number exists on any side before it runs" + "first campaign" — answers the listener's closing question with the only anchored statement available (no gain number claimed; abstention weakens nothing).
- "For the programmes" → "For the decision-makers" (register: same audience, plainer address; heads are labels, not claims).
- Figure → current fig spec (F-2/F-23: same naming as C13/s-38, legible size) — made explicit as a build requirement including the footer collision fix (Listener 1, layout defect).
- SENSE [45/C19] check: first per-phase variational method ✓ (on-slide bullet; spoken form bounded), measurable discarded operator ✓, source-by-source error budget ✓, affordable validation ✓; "honesty built into the method" carried by the closing band's content (limits with numbers or named roads) rather than by the word.

---

## CROSS-SLIDE CONSISTENCY NOTES (for the implementer)
1. "error source" / "source" is the single term replacing "channel" on all five slides; C11's table header, C17's card consequences, and C19's bullet all use it.
2. "route — partner or purchase" + "commit decided after step 1 / after the residual measurement" is the single plain form on C17 card 4 and C18 card 1 — the two slides must match verbatim (REFUTE (7)/(2) propagation: decision reserved, commitment never promised).
3. The ~1% substitution estimate appears twice (C11 row 5 "Designing the nozzle alone", C17 card 3 "the cost of designing alone") — both say what is substituted; values untouched.
4. "stop criterion … ~1% Isp → certification and operability" appears on C17 (band) and C19 (bullet + script): identical wording per F-1.
5. Gap letters (A/B) appear NOWHERE on any slide or script — words only ("formulation"/"model"/"the total"; "ours vs time-averaged"/"the true 3D optimum"), per FD-4/CW-4.
6. No dates on any slide (CKP-S3-5(b)): only "first campaign", "after the residual measurement / after step 1", "now", "later", "at your convenience".
7. Dropped from C11 on-slide (moved to script): "+0.51% ± ~30%" and "Rao 0.04–0.34%" — script 4–5 disambiguate the ± as relative and keep the Rao weld (F-15) intact after position 38.
8. Word budgets: C11 table+bullets and C17 cards+bands are trimmed to the REFUTE targets; any residual overrun (C11 honesty_table, C17 bands, C19 summary) is an explicit BUILD_LOG declaration by the implementer, never silent.

---

## LISTENER-2 CHECK (fresh first-time listener — ON-SLIDE text only)

Slide 42 [41/C11] — Takeaway: "The remaining error is broken down source by
source with best/worst numbers and how each was estimated; best case a few
percent, above 10% possible with strong swirl; two sources have no number
yet; the worst published signal is +13 points, unexplained; no benchmark
exists to check this, so they will measure it themselves."
**YES** — that is the SENSE contract: an honest per-source error budget with
evidence classes, single-digit best case, the +13-point marker on the table,
and no external referee — they close it or it stays open.

Slide 43 [42/C17-pre] — Takeaway: "Between averaged design, their design, and
the uncomputable true optimum sit a formulation distance, a model distance,
and the end-to-end total; they hypothesize — testably — that formulation
dominates, admit the wave-front jumps could overturn that, and the programme
fails only if two independent measurements both go against it."
**YES** — three gaps present, hypothesis stated as falsifiable with its weak
point on the same slide, two-independent-misses failure condition intact.

Slide 44 [43/C17] — Takeaway: "Four measurements in a fixed order — residual,
head-to-head, coupled pair, full 3D reference — each with consequences set
before the data, and a stop rule: below ~1% Isp gain they pivot to
certification and operability."
**YES** — four derivers in order with decision rules, stop criterion, and
outcomes fixed before data: the SENSE contract in engineering words.

Slide 45 [44/C18] — Takeaway: "They ask for three things — a route to a big
reference simulation, engine test data, and publication support — and their
method needs only engine specs to produce a design, with more data raising
confidence and bad data rejected (though the rejection is untried on real
data)."
**YES** — three concrete decision-ready requests plus the data-admission
answer to "what input does your method need", including the honest untried
admission.

Slide 46 [45/C19] — Takeaway: "First per-phase variational design method for
RDE nozzles; what it throws away is a measurable operator; errors are budgeted
source by source; checking a design takes minutes; the limits shown each carry
a number or a named way to get one."
**YES** — first-method claim, measurable discarded operator, per-source error
budget, affordable validation; the honesty-built-in thought arrives via the
band's content without the word being said.

### RESIDUAL RISKS
1. C19 word budget: ~66 net words vs the 60 cap and 5 bullets vs ≤3 — the
   two-column summary grammar mitigates, but the BUILD_LOG declaration is
   mandatory, not optional (REFUTE (12)).
2. C11 table: even after cell trims the honesty_table slide sits near/at the
   ~100 budget; if the build measures over, the layout exemption must be
   declared in BUILD_LOG (REFUTE (12) alternative), or cells trimmed further.
3. C19 spoken "first": the C19 notes pointer "spoken as in A2" has no target
   in the built A2 (agenda-only per CKP-S3-2) — the query-bounded formula
   here renders guard 9, but the dangling pointer must be reconciled at
   implementation (update the C19 note or restore a bounded primacy sentence
   in A2's script).
4. C19 closing band "each with a number, or the named way to get one" is a
   per-limit claim that must be re-verified against the final built slide
   set; if any stated limit lacks both, the band weakens further or the limit
   gains its road on-slide.
5. C11 row "first campaign measures it" is the only on-slide time-flavored
   phrase; it is CKP-S3-5(b)-safe (no date) but a listener may ask "when" —
   the answer lives in C17's order, two slides later.
6. Backup dependency: s-60 (full error table) is still a stub of record
   (F-3); C11's visual note promises it — delivery requires the build.
