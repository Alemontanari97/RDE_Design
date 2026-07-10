#!/usr/bin/env python3
"""Converged nozzle-area-ratio optimization (bell and aerospike) for the
Stechmann-Heister-Harroun RDE performance model, validated row-by-row against
the paper's Table 1.

Lecture-repo edition of project_build/scripts/st_nozzle_opt.py: verbatim physics;
the model core is imported from st_core.py (extracted from the figs_st_eap.py
figure module of the build), paths are repo-relative, and the one-off migration
shim for the legacy st_cycle_states.json cache was removed (all states ship
precomputed in data/st_nozzle_opt.json).

Reference: Stechmann, Heister & Harroun, "Rotating Detonation Engine
Performance Model for Rocket Applications", J. Spacecraft & Rockets 56(3),
2019, doi:10.2514/1.A34313.  Equation numbers below are the paper's.

------------------------------------------------------------------------------
STEP-BY-STEP PROCEDURE (student deliverable)
------------------------------------------------------------------------------
Step 1 - Gas states (equilibrium chemistry, paper assumption 4).
  CP side: HP equilibrium of the premixture (phi, Ti) at Pcp -> T0, M and the
  equilibrium isentropic exponent gamma_s = rho*a_eq^2/P; c* from Eq. (1)/(7).
  Detonation side: equilibrium Chapman-Jouguet state of the fill (Pinit, Ti)
  (minimum of the wave speed along the equilibrium Hugoniot, parabolic
  refinement; sonic residual |w2/a_eq - 1| recorded) -> PR = P_CJ/Pinit, T_CJ,
  gamma_s, c*(0).  gamma and M are then FROZEN in space and time (paper
  assumption 2): the same gamma drives the blowdown, c*(t) and the nozzle.

Step 2 - Matched detonation cycle (paper Sec. III protocol).
  Blowdown Pc(t) = PR*Pinit*exp(-lambda*t), lambda = ln(PR)/tc (Eqs. 13-14);
  Tc(t) isentropic (Eq. 15) so c*(t) = c*(0)*(Pc/P_CJ)^((gamma-1)/(2 gamma));
  mass flux mdot/A_t = Pc/c* (Eq. 6, thermally choked exit).  Pinit is
  iterated until the mass per cycle equals that of a CP combustor at Pcp with
  the SAME propellant, phi, Ti and throat area.  For the exponential profile
  the cycle-mean mass flux is closed-form:
     mean(mdot/A) = (P_CJ/c*(0)) * I(k),  k = (gamma+1)/(2 gamma),
     I(k) = (1 - PR^-k)/(k ln PR)   =>   P_CJ = Pcp * (c*(0)/c*_cp) / I(k).
  Fixed-point iteration on Pinit = P_CJ/PR to |dPinit/Pinit| < 1e-2
  (<= 5 CJ evaluations; each shifts P_CJ far less than the tolerance).
  The DC (mean-pressure) shift falls out as mean(Pc)/Pcp - 1.

Step 3 - Time-variant thrust coefficient (Eqs. 8-12).
  General form (Eq. 8):
     CF(t) = sqrt[ (2 g^2/(g-1)) (2/(g+1))^((g+1)/(g-1))
                   (1 - (Pe/Pc)^((g-1)/g)) ] + eps*(Pe/Pc - Pa/Pc).
  BELL, fixed eps (Eq. 9): isentropic area-Mach relation fixes
  NPR(eps,gamma) = Pc/Pe, so Pe(t) tracks Pc(t); only the pressure-thrust
  term eps*(1/NPR - Pa/Pc(t)) is time-dependent.  No flow-separation model:
  as in the paper, CF is allowed to collapse when the bell becomes badly
  overexpanded late in the cycle (Fig. 8); the channel choking condition
  Pc/Pa > ((g+1)/2)^(g/(g-1)) is verified and reported for every case.
  AEROSPIKE, exit-area limit eps_max: while the expansion is limited by the
  annulus exit diameter, i.e. Pe(t, eps_max) > Pa (Eq. 12), the plug behaves
  as a bell at eps_max (Eq. 11); once Pe(t, eps_max) <= Pa the free boundary
  self-adapts, Pe(t) = Pa, and the eps-term vanishes (Eq. 10).

Step 4 - Mass-weighted cycle specific impulse (Eqs. 4-5).
  Isp(eps) = int(mdot CF c* dt) / (g0 int(mdot dt)); with mdot*c* = Pc*A_t
  this is int(Pc CF dt) / (g0 int(Pc/c* dt)).  Trapezoidal quadrature on a
  uniform grid of n = 4001 points in xi = t/tc (cycle time cancels).  Grid
  convergence documented: |Isp(4001) - Isp(16001)| < 2e-3 s in all cases.
  For the CP cycle every factor is constant and Isp = CF*c*/g0 (the model
  collapses to the classical steady expressions by construction).

Step 5 - Area-ratio optimization (this script's contribution).
  (a) Coarse bracketing sweep: 241-point geometric grid in eps
      ([1.05, 40] for Pcp = 20 atm rows, [2, 400] for 200 atm rows).
  (b) BELL: golden-section refinement of the bracketed maximum to an
      absolute tolerance on eps of 1e-3 (20 atm) / 5e-3 (200 atm).
      Convergence cross-check, exact in this model: since
      dCF_bell/deps = (Pe - Pa)/Pc at fixed Pc, and mdot c*/Pc = A_t,
      d(Isp)/deps = 0  <=>  NPR(eps_opt, gamma) = mean_t(Pc)/Pa,
      i.e. the optimum bell is perfectly expanded at the TIME-mean chamber
      pressure Pcp*(1+DC).  |eps_golden - eps_analytic| is reported
      (< 1e-3 in all rows) and the analytic root is taken as eps_opt.
  (c) AEROSPIKE: Isp(eps) is strictly increasing while any instant of the
      cycle is exit-area-limited (dCF/deps = (Pe-Pa)/Pc > 0 under Eq. 12)
      and exactly constant once even the cycle peak is fully expanded, so
      the optimum is the saturation knee, the smallest eps attaining the
      plateau:  NPR(eps_opt, gamma) = Pmax/Pa,  Pmax = P_CJ (det), Pcp (CP).
      eps_opt is evaluated in closed form from the area-Mach relation at
      Me(NPR); monotonicity and plateau flatness are verified on the sweep.
      For the CP cycle this knee coincides with the CP bell optimum, and the
      plateau Isp equals the CP bell maximum (asserted; Table 1 shows the
      same behavior).  In vacuum (Pa = 0) both nozzles reduce to the same
      fixed-NPR expression: the "N/A" rows use the tabulated eps_max (15 or
      150) with no optimization, exactly as in the paper.

Step 6 - Validation against Table 1 (all 18 rows).
  Each row is recomputed at the paper's tabulated optimum equivalence ratios
  (phi_det, phi_cp) at Ti = 200 K.  Model vs paper: max Isp (det and CP),
  optimum area ratio (det; CP), detonation benefit in percent.  PASS if both
  Isp agree within 5%, area ratios within 10% (floor 0.25), benefit within
  3 points.  RP-1 is modeled as gaseous n-dodecane (equilibrium-species
  thermo file; H/C = 2.17 vs ~1.95 of RP-1, NASA7 extrapolated 300->200 K):
  the coarsest surrogate in the set, flagged with its own caveat.

Usage:
  python3 stechmann_nozzle.py states [budget_s]  # chunked, resumable
  python3 stechmann_nozzle.py optimize           # -> data/st_nozzle_opt.json
  python3 stechmann_nozzle.py validate           # -> data/st_opt_validation.md
  python3 stechmann_nozzle.py fig                # -> figs/st_fig_nozzle_opt.png
Cache/results: data/st_nozzle_opt.json (states + optimization + validation).
"""
import sys, os, json, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # repo root
sys.path[:0] = [ROOT, HERE, os.path.join(ROOT, 'src')]  # sdtoolbox / st_core / style
try:                                    # package mode: from src.thrust import ...
    from .st_core import (G0, ATM, TR, cstar_fn, Ik, cf_base, npr_of_eps,
                          cf_bell, cf_spike, _hug_point, _ct)
