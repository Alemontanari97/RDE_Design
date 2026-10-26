#!/usr/bin/env python3
"""Re-run, on s2, the proofs of the 17 carriers whose closure holds a1_qntr.py / a1_plug_spline_opt.py
(worktree of rde-nozzle-revalidation), outputs redirected: harness tests write into a COPY of out/ (the t17
ladder caches removed), old verifiers into RUN/old_art/<script> through their *_ART variables.
usage: restamp_run.py <wave 1|2> <first cpu>"""
import os
import shutil
import subprocess
import sys
import time

WT = "/data10/falco/RDE/_wt_rde_revalidation"
VAL = os.path.join(WT, "validation")
RVD = os.path.join(VAL, "_revalidation_2026-10-07")
RUN = "/data10/falco/RDE/_wt_logs/restamp_2026-10-23"
PY = "/data10/falco/RDE/venv-a1/bin/python"
OUT = os.path.join(RUN, "out")
ENV = dict(os.environ, PYTHONUNBUFFERED="1", MALLOC_ARENA_MAX="2",
           XLA_FLAGS="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=1",
           OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
for k in list(ENV):
    if k.startswith(("QNTR_", "PSPL_", "TWOP_", "A1_")):
        ENV.pop(k)

wave, cpu0 = sys.argv[1], int(sys.argv[2])
os.makedirs(RUN, exist_ok=True)
if not os.path.isdir(OUT):
    shutil.copytree(os.path.join(RVD, "out"), OUT, symlinks=True)
    for f in os.listdir(OUT):
        if f.startswith("t17_") and f.endswith("_rows.json"):
            os.remove(os.path.join(OUT, f))
os.makedirs(os.path.join(RUN, "figs"), exist_ok=True)


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


if wave == "1":
    jobs = {"t04": harness("t04_axi_source_channel"), "t05": harness("t05_geno_migdal"),
            "t07": harness("t07_gradients"), "t07b": harness("t07b_phases"),
            "rot_march": verifier("a1_rot_march", None), "o31_rot": verifier("o31_rot", None),
            "plug_margin": verifier("a1_plug_margin", "PMRG_ART"), "base_pressure": verifier("base_pressure", "BPRS_ART"),
            "chutkey_twin": verifier("a1_chutkey_twin", "CHTW_ART"), "axi_fan": verifier("a1_axi_fan", "AFAN_ART")}
elif wave == "1b":
    jobs = {"rot_march": verifier("a1_rot_march", None), "o31_rot": verifier("o31_rot", None),
            "plug_margin": verifier("a1_plug_margin", "PMRG_ART"), "base_pressure": verifier("base_pressure", "BPRS_ART"),
            "axi_fan": verifier("a1_axi_fan", "AFAN_ART")}
else:
    jobs = {"t17_" + c: harness("t17_slides", [c]) for c in
            ("planar", "methane", "rao61", "axial", "hth", "migdal", "bell", "bellideal")}
    jobs["quick_regression"] = ([PY, os.path.join(RVD, "tests", "quick_regression.py")], os.path.join(RVD, "tests"), dict(ENV))
procs = {}
for i, (name, (cmd, cwd, env)) in enumerate(jobs.items()):
    log = open(os.path.join(RUN, "%s.log" % name), "w")
    log.write("== %s on cpu %d, start %s\n" % (name, cpu0 + i, time.strftime("%Y-%m-%d %H:%M:%S")))
    log.flush()
    procs[name] = (subprocess.Popen(["nice", "-n", "19", "taskset", "-c", str(cpu0 + i)] + cmd, cwd=cwd, env=env,
                                    stdout=log, stderr=subprocess.STDOUT), log, time.time())
left = dict(procs)
while left:
    for name in list(left):
        p, log, t0 = left[name]
        if p.poll() is not None:
            log.write("\n== exit %d, %.0f s, end %s\n" % (p.returncode, time.time() - t0, time.strftime("%Y-%m-%d %H:%M:%S")))
            log.close()
            print("%-16s exit %d  %.0f s" % (name, p.returncode, time.time() - t0), flush=True)
            left.pop(name)
    time.sleep(5)
print("wave %s done %s" % (wave, time.strftime("%Y-%m-%d %H:%M:%S")), flush=True)
