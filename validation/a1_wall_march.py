#!/usr/bin/env python3
"""A1 BRICK 2, STEP 4 [F2/A1]: THE PRESCRIBED-WALL MARCH — the wall as an
INPUT. This is the structural inversion the optimizer needs: Brick 1's
type-0 march GENERATES its wall (mass-flow streamline placement); free-
form design needs the opposite data flow — a wall handed in, the flow
computed ON it. Everything here is assembled from Brick 1's verified
unit processes (interior, axis, inverse-wall) and Sched record/replay;
no new physics, one new march driver.

ENGINE. IVL (Sauer, as Brick 1) -> characteristic fan (as Brick 1) ->
then, instead of the arc + streamline construction, a column per
prescribed wall STATION (x_k, y_k, slope_k): inverse-wall unit at the
station (chord foot search with the same void-row bookkeeping), interior
sweep to the axis, axis unit. Stops at the last station = the lip. The
objective on a prescribed wall is the WALL FORM of step 1 (no uniform
exit is assumed anywhere):

    J_wall = F_ivl + W_wall            (momentum theorem, step 1)

CERTIFICATES (derived bands, R5):
  T1 TWIN: feed the engine Brick 1's OWN type-0 wall polyline as the
     prescribed wall. Same geometry, two different marches: J_wall(new
     engine) must equal J_exit (Brick 1's uniform-exit thrust) within a
     Richardson band from the coarse/fine pair. This certifies the new
     engine end-to-end against the validated one — no GENO needed.
  T2 MASS: the prescribed wall is a streamline of the same flow, so the
     mass flux through the LAST column must equal the throat mdot
     within a Richardson band (independent physics check).
  T3 MARGIN: min wall Mach > 1 (S1-lite monitor; a prescribed wall that
     drives the march subsonic is outside the class and must be seen).
  G1 GRADIENT (STAGE=grad): wall_y -> wall_y + amp*bump(x) with a
     smooth localized bump; dJ/damp by reverse AD over the replayed
     march vs central FD, Richardson-banded. The full spline-control-
     point vector is plumbing on top of this one verified scalar path.
  R1 REJECTOR: a corrupted wall (slope field sign-flipped) must FAIL
     the twin band or fail to march at all.

STAGES (each fits a background budget): default runs T1+T2+T3+R1;
STAGE=grad runs G1 (records at amp=0, replays differentiably).

Run:  .venv-a1/bin/python validation/a1_wall_march.py
      STAGE=grad .venv-a1/bin/python validation/a1_wall_march.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1              # noqa: E402
import a1_thrust_functional as TF            # noqa: E402

import jax                                    # noqa: E402
import jax.numpy as jnp                       # noqa: E402

EPS = A1.EPS
CASE = A1.CASE
K_RICH = A1.K_RICH
NPASS = [0, 0]
d2r = np.pi / 180.0


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ----------------------------------------------------------------------
# the prescribed-wall march
# ----------------------------------------------------------------------
def wall_march(stations, P, tab, cfg, sched=None):
    """stations = (wx, wy, wslope) jnp arrays (K,), ordered downstream,
    starting at the first wall point past the throat lip. P = [yt, rtu]
    relevant part (IVL only). Returns out dict + schedule."""
    ta = A1.tab_arrays(tab)
    S = A1.Sched("rec") if sched is None else A1.Sched("play", sched.d)
    delta_eff = 1.0
    NI = cfg["NI"]
    yt, rtu = P[0], P[1]
    gm = tab["gammamedio"]
    as_ = tab["_as"]
    wx, wy, wsl = stations

    t_int = A1.get_solver(("int", delta_eff),
                          lambda: A1.make_resid_interior(delta_eff))
    t_axi = A1.get_solver(("axi", delta_eff),
                          lambda: A1.make_resid_axis(delta_eff))
    t_wal = A1.get_solver(("wal", delta_eff),
                          lambda: A1.make_resid_inwall(delta_eff))

    def with_ta(t):
        return (lambda z0, p: t[0](z0, p, ta),
                lambda z, p: t[2](z, p, ta))
    solver_int, solver_axi = with_ta(t_int), with_ta(t_axi)
    solver_wal = with_ta(t_wal)
    cert = dict(worst=0.0, n=0)

    def certify(stepfn, z, p):
        if S.mode != "rec":
            return
        step = float(stepfn(z, jnp.asarray(p)))
        sc = max(1.0, float(jnp.max(jnp.abs(z))))
        cert["worst"] = max(cert["worst"],
                            step / (A1.NEWTON_TOL_FACTOR * EPS * sc))
        cert["n"] += 1

    def cell(solver, p, z0):
        p = jnp.asarray(p)
        z = S.cell(solver[0], p, z0)
        certify(solver[1], z, p)
        return z

    # ---- IVL (identical formulas to Brick 1)
    delta = 1.0
    alpha = jnp.sqrt((1.0 + delta) / ((gm + 1.0) * rtu * yt))
    c1 = -(gm + 1.0) * alpha / (2.0 * (3.0 + delta))
    c2 = (gm + 1.0) * alpha**2 / (2.0 * (1.0 + delta))
    eshift = -(gm + 1.0) * alpha * yt**2 / (2.0 * (3.0 + delta))
    jj = jnp.arange(NI)
    y_ivl = yt * (1.0 - jj / (NI - 1.0))
    x_raw = c1 * y_ivl**2 + 0.000001
    u_ivl = as_ * (1.0 + alpha * x_raw + c2 * y_ivl**2)
    x_ivl = x_raw - eshift
    G = {}
    for k in range(NI):
        G[(k + 1, 1)] = jnp.array([x_ivl[k], y_ivl[k], u_ivl[k], 0.0])
    _, _, rho_ivl, _, _, _ = A1.state_q(u_ivl, ta)
    f_m = rho_ivl * u_ivl * y_ivl
    yy, ff = y_ivl[::-1], f_m[::-1]
    hgrid = yy[1] - yy[0]
    w = np.ones(NI)
    w[1:-1:2], w[2:-1:2] = 4.0, 2.0
    mdot = 2.0 * jnp.pi * hgrid / 3.0 * jnp.sum(jnp.array(w) * ff)

    # ---- characteristic fan (identical structure to Brick 1)
    for i in range(2, NI + 1):
        G[(NI + 1 - i, i)] = G[(NI + 1 - i, 1)]
        for j in range(2 - i, i - 1):
            pt1 = G[(NI + j - 1, i)]
            pt2 = G[(NI + j, i - 1)]
            z0 = A1.predict_interior(pt1, pt2, ta, delta_eff) \
                if S.mode == "rec" else None
            p = jnp.concatenate([pt1, pt2])
            z = cell(solver_int, p,
                     z0 if z0 is not None else jnp.zeros(4))
            G[(NI + j, i)] = z
        pt1 = G[(NI + i - 2, i)]
        z0 = A1.predict_axis(pt1, ta, delta_eff) \
            if S.mode == "rec" else None
        z = cell(solver_axi, pt1,
                 z0 if z0 is not None else jnp.zeros(2))
        G[(NI + i - 1, i)] = jnp.array([z[0], 0.0, z[1], 0.0])

    # ---- prescribed-wall columns (arc-loop structure, geometry from
    #      the stations; no Me logic — stop at the last station)
    j2 = 2 * NI - 1
    Nv = 1
    K = int(wx.shape[0]) if S.mode == "rec" else len(S.d["K_cols"])
    wall_pts = []
    for kst in range(K):
        i = NI + 1 + kst
        x4, y4, l0 = wx[kst], wy[kst], wsl[kst]
        if S.mode == "rec":
            N = 0
            while True:
                N += 1
                if N > j2 + 2:
                    raise RuntimeError("wall col %d: wall_search did"
                                       " not land" % i)
                pt3 = G[(N, i - 1)]
                pt1 = G[(Nv + 1, i - 1)]
                p = jnp.concatenate([pt1, pt3, jnp.array([x4, y4, l0])])
                z0 = A1.predict_wall(pt1, pt3, x4, y4, l0, ta, delta_eff)
                zt = solver_wal[0](z0, p)
                if float(zt[0]) > float(pt1[0]):
                    N = Nv
                    Nv += 1
                    continue
                break
            S.d["dec"].append((N, Nv))
            S.d["z"].append(np.asarray(zt))
            certify(solver_wal[1], zt, p)
            z = zt
        else:
            N, Nv = S.dec(None)
            pt3 = G[(N, i - 1)]
            pt1 = G[(Nv + 1, i - 1)]
            p = jnp.concatenate([pt1, pt3, jnp.array([x4, y4, l0])])
            z0r = jax.lax.stop_gradient(jnp.array(S.d["z"][S._iz]))
            S._iz += 1
            z = solver_wal[0](z0r, p)
        u4 = z[1]
        wall_pt = jnp.array([x4, y4, u4, l0 * u4])
        G[(1, i)] = wall_pt
        wall_pts.append(wall_pt)
        for j in range(Nv + 1, j2 + 1):
            pt1 = G[(1, i)] if j == Nv + 1 else G[(j - 1, i)]
            pt2 = G[(j, i - 1)]
            z0 = A1.predict_interior(pt1, pt2, ta, delta_eff) \
                if S.mode == "rec" else None
            p = jnp.concatenate([pt1, pt2])
            z = cell(solver_int, p,
                     z0 if z0 is not None else jnp.zeros(4))
            G[(j, i)] = z
        pt1 = G[(j2, i)]
        z0 = A1.predict_axis(pt1, ta, delta_eff) \
            if S.mode == "rec" else None
        z = cell(solver_axi, pt1,
                 z0 if z0 is not None else jnp.zeros(2))
        G[(j2 + 1, i)] = jnp.array([z[0], 0.0, z[1], 0.0])
        j2 += 1
        if S.mode == "rec":
            S.d.setdefault("K_cols", []).append(int(i))

    # last column states (wall row 1 .. axis row j2), for the mass check
    ilast = NI + K
    col = [G[(j, ilast)] for j in range(1, j2 + 1) if (j, ilast) in G]
    # [O3.3 addition, ADDITIVE: full mesh nodes (rec mode only) for
    #  field interpolation onto reference surfaces]
    mesh = jnp.stack(list(G.values())) if S.mode == "rec" else None
    out = dict(wall_x=jnp.stack([p[0] for p in wall_pts]),
               wall_y=jnp.stack([p[1] for p in wall_pts]),
               wall_u=jnp.stack([p[2] for p in wall_pts]),
               wall_v=jnp.stack([p[3] for p in wall_pts]),
               mdot=mdot, cert_worst=cert["worst"], cert_n=cert["n"],
               last_col=jnp.stack(col), mesh_pts=mesh)
    return out, S


def col_massflux(col, ta):
    """Mass flux through a column polyline (axisym): sum of segment
    fluxes rho * (u.n) * 2 pi y_m * ds with the segment normal."""
    x, y = col[:, 0], col[:, 1]
    u, v = col[:, 2], col[:, 3]
    dx, dy = x[1:] - x[:-1], y[1:] - y[:-1]
    ds = jnp.sqrt(dx * dx + dy * dy)
    nx, ny = dy / ds, -dx / ds                # normal, downstream-facing
    um, vm = 0.5 * (u[1:] + u[:-1]), 0.5 * (v[1:] + v[:-1])
    ym = 0.5 * (y[1:] + y[:-1])
    q = jnp.sqrt(um * um + vm * vm)
    rho = A1.state_q(q, ta)[2]
    flux = rho * (um * nx + vm * ny) * 2.0 * jnp.pi * ym * ds
    return jnp.abs(jnp.sum(flux))


def stations_from_wall(out):
    """Brick-1 wall polyline -> stations with central-difference slopes."""
    wx = np.array(out["wall_x"])
    wy = np.array(out["wall_y"])
    sl = np.gradient(wy, wx)
    return jnp.array(wx), jnp.array(wy), jnp.array(sl)


def J_wall(P4, out, tab, ta, pa=0.0):
    F, _ = TF.ivl_flux(P4, tab, ta, pa)
    W = TF.wall_push(out, ta, pa, close=TF.ivl_top(P4, tab))
    return F + W


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    stage = os.environ.get("STAGE", "twin")
    print("== A1 brick 2 step 4: prescribed-wall march [F2/A1]"
          " (stage=%s) ==" % stage)
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    P0 = jnp.array([CASE["yt"], CASE["rtu"], CASE["rtd"], CASE["eps"]])
    cfg = dict(NI=CASE["NI"], Ne=CASE["Ne"], da_deg=CASE["da_deg"])
    cfg_f = dict(NI=2 * CASE["NI"] - 1, Ne=2 * CASE["Ne"] - 1,
                 da_deg=0.5 * CASE["da_deg"])

    print("-- S1: Brick-1 reference marches (coarse%s) --"
          % ("+fine" if stage == "twin" else ""))
    ref_c, _ = A1.run_march(P0, tab, cfg)
    Jex_c = float(TF.J_exit_of_out(ref_c, ta, tab["_as"]))
    st_c = stations_from_wall(ref_c)

    if stage == "grad":
        print("-- S2g: record at amp=0; replay-differentiable J(amp) --")
        wx0, wy0, sl0 = st_c
        xm = 0.5 * (float(wx0[0]) + float(wx0[-1]))
        sig = 0.15 * (float(wx0[-1]) - float(wx0[0]))

        def shaped(amp):
            b = jnp.exp(-0.5 * ((wx0 - xm) / sig) ** 2)
            db = b * (-(wx0 - xm) / sig**2)
            return wx0, wy0 + amp * b, sl0 + amp * db

        out0, S0 = wall_march(shaped(0.0), P0, tab, cfg)

        def Jfun(amp):
            o, _ = wall_march(shaped(amp), P0, tab, cfg, sched=S0)
            return J_wall(P0, o, tab, ta)

        # DIAGNOSED (see docs): the EOS tables are interpolated
        # piecewise-LINEARLY, so the exact derivative of the code
        # carries a ripple at the table-cell scale (measured ~0.3%
        # of the gradient, ~1e-10 of J). AD is exact for the code as
        # written; the meaningful certificate is the ENVELOPE identity:
        # the ripple-averaged AD must equal the large-h secant, with
        # the band derived from Richardson + the measured AD scatter.
        amps = [-2e-4, -1e-4, 0.0, 1e-4, 2e-4]
        Js = [float(Jfun(jnp.float64(a))) for a in amps]
        gs = [float(jax.grad(Jfun)(jnp.float64(a))) for a in amps]
        s_h = (Js[4] - Js[0]) / 4e-4
        s_h2 = (Js[3] - Js[1]) / 2e-4
        # separate CURVATURE (smooth J'' trend, physical) from RIPPLE
        # (table-cell kinks): linear fit of AD(amp); the fit residual is
        # the ripple, the fit intercept estimates the envelope J'(0).
        A = np.polyfit(np.array(amps), np.array(gs), 1)
        ad_env = float(np.polyval(A, 0.0))
        resid = np.array(gs) - np.polyval(A, np.array(amps))
        rip_std = float(np.std(resid))
        band = K_RICH * (abs(s_h - s_h2) + rip_std / np.sqrt(len(gs))) \
            + A1.C_FLOOR * EPS * abs(Js[2]) / 1e-4
        d = abs(ad_env - s_h2)
        print("  AD samples: %s" % " ".join("%.1f" % g for g in gs))
        print("  curvature J'' = %.3e (smooth, physical); ripple std ="
              " %.1f (%.3f%% of grad — table-cell kinks)"
              % (A[0], rip_std, 100 * rip_std / abs(ad_env)))
        print("  envelope: AD fit intercept=%.3f  secants s(h)=%.3f"
              " s(h/2)=%.3f" % (ad_env, s_h, s_h2))
        print("  |AD_env - secant| = %.3f   band = %.3f" % (d, band))
        check("G1 envelope gradient: AD == secant within derived band",
              d <= band)
        check("G1b sensitivity nonzero (the wall matters)",
              abs(ad_env) > band)
        rip = max(abs(Js[i] - (Js[2] + ad_env * amps[i]))
                  for i in (0, 1, 3, 4))
        print("  ripple in J: max linear-fit residual %.3e (%.1e of J)"
              % (rip, rip / abs(Js[2])))
        print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                              time.time() - t0))
        sys.exit(0 if NPASS[0] == NPASS[1] else 1)

    ref_f, _ = A1.run_march(P0, tab, cfg_f)
    Jex_f = float(TF.J_exit_of_out(ref_f, ta, tab["_as"]))
    st_f = stations_from_wall(ref_f)

    print("-- S2: prescribed-wall marches on Brick 1's own contours --")
    out_c, _ = wall_march(st_c, P0, tab, cfg)
    NI_save = CASE["NI"]
    out_f, _ = wall_march(st_f, P0, tab, cfg_f)
    print("  coarse: %d stations, cert=%.2f (n=%d)"
          % (out_c["wall_x"].shape[0], out_c["cert_worst"],
             out_c["cert_n"]))
    print("  fine  : %d stations, cert=%.2f (n=%d)"
          % (out_f["wall_x"].shape[0], out_f["cert_worst"],
             out_f["cert_n"]))
    check("all cells Newton-certified (both resolutions)",
          out_c["cert_worst"] <= 1.0 and out_f["cert_worst"] <= 1.0)

    print("-- S3: T1 twin — J_wall(new engine) vs J_exit(Brick 1) --")
    Jw_c = float(J_wall(P0, out_c, tab, ta))
    CASE["NI"] = cfg_f["NI"]
    Jw_f = float(J_wall(P0, out_f, tab, ta))
    CASE["NI"] = NI_save
    dc, df = Jw_c - Jex_c, Jw_f - Jex_f
    band = K_RICH * abs(dc - df) + A1.C_FLOOR * EPS * abs(Jex_f)
    print("  J_wall coarse/fine = %.10e / %.10e" % (Jw_c, Jw_f))
    print("  J_exit coarse/fine = %.10e / %.10e" % (Jex_c, Jex_f))
    print("  delta  coarse/fine = %+.3e / %+.3e   band = %.3e"
          " (rel %.1e)" % (dc, df, band, band / abs(Jex_f)))
    check("T1 twin: |J_wall - J_exit| <= Richardson band on same wall",
          abs(df) <= band)

    print("-- S4: T2 mass conservation through the last column --")
    md_col = float(col_massflux(out_f["last_col"], ta))
    md = float(out_f["mdot"])
    md_c = float(col_massflux(out_c["last_col"], ta))
    band_m = K_RICH * abs(md_c / float(out_c["mdot"]) - md_col / md) \
        * md + A1.C_FLOOR * EPS * md
    print("  mdot(last col)=%.8e vs throat %.8e  |d|=%.2e band=%.2e"
          % (md_col, md, abs(md_col - md), band_m))
    check("T2 mass flux through last column == throat mdot in band",
          abs(md_col - md) <= band_m)

    print("-- S5: T3 wall Mach margin (S1-lite) --")
    q = jnp.sqrt(out_f["wall_u"]**2 + out_f["wall_v"]**2)
    Mwall = np.array(A1.state_q(q, ta)[5])
    print("  min wall M = %.4f" % Mwall.min())
    check("T3 min wall Mach > 1", Mwall.min() > 1.0)

    print("-- S6: R1 rejector — corrupted wall (slopes sign-flipped) --")
    try:
        bad = (st_c[0], st_c[1], -st_c[2])
        out_b, _ = wall_march(bad, P0, tab, cfg)
        Jb = float(J_wall(P0, out_b, tab, ta))
        ok_rej = abs(Jb - Jex_c) > 10.0 * band
        print("  corrupted J delta = %.3e (band %.3e)"
              % (abs(Jb - Jex_c), band))
    except (RuntimeError, FloatingPointError,
            ZeroDivisionError, ValueError) as e:
        ok_rej = True
        print("  corrupted wall failed to march (%s) -> rejected"
              % type(e).__name__)
    check("R1 corrupted wall rejected (band exit or march failure)",
          ok_rej)

    print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
