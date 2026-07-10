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

def _mech_id(m):
    """Portable mechanism id for JSON records: repo-internal paths -> repo-relative."""
    if os.path.isabs(m):
        rel = os.path.relpath(m, PROJ)
        if not rel.startswith('..'):
            return rel.replace(os.sep, '/')
    return m

def resolve_mech(m):
    """Make a stored mech id loadable from any cwd (inverse of _mech_id)."""
    if not os.path.isabs(m) and ('/' in m or os.sep in m):
        cand = os.path.join(PROJ, m)
        if not os.path.exists(cand):
            raise FileNotFoundError(
                'mechanism file %r not found under the repo root (%s) — '
                'restore data/ (git checkout data/) or pass mech= explicitly'
                % (m, PROJ))
        return cand
    return m                       # bare names (gri30.yaml): Cantera search path

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
def cj_calc(key):
    """CJ speed + equilibrium CJ state for CASES[key] -> record dict (no I/O).

    U_CJ from the SD Toolbox equilibrium-Hugoniot minimization (FM2018.001);
    the record carries BOTH exponents: gamma_e = rho2*a_eq^2/P2 (equilibrium
    isentropic exponent, the S&K Eq. 19-22 / Stechmann gamma) and gamma_fr =
    cp/cv at frozen CJ composition (leading-shock gamma). See README, "Two
    conventions you must not mix"."""
    c, T1, P1, gas, q = setup(key)
    h1 = gas.enthalpy_mass; rho1 = gas.density; a1f = gas.sound_speed
    Yf = float(gas[c['fuel']].Y[0]); M1w = gas.mean_molecular_weight
    U = float(CJspeed(P1, T1, q, c['mech']))
    g2 = PostShock_eq(U, P1, T1, q, c['mech'])
    P2, T2, rho2 = g2.P, g2.T, g2.density
    a2 = float(aeq(g2)); ge = rho2 * a2**2 / P2
    w2 = U * rho1 / rho2
    return dict(cond=dict(T1=T1, P1=P1, phi=1.0, mech=_mech_id(c['mech']), q=q),
                UCJ=U, MCJ=U / a1f, p2p1=P2 / P1, P2=float(P2), T2=float(T2),
                rho1=float(rho1), rho2=float(rho2), s2=float(g2.entropy_mass),
                h1=float(h1), h2=float(g2.enthalpy_mass), a_eq2=a2, w2=float(w2),
                u2lab=float(U - w2), gamma_e=float(ge), gamma_fr=float(g2.cp / g2.cv),
                Yf=Yf, M1w=float(M1w), M2w=float(g2.mean_molecular_weight),
                cj_sonic_resid=float(abs(w2 / a2 - 1.0)))

def stage_cj(key):
    rec = cj_calc(key)
    d = load(); d['cases'].setdefault(key, {}); d['cases'][key]['cj'] = rec; save(d)
    print('%s CJ: U=%.1f p2/p1=%.2f T2=%.0f ge=%.4f sonic_resid=%.4f'
          % (key, rec['UCJ'], rec['p2p1'], rec['T2'], rec['gamma_e'],
             rec['cj_sonic_resid']), flush=True)

# ---------------------------------------------------------------- stage: SK pressure history
def ph_calc(cj, K, uc=UC, Pa=PA):
    """S&K pressure-history model from a CJ record (no I/O).

    Term I (Eqs. 6, 15-18): F_I/Mdot = K*(P_CJ - P1)/(rho1*U_CJ), K = 1/alpha
    from the exponential tail fit psi(xi) = exp(-alpha*xi) (K = 1.02 fuel-air,
    1.54 fuel-O2).  Term II (Eqs. 7-8): F_II/Mdot = u_c + (P1 - Pa)/(rho1*u_c).
    Headline approx (Eqs. 19-20): K*U_CJ/(gamma_e + 1), term I only."""
    P1 = cj['cond']['P1']; dP = cj['P2'] - P1
    FI = K * dP / (cj['rho1'] * cj['UCJ'])                 # term I, exact DeltaP_CJ
    FII = uc + (P1 - Pa) / (cj['rho1'] * uc)               # term II (Eq. 7)
    F = FI + FII
    Fap = K * cj['UCJ'] / (cj['gamma_e'] + 1.0)            # headline approx, term I only
    return dict(K=K, alpha=1.0 / K, uc=uc, Pa=Pa, FI=FI, FII=FII, FovM=F,
                Ispf=F / (cj['Yf'] * G0), Ispf_I=FI / (cj['Yf'] * G0),
                Isp_tot=F / G0,
                FovM_approx_I=Fap, Ispf_approx_I=Fap / (cj['Yf'] * G0))

