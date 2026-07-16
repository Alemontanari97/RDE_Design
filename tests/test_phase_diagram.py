"""(x) OP-11-eps phase diagram - oracles, structure, and REJECTION.

Verifies, on the persisted record (data/phase_diagram.json) and by live
recomputation, the topology phase diagram of src/thrust/phase_diagram.py,
with the theorem limits as ORACLES and explicit NEGATIVE CONTROLS (a wrong
winning topology must be rejected, not merely not-confirmed):

  D1  staleness guard: live recomputation of every cell == persisted JSON.
  D2  T3 oracle (spread -> 0): the PR = 1 column ties on every envelope;
      the tied value equals the independently recomputed single-phase
      closed form (Rao-at-<Pc> under the cap); the degenerate check_chain
      strictness signature is exactly the expected one.
  D3  T4/M1 oracle (generous envelope): every eps_max >= knee cell attains
      the CAPPED ceiling (duality-gap-zero), INCLUDING the subcritical-
      tail cycles - the capped-closure extension of OP-0's attainment.
  D4  vacuum oracle: ties, strictly increasing in eps_max, ceiling never
      attained (no finite optimum).
  D5  subcritical strip: the published (naive-branch) S-H plug value is
      strictly below the capped closure on every frac_sonic > 0 cell; the
      OP-0 artifact of record - at eps_max = 1 the naive closure loses to
      the sonic exit (bell) - is reproduced live: the naive-closure winner
      flip is DETECTED (and rejected by check_cell in D6).
  D6  REJECTION (negative controls, incl. T3/T4 as required): corrupted
      cells - T3 tie broken at PR = 1, fake T4 attainment flag, winner
      label flipped to 'bell', dominance breach, naive closure passed off
      as the capped one on a subcritical cell, fake vacuum attainment,
      non-monotone vacuum sweep - must all FAIL check_cell/check_vacuum.
  D7  cross-anchor: the blessed-PR cell reproduces the eps_fix-independent
      rungs (ideal, intmax, ek) of data/bounds_ladder.json exactly.
"""
import copy
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import numpy as np

from src.common.constants import G0, P_ATM as ATM
from src.thrust.bounds import LADDER_JSON, check_chain
from src.thrust.st_core import cf_bell, cf_spike
from src.thrust.phase_diagram import (ANCHOR, DIAG_JSON, cell_row,
                                      cf_plug_capped, check_cell,
                                      check_vacuum,
                                      expected_pr1_violations, i1,
                                      state_at, winner_of)
from src.thrust.stechmann_nozzle import load


