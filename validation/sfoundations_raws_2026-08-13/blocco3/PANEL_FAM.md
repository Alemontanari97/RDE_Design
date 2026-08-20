# PANEL_FAM — DERIVED-CONSTANTS FAMILY (C34, C35, C36, C41, C42, C43)
# S-FOUNDATIONS-C3 wave 3, 2026-08-20. One panel, per-row verdicts.
# BASE = validation/sfoundations_raws_2026-08-13. Census validity
# stamp: 2026-08-20 (WebSearch, 6 queries, table in §2.1).
# Binding frames consumed: BRIEF_wave3_panels.md §0+§FAM;
# BRIEF_wave1_panels.md §0 FRAME; BRIEF_wave2_panels.md §0-bis/§0-ter;
# LOAD-CLASS VALVE (AG-1, user-ratified 2026-08-20) — these rows are
# largely bookkeeping-of-derivation-duties: converged
# sufficient-not-optimized, declared as such per row.

## 1. FROZEN FORMAL STATEMENT (frozen BEFORE search; criteria pre-registered)

**Shared sub-problem (frozen).** The certified loop (marched
axisymmetric Euler solver with fitted fronts, JAX custom_vjp adjoint,
TR-SQP-class driver per VERDICT_wave2 §2.1, certificate/verdict
discipline R5) carries a chain of numerical constants: TR radius
floor/caps, optimizer step tolerance (xtol), variable/constraint
scaling, certificate band composition operators, the reused safety
constant K_RICH, and the asymptotic-range premise under every
two-level band. QUESTION FAMILY: which of these constants are DERIVED
(from measured noise floors, observed orders, conditioning) vs
literal; what composition policy governs heterogeneous bands; and
what is the per-constant derivation program with falsifier. The
tolerance-chain doctrine of the blind trees (O-F25:
phaseA_tree_optimization.md:1293-1330 machine-eps -> linear tol ->
Newton floor -> eps_J -> eps_g -> optimizer tolerances -> bands, each
link measured; H-F40: phaseA_tree_hyperbolic.md:1253-1272 global
budget partition, derivation hash per tolerance) is the candidate
formal frame.

Per-row single main questions + pre-registered decision criteria
(what would make each option win, derived from the question — frozen
before the census ran):

- **C34 (TR floor/caps).** Q: what derives TR_FLOOR/tr0/tr_cap from
  measured noise so certificate semantics never rest on a literal?
  WIN criteria: incumbent literals win only if a measured
  rho-histogram shows the certified walks never touch the floor/cap
  (immateriality); the noise-derived-floor alternative wins if the
  modern noisy-TR literature gives a derivation rule consuming only
  quantities the loop already measures (tol_dp, ||g||) AND the rule
  is checkable on the first post-8761dce campaign artifact. A third
  option (drop the floor entirely) wins only if theory shows floors
  are unnecessary under noise — pre-registered as unlikely (S18 clip
  exists because of a real collapse mode).
- **C35 (xtol).** Q: what xtol does the Newton floor on the u scale
  imply? WIN criteria: literal 1e-10 wins only if it provably sits
  between the true stagnation floor and the smallest step the driver
  must resolve, with margin, on the record walks (i.e. accidentally
  correct); the derived form wins if xtol = (safety) x (Newton floor
  propagated to the u scale via the Dv map) is computable from
  already-measured quantities. Duty-only outcome (bookkeeping) wins
  if the derivation's inputs are owned by another adjudicated window
  (the C18/C20 Tier-1 seam) — then C35 pins the FORM and consumes
  that window's value.
- **C36 (scaling policy).** Q: what scaling policy is derived rather
  than frozen? WIN criteria: frozen once-per-walk Jacobi wins if
  refresh is measurably cost-bearing or destabilizing; per-segment
  refresh + constraint-row equilibration wins if it is free of extra
  evaluations (the diagonal is already re-measured) and covers the
  measured defect (constraint rows orders steeper, never
  equilibrated); the H^s spectral-metric alternative (O-F7) wins
  only if it can be instantiated without new machinery (else it is
  an option-with-precondition, named not adopted — LOAD-CLASS).
- **C41 (band form/composition).** Q: ONE declared composition
  policy for heterogeneous bands? WIN criteria: an option wins by
  giving a decidable per-site rule (which operator, from which
  correlation argument) that is conservative where correlation is
  unknown and collapses to RSS where independence is measured; the
  incumbent ad-hoc mix loses automatically if any site is shown
  under-covering (the 2.11x vs intended 4x arithmetic of record).
- **C42 (K_RICH role reuse).** Q: per-role derivation program for
  every K_RICH role — census the roles FIRST (measured grep). WIN
  criteria: the one-numeral incumbent wins per-role only where the
  role's constant is provably redundant safety on an already-derived
  bound; the per-role alternative wins where a published derivation
  route exists (GCI Fs from observed p; KS rho from conservativeness
  — already derived; coverage statistics for thresholds). Outcome
  class pre-registered: ordered derivation program (duty), not a
  same-window re-derivation of 100+ sites.
- **C43 (asymptotic-range handling).** NOT a fresh adjudication —
  CONFIRM-ALIGNMENT duty only (brief §FAM): verify the declared
  content identity against VERDICT_wave1 §4.5 and close the residue
  bookkeeping. Criterion: textual identity of the row's listed
  alternative with the C11 interim regime + consistency of
  status/owner/evidence fields.

