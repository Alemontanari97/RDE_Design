#!/usr/bin/env python3
"""phase_diagram_real.py — OP-11-eps ON THE REAL ROUTE [F1/OP-0-gamma tail,
session S8]: the quasi-1D topology phase diagram re-derived with the
EOS-GENERAL primary route of bounds_gamma (Cantera h(s,P) on the frozen
CJ-products isentrope, exact sonic cap via w(P*) = h0), plus the
EQUILIBRIUM-EXPANSION (shifting) ceiling as the declared UPPER BRACKET of
the frozen rung.

WHY (standing gamma directive, strengthened S5; M0 Prop. 7 GAMMA-PURGE
INSTANCE, declared residual): the OP-11-eps diagram of record
(src/thrust/phase_diagram.py) evaluates its cells with the gamma = const
closed forms — after the S7 ladder purge those are DECLARED ORACLES, so
the diagram itself needed the primary-route re-derivation.  This module
supplies it.  The eps-level module REMAINS of record as the closed-form
oracle instrument; this one is the PRIMARY-route instance.

WINNER SEMANTICS — unchanged and non-negotiable (D3 §10quater(5), M0
D2.6): winners rank VALUE MODELS (closures) at equal eps_max, NEVER
hardware sectors of the constrained problem (P); the released capped plug
IS the per-phase relaxation (its win prices the ADAPTATION PREMIUM);
bell-winning regions of (P) are EXPECTED at contour level; the per-cell
certificate toward (P) is premium_bound = Isp_ideal - Isp_bell.

THE REAL-ROUTE CELL (all EOS-general, no gamma anywhere in the primary
computations):
  bell     fixed full-flowing bell at eps_bell = min(eps*_real, eps_max),
           where eps*_real solves the EXECUTABLE (**') REDUCTION
                <P_E(eps; xi)>_mu = Pa
           by bisection — the quasi-1D weighted-transversality condition
           (M0 T7(c) executable reduction) evaluated with real thermo:
           the first EOS-GENERAL carrier of the reduction (the closed
           form NPR(eps*) = <Pc>/Pa is its gamma = const oracle).  The
           per-phase exit state P_E(eps) inverts the real area-ratio map
           eps(P) = mdot/(rho(P) u(P)), u = sqrt(2[h0 - h(P)]), on the
           supersonic branch of the phase's isentrope segment.
  plug_sh  the NAIVE-adaptation closure (released phases at UNCAPPED
           complete expansion) — kept ONLY as the executable rejection
           instrument (the published S-H free branch, gamma-purged).
  plug     the closure OF RECORD (capped adaptation): bell branch at
           eps_plug = min(knee_real, eps_max) while underexpanded
           (P_E > Pa), per-phase SONIC-CAPPED ideal once released;
           knee_real = real adaptation area ratio of the PEAK phase,
           eps_ad = mdot_peak / (rho(Pa) V_id,peak).
  ideal    the sonic-capped real ceiling (bounds_gamma.real_phase_cf).
DOMINANCE (EOS-general, phase-wise): underexpanded phases ride the same
bell branch at eps_plug >= eps_bell with dF/dA_E = P_E - Pa > 0 (the
classical sign argument, no EOS input); released phases take the capped
per-phase supremum (cap-probe theorem of bounds_gamma).  Hence plug >=
bell and plug >= plug_sh pointwise, and a 'bell' winner is IMPOSSIBLE
under the closure of record — check_cell_real treats it as a violation
and the tests corrupt cells to prove rejection.  At eps_max >= knee_real
the plug coincides with the capped ceiling phase by phase: M1
duality-gap-zero attainment NOW CERTIFIED ON THE REAL ROUTE (previously
an eps-level closed-form result).

EQUILIBRIUM BRACKET (per PR; ceiling is eps_max-independent): the same
cycle evaluated with the SHIFTING-equilibrium isentrope (SP-equilibrate
at each (s0, P); equilibrium sound speed from c^2 = dP/drho along the
table).  Classical model ordering frozen <= finite-rate <= equilibrium
(Sutton/CEA doctrine; N4 ladder rungs): here EXECUTABLE —
Isp_ideal,eq >= Isp_ideal,frozen is CHECKED per PR with derived bars
(nested-table Richardson + roundoff floor) and a known-answer rejector
(constant-cp gas: equilibrate is a no-op, the eq route must reproduce
the closed forms within bounds_gamma.TOL_KA; corrupted route rejected).
The pair [frozen, equilibrium] is the declared MODEL BRACKET of the
caloric closure at ceiling level; class THEOREM* within the ideal-gas
mixture closure pair, falsifier = the executable inequality itself.

DECLARED SCOPE LIMITS: (a) vacuum sweep NOT re-derived here — the vacuum
no-finite-optimum theorem is EOS-general with the eps-level executable
as carrier, and real vacuum rows are T-floor-truncated lower-bound
instruments (bounds_gamma), where diagram semantics add nothing;
(b) full-flowing members (no separation), as in the eps module.

NUMERICS (bars derived, no magic numbers): one frozen isentrope table
(bounds_gamma.isen_table, M_TAB flashes) re-anchored at the highest grid
P0 covers every cell (all cells share the anchor's entropy s0);
quadrature bar per cell by nested-grid Richardson on the phase grid
(N_PH odd); interpolation bar per PR by bounds_gamma.real_phase_exact
spot flashes; tie tolerance = the cell's summed derived bars.

Usage:
  python src/thrust/phase_diagram_real.py   # grid -> data/ + stdout
Outputs: data/phase_diagram_real.json (numbers of record, consumed by
tests/test_phase_diagram_real.py) and data/phase_diagram_real.md.
"""
import json
import os
import sys

