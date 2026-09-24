#!/usr/bin/env python3
"""[X-RAOPO] RAO 1961's TABLE 1 BY OUR OWN MARCH FROM HIS OPTIMALITY
CONDITIONS, AND THE TR-SQP RE-OBTENTION FROM A START THAT IS OURS -- the
F3 exit leg "spike Table-1 oracle in derived bands", with no GENO field
anywhere in the chain. [F3/A1], S37 2026-09-24 (the owner's realignment
with the D6 plan: F3 opened, its exit duties first).

WHAT WAS MISSING. Every Rao-world instrument of record starts from GENO's
field: the twin [X-RAOTW], the plug O3.3 [X-RAOO3], the SQP return
[X-RAOSQ] read GENO's legacy RaoPlug run on a cut. The Table-1 contour
therefore reached us THROUGH GENO (which reproduces it at 2.44e-3). What
is ours is the control surface: [X-RAOCS] rebuilds ED from his first
integrals without a march (X_D/R_E to 1.3e-6) and [X-RAOFN] evaluates our
functional on it (C_F 1.58). The contour UPSTREAM of ED -- his Table 1 --
had never been produced by our method.

THE CONSTRUCTION (stage derive). His optimum is characterised by ED: the
C- from the lip E carrying Eqs. (6)-(7), w cos(theta + alpha)/cos alpha =
C2 and R rho w^2 sin^2 theta tan alpha = C3, down to his terminus D. The
field between the lip's centred fan and ED is a Goursat problem between
two characteristics: the fan's rays leave E with the corner relation
(exact at the singular point: theta(M) = theta_E - (nu(M_E) - nu(M))),
ED is the terminal ray. [X-AFAN] solved exactly this problem for the
ideal spike (terminal ray uniform, to the axis) with the record's
certified interior cell run UPSTREAM (its C+ relation is symmetric in
the given and the unknown point): here the terminal ray is HIS ED,
resampled at uniform arc length, and the cell is the record's top-down
interior cell with its compatibility rows scaled by q^3 ([X-FRMR], same
root; the unscaled cell's damped Newton stalls on this fan, measured);
nothing else changes. The wall is
the streamline traced backward from D (his terminus, the flow angle
there) ray by ray; upstream of the leading ray (M_i 1.05, the sonic line
cannot be a ray) it continues straight at its flow angle to the sonic
line, declared. MEASURED BEFORE (S37, three FORWARD posings of his sonic
start, abandoned): his straight sonic line carried to M_i > 1 as a
transverse start is no axisymmetric solution (the IVL triangle found
subsonic roots, cert 3e12); a uniform leading C- decelerates to M 1;
his sonic line as the fan's leading ray certifies only at 31 rays (61
rays: the free-jet triangle folds at the edge, cert 5e14) and reads
theta on ED 2-4 deg off at that resolution. The inverse construction
has the corner exact at E and his ED exact as data.

  ID-1 every inverse cell certified on the three-rung ladder;
  ID-2 mass: the leading ray (lip -> wall crossing) carries ED's mass
       (lip -> D) within K_RICH x the ladder's last difference;
  ID-3 the traced wall converges under refinement (band_W = K_RICH x
       the last difference);
  ID-4 THE ORACLE: the wall at his Table 1 abscissae downstream of the
       leading ray's crossing reads his radii within his printing
       (5e-4 R_E) + band_W;
  ID-5 his area ratio from our mass: eps = pi R_E^2 / A_t, A_t = m /
       (rho* a*) of the table, vs 3.81 within printing + ladder;
  ID-6 his thrust coefficient from OUR field: F through the leading
       ray + push on the traced wall + his base (p_b = 0), in his vacuum
       convention, vs 1.58 within printing + ladder -- and the momentum
       closure F(leading) + push = F(ED) within the ladder band;
  R-1  REJECTOR: the planar inverse march (delta = 0) on the same data
       misses his contour by more than 10x the band (the centred fan is
       a point relation in axisymmetric flow, [X-RAOIS]).

THE RE-OBTENTION (stage walk, [DIR-REOB]). The [X-RAOSQ] v3 instrument
VERBATIM (rao1961_sqp_return: its stations, spline, frozen near-cut
zone, pinned tip, J_replay, segmented TR-SQP, AD-Hessian bands per
eigen-direction) with ONE change: the start line at x0 = 0.30 is the
vertical cut through OUR inverse field (the traced wall point first,
then the rays' crossings up to ED; EDGE_FILL rows to the jet as the
record), and the reference wall is HIS Table 1 (spline through his
points) instead of GENO's contour.
  RE-0  STATIONARITY: his contour's gradient floor and spectrum under
        this instrument (the bands; nothing graded);
  RE-1  RE-OBTENTION from a GENERIC start (the chord from the frozen
        zone's end to D): the landing inside every direction's band,
        the value within band_J;
  RE-1b the same from [X-RAOSQ]'s 1.5-percent perturbed start;
  RE-3  COINCIDENCE: the two landings coincide within the band;
  R-3   REJECTOR: the sign-flipped driver from the perturbed start ends
        farther from his contour than it began.
FALSIFIER: ID-4 failing = our march from his conditions does not
produce his contour (a finding about the march or about his table);
RE-1 failing with the gradient closed = a second stationary point of
the spline space from our start.

DECLARED. His p_b = 0 and vacuum convention; his published terminus
(R_D/R_E 0.137, which leaves his own Eq. (9) at a residual [X-RAOCS]);
the leading ray at M_i 1.05 and the straight wall upstream of it; the
world's units are the Rao-world twin's. No GENO field is read.

ENVIRONMENT. RAOPO_STAGE derive|walk|rejector (default derive); RAOPO_SEG_R1
(stage rejector: the sign-flipped driver's segment budget, default the
record's); RAOPO_START
(walk: comma list of line,perturb; default both); RAOPO_ART (default
_rao1961_posing/). Constants in rao1961_posing_cases.json.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import jax.numpy as jnp                                 # noqa: E402
from scipy.interpolate import CubicSpline               # noqa: E402
from scipy.optimize import brentq                       # noqa: E402

import a1_ideal_march_jax as A1                         # noqa: E402
import a1_plug_march as PM                              # noqa: E402
from a1_freejet_unit import q_at_pa                     # noqa: E402
from rao1961_control_surface import REF                 # noqa: E402
from rao1961_ideal_spike import nu                      # noqa: E402
from rao1961_control_surface import state, theta_of_M     # noqa: E402
from rao1961_world import TAB1, G, M_E, TH_E, PA_PC     # noqa: E402

CASES = {k: v["value"] for k, v in json.load(
    open(os.path.join(HERE, "rao1961_posing_cases.json"))).items() if k != "_doc"}
WORLD, INV, BANDS, WALK = CASES["world"], CASES["inverse"], CASES["bands"], CASES["walk"]
ART = os.environ.get("RAOPO_ART", os.path.join(HERE, "_rao1961_posing"))
K_RICH = A1.K_RICH
NPASS = [0, 0]
_FAIL = {}                      # the state of a failed crossing (diagnostic)


def say(msg):
    print(msg, flush=True)


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def build_world():
    tab = A1.prep_tab(A1.build_tab_gconst(g=G, Rg=WORLD["Rg"], ts=WORLD["T0"], ps=WORLD["p0"]))
    ta = A1.tab_arrays(tab)
    pa = PA_PC * WORLD["p0"]
    return dict(tab=tab, ta=ta, as_=tab["_as"], pa=pa, P0=WORLD["p0"], T0=WORLD["T0"],
                qpa=float(q_at_pa(pa, ta, tab["_as"])))


def q_closed(M):
    """Speed at Mach M on his isentrope (the gconst table's own closed form)."""
    T = WORLD["T0"] / (1.0 + 0.5 * (G - 1.0) * np.asarray(M) ** 2)
    return np.asarray(M) * np.sqrt(G * WORLD["Rg"] * T)


def his_wall():
    """Table 1 as the not-a-knot cubic spline through his 16 points."""
    return CubicSpline(TAB1[:, 0], TAB1[:, 1])


def his_surface(n, M_e=M_E, th_e=TH_E, r_D=None):
    """His control surface E -> D from his first integrals (Eqs. 6-7, x
    from Eq. 5), cut at the radius r_D (default his published terminus):
    rao1961_our_functional.build_surface with (M_E, theta_E) as arguments,
    so that the rejector can pose a NEIGHBOURING optimum."""
    r_D = REF["rd"] if r_D is None else r_D
    wE, rhoE, pE, alE = state(M_e)
    C2 = wE * np.cos(th_e + alE) / np.cos(alE)
    C3 = rhoE * wE ** 2 * np.sin(th_e) ** 2 * np.tan(alE)

    def R_of(m):
        w_, r_, _, a_ = state(m)
        return C3 / (r_ * w_ ** 2 * np.sin(theta_of_M(m, C2)) ** 2 * np.tan(a_))
    m_D = brentq(lambda m: R_of(m) - r_D, 1.0 + (M_e - 1.0) / 4.0, M_e * (1.0 - np.finfo(float).eps),
                 xtol=A1.EPS)
    Ms = np.linspace(M_e, m_D, n)
    ths = np.array([theta_of_M(m, C2) for m in Ms])
    st = np.array([state(m) for m in Ms])
    rs = C3 / (st[:, 1] * st[:, 0] ** 2 * np.sin(ths) ** 2 * np.tan(st[:, 3]))
    dxdr = 1.0 / np.tan(ths - st[:, 3])
    xs = np.concatenate([[0.0], np.cumsum(0.5 * (dxdr[1:] + dxdr[:-1]) * np.diff(rs))])
    return Ms, ths, rs, xs


def his_T_class():
    """His table's own consistency at its first row: the throat point T
    his Eq. (12) puts on the straight sonic line from E normal to the
    sonic flow angle theta* = theta_E - nu(M_E), for his eps; against his
    printed T. A MEASURED class of the reference, not a chosen number."""
    th_s = TH_E - nu(M_E, G)
    R_T = np.sqrt(1.0 - np.cos(th_s) / REF["eps"])
    L = (1.0 - R_T) / np.cos(th_s)
    X_T = L * np.cos(th_s - np.pi / 2.0)
    return float(X_T), float(R_T), float(abs(X_T - TAB1[0, 0])), float(abs(R_T - TAB1[0, 1]))


def _state(q, ta):
    return [float(t) for t in A1.state_q(jnp.float64(q), ta)]


# ----------------------------------------------------------------------
# the inverse march from his ED
# ----------------------------------------------------------------------
def inverse_fan(w, n_rays, n_lev, delta=1.0, M_i=None, lev_power=None, M_e=M_E, th_e=TH_E):
    """[X-AFAN]'s inverse Goursat march with HIS control surface as the
    terminal ray. Returns the rays, the traced wall (x, y, theta, q) from
    the leading ray's crossing to D, ED's polyline and the certification."""
    t0 = time.time()
    ta = w["ta"]
    M_i = INV["M_i"] if M_i is None else float(M_i)
    lev_power = INV["lev_power"] if lev_power is None else float(lev_power)
    RE = WORLD["R_E"]
    # ED: his first integrals, cut at his terminus; uniform arc length
    Ms, ths, rs, xs = his_surface(INV["ed_points"], M_e, th_e)
    sE = np.concatenate([[0.0], np.cumsum(np.hypot(np.diff(xs), np.diff(rs)))])
    s = sE[-1] * np.linspace(0.0, 1.0, n_lev) ** lev_power
    xt, yt = np.interp(s, sE, xs) * RE, RE * np.interp(s, sE, rs)
    Mt, tht = np.interp(s, sE, Ms), np.interp(s, sE, ths)
    qt = q_closed(Mt)
    term = np.stack([xt, yt, qt * np.cos(tht), qt * np.sin(tht)], axis=1)
    # the lip rays: the corner relation, uniform in the planar ray angle
    Mg = np.linspace(M_i, M_e, INV["M_grid"])
    thg = th_e - (nu(M_e, G) - np.array([nu(m, G) for m in Mg]))
    phg = thg - np.arcsin(1.0 / Mg)
    phk = np.linspace(phg[0], phg[-1], n_rays)
    Mk = np.interp(phk, phg, Mg)
    thk = np.interp(phk, phg, thg)
    Mk[-1], thk[-1] = M_e, th_e
    qk = q_closed(Mk)
    # THE FRAME (S37, measured): the fan's C- rays turn through the vertical
    # (theta - mu from -124 deg at M_i to -33 deg at M_E), where the slope
    # form of the characteristic rows is singular (cond(J) 2e14 at the
    # stalled cell, its C- at -90.4 deg; the S32 lesson of the throat
    # kernel). Marched in the frame rotated by the leading ray's flow angle
    # (the throat frame of [X-FRMR], origin at E), both families stay off
    # the vertical: C- in [-72, +19] deg, C+ in [+46, +73] deg.
    import a1_frame_march as FM
    th_f = float(thk[0])
    X0f, Y0f = 0.0, RE
    tx, ty, tu, tv = FM.to_frame(term[:, 0], term[:, 1], term[:, 2], term[:, 3], th_f, X0f, Y0f)
    term_f = np.stack([tx, ty, tu, tv], axis=1)
    thk_f = thk - th_f
    xl, yl = 0.0, 0.0                              # E at the frame origin
    rays = [None] * n_rays
    rays[-1] = term_f
    t_int = A1.get_solver(("inttd_rot", delta, th_f, Y0f),
                          lambda: FM.make_resid_interior_td_rot(delta, th_f, Y0f))
    newton, step_norm = t_int[1], t_int[2]
    cert = dict(worst=0.0, where=None, n=0)
    import a1_ivl_triangle as IVT

    def cell(pt1, pt2):
        p = jnp.concatenate([jnp.asarray(pt1), jnp.asarray(pt2)])
        z0 = IVT._seed(np.asarray(pt1, float), np.asarray(pt2, float), ta)
        z = newton(z0, p, ta)
        step = float(step_norm(z, p, ta))
        sc = max(1.0, float(jnp.max(jnp.abs(z))))
        cert["n"] += 1
        return np.asarray(z, float), step / (A1.NEWTON_TOL_FACTOR * A1.EPS * sc)

    def crossing(ray, xc, yc, thc):
        th = np.arctan2(ray[:, 3], ray[:, 2])
        n = len(ray)

        def lerp(col, sv):
            j = int(min(max(np.floor(sv), 0), n - 2))
            t = sv - j
            return float(col[j] + t * (col[j + 1] - col[j]))

        def g(sv):
            x, y, t = lerp(ray[:, 0], sv), lerp(ray[:, 1], sv), lerp(th, sv)
            return (y - yc) - np.tan(0.5 * (t + thc)) * (x - xc)
        gv = np.array([g(sv) for sv in np.arange(n + 1, dtype=float)])
        sign = np.where(gv[:-1] * gv[1:] <= 0.0)[0]
        if len(sign) == 0:
            return None
        j = int(sign[0])
        sv = brentq(g, float(j), float(j + 1))
        return (lerp(ray[:, 0], sv), lerp(ray[:, 1], sv), lerp(th, sv), sv,
                float(np.hypot(lerp(ray[:, 2], sv), lerp(ray[:, 3], sv))))

    xc, yc, thc = float(term_f[-1, 0]), float(term_f[-1, 1]), float(tht[-1] - th_f)
    jw = n_lev - 1
    wall = [(xc, yc, thc, float(qt[-1]))]
    svs = [float(jw)]
    for k in range(n_rays - 2, -1, -1):
        nxt = rays[k + 1]
        J = min(jw + 1, len(nxt) - 1)
        pts = [np.array([xl, yl, qk[k] * np.cos(thk_f[k]), qk[k] * np.sin(thk_f[k])])]
        certs = [0.0]
        for j in range(1, J + 1):
            z, r = cell(pts[j - 1], nxt[j])
            if not np.all(np.isfinite(z)) or Y0f + z[0] * np.sin(th_f) + z[1] * np.cos(th_f) <= 0.0:
                break
            pts.append(z)
            certs.append(r)
        ray = np.stack(pts, axis=0)
        rays[k] = ray
        c = crossing(ray, xc, yc, thc)
        if c is None:
            _FAIL.update(ray=ray, nxt=nxt, xc=xc, yc=yc, thc=thc, k=k, jw=jw)
            raise RuntimeError("no wall crossing on ray %d (J %d, jw %d)" % (k, len(ray) - 1, jw))
        xc, yc, thc, sv, qc = c
        jw = int(np.floor(sv))
        jc = min(jw + 1, len(certs) - 1)
        rw = max(certs[: jc + 1])
        if rw > cert["worst"]:
            cert["worst"], cert["where"] = rw, (k, int(np.argmax(certs[: jc + 1])))
        wall.append((xc, yc, thc, qc))
        svs.append(float(sv))
    Wf = np.array(wall[::-1])                     # leading ray -> D, frame
    Xw, Yw, _, _ = FM.to_record(Wf[:, 0], Wf[:, 1], 0.0 * Wf[:, 0], 0.0 * Wf[:, 0], th_f, X0f, Y0f)
    W = np.stack([Xw, Yw, Wf[:, 2] + th_f, Wf[:, 3]], axis=1)   # record (x, y, theta, q)
    rays_rec = []
    for r in rays:
        X, Y, U, V = FM.to_record(r[:, 0], r[:, 1], r[:, 2], r[:, 3], th_f, X0f, Y0f)
        rays_rec.append(np.stack([X, Y, U, V], axis=1))
    return dict(rays=rays_rec, wall=W, svs=svs[::-1], term=term, cert=cert, n_rays=n_rays,
                n_lev=n_lev, delta=delta, Mk=Mk, th_frame=th_f, t_build=time.time() - t0)


def ray_polyline(ray, sv):
    """The ray from the lip to the fractional level sv."""
    n = len(ray)
    j = int(min(max(np.floor(sv), 0), n - 2))
    end = ray[j] + (sv - j) * (ray[j + 1] - ray[j])
    return np.vstack([ray[: j + 1], end[None, :]])


def wall_push(W, ta, pa):
    """Axial force of the wall from the leading ray's crossing to D
    (gauge p_a): integral (p - p_a) 2 pi y (-dy), the record's sign."""
    pw = np.array([_state(q, ta)[1] for q in W[:, 3]])
    dy = np.diff(W[:, 1])
    ym = 0.5 * (W[1:, 1] + W[:-1, 1])
    return float(np.sum(0.5 * (pw[1:] + pw[:-1] - 2.0 * pa) * 2.0 * np.pi * ym * (-dy)))


def readings(w, fa):
    """Mass, eps, fluxes and C_F of one construction."""
    ta, pa = w["ta"], w["pa"]
    lead = ray_polyline(fa["rays"][0], fa["svs"][0])
    ED = fa["term"]
    m_lead, F_lead = PM.col_fluxes(lead[::-1], ta, pa, 1.0)       # wall -> lip
    m_ED, F_ED = PM.col_fluxes(ED[::-1], ta, pa, 1.0)             # D -> E
    m_lead, m_ED = abs(float(m_lead)), abs(float(m_ED))
    push = wall_push(fa["wall"], ta, pa)
    y_D = float(fa["wall"][-1, 1])
    base = -pa * np.pi * y_D ** 2                                 # his p_b = 0, gauge
    st_s = _state(w["as_"], ta)
    A_t = m_ED / (st_s[2] * w["as_"])
    eps = np.pi * WORLD["R_E"] ** 2 / A_t
    F_vac = float(F_lead) + push + base + pa * np.pi * WORLD["R_E"] ** 2
    CF = F_vac / (w["P0"] * A_t)
    return dict(m_lead=m_lead, m_ED=m_ED, F_lead=float(F_lead), F_ED=float(F_ED), push=push,
                base=base, A_t=A_t, eps=eps, CF=CF, x_lead=float(fa["wall"][0, 0]),
                y_lead=float(fa["wall"][0, 1]))


def wall_at(fa, xq):
    W = fa["wall"]
    return np.interp(xq, W[:, 0], W[:, 1])


# ======================================================================
# stage derive
# ======================================================================
def derive():
    t00 = time.time()
    os.makedirs(ART, exist_ok=True)
    say("== [F3] Rao 1961 Table 1 by OUR inverse march from HIS control surface [X-RAOPO]"
        " (stage derive) ==")
    w = build_world()
    rec = dict(ladder=INV["ladder"], M_i=INV["M_i"])
    fans, rds = [], []
    for nr, nl in INV["ladder"]:
        fa = inverse_fan(w, nr, nl)
        rd = readings(w, fa)
        fans.append(fa)
        rds.append(rd)
        say("   rung (%d rays, %d levels): %d cells, cert %.3e at %s; leading ray (M %.3f) crosses"
            " the wall at (%.5f, %.5f); m lead %.6g / ED %.6g kg/s; eps %.5f; F lead %.6g + push"
            " %.6g + base %.6g -> C_F %.5f (F_ED %.6g); %.0f s"
            % (nr, nl, fa["cert"]["n"], fa["cert"]["worst"], fa["cert"]["where"], fa["Mk"][0],
               rd["x_lead"], rd["y_lead"], rd["m_lead"], rd["m_ED"], rd["eps"], rd["F_lead"],
               rd["push"], rd["base"], rd["CF"], rd["F_ED"], fa["t_build"]))
    fa, rd = fans[-1], rds[-1]
    rec["cert"] = [f_["cert"]["worst"] for f_ in fans]
    rec["readings"] = rds
    check("ID-1 every inverse cell certified on every rung (worst %s)"
          % ", ".join("%.3f" % c for c in rec["cert"]), all(c <= 1.0 for c in rec["cert"]))
    # ID-2 mass
    r_m = abs(rd["m_lead"] / rd["m_ED"] - 1.0)
    b_m = K_RICH * abs(rds[-1]["m_lead"] / rds[-1]["m_ED"] - rds[-2]["m_lead"] / rds[-2]["m_ED"])
    check("ID-2 the leading ray carries ED's mass: |m_lead/m_ED - 1| %.2e <= %.2e (K x ladder;"
          " rungs %s)" % (r_m, b_m, ", ".join("%.2e" % abs(r_["m_lead"] / r_["m_ED"] - 1.0)
                                               for r_ in rds)), r_m <= b_m)
    # ID-3 wall convergence
    x_lo = max(f_["wall"][0, 0] for f_ in fans)
    xg = np.linspace(x_lo, float(fa["wall"][-1, 0]), 4 * INV["ladder"][-1][0])
    d01 = float(np.max(np.abs(wall_at(fans[1], xg) - wall_at(fans[0], xg))))
    d12 = float(np.max(np.abs(wall_at(fans[2], xg) - wall_at(fans[1], xg))))
    band_W = K_RICH * d12
    rec.update(d01=d01, d12=d12, band_W=band_W)
    check("ID-3 the traced wall converges (%.2e -> %.2e R_E; band_W %.2e)" % (d01, d12, band_W),
          d12 < d01)
    # ID-4 the oracle
    m = TAB1[:, 0] >= fa["wall"][0, 0]
    dr = wall_at(fa, TAB1[m, 0]) - TAB1[m, 1]
    X_Tc, R_Tc, dX_T, dR_T = his_T_class()
    cls = max(dX_T, dR_T)
    b4 = cls + band_W
    say("   his table's own class at T: his Eq. (12) with his eps puts T at (%.5f, %.5f) on the"
        " sonic line; he prints (%.3f, %.4f): |dX| %.2e, |dR| %.2e -> class %.2e R_E"
        % (X_Tc, R_Tc, TAB1[0, 0], TAB1[0, 1], dX_T, dR_T, cls))
    say("   Table 1 rows downstream of the leading ray (x >= %.4f): %d of %d; our r - his r: %s"
        % (fa["wall"][0, 0], int(m.sum()), len(TAB1), np.array2string(dr, precision=4)))
    W0 = fa["wall"][0]
    th_s = TH_E - nu(M_E, G)
    # upstream of the leading ray: straight at its flow angle to the sonic line from E
    nx, ny = np.cos(th_s), np.sin(th_s)            # the sonic line is normal to (nx, ny)
    t_s = ((0.0 - W0[0]) * nx + (WORLD["R_E"] - W0[1]) * ny) / (np.cos(W0[2]) * nx + np.sin(W0[2]) * ny)
    T_ours = (W0[0] + t_s * np.cos(W0[2]), W0[1] + t_s * np.sin(W0[2]))
    say("   upstream of the leading ray (declared: straight at its flow angle %.2f deg to the sonic"
        " line): our T (%.5f, %.5f), Eq. (12)'s (%.5f, %.5f), his (%.3f, %.4f)"
        % (np.degrees(W0[2]), T_ours[0], T_ours[1], X_Tc, R_Tc, TAB1[0, 0], TAB1[0, 1]))
    rec.update(dr=dr.tolist(), class_T=cls, T_ours=list(T_ours), T_eq12=[X_Tc, R_Tc])
    check("ID-4 THE ORACLE: our wall reads his Table 1 at %d rows, max |dr| %.2e R_E <= %.2e"
          " (his table's own class at T %.2e + band_W)" % (int(m.sum()), float(np.max(np.abs(dr))),
                                                           b4, cls), float(np.max(np.abs(dr))) <= b4)
    check("ID-4b ... and on the mean: |mean dr| %.2e <= his printing %.1e + band_W"
          % (abs(float(np.mean(dr))), BANDS["table_coord"]),
          abs(float(np.mean(dr))) <= BANDS["table_coord"] + band_W)
    # ID-5 eps, ID-6 C_F and the momentum closure
    b_eps = BANDS["print_rel"] + K_RICH * abs(rds[-1]["eps"] - rds[-2]["eps"]) / REF["eps"]
    d_eps = abs(rd["eps"] / REF["eps"] - 1.0)
    check("ID-5 his area ratio from our mass: eps %.5f vs %.2f (rel %.2e <= %.2e)"
          % (rd["eps"], REF["eps"], d_eps, b_eps), d_eps <= b_eps)
    b_cf = BANDS["print_rel"] + K_RICH * abs(rds[-1]["CF"] - rds[-2]["CF"]) / REF["cf"]
    d_cf = abs(rd["CF"] / REF["cf"] - 1.0)
    clos = abs((rd["F_lead"] + rd["push"]) / rd["F_ED"] - 1.0)
    b_clos = K_RICH * abs((rds[-1]["F_lead"] + rds[-1]["push"]) / rds[-1]["F_ED"]
                          - (rds[-2]["F_lead"] + rds[-2]["push"]) / rds[-2]["F_ED"])
    check("ID-6 his vacuum thrust coefficient from our field: C_F %.5f vs %.2f (Table 3 1.5804;"
          " rel %.2e <= %.2e); momentum closure F_lead + push vs F_ED %.2e <= %.2e"
          % (rd["CF"], REF["cf"], d_cf, b_cf, clos, b_clos), d_cf <= b_cf and clos <= b_clos)
    # R-1 planar rejector
    nr, nl = INV["ladder"][1]
    try:
        fp = inverse_fan(w, nr, nl, delta=0.0)
        dp = float(np.max(np.abs(wall_at(fp, TAB1[m, 0]) - TAB1[m, 1])))
        say("   planar (delta 0) at (%d, %d): cert %.3e, wall vs his Table 1 max %.3e R_E"
            % (nr, nl, fp["cert"]["worst"], dp))
    except RuntimeError as exc:
        dp = float("inf")
        say("   planar (delta 0) at (%d, %d): the construction fails (%s)" % (nr, nl, exc))
    check("R-1 REJECTOR: the planar inverse march misses his contour (%.2e > 10 x %.2e)"
          % (dp, b4), dp > 10.0 * b4)
    rec["planar_miss"] = dp
    # R-2 a neighbouring optimum: his construction at theta_E moved by d_th
    d_th = np.radians(CASES["controls"]["d_theta_E_deg"])
    fn_ = inverse_fan(w, nr, nl, th_e=TH_E + d_th)
    dn = float(np.max(np.abs(wall_at(fn_, TAB1[m, 0]) - TAB1[m, 1])))
    say("   neighbouring optimum (theta_E %+.2f deg) at (%d, %d): cert %.3e, wall vs his Table 1"
        " max %.3e R_E" % (np.degrees(d_th), nr, nl, fn_["cert"]["worst"], dn))
    check("R-2 REJECTOR: the optimum for theta_E %+.2f deg leaves the ID-4 band (%.2e > %.2e)"
          % (np.degrees(d_th), dn, b4), dn > b4)
    rec["neighbour_miss"] = dn
    np.savez_compressed(os.path.join(ART, "inverse_wall.npz"), wall=fa["wall"], term=fa["term"],
                        table1=TAB1)
    rec["npass"] = list(NPASS)
    fn = os.path.join(ART, "derive_%s.json" % time.strftime("%Y-%m-%d"))
    json.dump(rec, open(fn, "w"), indent=1, default=float)
    say("   record: %s" % fn)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    say("VERDICT: %s" % ("PASS -- our march produces Rao's Table 1 from his optimality conditions"
                         if NPASS[0] == NPASS[1] else "FAIL"))
    return 0 if NPASS[0] == NPASS[1] else 1


# ======================================================================
# stage walk: the [X-RAOSQ] v3 instrument from OUR start
# ======================================================================
def start_from_ours(fa, x0, N):
    """The vertical cut at x0 through our inverse field: the traced wall
    point, then every ray's crossing with x = x0 above the wall, up to ED;
    N rows uniform in y, states linear in y between the crossings (the
    analogue of rao1961_twin.start_from_geno on our field)."""
    W = fa["wall"]
    yw = float(np.interp(x0, W[:, 0], W[:, 1]))
    tw, qw = float(np.interp(x0, W[:, 0], W[:, 2])), float(np.interp(x0, W[:, 0], W[:, 3]))
    ys, us, vs = [yw], [qw * np.cos(tw)], [qw * np.sin(tw)]
    for ray in fa["rays"]:
        dx = ray[:, 0] - x0
        idx = np.where(dx[:-1] * dx[1:] <= 0.0)[0]
        for j in idx:
            if dx[j + 1] == dx[j]:
                continue
            t = dx[j] / (dx[j] - dx[j + 1])
            pt = ray[j] + t * (ray[j + 1] - ray[j])
            if pt[1] > yw:
                ys.append(float(pt[1]))
                us.append(float(pt[2]))
                vs.append(float(pt[3]))
    o = np.argsort(ys)
    ys, us, vs = np.asarray(ys)[o], np.asarray(us)[o], np.asarray(vs)[o]
    yq = np.linspace(ys[0], ys[-1], N)
    return (x0, yq, np.interp(yq, ys, us), np.interp(yq, ys, vs)), float(ys[-1])


def walk_world(fa):
    """rao1961_sqp_return's World, set up as its setup() does, with OUR
    start line and HIS Table 1 as the reference wall."""
    import rao1961_sqp_return as SR
    w = SR.World()
    wd = build_world()
    w.tab, w.ta, w.pa, w.qpa = wd["tab"], wd["ta"], wd["pa"], wd["qpa"]
    cs = his_wall()
    xd = np.linspace(TAB1[0, 0], TAB1[-1, 0], INV["ed_points"])
    w.wall = np.stack([xd, cs(xd)], 1)
    w.xD = float(TAB1[-1, 0])
    w.start, ytop = start_from_ours(fa, SR.X0, SR.N_ROW)
    stl = np.stack([np.full(len(w.start[1]), SR.X0), w.start[1], w.start[2], w.start[3]], 1)
    _, w.F_in = PM.col_fluxes(stl, w.ta, w.pa, 1.0)
    w.xs0 = SR.X0 + SR.FREEZE * (w.xD - SR.X0)
    w.yw0 = float(cs(w.xs0))
    w.slope0 = float(cs(w.xs0, 1))
    w.xk = w.xs0 + (w.xD - w.xs0) * np.arange(1, SR.M_NODES + 1) / SR.M_NODES
    w.yD = float(TAB1[-1, 1])
    w.W_fit = np.asarray(cs(w.xk[:-1]), float)
    say("   walk world: our start at x0 %.2f, %d rows from the traced wall (y %.5f) to ED (y %.5f);"
        " F_in %.6g N; his Table 1 as the reference wall; frozen to his contour on [%.2f, %.4f];"
        " %d knots (tip pinned at y_D %.3f)" % (SR.X0, len(w.start[1]), w.start[1][0], ytop,
                                                 w.F_in, SR.X0, w.xs0, SR.M_NODES, w.yD))
    return SR, w


def walk():
    t00 = time.time()
    os.makedirs(ART, exist_ok=True)
    say("== [F3] Rao 1961 Table 1: the TR-SQP re-obtention from OUR start [X-RAOPO] (stage walk) ==")
    w0 = build_world()
    nr, nl = INV["ladder"][-1]
    fa = inverse_fan(w0, nr, nl)
    say("   our field: inverse march (%d, %d), cert %.3e" % (nr, nl, fa["cert"]["worst"]))
    SR, w = walk_world(fa)
    for k_, v_ in (("X0", "x0"), ("N_ROW", "N"), ("K_ST", "K"), ("M_NODES", "M_knots"),
                   ("FREEZE", "freeze"), ("PERT", "perturb"), ("MAXSEG", "iters"),
                   ("SEG_R1", "seg_r1"), ("TR0", "tr0")):
        if abs(float(getattr(SR, k_)) - float(WALK[v_])) > np.finfo(float).eps * max(1.0, abs(WALK[v_])):
            raise ValueError("the [X-RAOSQ] instrument's %s is %s, the posing of record %s"
                             % (k_, getattr(SR, k_), WALK[v_]))
    starts = os.environ.get("RAOPO_START", "perturb,line").split(",")
    # S1 the reference in spline space and the bands (SR v3, verbatim)
    e_rep = SR.wall_dist(w.W_fit, w)
    out_fit, S_fit = SR.march_record(w.W_fit, w)
    J_fit, g_fit = SR.J_and_grad(w.W_fit, w, S_fit)
    g_floor = float(np.max(np.abs(g_fit)))
    gtol = K_RICH * g_floor
    out_fit2, _ = SR.march_record(w.W_fit, w, K=2 * SR.K_ST - 1)
    J_fit2 = float(w.F_in + SR.push_of(out_fit2, w))
    say("   his contour in spline space: e_rep %.3e; record cert %.3e; J_fit %.8e (K %d) vs %.8e"
        " (K %d); grad floor %.3e -> gtol %.3e" % (e_rep, float(out_fit["cert_worst"]), J_fit,
                                                  SR.K_ST, J_fit2, 2 * SR.K_ST - 1, g_floor, gtol))
    check("RE-0 his contour marched from our start certifies (%.3e)" % float(out_fit["cert_worst"]),
          float(out_fit["cert_worst"]) <= 1.0)
    t1 = time.time()
    sp = SR.spectrum_at(w.W_fit, w, S_fit, g_fit, e_rep)
    SR.print_spectrum(sp, w.W_fit * (1.0 + SR.PERT * np.array([(-1.0) ** k for k in range(len(w.W_fit))])),
                      w.W_fit)
    band_J = K_RICH * abs(J_fit - J_fit2) + float(np.sum(np.abs(g_fit))) * float(np.max(sp["band"]))
    say("   spectrum %.0f s; band_J %.3e" % (time.time() - t1, band_J))
    rec = dict(e_rep=e_rep, J_fit=J_fit, g_floor=g_floor, gtol=gtol, band=sp["band"].tolist(),
               c=sp["c"].tolist(), band_J=band_J, W_fit=w.W_fit.tolist(), xk=w.xk.tolist(), starts={})
    land = {}
    for name in starts:
        if name == "perturb":
            W0 = w.W_fit * (1.0 + SR.PERT * np.array([(-1.0) ** k for k in range(len(w.W_fit))]))
        elif name == "line":
            W0 = w.yw0 + (w.yD - w.yw0) * (w.xk[:-1] - w.xs0) / (w.xD - w.xs0)
        else:
            raise ValueError("RAOPO_START %s" % name)
        a0 = SR.components(W0, w.W_fit, sp)
        d0 = SR.wall_dist(W0, w)
        say("-- start '%s': dist to his wall %.3e; outside its band in %d of %d directions (worst"
            " %.1fx) --" % (name, d0, int(np.sum(np.abs(a0) > sp["band"])), len(a0),
                            float(np.max(np.abs(a0) / sp["band"]))))
        t1 = time.time()
        W_s, J_s, g_s, n_rec, wc = SR.run_trsqp(W0, w, +1.0, tag="max ")
        ok3, a_s, r_s = SR.return_v3(W_s, w.W_fit, sp)
        d_s = SR.wall_dist(W_s, w)
        say("   landing: %d records, worst accepted cert %.3e, %.0f s; J %.8e (J - J_fit %+.3e);"
            " |grad|inf %.3e (gtol %.3e); dist %.3e; by direction |a|/band %s"
            % (n_rec, wc, time.time() - t1, J_s, J_s - J_fit, np.max(np.abs(g_s)), gtol, d_s,
               np.array2string(r_s, precision=2)))
        lab = {"perturb": "RE-1b from [X-RAOSQ]'s 1.5-percent perturbed start",
               "line": "RE-1 from the GENERIC chord start"}[name]
        check("%s: every accepted base certified (%.3e)" % (lab, wc), wc <= 1.0)
        check("   ... CONVERGENCE |grad J(W*)|inf %.3e <= gtol %.3e" % (np.max(np.abs(g_s)), gtol),
              np.max(np.abs(g_s)) <= gtol)
        check("   ... RETURN: every eigen-direction of W* - W_fit inside its band (worst %.2f, dir %d)"
              % (r_s.max(), int(np.argmax(r_s))), ok3)
        check("   ... VALUE |J(W*) - J_fit| %.3e <= band_J %.3e" % (abs(J_s - J_fit), band_J),
              abs(J_s - J_fit) <= band_J)
        land[name] = W_s
        rec["starts"][name] = dict(W0=W0.tolist(), W=np.asarray(W_s).tolist(), J=float(J_s),
                                   ratio=r_s.tolist(), dist=d_s, n_rec=n_rec, cert=wc,
                                   grad_inf=float(np.max(np.abs(g_s))))
        if name == "perturb":
            t1 = time.time()
            W_r, J_r, _, n_r, _ = SR.run_trsqp(W0, w, -1.0, max_segments=SR.SEG_R1, tag="min ")
            d_r = SR.wall_dist(W_r, w)
            check("R-3 REJECTOR: the sign-flipped driver ends FARTHER from his contour (%.3e >"
                  " %.3e; %d records, %.0f s)" % (d_r, d0, n_r, time.time() - t1), d_r > d0)
            rec["starts"]["rejector"] = dict(W=np.asarray(W_r).tolist(), dist=d_r)
    if "line" in land and "perturb" in land:
        r_lp = np.abs(SR.components(land["line"], land["perturb"], sp)) / sp["band"]
        check("RE-3 COINCIDENCE: the two landings coincide (worst %.2f of band, sup %.2e)"
              % (r_lp.max(), SR.wall_gap(land["line"], land["perturb"], w)),
              bool(np.all(r_lp <= 1.0)))
    rec["npass"] = list(NPASS)
    fn = os.path.join(ART, "walk_%s.json" % time.strftime("%Y-%m-%d_%H%M"))
    json.dump(rec, open(fn, "w"), indent=1, default=float)
    say("   record: %s" % fn)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    say("VERDICT: %s" % ("PASS -- the TR-SQP re-obtains Rao's Table 1 from our start"
                         if NPASS[0] == NPASS[1] else "FAIL"))
    return 0 if NPASS[0] == NPASS[1] else 1


def rejector():
    """R-3 ATTRIBUTION (stage rejector, S37): the sign-flipped driver alone
    from the perturbed start, with the segment budget RAOPO_SEG_R1 (default
    the record's SEG_R1 of [X-RAOSQ]). MEASURED in the walk of record: with
    the record's 14 segments every trial of the sign-flipped driver was an
    uncertified record (cert 1e15-1e18) and it never took a step; the same
    instrument in Rao's world with GENO's start took its first step at
    segment 11 of 14. This stage measures whether a larger budget (a smaller
    radius reached) lets it step, and where it goes."""
    t00 = time.time()
    os.makedirs(ART, exist_ok=True)
    w0 = build_world()
    nr, nl = INV["ladder"][-1]
    fa = inverse_fan(w0, nr, nl)
    SR, w = walk_world(fa)
    budget = int(os.environ.get("RAOPO_SEG_R1", SR.SEG_R1))
    say("== [F3] R-3 attribution: the sign-flipped driver from the perturbed start, budget %d"
        " segments (record %d) ==" % (budget, SR.SEG_R1))
    W0 = w.W_fit * (1.0 + SR.PERT * np.array([(-1.0) ** k for k in range(len(w.W_fit))]))
    d0 = SR.wall_dist(W0, w)
    W_r, J_r, _, n_r, wc = SR.run_trsqp(W0, w, -1.0, max_segments=budget, tag="min ")
    d_r = SR.wall_dist(W_r, w)
    moved = SR.wall_gap(W_r, W0, w)
    say("   result: %d records, worst accepted cert %.3e; J %.8e; dist to his contour %.3e (start"
        " %.3e); moved %.3e from the start; %.0f s" % (n_r, wc, J_r, d_r, d0, moved, time.time() - t00))
    ok = check("R-3 REJECTOR (budget %d): the sign-flipped driver ends FARTHER from his contour"
               " (%.3e > %.3e)" % (budget, d_r, d0), d_r > d0)
    json.dump(dict(budget=budget, d0=d0, d_r=d_r, moved=moved, n_rec=n_r, J_r=float(J_r),
                   W_r=np.asarray(W_r).tolist()),
              open(os.path.join(ART, "rejector_%s_budget%d.json" % (time.strftime("%Y-%m-%d"), budget)), "w"),
              indent=1)
    return 0 if ok else 1


if __name__ == "__main__":
    stage = os.environ.get("RAOPO_STAGE", "derive")
    sys.exit({"derive": derive, "walk": walk, "rejector": rejector}[stage]())
