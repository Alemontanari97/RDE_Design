"""[F3] OUR WORLD, PLUG-SECTOR O3.3 (value half): is GENO's axisymmetric
ideal spike stationary for OUR thrust functional under OUR march, in
OUR gas?

The rao1961_o33 instrument transported from Rao's world (gamma 1.23,
truncated spike, p_b = 0 base term) to the member the full-expansion A/B
needs (CASES/raoplug_ch4o2/run_val_repro: CH4/O2 frozen gas, theta_E =
-0.02 deg, L = 5.926, the C- curve reaches the axis, y_D = 3.8e-4).
World posing: ourworld_geno (gas VERIFIED against the field; ambient =
the member's lip ambient from raoplug_performance.dat).

PRE-REGISTERED (R5), mirroring rao1961_o33 v2 with the re-posing the
axis-closing member forces, DECLARED here before the first run:
  P1  the reference record certifies (worst <= 1);
  P2  STATIONARITY: the six interior projected AD gradients (endpoint-
      pinned Gaussian bumps, support excluded from the first 0.35 L_r
      after the cut -- the rao1961_o33 v2 instrument zone) are ~ 0
      inside their own FD-Richardson + ripple bands;
  N2  negative control: a bump-perturbed wall is NOT stationary
      (max |g| > 10x the reference's);
  P3  MAXIMUM: J(reference) > J(perturbed wall);
  T   tip direction REPORTED (not gated): Rao's base balance
      dJ_wall/dy_D = 2 pi y_D p_a with y_D = 3.8e-4 m predicts a tip
      gradient ~ 1.8e3 N/m -- at the axis the base term vanishes by
      construction, so the Rao-world N1 (tip gradient NONZERO) and P4
      (Eq. (9) corner relation, a gamma-const truncated-plug identity)
      are N/A for this member and are not posed.
Scales (declared): bump amplitude T_H and control amplitude A_PERT are
the Rao-world 5e-3 / 1e-2 times the design-length ratio 5.04
(L 5.926 / 1.177); stations RAO_K default 161 (twice the Rao-world 81:
the spike is 2.2x longer in lip radii); cut RAO_X0 default 1.50 (0.25
of x_D, as 0.30 of 1.18).
FALSIFIER: P2 failing = the classical optimum is NOT stationary for the
functional the SQP consumes in our world -> the A/B is void until the
cause is attributed (instrument zone first, as in the Rao-world v1).

ON-DEMAND CARRIER (env: jax + the GENO run directory; ~10 min on s2).
Run:  .venv-a1/bin/python validation/ourworld_o33.py
"""
import os
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import ourworld_geno as OW                             # noqa: E402
import a1_ideal_march_jax as A1                        # noqa: E402
from a1_plug_march import plug_march, col_fluxes       # noqa: E402
from rao1961_twin import start_from_geno, EDGE_FILL   # noqa: E402

K_RICH = A1.K_RICH
X0 = float(os.environ.get("RAO_X0", 1.50))
N_ROW = int(os.environ.get("RAO_N", 61))
K_ST = int(os.environ.get("RAO_K", 161))
L_RATIO = 5.926 / 1.1766          # this member's x_D over the Rao-world x_D
T_H = 5.0e-3 * L_RATIO            # bump amplitude scale [m]
A_PERT = 0.01 * L_RATIO           # the non-optimal control wall (bump 3)
NPASS = [0, 0]


