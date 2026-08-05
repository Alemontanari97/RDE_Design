#!/usr/bin/env python3
"""[X-SLRW] Carrier for the rotating side-load lemma [T-SLRW]
(docs/rde_nozzle_side_load.md; S15 deep-foundations campaign, [RIGOR/A]).

SYMBOLIC part (sympy, exact):
  S1  m = 1 selection integral: Int_0^{2pi} e^{i(m+1)theta} dtheta =
      2pi iff m = -1, else 0 (checked exactly for m = -4..4).
  S2  n-fold null: a generic trig polynomial supported on multiples of
      n (n = 2, 3; symbolic coefficients) has ZERO transverse integral
      against e^{i theta} — exactly.
  S3  n = 1 structure: for a generic first-harmonic pattern
      a cos(theta - W t) + b sin(theta - W t), the transverse integral
      F(t) satisfies d|F|^2/dt == 0 and d/dt [F e^{-i W t}] == 0
      (constant modulus, rigid rotation at exactly W).
  S4  geometric kernels (proof step (i) of the lemma): on r = R(x),
      r_pos x (e_r - R' e_x) = (x + R R') e_theta exactly; its axial
      component is 0 (pressure cannot torque a surface of revolution)
      and its transverse combination is i e^{i theta} (x + R R') —
      pure m = 1.

NUMERIC part (numpy; FULL vector surface quadrature, independent of
the symbolic reduction; tolerances DERIVED, never magic):
  N1  n = 2 and n = 3 patterns WITH an azimuthal jump (sawtooth,
      shock-like): max over time samples of |F_perp| and |M_perp| is
      below the rigorous floating-point summation floor
      (len * eps * sum|terms|). With N_theta a multiple of n the
      discrete orthogonality is exact, so the null must hold to
      roundoff — jumps included.
  N2  axial-force constancy across time samples (smooth pattern,
      spectrally resolved: aliasing below roundoff) — the [T-T0]
      companion line.
  N3  n = 1 smooth pattern: modulus constant across 7 time samples
      (roundoff floor) + phase advance arg F(t2)-arg F(t1) = W dt
      + DUAL ROUTE: full vector quadrature vs 2pi e^{iWt} *
      Int R conj(c1) dx with c1 from an FFT — agreement within the
      derived band.
REJECTORS (each must DETECT its breakage, else this carrier FAILS):
  R1  counter-rotating pair: nonzero side load with PULSATING modulus
      (elliptical orbit) must be detected.
  R2  two co-rotating waves with unequal amplitudes (1 vs 1.3):
      nonzero CONSTANT-modulus rotating side load must be detected.
  R3  corrupted geometric kernel e^{i 2 theta} on the n = 2 null
      pattern: must report nonzero (guards against a degenerate
      always-zero implementation).

Exit 0 iff all checks AND all rejectors pass. Terminal line:
"VERDICT: PASS" / "VERDICT: FAIL".
Measured runtime: seconds-scale (fast tier, suite group (xiii)).
"""
import sys

import numpy as np
import sympy as sp


