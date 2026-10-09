"""Rao 1961 (Astronautica Acta 7, 'Spike nozzle contour for optimum thrust') solved from its own equations, written
from the paper only. Perfect gas, isentropic, axisymmetric; lengths in units of R_E (lip radius), pressures in P_c.

Control surface ED (a right-running characteristic, phi = theta - alpha) carries
  (6)  w cos(theta + alpha) / cos(alpha)          = C2      (mass multiplier; Rao writes cos(-theta-alpha))
  (7)  R rho w^2 sin^2(theta) tan(alpha)          = C3      (length multiplier)
end conditions
  (8)  E: (p - p_a) cot(alpha) / (rho w^2 / 2)    = sin(-2 theta)   -> p_a a posteriori
  (9)  D: (p - p_b) cot(alpha) / (rho w^2 / 2)    = sin(-2 theta)   -> where ED stops (p_b given, 0 in the paper)
so along ED every quantity is algebraic in M: theta(M) from (6), R(M) from (7). Then
  x_D   = int dR / tan(theta - alpha)                                 (length, E at x = 0)
  mdot  = int rho w sin(alpha) / sin(alpha - theta) 2 pi R |dR|       (mass through ED)
  F_vac = int [p + rho w^2 sin(alpha) cos(theta) / sin(alpha - theta)] 2 pi R |dR|   (+ p_b pi R_D^2)
  eps = pi R_E^2 rho* w* / mdot,  C_F = F_vac / (P_c A*)  (eqs 11, 12).
Ideal spike (theta = 0 on ED, uniform exit at p_a): M_a from eps, length R_E sqrt(M_a^2 - 1), C_F = one-dimensional.
"""
import numpy as np
from scipy.optimize import brentq

import exact


class Rao1961:
    def __init__(self, gamma):
        self.G = exact.PerfectGas(gamma, 1.0, 1.0, 1.0)        # R = T0 = P0 = 1: ratios only
        G = self.G
        self.rs_ws = float(G.rho(1.0) * G.q(1.0))              # rho* w*

    def _state(self, M):
        G = self.G
        return G.p(M), G.rho(M), G.q(M), np.arcsin(1.0 / M)

    def member(self, M_E, th_E_deg, p_b=0.0, n=40001, pb_model=None):
        """pb_model(p, M) -> p_b: a base pressure set by the state at D (Humphreys et al. 1971 eq. 12 is
        0.846 p / M^1.3); then (9) is solved with p_b = pb_model(p_D, M_D) at the same point."""
        G = self.G
        thE = np.radians(th_E_deg)
        pE, rE, wE, aE = self._state(M_E)
        C2 = wE * np.cos(thE + aE) / np.cos(aE)
        sg = np.sign(thE + aE)                                 # branch of (6) through E
        C3 = 1.0 * rE * wE ** 2 * np.sin(thE) ** 2 * np.tan(aE)
        p_a = pE - 0.5 * rE * wE ** 2 * np.tan(aE) * np.sin(-2.0 * thE)

        def theta_R(M):
            p, r, w, a = self._state(M)
            th = sg * np.arccos(np.clip(C2 * np.cos(a) / w, -1.0, 1.0)) - a
            R = C3 / (r * w ** 2 * np.sin(th) ** 2 * np.tan(a))
            return th, R, p, r, w, a

        def corner(M):
            th, R, p, r, w, a = theta_R(M)
            pb = p_b if pb_model is None else pb_model(p, M)
            return (p - pb) / (0.5 * r * w ** 2) / np.tan(a) + np.sin(2.0 * th)

        # ED leaves E towards the axis: the direction of M along which R decreases (for the paper's members M
        # DEcreases from E to D, Fig. 2); D = the first root of (9) on that branch (scan, then refine)
        dM = -1e-4 if theta_R(M_E - 1e-4)[1] < 1.0 else 1e-4
        Ms = M_E + dM * np.arange(1, 40001)
        Ms = Ms[Ms > 1.0 + 1e-9]
        g = corner(Ms)
        k = int(np.argmax(np.sign(g) != np.sign(g[0])))
        M_D = brentq(corner, min(Ms[k - 1], Ms[k]), max(Ms[k - 1], Ms[k]), xtol=1e-14)
        M = np.linspace(M_E, M_D, n)
        th, R, p, r, w, a = theta_R(M)
        dR = np.diff(R)
        mid = lambda f: 0.5 * (f[1:] + f[:-1])                 # noqa: E731
        x = np.r_[0.0, np.cumsum(mid(1.0 / np.tan(th - a)) * dR)]
        dm = mid(r * w * np.sin(a) / np.sin(a - th) * 2.0 * np.pi * R) * (-dR)
        dF = mid((p + r * w ** 2 * np.sin(a) * np.cos(th) / np.sin(a - th)) * 2.0 * np.pi * R) * (-dR)
        if pb_model is not None:
            p_b = float(pb_model(p[-1], M[-1]))
        mdot, F = dm.sum(), dF.sum() + p_b * np.pi * R[-1] ** 2
        A_s = mdot / self.rs_ws
        return dict(M=M, theta=th, R=R, x=x, p=p, p_a=p_a, p_b=p_b, M_D=M_D, theta_D=th[-1], x_D=x[-1], R_D=R[-1],
                    eps=np.pi / A_s, C_F=F / A_s, mdot=mdot, F=F, C2=C2, C3=C3)

    def ideal(self, eps):
        G = self.G
        Ma = G.M_of_area(eps)
        p, r, w, a = self._state(Ma)
        C_F = (self.rs_ws * w + p * eps) / 1.0                 # (mdot V_a + p_a A_e) / (P_c A*)
        return dict(M_a=Ma, L=np.sqrt(Ma ** 2 - 1.0), C_F=C_F, p_a=p)


