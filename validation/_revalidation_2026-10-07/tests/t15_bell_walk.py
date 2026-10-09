#!/usr/bin/env python3
"""T15 (one walk) -- the optimiser on BELL nozzles: the model's bell engine (ref/bell_posing.py) walked by the
agnostic driver (validation/a1_qntr.py, the same defaults as every plug walk), against two known optima of GENO
(exp/ws-c-prod-nozzles, CH4/O2 frozen gas of raptor.plt, throat radius 1, arcs 1.5 / 0.45):
  toc    Rao's thrust-optimised contour (GENO nozzle_type 2), eps 4, length 4 (54 % of the ideal bell's): the maximum
         thrust at fixed length and exit radius (Rao 1958). The lip is pinned at GENO's exit point.
  ideal  the ideal bell (GENO nozzle_type 0), eps 4, length 7.341 = its own length: at that length and exit radius the
         uniform parallel exit is the optimum (in vacuum T <= F_1D(eps), equality only for the uniform exit).
Starts (distant, shock-free):
  cone   a straight wall from the throat arc to the lip, tangent to the arc (the conical nozzle of that length):
         NOT a usable start -- the march is not certified (a cell crosses the axis: the arc-to-cone junction sends
         compressions that coalesce near the axis, the conical nozzle's internal shock);
  steep  (toc case) GENO's TOC of length 6 compressed in x to length 4 (attachment 28.7 deg);
  tic    (toc case) the ideal contour of eps 6 truncated at the length and scaled to the exit radius;
  stretched / extended  (ideal case) GENO's TOC of length 6 stretched to the ideal length / continued by a cylinder.
usage: t15_bell_walk.py <toc|ideal> <tic|steep|stretched|extended> [NI Nw]   -> out/t15_bell_<case>_<start>.json
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import bell_posing as BP                           # noqa: E402
import a1_qntr as QN                               # noqa: E402

case, start = sys.argv[1], sys.argv[2]
NI = int(sys.argv[3]) if len(sys.argv) > 3 else 41
NW = int(sys.argv[4]) if len(sys.argv) > 4 else 120
LEVELS = [(NI, NW), (2 * NI - 1, 2 * NW)]          # walk grid, then the reading grid
MW = int(os.environ.get("T15_M", "8"))               # wall points of the bell engine's curve (its default: 8)
tag = "t15_bell_%s_%s" % (case, start) + ("" if (NI, NW) == (41, 120) else "_NI%d" % NI) + ("" if MW == 8 else "_M%d" % MW)
G = os.path.join(rv.RV, "geno")
ref_dir = os.path.join(G, dict(toc="bell_toc_e4_L4", ideal="bell_ideal_e4")[case])
gx, gy = BP.geno_wall(ref_dir)
L, yL = float(gx[-1]), float(gy[-1])
t00 = time.time()
bp = BP.BellPosing(L, yL, NI=NI, Nw=NW, M=MW)
V_fit = bp.fit(gx, gy)
if start == "cone":
    th = 0.25
    for _ in range(60):
        xB = bp.cfg["rtd"] * np.sin(th)
        yB = 1.0 + bp.cfg["rtd"] * (1.0 - np.cos(th))
        th = float(np.arctan((yL - yB) / (L - xB)))
    V0 = np.concatenate([[th], np.zeros(bp.m - 1)])
    V0[1:] = yB + np.tan(th) * (bp.knots(V0)[:-1] - xB)
elif start == "tic" and case == "toc":
    x6, y6 = BP.geno_wall(os.path.join(G, "bell_ideal_e6"))
    sx = x6[x6 <= L]
    sy = 1.0 + (y6[x6 <= L] - 1.0) * (yL - 1.0) / (np.interp(L, x6, y6) - 1.0)
    V0 = bp.fit_lsq(sx, sy)
elif start == "steep" and case == "toc":
    # GENO's TOC of length 6 compressed in x to length 4: attachment 28.7 deg against the optimum's 16.9
    ox, oy = BP.geno_wall(os.path.join(G, "bell_toc_e4_L6"))
    V0 = bp.fit_lsq(ox * L / ox[-1], 1.0 + (oy - 1.0) * (yL - 1.0) / (oy[-1] - 1.0))
elif start in ("stretched", "extended") and case == "ideal":
    # GENO's TOC of length 6 (eps 4), stretched in x to the ideal length, or continued by a cylinder to it (the
    # cone and the TOC of length 4 stretched are refused by the engine: axial Mach below 1 in a cell near the throat)
    ox, oy = BP.geno_wall(os.path.join(G, "bell_toc_e4_L6"))
    oy = 1.0 + (oy - 1.0) * (yL - 1.0) / (oy[-1] - 1.0)
    if start == "stretched":
        V0 = bp.fit_lsq(ox * L / ox[-1], oy)
    else:
        V0 = bp.fit_lsq(np.r_[ox, np.linspace(ox[-1] + 1e-3, L, 50)], np.r_[oy, np.full(50, yL)])
else:
    raise SystemExit("unknown start %s" % start)


def wall_gap(V):
    x, y = bp.wall_xy(V)
    m = x >= 0.0
    return float(np.max(np.abs(y[m] - np.interp(x[m], gx, gy))))


def reading(V, label, levels=LEVELS):
    r = dict(V=np.asarray(V).tolist(), gap_wall=wall_gap(V), J={}, cert={})
    for (ni, nw) in levels:
        b = bp if (ni, nw) == (NI, NW) else BP.BellPosing(L, yL, NI=ni, Nw=nw, M=MW)
        try:
            out, _ = b.record(V)
            r["J"]["%d_%d" % (ni, nw)] = b.J_of(out)
            r["cert"]["%d_%d" % (ni, nw)] = float(out["cert_worst"])
        except Exception as err:                    # noqa: BLE001
            r["J"]["%d_%d" % (ni, nw)] = None
            r["cert"]["%d_%d" % (ni, nw)] = str(err)[:100]
    x, y = bp.wall_xy(V)
    r.update(x=x.tolist(), y=y.tolist())
    print("  %-8s theta_B %.4f deg | max |y - y_GENO| %.3e | J %s | cert %s" % (
        label, np.degrees(V[0]), r["gap_wall"], {k: ("%.10e" % v if v else v) for k, v in r["J"].items()},
        r["cert"]), flush=True)
    return r


print("== %s: L %.6f, exit radius %.6f (eps %.5f); walk grid NI %d Nw %d, reading grid %s" % (
    tag, L, yL, yL ** 2, NI, NW, LEVELS[1]), flush=True)
V_fit = bp.fit_lsq(gx, gy)                         # the best spline (least squares) of GENO's wall
r_fit = reading(V_fit, "GENO fit")
r_0 = reading(V0, "start")
walk = QN.Walk(bp.record, bp.jg, sign=1.0, verbose=1)
Vf, hist, n_rec = walk.run(V0, max_segments=int(os.environ.get("T15_SEGS", "100")), tr0=0.01)
r_f = reading(np.asarray(Vf, float), "landing")
json.dump(dict(tag=tag, case=case, start=start, L=L, yL=yL, levels=LEVELS, geno_x=gx.tolist(), geno_y=gy.tolist(),
               geno_cf=BP.geno_cf(ref_dir), fit=r_fit, start_r=r_0, landing=r_f, qntr=QN.LAST,
               hist=[list(map(float, h)) for h in hist], records=n_rec, seconds=time.time() - t00),
          open(os.path.join(rv.OUT, tag + ".json"), "w"), indent=1, default=float)
print("== %s done: %.0f s" % (tag, time.time() - t00), flush=True)
