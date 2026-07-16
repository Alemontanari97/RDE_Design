# SESSION LOG — 2026-07-16, Sessione 6 (DEDICATA RIGORE): "attacco ai
# punti scoperti — P-A1, P-A2, P3"

Append-only, total-order log (CLAUDE.md R3). One numbered row per
step. Branch `rde-nozzle-program`, HEAD at open: aaf8b25. Same
conversation as S5 (user: "attaccalo in questa sessione"); R2 reads
(memoria, M0, PROGRESS, Lemma-A draft, P-2 outline) are in-context
from S5 and re-declared here.

1. [R2 apertura] Restart point declared: S5 closed at aaf8b25; this
   session = Sessione 6 dedicata rigore, tasks [F1/P-2] P-A1 + P-A2,
   [F1/P3], optional [F1/OP-11-molteplicita] + Lemma-B mesh-limit.
   The previously drafted "S6" task list becomes Sessione 7.
2. [R2 apertura] PROGRESS NEXT extension DECLARED (plan placement per
   gate A): new NEXT entries to be added at close — P-A1/P-A2 serve
   the P-2 rigor upgrades (D6 §3 stream, TIME-SENSITIVE), P3 serves
   T7 rigor (P-1/P-4 stream). All fit Fase 1 (quasi-1D foundations /
   theory consolidation); no orphan step.
3. [R2 apertura] Environment: sympy 1.14.0 available (no install
   needed); Hoffman 1967 PDF in-house = GENO/literature/
   hoffman-2012-...-chemically-reacting-gas-flows.pdf (AIAA electronic
   re-issue of AIAA J 5(4):670-676, 1967). GENO read-only.

4. [GATE PRE-ESECUZIONE] (A) Plan adherence: T1 (P-A1) -> Lemma A
   §3.6 PENDING register + D6 §3 P-2; T2 (P-A2) -> same; T3 (P3) ->
   D3 §9 P3 entry + M0 T7 named gap; T4/T5 optional per prompt. All
   placed (with the NEXT extension of step 2). (B) Upstream rigor:
   re-read of Lemma A §3.4 in-context — the (i) justification uses a
   dimension-counting argument on admissible trace variations; this
   is the very object T1 attacks: any discrepancy found will be
   treated as DISCOVERY with R4 refinement of the draft (not silent
   patching). Gamma question: T1 symbolic work will be run in
   primitive variables with c^2 symbolic (EOS-general form) AND
   perfect-gas instantiation as cross-check; T2 (Hoffman) is the
   reacting-gas bank (frozen-gamma boundary NOT load-bearing); T3 is
   measure-theoretic (gamma-free). Scope §10quater(5) untouched by
   all tasks. (C) VERDICT: **gate pre-esecuzione PASS** (refs: Lemma A
   draft §3.4/§3.6; D3 §8/§9; D6 §3; M0 T7/D2.6).

5. [T1 EXEC] WROTE validation/pa1_symbolic_lemmaA.py: Part 1 = sympy
   machine verification of the ENTIRE §3.2 classical derivation under
   EOS-general closure rules (dp/dW = -rho W, drho/dW = -rho W/c^2,
   c = W/M symbolic): (L.6), (L.7), (L.10) factorization, (L.12) C+
   and C- families, (L.13), (L.15) corner == CSTR_PA, (L.16) mirror
   == CSTR_PB, + rejector R1 (sign-corrupted corner must fail).
   Part 2 = KERNEL SOLVABILITY LEMMA, EOS-general (c free symbol):
   eigvec check + both flux-covector contractions + rejector R2
   (family specificity) + the exploratory kernel-ratio identity.
6. [T1 DEBUG — declared] First run: 2 FAILs, BOTH script
   normalization bugs, zero math errors: (a) target of (L.10) carried
   a spurious 1/M^2 (the machine lhs equals the hand result exactly;
   bonus identity of record: (M^2-1)sin^2 psi - cos^2 psi ==
   M^2 sin^2 psi - 1); (b) |n| = 1 constraint not substituted in the
   <grad g, r-> check (residual was c rho u (nx^2+ny^2-1), i.e. zero
   under the constraint). Fixed both; re-run.
7. [T1 VERDICT] PASS 14/14 (8 derivation identities + eigvec + 2
   contractions + ratio identity + rejectors R1/R2 both PASS).
