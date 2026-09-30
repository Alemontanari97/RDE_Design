# REFUTE_LOTB_v1 — adversarial refutation of REWRITE_LOTB_v1 (s-27..s-33, minus s-28)

**Confronto/record stage**: REWRITE_LOTB_v1.md vs specs_c12.py notes [PROVENANCE]
+ rigor classes (ceiling), NARRATIVE_SPINE_v2.md blocks [27]..[33], BRIEF.md HARD
RULES, BRIEF_LOTB.md orders. Independent verifications run in-window:
specs_a.py:179, eqs_spres.py:49, ADVISORY_generality_litmap_2026-08-12.md:58,
specs_c12.py C9/error-budget swirl rows (:648-660, :751-758).
**Consumption arc**: this file → S4 orchestrator applies repairs before
implementing REWRITE_LOTB into specs_c12.py → assert-gated rebuild → CKP-S4-1
listener → user gate.

**Ruling used throughout (declared)**: the forbidden word "phase" is read in its
meta/process sense (programme phase, ESA Phase-A/B/C — spine F-9). Technical
uses ("per-phase", "cycle phase", "no single phase", "peak-phase") are the
deck's subject and are NOT register hits; the rewrite correctly purged the one
programme-phase use ("first campaign of the phase" → "its first task").

**Status-inflation sweep (the killing class) — verdict: ZERO upgrades found.**
Every "proven" was checked against the notes class:
- s-30 band L2 ← THEOREM* [T-T7FS(b)] (CH2-feed-1): correct ceiling; adds a
  limit-clause the current band lacks → weakening.
- s-31 p1 L1 ← THEOREM [T-T7RED] (CH1-feed-3): correct; current slide says bare
  "proven" → L1 is equal-or-weaker.
- s-31 p2 L2 ← THEOREM* [T-T4]: correct ("perimeter declared" → "within stated
  limits", same class, rule-clean).
- s-31 p3 L2 ← THEOREM* [T-T4] break: WEAKER than the current bare "proven" →
  correct direction.
- s-32 card L3 ← SCHEMA route S1 (CH1-feed-2): correct; "(one building block
  proven)" ← [T-T0P-E] THEOREM leg — anchored, not an upgrade (THEOREM is the
  top class; bare "proven" for it is within ceiling).
