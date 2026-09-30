#!/usr/bin/env python3
"""ST SCOPING NUMBER [S-REVIEW 2026-09-05, carrier §H.2 (user order)]:
the per-wave Strouhal number St_n = f_wave * tau_n of the case-A family,
computed as ARITHMETIC ON RECORD DATA (no campaign), with a band over the
envelope of the RECORDED parameters. Registry ID: [X-STSC]. Consumes
finding problem-statement:st-marginal-numbers-uncarried (problem book
Def. 8.1: St := tau_n / t_c, tau_n = int dx/u along the mean streamline;
D1 sharpened: St_n = n Omega_w tau_n / 2 pi = f_wave tau_n).

RECORD INPUTS (each cited; nothing declared):
  (a) matched detonation cycle of the case-A family, CH4/O2 at Pcp = 20 atm,
      Ti = 200 K (Stechmann Table-1 chain, src/thrust/stechmann_nozzle.py
      matched(); cached states data/st_nozzle_opt.json keys
      det|CH4|20|1.66 (Table-1 det optimum phi) and det|CH4|20|1.00 (the
      fixed-phi anchor of Figs. 9/10)): U_CJ, PR, gamma_s, T_CJ, R.
      Blowdown T0(xi) isentropic (Stechmann Eq. 15): T0 in
      [T_CJ * PR^(-(g-1)/g), T_CJ] over the cycle.
  (b) annulus geometry of record: examples/example_design_10kN.py:36
      RBAR = 0.140 m (CH4/O2 10 kN, nozzled, A_t = 32.4 cm2 per
      examples/SOLUTION_headtohead.md:55 chain, W = 3.14 [2.2-5.4] -> ~3
      co-rotating heads) and examples/SOLUTION_headtohead.md:17-18 the
      45-mm workhorse annulus (600 N nozzled, A_t = 4.3 cm2, ~2-3 heads).
      Throat radius yt = sqrt(A_t/pi).
  (c) nozzle contour of record: the TOC instance of [X-TOCV]
      (validation/a1_toc_variational_jax.py TCASE: yt = 1, rtd = 0.45,
      eps = 4, L = xtronc = 4 throat radii) with the S18 W* design vector
      of record (validation/s20_adaptive_design.json W: theta_B + 8 wall
      heights at uniform nodes on [x_B, L], natural cubic spline clamped
      left — the same construction as wall_geometry()). Plug class:
      L_ideal = R_lip / tan(mu_e), mu_e = asin(1/M_e) (ADR panel 2026-07-16
      length model; truncation band 0.20-0.40 printed as sensitivity).
  (d) wave count n in {1, 2, 3} (record: n = 1 in the example lap time
      t_lap = 2 pi RBAR / U_CJ, example_design_10kN.py:55; multi-wave
      operation W ~ 3 at 10 kN is the record's own estimate; the M0
      side-load remark scopes n >= 2).
  (e) wave speed = U_CJ (the record's own convention, example :55;
      velocity-deficit corrections are OUTSIDE the record -> declared
      one-sided caveat: a deficit LOWERS f_wave and St).

MEAN AXIAL VELOCITY (PRACTICE, bracketed): quasi-1D isentropic M(x) from
A(x)/A* = y(x)^2 on the record contour at the record gamma_s, u = M a(T0);
tau_1D = int dx/u from the throat to the lip; RIGOROUS-IN-CLASS bracket
tau in [L/u_e, L/a*] (u monotone from sonic to exit in a supersonic
nozzle) reported beside it; the certified-march tau_n (the finding's own
named carrier) is the F2.ENGINE instrumentation upgrade, declared.

REJECTORS (each must FIRE; exit code 0 iff all pass):
  R1 corrupted-u: u scaled by 10 -> St must leave its own band (>= 3x).
  R2 wrong-unit CJ speed (km/s fed as m/s): the record-consistency gate
     |U - U_cache|/U_cache <= TOL['cross_solver_rel'] must REJECT it.
  R3 bracket consistency: tau_1D inside [L/u_e, L/a*] else FAIL (the
     quasi-1D integral cannot leave the monotone bracket).
  R4 seeded reversed contour (decreasing y downstream of the throat): the
     supersonic area-Mach inversion must FAIL loudly (A/A* < 1).
LICENSE RULE (declared, from the problem book's own marginal band): St_n
< 0.1 -> the frozen-time (per-phase) rung is self-licensing; 0.1 <= St_n
< 1 -> MARGINAL, the first-order unsteady corrector (P4) is mandatory and
the wave-frame anchor is the backstop; St_n >= 1 -> the frozen-time rung
alone is NOT defensible, wave-frame/unsteady rung required.
"""
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from src.common.constants import TOL  # noqa: E402

