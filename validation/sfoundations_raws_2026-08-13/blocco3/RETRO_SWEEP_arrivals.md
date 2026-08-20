# RETRO-SWEEP — arrivals vs landed-verdict premises (+ PAIR-8/9 scope extension)
# S-FOUNDATIONS-C3, 2026-08-20. Agent: RETRO-SWEEP (single agent per brief).
# Mandate: BASE/blocco3/BRIEF_retro_sweep_arrivals.md + coordinator scope
# extension of the same window (PAIR-8 proof-layer bearing sweep on the 18
# manifest arrivals; PAIR-9 known-wrong-cite chain sweep, report-only).
# NON-RELITIGATION honored: no verdict change proposed anywhere below; every
# row maps evidence to a named premise/falsifier and stops there.
# Read-depth markers: [FULL] = section/doc read in full; [PARTIAL-<pages/secs>]
# = only the named parts read; [VISUAL-p.N] = rendered page read visually
# (uno_paper.pdf has no text layer — declared); [TITLE-manifest] = identity
# from MANIFEST_papers_foundations_c.md page-1 verification only.
# Machine keyword sweeps (pymupdf, whole-document) are declared per use; a
# keyword-absence claim is a measured whole-doc text-layer scan, not a read.
# Only file written: this one. No installs; GENO/ untouched; no git commands.

## PAIR 1 — uno_paper.pdf (+ vanaret_leyffer arXiv searchable copy) + byrd_hribar_nocedal_1999 vs VERDICT_wave2.md C31

Premise/falsifier anchors: VERDICT_wave2.md:493-511 (§2.1 adopted + pinned
falsifiers), :187-197 (§1.1 F-C31-1/2/3 definitions of record), :224-238
(RC31T-3 warm-start census line), :926-938 (§4.1 ledger delta), :1154-1162
(§5 C31 overturn conditions).

| # | Paper evidence (depth) | Premise / falsifier (anchor) | Verdict |
|---|---|---|---|
| 1.1 | BHN 1999, SIOPT 9(4):877-900 identity p.877; Algorithm I p.879: "Choose an initial value for the barrier parameter µ>0 … Choose the starting point x and s>0"; barrier update = "reducing both ε_µ and µ by a constant factor θ∈(0,1)" (p.879). Whole-doc scan: the string "warm" occurs on 0 of 24 pages (measured, pymupdf). [PARTIAL-pp.877,879,884] | scipy trust-constr cold-restart premise, "BHN is the algorithm source" (VERDICT_wave2.md:493-498; overturn condition (ii) at :1156-1158 = a source showing tr_interior_point DOES expose a usable warm-start interface) | **CONSISTENT** — the algorithm source itself defines no warm-start mechanism (fresh µ, ε_µ, (x,s) per solve; "warm" absent doc-wide); nothing in the paper touches overturn condition (ii), which concerns the scipy implementation and stays untriggered. |
| 1.2 | Uno published version of record §5.2, p.14 [VISUAL-p.14]: "The following presets are available in Uno 2.2.0: – filtersqp … – ipopt …" (no third preset); identical list in the arXiv searchable copy p.15 [PARTIAL-p.15] and in JOSS 11(123):10229 p.2 [PARTIAL-pp.2-3]: "Two presets are currently available: an ipopt preset … and a filtersqp preset …". "funnel method" appears only as a globalization STRATEGY in the wheel of strategies (preprint p.6; JOSS p.3), runtime-selectable via options, not a preset. | Arm-B preset semantics as pinned: "Flip candidate of record = **Uno** (filterSQP/funnel preset…)" (VERDICT_wave2.md:502-503; repeated in the §6 machine summary :1233 and consumed by §4.1 :926-938) | **TENSION (naming-level)** — the published paper of record contradicts the pinned arm-B configuration name: a "funnel preset" does not exist in Uno 2.2.0; presets = `filtersqp`/`ipopt` only, funnel = a separate globalization option. NO pinned falsifier fires (F-C31-1/2/3 all untouched — they gate on [P-IPADJ] outcomes, A/B outcomes, and the resolution guard respectively). The row's own protocol governs: the arm-B configuration is specified inside the F2-C31-ENGINE-AB duty; mapping only. Proposed landing-window one-line delta (rider): "arm B = Uno `filtersqp` preset (published §5.2: presets = filtersqp/ipopt only); any funnel-globalization configuration is a DECLARED third configuration selected via options, not a preset." |
| 1.3 | Uno preprint §4.2 pp.9-10 [PARTIAL]: ℓ1 relaxation and feasibility restoration are INTERNAL subproblem mechanisms (restoration "temporarily discard[s]" the objective, resumes the optimality phase; ℓ1 reformulation is exact for small ρ); the posed NLP (objective + constraint set) is unchanged. Uno accepts general NLPs (equalities/inequalities/bounds). | A/B matched-constraint-set feasibility for arm B (VERDICT_wave2.md:509-511: "A/B protocol = matched constraint set per RC28-1 discipline, W1-W4 metrics, identical-certified-outcomes guard") | **CONSISTENT** — arm B can be posed on the identical constraint set; Uno's relaxation/restoration machinery never edits the posed set, so matched-constraint-set A/B is implementable as pinned. |
| 1.4 | Uno preprint §7 p.21 [PARTIAL-p.21]: performance-profile benchmark discipline vs filterSQP/IPOPT on 429 CUTE problems, logs published. BHN pp.883-884 [PARTIAL]: multipliers = least-squares estimates subordinate to primal variables, Eq. (3.15); "This approach could just barely be considered a primal-dual method"; optimality measure = E(x,s;µ), Eq. (2.3) p.879. | Engine falsifiers F-C31-1/2/3 as defined (VERDICT_wave2.md:187-197) and the [P-IPADJ] item list (:496-500: barrier update law, what `optimality` measures, status semantics, multiplier semantics, warm-start capability) | **CONSISTENT + ENRICHMENT** — no falsifier arm is touched; F-C31-2's decidability premise is supported (published A/B benchmark discipline exists for exactly this engine). ENRICHMENT delta for [P-IPADJ]: "BHN source anchors now on disk: barrier update law = (µ, ε_µ) reduced by constant factor θ (p.879); `optimality` source semantics = E(x,s;µ) Eq. (2.3); multiplier semantics = subordinate least-squares estimates Eq. (3.15) ('just barely … primal-dual', p.884) — consume at equation level, not from memory." |
| 1.5 | Whole-doc scans: "warm" absent in BHN (24 pp) and in the Uno preprint (38 pp) (measured, pymupdf). | IP warm-start census line as repaired (VERDICT_wave2.md:232-238: "primal-only warm-starts fail; dual-shifted/central-path-proximal repairs are an active 2023-2026 line; the incumbent IMPLEMENTATION exposes no warm-start interface — the cold restart is of record regardless") | **CONSISTENT** — neither arrival adds or contradicts a warm-start capability; the census line's 2023-2026 repair-line claim is untouched by these papers. |

