#!/usr/bin/env python3
"""THE DATA ADMISSION AUDITS (stage A of the data contract) [X-ADMA] (F2a; F2.ENGINE night of 2026-09-30/10-01; gates
declared in validation/PROGRESS_2026-09-30_F2ENGINE.md before this file was written).

Before a family of RDE outflow states feeds a design: (i) every phase must carry a complete, physical state (A-1);
(ii) the extraction surface must be one the march can start from: every characteristic leaves it into the nozzle
(M0 Lemma 4: the normal Mach above one with margin), and the recorded stagnation state must be the one its static state
and Mach imply (A-2); (iii) the profiles across the gap must be a possible steady flow (Crocco, parallel extraction: a
radial pressure gradient cannot be held without radial velocity or streamline curvature) (A-3). On the families of the
program the phases are uniform across the gap, so A-3 holds identically -- it bites only on layered data. Three planted
phases must be rejected (R-1 subsonic, R-2 composition, R-3 layered pressure gradient).
usage: .venv-a1/bin/python validation/data_admission_audit.py [<phases.json> <T_lo> <T_hi> <tag> ...]"""
import copy
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RU = 8314.462618
MN_LINE = 0.02                # X-CHOK's line: the data's own uncertainty in Mach
CROCCO_LINE = 1.0e-3          # |dp/dr| x gap / p allowed in a parallel extraction
ONERA7 = {"O2": 31.998, "H2O": 18.015, "H2": 2.016, "H": 1.008, "O": 15.999, "OH": 17.007, "N2": 28.014}
ONERA7_ORDER = ["O2", "H2O", "H2", "H", "O", "OH", "N2"]
DEFAULT = [("/data10/falco/RDE/Nozzle/phases_405.json", 300.0, 3900.0, "THOR_CAv3 (Q2D extraction)", 1e-3),
           (os.path.join(HERE, "_cycle_family", "sdt_ch4_phi1_pcp20", "phases_cfd.json"), 300.0, 4200.0, "CycleFamily v0 methane", 1e-6)]
OK = True


def check(name, cond, detail=""):
    global OK
    OK &= bool(cond)
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, (" -- " + detail) if detail else ""))
    return bool(cond)


_MW = {}


def molar_masses(names):
    """Molar masses: the ONERA-7 kit's for its species, Cantera's (the CJ chain's mechanism) for the rest."""
    miss = [n for n in names if n not in ONERA7 and n not in _MW]
    if miss:
        import cantera as ct
        g = ct.Solution(os.path.join(ROOT, "data", "gri30_CHO_eq.yaml"))
        for n in miss:
            _MW[n] = float(g.molecular_weights[g.species_index(n)])
    return np.array([ONERA7.get(n, _MW.get(n)) for n in names])


def as_dict(Y):
    return dict(zip(ONERA7_ORDER, Y)) if isinstance(Y, list) else dict(Y)


def audit_phase(p, T_lo, T_hi, tol_stag):
    """(a1 ok, a2 ok, a3 ok, details) for one phase."""
    Y = as_dict(p["Y"]); names = list(Y); y = np.array([Y[n] for n in names])
    W = molar_masses(names)
    R_y = RU * np.sum(y / W)
    g, R, T, pr, M = float(p["gamma"]), float(p["R"]), float(p["T"]), float(p["p"]), float(p["mach"])
    T0, P0 = float(p["T0"]), float(p["P0"])
    a1 = (pr > 0 and T_lo <= T <= T_hi and T_lo <= T0 <= T_hi and abs(y.sum() - 1.0) <= 1e-9 and 1.0 < g < 5.0 / 3.0
          and abs(R_y / R - 1.0) <= 1e-4 and np.all(np.isfinite(y)))
    a = np.sqrt(g * R * T)
    vt = float(p.get("v", 0.0))                                  # the azimuthal velocity of the phase (THOR: the mean swirl)
    Mx = np.sqrt(max(M * M - (vt / a) ** 2, 0.0))
    T0c = T * (1 + 0.5 * (g - 1) * M * M)
    P0c = pr * (T0c / T) ** (g / (g - 1))
    a2 = (Mx - 1.0 >= MN_LINE and abs(T0c / T0 - 1) <= tol_stag and abs(P0c / P0 - 1) <= tol_stag)
    prof = p.get("profile")
    cro = 0.0
    if prof:                                                      # layered data: {r: [...], p: [...]} across the gap, parallel extraction
        r_, p_ = np.asarray(prof["r"], float), np.asarray(prof["p"], float)
        cro = float(np.max(np.abs(np.gradient(p_, r_))) * (r_[-1] - r_[0]) / np.mean(p_))
    a3 = cro <= CROCCO_LINE
    return a1, a2, a3, dict(R_err=R_y / R - 1, sumY=y.sum() - 1, Mn_margin=Mx - 1, T0_err=T0c / T0 - 1, P0_err=P0c / P0 - 1, crocco=cro)


