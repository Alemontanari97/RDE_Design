"""[F3] THE SQP-RETURN STAGE OF THE PLUG O3.3 — from a perturbed start,
does OUR optimizer walk back to Rao's contour in HIS world?

WHAT [X-RAOO3] SHOWED AND WHAT IT DID NOT. Rao's optimum is stationary
for our functional under our march (interior AD gradients at the noise
floor, the tip identity to 0.5 percent). Stationarity is a statement
about one point; the SQP's licence needs the OTHER half of the bell's
precedent ([X-TOCV]: "TR-SQP from a 1.5 percent perturbed start ->
KKT closure, contour inside the derived cross-code band"): started off
the optimum, the driver must come BACK to it — and the sign-flipped
objective must walk AWAY (the S23 rejector: an optimizer is part of the
instrument).

POSING. As [X-RAOO3]/[X-RAOTW]: GENO's legacy p_b = 0 field at x0 as
start line (gas identified from the field, q_at_pa, EDGE_FILL); design =
cubic-spline knot heights on (x0, x_D] (clamped at the start-line wall
point with GENO's slope, natural right end), the TIP knot PINNED at
Rao's y_D so the base term is a constant and no base-pressure model
enters; objective J = F_in + integral (p_w - p_a) 2 pi y (-dy) on the
frozen record (replay-differentiable, the [X-PSPL] pattern); driver =
the segmented trust-constr of [X-PSPL] (record -> certified base ->
walk on the frozen schedule -> accept only an improving certified base;
reject-and-shrink; no-motion at the radius floor = convergence).

DERIVED BANDS (nothing chosen):
  W_fit    = GENO's wall at the knots (Rao's contour in spline space);
  e_rep    = |spline(W_fit) - GENO wall| at the stations: the
             representation error — the optimizer cannot resolve
             Rao's wall better than its own space represents it;
  band_W   = K_RICH * max e_rep;
  g_floor  = |grad J(W_fit)|_inf, the stationarity residual of Rao's
             own contour under this instrument ([X-RAOO3] level);
  gtol     = K_RICH * g_floor;
  band_J   = K_RICH * |J(W_fit; K) - J(W_fit; 2K-1)| + |grad J(W_fit)|_1 * band_W.

PRE-REGISTERED (R5)
  P1  every accepted base is a certified record (driver-enforced;
      worst cert reported);
  P2  CONVERGENCE: |grad J(W*)|_inf <= gtol at the final base;
  P3  RETURN: max over stations |y(W*) - y_GENO| <= band_W, from a
      start whose distance is far outside it (the 1.5 percent
      perturbation; ratio reported);
  P4  VALUE: J(W_pert) < J(W*) and |J(W*) - J(W_fit)| <= band_J;
  R1  REJECTOR: the same driver on the SIGN-FLIPPED objective from
      the same start ends FARTHER from Rao's wall than it began.
FALSIFIER: P3 failing with P2 passing = the driver converged to a
different stationary point of the spline space (a finding about the
posing or a second optimum); P2 failing = the driver cannot close
where [X-RAOO3] says the gradient vanishes (a driver finding).

FIRST POSING AND RE-POSING (2026-08-27, declared; log
_rao1961_twin/run_sqpret_posing1_2026-08-27.log). v1 put the knots on
the whole design region (x0, x_D]: 5/6 — P1, P2, P4a/b, R1 PASS; P3 FAIL
(return 7.0e-3 -> 4.3e-3 against band_W 3.8e-4). Two measured causes,
both instrument: (i) the gradient floor on Rao's own wall was 3.7e5 N/m
against the 8e1..4e2 of [X-RAOO3]'s interior bumps — the first knot's
cardinal function deforms the wall INSIDE the near-cut zone (first
~0.35 L_r after the Cauchy start line) that [X-RAOO3] v2 had to
exclude, so the driver chased noise (trials rejected, one uncertified
base) and gtol = 1.5e6 was non-discriminating; (ii) the location band
ignored the gradient floor: a floor g on a surface of curvature c
locates the optimum only to g/c (measured c from the perturbation:
2 (J_fit - J_p) / d_start^2 = 2.9e8 -> 1.2e-3 at v1's floor, above
band_W). v2 (this file): the wall on [x0, x0 + 0.35 L_r] is FROZEN to
Rao's (start of the spline clamped to GENO's value and slope there),
the knots live on [x0 + 0.35 L_r, x_D] with the tip pinned; band_W =
K_RICH (e_rep + g_floor / c_hat) with both terms measured; the sign=-1
bookkeeping of the rejector driver fixed (v1's R1 verdict stood on the
final trial point; the walk-away was real, the printed J was not).
v2 run (log run_sqpret_v2_2026-08-27.log): P1-P4 PASS — floor 6.3e3
(60x below v1), return 4.98e-3 -> 1.07e-4 inside band_W 2.4e-4, |grad|
7.8e5 -> 86, J* - J_fit = +0.3 N — but R1 UNDECIDED: with a budget of 6
segments every thrust-MINIMIZING trial landed on an uncertifiable record
(worst 5e16..4e15 at radii 5e-2..2.1e-2) and the driver never moved,
which the gate reads as FAIL by discipline. R1 PROBE (same posing, 14
segments; log run_sqpret_r1probe_2026-08-27.log + r1_probe_2026-08-27.py):
the radius must fall to ~1.2e-2 before a certifiable descent step
exists (five uncertifiable bases first), then the walk leaves Rao's
contour (dist 5.0e-3 -> 1.09e-2, J -3.1e4 N). SEG_R1 = 14 is therefore
the rejector's calibrated budget (declared), and the run of record is
the full carrier with it.

ON-DEMAND CARRIER (env: jax + a GENO run directory via RAO_GENO_RUN).
"""
import os
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import a1_ideal_march_jax as A1                        # noqa: E402
from a1_plug_march import plug_march, col_fluxes       # noqa: E402
from a1_freejet_unit import q_at_pa                    # noqa: E402
from a1_toc_variational_jax import spline_coeffs, spline_eval  # noqa: E402
from rao1961_twin import (load_geno, gas_from_field, start_from_geno,
                          G, PA_PC, EDGE_FILL)         # noqa: E402