# Rao 1961, published (Table 1, Table 2, Table 3 and the text of section 4)
PUB = {
    "e381": dict(M_E=2.4, th_E=-8.25, p_a=0.0355, eps=3.81, L=1.164, R_D=0.137, C_F=1.5804, th_D=-19.73,
                 ideal_L=2.433, ideal_L_text=2.428, ideal_C_F=1.5909, trunc_R_D=0.245, trunc_C_F=1.5783),
    "e1069": dict(M_E=3.2, th_E=-6.0, eps=10.69, L=1.731, R_D=0.126, C_F=1.7269, th_D=-14.94,
                  ideal_L=3.271, ideal_C_F=1.7326, trunc_C_F=1.7252),
}
# Table 1 (eps 3.81, L/R_E 1.164): X/R_E, R/R_E, theta deg  (row 0 = cowl lip, row 1 = throat on the spike)
TAB1 = np.array([[0.0, 1.000, np.nan], [-0.109, 0.9165, -51.92], [-0.016, 0.782, -50.10], [0.034, 0.728, -45.18],
                 [0.087, 0.678, -41.21], [0.132, 0.640, -38.44], [0.192, 0.596, -35.59], [0.267, 0.545, -32.73],
                 [0.314, 0.516, -31.21], [0.367, 0.484, -29.72], [0.429, 0.450, -28.23], [0.502, 0.413, -26.75],
                 [0.588, 0.371, -25.32], [0.690, 0.324, -23.92], [0.815, 0.271, -22.59], [0.969, 0.209, -21.47],
                 [1.164, 0.137, -19.73]])
# Table 2 (eps 10.69, L/R_E 1.731)
TAB2 = np.array([[0.0, 1.000, np.nan], [-0.045, 0.9856, -71.43], [-0.021, 0.917, -63.06], [-0.002, 0.886, -56.23],
                 [0.024, 0.852, -50.27], [0.054, 0.818, -45.73], [0.101, 0.775, -40.56], [0.173, 0.718, -35.52],
                 [0.245, 0.670, -32.04], [0.347, 0.611, -28.45], [0.413, 0.577, -26.66], [0.494, 0.537, -24.90],
                 [0.594, 0.493, -23.12], [0.717, 0.442, -21.32], [0.874, 0.384, -19.56], [1.076, 0.316, -17.85],
                 [1.347, 0.233, -16.34], [1.731, 0.126, -14.94]])


# Humphreys, Thompson & Hoffman 1971 (AIAA J 9(8) 1581-1587), the Rao nozzle of their comparison (Table 3, text p.1586).
# Table 3 is typed as printed (checked at 300 dpi, 2026-10-07); its angle -12.27169 at x 5.33714 is a misprint for
# -22.27169 (neighbours -25.23 / -20.08; GENO's wall there -22.29 deg). Only x, y are compared.
# same mass flow, plug length, ambient, gas and base-pressure model as their parametric study.
HTH = dict(gamma=1.23, R_ftlbf=56.0, Tc_R=6000.0, pc_psia=500.0, pa_psia=14.7, mdot_lbm=148.08, x_D_in=11.51781,
           y_E_in=8.33, inj_deg=-58.5, thrust_lbf=34253.0, thrust_rao_startline_lbf=34375.0, R_D_in=1.37506,
           th_D_deg=-13.25333)
