"""cj_states.py — CJ / von Neumann solver on Cantera (SD Toolbox equilibrium-Hugoniot method).

Lecture-repo edition of project_build/scripts/detonation.py (verbatim physics;
one dead placeholder removed from the returned dict).

Provides CJ_state() (equilibrium-Hugoniot CJ point via Rayleigh-speed minimisation)
and vN_state() (frozen post-shock von Neumann state). Validated against
Shepherd & Kasahara GALCIT FM2017.001 Table 2 / Caltech detonation DB
(U_CJ within 0.1%, see data/sk_tables.json and validation/VALIDATION.md).

EQUATIONS IMPLEMENTED
  * equilibrium Hugoniot:  h2 - h1 = (p2 - p1)(v1 + v2)/2   with products in
    shifting equilibrium (Shepherd, GALCIT FM2018.001, Eq. 2.1-2.5);
  * Rayleigh wave speed:   U = v1 sqrt((p2 - p1)/(v1 - v2));
  * CJ point = minimum of U over the compression ratio v1/v2 (the tangency /
    minimum-wave-speed statement of the CJ condition);
  * von Neumann state: frozen-composition shock jump (mass + momentum +
    energy, fixed-point iteration on specific volume).

GAMMA CONVENTION (see validation/gamma_audit.md):
  gamma_eq = rho2*a_eq^2/P2  -- EQUILIBRIUM isentropic exponent of the products at CJ
             (a_eq = equilibrium/shifting sound speed), ~1.13-1.17. This is the
             "gamma_e" of Shepherd & Kasahara Eq. 19-22 and Tables 1-2.
  gamma_fr = cp/cv of the products at fixed (frozen) composition, ~1.22-1.27.
             NOT interchangeable with gamma_eq: the CJ point is sonic w.r.t. the
             EQUILIBRIUM sound speed (M2 = w2/a_eq = 1; w2/a_fr ~ 0.96-0.97).
(Bug fixed 2026-07-08: gamma_eq was previously the frozen cp/cv, mislabelled.)

Usage:
    python cj_states.py                  # 5-mixture demo table vs Caltech DB
    from cj_states import CJ_state, vN_state
    cj = CJ_state('gri30.yaml', 'H2:2,O2:1,N2:3.76', 300., 101325.)
    # -> cj['UCJ'] ~ 1969 m/s, cj['M2'] ~ 1.000 (equilibrium-sonic check)
"""
import cantera as ct, numpy as np
from scipy.optimize import brentq, minimize_scalar

def soundspeed_eq(gas):
    """Equilibrium (shifting) sound speed a_eq = sqrt((dP/drho)_s at shifting equilibrium).

    SD Toolbox 'soundspeed_eq' method: perturb density at constant entropy,
    re-equilibrate ('SV'), difference the pressure. Cantera's gas.sound_speed is
    the FROZEN sound speed and must not be used for CJ sonic checks.
    The gas object is restored to its incoming state on exit."""
    s0, rho0, T0, P0 = gas.entropy_mass, gas.density, gas.T, gas.P
    rho1 = rho0*(1.0 + 1e-4)
    gas.SV = s0, 1.0/rho1
    gas.equilibrate('SV')
    P1 = gas.P
    a_eq = float(np.sqrt((P1 - P0)/(rho1 - rho0)))
    gas.TD = T0, rho0
    gas.equilibrate('TV')                    # restore equilibrium state at CJ
    return a_eq

def eq_hugoniot_speed(gas, v2, p1, v1, h1, Tlo=1200., Thi=6500.):
    """Return Rayleigh wave speed for equilibrium-Hugoniot state at specific volume v2."""
    def resid(T2):
        gas.TD = T2, 1.0/v2
        gas.equilibrate('TV')
        return gas.enthalpy_mass - h1 - 0.5*(gas.P - p1)*(v1 + v2)
    T2 = brentq(resid, Tlo, Thi, xtol=1e-6, rtol=1e-10)
    gas.TD = T2, 1.0/v2
    gas.equilibrate('TV')
    p2 = gas.P
    if (p2-p1)/(v1-v2) <= 0:  # not on detonation branch
        return np.nan
    U = v1*np.sqrt((p2-p1)/(v1-v2))
    return U

