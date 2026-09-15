"""[F3] OUR WORLD, DUAL-CODE TWIN: GENO's ideal-spike field as our start
line, in our gas, over GENO's wall.

The rao1961_twin instrument (start line cut from the reference field,
free-jet edge above the kernel top ED, wedge-below-ED comparison at the
declared S8 cross-code level) run on the member the full-expansion A/B
needs: GENO RaoPlug in the CH4/O2 frozen gas at our chamber, lip, inlet
angle and start Mach (CASES/raoplug_ch4o2/run_val_repro: theta_E =
-0.02 deg, L = 5.926, eps 5.1506 = y_E^2, the C- curve reaches the
axis). World posing: ourworld_geno (gas VERIFIED against the field, lip
ambient from raoplug_performance.dat).

PRE-REGISTERED (R5), the rao1961_twin gates transported:
  P1  our march CERTIFIES from the interpolated start line at every cut
      (N = 61);
  P2  at the cut of record, no nonfinite point below ED, and the wedge
      below ED reproduces GENO's field inside the DECLARED S8 thresholds
      (q 1e-3 rel, theta 1.5e-3 rad) with coverage >= 0.95;
  P3  the upstream ladder REPORTED against the reconstruction floor
      (not gated, as in the Rao-world instance).
Cuts: x0 = 1.50 / 1.00 / 0.50 m -- the same fractions of the design
length (0.25 / 0.17 / 0.08 of x_D) as the Rao-world 0.30 / 0.20 / 0.10
of 1.18. Stations: OW_K (default 161 = twice the Rao-world 81: this
spike is 2.2x longer in lip radii).
FALSIFIER: P2 failing at every x0 = our march does not reproduce the
reference in our world; the our-world O3.3 and SQP-return are blocked.

ON-DEMAND CARRIER (env: jax + the GENO run directory; ~20 min on s2).
Run:  .venv-a1/bin/python validation/ourworld_twin.py
"""
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import ourworld_geno as OW                             # noqa: E402
from a1_plug_march import plug_march                   # noqa: E402
from rao1961_twin import (start_from_geno, control_surface,   # noqa: E402
                          wedge_deviation, reference_band,
                          EDGE_FILL, Q_TOL, TH_TOL, COVER)

CUTS = tuple(float(v) for v in
             os.environ.get("OW_CUTS", "1.50,1.00,0.50").split(","))
K_ST = int(os.environ.get("OW_K", 161))
NPASS = [0, 0]


def check(label, ok):
    NPASS[1] += 1
    NPASS[0] += int(bool(ok))
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def main():
    t0 = time.time()
    print("== [F3] OUR world, dual-code twin: GENO ideal-spike field -> "
          "our march ==")
    if not os.path.isdir(OW.RUN):
        print("   OW_GENO_RUN not a directory -- nothing to do")
        return 2
    W = OW.load_world()
    fld, wall, tab, qpa = W["fld"], W["wall"], W["tab"], W["qpa"]
    ED = control_surface(W["run"], fld)
    print("   kernel top ED: %d pts, (%.3f,%.3f) -> (%.3f,%.4f)"
          % (len(ED), ED[0, 0], ED[0, 1], ED[-1, 0], ED[-1, 1]))

    res = {}
    print("\n   x0    rows  cert(glob)  where          wedge  nonfin"
          "  |dq|/q mean/max      |dth| mean/max deg   t[s]")
    print("   " + "-" * 104)
    for x0 in CUTS:
        for N in (41, 61):
            t1 = time.time()
            start, ytop = start_from_geno(fld, wall, x0, N)
            if len(start[1]) < 8:
                print("   %.2f  %3d   start line too short" % (x0, N))
                continue
            dy_row = ((start[1][-1] - start[1][0])
                      / max(len(start[1]) - 1, 1))
            xs = np.linspace(x0, wall[-1, 0], K_ST)[1:]
            yws = np.interp(xs, wall[:, 0], wall[:, 1])
            sl = np.gradient(yws, xs)
            try:
                out, _ = plug_march((xs, yws, sl), start, qpa, tab, 1.0,
                                    edge_fill=EDGE_FILL)
            except Exception as exc:
                print("   %.2f  %3d   RAISED: %s" % (x0, N, str(exc)[:44]))
                continue
            dq, dth, P, nonfin = wedge_deviation(out, fld, ED, x0, dy_row)
            print("   %.2f  %3d  %9.2e  %-13s  %5d  %5d   %.2e/%.2e"
                  "    %.2e/%.2e   %5.0f"
                  % (x0, len(start[1]), out["cert_worst"],
                     str(out["cert_where"])[:13], len(dq), nonfin,
                     dq.mean(), dq.max(), dth.mean(), dth.max(),
                     time.time() - t1), flush=True)
            res[(x0, N)] = (out, dq, dth, P, nonfin)

    for x0 in CUTS:
        if (x0, 61) in res:
            out = res[(x0, 61)][0]
            check("P1 x0=%.2f the march certifies (worst %.2e at %s)"
                  % (x0, out["cert_worst"], out["cert_where"]),
                  float(out["cert_worst"]) <= 1.0)

    x0r = CUTS[0]
    if (x0r, 61) in res:
        out, dq, dth, P, nonfin = res[(x0r, 61)]
        (bq2, bth2), (bq4, bth4) = reference_band(fld, P)
        print("\n   derived band (reference reconstruction, 1:2 / 1:4):")
        print("     |dq|/q  mean %.2e / %.2e   max %.2e / %.2e"
              % (bq2.mean(), bq4.mean(), bq2.max(), bq4.max()))
        print("     |dth|   mean %.2e / %.2e   max %.2e / %.2e deg"
              % (bth2.mean(), bth4.mean(), bth2.max(), bth4.max()))
        fq = float((dq <= Q_TOL).mean())
        fth = float((dth <= np.degrees(TH_TOL)).mean())
        print("   the wedge gap (%.1e mean) sits %.0fx above the "
              "reconstruction floor" % (dq.mean(),
                                        dq.mean() / max(bq4.mean(), 1e-300)))
        check("P2 no nonfinite point below ED", nonfin == 0)
        check("P2 %.1f%% of the wedge within q %.0e (declared S8 "
              "threshold; need >= %.0f%%)" % (100 * fq, Q_TOL, 100 * COVER),
              fq >= COVER)
        check("P2 %.1f%% of the wedge within theta %.1e rad (declared S8 "
              "threshold; need >= %.0f%%)" % (100 * fth, TH_TOL, 100 * COVER),
              fth >= COVER)

    ms = [(x0, res[(x0, 61)][1].mean()) for x0 in CUTS if (x0, 61) in res]
    if len(ms) == len(CUTS):
        print("\n   P3 (reported): |dq|/q mean at x0 = "
              + ", ".join("%.2f: %.2e" % m for m in ms))

    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    print("VERDICT: %s" % ("PASS -- our march reproduces GENO's ideal-spike "
                           "kernel below ED in OUR world at the declared S8 "
                           "cross-code level" if NPASS[0] == NPASS[1]
                           else "FAIL"))
    return 0 if NPASS[0] == NPASS[1] else 1


if __name__ == "__main__":
    sys.exit(main())