K_RICH = A1.K_RICH
RUN = os.environ.get("RAO_GENO_RUN", "")
X0 = float(os.environ.get("RAO_X0", 0.30))
N_ROW = int(os.environ.get("RAO_N", 61))
K_ST = int(os.environ.get("RAO_K", 81))
M_NODES = int(os.environ.get("RAO_M", 8))
PERT = float(os.environ.get("RAO_PERT", 0.015))
MAXSEG = int(os.environ.get("RAO_SEG", 12))
FREEZE = float(os.environ.get("RAO_FREEZE", 0.35))   # v2: near-cut zone kept as Rao's
SEG_R1 = int(os.environ.get("RAO_SEG_R1", 14))       # rejector budget, calibrated (see docstring)
NPASS = [0, 0]


def check(label, ok):
    NPASS[1] += 1
    NPASS[0] += int(bool(ok))
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


class World:
    pass


def setup():
    w = World()
    fld, wall = load_geno(RUN)
    Rg, ts, ps = gas_from_field(fld)
    w.tab = A1.prep_tab(A1.build_tab_gconst(g=G, Rg=Rg, ts=ts, ps=ps))
    w.ta = A1.tab_arrays(w.tab)
    w.pa = PA_PC * ps
    w.qpa = float(q_at_pa(w.pa, w.ta, w.tab["_as"]))
    w.xD = float(wall[-1, 0])
    w.wall = wall
    w.start, _ = start_from_geno(fld, wall, X0, N_ROW)
    stl = np.stack([np.full(len(w.start[1]), X0), w.start[1], w.start[2],
                    w.start[3]], 1)
    md_in, w.F_in = col_fluxes(stl, w.ta, w.pa, 1.0)
    w.xs0 = X0 + FREEZE * (w.xD - X0)              # spline starts here (v2)
    w.yw0 = float(np.interp(w.xs0, wall[:, 0], wall[:, 1]))
    sl = np.gradient(wall[:, 1], wall[:, 0])
    w.slope0 = float(np.interp(w.xs0, wall[:, 0], sl))
    xi = np.arange(1, M_NODES + 1) / M_NODES
    w.xk = w.xs0 + (w.xD - w.xs0) * xi             # last knot AT x_D
    w.yD = float(np.interp(w.xD, wall[:, 0], wall[:, 1]))
    w.W_fit = np.interp(w.xk[:-1], wall[:, 0], wall[:, 1])   # free dofs
    print("   gas Rg=%.4f ts=%.2f ps=%.6g; pa=%.4g; q_at_pa=%.1f; x_D=%.4f"
          % (Rg, ts, ps, w.pa, w.qpa, w.xD))
    print("   start line %d rows at x0=%.2f (F_in %.6g N); wall frozen to Rao's on"
          " [%.2f, %.4f]; knots M=%d on [%.4f, %.4f] (tip pinned at y_D=%.4f);"
          " clamped slope0=%.4f"
          % (len(w.start[1]), X0, w.F_in, X0, w.xs0, M_NODES, w.xs0, w.xD,
             w.yD, w.slope0))
    return w


