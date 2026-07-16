# N6 attacked — swirl: structure theorems, the free-vortex extension,
# and the sharp negative (field-level necessity)

Status: RIGOR ATTACK OF RECORD (2026-07-16, Sessione 8-rigore
riaperta, [F1/N6-S1]). Target: the N6 gap ("no transfer of Rao's
closed-form machinery to swirl/3-D"). Carrier:
validation/n6_swirl_kernel.py (PASS 16/16, rejector + sharp negative
control). Gamma status: EVERYTHING here is EOS-general (c^2 free
symbol; closure only through dh = dp/rho on the isentrope).

VERIFICATION-SUFFICIENCY DISCIPLINE (standing user directive, this
session): every claim below declares whether SYMBOLIC verification
SUFFICES (the claim is a finite algebraic identity — the machine
check IS the proof) or the claim lives in FUNCTION SPACE (existence,
regularity, limits — symbolic checks are consistency only, the
analytic content is named and classed separately).

------------------------------------------------------------------------------
## §1 THEOREM N6-1 (swirl structure — symbolic SUFFICES, closed)

Axisymmetric steady Euler WITH swirl, V = (rho, u, v, w, p) in
(x, r); swirl w enters the FLUXES only through its transport row
(theta-momentum) and the geometry only through SOURCES (centrifugal
rho w^2/r in r-momentum; -rho v w/r in theta-momentum). Machine-
verified identities (each a finite algebraic fact — symbolic check =
proof):
 (a) det A_p = u^3 (u^2 - c^2): the x-marching matrix is invertible
     exactly under AXIAL supersonicity — unchanged criterion.
 (b) det(B_p - lambda A_p) = (v - lambda u)^3 [ (v - lambda u)^2 -
     c^2 (1 + lambda^2) ]: characteristics = streamline family now
     TRIPLE (entropy, h0, and the swirl invariant Gamma = r w) + the
     SAME MERIDIONAL Mach lines as the swirl-free case. Sources do
     not touch the pencil.
 (c) Kernel lemma with swirl (Prop. A2 analogue): at u_n = c the
     acoustic kernel eigenvector is r- = (rho, -c n_x, -c n_r, 0,
     rho c^2) — swirl component EXACTLY ZERO — and the thrust/mass
     trace covectors annihilate it by the SAME laws
     <grad g, r-> = rho (u_n - c)(u - c n_x), <grad m, r-> =
     rho (u_n - c).
CONSEQUENCES (imports classed separately): the ENTIRE G12-S1
machinery extends to swirling flow verbatim — x-as-time evolution
reading (with three transport rows instead of one), front brick
(K_p(n) 5x5, det ∝ u_n^3 (u_n^2 - c^2), linearized RH nonsingular
inside Lax, degeneration exactly characteristic), adjoint boundary
solvability. The IMPORT of the Li-Yu semiglobal theory is a
FUNCTION-SPACE step: it inherits the D2.5 conditional exactly as in
G12-S1 (beyond symbolic, named, nothing new assumed).

------------------------------------------------------------------------------
## §2 THEOREM N6-2 (free-vortex extension — symbolic SUFFICES for the
##     identities; one-line analytic closure justification)

Claim: for FREE-VORTEX swirl — uniform Gamma_0 = r w, uniform h0 and
s (homenergetic, homentropic) — the COMPLETE classical stationarity
system of Lemma A ((L.6), (L.7), (L.10) characteristic factorization,
(L.12) both families, (L.13), corner (L.15)) holds VERBATIM with W =
MERIDIONAL speed: Rao's control-surface machinery extends to this
swirl class UNCHANGED.
Proof, two steps:
 (i) CLOSURE (analytic, one line, machine-checked): the meridional
     Bernoulli h = h0 - W^2/2 - Gamma_0^2/(2 y^2) gives, AT FIXED y,
     dh/dW = -W, hence with dh = dp/rho on the isentrope:
     dp/dW|_y = -rho W and drho/dW|_y = -rho W/c^2 — the EXACT
     closure rules of the classical derivation, now for two-argument
     p(W, y), rho(W, y).
 (ii) EL IDENTITIES (symbolic SUFFICES): the classical derivation
     takes ONLY d/dW, d/dtheta, d/dphi at fixed y — never d/dy — so
     with the rules of (i) every identity closes unchanged
     (machine-verified re-run, Part B2, including the corner and the
     corrupted-corner rejector). QED.
Scope notes (declared): the thrust flux is the AXIAL momentum flux —
swirl contributes none directly (its kinetic energy is unrecoverable
axial thrust, consistently with the G-B ceiling's V_id built on total
h(s, Pa)); the MOC compatibility along Sigma acquires swirl source
terms (flow-side consistency, not used by the EL derivation); Lax
front analysis carries over by N6-1.

------------------------------------------------------------------------------
## §3 THEOREM N6-3 (the sharp negative — symbolic verifies the
##     obstruction identity; the "only-if" beyond it is SCHEMA)

Claim (obstruction — symbolic SUFFICES): for NON-uniform Gamma(psi)
or h0(psi) (or s(psi)), the fixed-y W-derivative of h along the
control surface acquires the extra term
    dh/dW|_y = -W + (h0' - Gamma Gamma'/y^2) dpsi/dW,
which vanishes identically IFF Gamma' = h0' = 0 (machine-verified,
Part B3): the pointwise closure p = p(W, y) used by every control-
surface derivation FAILS beyond the free-vortex class — the state on
Sigma depends on the variation through the streamline label psi.
CONSEQUENCE (classed honestly): the STANDARD control-surface
reduction (Rao two-constant machinery) does not extend beyond free
vortex; the FIELD-LEVEL machinery (five-field multiplier system, §4;
equivalently reverse-AD of the march) is NECESSARY there. This
UNCONDITIONALLY grounds M0 VI.4bis(iv). The stronger statement "NO
alternative pointwise reduction exists" is SCHEMA (a different
change of variables might conceivably restore a closure; none is
known; falsifier: exhibit one).

