#!/usr/bin/env python3
"""U3 bordered front-solve carrier [RIGOR/A, S16 deep-foundations
tranche 2]: machine verification of the free-boundary solvability
structure that D2.5-U step U3 rests on (docs/rde_nozzle_D25U_U3U4.md
§2-§3; registry [X-U3BD], theorem-side [S-D25U-U34] / condition U3-H1).

CONTENT. In the x-as-time reading a fitted Lax front is a genuine 1-D
shock of the y-line evolution. Per x-station the front solve couples
   (delta V_plus, delta sigma')  —  5 unknowns
to
   4 linearized RH equations + 1 impinging downstream characteristic
   variable (the Lax count supplies exactly one),
i.e. the BORDERED system
   M = [ dH/dV_plus   dH/dsigma' ]
       [   w_imp^T        0      ],   w_imp^T = l_imp^T A_p(V_plus),
where l_imp is the left eigenvector of the impinging downstream
family. G12-L2 certified the two blocks separately (dH/dV_plus
nonsingular, dH/dsigma' /= 0); U3 additionally needs M itself
nonsingular — equivalently the SCHUR SCALAR
   s_L := w_imp^T (dH/dV_plus)^{-1} dH/dsigma'  /=  0,
which is the 1-D Majda-Lopatinskii determinant of the front in this
frame: THE sharpened quantitative content of C-MAJDA inside the
planar S1 class.

Checks (numeric known-answer oracle, perfect gas gamma = 1.4 as
DECLARED instantiation; derived SVD/FD tolerances, no magic numbers):
  (P1) LAX COUNT at the oracle (M1 = 2.5, beta = 40 deg): exactly ONE
       downstream family impinges on the front (lambda > sigma' on the
       downstream side) and all FOUR upstream characteristics impinge
       — total 5 = n + 1, the classical Lax count; slope margins
       printed as the certified-set "Lax front-strength margins".
  (P2) bordered matrix M nonsingular: equilibrated s_min above the
       derived FD floor.
  (P3) Schur scalar s_L /= 0 above the same floor, PLUS the linear-
       algebra crosscheck det M_eq == -det(J_eq) * s_L_eq within
       derived tolerance (bordered-determinant identity).
  (P4) class-margin exhibit: axial supersonicity u > c on BOTH sides
       (the S1 margin) and total-supersonic downstream q > c (the
       Mach-angle construction is well-defined; U2's q = c locus is
       away) — printed, and REQUIRED > 0.
  REJECTORS:
  (R1) characteristic-front degeneration (zero strength, Mach-line
       slope): the bordered matrix must be DETECTED singular — the
       honest boundary of the front brick (same locus as G12-L2(c)).
  (R2) a sign-corrupted RH row must break the known-answer oracle.

Exit 0 iff all checks pass INCLUDING both rejectors.
"""
import math
import sys

import numpy as np

EPS = sys.float_info.epsilon


# ---------------------------------------------------------------- shared
# oracle pieces (same construction as validation/g12_shock_linearization.py,
# duplicated by design: carriers stay standalone)
def _perfect_gas_state(M, gam, rho1=1.2, p1=1.0e5, theta=0.0):
    c1 = math.sqrt(gam * p1 / rho1)
    V = M * c1
    return np.array([rho1, V * math.cos(theta), V * math.sin(theta), p1])


def _oblique_downstream(V1, beta, gam):
    rho1, u1, v1, p1 = V1
    c1 = math.sqrt(gam * p1 / rho1)
    n = np.array([math.sin(beta), -math.cos(beta)])
    t = np.array([math.cos(beta), math.sin(beta)])
    q1 = np.array([u1, v1])
    un1, ut1 = q1 @ n, q1 @ t
    Mn1 = abs(un1) / c1
    p2 = p1 * (1.0 + 2.0 * gam / (gam + 1.0) * (Mn1**2 - 1.0))
    r2 = rho1 * ((gam + 1.0) * Mn1**2) / ((gam - 1.0) * Mn1**2 + 2.0)
    un2 = un1 * rho1 / r2
    q2 = un2 * n + ut1 * t
    return np.array([r2, q2[0], q2[1], p2])


def _H(Vp, Vm, sig, gam):
    s = 1.0 / math.sqrt(1.0 + sig * sig)

    def parts(V):
        rho, u, v, p = V
        un = (sig * u - v) * s
        ut = (u + sig * v) * s
        h = gam / (gam - 1.0) * p / rho
        return rho, un, ut, p, h

    rp, unp, utp, pp, hp = parts(Vp)
    rm, unm, utm, pm, hm = parts(Vm)
    return np.array([
        rp * unp - rm * unm,
        (pp + rp * unp**2) - (pm + rm * unm**2),
        utp - utm,
        (hp + 0.5 * (unp**2 + utp**2)) - (hm + 0.5 * (unm**2 + utm**2))])