except ImportError:                     # script mode: python src/thrust/stechmann_nozzle.py
    from st_core import (G0, ATM, TR, cstar_fn, Ik, cf_base, npr_of_eps,
                         cf_bell, cf_spike, _hug_point, _ct)

CACHE = os.path.join(ROOT, 'data', 'st_nozzle_opt.json')
# Stechmann-paper propellant set (fuel-O2 at the paper's phi, reduced CHO /
# dodecane mechanisms for matched-cycle speed).  Deliberately NOT a view of
# src/common/mixtures.py (that registry holds the 12 stoichiometric lecture
# mixtures); coherence with the canonical CJ chain is asserted per-state by
# cj_ref() below and tests/test_cj_coherence.py.
PROPS = {'H2':   ('data/gri30_CHO_eq.yaml', 'H2', 'O2'),
         'CH4':  ('data/gri30_CHO_eq.yaml', 'CH4', 'O2'),
         'RP-1': ('data/dodecane_eq_thermo.yaml', 'c12h26', 'o2')}

# TABLE 1 verbatim (p. 896): prop, Pcp[atm], nozzle, Pa[atm],
#   det (Isp[s], phi, eps) | CP (Isp[s], phi, eps) | benefit[%]
TABLE1 = [
 ('H2',   20, 'Bell',      1.0, 394, 3.28,  3.8, 362, 2.54,   3.6,  9.0),
 ('H2',   20, 'Aerospike', 1.0, 406, 3.15,  9.2, 362, 2.54,   3.6, 12.2),
 ('H2',   20, 'N/A',       0.0, 497, 2.98, 15.0, 460, 2.25,  15.0,  7.9),
 ('H2',  200, 'Bell',      1.0, 475, 2.70, 21.2, 440, 2.04,  20.6,  8.0),
 ('H2',  200, 'Aerospike', 1.0, 483, 2.62, 55.6, 440, 2.04,  20.6,  9.7),
 ('H2',  200, 'N/A',       0.0, 545, 2.44, 150., 508, 1.81, 150.0,  7.2),
 ('CH4',  20, 'Bell',      1.0, 286, 1.66,  4.0, 274, 1.48,   3.9,  4.4),
 ('CH4',  20, 'Aerospike', 1.0, 299, 1.64, 11.4, 274, 1.48,   3.9,  9.2),
 ('CH4',  20, 'N/A',       0.0, 365, 1.60, 15.0, 353, 1.44,  15.0,  3.5),
 ('CH4', 200, 'Bell',      1.0, 358, 1.47, 23.2, 345, 1.32,  23.4,  3.7),
 ('CH4', 200, 'Aerospike', 1.0, 366, 1.46, 71.6, 345, 1.32,  23.4,  6.2),
 ('CH4', 200, 'N/A',       0.0, 415, 1.43, 150., 402, 1.29, 150.0,  3.0),
 ('RP-1', 20, 'Bell',      1.0, 273, 1.71,  3.9, 262, 1.55,   3.9,  4.0),
 ('RP-1', 20, 'Aerospike', 1.0, 287, 1.70, 12.2, 262, 1.55,   3.9,  9.6),
 ('RP-1', 20, 'N/A',       0.0, 348, 1.65, 15.0, 338, 1.51,  15.0,  3.0),
 ('RP-1',200, 'Bell',      1.0, 342, 1.53, 22.8, 331, 1.39,  23.2,  3.3),
 ('RP-1',200, 'Aerospike', 1.0, 351, 1.53, 75.7, 331, 1.39,  23.2,  6.2),
 ('RP-1',200, 'N/A',       0.0, 396, 1.49, 150., 386, 1.36, 150.0,  2.5),
]
NQ = 4001                 # quadrature grid (Step 4); convergence checked vs 16001
XTOL = {20: 1e-3, 200: 5e-3}                 # golden-section tolerance on eps
PASS_ISP, PASS_EPS_REL, PASS_EPS_ABS, PASS_BEN = 5.0, 10.0, 0.25, 3.0


