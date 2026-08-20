# PANEL — CLUSTER C2021 (C20 certificate qualification + C21 seed validity)
S-FOUNDATIONS-C2, blocco 3 wave 2 — RECONCILED of record per
BRIEF_wave2_reconcile.md (post quota-kill #5 relaunch; the on-disk partial of
this same path consumed as UNVERIFIED DRAFT INPUT, verified/repaired/completed
— see RECONCILIATION DECLARATION at end). Panel of record per
BRIEF_wave2_panels.md §C2021 (+ §0 of BRIEF_wave1_panels.md verbatim, §0-bis
directive axes, §0-ter world-class census protocol).
BASE = validation/sfoundations_raws_2026-08-13.
CENSUS VALIDITY STAMP: census executed and dated 2026-08-19; reconcile pass
same day re-verified 4 load-bearing census items at source (§2.1 note) and
re-measured every dedup grep (§2.4). Wave-1 dependency consumed:
VERDICT_wave1.md §2.1 (C28) + RC28-8 — read in full this window. NEW in the
reconcile: the LANDED C9/C11/C56 ledger rows consumed (§1.5). All file:line
anchors below re-read at source in THIS window (SR-12); wave-1-era and
gapmap-era anchors tagged where line drift exists.

---

## 1. FROZEN FORMAL STATEMENT

### 1.0 Shared sub-problem (frozen before census)

Objects. Per-cell implicit system F_cell(z; p) = 0 — z in R^4 (interior
cell; R^2 axis/wall variants), p = parent-cell data + design/thermo
parameters — solved by damped Newton inside the custom_vjp implicit-solver
factory (`get_solver`/`make_implicit_solver`, validation/
a1_ideal_march_jax.py:752-758), compiled once per residual family. The march
is a DAG of such solves (record mode: predictor seeds from the GENO Ch.16
foot-state expressions, `predict_interior` :621-639 and traced twin
`predict_interior_t` :668-693; replay mode: recorded z reused as
gradient-stopped Newton seeds, `Sched.cell` :737-746, at possibly PERTURBED
p — the verdict-bearing O3.1 FD probes replay at perturbed P with
h_FD = 6.1e-6, CERT_PLAY armed :1429-1430). Certificate of record: the
one-extra-step ratio in `certify` (:795-828): ratio = |extra Newton step| /
(NEWTON_TOL_FACTOR * EPS * sc), NEWTON_TOL_FACTOR = 100.0 (:200),
sc = max(1, max|z|) (:812); accepted iff ratio <= 1 (:821); the P4 gate
consumes cert_worst. Fold set: det J_cell -> 0 (the branch pair meets; in
the closed-form predictor the same degeneration is den -> 0, :690 in the
traced twin, :636 in the host).

Hypotheses of record. The `certify` comment claims derivation "from the
Newton contraction" (:801) — the contraction hypothesis is never checked;
no kappa(J) qualification, no branch-consistency monitor exists (findings
row cell-cert:certify-no-conditioning-qualification, findings_registry.yaml
:1145-1154, CONFIRMED HIGH, failure modes TOY-measured — Q3 quarantine
carried in-row :1154). The z-basin shrinks like sqrt(dist-to-fold) below
h_FD near folds (cell-cert:seed-validity-radius-underived :1281-1289,
CONFIRMED MEDIUM). Record campaigns ran margin-inactive, far from folds
(gapmap GAP-3 EXPOSURE :161-164 "invisible exactly where everything works";
GAP-20 SEVERITY :558-560 "record campaigns ran margin-inactive, far from
folds").

Program context (binding): certified marched axisymmetric solver, JAX
custom_vjp discrete-adjoint stack, one-lowering discipline; P4/P3(ii)
binary gates are absolute verifiers (wave-1 C28 verdict, facet quote of
record); "Only K_budget may ever be enlarged; the certification floor is a
tolerance and does not move" (M0:2056-2058, re-read this window; the
wave-1-era anchor M0:2005-2011 has drifted — M0 was edited between the
verdict's window and this one); R5: tolerances derived, rejectors must
fire; env pinned.

### 1.1 C20 — THE SINGLE MAIN QUESTION

**What must the per-cell certificate ASSERT — and against which CHECKED
hypotheses — so that a P4-gated "certified" verdict rules out both
conditioning artifacts (false FAIL: exact root rejected at ratio 25) and
wrong-branch roots (false PASS: other branch certified at ratio 0.0) at the
certifiability frontier where the program's outcome-II verdicts live?**

Pre-registered decision criteria (frozen BEFORE the census; no mid-census
amendments were made):
- W1 (discrimination): the option must discriminate BOTH measured failure
  modes on the GAP-3 near-fold toy family, committed as carrier.
- W2 (derivation): constants derived, no new magic factors (interacts with
  C18 NEWTON_TOL_FACTOR derivation duty and C19 metric scale — named, not
  decided here).
- W3 (cost): always-on part must reuse the Newton Jacobian already formed
  (O(1) extra per cell at production counts); heavier machinery only at
  flagged cells.
- W4 (stack fit): record/replay modes + tracer guard preserved (certify's
  own guard :808-810); the custom_vjp implicit path untouched.
- W5 (discipline fit): P4 stays the absolute verifier; the floor does not
  move; qualification RE-DERIVES what the certificate asserts and may
  re-class verdicts only via an ITEMIZED reclassification report — never a
  silent relabel.
LOSS criteria: an option that cannot fire (no rejector), or that asserts
membership it cannot check at cell granularity, or that needs per-cell
exact/rational arithmetic at production counts, LOSES the always-on role
(referee roles remain open to it).

### 1.2 C21 — THE SINGLE MAIN QUESTION

**What DERIVED predicate makes a Newton seed valid — predictor output at
record time, recorded z at PERTURBED p at replay time — i.e. guaranteed in
the intended root's basin, replacing the asserted O(h) and the unqualified
stale-replay premise on the verdict-bearing O3.1 path?**

Pre-registered decision criteria (frozen BEFORE the census):
- V1 (radius): a per-seed or per-region DERIVED validity radius in z-space
  tied to the INTENDED branch.
- V2 (coverage): both seed families covered (predictor at record; recorded
  z at perturbed p in replay) including the O3.1 perturbation ball h_FD.
- V3 (fires): the certificate must FIRE on planted frontier cells and stay
  quiet at everyday cells (fire rate measured; cava D-47 discipline: seed
  rejector demonstrated firing).
- V4 (cost): O(one Jacobian + Hessian-norm surrogate) per audited cell (the
  named probe of record, findings :1288); full certificates only at flagged
  cells.
- V5 (composition): must compose with C20 — a seed certificate without
  branch discrimination cannot close the wrong-branch case (GAP-20's own
  coupling clause, findings :1284).

### 1.3 Materiality (§0-ter (c))

MATERIAL at the frontier: GAP-3's false-fail is a named candidate MECHANISM
inside the outcome-II certifiability-limited frontier of record — M0
:2352-2360 (re-read this window): "damped Newton stalls at HEALTHY-margin
cells", near-axis columns 23-30, mechanism identification OWNED BY F2; the
false-pass sits on the verdict-bearing O3.1 FD-probe replay path. A
conditioning-rejected converged cell at the frontier would be
manufacturing exactly the verdicts the program spends sessions
adjudicating. IMMATERIAL at everyday cells: record campaigns margin-
inactive (GAP-3 :161-164; GAP-20 :558-560); the incumbent metric is correct
in its regime. CONSEQUENCE (anti-over-engineering valve, both directions):
the right verdict shape is a TIERED stack — cheap always-on monitors +
gated heavier certificates — not wholesale replacement (no per-cell
interval arithmetic at production counts) and not leaving the frontier path
unqualified either.

### 1.4 Wave-1 consumption (binding)

VERDICT_wave1 §2.1 (C28): CONVERGED-ON-PROTOCOL, escalation NONE — consumed
directly, no conditional adjudication needed. Two clauses bind this
cluster: (i) "solvability regions re-scoped to the physical family
(wave-2)" — the O-F20 solvability-region half lands HERE (PANEL_C28.md
:398-402 verbatim: "RE-SCOPED, not adopted for frontier (ii) ... the
per-sector derivation program is O-F20's other half = wave-2 advocacy");
(ii) RC28-8: O-F20's falsifier trigger was never evaluated — NO provable
inner region was ever derived and no mu of record exists (O1 OPEN,
M0:2303-2306 current site — verdict-era anchor :2256-2259 drifted; O1 text
verbatim: "until discharged the margin-active KKT is B-STATIONARITY ONLY —
no multiplier mu is defined"); the re-scope stands on the measured S22
(v)/(vi) record. SHARED-SOURCE DECLARATION (brief §C2021 mandate): O-F20
is ONE tree fork feeding both C28 (how the frontier enters the
OPTIMIZATION — consumed in wave 1) and C20 (how a delivered certificate is
QUALIFIED — adjudicated here in §3.1-alt-5). Its advocacy is counted ONCE;
the two uses are different halves of the same fork, not two independent
validations.

### 1.5 Landed-row consumption (NEW in the reconcile — C9/C11/C56 of record)

The C9/C11 landing executed between the killed draft and this rewrite
(ledger re-read at source this window; row line anchors re-measured).
Three landed rows bear on this cluster:

- **C9 (choice_ledger.yaml:219-228, MIXED, wave-1 + SUPPLEMENT of record):**
  the supplement folded a THIRD adaptation arm R (fixed-count wall-station
  seed redistribution, frozen seed families) with F9b executed "via frozen
  pre-motion seed set". BOUNDARY DECLARED for C21: recorded-z replay
  presupposes IDENTICAL march topology AND identical seed set; seed
  validity under remeshing/seed-redistribution is F9b's object (frozen-
  topology / frozen-pre-motion-seed-set attribution re-runs), NOT C21's.
  C21's predicate applies at fixed topology + fixed seed set — the regime
  every verdict-bearing O3.1 replay of record runs in.
- **C11 (choice_ledger.yaml:240-250, MIXED, wave-1 + SUPPLEMENT of record):**
  two clauses land ON this cluster. (a) The estimator design leans on the
  object C20 qualifies: "same-level pairing signal-free at the certified
  Newton floor ([X-A1IM] per-cell z-space certification) so enrichment
  MANDATORY" — the DWR estimator architecture consumes the per-cell
  certificate's meaning; an unqualified false-PASS cell poisons that
  premise silently. (b) The DWR WEIGHT of record = DISCRETE AD-adjoint of
  the marched scheme (custom_vjp), with pin F11d two legs (oracle
  convergence; ACE compatibility residuals at band sites). Both F11d legs
  verify the weight GIVEN the computed root — they evaluate AT whatever
  root was solved, so ROOT IDENTITY at the estimator sites is a premise
  F11d cannot check. C20's Tier-0 branch monitor is the instrument that
  guards it (§3.4 dependency line extended).
- **C56 (choice_ledger.yaml:731-740, MIXED, minted at the C9/C11 landing):**
  the §0-bis axis-2 adjoint-realization question NOW HAS A LEDGER HOME —
  the draft's candidate ledger row is WITHDRAWN AS DEDUPED (§4.5). Owner
  field verbatim (:739): "weight role CLOSED (C11 supplement, F11d pinned);
  gradient role OWED TO wave-2 C31TRIO (forecast, not consumed ...);
  indicator role closed by transitivity". EXPLICIT STATEMENT (task-note
  discharge): the C56 GRADIENT-ROLE adjudication is NOT this panel's
  object — C2021 freezes no engine question (brief §C2021 questions =
  qualification + seed validity only); the gradient-role realization
  belongs to the C31TRIO reconcile panel per the row's own owner field and
  per brief §C31TRIO. What C2021 DOES adjudicate about C56 is the PREMISE
  every realization consumes at replay: gradient role, weight role and
  indicator role all linearize AT the replayed root, so all three inherit
  the root-identity blind spot until C20 Tier-0 lands (§3.4). This panel
  proposes a C56 note rider carrying exactly that (§4.3) — a premise
  guard, not a realization adjudication.

