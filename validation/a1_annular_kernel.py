"""The annular throat kernel [F3/A1, S32]: Dutton & Addy's series for the
transonic flow in the throat of an annular, inclined nozzle, DERIVED to
the third order in our own hands (the paper gives the framework, its
boundary conditions and its reductions; the coefficients are in a
report that cannot be obtained), exact in the stretched axial variable
and spectral in the cross-throat coordinate.

THE SOURCE. Dutton, J. C. & Addy, A. L., "Transonic flow in the throat
region of annular supersonic nozzles", AIAA J. 20(9) 1236-1243 (1982),
GENO/literature/dutton1982.pdf. Frame = OURS (Fig. 1): x along the
mean flow direction at the throat, y across, along the minimum-area
section, the axis of symmetry at y = 0 (y is the radius when the
inclination beta is zero), lengths in the wall separation d,
velocities in a*; inner wall y = g(x) (y_i at the throat), outer
y = h(x) (y_o = y_i + 1). Expansion parameter eps = 1/(R_c + eta),
R_c = 2/(h''(0) - g''(0)), eta free (Kliegel-Levine's device for small
radii; the paper recommends eta = 2 at third order); stretched axial
coordinate z = x / (K eps^(1/2)), K = ((gamma+1)/2)^(1/2); the wall
parameters g_1 = g'(0)/(K eps^(3/2)), g_2 = 2g''(0)/(h''(0)-g''(0)) and
h_1, h_2 alike (h_2 - g_2 = 2 identically), beta_1 = tan(beta)/(K
eps^(3/2)); the series (20)-(21):
    u/a* = 1 + eps u_1 + eps^2 u_2 + eps^3 u_3
    v/a* = K [eps^(3/2) v_1 + eps^(5/2) v_2 + eps^(7/2) v_3].

THE DERIVATION (sympy, system python, 2026-09-21; the pinned venv has
no sympy; the derivation script is filed as
validation/_annular_kernel/derive_fn_sympy.py.txt and its output is
what is coded here). Eq. (11) expanded with (19)-(21): at each order n,
irrotationality (22) u_n,y = v_n,z and
    -2 u_1 u_n,z - 2 u_1,z u_n + v_n,y + v_n / y = f_n,
f_1 = -beta_1 / y (eq. (23) reproduced exactly), f_2 and f_3 the
lower-order products listed in _f2 and _f3 below (the (y + x tan beta)
denominator and the a^2/a*^2 factor of the source expanded; f_3
carries the beta_1^2 z / y^2 and beta_1 z v_1 / y^2 terms). The wall
conditions (25)-(30) are the paper's, transcribed. THE SOLUTION: the
first order is Hall's structure with the annular constant, u_1 = D z +
a(y), a' = D^2 y + C_1 / y (the z^2 wall condition forces the
z-coefficient of u_1 to be constant), D^2 and C_1 from the two wall
values of the z-coefficient of v_1 -- D^2 = 2 on the axis (Sauer
axisymmetric), 1 in the planar limit (Moore); every higher order is
LINEAR: with u_n = sum_k z^k A_k(y), v_n = sum_k z^k B_k(y), the z^k
coefficient of the operator gives (y B_k)' = y [F_k + 2 D (k+1) A_k +
2 a (k+1) A_{k+1}] and A_k' = (k+1) B_{k+1}: a triangular chain of
QUADRATURES in y from the top degree down, each pair of constants
(A_k's, B_k's) fixed by the two wall values of B_k. The y-dependence
(polynomials, logarithms from the annular constant) is carried on a
Chebyshev-Lobatto grid with spectral differentiation/integration
(N_CHEB nodes): exact in z, spectral in y, no closed-form explosion.

THE GATES (stage verify): V-1 the residual of the FULL equations
(10)-(11), evaluated with jax on the truncated series at random
points, falls with eps at the observed order of the first omitted
term (1, 2, 3 terms -> orders 1, 2, 3 on the ladder) -- a transcription
error in f_2 or f_3 breaks the third-order scaling; V-2 the wall
conditions (12)-(13) hold on both walls at the same orders; V-3 the
axis limit y_i -> 0 at first order is the record's Sauer (a1_thrust
_functional.ivl_flux, delta = 1): the sonic line and the v = 0 line;
V-4 the planar limit y_i -> 1000 (Dutton's own footnote) to the THIRD
order is Moore's asymmetric solution as transcribed and verified in
a1_throat_kernel [X-TKRN], for K = 0, 0.5, 1 -- a known answer at
every order; V-5 Chebyshev convergence (N and 2N agree to round-off).

Usage:
    python validation/a1_annular_kernel.py             # stage verify
"""
import os
import sys
import time

import numpy as np
from numpy.polynomial import chebyshev as C

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1                        # noqa: E402,F401  (x64)
import a1_throat_kernel as TK                          # noqa: E402
import jax                                             # noqa: E402
import jax.numpy as jnp                                # noqa: E402

NPASS = [0, 0]
N_CHEB = int(os.environ.get("ANK_NCHEB", 48))
HERE = os.path.dirname(os.path.abspath(__file__))
import json                                            # noqa: E402
CASES = {k: v["value"] for k, v in json.load(
    open(os.path.join(HERE, "annular_kernel_cases.json"))).items() if k[0] != "_"}


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


