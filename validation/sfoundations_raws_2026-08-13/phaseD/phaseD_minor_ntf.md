# PHASE D MINOR (a) — NTF: DERIVATION OF NEWTON_TOL_FACTOR
# (theory half only; gate REFORM stays F2 per brief)
# S-FOUNDATIONS-C4 Blocco 1, 2026-08-20. Author slot per
# BRIEF_blocco2_phaseD.md MINORS (a). Output of record for the
# one-refuter round; adopted statements land in M0 + registry rows in
# the same landing window (orchestrator executes).

## 0. Mandate and seam position (no collisions)

Mandate row: docs/findings_registry.yaml `engine-core:F5-underived-
factors` (:214-222, read [FULL]): NEWTON_TOL_FACTOR = 100.0
(validation/a1_ideal_march_jax.py:200) is the S-CERT P1 underived
load-bearing constant; GAP-29 sweep of record
(validation/s25bis_gap29_sweep.json, committed carrier): NTF/2 FLIPS
cert_verdict (PASS -> FAIL), C_FLOOR/2 and C_OPS/2 no-flip. Owner:
"F2 (derivation paragraph or reclassification per flip row)". This
document IS that derivation paragraph.

SEAM (binding, consumed): VERDICT_wave2 §4.11 — "the kappa-qualified
band and the NEWTON_TOL_FACTOR derivation are one question (GAP-29
factor-2 cliff)"; VERDICT_wave3 §7 item 2 — the noise-floor
derivation window (C18/C20 Tier-1) has FOUR riders and ONE owner
(C34/C35 consume the floor as input; C17 joins the seam; C44 rides
the same measured-noise object); no side re-derives it. POSITION OF
THIS DOCUMENT: it is the THEORY HALF of that single window — it
derives the bound structure and the derived form of the constant; the
per-cell floor MEASUREMENT stays inside the F2-C20-CERTQUAL-CAMPAIGN
Tier-1 window shared with C18 (VERDICT_wave2 §2.8). Nothing here
re-derives C34's TR floor, C35's xtol_u arithmetic (VERDICT_wave3
§1.1/§1.2 adopted forms, consumed as-is), or the Tier-1 kappa band
itself. Anchor-drift note: VERDICT_wave2 cites the C18 ledger row at
:315-324; measured in this window the row sits at
docs/choice_ledger.yaml:324-333 (row id C18 unchanged — cite by id).

Object under derivation. Code semantics (a1_ideal_march_jax.py, read
at :427-460 and :793-825):
- Termination: the Newton loop exits when the undamped step satisfies
  step <= T(z) := NTF * EPS * sc(z), sc(z) = max(1, max|z|)
  (scalar scale = C19, DECIDED ADJUDICATED-ON-COST, not re-litigated),
  EPS = float64 machine epsilon (:168), cap N_NEWTON = 30 (C17).
- Certification ("one-extra-step ratio semantics", :795-813): one
  extra Newton step at the returned solution must move it by less
  than T(z); recorded ratio = step/T(z); cert_verdict PASS iff
  worst ratio <= 1 over the certified population.

## 1. NTF-1 — Roundoff-floor model of the extra step [SCHEMA]

Hypotheses (H1-H4, each trivially checkable):
H1 (float model) Every stored/computed scalar obeys
    fl(x) = x(1+e), |e| <= u = EPS/2 [Nocedal-Wright 2ed, App. A,
    eq. (A.30), book p. 614 — read [PAGES]].
H2 (root regularity) At the certified cell the true root z* has
    invertible Jacobian J(z*) and the iterate sits in the Newton
    contraction ball (checkable from the recorded contraction).
H3 (evaluation-error envelope) The computed residual satisfies
    r_hat(z) = r(z) + delta(z), ||delta|| <= gamma_R * EPS * S_R,
    with S_R the intermediate-quantity scale of the residual
    evaluation and gamma_R an op-count/cancellation factor
    (Higham-class gamma_n envelope; for THIS residual gamma_R * S_R
    is NOT derivable a priori at useful tightness: the residual mixes
    units across rows (position ~ y, compatibility ~ u^3, code
    comment :796-798) and includes tabulated-thermo interpolation
    (N_TAB grid) whose error scale is a table property, not an
    op-count — this is WHY the route of record is measured-model, not
    pure Higham; consistent with the C18 alternatives row and with
    the Moré-Wild measured-noise route named there).
H4 (solve error) The linear solve contributes a comparable
    EPS-proportional term (folded into gamma_R below; refinement
    belongs to the measurement, not to this schema).

