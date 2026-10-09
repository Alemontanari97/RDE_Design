#!/usr/bin/env python3
"""T08c -- the production carrier's walks on its known optimum (Migdal, vacuum, exit annulus pinned: C_F <= C_F,1D,
reached by the perfect nozzle = GENO's pair). Re-marches GENO's walls (W_ref) and every landing at (140,31), (280,61),
(560,121) with the carrier itself (TwoWall(K, N): the same representation, finer stations and start rows).
Checks:
  M1 the unconstrained walk returns from a folded start (-4.5e-4) to GENO's pair: |C_F(landing) - C_F(GENO)| at the
     walk's grid within the march's own error there (|C_F(GENO)/C_F,1D - 1|), and the landing in class;
  M2 the landing's excess over GENO at the walk's grid is a discretisation artefact: at (560,121) the landing is not
     above GENO's pair beyond the march's error there (one-sided);
  M3 the class-constrained walk (if run) reaches the unconstrained value within 1e-6.
"""
import json
import os
import sys

RV = "/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07"
sys.path.insert(0, os.path.join(RV, "ref"))
import rv                                          # noqa: E402
os.environ.update(dict(TWOP_GAS=os.path.join(rv.OUT, "t08c_gas.json"),
                       TWOP_ART="/tmp/claude-1700/-data10-falco-MOSE/92599c7b-9637-4352-802d-d26f8eac9fd5/scratchpad/twop_art"))
import numpy as np                                 # noqa: E402
import a1_twowall as T                             # noqa: E402

R = rv.Report("t08c_summary")
walks = {}
for k, name in ((0, "t08c_walk_0"), (1, "t08c_walk_1_a0.002")):
    fn = os.path.join(rv.OUT, name + ".json")
    if os.path.exists(fn):
        walks[k] = json.load(open(fn))
fn = os.path.join(rv.OUT, "t08c_walk_1.json")
if os.path.exists(fn):
    w_out = json.load(open(fn))
    R.note("class walk from the 0.01 bump (OUT of class: KS - mu0 %+.4f): %d bases, %d records -- %s" % (
        w_out["start_r"]["ks"], w_out["segments"], w_out["records"],
        "no step (the driver's restoration is inert, T08a)" if w_out["landing"]["W"] == w_out["start_r"]["W"] else "moved"))
    R.check("M4 the driver restores an out-of-class start [expected to fail: inert restoration]",
            float(w_out["landing"]["ks"]), None, ok=w_out["landing"]["ks"] >= 0.0)
w0 = walks[0]
CF1 = w0["CF_1d"]
R.note("C_F,1D %.9f; walk without class: GENO %.9f (%+.3e), start %+.3e, landing %.9f (%+.3e), gaps plug %.1e shroud %.1e,"
       " KS - mu0 %+.4f, %d bases" % (CF1, w0["ref"]["J"], w0["ref"]["J"] / CF1 - 1, w0["start_r"]["J"] / CF1 - 1,
                                     w0["landing"]["J"], w0["landing"]["J"] / CF1 - 1, w0["landing"]["gap_plug"],
                                     w0["landing"]["gap_shroud"], w0["landing"]["ks"], w0["segments"]))
err140 = abs(w0["ref"]["J"] / CF1 - 1.0)
R.check("M1 the landing equals GENO's pair at the walk's grid within the march's error there",
        w0["landing"]["J"] / w0["ref"]["J"] - 1.0, err140)
R.check("M1 the landing is in class (KS - mu0 >= 0)", w0["landing"]["ks"], None, ok=w0["landing"]["ks"] >= 0.0)
rows = []
for K, N in ((140, 31), (280, 61), (560, 121)):
    tw = T.TwoWall(K=K, N=N, verbose=False)
    row = dict(K=K, N=N)
    for name, W in (("geno", tw.W_ref), ("landing0", w0["landing"]["W"])) + (
            (("landing1", walks[1]["landing"]["W"]),) if 1 in walks else ()):
        out, _ = tw.march_record(np.asarray(W, float))
        row[name] = float(tw.J_of(out)) / CF1 - 1.0
        row[name + "_cert"] = float(out["cert_worst"])
    rows.append(row)
    R.note("(K %3d, N %3d): C_F/C_F,1D - 1: GENO %+.3e | landing (no class) %+.3e%s | certs %s" % (
        K, N, row["geno"], row["landing0"], (" | landing (class) %+.3e" % row["landing1"]) if 1 in walks else "",
        ", ".join("%.2f" % row[k] for k in row if k.endswith("_cert"))))
f = rows[-1]
R.check("M2 at (560,121) the landing is not above GENO's pair beyond the march's error there (one-sided)",
        f["landing0"] - f["geno"], abs(f["geno"]), ok=f["landing0"] - f["geno"] <= abs(f["geno"]))
if 1 in walks:
    R.check("M3 the class-constrained walk reaches the unconstrained value within 1e-6",
            walks[1]["landing"]["J"] / w0["landing"]["J"] - 1.0, 1e-6)
sys.exit(R.save(dict(rows=rows, CF_1d=CF1)))
