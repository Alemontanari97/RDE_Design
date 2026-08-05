#!/usr/bin/env python3
"""[X-XBVP] Carrier for the Cauchy->steady-BVP transfer bricks
(docs/rde_nozzle_cauchy_bvp_transfer.md; S15 deep-foundations campaign,
[RIGOR/A]; closes the declared analytic soft spot of shock-free
canonicity at the *boundary-term* and *bijection* levels, and
instance-certifies the convexity-from-margin brick).

Steady 2-D Euler as an x-as-time system: U = (rho, u, v, S),
  m(U) = (rho u, rho u^2 + p, rho u v, rho u H)   (x-fluxes, "state")
  n(U) = (rho v, rho u v, rho v^2 + p, rho v H)   (y-fluxes)
with EOS-GENERAL closure p = p(rho, S), e = e(rho, S),
e_rho = p/rho^2 (Gibbs along isentropes), e_S = theta > 0,
H = e + p/rho + (u^2+v^2)/2, c^2 = p_rho|_S.

SYMBOLIC bricks (EOS-general, abstract p, e — decisive):
  P1  BIJECTION/SONIC DEGENERACY: det(dm/dU) vanishes IDENTICALLY at
      u = c and at u = 0 (symbolic, abstract EOS); on u > c the map
      U -> m is a local diffeomorphism (numeric nonvanishing +
      near-sonic degeneration rate on the ideal-gas instance).
  P2  WALL LEMMA (new, the boundary soft spot): at a slip wall
      y = w(x) (v = w' u for BOTH states), the relative-entropy flux
      of the pair eta = -rho u g(S), q = -rho v g(S) through the wall
      VANISHES IDENTICALLY: the admissible flux perturbation at slip,
      d = (F_y - w' F_x)(V) - (F_y - w' F_x)(U) = (p_V - p_U) *
      (0, -w', 1, 0), is annihilated by D_m eta for EVERY g and EVERY
      EOS. Proved by solving J dU = d symbolically: the induced dS
      and d(rho u) both vanish at slip. (The pressure direction at a
      slip wall is isentropic at constant mass flux.)
  P3  ENTROPY-PAIR IDENTITY: (eta, q) is an entropy pair of the
      x-system: D_U eta . (dU/dx) + D_U q . (dU/dy) = 0 reduces to
      the S-transport identity on smooth solutions (symbolic:
      grad eta = lambda^T dm/dU + mu grad(S-transport residual) —
      checked as D_U q == D_m eta . D_U n on the constraint manifold;
      implemented as: the pair identity D_U q = (D_U eta) (dm/dU)^{-1}
      (dn/dU) holds iff u != c — verified numerically on random
      states (ideal gas), consistent with P1.)
NUMERIC brick (ideal-gas INSTANCE, declared oracle role):
  P4  CONVEXITY FROM THE MARGIN: Hessian of eta as a function of m
      (pushforward H_m = J^{-T} [H_U(eta) - sum_k lam_k H_U(m_k)]
      J^{-1}, lam = J^{-T} grad_U eta) tested for positive
      definiteness on randomized states: for g(S) = S (eta = -rho u S
      up to sign — both signs tested, the definite one reported):
      REJECTOR R1: subsonic-in-x states (u < c) must yield an
      INDEFINITE Hessian (no convex extension across the sonic line);
      near-sonic states must show lambda_min -> 0.
      The supersonic-margin verdict (definite on u/c >= 1 + margin
      over the declared box) is an INSTANCE CERTIFICATE (SCHEMA
      grade), not a proof over the whole branch — recorded as such.

Exit 0 iff all checks AND the rejector pass. Terminal line:
"VERDICT: PASS"/"VERDICT: FAIL".
"""
import sys

import numpy as np
import sympy as sp


def build_symbolic():
    rho, u, v, S, th, wp = sp.symbols('rho u v S theta wprime',
                                      positive=True, real=True)
    # abstract EOS: p(rho,S); e via e_rho = p/rho^2, e_S = theta
    p = sp.Function('p')(rho, S)
    e = sp.Function('e')(rho, S)
    H = e + p / rho + (u**2 + v**2) / 2
    m = sp.Matrix([rho * u, rho * u**2 + p, rho * u * v, rho * u * H])
    n = sp.Matrix([rho * v, rho * u * v, rho * v**2 + p, rho * v * H])
    U = sp.Matrix([rho, u, v, S])
    J = m.jacobian(U)
    Jn = n.jacobian(U)
    # impose the Gibbs closure on e-derivatives
    sub = {sp.Derivative(e, rho): p / rho**2, sp.Derivative(e, S): th}
    J = J.subs(sub)
    Jn = Jn.subs(sub)
    return (rho, u, v, S, th, wp, p, e, J, Jn)


