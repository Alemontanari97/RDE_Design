# PANEL C50 — DATUM-SPACE METRIC (Form-2 solo)
S-FOUNDATIONS-C3 WAVE 3. Census dated 2026-08-20 (validity stamp).
Slot mandate: BRIEF_wave3_panels.md §C50; frame = wave-1 §0 + wave-2
§0-bis/§0-ter, binding verbatim. Row: docs/choice_ledger.yaml:667-677
(C50, NEVER). Mandate anchor read in full:
validation/sfoundations_raws_2026-08-13/VERDICT_contract_and_L4R1.md#D-3
(:140-145) + F-3 (:66-74). No registry/doc of record edited — all
deltas PROPOSED for the landing window.

---

## 1 FROZEN FORMAL STATEMENT

**THE single main question (pre-registered, §0-ter(b)):** what metric
must the uncertainty contract carry so that acceptance tests and
sensitivity statements are BOTH well-posed on periodic front-bearing
interface data?

**Objects.** Datum = the per-phase interface profile Û on
A = 𝕋 × [r_i, r_o] (annulus × phase), BV ∩ L∞, front-bearing (jump
set = wave-front traces, positions known only to jitter accuracy),
delivered as a calibrated tuple (nominal; metric d; certified radius
ε; validity window W) per [PDE] D7.1 (contract_blind_pde.md:589-599)
and [DATA] Def 7.1 (contract_blind_data.md:578-592). Two distinct
semantic ROLES the metric serves:

- **ACCEPTANCE**: membership of a delivered datum in the ε-ball;
  extrapolation outside W = NO DATUM (rejected, not error-barred).
- **SENSITIVITY**: certified first-order bound |J(D) − J(D₀)| in
  terms of d-distance, feeding the interval-separation obligation
  (designs distinct only when certified intervals separate; ties
  reported as ties — [PDE] C7.2 :620-634, [DATA] Claim 7.4 :638-651).

