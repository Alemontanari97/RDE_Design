# First-time listener audit — slides 23-35

Persona: aerospace propulsion engineer at an ESA briefing, zero knowledge of this
project's internals. Judged only from the renders `s-01.png`–`s-46.png`.
Slides 1-22 skimmed once for context; full (a)-(d) report below for each of 23-35.

## Context impression from slides 1-22 (one-glance skim)

Group intro, PGC/RDE physics primer, HYPERDE code and V&V, refill-region and
bladeless-turbine collaborations, disk RDEs, then a pivot at s-21/22 to nozzle
design and the claim that averaging the periodic exhaust is the central problem.
Solid, conventional academic-group front half; the register changes noticeably
from s-27 onward (see below).

---

## Slide 23 — "One nozzle, two flowfields"

(a) **Paraphrase:** The same RDE nozzle has an instantaneous flowfield (rotating
oblique shock), a time-averaged flowfield (clean axisymmetric plume), and a third
"steady state" field that designers actually use — and even the throat is unsteady.

(b) **Confusing / jargon:** "a third field exists: the steady state the field
designs on (left figure, right panels)" — the parenthetical pointer is ambiguous;
I could not tell which panel is the "third field". "~6:1 excursions" — excursions
of WHAT (pressure? Mach? sonic-surface position?) is never stated. "we design
downstream of it" — downstream of the corrugated sonic surface, presumably, but
the sentence is compressed to the point of riddle.

(c) **Question left with:** Which quantity swings 6:1 at the throat, and does
"designing downstream of it" mean the method never needs throat data at all?

(d) **Visual defects:** Left figure pair duplicates two identical Mach colorbars
and is cramped; the two right-hand Jourdaine figures have annotation text
(detonation front / oblique shock / triple point) far too small to read from a
seat; all source captions are in a microscopic gray italic font.

---

## Slide 24 — "How the field designs RDE nozzles today"

(a) **Paraphrase:** Four published RDE nozzle design approaches (ramp, classical
MoC on averaged inflow, non-optimized spike, manual CFD redesign) all design on
an averaged flow, and nobody quantifies the error of that substitution.

(b) **Confusing / jargon:** "the substitution error" appears here for the first
time with no definition — I inferred it means design-on-average vs true-periodic
performance delta, but I had to infer it. "in a systematic census" — whose
census, how bounded? This is process talk about your own literature survey, not a
result. "poses the optimum on the real RDE exhaust" is compressed phrasing.

(c) **Question left with:** Is the "substitution error" an error in thrust value,
or an error in WHERE the optimum shape is? (Slide 25 later answers this, but at
this point I did not know.)

(d) **Visual defects:** The bottom banner box collides with the footer band —
the last line "the substitution error is never quantified." is visually clipped
by the maroon footer. Jourdaine dimension drawings (0.877 mm etc.) are too small
to serve any purpose at briefing distance.

---

## Slide 25 — "Same hardware, two flowfields — and the optimum moves"

(a) **Paraphrase:** Paired steady vs transient runs from the literature show the
steady-designed thrust coefficient differs from the transient one, the optimum
truncation point moves, and the ranking of five cowl/spike variants inverts.

(b) **Confusing / jargon:** Box 2 is a data dump: "peaks at 40% (+0.52%) and
falls at 80% (−5.78%)" — 40% of what? (Truncation ratio ΔL/L, I eventually
matched it to the left plot's x-axis, but the box does not say so.) "No published
work prices this error" — "prices" is an odd in-house verb; "quantifies" is what
you mean. "steady-from-averages" is compressed to near-opacity.

(c) **Question left with:** Are these numbers your reruns or the cited authors'
own — and is a 0.5-5.8% delta significant relative to the CFD's own uncertainty?

(d) **Visual defects:** The middle-column figures are small with illegible
legends; the caption "ibid. 2023, Fig. 16" is cramped against the figure; box 3
("No published work prices this error.") floats in a mostly empty rounded
rectangle — one line of text in a huge box reads as unfinished layout.

---

## Slide 26 — "A 1971 warning: the closure alone moves the optimum"

(a) **Paraphrase:** A 1971 study showed that changing only the base-pressure
model moves the optimum contour a lot (×2.45) while barely changing the thrust
value (+0.26%), and the same closure is still used today even though hot-fire
base pressures (0.59 atm) sit far from steady predictions (0.95 atm).

