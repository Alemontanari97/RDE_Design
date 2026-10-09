#!/usr/bin/env python3
"""T08b -- does the SQP re-obtain GENO's Rao plug on the SAME problem (ref/rao_posing.py, tests/t08b_rao_walk.py)?

Rao is the optimum of this problem (the owner's rule, and the argument in t08b_rao_walk.py's docstring), so the walk
must land on GENO's contour; a landing ABOVE it is a symptom to be explained, never a result. The band for "above":
the march's own error, measured as the change of J on GENO's contour between the two finest re-march levels.
Re-march levels (rao_posing.posing_level): 1, 2, 3 (start rows 132 / 262 / 522, stations 120 / 240 / 480).
Checks:
  Q1 each landing is not above GENO's contour at the finest level beyond the march's error there (one-sided);
  Q2 each landing is within the march's error of GENO's contour in value at the finest level (two-sided: re-obtained);
  Q3 the landing's contour: max |y - y_GENO| on the designed part, reported with the curvature that links it to Q2.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import rao_posing as RP                            # noqa: E402

R = rv.Report("t08b_summary")
D = os.path.join(rv.RV, "geno", "rao_sdt_L0448")
walks = {}
for tag in ("A0", "C0", "A1", "C1"):
    fn = os.path.join(rv.OUT, "t08b_walk_%s.json" % tag)
    if os.path.exists(fn):
        walks[tag] = json.load(open(fn))
for tag, r in walks.items():
    R.note("walk %s: start %+.3e -> landing %+.4e (J/J(GENO contour) - 1 at the walk's grid), max |y - y_GENO| %.2e, "
           "|grad|/J %.1e, KS - mu0 %+.3f, %d bases, %d records, %.0f s" % (
               tag, r["start_r"]["gap"], r["landing"]["gap"], r["landing"]["dy_max"], r["landing"]["grad_inf"],
               r["landing"]["ks"], r["segments"], r["records"], r["seconds"]))
fit_W = next(iter(walks.values()))["fit"]["W"]
rows = []
for L in (1, 2, 3):
    rp = RP.posing_level(D, L, design=True)
    out, _ = rp.march_record(None)
    Jg = float(rp.J_of(out))
    row = dict(level=L, K=rp.K, N=rp.N, J_geno=Jg, cert_geno=float(out["cert_worst"]))
    for name, W in [("fit", fit_W)] + [(t, r["landing"]["W"]) for t, r in walks.items()]:
        o, _ = rp.march_record(np.asarray(W, float))
        row[name] = float(rp.J_of(o)) / Jg - 1.0
        row[name + "_cert"] = float(o["cert_worst"])
    rows.append(row)
    R.note("level %d (rows %d, stations %d): J(GENO contour) %.10e (cert %.2f) | relative to it: fit %+.2e%s" % (
        L, rp.N, rp.K, Jg, row["cert_geno"], row["fit"],
        "".join(" | %s %+.2e (cert %.2f)" % (t, row[t], row[t + "_cert"]) for t in walks)))
f, c = rows[-1], rows[-2]
err = abs(f["J_geno"] / c["J_geno"] - 1.0)
R.note("the march's error at the finest level (change of J on GENO's contour, levels 2 -> 3): %.2e" % err)
for t in walks:
    R.check("Q1 landing %s not above GENO's Rao contour at the finest level beyond the march's error (one-sided)" % t,
            f[t], err, ok=f[t] <= err)
    R.check("Q2 landing %s re-obtains GENO's value at the finest level (|dJ| <= march's error)" % t, f[t], err)
    R.note("Q3 landing %s: max |y - y_GENO| %.2e on the designed part; at the finest level dJ/J %+.2e" % (
        t, walks[t]["landing"]["dy_max"], f[t]))

import matplotlib                                   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                     # noqa: E402
rp = RP.RaoPosing(D, K=120, n_fan=20, m=10, design=True)
fig, ax = plt.subplots(1, 3, figsize=(17, 4.6))
a = ax[0]
fr = rp.free
B, c0 = rp.basis()
a.axhline(0.0, color="k", lw=2, label="GENO Rao contour")
for t, r in walks.items():
    y = B @ np.asarray(r["landing"]["W"]) + c0
    a.plot(rp.sx[fr], (y - rp.sy_g)[fr], "-", lw=1.2, label="landing %s" % t)
    y0 = B @ np.asarray(r["start_r"]["W"]) + c0
    a.plot(rp.sx[fr], (y0 - rp.sy_g)[fr], ":", lw=1, label="start %s" % t)
a.set_xlabel("x"); a.set_ylabel("y - y_GENO"); a.legend(fontsize=7); a.grid(alpha=0.3)
a.set_title("Designed part of the plug, relative to GENO's Rao contour")
a = ax[1]
for t, r in walks.items():
    h = np.asarray(r["hist"])
    a.semilogy(np.arange(len(h)), np.maximum(np.abs(h[:, 1] / r["J_geno"] - 1.0), 1e-9), "-", lw=1.2, label=t)
a.set_xlabel("accepted base"); a.set_ylabel("|J / J(GENO contour) - 1|"); a.legend(fontsize=7); a.grid(alpha=0.3, which="both")
a.set_title("walks")
a = ax[2]
hh = np.array([1.0 / r["K"] for r in rows])
a.semilogx(hh, [r["fit"] for r in rows], "o-", label="best spline of GENO's contour")
for t in walks:
    a.semilogx(hh, [r[t] for r in rows], "o-", label="landing %s" % t)
a.axhline(0.0, color="k", lw=1)
a.set_xlabel("1/K"); a.set_ylabel("J / J(GENO contour) - 1"); a.legend(fontsize=7); a.grid(alpha=0.3, which="both")
a.set_title("re-marched at finer levels")
rv.savefig(fig, "08b_sqp_vs_geno_rao.png")
sys.exit(R.save(dict(rows=rows, err=err)))