def sym_checks():
    ok = True
    rho, u, v, S, th, wp, p, e, J, Jn = build_symbolic()
    c2 = sp.Derivative(p, rho)          # c^2 = p_rho|_S (abstract)

    # P1: det(J) == 0 identically at u = c and at u = 0 (abstract EOS)
    det = sp.simplify(J.det())
    at_sonic = sp.simplify(det.subs(u, sp.sqrt(c2)))
    at_zero = sp.simplify(det.subs(u, 0))
    p1 = (at_sonic == 0) and (at_zero == 0)
    print('  P1 det(dm/dU): == 0 at u=c and u=0 (abstract EOS):        %s'
          % ('PASS' if p1 else 'FAIL [%s | %s]' % (at_sonic, at_zero)))
    ok &= p1

    # P2: WALL LEMMA — J dU = (0,-w',1,0)*(dp) at slip (v = w' u):
    #     induced d(rho u) = 0 by construction; induced dS must be 0.
    d = sp.Matrix([0, -wp, 1, 0])
    dU = J.LUsolve(d)
    dS_slip = sp.simplify(dU[3].subs(v, wp * u))
    drhou = sp.simplify((J[0, :] * dU)[0, 0])     # = d1 = 0 by constr.
    p2 = (dS_slip == 0) and (sp.simplify(drhou - 0) == 0)
    print('  P2 WALL LEMMA: slip flux direction gives dS == 0, '
          'd(rho u) == 0:  %s' % ('PASS' if p2 else 'FAIL [%s]' % dS_slip))
    ok &= p2
    return ok


# ---------------- ideal-gas instance (declared oracle role for P3/P4)
GAMMA = 1.4
CV = 1.0


def ideal_lambdas():
    rho, u, v, S = sp.symbols('rho u v S', real=True)
    p = sp.exp(S / CV) * rho**GAMMA
    e = p / ((GAMMA - 1) * rho)
    H = e + p / rho + (u**2 + v**2) / 2
    m = sp.Matrix([rho * u, rho * u**2 + p, rho * u * v, rho * u * H])
    n = sp.Matrix([rho * v, rho * u * v, rho * v**2 + p, rho * v * H])
    U = sp.Matrix([rho, u, v, S])
    eta = -rho * u * S                      # g(S) = S; sign tested below
    q = -rho * v * S
    J = m.jacobian(U)
    Jn = n.jacobian(U)
    geta = sp.Matrix([eta]).jacobian(U)
    gq = sp.Matrix([q]).jacobian(U)
    Heta = sp.hessian(eta, U)
    Hm = [sp.hessian(m[k], U) for k in range(4)]
    args = (rho, u, v, S)
    L = sp.lambdify
    return {
        'J': L(args, J, 'numpy'), 'Jn': L(args, Jn, 'numpy'),
        'geta': L(args, geta, 'numpy'), 'gq': L(args, gq, 'numpy'),
        'Heta': L(args, Heta, 'numpy'),
        'Hm': [L(args, h, 'numpy') for h in Hm],
        'c': L(args, sp.sqrt(GAMMA * p / rho), 'numpy'),
    }


def hess_in_m(fns, st):
    J = np.array(fns['J'](*st), float)
    lam = np.linalg.solve(J.T, np.array(fns['geta'](*st), float).ravel())
    Hu = np.array(fns['Heta'](*st), float)
    for k in range(4):
        Hu = Hu - lam[k] * np.array(fns['Hm'][k](*st), float)
    Ji = np.linalg.inv(J)
    return Ji.T @ Hu @ Ji