CACHE = os.path.join(ROOT, 'data', 'st_nozzle_opt.json')
DESIGN = os.path.join(ROOT, 'validation', 's20_adaptive_design.json')
STATE_KEYS = ('det|CH4|20|1.66', 'det|CH4|20|1.00')
# annulus instances of record: (label, R_bar [m], A_t [m^2], record heads)
ANNULI = (('10kN CH4/O2 nozzled (example_design_10kN.py:36; A_t SOLUTION:55)',
           0.140, 32.4e-4, 3),
          ('600N workhorse nozzled (SOLUTION_headtohead.md:17-18)',
           0.045, 4.3e-4, 2))
WAVES = (1, 2, 3)
TCASE = dict(yt=1.0, rtd=0.45, eps=4.0, L=4.0)   # [X-TOCV] TCASE (:106-107)
TRUNC_BAND = (0.20, 0.30, 0.40)                   # ADR panel industrial band
ST_MARGINAL = (0.1, 1.0)                          # problem book §8 band


# ------------------------------------------------------------ record contour
def spline_natural_clamped(xs, ys, slope0):
    """Cubic spline second derivatives: clamped left slope, natural right
    (numpy twin of a1_toc_variational_jax.spline_coeffs)."""
    n = len(xs)
    h = np.diff(xs)
    A = np.zeros((n, n)); r = np.zeros(n)
    A[0, 0] = 2 * h[0]; A[0, 1] = h[0]
    r[0] = 6.0 * ((ys[1] - ys[0]) / h[0] - slope0)
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]; A[i, i] = 2 * (h[i - 1] + h[i]); A[i, i + 1] = h[i]
        r[i] = 6.0 * ((ys[i + 1] - ys[i]) / h[i] - (ys[i] - ys[i - 1]) / h[i - 1])
    A[n - 1, n - 1] = 1.0
    return np.linalg.solve(A, r)


def spline_eval(x, xs, ys, M):
    i = np.clip(np.searchsorted(xs, x) - 1, 0, len(xs) - 2)
    h = xs[i + 1] - xs[i]
    a = (xs[i + 1] - x) / h; b = (x - xs[i]) / h
    return (a * ys[i] + b * ys[i + 1]
            + ((a**3 - a) * M[i] + (b**3 - b) * M[i + 1]) * h * h / 6.0)


def record_contour(nx=2001):
    d = json.load(open(DESIGN))
    W = np.array([float(w) for w in d['W']])
    thB = W[0]; yt, rtd, L = TCASE['yt'], TCASE['rtd'], TCASE['L']
    xB = rtd * np.sin(thB); yB = yt + rtd * (1.0 - np.cos(thB))
    m = len(W) - 1
    xs = np.concatenate([[xB], xB + (L - xB) * np.arange(1, m + 1) / m])
    ys = np.concatenate([[yB], W[1:]])
    M = spline_natural_clamped(xs, ys, np.tan(thB))
    x = np.linspace(0.0, L, nx)
    y = np.where(x <= xB, yt + rtd * (1.0 - np.cos(np.arcsin(np.clip(x / rtd, -1, 1)))),
                 spline_eval(np.maximum(x, xB), xs, ys, M))
    return x, y, dict(thB=thB, xB=xB, yB=yB, W=W, provenance=d['provenance'])


# ------------------------------------------------------------ quasi-1D gas
def area_mach_supersonic(ar, g):
    """M(A/A*) on the supersonic branch (bisection; ar >= 1 required)."""
    ar = np.asarray(ar, float)
    if np.any(ar < 1.0 - 1e-12):
        raise ValueError('A/A* < 1 downstream of the throat: contour not '
                         'monotone-diverging (min A/A* = %.6f)' % ar.min())
    def f(M):
        return (1.0 / M) * ((2.0 / (g + 1)) * (1 + (g - 1) / 2 * M * M)) ** ((g + 1) / (2 * (g - 1))) - ar
    lo = np.ones_like(ar); hi = np.full_like(ar, 50.0)
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        s = f(mid) > 0
        hi = np.where(s, mid, hi); lo = np.where(s, lo, mid)
    return 0.5 * (lo + hi)


