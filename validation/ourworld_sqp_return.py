"""[F3] OUR WORLD, PLUG-SECTOR O3.3 (motion half): started off GENO's
axisymmetric ideal spike in OUR world, does the [X-PSPL] TR-SQP driver
come back to it?

The rao1961_sqp_return instrument (8-knot spline on the spike, near-cut
zone frozen to the reference wall, bands derived from the spline
representation error, the march resolution ladder and the gradient
floor on the reference wall; the sign-flipped rejector with its
calibrated segment budget) run on the member the full-expansion A/B
needs (CASES/raoplug_ch4o2/run_val_repro, CH4/O2 frozen gas, L 5.926,
closes on the axis). The driver, the design representation, the checks
and the bands are rao1961_sqp_return's own functions, imported; only the
world is replaced (ourworld_geno: gas VERIFIED against the field,
ambient = the member's lip ambient), the tip is pinned at the member's
y_D = 3.8e-4 (the axis), and the scales follow the member:
RAO_X0 default 1.50 (0.25 of x_D), RAO_K default 161.

PRE-REGISTERED (R5) = rao1961_sqp_return v2, unchanged:
  P1 every accepted base certified; P2 |grad J(W*)| <= K_RICH x the
  gradient floor measured on the reference wall; P3 RETURN inside
  band_W = K(e_rep + g/c); P4a J(W*) > J(W_pert); P4b |J(W*) - J_fit| <=
  band_J; R1 the sign-flipped driver ends FARTHER from the reference.
FALSIFIER: P3 failing with P2 passing = the driver converges elsewhere
-> the classical optimum is not the SQP's optimum in our world (a
finding about the A/B, to be attributed before any gain is claimed).

ON-DEMAND CARRIER (env: jax + the GENO run directory; the Rao-world
run of record took 2910 s at K = 81).
Run:  .venv-a1/bin/python validation/ourworld_sqp_return.py
"""
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import ourworld_geno as OW                             # noqa: E402

os.environ.setdefault("RAO_X0", "1.50")
os.environ.setdefault("RAO_K", "161")
os.environ["RAO_GENO_RUN"] = OW.RUN
import rao1961_sqp_return as R                         # noqa: E402

K_RICH = R.K_RICH
NPASS = [0, 0]


