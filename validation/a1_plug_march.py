#!/usr/bin/env python3
"""A1 BRICK 2, STEP 9b [F2/A1]: THE PLUG MARCH — assembly of the plug
topology from certified cells, with a march-level EXACT known answer.

TOPOLOGY (the bell, mirrored): columns march downstream at the
PRESCRIBED stations; each column is swept BOTTOM-UP:
  row 1      = SPIKE WALL (prescribed station, solved by the C- mirror
               of the certified inverse-wall cell with a MULTI-COLUMN
               FOOT SEARCH — the bell wall uses the C+ family from
               below; a bottom wall receives C- from above),
  rows 2..M  = interior cells (bottom-up mirror of Brick 1's),
  row M+1    = FREE JET EDGE (step 9a's certified cell: p = pa,
               position solved), fed from ITS OWN column.
Row bookkeeping, one characteristic at a time at both boundaries:
the edge ADDS one row per column (the widening jet gains a crossing;
the bell's j2 += 1 mirrored) and the wall CONSUMES the previous
column's rows below the new foot (their C- terminated on the wall
between stations; prolonging them creates ghost rows below the spike
whose only remaining Newton root is the backward, wrong-branch
crossing — measured: an M1-state mesh limb below the wall, mass +9%).

MARCH-LEVEL ORACLE (planar simple-wave twin, gconst tables). Uniform
flow at M1 meets a corner at the cowl lip with ambient pa = p(M2): the
exact field is (uniform M1) U (centered Prandtl-Meyer fan at the lip)
U (uniform M2 turned by dnu), all closed-form for a calorically
perfect gas. The prescribed "spike" is the EXACT STREAMLINE of that
field through the throat's lower point (fine-step RK4 integration of
the closed-form field, 1e-10 grade — an independent reference, not an
MOC). The marched solution must reproduce:
  P-1  the edge: asymptotic angle = dnu and speed = q(M2) within
       Richardson bands (station-halving),
  P-2  the wall pressure distribution along the spike vs the exact
       simple-wave pressure at each station,
  P-3  mass conservation: flux through the last column = start-line
       flux (per unit depth),
  P-4  momentum closure: exit-column flux = start flux + spike
       pressure push, with the FREE EDGE contributing exactly zero in
       the pa gauge (p = pa on it — the plug's defining property),
  R-1  rejector: corrupted ambient (qpa * 1.01) leaves the P-1 band,
  R-2  rejector: corrupted spike slopes fail to march or leave bands.

STAGE=axi: the same assembly in axisymmetric mode on the real-gas
tables (smoke + internal closures P-3/P-4; the external plug referee
— GENO's RaoPlug — is deferred until its S1/S2 fix, declared).

Run:  .venv-a1/bin/python validation/a1_plug_march.py
      STAGE=axi .venv-a1/bin/python validation/a1_plug_march.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1              # noqa: E402
import a1_thrust_functional as TF            # noqa: E402
from a1_freejet_unit import (make_resid_freejet, q_at_pa)  # noqa: E402

import jax                                    # noqa: E402
import jax.numpy as jnp                       # noqa: E402

EPS = A1.EPS
K_RICH = A1.K_RICH
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ----------------------------------------------------------------------
# the bottom-wall (spike) cell: C- mirror of the inverse-wall cell
# ----------------------------------------------------------------------
def make_resid_wallbot(delta):
    """Foot parameterized by y (z = (y2, u4)): the chord between the
    previous wall point and the interior above it is VERTICAL on the
    start line, so an x-parameterized foot divides by zero there —
    found by the cert localizer at ('wall', 1) on the fine grid; the
    chord is never horizontal near a bottom wall, so y is the robust
    parameter."""
    def resid(z, p, ta):
        y2, u4 = z
        xA, yA, uA, vA, xB, yB, uB, vB, x4, y4, slope = p
        D = (y2 - yA) / (yB - yA)
        x2 = xA + D * (xB - xA)
        u2 = uA + D * (uB - uA)
        v2 = vA + D * (vB - vA)
        v4 = slope * u4
        um, vm = 0.5 * (u2 + u4), 0.5 * (v2 + v4)
        ym = 0.5 * (y2 + y4)
        lm, _, qm, rm0, sm = A1._coef(um, vm, ym, ta, delta)
        rm = rm0 - qm * lm
        return jnp.array([
            (y4 - y2) - lm * (x4 - x2),
            (qm + slope * rm) * u4
            - (sm * (x4 - x2) + qm * u2 + rm * v2),
        ])
    return resid


def make_resid_interior_bu(delta):
    """Bottom-up interior cell (the mirror of Brick 1's): pt1 sits
    BELOW in the SAME column and sends the C+ characteristic; pt2 sits
    on the PREVIOUS column at the same row and sends the C-. (Brick 1's
    top-down cell is the transpose: C- within-column, C+ across.)"""
    def resid(z, p, ta):
        x4, y4, u4, v4 = z
        x1, y1, u1, v1, x2, y2, u2, v2 = p
        up, vp, yp = 0.5 * (u1 + u4), 0.5 * (v1 + v4), 0.5 * (y1 + y4)
        _, lp, qp, rp0, sp = A1._coef(up, vp, yp, ta, delta)
        rp = rp0 - qp * lp
        um, vm, ym = 0.5 * (u2 + u4), 0.5 * (v2 + v4), 0.5 * (y2 + y4)
        lm, _, qm, rm0, sm = A1._coef(um, vm, ym, ta, delta)
        rm = rm0 - qm * lm
        return jnp.array([
            (y4 - y1) - lp * (x4 - x1),
            (y4 - y2) - lm * (x4 - x2),
            qp * u4 + rp * v4 - (sp * (x4 - x1) + qp * u1 + rp * v1),
            qm * u4 + rm * v4 - (sm * (x4 - x2) + qm * u2 + rm * v2),
        ])
    return resid


def predict_bu(pt1, pt2, ta):
    """Seed for the bottom-up interior cell: straight-line crossing of
    the foot-state characteristics, averaged state."""
    x1, y1, u1, v1 = (float(v) for v in pt1)
    x2, y2, u2, v2 = (float(v) for v in pt2)
    st1 = A1.state_q(jnp.float64(np.hypot(u1, v1)), ta)
    st2 = A1.state_q(jnp.float64(np.hypot(u2, v2)), ta)
    mu1 = np.arcsin(min(1.0, 1.0 / max(float(st1[5]), 1.0001)))
    mu2 = np.arcsin(min(1.0, 1.0 / max(float(st2[5]), 1.0001)))
    th1, th2 = np.arctan2(v1, u1), np.arctan2(v2, u2)
    sp = np.tan(th1 + mu1)
    sm = np.tan(th2 - mu2)
    x4 = (y2 - y1 + sp * x1 - sm * x2) / (sp - sm)
    y4 = y1 + sp * (x4 - x1)
    return jnp.array([x4, y4, 0.5 * (u1 + u2), 0.5 * (v1 + v2)])


# ----------------------------------------------------------------------
# the plug march
# ----------------------------------------------------------------------
def plug_march(stations, start, qpa, tab, delta, sched=None,
               consume=True, cells=None, q_edge=None,
               edge_fill=0):
    """stations = (sx, sy, ssl) spike wall stations (K,), downstream of
    the start line. start = (x0, ys, us, vs) start-line states (row 1 =
    wall/bottom ... row N = edge/top), e.g. the exact corner-fan field
    on a vertical cut — the corner itself lives in the DATA, exactly as
    Brick 1's throat corner lives in its initialExpansion fan; ordinary
    cells cannot jump a centered wave (measured: cert 8.9e9 when they
    were asked to — the restructure of record). consume=False disables
    the wall-side row consumption (diagnostic only: reproduces the
    measured ghost-limb regression the mass check caught).
    cells (optional) = (t_int, t_fj, t_wb) solver triples that swap
    the three cell processes while keeping this driver's certified
    control flow (the swirl extension's seam); q_edge (optional) =
    the edge speed law y -> q (default: the constant qpa; the swirl
    edge carries q_m(y) = sqrt(qpa_tot^2 - Gamma^2/y^2)).
    edge_fill (int): rows to insert in the FIRST marched column
    between its topmost interior point and the free edge. A column is
    a characteristic while a vertical start line is not, so the first
    column alone opens a wedge there that no cell computes --- MEASURED
    on the plug worlds: gap 0.99 m (rising) and 1.31 m (descending),
    26x and 39x the mean row spacing, against 0.5-1.0x for EVERY other
    column. Mass jumps once, in that column, and is flat thereafter.
    Returns out + sched."""
    ta = A1.tab_arrays(tab)
    S = A1.Sched("rec") if sched is None else A1.Sched("play", sched.d)
    sx, sy, ssl = stations
    x0, ys0, us0, vs0 = start
    N = len(ys0)

    if cells is None:
        t_int = A1.get_solver(("intbu", delta),
                              lambda: make_resid_interior_bu(delta))
        t_fj = A1.get_solver(("fj", False, delta),
                             lambda: make_resid_freejet(delta))
        t_wb = A1.get_solver(("wb", delta),
                             lambda: make_resid_wallbot(delta))
    else:
        t_int, t_fj, t_wb = cells
    qe_of = (lambda yy: qpa) if q_edge is None else q_edge

    def with_ta(t):
        return (lambda z0, p: t[0](z0, p, ta),
                lambda z, p: t[2](z, p, ta))
    s_int, s_fj, s_wb = with_ta(t_int), with_ta(t_fj), with_ta(t_wb)
    cert = dict(worst=0.0, n=0, where=None)
    _tag = [None]

    def certify(stepfn, z, p):
        if S.mode != "rec":
            return
        step = float(stepfn(z, jnp.asarray(p)))
        sc = max(1.0, float(jnp.max(jnp.abs(z))))
        r = step / (A1.NEWTON_TOL_FACTOR * EPS * sc)
        if r > cert["worst"]:
            cert["worst"], cert["where"] = r, _tag[0]
        cert["n"] += 1

    def cell(solver, p, z0, tag=None):
        _tag[0] = tag
        p = jnp.asarray(p)
        z = S.cell(solver[0], p, z0)
        certify(solver[1], z, p)
        return z

    # start line: row 1 = WALL (bottom) ... row M0 = EDGE (top);
    # the mesh GROWS one row per column (the bell's j2 += 1, mirrored):
    # each column is a wall-to-edge characteristic, and the widening
    # jet gets its extra crossing as an extra row — the fix for the
    # measured fixed-row tangling.
    # x0 may be a SCALAR (a vertical cut, the historical posing) or an
    # ARRAY of per-row stations, which lets the caller pose the start
    # data ALONG A CHARACTERISTIC. That matters: a march column IS a
    # characteristic, so a vertical start line forces the first column
    # to bridge from vertical to characteristic geometry, and the free
    # edge takes one enormous step to get there (measured on the
    # configuration-comparison world: the edge advanced 2.35 m in a
    # single chord and leaked 1.45% of the mass, once, in the first
    # column). Posing the start on a characteristic removes the
    # transition entirely.
    x0a = np.atleast_1d(np.asarray(x0, dtype=float))
    if x0a.size == 1:
        x0a = np.full(N, float(x0a[0]))
    G = {}
    for j in range(1, N + 1):
        G[(j, 1)] = jnp.array([float(x0a[j - 1]), float(ys0[j - 1]),
                               float(us0[j - 1]), float(vs0[j - 1])])

    # MULTI-COLUMN FOOT SEARCH (the fix for the third measured lesson,
    # replacing the characteristic pacing). The wall receives the C-
    # family; the earlier scheme confined its foot to the FIRST
    # segment of the previous column (previous wall -> first interior)
    # and therefore had to PACE the columns (dx = row_gap/|lm|, clamped
    # at 0.30) so the foot stayed there — and the 0.30-long chords
    # crossing the fan gradient biased the midpoint closure (measured:
    # wall speeds high, pressures low, 55% of stations in band). Now
    # the march runs at the PRESCRIBED stations (fine columns) and the
    # wall cell searches the WHOLE previous column — stepping further
    # columns back if needed — for the segment that BRACKETS its
    # arriving characteristic, exactly like the bell's wall_search.
    # Chords shrink from the 0.30 clamp to the station spacing.
    def foot_lm(pt, u4_est, sl):
        """Estimated C- slope at a stored point, toward wall state."""
        u_, v_ = float(pt[2]), float(pt[3])
        um = 0.5 * (u_ + u4_est)
        vm = 0.5 * (v_ + sl * u4_est)
        q_ = float(np.hypot(um, vm))
        Mm = float(A1.state_q(jnp.float64(q_), ta)[5])
        mum = float(np.arcsin(min(1.0, 1.0 / max(Mm, 1.0001))))
        thm = float(np.arctan2(vm, um))
        return np.tan(thm - mum)

    def wall_foot_search(i, x4, y4, sl, u4_est, M_prev):
        """Find (back-column b, row j) whose segment brackets the
        arriving C- of the wall point at (x4, y4): the bracketing
        function f_j = (y4 - y_j) - lm_j (x4 - x_j) is positive at the
        previous wall (both terms positive) and decreases with row
        height; the first sign change is the foot segment."""
        for b in (1, 2, 3):
            if (1, i - b) not in G:
                break
            Mp = M_prev if b == 1 else max(
                j for j in range(1, M_prev + 1) if (j, i - b) in G)
            f_prev = None
            for j in range(1, Mp + 1):
                pt = G[(j, i - b)]
                f = (y4 - float(pt[1])) - foot_lm(pt, u4_est, sl) \
                    * (x4 - float(pt[0]))
                if f_prev is not None and f_prev > 0.0 >= f:
                    return b, j - 1
                f_prev = f
        return 1, 1                       # fallback: first segment

    x_end_march = float(sx[-1])
    edge_pts, wall_pts = [], []
    M = N                                     # top row of the PREVIOUS column
    kst = -1
    while True:
        kst += 1
        i = 2 + kst
        if S.mode == "rec":
            x_next = float(sx[kst])
            S.d.setdefault("xcols", []).append(x_next)
            done = kst == len(sx) - 1
        else:
            x_next = S.d["xcols"][kst]
            done = kst == len(S.d["xcols"]) - 1
        x4w = jnp.float64(x_next)
        y4w = jnp.interp(x4w, sx, sy)
        sl = jnp.interp(x4w, sx, ssl)
        if S.mode == "rec":
            u4e = float(G[(1, i - 1)][2])
            b, jf = wall_foot_search(i, float(x4w), float(y4w),
                                     float(sl), u4e, M)
            S.d.setdefault("wfoot", []).append((b, jf))
        else:
            b, jf = S.d["wfoot"][kst]
        ptA = G[(jf, i - b)]
        ptB = G[(jf + 1, i - b)]
        p = jnp.concatenate([ptA, ptB, jnp.array([x4w, y4w, sl])])
        if S.mode == "rec":
            z0 = jnp.array([0.5 * (float(ptA[1]) + float(ptB[1])),
                            float(ptA[2])])
        else:
            z0 = jnp.zeros(2)
        z = cell(s_wb, p, z0, tag=("wall", kst))
        wpt = jnp.array([x4w, y4w, z[1], sl * z[1]])
        G[(1, i)] = wpt
        wall_pts.append(wpt)
        # ---- ROW CONSUMPTION at the wall: the previous column's rows
        # 2..jf lie BELOW the new wall point's foot — their C-
        # characteristics have already terminated on the wall between
        # stations. Prolonging them (the first fine-station build did)
        # creates ghost rows below the spike: Newton's only remaining
        # crossing for such a row is the BACKWARD one, a valid root of
        # the equations on the wrong branch (measured: a whole M1-state
        # mesh limb below the wall, mass +9%). At a solid wall the
        # incoming family must be consumed exactly as the edge adds
        # one: rows are re-indexed from the foot up.
        jsrc0 = (jf + 1 if b == 1 else 2) if consume else 2
        # ---- interiors, bottom-up, partnered with previous rows
        #      jsrc0..M (the top one uses the previous EDGE point)
        jnew = 1
        for jprev in range(jsrc0, M + 1):
            jnew += 1
            pt1 = G[(jnew - 1, i)]
            pt2 = G[(jprev, i - 1)]
            z0 = predict_bu(pt1, pt2, ta) if S.mode == "rec" else None
            p = jnp.concatenate([pt1, pt2])
            z = cell(s_int, p, z0 if z0 is not None else jnp.zeros(4),
                     tag=("int", kst, jnew))
            G[(jnew, i)] = z
        # ---- new top row: the free edge, fed from THIS column
        pt1 = G[(jnew, i)]
        pt3 = G[(M, i - 1)]          # previous edge (top of prev col)
        if S.mode == "rec":
            th_g = float(jnp.arctan2(pt3[3], pt3[2]))
            dx_g = max(float(pt1[0]) - float(pt3[0]), 1e-3)
            z0 = jnp.array([float(pt3[0]) + dx_g,
                            float(pt3[1]) + dx_g * np.tan(th_g), th_g])
        else:
            z0 = jnp.zeros(3)
        p = jnp.concatenate([pt1, pt3, jnp.array([qpa])])
        z = cell(s_fj, p, z0, tag=("edge", kst))
        q_e = qe_of(z[1])
        ept = jnp.array([z[0], z[1], q_e * jnp.cos(z[2]),
                         q_e * jnp.sin(z[2])])
        if edge_fill and kst == 0:
            # fill the start-up wedge: the flow between the topmost
            # interior and the edge is smooth and unsampled, so seed it
            # as DATA (the pattern already used for the throat and lip
            # corners) rather than leave a hole the row-growth rule
            # cannot close at one row per column.
            base = G[(jnew, i)]
            for t in np.linspace(0.0, 1.0, edge_fill + 2)[1:-1]:
                jnew += 1
                G[(jnew, i)] = base + t * (ept - base)
        M = jnew + 1
        G[(M, i)] = ept
        edge_pts.append(ept)
        if S.mode == "rec":
            S.d.setdefault("K_cols", []).append(int(i))
        if done:
            break

    ilast = 2 + kst
    col = jnp.stack([G[(j, ilast)] for j in range(1, M + 1)
                     if (j, ilast) in G])
    out = dict(
        edge=jnp.stack(edge_pts), wall=jnp.stack(wall_pts),
        last_col=col, cert_worst=cert["worst"], cert_n=cert["n"],
        cert_where=cert["where"],
        mesh_pts=(jnp.stack(list(G.values()))
                  if S.mode == "rec" else None),
        mesh_keys=(list(G.keys()) if S.mode == "rec" else None))
    return out, S


# ----------------------------------------------------------------------
# conservation fluxes through a wall-to-edge polyline (pa gauge)
# ----------------------------------------------------------------------
def col_fluxes(col, ta, pa, delta):
    """Mass and axial-momentum flux (ambient gauge) through a polyline
    of (x, y, u, v) rows, oriented wall -> edge; the normal (dy, -dx)
    points downstream. Weight = 2 pi y for axisymmetric (delta=1),
    1 for planar."""
    c = np.asarray(col)
    q = np.hypot(c[:, 2], c[:, 3])
    st = A1.state_q(jnp.array(q), ta)
    p = np.array(st[1])
    rho = np.array(st[2])
    dx = np.diff(c[:, 0])
    dy = np.diff(c[:, 1])
    um = 0.5 * (c[1:, 2] + c[:-1, 2])
    vm = 0.5 * (c[1:, 3] + c[:-1, 3])
    rm = 0.5 * (rho[1:] + rho[:-1])
    pm = 0.5 * (p[1:] + p[:-1])
    w = (2.0 * np.pi * 0.5 * (c[1:, 1] + c[:-1, 1])) if delta \
        else 1.0
    dmd = rm * (um * dy - vm * dx) * w
    return (float(np.sum(dmd)),
            float(np.sum(um * dmd + (pm - pa) * dy * w)))


def wall_push_poly(wall, ta, pa, delta):
    """Gauge pressure push of the wall polyline, ∫ (p - pa) w dy with
    signed dy: the momentum theorem for the marched region closes as
    F_out - F_in + push = 0 (the free edge contributes exactly zero
    in the pa gauge — the plug's defining property)."""
    c = np.asarray(wall)
    q = np.hypot(c[:, 2], c[:, 3])
    p = np.array(A1.state_q(jnp.array(q), ta)[1])
    dy = np.diff(c[:, 1])
    pm = 0.5 * (p[1:] + p[:-1])
    w = (2.0 * np.pi * 0.5 * (c[1:, 1] + c[:-1, 1])) if delta \
        else 1.0
    return float(np.sum((pm - pa) * dy * w))


# ----------------------------------------------------------------------
# exact planar simple-wave reference (gconst)
# ----------------------------------------------------------------------
def pm_exact(gam, Rg, ts, M1, M2):
    def nu(M):
        a = np.sqrt((gam + 1) / (gam - 1))
        return a * np.arctan(np.sqrt((M * M - 1) / a / a)) \
            - np.arctan(np.sqrt(M * M - 1))
    dnu = nu(M2) - nu(M1)

    def state_of_M(M):
        T = ts / (1 + 0.5 * (gam - 1) * M * M)
        q = M * np.sqrt(gam * Rg * T)
        return q

    def field(x, y, lip):
        """exact simple-wave state at (x,y): returns (q, theta)."""
        # ray angle from the lip, measured from +x axis (rays go
        # down-right, angle negative)
        phi = np.arctan2(y - lip[1], x - lip[0])
        mu1 = np.arcsin(1.0 / M1)
        mu2 = np.arcsin(1.0 / M2)
        phi1 = -mu1                       # first ray (theta = 0)
        phi2 = dnu - mu2                  # last ray (theta = dnu)
        if phi <= phi1:
            return state_of_M(M1), 0.0
        if phi >= phi2:
            return state_of_M(M2), dnu
        # in the fan: on the ray, phi = theta - mu(M); invert for M
        from scipy.optimize import brentq

        def f(M):
            # ray angle of the M-characteristic: phi_ray = theta - mu
            return nu(M) - nu(M1) - np.arcsin(1.0 / M) - phi
        M = brentq(f, M1, M2, xtol=1e-12)
        th = nu(M) - nu(M1)
        return state_of_M(M), th
    return dnu, field, state_of_M


def exact_streamline(field, lip, p0, x_end, h=2e-4):
    """RK4 streamline of the exact field from p0 to x_end."""
    xs, ys = [p0[0]], [p0[1]]
    x, y = p0
    while x < x_end:
        def slope(xx, yy):
            q, th = field(xx, yy, lip)
            return np.tan(th)
        k1 = slope(x, y)
        k2 = slope(x + h / 2, y + h * k1 / 2)
        k3 = slope(x + h / 2, y + h * k2 / 2)
        k4 = slope(x + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    stage = os.environ.get("STAGE", "oracle")
    print("== A1 brick 2 step 9b: plug march [F2/A1] (stage=%s) =="
          % stage)

    if stage == "oracle":
        tg = A1.prep_tab(A1.build_tab_gconst())
        ta = A1.tab_arrays(tg)
        gam, Rg, ts = tg["_g"], tg["Rg"], tg["ts"]
        M1, M2 = 1.5, 2.2
        dnu, field, q_of = pm_exact(gam, Rg, ts, M1, M2)
        q1, q2 = q_of(M1), q_of(M2)
        pa = float(A1.state_q(jnp.float64(q2), ta)[1])
        qpa = q_at_pa(pa, ta, tg["_as"])
        print("  planar simple-wave twin: M1=%.2f M2=%.2f dnu=%.5f"
              " rad; q2=%.3f (tables %.3f)" % (M1, M2, dnu, q2, qpa))
        lip = (0.0, 2.0)
        x0, x_end = 0.5, 3.0

        def run_case(K, N):
            xs, ys = exact_streamline(field, lip, (0.0, 1.0), x_end)
            # start line: exact field on the vertical cut at x0, from
            # the exact edge point down to the exact wall point
            y_wall0 = float(np.interp(x0, xs, ys))
            y_edge0 = lip[1] + np.tan(dnu) * x0
            yline = np.linspace(y_wall0, y_edge0, N)
            us, vs = [], []
            for yy in yline:
                q, th = field(x0, yy, lip)
                us.append(q * np.cos(th))
                vs.append(q * np.sin(th))
            start = (x0, yline, np.array(us), np.array(vs))
            m = xs > x0 + 1e-9
            tgrid = np.linspace(0, 1, K)
            sxa = x0 + tgrid[1:] * (x_end - x0)
            sya = np.interp(sxa, xs, ys)
            ssl = np.interp(sxa, xs, np.gradient(ys, xs))
            st = (jnp.array(sxa), jnp.array(sya), jnp.array(ssl))
            out, _ = plug_march(st, start, qpa, tg, 0.0)
            return out, (xs, ys)

        out_c, _ = run_case(41, 21)
        out_f, exact_w = run_case(81, 41)
        print("  cert: coarse %.3f (n=%d) fine %.3f (n=%d) worst at"
              " %s / %s" % (out_c["cert_worst"], out_c["cert_n"],
                            out_f["cert_worst"], out_f["cert_n"],
                            out_c["cert_where"], out_f["cert_where"]))
        check("all cells Newton-certified", out_c["cert_worst"] <= 1.0
              and out_f["cert_worst"] <= 1.0)

        # P-1: edge asymptotics
        def edge_stats(out):
            e = np.array(out["edge"])
            n = e.shape[0]
            tail = e[int(0.7 * n):]
            th = np.arctan2(tail[:, 3], tail[:, 2]).mean()
            qe = np.hypot(tail[:, 2], tail[:, 3]).mean()
            return th, qe
        thc, qec = edge_stats(out_c)
        thf, qef = edge_stats(out_f)
        band_th = K_RICH * abs(thc - thf) + 64 * EPS * abs(dnu)
        d_th = abs(thf - dnu)
        print("  P-1 edge: angle %.5f vs dnu %.5f (|d|=%.2e,"
              " band=%.2e); speed %.3f vs %.3f"
              % (thf, dnu, d_th, band_th, qef, q2))
        check("P-1 edge angle -> dnu within Richardson band",
              d_th <= band_th)

        # P-2: wall pressures vs the exact field
        def wall_p(out):
            w = np.array(out["wall"])
            q = np.hypot(w[:, 2], w[:, 3])
            p = np.array(A1.state_q(jnp.array(q), ta)[1])
            pex = np.array([A1.state_q(jnp.float64(
                field(w[k, 0], w[k, 1], lip)[0]), ta)[1]
                for k in range(w.shape[0])])
            return w[:, 0], p, pex
        xwc, pc, pexc = wall_p(out_c)
        xwf, pf, pexf = wall_p(out_f)
        # compare at the coarse stations (both grids share the exact
        # wall, bands from grid halving via interpolation)
        pf_i = np.interp(xwc, xwf, pf)
        band_p = K_RICH * np.abs(pc - pf_i) + A1.C_FLOOR * EPS * pa
        dev_p = np.abs(pf_i - np.interp(xwc, xwc, pexc))
        frac = float((dev_p <= band_p).mean())
        print("  P-2 wall pressure: %.0f%% of stations inside band"
              " (max dev/pa %.2e)" % (100 * frac, dev_p.max() / pa))
        check("P-2 wall pressure matches the exact field (>= 90%"
              " in band)", frac >= 0.90)

        # P-3: mass conservation (planar, per unit depth)
        def mass(col):
            c = np.array(col)
            q = np.hypot(c[:, 2], c[:, 3])
            rho = np.array(A1.state_q(jnp.array(q), ta)[2])
            dx = np.diff(c[:, 0])
            um = 0.5 * (c[1:, 2] + c[:-1, 2])
            vm = 0.5 * (c[1:, 3] + c[:-1, 3])
            rm = 0.5 * (rho[1:] + rho[:-1])
            dy_s = np.diff(c[:, 1])          # SIGNED (top-down column)
            # flux through the segment (normal ds = (dy, -dx))
            return float(np.abs(np.sum(rm * (um * dy_s - vm * dx))))
        # start flux: integrate the exact (nonuniform) start line
        yl = np.linspace(lip[1] + np.tan(dnu) * x0,
                         float(np.interp(x0, exact_w[0], exact_w[1])),
                         801)
        uu, vv = [], []
        for yy in yl:
            q, th = field(x0, yy, lip)
            uu.append(q * np.cos(th))
            vv.append(q * np.sin(th))
        uu = np.array(uu)
        rr = np.array(A1.state_q(jnp.array(np.hypot(uu, vv)), ta)[2])
        md0 = float(np.abs(np.trapezoid(rr * uu, yl)))
        mdc = mass(out_c["last_col"])
        mdf = mass(out_f["last_col"])
        band_m = K_RICH * abs(mdc - mdf) + A1.C_FLOOR * EPS * md0
        print("  P-3 mass: exit %.6e vs start %.6e (|d|=%.2e,"
              " band=%.2e)" % (mdf, md0, abs(mdf - md0), band_m))
        check("P-3 mass conserved within band",
              abs(mdf - md0) <= band_m)

        # P-4: momentum closure in the pa gauge (free edge = 0)
        yl_st = np.linspace(float(np.interp(x0, exact_w[0],
                                            exact_w[1])),
                            lip[1] + np.tan(dnu) * x0, 801)
        uu2, vv2 = [], []
        for yy in yl_st:
            q, th = field(x0, yy, lip)
            uu2.append(q * np.cos(th))
            vv2.append(q * np.sin(th))
        stline = np.stack([np.full(801, x0), yl_st,
                           np.array(uu2), np.array(vv2)], axis=1)
        _, Fin = col_fluxes(stline, ta, pa, 0.0)

        def mom_closure(out):
            _, Fout = col_fluxes(np.array(out["last_col"]), ta, pa,
                                 0.0)
            wallpoly = np.vstack([stline[:1], np.array(out["wall"])])
            push = wall_push_poly(wallpoly, ta, pa, 0.0)
            return Fout - Fin + push
        Rm_c = mom_closure(out_c)
        Rm_f = mom_closure(out_f)
        band_F = K_RICH * abs(Rm_c - Rm_f) + A1.C_FLOOR * EPS \
            * abs(Fin)
        print("  P-4 momentum: closure %.4e (coarse %.4e) vs band"
              " %.4e on F_in %.4e; free edge contributes 0 by"
              " construction" % (Rm_f, Rm_c, band_F, Fin))
        check("P-4 momentum closes in the pa gauge within band",
              abs(Rm_f) <= band_F)

        # R-1: corrupted ambient
        def run_bad():
            xs, ys = exact_w
            y_wall0 = float(np.interp(x0, xs, ys))
            y_edge0 = lip[1] + np.tan(dnu) * x0
            yline = np.linspace(y_wall0, y_edge0, 41)
            us, vs = [], []
            for yy in yline:
                q, th = field(x0, yy, lip)
                us.append(q * np.cos(th))
                vs.append(q * np.sin(th))
            start = (x0, yline, np.array(us), np.array(vs))
            tgrid = np.linspace(0, 1, 81)
            sxa = x0 + tgrid[1:] * (x_end - x0)
            st = (jnp.array(sxa),
                  jnp.array(np.interp(sxa, xs, ys)),
                  jnp.array(np.interp(sxa, xs,
                                      np.gradient(ys, xs))))
            o, _ = plug_march(st, start, qpa * 1.01, tg, 0.0)
            return edge_stats(o)
        thb, _ = run_bad()
        print("  R-1: corrupted-ambient edge angle %.5f (|d - dnu| ="
              " %.2e vs band %.2e)" % (thb, abs(thb - dnu), band_th))
        check("R-1 rejector: corrupted ambient leaves the P-1 band",
              abs(thb - dnu) > band_th)

        print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                              time.time() - t0))
        sys.exit(0 if NPASS[0] == NPASS[1] else 1)

    if stage == "axi":
        # the same assembly, axisymmetric (delta = 1), on the real-gas
        # NASA tables. No closed form exists here, so the stage
        # certifies by INTERNAL closures: Newton certification, mass
        # conservation, the pa-gauge momentum theorem (free edge = 0
        # by construction), a source-alive control (the delta = 1 run
        # must differ measurably from delta = 0 on the same data),
        # and a corrupted-spike rejector.
        from scipy.optimize import brentq
        tb = A1.prep_tab(A1.build_tab_nasa())
        ta = A1.tab_arrays(tb)
        as_ = tb["_as"]
        M1, M2 = 1.5, 2.2

        def q_of_M(Mt):
            return brentq(lambda q: float(
                A1.state_q(jnp.float64(q), ta)[5]) - Mt,
                1.02 * as_, 3.2 * as_, xtol=1e-11)
        q1, q2 = q_of_M(M1), q_of_M(M2)
        pa = float(A1.state_q(jnp.float64(q2), ta)[1])
        qpa = q_at_pa(pa, ta, as_)
        # tables-consistent planar corner fan (start-line DATA):
        # dtheta = sqrt(M^2-1)/q dq integrated on the tables' own M(q)
        qs = np.linspace(q1, q2, 400)
        Ms = np.array([float(A1.state_q(jnp.float64(q), ta)[5])
                       for q in qs])
        mus = np.arcsin(np.clip(1.0 / Ms, 0, 1))
        dth = np.sqrt(np.maximum(Ms ** 2 - 1.0, 0.0)) / qs
        ths = np.concatenate([[0.0], np.cumsum(
            0.5 * (dth[1:] + dth[:-1]) * np.diff(qs))])
        phis = ths - mus                       # ray angles, monotone
        th2 = float(ths[-1])
        print("  tables fan: q %.2f -> %.2f, turn %.5f rad, pa ="
              " %.4e" % (q1, q2, th2, pa))

        def field_tab(x, y, lip):
            ph = np.arctan2(y - lip[1], x - lip[0])
            if ph <= phis[0]:
                return q1, 0.0
            if ph >= phis[-1]:
                return q2, th2
            return (float(np.interp(ph, phis, qs)),
                    float(np.interp(ph, phis, ths)))

        lip = (0.0, 2.0)
        x0, x_end = 0.5, 2.5
        xs, ys = exact_streamline(field_tab, lip, (0.0, 1.0), x_end,
                                  h=5e-4)

        def run_case(K, N, delta, dssl=0.0):
            y_wall0 = float(np.interp(x0, xs, ys))
            y_edge0 = lip[1] + np.tan(th2) * x0
            yline = np.linspace(y_wall0, y_edge0, N)
            us, vs = [], []
            for yy in yline:
                q, th = field_tab(x0, yy, lip)
                us.append(q * np.cos(th))
                vs.append(q * np.sin(th))
            start = (x0, yline, np.array(us), np.array(vs))
            tgrid = np.linspace(0, 1, K)
            sxa = x0 + tgrid[1:] * (x_end - x0)
            st = (jnp.array(sxa), jnp.array(np.interp(sxa, xs, ys)),
                  jnp.array(np.interp(sxa, xs, np.gradient(ys, xs))
                            + dssl))
            out, _ = plug_march(st, start, qpa, tb, delta)
            return out

        out_c = run_case(33, 17, 1.0)
        out_f = run_case(65, 33, 1.0)
        print("  cert: coarse %.3f (n=%d) fine %.3f (n=%d) worst at"
              " %s / %s" % (out_c["cert_worst"], out_c["cert_n"],
                            out_f["cert_worst"], out_f["cert_n"],
                            out_c["cert_where"], out_f["cert_where"]))
        check("A-1 all cells Newton-certified (axi, real-gas)",
              out_c["cert_worst"] <= 1.0 and out_f["cert_worst"]
              <= 1.0)

        # dense start-line polyline for reference fluxes
        yl_st = np.linspace(float(np.interp(x0, xs, ys)),
                            lip[1] + np.tan(th2) * x0, 801)
        uu, vv = [], []
        for yy in yl_st:
            q, th = field_tab(x0, yy, lip)
            uu.append(q * np.cos(th))
            vv.append(q * np.sin(th))
        stline = np.stack([np.full(801, x0), yl_st, np.array(uu),
                           np.array(vv)], axis=1)
        md0, Fin = col_fluxes(stline, ta, pa, 1.0)

        def closures(out):
            md, Fout = col_fluxes(np.array(out["last_col"]), ta, pa,
                                  1.0)
            wallpoly = np.vstack([stline[:1], np.array(out["wall"])])
            push = wall_push_poly(wallpoly, ta, pa, 1.0)
            return md, Fout - Fin + push
        md_c, Rm_c = closures(out_c)
        md_f, Rm_f = closures(out_f)
        band_m = K_RICH * abs(md_c - md_f) + A1.C_FLOOR * EPS * md0
        print("  A-2 mass: exit %.6e vs start %.6e (|d|=%.2e,"
              " band=%.2e)" % (md_f, md0, abs(md_f - md0), band_m))
        check("A-2 mass conserved within band (2 pi y flux)",
              abs(md_f - md0) <= band_m)
        band_F = K_RICH * abs(Rm_c - Rm_f) + A1.C_FLOOR * EPS \
            * abs(Fin)
        print("  A-3 momentum: closure %.4e (coarse %.4e) vs band"
              " %.4e on F_in %.4e" % (Rm_f, Rm_c, band_F, Fin))
        check("A-3 momentum closes in the pa gauge within band",
              abs(Rm_f) <= band_F)

        # A-4: the axisymmetric source must be ALIVE — the same data
        # marched with delta = 0 must differ beyond the axi pair's
        # own Richardson band (guards a silently-planar axi mode)
        out_p = run_case(33, 17, 0.0)
        wq_a = np.hypot(np.array(out_c["wall"])[-1, 2],
                        np.array(out_c["wall"])[-1, 3])
        wq_f = np.hypot(np.array(out_f["wall"])[-1, 2],
                        np.array(out_f["wall"])[-1, 3])
        wq_p = np.hypot(np.array(out_p["wall"])[-1, 2],
                        np.array(out_p["wall"])[-1, 3])
        band_q = K_RICH * abs(wq_a - wq_f) + 64 * EPS * abs(wq_a)
        print("  A-4 source-alive: wall speed at x_end axi %.3f vs"
              " planar %.3f (|d|=%.2e, band=%.2e)"
              % (wq_f, wq_p, abs(wq_f - wq_p), band_q))
        check("A-4 axisymmetric source alive (differs from planar"
              " beyond band)", abs(wq_f - wq_p) > band_q)

        # A-5 rejector: corrupted spike slopes must break closure
        try:
            out_b = run_case(33, 17, 1.0, dssl=0.05)
            _, Rm_b = closures(out_b)
            bad = abs(Rm_b) > band_F
            print("  A-5: corrupted spike slope -> closure %.4e vs"
                  " band %.4e" % (Rm_b, band_F))
        except Exception as ex:                     # noqa: BLE001
            bad = True
            print("  A-5: corrupted spike slope -> march failed"
                  " (%s)" % type(ex).__name__)
        check("A-5 rejector: corrupted spike leaves the closure"
              " band", bad)

        print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                              time.time() - t0))
        sys.exit(0 if NPASS[0] == NPASS[1] else 1)

    print("stage %s not implemented in this carrier version" % stage)
    sys.exit(1)


if __name__ == "__main__":
    main()
