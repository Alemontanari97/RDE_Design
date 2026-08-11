"""[X-TBAK] TOLERANCE-BALL MARGIN BACKOFF — DUTY-6(i) of the
S-GAUNTLET ratified duty package (owner: F1 margin-governor
derived-floor machinery; executed S23, F1 close; log
validation/PROGRESS_2026-08-11_S23_f1close.md).

THE DEFECT THIS CLOSES (gauntlet C028): a KKT-active optimum has ZERO
margin by construction — its certificate certifies a MEASURE-ZERO
design; any as-built contour inside a manufacturing tolerance ball
around it can sit outside the certified set. The ratified falsifier:
"re-certify a shipped optimum on a tolerance-perturbed contour — at a
KKT-active optimum it MUST fail until the backoff exists."

THE BACKOFF (derivation of record; classes declared):
 * BALL (declared, in-class): the as-built contour is the design-class
   interpolant of perturbed dofs. A function-space perturbation p with
   ||p||_inf <= delta has nodal values |dW_i| = |p(x_i)| <= delta, so
   the in-class as-built set maps INTO the dof box {||dW||_inf <=
   delta}; bounding the worst case over the BOX is conservative
   [THEOREM-level step: nodal evaluation is norm-nonexpansive]. Slope
   control (the W^{1,inf}/C^1 qualifier of the ratified duty) is
   automatic in-class: the fixed spline basis maps the dof box to a
   bounded-slope family, and the margin's dof-gradient chain already
   carries the full slope dependence. OUT-OF-CLASS waviness (e.g. AM
   surface texture below the class resolution) is a DECLARED class-
   scope boundary, not covered here (F2/F6 per the ratified split).
 * MEAN-VALUE BOUND [THEOREM, m C^1 on the box]:
     min_{||dW||_inf <= delta} m(W + dW) >= m(W) - L1_sup * delta,
   with L1_sup = sup over the box of ||grad m||_1 (Hoelder pairing of
   the l_inf box with the l1 dual norm).
 * MEASURED-SUP SURROGATE [PRACTICE, K_RICH-safeguarded — the same
   two-point pattern as every derived band in this repo]:
     L_TB = K_RICH * max( ||grad m(W)||_1,
                          ||grad m(W + dW*(delta_max))||_1 ),
   with dW*(delta) = -delta * sign(grad m(W)) the first-order worst
   box vertex; BACKOFF RULE OF RECORD: Delta(delta) = L_TB * delta.
   SHIP GATE: a design is shippable at declared tolerance delta only
   if m(W) >= Delta(delta). SCOPE: this is a CERTIFICATION-TIME
   (ship) requirement on the nominal optimum; the search-time margin
   machinery ([X-MGOV], REQ-NONSTALL, G1 surrogate) is UNTOUCHED.
 * GENERALITY (binding, per the generality-nonhardcoded directive +
   the S23 user pin): delta is a DECLARED APPLICATION INPUT, never
   tuned here — the deliverable of record is the COEFFICIENT L_TB
   (backoff per unit ball radius, design units) for the CURRENT class;
   the reference list DELTAS below spans 0.1 mm on throat radii
   {1 m, 10 cm, 1 cm} in the nondimensional y_t = 1 units (a
   declaration for the rejector runs, overridable via A1_TB_DELTA);
   PER-CLASS RE-DERIVATION is mandatory at every tier/geometry-class
   transition (D6 tier-invariant transition duty — a coefficient
   valid only on the class it was derived in is a defect to declare).
 * SURVEY (adopt-or-declare, SOTA): worst-case linearization over a
   tolerance ball is the standard robust-margin treatment
   (linearized robust counterpart of the semi-infinite constraint
   min over the ball; cf. Ben-Tal/Nemirovski robust-LP lineage and
   tolerance-allocation practice). Full robust-optimization machinery
   (minimax re-optimization, DRO over as-built distributions) NOT
   adopted here, with reason: the robust/mode-measure layer has a
   ratified owner (DUTY-13, post-F5a re-adjudication) and P3
   anti-divergence pins this duty to the derived-floor backoff.

REJECTORS (R5 — rows that can reject, with the ratified falsifier as
the firing row):
 (R-TB1) BOUND VALIDITY, must HOLD: the measured margin drop at the
   worst vertex satisfies drop(delta) <= Delta(delta) at EVERY
   declared delta (the K_RICH-safeguarded surrogate covers the
   measured curvature); the per-delta linearity ratio is printed.
 (R-TB2) THE RATIFIED DUTY-6 FALSIFIER, must FIRE: at a SYNTHETIC
   margin-active floor (mu_0* = the measured KS at the nominal base,
   so the nominal margin is 0 by construction = KKT-active
   surrogate), the delta_max-perturbed contour FAILS re-certification
   (margin < 0). Failure to fire = the backoff is untestable on this
   instance = carrier FAIL.
 (R-TB3) THE BACKOFF DISCRIMINATES: (a) the margin-active nominal is
   REJECTED by the ship gate at every declared delta > 0; (b) the
   healthy rung-1 configuration (floor mu_0_1 = m_ref/2) is ACCEPTED
   at every delta with Delta(delta) < m(W), and at each accepted
   delta the perturbed margin stays >= 0 (the certificate SURVIVES
   the ball — the bound's conclusion, measured); (c) NO-BACKOFF
   CONTROL, must show the defect: with Delta forced to 0 the active
   nominal is accepted, yet its perturbed margin is < 0 — the
   acceptance is measurably UNSAFE (this is C028 reproduced).

ON-DEMAND CARRIER (env: jax). Exit 0 = PASS, 1 = FAIL.
"""
import os
import sys

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1        # noqa: E402
import o33_bench as O33                # noqa: E402
from margin_governor import (baseline_val_stats, make_margin_fn,
                             check, N_RUNGS)  # noqa: E402

