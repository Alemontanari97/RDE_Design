# REWRITE v1 — final act (C11, C17-pre, C17, C18, C19)

Proposal only — of no effect until implemented in specs_c12.py / specs_c34.py,
assert-gate rebuilt, and user-gated (per BRIEF consumption arc). Rules applied:
CKP-S3-1 word caps, forbidden-register list, CKP-S3-5(b) no internal deadlines
on-slide, no new claims / no new numbers (weakening only), SENSE contracts
preserved in plain engineering words. Internal ids live in ANCHORS only.

Conventions: forbidden words eliminated on-slide AND in script ("channel" →
"source", "bracket" → "error band / error budget", "pre-registered" → "fixed
before the data arrive", "declared" → dropped or "stated", "honest(y)" →
shown, never said). Card headers sentence case (no ALL-CAPS).

---

## SLIDE [41/C11] (position 42) — replaces "The residual error, channel by channel"

### TITLE
Where the remaining error lives, source by source

### ON-SLIDE
Table (layout `honesty_table`, header: **error source | best case | worst case | how estimated**):

| error source | best case | worst case | how estimated |
|---|---|---|---|
| Mean azimuthal residual | exactly 0 | exactly 0 | proven (hypotheses stated) |
| Swirl thrust not in the model | 1.5% of thrust | 3% of thrust | order estimate |
| Input-data bias | 0.6% of pressure | 9% of pressure | order estimate + literature |
| Jumps at the wave fronts | no number yet — derivation planned | — | open |
| Substituting the coupled problem | ~1% | ~1% | literature, page-verified |
| Shift of the optimum | no number yet — first campaign measures it | — | open |

Bullets (3):
- Sources do not add into one figure: best case single-digit %; with strong swirl, above 10% not excluded.
- Largest published adverse signal: +13 points of ideal from a shroud, unexplained (Paxson & Miki 2022).
- No published benchmark separates this kind of prediction from the true unsteady flow — we measure it ourselves.

### VISUAL
Keep the existing six-row table + bullets grammar. One change of emphasis:
the two "no number yet" rows get a visibly lighter fill than the four
numbered rows, so the admission is read directly off the table (fact, not
narration), and the "how estimated" column uses only the plain words above.
Full table stays in backup (s-60, to be built per F-3).

### SCRIPT
1. This is our error budget: every source of error we know, its best and worst case, and how each number was obtained — a theorem, an order estimate, or a published datum.
2. Start with the two rows that have no number yet: the jumps at the wave fronts, and the shift of the optimum; for each, the derivation or the measurement that will produce the number is already in the plan you will see in two slides.
3. These sources do not add into a single figure — they are different physics at different confidence levels — so the summary is a band: best case, with weak swirl, single-digit percent overall is plausible; with strong swirl, more than ten percent is not excluded.
4. One computed case of ours gained +0.51 percent — and the uncertainty on that figure is about thirty percent of the value itself, so read it as roughly half a percent, not as a promise of more.
5. For scale: Rao's classical method is credited with 0.04 to 0.34 percent — their numbers, in their regime.
6. The largest published signal in the adverse direction: Paxson and Miki, 2022, add a shroud at fixed area ratio and the plug gains thirteen points of ideal — unexplained by the authors; if swirl content is doing that, it is exactly the worst row of this table.
7. And note what the literature does not contain: no published benchmark separates a phase-averaged prediction like ours from the true unsteady three-dimensional flow.
8. So nobody else can settle this table for us — the measurements that fill it are ours to make, and they come next.

