#!/usr/bin/env python3
"""N6 attack carrier [F1/N6-S1, rigor session 8 reopened]: machine
verification of the swirl structure lemmas of docs/rde_nozzle_N6_swirl.md.

Part A (SYMBOLIC, EOS-general: c^2 free): axisymmetric steady Euler
WITH SWIRL, V = (rho, u, v, w, p) in (x, r):
  (A1) det A_p = u^3 (u^2 - c^2): x-marching invertible under axial
       supersonicity — the G12-S1 evolution reading EXTENDS to swirl.
  (A2) pencil factorization det(B_p - lambda A_p) =
       (v - lambda u)^3 [ (v - lambda u)^2 - c^2 (1 + lambda^2) ]:
       characteristics = streamline (TRIPLE: entropy, h0, and the
       swirl invariant Gamma = r w) + the SAME MERIDIONAL Mach lines
       as the swirl-free case. Swirl enters fluxes only via transport;
       centrifugal terms are SOURCES (do not touch the pencil).
  (A3) kernel lemma with swirl (Prop. A2 3-D-axi analogue): at
       u_n = c the acoustic kernel eigenvector is
       r- = (rho, -c n_x, -c n_r, 0, rho c^2) (swirl component ZERO),
       and the thrust/mass trace covectors annihilate it by the SAME
       law: <grad g, r-> = rho (u_n - c)(u - c n_x),
            <grad m, r-> = rho (u_n - c).

Part B (SYMBOLIC): free-vortex extension theorem N6-2 and the sharp
negative control N6-3:
  (B1) closure justification: with UNIFORM Gamma0 = r w, h0, s, the
       meridional Bernoulli h = h0 - W^2/2 - Gamma0^2/(2 y^2) gives,
       AT FIXED y, dp/dW = -rho W and drho/dW = -rho W/c^2 — the
       exact closure rules of the classical derivation, now with
       p = p(W, y), rho = rho(W, y).
  (B2) VERBATIM re-run of the classical stationarity derivation
       ((L.6), (L.7), (L.10) factorization, (L.12) both families,
       (L.13), corner (L.15)) with two-argument p(W, y), rho(W, y):
       every identity must close UNCHANGED — Rao's machinery extends
       to free-vortex swirl with W = meridional speed. REJECTOR R1:
       sign-corrupted corner must fail.
  (B3) NEGATIVE control (theorem N6-3 seed): with NON-uniform
       Gamma(psi) (or h0(psi)), the fixed-y W-derivative of h picks
       up the extra term -(Gamma Gamma'/y^2 - h0') dpsi/dW /= 0
       generically: the pointwise closure p = p(W, y) FAILS — the
       control-surface reduction does not survive general swirl
       profiles (field-level machinery required).

Exit 0 iff all checks pass INCLUDING the rejectors/negative control.
"""
import sys

import sympy as sp


