"""znd_profiles.py — ZND detonation-structure profiles via the official SD Toolbox.

Lecture-repo edition of project_build/scripts/znd_sdt.py (verbatim numerics;
paths made repo-relative, case selection added on the command line).

PIPELINE (Shepherd, GALCIT FM2018.001):
  1. CJspeed(P1, T1, q, mech)      — CJ detonation speed (equilibrium Hugoniot,
                                     density-ratio sweep + LSQ parabola);
  2. PostShock_fr(U_CJ, ...)       — frozen post-shock (von Neumann) state;
  3. zndsolve(...)                 — ZND ODE system integrated behind the shock:
       dP/dx, drho/dx driven by the THERMICITY
       sigma-dot = sum_i (W/W_i - h_i/(cp T)) dY_i/dt   [1/s]
     through the sonic parameter eta = 1 - M^2 (FM2018.001 Sec. 2.4);
     induction length = x(max sigma-dot), exothermic length = FWHM of sigma-dot.

ASSUMPTIONS: 1-D steady wave, frozen leading shock, detailed kinetics
(GRI-Mech 3.0); the frozen sound speed governs the local Mach number M.

OUTPUT: data/znd_sdt.json — per case: cj [m/s], x [mm], T [K], P/P1,
normalised thermicity, M, induction/exothermic lengths [mm], vN state.
The shipped file is the validated build artifact; re-running reproduces it
(energy invariant h + U^2/2 conserved to 6e-6 %, see validation/VALIDATION.md).

Usage:
    python znd_profiles.py                 # all four cases (~minutes)
    python znd_profiles.py "H2/air"        # single case
Expected (H2/air, 1 atm, 300 K): CJ = 1969 m/s, induction length 0.24 mm,
T_vN = 1532 K.
"""
import os, sys, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # repo root
sys.path.insert(0, ROOT)                               # vendored sdtoolbox/
import cantera as ct, numpy as np
from sdtoolbox.postshock import CJspeed, PostShock_fr
from sdtoolbox.znd import zndsolve

ct.suppress_thermo_warnings()
P1 = ct.one_atm; T1 = 300.0; mech = 'gri30.yaml'
OUT = os.path.join(ROOT, 'data', 'znd_sdt.json')

# (label, composition, t_end [s], max_step [s]) — tuned per mixture stiffness
CASES = [('H2/air',  'H2:2 O2:1 N2:3.76', 3.0e-6, 1.5e-8),
         ('H2/O2',   'H2:2 O2:1',         2.0e-6, 1.0e-8),
         ('CH4/O2',  'CH4:1 O2:2',        1.2e-5, 6.0e-8),
         ('C2H4/O2', 'C2H4:1 O2:3',       8.0e-6, 4.0e-8)]

if __name__ == '__main__':
    sel = sys.argv[1:] or [c[0] for c in CASES]
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for nm, q, tend, mstep in CASES:
        if nm not in sel:
            continue
        t0 = time.time()
        cj = CJspeed(P1, T1, q, mech)
        gas1 = ct.Solution(mech); gas1.TPX = T1, P1, q
        gas = PostShock_fr(cj, P1, T1, q, mech)
        z = zndsolve(gas, gas1, cj, relTol=1e-5, absTol=1e-9, t_end=tend,
                     max_step=mstep, advanced_output=True, Method='LSODA')
        rec = dict(cj=cj,
                   x=(z['distance']*1000).tolist(), T=z['T'].tolist(),
                   P=(z['P']/P1).tolist(),
                   thermicity=(z['thermicity']/max(z['thermicity'])).tolist(),
                   M=z['M'].tolist(),
                   ind_mm=z['ind_len_ZND']*1000, exo_mm=z['exo_len_ZND']*1000,
                   T_vN=float(z['T'][0]), p_vN=float(z['P'][0]/P1))
        out[nm] = rec
        print("%s: CJ=%.0f ind=%.4gmm exo=%.4gmm T_vN=%.0f Mend=%.3f (%.1fs)"
              % (nm, cj, rec['ind_mm'], rec['exo_mm'], rec['T_vN'],
                 z['M'][-1], time.time()-t0), flush=True)
        json.dump(out, open(OUT, 'w'))
    print("DONE", flush=True)
