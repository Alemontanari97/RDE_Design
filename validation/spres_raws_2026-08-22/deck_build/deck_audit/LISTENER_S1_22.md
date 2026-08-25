# LISTENER REPORT — Slides 2-22 (first-time technical listener, ESA briefing)

Persona: aerospace propulsion engineer, no prior exposure to this group or project.
Judged only from the renders s-02.png .. s-22.png. Slide 1 (title) skipped per brief.

---

## Slide 2 — "Today"

(a) This is the agenda: five parts moving from who the group is, to the real RDE exhaust problem, to their formulation, a "design machine", and a closing section with a roadmap and requests to us.

(b) "The design machine" is intriguing but opaque as an agenda item — I don't yet know if it is software, a method, or a metaphor. "Honesty, roadmap & requests" — "Honesty" as a section title is unusual; it made me wonder what they need to be honest about. "Our formulation" — formulation of what? The agenda items are catchy but three of five are not self-explanatory.

(c) What exactly will they ask the panel for (money, data, test time)? And what is "the design machine"?

(d) None serious. Large empty area top-right; the teal italic line "Three requests for the panel — at the end." is small and easy to miss, yet it is the most important sentence for an ESA audience.

## Slide 3 — "Research Roads / Group Overview"

(a) A young (~1.5 yr) RDE group at Sapienza doing URANS/low-order modelling, with international partners, whose two pillars are an in-house hybrid-dimensional CFD framework (HYPERDE) and a set of open research topics.

(b) "'Newborn' RDE activity" — the scare quotes read oddly; "young" or "started 2025" would be cleaner. "Q2D" is not yet defined but "hybrid-dimensional" appears here before being explained. "Open research lines" with the arrow "(→ dedicated section today)" embedded mid-list is process talk. The double-headed arrow between HYPERDE and the open lines carries no obvious meaning — are they feeding each other?

(c) What does "industrially-relevant challenges" concretely mean for this group — flight engines, ground demo, turbomachinery integration?

(d) The bottom banner crops the last line of the "Open research lines" list ("heat flux" sits right on the banner edge). Bottom-left HYPERDE block text also nearly touches the footer. Three-column top row has uneven text lengths leaving ragged white space.

## Slide 4 — "Detonation compresses by itself: pressure-gain combustion"

(a) Detonation gives you pressure rise without a mechanical compressor (near-constant-volume burn), hence higher ideal cycle efficiency, and CJ speeds are ~1.8-2.8 km/s across common fuels.

(b) The left plot is very dense: "von Neumann state", "ZND", "Fickett-Jacobs", "Humphrey", "Rayleigh line" all in tiny red annotation text — fine for specialists, unreadable from the room. Caption "— group figure" repeated under both plots reads like an internal provenance note, not audience information ("group figure" means nothing to me; if the point is "we made this," say "T(H)RUST" or drop it). "SD Toolbox" in the bar-chart legend is unexplained.

(c) If ideal efficiency is higher, what is the practically realized gain after losses — is there a number the field agrees on?

(d) The tiny red annotations on the p-v plot are below legibility at presentation distance. Bar chart value labels (rotated numbers on bars) are cramped. Otherwise clean.

## Slide 5 — "The RDE: a detonation made steady in a rotating frame"

(a) In an RDE a detonation front spins around an annulus at near-CJ speed (kHz rate) over continuously injected fresh mixture, and the exhaust is continuous and axial with no valves.

(b) The annulus schematic has text partially obscured: "fresh layer" label overlaps the shaded sector. The teal caption "front view: the fresh-layer fill height H is axial (into the page)" is a footnote-level clarification set in colored italic — I had to squint to parse why it mattered. "products expand axially (out of page) → thrust" and the H remark seem to be pre-seeding something later; as a first-time listener I don't know why fill height deserves this emphasis. "Unwrapped" appears in the right figure caption without the concept being explained yet (it gets explained implicitly by the picture, but a one-word gloss would help).

(c) How many waves typically coexist, and what sets the wave count/stability?

