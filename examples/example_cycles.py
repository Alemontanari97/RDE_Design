"""example_cycles.py — detonation-cycle efficiencies (Wintenberger & Shepherd).

Reads the validated Fickett-Jacobs results (data/cycles_ws.json: 12 stoichiometric
mixtures, full shifting-equilibrium chemistry, eta_FJ = (h1-h5)/q_c per Paper B
Eq. 1) and re-derives one analytic anchor of the one-gamma model live:
M_CJ(gamma=1.4, qtilde=4) = 4.599 (Paper B Eq. 2, spec benchmark).

Run:      python examples/example_cycles.py        (instant)
Expected: eta_FJ(CH4/air) = 0.300; fuel-air band 0.28-0.31 > fuel-O2 0.18-0.23
          (dissociation penalty); M_CJ anchor 4.599.
"""
import os, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src', 'cycles'))
from cycles import cj_mach, eta_fj_1g          # one-gamma model (Eqs. B2-B3/A57)

fj = json.load(open(os.path.join(ROOT, 'data', 'cycles_ws.json')))['fj_mixtures']

print(f"{'mixture':14s}{'U_CJ [m/s]':>11s}{'M_CJ':>7s}{'q_c [MJ/kg]':>12s}{'eta_FJ':>8s}")
for k, r in fj.items():
    print(f"{k:14s}{r['U_CJ']:11.1f}{r['M_CJ']:7.2f}{r['qc_MJkg']:12.2f}{r['eta_FJ']:8.3f}")

air = [r['eta_FJ'] for k, r in fj.items() if k.endswith('/air')]
ox  = [r['eta_FJ'] for k, r in fj.items() if k.endswith('/O2')]
assert all(0.27 < e < 0.32 for e in air) and all(0.18 < e < 0.24 for e in ox)
assert min(air) > max(ox), "every fuel-air cycle must beat every fuel-O2 cycle"

M = cj_mach(4.0, 1.4)[0]                       # analytic anchor, Paper B Eq. 2
eta20 = eta_fj_1g(4.0, 1.4, pic=20.0)          # precompression benefit (A57/A58)
print(f"\none-gamma anchors: M_CJ(g=1.4, q~=4) = {M:.3f} (spec: 4.599); "
      f"eta_FJ rises {eta_fj_1g(4.0, 1.4):.3f} -> {eta20:.3f} at pi_c = 20")
assert abs(M - 4.599) < 5e-3
print(f"OK: eta_FJ(CH4/air) = {fj['CH4/air']['eta_FJ']:.3f}; bands and anchors verified")
