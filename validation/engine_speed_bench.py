#!/usr/bin/env python3
"""[X-SPDB] S25 ENGINE SPEED BENCH — clean-host re-baseline (M0) +
MEASURE checkpoints (M-A..M-E) + the M1/M2 acceptance gate, per
DISPATCH_Sspeed_to_S25_2026-08-12 and ADVISORY_engine_speed_audit
2026-08-12 (S-SPEED session; every S-SPEED absolute was measured under
declared contention — THIS carrier is the clean-host anchor that
re-baselines them before any acceptance verdict).

INSTANCE: the defnoz twin class of record ([X-DEFTW] CASE — eps = 30,
L = 8, NI = 21, Nw = 60, frozen CH4/O2 quintic-C1 thermo), seeded from
the COMMITTED leg-1 artifact s24_deftw_leg1.json (GENO wall -> 9-dof
class representative, the wall_to_class recipe of record). NO GENO/WSL
dependency: the bench replays committed artifacts only.

MODES (argv[1], default m0):
  m0       clean-host baselines: fresh adaptive RECORD (x{R} reps,
           medians + spread), whole-loop C1 REPLAY (compile+first vs
           steady), val_grad (compile vs steady), Hessian-row cost
           estimate, host pycount DECLARED. Artifact:
           validation/s25_spdb_m0.json. Machinery gates: record
           certified; replay fidelity within the driver's own monitor
           band; finite val/grad.
  m12gate  M1+M2 acceptance gate (POST-edit): A/B short decisive-free
           walk (run_trsqp, few segments, no margin constraint) with
           the memos ON vs OFF (env arbitration flags of record):
           REQUIRES bit-identical (W, J, n_segments, wall) between
           arms, memo counters reconciling (fresh + cached = legacy
           record count on the SAME trajectory), at least one
           exercised cached boundary in the ON arm, and the in-driver
           first-hit fresh-equality probe + perturbed-W miss control
           rows to have fired. Artifact: validation/s25_spdb_m12.json.
  ma..me   MEASURE checkpoints of the dispatch (attribution snapshot
           after the corresponding M-item): the m0 measurement core
           re-run + memo counters, artifact per mode
           (validation/s25_spdb_<mode>.json). STOP-WHEN-MET reads
           md/me against the targets (segment <= 30 s pessimistic-end,
           campaign <= 25 min projected per advisory §5).

R5: every number this bench prints is measured in-process by
time.perf_counter around the exact call of record; NO tuned
constants — reps and the gate walk budget are DECLARED budget knobs
(env-overridable), never tolerances; the pass/fail gates are
bit-identity, the driver's own derived monitor band, and counter
reconciliation. Contention honesty: the live python process count is
printed in every artifact (tasklist read; ratios remain the evidence
if pycount > 1).

ON-DEMAND CARRIER (env: jax): outside CI tiers by declaration; exit 0
iff the executed mode's machinery/acceptance gates pass.
"""
import json
import os
import subprocess
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1        # noqa: E402
import a1_toc_variational_jax as TV    # noqa: E402
import def_twin_falsifier as DT        # noqa: E402

jax.config.update("jax_enable_x64", True)

HERE = os.path.dirname(os.path.abspath(__file__))
REPS_RECORD = int(os.environ.get("A1_SPDB_REC_REPS", "3"))
REPS_FAST = int(os.environ.get("A1_SPDB_FAST_REPS", "5"))
GATE_SEGS = int(os.environ.get("A1_SPDB_GATE_SEGS", "3"))
GATE_ITER = int(os.environ.get("A1_SPDB_GATE_ITER", "4"))


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def pycount():
    """Declared host-contention datum: live python interpreter count
    (plain tasklist read, name-substring match — the interpreter
    image on this host is python3.13.exe, so an IMAGENAME filter on
    python.exe silently returns none; S-SPEED convention, never
    kill -0). Includes THIS process: 1 = clean."""
    try:
        r = subprocess.run(["tasklist"], capture_output=True,
                           text=True, timeout=30)
        return sum(1 for ln in r.stdout.splitlines()
                   if "python" in ln.lower())
    except Exception:
        return -1


def med(xs):
    return float(np.median(np.asarray(xs)))


def setup_instance():
    """Engine + class representative from committed artifacts only."""
    tab, state_fn, solv, cfg = DT.setup_engine()
    leg1 = json.load(open(DT.ART_LEG1))
    wx = np.array(leg1["res"]["r1"]["obs"]["wall_x"])
    wy = np.array(leg1["res"]["r1"]["obs"]["wall_y"])
    W0, thB, rep = DT.wall_to_class(wx, wy, cfg, DT.M_NODES)
    print("  instance: defnoz class M = %d, thB = %.3f deg, "
          "representation %.3e (committed leg-1 wall)"
          % (DT.M_NODES, thB / DT.d2r, rep))
    return tab, state_fn, solv, cfg, np.asarray(W0, float)


def walk_start(tab, state_fn, solv, cfg, W0):
    """Walk start for the gate/measure walks: the RECORDED perturbed
    start Wp of the committed derive artifact (the [X-TOCV] 1.5%
    sine-bump recipe of record — guarantees a non-stationary start
    so the walk crosses segment boundaries); DECLARED fallback to
    the class representative if Wp fails certification at the
    reduced gate net."""
    try:
        Wp = np.array(json.load(open(DT.ART_DERIVE))["Wp"], float)
        old = (TV.M_NODES, TV.KNOT_XI)
        TV.M_NODES, TV.KNOT_XI = len(Wp) - 1, None
        try:
            outp, _ = TV.run_toc_record(Wp, tab, cfg,
                                        state_fn=state_fn,
                                        solvers=solv)
        finally:
            TV.M_NODES, TV.KNOT_XI = old
        if outp["cert_worst"] <= 1.0:
            print("  walk start = recorded Wp (derive artifact, "
                  "cert_worst %.3e)" % outp["cert_worst"])
            return Wp
        print("  walk start: recorded Wp NOT certified at this net "
              "(%.3e) — declared fallback to the class "
              "representative" % outp["cert_worst"])
    except Exception as e:
        print("  walk start: derive artifact unavailable (%s) — "
              "declared fallback to the class representative" % e)
    return W0


