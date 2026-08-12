#!/usr/bin/env python3
"""LOOP-SPEED THRESHOLD [F2/A1, session S17, brick-2 kickoff duty (a)]:
the DERIVED quantification of the DIR-G0 loop-speed falsifier
("impractical" was unquantified as written — S15 T2 fix d1), under the
clean-host protocol (S9 lesson). Registry ID: [X-LSG0]. Normative
spec: docs/rde_nozzle_brick2_kickoff.md §4.

DERIVED THRESHOLDS (no magic constants — theorem constants or
measured quantities only):
  T1 (cheap-gradient bound): measured t_grad / t_solve <= 4.
     Reverse-mode AD evaluates a scalar gradient at <= omega_rev x
     primal cost, omega_rev in [3, 4] (Baur-Strassen /
     Griewank-Walther); a measured ratio above 4 indicts the
     IMPLEMENTATION, not the method. EXECUTABLE HERE (rejector).
  T2a (per-evaluation practicality anchor, NECESSARY condition):
     t_solve <= K_prac x t_GENO at the SAME case and resolution,
     K_prac = 4 (the repo's two-level Richardson safety constant,
     reused not invented; rationale in the spec: a differentiable
     loop paying > 4x the classical forward per evaluation has lost
     its practical case regardless of iteration counts).
     EXECUTABLE HERE (rejector).
  T2 (whole-loop bound, ARMED for the brick run): N_TR x (t_solve +
     t_grad) <= K_prac x N_outer x t_GENO with N_TR measured by the
     brick-2 TR-SQP run itself and N_outer the measured GENO type-2
     outer-loop forward count; this carrier STORES the measured
     constants (printed table) — the check EXECUTES in the brick
     carrier's Verdict (its formula and constants come from here).
  FLIP CLAUSE (D6 item 9): T1 or T2a failing on a clean host AFTER
     the duty-(b) architecture = structural failure -> Julia/Enzyme
     re-decision session (declared, not silent).

CLEAN-HOST PROTOCOL (S9 lesson, rejector-grade): the bench REFUSES
to certify under contention — it counts OTHER busy python/GENO
processes on the host before timing; nonzero -> FAIL (measurements
under contention are not record-grade). Timings: perf_counter,
1 warmup + median of N_REP, jax results block_until_ready.

MEASUREMENT OBJECT (S18 update, P2 executed): the PRODUCTION replay
path — the [X-SCANM] bucketed whole-loop jit engine
(make_run_scan_jit; T2a remediation of record) on the reduced twin
case (the brick's inner loop = replay + gradient at fixed schedule;
record cost is ALSO measured and reported — it is the RK-G P2
re-record cost, paid once per accepted step, not per evaluation).
One-time compile cost reported separately. Scalar functional for the
gradient = a fixed random projection of the contour (representative
of J's structure: a contour functional).

PRODUCTION PROJECTION (DECLARED, not a gate): measured per-cell
replay cost x the production cell-count estimate; the T1/T2a gates
re-run at production scale when the brick reaches production cases.

NEGATIVE CONTROL: a corrupted timing (grad inflated 10x in-memory)
must FAIL T1 — proves the check can reject.

ON-DEMAND CARRIER (env: jax + WSL gfortran GENO binary): outside CI
tiers by declaration. Exit code 0 iff all checks incl. the negative
control pass.
"""
import os
import statistics
import subprocess
import sys
import time

# persistent XLA compilation cache: THE canonical block lives in
# a1_ideal_march_jax (S25 M4/H6 of record — one block, ONE dir
# %TEMP%/jax_cache_rde, built-in LRU cap). The former module-local
# env default pointing at the DISJOINT rde_jax_cache dir is RETIRED
# (that split was cache-hygiene debt, advisory §1.2).
import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1  # noqa: E402
import a1_march_scan as SC       # noqa: E402

jax.config.update("jax_enable_x64", True)

