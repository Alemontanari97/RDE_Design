#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
q_mapping.py — formal definition and mixture traceability of the heat release q
in the Wintenberger–Shepherd cycle analysis (AIAA 2004-1033 = Paper A;
JPP 22(3):694-698, 2006 = Paper B).  Companion to src/cycles/cycles.py.
Lecture-repo edition of project_build/src/cycles/q_mapping.py (verbatim physics;
paths adapted to the repo layout).

DEFINITION (Paper B, Eq. B1; Paper A, Eq. A3 with ambient = standard state):
    q_c = h_1(T1,P1) - h_6(T1,P1)
i.e. specific enthalpy of the reactants minus that of the *equilibrium* products
at the same initial (T1,P1).  At T1 = 300 K equilibrium composition reduces to
the major products (CO2, H2O vapour, N2), so q_c coincides with the classical
formation-enthalpy heat of combustion (lower heating value basis, per unit
mass of mixture); this script computes both and reports the deviation.
Standard-state anchor (2026-07-09): the formal q° is defined at T_ref = 298.15 K; exactly
q_c(T1) = q° + int_{Tref}^{T1} (cp_react - cp_prod) dT  (see validation/q_formal.md);
at T1 = 300 K the shift is -0.0076%/+0.0023% (H2/CH4-air), percent-grade at 700 K.

NON-DIMENSIONAL FORMS used by the papers (all verified against the spec):
    q~   = q_c/(cp T1)    classical Hugoniot & FJ closed form (A18, A21, B2-B3)
    q~_t = q_c/(cp Tt1)   stagnation Hugoniot (A40-A42), existence limit
                          q~_t < 1/(gamma^2-1)
    q_c/(R T1) = gamma/(gamma-1) * q~     Fig. A22 family labels (10,20,30,40)

ONE-GAMMA CJ RELATION AND ITS EXACT INVERSE (Paper B, Eq. B2):
    M_CJ = sqrt(H+1) + sqrt(H),   H = (gamma^2-1) q_c / (2 gamma R T2)
                                    = (gamma+1)/2 * q_c/(cp T2)
    inverse:  H = (M_CJ^2 - 1)^2 / (4 M_CJ^2)
    =>  q~ = q_c/(cp T1) = (M_CJ^2 - 1)^2 / (2 (gamma+1) M_CJ^2)     [pi_c = 1]
    =>  q_c/(R T1)       = gamma (M_CJ^2 - 1)^2 / (2 (gamma^2-1) M_CJ^2)

