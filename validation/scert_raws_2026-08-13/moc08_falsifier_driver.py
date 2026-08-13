#!/usr/bin/env python3
"""MOC-08 economic falsifier of claim 19 (S-CERT hook 2a, enrolled in
the MC1/MC2 sample; the A36/C33 review's derived lever).

CLAIM ATTACKED: the +0.51%-class in-class surplus DELTA between two
designs of the deftw case is IVL-refinement-insensitive because the
log-amplified DWR strip lives downstream of an IVL/throat IDENTICAL
for both designs (common mode, cancels in the difference).

FALSIFIER: re-march the committed designs at critical-speed
refinement M_IVL - 1 in {5e-6 (the GENO constant of record),
5e-4 (100x coarser; ln-budget drops by 4.6)} and verify (i) the
committed J_def reproduces at baseline, (ii) the PAIR DIFFERENCE
DJ does not drift beyond the pair's own committed band (band_f7).

DECLARED LIMIT (audit finding, registered): the F7 direct-side design
vector was never persisted (s24_deftw_campaign.json absent from disk
and from git history) — the executable pair TODAY is (W0, W16), the
two committed class representatives of the same case, which share
the IVL/throat exactly as the claim-19 pair does. The F7-side
non-reproducibility is itself an MC7 finding — filed of record at
the S-CERT closing window as findings-registry row
provenance:f7-design-vector-irrecoverable (the audit caught this
docstring claiming 'filed separately' BEFORE the row existed:
repaired by filing the row, not the wording).

KNOB (no tree edit): tab["_as"] re-solved for the perturbed target
Mach by the same damped iteration prep_tab uses (re-implemented here
parametrically; the engine reads only tab["_as"]).
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VAL = os.path.dirname(HERE)
sys.path.insert(0, VAL)

import jax                                        # noqa: E402
import jax.numpy as jnp                           # noqa: E402
import a1_ideal_march_jax as A1                   # noqa: E402
import a1_toc_variational_jax as TV               # noqa: E402
import o33_bench as O33                           # noqa: E402

jax.config.update("jax_enable_x64", True)
EPS = float(np.finfo(np.float64).eps)


def solve_as(tab, m_target):
    """Parametric twin of prep_tab's critical-speed solve."""
    ta = A1.tab_arrays(tab)
    g, Rg, ts = tab["gammamedio"], tab["Rg"], tab["ts"]
    q = float(np.sqrt(2.0 * g * Rg * ts / (g + 1.0)))
    for _ in range(80):
        _, _, _, c, _, M = A1.state_q(jnp.float64(q), ta)
        q = q - float((M - m_target) * c)
    return float(q)


def march_J(W, tab, cfg, state_fn, solv):
    W = np.asarray(W, float)
    old_cls = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    try:
        out, plan = TV.run_toc_record(W, tab, cfg, state_fn=state_fn,
                                      solvers=solv, return_field=True)
        runj = TV.make_run_toc_scan_jit(tab, cfg, plan,
                                        state_fn=state_fn, solvers=solv)
        J = float(TV.thrust_J(runj(jnp.asarray(W)), tab,
                              state_fn=state_fn))
    finally:
        TV.M_NODES, TV.KNOT_XI = old_cls
    return J, float(out["cert_worst"]), int(out["cert_n"])


def main():
    print("== MOC-08 falsifier driver (S-CERT 2026-08-13, hook 2a) ==")
    der = json.load(open(os.path.join(VAL, "s24_deftw_derive.json")))
    f37 = json.load(open(os.path.join(VAL, "s24_deftw_f3f7.json")))
    cfg = dict(der["case"])
    eps_area = cfg.pop("eps")
    W0 = np.asarray(der["W0"], float)
    W16 = np.asarray(der["W16"], float)
    J_def_committed = float(f37["J_def"])
    J_def16_committed = float(der["tail"]["J_def16"]) if "tail" in der \
        else float(f37.get("J_def16", 0.0)) or None
    band_f7 = float(f37["band_f7"])

    tab = A1.prep_tab(A1.build_tab_nasa())
    state_c1, solv, _cfg_o33 = O33.make_case(tab)
    as_base = float(tab["_as"])

    results = {}
    for tag, mt in (("5e-6", 1.000005), ("5e-4", 1.0005)):
        tab["_as"] = solve_as(tab, mt)
        print("  [offset %s] M_target %.6f -> as = %.9e (base %.9e, "
              "shift %.2e rel)" % (tag, mt, tab["_as"], as_base,
                                   (tab["_as"] - as_base) / as_base))
        J0, cw0, cn0 = march_J(W0, tab, cfg, state_c1, solv)
        J16, cw16, cn16 = march_J(W16, tab, cfg, state_c1, solv)
        print("    J(W0)  = %.7e (cert worst %.3e, %d cells)"
              % (J0, cw0, cn0))
        print("    J(W16) = %.7e (cert worst %.3e, %d cells)"
              % (J16, cw16, cn16))
        results[tag] = dict(J0=J0, J16=J16, dJ=J16 - J0,
                            cw=(cw0, cw16))
    tab["_as"] = as_base

    ok = True
    # (i) MC1 reproduction row at baseline
    rep = abs(results["5e-6"]["J0"] - J_def_committed)
    print("  [MC1] J_def baseline reproduction: %.7e vs committed "
          "%.7e -> |delta| = %.3e (band_f7 %.3e)"
          % (results["5e-6"]["J0"], J_def_committed, rep, band_f7))
    ok &= (rep <= band_f7)
    print("  [%s] committed J_def reproduces at the 5e-6 offset of "
          "record" % ("PASS" if rep <= band_f7 else "FAIL"))
    # (ii) the falsifier row: DJ drift across offsets vs the pair band
    drift = abs(results["5e-4"]["dJ"] - results["5e-6"]["dJ"])
    print("  [MOC-08] DJ(5e-6) = %.6e ; DJ(5e-4) = %.6e ; "
          "|drift| = %.3e vs band_f7 = %.3e"
          % (results["5e-6"]["dJ"], results["5e-4"]["dJ"], drift,
             band_f7))
    fires = drift > band_f7
    print("  [%s] MOC-08: the pair difference is IVL-refinement-"
          "insensitive within its own band (claim-19 common-mode "
          "mechanism %s)"
          % ("PASS" if not fires else "FAIL",
             "HOLDS" if not fires else "FALSIFIED"))
    ok &= not fires
    out = dict(seed_note="deterministic, no sampling", results=results,
               J_def_committed=J_def_committed, band_f7=band_f7,
               drift=drift, verdict=("PASS" if ok else "FAIL"))
    json.dump(out, open(os.path.join(HERE, "moc08_results.json"), "w"),
              indent=1)
    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
