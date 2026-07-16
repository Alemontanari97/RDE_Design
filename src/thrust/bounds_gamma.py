#!/usr/bin/env python3
"""bounds_gamma.py — OP-0-gamma: purge of gamma = const from the EXECUTABLE
ceiling of the OP-0 bound ladder [F1/OP-0-gamma, session S7].

STANDING DIRECTIVE OF RECORD (user, 2026-07-16, strengthened S5): gamma =
const may appear in the program ONLY as (a) a DECLARED ORACLE/TEST instance
or (b) a demoted corollary — never as a load-bearing hypothesis of a
deliverable.  The OP-0 ladder ceiling (src/thrust/bounds.py cf_ideal) was
the last executable deliverable whose PRIMARY route was gamma = const.
This module inverts that architecture:

  PRIMARY (EOS-general executable): the per-streamtube ceiling of M0
  Prop. G-B evaluated with REAL THERMOCHEMISTRY —
      V_id = sqrt( 2 [ h0 - h(s, Pa) ] )
  with h(s, P) from Cantera along the FROZEN-COMPOSITION isentrope of the
  CJ products (frozen gamma(T) rung of the N4 ladder: composition frozen,
  caloric closure exact), and the SONIC CAP located on the SAME isentrope
  by the exact criterion  h0 - h(P*) = c(P*)^2 / 2  (c = frozen sound
  speed).  The cap criterion is EOS-general (M0 Prop. 7 sharpening: the
  dF/dA_e = Pe - Pa sign argument never invokes the caloric EOS); here it
  becomes EXECUTABLE at gamma(T).

  ORACLES (DECLARED, demoted): the closed forms of src/thrust/bounds.py
  (cf_ideal / cf_ideal_naive / npr_sonic at the blessed frozen gamma_s)
  are evaluated ALONGSIDE on the same grid; they remain the known-answer
  instruments and the cross-route delta is the MEASURED gamma-purge
  correction, reported with a derived bar.

MODEL CLOSURES INHERITED UNCHANGED (declared; only the caloric closure is
generalized): S-H matched blowdown Pc(xi) = P0 PR^-xi; isentropic blowdown
(one entropy s0 for the whole cycle, anchored at (T_CJ, P0) exactly as the
closed-form route anchors c*(0) = c*(T_CJ) and scales isentropically);
frozen products composition (equilibrium at the CJ state, then frozen —
paper assumption 2 freezes composition AND gamma; we keep the first,
generalize the second); choked feed; quiescent ambient Pa.

REGIME SEMANTICS PER ROW (mirrors bounds.py):
  supercritical phase (P*(xi) >= Pa): full expansion to Pa realizable on
    the supersonic branch; F/A_t = (rho* u*) V_id.
  subcritical phase (P*(xi) < Pa): SONIC CAP; F/A_t = (rho* u*) u* +
    (P* - Pa)  (exit = throat, eps = 1).  The NAIVE (uncapped) form is
    also computed, ONLY as the executable rejection instrument: on
    subcritical phases it must LOSE to the capped form — the g = 1.15
    counterexample of record generalized to gamma(T).
  vacuum rows (Pa = 0): real h(s, P) requires P > 0; the expansion is
    truncated at the declared mechanism-validity floor T_FLOOR = 200 K
    (NASA7 range) and reported as a certified LOWER-BOUND instrument on
    the (unattained, Theorem 3) vacuum ceiling — EXCLUDED from the
    concordance rejector, by declaration.

NUMERICS (all bars derived, no magic numbers):
  - one frozen isentrope TABLE per state (M_TAB log-spaced exact Cantera
    SP flashes); phase quantities by monotone interpolation in ln P;
    sonic state per phase by inverting the MONOTONE function
    w(P) := h(P) + c(P)^2/2  (w(P*) = h0 exactly — one interpolation,
    no per-phase root-finding);
  - interpolation/flash bar: N_SPOT phases per row re-evaluated with
    EXACT flashes (no table); the max relative deviation, times safety
    S_BAR, enters the row bar;
  - quadrature bar: Richardson on nested grids (N_REAL vs (N_REAL-1)/2+1
    points): err <= |I_n - I_n2|/3, times S_BAR;
  - known-answer oracle: a synthetic CONSTANT-cp gas (NASA7 with a2..a5
    = 0 -> gamma = 7/5 exactly) run through the SAME real route must
    reproduce the gamma = const closed forms within TOL_KA, derived from
    the Cantera flash convergence (rel ~1e-9 on the state) times a
    sensitivity factor <= 1e2, times safety 10 -> 1e-6.  The test
    corrupts the route (h0 scaled by 1 + 1e-4) and REQUIRES rejection.

Usage:
  python src/thrust/bounds_gamma.py       # 18 rows -> data/ + stdout
Outputs: data/bounds_ladder_real.json (numbers of record, consumed by
tests/test_bounds_gamma.py) and data/bounds_ladder_real.md (human table).
"""
import json
import os
import sys