EFFECTIVE HEAT RELEASE (dissociation-aware, per assignment):
    q_eff = inverse formula evaluated at the *real* M_CJ (SD Toolbox CJ speed
    over the frozen reactant sound speed, as in Fig. A16 usage) with
    gamma = gamma_e(CJ), the equilibrium isentropic exponent of the products,
    and cp_e = gamma_e R / (gamma_e - 1), R = gas constant of the mixture.
    Interpretation (see validation/gamma_phase_audit.md):
      * fuel-O2: q_eff < q_c — dissociation absorbs part of the heat release
        (the paper's mechanism for the low fuel-O2 efficiencies);
      * fuel-air: q_eff modestly exceeds q_c because the physical M_CJ is
        referenced to the reactants' sound speed (gamma_1 ~ 1.39) while the
        one-gamma model implies a1 = sqrt(gamma_e R T1) — the same
        reactants-vs-products gamma tension quantified in the audit.

Outputs: data/q_mapping.json, data/q_mapping.md.
Run from anywhere: paths are resolved relative to this file.
"""
import datetime
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(HERE))          # repo root
sys.path.insert(0, PROJ)                               # vendored sdtoolbox/

T1, P1 = 300.0, 1.0e5

# (label, reactant composition, mechanism, fuel (x,y) for CxHy major products)
MIX = [
    ('H2/air',       'H2:2,O2:1,N2:3.76',         'gri30.yaml', (0, 2, 2.0)),
    ('H2/O2',        'H2:2,O2:1',                 'gri30.yaml', (0, 2, 2.0)),
    ('CH4/air',      'CH4:1,O2:2,N2:7.52',        'gri30.yaml', (1, 4, 1.0)),
    ('CH4/O2',       'CH4:1,O2:2',                'gri30.yaml', (1, 4, 1.0)),
    ('C2H4/air',     'C2H4:1,O2:3,N2:11.28',      'gri30.yaml', (2, 4, 1.0)),
    ('C2H4/O2',      'C2H4:1,O2:3',               'gri30.yaml', (2, 4, 1.0)),
    ('C2H2/air',     'C2H2:1,O2:2.5,N2:9.4',      'gri30.yaml', (2, 2, 1.0)),
    ('C2H2/O2',      'C2H2:1,O2:2.5',             'gri30.yaml', (2, 2, 1.0)),
    ('C3H8/air',     'C3H8:1,O2:5,N2:18.8',       'gri30.yaml', (3, 8, 1.0)),
    ('C3H8/O2',      'C3H8:1,O2:5',               'gri30.yaml', (3, 8, 1.0)),
    ('kerosene/air', 'c12h26:1,o2:18.5,n2:69.56',
     os.path.join(PROJ, 'data', 'dodecane_eq_thermo.yaml'), (12, 26, 1.0)),
    ('kerosene/O2',  'c12h26:1,o2:18.5',
     os.path.join(PROJ, 'data', 'dodecane_eq_thermo.yaml'), (12, 26, 1.0)),
]


def spec_name(gas, generic):
    """Species name lookup robust to mechanism case conventions."""
    for s in gas.species_names:
        if s.lower() == generic.lower():
            return s
    raise KeyError(f'{generic} not in mechanism')


def h_inv(M):
    """Inverse of M = sqrt(H+1)+sqrt(H):  H = (M^2-1)^2/(4 M^2)."""
    return (M * M - 1.0) ** 2 / (4.0 * M * M)


def m_cj(H):
    return np.sqrt(H + 1.0) + np.sqrt(H)


def main():
    import cantera as ct
    store = json.load(open(os.path.join(PROJ, 'data', 'cycles_ws.json')))
    fj = store['fj_mixtures']

    # --- self-check of the inverse pair on the spec Sec. 3.1 benchmark -------
    g, qt = 1.4, 4.0
    M = m_cj(0.5 * (g + 1.0) * qt)
    qt_back = h_inv(M) * 2.0 / (g + 1.0)
    check_bench = dict(gamma=g, qtilde=qt, M_CJ=float(M), qtilde_back=float(qt_back),
                       spec_anchor_M=4.60)
    assert abs(M - 4.599) < 5e-3 and abs(qt_back - qt) < 1e-12

    rows, mdev_q, mdev_M = [], 0.0, 0.0
    for label, X, mech, (x, y, nfuel) in MIX:
        gas = ct.Solution(mech)
        gas.TPX = T1, P1, X
        h1 = gas.enthalpy_mass
        W = gas.mean_molecular_weight                 # kg/kmol
        R = ct.gas_constant / W                       # J/(kg K)
        g1 = gas.cp_mass / gas.cv_mass                # reactants (compression leg)
        a1 = gas.sound_speed
        # major-products state at (T1,P1): x CO2 + y/2 H2O (+ N2 unchanged)
        n = {t.split(':')[0]: float(t.split(':')[1]) for t in X.split(',')}
        n_n2 = next((v for k, v in n.items() if k.lower() == 'n2'), 0.0)
        prod = []
        if x > 0:
            prod.append(f'{spec_name(gas, "CO2")}:{nfuel * x}')
        prod.append(f'{spec_name(gas, "H2O")}:{nfuel * y / 2}')
        if n_n2 > 0:
            prod.append(f'{spec_name(gas, "N2")}:{n_n2}')
        gas.TPX = T1, P1, ','.join(prod)
        q_major = (h1 - gas.enthalpy_mass) / 1e6      # MJ/kg mixture, H2O vapour

        r = fj[label]
        q_eq = r['qc_MJkg']                            # B1: h1 - h6, equilibrium
        Mcj, ge = r['M_CJ'], r['gamma_e_CJ']
        mdev_q = max(mdev_q, abs(q_major - q_eq) / q_eq)
        mdev_M = max(mdev_M, abs(r['U_CJ'] / a1 - Mcj) / Mcj)

        H = h_inv(Mcj)
        qt_cp_eff = 2.0 * H / (ge + 1.0)               # q_eff/(cp_e T1)
        cp_e = ge * R / (ge - 1.0)
        q_eff = qt_cp_eff * cp_e * T1 / 1e6            # MJ/kg
        qt_R_true = q_eq * 1e6 / (R * T1)              # Fig. A22 axis value
        qt_cp12 = 2.0 * H / 2.2                        # gamma = 1.2 inversion
        rows.append(dict(
            label=label, W_react=W, R_JkgK=R, gamma1_react=g1, a1_ms=a1,
            U_CJ=r['U_CJ'], M_CJ=Mcj, gamma_e_CJ=ge, gamma_fr_CJ=r['gamma_fr_CJ'],
            q_thermochem_MJkg=q_major, q_c_B1_MJkg=q_eq,
            qtilde_R=qt_R_true, qtilde_cp=q_eq * 1e6 / (cp_e * T1),
            q_eff_MJkg=q_eff, qtilde_cp_eff=qt_cp_eff,
            qtilde_R_eff=qt_cp_eff * ge / (ge - 1.0),
            qtilde_R_eff_g12=6.0 * qt_cp12,
            q_eff_over_qc=q_eff / q_eq, eta_FJ=r['eta_FJ'],
            M_model_g12_from_qtildeR=float(m_cj(1.1 * qt_R_true / 6.0)),
        ))

    # family-figure correspondence (gamma = 1.2 curves, axis q_c/(R T1))
    fam = {}
    for q in (10, 20, 30, 40):
        near = sorted(rows, key=lambda r: abs(r['qtilde_R'] - q))
        fam[str(q)] = [dict(label=r['label'], qtilde_R=round(r['qtilde_R'], 1))
                       for r in near[:2] if abs(r['qtilde_R'] - q) < 5.0]

    out = dict(
        meta=dict(
            script='src/cycles/q_mapping.py',
            updated=datetime.date.today().isoformat(),
            T1_K=T1, P1_Pa=P1, phi=1.0,
            definition='q_c = h1(T1,P1) - h6(T1,P1), equilibrium products (B1); '
                       'q_thermochem = formation-enthalpy value, major products '
                       '(CO2, H2O vapour, N2), LHV basis, per kg of mixture | standard-state '
                       'anchor: q_std at T_ref = 298.15 K (validation/q_formal.md); '
                       'q_c(300K) - q_std = +0.0076%/-0.0023% (H2/CH4-air)',
            nondimensional=dict(
                classical='q~ = q_c/(cp T1)  (A18, A21, B2-B3)',
                stagnation='q~_t = q_c/(cp Tt1)  (A40-A42); existence q~_t < 1/(g^2-1)',
                family_A22='q_c/(R T1) = g/(g-1) q~  (Fig. A22 labels 10-40)'),
            inverse_B2='H = (M_CJ^2-1)^2/(4 M_CJ^2);  q~ = (M_CJ^2-1)^2/(2(g+1)M_CJ^2);  '
                       'q_c/(RT1) = g (M_CJ^2-1)^2/(2(g^2-1) M_CJ^2)',
            q_eff='inverse evaluated at real M_CJ = U_CJ/a1(frozen reactants) with '
                  'g = gamma_e(CJ) and cp_e = gamma_e R/(gamma_e-1), R of the mixture',
            checks=dict(benchmark_inverse=check_bench,
                        max_dev_qmajor_vs_B1=float(mdev_q),
                        max_dev_MCJ_recomputed=float(mdev_M)),
            sources=['AIAA 2004-1033 Eqs. 18, 21, 40-42, 57; Fig. 16/22',
                     'JPP 22(3) 2006 Eqs. 2-3', 'data/cycles_ws.json fj_mixtures'],
        ),
        mixtures=rows, family_A22_correspondence=fam,
    )
    with open(os.path.join(PROJ, 'data', 'q_mapping.json'), 'w') as f:
        json.dump(out, f, indent=1)

    # ------------------------------------------------------------------ md --
    L = []
    L.append('# q and q̃ — formal definition and mixture map (Wintenberger–Shepherd)')
    L.append('')
    L.append(f'*Generated by `src/cycles/q_mapping.py` on {datetime.date.today()}; '
             'inputs from `data/cycles_ws.json` (Cantera 3.2 + SD Toolbox, '
             'stoichiometric mixtures at 300 K, 1 bar). Slide-ready.*')
    L.append('')
    L.append('## Formal statement (five lines)')
    L.append('')
    L.append('1. **Definition (Paper B, Eq. 1).** '
             'q_c ≡ h₁(T₁,P₁) − h₆(T₁,P₁): specific heat of combustion = enthalpy of the '
             'reactants minus enthalpy of the **equilibrium products at the same initial '
             'state** (T₁, P₁), per unit mass of mixture. At 300 K the equilibrium products '
             'are the major species (CO₂, H₂O vapour, N₂), so q_c equals the '
             'formation-enthalpy (lower-heating-value) heat release: max deviation across '
             f'the 12 mixtures {100 * mdev_q:.2f}%. '
             'Standard-state precision (2026-07-09, `validation/q_formal.md`): the *formal* '
             'heat release is anchored to T_ref = 298.15 K, q° ≡ Σᵢ Y_i,1 Δh°f,i(T_ref) − '
             'Σᵢ Y_i,2 Δh°f,i(T_ref); exactly q_c(T₁) = q° + ∫_{T_ref}^{T₁}(c_p,react − '
             'c_p,prod)dT′, so the q_c of this table (T₁ = 300 K) differs from q° only by '
             'the sensible shift q° − q_c = −0.0076 % (H₂–air) / +0.0023 % (CH₄–air) — '
             'percent-grade only at preheated T₁ (700 K: +1.58 %/−0.30 %); the 300 K values '
             'below are unaffected.')
    L.append('2. **Non-dimensionalization.** The papers use q̃ = q_c/(c_p T₁) on the classical '
             'Hugoniot and in the FJ closed form (Eqs. A18/A21, B2–B3), '
             'q̃_t = q_c/(c_p T_t1) on the stagnation Hugoniot (A40–A42, existence limit '
             'q̃_t < 1/(γ²−1)), and q_c/(R T₁) = γ/(γ−1)·q̃ as the family label of Fig. A22.')
    L.append('3. **CJ Mach number (Eq. B2).** M_CJ = √(H+1) + √H with '
             'H = (γ²−1) q_c/(2γRT₂) = (γ+1)/2 · q_c/(c_p T₂), T₂ = temperature of the '
             '(possibly precompressed) reactants ahead of the wave.')
    L.append('4. **Exact inverse.** H = (M_CJ²−1)²/(4M_CJ²), hence '
             '**q̃ = q_c/(c_p T₁) = (M_CJ²−1)²/(2(γ+1)M_CJ²)** and '
             'q_c/(RT₁) = γ(M_CJ²−1)²/(2(γ²−1)M_CJ²). '
             'Check on the spec §3.1 benchmark: γ=1.4, q̃=4 → M_CJ=4.599 → q̃ back to 4.000.')
    L.append('5. **Effective heat release.** q_eff = inverse formula at the physical M_CJ '
             '(CJ speed over frozen reactant sound speed) with γ = γ_e(CJ) of the products: '
             'for fuel–O₂, q_eff < q_c — dissociation withholds part of the release '
             '(the paper’s mechanism for the low fuel–O₂ η); for fuel–air, q_eff mildly '
             'exceeds q_c because M_CJ is referenced to the reactants’ sound speed '
             '(γ₁≈1.39) while the one-γ model implies a₁=√(γ_e RT₁) — see '
             '`validation/gamma_phase_audit.md`.')
    L.append('')
    L.append('## Mixture table (φ = 1, 300 K, 1 bar)')
    L.append('')
    L.append('| mixture | M_CJ | γ_e(CJ) | q_thermo [MJ/kg] | q_c=h₁−h₆ [MJ/kg] | '
             'q̃ = q_c/c_pT₁ | q_c/RT₁ | q_eff [MJ/kg] | q_eff/q_c | η_FJ |')
    L.append('|---|---|---|---|---|---|---|---|---|---|')
    for r in rows:
        L.append(f"| {r['label']} | {r['M_CJ']:.2f} | {r['gamma_e_CJ']:.3f} | "
                 f"{r['q_thermochem_MJkg']:.2f} | {r['q_c_B1_MJkg']:.2f} | "
                 f"{r['qtilde_cp']:.2f} | {r['qtilde_R']:.1f} | "
                 f"{r['q_eff_MJkg']:.2f} | {r['q_eff_over_qc']:.2f} | {r['eta_FJ']:.3f} |")
    L.append('')
    L.append('*q_thermo: formation enthalpies, major products, H₂O vapour. '
             'q̃ and q_c/RT₁ use c_p = γ_e R/(γ_e−1) and the mixture gas constant R '
             '(reactants). q_eff: inversion of M_CJ with γ = γ_e(CJ).*')
    L.append('')
    L.append('## Traceability of the Fig. A22 family (`fig_cycle_family`, γ = 1.2)')
    L.append('')
    L.append('Curve labels are q_c/RT₁; nearest stoichiometric mixtures by their actual '
             'q_c/RT₁ (γ=1.2 model reproduces their M_CJ within ≈5% for fuel–air):')
    L.append('')
    for q in (10, 20, 30, 40):
        hits = fam[str(q)]
        txt = ', '.join(f"{h['label']} ({h['qtilde_R']})" for h in hits) if hits \
            else '— (no stoichiometric mixture this low; lean fuel–air territory)'
        L.append(f'- **q_c/RT₁ = {q}** ↔ {txt}')
    L.append('- fuel–O₂ mixtures lie far above the family '
             f"(q_c/RT₁ = {min(r['qtilde_R'] for r in rows if 'O2' in r['label']):.0f}–"
             f"{max(r['qtilde_R'] for r in rows if 'O2' in r['label']):.0f}) and have "
             'γ_e ≈ 1.13, not 1.2: the family is a fuel–air-class model.')
    L.append('')
    with open(os.path.join(PROJ, 'data', 'q_mapping.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')

    print(f'[q_mapping] 12 mixtures; max |q_major - q_B1|/q_B1 = {100 * mdev_q:.2f}%; '
          f'max M_CJ recompute dev = {100 * mdev_M:.2f}%')
    for r in rows:
        print(f"  {r['label']:14s} M={r['M_CJ']:5.2f} ge={r['gamma_e_CJ']:.3f} "
              f"q_th={r['q_thermochem_MJkg']:6.2f} q_B1={r['q_c_B1_MJkg']:6.2f} "
              f"q~R={r['qtilde_R']:6.1f} q_eff={r['q_eff_MJkg']:6.2f} "
              f"ratio={r['q_eff_over_qc']:.2f}")


if __name__ == '__main__':
    main()
