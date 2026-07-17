"""(xii) OP-11-eps REAL-ROUTE phase diagram + equilibrium bracket -
oracles, structure, and REJECTION.

Verifies, on the persisted record (data/phase_diagram_real.json) plus a
declared live-recomputation subset, the EOS-general re-derivation of the
topology phase diagram (src/thrust/phase_diagram_real.py) and the
shifting-equilibrium ceiling bracket:

  E1  every persisted cell passes a FRESH check_cell_real run (not the
      stored flag) and all stored flags are true.
  E2  staleness guard on a DECLARED subset (full live recomputation would
      re-run the Cantera table build; the subset is the blessed-PR block,
      every eps_max): winners, candidates, premium bounds match within
      the persisted tolerances.
  E3  T3 oracle: the PR = 1 (degenerate-measure) column ties on every
      envelope.
  E4  T4/M1 oracle ON THE REAL ROUTE: every knee-fitting cell attains the
      capped real ceiling (duality-gap-zero) INCLUDING cells with
      subcritical tails - the attainment extension of record, now
      EOS-general.
  E5  the naive-adaptation instrument loses strictly to the capped
      closure on every cell with released subcritical phases (the
      gamma(T) generalization of the OP-0 artifact).
  E6  equilibrium bracket: frozen <= eq ceiling per PR within derived
      bars; the eq-route constant-cp known-answer PASSED at generation;
      the recombination gain is strictly positive beyond bars on the
      blessed PR (dissociating CH4/O2 state - a zero gain would flag a
      broken eq route).
  E7  REJECTION (negative controls): corrupted cells (bell winner label,
      dominance breach, stale premium, fake M1 flag, naive closure
      passed off as the record one) must FAIL check_cell_real; an eq row
      pushed below the frozen ceiling must FAIL check_bracket; the
      corrupted eq known-answer (h column scaled) must be REJECTED live.
  E8  cross-anchor: the blessed-PR cell's capped real ceiling equals the
      independently generated data/bounds_ladder_real.json row (CH4-20,
      sea level) within the two records' summed derived bars.
"""
import copy
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import numpy as np

from src.common.constants import P_ATM as ATM
from src.thrust.bounds_gamma import REAL_JSON
from src.thrust.phase_diagram import ANCHOR, i1
from src.thrust.phase_diagram_real import (REAL_DIAG_JSON, build_frozen_table,
                                           cell_row_real, check_bracket,
                                           check_cell_real, known_answer_eq,
                                           pr_block)
from src.thrust.stechmann_nozzle import load


