"""example_cj.py — Chapman-Jouguet detonation of stoichiometric H2/air, end to end.

Computes the CJ speed with the vendored SD Toolbox (equilibrium-Hugoniot method,
GALCIT FM2018.001) and the equilibrium CJ state, then checks both against the
Caltech detonation database / CEA reference and against the shipped validated
results (data/thrust_models_all.json).

Run:      python examples/example_cj.py            (~1-2 min: full CJ search)
Expected: U_CJ = 1969 m/s (ref 1971 m/s, err -0.10%), p2/p1 = 15.5, T2 = 2944 K.
"""
import os, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)                       # vendored sdtoolbox/
import cantera as ct
from sdtoolbox.postshock import CJspeed, PostShock_eq

ct.suppress_thermo_warnings()
P1, T1, mech = ct.one_atm, 300.0, 'gri30.yaml'
q = 'H2:2 O2:1 N2:3.76'                        # stoichiometric H2/air

U = CJspeed(P1, T1, q, mech)                   # min wave speed on the eq. Hugoniot
eq = PostShock_eq(U, P1, T1, q, mech)          # equilibrium CJ (post-wave) state

ref = json.load(open(os.path.join(ROOT, 'data', 'thrust_models_all.json')))
cj0 = ref['cases']['H2/air']['cj']             # shipped validated CJ state

print(f"stoichiometric H2/air at 1 atm, {T1:.0f} K  (gri30.yaml, SD Toolbox)")
print(f"  U_CJ  = {U:7.1f} m/s   | Caltech DB/CEA 1971 m/s  -> err {U/1971.0-1:+.2%}")
print(f"  p2/p1 = {eq.P/P1:7.2f}       | shipped validated value {cj0['p2p1']:.2f}")
print(f"  T2    = {eq.T:7.1f} K     | shipped validated value {cj0['T2']:.1f} K")
assert abs(U/1971.0 - 1.0) < 0.005, "U_CJ off the literature value"
assert abs(U/cj0['UCJ'] - 1.0) < 0.002 and abs(eq.T/cj0['T2'] - 1.0) < 0.002
print("OK: CJ state reproduces literature (<0.5%) and shipped data (<0.2%)")
