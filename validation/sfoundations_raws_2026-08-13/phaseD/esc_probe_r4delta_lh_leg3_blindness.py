# esc_probe_r4delta_lh_leg3_blindness.py
# S-FOUNDATIONS-C4 escalation window (RES-CAP-1 targeted round-4-delta
# refutation), lens L1. Feeds findings E5-L1-2 (parts A, B) and E5-L1-5
# (part C) of esc_refute_r4delta_l1.md.
#
# Targets (round-4 delta of phaseD_r22f_centerpiece.md):
#   [REV2-r4-1](b) H-G6 deriver leg (3): "divided differences of the
#     MEASURED gradient gaps along the SS3.6 design sweep = measured
#     directional Hessian-gap" -- offered as a NAMED DERIVER of
#     L_H := sup_ball ||H_true - H_red||_M with NO measurement-class
#     label (contrast [REV2-r4-3]'s SAMPLED-SUP class + refinement-
#     stability clause for eps_U, same round, same rider).
#   [REV2-r4-2](a)/[REV2-r4-4] R-17: the F2 "curvature-corrected
#     prox-regular refinement" clause mu_eff = mu - |lambda*|*kappa_max
#     > 0, listed as an R-14 DECIDER branch.
#
# PART A: the leg-(3) measurement is DIRECTIONAL -- along the sweep it
#   can be IDENTICALLY ZERO (hence trivially "sustained under sweep-
#   sampling refinement" at every density) while the true L_H is large;
#   plugging the sampled value into mu_eff = mu_meas - L_H_sampled
#   yields a gradient-route bound violated by the unbounded factor
#   mu_meas/(mu_meas - L_H_true). Every printed check of the corrected
#   schema passes (H-G5 convex full space, metric M = I, constant
#   Hessians so any (E)-ladder basin certificate passes, H-G4 moot,
#   functional identity honored -- the defect is ONLY the measurement
#   class of the deriver).
# PART B: sub-sample-width curvature structure -- a C^1 bump between
#   two sweep samples: ALL sampled gradient gaps are exactly zero at
#   two refinement levels (sampled delta = 0, sampled directional
#   Hessian-gap = 0), while the true argmax shift is macroscopic and
#   sup|phi''| (the 1-D L_H) is large. The exact mirror, one derivative
#   up, of the round-4 L2 part-G spike for eps_U.
# PART C: R-17 clause arithmetic on the annulus counter-model of record
#   (r22f_v2_probe_r4_l2_proxreg_annulus.py geometry): the printed
#   clause mu_eff = mu - |lambda*|*kappa_max = eps > 0 PASSES, yet the
#   form-(T) bound is delta_T/mu_eff = 0 against actual shift 2 -- the
#   curvature correction does not restore segment feasibility, so the
#   R-14 decider branch as specified would re-license the probe-killed
#   geometry.
#
# CT-6 clean: synthetic models only; no number from any nozzle paper.
# Tolerances derived: TOL_EXACT = 64*machine-eps for algebraically
# exact quantities; grid tolerances = one grid step of the stated grid.

import numpy as np

EPS_MACH = np.finfo(float).eps
TOL_EXACT = 64.0 * EPS_MACH

print("=" * 72)
print("PART A: directional blindness of H-G6 deriver leg (3)")
print("=" * 72)

# Design space R^2, metric M = I (condition (3) holds). Sweep along e1.
# J_red  = -(mu/2)(x1^2 + x2^2)                      (measured carrier)
# J_true = -(mu/2)x1^2 - ((mu-c)/2)x2^2 + b*x2
# Hessian gap E = H_true - H_red = diag(0, +c)  (constant), L_H = c.
mu = 1.0     # measured carrier floor (J_red Hessian = -mu*I)
c = 0.99     # true curvature deficit in the e2 (off-sweep) direction
b = 0.1      # gradient-level residual amplitude

def grad_gap(x1, x2):
    # grad J_true - grad J_red = (0, c*x2 + b)
    return np.array([0.0, c * x2 + b])

# S*_red = argmax J_red = origin (interior, margin-inactive: H-G4 moot).
S_red = np.array([0.0, 0.0])
# S*_true = argmax J_true = (0, b/(mu-c)).
S_true = np.array([0.0, b / (mu - c)])
shift_actual = np.linalg.norm(S_true - S_red)

