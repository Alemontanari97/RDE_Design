"""R22F v2 round-3 L1 probe: grid-scan min vs refined/continuum min of a
margin field — the domain-margin floor certificate ([REV2-r2-5](a)) can
FLIP under mesh refinement when a near-sonic strip is narrower than the
local axial spacing.

Consumed by finding R22F-L1-13 (phaseD_r22f_refute_r3_l1.md).

Model: the marched-domain margin field g(x) = M_march(x) - 1 on [0, 1]
with a smooth background level and ONE narrow dip (Gaussian) centered
BETWEEN two nodes of the coarse march grid. The dip width is a PHYSICAL
parameter (set by front geometry / post-front expansion length), not a
mesh parameter: refining the march reveals it, coarsening hides it.

The floor check of record is "min over the marched domain ... checked A
POSTERIORI from the march output (one scan)". At mesh h the one-scan min
is the DISCRETE min of the computed field; the licensing consumer (B-4's
ln-truncation argument, sec 2.4 limit-L3 logic) consumes the continuum
margin. This probe shows: floor PASSES at the coarse mesh, FAILS at the
refined mesh -> a mesh-dependent licensing certificate unless the check
is tied to the registered refinement discipline.

No external-paper number is used (CT-6 clean). Pinned env, numpy only.
All tolerances are exact constructed values (no magic constants).
"""

import numpy as np

# --- construction -----------------------------------------------------------
m0 = 1e-2          # declared per-family floor (illustrative; any m0 > 0 works)
bg = 10.0 * m0     # background margin level, comfortably above the floor
dip_min = m0 / 100.0   # true continuum minimum of the margin field
x0_frac = 0.5      # dip centered midway between two coarse nodes (see below)

N_coarse = 101                      # coarse march grid on [0, 1]
h = 1.0 / (N_coarse - 1)            # coarse spacing
sigma = h / 8.0                     # PHYSICAL strip half-width << h
# center the dip exactly midway between nodes i0 and i0+1:
i0 = N_coarse // 2
x_dip = (i0 + x0_frac) * h

def margin(x):
    """g(x) = M_march(x) - 1: background with one narrow Gaussian dip."""
    return bg - (bg - dip_min) * np.exp(-0.5 * ((x - x_dip) / sigma) ** 2)

# --- the one-scan check at the coarse march mesh ----------------------------
x_c = np.linspace(0.0, 1.0, N_coarse)
g_c = margin(x_c)
min_c = g_c.min()

# nearest coarse node sits h/2 from the dip center: attenuation factor
# exp(-0.5 * (h/2/sigma)^2) = exp(-0.5 * 16) = exp(-8)  (derived, not magic)
atten = np.exp(-0.5 * ((h / 2.0) / sigma) ** 2)
assert atten == np.exp(-8.0)

# A1: the coarse one-scan check PASSES the floor (min >= m0), because the
# dip is invisible at spacing h.
assert min_c >= m0, (min_c, m0)

# A2: the continuum minimum VIOLATES the floor by 100x (constructed).
assert abs(margin(x_dip) - dip_min) < 1e-15 * bg
assert dip_min == m0 / 100.0 < m0

# --- the same one-scan check after one registered refinement ladder ---------
# refine until spacing resolves the strip: 16x refinement -> h/16 = sigma/...
N_fine = 16 * (N_coarse - 1) + 1
x_f = np.linspace(0.0, 1.0, N_fine)
g_f = margin(x_f)
min_f = g_f.min()

# A3: the refined one-scan check FAILS the floor: certificate FLIPS.
assert min_f < m0, (min_f, m0)

# A4: the flip is not marginal — the refined min sits at least 10x below
# the floor (dip_min = m0/100; nearest fine node within h/16 of center,
# attenuation exp(-0.5*(h/16/sigma)^2) = exp(-0.5) at worst).
assert min_f <= m0 / 10.0, (min_f, m0 / 10.0)

# A5: collapse factor coarse-scan-min / true-min >= 100x class
assert min_c / min_f >= 10.0
assert min_c / dip_min >= 100.0 * (1.0 - 1e-12)

print("A1 PASS: coarse one-scan min = %.3e >= m0 = %.3e (floor PASSES at mesh h)"
      % (min_c, m0))
print("A2 PASS: continuum min = %.3e = m0/100 (floor violated in the continuum)"
      % dip_min)
print("A3 PASS: refined one-scan min = %.3e < m0 (certificate FLIPS at h/16)"
      % min_f)
print("A4 PASS: refined min <= m0/10")
print("A5 PASS: coarse-scan/true-min collapse factor = %.0fx" % (min_c / dip_min))
print("ALL ASSERTS PASS")
