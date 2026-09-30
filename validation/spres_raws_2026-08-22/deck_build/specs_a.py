# -*- coding: utf-8 -*-
"""S-PRES deck — Part A (opening + group, Heister improved) + Part B (bridge).

Content-of-record source: STORYBOARD_v3.md v3.1 (user-approved, gate S2)
+ STORYBOARD.md v1 Part A rows + Heister form fixes 1-9 + style pact (b)
E1-E7. Guard 18: on-slide text = engineering language, zero internal
accounting; accounting and provenance live in the 'notes' field
(speaker notes channel, guard 15). Deck language: English.

Spec contract (consumed by build_deck_spres.py):
  id      slide id of the storyboard join table
  kind    'edit' (existing Heister slide, form-only ops) | 'new'
  src     1-based slide index in ppt_Heister.pptx (kind='edit')
  title   None = keep existing title (edits); str = assertion title (new)
  kicker  optional teal sub-heading
  layout  builder function name for kind='new'
  content layout-specific payload (all on-slide text lives here)
  edits   list of declared form ops for kind='edit'
  minutes storyboard time budget
  cut     cut-list position ('MAI', 'no', or int)
  notes   speaker notes: script + [PROVENANCE] rows (guard 15) +
          off-slide accounting (guard 18)
"""

SLIDES_A = [
    # ------------------------------------------------------------------ A1
    dict(
        id="A1", kind="edit", src=1, title=None, minutes=1.0, cut="no",
        edits=["title_slide_frontmatter"],  # version/date/venue line (audit criterion (n))
        notes=(
            "SCRIPT: Good morning. This is the rotating-detonation work of the "
            "T(H)RUST group at Sapienza - Montanari, Grossi, Falco, Nasuti. "
            "Today: the group's full-engine RDE activity, and then, in depth, "
            "the nozzle design programme and what we are asking of you.\n"
            "[PROVENANCE] Host-group title slide (Heister deck S1); form-only "
            "edits: frontmatter line with version/date/venue (audit criterion "
            "(n)); master defaults cleaned (fix 3)."
        ),
    ),
    # ------------------------------------------------------------------ A2
    dict(
        id="A2", kind="new", layout="bluf", minutes=0, cut="S4v2", to_backup=True,
        title="Today",
        content=dict(
            agenda=[
                "The group and its tools",
                "The real RDE exhaust",
                "Our formulation",
                "The design machine",
                "Honesty, roadmap & requests",
            ],
            closing="Three requests for the panel — at the end.",
        ),
        notes=(
            "SCRIPT: The plan for the hour: the group and its tools; then one "
            "research line in depth - what the RDE exhaust really is, how we "
            "formulate its design problem, the machine we built for it, and "
            "an honest account of limits; we close with three concrete "
            "requests.\n"
            "[CKP-S3-2 wired] A2 = agenda only: no per-section minutes, no "
            "group-intro repetition (A3 does that better), no nozzle emphasis "
            "in the intro (user order at the Block-1 loop, 2026-08-23; "
            "supersedes the v3.1 mini-map-with-minutes form - declared "
            "deviation, BUILD_LOG).\n"
            "[PROVENANCE] Ask preview -> MESSAGE_ARCHITECTURE §BLUF (asks "
            "return decision-ready in C18)."
        ),
    ),
    # ------------------------------------------------------------------ A3
    dict(
        id="A3", kind="edit", src=2, title=None, minutes=1.0, cut="no",
        edits=["fix_bellenoue", "open_lines_pointer"],
        notes=(
            "SCRIPT: Five research roads, one framework underneath. Everything "
            "you will hear today is numerical, oriented to industrially relevant "
            "questions, and run with an international network - NC State, RMIT, "
            "ISAE-ENSMA. The 'nozzle design' line in the open-research card is "
            "the one we expand today in a dedicated section.\n"
            "[PROVENANCE] Host-group slide (Heister S2), content invariant; "
            "form fixes: 'Belleonue'->'Bellenoue' (fix 6), open-lines card "
            "carries pointer to the nozzle section (fix 9)."
        ),
    ),
    # ------------------------------------------------------------------ A4
    dict(
        id="A4", kind="new", layout="two_fig_primer", minutes=2.0, cut="pos3",
        title="Detonation compresses by itself: pressure-gain combustion",
        content=dict(
            left_fig=("figs/fig_cycles_pv.png",
                      "p–v plane: Brayton vs Humphrey vs detonation (FJ) cycles — group figure"),
            right_fig=("figs/fig_ucj_bar.png",
                       "CJ speeds across fuels — group figure"),
            bullets=[
                "Near-constant-volume burn: pressure rises without a compressor.",
                "Higher ideal efficiency at the same pre-compression.",
            ],
        ),
        notes=(
            "SCRIPT: For anyone new to detonation engines: a deflagration burns "
            "at roughly constant pressure - you pay a compressor for every bar. "
            "A detonation burns so fast the volume cannot follow: the burn "
            "itself compresses. On the p-v plane the detonation cycle encloses "
            "more work at the same pre-compression. That thermodynamic premium "
            "- pressure-gain combustion - is what the whole field is chasing.\n"
            "[PROVENANCE] Primer class: standard literature material already "
            "validated in the group's CVA lecture deck (figures of the house "
            "pipeline: fig_cycles_pv, fig_ucj_bar; every number in them traced "
            "to committed scripts in that pipeline). Zero new claims (v1 A6 "
            "NOTA CLASSE).\n"
            "[GUARD 18] cycle-efficiency numbers live in the figure annotations "
            "(physical numbers), none of our programme accounting here."
        ),
    ),
    # ------------------------------------------------------------------ A5
    dict(
        id="A5", kind="new", layout="two_fig_primer", minutes=2.0, cut="pos3",
        title="The RDE: a detonation made steady in a rotating frame",
        content=dict(
            left_fig=("figs/fig_rde_schematic.png",
                      "Annular RDE: rotating front, continuous refill — group figure"),
            right_fig=("figs_paper/sk_orig_fig01_rde_annulus.png",
                       "Unwrapped RDE flowfield — Shepherd & Kasahara, GALCIT FM2017.001 (2017)"),
            bullets=[
                "A front rotates at near-CJ speed (kHz); continuous refill behind it.",
                "Axial, continuous exhaust — no valves.",
            ],
        ),
        notes=(
            "SCRIPT: The RDE traps that premium in a ring. The front rotates at "
            "nearly the Chapman-Jouguet speed - several kilohertz around a "
            "typical annulus - while injection refills continuously behind it. "
            "In the frame rotating with the wave the picture is steady. Keep "
            "that sentence: it is the seed of everything in the nozzle section.\n"
            "[PROVENANCE] Primer class, standard material validated in the CVA "
            "deck. Right figure: paper crop, full citation on slide, CT-6 "
            "(shown for discussion, not re-derived). The 'steady in the "
            "rotating frame' seed anticipates C8's exact-quotient claim - "
            "stated here only phenomenologically (fluency seeding, CKP-S2-4).\n"
        ),
    ),
    # ------------------------------------------------------------------ A7
    dict(
        id="A7", kind="edit", src=3, title=None, minutes=1.2, cut="no",
        edits=["lighten_a7"],
        notes=(
            "SCRIPT: HYPERDE in one picture: each subsystem solved at its most "
            "informative dimensionality - 3D or unwrapped quasi-2D chamber, "
            "quasi-1D injectors when the coupling is longitudinal, 3D URANS "
            "expansion - inside one consistent formulation.\n"
            "[PROVENANCE] Host slide (Heister S3); form-only: card text "
            "lightened toward the ≤60-word budget, no content removed."
        ),
    ),
    # ------------------------------------------------------------------ A8
    dict(
        id="A8", kind="edit", src=4, title=None, minutes=1.0, cut="no",
        edits=["lighten_a8"],
        notes=(
            "SCRIPT: The solver suite under it: finite volume, second order in "
            "space, up to third in time; tabulated thermally-perfect thermo; "
            "turbulence models swappable; OpenMP plus MPI; interfaces to the "
            "in-house solid, multiphase and real-fluid solvers.\n"
            "[PROVENANCE] Host slide (Heister S4), content invariant, text "
            "tightened (v1: 'testo asciugato')."
        ),
    ),
    # ------------------------------------------------------------------ A9
    dict(
        id="A9", kind="edit", src=5, title=None, minutes=1.0, cut="no",
        edits=[],
        notes=(
            "SCRIPT: Where the quasi-2D solver goes beyond recent literature: "
            "rigorous diffusive fluxes and generic RANS closure, a general "
            "z(x,y) width law, and the non-isentropic backward-facing-step "
            "boundary condition adapted from Fievisohn & Yu's method-of-"
            "characteristics analysis.\n"
            "[PROVENANCE] Host slide (Heister S5); citation [1] Fievisohn & Yu "
            "JPP 33(1) 2017 already on slide. Note for Q&A: Fievisohn's "
            "wave-frame MoC is also the closest ancestor of our per-phase view "
            "- that thread returns in the nozzle section (C7-bis-pre)."
        ),
    ),
    # ------------------------------------------------------------------ A10
    dict(
        id="A10", kind="edit", src=6, title=None, minutes=1.0, cut="no",
        edits=[],
        notes=(
            "SCRIPT: Verification and validation, first rung: the chamber "
            "solver against 1-D ZND structure from the Shock & Detonation "
            "Toolbox - overlaid profiles.\n"
            "[PROVENANCE] Host V&V slide (Heister S6), invariant."
        ),
    ),
    # ------------------------------------------------------------------ A11
    dict(
        id="A11", kind="edit", src=7, title=None, minutes=1.0, cut="no",
        edits=[],
        notes=(
            "SCRIPT: Second rung: unwrapped literature test cases - Schwer & "
            "Kailasanath's plenum-feedback configuration - reproduced.\n"
            "[PROVENANCE] Host V&V slide (Heister S7), invariant; citation [2] "
            "on slide."
        ),
    ),
    # ------------------------------------------------------------------ A12a
    dict(
        id="A12a", kind="edit", src=8, title=None, minutes=1.0, cut="no",
        edits=[],
        notes=(
            "SCRIPT: Third rung, HYPERDE-specific features. Here the quasi-2D "
            "source terms: Mach field and stagnation-pressure traces across "
            "aspect ratios against the resolved reference.\n"
            "[PROVENANCE] Host V&V slide (Heister S8). DECLARED authoring "
            "decision (v1 A12 clause): the S8+S9 fusion was measured against "
            "the 3-metre legibility criterion and REJECTED - six dense plots "
            "on one 16:9 slide push axis labels below readable size; the two "
            "slides stay (A12a/A12b), the minute is recovered on the A14-A20 "
            "pace as budgeted in v3.1."
        ),
    ),
    # ------------------------------------------------------------------ A12b
    dict(
        id="A12b", kind="edit", src=9, title=None, minutes=1.0, cut="no",
        edits=[],
        notes=(
            "SCRIPT: And the quasi-1D injector-chamber coupling: temperature "
            "and velocity profiles, modelled versus resolved versus "
            "boundary-condition-only - the three collapse.\n"
            "[PROVENANCE] Host V&V slide (Heister S9); see A12a note for the "
            "declared fusion decision."
        ),
    ),
    # ------------------------------------------------------------------ A13
    dict(
        id="A13", kind="edit", src=10, title=None, minutes=1.3, cut="no",
        edits=[],
        notes=(
            "SCRIPT: Fourth rung: quasi-2D to full-3D connection - and the "
            "26-second video of the coupled solution. [PLAY VIDEO]\n"
            "[PROVENANCE] Host V&V slide (Heister S10), media preserved."
        ),
    ),
    # ------------------------------------------------------------------ A14
    dict(
        id="A14", kind="edit", src=11, title=None, minutes=1.0, cut="pos6",
        edits=["remove_offcanvas_a14"],
        notes=(
            "SCRIPT: The refill region, with RMIT and NC State: four questions "
            "on how geometry shapes the refill expansion - and the "
            "counter-intuitive datum that diverging inlets, introduced to cut "
            "step losses, degrade overall performance instead.\n"
            "[PROVENANCE] Host slide (Heister S11); form fix 5: the off-canvas "
            "text box ('Inlet extension added for supersonic cases') removed "
            "from the canvas - its content preserved here: the inlet extension "
            "is added for the supersonic cases of the sweep."
        ),
    ),
    # ------------------------------------------------------------------ A15
    dict(
        id="A15", kind="edit", src=12, title=None, minutes=1.0, cut="pos6",
        edits=[],  # F-7: host in-body header retained; added heading suppressed
        notes=(
            "SCRIPT: The wave-number sweep: stagnation-pressure losses grow "
            "with Λ; at Λ = 2.9 the inlet turns entirely supersonic and the "
            "pressure gain goes negative.\n"
            "[PROVENANCE] Host slide (Heister S12); form fix 4: native heading "
            "added (Λ as native text in the template font - no raster "
            "heading)."
        ),
    ),
    # ------------------------------------------------------------------ A16
    dict(
        id="A16", kind="edit", src=13, title=None, minutes=1.0, cut="pos6",
        edits=[],
        notes=(
            "SCRIPT: The group's synthesis model of the refill region: the "
            "subsonic/supersonic expansion picture in one figure.\n"
            "[PROVENANCE] Host slide (Heister S13), invariant."
        ),
    ),
    # ------------------------------------------------------------------ A17
    dict(
        id="A17", kind="edit", src=14, title=None, minutes=1.0, cut="pos6",
        edits=[],
        notes=(
            "SCRIPT: Supersonic bladeless turbines with NC State: CFD-designed "
            "Mach-4 wind tunnel, swappable nozzle and second-throat diffuser - "
            "real hardware, real photographs.\n"
            "[PROVENANCE] Host slide (Heister S14), invariant."
        ),
    ),
    # ------------------------------------------------------------------ A18
    dict(
        id="A18", kind="edit", src=15, title=None, minutes=1.0, cut="pos6",
        edits=[],
        notes=(
            "SCRIPT: Tunnel validation: isentropic prediction versus "
            "experiment versus CFD at 3 and 4 bar feed.\n"
            "[PROVENANCE] Host slide (Heister S15), invariant."
        ),
    ),
    # ------------------------------------------------------------------ A19
    dict(
        id="A19", kind="edit", src=16, title=None, minutes=1.0, cut="pos1",
        edits=[],
        notes=(
            "SCRIPT: Ongoing: bladeless-turbine shape optimization and the "
            "ejector-diffuser system for RDE testing - 14-second video. "
            "[PLAY VIDEO]\n"
            "[PROVENANCE] Host slide (Heister S16), media preserved."
        ),
    ),
    # ------------------------------------------------------------------ A20
    dict(
        id="A20", kind="edit", src=17, title=None, minutes=1.0, cut="pos6",
        edits=[],
        notes=(
            "SCRIPT: Disk RDEs with RMIT, ISAE-ENSMA and PPRIME: 3D URANS "
            "versus quasi-2D on the same disk configuration.\n"
            "[PROVENANCE] Host slide (Heister S17), invariant."
        ),
    ),
]

