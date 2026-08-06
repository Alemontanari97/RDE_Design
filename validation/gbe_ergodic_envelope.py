#!/usr/bin/env python3
"""G-B ergodic-transfer envelope carrier [RIGOR/A, S16 tranche 2, T4]:
machine verification of the finite-dimensional bricks of the ergodic
G-B lemma (docs/rde_nozzle_GB_ergodic.md; registry [S-GBE], carrier
[X-GBE]).

WHAT THE LEMMA NEEDS FROM THIS CARRIER (doc §3-§4):
 (a) the per-(h0, s) thrust-velocity ENVELOPE V_env — the sup of the
     effective exhaust velocity c_eff = u + (p - Pa)/(rho u) over
     admissible exit states with the AXIAL-MARGIN constraint u >= c —
     equals the record's sonic-capped ideal (complete expansion to Pa
     on the supercritical branch, sonic exit otherwise): verified
     against the independent OP-0 ladder closed forms
     (src/thrust/bounds.py cf_ideal/cf_sonic, tested 18/18);
 (b) CONCAVITY of V_env(h0, s) (so the perspective F_env(m, e, sig) =
     m V_env(e/m, sig/m) is concave and Jensen transfers the pointwise
     bound to time/area averages):
       S1 symbolic (perfect gas): the supercritical branch
          V = sqrt(2(h0 - K exp(s/cp))) has V_h0h0 < 0 and
          det Hess = (K exp(s/cp)/cp^2) W^-2 > 0 — NSD, strict;
       S2 symbolic: the sonic branch c* + (p* - Pa)/(rho* c*) —
          Hessian minors checked symbolically on the domain;
       S3 numeric: the COMPOSITE envelope (branch switch at
          P0/Pa = NPR(1, g)) scanned for concavity across the seam
          (FD Hessians of the perspective F_env over a derived
          (m, e, sig) box; max eigenvalue below the derived FD floor).
  REJECTORS:
  (R1) a corrupted (convexified) branch function must be DETECTED
       non-concave by the same scan;
  (R2) a corrupted cap rule (naive uncapped ideal on subcritical
       states) must break the bounds.py cross-check.

Perfect gas gamma = 1.4 as DECLARED instantiation (EOS-general
statement in the doc; the h(s, p) convexity in s is EOS-general:
d2h/ds2 = T/cp > 0). Derived tolerances; no magic numbers.
"""
import math
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from src.thrust.bounds import cf_ideal, cf_sonic, npr_sonic  # noqa: E402

EPS = sys.float_info.epsilon
GAM = 1.4
R = 287.0
CP = GAM * R / (GAM - 1.0)
PREF, TREF = 1.0e5, 300.0


# ------------------------------------------------------------ envelope
def P0_of(h0, s):
    """Stagnation pressure from (h0, s): s = cp ln(T0/TREF) - R ln(P0/PREF)."""
    T0 = h0 / CP
    return PREF * np.exp((CP * np.log(T0 / TREF) - s) / R)


def V_sup(h0, s, Pa):
    """Complete isentropic expansion to Pa: sqrt(2(h0 - h(s, Pa)))."""
    Ta = TREF * np.exp((s + R * np.log(Pa / PREF)) / CP)
    return np.sqrt(np.maximum(2.0 * (h0 - CP * Ta), 0.0))


def V_son(h0, s, Pa):
    """Sonic-exit effective velocity c* + (p* - Pa)/(rho* c*)."""
    Tst = 2.0 * h0 / (CP * (GAM + 1.0))
    cst = np.sqrt((GAM - 1.0) * CP * Tst)
    pst = PREF * np.exp((CP * np.log(Tst / TREF) - s) / R)
    rst = pst / (R * Tst)
    return cst + (pst - Pa) / (rst * cst)


def V_env(h0, s, Pa):
    """The record's capped envelope: supercritical -> complete
    expansion; subcritical -> sonic exit."""
    sup = P0_of(h0, s) / Pa >= npr_sonic(GAM)
    return np.where(sup, V_sup(h0, s, Pa), V_son(h0, s, Pa))


def F_env(m, e, sig, Pa, V=V_env):
    return m * V(e / m, sig / m, Pa)


