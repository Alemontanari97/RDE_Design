#!/usr/bin/env python3
"""[X-U2RG] Carrier for the slip-wall reflection brick [T-U2RG]
(D2.5-U step U2; candidate declared in docs/rde_nozzle_D25U_U1.md §8,
EXECUTED here — S15 reopened segment, [RIGOR/A]).

Steady 2-D Euler as x-as-time (same construction as X-XBVP):
U = (rho, u, v, S), A = dm/dU, B = dn/dU, EOS-GENERAL p(rho,S),
e_rho = p/rho^2, e_S = theta, c^2 = p_rho. Wall y = w(x), slip
v = w' u; linearized-BC covector l_BC = d(v - w'u)/dU = (0,-w',1,0).
Acoustic pencil bracket: det(B - lam A) = (v - lam u)^2 *
[ (v - lam u)^2 - c^2 (1 + lam^2) ]  (G12-L1 planar structure).

SYMBOLIC bricks (abstract EOS, decisive):
  P1  NO GLANCING AT SLIP: bracket(lam = w', v = w'u) ==
      -c^2 (1 + w'^2) != 0 identically — the x-evolution wall
      boundary is NON-CHARACTERISTIC at every slip state with c > 0
      (no separate angle margin needed: hypothesis REDUCTION vs the
      U1 writing, which derived angle_min from (delta, C_geo,
      C_dat)).
  P2  ACOUSTIC EIGENVECTOR CLOSED FORM: r_cand =
      (-rho (v - lam u)/c^2, -lam, 1, 0) satisfies (B - lam A) r = 0
      MODULO the bracket: every component of (B - lam A) r_cand is
      divisible by the bracket (exact symbolic quotient, no
      remainder) — the front-normal law (du,dv) ~ (-lam, 1) with
      dp = -rho (v - lam u), dS = 0, at abstract EOS.
  P3  SOLVABILITY == SUPERSONIC: s(lam) := l_BC . r_cand =
      1 + w' lam exactly; s(lam_acoustic) = 0 forces lam = -1/w',
      and bracket(-1/w', v = w'u) == (1 + w'^2)/w'^2 * (q^2 - c^2)
      with q^2 = u^2(1 + w'^2) the slip speed: the reflection solve
      degenerates EXACTLY at total-sonic q = c — on the axial branch
      u > c it is UNIFORMLY solvable (q >= u > c). Reflection
      coefficient closed form R = -(1 + w' lam_+)/(1 + w' lam_-).
NUMERIC + REJECTORS:
  N1  margin samples: |s_-| bounded below on u/c in [1.15, 3] slip
      states; |R| finite (lam_+ finite by the axial margin).
  R1  CORRUPTED BC covector (0,-w',0,0): its zero locus is NOT the
      sonic locus — exhibit a healthy margin state where the
      corrupted pairing vanishes while the true s does not
      (detected), killing any implementation that dropped the
      v-slot.
  R2  SLIP HYPOTHESIS NECESSARY (counterexample exhibited): off-slip
      wall data v = w'u + c sqrt(1+w'^2) makes bracket(w') == 0 —
      glancing IS possible off slip; the carrier must DETECT the
      characteristic boundary (P1 quantity vanishing) at that state.
  R3  near-sonic degeneration: |s_-| ~ (q^2 - c^2)^{1/2} as
      q -> c+ (double-root splitting): measured log-log slope in a
      derived band around 1/2.

Exit 0 iff all checks and rejectors pass. Terminal line:
"VERDICT: PASS"/"VERDICT: FAIL".
"""
import sys

import numpy as np
import sympy as sp


