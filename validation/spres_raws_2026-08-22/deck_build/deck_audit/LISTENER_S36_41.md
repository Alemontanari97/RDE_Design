# First-time listener report — slides 36–41

Persona: aerospace propulsion engineer at an ESA briefing, no prior exposure to this
project. Context absorbed by skimming slides 23–35 (one glance each). Judgement is
based strictly on what is rendered on the slides.

Context impression from the skim (23–35): the story I picked up is — RDE nozzle flow
is unsteady but the field designs on a time-averaged substitute; that substitution
moves the optimum and nobody has quantified the error; this team formulates the
optimization on the true periodic flow via a per-phase change of coordinates, and
claims theorems about when the substitute optimum coincides or breaks. That arc
mostly landed. Recurring irritants already visible in the skim: "named campaign",
"named owners and windows", "driver today — 9 DOF", "the machine is ready" — I keep
hearing a team talk to itself about its own project management instead of to me.

---

## Slide 36 — "What the reduction drops is explicit — and measurable"

**(a) Paraphrase.** The per-phase simplification throws away certain terms of the
full 3D unsteady physics, but those terms are written down as an explicit operator:
its mean part is provably zero, and the two surviving parts (front jumps, covariance)
will be measured rather than assumed small.

**(b) Confusing / jargon / process talk.**
- "the declared HEEL" — I do not know what a "heel" is here. Achilles' heel? A named
  internal weakness register? This word alone made me distrust my paraphrase.
- "mean channel", "covariance" — channels of *what*? Covariance between *which two
  quantities*? The boxes name categories without operands.
- "machine-verified identities" — verified by what machine, against what?
- "the first campaign of the phase" — pure internal scheduling talk; as a listener I
  don't know what a "campaign" is or which "phase" (project phase? flow phase? the
  word "phase" is dangerously overloaded on this slide — it means wave phase
  everywhere else in the deck).
- "Published face: lateral force 25–35% of axial" — "published face" is an odd
  locution; and I could not connect the lateral-force figure on the right to the
  discarded-operator story on the left. Is lateral force one of the discarded terms?
  The slide never says so.
- "no number yet — our declared weak point" — honest, but reads like a line from an
  internal audit log, not a briefing sentence.

**(c) Question left with.** Physically, what ARE the discarded terms, and roughly how
big could they be relative to thrust? (An order of magnitude, even a bound, would
anchor everything; "no number yet" on one of only two surviving terms leaves me
unable to judge whether the whole per-phase claim is safe.)

**(d) Visual/layout defects.** Left diagram is cramped: "full azimuthal physics"
title nearly touches its box border; parenthetical text inside boxes is very small.
The gold/yellow border on the "covariance" box breaks the deck's two-color (teal/
maroon) code with no legend explaining what gold means. The right-hand borrowed
figure has tiny axis annotations (unreadable numbers in red), and its caption is the
only link to the bullets — the figure floats.

---

## Slide 37 — "What is an adjoint — the whole gradient for one extra solve"

**(a) Paraphrase.** Instead of N flow solves for N shape parameters (finite
differences), one forward solve plus one backward "adjoint" solve gives the exact
derivative of the thrust objective with respect to every wall parameter at once, so
the optimizer's cost is roughly two solves per step.

**(b) Confusing / jargon / process talk.**
- "the gradient a trust-region Newton then climbs" — grammatically compressed;
  I parsed it on the second read. "which a trust-region Newton method then climbs"
  would have cost four words.
- "cost ≈ 2" — two *what*? (Solves, presumably — say it.)
- Otherwise this is the cleanest slide of the section: a genuine explainer aimed at
  a listener, not at the project log.

**(c) Question left with.** Is the adjoint here for the steady per-phase problem
(one adjoint per phase?) or for the cycle-averaged functional as a whole — i.e., how
does "one extra solve" interact with the many phases I was just told stay separate?

