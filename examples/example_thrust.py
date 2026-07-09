"""example_thrust.py — analytical RDE specific thrust and Isp (three SOTA models).

Prints the validated thrust table (data/thrust_models_all.json): Shepherd-Kasahara
pressure-history [PH, FM2017.001 Eqs. 6-20] and axial-flow [AX, Eqs. 44-45]
specific thrust and fuel-based Isp. Then recomputes ONE number live — the
Stechmann mass-weighted blowdown Isp (JSR 56(3) 2019, Eqs. 4-15) for H2/O2 —
and checks it against the shipped value.

Run:      python examples/example_thrust.py        (~seconds)
Expected: H2/air  F/Mdot = 1194 (PH) / 1353 (AX) m/s, Isp_f = 4268 / 4838 s;
          live Stechmann H2/O2 Isp(sl, eps=1) = 237.1 s == shipped value.
"""
import os, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src', 'thrust'))
import cantera as ct
from sk_models import stech_calc                     # Stechmann Eqs. 4-15

C = json.load(open(os.path.join(ROOT, 'data', 'thrust_models_all.json')))['cases']

print(f"{'mixture':10s}{'U_CJ':>7s}{'p2/p1':>7s}{'g_e':>7s}{'F/M PH':>8s}{'F/M AX':>8s}"
      f"{'Ispf PH':>9s}{'Ispf AX':>9s}   [m/s, s; phi=1, 1 atm, 300 K]")
for k in ['H2/air', 'H2/O2', 'CH4/air', 'CH4/O2', 'C2H4/O2', 'C3H8/O2']:
    cj, ph, ax = C[k]['cj'], C[k]['ph'], C[k]['axial']
    print(f"{k:10s}{cj['UCJ']:7.0f}{cj['p2p1']:7.2f}{cj['gamma_e']:7.3f}"
          f"{ph['FovM']:8.0f}{ax['FovM_sonic']:8.0f}{ph['Ispf']:9.0f}{ax['Ispf_sonic']:9.0f}")

cj, ref = C['H2/O2']['cj'], C['H2/O2']['stech']      # live Stechmann recompute
st = stech_calc(cj['gamma_e'], ct.gas_constant / cj['M2w'],
                cj['p2p1'], cj['cond']['P1'], cj['T2'])
print(f"\nStechmann H2/O2 (mass-weighted, eps=1, sea level): "
      f"live {st['Isp_sl_e1']:.1f} s | shipped {ref['Isp_sl_e1']:.1f} s")
assert abs(st['Isp_sl_e1'] - ref['Isp_sl_e1']) < 0.05
assert st['Isp_sl_e1'] > st['Isp_ta_sl_e1'], "mass-weighting must beat time-averaging"
print("OK: table printed; live Stechmann matches shipped value to <0.05 s")