# ======================================================================
# the field algebra: polynomial in z, Chebyshev in y on [y_i, y_o]
# ======================================================================
class Grid:
    def __init__(self, y_i, y_o, N=N_CHEB):
        self.y_i, self.y_o, self.N = float(y_i), float(y_o), int(N)
        self.t = np.cos(np.pi * np.arange(N) / (N - 1))          # Lobatto, 1 -> -1
        self.half = 0.5 * (self.y_o - self.y_i)
        self.mid = 0.5 * (self.y_o + self.y_i)
        self.y = self.mid + self.half * self.t
        self.V = C.chebvander(self.t, N - 1)                     # values = V @ coef
        self.Vinv = np.linalg.inv(self.V)

    def coef(self, vals):
        return self.Vinv @ vals

    def vals(self, coef):
        return self.V @ coef

    def dy(self, vals):
        c = C.chebder(self.coef(vals)) / self.half
        return C.chebval(self.t, c)

    def integ_from_yi(self, vals):
        """int_{y_i}^{y} vals ds on the grid."""
        c = C.chebint(self.coef(vals)) * self.half
        out = C.chebval(self.t, c)
        return out - C.chebval(-1.0, c)


class ZY:
    """sum_k z^k c[k](y), c an array (K+1, N) of grid values."""
    def __init__(self, grid, c):
        self.g, self.c = grid, np.asarray(c, float)

    @classmethod
    def const(cls, grid, val):
        return cls(grid, np.asarray(val, float)[None, :] * np.ones((1, grid.N)))

    @classmethod
    def zpow(cls, grid, k):
        c = np.zeros((k + 1, grid.N)); c[k] = 1.0
        return cls(grid, c)

    def _pad(self, other):
        K = max(self.c.shape[0], other.c.shape[0])
        a = np.zeros((K, self.g.N)); a[:self.c.shape[0]] = self.c
        b = np.zeros((K, self.g.N)); b[:other.c.shape[0]] = other.c
        return a, b

    def __add__(self, o):
        if not isinstance(o, ZY):
            o = ZY.const(self.g, np.full(self.g.N, float(o)))
        a, b = self._pad(o)
        return ZY(self.g, a + b)
    __radd__ = __add__

    def __neg__(self):
        return ZY(self.g, -self.c)

    def __sub__(self, o):
        return self + (-o)

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if isinstance(o, ZY):
            K1, K2 = self.c.shape[0], o.c.shape[0]
            out = np.zeros((K1 + K2 - 1, self.g.N))
            for i in range(K1):
                for j in range(K2):
                    out[i + j] += self.c[i] * o.c[j]
            return ZY(self.g, out)
        return ZY(self.g, self.c * float(o))
    __rmul__ = __mul__

    def dz(self):
        if self.c.shape[0] == 1:
            return ZY(self.g, np.zeros((1, self.g.N)))
        return ZY(self.g, self.c[1:] * np.arange(1, self.c.shape[0])[:, None])

    def dy(self):
        return ZY(self.g, np.stack([self.g.dy(r) for r in self.c]))

    def over_y(self):
        return ZY(self.g, self.c / self.g.y[None, :])

    def at(self, z, y):
        """evaluate at scalar/array z, y (y inside [y_i, y_o])."""
        t = (np.asarray(y, float) - self.g.mid) / self.g.half
        rows = np.stack([C.chebval(t, self.g.coef(r)) for r in self.c])
        return sum(rows[k] * np.asarray(z, float) ** k for k in range(rows.shape[0]))

    def wall(self, side):
        """the z-polynomial coefficients at the inner (0 = y_i, last
        node) or outer (1 = y_o, first node) wall."""
        return self.c[:, -1] if side == 0 else self.c[:, 0]


# ======================================================================
# f_2, f_3 (sympy, see the docstring), as field algebra
# ======================================================================
def _f2(g, b1, u1, v1):
    return (b1 * g * u1.over_y() - 2.0 * b1 * u1.over_y() + g * u1 * v1.dy()
            + g * (u1 * v1).over_y() + u1 * u1 * u1.dz() - u1 * v1.dy()
            + 2.0 * v1 * u1.dy() - (u1 * v1).over_y())


def _f3(g, b1, grid, u1, v1, u2, v2):
    z = ZY.zpow(grid, 1)
    y2 = ZY.const(grid, grid.y ** 2)
    inv_y2 = ZY.const(grid, 1.0 / grid.y ** 2)
    return (0.5 * b1 * b1 * (g + 1.0) * z * inv_y2
            + 1.5 * b1 * (g - 1.0) * (u1 * u1).over_y()
            + b1 * (g - 2.0) * u2.over_y()
            + 0.5 * b1 * (g + 1.0) * (z * v1) * inv_y2
            + 0.5 * (g - 1.0) * u1 * u1 * v1.dy()
            + (g - 1.0) * u1 * v2.dy() + (g - 1.0) * u2 * v1.dy()
            + 0.5 * (g - 1.0) * v1 * v1 * u1.dz()
            + 0.5 * (g - 1.0) * (u1 * u1 * v1).over_y()
            + (g - 1.0) * (u1 * v2).over_y() + (g - 1.0) * (u2 * v1).over_y()
            + u1 * u1 * u2.dz() + 2.0 * u1 * u2 * u1.dz()
            + 2.0 * u1 * v1 * u1.dy() + 2.0 * u2 * u2.dz()
            + 2.0 * v1 * u2.dy() + 2.0 * v2 * u1.dy())


