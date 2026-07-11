"""Second worked case -- 10 kN class, CH4/O2 (LOX/methane class hardware).
MISSION: ground static demo, F = 10 kN at sea level, P_a = 1 atm; envelope
OD <= 320 mm x L <= 260 mm; CH4/O2 phi = 1, T1 = 300 K; CP combustor
L* = 1.0 m (LOX/CH4). Same validated chain as example_design_study /
example_headtohead (asserts on CJ). Consolidated rules:
* Feed equivalence (Stechmann protocol): equal mass per cycle through equal
  throat area at P_cp = 20 atm -> <Pc> = P_cp(1+DC), same pump class. The
  matched-cycle fill is an OUTPUT (P_init, printed in (f)): that mission
  chain contains no 1-atm assumption. 'fill 1 atm / 300 K' is the DECLARED
  state of the SK leg only (lab-class validated tables; the choked annulus
  exit decouples the chamber from ambient, so fill is a feed choice).
* Two-DOF rule: F is fixed, Isp is intensive from each model, and the TWO
  mdot are DERIVED, one per declared basis: mission mdot = F/(g0*Isp_spike)
  (NOZZLED configuration: aft throat A_t = mdot*cbar/<Pc>) vs SK bracket
  mdot = F/(F/Mdot) (THROATLESS configuration: annulus = throat, closure
  R_bar = mdot/(2 pi gap G*) = 142.1 mm vs chosen 140 mm, -1.5%).
* Protocols: A (bell) analytic NPR* = <Pc>/Pa; B (aerospike) saturation
  knee NPR* = P_max/Pa. SK 'F/mdot' lines are specific thrust on TOTAL
  mdot; Stechmann/CP 'Isp' are total-propellant.
EXPECTED: U_CJ 2390.3 m/s, W 3.14 -> ~3 heads; RDE bell 268.0 s @ eps* 4.04
| spike 278.4 s @ 10.64; CP 261.2 s @ 4.04; verdict +6.6% Isp, -6% propellant."""
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.thrust.sk_models import cj_calc, ph_calc, axial_calc, CASES, ATM, G0
import cantera as ct
import src.thrust.stechmann_nozzle as stn
F, T1, PCP, Pa, LSTAR = 10e3, 300.0, 20, 1*ATM, 1.0
RBAR, GAP, L = 0.140, 0.015, 0.180          # annulus [m]
LAM = 2.5e-3                                 # cell size CH4/O2 [m] (Caltech DB 2.5+-0.4)
cj = cj_calc('CH4/O2'); U, ge = cj['UCJ'], cj['gamma_e']
gas = ct.Solution(CASES['CH4/O2']['mech']); gas.set_equivalence_ratio(1.0,'CH4','O2'); gas.TP = cj['cond']['T1'], cj['cond']['P1']
ph = ph_calc(cj, CASES['CH4/O2']['K']); ax = axial_calc(cj, 'CH4', 'O2')
mdot_sk = F/ph['FovM']            # nozzle-less chamber bracket (SK)
s = stn.matched('CH4', 1.0, T1, PCP); gd = s['gamma']
Pmean = s['P0']*stn.Ik(s['PR'], 1.0)
bell = lambda e: stn.cycle_isp(s, lambda Pc, e=e: stn.cf_bell(gd, e, Pc, Pa))
spik = lambda e: stn.cycle_isp(s, lambda Pc, e=e: stn.cf_spike(gd, e, Pc, Pa))
ob,_,_ = stn.bell_opt(bell, Pmean, Pa, gd, PCP); osp,_,_ = stn.spike_opt(spik, s['P0'], Pa, gd, PCP)
mdot_m = F/(osp['Isp']*G0)          # mission mdot, nozzle configuration (spike)
print(f"    mission mdot (with nozzle) = {mdot_m:.2f} kg/s; SK nozzle-less bracket = {mdot_sk:.2f} kg/s (declared bases)")
rho1 = gas.density; A_ann = 2*np.pi*RBAR*GAP
u_fill = mdot_m/(rho1*A_ann); t_lap = 2*np.pi*RBAR/U; l_fill = u_fill*t_lap
lcr = 12*LAM; W = l_fill/lcr
print(f"(a) CJ CH4/O2: U_CJ={U:.1f} m/s  p2/p1={cj['p2p1']:.1f}  gamma_e={ge:.4f}")
print(f"(c) SK chamber bracket (fill 1 atm / 300 K declared): F/mdot PH={ph['FovM']:.0f} m/s (Term II {100*ph['FII']/ph['FovM']:.0f}%) | axial sonic={ax['FovM_sonic']:.0f} m/s")
print(f"(b/d) l_fill={l_fill*1e3:.0f} mm ({100*l_fill/L:.0f}% of L)  checks: l_fill/lam={l_fill/LAM:.0f} (>=12+-5)  gap/lam={GAP/LAM:.1f}  Dbar/lam={2*RBAR/LAM:.0f} (>=28)")
print(f"      W={W:.2f} [{l_fill/(17*LAM):.2f}-{l_fill/(7*LAM):.2f}] -> ~{max(1,round(W))} heads")
cs = stn.cp_state('CH4', 1.0, T1, PCP); g, cst = cs['gamma'], cs['cstar']
E = np.linspace(1.05, 15, 500); CF = np.array([stn.cf_bell(g, e, PCP*ATM, Pa) for e in E])
i = CF.argmax(); Isp_cp = cst*CF[i]/G0; mcp = F/(Isp_cp*G0)
At = mcp*cst/(PCP*ATM); Lc = LSTAR*At/(np.pi/4*0.22**2)
print(f"(f) RDE @20 atm (fill P_init={s['Pinita']:.2f} atm, matched OUTPUT): bell eps*={ob['eps']:.2f} Isp={ob['Isp']:.1f} s | spike eps*={osp['eps']:.2f} Isp={osp['Isp']:.1f} s (choke margin {s['choke_margin']:.2f})")
print(f"CP  @20 atm: eps*={E[i]:.2f} Isp={Isp_cp:.1f} s  mdot={mcp:.2f} kg/s  A_t={At*1e4:.0f} cm2  L_ch(0.22 m bore)={Lc*1e3:.0f} mm (+nozzle)")
print(f"VERDICT 10 kN: spike vs CP {100*(osp['Isp']/Isp_cp-1):+.1f}% Isp, {100*(mdot_m/mcp-1):+.0f}% propellant; CP combustor {Lc*1e3:.0f} mm vs RDE annulus {L*1e3:.0f} mm (heat release at cell scale)")
assert abs(U-2390.4) < 2.0
