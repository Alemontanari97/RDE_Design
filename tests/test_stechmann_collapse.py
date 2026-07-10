"""(ii) Stechmann mass-weighted blowdown -> steady constant-pressure collapse.

For PR -> 1 the blowdown cycle degenerates to a steady CP chamber, so the
mass-weighted Isp (Eqs. 4-15) must equal the classical steady CF*c*/g0 at the
same gamma, R, T0, Pc (eps = 1, sea level).  Asserted at two parameter sets:
the synthetic tables.py anchor (gamma = 1.2) and the real H2/O2 shipped CJ
record.  Tolerance TOL['cp_collapse_rel'] = 1e-6 (measured ~1e-10).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import numpy as np

from src.common.constants import G0, P_ATM, TOL


def _steady(ge, R, T, Pin):
    from src.thrust.st_core import cstar_fn, cf_base
    NPR = ((ge + 1) / 2) ** (ge / (ge - 1))
    base = cf_base(ge)
    cf = np.sqrt(base * (1 - (1 / NPR) ** ((ge - 1) / ge))) + (1 / NPR - P_ATM / Pin)
    return cf * cstar_fn(ge, R, T) / G0


def run():
    from src.thrust.sk_models import stech_calc
    import cantera as ct

    cases = [('synthetic g=1.2', 1.20, 8314.462 / 24.0, 3500.0, 20 * P_ATM)]
    cj = json.load(open(os.path.join(ROOT, 'data', 'thrust_models_all.json'))
                   )['cases']['H2/O2']['cj']
    cases.append(('H2/O2 shipped CJ', cj['gamma_e'],
                  ct.gas_constant / cj['M2w'], cj['T2'], 20 * P_ATM))

    ok = True
    for name, ge, R, T, Pin in cases:
        st = stech_calc(ge, R, 1.0 + 1e-9, Pin, T)
        ref = _steady(ge, R, T, Pin)
        err = abs(st['Isp_sl_e1'] / ref - 1.0)
        good = err <= TOL['cp_collapse_rel']
        ok &= good
        print('  %-24s Isp %-9.4f vs steady %-9.4f rel.err %.2e  %s'
              % (name, st['Isp_sl_e1'], ref, err, 'PASS' if good else 'FAIL'))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
