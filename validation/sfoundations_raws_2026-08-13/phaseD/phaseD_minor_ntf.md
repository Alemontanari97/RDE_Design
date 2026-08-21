# PHASE D MINOR (a) — NTF: DERIVATION OF NEWTON_TOL_FACTOR
# (theory half only; gate REFORM stays F2 per brief)
# S-FOUNDATIONS-C4 Blocco 1, 2026-08-20. Author slot per
# BRIEF_blocco2_phaseD.md MINORS (a). Output of record for the
# one-refuter round; adopted statements land in M0 + registry rows in
# the same landing window (orchestrator executes).
# [ESC-r1] ESCALATION E-1 REVISION (VERDICT_blocco2 §3 E-1, 2026-08-20):
# revised IN PLACE, escalation round 1; ALL 12 sustained findings of
# refute_minor_ntf.md applied with markers [ESC-r1-<n>] (<n> = the
# MIN-NTF finding number); dispositions in §9 at EOF. Repairs verified
# BEFORE adoption: refuter probe re-run exit 0 this window + escalation
# probe esc_probe_ntf_repaired_bound_window.py (16/16 checks, exit 0).
# [ESC-r2] ESCALATION ROUND 2 REVISION (2026-08-20): all findings of
# esc_refute_ntf_r1.md addressed with markers [ESC-r2-<n>] (<n> = the
# ESC-NTF-r1 finding number); dispositions in §10 at EOF. Repairs
# verified BEFORE adoption, all probes re-run exit 0 THIS window:
# esc_probe_ntf_r1_envelope_lower_bound.py (scene C counterexample
# stands, scene D confirms the H5-conditioned claim),
# esc_probe_ntf_repaired_bound_window.py (16/16),
# r22f_v2_probe_minor_ntf_pass_bound_and_termination.py (scenes A+B).

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
    eqs. (A.30)-(A.31), book pp. 614-615 — read [PAGES]; [ESC-r1-7]
    (A.30) is the storage model, (A.31) the per-operation model, same
    bound u — both consumed].
H2 (root regularity) At the certified cell the true root z* has
    invertible Jacobian J(z*) and the iterate sits in the Newton
    contraction ball (checkable from contraction data the F2 probes
    will record [ESC-r1-11]: the current record carries no per-cell
    Theta — the march records cert ratio and population count only,
    a1:793-828, and the sweep adds none).
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
    kappa_eff := ||J^{-1}|| * gamma_R * S_R / sc   (dimensionless)
[ESC-r1-6: the previously printed denominator "(EPS-normalized sc)"
was garbled and invited reading an extra 1/EPS into kappa_eff; EPS
appears exactly once, explicitly, in the floor formula below — the
measured-instance arithmetic never used the symbolic form and is
unaffected],
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
      [ESC-r1-4: attributed as the geometric-series consequence of
      uniform contraction Theta_j <= Theta <= 1/2 for j >= k — which
      H2's contraction ball supplies (cf. Deuflhard CSM 35,
      (2.10)-(2.14), book pp. 51-52, read [PAGES] [ESC-r2-2: span
      opened at (2.10), the first display ON the declared read
      pages — p. 52 only REFERENCES (2.8), which sits on an unread
      page]; note (2.14)'s literal denominator at source is
      1 - Theta^2_{k-1}, not 1 - Theta — the form used here is the
      series bound, not the literal equation; cf. also Yamamoto
      eq. (7), already cited in (b): a two-sided DISPLAY whose upper
      half bounds the PREVIOUS correction at source and yields the
      current-correction form only after an index shift plus one
      triangle step [ESC-r2-2 — "equivalently" retired: the
      geometric-series attribution is primary and carries the
      statement alone])];
  (b) lower: ||z_k - z*|| >= c_L ||dz_k|| with c_L >= 1/2 in the
      contraction regime [Gragg-Tapia two-sided bound, eq. (7) of
      Yamamoto 1986, Numer. Math. 48, pp. 91-92 — rendered pages
      (PDF has no text layer), read [PAGES]; [ESC-r1-10] eq. (7)
      actually yields c_L >= 2/(1+sqrt(2)) ~= 0.828 (worst case at
      theta -> 1); 1/2 is kept as the declared valid-conservative
      constant — ~1.66x tightening available for free at the F2 duty
      window if the FAIL-witness bound ever becomes binding].
