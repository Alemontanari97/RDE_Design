#!/usr/bin/env python3
"""bounds.py — OP-0: the eps-level bound ladder for the cycle-averaged
thrust functional, from the Stechmann-Heister-Harroun closed forms.

Proposition B1 of the development plan (docs/rde_nozzle_development_plan.md
S1(iii), action A0.4); the eps-level instance of the M0 bound-ladder
globality mechanism M1 (docs/rde_nozzle_MASTER.md, Part IV).

THE LADDER. For each Table-1 detonation cycle {Pc(xi) = P0 PR^-xi,
xi ~ U[0,1), one frozen gamma, c*(xi) = c*0 (Pc/P0)^((g-1)/2g)} and
ambient Pa, in mass-weighted cycle-Isp units (Eq. 4; per unit throat
area, mdot c* = Pc A_t):

    Isp[eps_fix]  <=  Isp_intmax  ==  Isp_ideal  <=  B_EK        (chain C)

  Isp[eps_fix]  incumbent: fixed-geometry bell at the blessed row optimum
                (vacuum rows: the paper's geometric spec eps_max).
  Isp_intmax    int-max relaxation, int max_eps F dmu: each phase gets its
                own optimal admissible area ratio, from Theorem 1 of
                validation/bell_optimality_proof.md applied to the
                degenerate (single-phase) measure: interior root
                NPR(eps*(xi), g) = Pc(xi)/Pa where Pc/Pa > NPR(1,g),
                sonic boundary eps = 1 otherwise (there dCF/deps =
                1/NPR - Pa/Pc < 0: the boundary IS the phase argmax).
                Route: explicit eps*(xi) fed through the full Eq. 9.
  Isp_ideal     per-streamtube thermodynamic ceiling (M0 Proposition G-B
                at eps level) WITH the jet-matching admissibility (see
                CHOKING CAP below): complete isentropic expansion to Pa
                where realizable on the supersonic branch, sonic exit
                otherwise.  Independent closed-form route (no eps, no
                Eq. 9); Isp_intmax == Isp_ideal is the quasi-1D
                exhaustiveness theorem (the single eps DOF per phase
                exhausts the choked-streamtube freedom) and is ASSERTED
                by the dual-route agreement, not assumed.
  B_EK          integral-flux relaxation at eps level (the Efremov-Kraiko
                2004 mechanism; detonation-cycle precedent Kraiko-Egoryan
                2020): retain only the cycle-integral mass and kinetic-
                energy fluxes of the ideal family and allow redistribution
                between phases.  Closed form by Cauchy-Schwarz on the
                mdot-measure:  B_EK = sqrt(<u_eff^2>_mdot)/g0  with
                u_eff(xi) = F_id(xi)/mdot(xi) = CF_id(xi) c*(xi), against
                Isp_ideal = <u_eff>_mdot/g0.  Equality iff u_eff is
                mu-a.e. constant — strictly false under blowdown (PR > 1),
                so the top gap is strictly positive.

  M1 INSTANCE (M0 Theorem 6 + corollary): for Pa > 0 the untruncated
  peak-designed S-H plug (saturation knee at NPR = P0/Pa, Eq. 10-12
  closure) reproduces the complete-expansion form phase by phase, hence
  ATTAINS the ceiling wherever the cycle stays supercritical
  (choke_margin >= 1): zero duality gap = global optimality over the
  eps-level class.  In vacuum no finite geometry attains the ceiling
  (Theorem 3 of the proof note: Isp strictly increasing in eps).

CHOKING CAP (correction of record to the naive per-streamtube form).
The published ideal-adaptation form F_id = "complete isentropic expansion
to Pa, phase by phase" is an upper bound ONLY where Pc/Pa >= NPR(1,g)
(supercritical phases: full expansion realizable supersonic).  For
1 < Pc/Pa < NPR(1,g) the exit that matches Pa is SUBSONIC, and moving
from the sonic exit toward it along the subsonic branch loses thrust
monotonically (dF/dA_e = Pe - Pa < 0 there, with the jet-matching
condition Pe = Pa enforceable only at the endpoint): the sonic exit
strictly beats "full expansion to Pa".  Executable counterexample
(cf_ideal_naive vs cf_sonic, g = 1.15, Pc/Pa = 1.3): 0.4587 < 0.4656.
Consequently on cycles that dip subcritical (Table-1 20-atm hydrocarbon
rows, choke_margin < 1) the NAIVE ladder rung is VIOLATED
(Isp_ideal_naive < Isp_intmax); the capped ceiling restores chain C.
Both forms are computed and persisted; tests/test_bounds.py REJECTS the
naive rung on exactly those rows.  M0 Prop. G-B and the T4/H-T4 closure
inherit the cap as an explicit hypothesis (min-cycle NPR >= critical).

Hypotheses (inherited, stated): H1-H5 of validation/bell_optimality_proof
.md (frozen gamma, choked feed mdot = Pc A_t/c*, fixed full-flowing
geometry per member, exponential blowdown only through the shipped
states); quadrature = trapezoid on the NQ grid of the blessed pipeline —
the chain is pointwise in xi for rungs 0-2 and discrete-Cauchy-Schwarz
for the top rung, so it holds row by row up to roundoff, for which the
derived tolerance is TOL_REL = NQ * machine-eps (N-term sum error bound),
never a magic number.

Usage:
  python src/thrust/bounds.py          # evaluate 18 rows -> data/ + stdout
Outputs: data/bounds_ladder.json (numbers of record, consumed by
tests/test_bounds.py) and data/bounds_ladder.md (human table).
"""
import json
import os
import sys

