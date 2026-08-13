# ADVISORY — S24 SOTA GAP MAP OF RECORD (six-facet adversarial census)

- **Date**: 2026-08-12 (S24 window; untracked ADR in validation/)
- **Workflow**: six-facet SOTA gap census on the certified engine stack.
  Facets: (1) march mesh / error control [mesh-amr], (2) cell solver +
  certification [cell-cert], (3) design parametrization [parametrization],
  (4) optimizer/driver at the nonsmooth frontier [driver-nonsmooth],
  (5) constraint machinery [constraints], (6) thermo closure +
  tolerance/band culture [thermo-bands].
- **Participants**: 6 finder agents + 6 adversarial verifiers (one
  find→verify pair per facet; verifiers re-ran every probe and re-read
  every anchor at source, default-to-refute) + 1 judge (this synthesis).
- **Method**: repo Form-1 (find→verify avversario, then judge synthesis).
  Only VERIFIER-CONFIRMED content enters the map; downgraded findings
  enter only with their surviving (verified) residue; refuted-because-
  already-covered items go to the coverage ledger (§3), not the map.
  Cross-facet code-level dedup performed by the judge; every merge and
  every judge-side adjudication is labeled. Disagreements between
  verifiers are NOT harmonized — they are quarantined (§4).
- **Label**: judge-adjudicated in one round (no second panel round ran;
  quarantined items are open, not settled).
- **FORM-3 RED-TEAM EXECUTED (S25, 2026-08-12 — verdict of record:
  sota_gapmap_raws_2026-08-12/s25_redteam_gapmap_judge.md): ABSORB-
  WITH-REPAIRS (2 HIGH, 3 MED, 4 LOW) — the repairs are APPLIED IN
  THIS DOCUMENT, each marked [S25-REPAIR]. Root cause of both HIGHs:
  the judge consumed the INTERRUPTED driver-verifier draft; the
  superseding second pass (s24_gapv_driver-nonsmooth.md) is the
  verification of record and its G4/G5b verdicts govern.**
- **Honesty frame (global rigor-preservation note)**: no entry proposes
  weakening per-cell certification, rejectors, derived tolerances, RK-G
  determinism, or any gate. Every fix shape is additive: surrogates
  steer, binary gates stay the verifiers of record; new checks are
  rejector-formed with derived bands. Per-entry rigor notes state the
  specific contract.
- **Standing state respected**: [X-THC1] KEEP verdict fresh (thermo
  survey advisory of record); free-knot rejection (D6 item 9)
  adjudicated, not relitigated; S24 F1b campaign untouched by all probes.

---

## 1. COUNTS

- Finder findings across six facets: **47**
  (8+8+8+8+8+7).
- Verifier verdicts: **CONFIRMED 26 / DOWNGRADED 18 / REFUTED-outright 3**
  (+ refuted sub-claims inside downgrades: crash claim G5a, novelty
  clauses of thermo G1/G5, headline arithmetic of mesh F5, magnitude of
  param F8, AFEM attribution of param F5, and others per §4).
- After judge dedup (code-level): **36 map entries** — **5 HIGH,
  23 MEDIUM, 8 LOW** — plus **16 already-covered items** (§3) and
  **10 quarantine rows** (§4).
- Cross-facet merges performed (judge dedup, labeled in place):
  driver-G1 ≡ constraints-G7 (GAP-1); mesh-F2-residual ⊕ thermo-G7
  (GAP-9); param-F7 ⊕ constraints-G6 (GAP-22); cell-F8 ⊕ thermo-G5
  execution nudge (GAP-29); K_RICH items (mesh-F8 ⊕ thermo-G3 → §3
  AC5); box-edge items (cell-F1 ⊕ thermo-G1 → §3 AC6); cert-scale
  items (cell-F3 ⊕ thermo-G5 sub-claim → §3 AC8, judge-adjudicated).

---

## 2. THE SOTA GAP MAP (verifier-confirmed, deduplicated, ranked by severity then leverage)

### ——— HIGH TIER (5) ———

#### GAP-1 [driver-nonsmooth ≡ constraints; judge dedup of G1(F4)+G7(F5), both CONFIRMED HIGH by their verifiers]
**The certification frontier — the measured binding constraint of the program — is invisible to the KKT system; the registered quantifier is dead with no successor.**
- GAP: cert(W) <= 1 enters the problem only as binary outside gates (P4
  `a1_toc_variational_jax.py:935-938`, P3(ii) `:1158-1161`), while the
  traced, W-differentiable per-lane certification ratio ALREADY EXISTS on
  the replay path (`_ratio`/`_chain_ratios` :682-700, cert_diag worst
  :807-809) and is consumed only as a diagnostic (:1458). The KKT system
  is structurally incapable of closing at frontier-pinned points; the
  state of record is worse than "unquantified": M0:1624-1637 registered
  the Le Digabel–Wild taxonomy FOR this constraint and adopted the
  margin-constrained reformulation as its quantifier under the K_disc~A_0
  CONJECTURE — which was then FALSIFIED (S22; third instance S24/F4). No
  successor quantifier exists; census row 10 (C1 field-level rejector,
  owner F2) is a rejector, not an in-KKT surrogate.
- CLASS: INCOMPLETE (formulation). SEVERITY: HIGH — mechanism behind
  three outcome-II records (S20, S22, S24); determines whether outcome-I
  (KKT-closed) verdicts are producible at frontier instances at all.
- SOTA: KS constraint aggregation (Kreisselmeier–Steinhauser 1979;
  Poon–Martins SMO 2007) — KS-max upper form with derived rho (exact dual
  of `margin_governor.py:25-29`); MPCC smoothing (Scholtes;
  Fischer–Burmeister); proximal-bundle (Kiwiel — named in D6:738, never
  built). Spec of record (finder F4, verifier-confirmed): enforce
  KSmax_rho(r(W)) <= 1 − ln(N)/rho, sufficiency proven, stratum-local by
  construction, wired via the existing margin_factory slot (:1179-1182).
- EXPOSURE: extremal = deep-DEF eps=30 (S24 measured: 19-21 segments of
  frontier fencing, trial cert_worst 1e1..1e7, KKT open 1.417e6);
  everyday = mild S18 (surrogate inactive, mu_c=0, walk bit-comparable —
  zero cost far from the frontier).
- PROBE: measured — Probe B (analytic toy, both verifiers reproduced):
  binary-gate arm exits at radius floor with optimality 1.0 at distance
  7.1e-2 from the true optimum; KS-max arm closes KKT to 4.6e-11 with
  mu=0.709>0, binary gate never fires. Named-for-S25: [P-CERTKS] pilot at
  eps=4/NI=21 (cert_diag KS row + R-GRAD spot + short constrained walk vs
  S18 record).
- OWNER/PLACEMENT: F2 (S21 no-driver-work pin; this is specification
  content FOR census row 10, first named successor to the falsified
  bridge). Implementation caveats of record: cert_diag XOR val_diag
  (:576-577) needs a combined diag mode; one margin_factory slot →
  vector-valued constraint avoids driver surgery.
- RIGOR NOTE: surrogate steers, P4/P3(ii) stay absolute adjudicators —
  the repo's own [X-MGOV] surrogate-inside/gate-outside precedent.

#### GAP-2 [driver-nonsmooth G2 — CONFIRMED HIGH]
**No B-stationarity certificate at outcome-II: radius-ratchet exhaustion is the de-facto stationarity test, and the reported "KKT OPEN" number is the residual of the wrong problem.**
- GAP: outcome-II exit (`a1_toc_variational_jax.py:1000-1023`) fires on
  ratchet exhaustion at TR_FLOOR; the reported residual (S24: 1.417e6) is
  ||grad f + A^T v|| of the problem WITHOUT the certification constraint
  — at a frontier-pinned point it measures nothing about optimality.
  Today "pinned at a genuine frontier optimum" and "TR machinery failure
  at an interior point" are indistinguishable; the S24 EQ-v2 H-CLASS
  qualification leans on this distinction.
- CLASS: RIGOR-GAP. SEVERITY: HIGH (verdict-adjacent: three outcome-II
  records). Fairness annotation of record: the outcome-II wording is
  honest ("never a silent success") and S24's attribution has independent
  measured support (P4 trial rejections 5.0e0..3.4e5) — no recorded
  number shown wrong, none CERTIFIED.
- SOTA: B-stationarity for MPCCs (Scheel–Scholtes 2000); gradient/
  manifold sampling (Burke–Lewis–Overton; Larson–Menickelly–Wild SIOPT
  2018); Clarke tests in nonsmooth TR (Conn–Gould–Toint §11).
  Executable form: (i) with GAP-1's surrogate, scipy optimality IS the
  surrogate B-residual (Probe B Arm 2 closes); (ii) without it, a
  convex-hull test 0 ∈ conv{stratum gradients}+normals on the persisted
  rejected designs (s22_rejected_designs.json exists; :904-912).
- EXPOSURE: extremal = optimum ON a stratum seam (two plans meet: both
  single-stratum gradients nonzero, point B-stationary, today reported
  "KKT OPEN"); rejector-family crossings; raw-vs-relative residual
  conflation at eps→100 (7.7e-2 vs 1.6e6 compare different scales).
  Everyday = mild S18: certificate trivially passes, zero cost.
- PROBE: measured — Probe B Arm 1 (reproduced). Named-for-S25: [P-BSTAT]
  convex-hull test from persisted S24 artifacts (+ ~5 re-records, engine
  session).
- OWNER/PLACEMENT: F2 (with GAP-1; the certificate is what upgrades every
  future outcome-II from declaration to adjudication).
- RIGOR NOTE: adds a certificate; changes no exit semantics until it can
  fire; the honest outcome-II branch remains.

#### GAP-3 [cell-cert F2 — CONFIRMED HIGH]
**The one-extra-Newton-step certificate has no conditioning or branch qualification: near a fold it both false-fails (converged cell rejected) and false-passes (wrong-branch root certified at ratio 0).**
- GAP: `certify` (`a1_ideal_march_jax.py:682-707`) claims derivation
  "from the Newton contraction" — the contraction hypothesis is never
  checked, no kappa(J) qualification exists, and no branch-consistency
  monitor (sign det J / den-sign continuity) exists anywhere. Measured on
  a near-fold quadratic (probe re-run by verifier): exact root → ratio 25
  = false FAIL (roundoff amplified by 1/|J|); basin-scale stale seed →
  other branch at ratio 0.0 = false PASS. [X-CDKAT] does NOT discriminate
  this (a conditioning-rejected cell is also bit-identical under cap
  raise); C2-F2 CERT_PLAY cannot see the wrong-branch pass.
- CLASS: RIGOR-GAP. SEVERITY: HIGH — (a) false-fail is a candidate
  MECHANISM inside the outcome-II "certifiability-limited" frontier of
  record (S20, S22, S24 — enlarges the F2-owned mechanism candidate list,
  which today has only spline-conditioning/knot-mismatch); (b) false-pass
  sits on the verdict-bearing O3.1 FD-probe replay path.