def stage_ph(key):
    d = load(); cj = d['cases'][key]['cj']
    ph = ph_calc(cj, CASES[key]['K'])
    d['cases'][key]['ph'] = ph; save(d)
    print('%s PH: FI=%.1f FII=%.1f F/M=%.1f m/s Ispf=%.0f s'
          % (key, ph['FI'], ph['FII'], ph['FovM'], ph['Ispf']), flush=True)

# ---------------------------------------------------------------- stage: SK axial flow
def _sp_state(gas, s2, P, X_seed=None):
    import warnings
    if X_seed is not None:
        gas.SPX = s2, P, X_seed
    else:
        gas.SP = s2, P
    with warnings.catch_warnings():
        # Cantera tries ChemEquil first and warns if T leaves its 300-3000 K
        # comfort zone before falling back to the Gibbs solver; the fallback
        # is automatic and the converged state is what we use. Silence only
        # that specific, expected message.
        warnings.filterwarnings('ignore', message='.*ChemEquil.*')
        gas.equilibrate('SP')
    return gas

def axial_calc(cj, fuel, ox, mech=None, nstep=90, pfloor=0.012, chem='eq', Pa=PA):
    """S&K axial-flow model from a CJ record (no I/O).

    Marches down the isentrope through the CJ state (entropy s2), solving
    w = sqrt(2*(h1 - h(P, s2))) (Eq. 44) and T/Mdot = w + (P - Pa)/(rho*w)
    (Eq. 45); tabulated at the sonic point w = a (as SK Table 1) and at the
    pressure-matched exit P = Pa.

    chem='eq'     : shifting equilibrium along the isentrope (the SK model;
                    recombination exothermicity recovered -> UPPER bound);
    chem='frozen' : composition frozen at the CJ equilibrium value (no
                    recombination -> LOWER bound).  The physical expansion
                    lies between the two; a Bray sudden-freeze criterion
                    would pick the switch point but needs nozzle-timescale
                    kinetics, out of scope here (see validation/gamma_
                    phase_audit.md section 4 and README assumptions map).
    """
    if chem not in ('eq', 'frozen'):
        raise ValueError("chem must be 'eq' or 'frozen', got %r" % (chem,))
    eq = (chem == 'eq')
    mech = resolve_mech(mech if mech is not None else cj['cond']['mech'])
    gas = ct.Solution(mech); gas.set_equivalence_ratio(1.0, fuel, ox)
    gas.TP = cj['cond']['T1'], cj['cond']['P1']; X1 = gas.X.copy()
    h1 = gas.enthalpy_mass
    gas.TPX = cj['T2'], cj['P2'], X1; gas.equilibrate('TP')     # rebuild CJ equilibrium
    s2 = gas.entropy_mass
    X2 = gas.X.copy()                                           # frozen-branch composition
    P2 = cj['P2']

    def _state(P):
        if eq:
            _sp_state(gas, s2, P)                               # SP + equilibrate
        else:
            gas.SPX = s2, P, X2                                 # frozen isentrope

    def _a():
        return aeq(gas) if eq else float(gas.sound_speed)

    Ps = np.exp(np.linspace(np.log(P2), np.log(pfloor * P2), nstep))
    H = np.zeros(nstep); Rho = np.zeros(nstep); T = np.zeros(nstep)
    for i, P in enumerate(Ps):                                   # march down the isentrope
        _state(P)
        H[i], Rho[i], T[i] = gas.enthalpy_mass, gas.density, gas.T
    # local sound speed from the isentrope table itself: a^2 = dP/drho|s
    a2tab = np.gradient(Ps, Rho)                                 # (dP/drho) along s = s2
    atab = np.sqrt(np.maximum(a2tab, 1.0))
    # --- limiting (stagnation) pressure P_m : h(P_m,s2) = h1
    im = np.where(H < h1)[0][0]
    Pm = float(np.interp(h1, [H[im], H[im - 1]], [Ps[im], Ps[im - 1]]))
    # --- sonic point: w = a
    w = np.sqrt(np.maximum(2.0 * (h1 - H), 0.0))
    fs = w - atab
    js = np.where((Ps < 0.98 * Pm) & (fs > 0))[0][0]             # first supersonic node
    Plo, Phi = Ps[js], Ps[js - 1]
    for _ in range(40):                                          # bisection, exact evals
        Pmid = np.sqrt(Plo * Phi)
        _state(Pmid)
        wm = np.sqrt(max(2.0 * (h1 - gas.enthalpy_mass), 0.0))
        am = _a()
        if wm - am > 0: Plo = Pmid
        else: Phi = Pmid
        if abs(Phi / Plo - 1) < 1e-6: break
    Pst = np.sqrt(Plo * Phi)
    _state(Pst)
    wst = float(np.sqrt(2.0 * (h1 - gas.enthalpy_mass)))
    Tst, rst, ast = float(gas.T), float(gas.density), float(_a())
    F_sonic = wst + (Pst - Pa) / (rst * wst)
    # --- pressure-matched exit P = Pa
    _state(Pa)
    w_pa = float(np.sqrt(max(2.0 * (h1 - gas.enthalpy_mass), 0.0)))
    # --- flatness of T/Mdot over supersonic branch (SK Fig. 8b argument)
    sel = (Ps <= Pst) & (Ps > min(Pa * 0.8, 0.02 * P2)) & (w > 1)   # supersonic branch
    FvM = w[sel] + (Ps[sel] - Pa) / (Rho[sel] * w[sel])
    flat = float((FvM.max() - FvM.min()) / FvM.mean() * 100)
    ax = dict(Pm=Pm, Pm_over_P2=Pm / P2, Pm_over_P1=Pm / cj['cond']['P1'],
              Pstar=float(Pst), Pstar_over_P1=float(Pst / cj['cond']['P1']),
              Tstar=Tst, rhostar=rst, wstar=wst, astar=ast, Mstar=wst / ast,
              FovM_sonic=float(F_sonic), Ispf_sonic=float(F_sonic / (cj['Yf'] * G0)),
              Isp_tot_sonic=float(F_sonic / G0),
              w_matched=w_pa, FovM_matched=w_pa, Ispf_matched=float(w_pa / (cj['Yf'] * G0)),
              flatness_pct=flat, Pa=Pa)
    if not eq:
        ax['chem'] = chem        # tag only the non-default branch: keeps the
    return ax                    # shipped JSON schema byte-stable