import numpy as np

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from src.common.constants import G0, P_ATM as ATM
from src.thrust.st_core import TR, cf_base, cf_bell, cf_spike
from src.thrust.stechmann_nozzle import NQ, dkey, eps_of_npr, load

EPS_MACH = float(np.finfo(float).eps)
TOL_REL = NQ * EPS_MACH          # roundoff bound for an NQ-term quadrature sum
LADDER_JSON = os.path.join(_ROOT, 'data', 'bounds_ladder.json')
LADDER_MD = os.path.join(_ROOT, 'data', 'bounds_ladder.md')


# ------------------------------------------------------ per-phase closed forms
def npr_sonic(g):
    """Critical (sonic-exit) pressure ratio NPR(eps=1, g)."""
    return ((g + 1) / 2) ** (g / (g - 1))


def cf_ideal_naive(g, Pc, Pa):
    """NAIVE per-streamtube ideal: complete isentropic expansion to Pa,
    unconditionally (the published ideal-adaptation form; == the free
    branch of Eq. 10).  NOT an upper bound on subcritical phases — kept
    for the executable rejection; see CHOKING CAP in the module header."""
    Pc = np.asarray(Pc, dtype=float)
    if Pa == 0.0:
        return np.full_like(Pc, np.sqrt(cf_base(g)))
    x = np.clip(1.0 - np.minimum(Pa / Pc, 1.0) ** ((g - 1) / g), 0.0, None)
    return np.sqrt(cf_base(g) * x)


def cf_sonic(g, Pc, Pa):
    """Thrust coefficient of the sonic (eps = 1) exit: momentum at the
    critical state plus the (Pe - Pa) A_t term — the per-phase argmax on
    the boundary of the admissible class when Pc/Pa <= NPR(1, g)."""
    return cf_bell(g, 1.0, np.asarray(Pc, dtype=float), Pa)


def cf_ideal(g, Pc, Pa):
    """Per-streamtube thermodynamic ceiling WITH the jet-matching
    admissibility: complete expansion to Pa where the supersonic branch
    reaches it (Pc/Pa >= NPR(1,g)), sonic exit otherwise."""
    Pc = np.asarray(Pc, dtype=float)
    if Pa == 0.0:
        return cf_ideal_naive(g, Pc, Pa)
    return np.where(Pc / Pa >= npr_sonic(g),
                    cf_ideal_naive(g, Pc, Pa), cf_sonic(g, Pc, Pa))


