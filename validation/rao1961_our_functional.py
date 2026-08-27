"""[F3-entry] OUR THRUST FUNCTIONAL vs RAO 1961, ON HIS OWN SURFACE.

THE QUESTION. The SQP maximizes OUR thrust functional. Before any
optimizer comparison against Rao can mean anything, that functional
has to agree with his on a design where he published the answer --
otherwise a difference in optimum is just a difference in objective.

WHAT MAKES THIS POSSIBLE WITHOUT A MARCH. Rao's solution lives on the
control surface ED, and we now reconstruct that surface from his own
first integrals to his published precision (rao1961_control_surface:
X_D/R_E to 1.3e-06, C_F to 2.5e-04, theta_D to 0.04 deg). His area
ratio (his Eq. 11) and thrust coefficient (his Eq. 12) are integrals
ALONG that surface. Our `col_fluxes_rot` computes the same two
integrals for any line of nodes:

    mass   rho (u dy - v dx) . 2 pi y          <-> his Eq. (2)
    thrust rho u (u dy - v dx) + (p - pa) dy   <-> his Eq. (3) integrand

so his surface can be handed to OUR functional directly, in physical
units, on OUR tabulated thermodynamics.

This therefore tests the objective itself: our quadrature, our
state routines, our flux convention -- against a number published in
1961 and independent of everything in this repository.

THE WORLD. gamma = 1.23 via build_tab_gconst (its default, and
verified equal to the closed forms Rao's example needs to 2.6e-08),
R_E = 1 m, p_b = 0, and the vacuum convention of his Eq. (12).

PRE-REGISTERED (R5)
  P1  our mass integral gives his area ratio eps = 3.81;
  P2  our thrust integral gives his C_F = 1.58 (Table 3: 1.5804);
  both inside the precision he prints (5e-3 relative).
FALSIFIER: either outside its bar means our objective is NOT his, and
the Rao-vs-SQP comparison is blocked until the difference is found --
which would be a finding about our functional, not about his design.

REJECTOR
  N1  a 1 % perturbation of the surface's velocities must move C_F
      outside the bar (the test must be able to see an error).

ON-DEMAND CARRIER (env: jax).
"""
import os
import sys

import numpy as np
import jax.numpy as jnp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import a1_ideal_march_jax as A1                       # noqa: E402
import a1_rot_march as R                              # noqa: E402
from rao1961_control_surface import (state, theta_of_M,  # noqa: E402
                                     G, M_E, TH_E, REF)

RE = 1.0                       # cowl-lip radius [m]; Rao is in R_E units
PRINT_BAR = 5.0e-3


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def build_surface(n=4001):
    """Rao's control surface E -> D, cut at HIS published terminus."""
    wE, rhoE, pE, alE = state(M_E)
    C2 = wE * np.cos(TH_E + alE) / np.cos(alE)
    C3 = rhoE * wE ** 2 * np.sin(TH_E) ** 2 * np.tan(alE)
    from scipy.optimize import brentq
    m_D = brentq(lambda m: (C3 / (state(m)[1] * state(m)[0] ** 2
                                  * np.sin(theta_of_M(m, C2)) ** 2
                                  * np.tan(state(m)[3]))) - REF["rd"],
                 1.6, M_E - 1e-9, xtol=1e-13)
    Ms = np.linspace(M_E, m_D, n)
    ths = np.array([theta_of_M(m, C2) for m in Ms])
    st = np.array([state(m) for m in Ms])
    rs = C3 / (st[:, 1] * st[:, 0] ** 2 * np.sin(ths) ** 2
               * np.tan(st[:, 3]))
    # x from the surface direction, his Eq. (5): dx/dR = cot(theta-alpha)
    dxdr = 1.0 / np.tan(ths - st[:, 3])
    xs = np.concatenate([[0.0], np.cumsum(
        0.5 * (dxdr[1:] + dxdr[:-1]) * np.diff(rs))])
    return Ms, ths, rs, xs


def main():
    ok = True
    print("== [F3-entry] OUR thrust functional on RAO's control "
          "surface ==")
    tab = A1.prep_tab(A1.build_tab_gconst())     # gamma = 1.23 default
    ta = A1.tab_arrays(tab)
    p0, T0, Rg = float(tab["ps"]), float(tab["ts"]), float(tab["Rg"])
    s0, h0 = float(tab["s0"]), float(tab["h0"])
    print("   world: gamma %.2f  p_c %.3e Pa  T_0 %.1f K  R_E %.1f m"
          % (tab["_g"], p0, T0, RE))

    Ms, ths, rs, xs = build_surface()
    # physical nodes, ordered D -> E so dy > 0 along the line
    T = T0 / (1.0 + 0.5 * (G - 1.0) * Ms ** 2)
    q = Ms * np.sqrt(G * Rg * T)
    col = np.stack([xs * RE, rs * RE, q * np.cos(ths), q * np.sin(ths),
                    np.full(Ms.size, s0), np.full(Ms.size, h0)],
                   axis=1)[::-1]
    print("   surface: %d nodes, R/R_E %.4f -> %.4f, M %.4f -> %.4f"
          % (col.shape[0], rs[-1], rs[0], Ms[-1], Ms[0]))

    md, F, _ = R.col_fluxes_rot(col, ta, 0.0, 1.0)   # vacuum: pa = 0
    # A* from the choked-throat relation for a perfect gas
    Gam = np.sqrt(G) * (2.0 / (G + 1.0)) ** ((G + 1.0)
                                             / (2.0 * (G - 1.0)))
    A_star = abs(md) * np.sqrt(Rg * T0) / (p0 * Gam)
    eps = np.pi * RE ** 2 / A_star
    cf = abs(F) / (p0 * A_star)

    print("\n   OUR mass integral  -> mdot = %.6e kg/s -> A* = %.6e m^2"
          % (abs(md), A_star))
    for name, got, ref in (("eps  (pi R_E^2/A*)", eps, REF["eps"]),
                           ("C_F  (vacuum)", cf, REF["cf"])):
        rel = abs(got - ref) / ref
        print("   %-20s ours %.4f   Rao %.4f   rel %.2e"
              % (name, got, ref, rel))
        ok &= check("%s from OUR functional reproduces Rao"
                    % name.split()[0], rel <= PRINT_BAR)

    colb = col.copy()
    colb[:, 2:4] *= 1.01
    _, Fb, _ = R.col_fluxes_rot(colb, ta, 0.0, 1.0)
    cfb = abs(Fb) / (p0 * A_star)
    ok &= check("N1 rejector: a 1 %% velocity error moves C_F outside "
                "the bar (rel %.2e)" % (abs(cfb - REF["cf"])
                                        / REF["cf"]),
                abs(cfb - REF["cf"]) / REF["cf"] > PRINT_BAR)

    print("\nVERDICT: %s" % ("PASS -- our objective IS Rao's objective"
                             if ok else "FAIL -- the objectives differ"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
