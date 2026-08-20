# VERDICT — BLOCCO 3 WAVE 1 (clusters C28 / C27 / C9+C11)
S-FOUNDATIONS-C2, 2026-08-19. Wave judge of record per
BRIEF_wave1_judge.md. BASE = validation/sfoundations_raws_2026-08-13.
Inputs read IN FULL: PANEL_C28.md, PANEL_C27.md, PANEL_C9C11.md,
refute_C28.md, refute_C27.md, refute_C9C11.md, BRIEF_wave1_panels.md,
BRIEF_wave1_refuter.md. This file is the only file written; ledger
edits happen at the landing window (proposals in §4).

## 0. NULL=FAILURE CHECK — PASS

All six slot files exist, are well-formed, and end with machine
summaries (panels: cluster/rows/census_recency/alternatives_closed/
inflation_check; refuters: findings/breaks/repairs/amendments/notes).
No dead slot; all four rows (C28, C27, C9, C11) are ADJUDICABLE this
wave. Refuter totals as filed: C28 = 0 breaks / 3 repairs / 5
amendments / 3 notes; C27 = 0/3/4/1; C9C11 = 0/5/8/1. Grand total 33
findings, 0 BREAKS-VERDICT anywhere.

## 0.1 Judge's independent source verification (this window)

Every citation this verdict relies on was re-read at source in this
window (SR-12: measured commands are mine, not inherited):

- Ledger rows verbatim: C9 :217-226, C10 :228-236, C11 :238-248,
  C27 :407-417, C28 :419-427, C42 :571-579, C43 :581-589
  (docs/choice_ledger.yaml).
