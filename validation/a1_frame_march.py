"""The plug march in a ROTATED frame [F3/A1, S32]: the axisymmetric
cells of the record with the source term read in the true radius.

WHY. The throat kernel (a1_throat_kernel, [X-TKRN]) delivers its start
line in the THROAT's own frame -- x along the mean flow direction at
the throat, tilted by theta_t (-56.9 deg on Chutkey's plug) -- and
from a sonic lip the C- family points UPSTREAM in the record's x
(theta - mu < -90 deg until M > 1/sin(90 deg - |theta_t|) = 1.83 on
that plug: the S31 section 3.3 limit, measured). A march in x cannot
carry that strip; a march in the throat frame can, because there
theta' - mu = -85 deg at the lip and rises. The record's cells are
written in (x, y = r): the characteristic slopes tan(theta +- mu) are
geometric and frame-free, the ONLY frame-bound term is the
axisymmetric source delta c^2 v / y (A1._coef), which in a frame
rotated by theta_t reads delta c^2 v_r / r with v_r = u sin theta_t +
v cos theta_t and r = Y_0 + x sin theta_t + y cos theta_t. This file
is that one change, threaded through the three cell types of the plug
march by its own `cells=` seam (the swirl seam of S24): interior
(bottom-up), bottom wall, free jet. With theta_t = 0 and Y_0 = 0 every
expression is the record's, bit for bit (gate F-0).

THE A/B (stage frame). The same physical problem twice: Chutkey's
plug from the axisymmetric fan's cut (the S31 twin's case, X-CHTW) in
the record's frame, and the SAME start line, wall and edge rotated
into the throat frame and marched there with the rotated cells. Two
independent discretisation geometries of one flow: the wall pressure
against the wall's arc length must agree within the record's own
resolution band, derived from its (81,41) -> (161,81) ladder
(K_RICH x the difference). The wall states are frame-free scalars;
the column fluxes are read after rotating the columns back.

STAGE STRIP (measured 2026-09-21, NEGATIVE, kept as the record of the
attempt): Chutkey's plug marched from a uniform line ON THE THROAT LINE
(M_i 1.02-1.20, tilted by nu(M_i) so the lip fan ends axial, the fan as
the record's planar corner wave on a cut d half-heights downstream)
does NOT march: the wall cells fail within the first 0.7 mm (kst 1-10)
at every M_i and every cut tried (d 0.1, 0.5), on the digitised
contour AND on Angelino's own streamline for the foot region
(FRM_WALL=angelino), and the mesh folds downstream (mass +140..+950
percent by mid-plug). Two obstacles, both measured: (i) the digitised
contour's foot is noise at the 0.1-mm scale (chords +-8 deg, the
clamped smoothing spline turns 5 deg within 0.2 mm, 10x the ideal
wall's rate); (ii) the near-sonic wall cells (M 1.02-1.2, mu 57-79
deg) with the corner fan 0.1-0.5 h away -- the S31 conditioning limit
in the throat frame. The record's construction (the cut at 1.5 mm on
the ideal fan, wall M 1.72) is what marches; its X0 ladder extends to
1.0 mm in both frames with identical readings (see the S32 log, 8).

STAGE KERNEL (2026-09-21 evening, NEGATIVE as posed, the cause read):
the plug marched from the ANNULAR KERNEL's line [X-ANKR] (L-b posing:
the plug-wall throat radius posed 1.5 d, cowl straight, R_c 3, eps
0.20; the cut at z 0.5 = 0.65 mm, the lip 0.13 mm upstream on the
cowl at M 1.08). The kernel line itself is sound -- M 1.11 (cowl) to
1.55 (plug), direction -7.4..0 deg, mass 0.954 of the choked 1-D --
but the lip fan posed as the record's planar corner wave ON A CUT
carried a JUMP across its leading ray (lip state M 1.08 against the
field's 1.15) and the march folded. THE CORNER FAN IN A NON-UNIFORM
FIELD (corner_fan, night): the centred expansion marched as a Goursat
problem through the kernel field -- the leading ray traced through
the field, every next ray a C- from the lip with the corner
relation's state, its points solved by the top-down rotated cell from
the previous point on the ray (C-) and the same-index point on the
previous ray (C+). MEASURED: 24 rays, worst cell certification 0.016,
the cut data continuous across the leading ray (kernel M 1.109 ->
fan 1.134). With it the march no longer fails at the cut: the first
column loses 2.4 percent (the vertical-start wedge, the record's
own), the mass then holds to column 11, and at x' 1.7 mm the wall
cell consumes 18 rows at once and the mesh folds -- the POSED L-b
wall (the throat parabola curving away up to 0.4 d, then a cubic
transition bending 20 deg UP to the Angelino contour) is a
compression turn, i.e. a shock, which no march of characteristics
carries. READ: the external plug (Angelino) is not a series-kernel
geometry -- its plug wall turns INTO the channel at the foot while
every throat series needs walls curving away on both sides -- and the
consistent L-b geometry is an internal-external plug. The tools are
complete (kernel, corner fan, frame march); their twin is an
internal-external plug: Humphreys' configuration once its throat
radii are known, or a posed one whose plug wall keeps diverging.

Usage:
    python validation/a1_frame_march.py                  # stage frame
    FRM_STAGE=strip FRM_MI=1.05 FRM_D=0.1 [FRM_WALL=angelino] ...
    FRM_STAGE=kernel FRM_ZCUT=0.5 FRM_RCIN=1.5 [FRM_RCOUT=..]
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1                        # noqa: E402
import a1_plug_march as PM                             # noqa: E402
import a1_chutkey_twin as CT                           # noqa: E402
import jax                                             # noqa: E402
import jax.numpy as jnp                                # noqa: E402

NPASS = [0, 0]
HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.environ.get("FRM_ART", os.path.join(HERE, "_frame_march"))
import json                                            # noqa: E402
CASES = {k: v["value"] for k, v in json.load(
    open(os.path.join(HERE, "frame_march_cases.json"))).items() if k[0] != "_"}
REC = {float(k): tuple(v) for k, v in CASES["record_readings_s31"].items()}


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


# ======================================================================
# the rotated cells
# ======================================================================
def coef_rot(u, v, x, y, ta, delta, th, Y0):
    """A1._coef with the source in the TRUE radius: the frame is
    rotated by th (record -> frame), its origin at radius Y0."""
    q = jnp.sqrt(u * u + v * v)
    Aa = jnp.arctan2(v, u)
    _, _, _, c, _, M = A1.state_q(q, ta)
    mu = jnp.arcsin(1.0 / M)
    lm = jnp.tan(Aa - mu)
    lp = jnp.tan(Aa + mu)
    qq = u * u - c * c
    st, ct = jnp.sin(th), jnp.cos(th)
    r = Y0 + x * st + y * ct
    vr = u * st + v * ct
    s = delta * c * c * vr / r
    return lm, lp, qq, 2.0 * u * v, s


def make_resid_interior_rot(delta, th, Y0):
    def resid(z, p, ta):
        x4, y4, u4, v4 = z
        x1, y1, u1, v1, x2, y2, u2, v2 = p
        up, vp = 0.5 * (u1 + u4), 0.5 * (v1 + v4)
        xp, yp = 0.5 * (x1 + x4), 0.5 * (y1 + y4)
        _, lp, qp, rp0, sp = coef_rot(up, vp, xp, yp, ta, delta, th, Y0)
        rp = rp0 - qp * lp
        um, vm = 0.5 * (u2 + u4), 0.5 * (v2 + v4)
        xm, ym = 0.5 * (x2 + x4), 0.5 * (y2 + y4)
        lm, _, qm, rm0, sm = coef_rot(um, vm, xm, ym, ta, delta, th, Y0)
        rm = rm0 - qm * lm
        return jnp.array([
            (y4 - y1) - lp * (x4 - x1),
            (y4 - y2) - lm * (x4 - x2),
            (qp * u4 + rp * v4 - (sp * (x4 - x1) + qp * u1 + rp * v1))
            / _q3(up, vp),
            (qm * u4 + rm * v4 - (sm * (x4 - x2) + qm * u2 + rm * v2))
            / _q3(um, vm),
        ])
    return resid


def _q3(u, v):
    """The compatibility rows are DIVIDED by q_m^3 (a smooth positive
    factor: the root is the record's, the Newton step is affine-
    invariant, only the DAMPING of A1's solver reads the residual
    norm). Measured on Chutkey's case rotated into the throat frame,
    wall cell at station 79 (r 0.015 R): unscaled, the geometric row
    (1e-2) and the compatibility row (1e6) make the norm test accept
    a half step and then stall (metric 3.7, the record's own cell at
    the same physical point converges); scaled by 1/q^3 both rows are
    O(1) and the damped Newton converges (3e-14). The record's cells
    in the record's frame never needed it; a rotated frame moves the
    seed (chord midpoint, previous wall u) relative to the root."""
    q2 = u * u + v * v
    return q2 * jnp.sqrt(q2)


def make_resid_interior_td_rot(delta, th, Y0):
    """The record's TOP-DOWN interior cell (A1.make_resid_interior: the
    C- runs from pt1 within the column, the C+ arrives from pt2 on the
    previous column) with the source in the true radius and the
    compatibility rows scaled (_q3): the cell of the corner fan, whose
    columns are the C- rays from the lip."""
    def resid(z, p, ta):
        x4, y4, u4, v4 = z
        x1, y1, u1, v1, x2, y2, u2, v2 = p
        um, vm = 0.5 * (u1 + u4), 0.5 * (v1 + v4)
        xm, ym = 0.5 * (x1 + x4), 0.5 * (y1 + y4)
        lm, _, qm, rm0, sm = coef_rot(um, vm, xm, ym, ta, delta, th, Y0)
        rm = rm0 - qm * lm
        up, vp = 0.5 * (u2 + u4), 0.5 * (v2 + v4)
        xp, yp = 0.5 * (x2 + x4), 0.5 * (y2 + y4)
        _, lp, qp, rp0, sp = coef_rot(up, vp, xp, yp, ta, delta, th, Y0)
        rp = rp0 - qp * lp
        return jnp.array([
            (y4 - y1) - lm * (x4 - x1),
            (y4 - y2) - lp * (x4 - x2),
            (qm * u4 + rm * v4 - (sm * (x4 - x1) + qm * u1 + rm * v1)) / _q3(um, vm),
            (qp * u4 + rp * v4 - (sp * (x4 - x2) + qp * u2 + rp * v2)) / _q3(up, vp),
        ])
    return resid


def make_resid_wallbot_rot(delta, th, Y0):
    def resid(z, p, ta):
        y2, u4 = z
        xA, yA, uA, vA, xB, yB, uB, vB, x4, y4, slope = p
        D = (y2 - yA) / (yB - yA)
        x2 = xA + D * (xB - xA)
        u2 = uA + D * (uB - uA)
        v2 = vA + D * (vB - vA)
        v4 = slope * u4
        um, vm = 0.5 * (u2 + u4), 0.5 * (v2 + v4)
        xm, ym = 0.5 * (x2 + x4), 0.5 * (y2 + y4)
        lm, _, qm, rm0, sm = coef_rot(um, vm, xm, ym, ta, delta, th, Y0)
        rm = rm0 - qm * lm
        return jnp.array([
            (y4 - y2) - lm * (x4 - x2),
            ((qm + slope * rm) * u4
             - (sm * (x4 - x2) + qm * u2 + rm * v2)) / _q3(um, vm),
        ])
    return resid


def make_resid_freejet_rot(delta, th, Y0):
    def resid(z, p, ta):
        x4, y4, th4 = z
        x1, y1, u1, v1, x3, y3, u3, v3, qpa = p
        u4 = qpa * jnp.cos(th4)
        v4 = qpa * jnp.sin(th4)
        um, vm = 0.5 * (u1 + u4), 0.5 * (v1 + v4)
        xm, ym = 0.5 * (x1 + x4), 0.5 * (y1 + y4)
        _, lp, qp, rp0, sp = coef_rot(um, vm, xm, ym, ta, delta, th, Y0)
        rp = rp0 - qp * lp
        th3 = jnp.arctan2(v3, u3)
        thm = 0.5 * (th3 + th4)
        return jnp.array([
            (y4 - y1) - lp * (x4 - x1),
            ((qp * u4 + rp * v4)
             - (sp * (x4 - x1) + qp * u1 + rp * v1)) / _q3(um, vm),
            (y4 - y3) - jnp.tan(thm) * (x4 - x3),
        ])
    return resid


def make_cells_rot(delta, th, Y0):
    """The (t_int, t_fj, t_wb) triple for plug_march(cells=...)."""
    th, Y0 = float(th), float(Y0)
    t_int = A1.get_solver(("intbu_rot", delta, th, Y0),
                          lambda: make_resid_interior_rot(delta, th, Y0))
    t_fj = A1.get_solver(("fj_rot", delta, th, Y0),
                         lambda: make_resid_freejet_rot(delta, th, Y0))
    t_wb = A1.get_solver(("wb_rot", delta, th, Y0),
                         lambda: make_resid_wallbot_rot(delta, th, Y0))
    return t_int, t_fj, t_wb


# ======================================================================
# the frame: record <-> rotated
# ======================================================================
def to_frame(X, Y, U, V, th, X0, Y0):
    """Record -> frame rotated by th with origin (X0, Y0)."""
    ct, st = np.cos(th), np.sin(th)
    x = (X - X0) * ct + (Y - Y0) * st
    y = -(X - X0) * st + (Y - Y0) * ct
    u = U * ct + V * st
    v = -U * st + V * ct
    return x, y, u, v


def to_record(x, y, u, v, th, X0, Y0):
    ct, st = np.cos(th), np.sin(th)
    X = X0 + x * ct - y * st
    Y = Y0 + x * st + y * ct
    U = u * ct - v * st
    V = u * st + v * ct
    return X, Y, U, V


def rotate_case(c, th, X0, Y0, n_dense=None):
    """The twin's case (start line on a vertical cut, wall stations
    with slopes, edge speed) posed in the rotated frame: the start
    line becomes a per-row x0 array (the driver's characteristic
    posing), the wall is rotated densely and resampled at K stations
    of the frame's x from the start line's wall point to the tip."""
    x0, yline, us, vs = c["start"]
    xs, ys, u_s, v_s = to_frame(np.full_like(yline, x0), yline, us, vs,
                                th, X0, Y0)
    # the wall, densely, from the twin's spline (single-valuedness check)
    from a1_toc_variational_jax import spline_coeffs, spline_eval
    n_dense = CASES["frame_defaults"]["n_dense"] if n_dense is None else n_dense
    cx, cy = c["cx"], c["cy"]
    Mc = spline_coeffs(jnp.asarray(cx), jnp.asarray(cy), float(CT.FOOT_SLOPE))
    xd = np.linspace(float(x0), float(cx[-1]), n_dense)
    yd, sd = jax.vmap(lambda xx: spline_eval(xx, jnp.asarray(cx),
                                             jnp.asarray(cy), Mc))(jnp.asarray(xd))
    yd, sd = np.asarray(yd), np.asarray(sd)
    xw, yw, _, _ = to_frame(xd, yd, np.zeros_like(xd), np.zeros_like(xd),
                            th, X0, Y0)
    if np.any(np.diff(xw) <= 0.0):
        raise ValueError("the wall is not single-valued in the frame's x")
    K = c["K"]
    ct, st = np.cos(th), np.sin(th)
    # the SAME wall points as the record's (its x-stations, evaluated
    # on the spline exactly), rotated: the A/B then differs by the
    # frame alone, never by the station distribution (measured: x'-
    # equispaced stations are 2.7x coarser at the tip, and the wall
    # cell fails there at r ~ 0.02 R)
    xr = np.asarray(c["stations"][0])
    yv, sv = np.asarray(c["stations"][1]), np.asarray(c["stations"][2])
    xq, yq, _, _ = to_frame(xr, yv, np.zeros_like(xr), np.zeros_like(xr), th, X0, Y0)
    # the tangent (1, s) rotated: exact at theta = 0
    sq = (sv * ct - st) / (ct + sv * st)
    return dict(stations=(xq, yq, sq), start=(xs, ys, u_s, v_s),
                qpa=c["qpa"], K=K, N=c["N"], wall_dense=(xw, yw))


def march_rot(w, c_rot, th, Y0, cells=True):
    t0 = time.time()
    out, sched = PM.plug_march(c_rot["stations"], c_rot["start"], c_rot["qpa"],
                               w["tab"], 1.0, edge_fill=CT.EDGE_FILL,
                               cells=(make_cells_rot(1.0, th, Y0) if cells
                                      else None))
    wall = np.asarray(out["wall"])
    q = np.hypot(wall[:, 2], wall[:, 3])
    T, p, rho, cs, gam, M = [np.asarray(v) for v in
                             A1.state_q(jnp.asarray(q), w["ta"])]
    return dict(wall=wall, p=p, M=M, cert=float(out["cert_worst"]),
                cert_n=int(out["cert_n"]), seconds=time.time() - t0,
                last_col=np.asarray(out["last_col"]),
                where=out.get("cert_where"))


def spacelike(xl, yl, ul, vl, ta):
    """Along a start line: the angle between the line and the flow
    minus mu at each row (positive = space-like there)."""
    q = np.hypot(ul, vl)
    M = np.asarray(A1.state_q(jnp.asarray(q), ta)[5])
    mu = np.arcsin(1.0 / M)
    d = np.stack([np.gradient(xl), np.gradient(yl)], 1)
    d /= np.linalg.norm(d, axis=1)[:, None]
    f = np.stack([ul, vl], 1) / q[:, None]
    a = np.arccos(np.clip(np.abs(np.sum(d * f, 1)), 0.0, 1.0))
    return a - mu, M


def arc(x, y):
    return np.concatenate([[0.0], np.cumsum(np.hypot(np.diff(x), np.diff(y)))])


# ======================================================================
# stage frame
# ======================================================================
def frame():
    t00 = time.time()
    print("== [F3/A1] the plug march in a rotated frame: the A/B on"
          " Chutkey's case (stage frame) ==", flush=True)
    w = CT.build_world()
    fan = CT.fan_axi_lip(w)
    K, N = int(os.environ.get("FRM_K", CASES["frame_defaults"]["K"])), int(os.environ.get("FRM_N", CASES["frame_defaults"]["N"]))
    c = CT.build_case(w, K=K, N=N, fan=fan)
    print("   case (%d, %d): cut X0 %.2f mm, y_w0 %.3f mm, %d rows"
          % (K, N, c["x0"] * CT.MM, c["yw0"] * CT.MM, N), flush=True)
    sl, Ml = spacelike(np.full(N, c["x0"]), c["start"][1], c["start"][2],
                       c["start"][3], w["ta"])
    print("   the cut: M %.3f..%.3f, angle(line, flow) - mu from %+.1f deg at"
          " the wall to %+.1f deg at the edge (%d/%d rows space-like)"
          % (Ml.min(), Ml.max(), np.degrees(sl[0]), np.degrees(sl[-1]),
             int((sl > 0).sum()), N), flush=True)
    r0 = CT.march(w, c)
    print("   record frame: cert %.3f (%d cells) at %s, %.1f s"
          % (r0["cert"], r0["cert_n"], r0.get("where"), r0["seconds"]), flush=True)
    s0 = arc(r0["wall"][:, 0], r0["wall"][:, 1])

    # F-0: the rotated cells at theta = 0, origin 0 = the record's, bit for bit
    c_id = rotate_case(c, 0.0, 0.0, 0.0)
    r_id = march_rot(w, c_id, 0.0, 0.0)
    dw = float(np.max(np.abs(r_id["wall"] - r0["wall"])
                      / np.maximum(1.0, np.abs(r0["wall"]))))
    # the roots are the record's; the Newton paths are not (the scaled
    # compatibility rows, _q3, and XLA's fusion of the frame-constant
    # terms): the two marches agree to the certification class
    # propagated over the mesh, never bit for bit (measured 1.4e-14
    # relative with unscaled rows)
    tol0 = A1.NEWTON_TOL_FACTOR * A1.EPS * float(r0["cert_n"])
    check("F-0 rotated cells at theta = 0: the wall array equals the record's"
          " within the certification class (max rel |diff| %.1e <= %.1e;"
          " cert %.3f vs %.3f, both certified)"
          % (dw, tol0, r_id["cert"], r0["cert"]),
          dw <= tol0 and r_id["cert"] <= 1.0 and r0["cert"] <= 1.0)

    # the record's own resolution band on p(s): (K, N) vs (2K-1, 2N-1)
    c2 = CT.build_case(w, K=2 * K - 1, N=2 * N - 1, fan=fan)
    r2 = CT.march(w, c2)
    s2 = arc(r2["wall"][:, 0], r2["wall"][:, 1])
    p2_on_0 = np.interp(s0, s2, r2["p"])
    band = A1.K_RICH * np.abs(r0["p"] - p2_on_0)
    print("   record ladder (%d,%d) -> (%d,%d): cert %.3f, max |dp|/p_0 %.2e"
          " -> band K_RICH x that" % (K, N, 2 * K - 1, 2 * N - 1, r2["cert"],
                                     float(np.max(np.abs(r0["p"] - p2_on_0)) / w["P0"])),
          flush=True)

    # F-1/F-2: the throat frame
    th = np.radians(-CT.TILT_DEG)
    Xm = 0.5 * (CT.FOOT[0] * CT.S_LEN + 0.0)
    Ym = 0.5 * (CT.FOOT[1] * CT.S_LEN + CT.R_LIP * CT.S_LEN)
    c_r = rotate_case(c, th, Xm, Ym)
    r_r = march_rot(w, c_r, th, Ym)
    X, Y, U, V = to_record(r_r["wall"][:, 0], r_r["wall"][:, 1],
                           r_r["wall"][:, 2], r_r["wall"][:, 3], th, Xm, Ym)
    sr = arc(X, Y)
    pr_on_0 = np.interp(s0, sr, r_r["p"])
    gap = np.abs(pr_on_0 - r0["p"])
    inband = gap <= np.maximum(band, A1.EPS * w["P0"])
    print("   throat frame (theta_t %.1f deg): cert %.3f (%d cells) at %s, %.1f s;"
          " wall p vs the record's on the arc: max |dp|/p_0 %.2e, %d/%d"
          " stations inside the band, worst gap/band %.2f"
          % (CT.TILT_DEG, r_r["cert"], r_r["cert_n"], r_r["where"], r_r["seconds"],
             float(np.max(gap) / w["P0"]), int(inband.sum()), len(inband),
             float(np.max(gap / np.maximum(band, A1.EPS * w["P0"])))), flush=True)
    check("F-1 the rotated-frame march certifies (%.3f)" % r_r["cert"],
          r_r["cert"] <= 1.0)
    check("F-2 the rotated-frame wall pressure lies inside the record's"
          " resolution band at every station (%d/%d)"
          % (int(inband.sum()), len(inband)), bool(np.all(inband)))
    # F-3: the source is ALIVE in the frame -- with the record's cells
    # (source in the frame's y as if it were the radius) the march
    # must differ from the rotated one beyond the band
    r_w = march_rot(w, c_r, th, Ym, cells=False)
    gw = np.abs(r_w["p"] - r_r["p"])
    print("   control (record's cells in the rotated frame, source in y'):"
          " cert %.3f, max |dp|/p_0 vs the rotated cells %.2e"
          % (r_w["cert"], float(np.max(gw) / w["P0"])), flush=True)
    check("F-3 the rotated source is alive: the frame's y read as the radius"
          " moves the wall pressure beyond the band (%.2e > %.2e)"
          % (float(np.max(gw)), float(np.max(band))),
          float(np.max(gw)) > float(np.max(band)))
    os.makedirs(ART, exist_ok=True)
    np.savez(os.path.join(ART, "frame_%d_%d.npz" % (K, N)), s0=s0, p0=r0["p"],
             band=band, pr=pr_on_0, p_ctrl=r_w["p"], wall_rot=r_r["wall"])
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return NPASS[0] == NPASS[1]


# ======================================================================
# stage strip: Chutkey's plug marched ON THE CONTOUR from a start line
# at the throat, in the throat frame (the owner's posing of 18-09:
# "the throat kernel forward from the sonic line, computed on the
# contour"). The start data are DECLARED (no transonic kernel applies:
# Chutkey's primary nozzle is a symmetric convergent duct whose walls
# end in circular arcs of radius 0.867 mm on a half-height of 1.32 mm,
# R/h 0.66 -- outside every throat series, Moore's included, see the
# S32 log): a uniform line at M_i slightly above 1 on the throat line
# (Angelino's own assumption, made marchable), with an optional
# linear variation of the direction across it (Humphreys' 6 deg), and
# the lip fan as the record's planar corner wave. The region between
# the throat line and the cut at X0' = d half-heights is the fan's and
# the uniform state's; everything downstream is MARCHED on the real
# contour with the rotated cells -- against the record's posing, in
# which the first 1.5 mm of the wall are read on the ideal fan.
# ======================================================================
def _pm_fan(w, q1):
    """Planar corner wave from speed q1 to the ambient speed: the
    record's tables (a1_inlet_angle_opt.fan_at's integration), rays
    at angles phi = theta' - mu in the throat frame with theta' = 0
    on the leading ray."""
    ta = w["ta"]
    M_of = lambda q: float(A1.state_q(jnp.float64(q), ta)[5])   # noqa
    qs = np.linspace(q1, CT.q_at_pa(CT.PA, ta, w["as_"]), CASES["pm_fan_points"])
    Ms = np.array([M_of(q) for q in qs])
    mus = np.arcsin(np.clip(1.0 / Ms, 0, 1))
    dth = np.sqrt(np.maximum(Ms ** 2 - 1.0, 0.0)) / qs
    nu = np.concatenate([[0.0], np.cumsum(0.5 * (dth[1:] + dth[:-1]) * np.diff(qs))])
    return dict(qs=qs, ths=nu, mus=mus, phis=nu - mus, Ms=Ms)


def strip_case(w, MI, d, K, N, dth_deg=0.0):
    """The throat-frame case: wall stations (clustered at the throat),
    the start line on the cut x' = d h, the edge speed."""
    ta = w["ta"]
    th = np.radians(-CT.TILT_DEG)
    hh = 0.5 * CT.H_T * CT.S_LEN
    Xm = 0.5 * CT.FOOT[0] * CT.S_LEN
    Ym = 0.5 * (CT.FOOT[1] + CT.R_LIP) * CT.S_LEN
    xw, yw, sw = _wall_in_frame(w, th, Xm, Ym, os.environ.get("FRM_WALL", "digitised"),
                                float(os.environ.get("FRM_XBLEND_MM", CASES["angelino_blend_mm"][0])))
    x0 = d * hh
    # stations: geometric clustering from ds0 at the cut
    ds0, grow = CASES["station_clustering"][0] * hh, CASES["station_clustering"][1]
    ds_max = (xw[-1] - x0) / K
    xs, dsn = [x0], ds0
    while xs[-1] + dsn < xw[-1]:
        xs.append(xs[-1] + dsn)
        dsn = min(ds_max, dsn * grow)
    xq = np.array(xs[1:] + [xw[-1]])
    yq = np.interp(xq, xw, yw)
    sq = np.interp(xq, xw, sw)
    yw0, sw0 = float(np.interp(x0, xw, yw)), float(np.interp(x0, xw, sw))
    # the start data
    bq = CASES["brentq_q_window"]
    q_i = float(__import__("scipy.optimize", fromlist=["brentq"]).brentq(
        lambda q: float(A1.state_q(jnp.float64(q), ta)[5]) - MI,
        bq[0] * w["as_"], bq[1] * w["as_"], xtol=bq[2]))
    fan = _pm_fan(w, q_i)
    # the uniform line's direction: theta'_i = nu(M_i), so that the lip
    # fan (from M_i) still ends AXIAL in the record's frame -- Migdal's
    # tilted line; at M_i -> 1 it is the throat line's own normal
    full = _pm_fan(w, float(w["as_"]))
    th_i = float(np.interp(q_i, full["qs"], full["ths"]))
    fan["ths"] = fan["ths"] + th_i
    fan["phis"] = fan["phis"] + th_i
    dth = np.radians(dth_deg)
    y_lead = hh + x0 * np.tan(fan["phis"][0])          # the leading ray on the cut
    y_term = hh + x0 * np.tan(fan["phis"][-1])         # the terminal ray
    th_e = float(fan["ths"][-1])
    y_edge = hh + x0 * np.tan(th_e)                    # the jet boundary
    nA = max(3, int(round(N * (y_lead - yw0) / (y_edge - yw0))))
    nB = max(5, N - nA - 2)
    yA = np.linspace(yw0, y_lead, nA, endpoint=False)
    thA = th_i + dth * yA / hh / 2.0
    thA[0] = np.arctan(sw0)                            # the wall row follows the wall
    uA, vA = q_i * np.cos(thA), q_i * np.sin(thA)
    # the fan rows by ray angle (uniform in nu), cut at y' = hh + x0 tan(phi)
    nus = np.linspace(float(fan["ths"][0]), float(fan["ths"][-1]), nB)
    qB = np.interp(nus, fan["ths"], fan["qs"])
    phB = np.interp(nus, fan["ths"], fan["phis"])
    yB = hh + x0 * np.tan(phB)
    thB = nus + dth / 2.0
    uB, vB = qB * np.cos(thB), qB * np.sin(thB)
    yC = np.array([0.5 * (y_term + y_edge), y_edge])
    uC, vC = np.full(2, fan["qs"][-1] * np.cos(th_e + dth / 2.0)), np.full(2, fan["qs"][-1] * np.sin(th_e + dth / 2.0))
    ys = np.concatenate([yA, yB, yC])
    us = np.concatenate([uA, uB, uC])
    vs = np.concatenate([vA, vB, vC])
    assert np.all(np.diff(ys) > 0.0)
    start = (np.full(len(ys), x0), ys, us, vs)
    X, Y, U, V = to_record(start[0], ys, us, vs, th, Xm, Ym)
    md_in, F_in = PM.col_fluxes(np.stack([X, Y, U, V], 1), ta, CT.PA, 1.0)
    return dict(stations=(xq, yq, sq), start=start, qpa=float(fan["qs"][-1]),
                th=th, Xm=Xm, Ym=Ym, hh=hh, x0=x0, K=len(xq), N=len(ys),
                nA=nA, nB=nB, md_in=abs(md_in), F_in=F_in, q_i=q_i, th_i=th_i,
                y_lead=y_lead, y_edge=y_edge, wall_dense=(xw, yw))