**Materiality (pre-registered, per §0-ter(c)).** C34/C35/C36 sit on
the S18 finding of record "conditioning IS the convergence rate on
this driver" (findings driver-nonsmooth:jacobi-scaling-frozen
:1257) and the GAP-29 one-flip evidence that a factor 2 on a
tolerance constant can flip cert_verdict (glossary NTF entry) —
the family is MATERIAL as a class; individual constants may still be
immaterial and are closed on cost where shown so. C41/C42 are
certificate-semantics rows (coverage), material by construction.
C43 is bookkeeping (zero fresh materiality).

## 2. SOTA CENSUS (dated 2026-08-20)

### 2.1 Query protocol table (verbatim strings; WebSearch, US index)

| # | Query (verbatim) | Date | Hits returned / screened / included |
|---|---|---|---|
| Q1 | "noise-aware trust region method minimum radius bound gradient noise Sun Nocedal ECNoise More Wild" | 2026-08-20 | 10 / 10 / 5 |
| Q2 | "optimization termination criteria in presence of function evaluation noise stopping test derived noise level 2023 2024" | 2026-08-20 | 10 / 10 / 1 |
| Q3 | "variable scaling nonlinear programming constraint row equilibration SNOPT diagonal scaling policy derived" | 2026-08-20 | 8 / 8 / 3 |
| Q4 | "Sobolev gradient smoothing shape optimization metric order derived Hessian symbol Schmidt Schulz aerodynamic" | 2026-08-20 | 10 / 10 / 3 |
| Q5 | "ASME V&V 20 uncertainty combination u_val RSS numerical error GUM correlated components validation uncertainty" | 2026-08-20 | 9 / 9 / 3 |
| Q6 | "grid convergence index safety factor derived Xing Stern factor of safety method observed order 2010 2011 verification" | 2026-08-20 | 7 / 7 / 3 |

Databases/communities covered: arXiv (math.OC, cs.CE), Springer
MathProg/OptEng, ASME (JFE, VVS), SIAM-adjacent preprints, DLR elib
(shape-calculus school), plus the ON-DISK arrivals (manifest
BASE/MANIFEST_papers_foundations_c.md) and the repo literature
registry (WANTED rows cited below). Russian classical school: not
census-bearing for this family (these are numerics-of-certification
constants, not gasdynamics — declared per §0-ter(a); the classical
end is covered by Richardson/GCI lineage itself).

### 2.2 Corpus recency
Span 1981-2026; newest included items 2023-2025 (Sun-Nocedal MathProg
2023; Cao-Berahas-Scheinberg MathProg 2023; noisy TR-SQP arXiv
2411.02665, 2024; interior-point-with-noise arXiv 2405.11400, 2024;
TR gradient-sampling for noisy nonsmooth, Optim.Eng. 2026). The
modern refined line (noise-aware optimization constants) is
represented, not just classics.

### 2.3 Per-source one-liners (read-depth markers per §0-bis(b))

Noisy-optimization constants (C34/C35):
- Sun & Nocedal, "A trust region method for the optimization of
  noisy functions", Math. Prog. 2023 / arXiv:2201.00973 [ABS]: TR
  radius must be kept from shrinking below the noise scale — the
  radius is bounded BELOW by a quantity derived from the measured
  function-noise level epsilon_f; only the noise standard deviation
  is needed, no extra evaluations. THE published derivation rule for
  the C34 alternative's class.
- Cao, Berahas & Scheinberg, "First- and second-order high
  probability complexity bounds for trust-region methods with noisy
  oracles", Math. Prog. 2023 / arXiv:2205.03667 [TITLE]: complexity
  guarantees for TR under bounded-noise oracles — theory backing
  that noise-floored TR constants are the analyzed regime.
- "A Trust-Region Algorithm for Noisy Equality Constrained
  Optimization", arXiv:2411.02665 (2024) [TITLE]: extends the
  noise-aware TR line to the constrained case (our case).
- Moré & Wild, ECNoise ("Estimating computational noise", SISC
  2011) [ABS, cited via Q1 result text and O-F25's independent
  blind citation]: the standard instrument for measuring epsilon_J
  along design rays — the measurement half every derivation above
  consumes. PAPERS-NEEDED item 1.
- "On the convergence of interior-point methods for
  bound-constrained problems with noise", arXiv:2405.11400 (2024)
  [ABS]: termination tests that detect the noise-dominated regime —
  modern support for noise-derived stopping (C35's gtol-side
  neighbor; the xtol form is the same doctrine on the step scale).
- Deuflhard, Newton Methods (CSM 35), ON DISK
  (literature/deuflhard_2011_newton_methods_affine_invariance_csm35.pdf)
  [TITLE this panel — deliberately NOT consumed at depth here: the
  Deuflhard band is the C20 Tier-1 window's object of record
  (VERDICT_wave2 §4.9/§4.11) and this panel must not collide with
  that window; C35 consumes its OUTPUT (the floor value), see seam].
- Nocedal & Wright 2ed, ON DISK
  (literature/nocedal_wright_2006_numerical_optimization_2ed.pdf)
  [TITLE this panel]: cited by the C44/C32 windows for FD error
  models and TR safeguards; for THIS panel it is background — no
  claim here rests on unread pages (zero inflation).

Scaling (C36):
- Gill-Murray-Saunders, SNOPT (SIREV/SIOPT) [ABS]: production-code
  precedent for automatic row/column scaling reducing Jacobian
  element spread — the "constraint-row equilibration (SNOPT
  lineage)" alternative's source identity.
- "Scaling nonlinear programs" (Math. Prog. Study line, 1981)
  [TITLE]: the classical automatic-scaling procedure family.
- "Performance analysis of linear and nonlinear techniques for
  automatic scaling of discretized control problems" (Oper. Res.
  Lett. 2014-15) [ABS]: measured evidence that automatic scaling
  (incl. projected-Jacobian-row normalization) improves NLP
  conditioning on SNOPT/IPOPT — modern support that equilibration
  is a derived, not aesthetic, choice.
