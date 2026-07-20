# PROGRESS S10 — 2026-07-17 — APERTURA FASE 2 (G0) + coda Fase 1 (P-1 §5-§7)

Total-order session log (CLAUDE.md R3; one numbered row per step /
file / commit). Session S10, branch `rde-nozzle-program`. Tasks:
T1 [F2/G0 formal decision incl. GENO cross-code criterion],
T2 [F1/P-1 §5-§7], T3 [leads, optional], T4/T5 optional.

1. OPENING (protocol S10+, S9 order). Read in order: project memory
   (MEMORY.md + gate-pre-esecuzione + python-env-cantera +
   research-cycle-averaged-rao + gamma-variable-generality +
   periodic-wave-data-scope); L0 = SCAFFOLD §1 (objective, layers,
   maintainer contract §3); docs/claims_registry.yaml (83 entries,
   index of the theory, lint group (xv)); D6 §5 gate states (G0
   INSTRUCTED, residual = Fortran toolchain; A1 started at spike
   level) + 90-day refresh; PROGRESS (ORA = S9 closure at 11163ba;
   NEXT S10 consolidated list 1-5). HEAD verified = 11163ba (expected
   S9 closure; git log -3 + status). NO foreign commits. RESTART
   POINT DECLARED: Fase 2 opening (G0 decision = D6 gate G0 / NEXT 1)
   + Fase 1 queue (P-1 §5-§7 = NEXT 2). ONE session active (S10).
2. TREE RECONCILIATION (declared): `data/q_mapping.json` +
   `data/q_mapping.md` carried a 2-line uncommitted diff = date-stamp
   regeneration (2026-07-16 -> 2026-07-17) from the S9 full-suite
   run (live examples rewrite their outputs; content otherwise
   identical). Action: restored via `git checkout -- data/q_mapping.*`
   (content-identical, reversible). Untracked GENO/ (independent repo,
   never committed) and validation/ADR_panel_2026-07-16.md (awaiting
   user ratification, untouched) left as-is.
