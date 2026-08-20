# PANEL_REMENG — ENGINE/DRIVER REMAINDER (C16, C19, C22, C37, C39, C40, C44, C45)

S-FOUNDATIONS-C3 WAVE 3, slot REMENG. Census validity stamp: 2026-08-20.
Frame consumed: BRIEF_wave3_panels.md (§0 + §REMENG + shared blocks) +
BRIEF_wave1_panels.md §0 FRAME + BRIEF_wave2_panels.md §0-bis/§0-ter, all
read in full this window. Authorities consumed, not re-litigated:
VERDICT_wave1.md, VERDICT_wave2.md (§2.1/§2.2/§4.1/§4.2/§4.10/§4.11 read
this window). Row authority: docs/choice_ledger.yaml rows C16 :296-305,
C19 :328-336, C22 :362-370, C37 :519-528, C39 :541-550, C40 :552-560,
C44 :595-604, C45 :606-615 (read in full, wave notes consumed).
No registry/doc of record edited; every delta below is PROPOSED for the
landing window.

---

## 1. FROZEN FORMAL STATEMENT + PRE-REGISTERED DECISION CRITERIA

Shared sub-problem (frozen before search): the certified optimize-loop's
inner mechanics. Context of record: marched axisymmetric Euler solver
with fitted fronts; per-column implicit Newton cell solves certified
against DERIVED floors (C18 constants, GAP-29 factor-2 cliff of record);
driver = segmented TR loop (RK-G P2: any (N,Nv) flip ends segment) on
scipy trust-constr, engine retained AS-IS under the wave-2
INFORMATION-ONLY multiplier discipline until [P-IPADJ]
(VERDICT_wave2 §2.1/§4.1); curvature = fresh-FD-per-segment interim with
[P-QNCARRY]/[P-HESSREJ] duties (§2.2/§4.2); JAX/custom_vjp stack, M5c
compiled executor of record (wall_search decisions bitwise inside the
compiled path). Every REMENG row sits BELOW the engine-level wave-1/2
adjudications and must COMPOSE with them.

Per-row single main question + what would make each option win
(frozen BEFORE the census; no mid-census amendments were needed):

- **C16 (damping ladder).** Q: what damping policy globalizes the march
  Newton solves so that robustness rests on measured contraction rather
  than an unexplained fixed ladder? WIN criteria: incumbent wins if the
  ladder is demonstrably inactive above program noise on record
  instances (materiality) or ties the challenger at identical certified
  outcomes; Deuflhard-class adaptive damping wins if, on
  activation-bearing instances, it reduces eval count or failure rate at
  identical certified outcomes; Armijo wins only if the residual-based
  test is provably adequate on our conditioning (it must survive the
  ill-conditioned-Jacobian objection).
- **C19 (cert metric scale).** Q: what scale makes the certified floor
  statement invariant to component-magnitude disparity in z? WIN:
  componentwise wins iff measured disparity across the record corpus is
  large enough to move a certificate verdict (>= the GAP-29 factor-2
  headroom scale); scalar incumbent wins otherwise on cost/simplicity
  (AUDIT F8 LOW = standing materiality input).
- **C22 (wall-foot search).** Q: what search policy locates the wall
  foot so the decision-flip rate (which sets the re-record rate) drops
  without weakening the cell certificate? WIN: alternative
  (bracketed continuous-parameter root + orientation pre-filter) wins if
  the monotone-foot predicate can be falsified (doctored probe) or the
  measured flip-rate delta is material; incumbent wins if the predicate
  survives the probe family and the rate delta is below the derived
  band (it is already compiled and bitwise-verified).
- **C37 (segmentation trigger).** Q: when must an (N,Nv) flip END the
  RK-G segment vs be absorbed, without breaking replay-fidelity
  (constraint 7)? WIN: incumbent (any-flip-ends) wins as certified-safe
  default unless a merge can be shown replay-bit-identical with
  certificate deltas inside a derived band AND the measured benign-flip
  fraction makes the lever material; PC^1 anticipation wins only as an
  instrument of that same band, never as a standalone policy.
- **C39 (multiplier verification half).** Q: what instruments verify
  that consumed multipliers are the true KKT prices, given
  INFORMATION-ONLY discipline until [P-IPADJ]? WIN: an instrument enters
  the stack iff it is cheap, catches a failure mode the others miss,
  and VERIFIES without CONSUMING res.v as certified. (Convention half
  CONVERGED T1 — not re-opened here.)
- **C40 (lip equality).** Q: LinearConstraint row vs variable
  elimination — what does the choice do to multiplier provenance and
  conditioning? WIN: elimination wins iff it is the enabling mechanism
  for verified lambda_e (C39 instrument (d)) or a measured conditioning
  effect exists; incumbent wins on materiality otherwise (findings row
  severity LOW, "no record impact").
- **C44 (FD steps).** Q: what step policy keeps FD columns valid near
  seams and above the measured noise floor? WIN: noise-aware per-column
  steps win iff the incumbent's derived-for-smooth steps fall outside
  the Moré-Wild near-optimal band on measured noise; seam handling wins
  as a VERIFICATION battery (ramp/complex-step cross-checks), not as a
  new stencil scheme, unless the ramp falsifier fires.
- **C45 (leggeAree bracket).** Q: does the hardcoded 400-point
  [1.01, 2.8]*as bracket cover all admissible cases, at what cost?
  WIN: box-derived window wins iff bracket coverage is not provable
  from the admissible box; vectorization is a speed conditional only
  (H2 of record), never a correctness verdict. GAP-ACCOUNTING row —
  LOAD-CLASS VALVE (brief §0(i)) applies.

MATERIALITY (pre-registered, per §0-ter(c)): C19, C40, C45 are
presumptively at-or-below the program noise floor (AUDIT F8 LOW;
findings "no record impact"; single scalar root solve) — decided on
cost/simplicity with cheap rejectors unless a falsifier fires. C16 is
material on the robustness/rate axis only (certificates consume final
residual vs floor, not the damping path). C22/C37 are material through
the re-record rate (the churn axis, measured of record). C39/C44 are
material through verdict integrity (multiplier-consuming quantities;
Hessian attribution at outcome-II).

---

## 2. SOTA CENSUS

### 2.1 Query protocol table (all searches 2026-08-20, WebSearch, US index)

