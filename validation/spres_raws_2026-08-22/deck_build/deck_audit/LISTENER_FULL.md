# LISTENER_FULL — First-time technical listener audit (ESA briefing persona)

Auditor persona: aerospace propulsion engineer, zero prior exposure to this project.
Judged ONLY the 46 rendered slides (s-01..s-46), in order. Format per slide:
**takeaway** (one line) · `jargon/confusion` · **Q:** open question · **defect:** visual issue.
"FAIL" = I could not paraphrase the slide from what is on it.

---

## Per-slide walk

**s-01** — Title: Sapienza team presents its Rotating Detonation Engine activities ("T(H)RUST") to ESA. · Clean. · Q: is T(H)RUST a project acronym or a pun? · defect: none.

**s-02** — Agenda: group → RDE exhaust → their formulation → a "design machine" → honesty/roadmap, with three requests at the end. · "The design machine" is intriguing but opaque at this point. · Q: requests for money, data, or endorsement? · defect: none.

**s-03** — A ~1.5-year-old RDE group doing URANS/low-order modelling with US/Australian/French partners and an in-house framework called HYPERDE. · `"Newborn" in scare quotes; the red double-arrow between HYPERDE and "Open research lines" conveys nothing`. · Q: how many people/FTEs is this group? · defect: bottom-right text block nearly touches the footer bar.

**s-04** — Detonation gives pressure gain without a compressor, hence better ideal efficiency. · `ZND/von-Neumann annotations in the p-v plot are tiny; "SD Toolbox" unexplained`. · Q: how much of the ideal gain survives in practice? · defect: red annotation text in left figure is near-illegible at room distance.

**s-05** — An RDE is a detonation wave made steady in a rotating frame: kHz rotating front, continuous refill, valveless axial exhaust. · Clear, good pedagogic slide. · Q: none blocking. · defect: "fresh layer" label collides with the teal fill in the ring sketch.

**s-06** — HYPERDE solves each engine subsystem (chamber/plenum/injectors/expansion) at the "most informative dimensionality". · `Q2D and "unwrapped" are used before being defined — I inferred quasi-2D but only from context`. · Q: what does Q2D actually collapse — the radial direction? · defect: none.

**s-07** — Their solver suite is a fairly standard FV URANS stack (2nd order space, tabulated thermo, MPI) with modular options. · `Bullet-list slide; "Lots of degrees of freedom on numerics" reads as filler`. · Q: is the code public/shared or proprietary? · defect: the lone "+" between the two rule lines looks like a typo rather than a design element.

**s-08** — Their Q2D solver is claimed novel vs literature: rigorous diffusive fluxes, generic width variation, a BFS-type non-isentropic BC adapted to CFD. · `"BFS" never expanded (backward-facing step? the citation suggests something else); left diagram is a dense reproduction with microscopic labels`. · Q: what exactly is new vs Fievisohn & Yu? · defect: left figure labels illegible; three unrelated figure styles side-by-side.

**s-09** — Their CFD matches a 1D ZND H2/air benchmark. · `"SDT" acronym unexplained (Shock & Detonation Toolbox, I assume)`. · Q: pressure curves visibly diverge downstream — is that resolved-vs-model or a defect? · defect: plots small, much empty space top-right; slide is half blank.

**s-10** — Their CFD reproduces the Schwer & Kailasanath unwrapped RDE test case. · Fine. · Q: what grid/cost was needed for that agreement? · defect: right plot's legend partially overlaps gridlines; left/right figure heights mismatched.

**s-11** — Q2D source terms verified: nozzle-like area law recovered, and aspect-ratio sweep shows pressure effects. · `The three panels are three different stories (verification, flowfield, AR sweep) crammed under one bullet`. · Q: what am I supposed to conclude from the AR=0.4 spaghetti plot? · defect: right plot is unreadable line-spaghetti; "AR = 0.4" caption floats ambiguously.

**s-12** — The Q1D injector model matches resolved-injector simulations. · `MQ2D appears in the legend, never defined; three near-identical acronyms (MQ2D / Q2D Resolved / Q2D BC) undecipherable to me`. · Q: which of the three curves is "truth"? · defect: middle plot axis labels cramped; legends duplicated across panels.

