#!/usr/bin/env python3
"""example_phase_diagram.py — OP-11-eps: compute the quasi-1D topology
phase diagram LIVE and render the P-1 figure.

Runs src/thrust/phase_diagram.evaluate_all() (regenerates the record in
data/phase_diagram.{json,md} — idempotent, ~seconds) and renders
figs/phase_diagram_op11.png: (a) the winner map over (PR, eps_max) with
the knee curve eps*(P0(PR)), the Rao line eps*(<Pc>) and the subcritical
strip; (b) the gap to the CAPPED ceiling (M1 certificate: white = zero
gap = certified global optimum of the eps-level class).

Run:      python examples/example_phase_diagram.py         (~5 s)
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from src.style import GOLD, LGRAY, NAVY, RED, TEAL, save  # noqa: E402 (rcParams)
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap, ListedColormap
from matplotlib.patches import Patch

from src.thrust.phase_diagram import evaluate_all
from src.thrust.stechmann_nozzle import eps_of_npr
from src.common.constants import P_ATM as ATM


def edges(vals):
    """Geometric cell edges around an irregular positive grid."""
    v = np.asarray(vals, dtype=float)
    mid = np.sqrt(v[:-1] * v[1:])
    lo = v[0] ** 2 / mid[0]
    hi = v[-1] ** 2 / mid[-1]
    return np.concatenate([[lo], mid, [hi]])


def main():
    rec = evaluate_all()
    PRs, EMs = rec['pr_grid'], rec['eps_max_grid']
    bykey = {(r['PR'], r['eps_max']): r for r in rec['cells']}
    cat = {'tie': 0, 'plug-capped': 1, 'plug': 2}
    W = np.array([[cat[bykey[(p, e)]['winner']] for p in PRs] for e in EMs])
    Gap = np.array([[bykey[(p, e)]['m1_gap'] for p in PRs] for e in EMs])
    nm1 = sum(1 for r in rec['cells'] if r['m1_gap_zero'])
    counts = [int((W == k).sum()) for k in (0, 1, 2)]
    print('winner map %d cells: %d tie / %d plug-capped / %d plug-knee'
          % (len(rec['cells']), counts[0], counts[1], counts[2]))
    print('M1 gap-zero (capped ceiling attained) on %d cells' % nm1)
    pmax = max(rec['cells'], key=lambda r: r['premium_bound'])
    print('premium bound (ideal - bell, most ANY non-bell sector can earn):'
          ' max %.1f s at (PR=%g, eps_max=%g); winners rank closures, not'
          ' hardware - see SCOPE note in data/phase_diagram.md'
          % (pmax['premium_bound'], pmax['PR'], pmax['eps_max']))
    sub = sorted({r['PR'] for r in rec['cells'] if r['subcritical']})
    print('subcritical strip: PR in {%s} (capped closure load-bearing)'
          % ', '.join('%g' % p for p in sub))
    v0, v1 = rec['vacuum']['rows'][0], rec['vacuum']['rows'][-1]
    print('vacuum oracle: Isp %.1f -> %.1f s over eps %g -> %g, ceiling'
          ' %.1f s unattained'
          % (max(v0['cand'].values()), max(v1['cand'].values()),
             v0['eps_max'], v1['eps_max'], v0['Isp']['ideal']))

    xe, ye = edges(PRs), edges(EMs)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 4.9), sharey=True)

    # (a) winner map: categorical, identity-ordered colors (tie/capped/knee)
    cmap = ListedColormap([LGRAY, GOLD, TEAL])
    ax1.pcolormesh(xe, ye, W, cmap=cmap,
                   norm=BoundaryNorm([-0.5, 0.5, 1.5, 2.5], 3),
                   edgecolors='white', linewidth=1.2)
    prf = np.geomspace(PRs[0], PRs[-1], 200)
    anchor = rec['anchor']
    g, pcm = anchor['gamma'], anchor['Pc_mean']
    i1 = lambda PR: 1.0 if PR == 1.0 else (1 - 1 / PR) / np.log(PR)
    knee = [eps_of_npr(pcm / i1(p) / ATM, g) for p in prf]
    ax1.plot(prf, knee, color=NAVY, lw=2.2,
             label=r'knee $\varepsilon^*(P_0(PR))$')
    ax1.axhline(eps_of_npr(pcm / ATM, g), color=RED, lw=1.8, ls='--',
                label=r'Rao $\varepsilon^*(\langle P_c\rangle)$')
    pr_sub = next(p for p in prf if p > 1.0
                  and pcm * np.log(p) / (p - 1) / ATM
                  < ((g + 1) / 2) ** (g / (g - 1)))
    ax1.axvline(pr_sub, color=RED, lw=1.6, ls=':',
                label='subcritical tail onset')
    ax1.set_xscale('log'); ax1.set_yscale('log')
    ax1.set_xlabel(r'blowdown spread $PR$ at fixed $\langle P_c\rangle$')
    ax1.set_ylabel(r'envelope cap $\varepsilon_{\max}$')
    ax1.set_title('(a) winning topology')
    handles = [Patch(fc=LGRAY, label='tie (bell $=$ plug)'),
               Patch(fc=GOLD, label='plug, cap-bound (gap $>$ 0)'),
               Patch(fc=TEAL, label='plug at knee (M1 gap-zero)')]
    fig.legend(handles=handles + ax1.get_legend_handles_labels()[0],
               loc='upper center', bbox_to_anchor=(0.5, 0.02), ncol=3,
               framealpha=0.95, fontsize=11)

    # (b) gap to the capped ceiling: sequential single-hue (white -> red)
    cs = LinearSegmentedColormap.from_list('gap', ['#FFFFFF', RED])
    pm = ax2.pcolormesh(xe, ye, Gap, cmap=cs, vmin=0.0,
                        edgecolors='white', linewidth=1.2)
    ax2.plot(prf, knee, color=NAVY, lw=2.2)
    ax2.set_xscale('log'); ax2.set_yscale('log')
    ax2.set_xlabel(r'blowdown spread $PR$ at fixed $\langle P_c\rangle$')
    ax2.set_title('(b) gap to capped ceiling [s]')
    fig.colorbar(pm, ax=ax2, pad=0.02)
    for ax in (ax1, ax2):
        ax.set_xticks(PRs[:1] + PRs[1:-2:2] + PRs[-1:])
        ax.set_xticklabels(['%g' % p for p in
                            PRs[:1] + PRs[1:-2:2] + PRs[-1:]], fontsize=10)
        ax.set_yticks(EMs)
        ax.set_yticklabels(['%g' % e for e in EMs], fontsize=10)
        ax.minorticks_off()
    fig.suptitle('OP-11-$\\varepsilon$: the measure selects the topology '
                 '(anchor %s, $\\langle P_c\\rangle$ = %.1f atm)'
                 % (anchor['key'].replace('|', '/'), pcm / ATM),
                 fontsize=13, y=1.03)
    save(fig, 'phase_diagram_op11')
    print('OK: phase diagram example complete')


if __name__ == '__main__':
    main()