- Schmidt/Schulz school (Sobolev/Steklov-Poincare metrics; "Combining
  Sobolev smoothing with parameterized shape optimization",
  C&F 2022 / arXiv:2109.15279) [ABS]: Sobolev smoothing =
  approximation of the reduced shape Hessian; the modern instance of
  O-F7's derived-metric alternative. Precondition: Hessian-symbol
  probes (HVP machinery = the C32 wave-2 landed window).

Band composition + safety factors (C41/C42):
- ASME V&V 20-2009 (R2016) [ABS via Coleman overview PDF]: u_val
  composition of experimental/numerical/parameter uncertainties;
  GUM-lineage RSS with declared correlation treatment — the
  standard's composition semantics is exactly the "declared
  GUM/RSS policy" alternative. PAPERS-NEEDED item 2 (standard text
  paywalled).
- ISO GUM (JCGM 100) [ABS, via the V&V 20 overview]: RSS for
  independent components, covariance terms otherwise — the root
  doctrine.
- Roache GCI (1994/1997) — literature registry WANTED row
  wanted_roache_gci_1994_1997 (:838-843) [registry-row depth]:
  Fs=1.25 only with three grids + observed order; Fs=3 two-grid.
  Directly prices the repo's K=4-on-two-level practice: the repo is
  MORE conservative than Roache two-grid (4 > 3) — an honest datum
  FOR the incumbent's interim safety, not for its derivation status.
- Celik et al. 2008 — WANTED row wanted_celik_2008 (:844-849)
  [registry-row depth]: codified three-mesh observed-p GCI = the
  C11/C43 interim regime's published procedure.
- Eca & Hoekstra 2014, JCP 262:104-130 — WANTED row
  wanted_eca_hoekstra_2014 (:850-855) [registry-row depth]: safety
  factor as a FUNCTION of observed order and fit quality — the
  strongest published instance of "safety factors derived, not
  frozen" (the C42 per-role doctrine for the Richardson role).
- Xing & Stern, "Factors of safety for Richardson extrapolation",
  ASME JFE 132:061403 (2010; discussion+closure 2011) [ABS]: factor
  of safety derived from the ratio observed/theoretical order with
  95%-coverage statistical evidence — the second published
  derivation route for the same role; open PDF located (DTIC/UFPR
  mirrors), procurement optional.

### 2.4 Cava (validation/ADVISORY_litreview_confrontation_2026-08-13.md)
Measured sweep this window: `grep -n -i "GCI|K_RICH|safety factor|
1\.25|toleran" ADVISORY_litreview_confrontation_2026-08-13.md` ->
hits only on Harroun's c_F = 1.25 (a thrust-coefficient datum, rows
:51/:794/:805/:829/:834 and R26 :1153 — cycle-average resolution
threshold). NOT the Richardson/KS safety constant: no cava row bears
on this family. Declared closed by stated reason (the numeral
coincidence 1.25 is semantic noise).

### 2.5 §0-bis cross-cutting axes — per-row bearing (one sentence each)
- (1) optimizer query-level choice: bears on C34/C35/C36 only
  through the wave-2 C31 verdict (TR-SQP direction of record,
  VERDICT_wave2 §2.1) — consumed as the frame, not re-opened; does
  not bear on C41/C42/C43 (estimator-side constants).