| # | Verbatim query | Hits | Screened | Included |
|---|---|---|---|---|
| Q1 | adaptive damping Newton method globalization affine invariant natural monotonicity recent 2023 2024 | 9 | 9 | 3 |
| Q2 | ITP method root finding bracketing superlinear Brent Chandrupatla comparison | 9 | 9 | 4 |
| Q3 | adaptive finite difference interval estimation noise Shi Nocedal derivative-free 2022 | 7 | 7 | 1 |
| Q4 | parametric nonlinear programming active-set change prediction sensitivity path-following warm start segmentation | 9 | 9 | 4 |
| Q5 | Lagrange multiplier least-squares estimate verification complementarity residual termination Wächter Biegler shadow price consistency check | 9 | 9 | 2 |
| Q6 | componentwise scaling convergence test nonlinear solver termination "scaled norm" Deuflhard NLEQ diagonal scaling condition | 7 | 7 | 2 |

No web query for C40 and C45 — stated reason: C40 is settled textbook
territory with the canonical source ON DISK and read [FULL] this window
(N-W §15.3); C45 is a gap-accounting row under the LOAD-CLASS VALVE
whose alternatives are in-house objects (box derivation, vectorization)
with the speed-audit measurement already of record. Russian classical
school: not classical-adjacent territory for these eight rows (loop
micro-policies, post-1970 numerics) — closed by stated reason.

### 2.2 On-disk full-text reads (new papers, brief §0(ii))

- **Deuflhard CSM 35 (2011)**, literature/deuflhard_2011_newton_methods_
  affine_invariance_csm35.pdf — **[FULL] read this window: §3.3 pp.
  134-148** (error-oriented descent; natural level function; natural
  monotonicity test ||Dx-bar^{k+1}|| <= ||Dx^k||; theoretically optimal
  damping lambda_k = min(1, 1/h_k) with h_k = omega_k ||Dx^k|| (3.43);
  computational a-posteriori correction estimate [h_k] from ONE trial
  value (3.48) and prediction estimate (3.49) — both MEASURED
  in-iteration, no asserted constants; bit-counting Lemma 3.16 (the
  estimate need only catch the leading binary digit of h_k); residual
  monotonicity FAILS on ill-conditioned Jacobians (3.40) — the Armijo
  objection; algorithm NLEQ-ERR with XTOL termination
  ||Dx-bar^{k+1}|| <= XTOL and scaled smooth norms ||D^{-1}.||_2 with
  the diagonal scaling ADAPTED iteratively).
- **Nocedal-Wright 2ed**, literature/nocedal_wright_2006_numerical_
  optimization_2ed.pdf — **[FULL] read this window: §15.3 pp. 427-430**
  (nonlinear elimination dangerous — Fletcher example; SIMPLE
  elimination via linear constraints safe and exactly equivalent
  (15.9)-(15.10); basis-conditioning caveat — trivial for a single
  equality row where B is 1x1).

### 2.3 Census entries (per-source one-liners, depth-marked)

Damping/globalization (C16): Deuflhard CSM 35 [FULL] (above) = the
measured-contraction alternative of record. Modern lines: AICN
self-concordant adaptive damped Newton, arXiv:2210.17107 [ABS]; damped
Newton with global O(1/k^2), NeurIPS 2022 [TITLE]; "The Grand Four:
affine invariant globalizations of Newton's method" (Deuflhard, 2018)
[TITLE] — all optimization-context or survey; none displaces the
affine-covariant strategy for small algebraic root solves. Field
settled at Deuflhard-class for exact Newton on nonlinear systems.

Scaling (C19): Deuflhard NLEQ scaled norms with iteratively adapted
diagonal D [FULL] (§2.2); production-PDE practice: COMSOL stationary
solver and Sandia Aria expose exactly the incumbent's form
(corrections scaled by max(1, |max solution|), DOF_AMAX class) [ABS] —
the incumbent is not an outlier, it is one of the two standard forms.

1-D bracketed root solving (C22, C45): Brent 1973 [ABS,
wikipedia/handwiki summaries]; Chandrupatla 1997 (simpler/faster on
flat roots) [ABS]; **ITP (Oliveira-Takahashi, ACM TOMS 2020)** [ABS] —
first bracketing method with secant-class superlinear rate AND optimal
worst case; SciML NonlinearSolve.jl ships it as a production bracketed
solver [ABS]. Modern family closed: for a certified loop the choice
among Brent/Chandrupatla/ITP is IMMATERIAL at our granularity (all
bracketed = the certificate-relevant property; rate differences below
program noise) — decided on cost: no new dependency (env PINNED),
hand-rolled bracketed step or scipy brentq in-env.

Parametric active-set / segmentation (C37): qpOASES online active-set
(Ferreau et al) [ABS]; NMPC path-following tracks solutions across
active-set changes without locating the exact change points
(Diehl-Ferreau-Haverbeke overview) [ABS]; predictor-corrector
path-following for dual-degenerate parametric NLP [TITLE]; GNN/ML
warm-start of active-set solvers, arXiv:2511.13174 [TITLE] — modern
line exists, out of scope (no certificate semantics). Supports PC^1
anticipation as genuine practice, but none of it carries a
replay-fidelity certificate — our constraint 7 is stricter than the
field's.

Multiplier verification (C39): LSQ multiplier estimation with
complementarity-slackness structure (Gill-Murray-Wright lineage;
recent exposition arXiv:2606.07984 [ABS]); pathological Lagrange
multiplier behavior in infeasible interior-point methods,
arXiv:1707.07327 [ABS] — direct modern support for
verify-before-consume on an IP path; Wächter-Biegler 2006 three-part
termination [ABS, already the findings-row prescription of record].
Tree instruments: O-F18 exchange-multiplier ≈ binding-measure density +
P-F26 marginal-value audit (diff :195-198, cited not regenerated).

FD steps (C44): Moré-Wild computational-noise line (ECnoise 2011;
derivative estimates 2012) [ABS]; **Shi-Xie-Xuan-Nocedal, SISC 2022**
(arXiv:2110.06380) [ABS] — adaptive FD-interval by bisection balancing
truncation vs measurement error, no higher-derivative estimates = the
modern default; complex-step (Squire-Trapp/Martins) — precondition
below; kink/seam obligations = tree battery O-F22/V-F29 (diff
:212-218, cited).