Composition with NTF-1 (this is what earns the star) [ESC-r1-1,
repaired constant — verified by probe scene A + escalation probe]:
the measured extra step is dz_hat = dz_exact + delta with ||delta||
<= floor_z (NTF-1); noise bounded by the floor can CANCEL part of
the exact correction, not only inflate the measured step, so a PASS
(||dz_hat|| <= T) bounds only ||dz_exact|| <= T + floor_z. Composing
with the exact two-sided upper estimator (a), a PASS of the
one-extra-step certificate at threshold T(z) = NTF*EPS*sc certifies
    ||z_hat - z*|| <= 2 * (T(z) + floor_z)
                    = 2 * (NTF + kappa_eff(cell)) * EPS * sc(z)
                   <= 2 * NTF * (1 + 1/eta) * EPS * sc(z)
(last step population-wide under NTF-3's LB, NTF >= eta*kappa_eff,max.
The previously printed constant 2*NTF*EPS*sc and its "floor is
absorbed" parenthetical were WRONG — the parenthetical inverted the
triangle inequality; executable counterexample of record, probe
scene A: PASS at ratio 0.990 with true error 3.401*T > 2*T under the
declared floor 0.8*T; the repaired bound 2*(T+floor) = 3.6*T holds,
err/bound = 0.945), and a FAIL at a cell whose kappa_eff < NTF
witnesses genuine non-convergence (error >= T/2 up to the floor
term — this direction already carried the floor caveat and HELD).
[ESC-r1-9] Two DISTINCT objects, stated so no downstream reader
conflates them: the THRESHOLD object T(z) = floor_W = NTF*EPS*sc is
what C34/C35 consume (correct for C35's premature-stop purpose,
VERDICT_wave3 §1.2 — unchanged); the CERTIFIED-ERROR object is the
strictly larger 2*(T+floor_z) <= 2*T*(1+1/eta) above — consumers of
a certified ERROR bound must take the latter, never T itself.
Rigor: THEOREM* on the repaired constant — exact-arithmetic theorem
(cited) composed with the SCHEMA-level floor model NTF-1; the star
discharges to THEOREM when the F2 floor measurement bounds kappa_eff
population-wide.

Falsifier (NTF-2): a planted-root test where a cell PASSes the
certificate while an independently computed true root (e.g. extended
precision) sits farther than 2*(T + measured-floor) from the iterate
[ESC-r1-1: threshold aligned to the repaired constant];
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

  (UB — soundness for consumers) [ESC-r1-1/-2, repaired form]
      For EACH downstream consumer c of the certified error:
          2 * (1 + 1/eta) * NTF * EPS * sc * A_c <= tol_c,
      where A_c is the DECLARED unit-transfer factor from the
      certified z-space state error (per-cell, infinity norm, a1:469)
      to consumer c's comparison space — declared
      sufficient-not-optimized (AG-1); A_c = 1 only when the consumer
      reads the state error directly in z-space. tol_min = the
      tightest such tolerance among consumers that are not
      NTF-proportional [ESC-r1-5: previously labeled
      "NTF-INDEPENDENT" — the cited carrier itself shows o31_tol
      drifting 4.1% across the ntf50 arm (0.07646 -> 0.07960), a
      solution-mediated drift; the honest label is "not
      NTF-proportional": no NTF factor in its formula, so it does not
      co-move. Consumers that ARE NTF-proportional — the O3.1 replay
      band at a1:1448 = 10*NTF*EPS*scale — re-price automatically and
      do not bind the UB]. Guarantees: a PASS delivers an error every
      consumer can absorb (NTF-2, repaired constant).

  (Window nonemptiness — the load-bearing compatibility condition)
      [ESC-r1-1/-2] 2 * (eta + 1) * kappa_eff,max * EPS * sc * A_c
      <= tol_c for every bound-side consumer c.
      On the record case, stated honestly [ESC-r1-2]: the certified
      error 2*(1+1/eta)*100*EPS = 7.99e-14 at eta = 1.25 (unit scale)
      lives in z-space, while o31_tol = 7.65e-2 (carrier
      s25bis_gap29_sweep.json) tolerances an O3.1
      DIRECTIONAL-DERIVATIVE agreement — a cross-space comparison
      licensed only through a declared A_c: the z-error reaches that
      consumer through the evaluation/differentiation chain, whose
      amplification the program's own record prices (registry row
      engine:cross-lowering-gradient-floor :328-336 [ADV], ~7-order
      FD amplification class). Even at that worst class (A_c = 1e7)
      the window stays open by ~5 orders (10^4.98, escalation probe;
      conservatively stated: >= 4 orders). The previously printed
      ">11 orders" headline was the undeclared-A_c = 1 reading and is
      RETIRED as a headline (it survives only as the A_c = 1 special
      case). The condition is stated because it is what a future
      tighter consumer (C35's xtol_u chain, C34's TR floor) must be
      checked against at composition time (C41 P-tag discipline).

