#!/usr/bin/env python3
"""[X-QNTR] The plug walk's driver without knowledge of the optimum: a quasi-Newton
trust region whose every trial point is the TRUE march (2026-10-08, revalidation;
owner: "the tool must find the optimum agnostically -- in practice it will not know
the certified optimum").

WHY (measured on Rao 1961's plug, revalidation T10, logs t10_walk_rao61_*):
the segmented trust-constr driver (a1_plug_spline_opt.run_trsqp, now PSPL_DRIVER=
legacy) stopped 0.8-1.4e-5 below the best spline from both starts, |grad J|/J 2e-3,
for three reasons that are properties of the driver, not of the case:
  1. a segment walks the frozen-schedule replay, exact only within ~1.5e-3 of its
     base (T10b), but a trust-constr segment is not bounded by its radius (2.8 at
     radius 1e-3 on a quadratic): the replay predicted +1..4 % and the re-march
     said "worse", every few segments;
  2. the curvature is rebuilt from nothing at every segment, so the steps are
     gradient-like; on an ill-conditioned objective (best step along grad J
     2.4e-4, gain 6e-7) progress is slow;
  3. the stop rule (two steps in a row under a floor) reads slow progress as
     convergence.
One trust-constr step per segment and a floor of 1e-6 reached the optimum, but
that is a per-case setting and cost 2 h per walk.

WHAT THIS DRIVER DOES (textbook: Nocedal & Wright, Alg. 4.1 + damped BFGS 18.2):
  - every trial point is MARCHED (record, Newton-certified) and graded by its own
    J; the replay is used only for the gradient AT a marched point, where it is
    exact -- no step ever relies on the replay away from its base;
  - step d = argmax of the model  g.d - 1/2 d.B.d  inside |d| <= Delta (plus the
    linearised fold class m + gm.d >= 0 and the bounds when the caller has them);
  - B (the curvature of -J) starts from a SECANT Hessian of the replay at the
    start (2n reverse gradients at +-h), |eigenvalues| floored, then a damped
    BFGS update on every certified trial (accepted or not): the curvature is
    carried across the whole walk;
  - Delta: rho < 1/4 -> |d|/4; rho > 3/4 with the step on the boundary -> 2 Delta;
    a trial that fails (uncertified, non-finite, out of class) -> |d|/4;
  - STOP, three outcomes, none needs the optimum:
      CONVERGED  at an accepted point, the gain the model still predicts without
                 a radius (1/2 g.B^-1.g, or the class-constrained QP's value) is
                 below QNTR_TOL x |J| -- and stays below after B is replaced by a
                 secant Hessian MEASURED there (BFGS can over-estimate curvature
                 along directions the walk has not explored);
      RESOLUTION the radius fell below DELTA_MIN without an acceptable trial
                 (the predicted gain at that point is reported); OR five trials in
                 a row, each shorter than a tenth of the longest accepted step,
                 missed their predicted gain by more than half (|rho - 1| > 1/2):
                 at that scale the march's thrust is not smooth (its discrete
                 decisions -- which column a wall foot falls in, how many cells a
                 column has -- make steps of the order of the reported mismatch),
                 so a smaller step cannot be graded; refine the grid for more
                 precision (measured 2026-10-08 on the bell engine at (41,120):
                 steps of ~0.2 ppm, the walk kept "climbing" them);
      BUDGET     max_segments trials.
  - a start outside the fold class first maximises the margin with the same
    machinery (restoration), then switches to J at the first in-class point.
The answer is the best certified (in-class) point, never the last trial.

QNTR_TOL (default 1e-8): the relative gain below which a further move is not worth
a march -- one decade under the smallest difference this campaign reads (1e-7),
two under the march's discretisation error (~1e-6). It is a statement about the
precision wanted, the same for every case.
"""
import os
import time

import numpy as np

TOL = float(os.environ.get("QNTR_TOL", "1e-8"))
LAST = {}          # the last walk's report (stop reason, predicted gain, counts)


