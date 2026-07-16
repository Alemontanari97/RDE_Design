"""(xi) OP-0-gamma — real-thermo ceiling vs demoted gamma=const oracle,
with REJECTION.

Verifies the gamma-purge deliverable of src/thrust/bounds_gamma.py
(strengthened S5 gamma directive: the executable ceiling's PRIMARY route
is EOS-general Cantera h(s,P); the closed forms are DECLARED ORACLES):

  G1  known-answer oracle LIVE: a constant-cp gas (gamma = 7/5 exact)
      through the SAME real route reproduces the closed forms within the
      derived TOL_KA; a corrupted route (h0 scaled by 1+1e-4) is REJECTED.
  G2  persisted record structure: 18 rows (12 finite-Pa + 6 vacuum
      declared lower-bound instruments), all row_ok, no violations.
  G3  row invariants re-run live via check_row (not the persisted flag):
      cap probe holds; subcritical rows: the NAIVE (uncapped) form
      strictly LOSES to the sonic cap — the g=1.15 counterexample of
      record generalized to gamma(T), executably; supercritical rows:
      naive == capped within the derived row bar.
  G4  cross-route concordance semantics: each row's delta vs the closed
      oracle carries its derived bar (Richardson + exact-flash interp
      probes); the persisted 'delta_significant' flag is CONSISTENT with
      |delta| vs bar (the record cannot claim significance it does not
      have, nor hide significance it has).
  G5  REJECTION (negative controls): corrupted rows — suppressed
      subcritical naive-loss, broken cap probe, naive==capped violation
      forged on a supercritical row — must all FAIL check_row.
"""
import copy
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from src.thrust.bounds_gamma import (REAL_JSON, TOL_KA, check_row,
                                     known_answer)


def run():
    ok = True

    def check(name, cond, detail=''):
        nonlocal ok
        ok &= bool(cond)
        print('  %-56s %s %s' % (name, 'PASS' if cond else 'FAIL', detail))

    # ---- G1: known-answer oracle live + rejection -------------------------
    ka_ok, ka = known_answer()
    check('G1: constant-cp known-answer reproduces closed forms', ka_ok,
          '(worst %.1e vs tol %.0e)' % (max(ka.values()), TOL_KA))
    ka_bad, kb = known_answer(corrupt=True)
    check('G1: corrupted route (h0 * (1+1e-4)) REJECTED', not ka_bad,
          '(worst %.1e)' % max(kb.values()))

    # ---- G2: persisted record structure ------------------------------------
    rec = json.load(open(REAL_JSON))
    rows = rec['rows']
    vac = [r for r in rows if r['vacuum']]
    fin = [r for r in rows if not r['vacuum']]
    sub = [r for r in fin if r['subcritical']]
    check('G2: 18 rows = 12 finite-Pa + 6 vacuum instruments',
          (len(rows), len(fin), len(vac)) == (18, 12, 6))
    check('G2: all rows OK, no violations',
          all(r['row_ok'] and not r['violations'] for r in rows))
    check('G2: subcritical rows present (cap regime exercised)',
          len(sub) >= 1, '(%d rows)' % len(sub))

    # ---- G3: invariants re-run (not the flag) ------------------------------
    bad = []
    for r in rows:
        good, viol = check_row(r)
        if not good:
            bad.append('%s|%d|%s: %s' % (r['prop'], r['Pcp'], r['nozzle'],
                                         '; '.join(viol)))
    check('G3: check_row holds on all rows (re-run)', not bad,
          bad[0] if bad else '')
    check('G3: subcritical naive strictly loses to the sonic cap at the '
          'deepest phase (EOS-general counterexample)',
          all(r['naive_gap_deep'] < -r['cf_noise'] for r in sub),
          '(worst deep gap %.2e)' % max(
              (r['naive_gap_deep'] for r in sub), default=float('nan')))
    check('G3: cap probe (grid exits never beat the capped formula)',
          all(r['cap_probe']['ok'] for r in fin))

    # ---- G4: significance flags consistent with bars ----------------------
    incons = [r for r in fin
              if r['delta_significant'] != (abs(r['delta_rel'])
                                            > r['tol_row']
                                            / r['Isp']['ideal_closed'])]
    check('G4: delta_significant flags consistent with derived bars',
          not incons)

    # ---- G5: negative controls — corrupted rows MUST be rejected ----------
    if sub:
        r = copy.deepcopy(sub[0])
        r['naive_gap_deep'] = +1.0e-3
        check('G5: suppressed subcritical naive-loss REJECTED',
              not check_row(r)[0])
        r = copy.deepcopy(sub[0])
        r['Isp']['ideal_real_naive'] = r['Isp']['ideal_real'] + 1.0
        check('G5: naive Isp above capped Isp REJECTED',
              not check_row(r)[0])
    sup = [r for r in fin if not r['subcritical']]
    if sup:
        r = copy.deepcopy(sup[0])
        r['Isp']['ideal_real_naive'] = r['Isp']['ideal_real'] \
            + 10.0 * r['tol_row'] + 1.0e-6
        check('G5: supercritical naive != capped beyond bar REJECTED',
              not check_row(r)[0])
        r = copy.deepcopy(sup[0])
        r['cap_probe']['ok'] = False
        check('G5: broken cap probe REJECTED', not check_row(r)[0])
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