Given NTF-1/NTF-2 as hypotheses AND the declared per-consumer A_c,
the window inequality is exact [THEOREM*, conditional on the declared
A_c — same star-discharge as NTF-2] [ESC-r1-2]. The DERIVED FORM of the
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
within the same decade as the floor — [ESC-r1-1] the argument
survives the repaired constant: 2*(eta+1) <= 7 < 10 across the
bracket, escalation probe), superseded by the measured
kappa_eff dispersion at duty time.

Incumbent adjudication: NTF = 100 is a VALID INSTANCE of the derived
form on the record case — measured headroom 100/70.110 = 1.426,
inside the declared bracket. The GAP-29 /2 flip is the model's
PREDICTION, not an anomaly [ESC-r1-12, witness restated
self-containedly]: the SELF-CONTAINED witness is the ntf50 arm's OWN
measurement, worst extra-step multiple 51.665 > 50 — FAIL required
by the arm's own data, with a 3.3% margin (the flip sits close to
the cliff, worth knowing at duty time); the cross-arm comparison
"50 < kappa_eff,worst ~= 70.1" (base arm) inherits NTF-1's declared
worst-cell-may-differ caveat, restated here at the point of use, and
is kept only as corroboration; the flip row retro-validates NTF-1
(one committed confirmation instance). The incumbent's own evidence class:
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
threshold T(z). [ESC-r1-3, claim SCOPED — the previous unconditional
conjunction was false inside the floor model itself, probe scene B]
Two regimes, split by a declared fluctuation margin m (declaration of
record: m = 0.25, sufficient-not-optimized, same class as the eta
lower edge; superseded by the measured per-trip fluctuation band at
duty time). [ESC-r2-1] The regime split CONSUMES one hypothesis
beyond H1-H4, stated explicitly as a hypothesis — H3 bounds the
noise from ABOVE only, so H1-H4 alone yield NO lower bound on the
realized per-trip step at ANY kappa_eff/NTF ratio (executable
counterexample of record, escalation probe scene C, re-run exit 0
this window: kappa_eff = 2*NTF, deep inside the regime at m = 0.25,
200/200 metric terminations at max 7 trips vs cap 30 and 87/200 cert
PASSes — both conjuncts of the previously unconditioned bullet fail
in an H3-consistent instance):
  H5 (fluctuation band; measured half = F2): per-trip realized steps
  at a converged cell lie within [floor_z/(1+m), floor_z]; m = 0.25
  declared sufficient-not-optimized, ratified or superseded by
  F2-NTF-TERMCOUPLE-TRIPCOUNT's measured band.
- DETERMINISTIC-ENVELOPE regime, kappa_eff(cell) >= (1+m)*NTF: UNDER
  H5 (whose lower edge gives realized step >= floor_z/(1+m) >= T(z)
  in this regime), metric-termination is unreachable at that cell —
  the loop exhausts N_NEWTON = 30 trips (C17's cap becomes the de
  facto terminator — silent per-cell cost inflation) AND the cell
  then fails certification (probe scene D, exit 0 this window:
  kappa_eff = 2*NTF under H5, 0/200 terminations with cap exhausted,
  0/200 cert PASSes — the conditioned claim HOLDS).
- NEAR-THRESHOLD band, NTF < kappa_eff(cell) < (1+m)*NTF: H3 is an
  ENVELOPE — it bounds ||delta||, it does not pin each per-trip
  realization; per-trip fluctuation can dip a step below T, giving
  EARLY metric-termination while a fresh certification sample still
  exceeds T at some cells — termination-in-few-trips probability and
  FAIL probability are BOTH nonzero (executable instance of record,
  probe scene B: T = 0.97*floor, 200 cells, 200/200 metric
  terminations at max 3 trips vs cap 30, 6/200 cert FAILs =>
  population FAIL). This fluctuation band is also the cleaner
  explanation of how the ntf50 arm carries worst ratio 1.033 while
  still terminating.