- s-32 card echo of s-30 theorem at L2 ← CH2-feed-1 THEOREM*: correct.
- Spoken "provably coincide"/"provably breaks" (s-31 script 5/9) — matches the
  current notes SCRIPT ("coincide by construction"/"the coincidence breaks,
  proven") and spine SENSE ("provably BREAK"); chips carry the class on-slide.
- s-33 verdict band carries NO status stamp and drops "pointwise" — weakening;
  none invented (correct: notes give no single class for the verdict).
The Order-B vocabulary substitution ("perimeter declared" → "within stated
limits") is a legitimate register-clean equivalent, not a content change.

---

## SLIDE s-27 (C6) — verdict table

### ON-SLIDE
| # | Statement | Verdict | Notes |
|---|---|---|---|
| 1 | 1958 Rao box (caps EMERGES dropped) | PASS | anchor: C6 timeline; F-22 |
| 2 | 1967 Hoffman box "the adjoint before it had a name" | PASS | decode of "ante litteram" per audit |
| 3 | 1970 K-O box "a time-weighted wall, **the closest ancestor**: no cycle average, no per-phase family, no error control" | **UNANCHORED** | "the closest ancestor" is nowhere in the anchor set AND collides with the record: specs_a.py:179 gives "closest ancestor of our per-phase view" to the **wave-frame MoC** (Fievisohn line), and s-29 names Fievisohn "the closest cousin". Two "closest" relatives = a panel catch. The decode triple ("no cycle average / no per-phase family / no error control" ← "no cycle measure / no quotient / no certificates") itself is a fair weakening — PASS on that half. |
| 4 | 1981 box "maximum-thrust contours by direct optimization of the parameters" | **UNANCHORED (minor, anchor-citation repair)** | Not in C6 notes or spine; the rewrite's own anchor ("the cited work's own subject") is not a [PROVENANCE] pointer. The anchor EXISTS on disk — ADVISORY_generality_litmap_2026-08-12.md:58 (Allman_Hoffman_1981.pdf = AIAA J 19(6):750-751) whose title is "Design of maximum thrust nozzle contours by direct optimization methods". Statement is true and cite-backed; the ANCHORS block must cite the litmap row, not "the work's own subject". |
| 5 | 1994–2002 Kraiko–Tillyaeva box | PASS | anchor: C6 timeline verbatim minus "&" |
| 6 | "now" box "the same line, carried to the periodic exhaust" | PASS | "extended to the periodic system" → "carried to the periodic exhaust": decode; spine title keeps "periodic system" — acceptable variation, sense identical |
| 7 | Rao Eq. 14 strip + caption (kept, re-anchored under 1958 box) | PASS | anchor: C6 eq_fig verbatim |
| 8 | Footline deleted from slide, verbatim to notes | PASS | Order D executes exactly this; spine SENSE "procurement gaps declared" survives in script 9 + notes — declared divergence from spine footline repair F-8, ordered by the later-binding brief |

### SCRIPT
| # | Sentence | Verdict |
|---|---|---|
| 1 | "We are not inventing a genre; we inherit one." | PASS (notes verbatim) |
| 2 | Rao '58 + transversality pointer | PASS (notes + eq caption) |
| 3 | Hoffman '67 multiplier fields / adjoint before the name | PASS (notes verbatim) |
| 4 | Allman–Hoffman direct route | PASS (notes "for the direct route"; "optimize the contour parameters directly" covered by litmap row once cited) |
| 5 | Kraiko–Tillyaeva school field adjoint | PASS (notes) |
| 6 | K-O 1970 "the ancestor we always cite" | PASS (notes verbatim — NOTE: the script keeps the RIGHT epithet; only the on-slide box drifted to "closest") |
| 7 | "no cycle average, no per-phase family, no error control" | PASS (decode of notes "cycle measure / quotient / certificates") |
| 8 | "We extend this line to the periodic exhaust." | PASS (notes) |
| 9 | 1975 on order; "we say so, and we do not summarize what we have not read" | PASS (notes verbatim; "we say so" is spoken, not on-slide — HARD RULE 2 governs on-slide only) |

### REPAIRS (word-exact)
- **R27-1 (box 3)**: replace "a time-weighted wall, the closest ancestor:" with
  **"a time-weighted wall — the ancestor we always cite:"** (matches notes and
  current box; removes the collision with specs_a.py:179 and s-29's "closest
  cousin"; +1 word, box stays ≤ current length).
- **R27-2 (ANCHORS block, 1981 box)**: replace the anchor line with:
  **"1981 box expansion → ADVISORY_generality_litmap_2026-08-12.md:58
  (Allman_Hoffman_1981, AIAA J 19(6):750-751; title: maximum-thrust nozzle
  contours by direct optimization methods) — box text = title decode, no claim
  about results."**

---

## SLIDE s-29 (C7-bis-pre) — verdict table

### ON-SLIDE
| # | Statement | Verdict | Notes |
|---|---|---|---|
| 1 | Title "…and we name them" | PASS | "declare"→"name" forced by HARD RULE 2; SENSE intact |
| 2 | Stechmann card "0-D blowdown per phase, mass-weighted mean — nozzle families fixed" | **SENSE-LOST (minor)** | The anchor says "DECLARED mass-weighted mean" — Stechmann's credit is that he STATES his weight, the exact contrast with Harroun's "with which weight?". Dropping the adjective deletes the contrast the two cards are built on. "declared" is forbidden; "stated" is not. |
| 3 | Harroun card "…thrust coefficients then averaged — with which weight?" | PASS | softening of "the weight is undeclared" to question form — Order C-compatible; non-commuting clause rerouted to the band (anchored) |
| 4 | Fievisohn card "characteristics in the wave frame, the closest cousin — no design, no shape family" | PASS | anchor verbatim + audit grammar repair |
| 5 | Band: eq_ratio_mean centerpiece + caption "the mean of a ratio is not the ratio of the means — on 10:1 cycles the bias is first-order in the variance" | PASS | Order C executed; caption = notes SCRIPT ("ten-to-one cycles, bias first order in the variance") — no new number |
| 6 | Claim line "…the variational optimum on the family of per-phase flows sharing one wall — to our literature search, never posed before." | PASS | query bound promoted ON-slide (weakening, guard 9); family definition = C7-bis notes decode ("family sharing one wall") — cross-slide anchor, legitimate |

### SCRIPT
| # | Sentence | Verdict |
|---|---|---|
| 1 | "named by us before you ask; two of the three come from this group's collaborators at Purdue" | PASS ("both ancestors" of the notes disambiguated to "two of the three" — LL-2/LL-3; faithful decode) |
| 2 | Stechmann: zero-D blowdown, stated mass-weighted mean, families fixed | PASS (notes; "stated" replaces forbidden-on-slide "declared" — spoken either way is fine, wording anchored) |
| 3 | Harroun: 2-D axi per pressure ratio, average the coefficients | PASS (notes) |
| 4 | "the mean of a ratio is not the ratio of the means" | PASS (notes "does not commute" decode + eq content) |
| 5 | 10:1 bias first order in variance; weight not stated; "question we pose formally, with the source verification assigned" | PASS (notes + W-B.0) |
| 6 | Fievisohn closest cousin, BC met in code section | PASS (notes verbatim) |
| 7 | "the pieces exist in the field; the edifice does not" | PASS (weakening decode of "the quotient exists in the field; the edifice does not") |
| 8 | family definition | PASS (C7-bis notes) |
| 9 | variational optimum on that family, query-bounded | PASS (notes) |
| 10 | "our simplest rung is exactly Stechmann's reduction level, with the right mean proven" | PASS (notes SCRIPT verbatim, guard 2/3 respected — spoken in the current deck too, no change of level) |

### REPAIRS (word-exact)
- **R29-1 (card 1)**: replace "0-D blowdown per phase, mass-weighted mean —
  nozzle families fixed" with **"0-D blowdown per phase, stated mass-weighted
  mean — nozzle families fixed"** (+1 word; restores the stated-vs-unstated
  weight contrast; "stated" is rule-clean; budget stays ≈ 89 < 100).

---

## SLIDE s-30 (C7-bis, PROTECTED) — verdict table

### ON-SLIDE
| # | Statement | Verdict | Notes |
|---|---|---|---|
| 1 | Left head "The field: average first" (caps dropped) | PASS | F-22 |
| 2 | Left chain incl. "the optimum of a SUBSTITUTE problem" | PASS | SUBSTITUTE = the one kept cap (spine F-22, brief exception) |
| 3 | Left foot "the optimum's location — no error bar" | PASS | decode of "the error on the argmax has no bar" per audit |
| 4 | Right head "Us: formulate the periodic optimum" | PASS | F-22 |
| 5 | Right chain: "per-phase family — one wall shared by every phase" / "its own optimality conditions, averaged" ("corner" off-slide) | PASS | shared-wall decode ← notes SCRIPT; corner removal = declared weakening, kept in script 4 |
| 6 | Right foot "to our literature search: never written before" | PASS | query bound promoted on-slide (weakening, guard 9) |
| 7 | Eq strips + legend "ξ = cycle phase · dμ(ξ) = its weight in the mean · Σ = the shared wall" | PASS | = AUDIT_SYNTHESIS row 12 prescribed repair almost verbatim. RESIDUAL (named): row 12 also lists G_ξ, λ_L, g_L — still undefined on-slide; the audit's own proposed legend covered only ξ/μ/Σ, so the rewrite matches the prescribed repair; route the rest to notes explicitly (repair R30-3). |
| 8 | "a. e." dropped from strip annotation | PASS + IMPLEMENTATION NOTE | the annotation is BAKED INTO the rendered equation (eqs_spres.py:49: `a.e.\ on\ the\ shared\ wall`) — dropping it requires regenerating eq_avg_wall.png, not a layout edit; content change = precision weakening only, allowed |
| 9 | Theorem band with L2 stamp | PASS | THEOREM* ceiling respected; band text otherwise = current verbatim; promoted weight kept (F-10) |

**Slide-level — BUDGET: REGISTER-HIT.** Claimed ≈ 99; refuter recount ≈ 104-112
(head+chain+foot 29 left + 41 right, legend 13, band 29) depending on whether
symbols (ξ, dμ(ξ), Σ) count as words. Over the 100 cards cap on the
straightforward count. See R30-1/R30-2.

**Slide-level — PROTECTION: no hit, one GATE FLAG.** Fork and promoted band
intact; s-28 untouched. But the eq-strip migration into the right column
exceeds the brief's literal "repairs are register/wording/definition only". It
is legitimized by AUDIT_SYNTHESIS row 12 ("anchor equations to their columns")
— name it explicitly at the S4 gate as an audit-directed structural repair;
fallback if refused: keep strips in place, put the legend beneath them there.

### SCRIPT
| # | Sentence | Verdict |
|---|---|---|
| 1 | "The heart slide." | PASS (notes verbatim) |
| 2 | field's route incl. "the best of the four papers you saw" | PASS (notes "the best of those four papers") |
| 3 | "the optimum of a substitute problem" | PASS (notes) |
| 4 | ours: family sharing one wall, functional, transversality + corner averaged | PASS (notes verbatim) |
| 5 | symbol walk (ξ, dμ, Σ) | PASS (decode of on-slide legend; audit-directed) |
| 6 | "To our literature search, these conditions were never written before." | PASS ("census" → "literature search": internal-vocabulary decode, bound kept) |
| 7 | read the band verbatim | PASS (F-10 speech duty verbatim) |
| 8 | "proven, within stated limits — the hypotheses travel with it" | PASS (L2 decode; THEOREM* = proven under stated hypotheses — no upgrade) |
| 9 | take-away "optimal at no single operating point" | PASS (F-10 duty verbatim) |

### REPAIRS (word-exact)
- **R30-1 (legend)**: shorten to **"ξ = phase · dμ = its weight · Σ = the
  shared wall"** (audit row 12's own compact form; −3 words; "cycle" survives
  in script 5).
- **R30-2 (right chain item)**: "per-phase family — one wall shared by every
  phase" → **"per-phase family — one shared wall"** (−3 words; full clause
  stays in script 4 and s-29 claim line). With R30-1+R30-2 the recount lands
  ≈ 98-106 → re-measure at build with the deck's counting convention (SR-12:
  measured command, not inherited estimate); if still > 100, drop the left
  chain word "problem" after SUBSTITUTE (the cap carries it).
