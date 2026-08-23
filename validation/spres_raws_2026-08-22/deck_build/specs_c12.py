# -*- coding: utf-8 -*-
"""S-PRES deck — Part C, sections C-I (real exhaust & field practice) and
C-II (the problem & our framework). 17 new slides: C1..C6+C3-bis,
C7..C12 + bis/ter/pre.

Content-of-record: STORYBOARD_v3.md v3.1 (approved). Gate decisions
wired: twin PB-2 = (b) honest form (C7-ter). Critic notes wired: FD-2
(C2 'the four studies we are about to see'), FD-3 (C5 gloss in notes),
FD-5(i) (C7-ter 'numerical test bench'). Guard 18 everywhere: process
names/classes/counts live in 'notes' only; physical & paper numbers stay
on slide. Guard 15: [PROVENANCE] rows in notes = claim -> anchor ->
class -> convergence.
"""

SLIDES_C12 = [
    # ------------------------------------------------------------------ C1
    dict(
        id="C1", kind="new", layout="dichotomy_figs", minutes=1.0, cut="no",
        title="One nozzle, two flowfields",
        content=dict(
            main_fig=("figs_paper/pc_fig10_dichotomy.png",
                      "Transient (left) vs reference steady state (right) — Li, Xu, Lv, Yu, Zhou, Aerosp. Sci. Technol. 158:109878 (2025), Fig. 10"),
            thumbs=[
                ("figs_paper/pd_fig9.png", "Instantaneous internal flow — Jourdaine et al., PCI 37 (2019), Fig. 9"),
                ("figs_paper/pd_fig4.png", "Time-averaged exhaust — Jourdaine et al., PCI 37 (2019), Fig. 4"),
            ],
            bullets=[
                "Instantaneous: a rotating oblique shock. Time-averaged: a clean axisymmetric plume.",
                "And a third field exists: the steady state the field designs on (left figure, right panels).",
                "Even the throat is unsteady: a corrugated sonic surface, ~6:1 excursions — we design downstream of it.",
            ],
        ),
        notes=(
            "SCRIPT: Start from what the exhaust actually is. Freeze time: a "
            "rotating oblique shock, a helix through the nozzle - Jourdaine's "
            "Fig. 9. Average over a cycle: a clean, steady-looking "
            "axisymmetric plume - their Fig. 4. Both pictures are true; they "
            "are different fields. And the large figure shows a THIRD field: "
            "on its right panels, not the time-average but the reference "
            "STEADY state - the flow the field actually designs on. Keep the "
            "three apart: instantaneous, time-averaged, steady-equivalent. "
            "Four independent codes show the same phenomenology.\n"
            "[USER CATCH 2026-08-23 - source-verified] P-C Fig.10 caption "
            "verbatim (pdf p.9): 'Mach numbers ... for transient (left) and "
            "reference steady states (right)' - the right panels are the "
            "STEADY COMPANION, not a time-average. Slide caption and bullets "
            "repaired accordingly; P-D Fig.4 caption verbatim: 'Time-"
            "averaged exhaust flow structure' (true average), Fig.9: "
            "instantaneous internal flow. FINDING vs frozen atlas (pending "
            "mint at R3 close, BUILD_LOG): CH5 §1 lists P-C Fig.10 among "
            "the 'istantaneo vs medio' dichotomy instances - at source it "
            "is transient-vs-reference-steady; P-B Fig.14 likely same class "
            "(to check at mint).\n"
            "[PROVENANCE - guard 15] Dichotomy instances -> CH5 §1 anchors "
            "(with the correction above); class [ADV], CT-6 (their figures, "
            "full citations on slide). Convergence: 4-paper campaign, 0 "
            "BREAK (S-FOUNDATIONS-C4).\n"
            "[GUARD 18] no process language on slide."
        ),
    ),
    # ------------------------------------------------------------------ C2
    dict(
        id="C2", kind="new", layout="c2_throat", minutes=0, cut="pos4", to_backup=True,
        title="The throat is not steady — and not the design interface",
        content=dict(
            fig1=("figs_paper/kp18_fig6_sonicline.png",
                  "Corrugated sonic line — Kaemming & Paxson, AIAA 2018-1101, Fig. 6"),
            fig2=("figs_paper/kp18_tab1_throat.png",
                  "Published throat statistics — ibid., Table 1"),
            fig3=("figs/fig_c2_interface.png", None),  # home micro-schema
            bullets=[
                "The sonic line is corrugated — M = 1 crossed twice per cycle; ~6:1 throat excursions.",
                "Design interface: the supersonic-with-margin station downstream of heat release.",
                "None of the four studies ahead declares its data class.",
            ],
        ),
        notes=(
            "SCRIPT: Zoom on the throat. It is not steady - the sonic line "
            "corrugates and crosses Mach one twice per cycle - and with heat "
            "release downstream, it is not even the right design interface. We "
            "design at the station that is axially supersonic with margin, "
            "downstream of the heat release. One more fact you will not find "
            "stated in the design papers: the data class - a clean periodic "
            "rotating wave - is exhibited in the CFDs, never verified "
            "spectrally.\n"
            "[PROVENANCE - guard 15] Sonic line + Table 1 -> CH10-feed-3 "
            "(Γ_d interface: THEOREM T-TH0/T-NSW backing) + CH10-feed-4 "
            "(KP18 = kaemming_paxson_2018, [IO], CT-6). 'Nobody declares the "
            "class' -> CH10-feed-6 + CH5-feed-5 (search-proven, bounded to "
            "the read corpus - query-bounded wording lives HERE). Guard 11: "
            "Γ_d is NOT 'the throat' - margin station per L4-DEFAULT; "
            "corrugated sonic line (KP18) is the reason; subsonic patches = "
            "declared case-class (D1 4.3bis O1-O4), never silently averaged. "
            "FD-2 applied: 'the four studies we are about to see' "
            "(forward-declared, resolved in C3).\n"
            "[GUARD 18] 'search-proven' and class names in notes only."
        ),
    ),
    # ------------------------------------------------------------------ C3
    dict(
        id="C3", kind="new", layout="grid4_methods", minutes=1.5, cut="no",
        title="How the field designs RDE nozzles today",
        content=dict(
            grid=[
                ("figs_paper/pa_ramp_profile.png",
                 "Angelino-type ramp on averaged flow — Liu et al. 2022",
                 "Liu et al., Aerosp. Sci. Technol. 120:107300 (2022)"),
                ("figs_paper/pb_moc_profile.png",
                 "Classical max-thrust MoC on averaged inflow — Li et al. 2023",
                 "Li, Xu et al., Aerosp. Sci. Technol. 136:108221 (2023)"),
                ("figs_paper/pd_setup_cone.png",
                 "Non-optimized conical spike — Jourdaine et al. 2019",
                 "Jourdaine et al., Proc. Combust. Inst. 37:3443 (2019)"),
                ("figs_paper/pm_contour.png",
                 "Manual CFD-guided redesign — Paxson & Miki 2022 (NASA)",
                 "Paxson & Miki, AIAA (2022)"),
            ],
            takeaway=("Best of a sweep is not an optimum — and in a systematic census, no published "
                      "work poses the optimum on the real RDE exhaust: the substitution error is never "
                      "quantified."),
        ),
        notes=(
            "SCRIPT: The four published design routes, each with its own plot. "
            "Peking University: an Angelino-style ramp built on averaged flow. "
            "Nanjing: classical maximum-thrust surfaces - Rao, Vander Veen - "
            "fed with averaged inflow. KIT and Aoyama: a cone, declaredly not "
            "optimized. NASA Glenn: manual, CFD-guided redesign. All "
            "legitimate engineering - and none closes the loop: the best of a "
            "sweep is not an argmax.\n"
            "[PROVENANCE - guard 15] The 4 methods -> v1 C3 rows + CH5 §1 "
            "(P-A/P-B/P-D/NASA-Glenn method attributions, id registry "
            "verbatim: PKU liu_2022; NUAA li_xu_lv_lv_song_2023; KIT/Aoyama "
            "jourdaine_2019; NASA-Glenn paxson_miki_2022). Best-of-sweep != "
            "argmax rule -> CH8-feed-5 (guard 8: sweep numbers presented as "
            "certified best-of-sweep, never global optimum without M1-M5 "
            "mechanism). Guard 4: field ALWAYS instantiated (PKU/NUAA/KIT-"
            "Aoyama/NASA-Glenn named, never 'the field' bare). CT-6 on all "
            "four crops.\n"
            "[GUARD 18] guards cited here, not on slide."
        ),
    ),
    # --------------------------------------------------------------- C3-bis
    dict(
        id="C3-bis", kind="new", layout="table_claim", minutes=0, cut="merged-into-C3", to_backup=True,
        title="The optimization that has never happened",
        content=dict(
            table_header=["published work", "what is actually optimized"],
            table=[
                ("Liu et al. 2022", "trade study, 4 cases — no optimizer"),
                ("Li et al. 2023", "classical steady surfaces on averaged inflow — the substitute problem"),
                ("Li et al. 2025", "no new design"),
                ("Jourdaine et al. 2019", "conical — declaredly not optimized"),
                ("Paxson & Miki 2022", "manual CFD-guided redesign"),
                ("nearest neighbours", "an ideal bound (no design); direct search (no optimality conditions)"),
            ],
            claim=("In a systematic census: no published work poses the optimum on the real RDE "
                   "exhaust — and the substitution error is never quantified."),
        ),
        notes=(
            "SCRIPT: Sharper: who optimizes what. Nanjing deserves precision: "
            "that work DOES use classical variational calculus - what is "
            "missing is the optimization of the true problem. The two nearest "
            "works outside the quartet: Kraiko-Egoryan's ideal bound - a "
            "bound, not a design - and Levin's direct search without "
            "optimality conditions. Our central claim, within a systematic "
            "census: nobody poses the optimum on the real exhaust, and nobody "
            "prices the substitution.\n"
            "[PROVENANCE - guard 15] Central claim -> CH5-feed-1, BINDING "
            "FORM WB1-C3-10 (never bare 'nobody optimizes'; ISABE [SE] caveat "
            "lives here, recallable aloud: ISABE-2003-117 near-miss named in "
            "litmap; claim query-bounded per guard 9 - three adversarial "
            "passes, G5 residual declared). P-B caveat -> CH4-feed-8 "
            "([ADV]+[REP]: absorbed in the table cell 'does use variational "
            "calculus'). No globality mechanism in the four -> CH8-feed-6. "
            "Nearest neighbours -> v1 C3-bis (Kraiko-Egoryan 2020 bound; "
            "Levin et al. 2010 direct search).\n"
            "[GUARD 18] 'NOT-FOUND(q)/query-bounded' wording in notes only; "
            "on-slide phrasing = 'as far as a systematic census allows us to "
            "verify'."
        ),
    ),
    # ------------------------------------------------------------------ C4
    dict(
        id="C4", kind="new", layout="c4_chain", minutes=2.0, cut="MAI",
        title="Same hardware, two flowfields — and the optimum moves",
        content=dict(
            main_fig=("figs_paper/pb_fig15_cfx.png",
                      "Steady vs transient thrust coefficient across truncation — Li, Xu et al., AST 136:108221 (2023), Fig. 15"),
            side_fig=("figs_paper/pc_fig13_ranking.png",
                      "Thrust coefficient, transient vs steady, five cowl/spike settings — Li, Xu et al., AST 158:109878 (2025), Fig. 13"),
            thumb=("figs_paper/pb_fig16_feedback.png",
                   "Nozzle→chamber feedback with truncation — ibid. 2023, Fig. 16"),
            steps=[
                ("1", "Same solver, paired runs: steady-from-averages differs from transient — and the nozzle feeds back into the chamber."),
                ("2", "Steady curve flat (0.965–0.971) where the transient peaks at 40% (+0.52%) and falls at 80% (−5.78%); the ranking of five cowl/spike settings inverts (0.2–1.5%)."),
                ("3", "No published work prices this error."),
            ],
        ),
        notes=(
            "SCRIPT: The chain, in three acts, on THEIR data - same solver, "
            "paired runs. One: the fields differ, and the nozzle talks back to "
            "the chamber as truncation changes - which forbids assuming "
            "decoupling without verifying choking. Two: the difference reaches "
            "design - the steady curve is flat exactly where the transient has "
            "a real optimum and a real cliff; the true optimum is INVISIBLE to "
            "the curve the field designs on; and rankings between geometries "
            "invert mid-table. Three: nobody prices this substitution error.\n"
            "[PROVENANCE - guard 15] Fig.15/Fig.13 -> CH5-feed-2 ([ADV], "
            "CT-6, page-verified pp.10-11); Fig.16 feedback -> CH5-feed-4 "
            "([ADV-FIG], threat CT-1 adjacency). GUARD 17 (binding, user pin "
            "CKP-S2-1): NO decoupling/one-way-BC claim without the choking "
            "condition stated - upstream decoupling only under convergent "
            "pre-throat AND fully sonic/supersonic throat along cycle and "
            "azimuth; subsonic patches (even throatless) are the information "
            "channels upstream - binds the spoken line and every Q&A answer "
            "on this slide. Their steady companion is GLOBAL-averaged - "
            "cruder than our per-phase (honesty note, spoken if asked).\n"
            "[GUARD 18] paper numbers on slide (allowed); threat ids here."
        ),
    ),
    # ------------------------------------------------------------------ C5
    dict(
        id="C5", kind="new", layout="fig_bullets", minutes=1.0, cut="no",
        title="A 1971 warning: the closure alone moves the optimum",
        content=dict(
            fig=("figs_paper/hum_table.png",
                 "Optimum shift under base-pressure model swap — Humphreys, Thompson & Hoffman, AIAA J. 9(8):1581 (1971), pp. 1586–87"),
            fig2=("figs_paper/hum_contour.png", None),
            fig3=("figs_paper/harroun_fig13_base.png",
                  "Base pressure, steady vs RDE (CFD + five hot-fire tests) — Harroun, Heister & Ruf, JPP 37(5):660 (2021), Fig. 13"),
            bullets=[
                "Only the base-pressure model changes: the optimum moves ×2.45 (value: +0.26%).",
                "The same closure is still in use — and RDE hot-fire base pressure sits far from steady predictions: 0.59 vs 0.95 atm (Harroun et al. 2021).",
            ],
        ),
        notes=(
            "SCRIPT: This fragility is not new. Nineteen seventy-one, "
            "Humphreys: change nothing but the base-pressure closure and the "
            "optimum moves by a factor two point four five, while the value "
            "moves a quarter of a percent. Flat value, mobile argmax - "
            "exactly the regime you just saw in the modern plots. The same "
            "closure - Veen's equation nine IS Humphreys' five-one - is still "
            "in today's papers, and the AGARD-class working group that "
            "re-evaluated it called it unreliable. And the RDE case is not "
            "hypothetical: the only hot-fire base-pressure data in the field "
            "- Harroun, Purdue - sit at zero-point-five-nine atmospheres "
            "where the steady-equivalent computation at the same mass flow "
            "says zero-point-nine-five: roughly an eightfold increase in "
            "base drag, with five hot fires following the detonation-wave "
            "curve. The mechanism is the RDE's own ejector action: the wave "
            "replenishes faster than the base region can adjust. So the "
            "closure is fragile AND the RDE sits far from where the "
            "inherited steady closure was calibrated - which is exactly why "
            "we refuse to let an uncertified closure pick the argmax.\n"
            "[FIG ADD - user order 2026-08-23] Harroun Fig.13 on-slide: "
            "base pressure vs radius, constant-pressure CFD (solid) vs "
            "detonation-wave CFD (dashed) + 5 hot-fire tests following the "
            "RDE curve - the visual for the 0.59-vs-0.95 bullet (crop "
            "harroun_fig13_base.png, journal p.667, CT-6 full citation on "
            "slide).\n"
            "[PROVENANCE - guard 15] x2.45/+0.26% -> CH5-feed-8 ([REP] "
            "primary source, pages verified 1586-87; WG10-FAILED verdict on "
            "the Veen-fit closure, choice_ledger:830 evidence note). Contract "
            "unimodality -> CH8-feed-7 (target M3 mechanism; CT-6 on their "
            "numbers). Harroun 0.59-vs-0.95 atm / ~8x base drag / 5 hot "
            "fires on the detonation-wave curve / ejector mechanism -> "
            "BASE_PRESSURE_HARVEST_c4.md:79-92 [ADV-CFD, experimentally "
            "refereed; atlas H21-F12/F13], Harroun-Heister-Ruf JPP 37(5) "
            "pp.666-667 page-verified. CAVEAT (binding, BPH:100-105): the "
            "departure is CONFIGURATION-DEPENDENT - Schwer et al. (AIAA "
            "2018-4968) found NO substantial steady-vs-RDE base difference "
            "on a truncated airbreathing aerospike; Harroun attributes the "
            "disparity to feed pressure, wave strength, plug area ('an area "
            "demanding more focused study'). The datum is NOZZLELESS "
            "rocket-condition: it does not transfer to truncated plugs even "
            "directionally without the analogy label (R8: no hot-fire base "
            "measurement on truncated plug exists - our procurement ask). "
            "If asked 'so RDE base pressure is always lower': answer with "
            "the Schwer counter-finding, never overclaim.\n"
            "[AUTHORING ENRICHMENT - declared] This Harroun link was added "
            "at authoring (S3 window, user catch 2026-08-23): the storyboard "
            "C5 join (CH5-feed-8 + CH8-feed-7) did not carry it; anchored "
            "to the committed harvest (b3da86d), consumed here because C5's "
            "argument (closure moves argmax) is load-bearing exactly where "
            "the RDE-vs-steady base departure is measured.\n"
            "[F-19] Third bullet moved to speech: 'this is why our design "
            "contract demands unimodality of the working variable, not "
            "flatness' - the flatness-to-fragility link is spoken, not "
            "printed.\n"
            "[GLOSS - FD-3] 'truncated plug' = plug nozzle with the spike cut "
            "at a declared fraction of full length (the programme's "
            "configuration, default cut 0.20); 'working variable' = the "
            "scalar design variable swept in that family (the truncation/"
            "area parameter the contract monitors) - gloss at first use, "
            "design space proper arrives in C8-bis.\n"
            "[GUARD 18] closure names (Veen Eq.9/Humphreys 5.1, WG10) spoken, "
            "kept off slide."
        ),
    ),
    # ------------------------------------------------------------------ C6
    dict(
        id="C6", kind="new", layout="timeline_rao", minutes=1.5, cut="no",
        title="Seventy years of variational design — extended to the periodic system",
        content=dict(
            timeline=[
                ("1958", "Rao", "the control surface EMERGES as a result of the variational problem"),
                ("1967", "Hoffman", "multiplier FIELDS along characteristics — the adjoint ante litteram"),
                ("1970", "Kraiko–Osipov", "the time-weighted wall — the ancestor we always cite: no cycle measure, no quotient, no certificates"),
                ("1981", "Allman–Hoffman", "the direct route"),
                ("1994–2002", "Kraiko–Tillyaeva school", "field adjoint & shape gradient; non-uniform, vortical inflow"),
                ("now", "this programme", "the same line, extended to the periodic system"),
            ],
            eq_fig=("figs_paper/rao_eq14_transversality.png",
                    "The transversality condition — Rao, Jet Propulsion 28(6), Eq. 14, p. 379 (1958)"),
            footline="A 1975 Russian precedent is still in procurement — not yet read against the original.",
        ),
        notes=(
            "SCRIPT: We are not inventing a genre; we inherit one. Rao "
            "fifty-eight - the optimal contour where the control surface "
            "itself is an output. Hoffman sixty-seven - multiplier fields "
            "along the characteristics: the adjoint before the name existed; "
            "you will meet those fields again inside our machine. "
            "Allman-Hoffman for the direct route; the Kraiko-Tillyaeva school "
            "for the field adjoint with non-uniform vortical inflow. And the "
            "ancestor we always cite: Kraiko-Osipov nineteen-seventy, a wall "
            "weighted in time - missing the cycle measure, the quotient and "
            "the certificates. We extend this line to the periodic system. "
            "One Russian 1975 paper is still in procurement: we say so and do "
            "not summarize what we have not read.\n"
            "[PROVENANCE - guard 15] K-O 1970 mandatory citation -> "
            "CH2-feed-6 (LL-1, ADJUDICATED); classical school -> CH5-feed-6 "
            "(LL-7/14/27); Tillyaeva 1975 -> CH7-feed-6 PENDING-PROCUREMENT "
            "(honest form on slide). Lineage claims ONLY from LINEAGE_LEDGER "
            "(guard 10; lint 7). 'No family-averaged classical contouring "
            "found' = query-bounded (guard 9) - wording lives here.\n"
            "[GUARD 18] LL-ids and 'query-bounded' in notes only."
        ),
    ),
    # ------------------------------------------------------------------ C7
    dict(
        id="C7", kind="new", layout="quote_twolevel", minutes=1.5, cut="MAI",
        title="The field's own conclusion: 'approximately applicable' — with no error bar",
        content=dict(
            quote=("“the maximum thrust theory… proposed by Veen et al. is approximately "
                   "applicable to the RDE nozzle…”"),
            quote_src="Li, Xu, Lv, Yu, Zhou, Aerosp. Sci. Technol. 158:109878 (2025) — conclusions",
            levels=[
                ("SIZING", "error ~1% — supported at this level", "known"),
                ("RANKING between geometries", "fractions of a point — the question is OPEN, and nobody today can answer it", "open"),
            ],
            thesis="Our thesis: 'approximately' is an adverb to be quantified.",
        ),
        notes=(
            "SIGNPOST: agenda point 3 - our formulation.\n"
            "SCRIPT: After that chain, read the field's own conclusion - "
            "verbatim: approximately applicable. No error bar accompanies the "
            "adverb, and in the whole literature the validity regime of the "
            "average used for design is never priced. Our thesis in one line: "
            "approximately is an adverb to be quantified. Two levels: at "
            "sizing, the error is about one percent - supported. At ranking "
            "between geometries - fractions of a point, where design "
            "decisions live - the question is open, and nobody today can "
            "answer it. This talk is about building the instrument that can.\n"
            "[PROVENANCE - guard 15] Verbatim quote -> P-C p.11/16 concl.(3) "
            "(page-verified [IO]); 'regime never priced' -> CH1-feed-7 "
            "(NOT-FOUND(q), search-proven; K-O footnote unpriced) + carrier "
            ":178-180. Level-1 sizing ~1% -> [REP] (Paxson-Miki 6.54 vs ~6.5, "
            "CH3 forchetta row (v)); Level-2 ranking threshold -> OPEN R26 of "
            "record. Convergence: S-FOUNDATIONS lit campaign + refuter pass.\n"
            "[GUARD 18] 'NOT-FOUND(q)', 'R26' in notes only."
        ),
    ),
    # --------------------------------------------------------- C7-bis-pre
    dict(
        id="C7-bis-pre", kind="new", layout="cards4_timeline", minutes=1.5, cut="no",
        title="The per-phase idea has ancestors — and we declare them",
        content=dict(
            cards=[
                ("Stechmann et al. 2019",
                 "0-D blowdown per phase, declared mass-weighted mean — on fixed nozzle families"),
                ("Harroun et al. 2021",
                 "2D-axi at cycle pressure ratios, then averaged thrust coefficients — but the mean of a ratio does not commute, and the weight is undeclared"),
                ("Fievisohn & Yu 2017",
                 "wave-frame method of characteristics — the closest cousin: never design, never a family"),
                ("This programme",
                 "the variational optimum on the family — never posed before"),
            ],
            eq="eqs/eq_ratio_mean.png",  # <F/p> != <F>/<p>
        ),
        notes=(
            "SCRIPT: Before the heart of the method, the ancestry - declared "
            "by us before you ask, and both ancestors come from this very "
            "group's collaborators at Purdue. Stechmann: evaluate each phase "
            "with a zero-D blowdown, then a declared mass-weighted mean - but "
            "nozzle families are fixed. Harroun: two-D axisymmetric at the "
            "cycle's pressure ratios, then average the thrust coefficients - "
            "except the mean of a ratio does not commute, on ten-to-one "
            "cycles the bias is first order in the variance, and the paper "
            "does not declare its weight - a question we pose formally, with "
            "the source verification assigned. Fievisohn - whose boundary "
            "condition you saw in our code section - is the closest cousin: "
            "wave-frame characteristics, but never design, never a family. "
            "The quotient exists in the field; the edifice does not. We pose "
            "the variational optimum ON the family - and our simplest rung is "
            "exactly Stechmann's REDUCTION level, with the right mean proven.\n"
            "[PROVENANCE - guard 15] -> checkpoint C-1 (:131-145); lineage "
            "LL-2/LL-3/LL-13 (guard 10, ledger ADJUDICATED); CH7-feed-7 "
            "(Fievisohn); Harroun weight/denominator UNDECLARED -> W-B.0 "
            "matrix (source pp.670-671, verification assigned). WA_A3 "
            "borderline fix incorporated: 'Stechmann's REDUCTION level', "
            "never 'rung-1 = a 1-DOF optimal nozzle' (guard 3). T1c (which "
            "mean, proven) stays in notes: pattern-level, guard 2.\n"
            "[GUARD 18] LL-ids here; on-slide language engineering-only. "
            "Q&A: THE pre-cooked answer to the Purdue/Heister front "
            "(REFUTE_LINEAGE :549)."
        ),
    ),
    # -------------------------------------------------------------- C7-bis
    dict(
        id="C7-bis", kind="new", layout="two_problems", minutes=2.0, cut="MAI",
        title="Two different optimization problems",
        content=dict(
            left=dict(
                head="The field: average FIRST",
                chain=["the cycle", "collapse to ONE mean field", "apply steady optimality (Rao / Veen)",
                       "the optimum of a SUBSTITUTE problem"],
                foot="the error on the argmax has no bar",
            ),
            right=dict(
                head="Us: formulate the PERIODIC optimum",
                chain=["the cycle", "per-phase family (phases stay separate)", "cycle-averaged thrust functional",
                       "ITS optimality conditions: averaged transversality & corner"],
                foot="conditions never written before",
            ),
            eqs=["eqs/eq_javg.png", "eqs/eq_avg_wall.png"],
            theorem_band_runs=("The deciding theorem: no single phase satisfies its own wall condition — ",
                               "the weighted mean does",
                               ". The cycle-optimal nozzle is optimal at no single operating point."),
        ),
        notes=(
            "SPEECH DUTY (F-10): stop and read the theorem band verbatim; "
            "then give the room its take-away: 'the cycle-optimal nozzle "
            "is optimal at no single operating point'.\n"
            "SPEECH DUTY (F-10): stop and read the theorem band verbatim; "
            "then give the room its take-away: 'the cycle-optimal nozzle "
            "is optimal at no single operating point'.\n"
            "SCRIPT: The heart slide. Left, the field's route - including the "
            "best of those four papers: collapse the cycle into one mean "
            "field, then apply to it the steady optimality conditions of the "
            "fifties. You solve the optimum of a SUBSTITUTE. Right, ours: "
            "keep the phases separate as a family sharing one wall, define "
            "the cycle-averaged thrust functional, and derive ITS optimality "
            "conditions - transversality and corner conditions, averaged. To "
            "our census, never written. And the theorem that decides it: no "
            "single phase satisfies its own wall condition - the weighted "
            "mean does. The cycle-optimal nozzle is nobody's single-point "
            "optimal nozzle.\n"
            "[PROVENANCE - guard 15] Ladder I4 vs I2/I3 -> CH1-feed-1; "
            "'(**') weighted-mean wall condition necessary; no phase "
            "satisfies its own' -> CH2-feed-1 (THEOREM* T-T7FS(b)); boxed "
            "warning (substitute problem) -> CH1-feed-4; 'three ways to "
            "average, one survives; collapse class' -> CH2-feed-2 (THEOREM* "
            "[T-T3], degenerate case = pressure-scaling similarity class). "
            "'Never written' -> litmap C2 NOT-FOUND(q) 'averaged Rao-type "
            "wall/corner conditions - zero hits' (query-bounded, guard 9).\n"
            "[GUARD 18] class sigle (THEOREM*, ids) and 'zero hits' in notes "
            "only; on-slide says 'proven / never written before' in plain "
            "engineering register."
        ),
    ),
    # -------------------------------------------------------------- C7-ter
    dict(
        id="C7-ter", kind="new", layout="three_panel_bifurcation", minutes=1.5, cut="no",
        title="Where the difference is a theorem — and where it is an open, measured question",
        content=dict(
            panels=[
                ("area ratio only — no contouring",
                 "the two problems coincide — proven",
                 "even here the wrong mean moves the optimum area ratio by +44–87% (3–10 s of Isp) — measured on our numerical test bench",
                 False),
                ("full adapted plug",
                 "still coincide — proven, perimeter declared",
                 "the peak-phase design is optimal",
                 False),
                ("TRUNCATED plug — our configuration",
                 "the coincidence breaks — proven",
                 "the first genuinely averaged shape problem opens",
                 True),
            ],
            honesty_band=("Its size at contouring is open — not presumed small (10:1 inlet, ~6:1 throat, "
                          "~20:1 combustor swings). The machine is ready: it is the first campaign."),
        ),
        notes=(
            "SCRIPT: Honesty about where this is a theorem. Rung one: no "
            "contouring, only the area ratio - not a Rao nozzle - there the "
            "two problems coincide by construction; and even there, using the "
            "wrong mean moves the optimum area ratio by up to eighty-seven "
            "percent and costs up to ten seconds of Isp, measured on our "
            "numerical test bench with rejecting checks. Same pattern as "
            "Humphreys: mobile argmax at flat value - a pattern, not the "
            "proof of the general case. Full adapted plug: still coincide - "
            "peak-phase design is optimal, perimeter declared. Truncated "
            "plug - OUR configuration: the coincidence breaks, proven, and "
            "the first genuinely averaged shape problem opens. Its size at "
            "contouring is open, the record does not call it small, and no "
            "expectation of smallness is anywhere in our records. The "
            "machine is ready; that comparison is the first campaign of the "
            "phase opening now.\n"
            "[PROVENANCE - guard 15] Coincidence/breaks map -> CH1-feed-3 "
            "(THEOREM [T-T7RED] rung; THEOREM* [T-T4] nesting + break; "
            "sharpness clause declared); primacy claims in locked form D-06 "
            "-> CH1-feed-10 (notes+Q&A only). Bench inset -> CH2-feed-3 "
            "(PRACTICE with rejector; dIsp +3.33..+9.71 s on 6 cases, "
            "carrier suite, measured 2026-08-22; stage: verified). "
            "Cycle-wall 2-D -> CH2-feed-8 (OPEN, owner F2). Strictness "
            "clause -> CH6-feed-8 (carrier PB-2 OPEN). Excursions 10:1/6:1/"
            "20:1 -> CH5-feed-9 (CT-6, their BCs/data). Panel quote -> "
            "swirl5f panel of record ('single-digit % plausible on-ray, "
            ">10% not excluded off-ray; could be large - not refutable by "
            "theory today').\n"
            "[GATE DECISION WIRED] Twin PB-2 = (b) honest form (user "
            "decision of record, S2 gate): NO pre-milestone number; the "
            "slide carries 'machine ready, first campaign of the phase "
            "opening now' - the bifurcation declared at the S2 gate is "
            "RESOLVED here; C17's twin card carries the same form.\n"
            "[GUARDS] 2/3 wired in the panel-1 wording (pattern-only, "
            "never '1-DOF nozzle case'); FD-5(i) wired ('numerical test "
            "bench'). Guard 18: 'PB-2', class sigle here only."
        ),
    ),
    # ------------------------------------------------------------------ C8
    dict(
        id="C8", kind="new", layout="fig_bullets_tag", minutes=1.5, cut="no",
        title="Per-phase is not an approximation — it is a change of coordinates",
        content=dict(
            fig=("figs/fig_c8_quotient.png",
                 None),  # home diagram: annulus -> rotating frame -> family vs global collapse
            bullets=[
                "In the declared class (pure rotating wave) the flow is steady in the wave frame: the family is an exact change of coordinates, with one declared approximation.",
                "The global time average mixes the phases — the cruder reduction, not ours.",
            ],
            tag=("Proof structure declared; complete proof in progress — stated openly."),
        ),
        notes=(
            "SCRIPT: Why is the family the right object and not an "
            "approximation? Remember the primer: in the frame rotating with "
            "the wave, this flow is steady. Within the declared data class - "
            "pure periodic rotating wave, monitored on the flatness of "
            "stagnation temperature - passing to the per-phase family is a "
            "change of coordinates, a quotient: exact, with one declared "
            "Strouhal-order approximation whose hypotheses are printed. The "
            "field's global time average MIXES phases - that is the crudest "
            "reduction, not ours. And the honest tag, on the slide by "
            "explicit order: this step has a declared proof structure - the "
            "equivariance route - not yet the complete proof.\n"
            "[PROVENANCE - guard 15] Quotient + O(St) -> CH1-feed-2 (SCHEMA "
            "with route S1 named + [T-T0P-E] THEOREM leg); three-floor "
            "organizer -> CH7-feed-1 (what enters the state / what is lost "
            "/ what climbing costs). On-slide tag = user decision :1450 "
            "(checkpoint :95-97, guard 12): two-stage claim at DECLARED "
            "SCHEMA class, proof route named, spoken form - the tag is the "
            "slide's honesty device, verbatim-stable.\n"
            "[GUARD 18] 'SCHEMA', 'S1', ':1450' in notes; slide says it in "
            "words."
        ),
    ),
    # -------------------------------------------------------------- C8-bis
    dict(
        id="C8-bis", kind="new", layout="envelope_sectors", minutes=1.5, cut="no",
        title="The design space: configurations are outputs, not inputs",
        content=dict(
            fig=("figs/fig_c8bis_envelope.png", None),  # envelope + 4 sector cards w/ status
            bullets=[
                "The design variable is a solid body inside an envelope: bell, plug, shrouded plug, expansion–deflection are not presupposed — they emerge as classes of the result.",
                "Sectors are finitely many: the global optimum is a tournament among sector optima — every delivered optimum declares its guarantee and its strength.",
                "First verdict on record: at certified closures the plug weakly dominates the bell, tie region characterized — closures at equal area ratio, never hardware.",
                "Route: certified splines per sector, no level-sets — an infinitesimal body in supersonic flow pays only wave drag: sectors are compared whole.",
            ],
            state_line="Honest state: the driver exercises one sector today (bell, 9 DOF); the others have named owners and windows.",
        ),
        notes=(
            "SCRIPT: What do we actually optimize over? A solid body inside "
            "an envelope. Bell, plug, shrouded plug, expansion-deflection are "
            "not menu choices - they are topological classes of the RESULT. "
            "The admissible classes are finitely many, so the global optimum "
            "is the winner of a finite tournament among sector optima - and "
            "whenever we say 'optimum' we attach which mechanism guarantees "
            "it and how strong it is. One tournament verdict already exists "
            "at the reduced rung: the plug weakly dominates the bell "
            "pointwise under certified closures, with the tie region "
            "characterized - mind: a ranking between closures at equal area "
            "ratio, never between hardware. On parameterization we chose "
            "certified splines per sector and refused topological "
            "derivatives: an infinitesimal body in supersonic flow pays only "
            "wave drag, so you compare whole sectors. Honest state: the "
            "discrete driver exercises one sector today - bell, nine "
            "degrees of freedom; plug truncated and shrouded are the named "
            "campaigns.\n"
            "[PROVENANCE - guard 15] Configuration-free formulation -> "
            "CH8-feed-1 (flagship feed; problem book §5; uniform-cone pin, "
            "user 2026-08-02: cono/Chenais, Λ=cerchi); finite sectors + "
            "tournament -> CH8-feed-2 (THEOREM leg, carriers X-GRP10/12) + "
            "CH8-feed-3 (THEOREM* existence per sector); mechanism contract "
            "-> CH8-feed-4 (M1-M5: sigla here, concept on slide; guard 8); "
            "driver one-sector state -> CH8-feed-8; spline route + no-TD "
            "caution + classical datum -> CH8-feed-9 (LL-29).\n"
            "[F-14] Qualifier prose moved OFF-slide (spoken): the tournament "
            "verdict is a ranking between CLOSURES at equal area ratio, "
            "never between hardware; every delivered optimum declares its "
            "guarantee mechanism and strength; the no-level-set reason: an "
            "infinitesimal body in supersonic flow pays only wave drag, so "
            "whole sectors are compared.\n"
            "[GUARD 18] M1-M5/X-GRP ids in notes."
        ),
    ),
    # ------------------------------------------------------------------ C9
    dict(
        id="C9", kind="new", layout="fig_bullets", minutes=1.5, cut="no",
        title="Same pressure trace, different thrust",
        content=dict(
            fig=("figs/fig_c9_fiber.png",
                 None),  # home fiber schema: P-trace fixed, family of compatible states
            bullets=[
                "Same pressure trace, different swirl content → different thrust — no CFD needed: a pressure-only description cannot rank designs.",
                "The full-state per-phase mean passes on this axis. Stakes: 1.5–3% of thrust.",
                "The field imposes only pressure at the boundary — our full-state contract is the repair.",
            ],
        ),
        notes=(
            "SCRIPT: Can any pressure-only average be enough? No - and we "
            "can show it without a single CFD run. Fix the pressure trace at "
            "the interface: a whole family of physically distinct states "
            "remains - different swirl, different fluctuation content - and "
            "they produce different thrust. So pressure-only reduction is "
            "condemned; the full-state per-phase mean is exonerated on that "
            "axis. Stakes: one-and-a-half to three percent of thrust, "
            "contributions up to nine percent of pressure. And the contract "
            "consequence: the field's practice of imposing only pressure at "
            "the boundary throws thrust information away - our full-state "
            "data contract is exactly the repair.\n"
            "[PROVENANCE - guard 15] Fiber non-degeneracy + separation -> "
            "CH3-feed-3, REPAIRED FORM of record (REFUTE_CH10 F1, classes "
            "PER LEG): T-DISC-1 THEOREM* (fibers non-degenerate); T-DISC-2 "
            "split-grade SCOPED (in-fiber separation, booking-level, "
            "physical-h0-fixed); T-DISC-3(b) SCHEMA with premise (DR) - "
            "never bare 'THEOREM'; the slide says it in words ('declared "
            "proof structure with its explicit premise'). Exoneration -> "
            "CH10-feed-5 (T-DISC-4(b) SCHEMA). Stakes 1.5-3% / up to 9% -> "
            "[SE] scaling estimates (M0:1140-1151; swirl5f B1/B2). Weights "
            "-> CH7-feed-2 ([SE]). Lineage LL-6/LL-24.\n"
            "[GUARD 18] class names per leg live here; on-slide phrasing "
            "carries the distinction in engineering words."
        ),
    ),
    # ------------------------------------------------------------------ C10
    dict(
        id="C10", kind="new", layout="operator_fig", minutes=1.5, cut="no",
        title="What the reduction drops is explicit — and measurable",
        content=dict(
            fig=("figs_paper/pc_fig21_lateral.png",
                 "Rotating lateral force, averaging to zero — Li, Xu et al., AST 158:109878 (2025), Fig. 21"),
            schema=("figs/fig_c10_operator.png", None),  # operator + channels schema
            bullets=[
                "The discarded terms form an explicit operator; its mean channel is exactly zero — proven.",
                "Two first-order channels survive: front jumps (no number yet — our declared weak point) and covariance.",
                "Both are measurable — the campaign starting now measures them.",
                "Published face: lateral force 25–35% of axial, rotating, averaging to zero.",
            ],
        ),
        notes=(
            "SCRIPT: What exactly does the reduction throw away? Not a vague "
            "'unsteadiness': an explicit operator - six advective lines plus "
            "front atoms - with identities verified by computer algebra. Its "
            "mean channel is exactly zero: proven. What survives at first "
            "order is exactly two channels: the jumps at the fronts - our "
            "declared heel, no number yet - and the covariance. So the "
            "residual is measurable, and measuring it is the first campaign "
            "of the phase opening now. The published face of the zero-mean "
            "theorem: the lateral force is a quarter to a third of axial "
            "instantaneously, rotates at wave frequency, and averages to "
            "zero.\n"
            "[PROVENANCE - guard 15] Operator K explicit -> CH3-feed-1 "
            "(DEFINITION + THEOREM* identities, sympy witnesses); K-bar=0 + "
            "two channels (J)/(H) -> CH3-feed-2 (THEOREM* minted at record "
            "grade BV; SBV-conditional clause H-RED-2 declared); heel "
            "always co-stated -> CH7-feed-3 (guards 1/16: hierarchy never "
            "without the (J) heel; suppression-claim perimeter rule). "
            "Fig.21 -> CH5-feed-3 ([FIG]+[INFER], CT-6). M-RED consumption "
            "-> C17.\n"
            "[GUARD 18] channel letters (J)/(H) and class names here; slide "
            "says 'jumps at the fronts' and 'covariance' in words."
        ),
    ),
    # ------------------------------------------------------------------ C11
    dict(
        id="C11", kind="new", layout="honesty_table", minutes=2.0, cut="no",
        title="The residual error, channel by channel",
        content=dict(
            table_header=["channel", "best case", "worst case", "evidence"],
            table=[
                ("Mean azimuthal residual", "exactly 0", "exactly 0", "theorem (declared perimeter)"),
                ("Swirl booking debt", "1.5% of thrust", "3% of thrust", "order estimate"),
                ("Data-fidelity biases", "0.6% of pressure", "9% of pressure", "order estimate + literature"),
                ("Jumps at the fronts (the heel)", "no number yet — derivation road named", "—", "declared open"),
                ("Sizing level", "~1%", "~1%", "literature, page-verified"),
                ("Optimum shift", "no number at any grade — the first campaign measures it", "—", "declared open"),
            ],
            bullets=[
                "Channels do not sum. Best case: single-digit %; off-axis, >10% not excluded.",
                "Largest adverse marker, published: +13 points of ideal from a shroud at fixed area ratio — unexplained (Paxson & Miki 2022).",
                "Our one in-class number: +0.51% ± ~30% — Rao's classical scale: 0.04–0.34%.",
                "No external referee exists: we close the bracket, or it stays open.",
            ],
        ),
        notes=(
            "SCRIPT: Our honesty table - the highlights; the full table is "
            "in backup. Channel by channel, best and worst, each cell with "
            "its evidence level: theorem, our measurement, order estimate, "
            "or literature datum. Read the two 'no number yet' rows first: "
            "the front jumps and the optimum shift - we say it, and the "
            "road to a number is named and ordered. Best case, off-axis "
            "excluded, single-digit percent is plausible; off-axis, more "
            "than ten percent is not excluded. Our one in-class number, "
            "half a percent, carries a thirty-percent uncertainty - "
            "against Rao's classical hundredths-to-thirds of a percent, "
            "their numbers. And no external referee exists for this error: "
            "either we close the bracket, or it stays open.\n"
            "[PROVENANCE - guard 15] Table cells -> CH3-feed-4 (classes "
            "per cell, forchetta §; CH7 PART 5 headline :1731-1743): mean "
            "channel THEOREM* (K-bar=0, perimeter H-RED-2); booking debt "
            "1.5-3% [SE]; B1 0.6-9% p [SE]+lit; heel delta/L_H UNDERIVED "
            "-> CH3-feed-5 (SCHEMA + derivers named: five-field -> "
            "route-B -> M-RED -> R22-CFD); sizing ~1% [REP]; optimum-"
            "shift no number (:1506). +0.51%±~30% -> CH1-feed-9 (band-"
            "underinclusion declared); Rao 0.04-0.34% their numbers "
            "(CT-6). No-referee -> CH5-feed-10 + CT-3 STRICT form: no "
            "published referee THAT DISCRIMINATES the per-phase-averaged "
            "prediction against 3D-unsteady truth (restrictive clause is "
            "part of the sentence - binding for Q&A). Conditional spine "
            "C-D25U -> CH2-feed-7 (here only). Guard 6 / D-44: bracket, "
            "NEVER adequacy - the slide shows a bracket and never claims "
            "the average adequate for contour ranking.\n"
            "[GUARD 18] class sigle/registry ids here; evidence column on "
            "slide uses plain words."
        ),
    ),
    # ------------------------------------------------------------------ C12
    dict(
        id="C12", kind="new", layout="fig_bullets", minutes=0, cut="pos7", to_backup=True,
        title="The largest adverse signal is published: a shroud worth 13 points",
        content=dict(
            fig=("figs_paper/pm_shroud_5871.png",
                 "Shroud effect at fixed area ratio — Paxson & Miki, AIAA (2022)"),
            bullets=[
                "A shroud lifts a plug from 58.1% to ~71.5% of ideal at fixed area ratio — unexplained by the authors.",
                "On record as a candidate swirl-interaction effect.",
            ],
        ),
        notes=(
            "SCRIPT: The largest signal in the worst direction is published: "
            "Paxson and Miki add a shroud at fixed area ratio and the plug "
            "jumps thirteen points of ideal - more than their whole "
            "area-ratio line buys - and the authors do not explain it. We "
            "register it as a candidate swirl-breaker: if swirl content is "
            "doing that, it is exactly the off-axis channel our bracket "
            "flags.\n"
            "[PROVENANCE - guard 15] 58.1->71.5 at fixed AR, unexplained -> "
            "[REP] page-verified (findings_registry:2026; M0:1345, "
            "1350-1353); shroud prediction pre-registered F2a; S-5F decision "
            "at F2-entry (user, of record). LL-5 note for Q&A: Paxson-Miki's "
            "metric IS our cycle-time-averaged thrust - published as a "
            "metric, never posed as a design functional (affilata form).\n"
            "[GUARD 18] registry ids here."
        ),
    ),
]
