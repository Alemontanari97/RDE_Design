"""Head-to-head at each design's OWN optimum — RDE vs conventional CP engine.
Same mission (F = 600 N, sea level), same propellant (C2H4/O2, phi = 1), same
feed (P_cp = 10 atm), same Stechmann framework (validated 18/18 vs Table 1).
The verdict is NOT assumed: each engine is optimized independently.
Expected output (validated 2026-07-10):
  CP  : gamma_s 1.1247, c* 1746 m/s, eps* 2.44 (matched), Isp_SL 227.4 s,
        mdot 269 g/s, L* = 0.9 m -> chamber ~66 mm (fits the 100 mm envelope)
  RDE : bell 233.6 s (eps* 2.44, +2.7%) | aerospike 245.3 s (eps* 6.27, +7.9%)
        mdot 249 g/s -> -7% propellant at the same thrust and the same pump.
Note: eps*_bell coincides CP/det (NPR* = <Pc>/Pa and the det cycle is matched
on the same mean pressure); the aerospike rides the blowdown swing to 6.27.
At larger thrust the CP combustor grows with V_c = L*·A_t ~ mdot, while the
RDE heat-release zone stays at cell scale: the envelope argument sharpens.
"""
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import src.thrust.stechmann_nozzle as stn
from src.thrust.sk_models import ATM, G0
stn.PROPS['C2H4'] = ('data/gri30_CHO_eq.yaml', 'C2H4', 'O2')
T1, PcpA, Pa, F, Lstar = 300.0, 10, 1*ATM, 600.0, 0.9
cs = stn.cp_state('C2H4', 1.0, T1, PcpA); g, cstar = cs['gamma'], cs['cstar']
eps = np.linspace(1.05, 12, 600)
CF = np.array([stn.cf_bell(g, e, PcpA*ATM, Pa) for e in eps])
i = CF.argmax(); Isp_cp = cstar*CF[i]/G0; mdot = F/(Isp_cp*G0)
At = mdot*cstar/(PcpA*ATM); Lc = Lstar*At/(np.pi/4*0.09**2)
print(f"CP  optimum: eps*={eps[i]:.2f}  Isp={Isp_cp:.1f} s  mdot={mdot*1e3:.0f} g/s  L_chamber={Lc*1e3:.0f} mm (L*={Lstar} m)")
print(f"RDE optimum: bell 233.6 s | aerospike 245.3 s  (example_design_study.py)")
print(f"VERDICT: +{100*(245.3/Isp_cp-1):.1f}% Isp, {100*(F/(245.3*G0)/mdot-1):+.0f}% propellant, same pump.")
assert abs(Isp_cp-227.4) < 0.5 and abs(eps[i]-2.44) < 0.05
