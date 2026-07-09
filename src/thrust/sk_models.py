#!/usr/bin/env python3
"""
sk_models.py -- SOTA analytical RDE thrust models for ALL propellant combos.
Lecture-repo edition of project_build/scripts/thrust_models.py (verbatim physics;
paths adapted to the repo layout).
Faithful implementations of:
 [PH] Shepherd & Kasahara, GALCIT FM2017.001 (2017), Sec.3 "pressure history":
      F_I/Mdot  = K*(P_CJ - P_c1)/(rho_c*U_CJ)   (Eqs. 6,15,17,18; exact DeltaP_CJ)
      F_II/Mdot = u_c + (P_c1 - P_a)/(rho_c*u_c) (Eqs. 7-8; u_c = 300 m/s, S&K 2013)
      K = 1/alpha from psi(xi)=exp(-alpha*xi) tail fit (Eq. 14,16):
      K = 1.02 (fuel-air, alpha=0.98), K = 1.54 (fuel-O2, alpha=0.65).
      Headline approx (Eq. 19-20): F_I/Mdot ~= K*U_CJ/(gamma_e+1), gamma_e EQUILIBRIUM.
 [AX] ibid. Sec.4 "axial flow": w = sqrt(2*(h1 - h(P,s2))) on the EQUILIBRIUM isentrope
      through the CJ state (Eq. 44); T/Mdot = w + (P-Pa)/(rho*w) (Eq. 45);
      tabulated at the sonic point w = a_eq (as SK Table 1); P_m: h(P_m,s2)=h1.
 [ST] Stechmann, Heister & Harroun, J. Spacecraft & Rockets 56(3) 2019 (10.2514/1.A34313):
      mass-weighted cycle Isp (Eq. 4-5): Isp = int(mdot*Cf*cstar)dt / (g*int(mdot)dt),
      exponential blowdown Pc(t)=PR*Pinit*exp(-lambda t), lambda=ln(PR)/tc (Eq. 13-14),
      isentropic Tc (Eq. 15), choked exit mdot ~ Pc/cstar (Eq. 6-8),
      Cf bell eps=1 (Eq. 9) and ideal aerospike Pe=Pa (Eq. 10).
Conditions: phi=1, P1=1 atm, T1=300 K (std);  SKREP:* cases at 1.5 atm / 255 K
(Schwer & Kailasanath 2013 fill state) for literature convergence checks.
Usage:  python3 sk_models.py <stage> <case> [<case> ...]
        stage in {cj, ph, axial, stech, all};  case keys as in CASES below.
"""
import sys, os, json
PROJ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # repo root
sys.path.insert(0, PROJ)
import numpy as np
import cantera as ct
from sdtoolbox.postshock import CJspeed, PostShock_eq
try:
    from sdtoolbox.thermo import soundspeed_eq as _aeq_sdt
except Exception:
    _aeq_sdt = None
ct.suppress_thermo_warnings()

G0 = 9.80665; ATM = 101325.0; PA = ATM          # ambient (sea level, as SK Table 1)
UC = 300.0                                       # inlet axial speed, S&K 2013 (SK Sec.5)
GRI = 'gri30.yaml'; DOD = 'nDodecane_Reitz.yaml'
# reduced THERMO-only mech for kerosene surrogate (equilibrium needs no kinetics):
# 16 Reitz species + NO,N,N2O,NO2 thermo grafted from GRI-3.0 (see make step in log)
DODEQ = os.path.join(PROJ, 'data', 'dodecane_eq_thermo.yaml')
AIR = 'O2:1,N2:3.76'; AIRD = 'o2:1,n2:3.76'

CASES = {
 'H2/air'    : dict(mech=GRI, fuel='H2',    ox=AIR,  K=1.02),
 'H2/O2'     : dict(mech=GRI, fuel='H2',    ox='O2', K=1.54),
 'CH4/air'   : dict(mech=GRI, fuel='CH4',   ox=AIR,  K=1.02),
 'CH4/O2'    : dict(mech=GRI, fuel='CH4',   ox='O2', K=1.54),
 'C2H4/air'  : dict(mech=GRI, fuel='C2H4',  ox=AIR,  K=1.02),
 'C2H4/O2'   : dict(mech=GRI, fuel='C2H4',  ox='O2', K=1.54),
 'C2H2/air'  : dict(mech=GRI, fuel='C2H2',  ox=AIR,  K=1.02),
 'C2H2/O2'   : dict(mech=GRI, fuel='C2H2',  ox='O2', K=1.54),
 'C3H8/air'  : dict(mech=GRI, fuel='C3H8',  ox=AIR,  K=1.02),
 'C3H8/O2'   : dict(mech=GRI, fuel='C3H8',  ox='O2', K=1.54),
 'C12H26/air': dict(mech=DODEQ, fuel='c12h26', ox=AIRD, K=1.02),
 'C12H26/O2' : dict(mech=DODEQ, fuel='c12h26', ox='o2', K=1.54),
}
for _c in ['H2/air', 'C2H4/air', 'C2H4/O2', 'C3H8/O2']:   # SK Table-1 replicas
    CASES['SKREP:' + _c] = dict(CASES[_c], T1=255.0, P1=1.5 * ATM)

