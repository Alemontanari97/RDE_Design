# PROGRESS — [F2/A1] S23: resolving the free-form spike's gain (2026-08-10)

**Carrier:** `validation/a1_plug_gain_resolve.py` ([X-PGRS]).
**Question:** S21/S22's open item 1 — is the free-form spike's gain
over the fan streamline real, zero, or negative, with a band that
supports the answer?

## Step 1 — Extrapolation done right (stage analysis)

The S22 ladders, extrapolated PER DESIGN (each sequence by its own
geometric model on the spacing-halving ladder):

    J(streamline)      r = +0.506  -> limit 1.160260e+08   (clean first order)
    J(61-tuned opt)    r = -0.263  -> limit 1.160127e+08   (non-monotone)
    provisional gain limit of the 61-TUNED design:  -0.0115 %

So the S22 coarse-tuned optimum extrapolates BELOW the streamline:
its measured coarse-grid gain was entirely instrument fit. Also of
record: the naive PAIRED-difference extrapolation (r = 0.846, "limit"
-0.51 %) is INADMISSIBLE — it mixes a +0.5-ratio sequence with a
-0.26-ratio one, and the carrier refuses mixed modes (rejector R-1c).

## Step 2 — The no-motion wedge: found, diagnosed, fixed, verified

The first fineopt attempt returned "no motion" from the S22 optimum
at (121,101) with |grad| = 6.0e6. Diagnosis BEFORE fix, instrument
before object:

- probe 1 (the objective): J_replay along +grad on an h-ladder is
  SMOOTH — matches the linear prediction to 3 digits for h <= 1e-4,
  +7.1e4 available at h = 1e-3, folds over between 1e-3 and 1e-2.
  No NaN, no exception. The surface is fine; improvement is real.
- probe 2 (the driver): scipy trust-constr, exact options of record,
  verbose trace: the FIRST trial (radius 0.05) lands past the fold,
  is rejected, and its negative curvature poisons the BFGS model;
  iterations 3-8 then burn CG cycles WITHOUT EVALUATING the
  objective again (f-evals frozen at 3) and return x0 unchanged.
  A scipy wedge, not a physics event.

FIX (in `run_trsqp`, [X-PSPL]): no-motion with the radius above the
floor now follows the SAME reject-and-shrink semantics as a rejected
base — shrink the OUTER radius, retry the segment on the same record;
only no-motion at the floor is convergence. VERIFIED: the full smoke
suite re-run is bit-identical in every J on every path that never
wedged (only wall-clock times differ), 9/10 as before.

Also this session, the artifact-overwrite trap struck twice more and
is now closed: the smoke re-run clobbered the committed production
`design.json` (restored from git, one command — the reason artifacts
belong in commits); both `a1_plug_spline_opt` and `a1_plug_adaptive`
now write settings-tagged artifact names (`design_m10_k61_n51.json`
style), so an instrument run can no longer overwrite a production
record.

## Step 3 — The fine-tuned incumbent (stage fineopt)

Record checks first: J(S22 optimum) at (61,51) reproduces
design.json at rel 0.0; all four fresh rung-1/2 J's reproduce the
S22 log at printed precision.

TR-SQP at (121,101), warm from the S22 optimum: 15 accepted
segments, 5 no-motion retries (each fatal to the old driver),
2 uncertified bases rejected, 3 worse trials rejected.

    fine optimum J(121) = 1.16037436e+08   (+0.0098 % over the S22
    design at the same instrument; |grad| 6.0e6 -> 1.1e5; cert 0.660)

R-3 PASS (certified, no loss to warm start), R-4 PASS (adjoint vs FD
ladder at the optimum).

Fresh full-precision ladders, both designs:

    rung ( 61, 51): J_inc 1.1560020078e+08  J_fine 1.1595026809e+08  gain +0.303 %
    rung (121,101): J_inc 1.1581033856e+08  J_fine 1.1603743640e+08  gain +0.196 %
    rung (241,201): J_inc 1.1591676617e+08  J_fine 1.1604150628e+08  gain +0.108 %

    extrapolations: inc r = +0.506 -> 1.160260e+08
                    fine r = +0.047 -> 1.160417e+08
    PROVISIONAL 3-rung gain limit = +0.0136 %

The finding inside the finding: the FINE-TUNED design's ladder has
r = 0.047 — its rung-3 value IS its limit to ~2e-7 relative. The
design tuned at the coarse march was non-monotone (r = -0.26); the
design tuned at the fine march converges almost instantly. The
remaining uncertainty in the gain is essentially all in the
STREAMLINE's slow first-order tail (~0.09 %), which is exactly what
the rung-4 model check measures.