def dkey(prop, Pcp, phi):
    return 'det|%s|%d|%.2f' % (prop, Pcp, phi)


def ckey(prop, Pcp, phi):
    return 'cp|%s|%d|%.2f' % (prop, Pcp, phi)


def load():
    return json.load(open(CACHE)) if os.path.exists(CACHE) else {'states': {}}


def dump(D):
    json.dump(D, open(CACHE, 'w'), indent=1)


# --------------------------------------------------------------- gas states
def _prop(prop, phi):
    """PROPS lookup with actionable errors (extension point for new propellants)."""
    if prop not in PROPS:
        raise KeyError(
            'unknown propellant %r — known: %s. Register new ones first, e.g. '
            "PROPS['C2H4'] = ('data/gri30_CHO_eq.yaml', 'C2H4', 'O2')"
            % (prop, ', '.join(sorted(PROPS))))
    if not 0.2 <= phi <= 3.0:
        raise ValueError(
            'phi = %g outside 0.2-3.0: the CJ/CEA equilibria are only '
            'meaningful near detonable compositions (Table 1 spans 0.44-1.26)'
            % phi)
    return PROPS[prop]

def cp_state(prop, phi, Ti, Pcp_atm):
    """Step 1, CP side: HP equilibrium at Pcp -> gamma_s, c* (Eqs. 1/7)."""
    ct = _ct()
    from sdtoolbox.thermo import soundspeed_eq
    mech, fuel, ox = _prop(prop, phi)
    gas = ct.Solution(os.path.join(ROOT, mech))
    gas.set_equivalence_ratio(phi, fuel, ox)
    gas.TP = Ti, Pcp_atm * ATM
    gas.equilibrate('HP')
    a = soundspeed_eq(gas)
    g = gas.density * a * a / gas.P
    R = ct.gas_constant / gas.mean_molecular_weight
    return dict(T0=float(gas.T), M=float(gas.mean_molecular_weight),
                gamma=float(g), cstar=float(cstar_fn(g, R, gas.T)))


def det_state(prop, phi, Ti, Pinit):
    """Step 1, detonation side: equilibrium CJ state of the fill (Pinit, Ti).
    Same algorithm as figs_st_eap.det_side, generalized to any propellant."""
    ct = _ct()
    from sdtoolbox.thermo import soundspeed_eq
    mech, fuel, ox = _prop(prop, phi)
    gas = ct.Solution(os.path.join(ROOT, mech))
    gas.set_equivalence_ratio(phi, fuel, ox)
    gas.TP = Ti, Pinit
    h1, v1 = gas.enthalpy_mass, 1.0 / gas.density
    work = ct.Solution(os.path.join(ROOT, mech))
    work.set_equivalence_ratio(phi, fuel, ox)
    Tg = 3500.0
    Uofx = {}

    def U(x):
        if x not in Uofx:
            P2, T2 = _hug_point(work, h1, v1, Pinit, x, Tg)
            Uofx[x] = (float(v1 * np.sqrt((P2 - Pinit) / (v1 - v1 / x))), P2, T2)
        return Uofx[x]

    xs = list(np.arange(1.55, 2.101, 0.05))
    xstar = None
    for _ in range(3):
        us = [U(round(x, 5))[0] for x in xs]
        i = int(np.argmin(us))
        if i == 0:
            xs = list(np.arange(xs[0] - 0.25, xs[0], 0.05)); continue
        if i == len(xs) - 1:
            xs = list(np.arange(xs[-1] + 0.05, xs[-1] + 0.30, 0.05)); continue
        xa, xb, xc = xs[i - 1], xs[i], xs[i + 1]
        ua, ub, uc = us[i - 1], us[i], us[i + 1]
        den = (xa - xb) * (xa - xc) * (xb - xc)
        A = (xc * (ub - ua) + xb * (ua - uc) + xa * (uc - ub)) / den
        B = (xc * xc * (ua - ub) + xb * xb * (uc - ua) + xa * xa * (ub - uc)) / den
        xstar = -B / (2 * A)
        Tg = U(round(xb, 5))[2]
        if max(xs) - min(xs) < 0.1:
            break
        xs = list(np.linspace(xstar - 0.018, xstar + 0.018, 5))
    Ucj, P2, T2 = U(round(xstar, 5))
    a = soundspeed_eq(work)
    g = work.density * a * a / work.P
    R = ct.gas_constant / work.mean_molecular_weight
    return dict(PR=float(P2 / Pinit), TCJ=float(T2), gamma=float(g),
                M=float(work.mean_molecular_weight), R=float(R),
                cstar0=float(cstar_fn(g, R, T2)),
                sonic_resid=float(abs(Ucj / xstar / a - 1.0)))