------------------------------------------------------------------------------
## §4 The five-field variational system (SCHEMA — function space,
##     beyond symbolic; derivation route named)

For general swirl the per-phase optimality system is the Hoffman-type
FIELD formulation with FIVE multiplier fields (continuity, x-mom,
r-mom, theta-transport, energy row), sources included (centrifugal
couples r-mom; -vw/r couples the transport). Route (named, per the
Hoffman-1967 map of record): adjoin the five quasilinear rows, vary
(u, v, w, P, rho), Green's theorem, boundary counting on the terminal
MERIDIONAL Mach line via the N6-1 kernel degeneracy (one condition
lost — the same Hoffman-p.673/Prop.-A2 mechanism, now machine-
verified in the swirl pencil), wall and endpoint transversality with
the centrifugal contributions. Deliverables when discharged: the
swirl corner conditions and the five-field terminal data (the
analogue of Eqs. (31)-(34)). CLASS: SCHEMA until derived; the
COUNTING ingredient is already THEOREM (N6-1(c)). Algorithmic note:
this is the only rigor item with real (contained) implementation
delta — one unknown/equation per unit process + one adjoint row +
a swirl oracle (M0 VI.4bis(iv) unchanged).

------------------------------------------------------------------------------
## §5 Claim register (with verification-sufficiency column)

| Claim | Class | Symbolic suffices? | Carrier / residue |
|---|---|---|---|
| N6-1(a,b,c) swirl structure (pencil, kernel, laws) | THEOREM (EOS-general) | YES — finite algebraic identities | n6_swirl_kernel.py Part A |
| G12-S1 extension to swirl (marching + front) | THEOREM* | structure YES; Li-Yu import NO (function space, inherits D2.5) | G12-S1 doc + Part A |
| N6-2 free-vortex verbatim extension | THEOREM | YES (identities) + one-line closure justification | Part B1-B2 + rejector R1 |
| N6-3 obstruction identity (closure fails iff not free vortex) | THEOREM | YES | Part B3 (double control) |
| N6-3 strong only-if (no alternative reduction) | SCHEMA | NO — needs a classification argument | falsifier: exhibit a reduction |
| Five-field optimality system | SCHEMA | NO — calculus of variations in function space | route named; counting brick already THEOREM |
