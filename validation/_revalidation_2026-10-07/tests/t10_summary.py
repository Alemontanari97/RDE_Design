#!/usr/bin/env python3
"""T10 summary -- the SQP against Rao's method on two literature-anchored problems (walks: t10_rao_walk.py).
  Rao 1961 (eps 3.81, GENO = Rao's Table 1, T09): does the SQP re-obtain Rao's contour?
  axial exit (Rao's theta_E = 0 member, plug ended at R_D 0.4): the optimum is known exactly, T = mdot V_a.
Tests (no hand-set tolerance):
  reach   at the walk's grid the landing is not below the best spline of GENO's contour (a point of the same design
          space) by more than the gain still available at the walk's resolution, sqrt(m) |grad J|_inf x floor;
  limit   every contour (GENO's, its best spline, each landing) is re-marched at levels 1-3 (stations 120/240/480, GENO's
          C+ at 111/221/441 points, 20/40/80 fan rays); the DIFFERENCE landing - best spline (same grid: the march errors
          nearly cancel) is extrapolated (Richardson) and must lie within the walk grid's resolution of differences
          (its change from level 1 to level 3); (axial) GENO's contour reaches the bound mdot V_a in the limit;
  pair    two starts land on the same value within the sum of their remaining gains.
Run with A1_NEWTON_RESCUE=1 (as the walks): bash run.sh with the variable exported.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import numpy as np                                 # noqa: E402
import matplotlib                                  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                    # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import rv                                          # noqa: E402
import rao_posing as RP                            # noqa: E402
import rao1961 as R61                              # noqa: E402
from a1_toc_variational_jax import spline_coeffs, spline_eval     # noqa: E402

rep = rv.Report("t10_summary")
if os.environ.get("A1_NEWTON_RESCUE") != "1":
    rep.note("WARNING: A1_NEWTON_RESCUE is not 1; the Rao 1961 fine levels stall uncertified without it")
CASES = [("rao61_e381_pbR_mi15", "Rao 1961, eps 3.81 (Table 1)"), ("axial_e381_RD04_mi15", "axial exit (theta_E = 0), R_D 0.4")]
STARTS = [("bump", "start: Rao's contour + bump (1 % of lip radius)", "C0", "-"),
          ("half", "start: halfway between Rao's contour and a straight line", "C1", "-"),
          ("cont_bump_it2", "continued from the bump landing, one step <= 1e-3 per segment", "C2", "--"),
          ("cont_half_it2", "continued from the halfway landing, one step <= 1e-3 per segment", "C3", "--")]
LEVELS = (1, 2, 3)
extra = {}


def dense_wall(rp, W, xd):
    g = rp.g
    xk = np.r_[g.x_s, rp.xk]
    yk = np.r_[g.y_s, np.asarray(W), g.D[1]]
    Mc = spline_coeffs(jnp.asarray(xk), jnp.asarray(yk), rp.slope_s)
    return np.asarray(jax.vmap(lambda xx: spline_eval(xx, jnp.asarray(xk), jnp.asarray(yk), Mc)[0])(jnp.asarray(xd)))


def richardson(J):
    """J at levels 1, 2, 3 (h halving) -> (limit, |J_3 - limit|, order); order clipped to [0.5, 4]."""
    d1, d2 = J[0] - J[1], J[1] - J[2]
    p = np.log2(d1 / d2) if d1 * d2 > 0 else 1.0
    p = float(np.clip(p, 0.5, 4.0))
    lim = J[2] - d2 / (2.0 ** p - 1.0)
    return float(lim), float(abs(J[2] - lim)), p


for case, title in CASES:
    d = os.path.join(rv.RV, "geno", case)
    walks = {}
    for s, *_ in STARTS:
        f = os.path.join(rv.OUT, "t10_walk_%s_%s.json" % (case, s))
        if os.path.exists(f):
            walks[s] = json.load(open(f))
    if not walks:
        rep.note("%s: no walk output yet" % case)
        continue
    rp = RP.RaoPosing(d, K=120, n_fan=20, m=10, design=True, n_cplus=56)
    g = rp.g
    axial = case.startswith("axial")
    out_g, _ = rp.march_record(None)
    J_g0 = float(rp.J_of(out_g))
    o_f, _ = rp.march_record(rp.fit_geno())
    J_f0 = float(rp.J_of(o_f))
    rem = {}
    for s, w in walks.items():
        L_ = w["landing"]
        n = len(L_["W"])
        rem[s] = float(np.sqrt(n) * L_["grad_inf"] * w["switches"]["tr_floor"])      # relative to J (grad_inf / J)
        rep.note("%s, %s: start %+.3e -> landing %+.4e (J/J_GENO - 1, walk's grid; best spline %+.4e), |grad|/J %.1e, "
                 "remaining gain %.1e, max |y - y_GENO| %.2e, %d bases, %.0f s" % (
                     case, s, w["start_r"]["gap"], L_["gap"], J_f0 / J_g0 - 1, L_["grad_inf"], rem[s], L_["dy_max"],
                     w["segments"], w["seconds"]))
        rep.check("%s, %s: reach -- the landing is not below the best spline by more than the remaining gain"
                  % (case, s), (L_["J"] - J_f0) / J_g0, rem[s], ok=bool((L_["J"] - J_f0) / J_g0 >= -rem[s]))
    pairs = []
    for sa, sb in (("bump", "half"), ("cont_bump_it2", "cont_half_it2")):
        if sa in walks and sb in walks:
            a, b = walks[sa]["landing"], walks[sb]["landing"]
            # tolerance: the walk grid's resolution of differences between designs, read on the ladder of the first
            # start's (landing - best spline) from the walk's level to the finest (filled after the ladder below)
            pairs.append((sa, sb, a["J"] / b["J"] - 1.0))
            rep.note("%s: pair %s / %s: max |y_a - y_b| %.2e" % (
                case, sa, sb, float(np.max(np.abs(np.asarray(a["y"]) - np.asarray(b["y"]))))))
    # ---------------------------------------------------------------- the limit
    ladder = []
    for L in LEVELS:
        rl = RP.posing_level(d, L, design=True)
        row = dict(level=L, K=rl.K, N=rl.N)
        o, _ = rl.march_record(None)
        row["geno"], row["cert_geno"], row["bound"] = float(rl.J_of(o)), float(o["cert_worst"]), float(rl.mdot_start * rl.qpa)
        o, _ = rl.march_record(rl.fit_geno())
        row["fit"], row["cert_fit"] = float(rl.J_of(o)), float(o["cert_worst"])
        for s, w in walks.items():
            o, _ = rl.march_record(np.asarray(w["landing"]["W"]))
            row[s], row["cert_" + s] = float(rl.J_of(o)), float(o["cert_worst"])
        ladder.append(row)
        rep.note("  level %d (stations %d, rows %d): J/J_GENO - 1: fit %+.2e | %s | GENO vs mdot V_a %+.2e | worst cert %.2f"
                 % (L, rl.K, rl.N, row["fit"] / row["geno"] - 1, " | ".join("%s %+.2e" % (s, row[s] / row["geno"] - 1)
                                                                             for s in walks),
                    row["geno"] / row["bound"] - 1, max(v for k, v in row.items() if k.startswith("cert"))))
    certs_ok = all(v <= 1.0 for r_ in ladder for k, v in r_.items() if k.startswith("cert"))
    rep.check("%s: every re-march of the ladder certified" % case, 0.0, 0.0, ok=bool(certs_ok))
    # Richardson on DIFFERENCES between contours marched on the same grid (their march errors nearly cancel): the
    # difference's own ladder gives its limit and error bar; a single J's error bar (~2e-5 here) cannot resolve 1e-6
    def diff_limit(a, b):
        return richardson([(r_[a] - r_[b]) / r_["geno"] for r_ in ladder])
    lim = {}
    for s_ in list(walks):
        li, eb, p = diff_limit(s_, "fit")
        lim[s_] = (li, eb, p)
        rep.note("  limit of (landing %s - best spline) / J: %+.3e (error bar %.1e, order %.2f); per level %s" % (
            s_, li, eb, p, " ".join("%+.2e" % ((r_[s_] - r_["fit"]) / r_["geno"]) for r_ in ladder)))
        # DESCRIPTIVE (no pass/fail): a tolerance built from this landing's own change between grids would pass by
        # construction (a landing above the spline at the walk grid and below it finer always satisfies it)
        rep.note("  %s: landing - best spline at the walk grid %+.2e, in the limit %+.2e (the cost of maximising J_h)"
                 % (s_, (walks[s_]["landing"]["J"] - J_f0) / J_g0, li))
    # the walk grid's resolution of differences, read on two designs NOT optimised on any grid: how much
    # (best spline - GENO) moves from the walk grid to the finest level -- the yardstick of the pair test
    yard = abs((J_f0 - J_g0) / J_g0 - (ladder[-1]["fit"] - ladder[-1]["geno"]) / ladder[-1]["geno"])
    rep.note("  yardstick: (best spline - GENO) moves by %.2e from the walk grid to the finest level" % yard)
    for sa, sb, dJ in pairs:
        rep.check("%s: pair %s / %s -- one value, within the grid's resolution of differences (yardstick)" % (case, sa, sb),
                  dJ, yard)
    li, eb, p = diff_limit("fit", "geno")
    lim["fit"] = (li, eb, p)
    rep.note("  limit of (best spline - GENO) / J, the basis' cost: %+.3e (error bar %.1e, order %.2f); per level %s" % (
        li, eb, p, " ".join("%+.2e" % ((r_["fit"] - r_["geno"]) / r_["geno"]) for r_ in ladder)))
    gl = richardson([r_["geno"] / r_["bound"] - 1.0 for r_ in ladder])
    lim["geno_over_bound"] = gl
    rep.note("  limit of J_GENO / (mdot V_a) - 1: %+.3e (error bar %.1e, order %.2f)" % gl)
    if axial:
        rep.check("%s: GENO's contour reaches the bound mdot V_a in the limit (Richardson)" % case, gl[0], gl[1])
        xw = np.linspace(g.x_s, g.D[0], 2000)
        ang = np.arctan(np.gradient(dense_wall(rp, rp.fit_geno(), xw), xw)) - np.arctan(rp.wall_of(xw)[1])
        dth = float(np.sqrt(np.mean(ang ** 2)))
        rep.note("  the best spline's wall-angle error: rms %.2e rad -> planar estimate -2 dth^2 = %+.1e" % (dth, -2 * dth ** 2))
    # ---------------------------------------------------------------- figure
    xd = np.linspace(g.x_s, g.D[0], 700)
    yg = rp.wall_of(xd)[0]
    fig, ax = plt.subplots(2, 1, figsize=(11.5, 7.8), constrained_layout=True, gridspec_kw=dict(height_ratios=[2.2, 1]),
                           sharex=True)
    fig.suptitle("%s: the SQP results against Rao's method (GENO)" % title, fontsize=12)
    A, B = ax
    xu = np.linspace(rp.wall_g[0, 0], g.x_s, 200)
    A.plot(np.r_[xu, xd], np.r_[rp.wall_of(xu)[0], yg], "-", color="0.25", lw=5, alpha=0.35,
           label="GENO, Rao's method%s" % (" (= the bound mdot V_a)" if axial else ""))
    A.plot(g.cowl[:, 0], g.cowl[:, 1], "-", color="0.5", lw=1.2, label="cowl (GENO)")
    A.plot(g.cplus[:, 0], g.cplus[:, 1], "-", color="k", lw=0.9, label="start line: GENO's last internal C+")
    A.plot(g.ED[:, 0], g.ED[:, 1], "--", color="0.45", lw=0.9,
           label="control surface ED" + (" (uniform, axial, p = p_a)" if axial else ""))
    A.plot(g.first_wave[:, 0], g.first_wave[:, 1], ":", color="0.45", lw=0.9)
    A.annotate("x_s: first lip wave lands", (g.x_s, g.y_s), (g.x_s + 0.03, g.y_s + 0.06), fontsize=8,
               arrowprops=dict(arrowstyle="->", lw=0.6))
    if not axial:
        A.plot(R61.TAB1[1:, 0], R61.TAB1[1:, 1], "o", mfc="none", mec="k", ms=6, label="Rao 1961, Table 1")
    for s, lab, c, ls in STARTS:
        if s not in walks:
            continue
        w = walks[s]
        y1 = dense_wall(rp, w["landing"]["W"], xd)
        if not s.startswith("cont"):
            y0 = dense_wall(rp, w["start_r"]["W"], xd)
            A.plot(xd, y0, ":", color=c, lw=1.4, label=lab)
            B.plot(xd, 1e3 * (y0 - yg), ":", color=c, lw=1.2)
        A.plot(xd, y1, ls, color=c, lw=1.3, label=("  SQP result" if not s.startswith("cont") else "SQP " + lab))
        B.plot(xd, 1e3 * (y1 - yg), ls, color=c, lw=1.6)
    B.plot(xd, 1e3 * (dense_wall(rp, rp.fit_geno(), xd) - yg), "-.", color="k", lw=1.0, label="best spline of GENO's contour")
    if not axial:
        tab = R61.TAB1[1:]
        k = tab[:, 0] >= g.x_s
        B.plot(tab[k, 0], 1e3 * (tab[k, 1] - rp.wall_of(tab[k, 0])[0]), "o", mfc="none", mec="k", ms=5,
               label="Rao 1961 Table 1 (3 decimals: +-0.5)")
    A.set_ylabel("y / y_E")
    A.legend(fontsize=8, loc="upper right")
    B.axhline(0, color="0.5", lw=0.8)
    B.set_ylim(-4, 4)
    B.set_xlabel("x / y_E")
    B.set_ylabel("(y - y_GENO) x 1000")
    B.legend(fontsize=8, loc="lower left")
    rv.savefig(fig, "10_profiles_%s.png" % ("axial" if axial else "rao1961"))
    extra[case] = dict(ladder=ladder, limits=lim, J_geno_walk=J_g0, J_fit_walk=J_f0,
                       walks={s: dict(start=w["start_r"]["gap"], landing=w["landing"]["gap"],
                                      over_bound=w["landing"]["over_bound"], dy_max=w["landing"]["dy_max"],
                                      grad=w["landing"]["grad_inf"], remaining=rem[s], bases=w["segments"],
                                      seconds=w["seconds"], switches=w["switches"]) for s, w in walks.items()})
sys.exit(rep.save(extra))
