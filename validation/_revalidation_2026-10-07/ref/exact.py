"""Independent exact references for the revalidation of the rde-nozzle march (2026-10-07).

Written from the textbook relations only (calorically perfect gas, steady inviscid homentropic flow);
nothing here imports or copies the model's own oracles (a1_plug_march.pm_exact, a1_shroud_twin.channel, ...).

  PerfectGas            isentropic relations, Prandtl-Meyer function, area-Mach relation, inverses
  CenteredFan           planar centred expansion (Prandtl-Meyer fan) at a corner: field + streamlines
  SphericalSource       axisymmetric radial source flow (exact Euler solution with v != 0 off the axis)
  wall_push             high-accuracy (p - pa) w dy integral of a known pressure along a known wall
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


class PerfectGas:
    def __init__(self, gamma, R, T0, P0):
        self.g, self.R, self.T0, self.P0 = float(gamma), float(R), float(T0), float(P0)
        self.cp = self.g * self.R / (self.g - 1.0)
        self.qmax = np.sqrt(2.0 * self.cp * self.T0)

    # --- states as functions of the Mach number -------------------------------------------
    def T(self, M):
        return self.T0 / (1.0 + 0.5 * (self.g - 1.0) * np.asarray(M, float) ** 2)

    def p(self, M):
        return self.P0 * (self.T(M) / self.T0) ** (self.g / (self.g - 1.0))

    def rho(self, M):
        return self.p(M) / (self.R * self.T(M))

    def c(self, M):
        return np.sqrt(self.g * self.R * self.T(M))

    def q(self, M):
        return np.asarray(M, float) * self.c(M)

    # --- states as functions of the speed q ---------------------------------------------------
    def T_q(self, q):
        return self.T0 - np.asarray(q, float) ** 2 / (2.0 * self.cp)

    def M_q(self, q):
        return np.asarray(q, float) / np.sqrt(self.g * self.R * self.T_q(q))

    def p_q(self, q):
        return self.P0 * (self.T_q(q) / self.T0) ** (self.g / (self.g - 1.0))

    def rho_q(self, q):
        return self.p_q(q) / (self.R * self.T_q(q))

    def q_of_p(self, p):
        return np.sqrt(2.0 * self.cp * self.T0 * (1.0 - (np.asarray(p, float) / self.P0) ** ((self.g - 1.0) / self.g)))

    def M_of_p(self, p):
        return np.sqrt(2.0 / (self.g - 1.0) * ((self.P0 / np.asarray(p, float)) ** ((self.g - 1.0) / self.g) - 1.0))

    # --- Prandtl-Meyer -----------------------------------------------------------------------------
    def nu(self, M):
        M = np.asarray(M, float)
        a = np.sqrt((self.g + 1.0) / (self.g - 1.0))
        b = np.sqrt(np.maximum(M * M - 1.0, 0.0))
        return a * np.arctan(b / a) - np.arctan(b)

    def M_of_nu(self, nu):
        nu = float(nu)
        if nu <= 0.0:
            return 1.0
        return brentq(lambda M: float(self.nu(M)) - nu, 1.0, 200.0, xtol=1e-15, rtol=1e-15, maxiter=500)

    def mu(self, M):
        return np.arcsin(1.0 / np.asarray(M, float))

    # --- area-Mach ---------------------------------------------------------------------------------
    def area_ratio(self, M):
        M = np.asarray(M, float)
        e = (self.g + 1.0) / (2.0 * (self.g - 1.0))
        return (1.0 / M) * ((2.0 / (self.g + 1.0)) * (1.0 + 0.5 * (self.g - 1.0) * M * M)) ** e

    def M_of_area(self, AR, supersonic=True):
        AR = float(AR)
        if supersonic:
            return brentq(lambda M: float(self.area_ratio(M)) - AR, 1.0 + 1e-14, 100.0, xtol=1e-15, rtol=1e-15,
                          maxiter=500)
        return brentq(lambda M: float(self.area_ratio(M)) - AR, 1e-9, 1.0 - 1e-14, xtol=1e-15, rtol=1e-15,
                      maxiter=500)

    def mass_flux_star(self):
        """rho* a* (the mass flux per unit area at the sonic point)."""
        return float(self.rho(1.0) * self.c(1.0))


class CenteredFan:
    """Planar centred Prandtl-Meyer expansion at the corner F = (xF, yF).

    Upstream: uniform M1 at flow angle th1 (radians). The corner turns the flow by d_nu = nu(M2) - nu(M1) toward
    +y (the expansion of an upper wall that ends at F: the waves are C- characteristics, theta - nu = const along
    the C+ lines that cross them). Downstream of the last wave: uniform M2 at th2 = th1 + d_nu.
    A ray from F at angle phi (characteristic direction theta - mu) carries a constant state."""

    def __init__(self, gas, M1, th1, M2, xF, yF):
        self.gas, self.M1, self.th1, self.M2 = gas, float(M1), float(th1), float(M2)
        self.xF, self.yF = float(xF), float(yF)
        self.nu1 = float(gas.nu(M1))
        self.th2 = self.th1 + float(gas.nu(M2)) - self.nu1
        self.phi1 = self.th1 - float(gas.mu(M1))         # first wave
        self.phi2 = self.th2 - float(gas.mu(M2))         # last wave

    def state_on_ray(self, phi):
        """(M, theta) on the fan ray of angle phi, phi1 <= phi <= phi2 (ray angles measured from F; the rays point
        downstream-downward and rotate counter-clockwise from the first wave to the last)."""
        g = self.gas

        def f(M):
            th = self.th1 + float(g.nu(M)) - self.nu1
            return th - float(g.mu(M)) - phi
        M = brentq(f, self.M1, self.M2, xtol=1e-15, rtol=1e-15, maxiter=500)
        return M, self.th1 + float(g.nu(M)) - self.nu1

    def region(self, x, y):
        """0 upstream of the first wave, 1 inside the fan, 2 downstream of the last wave; points below F only."""
        ang = np.arctan2(y - self.yF, x - self.xF)
        if ang <= self.phi1:
            return 0, ang
        if ang >= self.phi2:
            return 2, ang
        return 1, ang

    def state(self, x, y):
        reg, ang = self.region(x, y)
        if reg == 0:
            return self.M1, self.th1
        if reg == 2:
            return self.M2, self.th2
        return self.state_on_ray(ang)

    def streamline(self, x0, y0, x_end, n_out=4001):
        """The streamline through (x0, y0) (a point upstream of the fan, below F), integrated to x_end.
        Straight segments in the uniform regions, solve_ivp (rtol 1e-12) across the fan."""
        # entry into the fan: along th1 from (x0, y0) to the first wave
        t1 = np.tan(self.th1)
        # first wave: y - yF = tan(phi1) (x - xF)
        xe = (y0 - t1 * x0 - self.yF + np.tan(self.phi1) * self.xF) / (np.tan(self.phi1) - t1)
        ye = y0 + t1 * (xe - x0)

        def rhs(x, Y):
            M, th = self.state_on_ray(np.clip(np.arctan2(Y[0] - self.yF, x - self.xF), self.phi1, self.phi2))
            return [np.tan(th)]

        def exit_ev(x, Y):
            return np.arctan2(Y[0] - self.yF, x - self.xF) - self.phi2
        exit_ev.terminal, exit_ev.direction = True, 1
        sol = solve_ivp(rhs, (xe, x_end + 10.0 * abs(x_end - x0)), [ye], events=exit_ev, rtol=1e-12, atol=1e-14,
                        dense_output=True, max_step=(x_end - x0) / 400.0)
        xo = float(sol.t_events[0][0])
        yo = float(sol.y_events[0][0][0])
        self.sl_points = dict(entry=(xe, ye), exit=(xo, yo))

        def y_of(x):
            x = np.asarray(x, float)
            yv = np.where(x <= xe, y0 + t1 * (x - x0), 0.0)
            infan = (x > xe) & (x < xo)
            if np.any(infan):
                yv = np.where(infan, sol.sol(np.clip(x, xe, xo))[0], yv)
            yv = np.where(x >= xo, yo + np.tan(self.th2) * (x - xo), yv)
            return yv

        def slope_of(x):
            x = np.asarray(x, float)
            out = np.empty_like(x)
            for i, xi in enumerate(np.atleast_1d(x)):
                if xi <= xe:
                    out.flat[i] = t1
                elif xi >= xo:
                    out.flat[i] = np.tan(self.th2)
                else:
                    out.flat[i] = rhs(xi, [float(y_of(xi))])[0]
            return out
        return y_of, slope_of, (xe, ye), (xo, yo)


class SphericalSource:
    """Radial (source) flow from the origin, axisymmetric about the x axis: the flow at (x, y) is directed along
    the ray from the origin, its Mach number set by the area-Mach relation with A/A* = (r / r_star)^2 on the
    supersonic branch. An exact solution of the axisymmetric Euler equations (homentropic, irrotational)."""

    def __init__(self, gas, r_star):
        self.gas, self.r_star = gas, float(r_star)

    def M(self, r):
        return np.array([self.gas.M_of_area((ri / self.r_star) ** 2) for ri in np.atleast_1d(r)])

    def state(self, x, y):
        r = np.hypot(x, y)
        M = self.M(r)
        q = self.gas.q(M)
        th = np.arctan2(y, x)
        return M, q * np.cos(th), q * np.sin(th)


def wall_push(x, y, p, pa, axi):
    """Integral of (p - pa) w dy along a polyline sampled finely (trapezoid on a dense sampling: the caller
    passes >= 1e4 points of the EXACT p, so the quadrature error is far below the model's)."""
    x, y, p = (np.asarray(v, float) for v in (x, y, p))
    w = 2.0 * np.pi * 0.5 * (y[1:] + y[:-1]) if axi else 1.0
    return float(np.sum((0.5 * (p[1:] + p[:-1]) - pa) * w * np.diff(y)))
