"""[X-VMON] (G)/Lambda-form validity monitor + gamma=1.4 KAT vs
Rao-Beck Eq. (4) (S21, F0 of plan v3 — the Eq.(4)/Sternin monitor
ARMED per the F0 exit gate; panel S4 THEOREM's evidence half).

WHAT THIS IS. The general validity boundary of the Rao control-
surface march (ADVISORY_def_equivalence_proof, ratified S21 into M0):

    (G)  val = [Lam*B*(A+B) - (A-B)] / [1 + Lam*(A+B)],
         A = tan(theta - alpha), B = tan(alpha),
         Lam = V * d(alpha)/dV along the isentrope,

with val > 0 the VALID side (Rao-Beck Fig. 2 orientation; GENO
Rao_m.f90 boundaryfunction_solve). For a PERFECT GAS,
Lam_pg = -(gamma - cos 2alpha)/sin 2alpha and the zero set of val is
EXACTLY Rao-Beck Eq. (4) — the S4 THEOREM (hand proof + judge
re-derivation); the algebraic identity behind it is

    N := Lam*B*(A+B) - (A-B) == -tan(alpha) * E4,
    E4 := ((gamma - cos 2alpha)/sin 2alpha) * sin(theta) /
          (cos(theta-alpha) cos(alpha)) + tan(theta-alpha)/tan(alpha)
          - 1                     [Eq. (4) as a residual],

which this carrier verifies MACHINE-LEVEL on a grid (KAT-A), then
verifies the BACKEND route (Lam by AD through OUR tabulated closure
on a synthetic gamma=1.4 table) against the closed form (KAT-B) with
a DERIVED two-resolution band. SCOPE BOUNDS OF RECORD (panel S4,
both adopted): (a) EOS-GENERAL but NOT DATA-GENERAL — valid on
homentropic-homoenergetic (single-isentrope alpha = alpha(V)) data
only, per the periodic-wave scoping; entropy/h0-gradient flows need
the F2 extended margin; (b) implementation magics of the GENO
reference (dV_pert = 1.0, |den| < 1e-10 guard, PM landing window)
are NOT adopted here — Lam comes from AD (exact to the table), and
the den-guard is replaced by reporting the denominator itself.

CONVENTION TRAP OF RECORD (Rao-vs-Zucrow): Rao 1958/Rao-Beck name
the LEFT-running characteristic C+ where Zucrow-Hoffman/GENO name it
C- (family naming INVERTED); the control surface called "the C+
traced back from the lip" in this repo is Rao's left-Mach-line DE.
The (G) form is family-symmetric in (theta, alpha) as written here
(bell branch, theta -/+ alpha per this repo's convention); the plug
C- mirror (boundaryfunction_cminus_solve) is UNPROVEN (panel scope
limit) and NOT covered by this carrier.

MONITOR (ARMED, default not consumed — the F0 gate arms it; F1
consumes it along the walk): surface_min_val(q, theta, ta) returns
per-node val from the AD Lambda plus (min val, argmin index) — the
argmin-margin locus the O4 logs require. THE VERDICT FORM for any
consumption is the THREE-WAY DECISION TABLE of
ADVISORY_claims_to_code C-1 (each row can fire):
 (a) min-val locus AND cert-failing cell within the stencil radius
     of the terminal C+ chain -> DEF-signature reading CONFIRMED;
 (b) min-val locus INTERIOR (upstream, inside the wall's domain of
     dependence) -> INTERIOR CAUSTIC: the DEF reading for S20 is
     FALSIFIED, the design belongs to tier-1 evaluation;
 (c) val healthy at the failing cell yet Newton stalls -> NON-FOLD
     mechanism (class construction, not physics): both readings
     falsified.
The K_disc ~ A_0 bridge stays CONJECTURE (M0 Part VI); this monitor
IS its named falsifier (val must approach 0 where certification
degrades, else the bridge is dead).

TOLERANCES — DERIVED (R5): KAT-A gate = C_OPS * eps * (local term
scale) per grid point (pure-roundoff identity, no free constant);
KAT-B gate = K_RICH * |Lam_AD(N_TAB) - Lam_AD(N_TAB/2)| + the KAT-A
floor (two-resolution table-interpolation band). Rejectors: a
corrupted gamma (KAT-A) and a corrupted table (KAT-B) must exceed
their bands; the Fig.-2 sign spot checks must reproduce.

On-demand carrier (env: jax).
"""
import os
import sys

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1   # noqa: E402