---

## 2. SOTA CENSUS (dated 2026-08-19)

### 2.1 Query protocol table (§0-ter (a))

Engine: WebSearch (US index), 2026-08-19. Counts = links returned /
screened at title+snippet level / included in §2.3. No installs, no page
fetches beyond the search results themselves (0 WebFetch calls).
RECONCILE NOTE: the killed draft's table is carried as the census of
record; the reconcile pass re-verified 4 load-bearing entries at source
same day (arXiv:2602.12940; arXiv:2208.05954; arXiv:1209.5704;
Breiding-Rose-Timme TOMS 2023/arXiv:2011.05000) — all four EXIST as
described at [ABS] depth; two one-liner details were trimmed to the depth
actually verified (declared in §2.3 and in the RECONCILIATION DECLARATION).

| # | Query string (VERBATIM) | hits | scr | incl |
|---|---|---|---|---|
| Q1 | a posteriori certification Newton solution conditioning kappa bound accepted root | 6 | 6 | 2 |
| Q2 | alpha theory Smale certified approximate zero software alphaCertified successor 2023 | 10 | 10 | 5 |
| Q3 | Kantorovich theorem ball radius warm start predictor seed Newton continuation validity | 9 | 9 | 3 |
| Q4 | affine covariant Newton a posteriori error estimate Deuflhard termination criterion last correction | 17 | 17 | 4 |
| Q5 | fold detection continuation smallest singular value monitor bifurcation test function production code | 9 | 9 | 4 |
| Q6 | deflation Newton distinct solutions Farrell Birkisson Funke branch switching avoid wrong root | 10 | 10 | 5 |
| Q7 | certification interval arithmetic Krawczyk HomotopyContinuation.jl certifying solutions Breiding Rose Timme | 10 | 10 | 4 |
| Q8 | method of characteristics supersonic nozzle marching Newton per-cell convergence certificate wrong branch interval | 10 | 10 | 0 |
| Q9 | real-time iteration warm start Newton contraction guarantee parameter perturbation bound predictor corrector MPC | 9 | 9 | 3 |
| Q10 | Yamamoto Kantorovich Mysovskikh error bounds Newton method historical survey a posteriori | 9 | 9 | 4 |

Communities covered: numerical algebraic geometry / validated numerics
(Q1/Q2/Q7), classical semi-local Newton theory incl. the RUSSIAN CLASSICAL
SCHOOL — Kantorovich 1948 is the school's root object, reached through the
theorem statement + the Yamamoto/Galantai/ACM-survey comparison corpus
covering Kantorovich/Ostrowski/Potra-Ptak lines (Q3/Q10; Mysovskikh named
in survey territory only — honest depth [TITLE], see §2.3); affine-
covariant German school (Q4); continuation/bifurcation software practice
(Q5/Q6); embedded/real-time optimization (Q9); the program's own MoC
territory (Q8 — precedent probe). Completeness is falsifiable against this
table: a family absent from all ten result sets can be named by a referee
and would extend the census (falsifier for §2.4's absence claims).

### 2.2 Corpus recency (per-axis newest, RC28-6 lesson: no blanket claim)

- Axis A (a-posteriori qualification / validated certification): newest
  2024 (interval alpha-theory over regions, ICMS 2024; certified homotopy
  tracking via Krawczyk, ISSAC 2024); anchor TOMS 2023.
- Axis B (branch discrimination / deflation): newest 2026
  (arXiv:2602.12940, existence re-verified this window: Kumar-Pichi-Rozza,
  submitted 2026-02-13) + 2025 (ff-bifbox, arXiv:2509.18429).
- Axis C (fold monitoring / continuation practice): newest 2024-2025
  (cusp CAPs arXiv:2404.00535; ff-bifbox 2025; BifurcationKit maintained
  docs); signed-sigma_min test function 2022.
- Axis D (seed/warm-start validity): newest 2021 (memory-based warm
  starting, Automatica) on the guarantees line; RTI lineage 2019 (AS-RTI)
  with active successors; plus 2023 continuation+validation instance
  (arXiv:2309.04320).
- Axis E (classical school): 1948 root; Yamamoto 1986; surveys 2000/2016.
Span: 1948-2026. Axes A-C reach >= 2023; axis D's guarantee layer stops at
2021 in this census (its modern refinements live in NMPC venues — a deeper
sweep is NOT needed for this cluster: the condition FORM, not the field's
frontier, is what C21 consumes).

### 2.3 Per-source one-liners (read-depth marked; §0-bis (b))

Validated certification / alpha-theory:
- [ABS] Hauenstein & Sottile, alphaCertified (Algorithm 921), ACM TOMS
  38(4), 2012 — Smale alpha-theory certificates for polynomial-system
  solutions, exact rational or arbitrary-precision float; the canonical
  point-estimate certifier (author preprint openly hosted).
- [ABS] Breiding, Rose & Timme, "Certifying zeros of polynomial systems
  using interval arithmetic", ACM TOMS 2023 (arXiv:2011.05000; RE-VERIFIED
  at source this window) — Krawczyk-method certification "dramatically
  outperforms" exact-arithmetic approaches; built into
  HomotopyContinuation.jl `certify`; one-sided semantics (not-certified
  does NOT imply no zero) — the modern doctrine that certification can be
  "the default, not just an option".