def mass_by_column_frame(w, out, c, md0):
    cols = {}
    for (j, i), pt in zip(out["mesh_keys"], out["mesh_pts"]):
        cols.setdefault(i, []).append((j, np.asarray(pt)))
    rows = []
    for i in sorted(cols):
        col = np.array([pt for j, pt in sorted(cols[i])])
        X, Y, U, V = to_record(col[:, 0], col[:, 1], col[:, 2], col[:, 3],
                               c["th"], c["Xm"], c["Ym"])
        md, _ = PM.col_fluxes(np.stack([X, Y, U, V], 1), w["ta"], CT.PA, 1.0)
        rows.append((i, abs(md) / md0 - 1.0, len(col)))
    return rows


def strip():
    t00 = time.time()
    print("== [F3/A1] Chutkey's plug marched ON THE CONTOUR from the throat,"
          " in the throat frame (stage strip) ==", flush=True)
    w = CT.build_world()
    SD = CASES["strip_defaults"]
    MI = float(os.environ.get("FRM_MI", SD["MI"]))
    d = float(os.environ.get("FRM_D", SD["d"]))
    K, N = int(os.environ.get("FRM_K", SD["K"])), int(os.environ.get("FRM_N", SD["N"]))
    dth = float(os.environ.get("FRM_DTH", 0.0))
    c = strip_case(w, MI, d, K, N, dth)
    W_star = CT.choked_mass(w)
    print("   start: M_i %.3f uniform at theta' %.2f deg (direction variation"
          " %.1f deg across), cut at %.2f h = %.3f mm; %d rows (%d uniform, %d"
          " fan, 2 above); %d stations (first spacing %.3f mm); mass through"
          " the cut %.6f of the choked throat's"
          % (MI, np.degrees(c["th_i"]), dth, d, c["x0"] * CT.MM, c["N"],
                                            c["nA"], c["nB"], c["K"],
                                            (c["stations"][0][0] - c["x0"]) * CT.MM,
                                            c["md_in"] / W_star), flush=True)
    t0 = time.time()
    out, _ = PM.plug_march(c["stations"], c["start"], c["qpa"], w["tab"], 1.0,
                           cells=make_cells_rot(1.0, c["th"], c["Ym"]))
    wall = np.asarray(out["wall"])
    q = np.hypot(wall[:, 2], wall[:, 3])
    T, p, rho, cs, gam, M = [np.asarray(v) for v in A1.state_q(jnp.asarray(q), w["ta"])]
    cert = float(out["cert_worst"])
    print("   march: cert %.3f (%d cells) at %s, %.1f s" % (cert, int(out["cert_n"]),
                                                            out.get("cert_where"),
                                                            time.time() - t0), flush=True)
    check("S-1 the march from the throat line certifies (%.3f)" % cert, cert <= 1.0)
    rows = mass_by_column_frame(w, out, c, c["md_in"])
    m2, mmid, mlast = rows[1][1], rows[len(rows) // 2][1], rows[-1][1]
    print("   mass vs the cut: column 2 %+.5f, mid %+.5f, last %+.5f; vs the"
          " choked throat: last %+.5f" % (m2, mmid, mlast,
                                          (1.0 + mlast) * c["md_in"] / W_star - 1.0),
          flush=True)
    check("S-2 the mass is conserved from the cut to the last column"
          " (|dm/m| %.1e <= %.0e) -- no first-column jump on the real"
          " contour" % (abs(mlast), CT.MASS_TOL), abs(mlast) <= CT.MASS_TOL)
    # the wall in the record's frame: the reading at the four ATPN truncations
    X, Y, U, V = to_record(wall[:, 0], wall[:, 1], wall[:, 2], wall[:, 3],
                           c["th"], c["Xm"], c["Ym"])
    r = dict(wall=np.stack([X, Y, U, V], 1), p=p, M=M)
    st = CT.read_stations(w, c, r)
    worst_p, worst_M = 0.0, 0.0
    print("   wall state at the truncations (paper / this march / the record's"
          " fan-cut march of S31):")
    for row in st:
        rp, rM = REC[round(row["frac"], 2)]
        print("     %2.0f %%: p_w/p_0 %.5f / %.5f (%+.2e) / %.5f;  M %.3f / %.3f"
              " (%+.2e) / %.3f" % (100 * row["frac"], row["p_p0_meas"], row["p_p0"],
                                   row["p_p0"] / row["p_p0_meas"] - 1.0, rp,
                                   row["M_meas"], row["M"], row["M"] / row["M_meas"] - 1.0, rM))
        worst_p = max(worst_p, abs(row["p_p0"] / row["p_p0_meas"] - 1.0))
        worst_M = max(worst_M, abs(row["M"] / row["M_meas"] - 1.0))
    check("S-3 the wall pressure at the four truncations within the oracle's"
          " class %.0f percent (worst %.2e)" % (100 * CASES["wall_class"][0], worst_p),
          worst_p <= CASES["wall_class"][0])
    check("S-4 the wall Mach at the four truncations within %.0f percent (worst"
          " %.2e)" % (100 * CASES["wall_class"][1], worst_M), worst_M <= CASES["wall_class"][1])
    os.makedirs(ART, exist_ok=True)
    tag = "MI%.3f_d%.2f_K%d_N%d_dth%.1f" % (MI, d, c["K"], c["N"], dth)
    np.savez(os.path.join(ART, "strip_%s.npz" % tag), wall=r["wall"], p=p, M=M,
             mass_rows=np.array([(i, m, n) for i, m, n in rows]),
             stations=st, md_in=c["md_in"], W_star=W_star, cert=cert)
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return NPASS[0] == NPASS[1]


# ======================================================================
# stage kernel: the plug marched from the ANNULAR THROAT KERNEL's line
# [X-ANKR] in the throat frame -- the L-b posing (cowl smooth through
# the throat, the lip downstream on the kernel's cowl wall), the plug
# wall's foot from Angelino's own construction, the throat's radii
# inside the kernel's domain
# ======================================================================
def _wall_in_frame(w, th, Xm, Ym, mode="angelino", x_blend_mm=None):
    """The plug wall, dense, in the throat frame: (xw, yw, sw) with sw
    the slope dy'/dx'. mode = 'digitised' (the twin's smoothing spline)
    or 'angelino' (the sonic-lip fan's streamline for the first
    x_blend_mm, ramped into the digitised spline over 1 mm)."""
    from a1_toc_variational_jax import spline_coeffs, spline_eval
    cx, cy = CT.load_contour(True)
    cx, cy, _ = CT.smooth_contour(cx, cy)
    Mc = spline_coeffs(jnp.asarray(cx), jnp.asarray(cy), float(CT.FOOT_SLOPE))
    xd = np.linspace(float(cx[0]), float(cx[-1]), CASES["dense_wall_points"])
    yd, sd = jax.vmap(lambda xx: spline_eval(xx, jnp.asarray(cx), jnp.asarray(cy), Mc))(jnp.asarray(xd))
    yd, sd = np.asarray(yd), np.asarray(sd)
    if mode == "angelino":
        fs = CT.fan_sonic(w, 0.0)
        bl_mm, ramp_mm = CASES["angelino_blend_mm"]
        x_bl = (bl_mm if x_blend_mm is None else x_blend_mm) * 1e-3 * CT.S_LEN
        ramp = ramp_mm * 1e-3 * CT.S_LEN
        xa, ya = PM.exact_streamline(lambda xx, yy, lip: fs["field"](xx, yy),
                                     None, (float(cx[0]), float(cy[0])),
                                     float(cx[0]) + x_bl + ramp, h=CASES["streamline_step"])
        ya_d = np.interp(xd, xa, ya, right=np.nan)
        wgt = np.clip((xd - (float(cx[0]) + x_bl)) / ramp, 0.0, 1.0)
        yd = np.where(np.isnan(ya_d), yd, (1.0 - wgt) * ya_d + wgt * yd)
        sd = np.gradient(yd, xd)
    xw, yw, _, _ = to_frame(xd, yd, np.zeros_like(xd), np.zeros_like(xd), th, Xm, Ym)
    ct, st = np.cos(th), np.sin(th)
    sw = (sd * ct - st) / (ct + sd * st)
    assert np.all(np.diff(xw) > 0.0)
    if mode == "lb":
        # THE L-b GEOMETRY, POSED: the plug wall continues the throat's
        # parabola (radius rc_in_d separations, curving AWAY from the
        # channel as the kernel's inner wall does) up to x_1, then a
        # cubic Hermite transition to the Angelino wall at x_2, the
        # Angelino wall beyond -- an internal-external plug in the
        # kernel's own terms (measured 2026-09-21 night: with the real
        # external plug the kernel's parabola and the flat Angelino foot
        # differ by 9 deg of wall angle at the cut z 0.5, and the wall
        # cell must compress the flow by that much at once)
        hh = 0.5 * CT.H_T * CT.S_LEN
        rc = float(os.environ.get("FRM_RCIN", CASES["kernel_defaults"]["rc_in_d"])) * CT.H_T * CT.S_LEN
        x1, x2 = CASES["lb_transition_d"][0] * CT.H_T * CT.S_LEN, CASES["lb_transition_d"][1] * CT.H_T * CT.S_LEN
        y1, s1 = -hh - 0.5 * x1**2 / rc, -x1 / rc
        y2, s2 = float(np.interp(x2, xw, yw)), float(np.interp(x2, xw, sw))
        yw2, sw2 = yw.copy(), sw.copy()
        par = xw <= x1
        yw2[par] = -hh - 0.5 * xw[par]**2 / rc
        sw2[par] = -xw[par] / rc
        tr = (xw > x1) & (xw < x2)
        t = (xw[tr] - x1) / (x2 - x1); L = x2 - x1
        h00, h10, h01, h11 = 2*t**3 - 3*t**2 + 1, t**3 - 2*t**2 + t, -2*t**3 + 3*t**2, t**3 - t**2
        yw2[tr] = h00 * y1 + h10 * L * s1 + h01 * y2 + h11 * L * s2
        d00, d10, d01, d11 = 6*t**2 - 6*t, 3*t**2 - 4*t + 1, -6*t**2 + 6*t, 3*t**2 - 2*t
        sw2[tr] = (d00 * y1 + d10 * L * s1 + d01 * y2 + d11 * L * s2) / L
        yw, sw = yw2, sw2
    return xw, yw, sw


def corner_fan(w, field_uv, lip, q_L, th_L, x_cut, th, Y0, n_rays, n_pts, q_E,
               x_stop=None, ray0=None):
    """THE LIP CORNER IN A NON-UNIFORM FIELD: the centred expansion at
    the lip marched as a Goursat problem through the incoming field
    (field_uv(x', y') -> (u, v) in the throat frame). The leading ray
    is the C- from the lip traced through the field (its states the
    field's); every next ray is a C- from the lip carrying the corner
    relation's state (theta - nu = const across a C- fan: theta_k =
    th_L + nu(q_k) - nu(q_L)), its points solved by the top-down cell
    from the previous point on the same ray (C-) and the same-index
    point on the previous ray (C+) -- the bell's step-(3) structure
    with a centred corner. Rays run from the lip to the cut x' = x_cut.
    Returns the rays (list of (n, 4) arrays), the crossing of each ray
    with the cut (y, u, v), the terminal direction and the worst cell
    certification. The grid's index lines are C+ characteristics (the
    cell joins point j of ray k-1 to point j of ray k along a C+);
    x_stop (S33, default x_cut: unchanged) is where the rays after the
    leading one stop -- np.inf runs every ray to index n_pts, so that
    every C+ line up to the leading ray's last point is complete (the
    start line posed on a characteristic).
    ray0 (S33, default None: unchanged) GIVES the leading ray instead of
    tracing it through field_uv: an (n, 4) array of points from the lip
    with their states -- the C- line of an initial-value triangle whose
    top point lies on the leading ray [a1_ivl_triangle] -- and every
    next ray is then run to its index n - 1."""
    ta = w["ta"]
    xl, yl = lip
    # the corner relation's states from q_L to q_E
    full = _pm_fan(w, q_L)                              # nu from q_L
    qs = np.linspace(q_L, q_E, n_rays)
    ths = th_L + np.interp(qs, full["qs"], full["ths"])
    # the leading ray traced through the field (RK4 in x')
    def slope_field(x, y):
        u, v = field_uv(x, y)
        M = float(A1.state_q(jnp.float64(np.hypot(u, v)), ta)[5])
        return np.tan(np.arctan2(v, u) - np.arcsin(1.0 / M))
    if ray0 is None:
        hx = (x_cut - xl) / n_pts
        ray0 = [[xl, yl, *field_uv(xl, yl)]]
        x, y = xl, yl
        for j in range(n_pts):
            k1 = slope_field(x, y); k2 = slope_field(x + hx / 2, y + hx * k1 / 2)
            k3 = slope_field(x + hx / 2, y + hx * k2 / 2); k4 = slope_field(x + hx, y + hx * k3)
            y += hx / 6 * (k1 + 2 * k2 + 2 * k3 + k4); x += hx
            ray0.append([x, y, *field_uv(x, y)])
    else:
        n_pts = len(ray0) - 1
        x_stop = np.inf
    rays = [np.array(ray0, float)]
    t_int = A1.get_solver(("inttd_rot", 1.0, float(th), float(Y0)),
                          lambda: make_resid_interior_td_rot(1.0, th, Y0))
    cert = 0.0
    for k in range(1, n_rays):
        qk, thk = float(qs[k]), float(ths[k])
        pts = [np.array([xl, yl, qk * np.cos(thk), qk * np.sin(thk)])]
        prev = rays[-1]
        for j in range(1, n_pts + 1):
            pt1 = pts[-1]                                   # same ray, sends the C-
            pt2 = prev[min(j, len(prev) - 1)]               # previous ray, sends the C+
            p = jnp.concatenate([jnp.asarray(pt1), jnp.asarray(pt2)])
            # seed: straight-line crossing of the two characteristics
            M1 = float(A1.state_q(jnp.float64(np.hypot(pt1[2], pt1[3])), ta)[5])
            M2 = float(A1.state_q(jnp.float64(np.hypot(pt2[2], pt2[3])), ta)[5])
            lm = np.tan(np.arctan2(pt1[3], pt1[2]) - np.arcsin(1.0 / M1))
            lp = np.tan(np.arctan2(pt2[3], pt2[2]) + np.arcsin(1.0 / M2))
            x4 = (pt1[1] - pt2[1] - lm * pt1[0] + lp * pt2[0]) / (lp - lm)
            y4 = pt1[1] + lm * (x4 - pt1[0])
            z0 = jnp.array([x4, y4, 0.5 * (pt1[2] + pt2[2]), 0.5 * (pt1[3] + pt2[3])])
            z = t_int[0](z0, p, ta)
            step = float(t_int[2](z, p, ta))
            sc = max(1.0, float(jnp.max(jnp.abs(z))))
            cert = max(cert, step / (A1.NEWTON_TOL_FACTOR * A1.EPS * sc))
            pts.append(np.asarray(z, float))
            if pts[-1][0] >= (x_cut if x_stop is None else x_stop):
                break
        rays.append(np.array(pts))
    # the crossing of each ray with the cut
    cross = []
    for r in rays:
        if r[-1, 0] < x_cut:
            cross.append(None); continue
        j = np.argmax(r[:, 0] >= x_cut)
        a, b = r[j - 1], r[j]
        t = (x_cut - a[0]) / (b[0] - a[0])
        cross.append(a + t * (b - a))
    return dict(rays=rays, cross=cross, qs=qs, ths=ths, th_E=float(ths[-1]), cert=cert)


def kernel_case(w, z_cut, K, N, d_fan_h=None, rc_out_d=None):
    """The kernel-fed case. The plug wall's curvature at the foot is
    read from the wall itself (the slope's derivative at x' = 0); the
    cowl's radius rc_out_d (in separations; None = straight). The cut
    at z = z_cut of the kernel's stretched variable; the lip d_fan_h
    half-heights upstream of the cut on the cowl wall, its fan the
    record's planar corner wave from the kernel's own lip state."""
    import a1_annular_kernel as AK
    ta = w["ta"]
    th = np.radians(-CT.TILT_DEG)
    hh = 0.5 * CT.H_T * CT.S_LEN
    d_fr = 2.0 * hh                                   # the separation, frame units
    Xm = 0.5 * CT.FOOT[0] * CT.S_LEN
    Ym = 0.5 * (CT.FOOT[1] + CT.R_LIP) * CT.S_LEN
    xw, yw, sw = _wall_in_frame(w, th, Xm, Ym, os.environ.get("FRM_WALL", "lb"))
    # the foot curvature: d(slope)/dx' at x' = 0 over the first 0.3 h
    m = (xw >= 0.0) & (xw <= CASES["kernel_defaults"]["foot_window_h"] * hh)
    kappa = float(np.polyfit(xw[m], sw[m], 1)[0])    # 1/frame-length
    # the Angelino wall leaves the foot with ~zero curvature (measured:
    # 1/180 of a separation), so the throat's transonic length would
    # vanish and the inclination term would dominate the kernel (M ~ 2
    # on the line, the axial-flow branch): the plug wall's throat radius
    # is POSED (FRM_RCIN, separations; default 1.5, inside the domain)
    # and the kernel's parabola is used only within |x'| <~ 0.3 d
    KD = CASES["kernel_defaults"]
    rc_in_d = float(os.environ.get("FRM_RCIN", KD["rc_in_d"]))
    d_fan_h = KD["d_fan_h"] if d_fan_h is None else d_fan_h
    rc_in_m = rc_in_d * CT.H_T
    rc_out_m = (rc_out_d * CT.H_T) if rc_out_d else np.inf
    gam = CT.GAMMA
    eta = 2.0
    P = AK.throat_params(CT.FOOT[1], CT.H_T, CT.TILT_DEG, rc_in_m, rc_out_m, eta, gam)
    grid, fields, cst = AK.solve_kernel(P["y_i"], P["g1"], P["g2"], P["h1"], P["h2"], P["b1"], gam, eta)
    eps, Kk = P["eps"], P["K"]

    def kernel_uv(xp, yp):
        """frame (x', y') -> kernel (z, y) -> (u, v) in m/s, throat frame."""
        z = (np.asarray(xp, float) / d_fr) / (Kk * eps**0.5)
        yk = P["y_i"] + (np.asarray(yp, float) + hh) / d_fr
        u, v = AK.series_uv(grid, fields, eps, gam, z, yk)
        return u * w["as_"], v * w["as_"]

    x_cut = z_cut * Kk * eps**0.5 * d_fr
    x_lip = x_cut - d_fan_h * hh
    # the cowl wall (parabolic, the kernel's) at the lip
    y_cowl = lambda xp: hh + (0.5 * xp**2 / (rc_out_m * CT.S_LEN) if np.isfinite(rc_out_m) else 0.0)   # noqa
    yl = float(y_cowl(x_lip))
    u_l, v_l = kernel_uv(x_lip, yl)
    q_l, th_l = float(np.hypot(u_l, v_l)), float(np.arctan2(v_l, u_l))
    q_E = CT.q_at_pa(CT.PA, ta, w["as_"])
    n_rays, n_pts = int(os.environ.get("FRM_NRAYS", KD["n_rays"])), int(os.environ.get("FRM_NPTS", KD["n_pts"]))
    CF = corner_fan(w, kernel_uv, (x_lip, yl), q_l, th_l, x_cut, th, Ym, n_rays, n_pts, q_E)
    th_e = CF["th_E"]
    # rows on the cut: kernel rows from the plug wall to the leading ray's
    # crossing, the fan's rays' crossings, two above up to the jet boundary
    yw0, sw0 = float(np.interp(x_cut, xw, yw)), float(np.interp(x_cut, xw, sw))
    crs = [c_ for c_ in CF["cross"] if c_ is not None]
    y_lead = float(crs[0][1])
    y_edge = yl + (x_cut - x_lip) * np.tan(th_e)
    nA = max(5, int(round(N * (y_lead - yw0) / (y_edge - yw0))))
    yA = np.linspace(yw0, y_lead, nA, endpoint=False)
    uA, vA = kernel_uv(np.full(nA, x_cut), yA)
    vA[0] = sw0 * uA[0]                               # the wall row on the wall
    yB = np.array([c_[1] for c_ in crs]); uB = np.array([c_[2] for c_ in crs]); vB = np.array([c_[3] for c_ in crs])
    nB = len(yB)
    y_term = yB[-1]
    yC = np.array([0.5 * (y_term + y_edge), y_edge])
    uC, vC = np.full(2, q_E * np.cos(th_e)), np.full(2, q_E * np.sin(th_e))
    ys = np.concatenate([yA, yB, yC]); us = np.concatenate([uA, uB, uC]); vs = np.concatenate([vA, vB, vC])
    assert np.all(np.diff(ys) > 0.0), "rows not ordered"
    start = (np.full(len(ys), x_cut), ys, us, vs)
    X, Y, U, V = to_record(start[0], ys, us, vs, th, Xm, Ym)
    md_in, F_in = PM.col_fluxes(np.stack([X, Y, U, V], 1), ta, CT.PA, 1.0)
    # the kernel's own mass through the cut (the whole throat, plug wall to cowl) vs choked
    W_line = AK.mass_ratio(grid, fields, eps, gam, z_cut)
    # stations along the wall from the cut
    ds0, grow = CASES["station_clustering"][0] * hh, CASES["station_clustering"][1]
    ds_max = (xw[-1] - x_cut) / K
    xs, dsn = [x_cut], ds0
    while xs[-1] + dsn < xw[-1]:
        xs.append(xs[-1] + dsn); dsn = min(ds_max, dsn * grow)
    xq = np.array(xs[1:] + [xw[-1]])
    return dict(stations=(xq, np.interp(xq, xw, yw), np.interp(xq, xw, sw)), start=start,
                qpa=float(q_E), th=th, Xm=Xm, Ym=Ym, hh=hh, x0=x_cut, K=len(xq), fan_cert=CF["cert"],
                rays=CF["rays"],
                N=len(ys), nA=nA, nB=nB, md_in=abs(md_in), P=P, eps=eps, kappa=kappa,
                rc_in_d=rc_in_m / CT.H_T, x_lip=x_lip, M_lip=float(A1.state_q(jnp.float64(q_l), ta)[5]),
                th_lip=th_l, W_line=W_line, MA=np.asarray(A1.state_q(jnp.asarray(np.hypot(uA, vA)), ta)[5]),
                thA=np.degrees(np.arctan2(vA, uA)), y_lead=y_lead, y_edge=y_edge)


def kernel():
    t00 = time.time()
    print("== [F3/A1] Chutkey's plug marched from the ANNULAR KERNEL's line in the throat"
          " frame (stage kernel, L-b posing, Angelino foot) ==", flush=True)
    w = CT.build_world()
    KD = CASES["kernel_defaults"]
    z_cut = float(os.environ.get("FRM_ZCUT", KD["z_cut"]))
    K, N = int(os.environ.get("FRM_K", KD["K"])), int(os.environ.get("FRM_N", KD["N"]))
    rc_out = os.environ.get("FRM_RCOUT")
    c = kernel_case(w, z_cut, K, N, rc_out_d=(float(rc_out) if rc_out else None))
    W_star = CT.choked_mass(w)
    P = c["P"]
    print("   throat: plug-wall radius POSED %.2f d (the Angelino foot's own: 1/%.0f d), cowl %s;"
          " R_c %.2f, eps %.4f, y_i %.1f, beta_1 %.2f -> the kernel's domain %s"
          % (c["rc_in_d"], 1.0 / (c["kappa"] * 2.0 * c["hh"]) if c["kappa"] > 0 else np.inf,
             ("R %s d" % rc_out) if rc_out else "straight",
             P["R_c"], c["eps"], P["y_i"], P["b1"], "OK (R_c >= 1)" if P["R_c"] >= 1.0 else "MARGINAL"), flush=True)
    print("   cut at z %.2f = x' %.3f mm; lip at x' %.3f mm on the cowl, M_lip %.4f theta' %+.2f deg;"
          " kernel rows %d (M %.3f..%.3f, theta' %+.2f..%+.2f deg), corner-fan rays %d (Goursat"
          " through the kernel field, worst cell cert %.3f); kernel mass through the cut %.5f of"
          " the choked 1-D; the start line's mass (wall to edge) %.5f"
          % (z_cut, c["x0"] * CT.MM, c["x_lip"] * CT.MM, c["M_lip"], np.degrees(c["th_lip"]), c["nA"],
             c["MA"].min(), c["MA"].max(), c["thA"].min(), c["thA"].max(), c["nB"], c["fan_cert"],
             c["W_line"], c["md_in"] / W_star), flush=True)
    t0 = time.time()
    out, _ = PM.plug_march(c["stations"], c["start"], c["qpa"], w["tab"], 1.0,
                           cells=make_cells_rot(1.0, c["th"], c["Ym"]))
    wall = np.asarray(out["wall"])
    q = np.hypot(wall[:, 2], wall[:, 3])
    T, p, rho, cs, gam, M = [np.asarray(v) for v in A1.state_q(jnp.asarray(q), w["ta"])]
    cert = float(out["cert_worst"])
    print("   march: cert %.3f (%d cells) at %s, %.1f s" % (cert, int(out["cert_n"]), out.get("cert_where"),
                                                            time.time() - t0), flush=True)
    check("K-1 the march from the kernel's line certifies (%.3f)" % cert, cert <= 1.0)
    rows = mass_by_column_frame(w, out, c, c["md_in"])
    m2, mmid, mlast = rows[1][1], rows[len(rows) // 2][1], rows[-1][1]
    print("   mass vs the cut: column 2 %+.5f, mid %+.5f, last %+.5f" % (m2, mmid, mlast), flush=True)
    check("K-2 the mass is conserved from the kernel's cut to the last column (|dm/m| %.1e"
          " <= %.0e)" % (abs(mlast), CT.MASS_TOL), abs(mlast) <= CT.MASS_TOL)
    X, Y, U, V = to_record(wall[:, 0], wall[:, 1], wall[:, 2], wall[:, 3], c["th"], c["Xm"], c["Ym"])
    r = dict(wall=np.stack([X, Y, U, V], 1), p=p, M=M)
    st = CT.read_stations(w, c, r)
    print("   wall state at the truncations (paper / this march / the record's fan-cut march):")
    for row in st:
        rp, rM = REC[round(row["frac"], 2)]
        print("     %2.0f %%: p_w/p_0 %.5f / %.5f (%+.2e vs paper, %+.2e vs record);  M %.3f / %.3f / %.3f"
              % (100 * row["frac"], row["p_p0_meas"], row["p_p0"], row["p_p0"] / row["p_p0_meas"] - 1.0,
                 row["p_p0"] / rp - 1.0, row["M_meas"], row["M"], rM))
    os.makedirs(ART, exist_ok=True)
    np.savez(os.path.join(ART, "kernel_z%.2f_K%d_N%d.npz" % (z_cut, c["K"], c["N"])), wall=r["wall"], p=p, M=M,
             mass_rows=np.array([(i, m_, n_) for i, m_, n_ in rows]), md_in=c["md_in"], W_star=W_star, cert=cert)
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return NPASS[0] == NPASS[1]


STAGE = os.environ.get("FRM_STAGE", "frame")

if __name__ == "__main__":
    sys.exit(0 if {"frame": frame, "strip": strip, "kernel": kernel}.get(STAGE, frame)() else 1)