import numpy as np

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from src.common.constants import G0, P_ATM as ATM
from src.thrust.st_core import TR, _ct, cstar_fn
from src.thrust.bounds import cf_ideal, cf_ideal_naive, npr_sonic
from src.thrust.stechmann_nozzle import PROPS, dkey, load

EPS_MACH = float(np.finfo(float).eps)

# --- derived numerical parameters (rationale in the module docstring) ----
M_TAB = 1200        # isentrope table points (interp bar MEASURED per row)
N_REAL = 801        # phase grid (odd -> nested Richardson at 401)
N_SPOT = 12         # exact-flash spot checks per row (bar measurement)
S_BAR = 4.0         # safety on measured/Richardson bars (same role as the
                    # g0-spike K_RICH: covers the 1/3 Richardson factor)
TOL_KA = 1.0e-6     # known-answer: 1e-9 flash rel * sensitivity 1e2 * 10
T_FLOOR = 200.0     # NASA7 validity floor of the shipped mechanisms [K]

REAL_JSON = os.path.join(_ROOT, 'data', 'bounds_ladder_real.json')
REAL_MD = os.path.join(_ROOT, 'data', 'bounds_ladder_real.md')

_PG_YAML = """
phases:
- name: pg
  thermo: ideal-gas
  elements: [Ar]
  species: [PG]
  state: {T: 300.0, P: 101325.0}
species:
- name: PG
  composition: {Ar: 1}
  thermo:
    model: NASA7
    temperature-ranges: [50.0, 1000.0, 6000.0]
    data:
    - [3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
"""


# ----------------------------------------------------------- state rebuild
def products_gas(state):
    """Rebuild the CJ-products gas of a blessed det state: equilibrate the
    fill (phi, Ti, Pinit) at the CJ point (T_CJ, P_CJ = Pinit*PR), then
    FREEZE the composition (paper asm 2, caloric part dropped)."""
    ct = _ct()
    mech, fuel, ox = PROPS[state['prop']]
    gas = ct.Solution(os.path.join(_ROOT, mech))
    gas.set_equivalence_ratio(state['phi'], fuel, ox)
    gas.TP = state['TCJ'], state['Pinit'] * state['PR']
    gas.equilibrate('TP')
    X = gas.X.copy()                       # frozen products composition
    gas.TPX = state['TCJ'], state['P0'], X  # anchor of the blowdown isentrope
    return gas


def frozen_sound_speed(gas):
    """Frozen (fixed-composition) sound speed of an ideal-gas mixture."""
    ct = _ct()
    R = ct.gas_constant / gas.mean_molecular_weight
    return float(np.sqrt(gas.cp_mass / gas.cv_mass * R * gas.T))


def isen_table(gas, P_lo, m=M_TAB):
    """Exact-flash isentrope table from the CURRENT gas state down to P_lo:
    arrays (lnP, h, c, rho, T), log-spaced.  Composition frozen."""
    s0, P_hi = gas.entropy_mass, gas.P
    lnP = np.linspace(np.log(P_hi), np.log(P_lo), m)
    h = np.empty(m); c = np.empty(m); rho = np.empty(m); T = np.empty(m)
    for i, lp in enumerate(lnP):
        gas.SP = s0, float(np.exp(lp))
        h[i] = gas.enthalpy_mass
        c[i] = frozen_sound_speed(gas)
        rho[i] = gas.density
        T[i] = gas.T
    return dict(lnP=lnP[::-1], h=h[::-1], c=c[::-1], rho=rho[::-1],
                T=T[::-1], s0=s0, P_hi=P_hi)   # ascending lnP for interp


