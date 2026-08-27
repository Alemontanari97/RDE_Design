"""[F2a] O3.1 ON THE STRATIFIED MARCH — is the gradient through a
rotational (per-streamline s, h0) march the adjoint of that march?

WHY THIS, AND WHY BEFORE ANY OPTIMIZATION. S25 closed W-5: the
stratified forward march is certified (a1_rot_march 9/9). The
GRADIENT through it is not. The S24 handoff carries it as open queue
item 9 -- "adjoint through stratified marches (should work -- same
implicit-solver machinery -- unverified)". An optimizer walking on an
unverified derivative is the failure this program has already paid for
twice (S21's missing acceptance test; S23's no-motion wedge), so the
derivative is measured FIRST and the optimization waits on it.

WHAT IS ACTUALLY IN DOUBT. The homentropic march's adjoint is
certified ([X-A1IM] O3.1, whole-march). The stratified march adds
three things that the certified path never exercised: a FIFTH cell
unknown (the streamline-foot parameter t), a transported pair (s, h0)
carried per node, and -- as of S25 -- a CLAMP, clip(t, 0, 1), inside
the residual and matched in the storage. A clamp is not differentiable
at its corner: where a foot sits exactly at t = 0 or t = 1 the
derivative of the transported pair with respect to the design is ZERO
on one side and non-zero on the other. The measured design has 20 feet
outside their chord, so the clamp IS active there, and the question
this carrier answers is whether the resulting derivative is still the
adjoint of the function the march computes.

THE TEST (the [X-A1IM] S6 pattern, verbatim in structure): pick a
direction v in design space and a covector w on the outputs; compare

    <w, J v>   by CENTERED FINITE DIFFERENCES at two step sizes
    <J^T w, v> by ONE REVERSE SWEEP

against a tolerance DERIVED from the finite-difference scheme's own
two-step disagreement plus the round-off floor -- never a magic
number.

PRE-REGISTERED PREDICTIONS (R5, declared before the first run):
  P1  replay reproduces the primal march to the Newton floor (if this
      fails, nothing downstream means anything);
  P2  |<w,Jv> - <J^T w,v>| <= the derived tolerance -- the reverse
      sweep IS the adjoint of the stratified march;
  P3  the probe replays stay certified (an uncertified probe would be
      measuring a march nobody would trust).
FALSIFIERS:
  N1  a deliberately corrupted vjp must BREAK the identity, else the
      test has no power;
  N2  if P2 fails while P1 passes, the clamp corner is the prime
      suspect and the honest report is "the stratified adjoint is not
      the adjoint where the clamp is active" -- which would BLOCK
      optimization on stratified inlets rather than merely annoy it.

ON-DEMAND CARRIER (env: jax).
"""
import os
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import a1_ideal_march_jax as A1                       # noqa: E402
import a1_config_compare as CC                        # noqa: E402
import a1_plug_spline_opt as PS                       # noqa: E402
import a1_rot_march as R                              # noqa: E402