def run():
    ok = True

    def check(name, cond, detail=''):
        nonlocal ok
        ok &= bool(cond)
        print('  %-56s %s %s' % (name, 'PASS' if cond else 'FAIL', detail))

    rec = json.load(open(DIAG_JSON))
    cells = rec['cells']
    anchor = load()['states'][ANCHOR]
    Pc_mean = anchor['P0'] * i1(anchor['PR'])
    Pa = rec['Pa_atm'] * ATM

    # ---- D1: live recomputation == persisted record -----------------------
    worst, winners_match = 0.0, True
    for r in cells:
        live = cell_row(anchor, r['PR'], r['eps_max'], Pa, Pc_mean)
        for k in ('bell', 'plug_sh', 'plug'):
            worst = max(worst, abs(live['cand'][k] - r['cand'][k])
                        / abs(live['cand'][k]))
        winners_match &= (live['winner'] == r['winner']
                          and live['m1_gap_zero'] == r['m1_gap_zero'])
        worst = max(worst, abs(live['premium_bound'] - r['premium_bound'])
                    / max(abs(live['premium_bound']), 1.0))
    check('D1: live grid == persisted JSON (%d cells)' % len(cells),
          worst <= rec['tol_rel'] and winners_match,
          '(worst rel %.1e, winners %s)'
          % (worst, 'match' if winners_match else 'DRIFTED'))
    check('D1: persisted cell_ok flags all true',
          all(r['cell_ok'] and not r['violations_cell'] for r in cells))
    check('D1: every cell passes check_cell re-run (not flag)',
          all(check_cell(r)[0] for r in cells))

    # ---- D2: T3 oracle - the PR = 1 column --------------------------------
    col1 = [r for r in cells if r['PR'] == 1.0]
    check('D2: PR=1 column present and fully tied (T3)',
          len(col1) == len(rec['eps_max_grid'])
          and all(r['winner'] == 'tie' for r in col1))
    g = anchor['gamma']
    # single-phase Isp = CF * c* / g0 (mdot = Pc/c* cancels the Pc weight)
    worst = max(abs(r['cand']['bell']
                    - float(cf_bell(g, r['eps_bell'], Pc_mean, Pa))
                    * _cs(anchor, Pc_mean) / G0) / r['cand']['bell']
                for r in col1)
    check('D2: tied value == independent single-phase closed form',
          worst <= rec['tol_rel'], '(worst rel %.1e)' % worst)
    sig = all(check_chain(r)[1] == expected_pr1_violations(r) for r in col1)
    check('D2: degenerate chain signature exact on PR=1 column', sig)

    # ---- D3: T4/M1 oracle - generous envelope, incl. subcritical ----------
    fits = [r for r in cells if r['knee_fits']]
    check('D3: every knee-fitting cell attains the capped ceiling (M1)',
          fits and all(r['m1_gap_zero'] for r in fits),
          '(%d cells)' % len(fits))
    sub_fit = [r for r in fits if r['subcritical']]
    check('D3: attainment includes subcritical cycles (capped extension)',
          sub_fit and all(r['m1_gap_zero'] for r in sub_fit),
          '(%d subcritical)' % len(sub_fit))
    check('D3: no cell exceeds the capped ceiling',
          all(max(r['cand']['bell'], r['cand']['plug'])
              <= r['Isp']['ideal'] + r['tol_abs'] for r in cells))

    # ---- D4: vacuum oracle -------------------------------------------------
    vac = rec['vacuum']['rows']
    vok, vviol = check_vacuum(vac)
    check('D4: vacuum sweep - ties, increasing, ceiling unattained',
          vok and rec['vacuum']['ok'], '; '.join(vviol))

    # ---- D5: subcritical strip + the naive-closure artifact ---------------
    strip = [r for r in cells if r['PR'] != 1.0 and r['frac_sonic'] > 0]
    check('D5: naive plug strictly below capped plug on the strip',
          strip and all(r['cand']['plug_sh'] < r['cand']['plug']
                        - r['tol_abs'] for r in strip),
          '(%d cells)' % len(strip))
    # live artifact of record: at eps_max = 1 on the deepest-spread cycle
    # the PUBLISHED closure flips the winner to the bell (sonic exit beats
    # the naive free branch) - the wrong topology the suite must reject.
    r0 = max(strip, key=lambda r: r['PR'])
    s = state_at(anchor, r0['PR'], Pc_mean)
    Pc = s['P0'] * s['PR'] ** (-np.linspace(0.0, 1.0, r0['n']))
    from src.thrust.phase_diagram import _isp_of
    em1 = [r for r in cells if r['PR'] == r0['PR']
           and r['eps_max'] == 1.0][0]
    naive = _isp_of(s, Pa, cf_spike(g, 1.0, Pc, Pa))
    check('D5: published closure loses to bell at eps_max=1 (artifact)',
          naive < em1['cand']['bell'] - em1['tol_abs'],
          '(delta %.1e s)' % (em1['cand']['bell'] - naive))
    capped = _isp_of(s, Pa, cf_plug_capped(g, 1.0, Pc, Pa))
    check('D5: capped closure restores the exact tie there',
          abs(capped - em1['cand']['bell']) <= em1['tol_abs'])

    # ---- D6: negative controls - corrupted cells MUST be rejected ---------
    def corrupt(base, **edits):
        r = copy.deepcopy(base)
        for k, v in edits.items():
            (r['cand'] if k in r['cand'] else r)[k] = v
        return check_cell(r)[0]

    r_tie = col1[0]
    big = 10.0 * r_tie['tol_abs']
    check('D6: T3 control - broken tie at PR=1 REJECTED',
          not corrupt(r_tie, plug=r_tie['cand']['bell'] + big,
                      winner='plug'))
    r_fit = sub_fit[0]
    check('D6: T4 control - fake attainment flag REJECTED',
          not corrupt(r_fit, plug=r_fit['Isp']['ideal'] - 1.0,
                      bell=r_fit['Isp']['ideal'] - 1.0))
    check('D6: bell winner label REJECTED (dominance theorem)',
          not corrupt(r_fit, winner='bell'))
    check('D6: dominance breach (bell above capped plug) REJECTED',
          not corrupt(r_fit, bell=r_fit['cand']['plug'] + 1.0))
    check('D6: stale premium bound REJECTED',
          not corrupt(r_fit, premium_bound=r_fit['premium_bound'] + 1.0))
    # broken implementation: the naive closure passed off as the record one
    broken = copy.deepcopy(r_fit)
    broken['cand']['plug'] = broken['cand']['plug_sh']
    broken['m1_gap_zero'] = True
    check('D6: naive closure as record closure REJECTED (subcritical)',
          not check_cell(broken)[0])
    v_bad = copy.deepcopy(vac)
    v_bad[-1]['cand']['plug'] = v_bad[-1]['Isp']['ideal']
    v_bad[-1]['cand']['bell'] = v_bad[-1]['Isp']['ideal']
    check('D6: fake vacuum attainment REJECTED', not check_vacuum(v_bad)[0])
    v_mono = copy.deepcopy(vac)
    v_mono[0]['cand']['plug'] = v_mono[-1]['cand']['plug'] + 1.0
    v_mono[0]['cand']['bell'] = v_mono[0]['cand']['plug']
    check('D6: non-monotone vacuum sweep REJECTED',
          not check_vacuum(v_mono)[0])
    check('D6: winner_of flags the naive flip as a bell win (detectable)',
          winner_of(dict(cand=dict(bell=em1['cand']['bell'], plug=naive,
                                   plug_sh=naive),
                         tol_abs=em1['tol_abs'],
                         knee_fits=em1['knee_fits'])) == 'bell')

    # ---- D7: cross-anchor vs the OP-0 ladder record ------------------------
    BL = json.load(open(LADDER_JSON))
    blrow = [r for r in BL['rows']
             if r['key'] == ANCHOR and r['Pa_atm'] == rec['Pa_atm']][0]
    r_bl = [r for r in cells if abs(r['PR'] - anchor['PR']) < 1e-6][0]
    worst = max(abs(r_bl['Isp'][k] - blrow['Isp'][k]) / abs(blrow['Isp'][k])
                for k in ('ideal', 'intmax', 'ek'))
    check('D7: blessed-PR cell == bounds_ladder eps_fix-free rungs',
          worst <= rec['tol_rel'], '(worst rel %.1e)' % worst)
    return ok


def _cs(anchor, P):
    """Anchor-isentrope c* at chamber pressure P (single-phase D2 check)."""
    g = anchor['gamma']
    return anchor['cstar0'] * (P / anchor['P0']) ** ((g - 1) / (2 * g))


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
