"""R22F-L1-4 probe (refuter round 1, lens L1) — per-part vs joint mass
nullity of the distributional phi-derivative of a periodic BV composite.

TARGET CLAIM (phaseD_r22f_centerpiece.md, Part 2 per-term disposition
table, front-atom row): "signed-mass-zero BOUNDED here (inside K-bar = 0)".
ATTACK: the ATOM part alone of D_phi F for a periodic BV composite has, in
general, NONZERO signed mass; only the JOINT mass (a.c. + Cantor + atoms)
vanishes (judgeverify ITEM 3.3, which itself books the atom mass INTO the
(J) channel). A per-term/per-part "signed-mass-zero" reading is therefore
false; the row wording must claim joint nullity only.

COUNTEREXAMPLE (periodic BV composite, one front crossing per period, the
minimal member of the H-RED-2 class): F(phi) = sin(3 phi) + c*phi on
[0, 2pi), extended periodically. Then
  D_phi F = (3 cos(3 phi) + c) d(phi)  -  2 pi c * delta_{phi=0},
  a.c. mass = 2 pi c != 0,   atom mass = -2 pi c != 0,   total = 0.
With a CONSTANT weight psi: <psi, D F> = 0 but <psi, atoms> = -2 pi c psi
!= 0 — the atoms are "bounded" only jointly with the a.c. part.

Tolerance: derived, not magic — trapezoid a.c. quadrature error is
O(h^2 * ||F'''||); we use 10 * (2*pi)^3 * max|F'''| / N^2 + 100*eps.
Env: pinned, numpy only (no installs).
"""

import numpy as np

c = 0.7            # ramp slope -> atom mass -2*pi*c (any c != 0 works)
N = 200_001        # quadrature nodes over one period

phi = np.linspace(0.0, 2.0 * np.pi, N)
h = phi[1] - phi[0]

# a.c. density of D_phi F on (0, 2pi): F'(phi) = 3 cos(3 phi) + c
ac_density = 3.0 * np.cos(3.0 * phi) + c
ac_mass = np.trapezoid(ac_density, phi)

# atom at the periodic seam: jump [F] = F(0+) - F(2pi-) = -2*pi*c
atom_mass = (0.0) - (c * 2.0 * np.pi)   # sin part continuous at seam

total_mass = ac_mass + atom_mass

# derived tolerance: trapezoid error bound + float headroom
tol = 10.0 * (2.0 * np.pi) ** 3 * 27.0 / (N - 1) ** 2 + 100.0 * np.finfo(float).eps

print(f"a.c. mass    = {ac_mass:+.12e}   (exact +2*pi*c = {2*np.pi*c:+.12e})")
print(f"atom mass    = {atom_mass:+.12e}   (exact -2*pi*c)")
print(f"total mass   = {total_mass:+.12e}   (must be 0: joint nullity)")
print(f"derived tol  = {tol:.3e}")

# REJECTOR structure: both assertions can fail independently.
assert abs(total_mass) < tol, "joint nullity FAILED - would kill K-bar=0 itself"
assert abs(atom_mass) > 1.0, "atom mass vanished - counterexample degenerate"

# constant-weight pairing: <psi, DF> = 0 but <psi, atoms> != 0
psi = 1.3
pair_total = psi * total_mass
pair_atoms = psi * atom_mass
print(f"<psi, D F>   = {pair_total:+.12e}   (0: mean channel dead, total only)")
print(f"<psi, atoms> = {pair_atoms:+.12e}   (NONZERO: no per-part nullity)")
assert abs(pair_total) < abs(psi) * tol
assert abs(pair_atoms) > 1.0

print("\nVERDICT: per-part 'signed-mass-zero' for the atom content is FALSE")
print("on the minimal H-RED-2 composite; only JOINT nullity holds. The")
print("front-atom table cell must claim joint nullity (atom mass books into")
print("the (J) pairing), exactly as judgeverify ITEM 3.3 states.")