8. [T1 DISCOVERY + R4] Prop. A2 (kernel solvability) shows the first
   draft's dimension-count justification of identification (i) was
   TOO LOOSE: on a characteristic surface the adjoint b.c. (L.22) is
   solvable for EVERY lambda2 (both flux covectors annihilate the
   tangent-family kernel identically); moreover the pointwise kernel
   ratio does NOT reproduce f2 (computed: W cos(al) cos(th+al)).
   Hence the invariant does NOT live in the pointwise boundary
   algebra: the adjoint reading of Rao's conditions is the
   TANGENT-FAMILY TRANSPORT along Sigma. R4 SAME SESSION: draft
   §3.3 (new Prop. A2 with carrier), §3.4(i) rewritten (refined
   route), §3.4(ii) precision paragraph, §3.6 register rows updated,
   PENDING P-A1 NARROWED to P-A1' (derive the adjoint transport
   relation and exhibit f2 as its first integral); D3 §8 upgraded
   with the rigor-session paragraph. HONEST STATUS: P-A1 partially
   discharged (solvability half = THEOREM machine-verified; transport
   half = P-A1', precisely stated, open). Classes (i)-(iii) stay
   THEOREM* with the refined route — no overclaim.

9. [T1 COMMIT] 5ec62ef "[F1/P-2] (rigore-T1): P-A1 attack - machine
   verification + kernel solvability lemma, P-A1 narrowed".
10. [T2 EXEC] Hoffman 1967 FULL page-level read: PDF renderer absent
    (no poppler) -> text extraction via pypdf 6.14.2 (already present,
    no install) to UTF-8 file, read in full (7 pages, pp. 670-676).
    Page-verified facts of record: fields h_1..h_4 (one per flow PDE,
    Eq. 17) + g_i species (Eq. 15) + constants C_1 (isoperimetric,
    Eq. 12) and C_2 (streamline multiplier; h_1 = C_2 on AC, Eq. 29);
    interior multiplier PDEs Eqs. (35)-(39) with sources (42)-(44)/
    (55)-(57); hyperbolic (8+2n) system, characteristics = streamlines
    + Mach lines; multiplier compatibility Eqs. (49)-(51) (streamline)
    and (54) (Mach lines); terminal-characteristic data Eqs. (31),
    (33), (34) (g_i = 0 on BC); the FIFTH relation Eq. (32) NOT
    imposed (p. 673: five would OVERSPECIFY unless BC is a
    left-running Mach line — the control surface is selected by b.c.
    counting); endpoint/wall data Eqs. (60)-(65), constant-length
    case Eq. (68); E = y h_1 - (u y' - v) h_3 (Eq. 78 == unused
    Eq. 32) as the a-posteriori optimality check (p. 676).
11. [T2 DISCOVERY + R4] (a) SYMBOL CORRECTION of record: program docs
    paraphrased "lambda1..lambda4 (+lambda5)" — corrected to
    Hoffman's real notation in the draft §3.4(iv) and D3 §8.
    (b) Hoffman p. 673 = the 1967 ANCESTOR of Prop. A2 (surface
    selected by boundary-condition counting): recorded in the map.
    (c) Eq. (54) = the published adjoint transport relation along
    Mach lines -> NEW ROUTE OF RECORD for P-A1' (specialize to frozen
    homentropic, integrate to f2). Draft §3.4(iv) UPGRADED SCHEMA ->
    THEOREM* with the full component-map table (every row
    equation-numbered post-read); P-A2 marked DISCHARGED in the
    PENDING register (numeric half remains in P-A3/O3.2).
