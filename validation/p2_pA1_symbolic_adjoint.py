#!/usr/bin/env python3
"""INDEPENDENT DUAL-ROUTE VERIFICATION of the Prop. A2 layer of Lemma A
[F1/P-2, session S7 — operational session, written CONCURRENTLY with
and reconciled AGAINST the rigor session S6 that discharged P-A1/P-A1'
(commits 5ec62ef/86e6d6d: Prop. A2 kernel solvability in PRIMITIVE
variables; Prop. A3 f2 = transported adjoint invariant)].

WHAT THIS SCRIPT ADDS (it does NOT re-claim the P-A1' discharge):
an independent machine verification of the same boundary-layer facts
in CONSERVATIVE variables — the variable set the discrete engine of
Lemma B actually transposes — with a general-EOS Grueneisen closure
(p(rho, rho e), a = dp/drho|_{rho e}, b = dp/d(rho e)|_rho free
symbols, exact identity c^2 = a + b h), Weierstrass-exact zero tests,
the EXPLICIT left null covector, extra negative controls, and the
(L.20) flux-vs-Rao bookkeeping check. Agreement of this conservative
route with the rigor session's primitive route is a genuine dual-route
certificate (independent code, variables, and zero-test machinery).

 C1  Geometry: with n = (sin phi, -cos phi), phi = theta +/- alpha,
     the normal velocity on the Mach surface is u_n = +/- c exactly.
 C2  Kernel pair: K := A n_x + B n_y (conservative flux Jacobians) has
     K r = 0 with r = (1, u - u_n n_x, v - u_n n_y, H - c^2) (acoustic;
     proves det K = 0) and l^T K = 0 with the EXPLICIT left covector
     l . dU = dp - rho u_n du_n — both EOS-general.
 C3  Bookkeeping (L.20): the flux forms reproduce Rao's integrands,
     g ds = f1 dy and (rho u_n) ds = f2^i dy with ds = dy/sin(phi)
     (the "elementary bookkeeping" the Lemma-A draft deferred to the
     paper appendix — now executable).
 C4  KERNEL-ANNIHILATION IDENTITY (= Prop. A2 in conservative
     variables): the augmented boundary datum
     d = grad_U [ rho u_n u + (p - pa) n_x + lambda2 rho u_n ]
     satisfies d . r = 0 IDENTICALLY — for EVERY lambda2, every EOS,
     both families. Consequence (per Prop. A2 of record): (L.22) is
     SOLVABLE on the characteristic surface for every lambda2, i.e.
     mere solvability imposes NO pointwise condition — the refined
     reading of identification (i); the f2 content lives in the
     TANGENT TRANSPORT (Prop. A3, rigor session), not here.
 C5  The adjoint trace: psi = psi_p + t * l (Fredholm C4 + the rank-3
     certificate below); the gauge t is fixed only by the interior
     transport along the tangent characteristic (Prop. A3's layer).
 C6  BOUNDARY-DATUM READING LEMMA (complementary to Prop. A3, weaker
     by design): for ANY probe w with grad_U(mass flux) . w = 1,
     grad_U(thrust flux) . w = 0, the combination
         Lambda(psi) := psi . (K w)
     is (a) GAUGE-INDEPENDENT ((K w) . l = 0 exactly) and (b) equal to
     -lambda2 for EVERY adjoint solution psi: the constant lambda2 can
     be read pointwise off the adjoint trace through the boundary
     condition — the executable form of the draft's "constants <->
     boundary data" half of (ii). With (L.12) [lambda2 = -f2, THEOREM]
     this evaluates to f2 = W cos(theta -/+ alpha)/cos(alpha) on the
     optimal Sigma. NOTE (honesty, consistent with Prop. A2): this
     reads the datum back through (L.22); it does NOT derive f2's
     invariance from transport — that is Prop. A3, already of record.
 C7  NEGATIVE CONTROLS (the pass must be able to REJECT):
     NC1 on a NON-characteristic surface (phi = theta + alpha + delta)
         det K != 0: no closure freedom — rejects "any surface works";
     NC2 with the pressure term dropped from the thrust datum,
         d_corr . r != 0: the annihilation identity is structure-
         sensitive — rejects a wrong objective pairing;
     NC3 a corrupted kernel vector (H -> h) fails K r = 0.

METHOD: exact rational algebra. sin/cos of theta and alpha are symbols
with Pythagorean constraints; every zero-claim is decided by the
WEIERSTRASS substitution (st = 2t/(1+t^2), ct = (1-t^2)/(1+t^2), same
for alpha) which satisfies the constraints identically, turning each
claim into a rational-function identity settled by cancel() — proofs,
not floats. The EOS enters only through the free symbols (a, b, p,
e0) with a eliminated via c^2 = a + b h (h = e0 + p/rho): no caloric
closure anywhere in the symbolic core.

NUMERIC INSTANTIATION (DECLARED gamma = const ORACLE, per the
strengthened directive: perfect gas appears ONLY as a known-answer
instance): the Rao-1961 spike Table-1 oracle regime, gamma = 1.23,
M = 2.4, theta = -8.25 deg (C- family, plug) and a C+ bell-regime
point (M = 2.2, theta = +8 deg); includes the rank-3 certificate
(exactly one vanishing singular value of K). Tolerance DERIVED: the
residuals are sums of <= ~60 products of <= 6 factors, so accumulated
relative roundoff <= 360 eps; we use K_OPS = 1024 (safety ~3x) times
eps times the max term magnitude — no magic numbers.

Exit code 0 iff ALL checks pass INCLUDING the negative-control
rejections.
"""
import sys