# ======================================================================
# the solver
# ======================================================================
def solve_kernel(y_i, g1, g2, h1, h2, b1, gam, eta, N=N_CHEB, order=3):
    """The series terms (u_n, v_n), n = 1..order, on the grid. The
    wall parameters as defined in the docstring (h2 - g2 = 2)."""
    assert abs((h2 - g2) - 2.0) < 1e-12, "h2 - g2 must be 2"
    grid = Grid(y_i, y_i + 1.0, N)
    y = grid.y
    # ---- first order: u1 = D z + a(y), v1 = z a'(y) + c(y)
    #      a' = D^2 y + C1 / y; wall values of a': g2 at y_i, h2 at y_o
    yi, yo = grid.y_i, grid.y_o
    M = np.array([[yi, 1.0 / yi], [yo, 1.0 / yo]])
    D2, C1 = np.linalg.solve(M, np.array([g2, h2]))
    D = np.sqrt(D2)
    ap = D2 * y + C1 / y
    a = 0.5 * D2 * y**2 + C1 * np.log(y)            # + C2, fixed below
    # (y c)' = 2 y a D - beta_1 ; c(y_i) = g1, c(y_o) = h1 fix C2 and c's constant
    # c = [I(y) + 2 D C2 (y^2 - yi^2)/2 + K3] / y, I = int_{yi}^y (2 s a0 D - b1) ds
    I = grid.integ_from_yi(2.0 * y * a * D - b1)
    # unknowns (C2, K3): c(yi) = K3 / yi = g1 ; c(yo) = [I(yo) + D C2 (yo^2 - yi^2) + K3] / yo = h1
    K3 = g1 * yi
    C2 = (h1 * yo - I[0] - K3) / (D * (yo**2 - yi**2))
    a = a + C2
    c = (I + D * C2 * (y**2 - yi**2) + K3) / y
    u1 = ZY(grid, np.stack([a, D * np.ones_like(y)]))
    v1 = ZY(grid, np.stack([c, ap]))
    fields = [(u1, v1)]
    if order == 1:
        return grid, fields, dict(D=D, C1=C1, C2=C2)
    # ---- wall polynomials (25)-(30): v_n(z, wall) as coefficients in z
    K = np.sqrt(0.5 * (gam + 1.0))

    def wall_poly(n, side):
        gg1, gg2 = (g1, g2) if side == 0 else (h1, h2)
        u1w = u1.wall(side)                       # [a_w, D]
        lin = np.array([gg1, gg2])                # g1 + g2 z
        if n == 2:
            # g2 eta z + (g1 + g2 z) u1
            p = np.polynomial.polynomial.polymul(lin, u1w)
            p = np.polynomial.polynomial.polyadd(p, np.array([0.0, gg2 * eta]))
            return p
        # n == 3: g2 eta^2 z + g2 eta z u1 + (g1 + g2 z) u2 - K^2 (g1 z + g2 z^2 / 2) v1_y|_wall
        u2w = fields[1][0].wall(side)
        v1y_w = v1.dy().wall(side)
        p = np.array([0.0, gg2 * eta**2])
        p = np.polynomial.polynomial.polyadd(p, np.polynomial.polynomial.polymul(np.array([0.0, gg2 * eta]), u1w))
        p = np.polynomial.polynomial.polyadd(p, np.polynomial.polynomial.polymul(lin, u2w))
        p = np.polynomial.polynomial.polyadd(p, -K**2 * np.polynomial.polynomial.polymul(np.array([0.0, gg1, 0.5 * gg2]), v1y_w))
        return p

    for n in range(2, order + 1):
        f = _f2(gam, b1, u1, v1) if n == 2 else _f3(gam, b1, grid, u1, v1, *fields[1])
        Kz = max(2 * n, f.c.shape[0] - 1)         # generous top degree
        F = np.zeros((Kz + 1, grid.N))
        F[:f.c.shape[0]] = f.c
        Pi, Po = wall_poly(n, 0), wall_poly(n, 1)
        Pi = np.concatenate([Pi, np.zeros(Kz + 1 - len(Pi))])
        Po = np.concatenate([Po, np.zeros(Kz + 1 - len(Po))])
        A = np.zeros((Kz + 1, grid.N))
        B = np.zeros((Kz + 1, grid.N))
        for k in range(Kz, -1, -1):
            # A_k = A_k^part + alpha_k, A_k^part' = (k+1) B_{k+1}
            Apart = grid.integ_from_yi((k + 1) * B[k + 1]) if k < Kz else np.zeros(grid.N)
            Ak1 = A[k + 1] if k < Kz else np.zeros(grid.N)
            # (y B_k)' = y [F_k + 2 D (k+1) (Apart + alpha) + 2 a (k+1) A_{k+1}]
            R0 = y * (F[k] + 2.0 * D * (k + 1) * Apart + 2.0 * a * (k + 1) * Ak1)
            I0 = grid.integ_from_yi(R0)
            Ia = grid.integ_from_yi(y * 2.0 * D * (k + 1) * np.ones(grid.N))
            # B_k = [I0 + alpha Ia + bk] / y ; B_k(yi) = Pi[k], B_k(yo) = Po[k]
            # at yi: I0 = Ia = 0 -> bk = Pi[k] yi ; at yo: (I0[0] + alpha Ia[0] + bk)/yo = Po[k]
            bk = Pi[k] * yi
            alpha = (Po[k] * yo - I0[0] - bk) / Ia[0]
            A[k] = Apart + alpha
            B[k] = (I0 + alpha * Ia + bk) / y
        fields.append((ZY(grid, A), ZY(grid, B)))
    return grid, fields, dict(D=D, C1=C1, C2=C2)


