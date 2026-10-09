#!/usr/bin/env python3
"""T17 -- one uniform reading of every optimiser case for the slide deck (agnostic driver a1_qntr, one setting for all):
for each case, the known optimum, the landings from >= 2 starts, re-marched on three grids, and one overlay figure.
  numbers per landing: (J - J_opt)/J_opt at the walk grid and at the finest grid; the Richardson limit of that
  difference (differences between walls marched on the same grid: the march errors nearly cancel); the gap to the best
  design of the basis (the best spline of the optimum) on the same grids; the distance between the walls; the driver's
  report (stop reason, trials, marches, time, gain it still predicts).
usage: t17_slides.py <planar|methane|rao61|axial|hth|migdal|bell|bellideal> ...   -> out/t17_<case>.json, figs/17_<case>.png
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import matplotlib                                  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                    # noqa: E402

plt.rcParams.update({"font.size": 11, "axes.titlesize": 12, "legend.fontsize": 9})
Jl = lambda n: json.load(open(os.path.join(rv.OUT, n + ".json")))          # noqa: E731
ex = lambda n: os.path.exists(os.path.join(rv.OUT, n + ".json"))           # noqa: E731
COLS = ["C0", "C1", "C2", "C3"]


def richardson(v):
    d1, d2 = v[0] - v[1], v[1] - v[2]
    p = np.log2(d1 / d2) if d1 * d2 > 0 else 1.0
    p = float(np.clip(p, 0.5, 4.0))
    lim = v[2] - d2 / (2.0 ** p - 1.0)
    return float(lim), float(abs(v[2] - lim)), p


def report_of(name):
    """the agnostic driver's report: in the walk's JSON (t10, t15) or beside it (t08: <tag>_report.json)"""
    d = Jl(name)
    if d.get("qntr"):
        return d["qntr"]
    if ex(name + "_report"):
        return Jl(name + "_report")
    return {}


CASE = [None]


def ladder(levels, make, ref_W, fit_W, runs, J_ref_fn=None):
    """re-march: rows of J for the reference (or its value function), the fit and every landing on each level.
    Cached in out/t17_<case>_rows.json, keyed by the design vectors (a figure error never costs a re-march)."""
    key = dict(levels=[str(l) for l in levels], fit=np.asarray(fit_W, float).round(14).tolist(),
               runs={k: np.asarray(W, float).round(14).tolist() for k, (_, W) in runs.items()})
    cf = os.path.join(rv.OUT, "t17_%s_rows.json" % CASE[0])
    if os.path.exists(cf):
        c = json.load(open(cf))
        if c.get("key") == key:
            print("  ladder: cached (%s)" % cf, flush=True)
            return c["rows"]
    rows = []
    for lev in levels:
        po = make(lev)
        row = dict(level=str(lev))
        if J_ref_fn is not None:
            row["ref"] = J_ref_fn(po)
        else:
            o, _ = po.march_record(ref_W)
            row["ref"] = float(po.J_of(o))
        o, _ = po.march_record(np.asarray(fit_W, float))
        row["fit"], row["cert_fit"] = float(po.J_of(o)), float(o["cert_worst"])
        for k, (lab, W) in runs.items():
            o, _ = po.march_record(np.asarray(W, float))
            row[k], row["cert_" + k] = float(po.J_of(o)), float(o["cert_worst"])
        rows.append(row)
        print("  level %s: J_opt %.10e | fit %+.3e | %s" % (lev, row["ref"], row["fit"] / row["ref"] - 1, " | ".join(
            "%s %+.3e (cert %.2f)" % (k, row[k] / row["ref"] - 1, row["cert_" + k]) for k in runs)), flush=True)
    json.dump(dict(key=key, rows=rows), open(cf, "w"), indent=1, default=float)
    return rows


def numbers(rows, runs, walls, walk_level=None, pair=None):
    res = dict(rows=rows, runs={})
    for k in list(runs) + ["fit"]:
        g = [r_[k] / r_["ref"] - 1.0 for r_ in rows]
        dfit = [(r_[k] - r_["fit"]) / r_["ref"] for r_ in rows]
        res["runs"][k] = dict(gap=g, gap_lim=richardson(g), minus_fit=dfit, minus_fit_lim=richardson(dfit),
                              walk_level=(walk_level or {}).get(k, 0))
    ks = list(pair) if pair else list(runs)
    if len(ks) >= 2 and ks[0] in runs and ks[1] in runs:
        a, b = ks[0], ks[1]
        res["pair"] = dict(a=a, b=b, dJ=[(r_[a] - r_[b]) / r_["ref"] for r_ in rows],
                           dwall=float(np.max(np.abs(walls[a] - walls[b]))))
    res["yardstick"] = abs(res["runs"]["fit"]["gap"][0] - res["runs"]["fit"]["gap"][-1])
    return res


def figure(case, title, x, y_ref, ref_label, starts, lands, fit_y, ylab, dlab, extra=None, scale=1e3, legend_loc="best"):
    fig, ax = plt.subplots(2, 1, figsize=(8.2, 5.6), constrained_layout=True, sharex=True,
                           gridspec_kw=dict(height_ratios=[1.7, 1]))
    A, B = ax
    A.plot(x, y_ref, "-", color="0.2", lw=6, alpha=0.3, label=ref_label)
    for i, (lab, y0) in enumerate(starts):
        A.plot(x, y0, ":", color=COLS[i], lw=1.6, label="start: " + lab)
        B.plot(x, scale * (y0 - y_ref), ":", color=COLS[i], lw=1.3)
    for i, ln in enumerate(lands):
        lab, y1 = ln[0], ln[1]
        col = ln[2] if len(ln) > 2 else COLS[i]
        ls = ln[3] if len(ln) > 3 else "-"
        A.plot(x, y1, ls, color=col, lw=1.3, label=lab)
        B.plot(x, scale * (y1 - y_ref), ls, color=col, lw=1.8)
    if fit_y is not None:
        B.plot(x, scale * (fit_y - y_ref), "--", color="k", lw=1.0, label="closest curve to the optimum (same number of points)")
    if extra:
        extra(A, B)
    A.set_ylabel(ylab)
    A.legend(loc=legend_loc, framealpha=0.9)
    A.set_title(title)
    B.axhline(0, color="0.5", lw=0.8)
    lim = max(1e-9, np.max([np.max(np.abs(scale * (ln[1] - y_ref))) for ln in lands] + (
        [np.max(np.abs(scale * (fit_y - y_ref)))] if fit_y is not None else [])))
    B.set_ylim(-2.5 * lim, 2.5 * lim)
    B.set_ylabel(dlab)
    B.set_xlabel("x")
    if fit_y is not None:
        B.legend(loc="lower left", framealpha=0.9)
    rv.savefig(fig, "17_%s.png" % case)
    plt.close(fig)


def save(case, res):
    json.dump(res, open(os.path.join(rv.OUT, "t17_%s.json" % case), "w"), indent=1, default=float)
    print("== t17 %s saved" % case, flush=True)


# ------------------------------------------------------------------------------------------------------------ cases
def case_planar():
    import planar_posing as PP
    runs_n = dict(B="t08a_walk_B0_K80_qntr", C="t08a_walk_C0_K80_qntr", A1="t08a_walk_A1_K80_qntr",
                  B1="t08a_walk_B1_K80_qntr")
    runs_n = {k: v for k, v in runs_n.items() if ex(v)}
    d = {k: Jl(v) for k, v in runs_n.items()}
    fit_W = next(iter(d.values()))["fit"]["W"]
    pp0 = PP.PlanarPlug(K=80, N=21, m=12, L=2.0)
    T = pp0.T_ideal
    rows = ladder([(80, 21), (160, 41), (320, 81)], lambda lv: PP.PlanarPlug(K=lv[0], N=lv[1], m=12, L=2.0), None,
                  fit_W, {k: ("", w["landing"]["W"]) for k, w in d.items()}, J_ref_fn=lambda po: T)
    pf = PP.PlanarPlug(K=800, N=21, m=12, L=2.0)
    x = np.asarray(pf.sx)
    yi = np.asarray(pf.y_ideal(x))
    wy = lambda W: np.asarray(pf.walls(np.asarray(W, float))[1])                # noqa: E731
    walls = {k: wy(w["landing"]["W"]) for k, w in d.items()}
    res = numbers(rows, d, walls)
    res["report"] = {k: report_of(v) for k, v in runs_n.items()}
    labs = dict(B="ideal plug for another ambient (15 deg fan)", C="straight line",
                A1="ideal plug deformed by 2 %, no-fold rule on, starting outside it",
                B1="ideal plug for another ambient, no-fold rule on")
    show = [k for k in ("B", "C") if k in d]
    figure("planar", "Planar plug vs the exact ideal plug (T = mdot V_a)", x, yi, "exact ideal plug (the optimum)",
           [(labs[k], wy(d[k]["start_r"]["W"])) for k in show],
           [("result from: " + labs[k], walls[k]) for k in show] +
           ([("result with the no-fold rule on (start outside it)", walls["A1"])] if "A1" in walls else []),
           wy(fit_W), "y", "(y - y_ideal) x 1000")
    save("planar", res)


def _rao_case(case, geno, runs_n, labs, title, cname, fit_from=None, lit=None):
    import jax
    import jax.numpy as jnp
    import rao_posing as RP
    from a1_toc_variational_jax import spline_coeffs, spline_eval
    runs_n = {k: v for k, v in runs_n.items() if ex(v)}
    d = {k: Jl(v) for k, v in runs_n.items()}
    D = os.path.join(rv.RV, "geno", geno)
    kw = dict(n_cplus=56) if geno.endswith("mi15") else {}
    rp = RP.RaoPosing(D, K=120, n_fan=20, m=10, design=True, **kw)
    fit_W = rp.fit_geno()

    def make(L):
        return RP.posing_level(D, L, design=True)
    rows = ladder([1, 2, 3], make, None, fit_W, {k: ("", w["landing"]["W"]) for k, w in d.items()},
                  J_ref_fn=lambda po: float(po.J_of(po.march_record(None)[0])))
    g = rp.g
    xd = np.linspace(g.x_s, g.D[0], 700)
    xk = np.r_[g.x_s, rp.xk]

    def dense(W):
        yk = np.r_[g.y_s, np.asarray(W), g.D[1]]
        Mc = spline_coeffs(jnp.asarray(xk), jnp.asarray(yk), rp.slope_s)
        return np.asarray(jax.vmap(lambda xx: spline_eval(xx, jnp.asarray(xk), jnp.asarray(yk), Mc)[0])(jnp.asarray(xd)))
    yg = rp.wall_of(xd)[0]
    walls = {k: dense(w["landing"]["W"]) for k, w in d.items()}
    res = numbers(rows, d, walls)
    res["report"] = {k: report_of(v) for k, v in runs_n.items()}
    if case == "axial":
        bnd = []
        for L in (1, 2, 3):
            po = make(L)
            bnd.append(float(po.mdot_start * po.qpa))
        res["bound"] = bnd
        res["geno_over_bound"] = [r_["ref"] / b - 1.0 for r_, b in zip(rows, bnd)]
        res["geno_over_bound_lim"] = richardson(res["geno_over_bound"])
    starts = [k for k in d if not k.startswith("old")][:2]
    extra = None
    if lit is not None:
        lx, ly, llab = lit

        def extra(A, B):
            k_ = (lx >= g.x_s) & (lx <= g.D[0] + 1e-3)      # the designed part (upstream: GENO's internal part)
            A.plot(lx[k_], ly[k_], "o", mfc="none", mec="k", ms=6, label=llab)
            B.plot(lx[k_], 1e3 * (ly[k_] - rp.wall_of(lx[k_])[0]), "o", mfc="none", mec="k", ms=5)
    figure(cname, title, xd, yg, "GENO, Rao's method (the optimum)",
           [(labs[k], dense(d[k]["start_r"]["W"])) for k in starts],
           [("result from: " + labs[k], walls[k]) for k in starts] +
           [(labs[k], walls[k]) for k in d if k.startswith("old")], dense(fit_W), "y / y_E", "(y - y_Rao) x 1000",
           extra=extra)
    save(cname, res)


def case_methane():
    _rao_case("methane", "rao_sdt_L0448", dict(A="t08b_walk_A0_qntr", C="t08b_walk_C0_qntr"),
              dict(A="Rao's contour deformed (up to 1 % of the lip radius)", C="straight line from x_s to D"),
              "Rao plug, methane, lip Mach 1.556 (RDE-like)", "methane")


def case_rao61():
    import rao1961 as R61
    c = "rao61_e381_pbR_mi15"
    _rao_case("rao61", c, dict(bump="t10_walk_%s_bump_qntr" % c, half="t10_walk_%s_half_qntr" % c,
                               old_bump="t10_walk_%s_bump" % c, old_half="t10_walk_%s_half" % c),
              dict(bump="Rao's contour deformed (up to 1 %)", half="average of Rao's contour and a straight line",
                   old_bump="old driver, from the deformed contour: stopped short",
                   old_half="old driver, from the average contour: stopped short"),
              "Rao 1961, eps 3.81 (paper's Table 1)", "rao61",
              lit=(R61.TAB1[1:, 0], R61.TAB1[1:, 1], "Rao 1961, Table 1 (printed, 3 decimals)"))


def case_axial():
    c = "axial_e381_RD04_mi15"
    _rao_case("axial", c, dict(bump="t10_walk_%s_bump_qntr" % c, half="t10_walk_%s_half_qntr" % c),
              dict(bump="Rao's contour deformed (up to 1 %)", half="average of Rao's contour and a straight line"),
              "Axial exit (Rao theta_E = 0, plug ended at R_D 0.4)", "axial")


def case_hth():
    import rao1961 as R61
    h = R61.hth_rao(n=20001)
    c = "hth71_rao_mi17"
    _rao_case("hth", c, dict(bump="t10_walk_%s_bump_qntr" % c, half="t10_walk_%s_half_qntr" % c),
              dict(bump="Rao's contour deformed (up to 1 %)", half="average of Rao's contour and a straight line"),
              "Humphreys et al. 1971: their Rao plug (148 lbm/s, 500 psia, 14.7 psia, length 11.52 in)", "hth",
              lit=(R61.TAB3_HTH[:, 0] / h["R_E_in"], R61.TAB3_HTH[:, 1] / h["R_E_in"],
                   "Humphreys 1971, Table 3 (Rao's contour, printed)"))


def case_migdal():
    os.environ.update(dict(TWOP_GAS=os.path.join(rv.OUT, "t08c_gas.json"),
                           TWOP_ART="/tmp/claude-1700/-data10-falco-MOSE/92599c7b-9637-4352-802d-d26f8eac9fd5/scratchpad/twop_art"))
    import a1_twowall as T
    runs_n = {k: v for k, v in dict(free="t08c_walk_0_qntr", cls="t08c_walk_1_qntr").items() if ex(v)}
    d = {k: Jl(v) for k, v in runs_n.items()}
    tw = T.TwoWall()
    W_ref = np.asarray(tw.W_ref, float)
    rows = ladder([(140, 31), (280, 61), (560, 121)], lambda lv: T.TwoWall(K=lv[0], N=lv[1], verbose=False), W_ref,
                  W_ref, {k: ("", w["landing"]["W"]) for k, w in d.items()})
    (xp, yp, _), (xs, ys, _) = (tuple(np.asarray(v) for v in w) for w in tw.walls(W_ref))
    xx = np.r_[xp, xs]
    yy = lambda W: np.concatenate([np.asarray(v[1]) for v in tw.walls(np.asarray(W, float))])   # noqa: E731
    walls = {k: yy(w["landing"]["W"]) for k, w in d.items()}
    res = numbers(rows, d, walls)
    res["CF_1d"] = tw.CF_1d
    res["report"] = {k: report_of(v) for k, v in runs_n.items()}
    labs = dict(free="without the no-fold rule", cls="with the no-fold rule (start breaking it)")
    np_ = len(xp)
    fig, ax = plt.subplots(2, 1, figsize=(8.2, 5.6), constrained_layout=True, sharex=True,
                           gridspec_kw=dict(height_ratios=[1.7, 1]))
    A, B = ax
    A.plot(xp, yp, "-", color="0.2", lw=6, alpha=0.3, label="GENO's Migdal walls (perfect nozzle)")
    A.plot(xs, ys, "-", color="0.2", lw=6, alpha=0.3)
    y0 = yy(d[next(iter(d))]["start_r"]["W"])
    A.plot(xp, y0[:np_], ":", color="0.4", lw=1.4, label="start: both walls deformed by 1 %")
    A.plot(xs, y0[np_:], ":", color="0.4", lw=1.4)
    for i, k in enumerate(d):
        A.plot(xp, walls[k][:np_], "-", color=COLS[i], lw=1.3, label="result " + labs[k])
        A.plot(xs, walls[k][np_:], "-", color=COLS[i], lw=1.3)
        B.plot(xp, 1e3 * (walls[k][:np_] - yp), "-", color=COLS[i], lw=1.8)
        B.plot(xs, 1e3 * (walls[k][np_:] - ys), "--", color=COLS[i], lw=1.8)
    A.set_ylabel("y")
    A.legend(loc="best")
    A.set_title("Annular nozzle (GENO's Migdal walls, vacuum): optimum C_F,1D")
    B.axhline(0, color="0.5", lw=0.8)
    B.set_ylabel("(y - y_GENO) x 1000\nsolid: plug, dashed: shroud")
    B.set_xlabel("x")
    rv.savefig(fig, "17_migdal.png")
    plt.close(fig)
    save("migdal", res)


def _bell(case, runs_n, labs, title, walk_level=None, pair=None):
    import bell_posing as BP
    runs_n = {k: v for k, v in runs_n.items() if ex(v)}
    d = {k: Jl(v) for k, v in runs_n.items()}
    w0 = next(iter(d.values()))
    L, yL = w0["L"], w0["yL"]
    gx, gy = np.asarray(w0["geno_x"]), np.asarray(w0["geno_y"])
    bp = BP.BellPosing(L, yL, NI=41, Nw=120)
    fit_V = bp.fit_lsq(gx, gy)

    class Lev:
        def __init__(self, lv):
            self.b = BP.BellPosing(L, yL, NI=lv[0], Nw=lv[1])

        def march_record(self, V):
            return self.b.record(V)

        def J_of(self, o):
            return self.b.J_of(o)
    # the reference is the best spline of GENO's wall (the engine marches only its own class)
    rows = ladder([(41, 120), (81, 240), (161, 480)], Lev, fit_V, fit_V,
                  {k: ("", w["landing"]["V"]) for k, w in d.items()})
    xg = np.linspace(0.0, L, 800)
    yref = np.interp(xg, gx, gy)
    wy = lambda V: np.interp(xg, *bp.wall_xy(np.asarray(V, float)))             # noqa: E731
    walls = {k: wy(w["landing"]["V"]) for k, w in d.items()}
    res = numbers(rows, d, walls, walk_level=walk_level, pair=pair)
    if pair and all((k + "81") in d for k in pair):
        a, b = pair[0] + "81", pair[1] + "81"
        res["pair81"] = dict(a=a, b=b, dJ=[(r_[a] - r_[b]) / r_["ref"] for r_ in rows],
                             dwall=float(np.max(np.abs(walls[a] - walls[b]))))
    res["report"] = {k: w.get("qntr", {}) for k, w in d.items()}
    res["fit_V"] = fit_V.tolist()
    res["geno_cf"] = w0["geno_cf"]
    res["thB"] = dict(fit=float(np.degrees(fit_V[0])), **{k: float(np.degrees(w["landing"]["V"][0])) for k, w in d.items()},
                      **{"start_" + k: float(np.degrees(w["start_r"]["V"][0])) for k, w in d.items()})
    coarse = [k for k in d if (walk_level or {}).get(k, 0) == 0]
    lands = []
    for i, k in enumerate(coarse):
        lands.append(("result from: " + labs[k], walls[k], COLS[i], "-"))
        if k + "81" in d:
            lands.append(("  same start, grid twice as fine", walls[k + "81"], COLS[i], "--"))
    figure(case, title, xg, yref, "GENO, Rao's method (the optimum)",
           [(labs[k], wy(d[k]["start_r"]["V"])) for k in coarse], lands, wy(fit_V), "y / r_t", "(y - y_GENO) x 1000",
           legend_loc="lower right")
    save(case, res)


def case_bell():
    _bell("bell", dict(tic="t15_bell_toc_tic", tic81="t15_bell_toc_tic_NI81", steep="t15_bell_toc_steep",
                       steep81="t15_bell_toc_steep_NI81"),
          dict(tic="truncated ideal contour (attachment 12.9 deg)",
               steep="Rao's contour for length 6 squeezed to 4 (attachment 28.7 deg)",
               tic81="same start, grid twice as fine", steep81="same start, grid twice as fine"),
          "Bell, eps 4, length 4 r_t: Rao's thrust-optimised contour (TOC)",
          walk_level=dict(tic81=1, steep81=1), pair=("tic", "steep"))


def case_bellideal():
    _bell("bellideal", dict(stretched="t15_bell_ideal_stretched", stretched81="t15_bell_ideal_stretched_NI81",
                            extended="t15_bell_ideal_extended", extended81="t15_bell_ideal_extended_NI81"),
          dict(stretched="Rao's contour for length 6 stretched to 7.34", extended="Rao's contour for length 6 + a cylinder",
               stretched81="same (stretched) start, grid twice as fine", extended81="same (cylinder) start, grid twice as fine"),
          "Bell, eps 4, at the ideal length 7.34 r_t: the ideal bell (uniform exit)",
          walk_level=dict(stretched81=1, extended81=1), pair=("stretched", "extended"))


for c in sys.argv[1:]:
    print("== t17 %s" % c, flush=True)
    CASE[0] = c
    globals()["case_" + c]()