Cava sweep (brief §0(iv)): measured grep of
validation/ADVISORY_litreview_confrontation_2026-08-13.md for
damping|brent|finite.difference|multiplier|complementarity|elimination|
bracket = 1 hit (line 153, Giles-Pierce "adjoint variables are
Lagrange multipliers") — background for C39's semantics, not
adjudication-bearing for the verification instruments. No cava row
bears on these eight rows.

### 2.4 Corpus recency

Span 1973-2026. Core modern items: ITP 2020, Shi et al SISC 2022,
AICN 2022-2023, qpOASES-lineage + NMPC path-following 2014-2020,
GNN warm-start 2025 [TITLE], LSQ-multiplier exposition 2026 [ABS].
Classics: Brent 1973, Chandrupatla 1997, Gill-Murray-Wright 1981,
N-W 2006 [FULL §15.3], Deuflhard 2011 [FULL §3.3], Wächter-Biegler
2006. The census reaches the active lines on every axis where an
active line exists; C19/C40/C45 territories are settled and declared
so.

### 2.5 Per-row §0-bis axis bearing (one sentence each; no padding)

- Axis (1) engine query-level: bears on **C39** (multiplier meaning is
  engine-dependent — consumed via VERDICT_wave2 §2.1 INFORMATION-ONLY +
  [P-IPADJ] ordering) and weakly on **C40** (either handling is
  engine-portable); does not bear on C16/C19/C22/C37/C44/C45 (below
  engine level or engine-independent policies).
- Axis (2) discrete vs continuous adjoint: bears on **C44** (FD steps
  exist only on the FD tier beside the AD-adjoint; the comparison
  discipline pins ONE lowering per the cross-lowering row, cited) and
  on **C39** (the adjoint IS the multiplier field — cava :153 — but the
  verification instruments are discrete-side); does not bear on the
  others.
- Axis (3) moving-mesh/r-adaptive: does not bear on any REMENG row
  (inner loop mechanics; the fitted-front geometry is the given), with
  the single named seam that C22's foot search operates ON the fitted
  geometry (owned by C12/C13/C5 territory, not decided here).
- Axis (4) adjoint-free routes: does not bear — quarantined to
  exploration by wave-2 C31 (cited), and no REMENG row is an optimizer
  choice.
- Axis (5) emergent: **JAX traceability** (fixed trip-count loops
  compile; data-dependent-iteration Brent-style loops sit badly in the
  compiled executor) — named and CLOSED inside the C22/C16 protocol
  pins below (challenger builds must present a compiled-path-compatible
  form or run on the referee tier); this is existing C48/engine
  territory, no new row (dedup: measured grep, §6).

---

## 3. ADJUDICATION (per row)

### 3.1 C16 — Newton damping ladder

Incumbent (genuine case): fixed trial ladder TRIALS = (1.0, 0.5, 0.25,
0.0625, 0.015625, 0.0) with bare argmin non-increase,
validation/a1_ideal_march_jax.py:419-424. It is simple, branch-free,
compiles into the M5c executor with a FIXED trip count (axis-(5)
advantage), and the cell certificate consumes the FINAL residual vs the
derived floor — the damping path never enters the certified statement.
No recorded rationale (annex verbatim); trees SILENT at ladder
granularity, but O-F25/V-F31 (diff :96-98) mandate the derivation-duty
standard for every constant.

Challenger at its best (Deuflhard [FULL]): natural monotonicity test
with a-posteriori correction (3.48) and prediction (3.49) estimates —
every damping factor MEASURED from in-iteration quantities; Lemma 3.16
shows leading-binary-digit accuracy suffices. Two content points
against the incumbent's accept rule: (i) argmin non-increase on the
RESIDUAL is the residual-monotonicity criterion, which Deuflhard proves
practically inadequate for ill-conditioned Jacobians (3.40) — and
"conditioning IS the convergence rate on this driver" is an S18 finding
of record (findings row driver-nonsmooth:jacobi-scaling-frozen); (ii)
the trailing 0.0 candidate makes "accept-no-step" a silent outcome that
only the trip cap (C17, FAM-adjacent, not decided here) eventually
converts into a refusal.

Armijo closed by stated reason at its best: it is a residual-based
sufficient-decrease rule — strictly dominated by the natural-monotonicity
family on the ill-conditioning axis (Deuflhard (3.40), [FULL]) and adds
nothing the ladder lacks structurally.

Cross-link discipline honored (brief): the wave-2 C21 verdict retired
the asserted O(h) predictor to measured-or-deleted — the challenger
adopted here asserts NO contraction constant: (3.48)/(3.49) are
measured per-iteration estimates. No resurrection.

Materiality (honest, both directions): the certified statement is
damping-invariant; the fork is material only through robustness/rate
(ladder activations force extra implicit solves; failures force
re-records). Whether it is material ABOVE program noise is exactly a
measured question — so the row splits.

**Outcome: measurement-gated SPLIT.** Incumbent retained interim
(compiled, gate-verified); Deuflhard natural-monotonicity damping =
pinned challenger. Protocol + falsifiers in §4.1.

### 3.2 C19 — certification metric scale

Incumbent: sc = max(1, max|z|), a1_ideal_march_jax.py:446 and :812.
Census: this is the DOF_AMAX form used by production PDE solvers
(COMSOL/Aria [ABS]); the alternative (componentwise adapted diagonal,
Deuflhard [FULL] p.148; Higham) is the other standard form. Trees
PARTIAL (H-F23 monitor-list doctrine; the specific fork unaddressed,
diff :104-105). AUDIT F8 adjudicated LOW = the standing materiality
input; no panel has found a record instance where the scalar scale
moved a verdict.

Steelman for componentwise: if z components span decades, a scalar
scale hides small-component floor violations (certificate laxity on the
small component). Against: our cell states are low-dimensional with
components of comparable magnitude on record instances (F8 LOW), and a
laxity that never exceeds the GAP-29 factor-2 cliff headroom cannot
flip a verdict.

**Outcome: CONVERGED-ON-COST (incumbent retained), DECLARED IMMATERIAL
pending one cheap measured census** — a disparity census with a
rejector, not a rebuild (LOAD-CLASS VALVE; sufficient-not-optimized).
Protocol in §4.2.

### 3.3 C22 — wall-foot search

Incumbent (genuine case): linear index scan + full Newton per attempt +
monotone-foot predicate; M5c consumed the COST side of record
(wall_search decisions bitwise inside the compiled executor — ledger
note). The RATE side and the PREDICATE are the open halves: findings
row cell-cert:wall-foot-search-fragile (GAP-28) — decision flips SET
the re-record rate (n_rec ~ n_segments); wrong-foot silent acceptance
under a non-monotone spline PLAUSIBLE, unmeasured; Q5 folded = the
doctored two-close-knots probe vs a Brent-bracketed reference decides.

Alternative at its best: bracketed root on the continuous chord
parameter (+ Shewchuk-class orientation pre-filter) -> derived (N,Nv),
ONE implicit solve at the bracketed foot (findings owner text, cited).
Census adds: the bracketing property is the certificate-relevant
content (guaranteed enclosure); the specific engine
(Brent/Chandrupatla/ITP) is immaterial at our granularity — declared,
decided on cost (no new dependency; env PINNED).

Axis-(5) seam (named): a data-dependent-iteration bracketed loop does
not sit in the compiled executor as-is; the challenger therefore runs
first as the REFEREE (probe tier), and any production adoption must
present a fixed-trip-count or host-side form — this is C48/engine
territory, constraint honored in the pins, not adjudicated here.

Speed-audit numbers cited, never re-measured (brief): H2 measured
>=1.86x whole-record from _foot alone (fallback branch, dormant —
targets MET per S25-bis).

**Outcome: measurement-gated SPLIT, burden on the INCUMBENT'S
PREDICATE** (an unproven hypothesis inside a certified loop is the
defect; the scan itself is fine). The Q5-folded probe is the decider.
Protocol in §4.3.

### 3.4 C37 — segmentation trigger (the N6 panel, right-sized instance)

DECLARED: this adjudication IS the speed-audit N6 panel's right-sized
instance (brief §REMENG; findings row
driver-nonsmooth:flip-segmentation-materiality routes any materiality
instrument through "that panel's own instrument" — this panel).
[P-FLIPMAT] was DE-REGISTERED as not licensable without the N6 panel;
what follows is its licensed re-entry path.

Incumbent (genuine case): any (N,Nv) flip ends the segment. It is
certified-SAFE by construction: curvature is never carried across a
decision boundary, so constraint 7 (replay fidelity) cannot be violated
by policy. Cost of record: a flip fires at almost every accepted step
on the mild S18 walk — record-scale cost per productive step; a
lipward-only flip discards a Hessian exactly valid for every dof but
the lip (findings magnitude text, cited). Speed audit N6: "needs its
own panel. Flagged, never traded" (ADVISORY_engine_speed_audit par.4
N6, cited, not re-measured).