import numpy as np

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from src.common.constants import G0, P_ATM as ATM
from src.thrust.st_core import TR, _ct
from src.thrust.stechmann_nozzle import dkey, load
from src.thrust.bounds_gamma import (EPS_MACH, M_TAB, N_SPOT, S_BAR, TOL_KA,
                                     _PG_YAML, _interp, frozen_sound_speed,
                                     isen_table, products_gas, real_phase_cf,
                                     real_phase_exact)
from src.thrust.phase_diagram import ANCHOR, EPS_MAX_GRID, PR_GRID, i1

REAL_DIAG_JSON = os.path.join(_ROOT, 'data', 'phase_diagram_real.json')
REAL_DIAG_MD = os.path.join(_ROOT, 'data', 'phase_diagram_real.md')

# --- derived numerical parameters (rationale in module docstring) --------
N_PH = 401        # phase grid per cell (odd -> nested Richardson at 201);
                  # quadrature error carried as the derived per-cell bar
M_EQ = 241        # equilibrium isentrope table points (odd -> nested
                  # Richardson at 121); eq bar measured, not trusted
N_BIS = 60        # bisection budget: 2^-60 interval << all derived bars
C_RND = 64.0      # roundoff floor factor (ops-count scale, as bounds_gamma)


# ------------------------------------------------------------- tables
def build_frozen_table(anchor, Pa, PRs):
    """One frozen isentrope table spanning ALL cells: every synthetic
    state at spread PR sits on the anchor's products isentrope (entropy
    s0), with stagnation at P0(PR) = <Pc>/I1(PR).  Re-anchor the gas at
    the HIGHEST grid P0 and tabulate down to the bounds_gamma margin."""
    gas = products_gas(anchor)
    s0 = gas.entropy_mass
    Pc_mean = anchor['P0'] * i1(anchor['PR'])
    P_hi = max(Pc_mean / i1(PR) for PR in PRs)
    gas.SP = s0, float(P_hi)
    # table floor: the AREA-RATIO inversion needs branch depth beyond the
    # ceiling's Pa/8 margin — the deepest phase (Pc_min = <Pc> ln PR /
    # (PR - 1), ~1.06 atm at PR = 90) must tabulate past eps ~ eps*
    # (~3.5): Pa/64 gives it eps ~ 8-9 of headroom; the eps_star_real
    # RuntimeError guard rejects any future grid that outruns this.
    P_lo = Pa / 64.0
    tab = isen_table(gas, P_lo)
    return gas, tab, Pc_mean