def _interp(tab, key, lnP):
    return np.interp(lnP, tab['lnP'], tab[key])


def floor_pressure(gas, T_floor=T_FLOOR):
    """Pressure on the current isentrope where T = T_floor (vacuum rows'
    declared truncation).  Sequential descent in ln P (robust flash
    starts: each SP flash begins near the previous state) followed by
    bisection inside the final one-unit bracket."""
    s0, P0 = gas.entropy_mass, gas.P
    hi = np.log(P0)
    lo = hi
    while True:
        lo -= 1.0
        gas.SP = s0, float(np.exp(lo))
        if gas.T <= T_floor:
            break
        if lo < hi - 80.0:
            raise RuntimeError('T floor %g K not reached 80 decades below '
                               'P0 — isentrope anchor suspect' % T_floor)
    a, b = lo, lo + 1.0
    for _ in range(60):
        mid = 0.5 * (a + b)
        gas.SP = s0, float(np.exp(mid))
        if gas.T > T_floor:
            b = mid
        else:
            a = mid
    return float(np.exp(b))


# --------------------------------------------------------- the real route
def real_phase_cf(tab, Pc, Pa):
    """Capped and naive ceiling CF per phase, REAL-THERMO route, vectorized
    on the isentrope table.  Returns dict of per-phase arrays."""
    lnPc = np.log(Pc)
    h0 = _interp(tab, 'h', lnPc)                       # stagnation enthalpy
    w = tab['h'] + 0.5 * tab['c'] ** 2                 # monotone in P
    if not np.all(np.diff(w) > 0):
        raise RuntimeError('w = h + c^2/2 not monotone on the isentrope '
                           'table — sonic inversion invalid')
    lnPstar = np.interp(h0, w, tab['lnP'])             # w(P*) = h0
    Pstar = np.exp(lnPstar)
    ustar = _interp(tab, 'c', lnPstar)                 # u* = c(P*)
    rhostar = _interp(tab, 'rho', lnPstar)
    mdot = rhostar * ustar                             # mdot / A_t
    if Pa > 0.0:
        hE = float(np.interp(np.log(Pa), tab['lnP'], tab['h']))
        Vid = np.sqrt(np.maximum(2.0 * (h0 - hE), 0.0))
        sup = Pstar >= Pa
        F_capped = np.where(sup, mdot * Vid,
                            mdot * ustar + (Pstar - Pa))
        F_naive = mdot * Vid                           # rejection instrument
    else:                                              # vacuum: T-floor
        hE = tab['h'][0]                               # lowest-P table point
        Vid = np.sqrt(np.maximum(2.0 * (h0 - hE), 0.0))
        uE = Vid
        rhoE = _interp(tab, 'rho', tab['lnP'][0] * np.ones_like(h0))
        PE = np.exp(tab['lnP'][0])
        sup = np.ones_like(h0, dtype=bool)
        F_capped = mdot * uE + PE * mdot / (rhoE * uE)  # truncated expansion
        F_naive = F_capped
    return dict(cf_capped=F_capped / Pc, cf_naive=F_naive / Pc,
                mdot=mdot, Pstar=Pstar, supercritical=sup, ustar=ustar,
                cstar=Pc / mdot, h0=h0)


def real_phase_exact(gas, tab, Pc, Pa):
    """ONE phase by exact flashes (no table): the interp-bar probe."""
    s0 = tab['s0']
    gas.SP = s0, float(Pc)
    h0 = gas.enthalpy_mass
    # sonic point: bisection on exact w(P) = h + c^2/2 = h0
    lo, hi = tab['lnP'][0], float(np.log(Pc))
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        gas.SP = s0, float(np.exp(mid))
        if gas.enthalpy_mass + 0.5 * frozen_sound_speed(gas) ** 2 > h0:
            hi = mid
        else:
            lo = mid
    lnPs = 0.5 * (lo + hi)
    gas.SP = s0, float(np.exp(lnPs))
    ustar = frozen_sound_speed(gas)
    mdot = gas.density * ustar
    Pstar = float(np.exp(lnPs))
    if Pa > 0.0:
        gas.SP = s0, Pa
        Vid = float(np.sqrt(max(2.0 * (h0 - gas.enthalpy_mass), 0.0)))
        if Pstar >= Pa:
            F = mdot * Vid
        else:
            F = mdot * ustar + (Pstar - Pa)
    else:
        gas.SP = s0, float(np.exp(tab['lnP'][0]))
        uE = float(np.sqrt(max(2.0 * (h0 - gas.enthalpy_mass), 0.0)))
        F = mdot * uE + gas.P * mdot / (gas.density * uE)
    return F / float(Pc)