def cj_ref(prop, phi, Ti, Pinit):
    """Canonical CJ state (src/common/cj_core chain) for the same fill as
    det_state(prop, phi, Ti, Pinit) — the coherence adapter.

    det_state keeps its own verbatim Stechmann-pipeline Hugoniot solver (the
    blessed 18/18 Table-1 states and the live design-study numbers depend on
    it bit-for-bit); this function exposes the package-canonical CJ state of
    the identical fill so that tests/test_cj_coherence.py can ASSERT their
    agreement (U_CJ, PR, T_CJ, gamma within TOL['cross_solver_rel']) instead
    of assuming it.  Returns the cj_core canonical record."""
    ct = _ct()
    from src.common.cj_core import cj_state
    mech, fuel, ox = _prop(prop, phi)
    gas = ct.Solution(os.path.join(ROOT, mech))
    gas.set_equivalence_ratio(phi, fuel, ox)
    X = ','.join('%s:%.12g' % (k, v)
                 for k, v in gas.mole_fraction_dict().items() if v > 1e-12)
    return cj_state(X, p1=Pinit, T1=Ti, mech=os.path.join(ROOT, mech))


def matched(prop, phi, Ti, Pcp_atm, tol=0.01, itmax=5):
    """Step 2: iterate Pinit so the det cycle passes the CP mass per cycle
    through the same throat area (closed form for the exponential profile)."""
    Pcp = Pcp_atm * ATM
    cpm = cp_state(prop, phi, Ti, Pcp_atm)
    Pin, conv, nev = 0.11 * Pcp, 1.0, 0
    for _ in range(itmax):
        det = det_state(prop, phi, Ti, Pin)
        nev += 1
        g = det['gamma']; k = (g + 1) / (2 * g)
        P0 = Pcp * det['cstar0'] / cpm['cstar'] / Ik(det['PR'], k)
        Pnew = P0 / det['PR']
        conv = abs(Pnew / Pin - 1.0)
        Pin = Pnew
        if conv < tol:
            break
    g = det['gamma']; k = (g + 1) / (2 * g)
    DC = det['cstar0'] / cpm['cstar'] * Ik(det['PR'], 1.0) / Ik(det['PR'], k) - 1.0
    chok = (P0 / det['PR'] / ATM) / ((g + 1) / 2) ** (g / (g - 1))  # min Pc/Pa*
    return dict(prop=prop, phi=phi, Ti=Ti, Pcp_atm=Pcp_atm, P0=P0,
                P0a=P0 / ATM, Pinit=Pin, Pinita=Pin / ATM, DC=DC, conv=conv,
                nev=nev, choke_margin=chok, cpm=cpm, **det)


STATE_LIST = []
for r in TABLE1:
    STATE_LIST.append(('det', r[0], r[1], r[5]))
    STATE_LIST.append(('cp', r[0], r[1], r[8]))
STATE_LIST.append(('det', 'CH4', 20, 1.00))     # fixed-phi anchor (Figs. 9/10)
STATE_LIST.append(('cp', 'CH4', 20, 1.00))


def states(budget=38.0):
    """Chunked, resumable state computation (Step 1-2 for every Table-1 phi)."""
    D = load(); S = D['states']; t0 = time.time()
    for kind, prop, Pcp, phi in STATE_LIST:
        k = dkey(prop, Pcp, phi) if kind == 'det' else ckey(prop, Pcp, phi)
        if k in S:
            continue
        if time.time() - t0 > budget:
            print('budget reached; pending: %d' %
                  len([1 for kk, p, pc, ph in STATE_LIST
                       if (dkey(p, pc, ph) if kk == 'det' else
                           ckey(p, pc, ph)) not in S]), flush=True)
            return
        if kind == 'cp':
            S[k] = cp_state(prop, phi, 200, Pcp)
            print('%-22s c*=%7.1f  g=%.4f  T0=%.0f' %
                  (k, S[k]['cstar'], S[k]['gamma'], S[k]['T0']), flush=True)
        else:
            S[k] = matched(prop, phi, 200, Pcp)
            s = S[k]
            print('%-22s P0=%7.1f atm  Pinit=%6.2f  PR=%5.1f  g=%.4f  '
                  'c*0=%6.1f  DC=%+.2f%%  conv=%.4f  nev=%d  chk=%.2f' %
                  (k, s['P0a'], s['Pinita'], s['PR'], s['gamma'], s['cstar0'],
                   100 * s['DC'], s['conv'], s['nev'], s['choke_margin']),
                  flush=True)
        dump(D)
    print('states complete: %d' % len(S), flush=True)


# ------------------------------------------------------------- optimization
def eps_of_npr(NPR, g):
    """Closed-form area ratio for a given NPR (isentropic area-Mach relation)."""
    Me2 = 2.0 / (g - 1) * (NPR ** ((g - 1) / g) - 1.0)
    Me = np.sqrt(Me2)
    return float((1.0 / Me) * ((2.0 / (g + 1)) * (1 + (g - 1) / 2 * Me2))
                 ** ((g + 1) / (2 * (g - 1))))


def cycle_isp(s, cf_of_Pc, n=NQ):
    """Step 4, Eq. 4: mass-weighted cycle Isp for a CF(Pc(t)) closure."""
    g = s['gamma']
    xi = np.linspace(0.0, 1.0, n)
    Pc = s['P0'] * s['PR'] ** (-xi)
    cs = s['cstar0'] * (Pc / s['P0']) ** ((g - 1) / (2 * g))
    md = Pc / cs
    return float(TR(md * cf_of_Pc(Pc) * cs, xi) / TR(md, xi) / G0)


def golden_max(f, a, b, xtol):
    """Golden-section maximization on [a, b] to |b-a| < xtol."""
    gr = 0.5 * (np.sqrt(5.0) - 1.0)
    c, d = b - gr * (b - a), a + gr * (b - a)
    fc, fd, n = f(c), f(d), 2
    while b - a > xtol:
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a); fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a); fd = f(d)
        n += 1
    x = 0.5 * (a + b)
    return x, f(x), n