def series_uv(grid, fields, eps, gam, z, y, nterms=None):
    """u/a*, v/a* from the series at (z, y)."""
    nterms = len(fields) if nterms is None else nterms
    K = np.sqrt(0.5 * (gam + 1.0))
    u = 1.0
    v = 0.0
    for n in range(1, nterms + 1):
        un, vn = fields[n - 1]
        u = u + eps**n * un.at(z, y)
        v = v + K * eps**(n + 0.5) * vn.at(z, y)
    return u, v


# ======================================================================
# the residual of the FULL equations (jax), on the series
# ======================================================================
def residual_full(grid, fields, eps, gam, b1, nterms, zs, ys):
    """max |eq. (11)| and |eq. (10)| over the points, the series
    evaluated through jax-traceable Chebyshev sums."""
    K = np.sqrt(0.5 * (gam + 1.0))
    tanb = K * eps**1.5 * b1
    coefs = [(np.stack([grid.coef(r) for r in un.c]), np.stack([grid.coef(r) for r in vn.c]))
             for un, vn in fields[:nterms]]

    def cheb(cs, t):
        # Clenshaw for a batch of coefficient rows
        out = []
        for c in cs:
            b0, b1_ = 0.0, 0.0
            for ck in c[::-1]:
                b0, b1_ = ck + 2.0 * t * b0 - b1_, b0
            out.append(b0 - t * b1_)
        return jnp.stack(out)

    def uv(x, yy):
        z = x / (K * eps**0.5)
        t = (yy - grid.mid) / grid.half
        u, v = 1.0, 0.0
        for n, (cu, cv) in enumerate(coefs, start=1):
            ru, rv = cheb(cu, t), cheb(cv, t)
            un = sum(ru[k] * z**k for k in range(ru.shape[0]))
            vn = sum(rv[k] * z**k for k in range(rv.shape[0]))
            u = u + eps**n * un
            v = v + K * eps**(n + 0.5) * vn
        return u, v

    def eq11(x, yy):
        u, v = uv(x, yy)
        ub, vb = u - 1.0, v
        ux, uy = jax.grad(lambda a, b: uv(a, b)[0], 0)(x, yy), jax.grad(lambda a, b: uv(a, b)[0], 1)(x, yy)
        vy = jax.grad(lambda a, b: uv(a, b)[1], 1)(x, yy)
        gm = (gam - 1.0) / (gam + 1.0)
        return ((-2.0 * ub - ub**2 - gm * vb**2) * ux - 4.0 / (gam + 1.0) * (1.0 + ub) * vb * uy
                + (2.0 / (gam + 1.0) - vb**2 - 2.0 * gm * ub - gm * ub**2) * vy
                + (2.0 / (gam + 1.0) - 2.0 * gm * ub - gm * ub**2 - gm * vb**2)
                * (vb + (1.0 + ub) * tanb) / (yy + x * tanb))

    def eq10(x, yy):
        return (jax.grad(lambda a, b: uv(a, b)[0], 1)(x, yy)
                - jax.grad(lambda a, b: uv(a, b)[1], 0)(x, yy))
    r11 = np.asarray(jax.vmap(eq11)(jnp.asarray(zs * K * eps**0.5), jnp.asarray(ys)))
    r10 = np.asarray(jax.vmap(eq10)(jnp.asarray(zs * K * eps**0.5), jnp.asarray(ys)))
    return float(np.max(np.abs(r11))), float(np.max(np.abs(r10)))


def wall_residual(grid, fields, eps, gam, eta, g2, h2, g1, h1, nterms, zs):
    """|v - (1+u) g'(x)| on the inner and outer walls, the walls
    parabolic: g(x) = y_i + g'(0) x + g''(0) x^2/2 with g''(0) =
    g2 eps / (1 - eta eps), g'(0) = K eps^1.5 g1."""
    K = np.sqrt(0.5 * (gam + 1.0))
    worst = 0.0
    for side, (gg1, gg2) in ((0, (g1, g2)), (1, (h1, h2))):
        y0 = grid.y_i if side == 0 else grid.y_o
        gpp = gg2 * eps / (1.0 - eta * eps)
        gp0 = K * eps**1.5 * gg1
        x = zs * K * eps**0.5
        yw = y0 + gp0 * x + 0.5 * gpp * x**2       # outside the grid where the
        # wall curves away: the Chebyshev sums extrapolate (polynomials)
        u, v = series_uv(grid, fields, eps, gam, zs, yw, nterms)
        worst = max(worst, float(np.max(np.abs(v - u * (gp0 + gpp * x)))))
    return worst