def _sym_floor(H, rel=1e-10):
    """Symmetrise and replace eigenvalues by their absolute values, floored."""
    H = 0.5 * (H + H.T)
    lam, V = np.linalg.eigh(H)
    a = np.abs(lam)
    fl = rel * a.max() if a.max() > 0.0 else 1.0
    return (V * np.maximum(a, fl)) @ V.T, lam


def _bfgs(B, s, y):
    """Damped BFGS (Powell) update of B, the curvature of the MINIMISED function."""
    Bs = B @ s
    sBs = float(s @ Bs)
    sy = float(s @ y)
    if not (np.isfinite(sBs) and np.isfinite(sy)) or sBs <= 0.0:
        return B, False
    if sy < 0.2 * sBs:
        th = 0.8 * sBs / (sBs - sy)
        r = th * y + (1.0 - th) * Bs
    else:
        r = y
    sr = float(s @ r)
    if sr <= 0.0:
        return B, False
    return B - np.outer(Bs, Bs) / sBs + np.outer(r, r) / sr, sy < 0.2 * sBs


def tr_step(g, B, delta, lin=None, lb=None, ub=None):
    """argmax g.d - 1/2 d.B.d over |d| <= delta [, a + b.d >= 0] [, lb <= d <= ub];
    B symmetric positive definite. Unconstrained part exact (eigen-decomposition +
    bisection on the shift); with the class or bounds active, SLSQP on the model in
    variables scaled by delta (the model is cheap: no march)."""
    lam, V = np.linalg.eigh(B)
    gq = V.T @ g

    def d_of(mu):
        return V @ (gq / (lam + mu))

    d = d_of(0.0)
    if np.isfinite(delta) and np.linalg.norm(d) > delta:
        lo, hi = 0.0, float(np.linalg.norm(g)) / delta
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if np.linalg.norm(d_of(mid)) > delta:
                lo = mid
            else:
                hi = mid
        d = d_of(hi)
    ok = True
    if lin is not None:
        ok = ok and lin[0] + float(lin[1] @ d) >= 0.0
    if lb is not None:
        ok = ok and bool(np.all(d >= lb) and np.all(d <= ub))
    if ok:
        return d
    from scipy.optimize import minimize
    sc = delta if np.isfinite(delta) else max(float(np.linalg.norm(d)), 1e-300)
    gs = g * sc
    Bs_ = B * sc * sc
    f0 = max(float(np.linalg.norm(gs)), 1e-300)
    cons = []
    if np.isfinite(delta):
        cons.append(dict(type="ineq", fun=lambda u: 1.0 - u @ u, jac=lambda u: -2.0 * u))
    if lin is not None:
        a, b = float(lin[0]), np.asarray(lin[1], float) * sc
        nb = max(float(np.linalg.norm(b)), 1e-300)
        cons.append(dict(type="ineq", fun=lambda u: (a + b @ u) / nb, jac=lambda u: b / nb))
    bnds = None if lb is None else list(zip(np.asarray(lb) / sc, np.asarray(ub) / sc))
    u0 = np.zeros(len(g))
    if lin is not None and lin[0] < 0.0:
        # the linearised class excludes 0: start on its boundary, nearest point
        u0 = -(a / (b @ b)) * b
    r = minimize(lambda u: (-(gs @ u) + 0.5 * u @ Bs_ @ u) / f0, u0,
                 jac=lambda u: (-gs + Bs_ @ u) / f0, method="SLSQP", constraints=cons,
                 bounds=bnds, options=dict(ftol=1e-14, maxiter=1000))
    return np.asarray(r.x, float) * sc


def model_gain(g, B, d):
    return float(g @ d - 0.5 * d @ B @ d)