**s-13** — Q2D chamber output can be lifted into a 3D expansion simulation (their hybrid coupling works end-to-end). · Good visual left-to-right arrow story. · Q: is the 3D case validated against anything, or just demonstrated? · defect: none serious.

**s-14** — Side project 1: physics of diverging-inlet refill regions (with RMIT/NCSU); geometry hurts performance and they ask why. · `Text-heavy; hyphens used as second-level bullets read as typos; figure strip is five thumbnails with tiny labels`. · Q: none — the four posed questions are actually good. · defect: title wraps and pushes body text up against it; bottom-right 3D sketch overlaps the footer region.

**s-15** — More inlet expansion (Λ up) creates supersonic refill zones and can even destroy pressure gain (PG negative at Λ=2.9). · `Λ, e, ε, PG all thrown in the panel labels at once; "PG" must be back-inferred from slide 4's title`. · Q: is Λ area ratio? (never stated). · defect: colorbar tiny and vertical-label rotated; four panels visually noisy with red/green streamline hash.

**s-16** — A conceptual model splits refill into subsonic vs supersonic (coupled/de-coupled) regimes based on where expansion lines land. · Genuinely nice explanatory figure. · Q: has this model been checked against the CFD of s-15? · defect: none.

**s-17** — Side project 2: they design a Mach-4-capable wind tunnel at NCSU to study bladeless conical turbines. · Clear. · Q: what does a "bladeless turbine" extract work from — shear? · defect: left CFD figure has no caption; both figures uncaptioned.

**s-18** — Their tunnel-nozzle CFD matches experiments across pressure ratios. · `The three header bullets are copy-pasted verbatim from s-17 — as a listener I checked whether the slide had advanced`. · Q: what causes the CFD-isentropic gap at high PR? · defect: repeated header text (real defect for a talk); MATLAB-default plots with tiny titles.

**s-19** — Ongoing: turbine shape optimization and ejector-diffuser design for RDE testing; hardware exists. · Six thumbnail CFD frames + a lab photo, none labelled. · Q: which of the six frames is the optimized shape? · defect: thumbnails have illegible axes; a stray horizontal line floats under the top-right thumbnail.

**s-20** — Side project 3: disk ("radial") RDEs with PPRIME, simulated both 3D and Q2D. · Minimal but clear. · Q: does Q2D capture the disk wave count correctly? · defect: half the slide is white space; one-bullet slide.

**s-21** — Pivot to the main act: an in-house MoC nozzle-design API (ideal/Rao/Veen families) and the open question "does an optimal RDE exhaust profile exist" — with a claimed +4–7% Isp at stake. · `"three-waves 2D MoC" and "TIC" unexpanded; "Veen" dropped as if famous`. · Q: what does "58.1→71.5% of ideal (shroud)" mean — of what baseline? · defect: **"Optimized shrouded plug" caption collides with "The stakes are real" box; reference [4] text is clipped by the footer bar** — visibly broken.

**s-22** — Core problem statement: everyone designs on an averaged exhaust flow, the accepted average (EAP) mis-states performance and carries no error bar; they will construct one. · `"our programme constructs it" — first taste of programme-speak; the EAP formula is shown but not walked through`. · Q: mis-states by how much (deferred, fair)? · defect: equation image slightly small; left figure axis labels tiny.

**s-23** — One nozzle owns three different flowfields: instantaneous (rotating shock), time-averaged, and the fictitious steady one the field designs on; even the throat is unsteady (~6:1 excursions). · Strong slide, the deck's thesis clicks here. · Q: 6:1 excursions of what quantity? · defect: right column's two stacked citations cramped; left double-figure caption font very small.

**s-24** — Survey of current practice: four published RDE-nozzle design routes, all on averaged/substitute flow; nobody quantifies the substitution error. · Good gallery layout. · Q: none. · defect: **the bottom banner's second line ("...the substitution error is never quantified.") is clipped by the footer bar** — the punchline is the damaged text.

**s-25** — Evidence: same hardware, steady-designed vs transient evaluation diverges (up to −5.78%) and even inverts rankings — and nobody prices this. · Numbered callout boxes work well. · Q: is this their own solver's replication or just the cited paper's data? · defect: middle column has two tiny stacked figures with 6-pt captions.

