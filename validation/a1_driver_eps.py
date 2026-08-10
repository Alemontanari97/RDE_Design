#!/usr/bin/env python3
"""A1 BRICK 2, STEP 3 [F2/A1]: FIRST OPTIMIZATION — one knob (eps), with
a KNOWN-ANSWER oracle. The march + score (step 1) + meter (step 2) are
driven by a derivative-free 1-D search, and the result is checked
against the closed-form optimum the exit-area lemma predicts.

THE PROBLEM POSED. Fix an ambient pressure pa > 0 and maximize J(eps) =
mdot*q_e + (p_e - pa)*A_e over the area ratio, all other knobs at the
twin-case values. The exit-area lemma (dJ/dA_e = P_e - pa) says the
optimum sits EXACTLY where the exit pressure matches ambient:
p_e(eps*) = pa. Because mdot is set by the throat alone (invariant in
eps) and the march's own area law ties eps to the exit Mach, eps* has a
CLOSED FORM through the gas tables:

    choose target Me_t  ->  pa := p(Me_t)         (the posed ambient)
    eps* = mdot / (pi yt^2 rho(q_t) q_t)          (area law at Me_t)

The optimizer knows NOTHING of this: it only calls the march and reads
J. PASS = it lands on eps* anyway.

CHECKS (derived bands, R5):
  C1  |p_e(eps_gs) - pa| <= Richardson band of p_e (coarse vs refined
      march at the found optimum) + golden-window sensitivity.
  C2  J(eps_gs) >= J(eps*) - band_J: the found optimum is not worse
      than the analytic one beyond the derived flatness band.
  C3  corner meter at the found optimum reads ~0 at pa (step 2's
      instrument certifying step 3's result).
  R1  rejector: the same search on the CORRUPTED objective J without
      the pressure-area term must land AWAY from eps* (> 10x band).
      (Without (p_e-pa)A_e the integrand has no interior optimum in
      the bracket: monotone toward one end.)

CHECKPOINTING: every (eps -> J, Me, pe) evaluation is appended to
validation/_driver_eps_ckpt.json and reloaded on restart, so a timeout
costs only a rerun, not the evaluations.

Run:  .venv-a1/bin/python validation/a1_driver_eps.py
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1              # noqa: E402
import a1_thrust_functional as TF            # noqa: E402
import a1_corner_instrument as CI            # noqa: E402

import jax.numpy as jnp                      # noqa: E402

EPS = A1.EPS
CASE = A1.CASE
K_RICH = A1.K_RICH
CKPT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "_driver_eps_ckpt.json")
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def main():
    t0 = time.time()
    print("== A1 brick 2 step 3: eps optimization vs known answer"
          " [F2/A1] ==")
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    cfg = dict(NI=CASE["NI"], Ne=CASE["Ne"], da_deg=CASE["da_deg"])
    cfg_f = dict(NI=2 * CASE["NI"] - 1, Ne=2 * CASE["Ne"] - 1,
                 da_deg=0.5 * CASE["da_deg"])
    yt = CASE["yt"]

    ck = json.load(open(CKPT)) if os.path.exists(CKPT) else {}

    def march_at(eps, fine=False):
        key = "%s:%.6f" % ("f" if fine else "c", eps)
        if key in ck:
            return ck[key]
        P = jnp.array([CASE["yt"], CASE["rtu"], CASE["rtd"], eps])
        out, _ = A1.run_march(P, tab, cfg_f if fine else cfg)
        qe = float(TF.solve_qe(out["Me"], ta, tab["_as"]))
        pe = float(A1.state_q(jnp.float64(qe), ta)[1])
        rec = dict(J0=float(out["mdot"]) * qe
                   + pe * np.pi * float(out["wall_y"][-1]) ** 2,
                   mdot=float(out["mdot"]), Me=float(out["Me"]),
                   qe=qe, pe=pe, ylip=float(out["wall_y"][-1]),
                   uL=float(out["wall_u"][-1]),
                   vL=float(out["wall_v"][-1]))
        ck[key] = rec
        json.dump(ck, open(CKPT, "w"))
        return rec

    # ---------------- S1: pose the problem (closed-form target)
    print("-- S1: pose pa via target Me_t = 2.80; closed-form eps* --")
    qt = float(TF.solve_qe(jnp.float64(2.80), ta, tab["_as"]))
    st = A1.state_q(jnp.float64(qt), ta)
    pa, rho_t = float(st[1]), float(st[2])
    base = march_at(CASE["eps"])          # for the eps-invariant mdot
    eps_star = base["mdot"] / (np.pi * yt * yt * rho_t * qt)
    print("  pa = %.6e ; mdot = %.6e (eps-invariant) ; eps* = %.6f"
          % (pa, base["mdot"], eps_star))

    def J_of(rec, drop_pa_term=False):
        if drop_pa_term:
            return rec["mdot"] * rec["qe"]
        return rec["J0"] - pa * np.pi * rec["ylip"] ** 2

    # ---------------- S2: golden-section search (knows nothing of eps*)
    print("-- S2: golden search on [3.2, 8.0], xtol 0.04 --")
    gr = 0.5 * (np.sqrt(5.0) - 1.0)
    a, b = 3.2, 8.0
    c, d = b - gr * (b - a), a + gr * (b - a)
    fc, fd = J_of(march_at(round(c, 6))), J_of(march_at(round(d, 6)))
    nev = 3
    while b - a > 0.04:
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = J_of(march_at(round(c, 6)))
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = J_of(march_at(round(d, 6)))
        nev += 1
        print("    bracket [%.4f, %.4f]  (%d evals, %.0f s)"
              % (a, b, nev, time.time() - t0))
    eps_gs = 0.5 * (a + b)
    print("  eps_gs = %.5f  vs eps* = %.5f  (|d| = %.4f)"
          % (eps_gs, eps_star, abs(eps_gs - eps_star)))

    # ---------------- S3: certificates
    print("-- S3: certificates --")
    rc = march_at(round(eps_gs, 6))
    rf = march_at(round(eps_gs, 6), fine=True)
    band_pe = K_RICH * abs(rc["pe"] - rf["pe"]) + A1.C_FLOOR * EPS * pa
    # golden-window sensitivity of pe: |dpe/deps| ~ |pe(c)-pe(d)|/(d-c)
    slope = abs(ck["c:%.6f" % round(c, 6)]["pe"]
                - ck["c:%.6f" % round(d, 6)]["pe"]) / max(abs(d - c), 1e-9)
    band1 = band_pe + slope * (b - a)
    d1 = abs(rf["pe"] - pa)
    print("  C1: |p_e(eps_gs) - pa| = %.3e  band = %.3e" % (d1, band1))
    check("C1 exit pressure matches ambient at the found optimum",
          d1 <= band1)

    rs = march_at(round(eps_star, 6))
    dJ = J_of(rs) - J_of(rc)
    band_J = K_RICH * abs(J_of(rc) - (rf["J0"] - pa * np.pi
                                      * rf["ylip"] ** 2)) \
        + A1.C_FLOOR * EPS * abs(J_of(rc))
    print("  C2: J(eps*) - J(eps_gs) = %+.3e  flatness band = %.3e"
          % (dJ, band_J))
    check("C2 found optimum not worse than analytic beyond band",
          dJ <= band_J)

    out_like = dict(wall_u=jnp.array([rf["uL"]]),
                    wall_v=jnp.array([rf["vL"]]))
    Rcorner = CI.corner_residual(out_like, ta, pa)
    print("  C3: corner meter at optimum, pa: R = %+.3e  (band %.3e)"
          % (Rcorner, band1))
    check("C3 corner instrument reads ~0 at the optimum",
          abs(Rcorner) <= band1)

    # ---------------- S4: rejector — corrupted objective
    print("-- S4: rejector R1 (objective without the pressure-area"
          " term) --")
    evs = sorted((float(k.split(":")[1]), J_of(v, drop_pa_term=True))
                 for k, v in ck.items() if k.startswith("c:"))
    j_bad = [j for _, j in evs]
    mono = all(j_bad[i + 1] >= j_bad[i] - abs(j_bad[i]) * 1e-12
               for i in range(len(j_bad) - 1))
    e_bad = evs[int(np.argmax(j_bad))][0]
    print("  corrupted J: argmax at eps = %.4f (bracket edge %s);"
          " monotone = %s" % (e_bad, "yes" if e_bad >= evs[-1][0] else
                              "no", mono))
    check("R1 corrupted objective lands away from eps* (> 10x window)",
          abs(e_bad - eps_star) > 10.0 * 0.04)

    print("== %d/%d PASS  (%.1f s, %d march evals) ==" %
          (NPASS[0], NPASS[1], time.time() - t0, nev))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()