def build_eq_table(anchor, Pa, P_hi, m=M_EQ):
    """Shifting-equilibrium isentrope table on the SAME entropy s0:
    sequential SP flashes each followed by equilibrate('SP', Gibbs
    solver: no ChemEquil 3000-K guess-range extrapolation) (descent in
    ln P keeps every flash near its start — robust); equilibrium sound
    speed from c^2 = dP/drho along the table (no closed form used)."""
    gas = products_gas(anchor)
    s0 = gas.entropy_mass
    lnP = np.linspace(np.log(P_hi), np.log(Pa / 8.0), m)
    h = np.empty(m); rho = np.empty(m); T = np.empty(m)
    for i, lp in enumerate(lnP):
        gas.SP = s0, float(np.exp(lp))
        gas.equilibrate('SP', solver='gibbs')
        h[i] = gas.enthalpy_mass
        rho[i] = gas.density
        T[i] = gas.T
    P = np.exp(lnP)
    c2 = np.gradient(P, rho)                    # dP/drho along the isentrope
    if not np.all(c2 > 0):
        raise RuntimeError('equilibrium c^2 = dP/drho not positive — '
                           'eq isentrope table invalid')
    return dict(lnP=lnP[::-1], h=h[::-1], c=np.sqrt(c2)[::-1],
                rho=rho[::-1], T=T[::-1], s0=s0, P_hi=P_hi)


# ------------------------------------------- per-phase bell-branch inversion
def phase_branches(tab, Pc):
    """Per-phase supersonic-branch arrays for the area-ratio inversion:
    for phase i, (epsd, lnPd) with epsd ASCENDING from the exact sonic
    point (eps = 1 at lnP*) down the isentrope; plus h0, mdot, lnPstar."""
    lnPc = np.log(Pc)
    h0 = _interp(tab, 'h', lnPc)
    w = tab['h'] + 0.5 * tab['c'] ** 2
    lnPstar = np.interp(h0, w, tab['lnP'])
    ustar = _interp(tab, 'c', lnPstar)
    rhostar = _interp(tab, 'rho', lnPstar)
    mdot = rhostar * ustar
    branches = []
    for i in range(Pc.size):
        mask = tab['lnP'] < lnPstar[i]
        lnPb = tab['lnP'][mask]                 # ascending
        u = np.sqrt(np.maximum(2.0 * (h0[i] - tab['h'][mask]), 0.0))
        eps = mdot[i] / (tab['rho'][mask] * u)
        # descending lnP == ascending eps; prepend the exact sonic point
        lnPd = np.concatenate(([lnPstar[i]], lnPb[::-1]))
        epsd = np.concatenate(([1.0], eps[::-1]))
        branches.append((epsd, lnPd))
    return dict(branches=branches, h0=h0, mdot=mdot, lnPstar=lnPstar,
                ustar=ustar, rhostar=rhostar)


def pe_of_eps(br, eps):
    """Exit pressure per phase at shared area ratio eps (>= 1): monotone
    interpolation on each phase's branch (clipped at the table floor —
    only the threshold vs Pa is consumed beyond adaptation)."""
    return np.exp(np.array([np.interp(eps, e, l) for e, l in
                            br['branches']]))


def bell_cf_at(br, tab, Pc, Pa, eps):
    """Fixed full-flowing bell CF per phase at area ratio eps (real
    route): CF = [mdot u_E + (P_E - Pa) eps] / Pc."""
    PE = pe_of_eps(br, eps)
    lnPE = np.log(PE)
    hE = _interp(tab, 'h', lnPE)
    uE = np.sqrt(np.maximum(2.0 * (br['h0'] - hE), 0.0))
    return (br['mdot'] * uE + (PE - Pa) * eps) / Pc, PE