def measure_core(tab, state_fn, solv, cfg, W, label):
    """The shared measurement core: record / replay / val_grad /
    Hessian-row costs, medians with declared reps, driver-band
    fidelity gate. Returns (ok, rows dict)."""
    ok = True
    rows = dict(label=label, pycount=pycount(),
                reps=dict(record=REPS_RECORD, fast=REPS_FAST))
    print("  pycount (declared contention datum): %d" % rows["pycount"])
    old = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    try:
        # (a) fresh adaptive record
        t_rec = []
        for r in range(REPS_RECORD):
            t0 = time.perf_counter()
            out, plan = TV.run_toc_record(W, tab, cfg,
                                          state_fn=state_fn,
                                          solvers=solv)
            t_rec.append(time.perf_counter() - t0)
        rows["record_s"] = dict(median=med(t_rec),
                                all=[round(t, 3) for t in t_rec])
        print("  RECORD (fresh adaptive march): median %.2f s %s"
              % (med(t_rec), rows["record_s"]["all"]))
        ok &= check("record certified (cert_worst %.3e <= 1)"
                    % out["cert_worst"], out["cert_worst"] <= 1.0)
        # (b) whole-loop C1 replay: compile+first vs steady
        t0 = time.perf_counter()
        runj = TV.make_run_toc_scan_jit(tab, cfg, plan,
                                        state_fn=state_fn, solvers=solv)
        wall_sc = runj(jnp.asarray(W))
        wall_sc.block_until_ready()
        t_first = time.perf_counter() - t0
        t_rep = []
        for r in range(REPS_FAST):
            t0 = time.perf_counter()
            w2 = runj(jnp.asarray(W))
            w2.block_until_ready()
            t_rep.append(time.perf_counter() - t0)
        rows["replay_s"] = dict(compile_first=t_first, steady=med(t_rep))
        print("  REPLAY (C1 whole-loop jit): compile+first %.2f s, "
              "steady median %.3f s" % (t_first, med(t_rep)))
        dev = float(jnp.max(jnp.abs(wall_sc - out["wall"])))
        scale = float(jnp.max(jnp.abs(out["wall"])))
        band = A1.NEWTON_TOL_FACTOR * DT.EPS * scale * 10.0
        ok &= check("replay fidelity at base (dev %.3e <= driver band "
                    "%.3e)" % (dev, band), dev <= band)
        # (c) val_grad: compile vs steady
        def scalar_J(Wv):
            return -TV.thrust_J(runj(Wv), tab, state_fn=state_fn)
        val_grad = jax.jit(jax.value_and_grad(scalar_J))
        t0 = time.perf_counter()
        v, g = val_grad(jnp.asarray(W))
        v.block_until_ready()
        t_vg_first = time.perf_counter() - t0
        t_vg = []
        for r in range(REPS_FAST):
            t0 = time.perf_counter()
            v2, g2 = val_grad(jnp.asarray(W))
            v2.block_until_ready()
            t_vg.append(time.perf_counter() - t0)
        rows["val_grad_s"] = dict(compile_first=t_vg_first,
                                  steady=med(t_vg))
        print("  VAL_GRAD: compile+first %.2f s, steady median %.3f s"
              % (t_vg_first, med(t_vg)))
        ok &= check("val/grad finite", bool(np.isfinite(float(v))
                    and np.all(np.isfinite(np.asarray(g)))))
        # (d) Hessian-block estimate: n+1 rows at the steady eval cost
        n = len(W)
        rows["hessian_block_s"] = dict(
            per_row=med(t_vg), rows=n + 1,
            block_estimate=(n + 1) * med(t_vg))
        print("  HESSIAN BLOCK (n+1 = %d rows x steady val_grad): "
              "estimate %.1f s" % (n + 1, (n + 1) * med(t_vg)))
        # segment-class synthesis (advisory §5 row shapes)
        rows["segment_synthesis_s"] = dict(
            base_record=med(t_rec), callback_record=med(t_rec),
            hessian=(n + 1) * med(t_vg),
            walk_evals=3.4 * med(t_vg), replay_monitor=med(t_rep))
        seg = (2 * med(t_rec) + (n + 1) * med(t_vg)
               + 3.4 * med(t_vg) + med(t_rep))
        rows["segment_synthesis_s"]["total_pre_memo"] = seg
        print("  SEGMENT SYNTHESIS (pre-memo shape, advisory rows): "
              "%.1f s" % seg)
        # post-M1 shape (S25-bis M-D/M-E STOP CHECK reads THIS):
        # base record -> 0 (M1 memo), one callback record remains;
        # pessimistic end = the same synthesis at the WORST measured
        # rep of every term (the measured band IS the margin — no
        # magic margin constant).
        seg_post = (med(t_rec) + (n + 1) * med(t_vg)
                    + 3.4 * med(t_vg) + med(t_rep))
        seg_pess = (max(t_rec) + (n + 1) * max(t_vg)
                    + 3.4 * max(t_vg) + max(t_rep))
        rows["segment_synthesis_s"]["total_post_m1"] = seg_post
        rows["segment_synthesis_s"]["total_post_m1_pessimistic"] = \
            seg_pess
        print("  SEGMENT SYNTHESIS (post-M1 shape): central %.1f s, "
              "pessimistic-end %.1f s (worst reps)"
              % (seg_post, seg_pess))
    finally:
        TV.M_NODES, TV.KNOT_XI = old
    return ok, rows


def mode_m0():
    print("== [X-SPDB] M0 clean-host re-baseline (defnoz class) ==")
    # BASELINE PIN (declared): the M0 anchor is the PRE-M4 state —
    # legacy constants-baked engine (A1_PLAN_ARGS=0) AND (S25-bis)
    # the pre-M5c per-cell recorder (A1_COLEXEC=0); the args engine
    # is adopted only through m4gate, the column executor only
    # through m5cgate.
    os.environ["A1_PLAN_ARGS"] = "0"
    os.environ["A1_COLEXEC"] = "0"
    try:
        tab, state_fn, solv, cfg, W = setup_instance()
        ok, rows = measure_core(tab, state_fn, solv, cfg, W, "m0")
        art = os.path.join(HERE, "s25_spdb_m0.json")
        json.dump(rows, open(art, "w"), indent=1)
        print("  artifact -> %s" % art)
    finally:
        os.environ.pop("A1_PLAN_ARGS", None)
        os.environ.pop("A1_COLEXEC", None)
    return ok


def mode_measure(mode):
    print("== [X-SPDB] MEASURE %s (attribution snapshot) ==" % mode)
    tab, state_fn, solv, cfg, W = setup_instance()
    ok, rows = measure_core(tab, state_fn, solv, cfg, W, mode)
    art = os.path.join(HERE, "s25_spdb_%s.json" % mode)
    json.dump(rows, open(art, "w"), indent=1)
    print("  artifact -> %s" % art)
    return ok


def _short_walk(tab, state_fn, solv, cfg, W0, yL, gtol):
    """One short arbitration walk (the m12gate arm): few segments, no
    margin constraint, shared derived gtol (computed once so both
    arms solve the IDENTICAL problem)."""
    t0 = time.perf_counter()
    opt = TV.run_trsqp(W0, tab, cfg, yL, gtol=gtol, xtol=1e-10,
                       max_segments=GATE_SEGS,
                       maxiter_per_seg=GATE_ITER,
                       state_fn=state_fn, solvers=solv, verbose=0)
    opt["walltime_s"] = time.perf_counter() - t0
    return opt