(b) **Confusing / jargon:** "the optimum moves ×2.45" — moves times 2.45 in WHAT
metric? A coordinate? An angle? A length? This is the slide's headline number and
it is dimensionless-by-omission. "the closure" in the title is only decoded by
the first bullet; a title should not need decoding.

(c) **Question left with:** What physical quantity is multiplied by 2.45 — and if
the value changes only +0.26%, why should I care that the contour moves? (The
answer — flat optimum, so shape matters and value forgives — is exactly the
argument, but the slide never says it.)

(d) **Visual defects:** The 1971 table scan is an unreadable wall of six-decimal
numbers — it conveys "we found an old table" and nothing else; the contour plot
below it is a low-resolution photocopy with axis labels too small to read.

---

## Slide 27 — "Seventy years of variational design — extended to the periodic system"

(a) **Paraphrase:** A timeline from Rao 1958 through the Kraiko school to "this
programme", claiming yours is the same variational-design lineage extended to
periodic flow.

(b) **Confusing / jargon:** Heavy. "the adjoint ante litteram" — cute but
Latin-plus-adjoint in one breath. "no cycle measure, no quotient, no
certificates" — "quotient" and "certificates" are internal project vocabulary; I
have no idea what a "certificate" is in this context, and it recurs later. "1981
Allman–Hoffman: the direct route" — a four-word box that tells me nothing.
Worst: "*A 1975 Russian precedent is still in procurement — not yet read against
the original.*" — this is internal process talk (you are telling ESA you haven't
obtained a paper yet); at a briefing it reads as an odd confession dropped into a
lineage slide, and "in procurement" sounds like you're buying hardware.

(c) **Question left with:** What is a "certificate", and does the unread 1975
precedent threaten the novelty claim on the previous slides?

(d) **Visual defects:** Six timeline boxes with wildly uneven text density (the
1981 box is nearly empty, the 1970 box overflows); the Rao Eq. [14] scan floats
bottom-left disconnected from any box; the "now" box switches to red styling
while the italic caveat sits unanchored to its right.

---

## Slide 28 — "The field's own conclusion: 'approximately applicable' — with no error bar"

(a) **Paraphrase:** A 2025 paper itself concedes steady max-thrust theory is only
"approximately applicable" to RDE nozzles; sizing is fine to ~1% but ranking
geometries is an open question, and your thesis is to quantify "approximately".