def stations(W, w, K=None):
    """Design vector (free knot heights) -> (x, y, slope) at K stations."""
    xs = jnp.concatenate([jnp.array([w.xs0]), jnp.asarray(w.xk)])
    ys = jnp.concatenate([jnp.array([w.yw0]), jnp.asarray(W),
                          jnp.array([w.yD])])
    Mc = spline_coeffs(xs, ys, w.slope0)
    Kq = K_ST if K is None else K
    xq = jnp.linspace(X0, w.xD, Kq + 1)[1:]
    yq_s, sq_s = jax.vmap(lambda x: spline_eval(x, xs, ys, Mc))(xq)
    # frozen part: Rao's (GENO's) wall, value and slope, upstream of xs0
    yq_f = jnp.interp(xq, jnp.asarray(w.wall[:, 0]), jnp.asarray(w.wall[:, 1]))
    sq_f = jnp.interp(xq, jnp.asarray(w.wall[:, 0]),
                      jnp.asarray(np.gradient(w.wall[:, 1], w.wall[:, 0])))
    frozen = xq < w.xs0
    return xq, jnp.where(frozen, yq_f, yq_s), jnp.where(frozen, sq_f, sq_s)


def push_of(out, w):
    wl = out["wall"]
    q = jnp.sqrt(wl[:, 2] ** 2 + wl[:, 3] ** 2)
    pw = A1.state_q(q, w.ta)[1]
    dy = wl[1:, 1] - wl[:-1, 1]
    wgt = 2.0 * jnp.pi * 0.5 * (wl[1:, 1] + wl[:-1, 1])
    pm = 0.5 * (pw[1:] + pw[:-1])
    return jnp.sum((pm - w.pa) * wgt * (-dy))


def march_record(W, w, K=None):
    st = tuple(np.asarray(v) for v in stations(np.asarray(W, float), w, K))
    return plug_march(st, w.start, w.qpa, w.tab, 1.0, edge_fill=EDGE_FILL)


def J_replay(W, w, sched, K=None):
    out, _ = plug_march(stations(W, w, K), w.start, w.qpa, w.tab, 1.0,
                        sched=A1.Sched("play", sched.d), edge_fill=EDGE_FILL)
    return w.F_in + push_of(out, w)


def J_and_grad(W, w, sched):
    f = lambda z: J_replay(z, w, sched)                 # noqa: E731
    v, g = jax.value_and_grad(f)(jnp.asarray(W, dtype=float))
    return float(v), np.asarray(g, dtype=float)


