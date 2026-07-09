#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
q_formal.py — numerical backing for validation/q_formal.md.

Lecture-repo edition of project_build/src/cycles/q_formal.py (verbatim physics;
paths adapted to the repo layout).

Standard-state anchoring (rigor fix 2026-07-09): the formal heat release is
    q_std = sum_i (Y_i,1 - Y_i,2) Dh_f,i(T_ref),   T_ref = 298.15 K,
i.e. formation enthalpies at the STANDARD reference temperature — not at a
generic T1.  The calorimetric difference at any initial state obeys exactly
    h_react(T1,p1) - h_prod(T1,p1) = q_std + int_{T_ref}^{T1} (cp_react - cp_prod) dT'
(frozen product composition; with equilibrium products the same holds up to
composition drift, negligible for T1 <= 700 K here).  The script verifies,
with Cantera (gri30.yaml) at p1 = 1 bar, phi = 1 (H2-air, CH4-air):

 (a)  q_std from formation enthalpies (major products, H2O vapour), computed
      twice — as h_react(298.15) - h_majors(298.15) and as the explicit
      per-species sum (identical to < 1 J/kg).

 (a') the calorimetric difference at T1 = 300 K and T1 = 700 K, both with
      frozen major products, h_react(T1) - h_majors(T1), and with equilibrium
      products, h_react(T1) - h_eq(T1)  (HP -> TP equilibrate); the sensible
      mismatch term I(T1) = int (cp_react - cp_majors) dT' is obtained from
      the identity I = q_frozen(T1) - q_std AND cross-checked by direct
      trapezoid quadrature of the cp difference (201 nodes).

 (b)  q_c = h1(300,p1) - h_prod,eq(300,p1)  (Paper B Eq. 1, h1 - h6; the
      project-wide definition of src/cycles/q_mapping.py and cycles.py) and
      its deviation from q_std: the 298.15 -> 300 K reference shift.

 (c)  context for q_eff vs q_thermo: chemical energy actually converted at
      the CJ plane, sum_i (Y_i,1 - Y_i,CJ) Dh_f,i, with the CJ state from
      PostShock_eq at the stored U_CJ (data/cycles_ws.json, fj_mixtures).

Writes data/q_formal.json. Runs from anywhere (paths resolve relative to this file).
"""
import json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(HERE))          # repo root
sys.path.insert(0, PROJ)                               # vendored sdtoolbox/
import cantera as ct
from sdtoolbox.postshock import PostShock_eq

T1, P1, TREF = 300.0, 1e5, 298.15
T_EVAL = (300.0, 700.0)                        # sensible-term drift diagnostic
MECH = 'gri30.yaml'
CASES = [
    ('H2/air',  'H2:2,O2:1,N2:3.76',  'H2O:2,N2:3.76',        ('H2O', 'N2')),
    ('CH4/air', 'CH4:1,O2:2,N2:7.52', 'CO2:1,H2O:2,N2:7.52',  ('CO2', 'H2O', 'N2')),
]

trapz = getattr(np, 'trapezoid', np.trapz)

def ydict(gas):
    return {s: y for s, y in zip(gas.species_names, gas.Y) if y > 0.0}

def h_at(gas, T, X):
    gas.TPX = T, P1, X
    return gas.enthalpy_mass

def cp_at(gas, T, X):
    gas.TPX = T, P1, X
    return gas.cp_mass

def main():
    gas = ct.Solution(MECH)
    hf = {s: gas.species(s).thermo.h(TREF) / gas.molecular_weights[i]
          for i, s in enumerate(gas.species_names)}          # J/kg, formation @298.15
    cw = json.load(open(os.path.join(PROJ, 'data', 'cycles_ws.json')))
    out = {'meta': {
        'script': 'src/cycles/q_formal.py', 'mech': MECH,
        'T1_K': T1, 'P1_Pa': P1, 'Tref_K': TREF, 'T_eval_K': list(T_EVAL),
        'phi': 1.0,
        'definition': 'q_std = sum_i (Y_i1 - Y_i2) Dhf_i(298.15 K) — STANDARD state; '
                      'h1(T1,p1) - h_prod(T1,p1) = q_std + int_{298.15}^{T1} '
                      '(cp_react - cp_prod) dT (frozen products, exact identity)',
        'routes': {
            'q_std': 'sum_i (Y_i1 - Y_i2) Dhf_i(298.15), major products, H2O vapour',
            'q_frozen_T': 'h_react(T,p1) - h_majors(T,p1), frozen major composition',
            'q_eq_T': 'h_react(T,p1) - h_prod,eq(T,p1)  (HP then TP equilibrate); '
                      'at T = 300 K this is q_c of B1 (h1 - h6)',
            'sens_int': 'I(T) = int_{298.15}^{T} (cp_react - cp_majors) dT: identity '
                        'q_frozen(T) - q_std, cross-checked by 201-node quadrature',
            'cj_plane': 'sum_i (Y_i1 - Y_iCJ) Dhf_i at PostShock_eq(U_CJ, p1, T1)'},
    }, 'cases': {}}
    for label, X, Xp, majors in CASES:
        gas.TPX = TREF, P1, X;  Y1 = ydict(gas)
        h1_ref = gas.enthalpy_mass; cp1 = gas.cp_mass
        gas.TPX = TREF, P1, Xp; Y2 = ydict(gas)
        h2_ref = gas.enthalpy_mass; cp2 = gas.cp_mass
        q_std = h1_ref - h2_ref                                # standard-state q
        q_std_sum = sum((Y1.get(s, 0.0) - Y2.get(s, 0.0)) * hf[s]
                        for s in set(Y1) | set(Y2))            # explicit sum
        assert abs(q_std_sum - q_std) < 1.0, (q_std_sum, q_std)  # < 1 J/kg
        c = dict(X=X, X_majors=Xp,
                 q_std_MJkg=q_std / 1e6, q_std_sum_MJkg=q_std_sum / 1e6,
                 # legacy aliases (kept for downstream compatibility)
                 q_a_hf298_MJkg=q_std / 1e6, q_a_sum_MJkg=q_std_sum / 1e6,
                 cp_react_298_JkgK=cp1, cp_majors_298_JkgK=cp2, at_T={})
        for T in T_EVAL:
            q_frz = h_at(gas, T, X) - h_at(gas, T, Xp)         # frozen majors
            # equilibrium products at (T,p1): HP -> TP for robustness
            gas.TPX = T, P1, X
            gas.equilibrate('HP'); gas.TP = T, P1; gas.equilibrate('TP')
            q_eq = h_at(ct.Solution(MECH), T, X) - gas.enthalpy_mass
            Xeq = {s: x for s, x in zip(gas.species_names, gas.X) if x > 0.0}
            minors = {s: x for s, x in Xeq.items() if s not in majors}
            max_minor = max(minors.values()) if minors else 0.0
            I_ident = q_frz - q_std                            # exact identity
            Ts = np.linspace(TREF, T, 201)
            dcp = np.array([cp_at(gas, t, X) - cp_at(gas, t, Xp) for t in Ts])
            I_quad = trapz(dcp, Ts)                            # independent check
            assert abs(I_quad - I_ident) < max(2.0, 1e-4 * abs(I_ident)), \
                (T, I_quad, I_ident)
            c['at_T'][f'{T:.0f}'] = dict(
                q_frozen_MJkg=q_frz / 1e6, q_eq_MJkg=q_eq / 1e6,
                sens_int_kJkg=I_ident / 1e3, sens_int_quad_kJkg=I_quad / 1e3,
                shift_vs_qstd=I_ident / q_std,
                dev_eq_vs_frozen=(q_eq - q_frz) / q_frz,
                max_minor_X_eq=max_minor,
                dcp_react_minus_prod_at_T_JkgK=float(dcp[-1]))
            print(f"{label} @ {T:.0f} K: q_frozen = {q_frz/1e6:.5f}  q_eq = "
                  f"{q_eq/1e6:.5f} MJ/kg | I = {I_ident/1e3:+.3f} kJ/kg "
                  f"(quad {I_quad/1e3:+.3f}) = {100*I_ident/q_std:+.4f}% of q_std | "
                  f"eq-frz = {100*c['at_T'][f'{T:.0f}']['dev_eq_vs_frozen']:+.2e}% "
                  f"| max minor X = {max_minor:.2e}")
        # (b) aliases at the project initial state T1 = 300 K
        a300 = c['at_T']['300']
        c.update(q_b_eq_MJkg=a300['q_eq_MJkg'], q_a_T1_MJkg=a300['q_frozen_MJkg'],
                 dev_std_vs_b=(q_std / 1e6 - a300['q_eq_MJkg']) / a300['q_eq_MJkg'],
                 dev_a_vs_b=(q_std / 1e6 - a300['q_eq_MJkg']) / a300['q_eq_MJkg'],
                 dev_aT1_vs_b=(a300['q_frozen_MJkg'] - a300['q_eq_MJkg'])
                              / a300['q_eq_MJkg'],
                 ref_shift_Jkg=a300['sens_int_kJkg'] * 1e3,
                 max_minor_X_eq_T1=a300['max_minor_X_eq'])
        print(f"{label}: q_std(298.15) = {q_std/1e6:.5f}  q_c(300) = "
              f"{a300['q_eq_MJkg']:.5f} MJ/kg | q_std - q_c = "
              f"{100*c['dev_std_vs_b']:+.4f}%")
        # (c) CJ plane: dissociation withholds part of q_c
        ucj = cw['fj_mixtures'][label]['U_CJ']
        gcj = PostShock_eq(ucj, P1, T1, X, MECH)
        Ycj = ydict(gcj)
        q_cj = sum((Y1.get(s, 0.0) - Ycj.get(s, 0.0)) * hf[s]
                   for s in set(Y1) | set(Ycj))
        Xcj = {s: x for s, x in zip(gcj.species_names, gcj.X) if x > 1e-4}
        diss = {s: round(x, 5) for s, x in sorted(Xcj.items(), key=lambda kv: -kv[1])
                if s not in majors}
        c.update(U_CJ=ucj, T_CJ=gcj.T, P_CJ_bar=gcj.P / 1e5,
                 q_CJplane_MJkg=q_cj / 1e6,
                 frac_released_at_CJ=q_cj / (a300['q_eq_MJkg'] * 1e6),
                 dissociated_at_CJ_X=diss)
        out['cases'][label] = c
        print(f"   CJ plane: T = {gcj.T:.0f} K, p = {gcj.P/1e5:.1f} bar, released "
              f"{q_cj/1e6:.3f} MJ/kg = {100*c['frac_released_at_CJ']:.1f}% of q_c; "
              f"dissociated: {diss}")
    with open(os.path.join(PROJ, 'data', 'q_formal.json'), 'w') as f:
        json.dump(out, f, indent=1, default=float)
    print('[q_formal] wrote data/q_formal.json')

if __name__ == '__main__':
    main()