Alternatives: (a) materiality-gate by replay-fidelity band; (b) PC^1
active-set anticipation. Formal frame adopted from the trees
(ENRICHING, diff :186-190): O-F19 regime-cell doctrine — activity
changes are certified-class boundaries, logged as (S,xi) stratification
loci (H-F11). Under that frame the question is exact: which boundary
crossings change the certified class MATERIALLY (beyond a derived
replay-fidelity band) vs benign relabelings.

Census: parametric path-following crosses active-set changes without
locating them exactly [ABS] and online active-set methods warm-start
across changes [ABS] — the merge family is genuine modern practice —
but none of it carries our replay-fidelity certificate; the field's
practice cannot be imported without the band+rejector. PC^1
anticipation closed by stated reason at its best (path-following
predictor-corrector [ABS/TITLE]): it improves PREDICTION, not
certificate semantics; it re-enters only as an instrument computing the
same materiality data (O-F19 loci give it its logging home).

Wave-2 composition pin (binding, cited): [P-QNCARRY]'s arm-B
invalidates flip-touched columns and rejects cross-lowering pairs
(VERDICT_wave2 §4.2) — any merge policy must PRESERVE that
invalidation semantics (a merged segment does not resurrect
flip-touched curvature).

**Outcome: CONVERGED-ON-DEFAULT + measurement-gated lever.** Incumbent
stays the default of record (certified-safe); the merge lever is
licensed ONLY behind the derived band + bitwise rejector + measured
benign-fraction materiality, on the first post-8761dce campaign
artifact (the trigger already named of record). Protocol in §4.4.

### 3.5 C39 — multiplier provenance (verification half only)

The convention half (res.v reading, S24-T1) is CONVERGED of record —
not re-opened. Standing constraint CONSUMED (brief): wave-2 C31
INFORMATION-ONLY multiplier discipline until [P-IPADJ]
(VERDICT_wave2 §2.1/§4.1) — res.v is not certified-consumable today;
the verification instruments below are exactly the promotion path.

Instrument stack, each at its best and each catching a distinct
failure mode (this is an instrument ADJUDICATION, not a measurement
question — the instruments are cheap and complementary, so the stack
converges NOW; only their EXECUTION is F2):

1. **Complementarity band + except-pass counter** (findings row
   constraints:multiplier-rejector-missing, GAP-12, owner text cited):
   catches barrier/inactive-constraint artifacts; the S24 step-13d
   |mu*m| = 3.55e3 by-hand catch becomes the retro-fixture the band
   must fire on. Wächter-Biegler three-part termination [ABS] is the
   canonical form.
2. **Marginal-value audit** (P-F26, diff :195-198, cited): FD dJ/dc vs
   multiplier at a margin-active checkpoint — catches wrong-scale and
   wrong-sign provenance; the O-F18 exchange-density reading gives the
   SIP-side semantics the audit tests against.
3. **LSQ re-estimate referee** (Gill-Murray-Wright lineage;
   arXiv:2606.07984 [ABS] modern exposition): recomputes multipliers
   from recorded gradients independent of solver internals — catches
   solver-internal pathologies; census support: multipliers in
   infeasible IP methods can behave pathologically (arXiv:1707.07327
   [ABS]) — direct modern justification for a solver-independent
   referee on an IP path.
4. **Fiacco AD post-optimality via lip elimination** — deferred INTO
   the C40 outcome (§3.6): it is the exact-provenance mechanism for
   lambda_e specifically; adopted only if/when C40's elimination lands.

