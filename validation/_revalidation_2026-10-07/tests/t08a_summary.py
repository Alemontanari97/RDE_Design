#!/usr/bin/env python3
"""T08a -- the optimiser on an EXACT optimum (planar plug, ref/planar_posing.py): the walks' verdict.

The exact optimum: for every shock-free plug with the free edge at p_a and the base at p_a, the thrust is the axial
momentum flux through the exit plane x = L in the p_a gauge, T = int (rho u^2 + p - p_a) dy, and per unit mass
  u + (p - p_a)/(rho u) <= V(p) + (p - p_a)/(rho V) <= V_a          (supersonic: d(rho V)/dp > 0, maximum at p = p_a)
so T <= mdot V_a, with equality iff the exit is uniform, axial, at p_a: the ideal plug (T03's exact streamline).
Checks on the walks (logs/t08a_walk_*.log, out/t08a_walk_*.json):
  O1 every unconstrained walk reaches the class optimum IN VALUE: J(landing) >= J(fit) - 1e-7 T (the fit = the spline
     closest to the ideal plug, a member of the class; the walk maximises the same discrete J);
  O2 two walks from distant starts (B, C; floor tr0/256) land on the same value (|dJ| <= 1e-8 T) and contour (<= 2e-3);
  O3 the landing's advantage over the fit is a discretisation artefact: re-marched at (160,41) and (320,81), the
     landing's J is not above the fit's beyond the march's own error at that level (|J_disc - T_ideal|);
  O4 the class-constrained walk from an in-class start (B1) reaches the unconstrained value within 1e-6 T --
     EXPECTED TO FAIL (stall measured, see the diagnostics in the log).
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import planar_posing as PP                         # noqa: E402

R = rv.Report("t08a_summary")
W_ = {}
for tag in ("A0_K80", "B0_K80", "B0_K80_f256", "C0_K80_f256", "B1_K80", "B1_K80_f256", "A1_K80"):
    fn = os.path.join(rv.OUT, "t08a_walk_%s.json" % tag)
    if os.path.exists(fn):
        W_[tag] = json.load(open(fn))
for tag, r in W_.items():
    R.note("walk %-12s start %+.3e -> landing %+.4e (J/T_ideal - 1), max |y - y_ideal| %.2e, |grad|/T %.1e, %d bases, "
           "%d records, %.0f s" % (tag, r["start_r"]["gap"], r["landing"]["gap"], r["landing"]["dy_max"],
                                   r["landing"]["grad_inf"], r["segments"], r["records"], r["seconds"]))
fit = W_["B0_K80"]["fit"]
for tag in ("A0_K80", "B0_K80", "B0_K80_f256", "C0_K80_f256"):
    if tag in W_:
        R.check("O1 %s reaches the class optimum in value: J(landing) - J(fit) >= -1e-7 T" % tag,
                W_[tag]["landing"]["gap"] - fit["gap"], None, ok=W_[tag]["landing"]["gap"] - fit["gap"] >= -1e-7)
b, c = W_["B0_K80_f256"]["landing"], W_["C0_K80_f256"]["landing"]
R.check("O2 B and C (distant starts) land on the same value", b["gap"] - c["gap"], 1e-8)
dyBC = float(np.max(np.abs(np.asarray(b["y"]) - np.asarray(c["y"]))))
R.check("O2 B and C land on the same contour (max |dy|)", dyBC, 2e-3)
# O3: re-march fit, ideal (exact streamline at the stations), landings at three resolutions
levels = [(80, 21), (160, 41), (320, 81)]
rows = []
for K, N in levels:
    pp = PP.PlanarPlug(K=K, N=N, m=12, L=2.0)
    row = dict(K=K, N=N)
    for name, W in (("fit", fit["W"]), ("B", b["W"]), ("C", c["W"]), ("A", W_["A0_K80"]["landing"]["W"])):
        out, _ = pp.march_record(np.asarray(W, float))
        row[name] = float(pp.J_of(out)) / pp.T_ideal - 1.0
    # the exact ideal contour itself (not a spline) at this resolution
    import a1_plug_march as PM                     # noqa: E402
    sx = pp.sx
    out, _ = PM.plug_march((sx, np.asarray(pp.y_ideal(sx)), np.asarray(pp.s_ideal(sx))), pp.start, pp.q1, pp.tab, 0.0,
                           shroud=(pp.xs, pp.ys, pp.ss), wedge_every=pp.m_w, fast=True, lip_jet=pp.lip_jet)
    row["ideal"] = float(pp.J_of(out)) / pp.T_ideal - 1.0
    rows.append(row)
    R.note("(K %3d, N %2d): J/T_ideal - 1: exact ideal contour %+.3e | fit %+.3e | landing B %+.3e | C %+.3e | A %+.3e"
           % (K, N, row["ideal"], row["fit"], row["B"], row["C"], row["A"]))
f = rows[-1]
err = abs(f["ideal"])                 # the march's own error at the finest level (exact contour, exact answer 0)
R.check("O3 at (320,81) the landing B is not above the fit beyond the march's own error (one-sided)",
        f["B"] - f["fit"], err, ok=f["B"] - f["fit"] <= err)
R.check("O3 at (320,81) the landing C is not above the fit beyond the march's own error (one-sided)",
        f["C"] - f["fit"], err, ok=f["C"] - f["fit"] <= err)
p_id = np.log(abs(rows[0]["ideal"]) / abs(rows[1]["ideal"])) / np.log(2.0)
R.note("the march on the EXACT ideal contour: J/T_ideal - 1 = %s (order %.2f then %.2f)" % (
    " ".join("%+.2e" % r["ideal"] for r in rows), p_id,
    np.log(abs(rows[1]["ideal"]) / abs(rows[2]["ideal"])) / np.log(2.0)))
R.check("O5 the exact optimum mdot V_a is the march's limit on the ideal contour (finest |J/T - 1| <= 2|change|)",
        f["ideal"], 2.0 * abs(rows[-1]["ideal"] - rows[-2]["ideal"]))
# the representation's cost: the best 12-knot spline against the ideal (slope error where the ideal's curvature jumps)
ppf = PP.PlanarPlug(K=320, N=81, m=12, L=2.0)
yf, sf = (np.asarray(v) for v in ppf.walls(np.asarray(fit["W"], float))[1:])
si = np.asarray(ppf.s_ideal(ppf.sx))
ds = np.arctan(sf) - np.arctan(si)
i_ = int(np.argmax(np.abs(ds)))
R.note("the fit's wall-angle error: max %.2e rad at x %.3f (the ideal's curvature jumps at the fan's first / last wave,"
       " x %.4f / %.4f), rms %.2e rad; its thrust deficit at (320,81): %.2e" % (
           abs(ds[i_]), ppf.sx[i_], ppf.P_in[0], ppf.P_out[0], float(np.sqrt(np.mean(ds ** 2))), f["fit"] - f["ideal"]))
R.check("O6 the representation's cost: the class optimum (the fit) is below the exact optimum by more than the march's"
        " error [expected: the 12-knot spline cannot follow the ideal's curvature jumps]", f["fit"] - f["ideal"], err + 1e-7)
if "B1_K80" in W_:
    g1 = W_["B1_K80"]["landing"]["gap"]
    R.check("O4 the class-constrained walk B1 reaches the unconstrained value (within 1e-6 T) [stall expected]",
            g1 - b["gap"], 1e-6)

import matplotlib                                   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                     # noqa: E402
pp = PP.PlanarPlug(K=80, N=21, m=12, L=2.0)
fig, ax = plt.subplots(1, 3, figsize=(17, 4.6))
a = ax[0]
xs = pp.sx
a.plot(xs, np.zeros_like(xs), "k-", lw=2, label="ideal plug (exact)")
for tag, lab in (("fit", "spline closest to the ideal"), ("A0_K80", "landing A (perturbed optimum)"),
                 ("B0_K80_f256", "landing B (15-deg plug start)"), ("C0_K80_f256", "landing C (straight start)"),
                 ("B1_K80", "landing B with the class (stalled)")):
    yy = np.asarray((fit if tag == "fit" else W_[tag]["landing"])["y"])
    a.plot(xs, yy - np.asarray(pp.y_ideal(xs)), "-", lw=1.2, label=lab)
a.set_xlabel("x"); a.set_ylabel("y - y_ideal"); a.legend(fontsize=7); a.grid(alpha=0.3)
a.set_title("Planar plug: contours relative to the exact optimum")
a = ax[1]
for tag in ("A0_K80", "B0_K80_f256", "C0_K80_f256", "B1_K80", "B1_K80_f256"):
    if tag in W_:
        h = np.asarray(W_[tag]["hist"])
        a.semilogy(np.arange(len(h)), np.maximum(-(h[:, 1] / W_[tag]["T_ideal"] - 1.0), 1e-9), "-", lw=1.2, label=tag)
a.axhline(-fit["gap"], color="k", ls=":", lw=1, label="the fit (discrete J)")
a.set_xlabel("accepted base"); a.set_ylabel("1 - J / (mdot V_a)"); a.legend(fontsize=7); a.grid(alpha=0.3, which="both")
a.set_title("walks: distance to the exact optimum")
a = ax[2]
h = np.array([1.0 / r["K"] for r in rows])
for key, lab in (("ideal", "exact ideal contour"), ("fit", "fit"), ("B", "landing B"), ("C", "landing C")):
    a.semilogx(h, [r[key] for r in rows], "o-", label=lab)
a.set_xlabel("1/K"); a.set_ylabel("J/T_ideal - 1"); a.legend(fontsize=7); a.grid(alpha=0.3, which="both")
a.set_title("re-marched at finer grids")
rv.savefig(fig, "08a_planar_ideal_plug.png")
sys.exit(R.save(dict(rows=rows, walks={k: dict(gap=v["landing"]["gap"], dy=v["landing"]["dy_max"]) for k, v in W_.items()})))
