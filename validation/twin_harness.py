#!/usr/bin/env python3
"""F3.TWIN HARNESS (2026-10-05, protocol amendment A-INST in validation/TWIN_PROTOCOL_preregistration_2026-08-31.md).
Plain rules: a pair of designs (arm P = designed with the 12 phases, arm C = designed at the mean state) is ADMITTED only
if every check below passes; then both are read on the same tool, at the mean state and over the 12 phases of mu, and
delta = C_F,mu(P) / C_F,mu(C) - 1 is printed with each arm's certificate (A-1: quotable only if cert <= 1/K_RICH).
  R-TWIN-0/3  the instance: the content hashes pinned by A-INST (mu, the mean gas, the class, the wall basis, the start)
              and the two walks' settings identical except the objective (TWOP_MU / TWOP_MU_CLASS) and their folders;
  R-TWIN-1    the constraint vector: the held parts of the hardware (TWOP_FIX: the cowl's arc and end) and the lip
              identical to the last bit; REJECTOR: arm P's lip moved by twice the tolerance must be refused;
  R-TWIN-2    each arm IS its walk's landing: its objective replayed now equals the record's value (arm C at the mean
              state, arm P over mu) within the march's own epsilon (A1.EPS: the same code on the same tree replays to
              round-off); REJECTOR: a design moved on one knot by the walk's radius floor (TWOP_TR0 / K_RICH, the smallest
              step the walk itself measures) must be refused.
usage (env: RDE/handoff/plug_2026-09-29/sdt/sdt_env.sh 0.8 87 + the walks' TWOP_FIX, TWOP_CLASS, TWOP_SEP*, TWOP_REGION):
  twin_harness.py <arm P design.json> <arm C design.json> [--anchor <Rao design.json>] [--out <json>]"""
import argparse, glob, hashlib, json, os, re, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# a1_twowall / a1_toc_variational_jax are imported in main() AFTER the walks' settings are in the environment: the march
# modules read their switches at import (A1_NEWTON_RESCUE in a1_ideal_march_jax: imported first, the harness marched
# without the rescue the walks used and read a 12-phase certificate of 1e9 and a replay off by 2e-8, 2026-10-05)

V = os.path.dirname(os.path.abspath(__file__))
PINS = {                                                              # A-INST, md5[:8]
    "mu": ("_cycle_family/sdt_ch4_phi1_pcp20/family_K12.json", "a310b43d"),
    "gas_mean": ("_cycle_family/sdt_ch4_phi1_pcp20/gas_mean.json", "2ca9effc"),
    "class": ("_rde_tournament/stech/class_nofold_2026-09-28.json", "4e505fba"),
    "basis": ("_plug_contest/SDT/twin_inputs/basis_plug_only.json", "f0a01aed"),
    "start": ("_plug_contest/SDT/twin_inputs/start_rao_sdt.json", "a7997732"),
}
OBJECTIVE_KEYS = {"TWOP_MU", "TWOP_MU_CLASS"}                         # the only setting the arms may differ in
FOLDER_KEYS = {"TWOP_ART", "PSPL_WLOG"}


def md5(f):
    return hashlib.md5(open(f, "rb").read()).hexdigest()[:8]


def walk_env(design):
    """The walk's settings: the env line of its latest log (the line after the header)."""
    logs = sorted(glob.glob(os.path.join(design["walk"] if os.path.isabs(design["walk"]) else os.path.join(os.path.dirname(V), design["walk"]),
                                         "run_walk_*.log")))
    lines = open(logs[-1]).read().split("\n")
    env = {}
    for tok in re.split(r" (?=(?:TWOP|PSPL|A1)_[A-Z0-9_]*=)", " " + lines[1].strip()):   # values may hold spaces (TWOP_FIX's JSON)
        if "=" in tok:
            k, v = tok.strip().split("=", 1); env[k] = v.strip()
    return env, logs[-1]


