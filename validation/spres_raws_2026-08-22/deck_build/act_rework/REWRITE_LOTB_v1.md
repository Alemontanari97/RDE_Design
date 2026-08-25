# REWRITE_LOTB_v1 — theory-core rebuild proposals (s-27..s-33, minus protected s-28)

**Confronto/record stage**: NARRATIVE_SPINE_v2.md blocks [27/C6], [29/C7-bis-pre],
[30/C7-bis], [31/C7-ter], [32/C8], [33/C8-bis] + specs_c12.py notes (rigor
classes = ceiling) + deck_audit findings (LISTENER_S23_35, LISTENER_FULL,
AUDIT_SYNTHESIS rows 1/3/5/9/12 + LOT 1).
**Consumption arc**: this file → S4 orchestrator implements into specs_c12.py
(+ two new home figures specified under Order F) → assert-gated rebuild →
exact-persona listener (CKP-S4-1) → user gate. Nothing here is of record until
implemented and rebuilt.

---

## STATUS VOCABULARY (Order B — single 3-level wording, notes classes = ceiling)

| Level | On-slide wording | Maps from notes class | Used on |
|---|---|---|---|
| L1 | **proven (hypotheses stated)** | THEOREM ([T-T7RED]) | s-31 panel 1 |
| L2 | **proven, within stated limits** | THEOREM* ([T-T7FS(b)], [T-T3], [T-T4]) | s-30 band; s-31 panels 2, 3 |
| L3 | **proof laid out, completion in progress** | SCHEMA (quotient, route S1) | s-32 status card |

Rules applied: never upgrade (each claim carries its notes class or lower);
the wording appears identically wherever a status is stamped; no other status
phrasing anywhere on s-30/s-31/s-32. NOTE: Order B's example "proven,
perimeter declared" contains the HARD-RULES forbidden word "declared" —
replaced by "proven, within stated limits" (same content, rule-clean).

---

## SLIDE s-27 — C6 (Order D)

### TITLE
Seventy years of variational design — extended to the periodic system

### ON-SLIDE (exact final text)
Timeline, six boxes (unchanged layout, rebalanced text density):

- **1958 · Rao** — the control surface emerges as a result of the variational problem
- **1967 · Hoffman** — multiplier fields along characteristics — the adjoint before it had a name
- **1970 · Kraiko–Osipov** — a time-weighted wall, the closest ancestor: no cycle average, no per-phase family, no error control
- **1981 · Allman–Hoffman** — maximum-thrust contours by direct optimization of the parameters
- **1994–2002 · Kraiko–Tillyaeva school** — field adjoint and shape gradient; non-uniform, vortical inflow
- **now · this programme** — the same line, carried to the periodic exhaust

Equation strip (kept): `figs_paper/rao_eq14_transversality.png`, caption
"The transversality condition — Rao, Jet Propulsion 28(6), Eq. 14, p. 379 (1958)".

Footline **DELETED from slide** (moves verbatim to speaker notes).

Net words ≈ 77 (six-card timeline; under the 100 cards cap).

### VISUAL
Same `timeline_rao` layout with three repairs: (1) the Rao Eq. 14 strip moves
directly beneath the 1958 box, tied to it by a thin vertical connector line —
no longer floating bottom-left; (2) box text rebalanced (1970 box trimmed,
1981 box filled) so the six boxes have comparable density; (3) the italic
footline zone is removed, freeing the lower right for air. No new figure.

### SCRIPT
1. We are not inventing a genre; we inherit one.
2. Rao, fifty-eight: the optimal contour where the control surface itself is an output of the calculus — the equation below is his transversality condition.
3. Hoffman, sixty-seven: multiplier fields along the characteristics — the adjoint before the name existed; you will meet those fields again inside our machine.
4. Allman and Hoffman, eighty-one, took the direct route: optimize the contour parameters directly.
5. The Kraiko–Tillyaeva school built the field adjoint and the shape gradient for non-uniform, vortical inflow.
6. And the ancestor we always cite: Kraiko and Osipov, nineteen-seventy — a wall condition weighted in time.
7. What it lacks is exactly our subject: no cycle average, no per-phase family, and no error control on the substitution.
8. We extend this line to the periodic exhaust.
9. One Russian paper from 1975 is still on order; we say so, and we do not summarize what we have not read.

Speaker-notes-only line (moved from slide, verbatim): "A 1975 Russian
precedent is still in procurement — not yet read against the original."

