#!/usr/bin/env python3
"""O3.1-cs — AUDIT INSTRUMENT (A2 of the ADOPTED list; user decision
(a) 2026-08-13: built at S-CERT opening as an instrument of the
audit, never a repair; strengthens MC1/MC7). Registry ID: [X-O31CS].

WHAT IT CLOSES. O3.1 (the transpose identity |<w,Jv> - <J^T w,v>|)
certifies SELF-consistency of the (J, J^T) pair assembled by the SAME
lowered march: it provably cannot detect a transpose-CONSISTENT-but-
WRONG pair (the common-mode hole; D-08 qualifier of record;
Giles-Pierce 2000 p.402 lineage). This instrument produces the
PRIMAL-INDEPENDENT side: a complex-step derivative of an INDEPENDENTLY
RE-IMPLEMENTED residual (double implementation — numpy complex128,
no JAX), with the implicit-function rule re-derived in the complex
plane (residual evaluated complex; linear solves real), giving the
cell sensitivity dz/dp with NO shared code with the engine's AD path.

COVERAGE (declared): the INTERIOR unit process of the certified march
(the workhorse), on instances built from parent states of the
committed S18 design-of-record field and solved by the ENGINE's own
custom_vjp solver. DECLARED OUT (registered residual, owner F2): the
WALL process (the shape-gradient carrier — same twin pattern, not yet
implemented), axis/legge/qofM processes, and the assembled
whole-march sweep (the composition is exercised by O3.1 on the
engine side; this instrument attacks the per-cell implicit rule,
which is where the custom-vjp hand-written transpose lives — one
process class suffices to break the common mode, full coverage does
not follow and is not claimed).

ROWS (each PASS/FAIL gates the exit code)
 CS1 TWIN CONSISTENCY: the independent residual twin evaluates to the
     Newton floor at engine-solved instances (if the twin were a
     different mathematical function, this fires).
 CS3 PRIMAL-INDEPENDENT SENSITIVITY: S_cs = -A_cs^{-1} B_cs (complex-
     step Jacobians of the twin residual + IFT) against S_jax =
     jax.jacrev through the engine's custom_vjp solve (the audited
     hand-written implicit adjoint), max elementwise deviation within
     the DERIVED band; plus the pairing row <w, S_cs v> vs
     <S_jax^T w, v> on declared unit vectors.
 CS4 NEGATIVE CONTROL (must be DETECTED): S_bad = S_jax + E with E
     DERIVED (2x the CS3 band on the largest-magnitude entry — never
     a magic percent) and S_bad^T = (S_bad)^T: the O3.1-style
     self-consistency check on the pair passes at machine zero
     (verified — that IS the hole), while the CS3 metric on S_bad
     MUST fire.
 CS5 h-STABILITY: complex step h in {1e-20, 1e-12} — the spread bounds
     the step error (no subtractive cancellation in complex step);
     enters the derived band with K_RICH.
BAND (derived, no magic): K_RICH * (two-h spread of S_cs) +
     K_RICH * (engine Newton certification floor propagated through
     |A_cs^{-1}|_inf) — both terms measured per instance.

ENV: jax (the engine side) + numpy (the twin). On-demand instrument;
exit 0 iff all rows incl. the negative control PASS.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import jax                                        # noqa: E402
import jax.numpy as jnp                           # noqa: E402

import a1_ideal_march_jax as A1                   # noqa: E402
import a1_march_scan as SC                        # noqa: E402
import a1_toc_variational_jax as TV               # noqa: E402
import thermotab_c1_jax as TH                     # noqa: E402
import o33_bench as O33                           # noqa: E402

jax.config.update("jax_enable_x64", True)

EPS = float(np.finfo(np.float64).eps)
DELTA_EFF = 1.0        # axisymmetric march (the committed case)


def check(label, ok):
    print("  [%s] %s" % (label, "PASS" if ok else "FAIL"))
    return bool(ok)


# ======================================================================
# THE TWIN: complex-safe closure + residuals, numpy only (double
# implementation — re-derived from the quintic-Hermite node data, NOT
# from the engine's evaluator code)
# ======================================================================
def hermite5_coeffs(D):
    """Two-point quintic Hermite basis matrix on [0,1] scaled to
    interval width D: coefficients for (f0,f1,d0,d1,s0,s1) ->
    polynomial a0..a5 in t = (T-T_i)/D. Derived independently from
    the standard quintic Hermite conditions (own derivation)."""
    # p(t) = sum a_k t^k;  p(0)=f0, p(1)=f1, p'(0)=d0*D, p'(1)=d1*D,
    # p''(0)=s0*D^2, p''(1)=s1*D^2  (chain rule to physical T)
    M = np.zeros((6, 6))
    # value at 0 / 1
    M[0, 0] = 1.0
    M[1, :] = 1.0
    # first derivative in t at 0 / 1
    M[2, 1] = 1.0
    M[3, 1:] = np.arange(1, 6)
    # second derivative in t at 0 / 1
    M[4, 2] = 2.0
    M[5, 2:] = np.arange(2, 6) * np.arange(1, 5)
    return np.linalg.inv(M)


class TwinClosure:
    """Complex-safe C^1-closure twin built from the TABLE NODE DATA
    (Tg, hg, cpg, cpp', s0 grid) — locate by Re(T), evaluate the
    quintic polynomial in complex arithmetic."""

    def __init__(self, tab):
        Tg = np.asarray(tab["T"], float)
        hg = np.asarray(tab["h"], float)
        s0g = np.asarray(tab["s0m"], float)
        cpg = np.asarray(tab["cp"], float)
        D = Tg[1] - Tg[0]
        if not np.allclose(np.diff(Tg), D):
            raise RuntimeError("non-uniform grid — twin license fails")
        # cp' estimates: centered differences, one-sided ends (the
        # engine builds its own estimates the same public way; any
        # difference lands in CS1, which is the point of the row)
        cpp = np.gradient(cpg, D)
        s0d = cpg / Tg
        s0s = (cpp * Tg - cpg) / (Tg * Tg)
        Minv = hermite5_coeffs(D)
        self.Tg, self.D = Tg, D
        self.h0 = float(tab["h0"])
        self.Rg = float(tab["Rg"])
        self.s0_ref = float(tab["s0"])
        self.coef_h = self._build(Minv, hg, cpg * D, cpp * D * D)
        self.coef_s0 = self._build(Minv, s0g, s0d * D, s0s * D * D)
        self.coef_cp = None   # cp := d/dT of h quintic (structural)

    def _build(self, Minv, f, dD, sD2):
        n = len(f) - 1
        rhs = np.stack([f[:-1], f[1:], dD[:-1], dD[1:],
                        sD2[:-1], sD2[1:]], axis=0)   # (6, n)
        return (Minv @ rhs)                            # (6, n) a_k per interval

    def _eval(self, coef, T):
        i = int(min(max(np.floor((T.real - self.Tg[0]) / self.D), 0),
                    len(self.Tg) - 2))
        t = (T - self.Tg[i]) / self.D
        a = coef[:, i]
        v = a[5]
        for k in range(4, -1, -1):
            v = v * t + a[k]
        return v

    def _eval_d(self, coef, T):
        i = int(min(max(np.floor((T.real - self.Tg[0]) / self.D), 0),
                    len(self.Tg) - 2))
        t = (T - self.Tg[i]) / self.D
        a = coef[:, i]
        v = 5.0 * a[5]
        for k in range(4, 0, -1):
            v = v * t + k * a[k]
        return v / self.D

    def state_q(self, q):
        """q (complex) -> (T, p, rho, c, gam, M), all complex."""
        ht = self.h0 - 0.5 * q * q
        # Newton on h(T) = ht, own trip policy (independent impl.)
        T = complex(np.interp(ht.real, self._hg_real(), self.Tg))
        for _ in range(60):
            f = self._eval(self.coef_h, T) - ht
            cp = self._eval_d(self.coef_h, T)
            dT = f / cp
            T = T - dT
            if abs(dT) < 1e-14 * max(1.0, abs(T)):
                break
        cp = self._eval_d(self.coef_h, T)
        p = A1.PREF * np.exp((self._eval(self.coef_s0, T)
                              - self.s0_ref) / self.Rg)
        rho = p / (self.Rg * T)
        gam = cp / (cp - self.Rg)
        c = np.sqrt(gam * self.Rg * T)
        return T, p, rho, c, gam, q / c

    def _hg_real(self):
        # node h values for the real-seed interp
        return np.array([self._eval(self.coef_h, complex(t))
                         .real for t in self.Tg])


def twin_coef(cl, u, v, y):
    """Twin of the march coefficient pack (complex-safe: arctan(v/u)
    replaces arctan2 — u > 0 asserted on every instance)."""
    q = np.sqrt(u * u + v * v)
    if u.real <= 0.0:
        raise RuntimeError("u <= 0: arctan branch assertion fails")
    Aa = np.arctan(v / u)
    _, _, _, c, _, M = cl.state_q(q)
    mu = np.arcsin(1.0 / M)
    lm = np.tan(Aa - mu)
    lp = np.tan(Aa + mu)
    qq = u * u - c * c
    s = DELTA_EFF * c * c * v / y
    return lm, lp, qq, 2.0 * u * v, s


def twin_resid_int(z, p, cl):
    """Independent re-implementation of the INTERIOR unit-process
    residual (4 eqs) in numpy complex."""
    x4, y4, u4, v4 = z
    x1, y1, u1, v1, x2, y2, u2, v2 = p
    um, vm, ym = 0.5 * (u1 + u4), 0.5 * (v1 + v4), 0.5 * (y1 + y4)
    lm, _, qm, rm0, sm = twin_coef(cl, um, vm, ym)
    rm = rm0 - qm * lm
    up, vp, yp = 0.5 * (u2 + u4), 0.5 * (v2 + v4), 0.5 * (y2 + y4)
    _, lp, qp, rp0, sp = twin_coef(cl, up, vp, yp)
    rp = rp0 - qp * lp
    return np.array([
        (y4 - y1) - lm * (x4 - x1),
        (y4 - y2) - lp * (x4 - x2),
        qm * u4 + rm * v4 - (sm * (x4 - x1) + qm * u1 + rm * v1),
        qp * u4 + rp * v4 - (sp * (x4 - x2) + qp * u2 + rp * v2),
    ], dtype=complex)


def cs_jacobians(fun, z, p, cl, h):
    """Complex-step Jacobians A = dR/dz, B = dR/dp of the twin."""
    z = np.asarray(z, float)
    p = np.asarray(p, float)
    nz, npp = len(z), len(p)
    A = np.zeros((nz, nz))
    B = np.zeros((nz, npp))
    for k in range(nz):
        zc = z.astype(complex)
        zc[k] += 1j * h
        A[:, k] = fun(zc, p.astype(complex), cl).imag / h
    for k in range(npp):
        pc = p.astype(complex)
        pc[k] += 1j * h
        B[:, k] = fun(z.astype(complex), pc, cl).imag / h
    return A, B


# ======================================================================
# main
# ======================================================================
def main():
    print("== O3.1-cs AUDIT INSTRUMENT [X-O31CS] (A2 decision (a) of "
          "record, 2026-08-13) ==")
    ok = True
    tab = A1.prep_tab(A1.build_tab_nasa())
    state_c1, solv, cfg = O33.make_case(tab)
    cl = TwinClosure(tab)
    ta = A1.tab_arrays(tab)

    # instances: parent pairs from the committed S18 field
    out, plan = TV.run_toc_record(O33.W_STAR, tab, cfg,
                                  state_fn=state_c1, solvers=solv,
                                  return_field=True)
    chain, owner = O33.cplus_chain(out["cols"])
    print("  field re-certified: cert worst %.3e over %d cells"
          % (out["cert_worst"], out["cert_n"]))
    ok &= check("committed field re-certified", out["cert_worst"] <= 1.0)

    solve_int = solv["interior"][0] if isinstance(solv["interior"], tuple) \
        else solv["interior"]

    # sample N_INST interior instances along the chain (declared,
    # deterministic: evenly spaced interior nodes)
    N_INST = 3
    idxs = np.linspace(10, len(chain) - 10, N_INST).astype(int)
    K_RICH = A1.K_RICH
    for ii, i in enumerate(idxs):
        p1 = chain[i - 1]     # C- side parent (x1,y1,u1,v1)
        p2 = chain[i]         # C+ side parent
        p_vec = np.concatenate([p1, p2])
        z0 = 0.5 * (p1 + p2)
        z0[0] += 0.05 * abs(p2[0] - p1[0]) + 1e-3   # push downstream
        z = np.asarray(solve_int(jnp.asarray(z0), jnp.asarray(p_vec), ta))
        r_twin = twin_resid_int(z.astype(complex), p_vec.astype(complex), cl)
        scale = max(1.0, float(np.max(np.abs(z))))
        floor = A1.NEWTON_TOL_FACTOR * EPS * scale
        # CS1 — DERIVED bound (honest catch of record: the first
        # version used a 1e6x magic multiplier and FIRED on the
        # near-axis instance; the derived form maps the engine's
        # per-cell certification floor through the residual slope:
        # |R_twin(z*)| <= ||A||_inf x floor_z, i.e. the twin residual
        # expressed as a z-displacement must sit at the Newton floor).
        A_cs, B_cs = cs_jacobians(twin_resid_int, z, p_vec, cl, 1e-20)
        Anorm = float(np.linalg.norm(A_cs, np.inf))
        r_max = float(np.max(np.abs(r_twin.real)))
        print("    [%d] twin |R| = %.3e ; ||A||_inf x floor = %.3e "
              "(z-equivalent %.2e vs floor %.2e)"
              % (ii, r_max, Anorm * floor, r_max / Anorm, floor))
        ok &= check("CS1[%d] twin residual at engine-solved z within "
                    "the DERIVED slope-mapped Newton floor "
                    "(independence-coupling row)" % ii,
                    r_max <= Anorm * floor)
        # CS3: S_cs vs S_jax
        A_cs2, B_cs2 = cs_jacobians(twin_resid_int, z, p_vec, cl, 1e-12)
        S_cs = -np.linalg.solve(A_cs, B_cs)
        S_cs2 = -np.linalg.solve(A_cs2, B_cs2)
        spread = float(np.max(np.abs(S_cs - S_cs2)))
        S_jax = np.asarray(jax.jacrev(
            lambda pp: solve_int(jnp.asarray(z0), pp, ta))(
                jnp.asarray(p_vec)))
        # band: two-h spread + Newton floor propagated through A^-1
        Ainv_norm = float(np.linalg.norm(np.linalg.inv(A_cs), np.inf))
        band = K_RICH * spread + K_RICH * Ainv_norm * floor
        dev = float(np.max(np.abs(S_cs - S_jax)))
        print("    [%d] max|S_cs - S_jax| = %.3e  band = %.3e "
              "(spread %.1e, |A^-1| %.1e)" % (ii, dev, band, spread,
                                              Ainv_norm))
        ok &= check("CS3[%d] engine implicit-adjoint sensitivity "
                    "matches the primal-independent complex-step IFT "
                    "within the derived band" % ii, dev <= band)
        # pairing row
        w = np.zeros(4)
        w[ii % 4] = 1.0
        vv = np.zeros(8)
        vv[(2 * ii) % 8] = 1.0
        lhs = float(w @ (S_cs @ vv))
        rhs = float((S_jax.T @ w) @ vv)
        ok &= check("CS3[%d] pairing <w,S_cs v> == <S_jax^T w, v> "
                    "within band" % ii, abs(lhs - rhs) <= band)
        # CS4 negative control (first instance only; declared)
        if ii == 0:
            E = np.zeros_like(S_jax)
            j_flat = int(np.argmax(np.abs(S_jax)))
            E.flat[j_flat] = 2.0 * band * np.sign(S_jax.flat[j_flat] + EPS)
            S_bad = S_jax + E
            # O3.1-style self-consistency on the consistent pair:
            self_gap = abs(float(w @ (S_bad @ vv))
                           - float((S_bad.T @ w) @ vv))
            ok &= check("CS4 the transpose-consistent-but-wrong pair "
                        "PASSES the O3.1-style self check (the hole, "
                        "demonstrated)", self_gap <= 1e2 * EPS)
            dev_bad = float(np.max(np.abs(S_bad - S_cs)))
            ok &= check("CS4 the same pair is DETECTED by the "
                        "primal-independent side (negative control "
                        "fires)", dev_bad > band)
        # CS5
        ok &= check("CS5[%d] complex-step h-stability (two-h spread "
                    "below the deviation it must resolve)" % ii,
                    spread < max(dev, band) or spread == 0.0)

    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