- [ABS] "Certified homotopy tracking using the Krawczyk method", ISSAC
  2024 (arXiv:2402.07053) — a-priori certified tracking, Krawczyk-based.
- [ABS] "Effective Alpha Theory Certification Using Interval Arithmetic:
  Alpha Theory over Regions", ICMS 2024 (arXiv:2405.04842; LNCS ch.
  978-3-031-64529-7_29) — alpha certificates over regions via interval
  arithmetic to avoid exact-arithmetic cost.
- [ABS] NumericalCertification (Macaulay2), arXiv:2208.01784 (2022) —
  alpha-theory + Krawczyk + deflation-based soft certification for
  singular solutions in one package.
- [ABS] "An a posteriori certification algorithm for Newton homotopies",
  ISSAC 2014 — certify-after-heuristic-tracking pattern (the shape of our
  replay-then-qualify problem).
- [ABS] Numerical certification (Wikipedia overview) — a-priori vs
  a-posteriori taxonomy; alpha-theory and Newton-Kantorovich as the two
  standard a-posteriori instruments.

Classical semi-local theory (incl. Russian school):
- [ABS] Kantorovich theorem (statement + constants: h = eta*omega <= 1/2,
  rho_- = (1 - sqrt(1-2h))/omega) — the root object (Kantorovich 1948).
- [ABS] Ferreira & Svaiter, "Kantorovich's Theorem on Newton's Method"
  (arXiv:1209.5704; RE-VERIFIED at source this window) — majorant-function
  proof defining "good regions" and an INVARIANT SET for Newton iteration
  (any seed in the invariant ball iterates safely) — the seed-ball form
  C21 needs. RECONCILE REPAIR (depth honesty): the draft's "ROBUST version
  ... ANY starting point in a prescribed ball" wording is re-anchored to
  the verified abstract (good regions + invariant set); the explicitly
  "robust" companion surfaced this window is Ferreira-Goncalves-Svaiter's
  robust-Kantorovich line for inexact Newton (arXiv:1110.3430, [ABS]) —
  added to the corpus and the registration rider.
- [ABS] Yamamoto, "A method for finding sharp error bounds for Newton's
  method under the Kantorovich assumptions", Numer. Math. 49 (1986) —
  sharp a-posteriori bounds; compares Dennis/Doring/Gragg-Tapia/
  Kantorovich/Ostrowski/Potra-Ptak/Miel/Moret — the comparison corpus of
  the classical school.
- [ABS] "A short survey on Kantorovich-like theorems for Newton's method",
  ACM Comm. Computer Algebra 50(1), 2016 — historical notes + pointers to
  recent refinements.
- [ABS] Galantai, "The theory of Newton's method", JCAM 124 (2000).
- [TITLE] Mysovskikh convergence-condition line — named in the survey
  corpus; not screened beyond title level in this census (claims about it
  are NOT made below).

Affine-covariant a-posteriori (the incumbent's own theory family):
- [ABS] Deuflhard, "Newton Methods for Nonlinear Problems: Affine
  Invariance and Adaptive Algorithms", Springer CSM 35 — affine-covariant
  a-posteriori estimates; the last-Newton-correction error estimate (the
  incumbent's step test IS this family's natural criterion); natural
  monotonicity + Kantorovich quantities. FULL TEXT NOT HELD -> PAPERS
  NEEDED (the Tier-1 derivation waits on it).
- [ABS] Ern & Vohralik, "Adaptive inexact Newton methods with a posteriori
  stopping criteria for nonlinear diffusion PDEs", SISC 2013 — component-
  split a-posteriori stopping (discretization/linearization/algebra).
- [ABS] "The Grand Four: Affine Invariant Globalizations of Newton's
  Method", Vietnam J. Math. 2018.

Branch discrimination / deflation / fold monitoring:
- [ABS] Farrell, Birkisson & Funke, "Deflation techniques for finding
  distinct solutions of nonlinear PDEs", SISC 2015 (10.1137/140984798;
  arXiv:1410.5620) — systematic residual modification removing known
  roots; converges to OTHER solutions from the same seed; the root-
  discrimination instrument (already named in gapmap GAP-3 SOTA line
  :157-160).
- [ABS] "Deflation for semismooth equations", Optim. Methods Softw. 2019.
- [ABS] ff-bifbox, arXiv:2509.18429 (2025) — scalable open-source
  bifurcation toolbox (production practice).
- [ABS] "Bifurcation curve detection with deflation for multiparametric
  PDEs", arXiv:2602.12940 (2026; RE-VERIFIED at source this window:
  arclength continuation + deflation + zigzag curve tracking,
  Bratu/Allen-Cahn benchmarks) — deflation as detection instrument,
  newest item in this census.
- [ABS] BifurcationKit.jl documentation — minimally-augmented fold
  continuation; detect_bifurcation with bisection localization: fold
  monitoring as PRODUCTION-code practice.
- [ABS] "Spatially quasi-periodic bifurcations from periodic traveling
  water waves and a method for detecting bifurcations using signed
  singular values", arXiv:2208.05954 (2022; RE-VERIFIED at source this
  window) — SIGNED smallest-singular-value test function: sigma_min has a
  slope discontinuity at its zero, but with a sign factor (product of the
  determinants of the SVD's orthogonal factors) the test function is
  SMOOTH through the fold and admits root bracketing — the modern form of
  the V-F7 monitor. RECONCILE REPAIR (depth honesty): the draft's
  "computed cheaply from the bidiagonal" detail is NOT confirmed at [ABS]
  depth and is removed.
- [ABS] "Cusp bifurcations: numerical detection via two-parameter
  continuation and computer-assisted proofs", arXiv:2404.00535 (2024);
  [ABS] "Determination of stable branches of relative equilibria of the
  N-vortex problem", arXiv:2309.04320 (2023) — continuation + a-posteriori
  validation (Newton-Kantorovich) as the modern combined practice.

Warm-start / seed validity (industrial line):
- [ABS] Real-Time Iteration lineage (Diehl et al.; auto-generated RTI in
  the microsecond range) — ONE warm-started Newton step per sample with
  LOCAL CONTRACTION guarantees under bounded parameter drift: the modern
  industrial form of C21's replay-seed premise (seed valid iff drift stays
  inside the contraction region).
- [ABS] Nurkanovic et al., "The Advanced Step Real-Time Iteration for
  NMPC" (2019) — predictor-corrector variant with strengthened contraction
  guarantees.
- [ABS] "Online learning with stability guarantees: memory-based warm
  starting for real-time MPC", Automatica 2021 — warm-start validity as a
  first-class guaranteed property. (Aggregator topic pages that surfaced
  in Q9 were NOT leaned on.)