### ANCHORS
- K-O 1970 mandatory citation → CH2-feed-6 (LL-1, ADJUDICATED); "no cycle measure, no quotient, no certificates" decoded to plain words ("no cycle average, no per-phase family, no error control") from the same notes line — weakened/decoded, not strengthened.
- Classical school boxes → CH5-feed-6 (LL-7/14/27); lineage claims only from LINEAGE_LEDGER (guard 10; lint 7).
- 1981 box expansion → decode of "the direct route" via the cited work's own subject (Allman–Hoffman 1981, direct optimization of contour parameters); no new claim about results.
- Tillyaeva 1975 → CH7-feed-6 PENDING-PROCUREMENT; honest form now in notes + spoken script (spine [27/C6] SENSE "honest procurement gaps declared" preserved off-slide per HARD RULES).
- "No family-averaged classical contouring found" = query-bounded (guard 9) — wording stays in notes.

---

## SLIDE s-29 — C7-bis-pre (Order C)

### TITLE
The per-phase idea has ancestors — and we name them

(Title change "declare"→"name": "declared" register is forbidden on-slide;
SENSE preserved.)

### ON-SLIDE (exact final text)
Top row — three ancestor cards (author-year heads):

- **Stechmann et al. 2019** — 0-D blowdown per phase, mass-weighted mean — nozzle families fixed
- **Harroun et al. 2021** — 2D-axi at each cycle pressure ratio, thrust coefficients then averaged — with which weight?
- **Fievisohn & Yu 2017** — characteristics in the wave frame, the closest cousin — no design, no shape family

Full-width highlighted band below (maroon-tint, the programme's):

- centerpiece equation: `eqs/eq_ratio_mean.png` (large — see VISUAL)
- caption under equation: *the mean of a ratio is not the ratio of the means — on 10:1 cycles the bias is first-order in the variance*
- claim line (bold): **This programme: the variational optimum on the family of per-phase flows sharing one wall — to our literature search, never posed before.**

Net words ≈ 88 (cards + band; under the 100 cards cap).

### VISUAL
Replace the 3+1 tall-card row with: three SHORT ancestor cards across the top
(equal height ≈ 30% of body); below them one full-width highlighted band
occupying the lower ~45% of the body. Inside the band, `eqs/eq_ratio_mean.png`
rendered at **≈ 40% of slide width, centered horizontally, vertically centered
in the band's upper half** (≥ 3× the current strip height — it becomes the
largest object on the slide); caption directly beneath it in body-size type;
claim line bold beneath the caption. This executes spine REPAIR(F-18) (formula
into the punch element, punch element carries visual weight) and kills the
blank lower half. "ON the family" sentence-case (F-22).

### SCRIPT
1. Before the heart of the method, the ancestry — named by us before you ask; two of the three come from this group's collaborators at Purdue.
2. Stechmann, 2019: evaluate each phase with a zero-D blowdown, then take a stated mass-weighted mean — but the nozzle families are fixed; nothing is designed.
3. Harroun, 2021: two-D axisymmetric at each of the cycle's pressure ratios, then average the thrust coefficients.
4. Except the mean of a ratio is not the ratio of the means — that is the inequality on the slide.
5. On ten-to-one cycles the bias is first order in the variance, and the paper does not state its weight — a question we pose formally, with the source verification assigned.
6. Fievisohn and Yu, 2017 — whose boundary condition you met in our code section — is the closest cousin: characteristics in the wave frame, but no design and no shape family.
7. So the pieces exist in the field; the edifice does not.
8. A family, here, is the set of per-phase flows sharing one nozzle wall.
9. We pose the variational optimum on that family — to our literature search, never posed before.
10. And our simplest rung is exactly Stechmann's reduction level, with the right mean proven.

### ANCHORS
- Ancestry cards → checkpoint C-1 (:131-145); lineage LL-2/LL-3/LL-13 (guard 10, ledger ADJUDICATED); CH7-feed-7 (Fievisohn).
- Harroun weight/denominator undeclared → W-B.0 matrix (source pp. 670-671, verification assigned) — on-slide softened to the question form "with which weight?".
- Inequality + O(Var) bias caption → existing eq strip `eqs/eq_ratio_mean.png` content, currently on-slide (promoted, not altered).
- "Never posed before" keeps query-bounded form on-slide ("to our literature search") per Order C; full query-bounded wording in notes (guard 9).
- "Family = per-phase flows sharing one wall" → decode from C7-bis notes SCRIPT ("keep the phases separate as a family sharing one wall").
- WA_A3 borderline fix preserved: "Stechmann's reduction level", never "rung-1 = a 1-DOF optimal nozzle" (guard 3); T1c (which mean, proven) stays script/notes-level (guard 2).
- Q&A: pre-cooked answer to the Purdue/Heister front (REFUTE_LINEAGE :549) — unchanged in notes.

