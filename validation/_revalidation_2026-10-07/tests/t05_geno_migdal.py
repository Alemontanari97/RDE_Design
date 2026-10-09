#!/usr/bin/env python3
"""T05 -- cross-code: the model's two-wall march on the walls of GENO's PERFECT ANNULAR NOZZLE (nozzle_type 9,
Migdal; GENO exp/ws-c-prod-nozzles 28c7e7a, bin/GENO md5 in geno/<case>/geno_binary.md5), same inflow (uniform,
axial, M_i on the vertical line x = 0 between Y_L and Y_U = GENO's IVLINE_annular_solve with theta_i = 0), vacuum.

Two cases (geno/<case>_ni1001_ne2000/, thermo written self-consistent by ref/geno_io.py; the model uses GENO's
EFFECTIVE gamma and R, i.e. the values the thermo file's own digits define): SDT mean gas, M_i 1.556, eps 4; air
gamma 1.4, M_i 1.5, eps 6.

WHY Ne = 2000. GENO writes the straightening contours as polylines with one vertex per exit column (Ne); at its
default Ne = 100 a vertex turns the wall by up to 6.3e-3 rad (SDT) / 8.3e-3 rad (air), and the model, refined past
the vertex spacing, resolves every vertex as a corner (a wave of strength = the turning): measured with those walls
(logs/t05_geno_migdal_ne100_walls.log), the exit deviations grow with refinement to |d theta| 5.9e-3 rad and the
conservation closures stop converging at (560,121). The turning per vertex scales as 1/Ne (6.3e-3, 6.3e-4,
3.2e-4 rad at Ne 100, 1000, 2000, measured), so the marched walls are GENO's at Ne = 2000.

What must hold if both codes solve the Euler equations correctly:
  G1 wall pressure on both walls: |p_model - p_GENO| -> GENO's own error as the model is refined. Error model:
     |p_model(h) - p_GENO| <= |p_model(h) - p_exact| + |p_GENO - p_exact|. The model term is bounded by
     2|p_model(h) - p_model(2h)| (Richardson, any observed order >= 0.6); the GENO term is MEASURED on GENO's own
     ladder (NI, da, Ne) = (501, 0.02, 500) -> (1001, 0.01, 1000) -> (1001, 0.01, 2000): e_G = the sum of the two
     changes (a bound on the fine level's error for any GENO order >= 1). Norm: mean over the model's wall points,
     in units of p_i.
  G2 exit (the model's last column lies in the uniform region downstream of the Mach lines E_F-F and E_F-G):
     M = M_e and theta = 0. Error model: a wall-angle error d(theta_w) sends a wave of strength d(theta_w), so the
     exact flow on GENO's walls deviates by |d theta| <= d(theta_w) and |dM| <= d(theta_w) / nu'(M_e) (simple-wave
     relation d(nu) = d(theta)); d(theta_w) = the largest of GENO's wall-angle changes along its ladder and the
     marched wall's turning per vertex.
  G3 vacuum thrust (the carrier's functional F_in - push(plug) + push(shroud)) -> the 1-D thrust of a perfect
     nozzle with GENO's exit annulus: F_1D = mdot V_e + p_e A_e (momentum theorem over a control surface closed in
     the uniform exit region). Error model: 2|T(h) - T(2h)| + (d theta_w)^2 (a non-uniform exit loses thrust at
     second order: the uniform axial exit is the stationary point of the exit momentum flux at fixed mass and area).
  G4 conservation on the march's own exit surface. After the lip F the march computes only the region below F's C-
     (the top row of every later column lies on it; a1_plug_march docstring, SHROUD), so the surface that closes the
     control volume is the last column (from the plug end G up to F's C-) PLUS F's C- back up to F. Through it:
     mass = inlet mass (G4a) and axial momentum flux = F_in - push(plug) + push(shroud) (G4b, the momentum theorem
     in vacuum). Both hold exactly for the exact solution; band 2|change|.
  G5 the start line's stream thrust and mass vs exact (the table's own p error, T01: <= 4.1e-7).
  G6 every model march certified (Newton certificate <= 1).
Model ladder (K plug stations, N start rows) = (70,16) (140,31) (280,61) (560,121); stations by the carrier's rule
(a1_shroud_twin.stations_from on GENO's dense walls), wedge rule of the carrier (a1_twowall.TwoWall.__init__).
"""
import json
import os
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import exact                                       # noqa: E402
import geno_io as GI                               # noqa: E402
import numpy as np                                 # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import a1_ideal_march_jax as A1                    # noqa: E402
import a1_plug_march as PM                         # noqa: E402
import a1_shroud_twin as ST                        # noqa: E402
import a1_twowall as T                             # noqa: E402

