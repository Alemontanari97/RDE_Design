#!/usr/bin/env python3
"""DOES A K-SECTOR FAMILY RESOLVE THE CYCLE? [X-FRES] (F2a, the harmonic-decay half of the single-wave monitor; F2.ENGINE
night of 2026-09-30/10-01; gates declared in validation/PROGRESS_2026-09-30_F2ENGINE.md before this file was written).

A blowdown with a detonation front is a periodic signal with a JUMP: its harmonics fall only as 1/n, so the spectral
(trapezoid-on-the-circle) switch of M0 VI.4bis is not licensed for this data class. The equal-weight K-sector family is
exact for what is LINEAR in the sector means (mass, mean pressure: X-CYCF F-1/F-2), but the thrust is not linear in the
phase state (the pressure term, the over-expanded phases), so K sectors carry a discretisation error on C_F that only a
refinement measures. Read here: the same designs marched by the design tool (two-wall march, the separation closure of
the posing) on the CycleFamily v0 methane family at K = 12, 24, 48 (and 3 as the rejector).
  H-1 the spectrum of Pc(xi): |c_n| against the 1/n law of a jump (log-log slope within 0.1 of -1)
  H-2 |C_F(K12) - C_F(K48)| <= 0.17 percent of C_F on every design, the K-sequence monotone, and the K12 error estimated
      by Richardson from K24/K48 within a factor 2 of the measured one
  H-3 the difference between the designs at K12 and at K48 within 0.05 percent of C_F
  R-1 (must fire) K = 3 fails H-2
Inputs: the tool's evaluation records sdt/twop_phase_eval_<design tag>_K<K>.json (K12: the night's records).
usage: .venv-a1/bin/python validation/family_resolution_audit.py"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SDT = "/data10/falco/RDE/handoff/plug_2026-09-29/sdt"
FAM = os.path.join(HERE, "_cycle_family", "sdt_ch4_phi1_pcp20")
LINE = 0.0017                 # PILOT-WF's line: one third of the thrust-stand band
DLINE = 0.0005                # the comparison's line (the frozen-vs-rotating offset cancelled to 0.05 percent)
EVALS = {"RaSDT": {12: "twop_phase_eval_rao_sdt.json", 24: "twop_phase_eval_rao_K24.json", 48: "twop_phase_eval_rao_K48.json", 3: "twop_phase_eval_rao_K3.json"},
         "SaSDT": {12: "twop_phase_eval_sqpA_sdt.json", 24: "twop_phase_eval_sqpA_K24.json", 48: "twop_phase_eval_sqpA_K48.json", 3: "twop_phase_eval_sqpA_K3.json"}}
OK = True


def check(name, cond, detail=""):
    global OK
    OK &= bool(cond)
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, (" -- " + detail) if detail else ""))
    return bool(cond)


def main():
    print("== [F2a] does a K-sector family resolve the cycle? [X-FRES] (CycleFamily v0, methane, Rao's and the SQP plug) ==")
    # ---- H-1 the spectrum of the blowdown (the matched state of the family)
    sys.path[:0] = [os.path.dirname(HERE), os.path.join(os.path.dirname(HERE), "src"), os.path.join(os.path.dirname(HERE), "src", "thrust")]
    import stechmann_nozzle as SN
    st = SN.load()["states"]["det|CH4|20|1.00"]
    P0, PR = float(st["P0"]), float(st["PR"])
    lam = np.log(PR)
    n = np.arange(1, 129)
    c = np.abs(P0 * (1 - np.exp(-lam)) / (lam + 2j * np.pi * n))         # the exact Fourier coefficients of P0 exp(-lam xi) on [0, 1)
    sl = np.polyfit(np.log(n[8:]), np.log(c[8:]), 1)[0]
    check("H-1 the blowdown's harmonics fall as 1/n (log-log slope %.3f, n 9..128): a jump -- the spectral switch is NOT licensed" % sl, abs(sl + 1.0) <= 0.1)
    # ---- the tool's C_F at every K
    J = {}
    for d, files in EVALS.items():
        for K, f in files.items():
            p = os.path.join(SDT, f)
            if not os.path.exists(p):
                print("  missing %s" % p)
                continue
            r = json.load(open(p))["rows"].get(d, {})
            if "J_mu" in r:
                J[(d, K)] = float(r["J_mu"])
    for d in EVALS:
        print("  %s: C_F(K) %s" % (d, "  ".join("K%d %.6f" % (K, J[(d, K)]) for K in (3, 12, 24, 48) if (d, K) in J)))
    # ---- H-2 resolution on every design
    for d in EVALS:
        if not all((d, K) in J for K in (12, 24, 48)):
            check("H-2 %s: the K-sequence complete" % d, False)
            continue
        j12, j24, j48 = J[(d, 12)], J[(d, 24)], J[(d, 48)]
        e12 = abs(j12 - j48) / j48
        mono = (j12 - j24) * (j24 - j48) > 0
        rr = (j12 - j24) / (j24 - j48) if j24 != j48 else np.inf
        pord = np.log2(abs(rr)) if np.isfinite(rr) and rr != 0 else np.nan
        jinf = j48 + (j48 - j24) / (2 ** pord - 1) if np.isfinite(pord) and pord > 0 else np.nan
        e12r = abs(j12 - jinf) / jinf if np.isfinite(jinf) else np.nan
        check("H-2 %s: |C_F(K12) - C_F(K48)| = %.2e of C_F <= %.4f; monotone %s; order %.2f; K12 error by Richardson %.2e (measured %.2e)"
              % (d, e12, LINE, mono, pord, e12r, e12),
              e12 <= LINE and mono and np.isfinite(e12r) and 0.5 <= e12r / max(e12, 1e-300) <= 2.0)
    # ---- H-3 the comparison survives
    if all((d, K) in J for d in EVALS for K in (12, 48)):
        d12 = (J[("SaSDT", 12)] - J[("RaSDT", 12)]) / J[("RaSDT", 12)]
        d48 = (J[("SaSDT", 48)] - J[("RaSDT", 48)]) / J[("RaSDT", 48)]
        check("H-3 the SQP-Rao difference at K12 %.4f %% and at K48 %.4f %%: within %.2f %% of C_F" % (100 * d12, 100 * d48, 100 * DLINE), abs(d12 - d48) <= DLINE)
    # ---- R-1 the rejector: 3 sectors
    print("-- rejector (must fire) --")
    for d in EVALS:
        if (d, 3) in J and (d, 48) in J:
            e3 = abs(J[(d, 3)] - J[(d, 48)]) / J[(d, 48)]
            check("R-1 %s: K = 3 FAILS H-2 (|C_F(K3) - C_F(K48)| = %.2e > %.4f)" % (d, e3, LINE), e3 > LINE)
    print("VERDICT: %s" % ("PASS" if OK else "FAIL"))
    sys.exit(0 if OK else 1)


if __name__ == "__main__":
    main()
