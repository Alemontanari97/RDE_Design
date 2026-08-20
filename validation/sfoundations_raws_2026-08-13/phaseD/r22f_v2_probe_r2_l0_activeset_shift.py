"""R22F round-2 L0 probe: active-set migration defeats the delta/mu
argmax-shift form with mu = CRITICAL-CONE reduced-Hessian floor, even
when every printed soundness condition of phaseD_r22f_centerpiece.md
SS2.2-bis (1)-(3) is satisfied.

Feeds finding R22F-L0-10 (phaseD_r22f_refute_r2_l0.md).

Setup (synthetic, CT-6 clean; metric M = I so condition (3) holds
trivially; all quantities analytic quadratics => 'uniform on any ball'
curvature certificates are exact, so any finite basin-radius check
passes):

  J_red(x, y)  = -mu/2 x^2 - nu/2 y^2 + c y      on  {y <= 0}
  J_true(x, y) = J_red(x, y) - 2 c y             (gradient gap (0,-2c))

  mu  = 1.0    (curvature in the critical-cone direction)
  nu  = 1e-3   (tiny curvature in the constrained direction)
  c   = 0.05   (multiplier of the active constraint at S*_red)

At S*_red = (0,0): constraint y<=0 ACTIVE, multiplier lambda = c > 0
(strict complementarity HOLDS); critical cone = {d_y = 0} = x-axis;
reduced Hessian on the critical cone = mu, CONSTANT (hence uniform on
every ball). delta = ||grad J_true - grad J_red|| = 2c in the M = I
dual norm (projection onto the critical cone leaves it 0 -- the
PROJECTED residual P_T[g] is 0! -- we take the harsher unprojected 2c;
either reading is <= 2c and the violation below beats both).

True constrained argmax of J_true: y* = -c/nu (interior in y), x* = 0.
Shift = c/nu = 50  >>  delta/mu = 0.1.   Violation factor 500.

Sound repairs verified numerically below:
  (R-a) tangent-cone curvature floor mu_tan = nu  => VI bound
        shift <= delta/mu_tan holds (strong-monotonicity argument);
  (R-b) multiplier-margin clause: for perturbation delta' < lambda the
        active set is stable and the critical-cone bound holds.

Pinned env, numpy only. All tolerances derived (machine eps scale on
O(1)-O(1e2) quadratic algebra).
"""

import numpy as np

MU = 1.0     # critical-cone curvature
NU = 1e-3    # curvature in the constrained (y) direction
C = 0.05     # active-constraint multiplier at S*_red

TOL = 1e4 * np.finfo(float).eps * (1.0 / NU)  # derived: worst scale c/nu


def argmax_on_halfplane(gx, gy, hx, hy):
    """Argmax of -hx/2 x^2 - hy/2 y^2 + gx x + gy y on {y <= 0}.

    Separable strictly concave quadratic: x* = gx/hx; y* = min(gy/hy, 0).
    """
    return gx / hx, min(gy / hy, 0.0)


def grid_check(fun, xstar, ystar, half=None):
    """Brute-force check that (xstar, ystar) beats a feasible grid."""
    xs = np.linspace(xstar - 80, xstar + 80, 401)
    ys = np.linspace(min(ystar - 80, -80), 0.0, 401)  # feasible y <= 0
    vals = fun(xs[:, None], ys[None, :])
    return vals.max() <= fun(xstar, ystar) + TOL


def J_red(x, y):
    return -MU / 2 * x**2 - NU / 2 * y**2 + C * y


def J_true(x, y):
    return -MU / 2 * x**2 - NU / 2 * y**2 - C * y  # J_red - 2 c y


# --- reduced optimum: gradient of J_red = (0, c) at origin ------------
xr, yr = argmax_on_halfplane(0.0, C, MU, NU)
assert abs(xr) < TOL and abs(yr) < TOL, "S*_red must be the origin"
assert grid_check(J_red, xr, yr), "grid check S*_red"
lam = C  # KKT: grad J_red = lam * grad(y) => lam = c > 0, strict compl.
assert lam > 0.0

# --- true optimum under gradient gap (0, -2c): delta = 2c -------------
xt, yt = argmax_on_halfplane(0.0, -C, MU, NU)
assert abs(xt) < TOL and abs(yt - (-C / NU)) < TOL, "S*_true = (0,-c/nu)"
assert grid_check(J_true, xt, yt), "grid check S*_true"

delta = 2 * C                      # dual-norm (M = I) gradient gap
shift = np.hypot(xt - xr, yt - yr)  # = c/nu
bound_critical = delta / MU        # the SS2.2-bis licensed form

# (1) every printed condition holds: mu uniform (constant Hessian), so
# ANY finite basin-radius certificate passes the a-posteriori check
# delta/mu <= radius; strict complementarity holds at S*_red; M = I.
basin_radius_certificate = np.inf  # exact for a quadratic
assert bound_critical <= basin_radius_certificate

# (2) ... and yet the bound is violated by a large factor:
violation = shift / bound_critical
assert shift > bound_critical + TOL, "no violation -> probe refuted"
assert violation > 100.0, f"violation factor too small: {violation}"

# (R-a) tangent-cone curvature floor repairs the bound (VI argument):
mu_tan = NU
assert shift <= delta / mu_tan + TOL, "VI/tangent-cone bound must hold"

# (R-b) multiplier-margin clause: perturbation below the multiplier
# keeps the active set; critical-cone bound then holds (shift = 0).
delta_small = 0.5 * C  # < lambda = c
xs, ys = argmax_on_halfplane(0.0, C - delta_small, MU, NU)
assert abs(xs) < TOL and abs(ys) < TOL, "active set must be stable"
shift_small = np.hypot(xs - xr, ys - yr)
assert shift_small <= delta_small / MU + TOL

print("PROBE PASS: all assertions hold.")
print(f"  S*_red = ({xr:.3g},{yr:.3g})  lambda = {lam:.3g} (strict compl.)")
print(f"  S*_true = ({xt:.3g},{yt:.3g})")
print(f"  delta = {delta:.3g}   mu_critical = {MU:.3g}   "
      f"licensed bound delta/mu = {bound_critical:.3g}")
print(f"  actual shift = {shift:.6g}  -> VIOLATION factor {violation:.1f}x")
print(f"  repair (R-a): tangent-cone floor nu -> bound {delta/mu_tan:.3g} "
      f">= shift  OK")
print(f"  repair (R-b): delta' = {delta_small:.3g} < lambda -> shift "
      f"{shift_small:.3g} <= {delta_small/MU:.3g}  OK")