R = rv.Report("t05_geno_migdal")
CASES = ["migdal_sdt_eps4", "migdal_air_eps6"]
GRIDS = [(70, 16), (140, 31), (280, 61), (560, 121)]
LEVELS = [("c", "_ni501_ne500"), ("m", "_ni1001_ne1000"), ("f", "_ni1001_ne2000")]   # coarse, medium, fine (the walls marched)
o2 = lambda a, b: np.log(abs(a) / abs(b)) / np.log(2.0)      # noqa: E731
summary, plots = {}, {}

for case in CASES:
    d = os.path.join(rv.RV, "geno", case)
    c = json.load(open(os.path.join(d, "case.json")))
    th = c["thermo"]
    g_, R_, T0, P0 = th["gamma"], th["R"], c["gas"][2], c["gas"][3]
    G = exact.PerfectGas(g_, R_, T0, P0)
    T_tab = [0.2 * T0 / (1 + 0.5 * (g_ - 1) * 4.5 ** 2), 1.02 * T0]
    tab, ta = rv.model_table(g_, R_, T0, P0, T_tab)
    Mi = c["Mi"]
    pi_ = float(G.p(Mi))
    # ------------------------------------------------------------- GENO ladder
    gl = {}
    for lab, suf in LEVELS:
        dd = d + suf
        if not os.path.exists(os.path.join(dd, "performance.dat")):
            R.note("%s: GENO level %s missing (%s)" % (case, lab, dd))
            continue
        gl[lab] = GI.migdal_walls(dd)
    ref = gl["f"]
    up, lo = ("cm", "cp") if ref["cm"][1][0] > ref["cp"][1][0] else ("cp", "cm")
    shroud_g = np.stack(ref[up], 1)
    plug_g = np.stack(ref[lo], 1)
    plug_d, shroud_d = ST.dedup(plug_g[:, :2]), ST.dedup(shroud_g[:, :2])
    x0 = float(plug_d[0, 0])
    y_l, y_u = float(plug_d[0, 1]), float(shroud_d[0, 1])
    A_i = np.pi * (y_u ** 2 - y_l ** 2)
    eps_geo = (shroud_d[-1, 1] ** 2 - plug_d[-1, 1] ** 2) / (y_u ** 2 - y_l ** 2)
    Me = G.M_of_area(eps_geo * float(G.area_ratio(Mi)))
    q_i = float(G.q(Mi))
    mdot_ex = float(G.rho(Mi)) * q_i * A_i
    F_in_ex = (float(G.rho(Mi)) * q_i * q_i + pi_) * A_i
    A_e = eps_geo * A_i
    F_1D = mdot_ex * float(G.q(Me)) + float(G.p(Me)) * A_e
    R.note("%s: gamma %.10f R %.6f; walls (NI 1001): plug %d pts x %.4f..%.4f y %.4f..%.4f, shroud %d pts x ..%.4f"
           " y ..%.4f; exit area ratio of the walls %.8f (input %.1f) -> M_e %.6f (GENO %.6f); F_1D %.8e"
           % (case, g_, R_, len(plug_d), plug_d[0, 0], plug_d[-1, 0], plug_d[0, 1], plug_d[-1, 1], len(shroud_d),
              shroud_d[-1, 0], shroud_d[-1, 1], eps_geo, c["eps"], Me, ref["perf"]["Me"], F_1D))
    # GENO's own convergence: wall pressure, wall angle, thrust
    xs_cmp = {k: np.linspace(w[0, 0], w[-1, 0], 4001)[1:-1] for k, w in (("plug", plug_g), ("shroud", shroud_g))}

    def geno_on(lev, key):
        w = gl[lev][lo if key == "plug" else up]
        o = np.argsort(w[0])
        x, y, p = w[0][o], w[1][o], w[2][o]
        keep = np.r_[True, np.diff(x) > 0]
        x, y, p = x[keep], y[keep], p[keep]
        xq = xs_cmp[key]
        th_w = np.arctan(np.gradient(y, x))
        return np.interp(xq, x, p), np.interp(xq, x, th_w), np.interp(xq, x, y)
    eG, gth, gy, gF = {}, {}, {}, {}
    for lev in gl:
        gF[lev] = gl[lev]["perf"]["F"]
    turn = {}
    for key in ("plug", "shroud"):
        vals = {lev: geno_on(lev, key) for lev in gl}
        e_cm = float(np.mean(np.abs(vals["m"][0] - vals["c"][0]))) / pi_      # NI and Ne doubled
        e_mf = float(np.mean(np.abs(vals["f"][0] - vals["m"][0]))) / pi_      # Ne doubled
        eG[key] = e_cm + e_mf
        w = gl["f"][lo if key == "plug" else up]
        o = np.argsort(w[0]); xw, yw = w[0][o], w[1][o]
        k_ = np.r_[True, np.diff(xw) > 0]; xw, yw = xw[k_], yw[k_]
        turn[key] = float(np.max(np.abs(np.diff(np.arctan(np.diff(yw) / np.diff(xw))))))
        gth[key] = max(float(np.max(np.abs(vals["m"][1] - vals["c"][1]))), float(np.max(np.abs(vals["f"][1] - vals["m"][1]))),
                       turn[key])
        gy[key] = max(float(np.max(np.abs(vals["m"][2] - vals["c"][2]))), float(np.max(np.abs(vals["f"][2] - vals["m"][2]))))
        R.note("%s GENO ladder %s wall p (mean, units of p_i): (501,500)->(1001,1000) %.3e, (1001,1000)->(1001,2000) %.3e;"
               " wall angle: max change %.3e rad, max turning per vertex of the marched wall %.3e rad; wall y max change %.3e"
               % (case, key, e_cm, e_mf, gth[key], turn[key], gy[key]))
    R.note("%s GENO thrust vs F_1D: %s" % (case, ", ".join("%s %+.3e" % (lev, gF[lev] / F_1D - 1.0) for lev in gF)))
    R.note("%s GENO mdot vs exact: %+.3e" % (case, ref["perf"]["mdot"] / mdot_ex - 1.0))
    dth_w = max(gth.values())
    nu_p = float((G.nu(Me * (1 + 1e-6)) - G.nu(Me * (1 - 1e-6))) / (2e-6 * Me))
    # ------------------------------------------------------------- model ladder
    res = []
    for K, N in GRIDS:
        sx, sy, ssl = ST.stations_from(plug_d, K)
        Ks = max(8, int(K * (shroud_d[-1, 0] - shroud_d[0, 0]) / (plug_d[-1, 0] - plug_d[0, 0])))
        xs, ys_, ss_ = ST.stations_from(shroud_d, Ks)
        xs, ys_, ss_ = np.r_[x0, xs], np.r_[y_u, ys_], np.r_[0.0, ss_]
        yline = np.linspace(y_l, y_u, N)
        start = (x0, yline, np.full(N, q_i), np.zeros(N))
        dy_row = (y_u - y_l) / (N - 1)
        m_w = max(1, int(round(ST.GN["wedge_rows_per_station"] * (sx[0] - x0) * np.tan(np.arcsin(1.0 / Mi)) / dy_row)))
        out, S = PM.plug_march((np.asarray(sx), np.asarray(sy), np.asarray(ssl)), start, q_i, tab, 1.0,
                               shroud=(xs, ys_, ss_), wedge_every=m_w, fast=True)
        Wp, Ws = np.asarray(out["wall"]), np.asarray(out["shroud"])
        e = {}
        for key, Wk, Gw in (("plug", Wp, plug_g), ("shroud", Ws, shroud_g)):
            pm_ = np.asarray(A1.state_q(jnp.asarray(np.hypot(Wk[:, 2], Wk[:, 3])), ta)[1])
            o_ = np.argsort(Gw[:, 0])
            pg_ = np.interp(Wk[:, 0], Gw[o_, 0], Gw[o_, 2])
            e[key] = (pm_ - pg_) / pi_
        lc = np.asarray(out["last_col"])
        qlc = np.hypot(lc[:, 2], lc[:, 3])
        Mlc = np.asarray(A1.state_q(jnp.asarray(qlc), ta)[5])
        thlc = np.arctan2(lc[:, 3], lc[:, 2])
        # the exit surface: the last column (bottom -> top) then F's C- (the tops of the later columns) back to F
        mk, mpts = out["mesh_keys"], np.asarray(out["mesh_pts"])
        Gm = {k: mpts[n] for n, k in enumerate(mk)}
        i_last = max(k[1] for k in mk)
        jtop = {}
        for (j, ii) in mk:
            jtop[ii] = max(j, jtop.get(ii, 0))
        surf = np.concatenate([lc] + [Gm[(jtop[i], i)][None, :4] for i in range(i_last - 1, int(out["lip_col"]) - 1, -1)],
                              axis=0)
        md, mom = PM.col_fluxes(surf, ta, 0.0, 1.0)
        col0 = np.stack([np.full(N, x0), yline, start[2], start[3]], 1)
        md0, F_in = PM.col_fluxes(col0, ta, 0.0, 1.0)
        stub = types.SimpleNamespace(x0=x0, sep="")
        ctx = dict(q_i=q_i, ta=ta)
        Tm = F_in - float(T.TwoWall._gauge_push(stub, jnp.asarray(Wp), y_l, ctx, 0.0)) \
            + float(T.TwoWall._gauge_push(stub, jnp.asarray(Ws), y_u, ctx, 0.0))
        r = dict(K=K, N=N, ep1=float(np.mean(np.abs(e["plug"]))), es1=float(np.mean(np.abs(e["shroud"]))),
                 ep=float(np.max(np.abs(e["plug"]))), es=float(np.max(np.abs(e["shroud"]))),
                 dM=float(np.max(np.abs(Mlc - Me))), dth=float(np.max(np.abs(thlc))), mass=md / mdot_ex - 1.0,
                 mass0=md0 / mdot_ex - 1.0, T=Tm, eT=Tm / F_1D - 1.0, Fin=F_in / F_in_ex - 1.0,
                 mom=(mom - Tm) / F_1D, F_top=surf[-1, :2].tolist(),
                 cert=float(out["cert_worst"]), lip=out["lip_col"], ncell=int(out["cert_n"]), x_end=float(Wp[-1, 0]),
                 n_last=int(len(lc)), wall=(Wp, Ws, e), lastcol=(lc[:, 1], Mlc, thlc))
        res.append(r)
        R.note("%s K %3d N %3d (%6d cells, wedge %d, lip col %s, last col %d pts at x %.4f): wall p vs GENO mean plug "
               "%.2e shroud %.2e (max %.2e %.2e) | exit max|M-Me| %.2e max|theta| %.2e rad | mass %+.2e | thrust vs 1-D "
               "%+.3e | exit momentum - thrust %+.2e | cert %.2e"
               % (case, K, N, r["ncell"], m_w, r["lip"], r["n_last"], r["x_end"], r["ep1"], r["es1"], r["ep"],
                  r["es"], r["dM"], r["dth"], r["mass"], r["eT"], r["mom"], r["cert"]))
    f, cc = res[-1], res[-2]
    for k in range(1, len(res)):
        a, b = res[k - 1], res[k]
        R.note("%s orders %d->%d: wall vs GENO plug %.2f shroud %.2f | exit M %.2f theta %.2f | mass %.2f | thrust %.2f"
               " | momentum closure %.2f"
               % (case, k - 1, k, o2(a["ep1"], b["ep1"]), o2(a["es1"], b["es1"]), o2(a["dM"], b["dM"]),
                  o2(a["dth"], b["dth"]), o2(a["mass"], b["mass"]), o2(a["eT"], b["eT"]), o2(a["mom"], b["mom"])))
    # Richardson limit of the thrust from the two finest grids (observed order between the last three)
    p_T = o2(res[-3]["T"] - res[-2]["T"], res[-2]["T"] - res[-1]["T"])
    T_inf = f["T"] + (f["T"] - cc["T"]) / (2.0 ** p_T - 1.0) if np.isfinite(p_T) and p_T > 0.5 else f["T"]
    R.note("%s thrust: observed order %.2f, Richardson limit %.10e = F_1D x (1 %+.3e); GENO (fine) F = F_1D x (1 %+.3e)"
           % (case, p_T, T_inf, T_inf / F_1D - 1.0, gF["f"] / F_1D - 1.0))
    for key, lab in (("ep1", "plug"), ("es1", "shroud")):
        tol = 2.0 * abs(f[key] - cc[key]) + eG[lab]
        R.check("%s G1 %s wall p: mean |model - GENO| / p_i (finest) <= 2|change| + GENO's own ladder change"
                % (case, lab), f[key], tol)
    R.check("%s G2 exit max |M - M_e| (finest) <= 2|change| + d(theta_w)/nu'(M_e)" % case, f["dM"],
            2.0 * abs(f["dM"] - cc["dM"]) + dth_w / nu_p)
    R.check("%s G2 exit max |theta| rad (finest) <= 2|change| + d(theta_w)" % case, f["dth"],
            2.0 * abs(f["dth"] - cc["dth"]) + dth_w)
    R.check("%s G3 thrust vs F_1D (finest) <= 2|change| + d(theta_w)^2" % case, f["eT"],
            2.0 * abs(f["eT"] - cc["eT"]) + dth_w ** 2)
    R.check("%s G4a mass through the exit surface vs inlet (finest), band 2|change|" % case, f["mass"],
            2.0 * abs(f["mass"] - cc["mass"]) + 1e-12)
    R.check("%s G4b momentum theorem: (exit flux - wall thrust) / F_1D (finest), band 2|change|" % case, f["mom"],
            2.0 * abs(f["mom"] - cc["mom"]) + 1e-12)
    R.check("%s G5 start-line stream thrust vs exact (table p error <= 4.1e-7)" % case, f["Fin"], 4.1e-7)
    R.check("%s G5 start-line mass vs exact (table rho error <= 4.1e-7)" % case, f["mass0"], 4.1e-7)
    R.check("%s G6 certificates <= 1 over the ladder" % case, max(r["cert"] for r in res), 1.0)
    if case == CASES[0]:
        # REJECTOR (R5): the G1 plug check with the model's gas gamma 1 % too high (same walls, inflow speed, grids)
        tab_x, ta_x = rv.model_table(1.01 * g_, R_, T0, P0, T_tab)
        ex1 = []
        for K, N in GRIDS[-2:]:
            sx, sy, ssl = ST.stations_from(plug_d, K)
            Ks = max(8, int(K * (shroud_d[-1, 0] - shroud_d[0, 0]) / (plug_d[-1, 0] - plug_d[0, 0])))
            xs, ys_, ss_ = ST.stations_from(shroud_d, Ks)
            xs, ys_, ss_ = np.r_[x0, xs], np.r_[y_u, ys_], np.r_[0.0, ss_]
            yline = np.linspace(y_l, y_u, N)
            start = (x0, yline, np.full(N, q_i), np.zeros(N))
            dy_row = (y_u - y_l) / (N - 1)
            m_w = max(1, int(round(ST.GN["wedge_rows_per_station"] * (sx[0] - x0) * np.tan(np.arcsin(1.0 / Mi)) / dy_row)))
            out_x, _ = PM.plug_march((np.asarray(sx), np.asarray(sy), np.asarray(ssl)), start, q_i, tab_x, 1.0,
                                     shroud=(xs, ys_, ss_), wedge_every=m_w, fast=True)
            Wx = np.asarray(out_x["wall"])
            pm_x = np.asarray(A1.state_q(jnp.asarray(np.hypot(Wx[:, 2], Wx[:, 3])), ta_x)[1])
            o_ = np.argsort(plug_g[:, 0])
            ex1.append(float(np.mean(np.abs(pm_x - np.interp(Wx[:, 0], plug_g[o_, 0], plug_g[o_, 2])))) / pi_)
        R.note("%s rejector: gamma x1.01 -> plug wall p vs GENO mean %.3e (finest), %.3e (previous)" % (case, ex1[-1], ex1[-2]))
        R.reject("%s G1 plug wall p vs GENO (finest), model's gamma x1.01" % case, ex1[-1],
                 2.0 * abs(ex1[-1] - ex1[-2]) + eG["plug"])
    summary[case] = dict(turn_per_vertex=turn, model=[{k: v for k, v in r.items() if k not in ("wall", "lastcol")} for r in res],
                         geno_wall_p_change=eG, geno_wall_angle_change=gth, geno_wall_y_change=gy,
                         geno_F_over_F1D={k: v / F_1D - 1.0 for k, v in gF.items()}, F_1D=F_1D, T_inf=T_inf,
                         p_T=p_T, Me=Me, eps_geo=eps_geo, dth_w=dth_w)
    plots[case] = (res, plug_g, shroud_g, G, Mi, Me, F_1D, gF, eG, ta)