import sympy as sp

# ---------------------------------------------------------------- symbols
rho, W, p, pa, e0, b, lam2 = sp.symbols(
    'rho W p p_a e0 b lambda2', positive=False)
st, ct, sa, ca = sp.symbols('s_t c_t s_a c_a')   # sin/cos of theta, alpha
t_gauge = sp.symbols('t_gauge')                   # adjoint gauge parameter

IDEAL = [st**2 + ct**2 - 1, sa**2 + ca**2 - 1]
GENS = (st, ct, sa, ca)


_T, _U = sp.symbols('t_wp u_wp')
_WEIER = {st: 2 * _T / (1 + _T**2), ct: (1 - _T**2) / (1 + _T**2),
          sa: 2 * _U / (1 + _U**2), ca: (1 - _U**2) / (1 + _U**2)}


def is_zero(expr):
    """Exact zero test on the trig variety (proof, not float): the
    Weierstrass parametrization st = 2t/(1+t^2), ct = (1-t^2)/(1+t^2)
    (same for alpha with u) satisfies the Pythagorean constraints
    IDENTICALLY, so the claim becomes a rational-function identity in
    (t, u, rho, W, p, e0, b, ...) decided by cancel(): the numerator
    must vanish literally.  (The parametrization covers the circle
    minus one point — Zariski-dense, so a vanishing rational identity
    there vanishes on the whole variety.)"""
    e = sp.together(sp.expand(expr.subs(_WEIER)))
    num, _ = sp.fraction(sp.cancel(e))
    return sp.expand(num) == 0


