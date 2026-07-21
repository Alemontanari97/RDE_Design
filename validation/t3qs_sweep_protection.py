"""T3-QS — quasi-steady protection of the collapse class (symbolic carrier).

CLAIM (T3-QS, algebraic core; interpretation within the P4 first-order
framework J-CT1): on a T3-ray data family, the first-order sweep
correction J1 = -<psi_J, S_sweep W0> has integrand proportional to
k'(xi) with a PHASE-INDEPENDENT prefactor, hence its cycle integral
vanishes on the smooth part of the cycle and reduces to the data-jump
(wave-passage) residue:  J1 = <psi_hat, Z> * [k]_jump.

Proof chain verified here, EOS-general (ideal gas, ARBITRARY caloric
e(T) — the frozen gamma(T) rung):
 P1  RAY: the T3 scaling (rho -> k rho at fixed u,v,w,T) is LINEAR in
     conservative variables: W -> kW. (Conservative form of Lemma T3-A.)
 P2  HOMOGENEITY: Euler fluxes in any direction, the axisymmetric
     geometric source, and the Rankine-Hugoniot jump relations are
     degree-1 homogeneous along the ray: F(kW) = k F(W); RH is
     k-invariant (fitted-sheet position unchanged on the ray).
 P3  JACOBIAN INVARIANCE (Euler's theorem): differentiating
     F(kW) = kF(W) in W gives A(kW) = A(W) — the linearized (and hence
     adjoint) operator is IDENTICAL at every phase of the ray.
     Verified two routes: symbolic corollary + numeric Jacobians.
 P4  OBJECTIVE-GRADIENT INVARIANCE: the thrust surface integrand is
     (degree-1 homogeneous) - Pa*nx, so its W-gradient is invariant:
     the adjoint SOURCE is phase-independent. With P3 and the
     T3-class BC structure (H3: geometry and (M,theta) field
     phase-invariant), the per-phase adjoint is one fixed field
     psi_hat.  [Uniqueness of the linear adjoint solve = the S1
     apparatus; assembled corollary, stated.]
 P5  SWEEP FACTORIZATION: W0(theta) = k(theta) What  ==>
     S_sweep := (1/r) d_theta [F_theta(W0) - Omega r W0]
              = k'(theta) * Z(x,r),   Z fixed.
 P6  CYCLE INTEGRAL: for smooth periodic k, Int_0^1 k' dxi = 0
     (exact); for the blowdown sawtooth the smooth-part integral
     equals -[k]_jump: J1 concentrates at the wave passage.

REJECTORS (each must FAIL detectably):
 R1  non-ray direction (T scaled too): Jacobian invariance BREAKS.
 R2  H3 violated (What depends on theta): factorization BREAKS.
 R3  objective non-affine in Pa ((p-Pa)^2): gradient invariance BREAKS.

Scope boundary (declared): single-parameter ray cycles (Pc-only) —
EOS-general; two-parameter cycles ((P0,T0) both varying) leave the
ray, the integrand becomes a generically non-exact 1-form and J1 is
the area integral of its exterior derivative over the data loop.
"""
import sys
import time

import numpy as np
import sympy as sp

t00 = time.time()
ok_all = True


def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print('  %-64s %s' % (label, 'PASS' if cond else 'FAIL'))
    return cond


# ---------------------------------------------------------------- symbols
rho, u, v, w, T, R, k, Pa = sp.symbols('rho u v w T R k Pa', positive=True)
nx, ny, nz, sig = sp.symbols('n_x n_y n_z sigma', real=True)
e = sp.Function('e', positive=True)  # arbitrary caloric e(T): EOS-general

q2 = (u**2 + v**2 + w**2) / 2
E = e(T) + q2
p = rho * R * T

# conservative vector and generic-direction flux (primitive parametrization)
W = sp.Matrix([rho, rho*u, rho*v, rho*w, rho*E])
un = u*nx + v*ny + w*nz
F = sp.Matrix([rho*un,
               rho*un*u + p*nx,
               rho*un*v + p*ny,
               rho*un*w + p*nz,
               (rho*E + p)*un])
# axisymmetric geometric source (per-phase operator's H): ~ (1/r) * (...)
Hsrc = sp.Matrix([rho*v, rho*u*v, rho*v**2, rho*v*w, (rho*E + p)*v])

scale = {rho: k*rho}          # the T3 ray: rho -> k rho, (u,v,w,T) fixed

print('== T3-QS symbolic carrier (EOS-general: arbitrary e(T)) ==')

# P1 — ray linearity in conservative variables
check('(P1) W(S_k state) == k * W(state)  [conservative ray]',
      sp.simplify(W.subs(scale) - k*W) == sp.zeros(5, 1))

# P2 — degree-1 homogeneity: flux (generic n), source, RH
check('(P2a) F(kW) == k F(W)  (generic direction, e(T) arbitrary)',
      sp.simplify(F.subs(scale) - k*F) == sp.zeros(5, 1))