- SOTA: affine-covariant a-posteriori estimators + Kantorovich
  (Deuflhard, Newton Methods); Krawczyk interval-Newton enclosure
  (in-house lineage [X-IVXC]); deflation for root discrimination
  (Farrell–Birkisson–Funke).
- EXPOSURE: extremal = near-fold den→0 cells of deep-DEF defnoz; throat
  razor cells alpha→90 deg; FD probes at frontier designs (basin
  half-width < h_FD = 6.1e-6). Everyday = mild instances well-conditioned
  — the gap is invisible exactly where everything works.
- PROBE: measured (toy; declared caveat: not yet demonstrated in the repo
  4x4 cells — quarantine Q3). Named-for-S25: branch-consistency monitor +
  kappa-aware band evaluated over one recorded S18/defnoz march.
- OWNER/PLACEMENT: F2 (feeds the near-axis/outcome-II mechanism
  identification the F2 mandate already owns).
- RIGOR NOTE: a kappa-aware bound is still derived (eps·kappa(J)), a
  re-adjudication lever, not a loosening; branch monitor is additive.

#### GAP-4 [driver-nonsmooth G7 (TR_FLOOR half) — CONFIRMED HIGH]
**TR_FLOOR = 1e-3 is underived and is the de-facto resolution of the outcome-II verdict exit, in scaled coordinates whose physical size changes per instance.**
- GAP: `a1_toc_variational_jax.py:896-899` ("S18 clip", no derivation);
  exhaustion fires exactly at the ratcheted floor (:992-1023), three
  verdicts of record (S20, S22, S24); the floor lives in Jacobi-scaled u
  coordinates (:1064-1065) so cross-instance "exhausted at the floor"
  statements compare different physical resolutions.
- CLASS: RIGOR-GAP (R5: tolleranze derivate, non magiche — on a
  verdict-bearing exit). SEVERITY: HIGH.
- SOTA: noise-aware TR floors (Cartis–Scheinberg Math. Prog. 2018;
  Moré–Wild noise estimation). Derived floor available from quantities
  already measured: TR_FLOOR = K_RICH · tol_dp/||g|| in u units (tol_dp =
  O3.1 FD Richardson band, :1480-1482).
- EXPOSURE: extremal = eps→100 (fixed floor reached at physically larger
  steps → premature "exhaustion", false frontier); short-L deep-DEF (node
  spacing in u ~ floor → ratchet exhausts while certified descent exists
  below it). Everyday = eps=4 (constants happen adequate — S18 closed).
- PROBE: named-for-S25 — [P-TRFLOOR]: recompute S24 run-2 exhaustion with
  the derived floor from its own logged tol_dp/||g||; pure arithmetic on
  logged numbers, no reruns.
- OWNER/PLACEMENT: S25 arithmetic + F2 adoption (one line at the driver).
- RIGOR NOTE: replaces a magic constant with a derived one; tightens,
  never loosens, the meaning of outcome-II.

#### GAP-5 [parametrization F2 — CONFIRMED HIGH]
**The natural right BC (y''(L)=0) biases the design class exactly at the lip node where the open [C-O33] goal quantity is differentiated — a named, unexcluded alternative mechanism for the corner residual of record.**
- GAP: `a1_toc_variational_jax.py:148` forces zero lip curvature at every
  m; a Rao/TOC bell has nonzero lip curvature, so the representation
  error at the lip is O(h^2) and does not vanish by knot insertion
  elsewhere. The [C-O33] goal metric |dJ/dy_lip − corner density| is
  evaluated at this biased node (adaptive_knot_optimize.py:242-250; lip
  interval carries 17.6% indicator mass, M0:1501). Probe (verifier
  re-run): 76x last-interval error vs a not-a-knot end on a curved-lip
  contour. No carrier, duty, or census row measures the BC-induced floor.
- CLASS: RIGOR-GAP. SEVERITY: HIGH — bears directly on a diagnosis of
  record (S19 corner baseline 6.6295e-02, "design-class limit" reading).
- SOTA: not-a-knot end condition (de Boor; FITPACK/scipy default
  lineage); free-end B-spline control points.
- EXPOSURE: extremal = deep-DEF defnoz (Dtheta=−9.98 deg, strong lip
  curvature); eps=30 L=8 DEF-wall tier-0. Everyday = the eps=4 twin — the
  goal of record is measured at this biased node today.
- PROBE: named-for-S25 — `notaknot-twin`: one row of spline_coeffs
  changed, re-measure r=1/r=2 corner mismatch at W*8 vs the 6.6295e-02
  baseline; rejector-formed (GENO-oracle band must NOT move — same wall
  data).
- OWNER/PLACEMENT: S25 engine session (cheap, one-row twin); consequence
  adjudication F2.
- RIGOR NOTE: twin-with-rejector design; the incumbent BC is not touched
  until the twin discriminates.

### ——— MEDIUM TIER (23) ———

#### GAP-6 [mesh-amr F5 — DOWNGRADED MEDIUM; surviving content verified]
**No start-line accuracy rejector exists, and the two-resolution band is structurally blind to the shared Sauer IVL model error.**
- GAP: both resolutions share the same first-order Sauer start
  (gamma=const, GENO-mirrored 1e-6 offset, `a1_ideal_march_jax.py:719-727`),
  so IVL model error is invisible to e(x) BY CONSTRUCTION — an
  instrument-level statement in no record doc. Individual series terms at
  the record case are 0.17/0.33 of a* (NET 0.17 — corrected number, see
  Q9); at the panel's r=0.1 extreme the series is meaningless (net 2.5).
  Partial coverage exists (problem-book gamma-const row, IVL-provenance
  duty, o32 sonic exclusion — §3 AC14); the REJECTOR half is nowhere.
- CLASS: RIGOR-GAP (instrument blind spot). SEVERITY: MEDIUM (twin/EQ-v2
  verdicts are start-line-error-cancelling; bites absolute-accuracy
  claims and compact-throat instances).
- SOTA: Kliegel–Levine (AIAA J 7(7) 1969) / Hall (QJMAM 1962) higher-order
  starts; displaced-IVL invariance check (Zucrow–Hoffman lineage).
- EXPOSURE: extremal = rtu→0.5 / r=0.1 compact RDE throats (model-limited
  contours); eps→100 deep-DEF (start error propagates into Me target and
  D' localization). Everyday = rtu=1.5 twin (7.6e-9 cross-code agreement
  proves fidelity, not accuracy).
- PROBE: measured this session (series magnitudes, corrected by
  verifier). Named-for-S25: displaced-start-line invariance rejector
  (march 3 columns, restart, contour must move < band).
- OWNER/PLACEMENT: S25 probe; documentary one-liner in M0 NOW (band
  blindness statement); higher-order start = F4b/F5 lever if the rejector
  fires.
- RIGOR NOTE: adds a rejector; the twin DATA CONTRACT with GENO stays.

#### GAP-7 [thermo-bands G4 — CONFIRMED MEDIUM]
**Pointwise two-resolution bands are never topology-conditioned: a plan-topology flip between (h, h/2) can cancel against the smooth term, and e(x) has crossing zeros where the band collapses to floor.**
- GAP: contour_compare (`a1:1099-1117`), band_u (toc:1415-1427), o33
  field bands assume the (h,h/2) pair shares march topology; nothing
  checks it, though the LB-c2 monitor exists (o32:545-557) and an
  in-house cure for the zero-crossing collapse exists at ONE site
  (running max, toc:1701-1712) and is not applied to the band sites.
  PASSes of record (62/62, 0/98) are conditional on the unchecked
  hypothesis.
- CLASS: RIGOR-GAP. SEVERITY: MEDIUM (no demonstrated in-repo
  under-coverage; mechanism demonstrated on a TUNED synthetic — Q4).
- SOTA: topology-conditioned banding (wire LB-c2 into band rows);
  Eça–Hoekstra LSQ multi-grid (JCP 2014); DWR (Becker–Rannacher) — named
  in D4:217/M0:1297/R25.
- EXPOSURE: extremal = [X-AKNO] insertion-site skip at a flip boundary;
  deep-DEF wall-search re-records between resolutions (S23 defnoz lesson
  class). Everyday = eps=4 twin contour band (passes, no attestation).
- PROBE: measured (synthetic mechanism: 11.2% under-coverage, worst
  1853x, control 0-out — quarantined as mechanism-only, Q4).
  Named-for-S25: LB-c2 census attached to every band row + running-max
  envelope at the three band sites.
- OWNER/PLACEMENT: S25 (machinery exists; wiring task) / F2.
- RIGOR NOTE: adds an attestation to existing PASSes; bands never narrow.

#### GAP-8 [mesh-amr F6 — CONFIRMED MEDIUM (the facet's only outright confirm)]
**The axis (y→0) unit process is verification-free at march level while being the verdict-load-bearing read point (exit Mach is read at the axis cell).**
- GAP: resid_axis foot-ratio treatment (`a1:488-499`, GENO guard :566) is
  formally consistent (probe: O(h^2) coefficient bias, no order defect —
  honestly disclaimed), but no march-level axis oracle exists: the
  inherited gconst oracle never exercises the v/y limit cell
  (g0_spike has no axis point process), no MMS, no axis-only refinement.
  Me_ach = axis-cell value (:853, :889) gates the exit topology; the
  program's open "near-axis mechanism" residual (owner F2) is the
  OPTIMIZATION-stall object — a different thing, not covering this.
