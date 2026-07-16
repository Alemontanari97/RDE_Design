"""(viii) OP-0 eps-level bound ladder - chain, attainment, and REJECTION.

Verifies, on the shipped Table-1 states and the persisted ladder record
(data/bounds_ladder.json), the chain of src/thrust/bounds.py:

    Isp[eps_fix] <= Isp_intmax == Isp_ideal <= B_EK          (chain C)

  B1  live recomputation of all 18 rows == persisted record (staleness
      guard: the JSON cannot drift from the code that claims it).
  B2  chain C holds on every row via check_chain, re-run here (not the
      persisted flag); strict gaps resolvable above the derived
      quadrature-roundoff tolerance NQ*eps_mach.
  B3  structure: 18 rows; 6 vacuum (ceiling NOT attained at finite eps,
      Theorem 3); 4 subcritical (choke_margin < 1: the NAIVE uncapped
      ideal is violated as a bound); 8 supercritical sea-level rows where
      the peak-designed S-H plug ATTAINS the ceiling (M1 gap-zero).
  B4  per-phase counterexample of record: at g = 1.15, Pc/Pa = 1.3 the
      sonic exit strictly beats "complete expansion to Pa" - the naive
      per-streamtube form is not an upper bound below the critical NPR.
  B5  REJECTION (negative controls): corrupted ladders - each rung order
      flipped in turn, fake vacuum attainment, suppressed subcritical
      naive-violation, and a broken implementation that uses the naive
      ceiling - must all FAIL check_chain.  The suite can reject a wrong
      ladder, not merely confirm the right one.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import numpy as np

from src.common.constants import P_ATM as ATM
from src.thrust.bounds import (LADDER_JSON, TOL_REL, cf_ideal, cf_ideal_naive,
                               cf_intmax, cf_sonic, check_chain, ladder_row)
from src.thrust.stechmann_nozzle import dkey, load


def run():
    ok = True

    def check(name, cond, detail=''):
        nonlocal ok
        ok &= bool(cond)
        print('  %-56s %s %s' % (name, 'PASS' if cond else 'FAIL', detail))

    rec = json.load(open(LADDER_JSON))
    rows = rec['rows']
    D = load()

    # ---- B1: live recomputation == persisted record ----------------------
    worst = 0.0
    for r in rows:
        s = D['states'][dkey(r['prop'], r['Pcp'], r['phi_det'])]
        live = ladder_row(s, r['Pa_atm'] * ATM, r['eps_fix'])
        for k, v in live['Isp'].items():
            worst = max(worst, abs(v - r['Isp'][k]) / abs(v))
    check('B1: live ladder == persisted JSON, 18 rows x 6 rungs',
          worst <= TOL_REL, '(worst rel %.1e)' % worst)

    # ---- B2: chain C re-verified row by row ------------------------------
    bad = []
    for r in rows:
        good, viol = check_chain(r)
        if not good:
            bad.append('%s|%d|%s: %s' % (r['prop'], r['Pcp'], r['nozzle'],
                                         '; '.join(viol)))
    check('B2: chain C holds on all %d rows (re-run, not flag)' % len(rows),
          not bad, ('' if not bad else bad[0]))
    check('B2: persisted chain_ok flags all true',
          all(r['chain_ok'] and not r['violations'] for r in rows))

    # ---- B3: regime structure --------------------------------------------
    vac = [r for r in rows if r['vacuum']]
    sub = [r for r in rows if r['subcritical']]
    sup = [r for r in rows if not r['vacuum'] and not r['subcritical']]
    check('B3: 18 rows = 6 vacuum + 4 subcritical + 8 supercritical',
          (len(rows), len(vac), len(sub), len(sup)) == (18, 6, 4, 8))
    check('B3: M1 gap-zero (plug == ideal) on all supercritical rows',
          all(abs(r['Isp']['plug'] - r['Isp']['ideal']) <= r['tol_abs']
              for r in sup))
    check('B3: vacuum rows: ceiling strictly unattained at finite eps',
          all(r['Isp']['plug'] < r['Isp']['ideal'] - r['tol_abs']
              for r in vac))
    check('B3: subcritical rows: naive rung strictly violated',
          all(r['Isp']['ideal_naive'] < r['Isp']['intmax'] - r['tol_abs']
              for r in sub),
          '(worst gap %.1e s)' % min(
              (r['Isp']['intmax'] - r['Isp']['ideal_naive'] for r in sub),
              default=float('nan')))
    check('B3: EK gap strictly positive on every row (u_eff varies)',
          all(r['Isp']['ek'] > r['Isp']['ideal'] + r['tol_abs']
              for r in rows))

    # ---- B4: the per-phase counterexample of record ----------------------
    g_cx = 1.15                                 # documented value of record
    Pc = np.array([1.3 * ATM])
    d = float((cf_sonic(g_cx, Pc, ATM) - cf_ideal_naive(g_cx, Pc, ATM))[0])
    check('B4: sonic exit beats naive full expansion (g=1.15, Pc/Pa=1.3)',
          d > 0, '(delta CF = %+.4f)' % d)
    dcap = float((cf_ideal(g_cx, Pc, ATM) - cf_sonic(g_cx, Pc, ATM))[0])
    check('B4: capped ceiling equals the sonic branch there', dcap == 0.0)

    # ---- B5: negative controls - corrupted ladders MUST be rejected ------
    import copy

    def corrupt(base, **edits):
        r = copy.deepcopy(base)
        r['Isp'].update(edits)
        good, _ = check_chain(r)
        return good

    r_sup = sup[0]
    r_vac = vac[0]
    r_sub = sub[0]
    big = 10.0 * r_sup['tol_abs']
    check('B5: bell above intmax REJECTED',
          not corrupt(r_sup, bell=r_sup['Isp']['intmax'] + 1.0))
    check('B5: dual-route breach (ideal != intmax) REJECTED',
          not corrupt(r_sup, ideal=r_sup['Isp']['intmax'] - big))
    check('B5: B_EK below ideal REJECTED',
          not corrupt(r_sup, ek=r_sup['Isp']['ideal'] - 1.0))
    check('B5: fake M1 gap (plug below ideal) REJECTED',
          not corrupt(r_sup, plug=r_sup['Isp']['ideal'] - 1.0))
    check('B5: fake vacuum attainment REJECTED',
          not corrupt(r_vac, plug=r_vac['Isp']['ideal']))
    check('B5: suppressed subcritical naive-violation REJECTED',
          not corrupt(r_sub, ideal_naive=r_sub['Isp']['intmax'] + 1.0))
    # broken implementation: ceiling computed with the naive (uncapped)
    # form on a subcritical cycle - the dual-route certificate must fire
    s = D['states'][dkey(r_sub['prop'], r_sub['Pcp'], r_sub['phi_det'])]
    broken = ladder_row(s, r_sub['Pa_atm'] * ATM, r_sub['eps_fix'])
    broken['Isp']['ideal'] = broken['Isp']['ideal_naive']
    good, _ = check_chain(broken)
    check('B5: naive-ceiling implementation REJECTED on subcritical row',
          not good)

    # pointwise sanity: intmax route (Eq. 9 + eps*) vs ceiling route agree
    # on a dense grid, both regimes (the discrete backbone of chain C)
    for r in (r_sup, r_sub):
        s = D['states'][dkey(r['prop'], r['Pcp'], r['phi_det'])]
        g = s['gamma']
        Pc = s['P0'] * s['PR'] ** (-np.linspace(0.0, 1.0, r['n']))
        dmax = float(np.max(np.abs(cf_intmax(g, Pc, r['Pa_atm'] * ATM)
                                   - cf_ideal(g, Pc, r['Pa_atm'] * ATM))))
        check('B2+ pointwise dual-route agreement (%s %d)'
              % (r['prop'], r['Pcp']), dmax <= TOL_REL,
              '(max |dCF| = %.1e)' % dmax)
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
