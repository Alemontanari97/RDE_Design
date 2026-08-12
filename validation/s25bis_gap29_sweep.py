#!/usr/bin/env python3
"""[GAP-29 / AUDIT:426, S25-bis] halved-constants sensitivity sweep —
executes the AUDIT_agnostic_2026-08-07 engine-core:F5 prescribed test
(never executed until now; gap-map GAP-29 + choice-ledger C17/C18):
re-run the verdict-bearing checks with each asserted factor HALVED —
any PASS -> FAIL flip identifies a tolerance whose factor-2 margin is
LOAD-BEARING and must be derived (op-count/condition bound) or
reclassified; a no-flip result justifies the factor as carrying >= 2x
measured headroom (documented, not "derived").

ARMS (each in its OWN subprocess — the constants are read at
solver-build/trace time, so in-process re-patching would silently
reuse stale compiled bodies through the keyed caches):
  base     NEWTON_TOL_FACTOR=100, C_FLOOR=8, C_OPS=100 (of record)
  ntf50    NEWTON_TOL_FACTOR=50  (halves every NTF-built band AND
           the Newton termination bound; covers the x10 headroom
           rows scaled by it)
  cfloor4  C_FLOOR=4             (O3.1 / R-GRAD floor half)
  cops50   C_OPS=50              (thermotab uniformity-rejector bound
           + the K_NEWT derivation's floor input)

ROWS per arm (bounded, defnoz class of record, mild gate net):
  build_c1 (uniformity rejector + derived K_NEWT), fresh record
  cert verdict, replay fidelity vs its own band, O3.1 spot verdict.

Flips are DATA (reported + artifact), never silently absorbed; the
named owner for any derivation duty they create is F2 (gap-map C18
placement). Exit 0 iff every arm completes and the comparison table
prints.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARMS = dict(base=(100.0, 8.0, 100.0), ntf50=(50.0, 8.0, 100.0),
            cfloor4=(100.0, 4.0, 100.0), cops50=(100.0, 8.0, 50.0))


def run_arm(name):
    ntf, cfloor, cops = ARMS[name]
    print("== [GAP-29] arm %s: NEWTON_TOL_FACTOR=%g C_FLOOR=%g "
          "C_OPS=%g ==" % (name, ntf, cfloor, cops))
    sys.path.insert(0, HERE)
    import numpy as np
    import jax
    import jax.numpy as jnp
    import a1_ideal_march_jax as A1
    import thermotab_c1_jax as TH
    # patch BEFORE any solver/table build (trace-time constants)
    A1.NEWTON_TOL_FACTOR = ntf
    A1.C_FLOOR = cfloor
    TH.C_OPS = cops
    import a1_toc_variational_jax as TV
    import def_twin_falsifier as DT
    from adaptive_knot_optimize import grad_and_J as AK_gJ, \
        o31_spot as AK_o31
    jax.config.update("jax_enable_x64", True)
    rows = dict(arm=name, ntf=ntf, cfloor=cfloor, cops=cops)
    # (1) thermotab build: uniformity rejector + derived K_NEWT
    try:
        tab0 = A1.prep_tab(A1.build_tab_nasa())
        c1 = TH.build_c1(tab0)
        rows["c1_build"] = "PASS"
        rows["k_newt"] = int(c1["K_NEWT"])
    except Exception as e:
        rows["c1_build"] = "FAIL: %s" % str(e)[:120]
        rows["k_newt"] = None
    print("  c1 build: %s (K_NEWT %s)" % (rows["c1_build"],
                                          rows["k_newt"]))
    # (2) defnoz mild-net record + replay + O3.1
    DT.CASE["NI"], DT.CASE["Nw"], DT.CASE["da_deg"] = 11, 30, 1.0
    tab, state_fn, solv, cfg = DT.setup_engine()
    leg1 = json.load(open(DT.ART_LEG1))
    wx = np.array(leg1["res"]["r1"]["obs"]["wall_x"])
    wy = np.array(leg1["res"]["r1"]["obs"]["wall_y"])
    W, thB, rep = DT.wall_to_class(wx, wy, cfg, DT.M_NODES)
    W = np.asarray(W, float)
    old = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    try:
        out, plan = TV.run_toc_record(W, tab, cfg, state_fn=state_fn,
                                      solvers=solv)
        rows["cert_worst"] = float(out["cert_worst"])
        rows["cert_verdict"] = ("PASS" if out["cert_worst"] <= 1.0
                                else "FAIL")
        runj = TV.make_run_toc_scan_jit(tab, cfg, plan,
                                        state_fn=state_fn,
                                        solvers=solv)
        wall_sc = runj(jnp.asarray(W))
        dev = float(jnp.max(jnp.abs(wall_sc - out["wall"])))
        scale = float(jnp.max(jnp.abs(out["wall"])))
        band = A1.NEWTON_TOL_FACTOR * DT.EPS * scale * 10.0
        rows["replay_dev"] = dev
        rows["replay_band"] = band
        rows["replay_verdict"] = "PASS" if dev <= band else "FAIL"
        J_w, g_w, scalJ = AK_gJ(W, None, tab, cfg, plan, state_fn,
                                solv)
        dp, tol = AK_o31(W, None, scalJ, g_w, J_w)
        rows["o31_dp"] = float(dp)
        rows["o31_tol"] = float(tol)
        rows["o31_verdict"] = "PASS" if dp <= tol else "FAIL"
    except Exception as e:
        rows["cert_verdict"] = "RAISE: %s" % str(e)[:120]
        rows.setdefault("replay_verdict", "NOT-RUN")
        rows.setdefault("o31_verdict", "NOT-RUN")
    finally:
        TV.M_NODES, TV.KNOT_XI = old
    print("  record cert %.3e -> %s; replay %s (%.3e vs %.3e); "
          "O3.1 %s (%.3e vs %.3e)"
          % (rows.get("cert_worst", float("nan")),
             rows["cert_verdict"], rows.get("replay_verdict"),
             rows.get("replay_dev", float("nan")),
             rows.get("replay_band", float("nan")),
             rows.get("o31_verdict"), rows.get("o31_dp", float("nan")),
             rows.get("o31_tol", float("nan"))))
    path = os.path.join(HERE, "s25bis_gap29_%s.json" % name)
    json.dump(rows, open(path, "w"), indent=1)
    return 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ARMS:
        return run_arm(sys.argv[1])
    print("== [GAP-29] halved-constants sweep (AUDIT:426 executed; "
          "4 arms, each its own subprocess) ==")
    ok = True
    for name in ("base", "ntf50", "cfloor4", "cops50"):
        r = subprocess.run([sys.executable, os.path.abspath(__file__),
                            name], cwd=HERE)
        if r.returncode != 0:
            print("  arm %s FAILED to complete (exit %d)"
                  % (name, r.returncode))
            ok = False
    if not ok:
        print("VERDICT: FAIL (arm incomplete)")
        return 1
    arms = {n: json.load(open(os.path.join(
        HERE, "s25bis_gap29_%s.json" % n)))
        for n in ("base", "ntf50", "cfloor4", "cops50")}
    print("-- flip table (PASS->FAIL vs base = load-bearing margin, "
          "owner F2) --")
    flips = []
    for n in ("ntf50", "cfloor4", "cops50"):
        for rowk in ("c1_build", "cert_verdict", "replay_verdict",
                     "o31_verdict"):
            b = str(arms["base"].get(rowk, ""))
            a = str(arms[n].get(rowk, ""))
            flip = b.startswith("PASS") and not a.startswith("PASS")
            print("  %-8s %-14s base=%s -> %s%s"
                  % (n, rowk, b[:24], a[:24],
                     "   ** FLIP **" if flip else ""))
            if flip:
                flips.append((n, rowk))
    kb, kn = arms["base"].get("k_newt"), arms["cops50"].get("k_newt")
    if kb != kn:
        print("  note: derived K_NEWT moved %s -> %s under C_OPS/2 "
              "(derivation responds to its floor input — expected "
              "behavior, not a flip)" % (kb, kn))
    print("GAP-29 SWEEP DATUM: %d flip(s)%s"
          % (len(flips), (" -> derivation duty rows for F2: %s"
                          % flips) if flips else
             " — every halved factor keeps >= 2x measured headroom "
             "on these rows (margin documented, constants stay "
             "convention-classified)"))
    json.dump(dict(arms=arms, flips=flips),
              open(os.path.join(HERE, "s25bis_gap29_sweep.json"),
                   "w"), indent=1)
    print("VERDICT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