def stage_axial(key, nstep=90, pfloor=0.012):
    d = load(); cj = d['cases'][key]['cj']; c = CASES[key]
    ax = axial_calc(cj, c['fuel'], c['ox'], mech=c['mech'], nstep=nstep, pfloor=pfloor)
    d = load(); d['cases'][key]['axial'] = ax; save(d)
    print('%s AX: Pm/P2=%.3f P*=%.2fatm w*=%.0f F/M=%.1f Ispf=%.0f (matched %.0f) flat=%.1f%%'
          % (key, ax['Pm_over_P2'], ax['Pstar'] / ATM, ax['wstar'], ax['FovM_sonic'],
             ax['Ispf_sonic'], ax['Ispf_matched'], ax['flatness_pct']), flush=True)

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
    USAGE = ('usage: python sk_models.py <stage> <case> [<case> ...]\n'
             '  stage: ' + ' | '.join(list(STAGES) + ['all']) + '\n'
             '  case : ' + ', '.join(CASES))
    if len(sys.argv) < 3 or sys.argv[1] not in list(STAGES) + ['all']:
        sys.exit(USAGE)
    stage = sys.argv[1]
    bad = [k for k in sys.argv[2:] if k not in CASES]
    if bad:
        sys.exit('unknown case(s): %s\n%s' % (', '.join(map(repr, bad)), USAGE))
    for k in sys.argv[2:]:
        run(stage, k)
    print('OK', flush=True)