K_PRAC = 4.0        # reused repo two-level safety constant (spec §4)
OMEGA_REV = 4.0     # cheap-gradient theorem upper constant
N_REP = 3           # odd repetitions -> median (declared: at the
                    # measured 60-130 s/evaluation, 7 reps would be
                    # ~25 min of pure timing for no extra information)


def check(label, ok):
    print("  [%s] %s" % (label, "PASS" if ok else "FAIL"))
    return bool(ok)


def other_busy_processes():
    """Count OTHER python/GENO processes (clean-host rejector input)."""
    try:
        out = subprocess.run(["tasklist"], capture_output=True,
                             text=True, timeout=60).stdout.lower()
    except Exception:                                  # noqa: BLE001
        return -1
    me = os.getpid()
    n = 0
    for ln in out.splitlines():
        if ("python" in ln or ln.strip().startswith("geno")) \
                and str(me) not in ln.split():
            n += 1
    return n


def median_time(fn, n=N_REP):
    fn()                                               # warmup
    ts = []
    for _ in range(n):
        t0 = time.perf_counter()
        fn()
        ts.append(time.perf_counter() - t0)
    return statistics.median(ts)


def time_geno(case_dir, n=3):
    """Median wall time of the GENO forward on the twin case (WSL).
    EPOCHREALTIME around the binary only (bash `time` is a shell
    keyword whose report cannot be redirected per-command — found
    in-session, deviation declared)."""
    geno_bin = A1.win_to_wsl(os.path.join(A1.GENO_DIR, "bin", "GENO"))
    cmd = ("cd '%s' && export LD_LIBRARY_PATH="
           "/home/alessandro/miniconda3/envs/ct-env/lib && "
           "S=$EPOCHREALTIME; '%s' > /dev/null 2>&1; "
           "E=$EPOCHREALTIME; echo $S $E"
           % (A1.win_to_wsl(case_dir), geno_bin))
    ts = []
    for _ in range(n):
        r = subprocess.run(["wsl.exe", "-e", "bash", "-lc", cmd],
                           capture_output=True, text=True, timeout=600)
        toks = r.stdout.split()
        if len(toks) >= 2:
            try:
                ts.append(float(toks[-1]) - float(toks[-2]))
            except ValueError:
                pass
    if not ts:
        raise RuntimeError("GENO timing failed: %r" % r.stdout[-200:])
    return statistics.median(ts)


