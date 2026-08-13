# S24 GAP POSITION — FACET 2: CELL SOLVER + CERTIFICATION (FINDER: cell-cert)

Scope: per-cell Newton unit process + certification metric; basin-of-attraction at
extremal states; early-abort; cert_diag formal status; wall-foot search robustness.
Sources read whole: a1_ideal_march_jax.py (1360 ln), a1_toc_variational_jax.py
(1-1009 + grep), a1_march_scan.py (1-260 + solver factory), thermotab_c1_jax.py
(431 ln, whole), certdiag_kat.py (1-120), def_twin_falsifier.py (targeted grep),
margin_governor.py (targeted grep); docs: M0 S23 block (X-TBAK, ln 1832-1884),
theorem ledger U3 (DWR, ln 681-685), D6 item 9 (ln 881-923), brick2 kickoff.

PROBES RUN (declared, scratchpad/probe_cell_cert.py, total 5.9 s CPU, one JAX
import; nothing heavier launched — S24 campaign respected):
- P1 table-edge clamp (gconst backend, closed form as oracle);
- P2 branch-blindness + conditioning of the one-extra-step certificate at a
  near-fold quadratic (pure numpy analytic);
- P3 certificate-scale arithmetic (analytic).

HONESTY PREAMBLE: the per-cell certification, rejector culture, derived
tolerances and RK-G determinism are the strongest part of this codebase (the
S21 C2-F1/C2-F2 hardenings, the S20 reject-and-shrink, the [X-CDKAT] KAT are
genuinely above common practice). Every finding below names something MISSING
or SUBOPTIMAL on top of that stack, never a weakening.

---

## F1. Table-domain validity is unguarded per cell; past the edge the closure
## clamps silently and the adjoint goes exactly dead — {RIGOR-GAP}

**Cite:** `validation/a1_ideal_march_jax.py:349-356` (`state_q`: `jnp.interp`
clamps `ht -> T` at the table ends, constant extrapolation);
`validation/thermotab_c1_jax.py:143-146` (`_locate` clips i to n-2, t
unbounded => END-SEGMENT QUINTIC EXTRAPOLATION past the edge),
`:189-197` (`invert_h`: 8 fixed trips, clamped linear seed, no domain check).
The G>0 audit box "contains every march-realized state" is DECLARED
(`thermotab_c1_jax.py:31-33`) and never enforced or even monitored per run.

**Measured (P1, gconst oracle):** at q only 2% past the edge-equivalent speed,
`state_q` returns T = 1050.00 K vs exact 946.98 K (error 103 K, ~10% of state)
with **dT/dq = 0.0 exactly** (dead adjoint lane); at 10% past, error 536 K,
still silent, M reported 5.06. The per-cell certificate CANNOT see this: the
residual system is self-consistent with the clamped closure, so the cell
certifies against wrong physics and the vjp silently zeroes the thermo branch
of dJ/dW.

**SOTA reference:** guarded-domain evaluation with sticky validity flags +
rejector (IEEE-754 exception-flag discipline; NAG/DLMF domain-guard practice);
the repo's own interval substrate ([X-IVXC], Krawczyk, outward rounding —
`claims_registry.yaml:1695`) is the in-house lineage for an enclosure-grade
guard. Minimum honest fix class: per-run min/max distance-to-edge monitor in
the cert dict + rejector at zero margin (same pattern as the axial-margin
rejector `a1_toc_variational_jax.py:227-237`).

**Extremal exposures:** (a) eps -> 100+ (high Me drives static T below
T_TAB_LO = 1050 K — P1 shows the regime is reachable ~M 4.6 at gconst values);
(b) deep-DEF / very short L twin at high lip Mach with hot-H2 tables (edge on
the h side); (c) gconst-oracle probes at q > 3385 m/s certify wrong closed
forms. **Everyday case:** eps = 4 baseline — sits inside, but the MARGIN to
the edge is never reported, so no one can say by how much.

---

## F2. The one-extra-Newton-step certificate has no conditioning
## qualification: near a fold it BOTH false-fails and false-passes
## (branch-blind) — {RIGOR-GAP}

