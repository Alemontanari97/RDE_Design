"""R22F-L2-13 probe (round 2, lens L2): [REV2-r1-14] entry-margin routing
leaves eps(F) measure-accounting OPEN in the M-RED spec.

Target text (phaseD_r22f_centerpiece.md):
  - Sec 3.1: eps(F) := |J_exact - J_avg|(F), J_exact = integral of
    F_true(xi) dmu over the FULL cycle measure (sector-decomposition
    identity).
  - [REV2-r1-14] (Sec 3.4 / B-4): "Phases below the floor route to the
    declared subsonic sector (T-T3-MAP(d)), never into the march."
  - BAND RULE: every band = (fp floor) + (measured curvature/exponent)
    + (declared [INF] constants) -- NOTHING ELSE.

Attack: for a family with routed mu-mass mu_r > 0 (phases SUPERSONIC,
M_entry in (1, 1+m0) -- NOT members of T-T3-MAP(d)'s Xi_sub), the
published spec under-determines eps(F): the march defines F_2D only on
the marched sector, so an executor must EITHER (a) restrict the
comparison to the marched sector, or (b) book routed phases through the
mixture form as the routing sentence says literally. The two readings
differ by the routed-sector term mu_r * (booking error), which is NOT
representable inside the published band algebra (fp floor / measured
curvature / declared [INF] constant). Toy model, numpy only. CT-6: all
numbers synthetic; no number from the four nozzle papers used.
"""
import numpy as np

# Toy cycle: N phases, uniform measure. ALL phases supersonic
# (min M_entry = 1.02 > 1): Xi_sub is EMPTY, so nothing here belongs to
# the declared subsonic sector by the map's own definition.
N = 1000
xi = np.linspace(0.0, 1.0, N, endpoint=False)
m0 = 0.05
M_entry = 1.30 + 0.28 * np.sin(2 * np.pi * xi)          # in (1.02, 1.58)
assert M_entry.min() > 1.0                               # Xi_sub empty
marched = M_entry >= 1.0 + m0
routed = ~marched                                        # supersonic, routed
mu_r = routed.mean()
assert mu_r > 0.0, "toy must exercise the routed bucket"

# Per-phase true functional and models (synthetic, order-1 scale):
F_true = 1.0 + 0.10 * np.cos(2 * np.pi * xi)
# per-phase-2D march model: small genuine reduction error on marched set
F_2D = F_true + 0.010 * np.sin(4 * np.pi * xi)
# mixture-form booking (the only destination the routing sentence
# offers): as-if-subsonic booking of a supersonic phase carries its own
# model-form error, unpriced by any band of Part 3:
F_mix = F_true + 0.08

J_exact = F_true.mean()                                  # full measure

# READING (a): comparison restricted to the marched sector, renormalized
eps_marched_only = abs(F_true[marched].mean() - F_2D[marched].mean())

# READING (b): full-measure J_avg with routed phases booked via mixture
F_model_full = np.where(marched, F_2D, F_mix)
eps_routed_reading = abs(J_exact - F_model_full.mean())

gap = abs(eps_routed_reading - eps_marched_only)
routed_term = mu_r * abs((F_mix - F_true)[routed].mean())

print(f"mu_routed                    = {mu_r:.4f}")
print(f"eps reading (a) marched-only = {eps_marched_only:.6f}")
print(f"eps reading (b) routed-booked= {eps_routed_reading:.6f}")
print(f"|(a)-(b)| gap                = {gap:.6f}")
print(f"routed-sector term mu_r*err  = {routed_term:.6f}")

# ASSERT 1: the two spec-compatible readings genuinely diverge.
assert gap > 1e-3, "readings coincide -- attack void"

# ASSERT 2: the divergence is carried by the routed-sector term (within
# the marched-mean renormalization slack) -- i.e., a term proportional
# to the routed mass and the booking error: not an fp floor (~1e-16),
# not a curvature measured by the (D) sweep, not a declared [INF]
# constant of the spec.
assert gap > 0.5 * routed_term, (gap, routed_term)

# ASSERT 3: degenerate-limit control (L2 lens): as m0 -> 0+ the routed
# bucket empties and the ambiguity vanishes -- the defect belongs to the
# finite-m0 routing sentence, not to the floor idea itself.
marched0 = M_entry >= 1.0 + 1e-9
assert (~marched0).sum() == 0

print("ALL ASSERTS PASS: with mu_routed > 0 the published eps(F) is")
print("under-determined; the discrepancy term (mu_r x booking error) lies")
print("outside the published band algebra (fp-floor/curvature/[INF]).")