### ANCHORS
- Table rows (all six, values unchanged) → notes [PROVENANCE] "Table cells -> CH3-feed-4 (classes per cell, forchetta §; CH7 PART 5 headline :1731-1743): mean channel THEOREM* (K-bar=0, perimeter H-RED-2); booking debt 1.5-3% [SE]; B1 0.6-9% p [SE]+lit; heel delta/L_H UNDERIVED -> CH3-feed-5 (SCHEMA + derivers named); sizing ~1% [REP]; optimum-shift no number (:1506)". Row relabels are plain-word renderings, no value changed: "booking debt" → "swirl thrust not in the model" (same 1.5–3% of thrust); "the heel" → "jumps at the wave fronts" (same open status, derivation road named); "sizing level" → "substituting the coupled problem" (same ~1%; substitution reading anchored by C17 card 3 "price of the substitution" + "~1% sizing stands").
- Bullet 1 → current bullet "Channels do not sum. Best case: single-digit %; off-axis, >10% not excluded." ("off-axis" → "with strong swirl": weakened plain form).
- Bullet 2 → current bullet + C12 notes "[REP] page-verified (findings_registry:2026; M0:1345, 1350-1353)".
- Bullet 3 + script 7 → notes "CT-3 STRICT form: no published referee THAT DISCRIMINATES the per-phase-averaged prediction against 3D-unsteady truth (restrictive clause binding for Q&A)" — restrictive clause kept on-slide ("this kind of prediction … from the true unsteady flow").
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

Gaps caption: two gaps in series — **formulation** (which problem you solve) · **model** (which physics you keep) — composing, end to end, into the total.

Band 1 (hypothesis + weak point, merged per F-11c):
Working hypothesis, testable: at fixed constraints the formulation gap dominates — three proven bounds sit on the model gap, none on formulation. Its weak point: the wave-front jumps carry no bound yet — if large, the model gap wins.

Band 2 (failure condition):
The method is wrong only if two independent measurements both go against it: the head-to-head comparison and the residual measurement.

### VISUAL
Keep the three-box chain with two gap arrows (mean-state → ours = formulation;
ours → 3D optimum = model) and a light end-to-end arc over both labeled
"composition"; two full-width bands below (already merged to two per F-11c).
The arrows carry the words "formulation" / "model" directly — no bare letters
anywhere (gap-letters map, FD-4/CW-4).

### SCRIPT
1. Three designs on one axis: a design built on the time-averaged flow; ours, built phase by phase; and the true three-dimensional optimum, which nobody can compute.
2. Between them, two gaps in series: a formulation gap — you asked the wrong question of the flow — and a model gap — you kept the wrong physics; end to end, the two compose into the total distance to the truth.
3. The value question of the whole enterprise is which of the two dominates.
4. Note the left comparison first: nobody has ever computed a time-averaged design against a phase-resolved one at equal constraints — us included; it is the first measurement on our plan.
5. Our working hypothesis — a hypothesis, not a theorem, and it can be proven wrong: at fixed constraints, the formulation gap dominates.
6. The grounds: three of the results you have already seen bound pieces of the model gap — the exact change of coordinates, the vanishing mean equation, the cleared full-state average — while nothing yet bounds the formulation gap.
7. The weak point travels with the hypothesis, on the same slide: the jumps at the wave fronts are the one unbounded first-order piece of the model gap — if they turn out large, the model gap dominates anyway.
8. And the method fails only if two independent measurements both go against it — the head-to-head and the residual measurement; each of them is on the plan that follows.

### ANCHORS
- Three designs / gaps frame → notes "[PROVENANCE] Three designs / three gaps -> CH6-feed-1 (scope 'in the record', repair WB1-C3-14) + CH6-feed-2 (hierarchy hypothesis)". "Composition" glossed only as the end-to-end composition of the two named gaps (definitional rendering of the three-gap frame; no third mechanism claimed — weakening).
- "never compared head-to-head, by anyone" → current column text "which nobody has computed in this head-to-head, us included" (sentence case per F-22).
- "the programme" → "this method" (register repair; same referent).
- Band 1 → current hypothesis band verbatim content; "declared, falsifiable" → "testable / can be proven wrong" (plain form); "three suppression results" → "three proven bounds" + script 6 lists them exactly as the current script does ("the three results you saw" — FD-5(ii) back-pointer kept).
- Heel co-presence on the SAME slide → notes "CH6-feed-3 (guard 1: hierarchy NEVER without the (J) heel — THIS slide is the enforcement site)": band 1 keeps hypothesis and weak point together.
- Band 2 → current death_line "Programme failure needs two independent misses — both measurable: head-to-head + residual measurement" ("misses" → "measurements going against it": plain form, same content) + notes "two-failure death -> CH6-feed-4".
- SENSE [42/C17-pre] check: three-design frame ✓, formulation-dominates hypothesis stated as falsifiable ✓, weak point co-present ✓, two-independent-misses failure condition ✓.

