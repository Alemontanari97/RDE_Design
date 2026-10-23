#!/usr/bin/env python3
"""GATE of QNTR_WORKERS (2026-10-23, a1_qntr.SecantPool; [F3.TWIN] infrastructure
after the revalidation): the secant Hessians' columns on spawned workers.

WHAT IT GRADES. The switch claims to change the walk's TIME and nothing else.
The claim is graded bit for bit, never to a tolerance:
  unit -- at the certified landing of the methane Rao walk t08b C0 (record in
          _revalidation_2026-10-07/out/): the secant Hessian of J serial against
          the pool, every entry and the unmeasurable-column list bitwise; the two
          times. REJECTORS: the pool's gradient at W moved by ONE unit in the last
          place on one component must differ from the serial one at W (and equal
          it at W); a killed worker must surface as SecantWorkerDied (a
          BaseException, never a rejected trial).
  walk -- two certified walks re-run through their harness scripts with
          QNTR_WORKERS set (the planar B0, whose posing does not pickle: the
          serial secant, said aloud; the methane C0: the pool) (output redirected, nothing in the repository
          rewritten): landing W and J, the accepted-base history and the
          report's counts identical to the certified records; the wall times.
Usage: python validation/qntr_workers_gate.py unit|walk   (env QNTR_GATE_WORKERS,
default 4; launch on that many cores plus one). Needs the revalidation's GENO
run outputs (geno/rao_sdt_L0448: not in git, see its md5 manifest).
"""
import json
import os
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RVD = os.path.join(HERE, "_revalidation_2026-10-07")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(RVD, "ref"))
NW = int(os.environ.get("QNTR_GATE_WORKERS", "4"))
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def certified(name):
    return json.load(open(os.path.join(RVD, "out", name + ".json")))


def posing():
    """The methane Rao posing of t08b exactly as its harness script builds it, and
    W at the certified landing of its walk C0 (the posings whose secant is 85-94
    percent of the walk). The planar posing does not pickle (its fan keeps a local
    function): run_trsqp keeps the serial secant there, graded by the walk part."""
    import numpy as np
    import rv
    import rao_posing as RP
    rp = RP.RaoPosing(os.path.join(rv.RV, "geno", "rao_sdt_L0448"), K=120, n_fan=20, m=10, design=True)
    W = np.asarray(certified("t08b_walk_C0_qntr")["landing"]["W"], float)
    return "methane C0", dict(throat=rp), rp.ta, W


def unit():
    import numpy as np
    import a1_plug_spline_opt as P
    import a1_qntr as QN
    h = float(os.environ.get("QNTR_GATE_H", "1e-4"))     # a1_qntr's h = tr0 / 100 at the harness's tr0 0.01
    t00 = time.time()
    print("== QNTR_WORKERS unit: secant Hessian of J serial against %d workers (a1_qntr.run measures only J's) =="
          % NW, flush=True)
    lab, c, ta, W = posing()
    hooks = P._qntr_hooks({}, c, ta, None)
    rec = lambda z: P.march_record(z, {}, c)          # noqa: E731
    ws = QN.Walk(rec, hooks["J"], verbose=0)
    pt, why = ws.evaluate(W)
    if not check("%s: the certified landing marches and certifies (%s)" % (lab, why or "ok"), pt is not None):
        return 1
    t = time.time()
    A, ba = ws.secant(pt, h, "J")
    t_s = time.time() - t
    pool = QN.SecantPool(NW, "a1_plug_spline_opt", "_qntr_hooks", ({}, c, ta, None))
    wp = QN.Walk(rec, hooks["J"], verbose=0, pool=pool)
    t = time.time()
    B, bb = wp.secant(pt, h, "J")
    t_p = time.time() - t
    check("U %s, secant of J (%dx%d): bitwise %s, max |diff| %.1e, unmeasurable columns %s / %s"
          % (lab, len(A), len(A), bool(np.array_equal(A, B)), float(np.max(np.abs(A - B))), ba, bb),
          bool(np.array_equal(A, B)) and ba == bb)
    print("   %s: serial %.1f s, %d workers %.1f s (x%.2f; under the machine's load of the moment)"
          % (lab, t_s, NW, t_p, (t_s / t_p if t_p > 0 else float("nan"))), flush=True)
    # REJECTOR 1: one unit in the last place on one component must show (one gradient each side)
    e0 = np.zeros(len(W))
    e0[0] = h
    W1 = pt["W"].copy()
    W1[0] = np.nextafter(W1[0], np.inf)
    g_ser = np.asarray(hooks["J"](pt["W"] + e0, pt["sched"])[1], float)
    g_one = pool.grads("J", [W1 + e0], pt["sched"])[0]
    g_same = pool.grads("J", [pt["W"] + e0], pt["sched"])[0]
    check("R-1 the pool's gradient at W_0 + 1 ulp differs from the serial one at W (max |diff| %.1e; must differ),"
          " at W itself it is the serial one (%s)" % (float(np.max(np.abs(g_one - g_ser))), bool(np.array_equal(g_same, g_ser))),
          (not np.array_equal(g_one, g_ser)) and bool(np.array_equal(g_same, g_ser)))
    # REJECTOR 2: a dead worker is an infrastructure fault
    pool.procs[0].terminate()
    pool.procs[0].join()
    caught = None
    try:
        wp.secant(pt, h, "J")
    except BaseException as err:          # noqa: B902 -- the point of the test
        caught = err
    check("R-2 a killed worker surfaces as %s (an Exception: %s)" % (type(caught).__name__, isinstance(caught, Exception)),
          isinstance(caught, QN.SecantWorkerDied) and not isinstance(caught, Exception))
    pool.close()
    print("\n== %d/%d PASS  (%.0f s) ==" % (NPASS[0], NPASS[1], time.time() - t00), flush=True)
    print("VERDICT: %s" % ("PASS" if NPASS[0] == NPASS[1] else "FAIL"), flush=True)
    return 0 if NPASS[0] == NPASS[1] else 1


