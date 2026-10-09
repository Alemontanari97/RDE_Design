#!/usr/bin/env python3
"""T21 -- where does the bell engine's thrust jump? The ideal-bell walk from the stretched start (8 points, grid
41 x 120) stops with "RESOLUTION": short steps miss their predicted gain by more than half, five in a row. Here the walk
is repeated (the driver is deterministic) keeping the last rejected trial; the thrust is then marched along the segment
from the accepted point to that trial, the jump is bracketed by bisection, and the two sides are compared: thrust, wall
pressure along x, and the march's structure (cells, columns, certificate), to say WHICH discrete decision of the march
moves the thrust.  -> out/t21_bell_jump.json
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import bell_posing as BP                           # noqa: E402
import a1_qntr as QN                               # noqa: E402
import a1_ideal_march_jax as A1                    # noqa: E402

t00 = time.time()
G = os.path.join(rv.RV, "geno")
gx, gy = BP.geno_wall(os.path.join(G, "bell_ideal_e4"))
L, yL = float(gx[-1]), float(gy[-1])
bp = BP.BellPosing(L, yL, NI=41, Nw=120, M=8)
ox, oy = BP.geno_wall(os.path.join(G, "bell_toc_e4_L6"))
oy = 1.0 + (oy - 1.0) * (yL - 1.0) / (oy[-1] - 1.0)
V0 = bp.fit_lsq(ox * L / ox[-1], oy)                 # the stretched start of t15
walk = QN.Walk(bp.record, bp.jg, sign=1.0, verbose=1)
Vf, hist, n_rec = walk.run(V0, max_segments=100, tr0=0.01)
rep = dict(QN.LAST)
print("== walk: stop %s, J %.10e, %d trials" % (rep["stop"], rep["J"], rep["segments"]), flush=True)
lr = rep.get("last_reject")
if lr is None:
    raise SystemExit("no rejected trial to examine")
Va, Vb = np.asarray(lr["base_W"]), np.asarray(lr["W"])
print("   last rejected trial: step %.3e, J %.10e -> %.10e (predicted %+.3e)" % (
    np.linalg.norm(Vb - Va), lr["base_J"], lr["J"], lr["pred"]), flush=True)


def probe(t):
    V = Va + t * (Vb - Va)
    out, plan = bp.record(V)
    return out, bp.J_of(out)


# the thrust along the segment
ts = np.linspace(0.0, 1.0, 9)
prof = []
for t in ts:
    o, J = probe(t)
    prof.append(J)
    print("   t %.4f  J %.10e  cert %.3f  wall points %d" % (t, J, float(o["cert_worst"]), o["wall"].shape[0]), flush=True)
prof = np.asarray(prof)
dJ = np.diff(prof)
k = int(np.argmin(dJ))                               # the largest drop between neighbours
lo, hi = ts[k], ts[k + 1]
o_lo, J_lo = probe(lo)
o_hi, J_hi = probe(hi)
for _ in range(14):                                  # bisection on the drop
    mid = 0.5 * (lo + hi)
    o_m, J_m = probe(mid)
    if abs(J_m - J_lo) < abs(J_m - J_hi):
        lo, o_lo, J_lo = mid, o_m, J_m
    else:
        hi, o_hi, J_hi = mid, o_m, J_m
print("   jump bracketed in t [%.6f, %.6f] (|dV| %.2e): J %.10e -> %.10e (%+.2f ppm)" % (
    lo, hi, (hi - lo) * np.linalg.norm(Vb - Va), J_lo, J_hi, 1e6 * (J_hi - J_lo) / J_lo), flush=True)
# the two sides: wall pressure along x, and the march's structure
ta = A1.tab_arrays(bp.tab)


def wall_p(o):
    w = np.asarray(o["wall"])
    q = np.sqrt(w[:, 2] ** 2 + w[:, 3] ** 2)
    p = np.asarray(bp.state(jnp.asarray(q), ta)[1])
    return w[:, 0], w[:, 1], p


xa, ya, pa = wall_p(o_lo)
xb, yb, pb = wall_p(o_hi)
n = min(len(xa), len(xb))
dp = np.abs(pb[:n] - pa[:n]) / np.maximum(np.abs(pa[:n]), 1e-300)
i_first = int(np.argmax(dp > 1e3 * max(1e-12, float(np.median(dp))))) if np.any(dp > 0) else -1
struct = {}
for side, o in (("before", o_lo), ("after", o_hi)):
    struct[side] = {k_: (int(v) if np.isscalar(v) and float(v).is_integer() else (float(v) if np.isscalar(v) else None))
                    for k_, v in o.items() if np.isscalar(v)}
    struct[side]["wall_points"] = int(np.asarray(o["wall"]).shape[0])
print("   wall points before/after: %d / %d" % (len(xa), len(xb)), flush=True)
print("   largest relative wall-pressure change %.3e at x %.4f (wall point %d of %d); first point above 1000 x median:"
      " x %.4f" % (float(dp.max()), float(xa[int(np.argmax(dp))]), int(np.argmax(dp)), n,
                   float(xa[i_first]) if i_first >= 0 else float("nan")), flush=True)
print("   scalar fields that differ: %s" % {k_: (struct["before"].get(k_), struct["after"].get(k_))
                                         for k_ in struct["before"] if struct["before"].get(k_) != struct["after"].get(k_)},
      flush=True)
json.dump(dict(walk=dict(stop=rep["stop"], J=rep["J"], segments=rep["segments"]), last_reject=lr,
               segment_profile=dict(t=ts.tolist(), J=prof.tolist()),
               bracket=dict(t=[lo, hi], J=[J_lo, J_hi], dV=float((hi - lo) * np.linalg.norm(Vb - Va))),
               wall_before=dict(x=xa.tolist(), y=ya.tolist(), p=pa.tolist()),
               wall_after=dict(x=xb.tolist(), y=yb.tolist(), p=pb.tolist()), structure=struct,
               seconds=time.time() - t00),
          open(os.path.join(rv.OUT, "t21_bell_jump.json"), "w"), indent=1, default=float)
print("== t21 done: %.0f s" % (time.time() - t00), flush=True)