Statement (the model): at a true root, the computed one-extra-step
satisfies
    ||dz_extra|| = ||J_hat^{-1} r_hat(z*)|| <= kappa_eff * EPS * sc(z),
    kappa_eff := ||J^{-1}|| * gamma_R * S_R / (EPS-normalized sc),
i.e. the extra step at convergence does NOT go to zero: it stalls at
a floor floor_z = kappa_eff * EPS * sc(z), where kappa_eff is a
per-cell dimensionless amplification combining residual-evaluation
noise and Jacobian conditioning. kappa_eff is the certificate-side
face of the SAME object as the Tier-1 kappa(J)-aware band (C20) and
the C44 FD-noise floor — one measured-noise object, four riders
(VERDICT_wave3 §7.2). This floor is Deuflhard's "required error
accuracy sufficiently above the machine precision" (NLEQ-ERR, CSM 35
p. 148, read [PAGES]) — stated there as UNQUANTIFIED practice; NTF is
precisely its quantification for this engine.

Measured instance (committed carrier s25bis_gap29_sweep.json; R5
arithmetic declared: extra-step multiple = cert_worst * ntf per arm):
- base arm (NTF=100): worst ratio 0.7011026275409529 -> worst-cell
  extra step = 70.110 * EPS * sc.
- ntf50 arm (NTF=50): worst ratio 1.033309604151919 -> worst-cell
  extra step = 51.665 * EPS * sc.
The threshold halved (2x) while the worst-cell extra-step magnitude
moved only 1.357x (70.110/51.665) — the extra step is
floor-dominated, not tolerance-dominated (caveat declared: the worst
cell may differ between arms; the inference is population-level).
Measured floor bracket on the record case: kappa_eff,worst in
[51.7, 70.1].

