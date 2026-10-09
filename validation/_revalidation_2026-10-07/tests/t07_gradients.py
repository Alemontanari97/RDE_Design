#!/usr/bin/env python3
"""T07 -- the derivatives the SQP walks on, in the PRODUCTION posing (the SDT methane case of
handoff/plug_2026-09-29/sdt/sdt_env.sh on plug_env.sh 0.8 87: arc kernel, length cap 0.8, cowl frozen straight,
exit heights free, lip jet, ambient 0.024378 P0, Summerfield closure in J and in the class, class read in region RC,
shape-mode cell margin, plume excluded), single inflow state (the cycle-mean gas) and the 12 phases.

What the walk uses: J and the class margin are REPLAYED on the schedule frozen at the segment's record (the discrete
decisions of the march kept), and their gradients come from reverse-mode AD through the implicit cells (custom_vjp,
implicit-function rule). The walk then ACCEPTS a step on a fresh record (decisions re-taken).

Checks:
  D1 replay = record at the recording point (J and margin). Error model: the replay re-solves every cell from the
     recorded root and stops when one Newton step is below 100 eps |z| (the certification bound), so each cell moves
     by <= 100 eps |z|; J moves by that times its sensitivity: tolerance 1e-10 relative (a sum over 1e4 cells of
     2e-14 relative moves, with unit sensitivity).
  D2 the wavefront replay (production) = the sequential replay, value and gradient (same equations, batched):
     the same 1e-10 relative (value), 1e-8 relative (gradient: the transposed solves amplify by the cells' condition).
  D3 AD gradient = central differences of the FROZEN replay along 4 random unit directions and 6 coordinates, on a
     ladder h = 1e-3 .. 1e-6 (design units): the frozen replay is smooth, so the FD error is truncation (h^2) +
     noise (delta_J / h); the band is the ladder's own spread over its 3 finest steps, and the check is
     |AD - FD_median| <= max(spread, 1e-6 |AD|).
  D4 the frozen model against the TRUE objective (re-recorded marches, decisions re-taken): the jump
     J_record(W + h v) - J_replay(W + h v; frozen) is the resolution of the functional; reported, and the check is
     that the true directional derivative at the largest h agrees in SIGN with AD along +grad (the walk's direction
     must be an ascent of the true objective).
  D5 the class margin's AD gradient = central differences of the frozen margin replay (as D3, 2 random directions).
  D6 phases: J_mu = sum_k w_k C_F,k with sum w_k = 1; AD of J_mu = central differences of the frozen J_mu (2 random
     directions).
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
    TWOP_SEP="summerfield", TWOP_SEP_CLASS="1", TWOP_REGION="RC",
    TWOP_ART="/tmp/claude-1700/-data10-falco-MOSE/92599c7b-9637-4352-802d-d26f8eac9fd5/scratchpad/twop_art"))
os.makedirs(os.environ["TWOP_ART"], exist_ok=True)
CLASS = V + "/_rde_tournament/stech/class_nofold_2026-09-28.json"     # TWOP_CLASS of sdt_env.sh: mu0, rho, m_ref

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import jax                                         # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import a1_twowall as T                             # noqa: E402

R = rv.Report("t07_gradients")
Cr = json.load(open(CLASS))
mu0, rho, m_ref = Cr["floors"][0], Cr["rho"], Cr["m_ref"]
rng = np.random.default_rng(7)
LADDER = [1e-3, 1e-4, 1e-5, 1e-6]


def fd(f, W, v, hs):
    return np.array([(float(f(jnp.asarray(W + h * v))) - float(f(jnp.asarray(W - h * v)))) / (2.0 * h) for h in hs])


def grade(label, ad, vals, reject=False):
    fine = vals[1:]
    med, spread = float(np.median(fine)), float(fine.max() - fine.min())
    tol = max(spread, 1e-6 * abs(ad))
    R.note("%s: AD %+.10e | FD ladder %s | spread %.2e" % (label, ad, " ".join("%+.10e" % v for v in vals), spread))
    ok = R.check(label + ": |AD - FD| (band: ladder spread, floor 1e-6 |AD|)", ad - med, tol)
    if reject:
        # REJECTOR (R5): the same comparison with the AD derivative corrupted by 1e-3 relative
        R.reject(label + ": |AD - FD| with AD x(1 + 1e-3)", ad * (1.0 + 1e-3) - med, tol)
    return ok


def run_state(tw, tag, mu=False):
    t0 = time.time()
    W0 = np.asarray(tw.W_ref, float)
    mg = tw.margin_dict(mu0=mu0, rho=rho, m_ref=m_ref)
    out0, S0 = tw.march_record(W0, margin=mg)
    J_rec = float(tw.J_of(out0))
    R.note("%s: n = %d design components; record %.1f s; J %.10f; cert %.3e; KS - mu0 %+.4e; cells %d"
           % (tag, len(W0), time.time() - t0, J_rec, float(out0["cert_worst"]), float(out0["margin_ks"]) - mu0,
              int(out0.get("cert_n", 0))))
    fJ = lambda z: tw.J_replay(z, S0)                                       # noqa: E731
    t1 = time.time()
    J_rep, g = jax.value_and_grad(fJ)(jnp.asarray(W0))
    g = np.asarray(g)
    R.note("%s: replay value+grad %.1f s (first call, compile included); |grad|_inf %.3e" % (tag, time.time() - t1,
                                                                                         np.max(np.abs(g))))
    R.check("%s D1 replay J = record J (relative)" % tag, float(J_rep) / J_rec - 1.0, 1e-10)
    mgr = tw.margin_dict(mu0=mu0, rho=rho, m_ref=m_ref)
    fm = lambda z: tw.margin_replay(z, S0, mgr)                             # noqa: E731
    m_rep, gm = jax.value_and_grad(fm)(jnp.asarray(W0))
    gm = np.asarray(gm)
    R.check("%s D1 replay margin = record margin (absolute, margin units)" % tag,
            float(m_rep) - (float(out0["margin_ks"]) - mu0), 1e-10)
    res = dict(J=J_rec, grad=g.tolist(), margin=float(m_rep), grad_m=gm.tolist())
    if not mu:
        # D2: sequential replay
        t2 = time.time()
        Js, gs = jax.value_and_grad(lambda z: tw.J_replay(z, S0, wavefront=False))(jnp.asarray(W0))
        gs = np.asarray(gs)
        R.note("%s: sequential replay value+grad %.1f s" % (tag, time.time() - t2))
        R.check("%s D2 wavefront J = sequential J (relative)" % tag, float(J_rep) / float(Js) - 1.0, 1e-10)
        R.check("%s D2 wavefront grad = sequential grad (max rel to |grad|_inf)" % tag,
                float(np.max(np.abs(g - gs)) / np.max(np.abs(gs))), 1e-8)
    # D3 / D6: AD vs FD on the frozen replay
    dirs = [rng.standard_normal(len(W0)) for _ in range(4 if not mu else 2)]
    dirs = [d / np.linalg.norm(d) for d in dirs]
    labels = ["random %d" % k for k in range(len(dirs))]
    if not mu:
        for i in [0, tw.np_ // 2] + [len(W0) - k for k in (6, 5, 2, 1)]:
            e = np.zeros(len(W0)); e[i] = 1.0
            dirs.append(e); labels.append("component %d" % i)
    for d, lab in zip(dirs, labels):
        grade("%s %s J along %s" % (tag, "D6" if mu else "D3", lab), float(g @ d), fd(fJ, W0, d, LADDER),
              reject=(lab == "random 0" and not mu))
    # D5: the class margin
    if not mu:
        for k in range(2):
            d = dirs[k]
            grade("%s D5 margin along %s" % (tag, labels[k]), float(gm @ d), fd(fm, W0, d, LADDER))
    # D4: the frozen model against the re-recorded objective along +grad
    if not mu:
        u = g / np.linalg.norm(g)
        rows = []
        for h in (1e-3, 1e-4, 1e-5):
            Jp = float(tw.J_of(tw.march_record(W0 + h * u, margin=dict(mg))[0]))
            Jm = float(tw.J_of(tw.march_record(W0 - h * u, margin=dict(mg))[0]))
            Jpf, Jmf = float(fJ(jnp.asarray(W0 + h * u))), float(fJ(jnp.asarray(W0 - h * u)))
            rows.append((h, (Jp - Jm) / (2 * h), Jp - Jpf, Jm - Jmf))
            R.note("%s D4 h %.0e: true directional derivative %+.6e (AD %+.6e); record - frozen replay at +h %+.3e, "
                   "-h %+.3e" % (tag, h, rows[-1][1], float(g @ u), rows[-1][2], rows[-1][3]))
        R.check("%s D4 the true objective ascends along +grad at h 1e-3 (sign of the true derivative)" % tag,
                rows[0][1], None, ok=rows[0][1] > 0.0)
        res["D4"] = rows
    return res


tw = T.TwoWall()
out = dict(single=run_state(tw, "mean state"))
# the 12 phases on the same walls
os.environ["TWOP_MU"] = F + "/family_K12.json"
twm = T.TwoWall(verbose=False)
wsum = sum(ph["w"] for ph in twm.phases)
R.check("D6 phase weights sum to 1", wsum - 1.0, 1e-14)
out["phases"] = run_state(twm, "12 phases", mu=True)
sys.exit(R.save(out))