- (2) discrete-vs-continuous adjoint: does not bear on any FAM row
  (the constants are downstream of whichever adjoint; the choice
  itself is C56's row, VERDICT_wave2 §2.10) — named, not decided.
- (3) moving-mesh/r-adaptive: does not bear (no FAM constant
  parametrizes mesh motion; mesh law = C9, landed wave 1).
- (4) adjoint-free routes: does not bear (constants of the certified
  gradient loop; the exploration tier is the C31 §4.14 candidate).
- (5) emergent sub-aspect: ONE emerged — composition of TIMING bands
  (engine_speed_bench.py:449 K_RICH x measured spread on wall-clock)
  sits outside certificate semantics; named in C42 role census as
  out-of-certificate-scope, no new row needed (speed-audit territory,
  measured numbers of record).

## 3. ADJUDICATION (per row)

### 3.1 C34 — TR floor/caps (docs/choice_ledger.yaml:489-497)

**Incumbent case (genuine).** TR_FLOOR=1e-3, tr0=0.05, tr_cap=0.25
(a1_toc_variational_jax.py:1367-1369) exist because of a REAL
recorded collapse mode (S18 clip; the S20 ratchet comment :1575-1579
— tr_cap only ever decreases after replay-fidelity misses). The
literals have survived every committed walk; [P-TRFLOOR]'s inputs
were forfeited by the pre-8761dce kill (findings
conditional:P-TRFLOOR :283-291, blocked-with-named-cause) — the
incumbent is not defensible as DERIVED, but it is defensible as the
only value pair with campaign history.

**Alternative (noise-derived floor, ledger: Cartis-Scheinberg;
More-Wild).** Tree advocacy: O-F17
(phaseA_tree_optimization_CONDENSED.md:140-146; full tree L964):
radius-update constants DERIVED from measured actual/predicted
reduction statistics — accept thresholds where the measured
rho-histogram separates model-valid from model-broken steps. Diff of
record: CONVERGENT (phaseB_tree_diff.md:176-178). Census: Sun-Nocedal
2023 [ABS] gives the exact modern rule class — the TR radius is
bounded below by a noise-derived quantity, consuming only the
measured noise level; constrained extension exists (2411.02665
[TITLE]).

**Adjudication.** The alternative wins on DIRECTION (published
derivation rule + blind-tree convergence + zero extra evaluation
cost); the incumbent retains custody until the derivation's inputs
exist — which is precisely the standing blocked-with-named-cause
state. Per LOAD-CLASS VALVE this row is bookkeeping of an already-
named duty: the panel's job is to pin the protocol so the trigger
consumes it mechanically. Sufficient-not-optimized protocol (declared
such): on the FIRST post-8761dce decisive campaign artifact,
(i) run the rho-histogram over accepted/rejected steps (O-F17 form);
(ii) measure epsilon_J at the incumbent walk's scale (ECNoise-class
ray probe, or the already-measured tol_dp as the pessimistic bound —
tol_dp IS a measured noise carrier of record, a1_toc:2259-2263);
(iii) set TR_FLOOR_derived = K_RICH x tol_dp / ||g||_seg (the ledger
alternative's own formula) and tr_cap from the rho-histogram's
model-valid support. Immateriality branch declared: if the measured
histogram shows no accepted step within 10x of either literal, the
literals are immaterial and are KEPT with a derived-immateriality
stamp (cost-decided, honest per §0-ter(c)).

**Seam (named per brief).** The C18/C20 Tier-1 window (VERDICT_wave2
§4.11: kappa band + NEWTON_TOL_FACTOR = one question) owns the
Newton floor that seeds link (b) of the tolerance chain; C34's
epsilon_J measurement sits DOWNSTREAM (link c->e). No collision: C34
consumes the C20-window floor as input, never re-derives it.

### 3.2 C35 — xtol (docs/choice_ledger.yaml:499-507)

**Incumbent case (genuine).** Literal 1e-10 at the assignment site
a1_toc_variational_jax.py:2264 and 7 call sites (measured:
`grep -rn "xtol=1e-10" --include="*.py"` = 7 + 1 assignment, this
window). It has never caused a recorded false convergence by itself;
the S18 finding (status 2 with KKT open = stale-model collapse,
a1_toc:1941 comment) was a model-staleness symptom, not an xtol
mis-set (ledger note :507 says exactly this).

**The prose derivation — FOUND, and it is a REFUTATION, not a
derivation.** The brief mandates "find it or declare absent". Found:
findings row variational-driver:cross-unit-and-slack-tolerances
(:633-641) — "xtol = 1e-10 mislabeled 'Newton floor on W scale'
(actual floor ~4e-14)"; the code comment a1_toc:2261 carries the
mislabel. So the prose that exists DISPROVES the incumbent's label:
1e-10 sits ~4 decades ABOVE the measured floor, i.e. it is an
UNDECLARED slack factor ~2.5e3, not a derived floor. Tree advocacy:
O-F25 link (e) (phaseA_tree_optimization.md:1310-1313): terminate at
nu x eps_g with nu derived from a declared false-positive rate (P8
hypothesis-test form); H-F40 (phaseA_tree_hyperbolic.md:1262-1267):
derived stationarity tolerance from the TR model bound, "not a
gradient-norm folklore number". Diff: CONVERGENT with the derivation
duty (phaseB_tree_diff.md:179-180). Census: the 2024 interior-point-
with-noise line [ABS] supports noise-regime-detecting termination as
the modern norm.

**Adjudication.** Alternative wins (derived form); LOAD-CLASS
sufficient pin: xtol_u = K_RICH x floor_W / median(Dv) with floor_W
= the C20-window Newton floor propagated to the u scale via the SAME
Dv map the driver uses (the findings row :640 already names
"scaled-space gtol via the same Dv map" — same duty window, one
derivation). The 1e-10 literal is retired to derived-or-declared at
the F2 driver window; until then it stands as DECLARED slack (the
honest label swap costs one comment line and is part of the proposed
delta). Materiality: honest both ways — 1e-10 >> 4e-14 means the
driver never terminates ON the floor, so the risk is premature-stop
masquerading as convergence; the S18 symptom record shows exactly
this class fires in practice: MATERIAL, not immaterial.

### 3.3 C36 — Scaling policy (docs/choice_ledger.yaml:509-517)

**Incumbent case (genuine).** Jacobi Dv measured once per walk from
objective curvature (a1_toc:1370, 1697-1746), objective-only; it
LANDED the S18 plateau escape (R-3 activation comment :1750) — the
incumbent is a measured-once derived object, not a literal; freezing
it preserves RK-G replay semantics (comment :1281-1283).

**Alternatives.** (a) Per-segment refresh from diag(H) +
constraint-row equilibration (SNOPT lineage) — findings row
driver-nonsmooth:jacobi-scaling-frozen (:1254-1262) carries the
measured defect: Dv never refreshed across 19-21 frontier segments,
blind to constraint rows (KS rho ~5.75e4 -> rows orders steeper,
never equilibrated), refresh FREE (diag of the per-segment
re-measured H costs zero extra evals); the speed audit's DEAD row
killed only the REMOVAL lever (ledger note :517) — removal is dead,
refresh is untouched. Census: SNOPT lineage [ABS] + the 2014-15
automatic-scaling comparison [ABS] (measured conditioning gains on
SNOPT/IPOPT). (b) H^s metric from the MEASURED reduced-Hessian
symbol — O-F7 (phaseA_tree_optimization_CONDENSED.md:63-69, full
L472): probe H's action on high-frequency shape modes via HVPs, fit
the decay exponent, set smoothing order to flatten it; modern
instance = Schmidt/Schulz Sobolev-smoothing-as-Hessian-approximation
[ABS]. Diff: ENRICHING (phaseB_tree_diff.md:181-185).

**Adjudication.** (a) WINS as the converged direction: it is free,
it addresses the measured defect, it has production-code precedent,
and no tree defends the frozen policy; the incumbent's replay-
semantics concern is answered by the findings row's own pin
(determinism bit-check registered). (b) is real but carries a
precondition (HVP probe machinery = the C32 wave-2 landed window's
object) — recorded as OPTION-WITH-STATED-PRECONDITION (the C44
precedent pattern, brief §REMENG), named not adopted; adopting it
now would be over-machinery on a bookkeeping row (LOAD-CLASS).
Falsifier pinned: refreshed-vs-frozen twin walk on the S18 record
case; refresh must not move any certified verdict beyond its band
(if it does, the refresh policy is REJECTED and the row re-opens
with that datum). Constraint-row equilibration acceptance test:
post-equilibration row-norm spread reduced by a measured factor
with no verdict flip.

### 3.4 C41 — Band form/composition (docs/choice_ledger.yaml:562-573)

**Incumbent case (genuine).** K=4 pointwise two-level bands with
ad-hoc sum/max/heterogeneous mixes — every site individually
DERIVED-shaped (K x measured spread + floor), and no committed
verdict is currently touched by the composition defect (findings
thermo-bands:band-composition-no-declared-rule :1191-1199, honest
datum: D-prime band max-dominated 19:1).

**Alternatives + advocacy.** Declared GUM/RSS policy: census = ISO
GUM [ABS] + ASME V&V 20 u_val [ABS via overview]; trees 3/4
independent: H-F39 (phaseA_tree_hyperbolic.md:1225-1250) budget
TABLE t1-t6 with measured values + derived bands, partition itself
derived; O-F24 (phaseA_tree_optimization_CONDENSED.md:190-196)
mu-weighted sum with measured effectivity band; O-F25 link (f)
(full tree :1313-1314): "each certificate band = RSS or sum
(declared which, per correlation argument)" — the alternative
VERBATIM, derived blind. Diff: CONVERGENT with declared-policy, "no
tree tolerates ad-hoc mixes" (phaseB_tree_diff.md:200-204).
Three-level GCI / topology-conditioned / running-max: these are
per-site band FORMS, not composition operators — they live inside
C11's landed interim regime (VERDICT_wave1 §2.4) and are consumed,
not re-opened here (brief cross-link honored).

**Adjudication.** Declared-policy WINS; the measured 2.11x-vs-4x
undercoverage arithmetic (findings :1194) refutes max-composition
for comparable components outright — the incumbent mix loses by its
own pre-registered criterion. LOAD-CLASS sufficient policy (strong,
trivially checkable, declared sufficient-not-optimized):
(P1) components with a stated independence/correlation argument ->
RSS (GUM); (P2) unknown correlation or same-mechanism components ->
linear sum (conservative); (P3) max PERMITTED only with a recorded
dominance certificate (ratio >= K_RICH between the top component
and the runner-up, measured at composition time — the 19:1 D-prime
datum passes, comparable components fail); (P4) every composed band
records which of P1-P3 applied (derivation-hash spirit, H-F40).
Any site changed moves toward the conservative composition
(findings-row owner text honored). This policy needs no new
machinery — it is a declaration + a pass over the max sites.

### 3.5 C42 — K_RICH role reuse (docs/choice_ledger.yaml:575-583)

**Role census FIRST (measured this window, SR-12).** Commands:
`grep -rn "K_RICH" --include="*.py" .` (excl. GENO) = 107 sites in
17 files; classification by functional role from the full match list
(content grep of record, this window):
1. Two-resolution Richardson band multiplier (K x |D_h − D_h/2| +
   floor): a1_ideal_march_jax.py:1231/1267/1459; g0_spike_*.py:172/
   184/480; o33_bench.py:709/739/913; o31cs_instrument.py:304;
   a1_march_scan.py:864/899; adaptive_knot_optimize.py:266/380;
   a1_toc_variational_jax.py:2164/2224/2490; def_twin_falsifier.py
   (F-branches); s25bis_notaknot_twin.py:135; validity_monitor.py:221.
2. KS sharpness rho = K_RICH ln(N)/mu0: margin_governor.py:312;
   def_twin_falsifier.py:837; margin_tolerance_backoff.py:119.
3. KS finite-fallback/sentinel magnitude (−K_RICH·m_ref lane guard,
   −2K_RICH·m_ref G1 gradient): margin_governor.py:207-250;
   def_twin_falsifier.py:706-748.
4. P4 instance margin floor delta_inst = min_margin/K_RICH:
   a1_toc_variational_jax.py:2147; adaptive_knot_optimize.py:362.
5. Fold-implication threshold m_ref/K_RICH: locus_diagnosis.py:276.
6. Lipschitz-surrogate safety L_TB = K_RICH x max(two-point grads)
   ([X-TBAK]): margin_tolerance_backoff.py:147.
7. Thermo-table remainder floors (K_RICH x dT^2 x curv class):
   thermotab_c1_jax.py:384-637 (multiple).
8. Table floor guard (Gmin − K_RICH x dG): thermotab_c1_jax.py:488/635.
9. Timing band (K_RICH x measured wall-clock spread):
   engine_speed_bench.py:449 — OUT of certificate semantics
   (declared, §2.5 axis (5)).
10. Sensitivity-propagated landing band (K_RICH x dval_ds x cell):
   def_twin_falsifier.py:399/453.
Plus the two NOTIFIED roles consumed per mandate: (N1) wave-1
(VERDICT_wave1 §4.6): C27 near-binding band width w + chatter
red-line multiplier; C11 leg (a) produces the observed-p data this
audit consumes. (N2) wave-2 (VERDICT_wave2 §4.12): C21
[X-TBAK]-pattern omega surrogate in z = NEW role (role-6 pattern at
a new quantity); C31TRIO consumes C27/C28-derived rho constants (no
new role). MEASURED RESULT: the ledger's "8 roles" is stale — the
measured census is 10 in-code functional roles (9 certificate-
bearing + 1 out-of-scope) + 2 notified pending roles. Proposed note
delta carries the correction with this command.

**Adjudication.** Diff of record: 4/4 AGAINST the incumbent
(phaseB_tree_diff.md:205-209) — V-F28
(phaseA_tree_variational_CONDENSED.md:234-238) "every safety factor
traced to the measured effectivity distribution (no magic 1.25)";
H-F26 (phaseA_tree_hyperbolic_CONDENSED.md:168-172) safety factors
DERIVED from estimated-to-realized error ratios on the oracle suite;
H-F40 derivation hash per tolerance. Census: TWO independent
published derivation routes for role 1 exist (Eca-Hoekstra 2014
[registry-row]: Fs = f(observed p, fit quality); Xing-Stern 2010
[ABS]: Fs = f(p_obs/p_th) with 95% coverage evidence) — the
alternative is at full published strength for the highest-count
role. The incumbent has zero independent defenders BUT an honest
partial defense per-role: role 2 (rho) is ALREADY
conservativeness-derived (C27 window of record — K_RICH there is an
input safety, not a fitted constant); roles 3 and 8 are sentinel/
structural magnitudes where the constant needs a boundedness
argument, not coverage statistics; role 7 multiplies an
already-derived remainder bound (redundant safety, cheap to declare).
Adjudication per pre-registered criteria: PER-ROLE DERIVATION
PROGRAM wins, executed as an ORDERED audit (the R25/AC5 audit row's
instance), NOT a same-window re-derivation — LOAD-CLASS: the
sufficient hypothesis "K=4 covers Fs=3 (Roache two-grid) and the
measured p_obs >= 0.415 coverage bound (VERDICT_wave1 §2.4)" keeps
every current band VALID-AS-CONSERVATIVE while the program runs.
Order (derived from data availability): role 1 first (consumes
F2-C11-ESTIMATOR-CAMPAIGN leg (a) observed-p data — dependency of
record), then roles 4/5 (margin-distribution coverage, campaign
artifacts), then 6/N2 (third-point falsifier), then declarations for
2/3/7/8/10 (derivation-or-declared-structural, one paragraph each);
role 9 declared out-of-scope. Falsifier per role 1 (pinned): any
site where the Eca-Hoekstra/Xing-Stern-derived Fs EXCEEDS 4 at
measured p_obs refutes the "K=4 conservative" hypothesis for that
site class and forces the derived constant immediately.

### 3.6 C43 — Asymptotic-range handling (docs/choice_ledger.yaml:585-593) — CONFIRM-ALIGNMENT ONLY

Duty per brief: verify the declared content identity against
VERDICT_wave1 §4.5 and close residue bookkeeping; NOT a fresh
adjudication; §0-ter in reduced form (no fresh census — none run).

**Verification (all three legs PASS):**
1. Content identity: row alternative text :589 "per-site
   observed-order check (o32 estimator reuse) + NON-CONCLUSIVE
   propagation" vs the C11 interim regime (VERDICT_wave1 §2.4:
   observed-p Richardson/GCI via the [X-O32] extension (GAP-9);
   K=4 in-loop only at sites with measured p_obs >= 0.415; LSQ at
   NON-CONCLUSIVE order) — IDENTICAL in content: o32 reuse =
   [X-O32] extension; NON-CONCLUSIVE propagation = the degraded-p
   propagation rule. CONFIRMED.
