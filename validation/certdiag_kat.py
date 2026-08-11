"""[X-CDKAT] certdiag KNOWN-ANSWER TEST + S20 retro-validation
(S21, F0 of plan v3 — audit seed A1, P0).

WHAT THIS CLOSES (audit AUDIT_agnostic_2026-08-07, SEED-A1 verifier
note): the S20 certdiag adjudication ("8/8 GENUINE — every rejected
design re-recorded with N_NEWTON 30 -> 300 and the floor untouched
returned a BIT-IDENTICAL cert_worst") rested on an instrument whose
discriminating power was UNPROVEN: bit-identical output under a
RAISED cap is exactly what a NON-BITING knob would also produce, and
no executable test varied N_NEWTON anywhere in the repo. This KAT
proves (or refutes) the knob through the SAME binding chain the S20
certdiag used (module global A1.N_NEWTON read at trace time, fresh
solver-cache key so no stale closure can serve).

VERDICT SEMANTICS (pre-declared in the S21 gate, [D1-KAT], BEFORE
any number below existed):
  KAT-1 (bite, lowered cap): re-recording the HEALTHY baseline design
        with N_NEWTON = 3 MUST strictly worsen cert_worst (or refuse
        outright — a raise counts as the extreme worsening). If
        cert_worst is UNCHANGED, the instrument is demonstrated
        non-discriminating and the S20 8/8 GENUINE adjudication is
        DOWNGRADED of record (trip-cap hypothesis back to
        unresolved) — that outcome is a valid verdict of this
        carrier, exit 1.
  KAT-2 (invariance, raised cap): re-recording the same healthy
        design with N_NEWTON = 300 (the S20 certdiag setting) must
        reproduce cert_worst BIT-IDENTICALLY — a record whose cells
        all converge before the cap is invariant under raising it.
  KAT-3 (replay diagnostic fires, C2-F2): the cert_diag jit replay
        must certify the base point (worst <= 1) and must FIRE
        (worst > 1) when replaying a perturbed design under a solver
        starved to ZERO Newton trips (the replay then returns the
        stale recorded seeds verbatim — a diagnostic that reads
        anything but the actual solved state stays quiet). ATTEMPT 1
        DECLARED (S21 log): the first stimulus (cap 2, 1% wall
        perturbation) did NOT create an uncertifiable replay —
        two-trip Newton reached the floor from the stale seeds
        (measured worst 2.125e-01, bit-equal across caps 2 and 30;
        the max cell is a fan cell, W-independent) — an insufficient
        STIMULUS, not a band move: the check and its bound are
        unchanged, the starvation is hardened to cap 0.
  N-CTRL (determinism): a final re-record at the restored default
        cap must reproduce the baseline cert_worst bit-identically.

RETRO-VALIDATION LOGIC (what PASS licenses, no more): KAT-1 + KAT-2
prove the N_NEWTON knob bites through the exact S20 binding chain and
is invariant only on converged cells. Therefore the S20 bit-identity
under 30 -> 300 on the five REJECTED designs cannot have been a
non-biting-knob artifact: those cells were genuinely stalled (the
frozen damped-Newton signature), and the "trip-cap hypothesis DEAD"
adjudication stands RETRO-VALIDATED. This carrier does NOT re-run
the S20 rejected designs themselves (they were transient in S20; the
driver now persists rejections — T5 — so future adjudications carry
their designs).

TOLERANCES — DERIVED (R5): the only numeric gates are strict
inequality (KAT-1), bit-identity (KAT-2, N-CTRL: == on the float),
and the certification bound itself (KAT-3: worst vs 1.0, the
record-path bound NEWTON_TOL_FACTOR * eps * scale of record). The
KAT-3 perturbation is 1% of the local wall ordinate on the interior
nodes — the S18 OPT-seed amplitude of record, reused, not tuned.

On-demand carrier (env: jax + the cached GENO type-2 scratch case for
the W0 seed — the same seed path as [X-TOCV]).
"""
import os
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1   # noqa: E402
import a1_march_scan as SC        # noqa: E402
import thermotab_c1_jax as TH     # noqa: E402
import a1_toc_variational_jax as TV  # noqa: E402