- **R30-3 (notes)**: add one notes line: "Remaining symbols (G_ξ, λ_L, g_L) =
  phase-flow and multiplier fields — defined here, deliberately not on-slide."

---

## SLIDE s-31 (C7-ter, full rebuild per Order A) — verdict table

### ON-SLIDE
| # | Statement | Verdict | Notes |
|---|---|---|---|
| 1 | Question band (per-phase vs classical on cycle-mean p₀,T₀, same constraints, no swirl, contour + thrust question) | PASS | Order A wording, faithful transcription; user order = the anchor |
| 2 | Panel 1: label + chip L1 + verdict "with the proven mean the designs coincide; the wrong mean shifts **the optimum** +44–87%" | **STRENGTHENED** | The measured shift is of the optimum **area ratio** (CH2-feed-3; current slide: "moves the optimum area ratio by +44–87%"). Dropping "area ratio" generalizes the number to "the optimum" tout court — exactly the over-reading the panel would punish. Chip + right/wrong-mean split otherwise PASS (T-T7RED, T1c). |
| 3 | Panel 2: "full adapted plug / coincide — proven, within stated limits / the peak-phase design is optimal" | PASS | THEOREM* [T-T4]; class-correct |
| 4 | Panel 3: "truncated plug — our configuration / the coincidence breaks — proven, within stated limits / the averaged problem opens here" | PASS | weaker than current bare "proven"; "first genuinely averaged" primacy correctly left in locked form D-06 (notes only); TRUNCATED caps dropped (F-22) |
| 5 | Answer band: "Measured so far: 3–10 s of Isp from the mean alone. At contouring the size is open — not presumed small. The tool is ready; this comparison is its first task." | PASS | 3–10 s anchored (dIsp +3.33..+9.71); "not presumed small" anchored; F-9 repair applied ("phase" purged); twin PB-2 (b) form preserved: no pre-milestone number |
| 6 | New figure spec fig_c7ter_threeconfig.png | **UNANCHORED (minor, figure spec)** | "same spike cut at **~60% length**" plants an unanchored geometric fraction in a panel labeled "our configuration" — no record anchor for 60% truncation. Rest of the spec (three configurations, chips, dashed = not designed) PASS and answers the audit's missing-picture finding. |

