#!/usr/bin/env python3
"""T11 -- the profiles themselves: every optimiser result of T08a/T08b/T08c drawn over its reference optimum (top),
with the difference magnified underneath (bottom). No new computation: walls rebuilt from the saved design vectors.
usage: t11_profiles.py [a] [b] [c]   (default: all)
"""
import json
import os
import sys

RV = "/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07"
sys.path.insert(0, os.path.join(RV, "ref"))
import numpy as np                                 # noqa: E402
import matplotlib                                  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                    # noqa: E402
import rv                                          # noqa: E402

which = sys.argv[1:] or ["a", "b", "c"]
J = lambda n: json.load(open(os.path.join(rv.OUT, n + ".json")))   # noqa: E731
COL = dict(ref="0.25", s1="C0", s2="C1", s3="C2", s4="C3")


def two_rows(title, ratio=(2.2, 1.0), w=11.5, h=7.6):
    fig, ax = plt.subplots(2, 1, figsize=(w, h), constrained_layout=True, gridspec_kw=dict(height_ratios=ratio),
                           sharex=True)
    fig.suptitle(title, fontsize=12)
    return fig, ax


# ---------------------------------------------------------------------------------------------------- T08a
if "a" in which:
    import planar_posing as PP
    pp = PP.PlanarPlug(K=800, N=21, m=12, L=2.0)
    x = np.asarray(pp.sx)
    yi = np.asarray(pp.y_ideal(x))
    runs = [("A0_K80", "start: ideal plug + bump (2 % of inlet height)", COL["s1"]),
            ("B0_K80_f256", "start: ideal plug of a 15 deg fan (designed for another ambient)", COL["s2"]),
            ("C0_K80_f256", "start: straight line", COL["s3"])]
    fig, ax = two_rows("Planar plug: the SQP results against the exact ideal plug (thrust = mdot V_a)")
    A, B = ax
    A.plot(np.r_[PP.X0, x], np.r_[0.5, yi], "-", color=COL["ref"], lw=5, alpha=0.35, label="exact ideal plug (the optimum)")
    for tag, lab, c in runs:
        d = J("t08a_walk_" + tag)
        y0 = np.asarray(pp.walls(np.asarray(d["start_r"]["W"]))[1])
        y1 = np.asarray(pp.walls(np.asarray(d["landing"]["W"]))[1])
        A.plot(x, y0, ":", color=c, lw=1.4, label=lab)
        A.plot(x, y1, "-", color=c, lw=1.2, label="  SQP result (thrust %+.1e of the bound)" % d["landing"]["gap"])
        B.plot(x, 1e3 * (y0 - yi), ":", color=c, lw=1.2)
        B.plot(x, 1e3 * (y1 - yi), "-", color=c, lw=1.6)
    d = J("t08a_walk_B1_K80_f256")
    y1 = np.asarray(pp.walls(np.asarray(d["landing"]["W"]))[1])
    B.plot(x, 1e3 * (y1 - yi), "-.", color="C4", lw=1.4, label="SQP with the no-fold class ON (stalls, %+.1e)" % d["landing"]["gap"])
    yf = np.asarray(pp.walls(pp.fit_ideal())[1])
    B.plot(x, 1e3 * (yf - yi), "--", color="k", lw=1.0, label="best 12-knot spline of the ideal plug")
    A.plot([PP.X0, PP.X0], [0.5, 1.0], "-", color="k", lw=1.0)
    A.annotate("start line (M 1.556 at -20 deg)", (PP.X0, 0.75), (PP.X0 + 0.05, 0.85), fontsize=9)
    A.set_ylabel("y")
    A.legend(fontsize=8, loc="upper right")
    B.set_ylim(-8, 8)
    B.axhline(0, color="0.5", lw=0.8)
    B.set_xlabel("x")
    B.set_ylabel("(y - y_ideal) x 1000")
    B.legend(fontsize=8, loc="lower left")
    rv.savefig(fig, "11_profiles_planar.png")

