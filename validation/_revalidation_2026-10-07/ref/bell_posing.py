"""Bell posing of the revalidation (2026-10-08): the model's bell engine (validation/a1_toc_variational_jax: IVL ->
throat-arc fan -> prescribed wall, record + frozen-plan replay, reverse AD) on a GENO bell case, with the lip pinned.

Design vector (the engine's own class, M_NODES = 8 knots): W = [theta_B, y_1, ..., y_8], theta_B = where the wall
leaves the downstream throat arc (radius rtd, C^1), y_k = wall radii at knots uniform on [x_B(theta_B), L], natural
cubic spline clamped at B; the LAST knot is the lip and is PINNED here (y_8 = GENO's exit radius, at x = L = GENO's
length): the walk sees V = [theta_B, y_1, ..., y_7]. Objective: the engine's J = 2 pi int p y dy over the divergent
wall (vacuum): with the exit point fixed the ambient term is a constant, so the maximiser is the same at any p_a
(Rao 1958 with p_a = 0; GENO's TOC is run in vacuum).
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rv                                                  # noqa: E402,F401  (puts validation/ on the path)
import jax                                                 # noqa: E402
import jax.numpy as jnp                                    # noqa: E402
import a1_ideal_march_jax as A1                            # noqa: E402
import a1_march_scan as SC                                 # noqa: E402
import thermotab_c1_jax as TH                              # noqa: E402
import a1_toc_variational_jax as TV                        # noqa: E402

jax.config.update("jax_enable_x64", True)


def geno_wall(d):
    """GENO's divergent wall (x >= 0) from its profile file."""
    fn = [f for f in os.listdir(d) if f.startswith("profile")][0]
    a = np.loadtxt(os.path.join(d, fn))
    m = a[:, 0] >= 0.0
    return a[m, 0], a[m, 1]


def geno_cf(d):
    """GENO's vacuum C_F and Isp from performance.dat (4 decimals)."""
    v = open(os.path.join(d, "performance.dat")).read().split()
    return float(v[4]), float(v[5])


_TAB = {}


def tables():
    if "tab" not in _TAB:
        tab = A1.prep_tab(A1.build_tab_nasa())
        c1 = TH.build_c1(tab)

        def state_c1(q, ta_ignored):
            return TH.state_q_c1(q, c1)

        _TAB.update(tab=tab, state=state_c1, solv=SC.cached_solvers(("thc1_nasa", 1.0), state_c1, 1.0))
    return _TAB["tab"], _TAB["state"], _TAB["solv"]


class BellPosing:
    def __init__(self, L, yL, NI=21, Nw=60, da_deg=0.5, yt=1.0, rtu=1.5, rtd=0.45, M=None):
        if M is not None:
            TV.M_NODES = int(M)          # the engine's number of wall points is a module constant read at trace time
        self.tab, self.state, self.solv = tables()
        self.L, self.yL = float(L), float(yL)
        self.cfg = dict(NI=NI, Nw=Nw, da_deg=da_deg, yt=yt, rtu=rtu, rtd=rtd, xtronc=self.L)
        self.m = TV.M_NODES
        self._jit = {}

    # --- design vector <-> wall -------------------------------------------------
    def full(self, V):
        V = jnp.asarray(V)
        return jnp.concatenate([V, jnp.array([self.yL])])

    def knots(self, V):
        thB = float(V[0])
        xB = self.cfg["rtd"] * np.sin(thB)
        return xB + (self.L - xB) * np.arange(1, self.m + 1) / self.m

    def fit(self, wx, wy, thB=None):
        """V reproducing a wall: theta_B = the wall's largest slope near the throat (the attachment of a bell whose
        contour leaves the arc where it turns back), y_k = the wall at the knots."""
        if thB is None:
            xg = np.linspace(0.02, 0.4 * self.L, 2000)
            thB = float(np.arctan(np.max(np.gradient(np.interp(xg, wx, wy), xg))))
        V = np.concatenate([[thB], np.zeros(self.m - 1)])
        V[1:] = np.interp(self.knots(V)[:-1], wx, wy)
        return V

    def fit_lsq(self, wx, wy):
        """The class member closest to a wall (least squares on y over the whole divergent wall, arc included):
        the best spline. The engine's spline is reproduced with scipy (clamped slope tan theta_B at B, natural at
        the lip; checked against wall_xy by the caller)."""
        from scipy.interpolate import CubicSpline
        from scipy.optimize import least_squares
        rtd, yt, L = self.cfg["rtd"], self.cfg["yt"], self.L
        xi = np.arange(1, self.m + 1) / self.m

        def res(V):
            th = V[0]
            xB, yB = rtd * np.sin(th), yt + rtd * (1.0 - np.cos(th))
            xs = np.concatenate([[xB], xB + (L - xB) * xi])
            ys = np.concatenate([[yB], V[1:], [self.yL]])
            cs = CubicSpline(xs, ys, bc_type=((1, np.tan(th)), (2, 0.0)))
            a = wx <= xB
            ya = yt + rtd * (1.0 - np.cos(np.arcsin(np.clip(wx[a] / rtd, 0.0, 1.0))))
            return np.concatenate([ya - wy[a], cs(wx[~a]) - wy[~a]])

        r = least_squares(res, self.fit(wx, wy), x_scale="jac")
        return np.asarray(r.x, float)

    def wall_xy(self, V, n=400):
        """The design wall (arc + spline) as points, for figures."""
        xB, yB, xs, ys, M = TV.wall_geometry(self.full(V), (self.cfg["yt"], self.cfg["rtu"], self.cfg["rtd"]),
                                             self.L)
        th = np.linspace(0.0, float(V[0]), 40)
        xa = self.cfg["rtd"] * np.sin(th)
        ya = self.cfg["yt"] + self.cfg["rtd"] * (1.0 - np.cos(th))
        xq = np.linspace(float(xB), self.L, n)
        yq = np.array([float(TV.spline_eval(x, xs, ys, M)[0]) for x in xq])
        return np.concatenate([xa, xq[1:]]), np.concatenate([ya, yq[1:]])

    # --- the march ------------------------------------------------------------------
    def record(self, V):
        out, plan = TV.run_toc_record(np.asarray(self.full(V)), self.tab, self.cfg, state_fn=self.state,
                                      solvers=self.solv)
        return out, plan

    def J_of(self, out):
        return float(TV.objective_J(out["wall"], self.tab, self.cfg, state_fn=self.state))

    def _vg(self, plan):
        k = id(plan)
        if k not in self._jit:
            if len(self._jit) > 4:
                self._jit.clear()
            run = TV.make_run_toc_scan_jit(self.tab, self.cfg, plan, state_fn=self.state, solvers=self.solv)
            f = lambda V: TV.objective_J(run(self.full(V)), self.tab, self.cfg, state_fn=self.state)  # noqa: E731
            self._jit[k] = (plan, jax.jit(jax.value_and_grad(f)))
        return self._jit[k][1]

    def jg(self, V, plan):
        v, g = self._vg(plan)(jnp.asarray(V, dtype=float))
        return float(v), np.asarray(g, float)
