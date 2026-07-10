#!/usr/bin/env python3
"""st_core.py — model core of the Stechmann–Heister–Harroun RDE performance model.

PROVENANCE: extracted verbatim from project_build/scripts/figs_st_eap.py
(figure-generation module of the lecture build), keeping ONLY the physics
functions needed by stechmann_nozzle.py; all plotting code was left behind.

Reference: Stechmann, Heister & Harroun, "Rotating Detonation Engine
Performance Model for Rocket Applications", J. Spacecraft & Rockets 56(3),
2019, doi:10.2514/1.A34313. Paper equation numbers:

  Eq. 1/7   c* = sqrt(g R T0) / ( g sqrt( (2/(g+1))^((g+1)/(g-1)) ) )
  Eq. 6     mdot/A_t = Pc/c*                     (thermally choked exit)
  Eq. 9     CF_bell  = sqrt( B (1 - NPR^(-(g-1)/g)) ) + eps (1/NPR - Pa/Pc),
            B = 2g^2/(g-1) (2/(g+1))^((g+1)/(g-1));  NPR(eps,g) from the
            isentropic area–Mach relation (fixed geometry)
  Eq. 10    CF_spike = sqrt( B (1 - (Pa/Pc)^((g-1)/g)) )   ideal plug, Pe = Pa
  Eq. 11-12 spike capped at eps_max: behaves as a bell while Pe(t,eps_max) > Pa
  Eq. 13-14 exponential blowdown: Ik(PR,k) = (1-PR^-k)/(k ln PR) is the cycle
            mean of (Pc/P_CJ)^k, used for the closed-form mass matching

_hug_point solves one point of the EQUILIBRIUM Hugoniot (TP-equilibrations
only): T2 such that h2 - h1 = (P2 - P1)(v1 + v2)/2 with P2 = rho2 R T2 / M.
The CJ point is then the minimum of U(x) = v1 sqrt((P2-P1)/(v1-v2)) over the
density ratio x = rho2/rho1 (see stechmann_nozzle.det_state).

Assumptions (paper assumption 2): gamma = equilibrium isentropic exponent
gamma_s = rho a_eq^2 / P at the chamber state, then FROZEN in space and time
through blowdown and nozzle.

Usage example:
    from st_core import cstar_fn, cf_bell, npr_of_eps
    cf = cf_bell(1.15, 4.0, 20 * 101325.0)     # bell CF at eps=4, Pc=20 atm
"""
import os as _os
import sys as _sys
import numpy as np
from scipy.optimize import brentq

_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
if _ROOT not in _sys.path:
    _sys.path.insert(0, _ROOT)
from src.common.constants import G0, P_ATM as ATM        # shared constants

PA = 1.0 * ATM            # sea-level ambient (default of cf_bell / cf_spike)
TR = getattr(np, 'trapezoid', np.trapz)


# ------------------------------------------------------------------ gas model
def cstar_fn(g, R, T):
    """Eq. 1/7: characteristic velocity from (gamma, R_specific, T0)."""
    return np.sqrt(g * R * T) / (g * np.sqrt((2 / (g + 1)) ** ((g + 1) / (g - 1))))


def Ik(PR, k):
    """Cycle mean of (Pc/P_CJ)^k for the Eq. 13-14 exponential blowdown."""
    return (1.0 - PR ** (-k)) / (k * np.log(PR))


def _ct():
    import cantera as ct
    ct.suppress_thermo_warnings()
    return ct


def _hug_point(work, h1, v1, P1, x, Tg):
    """Equilibrium Hugoniot point at density ratio x = rho2/rho1, TP-equilibrates
    only: solve T2 s.t.  h2 - h1 = (P2 - P1)(v1 + v2)/2  with P2 = rho2 R T2 / M."""
    import cantera as ct
    Ru = ct.gas_constant
    v2 = v1 / x; rho2 = 1.0 / v2

    def state(T, Pg):
        for _ in range(8):
            work.TP = T, Pg
            work.equilibrate('TP')
            Pn = rho2 * Ru / work.mean_molecular_weight * T
            if abs(Pn / Pg - 1.0) < 2e-4:
                break
            Pg = Pn
        work.TP = T, Pn
        work.equilibrate('TP')
        return Pn

    def res(T, Pg):
        P = state(T, Pg)
        return work.enthalpy_mass - h1 - 0.5 * (P - P1) * (v1 + v2), P

    Ta, Tb = Tg, Tg * 1.03
    Ra, Pl = res(Ta, 30.0 * P1 * x / 1.8)
    Rb, Pl = res(Tb, Pl)
    for _ in range(30):
        if abs(Rb - Ra) < 1e-9:
            break
        Tc = min(max(Tb - Rb * (Tb - Ta) / (Rb - Ra), 1200.0), 5200.0)
        Ta, Ra = Tb, Rb
        Rb, Pl = res(Tc, Pl)
        Tb = Tc
        if abs(Rb) < 2e2:          # J/kg on an h-scale of ~5e6: <0.005 %
            break
    return Pl, Tb


# ------------------------------------------------------------------ nozzles
def cf_base(g):
    return 2 * g * g / (g - 1) * (2 / (g + 1)) ** ((g + 1) / (g - 1))


def npr_of_eps(eps, g):
    """NPR(eps, gamma) from the isentropic area-Mach relation (supersonic root)."""
    if eps <= 1.0:
        return ((g + 1) / 2) ** (g / (g - 1))
    f = lambda M: (1 / M) * ((2 / (g + 1)) * (1 + (g - 1) / 2 * M * M)) \
        ** ((g + 1) / (2 * (g - 1))) - eps
    Me = brentq(f, 1.0001, 20.0)
    return (1 + (g - 1) / 2 * Me * Me) ** (g / (g - 1))


def cf_bell(g, eps, Pc, Pa=PA, NPR=None):
    """Eq. 9: fixed-geometry (bell) thrust coefficient; only Pa/Pc(t) varies."""
    NPR = npr_of_eps(eps, g) if NPR is None else NPR
    mom = np.sqrt(cf_base(g) * (1 - NPR ** (-(g - 1) / g)))
    return mom + eps * (1.0 / NPR - Pa / Pc)


def cf_spike(g, eps_max, Pc, Pa=PA):
    """Eqs. 10-12: ideal aerospike, Pe = Pa, capped at eps_max early in cycle."""
    NPR = npr_of_eps(eps_max, g)
    free = np.sqrt(cf_base(g) *
                   np.clip(1 - np.minimum(Pa / Pc, 1.0) ** ((g - 1) / g), 0, None))
    return np.where(Pc / NPR > Pa, cf_bell(g, eps_max, Pc, Pa, NPR), free)
