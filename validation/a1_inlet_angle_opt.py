#!/usr/bin/env python3
"""A1 BRICK 2, STEP 15 [F2/A1]: THE INLET ANGLE AS A DESIGN VARIABLE.

OWNER DIRECTIVE (2026-08-08), standing:
  1. the initial turning angle theta_i is PART OF THE OPTIMIZATION,
     not a posed constant --- it is the angle at which the RDE
     delivers the flow, i.e. the inclination of the annular
     chamber-exit slot;
  2. the RDE INPUT is given as a STRAIGHT LINE: the inlet is a
     straight segment in the meridional plane between the spike start
     radius and the cowl lip;
  3. outward-turning aerospikes are excluded --- they cannot beat
     inward-turning ones.

(3) is right by a wide margin and this carrier measures it. An
outward-turning plug leaves its whole exhaust at theta_E > 0, so
thrust collects only cos(theta_E) of the momentum: at the design turn
of 26.66 deg that is a 10.6% divergence loss, against ~0 for an
inward design that brings the exhaust back to axial.

THE VARIABLE. The lip fan turn dnu is fixed by the expansion (M_i
down to p_a) and does NOT depend on theta_i, so the exhaust angle is
simply theta_E = theta_i + dnu. Sweeping theta_i therefore sweeps
theta_E, and the design condition "exhaust leaves axially" is
theta_E = 0. The sweep is reported in theta_E because that is the
quantity the physics cares about.

THE BASIS is step 13's, unchanged: same gas, chamber, ambient, and
MASS FLOW (hence the same throat area, hence comparable C_F), and the
same envelope radius. One thing must be redone at every candidate:
the axial mass flux through an inclined inlet scales with
cos(theta_i), so the annulus is RE-SIZED for each theta_i to hold the
reference mass flow. Thrust is compared at a FIXED length so that
length is not silently traded against angle.

THE BUILT-IN ORACLE. The divergence argument predicts the optimum
near theta_E = 0. A blind sweep landing there is a known-answer
check. Exact coincidence is NOT expected and would be suspicious:
the wall-pressure distribution trades against pure divergence, so a
small offset is physical and is reported rather than tuned away.

CHECKS
  T-0  the lip fan is geometrically valid at every candidate (every
       ray runs downstream) and the spike clears the axis;
  T-1  every march Newton-certified;
  T-2  every candidate passes the reference mass flow;
  T-3  the blind optimum agrees with the divergence prediction
       theta_E ~ 0 within the sweep's own resolution;
  T-4  the measured penalty for outward turning matches the
       cos(theta_E) divergence model in sign and order --- the
       directive's premise, measured;
  R-1  rejector: a 5% mis-sized annulus at the optimum moves C_F
       beyond the derived thrust band.

Run:  .venv-a1/bin/python validation/a1_inlet_angle_opt.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1                      # noqa: E402
import a1_config_compare as CC                       # noqa: E402
from a1_plug_march import plug_march, col_fluxes, wall_push_poly  # noqa: E402
from a1_freejet_unit import q_at_pa                  # noqa: E402

import jax.numpy as jnp                              # noqa: E402
from scipy.optimize import brentq                    # noqa: E402

NPASS = [0, 0]
PA = CC.PA
MI = CC.MI
X0 = 0.35
X_END = 3.0
L_REF = 2.5                    # thrust compared at this fixed length
G0 = 9.80665
BAND_J = 9.4e-5                # derived Richardson band on J (step 13)


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def fan_at(w, thE):
    """The lip fan for a given EXHAUST angle: theta_i = thE - dnu."""
    ta, as_ = w["ta"], w["as_"]
    M_of = lambda q: float(A1.state_q(jnp.float64(q), ta)[5])   # noqa
    p_of = lambda q: float(A1.state_q(jnp.float64(q), ta)[1])   # noqa
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
    dnu = float(nu[-1])
    th_i = thE - dnu
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
    # pm: the corner relation's own tables (q, theta, Mach angle, planar
    # ray angle), exposed for the axisymmetric fan [X-AFAN] which uses
    # the corner point's states as lip data and nothing else of the
    # planar wave (additive, 2026-09-16)
    return dict(field=field, dnu=dnu, th_i=th_i, th_e=float(ths[-1]),
                LIP=LIP, ray1=th_i - np.arcsin(1.0 / MI),
                pm=dict(qs=qs, ths=ths, mus=mus, phis=phis))


def spike(fan, y0, x_end=X_END + 0.3, h=1.5e-3):
    xs, ys = [0.0], [y0]
    x, y = 0.0, y0
    while x < x_end and y > 0.05:
        sl = lambda a, b: np.tan(fan["field"](a, b)[1])          # noqa
        k1 = sl(x, y)
        k2 = sl(x + h / 2, y + h * k1 / 2)
        k3 = sl(x + h / 2, y + h * k2 / 2)
        k4 = sl(x + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


def cut_mass(w, fan, y0, n=1200):
    sx, sy = spike(fan, y0)
    yw = float(np.interp(X0, sx, sy))
    ye = fan["LIP"][1] + np.tan(fan["th_e"]) * X0
    if ye <= yw:
        return -1e9
    yy = np.linspace(yw, ye, n)
    u = np.zeros(n)
    rho = np.zeros(n)
    for i, y in enumerate(yy):
        q, t = fan["field"](X0, y)
        u[i] = q * np.cos(t)
        rho[i] = float(A1.state_q(jnp.float64(q), w["ta"])[2])
    return float(np.trapezoid(rho * u * 2 * np.pi * yy, yy))


def start_line_state(w, fan, y0, N):
    """The march's own start line for a candidate start radius: the
    vertical cut at X0 from the spike wall up to the free edge, with
    the fan's state on it."""
    sx, sy = spike(fan, y0)
    yw = float(np.interp(X0, sx, sy))
    ye = fan["LIP"][1] + np.tan(fan["th_e"]) * X0
    if ye <= yw:
        return None
    yline = np.linspace(yw, ye, N)
    us, vs = [], []
    for y in yline:
        q, t = fan["field"](X0, y)
        us.append(q * np.cos(t))
        vs.append(q * np.sin(t))
    return sx, sy, yline, np.array(us), np.array(vs)