def mode_m12gate():
    print("== [X-SPDB] M1+M2 acceptance gate (A/B memo OFF vs ON, "
          "%d segments x %d iters) ==" % (GATE_SEGS, GATE_ITER))
    # DECLARED gate resolution (class/mesh knobs of the instance, not
    # tolerances — the memo-transparency property under test is
    # resolution-independent; the reduced march keeps the A/B pair
    # affordable). Same defnoz geometry, coarser march net.
    DT.CASE["NI"] = int(os.environ.get("A1_SPDB_GATE_NI", "11"))
    DT.CASE["Nw"] = int(os.environ.get("A1_SPDB_GATE_NW", "30"))
    DT.CASE["da_deg"] = float(os.environ.get("A1_SPDB_GATE_DA", "1.0"))
    print("  gate march net (declared): NI=%d Nw=%d da=%.2f deg"
          % (DT.CASE["NI"], DT.CASE["Nw"], DT.CASE["da_deg"]))
    tab, state_fn, solv, cfg, W0i = setup_instance()
    yL = DT.CASE["yt"] * np.sqrt(DT.CASE["eps"])
    from adaptive_knot_optimize import grad_and_J as AK_gJ, \
        o31_spot as AK_o31
    # ATTRIBUTION PIN (declared): both arms run the LEGACY
    # constants-baked engine (A1_PLAN_ARGS=0) AND the per-cell
    # recorder (A1_COLEXEC=0, S25-bis) so this gate isolates M1+M2
    # exactly as at its committed acceptance. The pins are set
    # BEFORE walk_start (S25-bis re-chain catch of record): the
    # start-selection record must use the SAME recorder as the gate
    # arms — at the cert-MARGINAL Wp the two recorders land on
    # opposite sides of the certification bound (per-cell 3.757 vs
    # per-column 0.585, mild net), so a default-recorder start
    # selection admits a start the gate's own recorder refuses.
    os.environ["A1_PLAN_ARGS"] = "0"
    os.environ["A1_COLEXEC"] = "0"
    W = walk_start(tab, state_fn, solv, cfg, W0i)
    old = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    ok = True
    try:
        # shared derived gtol (one record for the plan, O3.1 band)
        out0, plan0 = TV.run_toc_record(W, tab, cfg,
                                        state_fn=state_fn, solvers=solv)
        if not check("gate start certified (worst %.3e)"
                     % out0["cert_worst"], out0["cert_worst"] <= 1.0):
            return False
        J_w, g_w, scalJ_w = AK_gJ(W, None, tab, cfg, plan0,
                                  state_fn, solv)
        dp_o31, tol_dp = AK_o31(W, None, scalJ_w, g_w, J_w)
        gtol = max(tol_dp, 1e-8 * float(np.linalg.norm(g_w)))
        print("  shared derived gtol = %.3e (O3.1 %.3e <= %.3e)"
              % (gtol, dp_o31, tol_dp))
        os.environ["A1_RECORD_MEMO"] = "0"
        os.environ["A1_VG_MEMO"] = "0"
        print("-- arm A: memos OFF (legacy arbitration path) --")
        a = _short_walk(tab, state_fn, solv, cfg, W, yL, gtol)
        os.environ["A1_RECORD_MEMO"] = "1"
        os.environ["A1_VG_MEMO"] = "1"
        print("-- arm B: memos ON --")
        b = _short_walk(tab, state_fn, solv, cfg, W, yL, gtol)
    finally:
        TV.M_NODES, TV.KNOT_XI = old
        os.environ.pop("A1_RECORD_MEMO", None)
        os.environ.pop("A1_VG_MEMO", None)
        os.environ.pop("A1_PLAN_ARGS", None)
        os.environ.pop("A1_COLEXEC", None)
    ok &= check("bit-identical final W",
                bool(np.array_equal(a["W"], b["W"])))
    ok &= check("bit-identical J (%.10e vs %.10e)"
                % (-a["res"].fun, -b["res"].fun),
                float(a["res"].fun) == float(b["res"].fun))
    ok &= check("same n_segments (%d vs %d)"
                % (a["n_segments"], b["n_segments"]),
                a["n_segments"] == b["n_segments"])
    ra = (a["record_fresh"], a.get("record_cached", 0),
          a.get("record_failmemo", 0))
    rb = (b["record_fresh"], b.get("record_cached", 0),
          b.get("record_failmemo", 0))
    print("  records fresh/cached/failmemo: OFF %s -> ON %s" % (ra, rb))
    ok &= check("OFF arm ran memo-free (cached 0, failmemo 0)",
                ra[1] == 0 and ra[2] == 0)
    ok &= check("trajectory record events reconcile (ON fresh + "
                "cached + failmemo == OFF fresh)",
                sum(rb) == ra[0])
    ok &= check("ON arm exercised at least one cached boundary",
                rb[1] >= 1)
    print("  n_eval (honest compiled executions): OFF %d -> ON %d; "
          "dedup hits ON %d" % (a["n_eval"], b["n_eval"],
                                b.get("n_eval_dedup_hits", 0)))
    ok &= check("ON arm deduplicated compiled evals (n_eval ON < OFF)",
                b["n_eval"] < a["n_eval"])
    ok &= check("memo probe rows fired in ON arm (fresh-equality + "
                "perturbed-miss)", b.get("memo_probe_pass", 0) >= 1
                and b.get("memo_probe_miss", 0) >= 1)
    print("  walltime: OFF %.1f s -> ON %.1f s"
          % (a["walltime_s"], b["walltime_s"]))
    art = os.path.join(HERE, "s25_spdb_m12.json")
    json.dump(dict(off=dict(walltime_s=a["walltime_s"], n_eval=a["n_eval"],
                            records=ra, n_segments=a["n_segments"]),
                   on=dict(walltime_s=b["walltime_s"], n_eval=b["n_eval"],
                           records=rb, n_segments=b["n_segments"],
                           dedup_hits=b.get("n_eval_dedup_hits", 0)),
                   pycount=pycount()),
              open(art, "w"), indent=1)
    print("  artifact -> %s" % art)
    return ok