# ======================================================================
# stage verify
# ======================================================================
def verify():
    t0 = time.time()
    print("== [F3/A1] the annular throat kernel derived: Dutton & Addy's series"
          " to the third order (stage verify) ==", flush=True)
    gam = 1.4
    rng = np.random.default_rng(1)
    zs = rng.uniform(-0.5, 0.5, 40)
    # a generic annular, inclined, asymmetric throat
    y_i, g1, g2, h1, h2, b1, eta = 0.6, 0.1, -0.6, -0.05, 1.4, 0.3, 2.0
    grid, fields, cst = solve_kernel(y_i, g1, g2, h1, h2, b1, gam, eta)
    ys = rng.uniform(grid.y_i, grid.y_o, 40)
    print("   case: y_i %.2f, g_1 %.2f g_2 %.2f h_1 %.2f h_2 %.2f beta_1 %.2f eta %.1f:"
          " D %.4f, C_1 %.4f" % (y_i, g1, g2, h1, h2, b1, eta, cst["D"], cst["C1"]))
    eps_l = np.array([0.04, 0.02, 0.01])
    worst = 0.0
    for nt in (1, 2, 3):
        r = np.array([residual_full(grid, fields, e, gam, b1, nt, zs, ys)[0] / e**1.5 for e in eps_l])
        rw = np.array([wall_residual(grid, fields, e, gam, eta, g2, h2, g1, h1, nt, zs) / e**1.5 for e in eps_l])
        o = np.log(r[:-1] / r[1:]) / np.log(2.0)
        ow = np.log(rw[:-1] / rw[1:]) / np.log(2.0)
        print("   %d term(s): |eq.(11)| / eps^1.5 = %s, order %s; wall residual / eps^1.5"
              " %s, order %s" % (nt, np.array2string(r, precision=2), np.array2string(o, precision=2),
                                 np.array2string(rw, precision=2), np.array2string(ow, precision=2)))
        worst = max(worst, abs(o.min() - nt), abs(ow.min() - nt))
    r10 = max(residual_full(grid, fields, e, gam, b1, 3, zs, ys)[1] for e in eps_l)
    check("V-1/V-2 the residual of the full equations and of the wall conditions"
          " falls at the order of the first omitted term, 1/2/3 terms -> 1/2/3"
          " (worst |order - n| %.2f <= 0.3); irrotationality %.1e" % (worst, r10),
          worst <= 0.3 and r10 <= 1e-10)
    # V-3 axis limit: first order = Sauer axisymmetric (the record's delta = 1)
    #     sonic line x_s(r) = c1 r^2 with c1 = -(gamma+1) alpha / 8, v = 0 line
    #     -(gamma+1) alpha / 8 ... in Sauer's u' = alpha x + (gamma+1) alpha^2 r^2 / 4:
    #     sonic x = -(gamma+1) alpha r^2 / 4, v = 0 on x = -(gamma+1) alpha r^2 / 8.
    #     Here (no centerbody, g'' = 0, h'' = 2 eps): in units of d = r_t.
    yi0 = CASES["axis_y_i"]
    grid0, f0, c0 = solve_kernel(yi0, 0.0, 0.0, 0.0, 2.0, 0.0, gam, 0.0, order=1)
    eps0 = 0.05
    alpha = np.sqrt(2.0 / ((gam + 1.0) * (1.0 / (2.0 * eps0))))   # R_wall = 1/(2 eps) in d units
    rr = np.linspace(0.2, 0.95, 8)
    K = np.sqrt(0.5 * (gam + 1.0))
    # sonic line: root of u = 1 in z at each r
    zs_ = []
    for r in rr:
        zz = np.linspace(-3, 3, 6001)
        u = 1.0 + eps0 * f0[0][0].at(zz, r)
        zs_.append(np.interp(1.0, u, zz))
    xs = np.array(zs_) * K * eps0**0.5
    x_sauer = -(gam + 1.0) * alpha * rr**2 / 4.0
    # Sauer's origin: sonic on the axis; ours: the throat plane -> compare shapes (difference at r -> 0)
    shift = xs[0] - x_sauer[0]
    d_sonic = float(np.max(np.abs(xs - x_sauer - shift)))
    print("   axis limit y_i %.0e, eps %.2f: D^2 %.6f (2), C_1 %.1e (0); sonic line vs Sauer"
          " (shape, after the origin shift %.4f): %.1e" % (yi0, eps0, c0["D"]**2, c0["C1"], shift, d_sonic))
    check("V-3 the axis limit at first order is the record's Sauer (D^2 = 2 to %.1e, C_1 %.1e,"
          " sonic line shape to %.1e)" % (abs(c0["D"]**2 - 2.0), abs(c0["C1"]), d_sonic),
          abs(c0["D"]**2 - 2.0) <= 3.0 * yi0 and abs(c0["C1"]) <= 3.0 * yi0**2
          and d_sonic <= 1e-3 * abs(x_sauer[-1]))
    # V-4 planar limit: y_i = 1000 (Dutton's own footnote) vs Moore [X-TKRN].
    #     Moore expands in eps_M = R_M^(-1/2) (R_M the mean radius in
    #     HALF-heights), Dutton in eps = 1/R_c (R_c in separations, eta 0):
    #     eps_M^2 = eps / 2, so Moore's third approximation (eps_M^4) is
    #     Dutton's SECOND term (eps^2), and Dutton's third term is Moore's
    #     unpublished fifth: the two-term series must agree with Moore to
    #     O(eps^3) -- the gap must fall 8x under eps / 2 -- x_M = 2 x_D,
    #     K_M = (h'' - j'')/(h'' + j''): h2 = 1 + K_M, g2 = -(1 - K_M)
    #     At y_i = 1000 the residual gap is the FIRST-order annular term
    #     C_1 ln y, O(u_1 / y_i): it must fall 4x under y_i x 4 (measured
    #     before this gate was posed: the eps^3 term of the 3-term series
    #     hid it, the 2-term gap scales as eps^1, i.e. it is first order)
    worst_ratio, worst_gap = 0.0, 0.0
    ym = np.linspace(-0.9, 0.9, 13)                     # Moore's y in half-heights
    zd = np.linspace(-0.5, 0.5, 13)
    e = 0.05
    for KM in (0.0, 0.5, 1.0):
        dv = {}
        for yi in (1000.0, 4000.0):
            gridP, fP, cP = solve_kernel(yi, 0.0, -(1.0 - KM), 0.0, 1.0 + KM, 0.0, gam, 0.0)
            epsM = np.sqrt(0.5 * e)
            xd = zd * K * e**0.5
            zm = 2.0 * xd / (np.sqrt(gam + 1.0) * epsM)
            yd = yi + 0.5 + 0.5 * ym
            uD, vD = series_uv(gridP, fP, e, gam, zd, yd, nterms=2)
            uM, vM, _, _, _ = TK.field(ym, zm, KM, epsM, gam, order=3)
            dv[yi] = max(float(np.max(np.abs(uD - np.asarray(uM)))),
                         float(np.max(np.abs(vD - np.asarray(vM)))))
        ratio = dv[1000.0] / dv[4000.0]
        worst_ratio = max(worst_ratio, abs(ratio - 4.0))
        worst_gap = max(worst_gap, dv[1000.0] / (e / 1000.0))
        print("   planar limit, K_M %.1f: |2-term series - Moore's third approximation| = %.2e"
              " at y_i 1000, %.2e at 4000 (ratio %.2f = the annular O(1/y_i) term)"
              % (KM, dv[1000.0], dv[4000.0], ratio))
    check("V-4 the planar limit reproduces Moore's asymmetric third approximation up to"
          " the annular O(1/y_i) term (ratio 4 +- 0.5 under y_i x 4, worst %.2f; gap / (eps"
          " / y_i) <= 1, worst %.2f)" % (worst_ratio, worst_gap),
          worst_ratio <= 0.5 and worst_gap <= 1.0)
    # V-5 Chebyshev convergence
    gridA, fA, _ = solve_kernel(y_i, g1, g2, h1, h2, b1, gam, eta, N=N_CHEB)
    gridB, fB, _ = solve_kernel(y_i, g1, g2, h1, h2, b1, gam, eta, N=2 * N_CHEB)
    dd = 0.0
    for (ua, va), (ub, vb) in zip(fA, fB):
        dd = max(dd, float(np.max(np.abs(ua.at(zs, ys) - ub.at(zs, ys)))),
                 float(np.max(np.abs(va.at(zs, ys) - vb.at(zs, ys)))))
    check("V-5 Chebyshev convergence: N %d vs %d agree to %.1e" % (N_CHEB, 2 * N_CHEB, dd), dd <= 1e-10)
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    return NPASS[0] == NPASS[1]