class Walk:
    """The driver on three hooks: record(W) -> (out, sched) [raises on failure],
    jg(W, sched) -> (J, grad) on that frozen schedule, mg(W, sched) -> (m, grad m)
    (class margin minus its floor; only with a margin)."""

    def __init__(self, record, jg, mg=None, mtol=0.0, sign=1.0, verbose=1, say=print):
        self.record, self.jg, self.mg = record, jg, mg
        self.mtol, self.sign, self.verbose, self.say = float(mtol), float(sign), verbose, say
        self.n_rec = 0
        self.n_grad = 0
        self.t_rec = self.t_grad = self.t_sec = 0.0       # wall time of marches, gradients, secant Hessians

    def evaluate(self, W):
        W = np.asarray(W, float)
        t0 = time.time()
        try:
            out, sched = self.record(W)
        except Exception as err:                                  # noqa: BLE001
            self.t_rec += time.time() - t0
            return None, "record failed (%s)" % str(err)[:120]
        self.t_rec += time.time() - t0
        self.n_rec += 1
        cw = float(out["cert_worst"])
        if not cw <= 1.0:
            return None, "not certified (worst %.3e)" % cw
        t0 = time.time()
        J, g = self.jg(W, sched)
        self.t_grad += time.time() - t0
        self.n_grad += 1
        g = np.asarray(g, float)
        if not (np.isfinite(J) and np.all(np.isfinite(g))):
            return None, "non-finite J or gradient"
        pt = dict(W=W, J=float(J), g=g, cert=cw, out=out, sched=sched, m=None, gm=None)
        if self.mg is not None:
            m, gm = self.mg(W, sched)
            gm = np.asarray(gm, float)
            pt["m"] = float(m) if np.isfinite(m) else -np.inf
            pt["gm"] = np.where(np.isfinite(gm), gm, 0.0)
        return pt, None

    def secant(self, pt, h, which="J"):
        """Secant Hessian of J (or of the margin) on pt's frozen schedule, central at
        +-h; columns with a non-finite gradient are reported and left out."""
        W, n = pt["W"], len(pt["W"])
        H = np.zeros((n, n))
        bad = []
        t0 = time.time()
        f = self.jg if which == "J" else self.mg
        for j in range(n):
            e = np.zeros(n)
            e[j] = h
            gp = np.asarray(f(W + e, pt["sched"])[1], float)
            gm_ = np.asarray(f(W - e, pt["sched"])[1], float)
            self.n_grad += 2
            col = (gp - gm_) / (2.0 * h)
            if np.all(np.isfinite(col)):
                H[:, j] = col
            else:
                bad.append(j)
        self.t_sec += time.time() - t0
        return H, bad

    def curvature(self, pt, h, which="J"):
        """B = |secant Hessian of the minimised function|, floored; columns that
        could not be measured get the median measured diagonal (and no coupling)."""
        H, bad = self.secant(pt, h, which)
        sg = self.sign if which == "J" else 1.0
        Hm = -sg * H
        good = [j for j in range(len(Hm)) if j not in bad]
        if not good:
            gn = float(np.linalg.norm(pt["g"] if which == "J" else pt["gm"]))
            return np.eye(len(Hm)) * max(gn / max(h * 100.0, 1e-300), 1e-300), bad, None
        Hm = 0.5 * (Hm + Hm.T)
        dmed = float(np.median(np.abs(np.diag(Hm)[good])))
        for j in bad:
            Hm[j, :] = 0.0
            Hm[:, j] = 0.0
            Hm[j, j] = dmed
        B, lam = _sym_floor(Hm)
        return B, bad, lam

    def run(self, W0, max_segments=100, tr0=0.05, bounds=None, on_segment=None, h=None):
        t0 = time.time()
        say, sg = self.say, self.sign
        lb = ub = None
        if bounds is not None:
            lb = np.asarray(getattr(bounds, "lb", [b[0] for b in bounds]), float)
            ub = np.asarray(getattr(bounds, "ub", [b[1] for b in bounds]), float)
        base, why = self.evaluate(W0)
        if base is None:
            raise RuntimeError("QNTR: the start cannot be marched: %s" % why)
        scale = max(1.0, float(np.max(np.abs(base["W"]))))
        dmin = 1e-8 * scale
        h = (1e-2 * tr0) if h is None else h
        phase = 1 if (self.mg is not None and base["m"] < 0.0) else 2
        rep = dict(stop=None, segments=0, accepted=0, rejected=0, secants=0, damped=0,
                   phase1_segments=0, log=[])
        if phase == 2:
            B, bad, lam = self.curvature(base, h)
            rep["secants"] += 1
            if self.verbose:
                lo_, hi_ = (float(np.min(lam)), float(np.max(lam))) if lam is not None else (0.0, 0.0)
                say("    [qntr] start: J %.10e, secant Hessian at h %.2e (%d columns unmeasurable %s);"
                    " eigenvalues of -H in [%.3e, %.3e]" % (base["J"], h, len(bad), bad, lo_, hi_))
        else:
            B = None
        Bm = np.eye(len(base["W"])) * max(float(np.linalg.norm(base["gm"])) / tr0, 1e-300) if self.mg else None
        best = base if phase == 2 else None
        rest = base if phase == 1 else None
        hist = [] if phase == 1 else [(0, base["J"], float(np.linalg.norm(base["g"])), base["cert"])]
        delta = float(tr0)
        refreshed_at = None
        smax, n_err, mism = 0.0, 0, []          # longest accepted step; erratic trials in a row; their mismatches
        for seg in range(max_segments):
            rep["segments"] = seg + 1
            if on_segment is not None:
                on_segment(seg, None if best is None else best["W"], delta)
            if phase == 1:
                gv, Bc, lin = base["gm"], Bm, None
            else:
                gv, Bc = sg * base["g"], B
                lin = None if self.mg is None else (base["m"] + self.mtol, base["gm"])
            rl = None if lb is None else (lb - base["W"], ub - base["W"])
            # the gain the model still predicts at this point, no radius
            dN = tr_step(gv, Bc, np.inf, lin, *(rl if rl else (None, None)))
            gainN = model_gain(gv, Bc, dN)
            if phase == 2 and gainN < TOL * abs(base["J"]):
                if refreshed_at is not base:
                    B, bad, lam = self.curvature(base, h)
                    rep["secants"] += 1
                    refreshed_at = base
                    dN = tr_step(gv, B, np.inf, lin, *(rl if rl else (None, None)))
                    g2 = model_gain(gv, B, dN)
                    if self.verbose:
                        say("    [qntr %2d] predicted gain %.3e |J| under %.0e: secant Hessian measured here"
                            " (%d columns unmeasurable) -> predicted gain %.3e |J|"
                            % (seg, gainN / abs(base["J"]), TOL, len(bad), g2 / abs(base["J"])))
                    gainN = g2
                    Bc = B
                if gainN < TOL * abs(base["J"]):
                    rep["stop"] = "CONVERGED"
                    break
            d = tr_step(gv, Bc, delta, lin, *(rl if rl else (None, None)))
            pred = model_gain(gv, Bc, d)
            dn = float(np.linalg.norm(d))
            trial, why = self.evaluate(base["W"] + d)
            row = dict(seg=seg, phase=phase, J=base["J"], delta=delta, step=dn, pred=pred,
                       gainN=gainN, m=base["m"])
            if trial is None:
                rep["rejected"] += 1
                delta = 0.25 * dn
                row.update(result="fail: " + why)
                rep["log"].append(row)
                if self.verbose:
                    say("    [qntr %2d] step %.3e: %s -> radius %.3e" % (seg, dn, why, delta))
                if delta < dmin:
                    rep["stop"] = "RESOLUTION" if phase == 2 else "NOT RESTORABLE"
                    break
                continue
            s = trial["W"] - base["W"]
            if phase == 2 or self.mg is None:
                B, dmp = _bfgs(B, s, -sg * (trial["g"] - base["g"])) if B is not None else (None, False)
                rep["damped"] += int(dmp)
            if self.mg is not None:
                Bm, _ = _bfgs(Bm, s, -(trial["gm"] - base["gm"]))
            if phase == 1:
                ared = trial["m"] - base["m"]
                feas = True
            else:
                ared = sg * (trial["J"] - base["J"])
                feas = self.mg is None or trial["m"] >= -self.mtol
            rho = ared / pred if pred > 0.0 else -1.0
            if not feas:
                rho = -1.0
            row.update(Jt=trial["J"], ared=ared, rho=rho, mt=trial["m"])
            if ared > 0.0 and feas:
                rep["accepted"] += 1
                rep.setdefault("accepted_W", []).append(np.asarray(trial["W"], float).tolist())
                base = trial
                row.update(result="accept")
                if phase == 1:
                    rest = base
                    rep["phase1_segments"] = seg + 1
                    if base["m"] >= 0.0:
                        phase = 2
                        B, bad, lam = self.curvature(base, h)
                        rep["secants"] += 1
                        best = base
                        hist.append((seg + 1, base["J"], float(np.linalg.norm(base["g"])), base["cert"]))
                        if self.verbose:
                            say("    [qntr %2d] restoration done: in class (m %+.4e); J %.10e" %
                                (seg, base["m"], base["J"]))
                else:
                    best = base
                    hist.append((seg + 1, base["J"], float(np.linalg.norm(base["g"])), base["cert"]))
            else:
                rep["rejected"] += 1
                row.update(result="reject" + ("" if feas else " (out of class)"))
                rep["last_reject"] = dict(W=np.asarray(trial["W"], float).tolist(), J=float(trial["J"]),
                                          base_W=np.asarray(base["W"], float).tolist(), base_J=float(base["J"]),
                                          pred=float(pred))
            erratic = smax > 0.0 and dn < 0.1 * smax and abs(rho - 1.0) > 0.5
            if erratic:
                n_err += 1
                mism.append(abs(ared - pred))
            else:
                n_err = 0
            if row["result"] == "accept":
                smax = max(smax, dn)
            if rho < 0.25:
                delta = 0.25 * dn
            elif rho > 0.75 and dn >= 0.99 * delta:
                delta = min(2.0 * delta, 100.0 * tr0)
            rep["log"].append(row)
            if self.verbose:
                say("    [qntr %2d] %s J %.10e  step %.3e/%.3e  pred %.3e ared %.3e rho %+.2f"
                    "  remaining(model) %.2e|J|%s -> radius %.3e"
                    % (seg, "R" if phase == 1 else " ", trial["J"], dn, row["delta"], pred, ared, rho,
                       gainN / abs(base["J"]),
                       ("" if self.mg is None else "  m %+.3e" % trial["m"]), delta)
                    + ("" if row["result"] == "accept" else "  [%s]" % row["result"]))
            if delta < dmin:
                rep["stop"] = "RESOLUTION" if phase == 2 else "NOT RESTORABLE"
                break
            if phase == 2 and n_err >= 5:
                rep["stop"] = "RESOLUTION"
                rep["nonsmooth"] = float(np.median(mism[-5:]) / abs(base["J"]))
                if self.verbose:
                    say("    [qntr %2d] five short trials in a row missed their prediction by more than half: the"
                        " march's thrust is not smooth at this scale (steps ~%.1e |J|) -> resolution of this grid"
                        % (seg, rep["nonsmooth"]))
                break
        else:
            rep["stop"] = "BUDGET"
        land = best if best is not None else rest
        rep.update(J=land["J"], grad_inf=float(np.max(np.abs(land["g"]))), gain_pred=gainN,
                   gain_pred_rel=gainN / abs(land["J"]), records=self.n_rec, gradients=self.n_grad,
                   seconds=time.time() - t0, in_class=(best is not None), tol=TOL,
                   t_records=self.t_rec, t_gradients=self.t_grad, t_secant=self.t_sec)
        LAST.clear()
        LAST.update(rep)
        if self.verbose:
            say("    [qntr] STOP %s after %d trials (%d accepted, %d rejected, %d secant Hessians,"
                " %d records): J %.10e, predicted remaining gain %.2e |J|, |grad|inf %.3e, %.0f s"
                " (marches %.0f s, gradients %.0f s, secant Hessians %.0f s)"
                % (rep["stop"], rep["segments"], rep["accepted"], rep["rejected"], rep["secants"],
                   self.n_rec, land["J"], rep["gain_pred_rel"], rep["grad_inf"], rep["seconds"],
                   self.t_rec, self.t_grad, self.t_sec))
        return land["W"], hist, self.n_rec