TAB3_HTH = np.array([[-0.63971, 7.60953, -60.69463], [-0.52553, 7.41133, -59.26745], [-0.38991, 7.19374, -56.76264],
                     [-0.28105, 7.03417, -54.62384], [-0.11511, 6.81327, -51.56682], [0.08454, 6.57580, -48.37210],
                     [0.26305, 6.38348, -45.92900], [0.54982, 6.10414, -42.64770], [0.80980, 5.87499, -40.18842],
                     [1.11665, 5.62702, -37.74413], [1.75877, 5.16641, -33.72519], [2.24216, 4.85831, -31.35732],
                     [3.03421, 4.40556, -28.40556], [4.04195, 3.89898, -25.23198], [5.33714, 3.33063, -12.27169],
                     [6.55991, 2.85772, -20.07902], [8.07079, 2.33921, -17.86199], [9.28531, 1.96623, -16.29294],
                     [11.51781, 1.37506, -13.25333]])
# Table 2: their fixed-inlet optimum (y_E 7.55 in, injection -34 deg, 32,881 lbf); first 9 rows = the fixed throat arc
TAB2_HTH = np.array([[-0.56069, 6.71874, -36.25027], [-0.55023, 6.71087, -37.75027], [-0.53999, 6.70272, -39.25027],
                     [-0.52996, 6.69430, -40.75027], [-0.52016, 6.68563, -42.25027], [-0.51059, 6.67670, -43.75027],
                     [-0.50125, 6.66753, -45.25027], [-0.49216, 6.65811, -46.75027], [-0.48331, 6.64846, -48.25027],
                     [-0.40216, 6.55777, -48.02999], [-0.29091, 6.43493, -47.64577], [-0.03515, 6.15846, -46.81925],
                     [0.29695, 5.81595, -44.30856], [0.99456, 5.21035, -37.84839], [2.10220, 4.45395, -31.24354],
                     [3.01742, 3.93915, -27.61354], [5.08714, 2.98654, -22.22618], [6.75042, 2.35672, -19.37574],
                     [8.85315, 1.67387, -16.70496], [11.51707, 0.95441, -13.26458]])


def hth_rao(n=20001):
    """Rao's nozzle for HTH 1971's case: (M_E, theta_E) such that eq. (8) gives p_a = 14.7 psia and x_D R_E =
    11.51781 in (x from the lip E; R_E from the mass flow through A*), with their base model p_b = 0.846 p_D/M_D^1.3."""
    from scipy.optimize import fsolve
    H = HTH
    g = H["gamma"]
    r = Rao1961(g)
    Rsi = H["R_ftlbf"] * 1.3558179483 / (0.45359237 * 5.0 / 9.0)
    Tc, Pc, mdot = H["Tc_R"] * 5.0 / 9.0, H["pc_psia"] * 6894.757293, H["mdot_lbm"] * 0.45359237
    Gam = np.sqrt(g) * (2.0 / (g + 1.0)) ** ((g + 1.0) / (2.0 * (g - 1.0)))
    A_in2 = mdot * np.sqrt(Rsi * Tc) / (Pc * Gam) / 0.0254 ** 2
    pa = H["pa_psia"] / H["pc_psia"]
    pbm = lambda p, M: 0.846 * p / M ** 1.3            # noqa: E731

    def sol(z):
        m = r.member(z[0], z[1], n=n, pb_model=pbm)
        return m, np.sqrt(m["eps"] * A_in2 / np.pi)

    def res(z):
        m, RE = sol(z)
        return [m["p_a"] / pa - 1.0, m["x_D"] * RE / H["x_D_in"] - 1.0]
    z = fsolve(res, [2.5, -10.0], xtol=1e-12)
    m, RE = sol(z)
    m.update(M_E=float(z[0]), th_E=float(z[1]), R_E_in=float(RE), A_star_in2=float(A_in2),
             thrust_lbf=float((m["F"] - np.pi * pa) * H["pc_psia"] * RE ** 2))
    return m