Ordering pin: instruments 1-3 land WITH [P-IPADJ] (the first F2 engine
act, wave-2 of record) — the source adjudication of what `optimality`
and res.v measure on the IP path is prerequisite to interpreting any
band on them.

**Outcome: CONVERGED-ON-INSTRUMENTS (stack 1-3 + ordering pin);
measured half = F2 duty.** Status stays MIXED until the instruments
run. Protocol in §4.5.

### 3.6 C40 — lip equality handling

Incumbent: LinearConstraint row (a1_toc_variational_jax.py:1746-1749
per findings row constraints:lip-equality-not-eliminated, GAP-32,
severity LOW, "no record impact"). N-W §15.3 [FULL]: simple elimination
via a linear constraint is safe and exactly equivalent; the
basis-conditioning caveat is trivial for one row (B is 1x1). Trees
SILENT (diff :199) — the census carries the row alone.

Content: the only load-bearing payoff of elimination is that it makes
lambda_e EXACTLY recoverable by AD post-optimality with an O3.1-style
check (findings owner text) — i.e., it is C39's instrument (4). The
per-iteration normal-step saving is below the program noise floor
(declared immaterial; findings severity LOW).

**Outcome: GAP-ACCOUNTING, LOAD-CLASS VALVE — CONVERGED-CONDITIONAL.**
Elimination is adopted-as-direction ONLY as the C39 lambda_e-provenance
mechanism, executed in the same F2 window IF the C39 stack (1-3) leaves
lambda_e unverified; if the stack verifies lambda_e within bands
without it, C40 CLOSES on the incumbent by materiality. Sufficient
trivially-checkable hypothesis declared: one linear equality row, full
row rank trivially, exact equivalence by N-W (15.9)-(15.10) [FULL].
No separate duty (folded into F2-C39-MULTVER — anti-entropy). Protocol
in §4.6.

### 3.7 C44 — FD steps (gradient/Hessian)

Incumbent (genuine case): sqrt(eps)*scale and eps^(1/3)*scale ARE the
textbook-derived optima for smooth noise-free doubles (N-W §8.1 error
model — the same model [P-HESSREJ] already cites in its findings owner
text); "derived-for-smooth" is a real derivation on its own axis. The
open axes: (i) NOISE — the march output carries a measured noise floor
(the C18/GAP-29 territory), and the optimal step scales with it; (ii)
SEAMS — an FD step straddling a knot/plan seam makes a column O(1)
wrong (findings row driver-nonsmooth:hessian-no-rejector, GAP-16).

Alternatives at their best: **Moré-Wild noise-aware per-column steps**,
modern instance = Shi-Xie-Xuan-Nocedal SISC 2022 [ABS] (bisection
balancing truncation vs measurement error, no higher-derivative
estimates — cheap, per-column, exactly our shape); **seam-aware
stencils** — but the trees' enrichment (diff :212-218, cited) reframes
the seam axis as a VERIFICATION battery, not a new stencil scheme:
V-F29 (verify AT a fitted front and AT an active g_sep phase) + O-F22
(Taylor-remainder ramp with measured slope over a derived decade;
complex-step on the fitted/analytic tier). Right-sized adoption:
battery over stencils.

Complex-step recorded as OPTION-WITH-STATED-PRECONDITION (brief
mandate): usable on the analytic/twin tier ONLY — the repo already
operates a numpy-complex twin with h=1e-20 as an audit instrument
(claims registry O3.1-cs row, cited by measured grep §6); through the
JAX custom_vjp engine path it is NOT established and is not asserted
here.

Seam-of-record named (brief mandate, not double-adjudicated): the
noise-floor measurement that the Moré-Wild step consumes IS the same
measured object as the C18/C34/C35 floor-constant derivation window
(FAM slot) — ONE derivation window; C44's duty rides it, never forks
it. [P-HESSREJ] is already UNCONDITIONAL (VERDICT_wave2 §2.2) and
carries the seam-defect distribution instrument — no duplication.

**Outcome: measurement-gated SPLIT.** Incumbent retained interim
(genuinely derived on its axis); noise-aware per-column steps = pinned
challenger riding the C18 window; seam axis = the O-F22/V-F29 battery
under [P-HESSREJ]. Protocol in §4.7.

### 3.8 C45 — leggeAree bracket

Incumbent: hardcoded 400-point grid qs = linspace(1.01*as, 2.8*as, 400)
(a1_ideal_march_jax.py:868). GAP-ACCOUNTING row; LOAD-CLASS VALVE
applied as mandated.

Correctness half: the bracket bounds are a HIDDEN HYPOTHESIS (the
supersonic root q_e/as in [1.01, 2.8] for every admissible case). The
sufficient-not-optimized closure: derive the window once from the
admissible envelope box (the H-F6 reachable-set object — C25's
territory, NAMED not decided, CONV slot) OR, cheaper and trivially
checkable, add an ENDPOINT REJECTOR (root at either grid boundary =>
REFUSE loudly). The rejector alone converts the hidden hypothesis into
a monitored one — sufficient, declared as such.

Speed half: vectorization measured 444x on its block of record (H2 =
the leggeAree bracket-scan per the ledger note citing
s24_gapv_cell-cert.md:191; bitwise identity FALSIFIED at 1.46e-11 of
record, so it rides an X-SCANM-grade gate). That is measurement
evidence, not a verdict (brief) — and the speed program's targets are
MET of record (S25-bis), so the lever is DORMANT: named conditional,
trigger = measured shortfall, exactly the H2 fallback discipline
already of record. Weighed: no adoption now, no re-measure.

**Outcome: CONVERGED-WITH-VALVE.** Endpoint rejector + derived-window
derivation = one cheap F2 hygiene item; vectorization stays the
dormant H2 conditional. Protocol in §4.8.

---

## 4. PROPOSED VERDICTS + DUTIES (deltas PROPOSED; landing window executes)

### 4.1 C16 (choice_ledger :296-305)
- status: NEVER -> "ADJUDICATED-SPLIT (direction converged 2026-08-20
  wave-3; damping A/B = measured F2 duty)".
