# STAGE A — DIFF JUDGEMENT, SP8 "PROOF: what constitutes proof a number is right; stability across versions / recorders / environments" (S-REVIEW 2026-09-05)

Judge persona: JPP referee of the decisive number ("why not X?") + PM ("shortest credible path?"). NOT agnostic: the record was read
at the anchors of INCUMBENT_pointers.md §SP8 (M0 VI.6 :3181-3188; NTF block :3654 ff.; F2-B0 block :4250-4299; ledger C11/C17-C21/
C41-C43; TWIN §6-§7 + A-1 (§9); tests/test_claims_lint.py envfp + fail= grammar + closure; claims X-O32 :1262 / X-AKNO :1290 /
X-LOCD :1332 / X-CDKAT; findings record-path:cert-verdict-recorder-dependence, carriers:x-o32-negative-control-uncertifiable-on-
current-tree, audit-scert:staleness-import-closure-blind (DISCHARGED), audit-scert:xcdkat-record-numbers-drift, infra:scheduled-ci-
multiplatform; S-CERT verdict validation/PROGRESS_2026-08-13_Scert.md; prior diff phaseB_tree_diff.md §C11; LEVERS draft §F4).
Trees read integrally: stageA_tree_{variational,hyperbolic,optimization,propulsion}.md (SP8 sections V:474-504, H:433-470,
O:460-489, P:550-576, plus the SP0/SP9/order-of-battle passages that consume them). Memory files NOT read (LOG-4b).

## 0. Independence caveat applied (LOG-4b)
The statement's (R-vi) hands the derivers the TRIPLE "(code version, checking procedure, execution environment)" verbatim
(PROBLEM_STATEMENT §6). Every tree's "result = triple" sentence is therefore ORCHESTRATOR-SEEDED, not a convergence. What is
judged below is what each tree ADDS to (R-vi): the operational definition of the reproducibility band, the quotability margin
rule, the ownership of non-reproduction, and the proof ladder itself. Each verdict states whether the tree DERIVES (argument,
lemma, cost estimate present) or merely NAMES the choice.

