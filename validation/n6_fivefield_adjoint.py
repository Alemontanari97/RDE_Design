#!/usr/bin/env python3
"""Five-field swirl adjoint carrier [F1/N6-5F, rigor session 8]:
machine derivation and verification of the formal adjoint structure
of the axisymmetric-with-swirl per-phase system (docs/
rde_nozzle_N6_swirl.md section 4 upgrade).

EOS-general: the sound speed enters only as a free two-argument
function c2(P, rho); sources (centrifugal, swirl transport, axisymmetric
continuity weight) included exactly.

Checks (each a FINITE identity — symbolic verification SUFFICES):
 (5F.1) LINEARIZATION: compute the coefficient matrices (A, B, M) of
        the linearized operator L dV = A dV_x + B dV_r + M dV about an
        arbitrary base flow (M carries the base-flow gradients and the
        source couplings — the NEW record content).
 (5F.2) PRINCIPAL SYMBOL: det(B - lam A) equals the N6-1 pencil
        (streamline^3 x meridional Mach bracket) up to the exact row
        weights (r from continuity, rho from momenta/transport, u,v
        entering only via the pencil) — the adjoint system propagates
        along the SAME characteristics (Prop. A1 instance, now with
        swirl and sources).
 (5F.3) LAGRANGE IDENTITY: h . (L dV) - dV . (L* h) is an EXACT
        divergence with L* h := -d_x(A^T h) - d_r(B^T h) + M^T h —
        the bookkeeping certificate that (A, B, M) are consistent and
        the adjoint is correctly transposed.
 (5F.4) TERMINAL GAUGE DIRECTION: at a meridional Mach front
        (u_n = c) the transposed symbol K(n)^T = (A n_x + B n_r)^T is
        singular; compute its kernel l(n) in CLOSED FORM and verify
        K(n)^T l = 0 — l is the gauge direction of the adjoint
        boundary data (the Hoffman-counting object with swirl).
 REJECTOR (R1): a corrupted M (one source term sign flipped) must
        BREAK the Lagrange identity.

Exit 0 iff all checks pass INCLUDING the rejector.
"""
import sys

import sympy as sp


def build():
    x, r = sp.symbols('x r', positive=True)
    rho = sp.Function('rho', positive=True)(x, r)
    u = sp.Function('u')(x, r)
    v = sp.Function('v')(x, r)
    w = sp.Function('w')(x, r)
    P = sp.Function('P', positive=True)(x, r)
    c2 = sp.Function('c2', positive=True)(P, rho)
    V = [rho, u, v, w, P]

    E = [
        (r * rho * u).diff(x) + (r * rho * v).diff(r),
        rho * (u * u.diff(x) + v * u.diff(r)) + P.diff(x),
        rho * (u * v.diff(x) + v * v.diff(r)) + P.diff(r) - rho * w**2 / r,
        rho * (u * w.diff(x) + v * w.diff(r)) + rho * v * w / r,
        u * P.diff(x) + v * P.diff(r) - c2 * (u * rho.diff(x)
                                              + v * rho.diff(r)),
    ]
    return x, r, V, E


def linearize(x, r, V, E):
    """Frechet derivative of E at V in direction dV; extract (A, B, M)."""
    dV = [sp.Function('d%d' % j)(x, r) for j in range(5)]
    eps = sp.symbols('epsilon')
    subs_pert = {V[j]: V[j] + eps * dV[j] for j in range(5)}
    A = sp.zeros(5, 5)
    B = sp.zeros(5, 5)
    M = sp.zeros(5, 5)
    dE = []
    for i in range(5):
        Ei = E[i].subs(subs_pert).doit()
        dEi = sp.expand(sp.diff(Ei, eps).subs(eps, 0).doit())
        dE.append(dEi)
        for j in range(5):
            A[i, j] = sp.simplify(dEi.coeff(dV[j].diff(x)))
            B[i, j] = sp.simplify(dEi.coeff(dV[j].diff(r)))
        rem = sp.expand(dEi - sum(A[i, j] * dV[j].diff(x)
                                  + B[i, j] * dV[j].diff(r)
                                  for j in range(5)))
        for j in range(5):
            M[i, j] = sp.simplify(rem.coeff(dV[j]))
        leftover = sp.simplify(rem - sum(M[i, j] * dV[j] for j in range(5)))
        if leftover != 0:
            raise RuntimeError('linearization leftover row %d: %s'
                               % (i, leftover))
    return A, B, M, dV, dE