check('(P2b) axisym source H(kW) == k H(W)',
      sp.simplify(Hsrc.subs(scale) - k*Hsrc) == sp.zeros(5, 1))
# RH: F(WL)-F(WR)-sig*(WL-WR) scales by k => sheet position k-invariant
rhoL, uL, vL, wL, TL = sp.symbols('rho_L u_L v_L w_L T_L', positive=True)
subsR = {rho: rhoL, u: uL, v: vL, w: wL, T: TL}
FL, WL_ = F.subs(subsR), W.subs(subsR)
RH = (F - FL) - sig*(W - WL_)
RHs = RH.subs({rho: k*rho, rhoL: k*rhoL})
check('(P2c) RH(kWL,kWR,sigma) == k RH(WL,WR,sigma)  [sheet k-invariant]',
      sp.simplify(RHs - k*RH) == sp.zeros(5, 1))

# P3 — Jacobian invariance.
# Route 1 (symbolic corollary, Euler's theorem): d/dW of F(kW)=kF(W)
# gives A(kW)*k = k*A(W). Exhibited by differentiating both sides in the
# PRIMITIVE parametrization along the ray tangent:
Vp = sp.Matrix([rho, u, v, w, T])
J_F_prim = F.jacobian(Vp)               # dF/d(prim)
J_W_prim = W.jacobian(Vp)               # dW/d(prim)
lhs = sp.simplify(J_F_prim.subs(scale) - (k*J_F_prim).applyfunc(
    lambda x: x))                        # placeholder; real check below
# The invariant object is A = dF/dW = (dF/dprim)(dW/dprim)^{-1}.
A_sym = sp.simplify(J_F_prim * J_W_prim.inv())
A_scaled = sp.simplify(A_sym.subs(scale))
check('(P3a) A(kW) == A(W) symbolically  [adjoint operator invariant]',
      sp.simplify(A_scaled - A_sym) == sp.zeros(5, 5))

# Route 2 (numeric dual-route): conservative-variable Jacobians by FD.
gamma_num = sp.Rational(7, 5)


def econ(Tv):                            # a concrete nonlinear e(T)
    return 717.0*Tv + 0.05*Tv**2         # calorically IMPERFECT


def state_to_cons(rv, uv, vv, wv, Tv):
    Ev = econ(Tv) + (uv*uv + vv*vv + wv*wv)/2
    return np.array([rv, rv*uv, rv*vv, rv*wv, rv*Ev])


def cons_to_flux(c, n, Rg=287.0):
    r0, m1, m2, m3, Et = c
    uv, vv, wv = m1/r0, m2/r0, m3/r0
    ev = Et/r0 - (uv*uv + vv*vv + wv*wv)/2
    # invert e(T): Newton on econ(T)=ev
    Tv = ev/717.0
    for _ in range(60):
        Tv -= (econ(Tv) - ev)/(717.0 + 0.1*Tv)
    pv = r0*Rg*Tv
    unv = uv*n[0] + vv*n[1] + wv*n[2]
    return np.array([r0*unv,
                     r0*unv*uv + pv*n[0],
                     r0*unv*vv + pv*n[1],
                     r0*unv*wv + pv*n[2],
                     (Et + pv)*unv])


def num_jac(c, n, h=1e-6):
    A = np.zeros((5, 5))
    f0 = cons_to_flux(c, n)
    for j in range(5):
        cp = c.copy(); cp[j] += h*max(1.0, abs(c[j]))
        A[:, j] = (cons_to_flux(cp, n) - f0)/(h*max(1.0, abs(c[j])))
    return A

rng = np.random.default_rng(7)
worst = 0.0
for _ in range(20):
    st = (rng.uniform(0.2, 2.0), rng.uniform(50, 900), rng.uniform(-300, 300),
          rng.uniform(-1500, 1500), rng.uniform(300, 2800))
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    c = state_to_cons(*st)
    for kk in (0.3, 2.5, 7.0):
        d = np.abs(num_jac(kk*c, n) - num_jac(c, n)).max()
        scale_ref = np.abs(num_jac(c, n)).max()
        worst = max(worst, d/scale_ref)
tol_fd = 5e-5                            # derived: O(h) FD asymmetry bound
check('(P3b) numeric A(kW)==A(W), 20 states x 3 k, rel err %.1e <= %.0e'
      % (worst, tol_fd), worst <= tol_fd)

# P4 — objective-gradient invariance: g = [p*nx + rho*un*u] - Pa*nx
g_hom = p*nx + rho*un*u                  # degree-1 homogeneous part
check('(P4a) homogeneous part: g_hom(kW) == k g_hom(W)',
      sp.simplify(g_hom.subs(scale) - k*g_hom) == 0)
