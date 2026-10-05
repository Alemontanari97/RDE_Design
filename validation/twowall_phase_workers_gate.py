#!/usr/bin/env python3
"""GATE of the two speed switches of the two-wall walk (2026-10-05, [F3.TWIN]
infrastructure; a1_twowall: TWOP_PHASE_WORKERS, TWOP_SKIP_LADDER).

WHAT IT GRADES. Both switches claim to change the walk's TIME and nothing
else. The claim is graded bit for bit, never to a tolerance:
  unit  -- at a frozen design of the 12-phase arm (checkpoint_B24.json): the
           12-phase record (every phase's output and schedule, the combined
           J, certificate and margin), the objective's value and gradient on
           the frozen schedules (in W and in the walk's z coordinates of
           TWOP_BASIS), serial against TWOP_PHASE_WORKERS; REJECTORS: the
           same comparison at W moved by ONE unit in the last place on one
           component must find the difference; the phases' gradients summed
           in the other order must be told apart; a killed worker must
           surface as PhaseWorkerDied (a BaseException, never a rejected
           design).
  walks -- two short walks resumed from the same checkpoint and compared
           line by line (segment lines, checkpoints, the return line and the
           record's design): (L) the mean-state walk with and without the
           start ladder; (P) the 12-phase walk serial and with the workers,
           both without the ladder.
Usage: python twowall_phase_workers_gate.py unit|walks   (env PPG_WORKERS,
default 12; walks: PPG_CPUS_SERIAL = three cores, PPG_CPUS_PAR = the workers'
cores, PPG_SEGS = segments past the checkpoint, default 2).
The posing is the arm B of A-INST (SDT methane, 87 mm plug, 0.5 atm; class at
the mean state), its environment copied from the arm's live process.
"""
import json
import os
import pickle
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
GD = os.path.join(HERE, "_twowall_phase_workers")
CK = os.path.join(GD, "checkpoint_B24.json")
MAIN = "/data10/falco/RDE/RDE_Design/validation"          # the arm's data (class, gas, family)
HAND = "/data10/falco/RDE/handoff/plug_2026-09-29"
ENV_B = {
    "A1_NEWTON_RESCUE": "1", "PSPL_BACKTRACK": "4", "PSPL_FLOOR_LIMIT": "1", "PSPL_JSCALE": "radius",
    "PSPL_TRFOLLOW": "1", "TWOP_BASIS": HAND + "/basis_plug_only.json", "TWOP_CAP": "0.8",
    "TWOP_CLASS": MAIN + "/_rde_tournament/stech/class_nofold_2026-09-28.json",
    "TWOP_FIX": '{"xa_s": 0.0294, "ta_s": 1e-09, "u_s": -0.44419306935689357}', "TWOP_FREE_EXIT": "both",
    "TWOP_GAS": MAIN + "/_cycle_family/sdt_ch4_phi1_pcp20/gas_mean.json", "TWOP_ITERS": "12", "TWOP_JET": "1",
    "TWOP_KERNEL": "arc", "TWOP_MU_CLASS": "ref", "TWOP_MU": MAIN + "/_cycle_family/sdt_ch4_phi1_pcp20/family_K12.json",
    "TWOP_NOPLUME": "1", "TWOP_PA": "0.024378", "TWOP_REGION": "RC", "TWOP_SEP_CLASS": "1", "TWOP_SEP": "summerfield",
    "TWOP_SHAPE": "1", "TWOP_STAGE": "walk", "TWOP_START": "F", "TWOP_START_FROM": HAND + "/sdt/start_rao_sdt.json",
    "TWOP_TR0": "0.008073525393645567", "TWOP_U0": "10", "TWOP_U0_S": "-10",
}
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def same(a, b, path="", diffs=None):
    """Bitwise equality of nested outputs (dicts, lists, arrays, scalars,
    schedules): the list of the paths that differ."""
    import numpy as np
    diffs = [] if diffs is None else diffs
    if hasattr(a, "__dict__") and type(a).__name__ in ("Sched", "MuSched"):
        return same(vars(a), vars(b), path + ".", diffs)
    if isinstance(a, dict):
        if set(a) != set(b):
            diffs.append(path + " keys")
            return diffs
        for k in a:
            same(a[k], b[k], "%s[%r]" % (path, k), diffs)
        return diffs
    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            diffs.append(path + " len")
            return diffs
        for i, (x, y) in enumerate(zip(a, b)):
            same(x, y, "%s[%d]" % (path, i), diffs)
        return diffs
    try:
        xa, xb = np.asarray(a), np.asarray(b)
    except Exception:
        if a != b:
            diffs.append(path)
        return diffs
    if xa.dtype == object or xb.dtype == object:
        if repr(a) != repr(b):
            diffs.append(path)
        return diffs
    if xa.shape != xb.shape or not np.array_equal(xa, xb, equal_nan=xa.dtype.kind == "f"):
        diffs.append(path)
    return diffs