**Cite:** `validation/a1_ideal_march_jax.py:430-435` (`step_norm` =
max|J^-1 r|), `:682-707` (`certify`: "Newton at the roundoff floor. Derived
from the Newton contraction, no magic" — the contraction hypothesis is never
checked); `def_twin_falsifier.py:71-72` mirrors GENO's |den| < 1e-10
fold-guard at the MONITOR level only, not in the cell certificate.

**Measured (P2, near-fold quadratic r = z^2 - 2bz + (b^2-p), fold at p=0,
p0 = 1e-8, root separation 2e-4):**
- at the EXACT (+) root, the certificate reads ratio = 25 => **false FAIL**:
  the metric's roundoff floor is amplified by 1/|J| (|J| = 2e-4 here), so a
  genuinely converged near-fold cell is rejected — this names a candidate
  MECHANISM inside the outcome-II "certifiability-limited" frontier verdicts
  (S20/S22): part of the crawl boundary may be metric conditioning, not
  physics. A re-adjudication lever, not a weakening: the honest bound is
  eps * kappa(J)-aware, still derived.
- a stale seed shifted by basin-scale amounts (3e-4) converges to the OTHER
  root branch with ratio = 0.0 => **false PASS**: the certificate certifies
  "a root", never "the root of the recorded branch". No branch-consistency
  monitor (sign(det J) / den-sign continuity along the cell chain) exists.

**SOTA reference:** Kantorovich a-posteriori certification and affine-
covariant error estimators (Deuflhard, *Newton Methods for Nonlinear
Problems*); Krawczyk interval-Newton verified enclosure (Rump, INTLAB lineage
— already in-house via [X-IVXC]); deflated Newton for root discrimination
(Farrell-Birkisson-Funke deflation).

**Extremal exposures:** (a) near-fold den -> 0 cells of the deep-DEF defnoz
twin (S24 F1b instance); (b) throat razor cells alpha -> 90 deg (Jacobian
near-singular in the position rows); plus (c) FD probes at frontier designs
where basin half-width ~ sqrt(dist-to-fold) < h_FD = 6.1e-6. **Everyday
case:** mild instances (S18 7.7e-2 KKT closure) — well-conditioned, metric
fine; the gap is invisible exactly where everything works.

---

## F3. Certificate scale is one scalar max(1, max|z|) dominated by u:
## position components certified ~10^3x looser than the claimed roundoff
## floor; worst at y -> 0 axis cells — {RIGOR-GAP, mild} / {NOT-SOTA}

**Cite:** `a1_ideal_march_jax.py:393` (`sc = max(1, max|z|)` in the cond),
`:699` (same in `certify`), while the docstring `:682-688` motivates the
z-space metric precisely by unit-consistency — the motivation is right, the
implementation stops one step short (component-uniform bound over
mixed-magnitude z = [x, y, u, v] with u ~ 2.3e3 m/s, y as small as 1e-3).

**Measured (P3, arithmetic):** position bound = 100*eps*2300 = 5.1e-11
absolute = 5.1e-8 RELATIVE for a near-axis y = 1e-3 cell — 2300x looser than
the nominal 100 eps floor claimed. Not currently load-bearing at yt = 1
scales, but it is a latent unit-dependence (SI q values set the bound for
POSITION accuracy), against the generality directive.

**SOTA reference:** componentwise scaling vectors (Deuflhard scaling in
NLEQ-ERR; componentwise relative norms, Higham *Accuracy and Stability of
Numerical Algorithms*).

**Extremal exposures:** (a) y -> 0 axis cells at fine mesh (position bound
>> local y); (b) high-q propellants (H2/O2, u ~ 4500 m/s) — bound scales up
with u while geometry stays O(1). **Everyday case:** every interior cell of
the eps = 4 baseline already carries the u-dominated scale.

---

## F4. Basin-of-attraction of predictor and stale replay seeds is
## assumption-only: no derived seed-validity radius exists (contrast: the
## design-space ball got a THEOREM+PRACTICE stack in [X-TBAK]) — {INCOMPLETE}