def eps_star_of_pc(g, Pc, Pa):
    """Vectorized Theorem-1 per-phase argmax: eps*(xi) with
    NPR(eps*, g) = Pc/Pa on the interior, clipped to the eps = 1
    boundary where Pc/Pa <= NPR(1, g).  Pa > 0 only (vacuum: no finite
    argmax, Theorem 3)."""
    Pc = np.asarray(Pc, dtype=float)
    NPR = np.maximum(Pc / Pa, npr_sonic(g))
    Me2 = 2.0 / (g - 1) * (NPR ** ((g - 1) / g) - 1.0)
    Me = np.sqrt(Me2)
    return (1.0 / Me) * ((2.0 / (g + 1)) * (1 + (g - 1) / 2 * Me2)) \
        ** ((g + 1) / (2 * (g - 1)))


def cf_intmax(g, Pc, Pa):
    """Int-max rung by the EXPLICIT Theorem-1 route: per-phase optimal
    eps*(xi) fed through the full Eq. 9 (bell) closed form.  Numerically
    independent of cf_ideal (which never touches Eq. 9); the ladder test
    asserts their agreement (dual-route certificate).  Vacuum: the sup
    over eps is the complete-expansion limit, not attained."""
    Pc = np.asarray(Pc, dtype=float)
    if Pa == 0.0:
        return cf_ideal_naive(g, Pc, Pa)
    NPRs = npr_sonic(g)
    NPR = np.maximum(Pc / Pa, NPRs)
    eps = eps_star_of_pc(g, Pc, Pa)
    mom = np.sqrt(cf_base(g) * (1.0 - NPR ** (-(g - 1) / g)))
    return mom + eps * (1.0 / NPR - Pa / Pc)


# ------------------------------------------------------------ the ladder rung
def ladder_row(s, Pa, eps_fix, n=NQ):
    """Evaluate every rung of chain C on one blessed detonation state.

    s: state dict from data/st_nozzle_opt.json (P0, PR, gamma, cstar0);
    Pa: ambient [Pa]; eps_fix: incumbent fixed bell area ratio.
    Returns the persistable row record (Isp units, s)."""
    g = s['gamma']
    xi = np.linspace(0.0, 1.0, n)
    Pc = s['P0'] * s['PR'] ** (-xi)
    cs = s['cstar0'] * (Pc / s['P0']) ** ((g - 1) / (2 * g))
    md = Pc / cs                                  # mdot / A_t
    den = G0 * TR(md, xi)

    def isp_of(cf):
        return float(TR(Pc * cf, xi) / den)

    vacuum = (Pa == 0.0)
    cfid = cf_ideal(g, Pc, Pa)
    u_eff = cfid * cs                             # F_id/mdot per phase
    isp = dict(
        bell=isp_of(cf_bell(g, eps_fix, Pc, Pa)),
        intmax=isp_of(cf_intmax(g, Pc, Pa)),
        ideal=isp_of(cfid),
        ideal_naive=isp_of(cf_ideal_naive(g, Pc, Pa)),
        ek=float(np.sqrt(TR(md * u_eff ** 2, xi) / TR(md, xi)) / G0),
    )
    # peak-designed S-H plug (M1 candidate): knee at the cycle peak for
    # Pa > 0; in vacuum the spike closure degenerates to the bell at the
    # geometric spec (Eq. 12 never releases), so eps_fix is the honest cap.
    if vacuum:
        isp['plug'] = isp_of(cf_spike(g, eps_fix, Pc, Pa))
        eps_plug = eps_fix
    else:
        eps_plug = eps_of_npr(s['P0'] / Pa, g)
        isp['plug'] = isp_of(cf_spike(g, eps_plug, Pc, Pa))

    NPRs = npr_sonic(g)
    margin = float(Pc.min() / Pa / NPRs) if not vacuum else float('inf')
    frac_sonic = float(np.mean(Pc / Pa < NPRs)) if not vacuum else 0.0
    ueff_cv = float(np.std(u_eff) / np.mean(u_eff))
    tol_abs = TOL_REL * isp['ideal']
    return dict(gamma=g, PR=s['PR'], P0a=s['P0'] / ATM, Pa_atm=Pa / ATM,
                eps_fix=eps_fix, eps_plug=float(eps_plug), n=n,
                vacuum=vacuum, subcritical=bool(margin < 1.0),
                choke_margin=margin, frac_sonic=frac_sonic,
                eps_star_peak=(None if vacuum else
                               float(eps_star_of_pc(g, s['P0'], Pa))),
                u_eff_cv=ueff_cv, Isp=isp, tol_abs=tol_abs,
                gaps=dict(bell_vs_intmax=isp['intmax'] - isp['bell'],
                          intmax_vs_ideal=isp['ideal'] - isp['intmax'],
                          ideal_vs_ek=isp['ek'] - isp['ideal'],
                          plug_vs_ideal=isp['ideal'] - isp['plug'],
                          naive_vs_intmax=isp['ideal_naive'] - isp['intmax']))