- Proposed note delta: incumbent ladder retained interim
  (compiled-path, fixed trip count); challenger = Deuflhard
  natural-monotonicity damping with measured per-iteration estimates
  (CSM 35 §3.3 (3.48)/(3.49), read [FULL] 2026-08-20) — NO asserted
  contraction constants (C21 wave-2 discipline honored). Armijo closed
  (residual-monotonicity inadequacy on ill-conditioned Jacobians,
  Deuflhard (3.40)).
- Falsifiers pinned: **F-C16-1** (materiality gate): ladder-activation
  census on the record corpus (activations + accepted lambda<1 + 0.0
  accepts, logged per record); if activation share is below the derived
  noise-floor threshold, C16 CLOSES on incumbent-by-materiality.
  **F-C16-2**: on activation-bearing instances, the challenger must
  reduce implicit-solve count or failure rate at IDENTICAL certified
  outcomes; else incumbent retained converged. **F-C16-3** (rejector on
  the incumbent's accept rule): any accept where the natural
  monotonicity test REJECTS (||Dx-bar|| > ||Dx||) while argmin
  non-increase accepts = accept-rule defect of record.
- BINDING F2 duty: **F2-C16-DAMPAB** (census first — F-C16-1 may close
  the row for free; challenger build only if material). LOAD-CLASS
  note: derivation-duty bookkeeping, sufficient-not-optimized.
- Dependencies: C17/C18 constants (FAM window — trip cap and floors
  interact with 0.0-accept semantics; named, not decided).
- What would overturn: F-C16-1 below threshold (closes on incumbent);
  F-C16-2 failure (closes on incumbent); F-C16-3 firing (forces
  challenger regardless of cost).

### 4.2 C19 (:328-336)
- status: SINGLE-AUTHOR -> "ADJUDICATED-ON-COST (immaterial-declared
  2026-08-20 wave-3; disparity census = cheap monitored hypothesis)".
- Proposed note delta: scalar sc = max(1, max|z|) retained — one of the
  two standard production forms (COMSOL/Aria DOF_AMAX class [ABS];
  componentwise = Deuflhard NLEQ adapted-diagonal [FULL]); AUDIT F8 LOW
  consumed as materiality input; immateriality is DECLARED, monitored,
  not proven.
- Falsifier pinned: **F-C19-1**: per-record component-scale disparity
  census (max_i scale_i / min_i scale_i on z at certification points);
  if disparity exceeds the derived threshold (tied to the GAP-29
  factor-2 headroom scale — the smallest laxity that could flip a
  verdict), componentwise scaling RE-OPENS with burden inverted.
- F2 duty: **F2-C19-SCALECENSUS** — one logging row inside the AUDIT F8
  owner window (F2 hygiene); no rebuild.
- Dependencies: C18 window (threshold derivation source; named seam).
- What would overturn: F-C19-1 firing.

### 4.3 C22 (:362-370)
- status: NEVER -> "ADJUDICATED-SPLIT (burden on the incumbent's
  monotone-foot predicate 2026-08-20 wave-3; probe = measured F2
  duty)".
- Proposed note delta: M5c cost-side consumption respected (of record,
  cited never re-measured); the open halves = predicate validity + flip
  rate at source; challenger = bracketed continuous-chord root +
  orientation pre-filter -> derived (N,Nv), one implicit solve
  (findings GAP-28 owner text, cited); bracketed-engine choice
  (Brent/Chandrupatla/ITP) DECLARED IMMATERIAL, cost decides, env
  PINNED (no new dependency); challenger runs referee-tier first
  (compiled-path constraint named, C48 territory).
- Falsifiers pinned: **F-C22-1** (the Q5-folded decider, findings row
  verbatim): doctored two-close-knots probe — incumbent scan vs
  bracketed reference; ANY (N,Nv) disagreement = monotone-foot
  predicate FALSIFIED, challenger becomes the certificate-bearing
  reference (incumbent may stay as accelerator behind a
  agreement-gate). **F-C22-2**: probe-family agreement across the
  record corpus + a derived probe family (knot-spacing swept to the
  refinement floor) = predicate survives; C22 closes on incumbent with
  the predicate PROVEN-ON-FAMILY, flip-rate lever handed to C37's
  band. **F-C22-3** (rate): measured n_rec delta between policies on
  one campaign artifact below derived band = rate lever DEAD.
- BINDING F2 duty: **F2-C22-FOOTPROBE** (cheap: probe + referee, no
  engine surgery).
- Dependencies: C37 (same churn object attacked from materiality side —
  findings owner text names the coupling); C5/C12/C13 geometry rows
  (REMMARCH slot — named, not decided).
- What would overturn: F-C22-1 disagreement (flips the
  certificate-bearer); F-C22-2+3 both passing (closes on incumbent).

### 4.4 C37 (:519-528)
- status: NEVER -> "ADJUDICATED-DEFAULT+GATED-LEVER (N6 panel instance
  executed 2026-08-20 wave-3; merge lever licensed behind band +
  rejector + materiality census)".
- Proposed note delta: THIS panel = the N6 right-sized instance of
  record (speed-audit N6 'needs its own panel' — consumed); incumbent
  any-flip-ends-segment = the certified-safe DEFAULT (constraint 7
  cannot be policy-violated); formal frame adopted = O-F19
  regime-cell/stratification-loci (diff :186-190, cited); PC^1
  anticipation closed as standalone policy, licensed only as an
  instrument of the same materiality band; [P-FLIPMAT] re-entry path =
  the licensed lever below (it stays DE-REGISTERED until F-C37-1/2
  define it); wave-2 composition pin honored: merged segments never
  resurrect flip-touched curvature ([P-QNCARRY] arm-B invalidation
  semantics, VERDICT_wave2 §4.2).