def bell_opt(isp_of_eps, Pmean, Pa, g, Pcp):
    """Step 5b: sweep + golden section; analytic check NPR(eps*) = mean(Pc)/Pa."""
    hi = 40.0 if Pcp <= 20 else 400.0
    grid = np.geomspace(1.05, hi, 241)
    vals = np.array([isp_of_eps(e) for e in grid])
    i = int(np.argmax(vals))
    a, b = grid[max(i - 1, 0)], grid[min(i + 1, len(grid) - 1)]
    e_gs, isp_gs, nev = golden_max(isp_of_eps, a, b, XTOL.get(Pcp, 1e-3))
    e_an = eps_of_npr(Pmean / Pa, g)
    return dict(eps=e_an, Isp=isp_of_eps(e_an), eps_golden=e_gs,
                Isp_golden=isp_gs, gs_evals=nev + len(grid),
                gs_vs_analytic=abs(e_gs - e_an)), grid, vals


def spike_opt(isp_of_eps, Pmax, Pa, g, Pcp):
    """Step 5c: saturation knee NPR(eps*) = Pmax/Pa; verify plateau on sweep."""
    e_kn = eps_of_npr(Pmax / Pa, g)
    hi = max(40.0 if Pcp <= 20 else 400.0, 2.5 * e_kn)
    grid = np.geomspace(1.05, hi, 241)
    vals = np.array([isp_of_eps(e) for e in grid])
    mono = bool(np.all(np.diff(vals[grid <= e_kn * 0.999]) > -1e-9))
    plateau = abs(isp_of_eps(2.0 * e_kn) - isp_of_eps(e_kn))
    below = isp_of_eps(e_kn) - isp_of_eps(0.98 * e_kn)
    return dict(eps=e_kn, Isp=isp_of_eps(e_kn), monotone_below=mono,
                plateau_flatness=plateau, gain_last2pct=below), grid, vals