def check_chain(row):
    """Verify chain C and the M1/naive-rejection structure on one row.
    Returns (ok, violations).  Used by tests/test_bounds.py both ways:
    it must PASS every shipped row and FAIL every corrupted one."""
    v = []
    t, I = row['tol_abs'], row['Isp']
    if not I['bell'] <= I['intmax'] + t:
        v.append('order: bell > intmax')
    if not I['bell'] < I['intmax'] - t:
        v.append('strictness: bell gap below resolution')
    if not abs(I['intmax'] - I['ideal']) <= t:
        v.append('dual-route: intmax != ideal (quasi-1D exhaustiveness)')
    if not I['ideal'] <= I['ek'] + t:
        v.append('order: ideal > B_EK')
    if not I['ideal'] < I['ek'] - t:
        v.append('strictness: EK gap below resolution (u_eff constant?)')
    if row['vacuum']:
        if not I['plug'] < I['ideal'] - t:
            v.append('vacuum: finite plug must NOT attain the ceiling')
    elif row['subcritical']:
        if not abs(I['plug'] - I['ideal_naive']) <= t:
            v.append('subcritical: plug != naive ideal (S-H closure identity)')
        if not I['ideal_naive'] < I['intmax'] - t:
            v.append('subcritical: expected naive-bound violation missing')
    else:
        if not abs(I['plug'] - I['ideal']) <= t:
            v.append('M1: peak plug does not attain the ceiling')
        if not abs(I['ideal_naive'] - I['ideal']) <= t:
            v.append('supercritical: naive != capped ceiling')
    return (not v), v


