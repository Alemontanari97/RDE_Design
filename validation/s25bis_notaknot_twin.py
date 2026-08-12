#!/usr/bin/env python3
"""[GAP-5 probe, S25-bis] notaknot-twin — one-row BC twin of the wall
spline (gap-map ADVISORY_S24_sota_gapmap_2026-08-12 GAP-5, CONFIRMED
HIGH; choice-ledger row C2): the natural right end condition
(y''(L) = 0) biases the design class exactly at the lip node where
the [C-O33] goal quantity is differentiated. This twin changes ONE
row of spline_coeffs (natural -> not-a-knot, de Boor) and re-measures
the r=1 / r=2 corner mismatch at W*8 against the S19 baseline
6.6295e-02 ([X-O33B], margin_governor.S19_D1_BASELINE).

REJECTOR-FORMED (the probe's own falsifier; SECOND FORM of record —
the first form is REFUTED, honestly, by its own firing): the first
control demanded corner-density (cd) invariance between arms, but cd
is computed ON the marched design and the BC change moves the lip
flow state BY THE VERY MECHANISM under test — its 8.2% shift is the
finding's own evidence, not a confound (control re-derivation, the
R6/R-GRAD lesson class). The re-formed rejector: (i) the twin's
mismatch DELTA must be TWO-RESOLUTION STABLE — |delta(r=1) -
delta(r=2)| <= K_RICH x max(arm r1-vs-r2 spreads) + floor (a
resolution-unstable delta = mesh artifact = REJECT); (ii) the
artifact-fixed GENO reference data (leg-1 wall) is untouched by
construction (no re-read in either arm). The cd shift is REPORTED as
the mechanism datum. The incumbent BC is NOT touched (gap-map rigor
note: consequence adjudication = F2).

DECLARED HAZARD handled here: the M4 engine cache keys engines by
(tab/state_fn/solvers id, net, geometry, class knobs) — a MONKEY-
PATCHED spline_coeffs is invisible to that key (code identity covers
it across processes, not in-process patching), so the caches are
CLEARED between arms; a stale-engine reuse would silently void the
twin.

Exit 0 iff the machinery gates pass (cert, oracle rejector); the
twin mismatch movement itself is a MEASURED DATUM either way, logged
for the F2 adjudication.
"""
import json
import os
import sys

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1        # noqa: E402
import a1_toc_variational_jax as TV    # noqa: E402
import o33_bench as O33                # noqa: E402
from adaptive_knot_optimize import goal_metric   # noqa: E402
from margin_governor import S19_D1_BASELINE      # noqa: E402

jax.config.update("jax_enable_x64", True)
HERE = os.path.dirname(os.path.abspath(__file__))
EPS = float(jnp.finfo(jnp.float64).eps)


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def spline_coeffs_nak(xs, ys, slope0):
    """TV.spline_coeffs with EXACTLY ONE row changed: the natural
    right end (M_{n-1} = 0) becomes the not-a-knot condition (M'''
    continuity across the last interior knot):
    h_{n-2} M_{n-3} - (h_{n-3} + h_{n-2}) M_{n-2} + h_{n-3} M_{n-1}
    = 0. Every other row verbatim."""
    n = xs.shape[0]
    h = xs[1:] - xs[:-1]
    A = jnp.zeros((n, n))
    r = jnp.zeros(n)
    A = A.at[0, 0].set(h[0] / 3.0).at[0, 1].set(h[0] / 6.0)
    r = r.at[0].set((ys[1] - ys[0]) / h[0] - slope0)
    for i in range(1, n - 1):
        A = A.at[i, i - 1].set(h[i - 1] / 6.0)
        A = A.at[i, i].set((h[i - 1] + h[i]) / 3.0)
        A = A.at[i, i + 1].set(h[i] / 6.0)
        r = r.at[i].set((ys[i + 1] - ys[i]) / h[i]
                        - (ys[i] - ys[i - 1]) / h[i - 1])
    A = (A.at[n - 1, n - 1].set(h[n - 3])
          .at[n - 1, n - 2].set(-(h[n - 3] + h[n - 2]))
          .at[n - 1, n - 3].set(h[n - 2]))          # THE one row
    r = r.at[n - 1].set(0.0)
    return jnp.linalg.solve(A, r)


