# INVENTORY — seg7-literature (S-ORDINE Phase 1, 2026-08-13)

Reader: seg7-literature. Segment lists (authoritative):
`seg7_literature.txt` (13) + `seg7_parent_root_files.txt` (47) +
`seg7_geno_pdfs.txt` (77) = **137 files accounted**.

METHOD (declared): per brief, NO PDF was opened. The record is built
from what the repo already says: ADVISORY_rde_choking_2026-08-11.md
(5 papers READ-INTEGRAL, page-anchored), ADVISORY_generality_litmap_
2026-08-12.md (24 PDFs read by 8 reader agents, refuter-passed),
docs/rde_nozzle_literature_map.md (acquisitions register with
page-verify statuses), memory `generality-litmap-review`, parent-dir
prose (CONTINUATION_PROMPT.md and VALIDATION.md READ IN FULL here),
and an md5 dedup check on the parent txt extracts. UNREAD papers are
registered as UNREAD — no faked summaries.

COVERAGE ACCOUNTING: read-integral this session = 2 (the two parent
.md prose files). Classified-without-integral-read = 135, with
declared reasons per class: literature-pdf (analysis record lives in
the named advisories/litmap — the whole point of this inventory);
pptx/zip/png (binary assets); txt extracts (derived from PDFs,
head-peeked + hashed); hash lists (head-peeked, derived git
artifacts); vendor-docs (third-party library manuals, out of research
scope); GENO figures (derived plot outputs of an independent repo).

This file is the direct source for `docs/literature_registry.yaml`
(T2 deliverable, D6/S-ORDINE contract §3 Fase 1(vii)).

---

## ROOT A — repo `literature/` (13 files)

All class **literature-pdf**, all STATUS-AUTHORITY **OF-RECORD**
(primary sources; the ANALYSES of record live in the cited anchors —
none of these files is superseded/consumed). Cross-root dedup: none
of the 13 duplicates any Root B or Root C file.

### A1. `literature/0021-8928%2870%2990164-4.pdf`
- IDENTITY: Kraiko-Osipov, PMM/JAMM 34(6):1005-1013 (1970) —
  trajectory-averaged variational nozzle contouring.