---

## SLIDE [43/C17] (position 44) — replaces "What tightens the bracket, in order — every outcome pre-registered"

### TITLE
Four measurements, in order — consequences fixed before the data

### ON-SLIDE
Four cards as ONE numbered left-to-right arrow sequence (F-11b):

1. **Residual** — how much the phase-averaged equations miss, on nozzles already solved. Small → error bars tighten; large → dominant source named. *First — cheapest.*
2. **Head-to-head** — our design vs time-averaged design, equal constraints; no such number exists yet. Either result publishable. *Machine ready — first campaign.*
3. **Coupled pair** — same nozzle with and without the combustor: the cost of designing the nozzle alone. ~1% holds → literature estimate stands; exceeded → step 4 moves up. *After step 1.*
4. **Full 3D reference** — ~12M-cell unsteady benchmark the field lacks. Prediction inside its band → confirmed; outside → failing source named. *Route chosen now; run committed after step 1.*

Band 1: Ours vs time-averaged: measurable in-house. Distance to the true 3D optimum: computable by no one — we bound it.

Band 2: Stop criterion: measured gain below ~1% Isp → effort pivots to certification and operability.

### VISUAL
Replace the 2×2 card grid with one numbered left-to-right arrow chain of four
compact cards (order IS the content, per F-11b), arrowheads between cards;
two slim full-width bands underneath (in-house vs bounded; stop criterion).
No Gap A / Gap B letters anywhere — the two distances are said in words in
band 1 (gap-letters map, FD-4/CW-4). Buildable with existing cards + arrows.

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
- Card 3 → current card 3 ("price of the substitution, on the field's template" → "same nozzle with and without the combustor: the cost of designing the nozzle alone" — plain rendering of the paired substitution run; "bar holds → ~1% sizing stands" → "~1% holds → literature estimate stands", same number, C11 row cross-consistent).
- Card 4 → current card 4 ("~12M-cell decider" kept as number; "today: channel, not commit" → "route chosen now; run committed after step 1", plain form; route = collaboration-or-procurement per C18 card 1).
- Band 1 → current gap_line with letters removed per notes "[GAP-LETTERS MAP - FD-4/CW-4] … in speech use the words, not bare letters".
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

1. **Reference 3D simulation** — What: ~12M-cell reference run, by collaboration or procurement. To decide: the route — partner or purchase; the run commits after the residual measurement. When: route now, run later.
2. **Engine test data** — What: high-speed pressure traces or hot-fire imaging. To decide: which rig, which instrumentation. When: starting now.
3. **Publication & access** — What: venues for the method papers; three key papers we cannot access. To decide: endorsement. When: at your convenience.

Band: "What input does the method need?" Specs suffice to produce a design; each added measurement raises the confidence grade (scale in backup). Input is screened on entry — data outside the required class is rejected, not absorbed. Not yet exercised on real data.

### VISUAL
Keep the three ask-cards with the What / To decide / When triplet (sentence
case, no ALL-CAPS), equal width — no fourth card (F-4). The reliability-ladder
mini-diagram moves to backup (F-4 option b); the band below the cards keeps
only the input question and the screening statement, with "scale in backup"
as the pointer.