**s-26** — Historical warning (1971): changing only the base-pressure closure moved the optimum contour markedly, and that closure is still used while RDE base pressures sit far from steady predictions. · Persuasive. · Q: does the ×2.45 optimum shift matter if the value changed only +0.26%? (the slide even shows the tension — good). · defect: scanned 1971 table is decorative noise; illegible.

**s-27** — Their claim of lineage: 70 years of variational nozzle design (Rao→Kraiko et al.), which they now extend to periodic flow. · `"no cycle measure, no quotient, no certificates" — 'quotient' and 'certificates' are internal vocabulary, undefined; "A 1975 Russian precedent is still in procurement — not yet read against the original" is process talk that belongs in a status memo, not on the slide`. · Q: what is the 1975 precedent and does it undercut novelty? · defect: 6 timeline boxes of very unequal text density; the Rao equation strip sits disconnected below.

**s-28** — The field itself says maximum-thrust theory is only "approximately applicable"; sizing (~1%) is fine but geometry RANKING is open; their thesis: quantify "approximately". · Crisp, my favorite rhetorical slide. · Q: none. · defect: none.

**s-29** — They declare the ancestors of the per-phase idea and claim their variational-optimum-on-the-family question was never posed. · `The tiny inequality strip "⟨F/p⟩ ≠ ⟨F⟩/⟨p⟩ … bias = O(Var) on 10:1 cycles" is the only mathematics and it is nearly invisible`. · Q: what does "never design, never a family" mean grammatically? · defect: **the highlighted "This programme" box is ~70% empty white space with a microscopic formula at the bottom — the deck's central novelty claim is visually the emptiest box on the slide**.

**s-30** — The two optimization problems: average-then-optimize (the field, a substitute problem) vs formulate-the-periodic-optimum (them); a "deciding theorem": only the weighted mean satisfies the wall condition. · `"averaged transversality & corner conditions", "a.e. on the shared wall" — the wall was never introduced; the two functional equations flash by undefined (what is Ξ, μ(ξ), g_L?)`. · Q: what physically is the "shared wall" — one contour serving all phases? (I *think* yes, but I am guessing.) · defect: equations set small and inline between panels.

**s-31** — FAIL as a standalone: three regimes where their problem does/doesn't coincide with the classical one; I get the headline (truncated plug breaks the coincidence) but not the content. · `"certified closures", "the plug weakly dominates the bell", "tie region characterized", "closures at equal area ratio, never hardware", "+44–87% (3–10 s of Isp)" — a unit mix I could not parse; "The machine is ready: it is the first campaign" is pure internal process talk`. · Q: what is a "certified closure"? · defect: text-only slide at the moment I most needed a picture of the three configurations.

**s-32** — Per-phase is an exact change of coordinates (wave frame, azimuth=phase), not an approximation — except one declared O(St) term; global time-averaging is the cruder reduction. · `"one declared O(St) approx." — Strouhal? never said; the box "Proof structure declared; complete proof in progress — stated openly" reads as AI/audit flavor and, worse, tells me the deciding theorem of s-30 may not be fully proven`. · Q: so is the s-30 "deciding theorem" proven or not? · defect: ring diagram's segmented wheel could show phases more explicitly; right-bottom box overlaps the diagram zone awkwardly.

**s-33** — The design variable is a solid body in an envelope; nozzle classes (bell/plug/shrouded/E-D) emerge as outputs; first verdict: plug weakly dominates bell at "certified closures". · `Dense internal vocabulary: "named campaign", "driver today — 9 DOF", "certified splines per sector, no level-sets", "an infinitesimal body in supersonic flow pays only wave drag", "named owners and windows" — this is the project's internal ledger leaking onto a slide`. · Q: what is a "sector" here? · defect: left diagram boxes carry captions ("named campaign") that mean nothing to outsiders.

**s-34** — Pressure alone can't rank designs (swirl changes thrust 1.5–3% at same gauge reading), so boundary data must carry the full state — standard practice, and their Q2D provides it. · Nice gauge cartoon. · Q: none. · defect: large empty band below the bullets.

**s-35** — The interface state swings hugely over a cycle (pt ~4:1, Tt ~40%, M 0.85–1.33) and the sonic surface is corrugated — they measure per phase, never assume. · Good, evidence-backed. · Q: none. · defect: middle table borders faint; right cartoon's red annotations tiny.