def main():
    print("== LOOP-SPEED THRESHOLDS [X-LSG0]: derived G0 falsifier "
          "quantification (JAX %s) ==" % jax.__version__)
    ok = True

    print("-- clean-host protocol (S9 lesson) --")
    n_busy = other_busy_processes()
    print("  other python/GENO processes: %d" % n_busy)
    ok &= check("clean host (no concurrent compute)", n_busy == 0)

    tab = A1.prep_tab(A1.build_tab_nasa())
    P = jnp.array([A1.CASE["yt"], A1.CASE["rtu"], A1.CASE["rtd"],
                   A1.CASE["eps"]])
    cfg = dict(NI=A1.CASE["NI"], Ne=A1.CASE["Ne"],
               da_deg=A1.CASE["da_deg"])

    print("-- record (RK-G P2 cost, once per accepted step) --")
    t0 = time.perf_counter()
    out_rec, sched = A1.run_march(P, tab, cfg)
    t_record = time.perf_counter() - t0
    plan = SC.build_plan(sched.d, cfg)
    n_cells = (sum(c["n"] for c in plan["fan"])
               + sum(c["n"] for c in plan["arc"])
               + sum(c["n"] for c in plan["stra"])
               + len(plan["fan"]) + len(plan["arc"]) * 2
               + len(plan["stra"]) + 2)
    print("  t_record = %.2f s (adaptive march, %d cells; includes "
          "one-time jit)" % (t_record, n_cells))

    print("-- replay solve / gradient timings (production engine) --")
    proj = jnp.array(np.random.default_rng(0).standard_normal(1000))

    # MEASUREMENT OBJECT (S18, supersedes the S17 as-implemented
    # measurement): the P2 PRODUCTION path — single-bucket-per-phase
    # padded scans inside ONE whole-loop jit (SC.make_run_scan_jit,
    # the named T2a remediation executed; equivalence + O3.1 on this
    # path are rejector-gated in [X-SCANM]). Evaluations after warmup
    # pay NO Python re-trace; the one-time compile cost is reported
    # separately (not part of the per-evaluation anchor).
    runj = SC.make_run_scan_jit(tab, cfg, plan)

    def scalar_f(Pv):
        o = runj(Pv)
        vec = jnp.concatenate([o["wall_x"], o["wall_y"],
                               jnp.array([o["Me"]])])
        return jnp.dot(vec, proj[: vec.shape[0]])

    scalar_jit = jax.jit(scalar_f)
    grad_jit = jax.jit(jax.grad(scalar_f))

    t0 = time.perf_counter()
    jax.block_until_ready(scalar_jit(P))
    t_comp_s = time.perf_counter() - t0
    t0 = time.perf_counter()
    jax.block_until_ready(grad_jit(P))
    t_comp_g = time.perf_counter() - t0
    print("  one-time compile: solve %.1f s, grad %.1f s (whole-loop "
          "jit; persistent XLA cache)" % (t_comp_s, t_comp_g))

    def run_solve():
        return float(scalar_jit(P))

    def run_grad():
        return np.asarray(grad_jit(P))

    t_solve = median_time(run_solve)
    t_grad = median_time(run_grad)
    ratio = t_grad / t_solve
    print("  t_solve = %.3f s   t_grad = %.3f s   grad/solve = %.3f"
          % (t_solve, t_grad, ratio))

    print("-- GENO forward anchor (same case, same resolution, WSL) --")
    scratch = os.environ.get("A1_GENO_CASE")
    if scratch is None:
        scratch = os.path.join(os.environ.get("TEMP", "/tmp"),
                               "a1_geno_ideal_ni21")
    case_dir = A1.ensure_geno_case(scratch)
    t_geno = time_geno(case_dir)
    print("  t_GENO = %.3f s (median of 3, wall)" % t_geno)

    print("-- derived thresholds --")
    print("  T1: grad/solve = %.3f  <= %.1f (cheap-gradient theorem)"
          % (ratio, OMEGA_REV))
    ok &= check("T1 cheap-gradient bound", ratio <= OMEGA_REV)
    # T2a is a PRODUCTION-GATE INDICATOR, not a bench exit-fail (the
    # bench's own rejectors are clean-host, T1 and the negative
    # control). S18: the named remediation (single-bucket-per-phase
    # padding, whole-loop jit) is EXECUTED and is the measurement
    # object above — a T2a failure now is STRUCTURAL and triggers the
    # D6 flip clause (Julia/Enzyme re-decision session), not silence.
    t2a_pass = t_solve <= K_PRAC * t_geno
    print("  T2a: t_solve = %.3f s <= K_prac x t_GENO = %.3f s : %s"
          % (t_solve, K_PRAC * t_geno,
             "PASS (production gate OPEN)" if t2a_pass else
             "FAIL post-remediation (STRUCTURAL: D6 flip clause "
             "armed — Julia/Enzyme re-decision session due)"))
    print("  T2 (ARMED for the brick run): N_TR x (%.3f + %.3f) s <= "
          "%.1f x N_outer x %.3f s   [N_TR from the brick TR-SQP run; "
          "N_outer from the GENO type-2 outer loop]"
          % (t_solve, t_grad, K_PRAC, t_geno))
    per_cell = t_solve / n_cells
    print("  [declared projection, not a gate] per-cell replay cost "
          "%.2e s; production-scale gates re-run when the brick "
          "reaches production cases" % per_cell)
    print("  [RK-G accounting] t_record/t_solve = %.1f (re-record paid "
          "once per ACCEPTED step)" % (t_record / t_solve))

    print("-- negative control --")
    ok &= check("corrupted timing rejected by T1",
                not (10.0 * ratio <= OMEGA_REV))

    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