def CJ_state(mech, X, T1, P1):
    gas = ct.Solution(mech)
    gas.TPX = T1, P1, X
    v1 = 1.0/gas.density; h1 = gas.enthalpy_mass; p1 = gas.P
    a1 = gas.sound_speed
    gasW = gas.mean_molecular_weight
    # minimise wave speed over compression ratio r=v1/v2 (detonation compresses: v2<v1)
    def U_of_r(r):
        v2 = v1/r
        val = eq_hugoniot_speed(gas, v2, p1, v1, h1)
        return val if np.isfinite(val) else 1e9
    res = minimize_scalar(U_of_r, bounds=(1.35, 2.4), method='bounded',
                          options={'xatol':1e-6})
    rCJ = res.x; UCJ = res.fun
    v2 = v1/rCJ
    # recover full CJ state
    def resid(T2):
        gas.TD = T2, 1.0/v2; gas.equilibrate('TV')
        return gas.enthalpy_mass - h1 - 0.5*(gas.P - p1)*(v1 + v2)
    T2 = brentq(resid, 1200, 6500)
    gas.TD = T2, 1.0/v2; gas.equilibrate('TV')
    p2, T2 = gas.P, gas.T
    a2_fr = gas.sound_speed                 # FROZEN sound speed (fixed composition)
    gamma_fr = gas.cp_mass/gas.cv_mass      # FROZEN cp/cv of products (~1.22-1.27)
    a2_eq = soundspeed_eq(gas)              # EQUILIBRIUM (shifting) sound speed
    gamma_eq = a2_eq**2/(p2*v2)             # = rho2*a_eq^2/P2, equilibrium isentropic exponent (~1.13-1.17)
    w2 = v2/v1*UCJ                            # mass conservation
    MCJ = UCJ/a1
    return dict(UCJ=UCJ, MCJ=MCJ, p2p1=p2/p1, T2=T2, T1=T1, rho2rho1=rCJ,
                a1=a1, a2_eq=a2_eq, a2_fr=a2_fr, w2=w2,
                M2=w2/a2_eq, M2_fr=w2/a2_fr, gamma_eq=gamma_eq, gamma_fr=gamma_fr,
                P2=p2, Wu=gasW)

def vN_state(mech, X, T1, P1, U):
    """Frozen post-shock (von Neumann) state at wave speed U."""
    gas = ct.Solution(mech); gas.TPX = T1, P1, X
    v1 = 1.0/gas.density; h1 = gas.enthalpy_mass; p1 = gas.P
    m = gas.density*U
    v2 = v1*0.2
    for _ in range(200):
        p2 = p1 + m*m*(v1 - v2)
        h2 = h1 + 0.5*m*m*(v1*v1 - v2*v2)
        gas.HP = h2, p2            # frozen composition (no equilibrate)
        v2n = 1.0/gas.density
        if abs(v2n-v2) < 1e-12: v2=v2n; break
        v2 = v2n
    return dict(pvN_p1=gas.P/p1, TvN=gas.T, PvN=gas.P, rho_ratio=v1/v2)

if __name__ == '__main__':
    # validation vs Caltech detonation database (1 atm, ~298-300 K)
    P1 = ct.one_atm
    cases = [
        ('H2:2,O2:1,N2:3.76',      'H2/air  phi=1',  'gri30.yaml', 300.),
        ('H2:2,O2:1',              'H2/O2  phi=1',   'gri30.yaml', 300.),
        ('CH4:1,O2:2,N2:7.52',     'CH4/air phi=1',  'gri30.yaml', 300.),
        ('CH4:1,O2:2',             'CH4/O2 phi=1',   'gri30.yaml', 300.),
        ('C2H4:1,O2:3,N2:11.28',   'C2H4/air phi=1', 'gri30.yaml', 300.),
    ]
    print(f"{'mixture':16s}{'U_CJ':>8s}{'M_CJ':>7s}{'p2/p1':>7s}{'T2[K]':>8s}{'rho2/1':>7s}{'g_eq':>6s}{'g_fr':>6s}{'M2':>6s}{'pvN/p1':>8s}{'TvN[K]':>8s}")
    for X,name,mech,T1 in cases:
        cj = CJ_state(mech, X, T1, P1)
        vn = vN_state(mech, X, T1, P1, cj['UCJ'])
        print(f"{name:16s}{cj['UCJ']:8.1f}{cj['MCJ']:7.3f}{cj['p2p1']:7.2f}{cj['T2']:8.1f}{cj['rho2rho1']:7.3f}{cj['gamma_eq']:6.3f}{cj['gamma_fr']:6.3f}{cj['M2']:6.3f}{vn['pvN_p1']:8.2f}{vn['TvN']:8.1f}")
