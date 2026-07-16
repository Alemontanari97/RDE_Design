#!/usr/bin/env python3
"""phase_diagram.py — OP-11-eps: the quasi-1D (eps-level) topology phase
diagram of the cycle-averaged nozzle problem.

Plan anchor: [F1/OP-11-eps] (docs/rde_nozzle_development_plan.md Phase A2
first-science preview at the eps rung; conjecture OP-11 "the measure
selects the topology", M0 Part I discovery (3) and Prop. 7 corollary).
The proven limits interpolated here are theorems of record:
  spread -> 0        ==>  sectors tie at the Rao-at-<Pc> value   (T3),
  generous envelope  ==>  free boundary attains the ceiling      (T4/M1),
  vacuum             ==>  no finite optimum                      (Thm 3),
  subcritical phases ==>  ceiling CAPPED AT THE SONIC STATE      (Prop. 7
                          sharpening of record, OP-0 / bounds.py).

THE GRID. Cells (eps_max, PR): envelope cap eps_max (the one geometric
constraint representable at the eps rung; a length axis L needs contour
geometry, Phase A1+ — declared scope limit) x blowdown spread PR at FIXED
cycle-mean pressure <Pc>_mu (log-uniform measure, Lemma O2): P0(PR) =
<Pc> / I1(PR), I1 = (1 - PR^-1)/ln PR (I1(1) := 1, the degenerate
single-phase measure).  Gas anchor: one blessed Table-1 state (gamma,
c*) with c*0 rescaled along the SAME products isentrope,
c*0(P0) = c*0_bless (P0/P0_bless)^((g-1)/2g).  <Pc> is the blessed
cycle's own mean, so the blessed PR is a grid point and the cell there
must reproduce data/bounds_ladder.json (cross-anchor, tested).

CANDIDATES per cell (closed forms, st_core Eqs. 9-12 + bounds.py):
  bell        fixed full-flowing bell at eps_bell = min(eps*(<Pc>), eps_max),
              the T3/Theorem-1 optimum under the cap (cycle unimodality in
              eps: tests/test_bell_optimality.py).
  plug_sh     S-H spike closure VERBATIM (Eqs. 10-12) at
              eps_plug = min(knee, eps_max), knee = eps*(P0): the published
              ideal-adaptation closure, whose free branch is the NAIVE
              complete-expansion form — not admissible on subcritical
              phases (module CHOKING CAP of bounds.py).
  plug        the closure OF RECORD (capped adaptation): bell branch while
              underexpanded at eps_plug, per-phase CAPPED ideal (complete
              expansion to Pa above NPR(1,g), sonic exit below) once
              released.  THEOREM (eps-level, closed forms + Theorem-1
              unimodality): plug >= bell and plug >= plug_sh POINTWISE in
              every phase, hence in the mu-average — under this closure the
              bell never strictly wins a cell; at eps_max >= knee the capped
              plug equals the int-max rung pointwise and therefore ATTAINS
              the capped ceiling (M1 gap-zero) on EVERY Pa > 0 cell,
              INCLUDING subcritical cycles — extending OP-0's attainment
              record (8 supercritical rows) to the whole capped class.
              Back-propagated to M0 Prop. 7 corollary / D3 (R4).

WINNER per cell: tie if |plug - bell| <= tol_abs (derived roundoff
tolerance, NQ*eps_mach — no magic numbers), else the argmax; label
'plug' when the knee fits the envelope (eps_max >= knee), 'plug-capped'
when the cap binds (the genuinely averaged regime, PB-2 preview).  A
'bell' winner is IMPOSSIBLE under the closure of record (theorem above);
check_cell treats it as a violation, and the published-closure artifact
that produces it (eps_max -> 1 with subcritical tails, where the naive
free branch loses to the sonic exit) is kept as an executable negative
control in tests/test_phase_diagram.py.

LADDER REUSE. Every cell embeds the full OP-0 ladder row
(bounds.ladder_row, eps_fix = eps_bell) and re-runs bounds.check_chain:
chain C must hold verbatim on every PR > 1 cell; at PR = 1 the measure is
degenerate and check_chain must fail with EXACTLY the strictness
signature {EK-gap} + ({bell-gap} iff the cap does not bind} — the
degeneracy is asserted, not skipped.  Gap-zero vs the capped ceiling
(M1 mechanism) is the per-cell global-optimality certificate.

Hypotheses (inherited, stated): H1-H5 of validation/
bell_optimality_proof.md (frozen gamma, choked feed mdot = Pc A_t/c*,
full-flowing members, exponential blowdown); ideal-adaptation closure for
the plug family (T4/H-T4 with the sonic cap); PR grid capped so that
min-cycle Pc >= Pa (choked-feed edge + gauge validity of the (p - Pa)
closed forms; choke_margin persisted per cell regardless).  Quadrature =
trapezoid on the NQ grid of the blessed pipeline; TOL_REL = NQ*eps_mach.

Usage:
  python src/thrust/phase_diagram.py     # evaluate grid -> data/ + stdout
Outputs: data/phase_diagram.json (numbers of record, consumed by
tests/test_phase_diagram.py and examples/example_phase_diagram.py) and
data/phase_diagram.md (human table).  Figure for P-1: rendered by
examples/example_phase_diagram.py into figs/.
"""
import json
import os
import sys