The LB in NTF-3 therefore protects BOTH contracts at once ([ESC-r2-1]
the termination-side protection read under H5); conversely
C17's trip cap is the only guard below the floor. The ntf50 arm
carries the FAIL signature; the trip-count signature was not recorded
by the sweep (the sweep json has no per-cell trip field; [ESC-r1-8]
its k_newt field, = 2 in all arms, is the THERMOTAB derived K_NEWT —
c1["K_NEWT"], sweep script :66 — NOT a march trip count) — claim held
at SCHEMA with its measured half named, not asserted.

Falsifier (NTF-4) [ESC-r1-3, RE-PINNED — the previous pin was
over-broad: it fired on data fully consistent with the floor model
(probe scene B), an armed spurious-retraction hazard]: refutation
requires trip-count instrumentation under the NTF sweep showing
metric-termination WITH MARGIN — steps consistently below
T*(1 - band) for a declared band ([ESC-r2-1] = precisely a measured
violation of H5's band) — at cells whose MEASURED kappa_eff
sits >= (1+m)*NTF (deterministic-envelope regime). Near-threshold
early termination alone refutes nothing (it is the model's own
fluctuation-band prediction). F2 duty, §5.

## 5. F2 duties (measured halves, NAMED — nothing executed here)

- F2-NTF-FLOOR-POPULATION: per-cell kappa_eff measurement
  (converged-cell extra-step probes + ECNoise/Moré-Wild-class noise
  floor + float32 precision contrast for the EPS*sc scale law) across
  production marches; quantile + eta ratification; RIDES
  F2-C20-CERTQUAL-CAMPAIGN Tier-1 (window shared with C18 per
  VERDICT_wave2 §2.8 — no new window minted; the four-rider/one-owner
  discipline of VERDICT_wave3 §7.2 preserved). [ESC-r2-3] The duty
  PINS ONE operational kappa_eff: the REALIZED per-cell extra-step
  multiple (whose declared upper quantile is NTF-3's kappa_q — the
  object LB, the falsifier, and the measured bracket [51.7, 70.1]
  already use); H5's band CONVERTS realized -> envelope
  (envelope <= realized*(1+m)) wherever the NTF-4
  deterministic-envelope scoping needs the envelope object — so the
  measured worst 70.110 is a LOWER estimate of that cell's envelope
  kappa (<= 87.6 at m = 0.25), and LB (measured object) and the
  NTF-4 regime split (envelope object) never silently use the same
  symbol for two numbers up to (1+m) apart.
- F2-NTF-TERMCOUPLE-TRIPCOUNT: trip-count instrumentation under the
  NTF sweep (NTF-4 falsifier AS RE-PINNED [ESC-r1-3]: margin-scoped,
  deterministic-envelope cells only; the duty also records the
  per-trip fluctuation band that ratifies or supersedes H5's band
  and its m = 0.25 [ESC-r2-1]).
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
  NTF-2 [ESC-r1-1/-4/-9/-10]: two-sided certificate semantics, PASS =>
    error <= 2*(T+floor) = 2*(NTF+kappa_eff)*EPS*sc <=
    2*NTF*(1+1/eta)*EPS*sc — THEOREM* on the repaired constant
    (geometric-series bound cf. Deuflhard (2.10)-(2.14) [ESC-r2-2] +
    Yamamoto eq.(7) composed with NTF-1; star discharges on F2 floor
    measurement; threshold object T distinct from certified-error
    object 2*(T+floor))
  NTF-3 [ESC-r1-1/-2/-5/-12]: window bound eta*kappa_max <= NTF with
    2*(1+1/eta)*NTF*EPS*sc*A_c <= tol_c per consumer — THEOREM* given
    NTF-1/2 AND declared A_c (conditional); derived form NTF =
    eta*kappa_q — SCHEMA; record window open ~5 orders at worst
    A_c = 1e7 class (>= 4 conservative; old ">11 orders" = A_c=1
    reading, retired as headline); incumbent 100 = valid instance
    (headroom 1.426); GAP-29 /2 flip = model prediction, witness =
    ntf50's own 51.665 > 50 (3.3%), retro-validation
  NTF-4 [ESC-r1-3/-8, ESC-r2-1]: termination/certification
    same-threshold coupling — SCHEMA, SCOPED and CONDITIONED on the
    EXPLICIT hypothesis H5 (fluctuation band [floor_z/(1+m), floor_z],
    m = 0.25 declared; measured half = F2 trip-count duty):
    unreachability only at kappa_eff >= (1+m)*NTF UNDER H5 (probe
    scene D confirms; scene C shows H1-H4 alone never imply it);
    near-threshold band = fluctuation regime (early termination +
    FAIL both possible, probe scene B); falsifier re-pinned
    margin-scoped (= measured H5-band violation); trip-count measured
    half named; operational kappa_eff pinned realized-quantile with
    H5 converting to the envelope object [ESC-r2-3]
  NTF-5 (seam, §0) [ESC-r1-9]: theory half of the ONE C18/C20-Tier-1
    window; floor_W := NTF*EPS*sc consumed by C34/C35 unchanged
    (threshold object, NOT the certified-error object) — PRACTICE
f2_duties: [F2-NTF-FLOOR-POPULATION (rides F2-C20-CERTQUAL-CAMPAIGN
  Tier-1, shared C18), F2-NTF-TERMCOUPLE-TRIPCOUNT, gate-REFORM
  (pre-existing, out of scope here)]
escalation_candidates: none from author side
papers_needed: [Higham ASNA 2ed (conditional), Moré-Wild ECNoise
  (already filed wave-3, deduplicated)]

## 9. ESCALATION ROUND 1 DISPOSITIONS [ESC-r1] (append-only; E-1 per
## VERDICT_blocco2 §3; inputs = refute_minor_ntf.md + VERDICT_blocco2
## §2.1; every named repair VERIFIED before adoption: refuter probe
## r22f_v2_probe_minor_ntf_pass_bound_and_termination.py re-run exit 0
## this window + esc_probe_ntf_repaired_bound_window.py 16/16 exit 0)

| Finding | Class | Disposition | Where applied | Verification |
|---|---|---|---|---|
| MIN-NTF-1 | CONTENT | APPLIED — PASS constant 2*T replaced by 2*(T+floor) = 2*(NTF+kappa_eff)*EPS*sc <= 2*NTF*(1+1/eta)*EPS*sc; "absorbed" parenthetical struck (it inverted the triangle inequality); propagated into NTF-2 falsifier threshold, NTF-3 UB + window condition, eta upper-edge decade argument (2*(eta+1) <= 7 < 10), §8 | §2 [ESC-r1-1] (composition + falsifier), §3 [ESC-r1-1] (UB, window, eta bracket), §8 | probe scene A re-run (3.401*T > 2*T rejects old; <= 3.6*T confirms new); esc probe R1/R2 |
| MIN-NTF-2 | CONTENT | APPLIED — UB restated per-consumer with declared transfer factor A_c (AG-1 sufficient-not-optimized); record case restated cross-space-honest: ~5 orders open at worst A_c = 1e7 class (10^4.98; conservative claim >= 4 orders — refines the refuter's "~4 orders", probe-measured), ">11 orders" retired as headline (A_c = 1 special case); window inequality THEOREM* now explicitly conditional on declared A_c (judge guidance adopted) | §3 [ESC-r1-2] | esc probe R3 (margin 10^4.98; old headline reproduced only at A_c=1) |
| MIN-NTF-3 | CONTENT | APPLIED — NTF-4 conjunction SCOPED to deterministic-envelope regime kappa_eff >= (1+m)*NTF, m = 0.25 declared; near-threshold band stated as fluctuation regime (both probabilities nonzero; also explains ntf50's 1.033-yet-terminating); falsifier RE-PINNED margin-scoped (old pin fired on model-consistent data — spurious-retraction hazard disarmed); F2 duty extended to record the fluctuation band | §4 [ESC-r1-3], §5 duty line, §8 | probe scene B re-run (200/200 terminations, 6/200 FAILs at T = 0.97*floor); esc probe R4 (0.97-regime inside band at m = 0.25) |
| MIN-NTF-4 | WORDING | APPLIED — 1/(1-Theta) form re-attributed as geometric-series consequence of uniform contraction (cf. Deuflhard (2.8)-(2.14)); (2.14)'s literal denominator 1-Theta^2_{k-1} stated; Yamamoto eq. (7) upper half named as the two-sided alternative | §2(a) [ESC-r1-4] | esc probe R1 (series sums to 1/(1-Theta) <= 2 at Theta = 1/2); source read of record (refuter §2, verified verbatim) |
| MIN-NTF-5 | WORDING | APPLIED — "NTF-INDEPENDENT" replaced by "not NTF-proportional" with the measured 4.1% solution-mediated drift declared (0.07646 -> 0.07960 across the ntf50 arm, cited carrier) | §3 UB [ESC-r1-5] | esc probe R5 (drift = 4.1%) |
| MIN-NTF-6 | WORDING | APPLIED — kappa_eff := \|\|J^{-1}\|\|*gamma_R*S_R/sc, dimensionless; garbled "(EPS-normalized sc)" removed; EPS appears once, in the floor formula; measured arithmetic unaffected (never used the symbolic form) | §1 [ESC-r1-6] | dimensional check: floor_z = kappa_eff*EPS*sc consistent with \|\|J^{-1}\|\|*gamma_R*EPS*S_R |
| MIN-NTF-7 | NOTE | APPLIED — H1 citation extended to (A.30)-(A.31), storage vs per-operation named, pp. 614-615 | §1 H1 [ESC-r1-7] | source verified at PDF 633-634 (refuter §2, of record) |
| MIN-NTF-8 | NOTE | APPLIED — k_newt identity parenthetical added (thermotab K_NEWT, c1["K_NEWT"], sweep script :66 — not a trip count) | §4 [ESC-r1-8] | refuter verification of record (sweep script :66) |
| MIN-NTF-9 | NOTE | APPLIED — one disambiguating passage: threshold object T = floor_W (C34/C35 consumption, unchanged) vs certified-error object 2*(T+floor) (strictly larger); restated in §8 NTF-5 line | §2 [ESC-r1-9], §8 | rides MIN-NTF-1 (esc probe R1) |
| MIN-NTF-10 | NOTE | APPLIED — c_L >= 2/(1+sqrt(2)) ~= 0.828 recorded at the citation; 1/2 kept valid-conservative; ~1.66x free tightening flagged to the F2 duty window | §2(b) [ESC-r1-10] | esc probe R6 (0.828, > 1/2) |
| MIN-NTF-11 | NOTE | APPLIED — H2 checkability restated honestly: "contraction data the F2 probes will record" (no per-cell Theta in the current record, a1:793-828) | §1 H2 [ESC-r1-11] | refuter record check of record (a1:793-828, sweep adds none) |
| MIN-NTF-12 | NOTE | APPLIED — retro-validation witness restated self-containedly on ntf50's own 51.665 > 50 (3.3% margin, cliff proximity stated); cross-arm 70.1 comparison demoted to corroboration with the worst-cell caveat restated at point of use | §3 incumbent [ESC-r1-12] | esc probe R5 (51.665 > 50; margin 3.3%; headroom 1.426 in bracket) |

DISPOSITION TOTALS: 12/12 sustained findings APPLIED (3 CONTENT, 3
WORDING, 6 NOTES); 0 deferred, 0 declined. Deviations from the named
repair texts (declared): (i) MIN-NTF-2 record-case margin stated as
~5 orders (10^4.98, probe-measured) rather than the refuter's "~4
orders" — the conservative ">= 4 orders" clause is kept so the
refuter's claim form survives verbatim as a lower bound; (ii) m =
0.25 chosen as the declared fluctuation margin (the refuter left m
free) — sufficient-not-optimized, same class as the eta lower edge,
superseded at duty time. Judge guidance (non-adopted labels) is
CONSISTENT with the result: NTF-2 THEOREM* recovered on the repaired
constant; NTF-3 window THEOREM* now conditional-on-declared-A_c;
NTF-1/NTF-4 SCHEMA stand with the MIN-NTF-3 scoping; architecture
(floor model + two-sided semantics + window form + seam position)
untouched, as the refuter's §4 HELD list predicted. Incumbent
adjudication lands unchanged (100 = valid instance, headroom 1.426;
/2 flip = model prediction). Probes of this round:
esc_probe_ntf_repaired_bound_window.py (this file's escalation probe,
exit 0) + re-run of the refuter probe (exit 0). PAPERS NEEDED: none
new (Higham conditional entry unchanged, already deduplicated in
VERDICT_blocco2 §8).

## 10. ESCALATION ROUND 2 DISPOSITIONS [ESC-r2] (append-only; inputs =
## esc_refute_ntf_r1.md, all findings addressed; repairs VERIFIED
## before adoption — probes re-run exit 0 THIS window:
## esc_probe_ntf_r1_envelope_lower_bound.py scenes C+D,
## esc_probe_ntf_repaired_bound_window.py 16/16,
## r22f_v2_probe_minor_ntf_pass_bound_and_termination.py scenes A+B)

| Finding | Class | Disposition | Where applied | Verification |
|---|---|---|---|---|
| ESC-NTF-r1-1 | REPAIR | FIXED — the refuter's named one-sentence repair adopted: H5 (fluctuation band, [floor_z/(1+m), floor_z], m = 0.25 sufficient-not-optimized, measured half = F2-NTF-TERMCOUPLE-TRIPCOUNT) stated EXPLICITLY as a hypothesis beyond H1-H4; the deterministic-envelope bullet CONDITIONED on H5 ("UNDER H5, metric-termination is unreachable ... AND fails certification"); scene-C counterexample cited in-text as the reason H1-H4 alone never imply the bullet; everything the refuter listed as surviving kept verbatim (regime split, m declaration, near-threshold text, re-pinned falsifier — now explicitly = measured H5-band violation — F2 duty as extended, SCHEMA label, LB-protects-both with H5 read into it) | §4 [ESC-r2-1] (H5 + conditioned bullet + falsifier tie), §5 duty line, §8 NTF-4 | probe scene D re-run exit 0 this window: kappa_eff = 2*NTF under H5, 0/200 terminations (cap exhausted), 0/200 cert PASSes — conditioned claim HOLDS; scene C re-run: 200/200 terminations, 87/200 PASSes — unconditioned form stays rejected |
| ESC-NTF-r1-2 | NOTE | FIXED — both residues: (i) Deuflhard cite span opened at (2.10) (first display ON the declared read pages pp. 51-52; p. 52 only REFERENCES (2.8), stated in-text) — span-narrowing chosen over extending the read declaration (no new read claimed); (ii) "equivalently" RETIRED: Yamamoto eq. (7) restated as a two-sided display whose upper half bounds the PREVIOUS correction at source, yielding the current-correction form only after an index shift plus one triangle step; geometric-series attribution declared primary and load-bearing alone | §2(a) [ESC-r2-2], §8 NTF-2 | refuter's source verification of record (pp. 51-52 display (2.10)-(2.16); eq. (7) upper half previous-correction) — no new math, attribution-only touch; no probe applicable |
| ESC-NTF-r1-3 | NOTE | FIXED — the duty-time definitional sentence written NOW into the duty that owns it: F2-NTF-FLOOR-POPULATION pins ONE operational kappa_eff = REALIZED per-cell extra-step multiple (upper quantile = kappa_q, the object LB/falsifier/bracket already use); H5's band converts realized -> envelope (envelope <= realized*(1+m)); measured worst 70.110 stated as a LOWER estimate of that cell's envelope kappa (<= 87.6 at m = 0.25); the refuter's "nothing false today" confirmed — no body statement needed rewording, the reconciliation lives in the duty as the note prescribed (rides the two named F2 duties) | §5 [ESC-r2-3], §8 NTF-4 tail | arithmetic check: 70.110*(1+0.25) = 87.6375 (~87.6, matches refuter); internal-consistency claim (falsifier + derived form pinned to the MEASURED population) re-checked against §3 — holds |

DISPOSITION TOTALS: 3/3 round-1 findings FIXED (1 REPAIR, 2 NOTES);
0 CONTESTED, 0 deferred, 0 declined; breaks in round 1: 0 (nothing
else owed). Deviations from the refuter's named texts: NONE of
substance — H5 adopted in the refuter's own wording; (i) resolved by
span-narrowing (the refuter offered two options; the no-new-read
option chosen and declared); (iii)'s duty sentence placed in
F2-NTF-FLOOR-POPULATION (the kappa-owning duty) with the trip-count
duty riding via H5. The refuter's §1 verified-sound record (11/12 +
the [ESC-r1-3] falsifier half) is untouched by this round: no
[ESC-r2-*] marker rewrites any [ESC-r1-*] repair text — round 2 only
adds the H5 hypothesis, two attribution touches, and the operational
kappa_eff pin. Seam (§0): untouched again this round (no marker in
§0); C34/C35 consumption unchanged. Rigor labels unchanged by round 2
(NTF-4 stays SCHEMA, now honest per the refuter: "honest once H5 is
explicit"). PAPERS NEEDED: none new (unchanged).