### 2.4 Absence claims (query-bounded), cava rows, dedup greps
(ALL greps below re-run in THIS window — SR-12; hit sets are the measured
ones of this reconcile, superseding the draft's.)

MoC-precedent ABSENCE (Q8): 10 hits, all design tutorials/toolbox pages/
patents; ZERO items on per-cell Newton certificate qualification, branch
identity, or seed-validity certificates inside an MoC marching design
code. CLAIM (bounded by Q1-Q10): no published production MoC/marching
design line was found that qualifies its per-cell nonlinear-solve
certificates or certifies seed validity — the same shape as PANEL_C28's
no-precedent finding for priced certification (its census, :394-396).
Wave-1's judged precedent stands: these audits are work the published SOTA
never did.

CAVA (validation/ADVISORY_litreview_confrontation_2026-08-13.md), per the
RC27-5 bilingual lesson — two greps re-run this window, hit lists measured:
- Pattern `Kantorovich|alpha-theory|alpha theory|Deuflhard|interval-Newton|
  Krawczyk|Smale` -> 0 hits (re-measured: 0).
- Pattern `C20|C21|certificat|Newton|seed|seme|continuazione|piegatura|
  fold` -> measured hits {21, 86, 331, 414, 730, 840, 891, 983, 1023-1060
  (table block: 1023, 1024, 1027, 1029-1031, 1035-1036, 1039, 1044, 1047,
  1049, 1054, 1060), 1074, 1108, 1109, 1117, 1144, 1188, 1199, 1202, 1205,
  1233, 1242, 1247, 1261}. Inspected at source this window: :21 ("§6
  (C20)") and :1188 (D-13 "C1-C21") are the cava's OWN internal numbering —
  the same numbering-collision family RC28-7 adjudicated for C28;
  certificate-token hits are discipline-level rows (A12 wall-residual
  re-expression :1031; A20 Floquet certificate :1205; D-22 third
  certificate class :1202; A27 sonic minimality :1233; D-47
  dual-feasibility/seed-rejector discipline :1242 — "seed rejector
  dimostrato sparare" verbatim) — none adjudicates per-cell Newton
  qualification or seed validity; "seed" hits are D-19 (design-space CTP
  seeding :1199) and D-47 (rejector-demonstration discipline) — different
  objects. CONCLUSION: the cava contributes NO row to this cluster;
  nearest-adjacent = D-47, CONSUMED here as the falsifier-style
  requirement V3 (rejector demonstrated firing).

Registry dedup greps (re-run this window):
- docs/literature_registry.yaml, pattern `Deuflhard|Kantorovich|
  alpha-theory|Hauenstein|Farrell|deflation|Smale|Krawczyk|Rump|INTLAB|
  Moore|Kearfott` -> 0 hits EVEN AFTER the wave-1/C9C11 landing added its
  DWR-canon rows: NONE of this cluster's census canon has a registry row
  (registration rider in §4.6).
- docs/claims_registry.yaml, pattern `Kantorovich|alpha-theory|Krawczyk|
  deflation` -> measured hits {1753, 1754, 1766}: X-IVXC (:1749-1761,
  Krawczyk verified linear solve, outward-rounded arithmetic, PASS of
  record 2026-08-05) and PAP-GMAX (:1763-1774, deflation+exclusion as a
  certified GLOBAL-MAX route family — design-space level, different
  insertion point: cited, not re-minted).
- docs/rde_nozzle_MASTER.md, pattern `Kantorovich|kappa\(J\)|conditioning|
  wrong-branch|wrong branch` -> 1 hit (:2357, "spline conditioning" in the
  S20 candidate list) — M0 has NO qualification formalization: unlike C28
  (ledger lagged M0), here ledger and M0 agree the rows are genuinely
  NEVER; the R4 back-propagation of this panel's architecture is therefore
  part of the duty.
- docs/findings_registry.yaml, patterns `replay` (measured hits {217, 331,
  349, 571, 636, 1148, 1225, 1270, 1284, 1519}) and `custom_vjp|IFT`
  (measured hits {326, 1489, 1494, 1936}) -> every hit inspected; the
  coupling rows consumed in §3.4: engine-core:F2-cert-record-only
  (:564-572, DISCHARGED, residual [X-SCANM] old-path probes),
  oracles:o31-common-mode-hole (:1486-1494, [X-O31CS] complex-step IFT
  twin, interior-only), engine:cross-lowering-gradient-floor (:328-336).
  The two post-draft hits are audit-scert:xcdkat-record-numbers-drift
  (:1519, staleness mechanism) and litreview:graft-a21-a22-a23 (:1936,
  checkpointing) — neither adjudicates root identity at replay; a
  dedicated grep `root.identity|wrong-branch|wrong branch|branch.consist`
  returns ONLY the two cell-cert rows of this cluster (:1148, :1152,
  :1284). The §4.5 candidate findings row remains unminted anywhere.
- [X-TBAK] of record: claims_registry.yaml:1360-1372 — W-space tolerance-
  ball THEOREM+PRACTICE stack, measured-sup two-point K_RICH surrogate
  L_TB; the "pattern in z" the C21 ledger row names (row re-read verbatim
  this window).

### 2.5 Per-row §0-bis axis bearing (§0-ter (f))

- Axis 1 (optimizer query-level choice): does NOT bear on either row —
  C20/C21 live inside the STATE solve below any design optimizer; the only
  contact is qualification cost riding every engine iteration (named to
  the C31TRIO cluster, not adjudicated here).
- Axis 2 (discrete vs continuous adjoint; custom_vjp consistency): BEARS
  on both rows — the custom_vjp IFT adjoint and the O3.1 FD legs both
  presuppose ROOT IDENTITY at the replayed solution; C20/C21's monitors
  are the guards of that premise (emergent finding, §3.4; candidate
  FINDINGS row §4.5). RECONCILE UPDATE: the adjoint-REALIZATION question
  now HAS a ledger home — C56 minted at the C9/C11 landing (:731-740,
  re-read this window); the draft's candidate LEDGER row is withdrawn as
  deduped (§4.5); gradient role = C31TRIO's object (§1.5 explicit
  statement); this panel contributes the premise guard via a C56 note
  rider (§4.3).
- Axis 3 (moving-mesh / r-adaptive): does not bear beyond the landed C9
  row's pins — recorded-z replay presupposes IDENTICAL march topology AND
  (post-supplement) identical seed set; adapted-mesh/redistributed-seed
  laws are governed by F9b's frozen-topology / frozen-pre-motion-seed-set
  attribution tests (C9 row :228, landed; VERDICT_wave1 §2.3); seed
  validity under remeshing is F9b's object (named, not decided here).
- Axis 4 (adjoint-free routes): marginal bearing — the O3.1 FD probes are
  themselves derivative-free verification instruments and are exactly the
  exposed replay path; a DFO/BO design loop would still need C20/C21's
  primal qualification (certificates are optimizer-agnostic); no census
  family substitutes qualification with adjoint-freeness.
- Axis 5 (emergent sub-aspects named): (i) root-identity blindness of the
  common-mode adjoint/FD pair at replay (§3.4, candidate findings row) —
  post-landing this premise is consumed by THREE roles of C56 plus C11's
  estimator sites; (ii) the RTI/warm-start condition form absorbed into
  pin F-C21-2; (iii) deflation as explicit twin-root constructor absorbed
  at diagnostic tier (§3.1).

---

## 3. ADJUDICATION

### 3.1 Row C20 — certificate qualification (ledger :336-347 current site
(draft-era :334-345 drifted at the landing), NEVER, owner F2 HIGH)

INCUMBENT'S GENUINE CASE (represented, it may win): the one-extra-step
ratio is a UNIT-CONSISTENT z-space step test — the docstring's argument
against raw-residual tests is correct (residual rows mix units, :796-798);
it is the affine-covariant family's natural "last correction" criterion
(Deuflhard line, census §2.3); it costs one step-norm per cell; it carried
every campaign of record; it gained C2-F1 NaN-forcing (:814-818), C2-F2
CERT_PLAY replay coverage (:802-810) and the M5b typed early-abort
(:821-828). Its failure modes are TOY-measured only (Q3 quarantine,
findings :1154) and record campaigns ran margin-inactive. The incumbent is
the RIGHT base metric in its regime.

WHAT CONVICTS "UNQUALIFIED" (stated reasons, not vibes): (1) the
contraction hypothesis it claims (:801) is never checked — findings row
CONFIRMED HIGH :1145-1154; (2) both failure modes are measured on the toy:
false FAIL at ratio 25 on an exact root (1/|J| roundoff amplification),
false PASS at ratio 0.0 on the wrong branch — and the false-pass sits on
the verdict-bearing O3.1 replay path where [X-CDKAT] and CERT_PLAY are
structurally blind to it (findings :1148 verbatim); (3) the S25-bis GAP-29
sweep measured NEWTON_TOL_FACTOR/2 FLIPPING cert_verdict (C18 row note,
ledger :315-324 current site — the factor sits on a measured cliff,
underived); (4) the frontier of record is numerical-class at HEALTHY
physical margins (M0:2352-2360) — exactly where an unqualified
conditioning-blind certificate can manufacture outcome-II verdicts.

ALTERNATIVES, EACH AT ITS BEST (steelman, §0-ter (d)):

1. kappa(J)-aware derived band (ledger alt 1). Best instance: the
   attainable-accuracy qualification eps*kappa(J) — the false-FAIL
   mechanism IS this amplification; affine-covariant a-posteriori theory
   (Deuflhard; Ern-Vohralik component split) is its published form.
   OUTCOME: ADOPTED-FOR-MEASUREMENT as Tier 1, COMPOSED with the incumbent
   metric (it qualifies the SAME measurement; W1-half false-fail, W2-W5
   pass). It cannot see branch identity (W1-half false-pass FAILS) — never
   sufficient alone. Derivation duty shared with the C18 window (the
   factor-100 cliff gets derived in the same pass); Deuflhard full text =
   procurement ask (avoid an R-4-grade mis-transplant of the omega
   estimates).
2. Branch-consistency monitor (ledger alt 3; GAP-3's named form: sign
   det J / den-sign continuity along the march DAG). Best instance:
   deflation lineage for root discrimination (FBF SISC 2015 -> semismooth
   2019 -> 2025/2026 production toolboxes) + signed-sigma_min test
   functions (2022) as the smooth fold-crossing detector. OUTCOME: ADOPTED
   -FOR-MEASUREMENT as Tier 0 (always-on): the ONLY family addressing
   false-PASS at O(1) cost reusing the formed J (W1 false-pass leg, W3,
   W4). HONESTY CLASS: a NECESSARY-condition rejector, not a certificate —
   at a simple fold the two meeting branches carry opposite det signs
   (local discrimination is generic), but same-sign wrong-branch pairs
   away from simple folds can evade it (pin F-C20-4 makes this its own
   falsifier). Deflation itself = DIAGNOSTIC tier (explicit construction
   of the twin root at flagged cells; too heavy always-on; dedup: the
   design-space deflation family in PAP-GMAX is a different insertion
   point, cited).
3. Kantorovich / alpha-theory (ledger alt 2). Best instance: alphaCertified
   (TOMS 2012) and the 2024 interval-alpha refinement; Kantorovich
   seed-ball forms (Ferreira-Svaiter majorant/invariant-set line).
   OUTCOME: role-split — LOSES the always-on role by W3/LOSS (per-cell
   exact or higher-derivative machinery at production counts; the 2024
   line reduces but does not erase the cost) — WINS the flagged-cell
   a-posteriori role sharing its constants with C21's seed certificate
   (§3.2-alt-2/3: same eta/omega objects, one build).
4. Interval-Newton [X-IVXC] (ledger alt 4). Best instance: Krawczyk
   certification as shipped default in HomotopyContinuation.jl (BRT TOMS
   2023: "dramatically outperforms" exact arithmetic — re-verified at
   source this window; ISSAC 2024 tracking). OUTCOME:
   ADOPTED-FOR-MEASUREMENT as the REFEREE tier at flagged cells: the only
   POSITIVE existence+uniqueness certificate in a box — hence the only
   positive branch-identity instrument (uniqueness box excluding the twin
   root). In-house machinery exists and PASSed of record ([X-IVXC] claims
   :1749-1761); per-cell 4x4 Krawczyk is O(1) interval arithmetic —
   whether it can be promoted from referee to always-on is a MEASURED
   question the duty answers (not pre-committed).
5. Solvability-region pre-qualification (diff's ENRICHING mechanism,
   O-F20 option 5 + recommendation, phaseA_tree_optimization.md:1111-1127;
   falsifier :1129-1133 — both re-read verbatim this window). Wave-1
   consumption per §1.4; shared source declared. OUTCOME: CLOSED as a C20
   qualification mechanism, by stated reason: (i) CATEGORY MISMATCH — it
   pre-qualifies EXISTENCE of a smooth marching solution, it cannot
   qualify a DELIVERED numerical root (both measured failure modes occur
   at physically healthy states: conditioning and branch identity are
   invisible to physical-region reasoning); (ii) the measured record
   already shows the binding frontier is numerical-class at healthy
   margins (M0:2352-2360 — the same evidence C28's re-scope stands on,
   RC28-8); (iii) no provable inner region exists today (RC28-8: the
   derivation was never done, O1 OPEN, M0:2303-2306 current site).
   ABSORBED as an exposure-reduction ANNOTATION: inside a future provable
   region, a qualification failure is attributable to numerics by
   construction — diagnostic value, zero certificate value. The physical-
   family derivation program itself = candidate THEORY duty riding C28's
   re-scope (§4.5 item 3), NOT a C20 blocker. No double-counting: O-F20
   counted once (§1.4).
6. (Census-added) exact/rational alpha certification always-on
   (alphaCertified mode). CLOSED for the always-on role by W3/LOSS at its
   best modern instance (the 2024 interval-alpha paper exists precisely
   because the exact-arithmetic cost is prohibitive); lives inside
   option 3's flagged-cell role.

### 3.2 Row C21 — seed validity policy (ledger :349-358 current site
(draft-era :347-356 drifted at the landing), NEVER)

