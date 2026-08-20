"""R22F round-3 L2 probe: eps_U instantiation gap (feeds R22F-L2-19).

Target: phaseD_r22f_centerpiece.md [REV2-r2-3](F) (:655-657) and the
(vi) BEST cell (:1155): "|argmax shift| <= 2*sqrt(eps_U/mu) with
eps_U = M-RED measured per-family eps".

Claim under attack (the literal executor reading): the value-route
sqrt bound may be instantiated with eps_U = the M-RED PER-FAMILY
measured value error eps(F) — a number measured at the executed
design point(s) — as if it were the lemma's uniform-on-basin premise
(U_G): sup_{S in basin} |J_true(S) - J_red(S)| <= eps_U.

Demonstration (1-D design space, strongly concave, mu = 1):
  J_true(s) = -s^2/2            (argmax 0, curvature floor mu = 1)
  J_red(s)  = J_true(s) + a*(s - s0) + e0
  s0 = 0 = the design point where the family's eps is measured.
Then the per-family measured value error at s0 is |e0|, while the
argmax of J_red sits at s = a: the true shift is a, independent of e0.
The literal per-family instantiation gives bound 2*sqrt(e0/mu), which
the shift violates by the factor a/(2*sqrt(e0)) -> unbounded as
e0 -> 0.  The SUP-based premise (eps_sup = a*R + e0 on basin [-R, R])
keeps the lemma true: a <= 2*sqrt(eps_sup/mu) whenever a <= 4R (all
cases here).  The lemma itself is SOUND; the pointwise instantiation
printed in the cell is NOT.

Env: pinned (numpy only, already installed). Run: python <this file>.
All asserts must PASS; the probe FAILS (raises) if the literal
pointwise reading were actually safe (i.e. if no violation existed).
"""

import numpy as np

rng = np.random.default_rng(20260820)

mu = 1.0
R = 1.0  # basin radius around the measurement design point s0 = 0
grid = np.linspace(-R, R, 20001)


def j_true(s):
    return -0.5 * s * s


def run_case(a, e0):
    """Return (shift, eps_point, bound_point, eps_sup, bound_sup)."""
    def j_red(s):
        return j_true(s) + a * (s - 0.0) + e0

    # per-family measured value error AT the executed design point s0=0
    eps_point = abs(j_red(0.0) - j_true(0.0))          # = |e0|
    # sup value error over the certified basin (the (U_G) premise)
    eps_sup = np.max(np.abs(j_red(grid) - j_true(grid)))  # = a*R + e0
    # argmax of the reduced functional on the basin (analytic: s = a)
    shift = abs(grid[np.argmax(j_red(grid))] - 0.0)
    bound_point = 2.0 * np.sqrt(eps_point / mu)
    bound_sup = 2.0 * np.sqrt(eps_sup / mu)
    return shift, eps_point, bound_point, eps_sup, bound_sup


print("=== A. e0 = 0: measured per-family eps is EXACTLY ZERO, shift is not ===")
shift, ep, bp, es, bs = run_case(a=0.10, e0=0.0)
print(f"shift = {shift:.4f}; eps_point = {ep:.1e} -> bound_point = {bp:.1e}; "
      f"eps_sup = {es:.4f} -> bound_sup = {bs:.4f}")
assert shift > bp + 1e-12, "literal pointwise reading NOT violated?!"
assert shift <= bs + 1e-9, "sup-premise lemma violated?! (must never happen)"

print("=== B. e0 = 1e-8: finite pointwise eps, violation factor ~500x ===")
shift, ep, bp, es, bs = run_case(a=0.10, e0=1e-8)
ratio = shift / bp
print(f"shift = {shift:.4f}; bound_point = {bp:.3e}; violation = {ratio:.0f}x; "
      f"bound_sup = {bs:.4f} (holds)")
assert ratio > 100.0
assert shift <= bs + 1e-9

print("=== C. violation factor grows without bound as e0 -> 0 (fixed a) ===")
for e0 in (1e-4, 1e-6, 1e-8, 1e-10):
    shift, ep, bp, es, bs = run_case(a=0.10, e0=e0)
    print(f"  e0 = {e0:.0e}: shift/bound_point = {shift/bp:8.0f}x ; "
          f"sup bound holds: {shift <= bs + 1e-9}")
    assert shift > bp and shift <= bs + 1e-9

print("=== D. control: the lemma with the SUP premise holds on random draws ===")
for _ in range(200):
    a = rng.uniform(0.0, 0.5)
    e0 = rng.uniform(0.0, 0.05)
    # random extra smooth perturbation, included in the sup
    b = rng.uniform(-0.2, 0.2)
    def j_red(s, a=a, e0=e0, b=b):
        return j_true(s) + a * (s - 0.0) + e0 + b * np.sin(2.0 * s)
    eps_sup = np.max(np.abs(j_red(grid) - j_true(grid)))
    shift = abs(grid[np.argmax(j_red(grid))])
    assert shift <= 2.0 * np.sqrt(eps_sup / mu) + 1e-9
print("200/200 random draws: sup-premise bound holds (lemma sound)")

print("\nALL ASSERTS PASS: the (F)/(vi)-cell literal instantiation "
      "'eps_U = per-family measured eps' is UNSOUND (unbounded violation); "
      "the uniform sup-on-basin premise is the sound reading.")
