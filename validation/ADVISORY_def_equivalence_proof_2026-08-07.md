# ADVISORY — Equivalence of GENO's Lambda-form validity boundary with
# Rao-Beck Eq. (4), hand proof of record (2026-08-07, inter-session
# window after S20 closure; to be ratified/absorbed at S21 opening)

STATUS: advisory (untracked, ADR/PANEL pattern). Independent
verification by the def-equivalence panel (workflow wf_706f7901-32d,
sub-question S4) pending at the time of writing. Rigor class of the
content below: THEOREM-level algebra (every step displayed), scope
declared.

SCOPE: homentropic irrotational per-phase flow (single isentrope, so
alpha = alpha(V)); axisymmetric; left-Mach-line control surface
(bell branch). This is the SAME scope as the f2 invariant itself —
consistent with the 2026-08-07 audit finding that the closed-form
family is scoped to the irrotational homentropic subclass.

## 1. Objects

Rao & Beck, AIAA 94-3264 (page-verified in full, GENO/literature):
 Eq. (1)  V cos(theta - alpha)/cos alpha = const on the surface DE
 Eq. (3)  (dV/V) cot alpha - dtheta = (dR/R) sin alpha cos theta / sin(theta+alpha)
 Eq. (4)  ((gamma - cos 2alpha)/sin 2alpha) * (sin theta/(cos(theta-alpha) cos alpha))
          + tan(theta-alpha)/tan alpha = 1        [perfect gas, at D]

GENO (src/lib/Rao_m.f90, boundaryfunction_solve, lines ~24-56):
 val = [Lambda*B*(A+B) - (A-B)] / [1 + Lambda*(A+B)]
 A = tan(theta-alpha), B = tan alpha, Lambda = V * dalpha/dV
 (Lambda by central finite difference on the tabulated thermo
 backend, dV_pert = 1 m/s; valid side = val > 0).

## 2. Derivation of the general boundary (G)

Log-differentiate Eq. (1):
 dV/V - tan(theta-alpha) (dtheta - dalpha) + tan alpha dalpha = 0   (1')
On an isentrope alpha = alpha(V): dalpha = Lambda dV/V. Substitute:
 (dV/V) [1 + Lambda (A+B)] = A dtheta                               (I)
Insert (I) into Eq. (3), cot alpha = 1/B:
 dtheta * [A - B - Lambda B (A+B)] / (B [1 + Lambda (A+B)])
   = (dR/R) sin alpha cos theta / sin(theta+alpha)
The bracket is exactly -val * [1 + Lambda(A+B)] of GENO. Hence
val = 0  <=>  nontrivial (dV, dtheta, dalpha) exist with dR = 0 —
the surface march degenerates ("seeking nontrivial solutions for
dalpha and dtheta from Equations (1) and (3)", Rao-Beck verbatim).
General boundary:
 (G)  tan(theta-alpha) - tan alpha
        = Lambda * tan alpha * (tan(theta-alpha) + tan alpha)

## 3. Perfect-gas reduction of (G) = Eq. (4)

Perfect gas: c^2 = gamma R T, V dV + 2 c dc/(gamma-1) = 0
 => dc/dV = -(gamma-1) V / (2c). From sin alpha = c/V:
 Lambda = V dalpha/dV = -[(gamma-1)V^2 + 2c^2] / (2 c V cos alpha)
        = -(gamma - cos 2alpha)/ sin 2alpha
 (using c = V sin alpha, (gamma-1) + 2 sin^2 alpha = gamma - cos 2alpha).
Substitute in (G); Eq. (4) times tan(alpha) rearranges to
 tan(theta-alpha) - tan alpha
   + ((gamma - cos 2alpha)/sin 2alpha) * sin theta sin alpha /
     (cos(theta-alpha) cos^2 alpha) = 0.
The two coincide iff
 tan alpha (A+B) = sin theta sin alpha / (cos(theta-alpha) cos^2 alpha),
and by the sine addition formula
 A + B = sin theta / (cos(theta-alpha) cos alpha),
which makes the identity exact. QED: (G) with the perfect-gas Lambda
IS Eq. (4).

## 4. Sign-convention check (numeric spot check, gamma = 1.4)

 (theta, alpha) = (8 deg, 8 deg):  val ~ +0.14 > 0  -> VALID
 (theta, alpha) = (14 deg, 5 deg): val ~ -0.30 < 0  -> INVALID
Matches Rao-Beck Fig. 2 (valid region = smaller theta / larger
alpha; val > 0 = valid side as GENO assumes).

## 5. Consequences of record (pending S21 ratification)

(a) GENO's DEF implementation is FAITHFUL to Rao-Beck AND correctly
    generalized to variable gamma / tabulated EOS: the boundary via
    the Lambda-form (proven above), the PM jump integrated on the
    actual thermo (dq = q tan(alpha) dtheta with alpha(q) from
    td%solve), termination ON the boundary, E by DE<->BD mass
    matching (the paper's design constraint; A4 assert).
(b) Residual GENO caveats (hygiene, not structure): no CTest case
    exercises flagdef=1 (DEF branch effectively untested by the
    suite); magic tolerances in the PM loops (1e-8 abs on q, the
    (0,1e-6) boundary window, dtheta_0 = -0.001, floor 1e-12,
    dV_pert = 1.0); float .ne. comparisons in the flagdef test;
    den-guard val=0 at the fold singularity is conservative but
    heuristic. Suggested: a KAT comparing boundaryfunction_solve on
    synthetic gamma=1.4 thermo against Eq. (4) closed form, plus one
    DEF regression case.
(c) The (G) form with Lambda from OUR C^1 tabulated backend is the
    EOS-general validity margin the rde-lecture-code program needs
    for the S21 monitor and the margin-constrained (A') formulation
    — derived, citable, and cross-checkable against GENO's
    implementation. Scope stays homentropic-irrotational per phase;
    the general-engine tier owns the extension.
