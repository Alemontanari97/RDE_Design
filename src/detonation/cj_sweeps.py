"""cj_sweeps.py — functional-dependence sweeps of the CJ state via the SD Toolbox.

Lecture-repo edition of project_build/scripts/sweep_sdt.py (verbatim numerics;
paths made repo-relative).

Computes U_CJ, p_CJ/p1, T_CJ with CJspeed + PostShock_eq (equilibrium products,
GRI-Mech 3.0) as functions of:
  1. equivalence ratio phi (H2/CH4/C2H4 in air, phi = 0.6 ... 1.8) — the flat
     maximum slightly rich of stoichiometric;
  2. N2 dilution beta = N2/O2 of stoichiometric H2/O2 (beta = 0 ... 7);
  3. initial pressure P1 (0.2 ... 10 atm, H2/air) — weak log dependence;
  4. initial temperature T1 (250 ... 1000 K, H2/air) — U_CJ nearly flat,
     p_CJ/p1 drops ~ 1/T1 (density effect).

These are the lecture's "what controls U_CJ" figures (deck section 2).
Results accumulate in data/sweep_sdt.json (resumable: each completed block is
skipped on re-run; delete the file to force a full recompute, ~10-20 min).

Usage:
    python cj_sweeps.py
Expected: 'phi done', 'dilution done', 'P1 done', 'T1 done' as blocks finish;
U_CJ(H2/air, phi=1) = 1969 m/s appears inside the phi block.
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # repo root
sys.path.insert(0, ROOT)                               # vendored sdtoolbox/
import cantera as ct, numpy as np
from sdtoolbox.postshock import CJspeed, PostShock_eq

ct.suppress_thermo_warnings()
mech = 'gri30.yaml'; P0 = ct.one_atm; T0 = 300.0
OUT = os.path.join(ROOT, 'data', 'sweep_sdt.json')

def cj_state(q, P1, T1):
    U = CJspeed(P1, T1, q, mech); g = PostShock_eq(U, P1, T1, q, mech)
    return U, g.P/P1, g.T

def phi_mix(fuel, ox_o2, ox_n2, phi):
    # stoich O2 per fuel: H2->0.5, CH4->2, C2H4->3
    st = {'H2': 0.5, 'CH4': 2.0, 'C2H4': 3.0}[fuel]
    o2 = st/phi
    d = {fuel: 1.0, 'O2': o2}
    if ox_n2: d['N2'] = o2*3.76
    return ' '.join(f'{k}:{v}' for k, v in d.items())

res = json.load(open(OUT)) if os.path.exists(OUT) else {}
def save(): json.dump(res, open(OUT, 'w'))

if __name__ == '__main__':
    # 1) U_CJ vs phi (3 fuels, air)
    if 'phi' not in res:
        res['phi'] = {}
        for fuel in ['H2', 'CH4', 'C2H4']:
            xs = []; us = []; ts = []; ps = []
            for phi in [0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]:
                U, pr, T = cj_state(phi_mix(fuel, 1, 1, phi), P0, T0)
                xs.append(phi); us.append(U); ts.append(T); ps.append(pr)
            res['phi'][fuel] = dict(phi=xs, U=us, T=ts, p=ps); save()
        print('phi done', flush=True)
    # 2) U_CJ,T vs N2 dilution (H2/O2 with increasing N2/O2 ratio, stoich)
    if 'dilution' not in res:
        beta = [0, 1, 2, 3.76, 5, 7]; us = []; ts = []; ps = []
        for b in beta:
            q = f'H2:2 O2:1 N2:{b}'; U, pr, T = cj_state(q, P0, T0)
            us.append(U); ts.append(T); ps.append(pr)
        res['dilution'] = dict(beta=beta, U=us, T=ts, p=ps); save(); print('dilution done', flush=True)
    # 3) U_CJ vs initial pressure (H2/air stoich)
    if 'P1' not in res:
        Ps = [0.2, 0.5, 1.0, 2.0, 5.0, 10.0]; us = []; ts = []; ps = []
        for P in Ps:
            U, pr, T = cj_state('H2:2 O2:1 N2:3.76', P*ct.one_atm, T0)
            us.append(U); ts.append(T); ps.append(pr)
        res['P1'] = dict(P_atm=Ps, U=us, T=ts, p=ps); save(); print('P1 done', flush=True)
    # 4) U_CJ vs initial temperature (H2/air stoich)
    if 'T1' not in res:
        Ts = [250, 300, 400, 500, 700, 1000]; us = []; ts = []; ps = []
        for T in Ts:
            U, pr, T2 = cj_state('H2:2 O2:1 N2:3.76', P0, T)
            us.append(U); ts.append(T2); ps.append(pr)
        res['T1'] = dict(T1=Ts, U=us, T=ts, p=ps); save(); print('T1 done', flush=True)
    print('ALL SWEEPS DONE', {k: 'ok' for k in res})