DATA = os.path.join(PROJ, 'data', 'thrust_models_all.json')

def load():
    if os.path.exists(DATA):
        return json.load(open(DATA))
    return {'meta': {}, 'cases': {}}

def save(d):
    tmp = DATA + '.tmp'
    json.dump(d, open(tmp, 'w'), indent=1)
    os.replace(tmp, DATA)

def setup(key):
    c = CASES[key]
    T1 = c.get('T1', 300.0); P1 = c.get('P1', ATM)
    gas = ct.Solution(c['mech'])
    gas.set_equivalence_ratio(1.0, c['fuel'], c['ox'])
    gas.TP = T1, P1
    q = ' '.join('%s:%.6f' % (k, v) for k, v in gas.mole_fraction_dict().items() if v > 1e-9)
    return c, T1, P1, gas, q

def aeq(gas):
    """Equilibrium sound speed a2 = sqrt(dP/drho|s,eq) (finite diff, 2 SP-equilibrations)."""
    if _aeq_sdt is not None:
        return _aeq_sdt(gas)
    s0, P0, X0 = gas.entropy_mass, gas.P, gas.X.copy()
    dP = 1e-4 * P0; r = []
    for P in (P0 - dP, P0 + dP):
        g = ct.Solution(gas.source if hasattr(gas, 'source') else gas.name)
        g.SPX = s0, P, X0; g.equilibrate('SP'); r.append(g.density)
    return float(np.sqrt(2 * dP / (r[1] - r[0])))

# ---------------------------------------------------------------- stage: CJ state
def stage_cj(key):
    c, T1, P1, gas, q = setup(key)
    h1 = gas.enthalpy_mass; rho1 = gas.density; a1f = gas.sound_speed
    Yf = float(gas[c['fuel']].Y[0]); M1w = gas.mean_molecular_weight
    U = float(CJspeed(P1, T1, q, c['mech']))
    g2 = PostShock_eq(U, P1, T1, q, c['mech'])
    P2, T2, rho2 = g2.P, g2.T, g2.density
    a2 = float(aeq(g2)); ge = rho2 * a2**2 / P2
    w2 = U * rho1 / rho2
    rec = dict(cond=dict(T1=T1, P1=P1, phi=1.0, mech=c['mech'], q=q),
               UCJ=U, MCJ=U / a1f, p2p1=P2 / P1, P2=float(P2), T2=float(T2),
               rho1=float(rho1), rho2=float(rho2), s2=float(g2.entropy_mass),
               h1=float(h1), h2=float(g2.enthalpy_mass), a_eq2=a2, w2=float(w2),
               u2lab=float(U - w2), gamma_e=float(ge), gamma_fr=float(g2.cp / g2.cv),
               Yf=Yf, M1w=float(M1w), M2w=float(g2.mean_molecular_weight),
               cj_sonic_resid=float(abs(w2 / a2 - 1.0)))
    d = load(); d['cases'].setdefault(key, {}); d['cases'][key]['cj'] = rec; save(d)
    print('%s CJ: U=%.1f p2/p1=%.2f T2=%.0f ge=%.4f sonic_resid=%.4f'
          % (key, U, P2 / P1, T2, ge, rec['cj_sonic_resid']), flush=True)

# ---------------------------------------------------------------- stage: SK pressure history
def stage_ph(key):
    d = load(); cj = d['cases'][key]['cj']; c = CASES[key]
    P1 = cj['cond']['P1']; dP = cj['P2'] - P1
    FI = c['K'] * dP / (cj['rho1'] * cj['UCJ'])            # term I, exact DeltaP_CJ
    FII = UC + (P1 - PA) / (cj['rho1'] * UC)               # term II (Eq. 7)
    F = FI + FII
    Fap = c['K'] * cj['UCJ'] / (cj['gamma_e'] + 1.0)       # headline approx, term I only
    ph = dict(K=c['K'], alpha=1.0 / c['K'], uc=UC, Pa=PA, FI=FI, FII=FII, FovM=F,
              Ispf=F / (cj['Yf'] * G0), Ispf_I=FI / (cj['Yf'] * G0),
              Isp_tot=F / G0,
              FovM_approx_I=Fap, Ispf_approx_I=Fap / (cj['Yf'] * G0))
    d['cases'][key]['ph'] = ph; save(d)
    print('%s PH: FI=%.1f FII=%.1f F/M=%.1f m/s Ispf=%.0f s' % (key, FI, FII, F, ph['Ispf']), flush=True)