def mode_m4gate():
    """M4 acceptance (advisory §4-M4; the gate CAN fire and reject):
    args-engine vs legacy constants-engine on the SAME plan —
    Newton-floor equivalence (+ bitwise report), replay fidelity vs
    the record, O3.1 leak detector THROUGH the args engine,
    warm-path args-vs-constants band (derived from the measured rep
    spread, K_RICH-scaled), engine-cache re-bind warmth, and the V2
    property rejector (different topology -> different signature)."""
    print("== [X-SPDB] M4 acceptance gate (plan-as-args vs legacy "
          "constants) ==")
    import copy as _c
    from adaptive_knot_optimize import grad_and_J as AK_gJ, \
        o31_spot as AK_o31
    tab, state_fn, solv, cfg, W = setup_instance()
    ok = True
    old = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    try:
        out, plan = TV.run_toc_record(W, tab, cfg, state_fn=state_fn,
                                      solvers=solv)
        ok &= check("record certified (worst %.3e)"
                    % out["cert_worst"], out["cert_worst"] <= 1.0)
        os.environ["A1_PLAN_ARGS"] = "0"
        runL = TV.make_run_toc_scan_jit(tab, cfg, plan,
                                        state_fn=state_fn, solvers=solv)
        os.environ.pop("A1_PLAN_ARGS", None)
        runA = TV.make_run_toc_scan_jit(tab, cfg, plan,
                                        state_fn=state_fn, solvers=solv)
        Wj = jnp.asarray(W)
        wl = runL(Wj)
        wl.block_until_ready()
        wa = runA(Wj)
        wa.block_until_ready()
        dev = float(jnp.max(jnp.abs(wa - wl)))
        scale = float(jnp.max(jnp.abs(wl)))
        band = A1.NEWTON_TOL_FACTOR * DT.EPS * scale * 10.0
        print("  args-vs-constants wall: max|d| = %.3e (scale %.3e); "
              "bitwise = %s" % (dev, scale, bool(jnp.all(wa == wl))))
        ok &= check("Newton-floor equivalence (dev <= driver band "
                    "%.3e)" % band, dev <= band)
        devr = float(jnp.max(jnp.abs(wa - out["wall"])))
        ok &= check("args replay fidelity vs record (%.3e <= %.3e)"
                    % (devr, band), devr <= band)
        J_w, g_w, scalJ = AK_gJ(W, None, tab, cfg, plan, state_fn,
                                solv)
        dp, tol = AK_o31(W, None, scalJ, g_w, J_w)
        ok &= check("O3.1 leak detector through the args engine "
                    "(%.3e <= %.3e)" % (dp, tol), dp <= tol)
        tL, tA = [], []
        for r in range(REPS_FAST):
            t0 = time.perf_counter()
            runL(Wj).block_until_ready()
            tL.append(time.perf_counter() - t0)
            t0 = time.perf_counter()
            runA(Wj).block_until_ready()
            tA.append(time.perf_counter() - t0)
        mL, mA = med(tL), med(tA)
        spread = max((max(tL) - min(tL)) / max(mL, 1e-12),
                     (max(tA) - min(tA)) / max(mA, 1e-12))
        kband = A1.K_RICH * spread
        ok &= check("warm-path args-vs-constants band (args %.4f s <= "
                    "legacy %.4f s x (1 + %.3f), K_RICH x measured "
                    "spread)" % (mA, mL, kband),
                    mA <= mL * (1.0 + kband))
        t0 = time.perf_counter()
        run2 = TV.make_run_toc_scan_jit(tab, cfg, plan,
                                        state_fn=state_fn, solvers=solv)
        t_bind = time.perf_counter() - t0
        t0 = time.perf_counter()
        run2(Wj).block_until_ready()
        t2 = time.perf_counter() - t0
        # the re-bound engine's FIRST call must be a WARM call
        # (engine-cache hit => no retrace): bound = the same
        # measured-spread band as the warm path (derived, no
        # judgment constant); the bind cost itself (plan_operands +
        # dummy verification) is reported as its own row.
        print("  re-bind cost (plan_operands + dummy verification): "
              "%.4f s" % t_bind)
        ok &= check("engine-cache re-bind first call WARM (%.4f s <= "
                    "steady %.4f s x (1 + %.3f) — no per-segment "
                    "recompile)" % (t2, mA, kband),
                    t2 <= mA * (1.0 + kband))
        plan_p = _c.deepcopy(plan)
        plan_p["arc"] = plan_p["arc"] + [_c.deepcopy(plan_p["arc"][-1])]
        _, sig1 = TV.plan_operands(plan, cfg["NI"], cfg["Nw"])
        _, sig2 = TV.plan_operands(plan_p, cfg["NI"], cfg["Nw"])
        ok &= check("V2 property rejector: different topology -> "
                    "different signature (%s != %s)" % (sig1, sig2),
                    sig1 != sig2)
        # class-key rejector (refuter repair M4-F1): a SAME-LENGTH
        # knot-vector change keeps every shape identical — the
        # engine cache must still produce a NEW entry (a silent
        # stale-class reuse is the refuted failure mode)
        n_eng0 = len(TV._SCAN_ENGINES)
        xi_alt = np.linspace(0.0, 1.0, TV.M_NODES + 1)[1:] ** 1.5
        old_cls = (TV.M_NODES, TV.KNOT_XI)
        try:
            TV.KNOT_XI = xi_alt
            TV.make_run_toc_scan_jit(tab, cfg, plan,
                                     state_fn=state_fn, solvers=solv)
        finally:
            TV.M_NODES, TV.KNOT_XI = old_cls
        ok &= check("class-key rejector: same-length knot change -> "
                    "NEW engine entry (%d -> %d)"
                    % (n_eng0, len(TV._SCAN_ENGINES)),
                    len(TV._SCAN_ENGINES) == n_eng0 + 1)
        art = os.path.join(HERE, "s25_spdb_m4.json")
        json.dump(dict(dev_args_vs_const=dev, band=band,
                       steady_legacy_s=mL, steady_args_s=mA,
                       kband=kband, rebind_s=t2,
                       pycount=pycount()), open(art, "w"), indent=1)
        print("  artifact -> %s" % art)
    finally:
        TV.M_NODES, TV.KNOT_XI = old
        os.environ.pop("A1_PLAN_ARGS", None)
    return ok