def unit():
    import numpy as np
    for k, v in ENV_B.items():
        os.environ[k] = v
    os.environ["TWOP_ART"] = os.path.join(GD, "art_unit")
    os.environ.pop("TWOP_PHASE_WORKERS", None)
    os.makedirs(os.environ["TWOP_ART"], exist_ok=True)
    import jax
    import jax.numpy as jnp
    import a1_twowall as TW
    nw = int(os.environ.get("PPG_WORKERS", "12"))
    C = json.load(open(CK))
    W = np.asarray(C["W"], float)
    Ws, T = np.asarray(C["W_start"], float), np.asarray(C["T"], float)
    Z = np.asarray(C["Z"], float)
    Cr = json.load(open(os.environ["TWOP_CLASS"]))

    def mg(tw):
        return tw.margin_dict(mu0=Cr["floors"][0], rho=Cr["rho"], m_ref=Cr["m_ref"])

    def run(tw, Wx):
        t = time.time()
        o, S = tw.march_record(Wx, margin=mg(tw))
        t_rec = time.time() - t
        frozen = pickle.loads(pickle.dumps((o, S)))      # the record as returned, before any replay reads it
        t = time.time()
        J, g = jax.value_and_grad(lambda z: tw.J_replay(z, S))(jnp.asarray(Wx))
        g = np.asarray(g)
        t_g = time.time() - t
        Jv = float(tw.J_replay(jnp.asarray(Wx), S))
        M = TW.Metric(tw, Ws, T)
        Jz, gz = jax.value_and_grad(lambda z: M.J_replay(z, S))(jnp.asarray(Z))
        return dict(o=frozen[0], S=frozen[1], J=float(J), g=g, Jv=Jv, Jz=float(Jz), gz=np.asarray(gz), t_rec=t_rec, t_g=t_g)

    print("== [F3.TWIN] phase workers, unit: serial against %d workers at %s (C_F %.9f) ==" % (nw, CK, C["CF"]), flush=True)
    t0 = time.time()
    tws = TW.TwoWall(verbose=False)
    s = run(tws, W)
    print("   serial: record %.1f s, value and gradient %.1f s" % (s["t_rec"], s["t_g"]), flush=True)
    os.environ["TWOP_PHASE_WORKERS"] = str(nw)
    twp = TW.TwoWall(verbose=False)
    p = run(twp, W)                       # cold: the workers' first compile
    p = run(twp, W)
    print("   %d workers (warm): record %.1f s, value and gradient %.1f s" % (nw, p["t_rec"], p["t_g"]), flush=True)
    d_rec = same(s["o"], p["o"]) + same(s["S"], p["S"])
    check("U-1 the 12-phase record: every phase's output and schedule, J_mu %.12f, certificate, margin -- bitwise (%d"
          " differing paths%s)" % (p["o"]["J_mu"], len(d_rec), (": " + ", ".join(d_rec[:5])) if d_rec else ""), not d_rec)
    check("U-2 the objective on the frozen schedules: value %s, gradient in W %s (max |diff| %.1e) -- bitwise"
          % (s["J"] == p["J"], bool(np.array_equal(s["g"], p["g"])), float(np.max(np.abs(s["g"] - p["g"])))),
          s["J"] == p["J"] and bool(np.array_equal(s["g"], p["g"])))
    check("U-3 value without gradient %s; the walk's coordinates (TWOP_BASIS metric): value %s, gradient in z %s"
          % (s["Jv"] == p["Jv"], s["Jz"] == p["Jz"], bool(np.array_equal(s["gz"], p["gz"]))),
          s["Jv"] == p["Jv"] and s["Jz"] == p["Jz"] and bool(np.array_equal(s["gz"], p["gz"])))
    # REJECTOR 1: the comparator must see the smallest representable move of
    # one design component (one unit in the last place of W_0)
    W1 = W.copy()
    W1[0] = np.nextafter(W1[0], np.inf)
    r = run(twp, W1)
    d_r = same(s["o"], r["o"]) + same(s["S"], r["S"])
    check("R-1 rejector: at W_0 + 1 ulp (%.1e) the same comparison finds %d differing record paths, value %s, gradient %s"
          " (must differ)" % (W1[0] - W[0], len(d_r), "differs" if r["J"] != s["J"] else "SAME", "differs" if not np.array_equal(r["g"], s["g"])
                              else "SAME"), bool(d_r) and not np.array_equal(r["g"], s["g"]))
    # REJECTOR 3: the phases' gradients summed first-to-last (not the serial
    # reverse pass's last-to-first) must be told apart from the serial gradient
    twp._pool.send("Jg", W, p["S"].S, None)
    res = twp._pool.gather()
    g_fwd = None
    for k in range(len(twp.phases)):
        g_fwd = res[k][1].copy() if g_fwd is None else g_fwd + res[k][1]
    check("R-3 rejector: the same 12 phase gradients summed first-to-last differ from the serial gradient by %.1e"
          " (must differ: the summation order is part of the bitwise claim)" % float(np.max(np.abs(g_fwd - s["g"]))),
          not np.array_equal(g_fwd, s["g"]))
    # REJECTOR 2: a dead worker is an infrastructure fault, not a rejected design
    twp._pool.procs[0].terminate()
    twp._pool.procs[0].join()
    caught = None
    try:
        twp.march_record(W, margin=mg(twp))
    except BaseException as err:          # noqa: B902 -- the point of the test
        caught = err
    check("R-2 a killed worker surfaces as %s (an Exception: %s -- the driver's revert branch cannot catch it)"
          % (type(caught).__name__, isinstance(caught, Exception)),
          isinstance(caught, TW.PhaseWorkerDied) and not isinstance(caught, Exception))
    twp._pool.close()
    print("\n== %d/%d PASS  (%.0f s) ==" % (NPASS[0], NPASS[1], time.time() - t0), flush=True)
    print("VERDICT: %s" % ("PASS" if NPASS[0] == NPASS[1] else "FAIL"), flush=True)
    return 0 if NPASS[0] == NPASS[1] else 1