EPS = float(jnp.finfo(jnp.float64).eps)
d2r = np.pi / 180.0


def check(label, cond):
    print("  [%s] %s" % ("PASS" if cond else "FAIL", label))
    return bool(cond)


def val_G(theta, alpha, Lam):
    """(G) validity function, GENO Rao_m form; also returns den."""
    A = jnp.tan(theta - alpha)
    B = jnp.tan(alpha)
    den = 1.0 + Lam * (A + B)
    return (Lam * B * (A + B) - (A - B)) / den, den


def lambda_pg(gamma, alpha):
    return -(gamma - jnp.cos(2.0 * alpha)) / jnp.sin(2.0 * alpha)


def eq4_residual(gamma, theta, alpha):
    """Rao-Beck Eq. (4) as a residual (LHS - 1), page-verified form."""
    return ((gamma - jnp.cos(2.0 * alpha)) / jnp.sin(2.0 * alpha)
            * jnp.sin(theta)
            / (jnp.cos(theta - alpha) * jnp.cos(alpha))
            + jnp.tan(theta - alpha) / jnp.tan(alpha) - 1.0)


def lambda_backend(q, ta):
    """Lam = V d(alpha)/dV by AD through OUR tabulated closure
    (EOS-general; the monitor's production route)."""
    def alpha_of(qq):
        c = A1.state_q(qq, ta)[3]
        return jnp.arcsin(c / qq)
    return q * jax.grad(alpha_of)(q)


def surface_min_val(q_nodes, theta_nodes, ta):
    """ARMED monitor: per-node val with the AD Lambda; returns
    (val array, den array, argmin index). Consumption = the C-1
    three-way table (docstring)."""
    vals, dens = [], []
    for q, th in zip(np.asarray(q_nodes), np.asarray(theta_nodes)):
        c = float(A1.state_q(jnp.float64(q), ta)[3])
        al = float(np.arcsin(min(1.0, c / q)))
        lam = float(lambda_backend(jnp.float64(q), ta))
        v, d = val_G(jnp.float64(th), jnp.float64(al),
                     jnp.float64(lam))
        vals.append(float(v))
        dens.append(float(d))
    vals = np.asarray(vals)
    return vals, np.asarray(dens), int(np.argmin(vals))


