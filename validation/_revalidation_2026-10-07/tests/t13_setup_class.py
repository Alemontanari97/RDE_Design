#!/usr/bin/env python3
"""T13 setup -- the production walker (a1_twowall.walk, the stage the production launch scripts run) needs a class
record OF ITS POSING (it refuses another posing's). For T08c's posing (the carrier on GENO's Migdal walls, vacuum) this
writes one with the production no-fold constants (_rde_tournament/stech/class_nofold_2026-09-28.json: floors, rho,
gap, m_ref -- the same constants T08c used with run_trsqp) and this posing's identity fields read from the carrier."""
import json
import os
import sys

RV = "/data10/falco/RDE/RDE_Design/validation/_revalidation_2026-10-07"
sys.path.insert(0, os.path.join(RV, "ref"))
import rv                                          # noqa: E402
os.environ.update(dict(TWOP_GAS=os.path.join(rv.OUT, "t08c_gas.json"), TWOP_ART=os.path.join(rv.OUT, "t13_art")))
import a1_twowall as T                             # noqa: E402

tw = T.TwoWall()
C = json.load(open("/data10/falco/RDE/RDE_Design/validation/_rde_tournament/stech/class_nofold_2026-09-28.json"))
rec = {k: C[k] for k in ("floors", "rho", "gap", "m_ref")}
rec.update(m=[len(tw.kp), len(tw.ks)], kernel=bool(tw.kernel), kmode=tw.kmode, K=tw.K, N=tw.N, shape=bool(tw.shape),
           noplume=bool(tw.noplume), geno_run=tw.geno_run,
           note="T13: the production no-fold constants of class_nofold_2026-09-28.json declared for T08c's posing")
json.dump(rec, open(os.path.join(rv.OUT, "t13_art", "class_t08c_posing.json"), "w"), indent=1)
print({k: rec[k] for k in ("m", "kernel", "kmode", "K", "N", "shape", "noplume", "geno_run")})