def eps_star_real(br, Pc, Pa, xi):
    """The executable (**') reduction on the real route: eps* solving
    <P_E(eps; xi)>_mu = Pa (trapezoid mean on xi), by bisection in
    ln eps.  If even the sonic annulus is mu-mean overexpanded
    (<P*> <= Pa) the cap eps* = 1 binds."""
    def mean_pe(eps):
        return float(TR(pe_of_eps(br, eps), xi))
    if mean_pe(1.0) <= Pa:
        return 1.0
    # upper end: the shallowest branch's last tabulated eps bounds all
    eps_hi = min(float(e[-1]) for e, _ in br['branches'])
    if mean_pe(eps_hi) > Pa:                     # table floor too shallow
        raise RuntimeError('eps* beyond the tabulated branch — extend '
                           'the isentrope table')
    lo, hi = 0.0, float(np.log(eps_hi))
    for _ in range(N_BIS):
        mid = 0.5 * (lo + hi)
        if mean_pe(float(np.exp(mid))) > Pa:
            lo = mid
        else:
            hi = mid
    return float(np.exp(0.5 * (lo + hi)))


# ------------------------------------------------------------- one PR block
def pr_block(tab, anchor_Pc_mean, PR, Pa, n=N_PH):
    """Everything eps_max-independent for one spread PR: phase grid,
    ceiling, eps*_real, knee_real, branch arrays, derived bars."""
    P0 = anchor_Pc_mean / i1(PR)
    xi = np.linspace(0.0, 1.0, n)
    Pc = P0 * PR ** (-xi)
    ph = real_phase_cf(tab, Pc, Pa)
    br = phase_branches(tab, Pc)

    def isp(cf, md=None):
        md = ph['mdot'] if md is None else md
        return float(TR(Pc * cf, xi) / (G0 * TR(md, xi)))

    isp_ideal = isp(ph['cf_capped'])
    # nested-grid Richardson quadrature bar (same derivation as
    # bounds_gamma.real_row)
    ph2 = real_phase_cf(tab, Pc[::2], Pa)
    isp_ideal_2 = float(TR(Pc[::2] * ph2['cf_capped'], xi[::2])
                        / (G0 * TR(ph2['mdot'], xi[::2])))
    bar_quad = S_BAR * abs(isp_ideal - isp_ideal_2) / 3.0

    eps_star = eps_star_real(br, Pc, Pa, xi)
    # real knee: adaptation area ratio of the PEAK phase (complete
    # expansion to Pa); 1.0 if the peak itself is subcritical
    if ph['Pstar'][0] >= Pa:
        hE0 = float(np.interp(np.log(Pa), tab['lnP'], tab['h']))
        Vid0 = float(np.sqrt(max(2.0 * (br['h0'][0] - hE0), 0.0)))
        rhoa = float(np.interp(np.log(Pa), tab['lnP'], tab['rho']))
        knee = float(br['mdot'][0] / (rhoa * Vid0))
    else:
        knee = 1.0
    return dict(PR=PR, P0=P0, xi=xi, Pc=Pc, ph=ph, br=br, isp=isp,
                isp_ideal=isp_ideal, bar_quad=bar_quad,
                eps_star=eps_star, knee=knee)


