# S1-internal uniqueness — statement and proof architecture
# (canonicity across fitted shocks, attacked)

Status: RIGOR ATTACK OF RECORD (2026-07-16, Sessione 8-rigore,
[F1/S1-uniq]). Target: upgrade the D2.5 canonicity conditional from
"declared, backed by Majda stability" to a stated theorem with the
load-bearing bricks PROVEN and the remaining analysis NAMED.
Verification-sufficiency discipline: this item is intrinsically
FUNCTION-SPACE — no symbolic carrier can close it; what the machine
HAS closed are its two finite-dimensional bricks (G12-L1 structure,
G12-L2 front nonsingularity). Honest class: SCHEMA with proven
bricks; target THEOREM* under the D2.5 estimates.

------------------------------------------------------------------------------
## §1 Statement (target)

THEOREM S1-U (target; class SCHEMA -> THEOREM* when §3 is
discharged). Let U, U~ be two S1 solutions on the same finite
x-interval with the same wall, the same axially supersonic data
(uniform margin), each piecewise C^1 with the SAME finite number of
noninteracting Lax-transversal fitted fronts (graphs over x,
uniform strength margins). Then U == U~ (and the fronts coincide):
the S1 solution is UNIQUE WITHIN THE S1 CLASS.
Scope honesty: this is uniqueness INSIDE the piecewise-smooth class —
it does NOT touch the multi-D entropy-weak non-uniqueness (wild
solutions), which remains the field-level open problem; but it is
exactly the statement the pipeline needs (canonicity among the
objects the pipeline can produce and certify).

------------------------------------------------------------------------------
## §2 The two proven bricks (machine-verified, symbolic sufficed)

 B1 (G12-L1): under the audited margin the system is a 1-D-in-x
    hyperbolic evolution (invertible A_p, real complete
    characteristic structure) — so the comparison problem is a
    1-D-in-time uniqueness problem with internal free boundaries.
 B2 (G12-L2): the linearized RH map at each front is NONSINGULAR
    strictly inside the Lax condition (equilibrated s_min certified);
    hence the front position and downstream trace of one solution
    are LOCALLY LIPSCHITZ functions of the incoming trace — the
    quantitative ingredient for a front-distance Gronwall.

------------------------------------------------------------------------------
## §3 The assembly (function space — beyond symbolic; steps named)

 A1 Region step: on the common smooth region between fronts, the
    difference of two C^1 solutions of the same quasilinear
    hyperbolic system with the same data obeys an energy/Gronwall
    estimate in x (classical two-variable theory; equivalently the
    relative-entropy argument, which in Lipschitz regions is of
    record via D2.5). Needs: uniform C^1 bounds = the D2.5
    semiglobal estimates (inherited conditional, nothing new).
 A2 Front step: where the two solutions' fronts differ, straighten
    both by the same transform; the front-distance delta sigma(x)
    obeys d(delta sigma)/dx <= C (trace difference) by B2; the trace
    difference is controlled by the region estimate A1 up to that x.
 A3 Induction on the (finite, equal) front count, marching in x:
    Gronwall closes region-by-region and front-by-front on the
    finite interval. QED (architecture).
Named residues: (R-U1) the A1 estimate across the WALL boundary
(characteristic boundary at slip walls — standard but must be
written); (R-U2) the "same front count" hypothesis: two S1 solutions
with DIFFERENT front counts are not excluded by this argument
(excluded in practice by the a-posteriori S1 certificate that counts
fronts; declared); (R-U3) the constants' uniformity = D2.5
conditional.

Falsifier: two distinct certified S1 solutions with identical wall,
data, margins and front count (any such pair kills S1-U as stated).

Consequence when discharged: D2.5 canonicity across shocks upgrades
from "declared conditional" to THEOREM* within the class the
pipeline certifies — the Verdict's solution-concept caveat becomes a
checked hypothesis (margins + front count), closing residue R-P3.1
of the P3 theorem as well.