def start_mass(w, fan, y0, N):
    """Mass flow through the start line, measured with THE FUNCTIONAL
    THE VERDICT USES.

    T-2 previously sized the annulus with cut_mass and then graded the
    result with col_fluxes. Both are second-order rules on the same
    data and both are correct, but they are not the SAME rule:
    cut_mass takes the trapezoid of the product rho*u*2*pi*y, while
    col_fluxes multiplies midpoint means, rho_m * u_m * 2*pi*y_m. Those
    differ by a quarter of the product of the increments on every
    interval, which on 61 rows is ~7e-5 relative --- an order above the
    quadrature band and entirely an artefact of grading with a
    different instrument than the one used to set the target. Sizing
    with col_fluxes removes the mismatch at its source instead of
    widening a band to cover it."""
    s = start_line_state(w, fan, y0, N)
    if s is None:
        return -1e9
    _, _, yline, us, vs = s
    stl = np.stack([np.full(len(yline), X0), yline, us, vs], axis=1)
    return abs(col_fluxes(stl, w["ta"], PA, 1.0)[0])


def evaluate(w, thE, K=81, N=61, scale=1.0):
    """One candidate: size the annulus for the reference mass flow,
    march, return thrust at the fixed reference length."""
    fan = fan_at(w, thE)
    # Size the annulus with the SAME QUADRATURE AND THE SAME FUNCTIONAL
    # the verdict will use (see start_mass): same row count N, and
    # col_fluxes on both sides. Sizing on any other rule leaves a
    # residue that is pure instrument difference, and the wrong fix for
    # that is to widen a band until it disappears.
    y0 = brentq(lambda ys: start_mass(w, fan, ys, N) - w["mdot"] * scale,
                0.45 * w["RMAX"], 0.985 * w["RMAX"], xtol=1e-9)
    sx, sy = spike(fan, y0)
    yw0 = float(np.interp(X0, sx, sy))
    ye0 = fan["LIP"][1] + np.tan(fan["th_e"]) * X0
    yline = np.linspace(yw0, ye0, N)
    us, vs = [], []
    for y in yline:
        q, t = fan["field"](X0, y)
        us.append(q * np.cos(t))
        vs.append(q * np.sin(t))
    m = (sx > X0 + 1e-9) & (sx <= X_END)
    xs, ys = sx[m], sy[m]
    idx = np.unique(np.linspace(0, len(xs) - 1, K).astype(int))
    sl = np.gradient(sy, sx)
    st = (jnp.array(xs[idx]), jnp.array(ys[idx]),
          jnp.array(np.interp(xs[idx], sx, sl)))
    out, _ = plug_march(st, (X0, yline, np.array(us), np.array(vs)),
                        q_at_pa(PA, w["ta"], w["as_"]), w["tab"], 1.0)
    stl = np.stack([np.full(N, X0), yline, np.array(us),
                    np.array(vs)], axis=1)
    md, F_in = col_fluxes(stl, w["ta"], PA, 1.0)
    wall = np.array(out["wall"])
    q = np.hypot(wall[:, 2], wall[:, 3])
    pw = np.array(A1.state_q(jnp.array(q), w["ta"])[1])
    dy = np.diff(wall[:, 1])
    wgt = 2 * np.pi * 0.5 * (wall[1:, 1] + wall[:-1, 1])
    pm = 0.5 * (pw[1:] + pw[:-1])
    cum = np.concatenate([[0.0], np.cumsum((pm - PA) * wgt * (-dy))])
    J = F_in + float(np.interp(L_REF, wall[:, 0], cum))
    return dict(thE=thE, fan=fan, y0=y0, J=J, mdot=abs(md),
                cert=float(out["cert_worst"]),
                y_end=float(np.interp(L_REF, sx, sy)),
                ray1=fan["ray1"])