import numpy as np

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from src.common.constants import G0, P_ATM as ATM
from src.thrust.st_core import TR, Ik, cf_bell, cf_spike, npr_of_eps
from src.thrust.stechmann_nozzle import NQ, dkey, eps_of_npr, load
from src.thrust.bounds import (TOL_REL, cf_ideal, check_chain, ladder_row,
                               npr_sonic)

DIAG_JSON = os.path.join(_ROOT, 'data', 'phase_diagram.json')
DIAG_MD = os.path.join(_ROOT, 'data', 'phase_diagram.md')

# Gas anchor of record: the D3 S5.2 / gamma-probe blessed state (subcritical-
# capable 20-atm hydrocarbon row; its PR is a grid point, see PR_GRID).
ANCHOR = dkey('CH4', 20, 1.64)

# Spread axis: PR at fixed <Pc>.  1 = degenerate measure (T3 oracle);
# 90 = largest octave-ish rung keeping min-cycle Pc >= Pa at <Pc> ~ 20.9 atm
# (Pc_min/Pa = <Pc>/Pa * ln PR/(PR-1) = 1.05 there; 128 would cross 1).
# The blessed PR is inserted at build time (see grids()).
PR_GRID = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 90.0]

# Envelope axis: eps_max from the sonic annulus (1.0, where bell and plug
# coincide geometrically) past the largest knee on the grid (~12.9 at
# PR = 90), so both the capped and the attained regimes are populated.
EPS_MAX_GRID = [1.0, 1.5, 2.0, 3.0, 4.5, 7.0, 10.0, 14.0, 20.0, 30.0]

# Vacuum oracle sweep (Pa = 0, blessed PR): geometric eps ladder exposing
# the strictly-increasing, ceiling-unattained tail (no finite optimum).
VAC_EPS_GRID = [5.0, 20.0, 80.0, 320.0]


def i1(PR):
    """Cycle mean of Pc/P0 under log-uniform blowdown; I1(1) = 1 limit."""
    return 1.0 if PR == 1.0 else float(Ik(PR, 1))


def state_at(anchor, PR, Pc_mean):
    """Synthetic blowdown state at spread PR and fixed cycle mean Pc_mean,
    on the anchor's products isentrope (c* ~ P^((g-1)/2g))."""
    g = anchor['gamma']
    P0 = Pc_mean / i1(PR)
    cs0 = anchor['cstar0'] * (P0 / anchor['P0']) ** ((g - 1) / (2 * g))
    return dict(gamma=g, PR=PR, P0=P0, cstar0=cs0)


def cf_plug_capped(g, eps_arg, Pc, Pa):
    """The plug closure OF RECORD: S-H bell branch while underexpanded at
    eps_arg, per-phase CAPPED ideal (bounds.cf_ideal: complete expansion
    to Pa on the supersonic branch, sonic exit below critical) once
    released.  Equals cf_spike wherever the released phase is
    supercritical; strictly above it on released subcritical phases."""
    NPR = npr_of_eps(eps_arg, g)
    Pc = np.asarray(Pc, dtype=float)
    return np.where(Pc / NPR > Pa,
                    cf_bell(g, eps_arg, Pc, Pa, NPR), cf_ideal(g, Pc, Pa))


