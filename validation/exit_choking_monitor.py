#!/usr/bin/env python3
"""THE CHOKING MONITOR of the extraction surface [X-CHOK] (F2a item U3', 2026-09-30; gates declared in
validation/PROGRESS_2026-09-30_F2ENGINE.md before this file was written).

Taking the RDE outflow phase by phase presupposes a surface downstream of the throat where, in every phase, the gas
leaves axially faster than sound: no wave travels back through it, so the phases are independent data. This
monitor reads the extraction surface of record (the Q2D THOR_CAv3 exit column, one instant) and reports the axial
Mach margin M_x - 1 cell by cell. The surface is a plane x = const, so the normal Mach is M_x exactly (M0: the
meridional NORMAL Mach is the audit quantity, never the total Mach). Line: the smallest margin must exceed the
data's own uncertainty -- the wander X-SWAV measures (2 percent of pressure, about 1 percent of Mach) -> 0.02.
usage: .venv-a1/bin/python validation/exit_choking_monitor.py [--data <npz>]"""
import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "_rde_tournament", "q2d_thor_cav3_exit_t15.5ms.npz")
LY = 0.42278
LINE = 0.02                       # the wander of the data in Mach (X-SWAV: 2 percent of pressure)
OK = True


def check(name, cond, detail=""):
    global OK
    OK &= bool(cond)
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, (" -- " + detail) if detail else ""))
    return bool(cond)


def margin(d, suffix):
    u, T, g, R = d["u_" + suffix], d["T_" + suffix], d["g_" + suffix], d["R_" + suffix]
    return u / np.sqrt(g * R * T) - 1.0


def report(name, m, th):
    k = int(np.argmin(m))
    ok = check("%s: M_x - 1 > %.2f in every cell (min %.3f at theta %.1f deg, max %.3f)" % (name, LINE, m.min(), th[k], m.max()), m.min() > LINE)
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=DATA)
    a = ap.parse_args()
    d = np.load(a.data)
    th = np.mod(360.0 * d["yc_last"] / LY, 360.0)
    print("== [F2a U3'] the choking monitor of the extraction surface [X-CHOK] (%d cells, t %.2f ms, x %.4f m) ==" % (len(th), float(d["t"]) * 1e3, float(d["x_face_exit"])))
    m_last, m_prev = margin(d, "last"), margin(d, "prev")
    report("C-1 the exit column", m_last, th)
    report("C-2 the previous column", m_prev, np.mod(360.0 * d["yc_prev"] / LY, 360.0))
    # R-1: a subsonic patch planted on 30 degrees must be rejected with its location
    print("-- rejector (seeded, must fire) --")
    u = d["u_last"].copy()
    patch = (th >= 90.0) & (th < 120.0)
    u[patch] = 0.9 * np.sqrt(d["g_last"] * d["R_last"] * d["T_last"])[patch]
    m_r = u / np.sqrt(d["g_last"] * d["R_last"] * d["T_last"]) - 1.0
    k = int(np.argmin(m_r))
    fired = not (m_r.min() > LINE)
    check("R-1 a subsonic patch on [90, 120) deg is REJECTED and located (min %.3f at theta %.1f deg)" % (m_r.min(), th[k]), fired and 90.0 <= th[k] < 120.0)
    print("VERDICT: %s" % ("PASS" if OK else "FAIL"))
    sys.exit(0 if OK else 1)


if __name__ == "__main__":
    main()