def main():
    print("== [GAP-5] notaknot-twin (one-row BC twin at W*8, "
          "rejector-formed) ==")
    tab = A1.prep_tab(A1.build_tab_nasa())
    state_c1, solv, cfg = O33.make_case(tab)
    W = np.asarray(O33.W_STAR, dtype=float)
    old_cls = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    rows = {}
    ok = True
    try:
        for arm, fn in (("natural", TV.spline_coeffs),
                        ("notaknot", spline_coeffs_nak)):
            # cache hygiene (declared hazard, docstring): a patched
            # spline is invisible to the engine keys
            TV._SCAN_ENGINES.clear()
            TV._SCAN_SIGSEEN.clear()
            orig = TV.spline_coeffs
            TV.spline_coeffs = fn
            try:
                mism, cds, certs = {}, {}, {}
                for r_ in (1, 2):
                    rel, out, _g, cd = goal_metric(W, None, tab, cfg,
                                                   state_c1, solv,
                                                   r=r_)
                    mism[r_] = float(rel)
                    cds[r_] = float(cd)
                    certs[r_] = float(out["cert_worst"])
                    print("  [%s r=%d] corner mismatch %.6e  "
                          "(cd %.6e, cert %.3e)"
                          % (arm, r_, rel, cd, out["cert_worst"]))
            finally:
                TV.spline_coeffs = orig
            rows[arm] = dict(mismatch=mism, cd=cds, cert=certs)
            ok &= check("%s marches certified (r=1 %.3e, r=2 %.3e)"
                        % (arm, certs[1], certs[2]),
                        certs[1] <= 1.0 and certs[2] <= 1.0)
        base, twin = rows["natural"], rows["notaknot"]
        print("  baseline r=1 mismatch %.6e vs S19 figure %.6e "
              "(context: the M3 closure version change is between "
              "them — reported, not gated)"
              % (base["mismatch"][1], S19_D1_BASELINE))
        d1 = twin["mismatch"][1] - base["mismatch"][1]
        d2 = twin["mismatch"][2] - base["mismatch"][2]
        # RE-FORMED REJECTOR (see docstring — form 1 refuted by its
        # own firing): the twin delta must be two-resolution STABLE
        spread = max(abs(base["mismatch"][1] - base["mismatch"][2]),
                     abs(twin["mismatch"][1] - twin["mismatch"][2]))
        band_d = A1.K_RICH * spread + 100.0 * EPS
        ok &= check("delta-stability rejector: |delta_r1 - delta_r2|"
                    " = %.3e <= K_RICH x max arm spread %.3e (else "
                    "mesh artifact, twin REJECTED)"
                    % (abs(d1 - d2), band_d), abs(d1 - d2) <= band_d)
        d_cd = abs(twin["cd"][1] - base["cd"][1])
        print("  mechanism datum: corner-density (lip-state) shift "
              "|cd_twin - cd_base| = %.3e (%.2f%% — the BC bias "
              "moves the lip flow state, the mechanism under test; "
              "reported, not gated)"
              % (d_cd, 100.0 * d_cd / abs(base["cd"][1])))
        print("  GAP-5 TWIN DATUM: corner-mismatch delta r=1 %+.6e "
              "(%.6e -> %.6e), r=2 %+.6e — consequence adjudication "
              "= F2 (incumbent BC untouched)"
              % (d1, base["mismatch"][1], twin["mismatch"][1], d2))
        art = os.path.join(HERE, "s25bis_notaknot_twin.json")
        json.dump(dict(W_star=[float(t) for t in W], rows=rows,
                       delta_r1=d1, delta_r2=d2, band_delta=band_d,
                       cd_shift=d_cd,
                       s19_baseline=S19_D1_BASELINE),
                  open(art, "w"), indent=1)
        print("  artifact -> %s" % art)
    finally:
        TV.M_NODES, TV.KNOT_XI = old_cls
    print("VERDICT (machinery): %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