def _isp_of(s, Pa, cf_vals, n=NQ):
    """Mass-weighted cycle Isp (Eq. 4 route of bounds.ladder_row) of a
    per-phase CF array on the blessed NQ trapezoid grid."""
    g = s['gamma']
    xi = np.linspace(0.0, 1.0, n)
    Pc = s['P0'] * s['PR'] ** (-xi)
    cs = s['cstar0'] * (Pc / s['P0']) ** ((g - 1) / (2 * g))
    md = Pc / cs
    return float(TR(Pc * cf_vals, xi) / (G0 * TR(md, xi)))


# ------------------------------------------------------------------ one cell
def cell_row(anchor, PR, eps_max, Pa, Pc_mean, n=NQ):
    """Evaluate one (eps_max, PR) cell: OP-0 ladder row + the three
    topology candidates + winner + M1 gap-zero certificate."""
    s = state_at(anchor, PR, Pc_mean)
    g = s['gamma']
    xi = np.linspace(0.0, 1.0, n)
    Pc = s['P0'] * s['PR'] ** (-xi)

    eps_star = eps_of_npr(max(Pc_mean / Pa, npr_sonic(g)), g)
    eps_bell = min(eps_star, eps_max)
    knee = eps_of_npr(s['P0'] / Pa, g)
    eps_plug = min(knee, eps_max)

    row = ladder_row(s, Pa, eps_bell, n=n)
    cand = dict(
        bell=row['Isp']['bell'],
        plug_sh=_isp_of(s, Pa, cf_spike(g, eps_plug, Pc, Pa), n),
        plug=_isp_of(s, Pa, cf_plug_capped(g, eps_plug, Pc, Pa), n))

    row.update(eps_max=eps_max, eps_star=float(eps_star),
               eps_bell=float(eps_bell), eps_knee=float(knee),
               eps_plug_used=float(eps_plug), cand=cand,
               knee_fits=bool(eps_max >= knee))
    row['winner'] = winner_of(row)
    best = max(cand['bell'], cand['plug'])
    row['m1_gap'] = row['Isp']['ideal'] - best
    row['m1_gap_zero'] = bool(row['m1_gap'] <= row['tol_abs'])
    return row


def winner_of(row):
    """Winning topology of one cell from its candidates: 'tie' within the
    derived roundoff tolerance, else argmax; a strict plug win is labeled
    by whether the knee fits the envelope.  'bell' is returned only if the
    dominance theorem is violated (broken closure) — check_cell rejects."""
    c, tol = row['cand'], row['tol_abs']
    if abs(c['plug'] - c['bell']) <= tol:
        return 'tie'
    if c['plug'] > c['bell']:
        return 'plug' if row['knee_fits'] else 'plug-capped'
    return 'bell'


def expected_pr1_violations(row):
    """The exact check_chain strictness signature of the degenerate
    (PR = 1) measure: u_eff is constant so the EK gap collapses; the bell
    gap collapses iff the cap does not bind (bell == int-max there)."""
    exp = ['strictness: EK gap below resolution (u_eff constant?)']
    if row['eps_bell'] == row['eps_star']:
        exp = ['strictness: bell gap below resolution'] + exp
    return exp


def check_cell(row):
    """Verify one Pa > 0 cell: candidate/ladder consistency, the dominance
    theorem, winner-label discipline, the T3/T4/M1 oracle relations and
    the chain-C reuse.  Returns (ok, violations); tests/test_phase_diagram
    .py uses it BOTH ways (must pass every shipped cell, must fail every
    corrupted one)."""
    v = []
    t, c, I = row['tol_abs'], row['cand'], row['Isp']
    if not abs(c['bell'] - I['bell']) <= t:
        v.append('internal: bell candidate != ladder bell rung')
    if not (c['plug'] >= c['bell'] - t and c['plug'] >= c['plug_sh'] - t):
        v.append('dominance: capped plug beaten (closure theorem violated)')
    if row['winner'] != winner_of(row):
        v.append('winner label inconsistent with candidates')
    if row['winner'] == 'bell':
        v.append('bell winner: impossible under the capped closure')
    best = max(c['bell'], c['plug'])
    if not best <= I['ideal'] + t:
        v.append('winner above the capped ceiling')
    if row['m1_gap_zero'] != (I['ideal'] - best <= t):
        v.append('m1 flag inconsistent with the recomputed gap')
    if row['knee_fits'] and not row['m1_gap_zero']:
        v.append('T4/M1: generous envelope fails to attain capped ceiling')
    if row['PR'] == 1.0:
        if row['winner'] != 'tie':
            v.append('T3: zero spread must tie')
        good, viol = check_chain(row)
        if viol != expected_pr1_violations(row):
            v.append('PR=1: degenerate chain signature mismatch: %r' % viol)
    else:
        good, viol = check_chain(row)
        if not good:
            v.append('chain C violated: ' + '; '.join(viol))
        if row['frac_sonic'] > 0 and not c['plug_sh'] < c['plug'] - t:
            v.append('subcritical: naive-branch loss unresolved')
    return (not v), v