3. PRE-EXECUTION GATE (standing directive, memory
   gate-pre-esecuzione):
   (A) PLAN ADHERENCE — T1 = [F2/G0]: D6 §5 gate G0 (STATUS
   2026-07-17 "INSTRUCTED, decision pending (NEXT 1)"; named residual
   = Fortran toolchain for the O3.4 flowfield criterion) + PROGRESS
   NEXT 1; user decision of record S5 (GENO stays Fortran; interop =
   explicit G0 criterion) honored: GENO is COMPILED, never modified,
   never committed. T2 = [F1/P-1 §5-§7]: PROGRESS NEXT 2 (citable:
   eps*_real carrier group (xii) [T-T7RED], equilibrium bracket
   [T-EQBR], registry IDs per SCAFFOLD §5). T3 = NEXT 3 (leads,
   raw-HTML method pin S7). T4 = A1-prep (D6 A1 content: gamma(T)
   backend; PM-generalized unit process is its first brick). T5 = L6
   candidate declared in registry (T-NSW scope: "declared L6
   candidate, none exists today"). All tasks placed; no orphan step.
   (B) UPSTREAM RIGOR AUDIT — re-verified at source: (1) sonic cap on
   BOTH routes: T-GB registry entry (cap mandatory, groups
   (viii)/(xi)) + M0 Prop. 7 GAMMA-PURGE INSTANCE (primary route
   EOS-general, closed forms demoted to oracles); (2) (**') always
   weighted, carried by eps*_real: T-T7RED (group (xii); falsifier =
   wrong-averaging rejector) + M0 REAL-ROUTE DIAGRAM INSTANCE;
   (3) winners = CLOSURES never hardware: T-OP11e scope (D3
   §10quater(5) semantics binding) — P-1 §7 will be SEMANTICS-FIRST;
   (4) (P) = pair (S*, delta) anchor: D-P / M0 D2.6 (DIR-ANCHOR);
   (5) GAMMA QUESTION: M0 VI.4bis(iii) re-read — EOS-general backend
   mandatory, gamma=const corner<->eps bijection FORBIDDEN as solver
   step (f2 = const enforced actively; E4/G2 oracle gates shortcuts);
   G0 decision text must state this as an ENGINE constraint, and the
   cross-code carrier must not use closed-form gamma=const steps as
   primary route (GENO itself is gamma-const TOC reference = declared
   oracle side, admissible: dual-code M0 VI.7). NO discrepancies
   found; no R4 pre-fix needed.
   (C) VERDICT: gate pre-esecuzione PASS (this step). Execution order:
   T1 -> T2 -> (T3/T4/T5 time permitting) -> R3 closure.
4. T1a TOOLCHAIN (declared, reversible; ZERO new installs). WSL Ubuntu
   22.04 already carries gfortran 11.4.0 + cmake 3.23.3 + make; LAPACK/
   BLAS (dgesv needed by GENO write_profile — link error found first
   build) resolved from the PRE-EXISTING host conda env
   /home/alessandro/miniconda3/envs/ct-env (libopenblas), passed as
   -DBLAS_LIBRARIES/-DLAPACK_LIBRARIES. Submodules: cloned via HTTPS
   with NON-PERSISTENT env override (GIT_CONFIG_* url.insteadOf; SSH
   URLs in .gitmodules); ONLY the OFF-build set (ORION, FLINT+OSlo,
   FiNeR+third_party incl. lagging PENF/StringiFor/fortran_tester
   repaired by fetch+checkout at pinned SHAs); the cantera/sundials
   nested tree SKIPPED (USE_CANTERA=OFF USE_SUNDIALS=OFF USE_TECIO=OFF).
   Build: cmake -B build_wsl, RELEASE => bin/GENO (848 KB) exit 0.
   GENO never modified, never committed; outputs gitignored (verified
   git status clean in GENO/).
5. T1b TOCNOZ RUN + CHECKSUM CONVENTION (read in-session, cited from
   the file itself). test/run_case.sh CASES/tocnoz bin/GENO: solver
   exit 0; NaN/Inf clean; performance sane (Cd 0.9820, Cf 1.7759,
   Isp 338.8619 s); profile 550 pts monotone divergent; area ratio OK.
   reference/checksums.md5 HEADER declares baselines toolchain-
   dependent (gfortran 7.5.0 SUSE host s3; N-36: regenerate on
   toolchain change) => md5 equality NOT expected cross-toolchain:
   printed-scalar files (performance/dimensions/thermo.dat) MATCH,
   full-precision field dumps differ (expected). Scientific check =
   VALUE-based. CONTOUR OF RECORD REPRODUCED: regenerated
   "profile 30.0.dat" vs committed ch16_ref/: max |dx|,|dy| = 1e-10
   (full printed precision); independent TOC validation: yt=1.0 at
   x=0, eps=29.95, maxtheta 37.41 deg.
6. T1c CROSS-CODE CARRIER (validation/g0_geno_crosscode.py, NEW).
   Method honesty trail (declared): (v1) naive i-1 stencil FAILED
   (geom residual 3.4e-2 — GENO overshoot rule + void rows); (v2)
   geometric foot search better (7.3e-3) but cross-field h-order fit
   ILL-POSED on a fixed grid (small-h cells cluster near-throat:
   apparent negative order — test misdesign, not disagreement);
   (v3) FINAL: per-cell truncation band DERIVED from the scheme
   (|R_trap - R_end| = O(h^3) ambiguity; K=4 Richardson): residual
   test (EOS-general, local a) 218/218 = 100% inside; literal
   reproduction "two feet -> new point" (user-mandate wording;
   declared gamma=const cell-mean energy closure) 207/218 = 95%
   inside. Negative controls: corrupted child/foot 100%->0%; wrong
   pairing 84x; feet discrimination >=10x. Full-sweep vs 153-column
   subsample medians IDENTICAL (2.21e-5/6.8e-5) — subsample declared.
   Runtime 14-26 s. VERDICT PASS. SCOPE DECLARED (user challenge
   in-session, honest): interior unit process ONLY, not the
   profile-generation machinery (no JAX-generated contour exists yet
   — that is A1 brick 1); scope written into carrier docstring,
   X-GENOXC registry entry, and G0 dossier §4.
7. T1d G0 DECISION (docs/rde_nozzle_G0_decision.md, NEW; registry
   +DIR-G0 +X-GENOXC, lint (xv) PASS 85 entries + triple rejector).
   DECIDED: JAX primary (fidelity 52/52 + O3.1; loop speed MEASURED
   STANDALONE: solve ~322 us, solve+adjoint ~327 us => grad/solve
   ~1.01 host-invariant, absolutes host-caveated per S9 lesson;
   interop criterion S5 NOW EXERCISED); Julia+Enzyme declared
   alternate (unbenchmarked, stated); GENO dual-code reference.
   Falsifier armed: assembled-A1 loop-speed flip. R4 SAME SESSION:
   M0 VI.7 addendum (G0 decision + dual-code exercise of record);
   D6 gate G0 INSTRUCTED->DECIDED + Phase A1 -> OPEN (first brick =
   gamma(T) unit process + X-GENOXC standing regression).
8. COMMIT T1 = bfd0063 (path-limited: carrier + dossier + registry +
   M0 + D6; git log -3 + status BEFORE: HEAD 11163ba, no
   interleaving; post-commit hunk audit CLEAN — 5 hunks, all mine).
   Session log and PROGRESS stay for the closure commit. USER
   CERTAINTY AUDIT delivered in-chat (what is rejector-backed vs
   declared-conditional); pending user answer on S11 priority
   (A1 brick 1 vs other) recorded under NEXT.
9. T2 P-1 SECTIONS 5-7 FULL TEXT OF RECORD
   (docs/rde_nozzle_P1_sections_5_7.md, NEW): §5 averaged system
   (blocks (a)(b)(c), (**') factorization, BOXED WARNING naive
   average, quasi-1D reduction with EOS-general carrier eps*_real
   [T-T7RED] + closed form demoted to oracle + VI.4bis(iii) pin
   stated, P-2 pointer); §6 ceiling [T-GB] + sonic cap (g=1.15
   counterexample, 4 subcritical rejections) + ladder + PURGE DELTA
   -4.4..-7.9% + EQUILIBRIUM BRACKET +6.3..+7.0% [T-EQBR]; §7
   SEMANTICS-FIRST (D3 10quater(5) verbatim), (P) block, statements
   (1)-(4), artifact warning, REAL-ROUTE INSTANCE §7.5bis
   (eps*_real 3.49-3.52, knee_real 10.38 < ~12.9, M1 EOS-general 41
   cells incl. 11 subcritical), premium_bound, multiplicity, vacuum.
   Rules (a)-(e) audit line per subsection; claims by registry ID;
   CLASS REFRESH vs skeleton DECLARED in header (SCHEMA -> THEOREM*
   per S6/S8 upgrades); novelty wording CONDITIONAL (Kraiko-Osipov).
   Coherence grep PASS (winner/lemma/naive greps logged); lint (xv)
   PASS post-edit. Skeleton DRAFT TEXT STATUS updated.
10. COMMIT T2 = 570b38c (path-limited: sections_5_7 + skeleton; HEAD
    bfd0063 verified before, no interleaving; diff stat 2 files as
    expected).
11. T3 LEADS (both closed at source; raw-HTML/raw-PDF method of
    record, never the summarizer — S7 pin honored):
    (a) Rao 1958 "IAF Amsterdam" = G. V. R. Rao, "Contoured Rocket
    Nozzles", Proc. IXth Int. Astronautical Congress (Amsterdam
    1958), Springer Vienna, DOI 10.1007/978-3-7091-4745-0_18;
    abstract extracted from RAW Springer HTML (curl; phrase counts
    verified: "varying gas properties" x2, "equilibrium" x5):
    var-gamma thrust optimization is Rao himself, 1958, SINGLE steady
    state => mandatory citation in the P-1/P-2 gamma lineage, novelty
    of the CYCLE-AVERAGED composition untouched; full text paywalled
    (G5-queue residual declared, abstract-verified citation only).
    (b) van Meerbeeck-Zandbergen-Souverein, 5th EUCASS 2013: FULL
    TEXT read in-house (15-page PDF, pypdf): point-design TOP
    procedure (MMH-NTO, sea level, TDK); keyword counts of record
    average/trajectory/weighted/flight = 0/0/0/0 => NO averaged
    functional, G14 HOLDS, lead CLOSED. R4: both verdicts written
    into lit_b0bis (V1) + (A7 STATUS). COMMIT T3 = 0fb6a21
    (path-limited, lit_b0bis only).
12. SUITE COMPLETA: 16/16 groups PASS exit 0 in 213 s (healthy host,
    no caveat; incl. (xiii) 12.1 s, (xiv) 31.8 s rigor tier, (xv)
    lint with triple seeded rejector, (v+) live examples 99.2 s).
    Output to file (validation/suite_S10_full.log, ephemera — verdict
    recorded here, file removed at close per S9 cleanup precedent).
    Live examples regenerated data/q_mapping.* datestamps AGAIN
    (2026-07-16 -> 2026-07-20, 2-line diff, content-identical):
    restored via git checkout, second occurrence this session,
    declared both times.
13. DEVIAZIONI DICHIARATE (session-level): T4 (PM-generalized brick)
    and T5 (T-NSW symbolic carrier) NOT executed — priority
    T1>T2>T3 honored, both remain optional NEXT items (T4 folds
    naturally into A1 brick 1). Session dates: opened 2026-07-17
    (prompt date), closed 2026-07-20 (calendar gap across user
    pauses; single session, no concurrency at any of the three
    pre-commit checks). Model switch mid-session (user command)
    declared: opus -> fable-5 at the certainty-audit step.
14. CHIUSURA R3: PROGRESS updated (ORA S10 + NEXT S11 + BLOCCATO +
    LOG entry); INDEX.md + S10 row; memory updated
    (research-cycle-averaged-rao: S10 state appended); closure
    commit = see PROGRESS/git. Log CLOSED at total order, step 14.