**Slide-level — BUDGET: REGISTER-HIT.** Claimed ≈ 97; refuter recount ≈ 108
(band 24 + panels 23/14/17 + answer band 30), > 100 cards cap even before
counting sub-labels inside the figure. See R31-2.

### SCRIPT
| # | Sentence | Verdict |
|---|---|---|
| 1 | "the programme's deciding question, stated head-to-head" | PASS (Order A) |
| 2 | classical on cycle-mean p₀,T₀ vs per-phase, identical constraints, "set swirl aside — it gets its own slide" | PASS — VERIFIED: swirl does get its own slide (C9, position 34: same gauge, one flow swirls, thrust differs 1.5–3%; specs_c12.py:648-660) plus the error-budget swirl row (:751) |
| 3 | does the contour move, how much thrust | PASS (Order A) |
| 4 | "three settings" | PASS (panel map) |
| 5 | rung 1 coincide if fed the proven weighted mean | PASS (T-T7RED + T1c "right mean proven"; conditional stated, no upgrade) |
| 6 | "+44–87% … three to ten seconds … numerical test bench with rejecting checks" | PASS (CH2-feed-3 verbatim incl. FD-5(i) wording; says "optimum area ratio" correctly — the script has what the panel verdict lost) |
| 7 | no-contradiction sentence (coincidence about problems, shift about wrong mean) | PASS (decode of notes "coincide by construction; even there, the wrong mean moves…") |
| 8 | full plug: coincide within stated limits, peak-phase optimal | PASS |
| 9 | truncated plug: provably breaks, genuinely averaged optimum | PASS (notes verbatim) |
| 10 | "the answer in form: the two designs part ways" | PASS (Order A decode) |
| 11 | "not presume it small: ten-to-one at the inlet, about six-to-one at the throat" | PASS (CH5-feed-9; third ratio correctly notes-only) |
| 12 | "tool ready; first task" | PASS (PB-2 (b) form) |

