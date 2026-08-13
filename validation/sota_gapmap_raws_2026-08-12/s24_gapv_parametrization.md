# S24 GAP VERIFICATION — FACET 3: DESIGN PARAMETRIZATION (ADVERSARIAL)
VERIFIER key: `parametrization`. Date 2026-08-12. Position verified:
`s24_gap_parametrization.md` (read in full). Method: every citation
re-opened against the actual file at the cited lines; both probe
scripts read line-by-line against `TV.spline_coeffs`/`spline_eval`
(a1_toc_variational_jax.py:131-165 — formula-identical) and RE-RUN
(total < 5 s); the P5 curvature-wave claim re-derived INDEPENDENTLY
with a fresh script (verify_p5.py, this scratchpad); coverage checked
against D6 duty rows (grep DUTY, rows 395-438), the S24 T0 postponement
census (PROGRESS_2026-08-12_S24_f1b.md step 3, all 20 rows read), and
M0 S20-S24 blocks (grep not-a-knot / natural right / dev_warm / knot
removal / coarsen / control-point / B-spline: ZERO hits outside the
code line itself). Default posture: refute.

PROBE RE-RUN RESULTS (all reproduce): P1 undershoot 0.1658, decay
0.243/interval; P1b' monotone VALUES to thB = 40 deg (as the finder
honestly declared); P2 6.925e-04 vs 6.661e-16 (quadratic) and
8.482e-04 vs 1.115e-05 = 76.0x (non-poly); P3 6.661e-16; P4' cond(A)
4.96/5.68/6.12/6.17 vs amplitude 1.10/2.22/17.52/170.68. P5
INDEPENDENTLY RE-DERIVED: M0 = -0.6894 @18.85 deg, -2.3751 @30 deg on
the linear taper, M1/M0 = -0.267949 = -(2-sqrt(3)) EXACT (the
decaying root of M_{i+1} = -4M_i - M_{i-1}), 7/7 sign flips from the
clamped end, and the 1/h scaling measured EXACT (m=8 -> m=16 doubles
M0, ratio 2.000). Probe hygiene note: probe_parametrization.py P4
(first version) emits divide-by-zero warnings from a degenerate
ratio=1 construction; the position cites only the clean P4' ladder —
no number rests on the flawed probe.

---

## FINDING 1 (interpolation-vs-control-point adjudication missing on
the oscillation axis) — **CONFIRMED — MEDIUM**
- Citations REAL: D6:922-926 verbatim rejects the control-point switch
  on "re-validating the entire certified stack" + "knot PLACEMENT, not
  parametrization conditioning" — the oscillation / variation-
  diminishing / convex-hull axis appears NOWHERE in the rejection text
  (D6:901-939 read in full). a1 S17 chain text verified at 1333-1336
  (finder cited 1337-1343 — minor offset, same block, real).
  adaptive_knot_optimize.py:12-14 "basis class UNCHANGED" verbatim.
  M0:1498-1506 (41.8%/18.9%/17.6% mass) verbatim. M0:1624-1637
  (Le Digabel-Wild, Known-Unrelaxable-Simulation-NONQUANTIFIABLE,
  "QUANTIFY a margin") verbatim.