def audit_family(path, T_lo, T_hi, tag, tol_stag):
    P = json.load(open(path))["phases"]
    res = [audit_phase(p, T_lo, T_hi, tol_stag) for p in P]
    D = [r[3] for r in res]
    print("-- %s: %d states (%s) --" % (tag, len(P), os.path.basename(path)))
    check("A-1 %s: complete and physical (worst |sum Y - 1| %.1e, worst R vs composition %.1e, T/T0 inside [%g, %g] K)"
          % (tag, max(abs(d["sumY"]) for d in D), max(abs(d["R_err"]) for d in D), T_lo, T_hi), all(r[0] for r in res))
    check("A-2 %s: Lemma 4 -- smallest normal-Mach margin %.3f >= %.2f; stagnation state as recorded (worst T0 %.1e, P0 %.1e <= %.0e)"
          % (tag, min(d["Mn_margin"] for d in D), MN_LINE, max(abs(d["T0_err"]) for d in D), max(abs(d["P0_err"]) for d in D), tol_stag),
          all(r[1] for r in res))
    check("A-3 %s: Crocco, parallel extraction -- worst radial-gradient residual %.1e <= %.0e (uniform phases: identically zero)"
          % (tag, max(d["crocco"] for d in D), CROCCO_LINE), all(r[2] for r in res))
    return P


def main():
    print("== [F2a] the data admission audits, stage A [X-ADMA] ==")
    args = sys.argv[1:]
    fams = [(args[i], float(args[i + 1]), float(args[i + 2]), args[i + 3], 1e-3) for i in range(0, len(args), 4)] if args else DEFAULT
    P = None
    for f in fams:
        P = audit_family(*f) if P is None else (audit_family(*f) and P)
    # ---- the rejectors, planted on a copy of the methane family's first phase
    print("-- rejectors (planted, must fire) --")
    base = json.load(open(DEFAULT[1][0]))["phases"][0]
    r1 = copy.deepcopy(base); r1["mach"] = 0.95; r1["T0"] = r1["T"] * (1 + 0.5 * (r1["gamma"] - 1) * 0.95 ** 2)
    r1["P0"] = r1["p"] * (r1["T0"] / r1["T"]) ** (r1["gamma"] / (r1["gamma"] - 1))
    check("R-1 a phase leaving the plane at M 0.95 FAILS A-2", not audit_phase(r1, 300.0, 4200.0, 1e-6)[1])
    r2 = copy.deepcopy(base); k = max(r2["Y"], key=r2["Y"].get); r2["Y"][k] += 0.01
    check("R-2 a phase whose composition sums to 1.01 FAILS A-1", not audit_phase(r2, 300.0, 4200.0, 1e-6)[0])
    r3 = copy.deepcopy(base); rr = np.linspace(0.792 * 0.068, 0.068, 33)
    r3["profile"] = dict(r=rr.tolist(), p=(base["p"] * (1 + 0.10 * (rr - rr[0]) / (rr[-1] - rr[0]))).tolist())
    check("R-3 a layered phase with a 10 percent radial pressure rise in parallel flow FAILS A-3", not audit_phase(r3, 300.0, 4200.0, 1e-6)[2])
    print("VERDICT: %s" % ("PASS" if OK else "FAIL"))
    sys.exit(0 if OK else 1)


if __name__ == "__main__":
    main()