# ---------------------------------------------------------------- symbolic
def sym_checks():
    ok = True
    th, t, W = sp.symbols('theta t Omega', real=True)
    I = sp.I

    # S1: selection integral, exact, m = -4..4
    s1 = True
    for m in range(-4, 5):
        val = sp.integrate(sp.exp(I * (m + 1) * th), (th, 0, 2 * sp.pi))
        want = 2 * sp.pi if m == -1 else 0
        s1 &= sp.simplify(val - want) == 0
    print('  S1 selection Int e^{i(m+1)th} = 2pi*delta(m,-1), m=-4..4: %s'
          % ('PASS' if s1 else 'FAIL'))
    ok &= s1

    # S2: n-fold pattern (multiples of n only) -> zero m=1 line, n=2,3
    s2 = True
    a1, a2, a3, b1, b2, b3 = sp.symbols('a1 a2 a3 b1 b2 b3', real=True)
    for n in (2, 3):
        p = sum(a * sp.cos(k * n * th) + b * sp.sin(k * n * th)
                for k, (a, b) in enumerate(((a1, b1), (a2, b2), (a3, b3)),
                                           start=1))
        val = sp.integrate(p * sp.exp(I * th), (th, 0, 2 * sp.pi))
        s2 &= sp.simplify(val) == 0
    print('  S2 n-fold pattern kills the m=1 line (n=2,3, symbolic):    %s'
          % ('PASS' if s2 else 'FAIL'))
    ok &= s2

    # S3: n = 1 constant modulus + rigid rotation at exactly W
    a, b = sp.symbols('a b', real=True)
    p1 = a * sp.cos(th - W * t) + b * sp.sin(th - W * t)
    F = sp.integrate(p1 * sp.exp(I * th), (th, 0, 2 * sp.pi))
    mod2 = sp.simplify(sp.expand(F * sp.conjugate(F)))
    c1 = sp.simplify(sp.diff(mod2, t)) == 0
    c2 = sp.simplify(sp.diff(F * sp.exp(-I * W * t), t)) == 0
    Fval = sp.simplify(F - sp.pi * (a + I * b) * sp.exp(I * W * t)) == 0
    s3 = c1 and c2 and Fval
    print('  S3 n=1: |F| const, F = pi(a+ib)e^{iWt} rigid at W:         %s'
          % ('PASS' if s3 else 'FAIL'))
    ok &= s3

    # S4: geometric kernels: r x (e_r - R' e_x) = (x+RR') e_theta;
    #     axial component 0; transverse combo i e^{i th} (x+RR')
    x, R, Rp = sp.symbols('x R Rprime', real=True)
    e_r = sp.Matrix([0, sp.cos(th), sp.sin(th)])
    e_x = sp.Matrix([1, 0, 0])
    r_pos = x * e_x + R * e_r
    kern = r_pos.cross(e_r - Rp * e_x)
    e_thv = sp.Matrix([0, -sp.sin(th), sp.cos(th)])
    diff = kern - (x + R * Rp) * e_thv
    s4 = all(sp.simplify(sp.expand_trig(d)) == 0 for d in diff)
    s4 = s4 and sp.simplify(kern[0]) == 0
    combo = sp.simplify(sp.expand_complex(
        kern[1] + I * kern[2] - I * sp.exp(I * th) * (x + R * Rp))) == 0
    s4 = s4 and combo
    print('  S4 moment kernel = (x+RR")e_th; M_x == 0; combo i e^{ith}: %s'
          % ('PASS' if s4 else 'FAIL'))
    ok &= s4
    return ok


# ----------------------------------------------------------------- numeric
# Surface: r = R(x) on [0,1], generic (R' != 0, non-monotone).
def R_of(x):
    return 1.0 + 0.5 * x + 0.2 * np.sin(2.0 * x)


def Rp_of(x):
    return 0.5 + 0.4 * np.cos(2.0 * x)


def amp(x):
    return 1.0 + 0.3 * np.sin(3.0 * x)


def base_smooth(phi):
    # entire azimuthal profile, super-exponentially decaying spectrum
    return np.exp(np.cos(phi)) - 1.0


def base_jump(phi):
    # sawtooth: jump at phi = 0 (mod 2pi) — shock-like trace
    return np.mod(phi, 2.0 * np.pi) / (2.0 * np.pi)


def pattern(phi, n, base):
    out = np.zeros_like(phi)
    for k in range(n):
        out = out + base(phi - 2.0 * np.pi * k / n)
    return out


def trap_weights(x):
    h = x[1] - x[0]
    w = np.full(x.size, h)
    w[0] = w[-1] = 0.5 * h
    return w