INCUMBENT'S GENUINE CASE: the predictor is the GENO Ch.16 foot-state twin
(cross-code exactness; traced twin `predict_interior_t` shipped
GATE-verified S25-bis with DECLARED ulp divergence — an implementation
delta, not an adjudication, exactly as the ledger note records at :358
current site); O(h) is textbook-true for the predictor-corrector pair at
smooth cells; the recorded-z replay seed is the EXACT solution at
unperturbed p — the best possible seed there; C2-F2/CERT_PLAY certifies
the replayed SOLVE (though not the branch). The gap is real but localized:
PERTURBED replay (O3.1, h_FD = 6.1e-6) near folds where the basin
(~sqrt(dist-to-fold)) undercuts the perturbation, plus the wrong-branch
invisibility (GAP-20 :551-572; findings :1281-1289).

ALTERNATIVES, EACH AT ITS BEST:

1. alpha-theory per-seed certificate (ledger alt 1). Best: alphaCertified/
   2024-interval-alpha — certifies from the SEED that Newton converges
   quadratically to the associated zero (the "approximate zero" notion is
   literally C21's predicate). OUTCOME: role-split by V4 — the FULL alpha
   test is flagged-tier; the production form is option 2's surrogate
   (below), which is the same mathematics with measured constants.
2. Kantorovich radius, [X-TBAK] pattern in z (ledger alt 2). Best:
   Kantorovich seed-ball forms — Ferreira-Svaiter majorant "good regions"
   + invariant set (arXiv:1209.5704, re-verified this window), the robust
   inexact-Newton companion line (arXiv:1110.3430, [ABS]), and Yamamoto's
   sharp a-posteriori bounds; in-house precedent [X-TBAK] (claims
   :1360-1372) = the two-point K_RICH-safeguarded measured-Lipschitz
   surrogate, THEOREM-anchored, already of record in W-space. Constants
   computable on the stack: eta = norm of the FIRST Newton step from the
   seed (already computed by the solver); omega = two-point measured
   surrogate in z (the transplant the ledger row itself names). OUTCOME:
   ADOPTED-FOR-MEASUREMENT as the derived-radius instrument (V1/V2/V4
   pass; V3 = duty demonstration); radius
   r_K = (1 - sqrt(1 - 2*eta*omega))/omega on the intended-root ball;
   NOTE for C42: transplanting the K_RICH two-point pattern to z adds a
   NEW K_RICH role — notified to the wave-3 audit (RC27-8(iv) precedent),
   not adjudicated here.
3. Continuation-defined branch + fold-margin monitor (diff's ENRICHING
   family, :113-115; V-F7 = phaseA_tree_variational.md:373-404, monitor
   inf_xi sigma_min :395-398 — re-read verbatim this window). Best modern
   instance: BifurcationKit's minimally-augmented fold machinery + the
   2022 signed-sigma_min smooth test function + the RTI warm-start
   contraction line (census §2.3). OUTCOME: ADOPTED-FOR-MEASUREMENT as
   the always-on INSTRUMENT: per-cell scaled fold margin (sigma_min of
   the 4x4 J, or |det J| against its row-norm product as the cheap proxy —
   choice measured by the duty) monitors basin shrink continuously; the
   RTI line supplies the modern condition FORM for replay validity (drift
   bound vs contraction region) absorbed into pin F-C21-2. TRANSFER
   DECLARED: V-F7's native context is xi-continuation branch selection
   for F's definition (hysteresis); the diff transfers it to march-cell
   seed validity — the transfer is the adopted reading HERE; the xi-level
   fold monitor of V-F7 itself belongs to the M0 VI.4bis monitor family
   (named, not decided).
4. (Census-added) per-instance fresh re-record at perturbed p (RTI-style
   "advance step" analog). OUTCOME: ADOPTED as the named FALLBACK when
   F-C21-2 finds uncovered probe cells (the mitigation is already
   structurally available: record mode exists; cost = one record per probe
   direction at flagged instances).

### 3.3 Composed architecture (the convergence, both rows)

- Tier 0 (always-on, record + replay, O(1)/cell reusing the formed J):
  branch-consistency monitor (sign det J + den-sign continuity along the
  march DAG) + scaled fold-margin monitor with derived floor. Serves C20
  (false-pass rejector) and C21 (basin-shrink instrument) — ONE build,
  declared ride (the C9/C11 composition pattern of record).
- Tier 1 (C20): kappa(J)-aware derived band composed with the incumbent
  step metric; derivation shared with the C18 constants window; itemized
  reclassification only.
- Tier 2 (flagged cells): per-seed Kantorovich certificate (eta from first
  Newton step, omega = [X-TBAK]-pattern two-point K_RICH surrogate in z)
  for C21 + the same constants as C20's flagged-cell a-posteriori bound;
  Krawczyk/[X-IVXC] enclosure as the positive branch-identity REFEREE;
  deflation as diagnostic twin-root constructor.
- Policy: incumbent metric and seeds RETAINED as base layer; the labels
  "unqualified"/"asserted O(h)"/"stale replay unexamined" SUPERSEDED by
  the monitored + qualified stack; P4 absolute; floor unmoved; adoption of
  record gated on the F2 measured half.

### 3.4 Emergent cross-cutting finding (axis 2/5; §0-bis (a)(5))

ROOT-IDENTITY BLIND SPOT, COMMON-MODE: wave-1's C28 pin F-1 assumes the P4
gate catches what the KS-max surrogate misses. For the WRONG-BRANCH mode
this assumption fails STRUCTURALLY: gate and surrogate consume the same
unqualified ratio, and the ratio is 0.0 at a converged wrong-branch root —
NEITHER fires. Worse, on the replay path the custom_vjp IFT adjoint
linearizes AT the replayed root: a wrong-branch replay poisons the
adjoint AND the FD legs coherently (common-mode), so O3.1 self-consistency
passes — the same class as oracles:o31-common-mode-hole (:1486-1494) one
level up: ROOT identity instead of operator-pair identity ([X-O31CS]
cannot see it either: it verifies the adjoint of whatever root was
solved). RECONCILE EXTENSION (landed rows, §1.5): the SAME premise is now
consumed by every adjoint ROLE of record — C56's weight role (the C11
supplement's discrete AD-adjoint DWR weight and BOTH F11d legs evaluate at
the computed root; F11d verifies the weight GIVEN the root, never the
root's identity), C56's indicator role (same object by the row's
transitivity clause), and C56's gradient role (whatever realization
C31TRIO adjudicates); plus C11's estimator premise "signal-free at the
certified Newton floor", which cites the very certificate C20 qualifies.
CONSEQUENCE (dependency lines, mirroring wave-1's C27 -> C28):
**C20 -> C28** AND **C20 -> C56/C11-estimator**: the priced field r_i(W),
the absolute verifier, and every adjoint-role realization inherit GAP-3's
blind spot until Tier 0/1 land; the branch monitor is the instrument that
RESTORES F-1's discriminating assumption on the wrong-branch mode and
guards the F11d premise at estimator sites. Notified to the [P-CERTKS]
duty (§4.4) and proposed as a C56 note rider (§4.3). Candidate findings
row in §4.5 (dedup re-measured §2.4 — no existing row covers root identity
at replay).

---

## 4. PROPOSED VERDICTS + DUTIES

### 4.1 Row C20 — proposed outcome

**Measurement-gated CONVERGED-ON-PROTOCOL.** Formal half converged now:
the qualification ARCHITECTURE of §3.3 (Tier-0 branch/fold monitors +
Tier-1 kappa-derived band composed with the retained incumbent metric +
Tier-2 flagged-cell Kantorovich/Krawczyk referee; solvability-region
pre-qualification CLOSED as qualification mechanism and absorbed as
annotation). Adoption of record = ADOPTED-FOR-MEASUREMENT behind the F2
duty. Proposed status: NEVER -> "ADJUDICATED-SPLIT (architecture converged
2026-08-19 wave-2; qualification adoption gated on F2-C20-CERTQUAL-
CAMPAIGN)". Owner unchanged (F2 HIGH).

