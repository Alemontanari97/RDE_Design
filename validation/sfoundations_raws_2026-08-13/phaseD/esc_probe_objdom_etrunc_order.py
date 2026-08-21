# esc_probe_objdom_etrunc_order.py
# S-FOUNDATIONS-C4 escalation, minor (b) [OBJ-DOM], ESCALATED REFUTER
# round 1 (2026-08-20). Executable counterexample for
# ESC-OBJDOM-r1-1 / ESC-OBJDOM-r1-2 (see esc_refute_objdom_r1.md).
#
# TARGET CLAIMS (phaseD_minor_objdom.md, revision [ESC-r1-1/-2]):
#  (a.2) "DJ_panel^trap = DJ_panel + E_trunc, with E_trunc the
#        single-interval trapezoid truncation error: O((Dy)^3) with
#        Dy = rtd*(1 - cos th1) = O(th1^2), hence O(th1^6)-class"
#  (F-1 kernel branch) "kernel arc-flow rule: prediction =
#        2*pi*p(th1)*y(th1)*rtd*sin(th1)/n_B (OBJDOM-1(c); no extra
#        term)" -- i.e. any kernel-sampled implementation's AD
#        derivative is claimed to match the exact Leibniz derivative
#        within an AD/FD-noise bar.
#
# COUNTEREXAMPLE MECHANISM: the coded trapezoid rule integrates in y
# (thrust_J: dy = y[1:]-y[:-1]); on the throat panel dy/dth =
# rtd*sin(th) -> 0 at th = 0, so p as a function of y has a
# square-root cusp at the throat whenever p'(0) != 0 (generic
# accelerating transonic wall flow: p'(0) = rtd*(dp/dx)_throat != 0).
# Then f(y) = p*y is NOT C^2 on the panel, the standard trapezoid
# bound is inapplicable, and the true single-interval error is
#     E_trunc = -(pi/6)*rtd*p'(0)*yt*th1^3 + O(th1^4)   [O(th1^3)],
# NOT O(th1^6). The O(th1^6) claim is recovered ONLY under the extra
# hypothesis p'(0) = 0 (p even in th at the throat), which the file
# does not state.
#
# The probe measures, on the model family
#     p(th) = p0*(1 + c1*th + c2*th^2),
#     y(th) = yt + rtd*(1 - cos th),
# with the RECORD geometry constants (advisory SS1.3: yt = 1,
# rtd = 0.45, th1_record = 0.008727 rad, n_B = 23; p0 normalized to
# 1, record scale p_t = 5e6 Pa used only for the labeled
# SCALING-ESTIMATE lines):
#   [1] slope of log|E_trunc| vs log th1: generic case (c1 != 0)
#       -> 3 (KILLS the O(th1^6) claim); even case (c1 = 0, c2 != 0)
#       -> 6 (the claim's order holds only there);
#   [2] coefficient check: E_trunc / (-(pi/6)*rtd*p0*c1*yt*th1^3) -> 1;
#   [3] F-1 kernel-branch mismatch: the exact d/dth1 of the
#       theta=0-station trapezoid panel (the advisory's own first-named
#       fix-A form, "add the theta = 0 throat station" -- a
#       kernel-sampled rule, hence in F-1's kernel branch) vs the
#       Leibniz prediction (c): relative mismatch -> (c1/4)*th1-class
#       = O(th1) relative, the SAME class as the endpoint-rule
#       modeling term the revision itself declares "orders above any
#       AD/FD bar";
#   [4] consistency: endpoint-rule model error -> +2x the trapezoid
#       error with opposite sign (both O(th1^3)).
#
# Deps: numpy only (pinned env; no installs). Exit 0 iff all four
# rejectors PASS (i.e. iff the counterexample STANDS).

import numpy as np

YT, RTD = 1.0, 0.45
TH1_REC = 0.008727            # record th1 = da (advisory SS1.3)
NB_REC = 23                   # record n_B (advisory SS1.3)
TILT_REC = 5.36e3             # record gradient row, J-units/rad
ACC_REC = 9.3                 # record O3 acceptance 10*gtol

GL_X, GL_W = np.polynomial.legendre.leggauss(80)


def one_m_cos(t):
    """1 - cos(t) = 2*sin(t/2)^2, cancellation-free (the naive form
    loses ~9 digits at t ~ 5e-4 and was measured polluting the
    even-case control before this guard)."""
    s = np.sin(0.5 * t)
    return 2.0 * s * s


def panel_exact(th1, p):
    """DJ_panel = 2*pi * Int_0^{th1} p(th)*y(th)*rtd*sin(th) dth,
    Gauss-Legendre 80 (machine-exact here: smooth integrand in th)."""
    t = 0.5 * th1 * (GL_X + 1.0)
    g = p(t) * (YT + RTD * one_m_cos(t)) * RTD * np.sin(t)
    return 2.0 * np.pi * 0.5 * th1 * np.dot(GL_W, g)


def panel_trap(th1, p):
    """theta=0-station single-interval trapezoid in y (the coded
    thrust_J rule extended with the throat station; OBJDOM-1(a.1))."""
    y1 = YT + RTD * one_m_cos(th1)
    return 2.0 * np.pi * 0.5 * (p(0.0) * YT + p(th1) * y1) * (y1 - YT)