NOTE (named, no class): the Humphreys caveat of the current notes ("a pattern,
not the proof of the general case") does not survive in the script. Sentence 7
carries the same protective work and sentence 6 keeps the bench scoping, so no
strengthening results — but the Q&A notes should retain the Humphreys line
verbatim (it is the pre-cooked answer if a panelist generalizes rung 1).

### REPAIRS (word-exact)
- **R31-1 (panel 1 verdict)**: replace with **"coincide with the proven mean;
  the wrong mean shifts the optimum area ratio +44–87%"** (restores the
  measured quantity; net word count unchanged vs original panel text).
- **R31-2 (budget)**: apply BOTH: question band → **"Per-phase vs classical
  design on cycle-mean p₀, T₀ — same constraints, no swirl: does the contour
  move, and what thrust rides on it?"** (−3); answer band → **"Measured so
  far: 3–10 s of Isp from the mean alone. At contouring: open — not presumed
  small. The tool is ready — this is its first task."** (−4). Then re-measure
  with the build's counting convention (SR-12); if still > 100, shorten panel-3
  verdict to "the averaged problem opens" (−1) and panel-1 label to "area
  ratio only" (−2).
- **R31-3 (figure spec)**: replace "same spike cut at ~60% length" with
  **"same spike truncated partway (illustrative fraction — schematic, not to
  scale)"**, and add "schematic — not to scale" to the figure's corner
  annotation so no panelist reads geometry off it.

---

## SLIDE s-32 (C8) — verdict table

### ON-SLIDE
| # | Statement | Verdict | Notes |
|---|---|---|---|
| 1 | Title "Per-phase is a change of coordinates, not an approximation" | PASS | reorder of current title; SENSE identical; 9 words |
| 2 | Bullet 1 "Pure rotating wave: the flow is steady in the wave frame — azimuth becomes phase." | PASS | "azimuth becomes phase" = decode of the change-of-coordinates content (quotient); AUDIT row prescribes "ξ = phase" vocabulary; no new claim |
| 3 | Bullet 2 "One approximation enters, of Strouhal order (wave period vs transit time) — hypotheses stated." | PASS | O(St) anchored (CH1-feed-2); parenthetical = standard-definition decode the audit demanded; "declared"→"stated" rule-clean |
| 4 | Bullet 3 "The global time average mixes the phases — the cruder reduction, the field's." | PASS | current bullet decode ("not ours" → "the field's") |
| 5 | Status card (L3 for the equivalence + one block proven + s-30 theorem echoed at L2) | PASS content / see divergence | classes correct (SCHEMA→L3; [T-T0P-E] THEOREM leg; CH2-feed-1 THEOREM*→L2); Order B scoping executed; **:1450 verbatim-stable tag divergence is properly DECLARED in the rewrite and routed to user ratification — required, keep the flag** |

**Slide-level — BUDGET: REGISTER-HIT.** fig_bullets layout ⇒ cap 60. Refuter
count: bullets 39 + card 28 = **67** (> 60), before figure callouts (~16).
The rewrite's own "≈ 60" undercounts. See R32-1.