def partA_structure():
    ok = True
    rho, u, v, w, p, c, lam = sp.symbols('rho u v w p c lambda', real=True)
    A = sp.Matrix([
        [u, rho, 0, 0, 0],
        [0, u, 0, 0, 1 / rho],
        [0, 0, u, 0, 0],
        [0, 0, 0, u, 0],
        [0, rho * c**2, 0, 0, u]])
    B = sp.Matrix([
        [v, 0, rho, 0, 0],
        [0, v, 0, 0, 0],
        [0, 0, v, 0, 1 / rho],
        [0, 0, 0, v, 0],
        [0, 0, rho * c**2, 0, v]])

    d = sp.simplify(sp.det(A) - u**3 * (u**2 - c**2))
    print('  (A1) det A_p == u^3 (u^2 - c^2):           %s'
          % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0

    pencil = sp.det(B - lam * A)
    target = (v - lam * u)**3 * ((v - lam * u)**2 - c**2 * (1 + lam**2))
    d = sp.simplify(sp.expand(pencil - target))
    print('  (A2) pencil == streamline^3 x Mach bracket: %s'
          % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0

    nx, nr = sp.symbols('n_x n_r', real=True)
    un = u * nx + v * nr
    K = A * nx + B * nr
    r_min = sp.Matrix([rho, -c * nx, -c * nr, 0, rho * c**2])
    d = sp.simplify(sp.expand(K * r_min - (un - c) * r_min)
                    .subs(nx**2, 1 - nr**2))
    okv = d == sp.zeros(5, 1)
    print('  (A3) K_p r- == (u_n - c) r- (swirl comp 0): %s'
          % ('PASS' if okv else 'FAIL %s' % d.T))
    ok &= okv

    pa = sp.symbols('p_a', real=True)
    V = [rho, u, v, w, p]
    g = (p - pa) * nx + rho * un * u
    m = rho * un
    grad = lambda F: sp.Matrix([sp.diff(F, x) for x in V]).T
    cg = sp.simplify(sp.expand((grad(g) * r_min)[0]).subs(nx**2, 1 - nr**2))
    cm = sp.simplify(sp.expand((grad(m) * r_min)[0]).subs(nx**2, 1 - nr**2))
    d1 = sp.simplify(sp.expand(cg - rho * (un - c) * (u - c * nx))
                     .subs(nx**2, 1 - nr**2))
    d2 = sp.simplify(sp.expand(cm - rho * (un - c))
                     .subs(nx**2, 1 - nr**2))
    print('  (A3) <grad g, r-> law (swirl):              %s'
          % ('PASS' if d1 == 0 else 'FAIL %s' % d1))
    print('  (A3) <grad m, r-> law (swirl):              %s'
          % ('PASS' if d2 == 0 else 'FAIL %s' % d2))
    ok &= d1 == 0 and d2 == 0
    return ok


def partB_free_vortex():
    ok = True
    # (B1) closure justification at fixed y
    W, y, G0, c = sp.symbols('W y Gamma0 c', positive=True)
    h0 = sp.symbols('h0', positive=True)
    h = h0 - W**2 / 2 - G0**2 / (2 * y**2)
    d = sp.simplify(sp.diff(h, W) + W)
    print('  (B1) free vortex: dh/dW|_y == -W:           %s'
          % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0
    # (with dh = dp/rho along the isentrope at fixed y, this is
    #  dp/dW = -rho W; drho/dW = -rho W/c^2 follows from c^2 = dp/drho.)

    # (B2) verbatim re-run with TWO-ARGUMENT p(W,y), rho(W,y)
    M, q, pa = sp.symbols('M q p_a', positive=True)
    th, ph, al = sp.symbols('theta phi alpha', real=True)
    lam2, lam3 = sp.symbols('lambda2 lambda3', real=True)
    rho = sp.Function('rho', positive=True)(W, y)
    p = sp.Function('p', positive=True)(W, y)
    cW = W / M
    rules = {sp.Derivative(p, W): -rho * W,
             sp.Derivative(rho, W): -rho * W / cW**2}

    f1 = ((p - pa) + rho * W**2 * sp.sin(ph - th) * sp.cos(th)
          / sp.sin(ph)) * q
    f2i = rho * W * sp.sin(ph - th) / sp.sin(ph) * q
    f3 = sp.cot(ph)
    f = f1 + lam2 * f2i + lam3 * f3

    checks = []
    lhs = sp.simplify(f.diff(ph) * sp.sin(ph)**2)
    rhs = q * rho * W * sp.sin(th) * (W * sp.cos(th) + lam2) - lam3
    checks.append(('(L.6)', sp.simplify(sp.expand_trig(sp.simplify(lhs - rhs)))))
    checks.append(('(L.7)', sp.simplify(sp.expand_trig(sp.simplify(
        f.diff(th) + q * rho * W * (W * sp.cos(ph - 2 * th)
                                    + lam2 * sp.cos(ph - th)) / sp.sin(ph))))))
    lam2sol = -W * sp.cos(ph - 2 * th) / sp.cos(ph - th)
    dfW = f.diff(W).subs(rules).subs(lam2, lam2sol)
    lhs = sp.simplify(dfW * sp.sin(ph) * sp.cos(ph - th) / (q * rho * W))
    target = sp.sin(th) * ((M**2 - 1) * sp.sin(ph - th)**2
                           - sp.cos(ph - th)**2)
    checks.append(('(L.10)', sp.simplify(sp.expand_trig(sp.simplify(lhs - target)))))
    checks.append(('(L.12)C+', sp.simplify(sp.expand_trig(
        lam2sol.subs(ph, th + al) + W * sp.cos(th - al) / sp.cos(al)))))
    checks.append(('(L.12)C-', sp.simplify(sp.expand_trig(
        lam2sol.subs(ph, th - al) + W * sp.cos(th + al) / sp.cos(al)))))
    lam3sol = (q * rho * W * sp.sin(th)
               * (W * sp.cos(th) - W * sp.cos(th - al) / sp.cos(al)))
    checks.append(('(L.13)', sp.simplify(sp.expand_trig(sp.simplify(
        lam3sol + q * rho * W**2 * sp.sin(th)**2 * sp.tan(al))))))
    fE = f.subs({ph: th + al,
                 lam2: -W * sp.cos(th - al) / sp.cos(al),
                 lam3: -q * rho * W**2 * sp.sin(th)**2 * sp.tan(al)})
    corner = q * ((p - pa) - sp.Rational(1, 2) * rho * W**2
                  * sp.sin(2 * th) * sp.tan(al))
    checks.append(('(L.15)', sp.simplify(sp.expand_trig(sp.simplify(fE - corner)))))
    for name, d in checks:
        print('  (B2) %-8s verbatim with p(W,y):          %s'
              % (name, 'PASS' if d == 0 else 'FAIL %s' % d))
        ok &= d == 0

    # R1: corrupted corner must fail
    corner_bad = q * ((p - pa) + sp.Rational(1, 2) * rho * W**2
                      * sp.sin(2 * th) * sp.tan(al))
    d = sp.simplify(sp.expand_trig(sp.simplify(fE - corner_bad)))
    rejected = d != 0
    print('  [R1] corrupted corner REJECTED:             %s'
          % ('PASS' if rejected else 'FAIL'))
    ok &= rejected

    # (B3) negative control: general Gamma(psi), h0(psi) break the
    # fixed-y closure: dh/dW|_y = -W - (Gamma Gamma'/y^2 - h0') dpsi/dW
    psi = sp.Function('psi')(W, y)   # streamline label depends on the
    G = sp.Function('Gamma')(psi)    # variation through W at fixed y
    H0 = sp.Function('h0')(psi)
    h_gen = H0 - W**2 / 2 - G**2 / (2 * y**2)
    extra = sp.simplify(sp.diff(h_gen, W) + W)
    # extra == (h0' - Gamma Gamma'/y^2) dpsi/dW: nonzero unless BOTH
    # h0' == 0 and Gamma' == 0 (i.e., exactly the free-vortex case)
    nonzero = extra != 0
    is_free_vortex_only = sp.simplify(
        extra.subs({sp.Derivative(H0, psi): 0,
                    sp.Derivative(G, psi): 0})) == 0
    print('  (B3) general swirl breaks closure (extra term /= 0): %s'
          % ('PASS' if nonzero else 'FAIL'))
    print('  (B3) extra term vanishes EXACTLY at free vortex:     %s'
          % ('PASS' if is_free_vortex_only else 'FAIL'))
    ok &= nonzero and is_free_vortex_only
    return ok


def main():
    print('== N6 swirl carrier: structure + free-vortex + negative ==')
    print('[Part A] axisymmetric Euler WITH swirl (c^2 free)')
    ok = partA_structure()
    print('[Part B] free-vortex extension + sharp negative control')
    ok &= partB_free_vortex()
    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
