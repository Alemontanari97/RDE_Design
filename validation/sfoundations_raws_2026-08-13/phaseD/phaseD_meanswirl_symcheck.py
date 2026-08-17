#!/usr/bin/env python3
"""Phase D symbolic carrier for phaseD_meanswirl_formalization.md
(S-FOUNDATIONS R35, Phase D mean-swirl batch, 2026-08-17 window).

Machine verification (sympy, EOS-general: the only thermodynamic
input is dh = T ds + dp/rho along particle paths, used in the form
Dh = (1/rho) Dp on smooth isentropic-transport regions) of the
REDUCTION-RESIDUAL identities of Sec. 5 of the formalization doc:

  (C1) Gamma-pumping identity: for the EXACT 3-D wave-frame steady
       flow (fields F(x, r, phi), lab time derivative = -Omega d/dphi),
       the material derivative of Gamma = r*w along RELATIVE
       streamlines equals -(1/rho) dp/dphi. Torque = azimuthal
       pressure gradient, exactly.
  (C2) h0-pumping identity: D_rel h0 = -(Omega/rho) dp/dphi
       (the unsteady pressure-work term seen through the wave frame).
  (C3) ROTHALPY: D_rel (h0 - Omega*Gamma) = 0 EXACTLY in the smooth
       3-D wave-frame flow (C2 - Omega*C1). The per-phase invariant
       PAIR (h0, Gamma) is a reduction artifact; the exact flow
       transports only the combination I = h0 - Omega*Gamma.
  (C4) RESIDUAL BOOKKEEPING: the exact wave-frame system equals the
       per-phase 2.5-D system PLUS the named commutator terms
       K_rho, K_u, K_v, K_Gamma, K_s, K_h0 -- no unnamed leftover
       (in particular every curvature/metric term is retained by the
       2.5-D operator; ONLY phi-derivative terms are dropped).
  (R1) REJECTOR: corrupting the retained geometric coupling
       (-v*w/r in the theta-momentum) BREAKS C3 (nonzero leftover):
       the identity chain can fail, hence the checks can reject.

Exit 0 iff all checks pass (rejector = detected breakage).
Environment: pinned repo env (sympy present of record; nothing
installed). Run: python phaseD_meanswirl_symcheck.py
"""

import sympy as sp

x, r, phi, Omega = sp.symbols('x r phi Omega', real=True)
# Fields of the wave-frame coordinates (x, r, phi). Absolute velocity
# components (u, v, w) = (u_x, u_r, u_theta); p, rho, s, h fields.
u = sp.Function('u')(x, r, phi)
v = sp.Function('v')(x, r, phi)
w = sp.Function('w')(x, r, phi)
p = sp.Function('p')(x, r, phi)
rho = sp.Function('rho')(x, r, phi)
h = sp.Function('h')(x, r, phi)

FAIL = []


def check(name, expr, expect_zero=True):
    ok = (sp.simplify(expr) == 0) == expect_zero
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: simplify -> "
          f"{sp.simplify(expr)}")
    if not ok:
        FAIL.append(name)


# Lab material derivative D/Dt = d/dt + u d/dx + v d/dr + (w/r) d/dtheta
# acting on wave-frame fields F(x, r, theta - Omega t):
#   d/dt -> -Omega d/dphi, d/dtheta -> d/dphi.
def D(f):
    return (-Omega * sp.diff(f, phi) + u * sp.diff(f, x)
            + v * sp.diff(f, r) + (w / r) * sp.diff(f, phi))


# Inviscid momentum equations in cylindrical coordinates (absolute
# velocities), no body force; these DEFINE the substitutions for the
# material accelerations:
Du = -sp.diff(p, x) / rho
Dv = w**2 / r - sp.diff(p, r) / rho
Dw = -v * w / r - sp.diff(p, phi) / (rho * r)   # geometric coupling -vw/r
# Smooth isentropic transport (Ds = 0) + Gibbs dh = T ds + dp/rho:
Dh = D(p) / rho

print("(C1) Gamma-pumping: D(r w) + (1/rho) dp/dphi == 0")
# D(r w) = r*Dw + w*Dr with Dr = v (material derivative of coordinate r)
DGamma = r * Dw + w * v
check("C1", DGamma + sp.diff(p, phi) / rho)

print("(C2) h0-pumping: D h0 + (Omega/rho) dp/dphi == 0")
Dh0 = Dh + u * Du + v * Dv + w * Dw
check("C2", Dh0 + Omega * sp.diff(p, phi) / rho)

print("(C3) rothalpy: D(h0 - Omega*Gamma) == 0")
check("C3", Dh0 - Omega * DGamma)

print("(C4) residual bookkeeping: exact wave-frame rows == 2.5-D rows"
      " + named K terms")