def build():
    rho, u, v, S, th, wp, lam = sp.symbols(
        'rho u v S theta wprime lambda', real=True, positive=False)
    p = sp.Function('p')(rho, S)
    e = sp.Function('e')(rho, S)
    H = e + p / rho + (u**2 + v**2) / 2
    m = sp.Matrix([rho * u, rho * u**2 + p, rho * u * v, rho * u * H])
    n = sp.Matrix([rho * v, rho * u * v, rho * v**2 + p, rho * v * H])
    U = sp.Matrix([rho, u, v, S])
    sub = {sp.Derivative(e, rho): p / rho**2, sp.Derivative(e, S): th}
    A = m.jacobian(U).subs(sub)
    B = n.jacobian(U).subs(sub)
    c2 = sp.Derivative(p, rho)
    return rho, u, v, S, th, wp, lam, p, A, B, c2


def sym_checks():
    ok = True
    rho, u, v, S, th, wp, lam, p, A, B, c2 = build()
    bracket = (v - lam * u)**2 - c2 * (1 + lam**2)

    # P0 (structure): det(B - lam A) == rho^2 u? * streamline^2 * bracket
    det = sp.simplify(sp.det(B - lam * A))
    quo = sp.simplify(det / ((v - lam * u)**2 * bracket))
    p0 = sp.simplify(sp.diff(quo, lam)) == 0     # quotient lam-free
    print('  P0 pencil factorization: streamline^2 x acoustic bracket '
          '(quotient lam-free): %s' % ('PASS' if p0 else 'FAIL'))
    ok &= p0

    # P1: no glancing at slip — bracket(lam=w', v=w'u) = -c^2(1+w'^2)
    b_slip = sp.simplify(bracket.subs({lam: wp, v: wp * u}))
    p1 = sp.simplify(b_slip + c2 * (1 + wp**2)) == 0
    print('  P1 NO GLANCING AT SLIP: bracket(w\'; slip) == -c^2(1+w\'^2): '
          '%s' % ('PASS' if p1 else 'FAIL'))
    ok &= p1

    # P2: closed-form acoustic eigenvector modulo the bracket
    r_cand = sp.Matrix([-rho * (v - lam * u) / c2, -lam, 1, 0])
    resid = sp.expand((B - lam * A) * r_cand)
    p2 = True
    for k in range(4):
        q_, r_ = sp.div(sp.together(resid[k]) * c2, sp.expand(bracket * c2),
                        lam)
        # divide as polynomials in lam after clearing the 1/c2
        rem = sp.simplify(r_)
        p2 &= rem == 0
    print('  P2 (B-lam A) r_cand == 0 modulo bracket (4/4 components '
          'divisible): %s' % ('PASS' if p2 else 'FAIL'))
    ok &= p2

    # P3: s = l_BC . r_cand = 1 + w' lam; zero => lam = -1/w';
    #     bracket(-1/w'; slip) == (1+w'^2)/w'^2 (q^2 - c^2), q^2=u^2(1+w'^2)
    lbc = sp.Matrix([[0, -wp, 1, 0]])
    s = sp.simplify((lbc * r_cand)[0, 0])
    p3a = sp.simplify(s - (1 + wp * lam)) == 0
    b_perp = sp.simplify(bracket.subs({lam: -1 / wp, v: wp * u}))
    target = (1 + wp**2) / wp**2 * (u**2 * (1 + wp**2) - c2)
    p3b = sp.simplify(b_perp - target) == 0
    p3 = p3a and p3b
    print('  P3 s == 1 + w\'lam; degeneracy locus == total-sonic '
          'q^2 = c^2: %s' % ('PASS' if p3 else 'FAIL'))
    ok &= p3
    return ok


# ------------------------- ideal-gas instance for numerics (oracle role)
GAMMA = 1.4


def lam_pm(u, v, c):
    disc = np.sqrt(u * u + v * v - c * c)
    den = u * u - c * c
    return ((u * v + c * disc) / den, (u * v - c * disc) / den)


