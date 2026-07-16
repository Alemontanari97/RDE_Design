# D2 §b0-bis — Full-corpus evaluation of GENO/literature against the
# averaged variational theory (five-agent primary-source pass)

Status: EVALUATION OF RECORD (2026-07-16, rigor session, [F1/D2-b0bis];
user directive: "study all papers in GENO/literature — some do general
variational theory (variable inlet etc.), evaluate against what we are
developing"). Method: five parallel agents, one structured brief
(identification / variational content incl. variable-inlet flag /
NOVELTY-THREAT scan for multi-operating-point or averaged objectives
with verbatim quotes / importable oracles / gamma status; radical
honesty on citations — no equation number cited unread). This file is
the synthesis; the full agent reports live in the session record
(validation/PROGRESS_2026-07-16_rigore_PA.md step 13 + task outputs).
Supersedes nothing; DEEPENS D2 §b0 (which remains the corpus map).

------------------------------------------------------------------------------
## 1. HEADLINE VERDICTS

(V1) NOVELTY SWEEP: CLEAN ON THE WHOLE IN-HOUSE CORPUS. No paper in
GENO/literature formulates an averaged, weighted, multi-operating-
point, or ensemble VARIATIONAL nozzle objective. Nearest non-threats,
each quoted in the agent reports: Rao 1961 review p. 1488 (choose ONE
fixed area ratio "taking into consideration the performance
requirements over the entire trajectory" — parameter selection, no
functional); AIAA 99-2584 p. 5 (sea-level "other design factors must
be considered" — deferral, no objective); Veen 1974 (a CATALOGUE of
single-point optima indexed by (length, pa) — select-after, never
integrate-over); S-H 1971 cross-analysis matrices (design-vs-analysis
sensitivity, never a combined objective); Onofri RTO/AVT (altitude
behavior EVALUATED for fixed designs); theses (trajectory-mean CF
mentioned qualitatively, never optimized). The cycle-averaged claim's
query bound now rests on a PAGE-LEVEL pass of the entire in-house
corpus. External lead to close (the only one surfaced): van
Meerbeeck-Zandbergen-Souverein, EUCASS 2013 (Viviano ref. [23]) —
parametric altitude/weight/size optimization of TOP parabolas; by
title parametric multi-criterion, not a variational averaged
functional; VERIFY AT SOURCE before P-1 submission.

(V2) "VARIABLE INLET", RESOLVED. The corpus contains exactly two
inlet-freedom notions, NEITHER of which is variable inlet STATES:
 (a) Johnson-Thompson-Hoffman, Computers & Fluids 2:173 (1974)
     "Design of Maximum Thrust Plug Nozzles with VARIABLE INLET
     GEOMETRY": the cowl-lip radius y_E and plug base radius y_F are
     VARIATIONAL unknowns (three-DOF Bolza problem; lip transversality
     Eq. (25): lambda1_E = -(p - pa)/(rho u); notable consequence:
     the ambient pressure for which the design is optimal is an
     OUTPUT). Fixed-inlet companion: HTH AIAA J 9(8):1581 (1971)
     (inlet DOFs y_E, beta recovered by a 21-run parametric sweep).
 (b) Rao 1961 spike (Planet. Space Sci. 4:92): free lip R_E and free
     base R_D with only L fixed — the free-boundary (T4-side) brick.
Both freedoms are GEOMETRIC DOF at a single operating state. Our
program's variable object is the INFLOW STATE FAMILY s(xi) with a
measure — untouched by the corpus. No threat; both papers become
mandatory citations for the (P) admissible-set/sector discussion.

(V3) THE BRIDGE LEMMA GAINED ITS PUBLISHED ANCHORS. The literature
pass found, in-house, the exact objects P-2 needed:
 - HTH 1971 p. 1583: closed-form multiplier pair (y rho V sin theta,
   V cos theta + const) solving the multiplier PDEs for ANY admissible
   flow; Rao's f2 recovered via the terminal condition (their
   Eqs. (20)/(23)-(26)) — consumed by Prop. A3 (P-A1' discharge).
 - JOTA 10(3):133 (1972) (Hoffman-Scofield-Thompson, "Thrust Nozzle
   Optimization Including Boundary-Layer Effects" — identity of
   record for the BF00934730 file): multiplier compatibility along
   Mach lines Eqs. (21)-(23); terminal residual E = lambda1 +
   lambda2 y rho cot(alpha) (Eqs. (26)/(34)); EXPLICIT EOS-generality
   statement p. 138 ("these assumptions are not required in the
   development of the design equations, and other equations of state
   could have been used as well") — primary-source support for the
   standing gamma directive; and the historical point that
   Guderley-Armitage POSTULATED the characteristic surface while
   H-S-T DERIVED it from transversality (p. 142).
 - S-H 1971 + JTH 1974: same constants-vs-fields split (fields for
   PDEs, functions on wall constraints, ONE constant per isoperimetric
   constraint) — the Lemma-A structure attested three more times.
 - Lexical trap for P-2 §3 (footnote): AIAA 94-3264 says "variational
   calculus with ADJOINT constraints" meaning ADJOINED isoperimetric
   constraints, not the adjoint PDE.

------------------------------------------------------------------------------
## 2. CORRECTIONS OF RECORD (propagate where cited)

 C1 Veen Eq. (9) (base-pressure model p_b = 0.846 p_H / M_H^1.3) is
    on p. 1195, NOT p. 1194 (corner Eq. (8) is p. 1194).
 C2 ADA455494.pdf is NOT Guderley-Armitage: it is Onofri (chair),
    "Plug Nozzles: Summary of Flow Features and Engine Performance",
    AIAA 2002-0584 / RTO-TR-AVT-007-V1 (2006). The Guderley-Armitage
    chapter (Miele ed., 1965) is NOT in GENO/literature — if page-
    level verification is ever needed, it must be sourced (G5-adjacent
    library item, LOW priority: its content is superseded by the
    Purdue-school papers we hold).
 C3 S-H 1971 identification pinned: AIAA Journal 9(9):1824-1832,
    Sept. 1971 (not JOTA); the G2 oracle "Table 2 Case 1 frozen
    2290 lbf" is VERIFIED VERBATIM with the precision that 2290 is
    the frozen-contour/frozen-flow DIAGONAL entry, shared at 4-digit
    resolution by the 1e18/1e17 contours under frozen analysis; full
    Case-1 spec quoted in the agent report. The Case-1 frozen mixture
    is effectively gamma = const (constant per-species Cp) — the
    right shape for the E4/G2 gate.
 C4 RaoPlug oracle pinned at source: values live in Rao 1961 spike
    p. 95 TEXT and Table 3 (C_F = 1.5804 4-digit; R_D/R_E = 0.137;
    ideal-length discrepancy of record: 2.428 text vs 2.433 Table 3 —
    quote both, do not reconcile silently); "Table 1" is the CONTOUR
    table (first rows OCR-damaged in our copy; better render needed
    before contour-level oracle use). Second case: eps = 10.69,
    M_E = 3.2, theta_E = -6 deg, C_F = 1.7269.
 C5 Sternin/Rao-Beck boundary page-verified: AIAA 94-3264 Eq. (4)
    (with Sternin 1962 credited) and AIAA 99-2584 Eq. (6) (clean form;
    real-gas extension asserted for equilibrium/frozen chemistry).
 C6 Hoffman-1967 symbol correction (already of record from T2):
    fields h_1..h_4 + g_i, constants C_1, C_2 — not "lambda1..5".

------------------------------------------------------------------------------
## 3. GAMMA LEDGER ADDITIONS (standing directive)

 - JOTA 1972 p. 138: design equations EXPLICITLY EOS-general (quote
   above) — classical primary support for the architecture inversion.
 - Rao 1961 review p. 1490: a VARIABLE-GAMMA OPTIMIZATION PRECEDENT
   is claimed — "The method of optimizing nozzle contours for the
   case of nonconstant gamma was treated in (21)" = Rao, "Contoured
   Rocket Nozzles", Proc. 9th IAF Congress, Amsterdam, 1958. LEAD OF
   RECORD: not in GENO/literature; acquire/verify before P-2
   submission (affects the novelty wording of the gamma-general
   presentation, not the certificates). Also ref. 19 observation:
   contours near-insensitive to gamma at fixed (eps, L), C_F strongly
   gamma-dependent.
 - AIAA 99-2584: control-surface machinery + boundary function
   carried to equilibrium/frozen chemistry in engineering practice.
 - Migdal 1972 (J. Spacecraft 9(1):3-6): gamma(T) inside a CLASSICAL
   MOC design code (non-variational) — supports the E4 boundary
   statement (gamma(T) MOC standard since 1972; the VARIATIONAL
   closed forms stayed gamma = const).
 - Johnson-Boney 1975 (NASA Langley): contours strongly gamma-
   sensitive (2-D length ratio ~80 across gamma 1.1->1.667 at fixed
   exit M; axisymmetric ~11) — quantitative why-it-matters.

------------------------------------------------------------------------------
## 4. ORACLE REGISTRY ADDITIONS (candidates; R5: each needs a
##    committed script + rejector before any number becomes "ours")

 O-b1 S-H 1971 Table 2 diagonal (2290 lbf frozen; 2393 equil; 2343
      nonequil 1e18) + Case-1 full spec; Tables 3/4/7 rows quoted in
      the agent report (scale-x9 check; hydrogen case 971.4 lbf).
 O-b2 JOTA 1972 gamma=1.2 case: relaxation 5846.6 lbf vs Rao 5846.4
      lbf, M_e 4.0 vs 4.0015, theta_e 11.8966 vs 11.8931 deg — a
      dual-route classical pair for G1-class tests.
 O-b3 HTH 1971 Tables 1-4 (21-run parametric grid 32,699-32,881 lbf;
      optimum contour 20 stations; Rao-method contour; alternate-base
      contour; cross-method 34,373 vs 34,375 lbf on a shared start
      line = 0.006 percent; start-line sensitivity ~8 percent; base-
      model sensitivity numbers). One Table-3 theta entry visibly
      OCR-corrupt (-12.27169) — re-render before use.
 O-b4 Veen 1974 Tables 1-3 (plug-length ladder; shroud lengths; C_F
      1.4230-1.5888) + full spec (gamma 1.4, PR 43.23, y_u 10.0,
      y_l 8.5, theta_i -15 deg); caveat: base thrust excluded for
      Migdal comparability.
 O-b5 Rao-Beck 94-3264 (gamma 1.4): optimum eps=500 C_Fv 1.7591; DEF
      1.7596; short DEF 1.7538; ideal 1.7636; conical 1.7338; the
      22-percent-length / 0.3-percent-loss headline.
 O-b6 JTH 1974: perfect-plug closed forms Eqs. (33)-(36); 99.6 / 97.6
      percent-of-ideal at 50 / 20 percent length (gamma 1.23,
      P0/pa = 34); baseline spec (500 psia / 6000 R / 148.077 lbm/s);
      p_b model sensitivity (3 percent contribution, +/-10 percent
      p_b -> +/-0.3 percent thrust); declared failure boundary
      (pa -> 0, L/L_P < 20 percent).
 O-b7 Theses (regression-grade, not literature-canonical): Viviano
      Tables 3.1/3.3/3.4/3.5 (ideal eps=40 CF_vac 1.874; TOC L/rt
      14.6 eps 50.13 CF 1.856; validity limits theta* 26.4 deg,
      M* 3.67 at M_E 3.5 gamma 1.23; DEF vs TIC pair); Valeriani
      Table 5.1 (reproduces BOTH Rao-1961 spike cases incl. C_F
      1.5804 / 1.7269), Tables 3.1/3.2/7.x (M10 case).

------------------------------------------------------------------------------
## 5. IMPORTABLE THEORY / PROGRAM ACTIONS

 A1 Prop. A3 consumed HTH+JOTA (done this session; Lemma A (ii) now
    THEOREM in scope). Cite HTH pp. 1583-84 + JOTA Eqs. (21)-(26) in
    P-2 §3 next to Hoffman 1967.
 A2 (P)/sector discussion: cite JTH 1974 (variable inlet GEOMETRY as
    honest classical precedent for geometric DOF in the admissible
    set; ambient-as-output transversality) and Migdal's max-area-ratio
    feasibility boundary of the two-wall sector (constraint on A_gen's
    shrouded sector); Veen's shroud-existence degeneration = classical
    single-point echo of topology-as-output (OP-11 remark).
 A3 PB-2 base-pressure closures: Onofri RTO/AVT wake-transition model
    + base-pressure catalogue; HTH/JTH p_b sensitivity numbers as the
    declared-model risk budget precedent; SP-8120 p. 20 quote ("A
    method for directly optimizing truncated aerospike or plug
    nozzles has not been developed... necessary to assume that the
    base pressure is zero", 1976) — historical support for PB-2's
    "first genuinely averaged shape problem" positioning.
 A4 M3 (unimodality) evidence: Allman-Hoffman 1981 (2-DOF direct
    search: unique global max, found efficiently; parametrization
    penalty grows off-vacuum) — cite in the globality-mechanism
    discussion.
 A5 P-1 §1 negative citations (field practice is single-point):
    SP-8120, RP-1104, Onofri — all confirm design-at-one-point +
    off-design evaluation.
 A6 DEF as licensed shock-full exit (Rao-Beck/Shmyglevskii): the
    classical precedent for DELIBERATELY leaving the shock-free class
    under a hard length constraint — relevant to S1-class boundary
    discussion and to sector tournament candidates.
 A7 LEADS TO CLOSE (query-bounded discipline): Rao 1958 IAF Amsterdam
    (var-gamma optimization precedent — HIGH priority for the gamma
    narrative); van Meerbeeck EUCASS 2013 (altitude-parametric TOP);
    Guderley-Armitage 1965 chapter (LOW, superseded); Zucrow-Hoffman
    Vol. 2 remains UNREAD in-machine (image-only scan, no text layer
    - declared hole; its content reaches us via the theses and the
    Purdue papers).

Gamma status of this document: reporting layer; every imported
closed-form result carries the gamma tag noted per item.