def panel_trap_ddth1(th1, p, dp):
    """EXACT d/dth1 of panel_trap (what AD returns for this rule)."""
    y1 = YT + RTD * one_m_cos(th1)
    yp = RTD * np.sin(th1)
    return 2.0 * np.pi * (
        0.5 * (dp(th1) * y1 + p(th1) * yp) * (y1 - YT)
        + 0.5 * (p(0.0) * YT + p(th1) * y1) * yp)


def leibniz_c(th1, p):
    """OBJDOM-1(c) per unit th1: 2*pi*p(th1)*y(th1)*rtd*sin(th1)."""
    y1 = YT + RTD * (1.0 - np.cos(th1))
    return 2.0 * np.pi * p(th1) * y1 * RTD * np.sin(th1)


def slope(th1s, errs):
    return np.polyfit(np.log(th1s), np.log(np.abs(errs)), 1)[0]


def main():
    ok = True
    th1s = TH1_REC / 2.0 ** np.arange(0, 5)

    # -- [1] order of E_trunc, generic vs even ------------------------
    c1 = -0.3
    pg = lambda t: 1.0 + c1 * t                      # generic p'(0)!=0
    dpg = lambda t: c1 + 0.0 * t
    pe = lambda t: 1.0 - 0.3 * t * t                 # even   p'(0)==0
    e_gen = np.array([panel_trap(t, pg) - panel_exact(t, pg)
                      for t in th1s])
    # even-case sweep at larger th1 (all still < record thB = 0.2007):
    # the O(th1^6) signal must sit far above the float64 noise floor
    # of the two ~O(th1^2) panel values (diagnosed ~5e-16 absolute)
    th1s_e = TH1_REC * 2.0 ** np.arange(3, 0, -1)
    e_evn = np.array([panel_trap(t, pe) - panel_exact(t, pe)
                      for t in th1s_e])
    s_gen, s_evn = slope(th1s, e_gen), slope(th1s_e, e_evn)
    print("[1] E_trunc order: generic slope = %.4f (claim 6, true 3);"
          " even slope = %.4f (claim 6 holds only here)"
          % (s_gen, s_evn))
    r1 = (abs(s_gen - 3.0) < 0.1) and (abs(s_evn - 6.0) < 0.2)
    ok &= bool(r1)
    print("    REJECTOR[1] %s  (fires iff generic slope ~ 3, i.e."
          " O(th1^6) claim FALSE)" % ("PASS" if r1 else "FAIL"))

    # -- [2] coefficient -(pi/6)*rtd*p0*c1*yt*th1^3 -------------------
    pred = -(np.pi / 6.0) * RTD * c1 * YT * th1s ** 3
    ratio = e_gen / pred
    print("[2] E_trunc / [-(pi/6)*rtd*p'(0)*yt*th1^3] = %s"
          % np.array2string(ratio, precision=4))
    r2 = abs(ratio[-1] - 1.0) < 0.01
    ok &= bool(r2)
    print("    REJECTOR[2] %s  (coefficient of the true O(th1^3) law)"
          % ("PASS" if r2 else "FAIL"))

    # -- [3] F-1 kernel-branch mismatch for the station rule ----------
    mism = np.array([panel_trap_ddth1(t, pg, dpg) - leibniz_c(t, pg)
                     for t in th1s])
    rel = mism / np.array([leibniz_c(t, pg) for t in th1s])
    s_m = slope(th1s, rel)
    print("[3] station-rule AD-vs-(c) relative mismatch: %s"
          " (slope %.3f => O(th1)-relative; c1/4*th1 = %.3e at record"
          " th1)" % (np.array2string(rel, precision=3, max_line_width=79),
                     s_m, c1 / 4.0 * TH1_REC))
    print("    SCALING-ESTIMATE (record constants, illustration only):"
          " |rel| x tilt_record = %.1f J-units/rad vs acceptance %.1f"
          " and vs AD/FD-noise-class bars (orders below %.1f)"
          % (abs(rel[0]) * TILT_REC, ACC_REC, ACC_REC))
    r3 = (abs(s_m - 1.0) < 0.1) and (abs(rel[0]) * TILT_REC > 1.0)
    ok &= bool(r3)
    print("    REJECTOR[3] %s  (fires iff mismatch is O(th1)-relative"
          " and J-units-scale at the record instance, i.e. NOT"
          " AD/FD-noise-class => F-1 kernel-branch 'no extra term'"
          " spurious-fires on the station rule)"
          % ("PASS" if r3 else "FAIL"))

    # -- [4] endpoint-rule error = -2x trapezoid error (consistency) --
    e_end = np.array([2.0 * np.pi * pg(t) * (panel_exact(t, lambda u:
                      np.ones_like(np.atleast_1d(u))) / (2.0 * np.pi))
                      - panel_exact(t, pg) for t in th1s])
    q = e_end / e_gen
    print("[4] E_endpoint / E_trap = %s (both O(th1^3); -2 predicted)"
          % np.array2string(q, precision=4))
    r4 = abs(q[-1] + 2.0) < 0.05
    ok &= bool(r4)
    print("    REJECTOR[4] %s" % ("PASS" if r4 else "FAIL"))

    print("VERDICT: %s" % ("COUNTEREXAMPLE STANDS (all rejectors PASS)"
                           if ok else "counterexample FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
