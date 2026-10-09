"""A planar plug posing for the optimiser tests (T08a), built ONLY from the model's own pieces: the march
(a1_plug_march.plug_march with the cowl, the lip jet and the wedge rule of T03), the wavefront replay of the production
walks (a1_wavefront_replay), the spline basis of the walls (a1_toc_variational_jax: clamped left, natural right), the
fold-margin dictionary of the two-wall carrier (a1_twowall.TwoWall.margin_dict, region R + channel, shape mode). It
exposes the three hooks the SQP driver calls through c = dict(throat=posing): march_record(W, margin),
J_replay(W, sched), margin_replay(W, sched, margin) -- exactly as a1_twowall.TwoWall does.

Problem (the exact field of T03): uniform M1 = 1.556 (SDT mean gas) at theta1 = -20 deg through the vertical start line
x = 0, y in [0.5, 1]; a straight cowl at theta1 to the lip F (x 0.3); ambient p_a = p(M2), nu(M2) = nu(M1) + 20 deg.
Design: the plug y(x) on [0, L], a cubic spline through (0, 0.5) and m knots at x_k = L k / m (clamped slope
tan(theta1) at 0: the wall leaves the start tangent to the flow; natural at L); W = the m knot heights (the tip free).
Objective: thrust per unit depth in the p_a gauge, T = F_in - p_a A_in - sum (p - p_a) dy (plug) + sum (p - p_a) dy
(cowl), the base at p_b = p_a (no term), the carrier's own closing of the polylines by their start points.
Exact optimum: the ideal plug (the streamline of the centred-expansion field through (0, 0.5), flat after the last
wave), T_ideal = rho2 q2^2 h2 = mdot V_a.
"""
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
import a1_wavefront_replay as WF                   # noqa: E402
from a1_toc_variational_jax import spline_coeffs, spline_eval     # noqa: E402

TH1_DEG, X0, Y_L, Y_U, XF = -20.0, 0.0, 0.5, 1.0, 0.3