# Leg-(3) measurement as printed: divided differences of the MEASURED
# gradient gaps ALONG the design sweep (sweep line x2 = 0), at three
# sampling densities (refinement-stability check, [REV2-r4-3] pattern).
sampled_LH = []
for h in (0.2, 0.1, 0.05):
    ts = np.arange(-1.0, 1.0 + h / 2, h)
    gaps = np.array([grad_gap(t, 0.0) for t in ts])
    dd = (gaps[1:] - gaps[:-1]) / h          # divided differences
    sampled_LH.append(np.max(np.linalg.norm(dd, axis=1)) if len(dd) else 0.0)
sampled_LH = np.array(sampled_LH)

# (A1) the sampled directional Hessian-gap is EXACTLY zero at every
#      density: the gap field is constant along the sweep.
assert np.all(np.abs(sampled_LH) <= TOL_EXACT), sampled_LH
# (A2) it is therefore SUSTAINED under sweep-sampling refinement -- a
#      stability clause of the [REV2-r4-3] kind does NOT catch this.
assert np.all(np.abs(np.diff(sampled_LH)) <= TOL_EXACT)

# Claimed gradient-route bound with mu_eff = mu_meas - L_H_sampled:
delta_at_Sred = np.linalg.norm(grad_gap(*S_red))   # = b (full-space cone)
mu_eff_claimed = mu - sampled_LH[-1]               # = mu (L_H seen as 0)
bound_claimed = delta_at_Sred / mu_eff_claimed
# (A3) the claimed bound is violated by factor mu/(mu-c) = 100x.
assert bound_claimed + TOL_EXACT < shift_actual
violation = shift_actual / bound_claimed
assert abs(violation - mu / (mu - c)) <= 1e3 * TOL_EXACT * violation
# (A4) control: the TRUE L_H = c restores exactness.
mu_eff_true = mu - c
bound_true = delta_at_Sred / mu_eff_true
assert abs(bound_true - shift_actual) <= 1e3 * TOL_EXACT * shift_actual

print(f"  sampled directional Hessian-gap (3 densities): {sampled_LH}")
print(f"  true L_H = {c}; claimed bound = {bound_claimed:.4g}; "
      f"actual shift = {shift_actual:.4g}; violation = {violation:.1f}x")
print(f"  corrected (true-L_H) bound = {bound_true:.4g} -- exact")
print("  PART A: ALL ASSERTS PASS")

print("=" * 72)
print("PART B: sub-sample-width curvature spike (1-D)")
print("=" * 72)

# J_red = -(mu/2)x^2; J_true = J_red + phi, phi a C^1 bump of half-width
# w = h/8 centered strictly between sweep samples at BOTH refinement
# levels h and h/2 (support avoids every sample of both ladders).
mu_b = 1.0
h_sweep = 0.1
a_ctr = 0.0375      # between multiples of 0.05 and of 0.1
w = h_sweep / 8.0   # 0.0125 -> support (0.025, 0.05), endpoints excluded
A_amp = 0.05

def phi(x):
    u = (x - a_ctr) / w
    out = np.where(np.abs(u) < 1.0, A_amp * (1.0 - u ** 2) ** 2, 0.0)
    return out

def dphi(x):
    u = (x - a_ctr) / w
    return np.where(np.abs(u) < 1.0,
                    A_amp * 4.0 * u * (u ** 2 - 1.0) / w, 0.0)

for h in (h_sweep, h_sweep / 2.0):
    xs = np.arange(-1.0, 1.0 + h / 2, h)
    gaps = dphi(xs)                       # gradient gap at the samples
    # (B1) every sampled gradient gap is exactly zero at both levels:
    assert np.all(np.abs(gaps) <= TOL_EXACT), (h, np.max(np.abs(gaps)))
    # hence sampled delta = 0 and sampled directional Hessian-gap = 0,
    # sustained under this refinement step.