- CONTENT OF RECORD: time-integrated WEIGHTED wall condition (3.2)
  with endogenous weight W(t)=lambda2·k/m from the trajectory
  adjoint; multiplier fields on characteristics (3.6)-(3.10); §4
  collapse case (invariant inlet → classical family with averaged
  weight, the T-T3 trajectory analogue); §5 second collapse (short
  nozzle, T4 stationarity ancestor, F-KO5). Structural
  NON-containment of the coupled problem ((P)'s mu exogenous),
  litmap §3.12/§6(g). MANDATORY CITATION P-1/P-2.
- WHERE READ: FULL text read + adjudicated S13 2026-07-22
  (literature_map "KRAIKO-OSIPOV ADJUDICATION" block); re-read at
  page level, litmap §3.12. STATUS: **READ-INTEGRAL**.
- PLAN-ANCHOR: T7 precedent note / T-T7FS; D2 litmap b0; P-1/P-2
  mandatory cite; litmap duty D-D (G6-vs-K-O annotation).
- UNIQUE-AT-RISK: none (adjudication lives in literature_map + litmap
  advisory).

### A2. `literature/0041-5553%2880%2990091-9.pdf`
- IDENTITY: Shmyglevskii, "Variational Problems of Gas Dynamics",
  USSR CMMP 20(5):113-127 (issue 1980, transl. printed 1981) — THE
  Rao-Beck Ref. 4, identity page-verified twice (litmap §7.1(ii) +
  refuter).
- CONTENT OF RECORD: Route A/B taxonomy (litmap §2); rejection
  condition (6) (candidate identity with the (G)/Lambda-form
  boundary, [X-VMON]-grid falsifier, owner F4b — QUESTION, never
  cite as fact); SECOND SCHEME (shock+contact outside determining
  triangle, corner conditions (7)) + Fig. 4 completeness map = the
  classical optimality claim for the discontinuous regime the O3
  obligation needs; Naumova-Shmyglevskii 1967 swirl precedent;
  3-D Route-B existence (Borisov-Mikhailov).
- WHERE READ: READ IN FULL, litmap session 2026-08-12 (§3.13, §7.1,
  §7.2). STATUS: **READ-INTEGRAL**.
- PLAN-ANCHOR: O3 ledger obligation (gate moved ACQUIRE →
  ADJUDICATE, duty D-A); F1b/O3 adjudication (D-C); F4b lemma D-B.
- UNIQUE-AT-RISK: none (all findings in litmap advisory §7.1-7.3).

### A3. `literature/080727464.pdf`
- IDENTITY: Giles-Ulbrich, SINUM 48(3):882-904 (2010), Part 1 —
  convergence of linearized/adjoint approximations with shocks.
- CONTENT OF RECORD: eps=h^alpha interior-smearing repair; p.884
  counterexample lineage [Gil03]; p.886 adjoint interior BC at the
  shock; capturing-vs-fitting contrast explicit (literature_map
  acquisitions register).
- WHERE READ: ACQUIRED + PAGE-VERIFIED (S12/S13, literature_map);
  cited in S-SPEED audit context ("Giles-Ulbrich x2 on disk",
  choking advisory §5). STATUS: **READ-PARTIAL** (page-verified key
  content; no full-read claim of record).
- PLAN-ANCHOR: F4b ENTRY condition (D6 line ~236: "F2 exit +
  Giles-Ulbrich SINUM 2010 x2 + Lozano 2019"); captured-shock-
  adjoint rejection conditional (plan_v3_panel).
- UNIQUE-AT-RISK: none.

### A4. `literature/09078078x.pdf`
- IDENTITY: Giles-Ulbrich, SINUM 48(3):905-921 (2010), Part 2.
- CONTENT OF RECORD: adjoint convergence theorem proper (2/3<alpha<1);
  fixed-points-across-shock discrete adjoint converges to a WRONG
  value (p.907); p.910 strong negative for ANY fixed-stencil
  discretization; "the trap is a theorem" fully page-verified on
  both parts (literature_map register).
- WHERE READ: ACQUIRED + PAGE-VERIFIED S13-coda 2026-07-22.
  STATUS: **READ-PARTIAL** (page-verified theorem content).
- PLAN-ANCHOR: F4b entry; claims_verdict "Corollary 3 / oracle
  culture" row (adjoint-consistency trap = theorem).
- UNIQUE-AT-RISK: none.

### A5. `literature/aerospace-12-00494-v2 (1).pdf`
- IDENTITY: Lozano-Ponsin, Aerospace 12(6):494 (2025) — 2-D analytic
  Euler adjoints with characteristic structure (the resolved "MDPI
  2025 hit", G14 bank B3).
- CONTENT OF RECORD: det-transpose argument = our Prop. A1; adjoint
  compatibility Eqs. (30)/(31) = supplementary O3.3 bench rows
  (F-O33BENCH); adjoint Riemann invariants (32)-(34) constant-flow-
  only except R1^psi; shocks excluded from scope; all 42 references
  verified S14 — ZERO cites of Rao/Guderley/Kraiko → G14 "both
  banks, no bridge" page-verified at the B3 end.
- WHERE READ: ACQUIRED + PAGE-VERIFIED through §2 + full reference
  list (S13/S14, literature_map). STATUS: **READ-PARTIAL**.
- PLAN-ANCHOR: G14/P2 identification lemma; O3.3 oracle bench of
  record; D2 b2.
- UNIQUE-AT-RISK: none.

### A6. `literature/aerospace-12-00502.pdf`
- IDENTITY: Gonzalez-Viana, Sastre, Martin, Velazquez, Aerospace
  12:502 (2025) — single-cycle H2-air PDE nozzle optimization
  (quasi-1D unsteady reactive Euler + HOSVD surrogate + GA).
- CONTENT OF RECORD: optimum always divergent with SMALL area ratio
  (1.13-1.31 of 15 available), length bound ACTIVE; time-averaged
  exit pressure 1.4-2.1 bar >> Pa; "classical nozzle optimization
  criterion is no longer valid" (p.14); three-way attribution of
  record S12 (constraints + MEASURE effects rung-2 + genuinely
  unsteady residue → O5 anchor).
- WHERE READ: FULL-TEXT READ S12 2026-07-21 (literature_map) AND
  17/17 pp at the choking census 2026-08-11 (choking advisory
  header + §1(e)). STATUS: **READ-INTEGRAL** (twice).
- PLAN-ANCHOR: D6 Phase A2 benchmark row; O5-lite bench class
  (F5b); T3-QS severity ranking.
- UNIQUE-AT-RISK: none.

### A7. `literature/dan25254.pdf`
- IDENTITY: Sternin, DAN SSSR 139(2):335-336 (1961) — Russian
  ORIGINAL of the boundary paper (the 1962 Sov. Phys. Dokl. is its
  translation); identity page-verified twice (litmap §7.1(i) +
  refuter). NOTE: the D2 b0 "Sternin 1962 in GENO/literature"
  source line is a PHANTOM (refuter finding, duty D-D) — the file
  lives HERE, not in GENO.
- CONTENT OF RECORD: dy/dalpha=0 on the pencil characteristic;
  explicit gamma=const boundary Eq. (4) (scan-transcription
  cautions declared); "shockless solutions impossible left of C0"
  — the classical ancestor of the A_t certifiability boundary and
  the Rao-Beck cite.
- WHERE READ: READ IN FULL (both pages), litmap 2026-08-12.
  STATUS: **READ-INTEGRAL**.
- PLAN-ANCHOR: O3 obligation (D-A); S4 Lambda-form provenance.
- UNIQUE-AT-RISK: none.

### A8. `literature/lozano-2018-singular-and-discontinuous-solutions-of-the-adjoint-euler-equations.pdf`
- IDENTITY: Lozano, AIAA J 56(11):4437-4452 (2018),
  doi:10.2514/1.J056523.
- CONTENT OF RECORD: objective-dependent taxonomy of adjoint
  shock/sonic behavior (lift adjoint continuous at shock + log
  singularity at sonic throat; nonlinear-in-p cost → discontinuous
  derivatives + shock-foot discontinuity; entropy adjoint jumps);
  2-D adjoint shock equations (Baeza lineage); oblique-shock case
  DECLARED OPEN in 2018.
- WHERE READ: ACQUIRED + PAGE-VERIFIED S14 (literature_map).
  STATUS: **READ-PARTIAL**.
- PLAN-ANCHOR: F4b fitted-front adjoint jump line; transonic-
  degeneracy confinement (claims_verdict).
- UNIQUE-AT-RISK: none.

### A9. `literature/lozano-2019-watch-your-adjoints-lack-of-mesh-convergence-in-inviscid-adjoint-solutions.pdf`
- IDENTITY: Lozano, "Watch Your Adjoints!", AIAA J 57(9):3991-4006
  (2019).
- CONTENT OF RECORD: mesh-divergence locus CORRECTED of record —
  wall/trailing-edge-driven, NOT the shock (Lemma B §4.4 fixed S13).
- WHERE READ: ACQUIRED + PAGE-VERIFIED, S13. STATUS:
  **READ-PARTIAL**.
- PLAN-ANCHOR: F4b entry trio (D6 ~236); Lemma B hygiene.
- UNIQUE-AT-RISK: none.

### A10. `literature/morris-2012-numerical-modeling-of-single-pulse-gasdynamics-and-performance-of-pulse-detonation-rocket-engines.pdf`
- IDENTITY: Morris, JPP 21(3):527-538 (2005), doi:10.2514/1.7875
  (filename "2012" = repository re-issue).
- CONTENT OF RECORD: METHOD CORRECTION of record (S14): NOT MOC —
  quasi-1D unsteady finite-rate FV-CFD (Yee TVD + Roe + Strang,
  9-species H2/O2); optimized-CD gains +53-57% / +20-21% / +10% by
  pressure-ratio band; machine-checkable Table 2; beneficial early
  blowdown cutoff. Implementation basis of record for the O5-lite
  bench exit-BC.
- WHERE READ: ACQUIRED + PAGE-VERIFIED S14 (literature_map).
  STATUS: **READ-PARTIAL** (page-verified incl. method correction).
- PLAN-ANCHOR: F5b O5-lite single-cycle PDE falsification bench
  (D6 ~634, ~993).
- UNIQUE-AT-RISK: none.

### A11. `literature/owens-hanson-2012-single-cycle-unsteady-nozzle-phenomena-in-pulse-detonation-engines.pdf`
- IDENTITY: Owens-Hanson, JPP 23(2):325-337 (2007),
  doi:10.2514/1.22415.
- CONTENT OF RECORD: 11 distinct single-cycle unsteady nozzle
  phenomena catalogued; quasi-1D inadequate for CONVERGING sections;
  PRECEDENT DUTY for P-1: 2007 empirical precursor of the
  mean-pressure design rule at eps level ("optimal expansion ratio
  well-predicted by isentropic theory + time-averaged head-wall
  pressure") — cite next to S-H in the T3 practice line.
- WHERE READ: ACQUIRED + PAGE-VERIFIED S14. STATUS: **READ-PARTIAL**.
- PLAN-ANCHOR: F5b bench anchors; P-1 §T3 practice-explanation.
- UNIQUE-AT-RISK: none.

### A12. `literature/s0045-7930%2801%2900072-x.pdf`
- IDENTITY: Moretti, Computers & Fluids 31:719-723 (2002) —
  shock-fitting retrospective (non-variational).
- CONTENT OF RECORD: F4b fitted-front methodological support
  (litmap §1, §3.15).
- WHERE READ: litmap 2026-08-12, triaged depth (non-variational
  class). STATUS: **READ-PARTIAL**.
- PLAN-ANCHOR: F4b (fitted fronts); Moretti/Salas conditional
  (plan_v3_panel acquisition row).
- UNIQUE-AT-RISK: none.

### A13. `literature/single-cycle-impulse-from-detonation-tubes-with-nozzles.pdf`
- IDENTITY: Cooper & Shepherd, JPP 24(1):81-87 (2008),
  doi:10.2514/1.30192.
- CONTENT OF RECORD: +72% (100 kPa, unsteady tamper regime) / +43%
  (1.4 kPa, quasi-steady from AVERAGE upstream pressure) verbatim;
  nozzle-dependent transition pressure 5.2 kPa; nozzle startup
  6-12% of cycle — N5/P4 relevant; unsteady/quasi-steady
  competition anchor for gate G3.
- WHERE READ: ACQUIRED + PAGE-VERIFIED S13 2026-07-22
  (literature_map). STATUS: **READ-PARTIAL** (page-verified).
- PLAN-ANCHOR: F5b/G3 (D6 ~629 "Cooper-Shepherd competition data").
- UNIQUE-AT-RISK: none.

### Root A — WANTED (missing, NOT in the 137 count; downstream duties)
- **AIAA 2019-0197** (Harroun 2019) — SOLE remaining fetch of the
  choking census (choking advisory §3/§5); needed before any
  reattribution of the "near-perfect time-averaged expansion"
  phrase. Owner: acquisition register / next lit window.
- Peter-Desideri PoF 34:086113 (2022), Ancourt-Peter-Atinault
  Aerospace 10:797 (2023), Lozano-Ponsin Aerospace 10:267 (2023) —
  MANDATORY-CITE for P-2, ACQUISITION-PENDING (literature_map
  F-PETERANC: no content claim until page-verified).
- Breitkopf-Ulbrich arXiv:2509.22076 (D25U leads); Tillyaeva 1975
  (N6-2 novelty bound, unacquired); Naumova-Shmyglevskii 1967
  (swirl precedent, cited via Shmyglevskii 1980 only).

---

## ROOT B — parent dir "Presentazione RDE CVA/" top-level (47 files)

Two projects share this root: the COMPLETED lecture project
("Lezione Detonazione & RDE", deliverable Presentazione_CVA.pptx,
closure record VALIDATION.md) and the research program (repo
rde-lecture-code born as its "repo per studenti" deliverable).
PLAN-ANCHOR for lecture-lineage items = parent lecture project
(pre-program ancestor; the research plan D6 inherits its V&V
culture), NOT a D6 phase — declared, not orphan.

### B-papers (10 literature-pdf, OF-RECORD)

### B1. `PARENT/1-s2.0-S1540748912004014-main.pdf`
- IDENTITY: Wolanski, "Detonative propulsion", PCI 34:125-158
  (2013) — the RDE review.
- CONTENT OF RECORD: lecture-level digest only (CONTINUATION_PROMPT
  §5: rotating beats standing and pulsed; Wave Number W ties
  geometry to detonability; injection inversion behind the wave;
  Voitsekhovskii/Nicholls history). Registered as identified
  ARRIVAL in choking advisory §5. NOT cited in docs/ of the
  research program (grep: zero hits in docs/).
- WHERE READ: lecture project analyzer (paper 4 of 6, spec in
  parent project_build/specs/). STATUS: **READ-PARTIAL**
  (lecture-grade extraction; no page-verified research-grade read).
- PLAN-ANCHOR: lecture project; research-side UNCONSUMED — flag as
  candidate row for literature_registry with owner (any P-1
  framing window).
- UNIQUE-AT-RISK: none in the PDF; digest lives in
  CONTINUATION_PROMPT §5 + parent specs.

### B2. `PARENT/20180006890.pdf`
- IDENTITY: Kaemming-Paxson, "Determining the Pressure Gain of
  Pressure Gain Combustion", NTRS 20180006890 (EAP paper).
- CONTENT OF RECORD: choking = CYCLE-INTEGRAL definition shift
  (p.10); throat axial Mach 0.86-1.33 avg 0.99 (Table 1/Fig. 6);
  M=1 surrogate priced <5.4% (Fig. 7); swirl energy +6% EAPi CFD /
  +3% exp (p.7/p.11, quote completed at S-GAUNTLET); EAP
  construction (lecture §5); mediating total pressure is WRONG.
- WHERE READ: 15/15 pp READ-INTEGRAL, choking census 2026-08-11;
  earlier lecture analyzer (paper 5). STATUS: **READ-INTEGRAL**.
- PLAN-ANCHOR: U3' two-regime contract (choking C1-C5); T-T3-MAP
  breaker (c)/(d); K-P EAP lineage in M0.
- UNIQUE-AT-RISK: none (page anchors in choking advisory).

### B3. `PARENT/Aviation_2022_final.pdf`
- IDENTITY: Paxson-Miki-Perkins-Yungster, AIAA 2022-4107 — CFD
  optimization of an experimental RDRE nozzle.
- CONTENT OF RECORD: "pressure ratio and throat Mach number
  ILL-DEFINED" (p.2); fluidically choked exit, total Mach
  1.05-1.65 incl. tangential (Fig. 3 p.5); decoupling premise →
  our C3 certificate; steady sizing assuming M=1 misses optimal
  area ratio ~31%; interface std dev ~70% of means → Jensen
  (sigma/mu)^2~0.5 (breaker (b)).
- WHERE READ: 12/12 pp READ-INTEGRAL, choking census 2026-08-11.
  STATUS: **READ-INTEGRAL**.
- PLAN-ANCHOR: U3' contract C1-C3; F2a swirl data contract
  (F-swirl-1); shape-side ancestry (G1/G4 novelty rows).
- UNIQUE-AT-RISK: none.

### B4. `PARENT/FickettJacobsCycle (1).pdf`
- IDENTITY: Wintenberger-Shepherd, "Thermodynamic Cycle Analysis
  for Propagating Detonations", JPP 22(3):694-698 (2006) —
  CITATION.md source B.
- CONTENT OF RECORD: FJ cycle; implemented in src/cycles
  (B1/B2/B3=A57 equations), validated 99/99 PASS
  (data/cycles_validation.md); fixed-static vs fixed-stagnation
  ranking inversion = lecture's deepest point (CONTINUATION §5).
- WHERE READ: lecture project analyzer + equation-level
  implementation. STATUS: **READ-INTEGRAL** (implementation-grade).
- PLAN-ANCHOR: lecture project; repo src/cycles provenance
  (CITATION.md).
- UNIQUE-AT-RISK: none.

### B5. `PARENT/ShockDetonation.pdf`
- IDENTITY: Browne-Ziegler-Bitter-Schmidt-Lawson-Shepherd,
  "SDToolbox: Numerical Tools for Shock and Detonation Wave
  Modeling", GALCIT FM2018.001 (rev. 2021).
- CONTENT OF RECORD: SD Toolbox method doc (equilibrium-Hugoniot CJ
  minimum, PostShock frozen, zndsolve thermicity eigenvalue);
  vendored sdtoolbox/ provenance (sdtoolbox/PROVENANCE.md).
- WHERE READ: lecture project (paper 6 analyzer). STATUS:
  **READ-INTEGRAL** (lecture/implementation-grade).
- PLAN-ANCHOR: lecture project; sdtoolbox vendoring provenance.
- UNIQUE-AT-RISK: none.

### B6. `PARENT/aiaa2004-1033.pdf`
- IDENTITY: Wintenberger-Shepherd, AIAA 2004-1033, "Thermodynamic
  Analysis of Combustion Processes for Propulsion Systems" —
  CITATION.md source A.
- CONTENT OF RECORD: A-series equations (A19-A22 jump ratios,
  A31-A32 entropy partition, A38-A42, A57-A60) implemented in
  src/cycles/cycles.py, 99/99 PASS.
- WHERE READ: lecture project analyzer + implementation.
  STATUS: **READ-INTEGRAL** (implementation-grade).
- PLAN-ANCHOR: lecture project; src/cycles provenance.
- UNIQUE-AT-RISK: none.

### B7. `PARENT/computational-and-experimental-study-of-nozzle-performance-for-rotating-detonation-rocket-engines (2).pdf`
- IDENTITY: Harroun-Heister-Ruf, JPP 37(5):659-673 (2021),
  doi:10.2514/1.B38244.
- CONTENT OF RECORD: choking BYPASSED (inlet state imposed 1D
  upstream, Eq. (7) waveform, frozen T/velocities); 8x base drag;
  delayed separation; MISQUOTE OF RECORD — "near-perfect
  time-averaged expansion" DOES NOT EXIST in the paper (choking §3,
  T3 novelty STRENGTHENED, 3 litmap lines to rewrite);
  quasi-cycle-averaged C_F~1.25 method precision (§3-bis: no
  unsteady C_F exists; averaging convention UNDECLARED); throat
  restrictions may quench detonation (p.661 → C4 caveat);
  mass-flow matching convention (§2-bis(i)).
- WHERE READ: 14/14 pp READ-INTEGRAL, choking census 2026-08-11
  (+ §3-bis pages re-read by session lead). STATUS:
  **READ-INTEGRAL**.
- PLAN-ANCHOR: T3 novelty/misquote fix (F0 fix, litmap lines ~20,
  ~63-65, ~639); T0/measure formalization motivation; C4
  data-validity caveat; N2 truncation band.
- UNIQUE-AT-RISK: none (all in choking advisory).
- DEDUP: same content as `PARENT/harroun.txt` = `PARENT/hr.txt`
  (text extracts, md5-identical to each other).

### B8. `PARENT/rde_model_report.pdf`
- IDENTITY: Shepherd-Kasahara, "Analytical Models for the Thrust of
  a Rotating Detonation Engine", GALCIT FM2017.001 (2017).
- CONTENT OF RECORD: PH + axial-flow thrust models implemented in
  src/thrust/sk_models.py (Eqs. 6, 15-20, 44-45), validated vs
  Tables 1-2 (vv_thrust 8/8; U_CJ ≤0.1%); wave count N cancels;
  axial expansion on the CJ isentrope; term II ~15-20%. Choking-
  relevant RE-READ QUEUED (choking advisory §5) — never executed.
- WHERE READ: lecture project analyzer (paper 1) + implementation.
  STATUS: **READ-INTEGRAL** (implementation-grade); research-side
  choking re-read = OPEN duty with owner (next lit window).
- PLAN-ANCHOR: lecture project; src/thrust provenance; choking §5
  queued-read row.
- UNIQUE-AT-RISK: none.

### B9. `PARENT/stechmann-et-al-2018-rotating-detonation-engine-performance-model-for-rocket-applications (1).pdf`
- IDENTITY: Stechmann-Heister-Harroun, JSR 56(3):887-898 (2019).
- CONTENT OF RECORD: choking = DECLARED ASSUMPTION p.889 verbatim
  (corrected at S-GAUNTLET page-verify); Eq. (4) mass-weighted
  averaging = the functional's 0-D ancestor (18/18 Table-1 fidelity
  in-repo, data/st_opt_validation.md); Assumption 3 = priced H2;
  Fig. 8 bells "significantly overexpanded" remark (breaker (a));
  anchors of record Eq. (4) p.888, quotes pp.893-895.
- WHERE READ: 12/12 pp READ-INTEGRAL, choking census 2026-08-11;
  earlier lecture analyzer (paper 2) + Table-1 implementation.
  STATUS: **READ-INTEGRAL**.
- PLAN-ANCHOR: functional lineage (M0/D-MU); T-T3 breaker (a)
  sea-level verdict; H2 pricing.
- UNIQUE-AT-RISK: none. DEDUP: `PARENT/stech.txt` extract.

### B10. `PARENT/Presentazione_CVA.pdf`
- CLASS: **fig/asset** (NOT literature) — PDF export of the final
  deck. STATUS-AUTHORITY: OF-RECORD (lecture deliverable,
  VALIDATION.md §5). PLAN-ANCHOR: lecture project deliverable.
  UNIQUE-AT-RISK: none beyond the pptx it renders. Classified
  without read (binary render).

### B-presentation lineage (26 pptx — bulk block; class
### **presentation-lineage**, classified without read, binary)

Deck of record: **`PARENT/Presentazione_CVA.pptx`** (82 slide, 75
speaker notes — OF-RECORD, the lecture deliverable per
VALIDATION.md §5). Template: **`PARENT/ppt_Heister.pptx`**
(OF-RECORD asset — the binding style template). ALL others are
SUPERSEDED-BY-Presentazione_CVA.pptx (draft lineage; R4: archive
candidates with banner, never delete):
- `PARENT/Presentazione_CVA_FINALE_84slide.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_Editing.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v2.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v3.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v4.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v5.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v6.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v7.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v8.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v9.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v10.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v11.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v12.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v13.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v14.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v15.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v16.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v17.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v18.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v19.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v20.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_FINALE_v21.pptx` — SUPERSEDED
- `PARENT/Presentazione_CVA_v1_backup.pptx` — SUPERSEDED (backup)
- `PARENT/Presentazione_CVA_v6_PRONTA_83slide.pptx` — SUPERSEDED
PLAN-ANCHOR (all): lecture project lineage. UNIQUE-AT-RISK: the
FINAL deck + template carry the deliverable; intermediates none
(lineage only). NOTE for T2: which of v21 / FINALE_84slide /
Presentazione_CVA.pptx is truly last needs a mtime check at
migration time — VALIDATION.md names `Presentazione_CVA.pptx` (82
slide) as the deliverable; trust it as of-record.

### B-prose, extracts, assets (11 files)

### B11. `PARENT/CONTINUATION_PROMPT.md` — READ IN FULL here.
- CLASS: session-prompt (lecture project transfer prompt).
- ROLE: SOTA multi-agent workflow spec for the lecture project
  (per-paper analyzer protocol, image-QA loops, V&V, style pins,
  project_build/ inventory).
- STATUS-AUTHORITY: **CONSUMED** (lecture completed; closure record
  = VALIDATION.md; the repo's whole V&V/convergence-loop culture is
  its descendant).
- PLAN-ANCHOR: lecture project (ancestor of R5 discipline).
- UNIQUE-AT-RISK: §5 "note di merito per paper" (per-paper subtle
  points: SK N-cancellation, S-H mass-weighting rationale, W-S
  ranking inversion, Wolanski Wave Number, K-P EAP construction)
  and §4 validated reference data live only here + parent
  project_build/specs — MODERATE risk; destination candidate:
  literature_registry per-paper notes.
- REFS: project_build/ (outside all three roots — flag: the
  per-paper specs it cites are in the parent project_build/specs/,
  not inventoried in any segment list).

### B12. `PARENT/VALIDATION.md` — READ IN FULL here.
- CLASS: doc-validation (lecture project closure record).
- ROLE: final V&V map of the lecture (all suites converged), deck
  QA, deliverables; dated 2026-07-10, repo @ a986717.
- STATUS-AUTHORITY: **OF-RECORD** (parent project closure).
- PLAN-ANCHOR: lecture project closure; repo V&V lineage (its
  suite rows point INTO rde-lecture-code data/ and validation/).
- UNIQUE-AT-RISK: §3 "correzioni sostanziali" 7-item list (gamma_eq
  bug, SK term II omission, p_t2/p_t1 one-gamma artifact, q at
  298.15 K, vN chord fix, SK Table 1 704 s shown to be a paper
  typo (ours 937 s), CJ deflagrative-branch maximum) — the typo
  finding and correction history live ONLY here at this level of
  synthesis (suite files carry the numbers). HIGH-value unique row
  for the nothing-lost ledger.
- REFS: data/*.md suites in the repo; project_build/qa reports.

### B13-B17. Text extracts (class **extract/derived**, classified
without integral read — derived from the B-paper PDFs for the
2026-08-11 page-reads; head-peeked + hashed here):
- `PARENT/harroun.txt` — Harroun JPP 2021 full-text extract (647
  lines). DERIVED from B7. Watermark: downloaded 2026-08-11 (the
  choking-census read). UNIQUE-AT-RISK: none (regenerable).
- `PARENT/hr.txt` — **md5-IDENTICAL duplicate of harroun.txt**
  (782a3f45...). DERIVED, redundant copy — dedup row for T2.
- `PARENT/kp.txt` — Kaemming-Paxson EAP extract (319 lines).
  DERIVED from B2.
- `PARENT/pm.txt` — Paxson-Miki AIAA 2022-4107 extract (518
  lines). DERIVED from B3.
- `PARENT/stech.txt` — Stechmann JSR 2019 extract (860 lines).
  DERIVED from B9.
PLAN-ANCHOR (all five): choking census machinery (ADVISORY_
rde_choking evidence base).

### B18. `PARENT/old_commit_hashes.txt` (115 lines, full hashes)
### B19. `PARENT/old_short_hashes.txt` (115 lines)
- CLASS: derived-cache / **garbage-candidate**. ROLE: git-history
  maintenance byproducts (Jul 22 window; sibling of repo-root
  mailmap.txt / current_commit_messages.txt untracked strays).
- STATUS-AUTHORITY: RAW/DERIVED. PLAN-ANCHOR: **ORPHAN — flagged
  loudly** (no nameable plan need; candidate archive-with-banner or
  user-approved disposal decision in T2; R4 forbids silent delete).
- UNIQUE-AT-RISK: pre-rewrite commit-hash map (115 hashes) — IF a
  history rewrite happened, this is the only old↔new provenance
  map; verify against repo reflog before archiving.

### B20. `PARENT/SDToolbox.zip` (4.5 MB, Jul 9)
- CLASS: data/asset. ROLE: official SD Toolbox release (Apr 2026,
  "zip del docente") — the audit source of
  data/sdt_official_audit.md ("vendored functionally identical,
  patch a_fr ≤0.02%").
- STATUS-AUTHORITY: **OF-RECORD** (audit input; single copy).
- PLAN-ANCHOR: lecture V&V row (VALIDATION.md §1 last row);
  sdtoolbox vendoring provenance.
- UNIQUE-AT-RISK: the official upstream snapshot itself (single
  copy; the audit refers to it).

### B21. `PARENT/brick2_profiles_record.png` (Aug 6)
- CLASS: fig. ROLE: brick-2 profiles record figure (S18 window,
  matching s18-brick2-closed era).
- STATUS-AUTHORITY: OF-RECORD (record figure) but **MISPLACED**
  (lives in the parent dir, outside the repo, single copy,
  untracked). PLAN-ANCHOR: S18 brick-2 closure (O3.3 unlock).
- UNIQUE-AT-RISK: the figure itself (numbers of record are in the
  repo; the rendered record figure exists only here). T2
  destination: move-copy into validation/ with index row.

---

## ROOT C — GENO/ (77 PDF, read-only, independent repo)

### C-literature: `REPO/GENO/literature/` (20 files, class
### literature-pdf, OF-RECORD; identities and read-status all from
### ADVISORY_generality_litmap_2026-08-12.md §1 — every VARIATIONAL
### paper read IN FULL by the 8-reader campaign; handbooks/theses/
### non-variational triaged at declared depth)

- `REPO/GENO/literature/RAO.pdf` — Rao, Jet Propulsion 28(6):377-382
  (1958), bell TOC. **READ-INTEGRAL** (litmap §3.1; [X-TOCV] 91/91
  classical-vs-gradient agreement; T-T3 collapse point; p.382
  refutes G-H single-contour). Anchor: litmap §3.1/§3.2.
- `REPO/GENO/literature/Rao_1961_review.pdf` — Rao, ARS J
  31(11):1488-1494 (1961) survey. **READ-INTEGRAL** (litmap §3.15,
  §7.8: the 1961 unsolved-gap list maps 1:1 onto the program —
  P-1 framing material).
- `REPO/GENO/literature/Rao_1961_spike.pdf` — Rao, BMST v2:92-101
  (1961) spike/plug; DUAL-VENUE identity with Planet. Space Sci.
  4:92-101. **READ-INTEGRAL** (litmap §3.3; printed Eqs. (8)/(9)
  endpoint-label SWAP page-verified twice; GENO CSTR_PA/CSTR_PB
  pairing correct; flag D-F).
- `REPO/GENO/literature/migdal.pdf` — Migdal, JSR 9(1):3-6 (1972),
  annular, non-variational. **READ-PARTIAL** (triaged; litmap
  §3.15: two-wall design-space geometry, optimization deferred to
  Rao).
- `REPO/GENO/literature/design-of-maximum-thrust-plug-nozzles-for-fixed-inlet-geometry.pdf`
  — Humphreys-Thompson-Hoffman, AIAA J 9(8):1581-1587 (1971).
  **READ-INTEGRAL** (litmap §3.4; §7.4 start-line precedent 34,373
  vs 34,375 lbf — D1 interface-contract provenance).
- `REPO/GENO/literature/hoffman-2012-a-general-method-for-determining-optimum-thrust-nozzle-contours-for-chemically-reacting-gas-flows.pdf`
  — Hoffman, AIAA J 5(4):670-676 (1967), reacting, multiplier
  fields. **READ-INTEGRAL** (litmap §3.5; E-residual Eq. (78) = a
  VI.3 certificate; p.676 corner-bijection death = closed-form
  boundary proof; M0 T-T3-CE cites it).
- `REPO/GENO/literature/scofield-hoffman-2012-maximum-thrust-nozzles-for-nonequilibrium-simple-dissociating-gas-flows.pdf`
  — Scofield-Hoffman, AIAA J 9(9):1824-1832 (1971). **READ-INTEGRAL**
  (litmap §3.6; tabular-EOS precedent for [DIR-THERMOTAB];
  noneq-closer-to-frozen finding = freeze-at-CJ twin; quote-residue
  spot-check flag before PRINT citation, refuter E4).
- `REPO/GENO/literature/Allman_Hoffman_1981.pdf` — AIAA J
  19(6):750-751 (1981) direct method. **READ-INTEGRAL** (litmap
  §3.9; direct-vs-indirect resolution; ≤0.2%/0.66% price).
- `REPO/GENO/literature/rao-beck-2012-use-of-discontinuous-exit-flows-to-reduce-rocket-nozzle-length.pdf`
  — Rao-Beck, AIAA 94-3264 (1994), DEF. **READ-INTEGRAL** (litmap
  §3.10; "Rao-Beck Eq. (4)" MUST cite the 1994 paper; S4 THEOREM
  (G)≡Eq.(4); refuter re-opened incl. reference list).
- `REPO/GENO/literature/rao-et-al-2012-nozzle-optimization-for-space-based-vehicles.pdf`
  — Rao-Beck-Booth, AIAA 99-2584 (1999), DEF eq/frozen chemistry.
  **READ-INTEGRAL** (litmap §3.10; Eq.-numbering trap — 1999
  renumbers; boundary = unnumbered or Eq. (6); optimum ON the
  validity boundary = margin-activity classical statement).
- `REPO/GENO/literature/BF00934730.pdf` — Hoffman-Scofield-Thompson,
  JOTA 10(3):133-159 (1972), BL-in-the-loop. **READ-INTEGRAL**
  (litmap §3.7; ≤0.018% thrust in-loop gain = evidence FOR viscous
  layering; §6(c) structural non-containment).
- `REPO/GENO/literature/1-s2.0-0045793074900127-main.pdf` —
  Johnson-Thompson-Hoffman, C&F 2:173-190 (1974), variable-inlet
  rotational plug. **READ-INTEGRAL** (litmap §3.8; lip
  transversality = classical dJ/dy_lip; p_a>0 limit = vacuum
  no-optimum instance; base-constant sensitivity split → DUTY-10).
- `REPO/GENO/literature/Veen.pdf` — Vander Veen-Gentry-Hoffman,
  AIAA J 12(9):1193-1197 (1974), shrouded plug. **READ-INTEGRAL**
  (litmap §3.11; two decoupled Rao problems; GENO S4/S5/S6
  implementation bugs of record stand; base constants 0.846/M^1.3
  → §7.5 unreliability row).
- `REPO/GENO/literature/ADA455494.pdf` — Onofri et al.,
  RTO-TR-AVT-007 / AIAA 2002-0584 plug survey, non-variational.
  **READ-PARTIAL** (triaged; litmap §7.5: Veen constants reappear
  as Eq. (5.1), reported UNRELIABLE vs WG10 [+19%,-15%]; Angelino
  planar-only caveat page-anchored).
- `REPO/GENO/literature/NASA_RP1104_bell_nozzle_curves.pdf` — NASA
  RP-1104 (1983) truncated-perfect curves, non-variational.
  **READ-PARTIAL** (triaged; litmap §3.15: graphical truncation
  tangency = cheap surrogate the bound ladder prices).
- `REPO/GENO/literature/NASA_SP8120_liquid_rocket_nozzles.pdf` —
  NASA SP-8120 (1976). **READ-PARTIAL** (triaged; litmap §3.15:
  Fig. 6 institutional failure boundary (Sternin echo, P-1
  framing) + plug-optimization GAP declaration — PB-2/T4 open at
  handbook level).
- `REPO/GENO/literature/Johnson_Boney_1975_NASA_real_gas_nozzle.pdf`
  — NASA TM X-3243. **READ-PARTIAL** (triaged; litmap §7.6
  RECLASSIFIED non-variational: tabulated real-gas MoC uniform-exit
  design; [DIR-THERMOTAB] classical ancestor; gamma-sensitivity
  ~80x length ratio; D2 b0 label duty).
- `REPO/GENO/literature/Zucrow_Hoffman_Gas_Dynamics_Vol2.pdf` —
  Zucrow-Hoffman (1977) handbook. **READ-PARTIAL** (triaged;
  litmap §1: 16-4(c) Rao; 17-5(c) rotational max-thrust lineage;
  "Rao-vs-Zucrow naming inversion" table context in §7.2).
- `REPO/GENO/literature/tesi_viviano.pdf` — Viviano, Sapienza 2023
  (rel. Nasuti). **READ-PARTIAL** (declared depth; litmap §3.16:
  p.82 fluid-independence claim; psi (4.27-4.28) = FD Lambda-form
  = GENO boundaryfunction lineage; DEF "suboptimal by construction"
  → §7.3 three-way tension; zero RDE content verified).
- `REPO/GENO/literature/thesis_valeriani.pdf` — Valeriani, Sapienza
  2019/20 (rel. Nasuti). **READ-PARTIAL** (declared depth; litmap
  §3.16: GENO v3.x lineage doc; Rao plug outside perfect-gas with
  honest caveat; PSO/fminsearch = direct-method instances).

UNIQUE-AT-RISK (all 20): none — analyses live in the litmap
advisory + D2 b0/b2 + literature_map; the PDFs are primary sources
(GENO repo is their home; read-only from here).

### C-GenoPlug (5 entries, class fig/DERIVED — GENO plot outputs)
- `REPO/GENO/GenoPlug/ang_contour.pdf` — DERIVED (GENO run figure,
  Angelino contour). Classified without read (derived binary).
- `REPO/GENO/GenoPlug/ang_wall.pdf` — DERIVED (wall profile fig).
- `REPO/GENO/GenoPlug/mira_contour.pdf` — DERIVED (contour fig).
- `REPO/GENO/GenoPlug/mira_wall.pdf` — DERIVED (wall fig).
- `REPO/GENO/GenoPlug/plt/mira_*.pdf` — NOTE: this list line is a
  literal GLOB, not a single file; it stands for the mira_* plot
  set under plt/. Accounted as one list entry per the authoritative
  list; T2 lint should expand it. DERIVED (regenerable by GENO).
PLAN-ANCHOR: GENO twin/oracle machinery (KAT/defnoz gate era);
no repo-side record content — numbers of record live in repo
gates/advisories. UNIQUE-AT-RISK: none (regenerable, GENO-owned).

### C-vendor docs (52 files, class vendor-doc, DERIVED/external —
### third-party library documentation vendored inside GENO's
### dependency tree; NOT literature; classified without read; no
### plan anchor needed beyond "GENO dependency tree, read-only";
### UNIQUE-AT-RISK: none — all publicly redistributable manuals)

FLINT/ORION/OSlo/FATODE/Intel-ODE tree (4):
- `REPO/GENO/lib/FLINT/lib/ORION/docs/360_data_format_guide.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/FATODE/doc/FATODE_user_guide.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/Intel-ODE/doc/ODE_install.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/Intel-ODE/doc/ODE_manual.pdf`

sundials doc tree under OSlo (35):
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/arkode/examples/source/figs/doc_logo_blue.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/cvodes/cvsadjkryx_p2D.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/cvodes/cvsadjkryx_p3Dcf.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/cvodes/cvsadjkryx_p3Dgrad.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/cvodes/cvsadjnonx_p.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/cvodes/cvsfwddenx.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/cvodes/cvsfwdkryx_p.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/cvodes/cvsfwdnonx.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/cvodes/pvfktTest.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/ida/idaorg.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/idas/ckpnt.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/idas/figs_slcrank/slider_crank.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/idas/figs_slcrank/x2sensi.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/idas/idasorg.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/arkode/doc_logo_blue.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/bandmat.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/ckpnt.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/cmake/ccmakeempty.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/cmake/cmaketest.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/cscmat.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/cvode/cvorg.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/doc_logo.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/doc_logo_blue.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/sunorg1.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/sunorg2.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/shared/figs/warning.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/sundials/figures/bandmat.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/sundials/figures/cmake/ccmakeempty.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/sundials/figures/cmake/cmaketest.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/sundials/figures/cscmat.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/sundials/figures/doc_logo.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/sundials/figures/doc_logo_blue.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/sundials/figures/sunorg1.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/sundials/figures/sunorg2.pdf`
- `REPO/GENO/lib/FLINT/lib/OSlo/lib/sundials/doc/sundials/figures/warning.pdf`

sundials doc tree under cantera/ext (13):
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/INSTALL_GUIDE.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/arkode/ark_examples.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/arkode/ark_guide.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/cvode/cv_examples.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/cvode/cv_guide.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/cvodes/cvs_examples.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/cvodes/cvs_guide.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/ida/ida_examples.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/ida/ida_guide.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/idas/idas_examples.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/idas/idas_guide.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/kinsol/kin_examples.pdf`
- `REPO/GENO/lib/FLINT/lib/cantera/ext/sundials/doc/kinsol/kin_guide.pdf`
(Note: sundials manuals appear TWICE inside GENO — OSlo tree and
cantera/ext tree — an internal GENO duplication, out of our
jurisdiction, recorded for completeness.)

---

## CROSS-ROOT DEDUP SUMMARY
1. `PARENT/hr.txt` == `PARENT/harroun.txt` (md5 782a3f45... —
   bitwise duplicate; one is disposable-after-archive decision).
2. `PARENT/harroun.txt`/`hr.txt` are extracts of B7 (Harroun PDF);
   `PARENT/kp.txt` of B2; `PARENT/pm.txt` of B3; `PARENT/stech.txt`
   of B9 — derived, regenerable.
3. `PARENT/Presentazione_CVA.pdf` is the render of
   `PARENT/Presentazione_CVA.pptx`.
4. No paper PDF is duplicated across the three roots (Stechmann/
   Harroun/K-P/P-M live only in PARENT; classical corpus only in
   GENO; adjoint/Soviet/PDE corpus only in repo literature/).
5. GENO-internal: sundials manuals duplicated across two vendored
   trees (35-set vs 13-set overlap in content, different builds).

## AT-RISK LEDGER ROWS (unique content living only in this segment)
1. `PARENT/VALIDATION.md` §3 — the 7 substantive corrections incl.
   SK Table 1 "704 s is a paper typo (ours 937 s)". Destination
   needed (literature_registry note or archived index row).
2. `PARENT/CONTINUATION_PROMPT.md` §4-§5 — validated reference data
   + per-paper notes of merit. Destination: literature_registry
   per-paper notes (or archive-with-banner + index row).
3. `PARENT/Presentazione_CVA.pptx` + `ppt_Heister.pptx` — the
   lecture deliverable and its binding template (single copies).
4. `PARENT/SDToolbox.zip` — official upstream snapshot, audit input
   (single copy).
5. `PARENT/brick2_profiles_record.png` — S18 record figure,
   misplaced outside the repo (single copy).
6. `PARENT/old_commit_hashes.txt` + `old_short_hashes.txt` —
   possible pre-rewrite hash provenance map (verify vs reflog
   before any disposal; ORPHAN otherwise).
Everything else in the segment: "none" (analyses live in advisories
/ literature_map / data suites; PDFs are primary sources kept
of-record in place).

## ORPHAN CANDIDATES (PRIMARY LENS)
- `PARENT/old_commit_hashes.txt` — no nameable plan need. ORPHAN.
- `PARENT/old_short_hashes.txt` — same. ORPHAN.
(All other artifacts anchor to: the lecture project lineage, a D6
phase/gate (F4b entries, F5b bench, O3 obligation, G14/P-2, U3'
contract), a census row (R31/R32), or GENO's own machinery.)

## DOWNSTREAM DUTIES SURFACED (for T2 literature_registry, with owner)
1. WANTED: AIAA 2019-0197 (sole remaining fetch; choking §3) —
   acquisition register.
2. WANTED: Peter-Desideri 2022 / Ancourt-Peter 2023 / L-P 2023
   Aerospace 10:267 (P-2 mandatory-cite, acquisition-pending).
3. Shepherd-Kasahara rde_model_report choking-relevant RE-READ
   (queued in choking §5, never executed) — next lit window.
4. Wolanski PCI 2013: research-grade read never done (lecture-grade
   only) — register READ-PARTIAL with owner.
5. Litmap duties D-A..D-F (already owned; restated here because the
   files they concern are in this segment).
6. `plt/mira_*.pdf` glob line in seg7_geno_pdfs.txt should be
   expanded to literal files by the T2 lint (accounting hygiene).
7. project_build/specs/ (parent, 6 per-paper specs) is cited by
   CONTINUATION_PROMPT but is in NO segment list — coverage-gap
   flag for the reconciliation master (it may be outside the
   declared 3-root scope; decide explicitly, don't drop silently).

## CODENAME TOKENS COLLECTED (token | where seen | meaning)
1. [X-TOCV] | litmap §3.1 | classical-vs-gradient Rao agreement carrier (91/91)
2. [X-O33B] | litmap Route A | f2=-lambda2 constancy measurement carrier
3. [X-MGOV] | litmap §3.10 | margin-governor derived bands carrier
4. [X-VMON] | litmap §7.2 | 247-point validity-monitor grid (falsifier substrate)
5. [X-A1IM] | litmap §3.4 | GENO IVL twin interface checks
6. [X-TBAK] | litmap §4(5) | tolerance-ball backoff carrier (L_TB=4.32e+01)
7. [X-IVXC] | memory/gitStatus | cross-code invariant suite carrier
8. [X-CDKAT] | memory S21 | certdiag retro-validation vs KAT
9. [X-SCANM] | memory S17 | scan-matrix duty carrier
10. [X-LSG0] | memory S17 | G0-related S17 duty carrier
11. [X-THC1] | memory S25 | thermo-closure flip-condition test
12. [X-SPDB] | S25 commits | speed-database claims-registry scope row
13. GAP-5 | prompt/memory | notaknot BC-twin gap (corner mismatch -82%, owner F2)
14. GAP-29 | prompt/memory | halved-constants sweep gap (NTF flip, owner F2)
15. GAP-18 | gitStatus S25 | gap-map row re-owned to N6
16. R1-R6 | CLAUDE.md | plan-adherence protocol rules
17. R25/R28-R33 | prompt/census | census rows (R31 findings-as-code, R32 S-ORDINE, R33 next)
18. C1-C5 | choking §2 | extraction-contract consequences (two-regime, axial criterion, decoupling cert, throat caveat, surrogate pricing)
19. C-O33 | litmap Route A | open conditional: O3.3 class-limited residual
20. C-MAJDA | memory S16 | conditional sharpened to U3-H1
21. C-EQV2 / EQ-v2 | memory/litmap §3.10 | DEF equivalence conjecture A/B under H1-H6
22. [C-HT4] | litmap §3.3 | hypothesis class for T-T4 THEOREM*
23. M0 | CLAUDE.md | master theory doc of record
24. M1-M6, M-D, M-E | S25 memory | speed-chain levers and stop-check counters
25. H1-H4 | litmap §3.1 | T-T3 collapse hypotheses
26. H2' | choking 2-ter | separation-related hypothesis exit at pa!=0
27. T0-T7 | choking/litmap | theory theorems (T0 steadification; T7 averaged stationarity; (**') weighted transversality)
28. T-T3 / T-T4 / T-T3-MAP / T-T3-CE / T-T7FS | litmap | collapse dichotomy theorems, breaker map, corner-example, weighted-transversality precedent note
29. T-O1 / T-O2 | choking (a)/litmap §4 | protection/log-uniform measure theorems
30. [T-EQBR] | litmap §3.5 | frozen/equilibrium bracket pricing
31. [T-SLRW] | memory S15 | side-load/rim theorem row
32. T-XWALL / T-XWS | memory S15 | S15 foundations tranche theorems
33. T3-QS | litmap/choking | quasi-steady per-phase sweep protocol
34. T3-C2 | literature_map | altitude-duality bridge corollary
35. O1-O5 | plan/choking | oracles (O3 = classical-optimality ledger obligation; O5 = single-cycle PDE bench anchor)
36. O3.1/O3.2/O3.3 | litmap | adjoint-identity measurement campaigns
37. P-1 / P-2 | CLAUDE.md/litmap | paper deliverables (JPP; adjoint-bridge companion)
38. P1/P2 (pins) | litmap §6 | user scope pins: frozen thermally-perfect; no two-phase
39. PB-1..PB-4 | litmap | problem-book frontier problems (PB-2 truncated plug averaged; PB-4 bilevel coupling)
40. OP-11 | litmap §4(7) | measure-selects-topology open problem
41. REQ-NONSTALL | memory/plan | user requirement: optimizer never stalls on internal-shock fields
42. G0-G6 | CLAUDE.md R6 | plan gates (G1 oracle certification absolute; G5 Kraiko/PMM human pass)
43. G8/G10/G12/G14 | literature_map | novelty gap rows (G14 = Rao=adjoint bridge)
44. (P) / (P_t) | litmap §0 | problem of record + tier ladder
45. (G) / Lambda-form | litmap §3.10/§7.2 | validity-boundary margin (S4 THEOREM ≡ Rao-Beck Eq. (4) 1994)
46. KAT | memory S23 | GENO kernel acceptance test (conditional landed, GENO fca273a)
47. defnoz | S25 commits | default-nozzle gate case family
48. A1_COLEXEC / A1_VMAP_HESS | S25bis commits | arbitration env-flags (col-executor default; batched-Hessian opt-in)
49. K_RICH / K_NEWT / NEWTON_TOL_FACTOR / C_FLOOR / C_OPS | S25bis/gitStatus | derived-constant bounds in the speed program (NTF = GAP-29 flip)
50. N2 / N4 / N5 / N6 | choking/litmap | base-closure band; thermo ladder; startup pricing; swirl rigor attack (N6-1/2/3, N6-5F)
51. F0-F6, F1b, F2a, F4b, F5b | plan D6 | program phases (F4b = fitted fronts; F2 = general engine, NEXT)
52. F-KO5 / F-CONTAINDIR / F-O33BENCH / F-PETERANC | literature_map (PAN-S14) | S14 panel findings (K-O §5 collapse; containment direction; O3.3 bench of record; Peter/Ancourt reclass)
53. F-swirl-1 / F-swirl-2 | choking 4-bis | F2a swirl-transport row + swirl-uniformity monitor flags
54. D-A..D-F | litmap §8 | litmap-advisory duties with owners
55. [DIR-THERMOTAB] | litmap §3.6 | standing directive: tabulated thermo backend
56. DIR-RKG | memory S17 | S17 duty (RKG directive)
57. D1-D7, D2 b0/b2 | CLAUDE.md/litmap | depth docs; litmap bibliography annexes
58. S-H | choking/litmap | Stechmann-Heister (EAP-school shorthand in M0 remarks)
59. EAP / EAPi | choking (b) | equivalent available pressure (K-P doctrine)
60. [S-D25U-U34] | litmap §2 | fitted-front adjoint jump lineage row
61. S-ACFR / S-GBE / S-LBML | memory S16 | S16 foundations results
62. U1-U5, U3' | choking §2/memory | foundations lemmas; U3' = sharpened extraction contract
63. L4 | memory S16 | ledger default row (p2 tranche)
64. [P-TRFLOOR] / [P-FLIPMAT] | S25 commits | ledger rows (blocked / de-registered)
65. [PAP-RIM] | memory | roads-x-insertions paper duty queued after brick 2
66. [OBJ-DOM] / [G1-DISC] | S25 commits | F2-entry owner rows (objective-domain; G1 discharge)
67. CSTR_PA / CSTR_PB | litmap §3.3 | GENO spike endpoint-constraint implementations (pairing verified correct)
68. m5cgate/m6gate/h3gate/m12gate | S25bis commits | speed-program acceptance gates
69. H-T4 / H-CLASS | litmap §3.15 / memory S24 | Angelino ideal-adaptation closure hypothesis; S24 EQ-v2 hypothesis class
70. RK-A | plan D6 ~1058 | risk row: P2' scoop risk (Lozano-Ponsin)

---
RECONCILIATION: Root A 13 + Root B 47 + Root C 77 = **137 = list
total, discrepancy 0**. Every listed path appears literally above
(A1-A13; B1-B10 papers/asset, 26-row pptx block, B11-B21;
C-literature 20, C-GenoPlug 5, C-vendor 52).