def mode_mbwalk():
    """MEASURE M-B walk half: the SAME short walk as m12gate arm B
    (memos ON) but on the M4 args-engine (default flags) — reports
    walltime (compare vs the m12gate ON arm = M4's walk-level
    attribution), the engine-signature CHURN count along the walk
    (the Q3 datum: signatures/segments), and the memo counters."""
    print("== [X-SPDB] M-B walk (args engine ON, %d segments x %d "
          "iters) ==" % (GATE_SEGS, GATE_ITER))
    DT.CASE["NI"] = int(os.environ.get("A1_SPDB_GATE_NI", "11"))
    DT.CASE["Nw"] = int(os.environ.get("A1_SPDB_GATE_NW", "30"))
    DT.CASE["da_deg"] = float(os.environ.get("A1_SPDB_GATE_DA", "1.0"))
    print("  gate march net (declared): NI=%d Nw=%d da=%.2f deg"
          % (DT.CASE["NI"], DT.CASE["Nw"], DT.CASE["da_deg"]))
    tab, state_fn, solv, cfg, W0i = setup_instance()
    yL = DT.CASE["yt"] * np.sqrt(DT.CASE["eps"])
    from adaptive_knot_optimize import grad_and_J as AK_gJ, \
        o31_spot as AK_o31
    W = walk_start(tab, state_fn, solv, cfg, W0i)
    old = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    ok = True
    try:
        out0, plan0 = TV.run_toc_record(W, tab, cfg,
                                        state_fn=state_fn, solvers=solv)
        if not check("start certified (worst %.3e)"
                     % out0["cert_worst"], out0["cert_worst"] <= 1.0):
            return False
        J_w, g_w, scalJ_w = AK_gJ(W, None, tab, cfg, plan0,
                                  state_fn, solv)
        dp_o31, tol_dp = AK_o31(W, None, scalJ_w, g_w, J_w)
        gtol = max(tol_dp, 1e-8 * float(np.linalg.norm(g_w)))
        b = _short_walk(tab, state_fn, solv, cfg, W, yL, gtol)
        sigs = sum(len(s) for s in TV._SCAN_SIGSEEN.values())
        segs = b["n_segments"]
        print("  walk: %d segments in %.1f s; engine signatures seen "
              "in-process = %d (Q3 churn datum: %.2f sig/segment); "
              "records fresh/cached/failmemo = %d/%d/%d; n_eval %d "
              "(dedup hits %d)"
              % (segs, b["walltime_s"], sigs, sigs / max(segs, 1),
                 b["record_fresh"], b["record_cached"],
                 b["record_failmemo"], b["n_eval"],
                 b.get("n_eval_dedup_hits", 0)))
        art = os.path.join(HERE, "s25_spdb_mbwalk.json")
        json.dump(dict(walltime_s=b["walltime_s"], n_segments=segs,
                       signatures=sigs, n_eval=b["n_eval"],
                       records=(b["record_fresh"], b["record_cached"],
                                b["record_failmemo"]),
                       pycount=pycount()), open(art, "w"), indent=1)
        print("  artifact -> %s" % art)
    finally:
        TV.M_NODES, TV.KNOT_XI = old
    return ok


def mode_m5gate():
    """M5a+M5b acceptance: (a) fused-vs-legacy record A/B on the SAME
    design (wall bitwise + cert_worst equality + timing rows — the
    fused entry calls the IDENTICAL jitted newton and the verbatim
    step expressions); (b) M5b doctored-cell control: a doctored
    solve_cert at host-call K must produce the TYPED refusal AT K
    (first-offender index stable) with abort armed. ATTRIBUTION PIN
    (S25-bis): the whole mode runs the per-cell recorder
    (A1_COLEXEC=0) — the M5a/M5b properties under test are
    host-dispatch properties; the column executor has its own
    m5cgate with its own doctored control."""
    print("== [X-SPDB] M5a+M5b acceptance gate ==")
    tab, state_fn, solv, cfg, W = setup_instance()
    old = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    ok = True
    os.environ["A1_COLEXEC"] = "0"
    try:
        os.environ["A1_FUSED_CERT"] = "0"
        t0 = time.perf_counter()
        outL, planL = TV.run_toc_record(W, tab, cfg,
                                        state_fn=state_fn,
                                        solvers=solv)
        tL = time.perf_counter() - t0
        os.environ.pop("A1_FUSED_CERT", None)
        t0 = time.perf_counter()
        outF, planF = TV.run_toc_record(W, tab, cfg,
                                        state_fn=state_fn,
                                        solvers=solv)
        tF = time.perf_counter() - t0
        ok &= check("M5a wall BITWISE fused vs legacy",
                    bool(np.array_equal(np.asarray(outF["wall"]),
                                        np.asarray(outL["wall"]))))
        ok &= check("M5a cert_worst identical (%.6e vs %.6e)"
                    % (outF["cert_worst"], outL["cert_worst"]),
                    float(outF["cert_worst"])
                    == float(outL["cert_worst"]))
        ok &= check("M5a plan identical (dec vectors)",
                    [(c["N"], c["Nv"]) for c in planF["arc"]]
                    == [(c["N"], c["Nv"]) for c in planL["arc"]])
        print("  record walltime: legacy 2-dispatch %.2f s -> fused "
              "%.2f s (%.2fx)" % (tL, tF, tL / max(tF, 1e-9)))
        # (b) M5b doctored-cell first-offender control (constraint 5)
        K_DOCT = 7
        count = dict(n=0)
        base_int = solv["interior"]

        def doct_solve_cert(z0, p, ta):
            z, step = base_int[3](z0, p, ta)
            k = count["n"]
            count["n"] += 1
            if k == K_DOCT:
                return z, step + 1.0e9   # doctored: huge metric
            return z, step

        solv_d = dict(solv)
        solv_d["interior"] = (base_int[0], base_int[1], base_int[2],
                              doct_solve_cert)
        fired = None
        try:
            TV.run_toc_record(W, tab, cfg, state_fn=state_fn,
                              solvers=solv_d, abort_uncert=True)
        except A1.UncertifiedCellError as e:
            fired = e
        ok &= check("M5b doctored cell K=%d -> TYPED refusal fired"
                    % K_DOCT, fired is not None)
        if fired is not None:
            print("  refusal: aborted_at_cell = %s (cert index over "
                  "ALL kinds), cert_worst = %.3e; interior solve "
                  "calls made = %d" % (fired.aborted_at_cell,
                                       fired.cert_worst, count["n"]))
            # first-offender stability: the march stopped AT the
            # doctored interior call — exactly K_DOCT+1 interior
            # dispatches happened, none after; and the carried
            # cert_worst is the doctored (huge) ratio.
            ok &= check("M5b abort stopped AT the doctored call "
                        "(interior calls == K+1)",
                        count["n"] == K_DOCT + 1)
            ok &= check("M5b cert_worst carries the doctored ratio "
                        "(> 1e6)", fired.cert_worst > 1e6)
        art = os.path.join(HERE, "s25_spdb_m5.json")
        json.dump(dict(record_legacy_s=tL, record_fused_s=tF,
                       cert_worst=float(outF["cert_worst"]),
                       pycount=pycount()), open(art, "w"), indent=1)
        print("  artifact -> %s" % art)
    finally:
        TV.M_NODES, TV.KNOT_XI = old
        os.environ.pop("A1_FUSED_CERT", None)
        os.environ.pop("A1_COLEXEC", None)
    return ok


