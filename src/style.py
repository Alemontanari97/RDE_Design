"""Shared matplotlib style for all lecture figures (colors, fonts, save helper).

Repo edition of project_build/scripts/style.py: identical rcParams and palette;
save() now writes into the repo-local figs/ directory (created on demand)
instead of a hard-coded absolute path, so the repo is self-contained.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

RED = '#822433'; TEAL = '#006778'; GRAY = '#2B2B2B'
LGRAY = '#B2B2B2'; GOLD = '#B8860B'; NAVY = '#1F3B5B'

plt.rcParams.update({
    'font.family': 'serif', 'font.serif': ['DejaVu Serif'], 'mathtext.fontset': 'cm',
    'font.size': 15, 'axes.edgecolor': GRAY, 'axes.labelcolor': GRAY, 'text.color': GRAY,
    'xtick.color': GRAY, 'ytick.color': GRAY, 'axes.linewidth': 1.3, 'figure.dpi': 150,
    'axes.labelsize': 16, 'legend.fontsize': 13, 'axes.titlesize': 16})

FIGS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figs')


def save(fig, name):
    os.makedirs(FIGS, exist_ok=True)
    fig.savefig(os.path.join(FIGS, name + '.png'),
                dpi=200, bbox_inches='tight', facecolor='white', pad_inches=0.12)
    plt.close(fig)
    print('saved', os.path.join('figs', name + '.png'))