2. Ledger row state: status MIXED :590, evidence =
   VERDICT_wave1.md#4.5 :591, owner "F2 (aligned with C11; was
   S25)" :592, note carries the alignment text + shared GAP-9
   pointer :593 — all consistent with VERDICT_wave1 §4.5's proposed
   delta (status wording there is "ADJUDICATED-WITH-C11", enum
   MIXED; the row carries exactly that). CONFIRMED.
3. Residue bookkeeping: the measured half lives in
   F2-C11-ESTIMATOR-CAMPAIGN leg (a); findings row
   mesh-amr:observed-order-not-at-band-sites (:1185-1190) carries
   the trigger ("next band-bearing verdict at an unverified observed
   order, or the R25 K_RICH audit window") and feeds the C42 audit —
   the dependency chain C43 -> C11 leg (a) -> C42 role-1 is closed
   and singly-owned; no orphan residue found. CONFIRMED.

Verdict: CONFIRMED-ALIGNED, zero delta beyond a one-line row-note
append recording this wave-3 confirmation. No escalation.

## 4. PROPOSED VERDICTS + DUTIES (proposals only; landing window executes)

### 4.1 C34
- Proposed: NEVER -> "ADJUDICATED-SPLIT (direction converged wave-3:
  noise-derived floor/caps per O-F17 + Sun-Nocedal class; measured
  half blocked-with-named-cause UNCHANGED — [P-TRFLOOR] trigger =
  first post-8761dce decisive campaign artifact)".