# ======================================================================
# a physical throat -> the kernel's parameters
# ======================================================================
def throat_params(R_i_m, d_m, beta_deg, rc_in_m, rc_out_m, eta, gam,
                  slope_in=0.0, slope_out=0.0):
    """Dutton's parameters from a throat of inner radius R_i (the inner
    wall's point on the minimum-area section), wall separation d,
    inclination beta of the mean flow to the axis, radii of curvature
    of the inner and outer walls at the throat (positive = the wall
    curves AWAY from the channel, the duct diverging on both sides in
    the throat's own frame; infinite = straight), and the wall slopes
    at the throat in the throat frame (zero for a minimum-area
    section normal to the flow). y_i = R_i / (d cos beta) (eqs.
    (3)-(4) with the x-y origin on the axis)."""
    beta = np.radians(beta_deg)
    gpp = -(d_m / rc_in_m) if np.isfinite(rc_in_m) else 0.0
    hpp = (d_m / rc_out_m) if np.isfinite(rc_out_m) else 0.0
    eps = (hpp - gpp) / (2.0 + eta * (hpp - gpp))
    K = np.sqrt(0.5 * (gam + 1.0))
    s3 = K * eps * np.sqrt(eps)                  # K eps^(3/2), the slope scale
    return dict(y_i=R_i_m / (d_m * np.cos(beta)), eps=eps,
                g2=2.0 * gpp / (hpp - gpp), h2=2.0 * hpp / (hpp - gpp),
                g1=slope_in / s3, h1=slope_out / s3,
                b1=np.tan(beta) / s3, R_c=2.0 / (hpp - gpp), K=K)


def sonic_line(grid, fields, eps, gam, ys, nterms=None, zspan=CASES["z_span"]):
    """z_s(y): the root of q = 1 in z nearest the throat plane, within
    the series' range |z| <= zspan (nan when there is none)."""
    zz = np.linspace(-zspan, zspan, CASES["z_scan_points"])
    out = []
    for y in ys:
        u, v = series_uv(grid, fields, eps, gam, zz, y, nterms)
        q = np.sqrt(u**2 + v**2) - 1.0
        k = np.where(q[:-1] * q[1:] <= 0.0)[0]
        if len(k) == 0:
            out.append(np.nan)
            continue
        kk = k[np.argmin(np.abs(zz[k]))]
        out.append(zz[kk] - q[kk] * (zz[kk + 1] - zz[kk]) / (q[kk + 1] - q[kk]))
    return np.array(out)


