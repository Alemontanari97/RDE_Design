#!/usr/bin/env python3
"""T07b -- the 12-phase objective of the production posing (T07's environment + TWOP_MU = the SDT family, 12 equal
weights) at a design where every phase's march is CERTIFIED (T07 found phases 10-11 uncertified at the posing's
reference W_ref; the carrier's generic cone start a1_twowall.cone_start is used here). Per phase: certificate,
class margin, C_F. Checks:
  P1 J_mu (record) = sum_k w_k C_F,k exactly (the carrier's _march_record_mu), weights summing to 1;
  P2 replay J_mu = record J_mu (relative 1e-10, T07's error model);
  P3 AD gradient of J_mu = central differences of the frozen J_mu replay along 2 random directions (T07's ladder);
  P4 the per-phase class margins and certificates, reported (the over-expanded phases fold, T07).
"""
import json
import os
import sys
import time

V = "/data10/falco/RDE/RDE_Design/validation"
F = V + "/_cycle_family/sdt_ch4_phi1_pcp20"
os.environ.update(dict(
    TWOP_KERNEL="arc", TWOP_CAP="0.8", TWOP_U0="10", TWOP_U0_S="-10", TWOP_FREE_EXIT="both",
    TWOP_GAS=F + "/gas_mean.json", TWOP_PA="0.024378", TWOP_SHAPE="1", TWOP_NOPLUME="1", TWOP_JET="1",
    TWOP_FIX='{"hs": 1.0, "xa_s": 0.0294, "ta_s": 1e-9, "u_s": -10.0, "ye_s": 1.0}',
    TWOP_SEP="summerfield", TWOP_SEP_CLASS="1", TWOP_REGION="RC", TWOP_MU=F + "/family_K12.json",
    TWOP_ART="/tmp/claude-1700/-data10-falco-MOSE/92599c7b-9637-4352-802d-d26f8eac9fd5/scratchpad/twop_art"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import a1_twowall as T                             # noqa: E402

R = rv.Report("t07b_phases")
Cr = json.load(open(V + "/_rde_tournament/stech/class_nofold_2026-09-28.json"))
mu0, rho, m_ref = Cr["floors"][0], Cr["rho"], Cr["m_ref"]
tw = T.TwoWall(verbose=False)
W0 = np.asarray(T.cone_start(tw), float)
t0 = time.time()
out, S = tw.march_record(W0, margin=tw.margin_dict(mu0=mu0, rho=rho, m_ref=m_ref))
R.note("cone start, 12 phases: record %.0f s; J_mu %.10f; worst cert %.3e; KS - mu0 %+.4f" % (
    time.time() - t0, out["J_mu"], out["cert_worst"], float(out["margin_ks"]) - mu0))
for k, (ph, o_k) in enumerate(zip(tw.phases, out["outs"])):
    R.note("  phase %2d: P0 %.3e Pa, w %.4f: C_F %.6f, cert %.3e at %s, KS - mu0 %+.4f, lip q %.1f / jet q %.1f" % (
        k, ph["P0"], ph["w"], out["J_phase"][k], float(o_k["cert_worst"]), o_k["cert_where"],
        float(o_k["margin_ks"]) - mu0, float(o_k["lip_q"][0]), float(o_k["lip_q"][1])))
wsum = sum(ph["w"] for ph in tw.phases)
R.check("P1 weights sum to 1", wsum - 1.0, 1e-14)
R.check("P1 J_mu = sum_k w_k C_F,k", out["J_mu"] - sum(ph["w"] * j for ph, j in zip(tw.phases, out["J_phase"])), 1e-14)
R.check("P4 every phase certified (prerequisite of P2-P3)", out["cert_worst"], 1.0)
fJ = lambda z: tw.J_replay(z, S)                     # noqa: E731
t1 = time.time()
Jr, g = jax.value_and_grad(fJ)(jnp.asarray(W0))
g = np.asarray(g)
R.note("replay value+grad %.0f s; |grad|_inf %.3e" % (time.time() - t1, float(np.max(np.abs(g)))))
R.check("P2 replay J_mu = record J_mu (relative)", float(Jr) / out["J_mu"] - 1.0, 1e-10)
rng = np.random.default_rng(7)
for k in range(2):
    dvec = rng.standard_normal(len(W0))
    dvec /= np.linalg.norm(dvec)
    vals = np.array([(float(fJ(jnp.asarray(W0 + h * dvec))) - float(fJ(jnp.asarray(W0 - h * dvec)))) / (2 * h)
                     for h in (1e-3, 1e-4, 1e-5, 1e-6)])
    fine = vals[1:]
    med, spread = float(np.median(fine)), float(fine.max() - fine.min())
    ad = float(g @ dvec)
    R.note("P3 random %d: AD %+.10e | FD %s | spread %.2e" % (k, ad, " ".join("%+.10e" % v for v in vals), spread))
    R.check("P3 AD = FD of the frozen J_mu along random %d (band: ladder spread, floor 1e-6 |AD|)" % k, ad - med,
            max(spread, 1e-6 * abs(ad)))
    if k == 0:
        # REJECTOR (R5): the same comparison with the AD derivative corrupted by 1e-3 relative
        R.reject("P3 AD = FD of the frozen J_mu along random 0, AD x(1 + 1e-3)", ad * (1.0 + 1e-3) - med,
                 max(spread, 1e-6 * abs(ad)))
sys.exit(R.save(dict(J_mu=out["J_mu"], J_phase=out["J_phase"], cert=[float(o["cert_worst"]) for o in out["outs"]],
                     ks=[float(o["margin_ks"]) - mu0 for o in out["outs"]], grad=g.tolist(), W=W0.tolist())))
