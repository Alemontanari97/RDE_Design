#!/usr/bin/env python3
"""Re-run, on s2, the proofs of the 17 carriers whose closure holds a1_qntr.py / a1_plug_spline_opt.py
(worktree of rde-nozzle-revalidation), outputs redirected as in restamp_run_2026-10-23.py, in LANES: the jobs
named on the command line run one after the other on one core (so that the re-stamp fits beside other work
inside s2's 12-thread rule). Every QNTR_/PSPL_/TWOP_/A1_ variable is removed: the default path; on one core
the default has no worker (a1_qntr.default_workers() = 0).
usage: restamp_lanes.py <run dir> <cpu> <job> [<job> ...]
jobs: t04 t05 t07 t07b rot_march o31_rot plug_margin base_pressure chutkey_twin axi_fan quick_regression t17_<case>"""
import os
import shutil
import subprocess
import sys
import time

WT = "/data10/falco/RDE/_wt_rde_revalidation"
VAL = os.path.join(WT, "validation")
RVD = os.path.join(VAL, "_revalidation_2026-10-07")
PY = "/data10/falco/RDE/venv-a1/bin/python"
ENV = dict(os.environ, PYTHONUNBUFFERED="1", MALLOC_ARENA_MAX="2",
           XLA_FLAGS="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=1",
           OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
for k in list(ENV):
    if k.startswith(("QNTR_", "PSPL_", "TWOP_", "A1_")):
        ENV.pop(k)

RUN, cpu, names = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
OUT = os.path.join(RUN, "out")
os.makedirs(os.path.join(RUN, "figs"), exist_ok=True)
if not os.path.isdir(OUT):
    try:
        shutil.copytree(os.path.join(RVD, "out"), OUT, symlinks=True)
        for f in os.listdir(OUT):
            if f.startswith("t17_") and f.endswith("_rows.json"):
                os.remove(os.path.join(OUT, f))
    except FileExistsError:          # another lane made it first
        pass


def harness(name, argv=()):
    path = os.path.join(RVD, "tests", name + ".py")
    code = ("import sys, runpy; sys.path.insert(0, %r); import rv; rv.OUT = %r; rv.FIGS = %r; "
            "sys.argv = [%r] + %r; runpy.run_path(%r, run_name='__main__')"
            % (os.path.join(RVD, "ref"), OUT, os.path.join(RUN, "figs"), path, list(argv), path))
    return [PY, "-c", code], os.path.join(RVD, "tests"), dict(ENV)


def verifier(script, artvar):
    env = dict(ENV)
    if artvar:
        env[artvar] = os.path.join(RUN, "old_art", script)
        os.makedirs(env[artvar], exist_ok=True)
    return [PY, os.path.join(VAL, script + ".py")], VAL, env


JOBS = {"t04": lambda: harness("t04_axi_source_channel"), "t05": lambda: harness("t05_geno_migdal"),
        "t07": lambda: harness("t07_gradients"), "t07b": lambda: harness("t07b_phases"),
        "rot_march": lambda: verifier("a1_rot_march", None), "o31_rot": lambda: verifier("o31_rot", None),
        "plug_margin": lambda: verifier("a1_plug_margin", "PMRG_ART"),
        "base_pressure": lambda: verifier("base_pressure", "BPRS_ART"),
        "chutkey_twin": lambda: verifier("a1_chutkey_twin", "CHTW_ART"),
        "axi_fan": lambda: verifier("a1_axi_fan", "AFAN_ART"),
        "quick_regression": lambda: ([PY, os.path.join(RVD, "tests", "quick_regression.py")],
                                     os.path.join(RVD, "tests"), dict(ENV))}
for c in ("planar", "methane", "rao61", "axial", "hth", "migdal", "bell", "bellideal"):
    JOBS["t17_" + c] = (lambda c=c: harness("t17_slides", [c]))
bad = [n for n in names if n not in JOBS]
if bad:
    raise SystemExit("unknown jobs: %s" % bad)
head = subprocess.run(["git", "-C", WT, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
dirty = subprocess.run(["git", "-C", WT, "status", "--porcelain", "--untracked-files=no"], capture_output=True,
                       text=True).stdout.strip()
for name in names:
    cmd, cwd, env = JOBS[name]()
    t0 = time.time()
    with open(os.path.join(RUN, "%s.log" % name), "w") as log:
        log.write("== %s on cpu %d, start %s, HEAD %s, tracked changes: %s\n"
                  % (name, cpu, time.strftime("%Y-%m-%d %H:%M:%S"), head, dirty.replace("\n", "; ") or "none"))
        log.flush()
        rc = subprocess.run(["nice", "-n", "19", "taskset", "-c", str(cpu)] + cmd, cwd=cwd, env=env,
                            stdout=log, stderr=subprocess.STDOUT).returncode
        log.write("\n== exit %d, %.0f s, end %s\n" % (rc, time.time() - t0, time.strftime("%Y-%m-%d %H:%M:%S")))
    print("%-16s exit %d  %.0f s  (cpu %d)" % (name, rc, time.time() - t0, cpu), flush=True)
print("lane cpu %d done %s" % (cpu, time.strftime("%Y-%m-%d %H:%M:%S")), flush=True)
