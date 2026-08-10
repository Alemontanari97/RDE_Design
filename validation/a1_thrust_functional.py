#!/usr/bin/env python3
"""A1 BRICK 2, STEP 1 [F2/A1]: THE THRUST FUNCTIONAL AND ITS GRADIENT on
the assembled differentiable march (validation/a1_ideal_march_jax.py =
Brick 1; one ADDITIVE change there: run_march also returns wall_u/wall_v,
the wall state vectors it already computed).

WHAT THIS CARRIER ADDS (and Brick 1 deliberately did not have): a scalar
objective J[design] and its exact reverse-mode gradient dJ/dP. Until this
file the march generated contours but nothing scored them; after it the
engine has a notion of "better" and a verified search direction — the two
prerequisites of profile optimization (M0 T7; plan D6 item 9, NEXT-1).

J IS COMPUTED BY TWO INDEPENDENT ROUTES; THEIR AGREEMENT IS THE TEST
(steady momentum theorem = M0 Theorem 0(i) with no storage term):

  EXIT form (the objective).  On the ideal (type-0) nozzle the exit
  region is UNIFORM at the achieved Mach Me with axial flow (the march's
  own construction: focus K, straightening, mass-flow streamline wall):
      J_exit = mdot * q_e + (p_e - pa) * pi * y_lip^2
  q_e solved through the march's own resid_qofM unit process (implicit
  rule => exact reverse derivative); p_e from the tabulated EOS-general
  isentrope; y_lip = last wall point. Differentiable end-to-end.

  WALL+IVL form (the referee).  Control volume = Sauer IVL + wall + exit
  + axis. v = 0 on the IVL and no through-flow on the wall give
      J_exit = F_ivl + W_wall,
      F_ivl  = Int_0^yt (rho u^2 + p - pa) 2 pi y dy   (the march's own
               IVL nodes and Simpson weights),
      W_wall = Int_wall (p - pa) 2 pi y dy             (trapezoid on the
               wall nodes; p from the wall speed via the same closure).
  R_mom := J_exit - F_ivl - W_wall must sit inside a DERIVED band. Not a
  tautology: the exit route never reads wall pressures; the referee
  route never reads the exit state.

DERIVED TOLERANCES (R5: no magic numbers).
  * momentum residual: wall trapezoid + march are 2nd-order; Richardson
    band from the coarse (NI, da, Ne) vs refined (2NI-1, da/2, 2Ne-1)
    marches: band = K_RICH*|R_c - R_f| + C_FLOOR*eps*scale(J). PASS =
    |R_f| <= band.
  * gauge invariance: R_mom at pa = 0 vs pa = p_e/2 equal to roundoff
    (a constant integrates to zero over a closed surface): 64 eps scale.
  * gradient: reverse-mode dJ/dP vs central differences, per-component
    Richardson band K_RICH*|FD(h) - FD(h/2)| + floor; plus the scalar
    dot-product identity <grad J, v> vs jvp at machine.

REJECTORS (a suite must be able to say NO):
  * R1 sign flip: negate W_wall -> residual leaves the band.
  * R2 dropped physics: omit the pressure-area exit term -> ditto.
  * R3 gradient corruption: permuted-gradient FD check must FAIL.

SCOPE (declared): single phase, shock-free, type-0 generated wall; pa is
a gauge (no separation model); design space = the existing P = [yt, rtu,
rtd, eps]. The prescribed-wall (spline) march is the next brick.

Run:  .venv-a1/bin/python validation/a1_thrust_functional.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1  # noqa: E402  (Brick 1)

import jax  # noqa: E402
import jax.numpy as jnp  # noqa: E402

EPS = A1.EPS
CASE = A1.CASE
K_RICH = A1.K_RICH
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ----------------------------------------------------------------------
# the two routes
# ----------------------------------------------------------------------
def solve_qe(Me, ta, as_seed=None):
    t = A1.get_solver(("qme", 0), lambda: A1.resid_qofM)
    z0 = jnp.array([2.0 * (as_seed if as_seed is not None else 1000.0)])
    z = t[0](z0, jnp.array([Me]), ta)
    return z[0]


def J_exit_of_out(out, ta, as_seed=None, pa=0.0):
    qe = solve_qe(out["Me"], ta, as_seed)
    _, pe, _, _, _, _ = A1.state_q(qe, ta)
    ylip = out["wall_y"][-1]
    return out["mdot"] * qe + (pe - pa) * jnp.pi * ylip**2


def ivl_flux(P, tab, ta, pa=0.0):
    """Axial momentum+pressure flux through the Sauer IVL (v=0 there, so
    the projected area element is exactly 2 pi y dy). Same nodes and
    Simpson weights as the march; the same-node mass flow is returned as
    a self-consistency rejector for this replica."""
    NI = CASE["NI"]
    gm, as_ = tab["gammamedio"], tab["_as"]
    yt, rtu = P[0], P[1]
    delta = 1.0
    alpha = jnp.sqrt((1.0 + delta) / ((gm + 1.0) * rtu * yt))
    c1 = -(gm + 1.0) * alpha / (2.0 * (3.0 + delta))
    c2 = (gm + 1.0) * alpha**2 / (2.0 * (1.0 + delta))
    jj = jnp.arange(NI)
    y = yt * (1.0 - jj / (NI - 1.0))
    u = as_ * (1.0 + alpha * (c1 * y**2 + 0.000001) + c2 * y**2)
    _, p, rho, _, _, _ = A1.state_q(u, ta)
    w = np.ones(NI)
    w[1:-1:2], w[2:-1:2] = 4.0, 2.0
    w = jnp.array(w)
    yy = y[::-1]
    h = yy[1] - yy[0]
    F = 2.0 * jnp.pi * h / 3.0 * jnp.sum(w * ((rho * u**2 + p - pa) * y)[::-1])
    md = 2.0 * jnp.pi * h / 3.0 * jnp.sum(w * (rho * u * y)[::-1])
    return F, md


def ivl_top(P, tab):
    """State at the IVL's wall-end node (y = yt): the point that CLOSES
    the control surface between the IVL and the first wall-polyline
    node. Same Sauer formulas as the march."""
    gm, as_ = tab["gammamedio"], tab["_as"]
    yt, rtu = P[0], P[1]
    delta = 1.0
    alpha = jnp.sqrt((1.0 + delta) / ((gm + 1.0) * rtu * yt))
    c1 = -(gm + 1.0) * alpha / (2.0 * (3.0 + delta))
    c2 = (gm + 1.0) * alpha**2 / (2.0 * (1.0 + delta))
    u0 = as_ * (1.0 + alpha * (c1 * yt**2 + 0.000001) + c2 * yt**2)
    return yt, u0


def wall_push(out, ta, pa=0.0, close=None):
    """Pressure push of the wall on the gas: Int (p-pa) 2 pi y dy over
    the wall polyline (trapezoid; p from the wall speed). close=(y0,u0)
    prepends the IVL top node so the control surface CLOSES exactly —
    without it a sliver of wall between the IVL and the first polyline
    node is uncovered, and the gauge test (rightly) fails."""
    q = jnp.sqrt(out["wall_u"]**2 + out["wall_v"]**2)
    y = out["wall_y"]
    if close is not None:
        y0, u0 = close
        q = jnp.concatenate([jnp.array([u0]), q])
        y = jnp.concatenate([jnp.array([y0]), y])
    _, p, _, _, _, _ = A1.state_q(q, ta)
    f = (p - pa) * 2.0 * jnp.pi * y
    return jnp.sum(0.5 * (f[1:] + f[:-1]) * (y[1:] - y[:-1]))


def mom_residual(P, out, tab, ta, pa=0.0, flip_wall=False, drop_pe=False):
    Je = J_exit_of_out(out, ta, tab["_as"], pa)
    if drop_pe:
        qe = solve_qe(out["Me"], ta, tab["_as"])
        Je = out["mdot"] * qe                      # R2: physics dropped
    F, md = ivl_flux(P, tab, ta, pa)
    W = wall_push(out, ta, pa, close=ivl_top(P, tab))
    if flip_wall:
        W = -W                                     # R1: sign corruption
    return Je - F - W, md


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    print("== A1 brick 2 step 1: thrust functional + gradient [F2/A1] ==")
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    P0 = jnp.array([CASE["yt"], CASE["rtu"], CASE["rtd"], CASE["eps"]])
    cfg = dict(NI=CASE["NI"], Ne=CASE["Ne"], da_deg=CASE["da_deg"])

    # ---------------- S1: marches (coarse + Richardson refined)
    print("-- S1: adaptive marches, coarse and refined --")
    out, S = A1.run_march(P0, tab, cfg)
    cfg_f = dict(NI=2 * CASE["NI"] - 1, Ne=2 * CASE["Ne"] - 1,
                 da_deg=0.5 * CASE["da_deg"])
    out_f, S_f = A1.run_march(P0, tab, cfg_f)
    print("  coarse: Me=%.6f mdot=%.8e ylip=%.6f" %
          (out["Me"], out["mdot"], out["wall_y"][-1]))
    print("  fine  : Me=%.6f mdot=%.8e ylip=%.6f" %
          (out_f["Me"], out_f["mdot"], out_f["wall_y"][-1]))

    # ---------------- S2: the two routes + momentum-theorem band
    print("-- S2: J by two routes; momentum residual in Richardson band --")
    Jc = float(J_exit_of_out(out, ta, tab["_as"]))
    Jf = float(J_exit_of_out(out_f, ta, tab["_as"]))
    Rc, mdc = mom_residual(P0, out, tab, ta)
    # the refined referee must use the refined IVL (same NI as its march)
    NI_save = CASE["NI"]
    CASE["NI"] = cfg_f["NI"]
    Rf, mdf = mom_residual(P0, out_f, tab, ta)
    CASE["NI"] = NI_save
    Rc, Rf = float(Rc), float(Rf)
    scale = abs(Jf)
    band = K_RICH * abs(Rc - Rf) + A1.C_FLOOR * EPS * scale
    print("  J_exit  coarse/fine       = %.10e / %.10e" % (Jc, Jf))
    print("  R_mom   coarse/fine       = %+.3e / %+.3e" % (Rc, Rf))
    print("  Richardson band           = %.3e   (rel %.2e of J)"
          % (band, band / scale))
    check("momentum theorem: |R_f| <= band", abs(Rf) <= band)
    check("IVL replica mdot == march mdot (coarse, 1e3 eps)",
          abs(float(mdc) - float(out["mdot"])) <= 1e3 * EPS * float(out["mdot"]))
    conv = abs(Rc) / max(abs(Rf), 1e-300)
    print("  |R_c|/|R_f| = %.2f (2nd-order scheme: expect ~4)" % conv)

    # gauge invariance
    qe = solve_qe(out_f["Me"], ta, tab["_as"])
    _, pe, _, _, _, _ = A1.state_q(qe, ta)
    CASE["NI"] = cfg_f["NI"]
    Rg, _ = mom_residual(P0, out_f, tab, ta, pa=0.5 * float(pe))
    CASE["NI"] = NI_save
    dg = abs(float(Rg) - Rf)
    print("  gauge delta |R(pa)-R(0)|  = %.3e  (allowed %.3e)"
          % (dg, 64.0 * EPS * scale))
    check("gauge invariance |R(pa)-R(0)| <= 64 eps scale",
          dg <= 64.0 * EPS * scale)

    # rejectors R1, R2
    CASE["NI"] = cfg_f["NI"]
    R1, _ = mom_residual(P0, out_f, tab, ta, flip_wall=True)
    R2, _ = mom_residual(P0, out_f, tab, ta, drop_pe=True)
    CASE["NI"] = NI_save
    check("rejector R1 (wall sign flip) leaves band",
          abs(float(R1)) > 10.0 * band)
    check("rejector R2 (dropped p_e A_e term) leaves band",
          abs(float(R2)) > 10.0 * band)

    # ---------------- S3: gradient — reverse AD vs FD, + dot product
    print("-- S3: dJ/dP: reverse AD vs central FD (Richardson banded) --")

    def Jfun(P):
        o, _ = A1.run_march(P, tab, cfg, sched=S)
        return J_exit_of_out(o, ta, tab["_as"])

    g = jax.grad(Jfun)(P0)
    gnp = np.array(g)
    print("  grad J = [% .6e % .6e % .6e % .6e]" % tuple(gnp))

    names = ["yt", "rtu", "rtd", "eps"]
    ok_all = True
    hrel = 1e-4
    for i in range(4):
        h = hrel * max(1.0, abs(float(P0[i])))
        fd = {}
        for hh in (h, 0.5 * h):
            Pp = P0.at[i].add(hh)
            Pm = P0.at[i].add(-hh)
            fd[hh] = (float(Jfun(Pp)) - float(Jfun(Pm))) / (2.0 * hh)
        bandi = K_RICH * abs(fd[h] - fd[0.5 * h]) + A1.C_FLOOR * EPS * scale / h
        di = abs(fd[0.5 * h] - gnp[i])
        ok = di <= bandi
        ok_all &= ok
        print("    d/d%-3s AD=% .8e FD=% .8e |d|=%.2e band=%.2e %s"
              % (names[i], gnp[i], fd[0.5 * h], di, bandi,
                 "PASS" if ok else "FAIL"))
    check("gradient: all 4 components inside FD Richardson bands", ok_all)

    v = jnp.array([0.3, -0.7, 0.5, 0.9])
    dot_g = float(jnp.dot(g, v))

    def dirder(hsc):
        h = EPS ** (1.0 / 3.0) * hsc
        return (float(Jfun(P0 + h * v)) - float(Jfun(P0 - h * v))) / (2 * h)
    dv, dv2 = dirder(1.0), dirder(0.5)
    tol_dp = K_RICH * (abs(dv - dv2) + A1.C_FLOOR * EPS ** (2.0 / 3.0) * scale)
    dd = abs(dot_g - dv2)
    check("directional-derivative identity <grad,v> vs central FD",
          dd <= tol_dp)
    print("  <grad,v>=%.10e  FD_v=%.10e  |d|=%.2e (tol %.2e)"
          % (dot_g, dv2, dd, tol_dp))

    # rejector R3: a permuted gradient must FAIL the FD check
    gperm = gnp[[1, 0, 3, 2]]
    bad = 0
    for i in range(4):
        h = hrel * max(1.0, abs(float(P0[i])))
        Pp = P0.at[i].add(0.5 * h)
        Pm = P0.at[i].add(-0.5 * h)
        fdv = (float(Jfun(Pp)) - float(Jfun(Pm))) / h
        if abs(fdv - gperm[i]) > 1e-3 * max(1.0, abs(fdv)):
            bad += 1
    check("rejector R3 (permuted gradient) fails FD on >=2 components",
          bad >= 2)

    # ---------------- verdict
    print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