## 1. Incumbent summary (record, cite-only)
Certificate stack per Verdict (M0 VI.6): KKT + transversality residuals, reduced-Hessian spectrum, dual-route agreement (B1 NLP vs
B2 collocation), oracles O1-O5, DWR bars, bound-ladder gap, O(St)/D2 physical bars, provenance + margins; NOTHING SHIPS OUTSIDE A
VERDICT. Per-cell Newton certification: exit when step <= NTF*EPS*sc(z), cap N_NEWTON=30 (C17 SINGLE-AUTHOR), NTF=100 (C18 SINGLE-
AUTHOR, NTF-1..3 derivation block SCHEMA/THEOREM*, GAP-29: NTF/2 flips cert_verdict), scalar scale sc (C19 DECIDED-on-cost),
qualification tiers (C20 MIXED), seed policy (C21 MIXED). Bands: two-level Richardson K_RICH=4 (C11 MIXED: DWR = TARGET primary,
Richardson/GCI = permanent referee, interim = observed-p GCI via [X-O32]; C41 P1-P4 composition MIXED; C42 one numeral 8 roles
MIXED; C43 presumed h^p retired to observed-p MIXED). Version binding (M0 :4250-4299, PRACTICE measured on 3 instances): a
certification verdict is a property of (tree, recorder, envfp); outcome classes reproduce, BINARY verdicts near the bound do not
(X-LOCD: base 2.023 FAILS per-column / 0.308 PASSES per-cell; X-AKNO: same knots, different frontier; X-CDKAT: -13.9% drift,
structure unchanged); A-1: quotable iff cert_worst <= 1/K_RICH under the pinned recorder, band (1/K_RICH,1] quotable only if both
recorders agree, seeded test cert_worst 0.9 refused. Gate: closure-aware staleness (transitive local import closure), envfp
REQUIRED on stamps >= 2026-08-31, fail= grammar with an owning OPEN finding, 9 seeded rejectors. FAILING of record: X-O32 (negative
control uncertifiable, env-induced by elimination), X-LOCD (recorder flip), X-AKNO (exit 1 by construction). S-CERT: NON-
CERTIFICABILE 2 P0 (P0#2 repaired in-window; P0#3 staleness DISCHARGED at F2-B0). Cross-version protocol: draft only (LEVERS §F4).
Adjudication class of the SP8 cluster: MIXED (C11 adjudicated 2026-08-19 with a genuine DWR advocate and inverted burden; C17/C18
single-author; C19 decided on cost; the cross-version protocol itself has NO ledger row).

## 2. Table of approaches (every SP8 approach the four trees propose)

| # | approach (tree locations) | lenses | class | derives or names | record anchor | weight on Q0 | reason |
|---|---|---|---|---|---|---|---|
| A1 | per-solve validity rejectors: conservation balance in/out, entropy inequality/positivity, RH residual, attachment raw check (V C.1-C.4; H (1)-(7); O V.3; P PR.1 v1-v4) | V,H,O,P | CONFIRM-candidate (principle) + NEW (integral conservation defect as a post-march rejector) | DERIVES (V: residual-vs-truncation ratio checked by the order test; H: RH/Lax/type-integrity per fitted front; P: pseudo-time from two initial states as multiplicity rejector) | VI.6 + X-A1IM falsifier list (P4 gate, replay monitor, thermo guard); C20 Tier-0 branch monitors | medium | adds a recorder-INSENSITIVE integral check beside the ulp-scale per-cell certificate — a candidate companion invariant for C20 Tier-0 |
| A2 | operational uniqueness: two independent engines (fitted vs captured) agree within band; two initial states coincide (H 444-451; P 355-358) | H,P | CONFIRM-candidate-NAMED (dual-code) + NEW (two-seed multiplicity rejector) | H NAMES the dual-engine principle with a weak-strong uniqueness argument [KNOWLEDGE Dafermos 1979, UNVERIFIED]; P derives the two-seed test | VI.7 GENO dual-code; C49 (SP2); START_HERE "cross-code agreement != truth" directive | low | cheap rejector; does not move the decisive band |
| A3 | three-mesh observed-order GCI, p-window rejector [p_s-0.5, p_s+0.5], Fs=1.25 derived from the source, refinement ratio >= 1.3 (V E.1; H (a); O V.2; P PR.2) | V,H,O,P | CONFIRM-candidate of the C11/C43 INTERIM regime; DIVERGENT vs the K=4 two-level presumed-h^p FORM | DERIVES (all four cite the observed-order mechanism; V/P give the window; H gives the error formula) | C11 note "interim bands = observed-p GCI via [X-O32]"; C43 retired h^p premise; C42 falsifier "Fs(p_obs) > 4 forces the derived constant" | medium (cost) | 4/4 converge with the wave-1 verdict, AGAINST the incumbent numeral form; the trees' p-window is the record's 0.5 conclusiveness cap (X-O32 dp_tot 0.67 NON-CONCLUSIVE would be flagged by both) — but the record's INSTRUMENT is FAILING today (X-O32 fail=2026-09-05), so the interim regime has no live executor |
| A4 | DWR as the second, independent estimator; effectivity eta measured; safety factor s = max(1, 1/eta_min) MEASURED, never chosen; disagreement of the two estimators rejects BOTH (V E.2; H (b)) | V,H | CONFIRM-candidate (architecture) + NEW (eta-derived safety factor for the DWR role) | DERIVES (H: s from eta_min; V: agreement-within-own-bands rejector) | C11 DWR-target + Richardson-referee (VERDICT_wave1 §2.4; supplement §4.2 weight = discrete AD adjoint); C42 per-role program | medium-high (credibility of the band the referee sees) | the record has the architecture but no eta-derived Fs role; adds a leg to F2-C42-KRICH-ROLE-AUDIT. Prior de-novo round 2026-08-17 had 4/4 DWR-primary; this round 2/4 name DWR (O and P do not) — the convergence WEAKENED, consistent with DWR being a cost item, not a load-bearing one for the decisive number |
| A5 | DIFFERENCE-RESOLVING protocol: Richardson/GCI applied to Delta itself on a MATCHED grid family (correlated discretization errors cancel to first order; band on Delta measured, "typically << band on J") (H 459-463; O V.2 "b_h on J and on Delta"; P SP9 "same meshes") | H,O,P | NEW (partially NAMED in TWIN §6 "bands on delta") | DERIVES (H: correlated-error cancellation argument; O: "converges faster on matched grids — measured, not assumed") | TWIN §6 band stack (two-resolution Richardson on... unspecified object); [T-DCRX] (value, delta) field is a different delta (fixed-exit-area relaxation) | HIGH | the TWIN stop rule (band <= 0.5% abs on delta) is reached at a FRACTION of the ladder cost if the band is measured on the paired difference on matched ladders; the record never says which object the Richardson band is on — a referee will ask; this is the largest SP8 lever the trees bring |
| A6 | explicit uncertainty budget as a SUM of named terms (disc, reduction, data/weights, base, gas pin, iteration, repro), claimable iff Delta > m + B; B >= b_TS => "undecidable at this fidelity", published as such (V 494-496; H 461-463; O 479-480, SP9 499-501; P 572-575 with abs(D) > 2 x band_total) | V,H,O,P | CONFIRM-candidate | DERIVES (O: worst-case sum because independence not proven = C41 P2 default; V/H: claim rule); P's factor 2 is DECLARED-NOT-DERIVED | TWIN §6 MATERIAL/SMALL/INTERMEDIATE/NON-CONCLUSIVE; C41 P1-P4 (RSS only with proven independence) | low | confirmation; P's "2x" would be a new magic constant — rejected here as un-derived, TWIN's band_upper reading stands |
| A7 | cross-code oracle: legacy MoC on smooth/shock-free phases; tolerance = SUM of both codes' bands, the MoC's own band from two mesh sizes; disagreement investigated, never averaged (V 489-491; H 449-451; O V.5; P PR.3) | V,H,O,P | CONFIRM-candidate | DERIVES (tolerance composition; P: MoC two-mesh band) | VI.7 GENO dual-code; X-O33B (2.6e-04 agreement on the Rao constant); M0 :4136 "GENO two-resolution wall" band | low | confirmation of a built rung |
| A8 | EXPERIMENTAL ANCHOR OF THE EVALUATOR: one published nozzle-equipped RDE thrust datum reproduced within RDE-stand band + GCI; a miss = no claim (kill K3) (P PR.4, DL-4; O V.7 class C only; V: anchors the LEVEL of J, not Delta) | P (O,V weaker) | NEW | DERIVES (P DL-4: RDE stands 1-3% thrust / 2-4% Isp [KNOWLEDGE Rankin 2017, Goto 2019, Fotia 2016 — UNVERIFIED], hence experiment anchors the evaluator, never the difference) | D6 G2 :779-782 (thrust-stand anchor = materiality calibration only); G6 data-contract gate; no evaluator-validation datum requirement anywhere | medium (credibility for the JPP referee); DEFERRED to SP9 for the accuracy-class consequence | on class-A generated data the datum anchors generator+evaluator JOINTLY (confounded); as a kill criterion it needs a datum with published nozzle geometry; the DL-4 numbers, if verified, move the TWIN's "thrust-stand 0.5-1%" anchor to 2-4% for RDE stands — an SP9 question, flagged |
| A9a | result = (code hash, checker hash, env fingerprint) printed on every number (all four) | V,H,O,P | ORCHESTRATOR-SEEDED (R-vi) | NAMES | M0 :4250-4299; envfp in test_claims_lint.py | zero (seeded) | not eligible for Stage B as a convergence |
| A9b | QUOTABILITY MARGIN = the MEASURED cross-triple spread: H "every decision inequality holds with margin >= eps_rep, eps_rep := max spread of the canonical suite across the environments actually exercised, re-measured at every change"; V "B_repro measured by re-running the reference case in >= 2 environments and after every version change"; P "scatter measured by re-running the REJECTORS in a second environment (different BLAS/compiler flags)" | H,V,P | DIVERGENT-ENRICHING vs A-1 (fixed 1/K_RICH) | DERIVES (H: the rule is stated for EVERY thresholded decision, matching the CLASS-WIDENING of the findings row that A-1 does not cover; V/P: two-environment precondition) | TWIN A-1 (cert_worst <= 1/K_RICH, certification only); findings row "mechanism covers ANY thresholded record decision"; C42 (K_RICH numeral) | HIGH | A-1 uses the K_RICH numeral in a 9th role with no derivation (C42's very defect); the trees replace it by a measured spread rho_meas with K_RICH as the interim floor, and extend the margin to truncation/wall_search/margin-floor decisions — closes the gap between the finding's widened class and the amendment's narrow rule |
| A9c | intra-environment repeat band: N_rep = 7 runs with permuted thread/order settings, N from std-of-std 29% (O 481-484) | O | DIVERGENT (detail) | DERIVES the N, but measures the WRONG object on this engine | per-path determinism of record (N-CTRL bit-identical, X-CDKAT); the variance axis of record is recorder/lowering/env (cross-lowering floor 1e-8 rel; recorder flip) | low | on a deterministic one-lowering engine N_rep repeats measure zero; salvage = read "permuted settings" as the recorder x lowering x batch-shape permutation set (C48 B-shape clause) — then it coincides with A9b |
| A9d | non-reproduction OWNED: declared FAILING under the new triple, number WITHDRAWN, kept in the record, re-stamped only with a named cause; explicit prohibition of tolerance widening (O 484-486; H 467-469; P 568-571; V 499-501) | V,H,O,P | CONFIRM-candidate | DERIVES (O: "re-derivation from scratch, not a tolerance widening" — the anti-pattern named) | fail= grammar + owning OPEN finding + 9 seeded rejectors; X-O32/X-LOCD/X-AKNO fail=2026-09-05 | low-medium | confirmation of a built gate; O's prohibition of tolerance widening is not written in the record and should be (a re-stamp by band inflation would pass today's lint) |
| A9e | eps_mach-bearing rejector tolerances re-derived per environment (V 501: "a floating-point-sensitive rejector (V.1's c*eps_mach) is re-derived per environment") | V | NEW | NAMES with a reason | C18 constants (NTF, C_FLOOR, C_OPS) are env-blind; NTF-1 kappa_eff is a MEASURED instance (s25bis_gap29_sweep.json) at ONE env; C44 FD steps; O3.1 c*eps floor | medium | the F2-B0 evidence (negative-control march non-finite under the new stack) is exactly an env-dependent floor; the F2-NTF-FLOOR-POPULATION duty should carry the envfp as a key |
| A10 | canonical reproducibility SUITE tied to the DECISIVE objects (the practice/comparator design + the decisive Delta), frozen with the triple, re-run at every change (H (8 checks + Delta), order-of-battle 10; O order 10) | H,O | NEW vs the draft's design set (internal engine designs only) | DERIVES (H: the suite IS the decision set whose inequalities carry the margin) | LEVERS §F4 design set {S18 W*, 5 S20 rejected, S22 certlim base, X-CDKAT baseline}; TWIN R-TWIN-0 | medium | both sets are needed: the marginal set TESTS the margin rule (its purpose), the decisive pair is what the referee quotes; the draft lacks the second |
| A11 | CERTIFICATION THRESHOLD SCALE: iterate/certify until the iteration error is negligible AGAINST THE DISCRETIZATION BAND (V C.1: residual < 1e-2 x local truncation estimate, factor checked by the order test; O V.3: abs(dJ) < b_TS/100 F), with hard rejection of non-convergence | V,O | DIVERGENT vs the roundoff-relative per-cell certificate (NTF*EPS*sc) | DERIVES (V: the 1e-2 factor is the ratio at which iteration error stops moving the Richardson estimate, verified by the order test; O: b_TS/100 from the ten-term budget) | C18/NTF block (:3654 ff.), C19, C20 Tier-1 kappa band; findings mechanism "seed-noise-at-marginal-cell" | HIGH | the recorder flip lives at cert_worst 1.06-2.46, i.e. cells converged to ~100-250 EPS instead of 100 EPS — invisible against any discretization band; a band-relative pass threshold with a contraction guard (Theta <= 1/2, NTF-2) would make the BINARY verdict recorder-independent by construction at those designs, while non-convergent cells (8/8 GENUINE at N_NEWTON x10) still reject. This is the structural alternative to the A-1 margin patch; it must be adjudicated, not assumed |
| A12 | exact / semi-exact verification ladder: thermally-perfect quasi-1D, PM fan with variable gamma, rotating-frame uniform-flow invariance, MMS on the periodic sector (O V.1) | O | CONFIRM-candidate (O1/O2/KAT class) + NEW (rotating-frame uniform-flow KAT, wave-frame engine only) | DERIVES (each a known-answer rejector) | O1 (T3-family -> Rao-at-<Pc>), O2 (ideal plug -> peak design), X-VMON KAT vs Rao-Beck Eq.(4), Rao-1961 spike Table-1 oracle | low | the rotating-frame KAT belongs to [S-BLITE] (SP0/SP2) when built |
| A13 | seeded corrupted-data / corrupted-gradient rejectors for every audit, estimator and derivative (P PR.5; V V.1-V.3; O (i)-(iv)) | V,H,O,P | CONFIRM-candidate | DERIVES tolerances (dot-product c*N*eps; Taylor slope window) — SP3 content | O3.1 corrupted-gradient rejector; X-STSC R1-R4; A-1 seeded 0.9; lint 9 seeds | zero-low | built; SP3 judge owns the derivative-test details |
| A14 | validated / interval numerics: declared ABSENT on cost (V 492; H (d); P PR.6) | V,H,P | DIVERGENT-minor (record is richer) | NAMES | C20 Tier-2 flagged-cell Kantorovich/Krawczyk referee; X-IVXC interval certificate (S15) | low | the record keeps interval arithmetic as a flagged-cell REFEREE, not a production tool — no change; trees' blanket rejection is weaker than the record |
| A15 | traveling-wave stability / drift test as an R-iv rung (H (8); O V.6 "thrust trace constant"; P DL-1 H3) | H,O,P | CONFIRM-candidate-NAMED | NAMES (argument lives in SP1/SP5) | O5 unsteady comparison; T0 flatness monitor (VI.4bis) | DEFERRED to SP1/SP5/SP9 | not an SP8 fork |
| A16 | experiment = the only rung at the reference accuracy class; without class C the number is anchored computationally and the claim says so (O V.7; P DL-4; V external anchor (iii)) | V,O,P | CONFIRM-candidate | DERIVES (P DL-4 numbers) | D6 G2; TWIN §6 "external calibration anchor, note-class, quoted as such" | low | confirmation; the DL-4 magnitudes are [KNOWLEDGE] UNVERIFIED (see §11) |

## 3. Prose reasons with anchors

3.1 What converges and why it weighs little. The proof LADDER (A1, A3, A6, A7, A12, A13, A16) is a 4/4 convergence with the record
at the level of architecture; every one of those rungs exists (VI.6, X-A1IM, X-O33B, O1/O2, the lint seeds). None can change the
credibility or the cost of the decisive number, except through the two places where the record is currently BROKEN: the interim
band instrument [X-O32] is FAILING (negative control uncertifiable, env-induced by elimination — findings carriers:x-o32-...) and the
binary certification verdict at marginal designs is recorder-bound (X-LOCD FAILING). The trees, agnostic, could not know that; but
their SP8 sections land exactly on those two joints, and that is where the weight is.

3.2 The reproducibility joint: A9b vs A-1. The record's amendment A-1 is a NUMERAL patch: "cert_worst <= 1/K_RICH under the pinned
recorder". K_RICH is the two-level Richardson safety constant (C42: one numeral, 8 roles, per-role derivation NEVER done); A-1 gives
it a ninth role with no derivation — the very defect C42 registers. H (467-469) states the rule the record should have written:
every DECISION INEQUALITY of the suite must hold with margin >= eps_rep, eps_rep the MEASURED max spread of the suite across the
triples actually exercised, re-measured at every change. This (i) replaces the numeral by a measurement (K_RICH survives only as
the interim floor until rho_meas exists), (ii) extends the margin to the whole widened class of the findings row ("ANY thresholded
record decision — cert verdict, truncation float(z[0])>L, wall_search revision, margin-floor raise") which A-1 does not cover, and
(iii) is falsifiable on the existing X-LOCD design set at zero new cost (rho_meas on the 5+1 designs across two recorders is
already in the logs: base 2.023 vs 0.308 = factor 6.6 > K_RICH = 4, so the A-1 margin 1/K_RICH would NOT have protected the S22
base under a recorder switch — the numeral is measured-insufficient on the record's own instance). V and P add the precondition
the record lacks: a SECOND ENVIRONMENT (P: different BLAS/compiler flags) is required before a number is quotable; today's record
has one host, and infra:scheduled-ci-multiplatform sits on path: non-critical. Under the trees' rule that row's path flips to
critical for the TWIN number (a second env is a user decision of O5 class; the pass-era env is unavailable — the F2-B0 finding
already says the reproduction of X-O32's pass is "at least env-bound").

3.3 The certification joint: A11 vs the roundoff-relative certificate. The per-cell certificate of record certifies convergence to
NTF*EPS*sc = 100 EPS (C18) and reads cert_worst = extra-step / threshold. The recorder flips of record occur at cert_worst 1.06-2.46:
cells converged to 100-250 EPS. Against ANY discretization band (K_RICH-safeguarded two-level; GCI at observed p; DWR) those cells
are converged beyond need by four to eight orders. V (C.1) and O (V.3) derive the certification threshold from the BAND: iterate
until the iteration error cannot move the Richardson estimate (V's factor 1e-2 is checked by the order test, not chosen; O's
b_TS/100 from the ten-term budget). The record's NTF-2 already carries the contraction semantics (Theta <= 1/2 two-sided estimator)
that separates "not converged" from "converged to a floor". A threshold hierarchy — hard reject on non-finite / non-contracting
cells; pass when the extra step is negligible against the band; the roundoff floor only as the reporting scale — would remove the
ulp-scale decision at its source instead of fencing it with a margin. Caveat the judge owns: the certificate's PURPOSE is also the
detection of non-convergent lanes (the 8/8 GENUINE rejections at N_NEWTON x10, M0 :3432), and the F2-B0 negative-control failure
is a non-finite step, which the hierarchy still rejects. This is a genuine DIVERGENT fork with a cheap decisive test (§5) and it
touches C18/C19/C20 (single-author / on-cost / mixed) — hence FULL-PANEL on this fork only.

3.4 The difference joint: A5. The TWIN §6 quotes "two-resolution Richardson K_RICH-safeguarded" without saying on which OBJECT.
H/O/P say: on Delta, on a MATCHED ladder, because the discretization errors of the two arms are correlated (same march, same
mesh law, same thermo tables) and cancel to first order; the per-arm bands are then referees, not the quoted band. On the record's
own numbers this matters: X-O32 fine-triple dp_tot 0.67 on J is NON-CONCLUSIVE, but the TWIN needs 0.5% on delta, not a
conclusive order on J. The record's [T-DCRX] (value, delta) field is a different delta. This is a protocol line the draft lacks
and the referee will ask for first ("your band on J is larger than your delta — how do you resolve delta?").

3.5 What the trees miss that the record has. (a) The DWR weight adjudication (discrete AD adjoint, one lowering, enrichment
mandatory, no smoothing across characteristic-borne adjoint discontinuities — C11 supplement §4.2) is far beyond any tree's "DWR
with measured effectivity". (b) The tiered certificate qualification (C20 Tier-0/1/2 incl. the interval referee) is richer than the
trees' "interval declared absent". (c) The closure-aware staleness gate with an import-closure culprit named is an instrument no
tree describes. (d) The recorder-as-authority semantics and the B-shape clause (one lowering = one executable AND one batch
shape) are engine facts no agnostic tree can reach. (e) The trees' "never re-stamped silently" is the record's fail= grammar with
an owning finding — already built and seeded (9/9 rejectors).

3.6 Prior de-novo evidence (2026-08-17). phaseB_tree_diff.md §C11: 4/4 DWR-primary, Richardson referee — adjudicated at wave-1
with inverted burden (C11 MIXED). This round: 2/4 name DWR; 4/4 name three-mesh observed-p GCI. The earlier statement had no
(R-vi); reproducibility was ABSENT from the 2026-08-17 trees (grep: one incidental "reproduce"), so A9b/A11/A5 are first-time
de-novo evidence, not repeats.

## 4. DELTA-SWEEP 2026 (inline, for the DECIDED/MIXED-with-advocate rows C11/C41/C42/C43 — the only sub-cluster adjudicated with
a genuine advocate; done here, so Stage B need not re-panel it)
- C11: no flip. Deltas since 2026-08-19: (i) the interim executor [X-O32] is FAILING (fail=2026-09-05) — the interim regime has no
  live instrument until the F2.ENGINE first bench act (S4 certification-aware re-form); every band-bearing verdict before that is
  UNBACKED, which the roadmap must show (the wave-1 verdict's "run the already-built [X-O32] estimator at their own sites" is not
  executable today); (ii) NEW LEG for F2-C11-ESTIMATOR-CAMPAIGN: leg (c) = the estimator applied to Delta on the matched ladder
  (A5), reported beside the per-arm bands; (iii) A4's eta-derived DWR safety factor = a notified role for C42.
- C41: no flip; the trees' worst-case SUM = P2 default; P's "2x band_total" rejected as un-derived (would violate C41 P3's
  dominance-certificate rule).
- C42: no flip; TWO notified roles (A-1's 1/K_RICH margin — to be REPLACED by rho_meas per A9b; the DWR eta-factor per A4).
- C43: no flip; the trees' p-window [p_s +- 0.5] = the record's 0.5 conclusiveness cap (S21 re-adjudication).
- Version-binding PRACTICE (M0 :4250-4299): no flip; the requirement text below supersedes the LEVERS draft §F4.

## 5. Proposed falsifier for Stage B (the parties must agree on it before any run)
On the EXISTING X-LOCD design set (5 S20 rejected designs + S22 certified base + S18 W* + X-CDKAT baseline), under the two
recorders and >= 2 lowerings at the pinned env (no new env required for this test), compute per design: cert_worst, the binary
verdict, the outcome class, and the integral conservation defect (A1). Then:
(F-1, margin rule A9b vs A-1): rho_meas := max over designs of max/min cert_worst across triples. If rho_meas > K_RICH (the record's
own instance already shows 6.6 on the S22 base), A-1's numeral is FALSIFIED as a sufficient margin and the requirement adopts
rho_meas (K_RICH stays the floor). If rho_meas <= K_RICH on the whole set, A-1 stands and A9b is a notational generalization only.
(F-2, threshold scale A11 vs the roundoff certificate): re-certify the same set with the band-relative hierarchy (hard reject on
non-finite / Theta > 1/2; pass when extra-step <= 1e-2 x the site's two-level Richardson band, the factor verified by the order
test on J). A11 SURVIVES iff (a) every binary verdict is recorder- and lowering-independent on the whole set AND (b) every S20
GENUINE rejection (certdiag 8/8 at N_NEWTON x10) is still rejected. A11 is KILLED if any genuine rejection passes (the band-relative
threshold is too lax to detect non-convergence) — then A-1/A9b is the right fix and A11 is closed converged.
(F-3, difference band A5): on the two S24 F1b twin designs (or the first TWIN pair), the matched-ladder band on Delta must be
smaller than the per-arm band on J by a measured factor; if it is not (the errors do not correlate on the fitted class), A5 gives
nothing and the TWIN stop rule stays on the per-arm bands.
Cost: one session-fraction (the designs and both recorders exist; 892 s for the X-AKNO cycle is the scale), no new theory.

## 6. REQUIREMENT TEXT (M0-ready; supersedes LEVERS draft §F4; target class stated)
[CERT-STAB] CERTIFICATION STABILITY — class PRACTICE (measured on three instances at F2-B0); target class THEOREM* for clause (ii)
under the measured-spread hypothesis (H-rho: the cross-triple amplification of every suite metric is bounded by the measured
rho_meas on the pre-registered design set; the lemma "m <= tau/rho under one exercised triple implies m <= tau under every
exercised triple" is then immediate — the content is the measurement, the class is honest).
(i) TRIPLE + LOWERING. Every Verdict prints (tree hash, recorder id + version, envfp) AND the lowering key (executable + batch
shape, C48 B-shape clause). The recorder is an explicit argument of every certification-bearing carrier, never an env-var default.
(ii) MARGIN ON EVERY DECISION. A thresholded record decision d = [m <= tau] (per-cell certification, truncation float(z[0])>L,
wall_search revision, margin-floor raise, TWIN branch assignment) is QUOTABLE iff m <= tau/rho with rho := max(K_RICH, rho_meas),
rho_meas = the measured max cross-triple spread of m on the pre-registered design set; K_RICH is the interim floor and a notified
C42 role until rho_meas exists. The band (tau/rho, tau] is MARGINAL: quotable only if every exercised triple agrees; otherwise no
delta is quoted (tightening of R-TWIN-4).
(iii) DIFFERENCE OBJECT. The band that gates a TWIN branch is the band on Delta measured on the MATCHED ladder; the per-arm bands
on J are printed as referees. A per-arm band larger than abs(Delta) does not by itself block a branch if the matched-ladder band on
Delta places it (pre-registered; F-3 decides whether the cancellation exists).
(iv) OWNERSHIP. A decision that does not reproduce under a new triple is fail=-owned by an OPEN finding; the number is WITHDRAWN,
never re-stamped by tolerance widening (prohibited in words); re-stamp only with reproduction on the new triple or a cause-named
finding.
(v) RE-FIRE. Any triple or lowering change after an arm's run re-fires R-TWIN-0.
(vi) OUTCOME CLASS is necessary, not sufficient: a reproduced outcome class with a flipped binary verdict is a FAIL of (ii).
(vii) EPS-BEARING CONSTANTS. Every tolerance carrying eps_mach (NTF, C_FLOOR, C_OPS, C44 FD steps, O3.1 floor) is stamped with the
envfp of its derivation; a new envfp re-opens the F2-NTF-FLOOR-POPULATION measurement before any stamp on that env.
(viii) SECOND ENVIRONMENT. A decisive number is quotable only after clause (ii) has been exercised on >= 2 environments (a second
env = user decision, O5 class; until then the Verdict prints "single-env" and the TWIN branch is at most INTERMEDIATE).
(ix) COMPANION INVARIANT. Beside cert_worst, every Verdict prints the integral conservation defect (mass, axial momentum, energy
in/out) against the discretization band — a recorder-insensitive check (C20 Tier-0 candidate; measured effect on the flips = F-2).

## 7. PRE-REGISTERED CROSS-VERSION PROTOCOL (no run here; owner F2.ENGINE first act with the X-O32 / X-LOCD re-forms)
- DESIGN SET (tiers, all mandatory): T1 marginal = {5 S20 rejected designs (validation/s22_rejected_designs.json), S22 cert-
  limited base (s22_certlim_base.json)} — purpose: rho_meas and the F-1/F-2 tests; T2 certified = {S18 W* (s20_adaptive_design.json),
  X-CDKAT baseline}; T3 decisive (added at F3.TWIN opening) = {both arms' final designs, the comparator, the paired Delta} (H's
  canonical suite). Files verified present 2026-09-05.
- RECORDERS x LOWERINGS: per-column (A1_COLEXEC=1) and per-cell (A1_COLEXEC=0); sequential-eager and jitted; batch shape B=1
  (C48). ENVS: e100f996 now; the second env when it exists (viii).
- MEASURED per design x triple: cert_worst, binary verdict, outcome class, certified J, KKT residual, conservation defect (ix);
  for T3 also Delta and its matched-ladder band.
- BAND / PASS-FAIL (all-or-nothing per tier, printed with the triple set): outcome class reproduces for every design; binary
  verdict reproduces for every design with cert_worst <= 1/rho; rho_meas reported and compared with K_RICH (F-1); T3: the matched-
  ladder band on Delta <= the per-arm band (F-3), else the per-arm band gates.
- SEEDED REJECTORS (each must FIRE): a design at cert_worst 0.9 refused as quotable; a doctored envfp refused; a doctored tree
  hash refused; a Verdict WITHOUT the recorder argument refused; a Verdict whose printed recorder differs from the executed one
  refused; a re-stamp whose only change is a widened tolerance refused (iv).
- FALSIFIER OF THE REQUIREMENT ITSELF: a design with cert_worst <= 1/rho whose binary verdict flips across exercised triples —
  then rho_meas was mis-measured (design set too small) and the requirement re-opens with the set enlarged; owner F2.ENGINE.

## 8. Where the trees go beyond the draft §F4 (summary for the ASSESSMENT)
(1) margin = MEASURED cross-triple spread, K_RICH only the floor (H,V,P) — the draft keeps the un-derived numeral; (2) margin on
EVERY thresholded decision, matching the findings row's widened class (H) — the draft covers certification only; (3) the band on
Delta on a matched ladder as the gating object (H,O,P) — absent from the draft and from TWIN §6; (4) a second environment as a
precondition of quotability (V,P) — the draft is single-host and the CI finding is non-critical; (5) eps_mach-bearing tolerances
re-derived per env (V); (6) tolerance widening prohibited in words (O); (7) the decisive objects in the reproducibility suite (H,O)
— the draft set is internal-engine only; (8) the DIVERGENT threshold-scale alternative A11 (V,O) which the draft does not consider;
(9) an evaluator experimental anchor as a kill criterion (P) — deferred to SP9 with its [KNOWLEDGE] rows. What the draft has that
the trees lack: the concrete design set, the two named recorders, the seeded doctored-envfp/tree-hash rejectors — kept.

## 9. Branch ledger (every branch seen)
| branch | status | reason |
|---|---|---|
| A1 per-solve validity + conservation defect | EXPANDED | recorder-insensitive companion; enters requirement (ix) |
| A2 dual-engine uniqueness / two-seed multiplicity | EXPANDED (low) | cheap rejector; SP2 owns the fitted-vs-captured fork (C49) |
| A3 three-mesh observed-p GCI | EXPANDED | converges with the wave-1 interim regime; instrument FAILING today — flagged |
| A4 DWR second estimator + eta-derived Fs | EXPANDED | C42 notified role; C11 unchanged |
| A5 matched-ladder band on Delta | EXPANDED | requirement (iii) + protocol T3 + F-3 |
| A6 budget sum + claim rule | EXPANDED (confirm) | P's 2x rejected as un-derived |
| A7 cross-code tolerance composition | PRUNED | built (X-O33B, GENO band); nothing to adjudicate |
| A8 evaluator experimental anchor as kill | DEFERRED | trigger: SP9 judge + [KNOWLEDGE] rows verified (Rankin/Goto/Fotia); owner F3.TWIN opening |
| A9a triple | PRUNED | orchestrator-seeded via (R-vi); zero weight |
| A9b measured-spread margin on every decision | EXPANDED | requirement (ii); F-1 |
| A9c intra-env N_rep=7 repeats | PRUNED | measures zero on a deterministic one-lowering engine; salvaged into A9b as the recorder x lowering permutation set |
| A9d fail-owned, never re-stamped, no tolerance widening | EXPANDED (confirm + one added prohibition) | requirement (iv) + seeded rejector |
| A9e eps-bearing tolerances per env | EXPANDED | requirement (vii); rides F2-NTF-FLOOR-POPULATION |
| A10 decisive objects in the suite | EXPANDED | protocol T3 |
| A11 band-relative certification threshold | EXPANDED — FULL-PANEL fork | F-2 decides; touches C18/C19/C20 |
| A12 exact-solution KATs (record has O1/O2/KATs) | PRUNED | built |
| A12' rotating-frame uniform-flow KAT | DEFERRED | trigger: [S-BLITE] wave-frame engine build; owner SP0/SP2 judges |
| A13 seeded rejectors everywhere | PRUNED | built; SP3 owns derivative tolerances |
| A14 interval numerics absent | PRUNED | record richer (C20 Tier-2, X-IVXC); trees weaker |
| A15 drift test as R-iv rung | DEFERRED | trigger: SP1/SP5/SP9 verdicts; owner O5 / T0 monitor |
| A16 experiment = only reference-class rung | PRUNED (confirm) | DL-4 magnitudes enter as [KNOWLEDGE] rows |
| second-environment precondition (from A9b) | EXPANDED | requirement (viii); recommends path flip of infra:scheduled-ci-multiplatform to critical for the TWIN number (user decision) |

## 10. Adjacent-field prior check (mandatory)
- Turbomachinery rotating-frame steady practice: considered by all four trees at SP0/SP1 (V S0.6, H S4/L5, O S4 with
  [KNOWLEDGE Lakshminarayana 1996; Wang & He 2010 — UNVERIFIED, no registry row], P DL-1 with [KNOWLEDGE Paxson 2014 wave-fixed
  frame — registry has Paxson rows, 2014-0284 identity to verify]). For SP8 specifically NO tree imports the turbomachinery
  verification practice (mixing-plane vs full-annulus reduction error as a measured effectivity; sector-periodic MMS) except O's
  rotating-frame uniform-flow KAT — census row.
- Harmonic-balance / time-spectral adjoints: considered and rejected-for-a-reason by all four (V S0.7, H S5 Gibbs argument, O S6,
  P S-5) with [KNOWLEDGE Hall, Thomas & Clark 2002 — no registry row; registry has rubino_2018]. SP8 consequence: no tree proposes
  an HB/space-time DWR estimator for the O(St) term — they MEASURE it (Omega-sweep); consistent with the record's M-RED and with
  the WANTED space-time DWR rows (:937-952). Not an SP8 gap.
- Steady adjoint-based shape optimization V&V practice: GCI/ASME V&V 20 (P), MMS (O), DWR (V,H), Giles-Pierce adjoint-at-shocks
  (V,H,O,P) — all present; ASME V&V 20 has NO registry row (census).

## 11. [KNOWLEDGE] rows (identity, why needed, procurement owner) — never evidence
| identity | why needed | owner |
|---|---|---|
| Roache 1994/1997 GCI (Fs=1.25 three grids + observed p) | A3 safety-factor derivation; already WANTED row :918 | F2-C11-ESTIMATOR-CAMPAIGN leg (a) |
| Celik et al. 2008 J. Fluids Eng. policy (three-mesh observed-p procedure; refinement ratio >= 1.3) | A3 p-window + ratio; row :925 exists (snippet) | same |
| ASME V&V 20-2009 (P PR.2) | solution-verification standard the JPP referee will cite; NO row | litreview census, tier [APERTO] |
| Becker & Rannacher 2001 (DWR, effectivity) | A4 eta-derived Fs; row exists, read PARTIAL pp.3,40-41,46 | F2-C11 leg (b) |
| Venditti & Darmofal 2000/2002 | A4 estimator form; rows exist | same |
| Giles & Pierce 2001 (adjoint at shocks) | A4/A13 cross-check; row exists | none |
| Deuflhard CSM 35 (Theta monitor, termination) | A11 contraction guard (NTF-2 already cites); row exists read-partial | F2-NTF |
| Dafermos 1979 weak-strong uniqueness (H 447) | A2 uniqueness argument in smooth regions; NO row | census, [APERTO] |
| Giesselmann, Makridakis & Pryer 2015 (rigorous a-posteriori, 1D systems) | A4 "out of reach in 3D with shocks" claim; NO row | census, [APERTO] |
| Rankin et al. 2017 JPP; Goto et al. 2019 JPP; Fotia et al. 2016 JPP (RDE stand accuracy 1-3% thrust, 2-4% Isp — P DL-4) | A8/A16: the TWIN's 0.5-1% "thrust-stand class" anchor may be a STEADY-stand number; registry has mentions, row-level identity to verify | SP9 judge + litreview [REP] tier at F3.TWIN opening |
| Hall, Thomas & Clark 2002 (HB); Nadarajah & Jameson time-spectral adjoint | adjacent-field check §10; NO rows (rubino_2018 exists) | census |
| Lakshminarayana 1996; Wang & He 2010 (rotating-frame adjoint in turbomachinery) | adjacent-field check §10; NO rows | census |
| Paxson 2014 AIAA 2014-0284 (wave-fixed-frame RDE simulation) | P DL-1 precedent; identity to verify against the Paxson rows | census |

## 12. Three questions (SP8 reading of §G.3)
Q1 (is "certificate = property of the triple, quotable with margin" the right sharpening of (R-vi)?): YES as the class, NO as the
numeral — the sharpening of record fixes the margin at 1/K_RICH without derivation and restricts it to certification; the trees'
measured-spread-on-every-decision form is the right sharpening.
Q2 (does the sharpened SP8 answer Q0?): only through SP9 — SP8 fixes what a quotable Delta IS; the band on Delta (A5) and the
second-environment precondition are the two SP8 items that change whether the decisive number can be quoted at all.
Q3 (separate rungs for designer and evaluator?): YES for proof: the designer's per-cell certificate (ulp-scale) and the
evaluator's band (discretization-scale) are different rungs; the recorder flips come from conflating them (A11).

## 13. Panel recommendation
FULL-PANEL scoped to ONE fork: A11 (band-relative certification threshold with contraction guard) vs the roundoff-relative
certificate + A-1/A9b margin — because it touches C18 (single-author), C19 (decided on cost) and C20 (mixed), and because F-2 is
cheap and decisive. Everything else in SP8: CONFIRM-BY-DIFF (this file) + the inline DELTA-SWEEP of §4; A5/A9b enter the
requirement text directly (their falsifiers F-1/F-3 are measurements, not adjudications). Budget: one panel round, judge + one
refuter, brief = §3.3 + §5 F-2 only.