Pinned protocol + falsifiers:
- **F-C20-1 (discrimination carrier):** the GAP-3 near-fold toy family is
  COMMITTED as a carrier with test (RC28-2 lesson: no scratchpad-class
  numbers into Verdicts); the qualified stack must ACCEPT the exact-root
  case the incumbent false-fails (ratio 25) AND REJECT the wrong-branch
  case it false-passes (ratio 0.0). Either miss => that tier is refuted;
  the incumbent stays with its blindness DECLARED in-row and the row
  re-opens.
- **F-C20-2 (no silent reclassification):** re-run ONE recorded S18 march
  + ONE deep-DEF defnoz plan (the named probe of record, findings :1152)
  under the qualified certify: every verdict flip itemized per cell; any
  FAIL->PASS flip ships measured kappa + the band's derivation arithmetic;
  any PASS->FAIL flip on a verdict-bearing record => escalation (prior
  verdicts FLAGGED, not voided — the RC911-11 honesty pattern). A
  FAIL->PASS flip at an outcome-II frontier cell = the candidate MECHANISM
  of record confirmed (report feeds the F2 mechanism identification that
  M0:2358-2360 owns).
- **F-C20-3 (cost gate):** monitored+qualified certify at production
  counts within a threshold DERIVED from the recorded M-chain baselines;
  the derivation (sites, measured baseline, implied threshold) is
  PUBLISHED by the duty BEFORE first use (RC911-3 pattern).
- **F-C20-4 (monitor honesty):** the branch monitor is a necessary-
  condition rejector: a planted same-sign wrong-branch pair passing
  sign-continuity => monitor demoted to diagnostic and the Krawczyk
  referee becomes MANDATORY at that exposure class.
- Reporting pins: cert_worst keeps its meaning; qualified verdicts carry
  {ratio, kappa-band, monitor state}; every number with committed script +
  derived band (R5).

**BINDING F2 duty: `F2-C20-CERTQUAL-CAMPAIGN`** — Tier-0 monitor build
(shared with C21, declared ride) + Tier-1 derivation (window shared with
the C18 constants derivation duty — the GAP-29 factor-2 cliff is the same
question) + committed toy carrier + itemized S18/defnoz re-run + cost
gate + M0 back-propagation of the architecture (R4: M0 currently has NO
qualification formalization — grep §2.4, re-measured this window).

### 4.2 Row C21 — proposed outcome

**Measurement-gated CONVERGED-ON-PROTOCOL.** Formal half converged now:
seed-validity policy = Tier-0 monitors (always-on) + derived Kantorovich
radius in z ([X-TBAK] two-point pattern; eta from the first Newton step)
at audited/flagged cells + O3.1 replay-ball coverage requirement + fresh
re-record fallback; predictor and replay seeds RETAINED as base layer;
"asserted O(h)" retired as an assertion (measured or deleted, F-C21-4).
Proposed status: NEVER -> "ADJUDICATED-SPLIT (policy converged 2026-08-19
wave-2; measured half gated on F2-C21-SEEDCERT-CAMPAIGN)". Owner
alignment proposed at landing: "S25 probe -> F2 ledger row" -> "F2" (the
S25 probe window was consumed by the speed program — findings :1152/:1288
record it; bookkeeping alignment, the RC911-1/C43 pattern at note level —
C43's landed row :583-591 is the executed precedent of exactly this
pattern). SCOPE BOUNDARY (landed C9, §1.5): C21's predicate holds at
fixed march topology + fixed seed set; seed validity under F9a-R seed
redistribution or AC2 insertion is F9b's object (named, not decided here).

Pinned protocol + falsifiers:
- **F-C21-1 (fire test):** per-cell Kantorovich/alpha audit over EVERY
  recorded cell of the S18 baseline + defnoz plans (the findings :1288
  probe verbatim: one Jacobian + Hessian-norm surrogate per cell): must
  stay quiet at everyday cells (fire rate ~ 0 within a derived band) AND
  FIRE on planted frontier cells (near-fold + razor-thin near-sonic start
  — GAP-20's exposure classes :564-567). Zero fire on planted cells =>
  certificate vacuous => NOT adopted (cava D-47 discipline consumed:
  rejector demonstrated firing).
- **F-C21-2 (replay-ball coverage, the RTI condition form):** at every
  O3.1 probe cell, derived r_K(recorded z; p) must cover the measured
  perturbation |z(p + h_FD e) - z(p)| per probe direction. An uncovered
  cell that ALSO trips the branch monitor at replay => the stale-replay
  premise is REFUTED of record for that instance class => the fresh
  re-record fallback (§3.2-alt-4) is MANDATED on that probe path.
- **F-C21-3 (monitor-vs-basin law):** the fold-margin monitor must
  reproduce the sqrt(dist-to-fold) basin scaling on the toy family + one
  recorded near-fold family within derived bands; failure => monitor
  demoted to diagnostic (it cannot underwrite validity claims).
- **F-C21-4 (label hygiene, cheap, rides the duty):** the predictor's
  O(h) becomes a MEASURED statement (predictor-to-root distance vs da
  scaling on record marches) or the assertion is deleted from comments
  (R5).

**BINDING F2 duty: `F2-C21-SEEDCERT-CAMPAIGN`** — omega-surrogate build in
z ([X-TBAK] transplant; K_RICH role delta NOTIFIED to C42) + the :1288
audit + F-C21-1/2/3/4 execution + fire-rate report. SHARES the Tier-0
monitor build with F2-C20-CERTQUAL-CAMPAIGN (one artifact, both duties
declare the ride — no duplicate build).

### 4.3 Proposed ledger deltas (proposals only — landing window applies;
row line anchors re-measured this window)

- C20 (docs/choice_ledger.yaml:336-347): status + note append per §4.1;
  note names: architecture tiers, solvability-region CLOSED-as-mechanism/
  absorbed-as-annotation with the C28 shared-source declaration
  (VERDICT_wave1 §2.1 + RC28-8 cited), pins F-C20-1..4, duty name, C18/C19
  interplay named-not-decided, the C20 -> {C28, C56/C11-estimator}
  dependency lines (§3.4).