def cap_structure_probe(tab, Pc, Pa, n_pe=192):
    """Executable EOS-general re-verification of the SONIC CAP (M0 Prop. 7
    sharpening) at one phase: scan the admissible exits Pe in (0, P*]
    along the isentrope and check the direct capped formula is their max
    (within the grid-curvature bar).  Returns (ok, margin, bar)."""
    ph = real_phase_cf(tab, np.array([Pc]), Pa)
    lnPe = np.linspace(np.log(ph['Pstar'][0]) - 6.0,
                       np.log(ph['Pstar'][0]), n_pe)
    h0 = ph['h0'][0]
    hE = _interp(tab, 'h', lnPe)
    uE = np.sqrt(np.maximum(2.0 * (h0 - hE), 0.0))
    rhoE = _interp(tab, 'rho', lnPe)
    F = ph['mdot'][0] * uE + (np.exp(lnPe) - Pa) * ph['mdot'][0] / (rhoE * uE)
    cf_grid = F / Pc
    i = int(np.argmax(cf_grid))
    # bar = curvature at an interior max + LOCAL interpolation
    # inconsistency at the sonic endpoint (u from the h-table vs u* from
    # the c-table are two interpolants of the same state: their gap is
    # the measured local table noise) + roundoff floor
    d2 = 0.0
    if 0 < i < n_pe - 1:
        d2 = abs(cf_grid[i - 1] - 2 * cf_grid[i] + cf_grid[i + 1])
    noise = ph['mdot'][0] * abs(uE[-1] - ph['ustar'][0]) / Pc
    bar = S_BAR * (d2 + noise + 64.0 * EPS_MACH * abs(cf_grid[i]))
    margin = float(ph['cf_capped'][0] - cf_grid[i])
    return margin >= -bar, margin, float(bar)