12. [T2 COMMIT] 36db818 "[F1/P-2] (rigore-T2): P-A2 DISCHARGED".
13. [T-LIT LAUNCH — user directive mid-session] User requested a
    study of ALL papers in GENO/literature ("variable inlet etc.,
    general variational theory, to evaluate against what we are
    developing"). Declared plan placement: [F1/D2-b0bis] corpus
    evaluation vs the averaged theory (D2 §b0 deepening). FIVE
    parallel background agents launched with structured briefs
    (identification, variational content incl. variable-inlet flag,
    NOVELTY-THREAT scan for multi-operating-point/averaged
    objectives with verbatim quotes, importable oracles, gamma
    status; radical-honesty citation rules; extraction via pypdf to
    scratchpad only): A1 = ADA455494 + BF00934730(JOTA) +
    Allman-Hoffman 1981; A2 = Scofield-Hoffman + JTH 1974 +
    Johnson-Boney 1975; A3 = HTH plug (fixed-inlet) + Veen + migdal;
    A4 = Rao 1961 spike/review + Rao-Beck 94-3264 + Rao et al.
    99-2584; A5 = NASA SP-8120/RP-1104 + Zucrow Vol.2 TOC + theses
    (skim). Synthesis doc to follow on completion.
14. [T3 EXEC] WROTE docs/rde_nozzle_P3_multipliers.md — P3 attack:
    THEOREM P3-S1 (shock-free S1 class, THEOREM* conditional on the
    declared P7 continuity): per-phase lambda2 exists and is UNIQUE
    (scalar Zowe-Kurcyusz CQ discharged by the Prop. A2 contraction
    <grad m, r+> = rho(u_n + c) > 0 — the rigor-session lemma doing
    double duty), equals the Lemma-A closed form -f2(lip data)
    (EOS-general), measurable (measurable data ∘ continuous shock-free
    S1 solution map — NO abstract selection theorem needed where the
    closed form lives: the correspondence is single-valued) and
    L^infinity(dmu) by the uniform margins (explicit bound
    W_max/sqrt(1-1/M_min^2)). Residues NAMED: R-P3.1 (across fitted
    shocks: inherits D2.5 conditional), R-P3.2 (beyond closed form:
    ZK + Kuratowski-Ryll-Nardzewski route, SCHEMA), R-P3.3 (interior
    field = P-2/G12). R4 same session: D3 §9 P3 row upgraded, M0 T7
    named-gap list updated. Falsifier written in the doc.
15. [T3 COMMIT] b5590f0 "[F1/P3] (rigore-T3): averaged multiplier gap
    ATTACKED - THEOREM* in shock-free S1".
16. [T-LIT RESULTS] All five agents returned (full reports in the
    task outputs; synthesized in step 18). Headlines: novelty sweep
    CLEAN corpus-wide (every objective is single-operating-point;
    nearest non-threats quoted verbatim); "variable inlet" RESOLVED =
    JTH 1974 variable inlet GEOMETRY (cowl-lip radius as variational
    DOF; ambient-as-output transversality) + Rao-1961 free lip — both
    geometric DOF at one state, no threat to the state-family claim;
    G2 oracle 2290 lbf VERIFIED VERBATIM at source (S-H 1971 AIAA J
    9(9), Table 2 diagonal, precision correction recorded); RaoPlug
    oracle verified at source (p. 95 + Table 3, C_F 1.5804);
    Sternin/Rao-Beck boundary page-verified (94-3264 Eq. 4, 99-2584
    Eq. 6); JOTA 1972 identity pinned + EXPLICIT EOS-general quote
    (p. 138); var-gamma optimization LEAD: Rao 1958 IAF Amsterdam
    (review ref. 21) — to acquire; misfile correction ADA455494 =
    Onofri RTO/AVT; Zucrow Vol. 2 unreadable in-machine (no text
    layer, declared hole); Veen Eq. (9) page correction (p. 1195).
17. [P-A1' DISCHARGE — user question on rotational scope answered in
    the same pass] Extended validation/pa1_symbolic_lemmaA.py with
    Part 3: (3a) multiplier-field PDEs DERIVED IN-HOUSE (only
    d rho/dV = -rho V/c^2; c^2 a free field => EOS-general) and the
    HTH closed-form pair (y rho v, u + K) verified to solve them for
    EVERY flow satisfying continuity + irrotationality (constraints
    substituted symbolically); (3b) terminal transversality on the
    family a(y rho v, u) + b(0,1) yields V cos(theta -/+ alpha)/cos
    alpha = -b/a = f2 EXACTLY, both families; (3c) corrupted-pair
    rejector PASS. Full suite PASS 19/19. One declared debug: sympy
    cannot differentiate wrt a compound expression — closure rules
    rewritten on field derivatives (chain rule); no math change.
    R4: draft §3.4(ii) STATUS UPGRADE paragraph (Prop. A3, THEOREM in
    scope; narrowing paragraph kept for audit trail), PENDING P-A1'
    marked DISCHARGED, D3 §8 upgraded. ROTATIONAL scope note written
    into the draft (user question): framework rotational-general
    (T0/T3-LemmaA/G-B/T7/(P) and the data contract carry rotational
    inflow; M0 VI.2 mandates rotational MOC); the two-field closed
    form is irrotational-homentropic; rotational transport = Hoffman
    four-field system + Kraiko school (identification survives at
    FIELD level; two-constant reduction does not).
18. [T-LIT SYNTHESIS] WROTE docs/rde_nozzle_lit_b0bis.md — corpus
    evaluation of record: verdicts V1 (novelty CLEAN, one external
    lead: van Meerbeeck EUCASS 2013), V2 (variable-inlet resolution),
    V3 (bridge anchors); corrections C1-C6; gamma-ledger additions
    (JOTA EOS-general quote; Rao 1958 IAF var-gamma lead; Migdal
    gamma(T) MOC; Johnson-Boney sensitivity); oracle registry
    O-b1..O-b7 (R5: scripts+rejectors required before adoption);
    program actions A1-A7.
19. [R3 CHIUSURA] Commits of record: T4/P-A1' = 86e6d6d, T-LIT =
    0fdbe7d. PROGRESS updated (ORA = S6 rigor closure with the class
    upgrades itemized; NEXT for S7 = Lemma B first + leads + the S5
    operational list; LOG entry S6). Memory updated
    (research-cycle-averaged-rao: S6 state). T4/T5 of the rigor
    prompt (feed-closure quantification; Lemma-B mesh-limit) NOT
    executed — declared, deferred to S7 (time). SESSION 6 CLOSED at
    step 19.

20. [POST-CLOSURE ADDENDUM — standing user assumption + R4] User
    declared the data scope: "il dato è sempre onda periodica, mai
    clapping o non periodico" and asked its effect on the corrector.
    Recorded as STANDING MODELING ASSUMPTION (monitor = T0
    thrust-trace flatness) and back-propagated to D3 §3 (C-T1 entry,
    PERIODIC-MODE SCOPING paragraph): (1) statistical stationarity
    reduces to the T0-covered case; (2) C-T1 re-scopes from two-scale
    time-homogenization to STEADY singular perturbation of the
    wave-frame BVP in the sweep parameter (anchor O4); (3) discrete
    spectrum -> Fredholm-on-the-circle, no secular terms/small
    divisors; (4) convergence regularity = harmonic decay, measurable
    at the contract audit. O(St) sweep error unchanged; C-T1 stays
    CONJECTURE in an easier class. Memory:
    periodic-wave-data-scope.md + MEMORY.md index.
21. [POST-CLOSURE ADDENDUM — algorithmic consequences, R4 to M0 VI]
    User asked whether these aspects MODIFY THE ALGORITHM. Answer of
    record written into M0 VI.4bis: skeleton unchanged (per-phase
    solve + per-phase adjoint + mu-assembly + TR-SQP + certificates);
    five choices PINNED DOWN: (i) periodic spectral quadrature in xi
    (trapezoid-on-the-circle, spectrally accurate for smooth periodic
    data) COMPOSED with the VI.4 switch-split rule; (ii) the O(St)
    corrector computed as ONE STEADY LINEARIZED SOLVE on the
    wave-frame anchor (sweep term as source) instead of primary
    unsteady simulation (O5 demoted to independent confirmation);
    (iii) EOS-general thermo backend mandatory, corner<->eps bijection
    FORBIDDEN as solver shortcut (enforce f2 = const actively; E4);
    (iv) per-phase adjoint = FIELD level (AD of the march); the
    two-constant closed form = oracle/initializer only (rotational
    data); NEW cheap per-phase certificates from this session's
    results: f2-drift and E-residual along the terminal
    characteristic, lambda2(xi) = -f2(lip) as closed-form multiplier
    initializer (P3); (v) robust CVaR/DRO layer OPTIONAL (out of
    baseline scope by the periodicity assumption; flatness monitor
    mandatory).
22. [POST-CLOSURE ADDENDUM — user clarification, AMENDMENT] "non
    farti condizionare dall'informazione che il segnale è sempre
    periodico, algoritmo sempre pienamente generale": M0 VI.4bis
    AMENDED — periodicity sets THEORY priorities and runtime
    opportunities, never structure: (i) general Gauss+switch-split
    quadrature is the BASELINE, circle rule = opportunistic upgrade
    gated by flatness+harmonic-decay certificates; (ii) both
    corrector routes live in the pipeline (steady sweep solve engaged
    when T0 certified; O5 always available); (v) CVaR/DRO layer part
    of the general architecture, idle (not absent) on certified-
    periodic data. (iii)-(iv) unconditional as before. Memory
    periodic-wave-data-scope.md amended with the clarification.
    NOTE: a concurrent S7 session is ACTIVE on this tree (commits
    1d762f8 OP-0-gamma purge, fb82846 PMM sweep 204/204 with top flag
    Kraiko-Osipov 1970; Lemma B draft in progress untracked) — third
    one-session-rule violation, reconciled so far without content
    conflicts; this session makes NO further edits to files S7 has
    open (P2_lemmaA.md left untouched).