- C21 (docs/choice_ledger.yaml:349-358): status + note append per §4.2;
  note names: retained incumbents, derived-radius instrument, V-F7
  transfer declared, pins F-C21-1..4, duty name, owner alignment, C42
  K_RICH role notification, F9b scope boundary (landed C9).
- C18 (:315-324, note line only): "C20 wave-2 verdict shares the Tier-1
  derivation window: the kappa-qualified band and the NEWTON_TOL_FACTOR
  derivation are one question (GAP-29 factor-2 cliff)." Named, not
  adjudicated.
- C42 (:573-581, note line only): K_RICH role-count delta from the
  [X-TBAK]-pattern transplant to z (omega surrogate) — notification, no
  role adjudicated (RC27-8(iv) precedent; appends to the wave-1
  notification already landed in the row).
- C28 duty rider ([P-CERTKS]; row :421-429): the §3.4 dependency line —
  the priced r_i(W) field inherits GAP-3's blind spot until C20 Tier-0/1
  land; F-1's wrong-branch discrimination requires the branch monitor.
- C56 (:731-740, note line only, NEW in the reconcile): "C2021 wave-2
  premise guard: ALL three roles (gradient/weight/indicator) linearize at
  the replayed root and inherit the GAP-3 wrong-branch blind spot until
  C20 Tier-0 lands (PANEL_C2021 §3.4); F11d verifies the weight GIVEN the
  root, not root identity — the branch monitor guards F11d's premise at
  estimator sites. Gradient-role adjudication NOT consumed here — owed to
  wave-2 C31TRIO per this row's owner field." Notification, no role
  adjudicated by this panel.

**ledger_deltas_proposed: 6** (C20, C21, C18-note, C42-note, C28-duty-
rider, C56-note) + one literature rider (§4.6).

COUNTING RULE for alternatives_closed (stated per the wave-1 judge's
RC27-8(vi)/RC911-14(i) precedent): each option-FAMILY counted once per
row where it competes, every disposition-by-stated-reason counted
(adopted-for-measurement, role-split, absorbed, closed, retained-with-
supersession all count; silent omission counts as zero and is a defect).
C20 = 8 (incumbent, kappa-band, branch-monitor, Kantorovich/alpha,
interval-Newton, solvability-region, exact-alpha-always-on [census-added],
deflation-diagnostic [census-added]); C21 = 6 (incumbent, alpha per-seed,
Kantorovich radius, fold-margin/continuation, fresh-re-record fallback
[census-added], RTI condition form [census-added, absorbed into F-C21-2]).
Total 14. (The C56 consumption is a premise-guard coordination item, not
an alternative of either row — not counted.)

### 4.4 Cross-cluster consistency (declared)

C20 -> C28 dependency direction mirrors wave-1's C27 -> C28 ("inherits the
defect if underived"): the certification-ratio FIELD is the shared object
— C28 prices it, C20 defines what it asserts. Both duties compose without
deadlock: [P-CERTKS] can pilot on the unqualified ratio (its F-1 catches
the conditioning side via gate disagreement) but its wrong-branch
discrimination WAITS on Tier-0 — stated in both duty texts. C21's
instruments feed C20's flagged-cell tier (same eta/omega constants).
LANDED-ROW COMPOSITION (reconcile): C20 Tier-0 additionally guards the
F11d premise at C11's estimator sites and the root-identity premise of
every C56 role (§3.4) — one monitor, three consumers, no duplicate build;
C9's F9b frozen-topology/frozen-seed-set tests govern seed validity under
remeshing/redistribution (C21's scope boundary, §4.2); the C56
gradient-role adjudication stays with C31TRIO (§1.5 explicit statement).
No object is decided twice; O-F20 advocacy counted once (§1.4).

### 4.5 Candidate rows (§0-bis (d) — proposed, NOT minted; dedup re-run §2.4)

1. FINDINGS candidate `oracles:root-identity-replay-common-mode`: wrong-
   branch root identity at replay is invisible to O3.1/[X-O31CS]/CERT_PLAY
   by construction (FD and IFT-adjoint legs share the replayed root) and
   is a premise of all three C56 roles + C11's F11d legs (which verify
   the weight GIVEN the root); guard = C20 Tier-0 monitor; extends
   oracles:o31-common-mode-hole one level up. Dedup re-measured this
   window (§2.4, patterns `replay`, `custom_vjp|IFT`, plus a dedicated
   `root.identity|wrong-branch|branch.consist` grep) — no existing row.
2. LEDGER candidate (axis 2) — WITHDRAWN AS DEDUPED in the reconcile: the
   draft proposed "discrete AD-adjoint vs continuous adjoint vs
   dual-consistent pairing — no ledger home"; the home NOW EXISTS: C56,
   minted at the C9/C11 landing (:731-740, re-read this window; the
   forecast "likely twin-proposed by C31TRIO" was overtaken by the
   landing-window mint). Replaced by the §4.3 C56 note rider. No new row
   proposed.