---

## SLIDE s-30 — C7-bis (PROTECTED FORM: two-column fork + promoted theorem band kept)

### TITLE
Two different optimization problems

### ON-SLIDE (exact final text)
LEFT column (card, head sentence-case):
- head: **The field: average first**
- chain: the cycle → collapse to one mean field → apply steady optimality (Rao / Veen) → **the optimum of a SUBSTITUTE problem**
- foot (italic): *the optimum's location — no error bar*

RIGHT column (card, head sentence-case):
- head: **Us: formulate the periodic optimum**
- chain: the cycle → per-phase family — one wall shared by every phase → cycle-averaged thrust functional → **its own optimality conditions, averaged**
- foot (italic): *to our literature search: never written before*

Equation strips (both), now INSIDE the right column's lower zone, stacked:
`eqs/eq_javg.png` and `eqs/eq_avg_wall.png`; the "a. e." annotation of the
second strip is dropped — it reads "on the shared wall" only.
One-line symbol legend directly beneath the strips (small but body-legible):
*ξ = cycle phase · dμ(ξ) = its weight in the mean · Σ = the shared wall*

Theorem band (kept at promoted weight, status stamped):
**The deciding theorem — proven, within stated limits: no single phase
satisfies its own wall condition — the weighted mean does.** The cycle-optimal
nozzle is optimal at no single operating point.

Net words ≈ 99 (two cards + band + legend; under the 100 cards cap).
SUBSTITUTE remains the deck's ONE kept emphatic cap (F-22); the former caps
FIRST / PERIODIC / ITS go sentence-case.

### VISUAL
Protected two-column fork retained exactly; the only structural moves: the two
equation strips migrate from the floating inter-column gap into the right
(teal) column, visually claiming them as OUR formulation, with the symbol
legend as their caption; the left column gains the freed height. Theorem band
keeps its promoted type size (F-10 of record) with "the weighted mean does" in
bold, and now opens with the L2 status stamp.

### SCRIPT
1. The heart slide.
2. Left, the field's route — including the best of the four papers you saw: collapse the cycle into one mean field, then apply to it the steady optimality conditions of the fifties.
3. You solve the optimum of a substitute problem.
4. Right, ours: keep the phases separate as a family sharing one wall, define the cycle-averaged thrust functional, and derive its own optimality conditions — transversality and corner conditions, averaged.
5. In the equations: ξ labels the phase of the cycle, dμ is the weight each phase carries in the mean, and Σ is the single wall every phase shares.
6. To our literature search, these conditions were never written before.
7. [Stop. Read the band verbatim:] "No single phase satisfies its own wall condition — the weighted mean does."
8. That result is proven, within stated limits — the hypotheses travel with it.
9. The take-away for the room: the cycle-optimal nozzle is optimal at no single operating point.

### ANCHORS
- Ladder I4 vs I2/I3 → CH1-feed-1; boxed substitute warning → CH1-feed-4.
- Deciding theorem → CH2-feed-1 (THEOREM* [T-T7FS(b)]) ⇒ status L2 "proven, within stated limits" (ceiling respected; the bare "proven" of the current render is thereby weakened, not strengthened).
- "Three ways to average, one survives" → CH2-feed-2 (THEOREM* [T-T3]) — stays notes-level.
- "Never written" → litmap C2 NOT-FOUND(q) (query-bounded, guard 9) — on-slide form now carries the bound ("to our literature search").
- Symbol legend → decode of the existing eq strips' own symbols (no new content); "one wall shared by every phase" → C7-bis notes SCRIPT wording.
- "Corner conditions" removed from on-slide chain (kept in script sentence 4 and notes) — weakening allowed; F-10 speech duty preserved.

---

## SLIDE s-31 — C7-ter (Order A: FULL REBUILD around the head-to-head question)

### TITLE
Same constraints, two designs: does the optimal contour move?