## PAIR 2 — hicken_zingg_2014 vs the F11d pin (VERDICT_C9C11_supplement.md §4.2 + choice_ledger C56 row)

Premise anchors: VERDICT_C9C11_supplement.md:175-202 (§4.2 final C11 note
delta, F11d two legs); docs/choice_ledger.yaml:733-742 (C56 row; :738
alternative arm "dual-consistent synthesis (discrete weight +
continuous-structure referee, Hicken-Zingg criteria)");
docs/literature_registry.yaml:876-880 (row, status UNREAD pre-sweep).

| # | Paper evidence (depth) | Premise (anchor) | Verdict |
|---|---|---|---|
| 2.1 | H-Z 2014, JCP 256:161-182. Actual criterion = **Definition 1, p.164**: L*_h and J_h are dual consistent of order q≥1 iff L*_h v + g = O(h^q) with v = the CONTINUOUS dual solution projected onto the discrete space; "dual consistency does not follow from consistency of the primal PDE discretization, in general" (p.164); consequences: smooth/interpolable adjoints (p.162, p.164 Fig. 1 discussion) + functional superconvergence for diagonal-norm SBP (§3, p.165ff; superconvergence results §3/§5). [PARTIAL-pp.161-165,174] | F11d as pinned: leg 1 = order-of-convergence bookkeeping of the AD weight against the analytic continuous adjoint on the Giles-Pierce oracle at pre-registered order/norms; leg 2 = ACE/L-P Eqs. (30)/(31) compatibility residuals at band sites; "dual consistency of the march = P2 Lemma B §4.5 SCHEMA — F11d is its execution at estimator sites" (supplement :190-202); C56 arm names "Hicken-Zingg criteria" (choice_ledger.yaml:738) | **CONSISTENT** — the pin is faithful at class level: H-Z's criterion is a residual-consistency-order statement against the projected continuous dual, and F11d's two legs (solution-convergence-order bookkeeping + computable compatibility residuals) are a faithful operationalization on a stack where the analytic dual is available only at the oracle; the class transfer (SBP finite-difference → characteristic march) is already declared SCHEMA in the pin itself, not silently assumed. No criterion in the paper contradicts the pinned form. |
| 2.2 | Same sections as 2.1. | Same premise, enrichment side. | **ENRICHMENT** — one-line delta for the landing (C56/F11d note): "published criterion set anchored: H-Z Definition 1 (JCP 256, p.164: L*_h v + g = O(h^q), v = projected continuous dual) + the p.164 caveat that primal consistency does NOT imply dual consistency — F11d's leg-1 order bookkeeping cites the definition by page, and the caveat is the published reason the F11d check cannot be waived on primal-order evidence." |