- Falsifiers pinned: **F-C37-1** (materiality census): on the FIRST
  post-8761dce campaign artifact (the trigger of record), flip census
  with benign-fraction measurement (benign = candidate-mergeable per
  F-C37-2's own definition); benign fraction below derived threshold =
  merge lever DEAD, C37 CLOSES on incumbent. **F-C37-2** (the license):
  a merged segment must replay BIT-IDENTICALLY in decisions and keep
  certificate/margin deltas inside the derived replay-fidelity band;
  any excess = merge REJECTED (constraint 7 upheld). **F-C37-3**
  (composition rejector): any merged segment carrying flip-touched
  curvature = REJECTED outright (wave-2 pin).
- BINDING F2 duty: **F2-C37-FLIPMAT** (census + band derivation; the
  merge build itself only fires if F-C37-1 shows materiality).
- Dependencies: C22 (rate at source), C32/[P-QNCARRY] (curvature carry
  semantics), O2 drift-watch data (named conditional of record,
  cited).
- What would overturn: F-C37-1 below threshold (closes row); F-C37-2
  violation (kills the lever permanently as stated).

### 4.5 C39 (:541-550)
- status: MIXED (unchanged — convention half stands; verification half
  moves NEVER -> "INSTRUMENTS-CONVERGED 2026-08-20 wave-3, execution =
  F2 duty riding [P-IPADJ]").
- Proposed note delta: verification stack of record = (1)
  complementarity band + except-pass counter with the S24 step-13d
  |mu*m| = 3.55e3 by-hand catch as MANDATORY retro-fixture (findings
  GAP-12 row, cited); (2) P-F26 marginal-value audit dJ/dc vs
  multiplier at margin-active checkpoints with O-F18 exchange-density
  semantics (diff :195-198, cited); (3) LSQ re-estimate referee on
  recorded gradients (Gill-Murray-Wright; Wächter-Biegler three-part
  termination; modern IP-multiplier pathology support arXiv:1707.07327
  [ABS]); instrument (4) Fiacco-via-elimination = C40-conditional.
  STANDING CONSTRAINT consumed: INFORMATION-ONLY discipline until
  [P-IPADJ] (VERDICT_wave2 §2.1/§4.1) — the stack VERIFIES, never
  consumes; it is the promotion path, ordered WITH [P-IPADJ].
- Falsifiers pinned: **F-C39-1**: the derived complementarity band must
  FIRE on the step-13d retro-fixture (a band that misses the known
  catch is rejected); **F-C39-2**: |dJ/dc - lambda| outside the derived
  band at a margin-active checkpoint = provenance REJECTED, LSQ referee
  becomes the reading of record for that verdict; **F-C39-3**: LSQ
  referee vs res.v disagreement above band on the S18/S24 recorded
  gradients = res.v demoted for that class until [P-IPADJ] explains
  it.
- BINDING F2 duty: **F2-C39-MULTVER** (rides the [P-IPADJ] window,
  first F2 engine act; C40's conditional elimination folded in).
- Dependencies: [P-IPADJ] (prerequisite semantics), C28 priced-frontier
  representation (multiplier meaning at boundary-active optima — wave-1
  of record, cited), C40 (instrument (4)).
- What would overturn: [P-IPADJ] revealing res.v semantics that
  invalidate a band's construction (bands re-derived, stack survives).

### 4.6 C40 (:552-560)
- status: NEVER -> "ADJUDICATED-CONDITIONAL (gap-accounting valve
  2026-08-20 wave-3; elimination = C39's lambda_e mechanism, else
  incumbent-by-materiality)".
- Proposed note delta: N-W §15.3 read [FULL] 2026-08-20 — simple linear
  elimination exact and safe, 1x1 basis conditioning trivial; findings
  severity LOW ("no record impact") consumed as materiality; the ONLY
  load-bearing payoff = exact lambda_e via AD post-optimality with
  O3.1-style check (C39 instrument (4)); adopted-as-direction
  CONDITIONAL on the C39 stack leaving lambda_e unverified; no
  standalone surgery, no separate duty (folded into F2-C39-MULTVER).
- Falsifier pinned: **F-C40-1**: eliminated-vs-row twin on one S18
  segment — identical certified outcomes + lambda_e agreement within
  derived band; disagreement = elimination WINS (provenance defect
  demonstrated); agreement + C39 stack sufficient = C40 CLOSES on
  incumbent by materiality.
- Dependencies: C39 (sole consumer); trees SILENT (census carries the
  row alone, declared).
- What would overturn: F-C40-1 disagreement.

### 4.7 C44 (:595-604)
- status: SINGLE-AUTHOR -> "ADJUDICATED-SPLIT (policy structure
  converged 2026-08-20 wave-3; noise-aware steps = measured F2 duty
  riding the C18 noise-floor window)".
- Proposed note delta: incumbent derived-for-smooth steps retained
  interim (genuine derivation on their axis, N-W §8.1 model);
  challenger = Moré-Wild-class noise-aware per-column steps, modern
  instance Shi-Xie-Xuan-Nocedal SISC 2022 [ABS]; SEAM DECLARED
  (brief mandate): the noise measurement consumed by the challenger IS
  the C18/C34/C35 derivation-window object — ONE window, C44 rides it,
  never forks it; seam/kink axis adopted as the O-F22/V-F29
  VERIFICATION BATTERY (diff :212-218, cited) under the UNCONDITIONAL
  [P-HESSREJ] (VERDICT_wave2 §2.2), not as new stencils; complex-step
  recorded as OPTION-WITH-STATED-PRECONDITION: analytic/twin tier only
  (the in-repo numpy-complex twin, O3.1-cs claims row, is the existing
  instrument; through the JAX custom_vjp engine path NOT established,
  not asserted).
- Falsifiers pinned: **F-C44-1**: measured per-column noise floor vs
  incumbent steps — incumbent inside the Moré-Wild near-optimal band
  (derived factor) => C44 CLOSES converged on incumbent; outside on any
  verdict-adjacent column => challenger adopted for those columns.
  **F-C44-2**: Taylor-remainder ramp with measured slope over a derived
  decade at a seam-adjacent column — slope break = seam defect of
  record, handled under [P-HESSREJ] (defect-distribution instrument
  already in its findings owner text). **F-C44-3**: complex-step
  cross-check on the twin tier at one record point (precondition
  honored) — disagreement beyond derived band = FD tier defect.
- BINDING F2 duty: **F2-C44-FDSTEP** (rides the C18 window +
  [P-HESSREJ]; no separate campaign).
- Dependencies: C18/C34/C35 (FAM slot — window owner; named, not
  double-adjudicated), C32 (fresh-FD interim = the consumer),
  cross-lowering discipline row (one lowering per comparison, cited).
- What would overturn: F-C44-1 inside-band (closes on incumbent);
  noise-floor window landing different constants (bands re-derived).

### 4.8 C45 (:606-615)
- status: SINGLE-AUTHOR -> "ADJUDICATED-WITH-VALVE (gap-accounting
  2026-08-20 wave-3; endpoint rejector + derived window = cheap duty;
  vectorization stays the dormant H2 conditional)".