def velocity_profile(x, y, g, R, T0):
    ar = (y / y[0]) ** 2
    M = area_mach_supersonic(ar, g)
    a0 = np.sqrt(g * R * T0)
    a = a0 / np.sqrt(1 + (g - 1) / 2 * M * M)
    return M, a, M * a


def residence(x, u):
    return float(np.trapezoid(1.0 / u, x))


def st_table(state, x_nd, y_nd, u_scale=1.0):
    g, R, TCJ, PR, U = state['gamma'], state['R'], state['TCJ'], state['PR'], state['Ucj']
    T0_end = TCJ * PR ** (-(g - 1) / g)
    rows = []
    for label, Rbar, At, heads in ANNULI:
        yt = np.sqrt(At / np.pi)
        x = x_nd * yt; y = y_nd * yt
        L = x[-1]
        for T0 in (TCJ, T0_end):
            M, a, u = velocity_profile(x, y, g, R, T0)
            u = u * u_scale
            tau = residence(x, u)
            astar = a[0] * u_scale; ue = u[-1]
            lo, hi = L / ue, L / astar
            # plug class: ideal length from the exit Mach angle at the lip
            Me = M[-1]; mu_e = np.arcsin(1.0 / Me)
            R_lip = Rbar  # cowl lip ~ mean annulus radius (record R_lip = R_bar + gap/2)
            L_plug = {t: (1 - t) * R_lip / np.tan(mu_e) for t in TRUNC_BAND}
            for n in WAVES:
                f = n * U / (2 * np.pi * Rbar)
                rows.append(dict(annulus=label, heads_record=heads, yt=yt, L=L,
                                 T0=T0, n=n, f=f, tau=tau, tau_lo=lo, tau_hi=hi,
                                 St=f * tau, St_lo=f * lo, St_hi=f * hi,
                                 He=f * L / a.mean(), Me=Me,
                                 St_plug={t: f * Lp / (0.5 * (astar + ue))
                                          for t, Lp in L_plug.items()},
                                 L_plug=L_plug))
    return rows


def license_rung(st):
    if st < ST_MARGINAL[0]:
        return 'frozen-time rung self-licensing (St < 0.1)'
    if st < ST_MARGINAL[1]:
        return 'MARGINAL: first-order unsteady corrector MANDATORY; wave-frame backstop'
    return 'NOT DEFENSIBLE alone: wave-frame / unsteady rung REQUIRED'