def build(side):
    """Everything on one characteristic family.

    side = +1: C+ (bell/shroud), phi = theta + alpha, u_n = +c;
    side = -1: C- (plug/spike),  phi = theta - alpha, u_n = -c
    (the draft's alpha -> -alpha mirror, implemented literally).
    Returns a dict of the symbolic objects."""
    sa_s, ca_s = side * sa, ca                    # sin/cos of (side*alpha)
    # trig of phi = theta + side*alpha
    sphi = st * ca_s + ct * sa_s
    cphi = ct * ca_s - st * sa_s
    nx, ny = sphi, -cphi                          # surface normal
    u, v = W * ct, W * st
    c = W * sa                                    # |u_n| = c = W sin(alpha)
    un = side * c                                 # u . n on the Mach surface
    h = e0 + p / rho
    H = h + W**2 / 2
    a_eos = c**2 - b * h                          # EXACT: c^2 = a + b h
    E0 = e0 + W**2 / 2

    # conservative variables and point values
    U1, U2, U3, U4 = sp.symbols('U1 U2 U3 U4')
    Uv = sp.Matrix([U1, U2, U3, U4])
    point = {U1: rho, U2: rho * u, U3: rho * v, U4: rho * E0}
    eps_expr = U4 - (U2**2 + U3**2) / (2 * U1)
    # linearized-at-the-point EOS: exact Jacobians, general p(rho, rho e)
    p_lin = p + a_eos * (U1 - rho) + b * (eps_expr - rho * e0)

    F = sp.Matrix([U2, U2**2 / U1 + p_lin, U2 * U3 / U1,
                   U2 / U1 * (U4 + p_lin)])
    G = sp.Matrix([U3, U2 * U3 / U1, U3**2 / U1 + p_lin,
                   U3 / U1 * (U4 + p_lin)])
    A = F.jacobian(Uv).subs(point)
    B = G.jacobian(Uv).subs(point)
    K = (A * nx + B * ny)

    # acoustic right null vector (EOS-general form)
    r = sp.Matrix([1, u - un * nx, v - un * ny, H - c**2])
    # acoustic LEFT null covector: l.dU = dp - rho*u_n*du_n (the
    # characteristic combination of the tangent family), explicitly
    l = sp.Matrix([a_eos + b * W**2 / 2 + c**2,
                   -b * u - un * nx, -b * v - un * ny, b])

    # boundary datum: thrust flux + lambda2 * mass flux, gradients in U
    m_expr = U2 * nx + U3 * ny                    # rho u_n
    g_expr = m_expr * U2 / U1 + (p_lin - pa) * nx  # rho u_n u + (p - pa) n_x
    d_g = sp.Matrix([sp.diff(g_expr, x) for x in Uv]).subs(point)
    d_m = sp.Matrix([sp.diff(m_expr, x) for x in Uv]).subs(point)
    d = d_g + lam2 * d_m

    return dict(A=A, B=B, K=K, r=r, l=l, d=d, d_g=d_g, d_m=d_m, u=u, v=v,
                c=c, un=un, H=H, h=h, nx=nx, ny=ny, sphi=sphi, cphi=cphi,
                sa_s=sa_s, ca_s=ca_s, point=point)


def f2_of(side):
    """Rao first integral (L.12): W cos(theta - side*alpha)/cos(alpha)."""
    return W * (ct * ca + side * st * sa) / ca    # cos(theta -/+ alpha)/cos a


def check(label, ok):
    print('  [%s] %s' % (label, 'PASS' if ok else 'FAIL'), flush=True)
    return ok


