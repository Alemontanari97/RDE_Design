"""The throat kernel of the plug [F3/A1, S32]: Moore's transonic solution
for the asymmetric two-dimensional throat, transcribed and VERIFIED.

WHY. The S31 twins left one defect with one cause: the near-lip flow
of the plug is DECLARED, not computed. On Chutkey's contour the march
loses 6.2 percent of the mass once, in the first column (the ideal
fan's cut data read on a non-ideal wall); on Humphreys' optimum the
first knot sits +0.34 in off Table 2 with y_w0 frozen by the mass
constraint; and Humphreys himself measured the stake (1971 p. 1587,
"Importance of start line"): Rao's straight sonic line with uniform
flow direction gives compression unless M >= 1.5 on it, a linear 6 deg
variation of the direction along the line cures it but leaves the
thrust 2700 lbf (8 percent) low, and a right-running characteristic
taken from the transonic field reproduces Rao's contour and thrust to
2 lbf. The start line is the whole difference. What replaces the
declaration is the transonic field in the throat computed ON the
contour: this file is its first brick.

THE SOURCE. Moore, A. W., "The transonic flow in the throat region of
a two-dimensional nozzle with walls of arbitrary smooth profile",
ARC R&M 3481 (1965, publ. 1967), reports.aerade.cranfield.ac.uk
handle 1826.2/4059 -- Hall's method of successive approximation
generalised to walls of DIFFERENT curvature (the mean radius R and the
asymmetry K), the series in eps = R^(-1/2), first three terms. Its
annular (axisymmetric) sequel, Moore & Hall, ARC 26-543 (1965), is
the "Moore-Hall start line" of Humphreys 1971 and is NOT in hand;
nor is Dutton & Addy, AIAA J. 20(9) 1236-1243 (1982), the general
axisymmetric/planar/annular series (both behind paywalls 2026-09-21,
DTIC ADA084787 unreachable). What is in hand is exact for the PLANAR
throat and is the structure of the annular one.

WHAT IS TRANSCRIBED (Moore's notation; unit of length = throat
half-height, origin in the throat plane, y from the lower wall j = -1
to the upper wall h = +1, the walls parabolic to this order:
h'' = (1+K)/R, j'' = (1-K)/R, 1/R = (h''+j'')/2, K = (h''-j'')/(h''+j'');
x = (gamma+1)^(1/2) eps z; u/a* = 1 + u', v/a* = v';
u' = eps^2 u1 + eps^4 u3, v' = (gamma+1)^(1/2)(eps^3 v1 + eps^5 v3);
the eps^3/eps^4 terms u2, v2 vanish for parabolic walls, l3 = m3 = 0,
and the quartic wall terms l4, m4 are O(R^-2) for circular arcs and
dropped, as the paper says circular, hyperbolic and parabolic arcs are
equivalent unless O(R^-3) is kept):
  eq. (2.32)-(2.33)  u1 = u1s + u1K, v1 = v1s + v1K        (page 7)
  eq. (2.36)         u3 = u3s + u3K, v3 = v3s + v3K        (page 8)
  eq. (4.4)          the isobars / sonic line to O(eps^2)  (page 11-12)
  eq. (4.6)          1 - W/W* the mass defect               (page 12)
  section 4.3        K = 1 is the straight-wall channel     (page 14)
Page 5 of the scan (definitions (2.6)-(2.15)) is BLANK in the archive
copy: the definitions of R, K above are reconstructed from the
boundary conditions (2.30)-(2.31) and confirmed by section 4.3 (a
straight wall gives K = 1) -- declared, not read.

HOW IT IS VERIFIED (the paper is its own rejector). The transcription
was checked SYMBOLICALLY (sympy, 2026-09-21, exact rationals) against
the paper's own equations: irrotationality (2.23) and continuity
(2.24) at first order, (2.25) with Phi_2 at third order (Phi_2
re-derived from (2.17) and agreeing with the print up to the
irrotationality identity), the wall conditions (2.30)-(2.31), and the
sonic-line formula (4.4) to O(eps^4): all residuals are IDENTICALLY
ZERO after ONE misprint of the scan was corrected (v3K's z-linear
constant reads (2 gamma+8)/8 in the image and must be (2 gamma+8)/3:
irrotationality fails by K(5 gamma/12 + 5/3) otherwise). The same
tests run here NUMERICALLY with jax derivatives (stage verify), plus
the known answers: at K = 0 the first approximation IS the record's
Sauer (a1_thrust_functional.ivl_flux, delta = 0) up to the origin
shift 1/6 -- sonic line z = 1/6 - y^2/2, the v = 0 line z = 1/6 -
y^2/6 -- and at K = 1 (one wall straight, the choked wind tunnel of
section 4.3) the sonic points are z = -4/3 on the curved wall and
z = +2/3 on the straight one, the singular point y = -K sitting ON
the straight wall; the mass defect (4.6) is reproduced by quadrature.

WHAT THIS IS NOT YET. Not axisymmetric (the annular mean-radius terms
of Moore-Hall / Dutton-Addy are the gap), not a start line for the
march (the frame is the throat's own -- tilted by theta_t in the plug
-- and the hand-over to the x-march in the record's frame is the next
brick, POSING_2026-09-21_throat_kernel.md), not a corner treatment
(the cowl lip is where the smooth wall ENDS; Moore's field is valid up
to it and the lip fan starts from the field's state there).

Usage:
    python validation/a1_throat_kernel.py            # stage verify
    TK_STAGE=startline python validation/a1_throat_kernel.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1                        # noqa: E402,F401  (x64)
import jax                                             # noqa: E402
import jax.numpy as jnp                                # noqa: E402

NPASS = [0, 0]
HERE = os.path.dirname(os.path.abspath(__file__))


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


# ======================================================================
# Moore (1965) R&M 3481: the series terms, transcribed
# ======================================================================
def u1_(y, z, K, g):
    """(2.32): u1s + u1K."""
    return 0.5 * y**2 - 1.0 / 6.0 + z + K * y


def v1_(y, z, K, g):
    """(2.33): v1s + v1K."""
    return y**3 / 6.0 - y / 6.0 + y * z + K * (0.5 * y**2 - 0.5 + z)


def u3_(y, z, K, g):
    """(2.36): u3s + u3K (l3 = m3 = l4 = m4 = 0)."""
    u3s = ((g + 6.0) / 18.0 * y**4 - (2.0 * g + 9.0) / 18.0 * y**2
           + (g + 30.0) / 270.0 + z * (y**2 - 0.5)
           - (2.0 * g - 3.0) / 6.0 * z**2)
    u3K = (K * ((2.0 * g + 12.0) / 9.0 * y**3 - (2.0 * g + 8.0) / 3.0 * y
                + 2.0 * y * z)
           + K**2 * (0.5 * y**2 - g / 3.0 - 0.5 * z))
    return u3s + u3K


def v3_(y, z, K, g):
    """(2.36): v3s + v3K; the (2 gamma+8)/3 constant is the corrected
    misprint (see the module docstring)."""
    v3s = ((22.0 * g + 75.0) / 360.0 * y**5 - (5.0 * g + 21.0) / 54.0 * y**3
           + (34.0 * g + 195.0) / 1080.0 * y
           + z * ((2.0 * g + 12.0) / 9.0 * y**3 - (2.0 * g + 9.0) / 9.0 * y)
           + y * z**2)
    v3K = (K * ((22.0 * g + 75.0) / 72.0 * y**4 - (3.0 * g + 14.0) / 6.0 * y**2
                + (14.0 * g + 93.0) / 72.0
                + z * ((2.0 * g + 12.0) / 3.0 * y**2 - (2.0 * g + 8.0) / 3.0)
                + z**2)
           + K**2 * ((4.0 * g + 11.0) / 12.0 * y**3
                     - (4.0 * g + 11.0) / 12.0 * y + z * y)
           - K**3 * (0.25 * y**2 - 0.25))
    return v3s + v3K


def phi2_(y, z, K, g):
    """Phi_2 of (2.25)/(2.27) as RE-DERIVED from (2.17) at O(eps^5)
    (u2 = 0): 2 v1 u1_y + (gamma-1) u1 v1_y + u1^2 u1_z / 2."""
    u1 = u1_(y, z, K, g)
    v1 = v1_(y, z, K, g)
    u1y = jax.grad(u1_, 0)(y, z, K, g)
    u1z = jax.grad(u1_, 1)(y, z, K, g)
    v1y = jax.grad(v1_, 0)(y, z, K, g)
    return 2.0 * v1 * u1y + (g - 1.0) * u1 * v1y + 0.5 * u1**2 * u1z


def sonic_z44(y, K, eps, g):
    """(4.4) with Q = 0: the sonic line z_s(y) to O(eps^2)."""
    return (-0.5 * y**2 + 1.0 / 6.0 - K * y
            + eps**2 * ((2.0 * g + 3.0) / 72.0 * y**4 + (g + 3.0) / 18.0 * y**2
                        + (2.0 * g - 15.0) / 360.0
                        + K * ((2.0 * g + 3.0) / 18.0 * y**3
                               + (5.0 * g + 18.0) / 9.0 * y)
                        + K**2 * ((4.0 * g + 9.0) / 12.0 * y**2
                                  + (4.0 * g + 1.0) / 12.0)
                        - 0.5 * K**3 * y))


def mass_defect46(K, eps, g):
    """(4.6): 1 - W/W* to O(eps^6)."""
    return (g + 1.0) * eps**4 * (1.0 / 90.0 - (2.0 * g + 9.0) / 945.0 * eps**2
                                 + K**2 * (1.0 / 6.0
                                           - (2.0 * g + 9.0) / 15.0 * eps**2))


# ======================================================================
# the field
# ======================================================================
def throat_params(c_h, c_j):
    """R, K, eps from the two wall curvatures at the throat in units of
    the throat half-height (c = half-height / radius of curvature,
    positive for a wall curving AWAY from the channel, i.e. h'' = c_h,
    j'' = c_j). A straight wall has c = 0 -> K = +-1."""
    inv_R = 0.5 * (c_h + c_j)
    K = (c_h - c_j) / (c_h + c_j)
    return 1.0 / inv_R, K, np.sqrt(inv_R)


def field(y, z, K, eps, g, order=3):
    """u/a*, v/a*, q/a*, theta, M at (y, z) from the series to the
    given order (1 or 3). Exact M from q/a* (not the series (3.3))."""
    y = jnp.asarray(y, float)
    z = jnp.asarray(z, float)
    up = eps**2 * u1_(y, z, K, g)
    vp = eps**3 * v1_(y, z, K, g)
    if order >= 3:
        up = up + eps**4 * u3_(y, z, K, g)
        vp = vp + eps**5 * v3_(y, z, K, g)
    ub = 1.0 + up
    vb = jnp.sqrt(g + 1.0) * vp
    qb = jnp.sqrt(ub**2 + vb**2)
    th = jnp.arctan2(vb, ub)
    M = qb / jnp.sqrt(0.5 * (g + 1.0) - 0.5 * (g - 1.0) * qb**2)
    return ub, vb, qb, th, M


def x_of_z(z, eps, g):
    """(2.20): the physical abscissa in half-heights."""
    return np.sqrt(g + 1.0) * eps * np.asarray(z, float)


def sonic_line(y, K, eps, g, order=3):
    """z_s(y): the root of q/a* = 1 in z, Newton from (4.4)."""
    y = np.atleast_1d(np.asarray(y, float))
    z = np.asarray(sonic_z44(y, K, eps, g), float)

    def f(zz, yy):
        return field(yy, zz, K, eps, g, order)[2] - 1.0
    df = jax.vmap(jax.grad(f, 0))
    for _ in range(12):
        r = np.asarray(jax.vmap(f)(jnp.asarray(z), jnp.asarray(y)))
        d = np.asarray(df(jnp.asarray(z), jnp.asarray(y)))
        z = z - r / d
        if np.max(np.abs(r)) < 1e-14:
            break
    return z


def mass_flow_ratio(K, eps, g, n=2001, order=3):
    """W/W* at the throat plane z = 0 by Simpson quadrature of
    rho u / (rho* a*) = ub [ (g+1)/2 - (g-1)/2 qb^2 ]^(1/(g-1))."""
    y = np.linspace(-1.0, 1.0, n)
    ub, vb, qb, _, _ = field(y, np.zeros(n), K, eps, g, order)
    f = np.asarray(ub * (0.5 * (g + 1.0) - 0.5 * (g - 1.0) * qb**2)
                   ** (1.0 / (g - 1.0)))
    w = np.ones(n)
    w[1:-1:2], w[2:-1:2] = 4.0, 2.0
    return float(np.sum(w * f) * (y[1] - y[0]) / 3.0) / 2.0


# ======================================================================
# the start line (stage startline): the first brick of the posing,
# section 5 of the S32 log
# ======================================================================
def start_line(c_h, c_j, g, n=81, margin=None, order=3):
    """The kernel's start line in the THROAT frame: the transverse line
    z = z_line = max_y z_s(y) + margin (the first z = const line on
    which every point is supersonic, plus a margin in stretched z;
    default = 2 percent of the sonic line's own spread), sampled
    at n points from the lower wall (y = -1, the cowl when c_j = 0) to
    the upper (the plug). Returns a dict with x, y (half-heights), q/a*,
    theta (rad, in the throat frame), M, the mass ratio W/W* through the
    line and through z = 0, and the kernel's parameters."""
    R, K, eps = throat_params(c_h, c_j)
    y = np.linspace(-1.0, 1.0, n)
    zs = sonic_line(y, K, eps, g, order)
    spread = float(zs.max() - zs.min())
    zl = float(zs.max()) + (0.02 * spread if margin is None else float(margin))
    ub, vb, qb, th, M = field(y, np.full(n, zl), K, eps, g, order)
    return dict(R=R, K=K, eps=eps, z_line=zl, x_line=x_of_z(zl, eps, g),
                y=y, x=np.full(n, x_of_z(zl, eps, g)),
                q=np.asarray(qb), theta=np.asarray(th), M=np.asarray(M),
                z_sonic=zs, x_sonic=x_of_z(zs, eps, g),
                W_line=_mass_on_line(y, zl, K, eps, g, order),
                W_throat=mass_flow_ratio(K, eps, g, n=2001, order=order))


def _mass_on_line(y, zl, K, eps, g, order):
    """W/W* through the z = zl transverse line (u is the normal
    component there), Simpson on the given odd-n sampling."""
    n = len(y)
    ub, vb, qb, _, _ = field(y, np.full(n, zl), K, eps, g, order)
    f = np.asarray(ub * (0.5 * (g + 1.0) - 0.5 * (g - 1.0) * qb**2)
                   ** (1.0 / (g - 1.0)))
    w = np.ones(n)
    w[1:-1:2], w[2:-1:2] = 4.0, 2.0
    return float(np.sum(w * f) * (y[1] - y[0]) / 3.0) / 2.0


def rotate_to_record(sl, theta_t, y_lip, h_half):
    """The start line in the RECORD's frame (x along the nozzle axis,
    y the radius): the throat frame is rotated by theta_t (the mean
    flow direction at the throat, negative toward the axis) and scaled
    by the half-height h_half, with the lower wall's line point (y = -1
    in the throat frame) placed at the lip (0, y_lip). Angles: theta
    in the record's frame = theta_t + theta_throat."""
    ct, st = np.cos(theta_t), np.sin(theta_t)
    xt = sl["x"] * h_half
    yt = (sl["y"] + 1.0) * h_half          # 0 at the lower wall
    # throat-frame axes: e_x = (ct, st), e_y = (-st, ct) in the record
    X = xt * ct - yt * st
    Y = y_lip + xt * st + yt * ct
    return dict(x=X, y=Y, q=sl["q"], theta=theta_t + sl["theta"], M=sl["M"])


def startline():
    t0 = time.time()
    print("== [F3/A1] throat kernel: the start line in the throat frame"
          " (stage startline) ==", flush=True)
    g = 1.4
    worst_m = 0.0
    gaps = {0.0: [], 0.5: []}
    for c_h in (0.4, 0.2, 0.1):                     # plug wall: R_w = 2.5, 5, 10 half-heights
        for f in (0.0, 0.5):                        # cowl: straight, or half the plug's
            c_j = f * c_h
            sl = start_line(c_h, c_j, g)
            mu = np.arcsin(1.0 / sl["M"])
            dm = np.diff(sl["theta"] - mu)
            gap = abs(sl["W_line"] / sl["W_throat"] - 1.0)
            worst_m = max(worst_m, float(1.0 - sl["M"].min()))
            gaps[f].append(gap)
            print("   c_h %.2f c_j %.2f (R %.2f, K %.2f, eps %.3f): line at x %+.3f"
                  " (sonic %+.3f..%+.3f); M %.4f..%.4f, theta %+.2f..%+.2f deg,"
                  " theta - mu %s; W/W* line %.6f throat %.6f (gap %.1e)"
                  % (c_h, c_j, sl["R"], sl["K"], sl["eps"], sl["x_line"],
                     sl["x_sonic"].min(), sl["x_sonic"].max(),
                     sl["M"].min(), sl["M"].max(),
                     np.degrees(sl["theta"].min()), np.degrees(sl["theta"].max()),
                     "monotone" if (np.all(dm >= 0) or np.all(dm <= 0)) else "NOT monotone",
                     sl["W_line"], sl["W_throat"], gap), flush=True)
    check("S-1 every point of every start line is supersonic (worst"
          " 1 - M_min %.1e)" % worst_m, worst_m <= 0.0)
    # the truncated series conserves mass between z = 0 and the line
    # only to its order, and the line sits 0.3-0.4 half-heights
    # downstream (K = 1: the straight wall's sonic point). The gap is
    # the kernel's DECLARED mass band; the gate is that it converges
    # with the curvature (order >= 1 on the c_h ladder 0.4/0.2/0.1,
    # i.e. it is the truncation, not a defect of the construction)
    orders = []
    for f, gl in gaps.items():
        gl = np.array(gl)
        o = np.log(gl[:-1] / gl[1:]) / np.log(2.0)
        orders.append(o.min())
        print("   cowl/plug curvature %.1f: mass gap line-vs-throat %s,"
              " observed order in c_h %s"
              % (f, np.array2string(gl, precision=2),
                 np.array2string(o, precision=2)))
    check("S-2 the line-vs-throat mass gap is the series' truncation:"
          " it converges with the curvature (worst order %.2f >= 1)"
          % min(orders), min(orders) >= 1.0)
    # the rotation: a pure isometry + scaling (lengths and the angle
    # between the line and the flow preserved)
    sl = start_line(0.2, 0.0, g)
    th_t, y_lip, hh = np.radians(-56.9), 32.0, 1.3235      # Chutkey's numbers
    rec = rotate_to_record(sl, th_t, y_lip, hh)
    L0 = np.hypot(np.diff(sl["x"]), np.diff(sl["y"])).sum() * hh
    L1 = np.hypot(np.diff(rec["x"]), np.diff(rec["y"])).sum()
    org = rotate_to_record(dict(x=np.zeros(1), y=-np.ones(1), q=None,
                                theta=np.zeros(1), M=None), th_t, y_lip, hh)
    # the line's cowl point lies x_line half-heights along the throat
    # direction from the lip
    d = np.hypot(rec["x"][0], rec["y"][0] - y_lip) / hh
    check("S-3 rotation into the record's frame: isometry (line length"
          " %.6f vs %.6f mm), the throat origin at the lip (%.1e, %.1e),"
          " the line's cowl point x_line = %.3f half-heights from it (%.3f)"
          % (L0, L1, org["x"][0], org["y"][0] - y_lip, sl["x_line"], d),
          abs(L0 - L1) <= 1e-9 * L0 and abs(org["x"][0]) <= 1e-12
          and abs(org["y"][0] - y_lip) <= 1e-12
          and abs(d - sl["x_line"]) <= 1e-12)
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    return NPASS[0] == NPASS[1]


# ======================================================================
# stage verify
# ======================================================================
def verify():
    t0 = time.time()
    print("== [F3/A1] throat kernel: Moore 1965 transcribed and verified"
          " (stage verify) ==", flush=True)
    g = 1.4
    rng = np.random.default_rng(0)
    pts = rng.uniform(-1.0, 1.0, size=(64, 3))          # y, z, K
    tol = 64 * np.finfo(float).eps

    # T-1 the PDE system at first and third order, jax derivatives
    def res1(y, z, K):
        irr = jax.grad(v1_, 1)(y, z, K, g) - jax.grad(u1_, 0)(y, z, K, g)
        con = (-u1_(y, z, K, g) * jax.grad(u1_, 1)(y, z, K, g)
               + jax.grad(v1_, 0)(y, z, K, g))
        return jnp.abs(irr) + jnp.abs(con)

    def res3(y, z, K):
        irr = jax.grad(v3_, 1)(y, z, K, g) - jax.grad(u3_, 0)(y, z, K, g)
        con = (-u1_(y, z, K, g) * jax.grad(u3_, 1)(y, z, K, g)
               - u3_(y, z, K, g) * jax.grad(u1_, 1)(y, z, K, g)
               + jax.grad(v3_, 0)(y, z, K, g) - phi2_(y, z, K, g))
        return jnp.abs(irr) + jnp.abs(con)
    r1 = float(jnp.max(jax.vmap(res1)(*[jnp.asarray(pts[:, i]) for i in range(3)])))
    r3 = float(jnp.max(jax.vmap(res3)(*[jnp.asarray(pts[:, i]) for i in range(3)])))
    check("T-1 (2.23)-(2.24) at first order: residual %.1e <= %.1e on 64"
          " random (y, z, K)" % (r1, tol), r1 <= tol)
    check("T-1 (2.23), (2.25)+Phi_2 at third order: residual %.1e <= %.1e"
          % (r3, tol), r3 <= tol)

    # T-2 the wall conditions (2.30)-(2.31), l4 = m4 = 0
    def bc(z, K):
        yp, ym = 1.0, -1.0
        a = jnp.abs(v1_(yp, z, K, g) - (1.0 + K) * z)
        b = jnp.abs(v1_(ym, z, K, g) + (1.0 - K) * z)
        c = jnp.abs(v3_(yp, z, K, g) - (1.0 + K) * z * u1_(yp, z, K, g))
        d = jnp.abs(v3_(ym, z, K, g) + (1.0 - K) * z * u1_(ym, z, K, g))
        return a + b + c + d
    rb = float(jnp.max(jax.vmap(bc)(jnp.asarray(pts[:, 1]), jnp.asarray(pts[:, 2]))))
    check("T-2 wall conditions (2.30)-(2.31) at both walls: %.1e <= %.1e"
          % (rb, tol), rb <= tol)

    # T-3 the sonic line: (4.4) vs the root of q = 1, O(eps^4) apart
    eps_l = np.array([0.1, 0.2, 0.4])
    yy = np.linspace(-1.0, 1.0, 21)
    worst = 0.0
    for K in (0.0, 0.5, 1.0):
        d = []
        for e in eps_l:
            zs = sonic_line(yy, K, e, g)
            d.append(np.max(np.abs(zs - sonic_z44(yy, K, e, g))))
        d = np.array(d)
        # the gap must scale like eps^4: ratio between consecutive
        # rungs ~ 2^4 = 16 (the rung ratio is 2)
        rate = np.log(d[1:] / d[:-1]) / np.log(2.0)
        worst = max(worst, float(np.max(np.abs(rate - 4.0))))
        print("   K %.1f: |z_s - (4.4)| = %s, observed order %s"
              % (K, np.array2string(d, precision=2),
                 np.array2string(rate, precision=2)))
    check("T-3 (4.4) is the sonic line to O(eps^4): observed order 4 +- 1"
          " (worst %.2f)" % worst, worst <= 1.0)

    # T-4 the mass defect (4.6) by quadrature
    worst = 0.0
    for K in (0.0, 0.5, 1.0):
        for e in (0.1, 0.2):
            md = 1.0 - mass_flow_ratio(K, e, g)
            md46 = mass_defect46(K, e, g)
            gap = abs(md - md46) / md46
            worst = max(worst, gap)
            print("   K %.1f eps %.1f: 1 - W/W* quadrature %.4e, (4.6) %.4e,"
                  " rel gap %.1e" % (K, e, md, md46, gap))
    # (4.6) is exact to O(eps^6); the quadrature carries the whole
    # series: the gap is O(eps^2) relative -> at eps 0.2, ~ 0.04 x C
    check("T-4 (4.6) reproduced by quadrature within 10 percent at"
          " eps <= 0.2 (worst %.1e)" % worst, worst <= 0.1)

    # T-5 K = 0 is Sauer (planar) up to the origin shift 1/6
    zs = sonic_line(yy, 0.0, 1e-3, g, order=1)
    zv = 1.0 / 6.0 - yy**2 / 6.0
    v0 = np.asarray(field(yy, zv, 0.0, 1e-3, g, order=1)[1])
    check("T-5 K = 0, first order: sonic line = 1/6 - y^2/2 (%.1e) and"
          " v = 0 on z = 1/6 - y^2/6 (%.1e) -- the record's Sauer, delta 0,"
          " shifted by 1/6" % (np.max(np.abs(zs - (1.0 / 6.0 - yy**2 / 2.0))),
                              np.max(np.abs(v0))),
          np.max(np.abs(zs - (1.0 / 6.0 - yy**2 / 2.0))) <= 1e-9
          and np.max(np.abs(v0)) <= 1e-12)

    # T-6 K = 1: one wall straight (section 4.3)
    z_curved = float(sonic_line(1.0, 1.0, 1e-3, g, order=1)[0])
    z_straight = float(sonic_line(-1.0, 1.0, 1e-3, g, order=1)[0])
    # the singular point y = -K: the sonic line is perpendicular to
    # the flow there, dz_s/dy = 0
    dz = float(jax.grad(lambda yv: sonic_z44(yv, 1.0, 0.0, g))(-1.0))
    check("T-6 K = 1 (straight lower wall): sonic point z = -4/3 on the"
          " curved wall (%.4f), +2/3 on the straight one (%.4f), singular"
          " point on the straight wall (dz_s/dy = %.1e)"
          % (z_curved, z_straight, dz),
          abs(z_curved + 4.0 / 3.0) <= 1e-9 and abs(z_straight - 2.0 / 3.0) <= 1e-9
          and abs(dz) <= 1e-12)

    # the reading, for the posing: the direction variation across a
    # straight-wall throat at the sonic line, and the M along z = const
    for R in (5.0, 10.0, 20.0):
        e = 1.0 / np.sqrt(R)
        zs = sonic_line(yy, 1.0, e, g)
        th = np.degrees(np.asarray(field(yy, zs, 1.0, e, g)[3]))
        zl = np.full_like(yy, float(np.max(zs)))
        M = np.asarray(field(yy, zl, 1.0, e, g)[4])
        print("   K = 1, R = %4.1f: sonic line x from %+.3f to %+.3f"
              " half-heights, theta on it %+.2f..%+.2f deg; on the first"
              " all-supersonic z = const line M %.3f..%.3f, 1 - W/W* %.2e"
              % (R, x_of_z(zs.min(), e, g), x_of_z(zs.max(), e, g),
                 th.min(), th.max(), M.min(), M.max(),
                 1.0 - mass_flow_ratio(1.0, e, g)))
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    return NPASS[0] == NPASS[1]


STAGE = os.environ.get("TK_STAGE", "verify")

if __name__ == "__main__":
    sys.exit(0 if {"verify": verify,
                   "startline": startline}.get(STAGE, verify)() else 1)