## PAIR 3 — becker_rannacker.pdf vs VERDICT_wave1.md C11 (§2.4 DWR-target architecture premises)

Premise anchors: VERDICT_wave1.md:653-712 (§2.4: DWR = TARGET PRIMARY,
Richardson referee permanence, signed-estimate vs absolute-indicator
distinction, F11a/b/c); supplement :185-190 ("same-level pairing is
signal-free … enrichment is mandatory; the enrichment operator must not
smooth across characteristic-borne adjoint discontinuities").

| # | Paper evidence (depth) | Premise (anchor) | Verdict |
|---|---|---|---|
| 3.1 | B-R 2001 (Acta Numerica pp.1-102): weighted a posteriori estimate |J(u)-J(u_h)| ≈ ⟨ρ(u_h), ω(z)⟩ with z from the adjoint problem A*z = j (Eq. (1.3), p.3); adaptive feedback controlling linearization + discretization (§6, p.46). [PARTIAL-pp.3,40-41,46] | DWR-target architecture of record (VERDICT_wave1.md:653-669): DWR primary for the J-bar, adjoint weight, signed error representation | **CONSISTENT** — the arrival is the canonical source of exactly the architecture the verdict targets; nothing in the read sections bears against any §2.4 premise (Richardson-referee permanence and the F11a promotion ladder are program-side additions the paper does not address). |
| 3.2 | p.41, §5.1(i)-(iii) weight-approximation menu with measured effectivities (Table 5.1, p.40): (i) global higher-order / finer-mesh dual solve → asymptotically sharp (I_eff→1); (ii) patch-wise higher-order interpolation i+_h z_h → I_eff≈1.2-3; (iii) difference-quotient weights → I_eff≈2-10; and the sentence "we cannot simplify this approach by using ẑ_h = z_h since then the whole error estimator would vanish" (p.41). | The landed enrichment-mandatory premise: "the same-level pairing is signal-free at the certified Newton floor … so enrichment is mandatory" (supplement :185-190) | **ENRICHMENT (expected class)** — one-line delta for the landing (C11 note, F2-C11 leg (b)): "B-R §5.1 pp.40-41 = the published enrichment-operator menu with measured effectivities (global higher-order dual solve / patch-wise higher-order interpolation / difference-quotient weights), and B-R p.41's vanishing-estimator sentence is the published same-level-signal-free anchor (Galerkin-orthogonality mechanism there, certified-Newton-floor mechanism here — analog DECLARED, not identified); admissibility of each menu item is still governed by the pinned no-smoothing-across-characteristic-discontinuities constraint." |

## PAIR 4 — thakur_nadarajah_2025 + huang_zahr_2022 + huang_zahr_2023 companion vs VERDICT_wave1 C9 (F9a-R arm + supplement folding) and VERDICT_wave2 C49 entry gate

Premise anchors: VERDICT_wave1.md:619-644 (F9a/F9b/F9c as repaired);
VERDICT_C9C11_supplement.md:144-173 (§4.1 folding: F9a-R fixed-count
wall-station seed redistribution, three-arm composition, MMPDE map-motion
does-not-transfer clause); VERDICT_wave2.md:691-693 + :1030-1041 (C49
implicit tracking = named upgrade path with STANDING ENTRY GATE =
"robustness at production counts + custom_vjp-compatible adjoint story");
F-C49a/b/c/d at :703-711.

| # | Paper evidence (depth) | Premise (anchor) | Verdict |
|---|---|---|---|
| 4.1 | Thakur-Nadarajah, JCP 523:113633 (journal version, NEWER than the ask's arXiv:2405.00904): goal-oriented implicit shock tracking, DWR as objective in full-space LNKS with second-order derivatives (p.2); staged initialization ladder (p=0 coarse → p=1 q=1 4 iters → q=2, tolerance 1e-10; penalty µ=0.001, ε_s0=ε_u0=1, Poisson-stiffness regularization) (p.23); conclusions p.26: "Several important issues need to be addressed in the future to make the proposed method a viable approach" — possible lack of stability when tracking part of a shock (artificial dissipation needed), robust mesh operations (collapse/split/swap) missing for quad/hex, R_u-preconditioner approximation needing formal investigation. [PARTIAL-pp.2,23,26,29] | C49 entry gate as pinned (robustness at production counts + custom_vjp-compatible adjoint story, VERDICT_wave2.md:691-693); promotion thresholds F9a/F9a-R (E_A ≤ E_U/2 discipline, VERDICT_wave1.md:626-631, supplement :161-164) | **CONSISTENT** — the journal version contains NO quantified result bearing on the pinned promotion thresholds (its accuracy results are DG-mesh-count benchmarks, not E_A/E_U twin-site ratios on matched unit-process counts), and its own conclusions RESTATE the robustness gaps the entry gate prices; the gate's premise is strengthened, not touched. F-C49a does not fire (no per-cell certification enforced on a captured production loop anywhere in the paper). |
| 4.2 | Huang-Zahr, JCP 454:110981: robustness measures = dimension/order-independent element removal via edge collapse + sensor-triggered element-wise solution re-initialization + adaptive penalty; κ re-balancing after topology/solution surgery (Eq. (71), p.18); shock-agnostic p=0 initialization replacing the predecessor's homotopy (Remark 22, p.18); Remark 21: element removal/re-initialization cause "abrupt changes to the objective function and constraints". [PARTIAL-pp.3,18-19] | Same C49 entry gate; also the C9 folding clause "MMPDE map-motion does not transfer (columns = characteristic intersections; free dofs = seeds + insertion)" (supplement :152-153) | **CONSISTENT** — HOIST's robustness is demonstrated on 2-D/3-D benchmark suites, not on this program's production counts, and its mid-solve mesh-topology surgery (Remark 21) is exactly the property the gate's custom_vjp-compatible-adjoint criterion must audit; nothing bears on the wall-station-seed F9a-R spec or the non-transfer clause (HOIST moves DG nodal coordinates, not characteristic-intersection columns). |
| 4.3 | Companion arXiv:2304.11427: many-query lead-shock framework — after one HOIST solve, elements UPSTREAM of the lead shock are removed and the boundary condition is applied directly on the shock boundary, only shock-boundary nodes optimized (pp.2,8). [PARTIAL-pp.2,8] | C49 two-tier reasons of record (fitted-front = sole certificate bearer; fronts as explicit unknowns, VERDICT_wave2.md:679-702) | **CONSISTENT** — the capturing-side SOTA's own many-query specialization converges toward front-as-explicit-boundary structure; supports (does not touch) the W1 reasoning. |
| 4.4 | Items 4.1-4.2 evidence. | Entry-gate/landing text enrichment side. | **ENRICHMENT** — two one-line deltas for the landing: (a) C49 entry-gate note gains the published audit checklist: "gate audit items per HZ JCP 454 §5.2-5.3 (edge-collapse element removal, sensor-triggered re-initialization, adaptive κ re-balancing Eq. (71), shock-agnostic p=0 init) + Thakur JCP 523 p.26 open-issues list (partial-shock stability, robust mesh ops, R_u-preconditioner approximation) — the gate's robustness criterion is now checkable against the line's own published measures"; (b) literature-registry rider: thakur row identity updated to the JCP 523:113633 journal version (supersedes the arXiv:2405.00904 ask identity). |

## PAIR 5 — venditti_darmofal_2000 vs the C11 estimator-form premise ("two-level fine-space residual, Venditti-Darmofal class")

Premise anchor: VERDICT_C9C11_supplement.md:185-190 ("Estimator form =
two-level fine-space residual (Venditti-Darmofal class) on the [X-O32]
ladder…").

| # | Paper evidence (depth) | Premise (anchor) | Verdict |
|---|---|---|---|
| 5.1 | V-D 2000, JCP 164:204-227: coarse mesh Ω_H, EMBEDDED fine mesh Ω_h, prolonged coarse solution U_h^H = I_h^H U_H, fine-space residual R_h(U_h^H) linearized and adjoint-weighted to correct f_h (Eqs. (1)-(5), pp.207-208); superconvergent corrected functionals on uniform grids (abstract, p.204); quasi-1-D Euler incl. shocked flows. [PARTIAL-pp.204,207-208] | Class attribution "two-level fine-space residual (Venditti-Darmofal class)" (supplement :185-186) | **CONSISTENT** — the attribution is faithful: the paper is exactly the embedded-two-level, prolongation-plus-fine-space-residual, adjoint-weighted correction class the pin names, in the quasi-1-D setting the F2 build may adopt (supplement §4.4 :238-240 already conditions the registry row on that discretion). |
| 5.2 | p.208: for PDEs with hyperbolic character, "isodirectional interpolation might lead to oscillatory behavior in an iterative adaptive procedure, as was initially encountered in the current implementation … Alternative reconstruction approaches may be required". | The pinned enrichment-operator constraint ("must not smooth across characteristic-borne adjoint discontinuities", supplement :188-190) | **ENRICHMENT** — one-line delta: "the class SOURCE itself flags hyperbolic prolongation pathology (V-D p.208: isodirectional interpolation oscillatory, alternative reconstruction needed) — published anchor, at the estimator-form source, for the pinned no-smoothing constraint on the enrichment operator." |

## PAIR 6 — fidkowski_darmofal_2011 vs the C9/C11 landed architecture (canon cross-check)

| # | Paper evidence (depth) | Premise (anchor) | Verdict |
|---|---|---|---|
| 6.1 | F-D 2011 (AIAA J 49(4):673-694, DOI 10.2514/1.J050073): review of adjoint-weighted-residual output-error estimation + output-based adaptation; "an adjoint-inconsistent discretization can lead to irregular or oscillatory adjoint solutions that pollute the error estimate with noise and lead to adaptation in incorrect areas" (p.676); discrete-vs-continuous adjoint comparison (Duraisamy et al. cited p.676): "the discrete adjoint is better at estimating the fine-space output, while the continuous adjoint is marginally better at estimating the analytical output when the computational space is well resolved"; open challenges incl. computable error bounds (abstract). [PARTIAL-pp.673-676] | Landed C9/C11 architecture: DWR-target + adjoint-consistency concern (F11d premise), discrete-AD weight of record + continuous line as frame/referee (C56, supplement §4.2), Richardson referee permanence (VERDICT_wave1.md:660-661,690-694) | **CONSISTENT** — the canon supports every checked leg: the adjoint-consistency pollution warning is the F11d premise in published form; the Duraisamy comparison is published support for the exact role split of record (discrete weight targets the fine-space output = our two-level estimator role; continuous line closer to the analytic object = referee/oracle role); the review's own "computable error bounds remain open" supports Richardson-referee permanence. |
| 6.2 | Same p.676 comparison. | C56 note (role split). | **ENRICHMENT** — one-line delta: "canon support anchored: F-D 2011 p.676 (Duraisamy et al. comparison — discrete adjoint superior for fine-space output, continuous marginally better for analytic output when resolved) = published independent support for the weight-of-record vs referee role assignment; cite in the C56 note." |

## PAIR 7 — masters_etal_2017 + lauer_ansell_2025 vs the landed C1 migration duty items (VERDICT_wave2 §4.5)

Premise anchors: VERDICT_wave2.md:987-1002 (§4.5: control-polygon chart of
the SAME certified spline space, duty items 0-6 + driver leg, F-C1a
re-pinned, GAP-21 carrier).

| # | Paper evidence (depth) | Premise (anchor) | Verdict |
|---|---|---|---|
| 7.1 | Masters et al. 2017 (AIAA J, DOI 10.2514/1.J054943): to converge lift AND drag to one count, B-spline needs ≈42 design variables on average (SVD 40, CST 42, RBF 44, Bézier 50, Hicks-Henne 60; per-case range 28-72, Table 2 discussion p.13); Kulfan's geometric tolerance is >1 order of magnitude too loose for aero convergence (p.13); strong linear correlation between geometric error and force-coefficient convergence (p.13). [PARTIAL-pp.1,4,13] | C1 duty items 0-6 + driver leg (VERDICT_wave2.md:993-1002) — none of which fixes a dof budget | **CONSISTENT + ENRICHMENT (expected class)** — nothing bears against any duty item (the migration changes CHART, not dof count, and the same-space bijection premise is untouched by parameterization-comparison results). ENRICHMENT one-line delta for the duty text: "published dof-budget prior: Masters 2017 (B-spline ≈42 dv average / 28-72 range for one-count aero convergence; geometric-error↔force-error linear correlation; Kulfan tolerance insufficient by >1 order) — consume as a PRIOR for the campaign's control-point-count check with declared transfer scope (2-D external-aero Euler), never as a program-side bound." |
| 7.2 | Lauer-Ansell 2025 (Prog. Aerosp. Sci. 158:101140): modern review; B-spline knot-interval locality and control-point proximity to the curve vs Bézier (p.19); degree effects (degree-5 B-spline "closer in nature to a Bézier curve", p.30); matching via boolean symmetric area difference (p.19). [PARTIAL-pp.19,30] | Same duty items; the chart-migration direction (control-polygon chart, Bernstein-exact certificates) | **CONSISTENT** — the modern layer's locality/proximity findings support the control-polygon chart direction and touch no premise; no independent delta beyond 7.1 (the review adds context, not a number the duty text should carry). |

## PAIR 8 — arrivals vs the COMMITTED PROOF LAYER (scope extension of record)

Theorem-layer statements checked against (anchors read this window):
[T-T0P] main + [T-T0P-E] (docs/rde_nozzle_MASTER.md:540-619 [PARTIAL]);
[L4=>R1] binding quotable form (MASTER:684-714 [FULL-block]); [MS]
mean-swirl/flux-nullity record (MASTER:991-1035 [PARTIAL] — H-AM block head);
D.18 cross-reference at SCHEMA (MASTER:1169-1180 [FULL-block]); [T-XWS] +
C-XBVP rows (docs/claims_registry.yaml:1643-1662 [FULL-rows]).
Materiality clause applied: optimizer/estimator/parameterization internals do
not bear on gas-dynamics theorems; the point of this pair is that the
NO-BEARING claim below is MEASURED (identity + read sections above), not
assumed.

| Paper (depth) | Verdict | Half-sentence why |
|---|---|---|
| byrd_hribar_nocedal_1999 [PARTIAL-pp.877,879,884] | NO-BEARING | NLP barrier/SQP algorithmics; states nothing about flows, PDE solution classes, or any H-hypothesis of the layer. |
| nocedal_wright_2006 [TITLE-manifest; p.iii cover text] | NO-BEARING | optimization textbook; constants source for [P-QNCARRY]/[P-HESSREJ], no gas-dynamics content. |
| yamamoto_1986 [TITLE-manifest; scan, no text layer] | NO-BEARING | Newton-Kantorovich error-bound sharpening for C20 Tier-2 certificates; touches no theorem-layer statement or falsifier. |
| giles_pierce_1997 [PARTIAL-p.1 abstract] | NO-BEARING | adjoint-equation duality/BC theory for Euler/NS — adjoint side only; the theorem layer's statements (steadification, causal separation, flux nullity, weak-strong uniqueness) are primal-side and untouched. |
| venditti_darmofal_2000 [PARTIAL-pp.204,207-208] | NO-BEARING | discrete two-level error-estimation algebra; no statement about the continuous solution classes the layer quantifies over. |
| hicken_zingg_2014 [PARTIAL-pp.161-165,174] | NO-BEARING | dual-consistency of SBP discretizations; discretization-property theory, no bearing on any primal PDE theorem hypothesis. |
| fidkowski_darmofal_2011 [PARTIAL-pp.673-676] | NO-BEARING | output-error-estimation review; numerical-error control, not PDE-class results. |
| huang_zahr_2022 [PARTIAL-pp.3,18-19] | NO-BEARING | numerical shock-tracking solver robustness; uses RH conditions as constraints but proves nothing about solution classes, uniqueness, or the excluded slip-sheet type (G9 scope untouched). |
| thakur_nadarajah_2025 [PARTIAL-pp.2,23,26,29] | NO-BEARING | goal-oriented tracking numerics (DG/LNKS); its continuous-adjoint appendix (A.4-A.10) is estimator-side, no primal-theorem bearing. |
| huang_zahr_2023 companion [PARTIAL-pp.2,8] | NO-BEARING | many-query lead-shock mesh framework; numerical, no analytic class content. |
| masters_etal_2017 [PARTIAL-pp.1,4,13] | NO-BEARING | airfoil parameterization geometry; no PDE analysis at all. |
| lauer_ansell_2025 [PARTIAL-pp.19,30] | NO-BEARING | parameterization review; same class as above. |
| breitkopf_ulbrich_2025 [PARTIAL-p.1 abstract] | NO-BEARING | closest arrival to the layer (variational calculus for entropy solutions of the 1-D GRP): it PRESUPPOSES entropy-solution well-posedness of the Cauchy GRP to differentiate the control-to-state map — it neither tests nor strengthens [T-XWS]'s BVP x-as-time uniqueness hypotheses, and its declared window is D25U front-terms adjoint theory; no named premise or falsifier touched. |
| deuflhard_2011 [TITLE-manifest; no p.1 text layer] | NO-BEARING | Newton-method affine-invariance monograph; C20 Tier-1 band source, no gas-dynamics statement. |
| uno_paper.pdf [VISUAL-pp.14,16,18] | NO-BEARING | NLP solver framework paper; optimizer internals only (materiality clause). |
| vanaret_leyffer_2026 preprint [PARTIAL-pp.6,9-10,15,21] | NO-BEARING | searchable copy of the above; same content class. |
| vanaret_montoison_2026 JOSS [PARTIAL-pp.2-3] | NO-BEARING | software paper (context only per the brief's exclusion rationale); no technical bearing on any layer statement. |
| becker_rannacker.pdf [PARTIAL-pp.3,40-41,46] | NO-BEARING | FEM a posteriori error-estimation theory; Galerkin-side, no bearing on the primal gas-dynamics statements or their hypothesis blocks. |

bearings_found = 0/18 (measured at the depths marked; the closest call,
breitkopf_ulbrich, is declared above with its reason).

## PAIR 9 — KNOWN-WRONG-CITE CHAIN SWEEP (mechanical, report-only)

Greps run this window (repo-wide, *.md/*.yaml/*.py, GENO/ and Uno/
excluded): `2009.07096`; `Hicken` lines lacking `256` cross-checked for
`250`; `C52` all sites, content-inspected. No file edited.

### (a) arXiv:2009.07096 mis-attribution (correct = Peter, Renac & Labbé)

| Site | Classification |
|---|---|
| PANEL_C9C11_SUPPLEMENT.md:441-449 | **already-correct** — the panel page carries the attribution "Peter, Renac & Labbé" WITH the RS911-3 correction-of-record note applied in place (:446-449). |
| refute_C9C11_supplement.md (:41,:97,:128,:201,:319), VERDICT_C9C11_supplement.md (:46,:70,:241), BRIEF_landing_mechanic.md:20, SESSION_STATE_checkpoint.md (:186,:286) | **already-correct** — all are defect DOCUMENTATION (the finding, its adjudication, the repair order, this sweep's own mandate); none asserts the wrong attribution as a claim. |

### (b) Hicken-Zingg "JCP 250" (correct of record = JCP 256:161-182, 2014)

| Site | Classification |
|---|---|
| refute_C9C11_supplement.md:320; SESSION_STATE_checkpoint.md:186 | **already-correct** — the wrong form survives ONLY inside the refuter finding quoting it and the checkpoint's mandate text. |
| docs/literature_registry.yaml:876-880 (wanted_hicken_zingg_2014) | **already-correct** — carries JCP 256:161-182 with the RS911-4 correction provenance in the identity string. |
| choice_ledger.yaml:738, PANEL_C1REP.md:864 ("Hicken-Zingg criteria/synthesis", no volume) | **already-correct** — no volume number stated, nothing to fix. |

### (c) stray C52 used with C56's content (adjoint-realization axis)

| Site | Classification |
|---|---|
| PANEL_C9C11_SUPPLEMENT.md:620 ("proposed id: C52 (next free…"), :660 ("candidate row C52"), :703 (machine summary: "candidate row C52 proposed for the stack-wide realization axis") | **WRONG-SURVIVING (superseded-upstream, non-load-bearing)** — the panel page still carries the C52 key with C56's content at three sites; unlike defect (a), the RS911-1 re-key was applied at the VERDICT level only (VERDICT_C9C11_supplement.md:204-218 §4.3, which explicitly supersedes supplement §4.1-4.4) and never in-place on the panel. Downstream chain is correct: choice_ledger.yaml:733-742 = C56 with the adjoint-realization content; choice_ledger.yaml:689-691 = C52 with its OWN content (mixed-signature contract status). Report-only; whether to annotate the panel in place is the landing window's call under its own repair protocol. |
| All other C52 hits (choice_ledger :52,:85,:742; findings_registry :2328,:2332; glossary :1101; PROGRESS_ARCHIVE :2506; AUDIT_agnostic_C2 :305,:400; refuter/verdict/checkpoint sites) | **already-correct** — legitimate references to the real C52 row, or defect documentation. |

wrong_cites_surviving = 1 family / 3 lines (PANEL_C9C11_SUPPLEMENT.md:620,
:660, :703 — C52-as-C56-content, superseded upstream, non-load-bearing).

## MACHINE SUMMARY

```json
{
  "pairs_checked": 9,
  "pairs_1_to_7_rows": 16,
  "tensions": [
    {
      "pair": 1,
      "premise": "arm-B preset semantics: 'Uno (filterSQP/funnel preset)' (VERDICT_wave2.md:502-503, :1233, consumed by par.4.1)",
      "paper_fact": "published version of record par.5.2 p.14 (visual; no text layer) + preprint p.15 + JOSS p.2: Uno 2.2.0 presets = filtersqp and ipopt ONLY; funnel = a globalization STRATEGY selectable via options, not a preset",
      "falsifier_fired": "NONE (F-C31-1/2/3 all untouched; naming-level tension only)",
      "owner_protocol": "F2-C31-ENGINE-AB arm-B configuration spec; landing window may carry the rider delta (mapped in PAIR 1 row 1.2) under the row's own protocol"
    }
  ],
  "enrichments": [
    "E1 [P-IPADJ]/C31: BHN equation-level anchors on disk — barrier update law (mu, eps_mu) x theta p.879; optimality = E(x,s;mu) Eq.(2.3); multipliers = subordinate least-squares Eq.(3.15) p.884",
    "E2 C31 arm-B wording rider: 'arm B = Uno filtersqp preset (published par.5.2: presets = filtersqp/ipopt only); funnel configuration = DECLARED options-selected variant, not a preset' (rides the pair-1 tension)",
    "E3 C56/F11d note: anchor H-Z Definition 1 (JCP 256 p.164) + p.164 caveat (primal consistency does not imply dual consistency) as the published criterion set for F11d leg-1 bookkeeping",
    "E4 C11 F2 leg (b): B-R par.5.1 pp.40-41 weight-approximation menu with measured effectivities + p.41 vanishing-estimator sentence as the published same-level-signal-free anchor (analog DECLARED)",
    "E5 C49 entry gate: HZ JCP454 par.5.2-5.3 robustness checklist + Thakur JCP523 p.26 open-issues list as the gate's published audit items; lit-registry thakur identity -> JCP 523:113633 journal version",
    "E6 C11 estimator-form note: V-D p.208 hyperbolic-prolongation warning = class-source anchor for the pinned no-smoothing enrichment constraint",
    "E7 C56 note: F-D 2011 p.676 Duraisamy discrete-vs-continuous comparison = published independent support for the weight-of-record vs referee role split",
    "E8 C1 duty text: Masters 2017 dof-budget prior (B-spline ~42 dv avg / 28-72 range, one-count criterion; geometric-force error correlation; Kulfan tolerance insufficient) with declared 2-D external-aero transfer scope"
  ],
  "bearings_found": 0,
  "pair8_papers_swept": 18,
  "wrong_cites_surviving": [
    {
      "defect": "C52 id used with C56 content (adjoint-realization axis)",
      "sites": ["PANEL_C9C11_SUPPLEMENT.md:620", "PANEL_C9C11_SUPPLEMENT.md:660", "PANEL_C9C11_SUPPLEMENT.md:703"],
      "class": "WRONG-SURVIVING (superseded-upstream, non-load-bearing: VERDICT_C9C11_supplement par.4.3 re-key of record supersedes supplement par.4.1-4.4; ledger C56/C52 rows both correct)",
      "action": "report-only; in-place panel annotation = landing-window call"
    }
  ],
  "wrong_cites_already_correct": ["2009.07096 attribution (panel repaired in place :446-449; all other hits = defect documentation)", "Hicken-Zingg JCP 250 (survives only in refuter quote :320 + checkpoint mandate :186; registry row correct at 256:161-182)"],
  "read_status_promotions": [
    {"paper": "byrd_hribar_nocedal_1999_interior_point_nlp_siopt9.pdf", "earned": "[PARTIAL-pp.877,879,884 + whole-doc warm-absence scan]"},
    {"paper": "vanaret_leyffer_2026_uno_unified_solver_mpc_arxiv2406_13454.pdf", "earned": "[PARTIAL-pp.6,9-10,15,21]"},
    {"paper": "vanaret_montoison_2026_uno_joss10229.pdf", "earned": "[PARTIAL-pp.2-3]"},
    {"paper": "uno_paper.pdf", "earned": "[PARTIAL-visual pp.14,16,18 (rendered; no text layer, declared)]"},
    {"paper": "hicken_zingg_2014_dual_consistency_functional_accuracy_jcp256.pdf", "earned": "[PARTIAL-pp.161-165,174] (registry row 876-880 status UNREAD -> READ-PARTIAL at landing)"},
    {"paper": "becker_rannacker.pdf", "earned": "[PARTIAL-pp.3,40-41,46]"},
    {"paper": "thakur_nadarajah_2025_goal_oriented_implicit_shock_tracking_jcp523.pdf", "earned": "[PARTIAL-pp.2,23,26,29]"},
    {"paper": "huang_zahr_2022_implicit_shock_tracking_jcp454.pdf", "earned": "[PARTIAL-pp.3,18-19]"},
    {"paper": "huang_zahr_2023_arxiv_2304_11427_companion.pdf", "earned": "[PARTIAL-pp.2,8]"},
    {"paper": "venditti_darmofal_2000_adjoint_error_quasi1d_jcp164.pdf", "earned": "[PARTIAL-pp.204,207-208]"},
    {"paper": "fidkowski_darmofal_2011_output_based_error_estimation_review_aiaaj.pdf", "earned": "[PARTIAL-pp.673-676]"},
    {"paper": "masters_etal_2017_airfoil_parameterization_geometric_comparison_aiaaj.pdf", "earned": "[PARTIAL-pp.1,4,13]"},
    {"paper": "lauer_ansell_2025_airfoil_parameterization_review_pas.pdf", "earned": "[PARTIAL-pp.19,30]"},
    {"paper": "giles_pierce_1997_adjoint_equations_cfd_aiaa97_1850.pdf", "earned": "[PARTIAL-p.1 abstract] (pair-8 identity check only; live consumer excluded per brief)"},
    {"paper": "breitkopf_ulbrich_2025_grp_optimal_control_variational_arxiv250922076.pdf", "earned": "[PARTIAL-p.1 abstract]"},
    {"paper": "nocedal_wright_2006 / yamamoto_1986 / deuflhard_2011", "earned": "[TITLE-manifest] (no promotion; p.1 text layer empty or cover-only)"}
  ],
  "verdict_changes_proposed": 0,
  "file": "validation/sfoundations_raws_2026-08-13/blocco3/RETRO_SWEEP_arrivals.md"
}
```