def check(label, ok):
    NPASS[1] += 1
    NPASS[0] += int(bool(ok))
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def main():
    t0 = time.time()
    print("== [F3] OUR world O3.3 for the plug: GENO's ideal spike vs OUR "
          "AD gradient ==")
    if not os.path.isdir(OW.RUN):
        print("   OW_GENO_RUN not a directory -- nothing to do")
        return 2
    W = OW.load_world()
    fld, wall, tab, ta, pa, qpa = (W["fld"], W["wall"], W["tab"], W["ta"],
                                   W["pa"], W["qpa"])
    xD = float(wall[-1, 0])

    start, ytop = start_from_geno(fld, wall, X0, N_ROW)
    stl = np.stack([np.full(len(start[1]), X0), start[1], start[2],
                    start[3]], 1)
    md_in, F_in = col_fluxes(stl, ta, pa, 1.0)
    print("   start line: %d rows at x0=%.2f; mass %.6g kg/s; F_in %.6g N;"
          " x_D=%.4f; K=%d; T_H=%.3e A_PERT=%.3e"
          % (len(start[1]), X0, abs(md_in), F_in, xD, K_ST, T_H, A_PERT))

    xj = np.linspace(X0, xD, K_ST + 1)[1:]
    dx = float(xj[1] - xj[0])
    yw = np.interp(xj, wall[:, 0], wall[:, 1])
    xjj = jnp.array(xj)
    Lr = xD - X0
    cent = X0 + Lr * np.array([0.40, 0.49, 0.58, 0.67, 0.76, 0.85])
    sig = 0.06 * Lr

    def window(x):
        wlo = jnp.clip((x - X0) / (0.25 * Lr), 0.0, 1.0)
        whi = jnp.clip((xD - x) / (0.10 * Lr), 0.0, 1.0)
        return (wlo * wlo * (3 - 2 * wlo)) * (whi * whi * (3 - 2 * whi))

    def shaped(a):
        y = jnp.array(yw)
        for k in range(6):
            b = jnp.exp(-0.5 * ((xjj - cent[k]) / sig) ** 2) * window(xjj)
            y = y + a[k] * b
        blip = jnp.exp(-0.5 * ((xjj - xD) / (0.10 * Lr)) ** 2)
        y = y + a[6] * blip
        s = jnp.gradient(y) / dx
        return xjj, y, s

    def push_of(out):
        w = out["wall"]
        q = jnp.sqrt(w[:, 2] ** 2 + w[:, 3] ** 2)
        pw = A1.state_q(q, ta)[1]
        dy = w[1:, 1] - w[:-1, 1]
        wgt = 2.0 * jnp.pi * 0.5 * (w[1:, 1] + w[:-1, 1])
        pm = 0.5 * (pw[1:] + pw[:-1])
        return jnp.sum((pm - pa) * wgt * (-dy))

    print("-- S1: record at GENO's wall; replay-differentiable J(a) --")
    st = tuple(np.asarray(v) for v in shaped(jnp.zeros(7)))
    out0, S0 = plug_march(st, start, qpa, tab, 1.0, edge_fill=EDGE_FILL)
    cert0 = float(out0["cert_worst"])
    J0 = float(F_in + push_of(out0))
    print("  cert %.3e (n=%d, worst at %s); J(ref) = %.8e N (push %.6g)"
          % (cert0, out0["cert_n"], out0["cert_where"], J0, J0 - F_in))
    check("P1 the reference record certifies (worst <= 1)", cert0 <= 1.0)

    def Jfun(a):
        o, _ = plug_march(shaped(a), start, qpa, tab, 1.0,
                          sched=A1.Sched("play", S0.d), edge_fill=EDGE_FILL)
        return F_in + push_of(o)

    gvec = np.array(jax.grad(Jfun)(jnp.zeros(7)))
    print("  AD projected gradient: interior %s ; tip %+.4e"
          % (" ".join("%+.2e" % v for v in gvec[:6]), gvec[6]))

    print("-- S2: FD bands per interior direction (t, t/2 Richardson + ripple) --")
    okall = True
    for k in range(6):
        e = jnp.zeros(7).at[k].set(1.0)
        fd, Jv = {}, {}
        for tt in (T_H, 0.5 * T_H):
            Jp = float(Jfun(tt * e)); Jm = float(Jfun(-tt * e))
            fd[tt] = (Jp - Jm) / (2 * tt); Jv[tt] = (Jp, Jm)
        rip = abs(Jv[T_H][0] + Jv[T_H][1] - 2 * J0) * 0.5
        band = K_RICH * (abs(fd[T_H] - fd[0.5 * T_H]) + rip / T_H)
        ok = abs(gvec[k]) <= band and abs(fd[0.5 * T_H]) <= band
        okall &= ok
        print("    dir %d: AD %+.3e FD %+.3e band %.3e  %s"
              % (k, gvec[k], fd[0.5 * T_H], band, "PASS" if ok else "FAIL"),
              flush=True)
    check("P2 STATIONARITY: all 6 interior directions ~ 0 in band", okall)

    e = jnp.zeros(7).at[6].set(1.0)
    fdl = (float(Jfun(T_H * e)) - float(Jfun(-T_H * e))) / (2 * T_H)
    fdl2 = (float(Jfun(0.5 * T_H * e)) - float(Jfun(-0.5 * T_H * e))) / T_H
    bandl = K_RICH * abs(fdl - fdl2)
    yD = float(yw[-1])
    pred = 2.0 * np.pi * yD * pa
    print("  tip direction (REPORTED, axis-closing member): AD %+.4e  FD %+.4e"
          "  band %.3e; base balance 2 pi y_D p_a = %+.4e (y_D %.2e)"
          % (gvec[6], fdl, bandl, pred, yD))

    print("-- S3: negative control - a non-optimal wall (bump 3, %.3f) --" % A_PERT)
    a_p = jnp.zeros(7).at[2].set(A_PERT)
    stp = tuple(np.asarray(v) for v in shaped(a_p))
    out_p, S_p = plug_march(stp, start, qpa, tab, 1.0, edge_fill=EDGE_FILL)
    Jp = float(F_in + push_of(out_p))

    def Jfun_p(a):
        o, _ = plug_march(shaped(a), start, qpa, tab, 1.0,
                          sched=A1.Sched("play", S_p.d), edge_fill=EDGE_FILL)
        return F_in + push_of(o)
    gp = np.array(jax.grad(Jfun_p)(a_p))
    print("  perturbed record cert %.3e; J(pert) = %.8e  (J_ref - J_pert = %+.4e)"
          % (float(out_p["cert_worst"]), Jp, J0 - Jp))
    print("  perturbed interior grad: %s" % " ".join("%+.2e" % v for v in gp[:6]))
    check("N2 negative control: perturbed wall NOT stationary (max |g| > 10x ref)",
          np.max(np.abs(gp[:6])) > 10.0 * np.max(np.abs(gvec[:6])))
    check("P3 MAXIMUM: J(GENO) > J(perturbed wall)", J0 > Jp)

    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    print("VERDICT: %s" % ("PASS -- GENO's ideal spike is stationary for our "
                           "functional under our march in OUR world (plug-sector "
                           "O3.3, value half)" if NPASS[0] == NPASS[1] else "FAIL"))
    return 0 if NPASS[0] == NPASS[1] else 1


if __name__ == "__main__":
    sys.exit(main())
