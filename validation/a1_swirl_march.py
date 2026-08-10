#!/usr/bin/env python3
"""A1 BRICK 2, STEP 12 [F2/A1]: FREE-VORTEX SWIRL — the certified
march extended to swirling exhaust, with the corpus's structural
guarantee (its statement N6-2) measured.

THE PHYSICS, IN FULL. An RDE exhaust carries an azimuthal (swirl)
velocity w. For a FREE VORTEX --- circulation y*w = Gamma, the same
constant everywhere --- three exact simplifications hold:
  (1) the azimuthal momentum equation is satisfied identically
      (y*w is conserved along streamlines, and it is already
      uniform);
  (2) with uniform total enthalpy and entropy, Crocco's theorem
      forces the MERIDIONAL flow to stay irrotational (the only
      possible vorticity is azimuthal, and V x omega = 0 then
      requires it to vanish);
  (3) the meridional (x, y) problem therefore keeps the ENTIRE
      certified characteristic structure --- same characteristic
      directions at the meridional Mach angle, same (u, v)
      compatibility coefficients --- with exactly two changes:
        state:  h = h0 - q_m^2/2 - Gamma^2/(2 y^2)
                (the swirl kinetic energy is a known function of
                position, so the gas state depends on y as well as
                the meridional speed), and
        source: c^2 v/y  ->  (c^2 + Gamma^2/y^2) v/y
                (the centrifugal pressure gradient adds to the
                axisymmetric source).
      That preservation-of-structure is the corpus's guarantee;
      beyond free vortex the flow turns rotational and belongs to
      the CFD-adjoint track (its identity N6-3).

IMPLEMENTATION. The state change costs nothing new: with the
augmented speed q_eff = sqrt(q_m^2 + Gamma^2/y^2) the energy
closure reads h = h0 - q_eff^2/2 --- the certified isentrope
machinery (state_q) applies verbatim to q_eff, and only the Mach
number is rebuilt as the MERIDIONAL M = q_m/c. The free edge keeps
its certified angle parameterization: p = pa fixes the TOTAL speed
q_eff = q_pa (the same scalar as without swirl), so the edge's
meridional speed is the explicit law q_m(y) = sqrt(q_pa^2 -
Gamma^2/y^2). The three cell processes (interior, prescribed-wall,
free jet) are mirrored with the swirl state and source, and run
through the UNCHANGED certified march driver via its cell seam
(plug_march(cells=, q_edge=) --- additive, defaults reproduce the
certified path; its oracle and axi suites re-run PASS after the
seam). The driver's foot search and Newton seeds keep the no-swirl
state as predictors --- they only bracket and seed; the residuals
decide.

WORLDS AND CHECKS:
  W-1  Gamma -> 0 regression: the swirl cells at Gamma = 0 must
       reproduce the certified cells' march on the same world at
       the Newton-tolerance scale (band 1e-9 relative: both solve
       identical equations to the per-cell certified tolerance;
       the only difference is sqrt(q^2) rounding in the augmented
       speed).
  W-2  the radial-equilibrium duct, an EXACT known answer: in a
       straight annular duct the exact swirling solution has
       UNIFORM axial speed and v = 0, with the whole radial
       structure (p, T, a, M varying across the duct) carried by
       the swirl term in the energy closure --- differentiating
       h0 = h + u^2/2 + Gamma^2/(2y^2) along y and subtracting
       radial equilibrium dp/dy = rho Gamma^2/y^3 gives du/dy = 0
       exactly. The march must PRESERVE this state (translation
       invariance): u drift, |v|, wall pressure and edge position
       are all checked against Richardson bands from station
       halving. This exercises the y-dependent state closure in
       every cell type.
  W-3  the expansion world (a smooth spike-like wall drop under
       the swirling stream, genuinely two-dimensional, v != 0):
       internal closures --- mass and pa-gauge AXIAL momentum
       (the centrifugal force is radial and the azimuthal
       momentum decouples, so the axial theorem is unchanged) ---
       within Richardson bands.
  W-4  two ALIVE controls on the expansion world: (i) swirl-alive:
       Gamma != 0 differs from Gamma = 0 beyond the pair's own
       Richardson band (the swirl matters); (ii) source-alive: the
       centrifugal source term deliberately dropped (state keeps
       Gamma, source loses it) differs beyond band (the new source
       is wired and material --- the equilibrium duct alone cannot
       see it, because there v = 0 multiplies it away).
  R-1  rejector: cells at a corrupted circulation (Gamma^2 x 1.10)
       marched on the true equilibrium data leave the W-2 bands.

Run:  .venv-a1/bin/python validation/a1_swirl_march.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1              # noqa: E402
from a1_plug_march import plug_march         # noqa: E402
from a1_freejet_unit import q_at_pa          # noqa: E402

import jax.numpy as jnp                       # noqa: E402

EPS = A1.EPS
K_RICH = A1.K_RICH
C_FLOOR = A1.C_FLOOR
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ----------------------------------------------------------------------
# the swirl state and coefficients (the two changes, and only those)
# ----------------------------------------------------------------------
def state_sw(q, y, G2, ta):
    """Meridional state under free-vortex swirl: thermodynamics from
    the augmented speed (total kinetic energy), Mach number from the
    meridional speed."""
    qeff = jnp.sqrt(q * q + G2 / (y * y))
    T, p, rho, c, gam, _ = A1.state_q(qeff, ta)
    return T, p, rho, c, gam, q / c


def _coef_sw(u, v, y, ta, delta, G2, G2s):
    """The certified _coef with the two swirl changes: state through
    the augmented speed (G2), source c^2 v/y -> (c^2 + G2s/y^2) v/y.
    G2s is separated from G2 only for the source-alive control."""
    q = jnp.sqrt(u * u + v * v)
    A = jnp.arctan2(v, u)
    _, _, _, c, _, M = state_sw(q, y, G2, ta)
    mu = jnp.arcsin(1.0 / M)
    lm = jnp.tan(A - mu)
    lp = jnp.tan(A + mu)
    qq = u * u - c * c
    s = delta * (c * c + G2s / (y * y)) * v / y
    return lm, lp, qq, 2.0 * u * v, s


def make_resid_interior_bu_sw(delta, G2, G2s):
    """Bottom-up interior cell, swirl coefficients (mirror of the
    certified make_resid_interior_bu). The compatibility rows are
    nondimensionalized by the (z-constant) parent speed scale: with
    mixed O(1)/O(u^2) rows the monotone-norm damped Newton can stall
    one step short of the root (measured: the position-correcting
    step trades a tiny compatibility increase against the O(1e-7)
    geometry fix and the argmin damping rejects it forever); a pure
    row scaling balances the norm without moving the root."""
    def resid(z, p, ta):
        x4, y4, u4, v4 = z
        x1, y1, u1, v1, x2, y2, u2, v2 = p
        sc = 1.0 / (u1 * u1 + v1 * v1)
        up, vp, yp = 0.5 * (u1 + u4), 0.5 * (v1 + v4), 0.5 * (y1 + y4)
        _, lp, qp, rp0, sp = _coef_sw(up, vp, yp, ta, delta, G2, G2s)
        rp = rp0 - qp * lp
        um, vm, ym = 0.5 * (u2 + u4), 0.5 * (v2 + v4), 0.5 * (y2 + y4)
        lm, _, qm, rm0, sm = _coef_sw(um, vm, ym, ta, delta, G2, G2s)
        rm = rm0 - qm * lm
        return jnp.array([
            (y4 - y1) - lp * (x4 - x1),
            (y4 - y2) - lm * (x4 - x2),
            sc * (qp * u4 + rp * v4
                  - (sp * (x4 - x1) + qp * u1 + rp * v1)),
            sc * (qm * u4 + rm * v4
                  - (sm * (x4 - x2) + qm * u2 + rm * v2)),
        ])
    return resid


def make_resid_wallbot_sw(delta, G2, G2s):
    """Bottom-wall cell, swirl coefficients (mirror of the certified
    make_resid_wallbot; same y-parameterized foot)."""
    def resid(z, p, ta):
        y2, u4 = z
        xA, yA, uA, vA, xB, yB, uB, vB, x4, y4, slope = p
        D = (y2 - yA) / (yB - yA)
        x2 = xA + D * (xB - xA)
        u2 = uA + D * (uB - uA)
        v2 = vA + D * (vB - vA)
        v4 = slope * u4
        sc = 1.0 / (uA * uA + vA * vA)
        um, vm = 0.5 * (u2 + u4), 0.5 * (v2 + v4)
        ym = 0.5 * (y2 + y4)
        lm, _, qm, rm0, sm = _coef_sw(um, vm, ym, ta, delta, G2, G2s)
        rm = rm0 - qm * lm
        return jnp.array([
            (y4 - y2) - lm * (x4 - x2),
            sc * ((qm + slope * rm) * u4
                  - (sm * (x4 - x2) + qm * u2 + rm * v2)),
        ])
    return resid


def make_resid_freejet_sw(delta, G2, G2s):
    """Free-jet cell, swirl form: p = pa fixes the TOTAL speed, so
    the meridional edge speed is the explicit law
    q_m(y4) = sqrt(qpa_tot^2 - G2/y4^2); the certified ANGLE
    parameterization is kept (the qpa slot of the parameter vector
    carries the total speed)."""
    def resid(z, p, ta):
        x4, y4, th4 = z
        x1, y1, u1, v1, x3, y3, u3, v3, qpa_tot = p
        q4 = jnp.sqrt(qpa_tot * qpa_tot - G2 / (y4 * y4))
        u4 = q4 * jnp.cos(th4)
        v4 = q4 * jnp.sin(th4)
        um, vm = 0.5 * (u1 + u4), 0.5 * (v1 + v4)
        ym = 0.5 * (y1 + y4)
        _, lp, qp, rp0, sp = _coef_sw(um, vm, ym, ta, delta, G2, G2s)
        rp = rp0 - qp * lp
        th3 = jnp.arctan2(v3, u3)
        thm = 0.5 * (th3 + th4)
        sc = 1.0 / (u1 * u1 + v1 * v1)
        return jnp.array([
            (y4 - y1) - lp * (x4 - x1),
            sc * ((qp * u4 + rp * v4)
                  - (sp * (x4 - x1) + qp * u1 + rp * v1)),
            (y4 - y3) - jnp.tan(thm) * (x4 - x3),
        ])
    return resid


def swirl_cells(delta, G2, G2s):
    t_int = A1.get_solver(("intbu_sw", delta, float(G2), float(G2s)),
                          lambda: make_resid_interior_bu_sw(
                              delta, G2, G2s))
    t_fj = A1.get_solver(("fj_sw", delta, float(G2), float(G2s)),
                         lambda: make_resid_freejet_sw(
                             delta, G2, G2s))
    t_wb = A1.get_solver(("wb_sw", delta, float(G2), float(G2s)),
                         lambda: make_resid_wallbot_sw(
                             delta, G2, G2s))
    return (t_int, t_fj, t_wb)


# ----------------------------------------------------------------------
# swirl-aware fluxes (mirror of col_fluxes/wall_push_poly with the
# y-dependent state)
# ----------------------------------------------------------------------
def col_fluxes_sw(col, ta, pa, G2):
    c = np.asarray(col)
    q = np.hypot(c[:, 2], c[:, 3])
    st = state_sw(jnp.array(q), jnp.array(c[:, 1]), G2, ta)
    p = np.array(st[1])
    rho = np.array(st[2])
    dx = np.diff(c[:, 0])
    dy = np.diff(c[:, 1])
    um = 0.5 * (c[1:, 2] + c[:-1, 2])
    vm = 0.5 * (c[1:, 3] + c[:-1, 3])
    rm = 0.5 * (rho[1:] + rho[:-1])
    pm = 0.5 * (p[1:] + p[:-1])
    w = 2.0 * np.pi * 0.5 * (c[1:, 1] + c[:-1, 1])
    dmd = rm * (um * dy - vm * dx) * w
    return (float(np.sum(dmd)),
            float(np.sum(um * dmd + (pm - pa) * dy * w)))


def wall_push_sw(wall, ta, pa, G2):
    c = np.asarray(wall)
    q = np.hypot(c[:, 2], c[:, 3])
    st = state_sw(jnp.array(q), jnp.array(c[:, 1]), G2, ta)
    p = np.array(st[1])
    dy = np.diff(c[:, 1])
    pm = 0.5 * (p[1:] + p[:-1])
    w = 2.0 * np.pi * 0.5 * (c[1:, 1] + c[:-1, 1])
    return float(np.sum((pm - pa) * dy * w))


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    print("== A1 brick 2 step 12: free-vortex swirl march"
          " [F2/A1] ==")
    from scipy.optimize import brentq
    tb = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tb)
    as_ = tb["_as"]

    # ---- the posed swirling stream --------------------------------
    Y1, Y2 = 1.0, 1.6
    # meridional speed: M_m ~ 1.7 at the outer radius (least swirl
    # energy there -> lowest M_m); Gamma: w/u = 0.35 at the inner
    def Mm_of(q, y, G2):
        return float(state_sw(jnp.float64(q), jnp.float64(y), G2,
                              ta)[5])
    u0 = brentq(lambda q: Mm_of(q, Y2, 0.0) - 1.7, 1.05 * as_,
                3.2 * as_, xtol=1e-11)
    GAM = 0.35 * u0 * Y1
    G2 = GAM * GAM
    Tin = float(state_sw(jnp.float64(u0), jnp.float64(Y1), G2,
                         ta)[0])
    print("  duct: u0 %.3f  Gamma %.3f (w/u %.2f at y1)  M_m"
          " %.3f..%.3f  T(y1) %.1f K" %
          (u0, GAM, GAM / Y1 / u0, Mm_of(u0, Y1, G2),
           Mm_of(u0, Y2, G2), Tin))
    pa_eq = float(state_sw(jnp.float64(u0), jnp.float64(Y2), G2,
                           ta)[1])
    p_w_eq = float(state_sw(jnp.float64(u0), jnp.float64(Y1), G2,
                            ta)[1])
    qpa_tot = float(np.sqrt(u0 * u0 + G2 / (Y2 * Y2)))

    def q_edge_law(G2v):
        return lambda yy: jnp.sqrt(qpa_tot * qpa_tot
                                   - G2v / (yy * yy))

    X_END = 1.5

    def start_duct(N):
        yline = np.linspace(Y1, Y2, N)
        return (0.0, yline, np.full(N, u0), np.zeros(N))

    def duct_stations(K):
        sx = np.linspace(0, X_END, K)[1:]
        return (jnp.array(sx), jnp.array(np.full(K - 1, Y1)),
                jnp.array(np.zeros(K - 1)))

    def run(stations, start, G2c, G2s, K, N):
        out, _ = plug_march(stations, start, qpa_tot, tb, 1.0,
                            cells=swirl_cells(1.0, G2c, G2s),
                            q_edge=q_edge_law(G2c))
        return out

    # ---- W-1: Gamma -> 0 regression through the seam --------------
    # same (planar-free) duct world at Gamma = 0, certified cells vs
    # swirl cells; both solve identical equations to the certified
    # per-cell Newton tolerance, so the results must agree at that
    # scale (band 1e-9 relative — the augmented-speed sqrt rounding)
    def start0(N):
        yline = np.linspace(Y1, Y2, N)
        return (0.0, yline, np.full(N, u0), np.zeros(N))
    qpa0 = float(A1.state_q(jnp.float64(u0), ta)[1])
    qpa0_q = q_at_pa(qpa0, ta, as_)
    st_c = duct_stations(41)
    out_ref, _ = plug_march(st_c, start0(17), qpa0_q, tb, 1.0)
    out_sw0, _ = plug_march(st_c, start0(17), qpa0_q, tb, 1.0,
                            cells=swirl_cells(1.0, 0.0, 0.0),
                            q_edge=None)
    d_reg = float(np.max(np.abs(np.array(out_ref["last_col"])
                                - np.array(out_sw0["last_col"]))))
    band_reg = 1e-9 * u0
    print("  W-1: Gamma=0 swirl cells vs certified cells: max"
          " last-col diff %.2e (band %.2e)" % (d_reg, band_reg))
    check("W-1 Gamma -> 0 reduces to the certified march (Newton"
          " scale)", d_reg <= band_reg)

    # ---- W-2: the radial-equilibrium duct, exact answer -----------
    out_c = run(duct_stations(41), start_duct(17), G2, G2, 41, 17)
    out_f = run(duct_stations(81), start_duct(33), G2, G2, 81, 33)
    print("  cert: coarse %.3f fine %.3f" % (out_c["cert_worst"],
                                             out_f["cert_worst"]))
    check("W-2a all cells Newton-certified (swirl, both"
          " resolutions)", out_c["cert_worst"] <= 1.0
          and out_f["cert_worst"] <= 1.0)

    def duct_errs(out):
        col = np.array(out["last_col"])
        du = np.max(np.abs(np.hypot(col[:, 2], col[:, 3]) - u0)) / u0
        dv = np.max(np.abs(col[:, 3])) / u0
        w = np.array(out["wall"])
        qw = np.hypot(w[:, 2], w[:, 3])
        pw = np.array(state_sw(jnp.array(qw), jnp.array(w[:, 1]),
                               G2, ta)[1])
        dp = np.max(np.abs(pw - p_w_eq)) / p_w_eq
        de = np.max(np.abs(np.array(out["edge"])[:, 1] - Y2)) / Y2
        return np.array([du, dv, dp, de])
    e_c = duct_errs(out_c)
    e_f = duct_errs(out_f)
    band = K_RICH * np.abs(e_c - e_f) + C_FLOOR * EPS
    print("  W-2 equilibrium preserved: du/u %.2e dv/u %.2e"
          " dp_w/p %.2e dy_e/y %.2e (bands %.1e %.1e %.1e %.1e)"
          % (*e_f, *band))
    check("W-2b exact radial-equilibrium state preserved within"
          " Richardson bands", bool(np.all(e_f <= band)))

    # ---- W-3: the expansion world, internal closures --------------
    def bump_stations(K):
        sx = np.linspace(0, X_END, K)[1:]
        t = np.clip((sx - 0.25) / 0.75, 0.0, 1.0)
        s = t * t * (3.0 - 2.0 * t)               # smoothstep
        ds = np.where((sx > 0.25) & (sx < 1.0),
                      6.0 * t * (1.0 - t) / 0.75, 0.0)
        AMP = 0.18
        return (jnp.array(sx), jnp.array(Y1 - AMP * s),
                jnp.array(-AMP * ds))
    outb_c = run(bump_stations(41), start_duct(17), G2, G2, 41, 17)
    outb_f = run(bump_stations(81), start_duct(33), G2, G2, 81, 33)
    check("W-3a all cells Newton-certified (expansion world)",
          outb_c["cert_worst"] <= 1.0 and outb_f["cert_worst"]
          <= 1.0)
    stline = np.stack([np.zeros(801),
                       np.linspace(Y1, Y2, 801),
                       np.full(801, u0), np.zeros(801)], axis=1)
    md0, Fin = col_fluxes_sw(stline, ta, pa_eq, G2)

    def closures(out):
        md, Fout = col_fluxes_sw(np.array(out["last_col"]), ta,
                                 pa_eq, G2)
        wallpoly = np.vstack([stline[:1], np.array(out["wall"])])
        push = wall_push_sw(wallpoly, ta, pa_eq, G2)
        return md, Fout - Fin + push
    md_c, Rm_c = closures(outb_c)
    md_f, Rm_f = closures(outb_f)
    band_m = K_RICH * abs(md_c - md_f) + C_FLOOR * EPS * abs(md0)
    print("  W-3 mass: exit %.6e vs start %.6e (|d| %.2e, band"
          " %.2e)" % (md_f, md0, abs(md_f - md0), band_m))
    check("W-3b mass conserved within band (swirling 2D world)",
          abs(md_f - md0) <= band_m)
    band_F = K_RICH * abs(Rm_c - Rm_f) + C_FLOOR * EPS * abs(Fin)
    print("  W-3 axial momentum: closure %.4e (coarse %.4e) vs"
          " band %.4e on F_in %.4e" % (Rm_f, Rm_c, band_F, Fin))
    check("W-3c pa-gauge axial momentum closes within band",
          abs(Rm_f) <= band_F)

    # ---- W-4: the two alive controls ------------------------------
    def wall_q_end(out):
        w = np.array(out["wall"])
        return float(np.hypot(w[-1, 2], w[-1, 3]))
    wq_c, wq_f = wall_q_end(outb_c), wall_q_end(outb_f)
    band_q = K_RICH * abs(wq_c - wq_f) + 64 * EPS * wq_f
    out_g0, _ = plug_march(bump_stations(41), start_duct(17),
                           qpa0_q, tb, 1.0)
    d_alive = abs(wall_q_end(out_g0) - wq_c)
    print("  W-4i swirl-alive: wall q at x_end, Gamma vs 0: |d|"
          " %.3e (band %.2e)" % (d_alive, band_q))
    check("W-4i swirl changes the flow beyond band (swirl alive)",
          d_alive > band_q)
    outb_ns = run(bump_stations(41), start_duct(17), G2, 0.0, 41,
                  17)
    d_src = abs(wall_q_end(outb_ns) - wq_c)
    print("  W-4ii source-alive: centrifugal source dropped: |d|"
          " %.3e (band %.2e)" % (d_src, band_q))
    check("W-4ii the centrifugal source term is wired and material",
          d_src > band_q)

    # ---- R-1: corrupted circulation rejector ----------------------
    out_bad = run(duct_stations(41), start_duct(17), 1.10 * G2,
                  1.10 * G2, 41, 17)
    e_bad = duct_errs(out_bad)
    print("  R-1: corrupted Gamma^2 x1.10 on true data: du/u %.2e"
          " dp_w/p %.2e (bands %.1e %.1e)" % (e_bad[0], e_bad[2],
                                              band[0], band[2]))
    check("R-1 rejector: corrupted circulation leaves the"
          " equilibrium bands", bool(np.any(e_bad > band)))

    print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