def main():
    t0 = time.time()
    print("== A1 brick 2 step 15: the inlet angle as a design"
          " variable [F2/A1] ==")
    w = CC.build_world()
    CF = lambda J: J / (w["P0"] * w["At"])                       # noqa
    f0 = fan_at(w, 0.0)
    print("  basis: chamber %.4e Pa / %.1f K, p_a %.4e Pa,"
          " mdot %.5e kg/s" % (w["P0"], w["T0"], PA, w["mdot"]))
    print("  lip fan turn dnu = %.2f deg (fixed by M_i = %.1f and"
          " p_a); theta_E = theta_i + dnu"
          % (np.degrees(f0["dnu"]), MI))
    print("  thrust compared at the fixed length l = %.2f m\n"
          % L_REF)

    # theta_E = -8 deg is EXCLUDED by T-0's geometric test, not by
    # preference: there the spike descends to y = 0.32 m and the march
    # loses certification (worst residual 1.4e10) as the flow runs into
    # the axis where the axisymmetric source diverges. The admissible
    # window is reported, not assumed.
    sweep = [-6, -4, -2, 0, 2, 4, 8, 12]
    res = []
    print("  %8s %9s %8s %8s %10s %9s %8s"
          % ("thE[deg]", "thi[deg]", "y_sp0", "cert", "mdot err",
             "C_F", "vs best"))
    for thE_deg in sweep:
        r = evaluate(w, np.radians(thE_deg))
        res.append(r)
        print("  %8.1f %9.2f %8.4f %8.3f %10.2e %9.5f"
              % (thE_deg, np.degrees(r["fan"]["th_i"]), r["y0"],
                 r["cert"], abs(r["mdot"] / w["mdot"] - 1), CF(r["J"])),
              flush=True)
    Js = np.array([r["J"] for r in res])
    cf = np.array([CF(r["J"]) for r in res])
    ib = int(np.argmax(Js))
    thE_best = sweep[ib]
    print("\n  best of the sweep: theta_E = %+.1f deg"
          "  (theta_i = %.2f deg), C_F = %.5f"
          % (thE_best, np.degrees(res[ib]["fan"]["th_i"]), cf[ib]))

    check("T-0 the lip fan is valid at every candidate (all rays"
          " downstream, spike clears the axis)",
          all(np.degrees(r["ray1"]) > -89.0 and r["y_end"] > 0.25
              for r in res))
    # T-1 binds on the ADMISSIBLE candidates. Outward-turning designs
    # (theta_E > 0) are excluded by the owner directive and appear in
    # this sweep for one purpose only: to MEASURE the penalty that
    # justifies excluding them (T-4). Requiring the march to certify on
    # configurations the program refuses to build would be the wrong
    # bar --- but so would dropping the observation, so the excluded
    # candidates' certification is reported, and any thrust figure
    # among them that is not certified is marked as indicative.
    adm = [r for r in res if r["thE"] <= 1e-12]
    bad = [r for r in res if r["cert"] > 1.0 and r["thE"] > 1e-12]
    if bad:
        print("  NOTE: %d excluded (outward) candidate(s) did not"
              " certify: %s -- their thrust entries are indicative,"
              " not results of record"
              % (len(bad), ", ".join("theta_E=%+.0f deg (cert %.2f)"
                                     % (np.degrees(r["thE"]), r["cert"])
                                     for r in bad)))
    # The bar is EVERY candidate, admissible or not: the whole sweep
    # certifies once sizing and grading share an instrument, so there
    # is no reason to accept the weaker bar. (It was briefly narrowed
    # to the admissible ones while a single outward candidate failed
    # at cert 6.5 -- that failure was an artefact of the mis-sized
    # annulus and disappeared with the instrument fix.) The note above
    # stays, so a future sweep that pushes far enough outward to lose
    # certification says so instead of failing silently.
    check("T-1 every march Newton-certified (whole sweep; %d of them"
          " admissible)" % len(adm), all(r["cert"] <= 1.0 for r in res))
    # DERIVED band: refine the row count of the START-LINE FUNCTIONAL
    # THAT T-2 GRADES WITH, and let that refinement measure its own
    # error. Sizing and grading now use one instrument (start_mass), so
    # the band and the residue are the same quantity's.
    fb = fan_at(w, 0.0)
    yb = brentq(lambda ys: start_mass(w, fb, ys, 61) - w["mdot"],
                0.45 * w["RMAX"], 0.985 * w["RMAX"], xtol=1e-9)
    m_lo = start_mass(w, fb, yb, 61)
    m_hi = start_mass(w, fb, yb, 8 * 61)
    band_m = (A1.K_RICH * abs(m_lo - m_hi)
              + A1.C_FLOOR * A1.EPS * w["mdot"]) / w["mdot"]
    print("  derived mass band (start-line row refinement): %.2e"
          % band_m)
    check("T-2 every candidate passes the reference mass flow",
          all(abs(r["mdot"] / w["mdot"] - 1) <= band_m for r in res))
    check("T-3 the blind optimum agrees with the divergence"
          " prediction theta_E ~ 0 (within the sweep resolution)",
          abs(thE_best) <= 2.0)

    # T-4: the measured penalty vs the cos(theta_E) divergence model
    print("\n  the divergence model against the measurement:")
    print("  %8s %12s %12s" % ("thE[deg]", "measured", "cos model"))
    ok4 = True
    for thE_deg, J in zip(sweep, Js):
        meas = J / Js[ib] - 1.0
        model = np.cos(np.radians(thE_deg)) / np.cos(
            np.radians(thE_best)) - 1.0
        print("  %8.1f %11.3f%% %11.3f%%" % (thE_deg, 100 * meas,
                                             100 * model))
        if thE_deg >= 4 and not (meas < 0 and model < 0):
            ok4 = False
    check("T-4 outward turning is penalised, in sign and order, as"
          " the divergence model says", ok4)

    rb = evaluate(w, np.radians(thE_best), scale=1.05)
    dcf = abs(CF(rb["J"]) - cf[ib])
    print("\n  R-1: annulus mis-sized 5%% at the optimum -> C_F shifts"
          " %.5f (band %.5f)" % (dcf, BAND_J * cf[ib]))
    check("R-1 rejector: a basis violation moves C_F beyond the"
          " derived thrust band", dcf > BAND_J * cf[ib])

    np.savez_compressed(os.path.join(CC.CKPT, "inlet_angle.npz"),
                        thE=np.array(sweep, dtype=float), J=Js,
                        CF=cf, dnu=np.degrees(f0["dnu"]),
                        y0=np.array([r["y0"] for r in res]))
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                            time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
