#!/usr/bin/env python3
"""LAB-WF, THE CHECK OF RECORD (2026-10-06; owner: "questo confronto, tra fisso e rotante, va messo nella memoria della
git"). Plain rules: the same plug run in 3-D in the laboratory frame (the RDE inlet turning in time) and in the frame
turning with the detonation wave (the inlet standing still) must give the same wall thrust. Read from the committed
reductions of both runs (validation/_labwf/: lab_post.json, wave_post.json, compare_lab_wave.json; spec labwf_spec.json,
every number there with its source; the CFD tools that made them are filed in _labwf/tools/*.txt and run from RDE/Nozzle):
  G-1  the A-REPR line: |C_F(lab, mean over the dumps after t_skip, inlet term at its period mean) / C_F(wave) - 1| below
       one third of the thrust-stand band;
  G-2  the walls alone (plug and cowl pushes) differ by less than a quarter of that line: the FRAME's share;
  G-3  the rest is the inlet table's time sampling: equal to the table-alone prediction within a quarter of the line;
  G-4  the lab thrust does not depend on time (a rigidly turning pattern): spread over the dumps under a quarter of the line;
  R-1  REJECTOR: the lab thrust moved by twice the line must fail G-1;
  R-2  REJECTOR: the lab walls moved by half the line must fail G-2.
usage: labwf_check.py"""
import json, os, sys
import numpy as np

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_labwf")
S = json.load(open(os.path.join(D, "labwf_spec.json")))
lab = json.load(open(os.path.join(D, S["files"]["lab"])))["dumps"]
wav = json.load(open(os.path.join(D, S["files"]["wave"])))["dumps"]
line = S["thrust_stand_band"] / 3
quarter = line / 4
late = [r for r in lab if r["t"] >= S["t_skip_s"]]
w = wav[-1]


def readings(cf_lab, walls_lab):
    cf_w = w["CF"]
    walls_w = -w["push_plug"] + w["push_cowl"]
    d_tot = float(np.mean(cf_lab)) / cf_w - 1.0
    d_walls = (float(np.mean(walls_lab)) - walls_w) / cf_w
    inlet_w = cf_w - walls_w
    pred = S["inlet_table"]["deficit_rel_inlet_term"][str(S["inlet_table"]["nt"])] * inlet_w / cf_w
    spread = (max(cf_lab) - min(cf_lab)) / float(np.mean(cf_lab))
    return d_tot, d_walls, pred, spread


cf_lab = [r["CF_inlet_mean"] for r in late]
walls_lab = [-r["push_plug"] + r["push_cowl"] for r in late]
d_tot, d_walls, pred, spread = readings(cf_lab, walls_lab)
gates = [
    ("G-1 the A-REPR line: lab %.6f vs wave %.6f, %+.4f percent (line %.3f percent)" % (np.mean(cf_lab), w["CF"], 100 * d_tot, 100 * line),
     abs(d_tot) < line),
    ("G-2 the walls alone: %+.4f percent of C_F (under %.4f)" % (100 * d_walls, 100 * quarter), abs(d_walls) < quarter),
    ("G-3 the rest %+.4f percent = the inlet table's sampling %+.4f percent (to %.4f)" % (100 * (d_tot - d_walls), 100 * pred, 100 * quarter),
     abs((d_tot - d_walls) - pred) < quarter),
    ("G-4 the lab thrust flat in time: spread %.2e over %d dumps (under %.2e)" % (spread, len(cf_lab), quarter), spread < quarter),
]
r1 = readings([c * (1 + 2 * line) for c in cf_lab], walls_lab)
r2 = readings(cf_lab, [x + line / 2 * w["CF"] for x in walls_lab])
gates += [("R-1 REJECTOR: the lab thrust moved by twice the line fails G-1 (%+.4f percent)" % (100 * r1[0]), not abs(r1[0]) < line),
          ("R-2 REJECTOR: the lab walls moved by half the line fail G-2 (%+.4f percent)" % (100 * r2[1]), not abs(r2[1]) < quarter)]
for txt, ok in gates:
    print("  [%s] %s" % ("PASS" if ok else "FAIL", txt))
n_ok = sum(ok for _, ok in gates)
print("VERDICT: %s (%d/%d)" % ("PASS" if n_ok == len(gates) else "FAIL", n_ok, len(gates)))
sys.exit(0 if n_ok == len(gates) else 1)