**Cite:** `a1_ideal_march_jax.py:540-543` (predictor "is O(h) and lands
inside" — asserted, not bounded), `:634` (replay seed = recorded z,
stop-gradient), `a1_toc_variational_jax.py:519` (same); `certdiag_kat.py:
36-41` (KAT-3 attempt-1: 2-trip Newton "reached the floor from the stale
seeds" — empirical, one instance, one perturbation amplitude). M0 S23 block
ln 1832-1884: the AS-BUILT perturbation ball in W-space is priced with a
theorem-anchored two-point surrogate (L_TB = 4.32e+01) — the EXACTLY
ANALOGOUS object in z-space (seed-to-root ball per cell kind) has no
counterpart anywhere; P2 shows the z-basin shrinks like sqrt(dist-to-fold)
below the FD step h = eps^(1/3) = 6.1e-6 near folds, so the O3.1 probes'
seed validity at frontier instances is unadjudicated (mitigated but not
bounded by C2-F2 cert-on-replay).

**SOTA reference:** Smale alpha-theory point estimates — a computable
per-seed certificate "Newton from this point converges quadratically to this
root" (Smale; Shub-Smale; alphaCertified, Hauenstein-Sottile TOMS 2012);
Kantorovich ball radii from measured local Lipschitz data (the [X-TBAK]
K_RICH two-point pattern transplants directly).

**Extremal exposures:** (a) near-fold deep-DEF cells (basin collapse +
branch twin = F2's false pass becomes REACHABLE); (b) steep thB / razor-thin
near-sonic start cells (the very cells that forced predictor seeding).
**Everyday case:** every O3.1 FD probe (4 replays per verdict) at mild
designs. **S25 REGISTERED PROBE (not run, > 30 s):** alpha-test evaluation at
every recorded cell of the S18 baseline plan + the defnoz twin — per-cell
cost is one Jacobian + one Hessian-norm surrogate; would convert F4 to a
measured ledger row.

---

## F5. cert_diag formal status: replay-vs-record certification equivalence is
## one-instance-empirical, its prefix-exactness lemma is unstated, and
## cert_diag XOR val_diag leaves the margin-governor constraint path with NO
## certification channel — {INCOMPLETE}

**Cite:** `a1_toc_variational_jax.py:549-576` — docstring declares
cert_diag/val_diag "mutually exclusive by declaration (no consumer needs
both)"; but [X-MGOV] consumes val_diag lanes (`margin_governor.py:172,245`)
to build the KS margin CONSTRAINT and its multiplier at TRIAL points, where
stalled/unconverged lanes are precisely the risk and no rejector reads them
(trial-point cert deferral to P3(ii) re-record is a DECLARED contract for the
OBJECTIVE path; the margin constraint entered the KKT system in S22 — the
declaration predates that consumer and was never re-adjudicated).
`:691-700` `_chain_ratios` rests on "active lanes form a prefix, so the carry
chain is exact there" — plausible, but unproven against the design-wall
TRUNCATION lanes (`:389-403` truncated columns), and no M0 rigor-class row
(THEOREM*/SCHEMA/PRACTICE, per R4) states "traced cert metric == record
metric". The KAT (`certdiag_kat.py`) is one healthy instance + one starved
perturbation — a knob-bite proof, not an equivalence family.

**SOTA reference:** differential/metamorphic testing across instance families
(property-based testing, QuickCheck/Hypothesis lineage) to populate the
equivalence claim; then registration as a SCHEMA with the masked-lane lemma
proved (finite induction on the scan carry). The val_diag+cert combination is
a one-line union (return both), cost-additive.

**Extremal exposures:** (a) deep-DEF trial points inside a governor segment —
margin value from a stalled lane feeds lambda without any certificate; (b)
short-L / truncated columns where the prefix assumption is actually stressed;
plus (c) zero-trip-starved replay (KAT-3 style) THROUGH the val_diag path —
nothing would fire today. **Everyday case:** every accepted governor segment
evaluates ~10-40 trial points on uncertified lanes. **S25 REGISTERED PROBE:**
KAT-3 twin on the val_diag path (starve solver, check the margin constraint
silently returns stale-seed values) — ~2 min, above budget here.

---

## F6. No early-abort in record mode: a stalled cell (trip-cap, 30 iters x
## 6-candidate damping vmap) still seeds the ENTIRE downstream march;
## failure surfaces only at the post-march P4 gate and downstream cells
## certify on corrupted upstream data — {EFFICIENCY-GAP}

**Cite:** `a1_ideal_march_jax.py:698-707` (`certify` accumulates worst, never
raises), `a1_toc_variational_jax.py:239-275` (`cell` raises ONLY on the
margin rejector; cert ratio > 1 just recorded), `:930-938` (P4 checks
cert_worst AFTER the full record); S20 reject-and-shrink pays a FULL record
per rejected base (baseline of record: 111 s at 7818 cells) before the
verdict. Downstream-of-stall cells solve exact roots of WRONG parameter data
(their pt1/pt2 come from the uncertified iterate), so their individual
PASS certificates are vacuous — localization exists only via the default-off
CERT_ARGMAX (`a1_toc:125,251-258`). The gate itself is correct and stays;
the gap is WHEN it fires and what the trailing compute buys (nothing).

**SOTA reference:** fail-fast infeasibility handling at evaluation
granularity, standard in trust-region frameworks (Conn-Gould-Toint, *Trust
Region Methods* — reject on first evidence, return infeasibility flag);
structured-exception + checkpoint/resume for long marches.

**Extremal exposures:** (a) frontier crawl (S20: 8 rejected designs, each a
full record burned after the first bad cell); (b) [X-AKNO] knot-insertion
cycles re-recording rejected classes. **Everyday case:** every rejected
accepted-step in a mild run pays ~full-march latency for a verdict decidable
at first uncertifiable cell (plus 30x6 residual evaluations burnt inside
that cell's stalled ladder).

---

## F7. Wall-foot chord search: unbracketed linear index scan, one FULL
## implicit Newton solve per failed attempt, foot-acceptance predicate
## assumes monotone foot ordering, Nv monotone nondecreasing by
## construction — measured fragile, degenerate geometry can only fail by
## exhaustion or accept a wrong foot silently — {INCOMPLETE} + {NOT-SOTA}

**Cite:** `a1_ideal_march_jax.py:806-833` (record wall_search: `while True:
N += 1 ... if float(zt[0]) > float(pt1[0]): Nv += 1; continue`, cap
`N > j2+2` -> RuntimeError), `a1_toc_variational_jax.py:355-375` (same, cap
`N > len(prev)+1`); the FRAGILITY is measured of record:
`a1_toc:847-852` "the wall-search indices (N, Nv) are FRAGILE decisions...
a decision flip fires at almost every accepted step: one RK-G segment ~ one
productive step" — i.e., this search's discreteness sets the RE-RECORD RATE
of the whole RK-G loop (n_rec ~ n_segments), a first-order driver of the
111 s-per-record tax. The predicate tests only the solved foot x-ordinate
against pt1; with a locally non-monotone wall (spline overshoot between
nearly-degenerate knots) the first index satisfying it need not be the
geometrically correct chord cell, and Nv can never step back.

**SOTA reference:** bracketed scalar root-finding on the CONTINUOUS chord
parameter D (Brent 1973) after a cheap orientation pre-filter (robust
geometric predicates, Shewchuk 1997) — solve the implicit cell ONCE at the
bracketed foot; this also makes (N, Nv) a derived quantity instead of a
fragile recorded decision, directly cutting re-record events.

**Extremal exposures:** (a) nearly-degenerate knots from [X-AKNO] insertion
(D6 item 9, ln 906: "new knot AT A DATA SITE" — adjacent sites can be
arbitrarily close) -> spline oscillation between stations; (b) thB steep
(arc end slope ~ tan thB large, foot jumps several rows per station); (c)
deep-DEF short-L truncated columns (prev shrinks, cap exhaustion).
**Everyday case:** Nw = 60-100 stations x O(Nv) failed attempts, each a full
4x4 Newton — pure waste on the hot path of every record. **S25 REGISTERED
PROBE:** doctored two-close-knots spline, count wrong-foot acceptances vs
the Brent-bracketed reference (~1 min, above budget here).

---

## F8. Certification/solver constants are conventions, not derivations:
## NEWTON_TOL_FACTOR = 100 ("spike factor convention"), N_NEWTON = 30,
## damping ladder (1, 1/2, 1/4, 1/16, 1/64, 0) with bare non-increase
## acceptance — against the repo's own R5 bar — {NOT-SOTA}

**Cite:** `a1_ideal_march_jax.py:145-148` (constants), `:371` (TRIALS),
`:397-416` (body: argmin over candidates, accepts ANY non-increase incl. the
t = 0 stall; no sufficient-decrease test, no contraction measurement).
Contrast the repo's own better practice: `thermotab_c1_jax.py:38-40, 270-272`
derives C_OPS = 100 from an operation count. [X-CDKAT] proved N_NEWTON bites
— it did not derive it. Note the ladder's gap 1/4 -> 1/16 -> 1/64 skips the
classical halving sequence with no recorded rationale; a near-fold cell burns
30 x 6 residual+Jacobian evaluations to certify a stall (compounds F6).

**SOTA reference:** affine-covariant natural monotonicity test with
contraction-derived damping factors (Deuflhard NLEQ-ERR/NLEQ-RES — the
damping factor is COMPUTED from measured contraction, not enumerated);
Armijo sufficient decrease (Nocedal-Wright §3.1); ops-count-derived roundoff
constants per residual kind (Higham) to replace the blanket 100.

**Extremal exposures:** (a) near-fold den -> 0 cells (ladder stall, budget
burn, then F2's conditioning ambiguity on the verdict); (b) near-sonic razor
cells where the useful t is data-dependent (measured contraction would find
it in 1-2 trials). **Everyday case:** every cell pays the 6-candidate vmap
even in the terminal quadratic phase where t = 1 always wins.

---

## DROPPED (declared, 5):
1. Wavefront/anti-diagonal vmap parallelization of record mode (efficiency;
   overlaps the do-not-remeasure 111 s baseline and the F2-engine session).
2. Dense per-iteration jacfwd instead of Jacobian reuse/Broyden on 4x4 cells
   (negligible at this cell size; dominated by F8's ladder cost).
3. DWR a-posteriori never built (named in theorem ledger U3 ln 681-685 and
   D6 ln 886-889) — real, but belongs to the MESH/refinement facet, not the
   cell-certification facet; deferred to that finder to avoid duplication.
4. Per-cell float() host-sync overhead in record mode (folded into F6's
   fail-fast rework; not separately actionable).
5. leggeAree bracket scan: hardcoded 400-point grid on [1.01, 2.8]*as
   (`a1_ideal_march_jax.py:747`) — a case-dependent constant against the
   generality directive, but one-shot per march and low stakes.

## PROBE LEDGER (this session)
- RUN: scratchpad/probe_cell_cert.py — P1 + P2 + P3, 5.9 s total, one
  process, no repo files touched, no heavy instance launched.
- REGISTERED for S25: (i) alpha-test/Kantorovich per-cell seed certificate at
  the S18 baseline + defnoz plans (F4); (ii) val_diag starvation KAT-3 twin
  (F5); (iii) doctored close-knots wall-foot search vs Brent reference (F7).

## SUMMARY TABLE
| # | Finding | Class | Decisive evidence |
|---|---------|-------|-------------------|
| F1 | table-edge clamp unguarded, dead adjoint | RIGOR-GAP | P1: 103 K error, dT/dq = 0, silent |
| F2 | certificate lacks conditioning/branch qualification at folds | RIGOR-GAP | P2: false-fail ratio 25 at true root; false-pass ratio 0 on wrong branch |
| F3 | scalar cert scale u-dominated; position bound 2300x loose | RIGOR-GAP (mild) | P3 arithmetic |
| F4 | no derived seed-basin radius (z-space X-TBAK missing) | INCOMPLETE | P2 basin < h_FD near fold; KAT is 1-instance |
| F5 | cert_diag equivalence informal; val_diag path uncertified | INCOMPLETE | a1_toc:549-576 XOR + margin_governor:172,245 |
| F6 | no early-abort; post-march P4 only; downstream cert vacuous | EFFICIENCY-GAP | S20 8 full records burned; 111 s baseline |
| F7 | wall-foot scan fragile + 1 Newton/attempt; drives re-record rate | INCOMPLETE + NOT-SOTA | a1_toc:847-852 measured fragility |
| F8 | tol factor/cap/ladder conventions not derived; no sufficient decrease | NOT-SOTA | a1:145-148,371,397-416 vs thermotab's derived C_OPS |