# ---------------------------------------------------------------- stage: SK axial flow
def _sp_state(gas, s2, P, X_seed=None):
    if X_seed is not None:
        gas.SPX = s2, P, X_seed
    else:
        gas.SP = s2, P
    gas.equilibrate('SP')
    return gas

def stage_axial(key, nstep=90, pfloor=0.012):
    d = load(); cj = d['cases'][key]['cj']; c = CASES[key]
    gas = ct.Solution(c['mech']); gas.set_equivalence_ratio(1.0, c['fuel'], c['ox'])
    gas.TP = cj['cond']['T1'], cj['cond']['P1']; X1 = gas.X.copy()
    h1 = gas.enthalpy_mass
    gas.TPX = cj['T2'], cj['P2'], X1; gas.equilibrate('TP')     # rebuild CJ equilibrium
    s2 = gas.entropy_mass
    P2 = cj['P2']
    Ps = np.exp(np.linspace(np.log(P2), np.log(pfloor * P2), nstep))
    H = np.zeros(nstep); Rho = np.zeros(nstep); T = np.zeros(nstep)
    for i, P in enumerate(Ps):                                   # march down the isentrope
        _sp_state(gas, s2, P)
        H[i], Rho[i], T[i] = gas.enthalpy_mass, gas.density, gas.T
    # local equilibrium sound speed from the isentrope table itself: a^2 = dP/drho|s
    a2tab = np.gradient(Ps, Rho)                                 # (dP/drho) along s = s2
    atab = np.sqrt(np.maximum(a2tab, 1.0))
    # --- limiting (stagnation) pressure P_m : h(P_m,s2) = h1
    im = np.where(H < h1)[0][0]
    Pm = float(np.interp(h1, [H[im], H[im - 1]], [Ps[im], Ps[im - 1]]))
    # --- sonic point: w = a_eq
    w = np.sqrt(np.maximum(2.0 * (h1 - H), 0.0))
    fs = w - atab
    js = np.where((Ps < 0.98 * Pm) & (fs > 0))[0][0]             # first supersonic node
    Plo, Phi = Ps[js], Ps[js - 1]
    for _ in range(40):                                          # bisection, exact evals
        Pmid = np.sqrt(Plo * Phi)
        _sp_state(gas, s2, Pmid)
        wm = np.sqrt(max(2.0 * (h1 - gas.enthalpy_mass), 0.0))
        am = aeq(gas)
        if wm - am > 0: Plo = Pmid
        else: Phi = Pmid
        if abs(Phi / Plo - 1) < 1e-6: break
    Pst = np.sqrt(Plo * Phi)
    _sp_state(gas, s2, Pst)
    wst = float(np.sqrt(2.0 * (h1 - gas.enthalpy_mass)))
    Tst, rst, ast = float(gas.T), float(gas.density), float(aeq(gas))
    F_sonic = wst + (Pst - PA) / (rst * wst)
    # --- pressure-matched exit P = Pa
    _sp_state(gas, s2, PA)
    w_pa = float(np.sqrt(max(2.0 * (h1 - gas.enthalpy_mass), 0.0)))
    # --- flatness of T/Mdot over supersonic branch (SK Fig. 8b argument)
    sel = (Ps <= Pst) & (Ps > min(PA * 0.8, 0.02 * P2)) & (w > 1)   # supersonic branch
    FvM = w[sel] + (Ps[sel] - PA) / (Rho[sel] * w[sel])
    flat = float((FvM.max() - FvM.min()) / FvM.mean() * 100)
    ax = dict(Pm=Pm, Pm_over_P2=Pm / P2, Pm_over_P1=Pm / cj['cond']['P1'],
              Pstar=float(Pst), Pstar_over_P1=float(Pst / cj['cond']['P1']),
              Tstar=Tst, rhostar=rst, wstar=wst, astar=ast, Mstar=wst / ast,
              FovM_sonic=float(F_sonic), Ispf_sonic=float(F_sonic / (cj['Yf'] * G0)),
              Isp_tot_sonic=float(F_sonic / G0),
              w_matched=w_pa, FovM_matched=w_pa, Ispf_matched=float(w_pa / (cj['Yf'] * G0)),
              flatness_pct=flat, Pa=PA)
    d = load(); d['cases'][key]['axial'] = ax; save(d)
    print('%s AX: Pm/P2=%.3f P*=%.2fatm w*=%.0f F/M=%.1f Ispf=%.0f (matched %.0f) flat=%.1f%%'
          % (key, Pm / P2, Pst / ATM, wst, F_sonic, ax['Ispf_sonic'], ax['Ispf_matched'], flat), flush=True)