### ON-SLIDE (exact final text)
Question band (top, thin, neutral tint):
**Per-phase design vs classical design on the cycle-mean p₀, T₀ — same
constraints, no swirl: does the contour move, and what thrust rides on it?**

New home figure (three configuration panels — spec below), each panel carrying
a label, a status chip, and a one-line verdict:

1. label: *area ratio only — no contour*
   chip: **coincide — proven (hypotheses stated)**
   verdict: with the proven mean the designs coincide; the wrong mean shifts the optimum +44–87%
2. label: *full adapted plug*
   chip: **coincide — proven, within stated limits**
   verdict: the peak-phase design is optimal
3. label: *truncated plug — our configuration*
   chip: **the coincidence breaks — proven, within stated limits**
   verdict: the averaged problem opens here

Answer band (bottom):
**Measured so far: 3–10 s of Isp from the mean alone.** At contouring the size
is open — not presumed small. The tool is ready; this comparison is its first
task.

Net words ≈ 97 (bands + three panel texts; under the 100 cards cap). No
ALL-CAPS ("TRUNCATED" dropped — SUBSTITUTE on s-30 is the only kept cap).

### VISUAL (Order F — new home figure spec: `figs/fig_c7ter_threeconfig.png`)
Matplotlib, deck palette (maroon/teal/gray), three equal side-by-side
axisymmetric half-section schematics on a shared centerline, all labels at
body-legible size (≥ 14 pt equivalent at slide scale):
- **Panel 1 — area ratio only**: annular duct with cowl and a generic dashed
  divergent (dashed = not designed); double-headed arrows marking throat area
  and exit area; sub-label "one number: Aₑ/Aₜ".
- **Panel 2 — full adapted plug**: center spike carried to a sharp tip, cowl
  lip; the plug contour drawn as a solid teal line (the designed wall);
  sub-label "contour designed to the tip".
- **Panel 3 — truncated plug**: same spike cut at ~60% length; vertical base
  face in gray with light hatching; contour solid maroon; truncation plane as
  a dashed red line; sub-label "contour + truncated base".
- Beneath each panel: the status chip as a rounded rectangle (teal fill for
  panels 1–2, maroon-tint for panel 3) containing the chip text above, and the
  one-line verdict beneath it in body type.
This gives the audit's "picture of the three configurations at the moment I
most needed it" and makes the third panel visually the marked one.

### SCRIPT
1. Now the programme's deciding question, stated head-to-head.
2. Take the classical variational design, built on the cycle-mean stagnation pressure and temperature; take our per-phase design; give both identical constraints, and set swirl aside — it gets its own slide.
3. Does the optimal contour move, and how much thrust rides on the difference?
4. We can answer in three settings.
5. First, no contouring at all: only the area ratio is chosen — there the two designs provably coincide, if the classical route is fed the proven weighted mean.
6. Feed it the naive mean instead, and the optimum area ratio moves by forty-four to eighty-seven percent — three to ten seconds of specific impulse — measured on our numerical test bench with rejecting checks.
7. So there is no contradiction on this slide: coincidence is a statement about the problems; the shift is what the wrong mean does to the answer.
8. Second, the full adapted plug: the designs still coincide, within stated limits — the peak-phase design is optimal.
9. Third, the truncated plug — our configuration: the coincidence provably breaks, and the answer becomes a genuinely averaged optimum.
10. That theorem is the answer in form: yes, for our configuration the two designs part ways.
11. How far, at contouring, is open — and we do not presume it small: the flow the mean hides swings ten-to-one at the inlet and about six-to-one at the throat.
12. The tool to measure it is ready; this comparison is its first task.

### ANCHORS
- Head-to-head organizing question → LOT-B Order A (user order, 2026-08-23) + atlas CH6 :440/:490/:712; "no swirl" scoping → same order ("swirl excluded") + swirl5f panel of record (single-digit % plausible on-ray, >10% not excluded off-ray) in notes for Q&A.
- Coincidence/breaks map → CH1-feed-3 (THEOREM [T-T7RED] rung ⇒ panel 1 = L1; THEOREM* [T-T4] nesting + break ⇒ panels 2–3 = L2; sharpness clause in notes); primacy claims stay in locked form D-06 → CH1-feed-10 (notes+Q&A only).
- "+44–87%, 3–10 s of Isp, numerical test bench" → CH2-feed-3 (PRACTICE with rejector; dIsp +3.33..+9.71 s on 6 cases, carrier suite, measured 2026-08-22, stage: verified); FD-5(i) wording "numerical test bench" preserved.
- "With the proven mean / the wrong mean" split → C7-ter notes SCRIPT ("coincide by construction; even there, using the wrong mean moves...") + C7-bis-pre notes (T1c: which mean, proven — pattern-level wording respected, guard 2/3: no "1-DOF optimal nozzle" phrasing).
- "At contouring open, not presumed small" → CH2-feed-8 (OPEN, owner F2 — id in notes only) + CH6-feed-8 (carrier PB-2 OPEN); swing ratios 10:1 / ~6:1 (script) → CH5-feed-9 (CT-6, their BCs/data); the third ratio (~20:1 combustor) moves to notes only.
- "The tool is ready; this comparison is its first task" → re-wording of the wired gate decision twin PB-2 = (b) honest form (NO pre-milestone number — form preserved; "campaign of the phase" removed per F-9 and forbidden-register purge).