# ------------------------------------------------------------- 18-row driver
def evaluate_all():
    """Chain C on the 18 Table-1 rows (blessed states + blessed incumbent
    eps).  Persists data/bounds_ladder.json + data/bounds_ladder.md."""
    D = load()
    if 'rows' not in D:
        raise RuntimeError('data/st_nozzle_opt.json has no optimization rows;'
                           ' run stechmann_nozzle.py optimize first')
    out = []
    for r in D['rows']:
        s = D['states'][dkey(r['prop'], r['Pcp'], r['paper']['phi_det'])]
        Pa = r['Pa'] * ATM
        row = ladder_row(s, Pa, float(r['model']['det']['eps']))
        row.update(prop=r['prop'], Pcp=r['Pcp'], nozzle=r['nozzle'],
                   phi_det=r['paper']['phi_det'],
                   key=dkey(r['prop'], r['Pcp'], r['paper']['phi_det']))
        ok, viol = check_chain(row)
        row['chain_ok'], row['violations'] = ok, viol
        out.append(row)
        I = row['Isp']
        print('%-5s %3d %-9s  bell %7.2f <= intmax %7.2f == ideal %7.2f'
              ' <= EK %7.2f | plug %7.2f | naive %7.2f | margin %7.2f %s'
              % (row['prop'], row['Pcp'], row['nozzle'], I['bell'],
                 I['intmax'], I['ideal'], I['ek'], I['plug'],
                 I['ideal_naive'], row['choke_margin'],
                 'OK' if ok else 'VIOLATED: ' + '; '.join(viol)),
              flush=True)
    rec = dict(
        provenance='src/thrust/bounds.py evaluate_all() on the blessed '
                   'states/rows of data/st_nozzle_opt.json; chain C of the '
                   'module docstring; OP-0 / plan action A0.4',
        definitions=dict(
            bell='fixed-geometry bell at the blessed row-optimal eps '
                 '(vacuum rows: geometric spec)',
            intmax='int max_eps F dmu, per-phase Theorem-1 argmax through '
                   'Eq. 9 (explicit eps*(xi) route)',
            ideal='per-streamtube ceiling with the choking cap '
                  '(complete expansion to Pa above NPR(1,g), sonic exit '
                  'below); independent closed-form route',
            ideal_naive='UNCAPPED complete expansion to Pa (published '
                        'ideal-adaptation form) — not a bound when '
                        'choke_margin < 1: kept for the executable '
                        'rejection',
            ek='integral-flux (Efremov-Kraiko-type) relaxation, '
               'Cauchy-Schwarz on the mdot measure: sqrt(<u_eff^2>)/g0',
            plug='S-H spike closure (Eqs. 10-12) at the peak-design knee '
                 'NPR = P0/Pa (vacuum: bell-degenerate at the spec eps)'),
        tol_rel=TOL_REL, n=NQ, rows=out)
    with open(LADDER_JSON, 'w') as f:
        json.dump(rec, f, indent=1)
    _write_md(rec)
    nok = sum(1 for r in out if r['chain_ok'])
    print('bound ladder: %d/%d rows chain-OK -> %s'
          % (nok, len(out), LADDER_JSON), flush=True)
    return rec


def _write_md(rec):
    L = ['# OP-0 — eps-level bound ladder on the 18 Table-1 rows',
         '',
         'Chain C:  Isp[eps_fix] <= Isp_intmax == Isp_ideal <= B_EK '
         '(mass-weighted cycle Isp, s).',
         'Generated by `src/thrust/bounds.py`; numbers of record in '
         '`data/bounds_ladder.json`;',
         'executable verification incl. violated-ordering rejection: '
         '`tests/test_bounds.py`.',
         'Ceiling = per-streamtube ideal WITH the choking cap; the naive '
         '(uncapped) column is',
         'NOT a bound on subcritical rows (choke_margin < 1) — shown '
         'struck through there.',
         '',
         '| Prop | Pcp | Nozzle | eps_fix | bell | int-max | ideal | B_EK |'
         ' plug(SH) | naive | margin | regime |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in rec['rows']:
        I = r['Isp']
        regime = ('vacuum: ceiling unattained' if r['vacuum'] else
                  'subcritical tail: naive rung VIOLATED' if r['subcritical']
                  else 'M1: plug attains ceiling (gap-zero)')
        naive = ('~~%.2f~~' if r['subcritical'] else '%.2f') % I['ideal_naive']
        L.append('| %s | %d | %s | %.2f | %.2f | %.2f | %.2f | %.2f | %.2f |'
                 ' %s | %.2f | %s |'
                 % (r['prop'], r['Pcp'], r['nozzle'], r['eps_fix'], I['bell'],
                    I['intmax'], I['ideal'], I['ek'], I['plug'], naive,
                    r['choke_margin'], regime))
    L += ['',
          'Notes: the bell gap (int-max minus bell) is the value of the '
          'per-phase relaxation;',
          'the EK gap is strictly positive because u_eff varies along the '
          'blowdown (CV column',
          'persisted in the JSON); plug == naive is an identity of the S-H '
          'spike closure, so the',
          'M1 attainment statement is exact precisely where the cycle stays '
          'supercritical.']
    with open(LADDER_MD, 'w') as f:
        f.write('\n'.join(L) + '\n')


if __name__ == '__main__':
    evaluate_all()
    print('OK', flush=True)