### SCRIPT
| # | Sentence | Verdict |
|---|---|---|
| 1 | "Is per-phase itself an approximation? No — and that must be said precisely." | PASS (spine BRIDGE verbatim) |
| 2 | primer recall: steady in the wave frame | PASS (notes) |
| 3 | stated data class, T0-flatness monitor, azimuth becomes phase | PASS (notes; scope pin) |
| 4 | change of coordinates, exact up to one approximation | PASS (notes; "quotient" correctly kept off the spoken line — lives in notes) |
| 5 | Strouhal order, hypotheses printed | PASS (notes verbatim) |
| 6 | global average mixes phases — cruder reduction, theirs | PASS (notes) |
| 7 | "Now the status, precisely scoped." | PASS (Order B) |
| 8 | proof route laid out, one block proven, completion in progress, "we say exactly that" | PASS (L3 + THEOREM leg; honesty device spoken, not narrated on-slide) |
| 9 | previous slide's theorem separate, proven within stated limits | PASS (CH2-feed-1, L2) |

### REPAIRS (word-exact)
- **R32-1 (status card, −10 words → total 57 ≤ 60)**: replace the card text
  with **"This equivalence: proof laid out, completion in progress. The
  previous slide's theorem is separate: proven, within stated limits."**
  — "(one building block proven)" moves to script only (already sentence 8:
  "one building block is already proven"), and the head-word "Status —" is
  carried by the card's visual role, not by text. No content lost from the
  slide+script pair; the L3/L2 scoping the Order demands stays on-slide.

---

## SLIDE s-33 (C8-bis) — verdict table

### ON-SLIDE
| # | Statement | Verdict | Notes |
|---|---|---|---|
| 1 | Title (unchanged) | PASS | |
| 2 | Bullet 1 "The design variable: one solid body in an envelope — classes emerge, not presupposed." | PASS | current bullet 1 headline cut (F-14) |
| 3 | Bullet 2 "Finitely many classes: the global optimum is the best of the class optima." | PASS | tournament decode; "sector"→"class" per Order E; guarantee clause routed to script 5 (declared weakening) |
| 4 | Bullet 3 "**Smooth** splines per class — no vanishing bodies: in supersonic flow they buy only wave drag." | **UNANCHORED (minor)** | anchor says "certified splines" (CH8-feed-9 / LL-29). "Smooth" is a DIFFERENT property, found nowhere in the anchor; it silently substitutes a mathematical attribute for the certification attribute. Not a strengthening — but not a decode either. |
| 5 | Verdict band "First verdict: the plug matches or beats the bell — on checked flow models at equal area ratio, never hardware; ties mapped." | PASS | "matches or beats" = exact plain decode of "weakly dominates"; "checked flow models" ← "certified closures" (Order E demands the decode); "pointwise" dropped = weakening; "on record" correctly purged; Order E headline promotion executed |
| 6 | State line "Today the optimizer runs one class — bell, nine design parameters; truncated plug and shrouded follow." | PASS | CH8-feed-8 decode; "honest state / owners / windows / named campaigns / 9 DOF driver" fully purged; "follow" weaker than spine's "assigned, with dates" — allowed |
| 7 | Rebuilt figure spec fig_c8bis_envelope.png | PASS | all elements anchored (lip attachment + uniform-cone pin ← CH8-feed-1; four class icons ← bullet classes; chips ← state line + "our configuration"); no ledger text — Order F satisfied |

**Slide-level — BUDGET: borderline REGISTER-HIT (adjudication needed).** The
rewrite claims the 100 cards cap; the layout is 3 bullets + band + state line
= bullets layout on the letter of HARD RULE 1 ⇒ cap 60. Refuter count: 13+13+15
(bullets, each ≤15 ✓) + 21 (band) + 15 (state line) = **77**. Precedent cuts
both ways (s-30 counts band toward a 100 cap). Orchestrator must adjudicate
the cap class at the gate; trims below get to 68 if 60 is ruled.

