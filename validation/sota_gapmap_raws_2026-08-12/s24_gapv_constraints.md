# FACET 5 — CONSTRAINT MACHINERY: adversarial verification (S24)

Verifier of the finder position `s24_gap_constraints.md`. Method: every anchor
re-read at source (`margin_governor.py`, `def_twin_falsifier.py`,
`a1_toc_variational_jax.py`, `PROGRESS_2026-08-12_S24_f1b.md`, D6, M0 S20 block,
`ADVISORY_S24_DEbucket_panel_2026-08-12.md`); the finder's probe script
`scratchpad/probe_constraints.py` RE-RUN by me (pure numpy, < 5 s, no march, no
interaction with the running campaign) — all P1/P2/P3 numbers REPRODUCE exactly
(one-hot 1/45 lanes, tie-jump 2.875e-2, rho/4 = 1.438e4; |mu·m| = 3.5509e3;
affinity residuals 2.665e-15 / 1.421e-13). Coverage checked against: D6 duty
rows (F1/F1b/F2 blocks + gate table), the S24 T0 census rows 1-20 in the session
log, M0 S20-S24 registration blocks, and the S24 DE-bucket panel's named
conditions C1-C10 + non-blocking residuals.

**Counts: 6 CONFIRMED, 2 DOWNGRADED, 0 REFUTED.**

---

## G1 (KS rho: conservativeness-only derivation) — DOWNGRADED, severity MEDIUM

Verified: derivation anchors real (`margin_governor.py:25-29`, `:281-283`;
`def_twin_falsifier.py:756-757`; PROGRESS step 9 rho = 5.7518e+4, N = 45,
m_ref = 4.2357e-3 — all of record). Probe P1 re-run: reproduces bit-for-bit.
The math is right: the derived rho pins ln(N)/rho only; gradient support and
curvature rho/4 are uncontrolled consequences; the mild instance is smooth,
the deep instance is a hard min. SOTA attributions real (Poon–Martins SMO 2007;
Kennedy–Hicken CMAME 2015; K-S 1979; Raspanti et al. 2000).

DOWNGRADE GROUNDS (prior coverage, two documents of record):
1. The S24 panel advisory ALREADY NAMES the argmin-tie chatter at this exact
   rho as a non-blocking residual: "TR-SQP chatter near KS ties at
   rho = 5.75e4: a budget risk inside the [P4] cap, not an unsoundness (E3) —
   monitor wall time per rung against the anchor"
   (`ADVISORY_S24_DEbucket_panel_2026-08-12.md:269-270`). The finder's E2
   extremal case presents this as undeclared; it is declared and owned
   (monitoring duty).
2. M0's S20 taxonomy block already registers "adaptive-parameter variants
   exist and are the current refinement" (`rde_nozzle_MASTER.md:1636-1637`) —
   the adaptive-KS lineage is on record as the named refinement, so "the wrong
   theorem was cited against the right technique" overstates the survey defect:
   the record holds both the NOT-ADOPTED reason and the refinement pointer.

WHAT GENUINELY SURVIVES (the downgraded finding): the rho DERIVATION itself
carries no curvature/weight-support budget and its instance sensitivity
(mild = genuine aggregate, deep = hard min) is declared NOWHERE in the
derivation text — the panel named the symptom, not the derivation defect. The
proposed two-constant derived rule is R5-conformant and uncovered by any duty.

Minor factual slips (immaterial to the conclusion): the probe's S22 inputs use
N = 3059 while the S22 record (rho = 766.83, gap 1.0641e-2) implies N ≈ 3496;
m_ref = 0.68103 confirmed (ladder rung 1 = 3.4051e-1). Recomputing at N = 3496
gives ~21 weighted lanes instead of 18 — same conclusion. Also the "exactly ONE
lane carries weight" claim rests on the probe's MODELED uniform lane spacing
(declared conservative), not a readout of the measured S24 field; the
conclusion is robust (any lane > 4.8e-4 above the min has weight < 1e-12) but
should be worded as model-inferred.

---

## G2 (rung-frozen chain mask granularity) — CONFIRMED, severity MEDIUM

Verified at source: freezing declaration `def_twin_falsifier.py:487-490`
("built at each RUNG START ... FROZEN across the rung's segments"); rung build
`:945-954`; C3 gate `:1000-1029` (drift_idx, drift_val, repeat-once, CONFOUNDED
semantics). Measured firing verified in PROGRESS step 12 verbatim: i_cross
96 -> 82 (14 nodes, 2.465e-1 position, kernelward), frozen-vs-rederived
val_min delta 9.188e-3 vs mu0 = 2.1178e-3 (4.34x the floor), C3 repeat COUNTED
AS DECISIVE RUN 2 (budget consumed). The plan-vs-mask granularity asymmetry is
real: `a1_toc_variational_jax.py:41-48` re-records the plan at every P2
acceptance (`:1135-1176` verified), and the mask is the only W-dependent frozen
object outside that rhythm (the per-segment `margin_factory(plan, Dv)` call at
`:1180` receives the FRESH plan but the factory closure holds the RUNG mask).