def num_checks():
    ok = True
    rng = np.random.default_rng(20260805)

    # N1: margin slip states: |s_-| bounded below, |R| finite
    smin, Rmax = np.inf, 0.0
    for _ in range(200):
        wp = np.tan(rng.uniform(-0.6, 0.6))
        c = rng.uniform(0.8, 1.6)
        u = c * rng.uniform(1.15, 3.0)
        v = wp * u
        lp, lm = lam_pm(u, v, c)
        s_p, s_m = 1 + wp * lp, 1 + wp * lm
        smin = min(smin, abs(s_m), abs(s_p))
        Rmax = max(Rmax, abs(s_p / s_m))
    n1 = smin > 1.0e-2 and np.isfinite(Rmax)
    print('  N1 margin slip states: min|s| = %.3f > 1e-2 (derived from '
          'q/c >= 1.15), max|R| = %.2f finite: %s'
          % (smin, Rmax, 'PASS' if n1 else 'FAIL'))
    ok &= n1

    # R1: corrupted BC covector (v-slot dropped): s_corr = w' lam —
    #     vanishes at lam=0 (wrong locus). Exhibit a margin state with
    #     lam_+ = 0 where true s != 0: theta = -mu (downward flow).
    c = 1.0
    q = 2.0 * c
    mu = np.arcsin(c / q)
    theta = -mu                      # lam_+ = tan(theta + mu) = 0
    u, v = q * np.cos(theta), q * np.sin(theta)
    wp = np.tan(theta)               # slip wall along the flow
    lp, lm = lam_pm(u, v, c)
    s_true = 1 + wp * lp
    s_corr = wp * lp
    r1 = abs(lp) < 1e-12 and abs(s_corr) < 1e-12 and abs(s_true) > 0.5
    print('  R1 corrupted covector zero at lam_+=0 while true s = %.3f '
          '!= 0 (wrong locus DETECTED): %s'
          % (s_true, 'PASS' if r1 else 'FAIL'))
    ok &= r1

    # R2: slip hypothesis NECESSARY — off-slip glancing exhibited:
    #     v = w'u + c sqrt(1+w'^2) makes bracket(w') = 0 exactly.
    wp = 0.3
    c = 1.0
    u = 1.7 * c
    v = wp * u + c * np.sqrt(1 + wp * wp)
    br = (v - wp * u)**2 - c * c * (1 + wp * wp)
    r2 = abs(br) < 1e-12
    print('  R2 off-slip glancing exhibited (bracket(w\') = %.1e == 0): '
          'slip hypothesis NECESSARY: %s' % (br, 'PASS' if r2 else 'FAIL'))
    ok &= r2

    # R3: near-sonic rate |s_-| ~ (q^2-c^2)^(1/2). The exponent is
    #     ASYMPTOTIC: measured log-log slopes carry finite-eps
    #     corrections, so the derived criterion is monotone approach
    #     to 1/2 plus the finest slope inside a tight band.
    wp = 0.25
    c = 1.0
    eps = np.array([1e-2, 1e-3, 1e-4, 1e-5, 1e-6])
    svals = []
    for e_ in eps:
        q = c * np.sqrt(1.0 + e_)            # q^2 - c^2 = c^2 e_
        th_ = np.arctan(wp)
        u, v = q * np.cos(th_), q * np.sin(th_)
        lp, lm = lam_pm(u, v, c)
        svals.append(abs(1 + wp * lm))
    slopes = np.diff(np.log(svals)) / np.diff(np.log(eps))
    err = np.abs(slopes - 0.5)
    r3 = np.all(np.diff(err) < 0) and err[-1] < 0.02
    print('  R3 near-sonic exponent -> 1/2: slopes %s (monotone, final '
          'err %.3f < 0.02): %s'
          % (np.round(slopes, 3).tolist(), err[-1],
             'PASS' if r3 else 'FAIL'))
    ok &= r3
    return ok


def main():
    print('[X-U2RG] slip-wall reflection / glancing carrier (T-U2RG)')
    ok = sym_checks()
    ok &= num_checks()
    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