SLIDES_B = [
    # ------------------------------------------------------------------ B1
    dict(
        id="B1", kind="edit", src=18, title=None, minutes=2.0, cut="MAI",
        edits=["b1_kicker_band"],
        content=dict(
            kicker="Does an 'optimal' profile exist for an RDE exhaust? — the group's open question",
            chips=[
                ("+4–7% Isp", "the largest published lever (choked interface) — corpus papers, their numbers"),
                ("58.1 → 71.5% of ideal", "a shroud at fixed area ratio — Paxson & Miki 2022, unexplained by the authors"),
            ],
            chips_lead="Pressure gain earned in the chamber can be lost — or won — at the nozzle:",
            arrow_text="the next section is the group's answer",
        ),
        notes=(
            "SIGNPOST: agenda point 2 - the real RDE exhaust. SPEECH DUTY: "
            "read the open question aloud - 'Does an optimal profile exist "
            "for an RDE exhaust?' - as the question of the rest of this "
            "talk.\n"
            "SIGNPOST: agenda point 2 - the real RDE exhaust. SPEECH DUTY: "
            "read the open question aloud - 'Does an optimal profile exist "
            "for an RDE exhaust?' - as the question of the rest of this "
            "talk.\n"
            "SCRIPT: This slide closed the group deck; today it opens the main "
            "act. We have an in-house method-of-characteristics API - fully "
            "non-isentropic, three-wave, 2D and axisymmetric - with the ideal, "
            "Rao and Vander-Veen families implemented. And one open question: "
            "does an optimal profile exist for an RDE exhaust? Two published "
            "numbers say the stakes are real - four to seven percent of Isp on "
            "the choked-interface lever, and thirteen points of ideal from a "
            "shroud at fixed area ratio, unexplained by its own authors. The "
            "rest of this talk is the group's answer.\n"
            "[PROVENANCE - guard 15] '+4-7% Isp choked lever' -> CH5 CT-1 "
            "(SYN:75-94): 'the largest published performance lever lives "
            "OUTSIDE the fixed-interface design class' - their numbers, CT-6; "
            "decider CFD-1. '58.1->71.5% at fixed AR' -> Paxson-Miki [REP "
            "page-verified] (findings_registry:2026; CH3 forchetta row). The "
            "two extremes stay SEPARATE with their own anchors - the "
            "unadjudicated '4-13 points' composite is banned (WA_A3 critic "
            "row 2, DISPOSED-VERIFIED). Citations [3][4] on slide + Paxson-"
            "Miki added to the reference line.\n"
            "[GUARD 18] numbers on slide are physical/paper numbers (allowed); "
            "threat-ledger names (CT-1) live here only."
        ),
    ),
    # ------------------------------------------------- A6 (moved after B1)
    dict(
        id="A6", kind="new", layout="fig_plus_eq", minutes=2.0, cut="pos3",
        title="The RDE exhaust is periodic — the literature designs on its time-average",
        content=dict(
            fig=("figs_paper/kp_orig_eap_construction.png",
                 "Nonuniform RDE exhaust — Kaemming & Paxson, AIAA 2018-1101 (Equivalent Available Pressure)"),
            eq="eqs/eq_eap.png",
            eq_caption="the literature's accepted average: one equivalent pressure for the whole cycle",
            bullets=[
                "The real exhaust rotates at kHz: every flow quantity swings within each cycle.",
                "Every published nozzle-design route replaces it with a steady average before designing — the authors of the average themselves caution that naive averaging mis-states performance.",
            ],
        ),
        notes=(
            "SCRIPT (S4v2): Before the designs, one fact to hold. This "
            "exhaust is periodic, not steady: a detonation front rotates "
            "at kilohertz, and every quantity the nozzle sees swings "
            "within each cycle. The literature designs its nozzles by "
            "first replacing that flow with a steady time-average - "
            "every published route does. And the authors of the accepted "
            "average published the warning themselves: average the total "
            "pressure naively and you mis-state performance. Whether "
            "designing on ANY average is even the right problem - that "
            "is the question this section answers, formally. Keep it in "
            "mind for every slide that follows.\n"
            "[CKP-S3-2 wired] A6 MOVED from primer-3 to post-B1 hinge (user "
            "order at the Block-1 loop: in the primer the averaging warning "
            "had no visible link; here it is the bridge into the nozzle "
            "section - declared deviation from v3.1 slide order, BUILD_LOG).\n"
            "[PROVENANCE - guard 15] 'EAP caution by the metric's own "
            "authors' -> CH1-feed-5 + CH5-feed-7, [IO] remark of record, "
            "M0:2526-2544. 'No error bar on the mean' -> CH1-feed-7 "
            "NOT-FOUND(q) (search-proven; wording lives here). 'Our "
            "programme constructs it' -> P4 corrector (FD-1: sigla here "
            "only; owner F2). CT-6 citation on slide. 'Every design route "
            "starts from an averaged flow' -> C3/C3-bis record (declared "
            "anticipation, resolved two slides later).\n"
        ),
    ),
]
