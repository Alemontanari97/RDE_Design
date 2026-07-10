"""cj_core.py — ONE canonical CJ-state function for the whole package.

`cj_state(mix, p1, T1)` wraps the vendored SD Toolbox chain — CJspeed
(equilibrium-Hugoniot minimum-wave-speed) → PostShock_eq → soundspeed_eq
(TP method) — and returns the canonical record used, via thin adapters, by

  * src/thrust/sk_models.cj_calc        (thrust suite, 1 atm fill)
  * src/cycles/cycles.three_cycles      (cycle suite, 1 bar fill, any pi_c)
  * src/cycles/q_mapping                (consumes the store built from it)
  * tests/test_cj_coherence.py          (asserts all paths agree <= 1e-9 rel)

The call sequence and floating-point formulas replicate the pre-refactor
per-module code exactly (validation/interface_audit.md §5), so every blessed
number is unchanged by construction.

Two CJ solvers intentionally remain OUTSIDE this core:
  * src/detonation/cj_states.CJ_state — standalone pedagogical solver,
    independent of the SD Toolbox by design (cross-validation value);
  * src/thrust/st_core._hug_point (via stechmann_nozzle.det_state) — the
    verbatim Stechmann-pipeline solver behind the blessed 18/18 Table-1
    validation and the live design-study numbers.
Their agreement with this core is *asserted* by tests/test_cj_coherence.py
at TOL['cross_solver_rel'] instead of being assumed.

GAMMA CONVENTION (see README "Two conventions you must not mix"):
  gamma_e  = rho2*a_eq^2/P2 — equilibrium isentropic exponent at CJ
             (the Shepherd–Kasahara Eq. 19-22 / Stechmann gamma, ~1.13-1.17);
  gamma_fr = cp/cv of the products at frozen CJ composition (~1.22-1.27).
The CJ point is sonic w.r.t. the EQUILIBRIUM sound speed (w2/a_eq = 1).
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(_HERE))           # repo root
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)                              # vendored sdtoolbox/

from src.common import mixtures
from src.common.constants import P_ATM, T_STD


def _resolve_mech(mech):
    """Make a registry/JSON mechanism id loadable from any cwd."""
    if not os.path.isabs(mech) and ('/' in mech or os.sep in mech):
        cand = os.path.join(ROOT, mech)
        if os.path.exists(cand):
            return cand
    return mech                     # bare names (gri30.yaml) or absolute paths


def cj_state(mix, p1=P_ATM, T1=T_STD, mech=None, return_gas=False):
    """Equilibrium Chapman–Jouguet state of `mix` at initial (p1 [Pa], T1 [K]).

    mix  : registry key/alias ('H2/air', 'kerosene/O2', ...) OR a Cantera
           composition string ('H2:2,O2:1,N2:3.76'; then `mech` is required).
    mech : mechanism override (default: registry entry / required for raw X).

    Returns the canonical dict (SI units):
      U_CJ, M_CJ            CJ speed [m/s], U_CJ/a1_fr
      p1, T1, p2, T2, p2_p1 initial & CJ pressure/temperature [Pa, K]
      rho1, rho2            densities [kg/m^3]
      h1, h2, s2            reactant/CJ enthalpy [J/kg], CJ entropy [J/kg/K]
      gamma_e, gamma_fr     equilibrium / frozen exponents at CJ (see above)
      a_eq, a_fr            equilibrium / frozen sound speed at CJ [m/s]
      a1_fr                 frozen sound speed of the reactants [m/s]
      w2, u2_lab            post-wave speed, wave / lab frame [m/s]
      W1, W2                mean molecular weights [kg/kmol]
      Yf                    fuel mass fraction (registry mixtures; else None)
      sonic_resid           |w2/a_eq - 1| (expect ~1e-3, the CJspeed fit floor)
      X, mech, key          provenance
    With return_gas=True returns (record, gas2) where gas2 is the Cantera
    Solution equilibrated at the CJ state (for downstream expansions).
    """
    import cantera as ct
    from sdtoolbox.postshock import CJspeed, PostShock_eq
    from sdtoolbox.thermo import soundspeed_eq

    key = None
    fuel = None
    if isinstance(mix, str) and (':' not in mix):         # registry key/alias
        key = mixtures.resolve(mix)
        m = mixtures.MIXTURES[key]
        X = m['X']
        fuel = m['fuel']
        mech = mech if mech is not None else m['mech']
    else:                                                  # raw composition
        X = mix
        if mech is None:
            raise ValueError('cj_state: mech= is required with a raw '
                             'composition string')
    mech = _resolve_mech(mech)

    gas1 = ct.Solution(mech)
    gas1.TPX = T1, p1, X
    h1 = gas1.enthalpy_mass
    rho1 = gas1.density
    a1_fr = gas1.sound_speed
    W1 = gas1.mean_molecular_weight
    Yf = float(gas1[fuel].Y[0]) if fuel is not None else None

    U = float(CJspeed(p1, T1, X, mech))
    gas2 = PostShock_eq(U, p1, T1, X, mech)
    P2, T2, rho2 = gas2.P, gas2.T, gas2.density
    a_eq = float(soundspeed_eq(gas2))
    a_fr = float(gas2.sound_speed)
    gamma_e = rho2 * a_eq ** 2 / P2
    gamma_fr = gas2.cp_mass / gas2.cv_mass
    w2 = U * rho1 / rho2

    rec = dict(U_CJ=U, M_CJ=U / a1_fr,
               p1=float(p1), T1=float(T1), p2=float(P2), T2=float(T2),
               p2_p1=float(P2 / p1), rho1=float(rho1), rho2=float(rho2),
               h1=float(h1), h2=float(gas2.enthalpy_mass),
               s2=float(gas2.entropy_mass),
               gamma_e=float(gamma_e), gamma_fr=float(gamma_fr),
               a_eq=a_eq, a_fr=a_fr, a1_fr=float(a1_fr),
               w2=float(w2), u2_lab=float(U - w2),
               W1=float(W1), W2=float(gas2.mean_molecular_weight), Yf=Yf,
               sonic_resid=float(abs(w2 / a_eq - 1.0)),
               X=X, mech=mech, key=key)
    return (rec, gas2) if return_gas else rec