def walk():
    import numpy as np
    outdir = tempfile.mkdtemp(prefix="qntr_workers_gate_")
    t00 = time.time()
    print("== QNTR_WORKERS walk: certified walks re-run with %d workers (output in %s) ==" % (NW, outdir), flush=True)
    for script, argv, rec in (("t08a_planar_walk.py", ["B", "0"], "t08a_walk_B0_K80_qntr"),
                              ("t08b_rao_walk.py", ["C", "0"], "t08b_walk_C0_qntr")):
        path = os.path.join(RVD, "tests", script)
        code = ("import sys, runpy; sys.path.insert(0, %r); import rv; rv.OUT = %r; rv.FIGS = %r; "
                "sys.argv = [%r] + %r; runpy.run_path(%r, run_name='__main__')"
                % (os.path.join(RVD, "ref"), outdir, outdir, path, argv, path))
        env = dict(os.environ, QNTR_WORKERS=str(NW))
        t = time.time()
        r = subprocess.run([sys.executable, "-c", code], cwd=os.path.join(RVD, "tests"), env=env,
                           capture_output=True, text=True)
        sec = time.time() - t
        open(os.path.join(outdir, rec + ".log"), "w").write(r.stdout + r.stderr)
        try:
            new, new_rep = (json.load(open(os.path.join(outdir, rec + s + ".json"))) for s in ("", "_report"))
        except FileNotFoundError as err:
            check("%s: the walk ran (exit %d, %s; log %s)" % (rec, r.returncode, err, outdir), False)
            continue
        old, old_rep = certified(rec), certified(rec + "_report")
        keys = ("stop", "segments", "accepted", "rejected", "records", "secants", "gradients")
        same = (np.array_equal(np.asarray(new["landing"]["W"], float), np.asarray(old["landing"]["W"], float))
                and new["landing"]["J"] == old["landing"]["J"]
                and np.array_equal(np.asarray(new["hist"], float), np.asarray(old["hist"], float))
                and all(new_rep.get(k) == old_rep.get(k) for k in keys))
        check("W %s with %d workers: landing W, J %.12f, history and counts %s identical to the certified record"
              % (rec, NW, new["landing"]["J"], "/".join(keys)), same)
        print("   %s: %.0f s with %d workers (record: %.0f s, of which secant %.0f s; the record's load is not this one)"
              % (rec, sec, NW, old_rep.get("seconds", float("nan")), old_rep.get("t_secant", float("nan"))), flush=True)
    print("\n== %d/%d PASS  (%.0f s) ==" % (NPASS[0], NPASS[1], time.time() - t00), flush=True)
    print("VERDICT: %s" % ("PASS" if NPASS[0] == NPASS[1] else "FAIL"), flush=True)
    return 0 if NPASS[0] == NPASS[1] else 1


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode not in ("unit", "walk"):
        raise SystemExit("usage: qntr_workers_gate.py unit|walk")
    sys.exit(unit() if mode == "unit" else walk())