def run_side(side, name):
    print('== family %s (side = %+d) ==' % (name, side), flush=True)
    S = build(side)
    ok = True

    # C1 geometry: u . n = side * c
    un_direct = S['u'] * S['nx'] + S['v'] * S['ny']
    ok &= check('C1 u_n = %+dc on the Mach surface' % side,
                is_zero(un_direct - S['un']))

    # C2 kernel: K r = 0 (which PROVES det K = 0, since r != 0) and the
    # EXPLICIT left null covector l = dp-cov -/+ rho*c du_n-cov (the
    # acoustic characteristic covector l.dU = dp - rho c du_n for the
    # u_n = +c family; + for u_n = -c): l^T K = 0.
    Kr = S['K'] * S['r']
    ok &= check('C2a K r = 0 (acoustic kernel => det K = 0, EOS-general)',
                all(is_zero(x) for x in Kr))
    lK = S['l'].T * S['K']
    ok &= check('C2b l^T K = 0 (explicit left null covector)',
                all(is_zero(x) for x in lK))

    # C3 bookkeeping (L.20): g/sin(phi) = f1, m/sin(phi) = f2^i
    #   with u_n = W sin(phi - theta) (valid for ANY phi, so stated with
    #   the surface's own phi): f1 = (p - pa) + rho W^2 sin(phi-theta)
    #   cos(theta)/sin(phi); f2i = rho W sin(phi-theta)/sin(phi).
    sphimt = S['sphi'] * ct - S['cphi'] * st      # sin(phi - theta)
    f1 = (p - pa) + rho * W**2 * sphimt * ct / S['sphi']
    f2i = rho * W * sphimt / S['sphi']
    g_scalar = rho * S['un'] * S['u'] + (p - pa) * S['nx']
    m_scalar = rho * S['un']
    ok &= check('C3a g ds = f1 dy', is_zero(g_scalar / S['sphi'] - f1))
    ok &= check('C3b (rho u_n) ds = f2^i dy',
                is_zero(m_scalar / S['sphi'] - f2i))

    # C4 Fredholm closure identity: d . r = 0 identically (all lambda2)
    dr = (S['d'].T * S['r'])[0, 0]
    ok &= check('C4 d . r = 0 identically (adjoint closure on the '
                'characteristic)', is_zero(dr))

    # C5 (structure, carried by C2+C4 + the numeric rank certificate):
    # rank K = 3 with l spanning ker K^T means psi^T K = -d^T is
    # solvable IFF d.r = 0 (C4), with solution affine space
    # psi_p + t*l — the gauge t is fixed only by the interior adjoint
    # transport along the tangent characteristic.  No symbolic solve
    # needed: every check below holds for EVERY solution psi.
    print('  [C5 adjoint trace = psi_p + t*l (Fredholm C4 + rank-3 '
          'certificate in the numeric section)]', flush=True)

    # C6 the boundary-datum reading lemma: w with grad(mass).w = 1,
    # grad(thrust).w = 0 (w3 = w4 = 0 representative); then for EVERY
    # adjoint solution, Lambda(psi) := psi.(K w) = psi^T K w = -d.w =
    # -lambda2.  Computed in the Weierstrass domain (rational functions
    # of (t, u)) for tractability; C6c/C6d are then PROVED COROLLARIES:
    #   C6c gauge independence kappa.l = (l^T K) w = 0 by C2b;
    #   C6d Lambda = -d.w = -(grad g + lambda2 grad m).w = -lambda2 by
    #       C6b and linearity.
    # The nondegeneracy of kappa is certified numerically (C6e below is
    # evaluated in the numeric-oracle section via kappa at the oracle).
    w1, w2 = sp.symbols('w1 w2')
    dm_w = sp.Matrix([sp.cancel(x.subs(_WEIER)) for x in S['d_m']])
    dg_w = sp.Matrix([sp.cancel(x.subs(_WEIER)) for x in S['d_g']])
    sol = sp.solve([dm_w[0] * w1 + dm_w[1] * w2 - 1,
                    dg_w[0] * w1 + dg_w[1] * w2], [w1, w2], dict=True)
    ok &= check('C6a normalized probe w exists', len(sol) == 1)
    wv = sp.Matrix([sp.cancel(sol[0][w1]), sp.cancel(sol[0][w2]), 0, 0])
    res_m = sp.cancel(sp.together(dm_w[0] * wv[0] + dm_w[1] * wv[1] - 1))
    res_g = sp.cancel(sp.together(dg_w[0] * wv[0] + dg_w[1] * wv[1]))
    ok &= check('C6b normalization verified: grad(m).w = 1, grad(g).w = 0',
                res_m == 0 and res_g == 0)
    print('  [C6c gauge independence kappa.l = (l^T K) w = 0: PROVED '
          'COROLLARY of C2b]', flush=True)
    print('  [C6d Lambda(psi) = psi.(K w) = -d.w = -lambda2 for EVERY '
          'adjoint solution: PROVED COROLLARY of C6b + linearity]',
          flush=True)
    print('      => with (L.12) [lambda2 = -f2, THEOREM]: psi.(K w) = f2'
          ' = W cos(theta %s alpha)/cos(alpha) on the optimal Sigma'
          % ('-' if side > 0 else '+'), flush=True)
    return ok, wv


