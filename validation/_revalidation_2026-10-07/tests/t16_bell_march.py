#!/usr/bin/env python3
"""T16 -- the model's bell march (a1_toc_variational_jax record, the engine the bell walks use) on GENO's two bells,
before any optimiser result is read:
  B1 convergence: J (the wall thrust 2 pi int p y dy) on the 8-knot least-squares fit of GENO's TOC and of GENO's ideal bell along
     the grid ladder (NI, Nw) = (21,60) (41,120) (81,240) (161,480): observed order and Richardson limit; every march
     certified.
  B2 the thrust DIFFERENCE between the two bells against GENO's. Both start from the same throat (same IVL, same arc), so
     their vacuum thrusts differ only by the wall integrals: C_F(TOC) - C_F(ideal) = (J_TOC - J_ideal) / (p_s A_t), p_s =
     the stagnation pressure of raptor.plt, A_t = pi. GENO prints C_F to 4 decimals: tolerance 1e-4 (its rounding,
     both numbers) + the model's Richardson error + the fits' representation error (|J(fit) - J(GENO wall)| is not
     measurable here; it is bounded by the fit's wall-angle error squared, below 1e-5 for both, see the printed max
     |y - y_GENO|).
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import bell_posing as BP                           # noqa: E402

R = rv.Report("t16_bell_march")
G = os.path.join(rv.RV, "geno")
LAD = [(21, 60), (41, 120), (81, 240), (161, 480)]
res = {}
for case, d in (("toc", "bell_toc_e4_L4"), ("ideal", "bell_ideal_e4")):
    gx, gy = BP.geno_wall(os.path.join(G, d))
    L, yL = float(gx[-1]), float(gy[-1])
    Js, certs = [], []
    for (ni, nw) in LAD:
        bp = BP.BellPosing(L, yL, NI=ni, Nw=nw)
        V = bp.fit_lsq(gx, gy)
        t0 = time.time()
        out, _ = bp.record(V)
        Js.append(bp.J_of(out))
        certs.append(float(out["cert_worst"]))
        x, y = bp.wall_xy(V)
        gap = float(np.max(np.abs(y[x >= 0] - np.interp(x[x >= 0], gx, gy))))
        print("  %-5s NI %3d Nw %3d: J %.10e cert %.3f (%.0f s); fit max |y - y_GENO| %.2e" % (
            case, ni, nw, Js[-1], certs[-1], time.time() - t0, gap), flush=True)
    d1, d2, d3 = Js[1] - Js[0], Js[2] - Js[1], Js[3] - Js[2]
    p = float(np.log2(abs(d2 / d3)))
    J_inf = Js[-1] + d3 / (2.0 ** p - 1.0)
    res[case] = dict(J=Js, cert=certs, order=p, J_inf=J_inf, e_fine=abs(Js[-1] - J_inf), cf_geno=BP.geno_cf(os.path.join(G, d)),
                     gap_fit=gap, L=L, yL=yL)
    R.check("%s: every march certified" % case, max(certs), 1.0)
    R.check("%s: observed order between the two finest pairs >= 1.5" % case, p, None, ok=p >= 1.5)
tab, _, _ = BP.tables()
ps = float(tab["ps"])
if ps < 1e4:                       # raptor.plt carries bar
    ps *= 1e5
print("  GENO's C_F reference pressure td%%ps = %.6e Pa" % ps, flush=True)
dJ = (res["toc"]["J_inf"] - res["ideal"]["J_inf"]) / (ps * np.pi)
dG = res["toc"]["cf_geno"][0] - res["ideal"]["cf_geno"][0]
tol = 1e-4 + (res["toc"]["e_fine"] + res["ideal"]["e_fine"]) / (ps * np.pi)
R.check("C_F(TOC) - C_F(ideal): model %.6f vs GENO %.4f" % (dJ, dG), dJ - dG, tol)
# REJECTOR (R5): the same check with the TOC's wall stretched to an exit radius 1 % too large (a wrong wall), marched on
# the two finest grids and extrapolated with the TOC's own observed order
gx, gy = BP.geno_wall(os.path.join(G, "bell_toc_e4_L4"))
L, yL = float(gx[-1]), float(gy[-1])
Jx = []
for (ni, nw) in LAD[-2:]:
    bp = BP.BellPosing(L, 1.01 * yL, NI=ni, Nw=nw)
    V = bp.fit_lsq(gx, 1.0 + (gy - 1.0) * (1.01 * yL - 1.0) / (yL - 1.0))
    Jx.append(bp.J_of(bp.record(V)[0]))
Jx_inf = Jx[-1] + (Jx[-1] - Jx[-2]) / (2.0 ** res["toc"]["order"] - 1.0)
dJx = (Jx_inf - res["ideal"]["J_inf"]) / (ps * np.pi)
R.note("rejector: TOC exit radius x1.01 -> C_F(TOC) - C_F(ideal) = %.6f" % dJx)
R.reject("C_F(TOC) - C_F(ideal) vs GENO, TOC exit radius x1.01", dJx - dG, tol)
res.update(dCF_model=dJ, dCF_geno=dG, ps=ps)
json.dump(res, open(os.path.join(rv.OUT, "t16_bell_march_detail.json"), "w"), indent=1, default=float)
sys.exit(R.save(extra=dict(dCF_model=dJ, dCF_geno=dG)))
