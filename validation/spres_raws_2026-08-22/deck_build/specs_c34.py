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
                "Two routes, one contour — the field's benchmark, passed.",
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
    # ------------------------------------------------------------------ C13
    dict(
        id="C13", kind="new", layout="graph_l0", minutes=2.0, cut="no",
        title="From theory to a design machine: every choice on record",
        content=dict(
            fig=("figs/fig_method_flow.png", None),  # CKP-S3-3: method flow; dense graphs -> backup
            fig_note="six stages shown — the full eight-stage engineering record is in backup",
            bullets=[
                "Every choice on a register, with alternatives and a test that can reject it — open choices declared, with a named lead and date.",
                "No published design method ships inside a chain built to reject it.",
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
        id="C14", kind="new", layout="cards3", minutes=1.5, cut="no",
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
        id="C16", kind="new", layout="numbers_bars", minutes=1.0, cut="MAI",
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
        id="C16-bis", kind="new", layout="audit_timeline", minutes=1.5, cut="no",
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
        id="C17-pre", kind="new", layout="three_gaps", minutes=1.5, cut="no",
        title="Which gap dominates — the honest map",
        content=dict(
            columns=[
                ("mean-state design", "the comparator — which nobody has computed in this head-to-head, us included"),
                ("our per-phase design", "the programme"),
                ("true 3D optimum", "incomputable — for anyone"),
            ],
            gaps_label="three gaps: formulation · model · composition — the value question is which dominates, on which axis",
            hypothesis=("Working hypothesis (declared, falsifiable): at fixed constraints the formulation "
                        "gap dominates — three suppression results on the model gap, none on formulation. "
                        "Its weak point, stated with it: front jumps are unsuppressed, no number yet — if "
                        "large, the model gap can dominate."),
            heel=None,
            death_line=("Programme failure needs two independent misses — both measurable: head-to-head + "
                        "residual measurement."),
        ),
        notes=(
            "SCRIPT: The value map, honestly. Three designs on the board: "
            "the mean-state design - the comparator, which nobody has ever "
            "computed in this controlled head-to-head, us included; ours; "
            "and the true three-D optimum, which nobody can compute. Three "
            "gaps between them - formulation, model, composition - and the "
            "value question is which dominates. Our working hypothesis - "
            "declared, falsifiable, not a theorem: at fixed constraints "
            "the formulation gap dominates, because on the model gap we "
            "hold three suppression results on the smooth part - the "
            "exact change of coordinates, the vanishing mean channel, the "
            "exonerated full-state mean, the three results you saw - "
            "while on the formulation gap there is none. But always with "
            "the heel: the front jumps are the unsuppressed first order "
            "of the model gap, no number yet - if large, the model "
            "dominates anyway. And programme death needs two independent "
            "failures, each measurable separately.\n"
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
            "'model', never bare letters. (C17 defines Gap A/Gap B "
            "inline in the historical sense - see its note.)\n"
            "[GUARD 18] channel letters and NOT-FOUND here."
        ),
    ),
    # ------------------------------------------------------------------ C17
    dict(
        id="C17", kind="new", layout="roadmap_cards", minutes=1.5, cut="MAI",
        title="What tightens the bracket, in order — every outcome pre-registered",
        content=dict(
            timeline_label="the roadmap = what tightens the bracket, in order",
            cards=[
                ("1 · MEASURE THE RESIDUAL",
                 "measured residual bands, per certified family",
                 "small → promoted, with a bar; large → dominant channel named",
                 "first campaign — starting now"),
                ("2 · HEAD-TO-HEAD",
                 "first number: our design vs mean-state design, equal constraints",
                 "material gap → method pays; small → field proven right — both publishable",
                 "cheap; machine ready — first campaign"),
                ("3 · PAIRED COUPLED RUN",
                 "price of the substitution, on the field's template",
                 "bar holds → ~1% sizing stands; exceeded → class run becomes priority",
                 "after the residual measurement"),
                ("4 · REFERENCE-CLASS RUN",
                 "~12M-cell decider anchoring the 3D bound",
                 "inside → bracket closes; outside → channel identified",
                 "decided after the residual — today: channel, not commit"),
            ],
            gap_line=("Gap B (ours vs mean-state) is measurable in-house; Gap A (distance to the true 3D "
                      "optimum) no one can compute — we bound it."),
            kill_line=("Declared stop criterion: measured gain below ~1% Isp → pivot to certification & "
                       "operability."),
            closing="Every outcome is pre-registered: the decision rule is fixed before the data arrive.",
        ),
        notes=(
            "SCRIPT: The roadmap is not a wish list - it is the ordered "
            "list of what tightens the bracket, and every outcome is "
            "pre-registered. First and cheapest: measure the residual on "
            "certified families - it builds the referee that does not "
            "exist in the literature; either outcome is informative. The "
            "head-to-head: the machine is ready, and it is the first "
            "campaign of the phase that opens now - no number exists on "
            "any side before it runs; a material gap pays the method, a "
            "small gap makes the field right at that rank and we would "
            "be the first to prove it - both publishable. Then the "
            "paired coupled run on the field's template; and only after "
            "the residual measurement, the reference-class decision - "
            "today we decide the CHANNEL, not the commit. Gap B we "
            "measure in-house; Gap A nobody can compute - we bound it. "
            "And the honest death criterion: below about one percent of "
            "measured Isp gain, we pivot to certification and "
            "operability - we do not insist. The phase is JUST opened: "
            "no campaign result is promised as acquired.\n"
            "[GATE DECISION WIRED] Twin (b): the card reads 'first "
            "campaign of the phase' - NOT 'if ordered'; consistent with "
            "C7-ter and C17-bis.\n"
            "[PROVENANCE - guard 15] Roadmap order -> CH6-feed-9; G2 "
            "value gate -> CH6-feed-6; value condition armed-rejector, "
            "today undecidable -> CH6-feed-7 (D-44 gated; 'pre-"
            "registered outcomes' = form of record); M-RED derived bands "
            "B-1..B-4 pre-registered -> CH3-feed-6; twin kill-or-"
            "validate both-informative -> CH6-feed-4; B-lite cheap lever "
            "-> CH3-feed-10 + CH1-feed-8 (notes only). Internal names "
            "(M-RED / CFD-2 / CFD-1 / twin PB-2) live HERE; slides "
            "carry the speaking forms (guard 18).\n"
            "[GAP-LETTERS MAP - FD-4/CW-4] Gap A / Gap B on this slide "
            "= HISTORICAL namespace (A = distance to true 3D optimum; "
            "B = ours vs mean-state), defined inline on the slide; do "
            "NOT confuse with the three-design frame letters of "
            "C17-pre (inverted) - in speech use the words, not bare "
            "letters, when crossing the two frames.\n"
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
        id="C18", kind="new", layout="ask_cards", minutes=1.5, cut="MAI",
        title="Three asks — each one decision-ready",
        content=dict(
            cards=[
                ("1 · The reference-class run",
                 "WHAT: collaboration or procurement, ~12M-cell class decider",
                 "TO DECIDE: the channel — the commit comes after the residual measurement",
                 "WHEN: channel now; run later"),
                ("2 · Engine data in the declared class",
                 "WHAT: high-speed pressure / hot-fire imaging",
                 "TO DECIDE: which rig, which instrumentation window",
                 "WHEN: starting now"),
                ("3 · Publication & procurement",
                 "WHAT: venues for the method papers + three key papers we cannot access",
                 "TO DECIDE: endorsement of channels",
                 "WHEN: at your convenience"),
            ],
            input_band=("'What input does your method need?' — Specs suffice to design; every extra datum "
                        "climbs a declared reliability ladder (full ladder in backup). Data is not fed in: "
                        "it is admitted — and the entry gate can say no. (A contract prediction — not yet "
                        "exercised on real data.)"),
        ),
        notes=(
            "[F-4] Open-items card moved OFF-slide (three asks means three "
            "cards): still open, said if asked - mean-swirl route; one "
            "wall closure; data contract (choking hypothesis, named lead); "
            "one gate threshold to be derived as a number. Full open-items "
            "slide in backup. Reliability ladder: backup slide.\n"
            "[F-4] Open-items card moved OFF-slide (three asks means three "
            "cards): still open, said if asked - mean-swirl route; one "
            "wall closure; data contract (choking hypothesis, named lead); "
            "one gate threshold to be derived as a number. Full open-items "
            "slide in backup. Reliability ladder: backup slide.\n"
            "SCRIPT: Three asks, each decision-ready - what we ask, what "
            "you need in order to decide, by when. One: the reference-"
            "class run - today we ask only for the CHANNEL, collaboration "
            "or procurement; the commit decision comes after the residual "
            "measurement, exactly as the roadmap ordered. Two: engine "
            "data in the class the method requires - high-speed pressure "
            "or hot-fire imaging sufficient to verify stagnation-"
            "temperature flatness and cycle frequency. Be aware: our "
            "monitor DECIDES, it does not bless - it is built to reject "
            "data outside the class, and we expect real data to exercise "
            "it. Three: publication channels, and three key papers we "
            "cannot access. And the question every panel asks - what "
            "input do you need: specs suffice; more data climbs a "
            "declared ladder - that ladder is on the slide, cases A to "
            "G. Evidence level said honestly: this is a contract "
            "prediction, not yet exercised on a real dataset.\n"
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
        id="C19", kind="new", layout="summary", minutes=1.0, cut="MAI",
        title="A method you can audit — fast enough to validate economically",
        content=dict(
            eng_head="For the engineers",
            eng_bullets=[
                "the first per-phase variational design method for RDE nozzles",
                "what the reduction discards is an explicit, measurable operator",
                "an honest error bracket, channel by channel, each cell with its evidence level",
            ],
            prog_head="For the programmes",
            prog_bullets=[
                "validation in minutes, not weeks",
                "an incremental plan, already priced, with pre-registered outcomes — and a declared stop criterion",
            ],
            closing=("Honesty here is not a disclaimer — it is built into the method: limits stated on "
                     "the slides, with their evidence levels."),
            fig=("figs/fig_method_flow.png", "signature"),  # F-2/F-23: same naming as C13, legible size
        ),
        notes=(
            "SCRIPT: Two take-aways. For the engineers: the first per-"
            "phase variational design method for RDE nozzles, with the "
            "discarded physics turned into an explicit measurable "
            "operator and an honest per-channel error bracket. For the "
            "programmes: a machine fast enough to make validation an "
            "economic act, an incremental plan already priced with "
            "pre-registered outcomes, and a declared honest-death "
            "criterion. And the line I want to leave you with: our "
            "honesty is not a disclaimer - it is instrumented inside "
            "the method. You saw the limits written on the slides, with "
            "their evidence levels. Thank you.\n"
            "[PROVENANCE - guard 15] Instrumented honesty -> CH6-feed-10 "
            "(D-44 / P34 / card discipline - the instrumentation SAID "
            "with content, sigle here; guard 18); dual takeaway -> "
            "MESSAGE_ARCHITECTURE (takeaway duali). 'First' in D-06 "
            "locked form, query-bounded (guard 9) - spoken as in A2.\n"
        ),
    ),
]