def mass_ratio(grid, fields, eps, gam, z, nterms=None, n=CASES["n_y_mass"]):
    """W / W* through the transverse line z = const: the y-weighted
    (radius) average of rho u / (rho* a*), against the choked 1-D value."""
    y = np.linspace(grid.y_i, grid.y_o, n)
    u, v = series_uv(grid, fields, eps, gam, np.full(n, z), y, nterms)
    q2 = u**2 + v**2
    f = u * (0.5 * (gam + 1.0) - 0.5 * (gam - 1.0) * q2) ** (1.0 / (gam - 1.0))
    return float(np.trapezoid(f * y, y) / np.trapezoid(y, y))


# ======================================================================
# stage chutkey: the primary nozzle of Chutkey 2014 (p. 479), explicit
# ======================================================================
def chutkey():
    t0 = time.time()
    print("== [F3/A1] the annular kernel on Chutkey's primary nozzle (stage chutkey) ==",
          flush=True)
    import a1_chutkey_twin as CT
    d_m, beta, rc = CT.H_T, CT.TILT_DEG, CASES["chutkey_primary_arc_radius_m"]
    R_i = CT.FOOT[1]                                     # the plug-side throat point
    gam = CT.GAMMA
    eta = float(os.environ.get("ANK_ETA", 2.0))
    P = throat_params(R_i, d_m, beta, rc, rc, eta, gam)
    print("   throat: d %.3f mm, beta %.1f deg, arcs R %.3f mm both walls -> R_c %.4f"
          " (separations), eta %.1f, eps %.4f, y_i %.2f, beta_1 %.3f (beta_1/y_i %.3f),"
          " g_2 %.1f h_2 %.1f" % (d_m * 1e3, beta, rc * 1e3, P["R_c"], eta, P["eps"],
                                  P["y_i"], P["b1"], P["b1"] / P["y_i"], P["g2"], P["h2"]))
    grid, fields, cst = solve_kernel(P["y_i"], P["g1"], P["g2"], P["h1"], P["h2"],
                                     P["b1"], gam, eta)
    eps, K = P["eps"], P["K"]
    NY = CASES["n_y_profile"]
    ys = np.linspace(grid.y_i, grid.y_o, NY)
    print("   the sonic line x_s (in d) at the plug wall / mid / lip wall, the throat-plane"
          " (x = 0) Mach and direction, and the mass, by number of terms:")
    rows = {}
    for nt in (1, 2, 3):
        zs = sonic_line(grid, fields, eps, gam, ys, nt)
        xs = zs * K * eps**0.5
        u0, v0 = series_uv(grid, fields, eps, gam, np.zeros(NY), ys, nt)
        M0 = np.sqrt(u0**2 + v0**2) / np.sqrt(0.5 * (gam + 1.0) - 0.5 * (gam - 1.0) * (u0**2 + v0**2))
        th0 = np.degrees(np.arctan2(v0, u0))
        W0 = mass_ratio(grid, fields, eps, gam, 0.0, nt)
        rows[nt] = dict(xs=xs, M0=M0, th0=th0, W0=W0)
        print("     %d term(s): x_s %+.4f / %+.4f / %+.4f d; M(x=0) %.4f..%.4f; theta(x=0)"
              " %+.2f..%+.2f deg; W/W* through x = 0: %.5f"
              % (nt, xs[0], xs[NY // 2], xs[-1], M0.min(), M0.max(), th0.min(), th0.max(), W0))
    d12 = float(np.max(np.abs(rows[2]["M0"] - rows[1]["M0"])))
    d23 = float(np.max(np.abs(rows[3]["M0"] - rows[2]["M0"])))
    print("   throat-plane Mach convergence: max |M_2 - M_1| %.4f, |M_3 - M_2| %.4f (ratio %.2f)"
          % (d12, d23, d12 / d23))
    # the re-summation parameter: at a given order the answer must not
    # depend on eta beyond the truncation error
    M_eta = {}
    for eta2 in CASES["eta_ladder"]:
        P2 = throat_params(R_i, d_m, beta, rc, rc, eta2, gam)
        g2_, f2_, _ = solve_kernel(P2["y_i"], P2["g1"], P2["g2"], P2["h1"], P2["h2"], P2["b1"], gam, eta2)
        u0, v0 = series_uv(g2_, f2_, P2["eps"], gam, np.zeros(NY), ys, 3)
        M_eta[eta2] = np.sqrt(u0**2 + v0**2) / np.sqrt(0.5 * (gam + 1.0) - 0.5 * (gam - 1.0) * (u0**2 + v0**2))
        print("   eta %.0f (eps %.3f): 3-term M(x=0) %.4f..%.4f, W/W* %.5f"
              % (eta2, P2["eps"], M_eta[eta2].min(), M_eta[eta2].max(),
                 mass_ratio(g2_, f2_, P2["eps"], gam, 0.0, 3)))
    d_eta = float(max(np.max(np.abs(M_eta[1.0] - M_eta[2.0])), np.max(np.abs(M_eta[3.0] - M_eta[2.0]))))
    check("C-1 the series converges on the throat-plane Mach at R_c %.2f (eta %.0f): the third"
          " term moves it less than the second (%.4f < %.4f), and eta 1/3 vs 2 move it by no more"
          " than the third term (%.4f)" % (P["R_c"], eta, d23, d12, d_eta),
          d23 < d12 and d_eta <= 2.0 * d23)
    # the first all-supersonic transverse line and its state
    zs3 = sonic_line(grid, fields, eps, gam, ys, 3)
    zl = float(np.nanmax(zs3))
    ul, vl = series_uv(grid, fields, eps, gam, np.full(NY, zl), ys, 3)
    Ml = np.sqrt(ul**2 + vl**2) / np.sqrt(0.5 * (gam + 1.0) - 0.5 * (gam - 1.0) * (ul**2 + vl**2))
    print("   first all-supersonic transverse line: x %+.4f d = %+.3f mm from the throat plane;"
          " M %.4f..%.4f, theta %+.2f..%+.2f deg; W/W* %.5f"
          % (zl * K * eps**0.5, zl * K * eps**0.5 * d_m * 1e3, Ml.min(), Ml.max(),
             np.degrees(np.arctan2(vl, ul)).min(), np.degrees(np.arctan2(vl, ul)).max(),
             mass_ratio(grid, fields, eps, gam, zl, 3)))
    lo, hi = CASES["discharge_band"]
    check("C-2 the mass through the throat plane is below the choked 1-D value and above"
          " %.2f of it (W/W* %.5f)" % (lo, rows[3]["W0"]), lo <= rows[3]["W0"] <= hi)
    os.makedirs(os.path.join(HERE, "_annular_kernel"), exist_ok=True)
    np.savez(os.path.join(HERE, "_annular_kernel", "chutkey_eta%.1f.npz" % eta),
             ys=ys, **{"xs%d" % k: rows[k]["xs"] for k in rows},
             **{"M0_%d" % k: rows[k]["M0"] for k in rows}, params=np.array([P[k] for k in ("y_i", "eps", "g2", "h2", "b1")]))
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    return NPASS[0] == NPASS[1]


# ======================================================================
# stage domain: where the series converges -- the throat-plane Mach
# convergence ratio and the eta-spread against R_c, on Chutkey's
# annulus (y_i 21, beta 56.9 deg, symmetric walls) and on the axis
# ======================================================================
def domain():
    t0 = time.time()
    print("== [F3/A1] the annular kernel's convergence domain (stage domain) ==", flush=True)
    import a1_chutkey_twin as CT
    gam = CT.GAMMA
    NY = CASES["n_y_profile"]
    ys = np.linspace(0.0, 1.0, NY)
    ok = True
    for label, (R_i, beta) in (("Chutkey annulus (y_i 21, beta 56.9)", (CT.FOOT[1], CT.TILT_DEG)),
                               ("axis (y_i %.0e, beta 0)" % CASES["axis_y_i"], (CASES["axis_y_i"] * CT.H_T, 0.0))):
        print("   " + label)
        for R_c in CASES["rc_ladder"]:
            rc = R_c * CT.H_T
            res = {}
            for eta in CASES["eta_ladder"]:
                P = throat_params(R_i, CT.H_T, beta, rc, rc, eta, gam)
                grid, fields, _ = solve_kernel(P["y_i"], P["g1"], P["g2"], P["h1"], P["h2"], P["b1"], gam, eta)
                yy = grid.y_i + ys
                Ms = []
                for nt in (1, 2, 3):
                    u0, v0 = series_uv(grid, fields, P["eps"], gam, np.zeros(NY), yy, nt)
                    Ms.append(np.sqrt(u0**2 + v0**2) / np.sqrt(0.5 * (gam + 1.0) - 0.5 * (gam - 1.0) * (u0**2 + v0**2)))
                res[eta] = dict(eps=P["eps"], M=Ms, W=mass_ratio(grid, fields, P["eps"], gam, 0.0, 3))
            d12 = float(np.max(np.abs(res[2.0]["M"][1] - res[2.0]["M"][0])))
            d23 = float(np.max(np.abs(res[2.0]["M"][2] - res[2.0]["M"][1])))
            d_eta = float(max(np.max(np.abs(res[1.0]["M"][2] - res[2.0]["M"][2])),
                              np.max(np.abs(res[3.0]["M"][2] - res[2.0]["M"][2]))))
            conv = d23 < d12 and d_eta <= 2.0 * d23
            print("     R_c %.3f: eps(eta 2) %.3f; M(x=0) 3 terms %.4f..%.4f; |M2-M1| %.4f |M3-M2| %.4f"
                  " (ratio %.2f); eta-spread %.4f; W/W* %.5f (eta 1/2/3: %.5f/%.5f/%.5f) -> %s"
                  % (R_c, res[2.0]["eps"], res[2.0]["M"][2].min(), res[2.0]["M"][2].max(), d12, d23,
                     d23 / d12, d_eta, res[2.0]["W"], res[1.0]["W"], res[2.0]["W"], res[3.0]["W"],
                     "converges" if conv else "NOT converged"))
            if R_c >= CASES["rc_converged_from"] and not conv:
                ok = False
    check("D-1 the series converges (third term < second, eta-spread <= 2 x third term) at"
          " R_c >= %.1f on both the annulus and the axis" % CASES["rc_converged_from"], ok)
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    return NPASS[0] == NPASS[1]


STAGE = os.environ.get("ANK_STAGE", "verify")

if __name__ == "__main__":
    sys.exit(0 if {"verify": verify, "chutkey": chutkey,
                   "domain": domain}.get(STAGE, verify)() else 1)