**(d) Visual/layout defects.** Bottom ~40% of the slide is empty and the diagram
sits low-left while the bullets sit high-right, leaving a large dead diagonal. The
tiny "flow solve" boxes in the top row are at the edge of legibility. Minor: the
diagram would carry more if the "cost ∝ N" row visually dwarfed the "cost ≈ 2" row.

---

## Slide 38 — "From theory to a design machine: every choice on record"

**(a) Paraphrase.** The theory is implemented as a six-stage pipeline — engine data →
objective functional → flow solver → adjoint → optimizer → certification — that
outputs a nozzle contour together with certificates and error bars.

**(b) Confusing / jargon / process talk.**
- "Every choice on a register, with alternatives and a test that can reject it —
  open choices declared, with a named lead and date." — this is project-governance
  language. "Named lead and date" means nothing to me and sounds like an internal
  action-item tracker leaked onto a slide.
- "No published design method ships inside a chain built to reject it." — I had to
  read this three times. I *think* it means "no other published method comes with
  built-in falsification tests", which is a strong and interesting claim — but the
  sentence is a riddle.
- "six stages shown — the full eight-stage engineering record is in backup" —
  fine as a footnote, but "engineering record" again sounds like internal
  documentation vocabulary.
- "THE FUNCTIONAL" as a stage name is odd next to concrete names like FLOW SOLVE;
  and "CERTIFY: independent checks that can reject; error bars attached" — I still
  do not know, after two certification mentions in two slides, what a "certificate"
  concretely IS in this pipeline. That word is doing a lot of unexplained work
  across the whole section.

**(c) Question left with.** What is one concrete example of a certificate — what
quantity is checked, against what independent reference, and what happens when the
check fires?

**(d) Visual/layout defects.** The curved teal arrow under the pipeline is
ambiguous: it appears to loop from OPTIMIZER back to FLOW SOLVE (iteration), but it
visually emanates from under ADJOINT and the caption beneath it ("why the adjoint…
iterate — seconds per design step") mixes two messages (adjoint cost + iteration
loop) on one arrow. Box-internal text is small and dense; "ENGINE DATA" body text
nearly touches its border; the header "THE FUNCTIONAL" is tight against its box
edges. The italic three-line caption in three colors (teal/maroon/teal) under the
arrow reads as decoration, not information hierarchy.

---

## Slide 39 — "Inside the optimizer stage — including what we will re-examine"

**(a) Paraphrase.** The optimizer is a trust-region Newton method with measured
curvature (chosen because the design landscape is irregular and this beats
quasi-Newton), the gradient underneath is exact for the discrete problem, and some
2026 solver will be compared against it later.

**(b) Confusing / jargon / process talk.**
- The entire third box is internal process: "a 2026 solver candidate, comparison
  pre-registered at equal constraints — the solver census is dated." Which solver?
  "Pre-registered" where? "The solver census is dated" — whose census, dated
  meaning obsolete or meaning time-stamped? I genuinely cannot tell which of the
  two opposite meanings is intended. This box tells an outsider nothing.
- "measured curvature and a certifiable step beat quasi-Newton guesses" — "beat" by
  what margin on what metric? An assertion with no evidence shown.
- "What we will re-examine" as a headline is a promise to the project log, not to
  the audience.

**(c) Question left with.** Why should I believe trust-region Newton was the right
choice — is there a convergence plot or an iteration count somewhere? (A single
number, e.g. "converges in ~12 steps where BFGS stalls", would have made the slide.)

**(d) Visual/layout defects.** Three small boxes, each less than a quarter full,
floating in a mostly white slide — this looks like an unfinished draft. The lower
half is entirely empty. Of the six focus slides this is visually the poorest.

---

## Slide 40 — "Before going where Rao cannot, the machine reproduces Rao"

**(a) Paraphrase.** As a sanity benchmark, the new variational/adjoint machinery
independently re-derives the classical Rao maximum-thrust nozzle contour, matching
it to a maximum deviation of about 2·10⁻³ throat radii, within a stated tolerance
band.

**(b) Confusing / jargon / process talk.**
- "independent cross-code tolerance band" — where does the band come from? Two
  other codes? The band is the whole acceptance criterion and its origin is a
  four-word legend entry.