# ---------------------------------------------------------------- stage: Stechmann mass-weighted
def stech_calc(ge, Rgas, PR, Pin, Tcj, Pa=PA, n=20001):
    """Mass-weighted cycle Isp per Stechmann Eq. 4; returns dict of [s] values (total-mass)."""
    xi = np.linspace(0.0, 1.0, n)                # xi = t/tc  (tc cancels, Eq. 4-5)
    PCJ = PR * Pin
    Pc = PCJ * np.exp(-np.log(PR) * xi)          # Eq. 13-14: Pc(tc) = Pin
    Tc = Tcj * (Pc / PCJ) ** ((ge - 1) / ge)     # Eq. 15
    cst = np.sqrt(ge * Rgas * Tc) / (ge * np.sqrt((2 / (ge + 1)) ** ((ge + 1) / (ge - 1))))
    md = Pc / cst                                # choked: mdot ~ Pc/cstar (Eq. 6)
    NPR = ((ge + 1) / 2) ** (ge / (ge - 1))      # eps = 1 (exit = throat)
    base = 2 * ge**2 / (ge - 1) * (2 / (ge + 1)) ** ((ge + 1) / (ge - 1))
    Cf1 = np.sqrt(base * (1 - (1 / NPR) ** ((ge - 1) / ge))) + (1 / NPR - Pa / Pc)   # Eq. 9
    Cfs = np.sqrt(base * np.clip(1 - np.minimum(Pa / Pc, 1.0) ** ((ge - 1) / ge), 0, None))  # Eq. 10
    Cfv = np.sqrt(base * (1 - (1 / NPR) ** ((ge - 1) / ge))) + 1 / NPR               # vacuum
    mw = lambda Cf: float(np.trapz(md * Cf * cst, xi) / np.trapz(md, xi) / G0)
    ta = lambda Cf: float(np.trapz(Cf * cst, xi) / G0)
    return dict(NPR=NPR,
                Isp_sl_e1=mw(Cf1), Isp_sl_spike=mw(Cfs), Isp_vac_e1=mw(Cfv),
                Isp_ta_sl_e1=ta(Cf1), Isp_ta_spike=ta(Cfs),
                frac_choked=float(np.mean(Pc / Pa >= NPR)),
                cstar_mw=float(np.trapz(md * cst, xi) / np.trapz(md, xi)))

def stage_stech(key):
    d = load(); cj = d['cases'][key]['cj']
    ge = cj['gamma_e']; Rgas = ct.gas_constant / cj['M2w']
    st = stech_calc(ge, Rgas, cj['p2p1'], cj['cond']['P1'], cj['T2'])
    st.update(gamma=ge, R=Rgas, PR=cj['p2p1'], Tcj=cj['T2'],
              Ispf_sl_e1=st['Isp_sl_e1'] / cj['Yf'],
              Ispf_sl_spike=st['Isp_sl_spike'] / cj['Yf'],
              Ispf_vac_e1=st['Isp_vac_e1'] / cj['Yf'],
              mw_over_ta_e1=st['Isp_sl_e1'] / st['Isp_ta_sl_e1'])
    d['cases'][key]['stech'] = st; save(d)
    print('%s ST: Isp(sl,e1)=%.1f Isp(sl,spike)=%.1f Isp(vac,e1)=%.1f s [total]; Ispf(spike)=%.0f s; choked %.0f%%'
          % (key, st['Isp_sl_e1'], st['Isp_sl_spike'], st['Isp_vac_e1'],
             st['Ispf_sl_spike'], 100 * st['frac_choked']), flush=True)

# ---------------------------------------------------------------- driver
STAGES = dict(cj=stage_cj, ph=stage_ph, axial=stage_axial, stech=stage_stech)

def run(stage, key):
    if stage == 'all':
        stage_cj(key); stage_ph(key); stage_axial(key)
        if CASES[key]['ox'].lower() in ('o2',) and not key.startswith('SKREP'):
            stage_stech(key)
    else:
        STAGES[stage](key)

if __name__ == '__main__':
    stage = sys.argv[1]
    for k in sys.argv[2:]:
        run(stage, k)
    print('OK', flush=True)