EPS = float(jnp.finfo(jnp.float64).eps)


def check(label, cond):
    print("  [%s] %s" % ("PASS" if cond else "FAIL", label))
    return bool(cond)


def record_with_cap(W, tab, cfg, state_fn, cap, key):
    """Re-record a design with A1.N_NEWTON = cap under a FRESH solver
    cache key (the S20 certdiag binding chain, verbatim: the module
    global is read at trace time inside the jitted while_loop cond,
    and the fresh key forces new closures so the new value is baked
    in). The floor (NEWTON_TOL_FACTOR * eps * scale) is UNTOUCHED."""
    n_old = A1.N_NEWTON
    try:
        A1.N_NEWTON = cap
        solv = SC.cached_solvers((key, 1.0), state_fn, 1.0)
        out, plan = TV.run_toc_record(W, tab, cfg, state_fn=state_fn,
                                     solvers=solv)
        return out, plan, solv
    finally:
        A1.N_NEWTON = n_old


def main():
    print("== [X-CDKAT] certdiag KAT + S20 retro-validation "
          "(JAX %s) ==" % jax.__version__)
    ok = True
    tab = A1.prep_tab(A1.build_tab_nasa())
    cfg = dict(NI=TV.TCASE["NI"], Nw=TV.NW, da_deg=TV.TCASE["da_deg"],
               yt=TV.TCASE["yt"], rtu=TV.TCASE["rtu"],
               rtd=TV.TCASE["rtd"], xtronc=TV.TCASE["xtronc"])
    c1 = TH.build_c1(tab)

    def state_c1(q, ta_ignored):
        return TH.state_q_c1(q, c1)

    # W0 = the GENO-seeded feasible baseline of [X-TOCV] (healthy by
    # the S18/S19/S20 records: cert_worst < 1 at every session)
    yL = TV.TCASE["yt"] * np.sqrt(TV.TCASE["eps"])
    Lx = TV.TCASE["xtronc"]
    scratch2 = os.path.join(os.environ.get("TEMP", "/tmp"),
                            "a1_geno_toc_ni21")
    gwx, gwy = TV.geno_type2_reference(scratch2)
    xg = np.linspace(0.05, 1.2, 400)
    sg = np.gradient(np.interp(xg, gwx, gwy), xg)
    thB0 = float(np.arctan(np.max(sg)))
    xB0 = TV.TCASE["rtd"] * np.sin(thB0)
    xsn = xB0 + (Lx - xB0) * np.arange(1, TV.M_NODES + 1) / TV.M_NODES
    y0 = np.interp(xsn, gwx, gwy)
    y0[-1] = yL
    W0 = np.concatenate([[thB0], y0])

    # ---------------- baseline record at the default cap
    t0 = time.perf_counter()
    out30, plan30, solv30 = record_with_cap(
        W0, tab, cfg, state_c1, 30, "cdkat_30")
    w30 = float(out30["cert_worst"])
    print("-- baseline record: N_NEWTON = 30, cert_worst = %.6e "
          "(%d cells, %.1f s) --"
          % (w30, out30["cert_n"], time.perf_counter() - t0))
    ok &= check("baseline design is HEALTHY (cert_worst <= 1; the "
                "KAT precondition)", w30 <= 1.0)

    # ---------------- KAT-1: lowered cap MUST worsen
    print("-- KAT-1: N_NEWTON = 3 on the healthy design --")
    try:
        out3, _, _ = record_with_cap(W0, tab, cfg, state_c1, 3,
                                     "cdkat_3")
        w3 = float(out3["cert_worst"])
        print("  cert_worst: %.6e -> %.6e (x%.3e)"
              % (w30, w3, w3 / max(w30, EPS)))
        kat1 = w3 > w30
        ok &= check("KAT-1: lowered cap STRICTLY worsens cert_worst "
                    "(the knob bites)", kat1)
        print("  (informational: starved record uncertifiable = %s)"
              % (w3 > 1.0))
    except RuntimeError as e:
        # a refusal under the starved cap (margin rejector / wall
        # search on garbage states) is the extreme form of worsening
        print("  starved record REFUSES: %s" % e)
        kat1 = True
        ok &= check("KAT-1: lowered cap worsens (refusal branch)",
                    True)

    # ---------------- KAT-2: raised cap must be bit-identical
    print("-- KAT-2: N_NEWTON = 300 (the S20 certdiag setting) --")
    out300, _, _ = record_with_cap(W0, tab, cfg, state_c1, 300,
                                   "cdkat_300")
    w300 = float(out300["cert_worst"])
    print("  cert_worst: %.17e vs %.17e" % (w30, w300))
    kat2 = (w300 == w30)
    ok &= check("KAT-2: raised cap BIT-IDENTICAL on converged cells",
                kat2)

    # ---------------- KAT-3: the C2-F2 replay diagnostic can fire
    print("-- KAT-3: cert_diag jit replay (C2-F2 rejector) --")
    runj_d = TV.make_run_toc_scan_jit(tab, cfg, plan30,
                                      state_fn=state_c1,
                                      solvers=solv30, cert_diag=True)
    _, worst_base = runj_d(jnp.asarray(W0))
    worst_base = float(worst_base)
    print("  base-point replay worst step/bound = %.3e" % worst_base)
    ok &= check("KAT-3a: base-point replay certified (worst <= 1)",
                worst_base <= 1.0)
    # perturbed design, solver starved to ZERO trips: the replay
    # returns the stale recorded seeds verbatim -> the diagnostic
    # must read the staleness and FIRE
    rng = np.random.default_rng(7)
    Wp = W0.copy()
    bump = 0.01 * y0[:-1] * np.sin(
        np.pi * (xsn[:-1] - xB0) / (Lx - xB0))
    Wp[1:-1] = Wp[1:-1] + bump * rng.standard_normal(1)[0]
    n_old = A1.N_NEWTON
    try:
        A1.N_NEWTON = 0
        solv0 = SC.cached_solvers(("cdkat_replay_0", 1.0), state_c1,
                                  1.0)
        runj_0 = TV.make_run_toc_scan_jit(tab, cfg, plan30,
                                          state_fn=state_c1,
                                          solvers=solv0,
                                          cert_diag=True)
        _, worst_p0 = runj_0(jnp.asarray(Wp))
        worst_p0 = float(worst_p0)
    finally:
        A1.N_NEWTON = n_old
    print("  perturbed replay, cap 0 (stale seeds verbatim): worst "
          "step/bound = %.3e" % worst_p0)
    ok &= check("KAT-3b: starved perturbed replay FIRES (worst > 1) "
                "— the replay rejector can reject", worst_p0 > 1.0)
    # negative control: same perturbed replay at the default cap
    _, worst_p30 = runj_d(jnp.asarray(Wp))
    worst_p30 = float(worst_p30)
    print("  perturbed replay, cap 30: worst step/bound = %.3e"
          % worst_p30)
    ok &= check("KAT-3c: same replay certifies at the default cap "
                "(the firing is the CAP, not the perturbation)",
                worst_p30 <= 1.0)

    # ---------------- N-CTRL: determinism at the restored default
    out30b, _, _ = record_with_cap(W0, tab, cfg, state_c1, 30,
                                   "cdkat_30b")
    ok &= check("N-CTRL: default-cap re-record bit-identical "
                "(deterministic instrument)",
                float(out30b["cert_worst"]) == w30)

    # ---------------- retro-validation verdict (pre-declared)
    if kat1 and kat2:
        print("RETRO-VALIDATION: the N_NEWTON knob BITES through the "
              "S20 binding chain (KAT-1) and is invariant only on "
              "converged cells (KAT-2) => the S20 8/8 GENUINE "
              "bit-identity under 30 -> 300 cannot be a "
              "non-biting-knob artifact: the 'trip-cap hypothesis "
              "DEAD' adjudication stands RETRO-VALIDATED.")
    else:
        print("RETRO-VALIDATION FAILED: instrument non-discriminating "
              "— per the S21 gate [D1-KAT] the S20 8/8 GENUINE "
              "adjudication is DOWNGRADED (trip-cap hypothesis "
              "unresolved) until the instrument is repaired.")
    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
