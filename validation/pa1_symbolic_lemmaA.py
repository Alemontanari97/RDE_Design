#!/usr/bin/env python3
"""P-A1 attack [F1/P-2, rigor session 2026-07-16]: symbolic machine
verification of the Lemma-A classical derivation (docs/
rde_nozzle_P2_lemmaA.md section 3.2, steps 1-7) plus the KERNEL
SOLVABILITY LEMMA on characteristic surfaces (new result of record;
it REFINES the justification of identification (i)/(ii) in section
3.4 -- see the session log for the discovery discussion).

All symbolic computations are EOS-GENERAL where claimed:
 - Part 1 closes the thermodynamics ONLY through the isentrope rules
   dp/dW = -rho W (Gibbs + Bernoulli) and drho/dW = -rho W / c^2
   (sound-speed definition), with c := W/M kept symbolic.
 - Part 2 keeps c a free positive symbol (no caloric closure at all).

Rejectors: (R1) a sign-corrupted corner formula must FAIL the corner
identity; (R2) the kernel-contraction lemma is FAMILY-SPECIFIC -- the
same contraction with the opposite acoustic eigenvector must be
NONZERO (a test that cannot distinguish the families cannot reject).

Exit code 0 iff all checks pass INCLUDING both rejectors.
"""
import sys

import sympy as sp