def same_hardware(dp, dc, tol=0.0):
    """R-TWIN-1: the held hardware and the lip of both arms; returns the list of differences beyond tol."""
    bad = []
    for key in ("fix", "lip"):
        a_, b_ = dp.get(key, {}), dc.get(key, {})
        if set(a_) != set(b_):
            bad.append("%s keys %s != %s" % (key, sorted(a_), sorted(b_)))
            continue
        for k in a_:
            va, vb = np.asarray(a_[k], float), np.asarray(b_[k], float)
            if va.shape != vb.shape or np.any(np.abs(va - vb) > tol * np.maximum(np.abs(vb), 1.0)):
                bad.append("%s.%s %s != %s" % (key, k, va.tolist(), vb.tolist()))
    return bad


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("armP"); ap.add_argument("armC"); ap.add_argument("--anchor"); ap.add_argument("--out")
    a = ap.parse_args()
    t0 = time.time()
    dP, dC = json.load(open(a.armP)), json.load(open(a.armC))
    verdict, rows = [], {}

    def check(name, ok, info):
        verdict.append((name, bool(ok), info))
        print("  [%s] %s -- %s" % ("PASS" if ok else "FAIL", name, info), flush=True)

    # ---- R-TWIN-0/3: the instance
    hashes = {k: md5(os.path.join(V, p)) for k, (p, _) in PINS.items()}
    check("R-TWIN-0/3 instance hashes = A-INST", all(hashes[k] == PINS[k][1] for k in PINS), json.dumps(hashes))
    eP, lP = walk_env(dP); eC, lC = walk_env(dC)
    env_files = {"TWOP_GAS": "gas_mean", "TWOP_CLASS": "class", "TWOP_BASIS": "basis", "TWOP_START_FROM": "start"}
    fh = {k: (md5(eP[k]), md5(eC[k])) for k in env_files if k in eP and k in eC}
    check("R-TWIN-0 the walks read the pinned files", all(fh[k][0] == fh[k][1] == PINS[env_files[k]][1] for k in fh) and len(fh) == 4,
          json.dumps(fh))
    diff = sorted(k for k in set(eP) | set(eC) if eP.get(k) != eC.get(k) and k not in OBJECTIVE_KEYS | FOLDER_KEYS)
    check("R-TWIN-0 the walks' settings identical but the objective", not diff, "differing: %s; P objective %s, C objective %s"
          % (diff, {k: eP.get(k) for k in OBJECTIVE_KEYS}, {k: eC.get(k) for k in OBJECTIVE_KEYS}))
    check("R-TWIN-3 arm P on mu, arm C on the mean state", eP.get("TWOP_MU", "").endswith("family_K12.json") and "TWOP_MU" not in eC
          and md5(eP["TWOP_MU"]) == PINS["mu"][1], "P %s / C %s" % (eP.get("TWOP_MU"), eC.get("TWOP_MU")))
    # ---- R-TWIN-1: the constraint vector, and its rejector
    bad = same_hardware(dP, dC)
    check("R-TWIN-1 held hardware + lip identical", not bad, "; ".join(bad) or "fix %s, lip %s" % (dP["fix"], dP["lip"]))
    k0 = sorted(dP["lip"])[0]
    seeded = json.loads(json.dumps(dP))
    v0 = np.asarray(seeded["lip"][k0], float)
    tol = 4.0 * np.finfo(float).eps
    seeded["lip"][k0] = (v0 + 2.0 * tol * np.maximum(np.abs(v0), 1.0)).tolist()
    check("R-TWIN-1 REJECTOR: arm P's lip moved by 2 x tol is refused", bool(same_hardware(seeded, dC, tol)),
          "lip.%s moved by %.1e" % (k0, 2.0 * tol))
    # ---- the tool, both objectives, posed exactly as the walks (their env line minus the walk's own controls)
    WALK_ONLY = {"TWOP_STAGE", "TWOP_ITERS", "TWOP_SEGS", "TWOP_RESUME", "TWOP_START", "TWOP_START_FROM", "TWOP_TR0", "TWOP_BASIS",
                 "TWOP_ART", "TWOP_MU", "TWOP_MU_CLASS"}
    for k_, v_ in eC.items():
        if k_.startswith(("TWOP_", "A1_")) and k_ not in WALK_ONLY:
            os.environ[k_] = v_
    import a1_twowall as T_
    import a1_ideal_march_jax as A1                                 # K_RICH, EPS, as every carrier reads them
    REPLAY_TOL = A1.EPS
    DW_SEED = float(eC["TWOP_TR0"]) / A1.K_RICH
    Cr = json.load(open(os.environ["TWOP_CLASS"]))
    os.environ.pop("TWOP_MU", None); os.environ.pop("TWOP_MU_CLASS", None)
    tw0 = T_.TwoWall(verbose=False)
    os.environ["TWOP_MU"], os.environ["TWOP_MU_CLASS"] = os.path.join(V, PINS["mu"][0]), "ref"
    twm = T_.TwoWall(verbose=False)
    mgd = lambda t: t.margin_dict(mu0=Cr["floors"][0], rho=Cr["rho"], m_ref=Cr["m_ref"])    # noqa: E731

    def read(W):
        o0, _ = tw0.march_record(W, margin=mgd(tw0))
        om, _ = twm.march_record(W, margin=mgd(twm))
        return dict(J_mean=float(tw0.J_of(o0)), cert_mean=float(o0["cert_worst"]), ks_mean=float(o0["margin_ks"]),
                    J_mu=float(om["J_mu"]), cert_mu=float(om["cert_worst"]), J_phase=[float(v) for v in om["J_phase"]])
    items = [("P", dP, "J_mu"), ("C", dC, "J_mean")] + ([("anchor", json.load(open(a.anchor)), None)] if a.anchor else [])
    for name, d, obj in items:
        r = read(np.asarray(d["W"], float))
        rows[name] = r
        print("  arm %-6s C_F mean %.9f  C_F 12 phases %.9f  cert %.3e / %.3e  KS %+.4f" % (name, r["J_mean"], r["J_mu"], r["cert_mean"],
                                                                                       r["cert_mu"], r["ks_mean"]), flush=True)
        if obj is not None:
            rel = abs(r[obj] / float(d["J_walk"]) - 1.0)
            check("R-TWIN-2 arm %s replays its record (%s)" % (name, obj), rel <= REPLAY_TOL, "rel %.1e (tol %.0e)" % (rel, REPLAY_TOL))
    # R-TWIN-2 rejector: arm C's design with one knot moved, fed as arm C
    Ws = np.asarray(dC["W"], float).copy(); Ws[len(Ws) // 3] += DW_SEED
    rs = read(Ws)
    rel = abs(rs["J_mean"] / float(dC["J_walk"]) - 1.0)
    check("R-TWIN-2 REJECTOR: a design moved by %.1e (the walk's radius floor) on one knot is refused as arm C" % DW_SEED, rel > REPLAY_TOL, "rel %.1e" % rel)
    # ---- the reading
    kr = 1.0 / A1.K_RICH
    quot = {n: rows[n]["cert_mu"] <= kr and rows[n]["cert_mean"] <= kr for n in ("P", "C")}
    delta = rows["P"]["J_mu"] / rows["C"]["J_mu"] - 1.0
    admitted = all(ok for _, ok, _ in verdict)
    print("  delta (tool, over mu) = %+.4f %%; quotable (A-1, cert <= %.3f): P %s, C %s; pair %s"
          % (100 * delta, kr, quot["P"], quot["C"], "ADMITTED" if admitted else "REFUSED"), flush=True)
    if a.anchor:
        print("  against the anchor (Rao, mean state design) over mu: P %+.4f %%, C %+.4f %%"
              % (100 * (rows["P"]["J_mu"] / rows["anchor"]["J_mu"] - 1), 100 * (rows["C"]["J_mu"] / rows["anchor"]["J_mu"] - 1)))
    res = dict(armP=a.armP, armC=a.armC, anchor=a.anchor, rung=dict(K=tw0.K, N=tw0.N), hashes=hashes, rows=rows, delta_tool_mu=delta,
               quotable=quot, admitted=admitted, checks=[dict(name=n, ok=o, info=i) for n, o, i in verdict], seconds=time.time() - t0)
    if a.out:
        json.dump(res, open(a.out, "w"), indent=1)
    print("VERDICT: %s (%d/%d checks, %.0f s)" % ("PASS" if admitted else "FAIL", sum(o for _, o, _ in verdict), len(verdict), time.time() - t0))
    sys.exit(0 if admitted else 1)


if __name__ == "__main__":
    main()
