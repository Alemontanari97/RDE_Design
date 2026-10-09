#!/usr/bin/env python3
"""T24 -- is the ideal bell's 'second top' a local MAXIMUM, or a saddle? (The driver's stop uses |eigenvalues| of the
curvature, so a stop alone does not tell.) At each of the two results of the 8-point walks on grid 81 x 240:
  1. the gradient (reverse AD on the frozen plan) and the secant Hessian H (central differences of that gradient,
     h = 1e-4), symmetrised; the eigenvalues of H: a local maximum needs all of them negative;
  2. the TRUE march (re-recorded, certified) at V + s v_k along every eigenvector v_k, s = +-2e-3, +-1e-2 (the scale of
     the walk's last steps and 5 x more): a local maximum needs J to fall in every direction, both ways, at the finite
     scale (not only in the frozen model).
-> out/t24_bell_top_check.json
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import bell_posing as BP                           # noqa: E402

t00 = time.time()
res = {}
for tag, lab in (("t15_bell_ideal_stretched_NI81", "second top (stretched start)"),
                 ("t15_bell_ideal_extended_NI81", "ideal bell (cylinder start)")):
    d = json.load(open(os.path.join(rv.OUT, tag + ".json")))
    bp = BP.BellPosing(d["L"], d["yL"], NI=81, Nw=240, M=8)
    V = np.asarray(d["landing"]["V"], float)
    out, plan = bp.record(V)
    J0 = bp.J_of(out)
    J, g = bp.jg(V, plan)
    n, h = len(V), 1e-4
    H = np.zeros((n, n))
    for j in range(n):
        e = np.zeros(n)
        e[j] = h
        H[:, j] = (bp.jg(V + e, plan)[1] - bp.jg(V - e, plan)[1]) / (2 * h)
    asym = float(np.max(np.abs(H - H.T)) / np.max(np.abs(H)))
    Hs = 0.5 * (H + H.T)
    lam, Q = np.linalg.eigh(Hs)
    print("== %s: J %.10e, |grad| %.3e (relative to J: %.2e), Hessian asymmetry %.1e" % (
        lab, J0, np.linalg.norm(g), np.linalg.norm(g) / J0, asym), flush=True)
    print("   eigenvalues of H / J: %s" % np.array2string(lam / J0, precision=3), flush=True)
    probes = []
    for k in range(n):
        v = Q[:, k]
        row = dict(k=k, lam=float(lam[k]), dJ={})
        for s in (-1e-2, -2e-3, 2e-3, 1e-2):
            o, _ = bp.record(V + s * v)
            Js = bp.J_of(o)
            row["dJ"]["%+.0e" % s] = (Js - J0) / J0
            row.setdefault("pred", {})["%+.0e" % s] = float(s * (g @ v) + 0.5 * s * s * lam[k]) / J0
        probes.append(row)
        print("   direction %d (eigenvalue %+.2e): true dJ/J at s -1e-2 -2e-3 +2e-3 +1e-2: %s | model %s" % (
            k, lam[k] / J0, " ".join("%+.2e" % v_ for v_ in row["dJ"].values()),
            " ".join("%+.2e" % v_ for v_ in row["pred"].values())), flush=True)
    worst = max(max(r["dJ"].values()) for r in probes)
    print("   largest change of J over all probes: %+.3e (a local maximum needs it <= 0)" % worst, flush=True)
    res[lab] = dict(J=J0, grad=g.tolist(), grad_rel=float(np.linalg.norm(g) / J0), eig=(lam / J0).tolist(),
                    asym=asym, probes=probes, worst=worst, theta_B=float(np.degrees(V[0])))
json.dump(res, open(os.path.join(rv.OUT, "t24_bell_top_check.json"), "w"), indent=1, default=float)
print("== t24 done: %.0f s" % (time.time() - t00), flush=True)
