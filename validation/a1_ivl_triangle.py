"""The initial-value-line triangle of the plug march [F3/A1, S33 experiment,
owner: "proviamo a fare come hanno fatto loro"; NOT on the shared branch].

WHY. Humphreys 1971 (p. 1583) start the method of characteristics ON
their start line A-E -- a transonic (modified Moore-Hall) line from the
plug foot to the cowl lip -- and march the flow field from it. A start
line is not a characteristic, and the classical way to march from one is
to fill its DOMAIN OF DEPENDENCE with characteristic cells, each new
point the crossing of the C+ from one start point and the C- from its
neighbour, until the outer boundaries are characteristics: the bell's
step (3) from the Sauer IVL (a1_ideal_march_jax, "initialExpansion
twin"). The plug march of record instead hands a transverse line to
plug_march as its first column (which bridges it: the structural -4.57
percent of stage kernel "cut"), or traces the hand-over C+ through the
throat kernel's ANALYTIC field out to z ~ 1 (stage kernel "char": the
series band of 2.5 percent on the discharge). Here the kernel is read
ONLY on the start line (as they read Moore-Hall only there); everything
downstream of it is marched by the record's certified cells.

THE CONSTRUCTION (throat frame, flow along +x', the plug wall below, the
lip above). Start points L_0 (on the plug wall) .. L_{N-1} (on the lip's
leading ray), on the transverse line x' = x_cut, their states the
kernel's. P[a][b] (a <= b) = the crossing of the C+ from L_a and the C-
from L_b: P[a][a] = L_a; P[a][b] = the top-down rotated cell of
a1_frame_march with pt1 = P[a+1][b] (the previous point on C- line b,
sending the C-) and pt2 = P[a][b-1] (the previous point on C+ line a,
sending the C+). The C+ line a = 0 (from the wall point) is the lower
boundary of the triangle; the C- line b = N-1 (from the top point, ON the
leading ray) is its upper boundary, i.e. the lip's leading ray continued
through the marched field. The corner fan at the lip is then run with
THAT leading ray (corner_fan ray0=), so its C+ line through the
triangle's last point continues the triangle's C+ line 0, and above the
fan's terminal ray the free-jet triangle (lifted verbatim from stage
kernel "char", piece (iii)) closes the column at the jet boundary. The
hand-over to plug_march is that column: a C+ characteristic from the
wall to the edge, by construction -- no bridge, and no series read off
the start line.
"""
import numpy as np

import a1_ideal_march_jax as A1
import jax.numpy as jnp


def _mach(pt, ta):
    return float(A1.state_q(jnp.float64(np.hypot(pt[2], pt[3])), ta)[5])


def _seed(pt1, pt2, ta):
    """straight-line crossing of the C- from pt1 and the C+ from pt2"""
    M1, M2 = _mach(pt1, ta), _mach(pt2, ta)
    lm = np.tan(np.arctan2(pt1[3], pt1[2]) - np.arcsin(1.0 / M1))
    lp = np.tan(np.arctan2(pt2[3], pt2[2]) + np.arcsin(1.0 / M2))
    x4 = (pt1[1] - pt2[1] - lm * pt1[0] + lp * pt2[0]) / (lp - lm)
    y4 = pt1[1] + lm * (x4 - pt1[0])
    return jnp.array([x4, y4, 0.5 * (pt1[2] + pt2[2]), 0.5 * (pt1[3] + pt2[3])])


def ivl_triangle(L, th, Y0, ta):
    """The domain of dependence of the start line L ((N, 4): x', y', u, v
    from the wall point to the top point), marched with the top-down
    rotated cell. Returns P (N x N, upper triangle filled) and the worst
    certification ratio."""
    import a1_frame_march as FM
    t_int = A1.get_solver(("inttd_rot", 1.0, float(th), float(Y0)),
                          lambda: FM.make_resid_interior_td_rot(1.0, th, Y0))
    N = len(L)
    P = [[None] * N for _ in range(N)]
    for a in range(N):
        P[a][a] = np.asarray(L[a], float)
    cert = 0.0
    for b in range(1, N):
        for a in range(b - 1, -1, -1):
            pt1, pt2 = P[a + 1][b], P[a][b - 1]
            p = jnp.concatenate([jnp.asarray(pt1), jnp.asarray(pt2)])
            z = t_int[0](_seed(pt1, pt2, ta), p, ta)
            step = float(t_int[2](z, p, ta))
            sc = max(1.0, float(jnp.max(jnp.abs(z))))
            cert = max(cert, step / (A1.NEWTON_TOL_FACTOR * A1.EPS * sc))
            P[a][b] = np.asarray(z, float)
    return P, cert