grad_g = sp.Matrix([g_hom - Pa*nx]).jacobian(Vp) * J_W_prim.inv()
grad_gs = sp.simplify(grad_g.subs(scale))
check('(P4b) d(g - Pa nx)/dW invariant along ray  [adjoint source fixed]',
      sp.simplify(grad_gs - grad_g) == sp.zeros(1, 5))

# P5 — sweep factorization on the ray family
th, r_, Om = sp.symbols('theta r Omega', positive=True)
kf = sp.Function('k', positive=True)
Fth = F.subs({nx: 0, ny: 0, nz: 1})      # azimuthal flux (unit e_theta)
W0 = kf(th)*W                            # H3: What has NO theta-dependence
Fth0 = sp.simplify(Fth.subs(scale).subs(k, kf(th)))   # F_theta(k(th) W)
Ssweep = sp.simplify(sp.diff(Fth0 - Om*r_*W0, th)/r_)
Zfix = sp.simplify((Fth - Om*r_*W)/r_)
check('(P5) S_sweep(k(th) What) == k\'(th) * Z,  Z theta-independent',
      sp.simplify(Ssweep - sp.diff(kf(th), th)*Zfix) == sp.zeros(5, 1))

# P6 — cycle integral: smooth periodic -> 0; sawtooth -> -[k]
xi, a1, b1, a2 = sp.symbols('xi a1 b1 a2', real=True)
ksm = 1 + a1*sp.cos(2*sp.pi*xi) + b1*sp.sin(2*sp.pi*xi) \
        + a2*sp.cos(4*sp.pi*xi)
check('(P6a) smooth periodic:  Int_0^1 k\'(xi) dxi == 0  exactly',
      sp.simplify(sp.integrate(sp.diff(ksm, xi), (xi, 0, 1))) == 0)
PR = sp.symbols('PR', positive=True)
ksaw = PR**(-xi)                          # blowdown decay, jump at xi=0
Ismooth = sp.simplify(sp.integrate(sp.diff(ksaw, xi), (xi, 0, 1)))
jump = sp.simplify(ksaw.subs(xi, 0) - ksaw.subs(xi, 1))   # [k] at passage
check('(P6b) sawtooth: smooth-part integral == -[k]_jump  (wave passage)',
      sp.simplify(Ismooth + jump) == 0)

# ---------------------------------------------------------------- rejectors
print('-- rejectors (each must be REJECTED) --')
# R1: non-ray direction (T scaled too) -> Jacobian invariance must break
worst_r1 = 0.0
for _ in range(6):
    st = (1.0, 400.0, 80.0, -900.0, 1500.0)
    c = state_to_cons(*st)
    c2 = state_to_cons(st[0]*2.0, st[1], st[2], st[3], st[4]*2.0)  # rho,T x2
    n = np.array([1.0, 0.0, 0.0])
    worst_r1 = max(worst_r1,
                   np.abs(num_jac(c2, n) - num_jac(c, n)).max()
                   / np.abs(num_jac(c, n)).max())
check('[R1] non-ray (T scaled): invariance BREAKS (rel dev %.2f >> tol)'
      % worst_r1, worst_r1 > 1e3*tol_fd)
# R2: H3 violated -> factorization must break
eps = sp.symbols('epsilon', positive=True)
W0b = kf(th)*W*(1 + eps*sp.sin(th))
Fthb = sp.simplify(Fth.subs(scale).subs(k, kf(th)*(1 + eps*sp.sin(th))))
Sb = sp.simplify(sp.diff(Fthb - Om*r_*W0b, th)/r_)
resid = sp.simplify(Sb - sp.diff(kf(th), th)*Zfix)
check('[R2] H3 violated (What theta-dep): S_sweep != k\'Z  (extra term)',
      sp.simplify(resid) != sp.zeros(5, 1))
# R3: non-affine objective -> gradient invariance must break
g_bad = (p - Pa)**2 * nx
grad_bad = sp.Matrix([g_bad]).jacobian(Vp) * J_W_prim.inv()
diff_bad = sp.simplify(grad_bad.subs(scale) - grad_bad)
check('[R3] objective (p-Pa)^2: gradient invariance BREAKS',
      sp.simplify(diff_bad) != sp.zeros(1, 5))

print('-- assembled corollary (stated) --')
print('  P3+P4 + H3 BC structure => per-phase adjoint psi_J(xi) == psi_hat')
print('  (one fixed field; uniqueness of the linear adjoint solve, S1).')
print('  Hence J1 = -<psi_hat, Z> * Int k\' dxi = <psi_hat, Z>*[k]_jump :')
print('  ZERO on smooth ray cycles; wave-passage-localized on blowdown.')

dt = time.time() - t00
print('VERDICT: %s (%.1f s)' % ('PASS' if ok_all else 'FAIL', dt))
sys.exit(0 if ok_all else 1)
