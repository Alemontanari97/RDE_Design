"""Head-to-head at each design's OWN optimum -- RDE vs conventional CP engine.

MISSION (explicit): ground static demonstrator. F = 600 N at sea level,
P_a = 101.325 kPa constant (no trajectory, no altitude compensation credit);
envelope OD <= 110 mm x L <= 100 mm (usable bore 90 mm, exit D_e <= 100 mm);
propellant C2H4/O2, phi = 1, T1 = 300 K; feed equivalence: SAME mean chamber
pressure P_cp = 10 atm for both engines (= same specific pump work; injector
drop not modelled); CP combustor sized by L* = 0.9 m (LOX/HC class).

FORMAL PROBLEM (each engine independently):
  max_{eps, mdot} Isp(eps)  s.t.  F = mdot*g0*Isp;  D_e(eps) <= 100 mm;
  CP: L_chamber(L*, A_t(mdot)) <= envelope;  det: choking/assert referees.
  Bell optimum: analytic NPR*(eps*) = <Pc>/Pa (golden-section verified);
  aerospike optimum: Eq.-12 saturation knee NPR* = P_max/Pa.

EXPECTED (validated 2026-07-10, sea level):
  CP  : eps* 2.44, Isp 227.4 s, mdot 269 g/s, L_chamber ~66 mm (fits)
  RDE : bell 233.6 s (+2.7%) | aerospike 245.3 s (eps* 6.27, +7.9%), -7% propellant
VACUUM EXTENSION (same envelope, eps capped at 15 by D_e): informative print --
the matched bell loses its altitude match, the aerospike self-adapts.
"""
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import src.thrust.stechmann_nozzle as stn
from src.thrust.sk_models import ATM, G0
stn.PROPS['C2H4'] = ('data/gri30_CHO_eq.yaml', 'C2H4', 'O2')
T1, PCP_A, F, LSTAR, BORE, EPS_VAC = 300.0, 10, 600.0, 0.9, 0.09, 15.0
Pa_SL, Pa_VAC = 1*ATM, 1e-4*ATM

# ---- CP engine at ITS optimum (sea level) ----
cs = stn.cp_state('C2H4', 1.0, T1, PCP_A); g, cstar = cs['gamma'], cs['cstar']
eps = np.linspace(1.05, 12, 600)
CF = np.array([stn.cf_bell(g, e, PCP_A*ATM, Pa_SL) for e in eps])
i = CF.argmax(); Isp_cp = cstar*CF[i]/G0; mdot_cp = F/(Isp_cp*G0)
At = mdot_cp*cstar/(PCP_A*ATM); Lc = LSTAR*At/(np.pi/4*BORE**2)
print(f"SL  CP : eps*={eps[i]:.2f}  Isp={Isp_cp:.1f} s  mdot={mdot_cp*1e3:.0f} g/s  L_ch={Lc*1e3:.0f} mm (L*={LSTAR} m, fits)")

# ---- det cycle (matched to the same mean pressure) ----
s = stn.matched('C2H4', 1.0, T1, PCP_A); gd = s['gamma']
Pmean = s['P0']*stn.Ik(s['PR'], 1.0)
bell = lambda e, Pa: stn.cycle_isp(s, lambda Pc, e=e: stn.cf_bell(gd, e, Pc, Pa))
spik = lambda e, Pa: stn.cycle_isp(s, lambda Pc, e=e: stn.cf_spike(gd, e, Pc, Pa))
ob,_,_ = stn.bell_opt(lambda e: bell(e, Pa_SL), Pmean, Pa_SL, gd, PCP_A)
os_,_,_ = stn.spike_opt(lambda e: spik(e, Pa_SL), s['P0'], Pa_SL, gd, PCP_A)
print(f"SL  RDE: bell eps*={ob['eps']:.2f} Isp={ob['Isp']:.1f} s | spike eps*={os_['eps']:.2f} Isp={os_['Isp']:.1f} s")
print(f"SL  VERDICT: +{100*(os_['Isp']/Isp_cp-1):.1f}% Isp, {100*(F/(os_['Isp']*G0)/mdot_cp-1):+.0f}% propellant, same pump.")

# ---- vacuum extension: eps capped by the envelope (D_e <= 100 mm -> eps ~ 15) ----
Isp_cp_v = cstar*stn.cf_bell(g, EPS_VAC, PCP_A*ATM, Pa_VAC)/G0
print(f"VAC CP : eps={EPS_VAC:.0f} (envelope-capped)  Isp={Isp_cp_v:.1f} s")
print(f"VAC RDE: bell {bell(EPS_VAC, Pa_VAC):.1f} s | spike {spik(EPS_VAC, Pa_VAC):.1f} s "
      f"(+{100*(spik(EPS_VAC, Pa_VAC)/Isp_cp_v-1):.1f}% vs CP)")

assert abs(Isp_cp-227.4) < 0.5 and abs(eps[i]-2.44) < 0.05
assert abs(ob['Isp']-233.6) < 0.7 and abs(os_['Isp']-245.3) < 0.7