3. THEORY-duty candidate (rides C28's re-scope, consequence of §3.1-alt-5):
   per-sector PHYSICAL solvability-region derivation (O-F20's program:
   monotone-expansion + PM-margin + coalescence bounds, dry-level) as an
   F4b/O1-adjacent theory WP item — exposure-reduction + tier-opening
   value; NOT a C20/F2 blocker.

### 4.6 Literature-registry rider (rides the landing)

Grep-proven absent this window (§2.4, 0 hits post-landing): Kantorovich
1948 (root), Deuflhard CSM 35, Yamamoto Numer. Math. 1986, Ferreira-
Svaiter (arXiv:1209.5704) + the robust inexact-Newton companion
(arXiv:1110.3430), Hauenstein-Sottile TOMS 2012, Breiding-Rose-Timme TOMS
2023 (arXiv:2011.05000), ISSAC 2024 Krawczyk tracking (arXiv:2402.07053),
ICMS 2024 interval-alpha (arXiv:2405.04842), Farrell-Birkisson-Funke SISC
2015 (arXiv:1410.5620), signed-sigma_min (arXiv:2208.05954), RTI/AS-RTI
anchors (Nurkanovic 2019 + Automatica 2021) — WANTED tier per procurement
discipline; rows minted at the landing window, not here.

---

## PAPERS NEEDED (§0-bis (c) — procurement channel)

1. **Deuflhard, "Newton Methods for Nonlinear Problems: Affine Invariance
   and Adaptive Algorithms", Springer CSM 35 (2004/2011).** WHY: the
   Tier-1 kappa/omega qualified band must be DERIVED from the affine-
   covariant a-posteriori theory (the incumbent's step test is this
   family's natural criterion); deriving it from abstracts risks an
   R-4-grade mis-transplant of the omega estimates and the natural-
   monotonicity constants. WAITING CLAIM: the exact form of the Tier-1
   derived band in F2-C20-CERTQUAL-CAMPAIGN (the duty can open on the
   open-access Kantorovich/Ferreira-Svaiter constants, but the band of
   record should cite the affine-covariant source).
2. **Yamamoto, "A method for finding sharp error bounds for Newton's
   method under the Kantorovich assumptions", Numer. Math. 49 (1986).**
   WHY: sharpest classical a-posteriori bounds under Kantorovich
   hypotheses (dominates the Miel/Moret family per its own abstract);
   would TIGHTEN r_K in F-C21-2 and the flagged-cell tier. WAITING CLAIM:
   optional strengthener — the duty is executable without it (declared).

(Openly hosted items — arXiv:1209.5704, 1110.3430, 2011.05000, 1410.5620,
2402.07053, 2405.04842, 2208.05954, 2208.01784, the alphaCertified author
preprint — need no procurement; they enter at the depth read when the duty
consumes them.)

---

## 5. MACHINE SUMMARY

```json
{
  "cluster": "C2021",
  "rows": {
    "C20": {
      "proposed": "CONVERGED-ON-PROTOCOL; NEVER -> ADJUDICATED-SPLIT (architecture converged 2026-08-19 wave-2: Tier-0 branch/fold monitors always-on + Tier-1 kappa(J)-derived band composed with retained incumbent step metric + Tier-2 flagged-cell Kantorovich/Krawczyk [X-IVXC] referee; solvability-region pre-qualification CLOSED as qualification mechanism per C28 re-scope consumption, absorbed as annotation; P4 absolute, floor unmoved; pins F-C20-1..4)",
      "gated": true,
      "duty": "F2-C20-CERTQUAL-CAMPAIGN (Tier-0 build shared with C21; Tier-1 derivation shared with C18 window; committed GAP-3 toy carrier; itemized S18/defnoz re-run; cost gate; M0 back-propagation)"
    },
    "C21": {
      "proposed": "CONVERGED-ON-PROTOCOL; NEVER -> ADJUDICATED-SPLIT (policy converged 2026-08-19 wave-2: incumbent predictor+replay seeds retained as base layer; derived Kantorovich radius in z via [X-TBAK] two-point K_RICH pattern (eta = first Newton step) at audited/flagged cells; V-F7 fold-margin monitor transferred to march cells always-on; O3.1 replay-ball coverage requirement with fresh re-record fallback; asserted O(h) retired to measured-or-deleted; pins F-C21-1..4; owner alignment S25-probe -> F2; F9b scope boundary declared per landed C9)",
      "gated": true,
      "duty": "F2-C21-SEEDCERT-CAMPAIGN (omega surrogate in z + findings:1288 audit at S18+defnoz recorded cells + fire-rate report + replay-ball coverage + basin-law check; rides C20's Tier-0 build; C42 K_RICH role delta notified)"
    }
  },
  "census_recency": "1948-2026; axes A(validated-cert)/B(deflation)/C(fold-monitoring) reach 2023-2026 (newest 2026 arXiv:2602.12940, re-verified at source), axis D(warm-start guarantees) newest 2021+2023, classical school to Kantorovich 1948; 10 verbatim queries tabled, MoC-precedent absence query-bounded; reconcile re-verified 4 load-bearing items",
  "alternatives_closed": 14,
  "inflation_check": "done",
  "ledger_deltas_proposed": 6,
  "c56_gradient_role": "NOT adjudicated by C2021 — owed to wave-2 C31TRIO per C56 owner field (choice_ledger.yaml:739); C2021 consumed C56 as the axis-2 ledger home (draft's candidate ledger row withdrawn as deduped) and contributes the root-identity premise guard: all three C56 roles + C11's F11d legs inherit GAP-3's wrong-branch blind spot until C20 Tier-0 lands (C56 note rider proposed in §4.3)",
  "reconciliation": "partial verified+repaired+completed; anchors re-measured (ledger/M0 drift), 2 census one-liners trimmed to verified depth, C9/C11/C56 consumption added; details in RECONCILIATION DECLARATION"
}
```

---

## RECONCILIATION DECLARATION (per BRIEF_wave2_reconcile.md order 3)

**What was on disk at read time (the UNVERIFIED partial, ~48k, mtime in
the quota-kill window):** a structurally COMPLETE panel — header with
census stamp; §1.0-1.4 (frozen statement, both questions with
pre-registered criteria, materiality, wave-1 consumption); §2.1-2.5 (query
table, recency, one-liners, absence claims + greps, axis bearing);
§3.1-3.4 (both adjudications, composed architecture, emergent finding);
§4.1-4.6 (verdicts, pins, duties, ledger deltas, counting rule, candidate
rows, literature rider); PAPERS NEEDED; §5 machine summary. It ended with
the machine-summary fence — nothing was truncated mid-section; what was
MISSING was this declaration, the reconcile-mandated consumption of the
landed C9/C11/C56 rows, and verification of its anchors (written before or
across the landing that shifted them).

**What VERIFIED clean (kept):** the frozen questions + pre-registered
criteria W1-W5/V1-V5 (no post-hoc amendment found); the materiality
statement; the wave-1 C28 consumption incl. the PANEL_C28.md:398-402
verbatim quote and the shared-source declaration (both re-read); the
census query table, communities, recency table and per-source one-liners
(4 load-bearing items re-verified at source this window: arXiv:2602.12940
= Kumar-Pichi-Rozza 2026 deflation detection EXISTS as described;
arXiv:2208.05954 signed-sigma_min EXISTS as described; arXiv:1209.5704
Ferreira-Svaiter EXISTS; BRT TOMS 2023 "dramatically outperforms" +
built-in certify CONFIRMED); the cava greps (both patterns re-run: 0-hit
pattern reproduces 0; the token pattern reproduces the draft's hit set
exactly, and the draft's line-level dispositions verified at :21, :1188,
:1199, :1202, :1205, :1233, :1242); the literature/claims/M0/findings
dedup greps (re-run: 0 / {1753,1754,1766} / 1 hit :2357 / no
root-identity row — all reproduce); every code witness in
a1_ideal_march_jax.py (:200, :621-639, :668-693, :737-746, :795-828 incl.
:796-798, :801, :808-810, :812-813, :814-818, :821-828, :690, :1429-1430);
findings rows :1145-1154, :1281-1289, :564-572, :1486-1494, :328-336;
gapmap GAP-3 :150-169 and GAP-20 :551-572; M0 :2352-2360; claims rows
[X-TBAK] :1360-1372, [X-IVXC] :1749-1761, PAP-GMAX :1763-1774; diff
:106-115; trees phaseA_tree_optimization.md:1111-1133 and
phaseA_tree_variational.md:373-404; both adjudications' logic, the
architecture, the pins/falsifiers, the counting rule and the count 14.

**What was REPAIRED (each declared):**
1. M0 anchor "K_budget ... floor does not move": draft claimed
   M0:2005-2011 "re-read this window" — FALSE at reconcile read time; the
   quote lives at M0:2056-2058 (M0 drifted between the wave-1 verdict's
   window and this one). Re-anchored + drift tagged (§1.0).
2. M0 anchor "O1 OPEN": draft carried the verdict-era :2256-2259; current
   site :2303-2306 (verbatim re-read). Re-anchored + tagged (§1.4, §3.1).
3. Ledger row line anchors (post-landing drift): C20 :334-345 -> :336-347;
   C21 :347-356 -> :349-358 (note at :358); C18 :302-322 -> :315-324;
   C42 :571-579 -> :573-581; C28 :419-427 -> :421-429. All re-measured
   (§3.1, §3.2, §4.3).
4. Census one-liner (signed-sigma_min): "computed cheaply from the
   bidiagonal" removed — not confirmed at [ABS] depth; replaced with the
   verified mechanism (sign = product of SVD orthogonal-factor
   determinants; smooth through the fold; root-bracketing enabled) (§2.3).
5. Census one-liner (Ferreira-Svaiter): "ROBUST version ... ANY starting
   point in a prescribed ball" re-anchored to the verified abstract (good
   regions + invariant set); the explicitly-robust companion
   arXiv:1110.3430 added at [ABS] and to the registration rider
   (§2.3, §3.2, §4.6).
6. GAP-20 margin-inactive attribution: the draft cited "both rows'
   EXPOSURE lines"; GAP-20 carries it in its SEVERITY line :558-560
   (GAP-3's is in EXPOSURE :161-164). Corrected (§1.0, §1.3).
7. get_solver anchor refined :749-758 -> :752-758 (:749 is the _SOLVERS
   dict); PAP-GMAX end line :1773 -> :1774; C18-note GAP-29 citation
   repointed to the current row site (§1.0, §2.4, §3.1).
8. Findings grep hit sets re-measured (two post-draft hits :1519/:1936
   appeared — both inspected, neither adjudicates root identity; reported
   in §2.4 so the dedup claim is measured, not inherited).

**What was ADDED (completion per the reconcile mandate):**
1. §1.5 Landed-row consumption: C9 (F9b scope boundary for C21, folded
   r-arm), C11 (estimator premise leaning on the C20-qualified
   certificate; F11d verifies the weight GIVEN the root), C56 (axis-2
   ledger home; gradient role EXPLICITLY declared C31TRIO's object per
   the row's owner field :739 — the task-note's "engine question" is
   C31TRIO's, not this cluster's; this panel contributes the premise
   guard only).
2. §3.4 extension: the root-identity premise's consumer list extended to
   all three C56 roles + C11's F11d legs; dependency line extended to
   C20 -> {C28, C56/C11-estimator}.
3. §4.3: NEW C56 note-rider delta (notification, no role adjudicated);
   ledger_deltas_proposed 5 -> 6.
4. §4.5 item 2: the draft's axis-2 LEDGER candidate WITHDRAWN AS DEDUPED
   (C56 is the home); counting explicitly unchanged (the C56 item is not
   an alternative of C20/C21).
5. §4.2/§4.4: C21 scope boundary vs F9b; landed-row composition paragraph;
   C43's landed row cited as the executed precedent of the proposed C21
   owner alignment.
6. Machine summary: "ledger_deltas_proposed", "c56_gradient_role" and
   "reconciliation" keys added; census_recency notes the re-verification.
7. This declaration.

The partial's UNVERIFIED status is hereby DISCHARGED for this rewritten
file: every kept section verified as itemized above, every repair applied
in the text it names, every addition present. No registry was edited; no
git command was run; env untouched; GENO/ untouched.
