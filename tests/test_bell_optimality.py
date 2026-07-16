"""(vi) Executable optimality proofs - Stechmann bell/spike area ratio.

Verifies, on the shipped Table-1 states, the theorems of
validation/bell_optimality_proof.md WITH the full mass-weighted averaging
machinery of the model (Eqs. 4-6, 9-15):

  L   Euler lemma dCF/deps = (Pe - Pa)/Pc: central differences vs the closed
      form over a (gamma, eps, Pc) grid (guards the implementation).
  T1a Stationarity at eps* = eps_of_npr(<Pc>_t/Pa): |dIsp/deps| ~ 0 there,
      strictly + below / - above (sign structure of Theorem 1).
  T1b Global dominance Isp(eps*) >= Isp(eps* + delta) for deltas up to
      several units, and concavity (second difference < 0).
  T1c Discrimination: the plausible-but-wrong MASS-weighted-mean condition
      NPR = <Pc>_mdot/Pa gives a measurably larger eps and strictly lower
      Isp - the suite can reject the wrong averaging, not just confirm.
  T2  Spike: strictly increasing below the saturation knee, exactly flat
      above it (Theorem 2).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import numpy as np

from src.common.constants import P_ATM as ATM
from src.thrust.st_core import TR, cf_bell, cf_spike, npr_of_eps
from src.thrust.stechmann_nozzle import cycle_isp, eps_of_npr, dkey


def run():
    ok = True

    def check(name, cond, detail=''):
        nonlocal ok
        ok &= bool(cond)
        print('  %-56s %s %s' % (name, 'PASS' if cond else 'FAIL', detail))

    # ---- L: Euler lemma by central differences --------------------------
    worst = 0.0
    for g in (1.13, 1.20, 1.30):
        for e in (2.0, 4.0, 10.0, 40.0):
            for Pc_atm in (3.0, 20.0, 200.0):
                Pc = Pc_atm * ATM
                h = 1e-4 * e
                num = (cf_bell(g, e + h, Pc) - cf_bell(g, e - h, Pc)) / (2 * h)
                ana = 1.0 / npr_of_eps(e, g) - ATM / Pc
                worst = max(worst, abs(num - ana) / (abs(ana) + 1e-3))
    check('L: dCF/deps == (Pe-Pa)/Pc (36-pt gamma/eps/Pc grid)',
          worst < 1e-5, '(worst rel %.1e)' % worst)

    D = json.load(open(os.path.join(ROOT, 'data', 'st_nozzle_opt.json')))
    S = D['states']
    for r in [r for r in D['rows'] if r['nozzle'] == 'Bell' and r['Pa'] > 0]:
        s = S[dkey(r['prop'], r['Pcp'], r['paper']['phi_det'])]
        g = s['gamma']
        Pa = ATM
        isp = lambda e: cycle_isp(s, lambda Pc, e=e: cf_bell(g, e, Pc, Pa))
        est = r['model']['det']['eps']
        key = '%s %d' % (r['prop'], r['Pcp'])
        h = 1e-3 * est
        d0 = (isp(est + h) - isp(est - h)) / (2 * h)
        dm = (isp(0.8 * est + h) - isp(0.8 * est - h)) / (2 * h)
        dp = (isp(1.3 * est + h) - isp(1.3 * est - h)) / (2 * h)
        c2 = isp(est + 10 * h) - 2 * isp(est) + isp(est - 10 * h)
        check('T1a %s: dIsp/deps ~ 0 at eps*, +/- around' % key,
              abs(d0) <= 0.02 * max(dm, -dp) and dm > 0 and dp < 0,
              '(%.1e; %+.3f/%+.3f)' % (d0, dm, dp))
        dom = all(isp(est) >= isp(max(est + d, 1.05)) - 1e-9
                  for d in (-3.0, -1.0, -0.2, -0.05, 0.05, 0.2, 1.0, 3.0))
        check('T1b %s: global dominance + concavity' % key,
              dom and c2 < 0, '(d2=%.1e)' % c2)
        # T1c: mass-weighted mean pressure is the WRONG condition
        xi = np.linspace(0.0, 1.0, 4001)
        Pc = s['P0'] * s['PR'] ** (-xi)
        cs = s['cstar0'] * (Pc / s['P0']) ** ((g - 1) / (2 * g))
        md = Pc / cs
        Pm_md = float(TR(md * Pc, xi) / TR(md, xi))
        e_alt = eps_of_npr(Pm_md / Pa, g)
        check('T1c %s: time-mean beats mass-mean condition' % key,
              e_alt > est + 0.01 and isp(est) > isp(e_alt) + 1e-6,
              '(eps* %.2f vs alt %.2f, dIsp %+.2f s)'
              % (est, e_alt, isp(est) - isp(e_alt)))

    # ---- T3: outer-DOF (phi) certificates on all 36 optimizations -------
    nfull = 0
    okc = oku = oks = True
    for r in D.get('full_rows', []):
        for side in ('det', 'cp'):
            m = r['full'][side]
            nfull += 1
            okc &= bool(m['lattice_certified']) and m['lattice_gap'] > 0
            oku &= bool(m['unimodal']) and m['n_local_max'] == 1
            # re-derive unimodality from the PERSISTED grid (reproducible)
            vals = [v for _, v in m['grid']]
            nloc = sum(1 for j in range(len(vals))
                       if (j == 0 or vals[j] > vals[j - 1]) and
                          (j == len(vals) - 1 or vals[j] > vals[j + 1]))
            oks &= nloc == 1
    check('T3 phi: strict lattice certificate, all %d optima' % nfull, okc)
    check('T3 phi: unimodal (n_local_max == 1), all %d' % nfull, oku)
    check('T3 phi: unimodality re-derived from persisted grids', oks)

    # ---- T2: spike knee structure (live, CH4 20 atm case) ---------------
    s = S[dkey('CH4', 20, 1.64)]
    g = s['gamma']
    Pa = ATM
    isps = lambda e: cycle_isp(s, lambda Pc, e=e: cf_spike(g, e, Pc, Pa))
    kn = eps_of_npr(s['P0'] / Pa, g)
    check('T2 spike: strictly increasing below knee',
          isps(0.6 * kn) < isps(0.8 * kn) < isps(0.98 * kn) < isps(kn))
    check('T2 spike: exactly flat above knee',
          abs(isps(1.5 * kn) - isps(kn)) < 1e-9 and
          abs(isps(3.0 * kn) - isps(kn)) < 1e-9)
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
