# esc_probe_r4delta_hg6_pointfloor.py
# E-5 TARGETED REFUTER, lens L2 (asymptotics / measure-scaling), C4
# escalation window, RES-CAP-1 targeted pass on the round-4 delta.
# Feeds finding E5-L2-2 (esc_refute_r4delta_l2.md).
#
# CLAIM UNDER TEST: [REV2-r4-1](b) H-G6 as printed —
#   "mu_true_floor >= mu_meas - L_H, with L_H := the sup over the
#    certified ball of the design-Hessian residual norm ||H_true-H_red||_M"
# with mu_meas = the POINT-measured carrier (condition (1)'s own words:
# "The segmented TR-Newton curvature of record is POINT-measured").
#
# PART A shows the inequality is FALSE as a freestanding hypothesis line
# even with L_H = 0 EXACTLY (H_true == H_red pointwise): the omitted
# premise is the (E)-ladder sustainment of mu_meas as a BALL floor of
# J_red. PART B shows the composed a-posteriori chain of record
# (condition (1) basin check with the (E)-certified radius) DOES refuse
# the counterexample — hence AMENDMENT, not BREAK: one premise-naming
# clause is missing at H-G6, no false certificate issues from the full
# printed chain today.
#
# Synthetic 1-D counter-model, closed forms only (no numerics beyond
# arithmetic; CT-6 clean; pinned-env safe: stdlib math only).
#
# Model: concave C^1 J_red with piecewise-constant curvature
#   mu(x) = MU_IN  for |x| <= R_SUST   (the region where the point
#                                       measurement at S*_red = 0 sustains)
#   mu(x) = MU_OUT for |x| >  R_SUST   (soft outer region)
#   J_red'(x) = -M(x),  M(x) = integral_0^x mu  (odd),  S*_red = 0.
# J_true = J_red + c*x  ==>  H_true == H_red everywhere ==> L_H = 0
# exactly on EVERY ball, in every metric. delta = |J_true' - J_red'| = c
# (constant; support-function form trivial in 1-D, metric M = I,
# feasible set = a large interval => H-G5 convex; interior argmaxes =>
# H-G4 moot; cone-pairing trivial).
# True argmax: M(x) = c.

import math

MU_IN = 1.0      # mu_meas: point curvature measured at S*_red = 0
MU_OUT = 0.01    # true curvature outside the sustained region
R_SUST = 0.5     # radius on which the measured floor actually sustains
L_H = 0.0        # H_true == H_red identically => exact, not estimated
R_BALL = 20.0    # a certified ball large enough to contain the shift


def M(x):
    """M(x) = int_0^x mu(t) dt, x >= 0."""
    if x <= R_SUST:
        return MU_IN * x
    return MU_IN * R_SUST + MU_OUT * (x - R_SUST)


def argmax_shift(c):
    """Solve M(x) = c for x >= 0 (the true-argmax shift from S*_red=0)."""
    if c <= MU_IN * R_SUST:
        return c / MU_IN
    return R_SUST + (c - MU_IN * R_SUST) / MU_OUT


# ---------------------------------------------------------------- PART A
# Freestanding H-G6 inequality with point-measured mu_meas: FALSE.
mu_meas = MU_IN                       # point measurement at S*_red
mu_true_floor_ball = MU_OUT           # true J_TRUE curvature floor on the
                                      # ball the shift explores (R_BALL)
hg6_rhs = mu_meas - L_H               # printed lower "floor" = 1.0

assert mu_true_floor_ball < hg6_rhs, "counter-model failed to build"
# violation of the printed inequality: 0.01 >= 1.0 is FALSE
print("PART A1: H-G6 printed inequality mu_true_floor >= mu_meas - L_H")
print(f"  mu_true_floor(ball) = {mu_true_floor_ball}, "
      f"mu_meas - L_H = {hg6_rhs}  -> FALSE (L_H = 0 exactly)")

# Composed misuse: bound delta/mu_eff with mu_eff = mu_meas - L_H.
c = 0.6
delta = c
shift = argmax_shift(c)               # = 0.5 + 0.1/0.01 = 10.5
bound_hg6 = delta / hg6_rhs           # = 0.6
violation = shift / bound_hg6         # = 17.5x
assert abs(shift - 10.5) < 1e-12
assert violation > 10.0, "expected an order-of-magnitude violation"
print(f"PART A2: delta = {delta}, actual shift = {shift}, "
      f"H-G6-composed bound = {bound_hg6} -> violation {violation:.1f}x")
# The violation is UNBOUNDED along the ladder MU_OUT -> 0 (shift ->
# infinity at fixed bound): same divergence shape as the r4_l0 A7 ladder.

# Control: the SCHEMA object itself (J_TRUE floor per [REV2-r4-1](a)) is
# sound — with the true floor the bound holds:
bound_true = delta / mu_true_floor_ball   # = 60
assert shift <= bound_true + 1e-12
print(f"PART A3: with the TRUE J_TRUE floor {mu_true_floor_ball}: "
      f"bound = {bound_true} >= shift {shift} -> schema sound; only the "
      "point-mu_meas instantiation of H-G6 is the defect")

# ---------------------------------------------------------------- PART B
# The full printed chain refuses: condition (1)'s a-posteriori check
# delta/mu <= certified basin radius, radius from the (E) ladder =
# "largest ball on which the measured floor sustains its value within
# its own band" = R_SUST here.
r_certified = R_SUST
assert bound_hg6 > r_certified, "the (E)-gated basin check must refuse"
print(f"PART B1: a-posteriori check {bound_hg6} <= r_cert {r_certified} "
      "FAILS -> the composed chain honestly refuses (hence AMENDMENT, "
      "not BREAK)")

# And on the (E)-certified ball the sustained-floor reading restores the
# transfer inequality and yields a tight, valid bound:
c_small = 0.3
shift_small = argmax_shift(c_small)   # = 0.3, inside the sustained region
mu_sustained = MU_IN                  # floor of J_red on the certified ball
mu_eff_sound = mu_sustained - L_H
bound_sound = c_small / mu_eff_sound  # = 0.3
assert shift_small <= bound_sound + 1e-12
assert bound_sound <= r_certified     # check passes
# transfer inequality on the certified ball: true floor there = MU_IN
assert MU_IN >= mu_eff_sound - 1e-12
print(f"PART B2: sustained-floor reading on the certified ball: bound = "
      f"{bound_sound} = shift {shift_small} (tight), check "
      f"{bound_sound} <= {r_certified} passes -> one clause (mu_meas = "
      "the (E)-certified sustained ball floor, band-lower edge) repairs "
      "H-G6")

print()
print("ALL ASSERTS PASS (PARTs A-B).")
print("PROBE-VERDICT: H-G6 as printed is FALSE as a freestanding")
print("hypothesis with point-measured mu_meas (L_H = 0 exactly,")
print("violation 17.5x, unbounded along the MU_OUT->0 ladder); the")
print("composed condition-(1)+(E) chain refuses the counter-model;")
print("fix = one premise clause naming the (E)-sustained ball floor")
print("(band-lower edge) as the mu_meas H-G6 consumes. AMENDMENT class.")