class PlanarPlug:
    def __init__(self, K=80, N=21, m=12, L=2.0, wavefront=True):
        gm = rv.sdt_gas()
        self.G = G = exact.PerfectGas(gm["gamma"], gm["R"], gm["T0"], gm["P0"])
        self.tab, self.ta = rv.model_table(gm["gamma"], gm["R"], gm["T0"], gm["P0"], gm["T_tab"])
        self.M1, self.th1 = gm["M_in"], np.radians(TH1_DEG)
        self.M2 = G.M_of_nu(float(G.nu(self.M1)) - self.th1)
        self.pa = float(G.p(self.M2))
        self.yF = Y_U + (XF - X0) * np.tan(self.th1)
        self.fan = exact.CenteredFan(G, self.M1, self.th1, self.M2, XF, self.yF)
        self.y_ideal, self.s_ideal, self.P_in, self.P_out = self.fan.streamline(X0, Y_L, L)
        self.K, self.N, self.m, self.L, self.wavefront = K, N, m, L, wavefront
        q1 = float(G.q(self.M1))
        self.q1 = q1
        self.sx = X0 + (L - X0) * np.arange(1, K + 1) / K
        Ks = max(8, int(round(K * (XF - X0) / (L - X0))))
        self.xs = X0 + (XF - X0) * np.arange(0, Ks + 1) / Ks
        self.ys = Y_U + (self.xs - X0) * np.tan(self.th1)
        self.ss = np.full(Ks + 1, np.tan(self.th1))
        yline = np.linspace(Y_L, Y_U, N)
        self.start = (X0, yline, np.full(N, q1 * np.cos(self.th1)), np.full(N, q1 * np.sin(self.th1)))
        dy_row = (Y_U - Y_L) / (N - 1)
        self.m_w = max(1, int(round((self.sx[0] - X0) * np.tan(np.arcsin(1.0 / self.M1)) / dy_row)))
        fq = lambda qq: float(A1.state_q(jnp.float64(qq), self.ta)[1]) - self.pa      # noqa: E731
        lo, hi = 1.02 * self.tab["_as"], 3.2 * self.tab["_as"]
        while not (np.isfinite(fq(hi)) and fq(hi) < 0.0):
            hi = lo + 0.9 * (hi - lo)
        self.qpa = brentq(fq, lo, hi, xtol=1e-12 * self.tab["_as"])
        self.lip_jet = dict(qpa=self.qpa, n_fan=int(round(0.5 * N)), n_gl=16)
        col0 = np.stack([np.full(N, X0), yline, self.start[2], self.start[3]], 1)
        self.F_in = float(PM.col_fluxes(col0, self.ta, self.pa, 0.0)[1])       # p_a gauge
        self.xk = X0 + (L - X0) * np.arange(1, m + 1) / m
        # the exact optimum
        rho2, q2 = float(G.rho(self.M2)), float(G.q(self.M2))
        self.mdot = float(G.rho(self.M1)) * q1 * np.cos(self.th1) * (Y_U - Y_L)
        self.h2 = self.mdot / (rho2 * q2)
        self.T_ideal = self.mdot * q2
        self.W_ideal_knots = np.asarray(self.y_ideal(self.xk), float)

    # ------------------------------------------------------------- walls
    def walls(self, W):
        xk = jnp.concatenate([jnp.array([X0]), jnp.asarray(self.xk)])
        yk = jnp.concatenate([jnp.array([Y_L]), jnp.asarray(W)])
        Mc = spline_coeffs(xk, yk, float(np.tan(self.th1)))
        y, s = jax.vmap(lambda x: spline_eval(x, xk, yk, Mc))(jnp.asarray(self.sx))
        return jnp.asarray(self.sx), y, s

    def basis(self):
        """y at the stations = B W + c (the spline is linear in the knot heights)."""
        c = np.asarray(self.walls(np.zeros(self.m))[1])
        B = np.stack([np.asarray(self.walls(np.eye(self.m)[k])[1]) - c for k in range(self.m)], 1)
        return B, c

    def fit_ideal(self):
        """The class member closest to the ideal plug in the least-squares sense at the stations."""
        B, c = self.basis()
        W, *_ = np.linalg.lstsq(B, np.asarray(self.y_ideal(self.sx)) - c, rcond=None)
        return W

    # ------------------------------------------------------------- march, objective, margin
    def march_record(self, W, margin=None):
        sx, y, s = (np.asarray(v, float) for v in self.walls(np.asarray(W, float)))
        if margin is not None:
            margin["x_max"] = float(max(sx[-1], self.xs[-1]))
            if margin.get("channel"):
                margin["x_channel"] = float(self.xs[-1])
        graph = {} if self.wavefront else None
        out, S = PM.plug_march((sx, y, s), self.start, self.q1, self.tab, 0.0, shroud=(self.xs, self.ys, self.ss),
                               wedge_every=self.m_w, fast=True, margin=margin, graph=graph, lip_jet=self.lip_jet)
        if graph is not None:
            S.plan = WF.plan(graph)
        return out, S

    def _replay(self, W, sched, margin):
        sx, y, s = self.walls(W)
        if margin is not None:
            margin = dict(margin)
            margin["x_max"] = max(float(sx[-1]), float(self.xs[-1]))
        if self.wavefront and getattr(sched, "plan", None) is not None:
            return WF.replay(sched.plan, sched, (sx, y, s), (self.xs, self.ys, self.ss), self.start, self.tab, 0.0,
                             16, margin=margin, rows_block=1024, lip_jet=self.lip_jet)
        S_ = A1.Sched("play", sched.d)
        out, _ = PM.plug_march((sx, y, s), self.start, self.q1, self.tab, 0.0, sched=S_,
                               shroud=(self.xs, self.ys, self.ss), wedge_every=self.m_w, margin=margin,
                               lip_jet=self.lip_jet)
        return out

    def _push(self, pts, y0):
        p0 = jnp.array([X0, y0, self.start[2][0], self.start[3][0]])
        c = jnp.concatenate([p0[None, :], pts[:, :4]], axis=0)
        p = A1.state_q(jnp.sqrt(c[:, 2] ** 2 + c[:, 3] ** 2), self.ta)[1]
        return jnp.sum((0.5 * (p[1:] + p[:-1]) - self.pa) * (c[1:, 1] - c[:-1, 1]))

    def J_of(self, out):
        return self.F_in - self._push(out["wall"], Y_L) + self._push(out["shroud"], Y_U)

    def J_replay(self, W, sched):
        return self.J_of(self._replay(W, sched, None))

    def margin_dict(self, mu0, rho, m_ref=1.0):
        ell = float(self.sx[-1] - X0) / len(self.sx)
        return dict(rho=float(rho), mu0=float(mu0), m_ref=float(m_ref), orient=-1.0, f_edge=0.0, jmin=2,
                    ell2=ell ** 2, vec=True, shape=True, eps2=1e-6 * ell ** 2, region="R", cert_net=True,
                    channel=True)

    def margin_replay(self, W, sched, margin):
        return self._replay(W, sched, margin)["margin_ks"] - margin["mu0"]
