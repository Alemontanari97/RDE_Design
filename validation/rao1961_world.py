"""[F3] RAO'S WORLD — his contour, marched by OUR solver.

THE GOAL. Four links of the Rao chain are closed: his tables are
usable, his optimum reconstructs from his own equations, our gas is
his gas (2.6e-08), and our thrust functional is his thrust functional
(eps 1.5e-04, C_F 2.5e-04). The fifth is the one the optimizer needs:
can OUR MARCH compute the field over an arbitrary contour in his
world? Until it can, the SQP cannot score a design there.

THE CONSTRUCTION. `plug_march`'s own docstring names the intended
start data: "the exact corner-fan field on a vertical cut -- the
corner itself lives in the DATA, exactly as Brick 1's throat corner
lives in its initialExpansion fan; ordinary cells cannot jump a
centered wave". So:

  * the lip at (0, R_E) with a SONIC throat, Rao's convention;
  * the centered fan spans M = 1 (the throat) to M_edge, where
    p = p_a = 0.0355 p_c -- his a-posteriori ambient;
  * theta(M) = theta_E + nu(M) - nu(M_E), which puts theta_E = -8.25
    deg at M_E = 2.4 (his control-surface value at the lip) and
    theta = -51.79 deg at the sonic throat -- against Table 1's
    -51.92 for the contour there;
  * the start line is a VERTICAL CUT at x0, rows from the wall
    (Rao's Table 1, interpolated) to the edge ray.

WHY THE CUT MUST BE CLOSE, AND WHY THAT IS TESTABLE. A centered fan is
a PLANAR object; in axisymmetric flow the source term accumulates with
distance from the corner (yesterday's finding: a planar-fan streamline
cannot reproduce his ideal spike, and Rao's own Eq. (10) carries the
dR/R term). Near the lip the correction is small, and it shrinks with
x0. So x0 is not a fudge -- it is a convergence parameter, and the
carrier sweeps it.

THE ACCEPTANCE TEST is a FIELD test, not a thrust test. Rao's control
surface is the C+ through the lip, and we already reproduce its state
independently of the march (rao1961_control_surface: M 2.4 -> 2.2029,
theta -8.25 -> -19.687 deg at R/R_E 1 -> 0.137, matching his Table 1
terminus to 0.04 deg). A thrust comparison would drag in
control-volume bookkeeping; the field comparison does not.

PRE-REGISTERED (R5)
  P1  the march CERTIFIES on his contour (worst cell <= 1);
  P2  the marched field on the C+ through the lip reproduces the
      reconstructed control surface, and the agreement IMPROVES as x0
      shrinks -- the planar-fan start error converging away.
FALSIFIER: no convergence in x0 means the start construction is wrong,
not merely coarse, and the world build must be re-thought rather than
refined.

ON-DEMAND CARRIER (env: jax).
"""
import os
import sys

import numpy as np
import jax.numpy as jnp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import a1_ideal_march_jax as A1                        # noqa: E402
from a1_plug_march import plug_march                   # noqa: E402
from rao1961_ideal_spike import nu                     # noqa: E402

G = 1.23
M_E = 2.4
TH_E = np.radians(-8.25)
PA_PC = 0.0355
RE = 1.0

# Rao Table 1 (gamma=1.23, eps=3.81, L/R_E=1.164): X/R_E, R/R_E
TAB1 = np.array([
    [-0.109, 0.9165], [-0.016, 0.782], [0.034, 0.728], [0.087, 0.678],
    [0.132, 0.640], [0.192, 0.596], [0.267, 0.545], [0.314, 0.516],
    [0.367, 0.484], [0.429, 0.450], [0.502, 0.413], [0.588, 0.371],
    [0.690, 0.324], [0.815, 0.271], [0.969, 0.209], [1.164, 0.137]])


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def fan(tab):
    """The centered lip fan: M in [1, M_edge], theta(M), ray angle."""
    g = G
    pa_p0 = PA_PC
    M_edge = np.sqrt(((pa_p0 ** (-(g - 1.0) / g)) - 1.0)
                     * 2.0 / (g - 1.0))
    Ms = np.linspace(1.0 + 1e-9, M_edge, 4000)
    nus = np.array([nu(m, g) for m in Ms])
    ths = TH_E + nus - nu(M_E, g)
    phis = ths - np.arcsin(1.0 / Ms)
    return Ms, ths, phis, M_edge


def wall_y(x):
    return np.interp(x, TAB1[:, 0], TAB1[:, 1])


def build_start(x0, N, Ms, ths, phis, tab, ta):
    """Vertical cut at x0: rows from the wall up to the edge ray."""
    yw = float(wall_y(x0))
    ye = RE + x0 * np.tan(phis[-1])          # last fan ray
    ys = np.linspace(yw, ye, N)
    psis = np.arctan2(ys - RE, x0)
    Mrow = np.interp(np.clip(psis, phis[0], phis[-1]), phis, Ms)
    throw = np.interp(np.clip(psis, phis[0], phis[-1]), phis, ths)
    T0, Rg = float(tab["ts"]), float(tab["Rg"])
    T = T0 / (1.0 + 0.5 * (G - 1.0) * Mrow ** 2)
    q = Mrow * np.sqrt(G * Rg * T)
    return (x0, ys, q * np.cos(throw), q * np.sin(throw)), Mrow, throw