# ---------------------------------------------------------------------------------------------------- T08b
if "b" in which:
    import jax.numpy as jnp
    import rao_posing as RP
    from a1_toc_variational_jax import spline_coeffs, spline_eval
    import jax
    rp = RP.RaoPosing(os.path.join(rv.RV, "geno", "rao_sdt_L0448"), K=120, n_fan=20, m=10, design=True)
    g = rp.g
    xd = np.linspace(g.x_s, g.D[0], 800)
    xk = np.r_[g.x_s, rp.xk]

    def dense(W):
        yk = np.r_[g.y_s, np.asarray(W), g.D[1]]
        Mc = spline_coeffs(jnp.asarray(xk), jnp.asarray(yk), rp.slope_s)
        return np.asarray(jax.vmap(lambda xx: spline_eval(xx, jnp.asarray(xk), jnp.asarray(yk), Mc)[0])(jnp.asarray(xd)))
    yg = rp.wall_of(xd)[0]
    fig, ax = two_rows("Rao plug, methane gas, lip Mach 1.556: the SQP results against GENO's Rao contour")
    A, B = ax
    xu = np.linspace(rp.wall_g[0, 0], g.x_s, 200)
    A.plot(np.r_[xu, xd], np.r_[rp.wall_of(xu)[0], yg], "-", color=COL["ref"], lw=5, alpha=0.35,
           label="GENO, Rao's method (the optimum of this problem)")
    A.plot(g.cowl[:, 0], g.cowl[:, 1], "-", color="0.5", lw=1.2, label="cowl (GENO)")
    A.plot(g.cplus[:, 0], g.cplus[:, 1], "-", color="k", lw=0.9, label="start line: GENO's last internal C+")
    A.plot(g.ED[:, 0], g.ED[:, 1], "--", color="0.45", lw=0.9, label="Rao's control surface ED")
    A.plot(g.first_wave[:, 0], g.first_wave[:, 1], ":", color="0.45", lw=0.9)
    A.annotate("x_s: first lip wave lands", (g.x_s, g.y_s), (g.x_s + 0.02, g.y_s + 0.06), fontsize=8,
               arrowprops=dict(arrowstyle="->", lw=0.6))
    for tag, lab, c in (("A0", "start: Rao's contour + bump (1 % of lip radius)", COL["s1"]),
                        ("C0", "start: straight line from x_s to D", COL["s2"])):
        d = J("t08b_walk_" + tag)
        y0, y1 = dense(d["start_r"]["W"]), dense(d["landing"]["W"])
        A.plot(xd, y0, ":", color=c, lw=1.4, label=lab)
        A.plot(xd, y1, "-", color=c, lw=1.2, label="  SQP result (thrust %+.1e of Rao's)" % d["landing"]["gap"])
        B.plot(xd, 1e3 * (y0 - yg), ":", color=c, lw=1.2)
        B.plot(xd, 1e3 * (y1 - yg), "-", color=c, lw=1.6)
    B.plot(xd, 1e3 * (dense(rp.fit_geno()) - yg), "--", color="k", lw=1.0, label="best spline of Rao's contour")
    A.set_ylabel("y / y_E")
    A.legend(fontsize=8, loc="upper right")
    B.axhline(0, color="0.5", lw=0.8)
    B.set_ylim(-3, 3)
    B.set_xlabel("x / y_E")
    B.set_ylabel("(y - y_Rao) x 1000")
    B.legend(fontsize=8, loc="lower left")
    rv.savefig(fig, "11_profiles_rao_methane.png")

# ---------------------------------------------------------------------------------------------------- T08c
if "c" in which:
    os.environ.update(dict(TWOP_GAS=os.path.join(rv.OUT, "t08c_gas.json"), PSPL_JSCALE="radius", PSPL_TRFOLLOW="1",
                           TWOP_ART="/tmp/claude-1700/-data10-falco-MOSE/92599c7b-9637-4352-802d-d26f8eac9fd5/scratchpad/twop_art"))
    import a1_twowall as T
    tw = T.TwoWall()
    W_ref = np.asarray(tw.W_ref, float)
    (xp, yp, _), (xs, ys, _) = (tuple(np.asarray(v) for v in w) for w in tw.walls(W_ref))
    fig, ax = two_rows("Annular nozzle (GENO's Migdal walls, vacuum): the SQP results against the perfect nozzle")
    A, B = ax
    A.plot(xp, yp, "-", color=COL["ref"], lw=5, alpha=0.35, label="GENO's Migdal walls (perfect nozzle)")
    A.plot(xs, ys, "-", color=COL["ref"], lw=5, alpha=0.35)
    for tag, lab, c in (("t08c_walk_0", "SQP, no class (start: 1 % bump)", COL["s1"]),
                        ("t08c_walk_1_a0.002", "SQP, no-fold class ON (start: 0.2 % bump, inside the class)", COL["s2"])):
        d = J(tag)
        (x0p, y0p, _), (x0s, y0s, _) = (tuple(np.asarray(v) for v in w) for w in tw.walls(np.asarray(d["start_r"]["W"])))
        (x1p, y1p, _), (x1s, y1s, _) = (tuple(np.asarray(v) for v in w) for w in tw.walls(np.asarray(d["landing"]["W"])))
        if tag.endswith("_0"):
            A.plot(x0p, y0p, ":", color="0.4", lw=1.3, label="start: Migdal walls + bump (1 %)")
            A.plot(x0s, y0s, ":", color="0.4", lw=1.3)
            B.plot(x0p, 1e3 * (y0p - yp), ":", color="0.4", lw=1.2, label="start (plug)")
            B.plot(x0s, 1e3 * (y0s - ys), "--", color="0.4", lw=1.0, label="start (shroud)")
        A.plot(x1p, y1p, "-", color=c, lw=1.2, label="%s (C_F %+.1e of GENO's)" % (lab, d["landing"]["J"] / d["ref"]["J"] - 1))
        A.plot(x1s, y1s, "-", color=c, lw=1.2)
        B.plot(x1p, 1e3 * (y1p - yp), "-", color=c, lw=1.6, label=lab + " (plug)")
        B.plot(x1s, 1e3 * (y1s - ys), "--", color=c, lw=1.6, label=lab + " (shroud)")
    d = J("t08c_walk_1")
    (x1p, y1p, _), _ = (tuple(np.asarray(v) for v in w) for w in tw.walls(np.asarray(d["landing"]["W"])))
    B.plot(x1p, 1e3 * (y1p - yp), "-.", color="C3", lw=1.2,
           label="class ON from the 1 % bump: no step (start outside the class, restoration inert)")
    A.set_ylabel("y")
    A.legend(fontsize=8, loc="lower left")
    B.axhline(0, color="0.5", lw=0.8)
    B.set_xlabel("x")
    B.set_ylabel("(y - y_GENO) x 1000")
    B.legend(fontsize=7, loc="upper right", ncol=2)
    rv.savefig(fig, "11_profiles_migdal.png")