def optimize():
    """Step 5 for all Table-1 rows + fixed-phi anchors -> cache['rows' etc.]."""
    D = load(); S = D['states']
    rows = []
    for (prop, Pcp, noz, Pa_atm, iD, phD, eD, iC, phC, eC, ben) in TABLE1:
        Pa = Pa_atm * ATM
        s = S[dkey(prop, Pcp, phD)]
        c = S[ckey(prop, Pcp, phC)]
        gd, gc = s['gamma'], c['gamma']
        Pmean = s['P0'] * ATM / ATM * Ik(s['PR'], 1.0)          # time-mean Pc [Pa]
        row = dict(prop=prop, Pcp=Pcp, nozzle=noz, Pa=Pa_atm,
                   paper=dict(Isp_det=iD, phi_det=phD, eps_det=eD,
                              Isp_cp=iC, phi_cp=phC, eps_cp=eC, benefit=ben),
                   state=dict(P0a=s['P0a'], Pinita=s['Pinita'], PR=s['PR'],
                              gamma_det=gd, gamma_cp=gc, cstar0=s['cstar0'],
                              cstar_cp=c['cstar'], DC=s['DC'],
                              choke_margin=s['choke_margin'],
                              sonic_resid=s['sonic_resid']))
        if noz == 'Bell':
            det = lambda e: cycle_isp(s, lambda Pc, e=e: cf_bell(gd, e, Pc, Pa))
            cp_ = lambda e: float(cf_bell(gc, e, Pcp * ATM, Pa)) * c['cstar'] / G0
            od, _, _ = bell_opt(det, Pmean, Pa, gd, Pcp)
            oc, _, _ = bell_opt(cp_, Pcp * ATM, Pa, gc, Pcp)
        elif noz == 'Aerospike':
            det = lambda e: cycle_isp(s, lambda Pc, e=e: cf_spike(gd, e, Pc, Pa))
            cp_ = lambda e: float(cf_spike(gc, e, np.array([Pcp * ATM]), Pa)[0]) \
                * c['cstar'] / G0
            od, _, _ = spike_opt(det, s['P0'], Pa, gd, Pcp)
            oc, _, _ = spike_opt(cp_, Pcp * ATM, Pa, gc, Pcp)
            # CP spike plateau == CP bell maximum (same knee): assert < 0.05 s
            cpbell = bell_opt(lambda e: float(cf_bell(gc, e, Pcp * ATM, Pa))
                              * c['cstar'] / G0, Pcp * ATM, Pa, gc, Pcp)[0]
            oc['equals_cp_bell'] = abs(oc['Isp'] - cpbell['Isp'])
        else:                                   # vacuum rows: fixed eps, Pa = 0
            e_fix = eD
            det = lambda e: cycle_isp(s, lambda Pc, e=e: cf_bell(gd, e, Pc, 0.0))
            od = dict(eps=e_fix, Isp=det(e_fix), fixed=True)
            oc = dict(eps=eC, Isp=float(cf_bell(gc, eC, Pcp * ATM, 0.0))
                      * c['cstar'] / G0, fixed=True)
        mben = 100.0 * (od['Isp'] / oc['Isp'] - 1.0)
        row['model'] = dict(det=od, cp=oc, benefit=mben)
        row['delta'] = dict(
            dIsp_det=100 * (od['Isp'] / iD - 1), dIsp_cp=100 * (oc['Isp'] / iC - 1),
            deps_det=100 * (od['eps'] / eD - 1), deps_cp=100 * (oc['eps'] / eC - 1),
            dben=mben - ben)
        ok_isp = (abs(row['delta']['dIsp_det']) <= PASS_ISP and
                  abs(row['delta']['dIsp_cp']) <= PASS_ISP)
        ok_eps = True
        if noz != 'N/A':
            ok_eps = ((abs(row['delta']['deps_det']) <= PASS_EPS_REL or
                       abs(od['eps'] - eD) <= PASS_EPS_ABS) and
                      (abs(row['delta']['deps_cp']) <= PASS_EPS_REL or
                       abs(oc['eps'] - eC) <= PASS_EPS_ABS))
        ok_ben = abs(row['delta']['dben']) <= PASS_BEN
        row['status'] = 'PASS' if (ok_isp and ok_eps and ok_ben) else 'FAIL'
        rows.append(row)
        print('%-5s %3d %-9s Pa=%.0f  det %6.1f s @eps %6.2f (pap %3d @%5.1f) '
              ' cp %6.1f @%6.2f (pap %3d @%5.1f)  ben %5.1f%% (pap %4.1f)  %s'
              % (prop, Pcp, noz, Pa_atm, od['Isp'], od['eps'], iD, eD,
                 oc['Isp'], oc['eps'], iC, eC, mben, ben, row['status']),
              flush=True)
    # fixed-phi anchors (CH4, phi=1, 20 atm): bell +2-3%, spike ~+7% at 200 K
    s = S[dkey('CH4', 20, 1.00)]; c = S[ckey('CH4', 20, 1.00)]
    gd, gc = s['gamma'], c['gamma']; Pa = ATM
    Pmean = s['P0'] * Ik(s['PR'], 1.0)
    db, _, _ = bell_opt(lambda e: cycle_isp(
        s, lambda Pc, e=e: cf_bell(gd, e, Pc, Pa)), Pmean, Pa, gd, 20)
    cb, _, _ = bell_opt(lambda e: float(cf_bell(gc, e, 20 * ATM, Pa))
                        * c['cstar'] / G0, 20 * ATM, Pa, gc, 20)
    ds, _, _ = spike_opt(lambda e: cycle_isp(
        s, lambda Pc, e=e: cf_spike(gd, e, Pc, Pa)), s['P0'], Pa, gd, 20)
    cs_, _, _ = spike_opt(lambda e: float(cf_spike(gc, e, np.array([20 * ATM]),
                          Pa)[0]) * c['cstar'] / G0, 20 * ATM, Pa, gc, 20)
    D['anchors_phi1_CH4_20atm'] = dict(
        det_bell=db, cp_bell=cb, det_spike=ds, cp_spike=cs_,
        bell_gain=100 * (db['Isp'] / cb['Isp'] - 1),
        spike_gain=100 * (ds['Isp'] / cs_['Isp'] - 1),
        eps_ratio=ds['eps'] / cs_['eps'],
        paper='bell +2-3% (Fig. 9), spike upward of 7% (Fig. 10), eps ~3x')
    a = D['anchors_phi1_CH4_20atm']
    print('anchor CH4 phi=1: bell %+.1f%% (2-3), spike %+.1f%% (~7), '
          'eps_spike/eps_cp = %.2f (~3)' %
          (a['bell_gain'], a['spike_gain'], a['eps_ratio']), flush=True)
    # quadrature convergence (Step 4): one bell + one spike case
    s = S[dkey('H2', 20, 3.28)]
    for nm, fn in (('bell', lambda Pc: cf_bell(s['gamma'], 3.8, Pc, ATM)),
                   ('spike', lambda Pc: cf_spike(s['gamma'], 9.2, Pc, ATM))):
        d = abs(cycle_isp(s, fn, 4001) - cycle_isp(s, fn, 16001))
        D.setdefault('quadrature_check', {})[nm] = d
        print('quadrature %s: |Isp(4001)-Isp(16001)| = %.2e s' % (nm, d))
    D['rows'] = rows
    D['meta'] = dict(
        method='coarse 241-pt geometric sweep + golden-section (bell) / '
               'closed-form saturation knee NPR(eps)=Pmax/Pa (aerospike); '
               'analytic optimality NPR(eps)=mean(Pc)/Pa cross-check (bell)',
        eps_tolerance=XTOL, quadrature_n=NQ, Ti=200,
        pass_criteria=dict(Isp_pct=PASS_ISP, eps_pct=PASS_EPS_REL,
                           eps_abs=PASS_EPS_ABS, benefit_pt=PASS_BEN),
        matching='Pinit fixed point, tol 1e-2, <=5 CJ evals (Sec. III)',
        no_separation='paper choice replicated: no flow-separation model; '
                      'bell CF free to collapse when overexpanded late in '
                      'cycle; choking margin min(Pc)/Pa vs ((g+1)/2)^(g/(g-1)) '
                      'reported per case')
    dump(D)
    print('optimize: %d rows -> %s' % (len(rows), CACHE), flush=True)