def main():
    print("== [X-VMON] (G)/Lambda-form validity monitor + gamma=1.4 "
          "KAT vs Eq. (4) (JAX %s) ==" % jax.__version__)
    ok = True
    gamma = 1.4

    # ---------------- KAT-A: algebraic identity N == -tan(a)*E4
    print("-- KAT-A: Lambda-form numerator == -tan(alpha) x Eq.(4) "
          "residual (machine identity, perfect gas) --")
    th_g = np.arange(2.0, 21.0, 1.5) * d2r
    al_g = np.arange(3.0, 31.0, 1.5) * d2r
    worst = 0.0
    n_pts = 0
    for th in th_g:
        for al in al_g:
            A = np.tan(th - al)
            B = np.tan(al)
            lam = float(lambda_pg(gamma, al))
            N = lam * B * (A + B) - (A - B)
            e4 = float(eq4_residual(gamma, th, al))
            scale = abs(lam * B * (A + B)) + abs(A) + abs(B) \
                + abs(B * e4)
            tol = 100.0 * EPS * max(1.0, scale)   # C_OPS convention
            r = abs(N + B * e4) / tol
            worst = max(worst, r)
            n_pts += 1
    print("  %d grid points, worst |N + tan(a)*E4| / derived floor "
          "= %.3e" % (n_pts, worst))
    ok &= check("KAT-A: zero sets identical at the roundoff floor "
                "(S4 THEOREM, evidence half)", worst <= 1.0)
    # rejector: corrupted gamma on one side must exceed the floor
    th, al = 10.0 * d2r, 12.0 * d2r
    A, B = np.tan(th - al), np.tan(al)
    lam_bad = float(lambda_pg(gamma * 1.001, al))
    N_bad = lam_bad * B * (A + B) - (A - B)
    e4 = float(eq4_residual(gamma, th, al))
    scale = abs(N_bad) + abs(B * e4)
    ok &= check("KAT-A negative control: corrupted gamma rejected",
                abs(N_bad + B * e4) > 100.0 * EPS * scale * 10)

    # sign spot checks (Rao-Beck Fig. 2 orientation, proof advisory)
    v1, _ = val_G(jnp.float64(8 * d2r), jnp.float64(8 * d2r),
                  lambda_pg(gamma, jnp.float64(8 * d2r)))
    v2, _ = val_G(jnp.float64(14 * d2r), jnp.float64(5 * d2r),
                  lambda_pg(gamma, jnp.float64(5 * d2r)))
    print("  sign spots: val(8deg,8deg) = %+.4f  val(14deg,5deg) = "
          "%+.4f" % (float(v1), float(v2)))
    ok &= check("Fig.-2 orientation: (8,8) VALID (+), (14,5) "
                "INVALID (-)", float(v1) > 0.0 > float(v2))

    # ---------------- KAT-B: backend AD Lambda vs closed form
    print("-- KAT-B: AD Lambda through OUR tabulated closure on a "
          "synthetic gamma=1.4 table vs the closed form --")
    tab = A1.prep_tab(A1.build_tab_gconst(g=gamma))
    ta = A1.tab_arrays(tab)
    n_old = A1.N_TAB
    try:
        A1.N_TAB = n_old // 2
        tab_h = A1.prep_tab(A1.build_tab_gconst(g=gamma))
        ta_h = A1.tab_arrays(tab_h)
    finally:
        A1.N_TAB = n_old
    # SPEED RANGE BOUNDED TO THE TABLE BOX (S21 live confirmation of
    # audit engine-core:F3, P2 row: outside the tabulated T range
    # jnp.interp CLAMPS silently and the AD Lambda is wrong-physics —
    # measured here at q = 2.8 a* (M ~ 4.7, T below T_TAB_LO):
    # lam_ad -0.216 vs closed form -1.185. The KAT range is therefore
    # LIMITED to states whose T stays strictly inside the box, and
    # the in-box points must match; the out-of-box behaviour is the
    # C7/F3 domain-guard defect, owned by its scheduled audit row,
    # not by this monitor.)
    qs_all = np.linspace(1.15, 2.8, 16) * float(tab["_as"])
    qs = [q for q in qs_all
          if float(A1.state_q(jnp.float64(q), ta)[0])
          > A1.T_TAB_LO * 1.02]
    worst_rel = 0.0
    band_rel = 0.0
    for q in qs:
        c = float(A1.state_q(jnp.float64(q), ta)[3])
        al = float(np.arcsin(c / q))
        lam_ad = float(lambda_backend(jnp.float64(q), ta))
        lam_ad_h = float(lambda_backend(jnp.float64(q), ta_h))
        lam_cf = float(lambda_pg(gamma, al))
        worst_rel = max(worst_rel, abs(lam_ad - lam_cf)
                        / abs(lam_cf))
        band_rel = max(band_rel, A1.K_RICH
                       * abs(lam_ad - lam_ad_h) / abs(lam_cf))
    band_rel += 100.0 * EPS
    print("  %d in-box speeds: worst |Lam_AD - Lam_pg| / |Lam_pg| "
          "= %.3e vs derived two-resolution band %.3e"
          % (len(qs), worst_rel, band_rel))
    ok &= check("KAT-B: backend Lambda matches the closed form "
                "within the derived table band", worst_rel <= band_rel)
    # rejector: corrupted table (gamma off) must exceed the band
    tab_b = A1.prep_tab(A1.build_tab_gconst(g=gamma * 1.01))
    ta_b = A1.tab_arrays(tab_b)
    q = float(qs[5])
    c_b = float(A1.state_q(jnp.float64(q), ta_b)[3])
    al_b = float(np.arcsin(c_b / q))
    lam_bad = float(lambda_backend(jnp.float64(q), ta_b))
    rel_bad = abs(lam_bad - float(lambda_pg(gamma, al_b))) \
        / abs(float(lambda_pg(gamma, al_b)))
    ok &= check("KAT-B negative control: corrupted table rejected",
                rel_bad > band_rel)

    # ---------------- monitor smoke: armed API on a synthetic surface
    print("-- monitor ARMED: surface_min_val on a synthetic surface --")
    qsurf = np.linspace(1.3, float(qs[-1]) / float(tab["_as"]), 9) \
        * float(tab["_as"])
    thsurf = np.linspace(4.0, 16.0, 9) * d2r
    vals, dens, i_min = surface_min_val(qsurf, thsurf, ta)
    print("  val in [%.4f, %.4f], argmin at node %d (den min %.3e; "
          "den reported, never guarded to zero)"
          % (vals.min(), vals.max(), i_min, np.abs(dens).min()))
    ok &= check("monitor returns finite vals + argmin localization",
                np.all(np.isfinite(vals)))

    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