- Plot annotations "attachment thB* = 15.55 deg" and "lip y = 2 (eps = 4)" are
  cryptic: "thB*" and "eps = 4" (epsilon of what — expansion ratio?) are unlabeled
  symbols.
- "Two routes, one contour — the field's benchmark, passed." — telegraphic but I
  got it. This slide otherwise speaks my language: it is exactly the validation
  slide an outside engineer wants to see, and I could paraphrase it on first read.

**(c) Question left with.** Contour agreement is shown — does the *thrust* also
agree, and to how many digits? (Two contours 2e-3 apart could still be the wrong
comparison if the objective is flat there — which slide 25 told me it often is.)

**(d) Visual/layout defects.** The embedded figure's internal text (subtitle,
legends, deviation-panel labels) is small and slightly soft/low-contrast grey —
borderline unreadable from the back of a room. Large empty region on the right
below the two bullets. The two-line grey figure caption at bottom-left is nearly
invisible.

---

## Slide 41 — "Speed was engineered, not found — validation becomes affordable"

**(a) Paraphrase.** The tool is fast enough for routine use: one evaluation-plus-
gradient takes 0.45 s, a design segment 15–20 s (target ≤ 30 s), a full campaign
10–14 min (target ≤ 25 min), about 18× faster than some reference run.

**(b) Confusing / jargon / process talk.**
- "Speed was engineered, not found" — slogan I only half-understand even after the
  slide (I assume: deliberate optimization work, not luck — but the slide never
  cashes it out).
- "one design segment" and "full campaign" — undefined units of work. How many
  design iterations is a "segment"? What does a "campaign" produce — one nozzle?
  Ten? Without that, the minutes are not interpretable.
- "vs reference run 18×" — reference run of *what*? The same code before speedup?
  A CFD baseline? These are wildly different claims.
- "Every speed lever passed an invariance gate: same results, same certificates.
  Our measurements, host declared." — three pieces of internal jargon in one box:
  "speed lever", "invariance gate", and above all "host declared", which I could
  not decode at all (declared to whom? does "host" mean the compute hardware?).
  This is the single most AI/process-flavored sentence in the six slides.
- "certificates" again, still undefined by slide 41.

**(c) Question left with.** 18× versus what baseline and on what hardware — and how
does 10–14 minutes compare with what a CFD-in-the-loop optimization would cost, which
is the comparison that decides whether "validation becomes affordable" for me.

**(d) Visual/layout defects.** In the bar chart, each bar has three segments (dark
teal, light teal, grey) with no legend — I guessed dark = measured range min, light =
range max, grey = headroom to target, but that is a guess. The table's target column
shows "—" for two rows that the chart then ignores, so table and chart cover
different rows without saying why. The red "target" tick labels are tiny. Vertical
gap between chart block and the wide summary box is large; slide bottom third is
mostly empty.

---

## Section verdict

Strongest: 37 (real explainer) and 40 (real validation evidence).
The section's chronic diseases: (1) the word **"certificate/certify"** is load-
bearing in slides 38, 39, 41 and is never once defined; (2) internal project-
management vocabulary ("campaign", "named lead and date", "pre-registered",
"census is dated", "declared weak point", "host declared", "HEEL") keeps
displacing physics; (3) three of six slides are half-empty.

**Three weakest slides:**
1. **Slide 39** — near-empty layout, one of three boxes is pure internal process
   ("solver census is dated") that an outsider cannot parse at all; no evidence
   shown for its central claim.
2. **Slide 41** — headline numbers rest on undefined units ("segment", "campaign",
   "reference run") and the summary sentence ("speed lever… invariance gate… host
   declared") is the most jargon-saturated line of the section; unlabeled chart
   segments.
3. **Slide 36** — the one slide whose physics I most needed and could least
   paraphrase with confidence: "HEEL", operand-less "mean channel"/"covariance",
   and a right-hand figure whose connection to the discarded operator is never
   stated.