def check(label, ok):
    NPASS[1] += 1
    NPASS[0] += int(bool(ok))
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def main():
    t0 = time.time()
    print("== [F3] SQP-return in OUR world: perturbed start -> back to GENO's"
          " ideal spike? ==")
    if not os.path.isdir(OW.RUN):
        print("   OW_GENO_RUN not a directory -- nothing to do")
        return 2
    Wd = OW.load_world()
    OW.install(R, Wd)
    print("   instrument: rao1961_sqp_return v2 (X0 %.2f, K %d, M %d, PERT %.3f,"
          " FREEZE %.2f, SEG %d, SEG_R1 %d)"
          % (R.X0, R.K_ST, R.M_NODES, R.PERT, R.FREEZE, R.MAXSEG, R.SEG_R1))
    w = R.setup()

    print("-- S1: the reference in spline space and the derived bands --")
    e_rep = R.wall_dist(w.W_fit, w)
    out_fit, S_fit = R.march_record(w.W_fit, w)
    J_fit, g_fit = R.J_and_grad(w.W_fit, w, S_fit)
    g_floor = float(np.max(np.abs(g_fit)))
    gtol = K_RICH * g_floor
    out_fit2, _ = R.march_record(w.W_fit, w, K=2 * R.K_ST - 1)
    J_fit2 = float(w.F_in + R.push_of(out_fit2, w))
    print("  e_rep (spline vs GENO wall) max %.3e" % e_rep)
    print("  W_fit record cert %.3e; J_fit %.8e (K=%d) vs %.8e (K=%d): |dJ| %.3e"
          % (float(out_fit["cert_worst"]), J_fit, R.K_ST, J_fit2,
             2 * R.K_ST - 1, abs(J_fit - J_fit2)))
    print("  grad floor |g(W_fit)|inf %.3e -> gtol %.3e" % (g_floor, gtol))

    print("-- S2: the perturbed start (%.1f percent, alternating) --"
          % (100 * R.PERT))
    sgn = np.array([(-1.0) ** k for k in range(len(w.W_fit))])
    W_p = w.W_fit * (1.0 + R.PERT * sgn)
    d_start = R.wall_dist(W_p, w)
    out_p, S_p = R.march_record(W_p, w)
    J_p, g_p = R.J_and_grad(W_p, w, S_p)
    c_hat = 2.0 * max(J_fit - J_p, 1e-300) / d_start ** 2
    band_loc = g_floor / c_hat
    band_W = K_RICH * (e_rep + band_loc)
    band_J = K_RICH * abs(J_fit - J_fit2) + float(np.sum(np.abs(g_fit))) * band_W
    print("  start: dist to GENO %.3e; cert %.3e; J_p %.8e (J_fit - J_p = %+.4e);"
          " |grad|inf %.3e" % (d_start, float(out_p["cert_worst"]), J_p,
                               J_fit - J_p, np.max(np.abs(g_p))))
    print("  curvature c_hat %.3e -> location floor g/c %.3e; band_W = K(e_rep + g/c)"
          " = %.3e (start = %.1fx band_W); band_J %.3e"
          % (c_hat, band_loc, band_W, d_start / band_W, band_J))

    print("-- S3: TR-SQP (maximize) from the perturbed start --")
    W_s, J_s, g_s, n_rec, wc = R.run_trsqp(W_p, w, +1.0, tag="max ")
    d_s = R.wall_dist(W_s, w)
    print("  result: %d records, worst accepted cert %.3e; J* %.8e"
          " (J* - J_fit = %+.4e, J* - J_p = %+.4e); |grad|inf %.3e; dist %.3e"
          % (n_rec, wc, J_s, J_s - J_fit, J_s - J_p, np.max(np.abs(g_s)), d_s))
    check("P1 every accepted base certified (worst %.3e <= 1)" % wc, wc <= 1.0)
    check("P2 CONVERGENCE |grad J(W*)|inf %.3e <= gtol %.3e"
          % (np.max(np.abs(g_s)), gtol), np.max(np.abs(g_s)) <= gtol)
    check("P3 RETURN max|y(W*) - y_GENO| %.3e <= band_W %.3e (start was %.1fx)"
          % (d_s, band_W, d_start / band_W), d_s <= band_W)
    check("P4a VALUE J(W*) > J(W_pert) (+%.4e)" % (J_s - J_p), J_s > J_p)
    check("P4b VALUE |J(W*) - J(W_fit)| %.3e <= band_J %.3e"
          % (abs(J_s - J_fit), band_J), abs(J_s - J_fit) <= band_J)

    print("-- S4: R1 rejector - the sign-flipped objective from the same start --")
    W_r, J_r, _, n_r, _ = R.run_trsqp(W_p, w, -1.0, max_segments=R.SEG_R1,
                                       tag="min ")
    d_r = R.wall_dist(W_r, w)
    print("  minimizer: %d records; J %.8e (J_p - J = %+.4e); dist to GENO %.3e"
          " (start %.3e)" % (n_r, J_r, J_p - J_r, d_r, d_start))
    check("R1 REJECTOR: sign-flipped driver ends FARTHER from GENO (%.3e > %.3e)"
          % (d_r, d_start), d_r > d_start)

    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    print("VERDICT: %s" % ("PASS -- the SQP returns to GENO's ideal spike in OUR "
                           "world (plug-sector O3.3, motion half)"
                           if NPASS[0] == NPASS[1] else "FAIL"))
    return 0 if NPASS[0] == NPASS[1] else 1


if __name__ == "__main__":
    sys.exit(main())