- Protocol pin (sufficient-not-optimized, declared): rho-histogram +
  epsilon_J probe (ECNoise-class or tol_dp pessimistic bound) ->
  TR_FLOOR_derived = K_RICH x tol_dp/||g||_seg, tr_cap from the
  model-valid rho support; immateriality branch: no accepted step
  within 10x of either literal -> literals kept with
  derived-immateriality stamp.
- Falsifier: derived floor producing a step-rejection cascade on the
  record walk (Sun-Nocedal failure mode) -> the derivation rule, not
  the floor concept, is rejected; literals restored with the datum.
- Duty: F2-C34-TRFLOOR-DERIVE (= [P-TRFLOOR] consumed at trigger;
  same window as the rho-histogram instrumentation). Dependencies:
  consumes C20-window Newton floor (seam §3.1); no collision.
- What-would-overturn: a modern source showing noise-floored TR
  constants HARM constrained certified loops (none found, Q1).

### 4.2 C35
- Proposed: NEVER -> "ADJUDICATED-SPLIT (derived form converged
  wave-3: xtol_u = K_RICH x floor_W/median(Dv), floor_W = C20-window
  output; prose 'derivation' of record FOUND = findings
  variational-driver:cross-unit-and-slack-tolerances — it REFUTES
  the incumbent label (actual floor ~4e-14 vs literal 1e-10);
  literal retired to declared-slack pending the F2 driver window)".
