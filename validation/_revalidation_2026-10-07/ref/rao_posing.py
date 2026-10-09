"""The axisymmetric Rao-plug posing for T06 (cross-code) and T08b (optimiser): the model's single-wall plug march (the
free jet after the lip, a1_plug_march.plug_march without shroud) started from GENO's OWN field data.

Start line (no interpolation): GENO's last internal C+ characteristic (plug_diag.dat, phase 3, iteration 1: from the
plug up to the cowl point next to the lip E), then E itself with the cowl's state, then the centred fan at E from that
state to the ambient speed q_pa on the model's tabulated gas (a1_plug_march.pm_turn, the lip-jet construction of the
production posing). A C+ start line is the march's preferred posing (a column IS a C+); a C- start line would put the
first wall cell's foot in the fan's centre (coincident rows: singular chord).
Plug: GENO's contour (inf.sol) downstream of the start line's plug point, up to D; slopes = tan(GENO's wall flow
angle). For the optimiser (T08b) the plug downstream of x_s (where the lip's first wave lands) is a cubic spline
through (x_s, y_s) clamped at GENO's slope there and pinned at D, the m-1 interior knot heights free; upstream of x_s
it stays GENO's (the internal kernel is data, as in Rao's construction).
Objective (p_a gauge, p_a = GENO's lip ambient, the ambient this design is optimal for): J = F(start line) - sum
(p - p_a) 2 pi y dy (plug, closed by the start point); the base at D is pinned, so its term is a constant.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rv                                          # noqa: E402
import exact                                       # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
from scipy.optimize import brentq                  # noqa: E402
import a1_ideal_march_jax as A1                    # noqa: E402
import a1_plug_march as PM                         # noqa: E402
import a1_shroud_twin as ST                        # noqa: E402
from a1_toc_variational_jax import spline_coeffs, spline_eval     # noqa: E402


def read_kv_colon(path):
    out = {}
    for ln in open(path):
        if "=" in ln:
            k, v = ln.split("=", 1)
            try:
                out[k.strip()] = float(v.split()[0])
            except (ValueError, IndexError):
                pass
    return out


class GenoRao:
    """GENO RaoPlug run directory -> start line, plug, cowl, references."""

    def __init__(self, d):
        self.d = d
        c = json.load(open(os.path.join(d, "case.json")))
        th = c["thermo"]
        self.gamma, self.R, self.T0, self.P0 = th["gamma"], th["R"], c["gas"][2], c["gas"][3]
        fp = os.path.join(d, "raoplug_performance.dat")
        if os.path.exists(fp):                                    # RaoPlug (type 8): the lip ambient of (8)
            self.perf = read_kv_colon(fp)
            self.pa = self.perf["p_a [Pa]"]
            self.pb = self.perf["p_b [Pa]"]
        else:                                                     # inverse plug from a uniform IVL (type 5)
            self.perf = {}
            self.pa = self.pb = float(c["p_a"])
        a = np.loadtxt(os.path.join(d, "plug_diag.dat"), comments="#", usecols=range(13))
        ph, it, j = a[:, 0].astype(int), a[:, 1].astype(int), a[:, 2].astype(int)
        s = (ph == 3) & (it == 1)
        o = np.argsort(j[s])
        # columns: phase iter j x y rho V theta p T a M gam
        self.cplus = a[s][o][:, 3:13]                    # plug (j=1) -> cowl (j=end)
        s1 = (ph == 1) & (it == it[ph == 1].max())
        self.first_wave = a[s1][np.argsort(j[s1])][:, 3:13]     # E (j=1) -> plug
        s0 = ph == 0
        self.ED = a[s0][np.argsort(j[s0])][:, 3:13]               # the control surface E -> D
        inf = np.loadtxt(os.path.join(d, "inf.sol"), comments="#")
        inf = inf[np.argsort(inf[:, 0])]
        keep = np.r_[True, np.diff(inf[:, 0]) > 0.0]
        self.plug = inf[keep]                                     # x y rho V theta p c T a, increasing x
        sup = np.loadtxt(os.path.join(d, "sup.sol"), comments="#")
        self.cowl = sup                                            # row 0 = E (fan-end state), row 1.. upstream
        self.E = sup[0, :2]
        self.x_s, self.y_s = self.first_wave[-1, 0], self.first_wave[-1, 1]   # where the first wave lands
        self.D = self.plug[-1, :2]


def resample_cplus(cp, n):
    """GENO's C+ start data (rows x y rho V theta p ...) resampled to n points: cubic splines of every column in
    chord length (GENO's points are dense and smooth; the data error is the spline's, ~1e-9 on these lines)."""
    from scipy.interpolate import CubicSpline
    s = np.r_[0.0, np.cumsum(np.hypot(np.diff(cp[:, 0]), np.diff(cp[:, 1])))]
    keep = np.r_[True, np.diff(s) > 1e-12]
    s, cp = s[keep], cp[keep]
    sq = np.linspace(0.0, s[-1], n)
    return np.stack([CubicSpline(s, cp[:, k])(sq) for k in range(cp.shape[1])], 1)


class RaoPosing:
    def __init__(self, d, K=120, n_fan=20, m=10, design=False, Kfix=None, n_cplus=None):
        g = self.g = GenoRao(d)
        if n_cplus is not None and len(g.cplus) != n_cplus:
            g.cplus = resample_cplus(g.cplus, n_cplus)
        self.G = exact.PerfectGas(g.gamma, g.R, g.T0, g.P0)
        T_lo = float(self.G.T(4.0))
        self.tab, self.ta = rv.model_table(g.gamma, g.R, g.T0, g.P0, [0.8 * T_lo, 1.02 * g.T0])
        self.pa = g.pa
        fq = lambda qq: float(A1.state_q(jnp.float64(qq), self.ta)[1]) - self.pa      # noqa: E731
        lo, hi = 1.02 * self.tab["_as"], 3.2 * self.tab["_as"]
        while not (np.isfinite(fq(hi)) and fq(hi) < 0.0):
            hi = lo + 0.9 * (hi - lo)
        self.qpa = brentq(fq, lo, hi, xtol=1e-12 * self.tab["_as"])
        # ---- start line: GENO's C+ (plug -> cowl), E with the cowl's pre-fan state, the fan at E to q_pa
        cp = g.cplus
        xs_, ys_ = cp[:, 0], cp[:, 1]
        us_, vs_ = cp[:, 3] * np.cos(cp[:, 4]), cp[:, 3] * np.sin(cp[:, 4])
        cw = g.cowl[1]                                         # the cowl state next to E (pre-fan)
        qE, thE = float(cw[3]), float(cw[4])
        rows = [np.stack([xs_, ys_, us_, vs_], 1), np.array([[g.E[0], g.E[1], qE * np.cos(thE), qE * np.sin(thE)]])]
        for kf in range(1, n_fan + 1):
            qk = qE + (self.qpa - qE) * kf / n_fan
            thk = thE + float(PM.pm_turn(jnp.float64(qE), jnp.float64(qk), self.ta, 16))
            rows.append(np.array([[g.E[0], g.E[1], qk * np.cos(thk), qk * np.sin(thk)]]))
        st = np.concatenate(rows, 0)
        self.start = (st[:, 0], st[:, 1], st[:, 2], st[:, 3])
        self.start_arr = st
        self.N = len(st)
        self.q_lip, self.th_lip = qE, thE
        self.th_edge = thE + float(PM.pm_turn(jnp.float64(qE), jnp.float64(self.qpa), self.ta, 16))
        # ---- the plug: GENO's contour from the start line's plug point to D
        pl = g.plug
        sel = pl[:, 0] > xs_[0] + 1e-12
        self.wall_g = np.concatenate([[[xs_[0], ys_[0], np.tan(cp[0, 4])]],
                                      np.stack([pl[sel, 0], pl[sel, 1], np.tan(pl[sel, 4])], 1)], 0)
        self.p_wall_g = np.r_[cp[0, 5], pl[sel, 5]]
        self.K = K
        # stations: the carrier's curvature measure on GENO's dense wall (x > x_start), slopes = tan(GENO's angle)
        sx, _, _ = ST.stations_from(self.wall_g[:, :2], K)
        self.sx = np.asarray(sx, float)
        # the wall between GENO's points: y and slope from ONE cubic spline per GENO segment (the isobaric edge up to
        # x_s, the Phase-1 wall after it). Linear y with linearly
        # interpolated angles (the first form) is inconsistent by ~half a vertex turning where GENO's points are
        # sparse (the isobaric edge: 55 points, 7.4e-3 apart, 1.2 deg of turning): a wall-angle error dth gives
        # dp/p = gamma M^2 / sqrt(M^2 - 1) dth ~ 5e-4 there (measured with the first form: 4.2e-4).
        from scipy.interpolate import CubicSpline
        # GENO's lists repeat points at the joins of its phases (measured: dx 4e-12 and 7e-7 at the start, 3e-8 and
        # 1e-8 at x_s): a cubic spline through points that close turns their y round-off into slopes of order 1;
        # points closer than 1e-6 to the previous kept one are dropped (GENO's spacing elsewhere: 1e-4 .. 7e-3)
        keep = [0]
        for k_ in range(1, len(self.wall_g)):
            if self.wall_g[k_, 0] - self.wall_g[keep[-1], 0] > 1e-6:
                keep.append(k_)
        self.wall_g = self.wall_g[keep]
        self.p_wall_g = self.p_wall_g[keep]
        xw, yw, sw = self.wall_g[:, 0], self.wall_g[:, 1], self.wall_g[:, 2]
        i_s = int(np.argmin(np.abs(xw - g.x_s)))
        # the wall is GENO's POINTS (its streamline); not-a-knot ends, GENO's flow angles are not imposed: near D
        # they disagree with GENO's own polyline by up to 7.3e-4 rad (measured; 1e-4 or less elsewhere)
        self.cs = (CubicSpline(xw[:i_s + 1], yw[:i_s + 1], bc_type="not-a-knot"),
                   CubicSpline(xw[i_s:], yw[i_s:], bc_type="not-a-knot"))
        self.x_join = float(xw[i_s])
        self.sy_g, self.ss_g = self.wall_of(self.sx)
        on = np.arange(len(xw))
        self.rep_err = float(np.max(np.abs(np.arctan(self.wall_of(xw)[1]) - np.arctan(sw))[on]))
        F = PM.col_fluxes(st, self.ta, self.pa, 1.0)
        self.mdot_start, self.F_start = abs(F[0]), F[1]
        # ---- the design (T08b): spline on [x_s, x_D]
        self.design = design
        if design:
            self.m = m
            xd = g.D[0]
            self.xk = g.x_s + (xd - g.x_s) * np.arange(1, m + 1) / m       # the last knot at D (pinned)
            self.slope_s = float(np.interp(g.x_s, self.wall_g[:, 0], self.wall_g[:, 2]))
            self.free = self.sx > g.x_s
            self.W_geno = np.interp(self.xk[:-1], self.wall_g[:, 0], self.wall_g[:, 1])

    # ------------------------------------------------------------- walls
    def wall_of(self, x):
        """GENO's wall (y, slope) at abscissae x from the two clamped splines."""
        x = np.asarray(x, float)
        a, b = self.cs
        left = x <= self.x_join
        return np.where(left, a(x), b(x)), np.where(left, a(x, 1), b(x, 1))

    def walls(self, W=None):
        if not self.design or W is None:
            return jnp.asarray(self.sx), jnp.asarray(self.sy_g), jnp.asarray(self.ss_g)
        g = self.g
        xk = jnp.concatenate([jnp.array([g.x_s]), jnp.asarray(self.xk)])
        yk = jnp.concatenate([jnp.array([g.y_s]), jnp.asarray(W), jnp.array([g.D[1]])])
        Mc = spline_coeffs(xk, yk, self.slope_s)
        y, s = jax.vmap(lambda x: spline_eval(x, xk, yk, Mc))(jnp.asarray(self.sx))
        fr = jnp.asarray(self.free)
        return (jnp.asarray(self.sx), jnp.where(fr, y, jnp.asarray(self.sy_g)), jnp.where(fr, s, jnp.asarray(self.ss_g)))

    def basis(self):
        c = np.asarray(self.walls(np.zeros(self.m - 1))[1])
        B = np.stack([np.asarray(self.walls(np.eye(self.m - 1)[k])[1]) - c for k in range(self.m - 1)], 1)
        return B, c

    def fit_geno(self):
        B, c = self.basis()
        yg = self.sy_g
        W, *_ = np.linalg.lstsq(B[self.free], (yg - c)[self.free], rcond=None)
        return W

    # ------------------------------------------------------------- march, objective
    def march_record(self, W=None, margin=None):
        sx, y, s = (np.asarray(v, float) for v in self.walls(None if W is None else np.asarray(W, float)))
        out, S = PM.plug_march((sx, y, s), self.start, self.qpa, self.tab, 1.0, margin=margin, fast=True)
        return out, S

    def _push(self, pts):
        p0 = jnp.asarray(self.start_arr[0])
        c = jnp.concatenate([p0[None, :], pts[:, :4]], axis=0)
        p = A1.state_q(jnp.sqrt(c[:, 2] ** 2 + c[:, 3] ** 2), self.ta)[1]
        w = 2.0 * jnp.pi * 0.5 * (c[1:, 1] + c[:-1, 1])
        return jnp.sum((0.5 * (p[1:] + p[:-1]) - self.pa) * w * (c[1:, 1] - c[:-1, 1]))

    def J_of(self, out):
        return self.F_start - self._push(out["wall"])

    def J_replay(self, W, sched):
        sx, y, s = self.walls(W)
        out, _ = PM.plug_march((sx, y, s), self.start, self.qpa, self.tab, 1.0, sched=A1.Sched("play", sched.d))
        return self.J_of(out)

    def margin_dict(self, mu0, rho, m_ref=1.0):
        ell = float(self.sx[-1] - self.sx[0]) / len(self.sx)
        return dict(rho=float(rho), mu0=float(mu0), m_ref=float(m_ref), orient=-1.0, f_edge=0.0, jmin=2,
                    ell2=ell ** 2, vec=True, shape=True, eps2=1e-6 * ell ** 2, region="R", cert_net=True)

    def margin_replay(self, W, sched, margin):
        sx, y, s = self.walls(W)
        out, _ = PM.plug_march((sx, y, s), self.start, self.qpa, self.tab, 1.0, sched=A1.Sched("play", sched.d),
                               margin=dict(margin))
        return out["margin_ks"] - margin["mu0"]