- Proposed note delta: correctness half closed
  sufficient-not-optimized: endpoint rejector (root at either bracket
  boundary => LOUD REFUSAL, ~5 LoC) converts the hidden bracket
  hypothesis into a monitored one; window derivation from the
  admissible envelope box = the H-F6 reachable-set object (C25 CONV
  territory, NAMED not decided); speed half: H2's 444x block
  measurement CITED of record (bitwise identity falsified 1.46e-11 ->
  X-SCANM-grade gate), NOT adopted — targets MET (S25-bis), lever
  dormant on its existing named trigger; nothing re-measured.
- Falsifiers pinned: **F-C45-1**: endpoint-hit fixture (admissible case
  driven to the box edge) must REFUSE, not silently return the boundary
  root. **F-C45-2**: the derived window must CONTAIN the measured root
  for every record-corpus case with declared margin; any excursion =
  the hardcoded bracket was unsound of record (severity upgrade).
- BINDING F2 duty: **F2-C45-BRACKETGUARD** (F2 hygiene window, cheap).
- Dependencies: C25 (envelope box — CONV slot), H2 conditional
  (existing, unchanged).
- What would overturn: F-C45-2 excursion (upgrades severity and forces
  the derived window immediately).

---

## 5. PAPERS NEEDED (procurement channel; §0-bis(c))

1. **Moré & Wild, "Estimating computational noise", SISC 33(3), 2011
   (ECnoise)** — full text needed at F2-C44-FDSTEP execution to derive
   the F-C44-1 near-optimal band factor (the census holds it at [ABS];
   the protocol pin does not need it, the band DERIVATION does).
2. **Shi, Xie, Xuan & Nocedal, "Adaptive finite-difference interval
   estimation for noisy derivative-free optimization", SISC 44(4),
   2022** — arXiv:2110.06380 is fetchable as the searchable copy; the
   published version = citation of record for the same duty.
3. **Oliveira & Takahashi, "An enhancement of the bisection method
   average performance preserving minmax optimality" (ITP), ACM TOMS
   47(1), 2020** — OPTIONAL tier: only if F-C22-1 falsifies the
   incumbent predicate and the bracketed reference is promoted to
   certificate-bearer (engine choice then needs the full text).

No other row's claim waits on an unavailable text (Deuflhard and N-W
consumed [FULL] on disk this window).

---

## 6. MACHINE SUMMARY

Counts measured this window (SR-12):
- rows in mandate: 8 — `grep -cE '^- id: C(16|19|22|37|39|40|44|45)$' docs/choice_ledger.yaml` = 8.
- deltas proposed: 8 (§4.1-§4.8, one per row).
- web queries run: 6 (protocol table §2.1); on-disk [FULL] reads: 2
  (Deuflhard §3.3 pp.134-148; N-W §15.3 pp.427-430).
- candidate new rows: 0 — dedup verified by measured greps this window
  (`grep -nE 'GAP-28|GAP-18|GAP-12|GAP-16|GAP-32|P-HESSREJ|More-Wild|Deuflhard|Brent|Shewchuk|marginal-value|complementarity|leggeAree|damping' docs/findings_registry.yaml`
  and the companion greps on choice_ledger/claims/literature
  registries): every sub-object adjudicated above already has a
  findings/ledger home (constraints:multiplier-rejector-missing,
  driver-nonsmooth:hessian-no-rejector,
  driver-nonsmooth:flip-segmentation-materiality,
  cell-cert:wall-foot-search-fragile,
  constraints:lip-equality-not-eliminated); the axis-(5) JAX
  traceability seam is existing C48/engine territory (no mint).
- cava bearing: 0 rows (measured grep, §2.3).

```
{slot: REMENG,
 rows: {
  C16: {proposed: "ADJUDICATED-SPLIT: incumbent ladder interim; Deuflhard measured-contraction challenger; Armijo closed", gated: true, duty: "F2-C16-DAMPAB"},
  C19: {proposed: "ADJUDICATED-ON-COST: scalar scale retained, immaterial-declared with disparity-census rejector", gated: false, duty: "F2-C19-SCALECENSUS (hygiene row)"},
  C22: {proposed: "ADJUDICATED-SPLIT: burden on monotone-foot predicate; Q5 doctored-probe decider; bracketed-engine choice immaterial", gated: true, duty: "F2-C22-FOOTPROBE"},
  C37: {proposed: "ADJUDICATED-DEFAULT+GATED-LEVER (N6 panel instance executed): any-flip-ends stays default; merge licensed only behind band+bitwise rejector+materiality census", gated: true, duty: "F2-C37-FLIPMAT"},
  C39: {proposed: "verification half INSTRUMENTS-CONVERGED (complementarity band + marginal-value audit + LSQ referee; Fiacco = C40-conditional; INFORMATION-ONLY honored, rides [P-IPADJ])", gated: true, duty: "F2-C39-MULTVER"},
  C40: {proposed: "ADJUDICATED-CONDITIONAL (valve): elimination only as C39 lambda_e mechanism, else incumbent-by-materiality; no separate duty", gated: true, duty: "folded into F2-C39-MULTVER"},
  C44: {proposed: "ADJUDICATED-SPLIT: incumbent interim; noise-aware per-column steps ride the C18 window; seam axis = O-F22/V-F29 battery under [P-HESSREJ]; complex-step = option-with-precondition (twin tier only)", gated: true, duty: "F2-C44-FDSTEP"},
  C45: {proposed: "ADJUDICATED-WITH-VALVE: endpoint rejector + box-derived window; H2 vectorization cited, dormant conditional unchanged", gated: false, duty: "F2-C45-BRACKETGUARD (cheap)"}
 },
 census_recency: "1973-2026; core modern 2020-2026 (ITP 2020, Shi et al SISC 2022, AICN 2022-23, GNN warm-start 2025 [TITLE], LSQ-multiplier exposition 2026 [ABS]); two on-disk [FULL] reads (Deuflhard 2011 par.3.3, N-W 2006 par.15.3)",
 alternatives_closed: 9,
 escalation_candidates: 0,
 papers_needed: 3,
 candidate_new_rows: 0,
 inflation_check: done}
```
