# SESSION LOG — 2026-07-16, Sessione 5: "Fase 1: P-1 skeleton + P-2 Lemma A (+ G0 spike)"
# [renumbered S4 -> S5 at step 15: a concurrent session claimed S4; see steps 14-15]

Append-only, total-order log (CLAUDE.md R3 + standing user directive).
One numbered row per step, per generated/modified .md, per codebase
action. Rows are ONLY appended at the end, never inserted.

Branch: `rde-nozzle-program`. HEAD at open: e23bb08.
Untracked at open (expected, untouched): GENO/, scratch_out.txt,
scratch_err.txt, validation/ADR_panel_2026-07-16.md (AWAITING USER
RATIFICATION — no implementation).

---

1. [R2 apertura] Verified branch `rde-nozzle-program` (git branch
   --show-current), HEAD e23bb08, tree clean except expected untracked.
   No other session active on this tree (single-session discipline per
   PROGRESS S2 note).
2. [R2 apertura] Read project memory (research-cycle-averaged-rao,
   gate-pre-esecuzione): state = S3 closed, Fase 1, NEXT = P-1
   skeleton / P-2 Lemma A / G0 spike; standing pre-execution gate
   directive active.
3. [R2 apertura] Read M0 (docs/rde_nozzle_MASTER.md) in full, with
   focus of record: D2.6 (problem (P) = pair (S*, delta), certified
   globality (iv), maximality rationale), Prop. 7 (G-B sonic-cap
   sharpening + OP-11-eps instance + SCOPE non-transfer remark:
   winners rank CLOSURES, premium_bound = tournament device), T7 (**')
   weighted transversality, Part III EAP + S-H bridge remarks.
4. [R2 apertura] Read PROGRESS (docs/rde_nozzle_PROGRESS.md): ORA = S3
   closed at e23bb08 (OP-11-eps DONE 1438b1b, P-2 outline 05001a5, G5
   text e23bb08); NEXT 1-3 = exactly this session's T1-T3; BLOCCATO =
   G5 dispatch, P-2 venue, ADR ratification, G0 decision at Fase 2,
   RaoPlug S1/S2. DECLARED RESTART POINT: Fase 1 (piano D6), tasks
   [F1/P-1], [F1/P-2], [F2-prep/G0].
5. [R2 apertura] Depth reads for the gate: D3 §10quater (Prop. G-B
   sharpened, OP-11-eps statements (1)-(5), non-transfer scope (5)),
   D6 §3 (publication stream: P-1 JPP after M1, P-2 time-sensitive,
   G5 gates all submissions), D2 §b0 (equation-numbered corpus: Rao
   1958 Eqs [1]-[15] page-verified vs RAO.pdf; Hoffman 1967 fields
   lambda1..lambda5 + E (Eq. 78), p. 676 corner death; constraint-pair
   equivalence; Sternin boundary function), P-2 outline of record
   (docs/rde_nozzle_P2_outline.md, esp. §4 skeleton and §5 O3 plan).
6. [R2 apertura] Verified artifacts of record exist on disk:
   figs/phase_diagram_op11.png, data/phase_diagram.{json,md},
   src/thrust/{bounds,phase_diagram}.py, tests/test_bounds.py,
   tests/test_phase_diagram.py (carriers for the P-1 claim map).

7. [GATE PRE-ESECUZIONE] (A) Plan adherence:
   - T1 [F1/P-1 skeleton] -> D6 Fase 1 ("quasi-1D foundations ...
     paper P-1") + D6 §3 stream P-1 (venue JPP; submission gated by
     M1 + G5, WRITING is not) + PROGRESS NEXT 1. PLACED.
   - T2 [F1/P-2 Lemma A] -> D6 §3 stream P-2 (TIME-SENSITIVE, RK-A) +
     P-2 outline §4 (paper §3 = Lemma A identification) + PROGRESS
     NEXT 2. PLACED.
   - T3 [F2-prep/G0 spike] -> D6 90-day plan item 2 (JAX unit-process
     spike instructing gate G0 decision at Fase 2) + PROGRESS NEXT 3.
     PLACED (optional, time permitting).
   (B) Upstream rigor audit (points the tasks rest on, re-read):
   - Sonic-capped ceiling in subcritical: PRESENT and consistent in
     M0 Prop. 7 (sharpening of record) and D3 §10quater (Prop. G-B
     sharpened; naive form test-rejected on 4 subcritical rows).
     Any P-1 text must carry the cap or the "min-cycle NPR >=
     critical" hypothesis explicitly.
   - Weighted transversality (**'): M0 T7(c) states the naive average
     is WRONG outside the T3 class; P-1 skeleton must state (**')
     as the implementable form (falsifier = wrong-averaging rejector
     in tests/test_bell_optimality.py).
   - Non-transfer scope D3 §10quater(5) + M0 Prop. 7 SCOPE: winners
     rank CLOSURES at equal eps_max, NEVER hardware sectors of (P);
     premium_bound = certified tournament device; bell-winning regions
     of (P) EXPECTED at contour level. P-1 skeleton section on the
     phase diagram MUST use exactly this semantics (grep gate at T1
     acceptance).
   - D2.6 canonical (P): optimum = PAIR (S*, delta) at declared
     constraint vector; P-1 must not state any unconditional-global
     claim outside M1/M2/M3 mechanisms.
   - No discrepancy found between M0 and D3/D2/D6 on these points at
     this read (consistency spot-checks: cap wording M0 Prop.7 ==
     D3 §10quater sharpening; (**') wording M0 T7 == D2 §b0 doctrinal
     point; premium_bound wording M0 == D3 (5) == PROGRESS). No R4
     back-propagation needed BEFORE the tasks.
   (C) VERDICT: **gate pre-esecuzione PASS** (references: M0 D2.6,
   M0 Prop. 7 + SCOPE, M0 T7(c); D3 §10quater(1)-(5); D2 §b0; D6 §3 +
   90-day item 2; PROGRESS NEXT 1-3). Tasks T1, T2, T3 cleared for
   execution in this order.

8. [T1 prep] Verified executable-carrier names for the claim map:
   tests/run_all.py groups (i)-(x) (read in full; group labels of
   record), data/phase_diagram.md (winner table + SCOPE block + knee
   table + subcritical strip PR in {49.2126, 64, 90} + vacuum sweep
   numbers), premium_bound max 64.7 s at (PR=90, eps_max=1) per
   PROGRESS/M0.
9. [T1 EXEC] WROTE docs/rde_nozzle_P1_skeleton.md — P-1 paper skeleton
   of record (venue JPP; submission gated M1+G5, declared in header):
   §0 metadata + negative-claims list; §1 intro with QUERY-BOUNDED
   novelty (C26); §2 Theorem 0 + O1/O2 + interface contract; §3 T0
   strengthened + N-SW + N6 negative scope; §4 collapse dichotomy
   (T3 proof, altitude duality, gamma_eff sharpness numbers of record,
   T4 THEOREM* with K-E closure citation); §5 T7/(**') with boxed
   naive-average warning + quasi-1D reduction; §6 G-B + SONIC CAP
   sharpening + OP-0 ladder; §7 phase diagram OP-11-eps with SEMANTICS
   FIRST (D3 §10quater(5) scope opens the section; (P) = D2.6 pair
   form in §7.0; premium_bound = tournament device §7.6; figure
   figs/phase_diagram_op11.png); §8 EAP + S-H bridges (quantitative
   3-5%/6-14% check, phi placement); §9 declared limits (OP-11
   CONJECTURE, P3/G12, D7 B1/B2 biases); appendices incl. A7
   reproducibility; §CM CLAIM MAP C1-C26, each claim -> class +
   falsifier + executable carrier (run_all groups (i)-(x) + data of
   record). Zero orphan claims by construction (map = acceptance
   checklist).
10. [T1 ACCEPT] Coherence grep on the skeleton (pattern:
    winner|hardware|dominan/dominat|optimal/best nozzle|plug is/wins):
    ALL hits are inside closure-semantics or scope-negation sentences
    (lines 22-28 header discipline, §7.1/7.6 scope, C17 "CLOSURE
    ranking only"); NO sentence reads a winner as a hardware verdict.
    VERDICT: T1 acceptance PASS (class+falsifier+carrier per section;
    zero orphans; grep clean).

11. [T1 COMMIT] 6263c22 "[F1/P-1] (T1): paper skeleton of record (JPP)
    with claim map C1-C26" (skeleton + this log, steps 1-10).
12. [T2 prep] Read GENO/docs/theory_variational_understanding.md
    (in-house corpus of record, page-verified vs primary PDFs; GENO
    read-only, never committed here): Rao 1958 Eqs [1]-[15] with pages,
    Hoffman 1967 anchors (fields lambda1..lambda5, single isoperimetric
    multiplier p. 672, E Eq. 78, corner death p. 676), C+/C- naming
    trap (Rao's "C+" = Zucrow C-), corner sign doctrine (CSTR_PA '-',
    CSTR_PB '+', sign from characteristic TYPE), normalization
    conventions.
13. [T2 EXEC] IN-SESSION RE-DERIVATION of the full classical
    stationarity system from the Rao Lagrangian (L.4): d/dphi, d/dtheta,
    d/dW conditions; combination collapses to
    sin(theta)[(M^2-1)sin^2psi - cos^2psi] = 0 => phi = theta +/- alpha
    (Eq. [11] as RESULT); lambda2 elimination => f2 = W cos(theta -/+
    alpha)/cos(alpha) = -lambda2 (Eq. [12]); (L.6) => q rho W^2 sin^2
    theta tan alpha = -lambda3 (Eq. [13], 2pi-normalization declared);
    free-endpoint density-vanishing => sin(2 theta_E) = (p-pa)cot
    alpha/(0.5 rho W^2) (Eq. [14] == CSTR_PA) and C- mirror by
    alpha -> -alpha (== CSTR_PB). ALL rows MATCH the page-verified
    corpus table — NO discrepancy found (no corrective R4 needed; the
    derivation itself is new written theory). WROTE
    docs/rde_nozzle_P2_lemmaA.md (paper §3 draft of record): §3.0
    scope/conventions (Zucrow naming, Rao translation declared), §3.1
    equation-numbered recall, §3.2 the eight-step derivation (THEOREM),
    §3.3 adjoint problem + Prop. A1 (adjoint characteristics = flow
    characteristics, det argument, THEOREM), §3.4 identifications
    (i)-(iii) THEOREM* (structure derived; explicit B2/B3 component
    match PENDING O3.3) and (iv) SCHEMA (Hoffman anchors verified;
    component map PENDING page re-read — NO equation numbers invented),
    §3.5 downstream yield, §3.6 claim register + PENDING register
    P-A1..P-A3. Acceptance: no "si vede che" — every identity carries
    its justification or a PENDING mark with falsifier.
14. [CONCURRENCY — DECLARED DEVIATION] After step 13, discovered a
    CONCURRENT session on the same tree (violates the one-session
    discipline of PROGRESS S2 note; reconciled): commits f6a5112 (G5
    dispatch package), 5540fe2 (P-2 VENUE DECISION OF RECORD: AIAA
    Journal primary + arXiv preprint at (G5 pass AND Lemma-A draft
    ready); fallback Aerospace with declared triggers; outline §7
    rewritten proposal->DECISION), cd903d1 (its log
    validation/PROGRESS_2026-07-16_S4_G5venue.md, claiming the name
    S4). Reconciliation: content disjoint from this session's work (my
    edits touch outline §4 pointer + D3 §8 + new files); my uncommitted
    edits applied cleanly on top; BLOCCATO row "venue P-2" is now
    RESOLVED by that session. NOTE: the P-2 venue decision plus the
    Lemma-A draft of step 13 together arm the "arXiv at G5" trigger
    (draft ready = half the condition; G5 pass still pending with
    user).
15. [RENUMBER] This session renumbered Sessione 4 -> SESSIONE 5 (S4
    taken by the concurrent session). Header annotated; numbering of
    steps unchanged (append-only preserved).
16. [USER DIRECTIVE — mid-session] "un'altra accertazione di tutta la
    teoria è che sia sempre generale a gamma variabile": recorded as
    STANDING AUDIT CRITERION. Actions, same session (R4):
    (a) gamma-variable audit of the §3.2 derivation: uses ONLY
    dh = dp/rho along the isentrope + c^2 = dp/drho|_s => (L.6)-(L.16)
    are EOS-GENERAL (frozen gamma(T), arbitrary convex EOS,
    homentropic) — THEOREM, audit trace written into
    docs/rde_nozzle_P2_lemmaA.md §3.0 (new block) + claim-register row;
    true gamma=const boundaries named: corner<->eps bijection (E4,
    oracle S-H 1971 Table 2/G2), T3 Lemma B (calorically perfect), S-H
    eps-rung closed forms.
    (b) D3 §8: gamma-variable audit paragraph appended to the Lemma-A
    status upgrade.
    (c) P-1 skeleton acceptance rule extended with item (e): every
    claim declares its gamma status (map C1-C26 classified).
    (d) memory/gamma-variable-generality.md written + MEMORY.md index
    line (standing directive, applies at every future gate (B)).

17. [T2 COMMIT] 18c9d88 "[F1/P-2] (T2): Lemma A draft of record" (draft
    + outline §4 pointer + D3 §8 upgrade + skeleton rule (e) + log
    steps 11-16).
18. [USER DECISION — mid-session] "GENO lo lasceremo in Fortran, se ciò
    non altera la funzionalità dell'intera pipeline": recorded. This
    RATIFIES the dual-code plan of record (M0 VI.7: differentiable
    engine = NEW code, GENO-Fortran = independent reference, oracle
    O3.4 cross-code). Condition carried into gate G0: the stack
    decision must include GENO-interop feasibility (file-based
    exchange + cross-code oracles) so the WHOLE pipeline keeps
    functioning with GENO untouched.
19. [T3 EXEC] Environment check: JAX absent; pip dry-run showed
    jax 0.11.0 (CPU) installable WITHOUT touching the numpy 2.2.6 pin.
    DECLARED user-level install executed: jax 0.11.0 + jaxlib 0.11.0 +
    ml_dtypes 0.5.4 + opt_einsum 3.4.0; verified numpy 2.2.6 intact,
    CPU device up. (Rollback: pip uninstall of the four packages.)
20. [T3 EXEC] WROTE validation/g0_spike_jax_moc.py — G0 spike: interior
    point + inverse/design-mode wall point as Newton-solved implicit
    residual systems wrapped in jax.custom_vjp with the implicit-
    function rule (adjoint solve on Jz^T, Newton NEVER unrolled, per
    M0 VI.3); planar, calorically perfect PM closure with GAMMA STATUS
    declared (structure EOS-general, closure gamma=const, A1 engine =
    gamma(T) backend); TOC-regime states (gamma = 1.23, M ~ 2.2-2.35);
    full Jacobian via jax.jacrev vs central FD at two steps with
    DERIVED tolerance (Richardson two-step error estimate + roundoff
    floor, constants derived in-comment from the FD error balance);
    Newton self-certification rejector; NEGATIVE CONTROL (corrupted
    vjp must fail).
21. [T3 VERDICT] Run PASS: Newton residuals 1.1e-16 / 2.8e-17 (tol
    ~4e-14); Jacobians 36/36 + 16/16 entries within derived tolerance
    (worst err/tol 3.3e-2 / 4.6e-2); negative control REJECTED as
    required (35/36 entries out, worst err/tol 2.3e4). G0 feasibility
    VERDICT: JAX stack viable on this machine (CPU, f64) with the
    numpy pin intact; implicit-vjp discipline demonstrated; decision
    G0 remains formally at Fase 2 per plan, now INSTRUCTED by an
    executable artifact.
22. [T3 COMMIT] b07b47e "[F2-prep/G0] (T3): JAX spike - differentiable
    MOC unit processes with implicit custom_vjp, PASS".
23. [USER Q&A — logged] User asked (mid-session) for the formal
    restatement of what/how/why JAX and for the gamma-variable status
    of the whole chain (incl. Rankine-Hugoniot). Answered in the
    session summary with pointers of record: RH jump conditions =
    EOS-general conservation statements, and T3's Lemma A scaling is
    verified ACROSS transversal shocks for gamma(T) (M0 Theorem 5
    proof, degree-1 homogeneity of RH fluxes at fixed (u,T)); V_id of
    Prop. G-B is EOS-general (h(s, Pa)); the sonic-CAP criterion is
    EOS-general while its closed-form critical-ratio EVALUATION in the
    executable ladder is gamma = const (declared); gamma = const
    boundaries of record: T3 Lemma B, corner<->eps bijection (E4,
    oracle S-H 1971 Table 2/G2), S-H eps-rung closed forms, spike PM
    function (declared in-file); A1 engine = gamma(T) backend by
    design (M0 VI.2), REACTING gas is the separate N4 rung (Hoffman
    p. 676: corner dies, E = 0 replaces it). No new record needed —
    all statuses already written in M0/D3/draft/memory.
24. [R3 CHIUSURA] PROGRESS updated (new ORA = S5 closure with S4
    interleave; NEXT 1-4 for S6; BLOCCATO: G0 row updated with spike
    verdict + GENO-interop criterion; LOG: S5 + S4 entries added).
    Project memory updated (research-cycle-averaged-rao: S5 state +
    two user directives; new memory gamma-variable-generality.md +
    MEMORY.md index). Session log CLOSED at step 24. Deviations
    declared: concurrency with S4 (reconciled); JAX install (declared,
    reversible); no other deviations from the plan.

25. [POST-CLOSURE ADDENDUM — user challenge on gamma generality]
    User rejected any load-bearing gamma=const: "tutto deve essere
    completamente generale, no traccia di ipotesi gamma costante in
    nessuna parte". Response of record (honesty preserved): T3's EXACT
    collapse is PROVABLY false for gamma(T) (two-gamma counterexample,
    M0) — it cannot be generalized, only DEMOTED. Directive codified
    as ARCHITECTURE INVERSION: primary objects = the EOS-general ones
    (per-phase stationarity (L.6)-(L.16), T7/(**') at adjoint level,
    V_id in h(s,Pa) form, sonic-cap criterion, gamma(T) A1 backend);
    gamma=const admitted ONLY as declared oracle instances or demoted
    corollaries (T3 collapse, gamma_eff closure, S-H eps forms), never
    as a hypothesis a deliverable needs. Edits: memory
    gamma-variable-generality.md STRENGTHENED; PROGRESS NEXT 5 added
    ([F1/OP-0-gamma]: purge gamma=const from the executable ceiling
    via Cantera h(s,P) evaluation of V_id + sonic cap, closed forms
    demoted to declared oracles, dual-route rejector); P-1 skeleton
    rule (e) strengthened; D3 §8 gamma paragraph extended.
26. [POST-CLOSURE ADDENDUM — user question on GENO/JAX] User asked
    whether the original plan involved TRANSLATING GENO to JAX and
    whether "GENO stays Fortran" steered the program suboptimally.
    Answer of record: NO translation was ever planned — M0 VI.7 and
    D6 (A1-A3) have always specified the differentiable engine as NEW
    code (JAX or Julia/Enzyme, gate G0) with GENO-Fortran kept as the
    INDEPENDENT reference (dual-code discipline, oracle O3.4,
    dual-route B1/B2). A port would DESTROY the certification value:
    independence is what makes cross-validation meaningful (shared
    bugs cancel in a port). GENO's role stays: reference + known-bug
    fixes IN FORTRAN (RaoPlug S1/S2 gated by the Rao-1961 Table-1
    oracle). The user decision coincides with the plan of record and
    ADDS an explicit G0 interop criterion — an improvement, zero
    deviation.
27. [HANDOFF] Session-6 prompt delivered to the user (tasks =
    PROGRESS NEXT 1-5 reprioritized: Lemma B + P-A1 time-sensitive
    first, then OP-0-gamma purge, PMM sweep, P-1 §2/§4 text incl. the
    Lemma-C pedagogical line agreed in conversation, spike extension;
    gate pre-esecuzione now includes the gamma-status question per the
    strengthened directive; one-session-at-a-time rule made EXPLICIT
    after two violations). SESSION 5 DEFINITIVELY CLOSED at step 27.
28. [POST-CLOSURE ADDENDUM — R4, multiplicity question] User asked
    whether wave multiplicity changes the optimal contour or whether
    mode-independence can be proven. NEW remark of record written to
    D3 §10quater(6): (a) THEOREM (T3-affinity corollary): within
    H1-H4 the optimum depends on μ only through ⟨Pc⟩ — modes with
    equal mean pressure share the SAME optimal fixed wall; (b) SCHEMA
    (O2 corollary, feed-closure caveat): k co-rotating waves give
    PR_k = PR_1^(1/k) — multiplicity moves the cycle along the PR
    axis of the ε-level phase diagram toward the T3 tie column, so
    outside the collapse class (free boundary/truncation/subcritical)
    the optimum IS k-dependent and the diagram already quantifies it
    (premium_bound and T4 knee decrease with k). H3 shape-channel and
    multistability (CVaR/DRO) declared on top.