def run_trsqp(W0, w, sign=+1.0, max_segments=MAXSEG, maxiter_per_seg=8,
              tag=""):
    """The [X-PSPL] segmented driver, verbatim in logic."""
    W = np.asarray(W0, dtype=float)
    W_cert = None
    W_best, J_best, g_best, cw_best = None, -sign * np.inf, None, None
    tr = 0.05
    n_rec = 0
    worst_cert = 0.0
    for seg in range(max_segments):
        try:
            out_rec, sched = march_record(W, w)
            n_rec += 1
            cw = float(out_rec["cert_worst"])
            if cw > 1.0:
                raise RuntimeError("record not certified (worst %.3e)" % cw)
        except Exception as err:
            if W_cert is not None and tr > 1e-3:
                tr = max(1e-3, 0.5 * tr)
                print("    %s[seg %2d] base REJECTED (%s) -> revert, radius %.3e"
                      % (tag, seg, str(err)[:40], tr), flush=True)
                W = W_cert.copy()
                continue
            raise
        J0, g0 = J_and_grad(W, w, sched)
        if W_best is not None and sign * J0 < sign * J_best:
            if tr <= 1.01e-3:
                print("    %s[seg %2d] trial worse at the radius floor -> converged"
                      % (tag, seg), flush=True)
                break
            tr = max(1e-3, 0.5 * tr)
            print("    %s[seg %2d] trial J = %.8e REJECTED -> revert, radius %.3e"
                  % (tag, seg, J0, tr), flush=True)
            W = W_best.copy()
            continue
        W_cert = W.copy()
        worst_cert = max(worst_cert, cw)
        if sign * J0 > sign * J_best:
            W_best, J_best, g_best, cw_best = W.copy(), J0, g0.copy(), cw
        print("    %s[seg %2d] J = %.8e  |grad|inf = %.3e  cert = %.3e"
              % (tag, seg, J0, np.max(np.abs(g0)), cw), flush=True)

        def fun(z):
            v, g = J_and_grad(z, w, sched)
            return -sign * v, -sign * g
        while True:
            res = minimize(fun, W, jac=True, method="trust-constr",
                           options=dict(maxiter=maxiter_per_seg,
                                        initial_tr_radius=tr, gtol=0.0,
                                        xtol=1e-14, verbose=0))
            step = float(np.linalg.norm(res.x - W))
            if step >= 1e-12 or tr <= 1.01e-3:
                break
            tr = max(1e-3, 0.5 * tr)
            print("    %s[seg %2d] no motion at radius %.3e -> retry at %.3e"
                  % (tag, seg, 2 * tr, tr), flush=True)
        if step < 1e-12:
            print("    %s[seg %2d] no motion -> stop" % (tag, seg), flush=True)
            break
        W = np.asarray(res.x, dtype=float)
        tr = float(min(0.25, 1.5 * tr))
    return (W_best if W_best is not None else W), J_best, g_best, n_rec, worst_cert


def wall_dist(W, w):
    xq, yq, _ = stations(np.asarray(W, float), w)
    yg = np.interp(np.asarray(xq), w.wall[:, 0], w.wall[:, 1])
    return float(np.max(np.abs(np.asarray(yq) - yg)))