import matplotlib                                   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                     # noqa: E402
fig, ax = plt.subplots(2, 3, figsize=(17, 8.5))
for row, case in enumerate(CASES):
    res, plug_g, shroud_g, G, Mi, Me, F_1D, gF, eG, ta = plots[case]
    pi_ = float(G.p(Mi))
    a = ax[row, 0]
    a.plot(plug_g[:, 0], plug_g[:, 2] / pi_, "k-", lw=2, label="GENO inner wall (plug)")
    a.plot(shroud_g[:, 0], shroud_g[:, 2] / pi_, "k--", lw=2, label="GENO outer wall (shroud)")
    Wp, Ws, e = res[-1]["wall"]
    for Wk, lab in ((Wp, "model plug"), (Ws, "model shroud")):
        pm_ = np.asarray(A1.state_q(jnp.asarray(np.hypot(Wk[:, 2], Wk[:, 3])), ta)[1])
        a.plot(Wk[:, 0], pm_ / pi_, "-", lw=1.0, label=lab + " (K %d)" % res[-1]["K"])
    a.set_title("%s: wall pressure" % case); a.set_xlabel("x"); a.set_ylabel("p / p_i"); a.legend(fontsize=7)
    a.grid(alpha=0.3)
    a = ax[row, 1]
    for r in res:
        Wp, Ws, e = r["wall"]
        a.plot(Wp[:, 0], e["plug"], lw=0.8, label="plug K %d" % r["K"])
    a.set_title("(p_model - p_GENO) / p_i on the inner wall"); a.set_xlabel("x"); a.legend(fontsize=7)
    a.grid(alpha=0.3)
    a = ax[row, 2]
    h = np.array([1.0 / r["K"] for r in res])
    for key, lab in (("ep1", "wall p vs GENO (inner, mean)"), ("es1", "wall p vs GENO (outer, mean)"),
                     ("dM", "exit max|M - Me|"), ("eT", "thrust vs F_1D"), ("mass", "mass")):
        a.loglog(h, [abs(r[key]) for r in res], "o-", label=lab)
    a.axhline(eG["plug"], color="C0", ls=":", lw=1, label="GENO ladder change (inner)")
    a.axhline(max(abs(gF["f"] / F_1D - 1.0), 1e-12), color="k", ls=":", lw=1, label="|GENO F / F_1D - 1|")
    a.loglog(h, res[0]["ep1"] * (h / h[0]) ** 2, "k--", lw=0.8, label="slope 2")
    a.set_xlabel("1/K"); a.legend(fontsize=6); a.grid(alpha=0.3, which="both"); a.set_title("convergence")
rv.savefig(fig, "05_geno_migdal.png")
sys.exit(R.save(summary))