Falsifier (NTF-1): a per-cell floor measurement (extra-step probes at
converged cells and/or ECNoise/Moré-Wild-class noise estimation, the
already-registered seam instrument) finding (i) extra-step magnitudes
that DO track the requested tolerance below 50*EPS*sc (no floor), or
(ii) a floor scaling other than proportional to EPS*sc under a
precision contrast (float32: floor multiple must be invariant while
EPS grows ~1e9x; if the multiple shifts by more than the declared
band, H3's envelope form is refuted). Measured half = F2 duty, §5.

## 2. NTF-2 — Two-sided certificate semantics [THEOREM*]

Exact-arithmetic content (cited, not re-proved): for a Newton iterate
z_k in the contraction regime Theta_k := ||dz_{k+1}||/||dz_k|| <= 1/2,
the newly computed correction is a two-sided estimator of the CURRENT
error:
  (a) upper: ||z_k - z*|| <= ||dz_k||/(1 - Theta) <= 2 ||dz_k||
      [Deuflhard CSM 35, termination criterion (2.13)-(2.14), book
      pp. 51-52, read [PAGES]];
  (b) lower: ||z_k - z*|| >= c_L ||dz_k|| with c_L >= 1/2 in the
      contraction regime [Gragg-Tapia two-sided bound, eq. (7) of
      Yamamoto 1986, Numer. Math. 48, pp. 91-92 — rendered pages
      (PDF has no text layer), read [PAGES]].
Composition with NTF-1 (this is what earns the star): in floats the
estimator saturates at the floor, so a PASS of the one-extra-step
certificate at threshold T(z) = NTF*EPS*sc certifies
    ||z_hat - z*|| <= 2 * NTF * EPS * sc(z)
(the floor term is absorbed: at a PASS, step <= T already includes
the floor contribution), and a FAIL at a cell whose kappa_eff < NTF
witnesses genuine non-convergence (error >= T/2 up to the floor
term). Rigor: THEOREM* — exact-arithmetic theorem (cited) composed
with the SCHEMA-level floor model NTF-1; the star discharges to
THEOREM when the F2 floor measurement bounds kappa_eff
population-wide.

Falsifier (NTF-2): a planted-root test where a cell PASSes the
certificate while an independently computed true root (e.g. extended
precision) sits farther than 2*T + measured-floor from the iterate;
or a genuinely unconverged planted iterate (error >> T) that PASSes.
(These are the GAP-3-class F-C20-1 cases; shared instrument, cited
not duplicated.)

## 3. NTF-3 — The bound the factor must guarantee, and the derived form [THEOREM* / SCHEMA]

The derivation paragraph proper (the brief's ask). The certificate is
simultaneously non-vacuous and sound iff T(z) = NTF*EPS*sc(z) sits in
the window between the roundoff floor and the downstream tolerance
budget:

  (LB — satisfiability/non-vacuity)  NTF >= eta * kappa_eff,max
      over the certified population, headroom eta > 1 declared.
      Guarantees: a true root PASSes (no false-FAIL — the exact-root
      false-FAIL mode of F-C20-1); equivalently the termination
      metric is reachable (see NTF-4).

  (UB — soundness for consumers)  2 * NTF * EPS * sc <= tol_min,
      where tol_min = the tightest NTF-INDEPENDENT downstream
      tolerance consuming the certified error (consumers that co-move
      with NTF — the O3.1 replay band at a1:1448 = 10*NTF*EPS*scale —
      re-price automatically and do not bind the UB). Guarantees: a
      PASS delivers an error every consumer of floor_W can absorb
      (NTF-2(a)).

  (Window nonemptiness — the load-bearing compatibility condition)
      2 * eta * kappa_eff,max * EPS * sc <= tol_min.
      On the record case: 2*100*EPS = 4.44e-14 (unit scale) vs the
      smallest NTF-independent record tolerances (o31_tol = 7.65e-2,
      carrier s25bis_gap29_sweep.json) — the window is open by >11
      orders; the condition is stated because it is what a future
      tighter consumer (C35's xtol_u chain, C34's TR floor) must be
      checked against at composition time (C41 P-tag discipline).

Given NTF-1/NTF-2 as hypotheses, the window inequality is exact
[THEOREM* — same star-discharge as NTF-2]. The DERIVED FORM of the
constant is
    NTF = eta * kappa_q,
kappa_q = an upper quantile (declared at duty time) of the measured
per-cell kappa_eff population, eta = declared headroom [SCHEMA until
the F2 measurement lands, then reclassifies per the flip row's owner
clause]. Headroom direction is TWO-SIDED and therefore NOT
blanket-declarable "conservative" (the C42 roles-4/5
inverted-direction precedent, VERDICT_wave3 §1.5): larger eta
protects against false-FAIL but loosens the certified error bound
linearly for every floor_W consumer. Declaration of record: eta
bracketed, eta in [1.25, 2.5], sufficient-not-optimized (lower edge =
25% floor-measurement slack; upper edge = keeps the certified error
within the same decade as the floor), superseded by the measured
kappa_eff dispersion at duty time.

Incumbent adjudication: NTF = 100 is a VALID INSTANCE of the derived
form on the record case — measured headroom 100/70.110 = 1.426,
inside the declared bracket. The GAP-29 /2 flip is the model's
PREDICTION, not an anomaly: 50 < kappa_eff,worst ~= 70.1, so FAIL is
required; the flip row retro-validates NTF-1 (one committed
confirmation instance). The incumbent's own evidence class:
PRACTICE-validated instance of a SCHEMA-derived form; population
measurement = F2.

Falsifier (NTF-3): the F2 population measurement finding
kappa_eff,q95 > 100/1.25 = 80 on production marches refutes the
incumbent's headroom claim and forces the derived constant (registry
trigger "any sweep flip row = immediate derivation duty" already
live); a measured kappa dispersion so wide that no eta in the
declared bracket covers q95 while meeting the UB refutes the
single-constant FORM itself (per-cell or per-family NTF then owed —
that would be a reclassification, flagged to the C18 row).

## 4. NTF-4 — Termination coupling (C17 seam) [SCHEMA]

The loop condition (:448) and the certificate (:813) use the SAME
threshold T(z). Hence if NTF < kappa_eff(cell), metric-termination is
unreachable at that cell: the loop always exhausts N_NEWTON = 30
trips (C17's cap becomes the de facto terminator — silent per-cell
cost inflation) AND the cell then fails certification. The LB in
NTF-3 therefore protects BOTH contracts at once; conversely C17's
trip cap is the only guard below the floor. The ntf50 arm carries the
FAIL signature; the trip-count signature was not recorded by the
sweep (the sweep json has no per-cell trip field) — claim held at
SCHEMA with its measured half named, not asserted.

Falsifier (NTF-4): trip-count instrumentation under the NTF sweep
showing metric-termination still reached at the ntf50 arm's failing
cells (would refute the same-threshold coupling claim for this
engine). F2 duty, §5.

## 5. F2 duties (measured halves, NAMED — nothing executed here)

- F2-NTF-FLOOR-POPULATION: per-cell kappa_eff measurement
  (converged-cell extra-step probes + ECNoise/Moré-Wild-class noise
  floor + float32 precision contrast for the EPS*sc scale law) across
  production marches; quantile + eta ratification; RIDES
  F2-C20-CERTQUAL-CAMPAIGN Tier-1 (window shared with C18 per
  VERDICT_wave2 §2.8 — no new window minted; the four-rider/one-owner
  discipline of VERDICT_wave3 §7.2 preserved).
- F2-NTF-TERMCOUPLE-TRIPCOUNT: trip-count instrumentation under the
  NTF sweep (NTF-4 falsifier).
- Gate REFORM (how the cert gate consumes the derived constant,
  incl. any per-family split): stays F2 per the brief — out of scope
  here, named for completeness.
- Downstream re-pricing on any NTF change: C34 TR floor, C35 xtol_u,
  O3.1 replay band re-price linearly (notification semantics per
  VERDICT_wave3 §7.1-7.2; composition P-tags per C41 policy) — a
  landing rider, not a new derivation.

## 6. Papers read (depth + pages, declared)

- Deuflhard, Newton Methods for Nonlinear Problems (CSM 35), 2011 —
  literature/deuflhard_2011_newton_methods_affine_invariance_csm35.pdf
  [PAGES]: book pp. 51-53 (§2.1.1-2.1.2: Theta monitor, Kantorovich
  estimates, termination (2.13)-(2.14)), pp. 96-98 (§2.3.1-2.3.2
  energy-norm termination), pp. 130-131 (NLEQ-RES: "residual accuracy
  sufficiently above the machine precision"), pp. 147-148 (NLEQ-ERR:
  ||dx_{k+1}|| <= XTOL + "error accuracy sufficiently above the
  machine precision"). Rest: keyword-scan only (declared).
- Yamamoto 1986, Numer. Math. 48:91-98 — literature/yamamoto_1986_
  newton_kantorovich_error_bounds_numermath48.pdf [PAGES]: pp. 91-92
  (Thm 1 Kantorovich; Thm 2 Gragg-Tapia eq. (7) two-sided bound; Thm
  3 Potra-Pták; Thm 4 Miel), read via rendered images (PDF has no
  text layer). pp. 93-98 unread.
- Nocedal-Wright, Numerical Optimization 2ed —
  literature/nocedal_wright_2006_numerical_optimization_2ed.pdf
  [PAGES]: p. 614 (App. A, float model (A.30), unit roundoff),
  p. 195 (§8.1 FD/noise context for the C44 seam). Rest unread this
  window.
Lit-registry rider for the landing: all three promote UNREAD ->
READ-PAGES with the where_read anchors above (orchestrator applies).

## 7. PAPERS NEEDED

- Higham, Accuracy and Stability of Numerical Algorithms 2ed —
  CONDITIONAL: only if a derivational (op-count gamma_n) cross-check
  of the measured kappa_eff route is wanted at the F2 duty window
  (the C18 row names it as the alternative route; the measured route
  stands without it).
- Moré-Wild ECNoise: ALREADY FILED in VERDICT_wave3 papers_needed
  (FAM item 1 = REMENG item 1, one deduplicated entry) — not
  re-requested here; this slot consumes the same arrival.

## 8. Machine summary

item: minor (a) NTF
statements:
  NTF-1: roundoff-floor model of the one-extra-step metric — SCHEMA
    (H1-H4 declared; measured instance kappa_eff,worst in [51.7,70.1],
    carrier s25bis_gap29_sweep.json)
  NTF-2: two-sided certificate semantics, PASS => error <= 2*NTF*EPS*sc
    — THEOREM* (Deuflhard (2.13)-(2.14) + Yamamoto eq.(7) composed
    with NTF-1; star discharges on F2 floor measurement)
  NTF-3: window bound eta*kappa_max <= NTF <= tol_min/(2*EPS*sc) —
    THEOREM* given NTF-1/2; derived form NTF = eta*kappa_q — SCHEMA;
    incumbent 100 = valid instance (headroom 1.426); GAP-29 /2 flip =
    model prediction (50 < 70.1), retro-validation
  NTF-4: termination/certification same-threshold coupling — SCHEMA
    (trip-count measured half named)
  NTF-5 (seam, §0): theory half of the ONE C18/C20-Tier-1 window;
    floor_W := NTF*EPS*sc consumed by C34/C35 unchanged — PRACTICE
f2_duties: [F2-NTF-FLOOR-POPULATION (rides F2-C20-CERTQUAL-CAMPAIGN
  Tier-1, shared C18), F2-NTF-TERMCOUPLE-TRIPCOUNT, gate-REFORM
  (pre-existing, out of scope here)]
escalation_candidates: none from author side
papers_needed: [Higham ASNA 2ed (conditional), Moré-Wild ECNoise
  (already filed wave-3, deduplicated)]