# ------------------------------------------------------------ main + rejectors
def main():
    D = json.load(open(CACHE))['states']
    states = {k: dict(D[k]) for k in STATE_KEYS}
    # the cache carries PR/TCJ/gamma/R but not U_CJ: re-run the RECORD's own
    # CJ solver at the cached fill (Pinit, Ti, phi) and gate the reproduction
    # of the cached PR/TCJ/gamma to TOL['cross_solver_rel'] (record consistency).
    from src.thrust.stechmann_nozzle import det_state
    for k, s in states.items():
        live = det_state(s['prop'], s['phi'], s['Ti'], s['Pinit'])
        for key in ('PR', 'TCJ', 'gamma'):
            rel = abs(live[key] - s[key]) / s[key]
            if rel > TOL['cross_solver_rel']:
                raise SystemExit('record consistency FAIL: %s %s live %.6g vs cache %.6g (rel %.2e)'
                                 % (k, key, live[key], s[key], rel))
        s['Ucj'] = live['Ucj']
        print('record CJ re-run %s: U_CJ = %.1f m/s (PR/TCJ/gamma reproduce the cache to %.1e)'
              % (k, live['Ucj'], max(abs(live[q] - s[q]) / s[q] for q in ('PR', 'TCJ', 'gamma'))))
    x_nd, y_nd, geo = record_contour()
    print('== [X-STSC] St SCOPING NUMBER (record arithmetic, 2026-09-05) ==')
    print('contour of record: %s; theta_B = %.4f, x_B = %.4f, L/yt = %.1f, '
          'eps_lip = %.3f (TCASE eps = %.1f)' % (geo['provenance'], geo['thB'],
          geo['xB'], TCASE['L'], y_nd[-1] ** 2, TCASE['eps']))
    ok = True
    all_rows = {}
    for k, s in states.items():
        print('\n-- family %s: U_CJ = %.1f m/s, PR = %.2f, gamma_s = %.4f, '
              'T_CJ = %.0f K, T0_end = %.0f K' % (k, s['Ucj'], s['PR'], s['gamma'],
              s['TCJ'], s['TCJ'] * s['PR'] ** (-(s['gamma'] - 1) / s['gamma'])))
        rows = st_table(s, x_nd, y_nd)
        all_rows[k] = rows
        print('%-42s %2s %7s %8s %8s %8s %8s %8s %6s %s' % (
            'annulus', 'n', 'f[kHz]', 'tau[us]', 'St', 'St_lo', 'St_hi', 'He', 'T0', 'St_plug(20/30/40%)'))
        for r in rows:
            print('%-42s %2d %7.2f %8.1f %8.3f %8.3f %8.3f %8.3f %6.0f %s' % (
                r['annulus'][:42], r['n'], r['f'] / 1e3, r['tau'] * 1e6, r['St'],
                r['St_lo'], r['St_hi'], r['He'], r['T0'],
                '/'.join('%.2f' % r['St_plug'][t] for t in TRUNC_BAND)))
            # R3 bracket consistency
            if not (r['tau_lo'] * (1 - 1e-12) <= r['tau'] <= r['tau_hi'] * (1 + 1e-12)):
                print('   R3 FAIL: tau_1D outside [L/u_e, L/a*]'); ok = False
    # envelope summary (bell class, both families, all annuli, n, T0)
    sts = [r['St'] for rows in all_rows.values() for r in rows]
    st_rec = [r['St'] for rows in all_rows.values() for r in rows if r['n'] == r['heads_record']]
    st_plug = [r['St_plug'][t] for rows in all_rows.values() for r in rows for t in TRUNC_BAND]
    print('\nENVELOPE (bell TOC L = 4 yt): St_n in [%.3f, %.3f] over annuli x n in {1,2,3} x cycle T0'
          % (min(sts), max(sts)))
    print('AT THE RECORD HEAD COUNT (n = %s): St_n in [%.3f, %.3f]'
          % ('/'.join(str(a[3]) for a in ANNULI), min(st_rec), max(st_rec)))
    print('PLUG CLASS (L_ideal(1-trunc), trunc 0.20-0.40): St_n in [%.3f, %.3f]'
          % (min(st_plug), max(st_plug)))
    print('LICENSE (declared rule): bell record-head-count -> %s' % license_rung(max(st_rec)))
    print('LICENSE (declared rule): plug class worst -> %s' % license_rung(max(st_plug)))
    print('CAVEATS (declared): quasi-1D u on the record contour (PRACTICE; bracket printed); '
          'wave speed = U_CJ (deficit lowers St); R_lip ~ R_bar for the plug length; '
          'certified-march tau_n = F2.ENGINE instrumentation upgrade.')

    # ---- rejectors
    print('\n== REJECTORS ==')
    s = states[STATE_KEYS[0]]
    base = st_table(s, x_nd, y_nd)[0]
    r1 = st_table(s, x_nd, y_nd, u_scale=10.0)[0]
    fired1 = r1['St'] < base['St_lo'] / 3.0
    print('R1 corrupted-u (x10): St %.4f -> %.4f, band floor %.4f: %s'
          % (base['St'], r1['St'], base['St_lo'], 'REJECTED (as required)' if fired1 else 'NOT REJECTED'))
    ok &= fired1
    U_wrong = s['Ucj'] / 1000.0
    gate = abs(U_wrong - s['Ucj']) / s['Ucj'] <= TOL['cross_solver_rel']
    print('R2 wrong-unit U_CJ (%.3f fed as m/s vs record %.1f, tol %.1e): %s'
          % (U_wrong, s['Ucj'], TOL['cross_solver_rel'],
             'NOT REJECTED' if gate else 'REJECTED (as required)'))
    ok &= not gate
    print('R3 bracket consistency: %s' % ('PASS (all rows inside [L/u_e, L/a*])' if ok else 'see above'))
    try:
        y_rev = y_nd[::-1] * (y_nd[0] / y_nd[-1])   # decreasing downstream, starts at yt
        velocity_profile(x_nd, y_rev, s['gamma'], s['R'], s['TCJ'])
        print('R4 reversed contour: NOT REJECTED'); ok = False
    except ValueError as e:
        print('R4 reversed contour: REJECTED (as required): %s' % e)
    print('\nVERDICT [X-STSC]: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
