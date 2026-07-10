"""mixtures.py — THE mixture registry (single source of truth, 12 mixtures).

One entry per stoichiometric propellant pair used anywhere in the package:
Cantera composition string (exact integer/rational ratios — the canonical
composition input for every CJ computation), mechanism, display names,
fuel/oxidizer split (for set_equivalence_ratio-style consumers), the
Shepherd–Kasahara K factor of the pressure-history model, and the CxHy
bookkeeping used by the q-mapping module.

Consumers (thin views, see validation/interface_audit.md §5):
  * src/cycles/cycles.py      MIXTURES  = [(label, X, mech_path), ...]
  * src/cycles/q_mapping.py   MIX       = [(label, X, mech_path, xy), ...]
  * src/thrust/sk_models.py   CASES     = {key: dict(mech, fuel, ox, K), ...}
  * src/common/cj_core.py     cj_state(mix, ...) accepts any key/alias

`src/thrust/stechmann_nozzle.PROPS` is deliberately NOT a view of this
registry: it is the Stechmann-paper propellant set (fuel–O2 at the paper's
optimum equivalence ratios, reduced CHO/dodecane mechanisms chosen for the
matched-cycle iteration speed). It cross-references this module in its
docstring instead.

Label aliases: the cycle suite historically says 'kerosene/…', the thrust
suite 'C12H26/…' — both resolve to the same entry via ALIASES.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(_HERE))          # repo root
DODEQ = os.path.join(ROOT, 'data', 'dodecane_eq_thermo.yaml')
GRI = 'gri30.yaml'
AIR, AIRD = 'O2:1,N2:3.76', 'o2:1,n2:3.76'

# K (SK pressure-history, Eqs. 14-18): 1.02 fuel-air (alpha=0.98),
# 1.54 fuel-O2 (alpha=0.65).  xy = (x, y, n_fuel) for CxHy major products.
# X strings: exact stoichiometric ratios (canonical CJ input, Finding MIX-2).
MIXTURES = {
    'H2/air':      dict(X='H2:2,O2:1,N2:3.76',          mech=GRI,   fuel='H2',     ox=AIR,  K=1.02, xy=(0, 2, 2.0),   display='H2/air'),
    'H2/O2':       dict(X='H2:2,O2:1',                  mech=GRI,   fuel='H2',     ox='O2', K=1.54, xy=(0, 2, 2.0),   display='H2/O2'),
    'CH4/air':     dict(X='CH4:1,O2:2,N2:7.52',         mech=GRI,   fuel='CH4',    ox=AIR,  K=1.02, xy=(1, 4, 1.0),   display='CH4/air'),
    'CH4/O2':      dict(X='CH4:1,O2:2',                 mech=GRI,   fuel='CH4',    ox='O2', K=1.54, xy=(1, 4, 1.0),   display='CH4/O2'),
    'C2H4/air':    dict(X='C2H4:1,O2:3,N2:11.28',       mech=GRI,   fuel='C2H4',   ox=AIR,  K=1.02, xy=(2, 4, 1.0),   display='C2H4/air'),
    'C2H4/O2':     dict(X='C2H4:1,O2:3',                mech=GRI,   fuel='C2H4',   ox='O2', K=1.54, xy=(2, 4, 1.0),   display='C2H4/O2'),
    'C2H2/air':    dict(X='C2H2:1,O2:2.5,N2:9.4',       mech=GRI,   fuel='C2H2',   ox=AIR,  K=1.02, xy=(2, 2, 1.0),   display='C2H2/air'),
    'C2H2/O2':     dict(X='C2H2:1,O2:2.5',              mech=GRI,   fuel='C2H2',   ox='O2', K=1.54, xy=(2, 2, 1.0),   display='C2H2/O2'),
    'C3H8/air':    dict(X='C3H8:1,O2:5,N2:18.8',        mech=GRI,   fuel='C3H8',   ox=AIR,  K=1.02, xy=(3, 8, 1.0),   display='C3H8/air'),
    'C3H8/O2':     dict(X='C3H8:1,O2:5',                mech=GRI,   fuel='C3H8',   ox='O2', K=1.54, xy=(3, 8, 1.0),   display='C3H8/O2'),
    'C12H26/air':  dict(X='c12h26:1,o2:18.5,n2:69.56',  mech=DODEQ, fuel='c12h26', ox=AIRD, K=1.02, xy=(12, 26, 1.0), display='Kerosene(C12H26)/air'),
    'C12H26/O2':   dict(X='c12h26:1,o2:18.5',           mech=DODEQ, fuel='c12h26', ox='o2', K=1.54, xy=(12, 26, 1.0), display='Kerosene(C12H26)/O2'),
}

ALIASES = {'kerosene/air': 'C12H26/air', 'kerosene/O2': 'C12H26/O2'}

ORDER = list(MIXTURES)                                   # canonical key order


def resolve(key):
    """Canonical key for `key` (alias-aware); KeyError with the known list."""
    k = ALIASES.get(key, key)
    if k not in MIXTURES:
        raise KeyError('unknown mixture %r — known: %s (aliases: %s)'
                       % (key, ', '.join(MIXTURES), ', '.join(ALIASES)))
    return k


def get(key):
    """Registry entry (dict) for a canonical key or alias."""
    return MIXTURES[resolve(key)]


def cycle_label(key):
    """Label as used by the cycle suite ('kerosene/…' for C12H26)."""
    k = resolve(key)
    inv = {v: a for a, v in ALIASES.items()}
    return inv.get(k, k)


def cycles_view():
    """[(label, X, mech), ...] — the historical cycles.MIXTURES layout."""
    return [(cycle_label(k), m['X'], m['mech']) for k, m in MIXTURES.items()]


def q_mapping_view():
    """[(label, X, mech, xy), ...] — the historical q_mapping.MIX layout."""
    return [(cycle_label(k), m['X'], m['mech'], m['xy'])
            for k, m in MIXTURES.items()]


def sk_cases_view():
    """{key: dict(mech, fuel, ox, K)} — the historical sk_models.CASES core
    (the SKREP:* replicas are added by sk_models itself)."""
    return {k: dict(mech=m['mech'], fuel=m['fuel'], ox=m['ox'], K=m['K'])
            for k, m in MIXTURES.items()}
