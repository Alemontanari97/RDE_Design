"""(i) ONE CJ state from every canonical path + independent-solver agreement.

Canonical paths (must be IDENTICAL, <= TOL['cj_identity_rel'] = 1e-9 rel):
  * src/common/cj_core.cj_state          (the core)
  * src/thrust/sk_models.cj_calc         (thrust adapter, 1 atm cases)
  * src/cycles/cycles.three_cycles       (cycle adapter, 1 bar, pi_c = 1)

Independent solvers (agreement asserted at TOL['cross_solver_rel'] = 2e-3,
NOT unified by design — see validation/interface_audit.md §5):
  * src/detonation/cj_states.CJ_state    (standalone pedagogical solver)
  * src/thrust/stechmann_nozzle.det_state (verbatim Stechmann-pipeline solver)
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from src.common.constants import P_ATM, P_REF_BAR, T_STD, TOL
from src.common.cj_core import cj_state


def _rel(a, b):
    return abs(a / b - 1.0)


def run():
    from src.thrust.sk_models import cj_calc
    from src.cycles.cycles import three_cycles
    from src.detonation.cj_states import CJ_state
    from src.thrust import stechmann_nozzle as stn

    checks = []

    # --- canonical identity: cj_core vs sk_models adapter (1 atm cases) ----
    for key in ('H2/air', 'C2H4/O2'):
        r0 = cj_state(key, p1=P_ATM, T1=T_STD)
        r1 = cj_calc(key)
        for name, a, b in (('U_CJ', r1['UCJ'], r0['U_CJ']),
                           ('gamma_e', r1['gamma_e'], r0['gamma_e']),
                           ('p2', r1['P2'], r0['p2']),
                           ('T2', r1['T2'], r0['T2']),
                           ('s2', r1['s2'], r0['s2']),
                           ('h1', r1['h1'], r0['h1'])):
            checks.append(('sk_models %s %s' % (key, name), _rel(a, b),
                           TOL['cj_identity_rel']))
        checks.append(('%s sonic residual' % key, r0['sonic_resid'],
                       TOL['sonic_resid_max']))

    # --- canonical identity: cj_core vs cycles adapter (1 bar, pi_c=1) -----
    r0 = cj_state('CH4/air', p1=P_REF_BAR, T1=T_STD)
    rc = three_cycles('CH4/air', 'CH4:1,O2:2,N2:7.52', 'gri30.yaml',
                      T1=T_STD, P1=P_REF_BAR, do_HB=False, n_exp=4)
    checks.append(('cycles CH4/air U_CJ', _rel(rc['U_CJ'], r0['U_CJ']),
                   TOL['cj_identity_rel']))
    checks.append(('cycles CH4/air gamma_e', _rel(rc['gamma_e_CJ'],
                   r0['gamma_e']), TOL['cj_identity_rel']))

    # --- independent solver 1: cj_states (standalone) ----------------------
    rH = cj_state('H2/air', p1=P_ATM, T1=T_STD)
    ri = CJ_state('gri30.yaml', 'H2:2,O2:1,N2:3.76', T_STD, P_ATM)
    checks.append(('indep cj_states U_CJ', _rel(ri['UCJ'], rH['U_CJ']),
                   TOL['cross_solver_rel']))
    checks.append(('indep cj_states gamma_e', _rel(ri['gamma_eq'],
                   rH['gamma_e']), TOL['cross_solver_rel']))

    # --- independent solver 2: stechmann det_state vs cj_ref ---------------
    det = stn.det_state('CH4', 1.00, 300.0, P_ATM)
    ref = stn.cj_ref('CH4', 1.00, 300.0, P_ATM)
    checks.append(('indep det_state PR', _rel(det['PR'], ref['p2_p1']),
                   TOL['cross_solver_rel']))
    checks.append(('indep det_state T_CJ', _rel(det['TCJ'], ref['T2']),
                   TOL['cross_solver_rel']))
    checks.append(('indep det_state gamma', _rel(det['gamma'],
                   ref['gamma_e']), TOL['cross_solver_rel']))

    # --- golden inline ------------------------------------------------------
    checks.append(('golden U_CJ(H2/air) == 1969.0',
                   abs(round(rH['U_CJ'], 1) - 1969.0), 1e-12))

    ok = True
    for name, val, tol in checks:
        good = val <= tol
        ok &= good
        print('  %-38s %.3e  (tol %.0e)  %s'
              % (name, val, tol, 'PASS' if good else 'FAIL'))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