Coverage check: the panel's C3 (advisory `:219-226`) ratified rung-freeze +
re-freeze-once + the drift detector; NO position considered segment-level
re-freeze or a differentiable gate — the C3 firing is post-adjudication
measured evidence. Not covered by any D6 duty or census row. Gap stands.

CAVEATS (do not refute, must accompany the finding): (i) "the record is
already computed — marginal cost ≈ one chain walk" is right on compute but
understates the interface change: the factory signature (plan, Dv) does not
receive the segment-base record, so segment re-freeze needs a
driver-interface extension — under the S21 no-driver-work pin that makes BOTH
legs (not only the smooth gate) F2-owned; (ii) severity is MEDIUM not HIGH:
the stale floor never bound (margin inactive by 33x at the stop), so no
recorded verdict number changes; the measured cost is budget (one decisive
run) and attribution machinery, both already honestly recorded.

---

## G3 (mask crop can silently drop enforced lanes) — CONFIRMED, severity MEDIUM

Verified at source: `def_twin_falsifier.py:618-625` — `mm[:r,:c] =
mask[:r,:c]` with r, c = min over shapes: a True lane beyond the overlap is
discarded; `:640` `n_sel = max(int(mloc.sum()), 1)` and `:648` frac_bad both
use the CROPPED count, so the lost lane exits numerator AND denominator —
neither enforced nor penalized nor counted. 16 shape adaptations in decisive
run 2 verified of record (PROGRESS step 13(a): "16 mask shape-adaptations
across segments, COUNTED, declared"). The counter records occurrence, not
enforcement loss — the finder's distinction is exact.

Coverage check: the panel's non-blocking residual ("per-rung shape-adaptation
counters ... adequate, keep — 0 events measured at derive", advisory
`:267-268`) adjudicated counter GRANULARITY at a point where 0 events existed;
the conservation-of-enforcement invariant is nowhere. Panel C4's "lane-count
(N_DE) drop is a declared adjudication item" covers the re-derived bucket
size, not the in-walk crop. The one-line fix (log `mask.sum() - mloc.sum()`,
nonzero = verdict-bearing per the `margin_governor.py:47-50` counter pattern)
is correctly scoped. Severity MEDIUM, not HIGH: the F4 margin-inactive reading
comes from re-derived `cs_stats` at the returned base (not the frozen mask),
and enforcement loss can only weaken an already-inactive-by-33x constraint at
this instance — no recorded number at risk; it is a counted-but-unbounded
event inside decisive-run machinery, against the repo's own C4/C5 standard.

---

## G4 (lip equality as constraint row vs elimination) — CONFIRMED, severity LOW

Verified at source: `a1_toc_variational_jax.py:887-888` (single-entry A row),
`:1072` (`lip_eq = LinearConstraint(A * Dv[None,:], [yL], [yL])`), docstring
`:16-17`; raw multiplier consumption `:1603` (`lam = res.v[0]...`) feeding
Pa_impl `:1604`, and `margin_governor.py:415-419`. The technical claims are
correct: one pinned coordinate; trust-constr runs its equality-constrained
path every iteration for it; elimination + AD post-optimality sensitivity
(lambda_e = dJ*/dy_L with an O3.1-style FD check) would source the multiplier
from the repo's own adjoint machinery. SOTA correct (Nocedal–Wright
elimination; Fiacco sensitivity). The finder correctly does NOT claim the
S24-T1 verdict is wrong (it stands of record) and correctly assigns owner F2
(driver surgery, S21 pin). No duty/census coverage found. Severity LOW:
structural efficiency + provenance upside; measurable but small at 9 dof; no
recorded number affected.

---

## G5 (no independent multiplier rejector) — CONFIRMED, severity MEDIUM

Verified at source, all three consumption sites: `a1_toc:1603` raw;
`margin_governor.py:536-542` — `except Exception: pass` leaves mu_est = None,
and `:556-558` converts that (when margin_active) into mu_use = 0.0 with no
counter, exactly as claimed (the nonfinite-counter pattern at `:47-50` exists
and is not applied here); `def_twin_falsifier.py:1033-1040` (S24-T1
convention, correct). PROGRESS step 13(d) verified: mu = +4.8582e4 read at
min DE val 7.31e-2 (33x floor), demoted BY HAND to information-only. Probe P2
re-run: |mu·m| = 3.5509e3 (rel 8.77e-5 vs J ~ 4.05e7, orders above gtol
scale) — a derived complementarity band fires on precisely the case the hand
caught. Driver termination check verified at `a1_toc:1203-1207`: stationarity
(res.optimality) + feasibility (res.constr_violation), complementarity never —
the IPOPT three-part contrast is accurate. SOTA correct (Gill–Murray–Wright
1981 LSQ estimates; Wächter–Biegler 2006).

