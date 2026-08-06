"""(ix) A0.3 gamma-channel probe - the D3 S5.2 numbers, verifiable & rejectable.

Consumes data/gamma_cycle_probe.json (written by the committed probe
examples/gamma_cycle_probe.py on the blessed state det|CH4|20|1.64) and
verifies, WITHOUT Cantera, the corrected numbers of record of D3 S5.2:

  G1  anchor: probe chamber gamma_s == blessed st_nozzle_opt gamma
      (TP re-equilibration class, < 1e-4).
  G2  physics structure: gamma_s(xi) has a SINGLE shallow interior
      minimum near the CJ end (dissociation-temperature competition,
      measured at xi ~ 0.1, depth ~4e-4) and then rises monotonically
      (recombination): exactly one sign change in its increments and a
      net rise across the cycle; gamma_fr >= gamma_s pointwise
      (a_fr >= a_eq), both within (1, 5/3].
  G3  golden digits of record: gamma_s 1.154 -> 1.209 (D3's "1.210"
      confirmed to its own rounding), eps* shift -0.56 % (STRIKES the
      stale -1.9 %), Isp penalty -0.0003 % (second-order, confirms the
      envelope claim; stale "-0.001 %" corrected in magnitude).
  G4  re-derivation: eps*_fr, eps*_var, shift and penalty recomputed
      here from the PERSISTED arrays (pure numpy + the repo closed
      forms) match the persisted scalars.
  G5  envelope structure: 0 < penalty <= shift^2 (second-order).
  G6  closure discrimination: gamma_eff = <Pc gamma>/<Pc> reproduces the
      true shift (< 0.1 pt); the unweighted <gamma> mean does NOT
      (> 1 pt off): the wrong averaging is REJECTED, and a corrupted
      record (gamma_s reversed) fails the re-derivation (negative
      control).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import numpy as np

from src.common.constants import G0, P_ATM as ATM
from src.thrust.st_core import Ik, cf_bell, npr_of_eps
from src.thrust.stechmann_nozzle import dkey, eps_of_npr, load

TR = np.trapezoid   # numpy >= 2.0 (toolchain-currency directive, S17)
PROBE = os.path.join(ROOT, 'data', 'gamma_cycle_probe.json')


def _derive(xi, Pc, gs, cs, P0, PR, g_cj, Pa):
    """Re-derive (eps_fr, eps_var, shift, penalty) from persisted arrays."""
    Pmean = P0 * Ik(PR, 1.0)
    eps_fr = eps_of_npr(Pmean / Pa, g_cj)
    n = len(xi)

    def dN(eps):
        Pe = np.array([Pc[i] / npr_of_eps(eps, gs[i]) for i in range(n)])
        return float(TR(Pe - Pa, xi))

    from scipy.optimize import brentq
    eps_var = brentq(dN, 0.5 * eps_fr, 2.0 * eps_fr)

    def isp_var(eps):
        cf = np.array([cf_bell(gs[i], eps, Pc[i], Pa) for i in range(n)])
        return float(TR(Pc * cf, xi) / (G0 * TR(Pc / cs, xi)))

    penalty = 1.0 - isp_var(eps_fr) / isp_var(eps_var)
    return eps_fr, eps_var, eps_var / eps_fr - 1.0, penalty


def run():
    ok = True

    def check(name, cond, detail=''):
        nonlocal ok
        ok &= bool(cond)
        print('  %-56s %s %s' % (name, 'PASS' if cond else 'FAIL', detail))

    d = json.load(open(PROBE))
    xi = np.array(d['xi']); Pc = np.array(d['Pc'])
    gs = np.array(d['gamma_s']); gf = np.array(d['gamma_fr'])
    cs = np.array(d['cstar'])
    Pa = d['Pa_atm'] * ATM

    # ---- G1: anchor to the blessed pipeline state ------------------------
    s = load()['states'][dkey('CH4', 20, 1.64)]
    check('G1: chamber gamma_s == blessed state gamma (<1e-4)',
          abs(gs[0] / s['gamma'] - 1.0) < 1e-4 and
          d['gamma_cj_blessed'] == s['gamma'],
          '(resid %.1e)' % abs(gs[0] / s['gamma'] - 1.0))

    # ---- G2: physical structure ------------------------------------------
    dg = np.diff(gs)
    nswitch = int(np.sum(np.diff(np.sign(dg)) != 0))
    check('G2: single interior minimum, then monotone recombination rise',
          nswitch == 1 and dg[0] < 0 and dg[-1] > 0 and gs[-1] > gs[0],
          '(min at xi=%.3f, depth %.1e)'
          % (xi[int(np.argmin(gs))], gs[0] - gs.min()))
    check('G2: gamma_fr >= gamma_s pointwise, both in (1, 5/3]',
          bool(np.all(gf >= gs) and np.all(gs > 1) and np.all(gf <= 5 / 3)))

    # ---- G3: golden digits of record (D3 S5.2, corrected) ----------------
    check('G3: gamma_s ends 1.154 -> 1.209 (3 decimals)',
          round(gs[0], 3) == 1.154 and round(gs[-1], 3) == 1.209,
          '(%.4f -> %.4f)' % (gs[0], gs[-1]))
    check('G3: eps* shift = -0.56% (strikes the stale -1.9%)',
          round(100 * d['eps_shift'], 2) == -0.56,
          '(%+.3f%%)' % (100 * d['eps_shift']))
    check('G3: Isp penalty magnitude ~3e-6 (stale -0.001% corrected)',
          1e-6 < d['isp_penalty'] < 1e-5,
          '(%.2e)' % d['isp_penalty'])

    # ---- G4: scalars re-derived from the persisted arrays ----------------
    e_fr, e_var, shift, pen = _derive(xi, Pc, gs, cs,
                                      d['P0'], d['PR'],
                                      d['gamma_cj_blessed'], Pa)
    check('G4: eps*_fr / eps*_var / shift re-derived == persisted',
          abs(e_fr / d['eps_fr'] - 1) < 1e-9 and
          abs(e_var / d['eps_var'] - 1) < 1e-6 and
          abs(shift - d['eps_shift']) < 1e-6)
    check('G4: penalty re-derived == persisted',
          abs(pen - d['isp_penalty']) < 1e-9,
          '(%.2e vs %.2e)' % (pen, d['isp_penalty']))

    # ---- G5: envelope (second-order) structure ---------------------------
    check('G5: 0 < penalty <= shift^2 (second-order design penalty)',
          0.0 < pen <= shift ** 2,
          '(pen %.2e, shift^2 %.2e)' % (pen, shift ** 2))

    # ---- G6: closure discrimination + negative control -------------------
    check('G6: gamma_eff closure reproduces the true shift (<0.1 pt)',
          abs(d['eps_shift_gamma_eff'] - d['eps_shift']) < 1e-3,
          '(%+.3f%% vs %+.3f%%)' % (100 * d['eps_shift_gamma_eff'],
                                    100 * d['eps_shift']))
    check('G6: unweighted <gamma> closure REJECTED (>1 pt off)',
          abs(d['eps_shift_plain_mean'] - d['eps_shift']) > 1e-2,
          '(%+.2f%%)' % (100 * d['eps_shift_plain_mean']))
    # corrupted record: gamma_s reversed must fail both structure and
    # re-derivation (the checks can REJECT, not merely confirm)
    gs_bad = gs[::-1].copy()
    shape_bad = gs_bad[-1] > gs_bad[0]          # net rise must fail reversed
    _, _, shift_bad, _ = _derive(xi, Pc, gs_bad, cs, d['P0'], d['PR'],
                                 d['gamma_cj_blessed'], Pa)
    check('G6: corrupted (reversed) gamma_s REJECTED',
          (not shape_bad) and abs(shift_bad - d['eps_shift']) > 1e-3,
          '(bad shift %+.3f%%)' % (100 * shift_bad))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