def perp_of_field(Pfun, Omega, tsamp, Nx=161, Nth=384):
    """F_perp(t) by full quadrature for an arbitrary trace P(x, th, t).

    Returns (list of complex F_perp, derived roundoff floor)."""
    x = np.linspace(0.0, 1.0, Nx)
    th = np.arange(Nth) * (2.0 * np.pi / Nth)
    X, TH = np.meshgrid(x, th, indexing='ij')
    R = R_of(X)
    wx = trap_weights(x)
    out, floor = [], 0.0
    for t in tsamp:
        common = Pfun(X, TH, t) * R * (2.0 * np.pi / Nth) * wx[:, None]
        out.append(np.sum(common * np.cos(TH))
                   + 1j * np.sum(common * np.sin(TH)))
        floor = max(floor, common.size * np.finfo(float).eps
                    * np.sum(np.abs(common)))
    return out, floor


def loads(t, n, base, Omega, Nx=161, Nth=384, kernel_m=1):
    """Full vector quadrature of F and M on the surface of revolution.

    Returns (F (3,), M (3,), floor): floor = rigorous fl-summation
    bound len*eps*sum|term| over the worst component (DERIVED tol).
    kernel_m: azimuthal wavenumber of the transverse projection basis
    (1 = physical; 2 = corrupted-kernel rejector R3)."""
    x = np.linspace(0.0, 1.0, Nx)
    th = np.arange(Nth) * (2.0 * np.pi / Nth)          # periodic trapezoid
    X, TH = np.meshgrid(x, th, indexing='ij')
    R, RP = R_of(X), Rp_of(X)
    P = amp(X) * pattern(TH - Omega * t, n, base)
    wx = trap_weights(x)                                # trapezoid weights
    dth = 2.0 * np.pi / Nth
    # dF = p R (e_r - R' e_x) dth dx ; e_r=(0,cos,sin), e_x=(1,0,0)
    common = P * R * dth * wx[:, None]
    cth, sth = np.cos(kernel_m * TH), np.sin(kernel_m * TH)
    Fx = np.sum(common * (-RP))
    Fy = np.sum(common * cth)
    Fz = np.sum(common * sth)
    # dM = p R (x + R R') e_theta dth dx ; e_th=(0,-sin,cos)
    wm = common * (X + R * RP)
    Mx = 0.0 * np.sum(wm)
    My = np.sum(wm * (-sth))
    Mz = np.sum(wm * cth)
    n_terms = common.size
    floor = n_terms * np.finfo(float).eps * max(
        np.sum(np.abs(common)), np.sum(np.abs(wm)))
    return np.array([Fx, Fy, Fz]), np.array([Mx, My, Mz]), floor


def perp(v):
    return v[1] + 1j * v[2]


def num_checks():
    ok = True
    Omega = 3.0
    tsamp = np.linspace(0.0, 2.0 * np.pi / Omega, 7, endpoint=False)

    # N1: n = 2, 3 null with the JUMP pattern, identically in t
    n1 = True
    worst = 0.0
    floor0 = None
    for n in (2, 3):
        for t in tsamp:
            F, M, floor = loads(t, n, base_jump, Omega)
            floor0 = floor if floor0 is None else max(floor0, floor)
            worst = max(worst, abs(perp(F)), abs(perp(M)))
    n1 = worst <= floor0
    print('  N1 n=2,3 jump pattern: max|F_perp|,|M_perp| = %.2e <= '
          'floor %.2e: %s' % (worst, floor0, 'PASS' if n1 else 'FAIL'))
    ok &= n1

    # N2: axial-force constancy (smooth pattern, n = 1 and n = 3)
    n2 = True
    for n in (1, 3):
        Fxs = []
        for t in tsamp:
            F, _, floor = loads(t, n, base_smooth, Omega)
            Fxs.append(F[0])
        spread = max(Fxs) - min(Fxs)
        n2 &= spread <= floor
    print('  N2 axial force constant in t (spread <= floor, n=1,3):     %s'
          % ('PASS' if n2 else 'FAIL'))
    ok &= n2

    # N3: n = 1 constant modulus + phase advance + FFT dual route
    mods, args, Fs = [], [], []
    for t in tsamp:
        F, _, floor = loads(t, 1, base_smooth, Omega)
        Fp = perp(F)
        mods.append(abs(Fp))
        args.append(np.angle(Fp))
        Fs.append(Fp)
    mod_spread = max(mods) - min(mods)
    c_mod = mod_spread <= floor
    dt = tsamp[1] - tsamp[0]
    dphase = np.angle(np.array(Fs[1:]) / np.array(Fs[:-1]))
    c_phase = np.max(np.abs(dphase - Omega * dt)) <= floor / min(mods)
    # dual route: 2pi e^{iWt} Int R conj(c1) dx, c1 from FFT at t = 0
    x = np.linspace(0.0, 1.0, 161)
    Nth = 384
    th = np.arange(Nth) * (2.0 * np.pi / Nth)
    Pxth = amp(x[:, None]) * pattern(th[None, :], 1, base_smooth)
    c1 = np.fft.fft(Pxth, axis=1)[:, 1] / Nth       # c_1(x) per station
    red = 2.0 * np.pi * np.trapezoid(R_of(x) * np.conj(c1), x)
    dual = abs(Fs[0] - red)
    band = max(floor, abs(red) * 1e2 * np.finfo(float).eps)
    c_dual = dual <= band
    n3 = c_mod and c_phase and c_dual
    print('  N3 n=1: |F| const (%.1e), phase = W dt, dual-route FFT '
          '(%.1e <= %.1e): %s'
          % (mod_spread, dual, band, 'PASS' if n3 else 'FAIL'))
    ok &= n3
    return ok, floor0 if floor0 is not None else 0.0