- CLASS: INCOMPLETE (verification coverage). SEVERITY: MEDIUM.
- SOTA: MMS order verification (Roache JFE 2002) at the axis cell;
  Zucrow–Hoffman axis point process (L'Hopital v/y → dv/dy).
- EXPOSURE: extremal = NI large (first ring y→0, foot ratio
  0/0-adjacent); deep-DEF (terminal characteristic + K at the axis:
  Me error = axis-cell error → D' and F1/F2 bands). Everyday = eps=4
  (axis cells pass Newton certification — ALGEBRAIC layer only).
- PROBE: measured (consistency hand-probe, reproduced). Named-for-S25:
  march-level gconst axis oracle at two NI (2 reduced marches).
- OWNER/PLACEMENT: S25 probe; F2 documentary (distinct from near-axis
  mechanism row — one line to avoid conflation).
- RIGOR NOTE: pure verification addition.

#### GAP-9 [judge dedup: mesh-amr F2 surviving residual (MEDIUM) ⊕ thermo-bands G7 (LOW) — severity split declared, carried MEDIUM]
**The observed-order machinery ([X-O32]) exists but is applied only to O3.2 registered norms: no verdict-bearing band site is order-verified, and the o32 NON-CONCLUSIVE verdict does not propagate to band rows sharing its hypothesis.**
- GAP: every two-resolution band presumes the h^p model at r=1,2 while
  the repo's own three-level measurement at the twin returned
  NON-CONCLUSIVE (p_fine=2.5347, dp_tot=0.6704 > 0.5 cap) and a standing
  counterexample exists (f2 drift GROWS under refinement, 9.48e-03 →
  1.42e-02, carried honestly). K_RICH is not conditioned on an observed p.
  Coverage threshold of record (verifier-corrected): deployed bands
  protect the COARSE member → under-coverage begins at p < log2(4/3) =
  **0.415** (not 0.3219).
- CLASS: RIGOR-GAP (coverage extension + missing declaration).
  SEVERITY: MEDIUM (mesh-amr verifier) vs LOW (thermo verifier) — split
  declared, judged MEDIUM because the corner row of record already shows
  the predicted signature ("converging in both limits but NOT confirmed
  at a Richardson band").
- SOTA: observed-order GCI (Roache 1994; Celik/ASME V&V 20-2009: Fs
  conditioned on observed vs assumed p); the estimator is ALREADY BUILT
  (o32:151-192) — reuse, not build.
- EXPOSURE: extremal = deep-DEF D' window + dtheta quantization put a
  non-mesh floor under the two-mesh delta; table-edge first-order
  contamination. Everyday = the r=1,2 pair every band actually uses.
- PROBE: named-for-S25 — extend [X-O32]'s estimator to the banded
  quantities (contour band, band_u, def_twin F-branches, corner row) +
  third resolution in contour_compare (~1 extra march per row);
  NON-CONCLUSIVE propagation rule (degraded-p coverage factor).
  NOTE: finder's P-S25-1 re-scoped to this; P-S25-2 dropped as duplicate
  (§3 AC4).
- OWNER/PLACEMENT: S25 engine session; feeds R25 K_RICH audit (§3 AC5).
- RIGOR NOTE: bands can only widen or gain a verified premise.

#### GAP-10 [thermo-bands G6 — CONFIRMED MEDIUM]
**Band composition has no declared rule: sum, max, and heterogeneous mixes coexist; K·max silently halves the intended safety exactly when both error mechanisms contribute.**
- GAP: SUM at a1:1338-40/toc:1480-82 (K_RICH also multiplies the
  roundoff floor — category-mixing, conservative), MAX at def_twin:380-381
  and :404 (band_dprime), heterogeneous unweighted sums at :1122-1124,
  :1146-47, :1167-69. No doc states when each form applies. Measured
  (arithmetic): comparable components a~b → K·max covers a+b by 2.11x
  (intended 4x). Honest datum of record: S24 D' band max-dominated 19:1 —
  no current verdict touched.
- CLASS: RIGOR-GAP. SEVERITY: MEDIUM.
- SOTA: GUM composition (JCGM 100:2008 — RSS independent, linear sum
  unknown-correlation); ASME V&V 20-2009 u_val composition.
- EXPOSURE: extremal = deep-DEF D' landing near a cell boundary (cell ~
  ds_land: both terms comparable). Everyday = O3.1 tol_dp (sum form,
  benign).
- PROBE: measured (P2c arithmetic, reproduced). Named-for-S25: declared
  one-paragraph composition policy + pass over the max sites.
- OWNER/PLACEMENT: documentary one-liner + S25 band pass.
- RIGOR NOTE: any site changed moves toward the conservative composition.

#### GAP-11 [thermo-bands G2 — CONFIRMED MEDIUM]
**The thermo table box is case-independent literals with no per-run margin certificate: the "contains every march-realized state" hypothesis is enforced nowhere.**
- GAP: T_TAB_LO/HI = 1050/3900, N_TAB=8192 literals (a1:142-143);
  thermotab:31-33 declares the hypothesis; grep of record + verifier:
  no box check on any run path. Measured margins (reproduced):
  stagnation margin **34.8 K** (undeclared), exit-T margin **8.34 K at
  eps=100**; comfortable at executed instances — and unrecorded.
- CLASS: INCOMPLETE (generality directive: case-independent procedures).
  SEVERITY: MEDIUM.
- SOTA: envelope-driven table generation with declared margin
  (CEA/CoolProp/REFPROP practice); unify with C-C joint-census ingest.
- EXPOSURE: extremal = eps=100+ scan (8 K margin, one continuation step
  from the edge); high-T0 case exits the TOP of the box in the subsonic
  seed region. Everyday = defnoz-class eps 10-25 (200-500 K, unrecorded).
- PROBE: measured (P1, verifier-reproduced). Named-for-S25: per-run
  realized-(T,ht) census → box-margin row in every Verdict.
- OWNER/PLACEMENT: F2 (same window as C-C/C-D, §3 AC6); Verdict-row
  addition is S25-cheap.
- RIGOR NOTE: adds a certificate; box unchanged until derived version
  lands.

#### GAP-12 [constraints G5 — CONFIRMED MEDIUM]
**No independent multiplier rejector: res.v is consumed raw into verdict-adjacent quantities, and extraction failure silently becomes mu_use = 0.0.**
- GAP: lam = res.v[0] raw (toc:1603 → Pa_impl); `except Exception: pass`
  at margin_governor.py:536-542 → mu_est=None → mu_use=0.0 with no
  counter ([D1]-constrained metric); driver checks stationarity +
  feasibility, never complementarity (toc:1203-1207). Measured
  (arithmetic, reproduced): at the S24 stop |mu·m| = 3.55e3 — a derived
  complementarity band fires on exactly the case that was caught BY HAND
  (barrier artifact demoted at step 13d).
- CLASS: RIGOR-GAP (R5: every consumed number needs a rejector).
  SEVERITY: MEDIUM (no recorded number currently wrong; rel_c runs only
  at margin-active, never yet reached).
- SOTA: LSQ multiplier estimates (Gill–Murray–Wright 1981); three-part
  KKT termination (Wächter–Biegler 2006).
- EXPOSURE: extremal = LICQ degradation (lip row ∥ one-hot margin
  gradient) — only an LSQ residual detects it. Everyday = S18 lambda →
  Pa_impl reading, currently uncheckable.
- PROBE: measured (P2). Named-for-S25: [R2'] LSQ re-estimate on recorded
  S18/S24 gradients; complementarity band as a check() row; counter on
  the except-pass path.
- OWNER/PLACEMENT: S25 (band + counter are cheap); F2 for the LSQ row.
- RIGOR NOTE: pure addition of rejectors on consumed numbers.

#### GAP-13 [constraints G2 — CONFIRMED MEDIUM]
**Rung-frozen chain mask granularity is provably wrong at deep-DEF (measured drift 14 nodes, drift_val 4.3x the floor) and the repair granularity costs decisive runs; segment-level re-freeze and the differentiable gate were never adjudicated.**
- GAP: mask frozen per RUNG (def_twin:487-490, :945-954) while the plan
  re-freezes per RK-G P2 segment — the only W-dependent frozen object
  outside that rhythm. C3 fired of record (i_cross 96→82, drift_val
  9.188e-3 vs mu0 2.118e-3; repeat consumed decisive run 2). Panel C3
  ratified rung-freeze; NO position considered segment re-freeze or the
  smooth gate sigma(val/eps_gate) — post-adjudication measured evidence.
- CLASS: INCOMPLETE + RIGOR-GAP (stale-mask window up to a full rung).
  SEVERITY: MEDIUM (stale floor never bound — margin inactive 33x; cost
  = budget + attribution, honestly recorded).
- SOTA: smoothed Heaviside projection (Guest–Prévost–Belytschko 2004);
  implicit differentiation of the crossing (Blondel et al. 2022);
  freezing-granularity-matched-to-stratum (CGT semantics the plan already
  follows).
- EXPOSURE: extremal = deep-DEF rung 1 (MEASURED); crossing near lip end
  (bucket of 2-3 lanes: absolute node-count gate too loose vs the bucket
  it protects). Everyday = mild eps=4 (no crossing; vacuously correct).
- PROBE: named-for-S25 — [R1] replay recorded run-1 segment bases through
  cs_stats, i_cross per segment (smooth accumulation → segment re-freeze
  suffices; jump → differentiable gate).
- OWNER/PLACEMENT: F2 (both legs — interface extension makes even the
  cheap leg driver-touching; S21 pin).
- RIGOR NOTE: C3 detector stays; granularity change only shrinks the
  stale window; gate transition lives inside the declared-unresolvable
  band.

#### GAP-14 [constraints G3 — CONFIRMED MEDIUM]
**The mask shape-adaptation crop can silently DROP enforced lanes: the event is counted, the enforcement loss is not bounded.**
- GAP: `mm[:r,:c] = mask[:r,:c]` (def_twin:618-625); a True lane beyond
  the overlap exits KS AND frac_bad (denominator recomputed on the crop,
  :640, :648). 16 adaptations counted in decisive run 2 — True-lanes lost
  per adaptation unmeasured. Panel residual adjudicated counter
  granularity at 0 events; the conservation-of-enforcement invariant is
  nowhere.
- CLASS: RIGOR-GAP (counted event ≠ bounded event; against the repo's own
  C4/C5 standard). SEVERITY: MEDIUM (loss can only weaken an
  inactive-by-33x constraint at this instance; no number at risk).
- SOTA: repo's own counted-events discipline one level deeper.
- EXPOSURE: extremal = deep-DEF truncation (DoD removes trailing columns
  where the DE chain lives — crop eats DE lanes preferentially); [X-AKNO]
  M_NODES change between derive and rung. Everyday = run 2's 16
  adaptations (loss almost surely 0 — unmeasured).
- PROBE: named-for-S25 — [R1'] log mask.sum() − mloc.sum() per adaptation
  over the recorded run.
- OWNER/PLACEMENT: one-line fix + verdict-bearing counter (S25);
  margin_governor.py:47-50 pattern.
- RIGOR NOTE: adds an invariant; nonzero loss becomes verdict-bearing.

#### GAP-15 [driver-nonsmooth G3 — CONFIRMED MEDIUM]
**Every margin-constrained walk since S22 runs scipy tr_interior_point — not the §4bis-adjudicated Byrd–Omojokun path — with cold barrier restarts at every RK-G segment; the IP engine was never source-adjudicated.**
- GAP: any inequality switches the method (verified at installed scipy
  1.18.0, minimize_trustregion_constr.py:403-406); the S22 margin entry
  (toc:1179-1182) did exactly that, unacknowledged in the S22 log; each
  segment is a fresh minimize() → 19-21 cold barrier restarts at S24.
  S24-T1 covered multiplier extraction only. GAP-1 adoption makes the IP
  (or replacement) engine PERMANENT — re-adjudication is on the F2
  critical path.
- CLASS: NOT-SOTA / INCOMPLETE (adjudication lapse). SEVERITY: MEDIUM
  (S18 KKT-closure record ran pre-S22 on the adjudicated path; IP-path
  records are outcome-II declarations robust to residual conventions).
- SOTA: IPOPT warm-start extensions (Wächter–Biegler); filter/funnel SQP
  (Fletcher–Leyffer; Uno); SLQP (Byrd–Gould–Nocedal–Waltz). Minimum bar:
  §4bis-grade read of tr_interior_point.py (barrier law, optimality
  semantics, status meanings, warm start).
- EXPOSURE: extremal = a margin/cert-ACTIVE rung (central path vs
  reject-and-shrink interaction untested; livelock analogue of S20
  sticky-shrink unexamined). Everyday = R-G1d derive walk (passes, under
  the wrong adjudication label).
- PROBE: measured (Probe C source read). Named-for-S25: [P-IPADJ]
  source adjudication (LLM-side, no compute) + optional S18-mild A/B for
  barrier-restart overhead.
- OWNER/PLACEMENT: F2 entry (with the engine re-decision, §3 AC10 row).
- RIGOR NOTE: adjudication work; no behavior change until decided.

#### GAP-16 [driver-nonsmooth G6 — CONFIRMED MEDIUM]
**The measured Hessian is the only verdict-adjacent measured quantity in the driver with no rejector and no derived band; symmetrization averages away the natural error signal.**
- GAP: Hw = 0.5(Hw+Hw^T) (toc:1096) destroys the asymmetry signal;
  nothing checks the matrix (contrast: gradient has O3.1 + corrupted
  control; margin gradient has R-GRAD). Kink risk real (searchsorted
  seams; FD step can straddle a knot/plan seam → column O(1) wrong). A
  wrong Hessian degrades TR steps and can MASQUERADE as
  certifiability-limiting — the main attribution risk at outcome-II
  (couples to GAP-2).
- CLASS: RIGOR-GAP. SEVERITY: MEDIUM (P4/P3(ii) certification is
  Hessian-independent — no recorded number at risk; attribution
  robustness is).
- SOTA: symmetry-defect band pre-symmetrization (Nocedal–Wright §8.1
  error model); directional second-difference Richardson (O3.1 lifted one
  derivative); Moré–Wild noise-aware steps (TOMS 2012).
- EXPOSURE: extremal = W at a plan-flip seam (frontier habitat);
  post-[X-AKNO] near-degenerate knots. Everyday = mild instance: 2 extra
  gradient evals/segment, passes silently.
- PROBE: named-for-S25 — [P-HESSREJ] wire both checks into one S18
  segment; measure defect distribution near vs far from a flip seam.
- OWNER/PLACEMENT: F2 (driver); cheap.
- RIGOR NOTE: adds a rejector to a measured quantity — R5 conformance.

#### GAP-17 [driver-nonsmooth G8 — CONFIRMED MEDIUM]
**Jacobi scaling Dv is measured once per walk, from objective curvature only, never refreshed across 19-21 frontier segments and blind to constraint rows.**
- GAP: measured at first segment base only (toc:1050-1070), frozen; S18
  finding of record: conditioning IS the convergence rate on this driver;
  constraint Jacobian rows (KS rho ~ 5.75e4 → rows orders steeper) are
  never equilibrated. Refresh is FREE: the full H is re-measured per
  segment — its diagonal costs zero extra evals.
- CLASS: EFFICIENCY-GAP. SEVERITY: MEDIUM.
- SOTA: affine-invariant scaling refreshed at model rebuild (Deuflhard);
  KKT row equilibration (Gill–Murray–Saunders SNOPT lineage).
- EXPOSURE: extremal = cert/margin-active walk with rho huge (mixed
  scales 1e4-1e6 → inner CG stagnation indistinguishable from TR
  failure); post-[X-AKNO] new dofs with no measured scale. Everyday =
  short mild walks (frozen Dv fine — why S18 never saw it).
- PROBE: named-for-S25 — [P-DVREFRESH] refresh from per-segment diag(H)
  on the S18 walk; segment count + KKT trajectory + determinism
  bit-check.
- OWNER/PLACEMENT: F2 (with GAP-15/AC10 review).
- RIGOR NOTE: determinism preserved (refresh from recorded quantities);
  bit-check registered.

#### GAP-18 [driver-nonsmooth G5b — DOWNGRADED MEDIUM; [S25-REPAIR, red-team HIGH: the verifier's SECOND pass downgraded G5b as a duplicate of speed-audit conditional N6 ("benign-flip segment merge... needs its own panel. Flagged, never traded") — the judge had consumed the interrupted draft; N6 ownership RESTORED, and the [P-FLIPMAT] probe is DE-REGISTERED from §5 (the verifier ruled it not licensable without the N6 panel)]]
**Any single (N,Nv) decision flip ends the RK-G segment with no materiality test: measured churn ("a flip fires at almost every accepted step") makes the walk pay record-scale cost per productive step.**
- GAP: comparator ends the segment on ANY difference (toc:1167-1176);
  no flip-materiality band, though the repo owns the right metric (replay
  fidelity band :1041). A lipward-only flip discards a Hessian exactly
  valid for every dof but the lip.
- CLASS: EFFICIENCY-GAP. SEVERITY: MEDIUM. Ownership annotation: same
  G0/T2 review window as AC10.
- SOTA: PC^1 TR methods with active-set anticipation (Scholtes; SLQP
  BGNW 2004) — stratum changes when the MODEL changes materially.
- EXPOSURE: extremal = Nw dense (segment length degenerates to 1);
  deep-DEF small-radius flips (S24 step 12 measured). Everyday = mild S18
  (measured: ~every accepted step).
- PROBE: named-for-S25 — [P-FLIPMAT] materiality-gated segmentation A/B
  on the S18 walk (flip → re-record → compare wall to replay band →
  continue if within band); determinism comparison.
- OWNER/PLACEMENT: F2 entry (G0/T2 review input).
- RIGOR NOTE: a flip within the replay-fidelity band is the same
  quadratic model to within the band — the gate stays for material flips.

#### GAP-19 [constraints G8 — CONFIRMED MEDIUM]
**The margin NonlinearConstraint ships exact jac but NO hess: scipy silently BFGS-estimates constraint curvature (~rho/4·|∇val|² when active) — the exact S18 plateau mechanism, re-created on the constraint side.**
- GAP: toc:1181-1182 (no hess=); R-3 of record repaired BFGS-quality
  curvature on the OBJECTIVE half only; at rho=5.75e4, rho/4 = 1.44e4 can
  dominate the measured H, re-learned from identity every segment.
- CLASS: NOT-SOTA / INCOMPLETE. SEVERITY: MEDIUM — declared boundary:
  margin INACTIVE at every recorded instance (zero recorded effect; pays
  only in the margin-active regime / enriched classes, F2+).
- SOTA: exact Lagrangian Hessian in SQP (Nocedal–Wright §18-19);
  forward-over-reverse HVP (standard JAX); or the existing
  FD-of-exact-gradient recipe (toc:1088-1094) applied to gm.
- EXPOSURE: extremal = margin-active rung (BFGS from identity, TR
  collapse pre-R-3 style); argmin-lane swap mid-segment (curvature jumps,
  stale estimate not sign-safe). Everyday = margin inactive (absent).
- PROBE: folded into [R2] S25 pilot (hess= flag A/B, segments-to-close).
- OWNER/PLACEMENT: F2 (with GAP-1 pilot).
- RIGOR NOTE: measured-per-segment-base, frozen within segment — R-3
  policy extended, not changed.

#### GAP-20 [cell-cert F4 — CONFIRMED MEDIUM]
**No derived seed-validity radius exists in z-space: the design-space ball got a THEOREM+PRACTICE stack ([X-TBAK]) while predictor and stale-replay seeds rest on an asserted "lands inside".**
- GAP: predictor asserted O(h) (a1:540-543); replay seeds = recorded z
  (:634, toc:519); KAT-3 is one instance + one amplitude. The z-basin
  shrinks like sqrt(dist-to-fold) below h_FD = 6.1e-6 near folds → O3.1
  probe seed validity at frontier instances unadjudicated; CERT_PLAY does
  not close the wrong-branch case (GAP-3).
- CLASS: INCOMPLETE (W-space/z-space asymmetry, verified exact).
  SEVERITY: MEDIUM (coverage; record campaigns ran margin-inactive, far
  from folds).
- SOTA: Smale alpha-theory point estimates (alphaCertified,
  Hauenstein–Sottile TOMS 2012); Kantorovich radii from measured local
  Lipschitz data ([X-TBAK] K_RICH two-point pattern transplants).
- EXPOSURE: extremal = near-fold deep-DEF cells (basin collapse + branch
  twin makes GAP-3's false pass REACHABLE); razor-thin near-sonic start
  cells. Everyday = every O3.1 FD probe (4 replays/verdict) at mild
  designs.
- PROBE: named-for-S25 — alpha-test at every recorded cell of the S18
  baseline + defnoz plans (one Jacobian + Hessian-norm surrogate per
  cell).
- OWNER/PLACEMENT: F2 (converts to a measured ledger row).
- RIGOR NOTE: pure certificate addition on the replay path.

#### GAP-21 [parametrization F1 — CONFIRMED MEDIUM; cross-facet tension with constraints-verifier declared in Q2]
**The interpolation-vs-control-point basis adjudication is missing on the axis that is actually failing (oscillation / variation-diminishing / convex-hull); the D6 rejection adjudicated conditioning + revalidation cost only.**
- GAP: D6:922-926 rejection text contains no oscillation axis (verified);
  the S17 chain of record (taper seed → attachment oscillation →
  uncertified cell + NaN gradient) has a now-measured analytic mechanism:
  clamped-end alternating curvature wave, ratio −(2−sqrt(3)) EXACT,
  amplitude ∝ slope mismatch, growing 1/h (independently re-derived by
  the verifier). The engine is feasible-seed-dependent because the class
  oscillates on innocent data. A zero-behavior-change first step exists:
  exact change of basis to B-spline control points POST-solve, for
  certificates only (convex-hull bounds on y, y').
- CLASS: NOT-SOTA (unadjudicated choice on the failing axis).
  SEVERITY: MEDIUM (no verdict overturned; missing adjudication +
  forward levers).
- SOTA: B-spline control polygon (de Boor; Boehm 1980); IGA shape-opt
  lineage; CST/Hicks–Henne correctly set aside (global support).
- EXPOSURE: extremal = deep-DEF steep thB (mismatch max at clamped end →
  compression cell at attachment, the S17 chain); post-[X-AKNO] close
  knots + height jump (cardinal amplitude 17-170x → invisible
  inter-node admissibility break). Everyday = any non-GENO-seeded start.
- PROBE: measured (P1/P5, verifier-reproduced incl. exact recurrence
  root). Named-for-S25: post-solve change-of-basis certificate (no
  optimization-variable change).
- OWNER/PLACEMENT: F2-entry adjudication (same survey-and-adjudicate
  treatment free-knot got, on the correct axis); F3 consequence.
- RIGOR NOTE: does NOT relitigate D6 on its own axis; certificates first,
  basis switch only if the adjudication converges on it.

#### GAP-22 [judge dedup: parametrization F7 (CONFIRMED MEDIUM) ⊕ constraints G6 surviving half (DOWNGRADED MEDIUM)]
**Declared shape monitors (slope positivity, curvature bounds) are computed nowhere: inadmissible trial walls are discovered only by paying a full march, and geometry rejections pollute the certifiability-frontier diagnosis of record.**
- GAP: toc:18-21 declares the monitors; no path computes them (verified
  grep). Two independent probes agree: per-interval slope/curvature at
  fixed thB are closed-form/affine in the dofs (affinity residuals at
  machine floor) → pre-march checks cost microseconds; today a geometry
  event lands in rejected_designs as a certifiability event. The S20
  certdiag 8/8 "genuine" discriminates tolerance-vs-budget, NOT
  geometry-vs-physics — the S20 frontier reading rests on rejections
  being physics.
- CLASS: INCOMPLETE (claims-to-code). SEVERITY: MEDIUM — escalates to
  HIGH only if the S25 probe finds a geometry-representable rejection
  among the S20 five (registered, rejector-grade design first).
- SOTA: a-priori geometric admissibility in shape optimization (linear
  control-point constraints, IGA practice; closed-form cubic slope
  extrema); precision note of record: "LINEAR inequalities in W" belongs
  to the B-spline basis (GAP-21) — in the current class the check is
  closed-form-cheap but thB-nonlinear (per-segment conservative
  linearization matches the RK-G rhythm).
- EXPOSURE: extremal = deep-DEF fencing (19-21 segments; fraction of
  trials excludable for free — UNMEASURED, Q6); [X-AKNO] close knots
  (overshoot between stations invisible at nodes). Everyday = every TR
  trial evaluation, currently marched blind.
- PROBE: measured (both facets' probes). Named-for-S25: [S25-P4 /
  geom-vs-cert tag] closed-form slope pre-check over the S20
  rejected_designs ledger + REJECTED-BY-GEOMETRY vs
  REJECTED-BY-CERTIFICATION tag; [R2] pilot rows at eps=4.
- OWNER/PLACEMENT: S25 (tag + ledger re-read); F2 (constraint rows in the
  KKT, with GAP-1).
- RIGOR NOTE: march rejectors stay the verdict layer; rows are a cheap
  outer approximation; the S20 reading is re-adjudicated only by a
  rejector-grade probe.

#### GAP-23 [parametrization F3 — CONFIRMED MEDIUM]
**The [X-AKNO] insertion degeneracy guard protects the wrong object: mesh-derived (station spacing, shrinks under refinement) instead of operator-derived (adjacent-knot ratio, mesh-independent).**
- GAP: guard = dx_loc median station spacing (adaptive_knot_optimize.py:
  209-213) rationalized as "solve poisoning"; measured: cond(A) saturates
  ~6 at ratio 1000 while the interpolation-operator cardinal amplitude
  grows ~linearly (2.2/17.5/170 at 10/100/1e3). Admitted knot ratio
  degrades with march refinement; repeated insertion into the persistent
  41.8%-mass interval produces clustering the guard progressively stops
  guarding.
- CLASS: RIGOR-GAP (tolerance not derived from the failure mode it
  guards). SEVERITY: MEDIUM (S20 record benign; exposure is the loop's
  future coverage).
- SOTA: local-mesh-ratio admissibility (de Boor; Schoenberg–Whitney;
  FITPACK placement discipline).
- EXPOSURE: extremal = Nw=240 + max_ins=3 into one interval over cycles
  (ratios O(1e2) admitted); height noise between close knots amplified
  17-170x between nodes. Everyday = cycle 2 inserting next to cycle 1's
  knot at Nw=60.
- PROBE: measured (P4' ladder, reproduced). Fix shape: operator-derived
  primary bound (declared max adjacent-knot ratio), station-spacing check
  secondary.
- OWNER/PLACEMENT: S25-cheap ([X-AKNO] guard edit + rejector).
- RIGOR NOTE: additive; the current guard stays as the secondary bound.

#### GAP-24 [parametrization F4 — CONFIRMED MEDIUM]
**Warm-start exactness across knot insertion is a provable THEOREM measured at machine zero — but the code disclaims it and wields a print instead of a rejector.**
- GAP: nested-space uniqueness ⇒ re-interpolation reproduces the
  incumbent EXACTLY (verifier independently checked the argument; P3 =
  6.7e-16); the header claims "NOT ... geometry-preserving" and dev_warm
  only prints (adaptive_knot_optimize.py:44-48, 434-451). dev_warm above
  a derived floor is a DEFECT DETECTOR (knot remap / BC inconsistency)
  that today would print and pass — R5: tests must be able to reject.
- CLASS: INCOMPLETE (armable invariant unarmed; under-claimed theorem —
  R4 promotion due). SEVERITY: MEDIUM (guards every future [X-AKNO]
  cycle verdict).
- SOTA: Boehm 1980 insertion exactness; Oslo algorithm
  (Cohen–Lyche–Riesenfeld 1980).
- EXPOSURE: extremal = insertion at near-degenerate site (floor must
  carry the measured cardinal amplitude); steep-thB clamp (floor scales
  with slope). Everyday = the S20 two-knot cycle (arm there first).
- PROBE: measured (P3). Named-for-S25: arm dev_warm <= K_RICH · eps ·
  (measured cardinal amplitude) · scale as a check() row + near-degenerate
  negative control; promote nestedness to M0 (class THEOREM).
- OWNER/PLACEMENT: S25-cheap; M0 delta same session (R4).
- RIGOR NOTE: converts a print into a rejector; nothing else moves.

#### GAP-25 [parametrization F5 — DOWNGRADED MEDIUM (verifier corrections absorbed)]
**The [X-AKNO] outer loop is insertion-only: no knot removal/coarsening, so dofs ratchet monotonically while "dof economy is part of correctness" (D6) stays unenforced.**
- GAP: stop rules never remove a knot; a knot justified by cycle-k
  residual can be dead at cycle k+1 (the optimum MOVES per cycle — the
  no-coarsening AFEM optimality theorems address a FIXED problem:
  verifier-corrected attribution, Stevenson 2007 / CKNS 2008 vs
  Binev–Dahmen–DeVore 2004); every retained dof taxes all later cycles
  (n+1 evals/segment). GAP-24's exactness makes removal cheap to TEST
  (project to coarser class, measure deviation vs derived band).
  Verifier-refuted sub-claim excluded: the artifact of record saves the
  BEST cycle's class — no failed-knot inheritance through the artifact.
- CLASS: INCOMPLETE. SEVERITY: MEDIUM (efficiency/coverage).
- SOTA: knot removal (Lyche–Morken 1987); AFEM with coarsening
  (Binev–Dahmen–DeVore 2004); hierarchical parametrization (Desideri).
- EXPOSURE: extremal = oscillating indicator (dof growth, stagnant goal,
  budget exhausted with polluted class). Everyday = default 4-cycle
  3-insert run: 8 → up to 20 dofs, no survivor audit.
- PROBE: named-for-S25: removal-test leg (project + derived band) on the
  recorded S20 cycle.
- OWNER/PLACEMENT: F2/F3 loop upgrade.
- RIGOR NOTE: removal is gated by the same derived-band machinery as
  insertion; goal metric unchanged.

#### GAP-26 [parametrization F6 — DOWNGRADED MEDIUM; partial ownership declared]
**The global-support cardinal basis makes the measured Hessian structurally dense (n+1 evals forced) — and the cheap alternative to a basis switch (adjudicated band-truncation with derived bar) was never priced.**
- GAP: cardinal decay 0.243/interval, never zero → no exploitable
  sparsity; the n+1-eval full measurement is the term named dominant when
  T2 FIRED. Colored Hessians are NAMED in D6:880-881 with the G0/T2
  review SCHEDULED (census row 7) — that half is owned (§3 AC10). NEW and
  unowned: coloring is USELESS under the current basis without a
  truncation adjudication; |H_ij| falls ~2 decades by 3 intervals — a
  MEASURABLE truncation with a derived bar, no basis switch needed. Also:
  O(n^3) unrolled dense solve of a tridiagonal system inside every traced
  evaluation (hygiene-grade at current m).
- CLASS: EFFICIENCY-GAP. SEVERITY: MEDIUM.
- SOTA: graph-colored FD Hessians (Curtis–Powell–Reid 1974;
  Gebremedhin–Manne–Pothen 2005); banded spline solves (Thomas; de Boor).
- EXPOSURE: extremal = m~30 after enrichment at a frontier instance
  (~3100 gradient evals of pure curvature). Everyday = 10-dof class: 11
  evals/segment, ~5 segments/cycle.
- PROBE: named-for-S25 — `hess-decay`: |H_ij| vs |i−j| at W*8 (n+1
  evals, ~30 s small instance) vs the cardinal-decay prediction.
- OWNER/PLACEMENT: feeds the scheduled G0/T2 review (F2 entry) with the
  measured decomposition it lacks; truncation route = S25 probe.
- RIGOR NOTE: truncation only with a derived bar; otherwise dense
  measurement stays.

#### GAP-27 [constraints G1 — DOWNGRADED MEDIUM (chatter symptom already panel-named; derivation defect survives)]
**The KS rho derivation controls conservativeness only: at rho = 5.75e4 the "smooth" aggregate is a hard min to machine precision (one-hot gradient, curvature ~rho/4), and this instance sensitivity is declared nowhere in the derivation.**
- GAP: rho = K_RICH ln(N)/mu0 pins ln(N)/rho below enforcement
  resolution — correct — but nothing budgets gradient support or
  curvature: mild S22 gets a genuine aggregate (~20 weighted lanes),
  deep-DEF gets a hard min (1/45 lanes above 1e-12, model-inferred — Q10).
  The panel named the CHATTER symptom (§3 AC12); the derivation-side
  budget is uncovered.
- CLASS: NOT-SOTA (+ RIGOR-GAP on the smoothness premise).
  SEVERITY: MEDIUM.
- SOTA: adaptive-KS (Poon–Martins SMO 2007); induced-exponential/power
  aggregates with bounded curvature (Kennedy–Hicken CMAME 2015);
  two-constant derived rule (gap AND curvature/weight-support budget,
  max-feasible smoothing).
- EXPOSURE: extremal = deeper ladder / smaller m_ref (rho ~ 1e7);
  two lanes tied near the crossing (argmin-swap gradient chatter reads as
  TR model error). Everyday = eps=4 (healthy — which is why it survived
  S22 green).
- PROBE: measured (P1, reproduced). Named-for-S25: [R3] argmin-swap
  census along the recorded S24 walk.
- OWNER/PLACEMENT: F2 (same window as GAP-1: the cert surrogate will
  reuse this aggregation and inherits the defect if underived).
- RIGOR NOTE: two-constant rule keeps the conservativeness theorem intact.

#### GAP-28 [cell-cert F7 — DOWNGRADED MEDIUM; un-owned lever isolated]
**The wall-foot chord search makes (N,Nv) fragile recorded decisions whose flips SET the re-record rate (n_rec ~ n_segments, measured of record) — and nobody owns making them derived quantities.**
- GAP: unbracketed linear index scan, one FULL implicit Newton per failed
  attempt, monotone-foot assumption, Nv never steps back (a1:806-833,
  toc:355-375); fragility measured of record (toc:847-852 verbatim). The
  speed audit cuts record COST (M5 keeps wall_search eager) — no document
  owns cutting the decision-flip RATE at source. Wrong-foot silent
  acceptance under non-monotone spline: PLAUSIBLE, unmeasured (Q5).
- CLASS: INCOMPLETE + NOT-SOTA. SEVERITY: MEDIUM.
- SOTA: bracketed scalar root-finding on the continuous chord parameter
  (Brent 1973) + orientation pre-filter (Shewchuk 1997) → (N,Nv) derived,
  one implicit solve at the bracketed foot.
- EXPOSURE: extremal = [X-AKNO] near-degenerate knots (spline overshoot
  between stations); steep thB (foot jumps rows); short-L truncation (cap
  exhaustion). Everyday = Nw x O(Nv) failed attempts per record on the
  hot path.
- PROBE: named-for-S25: doctored two-close-knots spline, wrong-foot count
  vs Brent-bracketed reference (~1 min).
- OWNER/PLACEMENT: F2 (derived-(N,Nv) lever; couples to GAP-18 — rate
  and materiality attack the same churn from both sides).
- RIGOR NOTE: the implicit cell solve and its certification are
  unchanged; only the SEARCH becomes bracketed/derived.

### ——— LOW TIER (8) ———

#### GAP-29 [cell-cert F8 — CONFIRMED LOW; merged with thermo-G5's surviving execution nudge (judge dedup)]
**Solver/cert constants are conventions under an "ALL DERIVED" header, and the damping ladder accepts any non-increase with no sufficient-decrease or contraction measurement.**
- GAP: NEWTON_TOL_FACTOR=100 "spike factor convention", N_NEWTON=30
  (KAT-proven biting, not derived), ladder (1,1/2,1/4,1/16,1/64,0) with
  bare argmin acceptance (a1:145-148, :371, :397-416) — vs thermotab's
  derived C_OPS (the repo knows how). Constants cluster = AUDIT F5
  registered with the halved-constants test NEVER EXECUTED (open duty);
  the ladder/sufficient-decrease half is new.
- SOTA: Deuflhard NLEQ measured-contraction damping; Armijo (N-W §3.1);
  Higham op-count constants; Moré–Wild FD floors.
- EXPOSURE: extremal = near-fold cells burn 30x6 evals to certify a
  stall. Everyday = every cell pays the 6-candidate vmap in the terminal
  quadratic phase.
- PROBE: named-for-S25: execute AUDIT:426 (halved-constants sweep) + one
  measured-contraction damping A/B at the F2 engine rebuild.
- OWNER/PLACEMENT: S25 (sweep) + F2 (ladder); documentary derivation
  paragraph.
- RIGOR NOTE: floors can only be justified or tightened.

#### GAP-30 [cell-cert F5 — DOWNGRADED LOW]
**cert_diag machinery hygiene: the prefix-exactness lemma of _chain_ratios is unstated (no M0 rigor row), and the replay-vs-record equivalence family is populated by ONE KAT instance.**
- Surviving after verifier corrections (the "predates consumer" claim was
  factually wrong; margin certified at acceptance via P4 + floor
  rejector): the lemma deserves an M0 SCHEMA/PRACTICE row (R4), the
  val_diag starvation KAT-3 twin does not exist (steering-quality, not
  verdict-bearing), union-return is a cheap fix.
- PROBE: named-for-S25: val_diag starvation KAT twin (~2 min).
- OWNER/PLACEMENT: S25-cheap + M0 one-liner.
- RIGOR NOTE: documentation + test family growth only.

#### GAP-31 [driver-nonsmooth G5a — DOWNGRADED LOW-MEDIUM; crash claim REFUTED]
**On a length-only plan change (thB crossing a da multiple) the flip comparator raises StopIteration — scipy catches it (clean status 3, recorded in §4bis), but the flip event is SILENTLY DROPPED from the P2 log of record (re_record_events undercount).**
- The one-line default repair (min(len(a), len(b))) is verified correct
  and cheap; the surviving defect is record-keeping on the record path.
- PROBE: measured (Probe A, both runs). OWNER: S25-cheap fix.
- RIGOR NOTE: restores completeness of a log of record.

#### GAP-32 [constraints G4 — CONFIRMED LOW]
**The lip equality is carried as a LinearConstraint row instead of eliminating one variable — paying a normal step every iteration and taking lambda_e from solver internals when AD post-optimality would give it exactly (Fiacco), with an O3.1-style check.**
- OWNER: F2 (driver surgery); no record impact. RIGOR NOTE: multiplier
  provenance moves from solver-trusted to repo-verified.

#### GAP-33 [driver-nonsmooth G7, xtol half — CONFIRMED LOW]
**xtol = 1e-10 is a hard-coded literal at every call site; even the [X-TOCV] origin claims the derivation in prose while assigning the literal (verifier-strengthened).**
- OWNER: F2 one-liner (propagate the Newton-floor derivation as
  arithmetic). RIGOR NOTE: derived replaces declared.

#### GAP-34 [parametrization F8 — DOWNGRADED LOW; magnitudes corrected]
**Insertion sites chosen in physical x are stored as normalized xi and silently migrate when thB moves at the next re-optimization; no drift monitor exists.**
- Corrected magnitude of record: S18 event ≈ 4.4% of the first m=8
  interval (everyday ~1.4%, NOT 15% — Q8); material only against
  post-insertion LOCAL intervals or short-L. Fix: print + band per-cycle
  knot drift; re-derive xi if it exceeds a declared fraction of the
  marked interval.
- OWNER: S25-cheap monitor. RIGOR NOTE: monitoring only.

#### GAP-35 [mesh-amr F3 residual — DOWNGRADED LOW]
**Joint refine() confounds the three error directions (IVL rows / arc angle / contour-exit stations): a band that fails to shrink cannot be attributed (mesh vs class vs floor).**
- Claim (i) of the finder (floor never measured) REFUTED of record (S19
  mstop diagnostic, §3 AC4); the per-direction attribution lever
  survives, adjacent to but not identical with R25.
- OWNER: S25 (per-direction refinement flag in o33_bench.refine).
- RIGOR NOTE: attribution sharpener for existing falsifier branches.

#### GAP-36 [mesh-amr F7 residual — DOWNGRADED LOW]
**The D'-band cell-vs-landing-window winner is implicit: :405-408 prints both terms, but no label states which floor binds, and at dtheta-quantization-dominated instances local mesh refinement provably cannot help.**
- The attribution print EXISTS (verifier); only the max() winner label is
  missing — 1-line addition. Seam-clustered refinement lever itself is
  R25-owned (§3 AC15).
- OWNER: S25 one-liner. RIGOR NOTE: label only.

---

## 3. ALREADY-COVERED LEDGER (refuted-because-covered; this list is EVIDENCE OF COVERAGE, not waste)

| # | Item (facet finding) | Covered by (existing duty/carrier of record) | Delta attached (discharge-priors, no new row) |
|---|---|---|---|
| AC1 | DWR march bars "named-never-built" (mesh F4) | Ledger 10bis U3 (Level-C target) + PROGRESS R25 "mesh AMR/DWR (F2)"; M0:313-318 BAR-CLASS note defuses the verdict-misstatement angle | Sizing input: dual weights = one vjp; per-cell residuals exist; sum(eta) vs two-mesh rejector = discharge design |
| AC2 | Uniform march net "lever nobody holds" (mesh F1 headline) | R25 (owner F2) + R21 joint mesh+knot F1/F4 leg (S24+1 pre-authorized) | Column-local C- insertion at RECORD time (RK-G P2-compatible) = the AMR primitive spec; 41.8% localization datum |
| AC3 | "No observed-order carrier exists" (mesh F2 headline) | [X-O32] o32_mesh_convergence.py: three-level estimator, known-answer tested, dp_model asymptotic indicator, NON-CONCLUSIVE honesty, negative control | Residual promoted to GAP-9 (extend to band sites) |
| AC4 | m_stop floor "never measured" (mesh F3(i)) | S19 pre-declared diagnostic EXECUTED (1e-5→1e-7, attribution confirmed); S22 STIM-1 (me_gap 3.55e-15); o32 "mstop" stage | Finder probe P-S25-2 DROPPED as duplicate |
| AC5 | K_RICH=4 universality (mesh F8 + thermo G3, judge dedup) | PROGRESS R25 open row "universalita' K_RICH=4 (F2 audit)" | Annex to R25: 8-role census (file:line), corrected coarse-member threshold p < 0.415, GCI Fs-conditioning on observed p, [X-TBAK] declared-surrogate label |
| AC6 | Table-edge silent clamp/extrapolation unguarded (cell F1 + thermo G1, judge dedup) | Named conditional C-D (S24 census, owner F2) + AUDIT F3 :386-400 (BOTH modes incl. C1 quintic extrapolation already in the finding of record) | C-D spec CORRECTION: advisory §8 restatement is clamp-only — rejector must cover BOTH modes; measured priors: dead adjoint dT/dq=0 exact; C1 sign-flipped gradient (+0.545 vs −1.94); reachability M~4.6; fix pattern toc:227-237 |
| AC7 | No early-abort in record mode (cell F6) | Speed audit H1 (complete design, gates, gains) + prompt L2 + PROGRESS R22; owner S25 item 8 | none needed (finder consumed the advisory's own 111 s baseline without dedup) |
| AC8 | Cert-scale unit mixing sc=max(1,max|z|) (cell F3 + thermo G5 sub-claim) — JUDGE-ADJUDICATED dedup, see Q1 | AUDIT F8 engine-core:F8-cert-scale-unit-mixing (:458-470), adjudicated LOW of record | New site a1_toc:243; P3 arithmetic (position bound 2300x loose at y=1e-3); componentwise-scaling fix shape (Deuflhard/Higham) |
| AC9 | Newton-floor constants cluster (thermo G5) | AUDIT F5 (:416-428) with prescribed halved-constants test | Execution is the open S25 duty (GAP-29); C_OPS=100 weakly derived note |
| AC10 | Fresh-Hessian-per-segment cost (driver G4 cost half; param F6 coloring half) | T2 FIRED of record + G0/T2 re-decision review SCHEDULED (census row 7, F2 entry); colored Hessians named D6:880-881 | [S25-REPAIR, red-team HIGH: the "survey absence" clause re-asserted a verifier-REFUTED claim from the interrupted draft] Input to the review: determinism-preserving SR1 carry (certified-pairs-only, pure function of walk history) + stale-symptom re-measure + per-segment directional rejector; NOTE: quasi-Newton reuse is ALREADY surveyed-OUT by policy (speed-audit §7.3 S1 "quasi-Newton reuse OUT by policy") — the review may re-open it only as an explicit policy re-adjudication, never as an unsurveyed gap |
| AC11 | StopIteration "uncaught crash of the whole walk" (driver G5a crash half) | scipy wraps callback StopIteration → clean status 3; recorded in kickoff §4bis:340-342 | Surviving log-omission defect = GAP-31 |
| AC12 | KS argmin-tie chatter at rho=5.75e4 (constraints G1-E2) | S24 DE-bucket panel non-blocking residual ("budget risk inside the [P4] cap ... monitor wall time per rung") | Derivation-side budget = GAP-27 |
| AC13 | B-spline basis switch as constraint lever (constraints G6 half) | D6 S20 residue-(a) rejection of record (:915-926) | Tension with param-F1 declared in Q2; oscillation-axis adjudication = GAP-21 |
| AC14 | Sauer start partial coverages (mesh F5 headline parts) | Problem book: gamma=const structural limit + named alternatives + "IVL provenance and accuracy order are part of the Verdict" duty; KPT-2002 sensitivity row; o32 sonic-line exclusion; in-code DATA CONTRACT declaration :37-40 | Rejector half + band-blindness statement = GAP-6 |
| AC15 | D'-seam local refinement lever (mesh F7 headline) | R25 (mesh AMR/DWR, owner F2); attribution print exists :405-408; GENO refinement direction RAN (801/4001) | Sizing detail: seam-local C- insertion ~linear vs global ~quadratic; winner label = GAP-36 |
| AC16 | leggeAree 400-point bracket scan (cell drop 5) | Speed audit H2 (bracket-scan vectorization, per-record) | box-derived q_max window credited under GAP-11 |

Probe-registry corrections of record: P-S25-2 (m_stop sweep) DROPPED
(duplicates AC4); P-S25-1 (three-mesh triplet) RE-SCOPED to GAP-9
(extend [X-O32] to banded quantities). Mandatory-read note for future
mesh/error-control facets: validation/o32_mesh_convergence.py + the
PROGRESS.md CHOICE LEDGER census are required sources (finder omission
caused two headline refutations).

---

## 4. QUARANTINE (non-converged items, declared caveats, judge adjudications — open, not settled)

- **Q1 [JUDGE-ADJUDICATED verifier disagreement]** cell-cert verifier
  CONFIRMED F3 stating "no coverage found anywhere"; thermo verifier
  produced the covering anchor (AUDIT F8 :458-470, same finding, same
  figure, adjudicated LOW). Judge resolution: already-covered (AC8) on
  the specific anchor; the facet-2 additions attach as priors. Both
  verdicts preserved here — not unanimity.
- **Q2 [cross-facet tension, declared]** constraints-verifier treats the
  B-spline lever as CLOSED (D6 rejection); parametrization-verifier
  verified the rejection text adjudicates conditioning+revalidation ONLY
  and CONFIRMED the oscillation-axis adjudication as missing. Judge
  synthesis: the D6 DECISION stands on its adjudicated axis; GAP-21 is a
  re-adjudication duty on the unadjudicated axis, not a relitigation.
  One round only — F2-entry adjudication decides.
- **Q3** GAP-3's failure modes are TOY-MEASURED (near-fold quadratic),
  not yet demonstrated in the repo's 4x4 cells — HIGH carried with this
  declared caveat; S25 probe named.
- **Q4** Thermo G4's numbers (11.2% under-coverage, 1853x) come from a
  TUNED synthetic (finder's two failed parameterizations show the regime
  is not generic): mechanism demonstration ONLY — never quotable as
  coverage failures of the bands of record.
- **Q5** Wall-foot wrong-foot silent acceptance (GAP-28 correctness
  half): PLAUSIBLE from predicate shape, unmeasured; S25 doctored-spline
  probe decides.
- **Q6** GAP-22's fencing-reduction benefit at S24 is UNMEASURED and
  plausibly small (rejections are certification failures at healthy val);
  the S25 geometry-tag probe over the S20 ledger decides — and touches a
  reading of record, so rejector-grade design first.
- **Q7** GAP-9 severity split: mesh-amr verifier MEDIUM vs thermo
  verifier LOW — carried MEDIUM by the judge on the corner-row signature;
  split preserved.
- **Q8** param F8 everyday magnitude corrected ~10x down by the verifier
  (≈1.4%, not 15%); only corrected numbers are of record (GAP-34).
- **Q9** mesh F5 probe headline corrected: NET wall perturbation +0.17 a*
  (terms 0.167/0.333 opposite-sign), not 0.50; r=0.1 conclusion robust
  (net 2.5). Only corrected numbers are of record (GAP-6).
- **Q10** constraints G1 "exactly ONE lane" is MODEL-INFERRED (uniform
  lane-spacing model, declared conservative), not a readout of the
  measured S24 field; S22 probe input N=3059 vs implied ~3496 (~21 lanes
  — conclusion unchanged). Wording of record: model-inferred.
- **Q11 [S25-REPAIR, red-team MED: this cross-verifier disagreement
  had been harmonized WITHOUT the promised quarantine row]** cell-cert
  verifier read cell-F8's constants cluster as "no coverage found";
  the thermo verifier (and the judge's AC9) point to AUDIT F5
  (:416-428, halved-constants test prescribed, never executed) as
  covering the same cluster. Both readings preserved — the AC8/AC9
  coverage stands on its anchors, the "no coverage" reading is
  RECORDED not erased; the GAP-29 sweep execution (S25-bis) settles
  the row either way.

---

## 5. S25 PROBE REGISTRY (consolidated across facets; each march-bearing or >30 s; dedup applied)

Engine session (scheduled, PROGRESS R22 — speed items live there too):
1. [P-CERTKS] KS-max cert surrogate pilot at eps=4/NI=21 + R-GRAD spot +
   short constrained walk vs S18 record (GAP-1; arm hess= A/B per GAP-19
   in the same pilot = [R2]).
2. [P-BSTAT] convex-hull B-stationarity test from persisted S24
   artifacts (+~5 re-records) (GAP-2).
3. [P-TRFLOOR] derived-floor recompute of S24 run-2 exhaustion from
   logged tol_dp/||g|| — pure arithmetic (GAP-4).
4. [P-IPADJ] §4bis-grade source adjudication of tr_interior_point
   (LLM-side) + optional S18 A/B (GAP-15).
5. [P-HESSREJ] symmetry-defect + directional-Richardson Hessian rejector
   on one S18 segment (GAP-16).
6. [P-DVREFRESH] per-segment Dv refresh from diag(H), determinism
   bit-check (GAP-17).
7. [DE-REGISTERED, S25-REPAIR] the [P-FLIPMAT] materiality-gated
   segmentation A/B is WITHDRAWN from this registry — the driver
   verifier's second pass ruled it not licensable without the N6
   panel (speed-audit conditional N6 owns the object: "needs its
   own panel. Flagged, never traded"); it may re-enter only AS the
   N6 panel's own instrument (GAP-18, repaired).
8. [P-QNCARRY] SR1-carry vs fresh-FD A/B, bit-compare determinism
   (AC10 input).
9. [R1]/[R1'] mask i_cross-per-segment replay + lost-True-lane count on
   the recorded S24 run (GAP-13, GAP-14).
10. [R2'] LSQ multiplier re-estimate on recorded S18/S24 gradients +
    complementarity band + except-pass counter (GAP-12).
11. [R3] argmin-swap census along the recorded S24 walk (GAP-27).
12. `notaknot-twin` one-row BC twin, corner mismatch r=1/r=2 at W*8,
    GENO-band rejector (GAP-5).
13. `hess-decay` |H_ij| vs |i−j| at W*8 vs cardinal-decay prediction
    (GAP-26/AC10).
14. `warmstart-rejector` arm dev_warm derived floor + near-degenerate
    negative control; M0 THEOREM promotion (GAP-24, GAP-23 guard edit).
15. `geom-vs-cert tag` closed-form slope pre-check over the S20
    rejected_designs ledger (GAP-22; rejector-grade design — Q6).
16. Displaced-start-line invariance rejector at the reduced case (GAP-6).
17. March-level gconst axis oracle at two NI (GAP-8).
18. One-off DWR assembly + sum(eta) vs two-mesh J-delta rejector (AC1
    discharge design).
19. Extend [X-O32] estimator to banded quantities + third resolution in
    contour_compare; NON-CONCLUSIVE propagation rule (GAP-9; replaces
    P-S25-1; P-S25-2 dropped).
20. Band-composition policy paragraph + pass over max sites; LB-c2 wired
    into band rows + running-max envelope (GAP-10, GAP-7).
21. Per-run box-margin census row in the Verdict (GAP-11).
22. Halved-constants sweep per AUDIT:426 + component-scaled z-metric
    (GAP-29/AC8/AC9).
23. alpha-test/Kantorovich per-cell seed certificate at S18 + defnoz
    plans (GAP-20).
24. val_diag starvation KAT-3 twin (GAP-30).
25. Doctored close-knots wall-foot vs Brent reference (GAP-28, Q5).
26. Per-direction refine() flag + D' winner label one-liners (GAP-35,
    GAP-36).

---

## 6. ANNEX — THE CHOICE LEDGER
(standing user directive 2026-08-12, choice-adjudication-convergence:
every algorithmic choice point surfaced by the six facets; the incumbent
gets NO home advantage — status NEVER is an open duty, never a silent
default. Status values: CONVERGED-panel / single-author / NEVER.
Judge-added rows are marked [J].)

| # | Choice | Incumbent | SOTA alternative set | Status | Evidence pointer | Owner+placement if open |
|---|---|---|---|---|---|---|
| C1 | Design basis class | Clamped/natural interpolating cubic, heights-as-dofs | B-spline control polygon (de Boor/Boehm); CST (Kulfan); Hicks–Henne | single-author on the oscillation axis (D6 adjudicated conditioning+revalidation only) | D6:915-926; param-F1 + Q2 | F2-entry adjudication (GAP-21); post-solve change-of-basis certificate = S25 |
| C2 | Right-end BC | natural y''(L)=0 | not-a-knot (de Boor/FITPACK); free-end control points | NEVER (code line only) | toc:148; param-F2 | S25 `notaknot-twin` (GAP-5) |
| C3 | Left-end BC | clamped tan(thB) | — (attachment tangency, forced by geometry) | CONVERGED (constructional) [J] | toc:146-147 | — |
| C4 | Knot placement law | uniform xi + [X-AKNO] goal-indicator insertion | free knots (Jupp); curvature-based abscissae | survey-decision of record [S25-REPAIR: was "CONVERGED-panel"; D6 item 9 records an adopt-or-declare SURVEY decision, not a Form-2 panel] | D6 item 9 (free-knot rejection, Jupp lethargy); S20 [X-AKNO] record | — |
| C5 | Knot anchoring across thB updates | normalized xi re-anchored to live xB | physical-x / arc-length / curvature-anchored knots | NEVER | param-F8 (corrected magnitudes Q8) | S25 drift monitor (GAP-34) |
| C6 | Insertion degeneracy guard | dx_loc = median station spacing (mesh-derived) | operator-derived max adjacent-knot ratio (de Boor; Schoenberg–Whitney) | single-author (rationale measured wrong: solve vs operator) | adaptive_knot_optimize:209-213; P4' probe | S25 guard edit (GAP-23) |
| C7 | Outer-loop dof policy | insertion-only ratchet | insert+remove (Lyche–Morken); AFEM coarsening (BDD04) | NEVER | param-F5 (corrected attribution) | F2/F3 loop upgrade (GAP-25) |
| C8 | Warm-start deviation handling | print-only dev_warm | derived-floor rejector (armed) + THEOREM row | NEVER (armable invariant unarmed) | param-F4; P3 = 6.7e-16 | S25 (GAP-24) |
| C9 | March mesh law | uniform NI/da/Nw/Ne per run | column-local C- insertion at record time; goal-oriented AMR (Venditti–Darmofal) | NEVER (registered open row) | R25; mesh-F1/AC2 | R25 owner F2; spec attached |
| C10 | Refinement operator | refine(r) joint global scaling | per-direction refinement (multi-parameter GCI, Eça–Hoekstra) | NEVER | o33_bench:172-176; mesh-F3(ii) | S25 flag (GAP-35) |
| C11 | Error estimator for J | two-level Richardson K=4 | three-mesh observed-p GCI (Roache/Celik); DWR (Becker–Rannacher); LSQ multigrid | single-author at band sites ([X-O32] exists for O3.2 norms only) | AC3; GAP-9 | S25 extension (GAP-9) + R25 DWR |
| C12 | Start line | Sauer first-order, gamma=const, GENO-mirrored (+1e-6 offset) | Kliegel–Levine higher-order; Hall; displaced-IVL rejector | single-author (twin DATA CONTRACT — fidelity adjudicated, accuracy NEVER) | a1:719-727, :37-40; GAP-6/AC14 | S25 rejector; F4b/F5 higher-order if it fires |
| C13 | Axis unit process | GENO foot-ratio guard v1/y1 | L'Hopital dv/dy carried (Zucrow–Hoffman); MMS verification | single-author (GENO mirror; march-level verification NEVER) | a1:488-499, :566; GAP-8 | S25 gconst axis oracle |
| C14 | Exit-condition read point | axis-cell Me only | multi-point exit read + band | NEVER [J] | a1:853, :889 | folded into GAP-8 oracle |
| C15 | m_stop exit floor | 1e-5 GENO-mirrored (S19 knob) | mesh-coupled floor m_stop ~ C·da^2 | CONVERGED-measured (attribution diagnostic executed; STIM-1) | AC4 | — (residual: coupling documentary) |
| C16 | Newton damping ladder | (1,1/2,1/4,1/16,1/64,0), bare argmin non-increase | Deuflhard measured-contraction damping; Armijo sufficient decrease | NEVER (no recorded rationale) | a1:371, :397-416; GAP-29 | F2 engine rebuild |
| C17 | Trip cap N_NEWTON | 30 | derived from contraction budget | single-author (KAT proved it bites, not derived) | [X-CDKAT]; a1:145-148 | AUDIT F5 execution (S25) |
| C18 | Roundoff-floor constants | NEWTON_TOL_FACTOR=100, C_FLOOR=8 ("spike convention") | Higham op-count gamma_n; Moré–Wild noise floors | single-author (AUDIT F5 registered; test never executed) | AC9; GAP-29 | S25 halved-constants sweep |
| C19 | Certification metric scale | scalar sc = max(1, max|z|) | componentwise scaling (Deuflhard NLEQ; Higham) | single-author (AUDIT F8 adjudicated LOW) | AC8/Q1 | F2 hygiene with AUDIT F8 |
| C20 | Certificate qualification | unqualified one-extra-step ratio | kappa(J)-aware derived bound; Kantorovich/alpha-theory; branch-consistency monitor; interval-Newton [X-IVXC] | NEVER | GAP-3 | F2 (HIGH) |
| C21 | Seed validity policy | asserted O(h) predictor + stale replay seeds (C2-F2 mitigation) | alpha-theory per-seed certificate; Kantorovich radius ([X-TBAK] pattern in z) | NEVER | GAP-20 | S25 probe → F2 ledger row |
| C22 | Wall-foot search | linear index scan, full Newton per attempt, monotone-foot predicate | Brent on chord parameter + Shewchuk pre-filter → derived (N,Nv) | NEVER | GAP-28; toc:847-852 | F2 (rate lever) |
| C23 | Record-failure policy | full record then P4 gate | fail-fast early-abort (opt-in, schema'd) | CONVERGED-panel (speed audit H1 design of record) | AC7 | scheduled S25 item 8 |
| C24 | Thermo closure | [X-THC1] quintic C1 tables (backend-1) | NASA-direct (oracle only per C-A); dCp-ingest (gated C-B) | CONVERGED-panel (KEEP verdict fresh) | ADVISORY_S24_thermo_closure_survey §8 | conditions C-A..C-D open as named |
| C25 | Table box | literals 1050/3900 K, N_TAB=8192 | envelope-derived box + declared margin + per-run certificate | NEVER | GAP-11 | F2 (with C-C/C-D) |
| C26 | Out-of-box behavior | silent clamp (linear) / silent quintic extrapolation (C1) | traced flag + rejector covering BOTH modes | NEVER (registered conditional C-D, spec corrected) | AC6 | C-D owner F2 |
| C27 | Constraint aggregation | KS-min, rho = K_RICH ln(N)/mu0 (conservativeness-derived) | adaptive-KS (Poon–Martins); induced-exp/power (Kennedy–Hicken); two-constant rule | single-author (survey answered accuracy axis; conditioning axis NEVER) | GAP-27; AC12 | F2 (with GAP-1) |
| C28 | Cert-frontier representation | binary outside gates only (quantifier bridge falsified) | KS-max surrogate inside KKT, gates kept | NEVER (successor to falsified K_disc~A_0 absent) | GAP-1 | F2 (census row 10) |
| C29 | Mask freezing granularity | rung-frozen + C3 drift gate | segment-level re-freeze (P2 rhythm); smooth gate sigma(val/eps_gate) | CONVERGED-panel for rung-freeze, alternatives NEVER considered; C3 fired post-adjudication | GAP-13; panel C3 | F2 re-adjudication |
| C30 | Mask crop policy | overlap crop + occurrence counter | conservation-of-enforcement invariant (lost-lane count verdict-bearing) | NEVER | GAP-14 | S25 one-liner |
| C31 | Optimizer engine | scipy trust-constr (eq-path §4bis-adjudicated; IP path in use since S22) | IPOPT; filter SQP (Fletcher–Leyffer); SLQP; Uno; proximal-bundle (D6:738, never built) | CONVERGED for eq-path; IP path NEVER | GAP-15; kickoff §4bis | F2 [P-IPADJ] |
| C32 | Curvature policy | fresh full FD Hessian per segment, no carry (policy-bound) | SR1 carry from certified pairs + stale-symptom re-measure + directional rejector | single-author (R-3 cites no alternatives; survey NEVER) | AC10 | G0/T2 review, F2 entry |
| C33 | Constraint curvature | scipy default BFGS (no hess=) | exact HVP (fwd-over-rev) or FD-of-exact-gradient per segment | NEVER | GAP-19 | F2 (R2 pilot flag) |
| C34 | TR floor/caps | TR_FLOOR=1e-3, tr0=0.05, tr_cap=0.25 ("S18 clip") | noise-derived floor K_RICH·tol_dp/||g|| (Cartis–Scheinberg; Moré–Wild) | NEVER | GAP-4 | S25 arithmetic + F2 adoption |
| C35 | xtol | literal 1e-10 at every call site | Newton-floor-derived on u scale (derivation exists as prose only) | NEVER | GAP-33 | F2 one-liner |
| C36 | Scaling policy | Jacobi Dv measured once/walk, objective-only | per-segment refresh from diag(H) (free) + constraint-row equilibration (SNOPT) | NEVER | GAP-17 | F2 [P-DVREFRESH] |
| C37 | Segmentation trigger | any (N,Nv) flip ends segment | materiality-gated by replay-fidelity band; PC^1 active-set anticipation | NEVER | GAP-18 | F2 entry (G0/T2) |
| C38 | Outcome-II stationarity declaration | ratchet exhaustion + raw KKT-open number | B-stationarity certificate (convex-hull / surrogate residual); normalized reporting | NEVER | GAP-2 | F2 |
| C39 | Multiplier provenance | res.v raw (convention closed S24-T1) | complementarity band + LSQ re-estimate; AD post-optimality (Fiacco) via lip elimination | convention CONVERGED (T1); verification NEVER | GAP-12, GAP-32 | S25 band/counter; F2 LSQ |
| C40 | Lip equality handling | LinearConstraint row | variable elimination (N-W §15.3) | NEVER | GAP-32 | F2 |
| C41 | Band form/composition | K=4 pointwise two-level; ad-hoc sum/max/heterogeneous mixes | declared GUM/RSS policy; three-level GCI; topology-conditioned (LB-c2); running-max envelope (in-house) | NEVER (no composition policy anywhere) | GAP-7, GAP-9, GAP-10 | S25 policy + band pass |
| C42 | Safety constant K_RICH role reuse | one numeral, 8 roles | per-role derivations (GCI Fs on observed p; KS rho from Lipschitz scale; etc.) | NEVER (registered open row) | AC5 (R25) | R25 F2 audit + census annex |
| C43 | Asymptotic-range handling at band sites | presumed h^p at r=1,2 | per-site observed-order check (o32 estimator reuse) + NON-CONCLUSIVE propagation | NEVER | GAP-9 | S25 |
| C44 | FD steps (gradient/Hessian) | fixed sqrt(eps)·scale / eps^(1/3)·scale | Moré–Wild noise-aware per-column steps; seam-aware stencils | single-author (derived-for-smooth; kink-aware NEVER) | GAP-16 | F2 (with P-HESSREJ) |
| C45 | leggeAree bracket | hardcoded 400-point grid [1.01, 2.8]·as | box-derived q_max window; vectorization | single-author (registered: speed audit H2 + AUDIT) | AC16 | S25 speed session |

Reading of the ledger [S25-REPAIR, red-team MED: the original
"8/14/23" line was irreconcilable with this very table; recounted
per-row]: 5 rows DECIDED-converged (C3 constructional, C4
survey-decision [status repaired below], C15 measured, C23 panel,
C24 panel) + 3 MIXED converged/NEVER (C29, C31, C39), 12
single-author, 25 NEVER. Every NEVER row above carries a named owner
and placement — none remains a silent default after this advisory.

---

*End of advisory. Sources: 12 scratchpad facet files (6 finder positions
+ 6 adversarial verifications), S24 session log, PROGRESS census, M0
S20-S24 blocks, D6, AUDIT_agnostic_2026-08-07, S24 panel + thermo-survey
+ speed-audit advisories. Judge synthesis performed in one round;
quarantine items are open.*