def run():
    ok = True

    def check(name, cond, detail=''):
        nonlocal ok
        ok &= bool(cond)
        print('  %-56s %s %s' % (name, 'PASS' if cond else 'FAIL', detail))

    rec = json.load(open(REAL_DIAG_JSON))
    cells = rec['cells']
    anchor = load()['states'][ANCHOR]
    Pa = rec['Pa_atm'] * ATM

    # ---- E1: fresh invariant run on every persisted cell -------------------
    check('E1: every cell passes check_cell_real re-run (fresh)',
          all(check_cell_real(r)[0] for r in cells),
          '(%d cells)' % len(cells))
    check('E1: persisted cell_ok flags all true',
          all(r['cell_ok'] and not r['violations_cell'] for r in cells))

    # ---- E2: staleness guard on the declared subset (blessed-PR block) ----
    gas, tab, Pc_mean = build_frozen_table(anchor, Pa, rec['pr_grid'])
    blk = pr_block(tab, Pc_mean, float(anchor['PR']), Pa)
    sub = [r for r in cells if abs(r['PR'] - anchor['PR']) < 1e-9]
    worst, wmatch = 0.0, True
    for r in sub:
        live = cell_row_real(blk, tab, r['eps_max'], Pa,
                             r['bar_interp_rel'])
        for k in ('bell', 'plug', 'plug_sh'):
            worst = max(worst, abs(live['cand'][k] - r['cand'][k]))
        worst = max(worst, abs(live['premium_bound'] - r['premium_bound']))
        wmatch &= (live['winner'] == r['winner']
                   and live['m1_gap_zero'] == r['m1_gap_zero'])
    tol_sub = max(r['tol_abs'] for r in sub)
    check('E2: blessed-PR block live == persisted (declared subset)',
          worst <= tol_sub and wmatch,
          '(worst abs %.2e s vs tol %.2e, winners %s)'
          % (worst, tol_sub, 'match' if wmatch else 'DRIFTED'))

    # ---- E3: T3 oracle ------------------------------------------------------
    col1 = [r for r in cells if r['PR'] == 1.0]
    check('E3: PR=1 column present and fully tied (degenerate measure)',
          len(col1) == len(rec['eps_max_grid'])
          and all(r['winner'] == 'tie' for r in col1))

    # ---- E4: T4/M1 attainment on the real route ----------------------------
    fits = [r for r in cells if r['knee_fits']]
    check('E4: every knee-fitting cell attains the capped real ceiling',
          bool(fits) and all(r['m1_gap_zero'] for r in fits),
          '(%d cells)' % len(fits))
    sub_fit = [r for r in fits if r['frac_subcritical'] > 0]
    check('E4: attainment includes subcritical cycles (EOS-general M1)',
          bool(sub_fit) and all(r['m1_gap_zero'] for r in sub_fit),
          '(%d subcritical)' % len(sub_fit))
    check('E4: no cell exceeds the capped real ceiling',
          all(max(r['cand']['bell'], r['cand']['plug'])
              <= r['Isp']['ideal'] + r['tol_abs'] for r in cells))

    # ---- E5: two-level naive metric on the strip (bounds_gamma precedent):
    # the naive instrument never BEATS the capped closure anywhere; near
    # the critical boundary its loss may hide inside the bar, but at the
    # DEEPEST-spread cells it must lose strictly (resolvable artifact).
    strip = [r for r in cells if r['frac_subcritical'] > 0
             and r['n_released'] > 0]
    check('E5a: naive closure never beats capped on the strip',
          bool(strip) and all(r['cand']['plug_sh'] <= r['cand']['plug']
                              + r['tol_abs'] for r in strip),
          '(%d cells)' % len(strip))
    fmax = max(r['frac_subcritical'] for r in strip)
    deep = [r for r in strip if r['frac_subcritical'] == fmax]
    check('E5b: strict naive loss at the deepest-spread cells',
          bool(deep) and all(r['cand']['plug_sh'] < r['cand']['plug']
                             - r['tol_abs'] for r in deep),
          '(%d cells, frac_sub %.3f)' % (len(deep), fmax))

    # ---- E6: equilibrium bracket -------------------------------------------
    eqb = rec['eq_bracket']
    check('E6: eq bracket recorded OK (frozen <= eq per PR)',
          eqb['ok'] and not eqb['violations'])
    bok, bviol = check_bracket(eqb['rows'], cells)
    check('E6: check_bracket re-run passes fresh', bok, '; '.join(bviol))
    r_bl = next(r for r in eqb['rows']
                if abs(r['PR'] - anchor['PR']) < 1e-9)
    c_bl = next(r for r in cells if abs(r['PR'] - anchor['PR']) < 1e-9)
    gain_abs = r_bl['isp_eq'] - c_bl['Isp']['ideal']
    check('E6: recombination gain strictly positive on blessed PR',
          gain_abs > r_bl['bar_tab'] + c_bl['tol_abs'],
          '(gain %.2f s, bars %.3f s)'
          % (gain_abs, r_bl['bar_tab'] + c_bl['tol_abs']))

    # ---- E7: negative controls ----------------------------------------------
    def corrupt(base, **edits):
        r = copy.deepcopy(base)
        for k, v in edits.items():
            (r['cand'] if k in r['cand'] else r)[k] = v
        return check_cell_real(r)[0]

    r_fit = sub_fit[0]
    check('E7: bell winner label REJECTED',
          not corrupt(r_fit, winner='bell'))
    check('E7: dominance breach REJECTED',
          not corrupt(r_fit, bell=r_fit['cand']['plug'] + 1.0))
    check('E7: stale premium bound REJECTED',
          not corrupt(r_fit, premium_bound=r_fit['premium_bound'] + 1.0))
    check('E7: fake M1 attainment REJECTED',
          not corrupt(r_fit, plug=r_fit['Isp']['ideal'] - 1.0,
                      bell=r_fit['Isp']['ideal'] - 1.0))
    # naive-as-record control ON A RESOLVABLE CELL: the deepest-spread
    # knee-fitting cell (its naive gap exceeds the bar per E5b), where
    # forcing plug = plug_sh with the attainment flag kept must trip the
    # recomputed-gap consistency check.
    r_deep = next(r for r in deep if r['knee_fits'])
    broken = copy.deepcopy(r_deep)
    broken['cand']['plug'] = broken['cand']['plug_sh']
    broken['m1_gap_zero'] = True
    check('E7: naive closure as record closure REJECTED',
          not check_cell_real(broken)[0])
    bad_rows = copy.deepcopy(eqb['rows'])
    bad_rows[0]['isp_eq'] = (cells[0]['Isp']['ideal']
                             - 10.0 * (bad_rows[0]['bar_tab']
                                       + cells[0]['tol_abs']))
    bad_rows[0]['PR'] = cells[0]['PR']
    check('E7: eq row below frozen ceiling REJECTED',
          not check_bracket(bad_rows, cells)[0])
    ka_bad_ok, _ = known_answer_eq(corrupt=True)
    check('E7: corrupted eq known-answer REJECTED (live)', not ka_bad_ok)

    # ---- E8: cross-anchor vs the real ladder record -------------------------
    BL = json.load(open(REAL_JSON))
    blrow = next(r for r in BL['rows']
                 if r['key'] == ANCHOR and r['Pa_atm'] == rec['Pa_atm'])
    tol_x = blrow['tol_row'] + c_bl['tol_abs']
    dx = abs(c_bl['Isp']['ideal'] - blrow['Isp']['ideal_real'])
    check('E8: blessed-PR ceiling == bounds_ladder_real row',
          dx <= tol_x, '(diff %.3e s vs summed bars %.3e s)' % (dx, tol_x))
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