def cell_row_real(blk, tab, eps_max, Pa, bar_interp_rel):
    """One (eps_max, PR) cell on the real route: candidates, winner,
    M1 certificate, premium bound, derived tie tolerance."""
    Pc, ph, br, xi = blk['Pc'], blk['ph'], blk['br'], blk['xi']
    eps_bell = min(blk['eps_star'], eps_max)
    eps_plug = min(blk['knee'], eps_max)

    cf_bell_v, _ = bell_cf_at(br, tab, Pc, Pa, eps_bell)
    cf_plug_branch, PE_plug = bell_cf_at(br, tab, Pc, Pa, eps_plug)
    released = PE_plug <= Pa
    cf_plug = np.where(released, ph['cf_capped'], cf_plug_branch)
    cf_plug_sh = np.where(released, ph['cf_naive'], cf_plug_branch)

    cand = dict(bell=blk['isp'](cf_bell_v),
                plug=blk['isp'](cf_plug),
                plug_sh=blk['isp'](cf_plug_sh))
    isp_ideal = blk['isp_ideal']

    tol_abs = (blk['bar_quad'] + bar_interp_rel * isp_ideal
               + C_RND * EPS_MACH * isp_ideal)
    if abs(cand['plug'] - cand['bell']) <= tol_abs:
        win = 'tie'
    elif cand['plug'] > cand['bell']:
        win = 'plug' if eps_max >= blk['knee'] else 'plug-capped'
    else:
        win = 'bell'
    best = max(cand['bell'], cand['plug'])
    subm = ~ph['supercritical']
    return dict(
        PR=blk['PR'], eps_max=eps_max, P0=blk['P0'],
        eps_star=blk['eps_star'], eps_bell=float(eps_bell),
        eps_knee=blk['knee'], eps_plug_used=float(eps_plug),
        knee_fits=bool(eps_max >= blk['knee']),
        n_released=int(np.sum(released)),
        frac_subcritical=float(np.mean(subm)),
        Isp=dict(ideal=isp_ideal), cand=cand, winner=win,
        m1_gap=float(isp_ideal - best),
        m1_gap_zero=bool(isp_ideal - best <= tol_abs),
        premium_bound=float(isp_ideal - cand['bell']),
        tol_abs=float(tol_abs), bar_quad=blk['bar_quad'],
        bar_interp_rel=float(bar_interp_rel))


def check_cell_real(row):
    """Invariants of one real-route cell (tests use it BOTH ways):
    dominance, winner discipline, ceiling ordering, M1 flags, premium
    identity, T3-oracle tie at PR = 1."""
    v = []
    t, c, I = row['tol_abs'], row['cand'], row['Isp']
    if not (c['plug'] >= c['bell'] - t and c['plug'] >= c['plug_sh'] - t):
        v.append('dominance: capped plug beaten (EOS-general closure '
                 'theorem violated)')
    # two-level naive metric (bounds_gamma precedent): the naive
    # instrument may TIE within the bar near the critical boundary but
    # must never BEAT the capped closure; strictness is asserted at the
    # deepest-spread cells by the test (where the gap resolves).
    if (row['frac_subcritical'] > 0 and row['n_released'] > 0
            and not c['plug_sh'] <= c['plug'] + t):
        v.append('naive instrument beats the capped closure beyond the '
                 'bar (cap theorem violated at gamma(T))')
    if row['winner'] == 'bell':
        v.append('bell winner: impossible under the capped closure')
    exp_win = ('tie' if abs(c['plug'] - c['bell']) <= t else
               ('plug' if (c['plug'] > c['bell'] and row['knee_fits'])
                else ('plug-capped' if c['plug'] > c['bell'] else 'bell')))
    if row['winner'] != exp_win:
        v.append('winner label inconsistent with candidates')
    best = max(c['bell'], c['plug'])
    if not best <= I['ideal'] + t:
        v.append('winner above the capped real ceiling')
    if row['m1_gap_zero'] != (I['ideal'] - best <= t):
        v.append('m1 flag inconsistent with the recomputed gap')
    if not abs(row['premium_bound'] - (I['ideal'] - c['bell'])) <= t:
        v.append('premium bound != ceiling minus bell (staleness)')
    if row['knee_fits'] and not row['m1_gap_zero']:
        v.append('T4/M1 real route: generous envelope fails to attain '
                 'the capped ceiling')
    if row['PR'] == 1.0 and row['winner'] != 'tie':
        v.append('PR=1 (degenerate measure): must tie')
    return (not v), v