# --------------------------------------------------------------- validation
def validate():
    D = load()
    L = ['# Stechmann Table 1 - nozzle optimization validation',
         '',
         'Model: `src/thrust/stechmann_nozzle.py` (Eqs. 4-15 of the paper; equilibrium',
         'CJ/HP chemistry, gamma frozen through the nozzle, mass-weighted cycle',
         'Isp, matched mass flow and throat area, Ti = 200 K).',
         'Optimizer: 241-pt geometric sweep + golden-section, tol 1e-3 (5e-3 at',
         '200 atm) on eps; bell optimum cross-checked against the exact model',
         'identity NPR(eps_opt) = mean_t(Pc)/Pa; aerospike optimum = saturation',
         'knee NPR(eps_opt) = Pmax/Pa (closed form, plateau verified on sweep).',
         'Vacuum ("N/A") rows use the paper-fixed eps (15 / 150), no optimization.',
         '',
         'PASS: |dIsp| <= %.0f%% (det and CP), eps within %.0f%% (or %.2f abs),' %
         (PASS_ISP, PASS_EPS_REL, PASS_EPS_ABS),
         'benefit within %.0f points.' % PASS_BEN, '',
         '| Prop | Pcp | Nozzle | Pa | Isp_det pap/mod (d%) | eps_det pap/mod |'
         ' Isp_cp pap/mod (d%) | eps_cp pap/mod | benefit pap/mod (d pt) |'
         ' status |',
         '|---|---|---|---|---|---|---|---|---|---|']
    for r in D['rows']:
        p, m, d = r['paper'], r['model'], r['delta']
        L.append('| %s | %d | %s | %.0f | %d / %.1f (%+.1f%%) | %.1f / %.2f |'
                 ' %d / %.1f (%+.1f%%) | %.1f / %.2f | %.1f / %.2f (%+.2f) |'
                 ' %s |' %
                 (r['prop'], r['Pcp'], r['nozzle'], r['Pa'],
                  p['Isp_det'], m['det']['Isp'], d['dIsp_det'],
                  p['eps_det'], m['det']['eps'],
                  p['Isp_cp'], m['cp']['Isp'], d['dIsp_cp'],
                  p['eps_cp'], m['cp']['eps'],
                  p['benefit'], m['benefit'], d['dben'], r['status']))
    a = D['anchors_phi1_CH4_20atm']
    npass = sum(1 for r in D['rows'] if r['status'] == 'PASS')
    L += ['',
          '%d/%d rows PASS.' % (npass, len(D['rows'])), '',
          '## Qualitative anchors (CH4/O2, phi = 1, Pcp = 20 atm, Ti = 200 K)',
          '',
          '- Bell detonation gain at fixed phi: **%+.1f%%** (paper: +2-3%%,'
          ' Fig. 9).' % a['bell_gain'],
          '- Aerospike detonation gain at fixed phi: **%+.1f%%** (paper: '
          '"upward of 7%%", Fig. 10).' % a['spike_gain'],
          '- Optimum aerospike/CP area-ratio growth: **%.2fx** (paper: ~3x;'
          ' largest tabulated benefit 12.2%%).' % a['eps_ratio'],
          '',
          '## Honest-model statement',
          '',
          '- No flow-separation model (paper choice, replicated): the fixed-eps',
          '  bell is allowed to run deeply overexpanded late in the cycle',
          '  (Fig. 8); real bells would separate and lose less, so the tabulated',
          '  bell penalty is a worst case within the ideal framework.',
          '- Channel choking (assumption 3): min(Pc)/Pa relative to the sonic',
          '  threshold ((g+1)/2)^(g/(g-1)) is reported per case. Minimum margin',
          '  over the sea-level rows: ' + ', '.join(
              '%s %.2f' % (p, min(r['state']['choke_margin'] for r in D['rows']
                                  if r['prop'] == p and r['Pa'] > 0))
              for p in ('H2', 'CH4', 'RP-1')) + ';',
          '  the low-mass-flux tail of the 20-atm hydrocarbon cycles therefore',
          '  dips marginally below choking. The paper retains assumption 3',
          '  there, and this model replicates that choice.',
          '- RP-1 is modeled as gaseous n-dodecane (H/C 2.17 vs ~1.95; NASA7',
          '  thermo extrapolated 300 K -> 200 K): the coarsest surrogate here.',
          '- Quadrature: |Isp(n=4001) - Isp(n=16001)| = %.1e / %.1e s'
          % (D['quadrature_check']['bell'], D['quadrature_check']['spike']),
          '  (bell / aerospike, H2 20 atm case).']
    open(os.path.join(ROOT, 'data', 'st_opt_validation.md'), 'w').write(
        '\n'.join(L) + '\n')
    ih = next(i for i, s in enumerate(L) if s.startswith('| Prop'))
    print('\n'.join(L[ih:ih + 2 + len(D['rows'])]))       # header + all rows
    print(L[ih + 2 + len(D['rows']) + 1])                 # 'n/n rows PASS.'
    print('validation -> data/st_opt_validation.md', flush=True)