def rejectors():
    """Each breakage must be DETECTED (nonzero where the class says zero)."""
    ok = True
    Omega = 3.0
    tsamp = np.linspace(0.0, 2.0 * np.pi / Omega, 9, endpoint=False)

    # R1 counter-rotating pair: nonzero + pulsating modulus
    def p_counter(X, TH, t):
        return amp(X) * (base_smooth(TH - Omega * t)
                         + base_smooth(TH + Omega * t + 0.7))
    Fs, floor = perp_of_field(p_counter, Omega, tsamp)
    mods = [abs(F) for F in Fs]
    margin = 1.0e3 * floor        # detection = orders above the null band
    r1 = (max(mods) > margin) and ((max(mods) - min(mods)) > margin)
    print('  R1 counter-rotating pair DETECTED (max %.2e, pulsation '
          '%.2e > %.1e): %s' % (max(mods), max(mods) - min(mods), margin,
                                'PASS' if r1 else 'FAIL'))
    ok &= r1

    # R2 unequal co-rotating amplitudes: nonzero, CONSTANT modulus
    def p_unequal(X, TH, t):
        return amp(X) * (base_smooth(TH - Omega * t)
                         + 1.3 * base_smooth(TH - Omega * t - np.pi))
    Fs, floor = perp_of_field(p_unequal, Omega, tsamp)
    mods = [abs(F) for F in Fs]
    margin = 1.0e3 * floor
    r2 = (max(mods) > margin) and ((max(mods) - min(mods)) <= 1.0e1 * floor)
    print('  R2 unequal amplitudes DETECTED, modulus constant '
          '(%.2e, spread %.1e): %s' % (max(mods), max(mods) - min(mods),
                                       'PASS' if r2 else 'FAIL'))
    ok &= r2

    # R3 corrupted kernel e^{i2th} on the n=2 null pattern: nonzero
    F, M, floor3 = loads(0.3, 2, base_smooth, Omega, kernel_m=2)
    r3 = abs(perp(F)) > 1.0e3 * floor3
    print('  R3 corrupted kernel m=2 on n=2 pattern reports %.2e > %.1e: %s'
          % (abs(perp(F)), 1.0e3 * floor3, 'PASS' if r3 else 'FAIL'))
    ok &= r3
    return ok


def main():
    print('[X-SLRW] rotating side-load lemma carrier (T-SLRW)')
    ok_sym = sym_checks()
    ok_num, _ = num_checks()
    ok_rej = rejectors()
    ok = ok_sym and ok_num and ok_rej
    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