def check_vacuum(rows):
    """Vacuum oracle (Theorem 3, no finite optimum): each point ties
    (spike degenerates to the bell at the cap), stays strictly below the
    ceiling, and the value is strictly increasing along the eps ladder.
    Returns (ok, violations); rejector-tested like check_cell."""
    v = []
    for r in rows:
        t, c, I = r['tol_abs'], r['cand'], r['Isp']
        if not abs(c['plug'] - c['bell']) <= t:
            v.append('vacuum eps=%g: bell/plug not degenerate' % r['eps_max'])
        if not max(c['bell'], c['plug']) < I['ideal'] - t:
            v.append('vacuum eps=%g: ceiling attained at finite eps'
                     % r['eps_max'])
        good, viol = check_chain(r)
        if not good:
            v.append('vacuum eps=%g: chain C violated: %s'
                     % (r['eps_max'], '; '.join(viol)))
    vals = [max(r['cand']['bell'], r['cand']['plug']) for r in rows]
    if not all(b > a + rows[0]['tol_abs'] for a, b in zip(vals, vals[1:])):
        v.append('vacuum: Isp not strictly increasing in eps_max')
    return (not v), v


# ------------------------------------------------------------------- driver
def grids(anchor):
    """The PR grid with the blessed spread inserted (cross-anchor cell)."""
    PRs = sorted(set(PR_GRID) | {float(anchor['PR'])})
    return PRs, list(EPS_MAX_GRID)


def evaluate_all():
    """The OP-11-eps phase diagram on the anchor state: full (eps_max, PR)
    grid at sea level + the vacuum oracle sweep.  Persists
    data/phase_diagram.json + data/phase_diagram.md."""
    anchor = load()['states'][ANCHOR]
    Pc_mean = anchor['P0'] * i1(anchor['PR'])
    PRs, EMs = grids(anchor)
    Pa = ATM

    cells, nok = [], 0
    for PR in PRs:
        for em in EMs:
            row = cell_row(anchor, PR, em, Pa, Pc_mean)
            ok, viol = check_cell(row)
            row['cell_ok'], row['violations_cell'] = ok, viol
            nok += ok
            cells.append(row)
        last = [r for r in cells if r['PR'] == PR]
        print('PR %8.2f: %s' % (PR, ' '.join(
            {'tie': 'T', 'plug': 'P', 'plug-capped': 'c',
             'bell': 'B'}[r['winner']] + ('*' if r['m1_gap_zero'] else ' ')
            for r in last)), flush=True)

    vac = []
    sv = state_at(anchor, anchor['PR'], Pc_mean)
    for em in VAC_EPS_GRID:
        r = ladder_row(sv, 0.0, em)
        g, Pc = sv['gamma'], sv['P0'] * sv['PR'] ** (-np.linspace(0, 1, NQ))
        r.update(eps_max=em, cand=dict(
            bell=r['Isp']['bell'],
            plug_sh=_isp_of(sv, 0.0, cf_spike(g, em, Pc, 0.0)),
            plug=_isp_of(sv, 0.0, cf_spike(g, em, Pc, 0.0))))
        vac.append(r)
    vac_ok, vac_viol = check_vacuum(vac)

    rec = dict(
        provenance='src/thrust/phase_diagram.py evaluate_all() on the '
                   'blessed anchor state %s of data/st_nozzle_opt.json; '
                   '[F1/OP-11-eps]; candidates/winner per module docstring'
                   % ANCHOR,
        anchor=dict(key=ANCHOR, gamma=anchor['gamma'], P0=anchor['P0'],
                    PR=anchor['PR'], cstar0=anchor['cstar0'],
                    Pc_mean=Pc_mean),
        definitions=dict(
            bell='fixed full-flowing bell at min(eps*(<Pc>), eps_max) '
                 '(T3/Theorem-1 optimum under the cap)',
            plug_sh='S-H spike closure verbatim (Eqs. 10-12) at '
                    'min(knee, eps_max) — naive free branch, kept for the '
                    'executable rejection',
            plug='capped-adaptation closure of record: released phases at '
                 'the per-phase CAPPED ideal (sonic cap below critical)',
            winner='tie within tol_abs, else argmax; plug labeled '
                   '"plug-capped" when eps_max < knee',
            m1_gap_zero='winner attains the capped ceiling within tol_abs '
                        '(duality-gap-zero global optimality, mechanism M1)'),
        tol_rel=TOL_REL, n=NQ, Pa_atm=1.0, pr_grid=PRs, eps_max_grid=EMs,
        vac_eps_grid=list(VAC_EPS_GRID), cells=cells,
        vacuum=dict(rows=vac, ok=vac_ok, violations=vac_viol))
    with open(DIAG_JSON, 'w') as f:
        json.dump(rec, f, indent=1)
    _write_md(rec)
    print('phase diagram: %d/%d cells OK, vacuum oracle %s -> %s'
          % (nok, len(cells), 'OK' if vac_ok else 'VIOLATED', DIAG_JSON),
          flush=True)
    return rec


