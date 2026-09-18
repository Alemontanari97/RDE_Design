#!/usr/bin/env python3
"""[X-AFAN] THE AXISYMMETRIC LIP FAN: the method's own ideal-spike
construction, by the inverse (Goursat) march of the certified cell.
[F3/A1], S29 2026-09-16 (owner's directive of the evening: "the fan our
code builds is planar; to obtain Rao it must account for axisymmetry --
planar only next to the lip, then propagated axisymmetrically").

WHAT WAS WRONG. a1_inlet_angle_opt.fan_at is a planar simple wave
centred at the lip (q, theta functions of the ray angle alone). The
plug march is axisymmetric (delta = 1, source c^2 v / y), but its
Cauchy data on the cut at X0 and the incumbent streamline were sampled
from that planar wave; past the last planar ray the streamline is
horizontal (y 0.863 m at x 5.6 on the tournament posing, against a
contour that must reach the axis for the annulus to pass the mass at
uniform exit: pi (y_E^2 - y_w^2) = eps A_t closes only for y_w -> 0;
falsifier [X-RAOIS], S26). Moving the cut towards the lip does not
help: the data stay planar and the cells certify 1e10 (rao1961_world,
2026-08-26).

WHY NOT A FORWARD FAN. In planar flow the centred wave is simple: no
C+ carries information, every streamline is the ideal wall, the exit is
uniform whatever the wall. In axisymmetric flow the C- rays from the
lip reflect on the wall and the field depends on it: "the streamline of
the free fan" is not a construction (any wall is a streamline of its
own flow; Rao's mass closure on each ray adds nothing to tangency).
The ideal spike -- uniform (q_e, theta_E) exit at p_a -- is the INVERSE
problem: data on the lip point (the corner relation, exact at the
singular point: q_k, theta_k on every ray leaving it) and on the
terminal C- ray (straight, uniform, from the lip at theta_E - mu_e
to the axis). Between them the field is marched UPSTREAM ray by ray;
the wall is the streamline traced backward from the tip.

THE SAME CERTIFIED CELL. a1_ideal_march_jax.make_resid_interior is
written with midpoint coefficients along each chord; its C+ relation
between the unknown point 4 and the given point 2 is symmetric in the
roles of 2 and 4, so the INVERSE interior cell (point 4 upstream, its
C- from the ray's previous point 1, its C+ running downstream to the
point 2 already known on the next ray) is the same residual, the same
Newton, the same certification metric -- pt2 is simply the downstream
point. Nothing of the march is re-derived; the planar limit is a gate
(G-0, delta = 0 reproduces the corner relation on every mesh point and
the planar streamline of IA.spike, both shrinking under refinement).

WHAT "PLANAR NEXT TO THE LIP" MEANS HERE. Every ray starts AT the lip
with its own corner state; its first cell has the multi-valued corner
as one corner and is O(h) like every other cell. No arc radius, no
extra parameter: the corner relation is used at the point where it is
exact and nowhere else.

THE CONSTRUCTION (fan_axi): rays k = 0..R-1 at uniform planar ray
angle between the leading ray (M_i, theta_i) and the terminal ray
(p_a, theta_E); terminal ray = N_LEV points at uniform arc length from
the lip to the axis (theta_E = 0: the ideal member closes on the axis;
the module is posed at theta_E = 0 -- a conical uniform exit is not an
axisymmetric solution). For k = R-2 down to 0: point (k, j) from
pt1 = (k, j-1), pt2 = (k+1, j); the ray is computed to one level past
the wall crossing of ray k+1 (the fictitious cell below the wall is
the smooth one-cell continuation the streamline interpolation needs,
never a datum for a point above the wall). Wall: from the tip floor
y = YCUT y_E on the terminal ray (the plug march's declared floor,
ourworld_geno.YCUT), backward strip by strip: the crossing on ray k
solves (y - y_c) = tan((theta + theta_c)/2) (x - x_c) along the ray's
polyline (the midpoint rule of every wall cell). Upstream of the
leading ray the wall continues straight at its flow angle to x = 0
(the inflow region is not marched: the same declared inlet posing as
before). The start radius y_sp0 is an OUTPUT (mass closes on the
terminal ray by construction: G-2 measures the residual against the
world's mdot), not a brentq on the cut.

INTERFACE: fan_axi(w, thE) returns the fan_at dict (field, th_i, th_e,
LIP, dnu, ray1, pm) plus wall (x, y), y_sp0, x_tip, rays, cert, so
a1_plug_spline_opt.build_case swaps it in under PSPL_FAN=axi and every
downstream instrument (cut at X0, col_fluxes, march, margin, TR-SQP)
is untouched. field(x, y) interpolates the rays' crossings with the
vertical line x (uniform (q_e, theta_E) above the terminal ray's
crossing; the leading ray's crossing state below it, declared).

GATES (stage derive): G-0 planar limit on two rungs; G-1 every cell
certified (worst step ratio <= 1); G-2 mass through the terminal ray
vs mdot; G-3 wall band from a three-rung ladder (K_RICH x last
difference); G-4 the oracle read AFTERWARDS: GENO's axisymmetric
member (ourworld_geno) -- tip abscissa, y_sp0, wall distance vs G-3's
band (the member expands to 0.9949 PA: residual declared); G-5 the
plug march from the cut at X0 with the axi data and the axi wall
certifies, and its wall pressure agrees with the fan's own within the
band. Artifact _axi_fan/derive.json. Environment: AFAN_RAYS (default
241), AFAN_LEV (default 241), AFAN_ART.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import jax.numpy as jnp                                 # noqa: E402
from scipy.optimize import brentq                       # noqa: E402

import a1_ideal_march_jax as A1                         # noqa: E402
import a1_config_compare as CC                          # noqa: E402
import a1_inlet_angle_opt as IA                         # noqa: E402
import ourworld_geno as OW                              # noqa: E402
from a1_freejet_unit import q_at_pa                     # noqa: E402

N_RAYS = int(os.environ.get("AFAN_RAYS", "241"))
N_LEV = int(os.environ.get("AFAN_LEV", "241"))
ART = os.environ.get("AFAN_ART", os.path.join(HERE, "_axi_fan"))
YTIP = OW.YCUT                 # the plug march's tip floor, in lip radii
EPS = A1.EPS
K_RICH = A1.K_RICH
NPASS = [0, 0]
_CACHE = {}


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def _state(q, ta):
    return [float(t) for t in A1.state_q(jnp.float64(q), ta)]


# ----------------------------------------------------------------------
# the inverse ray march
# ----------------------------------------------------------------------
def fan_axi(w, thE=0.0, n_rays=N_RAYS, n_lev=N_LEV, delta=1.0,
            verbose=False, lev_power=1.0):
    """The ideal-spike fan of OUR world by the inverse march. delta = 1
    axisymmetric (the construction); delta = 0 the planar gate.
    lev_power (additive, 2026-09-18 [X-CHTW]): the terminal ray's levels
    at s = s_tip t^lev_power, t uniform -- 1.0 = uniform arc length, the
    posing of every row of record (bit-identical); > 1 clusters the
    levels at the lip. A LADDER KNOB, NOT A REMEDY -- measured on the
    sonic-lip fan (M_i 1.05, cold air): uniform 121 levels cert 6.5e2,
    61 levels 9e9, 241 levels 2.9e2 (cert ~ step^1.2); clustering p = 2
    1.5e3 and p = 3 2.5e3 at 121 (the stalled cell moves to where the
    step is widest), 59-73 at 241. The wall is converged to 1e-3 mm
    across all of them; the certification is not. See [X-CHTW]."""
    key = (float(thE), int(n_rays), int(n_lev), float(delta),
           float(lev_power))
    if key in _CACHE:
        return _CACHE[key]
    t0 = time.time()
    ta = w["ta"]
    pm = IA.fan_at(w, thE)
    qs, ths, mus, phis = (pm["pm"][k] for k in ("qs", "ths", "mus", "phis"))
    LIP = pm["LIP"]
    xl, yl = LIP
    # lip states of the rays: uniform in the planar ray angle
    phk = np.linspace(phis[0], phis[-1], n_rays)
    qk = np.interp(phk, phis, qs)
    thk = np.interp(phk, phis, ths)
    qk[0], thk[0], qk[-1], thk[-1] = qs[0], ths[0], qs[-1], ths[-1]
    # terminal ray: straight, uniform (q_e, th_e), lip -> axis
    q_e, th_e = float(qs[-1]), float(ths[-1])
    mu_e = float(mus[-1])
    ang = th_e - mu_e
    s_axis = yl / np.sin(-ang)
    # levels: uniform arc length from the lip to the TIP-FLOOR node
    # (y = YTIP y_E); the excluded tip below it is the declared posing
    # of every plug instrument and its cells (source ~ v / y with the
    # axis point as a datum) are never computed
    y_tip = YTIP * yl
    s_tip = (y_tip - yl) / np.sin(ang)
    s = s_tip * np.linspace(0.0, 1.0, n_lev) ** lev_power
    term = np.stack([xl + s * np.cos(ang), yl + s * np.sin(ang),
                     np.full(n_lev, q_e * np.cos(th_e)),
                     np.full(n_lev, q_e * np.sin(th_e))], axis=1)
    rays = [None] * n_rays
    rays[-1] = term
    t_int = A1.get_solver(("int", delta),
                          lambda: A1.make_resid_interior(delta))
    newton, step_norm = t_int[1], t_int[2]
    cert = dict(worst=0.0, where=None, n=0)

    def cell(pt1, pt2):
        p = jnp.concatenate([jnp.asarray(pt1), jnp.asarray(pt2)])
        z0 = A1.predict_interior(jnp.asarray(pt1), jnp.asarray(pt2),
                                 ta, delta)
        z = newton(z0, p, ta)
        step = float(step_norm(z, p, ta))
        sc = max(1.0, float(jnp.max(jnp.abs(z))))
        r = step / (A1.NEWTON_TOL_FACTOR * EPS * sc)
        cert["n"] += 1
        return np.asarray(z, float), r

    # wall crossing on a ray: the streamline's midpoint rule backward
    # from the crossing (xc, yc, thc) on the next ray
    def crossing(ray, xc, yc, thc):
        th = np.arctan2(ray[:, 3], ray[:, 2])
        n = len(ray)

        def lerp(col, sv):
            # linear along the polyline; the LAST segment extends by one
            # (a ray that stops one node short of the wall crossing --
            # its next cell would sit below the tip floor -- is
            # continued by its last chord, an O(h) extrapolation)
            j = int(min(max(np.floor(sv), 0), n - 2))
            t = sv - j
            return float(col[j] + t * (col[j + 1] - col[j]))

        def g(sv):
            x, y, t = lerp(ray[:, 0], sv), lerp(ray[:, 1], sv), lerp(th, sv)
            return (y - yc) - np.tan(0.5 * (t + thc)) * (x - xc)
        nodes = np.arange(n + 1, dtype=float)
        gv = np.array([g(sv) for sv in nodes])
        sign = np.where(gv[:-1] * gv[1:] <= 0.0)[0]
        if len(sign) == 0:
            return None
        j = int(sign[0])
        sv = brentq(g, float(j), float(j + 1))
        return (lerp(ray[:, 0], sv), lerp(ray[:, 1], sv), lerp(th, sv), sv,
                float(np.hypot(lerp(ray[:, 2], sv), lerp(ray[:, 3], sv))))

    # the tip: the terminal ray's last node
    xc, yc, thc = float(term[-1, 0]), float(term[-1, 1]), th_e
    jw = n_lev - 1
    wall = [(xc, yc, thc, q_e)]
    jws = [jw]
    svs = [float(jw)]
    for k in range(n_rays - 2, -1, -1):
        nxt = rays[k + 1]
        # the crossing on ray k+1 sits in [jw, jw+1); (k, jw) lies
        # down-left of it along a C+, so the crossing on ray k is above
        # level jw: one level past it is the interpolation margin
        J = min(jw + 1, len(nxt) - 1)
        pts = [np.array([xl, yl, qk[k] * np.cos(thk[k]),
                         qk[k] * np.sin(thk[k])])]
        certs = [0.0]
        for j in range(1, J + 1):
            z, r = cell(pts[j - 1], nxt[j])
            if not np.all(np.isfinite(z)) or z[1] <= 0.0:
                break
            pts.append(z)
            certs.append(r)
        ray = np.stack(pts, axis=0)
        rays[k] = ray
        c = crossing(ray, xc, yc, thc)
        if c is None:
            raise RuntimeError("no wall crossing on ray %d (J %d, jw %d)"
                               % (k, len(ray) - 1, jw))
        xc, yc, thc, sv, qc = c
        jw = int(np.floor(sv))
        # certification over the cells the wall depends on: the levels
        # up to the node below the crossing (the fictitious one-cell
        # continuation is reported apart)
        jc = min(jw + 1, len(certs) - 1)
        rw = max(certs[: jc + 1])
        if rw > cert["worst"]:
            cert["worst"], cert["where"] = rw, (k, int(np.argmax(certs[: jc + 1])))
        rf = max(certs[jc + 1:]) if len(certs) > jc + 1 else 0.0
        if rf > cert.get("worst_fict", 0.0):
            cert["worst_fict"] = rf
        wall.append((xc, yc, thc, qc))
        jws.append(jw)
        svs.append(float(sv))
    # upstream of the leading ray: straight at the flow angle to x = 0
    x0w, y0w, th0w, q0w = wall[-1]
    y_sp0 = y0w - np.tan(th0w) * (x0w - xl)
    wall.append((xl, y_sp0, th0w, q0w))
    W = np.array(wall[::-1])             # x increasing, (x, y, theta, q)
    x_tip = float(W[-1, 0])

    def cut(x):
        """Data on the vertical line x, y increasing: the traced WALL
        point first (its own state: never an interpolation through the
        fictitious cell below the wall, never a constant extrapolation
        from the lowest ray above it -- measured: a 3 deg bias of the
        foot angle at X0 before this datum was added), then the
        crossings of the rays above the wall, up to the terminal ray."""
        ys, us, vs = [], [], []
        if W[0, 0] <= x <= W[-1, 0]:
            yw = float(np.interp(x, W[:, 0], W[:, 1]))
            tw = float(np.interp(x, W[:, 0], W[:, 2]))
            qw = float(np.interp(x, W[:, 0], W[:, 3]))
            ys.append(yw)
            us.append(qw * np.cos(tw))
            vs.append(qw * np.sin(tw))
        for ray in rays:
            if ray[-1, 0] < x or ray[0, 0] > x:
                continue
            y = float(np.interp(x, ray[:, 0], ray[:, 1]))
            if ys and y <= ys[0]:
                continue                       # below the wall: fictitious
            ys.append(y)
            us.append(float(np.interp(x, ray[:, 0], ray[:, 2])))
            vs.append(float(np.interp(x, ray[:, 0], ray[:, 3])))
        return np.array(ys), np.array(us), np.array(vs)

    cut_cache = {}

    def field(x, y):
        if x not in cut_cache:
            cut_cache[x] = cut(x)
        ys, us, vs = cut_cache[x]
        if len(ys) == 0 or y >= ys[-1]:
            return q_e, th_e
        u = float(np.interp(y, ys, us))
        v = float(np.interp(y, ys, vs))
        return float(np.hypot(u, v)), float(np.arctan2(v, u))

    out = dict(pm)
    out.update(field=field, wall=(W[:, 0].copy(), W[:, 1].copy()),
               wall_th=W[:, 2].copy(), wall_q=W[:, 3].copy(),
               y_sp0=float(y_sp0), x_tip=x_tip,
               rays=rays, jws=jws[::-1], svs=svs[::-1], cert=cert, delta=delta,
               n_rays=n_rays, n_lev=n_lev, q_e=q_e, mu_e=mu_e,
               s_axis=float(s_axis), t_build=time.time() - t0,
               cut=cut)
    if verbose:
        print("   fan_axi(delta %g, %d rays x %d levels): %d cells, cert"
              " worst %.3f at %s (fictitious cells below the wall %.3f);"
              " tip x %.4f (axis %.4f), y_sp0 %.5f; %.0f s"
              % (delta, n_rays, n_lev, cert["n"], cert["worst"],
                 cert["where"], cert.get("worst_fict", 0.0), x_tip,
                 xl + s_axis * np.cos(ang), y_sp0, out["t_build"]),
              flush=True)
    _CACHE[key] = out
    return out


def ray_mass(ray, ta, sv=None):
    """Mass flux through a ray polyline from the lip to the fractional
    level sv (the wall crossing; None = the whole polyline), 2 pi y
    weighted: the flux of rho (u, v) through the segment normals."""
    if sv is not None:
        n = len(ray)
        j = int(min(max(np.floor(sv), 0), n - 2))
        end = ray[j] + (sv - j) * (ray[j + 1] - ray[j])
        ray = np.vstack([ray[: j + 1], end[None, :]])
    x, y, u, v = ray[:, 0], ray[:, 1], ray[:, 2], ray[:, 3]
    rho = np.array([_state(float(np.hypot(uu, vv)), ta)[2]
                    for uu, vv in zip(u, v)])
    dx, dy = np.diff(x), np.diff(y)
    fm = rho * u
    fn = rho * v
    # flux through the segment: (F . n) dl with n dl = (dy, -dx)
    f = 0.5 * ((fm[1:] + fm[:-1]) * dy - (fn[1:] + fn[:-1]) * dx)
    ym = 0.5 * (y[1:] + y[:-1])
    return abs(float(np.sum(2.0 * np.pi * ym * f)))


def wall_on(fan, xq):
    sx, sy = fan["wall"]
    return np.interp(xq, sx, sy)


# ----------------------------------------------------------------------
# stage derive
# ----------------------------------------------------------------------
def main():
    os.makedirs(ART, exist_ok=True)
    w = CC.build_world()
    ta = w["ta"]
    yl = w["RMAX"]
    print("== [X-AFAN] the axisymmetric lip fan by the inverse march --"
          " %d rays x %d levels, tip floor %.3f y_E ==" % (N_RAYS, N_LEV,
                                                           YTIP))
    rec = dict(n_rays=N_RAYS, n_lev=N_LEV, ytip=YTIP, RMAX=float(yl),
               mdot=float(w["mdot"]))

    # G-0 the planar limit: delta = 0 must reproduce the corner relation
    # on every mesh point and the planar streamline of IA.spike
    print("-- G-0 planar limit (delta 0): mesh states vs the corner"
          " relation, traced wall vs IA.spike, two rungs --")
    pl = IA.fan_at(w, 0.0)
    e_q, e_t, e_w = [], [], []
    for f in (0.5, 1.0):
        nr, nl = int(round(N_RAYS * f)), int(round(N_LEV * f))
        fp = fan_axi(w, 0.0, nr, nl, delta=0.0, verbose=True)
        dq = dt = 0.0
        for ray in fp["rays"][:-1]:
            for pt in ray[1:]:
                if pt[1] <= 0.0:
                    continue
                q0, t0_ = pl["field"](float(pt[0]), float(pt[1]))
                q, t = np.hypot(pt[2], pt[3]), np.arctan2(pt[3], pt[2])
                dq = max(dq, abs(q - q0) / q0)
                dt = max(dt, abs(t - t0_))
        sx, sy = IA.spike(pl, fp["y_sp0"], x_end=fp["x_tip"] + 0.5)
        wx, wy = fp["wall"]
        m = wx <= sx[-1]
        dw = float(np.max(np.abs(wy[m] - np.interp(wx[m], sx, sy))))
        print("   rung %d x %d: max rel |q - q_pm| %.2e, max |theta -"
              " theta_pm| %.2e rad, wall vs IA.spike %.2e m (y_sp0 %.5f,"
              " tip x %.4f)" % (nr, nl, dq, dt, dw, fp["y_sp0"],
                                fp["x_tip"]), flush=True)
        e_q.append(dq)
        e_t.append(dt)
        e_w.append(dw)
    rec["g0"] = dict(e_q=e_q, e_t=e_t, e_w=e_w)
    check("G-0a planar limit: the inverse march reproduces the corner"
          " relation and the error shrinks under refinement (q %.1e ->"
          " %.1e, theta %.1e -> %.1e)" % (e_q[0], e_q[1], e_t[0], e_t[1]),
          e_q[1] < e_q[0] and e_t[1] < e_t[0])
    check("G-0b planar limit: the traced wall is IA.spike's streamline"
          " and the gap shrinks (%.1e -> %.1e m)" % (e_w[0], e_w[1]),
          e_w[1] < e_w[0])

    # G-1..G-3 the construction on a three-rung ladder
    print("-- G-1/G-3 axisymmetric construction (delta 1), ladder --")
    fans = []
    for f in (0.25, 0.5, 1.0):
        nr, nl = int(round(N_RAYS * f)), int(round(N_LEV * f))
        fans.append(fan_axi(w, 0.0, nr, nl, delta=1.0, verbose=True))
    fa = fans[-1]
    rec["cert"] = [float(f_["cert"]["worst"]) for f_ in fans]
    rec["x_tip"] = [float(f_["x_tip"]) for f_ in fans]
    rec["y_sp0"] = [float(f_["y_sp0"]) for f_ in fans]
    check("G-1 every inverse cell certified on every rung (worst %s)"
          % ", ".join("%.3f" % c for c in rec["cert"]),
          all(c <= 1.0 for c in rec["cert"]))
    # G-2 mass through the terminal ray (lip -> tip) and through the
    # leading ray vs the world's mdot
    m_terms = [ray_mass(f_["rays"][-1], ta, f_["svs"][-1]) for f_ in fans]
    m_term = m_terms[-1]
    m_lead = ray_mass(fa["rays"][0], ta, fa["svs"][0])
    m_disc = float(_state(fa["q_e"], ta)[2] * fa["q_e"] * np.pi
                   * (yl ** 2 - (YTIP * yl) ** 2))
    print("   mass: terminal ray (lip -> tip) %.6f kg/s, closed form"
          " rho_e q_e pi (y_E^2 - y_tip^2) %.6f, leading ray (lip ->"
          " wall) %.6f, world mdot %.6f" % (m_term, m_disc, m_lead,
                                            w["mdot"]), flush=True)
    rec["mass"] = dict(term=m_terms, disc=m_disc, lead=m_lead)
    r_m = abs(m_term / w["mdot"] - 1.0)
    # band: the tip floor's own share (y_tip^2 / y_E^2, exact for the
    # uniform terminal ray) + K_RICH x the ladder's last difference
    band_m = YTIP ** 2 + K_RICH * abs(m_terms[-1] - m_terms[-2]) / w["mdot"]
    check("G-2 the terminal ray passes the world's mass to the tip-floor"
          " residual (%.2e vs band %.2e = floor %.1e + ladder; rungs %s;"
          " leading ray %.2e)"
          % (r_m, band_m, YTIP ** 2,
             ", ".join("%.6f" % m_ for m_ in m_terms),
             abs(m_lead / w["mdot"] - 1.0)), r_m <= band_m)
    # G-3 wall band: K_RICH x the last ladder difference on a common grid
    xg = np.linspace(0.0, min(f_["x_tip"] for f_ in fans), 4 * N_RAYS)
    d01 = float(np.max(np.abs(wall_on(fans[1], xg) - wall_on(fans[0], xg))))
    d12 = float(np.max(np.abs(wall_on(fans[2], xg) - wall_on(fans[1], xg))))
    band_W = K_RICH * d12
    print("   wall ladder: |w1 - w0| %.3e, |w2 - w1| %.3e m -> band_W ="
          " K_RICH x %.3e = %.3e m; tip x %s; y_sp0 %s"
          % (d01, d12, d12, band_W, rec["x_tip"], rec["y_sp0"]),
          flush=True)
    rec["band_W"] = band_W
    rec["ladder"] = [d01, d12]
    check("G-3 the wall converges under refinement (%.2e -> %.2e, band_W"
          " %.2e m)" % (d01, d12, band_W), d12 < d01)

    # G-4 the oracle, read afterwards: GENO's member in our gas
    print("-- G-4 oracle (read after the construction): GENO's"
          " axisymmetric member --")
    if os.path.isdir(OW.RUN):
        Wo = OW.load_world(verbose=True)
        ow = Wo["wall"]
        sx, sy = fa["wall"]
        shift = float(sy[0] - ow[0, 1])
        m = (ow[:, 0] >= sx[0]) & (ow[:, 0] <= sx[-1])
        dist = np.abs(np.interp(ow[m, 0], sx, sy) - ow[m, 1])
        print("   member: x %.4f..%.4f (tip cut %.4f), y_sp0 %.5f vs ours"
              " %.5f (shift %+.2e); ours tip x %.4f; wall distance max"
              " %.3e mean %.3e m over %d member points; band_W %.3e"
              % (ow[0, 0], ow[-1, 0], Wo["x_end"], ow[0, 1], sy[0], shift,
                 fa["x_tip"], dist.max(), dist.mean(), int(m.sum()),
                 band_W), flush=True)
        rec["oracle"] = dict(x_end=float(Wo["x_end"]), y0=float(ow[0, 1]),
                             dist_max=float(dist.max()),
                             dist_mean=float(dist.mean()),
                             pa_ratio=float(Wo["pa"] / CC.PA))
        check("G-4 (reported) the member's tip abscissa %.4f vs ours %.4f:"
              " |d| %.3e m; the member expands to %.4f PA (declared)"
              % (Wo["x_end"], fa["x_tip"], abs(Wo["x_end"] - fa["x_tip"]),
                 Wo["pa"] / CC.PA), True)
        np.savez_compressed(os.path.join(ART, "oracle_walls.npz"),
                            ours=np.stack(fa["wall"], axis=1), geno=ow)
    else:
        print("   GENO run %s absent: oracle skipped" % OW.RUN)

    # G-5 the plug march from the cut at X0 with the axi data and wall:
    # two row counts N and 2N-1 (the tail's wall cells are ROW-limited:
    # measured 2026-09-16, x > 4.9 m, +7 % at N 61 -> +0.5 % at N 241,
    # the columns K irrelevant) -- the gate is that the two instruments
    # CONVERGE to each other, the number is the band at the rung used
    print("-- G-5 the plug march on the construction: cut at X0 %.2f,"
          " axi data, stations on the axi wall, rows N and 2N-1 --" % IA.X0)
    os.environ["PSPL_FAN"] = "axi"
    os.environ["PSPL_L"] = "%.10f" % fa["x_tip"]
    import a1_plug_spline_opt as P
    from a1_plug_march import plug_march
    sx, sy = fa["wall"]
    xq = np.linspace(IA.X0, fa["x_tip"], P.K_ST + 1)[1:]
    st = (jnp.asarray(xq), jnp.asarray(np.interp(xq, sx, sy)),
          jnp.asarray(np.tan(np.interp(xq, sx, fa["wall_th"]))))
    q_f = np.interp(xq, sx, fa["wall_q"])
    pw_f = np.array([_state(float(q), ta)[1] for q in q_f])
    g5 = []
    for N in (P.N_ROW, 2 * P.N_ROW - 1):
        c = P.build_case(w, 0.0, N=N)
        out, _ = plug_march(st, c["start"], c["qpa"], w["tab"], 1.0)
        wall = np.asarray(out["wall"])
        pw_m = np.array([_state(float(np.hypot(r[2], r[3])), ta)[1]
                         for r in wall])
        rel = (pw_m - pw_f) / pw_f
        i_mx = int(np.argmax(np.abs(rel)))
        print("   N %d: %d stations, cert worst %.3f at %s (%d cells); F_in"
              " %.6e, md_in %.6f; foot angle at X0 %.3f deg; wall pressure"
              " march vs fan: max |rel| %.3e at x %.3f, median |rel| %.3e"
              % (N, wall.shape[0], float(out["cert_worst"]),
                 out.get("cert_where"), int(out["cert_n"]), c["F_in"],
                 c["md_in"], np.degrees(np.arctan(c["slope0"])),
                 abs(rel[i_mx]), xq[i_mx], float(np.median(np.abs(rel)))),
              flush=True)
        for i in range(0, len(xq), max(1, len(xq) // 10)):
            print("      x %.3f  p_march %.5g  p_fan %.5g  rel %+.2e"
                  % (xq[i], pw_m[i], pw_f[i], rel[i]))
        g5.append(dict(N=N, cert=float(out["cert_worst"]),
                       dp_max=float(abs(rel[i_mx])), x_max=float(xq[i_mx]),
                       dp_median=float(np.median(np.abs(rel))),
                       md_in=float(c["md_in"]), F_in=float(c["F_in"])))
    rec["g5"] = g5
    check("G-5a the plug march certifies on the construction at both row"
          " counts (cert %.3f, %.3f)" % (g5[0]["cert"], g5[1]["cert"]),
          all(g["cert"] <= 1.0 for g in g5))
    check("G-5b the march's wall pressure converges to the fan's under row"
          " refinement (max |rel| %.2e -> %.2e, median %.2e -> %.2e): the"
          " residual at N %d is the march's tail band, ROW-limited"
          % (g5[0]["dp_max"], g5[1]["dp_max"], g5[0]["dp_median"],
             g5[1]["dp_median"], g5[0]["N"]),
          g5[1]["dp_max"] < g5[0]["dp_max"])

    json.dump(rec, open(os.path.join(ART, "derive.json"), "w"), indent=1)
    print("== %d/%d PASS ==" % tuple(NPASS))


if __name__ == "__main__":
    main()