- Falsifier: negative control — at the derived xtol a walk with KKT
  open above the gtol band must NOT terminate with status 2; firing
  = the propagation (Dv map) is wrong, re-derive from the u-scale
  directly.
- Duty: F2-C35-XTOL-DERIVE, RIDES the existing findings-row owner
  window (cross-unit tolerance repair, :640) — one window, not two.
  Dependencies: C20/C18 Tier-1 seam (consumes floor value); C36 (the
  same Dv map — if C36's refresh lands, xtol_u re-derives per
  segment for free, name only).
- What-would-overturn: measurement that the true stagnation floor on
  u scale is ABOVE 1e-10 on production walks (would make the literal
  accidentally correct; the ~4e-14 record datum says otherwise).

### 4.3 C36
- Proposed: NEVER -> "CONVERGED-panel (direction: per-segment Dv
  refresh from diag(H) + constraint-row equilibration, SNOPT
  lineage — free, addresses the measured defect, no tree defends
  frozen; adoption gated on the twin-walk falsifier) with
  OPTION-WITH-STATED-PRECONDITION recorded: O-F7/Schmidt-Schulz H^s
  metric from measured Hessian symbol (precondition: HVP probes =
  C32 window machinery)".
- Falsifier (pinned): refreshed-vs-frozen twin walk on the S18
  record case — any certified verdict moved beyond its band REJECTS
  the refresh policy; determinism bit-check (findings :1261) rides.
- Duty: F2-C36-DVREFRESH (= [P-DVREFRESH] instanced; same trigger
  as findings :1262 — first cert/margin-active walk).
- Dependencies: C39/C19 scale seam is REMENG territory — named, not
  decided here; C35 Dv-map link named above.
- What-would-overturn: measured refresh cost or nondeterminism on
  the committed stack (the free-refresh premise is measured from
  the per-segment H re-measure of record — if C32's landed policy
  removes the full per-segment H, diag(H) is no longer free and the
  duty re-prices: NAMED consequence of the C32 wave-2 outcome, to
  be checked at duty execution).

### 4.4 C41
- Proposed: NEVER -> "CONVERGED-panel (declared composition policy
  P1-P4: RSS with stated independence argument / linear sum at
  unknown correlation / max only with recorded >= K_RICH dominance
  certificate / per-band P-tag recorded; sufficient-not-optimized
  per LOAD-CLASS; adoption = the F2 band-policy pass already owned
  by findings thermo-bands:band-composition-no-declared-rule)".
- Falsifier: O-F25 chain falsifier (any downstream band violated in
  cross-checks invalidates the composition at that site — chain
  re-measured from that link down); plus the standing trigger
  (max-composed band with comparable components) now DECIDABLE by
  the P3 dominance certificate.
- Duty: F2-C41-BAND-POLICY (= the findings-row owner window; one
  paragraph policy + pass over max sites). Dependencies: consumes
  the C11 interim regime for per-site band FORMS (VERDICT_wave1
  §2.4, not re-opened); C42 role 1 provides the K inside each
  component — independent question, no collision (composition
  operates on components whatever their K).
- What-would-overturn: a correlation measurement showing RSS
  under-covers at a P1-tagged site (moves that class to P2 by the
  policy's own conservative-direction rule — self-repairing, not
  overturning).

### 4.5 C42
- Proposed: NEVER -> "ADJUDICATED-SPLIT (per-role derivation program
  converged wave-3, 4/4 diff + two published routes for the dominant
  role; measured half = ordered audit F2-C42-KRICH-ROLE-AUDIT;
  interim validity hypothesis DECLARED: K=4 >= Roache two-grid Fs=3
  and coverage conditioned on p_obs >= 0.415 per VERDICT_wave1
  §2.4)". Role-census note delta: "8 roles" -> "measured 2026-08-20:
  107 .py sites / 17 files; 10 functional roles (9
  certificate-bearing + timing role declared out-of-scope) + 2
  notified pending (C27 w/red-line; C21 omega-in-z)"; command
  recorded in §3.5 (SR-12).
- Duty: F2-C42-KRICH-ROLE-AUDIT (= the R25/AC5 audit row instanced),
  ORDERED: role 1 (Fs from observed p — Eca-Hoekstra/Xing-Stern
  routes) AFTER F2-C11-ESTIMATOR-CAMPAIGN leg (a) delivers
  observed-p data (dependency of record, VERDICT_wave1 §4.6); then
  roles 4/5 (coverage from campaign margin distributions); then
  6/N2 (third-point falsifier); then one-paragraph
  derivation-or-declared-structural closures for roles 2/3/7/8/10.
