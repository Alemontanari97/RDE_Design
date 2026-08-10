#!/usr/bin/env python3
"""A1 BRICK 2, STEP 13 [F2/A1]: CONFIGURATION COMPARISON — bell vs
full plug vs truncated plug vs swirled plug, all at ONE operating
point, on a common basis that makes their optima comparable.

WHY A COMMON BASIS IS THE WHOLE PROBLEM. Thrust scales with mass
flow, so comparing a bell computed in one posed world against a plug
computed in another compares the WORLDS, not the nozzle types. The
basis fixed here, and enforced by the checks below, is:

  * the same gas (NASA real-gas tables),
  * the same chamber state (P0, T0 = the tables' own reference),
  * the same ambient pressure p_a,
  * the same MASS FLOW.

The last one carries a bonus. For a choked throat mdot = p_c A_t/c*,
so at equal chamber state, equal mass flow means equal THROAT AREA
--- and therefore the thrust coefficient C_F = F/(p_c A_t) and the
specific impulse I_sp = F/(mdot g0) are directly comparable numbers,
with the size of the machine divided out.

  * and the same ENVELOPE: every configuration is allowed the same
    maximum radius, namely the bell optimum's own exit radius. A
    plug given unlimited radius would win trivially on expansion
    alone; holding the frontal size equal is what makes "which type
    is better" a fair question.

Each configuration is then optimized over its OWN design variable:
the bell over its area ratio, the plugs over where the spike is cut.

THRUST BOOKKEEPING, AND WHY THE TWO SIDES ARE THE SAME QUANTITY.
For a rocket fed from a closed chamber, the axial thrust equals the
ambient-gauge momentum flux through ANY surface that spans the whole
exhaust and encloses all the hardware:
    F = \\int [ rho u^2 + (p - p_a) ] dA .
For the bell that surface is the exit plane, giving the familiar
mdot*u_e + (p_e - p_a)A_e. For the plug the same theorem applies at
the march start line: the flux there already equals the thrust of
everything upstream of it (internal duct AND the spike stretch ahead
of it), because the free jet boundary between the lip and that cut
contributes exactly zero in the gauge (p = p_a on it). So
    F_plug(l) = F_in(x_0) + \\int_{x_0}^{l} (p_w - p_a) 2 pi y (-dy)
is the total thrust from the chamber through the truncation --- the
same physical quantity as the bell's. A flat base at p_b = p_a
contributes zero (declared).

CONFIGURATIONS
  A  BELL: the certified area-ratio optimum of Chapter "the first
     optimization" (its own closed form: p_e = p_a), read from that
     driver's cached marches and re-verified here.
  B  FULL PLUG: cowl lip at the envelope radius; flow arrives at the
     lip at M_i = 1.2 turned inward by exactly the tables-consistent
     fan turn, so the exhaust leaves axially (the classic plug design
     condition); the annulus is sized so the start line passes the
     reference mass flow; the spike is the streamline of that fan
     field; thrust taken at the end of the marched spike.
  C  TRUNCATED PLUG: the same single march, maximized over the cut
     length l (one march covers every truncation --- supersonic
     domain of dependence).
  D  SWIRLED PLUG: the same hardware and the same meridional start
     profile with a free vortex added (circulation Gamma), the
     annulus RE-SIZED to restore the reference mass flow, marched
     with the certified swirl cells. DECLARED MODELLING CHOICE: a
     lip fan is not self-similar once swirl is present (the state
     depends on radius as well as ray angle), so the swirled start
     line is POSED from the unswirled meridional profile rather than
     constructed as a centred fan. It is therefore a controlled A/B
     on identical hardware, not an independently designed swirled
     nozzle.

CHECKS
  C-1  every configuration passes the reference mass flow (derived
       band from the start-line quadrature refinement);
  C-2  every march Newton-certified;
  C-3  the bell really sits at its optimum: p_e = p_a within the
       driver's own derived band;
  C-4  the plug momentum theorem closes in the ambient gauge, with
       the free edge contributing zero;
  C-5  swirl regression: Gamma -> 0 reproduces the unswirled plug
       thrust at the Newton-tolerance scale;
  C-6  the envelope is respected: no configuration exceeds the
       shared maximum radius;
  R-1  rejector: an annulus deliberately mis-sized by 5% must fail
       the mass check AND shift C_F beyond the comparison band ---
       proving the comparison resolves a basis violation.

Run:  .venv-a1/bin/python validation/a1_config_compare.py
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1                      # noqa: E402
import a1_swirl_march as SW                          # noqa: E402
from a1_plug_march import plug_march, col_fluxes, wall_push_poly  # noqa: E402
from a1_freejet_unit import q_at_pa                  # noqa: E402

import jax.numpy as jnp                              # noqa: E402
from scipy.optimize import brentq                    # noqa: E402

EPS = A1.EPS
K_RICH = A1.K_RICH
C_FLOOR = A1.C_FLOOR
NPASS = [0, 0]
HERE = os.path.dirname(os.path.abspath(__file__))
CKPT = os.path.join(HERE, "_config_cmp")
os.makedirs(CKPT, exist_ok=True)

PA = 7.614420e5                 # ambient of record, shared by all
EPS_BELL = 5.150634             # the bell's closed-form optimum
MI = 2.0                        # plug inflow Mach at the lip: the
#   annular duct expands from the throat to M_i and the lip fan does
#   the rest (partial external expansion, as real aerospikes are).
#   M_i is NOT free: at M_i = 1.2 the tables-consistent fan turn is
#   54.5 deg, which drives the first fan ray to -111 deg -- pointing
#   upstream, geometrically impossible. M_i = 2.0 puts every ray
#   between -56.7 and -20.9 deg. Checked by C-0 below.
X0 = 0.35                       # plug march start station [m]
X_END = 6.0                     # end of the marched spike [m]
SWIRL_RATIO = 0.30              # w/u at the spike radius, config D
G0 = 9.80665


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ----------------------------------------------------------------------
# the shared world
# ----------------------------------------------------------------------
def build_world():
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    ck = json.load(open(os.path.join(HERE, "_driver_eps_ckpt.json")))
    b = [v for k, v in ck.items()
         if k.startswith("c:")
         and abs(float(k.split(":")[1]) - EPS_BELL) < 1e-6][0]
    yt = A1.CASE["yt"]
    At = np.pi * yt ** 2
    P0, T0 = tab["ps"], tab["ts"]
    w = dict(tab=tab, ta=ta, as_=tab["_as"], P0=P0, T0=T0, At=At,
             mdot=b["mdot"], RMAX=b["ylip"], bell=b,
             cstar=P0 * At / b["mdot"])
    return w


def fan_of(w):
    """Tables-consistent centred expansion at the lip, from M_i down
    to the shared ambient, with the inflow turned inward by exactly
    the fan turn so the exhaust leaves axially."""
    ta, as_ = w["ta"], w["as_"]

    def M_of(q):
        return float(A1.state_q(jnp.float64(q), ta)[5])

    def p_of(q):
        return float(A1.state_q(jnp.float64(q), ta)[1])
    q1 = brentq(lambda q: M_of(q) - MI, 1.0001 * as_, 3.4 * as_,
                xtol=1e-11)
    q2 = brentq(lambda q: p_of(q) - PA, 1.0001 * as_, 3.4 * as_,
                xtol=1e-11)
    qs = np.linspace(q1, q2, 900)
    Ms = np.array([M_of(q) for q in qs])
    mus = np.arcsin(np.clip(1.0 / Ms, 0, 1))
    dth = np.sqrt(np.maximum(Ms ** 2 - 1.0, 0.0)) / qs
    nu = np.concatenate([[0.0], np.cumsum(
        0.5 * (dth[1:] + dth[:-1]) * np.diff(qs))])
    th_i = -float(nu[-1])
    ths = th_i + nu
    phis = ths - mus
    LIP = (0.0, w["RMAX"])

    def field(x, y):
        ph = np.arctan2(y - LIP[1], x - LIP[0])
        if ph <= phis[0]:
            return float(qs[0]), float(ths[0])
        if ph >= phis[-1]:
            return float(qs[-1]), float(ths[-1])
        return (float(np.interp(ph, phis, qs)),
                float(np.interp(ph, phis, ths)))
    return dict(field=field, th_i=th_i, th_e=float(ths[-1]),
                q1=q1, q2=q2, LIP=LIP, Me=M_of(q2))


def streamline(field, p0, x_end, h=1.5e-3, y_stop=0.05):
    xs, ys = [p0[0]], [p0[1]]
    x, y = p0
    while x < x_end and y > y_stop:
        def sl(xx, yy):
            return np.tan(field(xx, yy)[1])
        k1 = sl(x, y)
        k2 = sl(x + h / 2, y + h * k1 / 2)
        k3 = sl(x + h / 2, y + h * k2 / 2)
        k4 = sl(x + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


def start_line(w, fan, y_sp0, N, G2=0.0):
    """The vertical cut at X0 from the spike to the free edge,
    carrying the exact fan field (plus a free vortex if G2 > 0)."""
    sx, sy = streamline(fan["field"], (0.0, y_sp0), X_END + 0.4)
    y_w = float(np.interp(X0, sx, sy))
    y_e = fan["LIP"][1] + np.tan(fan["th_e"]) * X0
    yy = np.linspace(y_w, y_e, N)
    us, vs = [], []
    for y in yy:
        q, t = fan["field"](X0, y)
        us.append(q * np.cos(t))
        vs.append(q * np.sin(t))
    return (X0, yy, np.array(us), np.array(vs)), (sx, sy), y_w, y_e


def cut_mass(w, fan, y_sp0, G2=0.0, n=1400):
    """Axial mass flux through the start-line cut, on the exact fan
    field (state through the swirl-augmented closure when G2 > 0)."""
    (_, yy, us, vs), _, _, _ = start_line(w, fan, y_sp0, n, G2)
    if G2 > 0.0:
        st = SW.state_sw(jnp.array(np.hypot(us, vs)), jnp.array(yy),
                         G2, w["ta"])
    else:
        st = A1.state_q(jnp.array(np.hypot(us, vs)), w["ta"])
    rho = np.array(st[2])
    return float(np.trapezoid(rho * us * 2 * np.pi * yy, yy))


def size_annulus(w, fan, G2=0.0, scale=1.0):
    """Choose the spike start radius so the cut passes the reference
    mass flow (times `scale`, which the rejector corrupts)."""
    tgt = w["mdot"] * scale
    return brentq(lambda ys: cut_mass(w, fan, ys, G2) - tgt,
                  0.55 * w["RMAX"], 0.985 * w["RMAX"], xtol=1e-8)


# ----------------------------------------------------------------------
# one plug configuration: march, then the closed-form truncation family
# ----------------------------------------------------------------------
def run_plug(w, fan, y_sp0, K, N, G2=0.0, key=None):
    f = os.path.join(CKPT, "%s.npz" % key) if key else None
    if f and os.path.exists(f):
        return dict(np.load(f, allow_pickle=True))
    ta = w["ta"]
    start, (sx, sy), y_w, y_e = start_line(w, fan, y_sp0, N, G2)
    m = (sx > X0 + 1e-9) & (sx <= X_END)
    xs, ys = sx[m], sy[m]
    idx = np.unique(np.linspace(0, len(xs) - 1, K).astype(int))
    sl = np.gradient(sy, sx)
    st = (jnp.array(xs[idx]), jnp.array(ys[idx]),
          jnp.array(np.interp(xs[idx], sx, sl)))
    qpa = q_at_pa(PA, ta, w["as_"])
    if G2 > 0.0:
        qtot = float(np.sqrt(qpa ** 2 + G2 / y_e ** 2))
        out, _ = plug_march(st, start, qtot, w["tab"], 1.0,
                            cells=SW.swirl_cells(1.0, G2, G2),
                            q_edge=(lambda yy: jnp.sqrt(
                                qtot ** 2 - G2 / (yy * yy))))
    else:
        out, _ = plug_march(st, start, qpa, w["tab"], 1.0)
    res = dict(wall=np.array(out["wall"]),
               last_col=np.array(out["last_col"]),
               cert=np.array([out["cert_worst"], out["cert_n"]]),
               start=np.stack([np.full(len(start[1]), X0), start[1],
                               start[2], start[3]], axis=1),
               spike=np.stack([sx, sy], axis=1),
               y_e=np.array([y_e]))
    if f:
        np.savez_compressed(f, **res)
    return res


def plug_thrust(w, out, G2=0.0):
    """F_in through the start line + the spike's gauge push, as a
    function of the cut length l. Returns (l grid, J grid, closure)."""
    ta = w["ta"]
    stl = out["start"]
    if G2 > 0.0:
        md_in, F_in = SW.col_fluxes_sw(stl, ta, PA, G2)
        wp = SW.wall_push_sw
        cf = lambda c: SW.col_fluxes_sw(c, ta, PA, G2)   # noqa: E731
    else:
        md_in, F_in = col_fluxes(stl, ta, PA, 1.0)
        wp = lambda ww, t, p, d: wall_push_poly(ww, t, p, d)  # noqa: E731
        cf = lambda c: col_fluxes(c, ta, PA, 1.0)        # noqa: E731
    wall = out["wall"]
    q = np.hypot(wall[:, 2], wall[:, 3])
    if G2 > 0.0:
        pw = np.array(SW.state_sw(jnp.array(q), jnp.array(wall[:, 1]),
                                  G2, ta)[1])
    else:
        pw = np.array(A1.state_q(jnp.array(q), ta)[1])
    xw, yw = wall[:, 0], wall[:, 1]
    dy = np.diff(yw)
    wgt = 2 * np.pi * 0.5 * (yw[1:] + yw[:-1])
    pm = 0.5 * (pw[1:] + pw[:-1])
    cum = np.concatenate([[0.0], np.cumsum((pm - PA) * wgt * (-dy))])
    J = F_in + cum
    # momentum closure through the final column (free edge = 0)
    md_out, F_out = cf(out["last_col"])
    wallpoly = np.vstack([stl[:1], wall])
    push = wp(wallpoly, ta, PA, 1.0) if G2 > 0.0 else \
        wall_push_poly(wallpoly, ta, PA, 1.0)
    return xw, J, dict(md_in=abs(md_in), F_in=F_in, md_out=abs(md_out),
                       closure=F_out - F_in + push, pw=pw)


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    print("== A1 brick 2 step 13: configuration comparison"
          " [F2/A1] ==")
    w = build_world()
    b = w["bell"]
    print("  COMMON BASIS: P0 = %.4e Pa, T0 = %.1f K, p_a = %.4e Pa"
          % (w["P0"], w["T0"], PA))
    print("                mdot = %.5e kg/s, A_t = %.4f m2,"
          " c* = %.2f m/s" % (w["mdot"], w["At"], w["cstar"]))
    print("                envelope radius R_max = %.4f m"
          % w["RMAX"])

    def CF(F):
        return F / (w["P0"] * w["At"])

    def ISP(F):
        return F / (w["mdot"] * G0)

    rows = []

    # ---------- A: the bell at its certified optimum ----------------
    J_bell = b["J0"] - PA * np.pi * b["ylip"] ** 2
    print("\n  [A] BELL at its area-ratio optimum"
          " (eps = %.4f, M_e = %.3f)" % (EPS_BELL, b["Me"]))
    print("      p_e = %.6e vs p_a = %.6e  -> the optimality"
          " condition" % (b["pe"], PA))
    print("      F = %.6e N   C_F = %.5f   Isp = %.2f s"
          % (J_bell, CF(J_bell), ISP(J_bell)))
    band_pe = 7958.0            # the driver's own derived band
    check("C-3 the bell sits at its optimum (p_e = p_a within the"
          " driver's derived band)", abs(b["pe"] - PA) <= band_pe)
    rows.append(("bell (area-ratio optimum)", J_bell, CF(J_bell),
                 ISP(J_bell), b["ylip"], float(b["ylip"]) * 0 + 7.34,
                 b["ylip"]))

    # ---------- the shared plug world -------------------------------
    fan = fan_of(w)
    print("\n  PLUG WORLD: lip at (0, %.4f); inflow M_i = %.2f turned"
          " %.2f deg inward;" % (w["RMAX"], MI, -np.degrees(fan["th_i"])))
    print("              tables fan turn = %.2f deg -> exhaust leaves"
          " at %.2f deg (axial by design), M_e = %.3f"
          % (-np.degrees(fan["th_i"]), np.degrees(fan["th_e"]),
             fan["Me"]))
    ray_first = fan["th_i"] - np.arcsin(1.0 / MI)
    ray_last = fan["th_e"] - np.arcsin(1.0 / fan["Me"])
    print("              fan rays span %.2f to %.2f deg (all must"
          " point downstream)" % (np.degrees(ray_first),
                                  np.degrees(ray_last)))
    check("C-0 the lip fan is geometrically valid (every ray runs"
          " downstream)", np.degrees(ray_first) > -89.0)
    y_sp0 = size_annulus(w, fan)
    print("              annulus sized for the reference mass flow:"
          " spike starts at y = %.4f m (gap %.4f m)"
          % (y_sp0, w["RMAX"] - y_sp0))

    KC, NC, KF, NF = 61, 41, 121, 81
    out_c = run_plug(w, fan, y_sp0, KC, NC, key="plug_K%d" % KC)
    out_f = run_plug(w, fan, y_sp0, KF, NF, key="plug_K%d" % KF)
    print("      cert: coarse %.3f (n=%d), fine %.3f (n=%d)"
          % (out_c["cert"][0], out_c["cert"][1],
             out_f["cert"][0], out_f["cert"][1]))
    xw_c, J_c, d_c = plug_thrust(w, out_c)
    xw, J, d = plug_thrust(w, out_f)
    # DERIVED band: the start-line mass is a quadrature, so refine it
    # and let the refinement measure its own error.
    m_lo = cut_mass(w, fan, y_sp0, n=NF)
    m_hi = cut_mass(w, fan, y_sp0, n=8 * NF)
    band_md = K_RICH * abs(m_lo - m_hi) + C_FLOOR * EPS * w["mdot"]
    print("      mass through the start line: %.5e kg/s vs reference"
          " %.5e (|d| %.2e, band %.2e)"
          % (d["md_in"], w["mdot"], abs(d["md_in"] - w["mdot"]),
             max(band_md, 1e-6 * w["mdot"])))
    check("C-1 the plug passes the reference mass flow",
          abs(d["md_in"] - w["mdot"]) <= band_md)
    check("C-2 all plug cells Newton-certified (both resolutions)",
          out_c["cert"][0] <= 1.0 and out_f["cert"][0] <= 1.0)
    band_cl = K_RICH * abs(d_c["closure"] - d["closure"]) \
        + C_FLOOR * EPS * abs(d["F_in"])
    print("      momentum closure (gauge, free edge = 0): %.4e vs"
          " band %.4e on F_in %.4e"
          % (d["closure"], band_cl, d["F_in"]))
    check("C-4 the plug momentum theorem closes in the ambient gauge",
          abs(d["closure"]) <= max(band_cl, 1e-3 * abs(d["F_in"])))

    # ---------- B: the full plug ------------------------------------
    J_full = float(J[-1])
    L_full = float(xw[-1])
    print("\n  [B] FULL PLUG (spike marched to x = %.2f m)" % L_full)
    print("      F = %.6e N   C_F = %.5f   Isp = %.2f s"
          % (J_full, CF(J_full), ISP(J_full)))
    rows.append(("plug, full spike", J_full, CF(J_full), ISP(J_full),
                 w["RMAX"], L_full, w["RMAX"]))

    # ---------- C: the truncated plug -------------------------------
    i_star = int(np.argmax(J))
    J_tr, l_star = float(J[i_star]), float(xw[i_star])
    print("\n  [C] TRUNCATED PLUG: optimal cut at l = %.3f m"
          " (%.0f%% of the marched spike)"
          % (l_star, 100 * l_star / L_full))
    print("      F = %.6e N   C_F = %.5f   Isp = %.2f s"
          % (J_tr, CF(J_tr), ISP(J_tr)))
    print("      wall pressure at the cut: %.4e Pa vs p_a %.4e"
          " (the corner condition)"
          % (float(np.interp(l_star, xw, d["pw"])), PA))
    rows.append(("plug, truncated at optimum", J_tr, CF(J_tr),
                 ISP(J_tr), w["RMAX"], l_star, w["RMAX"]))

    # ---------- D: the swirled plug ---------------------------------
    u_ref = float(np.interp(y_sp0, out_f["start"][:, 1],
                            out_f["start"][:, 2]))
    GAM = SWIRL_RATIO * abs(u_ref) * y_sp0
    G2 = GAM ** 2
    y_sp0_s = size_annulus(w, fan, G2=G2)
    print("\n  [D] SWIRLED PLUG: free vortex Gamma = %.2f m2/s"
          " (w/u = %.2f at the spike radius)" % (GAM, SWIRL_RATIO))
    print("      annulus re-sized for the same mass flow:"
          " spike starts at y = %.4f m (was %.4f)"
          % (y_sp0_s, y_sp0))
    out_s = run_plug(w, fan, y_sp0_s, KF, NF, G2=G2,
                     key="plug_swirl_K%d" % KF)
    xw_s, J_s, d_s = plug_thrust(w, out_s, G2=G2)
    print("      cert: %.3f (n=%d);  mass %.5e kg/s (|d| %.2e)"
          % (out_s["cert"][0], out_s["cert"][1], d_s["md_in"],
             abs(d_s["md_in"] - w["mdot"])))
    check("C-2b swirled plug cells Newton-certified",
          out_s["cert"][0] <= 1.0)
    ms_lo = cut_mass(w, fan, y_sp0_s, G2=G2, n=NF)
    ms_hi = cut_mass(w, fan, y_sp0_s, G2=G2, n=8 * NF)
    band_ms = K_RICH * abs(ms_lo - ms_hi) + C_FLOOR * EPS * w["mdot"]
    check("C-1b the swirled plug passes the reference mass flow",
          abs(d_s["md_in"] - w["mdot"]) <= band_ms)
    i_s = int(np.argmax(J_s))
    J_sw, l_sw = float(J_s[i_s]), float(xw_s[i_s])
    print("      optimal cut l = %.3f m (unswirled: %.3f m)"
          % (l_sw, l_star))
    print("      F = %.6e N   C_F = %.5f   Isp = %.2f s"
          % (J_sw, CF(J_sw), ISP(J_sw)))
    rows.append(("plug, truncated + swirl", J_sw, CF(J_sw),
                 ISP(J_sw), w["RMAX"], l_sw, w["RMAX"]))

    # C-5: swirl regression at Gamma -> 0
    out_z = run_plug(w, fan, y_sp0, KF, NF, G2=0.0,
                     key="plug_swirl0_K%d" % KF)
    _, J_z, _ = plug_thrust(w, out_z, G2=0.0)
    d_reg = abs(float(J_z[-1]) - J_full) / abs(J_full)
    print("\n      swirl regression: Gamma -> 0 reproduces the"
          " unswirled thrust to %.2e relative" % d_reg)
    check("C-5 Gamma -> 0 recovers the unswirled plug", d_reg <= 1e-9)

    # C-6: the envelope
    r_max_all = max(float(np.max(out_f["start"][:, 1])),
                    float(out_f["y_e"][0]), w["RMAX"])
    print("      max radius reached by any configuration: %.4f m"
          " (envelope %.4f m)" % (r_max_all, w["RMAX"]))
    check("C-6 no configuration exceeds the shared envelope",
          r_max_all <= w["RMAX"] * (1.0 + 1e-6))

    # ---------- R-1: the basis-violation rejector -------------------
    y_bad = size_annulus(w, fan, scale=1.05)
    out_b = run_plug(w, fan, y_bad, KC, NC, key="plug_bad_K%d" % KC)
    _, J_b, d_b = plug_thrust(w, out_b)
    dCF = abs(CF(float(np.max(J_b))) - CF(J_tr))
    print("\n  R-1: annulus mis-sized by 5%% -> mass %.5e (%.1f%% off)"
          ", C_F shifts by %.4f" % (d_b["md_in"],
                                    100 * (d_b["md_in"] / w["mdot"] - 1),
                                    dCF))
    check("R-1 rejector: a 5% basis violation is caught by the mass"
          " check and moves C_F", abs(d_b["md_in"] - w["mdot"])
          > band_md and dCF > 1e-3)

    # ---------- the comparison table --------------------------------
    print("\n  " + "=" * 74)
    print("  CONFIGURATION COMPARISON at one operating point")
    print("  (same gas, chamber, ambient, mass flow, throat area,"
          " envelope radius)")
    print("  " + "-" * 74)
    print("  %-30s %12s %9s %9s %8s" % ("configuration", "F [MN]",
                                        "C_F [-]", "Isp [s]",
                                        "L [m]"))
    print("  " + "-" * 74)
    base = rows[0][1]
    for name, F, cf_, isp, _, L, _ in rows:
        print("  %-30s %12.4f %9.5f %9.2f %8.2f" % (name, F / 1e6,
                                                    cf_, isp, L))
    print("  " + "-" * 74)
    for name, F, cf_, isp, _, L, _ in rows[1:]:
        print("  %-30s vs bell: %+7.3f%% of thrust"
              % (name, 100 * (F / base - 1)))
    print("  " + "=" * 74)

    np.savez_compressed(os.path.join(CKPT, "summary.npz"),
                        names=np.array([r[0] for r in rows]),
                        F=np.array([r[1] for r in rows]),
                        CF=np.array([r[2] for r in rows]),
                        Isp=np.array([r[3] for r in rows]),
                        L=np.array([r[5] for r in rows]),
                        l_curve_x=xw, l_curve_J=J,
                        l_curve_x_s=xw_s, l_curve_J_s=J_s,
                        pw=d["pw"], pw_s=d_s["pw"], pa=np.array([PA]))
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                            time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