# ------------------------------------------------------- equilibrium bracket
def eq_ceiling(eqtab, Pc, Pa, xi):
    """Sonic-capped ceiling Isp on the EQUILIBRIUM isentrope (same s0):
    identical structure to real_phase_cf, fed by the eq table."""
    ph = real_phase_cf(eqtab, Pc, Pa)
    return float(TR(Pc * ph['cf_capped'], xi) / (G0 * TR(ph['mdot'], xi)))


def known_answer_eq(Pa_atm_probe=None, corrupt=False):
    """Constant-cp known-answer through the EQUILIBRIUM machinery:
    equilibrate('SP') on a one-species gas is a no-op, so the eq route
    must agree with the FROZEN route on the same table specs within
    TOL_KA; corrupt=True scales the eq enthalpy column: MUST be
    rejected."""
    ct = _ct()
    gas = ct.Solution(yaml=_PG_YAML)
    T0, P0 = 3000.0, 20.0 * ATM
    Pa = ATM
    gas.TP = T0, P0
    s0 = gas.entropy_mass
    ftab = isen_table(gas, Pa / 8.0, m=M_EQ)
    # eq table on the same grid (equilibrate no-op for 1 species)
    lnP = np.linspace(np.log(P0), np.log(Pa / 8.0), M_EQ)
    h = np.empty(M_EQ); rho = np.empty(M_EQ)
    for i, lp in enumerate(lnP):
        gas.SP = s0, float(np.exp(lp))
        gas.equilibrate('SP', solver='gibbs')
        h[i] = gas.enthalpy_mass
        rho[i] = gas.density
    P = np.exp(lnP)
    c = np.sqrt(np.gradient(P, rho))
    etab = dict(lnP=lnP[::-1], h=h[::-1] * ((1.0 + 1e-4) if corrupt
                                            else 1.0),
                c=c[::-1], rho=rho[::-1], s0=s0, P_hi=P0)
    Pc = np.array([P0])
    # single-phase CF comparison (xi-integral degenerate): compare CFs
    pf = real_phase_cf(ftab, Pc, Pa)
    pe = real_phase_cf(etab, Pc, Pa)
    rel = abs(float(pe['cf_capped'][0] / pf['cf_capped'][0]) - 1.0)
    # the c^2 = dP/drho table derivative adds a grid term over the exact
    # frozen c: measure it on the sonic state and allow it beyond TOL_KA
    rel_c = abs(float(pe['ustar'][0] / pf['ustar'][0]) - 1.0)
    tol = TOL_KA + S_BAR * rel_c
    return (rel <= tol), dict(rel=rel, tol=tol, rel_c=rel_c)