**s-36** — What their reduction discards is an explicit operator: mean channel exactly zero (proven), front jumps (no number yet — declared weak point) and covariance survive; both measurable. · `"the declared HEEL" — capitalized internal codeword; "machine-verified identities"`. · Q: how big could the front-jump channel plausibly be? · defect: left flow-diagram text at ~6 pt; yellow "covariance" box hue breaks the deck palette.

**s-37** — Adjoint explainer: one forward + one backward solve gives the exact full gradient vs N finite-difference solves. · Textbook-clear; the best "teach one concept" slide in the deck. · Q: none. · defect: figure occupies top-left; large white void below it.

**s-38** — The design machine pipeline: data → functional → flow solve → adjoint → optimizer → certify, seconds per design step, every choice recorded with a rejecting test. · `"ships inside a chain built to reject it", "open choices declared, with a named lead and date" — internal audit language`. · Q: certification by whom — is "certify" a self-check? · defect: six boxes' fonts small; the teal annotation arrow text crowds the boxes.

**s-39** — FAIL by emptiness: three assertions about the optimizer (measured-curvature trust-region Newton; exact discrete gradient; a 2026 solver candidate will be re-examined). · `"comparison pre-registered at equal constraints — the solver census is dated" — I cannot tell what was compared or why the census being dated matters`. · Q: which 2026 solver? · defect: **three tall boxes each ~80% empty; the slide has ~40 words of content in a full-slide frame**.

**s-40** — Sanity anchor: their independent variational route reproduces the classical Rao contour to ~2e-3 of throat radius. · Exactly the validation a skeptic wants; well done. · Q: reproduced for which single operating condition? · defect: plot small and left-shifted, right half of slide underused; grey tolerance-band legend text tiny.

**s-41** — Speed table: 0.45 s per evaluation+gradient, 15–20 s per segment, 10–14 min full campaign, 18× vs reference, all under target. · `"Our measurements, host declared" — meaningless to me; "invariance gate" jargon`. · Q: what hardware is "host"? · defect: right bar chart adds nothing beyond the table and its grey segments are unexplained.

**s-42** — Honest error budget by channel: proven zeros, 1.5–3% swirl debt, up to 9% data-fidelity, two channels with no number yet; their single quantified gain is +0.51% ± ~30%. · `"Swirl booking debt" — is that a translation artifact? "the heel" again; "we close the bracket, or it stays open"`. · Q: the headline gain +0.51% with ±~30% (of what? relative?) — is the entire program's benefit currently indistinguishable from zero? · defect: table row shading faint; long cell texts wrap awkwardly.

**s-43** — The honest map: their design sits between the mean-state design (never head-to-headed by anyone) and the incomputable true 3D optimum; hypothesis: the formulation gap dominates, falsifiable, with the front-jump caveat. · `"three gaps: formulation · model · composition" named once and never unpacked; "Programme failure needs two independent misses" took me three reads`. · Q: what exactly is the "composition" gap? · defect: middle teal box carries a 3-line hypothesis in small italic-adjacent text — the deck's core bet deserves bigger type.

**s-44** — The 4-step plan, in order (residual → head-to-head → paired coupled run → 12M-cell reference), each with pre-registered decision rules and a ~1%-Isp stop criterion. · `"decided after the residual — today: channel, not commit", "bar holds → ~1% sizing stands" — telegraphic internal shorthand; "pre-registered" used three times`. · Q: calendar timeline? No dates anywhere. · defect: box 1 vs boxes 2–4 border colors differ without explanation (red vs teal — status? priority?).

**s-45** — The three asks: a partner/procurement for the 12M-cell reference run, engine data in the declared class, and publication/procurement endorsement. · `Ask 3 "venues for the method papers + three key papers we cannot access" — asking ESA for paywalled PDFs on a briefing slide is odd; bottom box "Data is not fed in: it is admitted — and the entry gate can say no" is poetic but cryptic, and "(A contract prediction — not yet exercised on real data.)" undercuts it`. · Q: what budget/compute size is ask 1, in CPU-hours or euros? · defect: three boxes again mostly empty in their lower halves.