# ------------------------------------------------------------ checks
def s1_symbolic():
    ok = True
    h0, s, cp, K = sp.symbols('h0 s c_p K', positive=True)
    E = K * sp.exp(s / cp)
    V = sp.sqrt(2 * (h0 - E))
    H = sp.hessian(V, (h0, s))
    v11 = sp.simplify(H[0, 0] * (2 * (h0 - E)) ** sp.Rational(3, 2))
    good = sp.simplify(v11 + 1) == 0          # V_h0h0 = -W^{-3/2}
    print('  (S1) supercritical V_h0h0 == -W^(-3/2):      %s'
          % ('PASS' if good else 'FAIL'))
    ok &= good
    det = sp.simplify(H[0, 0] * H[1, 1] - H[0, 1] ** 2)
    target = E / (cp ** 2 * (2 * (h0 - E)) ** 2)
    good = sp.simplify(det - target) == 0
    print('  (S1) supercritical det Hess == E/(cp^2 W^2):  %s'
          % ('PASS' if good else 'FAIL'))
    ok &= good

    # S2: sonic branch, symbolic minors on the domain (Pa, refs symbolic)
    Pa, Pr, Tr, Rg = sp.symbols('P_a P_r T_r R_g', positive=True)
    gam = sp.Rational(7, 5)
    cps = gam * Rg / (gam - 1)
    Tst = 2 * h0 / (cps * (gam + 1))
    cst = sp.sqrt((gam - 1) * cps * Tst)
    pst = Pr * sp.exp((cps * sp.log(Tst / Tr) - s) / Rg)
    rst = pst / (Rg * Tst)
    Vs = cst + (pst - Pa) / (rst * cst)
    Hs = sp.hessian(Vs, (h0, s))
    # structure: Vs = C1 sqrt(h0) - Pa * C2 * h0^(1/2 - cp/R) e^(s/R);
    # minors: H11 <= 0 iff the (positive, log-convex) Pa-term dominates
    # correctly; verify the two exact identities instead of inequalities:
    # (i) with Pa = 0 the s-dependence drops and H reduces to the
    #     concave sqrt term; (ii) the Pa-part of -Vs is log-convex:
    #     -(Vs - Vs|Pa=0) == Pa*C2*h0^a e^(s/R) with a = 1/2 - cp/R < 0.
    Vs0 = Vs.subs(Pa, 0)
    good = sp.simplify(sp.diff(Vs0, s)) == 0
    print('  (S2) sonic branch: Pa=0 part is s-free:       %s'
          % ('PASS' if good else 'FAIL'))
    ok &= good
    g11 = sp.simplify(sp.hessian(Vs0, (h0, s))[0, 0] * h0 ** sp.Rational(3, 2))
    good = bool(sp.simplify(g11).is_negative)
    print('  (S2) sonic branch: Pa=0 part concave in h0:   %s'
          % ('PASS' if good else 'FAIL'))
    ok &= good
    Pa_part = sp.simplify(Vs0 - Vs)          # = +Pa/(rho* c*) > 0
    logp = sp.expand_log(sp.log(Pa_part), force=True)
    hess_log = sp.hessian(logp, (h0, s))
    good = (sp.simplify(hess_log[0, 1]) == 0 and
            sp.simplify(hess_log[1, 1]) == 0 and
            bool(sp.simplify(hess_log[0, 0] * h0 ** 2).is_positive))
    print('  (S2) sonic branch: Pa-part log-convex => -part concave: %s'
          % ('PASS' if good else 'FAIL'))
    ok &= good
    return ok


def _hess_fd(f, x, scales):
    """Central-difference Hessian, steps h_i = eps^(1/4) scale_i."""
    n = x.size
    H = np.zeros((n, n))
    h = EPS ** 0.25 * scales
    for i in range(n):
        for j in range(i, n):
            ei = np.zeros(n); ei[i] = h[i]
            ej = np.zeros(n); ej[j] = h[j]
            H[i, j] = H[j, i] = (
                f(x + ei + ej) - f(x + ei - ej)
                - f(x - ei + ej) + f(x - ei - ej)) / (4 * h[i] * h[j])
    return H


