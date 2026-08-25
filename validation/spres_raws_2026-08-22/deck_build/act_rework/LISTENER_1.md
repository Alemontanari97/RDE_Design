# LISTENER 1 — first-time technical listener (aerospace propulsion engineer, no project knowledge)

Context read: ctx-34 through ctx-41 (data contract, interface evidence, adjoint, machine, optimizer, Rao benchmark, speed). Judged: ctx-42..46.

---

## Slide 42 — "The residual error, channel by channel"

**(a) What I believe it tells me:** The method's total error is decomposed into six named sources, of which one is proven zero, three are estimated at the level of a few percent, and two are honestly admitted as not yet quantified.

**(b) What confused me / read as jargon:**
- **"Swirl booking debt"** — "booking debt" is accounting language I have never seen in propulsion; I cannot tell if it means an unmodeled loss, a deferred correction, or something else.
- **"Jumps at the fronts (the heel)"** — "the heel" is clearly an internal nickname (Achilles' heel?); to an outsider a row label should say what the physical error source is, not the team's pet name for it.
- **"theorem (declared perimeter)"** — declared by whom, and what is a "perimeter" of a theorem? Reads like internal audit-process vocabulary.
- **"declared open"** — I infer "unquantified", but "declared" is process talk; "not yet quantified" would be plain.
- **"Sizing level ~1%"** — sizing of what? Grid? Nozzle scale? Discretization?
- **"Our one in-class number: +0.51% ± ~30%"** — a ± of 30% *on a percentage* is ambiguous (30% of 0.51, or ±30 points?), and "in-class" is undefined here.
- **"No external referee exists: we close the bracket, or it stays open"** — I sense the intent (no one else can validate this) but "close the bracket" is an internal metaphor carried over from slides I haven't internalized.
- **"Channels do not sum"** — then how do I combine them? The one operation an engineer wants to do with an error table is denied without a replacement rule (RSS? max? correlated?).

**(c) Question it leaves me with:** Bottom line — if I design a nozzle with this tool today, what is the expected error band on delivered thrust/Isp, as one number or interval?

---

## Slide 43 — "Which gap dominates — the honest map"

**(a) What I believe it tells me:** Their per-phase design method sits between a simpler mean-state approach (never computed head-to-head by anyone) and the true 3D optimum (uncomputable), and their falsifiable bet is that the gap due to problem formulation, not model fidelity, is the one that matters.

**(b) What confused me / read as jargon:**
- **"three gaps: formulation · model · composition"** — three technical terms introduced in a caption line and never defined on the slide; I can guess "formulation" and "model", but "composition" gap means nothing to me.
- **"three suppression results on the model gap, none on formulation"** — "suppression results" is completely opaque; suppressed by what, shown where?
- **"front jumps are unsuppressed, no number yet"** — inherited internal shorthand; without slide 36 fresh in mind this is unreadable.
- **"the programme"** as a box label — the box for *your own method* is labeled with a bureaucratic word instead of what the method is.
- **"Programme failure needs two independent misses — both measurable"** — I eventually decoded this (the method is only wrong if two separate tests both fail), but on first read it sounds like risk-management boilerplate, and "misses" is undefined.
- **"the honest map"** in the title — self-certifying honesty is AI/process-flavored; let the content be honest, don't announce it.

**(c) Question it leaves me with:** If the mean-state comparator has never been computed by anyone, on what evidence do you already believe the formulation gap dominates?

---

## Slide 44 — "What tightens the bracket, in order — every outcome pre-registered"

**(a) What I believe it tells me:** A four-step validation campaign (measure residuals, compare against mean-state design, run a coupled simulation, then a large 3D reference run), with the pass/fail decision rules fixed in advance and a stop criterion: gains below ~1% Isp mean pivot to certification work.

**(b) What confused me / read as jargon:**
- **"pre-registered"** (twice) — clinical-trials / open-science vocabulary; I understand it, but in an engineering briefing it reads as imported process ideology rather than a test plan.
- **"the bracket"** in the title — the bracket was introduced somewhere else; as a title concept it forces me to reconstruct it.
- **"per certified family"** — family of what? Designs? Solutions? "Certified" by the tool itself?
- **"PAIRED COUPLED RUN" / "price of the substitution, on the field's template"** — I genuinely cannot paraphrase this box. Substitution of what for what? Whose template? This is the weakest cell on the slide.
- **"bar holds → ~1% sizing stands; exceeded → class run becomes priority"** — chained internal shorthand ("bar", "sizing", "class run"); the logic is a decision tree written in team dialect.
- **"~12M-cell decider"** — I get that it's a 12-million-cell CFD run, but "decider" is odd; and *decider of what* is only recoverable from the footnote.
- **"decided after the residual — today: channel, not commit"** — this italic line is the most cryptic text in the deck; I cannot paraphrase it at all.
- **"Gap B (ours vs mean-state) ... Gap A ..."** — labels A/B appear only in the footnote, never in the main map on slide 43; a taxonomy introduced and used once, in fine print.

**(c) Question it leaves me with:** What is the schedule and cost of these four steps, and which of them need external facilities versus what you can do in-house?

---

## Slide 45 — "Three asks — each one decision-ready"

**(a) What I believe it tells me:** They are asking the audience for three things: help (collaboration or funding) with a large reference CFD run, access to engine test data with agreed instrumentation, and endorsement of publication venues plus access to three paywalled papers.

**(b) What confused me / read as jargon:**
- **"the declared class" / "class decider"** — "class" is doing enormous unexplained work across slides 44-45; as a newcomer I never learned what a "class" of engines/runs is.
- **"TO DECIDE: the channel — the commit comes after the residual measurement"** — "channel" and "commit" are internal state-machine words; I cannot map them to a concrete decision I would be asked to make in the room.
- **"climbs a declared reliability ladder (full ladder in backup)"** — a ladder of what rungs? "Declared" again — the deck's tic.
- **"Data is not fed in: it is admitted — and the entry gate can say no"** — a nice idea (input data is quality-screened) buried in courtroom metaphor; "admitted" vs "fed in" is a distinction I only got on second read.
- **"(A contract prediction — not yet exercised on real data.)"** — honest, but "contract prediction" is software-engineering vocabulary; and it quietly tells me the headline claim of the box is untested.
- **"each one decision-ready"** — process self-praise; whether an ask is decision-ready is for the decision-maker to judge.

**(c) Question it leaves me with:** Concretely, what are you asking ESA for — how many CPU-hours, which test rig, what budget, and by when?

---

## Slide 46 — "A method you can audit — fast enough to validate economically"

**(a) What I believe it tells me:** Closing summary: this is the first per-phase variational design method for RDE nozzles, its approximations are explicit and measurable, its error budget is stated cell by cell, and it runs fast enough that validating it is cheap.

**(b) What confused me / read as jargon:**
- **"Honesty here is not a disclaimer — it is built into the method"** — this is the most AI/process-flavored sentence in the deck; a method has accuracy, convergence, cost — "honesty" is a property of people. Saying it twice (title of 43, banner here) makes me *more* suspicious, not less.
- **"an honest error bracket, channel by channel, each cell with its evidence level"** — "evidence level" per table cell is audit-committee language; an engineer would say "each error source with how it was estimated".
- **"already priced, with pre-registered outcomes — and a declared stop criterion"** — three process words in one bullet (priced, pre-registered, declared); the actual engineering claim (we know what it costs and when we'd stop) is fine, the vocabulary is off-register for a propulsion audience.
- **Layout defect:** the pipeline diagram at the bottom is shrunk to illegibility and collides with the footer banner ("Ro..." / "(H)RUST team" text is cut through by the figure). It reads as a paste-in error, which undermines a slide whose message is rigor.
- **"For the programmes"** — the word "programme" again as a stand-in for "you, the funders"; slightly evasive.

**(c) Question it leaves me with:** After 46 slides I still don't have the one number a closing slide owes me: how much better is a nozzle designed this way — even as a bounded expectation — than what I would design with today's standard practice?

---

*Written by Listener 1, 2026-08-23. Naive by design — no project files consulted beyond the renders.*
