"""[F3-entry] THE IDEAL SPIKE, SONIC LIP — Rao's §5 construction,
validated on his numbers and then available for our world.

WHY. The plug line's incumbent starting design is the fan streamline
of our own case, and the length promotion (PSPL_L) exposed that at full
expansion it FLATTENS at y ~ 0.8633 instead of closing on the axis: the
fan's total turn is spent, the flow is axial, and a wall that is a
streamline cannot descend further. Rao's ideal spike does close, and
the reason is a different defining condition -- uniform axial exit at
the design Mach, with mass conservation forcing R_tip = 0 (every
"ideal spike contour" row of his Table 3 reads R_D/R_E = 0.000).

So the object needed for a full-expansion comparison is not a longer
version of our streamline; it is his construction. Owner decision
2026-08-13: build it with a SONIC LIP, his convention -- throat at the
cowl lip, all expansion external through a centered fan.

THE CONSTRUCTION (his §5, closed form for a perfect gas):
  1. M_e from the area-Mach relation at the prescribed area ratio eps;
  2. the fan turns the flow from sonic to M_e, so the total turn is
     nu(M_e) and the flow leaves the lip at theta_i = -nu(M_e),
     straightening to theta = 0 at the design Mach;
  3. simple wave: theta(M) = nu(M) - nu(M_e), ray direction
     phi(M) = theta(M) - alpha(M) from the lip;
  4. the throat radius follows from mass, his Eq. (12):
        pi (R_E^2 - R_T^2)/cos(theta*) = pi R_E^2 / eps;
  5. the wall is the streamline from T through the fan, integrated
     until it meets the axis.

PRE-REGISTERED (R5) -- the construction is checked against HIS
published ideal-spike lengths BEFORE it is used for anything:
    eps =  3.81 -> X/R_E = 2.433   (his Table 3)
    eps = 10.69 -> X/R_E = 3.271   (his Table 3)
and the contour must reach the axis (that is what "ideal" means).
FALSIFIER: a length outside the printing precision of those figures,
or a contour that flattens instead of closing, means this is not his
construction and it may not be used as his baseline.

REJECTOR
  N1  gamma = 1.4 must break both lengths.

ON-DEMAND CARRIER (env: none -- closed form + one quadrature, seconds).
"""
import sys

import numpy as np
from scipy.optimize import brentq

REF_LEN = {3.81: 2.433, 10.69: 3.271}     # his Table 3, ideal rows
PRINT_BAR = 2.0e-3                        # 4 s.f. on ~2.4-3.3


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def nu(M, g):
    """Prandtl-Meyer angle."""
    if M <= 1.0:
        return 0.0
    a = np.sqrt((g + 1.0) / (g - 1.0))
    b = np.sqrt(M * M - 1.0)
    return a * np.arctan(b / a) - np.arctan(b)


def mach_from_area(eps, g):
    def area(M):
        return (1.0 / M) * ((2.0 / (g + 1.0))
                            * (1.0 + 0.5 * (g - 1.0) * M * M)
                            ) ** ((g + 1.0) / (2.0 * (g - 1.0)))
    return brentq(lambda M: area(M) - eps, 1.0000001, 50.0, xtol=1e-13)


def ideal_spike(eps, g, RE=1.0, n=200000):
    """Rao §5. Returns (x, y) of the wall from the throat to the tip,
    plus the diagnostics that identify the construction."""
    Me = mach_from_area(eps, g)
    nu_e = nu(Me, g)
    th_i = -nu_e                       # flow angle at the sonic lip

    # the fan, parametrised by M: theta(M) and the ray angle phi(M)
    Ms = np.linspace(1.0 + 1e-9, Me, 20000)
    ths = np.array([nu(m, g) for m in Ms]) - nu_e
    als = np.arcsin(1.0 / Ms)
    phis = ths - als                   # C- ray direction from the lip

    def theta_on_ray(psi):
        """Flow angle on the fan ray through direction psi."""
        if psi <= phis[0]:
            return ths[0]
        if psi >= phis[-1]:
            return ths[-1]
        return float(np.interp(psi, phis, ths))

    # throat radius from mass, his Eq. (12)
    RT = RE * np.sqrt(max(1.0 - np.cos(th_i) / eps, 0.0))
    # the throat sits on the FIRST fan ray, at radius RT
    t = (RT - RE) / np.sin(phis[0])
    xT = t * np.cos(phis[0])

    # integrate the wall streamline from T to the axis
    xs, ys = [xT], [RT]
    x, y = xT, RT
    h = (3.0 * RE) / n
    for _ in range(n):
        if y <= 0.0:
            break
        def slope(xx, yy):
            return np.tan(theta_on_ray(np.arctan2(yy - RE, xx)))
        k1 = slope(x, y)
        k2 = slope(x + 0.5 * h, y + 0.5 * h * k1)
        k3 = slope(x + 0.5 * h, y + 0.5 * h * k2)
        k4 = slope(x + h, y + h * k3)
        y += h / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        xs.append(x); ys.append(y)
    xs, ys = np.array(xs), np.array(ys)
    if ys[-1] < 0.0:                   # land exactly on the axis
        xs[-1] = np.interp(0.0, ys[::-1], xs[::-1])
        ys[-1] = 0.0
    return dict(x=xs, y=ys, Me=Me, nu_e=nu_e, th_i=th_i, RT=RT, xT=xT,
                L_RE=(xs[-1] - 0.0) / RE, closed=bool(ys[-1] <= 1e-9))


def main():
    ok = True
    print("== [F3-entry] Rao's IDEAL SPIKE, sonic lip (his §5) ==")
    print("   validation FIRST: his published ideal lengths, gamma = 1.23")
    for eps, ref in REF_LEN.items():
        d = ideal_spike(eps, 1.23)
        print("\n   eps = %-6.2f M_e = %.4f  total fan turn = %.3f deg"
              % (eps, d["Me"], np.degrees(d["nu_e"])))
        print("      throat: R_T/R_E = %.4f at x/R_E = %+.4f  "
              "(flow leaves at %.2f deg)"
              % (d["RT"], d["xT"], np.degrees(d["th_i"])))
        print("      tip:    y = %.2e  ->  X/R_E = %.4f   "
              "Rao = %.3f   rel = %.2e"
              % (d["y"][-1], d["L_RE"], ref,
                 abs(d["L_RE"] - ref) / ref))
        ok &= check("eps=%.2f the contour CLOSES on the axis" % eps,
                    d["closed"])
        ok &= check("eps=%.2f length reproduces Rao's ideal X/R_E"
                    % eps, abs(d["L_RE"] - ref) / ref <= PRINT_BAR)

    bad = [abs(ideal_spike(e, 1.4)["L_RE"] - r) / r
           for e, r in REF_LEN.items()]
    ok &= check("N1 rejector: gamma = 1.4 breaks both lengths "
                "(min rel %.2e)" % min(bad), min(bad) > PRINT_BAR)

    print("\nVERDICT: %s" % ("PASS -- the construction IS Rao's ideal "
                             "spike and may be used as his baseline"
                             if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