def _write_md(rec):
    PRs, EMs = rec['pr_grid'], rec['eps_max_grid']
    bykey = {(r['PR'], r['eps_max']): r for r in rec['cells']}
    sym = {'tie': 'tie', 'plug': 'PLUG', 'plug-capped': 'plug-cap',
           'bell': 'BELL!'}
    L = ['# OP-11-eps — quasi-1D topology phase diagram '
         '(winner per (eps_max, PR) cell)',
         '',
         'Anchor %s, <Pc> = %.3f atm fixed, Pa = 1 atm; entry = winner'
         % (rec['anchor']['key'], rec['anchor']['Pc_mean'] / ATM),
         '(+ " *" = capped ceiling attained: M1 duality-gap-zero global '
         'optimality).',
         'Generated by `src/thrust/phase_diagram.py`; record in '
         '`data/phase_diagram.json`;',
         'oracles + rejection: `tests/test_phase_diagram.py`.  Proven '
         'limits: PR = 1 column',
         '= T3 tie at Rao-at-<Pc>; eps_max >= knee rows = T4/M1 '
         'attainment (incl. the',
         'SUBCRITICAL cycles PR >~ 46, via the sonic-capped closure — the '
         'published S-H',
         'free branch leaves a false positive gap there); vacuum sweep = '
         'no finite optimum.',
         '',
         '| eps_max \\ PR | ' + ' | '.join('%g' % p for p in PRs) + ' |',
         '|---' * (len(PRs) + 1) + '|']
    for em in EMs:
        cells = [bykey[(p, em)] for p in PRs]
        L.append('| %g | ' % em + ' | '.join(
            sym[c['winner']] + (' *' if c['m1_gap_zero'] else '')
            for c in cells) + ' |')
    L += ['',
          'Vacuum sweep (blessed PR, Pa = 0): ' + ', '.join(
              'eps %g -> %.1f s' % (r['eps_max'],
                                    max(r['cand'].values()))
              for r in rec['vacuum']['rows'])
          + ' (ceiling %.1f s, unattained).'
          % rec['vacuum']['rows'][0]['Isp']['ideal'],
          '',
          'Knee eps*(P0(PR)) per PR: ' + ', '.join(
              '%g: %.2f' % (p, bykey[(p, EMs[0])]['eps_knee'])
              for p in PRs) + '.',
          'Subcritical strip (choke_margin < 1): PR in {%s}.' % ', '.join(
              '%g' % p for p in PRs
              if bykey[(p, EMs[0])]['subcritical'])]
    with open(DIAG_MD, 'w') as f:
        f.write('\n'.join(L) + '\n')


if __name__ == '__main__':
    evaluate_all()
    print('OK', flush=True)