(b) **Confusing / jargon:** "SIZING — error ~1% — supported at this level" —
supported by what, at what level? No source for the ~1%. "RANKING between
geometries — fractions of a point" — fractions of a point of WHAT (Isp seconds?
percent of thrust coefficient?). "nobody today can answer it" is a strong claim
delivered without an anchor. The thesis line itself ("'approximately' is an
adverb to be quantified") is genuinely good — the one memorable sentence in the
section.

(c) **Question left with:** What evidence separates the ~1% sizing regime from
the fractions-of-a-point ranking regime — is that split yours or the paper's?

(d) **Visual defects:** The slide is two-thirds empty; there is a stray
horizontal line artifact above the quote box; the citation line under the quote
is in a font small enough to be decorative rather than informative.

---

## Slide 29 — "The per-phase idea has ancestors — and we declare them"

(a) **Paraphrase:** Three prior works (0-D per-phase blowdown, 2D-axi at cycle
pressure ratios, wave-frame MoC) came close, but none posed a variational optimum
on a per-phase family — that is your novelty.

(b) **Confusing / jargon:** "the mean of a ratio does not commute, and the weight
is undeclared" — I can decode ⟨F/p⟩ ≠ ⟨F⟩/⟨p⟩, but "the weight is undeclared" is
telegraphic. "never design, never a family" — sounds like a slogan, not a
sentence; what is "a family" here? The tiny inset formula
"⟨F/p⟩ ≠ ⟨F⟩/⟨p⟩ ⇒ bias = O(Var) on 10:1 cycles" is the actual technical content
of the slide and it is rendered as a near-illegible one-line strip.

(c) **Question left with:** What exactly is the "per-phase family" over which the
optimum is posed — a family of nozzle shapes, one per phase? (Slide 30/32 later
clarify; here it is dangling.)

(d) **Visual defects:** The worst layout in the section: four tall rounded boxes
that are ~70% empty white space; the fourth box's only distinguishing content is
the microscopic formula strip stuck at an arbitrary height; the bottom half of
the slide is blank. Looks like a template that was never filled.

---

## Slide 30 — "Two different optimization problems"

(a) **Paraphrase:** The field collapses the cycle to one mean field and applies
steady optimality (solving a substitute problem); you keep phases separate,
average the thrust functional, and derive that problem's own optimality
conditions — with a theorem that only the weighted mean satisfies the wall
condition.

(b) **Confusing / jargon:** The two floating equations use J[Σ], F[Σ; s(ξ)],
dμ(ξ), G_ξ, λ_L, g_L with zero symbol definitions — as a first-time listener I
can only pattern-match "integral over phases + constraint". "averaged
transversality & corner conditions" — "corner" is calculus-of-variations
insider vocabulary. "the error on the argmax has no bar" — clever once decoded,
cryptic at first read. "a.e. on the shared wall" — measure-theoretic "almost
everywhere" at a programmatic briefing is pure flavor.

(c) **Question left with:** What is ξ and the measure μ — phase angle with
time-weighting? That single definition would unlock the whole slide.

(d) **Visual defects:** The two equations sit unanchored in the gap between the
boxes and the theorem strip, with no labels tying them to either column; the
italic teal "conditions never written before" hangs below the right box looking
like an orphaned caption.

---

## Slide 31 — "Where the difference is a theorem — and where it is an open, measured question"

(a) **Paraphrase (attempted):** For area-ratio-only sizing and for a full adapted
plug the steady and periodic optima provably coincide; for a truncated plug the
coincidence breaks, and that is the first real averaged shape-optimization
problem — size unknown, machine ready.

(b) **Confusing / jargon:** This slide almost defeated me. Box 1 says "the two
problems coincide — proven" and then immediately "even here the wrong mean moves
the optimum area ratio by +44–87% (3–10 s of Isp)". To a naive listener this is a
flat self-contradiction: if the problems coincide, how does the optimum move by
44–87%?? (I suspect "coincide" means same-functional-form while the WRONG choice
of mean still shifts the input — but the slide does not resolve it, and 3-10 s of
Isp is enormous.) "perimeter declared", "the first genuinely averaged shape
problem opens" — declared where, opens how? "(10:1 inlet, ~6:1 throat, ~20:1
combustor swings)" — three unexplained ratios in a row. "The machine is ready: it
is the first campaign" — internal roadmap talk.

(c) **Question left with:** The contradiction above — coincide-yet-moves-44-87% —
is the question I would raise my hand on, and the answer decides whether I trust
the whole theorem structure.

(d) **Visual defects:** Three boxes with large empty lower halves; middle box
noticeably thinner in content; the color coding (teal/teal/red) is the only cue
for "proven/proven/open" and is never legended.

---

## Slide 32 — "Per-phase is not an approximation — it is a change of coordinates"

(a) **Paraphrase:** For a pure rotating wave the flow is steady in the wave
frame, so azimuth = phase and the per-phase family is an exact coordinate change
(with one declared approximation), whereas global time-averaging genuinely mixes
phases.

(b) **Confusing / jargon:** "an EXACT quotient (one declared O(St) approx.)" —
"quotient" again (group-theory flavor no propulsion listener will parse), and
"EXACT ... with one approximation" reads as an oxymoron unless O(St) is
explained; St (Strouhal?) is never defined. The bottom-right box "Proof structure
declared; complete proof in progress — stated openly." is internal audit language
verbatim on a slide — honest, but it sounds like a compliance note, not
engineering.

(c) **Question left with:** How small is the O(St) term for a real RDE — is the
"exactness" claim practically clean or does it hide a 10% correction?

(d) **Visual defects:** The ring diagram's labels and the two floating callout
boxes are in very small type; the callouts overlap the figure's gray background
awkwardly; the proof-status box is stranded in the bottom-right corner with no
visual connection to anything.

---

## Slide 33 — "The design space: configurations are outputs, not inputs"

(a) **Paraphrase:** The design variable is a solid body inside an envelope, so
bell/plug/shrouded-plug/expansion-deflection emerge as result classes rather than
assumptions; the global optimum is a tournament among finitely many sector
optima, and today only the bell sector actually runs.

(b) **Confusing / jargon:** The densest internal-vocabulary slide in the deck:
"at certified closures the plug weakly dominates the bell", "tie region
characterized", "closures at equal area ratio, never hardware", "certified
splines per sector, no level-sets", "named campaign", "driver today — 9 DOF",
"named owners and windows". "Certified" appears three times and is never defined
— proof? error bound? test suite? "named owners and windows" is project-
management minutes language; ESA does not know your owners or your windows. "an
infinitesimal body in supersonic flow pays only wave drag" — I sense a real
argument behind this but it is compressed past recovery.

(c) **Question left with:** What does "certified" operationally mean, and what is
the actual evidence behind "the plug weakly dominates the bell" — that sounds
like a headline result buried in a jargon bullet.

(d) **Visual defects:** The left dashed-envelope sketch contains only a tiny
chevron glyph — as the illustration of THE design variable it is almost content-
free; the four class boxes use three different text colors (teal/red/black) with
no legend; text balance is heavily right-loaded.

---

## Slide 34 — "Same pressure reading, different thrust"

(a) **Paraphrase:** Two flows can read identically on an inlet pressure gauge yet
differ in swirl and thrust (1.5-3%), so pressure alone cannot rank designs — the
nozzle boundary data must carry the full state, which your Q2D chamber solver
provides.

(b) **Confusing / jargon:** Very little — this is the cleanest slide of the
section and I could paraphrase it in one pass. Only gap: the "(1.5–3%)" thrust
difference has no source; every other number in the deck is cited, this one is
naked.

(c) **Question left with:** Where does 1.5-3% come from — measured, computed, or
literature?

(d) **Visual defects:** The gauge diagram is very schematic (fine — it is a
concept slide) but its labels are small gray-on-gray; the right-bottom third of
the slide is empty, so the one figure could have been drawn twice the size.

---

## Slide 35 — "Not just pressure — the whole interface state varies"

(a) **Paraphrase:** Published RDE data show the nozzle-interface state swings
hugely over one cycle (total pressure ~4:1, total temperature ~40%, Mach
0.85-1.33) and the sonic surface is corrugated with coexisting subsonic and
supersonic bands — so you measure the subsonic fraction per phase instead of
assuming choked flow.

(b) **Confusing / jargon:** "published both ways" — both WHICH ways? (Mostly
subsonic vs mostly supersonic, I guess, but it's a shrug of a phrase.) The
headline "~4:1" requires me to convert the table's "237% (Max-Min)/Avg" myself
to believe it. The right-hand schematic's red annotations ("sonic surface M = 1 —
corrugated...", "design interface: easily supersonic, with margin") are exactly
the point of the slide and are printed too small to read.

(c) **Question left with:** For YOUR configuration, what fraction of the
interface is subsonic per phase — the slide says you measure it, but shows no
number of yours.

(d) **Visual defects:** Right schematic annotation text illegible at distance;
the scanned table has low-res borders; left figure's axis and inset labels
(A3.1/A3.2 = 0.6 ...) are tiny.

---

## Section verdict

The physics argument of s-22-26 (three fields, optimum moves, 1971 precedent) is
genuinely compelling and mostly lands. From s-27 onward the deck increasingly
speaks its own private language: "certificates", "quotient", "closures",
"campaigns", "named owners and windows", "in procurement", "proof in progress —
stated openly". A first-time listener hears a rigorous group talking to itself.
Every slide that states a theorem should define its symbols or drop them.

**Three weakest slides of the section:**

1. **Slide 31** — the apparent self-contradiction ("the two problems coincide —
   proven" vs "moves the optimum area ratio by +44-87%, 3-10 s of Isp") sits at
   the exact center of the thesis and is unresolvable from the slide alone; a
   listener who trips here distrusts the whole theorem ladder.
2. **Slide 29** — layout failure: four mostly-empty boxes, the slide's only real
   technical content (⟨F/p⟩ ≠ ⟨F⟩/⟨p⟩ bias) rendered as an illegible one-line
   strip, half the slide blank; it reads as an unfinished template.
3. **Slide 33** — highest jargon density in the deck ("certified closures",
   "weakly dominates", "named owners and windows", "9 DOF driver"); a headline
   result (plug dominates bell) is buried inside undefined vocabulary, and the
   central illustration of the design variable is a near-empty dashed box.

Honorable mention: **Slide 27**'s "*A 1975 Russian precedent is still in
procurement — not yet read against the original*" is the single most jarring
sentence in the section — internal to-do-list language presented to an external
panel.