def s3_scan(V=V_env, label='composite envelope', expect_concave=True):
    """FD-Hessian concavity scan of the perspective F_env over a
    derived (m, e, sig) box spanning BOTH branches."""
    Pa = PREF
    rng = np.random.default_rng(20260806)
    # state box: T0 in [1500, 3600] K, P0/Pa in [1.2, 60] (both branches:
    # npr_sonic(1.4) = 1.893), unit mass flux scaled by m in [0.5, 2]
    npts, bad, maxev_scaled = 400, 0, -np.inf
    seam = 0
    for _ in range(npts):
        T0 = 1500.0 + 2100.0 * rng.random()
        NPR0 = 1.2 + 58.8 * rng.random()
        h0 = CP * T0
        s = CP * math.log(T0 / TREF) - R * math.log(NPR0 * Pa / PREF)
        m = 0.5 + 1.5 * rng.random()
        x = np.array([m, m * h0, m * s])
        scales = np.abs(x) + np.array([1.0, h0, abs(s) + R])
        f = lambda z: float(F_env(z[0], z[1], z[2], Pa, V=V))
        H = _hess_fd(f, x, scales)
        Hs_ = H * np.outer(scales, scales) / max(abs(f(x)), 1.0)
        ev = np.linalg.eigvalsh(Hs_)[-1]
        maxev_scaled = max(maxev_scaled, ev)
        # derived FD floor for scaled second differences: eps^(1/2)
        if ev > 1e3 * EPS ** 0.5:
            bad += 1
        if abs(P0_of(h0, s) / Pa - npr_sonic(GAM)) < 0.5:
            seam += 1
    verdict = (bad == 0) if expect_concave else (bad > 0)
    print('  (S3) %s: %d/%d points concave (max scaled eig %.2e, '
          'seam pts %d): %s'
          % (label, npts - bad, npts, maxev_scaled,
             seam, 'PASS' if verdict else 'FAIL'))
    return verdict, bad


def s4_crosscheck():
    """Envelope vs the independent OP-0 ladder closed forms: for a
    perfect-gas stagnation state, m*V_env == CF*Pc per unit throat."""
    ok = True
    Pa = PREF
    GAMMA = math.sqrt(GAM * (2.0 / (GAM + 1.0)) ** ((GAM + 1.0)
                                                    / (GAM - 1.0)))
    worst = 0.0
    for NPR0 in (1.3, 1.6, 1.893, 2.5, 10.0, 40.0):
        Pc = NPR0 * Pa
        T0 = 2500.0
        h0 = CP * T0
        s = CP * math.log(T0 / TREF) - R * math.log(Pc / PREF)
        mdot = Pc * GAMMA / math.sqrt(R * T0)          # A_t = 1
        F_mine = mdot * float(V_env(np.array(h0), np.array(s), Pa))
        F_ladder = float(cf_ideal(GAM, Pc, Pa)) * Pc   # A_t = 1
        rel = abs(F_mine - F_ladder) / F_ladder
        worst = max(worst, rel)
    good = worst < 1e3 * EPS ** 0.5   # transcendental chains, derived
    print('  (S4) envelope == OP-0 ladder closed forms (6 NPR incl. '
          'seam): worst rel %.2e: %s' % (worst, 'PASS' if good else 'FAIL'))
    ok &= good

    # R2: corrupted cap rule must break the cross-check on subcritical
    def V_bad(h0, s, Pa_):
        return V_sup(h0, s, Pa_)               # naive, uncapped
    Pc = 1.3 * Pa
    T0 = 2500.0
    h0 = CP * T0
    s = CP * math.log(T0 / TREF) - R * math.log(Pc / PREF)
    mdot = Pc * GAMMA / math.sqrt(R * T0)
    F_bad = mdot * float(V_bad(np.array(h0), np.array(s), Pa))
    F_ladder = float(cf_ideal(GAM, Pc, Pa)) * Pc
    rejected = abs(F_bad - F_ladder) / F_ladder > 1e3 * EPS ** 0.5
    print('  [R2] corrupted (uncapped) rule REJECTED at subcritical: %s'
          % ('PASS' if rejected else 'FAIL'))
    ok &= rejected
    return ok


def main():
    print('== G-B ergodic-transfer envelope carrier (X-GBE) ==')
    ok = s1_symbolic()
    good, _ = s3_scan()
    ok &= good

    # R1: a convexified branch must be DETECTED non-concave
    def V_corrupt(h0, s, Pa_):
        return V_env(h0, s, Pa_) + 1e-4 * (h0 - CP * TREF) ** 2 \
            / (CP * TREF)
    good, bad = s3_scan(V=V_corrupt, label='[R1] corrupted envelope',
                        expect_concave=False)
    print('  [R1] corruption DETECTED at %d points:        %s'
          % (bad, 'PASS' if good else 'FAIL'))
    ok &= good

    ok &= s4_crosscheck()
    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