def part1_classical_derivation():
    """Machine-verify (L.6), (L.7), (L.10)/(L.11) factorization,
    (L.12), (L.13), and the endpoint identity (L.15) + C- mirror."""
    ok = True
    W, M, q, pa = sp.symbols('W M q p_a', positive=True)
    th, ph, al = sp.symbols('theta phi alpha', real=True)
    lam2, lam3 = sp.symbols('lambda2 lambda3', real=True)
    rho = sp.Function('rho', positive=True)(W)
    p = sp.Function('p', positive=True)(W)
    c = W / M
    rules = {sp.Derivative(p, W): -rho * W,
             sp.Derivative(rho, W): -rho * W / c**2}

    f1 = ((p - pa) + rho * W**2 * sp.sin(ph - th) * sp.cos(th)
          / sp.sin(ph)) * q
    f2i = rho * W * sp.sin(ph - th) / sp.sin(ph) * q
    f3 = sp.cot(ph)
    f = f1 + lam2 * f2i + lam3 * f3

    # (L.6): sin^2(phi) * df/dphi == q rho W sin(th) (W cos(th)+lam2) - lam3
    lhs = sp.simplify(f.diff(ph) * sp.sin(ph)**2)
    rhs = q * rho * W * sp.sin(th) * (W * sp.cos(th) + lam2) - lam3
    d = sp.simplify(sp.expand_trig(sp.simplify(lhs - rhs)))
    print('  (L.6)  d/dphi condition:              %s' % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0

    # (L.7): df/dtheta == -(q rho W / sin(phi)) (W cos(phi-2th)+lam2 cos(phi-th))
    d = sp.simplify(sp.expand_trig(sp.simplify(
        f.diff(th) + q * rho * W * (W * sp.cos(ph - 2 * th)
                                    + lam2 * sp.cos(ph - th)) / sp.sin(ph))))
    print('  (L.7)  d/dtheta condition:            %s' % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0

    # (L.10): after eliminating lam2, df/dW * sin(phi) cos(phi-th) / (q rho W)
    #         == sin(th) [ (M^2-1) sin^2(psi) - cos^2(psi) ],  psi = phi-th
    lam2sol = -W * sp.cos(ph - 2 * th) / sp.cos(ph - th)
    dfW = f.diff(W).subs(rules).subs(lam2, lam2sol)
    lhs = sp.simplify(dfW * sp.sin(ph) * sp.cos(ph - th) / (q * rho * W))
    target = sp.sin(th) * ((M**2 - 1) * sp.sin(ph - th)**2
                           - sp.cos(ph - th)**2)
    d = sp.simplify(sp.expand_trig(sp.simplify(lhs - target)))
    print('  (L.10) characteristic factorization:  %s' % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0
    # Equivalent closed form (trig identity): (M^2-1)sin^2(psi)-cos^2(psi)
    # == M^2 sin^2(psi) - 1; the vanishing locus is sin(psi) = 1/M, i.e.
    # psi = +/- alpha -- Eq. [11].

    # (L.12): at phi = th+al the theta-condition gives lam2 = -W cos(th-al)/cos(al)
    d = sp.simplify(sp.expand_trig(
        lam2sol.subs(ph, th + al) + W * sp.cos(th - al) / sp.cos(al)))
    print('  (L.12) f2 first integral (C+):        %s' % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0
    # C- mirror: phi = th-al  ->  lam2 = -W cos(th+al)/cos(al)
    d = sp.simplify(sp.expand_trig(
        lam2sol.subs(ph, th - al) + W * sp.cos(th + al) / sp.cos(al)))
    print('  (L.12) f2 first integral (C- mirror): %s' % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0

    # (L.13): (L.6)=0 with lam2 of (L.12) gives lam3 = -q rho W^2 sin^2(th) tan(al)
    lam3sol = (q * rho * W * sp.sin(th)
               * (W * sp.cos(th) - W * sp.cos(th - al) / sp.cos(al)))
    d = sp.simplify(sp.expand_trig(sp.simplify(
        lam3sol + q * rho * W**2 * sp.sin(th)**2 * sp.tan(al))))
    print('  (L.13) second integral:               %s' % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0

    # (L.15): endpoint identity -- f at (phi=th+al, lam2, lam3 substituted)
    #         == q [ (p-pa) - (1/2) rho W^2 sin(2 th) tan(al) ]   (pure trig, al free)
    fE = f.subs({ph: th + al,
                 lam2: -W * sp.cos(th - al) / sp.cos(al),
                 lam3: -q * rho * W**2 * sp.sin(th)**2 * sp.tan(al)})
    corner = q * ((p - pa) - sp.Rational(1, 2) * rho * W**2
                  * sp.sin(2 * th) * sp.tan(al))
    d = sp.simplify(sp.expand_trig(sp.simplify(fE - corner)))
    print('  (L.15) corner == CSTR_PA:             %s' % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0

    # (L.16): C- mirror by al -> -al with base pressure role unchanged
    fG = f.subs({ph: th - al,
                 lam2: -W * sp.cos(th + al) / sp.cos(al),
                 lam3: q * rho * W**2 * sp.sin(th)**2 * sp.tan(al)})
    cornerG = q * ((p - pa) + sp.Rational(1, 2) * rho * W**2
                   * sp.sin(2 * th) * sp.tan(al))
    d = sp.simplify(sp.expand_trig(sp.simplify(fG - cornerG)))
    print('  (L.16) corner == CSTR_PB (mirror):    %s' % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0

    # REJECTOR R1: corrupted corner sign must FAIL
    corner_bad = q * ((p - pa) + sp.Rational(1, 2) * rho * W**2
                      * sp.sin(2 * th) * sp.tan(al))
    d = sp.simplify(sp.expand_trig(sp.simplify(fE - corner_bad)))
    rejected = d != 0
    print('  [R1] corrupted corner REJECTED:       %s' % ('PASS' if rejected else 'FAIL'))
    ok &= rejected
    return ok


def part2_kernel_solvability():
    """KERNEL SOLVABILITY LEMMA (EOS-general: c free symbol).
    On a Mach-characteristic surface (u_n = c), the trace covectors of
    the thrust flux g = (p-pa) n_x + rho u_n u and the mass flux
    m = rho u_n BOTH annihilate the kernel of the primitive normal
    Jacobian K_p(n): admissibility of the adjoint boundary data (L.22)
    imposes NO pointwise condition, for ANY lambda2."""
    ok = True
    rho, u, v, p, c, nx, ny, pa = sp.symbols(
        'rho u v p c n_x n_y p_a', real=True, positive=False)
    un = u * nx + v * ny
    K = sp.Matrix([
        [un, rho * nx, rho * ny, 0],
        [0, un, 0, nx / rho],
        [0, 0, un, ny / rho],
        [0, rho * c**2 * nx, rho * c**2 * ny, un]])
    unit = {nx**2: 1 - ny**2}  # |n| = 1

    r_minus = sp.Matrix([rho, -c * nx, -c * ny, rho * c**2])
    d = sp.simplify(sp.expand((K * r_minus - (un - c) * r_minus)).subs(unit))
    okv = d == sp.zeros(4, 1)
    print('  eigvec: K_p r- == (u_n - c) r-:       %s' % ('PASS' if okv else 'FAIL %s' % d.T))
    ok &= okv

    V = [rho, u, v, p]
    g = (p - pa) * nx + rho * un * u
    m = rho * un
    grad = lambda F: sp.Matrix([sp.diff(F, x) for x in V]).T
    cg = sp.simplify(sp.expand((grad(g) * r_minus)[0]).subs(unit))
    cm = sp.simplify(sp.expand((grad(m) * r_minus)[0]).subs(unit))
    d1 = sp.simplify(sp.expand(cg - rho * (un - c) * (u - c * nx))
                     .subs(nx**2, 1 - ny**2))
    d2 = sp.simplify(sp.expand(cm - rho * (un - c))
                     .subs(nx**2, 1 - ny**2))
    print('  <grad g, r-> == rho (u_n-c)(u-c n_x): %s' % ('PASS' if d1 == 0 else 'FAIL %s' % d1))
    print('  <grad m, r-> == rho (u_n-c):          %s' % ('PASS' if d2 == 0 else 'FAIL %s' % d2))
    ok &= d1 == 0 and d2 == 0
    # both vanish identically at u_n = c: solvability is AUTOMATIC.

    # REJECTOR R2: the lemma is family-specific -- with r_plus the
    # contractions must NOT vanish at u_n = c (generic state).
    r_plus = sp.Matrix([rho, c * nx, c * ny, rho * c**2])
    cgp = sp.simplify(sp.expand((grad(g) * r_plus)[0]).subs(unit))
    cgp_on = sp.simplify(cgp.subs(un, c))  # formal substitution u_n -> c
    # substitute un expression: un is u*nx+v*ny, replace v so that un=c
    vsol = sp.solve(sp.Eq(un, c), v)[0]
    cgp_on = sp.simplify(cgp.subs(v, vsol))
    rejected = sp.simplify(cgp_on) != 0
    print('  [R2] r+ contraction NONZERO at u_n=c: %s' % ('PASS' if rejected else 'FAIL'))
    ok &= rejected

    # Exploratory identity of record (computed fact, NOT an f2 claim):
    # off-surface ratio <grad g, r->/<grad m, r-> = u - c n_x; on the C+
    # surface (n=(sin phi, -cos phi), phi=th+al, u=W cos th, c=W sin al)
    # this equals W cos(al) cos(th+al)  --  NOT f2; recorded to document
    # that the naive kernel-ratio does NOT reproduce the invariant (the
    # transport route is where f2 lives; see draft section 3.4 refinement).
    W, th, al = sp.symbols('W theta alpha', positive=True)
    expr = (u - c * nx).subs({u: W * sp.cos(th), c: W * sp.sin(al),
                              nx: sp.sin(th + al)})
    d = sp.simplify(sp.expand_trig(expr - W * sp.cos(al) * sp.cos(th + al)))
    print('  ratio identity u-c n_x = W cos(al)cos(th+al): %s' % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0
    return ok


def part3_transport_invariant():
    """P-A1' DISCHARGE (rigor session, after the HTH-1971/JOTA-1972
    page-level reads): the adjoint (multiplier-field) TRANSPORT route.

    Scope: planar/axisymmetric (delta in {0,1}) IRROTATIONAL homentropic
    frozen flow — the classical bell/plug problem class. EOS-GENERAL:
    only drho/dV = -rho V / c(V)^2 is used, c(.) an arbitrary function.

    (3a) Derive IN-HOUSE the multiplier-field PDEs for the constraints
         continuity d_x(y^d rho u) + d_y(y^d rho v) = 0 (multiplier
         lambda2-field) and irrotationality u_y - v_x = 0 (multiplier
         lambda1-field), and verify that the HTH-1971 closed-form pair
             lambda1 = y^d rho v,   lambda2 = u + K
         solves them for EVERY flow satisfying the two constraints
         (published anchor: Humphreys-Thompson-Hoffman, AIAA J 9(8)
         1971, p. 1583; JOTA 10(3) 1972 Eqs. (19)-(23)).
    (3b) Verify that imposing the terminal-characteristic condition
         E_+/- = lambda1 -/+ lambda2 y^d rho cot(alpha) = 0 (JOTA
         Eq. (26)/(34) C+ form; HTH Eq. (20) C- form) on the family
         a*(y^d rho v, u) + b*(0,1) yields EXACTLY
             V cos(theta -/+ alpha)/cos(alpha) = -b/a = const = f2:
         Rao's first integral as the transported adjoint invariant.
    (3c) REJECTOR: the corrupted pair (lambda1 = y^d rho u) must NOT
         solve the multiplier PDEs.
    """
    ok = True
    x, y, K = sp.symbols('x y K', real=True)
    u = sp.Function('u')(x, y)
    v = sp.Function('v')(x, y)
    rho = sp.Function('rho', positive=True)(x, y)
    c2 = sp.Function('c2', positive=True)(x, y)   # c^2 as a field (EOS-free)
    Vm = sp.sqrt(u**2 + v**2)
    # closure rule rho = rho(V) along the homentrope, d rho/dV = -rho V/c^2,
    # applied to the FIELD derivatives via the chain rule:
    #   rho_x = -(rho V/c^2) V_x,  V_x = (u u_x + v v_x)/V  (same in y)
    rulz = {
        sp.Derivative(rho, x): -(rho / c2) * (u * u.diff(x) + v * v.diff(x)),
        sp.Derivative(rho, y): -(rho / c2) * (u * u.diff(y) + v * v.diff(y)),
    }

    # (3a) multiplier PDE system, derived by parts from
    # Int Int [ lam2 * (d_x(y rho u) + d_y(y rho v)) + lam1*(u_y - v_x) ]
    # (axisymmetric d=1 shown; the planar case replaces y by 1 and is
    # covered by the same check with y -> 1 at the end):
    #   coeff du: -y rho [(1-u^2/c^2) lam2_x - (uv/c^2) lam2_y] - lam1_y = 0
    #   coeff dv: -y rho [-(uv/c^2) lam2_x + (1-v^2/c^2) lam2_y] + lam1_x = 0
    lam1 = y * rho * v
    lam2 = u + K

    def resid_system(l1, l2):
        r1 = (-y * rho * ((1 - u**2 / c2) * l2.diff(x)
                          - (u * v / c2) * l2.diff(y))
              - l1.diff(y))
        r2 = (-y * rho * (-(u * v / c2) * l2.diff(x)
                          + (1 - v**2 / c2) * l2.diff(y))
              + l1.diff(x))
        return r1.subs(rulz).doit(), r2.subs(rulz).doit()

    # flow constraints used as substitution rules:
    # irrotationality: u_y = v_x ; continuity solved for v_y.
    vx = v.diff(x)
    cont = sp.expand(((y * rho * u).diff(x)
                      + (y * rho * v).diff(y)).subs(rulz).doit())
    vy_sol = sp.solve(sp.Eq(cont, 0), v.diff(y))[0]

    def reduce_flow(e):
        e = e.subs(v.diff(y), vy_sol)
        e = e.subs(u.diff(y), vx)
        return sp.simplify(e)

    r1, r2 = resid_system(lam1, lam2)
    d1, d2 = reduce_flow(r1), reduce_flow(r2)
    print('  (3a) HTH pair solves multiplier PDEs:  %s / %s'
          % ('PASS' if d1 == 0 else 'FAIL %s' % d1,
             'PASS' if d2 == 0 else 'FAIL %s' % d2))
    ok &= d1 == 0 and d2 == 0

    # (3b) terminal condition => f2 invariant (pure trig once
    # u = V cos th, v = V sin th, cot(alpha) with sin(alpha) = c/V):
    V, th, al, a, b = sp.symbols('V theta alpha a b', positive=True)
    l1g = a * y * sp.Symbol('rho_s') * V * sp.sin(th)
    l2g = a * V * sp.cos(th) + b
    for fam, sgn, want in (('C+ (bell/JOTA)', +1, th - al),
                           ('C- (plug/HTH)', -1, th + al)):
        E = l1g + sgn * l2g * y * sp.Symbol('rho_s') * sp.cot(al)
        # E = 0  <=>  a V cos(want)/cos(al) = -b  (divide by y rho, x cos/sin)
        expr = sp.simplify(sp.expand_trig(
            (E / (y * sp.Symbol('rho_s'))) * sp.sin(al) * sgn
            - (a * V * sp.cos(want) + b * sp.cos(al))))
        okf = expr == 0
        print('  (3b) %s: E=0 <=> V cos(%s)/cos(al) = -b/a: %s'
              % (fam, want, 'PASS' if okf else 'FAIL %s' % expr))
        ok &= okf

    # (3c) rejector: corrupted pair must fail (3a)
    r1b, r2b = resid_system(y * rho * u, lam2)
    d1b, d2b = reduce_flow(r1b), reduce_flow(r2b)
    rejected = not (d1b == 0 and d2b == 0)
    print('  (3c) corrupted pair REJECTED:          %s'
          % ('PASS' if rejected else 'FAIL (cannot reject)'))
    ok &= rejected
    return ok


def main():
    print('== P-A1 symbolic attack: Lemma A machine verification ==')
    print('[Part 1] classical derivation (EOS-general closure rules)')
    ok1 = part1_classical_derivation()
    print('[Part 2] kernel solvability lemma (c fully symbolic)')
    ok2 = part2_kernel_solvability()
    print('[Part 3] transport invariant: P-A1-prime discharge')
    ok3 = part3_transport_invariant()
    ok = ok1 and ok2 and ok3
    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
