#!/usr/bin/env python3
"""T10 (one walk) -- the model's SQP driver re-designing the plug of a GENO design, as in T08b, on two new problems:
  rao61_e381_pbR_mi15   Rao 1961's eps = 3.81 member (M_E 2.4, theta_E -8.25 deg, gamma 1.23) ended at Rao's printed
                        D (R_D 0.137): GENO's contour = Rao's Table 1 downstream of x_s
  axial_e381_RD04_mi15  axial exit: Rao's theta_E = 0 member (uniform axial flow at p_a on ED), plug ended at R_D 0.4,
                        base at p_a: its thrust is the bound mdot V_a of every contour
Posing (ref/rao_posing.py): GENO's last internal C+ (resampled to 56 points) + the lip E + 20 fan rays to p_a, 120
stations; the plug from x_s (where the lip's first wave lands) to D (pinned) is a cubic spline with 9 free knots.
Production switches of the driver as in T08b. The runner sets A1_NEWTON_RESCUE=1: Rao's eps 3.81 plug is so steep near
the throat that the default damped Newton stalls (C+ columns horizontal, theta + mu ~ 0; measured).
usage: t10_rao_walk.py <case> <start half|bump|cont:<start>> [floor_div]  -> out/t10_walk_<case>_<start>.json
  (env T10_TR0 / T10_FLOOR: the radius and its floor, default 0.01 and 0.01 / floor_div; T10_MAXITER: trust-constr
   iterations per segment, default 6 -- with 2 a segment is ONE step no longer than the radius, measured on a quadratic:
   maxiter 1/2/3/6 at radius 1e-3 -> step 0 / 1e-3 / 8e-3 / 2.8; T10_SEGS: segments, default 30;
   T10_METRIC=start: the production walker's Newton metric from the secant Hessian at the start, radius in W units)
  half = halfway between GENO's contour (spline fit) and the straight chord from (x_s, y_s) to D (the chord itself is
         not certified: the spline keeps GENO's steep slope at x_s and folds cells there, measured 4.9 and 8e15);
  bump = GENO's contour fitted by the spline + 0.01 sin(pi t)
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
os.environ.setdefault("PSPL_JSCALE", "radius")
os.environ.setdefault("PSPL_TRFOLLOW", "1")
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import rao_posing as RP                            # noqa: E402
import a1_plug_spline_opt as P                     # noqa: E402

case, start = sys.argv[1], sys.argv[2]
FDIV = float(sys.argv[3]) if len(sys.argv) > 3 else 256.0
tag = "t10_walk_%s_%s" % (case, start)
t00 = time.time()
rp = RP.RaoPosing(os.path.join(rv.RV, "geno", case), K=120, n_fan=20, m=10, design=True, n_cplus=56)
g = rp.g
W_fit = rp.fit_geno()
t = (rp.xk[:-1] - g.x_s) / (g.D[0] - g.x_s)
if start.startswith("cont:"):
    # continuation from a previous walk's landing (out/t10_walk_<case>_<start>.json), radius / floor from the env
    W0 = np.asarray(json.load(open(os.path.join(rv.OUT, "t10_walk_%s_%s.json" % (case, start[5:]))))["landing"]["W"])
    tag = "t10_walk_%s_cont_%s" % (case, start[5:])
elif start == "bump":
    W0 = W_fit + 0.01 * np.sin(np.pi * t)
else:
    W0 = 0.5 * (W_fit + g.y_s + (g.D[1] - g.y_s) * t)
TR0 = float(os.environ.get("T10_TR0", "0.01"))
MAXIT = int(os.environ.get("T10_MAXITER", "6"))       # trust-constr iterations per segment (2 = one step <= the radius)
SEGS = int(os.environ.get("T10_SEGS", "30"))
if MAXIT != 6 and start.startswith("cont:"):
    tag += "_it%d" % MAXIT
FLOOR = float(os.environ.get("T10_FLOOR", str(TR0 / FDIV)))
if P.DRIVER == "qntr":
    tag += "_qntr"      # the agnostic driver (a1_qntr, default since 2026-10-08): T10_MAXITER / T10_FLOOR are not used
out_g, _ = rp.march_record(None)
J_geno = float(rp.J_of(out_g))
bound = rp.mdot_start * rp.qpa


def reading(W, label):
    out, S = rp.march_record(W)
    J = float(rp.J_of(out))
    gr = np.asarray(jax.grad(lambda z: rp.J_replay(z, S))(jnp.asarray(W)))
    B, c = rp.basis()
    y = B @ np.asarray(W) + c
    dy = (y - rp.sy_g)[rp.free]
    r = dict(J=J, gap=J / J_geno - 1.0, over_bound=J / bound - 1.0, cert=float(out["cert_worst"]),
             grad_inf=float(np.max(np.abs(gr))) / J_geno, dy_max=float(np.max(np.abs(dy))),
             dy_rms=float(np.sqrt(np.mean(dy ** 2))), W=np.asarray(W).tolist(), y=y.tolist(), grad=gr.tolist())
    print("  %-8s J/J(GENO) - 1 = %+.4e | J/(mdot V_a) - 1 = %+.4e | max |y - y_GENO| %.3e | cert %.3f |"
          " |grad|_inf / J %.3e" % (label, r["gap"], r["over_bound"], r["dy_max"], r["cert"], r["grad_inf"]), flush=True)
    return r


print("== %s: J(GENO contour) %.10e (cert %.3f), mdot V_a %.10e; x_s %.5f -> D %s; rescue %s" % (
    tag, J_geno, float(out_g["cert_worst"]), bound, g.x_s, g.D, os.environ.get("A1_NEWTON_RESCUE")), flush=True)
r_fit = reading(W_fit, "fit")
r_0 = reading(W0, "start")
METRIC = os.environ.get("T10_METRIC", "")
if METRIC == "start":
    # the production walker's Newton metric (a1_twowall.walk, TWOP_METRIC=start): W = W0 + T z with
    # T = V diag(lam_eff^-1/2) from the secant Hessian of the frozen replay at the walk's own start (-H = V diag(lam) V^T,
    # lam floored at K_RICH x its asymmetry), scale h = the production's hess_steps[0] (1e-3), radius tr0 mapped to z
    import a1_twowall as TW
    tag += "_newton"
    _, S0 = rp.march_record(np.asarray(W0, float))
    gfun = jax.grad(lambda z: rp.J_replay(z, S0))
    Hs = TW.secant_hessian(gfun, np.asarray(W0, float), 1e-3)
    asym = float(np.max(np.abs(Hs - Hs.T)))
    lam, V = np.linalg.eigh(-0.5 * (Hs + Hs.T))
    lam_eff = np.maximum(lam, TW.K_RICH * asym)
    T = V @ np.diag(lam_eff ** -0.5)
    g0 = np.asarray(gfun(jnp.asarray(W0)))
    zlen = float(np.linalg.norm(T @ (T.T @ g0)) / np.linalg.norm(T.T @ g0))
    print("   NEWTON METRIC at the start: asymmetry %.2e -> floor %.2e; eigenvalues of -H/J %s (%d floored); a unit z-step "
          "along the Newton direction moves the wall %.3e" % (asym, TW.K_RICH * asym, np.array2string(lam / J_geno,
                                                                                                    precision=2),
                                                         int(np.sum(lam < TW.K_RICH * asym)), zlen), flush=True)
    pre = TW.Metric(rp, np.asarray(W0, float), T)
    Zf, hist, n_rec = P.run_trsqp(np.zeros(len(W0)), {}, dict(throat=pre), rp.ta, sign=+1.0, max_segments=SEGS,
                                  maxiter_per_seg=MAXIT, margin=None, tr0=TR0 / zlen, tr_floor=FLOOR / zlen, bounds=None,
                                  backtrack=4)
    Wf = np.asarray(W0, float) + T @ np.asarray(Zf, float)
else:
    Wf, hist, n_rec = P.run_trsqp(np.asarray(W0, float), {}, dict(throat=rp), rp.ta, sign=+1.0, max_segments=SEGS,
                                  maxiter_per_seg=MAXIT, margin=None, tr0=TR0, tr_floor=FLOOR, bounds=None, backtrack=4)
r_f = reading(np.asarray(Wf, float), "landing")
json.dump(dict(tag=tag, case=case, start=start, J_geno=J_geno, bound=bound, fit=r_fit, start_r=r_0, landing=r_f,
               segments=len(hist), records=n_rec, hist=[list(map(float, h)) for h in hist], seconds=time.time() - t00,
               sx=np.asarray(rp.sx).tolist(), sy_geno=np.asarray(rp.sy_g).tolist(), free=np.asarray(rp.free).tolist(),
               switches=dict(PSPL_JSCALE=os.environ.get("PSPL_JSCALE"), PSPL_TRFOLLOW=os.environ.get("PSPL_TRFOLLOW"),
                             A1_NEWTON_RESCUE=os.environ.get("A1_NEWTON_RESCUE"), metric=os.environ.get("T10_METRIC", ""),
                             backtrack=4, tr0=TR0,
                             tr_floor=FLOOR, max_segments=SEGS, maxiter=MAXIT, driver=P.DRIVER),
               qntr=(__import__("a1_qntr").LAST if P.DRIVER == "qntr" else None)),
          open(os.path.join(rv.OUT, tag + ".json"), "w"), indent=1, default=float)
print("== %s done: %d accepted bases, %d records, %.0f s" % (tag, len(hist), n_rec, time.time() - t00), flush=True)