(d) "fresh layer" label collides with the colored arc — looks like a rendering overlap. The two figures have very different visual styles (one minimalist, one busy GALCIT reproduction), which is fine but the right one's labels are small.

## Slide 6 — "Code Development and Capabilities — HYPERDE"

(a) Their in-house framework HYPERDE solves each engine subsystem (chamber, plenum, injectors, expansion) at the dimensionality that best captures its physics: 3D, "unwrapped" Q2D, or quasi-1D.

(b) "Q2D" is used four times and never expanded — I inferred "quasi-2D" but the slide should say it once. "Q2D (unwrapped)" as a mode label assumes I already own the unwrapping concept. "most informative dimensionality" is nice phrasing. "(2D for unwrapped)" in the Plenum box is a parenthetical that took me two reads. "choked and unchoked outflows" fine. The backronym "HYbrid-dimensional PERformance-predictive..." is charming but the mixed-case highlighting (HY...PER...R D E) is visually noisy.

(c) How are the sub-domain solvers coupled — one-way BCs or fully two-way, and at what cost per case?

(d) The four quadrant blocks are text-only; a small block diagram of chamber/plenum/injector/nozzle with the dimensionality tags would communicate this in one glance. No overlaps.

## Slide 7 — "General features of the solvers' suite"

(a) A standard capability checklist: finite-volume, 2nd order space / up to 3rd order time, several turbulence models, tabulated thermally-perfect thermo, yaml chemistry pre-processing, OpenMP+MPI, and interfaces to other in-house solvers.

(b) "II order in space, up to III order in time" — Roman numerals for order is idiosyncratic; "2nd/3rd" is the convention. "Lots of degrees of freedom on numerics" is casual and vague — reads like a filler bullet. "full integration with .yaml chemical datasets" — leading with a file extension is implementation talk; say "Cantera-format chemistry" or similar. The lone "+" between the two horizontal rules is a decorative device whose meaning (and?) is unclear.

(c) Which turbulence models actually get used for RDE runs, and is there any LES capability or plan?

(d) Bullet spacing is uneven (left column has large gaps, right column tight). The centered "+" between rules looks like a typo rather than a design element. No figures at all — weakest-looking slide so far visually.

## Slide 8 — "Q2D solver — innovation w.r.t. recent literature"

(a) Their Q2D (unwrapped annulus) solver is claimed to be more rigorous than existing literature versions: proper diffusive fluxes/RANS, generality to varying channel width z(x,y), and a CFD adaptation of a non-isentropic boundary condition from Fievisohn & Yu.

(b) "non-isentropic BFS boundary condition" — BFS is never expanded (backward-facing step? I only guess because slide 14 later mentions it). "innovation w.r.t. recent literature" is a claim header, not a message — which innovation matters and why? The left diagram is dense with tiny magenta/blue labels ("Lateral Expansion", "Periodic Boundary", A1/A2/B1/B2) at footnote size. Middle figure "Side view inward flow (constant area)" — I could not connect it to the other two figures without narration.

(c) What measurable prediction improves because of this rigor (wave speed? pressure? thrust), compared to the simpler Q2D of the literature?

(d) Three figures of clashing styles and sizes; the left composite has microscopic text; middle figure floats with lots of white space around it. Reference [1] font is fine.

## Slide 9 — "V&V (1D ZND)"

(a) Their CFD reproduces the canonical 1D ZND H2/air detonation structure (T and p vs x) against the SDT reference solution, with visually close agreement.

(b) "SDT" unexpanded (Shock & Detonation Toolbox, I assume — slide 4 said "SD Toolbox", inconsistent naming between slides). The pressure plot shows a visible systematic offset between CFD and ZND downstream — the slide makes no comment; an unexplained gap in a validation slide invites the exact question a panel will ask. Axis fonts are small.

(c) Is the p(x) offset understood (post-shock relaxation, mesh, chemistry), and how large is it in %?

(d) Both plots are small relative to the large empty band under the title; they could be 30% larger. Legend text tiny.