def mode_m5cgate():
    """M5c acceptance gate (advisory M5c F6-AMENDED; this gate CAN
    fire and REJECT the lever -> fallback H2 -> N1, never unbounded
    debugging): legacy per-cell recorder (A1_COLEXEC=0) vs the
    hoisted per-column compiled executor on the SAME W at TWO nets
    (defnoz-mild = the declared m12gate net, then FULL defnoz):
      (1) dec-vector BITWISE identity — n_B, per-fan-column n,
          per-design-column (N, Nv, n, has_axis), cert_n (covers
          every wall_search, truncation and axis decision on real
          columns, truncated ones included);
      (2) z inside the driver's Newton-floor band — wall stack,
          per-column seeds, min_margin (same derived band
          construction as m4gate: NEWTON_TOL_FACTOR x EPS x scale x
          10) + certification VERDICT equality (cert_worst <= 1
          agrees; the ratio itself is a floor-noise quantity,
          reported not gated);
      (3) doctored-cell control THROUGH the executor stacks: a
          doctored step row at an exact (column ctx, row) must raise
          the TYPED refusal with aborted_at_cell == the cert index
          at the chain boundary + row (first-offender localization
          through the compiled path);
      (4) near-seam margin-floor pair: floor dialed just above /
          below the recorded min_margin (delta derived from the
          band) — the SAME flip (raise vs complete) in BOTH
          recorders, and the raise names the SAME offending cell.
    ANY plan/dec difference = lever REJECTED (exit 1)."""
    import re as _re
    print("== [X-SPDB] M5c acceptance gate (per-column executor vs "
          "per-cell recorder) ==")
    full = dict(DT.CASE)          # the CASE net OF RECORD, pristine
    DT.CASE["NI"] = int(os.environ.get("A1_SPDB_GATE_NI", "11"))
    DT.CASE["Nw"] = int(os.environ.get("A1_SPDB_GATE_NW", "30"))
    DT.CASE["da_deg"] = float(os.environ.get("A1_SPDB_GATE_DA", "1.0"))
    nets = [("defnoz-mild", dict(DT.CASE)), ("defnoz-full", full)]
    ok = True
    rows = dict(pycount=pycount(), nets={})

    def dec_vec(out, plan):
        return (int(plan["n_B"]),
                tuple(int(c["n"]) for c in plan["fan"]),
                tuple((int(c["N"]), int(c["Nv"]), int(c["n"]),
                       bool(c["has_axis"])) for c in plan["arc"]),
                int(out["cert_n"]))

    def zdev(planA, planB):
        d, s = 0.0, 0.0
        for key in ("fan", "arc"):
            for ca, cb in zip(planA[key], planB[key]):
                if ca["n"]:
                    d = max(d, float(np.max(np.abs(
                        np.asarray(ca["seeds"])
                        - np.asarray(cb["seeds"])))))
                    s = max(s, float(np.max(np.abs(
                        np.asarray(ca["seeds"])))))
        return d, s

    tab = state_fn = solv = cfg = W = None
    for name, case in nets:
        print("-- net %s: NI=%d Nw=%d da=%.2f --"
              % (name, case["NI"], case["Nw"], case["da_deg"]))
        DT.CASE.update(case)
        tab, state_fn, solv, cfg, W = setup_instance()
        old = (TV.M_NODES, TV.KNOT_XI)
        TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
        try:
            os.environ["A1_COLEXEC"] = "0"
            t0 = time.perf_counter()
            outL, planL = TV.run_toc_record(W, tab, cfg,
                                            state_fn=state_fn,
                                            solvers=solv)
            tL = time.perf_counter() - t0
            os.environ.pop("A1_COLEXEC", None)
            t0 = time.perf_counter()
            outC, planC = TV.run_toc_record(W, tab, cfg,
                                            state_fn=state_fn,
                                            solvers=solv)
            tC1 = time.perf_counter() - t0        # incl. compiles
            t0 = time.perf_counter()
            outC, planC = TV.run_toc_record(W, tab, cfg,
                                            state_fn=state_fn,
                                            solvers=solv)
            tC = time.perf_counter() - t0         # warm executor
            ok &= check("%s dec-vector BITWISE identity" % name,
                        dec_vec(outL, planL) == dec_vec(outC, planC))
            wL = np.asarray(outL["wall"])
            wC = np.asarray(outC["wall"])
            scale = float(np.max(np.abs(wL)))
            band = A1.NEWTON_TOL_FACTOR * DT.EPS * scale * 10.0
            dw = float(np.max(np.abs(wC - wL)))
            ok &= check("%s wall inside Newton-floor band (%.3e <= "
                        "%.3e; bitwise = %s)"
                        % (name, dw, band, bool(np.array_equal(wC, wL))),
                        dw <= band)
            ds, ss = zdev(planL, planC)
            bs = A1.NEWTON_TOL_FACTOR * DT.EPS * max(ss, 1.0) * 10.0
            ok &= check("%s seeds inside Newton-floor band (%.3e <= "
                        "%.3e)" % (name, ds, bs), ds <= bs)
            dm = abs(float(outL["min_margin"])
                     - float(outC["min_margin"]))
            ok &= check("%s min_margin inside band (%.3e <= %.3e)"
                        % (name, dm, band), dm <= band)
            ok &= check("%s certification VERDICT agrees (L %.3e, C "
                        "%.3e)" % (name, outL["cert_worst"],
                                   outC["cert_worst"]),
                        (outL["cert_worst"] <= 1.0)
                        == (outC["cert_worst"] <= 1.0))
            cx = outC["colexec"]
            print("  record walltime: per-cell %.2f s -> colexec "
                  "%.2f s warm (%.2fx; first incl. compile %.2f s); "
                  "chains %d, cells %d, padded frac %.2f"
                  % (tL, tC, tL / max(tC, 1e-9), tC1, cx["calls"],
                     cx["cells"],
                     cx["padded"] / max(cx["cells"] + cx["padded"], 1)))
            rows["nets"][name] = dict(
                t_percell=tL, t_colexec_warm=tC, t_colexec_first=tC1,
                wall_dev=dw, band=band, seed_dev=ds, seed_band=bs,
                colexec=cx)
            if name == "defnoz-mild":
                # (3) doctored-cell first-offender through the stacks
                doc = dict(ctx=("design_col", 5), row=3, dstep=1.0e9)
                TV._COLEXEC_DOCTOR = doc
                fired = None
                try:
                    TV.run_toc_record(W, tab, cfg, state_fn=state_fn,
                                      solvers=solv, abort_uncert=True)
                except A1.UncertifiedCellError as e:
                    fired = e
                finally:
                    TV._COLEXEC_DOCTOR = None
                ok &= check("M5c doctored stack row -> TYPED refusal",
                            fired is not None)
                if fired is not None:
                    exp = doc.get("cert_n_at_chain", -10) + doc["row"]
                    ok &= check("M5c first-offender localization "
                                "(aborted_at_cell %s == chain-start "
                                "%s + row %d)"
                                % (fired.aborted_at_cell,
                                   doc.get("cert_n_at_chain"),
                                   doc["row"]),
                                fired.aborted_at_cell == exp)
                    ok &= check("M5c cert_worst carries doctored "
                                "ratio (> 1e6)", fired.cert_worst > 1e6)
                # (4) near-seam margin-floor pair (derived delta)
                mm = float(outC["min_margin"])
                dlt = max(abs(mm) * 1e-6, 1e3 * band)
                cells = {}
                for arm, flag in (("percell", "0"), ("colexec", "1")):
                    os.environ["A1_COLEXEC"] = flag
                    try:
                        TV.run_toc_record(W, tab, cfg,
                                          state_fn=state_fn,
                                          solvers=solv,
                                          margin_floor=mm + dlt)
                        cells[arm] = "NO-RAISE"
                    except RuntimeError as e:
                        mt = _re.search(r"at cell (\d+)", str(e))
                        cells[arm] = mt.group(1) if mt else "NO-INDEX"
                    finally:
                        os.environ.pop("A1_COLEXEC", None)
                ok &= check("near-seam floor_hi: SAME raise cell in "
                            "both recorders (%s == %s)"
                            % (cells["percell"], cells["colexec"]),
                            cells["percell"] == cells["colexec"]
                            and cells["percell"] not in
                            ("NO-RAISE", "NO-INDEX"))
                done = {}
                for arm, flag in (("percell", "0"), ("colexec", "1")):
                    os.environ["A1_COLEXEC"] = flag
                    try:
                        o2, _ = TV.run_toc_record(W, tab, cfg,
                                                  state_fn=state_fn,
                                                  solvers=solv,
                                                  margin_floor=mm - dlt)
                        done[arm] = float(o2["cert_worst"])
                    except RuntimeError:
                        done[arm] = None
                    finally:
                        os.environ.pop("A1_COLEXEC", None)
                ok &= check("near-seam floor_lo: BOTH recorders "
                            "complete (same flip side)",
                            done["percell"] is not None
                            and done["colexec"] is not None)
                rows["seam"] = dict(min_margin=mm, delta=dlt,
                                    raise_cell=cells, lo_done=done)
        finally:
            TV.M_NODES, TV.KNOT_XI = old
            os.environ.pop("A1_COLEXEC", None)
    art = os.path.join(HERE, "s25_spdb_m5c.json")
    json.dump(rows, open(art, "w"), indent=1)
    print("  artifact -> %s" % art)
    return ok