---

## SLIDE s-32 — C8 (Order B application + jargon repair)

### TITLE
Per-phase is a change of coordinates, not an approximation

### ON-SLIDE (exact final text)
Bullets (right of figure):
- Pure rotating wave: the flow is steady in the wave frame — azimuth becomes phase.
- One approximation enters, of Strouhal order (wave period vs transit time) — hypotheses stated.
- The global time average mixes the phases — the cruder reduction, the field's.

Status card (directly beneath the bullets, scoped — replaces the current tag):
**Status — this equivalence: proof laid out, completion in progress** (one
building block proven). The averaged-wall theorem of the previous slide is a
separate result: **proven, within stated limits.**

Net words ≈ 60 bullets+card (+ figure callouts ≈ 16).

### VISUAL
Keep `figs/fig_c8_quotient.png` (lab frame → wave frame ring schematic with
two-fates fork), with three repairs: callout-box type raised to bullet size;
callout texts simplified to — teal box: "per-phase family — phases kept
separate: exact, one Strouhal-order approx."; maroon box: "global time
average — mixes the phases"; the status card moves from the stranded
bottom-right corner to sit flush beneath the bullet column, so it reads as the
bullets' status, not an orphan. The word "quotient" no longer appears
on-slide (title already says "change of coordinates"; "quotient" survives in
notes only).

### SCRIPT
1. Is per-phase itself an approximation? No — and that must be said precisely.
2. Remember the primer: in the frame rotating with the wave, this flow is steady.
3. Within the stated data class — a pure periodic rotating wave, monitored on the flatness of stagnation temperature — azimuth becomes phase.
4. Passing to the per-phase family is then a change of coordinates: exact, up to a single approximation.
5. That approximation is of Strouhal order — the wave period against the gas transit time — and its hypotheses are printed.
6. The field's global time average, by contrast, mixes the phases: that is the cruder reduction, and it is theirs, not ours.
7. Now the status, precisely scoped.
8. This equivalence has its proof route laid out, one building block is already proven, and completion is in progress — we say exactly that.
9. The averaged-wall theorem of the previous slide is a separate result and stands on its own: proven, within stated limits.

### ANCHORS
- Quotient + O(St) → CH1-feed-2 (SCHEMA with route S1 named + [T-T0P-E] THEOREM leg) ⇒ status L3 for the equivalence; "one building block proven" = the THEOREM leg (never upgraded to more).
- Strouhal expansion "(wave period vs transit time)" → decode of "Strouhal-order" in the existing notes SCRIPT (standard definition; no new number).
- Data class + T0-flatness monitor → existing notes SCRIPT (periodic-wave scope pin).
- Three-floor organizer → CH7-feed-1 (notes only).
- Scoping order → LOT-B Order B ("s-32's current box must say WHICH result it scopes"); s-30 theorem echo at L2 → CH2-feed-1 (THEOREM* [T-T7FS(b)]).
- **DECLARED DIVERGENCE (for the gate)**: the current tag is a user decision of record (:1450, checkpoint :95-97, guard 12 — "verbatim-stable honesty device"). Order B (later, binding) requires re-scoping; this rewrite keeps the device (two-stage claim, openly stated, on-slide) but changes the verbatim. Needs explicit user ratification at the S4 gate.

---

## SLIDE s-33 — C8-bis (Order E)

### TITLE
The design space: configurations are outputs, not inputs

### ON-SLIDE (exact final text)
Bullets (right of figure, ≤3):
- The design variable: one solid body in an envelope — classes emerge, not presupposed.
- Finitely many classes: the global optimum is the best of the class optima.
- Smooth splines per class — no vanishing bodies: in supersonic flow they buy only wave drag.