# Actual shift: argmax of J_true on a fine grid (step df -> tolerance df).
df = 1e-5
xf = np.arange(-1.0, 1.0 + df / 2, df)
J_true_f = -(mu_b / 2.0) * xf ** 2 + phi(xf)
x_star = xf[np.argmax(J_true_f)]
shift_B = abs(x_star - 0.0)               # S*_red = 0
assert shift_B > 10 * df                  # macroscopic, not grid noise
# true 1-D L_H = sup|phi''| (numerical, fine grid)
d2 = np.gradient(np.gradient(phi(xf), df), df)
LH_true_B = np.max(np.abs(d2))
assert LH_true_B > mu_b                   # curvature gap dominates mu

print(f"  sampled gradient gaps: identically 0 at h = {h_sweep} and "
      f"{h_sweep/2}")
print(f"  actual argmax shift = {shift_B:.4g}  (claimed bound with "
      f"sampled delta = 0, sampled L_H = 0: 0)")
print(f"  true L_H (sup|phi''|) = {LH_true_B:.4g} >> mu = {mu_b}")
print("  PART B: ALL ASSERTS PASS")

print("=" * 72)
print("PART C: R-17 clause on the annulus counter-model of record")
print("=" * 72)

# Annulus C = {1 <= |x| <= 3} (prox-regular, reach r_prox = 1,
# connected). J_red = -mu|x|^2/2 + eps*x1; J_true = -mu|x|^2/2 - eps*x1.
mu_c = 1.0
eps = 1e-3
# S*_red = (1, 0): maximize -mu*r^2/2 + eps*x1 -> r = 1, x1 = +1.
# Verify by dense boundary scan (tolerance = angular step).
th = np.linspace(0.0, 2.0 * np.pi, 20001)
for r in (1.0, 3.0):
    Jb = -mu_c * r ** 2 / 2.0 + eps * r * np.cos(th)
    pass  # inner boundary r=1 dominates; explicit check below
J_inner = -mu_c / 2.0 + eps * np.cos(th)
assert abs(th[np.argmax(J_inner)] - 0.0) <= th[1] or \
       abs(th[np.argmax(J_inner)] - 2 * np.pi) <= th[1]
S_red_C = np.array([1.0, 0.0])
S_true_C = np.array([-1.0, 0.0])          # J_true symmetric mirror
shift_C = np.linalg.norm(S_true_C - S_red_C)   # = 2
assert abs(shift_C - 2.0) <= TOL_EXACT

# KKT multiplier at S*_red for constraint c(x) = |x| - 1 >= 0:
# grad J_red = (eps - mu, 0); grad c = (1, 0) => lambda* = mu - eps.
lam_star = mu_c - eps
kappa_max = 1.0 / 1.0                     # 1 / r_prox
mu_eff_R17 = mu_c - abs(lam_star) * kappa_max
# (C1) the printed R-17 clause PASSES: mu_eff = eps > 0.
assert mu_eff_R17 > 0.0
assert abs(mu_eff_R17 - eps) <= TOL_EXACT
# (C2) form-(T) residual at S*_red: gap = grad J_true - grad J_red =
# (-2*eps, 0); tangent cone at (1,0) = {d1 >= 0};
# delta_T = sup{<g,d> : d in cone, |d| <= 1} = 0 (positive part).
g_gap = np.array([-2.0 * eps, 0.0])
# discretized cone directions (tolerance = directional step):
ang = np.linspace(-np.pi / 2, np.pi / 2, 10001)   # d1 >= 0 half-circle
delta_T = max(0.0, np.max(g_gap[0] * np.cos(ang) + g_gap[1] * np.sin(ang)))
assert delta_T <= TOL_EXACT
# (C3) the re-licensed bound delta_T/mu_eff = 0 against actual shift 2.
bound_R17 = delta_T / mu_eff_R17
assert bound_R17 + TOL_EXACT < shift_C
print(f"  R-17 clause: mu_eff = mu - |lambda*|*kappa = {mu_eff_R17:.4g}"
      f" > 0  -> clause PASSES on the probe-killed annulus")
print(f"  form-(T) bound = {bound_R17:.4g} vs actual shift = {shift_C}")
print("  -> curvature correction does NOT restore segment feasibility;")
print("     the R-14 decider branch as specified re-licenses the killer")
print("  PART C: ALL ASSERTS PASS")

print("=" * 72)
print("ALL ASSERTS PASS (parts A, B, C)")
print("=" * 72)