K_RICH = A1.K_RICH
EPS = A1.EPS
C_FLOOR = A1.C_FLOOR


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def main():
    print("== [F2a] O3.1 on the STRATIFIED march (jax %s) =="
          % jax.__version__)
    ok = True

    w = CC.build_world()
    taw = A1.tab_arrays(w["tab"])
    _, _, _, _, _, h0w, s0w = taw
    c = PS.build_case(w)
    W0 = np.asarray(c["W0"], dtype=float)
    K = 41

    x0w, yl, us, vs = c["start"]
    yl = np.asarray(yl, dtype=float)
    zz = (yl - yl[0]) / (yl[-1] - yl[0])
    # the SAME stratified inlet as W-4/W-5 of record
    s_r = float(s0w) + 25.0 * np.sin(np.pi * zz)
    h_r = float(h0w) * (1.0 + 0.03 * np.sin(np.pi * zz))
    s6s = (x0w, yl, us, vs, s_r, h_r)

    def stations(Wv):
        xq, yq, sq = PS.wall_stations(jnp.asarray(Wv), c, K=K)
        return (xq, yq, sq)

    # ---- record once; every evaluation below REPLAYS this schedule
    t0 = time.perf_counter()
    out0, sched = R.rot_march(stations(W0), s6s, CC.PA, w["tab"], 1.0)
    print("  record: %d cells, cert worst %.3e, %.1f s"
          % (int(out0["cert_n"]), float(out0["cert_worst"]),
             time.perf_counter() - t0))
    ok &= check("the recorded stratified march is certified",
                float(out0["cert_worst"]) <= 1.0)
    nclamp = int(out0.get("foot_clamped_n", -1))
    print("  feet outside their chord in this record: %d "
          "(the clamp corner is %s on this design)"
          % (nclamp, "ACTIVE" if nclamp > 0 else "INACTIVE"))

    # mesh_pts is deliberately None in replay (stacking it is an XLA
    # compile with K*N operands -- the S23 seven-hour wedge). The
    # TRACED outputs are wall / edge / last_col, so the probe reads the
    # WALL, which is also the surface the objective integrates over.
    wall0 = np.asarray(out0["wall"])
    n_out = 8
    idx = np.linspace(0, wall0.shape[0] - 1, n_out).astype(int)

    def f(Wv):
        o, _ = R.rot_march(stations(Wv), s6s, CC.PA, w["tab"], 1.0,
                           sched=sched)
        m = o["wall"]
        return jnp.concatenate([m[idx, 0], m[idx, 1]])

    base = f(jnp.asarray(W0))
    prim = jnp.concatenate([jnp.asarray(wall0[idx, 0]),
                            jnp.asarray(wall0[idx, 1])])
    rep = float(jnp.max(jnp.abs(base - prim)))
    print("  [replay fidelity] max|replay - primal| = %.3e" % rep)
    ok &= check("P1 replay reproduces the primal stratified march",
                rep <= A1.NEWTON_TOL_FACTOR * EPS
                * float(jnp.max(jnp.abs(base))) * 10.0)

    rng = np.random.default_rng(0)
    v = jnp.asarray(rng.normal(size=W0.size) * 1e-3)
    wv = jnp.asarray([((-1.0) ** k) * (0.3 + 0.07 * k)
                      for k in range(2 * n_out)])

    def dirder(hsc):
        h = EPS ** (1.0 / 3.0) * hsc
        return (f(jnp.asarray(W0) + h * v)
                - f(jnp.asarray(W0) - h * v)) / (2.0 * h)

    dv_h, dv_h2 = dirder(1.0), dirder(0.5)
    lhs = float(wv @ dv_h2)
    _, vjp_fn = jax.vjp(f, jnp.asarray(W0))
    (JTw,) = vjp_fn(wv)
    rhs = float(JTw @ v)
    tol = K_RICH * (abs(float(wv @ (dv_h - dv_h2)))
                    + C_FLOOR * EPS ** (2.0 / 3.0)
                    * float(jnp.max(jnp.abs(base))))
    err = abs(lhs - rhs)
    print("  [O3.1] <w,Jv> = %.10e  <J^T w,v> = %.10e"
          "  |diff| = %.3e (tol %.3e)" % (lhs, rhs, err, tol))
    ok &= check("P2 O3.1 dot-product on the STRATIFIED march",
                err <= tol)

    # NEGATIVE CONTROL, and a POWER statement instead of a copied one.
    # The first version of this control was transplanted verbatim from
    # [X-A1IM], where the quantities are of order 1e+05; here
    # <J^T w, v> ~ 1e-03, and its additive and multiplicative terms
    # partially CANCEL against this v, so the corruption landed inside
    # the tolerance and the control proved nothing. It was REFUTED BY
    # ITS OWN FIRING -- the S24 trap of record ("a rejector world must
    # carry load") and the control-re-derivation lesson, now on its
    # fourth instance across the two lines.
    #
    # Replaced by two statements that do not depend on the world's
    # scale. (a) the test's DETECTION FLOOR, reported: the smallest
    # relative adjoint error this instance can resolve is tol/|rhs|.
    # (b) a control at a FIXED, physically meaningful size (1e-3
    # relative -- an error anyone would care about), applied purely
    # multiplicatively so nothing can cancel. The floor is derived; the
    # control is NOT tuned to the tolerance.
    floor_rel = tol / max(abs(rhs), 1e-300)
    agree_rel = err / max(abs(rhs), 1e-300)
    print("  [power] detection floor %.3e relative; measured "
          "agreement %.3e relative (%.0fx inside)"
          % (floor_rel, agree_rel, floor_rel / max(agree_rel, 1e-300)))
    rhs_c = rhs * (1.0 + 1e-3)
    ok &= check("N1 negative control: a 1e-3 relative adjoint error "
                "is rejected", abs(lhs - rhs_c) > tol)
    ok &= check("N1b the control is above the detection floor "
                "(the test can see it at all)", 1e-3 > floor_rel)

    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
