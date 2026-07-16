"""example_design_study.py — end-to-end RDE design study using the repo as a library.

Scenario: a lab-scale rotating detonation engine on stoichiometric C2H4/O2,
DECLARED fill state 1 atm / 300 K (the operating point of the validated
SK-class tables), annular chamber with mean radius 45 mm, channel gap
5 mm, length 80 mm, total mass flow 0.30 kg/s; candidate pump-fed upgrade at
P_cp = 10 atm with a nozzle. Every physical number below comes from the
validated modules (imported as a package — no code is duplicated here except
the Wolanski wave-number formula, which is lecture material not owned by any
module):

 (a) CJ state and gamma_e ................ src.thrust.sk_models.cj_calc
 (b) fill height + Wolanski wave number
     -> expected number of wave heads .... this file (PCI 34, Eqs. 4-5) +
                                           ZND induction length (data/znd_sdt.json)
 (c) specific thrust and fuel-based Isp_f:
     SK pressure-history (Terms I + II)... src.thrust.sk_models.ph_calc
     SK axial flow (Eq. 44-45) ........... src.thrust.sk_models.axial_calc
 (d) frozen-composition expansion bound .. axial_calc(chem='frozen')
 (e) Fickett-Jacobs cycle efficiency ..... src.cycles.cycles.three_cycles
 (f) Stechmann nozzle optimization at P_cp
     (bell vs aerospike) ................. src.thrust.stechmann_nozzle

DESIGN-CHAIN RULES (consolidated; full derivation in SOLUTION_headtohead.md):
* Two degrees of freedom: of (F, mdot, Isp) fix TWO, never three. Here mdot
  = 0.30 kg/s is declared, the models return the INTENSIVE F/mdot and Isp,
  and F = mdot*(F/mdot) is derived. (The mission examples fix F instead and
  derive mdot = F/(g0*Isp).)
* Dual optimization protocols (Stechmann cycle):
  A. bell — analytic optimum NPR(eps*) = <Pc>/Pa (from dCF/deps =
     (Pe - Pa)/Pc at fixed Pc), verified by golden section;
  B. aerospike — saturation knee NPR(eps*) = P_max/Pa (the Eq.-12 validity
     limit: Isp(eps) is monotone below the knee, exactly flat above it).
* Two configurations, two area closures:
  - THROATLESS (both SK control volumes assume a FREE annulus exit, which is
    then the sonic throat): A_ann = mdot/G* with G* = rho*·w* at the
    validated sonic state, i.e. R_bar = mdot/(2*pi*gap*G*) — the diameter
    follows the mass flow;
  - NOZZLED (the aft restriction is the throat): A_t = mdot*cbar*/<Pc>; the
    annulus is then a detonability/mixing DOF (gap from ~2.4*lambda,
    D_bar >= 28*lambda), NOT a mass-flow consequence.
  The given R_bar = 45 mm is the NOZZLED configuration; the script prints
  the throatless closure R_bar(mdot) next to it for contrast.
* Fill-state provenance: the SK branch (a)-(d) runs at the DECLARED fill
  (1 atm / 300 K — a feed choice, not an ambient consequence: the choked
  exit decouples the chamber, and SK themselves back out SUB-atmospheric
  fills in their Kato comparison). The matched Stechmann branch (f) derives
  its own fill: P_init = 1.11 atm is an OUTPUT of the mass-matching fixed
  point at P_cp = 10 atm — that mission chain contains no 1-atm assumption.
  Residual approximation, declared: the SK leg is evaluated at 1.00 atm vs
  P_init = 1.11 atm (11% on fill pressure, <1% on every intensive result).
* Isp conventions: SK Isp_f is FUEL-based (F/(Y_f*g0*mdot), airbreathing
  style); Stechmann Isp in (f) is TOTAL-propellant (rocket convention).
  Do not compare the two directly.

Run:      python examples/example_design_study.py      (~15-60 s, all live)
Expected (see also README "Use as a design tool"):
  (a) U_CJ = 2373.5 m/s, p_CJ/p1 = 33.2, gamma_e = 1.139  (= shipped values)
  (b) fill height/rev = 20.1 mm, W = 2.69 (band 1.9-4.6) -> nominally 2-3
      co-rotating wave heads (conservative band 1-4)
  (c) F/Mdot = 1979 (PH, term II = 300) / 1905 (AX sonic) m/s;
      Isp_f = 892 / 859 s; F = 594 / 571 N at 0.30 kg/s;
      throatless closure G* = 428 kg/m2s -> R_bar = 22.3 mm at this mdot
      (given R_bar = 45 mm = nozzled configuration)
  (d) frozen bound: AX 1715 m/s (-10.0% vs equilibrium; Bray in between)
  (e) eta_FJ = 0.2042 (fuel-O2 dissociation penalty; fuel-air would be ~0.30)
  (f) at P_cp = 10 atm: fill P_init = 1.11 atm (matched-cycle OUTPUT);
      bell eps* = 2.44, Isp = 233.6 s; aerospike eps* = 6.27,
      Isp = 245.3 s (+5.0% -- it tracks the blowdown); choke margin 0.64 (the
      late-cycle tail dips below choking; Stechmann assumption 3 retained,
      exactly as the paper does on its 20 atm hydrocarbon rows);
      nozzled throat A_t = 5.2 cm2 (2.7:1 contraction from the annulus)
"""
import os, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)                                # repo root -> src/, sdtoolbox/
import numpy as np
import cantera as ct