def main():
    t0 = time.time()
    print("== [F3] SQP-return in Rao's world: perturbed start -> back to Rao? ==")
    if not RUN or not os.path.isdir(RUN):
        print("   RAO_GENO_RUN not set -- nothing to do")
        return 2
    w = setup()

    print("-- S1: the reference in spline space and the derived bands --")
    e_rep = wall_dist(w.W_fit, w)
    out_fit, S_fit = march_record(w.W_fit, w)
    J_fit, g_fit = J_and_grad(w.W_fit, w, S_fit)
    g_floor = float(np.max(np.abs(g_fit)))
    gtol = K_RICH * g_floor
    out_fit2, _ = march_record(w.W_fit, w, K=2 * K_ST - 1)
    J_fit2 = float(w.F_in + push_of(out_fit2, w))
    print("  e_rep (spline vs GENO wall) max %.3e" % e_rep)
    print("  W_fit record cert %.3e; J_fit %.8e (K=%d) vs %.8e (K=%d): |dJ| %.3e"
          % (float(out_fit["cert_worst"]), J_fit, K_ST, J_fit2, 2 * K_ST - 1,
             abs(J_fit - J_fit2)))
    print("  grad floor |g(W_fit)|inf %.3e -> gtol %.3e" % (g_floor, gtol))

    print("-- S2: the perturbed start (%.1f percent, alternating) --" % (100 * PERT))
    sgn = np.array([(-1.0) ** k for k in range(len(w.W_fit))])
    W_p = w.W_fit * (1.0 + PERT * sgn)
    d_start = wall_dist(W_p, w)
    out_p, S_p = march_record(W_p, w)
    J_p, g_p = J_and_grad(W_p, w, S_p)
    c_hat = 2.0 * max(J_fit - J_p, 1e-300) / d_start ** 2      # measured curvature
    band_loc = g_floor / c_hat                                  # where a floor g can sit
    band_W = K_RICH * (e_rep + band_loc)
    band_J = K_RICH * abs(J_fit - J_fit2) + float(np.sum(np.abs(g_fit))) * band_W
    print("  start: dist to Rao %.3e; cert %.3e; J_p %.8e (J_fit - J_p = %+.4e);"
          " |grad|inf %.3e" % (d_start, float(out_p["cert_worst"]), J_p,
                               J_fit - J_p, np.max(np.abs(g_p))))
    print("  curvature c_hat %.3e -> location floor g/c %.3e; band_W = K(e_rep + g/c)"
          " = %.3e (start = %.1fx band_W); band_J %.3e"
          % (c_hat, band_loc, band_W, d_start / band_W, band_J))

    print("-- S3: TR-SQP (maximize) from the perturbed start --")
    W_s, J_s, g_s, n_rec, wc = run_trsqp(W_p, w, +1.0, tag="max ")
    d_s = wall_dist(W_s, w)
    print("  result: %d records, worst accepted cert %.3e; J* %.8e"
          " (J* - J_fit = %+.4e, J* - J_p = %+.4e); |grad|inf %.3e; dist %.3e"
          % (n_rec, wc, J_s, J_s - J_fit, J_s - J_p, np.max(np.abs(g_s)), d_s))
    check("P1 every accepted base certified (worst %.3e <= 1)" % wc, wc <= 1.0)
    check("P2 CONVERGENCE |grad J(W*)|inf %.3e <= gtol %.3e" % (np.max(np.abs(g_s)), gtol),
          np.max(np.abs(g_s)) <= gtol)
    check("P3 RETURN max|y(W*) - y_GENO| %.3e <= band_W %.3e (start was %.1fx)"
          % (d_s, band_W, d_start / band_W), d_s <= band_W)
    check("P4a VALUE J(W*) > J(W_pert) (+%.4e)" % (J_s - J_p), J_s > J_p)
    check("P4b VALUE |J(W*) - J(W_fit)| %.3e <= band_J %.3e" % (abs(J_s - J_fit), band_J),
          abs(J_s - J_fit) <= band_J)

    print("-- S4: R1 rejector - the sign-flipped objective from the same start --")
    W_r, J_r, _, n_r, _ = run_trsqp(W_p, w, -1.0, max_segments=SEG_R1, tag="min ")
    d_r = wall_dist(W_r, w)
    print("  minimizer: %d records; J %.8e (J_p - J = %+.4e); dist to Rao %.3e (start %.3e)"
          % (n_r, J_r, J_p - J_r, d_r, d_start))
    check("R1 REJECTOR: sign-flipped driver ends FARTHER from Rao (%.3e > %.3e)"
          % (d_r, d_start), d_r > d_start)

    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    print("VERDICT: %s" % ("PASS -- the SQP returns to Rao's optimum in his world"
                           if NPASS[0] == NPASS[1] else "FAIL"))
    return 0 if NPASS[0] == NPASS[1] else 1


if __name__ == "__main__":
    sys.exit(main())