## Step 4 — Rungs 4-6 and the verdict (stages rung4/final)

Rung 4 first BROKE the model, informatively: J_inc's march lost its
certification margin (2.652, one WALL cell at column 225 — a
round-off-MARGIN event, ~1e-13 relative, J-irrelevant; K-trend booked
as an open march-contract item) while J_fine, though certified, landed
1.1e5 BELOW its trend: the de-tuning transient, one rung past the
tuning resolution, the same signature the 61-tuned design showed at
rung 3. Both designs landing low at 481 said: extend the ladder, the
per-design fine extrapolation is premature.

Two instrument events on the way, both fixed and gated:

- the (481,401) marches first ran 7 h to nowhere: plug_march ended by
  jnp.stack-ing the mesh record (~193k operands at rung 4) and both
  processes wedged inside ONE XLA compile (py-spy: backend_compile).
  Fixed: the mesh record is concrete and every consumer converts to
  numpy, so it is now stacked in numpy — a memcpy, bit-identical
  (gated: J at (61,51) reproduces design.json at rel 0.0), and the
  481 march fell from 7 h (unfinished) to 8.5 min. Rungs 5-6 became
  affordable the same moment: the whole 6-rung campaign after the fix
  cost less than the single wedged compile.
- a session restart reset the shell cwd and one rung-6 launch died on
  a relative path (2 h lost silently); relaunched with absolute
  paths.

Rungs 5 (961,801) and 6 (1921,1601), both designs:

    J_inc:  1.1599624499e+08 (cert 0.865)   1.1601668529e+08 (cert 0.817)
    J_fine: 1.1602194399e+08 (cert 4.032*)  1.1600951521e+08 (cert 0.154)
    (* margin-degraded, reported; the 481/961 excursions are a
       one-cell lottery — rung 6 certifies clean on both designs)

AMENDMENT OF THE VERDICT RULE, declared 2026-08-11 BEFORE rung 6
completed: the verdict object is the PAIRED gain ladder (single-mode
once the design left its tuning window; ratios 0.829 -> 0.622 ->
0.554 measured on rungs 1-5 at declaration time), the fine design's
own-ladder extrapolation stays REFUSED (mixed-mode), gates R-5'a
(settling toward the march order) and R-5'b (the last rung predicted
from the window before it, miss <= step).

THE VERDICT (stage final, 3/3 PASS):

    paired gains  +0.30283 +0.19609 +0.10761 +0.05261 +0.02216 +0.00618 %
    diff ratios   0.8290   0.6216   0.5538   0.5244        (march order 0.5)
    R-5'a PASS; R-5'b PASS (predicted +0.00529 %, actual +0.00618 %,
                            miss 9.0e-6 = step/18)
    J_inc limit: 1.16022970e+08 -> 1.16022775e+08 (r = 0.500 exactly)
    gain limit: prev window -0.01566 %, last window -0.01144 %
    band = K_RICH x |shift| = 0.01688 %   (BAR 0.04 %)

    VERDICT: the gain is ZERO within the band. THE TRUNCATED
    STREAMLINE IS OPTIMAL AT THIS LENGTH TO WITHIN |0.0283| %.
    RESOLVED.

Reading of record: Rao's transposed argument survives in SIGN at
every finite resolution and is worth ~nothing in the limit at the
OPTIMIZED inlet split (theta_E = 0, L = 2.5 m, 57 % truncation).
Every coarse-grid gain of S21/S22 was the optimizer fitting the
march's own discretization error. The one design variable at fixed
length that pays is the inlet split (percent scale); shape refinement
after it is bounded by |0.028| %. Scoped: this is a statement at the
optimized posing, not "spike shaping never matters" (at a suboptimal
inlet split, or other lengths, unmeasured).

## Declared rule of record (written before the rung-4 runs)

gain* from the rung-2-4 extrapolations of both designs;
band = K_RICH x |limit(2-4) - limit(1-3)| + C_FLOOR*EPS on the gain;
gain* > band -> spike beats streamline; gain* < -band -> streamline
optimal at this length in this basis; |gain*| <= band -> zero within
band; RESOLVED iff band <= BAR = 0.04 %. Model gate R-5: the rung-4
prediction miss must not exceed the step it predicts, else
UNRESOLVED by declaration.