**Options** (ledger row C50 alternatives, verbatim class):
(O-a) L¹(A) [blind-PDE lens]; (O-b) thrust-calibrated flux-weighted
L² + separate L∞ realizability guard [blind-DATA lens]; (O-c) both,
split by role (the judge's named candidate, VERDICT #D-3 :143-145);
(O-d) census family the brief mandates closing: Wasserstein /
optimal-transport metrics for front-bearing data.

**Pre-registered decision criteria (frozen BEFORE search).**
ACCEPTANCE role — an option wins iff:
- (A1) the stage-A/§6 audits are d-continuous (acceptance stable to
  noise) — [PDE] C7.1(a);
- (A2) d responds PROPORTIONALLY (non-degenerately) to the dominant
  physical error mode of this data class = front-position jitter
  (O(jitter × slope) at shocks, [DATA] Claim 7.5(i); finding
  contract:phase-gauge-jitter-alignment-unpinned,
  docs/findings_registry.yaml:2316);
- (A3) d is computable from the delivered discretization +
  reconstruction operator, using no unmeasured quantity (this is
  what kills TV-class metrics);
- (A4) realizability (pointwise state-space membership) is
  enforceable — inside d or as a declared separate guard.
SENSITIVITY role — an option wins iff:
- (S1) it yields a certified first-order bound |δJ| ≤ ‖Λ‖_dual · ε
  with a COMPUTABLE dual object;
- (S2) that dual object exists in the adjoint stack of record
  including the front-motion terms (the fitted-tier load-bearing
  argument, phaseB_tree_diff.md §3.3 :330-335 — Giles-Pierce class);
- (S3) the calibration is falsifiable by a direct FD probe against
  the adjoint bound.
SPLIT-BY-ROLE (O-c) wins iff no single metric satisfies A1-A4 AND
S1-S3 without inflation, AND the two metrics' consistency seam is
pinned (declared bridge inequality or declared incomparability +
tie rule). Mid-census amendments: none were needed (declared).

**Materiality (§0-ter(c), honest both directions).** The row is
MATERIAL at the semantics level: the metric choice changes what gets
REJECTED at acceptance and what counts as a distinguishable design —
not bookkeeping, so the LOAD-CLASS VALVE does not downgrade the
adjudication itself. It IS immaterial today at the constants level
(no real datum has ever been imported; trigger of record = "F2
contract freeze / first imported real-data family", findings
registry :1668). Right-sizing: adjudicate the STRUCTURE to
convergence now; every numeric constant (ε floors, net spacings)
deferred to the F2 instantiation duty. No over-machinery.

---

## 2 SOTA CENSUS (dated 2026-08-20)

### 2.1 Query protocol table (§0-ter(a))

| # | Verbatim query string | Where | Date | Hits/Screened/Included |
|---|---|---|---|---|
| Q1 | "optimal transport Wasserstein misfit full waveform inversion discontinuous fronts review 2024" | WebSearch | 2026-08-20 | 10 links / 5 / 4 |
| Q2 | "validation metric model acceptance uncertainty quantification area metric Wasserstein CDF Oberkampf" | WebSearch | 2026-08-20 | 10 links / 4 / 2 |
| Q3 | "shift differentiability shock sensitivity conservation laws Ulbrich adjoint optimal control discontinuous solutions" | WebSearch | 2026-08-20 | 8 links / 5 / 2 |
| Q4 | "data assimilation sharp fronts position error metric feature displacement L1 norm hyperbolic" | WebSearch | 2026-08-20 | 7 links / 3 / 2 |

Local corpus consulted (measured greps, this window): choice ledger /
findings / claims / M0 / pipeline_audit / literature_map greps for
`Wasserstein|optimal transport`, `shift-differentiab|front-motion`,
`phase-gauge|jitter`, `datum-uncertainty-contract-missing` — anchors
cited inline below. Russian classical school: does not bear on this
row (the datum-metric question is a UQ/contract question with no
classical-nozzle-theory counterpart; the classical corpus enters this
program via the variational rows, not the data contract) — closed by
stated reason.

### 2.2 Corpus recency
Span 1997-2025; newest items 2024-2025 (Dong et al. JGR 2024
prescribed-direction OT-FWI; ScienceDirect 2024 W-FWI density
reconstruction; climate Wasserstein error-metrics 2025). Modern
refined lines reached: graph-space/unbalanced OT (2019-2021),
OT-FWI (2014-2024), area-validation-metric V&V practice
(2006-2019+), L¹/TV variational assimilation for fronts (2010-2013).

### 2.3 Per-source one-liners (read-depth markers mandatory)

**In-repo, of record (authority tier):**
- [FULL] contract_blind_pde.md §7 (:585-643): D7.1 calibrated-set
  contract; C7.1 metric requirements (a)/(b), TV ruled out, weaker-
  than-L¹ ruled out, declared d = ‖·‖_L¹(A) within L∞(K)-bounded +
  TV-bounded class, honest status: downstream L¹-stability is a
  theorem only in 1-D small-BV, else a sampling-verified modeling
  assertion; C7.2 first-order bound |J−J₀| ≤ ‖Λ‖_L∞(A) ε_Û +
  |∂_Ω J| ε_Ω with Λ = adjoint trace on Σ; C7.3 priors-not-bars.
  Also :187-189: L¹-continuity of translation on BV ⊂ L¹ (the
  linear-in-front-displacement property of L¹, standard).
- [FULL] contract_blind_data.md §7 (:575-651): Def 7.2 grade U-a =
  declared NORM PAIR — L∞(𝕋×[r_i,r_o]) for realizability-critical
  components AND flux-weighted L² ‖δQ‖_*² = ∫|G·δQ|² with G = Gâteaux
  derivative of thrust∘solve at Q̂ (metric CALIBRATED TO THE DESIGN
  TARGET, [PS] status declared); U-b covariance; U-c measure-valued;
  Claim 7.4 tie rule; Claim 7.5(i) phase-gauge quotient (jitter
  masquerades as amplitude uncertainty at shocks).
- [FULL] VERDICT_contract_and_L4R1.md #D-3 (:140-145), F-3 (:66-74),
  F-6 (:84-87), C7.2 anchors — the mandate + the contract gap row.
- [FULL] docs/choice_ledger.yaml C50 (:667-677), C55 (:721-731);
  docs/findings_registry.yaml contract:datum-uncertainty-contract-
  missing (:1660-1668), contract:phase-gauge-jitter-alignment-
  unpinned (:2316-…); docs/rde_nozzle_MASTER.md W1-W4 window
  (:167-175).
- [FULL] phaseB_tree_diff.md §3.3 :330-335 (adjoint front-terms
  designed-in, Giles-Pierce class — load-bearing fitted-tier
  argument), consumed via the C49 note of record (ledger :665).
- [FULL] docs/rde_nozzle_pipeline_audit.md :102 (shift-
  differentiability Bressan-Marson/Ulbrich already an adopted anchor
  of the record's shape-calculus row); docs/rde_nozzle_theorem_ledger
  .md :235 (multi-D shift-differentiability gap named);
  docs/rde_nozzle_G12_S1.md (:14, :137 — Bressan-Guerra lead,
  citation-to-verify residue R-G12.2). These home the front-parameter
  sensitivity machinery INSIDE the record already.

**External census (per-source):**
- [ABS] Engquist-Froese-Yang, "Application of Optimal Transport and
  the Quadratic Wasserstein Metric to Full-Waveform Inversion"
  (arXiv:1612.05075): W₂ misfit convex w.r.t. shifted/dilated
  signals — the OT family's differentiator = convexity of the MISFIT
  LANDSCAPE in displacement, curing cycle-skipping in inversion.
- [ABS] Métivier et al., "Optimal transport in full-waveform
  inversion: analysis and practice of the multidimensional
  Kantorovich-Rubinstein norm" (arXiv:2101.00904): KR/graph-space
  route exists PRECISELY because raw OT needs nonnegative
  equal-mass inputs — signed oscillatory data must be normalized or
  lifted, a known artifact source.
- [ABS] Dong et al., JGR Solid Earth 2024 (10.1029/2023JB027342):
  2024 state of the OT-FWI line — density-normalization of signals
  degrades the transport map; prescribed-direction repair. Confirms
  the normalization obstacle is live in the modern literature.
- [TITLE] "Application of an unbalanced optimal transport distance
  and a mixed L1/Wasserstein distance to full waveform inversion":
  unbalanced-OT workaround exists; mixed L¹/W forms exist.
- [ABS] Area Validation Metric line (Ferson-Oberkampf-Ginzburg 2008;
  Roy-Oberkampf 2011 framework, ftp.demec.ufpr.br copy; relialab
  "Toward a Better Understanding of Model Validation Metrics" 2011):
  the V&V acceptance metric of practice = area between CDFs of a
  SCALAR QoI = 1-Wasserstein on the QoI's distribution — i.e. the
  acceptance-metric literature operates in QoI SPACE, downstream of
  (not competing with) a datum-space metric.
- [ABS] Freitag-Ball-Nichols, QJRMS 2013 ("Resolution of sharp fronts
  in the presence of model error in variational data assimilation"):
  L¹/TV-penalty assimilation preserves fronts better than L²-class
  treatment — direct modern evidence that L²-type distances misjudge
  front-bearing fields while L¹-type respects them.
- [ABS] Ulbrich, "Adjoint-based derivative computations for the
  optimal control of discontinuous solutions of hyperbolic
  conservation laws" (Syst. Control Lett. 2003; + SICON 2002
  sensitivity/adjoint calculus): shift-variations = standard
  variation + weighted indicator corrections for moving shock
  positions; tracking-type functionals become differentiable in the
  SHIFT decomposition, NOT in raw Lᵖ — the theoretical basis for
  carrying front positions as a finite-dimensional block.
- [ON-DISK, not re-read this window] Giles-Pierce 1997 (literature/,
  manifest row): consumed via the diff §3.3 anchor of record, no
  claim made here above that anchor's content.

**Cava (ADVISORY_litreview_confrontation_2026-08-13.md), per-row per
(iv):** measured grep (`metric|Wasserstein|uncertain`, this window)
returns no row on datum-space metric choice or interface-data
uncertainty contracts (hits are EAP-as-metric and geometry rows —
different senses of "metric"). The cava does not bear on C50; no row
cited. Absence claim search-proven by the stated grep.

### 2.4 §0-bis named-axes bearing (one sentence each, per row C50)
1. **Optimizer query-level choice**: does not bear — C50 fixes a
   contract metric, no optimizer consumes it as an engine choice.
2. **Discrete vs continuous adjoint / consistency**: BEARS through
   S2 — the sensitivity dual object Λ (adjoint trace on Σ, plus
   front-motion terms) must be produced by the adjoint realization
   of record; that realization choice is C56 (ledger :733-…) — the
   interaction is NAMED here, not decided (C56 owns it).
3. **Moving-mesh / r-adaptive families**: does not bear — mesh
   motion lives in the downstream solve; the datum metric is defined
   on the fixed interface annulus A before any mesh exists.
4. **Adjoint-free routes**: bears only as the U-c bootstrap/sampling
   UQ grade ([DATA] Def 7.2), which is a fallback verification route
   for FS-1 below, not a competing metric — named, closed.
5. **Emergent sub-aspects**: (a) linearization-at-fronts /
   shift-differentiability — surfaced, closed INSIDE this
   adjudication (§3.3 below) with the record's existing G12/S1 home
   (no new row needed, dedup-verified); (b) Wasserstein/OT family —
   closed by stated reason in §3.4.

---

## 3 ADJUDICATION

**Incumbent.** NONE — the record is silent at the contract site
(finding contract:datum-uncertainty-contract-missing, CONFIRMED,
severity medium). There is no incumbent to defend; the burden is
symmetric between the two blind lenses. Zero-inflation note: neither
lens is "SOTA-validated" beyond what §2 shows; both are blind
single-lens proposals of record.

### 3.1 O-a — L¹(A), the blind-PDE lens at its genuine best (by citation)
Case FOR (contract_blind_pde.md:601-618): (a) audits are flux
integrals, L¹-continuous on L∞-bounded sets [PROOF-grade via
dominated convergence — the lens's own grading]; (b) TV metrics are
ruled out because jump POSITIONS are never measured to TV accuracy;
(c) metrics weaker than L¹ are ruled out by flux continuity; (d) L¹
responds LINEARLY to front displacement (translation continuity on
BV, :187-189): a front of jump size [q] displaced by δ costs
≈ |[q]|·δ — exactly the proportional response criterion (A2). L¹
therefore satisfies A1, A2, A3; A4 it satisfies by construction of
the lens's own contract: the L∞(K)-bounded, TV-bounded class is a
SIDE CONDITION of the contract, not part of the metric (:609-610).
Case AGAINST as sole metric: its sensitivity constant is the
L∞(A)-norm of the adjoint trace (C7.2) — a worst-case-per-unit-mass
constant, blind to WHERE on A the thrust functional is actually
sensitive; and the lens itself declares the honest limit: QoI
d-continuity (criterion (b)) is a theorem only in 1-D small-BV,
otherwise a sampling-verified assertion (:611-614). L¹ alone is a
sound acceptance metric and a CONSERVATIVE sensitivity metric.

### 3.2 O-b — flux-weighted L² + L∞ guard, the blind-DATA lens at its genuine best (by citation)
Case FOR (contract_blind_data.md:594-604): the norm PAIR — L∞ on
realizability-critical components (A4 handled explicitly) + weighted
L² with weight G = Gâteaux derivative of thrust∘solve at Q̂ — makes
the metric CALIBRATED TO THE DESIGN TARGET: ‖δQ‖_* directly bounds
first-order thrust error (S1 satisfied by construction), supports
worst-case robust design at grade U-a and upgrades naturally to U-b
covariance propagation. Its reject clause is a genuine falsifier
(perturbation inside the band with thrust change beyond the implied
bound rejects the calibration of G).
Case AGAINST as sole/acceptance metric — two independent failures:
- (A2 failure, structural): for a jump of size [q] displaced by δ,
  the L² distance scales as |[q]|·√δ — non-Lipschitz (degenerate) in
  the displacement; the dominant error mode of this data class is
  measured DISPROPORTIONATELY, so an acceptance radius calibrated to
  irreducible phase jitter inflates and admits unrelated smooth-mode
  errors. The modern assimilation literature documents exactly this
  L²-vs-fronts pathology (Freitag et al. 2013 [ABS], §2.3).
- (S2 subtlety the lens's own [PS] grading concedes): G is a
  LINEARIZATION AT Q̂; at fronts the derivative of the solve w.r.t.
  a front-displacement perturbation is NOT an L² object — the formal
  linearization of a shifted discontinuity is a delta sheet. This is
  the classical linearization-at-shocks obstruction; the rigorous
  repair of record is the SHIFT decomposition (Ulbrich 2002/2003
  [ABS]; already homed in this repo: pipeline_audit :102, G12/S1,
  theorem_ledger :235) and, on the solver side, the adjoint
  front-motion terms already load-bearing for the fitted tier (diff
  §3.3 :330-335). So flux-weighted L² is a sharp sensitivity metric
  ONLY on the smooth complement of the jump set; front-position
  uncertainty must ride a separate finite-dimensional parametric
  block (front positions/speeds with their own bars, sensitivities
  via the front-motion adjoint kernel).

### 3.3 O-c — split by role (the judge's candidate), refined
The criteria separate cleanly: L¹ wins A1-A4 and loses sharpness on
S1; calibrated-L² wins S1/S3 and structurally fails A2 (and needs
the shift repair for S2). No single metric satisfies both roles
without inflation ⇒ the split-by-role form wins, PROVIDED the seam
is pinned. Refinement forced by §3.2's second bullet (the emergent
sub-aspect, closed here): the sensitivity half is not "weighted L²"
tout court but weighted-L² ⊕ front-parameter block:

- **Acceptance metric d_acc** = ‖·‖_L¹(A) between PHASE-ALIGNED data
  (gauge quotient per [DATA] 7.5(i) / finding :2316), within the
  L∞(K) realizability guard + TV-bounded class as contract side
  conditions. (Note: the L∞ guard is CONVERGENT between the lenses
  — [PDE] :609-610 and [DATA] :596-598 both carry it; it was never
  in dispute.)
- **Sensitivity metric d_sens** = thrust-calibrated flux-weighted L²
  on the smooth complement of the declared jump set ⊕ finite-
  dimensional front block (front positions/speeds as parameters with
  bars), first-order thrust error = ‖δQ_smooth‖_* + Σ_k |∂J/∂s_k|·
  ε_{s_k} with ∂J/∂s_k from the front-motion adjoint term.
- **Seam (pinned, not left as incomparability)**: the conservative
  bridge is the PDE lens's own C7.2 bound — L¹(A) ball of radius
  ε_acc ⇒ |δJ| ≤ ‖Λ‖_L∞(A)·ε_acc + front-block terms — i.e. the
  acceptance ball always yields a (coarser) certified interval via
  the L∞-dual constant, while d_sens yields the sharp one; both
  feed the SAME interval-separation/tie rule ([PDE] C7.2 = [DATA]
  Claim 7.4, convergent). A datum accepted under d_acc but with
  unbounded d_sens statement is impossible by construction on the
  TV∩L∞ class (front block finite, smooth part L∞-bounded).

### 3.4 O-d — Wasserstein / optimal-transport family: CLOSED by stated reason
Modern family censused at its genuine best (Engquist-Froese-Yang W₂;
Métivier KR/graph-space; unbalanced OT; Dong 2024 — §2.3). Closed
for the CONTRACT SITE on three stated reasons:
1. **The differentiator does not address our question.** OT's proven
   advantage is CONVEXITY of the misfit LANDSCAPE w.r.t. front
   displacement — it cures cycle-skipping in data-FITTING
   optimization (inversion). The contract performs no optimization
   over datum space: acceptance is ball MEMBERSHIP, sensitivity is a
   LOCAL bound. Convexity-in-displacement buys nothing for either
   role.
2. **The proportional-response property is not a differentiator vs
   L¹.** OT distances are linear in front displacement — but so is
   L¹ on BV (translation continuity, [PDE] :187-189). The metric OT
   beats on fronts is L², which the split already confines to the
   smooth complement.
3. **Structural cost on this data class.** Raw OT needs nonnegative,
   mass-matched scalar densities; the datum is a SIGNED,
   multi-component gas-dynamic field. Every modern workaround
   (normalization, graph-space lift, unbalanced OT — Métivier
   [ABS], Dong 2024 [ABS]) exists precisely because this mismatch
   generates artifacts; adopting it would import machinery whose
   entire purpose is to fix a problem we do not need to have.
Named upgrade path (not a duty): if a state-estimation/assimilation
layer is ever inserted UPSTREAM of the contract (fitting a wave
model to raw rig data), OT misfits re-enter as candidates AT THAT
LAYER. Also recorded for orientation: the V&V acceptance literature's
area validation metric (Ferson-Oberkampf class [ABS]) is 1-Wasserstein
on the CDF of a scalar QoI — QoI-space, downstream of C50's
datum-space question; compatible, not competing. Zero inflation:
no OT claim above [ABS] depth is made anywhere in this panel.

### 3.5 Consumers respected (cited, not contradicted)
- Finding contract:datum-uncertainty-contract-missing (:1660-1668):
  this adjudication supplies the missing METRIC half; radius/
  extrapolation semantics stay with the finding's F2 window —
  sequenced together (the finding's own owner field already says
  "sequenced with the C50 metric adjudication").
- C55 (ledger :721-731): ν is a contract datum riding the operating
  box W; C50 governs the Û-component distance, C55 the ambient
  aggregation — disjoint slots, nothing here touches the C55
  single-point default or its sequencing clause.
- W1-W4 (M0 :167-175): the acceptance ball lives INSIDE the validity
  window; excursion is extrapolation = NO DATUM ([PDE] D7.1 :597-599,
  [DATA] Def 7.3 :625-636) — consistent with the window's
  reject-not-error-bar discipline; W1's measured-margin discipline is
  untouched.
- C56 / C49: the front-motion adjoint kernel that d_sens consumes is
  the C49 fitted-tier load-bearing object (diff §3.3); WHICH adjoint
  realization delivers it is C56's question — named, not decided.

---

## 4 PROPOSED VERDICT + DUTIES

### 4.1 Proposed ledger outcome for C50
**ADJUDICATED-SPLIT-BY-ROLE (alternative 3, refined), enum proposal
MIXED-equivalent per landing convention; measurement half = named F2
duty.** Proposed row-note delta text (for the landing window, not
executed here):

> WAVE-3 ADJUDICATION 2026-08-20 (PANEL_C50): split-by-role of
> record. ACCEPTANCE metric = L¹(A) on phase-aligned data within the
> L∞(K) realizability guard + TV-bounded class as contract side
> conditions (blind-PDE lens wins the acceptance role on criteria
> A1-A4; the L∞ guard is lens-CONVERGENT, never disputed).
> SENSITIVITY metric = thrust-calibrated flux-weighted L² on the
> smooth complement ⊕ finite-dimensional front-parameter block
> (positions/speeds with bars, sensitivities via the front-motion
> adjoint term — the shift-differentiability repair of the
> linearization-at-fronts obstruction; blind-DATA lens wins the
> sensitivity role at S1/S3 only WITH this repair; raw flux-weighted
> L² as sole/acceptance metric REJECTED on the √δ front-displacement
> degeneracy). SEAM pinned: L¹-ball ⇒ conservative interval via the
> ‖Λ‖_L∞(A)-dual bound ([PDE] C7.2); sharp interval via d_sens; one
> tie rule (≡ [DATA] Claim 7.4). Wasserstein/OT family CLOSED by
> stated reason (convexity-in-displacement addresses inversion, not
> acceptance/sensitivity; L¹ already linear in front displacement;
> signed multi-component data needs artifact-prone normalization) —
> named upgrade path only at any future upstream assimilation layer.
> Instantiation + all falsifiers = duty F2-C50-CONTRACT-METRIC,
> sequenced with contract:datum-uncertainty-contract-missing and
> contract:phase-gauge-jitter-alignment-unpinned.

### 4.2 Pinned falsifiers (exact tests, armed at first imported datum family)
- **FA-1 (acceptance d-continuity)**: FD sampling of the QoI over an
  ε-net of the d_acc ball at fixed numerics; QoI oscillation failing
  to → 0 with ε rejects d-continuity of the pipeline and with it any
  pointwise-nominal design claim ([PDE] C7.1 TEST :615-618, adopted
  verbatim as the of-record test).
- **FA-2 (gauge quotient)**: for a delivered cycle pair, d_acc
  computed unaligned vs phase-aligned must drop by the predicted
  O(jitter × slope) jump-sheet contribution; failure rejects the
  gauge-quotient specification (ties finding :2316 — same F2 window).
- **FS-1 (calibration)**: adjoint first-order bound violated by a
  direct FD probe outside the probe's own error bar rejects the
  adjoint implementation/calibration ([PDE] C7.2 TEST + [DATA] U-a
  reject clause, convergent).
- **FS-2 (front block, anti-vacuity)**: the FS-1 probe family MUST
  include a pure front-displacement perturbation (jump shifted by δ,
  smooth part frozen); |δJ| must match the front-motion adjoint term
  within bars — passing FS-1 on smooth perturbations alone is
  declared VACUOUS for this data class.
- **F-TIE (seam/consumer)**: two designs declared distinct with
  overlapping certified intervals reject the comparison claim
  (convergent [PDE] C7.2 / [DATA] 7.4 — cited, already of record as
  contract demand).

### 4.3 F2 duty (named, binding)
**F2-C50-CONTRACT-METRIC**: instantiate (d_acc, d_sens, seam
inequality, tie rule) at the contract site (D2.6 / problem-book
contract slot) in the same F2 contract window that consumes finding
contract:datum-uncertainty-contract-missing (radius ε semantics +
extrapolation rule) and finding contract:phase-gauge-jitter-
alignment-unpinned (the alignment operator FA-2 needs); implement
FA-1/FA-2/FS-1/FS-2 as of-record audits at trigger = F2 contract
freeze / first imported real-data family (the finding's own
trigger). All numeric constants derived there, none minted here.

### 4.4 Dependencies + what would overturn
- Depends on (named, not decided): C56 (adjoint realization
  delivering Λ + front-motion kernel); C49 fitted tier as
  certificate bearer (of record, VERDICT_wave2 §4.8).
- WOULD OVERTURN the acceptance half: a demonstrated stage-A audit
  that is NOT L¹-continuous on the L∞∩TV class (breaks A1), or a
  measured datum family whose dominant error mode is not
  front-position jitter (breaks the A2 weighting of criteria).
- WOULD OVERTURN the sensitivity half: FS-2 failing systematically
  (front-motion adjoint term not reproducing pure-shift |δJ|) — this
  would demote d_sens to the conservative L¹×L∞-dual bound alone and
  re-open the row at the sharp-metric slot only.
- WOULD OVERTURN the OT closure: insertion of an upstream
  assimilation/state-estimation layer into the datum pipeline (the
  named upgrade path's trigger).

---

## 5 PAPERS NEEDED (mandatory section)
NONE BLOCKING. Every load-bearing claim above is held at [FULL]
depth on in-repo documents of record; external sources are consumed
at [ABS]/[TITLE] depth and no conclusion exceeds that depth (the OT
closure uses only existence-level facts: what OT's differentiator
is, that normalization workarounds exist). Optional, non-blocking
enrichment if the user wishes to deepen the OT closure's paper
trail: Métivier et al., "Optimal transport in full-waveform
inversion: analysis and practice of the multidimensional
Kantorovich-Rubinstein norm" (arXiv:2101.00904) — would raise reason
3 of §3.4 from [ABS] to [FULL]; no claim currently waits on it.

---

## 6 MACHINE SUMMARY

```
cluster: C50
rows:
  C50:
    proposed: "ADJUDICATED-SPLIT-BY-ROLE — acceptance = L1(A) phase-aligned + L-inf(K) realizability guard (TV-bounded side condition); sensitivity = thrust-calibrated flux-weighted L2 on smooth complement + finite-dim front-parameter block via front-motion adjoint (shift-differentiability repair); seam pinned = L-inf-dual conservative bound bridging acceptance ball to certified interval; one tie rule; Wasserstein/OT closed by stated reason with named upgrade path"
    gated: true
    duty: "F2-C50-CONTRACT-METRIC (instantiate metrics+seam at contract site; arm FA-1/FA-2/FS-1/FS-2; trigger = F2 contract freeze / first imported real-data family; sequenced with findings contract:datum-uncertainty-contract-missing and contract:phase-gauge-jitter-alignment-unpinned)"
rows_adjudicated: 1
deltas_proposed: 1 (C50 row-note delta text, section 4.1; no registry edited)
escalation_candidates: 0
papers_needed: 0 blocking (1 optional enrichment named: arXiv:2101.00904)
candidate_new_rows: 0 (dedup-verified by measured greps this window: shift-differentiability already homed at docs/rde_nozzle_pipeline_audit.md:102, docs/rde_nozzle_theorem_ledger.md:235, docs/rde_nozzle_G12_S1.md; phase-gauge jitter already homed at docs/findings_registry.yaml:2316; OT upgrade path = note text, no row)
census_recency: "1997-2025, newest 2024-2025 (Dong JGR 2024 OT-FWI; 2025 Wasserstein error-metrics); 4 web queries + measured local greps, table section 2.1"
alternatives_closed: 4 (L1-solo as sole metric; flux-weighted-L2-solo incl. as acceptance metric; Wasserstein/OT family; TV-class metrics [inherited blind-PDE exclusion, cited])
inflation_check: done (no external claim above [ABS] depth; both lenses represented by citation at file:line; incumbent = none, declared)
```