def free_jet_triangle(rays, j, xE, yE, q_E, th_e, th, Y0, hs, ta):
    """Above the fan's terminal ray: for every C+ line i <= j of the fan,
    from its terminal-ray point up through the C- lines the jet boundary
    reflected at its earlier edge points, to its own edge point, with the
    march's own interior (bottom-up) and free-jet rotated cells. Lifted
    verbatim from a1_humphreys_twin._char_start piece (iii) (S33), so
    that the two poses share it bit for bit. Returns the rows of line j
    above the terminal ray (edge point last) and the worst cert."""
    import a1_frame_march as FM
    t_int, t_fj, _ = FM.make_cells_rot(1.0, th, Y0)
    cert = [0.0]

    def solve(t, z0, p):
        z = t[0](z0, p, ta)
        sc = max(1.0, float(jnp.max(jnp.abs(z))))
        cert[0] = max(cert[0], float(t[2](z, p, ta))
                      / (A1.NEWTON_TOL_FACTOR * A1.EPS * sc))
        return np.asarray(z, float)

    def mslope(pt, sgn):
        M_ = _mach(pt, ta)
        return np.tan(np.arctan2(pt[3], pt[2]) + sgn * np.arcsin(1.0 / M_))

    edge = [np.array([xE, yE, q_E * np.cos(th_e), q_E * np.sin(th_e)])]
    lines = {}
    n_r = len(rays)
    for i in range(1, j + 1):
        pts = [np.asarray(rays[n_r - 1][i], float)]
        for m in range(1, i):
            pt1, pt2 = pts[-1], np.asarray(lines[i - 1][m], float)
            lp, lm = mslope(pt1, +1.0), mslope(pt2, -1.0)
            x4 = (pt2[1] - pt1[1] - lm * pt2[0] + lp * pt1[0]) / (lp - lm)
            z0 = jnp.array([x4, pt1[1] + lp * (x4 - pt1[0]),
                            0.5 * (pt1[2] + pt2[2]), 0.5 * (pt1[3] + pt2[3])])
            pts.append(solve(t_int, z0, jnp.concatenate(
                [jnp.asarray(pt1), jnp.asarray(pt2)])))
        pt1, pt3 = pts[-1], edge[-1]
        th3 = float(np.arctan2(pt3[3], pt3[2]))
        dx = max(float(pt1[0]) - float(pt3[0]), hs)
        z = solve(t_fj, jnp.array([pt3[0] + dx, pt3[1] + dx * np.tan(th3), th3]),
                  jnp.concatenate([jnp.asarray(pt1), jnp.asarray(pt3),
                                   jnp.array([q_E])]))
        edge.append(np.array([z[0], z[1], q_E * np.cos(z[2]),
                              q_E * np.sin(z[2])]))
        pts.append(edge[-1])
        lines[i] = pts
    return np.array(lines[j][1:]), cert[0]


def tri_start(w, field_uv, lip, q_l, th_l, x_cut, yw0, sw0, N, n_lead,
              n_rays, q_E, th_e, th, Y0):
    """The hand-over column of the IVL-triangle pose. Returns the column
    (xs, ys, us, vs, wall -> edge), the pieces' sizes and the worst
    certification of the triangle, the fan and the free-jet triangle."""
    import a1_frame_march as FM
    ta = w["ta"]
    xE, yE = lip

    def cslope(xx, yy):
        u_, v_ = field_uv(xx, yy)
        M_ = float(A1.state_q(jnp.float64(np.hypot(u_, v_)), ta)[5])
        return np.tan(np.arctan2(v_, u_) - np.arcsin(1.0 / M_))

    # (a) the leading ray from the lip to the start line, in the kernel's
    # field (the one stretch where no start point is upstream of it)
    hs = (x_cut - xE) / n_lead
    lead = [[xE, yE, *field_uv(xE, yE)]]
    x, y = xE, yE
    for _ in range(n_lead):
        k1 = cslope(x, y)
        k2 = cslope(x + 0.5 * hs, y + 0.5 * hs * k1)
        k3 = cslope(x + 0.5 * hs, y + 0.5 * hs * k2)
        k4 = cslope(x + hs, y + hs * k3)
        y += hs * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        x += hs
        lead.append([x, y, *field_uv(x, y)])
    lead = np.array(lead, float)
    y_lead = float(lead[-1, 1])
    # (b) the start line: N points from the wall to the leading ray, the
    # kernel's states, the wall row turned onto the wall (stage kernel's
    # convention: v = slope * u)
    yL = np.linspace(yw0, y_lead, N)
    uL, vL = [np.array(v, float) for v in field_uv(np.full(N, x_cut), yL)]
    vL[0] = sw0 * uL[0]
    L = np.stack([np.full(N, x_cut), yL, uL, vL], 1)
    L[-1] = lead[-1]                                   # the top point ON the ray
    # (c) the triangle
    P, cert_tri = ivl_triangle(L, th, Y0, ta)
    # (d) the fan with the triangle's upper boundary as its leading ray
    ray0 = np.concatenate([lead, np.array([P[a][N - 1] for a in range(N - 2, -1, -1)])])
    CF = FM.corner_fan(w, field_uv, (xE, yE), q_l, th_l, x_cut, th, Y0,
                       n_rays, len(ray0) - 1, q_E, ray0=ray0)
    js = len(ray0) - 1                                 # ray0[js] = P[0][N-1]
    fan_line = np.array([r[js] for r in CF["rays"]])
    # (e) the free-jet triangle on the same C+ line
    top, cert_fj = free_jet_triangle(CF["rays"], js, xE, yE, q_E, th_e, th, Y0, hs, ta)
    tri_line = np.array([P[0][b] for b in range(N - 1)])  # wall ... below P[0][N-1]
    col = np.concatenate([tri_line, fan_line, top])
    return dict(col=col, n_tri=len(tri_line), n_fan=len(fan_line), n_top=len(top),
                cert_tri=cert_tri, cert_fan=CF["cert"], cert_fj=cert_fj,
                CF=CF, P=P, L=L, lead=lead, js=js, hs=hs)