Verdict band (full-width, highlighted — same visual grammar as s-30's theorem
band; the headline it deserves):
**First verdict: the plug matches or beats the bell — on checked flow models
at equal area ratio, never hardware; ties mapped.**

State line (small, above footer):
Today the optimizer runs one class — bell, nine design parameters; truncated
plug and shrouded follow.

Net words ≈ 78 (bullets + band + state line; under the 100 cards cap).
Ledger vocabulary fully purged from slide: no "named campaign", no "9 DOF
driver", no "owners and windows", no bare "certified", no "sector",
no "honest state", no "level-sets".

### VISUAL (Order F — rebuild `figs/fig_c8bis_envelope.png`)
Matplotlib, deck palette. Left: the envelope drawn as a dashed region attached
at the cowl lip downstream of the throat (small annotation kept: "attachment
at the lip; uniform-cone condition"), containing a non-trivial gray solid body
(truncated-plug-like silhouette) whose boundary is a teal spline with visible
control points — the design variable actually drawn, replacing the current
near-empty chevron. Arrow labeled "classes emerge" to the right: a 2×2 grid of
mini half-section contour icons drawn as real contours — bell (curved bell
wall), full plug (spike to tip), shrouded plug (spike + cowl), expansion–
deflection (center body deflecting flow outward) — each labeled with its class
name ONLY. The bell icon carries a small chip "running — 9 parameters"; the
truncated-plug icon a maroon-outline chip "our configuration". No ledger text
anywhere in the figure.

### SCRIPT
1. What do we actually optimize over?
2. One solid body inside an envelope, attached at the cowl lip.
3. Bell, plug, shrouded plug, expansion–deflection are not menu choices — they are the classes the result falls into.
4. The classes are finitely many, so the global optimum is the best of finitely many class optima.
5. And whenever we say "optimum", the argument that guarantees it travels with it.
6. One ranking already exists at the reduced rung: the plug matches or beats the bell, with the tie region mapped.
7. Mind the scope: that is a ranking between checked flow models at equal area ratio — never between hardware.
8. On parameterization we chose smooth splines per class and refused vanishing-body tricks: an infinitesimal body in supersonic flow buys only wave drag, so classes are compared whole.
9. Today the optimizer runs one class — the bell, with nine design parameters.
10. The truncated plug and the shrouded plug are next in line.

### ANCHORS
- Configuration-free formulation + envelope + lip attachment/uniform-cone → CH8-feed-1 (flagship feed; problem book §5; user pin 2026-08-02: cono/Chenais, Λ=cerchi).
- Finite classes + tournament → CH8-feed-2 (THEOREM leg, carriers X-GRP10/12) + CH8-feed-3 (THEOREM* existence per sector) — "sector"→"class" is a pure vocabulary decode, ids in notes only.
- Guarantee-with-optimum sentence (script 5) → CH8-feed-4 (M1–M5 mechanism contract; sigle in notes, concept spoken — guard 8; moved OFF-slide entirely, weakening allowed).
- Verdict band → CH8-feed-2/3 record wording "plug weakly dominates the bell pointwise under certified closures, tie region characterized — closures at equal area ratio, never hardware": "matches or beats" = exact plain decode of "weakly dominates"; "checked flow models" = decode of "certified closures"; scope clause kept verbatim-equivalent. No strengthening; no status chip (s-33 is outside the Order-B trio and the notes give no single class for the verdict — none invented).
- Spline route + no-topological-derivatives + wave-drag reason → CH8-feed-9 (LL-29).
- State line → CH8-feed-8 (driver one-sector state; "named campaigns" weakened to "follow"/"next in line").
- F-14 discipline preserved: qualifier prose lives in script/notes, bullets at headline length.

---

## AUDIT COVERAGE — every listener confusion resolved (R) or routed (→notes/backup)

| Finding (listener) | Slide | Disposition |
|---|---|---|
| "adjoint ante litteram" Latin | s-27 | R — "the adjoint before it had a name" |
| "quotient / certificates" undefined | s-27 | R — replaced by plain words ("no per-phase family, no error control") |
| 1975 procurement line on-slide | s-27 | → speaker notes verbatim + one spoken sentence (Order D) |
| 1981 box near-empty / density imbalance | s-27 | R — box filled (title-level decode), densities rebalanced |
| Rao eq strip disconnected | s-27 | R — tied under the 1958 box |
| Does 1975 precedent threaten novelty? | s-27 | → notes/Q&A (honest form retained: not read, not summarized) |
| Central formula illegible strip | s-29 | R — centerpiece at ≈40% slide width (Order C) |
| "never design, never a family" ungrammatical | s-29 | R — "no design, no shape family" |
| "weight is undeclared" telegraphic | s-29 | R — card asks "with which weight?"; script explains |
| What is the per-phase family? | s-29 | R — defined in the claim line ("per-phase flows sharing one wall") |
| Blank lower half / empty punch card | s-29 | R — full-width programme band carries equation + claim |
| ξ, μ, Σ, g_L undefined | s-30 | R — one-line symbol legend under the strips |
| "shared wall" never introduced | s-30 | R — chain item "one wall shared by every phase" |
| "a.e." measure-theory flavor | s-30 | R — dropped from strip annotation |
| "corner" insider vocabulary | s-30 | → script/notes (off-slide) |
| equations float unanchored | s-30 | R — moved inside the right column |
| "error on the argmax has no bar" cryptic | s-30 | R — "the optimum's location — no error bar" |
| theorem-status ambiguity s-30 vs s-32 | s-30/31/32 | R — Order B single vocabulary, L2 stamp on band, scoped card on s-32 |
| coincide-yet-moves-44–87% contradiction | s-31 | R — right-mean/wrong-mean split on-slide + script sentence 7 |
| no picture of the three configurations | s-31 | R — new home figure (Order F spec) |
| "perimeter declared" / "first campaign of the phase" | s-31 | R — status vocabulary / "its first task" (F-9) |
| three unexplained ratios in a row | s-31 | R — off-slide; two decoded in script, third notes-only |
| TRUNCATED caps | s-31 | R — sentence case (SUBSTITUTE only kept cap) |
| unit mix +44–87% / 3–10 s | s-31 | R — panel carries the % shift; band carries the Isp seconds, labeled "from the mean alone" |
| "EXACT quotient" oxymoron / quotient flavor | s-32 | R — "quotient" off-slide; "exact, one Strouhal-order approx." |
| O(St) / St never defined | s-32 | R — "(wave period vs transit time)" once |
| status box destabilizes s-30 theorem | s-32 | R — card scopes THIS equivalence; s-30 theorem echoed at L2 |
| How small is O(St) really? | s-32 | → notes (hypotheses printed; class monitored via T0 flatness; no anchored number exists — none invented) |
| callouts tiny / status box stranded | s-32 | R — type raised; card docked under bullets |
| "certified" ×3 undefined | s-33 | R — "checked flow models"; bare "certified" purged |
| "named campaign / 9 DOF driver / owners and windows" | s-33 | R — engineering words; ledger ids in notes |
| plug-vs-bell verdict buried | s-33 | R — promoted to highlighted verdict band (Order E) |
| "sector" undefined | s-33 | R — "class" throughout |
| envelope sketch content-free | s-33 | R — figure rebuilt with real solid body + spline + contour icons |
| "wave drag" argument compressed | s-33 | R — bullet shortened, full argument in script sentence 8 |

---

## COMPLIANCE NOTES + DECLARED DIVERGENCES (for the S4 gate)

1. **No new claims, no new numbers**: every on-slide statement above traces to
   the listed anchors; all edits are decodes or weakenings. The only added
   sentences are symbol/vocabulary decodes of content already on the slides.
2. **Order B wording**: "proven, perimeter declared" (brief's example) would
   put the forbidden word "declared" on-slide — replaced by "proven, within
   stated limits". Same 3-level ladder, notes classes as ceiling.
3. **s-32 tag divergence**: user decision :1450 fixed the tag verbatim; Order
   B forces re-scoping. Device preserved, verbatim changed — flagged for
   explicit user ratification.
4. **s-30 protected form** untouched structurally (fork + promoted band);
   s-28 untouched entirely.
5. **s-31 gate wiring preserved**: twin PB-2 = (b) honest form — still no
   pre-milestone number at contouring; only the register changed.
6. **New figures required from orchestrator** (Order F): `figs/
   fig_c7ter_threeconfig.png` (spec in s-31 block) and rebuilt
   `figs/fig_c8bis_envelope.png` (spec in s-33 block); deck palette,
   matplotlib, no ledger text inside figures.