def numeric_controls():
    """Negative controls + declared gamma=const oracle instantiation."""
    print('== negative controls + numeric oracle (gamma = 1.23, DECLARED '
          'perfect-gas instance) ==')
    import math
    ok = True
    EPS = sys.float_info.epsilon
    K_OPS = 1024.0                                # derived in the docstring

    gam = 1.23
    for side, Mn, th_deg, tag in ((-1, 2.4, -8.25, 'C-/plug (Rao-1961 '
                                   'spike oracle regime)'),
                                  (+1, 2.2, 8.0, 'C+/bell regime')):
        S = build(side)
        al = math.asin(1.0 / Mn)
        th = math.radians(th_deg)
        rhov, pv = 1.2, 1.0e5
        cv = math.sqrt(gam * pv / rhov)
        subs = {rho: rhov, p: pv, pa: 0.7e5, W: Mn * cv,
                e0: pv / ((gam - 1.0) * rhov), b: gam - 1.0,
                st: math.sin(th), ct: math.cos(th),
                sa: math.sin(al), ca: math.cos(al), lam2: 0.3}
        scale = pv / rhov * Mn                    # magnitude of d.r terms
        tol = K_OPS * EPS * scale
        dr = float((S['d'].T * S['r'])[0, 0].subs(subs))
        good = abs(dr) <= tol
        print('  [oracle %s] d.r = %.3e (tol %.3e): %s'
              % (tag, dr, tol, 'PASS' if good else 'FAIL'))
        ok &= good

        # rank-3 certificate: exactly one vanishing singular value of K
        import numpy as _np
        Knum = _np.array(S['K'].subs(subs), dtype=float)
        sv = _np.linalg.svd(Knum, compute_uv=False)
        good = sv[2] > K_OPS * EPS * sv[0] and sv[3] <= K_OPS * EPS * sv[0]
        print('  [oracle %s] rank K = 3 (sv/sv0: %s): %s'
              % (tag, ' '.join('%.1e' % (x / sv[0]) for x in sv),
                 'PASS' if good else 'FAIL'))
        ok &= good

        # NC3: corrupted kernel vector (H -> h) must FAIL K r = 0
        r_bad = S['r'].copy()
        r_bad[3] = S['h'] - S['c']**2
        Krb = (S['K'] * r_bad).subs(subs)
        worst = max(abs(float(x)) for x in Krb)
        rej = worst > K_OPS * EPS * scale
        print('  [NC3 %s] corrupted kernel |K r_bad| = %.3e: %s'
              % (tag, worst, 'REJECTED (PASS)' if rej
                 else 'NOT rejected (FAIL)'))
        ok &= rej

        # NC2: datum without the pressure term must FAIL d.r = 0
        # (corrupted datum: g_corr = rho u_n u only, p n_x term dropped)
        U1, U2, U3, U4 = sp.symbols('U1 U2 U3 U4')
        Uv = sp.Matrix([U1, U2, U3, U4])
        m_expr = U2 * S['nx'] + U3 * S['ny']
        g_corr = m_expr * U2 / U1
        d_corr = sp.Matrix([sp.diff(g_corr, x) for x in Uv]).subs(S['point'])
        drc = float((d_corr.T * S['r'])[0, 0].subs(subs))
        rej = abs(drc) > tol
        print('  [NC2 %s] pressure term dropped: d_corr.r = %.3e: %s'
              % (tag, drc, 'REJECTED (PASS)' if rej
                 else 'NOT rejected (FAIL)'))
        ok &= rej

        # NC1: non-characteristic surface (phi shifted by 0.1 rad):
        # det K != 0 -> no closure freedom
        dphi = 0.1
        sphi = math.sin(th + side * al + dphi)
        cphi = math.cos(th + side * al + dphi)
        # rebuild K numerically with the shifted normal
        subs_nc = dict(subs)
        # exploit: K depends on the normal only through nx, ny; rebuild
        Anum = S['A'].subs(subs)
        Bnum = S['B'].subs(subs)
        Knc = sp.Matrix(Anum) * sphi + sp.Matrix(Bnum) * (-cphi)
        detv = abs(float(Knc.det()))
        det_scale = (cv * Mn) ** 4                # det ~ (velocity)^4 scale
        rej = detv > K_OPS * EPS * det_scale
        print('  [NC1 %s] non-characteristic surface |det K| = %.3e '
              '(floor %.3e): %s' % (tag, detv, K_OPS * EPS * det_scale,
                                    'REJECTED (PASS)' if rej
                                    else 'NOT rejected (FAIL)'))
        ok &= rej
    return ok