wrel = w - Omega * r
# Exact wave-frame rows (advective form), written as
# LHS_exact = 0. Per-phase 2.5-D rows: same with all d/dphi struck.
# Named commutator terms (doc Sec. 5): the difference must be exactly
# K, no leftover.
Dm = lambda f: u * sp.diff(f, x) + v * sp.diff(f, r)  # meridional advection


def row_gap(exact, reduced, K):
    return sp.simplify(exact - reduced - K)


# continuity (divergence form): (1/r)[(r rho u)_x + (r rho v)_r] carried
# by 2.5-D; exact adds (1/r) d(rho wrel)/dphi   [d/dt rho -> -Omega rho_phi]
cont_exact = (sp.diff(r * rho * u, x) + sp.diff(r * rho * v, r)) / r \
    + sp.diff(rho * wrel, phi) / r
cont_25d = (sp.diff(r * rho * u, x) + sp.diff(r * rho * v, r)) / r
K_rho = sp.diff(rho * wrel, phi) / r
check("C4-cont", row_gap(cont_exact, cont_25d, K_rho))

# x-momentum: rho D u + p_x = 0 exact; 2.5-D: rho Dm u + p_x = 0
xmom_exact = rho * D(u) + sp.diff(p, x)
xmom_25d = rho * Dm(u) + sp.diff(p, x)
K_u = rho * (wrel / r) * sp.diff(u, phi)
check("C4-xmom", row_gap(xmom_exact, xmom_25d, K_u))

# r-momentum: rho (D v - w^2/r) + p_r = 0; 2.5-D keeps the centrifugal
# source -rho w^2/r (it is NOT dropped)
rmom_exact = rho * (D(v) - w**2 / r) + sp.diff(p, r)
rmom_25d = rho * (Dm(v) - w**2 / r) + sp.diff(p, r)
K_v = rho * (wrel / r) * sp.diff(v, phi)
check("C4-rmom", row_gap(rmom_exact, rmom_25d, K_v))

# Gamma row: exact rho*D(Gamma) + p_phi = 0 (equivalent to theta-mom);
# 2.5-D: rho*Dm(Gamma) = 0. K_Gamma = rho*(wrel/r) Gamma_phi + p_phi
Gam = r * w
gam_exact = rho * D(Gam) - rho * v * w + rho * v * w + sp.diff(p, phi)
# NOTE: D(Gam) here treats Gam as a FIELD of (x, r, phi); the material
# derivative of the coordinate factor r is carried by v*dGam/dr term
# composition; the field-form theta-momentum row is
#   rho*(D(Gam) + v*w - v*w) + p_phi -- i.e. rho*D_field(Gam) + p_phi
# equals r*(theta-momentum) identically:
theta_mom = rho * (D(w) + v * w / r) + sp.diff(p, phi) / r
check("C4-gamrow-equiv", sp.simplify(gam_exact - r * theta_mom))
gam_25d = rho * Dm(Gam)
K_Gamma = rho * (wrel / r) * sp.diff(Gam, phi) + sp.diff(p, phi)
check("C4-gamma", row_gap(gam_exact, gam_25d, K_Gamma))

# entropy row: D s = 0 exact; 2.5-D: Dm s = 0; K_s = (wrel/r) s_phi
s = sp.Function('s')(x, r, phi)
K_s = (wrel / r) * sp.diff(s, phi)
check("C4-s", row_gap(D(s), Dm(s), K_s))

# h0 row: exact D h0 = -(Omega/rho) p_phi (C2); 2.5-D: Dm h0 = 0;
# K_h0 = (wrel/r) h0_phi + (Omega/rho) p_phi  applied to h0 as a field
h0f = sp.Function('h0')(x, r, phi)
K_h0 = (wrel / r) * sp.diff(h0f, phi) + (Omega / rho) * sp.diff(p, phi)
check("C4-h0", row_gap(D(h0f) + (Omega / rho) * sp.diff(p, phi),
                       Dm(h0f), K_h0))

print("(R1) rejector: corrupt the geometric coupling -vw/r -> +vw/r")
Dw_bad = +v * w / r - sp.diff(p, phi) / (rho * r)
Dh0_bad = Dh + u * Du + v * Dv + w * Dw_bad
DGamma_bad = r * Dw_bad + w * v
resid_bad = sp.simplify(Dh0_bad - Omega * DGamma_bad)
ok = resid_bad != 0
print(f"  [{'PASS' if ok else 'FAIL'}] R1: corrupted rothalpy residual = "
      f"{resid_bad} (must be NONZERO)")
if not ok:
    FAIL.append("R1")

print()
if FAIL:
    print(f"OVERALL: FAIL ({FAIL})")
    raise SystemExit(1)
print("OVERALL: PASS (C1, C2, C3, C4 x7, R1)")
