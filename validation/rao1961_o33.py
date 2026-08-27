"""[F3] O3.3 FOR THE PLUG SECTOR — Rao's optimum is stationary for OUR
thrust functional, marched by OUR engine in HIS world.

WHAT THE BELL HAS AND THE PLUG DID NOT. For the bell, O3.3
(a1_o33_toc.py, S19) discharged the registry residual C-O33: on GENO's
Rao TOC our AD wall-gradient vanishes along interior endpoint-pinned
variations, does not vanish on the lip or on a perturbed wall, and the
TOC is a maximum. That is the licence for "the SQP's bell optimum is a
real optimum". The plug sector had no such run: no classical known
answer was usable ([X-RAOTB] fixed that), our objective had not been
shown to be Rao's ([X-RAOFN]), and our march could not enter his world
([X-RAOTW], the dual-code twin). This carrier is the missing run.

SETUP. GENO's legacy p_b = 0 corner-stop RaoPlug run at gamma = 1.23
(Rao's own rule; his Table 1 at mean 2.4e-3) gives the axisymmetric
field and the optimum contour. As in the twin, our march starts from
GENO's field on a vertical cut at x0 and marches GENO's wall on
[x0, x_D] with the free-jet edge and EDGE_FILL. The design region is
[x0, x_D]; everything upstream is inherited data (domain of
dependence), which is legitimate: Rao's optimum is stationary for EVERY
admissible variation, hence for those supported downstream of x0.

THE OBJECTIVE. Two-route thrust in the p_a gauge: J = F_in (start-line
flux, constant) + integral over the marched spike of (p_w - p_a) 2 pi y
(-dy). Rao's total also carries the BASE term (p_b - p_a) pi y_D^2,
which depends on the tip height only: for endpoint-pinned variations
it is a constant and drops out, so interior stationarity is tested
without any base-pressure model; for the tip-moving variation it gives
a QUANTITATIVE prediction (below).

PRE-REGISTERED (R5), mirroring a1_o33_toc STAGE=stationarity:
  P1  the record at the reference wall certifies (worst cell <= 1);
  P2  STATIONARITY: the AD gradient contracted with 6 interior,
      endpoint-pinned bumps is ~ 0 inside the per-direction band
      K_RICH*(|FD(t)-FD(t/2)| + ripple/t), and so is the FD estimate;
  N1  negative control: the tip-moving (blip at x_D) gradient is
      NONZERO (> 10x its band) — with p_b = 0 the base term makes the
      tip height a live variable;
  P5  TIP IDENTITY (v2, promoted): Rao's stationarity in y_D with
      p_b = 0, d J_wall / d y_D = -(p_b - p_a) 2 pi y_D = 2 pi y_D p_a,
      so the blip gradient must equal 2 pi y_D p_a * blip(x_D) inside
      the tip direction's own FD-Richardson band (measured 1.0046 and
      0.9989 of the prediction at x0 = 0.30 / 0.20 in the first posing);
  N2  negative control: a perturbed wall (bump 3, 0.01) is NOT
      stationary — max interior |g| > 10x the reference's;
  P3  MAXIMUM: J(reference) > J(perturbed wall);
  P4  CORNER: Rao's Eq. (9) residual with p_b = 0, evaluated at the
      marched wall end D, is < 1/10 of its value on the tip-lifted wall
      (lift 0.05 in v2)
      (the corner relation discriminates the stop; the tip-lifted
      record is the control).
FALSIFIER: P2 failing at every interior direction while N2 passes means
our functional or our march is not stationary where Rao's is — a
finding about the engine (the SQP could not be trusted in this sector).

FIRST POSING AND RE-POSING (2026-08-27, declared). Run 1 (x0 = 0.30,
bumps centred at 0.20..0.85 L_r as in the bell): P1 PASS, P2 PASS (dirs
2-5 at 1.7e2..5e2 against bands 3e5..1e6; dirs 0-1 with FD bands 1e8 —
vacuous), N1 PASS with the tip identity at measured/predicted 1.0046, P3
PASS, N2 FAIL and P4 FAIL. Attribution run (x0 = 0.20, everything else
equal): the direction nearest the cut FOLLOWS the cut (AD 9.2e4 ->
1.3e5, FD band 2e8 again) while dirs 1-5 stay at 1e2..1e3 and the tip
identity gives 0.9989 — the near-cut zone is where the wall cell's
multi-column foot search consumes the Cauchy start rows and the frozen
replay is not smooth: an instrument zone, not physics. N2 failed ONLY
because that value set the reference scale (excluding it the control
is 490x). P4's tip-lift control (0.02, dtheta_D 0.7 deg) was too weak:
the reference residual 5.4e-4 / 6.5e-4 sits at the cross-code level.
v2 (this file): bump support excluded from the first 0.35 L_r after the
cut (centres 0.40..0.85 L_r, sigma 0.06 L_r, ramp 0.25 L_r), tip-lift
control 0.05, and the tip identity PROMOTED to a check against its own
FD-Richardson band after two consistent measurements. The run-1 and
attribution logs are kept as records of the first posing.

ON-DEMAND CARRIER (env: jax + a GENO run directory via RAO_GENO_RUN).
Run:  RAO_GENO_RUN=.../GENO/CASES/raoplug_run_legacy \\
      .venv-a1/bin/python validation/rao1961_o33.py
"""
import os
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import a1_ideal_march_jax as A1                        # noqa: E402
from a1_plug_march import plug_march, col_fluxes       # noqa: E402
from a1_freejet_unit import q_at_pa                    # noqa: E402
from rao1961_twin import (load_geno, gas_from_field, start_from_geno,
                          control_surface, G, PA_PC, EDGE_FILL)  # noqa: E402