### SCRIPT
| # | Sentence | Verdict |
|---|---|---|
| 1 | "What do we actually optimize over?" | PASS (notes verbatim) |
| 2 | solid body in envelope, attached at the cowl lip | PASS (notes + CH8-feed-1) |
| 3 | classes not menu choices — classes the result falls into | PASS (notes decode, "topological" dropped = weakening) |
| 4 | finitely many ⇒ global optimum = best of finitely many class optima | PASS (notes decode) |
| 5 | "whenever we say 'optimum', the argument that guarantees it travels with it" | PASS (CH8-feed-4 decode; "how strong" dropped = weakening; sigle in notes — guard 8) |
| 6 | ranking at the reduced rung: plug matches or beats bell, tie region mapped | PASS (notes) |
| 7 | scope: checked flow models at equal area ratio, never hardware | PASS (notes F-14 qualifier verbatim-equivalent) |
| 8 | smooth splines + refused vanishing-body tricks + wave-drag reason | PASS spoken (the wave-drag argument is notes-verbatim; same "smooth" caveat as bullet 3 — repair below covers both) |
| 9 | one class today — bell, nine design parameters | PASS (notes decode) |
| 10 | truncated plug and shrouded next in line | PASS (notes "named campaigns" weakened) |

### REPAIRS (word-exact)
- **R33-1 (bullet 3 + script 8)**: replace "Smooth splines per class" with
  **"Splines per class"** (−1 word each; drops the unanchored attribute; the
  certification content already lives in notes via LL-29 and must not surface
  as bare "certified" per Order E). Bullet 3 becomes: **"Splines per class —
  no vanishing bodies: in supersonic flow they buy only wave drag."** (14
  words, ≤15 ✓).
- **R33-2 (budget, only if the 60 cap is ruled at the gate)**: state line →
  **"Today: one class running — bell, nine parameters; truncated plug and
  shrouded next."** (−3); band → **"First verdict: the plug matches or beats
  the bell — checked flow models, equal area ratio, never hardware; ties
  mapped."** (−2). Lands at 68; further cuts would lose anchored content —
  if 60 is enforced strictly, move the state line into the figure (chip text
  already carries "running — 9 parameters" + "our configuration") and delete
  it as a text line (−12 ⇒ 56).

---

## STATUS VOCABULARY TABLE (rewrite header) — verdict

| Item | Verdict |
|---|---|
| L1/L2/L3 ladder, classes as ceiling | PASS (verified per stamp; zero upgrades — see sweep at top) |
| "perimeter declared" → "within stated limits" substitution | PASS (register-forced, content-equivalent, divergence from Order B's example wording is itself declared in the rewrite) |
| Identical wording wherever stamped | PASS (checked s-30 band, s-31 chips ×3, s-32 card ×2 — no third phrasing appears) |

---

## FINAL COUNTS

Statements graded: 39 on-slide items + 59 script sentences = **98 rows**, plus
4 slide-level budget checks and 1 protection check.

| Class | Count | Where |
|---|---|---|
| PASS | 92 of 98 rows | everywhere else |
| STRENGTHENED | **1** | s-31 panel 1 verdict ("the optimum" without "area ratio" — generalizes a measured number; repair R31-1) |
| UNANCHORED | **3** | s-27 box 3 "the closest ancestor" (collides with specs_a.py:179; repair R27-1); s-31 figure spec "~60% length" (repair R31-3); s-33 "smooth splines" (repair R33-1). Plus 1 anchor-citation defect, statement itself cite-backed: s-27 box 4 (repair R27-2). |
| REGISTER-HIT | **3 + 1 borderline** (slide-level budgets) | s-30 ≈104-112 > 100 (R30-1/2); s-31 ≈108 > 100 (R31-2); s-32 67 > 60 (R32-1); s-33 77 — cap class needs gate adjudication (R33-2). Zero forbidden-word hits; zero illegal ALL-CAPS (SUBSTITUTE = the one kept cap, verified unique). |
| SENSE-LOST | **1** | s-29 card 1 (stated-mean contrast; repair R29-1) |
| PROTECTION-HIT | **0** | s-30 fork + promoted band intact, s-28 untouched. One GATE FLAG: eq-strip migration exceeds "register/wording/definition only" literally, legitimized by AUDIT_SYNTHESIS row 12 — must be named at the S4 gate (fallback provided). |

**Killing-class verdict: NO status inflation found** — all six stamps and both
spoken "provably" match or weaken their notes-class ceilings.

The rewrite SURVIVES refutation subject to repairs R27-1, R27-2, R29-1,
R30-1/2/3, R31-1/2/3, R32-1, R33-1 (+R33-2 conditional), the s-30 gate flag,
and SR-12 re-measurement of all four word counts at build time with the deck's
counting convention (refuter counts are hand counts, convention-sensitive).
