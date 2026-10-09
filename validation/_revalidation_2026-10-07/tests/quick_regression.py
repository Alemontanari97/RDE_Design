#!/usr/bin/env python3
"""QUICK REGRESSION of the rde-nozzle tool against the cases certified by the 2026-10-07/09 revalidation (owner,
2026-10-09: "istituire delle prove rapide ed indicative che ci permettano di certificare possibili versioni future con
casi passati"). A few minutes on one core; it writes NOTHING into the repository (report and scratch go to a temporary
folder, or to --out); the certified records in out/ are the reference and are only read.

  A  model checks with exact or published references -- t01 (gas tables), t02 (cells), t09 (Rao 1961, Humphreys 1971)
     -- re-run with their output redirected: every row must keep the verdict of its certified record.
  B  fingerprints -- every certified landing of the optimiser cases (planar, methane Rao, Rao 1961, axial exit,
     Humphreys 1971, Migdal two walls, bell TOC, ideal bell) and each case's reference re-marched ON THE WALK GRID
     (level 1 of the slide reading t17) and compared with its certified thrust:
       IDENTICAL  relative change <= 1e-13 (the same arithmetic);
       DRIFT      every landing's gap to the reference, (J - J_ref)/J_ref, moved by less than a tenth of what one grid
                  doubling does to the same gaps in the certified reading, and J_ref by less than a tenth of its own
                  change from level 1 to level 2: the certified ppm numbers cannot move beyond their stated precision,
                  but quote them only after the case's full protocol is re-run;
       CHANGED    beyond: the case must be re-certified with its full protocol before any number of it is quoted.
     Every fingerprint march must be certified (worst certificate <= 1).
  C  the driver -- the certified planar walk B0 re-run and compared bit for bit (landing, history, stop, counts).
  Rejector (R5): the planar landing B marched on the NEXT grid (160,41) is compared with its walk-grid record and must
  come out CHANGED (a change of the march's discretisation is caught); the classifier itself is checked first on
  synthetic changes of a certified row (same numbers -> IDENTICAL, 1e-12 -> DRIFT, 1e-5 -> CHANGED).
  The GENO run outputs are not in git (their decks and md5 manifest are): when absent the run stops with exit 2 and
  says how to regenerate them.
Exit 0 iff no CHANGED case, no verdict lost in A, every march certified, the walk identical and the rejector caught.
usage: quick_regression.py [--out DIR] [--skip-walk]
"""
import json
import os
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RVD = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(RVD, "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402

T0 = time.time()
args = sys.argv[1:]
OUTDIR = args[args.index("--out") + 1] if "--out" in args else tempfile.mkdtemp(prefix="quick_regression_")
os.makedirs(OUTDIR, exist_ok=True)
SKIP_WALK = "--skip-walk" in args
CERT = rv.OUT                                      # the certified records (read only)
IDENT = 1e-13
TENTH = 0.1
report = dict(date=time.strftime("%Y-%m-%d %H:%M:%S"), outdir=OUTDIR, A={}, B={}, C={}, rejector={})
bad = []


def say(msg):
    print(msg, flush=True)


def certified(name):
    return json.load(open(os.path.join(CERT, name + ".json")))


def run_redirected(script, argv, tag):
    """Run a harness test with rv.OUT and rv.FIGS redirected to OUTDIR (nothing in the repo is rewritten)."""
    code = ("import sys, runpy; sys.path.insert(0, %r); import rv; rv.OUT = %r; rv.FIGS = %r; "
            "sys.argv = [%r] + %r; runpy.run_path(%r, run_name='__main__')"
            % (os.path.join(RVD, "ref"), OUTDIR, OUTDIR, script, list(argv), script))
    t0 = time.time()
    r = subprocess.run([sys.executable, "-c", code], cwd=HERE, capture_output=True, text=True)
    open(os.path.join(OUTDIR, tag + ".log"), "w").write(r.stdout + r.stderr)
    return r.returncode, time.time() - t0


# ------------------------------------------------------------------------------------------------------------ A
say("== A  model checks against exact or published references (verdicts must not change)")
for t in ("t01_thermo", "t02_cells", "t09_literature"):
    code, sec = run_redirected(os.path.join(HERE, t + ".py"), [], "A_" + t)
    try:
        new = json.load(open(os.path.join(OUTDIR, t + ".json")))
    except FileNotFoundError:
        bad.append("A %s: no result (exit %d, see %s)" % (t, code, os.path.join(OUTDIR, "A_" + t + ".log")))
        say("   %-16s NO RESULT (exit %d)" % (t, code))
        continue
    old = certified(t)
    by_new = {r["label"]: r for r in new["rows"]}
    lost, moved = [], 0
    for r in old["rows"]:
        n = by_new.get(r["label"])
        if n is None or bool(n["ok"]) != bool(r["ok"]):
            lost.append(r["label"][:70])
        elif isinstance(r["value"], (int, float)) and isinstance(n["value"], (int, float)) and r["value"] != n["value"]:
            moved += 1
    report["A"][t] = dict(rows=len(old["rows"]), verdicts_lost=lost, values_moved=moved, seconds=sec)
    if lost:
        bad.extend("A %s: verdict changed: %s" % (t, x) for x in lost)
    say("   %-16s %d rows, verdicts kept %s, values moved %d (%.0f s)" % (t, len(old["rows"]), "YES" if not lost else
                                                                         "NO: %s" % lost, moved, sec))


# ------------------------------------------------------------------------------------------------------------ B
def classify(case, J_now, J_cert, cert_now, keys, ref_key="ref"):
    """IDENTICAL / DRIFT / CHANGED from the walk-grid thrusts now and at certification (level 1 of t17)."""
    rows = json.load(open(os.path.join(CERT, "t17_%s_rows.json" % case)))["rows"]
    rel = {k: abs(J_now[k] / J_cert[k] - 1.0) for k in keys}
    worst_cert = max(cert_now.values()) if cert_now else 0.0
    if max(rel.values()) <= IDENT:
        verdict = "IDENTICAL"
    else:
        lands = [k for k in keys if k != ref_key]
        gap_now = {k: J_now[k] / J_now[ref_key] - 1.0 for k in lands}
        gap_cert = {k: J_cert[k] / J_cert[ref_key] - 1.0 for k in lands}
        # what one grid doubling does to the same gaps, and to the reference, in the certified reading
        g_grid = max([abs((r1[k] / r1["ref"]) - (r0[k] / r0["ref"])) for k in lands
                      for r0, r1 in zip(rows[:-1], rows[1:]) if k in r0 and k in r1] + [0.0])
        r_grid = abs(rows[1]["ref"] / rows[0]["ref"] - 1.0)
        d_gap = max([abs(gap_now[k] - gap_cert[k]) for k in lands] + [0.0])
        d_ref = rel[ref_key]
        ok = d_gap <= TENTH * g_grid and d_ref <= TENTH * max(r_grid, 1e-12)
        verdict = "DRIFT" if ok else "CHANGED"
    if worst_cert > 1.0:
        verdict = "UNCERTIFIED"
    return verdict, rel, worst_cert


def fingerprint(case, make_po, landings, ref, ref_W=None):
    """landings: {key: W}; ref: 'march' (ref_W marched), 'value' (a constant J_ref: the planar bound), or None."""
    rows = json.load(open(os.path.join(CERT, "t17_%s_rows.json" % case)))["rows"]
    lev1 = rows[0]
    t0 = time.time()
    po = make_po()
    J_now, J_cert, cert_now = {}, {}, {}
    if ref == "march":
        o, _ = po.march_record(None if ref_W is None else np.asarray(ref_W, float))
        J_now["ref"], cert_now["ref"] = float(po.J_of(o)), float(o["cert_worst"])
    else:
        J_now["ref"] = float(ref)
    J_cert["ref"] = float(lev1["ref"])
    for k, W in landings.items():
        o, _ = po.march_record(np.asarray(W, float))
        J_now[k], cert_now[k] = float(po.J_of(o)), float(o["cert_worst"])
        J_cert[k] = float(lev1[k])
    verdict, rel, wc = classify(case, J_now, J_cert, cert_now, list(J_now))
    report["B"][case] = dict(level=lev1["level"], verdict=verdict, worst_relative_change=max(rel.values()),
                             worst_certificate=wc, J_now=J_now, J_cert=J_cert, seconds=time.time() - t0)
    if verdict in ("CHANGED", "UNCERTIFIED"):
        bad.append("B %s: %s" % (case, verdict))
    say("   %-10s %-11s worst relative change %.1e, worst certificate %.3f, %d marches (%.0f s)"
        % (case, verdict, max(rel.values()), wc, len(J_now) - (ref != "march"), time.time() - t0))
    return J_now


say("== B0 the classifier on synthetic changes of a certified planar row (it must tell the three verdicts apart)")
r0 = json.load(open(os.path.join(CERT, "t17_planar_rows.json")))["rows"][0]
base = dict(ref=float(r0["ref"]), B=float(r0["B"]))
for name, f, want in (("same numbers", 0.0, "IDENTICAL"), ("landing x(1 + 1e-12)", 1e-12, "DRIFT"),
                      ("landing x(1 + 1e-5)", 1e-5, "CHANGED")):
    got = classify("planar", dict(ref=base["ref"], B=base["B"] * (1.0 + f)), base, {}, ["ref", "B"])[0]
    report.setdefault("classifier", {})[name] = got
    if got != want:
        bad.append("classifier: %s gives %s, not %s" % (name, got, want))
    say("   %-22s -> %-9s (expected %s)" % (name, got, want))
# the GENO run outputs are not in git (decks + md5 manifest are): say so plainly when they are absent
need = [os.path.join(RVD, "geno", g, f) for g in ("rao_sdt_L0448", "rao61_e381_pbR_mi15", "axial_e381_RD04_mi15",
                                                  "hth71_rao_mi17") for f in ("plug_diag.dat", "inf.sol", "sup.sol")]
missing = [x for x in need if not os.path.exists(x)]
if missing:
    say("   GENO outputs absent (%d files, e.g. %s): regenerate them on s3 from the committed decks "
        "(geno/<case>/input.ini, md5 in geno/OUTPUTS_md5_2026-10-09.txt) before this regression" % (len(missing), missing[0]))
    bad.append("GENO outputs absent")
    json.dump(dict(report, failures=bad), open(os.path.join(OUTDIR, "quick_regression.json"), "w"), indent=1, default=float)
    sys.exit(2)

say("== B  fingerprints: certified landings re-marched on their walk grid")
Jl = lambda n: certified(n)                                                       # noqa: E731
# planar (exact optimum: the bound T, a constant)
import planar_posing as PP                         # noqa: E402
pl = {k: Jl(v)["landing"]["W"] for k, v in dict(B="t08a_walk_B0_K80_qntr", C="t08a_walk_C0_K80_qntr",
                                                 A1="t08a_walk_A1_K80_qntr", B1="t08a_walk_B1_K80_qntr").items()}
pp1 = PP.PlanarPlug(K=80, N=21, m=12, L=2.0)
fingerprint("planar", lambda: pp1, pl, pp1.T_ideal)
# the four Rao posings (GENO's contour marched as the reference)
import rao_posing as RP                            # noqa: E402
for case, geno, runs in (("methane", "rao_sdt_L0448", dict(A="t08b_walk_A0_qntr", C="t08b_walk_C0_qntr")),
                         ("rao61", "rao61_e381_pbR_mi15", dict(bump="t10_walk_rao61_e381_pbR_mi15_bump_qntr",
                                                               half="t10_walk_rao61_e381_pbR_mi15_half_qntr")),
                         ("axial", "axial_e381_RD04_mi15", dict(bump="t10_walk_axial_e381_RD04_mi15_bump_qntr",
                                                                half="t10_walk_axial_e381_RD04_mi15_half_qntr")),
                         ("hth", "hth71_rao_mi17", dict(bump="t10_walk_hth71_rao_mi17_bump_qntr",
                                                        half="t10_walk_hth71_rao_mi17_half_qntr"))):
    D = os.path.join(RVD, "geno", geno)
    fingerprint(case, lambda D=D: RP.posing_level(D, 1, design=True), {k: Jl(v)["landing"]["W"] for k, v in runs.items()},
                "march")
# Migdal's two walls (the production carrier on GENO's walls)
os.environ.update(dict(TWOP_GAS=os.path.join(CERT, "t08c_gas.json"), TWOP_ART=os.path.join(OUTDIR, "twop_art")))
os.makedirs(os.environ["TWOP_ART"], exist_ok=True)
import a1_twowall as T                             # noqa: E402
tw1 = T.TwoWall(K=140, N=31, verbose=False)
fingerprint("migdal", lambda: tw1, {k: Jl(v)["landing"]["W"] for k, v in dict(free="t08c_walk_0_qntr",
                                                                                cls="t08c_walk_1_qntr").items()},
            "march", ref_W=np.asarray(tw1.W_ref, float))
# the two bells (the reference = the best 8-point curve of GENO's wall)
import bell_posing as BP                           # noqa: E402
for case, runs in (("bell", dict(tic="t15_bell_toc_tic", tic81="t15_bell_toc_tic_NI81", steep="t15_bell_toc_steep",
                                 steep81="t15_bell_toc_steep_NI81")),
                   ("bellideal", dict(stretched="t15_bell_ideal_stretched", stretched81="t15_bell_ideal_stretched_NI81",
                                      extended="t15_bell_ideal_extended", extended81="t15_bell_ideal_extended_NI81"))):
    d = {k: Jl(v) for k, v in runs.items()}
    w0 = next(iter(d.values()))
    bp = BP.BellPosing(w0["L"], w0["yL"], NI=41, Nw=120, M=8)
    fit_V = bp.fit_lsq(np.asarray(w0["geno_x"]), np.asarray(w0["geno_y"]))

    class Lev:
        def march_record(self, V, bp=bp):
            return bp.record(V)

        def J_of(self, o, bp=bp):
            return bp.J_of(o)
    fingerprint(case, Lev, {k: w["landing"]["V"] for k, w in d.items()}, "march", ref_W=fit_V)

# ------------------------------------------------------------------------------------------------------------ rejector
say("== rejector: the planar landing B on the NEXT grid (160,41) against its walk-grid record must be CHANGED")
pp2 = PP.PlanarPlug(K=160, N=41, m=12, L=2.0)
o, _ = pp2.march_record(np.asarray(pl["B"], float))
J2 = float(pp2.J_of(o))
rows_pl = json.load(open(os.path.join(CERT, "t17_planar_rows.json")))["rows"]
v_rej, rel_rej, _ = classify("planar", dict(ref=float(rows_pl[0]["ref"]), B=J2),
                             dict(ref=float(rows_pl[0]["ref"]), B=float(rows_pl[0]["B"])), {}, ["ref", "B"])
caught = v_rej == "CHANGED"
report["rejector"] = dict(verdict=v_rej, relative_change=rel_rej["B"], caught=caught)
if not caught:
    bad.append("rejector not caught (%s)" % v_rej)
say("   verdict %s (relative change %.1e): %s" % (v_rej, rel_rej["B"], "caught" if caught else "NOT caught"))

# ------------------------------------------------------------------------------------------------------------ C
if SKIP_WALK:
    say("== C  driver walk SKIPPED (--skip-walk)")
    report["C"] = dict(skipped=True)
else:
    say("== C  the driver: certified planar walk B0 re-run, bit for bit")
    code, sec = run_redirected(os.path.join(HERE, "t08a_planar_walk.py"), ["B", "0"], "C_walk_B0")
    try:
        new, new_rep = (json.load(open(os.path.join(OUTDIR, "t08a_walk_B0_K80_qntr%s.json" % s))) for s in ("", "_report"))
        old, old_rep = certified("t08a_walk_B0_K80_qntr"), certified("t08a_walk_B0_K80_qntr_report")
        same = (np.array_equal(np.asarray(new["landing"]["W"], float), np.asarray(old["landing"]["W"], float))
                and new["landing"]["J"] == old["landing"]["J"]
                and np.array_equal(np.asarray(new["hist"], float), np.asarray(old["hist"], float))
                and all(new_rep.get(k) == old_rep.get(k) for k in ("stop", "segments", "accepted", "rejected",
                                                                     "records", "secants")))
    except (FileNotFoundError, KeyError) as err:
        same = False
        say("   no comparable result: %s (exit %d)" % (err, code))
    report["C"] = dict(identical=bool(same), seconds=sec)
    if not same:
        bad.append("C: the planar walk B0 is not bit-identical to its certified record")
    say("   walk B0 %s (%.0f s)" % ("BIT-IDENTICAL" if same else "DIFFERENT", sec))

# ------------------------------------------------------------------------------------------------------------ verdict
report["failures"] = bad
report["seconds"] = time.time() - T0
json.dump(report, open(os.path.join(OUTDIR, "quick_regression.json"), "w"), indent=1, default=float)
drift = [c for c, r in report["B"].items() if r["verdict"] == "DRIFT"]
say("== quick regression: %s in %.0f s%s; report %s" % (
    "PASS" if not bad else "FAIL (%d)" % len(bad), time.time() - T0,
    ("; DRIFT (indicative, re-run the full protocol before quoting): %s" % ", ".join(drift)) if drift else "",
    os.path.join(OUTDIR, "quick_regression.json")))
for b in bad:
    say("   FAIL: %s" % b)
sys.exit(0 if not bad else 1)