KEEP = re.compile(r"^\s*(\[seg|checkpoint at segment|return:|RESUMED|start F \(|Newton walk|ENDS|EXIT)")


def walk_lines(log):
    """The lines a walk's path is read from, timing and memory counts cut."""
    out = []
    for ln in open(log):
        s = ln.rstrip("\n")
        if not KEEP.search(s.strip()) and not KEEP.search(s):
            continue
        s = re.sub(r"; mappings \d+ -> \d+ \(cleared above \d+\)", "", s)
        s = re.sub(r"[;,] \d+ records, \d+ s$", "", s)
        out.append(s)
    return out


def walks():
    segs = int(os.environ.get("PPG_SEGS", "2"))
    nw = int(os.environ.get("PPG_WORKERS", "12"))
    cs = os.environ.get("PPG_CPUS_SERIAL", "").split(",")
    cp = os.environ.get("PPG_CPUS_PAR", "")
    if len(cs) < 3 or not cp:
        raise SystemExit("walks: set PPG_CPUS_SERIAL (three cores) and PPG_CPUS_PAR (the workers' cores)")
    C = json.load(open(CK))
    s0 = int(C["segments"])
    py = sys.executable
    t0 = time.time()
    print("== [F3.TWIN] phase workers, walks: %d segments past the checkpoint (%d) ==" % (segs, s0), flush=True)
    runs = {
        "L_ladder": (dict(ENV_B), cs[0]),
        "L_skip": (dict(ENV_B, TWOP_SKIP_LADDER="1"), cs[1]),
        "P_serial": (dict(ENV_B, TWOP_SKIP_LADDER="1"), cs[2]),
        "P_workers": (dict(ENV_B, TWOP_SKIP_LADDER="1", TWOP_PHASE_WORKERS=str(nw)), cp),
    }
    for k in ("L_ladder", "L_skip"):              # the mean-state arm: the phases off
        runs[k][0].pop("TWOP_MU")
        runs[k][0].pop("TWOP_MU_CLASS")
    procs = {}
    for name, (env_, cpus) in runs.items():
        art = os.path.join(GD, "walk_" + name)
        os.makedirs(art, exist_ok=True)
        for f in os.listdir(art):
            os.remove(os.path.join(art, f))
        json.dump(C, open(os.path.join(art, "walk_FN_checkpoint.json"), "w"), indent=1)
        env = dict(os.environ)
        for k in list(env):
            if k.startswith(("TWOP_", "PSPL_", "A1_")):
                env.pop(k)
        env.update(env_, TWOP_ART=art, TWOP_RESUME="1", TWOP_SEGS=str(s0 + segs),
                   PSPL_WLOG=os.path.join(art, "accepted_bases.jsonl"), MALLOC_ARENA_MAX="2")
        log = os.path.join(art, "walk.log")
        procs[name] = (subprocess.Popen(["nice", "-n", "19", "taskset", "-c", cpus, py, "validation/a1_twowall.py"],
                                        cwd=REPO, env=env, stdout=open(log, "w"), stderr=subprocess.STDOUT), log, time.time())
    left = dict(procs)
    while left:                                   # each walk's own end time, in the order they end
        for name in list(left):
            pr, log, ts = left[name]
            if pr.poll() is not None:
                print("   %-9s exit %d, %.0f s  (%s)" % (name, pr.returncode, time.time() - ts, log), flush=True)
                left.pop(name)
        time.sleep(2)
    L = {n: walk_lines(procs[n][1]) for n in procs}

    def rec(n):
        import glob
        f = sorted(glob.glob(os.path.join(GD, "walk_" + n, "walk_FB_*.json")))
        if not f:
            return None
        r_ = json.load(open(f[-1]))
        r_.pop("seconds", None)                   # the walk's wall time: the one field meant to differ
        return r_

    for a, b, what in (("L_ladder", "L_skip", "L the mean-state walk with and without the start ladder"),
                       ("P_serial", "P_workers", "P the 12-phase walk serial and with %d workers" % nw)):
        la, lb = L[a], L[b]
        nseg = sum(1 for s in la if "[seg" in s)
        ra, rb = rec(a), rec(b)
        dr = same(ra, rb) if (ra is not None and rb is not None) else ["record missing"]
        ok = la == lb and nseg > 0 and any("return:" in s for s in la) and not dr
        check("%s: %d path lines (%d segment lines), identical %s; the record json %s" %
              (what, len(la), nseg, la == lb, "identical" if not dr else "DIFFERS: " + ", ".join(dr[:4])), ok)
        if la != lb:
            for i, (x, y) in enumerate(zip(la, lb)):
                if x != y:
                    print("     first difference at line %d:\n       %s\n       %s" % (i, x, y), flush=True)
                    break
    print("\n== %d/%d PASS  (%.0f s) ==" % (NPASS[0], NPASS[1], time.time() - t0), flush=True)
    print("VERDICT: %s" % ("PASS" if NPASS[0] == NPASS[1] else "FAIL"), flush=True)
    return 0 if NPASS[0] == NPASS[1] else 1


if __name__ == "__main__":
    sys.path.insert(0, HERE)
    sys.exit({"unit": unit, "walks": walks}[sys.argv[1] if len(sys.argv) > 1 else "unit"]())