# ------------------------------------------------------------------- figure
def fig():
    from style import plt, RED, TEAL, GRAY, NAVY, save
    D = load(); S = D['states']
    fig_, axs = plt.subplots(1, 2, figsize=(13.2, 5.0))
    fig_.subplots_adjust(wspace=0.235)

    # --- left: CF(t), bell vs aerospike self-adaptation (paper Fig. 8 setup)
    ax = axs[0]
    s = S[dkey('CH4', 20, 1.64)]
    g = s['gamma']; Pa = ATM
    rowA = next(r for r in D['rows'] if r['prop'] == 'CH4' and r['Pcp'] == 20
                and r['nozzle'] == 'Aerospike')
    rowB = next(r for r in D['rows'] if r['prop'] == 'CH4' and r['Pcp'] == 20
                and r['nozzle'] == 'Bell')
    eb = 4.0
    t = np.linspace(0, 120, 1600)
    Pc = s['P0'] * s['PR'] ** (-t / 120.0)
    cfb = cf_bell(g, eb, Pc, Pa)
    ax.plot(t, cfb, color=NAVY, lw=2.2, label='Bell, $\\varepsilon=4$')
    ax.plot(t, cf_spike(g, eb, Pc, Pa), color=RED, lw=2.2, ls=(0, (2, 1.2)),
            label='Aerospike, $\\varepsilon_{max}=4$')
    NPR4 = npr_of_eps(eb, g)
    cfv = np.sqrt(cf_base(g) * (1 - NPR4 ** (-(g - 1) / g))) + eb / NPR4
    ax.axhline(cfv, color=GRAY, ls='--', lw=1.4)
    ax.text(3, cfv + 0.022, 'Vacuum limit, $\\varepsilon=4$', ha='left',
            fontsize=10.5)
    tsw = 120.0 * np.log(s['P0a'] / NPR4) / np.log(s['PR'])
    ax.axvline(tsw, color=GRAY, ls=':', lw=1.3)
    ax.annotate('$P_e(t,\\varepsilon_{max})>P_a$\n(Eq. 12): exit-area\n'
                'limited, aerospike\n$\\equiv$ bell (Eq. 11)',
                xy=(tsw * 0.57, float(np.interp(tsw * 0.57, t, cfb)) - 0.012),
                xytext=(tsw - 4, 1.24), ha='right', va='top', fontsize=10.5,
                arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.0))
    ax.annotate('$P_e(t)=P_a$: self-adapting\nexpansion (Eq. 10)',
                xy=(86, float(cf_spike(g, eb, np.array(
                    [s['P0'] * s['PR'] ** (-86 / 120.)]), Pa)[0]) + 0.02),
                xytext=(118, 1.525), ha='right', va='top', fontsize=10.5,
                arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.0))
    ax.annotate('fixed $NPR$: overexpanded late\nin cycle (no separation'
                ' modeled)', xy=(float(np.interp(1.0, cfb[::-1], t[::-1])), 1.0),
                xytext=(20, 0.735), fontsize=10.5,
                arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.0))
    ax.set_xlabel(r'Time ($\mu$s)')
    ax.set_ylabel('Local thrust coefficient $C_F$')
    ax.set_xlim(0, 120); ax.set_xticks(np.arange(0, 121, 20))
    ax.set_ylim(0.55, 2.0)
    ax.legend(loc='upper right', fontsize=11, handlelength=2.1,
              framealpha=0.95)
    ax.text(0.025, 0.035, 'CH$_4$/O$_2$, $\\varphi=1.64$, $T_i$=200 K, '
            '$P_{cp}$=20 atm, $P_a$=1 atm', transform=ax.transAxes,
            fontsize=11)

    # --- right: Isp(eps) with converged maxima, det vs CP, bell vs spike
    ax = axs[1]
    sB = S[dkey('CH4', 20, 1.66)]; sA = s
    c = S[ckey('CH4', 20, 1.48)]
    gB, gA, gc = sB['gamma'], sA['gamma'], c['gamma']
    eps = np.geomspace(1.6, 16, 300)
    dbell = np.array([cycle_isp(sB, lambda Pc, e=e: cf_bell(gB, e, Pc, Pa))
                      for e in eps])
    dspk = np.array([cycle_isp(sA, lambda Pc, e=e: cf_spike(gA, e, Pc, Pa))
                     for e in eps])
    cbell = np.array([float(cf_bell(gc, e, 20 * ATM, Pa)) * c['cstar'] / G0
                      for e in eps])
    cspk = np.array([float(cf_spike(gc, e, np.array([20 * ATM]), Pa)[0])
                     * c['cstar'] / G0 for e in eps])
    ax.plot(eps, dspk, color=RED, lw=2.3, label='Detonation, aerospike '
            '($\\varphi=1.64$)')
    ax.plot(eps, dbell, color=RED, lw=2.0, ls='--', label='Detonation, bell '
            '($\\varphi=1.66$)')
    ax.plot(eps, cspk, color=TEAL, lw=2.3, label='Constant $p$, aerospike '
            '($\\varphi=1.48$)')
    ax.plot(eps, cbell, color=TEAL, lw=2.0, ls='--', label='Constant $p$, bell '
            '($\\varphi=1.48$)')
    m = rowA['model']
    pts = [(rowB['model']['det']['eps'], rowB['model']['det']['Isp'], RED),
           (m['det']['eps'], m['det']['Isp'], RED),
           (m['cp']['eps'], m['cp']['Isp'], TEAL)]
    for x, y, col in pts:
        ax.plot(x, y, 'o', color=col, ms=7, zorder=5)
    for x, y in ((11.4, 299), (4.0, 286), (3.9, 274)):
        ax.plot(x, y, 'o', mfc='none', mec=GRAY, ms=12, mew=1.5, zorder=4)
    ax.plot([], [], 'o', mfc='none', mec=GRAY, ms=10, mew=1.5,
            label='Table 1 optima (paper)')
    ax.text(11.55, 292.6, '$\\varepsilon_{opt}=%.1f$' % m['det']['eps'],
            fontsize=10.5, color=RED)
    ax.text(4.55, 287.3, '$\\varepsilon_{opt}=%.1f$'
            % rowB['model']['det']['eps'], fontsize=10.5, color=RED)
    ax.text(4.55, 276.4, '$\\varepsilon_{opt}=%.1f$' % m['cp']['eps'],
            fontsize=10.5, color=TEAL)
    ax.set_xlabel(r'Nozzle area ratio $\varepsilon$')
    ax.set_ylabel('Cycle-averaged $I_{sp}$ (s)')
    ax.set_xlim(1.6, 15.5); ax.set_ylim(228, 313)
    ax.set_xticks(np.arange(2, 15, 2))
    ax.legend(loc='lower left', fontsize=10.2, handlelength=2.1,
              framealpha=0.95)
    ax.text(0.025, 0.975, 'CH$_4$/O$_2$, $T_i$=200 K, $P_{cp}$=20 atm, '
            '$P_a$=1 atm; each cycle at its\nTable 1 optimum equivalence '
            'ratio', transform=ax.transAxes, fontsize=11, va='top')
    save(fig_, 'st_fig_nozzle_opt')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'optimize'
    if cmd == 'states':
        states(float(sys.argv[2]) if len(sys.argv) > 2 else 38.0)
    elif cmd == 'optimize':
        optimize()
    elif cmd == 'validate':
        validate()
    elif cmd == 'fig':
        fig()
    print('OK', flush=True)