## Slide 10 — "V&V (unwrapped literature test cases)"

(a) Their unwrapped-chamber simulation reproduces the Schwer & Kailasanath 2012 RDE test case, with the wall pressure trace matching the reference in shape and peak.

(b) "'unwrapped' literature test cases" — quotes again around unwrapped; by now commit to the term. Legend "Sapienza CFD" vs "Schwer et al." is clear — good. In the pressure plot the red curve carries a dense comb of spikes that the blue reference doesn't show; no comment on why (injector discreteness?). Left contour "M" colorbar tops out at 1 — a Mach map clipped at 1 is odd and unexplained.

(c) Are the high-frequency spikes physical (discrete injectors) or numerical, and did the reference simply not resolve them?

(d) Empty white column between the two figures; the pressure-plot y-label appears clipped ("p (bar)" partially cut at left edge). Small legend fonts.

## Slide 11 — "V&V (Q2D source terms)"

(a) The Q2D area-variation source terms are verified against the quasi-1D area law on a nozzle (perfect overlay), and the effect of aspect ratio AR on the unwrapped solution and wall pressure is assessed.

(b) The bullet says "Extensive assessment of HYPERDE features (Q2D source terms, Q1D injectors-chamber, Q2D-3D connection)" and bolds the first item — I eventually realized slides 11/12/13 are a series bolding one item each; unguided, the repetition reads like the same slide three times. "AR = 1/0.8/0.6/0.4" — AR of what (annulus width to what?) is not defined. The right plot with four colored jagged traces has no takeaway stated: what should I see? Higher p0 for lower AR?

(c) What is the conclusion of the AR sweep — down to which AR does Q2D remain trustworthy?

(d) Right plot y-label "p0 (bar)" small; the four-curve plot is visually chaotic with no annotation of the message. Frame around middle+right figures groups them, but the left plot floats outside it without explanation of the split.

## Slide 12 — "V&V (Q1D injectors-chamber)"

(a) Three injector treatments (MQ2D, fully resolved Q2D, and a Q2D boundary-condition model) give nearly identical chamber temperature and velocity fields, justifying the cheap model.

(b) "MQ2D", "Q2D Resolved", "Q2D BC" — three internal acronym variants, none defined; MQ2D in particular is pure in-house jargon to me (Multi-? Modified-?). The middle plot is an extremely dense comb of red/black/green oscillations; agreement is plausible but unreadable in detail. No stated takeaway sentence — the claim "the BC model is as good as resolving injectors" is what I *inferred*, not what the slide says.

(c) Which of the three is the production configuration, and what is the speed-up bought by the BC model?

(d) Middle plot overplotted to near-solid color in places; contour figure duplicated from slide 10 (same picture?) which made me flip back to check — if it is the same field, say so; if not, distinguish them.

## Slide 13 — "V&V (Q2D-3D connection)"

(a) A cut of the unwrapped Q2D solution is wrapped back onto the annulus and handed to a 3D solver, showing the pipeline from cheap 2D to full 3D geometry.

(b) The three-panel arrow sequence is actually self-explanatory — best "process" visual so far. But no text states what is being validated: is the 3D field checked against anything, or is this just "it runs"? On a slide titled V&V that distinction matters. The black rectangle on the left figure (the sampling slice, I assume) is unlabeled.

(c) What quantitative check certifies the Q2D→3D handoff (mass flux? pressure continuity at the interface)?

(d) The black selection rectangle looks like a rendering artifact until you infer its purpose — label it "exit slice". Middle annulus figure axis fonts small. Otherwise clean and readable.

## Slide 14 — "Characterization of Refill Region Dynamics (with RMIT and NCSU)"

(a) With partners they study why diverging injector inlets — meant to reduce backward-facing-step separation losses — actually degrade RDE performance, asking how geometry shapes the refill expansion and its stagnation-pressure losses.

