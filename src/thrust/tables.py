#!/usr/bin/env python3
"""tables.py — build data/thrust_tables.md + data/vv_thrust.md from data/thrust_models_all.json.

Lecture-repo edition of project_build/scripts/make_thrust_tables.py (verbatim;
imports/paths adapted). Post-processing + V&V only: the physics lives in
sk_models.py (Shepherd-Kasahara pressure-history / axial-flow models and the
Stechmann mass-weighted blowdown cycle); this script re-derives the 8 V&V
verdicts (literature, internal-consistency and cross-model checks) and
regenerates both markdown tables. The frozen validated copy of vv_thrust.md
ships in validation/.

Usage: python3 tables.py   (inputs, all shipped: data/thrust_models_all.json,
       data/results_main.json, data/sk_tables.json)
"""
import sys, os, json
import numpy as np
SCR = os.path.dirname(os.path.abspath(__file__)); PROJ = os.path.dirname(os.path.dirname(SCR))  # repo root
sys.path.insert(0, SCR)
try:                                    # package mode
    from .sk_models import stech_calc, G0, ATM
except ImportError:                     # script mode
    from sk_models import stech_calc, G0, ATM
def main():
    DAT = os.path.join(PROJ, 'data')
    D  = json.load(open(os.path.join(DAT, 'thrust_models_all.json')))
    RM = {x['name']: x for x in json.load(open(os.path.join(DAT, 'results_main.json')))}
    SKT = json.load(open(os.path.join(DAT, 'sk_tables.json')))
    C = D['cases']; SK1 = SKT['T1']
    ORDER = ['H2/air','H2/O2','CH4/air','CH4/O2','C2H4/air','C2H4/O2',
             'C2H2/air','C2H2/O2','C3H8/air','C3H8/O2','C12H26/air','C12H26/O2']
    REPMAP = [('H2-air','SKREP:H2/air'),('C2H4-air','SKREP:C2H4/air'),
              ('C2H4-O2','SKREP:C2H4/O2'),('C3H8-O2','SKREP:C3H8/O2')]
    RHOC_SK = [1.48, 2.04, 2.19, 2.41]
    DISP = lambda k: k.replace('C12H26','Kerosene(C12H26)')
    pct = lambda a, b: (a/b - 1.0)*100.0

    # ---------------- V&V computations ----------------
    vv1 = []   # U_CJ vs results_main
    for nm, r in RM.items():
        if nm in C:
            u = C[nm]['cj']['UCJ']; vv1.append((nm, u, r['UCJ'], pct(u, r['UCJ'])))
    vv3 = []   # SK Table-1 replica, inputs+outputs
    for i, (lab, key) in enumerate(REPMAP):
        cj = C[key]['cj']; ph = C[key]['ph']; ax = C[key]['axial']
        vv3.append(dict(lab=lab, U=cj['UCJ'], U_sk=SK1['UCJ'][i], dU=pct(cj['UCJ'], SK1['UCJ'][i]),
            P2=cj['P2']/1e6, P2_sk=SK1['PCJ'][i], dP=pct(cj['P2']/1e6, SK1['PCJ'][i]),
            ge=cj['gamma_e'], ge_sk=SK1['ge'][i], rho=cj['rho1'], rho_sk=RHOC_SK[i],
            Yf=cj['Yf'], Yf_sk=SK1['Yf'][i],
            ph=ph['Ispf'], ph_sk=SK1['pressure_hist'][i], dph=pct(ph['Ispf'], SK1['pressure_hist'][i]),
            ax=ax['Ispf_sonic'], ax_sk=SK1['axial'][i], dax=pct(ax['Ispf_sonic'], SK1['axial'][i]),
            cfd=SK1['sim'][i], dph_cfd=pct(ph['Ispf'], SK1['sim'][i]), dax_cfd=pct(ax['Ispf_sonic'], SK1['sim'][i])))
    pmv  = [(k, C[k]['axial']['Pm_over_P2']) for k in C if 'axial' in C[k]]
    resv = [(k, C[k]['cj']['cj_sonic_resid']) for k in C]
    sm   = [(k, pct(C[k]['axial']['FovM_matched'], C[k]['axial']['FovM_sonic'])) for k in C if 'axial' in C[k]]
    # Stechmann collapse test (PR -> 1 must give steady Cf*cstar/g)
    ge_, R_, T_, Pin_ = 1.20, 8314.462/24.0, 3500.0, 20*ATM
    st0 = stech_calc(ge_, R_, 1.0 + 1e-9, Pin_, T_)
    NPR = ((ge_+1)/2)**(ge_/(ge_-1)); base = 2*ge_**2/(ge_-1)*(2/(ge_+1))**((ge_+1)/(ge_-1))
    cst = np.sqrt(ge_*R_*T_)/(ge_*np.sqrt((2/(ge_+1))**((ge_+1)/(ge_-1))))
    Isp_steady = (np.sqrt(base*(1-(1/NPR)**((ge_-1)/ge_))) + (1/NPR - ATM/Pin_))*cst/G0
    collapse_err = abs(st0['Isp_sl_e1']/Isp_steady - 1.0)
    stech_rows = [(k, C[k]['stech']) for k in ORDER if 'stech' in C.get(k, {})]
    xmod = []
    for k, st in stech_rows:
        trio = [C[k]['ph']['Isp_tot'], C[k]['axial']['Isp_tot_sonic'], st['Isp_sl_e1']]
        xmod.append((k, trio, (max(trio)-min(trio))/np.mean(trio)*100))

    # every V&V input set must be non-empty (key drift => diagnosable error,
    # never a bare min()/max() ValueError or a silently shrunken check)
    for nm_, seq_ in (('vv1', vv1), ('vv3', vv3), ('pmv', pmv), ('resv', resv),
                      ('sm', sm), ('stech_rows', stech_rows), ('xmod', xmod)):
        if not seq_:
            raise RuntimeError('V&V input set %r is empty - key drift between '
                               'results_main.json / thrust_models_all.json / '
                               'sk_tables.json?' % nm_)

    ck = {}
    ck['1_UCJ_vs_results_main'] = ('PASS' if max(abs(x[3]) for x in vv1) < 0.5 else 'FAIL',
        'max %+.2f%% (n=%d combos, threshold 0.5%%)' % (max((x[3] for x in vv1), key=abs), len(vv1)))
    # check 2 COMPUTED from sk_tables.json comp records (was a frozen string)
    eU2 = max(abs(x['err_U']) for x in SKT['comp'])
    eP2 = max(abs(x['err_P']) for x in SKT['comp'])
    ck['2_CJ_vs_SK_Table2'] = ('PASS' if eU2 < 0.5 and eP2 < 2.0 else 'FAIL',
        'live max errU %.1f%% (<0.5), errP %.1f%% (<2.0), %d mixtures (sk_tables.json comp)'
        % (eU2, eP2, len(SKT['comp'])))
    mdU = max(abs(r['dU']) for r in vv3); mge = max(abs(r['ge']-r['ge_sk']) for r in vv3)
    mdP = max(abs(r['dP']) for r in vv3)
    # rho_c: direct comparison since the 2026-07-16 re-bless at the SK fill
    # 0.15 MPa (anomaly A6); bound = 3-s.f. literature rounding + thermo
    mrho = max(abs(r['rho'] / r['rho_sk'] - 1) * 100 for r in vv3)
    mYf = max(abs(r['Yf']-r['Yf_sk']) for r in vv3)
    ck['3a_replica_inputs'] = ('PASS' if mdU<0.2 and mge<0.005 and mdP<2.0 and mrho<0.5 and mYf<0.002 else 'FAIL',
        'live max on 4 cases: |dU| %.3f%% (<0.2), |d g_e| %.4f (<0.005), |dP| %.2f%% (<2.0), '
        '|d rho_c| %.2f%% (<0.5, direct at the 0.15 MPa SK fill, A6), |d Y_f| %.4f (<0.002)'
        % (mdU, mge, mdP, mrho, mYf))
    ck['3b_axial_vs_SK'] = ('PASS' if all(abs(r['dax'])<1.0 for r in vv3) else 'FAIL',
        'all %d within %.1f%% (<1.0)' % (len(vv3), max(abs(r['dax']) for r in vv3)))
    # check 3c: PASS* is valid ONLY if the single failure IS the documented
    # C2H4-O2 anomaly (a new failure elsewhere must FAIL, not hide behind it)
    fails3c = [r['lab'] for r in vv3 if abs(r['dph']) >= 5.0]
    r_anom = [r for r in vv3 if r['lab'] == 'C2H4-O2'][0]
    ok_others = max((abs(r['dph']) for r in vv3 if r['lab'] != 'C2H4-O2'))
    ck['3c_PH_vs_SK'] = ('PASS' if not fails3c else
                         ('PASS*' if fails3c == ['C2H4-O2'] else 'FAIL'),
        '%d/%d within %.1f%%; the one failure IS the documented C2H4-O2 anomaly '
        '(published 704 s vs our %d s, %+.0f%%) - see A1'
        % (len(vv3)-len(fails3c), len(vv3), ok_others, round(r_anom['ph']), r_anom['dph']))
    # Pm/P2 band = SK quoted ~0.22-0.25 with +-0.005 figure-reading margin
    PM_LO, PM_HI = 0.215, 0.255
    ck['4_axial_internal'] = ('PASS' if all(PM_LO<v<PM_HI for _,v in pmv) and max(v for _,v in resv)<0.005 else 'FAIL',
        'Pm/P2 in [%.3f,%.3f] vs SK ~0.22-0.25 (+-0.005 reading margin => [%.3f,%.3f]); '
        'CJ sonic residual <= %.4f (<0.005); sonic-vs-matched span %+.1f..%+.1f%% (reported)'
        % (min(v for _,v in pmv), max(v for _,v in pmv), PM_LO, PM_HI,
           max(v for _,v in resv), min(v for _,v in sm), max(v for _,v in sm)))
    ck['5_stechmann_internal'] = ('PASS' if collapse_err < 1e-6 and all(st['Isp_sl_e1']>st['Isp_ta_sl_e1'] for _,st in stech_rows) else 'FAIL',
        'CP-collapse rel.err %.1e; mass-weighted > time-averaged for %d/%d; choked fraction %.0f-%.0f%% of cycle'
        % (collapse_err, sum(st['Isp_sl_e1']>st['Isp_ta_sl_e1'] for _,st in stech_rows),
           len(stech_rows), 100*min(st['frac_choked'] for _,st in stech_rows),
           100*max(st['frac_choked'] for _,st in stech_rows)))
    ck['6_cross_model'] = ('PASS' if all(s<12 for _,_,s in xmod) else 'FAIL',
        'PH vs axial-sonic vs Stechmann(eps=1,SL) total-mass Isp spread %.1f-%.1f%% '
        '(%d fuel-O2 combos; 12%% budget = the three closures differ by design: '
        'K-fit tail vs sonic-exit vs blowdown average, each ~5%% class, see A3/A4)'
        % (min(s for _,_,s in xmod), max(s for _,_,s in xmod), len(xmod)))

    # ---------------- thrust_tables.md ----------------
    L = []
    A = L.append
    A('# Analytical RDE thrust models - all propellant combinations')
    A('')
    A('Conditions: phi = 1, p1 = 1 atm, T1 = 300 K, Pa = 1 atm (sea level). '
      'CJ states: SD Toolbox (Caltech) on Cantera 3.2; GRI-3.0 for H2/CH4/C2H4/C2H2/C3H8; '
      'kerosene = n-dodecane surrogate (Reitz thermo + GRI NOx thermo, equilibrium-only reduced set, '
      'validated to +0.19% on U_CJ vs the full mechanism).')
    A('')
    A('Models: **PH** = Shepherd-Kasahara pressure-history, F/Mdot = K(P_CJ-P1)/(rho1 U_CJ) + [u_c + (P1-Pa)/(rho1 u_c)], '
      'K = 1.02 (air) / 1.54 (O2), u_c = 300 m/s; **AX** = SK axial flow, w = sqrt(2(h1-h(P,s2))) on the equilibrium '
      'isentrope through the CJ state, T/Mdot = w + (P-Pa)/(rho w) at the sonic point (matched-exit vs sonic '
      'span %+.1f..%+.1f%% on this set); **ST** = Stechmann-Heister mass-weighted blowdown cycle. '
      % (min(v for _, v in sm), max(v for _, v in sm)) +
      'gamma_e = equilibrium isentropic exponent rho2 a_eq^2/P2 at CJ. Isp_f = (T/Mdot)/(Y_f g0).')
    A('')
    A('## Table 1 - CJ state and specific thrust (all combos, phi=1, 1 atm, 300 K)')
    A('')
    A('| Mixture | U_CJ [m/s] | p2/p1 | T_CJ [K] | gamma_e | Y_f | T/Mdot PH [m/s] | T/Mdot AX [m/s] | Isp_f PH [s] | Isp_f AX [s] | Isp_f CFD lit [s] |')
    A('|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|')
    LIT_CFD = {'H2/air': 4860, 'C2H4/air': 1990, 'C2H4/O2': 700, 'C3H8/O2': 1070}
    for k in ORDER:
        cj = C[k]['cj']; ph = C[k]['ph']; ax = C[k]['axial']
        lit = ('%d^a' % LIT_CFD[k]) if k in LIT_CFD else '-'
        A('| %s | %.0f | %.2f | %.0f | %.3f | %.4f | %.0f | %.0f | %.0f | %.0f | %s |' % (
          DISP(k), cj['UCJ'], cj['p2p1'], cj['T2'], cj['gamma_e'], cj['Yf'],
          ph['FovM'], ax['FovM_sonic'], ph['Ispf'], ax['Ispf_sonic'], lit))
    A('')
    A('^a Schwer & Kailasanath (2013) unsteady 2-D CFD, computed at 0.15 MPa / 255 K fill - see Table 2 '
      'for the same-condition comparison. PH includes term II with u_c = 300 m/s (at p1 = Pa the pressure part vanishes).')
    A('')
    A('## Table 2 - Literature convergence at SK Table-1 conditions (0.15 MPa / 255 K fill, A6)')
    A('')
    A('| Case | U_CJ me/SK [m/s] | P_CJ me/SK [MPa] | gamma_e me/SK | Isp_f PH me/SK [s] | dPH% | Isp_f AX me/SK [s] | dAX% | CFD S&K [s] |')
    A('|---|---:|---:|---:|---:|---:|---:|---:|---:|')
    for r in vv3:
        A('| %s | %.0f / %d | %.2f / %.2f | %.3f / %.3f | %.0f / %d | %+.1f | %.0f / %d | %+.1f | %d |' % (
          r['lab'], r['U'], r['U_sk'], r['P2'], r['P2_sk'], r['ge'], r['ge_sk'],
          r['ph'], r['ph_sk'], r['dph'], r['ax'], r['ax_sk'], r['dax'], r['cfd']))
    A('')
    A('Axial model reproduced to +-0.2% on 4/4 cases; PH reproduced on 3/4 (the published C2H4-O2 value '
      'of 704 s is inconsistent with the model equations and its own twin case C3H8-O2 - see vv_thrust.md, anomaly A1).')
    A('')
    A('## Table 3 - Stechmann-Heister mass-weighted cycle Isp (fuel-O2, fill 1 atm / 300 K)')
    A('')
    A('| Mixture | PR = p_CJ/p1 | gamma_e | c*_mw [m/s] | Isp mw eps=1 SL [s] | Isp mw aerospike SL [s] | Isp mw eps=1 vac [s] | Isp_f aerospike SL [s] | mw/time-avg |')
    A('|---|---:|---:|---:|---:|---:|---:|---:|---:|')
    for k, st in stech_rows:
        A('| %s | %.1f | %.3f | %.0f | %.1f | %.1f | %.1f | %.0f | %.3f |' % (
          DISP(k), st['PR'], st['gamma'], st['cstar_mw'], st['Isp_sl_e1'], st['Isp_sl_spike'],
          st['Isp_vac_e1'], st['Ispf_sl_spike'], st['mw_over_ta_e1']))
    A('')
    A('Isp = total-propellant-mass based (rocket convention); Isp_f = fuel-based. eps=1: exit = throat (no nozzle), '
      'directly comparable to the SK sonic axial model; ideal aerospike: Pe = Pa throughout the blowdown (Eq. 10). '
      'Low absolute values reflect the 1-atm fill pressure (Stechmann Table 1 cases run 20-200 atm chambers).')
    A('')
    A('## Cross-model consistency (total-mass Isp [s], fuel-O2, sea level)')
    A('')
    A('| Mixture | PH | AX sonic | ST eps=1 | spread % |')
    A('|---|---:|---:|---:|---:|')
    for k, trio, s in xmod:
        A('| %s | %.0f | %.0f | %.0f | %.1f |' % (DISP(k), trio[0], trio[1], trio[2], s))
    open(os.path.join(DAT, 'thrust_tables.md'), 'w').write('\n'.join(L) + '\n')

    # ---------------- vv_thrust.md ----------------
    V = []; B = V.append
    B('# V&V - analytical thrust models (PH / axial / Stechmann)')
    B('')
    B('Pipeline: scripts/thrust_models.py -> data/thrust_models_all.json (16 cases: 12 std @ 1 atm/300 K + 4 SKREP @ 0.15 MPa/255 K, A6).')
    B('No number is reported without a cross-check; verdicts below.')
    B('')
    B('## Checks')
    B('')
    B('| # | Check | Verdict | Evidence |')
    B('|---|---|---|---|')
    NAMES = {'1_UCJ_vs_results_main': 'U_CJ vs results_main.json (%d validated combos, <0.5%%)' % len(vv1),
     '2_CJ_vs_SK_Table2': 'CJ state vs SK Table 2 literature (%d mixtures)' % len(SKT['comp']),
     '3a_replica_inputs': 'SK Table-1 replica: model INPUTS (U_CJ, P_CJ, gamma_e, rho_c, Y_f)',
     '3b_axial_vs_SK': 'Axial-flow Isp_f vs SK Table 1 (%d cases)' % len(vv3),
     '3c_PH_vs_SK': 'Pressure-history Isp_f vs SK Table 1 (%d cases)' % len(vv3),
     '4_axial_internal': 'Axial internal: Pm/P2 range, CJ sonicity (sonic-vs-matched span reported)',
     '5_stechmann_internal': 'Stechmann internal: CP-collapse, mass- vs time-weighting, choking',
     '6_cross_model': 'Cross-model coherence PH / axial / Stechmann (fuel-O2)'}
    for kk in ['1_UCJ_vs_results_main','2_CJ_vs_SK_Table2','3a_replica_inputs','3b_axial_vs_SK',
               '3c_PH_vs_SK','4_axial_internal','5_stechmann_internal','6_cross_model']:
        B('| %s | %s | **%s** | %s |' % (kk.split('_')[0], NAMES[kk], ck[kk][0], ck[kk][1]))
    B('')
    B('## Check 1 detail - U_CJ vs results_main.json')
    B('')
    B('| Mixture | U_CJ new [m/s] | U_CJ results_main [m/s] | d% |')
    B('|---|---:|---:|---:|')
    for nm, u, ur, dp in sorted(vv1):
        B('| %s | %.1f | %.1f | %+.3f |' % (nm, u, ur, dp))
    B('')
    B('C12H26/O2 differs by +0.19% because the new run uses the reduced 20-species equilibrium-thermo mechanism '
      '(full 100-species Reitz kinetics are irrelevant for CJ equilibrium; reduction validated by this very check). '
      'C2H2/air, C3H8/air, C12H26/air are new combos with no prior in-project reference: anchored by the same '
      'validated pipeline + physical ordering U_CJ(C2H2)>U_CJ(C2H4)>U_CJ(CH4)~U_CJ(C3H8)~U_CJ(C12H26) for air, satisfied.')
    B('')
    B('## Check 3 detail - SK Table-1 replica (0.15 MPa / 255 K, u_c = 300 m/s, Pa = 1 atm)')
    B('')
    B('| Case | rho_c me/SK | Y_f me/SK | U_CJ d% | P_CJ d% | Isp_f PH me/SK (d%) | Isp_f AX me/SK (d%) |')
    B('|---|---:|---:|---:|---:|---:|---:|')
    for r in vv3:
        B('| %s | %.2f / %.2f | %.4f / %.4f | %+.2f | %+.1f | %.0f / %d (%+.1f%%) | %.0f / %d (%+.1f%%) |' % (
          r['lab'], r['rho'], r['rho_sk'], r['Yf'], r['Yf_sk'], r['dU'], r['dP'],
          r['ph'], r['ph_sk'], r['dph'], r['ax'], r['ax_sk'], r['dax']))
    B('')
    B('## Anomalies and limitations')
    B('')
    r_c3 = [r for r in vv3 if r['lab'] == 'C3H8-O2'][0]
    B(('**A1 - SK Table 1, C2H4-O2 pressure-history value (704 s) is not reproducible.** '
       'Our faithful implementation gives %d s. Proof of anomaly: C2H4-O2 and C3H8-O2 have near-identical '
       'model inputs (U_CJ 2402/2383 m/s, gamma_e 1.142/1.137, Y_f 0.226/0.216, P_CJ 5.97/6.46 MPa), so the PH model '
       'cannot produce Isp_f differing by 44%% (704 vs 1016 s); our pair (%d/%d s) has the physically required ratio. '
       'The same-row axial value (911 s) IS reproduced at %+.1f%%, so the implementation is not at fault. '
       'The published 704 coincides with the CFD value (700): plausible transcription/erratum in the report table, '
       'or an undocumented case-specific alpha (~0.93 instead of 0.65). Also internally inconsistent in the report: '
       'Mdot = 1.91 kg/s with H = 15.1 mm and rho_c = 2.19 implies channel width W = 24 mm, vs W = 10 mm for the '
       'other three cases (Eq. 15).')
      % (round(r_anom['ph']), round(r_anom['ph']), round(r_c3['ph']),
         r_anom['dax']))
    B('')
    B('**A2 - kerosene surrogate.** Kerosene = n-C12H26 (as in the existing deck). The Reitz mechanism contains '
      'no NOx species at all, so kerosene/AIR equilibrium would miss NO: we grafted NO/N/N2O/NO2 NASA thermo from '
      'GRI-3.0 into the reduced equilibrium set (Tad check: 2279 K, X_NO = 0.0025 - textbook values). '
      'Kerosene/air IS feasible: U_CJ = 1795.9 m/s, T_CJ = 2836 K. Thermo polynomials valid to 5000 K (no extrapolation).')
    B('')
    B('**A3 - K calibration domain.** K = 1.02 (air) / 1.54 (O2) were fitted by SK on C2H4-air / C2H4-O2 injector-face '
      'pressure traces of S&K (2013); following SK Table 1 practice we extend them to all same-oxidizer mixtures. '
      'K for other fuels is an assumption of the method, not a measured value.')
    B('')
    B('**A4 - Stechmann at 1-atm fill.** With Pinit = Pa = 1 atm the choked-at-all-times assumption fails in the last '
      '~15-19% of the cycle (Pc/Pa < critical); values there follow the ideal choked formulas (Stechmann himself runs '
      '20-200 atm chambers, where the assumption holds). His published Table-1 Isp (200 K, optimized phi, 20/200 atm) '
      'is therefore NOT directly comparable; V&V for this model is the CP-collapse test, the mass-vs-time weighting '
      'inequality, and cross-model coherence (checks 5-6).')
    B('')
    B('**A6 - SK Table-1 fill convention (discovered 2026-07-15, RESOLVED by re-bless 2026-07-16).** '
      'SK Table 1 quotes rho_c consistent with a 0.15 MPa (1.5 bar) fill, not the 1.5 atm the replica '
      'historically ran: densities rescaled by 150000/151987.5 reproduced all four quoted rho_c to 3 s.f. '
      'The SKREP cases are NOW computed directly at 0.15 MPa / 255 K (sk_models.py); check 3a compares '
      'rho_c directly (live max %.2f%%). The former +1.32%% offset on P-linked quantities is gone; '
      'U_CJ, gamma_e and the Isp_f ratios were never affected (<0.2%%).' % mrho)
    B('')
    B('**A5 - correction to the existing deck numbers.** results_main.json FovM/Ispf used the FROZEN gamma at CJ '
      '(~1.22-1.25) in place of the equilibrium gamma_e (~1.13-1.17) required by SK Eq. 19-20, and omitted term II: '
      'e.g. H2/air Isp_f 3203 s (deck) -> 4268 s (faithful PH I+II at the same conditions). '
      'Slide tables built from results_main.json should be updated with data/thrust_models_all.json.')
    B('')
    B('Ambient/units: Pa = 101325 Pa, g0 = 9.80665; all Isp fuel-based unless noted. '
      'Generated by src/thrust/tables.py.')
    open(os.path.join(DAT, 'vv_thrust.md'), 'w').write('\n'.join(V) + '\n')

    # ---------------- meta into JSON ----------------
    D['meta'] = dict(
      conditions=dict(phi=1.0, P1_std=101325.0, T1_std=300.0, Pa=101325.0, T1_skrep=255.0, P1_skrep=0.15e6),
      models=dict(PH='Shepherd-Kasahara FM2017.001 Sec.3: F/Mdot = K(P_CJ-P1)/(rho1 U_CJ) + u_c + (P1-Pa)/(rho1 u_c); K=1.02 air (alpha=0.98), 1.54 O2 (alpha=0.65); u_c=300 m/s',
                  AX='ibid. Sec.4: w=sqrt(2(h1-h(P,s2))) equilibrium isentrope through CJ; T/Mdot=w+(P-Pa)/(rho w) at sonic point',
                  ST='Stechmann-Heister-Harroun JSR 56(3) 2019: mass-weighted blowdown Isp, Pc=PR*Pinit*exp(-ln(PR) t/tc), choked, Cf eps=1 / ideal aerospike'),
      literature_anchors=dict(SK_Table1=SK1, SK_Table2_check=SKT['comp']),
      vv={k: dict(verdict=v[0], evidence=v[1]) for k, v in ck.items()},
      kerosene='n-dodecane; reduced 20-sp equilibrium thermo (Reitz + GRI NOx); dU_CJ vs full mech +0.19%',
      gamma_e_def='equilibrium isentropic exponent rho2*a_eq^2/P2 at CJ (a_eq = equilibrium sound speed)')
    json.dump(D, open(os.path.join(DAT, 'thrust_models_all.json'), 'w'), indent=1)

    print('== VERDICTS =='); [print('%-26s %-5s %s' % (k, v[0], v[1])) for k, v in ck.items()]
    print('\n== MAIN TABLE (std 1 atm/300 K) ==')
    print('%-16s %6s %6s %6s %7s %7s %7s %7s %7s' % ('mix','U_CJ','p2/p1','T_CJ','g_e','F/M_PH','F/M_AX','IspfPH','IspfAX'))
    for k in ORDER:
        cj=C[k]['cj']; ph=C[k]['ph']; ax=C[k]['axial']
        print('%-16s %6.0f %6.2f %6.0f %7.3f %7.0f %7.0f %7.0f %7.0f' % (k, cj['UCJ'], cj['p2p1'], cj['T2'], cj['gamma_e'], ph['FovM'], ax['FovM_sonic'], ph['Ispf'], ax['Ispf_sonic']))
    print('\nfiles written: thrust_tables.md, vv_thrust.md, thrust_models_all.json (meta)')
    return 0 if all(v[0] in ('PASS', 'PASS*') for v in ck.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
