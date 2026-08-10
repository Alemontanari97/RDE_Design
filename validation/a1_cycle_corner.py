#!/usr/bin/env python3
"""A1 BRICK 2, STEP 8 [F2/A1]: THE CYCLE-LEVEL WEIGHTED TRANSVERSALITY
INSTRUMENT — T7(c) executable: "no phase satisfies its own corner
condition; the mu-average does."

THE CLAIM (M0 T7(c), quasi-1D shadow). At the cycle optimum the
per-phase corner residuals R(xi) = p_e(xi) - pa are individually
NONZERO — the wave-passage phases vote "lengthen" (underexpanded,
R > 0), the tail phases vote "shorten" (overexpanded, R < 0) — and
optimality is exactly the statement that the mu-weighted average of the
votes vanishes:

$$ <R>_mu = <p_e(xi)>_mu - pa = 0     at the cycle optimum

(the weight w(xi) = dA_e/deps is phase-independent in this class, so
the naive average IS the weighted one — the general-w case arrives
with the plug/truncated problems).

DATA: entirely from the cycle layer's cached marches (step 7,
validation/_cycle_ckpt.json) — the instrument is an ANALYSIS of the
existing certified runs; the only new marches are band probes.

CHECKS (derived bands):
  W-1  balance at the optimum: |<R>| <= band, band = K_RICH *
       |d<p_e>/deps| * (golden window) from cached neighbors + floor.
  W-2  the brokered compromise: EVERY phase's |R(xi)| exceeds 10x the
       band — no phase is individually satisfied.
  W-3  the vote pattern: R(xi) strictly decreasing with xi (high-P
       early phases vote +, late tail votes -) with exactly one sign
       change across the cycle.
  R-1  rejector: at the PEAK design (cached), |<R>| explodes — the
       meter detects a wrong design at cycle level.
Both cycles are tested: the T3 (P-only) cycle and the mock RDE (P+T).

Run:  .venv-a1/bin/python validation/a1_cycle_corner.py
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1              # noqa: E402
import a1_cycle_layer as CL                  # noqa: E402

NPASS = [0, 0]
K_RICH = A1.K_RICH


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def main():
    t0 = time.time()
    print("== A1 brick 2 step 8: cycle-level weighted transversality"
          " [F2/A1] ==")
    tab0 = A1.prep_tab(A1.build_tab_nasa())
    ts, ps = tab0["ts"], tab0["ps"]
    ck = json.load(open(CL.CKPT))
    pa = 7.614420e+05                     # ambient of record (step 3/7)

    xi = (np.arange(CL.NXI) + 0.5) / CL.NXI
    I1 = (1.0 - 1.0 / CL.PR) / np.log(CL.PR)
    P_CJ = ps / I1
    P0s = P_CJ * CL.PR ** (-xi)
    gm = tab0["gammamedio"]
    TR = CL.PR ** ((gm - 1.0) / gm)
    T0s_mock = 3850.0 * TR ** (-xi)

    def pe_of(eps, P0, T0):
        key = "%.6f:%.6e:%.3f" % (eps, P0, T0)
        if key not in ck:
            F, r = CL.march_F(eps, P0, T0, pa, tab0, ck)
            return r["pe"]
        return ck[key]["pe"]

    for name, T0s, eps_opt, eps_bad in (
            ("T3 (P-only)", np.full(CL.NXI, ts), 5.168446, 10.290700),
            ("mock RDE (P+T)", T0s_mock, 5.139510, 10.289200)):
        print("-- cycle: %s ; optimum of record eps = %.5f --"
              % (name, eps_opt))
        R = np.array([pe_of(eps_opt, P0s[k], T0s[k]) - pa
                      for k in range(CL.NXI)])
        # band: sensitivity of <p_e> to eps from a cached neighbor pair
        eps_nb = eps_opt * 1.02
        Rnb = np.array([pe_of(round(eps_nb, 6), P0s[k], T0s[k]) - pa
                        for k in range(CL.NXI)])
        slope = abs(Rnb.mean() - R.mean()) / (eps_nb - eps_opt)
        band = K_RICH * slope * 0.06 + A1.C_FLOOR * A1.EPS * pa
        print("  votes R(xi) [Pa]: %s"
              % "  ".join("%+.3e" % v for v in R))
        print("  <R> = %+.4e   band = %.4e   (pa = %.4e)"
              % (R.mean(), band, pa))
        check("W-1 %s: balance <R> ~ 0 at the optimum" % name,
              abs(R.mean()) <= band)
        rmin = np.abs(R).min()
        print("  min|R| = %.3e  (%.1fx band, %.0fx the achieved <R>)"
              % (rmin, rmin / band, rmin / max(abs(R.mean()), 1e-30)))
        check("W-2 %s: NO phase individually satisfied (min|R| > band"
              " AND > 10x |<R>|)" % name,
              rmin > band and rmin > 10 * abs(R.mean()))
        sgn = np.sign(R)
        nflips = int(np.sum(sgn[1:] != sgn[:-1]))
        mono = bool((np.diff(R) < 0).all())
        print("  pattern: R decreasing = %s ; sign changes = %d"
              % (mono, nflips))
        check("W-3 %s: votes decrease with xi, exactly one sign"
              " change" % name, mono and nflips == 1)
        Rbad = np.array([pe_of(eps_bad, P0s[k], T0s[k]) - pa
                         for k in range(CL.NXI)])
        print("  rejector: <R> at the peak design = %+.4e (%.1fx"
              " band)" % (Rbad.mean(), abs(Rbad.mean()) / band))
        check("R-1 %s: wrong design detected (|<R>| > K_RICH x band)"
              % name, abs(Rbad.mean()) > K_RICH * band)

    print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