def main():
    ok = True
    print('== five-field swirl adjoint carrier (EOS-general) ==')
    x, r, V, E = build()
    A, B, M, dV, dE = linearize(x, r, V, E)
    print('  (5F.1) linearization extracted, no leftover:  PASS')

    # (5F.2) principal symbol vs the N6-1 pencil with exact row weights:
    # rows (continuity, mom-x, mom-r, transport, energy) carry weights
    # (r, rho, rho, rho, 1); the pencil of the WEIGHTED primitive system
    # equals r rho^3 (v - lam u)^3 [ (v - lam u)^2 - c2 (1 + lam^2) ].
    lam = sp.symbols('lambda')
    rho_, u_, v_ = V[0], V[1], V[2]
    c2_ = sp.Function('c2', positive=True)(V[4], V[0])
    pencil = sp.det(B - lam * A)
    target = (r * rho_**3 * (v_ - lam * u_)**3
              * ((v_ - lam * u_)**2 - c2_ * (1 + lam**2)))
    d = sp.simplify(sp.expand(pencil - target))
    print('  (5F.2) det(B - lam A) == r rho^3 x N6-1 pencil: %s'
          % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0

    # (5F.3) Lagrange identity with the machine-derived (A, B, M)
    h = [sp.Function('h%d' % i)(x, r) for i in range(5)]
    Lstar = [sp.expand(
        -sum((A[i, j] * h[i]).diff(x) + (B[i, j] * h[i]).diff(r)
             for i in range(5))
        + sum(M[i, j] * h[i] for i in range(5))) for j in range(5)]
    lhs = sp.expand(sum(h[i] * dE[i] for i in range(5))
                    - sum(dV[j] * Lstar[j] for j in range(5)))
    fluxx = sum(h[i] * A[i, j] * dV[j] for i in range(5) for j in range(5))
    fluxr = sum(h[i] * B[i, j] * dV[j] for i in range(5) for j in range(5))
    d = sp.simplify(lhs - sp.expand(sp.diff(fluxx, x) + sp.diff(fluxr, r)))
    print('  (5F.3) Lagrange identity (exact divergence):   %s'
          % ('PASS' if d == 0 else 'FAIL %s' % d))
    ok &= d == 0

    # (5F.4) terminal gauge direction: left kernel of K(n) at u_n = c.
    # Closed-form candidate (hand-derived, then machine-VERIFIED —
    # more pristine than a generic nullspace call, which fails to
    # simplify): l(n) = (1, -r n_x/c, -r n_r/c, 0, r/c^2).
    # Note the ZERO swirl component — the swirl multiplier h_4 does
    # not enter the terminal gauge.
    nx, nr, c = sp.symbols('n_x n_r c', real=True)
    K = (A * nx + B * nr)
    un = u_ * nx + v_ * nr
    vsol = sp.solve(sp.Eq(un, c), v_)[0]
    Kc = sp.simplify(K.subs(c2_, c**2).subs(v_, vsol))
    ell = sp.Matrix([1, -r * nx / c, -r * nr / c, 0, r / c**2])
    chk = sp.simplify(sp.expand(ell.T * Kc).subs(nx**2, 1 - nr**2))
    okz = chk == sp.zeros(1, 5)
    print('  (5F.4) l(n)^T K == 0 at u_n = c (closed form): %s'
          % ('PASS' if okz else 'FAIL %s' % chk))
    ok &= okz
    # rank certificate: kernel EXACTLY 1-dim <=> some 4x4 minor /= 0;
    # rows (mom-x, mom-r, transport, energy) x cols (u, v, w, P):
    minor = Kc[1:5, 1:5]
    dmin = sp.simplify(sp.det(minor) - rho_**3 * c**4)
    okm = dmin == 0
    print('  (5F.4) 4x4 minor det == rho^3 c^4 (rank 4):    %s'
          % ('PASS' if okm else 'FAIL %s' % dmin))
    ok &= okm

    # R1: corrupted M (flip the centrifugal coupling sign) must break
    # the Lagrange identity
    Mbad = M.copy()
    Mbad[2, 3] = -M[2, 3]  # d(centrifugal)/dw coupling, sign flipped
    Lstar_bad = [sp.expand(
        -sum((A[i, j] * h[i]).diff(x) + (B[i, j] * h[i]).diff(r)
             for i in range(5))
        + sum(Mbad[i, j] * h[i] for i in range(5))) for j in range(5)]
    lhs_bad = sp.expand(sum(h[i] * dE[i] for i in range(5))
                        - sum(dV[j] * Lstar_bad[j] for j in range(5)))
    d = sp.simplify(lhs_bad - sp.expand(sp.diff(fluxx, x)
                                        + sp.diff(fluxr, r)))
    rejected = d != 0
    print('  [R1] corrupted M BREAKS Lagrange identity:     %s'
          % ('PASS' if rejected else 'FAIL'))
    ok &= rejected

    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