def posing_level(d, level, design=False, m=10):
    """RaoPosing at refinement level L: stations 60 * 2^L, fan rays 10 * 2^L, and GENO's C+ start data interpolated
    (cubic in chord length, data error ~1e-9) to 55 * 2^L + 1 points (level 0 = GENO's own 56 points)."""
    from scipy.interpolate import CubicSpline
    rp = RaoPosing(d, K=60 * 2 ** level, n_fan=10 * 2 ** level, m=m, design=design)
    if level > 0:
        cp = rp.g.cplus
        s = np.r_[0.0, np.cumsum(np.hypot(np.diff(cp[:, 0]), np.diff(cp[:, 1])))]
        sq = np.linspace(0.0, s[-1], 55 * 2 ** level + 1)
        cs = {k: CubicSpline(s, cp[:, k]) for k in (0, 1, 3, 4)}
        x_, y_, V_, th_ = (cs[k](sq) for k in (0, 1, 3, 4))
        tail = rp.start_arr[len(cp):]
        st = np.concatenate([np.stack([x_, y_, V_ * np.cos(th_), V_ * np.sin(th_)], 1), tail], 0)
        rp.start = (st[:, 0], st[:, 1], st[:, 2], st[:, 3])
        rp.start_arr = st
        rp.N = len(st)
        F = PM.col_fluxes(st, rp.ta, rp.pa, 1.0)
        rp.mdot_start, rp.F_start = abs(F[0]), F[1]
    return rp