jax.config.update("jax_enable_x64", True)

# DECLARED reference tolerance list (nondimensional, y_t = 1): 0.1 mm
# as-built ball on throat radii 1 m / 10 cm / 1 cm. A declaration for
# the rejector runs, NOT a tuned constant; applications override.
DELTAS = ([float(x) for x in os.environ["A1_TB_DELTA"].split(",")]
          if "A1_TB_DELTA" in os.environ else [1e-4, 1e-3, 1e-2])


def main():
    print("== [X-TBAK] tolerance-ball margin backoff (JAX %s; "
          "DUTY-6(i), F1 close) ==" % jax.__version__)
    ok = True
    tab = A1.prep_tab(A1.build_tab_nasa())
    state_fn, solv, cfg = O33.make_case(tab)

    # ---- derived context (same derivations of record as [X-MGOV])
    print("-- B0: baseline W* val field + derived governor context --")
    st = baseline_val_stats(tab, cfg, state_fn, solv, O33.W_STAR)
    ok &= check("baseline certified", st["out"]["cert_worst"] <= 1.0)
    m_ref, N, q_ref = st["m_ref"], st["N"], st["q_ref"]
    ladder = [m_ref / 2.0**k for k in range(1, N_RUNGS + 1)]
    rho = A1.K_RICH * np.log(N) / ladder[-1]
    print("  N = %d lanes; m_ref = %.6e; mu_0_1 = %.6e; rho = %.4e"
          % (N, m_ref, ladder[0], rho))

    # margin with mu0 = 0 (the KS + G1-surrogate aggregate itself);
    # every floored margin is m0(W) - mu0, so ONE traced fn serves all
    m0_fn = make_margin_fn(tab, cfg, st["plan"], state_fn, solv,
                           rho, 0.0, m_ref, q_ref)
    m0_jit = jax.jit(m0_fn)
    g0_jit = jax.jit(jax.grad(m0_fn))
    W0 = jnp.asarray(np.asarray(O33.W_STAR, dtype=float))
    m0_base = float(m0_jit(W0))         # = measured KS aggregate at W*
    g_base = np.asarray(g0_jit(W0))
    ok &= check("gradient finite at nominal",
                bool(np.all(np.isfinite(g_base))))
    g1_base = float(np.abs(g_base).sum())
    print("  m0(W*) = KS(base) = %.6e; ||grad m||_1 at nominal = "
          "%.6e" % (m0_base, g1_base))

    # ---- L_TB: two-point measured-sup surrogate, K_RICH-safeguarded
    print("-- B1: backoff coefficient L_TB (measured-sup surrogate) --")
    d_max = max(DELTAS)
    sgn = np.sign(g_base)
    W_vx = W0 + jnp.asarray(-d_max * sgn)   # first-order worst vertex
    g_vx = np.asarray(g0_jit(W_vx))
    ok &= check("gradient finite at worst vertex",
                bool(np.all(np.isfinite(g_vx))))
    g1_vx = float(np.abs(g_vx).sum())
    L_TB = A1.K_RICH * max(g1_base, g1_vx)
    print("  ||grad m||_1 at vertex(delta_max) = %.6e" % g1_vx)
    print("  L_TB OF RECORD (this class, %d-dof bell tier-0) = "
          "K_RICH * max = %.6e per unit ball radius" %
          (len(np.asarray(W0)), L_TB))
    print("  backoff rule: Delta(delta) = L_TB * delta; ship gate "
          "m(W) >= Delta(delta) at DECLARED delta")

    # ---- R-TB1: bound validity at every declared delta
    print("-- B2: R-TB1 bound validity over declared deltas %s --"
          % DELTAS)
    drops = {}
    for d in DELTAS:
        Wp = W0 + jnp.asarray(-d * sgn)
        m_p = float(m0_jit(Wp))
        drop = m0_base - m_p
        drops[d] = (drop, m_p)
        bound = L_TB * d
        print("  delta %.1e: drop %.6e vs Delta(delta) %.6e "
              "(ratio drop/delta = %.4e)" % (d, drop, bound,
                                             drop / d))
        ok &= check("R-TB1: drop <= Delta at delta %.1e" % d,
                    drop <= bound)

    # ---- R-TB2: the ratified falsifier MUST FIRE
    print("-- B3: R-TB2 synthetic margin-active nominal (mu_0* = "
          "KS(base) -> m = 0 by construction) --")
    mu0_star = m0_base
    m_act_nom = m0_base - mu0_star
    m_act_prt = drops[d_max][1] - mu0_star
    print("  active nominal margin = %.3e; perturbed (delta %.1e) "
          "margin = %.6e" % (m_act_nom, d_max, m_act_prt))
    ok &= check("R-TB2 FIRES: tolerance-perturbed re-certification "
                "FAILS at the margin-active nominal (margin < 0)",
                m_act_prt < 0.0)

    # ---- R-TB3: the backoff discriminates
    print("-- B4: R-TB3 ship-gate discrimination --")
    for d in DELTAS:
        ok &= check("R-TB3a: active nominal REJECTED by ship gate at "
                    "delta %.1e" % d, m_act_nom < L_TB * d)
    m_r1 = m0_base - ladder[0]          # healthy rung-1 margin
    print("  healthy rung-1 nominal margin m = %.6e (floor mu_0_1)"
          % m_r1)
    n_acc = 0
    for d in DELTAS:
        accepted = m_r1 >= L_TB * d
        m_r1_prt = drops[d][1] - ladder[0]
        if accepted:
            n_acc += 1
            ok &= check("R-TB3b: accepted at delta %.1e AND perturbed "
                        "margin %.4e >= 0 (certificate survives the "
                        "ball)" % (d, m_r1_prt), m_r1_prt >= 0.0)
        else:
            print("  delta %.1e: rung-1 nominal NOT shippable "
                  "(Delta %.4e > m %.4e) — honest verdict, backoff "
                  "binds" % (d, L_TB * d, m_r1))
    ok &= check("R-TB3b: at least one declared delta accepted at "
                "rung 1 (gate non-vacuous on the healthy instance)",
                n_acc >= 1)
    # (c) no-backoff control: acceptance without backoff is UNSAFE
    unsafe = (m_act_nom >= 0.0) and (m_act_prt < 0.0)
    ok &= check("R-TB3c: NO-BACKOFF control shows the C028 defect "
                "(active nominal accepted with Delta = 0, perturbed "
                "margin < 0)", unsafe)

    print("PER-CLASS NOTE (tier-invariant transition duty, binding): "
          "L_TB above is of record ONLY for this class (bell tier-0, "
          "%d-dof, baseline plan); every tier/class transition "
          "re-derives it." % len(np.asarray(W0)))
    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