def _jac(f, x, scale):
    x = np.asarray(x, dtype=float)
    cols = []
    for i in range(x.size):
        h = EPS ** (1.0 / 3.0) * scale[i]
        e = np.zeros_like(x)
        e[i] = h
        cols.append((f(x + e) - f(x - e)) / (2.0 * h))
    return np.stack(cols, axis=1)


# ---------------------------------------------------------------- pencil
def _Ap(V, gam):
    rho, u, v, p = V
    c2 = gam * p / rho
    return np.array([
        [u, rho, 0.0, 0.0],
        [0.0, u, 0.0, 1.0 / rho],
        [0.0, 0.0, u, 0.0],
        [0.0, rho * c2, 0.0, u]])


def _Bp(V, gam):
    rho, u, v, p = V
    c2 = gam * p / rho
    return np.array([
        [v, 0.0, rho, 0.0],
        [0.0, v, 0.0, 0.0],
        [0.0, 0.0, v, 1.0 / rho],
        [0.0, 0.0, rho * c2, v]])


def _slopes(V, gam):
    """Characteristic slopes dy/dx at a TOTAL-supersonic state:
    lambda_0 = v/u (double), lambda_pm = tan(theta -+/+ alpha)."""
    rho, u, v, p = V
    c = math.sqrt(gam * p / rho)
    q = math.hypot(u, v)
    if q <= c:
        raise ValueError('total-subsonic state: Mach angle undefined')
    th = math.atan2(v, u)
    al = math.asin(c / q)
    return v / u, math.tan(th - al), math.tan(th + al)


def _left_eigvec(V, lam, gam):
    """Left eigenvector l^T (B_p - lam A_p) = 0, unit norm, via SVD."""
    P = _Bp(V, gam) - lam * _Ap(V, gam)
    _, s, Vt = np.linalg.svd(P.T)
    l = Vt[-1]
    return l / np.linalg.norm(l), s[-1] / s[0]


