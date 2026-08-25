# -*- coding: utf-8 -*-
"""S-PRES deck — Part C, sections C-III (the machine: why these choices,
and the proof) and C-IV (final honesty, roadmap, asks). 12 new slides:
C13-pre, C13-val, C13, C14, C15, C16, C16-bis, C17-pre, C17, C17-bis,
C18, C19.

Content-of-record: STORYBOARD_v3.md v3.1 (approved). Gate decisions
wired: twin PB-2 = (b) honest form (C17 twin card = 'first campaign of
the phase'; C17-bis row resolved). FD-5(ii) wired (C17-pre spoken
back-pointer). Section rule (C-III): NOTHING assumed about the method —
each concept explained at first occurrence with its engineering WHY.
"""

SLIDES_C34 = [
    # -------------------------------------------------------------- C13-val
    dict(
        id="C13-val", kind="new", layout="big_fig", minutes=1.0, cut="no",
        title="Before going where Rao cannot, the machine reproduces Rao",
        content=dict(
            fig=("figs/fig_c13val_clean.png",  # F-6: presentation relabel of the record figure
                 "Variational contour vs classical Rao contour, with deviation panel — in-house, two independent routes"),
            bullets=[
                "By a route independent of the classical construction, the machine recovers Rao's contour: max deviation ~2·10⁻³ of throat radius.",
                "Two routes, one contour — the literature's benchmark, passed.",
                "And it is fast: one design segment in 15–20 s; a full validation campaign in 10–14 minutes.",
            ],
        ),
        notes=(
            "SCRIPT: Before trusting a machine where no benchmark exists, "
            "ask it to pass the benchmark that does. On the classical "
            "maximum-thrust problem - the reduced case - our optimizer, by "
            "a route completely independent of Rao's construction, finds "
            "Rao's contour: maximum deviation two parts in a thousand of "
            "the throat radius, inside the error band we derived from the "
            "cross-code comparison. The picture is ours, of record. This "
            "is the credibility bridge: the method goes where Rao cannot, "
            "standing on a machine that reproduces Rao where he can.\n"
            "[F-6] On-slide figure = fig_c13val_clean.png: presentation "
            "relabel of the record figure (title + legend text plain-"
            "English; internal ids GENO/S18/K_RICH and the 91/91 count "
            "moved here; DATA PIXELS UNTOUCHED - relabel script "
            "relabel_c13val.py, declared in BUILD_LOG).\n"
            "[PROVENANCE - guard 15] Source figure = validation/"
            "brick2_profiles_record.png, record run S18 [X-TOCV] (carrier "
            "validation/PROGRESS_2026-08-06_S18_brick2run.md). Run "
            "verification counts (oracle 91/91, KKT vs derived threshold) "
            "live HERE, not on slide (guard 18). Used AS-IS (record "
            "figure; light restyle only if visual QA demands, no "
            "regeneration outside contract - BUILD_LOG decision).\n"
        ),
    ),
    # ---------------------------------------------------------------- C-ADJ
    # NEW SLIDE (user order CKP-S3-5(c), S4): first-encounter adjoint
    # explainer, placed before C13. Declared deviation: main deck 45 -> 46.
    dict(
        id="C-ADJ", kind="new", layout="fig_bullets", minutes=0, cut="S4v2", to_backup=True,
        title="What is an adjoint — the whole gradient for one extra solve",
        content=dict(
            fig=("figs/fig_cadj_cost.png",
                 None),  # home cost schematic: N+1 flow solves vs forward+backward
            bullets=[
                "The objective is one number: J, the cycle-averaged thrust of the shared wall.",
                "To improve a shape we need its slope dJ/d(shape) — for hundreds of wall parameters.",
                "The adjoint: one flow solve + one backward solve → every derivative at once, exact — the gradient a trust-region Newton then climbs.",
            ],
        ),
        notes=(
            "SCRIPT (first-encounter language, user order): Before showing "
            "the machine, the one idea it runs on. Everything we optimize "
            "is a single number: J, the cycle-averaged thrust delivered by "
            "the shared nozzle wall. To improve a shape you need to know "
            "which way to move it - the slope of J with respect to every "
            "wall parameter, and there are hundreds. The obvious route: "
            "wiggle one parameter, re-solve the flow, repeat - hundreds of "
            "flow solutions for a single design step. The adjoint route: "
            "solve the flow once forward, then solve ONE auxiliary problem "
            "backward - the adjoint - and it returns the derivative with "
            "respect to ALL parameters at once, exactly, for the price of "
            "roughly one extra solve. That exact gradient is what the "
            "trust-region Newton optimizer climbs, a few seconds per "
            "iteration. That is the entire trick - the rest of the "
            "machine is discipline around it.\n"
            "[PROVENANCE - guard 15] Pedagogical slide: no new record "
            "claims. Adjoint-exactness anchor = same as C14 card 2 "
            "(discrete-exact gradient; CH9-feed-4 THEOREM T-LEMB, "
            "reverse-AD = transposed adjoint); cost structure (1 forward "
            "+ 1 backward per gradient) = standard adjoint identity, "
            "program carrier X-TOCV first dJ/dW (S17/S18, of record). "
            "Figure = home schematic fig_cadj_cost.png (no data).\n"
            "[GUARD 18] internal names (X-TOCV, T-LEMB) here only."
        ),
    ),
    # ------------------------------------------------------------------ C13
    dict(
        id="C13", kind="new", layout="graph_l0", minutes=2.0, cut="no",
        title="From theory to a design machine: every choice on record",
        content=dict(
            fig=("figs/fig_method_flow.png", None),  # CKP-S3-3: method flow; dense graphs -> backup
            fig_note="six stages shown — the full eight-stage engineering record is in backup",
            bullets=[
                "The objective is one number: J, the cycle-averaged thrust of the shared wall.",
                "The adjoint: one forward + one backward solve → the exact dJ/d(shape) for every wall parameter — trust-region Newton climbs it in seconds.",
                "Every choice sits on a register with alternatives and a test that can reject it.",
            ],
        ),
        notes=(
            "SIGNPOST: agenda point 4 - the design machine.\n"
            "SIGNPOST: agenda point 4 - the design machine.\n"
            "SCRIPT: The machine, end to end. Engine data give the cycle at "
            "the interface - one state per phase. We form the cycle-averaged "
            "thrust of the shared contour: that integral IS the objective. A "
            "fast supersonic march solves each phase. Then the adjoint - and "
            "here is why: ONE extra backward solve returns the exact "
            "gradient of the objective with respect to ALL wall parameters "
            "at once; it is Hoffman's 1967 multiplier fields, made exact for "
            "the discrete problem (identity verified at machine precision). "
            "A trust-region Newton with measured curvature updates the "
            "contour - robust where curvature is irregular, with steps you "
            "can certify. And nothing ships alone: independent checks that "
            "can reject, error bars attached. Iterations take seconds.\n"
            "[CKP-S3-3/-4 wired] C13-pre MERGED here (user cut order): its "
            "four concepts (adjoint / discrete-exact / optimizer / "
            "certificate) live in the flow blocks and this script; its "
            "provenance rows absorbed below. Status-graphs -> backup only.\n"
            "[PROVENANCE - absorbed from C13-pre] reverse-AD = transposed "
            "adjoint -> CH9-feed-4 (THEOREM T-LEMB; mesh-limit SCHEMA "
            "S-LBML); continuous-first / per-role AD -> CH2-feed-5 (C56 "
            "CLOSED; O3.1 PRACTICE); optimizer adjudication -> C31 card "
            "(full card in backup).\n"
            "[PROVENANCE - guard 15] 62 typed choices, tally 12 DECIDED / "
            "36 MIXED / 12 NEVER / 2 SINGLE-AUTHOR, 48 adjudicated -> "
            "CH4-feed-1 ([REP]; the WHOLE tally lives here and in backup, "
            "never on slide - CKP-S2-3). STATUS SEMANTICS of record "
            "(choice_ledger.yaml:20-27, user challenge 2026-08-23): "
            "DECIDED = converged-panel/constructional/measured verdict "
            "(12); MIXED = operative branch DECIDED, a sibling branch "
            "NEVER (36) - so rows with a convergence-adjudicated branch "
            "= 48 (12+36), never say bare '12 decided' as the machine's "
            "state, and never 'each with alternatives+falsifier' (the 12 "
            "NEVER rows are open, owner+trigger). 'No rejecting chain in "
            "the field' -> CH9-feed-8 (NOT-FOUND(q), query-bounded - "
            "wording here). Graph = extracted from pipeline_graph.json, "
            "assert-gated 18/18 at build (DERISK §1-§4; C46 footnote on "
            "render; never hand-typed). CH4 W2-R2 form preserved in the "
            "document for retro-audit (WA_A3 critic 3).\n"
            "[GUARD 18] tally numbers and NOT-FOUND(q) here only."
        ),
    ),
    # ------------------------------------------------------------------ C14
    dict(
        id="C14", kind="new", layout="cards3", minutes=0, cut="S4v2", to_backup=True,
        title="Inside the optimizer stage — including what we will re-examine",
        content=dict(
            cards=[
                ("Why Newton with a trust region",
                 "curvature along these designs is irregular: measured curvature and a certifiable step beat quasi-Newton guesses"),
                ("Exact gradient underneath",
                 "the adjoint gradient is exact for the discrete problem — the optimizer never chases noise"),
                ("What we will re-examine",
                 "a 2026 solver candidate, comparison pre-registered at equal constraints — the solver census is dated"),
            ],
        ),
        notes=(
            "SCRIPT: Zoom into the optimizer stage - three panels: the "
            "engine and driver, the numerics and tolerances, the design "
            "basis. Two things to read. First, the driver choice you "
            "already met. Second - and this is deliberate - the re-"
            "examination flag: at the next phase entry this cluster is "
            "re-adjudicated against a named 2026 candidate from the "
            "literature, with a pre-registered comparison at equal "
            "constraints. Our solver census has a date on it, and we say "
            "so.\n"
            "[PROVENANCE - guard 15] C31 6-field card (incumbent TR-"
            "Newton; candidate Uno / MPC-2026; falsifier; re-exam window "
            "F2-entry) -> CH4-feed-9 - the COMPLETE card lives here and "
            "in backup (guard 14 satisfied in the layer); panel split of "
            "record -> DERISK §3.1 (24 nodes measured, 3 panels, ≤12 "
            "cards each); LL-15/LL-30.\n"
            "[GUARD 18] cluster ids (C31/C57/C58/C60) in notes/backup; "
            "slide says 'this cluster', 'a 2026 candidate'."
        ),
    ),
    # ------------------------------------------------------------------ C15
    dict(
        id="C15", kind="new", layout="graph_certs", minutes=0, cut="pos2", to_backup=True,
        title="How results are verified: certificates that can fail",
        content=dict(
            fig=("graph/L1_stage45.png", None),  # dense: backup slide
            bullets=[
                "Gradient exact for the discrete problem; cross-checked on a second code, with negative controls.",
                "Thresholds are derived, and they bite: halving one flips the verdict.",
                "Discretization and model error never mixed — each has its own estimator or bracket.",
                "Results ship together: contour, certificates, bars, verdict.",
            ],
        ),
        notes=(
            "SCRIPT: Certification, stages four and five. The gradient: "
            "exact for the discrete problem, machine-precision verified, "
            "cross-checked against a second code with negative controls "
            "that actually reject. Thresholds: derived, and they bite - "
            "halve one and the verdict flips; a certificate that cannot "
            "fail is not a certificate. Errors are never mixed: "
            "discretization has its estimator and an independent referee; "
            "model error has the per-channel bracket you saw. The shock "
            "front is treated with the only scheme that can carry a "
            "gradient certificate - Giles and Ulbrich published why. And "
            "nothing ships alone: contour, certificates, bars, verdict "
            "travel together.\n"
            "[PROVENANCE - guard 15] 52/52 + 218/218 checks -> CH4-feed-2 "
            "(numbers HERE); KKT 7.7e-2 vs derived 1.156e-1, oracle "
            "91/91, stage V0 -> CH4-feed-3 (numbers here; guard 7: "
            "engine-level claims declare evidence stage); NTF threshold "
            "bites (η·κ_q; GAP-29) -> CH4-feed-5; DWR vs model-form "
            "separation -> CH3-feed-9 (C11 DWR); fitted-front for "
            "gradient certificate -> CH4-feed-10 (C49, LL-12; Giles-"
            "Ulbrich negative theorem, published reason); Verdict format "
            "-> CH9-feed-2; G1 absolute gate -> CH9-feed-3 (here only).\n"
            "[GUARD 18] all counts in notes; slide keeps qualitative "
            "engineering statements + the Giles-Ulbrich name (published "
            "reason = a citation, allowed)."
        ),
    ),
    # ------------------------------------------------------------------ C16
    dict(
        id="C16", kind="new", layout="numbers_bars", minutes=0, cut="S4v2", to_backup=True,
        title="Speed was engineered, not found — validation becomes affordable",
        content=dict(
            fig=("figs/fig_c16_bars.png", None),  # target-vs-measured bars
            table_header=["quantity", "measured", "target"],
            table=[
                ("evaluation + gradient", "0.45 s", "—"),
                ("one design segment", "15–20 s", "≤ 30 s"),
                ("full campaign", "10–14 min", "≤ 25 min"),
                ("vs reference run", "18×", "—"),
            ],
            footline="Every speed lever passed an invariance gate: same results, same certificates. Our measurements, host declared.",
        ),
        notes=(
            "SCRIPT: Speed, because it changes what validation costs. "
            "Every acceleration lever had to pass an invariance gate - "
            "same results, same certificates - before adoption. Where we "
            "are: under half a second for an evaluation with gradient; a "
            "design segment in fifteen to twenty seconds against a "
            "thirty-second target; a full campaign in ten to fourteen "
            "minutes against twenty-five; eighteen times the reference "
            "run. Our measurements, host declared. The consequence is "
            "programmatic: validation campaigns become economic acts.\n"
            "[PROVENANCE - guard 15] Speed chain -> CH4-feed-4 ([REP], "
            "host caveat; record chain 100.84 -> 32.09 -> 5.58 s lives "
            "here); targets MET formal (S25-bis, pessimistic-end "
            "criterion pre-registered). Suite state and [X-SPDB] ids in "
            "notes only (accounting, guard 18); stage 'verified' said "
            "aloud, P34 tag here (guard 7).\n"
        ),
    ),
    # --------------------------------------------------------------- C16-bis
    dict(
        # MOVED TO BACKUP (CKP-S3-5(e), S4): the audit process-story leaves
        # the main deck; honesty shows via content (C11 table). Q&A-ready.
        id="C16-bis", kind="new", layout="audit_timeline", minutes=0,
        cut="S4e", to_backup=True,
        title="We commissioned a hostile audit — and the chain failed us",
        content=dict(
            timeline_cards=[
                ("Audit 1 — self-check threat", "we built the way our self-check could fail silently, exposed it, closed it with a solver-independent verification"),
                ("Audit 2 — hostile, on the certification chain", "verdict: not certifiable — two named defects; one repaired and declared, one with a named lead and date"),
            ],
            bullets=[
                "Audits must also reject falsehood: a planted decoy was rejected before verdicts counted.",
                "Cross-code agreement is never treated as truth.",
                "Across the audits, defects moved from the object to the certifier: the standard got stricter.",
            ],
        ),
        notes=(
            "SCOPE FIRST (speech duty, F-13): the audit judged our "
            "CERTIFIER, not the flow solutions - and it found the "
            "certifier wanting.\n"
            "SCOPE FIRST (speech duty, F-13): the audit judged our "
            "CERTIFIER, not the flow solutions - and it found the "
            "certifier wanting.\n"
            "SCRIPT: The slide I most want you to remember. We commissioned "
            "a hostile audit of our own certification chain - and the chain "
            "failed us: not certifiable, two named defects; one repaired "
            "in the same window and declared, one with an owner and a "
            "deadline. Before that, we had constructed ourselves the way "
            "our self-check could lie, exhibited it with a negative "
            "control, and closed it with a verification independent of the "
            "solver. Our audits are two-sided: they pass only if they "
            "confirm truth AND reject falsehood - a decoy built for the "
            "purpose was rejected before any verdict counted. We never "
            "treat agreement between our two codes as truth. And across "
            "the audits the defects moved from the certified object to "
            "the certifier itself - the floor rose. The system works "
            "because it fails us.\n"
            "[PROVENANCE - guard 15] Chain-said-NO -> CH9-feed-1 (S-CERT "
            "verdict NON-CERTIFIABLE, 2 P0: (vii) repaired in-window; "
            "staleness import-closure owner F2 - internal audit names in "
            "notes only); claim-before-evidence incident caught by "
            "recount -> CH4-feed-6+CH4-feed-7 (paired as per feed); "
            "self-check-could-lie + dual-seed canary -> CH9-feed-5 + "
            "CH9-feed-7 (SEED-OMIT caught, SEED-DECOY not flagged - the "
            "decoy line); agreement != truth -> CH9-feed-6 (MoC-critical "
            "standing: independent invariants); progress across audits -> "
            "CH9-feed-10. '23/23', '2 P0' and audit names (S-CERT etc.) "
            "in notes only (guard 18).\n"
        ),
    ),
    # --------------------------------------------------------------- C17-pre
    dict(
        # S4 LOT-A REWORK (act_rework/REWRITE_FINAL.md [42/C17-pre], applied)
        id="C17-pre", kind="new", layout="three_gaps", minutes=0, cut="S4v2", to_backup=True,
        title="Which gap dominates — and how we would find out",
        content=dict(
            columns=[
                ("mean-state design", "designs to the time-averaged flow; never compared head-to-head, by anyone"),
                ("our per-phase design", "this method"),
                ("true 3D optimum", "incomputable, for anyone"),
            ],
            gaps_label=("three distances: formulation (which problem you solve) · model (which physics "
                        "you keep) · end to end, the total — the question is which dominates"),
            hypothesis=("Working hypothesis, testable: at fixed constraints the formulation gap dominates "
                        "— three exact results each close a piece of the model gap (its smooth part); "
                        "none touch formulation. Its weak point: the wave-front jumps carry no bound yet "
                        "— if large, the model gap can win."),
            heel=None,
            death_line=("The programme fails only if two independent measurements both go against it: "
                        "the head-to-head and the residual measurement."),
        ),
        notes=(
            "SCRIPT (S4 rework): Three designs on one axis: a design "
            "built on the time-averaged flow; ours, built phase by phase; "
            "and the true three-dimensional optimum, which nobody can "
            "compute. Between them, two gaps in series - a formulation "
            "gap: you asked the wrong question of the flow; and a model "
            "gap: you kept the wrong physics - and the end-to-end "
            "distance to the truth is their composition, the third thing "
            "on the map. The value question of the whole enterprise is "
            "which of these dominates. Note the left comparison first: "
            "nobody has ever computed a time-averaged design against a "
            "phase-resolved one at equal constraints - us included; it "
            "is the first measurement on our plan. Our working "
            "hypothesis - a hypothesis, not a theorem, and it can be "
            "proven wrong: at fixed constraints, the formulation gap "
            "dominates. The grounds: three of the results you have "
            "already seen close pieces of the model gap on its smooth "
            "part - the exact change of coordinates, the vanishing mean "
            "equation, the cleared full-state average - while nothing "
            "yet bounds the formulation gap. The weak point travels with "
            "the hypothesis, on the same slide: the jumps at the wave "
            "fronts are the one unbounded first-order piece of the model "
            "gap - if they turn out large, the model gap can dominate "
            "anyway. And the programme fails only if two independent "
            "measurements both go against it - the head-to-head and the "
            "residual measurement; each of them is on the plan that "
            "follows.\n"
            "[FD-5(ii) wired] the spoken back-pointer to C8/C9/C10 is in "
            "the script above ('the three results you saw').\n"
            "[PROVENANCE - guard 15] Three designs / three gaps -> "
            "CH6-feed-1 (scope 'in the record', repair WB1-C3-14) + "
            "CH6-feed-2 (hierarchy hypothesis); heel CO-PRESENCE on the "
            "SAME slide -> CH6-feed-3 (binding print in feeds; guard 1: "
            "hierarchy NEVER without the (J) heel - THIS slide is the "
            "enforcement site); two-failure death -> CH6-feed-4; field "
            "does not separate the gaps -> CH6-feed-5 (NOT-FOUND in "
            "notes).\n"
            "[GAP-LETTERS MAP - FD-4 enforcement, CW-4] gap(A)=formulation "
            "/ gap(B)=model of the three-design frame DO NOT coincide "
            "with the historical namespace Gap A / Gap B (inverted): "
            "on-slide and in speech use ONLY the words 'formulation'/"
            "'model', never bare letters. (S4: C17 no longer shows "
            "letters either - historical namespace lives in C17's note "
            "for Q&A only.)\n"
            "[GUARD 18] channel letters and NOT-FOUND here."
        ),
    ),
    # ------------------------------------------------------------------ C17
    dict(
        # S4 LOT-A REWORK (act_rework/REWRITE_FINAL.md [43/C17], applied;
        # head-to-head card sharpened to the atlas form CH6:440/490 —
        # comparator = classical variational design at cycle-mean p0/T0,
        # identical constraints; same claim, sharper comparator)
        id="C17", kind="new", layout="roadmap_cards", minutes=1.5, cut="MAI",
        title="Four measurements, in order — consequences fixed before the data",
        content=dict(
            timeline_label="",
            cards=[
                ("1 · Residual",
                 "how much the phase-averaged equations miss, on nozzles already solved",
                 "small → error bars tighten; large → dominant source named",
                 "first — cheapest"),
                ("2 · Head-to-head",
                 "our per-phase design vs the classical design at cycle-mean p₀/T₀ — identical constraints; no such number exists yet",
                 "either result publishable",
                 "machine ready — first campaign"),
                ("3 · Coupled pair",
                 "same nozzle with and without the combustor: the cost of designing alone",
                 "~1% holds → estimate stands; exceeded → step 4 moves up",
                 "after step 1"),
                ("4 · Full 3D reference",
                 "~12M-cell reference the literature lacks",
                 "inside its band → the error band closes; outside → failing source named",
                 "route chosen now; commit decided after step 1"),
            ],
            gap_line=("Ours vs time-averaged: measurable in-house. The true 3D optimum: computable by "
                      "no one — we bound it."),
            kill_line=("Stop criterion: measured gain below ~1% Isp → effort pivots to certification "
                       "and operability."),
            closing=("First per-phase variational design method for RDE nozzles — "
                     "the head-to-head number comes next. Thank you."),
        ),
        notes=(
            "SCRIPT (S4 rework): This is the measurement plan, and the "
            "order is the content: four steps, each with its two "
            "possible outcomes and what each outcome triggers - fixed "
            "now, before any data arrive. Step one, the cheapest: "
            "measure the residual - take nozzle families the machine "
            "has already solved and checked, put them back into the "
            "full phase-averaged equations, and read how much is "
            "missed. Small residual: the error bars tighten and the "
            "family is promoted with a stated bar; large residual: it "
            "names which error source dominates - either outcome is "
            "informative, and it also builds the referee that the "
            "literature does not contain. Step two, the head-to-head - "
            "the reason this programme exists: our per-phase design "
            "against the classical variational design built on "
            "cycle-mean stagnation pressure and temperature, identical "
            "constraints, swirl bracketed out - does the optimal "
            "contour move, and how much thrust does the difference "
            "carry? Today no such number exists, on any side; a "
            "material gap pays for the method, a small gap proves "
            "standard practice right at that rank and we would be the "
            "first to prove it - both results are publishable. Step "
            "three: a paired simulation of the same nozzle with and "
            "without the combustor coupled, on the kind of template "
            "the field already uses - it prices what we give up by "
            "designing the nozzle alone. If the literature's roughly "
            "one-percent estimate holds, that row of the error table "
            "stands; if it is exceeded, the big reference run moves up "
            "the queue. Step four, the largest: a twelve-million-cell "
            "unsteady reference simulation - the benchmark the field "
            "lacks; today we choose only how to procure it, partner or "
            "purchase - whether to commit the run is decided after "
            "step one. One distance we can measure entirely in-house - "
            "ours against the time-averaged design; the other - the "
            "distance to the true three-dimensional optimum - no one "
            "can compute, so we bound it. And the stop criterion is "
            "fixed in advance: if the measured gain falls below about "
            "one percent of Isp, we stop pushing performance and pivot "
            "to certification and operability. The campaign has just "
            "opened: none of these results is promised as acquired.\n"
            "[S4 HEAD-TO-HEAD FORM] card 2 comparator = atlas CH6 :440 "
            "(I4 = Rao/GENO design on cycle-mean (<Pc>, T0, gamma)) + "
            ":490 (twin PB-2 at IDENTICAL constraints: same eps, L, "
            "closure); 'ZERO computed instances' of the comparator in "
            "the record (CH6 :712). Twin-first = kill-or-validate "
            "(CH6 :223-225). Internal names (I4, twin PB-2) here only.\n"
            "[GATE DECISION WIRED] Twin (b): card 2 reads 'first "
            "campaign' - NOT 'if ordered'; consistent with C7-ter and "
            "the backup open-decisions slide.\n"
            "[PROVENANCE - guard 15] Order of the four steps -> "
            "CH6-feed-9 (on-slide word 'roadmap' dropped, order kept); "
            "G2 value gate -> CH6-feed-6; value condition armed-"
            "rejector, today undecidable -> CH6-feed-7 (D-44 gated; "
            "'consequences fixed before the data' = plain form of the "
            "pre-registration of record); M-RED derived bands B-1..B-4 "
            "-> CH3-feed-6; twin kill-or-validate both-informative -> "
            "CH6-feed-4; B-lite cheap lever -> CH3-feed-10 + CH1-feed-8 "
            "(notes only). Card 4 'inside its band -> the error band "
            "closes' = Guard 6 / D-44 form (band closure, never a "
            "validation verdict). Internal names (M-RED / CFD-2 / CFD-1 "
            "/ twin PB-2 / I4) live HERE; slides carry speaking forms "
            "(guard 18).\n"
            "[GAP-LETTERS MAP - FD-4/CW-4, S4 UPDATE] Gap letters A/B "
            "appear NOWHERE on slide or in speech anymore (S4 rework): "
            "band 1 says the two distances in words ('ours vs "
            "time-averaged' / 'the true 3D optimum'). Historical "
            "namespace (A = distance to true 3D optimum; B = ours vs "
            "mean-state) kept HERE for Q&A cross-reference only; "
            "C17-pre's frame letters are inverted vs this namespace - "
            "always words, never letters.\n"
        ),
    ),
    # --------------------------------------------------------------- C17-bis
    dict(
        id="C17-bis", kind="new", layout="open_cards", minutes=0, cut="pos5", to_backup=True,
        title="Decisions we have not taken yet — said before you ask",
        content=dict(
            intro=("The head-to-head choice is taken: no number exists before it runs — and it runs as "
                   "the first campaign."),
            cards=[
                ("Two technical roads — open, with criteria",
                 "the treatment of mean swirl, and the priority of one wall closure: presented with alternatives and the decision criterion, not yet decided — lead and date named"),
                ("The data contract is not frozen",
                 "one physical hypothesis (full choking of the RDE interface) is declared open, with a named lead"),
                ("One gate still lacks a rejecting threshold",
                 "we will derive it as a number"),
            ],
        ),
        notes=(
            "SCRIPT: What we have NOT decided - said before you ask. The "
            "head-to-head choice we HAVE taken: no pre-milestone number; "
            "the machine is ready and it runs as the first campaign. "
            "Still open, deliberately: the treatment of mean swirl and "
            "the priority of one wall closure - both presented with "
            "alternatives and a decision criterion; the data contract - "
            "one physical hypothesis, full choking of the RDE interface, "
            "is open with an owner (and remember the condition from the "
            "feedback slide: decoupling is only assertable under "
            "verified choking); and one acceptance gate still lacks a "
            "rejecting threshold - we will derive it as a number.\n"
            "[PROVENANCE - guard 15] S-5F path A/B/C + C51 priority -> "
            "CH7-feed-8 (non-adjudicated cards of record, F2-entry per "
            "user decision at gate - names in notes); U3' PREMISE-OPEN "
            "-> CH10-feed-7 (owner F2a); G3 without rejector -> "
            "CH3-feed-7 (F5b); twin cross-ref -> C7-ter (RESOLVED (b) "
            "at the S2 gate - intro line reflects the decision, no "
            "open bifurcation remains). Guard 17 rider on the choking "
            "hypothesis line (spoken).\n"
            "[GUARD 18] internal names (S-5F, C51, U3', G3, PB-2) in "
            "notes only; cards carry speaking forms."
        ),
    ),
    # ------------------------------------------------------------------ C18
    dict(
        # S4 LOT-A REWORK (act_rework/REWRITE_FINAL.md [44/C18], applied)
        id="C18", kind="new", layout="ask_cards", minutes=0, cut="S4v2-noasks", to_backup=True,
        title="Three requests: a reference simulation, engine data, publication support",
        content=dict(
            cards=[
                ("1 · Reference 3D simulation",
                 "What: ~12M-cell reference run, by collaboration or procurement",
                 "To decide: the route — partner or purchase; the commit is decided after the residual measurement",
                 "When: route now, run later"),
                ("2 · Engine test data",
                 "What: high-speed pressure traces or hot-fire imaging",
                 "To decide: which rig, which instrumentation",
                 "When: starting now"),
                ("3 · Publication & access",
                 "What: venues for the method papers; three key papers we cannot access",
                 "To decide: endorsement",
                 "When: at your convenience"),
            ],
            input_band=("'What input does the method need?' Specs suffice to design; each added "
                        "measurement raises the confidence grade (scale in backup). Data outside the "
                        "required class is rejected — not yet exercised on real data."),
        ),
        notes=(
            "[F-4] Open-items card moved OFF-slide (three asks means three "
            "cards): still open, said if asked - mean-swirl route; one "
            "wall closure; data contract (choking hypothesis, named lead); "
            "one gate threshold to be derived as a number. Full open-items "
            "slide in backup. Reliability ladder: backup slide (moved off "
            "the band per F-4 option b, S4).\n"
            "SCRIPT (S4 rework): Three requests - for each: what we ask, "
            "what you would need to decide, and when. First, the "
            "reference simulation: today we ask only for the route - a "
            "collaboration or a procurement; the decision to actually "
            "run it comes after the residual measurement, exactly in "
            "the order of the plan you just saw. Second, engine test "
            "data in the class the method needs: high-speed pressure "
            "traces or hot-fire imaging, sufficient to verify that "
            "stagnation temperature is flat over a cycle and to read "
            "the cycle frequency. One property to be aware of: the "
            "input screen decides, it does not bless - it is built to "
            "reject data outside that class, and we expect real data "
            "to exercise it. That screening has not yet been tried on "
            "a real dataset. Third: publication venues for the method "
            "papers, and three key papers we currently cannot access. "
            "And the question every panel asks - what input does your "
            "method need: engine specifications alone are enough to "
            "produce a design; every additional measurement raises the "
            "confidence grade of the result, on a scale spelled out in "
            "the backup.\n"
            "[PROVENANCE - guard 15] Specs-ladder Annex B -> CH10-feed-1 "
            "(the most valuable feed; stage P34 'prediction' declared - "
            "tag here, words on slide); G6 loud-reject never exercised "
            "-> CH10-feed-2 (spoken form on slide); TRIPLE monitor -> "
            "CH7-feed-5 (detail 'a Γ-only monitor would license the "
            "false' here, recallable); procurement Tier-1 names "
            "(Fotia/Goto/Ma) -> MESSAGE_ARCHITECTURE §ASK (notes).\n"
            "[GUARD 18] P34/G6/monitor names in notes; card language "
            "engineering-only."
        ),
    ),
    # ------------------------------------------------------------------ C19
    dict(
        # S4 LOT-A REWORK (act_rework/REWRITE_FINAL.md [45/C19], applied).
        # BUDGET DECLARATION (REFUTE (12)): summary layout ≈66 net words
        # > 60 cap and 5 bullets > 3 — two-column record grammar is the
        # declared treatment; see BUILD_LOG S4 lot A.
        id="C19", kind="new", layout="summary", minutes=0, cut="S4v2", to_backup=True,
        title="What we discard is measurable — validation costs minutes, not weeks",
        content=dict(
            eng_head="For the engineers",
            eng_bullets=[
                "the first per-phase variational design method for RDE nozzles",
                "what the reduction discards is an explicit, measurable operator",
                "an error budget, source by source, each with its estimate",
            ],
            prog_head="For the decision-makers",
            prog_bullets=[
                "validation in minutes, not weeks",
                "a stepwise plan with known costs, fixed consequences, and a stop criterion",
            ],
            closing=("The method's limits are on these slides — each with a number, or the named way "
                     "to get one."),
            fig=("figs/fig_method_flow.png", "signature"),  # F-2/F-23: same naming as C13, legible, clear of footer
        ),
        notes=(
            "SCRIPT (S4 rework): Two things to retain. For the "
            "engineers: this is, as far as our search of the literature "
            "has found, the first per-phase variational design method "
            "for RDE nozzles. What the reduction throws away is not "
            "hand-waved - it is an explicit operator you can evaluate, "
            "so the approximation itself is measurable. The error "
            "budget is stated source by source, each entry with how it "
            "was estimated - a theorem, an order estimate, or a "
            "published datum - and where there is no number yet, the "
            "way to get one is named. For the decision-makers: the "
            "machine validates a design in minutes, not weeks - so "
            "testing this method is cheap. The plan is stepwise, its "
            "costs are known, and the consequence of each possible "
            "outcome is fixed before the data arrive - including the "
            "point where we would stop: below about one percent of "
            "measured Isp gain, effort pivots to certification and "
            "operability. How much better a nozzle designed this way "
            "will fly, nobody yet knows - no number exists, on any "
            "side, until the head-to-head runs; it is the first "
            "measurement of the campaign. That number is what we came "
            "here to go and get. Thank you.\n"
            "[PROVENANCE - guard 15] Closing band = per-limit claim, "
            "verified at build (heel: road named on C11; optimum shift: "
            "campaign on C17; input screen: real data on C18; "
            "formulation gap: head-to-head on C17); the open-decisions "
            "backup slide is NOT claimed by the main slides. "
            "Instrumented honesty -> CH6-feed-10 (D-44 / P34 / card "
            "discipline - shown by the band's content, the word "
            "'honesty' never said; sigle here; guard 18); dual takeaway "
            "-> MESSAGE_ARCHITECTURE. 'First' SPOKEN in the D-06 "
            "locked, query-bounded form (guard 9), rendered in the "
            "script verbatim ('as far as our search of the literature "
            "has found') - POINTER RECONCILED S4: A2 as built is "
            "agenda-only (CKP-S3-2) and carries no primacy sentence; "
            "the old note 'spoken as in A2' is superseded by this "
            "in-script rendering. Closing question answered by "
            "abstention (no gain number claimed) -> C17 card 2 anchor.\n"
        ),
    ),
]