**s-46** — Closing: first per-phase variational RDE-nozzle method, explicit discarded operator, honest channel-by-channel error bracket; minutes-scale validation; honesty built in. · Decent summary. · Q: none. · defect: **the pipeline recap figure is a shrunken, illegible copy of s-38 dropped ON TOP of the footer bar, clipping the footer text ("Ro..."/"(H)RUST team") — the last thing the audience sees is a layout collision**.

---

## Where attention sagged

1. **s-09 to s-12 (V&V wall).** Four consecutive slides of small validation plots with near-identical headers and legend-alphabet-soup (Q2D/MQ2D/Q2D-BC/AR). The pass/fail message of each is never stated on-slide; I coasted.
2. **s-17 to s-20 (side-project tour).** Interesting per se, but by s-19's six unlabeled thumbnails I had lost the thread of why ESA is hearing this before the main topic; s-18 repeating s-17's bullets verbatim made it feel padded.
3. **s-29 / s-31 / s-33 / s-39 (the theory-status cluster).** Text-only or near-empty slides carrying the *most important* claims, in internal vocabulary ("certified closures", "sectors", "campaigns", "named owners"). This is where I stopped nodding and started writing down words I didn't understand.

## Where the thread broke

- **s-30 → s-31.** s-30 sets up "two problems" beautifully; s-31 then adjudicates coincidence/non-coincidence using terms ("certified closures", "tie region", "contouring", "sector") that had never been defined. I could follow the *headline* (truncated plug = the interesting case) but not the *argument*. This is the single largest comprehension cliff.
- **s-36 onward, the private vocabulary.** "HEEL", "channels", "campaign", "bracket", "pre-registered", "named lead and date" — the deck slides into speaking its own project-management dialect. Each word is guessable; the accumulation is alienating and reads like an internal audit trail (or AI-assisted process log) rather than a technical briefing.
- **s-32's admission** ("complete proof in progress") retroactively destabilizes s-30's "deciding theorem" — as a listener I no longer knew which of the boxed claims labelled "proven" are theorems and which are declarations of intent.

## The 5 worst slides

1. **s-31** — the pivotal theoretical result delivered as undefined-jargon text with no figure; I could not reconstruct the argument (FAIL).
2. **s-39** — three ~80%-empty boxes; ~40 words on a full slide; the third box is indecipherable ("the solver census is dated") (FAIL).
3. **s-29** — the deck's central novelty claim is a mostly-blank highlighted box with a microscopic formula; visually asserts emptiness where it means originality.
4. **s-46** — closing slide with an illegible shrunken diagram physically clipping the footer bar; ends the talk on a visible layout bug.
5. **s-33** — internal project ledger ("named campaign", "9 DOF driver", "owners and windows") presented to an external audience; content likely strong, packaging opaque.

Runner-up: **s-21** (caption/box collision and footer-clipped reference on the slide that launches the whole main act); **s-24** (footer clips the punchline banner).

## The 3 questions I would ask in the room

1. **"Your only quantified in-class gain is +0.51% with ±~30% — relative or absolute? — while your own stop criterion is ~1% Isp. What evidence should convince us the periodic-optimum gap is worth a campaign before the front-jump channel — your declared heel — even has a number?"**
2. **"On slide 30 you call the weighted-mean wall condition 'the deciding theorem', but slide 32 says the complete proof is in progress. Exactly which of the results you stamped 'proven' today are theorems under stated hypotheses, and which are conjectures?"**
3. **"The per-phase formulation needs phase-resolved interface states. From a real engine we get high-speed pressure at best — how do you reconstruct the full per-phase state (Tt, M, swirl) from measurable data, and what does your 'entry gate' do when the data can't support the declared class?"**

## Verdict on the arc

The spine — pressure-gain → RDE → our tools → the exhaust is periodic and everyone averages it wrong → nobody prices the error → we formulate the periodic optimum → a fast audited machine → honest error budget → plan → asks — is genuinely good and the honesty posture is distinctive. Slides 22–28 and 34–37 would stand in any venue. But the deck's crown jewels (s-29..s-33, s-39) are its weakest artifacts: text-heavy or near-empty, written in an internal dialect ("certified closures", "HEEL", "campaigns", "named owners", "pre-registered") that no first-time listener possesses, and s-32 quietly concedes that the flagship theorem is unfinished. Mechanical defects (footer collisions on s-21/s-24/s-46, verbatim-repeated headers on s-17/s-18) say "not proofread" to a review panel.