def mode_m6gate():
    """M6 acceptance gate (S25-bis; user-ordered re-entry over
    STOP-WHEN-MET — real improvement/generalization: batched FD rows
    + the nonfinite-lane guard the sequential block never had):
    (1) per-lane batched == sequential inside the FD-truncation-
        derived band |dg| <= sqrt(EPS) * max(1, |g|_scale) — the
        Hessian consumer's own step choice dH = sqrt(EPS)*scale
        makes smaller deviations semantically invisible to the
        measured quadratic (derived, not judged); bitwise reported;
    (2) corrupted-lane control THROUGH vg_batch_rows: a doctored
        batch NaN-ing lane k must be recovered from the sequential
        compiled path BITWISE and counted (REQ-NONSTALL);
    (3) O3.1 re-pass (version-change gate half; the closing suite
        is the KAT half);
    (4) timing row: sequential vs batched Hessian rows, the <= 8 s
        defnoz target row = MEASURE M-E input."""
    print("== [X-SPDB] M6 acceptance gate (vmapped FD rows vs "
          "sequential) ==")
    from adaptive_knot_optimize import grad_and_J as AK_gJ, \
        o31_spot as AK_o31
    tab, state_fn, solv, cfg, W = setup_instance()
    W = np.asarray(W, float)
    ok = True
    old = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    try:
        out, plan = TV.run_toc_record(W, tab, cfg, state_fn=state_fn,
                                      solvers=solv)
        ok &= check("record certified (worst %.3e)"
                    % out["cert_worst"], out["cert_worst"] <= 1.0)
        runj = TV.make_run_toc_scan_jit(tab, cfg, plan,
                                        state_fn=state_fn,
                                        solvers=solv)

        def scalar_J(Wv):
            return -TV.thrust_J(runj(Wv), tab, state_fn=state_fn)

        val_grad = jax.jit(jax.value_and_grad(scalar_J))
        runvgb = TV.make_run_toc_scan_jit(tab, cfg, plan,
                                          state_fn=state_fn,
                                          solvers=solv, vg_batch=True)
        n = len(W)
        dHs = np.array([DT.EPS ** 0.5 * max(abs(W[j]), 1.0)
                        for j in range(n)])
        P = np.repeat(W[None, :], n, axis=0)
        P[np.arange(n), np.arange(n)] += dHs
        # sequential reference (n rows + base = the n+1 block)
        val_grad(jnp.asarray(W))              # warm
        t0 = time.perf_counter()
        vs_seq, gs_seq = [], []
        for j in range(n):
            v, g = val_grad(jnp.asarray(P[j]))
            vs_seq.append(float(v))
            gs_seq.append(np.asarray(g))
        val_grad(jnp.asarray(W))
        t_seq = time.perf_counter() - t0
        gs_seq = np.stack(gs_seq)
        # batched (warm once; timing on the warm dispatch)
        TV.vg_batch_rows(runvgb, val_grad, P)
        t0 = time.perf_counter()
        vs_b, gs_b = TV.vg_batch_rows(runvgb, val_grad, P)
        val_grad(jnp.asarray(W))
        t_bat = time.perf_counter() - t0
        g_scale = max(1.0, float(np.max(np.abs(gs_seq))))
        band = DT.EPS ** 0.5 * g_scale
        dev = float(np.max(np.abs(gs_b - gs_seq)))
        devv = float(np.max(np.abs(np.asarray(vs_seq) - vs_b)))
        ok &= check("per-lane batched == sequential inside the FD-"
                    "truncation band (grad dev %.3e, val dev %.3e <= "
                    "%.3e; bitwise = %s)"
                    % (dev, devv, band,
                       bool(np.array_equal(gs_b, gs_seq))),
                    dev <= band and devv <= band)
        # corrupted-lane control through the driver's own helper
        K_L = 3

        def doct_vgb(Wm):
            vs, gs = runvgb(Wm)
            vs = np.asarray(vs).copy()
            gs = np.asarray(gs).copy()
            gs[K_L] = np.nan
            return vs, gs

        cnt = dict(hess_lane=0)
        vs_c, gs_c = TV.vg_batch_rows(doct_vgb, val_grad, P, cnt)
        ok &= check("corrupted-lane control: lane %d recovered from "
                    "the sequential path BITWISE + counted (%d)"
                    % (K_L, cnt["hess_lane"]),
                    cnt["hess_lane"] == 1
                    and bool(np.array_equal(gs_c[K_L], gs_seq[K_L])))
        J_w, g_w, scalJ = AK_gJ(W, None, tab, cfg, plan, state_fn,
                                solv)
        dp, tol = AK_o31(W, None, scalJ, g_w, J_w)
        ok &= check("O3.1 re-pass through the args engine (%.3e <= "
                    "%.3e)" % (dp, tol), dp <= tol)
        met = t_bat <= 8.0
        print("  Hessian rows (n=%d + base): sequential %.2f s -> "
              "batched %.2f s (%.2fx); <= 8 s target row: %s "
              "[MEASURE M-E input]"
              % (n, t_seq, t_bat, t_seq / max(t_bat, 1e-9),
                 "MET" if met else "NOT-MET"))
        art = os.path.join(HERE, "s25_spdb_m6.json")
        json.dump(dict(t_seq=t_seq, t_bat=t_bat, dev=dev, band=band,
                       n=n, pycount=pycount()),
                  open(art, "w"), indent=1)
        print("  artifact -> %s" % art)
    finally:
        TV.M_NODES, TV.KNOT_XI = old
    return ok