def main():
    ok = True
    print("== [F3] Rao's world: his contour marched by OUR solver ==")
    tab = A1.prep_tab(A1.build_tab_gconst())        # gamma = 1.23
    ta = A1.tab_arrays(tab)
    Ms, ths, phis, M_edge = fan(tab)
    print("   lip fan: M 1 -> %.4f (p_a/p_c = %.4f); theta %.2f -> %.2f"
          " deg" % (M_edge, PA_PC, np.degrees(ths[0]),
                    np.degrees(ths[-1])))
    print("   at M_E = 2.4 the fan gives theta = %.3f deg (Rao: -8.25)"
          % np.degrees(np.interp(M_E, Ms, ths)))
    print("   at the sonic throat theta = %.2f deg (Table 1 contour:"
          " -51.92)" % np.degrees(ths[0]))
    qpa = float(np.interp(M_edge, Ms, Ms) * 0.0) + float(
        Ms[-1] * np.sqrt(G * float(tab["Rg"])
                         * float(tab["ts"])
                         / (1.0 + 0.5 * (G - 1.0) * Ms[-1] ** 2)))

    # THE TWO-PARAMETER STUDY. x0 alone is not a refinement: the cut
    # NARROWS as x0 shrinks (wall and edge ray converge on the lip), so
    # a fixed row count crowds the rows -- the regime the plug march's
    # own W-2 checks flag as chord-error-dominated. Rows are therefore
    # scaled with the cut WIDTH, so the row spacing stays comparable and
    # x0 is the only thing actually varying.
    print("\n   x0     width   rows  cells   cert      dy_row")
    print("   " + "-" * 54)
    runs = []
    w_ref = None
    for x0 in (0.30, 0.20, 0.10, 0.05):
        yw = float(wall_y(x0)); ye = RE + x0 * np.tan(phis[-1])
        width = ye - yw
        if w_ref is None:
            w_ref, n_ref = width, 41
        N = max(9, int(round(n_ref * width / w_ref)))
        start, Mrow, throw = build_start(x0, N, Ms, ths, phis, tab, ta)
        xs = np.linspace(x0, TAB1[-1, 0], 61)[1:]
        ys = wall_y(xs); sl = np.gradient(ys, xs)
        try:
            out, _ = plug_march((xs, ys, sl), start, qpa, tab, 1.0)
        except Exception as exc:
            print("   %.2f   %.4f   %3d    RAISED: %s"
                  % (x0, width, N, str(exc)[:40]))
            continue
        print("   %.2f   %.4f   %3d  %5d  %.3e  %.5f"
              % (x0, width, N, int(out["cert_n"]),
                 float(out["cert_worst"]), width / (N - 1)))
        runs.append((x0, N, out))
        ok &= check("x0 = %.2f certifies with row-scaled start" % x0,
                    float(out["cert_worst"]) <= 1.0)

    # P2: the marched field ON THE CONTROL SURFACE vs the independent
    # reconstruction. The C+ through the lip is the locus; we read the
    # marched state at the radii Rao tabulates and compare theta.
    print("\n   -- P2: marched field on the lip C+ vs the "
          "reconstruction --")
    from rao1961_control_surface import (state as cs_state,
                                         theta_of_M as cs_theta)
    from scipy.optimize import brentq
    wE, rhoE, pE, alE = cs_state(M_E)
    C2 = wE * np.cos(TH_E + alE) / np.cos(alE)
    C3 = rhoE * wE ** 2 * np.sin(TH_E) ** 2 * np.tan(alE)

    def th_ref(r):
        m = brentq(lambda mm: (C3 / (cs_state(mm)[1] * cs_state(mm)[0] ** 2
                                     * np.sin(cs_theta(mm, C2)) ** 2
                                     * np.tan(cs_state(mm)[3]))) - r,
                   1.6, M_E - 1e-9, xtol=1e-13)
        return np.degrees(cs_theta(m, C2))

    probes = [0.30, 0.20, 0.137]
    print("   R/R_E   reconstruction   " + "   ".join(
        "x0=%.2f" % r[0] for r in runs))
    for r in probes:
        row = "   %.3f     %+8.3f    " % (r, th_ref(r))
        for _, _, out in runs:
            mesh = np.asarray(out["mesh_pts"])
            k = np.argmin(np.abs(mesh[:, 1] - r))
            row += "   %+7.3f" % np.degrees(
                np.arctan2(mesh[k, 3], mesh[k, 2]))
        print(row)
    print("   (a converging start construction moves these toward the")
    print("    reconstruction as x0 shrinks; a broken one does not)")

    print("\nVERDICT: %s" % ("PASS (setup stage)" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