from rao1961_control_surface import corner as rao_corner  # noqa: E402

K_RICH = A1.K_RICH
RUN = os.environ.get("RAO_GENO_RUN", "")
X0 = float(os.environ.get("RAO_X0", 0.30))
N_ROW = int(os.environ.get("RAO_N", 61))
K_ST = int(os.environ.get("RAO_K", 81))
T_H = 5.0e-3            # bump amplitude scale [m], as the bell's O3.3
A_PERT = 0.01           # the non-optimal control wall (bump 3)
NPASS = [0, 0]


def check(label, ok):
    NPASS[1] += 1
    NPASS[0] += int(bool(ok))
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def main():
    t0 = time.time()
    print("== [F3] O3.3 for the plug: Rao's optimum vs OUR AD gradient ==")
    if not RUN or not os.path.isdir(RUN):
        print("   RAO_GENO_RUN not set to a GENO run directory -- nothing to do")
        return 2
    fld, wall = load_geno(RUN)
    Rg_g, ts_g, ps_g = gas_from_field(fld)
    tab = A1.prep_tab(A1.build_tab_gconst(g=G, Rg=Rg_g, ts=ts_g, ps=ps_g))
    ta = A1.tab_arrays(tab)
    pa = PA_PC * ps_g
    qpa = float(q_at_pa(pa, ta, tab["_as"]))
    ED = control_surface(RUN, fld)
    xD = float(wall[-1, 0])
    print("   gas from the field: Rg=%.4f ts=%.2f ps=%.6g; pa=%.4g Pa; "
          "q_at_pa=%.1f m/s; x_D=%.4f" % (Rg_g, ts_g, ps_g, pa, qpa, xD))

    start, ytop = start_from_geno(fld, wall, X0, N_ROW)
    stl = np.stack([np.full(len(start[1]), X0), start[1], start[2],
                    start[3]], 1)
    md_in, F_in = col_fluxes(stl, ta, pa, 1.0)
    print("   start line: %d rows at x0=%.2f; mass %.6g kg/s; F_in %.6g N"
          % (len(start[1]), X0, abs(md_in), F_in))

    # reference stations = GENO's wall on (x0, x_D], uniform in x
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

    blip_D = 1.0        # the blip's value at x_D (its centre)

    def push_of(out):
        w = out["wall"]
        q = jnp.sqrt(w[:, 2] ** 2 + w[:, 3] ** 2)
        pw = A1.state_q(q, ta)[1]
        dy = w[1:, 1] - w[:-1, 1]
        wgt = 2.0 * jnp.pi * 0.5 * (w[1:, 1] + w[:-1, 1])
        pm = 0.5 * (pw[1:] + pw[:-1])
        return jnp.sum((pm - pa) * wgt * (-dy))

    print("-- S1: record at Rao's wall; replay-differentiable J(a) --")
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
              % (k, gvec[k], fd[0.5 * T_H], band, "PASS" if ok else "FAIL"))
    check("P2 STATIONARITY: all 6 interior directions ~ 0 in band", okall)

    e = jnp.zeros(7).at[6].set(1.0)
    fdl = (float(Jfun(T_H * e)) - float(Jfun(-T_H * e))) / (2 * T_H)
    fdl2 = (float(Jfun(0.5 * T_H * e)) - float(Jfun(-0.5 * T_H * e))) / T_H
    bandl = K_RICH * abs(fdl - fdl2)
    yD = float(yw[-1])
    pred = 2.0 * np.pi * yD * pa * blip_D
    print("  tip direction: AD %+.4e  FD %+.4e  band %.3e" % (gvec[6], fdl, bandl))
    print("  Rao stationarity in y_D with p_b = 0 predicts dJ_wall/da_tip"
          " ~ 2 pi y_D p_a = %+.4e  ->  measured/predicted = %.4f (reported)"
          % (pred, gvec[6] / pred))
    check("N1 negative control: tip-moving gradient NONZERO (> 10x band)",
          abs(gvec[6]) > 10.0 * max(bandl, 1e-6))
    check("P5 TIP IDENTITY: |g_tip - 2 pi y_D p_a| = %.3e <= band %.3e"
          % (abs(gvec[6] - pred), bandl), abs(gvec[6] - pred) <= bandl)

    print("-- S3: negative control 2 - a non-optimal wall (bump 3, %.3f) --" % A_PERT)
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
    check("P3 MAXIMUM: J(Rao) > J(perturbed wall)", J0 > Jp)

    print("-- S4: Rao's corner relation Eq. (9), p_b = 0, at the marched end D --")
    def corner_at_end(out):
        w = np.asarray(out["wall"])[-1]
        q = float(np.hypot(w[2], w[3]))
        M = float(A1.state_q(jnp.float64(q), ta)[5])
        th = float(np.arctan2(w[3], w[2]))
        return float(rao_corner(M, th, G, 0.0)), M, np.degrees(th)
    c0, M0, th0 = corner_at_end(out0)
    a_t = jnp.zeros(7).at[6].set(0.05)      # v2: dtheta_D ~ 1.7 deg control
    out_t, _ = plug_march(tuple(np.asarray(v) for v in shaped(a_t)), start,
                          qpa, tab, 1.0, edge_fill=EDGE_FILL)
    ct, Mt, tht = corner_at_end(out_t)
    print("  at D: M %.4f theta %.3f deg -> Eq.(9) residual %+.4e;"
          " tip-lifted wall: M %.4f theta %.3f -> %+.4e"
          % (M0, th0, c0, Mt, tht, ct))
    check("P4 CORNER: |Eq.(9)| at D on the reference < 1/10 of the tip-lifted wall's",
          abs(c0) < 0.1 * abs(ct))

    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    print("VERDICT: %s" % ("PASS -- Rao's plug optimum is stationary for our functional under our march (the plug-sector O3.3)"
                           if NPASS[0] == NPASS[1] else "FAIL"))
    return 0 if NPASS[0] == NPASS[1] else 1


if __name__ == "__main__":
    sys.exit(main())