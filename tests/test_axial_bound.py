"""(iii) SK axial-flow sonic point vs an INDEPENDENT equilibrium bound.

The equilibrium expansion bound of the sonic specific thrust (the live
counterpart of the build-side data/expansion_bounds.json, see
validation/README.md) is recomputed here by a second, independent algorithm —
the official SDT demo_PrandtlMeyerDetn / demo_quasi1d_eq march: SV-equilibrate
steps in specific volume from the CJ state, axial speed ue = sqrt(2(h1-h)),
sonic point interpolated on Me = ue/a_eq = 1, T/Mdot = ue + (P-Pa)/(rho*ue).

Assertions:
  * axial_calc (live, from the shipped H2/air CJ record) reproduces the
    shipped FovM_sonic to <= 1e-9 rel (pure determinism check);
  * axial_calc sonic T/Mdot == independent SV-march bound within
    TOL['axial_vs_bound_rel'] = 2e-3 (~0%; the official-audit cross-run
    measured 5e-5 on the same point, validation/sdt_official_audit.md §3.2.4).
"""
import json
import os
import sys
import warnings

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import numpy as np

from src.common.constants import P_ATM, TOL


def sv_march_bound(cj, fuel, ox, mech, vstep=500, vmax=20.0, Pa=P_ATM):
    """Demo-style independent equilibrium bound (SV march + sonic interp)."""
    import cantera as ct
    from sdtoolbox.thermo import soundspeed_eq
    ct.suppress_thermo_warnings()
    gas = ct.Solution(mech)
    gas.set_equivalence_ratio(1.0, fuel, ox)
    gas.TP = cj['cond']['T1'], cj['cond']['P1']
    h1 = gas.enthalpy_mass
    gas.TPX = cj['T2'], cj['P2'], gas.X
    gas.equilibrate('TP')                       # rebuild CJ equilibrium
    s2 = gas.entropy_mass
    v1 = 1.0 / gas.density
    ue = []; a = []; P = []; rho = []
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        for v in np.linspace(v1, vmax * v1, vstep):
            gas.SVX = s2, v, gas.X
            gas.equilibrate('SV')
            h = gas.enthalpy_mass
            ue.append(np.sqrt(max(2.0 * (h1 - h), 0.0)))
            a.append(soundspeed_eq(gas))
            P.append(gas.P); rho.append(gas.density)
    ue = np.asarray(ue); a = np.asarray(a)
    P = np.asarray(P); rho = np.asarray(rho)
    Me = ue / a
    j = int(np.argmax(Me >= 1.0))
    sl = slice(max(j - 4, int(np.argmax(Me > 0))), min(j + 4, len(Me)))
    from scipy.interpolate import pchip
    ues = float(pchip(Me[sl], ue[sl])(1.0))
    Ps = float(pchip(Me[sl], P[sl])(1.0))
    rs = float(pchip(Me[sl], rho[sl])(1.0))
    return ues + (Ps - Pa) / (rs * ues)


def run():
    from src.thrust.sk_models import axial_calc
    C = json.load(open(os.path.join(ROOT, 'data', 'thrust_models_all.json'))
                  )['cases']['H2/air']
    cj, shipped = C['cj'], C['axial']['FovM_sonic']

    ax = axial_calc(cj, 'H2', 'O2:1,N2:3.76', mech='gri30.yaml')
    live = ax['FovM_sonic']
    d_ship = abs(live / shipped - 1.0)
    bound = sv_march_bound(cj, 'H2', 'O2:1,N2:3.76', 'gri30.yaml')
    d_bound = abs(live / bound - 1.0)

    ok1 = d_ship <= 1e-9
    ok2 = d_bound <= TOL['axial_vs_bound_rel']
    print('  axial_calc live vs shipped   %.4f / %.4f  rel %.2e  %s'
          % (live, shipped, d_ship, 'PASS' if ok1 else 'FAIL'))
    print('  axial sonic vs indep. bound  %.4f / %.4f  rel %.2e (%.3f%%)  %s'
          % (live, bound, d_bound, 100 * d_bound, 'PASS' if ok2 else 'FAIL'))
    return ok1 and ok2


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