# ------------------------------------------------------------- row driver
def real_row(s, Pa, n=N_REAL):
    """Real-thermo ceiling on one blessed state + the closed-form ORACLE
    on the same grid; returns the persistable row record with derived
    bars.  Pa in [Pa]; vacuum rows get the declared T-floor treatment."""
    gas = products_gas(s)
    P_lo = min(Pa / 8.0, s['P0'] / s['PR'] / 50.0) if Pa > 0.0 else None
    if P_lo is None:
        P_lo = floor_pressure(gas, T_FLOOR)
        gas.TPX = s['TCJ'], s['P0'], gas.X          # re-anchor after search
    tab = isen_table(gas, P_lo)

    g = s['gamma']
    xi = np.linspace(0.0, 1.0, n)
    Pc = s['P0'] * s['PR'] ** (-xi)
    ph = real_phase_cf(tab, Pc, Pa)

    def isp(cf, md):
        return float(TR(Pc * cf, xi) / (G0 * TR(md, xi)))

    # closed-form ORACLE route on the same grid (bounds.py, demoted)
    cs_cl = s['cstar0'] * (Pc / s['P0']) ** ((g - 1) / (2 * g))
    md_cl = Pc / cs_cl
    isp_cl = isp(cf_ideal(g, Pc, Pa), md_cl)
    isp_cl_naive = isp(cf_ideal_naive(g, Pc, Pa), md_cl)

    isp_real = isp(ph['cf_capped'], ph['mdot'])
    isp_real_naive = isp(ph['cf_naive'], ph['mdot'])

    # Richardson quadrature bar (nested grid)
    n2 = (n - 1) // 2 + 1
    ph2 = real_phase_cf(tab, Pc[::2], Pa)
    isp_real_2 = float(TR(Pc[::2] * ph2['cf_capped'], xi[::2])
                       / (G0 * TR(ph2['mdot'], xi[::2])))
    bar_quad = S_BAR * abs(isp_real - isp_real_2) / 3.0

    # interpolation/flash bar: exact-flash spot probes
    idx = np.linspace(0, n - 1, N_SPOT).astype(int)
    dev = 0.0
    for i in idx:
        cf_ex = real_phase_exact(gas, tab, Pc[i], Pa)
        dev = max(dev, abs(cf_ex - ph['cf_capped'][i]) / abs(cf_ex))
    bar_interp = S_BAR * dev * isp_real
    tol_row = bar_quad + bar_interp + 64.0 * EPS_MACH * isp_real

    # cap-structure probe at the worst (lowest-margin) phase + mid phase
    cap_ok, cap_margin, cap_bar = True, np.inf, 0.0
    if Pa > 0.0:
        for i in (int(np.argmin(ph['Pstar'] / Pa)), n // 2):
            okp, mg, br = cap_structure_probe(tab, float(Pc[i]), Pa)
            cap_ok &= okp
            if mg < cap_margin:
                cap_margin, cap_bar = mg, br

    # naive-vs-capped on subcritical phases (EOS-general counterexample);
    # two-level metric with the MEASURED table-noise bar: near the
    # critical boundary the true gap -> 0 and only noise remains, so the
    # max is bounded by +noise while the DEEPEST subcritical phase must
    # lose strictly beyond the noise bar
    subm = ~ph['supercritical']
    cf_scale = float(np.max(np.abs(ph['cf_capped'])))
    cf_noise = S_BAR * dev * cf_scale + 64.0 * EPS_MACH * cf_scale
    if subm.any() and Pa > 0.0:
        gaps = ph['cf_naive'][subm] - ph['cf_capped'][subm]
        naive_gap_max = float(np.max(gaps))
        i_deep = int(np.argmin(np.where(subm, ph['Pstar'] / Pa, np.inf)))
        naive_gap_deep = float(ph['cf_naive'][i_deep]
                               - ph['cf_capped'][i_deep])
    else:
        naive_gap_max = naive_gap_deep = None

    delta = (isp_real - isp_cl) / isp_cl
    vac = (Pa == 0.0)
    return dict(
        prop=s['prop'], phi=s['phi'], PR=s['PR'], P0a=s['P0'] / ATM,
        Pa_atm=Pa / ATM, n=n, m_tab=M_TAB, vacuum=vac,
        T_floor=(T_FLOOR if vac else None),
        Isp=dict(ideal_real=isp_real, ideal_real_naive=isp_real_naive,
                 ideal_closed=isp_cl, ideal_closed_naive=isp_cl_naive),
        delta_rel=delta, tol_row=tol_row, bar_quad=bar_quad,
        bar_interp=bar_interp, delta_significant=bool(abs(delta) > tol_row
                                                      / isp_cl),
        cstar0_real=float(ph['cstar'][0]), cstar0_closed=s['cstar0'],
        crit_ratio_real=float((Pc / ph['Pstar'])[0]),
        crit_ratio_closed=float(npr_sonic(g)),
        frac_subcritical_real=float(np.mean(subm)),
        frac_subcritical_closed=(float(np.mean(Pc / Pa < npr_sonic(g)))
                                 if Pa > 0 else 0.0),
        subcritical=bool(subm.any()) and not vac,
        naive_gap_max=naive_gap_max, naive_gap_deep=naive_gap_deep,
        cf_noise=cf_noise,
        cap_probe=dict(ok=bool(cap_ok), margin=cap_margin, bar=cap_bar))


def check_row(row):
    """Invariants of one real-route row; used by tests/test_bounds_gamma.py
    both ways (must PASS shipped rows, FAIL corrupted ones)."""
    v = []
    I = row['Isp']
    if row['vacuum']:
        # declared lower-bound instrument: no cap/rejector semantics
        if not I['ideal_real'] > 0:
            v.append('vacuum: nonpositive floor instrument')
        return (not v), v
    if not row['cap_probe']['ok']:
        v.append('cap probe: grid exit beats the direct capped formula')
    if row['subcritical']:
        if row['naive_gap_deep'] is None:
            v.append('subcritical: naive-vs-capped margins missing')
        else:
            if not (row['naive_gap_deep'] < -row['cf_noise']):
                v.append('subcritical: naive does NOT lose to the cap at '
                         'the deepest phase beyond the noise bar '
                         '(EOS-general counterexample violated)')
            if not (row['naive_gap_max'] <= row['cf_noise']):
                v.append('subcritical: naive BEATS the cap beyond the '
                         'noise bar somewhere')
        if not I['ideal_real_naive'] < I['ideal_real'] + row['tol_row']:
            v.append('subcritical: naive Isp above capped Isp beyond bar')
    else:
        if abs(I['ideal_real_naive'] - I['ideal_real']) > row['tol_row']:
            v.append('supercritical: naive != capped beyond row bar')
    if not (row['crit_ratio_real'] > 1.0):
        v.append('critical ratio not > 1')
    return (not v), v


# ---------------------------------------------------- known-answer oracle
def known_answer(corrupt=False):
    """DECLARED gamma = const oracle: constant-cp gas (gamma = 7/5 exact)
    through the SAME real route must reproduce the closed forms within
    TOL_KA.  corrupt=True scales h0 by (1 + 1e-4): MUST be rejected."""
    ct = _ct()
    g = 1.4
    gas = ct.Solution(yaml=_PG_YAML)
    T0, P0, Pa = 3000.0, 20.0 * ATM, 1.0 * ATM
    gas.TP = T0, P0
    R = ct.gas_constant / gas.mean_molecular_weight
    tab = isen_table(gas, Pa / 8.0, m=M_TAB)
    checks = {}

    Pc = np.array([P0])
    ph = real_phase_cf(tab, Pc, Pa)
    h0 = ph['h0'][0] * ((1.0 + 1e-4) if corrupt else 1.0)
    cp = 3.5 * R
    # closed forms at gamma = 1.4 (the demoted oracle, exact here)
    Vid_cl = np.sqrt(2 * cp * T0 * (1 - (Pa / P0) ** ((g - 1) / g)))
    gas.SP = tab['s0'], Pa
    Vid_real = np.sqrt(max(2.0 * (h0 - gas.enthalpy_mass), 0.0))
    checks['V_id'] = abs(Vid_real / Vid_cl - 1.0)

    checks['crit_ratio'] = abs((Pc[0] / ph['Pstar'][0]) / npr_sonic(g) - 1.0)

    cstar_cl = cstar_fn(g, R, T0)
    checks['cstar'] = abs(ph['cstar'][0] / cstar_cl - 1.0)

    cf_cl = float(cf_ideal(g, Pc, Pa)[0])
    cf_real = float(ph['mdot'][0] * Vid_real / Pc[0])
    checks['CF_ideal'] = abs(cf_real / cf_cl - 1.0)

    ok = all(x <= TOL_KA for x in checks.values())
    return ok, checks


# ------------------------------------------------------------- 18 rows
def evaluate_all():
    D = load()
    if 'rows' not in D:
        raise RuntimeError('data/st_nozzle_opt.json has no rows')
    ka_ok, ka = known_answer()
    print('known-answer (gamma=1.4 constant-cp, DECLARED oracle): %s  %s'
          % ('PASS' if ka_ok else 'FAIL',
             ' '.join('%s=%.1e' % kv for kv in sorted(ka.items()))),
          flush=True)
    if not ka_ok:
        raise RuntimeError('known-answer oracle failed — real route broken')

    out, tabs = [], {}
    for r in D['rows']:
        key = dkey(r['prop'], r['Pcp'], r['paper']['phi_det'])
        s = D['states'][key]
        row = real_row(s, r['Pa'] * ATM)
        row.update(Pcp=r['Pcp'], nozzle=r['nozzle'], key=key,
                   phi_det=r['paper']['phi_det'])
        ok, viol = check_row(row)
        row['row_ok'], row['violations'] = ok, viol
        out.append(row)
        I = row['Isp']
        print('%-5s %3d %-9s  real %8.2f (naive %8.2f) | closed %8.2f '
              '(naive %8.2f) | delta %+.3f%% (bar %.3f%%) %s %s'
              % (row['prop'], row['Pcp'], row['nozzle'], I['ideal_real'],
                 I['ideal_real_naive'], I['ideal_closed'],
                 I['ideal_closed_naive'], 100 * row['delta_rel'],
                 100 * row['tol_row'] / I['ideal_closed'],
                 'SIG' if row['delta_significant'] else 'in-bar',
                 'OK' if ok else 'VIOLATED: ' + '; '.join(viol)),
              flush=True)

    rec = dict(
        provenance='src/thrust/bounds_gamma.py evaluate_all(): real-thermo '
                   '(frozen CJ products, Cantera h(s,P)) ceiling vs the '
                   'demoted gamma=const closed-form oracles; OP-0-gamma '
                   '(strengthened S5 gamma directive), session S7',
        semantics=dict(
            primary='ideal_real: sonic-capped per-streamtube ceiling, '
                    'V_id = sqrt(2[h0 - h(s,Pa)]) via Cantera frozen-'
                    'composition isentrope (EOS-general executable)',
            oracle='ideal_closed: bounds.py cf_ideal at the blessed frozen '
                   'gamma_s — DECLARED ORACLE, demoted per the standing '
                   'directive',
            naive='*_naive: uncapped complete-expansion forms, kept ONLY '
                  'as the executable rejection instrument',
            vacuum='vacuum rows: expansion truncated at T_FLOOR=200 K '
                   '(mechanism validity floor), a declared LOWER-BOUND '
                   'instrument, excluded from cap/concordance rejectors'),
        tol_ka=TOL_KA, m_tab=M_TAB, n=N_REAL, s_bar=S_BAR, rows=out)
    with open(REAL_JSON, 'w') as f:
        json.dump(rec, f, indent=1)
    _write_md(rec)
    nok = sum(1 for r in out if r['row_ok'])
    nsig = sum(1 for r in out if (not r['vacuum']) and r['delta_significant'])
    print('real ladder: %d/%d rows OK; %d finite-Pa rows with SIGNIFICANT '
          'gamma-purge delta -> %s' % (nok, len(out), nsig, REAL_JSON),
          flush=True)
    return rec


def _write_md(rec):
    L = ['# OP-0-gamma — real-thermo (gamma(T), frozen products) ceiling '
         'vs the demoted gamma=const oracle',
         '',
         'Primary route: Cantera h(s,P) frozen-composition isentrope; '
         'sonic cap via w(P*) = h0.',
         'Closed forms of `src/thrust/bounds.py` = DECLARED ORACLES '
         '(strengthened S5 directive).',
         'Generated by `src/thrust/bounds_gamma.py`; tests: '
         '`tests/test_bounds_gamma.py` (group (xi)).',
         '',
         '| Prop | Pcp | Nozzle | Pa | Isp real | Isp closed | delta % | '
         'bar % | sig | crit.ratio real/closed | subcrit frac r/c | '
         'cap probe |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in rec['rows']:
        I = r['Isp']
        L.append('| %s | %d | %s | %.1f | %.2f | %.2f | %+.3f | %.3f | %s |'
                 ' %.4f / %.4f | %.2f / %.2f | %s |'
                 % (r['prop'], r['Pcp'], r['nozzle'], r['Pa_atm'],
                    I['ideal_real'], I['ideal_closed'],
                    100 * r['delta_rel'],
                    100 * r['tol_row'] / I['ideal_closed'],
                    'SIG' if r['delta_significant'] else 'in-bar',
                    r['crit_ratio_real'], r['crit_ratio_closed'],
                    r['frac_subcritical_real'],
                    r['frac_subcritical_closed'],
                    'ok' if r['cap_probe']['ok'] else 'VIOLATED'))
    L += ['',
          'Vacuum rows: T-floor-truncated LOWER-BOUND instrument '
          '(declared), no cap semantics.',
          'delta % = (Isp_real - Isp_closed)/Isp_closed; SIG iff |delta| '
          'exceeds the derived row bar',
          '(Richardson quadrature + exact-flash interpolation probes + '
          'roundoff floor).']
    with open(REAL_MD, 'w') as f:
        f.write('\n'.join(L) + '\n')


if __name__ == '__main__':
    evaluate_all()
    print('OK', flush=True)