def mode_h3gate():
    """H3 acceptance gate (S25-bis, campaign rung-boundary dedup):
    the SAME short walk with and without preplan=(out, plan) of the
    start design. REQUIRES: bit-identical (W, J, n_segments) between
    arms (the reuse is bitwise or nothing); the preplan arm consumes
    the caller record as a memo hit (record_preplan == 1, fresh
    exactly one less than the no-preplan arm, cached one more); the
    M1 first-hit controls fire on the preplan consume (the H3
    'bitwise on reuse' gate IS the existing fresh-equality +
    perturbed-miss control pair); field_records=True carries cols in
    last_cert and last_cert.W must equal the returned W bitwise."""
    print("== [X-SPDB] H3 acceptance gate (preplan/rung-boundary "
          "dedup, %d segments x %d iters) ==" % (GATE_SEGS, GATE_ITER))
    DT.CASE["NI"] = int(os.environ.get("A1_SPDB_GATE_NI", "11"))
    DT.CASE["Nw"] = int(os.environ.get("A1_SPDB_GATE_NW", "30"))
    DT.CASE["da_deg"] = float(os.environ.get("A1_SPDB_GATE_DA", "1.0"))
    print("  gate march net (declared): NI=%d Nw=%d da=%.2f deg"
          % (DT.CASE["NI"], DT.CASE["Nw"], DT.CASE["da_deg"]))
    tab, state_fn, solv, cfg, W0i = setup_instance()
    yL = DT.CASE["yt"] * np.sqrt(DT.CASE["eps"])
    from adaptive_knot_optimize import grad_and_J as AK_gJ, \
        o31_spot as AK_o31
    W = walk_start(tab, state_fn, solv, cfg, W0i)
    old = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    ok = True
    try:
        out0, plan0 = TV.run_toc_record(W, tab, cfg,
                                        state_fn=state_fn,
                                        solvers=solv)
        if not check("gate start certified (worst %.3e)"
                     % out0["cert_worst"], out0["cert_worst"] <= 1.0):
            return False
        J_w, g_w, scalJ_w = AK_gJ(W, None, tab, cfg, plan0,
                                  state_fn, solv)
        dp_o31, tol_dp = AK_o31(W, None, scalJ_w, g_w, J_w)
        gtol = max(tol_dp, 1e-8 * float(np.linalg.norm(g_w)))
        print("-- arm A: no preplan --")
        t0 = time.perf_counter()
        a = TV.run_trsqp(W, tab, cfg, yL, gtol=gtol, xtol=1e-10,
                         max_segments=GATE_SEGS,
                         maxiter_per_seg=GATE_ITER,
                         state_fn=state_fn, solvers=solv, verbose=0)
        ta_ = time.perf_counter() - t0
        print("-- arm B: preplan + field_records --")
        t0 = time.perf_counter()
        b = TV.run_trsqp(W, tab, cfg, yL, gtol=gtol, xtol=1e-10,
                         max_segments=GATE_SEGS,
                         maxiter_per_seg=GATE_ITER,
                         state_fn=state_fn, solvers=solv, verbose=0,
                         preplan=(out0, plan0), field_records=True)
        tb_ = time.perf_counter() - t0
    finally:
        TV.M_NODES, TV.KNOT_XI = old
    ok &= check("bit-identical final W",
                bool(np.array_equal(a["W"], b["W"])))
    ok &= check("bit-identical J (%.10e vs %.10e)"
                % (-a["res"].fun, -b["res"].fun),
                float(a["res"].fun) == float(b["res"].fun))
    ok &= check("same n_segments (%d vs %d)"
                % (a["n_segments"], b["n_segments"]),
                a["n_segments"] == b["n_segments"])
    ra = (a["record_fresh"], a["record_cached"], a["record_failmemo"])
    rb = (b["record_fresh"], b["record_cached"], b["record_failmemo"])
    print("  records fresh/cached/failmemo: A %s -> B %s "
          "(preplan A %d, B %d)" % (ra, rb, a["record_preplan"],
                                    b["record_preplan"]))
    ok &= check("preplan arm consumed the caller record "
                "(record_preplan == 1)", b["record_preplan"] == 1)
    ok &= check("one fresh record deleted (fresh B == fresh A - 1)",
                rb[0] == ra[0] - 1)
    ok &= check("consumed as a memo hit (cached B == cached A + 1)",
                rb[1] == ra[1] + 1)
    ok &= check("M1 first-hit controls fired in arm B",
                b.get("memo_probe_pass", 0) >= 1
                and b.get("memo_probe_miss", 0) >= 1)
    lc = b.get("last_cert")
    ok &= check("last_cert returned, bitwise at the returned W, "
                "with cols (field_records)",
                lc is not None
                and bool(np.array_equal(np.asarray(lc["W"]), b["W"]))
                and "cols" in lc["out"])
    print("  walltime: A %.1f s -> B %.1f s" % (ta_, tb_))
    art = os.path.join(HERE, "s25_spdb_h3.json")
    json.dump(dict(a=dict(walltime_s=ta_, records=ra,
                          n_segments=a["n_segments"]),
                   b=dict(walltime_s=tb_, records=rb,
                          preplan=b["record_preplan"],
                          n_segments=b["n_segments"]),
                   pycount=pycount()), open(art, "w"), indent=1)
    print("  artifact -> %s" % art)
    return ok


def main():
    mode = (sys.argv[1] if len(sys.argv) > 1 else "m0").lower()
    if mode == "m0":
        ok = mode_m0()
    elif mode == "m12gate":
        ok = mode_m12gate()
    elif mode == "m4gate":
        ok = mode_m4gate()
    elif mode == "m5gate":
        ok = mode_m5gate()
    elif mode == "m5cgate":
        ok = mode_m5cgate()
    elif mode == "h3gate":
        ok = mode_h3gate()
    elif mode == "m6gate":
        ok = mode_m6gate()
    elif mode == "mbwalk":
        ok = mode_mbwalk()
    elif mode in ("ma", "mb", "mc", "md", "me"):
        ok = mode_measure(mode)
    else:
        print("unknown mode %r" % mode)
        ok = False
    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