def numeric_c6(side, wv, tag):
    """C6e: numeric certificate at the oracle point — kappa = K w is
    nonzero, gauge-independent, and psi.kappa = -lambda2 on two gauges
    (psi_p from least squares + psi_p + l)."""
    import math

    import numpy as np
    ok = True
    EPS = sys.float_info.epsilon
    K_OPS = 1024.0
    gam = 1.23
    Mn, th_deg = (2.2, 8.0) if side > 0 else (2.4, -8.25)
    al = math.asin(1.0 / Mn)
    th = math.radians(th_deg)
    rhov, pv = 1.2, 1.0e5
    cv = math.sqrt(gam * pv / rhov)
    lam2v = 0.3
    S = build(side)
    subs = {rho: rhov, p: pv, pa: 0.7e5, W: Mn * cv,
            e0: pv / ((gam - 1.0) * rhov), b: gam - 1.0,
            st: math.sin(th), ct: math.cos(th),
            sa: math.sin(al), ca: math.cos(al), lam2: lam2v,
            _T: math.tan(th / 2.0), _U: math.tan(al / 2.0)}
    Kn = np.array(S['K'].subs(subs), dtype=float)
    ln = np.array(S['l'].subs(subs), dtype=float).ravel()
    dn = np.array(S['d'].subs(subs), dtype=float).ravel()
    wn = np.array(wv.subs(subs), dtype=float).ravel()
    kap = Kn @ wn
    scale = float(np.max(np.abs(Kn)) * np.max(np.abs(wn)))
    tol = K_OPS * EPS * scale
    good = np.linalg.norm(kap) > 1e3 * tol
    print('  [C6e %s] kappa nondegenerate |kappa| = %.3e (floor %.3e): %s'
          % (tag, np.linalg.norm(kap), 1e3 * tol,
             'PASS' if good else 'FAIL'))
    ok &= good
    good = abs(kap @ ln) <= K_OPS * EPS * float(
        np.linalg.norm(kap) * np.linalg.norm(ln))
    print('  [C6e %s] kappa . l = %.3e: %s'
          % (tag, kap @ ln, 'PASS' if good else 'FAIL'))
    ok &= good
    psi_p = np.linalg.lstsq(Kn.T, -dn, rcond=None)[0]
    # conditioning-aware bar: lstsq error ~ eps * (sv0/sv2) on a rank-3
    # system; the dot products add |psi||kappa| roundoff
    sv = np.linalg.svd(Kn, compute_uv=False)
    tol_lam = K_OPS * EPS * (sv[0] / sv[2]) * max(
        1.0, abs(lam2v), float(np.abs(psi_p) @ np.abs(kap)))
    for gname, psi in (('psi_p', psi_p), ('psi_p + l', psi_p + ln)):
        lamr = -(psi @ kap)
        good = abs(lamr - lam2v) <= tol_lam
        print('  [C6e %s] Lambda(%s) = -psi.kappa -> lambda2: '
              '%.12f vs %.2f: %s' % (tag, gname, lamr, lam2v,
                                     'PASS' if good else 'FAIL'))
        ok &= good
    return ok


def main():
    print('== P-A1 standalone symbolic pass (EOS-general core; sympy %s) =='
          % sp.__version__)
    ok = True
    ok_p, wv_p = run_side(+1, 'C+ (bell/shroud)')
    ok &= ok_p
    ok_m, wv_m = run_side(-1, 'C- (plug/spike)')
    ok &= ok_m
    ok &= numeric_c6(+1, wv_p, 'C+')
    ok &= numeric_c6(-1, wv_m, 'C-')
    ok &= numeric_controls()
    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