Coverage check: census row 1 (T1) closed the CONVENTION only — no duty, gate,
or conditional anywhere requires machine verification of a consumed
multiplier; R5 ("every consumed number needs a rejector") is the finder's
correct standard. Severity MEDIUM: verdict-adjacent consumers exist ([D1]-
constrained rel_c is a kill-rule metric; Pa_impl of record) but no recorded
number is currently wrong — rel_c runs only at outcome-I margin-active (never
yet reached) and the S24 barrier artifact was caught and demoted of record.

---

## G6 (missing shape-constraint classes) — DOWNGRADED, severity MEDIUM

Verified: docstring anchor real (`a1_toc:18-20`, monitors declared not
enforced); R-G1 broken-design probe real (`margin_governor.py:331-334`); S24
fencing of record (rejected trial records worst 1e1..1e7 run 1, 5.0e0..3.4e5
run 2). Probe P3 re-run: affinity residuals at machine floor — the
slope/curvature-are-LinearConstraint-rows-at-fixed-thB consequence is
mathematically sound, and the conservative per-segment linearization for the
thB coupling matches the established RK-G rhythm.

DOWNGRADE GROUNDS (one SOTA half collides with a prior adjudication of
record): D6's S20 residue-(a) survey decision (`rde_nozzle_development_
plan.md:915-926`) explicitly REJECTED "a control-point B-spline basis switch"
with declared reasons (re-validating the entire certified stack; the measured
defect is knot PLACEMENT, not parametrization conditioning). The finder's
"B-spline control points would make slope/curvature bounds sufficient
conditions" is presented as an open NOT-SOTA data point; as a basis-switch
lever it is CLOSED of record — the finder's own D6 anchor (`:909-916`) reads
past the rejection three lines below it. What survives untouched by any prior
adjudication: station-sampled linear rows in the EXISTING clamped-natural
spline class (probe-proven affine), which is the finding's operative half.

Second correction: the efficiency claim ("would have converted part of the
S24 fencing into never-proposed") is unmeasured and plausibly small — the S24
rejections are CERTIFICATION failures at healthy val (F4 of record), and no
evidence shows the rejected trials violated slope/curvature sanity; the
finder's own E1 hedges "some fraction". The gap itself (INCOMPLETE:
feasibility structure exists, is probe-proven linear, and is not offered to
the SQP; broken designs priced by full adaptive marches) is genuine, uncovered
by any duty/census row, and P4-gate-preserving as framed. SOTA remainder
correct (Kulfan 2008; Masters et al. AIAA J 2017; the interpolating natural
cubic genuinely lacks the convex-hull property).

---

## G7 (certification frontier invisible to the KKT system) — CONFIRMED
(attribution corrected), severity HIGH

Verified at source, every anchor: binary gates `a1_toc:935-938` (P4 base) and
`:1158-1161` (P3(ii)); outcome-II return `:1000-1023`; traced per-lane ratio
`_ratio`/`_chain_ratios` `:682-700`, cert_diag worst `:807-809`, and — checked
independently — cert_diag is consumed ONLY at `:1458` (a diagnostic
CHECK; no constraint, no gate input beyond pass/fail), exactly as claimed;
margin_factory slot `:1179-1182`; rejected-designs persistence `:904-911`
(A1_REJ_SAVE). Measured record verified: three campaigns certifiability-
limited (S20 crawl; S22 branch (c); S24 runs 1-2 with KKT open at 1.417e6 /
~1.6e6, 19 / 21 segments of frontier fencing) and the F4 operative verdict
names march certification at healthy val as the binding frontier — all of
record in PROGRESS steps 12-13.

ATTRIBUTION CORRECTION (strengthens the gap, corrects the framing): the
Le Digabel–Wild taxonomy anchor is NOT missing from the record — M0's S20
block (`rde_nozzle_MASTER.md:1624-1637`) already registers it FOR THIS EXACT
CONSTRAINT ("the certifiability constraint is TODAY of class Known-
Unrelaxable-Simulation-NONQUANTIFIABLE ... the recognized remedy ... is to
QUANTIFY a margin") and adopted the margin-constrained reformulation as that
quantification, under the registered CONJECTURE "K_disc approximates A_0" with
its named falsifier. That bridge was then FALSIFIED of record (S22; third
instance S24/F4). So the true state of record is: the program's REGISTERED
quantifier of the certification frontier is dead, and NO successor quantifier
exists anywhere — census row 10 (C1 field-level rejector, F2) is a rejector,
and "near-axis mechanism identification" (F2 first item) is diagnosis; neither
is a differentiable in-KKT surrogate. The finder's proposal (KS over the
existing traced `_ratio` lanes as one more NonlinearConstraint, delta derived
from the persisted rejected-walk artifacts, P4/P3(ii) gates untouched — the
[X-MGOV] G1 surrogate-inside/gate-outside precedent) is the first named
successor. Owner F2 is correct (S21 no-driver-work pin).

Implementation caveats found at source (must be declared, do not refute):
(i) cert_diag and val_diag are MUTUALLY EXCLUSIVE by construction
(`a1_toc:576-577`) — a cert row alongside the margin row needs a combined
diag mode or a second jit replay per segment (engine edit, compile/memory
cost); (ii) the driver exposes ONE margin_factory slot — stacking cert into
the same NonlinearConstraint as a vector-valued constraint avoids driver
surgery, a separate row does not. Severity HIGH: this is the formulation gap
that determines whether outcome-I (KKT-closed) verdicts are producible at all
at frontier instances — the program's central deliverable class — and it is
the measured binding mechanism of three recorded campaigns; no recorded
number is invalidated (outcome-II exits are honest as written).

---

## G8 (margin constraint ships jac but no hess) — CONFIRMED, severity MEDIUM

Verified at source: `a1_toc:1181-1182` — `NonlinearConstraint(m_np, 0.0,
np.inf, jac=gm_np)`, no `hess=`; scipy's NonlinearConstraint default is
BFGS() (scipy 1.18 signature — confirmed knowledge of the interface, and the
finder's contrast object is real: the OBJECTIVE gets a measured exact Hessian
per segment, `:1074-1097`, with the fresh-BFGS-per-segment policy wording at
`:859-862`). The S18 R-3 precedent analogy is exact: the same
BFGS-quality-curvature plateau mechanism, repaired on the objective half only.
The scale argument is P1-verified (rho/4 = 1.438e4 at the S24 rho). The
proposed fix (JAX forward-over-reverse HVP or the existing
FD-of-exact-gradient recipe `:1088-1094` applied to gm, measured per segment
base) is policy-conformant as claimed. No duty/census coverage found.
Severity MEDIUM with a declared boundary: at every recorded instance the
margin was INACTIVE (S22; S24 33x floor), so the missing hess has had ZERO
recorded effect — the gap pays only in the margin-active regime that H-CLASS
says tier-0 never reaches; it is real for enriched classes/F2+, vacuous for
the recorded record.

---

## Drop-list audit (5 drops — all legitimate)

Spot-checked: #1 log-floor 1e-300 (`margin_governor.py:198`) — unreachable
with n_fin > 0 (min lane contributes exp(0) = 1, sum >= 1) and both branches
finite/grad-safe under the double-where; drop correct. #3 monotonicity stop —
derivation printed at `:575-583`, correct for a lower-bound ladder. #5 G1
continuity at frac_bad = 0 — where-structure holds (ks_part -> exact KS,
penalty term -> 0). #2 and #4 defer to the panel C4 declaration and the
S24-T1 read respectively — both of record. No dropped item should have been
kept.

## Verdict summary

| Finding | Verdict | Severity | One-line ground |
|---|---|---|---|
| G1 KS rho conservativeness-only | DOWNGRADED | MEDIUM | chatter risk already a named panel residual + M0 names adaptive variants; derivation-side curvature budget genuinely uncovered |
| G2 rung-frozen mask granularity | CONFIRMED | MEDIUM | C3 firing measured of record, cost run 2; segment re-freeze never adjudicated; interface caveat (F2-owned both legs) |
| G3 crop drops enforced lanes | CONFIRMED | MEDIUM | code verified; counted event is unbounded; panel residual covered granularity only |
| G4 lip equality not eliminated | CONFIRMED | LOW | structural; correct SOTA; F2-owned; no record impact |
| G5 no multiplier rejector | CONFIRMED | MEDIUM | raw res.v consumption + silent except-pass verified; P2 fires on the hand-caught case; T1 closed convention only |
| G6 missing shape constraints | DOWNGRADED | MEDIUM | linear-rows half probe-proven and uncovered; B-spline half collides with D6 S20 rejection of record; fencing benefit unmeasured |
| G7 cert frontier outside KKT | CONFIRMED | HIGH | mechanics verified; taxonomy already in M0 (attribution corrected); registered quantifier falsified of record, no successor — gap stands stronger |
| G8 no constraint hess | CONFIRMED | MEDIUM | interface verified; R-3 analogy exact; zero recorded effect (margin never active) — pays only at margin-active regime |