# ---------------------------------------------------------------- checks
def main():
    print('== U3 bordered front-solve carrier (X-U3BD) ==')
    ok = True
    gam = 1.4
    beta = math.radians(40.0)
    V1 = _perfect_gas_state(2.5, gam)
    V2 = _oblique_downstream(V1, beta, gam)
    sig = math.tan(beta)

    # oracle sanity (same derived floors as X-G12)
    scaleH = np.array([V1[0] * abs(V1[1]), V1[3], abs(V1[1]),
                       gam / (gam - 1.0) * V1[3] / V1[0]])
    tolH = 1e3 * EPS * scaleH
    r = _H(V2, V1, sig, gam)
    good = np.all(np.abs(r) <= tolH)
    print('  (P0) oracle RH residual == 0:               PASS' if good
          else '  (P0) oracle RH residual: FAIL (max %.2e)'
          % float(np.max(np.abs(r) / scaleH)))
    ok &= good

    # geometry of record: n = (sin b, -cos b) has n_y < 0, so the
    # DOWNSTREAM side (+n, mass flux direction) is y < sigma(x);
    # a downstream characteristic impinges iff lambda > sigma',
    # an upstream one (side y > sigma) iff lambda < sigma'.
    lam0_u, lamm_u, lamp_u = _slopes(V1, gam)
    lam0_d, lamm_d, lamp_d = _slopes(V2, gam)
    up_imp = [lam < sig for lam in (lam0_u, lam0_u, lamm_u, lamp_u)]
    dn_slopes = {'0': lam0_d, '-': lamm_d, '+': lamp_d}
    dn_imp = {k: lam > sig for k, lam in dn_slopes.items()}
    n_dn = sum(dn_imp.values()) + (1 if dn_imp['0'] else 0)  # 0 is double
    good = all(up_imp) and n_dn == 1 and dn_imp['+']
    print('  (P1) Lax count: upstream impinging 4/4, downstream '
          'impinging = {+} only: %s' % ('PASS' if good else 'FAIL'))
    print('       margins: lam+^dn - sig\' = %.4f, sig\' - lam+^up = %.4f,'
          % (lamp_d - sig, sig - lamp_u))
    print('                sig\' - lam0^dn = %.4f, sig\' - lam0^up = %.4f'
          % (sig - lam0_d, sig - lam0_u))
    ok &= good

    # bordered matrix M = [[dH/dV+, dH/ds'], [l+^T A_p(V2), 0]]
    scaleV = np.maximum(np.abs(V2), np.array([1e-3, 1.0, 1.0, 1.0]))
    Jv = _jac(lambda V: _H(V, V1, sig, gam), V2, scaleV)
    Js = _jac(lambda s_: _H(V2, V1, s_[0], gam), np.array([sig]),
              np.array([max(1.0, abs(sig))]))[:, 0]
    l_imp, resid = _left_eigvec(V2, lamp_d, gam)
    good = resid < 1e3 * EPS
    print('  (P1b) impinging left eigenvector residual %.2e:  %s'
          % (resid, 'PASS' if good else 'FAIL'))
    ok &= good
    w = _Ap(V2, gam).T @ l_imp

    M = np.zeros((5, 5))
    M[:4, :4] = Jv
    M[:4, 4] = Js
    M[4, :4] = w
    rowscale = np.concatenate([scaleH, [np.linalg.norm(w * scaleV)]])
    colscale = np.concatenate([scaleV, [max(1.0, abs(sig))]])
    Meq = (M / rowscale[:, None]) * colscale[None, :]
    sv = np.linalg.svd(Meq, compute_uv=False)
    floor = 1e3 * EPS ** (2.0 / 3.0) * sv[0]
    good = sv[-1] > floor
    print('  (P2) bordered M nonsingular (equilibrated): s_min %.3e '
          '(floor %.3e): %s' % (sv[-1], floor, 'PASS' if good else 'FAIL'))
    ok &= good

    # Schur scalar (equilibrated blocks) + determinant identity
    Jeq = Meq[:4, :4]
    beq = Meq[:4, 4]
    ceq = Meq[4, :4]
    sL = float(ceq @ np.linalg.solve(Jeq, beq))
    good = abs(sL) > floor
    print('  (P3) Lopatinskii-Schur scalar s_L = %.6e:   %s'
          % (sL, 'PASS' if good else 'FAIL'))
    ok &= good
    detM = float(np.linalg.det(Meq))
    detJ = float(np.linalg.det(Jeq))
    err = abs(detM + detJ * sL) / max(abs(detM), abs(detJ * sL))
    good = err < 1e3 * EPS ** (2.0 / 3.0)
    print('  (P3b) det identity det M == -det J * s_L: rel err %.2e: %s'
          % (err, 'PASS' if good else 'FAIL'))
    ok &= good

    # class margins exhibited (axial supersonic both sides; q > c dn)
    c1 = math.sqrt(gam * V1[3] / V1[0])
    c2 = math.sqrt(gam * V2[3] / V2[0])
    q2 = math.hypot(V2[1], V2[2])
    m_ax1, m_ax2, m_q2 = V1[1] - c1, V2[1] - c2, q2 - c2
    good = m_ax1 > 0 and m_ax2 > 0 and m_q2 > 0
    print('  (P4) margins: u-c up %.1f, u-c dn %.1f, q-c dn %.1f:  %s'
          % (m_ax1, m_ax2, m_q2, 'PASS' if good else 'FAIL'))
    ok &= good

    # R1: characteristic-front limit — bordered matrix must degenerate
    th = math.atan2(V1[2], V1[1])
    al = math.asin(1.0 / 2.5)
    sig_c = math.tan(th + al)
    Jv0 = _jac(lambda V: _H(V, V1, sig_c, gam), V1.copy(), scaleV)
    Js0 = _jac(lambda s_: _H(V1, V1, s_[0], gam), np.array([sig_c]),
               np.array([max(1.0, abs(sig_c))]))[:, 0]
    l0, _ = _left_eigvec(V1, math.tan(th + al), gam)
    w0 = _Ap(V1, gam).T @ l0
    M0 = np.zeros((5, 5))
    M0[:4, :4] = Jv0
    M0[:4, 4] = Js0
    M0[4, :4] = w0
    rs0 = np.concatenate([scaleH, [np.linalg.norm(w0 * scaleV)]])
    cs0 = np.concatenate([scaleV, [max(1.0, abs(sig_c))]])
    M0eq = (M0 / rs0[:, None]) * cs0[None, :]
    sv0 = np.linalg.svd(M0eq, compute_uv=False)
    deg = sv0[-1] < floor
    print('  [R1] characteristic front: bordered s_min %.3e DETECTED '
          'singular: %s' % (sv0[-1], 'PASS' if deg else 'FAIL'))
    ok &= deg

    # R2: corrupted RH row must break the oracle
    def H_bad(Vp, Vm, s_, g):
        rr = _H(Vp, Vm, s_, g)
        rr[1] = (Vp[3]) - (Vm[3])  # pressure jump only: wrong physics
        return rr
    rejected = np.any(np.abs(H_bad(V2, V1, sig, gam)) > tolH)
    print('  [R2] corrupted RH row REJECTED:              %s'
          % ('PASS' if rejected else 'FAIL'))
    ok &= rejected

    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
