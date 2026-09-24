#!/usr/bin/env python3
"""THE THROAT POSING of the plug optimiser [F3/A1, X-HMPH] (2026-09-23,
worktree tri-experiment; owner: "procedi con l'implementazione, fintanto
che non riusciamo a cominciare dallo stesso punto e' infattibile ottenere
il loro profilo").

The record's walks start from a PLANAR corner fan read on a vertical cut
0.378 in after the lip: the wall there is pinned at -26.65 deg and 6.037 in
by the fan and the imposed mass, while Humphreys' throat also expands the
flow from the PLUG side on the prescribed 0.5-in arc A-T (-36.25 ->
-48.25 deg) and puts their wall at -43.47 deg and 5.74 in at the same
abscissa (S34 G-1, G-11). No walk from our cut can land on their contour.
This posing starts the optimiser where THEY start:

  - the flow: THEIR throat A-E through the annular kernel [X-ANKR], the
    start 'come loro' (the initial-value triangle on A-E, a1_ivl_triangle,
    HMPH_IVL=tri), the lip corner fan in the kernel's field and the
    rotated-frame cells [X-FRMR] -- the chain of stage kernel, copied line
    for line (gate TP-1: bit-identical J on their wall);
  - the wall: THEIR arc from A to T, fixed (design-independent, as in the
    paper: T is where the optimised contour begins), then the DESIGN from
    T to D, anchored at T with the arc's end angle (C^1, no corner at T,
    their p. 1585), in the driver's y or angle coordinates, D at the fixed
    axial length T -> D of the paper (their last Table 2 row);
  - the stations: along the arc the kernel stage's own ladder; after T the
    same ladder's stations read on their wall and FROZEN AS RECORD-FRAME
    ABSCISSAE, so every design ends exactly at x_D; their frame abscissae
    then move with the design (a1_plug_march x_traced: the replay is
    differentiable in them);
  - the functional: J = F_in (the start column, fixed) + the wall push in
    the record frame + the base (the driver's BASE_MODEL, PB_FROZEN
    honoured), the formula of stage kernel's thrust.

The driver (a1_plug_spline_opt) routes march_record / J_replay /
margin_replay to this posing when the case dict carries "throat"; the
TR-SQP itself is unchanged. Environment BEFORE importing the driver (its
constants are read at import time -- the S32 import-order trap).

Stages (TPOSE_STAGE): "gates" (TP-1..TP-4), "walk" (the TR-SQP), "tslide"
(TS-1..TS-3, the gates of TPOSE_THT_DEG), "fig4" (their Fig. 4 contours,
F4-1..F4-4); run from validation/ with the
a1 venv, e.g.
  HMPH_CASE=opt HMPH_ZCUT=0.12 ANK_ETA=8 HMPH_K=160 HMPH_N=41 \\
  TPOSE_STAGE=gates python a1_throat_posing.py
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import a1_ideal_march_jax as A1                                   # noqa: E402
import jax                                                        # noqa: E402
import jax.numpy as jnp                                           # noqa: E402
import a1_humphreys_twin as HT                                    # noqa: E402
import base_pressure as BP                                        # noqa: E402

IN = HT.IN


def driver():
    """The driver module, imported only after the caller posed its
    environment (PSPL_*, A1_BASE_MODEL): its constants are read at import."""
    os.environ.setdefault("PSPL_M", "6")
    os.environ.setdefault("A1_BASE_MODEL", "veen")
    import a1_plug_spline_opt as P
    P.PA = HT.PA
    return P


class ThroatPosing:
    """Their throat, the start 'come loro', their arc A-T; the design from
    T to D. See the module docstring."""

    def __init__(self, verbose=True):
        import a1_annular_kernel as AK
        import a1_frame_march as FM
        import a1_plug_march as PM
        import a1_ivl_triangle as IVT
        from a1_freejet_unit import q_at_pa
        self.FM, self.PM = FM, PM
        say = HT.say if verbose else (lambda m: None)
        t0 = time.time()
        w = HT.build_world(HT.R_OPT)
        S, ta = w["S"], w["ta"]
        self.w, self.S, self.ta = w, S, ta
        KD = FM.CASES["kernel_defaults"]
        # the knobs of stage kernel, same names, same defaults
        z_cut = float(os.environ.get("HMPH_ZCUT", 0.25))
        K = int(os.environ.get("HMPH_K", KD["K"]))
        N = int(os.environ.get("HMPH_N", KD["N"]))
        n_rays = int(os.environ.get("HMPH_NRAYS", KD["n_rays"]))
        n_pts = int(os.environ.get("HMPH_NPTS", KD["n_pts"]))
        gam, eta = HT.GAMMA, float(os.environ.get("ANK_ETA", 2.0))
        self.K, self.N, self.z_cut, self.eta = K, N, z_cut, eta

        # ---- their throat and their arc (stage kernel, line for line) --
        # the reference optimum (TPOSE_TABLE): their Table 2 (the Veen base,
        # the record) or Table 4 (their optimum for the Panov-Shvets base,
        # Eq. (38), same throat, T at -45.75 deg; its last two rows recovered
        # from the paper's text, _table4_recovered_rows)
        self.table_name = os.environ.get("TPOSE_TABLE", "table2")
        if self.table_name == "table2":
            tab = np.array(HT.TABLES["table2_optimum_lip7.55_inj-34"])
        elif self.table_name == "table4":
            tab = np.array(HT.TABLES["table4_optimum_panov_shvets_base"]
                           + HT.TABLES["_table4_recovered_rows"], float)
            tab = tab[np.argsort(tab[:, 0])]
        else:
            raise ValueError("TPOSE_TABLE %s" % self.table_name)
        self.tab = tab
        x, y, th = tab[:, 0], tab[:, 1], np.radians(tab[:, 2])
        prec = HT.TABLES["_table_precision_in"]
        ds = np.hypot(np.diff(x), np.diff(y))
        rho_k = ds / np.abs(np.diff(th))
        band_rho = A1.K_RICH * (2.0 * prec / ds[0])
        n_arc = 1
        while (n_arc < len(rho_k)
               and abs(rho_k[n_arc] / rho_k[0] - 1.0) <= band_rho):
            n_arc += 1
        rho = float(np.mean(rho_k[:n_arc]))
        A, E = np.array([x[0], y[0]]), np.array([0.0, HT.R_OPT / IN])
        h = float(np.hypot(*(E - A)))
        R_mean = HT.TABLES["_throat_mean_radius_in"]
        rc_plug = rho
        rc_cowl = 1.0 / (2.0 / R_mean - 1.0 / rho)
        thA, thT = float(th[0]), float(th[n_arc])
        C = A + rho * np.array([np.sin(thA), -np.cos(thA)])
        n_arc_pts = max(2, int(FM.CASES["dense_wall_points"]
                               * (float(x[n_arc]) - float(x[0]))
                               / (float(x[-1]) - float(x[0]))))
        tt = np.linspace(thA, thT, n_arc_pts)
        xT, yT, xD = float(x[n_arc]), float(y[n_arc]), float(x[-1])
        # T SLIDING ON THEIR ARC (TPOSE_THT_DEG, the parametric study of the
        # plug-side expansion, 2026-09-23 evening; unset = their T, the
        # record). The arc keeps the record's angular step, so its points up
        # to the cut -- hence the start 'come loro' -- are bit-identical, and
        # ends exactly at theta_T on the circle; D follows T at their length
        # T -> D; after T the layout wall (it only places the stations) is
        # THEIR contour translated to the new T.
        self.T_moved = os.environ.get("TPOSE_THT_DEG") is not None
        dxT = dyT = 0.0
        if self.T_moved:
            thT = float(np.radians(float(os.environ["TPOSE_THT_DEG"])))
            step = (float(th[n_arc]) - thA) / (n_arc_pts - 1)
            # guards in ulps (their theta_T sits on a record point up to
            # round-off; either branch then yields the record's points + T)
            r_T = (thT - thA) / step
            k_max = int(np.floor(r_T + 8 * np.spacing(r_T)))
            tt = np.arange(k_max + 1) * step + thA
            if abs(tt[-1] - thT) > 8 * np.spacing(abs(thT)):
                tt = np.concatenate([tt, [thT]])
            else:
                tt[-1] = thT
        arc_xy = C[None, :] + rho * np.stack([-np.sin(tt), np.cos(tt)], 1)
        if self.T_moved:
            dxT, dyT = float(arc_xy[-1, 0]) - xT, float(arc_xy[-1, 1]) - yT
            xT, yT, xD = xT + dxT, yT + dyT, xD + dxT
        xd = np.linspace(xT, xD, FM.CASES["dense_wall_points"])[1:]
        yd = HT.read_table(xd - dxT, tab, mode="hermite") + dyT
        Xw = np.concatenate([arc_xy[:, 0], xd]) * IN * S
        Yw = np.concatenate([arc_xy[:, 1], yd]) * IN * S
        self.their_dense_in = (xd, yd)

        # ---- the throat frame ------------------------------------------
        thf = np.radians(HT.TH_I_OPT)
        Xm, Ym = 0.5 * (A + E) * IN * S
        hh = 0.5 * h * IN * S
        d_fr = 2.0 * hh
        xw, yw, _, _ = FM.to_frame(Xw, Yw, np.zeros_like(Xw), np.zeros_like(Xw),
                                   thf, Xm, Ym)
        if np.any(np.diff(xw) <= 0.0):
            raise ValueError("their wall is not single-valued in the throat frame")
        sw = np.gradient(yw, xw)
        xE, yE_, _, _ = FM.to_frame(E[0] * IN * S, E[1] * IN * S, 0.0, 0.0, thf, Xm, Ym)
        self.thf, self.Xm, self.Ym, self.hh = thf, float(Xm), float(Ym), hh

        # ---- the kernel on their throat ---------------------------------
        slope_A = float(np.tan(thA - thf))
        Pk = AK.throat_params(float(y[0]) * IN, h * IN, -HT.TH_I_OPT, rc_plug * IN,
                              rc_cowl * IN, eta, gam, slope_in=slope_A)
        grid, fields, _ = AK.solve_kernel(Pk["y_i"], Pk["g1"], Pk["g2"], Pk["h1"],
                                          Pk["h2"], Pk["b1"], gam, eta)
        eps, Kk = Pk["eps"], Pk["K"]
        xT_fr = float(FM.to_frame(xT * IN * S, yT * IN * S,
                                  0.0, 0.0, thf, Xm, Ym)[0])

        def kernel_uv(xp, yp):
            z = (np.asarray(xp, float) / d_fr) / (Kk * eps ** 0.5)
            yk = Pk["y_i"] + (np.asarray(yp, float) + hh) / d_fr
            u, v = AK.series_uv(grid, fields, eps, gam, z, yk)
            return u * w["as_"], v * w["as_"]

        x_cut = z_cut * Kk * eps ** 0.5 * d_fr
        yw0, sw0 = float(np.interp(x_cut, xw, yw)), float(np.interp(x_cut, xw, sw))

        # ---- the lip corner and the start 'come loro' -------------------
        q_E = q_at_pa(HT.PA, ta, w["as_"])
        u_l, v_l = kernel_uv(xE, yE_)
        q_l, th_l = float(np.hypot(u_l, v_l)), float(np.arctan2(v_l, u_l))
        CF = FM.corner_fan(w, kernel_uv, (float(xE), float(yE_)), q_l, th_l,
                           x_cut, thf, Ym, n_rays, n_pts, q_E)
        th_e = CF["th_E"]
        crs = [c_ for c_ in CF["cross"] if c_ is not None]
        y_lead0 = float(crs[0][1])
        y_edge0 = float(yE_) + (x_cut - float(xE)) * np.tan(th_e)
        nA = max(5, int(round(N * (y_lead0 - yw0) / (y_edge0 - yw0))))
        ts = IVT.tri_start(w, kernel_uv, (float(xE), float(yE_)), q_l, th_l,
                           float(x_cut), yw0, sw0, nA + 1, n_pts, n_rays, q_E,
                           th_e, thf, Ym)
        col = ts["col"]
        xs_, ys, us, vs = col[:, 0], col[:, 1], col[:, 2], col[:, 3]
        if not np.all(np.diff(ys) > 0.0):
            raise ValueError("tri column rows not ordered")
        self.start = (xs_, ys, us, vs)
        X0r, Y0r, U0r, V0r = FM.to_record(xs_, ys, us, vs, thf, Xm, Ym)
        md_in, F_in = PM.col_fluxes(np.stack([X0r, Y0r, U0r, V0r], 1), ta, HT.PA, 1.0)
        self.md_in, self.F_in, self.q_E = abs(float(md_in)), float(F_in), q_E
        self.cert_start = max(CF["cert"], ts["cert_tri"], ts["cert_fan"], ts["cert_fj"])
        self.cells = FM.make_cells_rot(1.0, thf, Ym)

        # ---- the stations: the kernel stage's ladder on their wall -------
        ds0 = float(os.environ.get("HMPH_DS0", FM.CASES["station_clustering"][0])) * hh
        grow = float(os.environ.get("HMPH_GROW", FM.CASES["station_clustering"][1]))
        x_start = float(x_cut)
        ds_max = (xw[-1] - x_start) / K
        xs, dsn = [x_start], ds0
        while xs[-1] + dsn < xw[-1]:
            xs.append(xs[-1] + dsn)
            dsn = min(ds_max, dsn * grow)
        xq = np.array(xs[1:] + [float(xw[-1])])
        yq, sq = np.interp(xq, xw, yw), np.interp(xq, xw, sw)
        self.ref_stations = (xq, yq, sq)            # stage kernel's, their wall
        arc = xq <= xT_fr
        self.xq_arc, self.yq_arc, self.sq_arc = xq[arc], yq[arc], sq[arc]
        if self.T_moved:
            # the arc's stations ON the circle: at a moved T the layout wall
            # has a corner, and its interpolated slope must not reach the
            # wall's boundary data
            ct_, st_ = np.cos(thf), np.sin(thf)
            Cm, Rm = C * IN * S, rho * IN * S
            c0 = (Cm[0] - Xm) * ct_ + (Cm[1] - Ym) * st_
            c1 = -(Cm[0] - Xm) * st_ + (Cm[1] - Ym) * ct_
            tq = thf + np.arcsin((c0 - self.xq_arc) / Rm)
            self.yq_arc = c1 + Rm * np.cos(tq - thf)
            self.sq_arc = np.tan(tq - thf)
        # after T: frozen as RECORD-FRAME abscissae (D exactly at x_D)
        Xs, _, _, _ = FM.to_record(xq[~arc], yq[~arc], 0.0 * xq[~arc], 0.0 * xq[~arc],
                                   thf, Xm, Ym)
        Xs = np.asarray(Xs, float)
        Xs[-1] = xD * IN * S
        self.Xs = Xs
        # the anchor T and the knots: uniform in x from T to D, the last AT D
        self.x_T, self.y_T = xT * IN * S, yT * IN * S
        self.s_T = float(np.tan(thT))
        self.x_D = xD * IN * S
        M = int(os.environ["PSPL_M"]) if "PSPL_M" in os.environ else 6
        self.xk = self.x_T + (self.x_D - self.x_T) * np.arange(1, M + 1) / M
        self.c = dict(throat=self, xk=self.xk, x0=self.x_T, yw0=self.y_T,
                      slope0=self.s_T, F_in=self.F_in, md_in=self.md_in)
        self.geom = dict(A_in=A.tolist(), E_in=E.tolist(), h_in=h, rho_arc_in=rho,
                         n_arc=n_arc, T_in=[xT, yT], thT_deg=float(np.degrees(thT)),
                         T_moved=self.T_moved, dT_in=[dxT, dyT], C_arc_in=C.tolist(),
                         D_in=[xD, float(y[-1]) + dyT], x_cut_in=x_cut / S / IN,
                         xT_frame_in=xT_fr / S / IN, R_c=Pk["R_c"], eps=eps,
                         n_start_rows=len(ys), n_arc_stations=int(arc.sum()),
                         n_design_stations=int((~arc).sum()))
        say("   throat posing: their arc rho %.4f in (%d rows) A -> T, T at x %.5f in"
            " (x' %.4f in), theta_T %.2f deg; D at x %.4f in (T -> D %.4f in);"
            " kernel R_c %.3f eps %.3f (z_cut %.2f, eta %g); start 'come loro' %d rows,"
            " cert %.3f, %.2f lbm/s, F_in %.0f lbf; stations %d (%d on the arc,"
            " %d designed, frozen in x); %d knots; %.1f s"
            % (rho, n_arc, xT, xT_fr / S / IN, np.degrees(thT), xD, xD - xT,
               Pk["R_c"], eps, z_cut, eta, len(ys), self.cert_start,
               self.md_in / S / S / HT.LBM, self.F_in / S / S / HT.LBF, len(xq),
               int(arc.sum()), int((~arc).sum()), M, time.time() - t0))

    # ------------------------------------------------------------------
    # the wall
    # ------------------------------------------------------------------
    def design_wall(self, W, X):
        """(y, dy/dx) of the design at record-frame abscissae X (traced in W)."""
        P = driver()
        X = np.asarray(X, float)
        if P.PARAM == "y":
            xs = jnp.concatenate([jnp.array([self.x_T]), jnp.asarray(self.xk)])
            ys = jnp.concatenate([jnp.array([self.y_T]), jnp.asarray(W)])
            Mc = P.spline_coeffs(xs, ys, self.s_T)
            return jax.vmap(lambda xx: P.spline_eval(xx, xs, ys, Mc))(jnp.asarray(X))
        return P.angle_wall(W, self.c, X)

    def stations(self, W):
        """(x', y', slope') at every station: the arc's fixed, then the
        design's at the frozen record abscissae, rotated into the frame."""
        yd, sd = self.design_wall(W, self.Xs)
        ct, st = np.cos(self.thf), np.sin(self.thf)
        dX = self.Xs - self.Xm
        xp = dX * ct + (yd - self.Ym) * st
        yp = -dX * st + (yd - self.Ym) * ct
        sp = jnp.tan(jnp.arctan(sd) - self.thf)
        return (jnp.concatenate([jnp.asarray(self.xq_arc), xp]),
                jnp.concatenate([jnp.asarray(self.yq_arc), yp]),
                jnp.concatenate([jnp.asarray(self.sq_arc), sp]))

    # ------------------------------------------------------------------
    # the march and the functional
    # ------------------------------------------------------------------
    def march_record(self, W, margin=None):
        sx, sy, ss = [np.asarray(v, float) for v in self.stations(np.asarray(W, float))]
        if np.any(np.diff(sx) <= 0.0):
            raise ValueError("the design's stations are not increasing in the throat frame")
        return self.PM.plug_march((sx, sy, ss), self.start, self.q_E, self.w["tab"], 1.0,
                                  cells=self.cells, margin=margin, x_traced=True)

    def march_dense(self, stations, margin=None):
        """Stage kernel's own march (x_traced off): the TP-1 reference."""
        return self.PM.plug_march(stations, self.start, self.q_E, self.w["tab"], 1.0,
                                  cells=self.cells, margin=margin)

    def J_parts(self, out):
        """F_in, wall push, base, p_b, record-frame wall; traced-friendly."""
        P = driver()
        wall = out["wall"]
        ct, st = np.cos(self.thf), np.sin(self.thf)
        Y = self.Ym + wall[:, 0] * st + wall[:, 1] * ct
        q = jnp.sqrt(wall[:, 2] ** 2 + wall[:, 3] ** 2)
        stt = A1.state_q(q, self.ta)
        pw = stt[1]
        dY = Y[1:] - Y[:-1]
        wgt = 2.0 * jnp.pi * 0.5 * (Y[1:] + Y[:-1])
        push = jnp.sum((0.5 * (pw[1:] + pw[:-1]) - HT.PA) * wgt * (-dY))
        if not P.BASE_MODEL:
            return dict(F_in=self.F_in, push=push, base=0.0, p_b=None, Y_D=Y[-1])
        # TPOSE_PS_REF=corner: Humphreys' Eq. (38) is written on p_inf, M_inf,
        # and their nomenclature (p. 1581) reads "inf = freestream conditions":
        # for a base, the stream that reaches it -- the state at D -- not the
        # ambient on which base_pressure's member is written (a reading, 09-23)
        p_ref = (pw[-1] if (P.BASE_MODEL == "panov_shvets"
                            and os.environ.get("TPOSE_PS_REF") == "corner") else HT.PA)
        p_b = (BP.p_base(pw[-1], stt[5][-1], stt[4][-1], p_ref, P.BASE_MODEL)
               if P.PB_FROZEN is None else P.PB_FROZEN)
        return dict(F_in=self.F_in, push=push, base=BP.base_term(p_b, Y[-1], HT.PA),
                    p_b=p_b, Y_D=Y[-1], p_D=pw[-1], M_D=stt[5][-1])

    def J_of(self, out):
        jp = self.J_parts(out)
        return jp["F_in"] + jp["push"] + jp["base"]

    def J_replay(self, W, sched):
        S_ = A1.Sched("play", sched.d)
        out, _ = self.PM.plug_march(self.stations(W), self.start, self.q_E, self.w["tab"],
                                    1.0, sched=S_, cells=self.cells, x_traced=True)
        return self.J_of(out)

    def margin_replay(self, W, sched, margin):
        S_ = A1.Sched("play", sched.d)
        out, _ = self.PM.plug_march(self.stations(W), self.start, self.q_E, self.w["tab"],
                                    1.0, sched=S_, cells=self.cells, margin=margin,
                                    x_traced=True)
        return out["margin_ks"] - margin["mu0"]

    # ------------------------------------------------------------------
    # designs
    # ------------------------------------------------------------------
    def W_table(self):
        """THEIR contour at the knots (their table read as they drew it)."""
        P = driver()
        xk_in = self.xk / self.S / IN
        if P.PARAM == "y":
            return HT.read_table(xk_in, self.tab, mode="hermite") * IN * self.S
        xd, yd = self.their_dense_in
        return P.angle_W0(xd * IN * self.S, yd * IN * self.S, self.xk, self.s_T)


# ======================================================================
# stage gates: TP-1 .. TP-4
# ======================================================================
def gates():
    """TP-1 the posing's chain IS stage kernel's (their wall, the same
         stations, x_traced off): J bit-identical to a direct re-run of
         that chain here, and within the march's class of the stage's
         own artifact at the same (K, N);
       TP-2 the design basis holds THEIR contour: the knots' spline
         against their Hermite wall at every design station (the class
         of permanence 0.15 in) and J through the basis against J on
         their dense wall (declared: the basis error);
       TP-3 replay = record at the recorded design (x_traced both ways);
       TP-4 the reverse-AD gradient against the FD ladder along random
         directions, within the ladder's own noise floor."""
    t00 = time.time()
    P = driver()
    HT.say("== [F3] the THROAT POSING of the optimiser [X-HMPH] (stage gates) ==")
    tp = ThroatPosing()
    S = tp.S
    lbf = lambda v: float(v) / S / S / HT.LBF                     # noqa: E731

    # TP-1: the kernel chain on their wall
    t0 = time.time()
    out_ref, sch_ref = tp.march_dense(tp.ref_stations)
    J_ref = float(tp.J_of(out_ref))
    HT.say("   their wall, stage kernel's stations: J %.4f lbf, cert %.3e, %.1f s"
           % (lbf(J_ref), float(out_ref["cert_worst"]), time.time() - t0))
    rec, art = None, None
    for f in (sorted(os.listdir(HT.ART)) if tp.table_name == "table2" and not tp.T_moved else []):
        if (f.startswith("kernel_opt_z%.2f_N%d_" % (tp.z_cut, tp.N)) and f.endswith("_tri_eta%g.json" % tp.eta)
                and "_theirs_" in f):
            r = json.load(open(os.path.join(HT.ART, f)))
            if r.get("K") == len(tp.ref_stations[0]):
                rec, art = r, f
    if rec is not None:
        dJ = abs(lbf(J_ref) / rec["J_lbf"] - 1.0)
        HT.check("TP-1 the posing's chain reproduces stage kernel's artifact %s on their wall"
                 " (J %.4f vs %.4f lbf, rel %.1e)" % (art, lbf(J_ref), rec["J_lbf"], dJ),
                 dJ <= np.finfo(float).eps * len(tp.ref_stations[0]) * tp.N)
    else:
        HT.say("   (no stage-kernel artifact at K %d stations, N %d: TP-1 reads the chain alone)"
               % (len(tp.ref_stations[0]), tp.N))
        HT.check("TP-1 the chain marches their wall certified (%.3e)" % float(out_ref["cert_worst"]),
                 float(out_ref["cert_worst"]) <= 1.0)

    # TP-2: the basis on their contour
    W_t = tp.W_table()
    yb, sb = tp.design_wall(W_t, tp.Xs)
    xd, yd = tp.their_dense_in
    yh = HT.read_table(tp.Xs / S / IN, tp.tab, mode="hermite")
    dev = np.abs(np.asarray(yb) / S / IN - yh)
    t0 = time.time()
    out_t, sch_t = tp.march_record(W_t)
    J_t = float(tp.J_of(out_t))
    HT.say("   their contour through the basis (%s, %d knots): max |y - theirs| %.4f in at"
           " the design stations; J %.4f lbf (their dense wall %.4f: %+.2e), cert %.3e, %.1f s"
           % (P.PARAM, len(tp.xk), dev.max(), lbf(J_t), lbf(J_ref), J_t / J_ref - 1.0,
              float(out_t["cert_worst"]), time.time() - t0))
    kc = HT.TABLES["_knot_class_in"]
    HT.check("TP-2 the basis holds their contour inside the class of permanence (max %.4f in"
             " <= %.2f in/node)" % (dev.max(), kc), dev.max() <= kc)

    # TP-3: replay = record
    t0 = time.time()
    J_rp = float(P.J_replay(jnp.asarray(W_t), tp.w, tp.c, sch_t, tp.ta))
    HT.say("   replay at the recorded design: J %.6f lbf vs record %.6f (rel %.1e), %.1f s"
           % (lbf(J_rp), lbf(J_t), abs(J_rp / J_t - 1.0), time.time() - t0))
    HT.check("TP-3 replay = record at the recorded design (rel %.1e)" % abs(J_rp / J_t - 1.0),
             abs(J_rp / J_t - 1.0) <= 1e3 * np.finfo(float).eps)

    # TP-4: gradient vs the FD ladder
    t0 = time.time()
    J_g, g = P.J_and_grad(W_t, tp.w, tp.c, tp.ta, sch_t)
    HT.say("   value and gradient: %.1f s; |grad| %.4e, grad %s"
           % (time.time() - t0, np.linalg.norm(g), np.array2string(g, precision=4)))
    rng = np.random.default_rng(int(os.environ.get("TPOSE_SEED", 1)))
    f = lambda z: P.J_replay(jnp.asarray(z), tp.w, tp.c, sch_t, tp.ta)   # noqa: E731
    ok = True
    for k in range(int(os.environ.get("TPOSE_NDIR", 2))):
        v = rng.standard_normal(len(W_t)); v /= np.linalg.norm(v)
        t0 = time.time()
        fd, spread = P.fd_ladder(f, W_t, v, 1.0)
        ad = float(g @ v)
        err = abs(ad - fd)
        ok &= err <= spread                        # the ladder's own noise floor
        HT.say("   direction %d: AD %.6e, FD %.6e (ladder spread %.1e), |AD - FD| %.1e, %.1f s"
               % (k, ad, fd, spread, err, time.time() - t0))
    HT.check("TP-4 the adjoint agrees with the FD ladder within its noise floor", ok)
    json.dump(dict(geom=tp.geom, K=tp.K, N=tp.N, J_ref_lbf=lbf(J_ref), J_table_basis_lbf=lbf(J_t),
                   basis=P.PARAM, xk_in=(tp.xk / S / IN).tolist(),
                   W_table_in=(np.asarray(W_t) / S / IN).tolist(), grad=np.asarray(g).tolist(),
                   seconds=time.time() - t00),
              open(os.path.join(HT.ART, "tpose_gates_K%d_N%d.json" % (tp.K, tp.N)), "w"), indent=1)
    HT.say("\n== %d/%d PASS  (%.1f s) ==" % (HT.NPASS[0], HT.NPASS[1], time.time() - t00))
    return HT.NPASS[0] == HT.NPASS[1]


# ======================================================================
# the census of a march: folds over the whole net and inside R
# ======================================================================
def census(tp, out, sch):
    """Stage kernel's H-4 field over the whole net (the march's own station
    spacing as the floor, the sign oriented by the median) and the minimum
    of the same field inside Humphreys' region R (the S34 topological R of
    a1_plug_march: cells whose C- ends on the wall before D). A reading:
    the region-R march is re-run with a census margin (rho 1, mu0 0)."""
    import a1_plug_margin as PMG
    ell2 = float(np.median(np.diff(np.asarray(sch.d["xcols"])))) ** 2
    ms, dep, wh, fl = PMG.np_margin(out, sch, len(tp.start[1]), 1.0, 0.0, ell2,
                                    with_depth=True, with_floor=True)
    orient = float(np.sign(np.median(ms)))
    ms, fl = np.asarray(ms) * orient, np.asarray(fl, bool)
    neg = (~fl) & (ms <= 0.0)
    mgR = dict(PMG.margin_dict(rho=1.0, mu0=0.0, m_ref=1.0, orient=orient, f_edge=0.0,
                               ell2=ell2), vec=True, region="R")
    return dict(n_res=int((~fl).sum()), n_neg=int(neg.sum()),
                frac=100.0 * float(neg.sum()) / max(1, int((~fl).sum())), orient=orient,
                mgR=mgR, ell2=ell2)


def read_design(tp, W, label):
    """Every reading of one design: J (closure priced), J/mdot, knots and tip
    against their contour, wall-angle turns, certificate, folds (net / R)."""
    P = driver()
    S = tp.S
    pbf, P.PB_FROZEN = P.PB_FROZEN, None
    out, sch = tp.march_record(W)
    jp = tp.J_parts(out)
    J = float(jp["F_in"] + jp["push"] + jp["base"])
    cz = census(tp, out, sch)
    oR, _ = tp.march_record(W, margin=cz["mgR"])
    P.PB_FROZEN = pbf
    xk_in = tp.xk / S / IN
    dk = (P.knot_radii(np.asarray(W, float), tp.c) / S / IN
          - HT.read_table(xk_in, tp.tab, mode="hermite"))
    xx = np.linspace(tp.x_T, tp.x_D, tp.FM.CASES["dense_wall_points"])
    yy, ss = tp.design_wall(np.asarray(W, float), xx)
    ang = np.degrees(np.arctan(np.asarray(ss)))
    yh = HT.read_table(xx / S / IN, tp.tab, mode="hermite")
    r = dict(label=label, J_lbf=J / S / S / HT.LBF, push_lbf=float(jp["push"]) / S / S / HT.LBF,
             base_lbf=float(jp["base"]) / S / S / HT.LBF, p_b_pa=float(jp["p_b"]) / HT.PA,
             J_over_m=(J / S / S / HT.LBF) / (tp.md_in / S / S / HT.LBM),
             y_D_in=float(jp["Y_D"]) / S / IN, knots_in=(P.knot_radii(np.asarray(W, float), tp.c)
                                                           / S / IN).tolist(),
             dknots_in=np.asarray(dk).tolist(), max_dev_wall_in=float(np.max(np.abs(np.asarray(yy) / S / IN - yh))),
             turns=HT.n_turns(ang), ang_min=float(ang.min()), ang_max=float(ang.max()),
             cert=float(out["cert_worst"]), folded_net_pct=cz["frac"], n_res=cz["n_res"],
             minR=float(oR["margin_min"]), nR=int(oR["margin_n"]), xk_in=xk_in.tolist())
    HT.say("   %s: J %.1f lbf (push %.0f, base %+.0f; p_b %.3f p_a) J/mdot %.2f; tip %.3f in;"
           " knots - theirs %s in (wall max %.3f in); angle %+.1f..%+.1f deg, %d turn(s);"
           " cert %.3f; folded %.1f %% of the net, min margin in R %+.4f over %d cells"
           % (label, r["J_lbf"], r["push_lbf"], r["base_lbf"], r["p_b_pa"], r["J_over_m"],
              r["y_D_in"], np.array2string(np.asarray(dk), precision=3), r["max_dev_wall_in"],
              r["ang_min"], r["ang_max"], r["turns"], r["cert"], r["folded_net_pct"], r["minR"], r["nR"]))
    return r


# ======================================================================
# stage walk: the TR-SQP from their throat
# ======================================================================
def walk():
    """The record's TR-SQP (a1_plug_spline_opt.run_trsqp, unchanged) on the
    throat posing, the base priced as Humphreys do (p_b frozen within a
    walk, recomputed between walks until compatible; TPOSE_BASE=frozen,
    TPOSE_OUTER walks at most). Starts (TPOSE_START):
      table    THEIR contour read at the knots (stationarity: does it stay?)
      line     a straight chord from T to the tip TPOSE_TIP_IN (default
               their tip) -- a GENERIC start for RE-1
      perturb  their contour + seeded normal knots of TPOSE_PERTURB in
      auniform (angle coordinates) equal increments of the wall angle from
               theta_T to TPOSE_THEND_DEG: a generic ORDERED start
      jsonl    the last accepted base of a per-base log TPOSE_W0_JSONL
    RE-1 reading (DIR-REOB): from a generic start the landing is on their
    contour within the class of permanence at every knot, and its value
    within the band on a move of their contour's (not derived here yet:
    reported, not graded)."""
    t00 = time.time()
    P = driver()
    HT.say("== [F3] the THROAT POSING: the TR-SQP from their throat [X-HMPH] (stage walk) ==")
    tp = ThroatPosing()
    S, w, c, ta = tp.S, tp.w, tp.c, tp.ta
    start = os.environ.get("TPOSE_START", "table")
    W_t = np.asarray(tp.W_table(), float)
    if start == "table":
        W0, tag = W_t.copy(), "table"
    elif start == "line":
        if P.PARAM != "y":
            raise ValueError("the chord start is posed in y coordinates")
        tip = float(os.environ.get("TPOSE_TIP_IN", tp.tab[-1, 1]))
        W0 = tp.y_T + (tip * IN * S - tp.y_T) * (tp.xk - tp.x_T) / (tp.x_D - tp.x_T)
        tag = "line%.2f" % tip
    elif start == "perturb":
        delta = float(os.environ["TPOSE_PERTURB"])
        seed = int(os.environ.get("TPOSE_SEED", 1))
        W0 = W_t + np.random.default_rng(seed).standard_normal(len(W_t)) * delta * IN * S
        tag = "perturb%.2f_seed%d" % (delta, seed)
    elif start == "auniform":
        # a GENERIC monotone start in angle coordinates: equal increments
        # from theta_T to the final angle TPOSE_THEND_DEG -- smooth, ordered,
        # not their distribution (theirs turns fast near T, then slowly)
        if P.PARAM != "angle":
            raise ValueError("the uniform-angle start is posed in angle coordinates")
        th_end = np.radians(float(os.environ["TPOSE_THEND_DEG"]))
        W0 = np.full(len(tp.xk), (th_end - np.arctan(tp.s_T)) / len(tp.xk))
        tag = "auniform%+.0f" % np.degrees(th_end)
    elif start == "jsonl":
        ln = [json.loads(x) for x in open(os.environ["TPOSE_W0_JSONL"]) if x.strip()]
        W0 = np.asarray(ln[-1]["W"], float)
        tag = "from_" + os.path.basename(os.environ["TPOSE_W0_JSONL"]).split(".")[0]
    elif start == "reanchor":
        # a landing of another T (a stage-walk JSON TPOSE_W0_JSON): its knot
        # ANGLES kept, the first increment re-measured from this T -- the
        # warm start of the parametric study in theta_T
        if P.PARAM != "angle":
            raise ValueError("the re-anchored start is posed in angle coordinates")
        src = json.load(open(os.environ["TPOSE_W0_JSON"]))
        W0 = np.asarray(src["W_model"], float).copy()
        W0[0] += np.radians(src["geom"]["thT_deg"]) - np.arctan(tp.s_T)
        tag = "reanchor_" + os.path.basename(os.environ["TPOSE_W0_JSON"]).split(".")[0][len("tpose_walk_"):]
    else:
        raise ValueError("TPOSE_START %s" % start)
    if tp.T_moved and start in ("table", "perturb", "line"):
        raise ValueError("TPOSE_START %s reads their contour from THEIR T" % start)
    if tp.T_moved:
        tag += "_thT%+.2f" % tp.geom["thT_deg"]
    if tp.table_name != "table2":
        tag += "_" + tp.table_name
    if P.BASE_MODEL != "veen":
        tag += "_pb-%s" % P.BASE_MODEL
        if os.environ.get("TPOSE_PS_REF") == "corner":
            tag += "-corner"
    if os.environ.get("TPOSE_PB_EVERY"):
        tag += "_pbevery"
    elif os.environ.get("TPOSE_PB_RELAX"):
        tag += "_pbrelax%s" % os.environ["TPOSE_PB_RELAX"]
    tag += "_%s_K%d_N%d" % (P.PARAM, tp.K, tp.N)
    r0 = read_design(tp, W0, "the start (%s)" % start)
    frozen = os.environ.get("TPOSE_BASE", "frozen") == "frozen"
    n_outer = int(os.environ.get("TPOSE_OUTER", 4)) if frozen else 1
    W = np.asarray(W0, float).copy()
    pb_hist, hists, n_rec_tot = [], [], 0
    stop = "outer budget"
    for it in range(n_outer):
        if frozen:
            P.PB_FROZEN = None
            o_f, _ = tp.march_record(W)
            pb = float(tp.J_parts(o_f)["p_b"])
            pb_hist.append(pb / HT.PA)
            HT.say("   [outer %d] p_b frozen at %.4f p_a (the closure on the current design's"
                   " corner state)" % (it, pb / HT.PA))
            relax = os.environ.get("TPOSE_PB_RELAX")
            if os.environ.get("TPOSE_PB_EVERY"):
                # TPOSE_PB_EVERY (09-23 night): their scheme (p. 1582-3) -- p_b recomputed
                # at EVERY iteration of the wall update: one ACCEPTED TR-SQP step per outer
                # walk (PSPL_ITERS=3 -- segment 0 records the base, a step accepted at segment
                # 1, directly or by backtracking, is recorded and returned at segment 2;
                # PSPL_ITERS=1 never moves, 2 loses a backtracked step) and no early stop on p_b alone (a
                # one-step walk barely moves p_b even far from the optimum); the outer budget
                # is the stop
                pass
            elif relax is None:
                if it > 0 and abs(pb_hist[-1] / pb_hist[-2] - 1.0) <= HT.THRUST_TOL:
                    HT.say("   [outer %d] p_b compatible with the flow (change %.2e <= %.0e): stop"
                           % (it, pb_hist[-1] / pb_hist[-2] - 1.0, HT.THRUST_TOL))
                    stop = "p_b compatible"
                    break
            else:
                # TPOSE_PB_RELAX (09-23 night): under-relaxed fixed point -- the closure on
                # the state at D (Panov-Shvets on p_D) oscillates undamped; compatibility =
                # the closure against the p_b the last walk was frozen at
                if it > 0:
                    if abs(pb / pb_prev - 1.0) <= HT.THRUST_TOL:
                        HT.say("   [outer %d] p_b compatible with the flow (closure/frozen - 1 ="
                               " %.2e): stop" % (it, pb / pb_prev - 1.0))
                        stop = "p_b compatible"
                        break
                    pb = float(relax) * pb + (1.0 - float(relax)) * pb_prev
                    HT.say("   [outer %d] relaxed (%.2f): p_b frozen at %.4f p_a" % (it, float(relax), pb / HT.PA))
                pb_prev = pb
            P.PB_FROZEN = pb
        W, hist, n_rec = P.run_trsqp(W.copy(), w, c, ta, sign=+1.0, max_segments=P.MAXSEG,
                                     maxiter_per_seg=8, verbose=1, bounds=P.design_bounds(c))
        hists.append([list(map(float, h)) if hasattr(h, "__iter__") else float(h) for h in hist])
        n_rec_tot += n_rec
    P.PB_FROZEN = None
    r1 = read_design(tp, W, "the landing")
    # the gradient at the landing, the base frozen at the landing's own p_b
    # (the walk's objective): is the landing stationary?
    o_l, s_l = tp.march_record(W)
    P.PB_FROZEN = float(tp.J_parts(o_l)["p_b"])
    Jl, gl = P.J_and_grad(W, w, c, ta, s_l)
    P.PB_FROZEN = None
    g0n = None
    if hists and hists[0]:
        g0n = hists[0][0][2] if isinstance(hists[0][0], list) and len(hists[0][0]) > 2 else None
    HT.say("   landing: |grad J| %.3e (the walk opened at %s); stop: %s; %d records"
           % (np.linalg.norm(gl), "%.3e" % g0n if g0n else "?", stop, n_rec_tot))
    HT.check("TW-1 the landing is Newton-certified (%.3f)" % r1["cert"], r1["cert"] <= 1.0)
    HT.check("TW-2 no fold inside R at the landing (min margin %+.4f over %d cells)"
             % (r1["minR"], r1["nR"]), r1["minR"] > 0.0)
    kc = HT.TABLES["_knot_class_in"]
    dmax = float(np.max(np.abs(r1["dknots_in"])))
    HT.check("TW-3 [RE-1 in contour] the landing is on their contour within the class of"
             " permanence at every knot (max %.3f in <= %.2f in)" % (dmax, kc), dmax <= kc)
    rec = dict(tag=tag, start=start, basis=P.PARAM, K=tp.K, N=tp.N, geom=tp.geom,
               W0_model=np.asarray(W0).tolist(), W_model=np.asarray(W).tolist(),
               start_reading=r0, landing=r1, pb_frozen_hist_pa=pb_hist, stop=stop,
               grad_landing=np.asarray(gl).tolist(), hist=hists, n_records=n_rec_tot,
               seconds=time.time() - t00)
    json.dump(rec, open(os.path.join(HT.ART, "tpose_walk_%s.json" % tag), "w"), indent=1)
    HT.say("\n== %d/%d PASS  (%.1f s) ==" % (HT.NPASS[0], HT.NPASS[1], time.time() - t00))
    return HT.NPASS[0] == HT.NPASS[1]


# ======================================================================
# stage tslide: the gates of T sliding on their arc (TPOSE_THT_DEG)
# ======================================================================
def tslide():
    """The gates of the knob TPOSE_THT_DEG (2026-09-23/24): T slides on their
    0.5-in arc, D follows at their length T -> D, the arc stations lie on the
    exact circle.
      TS-1 at THEIR theta_T the start 'come loro' is bit-identical to the
           record path (the arc keeps the record's points up to the cut);
      TS-2 at THEIR theta_T, J of their contour through the basis moves by
           less than the basis error of TP-2 (|J_dense - J_basis| on their
           wall): the circle's T against the table's T sits below what the
           representation already carries;
      TS-3 (angle basis) for every theta_T of TPOSE_TS_LIST: T downstream of
           the cut, and their contour's knot angles re-anchored at that T
           march certified (the warm start of the parametric study)."""
    t00 = time.time()
    P = driver()
    P.PB_FROZEN = None
    HT.say("== [F3] T sliding on their arc: the gates of TPOSE_THT_DEG [X-HMPH] (stage tslide) ==")
    os.environ.pop("TPOSE_THT_DEG", None)
    rec = ThroatPosing()
    S = rec.S
    lbf = lambda v: float(v) / S / S / HT.LBF                     # noqa: E731
    W_t = np.asarray(rec.W_table(), float)
    J_dense = lbf(rec.J_of(rec.march_dense(rec.ref_stations)[0]))
    J_rec = lbf(rec.J_of(rec.march_record(W_t)[0]))
    basis_err = abs(J_rec - J_dense)
    HT.say("   record: their wall J %.4f lbf, through the basis %.4f lbf (basis error %.4f lbf)"
           % (J_dense, J_rec, basis_err))
    th_their = rec.geom["thT_deg"]
    os.environ["TPOSE_THT_DEG"] = repr(float(th_their))
    mv = ThroatPosing(verbose=False)
    same = (all(np.array_equal(a, b) for a, b in zip(mv.start, rec.start))
            and mv.F_in == rec.F_in and mv.md_in == rec.md_in)
    HT.check("TS-1 at their theta_T %.5f deg the start 'come loro' is bit-identical to the record's"
             % th_their, same)
    W_m = W_t.copy()
    if P.PARAM == "angle":
        W_m[0] += np.radians(th_their) - np.arctan(mv.s_T)
    J_m = lbf(mv.J_of(mv.march_record(W_m)[0]))
    HT.say("   moved path at their theta_T: T shift (%+.2e, %+.2e) in, J %.4f lbf (%+.4f)"
           % (mv.geom["dT_in"][0], mv.geom["dT_in"][1], J_m, J_m - J_rec))
    HT.check("TS-2 at their theta_T J moves by %.4f lbf <= the basis error %.4f lbf"
             % (abs(J_m - J_rec), basis_err), abs(J_m - J_rec) <= basis_err)
    rows = []
    if P.PARAM != "angle":
        HT.say("   TS-3 skipped: the re-anchored start is posed in angle coordinates")
    else:
        ok3 = True
        for tok in os.environ.get("TPOSE_TS_LIST", "-43.25,-45.75,-51.25,-54.25").split(","):
            th = float(tok)
            os.environ["TPOSE_THT_DEG"] = repr(th)
            tq = ThroatPosing(verbose=False)
            W0 = W_t.copy()
            W0[0] += np.radians(th_their) - np.arctan(tq.s_T)
            out, _ = tq.march_record(W0)
            g = tq.geom
            ok = g["xT_frame_in"] > g["x_cut_in"] and float(out["cert_worst"]) <= 1.0
            ok3 &= ok
            rows.append(dict(thT_deg=th, T_in=g["T_in"], xT_frame_in=g["xT_frame_in"],
                             x_cut_in=g["x_cut_in"], cert=float(out["cert_worst"]),
                             J_start_lbf=lbf(tq.J_of(out))))
            HT.say("   theta_T %+.2f: T (%.5f, %.5f) in, x'_T %.4f > cut %.4f; arc stations %d;"
                   " re-anchored start J %.1f lbf, cert %.3f" % (th, g["T_in"][0], g["T_in"][1],
                                                                 g["xT_frame_in"], g["x_cut_in"],
                                                                 g["n_arc_stations"], rows[-1]["J_start_lbf"],
                                                                 rows[-1]["cert"]))
        HT.check("TS-3 every theta_T of the list: T downstream of the cut and the re-anchored start"
                 " certified", ok3)
    os.environ.pop("TPOSE_THT_DEG", None)
    json.dump(dict(K=rec.K, N=rec.N, basis=P.PARAM, J_dense_lbf=J_dense, J_record_lbf=J_rec,
                   J_moved_their_lbf=J_m, start_identical=bool(same), rows=rows,
                   seconds=time.time() - t00),
              open(os.path.join(HT.ART, "tpose_tslide_K%d_N%d_%s.json" % (rec.K, rec.N, P.PARAM)), "w"),
              indent=1)
    HT.say("\n== %d/%d PASS  (%.1f s) ==" % (HT.NPASS[0], HT.NPASS[1], time.time() - t00))
    return HT.NPASS[0] == HT.NPASS[1]


# ======================================================================
# stage fig4: their Fig. 4 comparison contours through the throat posing
# ======================================================================
def _fig4_read(path, tab):
    """a digitised curve (x y, inches), sorted, the base line at D dropped:
    trailing points steeper than K_RICH times the steepest printed wall angle"""
    a = np.loadtxt(path)
    a = a[np.argsort(a[:, 0], kind="stable")]
    steep = A1.K_RICH * float(np.max(np.abs(np.tan(np.radians(tab[:, 2])))))
    keep = len(a)
    while keep > 2:
        dx = a[keep - 1, 0] - a[keep - 2, 0]
        if dx > 0.0 and abs(a[keep - 1, 1] - a[keep - 2, 1]) <= steep * dx:
            break
        keep -= 1
    return a[:keep]


def fig4():
    """THEIR FIG. 4 through the throat posing (2026-09-24): the two contours of
    the same length as their optimum, +/-0.5 in at D (printed thrusts 32,556
    upper and 32,601 lower against 32,881; _fig4 in the tables), digitised by
    the owner (humphreys1971_digitised/). Each is marched as their Table 2
    (Hermite) plus the digitised DIFFERENCE comparison - optimum -- the
    calibration error common to the three curves cancels -- smoothed by a
    cubic spline at the RANDOM part of the digitisation noise (second
    differences of the optimum's residual; the whole rms as a sensitivity
    variant), then corrected linearly to hold exactly 0 at T and +/-dy at D
    (the paper's only definition). Posed in the y basis (the lower contour crosses theirs;
    the ordered angle basis cannot represent it).
      F4-1 the digitised optimum reads Table 2 inside the class of permanence;
      F4-2 SIGN: both comparison contours lose thrust against their optimum;
      F4-3 ORDER: the upper loses more than the lower (as printed);
      F4-4 CLASS: both comparison marches stay unfolded inside R -- when this
           fails the thrust differences are READINGS under G1.
    The magnitudes are reported against the paper's (also scaled to our mass),
    not graded: they move with the smoothing of the digitised near-throat
    shape by more than their size (measured 2026-09-24: lower -171 / -44 lbf
    between the two variants) -- the comparison is ill-conditioned as well
    as out of class."""
    from scipy.interpolate import UnivariateSpline
    t00 = time.time()
    P = driver()
    if P.PARAM != "y":
        raise ValueError("stage fig4 is posed in the y basis (PSPL_PARAM=y)")
    P.PB_FROZEN = None
    HT.say("== [F3] their Fig. 4 through the throat posing [X-HMPH] (stage fig4) ==")
    tp = ThroatPosing()
    S = tp.S
    tab = tp.tab
    F4 = HT.TABLES["_fig4"]
    rd = {k: _fig4_read(os.path.join(HERE, v), tab) for k, v in F4["digitised_files"].items()}
    herm = lambda x: HT.read_table(np.asarray(x, float), tab, mode="hermite")   # noqa: E731
    xT, xD = tp.x_T / S / IN, tp.x_D / S / IN
    o = rd["optimum"]
    r_opt = o[:, 1] - herm(o[:, 0])
    sig = float(np.sqrt(np.mean(r_opt ** 2)))
    kc = HT.TABLES["_knot_class_in"]
    HT.say("   digitised optimum vs Table 2: rms %.4f in, max %.4f in (%d points)"
           % (sig, np.max(np.abs(r_opt)), len(o)))
    HT.check("F4-1 the digitised optimum reads Table 2 inside the class of permanence"
             " (rms %.4f, max %.4f <= %.2f in)" % (sig, np.max(np.abs(r_opt)), kc),
             np.max(np.abs(r_opt)) <= kc)
    # the RANDOM part of the digitisation noise (the systematic calibration
    # error cancels in the difference): the second-difference estimator of
    # the optimum's residual, var(r_{i+1} - 2 r_i + r_{i-1}) = 6 sigma^2
    d2 = r_opt[2:] - 2.0 * r_opt[1:-1] + r_opt[:-2]
    sig_rand = float(np.sqrt(np.mean(d2 ** 2) / 6.0))
    HT.say("   digitisation noise: random part %.4f in (second differences), whole %.4f in" % (sig_rand, sig))
    xk = tp.xk / S / IN
    res = {"optimum": read_design(tp, tp.W_table(), "their optimum (Table 2)")}
    J_paper = HT.TABLES["thrust_lbf"]["table2"]
    m_ratio = (tp.md_in / S / S / HT.LBM) / (HT.MDOT / HT.LBM)
    for variant, sgm in (("random", sig_rand), ("whole", sig)):
        for name, sgn, J_pr in (("upper", 1.0, F4["thrust_upper_lbf"]), ("lower", -1.0, F4["thrust_lower_lbf"])):
            c = rd[name]
            sel = (c[:, 0] >= max(o[0, 0], xT)) & (c[:, 0] <= o[-1, 0])
            xc = c[sel, 0]
            dc = c[sel, 1] - np.interp(xc, o[:, 0], o[:, 1])
            sp = UnivariateSpline(xc, dc, k=3, s=len(xc) * sgm ** 2)
            a0 = -float(sp(xT))
            b0 = (sgn * F4["dy_at_D_in"] - float(sp(xD)) - a0) / (xD - xT)
            dl = lambda x, sp=sp, a0=a0, b0=b0: sp(x) + a0 + b0 * (np.asarray(x, float) - xT)  # noqa: E731
            W = (herm(xk) + dl(xk)) * IN * S
            key = name if variant == "random" else name + "_whole"
            r = read_design(tp, W, "%s comparison contour (smoothing at the %s noise)" % (name, variant))
            r.update(dJ_lbf=r["J_lbf"] - res["optimum"]["J_lbf"], dJ_paper_lbf=J_pr - J_paper,
                     dJ_paper_our_mass_lbf=(J_pr - J_paper) * m_ratio,
                     delta_knots_in=np.asarray(dl(xk)).tolist(), smoothing_in=sgm)
            res[key] = r
            HT.say("   %s (%s noise %.4f in): Delta at the knots %s in; dJ %+.1f lbf against the paper's"
                   " %+.0f (%+.0f on our mass)" % (name, variant, sgm, np.array2string(np.asarray(dl(xk)), precision=3),
                                                   r["dJ_lbf"], r["dJ_paper_lbf"], r["dJ_paper_our_mass_lbf"]))
    HT.say("   the magnitudes move with the smoothing of the digitised near-throat shape (upper %+.1f / %+.1f,"
           " lower %+.1f / %+.1f lbf): reported, not graded" % (res["upper"]["dJ_lbf"], res["upper_whole"]["dJ_lbf"],
                                                               res["lower"]["dJ_lbf"], res["lower_whole"]["dJ_lbf"]))
    HT.check("F4-2 SIGN: both comparison contours lose thrust (%+.1f, %+.1f lbf)"
             % (res["upper"]["dJ_lbf"], res["lower"]["dJ_lbf"]),
             res["upper"]["dJ_lbf"] < 0.0 and res["lower"]["dJ_lbf"] < 0.0)
    HT.check("F4-3 ORDER: the upper loses more than the lower, as printed",
             res["upper"]["dJ_lbf"] < res["lower"]["dJ_lbf"])
    HT.check("F4-4 CLASS: both comparison marches unfolded inside R (min margin %+.4f, %+.4f)"
             % (res["upper"]["minR"], res["lower"]["minR"]),
             res["upper"]["minR"] > 0.0 and res["lower"]["minR"] > 0.0)
    json.dump(dict(K=tp.K, N=tp.N, sigma_digit_in=sig, sigma_random_in=sig_rand, results=res,
                   seconds=time.time() - t00),
              open(os.path.join(HT.ART, "tpose_fig4_K%d_N%d.json" % (tp.K, tp.N)), "w"), indent=1)
    HT.say("\n== %d/%d PASS  (%.1f s) ==" % (HT.NPASS[0], HT.NPASS[1], time.time() - t00))
    return HT.NPASS[0] == HT.NPASS[1]


if __name__ == "__main__":
    stage = os.environ.get("TPOSE_STAGE", "gates")
    ok = {"gates": gates, "walk": walk, "tslide": tslide, "fig4": fig4}[stage]()
    sys.exit(0 if ok else 1)
