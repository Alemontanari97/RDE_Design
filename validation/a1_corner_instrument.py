#!/usr/bin/env python3
"""A1 BRICK 2, STEP 2 [F2/A1]: THE CORNER (TRANSVERSALITY) INSTRUMENT at
the lip, with f2 controls — on the assembled march (Brick 1) and the
thrust carrier (step 1, imported and reused).

WHAT THIS ADDS. Step 1 gave the engine a score (J) and a search
direction (dJ/dP). This step adds the OPTIMALITY METER: Rao's endpoint
condition (docs/rde_nozzle_P2_lemmaA.md, Eq. L.15),

    R_corner(pa) = (p - pa) - (1/2) rho W^2 sin(2 theta) tan(alpha)

evaluated at the lip E from the march's own wall states. R_corner = 0 is
the classical necessary condition for the lip to sit at a thrust
optimum; its mu-weighted average is the T7 (**') condition of the cycle
theory. An optimizer needs this meter to CERTIFY a converged shape, and
to place the lip by optimality instead of by prescription.

WHAT THE TYPE-0 (IDEAL) NOZZLE MUST SHOW — three known answers:
  (i)  MATCHED AMBIENT: the ideal nozzle exits uniform and axial
       (theta_E ~ 0), so R_corner(pa = p_e) ~ 0: the uniform-exit
       nozzle IS corner-stationary at its design ambient. PASS = |R| in
       a Richardson band derived from the coarse/fine marches.
  (ii) VACUUM: R_corner(0) ~ p_e > 0 — "lengthen me". This is the
       vacuum theorem read off an instrument: at pa = 0 no finite
       nozzle is optimal.
  (iii) CONSISTENCY WITH THE GRADIENT: the exit-area lemma says
       dJ/dA_e = P_e - pa; hence sign(dJ/deps) must equal
       sign(R_corner) at the same pa. Checked at pa = 0 against a
       central-FD dJ/deps computed from two fresh adaptive marches
       (no AD compile needed for this check).

f2 CONTROLS (the first-integral instrument, prepared for the TOC
oracle): f2 = W cos(theta - alpha)/cos(alpha).
  * POSITIVE (uniformity): at the lip, theta ~ 0, so f2(lip) must equal
    the exit speed q_e from step 1's implicit solve, within a
    Richardson band — instrument and exit solve must agree.
  * NEGATIVE (rejector): f2 is an invariant along CHARACTERISTICS of a
    thrust-optimal exhaust, NOT along arbitrary curves. Along the WALL
    (a streamline crossing the expansion) its variation must be LARGE:
    >= 10x its own discretization band. A "constant-f2-everywhere"
    implementation bug would be caught here.
  * The genuine positive control — f2 CONSTANT along the terminal
    characteristic of a thrust-optimal contour — needs the GENO type-2
    TOC reference; DECLARED PENDING until that binary is rebuilt.

Run:  .venv-a1/bin/python validation/a1_corner_instrument.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1              # noqa: E402  Brick 1
import a1_thrust_functional as TF            # noqa: E402  step 1

import jax.numpy as jnp                      # noqa: E402

EPS = A1.EPS
CASE = A1.CASE
K_RICH = A1.K_RICH
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def lip_state(out, ta):
    """(W, theta, p, rho, alpha) at the last wall point."""
    u, v = float(out["wall_u"][-1]), float(out["wall_v"][-1])
    W = float(jnp.sqrt(u * u + v * v))
    th = float(np.arctan2(v, u))
    _, p, rho, _, _, M = (float(x) for x in A1.state_q(jnp.float64(W), ta))
    al = float(np.arcsin(1.0 / M))
    return W, th, p, rho, al


def corner_residual(out, ta, pa):
    W, th, p, rho, al = lip_state(out, ta)
    return (p - pa) - 0.5 * rho * W * W * np.sin(2.0 * th) * np.tan(al)


def f2_of(u, v, ta):
    W = jnp.sqrt(u * u + v * v)
    th = jnp.arctan2(v, u)
    M = A1.state_q(W, ta)[5]
    al = jnp.arcsin(1.0 / M)
    return W * jnp.cos(th - al) / jnp.cos(al)


def main():
    t0 = time.time()
    print("== A1 brick 2 step 2: corner instrument + f2 controls"
          " [F2/A1] ==")
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    P0 = jnp.array([CASE["yt"], CASE["rtu"], CASE["rtd"], CASE["eps"]])
    cfg = dict(NI=CASE["NI"], Ne=CASE["Ne"], da_deg=CASE["da_deg"])
    cfg_f = dict(NI=2 * CASE["NI"] - 1, Ne=2 * CASE["Ne"] - 1,
                 da_deg=0.5 * CASE["da_deg"])

    print("-- S1: coarse + refined marches --")
    out, _ = A1.run_march(P0, tab, cfg)
    out_f, _ = A1.run_march(P0, tab, cfg_f)

    # exit speed / pressure of record (step 1 machinery)
    qe = float(TF.solve_qe(out_f["Me"], ta, tab["_as"]))
    pe = float(A1.state_q(jnp.float64(qe), ta)[1])

    print("-- S2: corner residual at the lip --")
    W, th, p, rho, al = lip_state(out_f, ta)
    print("  lip state: W=%.4f  theta=%.3e rad  p=%.6e  alpha=%.4f"
          % (W, th, p, al))
    Rc = corner_residual(out, ta, pe)
    Rf = corner_residual(out_f, ta, pe)
    band = K_RICH * abs(Rc - Rf) + A1.C_FLOOR * EPS * pe
    print("  R_corner(pa=p_e) coarse/fine = %+.3e / %+.3e  band=%.3e"
          "  (rel %.1e of p_e)" % (Rc, Rf, band, band / pe))
    check("matched ambient: |R_corner(p_e)| <= Richardson band",
          abs(Rf) <= band)

    R0 = corner_residual(out_f, ta, 0.0)
    dev = abs(R0 - pe)
    print("  R_corner(pa=0) = %+.6e  vs p_e = %.6e  |d|=%.2e"
          % (R0, pe, dev))
    check("vacuum reading: R_corner(0) = p_e within band (lengthen me)",
          dev <= band + abs(pe) * 1e2 * EPS)

    print("-- S3: consistency with the gradient (exit-area lemma) --")
    h = 1e-3 * CASE["eps"]
    Jp = float(TF.J_exit_of_out(
        A1.run_march(P0.at[3].add(h), tab, cfg)[0], ta, tab["_as"]))
    Jm = float(TF.J_exit_of_out(
        A1.run_march(P0.at[3].add(-h), tab, cfg)[0], ta, tab["_as"]))
    dJde = (Jp - Jm) / (2.0 * h)
    print("  FD dJ/deps (fresh adaptive marches) = %+.6e ; R_corner(0)"
          " = %+.6e" % (dJde, R0))
    check("sign(dJ/deps) == sign(R_corner) at pa=0 (exit-area lemma)",
          np.sign(dJde) == np.sign(R0) and abs(dJde) > 0)

    print("-- S4: f2 controls --")
    f2_lip_c = float(f2_of(out["wall_u"][-1], out["wall_v"][-1], ta))
    f2_lip_f = float(f2_of(out_f["wall_u"][-1], out_f["wall_v"][-1], ta))
    band_f2 = K_RICH * abs(f2_lip_c - f2_lip_f) + A1.C_FLOOR * EPS * qe
    dq = abs(f2_lip_f - qe)
    print("  f2(lip)=%.6f  q_e=%.6f  |d|=%.2e  band=%.2e"
          % (f2_lip_f, qe, dq, band_f2))
    check("uniformity: f2(lip) == q_e within band", dq <= band_f2)

    f2_wall = np.array([float(f2_of(u, v, ta)) for u, v in
                        zip(np.array(out_f["wall_u"]),
                            np.array(out_f["wall_v"]))])
    var = f2_wall.max() - f2_wall.min()
    print("  f2 along wall: min=%.4f max=%.4f  variation=%.4f"
          " (>= 10x band %.2e required)" % (f2_wall.min(), f2_wall.max(),
                                            var, 10 * band_f2))
    check("negative control: f2 NOT constant along the wall",
          var >= 10.0 * band_f2)
    print("  [DECLARED PENDING] positive control (f2 const on a real TOC"
          " terminal characteristic) awaits the GENO type-2 build")

    print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
