#!/usr/bin/env python3
"""A1 BRICK 2, STEP 11 [F2/A1]: THE GENO FULL-FIELD PLUG TWIN — our
certified plug march run on the spike contour GENO's two-constraint
RaoPlug produces (gamma123 case of record, N-65/N-66 session), the two
codes compared FIELD AGAINST FIELD.

THE TWO SIDES ARE INDEPENDENT CONSTRUCTIONS. GENO builds the Rao
spike backward: phase 1 rotates the lip member by fixed dtheta steps,
integrates one C- curve per member with its interior/inverse-wall
cells, and places each wall point by MASS BALANCE (the N-65
termination), truncated at the mass-set point D. Our engine knows
nothing of that construction: it is a general 2D axisymmetric MoC
march (interior + prescribed-wall + free-jet cells, individually
certified) that treats GENO's contour as an ordinary prescribed wall
and marches FORWARD from a Cauchy cut.

POSING (all data GENO's own; no analytic fan is posed):
  gas    — gconst tables identified FROM GENO's field: gamma =
           5.34782609/4.34782609 (the thermo recipe — GENO's gas is
           ANALYTIC cp = const, verified from Types_thermo_sm), Rg
           from nodal p/(rho T) (std 8.7e-9), and the field's own
           effective isentrope: p0 = 6.008172e6 Pa, NOT the nominal
           6.0e6 (GENO's construction offset, uniform to 1.1e-4);
  start  — a vertical Cauchy cut at x0 = 0.15 through GENO's
           phase-1 C- curves (each crossing interpolated on the
           curve's own nodes; cross-checked against an independent
           2D interpolation of the same field to 1e-5; polyline
           representation error <= 1e-4 at N = 33, measured);
           the top of the design region is the IVL (last C-)
           crossing; ABOVE the IVL (a region GENO does not compute)
           a free-jet strip is posed, blending continuously from
           the IVL-crossing state to the last-member edge state —
           by the domain of dependence it cannot influence the wall
           or the sub-IVL field (C- from above the IVL stays above
           it; the wall ends at D where the IVL lands; verified:
           uniform-vs-blend strip changes the wall by nothing);
  wall   — GENO's contour with slopes tan(theta_w) (wall tangency
           verified on GENO's own data to 1.6e-5), stations
           subsampled on [x0, 0.93] (D = 0.93873 excluded);
  edge   — ambient = our tables' pressure at the last member speed.

THE MEASURED CROSS-CODE GAP AND ITS FORENSICS (the step's central
finding — session 2026-08-07). The two fields agree to 3-4 digits
and NO BETTER, and the residual gap is characterized precisely:
  * a START TRANSIENT near the cut (mid-heights, |dtheta| up to
    1.1e-2 rad, decaying by x ~ 0.35; resolution-stable; moves with
    the cut, i.e. an artifact of ingesting a cut through the
    strong near-lip fan curvature), and
  * a settled UNIFORM DRIFT: q +4e-4 relative across the whole
    column, growing linearly with marched length (x0-sweep:
    ~4.4e-4 per unit length), wall p -2e-3.
  Exhaustively EXCLUDED as causes: the gas (both sides analytic-
  equivalent to ~1e-8); the wall geometry/tangency (1.6e-5); the
  cut data (1e-5, two independent routes); the cut polyline
  resolution (measured 1e-4 -> 5e-6, N 33 -> 201, drift unchanged);
  the above-IVL strip (blend-vs-uniform null + domain of
  dependence); GENO's own discretization (a DIAGNOSTIC GENO build
  with dtheta AND curve-dx halved moved its wall by only 3.5e-6 —
  GENO is step-converged; sources reverted, binary restored,
  md5-verified); our station/row resolution (K, N halving moves
  the deviation < 10% of itself). Both codes' fields satisfy the
  SAME trapezoidal MoC relations at 1e-8..1e-9 (route-B residual
  audit on both meshes) — which also proves the two discrete
  systems are algebraically EQUIVALENT, and that such an audit is
  TAUTOLOGICAL for accuracy (each code solves its own relations
  exactly; it cannot see a slowly-accumulating bias). Scale: the
  drift is 0.5% OF THE AXISYMMETRIC SOURCE CONTRIBUTION at the
  wall (-5.4% of q, measured by a delta = 0 control march).
  ATTRIBUTION OPEN (owner-side question for GENO: candidate
  mechanisms live in what refinement does not vary — e.g. the
  phase-1 backward-march re-interpolation bookkeeping — vs our
  foot-search chord interpolation; undecidable from outside at
  this level).

ACCEPTANCE THRESHOLDS ARE DECLARED, WITH PROVENANCE — this suite's
bands are NOT truncation-derived (the gap sits above both codes'
truncation): they are the S8-established cross-code agreement level
(the independent Rao-curve integrator of the two-constraint session
agreed with GENO to 3-4 digits), re-measured here on the full field,
with >= 2x margin on every measured statistic:
  wall p 3e-3 (measured median 1.9e-3, tail 2.3e-3), settled field
  q 1e-3 / theta 1.5e-3 (measured p95 4.5e-4 / 5.3e-4), IVL
  integrals 2.5e-3 (measured 1.2e-3). The rejectors prove the
  instrument resolves defects one order above the gap.

CHECKS:
  G-1  gas twin: our tables reproduce GENO's nodal (T, p, rho)
       from V alone within GENO's own measured self-consistency
       floors (h0 2.0e-5, s/R 4.7e-6, p0 1.1e-4) — DERIVED bands;
  G-2  all cells Newton-certified, both resolutions;
  G-3  wall pressure on the contour vs GENO's wall pressure:
       >= 95% of stations within 3e-3;
  G-4  settled interior field (x > 0.35) at GENO's own phase-1
       nodes: >= 95% of nodes within q 1e-3 AND theta 1.5e-3
       (the near-cut transient zone is reported, not gated);
  G-5  mass flux through the IVL segment x in [0.17, 0.90], same
       nodes same quadrature, ours vs GENO's within 2.5e-3
       (quadrature CALIBRATED: on GENO's full IVL it reproduces
       the printed mdot to 2.4e-7 and F to 2.3e-7 — F is the
       ABSOLUTE-pressure momentum integral);
  G-6  thrust functional through the same segment within 2.5e-3;
  R-1  rejector: corrupted gamma (x 1.01) collapses G-3 (< 50%);
  R-2  rejector: corrupted contour (y x 1.005) collapses G-3.

REFERENCE DATA (untracked cache, N-36 convention): validation/
_geno_twin/ref.npz, extracted from a GENO run of CASES/
raoplug_gamma123/input.ini (thermo paths absolute) by
extract_ref(rundir); provenance copies of input.ini and
raoplug_performance.dat sit beside it. Regenerate:
  GENO_RUN=<rundir> .venv-a1/bin/python validation/a1_geno_plug_twin.py

Run:  .venv-a1/bin/python validation/a1_geno_plug_twin.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1              # noqa: E402
from a1_freejet_unit import q_at_pa          # noqa: E402
from a1_plug_march import plug_march         # noqa: E402

import jax.numpy as jnp                       # noqa: E402

EPS = A1.EPS
K_RICH = A1.K_RICH
NPASS = [0, 0]
HERE = os.path.dirname(os.path.abspath(__file__))
CKPT = os.path.join(HERE, "_geno_twin")
REF = os.path.join(CKPT, "ref.npz")

X0 = 0.15                                    # start-cut station
X_END = 0.93                                 # short of D = 0.93873
X_SETTLED = 0.35                             # transient washed out
GAMMA = 5.34782609 / 4.34782609              # the thermo recipe
# declared cross-code thresholds (S8 3-4-digit level; >= 2x margin)
TH_WALL, TH_Q, TH_TH, TH_IVL = 3.0e-3, 1.0e-3, 1.5e-3, 2.5e-3


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ----------------------------------------------------------------------
# reference extraction (GENO run dir -> ref.npz)
# ----------------------------------------------------------------------
def _parse_sol(fn):
    """GENO .sol wall files: header + 15-value records over lines."""
    vals, buf = [], []
    with open(fn) as f:
        f.readline()
        for line in f:
            buf += line.split()
            if len(buf) >= 15:
                vals.append([float(v) for v in buf[:15]])
                buf = buf[15:]
    return np.array(vals)


def extract_ref(rundir):
    """Extract the twin reference bundle from a GENO gamma123 run."""
    os.makedirs(CKPT, exist_ok=True)
    PREF = A1.PREF
    d = np.loadtxt(os.path.join(rundir, "plug_diag.dat"))
    ph = d[:, 0].astype(int)
    m = ph <= 1
    V, th, p, T, M = (d[m, i] for i in (6, 7, 8, 9, 11))
    rho = d[m, 5]
    Rg = float(np.mean(p / (rho * T)))
    cp = GAMMA * Rg / (GAMMA - 1.0)
    h0n = cp * T + 0.5 * V * V
    ts_eff = float(np.mean(h0n) / cp)
    sn = cp * np.log(T) - Rg * np.log(p)
    s0t = float(np.mean(sn)) + Rg * np.log(PREF)
    ps_eff = PREF * np.exp((cp * np.log(ts_eff) - s0t) / Rg)
    fl_h0 = float((h0n.max() - h0n.min()) / np.mean(h0n))
    fl_s = float((sn.max() - sn.min()) / Rg)
    f = 1 + 0.5 * (GAMMA - 1) * M * M
    p0n = p * f ** (GAMMA / (GAMMA - 1))
    fl_p0 = float((p0n.max() - p0n.min()) / np.mean(p0n))
    w = _parse_sol(os.path.join(rundir, "inf.sol"))
    o = np.argsort(w[:, 0])
    wall = w[o][:, [0, 1, 2, 3, 4, 5, 7, 9]]   # x y rho V th p T M
    b = d[ph == 0]
    ivl = b[:, [3, 4, 5, 6, 7, 8, 9, 11]]
    b1 = d[ph == 1]
    ph1 = b1[:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]]
    np.savez_compressed(
        REF, wall=wall, ivl=ivl, ph1=ph1,
        gas=np.array([GAMMA, Rg, ts_eff, ps_eff]),
        floors=np.array([fl_h0, fl_s, fl_p0]))
    print("  extracted ref.npz from %s" % rundir)


# ----------------------------------------------------------------------
# quadrature over an oriented polyline of nodes
# (CALIBRATED on the full IVL vs the printed mdot/F: 2.4e-7 / 2.3e-7;
#  F is the ABSOLUTE-pressure momentum integral, GENO's convention)
# ----------------------------------------------------------------------
def curve_fluxes(x, y, rho, u, v, p):
    dx, dy = np.diff(x), np.diff(y)
    w = 2.0 * np.pi * 0.5 * (y[1:] + y[:-1])
    rm = 0.5 * (rho[1:] + rho[:-1])
    um = 0.5 * (u[1:] + u[:-1])
    vm = 0.5 * (v[1:] + v[:-1])
    pm = 0.5 * (p[1:] + p[:-1])
    dmd = rm * (um * dy - vm * dx) * w
    return (float(abs(np.sum(dmd))),
            float(abs(np.sum(um * dmd + pm * dy * w))))


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    print("== A1 brick 2 step 11: GENO full-field plug twin"
          " [F2/A1] ==")
    if not os.path.exists(REF):
        rd = os.environ.get("GENO_RUN")
        if not rd:
            print("  ref.npz missing and GENO_RUN not set — run the"
                  " GENO gamma123 case first (see docstring)")
            sys.exit(2)
        extract_ref(rd)
    elif os.environ.get("GENO_RUN"):
        extract_ref(os.environ["GENO_RUN"])
    R = np.load(REF)
    wall, ivl, ph1 = R["wall"], R["ivl"], R["ph1"]
    gam, Rg, ts_eff, ps_eff = R["gas"]
    fl_h0, fl_s, fl_p0 = R["floors"]
    print("  gas: gamma %.9f Rg %.4f  isentrope (%.4f K,"
          " %.6e Pa)" % (gam, Rg, ts_eff, ps_eff))
    print("  GENO self-consistency floors: h0 %.1e  s/R %.1e"
          "  p0 %.1e" % (fl_h0, fl_s, fl_p0))

    tab = A1.prep_tab(A1.build_tab_gconst(g=float(gam), Rg=float(Rg),
                                          ts=float(ts_eff),
                                          ps=float(ps_eff)))
    ta = A1.tab_arrays(tab)
    as_ = tab["_as"]

    # ---- G-1: the gas twin, on GENO's own nodes (DERIVED bands) ---
    idx = np.linspace(0, len(ph1) - 1, 4000).astype(int)
    Vn, pn, Tn, rn = ph1[idx, 5], ph1[idx, 7], ph1[idx, 8], \
        ph1[idx, 4]
    st = A1.state_q(jnp.array(Vn), ta)
    dT = np.max(np.abs(np.array(st[0]) - Tn) / Tn)
    dp = np.max(np.abs(np.array(st[1]) - pn) / pn)
    dr = np.max(np.abs(np.array(st[2]) - rn) / rn)
    band_T = K_RICH * fl_h0 + 64 * EPS
    band_p = K_RICH * fl_p0 + 64 * EPS
    print("  G-1 gas twin: max rel dT %.2e (band %.2e), dp %.2e"
          " (band %.2e), drho %.2e" % (dT, band_T, dp, band_p, dr))
    check("G-1 tables reproduce GENO's nodal (T, p, rho) from V"
          " within measured floors",
          dT <= band_T and dp <= band_p and dr <= band_p)

    # ---- the posed world ------------------------------------------
    q_last = float(ivl[0, 3])
    th_last = float(ivl[0, 4])
    pa = float(A1.state_q(jnp.float64(q_last), ta)[1])
    qpa = q_at_pa(pa, ta, as_)
    print("  edge member: q %.4f (GENO %.4f), th %.3f deg, pa ="
          " %.6e" % (qpa, q_last, np.degrees(th_last), pa))

    iters = ph1[:, 0].astype(int)
    order = np.argsort(iters, kind="stable")
    p1s = ph1[order]
    bounds = np.searchsorted(p1s[:, 0], np.arange(
        p1s[0, 0], p1s[-1, 0] + 2))

    def cut_crossings(x0):
        ys, us, vs = [], [], []
        for k in range(len(bounds) - 1):
            c = p1s[bounds[k]:bounds[k + 1]]
            if len(c) < 2 or c[-1, 2] <= x0:
                continue                      # curve ends left of cut
            xs = c[:, 2]
            if not np.all(np.diff(xs) > 0):
                o = np.argsort(xs)
                c = c[o]
                xs = c[:, 2]
            yy = np.interp(x0, xs, c[:, 3])
            VV = np.interp(x0, xs, c[:, 5])
            tt = np.interp(x0, xs, c[:, 6])
            ys.append(yy)
            us.append(VV * np.cos(tt))
            vs.append(VV * np.sin(tt))
        o = np.argsort(ys)
        return np.array(ys)[o], np.array(us)[o], np.array(vs)[o]

    ys_c, us_c, vs_c = cut_crossings(X0)
    y_w0 = float(np.interp(X0, wall[:, 0], wall[:, 1]))
    V_w0 = float(np.interp(X0, wall[:, 0], wall[:, 3]))
    t_w0 = float(np.interp(X0, wall[:, 0], wall[:, 4]))
    y_i0 = float(np.interp(X0, ivl[:, 0], ivl[:, 1]))
    V_i0 = float(np.interp(X0, ivl[:, 0], ivl[:, 3]))
    t_i0 = float(np.interp(X0, ivl[:, 0], ivl[:, 4]))
    y_e0 = 1.0 + np.tan(th_last) * X0         # free edge from lip
    print("  cut at x0=%.2f: %d curve crossings, wall y %.4f, IVL"
          " y %.4f, edge y %.4f" % (X0, len(ys_c), y_w0, y_i0,
                                    y_e0))

    def start_line(N):
        """N rows wall -> IVL from GENO data, + a free-jet strip
        above the IVL blending continuously from the IVL-crossing
        state to the last-member edge state, + the edge point."""
        m = (ys_c > y_w0 + 1e-9) & (ys_c < y_i0 - 1e-9)
        yy = np.concatenate([[y_w0], ys_c[m], [y_i0]])
        uu = np.concatenate([[V_w0 * np.cos(t_w0)], us_c[m],
                             [V_i0 * np.cos(t_i0)]])
        vv = np.concatenate([[V_w0 * np.sin(t_w0)], vs_c[m],
                             [V_i0 * np.sin(t_i0)]])
        pick = np.unique(np.linspace(0, len(yy) - 1, N).astype(int))
        yy, uu, vv = yy[pick], uu[pick], vv[pick]
        n_up = max(3, N // 8)
        y_up = np.linspace(y_i0, y_e0, n_up + 2)[1:-1]
        f = (y_up - y_i0) / (y_e0 - y_i0)
        q_up = V_i0 + (qpa - V_i0) * f
        t_up = t_i0 + (th_last - t_i0) * f
        ys = np.concatenate([yy, y_up, [y_e0]])
        us = np.concatenate([uu, q_up * np.cos(t_up),
                             [qpa * np.cos(th_last)]])
        vs = np.concatenate([vv, q_up * np.sin(t_up),
                             [qpa * np.sin(th_last)]])
        return (X0, ys, us, vs)

    mw = (wall[:, 0] > X0 + 1e-9) & (wall[:, 0] <= X_END)
    wx, wy, wth = wall[mw, 0], wall[mw, 1], wall[mw, 4]

    def stations(K, yscale=1.0):
        sx = np.interp(np.linspace(0, 1, K),
                       np.linspace(0, 1, mw.sum()), wx)
        sy = np.interp(sx, wx, wy) * yscale
        ssl = np.tan(np.interp(sx, wx, wth)) * yscale
        return (jnp.array(sx), jnp.array(sy), jnp.array(ssl))

    def run(K, N, tab_r=None, yscale=1.0, key=None):
        f = os.path.join(CKPT, "%s.npz" % key) if key else None
        if f and os.path.exists(f):
            return dict(np.load(f, allow_pickle=True))
        out, _ = plug_march(stations(K, yscale), start_line(N), qpa,
                            tab if tab_r is None else tab_r, 1.0)
        res = dict(wall=np.array(out["wall"]),
                   edge=np.array(out["edge"]),
                   last_col=np.array(out["last_col"]),
                   mesh=np.array(out["mesh_pts"]),
                   cert=np.array([out["cert_worst"],
                                  out["cert_n"]]))
        if f:
            np.savez_compressed(f, **res)
        return res

    KC, NC = 81, 33
    KF, NF = 161, 65
    out_c = run(KC, NC, key="blend_K%d" % KC)
    out_f = run(KF, NF, key="blend_K%d" % KF)
    print("  cert: coarse %.3f (n=%d) fine %.3f (n=%d)"
          % (out_c["cert"][0], out_c["cert"][1], out_f["cert"][0],
             out_f["cert"][1]))
    check("G-2 all cells Newton-certified (both resolutions)",
          out_c["cert"][0] <= 1.0 and out_f["cert"][0] <= 1.0)

    # ---- G-3: wall pressure vs GENO's wall ------------------------
    def wall_p(out):
        w = out["wall"]
        q = np.hypot(w[:, 2], w[:, 3])
        return w[:, 0], np.array(A1.state_q(jnp.array(q), ta)[1])
    xc, pc = wall_p(out_c)
    xf, pf = wall_p(out_f)
    pf_i = np.interp(xc, xf, pf)
    pg = np.interp(xc, wall[:, 0], wall[:, 5])
    dev = np.abs(pf_i - pg) / pg
    frac_w = float((dev <= TH_WALL).mean())
    print("  G-3 wall pressure: %.1f%% of %d stations within %.1e"
          " (median %.2e, max %.2e; coarse-fine Richardson %.2e)"
          % (100 * frac_w, len(xc), TH_WALL, np.median(dev),
             dev.max(), np.median(np.abs(pc - pf_i) / pg)))
    check("G-3 wall pressure matches GENO within the declared"
          " 3e-3 (>= 95%)", frac_w >= 0.95)

    # ---- G-4: settled interior field at GENO's phase-1 nodes ------
    from scipy.interpolate import griddata

    def interp_field(out, pts):
        mp = out["mesh"]
        u = griddata(mp[:, :2], mp[:, 2], pts, method="linear")
        v = griddata(mp[:, :2], mp[:, 3], pts, method="linear")
        return u, v

    nx, ny = ph1[:, 2], ph1[:, 3]
    yiv = np.interp(nx, ivl[:, 0], ivl[:, 1])
    ywa = np.interp(nx, wall[:, 0], wall[:, 1])
    gap = yiv - ywa

    def node_sel(xlo, xhi, nmax):
        m = ((nx > xlo) & (nx < xhi)
             & (ny < yiv - 0.03 * gap) & (ny > ywa + 0.03 * gap))
        sel = np.where(m)[0]
        return sel[np.linspace(0, len(sel) - 1,
                               min(nmax, len(sel))).astype(int)]

    sel = node_sel(X_SETTLED, X_END - 0.02, 2500)
    pts = ph1[sel][:, 2:4]
    qg, tg = ph1[sel, 5], ph1[sel, 6]
    uf, vf = interp_field(out_f, pts)
    ok_n = ~np.isnan(uf)
    qf_ = np.hypot(uf, vf)
    tf_ = np.arctan2(vf, uf)
    dq_n = np.abs(qf_ - qg) / qg
    dt_n = np.abs(tf_ - tg)
    frac_f = float(((dq_n <= TH_Q) & (dt_n <= TH_TH))[ok_n].mean())
    print("  G-4 settled field (x > %.2f): %.1f%% of %d nodes"
          " within (q %.0e, th %.0e); q med %.2e p95 %.2e, th med"
          " %.2e p95 %.2e"
          % (X_SETTLED, 100 * frac_f, int(ok_n.sum()), TH_Q, TH_TH,
             np.median(dq_n[ok_n]), np.percentile(dq_n[ok_n], 95),
             np.median(dt_n[ok_n]), np.percentile(dt_n[ok_n], 95)))
    check("G-4 settled interior field matches GENO at its own"
          " nodes (>= 95%)", frac_f >= 0.95)
    # the transient zone, reported (not gated): the measured
    # cut-ingestion artifact of the near-lip fan curvature
    sel_t = node_sel(X0 + 0.01, X_SETTLED, 1500)
    ut, vt = interp_field(out_f, ph1[sel_t][:, 2:4])
    ok_t = ~np.isnan(ut)
    dtt = np.abs(np.arctan2(vt, ut) - ph1[sel_t, 6])
    print("  (transient zone x < %.2f: max |dth| %.2e, p95 %.2e —"
          " reported, see docstring)" % (X_SETTLED, dtt[ok_t].max(),
                                         np.percentile(dtt[ok_t],
                                                       95)))

    # ---- G-5/G-6: mass and thrust through the IVL segment ---------
    md_full, F_full = curve_fluxes(
        ivl[:, 0], ivl[:, 1], ivl[:, 2],
        ivl[:, 3] * np.cos(ivl[:, 4]), ivl[:, 3] * np.sin(ivl[:, 4]),
        ivl[:, 5])
    print("  calibration: full-IVL quadrature mdot %.6e (printed"
          " 2.419692e3), F %.6e (printed 7.057036e6)"
          % (md_full, F_full))
    mi = (ivl[:, 0] >= X0 + 0.02) & (ivl[:, 0] <= 0.90)
    gx, gy = ivl[mi, 0], ivl[mi, 1]
    gr, gV, gth, gp = ivl[mi, 2], ivl[mi, 3], ivl[mi, 4], ivl[mi, 5]
    md_g, F_g = curve_fluxes(gx, gy, gr, gV * np.cos(gth),
                             gV * np.sin(gth), gp)

    def ours_on_ivl(out):
        u, v = interp_field(out, np.stack([gx, gy], axis=1))
        ok = ~np.isnan(u)
        u = np.where(ok, u, gV * np.cos(gth))
        v = np.where(ok, v, gV * np.sin(gth))
        q = np.hypot(u, v)
        stt = A1.state_q(jnp.array(q), ta)
        md, F = curve_fluxes(gx, gy, np.array(stt[2]), u, v,
                             np.array(stt[1]))
        return md, F, int((~ok).sum())
    md_f, F_f, nnan = ours_on_ivl(out_f)
    print("  G-5 mass through IVL [%.2f, 0.90]: ours %.6e vs GENO"
          " %.6e (rel %.2e, %d NaN-filled)"
          % (X0 + 0.02, md_f, md_g, abs(md_f - md_g) / md_g, nnan))
    check("G-5 IVL mass flux matches within the declared 2.5e-3",
          abs(md_f - md_g) / md_g <= TH_IVL)
    print("  G-6 thrust through IVL [%.2f, 0.90]: ours %.6e vs"
          " GENO %.6e (rel %.2e)"
          % (X0 + 0.02, F_f, F_g, abs(F_f - F_g) / F_g))
    check("G-6 IVL thrust functional matches within the declared"
          " 2.5e-3", abs(F_f - F_g) / F_g <= TH_IVL)

    # ---- R-1: corrupted gamma ------------------------------------
    tab_b = A1.prep_tab(A1.build_tab_gconst(
        g=float(gam) * 1.01, Rg=float(Rg), ts=float(ts_eff),
        ps=float(ps_eff)))
    try:
        out_b = run(KC, NC, tab_r=tab_b, key="bad_gamma_K%d" % KC)
        xb, pb = wall_p(out_b)
        pb_i = np.interp(xc, xb, pb)
        frac_b = float((np.abs(pb_i - pg) / pg <= TH_WALL).mean())
        print("  R-1: corrupted gamma -> %.1f%% within threshold"
              % (100 * frac_b))
        bad1 = frac_b < 0.5
    except Exception as ex:                     # noqa: BLE001
        print("  R-1: corrupted gamma -> march failed (%s)"
              % type(ex).__name__)
        bad1 = True
    check("R-1 rejector: corrupted gamma collapses the wall"
          " agreement", bad1)

    # ---- R-2: corrupted contour ----------------------------------
    try:
        out_b2 = run(KC, NC, yscale=1.005, key="bad_wall_K%d" % KC)
        xb2, pb2 = wall_p(out_b2)
        pb2_i = np.interp(xc, xb2, pb2)
        frac_b2 = float((np.abs(pb2_i - pg) / pg <= TH_WALL).mean())
        print("  R-2: corrupted contour -> %.1f%% within threshold"
              % (100 * frac_b2))
        bad2 = frac_b2 < 0.5
    except Exception as ex:                     # noqa: BLE001
        print("  R-2: corrupted contour -> march failed (%s)"
              % type(ex).__name__)
        bad2 = True
    check("R-2 rejector: corrupted contour collapses the wall"
          " agreement", bad2)

    print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