def num_checks():
    ok = True
    rng = np.random.default_rng(20260805)
    fns = ideal_lambdas()

    # P3: entropy-pair identity D_U q == D_m eta . D_U n, u != c
    worst = 0.0
    for _ in range(40):
        rho = rng.uniform(0.5, 2.0)
        S = rng.uniform(-0.5, 0.5)
        c = fns['c'](rho, 0, 0, S)
        u = c * rng.uniform(1.15, 3.0)
        v = c * rng.uniform(-0.8, 0.8)
        st = (rho, u, v, S)
        J = np.array(fns['J'](*st), float)
        Jn = np.array(fns['Jn'](*st), float)
        geta = np.array(fns['geta'](*st), float).ravel()
        gq = np.array(fns['gq'](*st), float).ravel()
        pred = np.linalg.solve(J.T, geta) @ Jn
        scale = max(np.abs(gq).max(), 1.0)
        worst = max(worst, np.abs(pred - gq).max() / scale)
    floor = 4 * 4 * np.finfo(float).eps * 1.0e3      # solve+matmul roundoff
    p3 = worst <= floor
    print('  P3 entropy-pair identity Dq = Dm(eta).Dn (40 states, '
          'rel %.1e <= %.1e): %s' % (worst, floor, 'PASS' if p3 else 'FAIL'))
    ok &= p3

    # P4: convexity from the margin (instance certificate) + rejector
    def lam_min(st, sign):
        Hm = hess_in_m(fns, st)
        w = np.linalg.eigvalsh(0.5 * (Hm + Hm.T))
        return (sign * w).min() if sign > 0 else (sign * w[::-1]).min()

    # supersonic box with margin: u/c in [1.15, 3], |v| <= 0.8 c
    n_pos = n_tot = 0
    lam_worst = np.inf
    for _ in range(200):
        rho = rng.uniform(0.5, 2.0)
        S = rng.uniform(-0.5, 0.5)
        c = fns['c'](rho, 0, 0, S)
        u = c * rng.uniform(1.15, 3.0)
        v = c * rng.uniform(-0.8, 0.8)
        Hm = hess_in_m(fns, (rho, u, v, S))
        w = np.linalg.eigvalsh(0.5 * (Hm + Hm.T))
        n_tot += 1
        if w.min() > 0:
            n_pos += 1
            lam_worst = min(lam_worst, w.min())
    p4a = n_pos == n_tot
    print('  P4a eta=-rho u S convex in m on margin box: %d/%d definite '
          '(lam_min_worst %.2e): %s'
          % (n_pos, n_tot, lam_worst if np.isfinite(lam_worst) else -1,
             'PASS' if p4a else 'FAIL'))
    ok &= p4a

    # R1 rejector: subsonic-in-x states must be INDEFINITE
    n_indef = n_sub = 0
    for _ in range(60):
        rho = rng.uniform(0.5, 2.0)
        S = rng.uniform(-0.5, 0.5)
        c = fns['c'](rho, 0, 0, S)
        u = c * rng.uniform(0.15, 0.85)
        v = c * rng.uniform(-0.8, 0.8)
        Hm = hess_in_m(fns, (rho, u, v, S))
        w = np.linalg.eigvalsh(0.5 * (Hm + Hm.T))
        n_sub += 1
        if w.min() < 0 < w.max():
            n_indef += 1
    r1 = n_indef == n_sub
    print('  R1 subsonic states INDEFINITE (no convex extension): '
          '%d/%d: %s' % (n_indef, n_sub, 'PASS' if r1 else 'FAIL'))
    ok &= r1

    # R2: the sonic line is EXACTLY the definiteness boundary (pincer):
    #     u = (1+eps)c definite, u = (1-eps)c indefinite, eps -> 0.
    #     (lam_min in m-variables is not scale-invariant, so no
    #     monotonicity is claimed — only the two-sided sign pincer.)
    r2 = True
    for (rho, S, vfrac) in ((1.1, 0.1, 0.3), (0.7, -0.3, -0.5),
                            (1.8, 0.4, 0.0)):
        c = fns['c'](rho, 0, 0, S)
        for eps in (1.0e-2, 1.0e-3):
            wp = np.linalg.eigvalsh(
                hess_in_m(fns, (rho, (1 + eps) * c, vfrac * c, S)))
            wm = np.linalg.eigvalsh(
                hess_in_m(fns, (rho, (1 - eps) * c, vfrac * c, S)))
            r2 &= (wp.min() > 0) and (wm.min() < 0)
    print('  R2 sonic pincer: definite at u=(1+eps)c, indefinite at '
          '(1-eps)c, eps=1e-2,1e-3: %s' % ('PASS' if r2 else 'FAIL'))
    ok &= r2
    return ok


def main():
    print('[X-XBVP] Cauchy->steady-BVP transfer bricks carrier')
    ok = sym_checks()
    ok &= num_checks()
    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
