# esc_probe_objdom_evenp_iff.py
# S-FOUNDATIONS-C4 escalation, minor (b) [OBJ-DOM], ESCALATED REFUTER
# round 2 (2026-08-20). Executable counterexample for ESC-OBJDOM-r2-1
# (see esc_refute_objdom_r2.md).
#
# TARGET CLAIM (phaseD_minor_objdom.md, revision [ESC-r2-1], stated at
# OBJDOM-1(a.2) and echoed in disposition rows SS6/SS7):
#   "The O((Dy)^3) = O(th1^6) class is recovered IFF p'(0) = 0
#    (p even in th at the throat)"
# The NECESSITY direction is true (r1 probe, unchanged). The
# SUFFICIENCY direction is FALSE: E_trunc is a LINEAR functional of p,
# and an odd CUBIC term p3*th^3 (p'(0) = 0, p'''(0) = 6*p3 != 0) maps
# under th(y) ~ sqrt(2(y-yt)/rtd) to a (y-yt)^{3/2} half-power in y,
# giving the single-interval trapezoid error
#     E_trunc = (pi/10)*rtd*p3*yt*th1^5 + h.o.t.   [O(th1^5)],
# NOT O(th1^6). The true characterization is
#     E_trunc = O(th1^6)  <=>  p'(0) = 0 AND p'''(0) = 0
# (odd th^5 terms map to (y-yt)^{5/2}, error O(th1^7) — below th1^6;
# full evenness of p in th is sufficient, p'(0) = 0 alone is not).
#
# Model family and record geometry constants as in the r1 probe
# (advisory SS1.3: yt = 1, rtd = 0.45, th1_record = 0.008727,
# record thB = 0.2007 — all sweep points kept below thB).
#
# Deps: numpy only (pinned env; no installs). Exit 0 iff all four
# rejectors PASS (i.e. iff the counterexample STANDS).

import numpy as np

YT, RTD = 1.0, 0.45
TH1_REC = 0.008727            # record th1 = da (advisory SS1.3)

GL_X, GL_W = np.polynomial.legendre.leggauss(80)


def one_m_cos(t):
    """1 - cos(t) = 2*sin(t/2)^2, cancellation-free (guard inherited
    from the r1 probe of record)."""
    s = np.sin(0.5 * t)
    return 2.0 * s * s


def panel_exact(th1, p):
    """DJ_panel = 2*pi * Int_0^{th1} p(th)*y(th)*rtd*sin(th) dth,
    Gauss-Legendre 80 (machine-exact: smooth integrand in th)."""
    t = 0.5 * th1 * (GL_X + 1.0)
    g = p(t) * (YT + RTD * one_m_cos(t)) * RTD * np.sin(t)
    return 2.0 * np.pi * 0.5 * th1 * np.dot(GL_W, g)


def panel_trap(th1, p):
    """theta=0-station single-interval trapezoid in y (OBJDOM-1(a.1))."""
    y1 = YT + RTD * one_m_cos(th1)
    return 2.0 * np.pi * 0.5 * (p(0.0) * YT + p(th1) * y1) * (y1 - YT)


def slope(th1s, errs):
    return np.polyfit(np.log(th1s), np.log(np.abs(errs)), 1)[0]


def main():
    ok = True
    # sweep well above the float64 noise floor of the two O(th1^2)
    # panel values (~5e-16 abs, r1 probe diagnosis); all < thB = 0.2007
    th1s = TH1_REC * 2.0 ** np.arange(4, 1, -1)   # [0.1396, 0.0698, 0.0349]

    # -- [1] cubic-odd case: p'(0) = 0, p'''(0) != 0 -> order 5, not 6
    c3 = 0.3
    pc = lambda t: 1.0 + c3 * t ** 3
    e_c3 = np.array([panel_trap(t, pc) - panel_exact(t, pc)
                     for t in th1s])
    s_c3 = slope(th1s, e_c3)
    print("[1] p = 1 + c3*th^3 (p'(0)=0): E_trunc slope = %.4f"
          " (IFF-claim predicts 6; true 5)" % s_c3)
    r1 = abs(s_c3 - 5.0) < 0.1
    ok &= bool(r1)
    print("    REJECTOR[1] %s  (fires iff slope ~ 5, i.e. sufficiency"
          " of p'(0)=0 for O(th1^6) is FALSE)" % ("PASS" if r1 else "FAIL"))

    # -- [2] coefficient law E = (pi/10)*rtd*p3*yt*th1^5 ---------------
    pred = (np.pi / 10.0) * RTD * c3 * YT * th1s ** 5
    ratio = e_c3 / pred
    print("[2] E_trunc / [(pi/10)*rtd*p3*yt*th1^5] = %s"
          % np.array2string(ratio, precision=4))
    r2 = abs(ratio[-1] - 1.0) < 0.01
    ok &= bool(r2)
    print("    REJECTOR[2] %s  (coefficient of the true O(th1^5) law)"
          % ("PASS" if r2 else "FAIL"))

    # -- [3] control: p EVEN in th -> O(th1^6) (evenness IS sufficient)
    pe = lambda t: 1.0 - 0.3 * t * t
    e_e = np.array([panel_trap(t, pe) - panel_exact(t, pe)
                    for t in th1s])
    s_e = slope(th1s, e_e)
    print("[3] p = 1 - 0.3*th^2 (even): slope = %.4f (6 expected)" % s_e)
    r3 = abs(s_e - 6.0) < 0.2
    ok &= bool(r3)
    print("    REJECTOR[3] %s  (control: even-p O(th1^6) branch intact)"
          % ("PASS" if r3 else "FAIL"))

    # -- [4] control: generic p'(0) != 0 -> O(th1^3) (r1 result intact)
    pg = lambda t: 1.0 - 0.3 * t
    th1s_g = TH1_REC / 2.0 ** np.arange(0, 5)
    e_g = np.array([panel_trap(t, pg) - panel_exact(t, pg)
                    for t in th1s_g])
    s_g = slope(th1s_g, e_g)
    print("[4] p = 1 - 0.3*th (generic): slope = %.4f (3 expected;"
          " necessity direction unchanged)" % s_g)
    r4 = abs(s_g - 3.0) < 0.1
    ok &= bool(r4)
    print("    REJECTOR[4] %s" % ("PASS" if r4 else "FAIL"))

    print("VERDICT: %s" % ("COUNTEREXAMPLE STANDS (all rejectors PASS)"
                           if ok else "counterexample FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