- Genuinely a gap: census rows 1-20, D6 duty rows, and M0 S20-S24
  blocks contain NO row owning the basis-class oscillation axis. The
  S24 step-9 datum ("representation error 5.679e-3... the residual is
  attachment-region curvature, not node count") independently SUPPORTS
  the relevance of the axis.
- Mechanism verified: the P5 wave is analytic (recurrence root), the
  amplitude is proportional to the clamped-slope mismatch and grows as
  1/h (measured exact) — a real structural channel matching the S17
  chain wording ("spline oscillation at the attachment"), at the
  CURVATURE level (values stayed monotone: correctly declared).
- SOTA attribution correct: convex hull + variation diminishing are
  standard B-spline control-polygon properties (de Boor; Boehm 1980);
  derivative control points are scaled differences -> linear slope
  constraints. CST/Hicks-Henne correctly set aside as global-support.
- Severity grounds for MEDIUM, not HIGH: no verdict or record number
  is overturned; the finding is a missing adjudication plus forward
  levers (the zero-behavior-change post-solve change of basis is a
  legitimate additive first step). It does not relitigate the D6
  decision on its own axis (honesty preamble accurate to the D6 text).

## FINDING 2 (natural-right BC bias at the lip) — **CONFIRMED — HIGH**
- Citations REAL: a1:148 (`natural right: M_{n-1}=0`) verbatim; goal
  metric at the lip verbatim (adaptive_knot_optimize.py:242-250:
  |dJ/dy_lip - corner density|/|corner density|); lip interval 17.6%
  mass at M0:1501; D6:889-891 wording verbatim.
- Probe reproduced: 76x last-interval error on the non-polynomial
  contour; machine-exact not-a-knot control on the quadratic. The
  O(h^2)-at-the-boundary degradation for natural BCs on data with
  nonzero end curvature is textbook (de Boor) — attribution correct
  (not-a-knot = de Boor / FITPACK-scipy default lineage).
- Genuinely a gap: grep over validation/ + docs finds the natural-right
  condition ONLY at the code line; no twin, no carrier, no duty row,
  no census row, and no named conditional (C7 = joint mesh+knot
  refinement of the F1 LADDER — it does not touch the BC) measures the
  BC-induced representation floor at the node the goal of record
  differentiates. A Rao/TOC bell has nonzero lip curvature; the class
  forces zero at every m — knot insertion elsewhere cannot remove it.
- HIGH is earned: this is a named, currently-unexcluded ALTERNATIVE
  MECHANISM for the OPEN [C-O33] corner residual — it bears directly
  on a diagnosis of record (the S19 baseline 6.6295e-02 and the
  "design-class limit" reading). The S25 probe is correctly
  rejector-formed (GENO-oracle band must NOT move) and correctly
  deferred (needs marches, > 30 s).

## FINDING 3 (insertion guard mesh-derived, not operator-derived) —
**CONFIRMED — MEDIUM**
- Citations REAL: adaptive_knot_optimize.py:210-212 (dx_loc = median
  station spacing, skip closer than dx_loc) and header 39-42 ("a
  degenerate interval poisons the spline solve", the GENO double-point
  lesson) verbatim.
- Probe reproduced: cond(A) saturates ~6.2 at ratio 1000 while the
  cardinal amplitude grows ~linearly (2.2/17.5/170.7): the guard's
  STATED failure mode (solve poisoning) is measurably not the binding
  one (exact degeneracy aside, which the guard does prevent); the
  operator-growth mode is unguarded at any fixed dx_loc.
- Mesh-dependence verified: x_st in insertion_site are the indicator's
  wall stations, so dx_loc halves under march refinement while the
  operator bound is mesh-independent — structural, as claimed.
- MEDIUM, not HIGH: no retroactive record impact (S20 ran m=8->10 at
  Nw=60, ratios benign); the exposure is the loop's future coverage.
  Fix shape is additive (operator-derived primary bound), R5-clean.

## FINDING 4 (warm-start exactness: unarmed rejector, under-claimed
theorem) — **CONFIRMED — MEDIUM**
- Citations REAL: header 44-48 ("NOT claimed geometry-preserving...
  MEASURED and printed") and 446-451 (dev_warm print, NO check() row)
  verbatim — the deviation cannot fail the carrier today.
- Theorem claim INDEPENDENTLY CHECKED and correct: the incumbent
  spline is piecewise-cubic C^2 on the refined knot set (C^inf at new
  knots), satisfies the refined interpolation data (y_new sampled from
  itself, lines 430-432), the same clamped-left slope (thB unchanged,
  line 434/419), and the same natural-right condition at the same
  endpoint — uniqueness of the clamped/natural interpolant gives
  EXACTNESS. P3 reproduces 6.7e-16. The y_new[-1] = yL overwrite (line
  433) is a no-op iff the incumbent satisfies the eps equality — if it
  ever is not, dev_warm reads the violation: MORE reason it is a
  defect detector, not less.
- Genuinely a gap: no duty/census row owns arming it; R5 ("tests must
  be able to reject") is the project's own standard; the derived-floor
  shape (K_RICH * eps * measured cardinal amplitude * scale) is
  consistent with the P4' measurement. The R4 promotion (nestedness
  statement to M0, class THEOREM) is a genuine same-session-culture
  duty the header currently contradicts ("interpolation is not Boehm
  insertion" — true as an algorithm, false as a property).
- MEDIUM: guards the integrity of every future [X-AKNO] cycle verdict;
  no existing record number affected.

## FINDING 5 (insertion-only outer loop, no removal/coarsening) —
**DOWNGRADED — MEDIUM** (core stands; one extremal REFUTED, one SOTA
attribution corrected)
- Citations REAL: header 6-14 (AFEM/FITPACK skeleton) and stop rules
  (improvement/rise/empty/budget, none remove — verified at 56-59 and
  567-574); D6:938-939 "dof economy is part of correctness here"
  verbatim; header 32-34 names the per-dof n+1-eval budget pressure.
- CORRECTION 1 (SOTA attribution): "the cited AFEM lineage achieves
  instance-optimal complexity ONLY with a coarsening/removal leg" is
  OVERSTATED — Binev-Dahmen-DeVore 2004 used coarsening, but
  Stevenson 2007 and Cascon-Kreuzer-Nochetto-Siebert 2008 established
  rate-optimality of Doerfler-marked AFEM WITHOUT coarsening for the
  elliptic model problem. The finder's point survives only via the
  correct narrower argument: those theorems address a FIXED problem;
  here the goal functional's optimum MOVES each cycle
  (re-optimization), so a knot justified by cycle-k residual can be
  dead at cycle k+1 — a setting the no-coarsening theorems do not
  cover, and where the measured per-dof tax (n+1 evals/segment) is
  real. With that repair the gap stands.
- CORRECTION 2 (E2 REFUTED): the artifact of record saves best["W"],
  best["xi"] (adaptive_knot_optimize.py:602-614), i.e. the BEST
  cycle's class — a restart from the artifact does NOT inherit the
  failed knots of a goal-ROSE final cycle. Only the in-memory
  W_cur/xi_cur at the break carries them, and nothing downstream
  consumes it.
- Residual severity MEDIUM (efficiency/coverage): removal is made
  cheap-to-test by the Finding-4 exactness (project + measure against
  a derived band), and the loop's own header prices the cost of dead
  dofs; but no verdict or record number is currently affected.

## FINDING 6 (dense Hessian + unrolled dense solve: basis-locality
cost component) — **DOWNGRADED — MEDIUM** (real, but partially OWNED
already)
- Citations REAL: a1:1087-1095 (full FD Hessian, n+1 evals, n_eval +=
  n+1) verbatim; a1:131-150 (dense (n,n) built by a Python .at[] loop
  + jnp.linalg.solve on a tridiagonal system) verbatim; D6:873-881
  T2-FIRED + "colored Hessians" as a NAMED scale lever verbatim;
  header 32-34 verbatim.
- Downgrade grounds: "a basis-locality component NOBODY priced"
  overstates — the colored-Hessian lever is NAMED in D6 with the G0/T2
  review SCHEDULED at F2 ENTRY (S24 census row 7, of record). What is
  genuinely new and correct: (i) coloring is USELESS under the current
  basis without a truncation adjudication — P1's measured never-zero
  cardinal decay (0.243/interval) is the honest obstacle, and the
  band-truncation-with-derived-bar route WITHOUT a basis switch is a
  legitimate, cheap, previously unpriced alternative (S25 hess-decay
  probe is well-formed: n+1 evals, ~30 s); (ii) the O(n^3) unrolled
  solve is real but self-admittedly noise at current m vs march cost
  (records 111 s) — hygiene-grade alone.
- MEDIUM (efficiency; feeds the already-queued T2/G0 review with a
  measured decomposition it currently lacks).

## FINDING 7 (declared slope/class monitors never computed;
geometry-vs-certification conflation in the rejection ledger) —
**CONFIRMED — MEDIUM**
- Citations REAL: a1:18-20 ("DECLARED monitors at instance, not active
  constraints") verbatim; independent grep confirms `slope` appears
  ONLY at the docstring and in spline internals — no positivity check
  on any path; rejected_designs ledger exists (a1:1023, 1229, 1556)
  with NO geometry tag; M0:1624-1637 taxonomy verbatim (and note: the
  margin-constrained reformulation there quantifies the
  CERTIFIABILITY constraint — it does not touch geometric
  admissibility, so no existing remedy covers this).
- PRECISION CORRECTION (does not kill the finding): "CLOSED-FORM in W
  ... linear in ys, M — and M is linear in ys" — linear in ys at FIXED
  thB only; thB enters xs (hence A, hence M) nonlinearly. The
  pre-march check is closed-form and microsecond-cheap regardless
  (per-interval cubic slope extrema given W), which is what the fix
  shape needs; but the "LINEAR inequalities on W" phrasing belongs to
  the B-spline basis of Finding 1, not to the current class. As
  written for the current class it is slightly overclaimed.
- Conflation channel verified open: the S20 "8/8 genuine" certdiag
  (M0:1618-1619) discriminates tolerance-vs-budget (cap raised, floor
  untouched), NOT geometry-vs-physics — so a geometry-representable
  rejection would still read "genuine". Whether any of the five S20
  frontier rejections actually WAS geometry is exactly the registered
  S25-P4 probe (correctly flagged as touching a reading of record,
  rejector-grade design first).
- MEDIUM now; escalates to HIGH only if S25-P4 finds a
  geometry-representable rejection among the S20 five. Claims-to-code
  genre attribution correct.

## FINDING 8 (normalized-xi knot anchoring drifts with thB) —
**DOWNGRADED — LOW** (mechanism real and unmonitored; everyday
magnitude overstated ~10x at the instance of record)
- Citations REAL: adaptive_knot_optimize.py:424-425 (xi from CURRENT
  xB) and a1:176-179 (xs re-anchored at LIVE thB) verbatim; S18 record
  verified in the S18 log ("W*: thB = 15.5527 deg (seed 18.8456)") and
  xB 0.145 -> 0.121 consistent with rtd sin(thB); d(x_knot)/d(xB) =
  1 - xi correct; no drift monitor exists (grep).
- MAGNITUDE CORRECTIONS: (a) "a ~17% shift of near-attachment knot
  positions" — 17% is the relative shift of xB itself (0.024/0.145);
  the near-attachment KNOT shift at the S18 event is ΔxB(1-xi) ≈
  0.021 ≈ 4.4% of the m=8 uniform first interval (L = 4.0 of record,
  TCASE xtronc — verified). (b) EVERYDAY claim "~0.008 in xB, ~15% of
  the first uniform interval at m=8" is WRONG at the instance of
  record: 0.008 * (1 - 1/8) / 0.485 ≈ 1.4%, not 15% — off by ~10x.
  The claimed magnitudes are reached only against post-insertion
  LOCAL intervals near the attachment (where [X-AKNO] concentrates
  knots) or at short-L instances — E2 legitimate, EVERYDAY not.
- Kept alive (not refuted) because: the mass concentration (41.8%)
  sits exactly where insertions shrink local intervals, so per-cycle
  drift CAN be a material fraction of the LOCAL marked interval, and
  nothing measures it; the additive fix (print + band the drift) is
  cheap and R5-clean. LOW (monitoring hygiene).

---

## DROPPED-CANDIDATE AUDIT (position section verified)
The 4 declared drops check out: CST/H-H/FFD fold-in is fair (global
support / embedding dimension); uniform-vs-curvature abscissae is
indeed superseded by the adjudicated [X-AKNO]; the xs_of duplication
(324-331 vs TV.wall_geometry) confirmed real and correctly triaged as
consequence-free smell; kappa_diag off-diagonal fold-in consistent
with Findings 1/6.

## COUNTS
- CONFIRMED: 5 (F1 MEDIUM, F2 HIGH, F3 MEDIUM, F4 MEDIUM, F7 MEDIUM)
- DOWNGRADED: 3 (F5 MEDIUM — E2 sub-claim refuted + AFEM attribution
  corrected; F6 MEDIUM — partially owned by the scheduled G0/T2
  review; F8 LOW — everyday magnitude overstated ~10x)
- REFUTED outright: 0
- Severity tally: HIGH 1, MEDIUM 6, LOW 1.

## VERIFIER'S NET READING
The position is citation-sound (every file/line real; two minor line
offsets noted, none load-bearing), probe-sound (all numbers reproduce;
P5 re-derived independently including the exact -(2-sqrt(3)) ratio and
1/h scaling), and coverage-sound (census, duty rows, M0 blocks checked:
none of the eight axes is owned elsewhere, except Finding 6's partial
overlap with the scheduled G0/T2 review). The single HIGH (natural-BC
lip bias as an unexcluded alternative mechanism for open [C-O33]) is
the item with verdict-of-record exposure and has a correctly
rejector-formed S25 probe. No proposed fix weakens any gate; all fix
shapes are additive. Overstatement pattern to watch in the finder's
future output: extremal arithmetic quoted as everyday (F8), and
lineage claims quoted at their strongest historical form (F5).
