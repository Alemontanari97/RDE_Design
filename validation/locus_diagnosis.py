"""[X-LOCD] S20 RETRO-DIAGNOSIS — the C-1 THREE-WAY LOCUS TEST
(S22, F1 entry row of plan v3; log validation/PROGRESS_2026-08-11_
S22_governor.md; consumes the O4 instrumentation ARMED at S21 F0:
cert argmax localization [X-TOCV], rejected-design persistence
(run_trsqp + A1_REJ_SAVE), and the [X-VMON] Lambda-form validity
monitor).

WHAT THIS DISCHARGES. The S20 standoff reading is of record as
"CONSISTENT WITH a DEF-sector optimum AND equally with an
interior-binding tier-1 optimum until O4 localization runs" (RT-1).
This carrier IS that O4 localization for the S20 instance: it takes
the DETERMINISTICALLY REGENERATED S20 walk rejections (the [X-AKNO]
attempt-3 path re-run with A1_REJ_SAVE + the class-completed
persistence payload) and, for each rejected design AND the returned
certified base, computes (i) the cert-argmax failing cell, (ii) the
per-cell (G)/Lambda-form validity field val over the design-wall
region, (iii) the terminal C+ chain (the Rao control surface,
locus_split of record), and classifies per the C-1 THREE-WAY
DECISION TABLE (ADVISORY_claims_to_code, adopted VERBATIM — each
branch can fire, none is failure):
 (a) argmin-val locus AND failing cell within the stencil radius of
     the terminal C+ chain -> DEF-signature reading CONFIRMED for
     the instance (H2 satisfied);
 (b) argmin-val locus INTERIOR (off-chain) -> INTERIOR CAUSTIC: the
     DEF reading for S20 is FALSIFIED; the design's evaluation
     belongs to tier-1 and the margin constraint must exclude it;
 (c) val healthy at the failing cell yet Newton stalls -> NON-FOLD
     mechanism (class construction, not physics): both readings
     falsified.

PRE-REGISTERED OPERATIONAL RULES (fixed BEFORE the first analysis
run, session gate [P2-T2] + this docstring; constants REUSED from
the record, none tuned):
 * m_ref  = min val over the design-wall region of the CERTIFIED
   baseline W* field (the healthy reference, measured in-run). The
   baseline must be certified with m_ref > 0 or the instrument is
   non-discriminating (carrier FAIL).
 * FOLD-IMPLICATED iff val_min(design region) < m_ref / K_RICH
   (K_RICH = 4, the repo's registered two-level safety constant).
   The same threshold defines "val healthy" at the failing cell.
 * ON-CHAIN iff the euclidean distance to the nearest CONTROL-
   SURFACE chain node <= STENCIL_RADIUS x (local chain node spacing
   at that node), STENCIL_RADIUS = 2 (o33_bench registered constant;
   local spacing = max of the two adjacent chain segment lengths).
 * DECISION TREE (annotations declared, no new branches): (1) not
   fold-implicated -> (c); (2) argmin off-chain -> (b); (3) argmin
   on-chain AND failing cell on-chain -> (a); (4) argmin on-chain,
   failing cell off-chain: val(fail) healthy -> (c) [annotated:
   fold present at the surface, the stall is elsewhere and
   non-fold]; val(fail) unhealthy -> (b) [annotated: the stall
   locus is itself an interior low-margin point].
 * SCOPE: the val field is evaluated on the DESIGN-WALL region
   (cols beyond n_fan + n_arc — where the S20 design variations
   act and where the DEF/interior dichotomy is defined). Kernel/arc
   cells are design-independent at fixed thB; their val is reported
   as information only. Non-finite/subsonic-clip val entries are
   masked and counted.

DETERMINISM ([P2-T2]): the regenerated rejection set is compared
against the S20 crawl signature of record (five rejections,
cert_worst = 1.170, 2.458, 1.060, 1.455, 1.698 to the printed 3
significant digits + the walk's own re-record on load). A mismatch
is a FINDING of record (printed loudly, carried into the verdict
wording as "regenerated-set"), and the locus test still runs on the
regenerated set — pre-declared, not a carrier failure.

BRIDGE FALSIFIER (M0 Part VI, K_disc ~ A_0 CONJECTURE): this run is
its named test on the S20 instance — val must approach 0 where
certification degrades. Branch (a)/(b) with genuine depression
SUPPORTS the bridge; branch (c) FIRES the falsifier for this
instance (the certifiability frontier here is not the validity
boundary) — reported explicitly either way.

MACHINERY REJECTORS (must be able to reject, R5): (KAT-CLS) the
classifier is exercised on four synthetic scenarios (one per
branch + the annotated (4) sub-case) and must return exactly the
expected branch for each; (BASE-CTRL) the certified baseline must
classify NOT fold-implicated (a monitor that fires on a healthy
certified field is non-discriminating -> FAIL); a rejected design
whose re-record does NOT reproduce cert_worst > 1 fails the
reproduction row.

ON-DEMAND CARRIER (env: jax). Inputs: A1_LOCD_REJ (default
validation/s22_rejected_designs.json — the A1_REJ_SAVE artifact of
the regeneration run), A1_LOCD_BASE (default
validation/s22_certlim_base.json — the A1_AKN_CERTLIM_SAVE
artifact; analyzed when present). Exit 0 iff all machinery rows
pass (KAT-CLS, baseline control, reproduction rows); the three-way
branches themselves are VERDICTS, printed per design + aggregated.
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
import thermotab_c1_jax as TH          # noqa: E402
import o33_bench as O33                # noqa: E402
import validity_monitor as VM          # noqa: E402
from adaptive_knot_optimize import design_class  # noqa: E402

jax.config.update("jax_enable_x64", True)

EPS = float(jnp.finfo(jnp.float64).eps)
HERE = os.path.dirname(os.path.abspath(__file__))
REJ_PATH = os.environ.get(
    "A1_LOCD_REJ", os.path.join(HERE, "s22_rejected_designs.json"))
BASE_PATH = os.environ.get(
    "A1_LOCD_BASE", os.path.join(HERE, "s22_certlim_base.json"))

# S20 crawl signature of record (log S20 step 8 / M0 Part VI attempt-3
# block): EIGHT rejection events over FIVE distinct designs,
# cert_worst to the printed 3 sig digits (2.458 rejected 4x = the
# same design re-proposed). The determinism check compares the SET of
# distinct rounded values and the distinct-design count; the analysis
# dedupes bit-identical designs first (dedup-before-downstream).
S20_SIGNATURE = frozenset((1.170, 2.458, 1.060, 1.455, 1.698))
S20_N_DISTINCT = 5


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ======================================================================
# val field on a recorded design (design-wall region scope)
# ======================================================================
def make_lambda_fn(state_fn):
    """Lam = V d(alpha)/dV by AD through the SAME closure the march
    used (the [X-VMON] construction, generalized in state_fn)."""
    def alpha_of(q):
        c = state_fn(q, None)[3]
        return jnp.arcsin(jnp.minimum(1.0, c / q))
    g = jax.grad(alpha_of)
    return jax.jit(jax.vmap(lambda q: q * g(q)))


def field_val(cols, k_lo, state_fn, lam_fn):
    """Per-cell val over cols[k_lo:] (the design-wall region).
    Returns (pts (n,2), val (n,), n_masked) with non-finite /
    subsonic-clip entries masked out."""
    pts = []
    for col in cols[k_lo:]:
        cl = np.asarray(col["cline"])
        if cl.size:
            pts.append(cl)
    P = np.concatenate(pts, axis=0)
    u, v = P[:, 2], P[:, 3]
    q = np.hypot(u, v)
    th = np.arctan2(v, u)
    c = np.asarray(state_fn(jnp.asarray(q), None)[3])
    ratio = np.minimum(1.0, c / q)
    al = np.arcsin(ratio)
    lam = np.asarray(lam_fn(jnp.asarray(q)))
    val, _den = VM.val_G(jnp.asarray(th), jnp.asarray(al),
                         jnp.asarray(lam))
    val = np.asarray(val)
    good = np.isfinite(val) & (ratio < 1.0)
    return P[good, :2], val[good], int((~good).sum())


def chain_geometry(cols, n_fan, n_arc):
    """Terminal C+ chain + control-surface mask (the registered
    locus) + per-node stencil radius (STENCIL_RADIUS x local max
    adjacent segment length)."""
    chain, owner = O33.cplus_chain(cols)
    cs = O33.locus_split(owner, n_fan, n_arc)
    nodes = chain[cs][:, :2]
    seg = np.linalg.norm(np.diff(nodes, axis=0), axis=1)
    r_loc = np.empty(len(nodes))
    for i in range(len(nodes)):
        left = seg[i - 1] if i > 0 else seg[0]
        right = seg[i] if i < len(seg) else seg[-1]
        r_loc[i] = O33.STENCIL_RADIUS * max(left, right)
    return nodes, r_loc


def dist_to_chain(pt, nodes, r_loc):
    """(distance to nearest control-surface node, its stencil radius,
    nearest index)."""
    d = np.linalg.norm(nodes - np.asarray(pt)[None, :], axis=1)
    i = int(np.argmin(d))
    return float(d[i]), float(r_loc[i]), i


# ======================================================================
# the pre-registered classifier (pure function -> KAT-able)
# ======================================================================
def classify(fold_implicated, argmin_on_chain, fail_on_chain,
             fail_healthy):
    """C-1 three-way decision tree, pre-registered rules 1-4."""
    if not fold_implicated:
        return "c", "no fold signature in the design region"
    if not argmin_on_chain:
        return "b", "argmin-val locus interior (off-chain)"
    if fail_on_chain:
        return "a", "argmin-val AND failing cell on the terminal C+"
    if fail_healthy:
        return "c", ("annotated: fold present at the surface, the "
                     "stall is elsewhere and non-fold")
    return "b", ("annotated: the stall locus is itself an interior "
                 "low-margin point")


def kat_classifier():
    print("-- KAT-CLS: classifier known-answer (4 scenarios) --")
    ok = True
    ok &= check("scenario (a): depressed on-chain argmin + on-chain "
                "fail -> a",
                classify(True, True, True, False)[0] == "a")
    ok &= check("scenario (b): depressed interior argmin -> b",
                classify(True, False, True, True)[0] == "b")
    ok &= check("scenario (c): no depression -> c",
                classify(False, True, True, True)[0] == "c")
    ok &= check("scenario (4): on-chain argmin, healthy off-chain "
                "fail -> c annotated",
                classify(True, True, False, True)[0] == "c")
    ok &= check("scenario (4'): on-chain argmin, unhealthy off-chain "
                "fail -> b annotated",
                classify(True, True, False, False)[0] == "b")
    return ok


# ======================================================================
# per-design analysis
# ======================================================================
def record_with_localization(W, xi, m, tab, cfg, state_fn, solv):
    """Re-record a persisted design in ITS class with argmax
    localization armed and the field returned. margin_floor = 0 (the
    in-optimization record semantics the rejection used)."""
    old_argmax = TV.CERT_ARGMAX
    TV.CERT_ARGMAX = True
    try:
        with design_class(xi, m=m):
            out, _plan = TV.run_toc_record(
                np.asarray(W, dtype=float), tab, cfg,
                state_fn=state_fn, solvers=solv, return_field=True)
    finally:
        TV.CERT_ARGMAX = old_argmax
    return out


def analyze(tag, out, state_fn, lam_fn, m_ref):
    """Compute the locus quantities + classification for one recorded
    design. Returns (branch, note, quants)."""
    n_fan, n_arc = out["n_fan"], out["n_arc"]
    k_lo = n_fan + n_arc
    pts, val, n_mask = field_val(out["cols"], k_lo, state_fn, lam_fn)
    nodes, r_loc = chain_geometry(out["cols"], n_fan, n_arc)
    i_min = int(np.argmin(val))
    val_min = float(val[i_min])
    p_min = pts[i_min]
    d_min, r_min, _ = dist_to_chain(p_min, nodes, r_loc)

    am = out.get("cert_argmax")
    fail_xy = None
    if am is not None and am.get("x") is not None:
        fail_xy = np.array([am["x"], am["y"]])
    if fail_xy is not None:
        d_f, r_f, _ = dist_to_chain(fail_xy, nodes, r_loc)
        # val at the failing cell = val of the nearest field point
        j = int(np.argmin(np.linalg.norm(pts - fail_xy[None, :],
                                         axis=1)))
        val_fail = float(val[j])
        fail_on_chain = d_f <= r_f
    else:
        d_f, r_f, val_fail, fail_on_chain = (np.nan, np.nan,
                                             np.nan, False)

    thr = m_ref / A1.K_RICH
    fold_implicated = val_min < thr
    fail_healthy = (np.isfinite(val_fail) and val_fail >= thr)
    argmin_on_chain = d_min <= r_min
    branch, note = classify(fold_implicated, argmin_on_chain,
                            fail_on_chain, fail_healthy)

    print("  [%s] cert_worst %.3e | argmax cell %s at (%s, %s) ctx %s"
          % (tag, out["cert_worst"], am["kind"] if am else "n/a",
             ("%.4f" % am["x"]) if fail_xy is not None else "n/a",
             ("%.4f" % am["y"]) if fail_xy is not None else "n/a",
             am["ctx"] if am else "n/a"))
    print("  [%s] val field: %d pts (%d masked) | val_min %.4e at "
          "(%.4f, %.4f) | m_ref %.4e thr(m_ref/K) %.4e"
          % (tag, len(val), n_mask, val_min, p_min[0], p_min[1],
             m_ref, thr))
    print("  [%s] locus: d(argmin,chain) %.4e vs r_st %.4e (%s) | "
          "d(fail,chain) %s vs r_st %s (%s) | val(fail) %s"
          % (tag, d_min, r_min,
             "ON-CHAIN" if argmin_on_chain else "interior",
             ("%.4e" % d_f) if np.isfinite(d_f) else "n/a",
             ("%.4e" % r_f) if np.isfinite(r_f) else "n/a",
             "ON-CHAIN" if fail_on_chain else "off-chain",
             ("%.4e" % val_fail) if np.isfinite(val_fail) else "n/a"))
    print("  [%s] BRANCH (%s): %s" % (tag, branch, note))
    return branch, note, dict(val_min=val_min, d_min=d_min,
                              r_min=r_min, val_fail=val_fail,
                              fold=fold_implicated)


def main():
    print("== [X-LOCD] S20 retro-diagnosis: C-1 three-way locus test "
          "(JAX %s) ==" % jax.__version__)
    ok = True
    ok &= kat_classifier()

    tab = A1.prep_tab(A1.build_tab_nasa())
    state_c1, solv, cfg = O33.make_case(tab)
    lam_fn = make_lambda_fn(state_c1)

    # ---------------- baseline healthy control (m_ref) ---------------
    print("-- BASE-CTRL: certified baseline W* (uniform 8-node) --")
    out_b = record_with_localization(O33.W_STAR, None, TV.M_NODES,
                                     tab, cfg, state_c1, solv)
    ok &= check("baseline certified (cert_worst <= 1)",
                out_b["cert_worst"] <= 1.0)
    k_lo_b = out_b["n_fan"] + out_b["n_arc"]
    _, val_b, n_mask_b = field_val(out_b["cols"], k_lo_b, state_c1,
                                   lam_fn)
    m_ref = float(np.min(val_b))
    print("  baseline design-wall val: %d pts (%d masked), min %.4e, "
          "median %.4e" % (len(val_b), n_mask_b, m_ref,
                           float(np.median(val_b))))
    ok &= check("BASE-CTRL: healthy field on the valid side "
                "(m_ref > 0; instrument discriminating)", m_ref > 0.0)

    # ---------------- load the regenerated rejection set -------------
    if not os.path.exists(REJ_PATH):
        print("FATAL: rejected-designs artifact not found: %s "
              "(run the [X-AKNO] regeneration with A1_REJ_SAVE first)"
              % REJ_PATH)
        return 1
    rej_all = json.load(open(REJ_PATH))["rejected"]
    # dedup bit-identical designs (the S20 livelock-side re-proposals)
    rej, seen = [], set()
    for r in rej_all:
        key = tuple(r["W"])
        if key not in seen:
            seen.add(key)
            rej.append(r)
    print("-- regenerated rejection set: %d events, %d distinct "
          "designs (%s) --" % (len(rej_all), len(rej), REJ_PATH))
    got = frozenset(round(float(r["cert_worst"]), 3) for r in rej
                    if r.get("cert_worst") is not None)
    sig_ok = (got == S20_SIGNATURE and len(rej) == S20_N_DISTINCT)
    print("  distinct cert_worst regenerated: %s" % sorted(got))
    print("  distinct cert_worst S20 record : %s"
          % sorted(S20_SIGNATURE))
    if sig_ok:
        print("  [PASS] S20 rejection signature REPRODUCED "
              "(determinism, [P2-T2])")
    else:
        print("  [FINDING, declared per gate P2-T2] regenerated set "
              "differs from the S20 signature — the verdict below is "
              "on the REGENERATED set (determinism finding of record)")

    # ---------------- three-way test per rejected design -------------
    branches = []
    for i, r in enumerate(rej):
        tag = "rej-%d(seg %d)" % (i + 1, r["seg"])
        print("-- %s --" % tag)
        out_r = record_with_localization(
            r["W"], r.get("knot_xi"), r.get("m_nodes"), tab, cfg,
            state_c1, solv)
        rep = check("%s: re-record reproduces the rejection "
                    "(cert_worst > 1)" % tag, out_r["cert_worst"] > 1.0)
        ok &= rep
        if not rep:
            continue
        b, note, _q = analyze(tag, out_r, state_c1, lam_fn, m_ref)
        branches.append(b)

    # ---------------- the returned certified base (when present) -----
    if os.path.exists(BASE_PATH):
        print("-- last certified base (outcome-II returned design) --")
        base = json.load(open(BASE_PATH))
        W_c = [float(x) for x in base["W"]]
        xi_c = [float(x) for x in base["xi"]]
        out_c = record_with_localization(W_c, xi_c, len(xi_c), tab,
                                         cfg, state_c1, solv)
        ok &= check("certified base re-certifies (cert_worst <= 1)",
                    out_c["cert_worst"] <= 1.0)
        _b, _n, qc = analyze("base", out_c, state_c1, lam_fn, m_ref)
        print("  [bridge] base val_min / m_ref = %.3f (a ratio << 1 "
              "at the frontier base SUPPORTS K_disc ~ A_0; ~1 with "
              "branch (c) above FIRES the bridge falsifier for this "
              "instance)" % (qc["val_min"] / m_ref))
    else:
        print("  (no certified-base artifact at %s — base analysis "
              "skipped, declared)" % BASE_PATH)

    # ---------------- aggregate verdict ------------------------------
    print("-- AGGREGATE (S20 instance, O4 discharge) --")
    from collections import Counter
    cnt = Counter(branches)
    print("  branch distribution over %d rejections: %s"
          % (len(branches), dict(cnt)))
    if branches:
        uniform = len(cnt) == 1
        b0 = branches[0] if uniform else None
        word = {"a": "DEF-signature reading CONFIRMED (H2 satisfied "
                     "for the instance)",
                "b": "INTERIOR CAUSTIC — the DEF reading for S20 is "
                     "FALSIFIED; tier-1 evaluation route",
                "c": "NON-FOLD mechanism — class construction, not "
                     "physics; BOTH readings falsified AND the "
                     "K_disc ~ A_0 bridge falsifier FIRES for this "
                     "instance"}
        if uniform:
            print("  VERDICT OF RECORD (%s%s): unanimous branch (%s) "
                  "-> %s"
                  % ("regenerated-set, " if not sig_ok else "",
                     "determinism OK" if sig_ok else "determinism "
                     "FINDING declared", b0, word[b0]))
        else:
            print("  VERDICT OF RECORD: MIXED branches %s — reported "
                  "per-design above; the instance discharge carries "
                  "the distribution (no forced synthesis)"
                  % dict(cnt))
    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