from src.thrust.sk_models import cj_calc, ph_calc, axial_calc, CASES, ATM, G0
from src.thrust import stechmann_nozzle as stn
from src.cycles.cycles import three_cycles

# ----------------------------------------------------------- design inputs
KEY, FUEL, OX = 'C2H4/O2', 'C2H4', 'O2'   # propellant (any key of sk_models.CASES)
MDOT = 0.30                               # total mass flow [kg/s]
RBAR, GAP, LCH = 0.045, 0.005, 0.080      # mean radius, channel gap, length [m]
PCP_ATM = 10.0                            # CP-equivalent chamber pressure [atm]


def wolanski_wave_number(Vdot, l_cr, gap, u_D, Rbar):
    """Wolanski's detonation Wave Number (PCI 34, 2013, Eqs. 4-5).

    W = t_r / t_mf: one wave revolution t_r = pi*d/u_D over the time
    t_mf = V_cr / Vdot to refill the critical fresh-mixture volume
    V_cr = (pi/4)(d_o^2 - d_i^2) * l_cr.  With d_o^2 - d_i^2 = 2*d*h
    (d mean diameter, h = d_o - d_i = 2*gap) this is Eq. 5:

        W = 2 Vdot / (l_cr * h * u_D)  =  l_fill / l_cr,

    where l_fill = Vdot * t_r / A_annulus is the fresh-layer height laid
    down per revolution.  Interpretation (paper text): W = 1, 2, ... n ->
    n steady heads; W slightly < 1 -> galloping rotating detonation;
    W << 1 -> deflagration only.
    """
    h = 2.0 * gap                          # Wolanski's h = d_o - d_i
    d = 2.0 * Rbar
    A_ann = np.pi * d * h / 2.0            # = 2*pi*Rbar*gap, annulus cross-section
    t_r = np.pi * d / u_D
    l_fill = Vdot * t_r / A_ann
    return dict(W=2.0 * Vdot / (l_cr * h * u_D), l_fill=l_fill, t_r=t_r,
                u_fill=Vdot / A_ann)


print('=== RDE design study: %s, mdot=%.2f kg/s, Rbar=%.0f mm, gap=%.0f mm, '
      'L=%.0f mm ===' % (KEY, MDOT, 1e3 * RBAR, 1e3 * GAP, 1e3 * LCH))
SHIP = json.load(open(os.path.join(ROOT, 'data', 'thrust_models_all.json')))['cases'][KEY]

# ------------------------------------------------- (a) CJ state and gamma_e
cj = cj_calc(KEY)                                        # live, ~3 s
print('\n(a) CJ state (live SD Toolbox): U_CJ = %.1f m/s, p_CJ/p1 = %.2f, '
      'T_CJ = %.0f K,\n    gamma_e = %.4f (gamma_fr = %.4f) — shipped: '
      'U = %.1f, err %+.3f%%'
      % (cj['UCJ'], cj['p2p1'], cj['T2'], cj['gamma_e'], cj['gamma_fr'],
         SHIP['cj']['UCJ'], 100 * (cj['UCJ'] / SHIP['cj']['UCJ'] - 1)))
assert abs(cj['UCJ'] / SHIP['cj']['UCJ'] - 1) < 2e-3, 'CJ regression vs shipped data'

# ------------------------- (b) fill height, Wolanski wave number, wave heads
gas = ct.Solution(CASES[KEY]['mech'])
gas.set_equivalence_ratio(1.0, FUEL, OX)
gas.TP = cj['cond']['T1'], cj['cond']['P1']
rho1 = gas.density
Vdot = MDOT / rho1
# critical fill height from the repo's ZND induction length:
#   cell size lambda ~ 29 * Delta_i (Westbrook-type engineering multiplier;
#   mixture-specific values scatter ~10-60, Ng et al. 2007), then Bykovskii's
#   criterion l_cr = (12 +/- 5) * lambda. Order-of-magnitude design guidance,
#   NOT a validated result — carry the band, not the central value alone.
di = json.load(open(os.path.join(ROOT, 'data', 'znd_sdt.json')))[KEY]['ind_mm'] * 1e-3
lam = 29.0 * di
lcr, lcr_lo, lcr_hi = 12.0 * lam, 7.0 * lam, 17.0 * lam
wn = wolanski_wave_number(Vdot, lcr, GAP, cj['UCJ'], RBAR)
W, Wlo, Whi = wn['W'], wolanski_wave_number(Vdot, lcr_hi, GAP, cj['UCJ'], RBAR)['W'], \
    wolanski_wave_number(Vdot, lcr_lo, GAP, cj['UCJ'], RBAR)['W']