- Falsifier (pinned now): any site where published-route Fs(p_obs)
  > 4 refutes the interim conservativeness hypothesis for that site
  class -> derived constant forced immediately at that class.
- Dependencies: C27 window owns rho (role 2) — consumed, not
  re-derived; C21 window owns the omega surrogate instance; C41
  orthogonal (composition vs component-K).
- What-would-overturn: the audit finding K=4 optimal-or-conservative
  at EVERY certificate-bearing role with measured coverage — the row
  would close CONVERGED-on-incumbent-value-with-derivations (the
  program is how we'd know; either branch closes the row).

### 4.6 C43
- Proposed: row note append only — "wave-3 FAM panel CONFIRM-ALIGNMENT
  PASS 2026-08-20: content identity, row state, and residue chain
  (C43 -> F2-C11-ESTIMATOR-CAMPAIGN leg (a) -> C42 role-1) verified
  three-legged; no further action; residue owner unchanged." No
  status change (MIXED stands). No duty minted (the measured half is
  C11's, of record).

### 4.7 Escalation candidates
NONE. No row leaves this panel unsettled; every measured half has a
named owner window that pre-existed this panel (zero new machinery —
LOAD-CLASS honored).

### 4.8 Candidate new rows
NONE (dedup-verified this window: duty-name greps F2-C34/35/36/41/42,
KRICH-ROLE, BAND-POLICY, TRFLOOR-DERIVE, XTOL over choice_ledger/
findings/claims/glossary = zero hits; every proposed duty lands
INSIDE an existing findings-row owner window or conditional row —
conditional:P-TRFLOOR, variational-driver:cross-unit-and-slack-
tolerances, driver-nonsmooth:jacobi-scaling-frozen, thermo-bands:
band-composition-no-declared-rule, the R25/AC5 audit row,
mesh-amr:observed-order-not-at-band-sites).

## 5. PAPERS NEEDED (procurement channel; §0-bis(c))
1. Moré & Wild, "Estimating computational noise", SIAM J. Sci.
   Comput. 33(3), 2011 (ECNoise) — needed at [FULL] for the
   C34/C35 epsilon_J measurement protocol arm (ray-probe design +
   the unbiasedness check O-F25/P8 presumes); the pins above are
   executable with the tol_dp pessimistic bound meanwhile (declared).
2. ASME V&V 20-2009 (R2016), the standard text (u_val composition
   §§ on correlated components) — needed at [FULL] to upgrade the
   C41 P1/P2 correlation-argument wording from overview-level [ABS]
   to standard-level; policy above is executable without it
   (conservative direction declared).
3. Xing & Stern 2010, ASME JFE 132:061403 (+2011 closure) — open
   mirrors located (DTIC ADA498086; UFPR); low-cost ask, needed at
   [FULL] only when C42 role-1 audit executes (second derivation
   route cross-check against Eca-Hoekstra).
4. Sun & Nocedal 2023 (arXiv:2201.00973, open) — self-procurable at
   [FULL] from arXiv within env pins at the C34 trigger window; ask
   recorded so the trigger consumes it deliberately, not from [ABS].

## 6. MACHINE SUMMARY

```yaml
cluster: FAM
rows:
  C34: {proposed: "ADJUDICATED-SPLIT (noise-derived floor direction; [P-TRFLOOR] blocked-with-named-cause unchanged, protocol pinned)", gated: true, duty: "F2-C34-TRFLOOR-DERIVE (= [P-TRFLOOR] at trigger)"}
  C35: {proposed: "ADJUDICATED-SPLIT (xtol_u = K_RICH x floor_W/median(Dv); prose found = REFUTATION of incumbent label; literal -> declared-slack)", gated: true, duty: "F2-C35-XTOL-DERIVE (rides findings :633 owner window)"}
  C36: {proposed: "CONVERGED-panel (per-segment Dv refresh + constraint-row equilibration; H^s metric = option-with-stated-precondition)", gated: true, duty: "F2-C36-DVREFRESH (= [P-DVREFRESH] at trigger)"}
  C41: {proposed: "CONVERGED-panel (declared P1-P4 composition policy, sufficient-not-optimized; max needs >= K_RICH dominance certificate)", gated: true, duty: "F2-C41-BAND-POLICY (= findings band-composition owner window)"}
  C42: {proposed: "ADJUDICATED-SPLIT (per-role derivation program, ordered; interim K=4 conservativeness hypothesis declared; role census corrected 8 -> 10+2 measured)", gated: true, duty: "F2-C42-KRICH-ROLE-AUDIT (ordered after F2-C11-ESTIMATOR-CAMPAIGN leg (a))"}
  C43: {proposed: "CONFIRM-ALIGNMENT PASS (three-legged verification vs VERDICT_wave1 par.4.5; note-append only, MIXED stands)", gated: false, duty: null}
census_recency: "1981-2026; newest included 2023-2025 (Sun-Nocedal MP 2023, Cao-Berahas-Scheinberg MP 2023, arXiv 2411.02665/2405.11400 2024, Optim.Eng. 2026 noisy-nonsmooth TR); 6 queries, table par.2.1"
alternatives_closed: 14
rows_adjudicated: 6
deltas_proposed: 6   # C34/C35/C36/C41/C42 status+note, C43 note-append
escalation_candidates: 0
papers_needed: 4
candidate_new_rows: 0   # dedup-verified by measured grep (par.4.8)
inflation_check: done   # every census claim carries [FULL]/[ABS]/[TITLE]/registry-row depth; no claim above depth held
sr12_counts: "K_RICH .py sites 107/17 files; xtol=1e-10 7 call sites + 1 assignment; duty-name dedup greps 0 hits — all commands run in this window"
```