def eq_bracket_rows(anchor, Pa, PRs, Pc_mean, P_hi):
    """Per-PR frozen-vs-equilibrium ceiling bracket with derived bars:
    nested-table Richardson (M_EQ vs (M_EQ-1)/2+1) + quadrature bar."""
    et_full = build_eq_table(anchor, Pa, P_hi, m=M_EQ)
    et_half = build_eq_table(anchor, Pa, P_hi, m=(M_EQ - 1) // 2 + 1)
    rows = []
    for PR in PRs:
        P0 = Pc_mean / i1(PR)
        xi = np.linspace(0.0, 1.0, N_PH)
        Pc = P0 * PR ** (-xi)
        isp_eq = eq_ceiling(et_full, Pc, Pa, xi)
        isp_eq_h = eq_ceiling(et_half, Pc, Pa, xi)
        bar_tab = S_BAR * abs(isp_eq - isp_eq_h)
        rows.append(dict(PR=PR, isp_eq=isp_eq, bar_tab=bar_tab))
    return rows


def check_bracket(rows_eq, cells):
    """The model-bracket inequality per PR: Isp_ideal,eq >= Isp_ideal,
    frozen within the summed bars (strictness reported, not required —
    it vanishes as dissociation does).  Rejector-tested."""
    v = []
    ideal_by_pr = {}
    for c in cells:
        ideal_by_pr.setdefault(c['PR'], c)
    for r in rows_eq:
        c = ideal_by_pr[r['PR']]
        tol = r['bar_tab'] + c['tol_abs']
        if not r['isp_eq'] >= c['Isp']['ideal'] - tol:
            v.append('PR=%g: equilibrium ceiling BELOW frozen beyond bars '
                     '(bracket violated)' % r['PR'])
    return (not v), v


# ------------------------------------------------------------------- driver
def evaluate_all():
    anchor = load()['states'][ANCHOR]
    Pa = ATM
    PRs = sorted(set(PR_GRID) | {float(anchor['PR'])})
    EMs = list(EPS_MAX_GRID)

    ka_ok, ka = known_answer_eq()
    print('eq-route known-answer (constant-cp, DECLARED oracle): %s '
          'rel=%.2e tol=%.2e' % ('PASS' if ka_ok else 'FAIL',
                                 ka['rel'], ka['tol']), flush=True)
    if not ka_ok:
        raise RuntimeError('equilibrium-route known-answer failed')

    gas, tab, Pc_mean = build_frozen_table(anchor, Pa, PRs)

    cells, nok = [], 0
    for PR in PRs:
        blk = pr_block(tab, Pc_mean, PR, Pa)
        # per-PR interpolation bar: exact-flash spot probes on the
        # ceiling route (bounds_gamma machinery)
        idx = np.linspace(0, N_PH - 1, N_SPOT).astype(int)
        dev = 0.0
        for i in idx:
            cf_ex = real_phase_exact(gas, tab, float(blk['Pc'][i]), Pa)
            dev = max(dev, abs(cf_ex - blk['ph']['cf_capped'][i])
                      / abs(cf_ex))
        bar_interp_rel = S_BAR * dev
        for em in EMs:
            row = cell_row_real(blk, tab, em, Pa, bar_interp_rel)
            ok, viol = check_cell_real(row)
            row['cell_ok'], row['violations_cell'] = ok, viol
            nok += ok
            cells.append(row)
        last = [r for r in cells if r['PR'] == PR]
        print('PR %8.2f (eps* %6.3f knee %7.3f): %s'
              % (PR, blk['eps_star'], blk['knee'], ' '.join(
                  {'tie': 'T', 'plug': 'P', 'plug-capped': 'c',
                   'bell': 'B'}[r['winner']]
                  + ('*' if r['m1_gap_zero'] else ' ') for r in last)),
              flush=True)

    rows_eq = eq_bracket_rows(anchor, Pa, PRs, Pc_mean, tab['P_hi'])
    br_ok, br_viol = check_bracket(rows_eq, cells)
    for r in rows_eq:
        c = next(x for x in cells if x['PR'] == r['PR'])
        gain = (r['isp_eq'] - c['Isp']['ideal']) / c['Isp']['ideal']
        r['gain_rel'] = float(gain)
        print('eq bracket PR %8.2f: frozen %8.2f s <= eq %8.2f s '
              '(gain %+.2f%%, bar %.3f s)'
              % (r['PR'], c['Isp']['ideal'], r['isp_eq'], 100 * gain,
                 r['bar_tab']), flush=True)

    rec = dict(
        provenance='src/thrust/phase_diagram_real.py evaluate_all() on '
                   'anchor %s: OP-11-eps re-derived on the EOS-general '
                   'primary route (bounds_gamma Cantera h(s,P), sonic '
                   'cap) + shifting-equilibrium ceiling bracket; '
                   '[F1/OP-0-gamma tail], session S8' % ANCHOR,
        semantics=dict(
            winner='ranks CLOSURES at equal eps_max, NEVER hardware '
                   'sectors of (P) — D3 par.10quater(5) verbatim; '
                   'premium_bound = ideal - bell is the tournament '
                   'device',
            eps_star='EXECUTABLE (**\') reduction <P_E(eps)>_mu = Pa on '
                     'the real isentrope — first EOS-general carrier of '
                     'the quasi-1D weighted transversality',
            plug='capped-adaptation closure of record (released phases '
                 'at the sonic-capped per-phase ideal)',
            plug_sh='naive-adaptation rejection instrument (uncapped '
                    'free branch)',
            bracket='frozen <= equilibrium ceiling per PR: executable '
                    'model bracket of the caloric closure (THEOREM* '
                    'within the ideal-gas mixture closure pair)'),
        anchor=dict(key=ANCHOR, P0=anchor['P0'], PR=anchor['PR'],
                    Pc_mean=Pc_mean),
        n_ph=N_PH, m_tab=M_TAB, m_eq=M_EQ, pr_grid=PRs, eps_max_grid=EMs,
        Pa_atm=1.0, cells=cells,
        eq_bracket=dict(rows=rows_eq, ok=br_ok, violations=br_viol,
                        known_answer=ka))
    with open(REAL_DIAG_JSON, 'w') as f:
        json.dump(rec, f, indent=1)
    _write_md(rec)
    print('real-route phase diagram: %d/%d cells OK, eq bracket %s -> %s'
          % (nok, len(cells), 'OK' if br_ok else 'VIOLATED',
             REAL_DIAG_JSON), flush=True)
    return rec


def _write_md(rec):
    PRs, EMs = rec['pr_grid'], rec['eps_max_grid']
    bykey = {(r['PR'], r['eps_max']): r for r in rec['cells']}
    sym = {'tie': 'tie', 'plug': 'PLUG', 'plug-capped': 'plug-cap',
           'bell': 'BELL!'}
    L = ['# OP-11-eps on the REAL ROUTE — EOS-general phase diagram '
         '(winner per (eps_max, PR) cell)',
         '',
         'Primary route: Cantera h(s,P) frozen-CJ-products isentrope, '
         'sonic cap via w(P*) = h0',
         '(src/thrust/bounds_gamma.py machinery); eps* from the '
         'EXECUTABLE weighted-transversality',
         'reduction <P_E(eps)>_mu = Pa (first EOS-general carrier); '
         'closed forms nowhere in the',
         'primary computations (gamma-purge complete at diagram level).',
         'Generated by `src/thrust/phase_diagram_real.py`; record in '
         '`data/phase_diagram_real.json`;',
         'oracles + rejection: `tests/test_phase_diagram_real.py` '
         '(group (xii)).',
         '',
         'SCOPE (unchanged, D3 par.10quater(5)): winners rank VALUE '
         'MODELS (closures) at equal',
         'eps_max, NOT hardware sectors of the constrained problem (P); '
         'premium_bound = ideal - bell',
         'is the per-cell tournament certificate.  Vacuum sweep: NOT '
         're-derived (declared — the',
         'vacuum theorem is EOS-general; real vacuum rows are T-floor '
         'lower-bound instruments).',
         '',
         '| eps_max \\ PR | ' + ' | '.join('%g' % p for p in PRs) + ' |',
         '|---' * (len(PRs) + 1) + '|']
    for em in EMs:
        cs = [bykey[(p, em)] for p in PRs]
        L.append('| %g | ' % em + ' | '.join(
            sym[c['winner']] + (' *' if c['m1_gap_zero'] else '')
            for c in cs) + ' |')
    L += ['',
          'Real eps*(<Pc>) and knee eps_ad(P0) per PR: ' + ', '.join(
              '%g: %.3f / %.2f' % (p, bykey[(p, EMs[0])]['eps_star'],
                                   bykey[(p, EMs[0])]['eps_knee'])
              for p in PRs) + '.',
          '',
          'Equilibrium bracket (per PR, ceiling level): ' + ', '.join(
              'PR %g: %+.2f%%' % (r['PR'], 100 * r['gain_rel'])
              for r in rec['eq_bracket']['rows'])
          + ' (gain of the shifting-equilibrium ceiling over the frozen '
            'rung; frozen <= eq verified within derived bars).']
    with open(REAL_DIAG_MD, 'w') as f:
        f.write('\n'.join(L) + '\n')


if __name__ == '__main__':
    evaluate_all()
    print('OK', flush=True)