print('\n(b) injection: rho1 = %.3f kg/m3, Vdot = %.3f m3/s, axial fill speed '
      '= %.0f m/s\n    ZND induction %.4f mm -> cell size ~%.2f mm -> l_cr = '
      '%.1f mm [%.1f..%.1f]\n    fill height per revolution l_fill = %.1f mm '
      '(t_r = %.0f us; l_fill/L = %.0f%%)\n    Wolanski W = %.2f (band '
      '%.2f..%.2f) -> expect %d-%d co-rotating head(s)'
      % (rho1, Vdot, wn['u_fill'], 1e3 * di, 1e3 * lam, 1e3 * lcr, 1e3 * lcr_lo,
         1e3 * lcr_hi, 1e3 * wn['l_fill'], 1e6 * wn['t_r'],
         100 * wn['l_fill'] / LCH, W, Wlo, Whi, max(1, int(Wlo)), int(Whi)))
assert abs(wn['W'] - wn['l_fill'] / lcr) < 1e-12          # Eq. 5 == fill-height form
assert W >= 1.0, 'W < 1: galloping/failing design — raise mdot or shrink chamber'
assert GAP > 2.4 * lam, ('channel gap below the documented ~2.4*lambda '
                         'detonability criterion (docstring / headtohead)')
assert 2 * RBAR >= 28 * lam, 'mean diameter below the D_bar >= 28*lambda criterion'
assert wn['l_fill'] < LCH, 'chamber shorter than the fresh fill layer'

# ---------------- (c) specific thrust and Isp_f: SK pressure-history + axial
ph = ph_calc(cj, CASES[KEY]['K'])                        # Terms I + II
ax = axial_calc(cj, FUEL, OX)                            # equilibrium isentrope
print('\n(c) SK models at the DECLARED fill (%.2f atm / %.0f K; Pa = 1 atm; '
      'Isp_f = fuel-based):\n    pressure-history: F/Mdot = %.1f m/s (term I '
      '%.1f + term II %.1f), Isp_f = %.0f s\n    SK axial flow (sonic): '
      'F/Mdot = %.1f m/s, Isp_f = %.0f s (matched-exit %.0f s)'
      % (cj['cond']['P1'] / ATM, cj['cond']['T1'],
         ph['FovM'], ph['FI'], ph['FII'], ph['Ispf'],
         ax['FovM_sonic'], ax['Ispf_sonic'], ax['Ispf_matched']))
assert abs(ph['FovM'] / SHIP['ph']['FovM'] - 1) < 5e-3
assert abs(ax['FovM_sonic'] / SHIP['axial']['FovM_sonic'] - 1) < 5e-3
print('    thrust at mdot = %.2f kg/s: F = %.0f N (PH) / %.0f N (AX)'
      % (MDOT, MDOT * ph['FovM'], MDOT * ax['FovM_sonic']))
# Area closure, THROATLESS configuration: both SK control volumes assume a
# FREE annulus exit, which is then the sonic throat -> A_ann = mdot/G* with
# G* = rho*·w* at the validated sonic state; the mean radius FOLLOWS the
# mass flow, R_bar = mdot/(2*pi*gap*G*).  The given 45-mm annulus is instead
# the NOZZLED configuration (aft-restriction throat, closed in section (f)).
Gstar = ax['rhostar'] * ax['wstar']              # sonic mass flux G* [kg/m2/s]
Rbar_tl = MDOT / (2 * np.pi * GAP * Gstar)       # throatless annulus closure
print('    area closure — THROATLESS config (SK free annulus exit = sonic '
      'throat):\n    G* = rho*·w* = %.0f kg/m2s -> R_bar = mdot/(2 pi gap G*)'
      ' = %.1f mm;\n    the given R_bar = %.0f mm is the NOZZLED config '
      '(aft throat, sized in (f))'
      % (Gstar, 1e3 * Rbar_tl, 1e3 * RBAR))

# --------------------------- (d) frozen bound of the axial expansion bracket
axf = axial_calc(cj, FUEL, OX, chem='frozen')
print('\n(d) recombination bracket (axial, sonic): frozen %.1f <= physical <= '
      'equilibrium %.1f m/s\n    (frozen composition loses %.1f%% — Bray '
      'sudden-freeze would land in between)'
      % (axf['FovM_sonic'], ax['FovM_sonic'],
         100 * (1 - axf['FovM_sonic'] / ax['FovM_sonic'])))