- Diff anchors verbatim: BASE/phaseB_tree_diff.md:66-72 (C9 4/4),
  :76-81 (C11 4/4, inverted burden), :133-142 (C27 3/4 DIVERGENT
  HIGH — the 3/4 is the DIVERGENCE call, bundling exactness),
  :143-155 (C28 4/4 CONVERGENT-WITH-M0, "the ledger row lags the M0
  state").
- M0 verbatim: :2005-2011 ("Only K_budget may ever be enlarged; the
  certification floor is a tolerance and does not move"); :2058-2064
  (certdiag 8/8, rejections "bit-identical under N_NEWTON 30 -> 300
  with the floor untouched"); :2126-2132 (KKT WITH THE MARGIN
  MULTIPLIER, grad J = lambda grad g + mu grad m, mu >= 0);
  :2164-2177 (taxonomy anchor: class string is
  Known-Unrelaxable-Simulation-NONQUANTIFIABLE, phrase "the worst
  tractable kind"); :2318-2335 (S22 (v)/(vi) incl. "CANNOT capture
  the S20-instance certifiability frontier" + standing per-instance
  monitor rule); :2336-2353 ([X-MGOV]: KS-min bounds, rho = K_RICH
  ln(N)/mu_0_min, m_ref = 6.810298e-01, N = 3498, rho = 766.83, gap
  = 1.0641e-02, AD-vs-FD 3.29e-06 vs 5.92e-05); :2369-2375
  (adopt-or-declare motive clause).
- Facet s24_gap_driver-nonsmooth.md :15-39 verbatim: probes declared
  "pure python/scipy in the scratchpad"; Probe B numbers (7.1e-2,
  4.6e-11, mu=0.709, 2.9e-3); Probe C scipy 1.18.0 method switch
  (`n_ineq == 0 -> equality_constrained_sqp else tr_interior_point`);
  "The binary P4 gate stays as the verifier of record in every
  formulation".
- Gapmap :89-103 (Probe B labeled "measured", never "committed";
  "walk bit-comparable" is the gapmap's own unmeasured prediction;
  margin_factory vector-slot note) and :728-750 (GAP-27 full block
  incl. "curvature ~rho/4", "1/45 lanes above 1e-12, model-inferred —
  Q10", "[R3] argmin-swap census", "inherits the defect if
  underived", "two-constant rule keeps the conservativeness theorem
  intact") — verbatim.
- Findings rows verbatim: :1136-1144 (no-B-stationarity, [P-BSTAT]),
  :1182-1190 (observed-order: p_fine=2.5347, dp_tot=0.6704,
  9.48e-03 -> 1.42e-02, 0.415 bound, trigger text), :1236-1244
  (ip-path: "any inequality switches the method", "GAP-1 adoption
  makes the IP (or replacement) engine PERMANENT"), :1468-1476
  (D-49: trigger IS two-armed — "F2 window, OR the first new DWR-bar
  claim of record").
- Literature registry verbatim: :199-208 (ancourt_peter_atinault_2023,
  READ-INTEGRAL, on disk in two roots, "ACE residuals as code
  verification", arXiv:2305.03499 = its own preprint) and :491-498
  (giles_pierce_2001).
- Trees verbatim: P-F16 :614-633 (recommendation "O2 in-loop +
  O3-style adaptive phase refinement", mandatory post-hoc sweep);
  O-F18 :1031-1049 ("4 wrapped around 2 ... KS within the working
  set", P3 dry proof rho = ln(m)/eta_KS); H-F24 :774-795 ("a
  certificate is not tradeable"; multiplier-prices clause; LICQ
  falsifier); V-F32 :1400-1411 ("arguably the most distinctive
  structural choice", margin-lies falsifier); P-F33 :1206-1212
  ("grind or lie"; boundary-ambiguity falsifier).
- Code witnesses measured: a1_toc_variational_jax.py :935-938 =
  build-time dummy certification (NOT the P4 gate), P4-gate string at
  :1520, P3(ii) gate site at :1849+, margin_factory at
  :1257/:1346/:1912-1913, :1179-1182 = thrust_J;
  a1_ideal_march_jax.py :194 (da_deg=0.5 — real-valued), :198
  (K_RICH = 4.0), :1459 (deployed band = K_RICH * |w@(dv_h - dv_h2)|
  + floor — NO r^p arithmetic); o32_mesh_convergence.py :24-41
  (pre-registered h-independent window, d = 2 x coarsest spacing;
  "RATE ESTIMATOR — DERIVED, NOT log2 OF TWO LEVELS"), :470 (knobs
  refined separately), :555-559 (`cells` printed separately from
  NI/Nw); o33_bench.py :124-129 (two-resolution Richardson x reused
  K_RICH = 4).
- Greps re-run this window: `git ls-files | grep -i probe_b` -> 0
  hits (no committed Probe B script); cava `grep -n "C28"` -> FIVE
  hits {36, 854, 1116, 1231, 1245}; cava
  `grep -inE 'C27|Poon|Kennedy|Kreisselmeier|aggregat|semi-infinite|exchange'`
  -> EXACTLY {1115, 1230}; ledger `grep -nE 'C42|K_RICH'` -> includes
  header hits :71 and :81 naming C43 (plus :409, :489, :571..., :649).
- Judge pen-grade re-derivations: RC28-4 band arithmetic (shifted
  KS-max enforcement -> worst-case certifiable-but-excluded band
  width 2 ln(N)/rho — CONFIRMED); RC27-1 per-group arithmetic
  (rho_g = K_RICH ln(d_g)/mu_0; ln 55/ln 3498 = 4.007/8.160 = 0.491 —
  CONFIRMED); RC27-3 falsifier-partition holes alpha/beta/gamma
  (predicate logic re-checked — all three genuinely unassigned);
  RC911-6/8 coverage arithmetic (K >= 2^p/(2^p-1) <=> p >= log2(4/3)
  = 0.415 — CONFIRMED; reserves at p=2, r=2: coarse 4/(4/3) = 3x,
  fine 4/(1/3) = 12x — "10x" matches neither).

Refuter claims NOT independently re-fetched: external web items
(Ziems-Ulbrich lineage, grouped-aggregation TO papers, Fidkowski-Luo
space-time line, Samakhoana-Grimmer page details). These enter only
at the evidence level the refuters state (search/abstract/page
level); no verdict below leans on them beyond census-completeness and
evidence-level labeling, and every closure that uses them also
carries an internal derivational or of-record leg verified above.

---

## 1. ADJUDICATION OF EVERY REFUTER FINDING (33/33)

Classes: SUSTAINED (class) / OVERRULED (reason) / RECLASSED.
Verdict-relevant sustained REPAIR-NEEDED findings are all
repairable-by-amendment on the page: the repair text is adjudicated
and CARRIED (applied at the landing window). Zero escalations.

### 1.1 Cluster C28 (11 findings)

- **RC28-1 SUSTAINED — REPAIR-NEEDED.** Pin F-3 as written misfires:
  verified of record that ANY inequality switches scipy trust-constr
  to tr_interior_point (facet Probe C :36-39; findings :1239), the
  S18 record walk is equality-only, and "bit-comparable" is literal
  in this repo (M0:2058-2064) — the pin would fire on the engine-path
  switch, discriminating nothing about pricing cost; the threshold is
  an unrecalibrated transplant of the gapmap's own unmeasured
  prediction (gapmap :91-92) — R-4. REPAIR CARRIED (adjudicated
  sound): re-pin F-3 at MATCHED engine path/constraint set (same walk
  re-run identically except the cert row, or governor-armed IP-vs-IP
  A/B per findings :1243); pass = mu_c = 0 strictly at every accepted
  iterate AND J/step-count/record-count deltas inside the existing
  derived bands; bitwise comparison claimed ONLY where the path is
  provably identical; the path-switch delta itself routes to
  [P-IPADJ] (already on the duty's critical path).
- **RC28-2 SUSTAINED — REPAIR-NEEDED.** "Probe B ... (committed)" is
  false of record, stated three times: measured this window,
  `git ls-files` has no probe_B script; the facet declares
  scratchpad-run (:23-25); the gapmap says "measured", never
  "committed" (:93). R5 makes the label load-bearing. REPAIR CARRIED:
  relabel everywhere as "scratchpad-run, reproduced by both S24
  verifiers, numbers carried in the committed advisory (gapmap
  :93-96; facet :28-35)"; F2 duty gains the clause that the
  [P-CERTKS] pilot commits its own carrier + test before any
  Probe-B-class number enters a Verdict.
- **RC28-3 SUSTAINED — REPAIR-NEEDED.** The adaptive-accuracy/inexact
  TR-SQP family (Ziems-Ulbrich SIOPT 2011 lineage; Kouri-
  Heinkenschloss) is a real fifth representation family — adapt the
  tolerance/budget demands so the frontier moves with the optimizer —
  absent from options AND census (q5 is failure-penalization; no §3.5
  row); under §0.2 it currently loses by omission. REPAIR CARRIED
  (closure adjudicated sound on anchors verified this window): add
  the family as option row §3.5.9, CLOSED by stated reason on both
  halves of K = K_phys ∩ K_budget — (i) the tolerance half is a
  certificate: "the certification floor is a tolerance and does not
  move" (M0:2010-2011), the honesty frame forbids floor motion (facet
  :18-21); (ii) the budget half is the only enlargeable half and its
  enlargement is MEASURED non-binding at the frontier instances
  (certdiag 8/8, bit-identical under N_NEWTON 30 -> 300, M0:2058-2062).
  Admissible at most as F2 budget-scheduling economics OUTSIDE the
  verdict loop. This also arms the census-bounded absence claim
  against the obvious referee counter.
- **RC28-4 SUSTAINED — AMENDMENT (carried).** Judge re-derivation
  confirms: with max r <= KSmax <= max r + s (s = ln(N)/rho) and the
  adopted SHIFTED enforcement KSmax <= 1 - s, the
  certifiable-but-possibly-excluded band is max r in (1 - 2s, 1] —
  worst-case width 2 ln(N)/rho, not ln(N)/rho (the stated gap is the
  KS-MIN governor bound, M0:2338-2339, transplanted without
  recalibration). CARRIED: state the <= 2 ln(N)/rho band (or
  adjudicate shift-vs-no-shift explicitly — the unshifted form is
  already sufficient with band s; the shift buys F-1's robustness);
  duty item 2 reports the REALIZED exclusion band on the
  frontier-class walk.
- **RC28-5 SUSTAINED — AMENDMENT (carried).** All four stale anchors
  verified this window: P4 gate at ~:1520 not :935-938 (build-time
  dummy check); P3(ii) at :1849+ not :1158-1161 (engine-cache key);
  margin_factory at :1257/:1346/:1912-1913 not :1179-1182 (thrust_J);
  D6 bundle line at :743 not :738. Every named OBJECT exists as
  described — anchor fixes only, with gapmap-era line refs tagged
  "(gapmap-era lines; current sites: ...)" when quoting the gapmap as
  the gapmap.
- **RC28-6 SUSTAINED — AMENDMENT (carried).** "Every census axis
  reaches >= 2023" is false for axis 1 (newest = AIAA kriging 2021,
  refuter-verified). CARRIED: correct to "axes 2-5 reach >= 2023;
  axis 1 newest = 2021 here — its modern refinement layer is C27's
  mandate (interplay already named)".
- **RC28-7 SUSTAINED — AMENDMENT (carried).** Measured this window:
  cava "C28" grep = FIVE hits {36, 854, 1116, 1231, 1245}, not three.
  All five are the cava's own numbering-collision family; the
  panel's CONCLUSION (the ratified cava contributes no row to this
  cluster) survives on all five. CARRIED: correct count + line list.
- **RC28-8 SUSTAINED — AMENDMENT (carried).** O-F20's falsifier
  trigger ("inner-region optimum presses the provable boundary with
  POSITIVE MULTIPLIER") was never evaluated — no provable inner
  region was derived and no mu of record exists (O1 OPEN,
  M0:2256-2259). CARRIED: rewrite "already past that trigger" as the
  a-fortiori INFERENCE it is. The (c) re-scope stands independently
  on the measured S22 (v)/(vi) (verified M0:2318-2335).
- **RC28-9 SUSTAINED — NOTE.** Verified M0:2167-2171: class =
  Known-Unrelaxable-Simulation-NONQUANTIFIABLE (Known, not Hidden);
  phrase = "the worst TRACTABLE kind". One-line census wording fix
  rides the amendment package; adjudication unchanged (remedy
  identical).
- **RC28-10 SUSTAINED — NOTE.** Pipeline-sense R1's same sentence
  names "GAP-1's in-KKT certification surrogate" among the NAMED
  EXITS — the proposed ledger-row edit is half-written in the record.
  Consumed in the §4 ledger-delta text: the C28 note edit quotes R1's
  full sentence, converting the "ledger lags M0" crux from panel
  assertion into record.
- **RC28-11 RECLASSED NOTE -> AMENDMENT (carried).** P-F33's
  boundary-ambiguity falsifier (verified :1210-1212) is the one tree
  falsifier with no counterpart among the pins, it is cheap, and it
  is exactly R5-grade reporting. CARRIED as new reporting pin F-4:
  mu_c and KSmax at the returned base ship with their derived bands;
  a base whose surrogate-active margin sits inside its own band is
  declared BOUNDARY-AMBIGUOUS, not optimal. (C38-adjacent: the pin is
  reporting-only here; C38's own adjudication stays open.)

### 1.2 Cluster C27 (8 findings)

- **RC27-1 SUSTAINED — REPAIR-NEEDED.** Grouped/block/regional
  (partitioned) aggregation is a real census family (stress-TO
  lineage, abstract-level witnesses named) absent from the candidate
  set (a)-(l) — §0.2 violation; and it falsifies the §3.1 escape
  taxonomy as stated (grouping shrinks effective d INSIDE the smooth
  class). REPAIR CARRIED (closure derivation judge-verified): add
  option (m); CLOSE as primary by stated reason — per-group gap pin
  mu_0/K_RICH forces rho_g = K_RICH ln(d_g)/mu_0, so the 1/mu_0 depth
  blow-up is unchanged and grouping buys only ln(d_g)/ln(N) (~0.49
  for d_g ~ 55 of N = 3498); argmin-tie chatter persists within
  groups (tied lanes are typically adjacent, hence co-grouped);
  ADJUDICATE per-group fencing as an optional fence refinement inside
  the adopted structure (better-conditioned fence at the same pin,
  zero extra VJP beyond the vector rows); extend the escape list with
  the structural-vs-constant distinction; add the three items to the
  §4.3 literature-row proposal.
- **RC27-2 SUSTAINED — REPAIR-NEEDED.** Arm B under-specified (the
  vector slot is capable but nothing pins arity/cadence — gapmap
  :101-103 verified); the w-derivation is circular as written
  ("band-adjacent" presupposes w); the certificate-equivalence guard
  is ambiguous between TR-step accept/reject (contradicts the
  design — rejected-step RATE is the metric) and rung-level
  enforcement verdicts. REPAIR CARRIED: pin band refresh cadence;
  fixed arity k_max derived from the recorded walks' max near-binding
  count, padded with provably-inactive rows (constants derived, R5);
  re-found w = K_RICH x max over the recorded walk over ALL lanes of
  the per-accepted-step |Delta v_i| (well-founded, conservative
  superset of the circular form); guard reworded to "identical
  rung-level enforcement verdicts at the declared resolution".
- **RC27-3 SUSTAINED — REPAIR-NEEDED.** The falsifier set does not
  partition the outcome space — judge re-checked the predicates:
  branches (alpha) conflict-fires-but-A-healthy, (beta) A-fails-AND-
  B-fails (reachable today only via band-escape, which beta does not
  require), (gamma) A-fails-with-NO-conflict are genuinely
  unassigned. REPAIR CARRIED: (alpha) -> rho_curv re-derivation duty;
  two-constant trigger demoted to declaration-only until re-derived;
  (beta) -> operator question re-opens, escalation to the named AL
  fallback or the binding-arc route WITHOUT the band-escape
  precondition; (gamma) -> the two-constant trigger is falsified as
  insufficient (its §4.1(2) role re-adjudicated), band mandated by
  measurement at that rung.
- **RC27-4 SUSTAINED — AMENDMENT (carried).** The §3.1 "wall" leans
  on an Optimization Online PREPRINT (statement page-verified, proof
  unchecked in-repo, no peer review), stated for smoothings of max in
  the infinity norm — the ~1.23x-in-rho transfer to the incumbent's
  curvature normalization is underived on file; and the theorem
  bounds FIXED smoothings, so extending it against adaptive-KS is an
  over-reach (adaptive-KS stays closed on its two independent legs:
  motive void of record M0:2369-2375 + measured direction-wrong on
  GAP-27). CARRIED: carry "preprint, statement page-verified, proof
  not checked" into §2.3/§3.1; restate the wall qualitatively (gap x
  smoothness ~ ln d lower bound) or add the norm bridge; replace "the
  census theorem guarantees" with "the trigger is arithmetic on
  derived constants; the preprint theorem predicts the conflict at
  depth". The verdict survives both worlds by design (F-C27-2 covers
  the no-conflict branch).
- **RC27-5 SUSTAINED — AMENDMENT (carried).** Measured this window:
  the TRUE cava hit set for the panel's stated pattern is EXACTLY
  {1115, 1230}; lines :83/:1117 contain no pattern token; the pattern
  is language-blind on the Italian corpus (cannot see "aggregazione",
  "scambio", "semi-infinito"). The material absence conclusion
  survives inspection (refuter inspected :660/:1182 = D-12 cross-mode
  OBJECTIVE-measure aggregation, out of scope; :1117 = cava C30,
  consumed by direct read). CARRIED: correct §2.4 hit set; re-run
  with bilingual stems and record the result; declare D-12
  inspected-adjacent.
- **RC27-6 SUSTAINED — AMENDMENT (carried).** Verified at source:
  P-F16 recommends KS KEPT in-loop (:628-633) — working-set/exchange
  STRUCTURE advocacy is 2/4 (O-F18, V-F23); "3/4" is the diff's
  DIVERGENCE call (:133-142), which bundles the exactness challenge.
  And the adopted inst-L design (explicit band rows + KS fence on the
  COMPLEMENT) INVERTS O-F18's "KS within the working set" (:1031-1032)
  — it is panel-designed structure, honestly declared but
  mis-headlined. CARRIED: attribute 2/4 advocacy + 3/4
  diff-divergence; mark the band+fence design as panel content (tree
  advocacy covers the inst-XI exchange semantics; RC27-8(i)'s
  epsilon-active census precedent may be attached); word the
  converged half as the four items — two-constant derivation repair,
  band block as the DERIVED escalation route, inst-XI covering +
  mandatory post-hoc sweep semantics, multiplier reporting — with
  hybrid production adoption conditional on the measured half (no
  flip-flop if F-C27-2 fires).
- **RC27-7 SUSTAINED — AMENDMENT (carried).** Two load-bearing
  context elements used by the verdict are absent from the frozen
  statement: the G1/REQ-NONSTALL globally-finite-scalar duty (decides
  the incumbent's retention and closes part of (j)/(k)) and the
  fixed-shape/jit requirement (drives RC27-2). CARRIED: add both to
  §1; (j)/(k) closures re-checked against them — closures stand.
- **RC27-8 SUSTAINED — NOTE.** Items consumed into §4: (ii) the
  blind-tree "independently confirmed" claim on derived-rho is
  pattern-level (target eta_KS differs from mu_0/K_RICH) — wording
  softened in the carried text; (iv) the C42 role-count DELTA (band
  width w + chatter red-line multiplier = new K_RICH roles) is
  explicitly notified to the wave-3 audit in the C42 note delta;
  (v) SR-9 arithmetic corrected to 6 queries + 1 page fetch;
  (vi) alternatives_closed counting rule stated at landing;
  (i)/(iii) ride the amendment package as strengtheners.

### 1.3 Cluster C9C11 (14 findings)

- **RC911-1 SUSTAINED — REPAIR-NEEDED (row C11).** C43
  (choice_ledger.yaml:581-589, verified verbatim) is decided in
  substance by C11 pins 1-2: C43's listed alternative ("per-site
  observed-order check (o32 estimator reuse) + NON-CONCLUSIVE
  propagation") IS the adopted interim regime. The panel's own grep
  returned header lines naming C43 (:71/:81 — reproduced this window)
  and the report dropped them. Landing C11 as proposed would leave a
  NEVER row whose question was decided elsewhere — the exact
  anti-entropy failure the R7/SR guards exist for. REPAIR CARRIED
  (option 1 adjudicated as the correct one): the landing marks C43
  ADJUDICATED-WITH-C11 (content identity, not a fresh adjudication —
  the adopted alternative is C43's own listed alternative; measured
  half = F2-C11-ESTIMATOR-CAMPAIGN leg (a); GAP-9 is both rows' annex
  pointer). Exact delta text in §4.5. Deferral (option 2) is
  REJECTED: it would keep a materially-decided question formally
  open.
- **RC911-2 SUSTAINED — REPAIR-NEEDED (row C9).** F9a's cost matcher
  equates two different meters — witnesses verified (o32 refines
  NI/Nw/da separately, prints `cells` separately; AC2 insertions
  carry position-dependent point counts): equal column count does not
  imply equal unit-process count, so E_A < E_U could be bought with
  resolution, not placement — the REFUTES-ADAPTATION arm could be
  unable to fire by construction. REPAIR CARRIED: matched cost is
  defined on TOTAL UNIT-PROCESS COUNT (the meter the pin itself
  names); the column-count equation is deleted; the F2-C9 duty
  reports both counts per arm.
- **RC911-3 SUSTAINED — REPAIR-NEEDED (row C9).** The F9a promotion
  threshold ("factor 2 = the smallest ratio distinguishable ...") is
  asserted-derived with no cited widths/sites/arithmetic (R5), and
  "twice in a row" is an undeclared repetition knob. REPAIR CARRIED:
  F2-C9-MESHLAW-CAMPAIGN publishes the derivation (site list,
  measured [X-O32] band widths, implied smallest distinguishable
  ratio) BEFORE first use of the promotion arm; the instantiated 2
  stands only as the pre-derivation placeholder governed by the
  honestly-pinned "threshold rises with wider bands" rule; "twice in
  a row" is classed variance-derived or declared-governance.
- **RC911-4 SUSTAINED — REPAIR-NEEDED (row C11).** F11a's twin arm
  presumes a "verified fine-ladder extrapolation" that does not exist
  today — the twin's observed order is NON-CONCLUSIVE of record
  (findings :1185, verified) — and §4.2 never orders leg (a) before
  leg (b). Unrepaired, the promotion gate is not a falsifier. REPAIR
  CARRIED: leg (a) is ORDERED before leg (b)'s twin arm; the twin arm
  is valid only at sites where leg (a) delivers a CONCLUSIVE observed
  p; degraded-p sites contribute only via the propagation-rule band;
  promotion on the Giles-Pierce oracle alone must be declared
  ORACLE-ONLY.
- **RC911-5 SUSTAINED — REPAIR-NEEDED (row C11).** The on-disk,
  READ-INTEGRAL Ancourt-Peter-Atinault 2023 row (literature registry
  :199-208, verified; "ACE residuals as code verification";
  arXiv:2305.03499 is its own preprint — same line as Lozano-Ponsin
  2025) is the closest existing published object to the
  characteristic-native residual the duty must build, and the panel's
  estimator-token greps could not see it — navigation-first defect
  (local sweep before procurement). REPAIR CARRIED: (i) leg (b) names
  ancourt_peter_atinault_2023 as a CONSUMED formulation input (held
  anchor of the adjoint-along-characteristics line, Lozano-Ponsin
  2025 as its extension); (ii) §2.4's nearest-hits line corrected to
  name the on-disk paper as nearest. The §2.4 absence claims
  themselves survive (Ancourt is equations + verification residuals,
  not a J-error estimator). Verdict strengthened.
- **RC911-6 SUSTAINED — AMENDMENT (carried, row C11).** The deployed
  band is K x |Delta| + floor with no r^p arithmetic (verified
  :1459); "ASSUMED order p=2" over-weakens the incumbent inside the
  frozen statement (mild anti-incumbent smuggle). The panel's
  adjudication used the CORRECT arithmetic (0.415 bound re-derived by
  this judge). CARRIED: restate the incumbent as "h^p asymptotics
  presumed, coverage bought by K alone".
- **RC911-7 SUSTAINED — AMENDMENT (carried, row C9).** da is
  real-valued (da_deg=0.5, verified) — "four per-run integers" is a
  mis-type. CARRIED: "four per-run mesh parameters".
- **RC911-8 SUSTAINED — AMENDMENT (carried, row C11).** "10x
  conservativeness reserve" is unsourced; the derived pair is 3x
  (coarse) / 12x (fine) — judge re-derived. CARRIED: replace with the
  derived pair or delete. (Incumbent loses on the confirmed defect
  regardless.)
- **RC911-9 SUSTAINED — AMENDMENT (carried, row C11).** D-49's
  trigger is TWO-ARMED of record ("F2 window, OR the first new
  DWR-bar claim" — verified :1476); the panel quotes only the second
  arm, so the DWR-failure path would silently drop the probe.
  CARRIED: D-49 lands in the F2 window in BOTH F11a branches.
- **RC911-10 SUSTAINED — AMENDMENT (carried, row C9).** "No longer
  the program's answer to C9" overstates against F9a's own
  refutation arm (which can close C9 on uniform+A36). CARRIED:
  "target-law status presumptive pending F9a".
- **RC911-11 SUSTAINED — AMENDMENT (carried, row C11).** The C11 half
  lacks C9's standing-verdict sentence and pin 2's regime is
  unexecutable until leg (a) lands (no observed-p certificates exist
  at band sites today — that IS GAP-9). CARRIED: standing
  Richardson-banded verdicts of record STAND with the row-:1182
  CONFIRMED flag attached (the retirement is of the premise's
  epistemic status, not a voiding); any pre-F2 band-bearing verdict
  either runs the ALREADY-BUILT [X-O32] three-level estimator at its
  own sites or declares the row's trigger ("next band-bearing verdict
  at an unverified observed order") fired.
- **RC911-12 SUSTAINED — AMENDMENT (carried, row C11).** The
  space-time/unsteady output-based DWR line (Fidkowski-Luo JCP 2011;
  Fidkowski JCP 2017; CMAME 2022 — refuter search-proven) is the
  published corpus of DWR on MARCHED (time-like) solves and the
  nearest template for the characteristic-native build; its absence
  makes §2.2's "modern refined layer is REACHED" an overstatement
  (the §2.4 absence claims survive as bounded by Q9's literal terms).
  CARRIED: add the line to the census and to leg (b)'s inputs; WANTED
  rows ride the same registration duty; soften the §2.2 sentence.
- **RC911-13 SUSTAINED — AMENDMENT (carried, row C9).** F9b's
  "rejection attributable to remeshing" has no defined attribution
  test (R-4 transplant of H-F27's falsifier). CARRIED: re-run the
  rejected step on the frozen pre-re-mesh topology; acceptance there
  attributes the rejection to remeshing. (The O3.1-floor half of F9b
  is already operational — hence AMENDMENT, not REPAIR.)
- **RC911-14 SUSTAINED — NOTE (cluster).** Consumed into §4: (i)
  alternatives_closed counting rule stated at landing; (ii) F11b
  completed — DWR eta computed EVERY solve, solves between
  checkpoints inherit the last measured population band, referee
  comparison at checkpoints; (iii) the signed-estimate vs
  absolute-indicator distinction written into leg (b)'s spec.

**Adjudication totals: 33 findings — 33 SUSTAINED (1 of them
RECLASSED NOTE -> AMENDMENT), 0 OVERRULED. Sustained classes: 0
BREAKS-VERDICT, 11 REPAIR-NEEDED, 18 AMENDMENT, 4 NOTE. All 11
repairs adjudicated repairable-by-amendment on the page; all 29
repair+amendment texts CARRIED to the landing window. ZERO
escalations to full Form-2.**

---

## 2. PER-ROW VERDICTS (the deliverable)

### 2.1 Row C28 — cert-frontier representation

**VERDICT: measurement-gated CONVERGED-ON-PROTOCOL (formal half
CONVERGED-panel), as repaired.** The proposed outcome survives an
adversarial refutation that verified every M0/tree/diff/registry
anchor and hunted its inflation candidates (one dropped after source
fetch); the three repairs move pins and provenance labels, not the
direction.

- **Adopted choice (formal half, converged now):** HYBRID
  PRICED-FRONTIER representation — the M0 tier-ladder /
  KKT-with-margin-multiplier formalization of record (M0:2111-2185;
  grad J = lambda grad g + mu grad m, mu >= 0 verified at :2126-2132)
  — with the ledger's listed alternative (b) instantiated for the
  NUMERICAL certification frontier by the GAP-1 spec: KS-max
  surrogate on the traced per-cell certification ratios r_i(W),
  derived rho, stratum-local, wired through the margin_factory slot
  (current site :1257/:1912-1913); P4/P3(ii) binary gates KEPT as
  absolute adjudicators (facet :21 verbatim: "The binary P4 gate
  stays as the verifier of record in every formulation"); physical
  margins stay priced by the existing [X-MGOV] governor; solvability
  regions re-scoped to the physical family (wave-2). The incumbent
  "binary outside gates only" is SUPERSEDED AS SOLE REPRESENTATION
  and retained as the absolute verifier layer.
- **Stated reasons that survived refutation:** (1) three outcome-II
  records (S20/S22/S24) where the KKT system is structurally
  incapable of closing at frontier-pinned points, and the reported
  "KKT OPEN" residual measures the WRONG problem (GAP-1/GAP-2;
  findings :1136-1144); (2) the surrogate prices the SAME field the
  gate checks — conservative-side inequality is a THEOREM at fixed
  stratum, not a bridge conjecture, honoring the S22 standing rule
  (M0:2325-2327) via pin F-1; (3) the taxonomy remedy of record is
  "quantify a margin" (M0:2164-2177); (4) 4/4 blind-tree convergence
  used as evidence under content adjudication (diff :143-155:
  CONVERGENT-WITH-M0 — "the ledger row lags the M0 state"); (5) nine
  alternatives (now incl. adaptive-accuracy/inexact SQP, RC28-3)
  closed by stated reason, none by omission.
- **Evidence level held (zero inflation):** ADOPTED-FOR-MEASUREMENT,
  not adopted-of-record. Probe B evidence = scratchpad-run analytic
  toy, reproduced by both S24 verifiers, numbers carried in the
  committed advisory (RC28-2 relabel) — NOT a committed carrier;
  census-bounded absence claim stays query-bounded (7 queries).
- **Pinned protocol + falsifiers (as repaired, quoted):**
  - F-1 (surrogate-lies rejector): any iterate ACCEPTED by the model
    (KSmax <= 1 - ln(N)/rho) that FAILS record P4/P3(ii)
    certification => stratum contract violated in flight; surrogate
    DEMOTED to diagnostic, incumbent (a) stands, row re-opens.
  - F-2 (pricing-fails): on the frontier-class walk, if the AUGMENTED
    KKT residual does not close below the existing derived gtol chain
    AND [P-BSTAT] refuses B-stationarity => the priced representation
    did not upgrade the verdict; escalate to the engine
    re-adjudication ([P-IPADJ]/C31, bundle fallback named) BEFORE any
    further C28 claim. F-2 firing refutes the ADOPTION, not the M0
    formalization.
  - F-3 (cost falsifier, REPAIRED per RC28-1): MATCHED engine
    path/constraint-set A/B (same walk re-run identically except the
    cert row, or governor-armed IP-vs-IP per findings :1243); pass =
    mu_c = 0 strictly at every accepted iterate AND
    J/step-count/record-count deltas inside the existing derived
    bands; bitwise only where the path is provably identical;
    path-switch delta routed to [P-IPADJ].
  - F-4 (boundary-ambiguity reporting pin, NEW per RC28-11): mu_c and
    KSmax at the returned base ship with derived bands; a
    surrogate-active margin inside its own band => the base is
    declared BOUNDARY-AMBIGUOUS, not optimal.
  - Reporting pins: mu_c only under the B-stationarity qualifier
    until O1 discharged (M0:2256-2259); KKT residuals normalized
    alongside raw; conservatism band stated as <= 2 ln(N)/rho for the
    shifted form (RC28-4), with the REALIZED band reported by the
    duty; every number in the eventual Verdict ships with its
    committed script + band, and the [P-CERTKS] pilot commits its own
    carrier + test before any Probe-B-class number enters a Verdict
    (RC28-2).
- **BINDING F2 duty:** [P-CERTKS] pilot + [P-BSTAT] B-stationarity
  certificate (the GAP-1/GAP-2 window), with [P-IPADJ] on the same
  critical path — registrations already of record (gapmap :96-98,
  :133-135; findings :1136-1144, :1236-1244); duty items 1-3 as in
  PANEL_C28 §4 with the RC28-1/-2/-4 clauses added.
- **Escalation: NONE.**

### 2.2 Row C27 — constraint aggregation

**VERDICT: measurement-gated CONVERGED-ON-PROTOCOL, as repaired
(converged half re-worded per RC27-6).** The panel's structure
survives; the refuter's repairs make the duty executable and the
alternative set complete.

- **Converged half (adopted now, the RC27-6 wording of record):**
  (1) two-constant rule adopted as DERIVATION REPAIR + ex-ante
  escalation trigger — rho := min(rho_gap, rho_curv), both derived;
  rho_gap > rho_curv at a rung DECLARES smooth-only
  infeasible-by-derivation at that rung and mandates the band block
  (the trigger is arithmetic on derived constants; the page-verified
  PREPRINT theorem predicts the conflict at depth — RC27-4 wording);
  (2) the near-binding band block (explicit vector rows through the
  margin_factory slot + incumbent KS fence on the complement) as the
  DERIVED ESCALATION ROUTE — panel-designed structure (tree advocacy
  2/4 covers the exchange semantics; diff divergence 3/4;
  epsilon-active census precedent attachable), production adoption
  CONDITIONAL on the measured half; (3) inst-XI certificate semantics
  (obligation, conditional on the cycle-problem window): measured-L_xi
  covering margin m >= L_xi*Delta_xi/2 + MANDATORY post-hoc
  fine-phase sweep — a violating phase between nodes VOIDS the
  certificate; (4) multiplier reporting: per-lane atoms where the
  band is active ((ii) marginal-value carriers), softmax weight
  distribution + n_eff where only KS is active. The incumbent KS-min
  derived-rho REMAINS the fence, the G1/REQ-NONSTALL surrogate
  everywhere, and the sole operator wherever the two-constant check
  passes; its conservativeness theorem and the measured instance
  (m_ref = 6.810298e-01, N = 3498, rho = 766.83, gap = 1.0641e-02 —
  verified M0:2341-2343) are untouched.
- **Alternatives:** eleven closed by stated reason (adaptive-KS,
  induced/p-norm primary, MPCC operator, CVaR/chance, scenario,
  exact-penalty NCP, interval enclosure, AL-all-local primary [named
  fallback], discretize-all-only, LSE-Hessian-shift, + grouped/
  regional aggregation (m) added and closed per RC27-1 with per-group
  fencing absorbed as optional refinement). Counting rule stated at
  landing (RC27-8(vi)).
- **Pinned protocol + falsifiers (as repaired, quoted):** duty
  **F2-DUTY-C27-AGGCOND** (subsumes gapmap [R3] argmin-swap census;
  window = the GAP-27/GAP-1 F2 window of findings row
  `margin-governor:G1-three-jump-channels`). Instances: recorded S22
  mild (rho = 766.83) + S24 deep-DEF (rho = 5.75e4) on the
  pre-registered floor ladder mu_0_k = m_ref/2^k, k=1..4. Arms: A =
  incumbent pure KS-min; B = band + fence with RC27-2's pins (band
  refresh cadence pinned; fixed arity k_max derived from the recorded
  walks' max near-binding count, padded with provably-inactive rows;
  w = K_RICH x max over the recorded walk over ALL lanes of
  per-accepted-step |Delta v_i|). Guard: identical RUNG-LEVEL
  ENFORCEMENT VERDICTS at the declared resolution (any divergence =
  protocol red). Falsifiers F-C27-1 (kills pure-KS-at-depth),
  F-C27-2 (kills the hybrid's necessity — shelved as escalation-only,
  incumbent re-labeled CONVERGED-measured with the two-constant
  declaration added to [X-MGOV]), F-C27-3 (kills the band
  construction; repeated escape -> named AL fallback), F-C27-4
  (inst-XI limb), F-C27-5 (multiplier semantics, non-blocking) PLUS
  the RC27-3 completion: (alpha) conflict-fires-but-A-healthy ->
  rho_curv re-derivation, trigger declaration-only until re-derived;
  (beta) both arms out of band -> operator re-opens, AL/binding-arc
  escalation without band-escape precondition; (gamma)
  A-fails-no-conflict -> two-constant trigger falsified as
  insufficient, band mandated by measurement at that rung.
- **Status transition proposed:** SINGLE-AUTHOR -> ADJUDICATED-SPLIT
  (structure/protocol converged 2026-08-19; conditioning axis =
  measured F2 duty open).
- **Escalation: NONE.**

### 2.3 Row C9 — march mesh law

**VERDICT: measurement-gated CONVERGED-ON-PROTOCOL, as repaired.**
The 4/4 challenge is sustained on content; the incumbent's
production-loop case is genuine and keeps it the interim
verdict-bearing law.

- **Converged direction:** goal-oriented, characteristic-native
  adapted placement is the TARGET production mesh law — status
  PRESUMPTIVE PENDING F9a (RC911-10 wording); the uniform-per-run
  incumbent is retained as the interim certificate law (no verdict of
  record moves; certificates bind to the o32 pre-registered window on
  uniform families — verified :24-41). Adopted now: the A36 derived
  spacing law as a static arm (refinement-only; constants from
  (gamma, rtu, yt); the IVL is NEVER moved — the cava row's own
  rejector, cited); the AC2 column-local C- insertion primitive as
  the adaptation mechanism of the F2 build, driven by the
  characteristic-native goal indicator (the [X-AKNO] f2 = -lambda2
  mechanism transferred from knots to march columns — transfer = the
  hypothesis under test; 41.8% is a knot-side prior, not a march-side
  claim).
- **Pinned falsifiers (as repaired, quoted):**
  - F9a (adaptivity value, REPAIRED per RC911-2/-3): same design,
    same phase set, matched TOTAL UNIT-PROCESS COUNT (both counts
    reported per arm; the column-count equation deleted); E_U vs E_A
    against the [X-O32]-verified reference with its own band. REFUTES
    ADAPTATION: E_A >= E_U outside the joint band on the
    pre-registered twin sites -> C9 CLOSES on uniform+A36, AMR
    dropped as production law. REFUTES THE INCUMBENT-INTERIM:
    E_A <= E_U/2 twice in a row at matched cost — with the threshold
    derivation (site list, measured [X-O32] band widths, implied
    smallest distinguishable ratio) PUBLISHED by the duty BEFORE
    first use of the promotion arm, and "twice in a row" classed
    variance-derived or declared-governance.
  - F9b (gradient-consistency contract, REPAIRED per RC911-13): O3.1
    dot-product identity at the adapted mesh at the SAME derived
    floor; a TR rejection is ATTRIBUTED to remeshing by re-running
    the rejected step on the frozen pre-re-mesh topology (acceptance
    there = attribution). FIRES -> adapted meshes frozen per trust
    region, or the law stays uniform-per-run.
  - F9c (IVL immobility): any law that moves the IVL is rejected a
    priori (Mach margin becomes mesh-dependent, de-rates O(h^2)) —
    cited from A36 clause (ii).
- **BINDING F2 duty:** `F2-C9-MESHLAW-CAMPAIGN` — AC2 primitive + A36
  arm + F9a/F9b protocol on the twin sites; march-side localization
  datum replaces the knot-side prior. Rides the same
  adjoint/indicator build as F2-C11 leg (b); feeds nothing into C42.
- **Status transition proposed:** NEVER -> ADJUDICATED-SPLIT.
- **Escalation: NONE.**

### 2.4 Row C11 — error estimator for J (burden inverted: incumbent defended, and lost as standalone)

**VERDICT: measurement-gated CONVERGED-ON-PROTOCOL, as repaired
(burden inversion honored at RC911-11's honesty level).**

- **Converged architecture:** DWR = TARGET PRIMARY estimator for the
  J-bar (4/4; modern census; adjoint already exact), built in
  characteristic-native form consuming the HELD Ancourt 2023 anchor
  (READ-INTEGRAL, "ACE residuals as code verification" — RC911-5) +
  Lozano-Ponsin 2025 + the space-time/unsteady DWR template line
  (Fidkowski-Luo 2011 etc. — RC911-12), with the signed-estimate vs
  absolute-indicator distinction written into the spec (RC911-14).
  Richardson-family = PERMANENT REFEREE (estimator independence —
  O-F24's argument cuts both ways and is honored). The incumbent's
  h^p-asymptotics premise (coverage bought by K alone — RC911-6
  wording; the deployed band is K x |Delta| + floor, verified :1459)
  is retired NOW as an epistemic premise: standing Richardson-banded
  verdicts of record STAND with the row-:1182 CONFIRMED flag
  attached (retirement of the premise's status, not a voiding —
  RC911-11); any pre-F2 band-bearing verdict runs the ALREADY-BUILT
  [X-O32] estimator at its own sites or declares the row's trigger
  fired.
- **Interim regime (adopted now):** observed-p Richardson/GCI via the
  [X-O32] extension (GAP-9) = the interim verdict-bearing band at
  band sites; two-level K=4 usable in-loop ONLY on quantity-sites
  carrying a measured observed-p certificate with p_obs >= 0.415
  (recorded coverage bound, judge re-derived); LSQ (Eca-Hoekstra) =
  the checkpoint rule at NON-CONCLUSIVE observed order, safety factor
  as published (per-direction variant = C10, named not decided).
- **Pinned falsifiers (as repaired, quoted):**
  - F11a (promotion gate, REPAIRED per RC911-4): leg (a) ORDERED
    FIRST; the twin arm is valid only at sites where leg (a) delivers
    a CONCLUSIVE observed p (degraded-p sites contribute only via the
    propagation-rule band; Giles-Pierce-oracle-only promotion must be
    declared ORACLE-ONLY). PROMOTE DWR iff theta settles under
    refinement AND the derived safety factor S = (min theta)^{-1} x
    (1 + variance-derived margin) yields S x eta_DWR <= the
    matched-cost GCI band on the same sites. REFUTES DWR-PRIMARY:
    theta drifting, or any oracle site with eta_DWR under-predicting
    E_true outside its own stated band -> DWR demoted to ADAPTATION
    DRIVER ONLY, bands stay GCI/LSQ — that outcome still CLOSES C11
    (converged, not re-gated).
  - F11b (referee permanence, completed per RC911-14): DWR eta
    computed EVERY solve; solves between checkpoints inherit the last
    measured population band; referee comparison at checkpoints;
    effectivity outside its population band VOIDS that solve's bar
    automatically. Richardson/GCI never retired.
  - F11c (excluded-locus honesty): the DWR bar DECLARES its
    Mach-margin excluded locus and the D-49 probe result; a DWR-bar
    claim without the probe is a live breach of the findings-row
    trigger. D-49 lands in the F2 window in BOTH F11a branches
    (two-armed trigger of record — RC911-9).
- **BINDING F2 duty:** `F2-C11-ESTIMATOR-CAMPAIGN` — leg (a) = GAP-9
  execution (feeds the C42 wave-3 audit) ORDERED BEFORE leg (b) =
  characteristic-native DWR-J bar build (Ancourt consumed;
  space-time-DWR template named) + F11a ladder + D-49 in-window;
  registration rider: literature-registry rows for
  Becker-Rannacher 2001, Venditti-Darmofal 2002, Fidkowski-Darmofal
  2011, Roache/Celik, Eca-Hoekstra 2014, Lozano-Ponsin 2025 +
  Fidkowski-Luo 2011 / Fidkowski 2017 / CMAME 2022 (WANTED per
  procurement discipline).
- **Status transition proposed:** SINGLE-AUTHOR -> ADJUDICATED-SPLIT;
  C43 marked ADJUDICATED-WITH-C11 at the same landing (RC911-1,
  §4.5).
- **Escalation: NONE.**

---

## 3. CROSS-CLUSTER CONSISTENCY

**Multiplier semantics (C28 price vs C27 exchange/SIP multipliers vs
the (ii) marginal-value theory).** CONSISTENT, with one shared rule
made explicit. C28's mu_c is the scalar marginal price of
certifiability attached to ONE aggregated KS-max row; C27's per-lane
band multipliers are the ATOMS of the measure-valued SIP dual
(Shapiro semantics), with the KS softmax weights as the smooth price
distribution where the aggregate is genuine. Both instantiate the
same (ii) reading (dJ/dc = -Int lambda d(binding measure)); they
compose without collision because C28 decides THAT the frontier is
priced (representation) and C27 decides HOW a margin family
aggregates (operator) — the declared dependency direction C27 -> C28
(the cert surrogate "inherits the defect if underived", gapmap
:748-749) is carried in both panels and both duties (the C28 KS-max
inherits the two-constant rule; its realized exclusion band <= 2
ln(N)/rho is reported per RC28-4). The shared rule this verdict makes
binding: EVERY reported multiplier at a margin/cert-active base —
mu_c (C28), band atoms and KS-distributed prices (C27 F-C27-5) —
carries the B-STATIONARITY QUALIFIER until O1 (Danskin/Clarke) is
discharged (M0:2256-2259); and boundary-ambiguity reporting (pin F-4)
applies wherever a surrogate-active margin sits inside its own band.
K_RICH appears in both clusters' derived constants (C28 rho; C27
rho/w/red-line) — all flagged to the C42 wave-3 audit with RC27-8(iv)'s
role-count delta, none adjudicated here.

**Estimator/mesh duties (C9/C11 protocols compose, no duplication).**
COMPOSED, with the ordering made binding: (1) C11 leg (a) (GAP-9
observed-p at band sites) runs FIRST — it manufactures the CONCLUSIVE
observed-p certificates that BOTH F11a's twin arm (RC911-4 repair)
and F9a's reference bands lean on ([X-O32]-verified ladder with its
own band; the F9a threshold derivation publishes those measured
widths); (2) the characteristic-native adjoint indicator/DWR build is
ONE shared artifact — leg (b) of F2-C11 builds it, F2-C9 consumes it
as the placement driver (both panels declare the ride; no duplicate
build); (3) D-49 lands ONCE, in the F2 window (two-armed trigger),
serving C11's bar honesty and C9's A36-arm excluded-locus discipline.
Failure paths compose without deadlock: if F11a demotes DWR to
adaptation-driver-only, F2-C9 still runs (the driver needs no
certificate role) and C11 closes GCI/LSQ-primary; if F9a closes C9 on
uniform+A36, leg (b)'s DWR bar remains decidable on its own sites.
The estimator's K=4 reuse condition (p_obs >= 0.415 per site) and
C42's K_RICH audit receive leg (a)'s data — named, not decided.

---

## 4. PROPOSED LEDGER DELTAS (proposals only — applied at the landing window)

### 4.1 C28 (docs/choice_ledger.yaml:419-427)
- status: NEVER -> "ADJUDICATED-SPLIT (representation converged
  2026-08-19 wave-1; adoption-of-record gated on F2 measured half)"
- note appends: "Wave-1 verdict (BASE/blocco3/VERDICT_wave1.md):
  hybrid priced-frontier representation = M0 tier-ladder
  KKT-with-margin-multiplier of record + GAP-1 KS-max on traced
  per-cell certification ratios (derived rho, stratum-local,
  margin_factory slot; realized exclusion band <= 2 ln(N)/rho
  reported by the duty); P4/P3(ii) gates kept absolute; incumbent
  binary-only SUPERSEDED as sole representation; solvability regions
  re-scoped to physical margins (wave-2). The 'no successor' gloss is
  retired: pipeline-sense R1's full sentence names 'GAP-1's in-KKT
  certification surrogate' among the NAMED EXITS
  (ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md:191-199) — the
  prior note's 'adjudicates no alternative representation' was
  imprecise against its own source. Duty: [P-CERTKS]+[P-BSTAT]
  (GAP-1/GAP-2 window), [P-IPADJ] same critical path; pins F-1..F-4 +
  reporting pins as repaired (RC28-1/-2/-4/-11). Probe B evidence =
  scratchpad-run toy reproduced by both S24 verifiers, numbers in the
  committed advisory (NOT a committed carrier)."
- owner: unchanged (F2), duty names added.

### 4.2 C27 (docs/choice_ledger.yaml:407-417)
- status: SINGLE-AUTHOR -> "ADJUDICATED-SPLIT (structure/protocol
  converged 2026-08-19 wave-1; conditioning axis = measured F2 duty
  open)"
- note appends: "Wave-1 verdict: converged half = {two-constant rule
  (derivation repair + ex-ante trigger, arithmetic on derived
  constants; preprint theorem predicts conflict at depth); vector
  near-binding band block via margin_factory as the DERIVED
  escalation route (panel-designed; tree advocacy 2/4 + diff
  divergence 3/4); inst-XI covering + mandatory post-hoc sweep
  certificate semantics; per-lane multiplier atoms = (ii) carriers
  under the B-stationarity qualifier}. Incumbent retained as fence +
  G1 surrogate + sole operator where the two-constant check passes;
  theorems and adopt-or-declare untouched. Alternatives closed by
  stated reason incl. grouped/regional aggregation (m) (per-group
  fencing = optional refinement). Duty: F2-DUTY-C27-AGGCOND (subsumes
  gapmap [R3]; window = findings row
  margin-governor:G1-three-jump-channels), protocol as repaired
  (RC27-2 arity/cadence/w pins; RC27-3 completed falsifier partition
  F-C27-1..5 + alpha/beta/gamma)."
- cross-ref line: "C27 -> C28 dependency of record: the C28 KS-max
  inherits the two-constant rule."

### 4.3 C9 (docs/choice_ledger.yaml:217-226)
- status: NEVER -> "ADJUDICATED-SPLIT (direction converged 2026-08-19
  wave-1; adapted-law adoption gated on F9a/F9b)"
- note appends: "Wave-1 verdict: goal-oriented characteristic-native
  adapted placement = TARGET production law, presumptive pending F9a;
  uniform-per-run retained as interim certificate law (no verdict of
  record moves); A36 static arm adopted now (refinement-only, IVL
  immobile); AC2 column-insertion = the adaptation primitive, driven
  by the [X-AKNO] mechanism transferred (hypothesis under test;
  41.8% = knot-side prior). Duty: F2-C9-MESHLAW-CAMPAIGN; falsifiers
  F9a (matched TOTAL unit-process count, both counts reported;
  promotion threshold derivation published before first use), F9b
  (frozen-topology re-run attribution test), F9c (IVL immobility)."

### 4.4 C11 (docs/choice_ledger.yaml:238-248)
- status: SINGLE-AUTHOR -> "ADJUDICATED-SPLIT (architecture converged
  2026-08-19 wave-1; DWR promotion gated on F11a)"
- note appends: "Wave-1 verdict: DWR = target primary
  (characteristic-native; consumes HELD ancourt_peter_atinault_2023 +
  Lozano-Ponsin 2025 + space-time-DWR template line);
  Richardson/GCI = permanent referee; h^p-asymptotics premise
  (coverage by K alone) retired as epistemic premise — standing
  banded verdicts STAND with findings row
  mesh-amr:observed-order-not-at-band-sites flag attached; interim
  bands = observed-p GCI via [X-O32]/GAP-9; K=4 in-loop only with
  measured p_obs >= 0.415 per site; LSQ = degraded-p checkpoint rule
  (per-direction variant = C10). Duty: F2-C11-ESTIMATOR-CAMPAIGN,
  leg (a) ORDERED before leg (b) twin arm (RC911-4); D-49 lands in
  the F2 window in BOTH F11a branches; F11b per-solve semantics
  completed; DWR-failure path closes C11 GCI/LSQ-primary (converged,
  not re-gated). Registration rider: DWR/GCI canon + space-time-DWR
  WANTED rows."

### 4.5 C43 (docs/choice_ledger.yaml:581-589) — consequence of RC911-1
- status: NEVER -> "ADJUDICATED-WITH-C11 (2026-08-19 wave-1)"
- note appends: "Content identity: C43's listed alternative
  ('per-site observed-order check (o32 estimator reuse) +
  NON-CONCLUSIVE propagation') IS the C11 interim regime adopted by
  the wave-1 verdict; measured half = F2-C11-ESTIMATOR-CAMPAIGN
  leg (a) (GAP-9, both rows' annex pointer). Owner alignment S25 ->
  F2 rides the same edit. Not a fresh adjudication — a bookkeeping
  alignment declared per VERDICT_wave1 RC911-1; landing window
  confirms."

### 4.6 C42 (docs/choice_ledger.yaml:571-579) — notification only
- note appends: "Wave-1 delta to the role census (RC27-8(iv)): C27's
  repaired protocol adds K_RICH roles (band width w; chatter
  red-line multiplier); C11 leg (a) produces the observed-p data this
  audit consumes. No role adjudicated in wave 1."

### 4.7 Literature-registry rider (rides the landing, not a choice row)
Proposed rows (all grep-proven absent today by panels + reproduced by
refuters): Poon-Martins 2007, Kennedy-Hicken 2015,
Lambe-Kennedy-Martins 2017, Shapiro 2009, Lopez-Still 2007,
Samakhoana-Grimmer 2025 (preprint tier), the three grouped-aggregation
items (RC27-1), Becker-Rannacher 2001, Venditti-Darmofal 2002,
Fidkowski-Darmofal 2011, Roache/Celik, Eca-Hoekstra 2014,
Lozano-Ponsin 2025, Fidkowski-Luo 2011 / Fidkowski 2017 / CMAME 2022
(WANTED tier per procurement discipline). The KS/MPCC/nonsmooth
lineage rows for C28 accompany F2 adoption (panel's own deferral,
kept). Ancourt 2023 needs NO new row (already :199-208) — it is named
as CONSUMED input in the C11 duty.

**ledger_deltas_proposed: 6** (C28, C27, C9, C11, C43, C42-note) +
one literature rider.

---

## 5. FALSIFIERS FOR THIS VERDICT (what evidence would overturn each per-row verdict)

- **C28:** (i) a source (within the panel's 7 queries' scope or a
  named 8th) showing a production design loop that prices a marched
  solver's per-cell certification ratio in-KKT AND reports failure —
  would break the census-bounded absence and re-open the
  representation choice against a real precedent; (ii) demonstration
  that the traced r_i field is NOT differentiable per RK-G stratum on
  the committed stack (breaks the smooth-NLP-within-stratum premise;
  the Scholtes fallback lineage then stops being optional); (iii)
  repaired pin F-2 firing on the frontier-class walk (refutes the
  ADOPTION of record, per the pin's own scope — not the M0
  formalization); (iv) verbatim source check showing any §0.1 anchor
  mis-verified by this judge.
- **C27:** (i) a proof or measured counterexample that a smooth
  aggregate holds the gap pin at deep floors WITHOUT the curvature
  blow-up (would falsify the qualitative wall this verdict kept after
  RC27-4's weakening — e.g. the preprint's lower bound failing under
  the incumbent's normalization); (ii) F-C27-2 firing (arm A in band
  at ALL rungs, no conflict) — by design this RE-LABELS the row
  CONVERGED-measured on the incumbent with the two-constant
  declaration, shelving the band as escalation-only (the verdict text
  already carries this branch — firing it does not overturn the
  verdict, it selects its named branch); (iii) the (gamma) branch
  firing (A fails with no two-constant conflict) — falsifies the
  trigger's sufficiency and re-opens §4.1(2)'s trigger role; (iv) a
  cava or registry row surfacing that already adjudicated the
  conditioning axis (would falsify the absence claims this verdict
  reproduced by grep).
- **C9:** (i) F9a's refutation arm (E_A >= E_U at matched total
  unit-process count on the twin sites) — closes C9 on uniform+A36,
  overturning the target-law direction by its own pinned protocol;
  (ii) F9b firing without a frozen-topology cure — restores
  uniform-per-run as the standing answer; (iii) evidence that the AC2
  primitive cannot be made RK-G P2-compatible as specced (breaks the
  adopted mechanism's buildability premise).
- **C11:** (i) F11a's refutation arm (theta drifting or oracle-site
  under-prediction outside stated band) — demotes DWR to
  driver-only; the verdict's OWN named branch (C11 then closes
  GCI/LSQ-primary — a selected branch, not an overturn); what WOULD
  overturn the architecture is (ii) the referee itself failing on the
  Giles-Pierce analytic oracle ([X-O32]-extended observed-p bands not
  covering the analytic E_true at derived factors — would break the
  interim regime's honesty), or (iii) a census/source showing the
  characteristic-native residual object is ill-posed for this march
  (e.g. the Ancourt/Lozano-Ponsin compatibility structure failing on
  fitted-front topologies), or (iv) discovery of an existing
  registry/verdict row already adjudicating estimator choice at band
  sites (would falsify the SINGLE-AUTHOR premise this wave consumed).

Wave-level: any demonstration that a refuter finding adjudicated
SUSTAINED above rests on a mis-verified witness (all witnesses are
re-measured in §0.1's window) overturns that adjudication and any
carried repair that leans on it.

---

## 6. MACHINE SUMMARY

```json
{
  "rows": {
    "C28": {
      "verdict": "CONVERGED-ON-PROTOCOL (formal half CONVERGED-panel: hybrid priced-frontier = M0 tier-ladder KKT-with-margin-multiplier + GAP-1 KS-max on traced per-cell ratios, gates kept absolute, incumbent superseded as sole representation; adoption-of-record = ADOPTED-FOR-MEASUREMENT behind F2 duty [P-CERTKS]+[P-BSTAT]+[P-IPADJ]; pins F-1..F-4 as repaired: F-3 matched-engine-path, Probe B relabeled scratchpad-run, conservatism band 2ln(N)/rho, boundary-ambiguity reporting added)",
      "gated": true,
      "escalation": null
    },
    "C27": {
      "verdict": "CONVERGED-ON-PROTOCOL (converged half per RC27-6 wording: two-constant rule as derivation repair + ex-ante trigger; vector near-binding band block as DERIVED escalation route, panel-designed, production adoption conditional on measurement; inst-XI covering + mandatory post-hoc sweep; per-lane multiplier atoms under B-stationarity qualifier; incumbent retained as fence/G1/sole-operator-where-check-passes; option (m) grouped aggregation added and closed; duty F2-DUTY-C27-AGGCOND with repaired arm-B pins and completed falsifier partition F-C27-1..5 + alpha/beta/gamma)",
      "gated": true,
      "escalation": null
    },
    "C9": {
      "verdict": "CONVERGED-ON-PROTOCOL (target law = goal-oriented characteristic-native adapted placement, PRESUMPTIVE pending F9a; uniform-per-run retained as interim certificate law, no verdict of record moves; A36 static arm + AC2 primitive adopted now; F9a repaired to matched TOTAL unit-process count with promotion-threshold derivation published before first use; F9b frozen-topology attribution test; F9c IVL immobility; duty F2-C9-MESHLAW-CAMPAIGN)",
      "gated": true,
      "escalation": null
    },
    "C11": {
      "verdict": "CONVERGED-ON-PROTOCOL, burden inversion honored (DWR = target primary, characteristic-native, consuming held Ancourt 2023 + Lozano-Ponsin 2025 + space-time-DWR template; Richardson/GCI permanent referee; h^p premise retired as epistemic premise with standing verdicts STANDING flagged; interim = observed-p GCI via [X-O32]/GAP-9 with K=4 reuse only at measured p_obs>=0.415; leg (a) ORDERED before leg (b) twin arm; D-49 lands in F2 window in BOTH F11a branches; DWR-failure path closes C11 GCI/LSQ-primary; C43 marked ADJUDICATED-WITH-C11 at landing; duty F2-C11-ESTIMATOR-CAMPAIGN)",
      "gated": true,
      "escalation": null
    }
  },
  "sustained": {"breaks": 0, "repairs": 11, "amendments": 18},
  "escalations": [],
  "amendments_carried": ["RC28-1", "RC28-2", "RC28-3", "RC28-4", "RC28-5", "RC28-6", "RC28-7", "RC28-8", "RC28-11", "RC27-1", "RC27-2", "RC27-3", "RC27-4", "RC27-5", "RC27-6", "RC27-7", "RC911-1", "RC911-2", "RC911-3", "RC911-4", "RC911-5", "RC911-6", "RC911-7", "RC911-8", "RC911-9", "RC911-10", "RC911-11", "RC911-12", "RC911-13"],
  "ledger_deltas_proposed": 6,
  "file": "validation/sfoundations_raws_2026-08-13/blocco3/VERDICT_wave1.md"
}
```