(b) The four questions at bottom are good and clear. But the middle strip of four figures (grayscale engine section, annotated schlieren-like schematic, two colored wedge plots "6.5 deg / 7.5 deg", quartz-window photo, plus a 3D wireframe box bottom-right) is a collage from visibly different sources with tiny labels ("relative luminescence", "ε = 7", "10.7 mm") and no per-figure captions or credits — I cannot tell which is experiment, which is simulation, or whose they are. "refill region" itself is used before being defined anywhere in the deck (I inferred it from slide 5's "fresh layer" — the two names for the same thing are never connected).

(c) Whose experiments are these (RMIT? NCSU?) and is the "degraded overall performance" claim from their rig or the literature?

(d) Title wraps awkwardly with "NCSU)" alone-ish on line 2. Figure strip is cluttered; the bottom-right wireframe box overlaps the whitespace near the question list and looks pasted. Question bullets use a different marker style (dashes) than the rest of the deck.

## Slide 15 — "Characterization of Refill Region Dynamics" (Λ sweep)

(a) Sweeping the inlet expansion ratio Λ shows that more expansion creates growing supersonic regions in the refill layer and total-pressure loss, until at Λ=2.9 part of the inlet goes fully supersonic and the pressure gain turns negative (PG = -4.5%).

(b) "PG" is used in the label boxes before ever being defined on a slide (it gets defined on slide 22 — too late; I guessed pressure gain). "Λ", "e = 40 mm", "ε = 7.5°" — three geometric symbols in the panel labels with no legend; I don't know what e and ε are (throat gap? divergence angle?). "(and negative PG)!" with exclamation is fine rhetorically. The green/red overlay curves on the CFD fields (characteristic lines? streamlines? sonic lines?) are never identified — the black contour I inferred is M=1 only because a black label "M = 1" appears in one panel.

(c) What are e and ε, and is there an optimum Λ (the numbers suggest Λ≈1 is best — so why diverge the inlet at all)?

(d) Four dense panels + colorbar squeezed at bottom center with tiny italic label "P, MPa"; annotation arrows at bottom right ("φ = 0.99  φ = 0.2") float ambiguously between panels. Overall the slide is heavy but the ordering of the four panels (Λ = 1, 1.5, 2.9, 1.8 — not monotonic!) forced me to hunt: top-left, top-right, bottom-right, bottom-left is the increasing-Λ order? Non-monotonic panel layout is a real comprehension defect.

## Slide 16 — "Characterization of Refill Region Dynamics" (subsonic vs supersonic refill)

(a) A conceptual model: in subsonic refill, the slip-line pressure history sets both inlet condition and front density, while in supersonic refill part of the expansion decouples from the inlet, splitting the layer into subsonic / supersonic-coupled / supersonic-decoupled zones.

(b) This is the clearest schematic in the section — good. Remaining confusions: "Pressure determining inlet condition" vs "Pressure determining front density" — 'front density' means the density the next detonation front sees? Not obvious. "x_0s" subscript unexplained. "Slip line Pressure" stacked as the y-axis label reads oddly. Why decoupling matters for performance is not stated on the slide — it stands as pure phenomenology.

(c) What is the practical consequence of the decoupled zone — is that where the PG loss of slide 15 comes from?

(d) Large empty band under the title before the figure; figure otherwise well-drawn. Legend colors (blue/orange/dark-blue) small but legible.

## Slide 17 — "Supersonic Bladeless Turbines (with NCSU)" (tunnel design)

(a) The group did CFD design of NCSU's Mach-4-capable supersonic wind tunnel with swappable nozzles and a second-throat diffuser, used to study bladeless (conical, friction-type?) turbines.

(b) "Bladeless turbine" is never explained — as a propulsion engineer I think Tesla/boundary-layer turbine, and the photo shows a grooved cone; one line on the working principle is missing (bullet 3 says they analyze the "working principle" but the slide never states it). "NEUMOTOR BLDC" in the photo callout is lab-inventory jargon (it's just the brand of the electric motor/dyno). The left CFD image (red field with green striated cone wake) has both M and p(kPa) colorbars but I cannot tell which field is displayed.

(c) What does a bladeless turbine buy for an RDE — is this for topping-cycle power extraction from the exhaust?

(d) Left CFD figure is cropped oddly at the top (white notch). The two colorbars on one image are ambiguous. Photo is good.

## Slide 18 — "Supersonic Bladeless Turbines" (tunnel validation)

(a) Tunnel CFD at different feed pressures shows when the test section starts (unstarted at p0 = 3 bar, started at 4), and CFD pressure-ratio distributions match experiment well across four nozzle pressure ratios.

(b) The three header bullets are copy-pasted identically from slide 17 — as a listener this reads as either an error or padding; the slide's actual content (start/unstart + validation) is stated nowhere in text. The four small plots are MATLAB-default styled with tiny titles ("Nozzle Pressure Ratio, P0 = 2.95 Bar") clashing with the deck's typography. In the top-left plot the red CFD curve departs drastically from experiment/isentropic after x≈0.05 with no comment (that IS the unstarted case, I think — say it).

(c) Which condition is the operational envelope for the turbine tests, and what caused the 2.95 bar mismatch (unstart, I presume — confirm)?

(d) Left stack labels "p0 = 3 bar / 4 bar" only cover two of the three fields (a/b/c) — panel (b)'s condition is unlabeled. Four right plots have unreadable axis text. Duplicated bullets = the slide's biggest defect.

## Slide 19 — "Supersonic Bladeless Turbines" (ongoing)

(a) Ongoing work: shape optimization of the bladeless turbine (a matrix of six Mach-field snapshots) and CFD design of an ejector-diffuser for RDE testing, with a photo of the test cell.

(b) The six mini CFD frames have no labels distinguishing them (different designs? different Mach numbers? iterations of the optimizer?) — a 2x3 grid of near-identical red plots communicates nothing specific. The photo is unexplained: is that the NCSU RDE rig the ejector will serve? No caption. "ejector-diffuser system for RDE testing" — for altitude simulation / back-pressure control? One clause would fix it.

(c) What objective does the shape optimization maximize (torque? efficiency?) and with what optimizer?

(d) The 2x3 grid tiles have inconsistent sizes and a stray horizontal rule fragment under the top-right tile; colorbar ranges differ tile-to-tile (0-1.8 vs 0-4.5) with no explanation. Photo uncaptioned.

## Slide 20 — "Disk RDEs (with RMIT and ISAE-ENSMA)"

(a) The group is CFD lead in a PPRIME-lab collaboration on disk (radial) RDEs with H2/air, simulated both in 3D URANS and in their Q2D framework.

(b) "Disk RDE" is never defined — the pictures show an annular-looking torus, and to a first-timer the difference between this and slide 5's annular RDE is not visible from the figures alone (radial outflow vs axial? say it). "PPRIME lab" appears with no tie to the title's RMIT/ISAE-ENSMA (PPRIME is Poitiers = ISAE-ENSMA's lab, but the slide makes me do that join). "(or Euler)" repeated under both figures reads like a hedge — viscous or not? Pick or explain.

(c) Why disk RDEs — compactness? integration with turbines? The slide gives zero motivation.

(d) One-bullet slide: a lot of empty space top-right; the two temperature fields use slightly different colorbar ranges (3450 vs 2800 max) making visual comparison misleading. Left 3D figure's axis triad tiny.

## Slide 21 — "Nozzle Design for RDEs"

(a) They have an in-house non-isentropic method-of-characteristics solver for designing nozzles (ideal/TIC/Rao/plug/shrouded-plug families), the open question is whether an "optimal" profile exists for an RDE exhaust, and 4-7% Isp is at stake — which the next section answers.

(b) Dense abbreviation load: "TIC" (thrust-optimized/truncated ideal contour? not expanded), "MoC" (method of characteristics — expanded nowhere), "Veen" (a name? a family? unknown to me even as a nozzle person — Rao I know, Veen I do not). "three-waves 2D" — three waves of what? "The stakes are real:" box — the phrasing "+4-7% Isp (choked interface) · 58.1→71.5% of ideal (shroud) — the next section is the group's answer" is cryptic: two disconnected number fragments with middle-dot separator, parenthetical qualifiers I can't unpack ("choked interface"? "of ideal (shroud)"?), and "the group's answer" is teaser talk. These are the deck's money numbers and they are illegible on first contact.

(c) 4-7% Isp relative to what baseline, from which reference — [3], [4], or their own work?

(d) The pink stakes box overlaps/crowds the caption "Optimized shrouded plug" and appears to clip its bottom edge against the footer banner; reference [4] text is partially cut by the banner ("Spacecraft and Rockets 56(3), 887-898, 2019" collides with the red bar). Visible layout defect.

## Slide 22 — "This exhaust is periodic — and averaging it is the crux"

(a) Pivot slide: the RDE exhaust is periodic and nonuniform, every published design route starts from an averaged flow, the field's accepted average (EAP, a thrust-equivalent pressure) mis-states performance and has no error bar — and this programme constructs one.

(b) The EAP formula is dropped in whole cloth with undefined symbols: F_g, A_8, P_0, P_t3, P_t8 (station numbering assumed), and "PG = EAP_i/P_t3 - 1" finally defines PG — 7 slides after it was first used. "naive total-pressure averages mis-state performance (the field's own published caution)" — "the field's own published caution" is insider shorthand; cite the actual caution ([ref]) or drop the clause. "our programme constructs it" — constructs the error bar? The antecedent of "it" takes a beat. The gray italic caption "the field's accepted average: a thrust-equivalent pressure — no error bar" under the equation is doing the real work and is styled as a footnote.

(c) Mis-states performance by how much — is the 4-7% of slide 21 that error, or a different number?

(d) The three stacked contour plots on the left are small with tiny colorbar labels ("T/Tref", "Log(P/Pref)", "Mx") and their relevance (nonuniformity evidence) is only carried by the caption. Right column text well-set. Acceptable slide, but the equation-with-undefined-symbols is a real barrier.

---

## Section verdict (slides 2-22)

Strengths: honest, well-structured arc (group → tools → V&V → research lines → nozzle bridge → averaging hinge); slides 13 and 16 are genuinely self-explanatory; the deck avoids AI-flavored filler prose almost everywhere.

Systemic defects:
1. **Acronym debt**: Q2D, MQ2D, BFS, SDT/SD-Toolbox (inconsistent), TIC, MoC, Veen, PG, Λ/e/ε — most used before or without definition. PG defined on slide 22 but used on slide 15.
2. **Figures without takeaways**: slides 11, 12, 18, 19 show data but never state the sentence the data proves.
3. **Provenance captions read internal**: "— group figure" (slide 4), uncredited collage (slide 14), uncaptioned photos (19).

## Three weakest slides of the section

1. **Slide 21 (Nozzle Design for RDEs)** — the deck's own bridge slide, carrying the money numbers, delivered as a cryptic fragment box ("+4-7% Isp (choked interface) · 58.1→71.5% of ideal (shroud)") with unexplained qualifiers, plus TIC/MoC/Veen/"three-waves" jargon and a visible layout clip against the footer. The single most consequential slide to fix.
2. **Slide 18 (Bladeless turbines, tunnel validation)** — header bullets duplicated verbatim from slide 17, the slide's actual message (start/unstart + validation quality) never written, unlabeled panel (b), unreadable MATLAB-styled sub-plots, unexplained gross CFD-experiment divergence in the top-left plot.
3. **Slide 15 (Refill Λ sweep)** — key physics result presented with three undefined symbols (Λ, e, ε), PG used before definition, unidentified overlay curves, and a non-monotonic Λ panel ordering that forces the audience to hunt for the trend.

(Runner-up: slide 12 — three undefined acronym variants (MQ2D/Q2D Resolved/Q2D BC) and no stated conclusion.)