assert axf['FovM_sonic'] < ax['FovM_sonic'], 'frozen must lower-bound equilibrium'

# ------------------------------------- (e) Fickett-Jacobs cycle efficiency
fj = three_cycles(KEY, 'C2H4:1 O2:3', 'gri30.yaml', do_HB=False, n_exp=12)
ref = json.load(open(os.path.join(ROOT, 'data', 'cycles_ws.json')))['fj_mixtures'][KEY]
print('\n(e) Fickett-Jacobs (live, 300 K / 1 bar): eta_FJ = %.4f, q_c = %.2f '
      'MJ/kg — shipped %.4f\n    (fuel-O2 dissociation penalty: fuel-air '
      'cycles reach ~0.28-0.31)'
      % (fj['eta_FJ'], fj['qc_MJkg'], ref['eta_FJ']))
assert abs(fj['eta_FJ'] - ref['eta_FJ']) < 1e-3

# ----------------- (f) Stechmann nozzle optimization at the chosen P_cp
# C2H4 is not one of the paper's Table-1 propellants: register it, then run
# the same matched-cycle + optimization machinery used for the 18/18 rows.
stn.PROPS['C2H4'] = ('data/gri30_CHO_eq.yaml', 'C2H4', 'O2')
s = stn.matched('C2H4', 1.0, cj['cond']['T1'], PCP_ATM)  # det cycle matched to CP
gd, Pa = s['gamma'], 1.0 * ATM
Pmean = s['P0'] * stn.Ik(s['PR'], 1.0)                   # time-mean chamber pressure
bell = lambda e: stn.cycle_isp(s, lambda Pc, e=e: stn.cf_bell(gd, e, Pc, Pa))
spik = lambda e: stn.cycle_isp(s, lambda Pc, e=e: stn.cf_spike(gd, e, Pc, Pa))
ob, _, _ = stn.bell_opt(bell, Pmean, Pa, gd, PCP_ATM)
os_, _, _ = stn.spike_opt(spik, s['P0'], Pa, gd, PCP_ATM)
print('\n(f) Stechmann matched det cycle at P_cp = %.0f atm (Ti = %.0f K, '
      'Pa = 1 atm; total-propellant Isp):\n    P_CJ = %.1f atm, fill P_init '
      '= %.2f atm (matched-cycle OUTPUT — the mission chain\n    contains no '
      '1-atm assumption), PR = %.1f, gamma = %.4f, DC shift = %+.1f%%,\n    '
      'choke margin %.2f\n    bell:      eps* = %5.2f  Isp = %.1f '
      's  (NPR* = <Pc>/Pa check: |deps| = %.1e)\n    aerospike: eps* = %5.2f  '
      'Isp = %.1f s  -> +%.1f%% over the fixed bell at sea level'
      % (PCP_ATM, cj['cond']['T1'], s['P0a'], s['Pinita'], s['PR'], gd,
         100 * s['DC'], s['choke_margin'], ob['eps'], ob['Isp'],
         ob['gs_vs_analytic'], os_['eps'], os_['Isp'],
         100 * (os_['Isp'] / ob['Isp'] - 1)))
# Area closure, NOZZLED configuration: with an aft-restriction throat the
# mass flow fixes A_t (NOT the annulus): A_t = mdot*cbar*/<Pc> with cbar* =
# mass-weighted c* of the cycle; the annulus is a detonability/mixing DOF.
kk = (gd + 1) / (2 * gd)
cbar = s['cstar0'] * stn.Ik(s['PR'], 1.0) / stn.Ik(s['PR'], kk)
At = MDOT * cbar / Pmean
print('    area closure — NOZZLED config at mdot = %.2f kg/s: A_t = '
      'mdot·cbar*/<Pc> = %.1f cm2\n    (annulus 2 pi Rbar gap = %.1f cm2 -> '
      '%.1f:1 contraction; annulus = detonability DOF)'
      % (MDOT, 1e4 * At, 1e4 * 2 * np.pi * RBAR * GAP,
         2 * np.pi * RBAR * GAP / At))
if s['choke_margin'] < 1.0:
    print('    note: choke margin < 1 — the low-pressure tail of the blowdown '
          'is not strictly\n    choked; Stechmann assumption 3 is retained '
          'there, as the paper itself does.')
assert os_['Isp'] >= ob['Isp'] - 0.05, 'ideal aerospike must not lose to fixed bell'
assert os_['monotone_below'], 'spike Isp(eps) must be monotone below the knee'

print('\nOK: design study complete — all cross-checks against shipped '
      'validated data passed.')