### SCRIPT
1. Three requests — for each: what we ask, what you would need to decide, and when.
2. First, the reference simulation: today we ask only for the route — a collaboration or a procurement; the decision to actually run it comes after the residual measurement, exactly in the order of the plan you just saw.
3. Second, engine test data in the class the method needs: high-speed pressure traces or hot-fire imaging, sufficient to verify that stagnation temperature is flat over a cycle and to read the cycle frequency.
4. One property to be aware of: the input screen decides, it does not bless — it is built to reject data outside that class, and we expect real data to exercise it.
5. That screening has not yet been tried on a real dataset — we say that now rather than after the fact.
6. Third: publication venues for the method papers, and three key papers we currently cannot access.
7. And the question every panel asks — what input does your method need: engine specifications alone are enough to produce a design; every additional measurement raises the confidence grade of the result, on a scale spelled out in the backup.

### SCRIPT NOTE (register)
Script 5 replaces the on-slide parenthesis "(A contract prediction — not yet
exercised on real data.)": the admission stays, the software vocabulary goes.

### ANCHORS
- Card 1 → current card 1 ("the channel" → "the route — partner or purchase": plain form of "collaboration or procurement"; "the commit comes after the residual measurement" kept in words). No internal deadline (CKP-S3-5(b)).
- Card 2 → current card 2 verbatim content; "instrumentation window" → "which instrumentation" (register); stagnation-flatness + cycle-frequency detail in script 3 → current script verbatim content.
- Card 3 → current card 3 verbatim content.
- Band → current input_band: "Specs suffice to design" ✓; "climbs a declared reliability ladder" → "raises the confidence grade (scale in backup)" (ladder itself to backup per F-4 option b); "Data is not fed in: it is admitted — and the entry gate can say no" → "screened on entry — data outside the required class is rejected, not absorbed" (same content, courtroom metaphor removed); "(A contract prediction — not yet exercised on real data.)" → "Not yet exercised on real data." (F-8 form, per spine repair).
- Provenance of all band content → notes "[PROVENANCE] Specs-ladder Annex B -> CH10-feed-1 (stage P34 'prediction' declared — tag here, words on slide); G6 loud-reject never exercised -> CH10-feed-2; TRIPLE monitor -> CH7-feed-5" (script 4 "decides, does not bless" is the current script's own wording).
- Open-items remain OFF-slide in backup (F-4, current notes) — unchanged here.
- SENSE [44/C18] check: three concrete requests ✓ (reference-class run, engine data in the stated class, publication/procurement) + the data-admission answer to "what input does your method need" ✓ — all in engineering words.

---

## SLIDE [45/C19] (position 46) — replaces "A method you can audit — fast enough to validate economically"

### TITLE
Every approximation is measurable — validation costs minutes, not weeks

### ON-SLIDE
**For the engineers**
- the first per-phase variational design method for RDE nozzles
- what the reduction discards is an explicit, measurable operator
- an error budget, source by source, each with how it was estimated

**For the decision-makers**
- validation in minutes, not weeks
- a stepwise plan with known costs, fixed consequences, and a stop criterion

Closing band: Every limit of the method is on these slides — with a number, or the named way to get one.

Figure: pipeline reprise, legible height, stage names identical to the machine slide (s-38).

### VISUAL
Keep the two-column summary (engineers / decision-makers) over a single
closing band. Fix the layout defect: enlarge the pipeline miniature to a
legible height, reuse the machine slide's stage naming verbatim (F-2/F-23),
and clear it from the footer banner so nothing collides. This reprise is the
bookend: first slide of the machine, last slide of the talk, same picture.

### SCRIPT
1. Two things to retain.
2. For the engineers: this is the first per-phase variational design method for RDE nozzles.
3. What the reduction throws away is not hand-waved — it is an explicit operator you can evaluate, so the approximation itself is measurable.
4. The error budget is stated source by source, each entry with how it was estimated — a theorem, an order estimate, or a published datum — and where there is no number yet, the way to get one is named.
5. For the decision-makers: the machine validates a design in minutes, not weeks — so testing this method is cheap.
6. The plan is stepwise, its costs are known, and the consequence of each possible outcome is fixed before the data arrive — including the point where we would stop: below about one percent of measured Isp gain, effort pivots to certification and operability.
7. How much better a nozzle designed this way will fly, nobody yet knows — no number exists, on any side, until the head-to-head runs; it is the first measurement of the campaign.
8. That number is what we came here to go and get. Thank you.

### ANCHORS
- Title → fusion of two current on-slide elements, no new claim: "fast enough to validate economically" + "what the reduction discards is an explicit, measurable operator"; "audit" (forbidden) removed; "minutes, not weeks" kept, "economic act(s)" dropped (F-21, per spine repair).
- Engineers bullets 1–2 → current eng_bullets 1–2 verbatim ("MEASURABLE" already to sentence case per F-22). "First" spoken in D-06 locked, query-bounded form as in A2 (notes, guard 9).
- Engineers bullet 3 → current bullet 3 "an honest error bracket, channel by channel, each cell with its evidence level" → "an error budget, source by source, each with how it was estimated" (forbidden words removed; content identical, weaker if anything).
- Decision-makers bullet 2 → current prog_bullet 2 "an incremental plan, already priced, with pre-registered outcomes — and a declared stop criterion" → "a stepwise plan with known costs, fixed consequences, and a stop criterion" (three process words removed, content identical; stop criterion wording consistent with position 44, per F-1 repair).
- Closing band → current closing "limits stated on the slides, with their evidence levels" + C11's "no number yet — derivation road named" rows → "with a number, or the named way to get one". The "honesty is not a disclaimer" sentence is deleted, not translated: the band shows the property instead of naming it (notes provenance: instrumented honesty -> CH6-feed-10, D-44/P34/card discipline; dual takeaway -> MESSAGE_ARCHITECTURE).
- Figure → current fig spec (F-2/F-23: same naming as C13/s-38, legible size) — made explicit as a build requirement including the footer collision fix (Listener 1, layout defect).
- Script 7 → C17 notes/script "no number exists on any side before it runs" + "first campaign" — answers the listener's closing question with the only anchored statement available (no gain number is claimed; abstention is stated, which weakens nothing).
- "For the programmes" → "For the decision-makers" (register: same audience, plainer address; heads are labels, not claims).
- SENSE [45/C19] check: first per-phase variational method ✓, measurable discarded operator ✓, source-by-source error budget ✓, affordable validation ✓; "honesty built into the method" is carried by the closing band's content (limits on the slides, with numbers or named roads) rather than by the word — the listener ends thinking the thought without being told to.

---

## CROSS-SLIDE CONSISTENCY NOTES (for the implementer)
1. "error source" is the single term replacing "channel" on all five slides; C11's table header, C17's card consequences, and C19's bullet all use it.
2. "route — partner or purchase" is the single plain form replacing "channel (collaboration/procurement)" on C17 card 4 and C18 card 1 — the two slides must match verbatim.
3. The ~1% substitution estimate appears twice (C11 row 5, C17 card 3) — both now say what is substituted (the coupled problem / designing the nozzle alone); values untouched.
4. "stop criterion … ~1% Isp → certification and operability" appears on C17 (band) and C19 (bullet + script): identical wording per F-1.
5. Gap letters (A/B, historical or frame) appear NOWHERE on any slide or script — words only ("formulation"/"model"; "ours vs time-averaged"/"distance to the true 3D optimum"), per FD-4/CW-4.
6. No dates on any slide (CKP-S3-5(b)): only "first campaign", "after the residual measurement / after step 1", "now", "later", "at your convenience".
7. Dropped from C11 on-slide (moved to script): "+0.51% ± ~30%" and "Rao 0.04–0.34%" — script 4–5 disambiguate the ± as relative and keep the Rao weld (F-15) intact after position 38.
