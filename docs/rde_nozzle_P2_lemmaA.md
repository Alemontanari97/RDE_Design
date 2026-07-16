# P-2 LEMMA A DRAFT — §3 of the bridge paper: term-by-term identification
# of the Rao/Kraiko machinery with the continuous adjoint on the terminal
# characteristic

Status: DRAFT OF RECORD for paper §3 (2026-07-16, [F1/P-2]). Implements
§4 of docs/rde_nozzle_P2_outline.md (outline of record 05001a5).
Equation-numbered against the page-verified corpus D2 §b0 (Rao 1958
Eqs [1]-[15] with page numbers verified in-house vs GENO/literature/
RAO.pdf; Hoffman 1967 anchors: multiplier fields, single isoperimetric
multiplier p. 672, residual E Eq. 78, corner death p. 676). Every step
below is either DERIVED IN FULL (verifiable line by line) or explicitly
marked SCHEMA/PENDING with its falsifier. No "it can be seen that".

Rigor legend as in M0: THEOREM / THEOREM* / SCHEMA / CONJECTURE /
PRACTICE; PENDING = requires the A1 differentiable engine (O3 oracles)
or a declared page-level re-read, named per item.

------------------------------------------------------------------------------
## §3.0 Scope and conventions (declared once, used throughout)

SCOPE (as in outline §1): S1 piecewise-smooth class, smooth supersonic
region between the kernel and the terminal characteristic; steady,
inviscid, HOMENTROPIC (uniform h0, s), frozen gamma; planar (delta = 0)
or axisymmetric (delta = 1). Shock/sonic edges and reacting gas are
OUTSIDE Lemma A's smooth scope and are treated in paper §6 (Giles-
Pierce log singularity; G12; Hoffman boundary).

CHARACTERISTIC NAMING (trap of record, declared to the reader): we use
the Zucrow-Hoffman convention throughout — C- has slope tan(theta -
alpha), C+ has slope tan(theta + alpha), alpha = arcsin(1/M). Rao
1958/1961 calls "C+" what this convention calls C-: every equation
number cited from Rao is stated here ALREADY TRANSLATED (the in-house
corpus D2 §b0 performed and verified the translation page-by-page).
Bell/shroud terminal surface: C+ (slope theta + alpha). Plug/spike
terminal surface: C- (slope theta - alpha).

NORMALIZATION: Rao's integrands carry 2*pi*y (axisymmetric); we write
q := 2*pi*y^delta so planar and axisymmetric read identically. The
length multiplier lambda3 as derived below absorbs the 2*pi (see
remark after (L.13)); the corpus table's f1 = y^delta rho W^2 sin^2
theta tan alpha = -lambda3 is the same statement in the q-normalized
multiplier — a CONVENTION, not a discrepancy (checked 2026-07-16).

GAMMA-VARIABLE GENERALITY (standing audit of record, user directive
2026-07-16: every piece of the theory must state its variable-gamma
status explicitly). Audit of THIS derivation: §3.2 uses ONLY the Gibbs
relation along the isentrope (dh = dp/rho at fixed s), the definition
c^2 = dp/drho|_s, and trigonometry — no caloric closure. Therefore the
FULL classical stationarity system as derived here ((L.6)-(L.16):
characteristic surface, both first integrals, both corner conditions)
is EOS-GENERAL in primitive variables: it holds verbatim for frozen
gamma(T) and for arbitrary (convex) EOS, given homentropic
homenthalpic frozen flow — consistent with the corpus finding that the
equations are gamma-agnostic in primitive variables (D2 §b0 item 4)
and with the Kraiko-school arbitrary-EOS scope. The TRUE gamma = const
boundaries of the program lie ELSEWHERE and are named: (a) the
corner <-> eps closed-form BIJECTION used by implementations is
derived only for gamma = const (risk E4; oracle = Scofield-Hoffman
1971 Table 2 Case 1, frozen thrust 2290 lbf — gate G2); (b) T3's
Lemma B (stagnation-temperature similarity) REQUIRES calorically
perfect gas (M0, declared); (c) the S-H closed forms used at the eps
rung are gamma = const evaluations. Falsifier for (this) EOS-general
claim: exhibit a homentropic frozen-gamma(T) state where any of
(L.6)-(L.16) fails; the E4 oracle discharges the implementation-level
twin. Class: THEOREM (the audit is the proof trace above).

------------------------------------------------------------------------------
## §3.1 The classical control-surface problem (equation-numbered recall)

Unknown functions along the terminal control surface Sigma from the
kernel-exit point C to the lip E, parameterized by the ordinate y:
speed W(y), flow angle theta(y), surface slope angle phi(y) (so
dx/dy = cot phi along Sigma). Homentropic closure: p = p(W),
rho = rho(W) via Bernoulli/isentrope at fixed (h0, s).

Thrust functional (Rao 1958 Eq. [2], p. 378):

  (L.1)   F = Int_C^E [ (p - pa) + rho W^2 sin(phi-theta) cos(theta)
                        / sin(phi) ] q dy

Mass-flow constraint (Rao 1958 Eq. [1], p. 378; multiplier lambda2,
p. 379 col. 1):

  (L.2)   Int_C^E [ rho W sin(phi-theta) / sin(phi) ] q dy = mdot

Length constraint (Rao 1958 Eqs. [3]->[4], pp. 378-379; multiplier
lambda3):

  (L.3)   Int_C^E cot(phi) dy = x_E - x_C  (fixed)

Augmented Lagrangian (Rao 1958 Eq. [5], p. 379; third multiplier h = 0
by Guderley-Hantsch, Rao p. 379 col. 2):

  (L.4)   I = Int_C^E f dy,   f = f1 + lambda2 f2^i + lambda3 f3,
          f1 = [ (p-pa) + rho W^2 sin(phi-theta) cos(theta)/sin(phi) ] q,
          f2^i = [ rho W sin(phi-theta)/sin(phi) ] q,
          f3 = cot(phi).

(We write f2^i for the mass INTEGRAND to keep the symbol f2 for Rao's
first integral, matching the corpus and M0 T7(a).)

f contains no derivatives of (W, theta, phi): the Euler-Lagrange
system is ALGEBRAIC in the three unknowns —

  (L.5)   df/dphi = 0,   df/dtheta = 0,   df/dW = 0   on Sigma,

plus the endpoint (transversality) condition at the free lip E and the
MOC compatibility along Sigma (Rao 1958 Eq. [15], p. 379) which
certifies that Sigma-data extend to a genuine flow.

------------------------------------------------------------------------------
## §3.2 Complete derivation of the classical stationarity system
##       (class THEOREM — every line verifiable; re-derived 2026-07-16
##        and CHECKED against the page-verified corpus table)

Throughout set psi := phi - theta (surface inclination relative to the
flow) and alpha := arcsin(1/M), tan(alpha) = 1/sqrt(M^2-1), M = W/c.

STEP 1 (df/dphi = 0). Only sin(psi)/sin(phi) and cot(phi) depend on
phi. Using
  d/dphi [ sin(phi-theta)/sin(phi) ]
    = [ cos(phi-theta) sin(phi) - sin(phi-theta) cos(phi) ] / sin^2(phi)
    = sin(theta) / sin^2(phi)                       (angle-difference)
and d/dphi [cot(phi)] = -1/sin^2(phi):

  (L.6)   q rho W sin(theta) [ W cos(theta) + lambda2 ] = lambda3.

STEP 2 (df/dtheta = 0). Using d/dtheta [sin(phi-theta) cos(theta)] =
-cos(phi-2theta) and d/dtheta [sin(phi-theta)] = -cos(phi-theta):

  (L.7)   W cos(phi - 2 theta) + lambda2 cos(phi - theta) = 0
          =>  lambda2 = - W cos(psi - theta) / cos(psi).

STEP 3 (df/dW = 0). Homentropic derivatives (Bernoulli dh = dp/rho,
h + W^2/2 = h0; sound speed c^2 = dp/drho at fixed s):

  (L.8)   dp/dW = -rho W,      drho/dW = -rho W / c^2,
          d(rho W)/dW = rho (1 - M^2),   d(rho W^2)/dW = rho W (2 - M^2).

Hence

  (L.9)   -W + W (2 - M^2) sin(psi) cos(theta)/sin(phi)
          + lambda2 (1 - M^2) sin(psi)/sin(phi) = 0.

STEP 4 (combination => the surface is a characteristic). Insert (L.7)
into (L.9), multiply by sin(phi) cos(psi) / W with sin(phi) =
sin(psi + theta), expand cos(psi - theta) and sin(psi + theta) by the
addition formulas, and collect. The mixed terms sin(psi) cos(psi)
cos(theta) cancel IDENTICALLY (coefficient -1 + 2 - M^2 + M^2 - 1 = 0),
leaving

  (L.10)  sin(theta) [ (M^2 - 1) sin^2(psi) - cos^2(psi) ] = 0.

On the interior of Sigma with theta /= 0 (the theta = 0 root is the
degenerate axis branch, excluded on a thrust-carrying surface):

  (L.11)  tan^2(psi) = 1/(M^2 - 1) = tan^2(alpha)
          =>  phi = theta + alpha  (bell/shroud, C+)
              or  phi = theta - alpha  (plug/spike, C-).

This IS Rao 1958 Eq. [11] p. 379 (and Rao 1961-spike Eq. (5) p. 94 for
the C- branch): "the optimal control surface is a characteristic" falls
out of the algebra — a RESULT, not an assumption. [Corpus row checked.]

STEP 5 (the first integral f2). Insert phi = theta + alpha into (L.7):
psi = alpha, cos(psi - theta) = cos(theta - alpha) (cos even), so

  (L.12)  f2 := W cos(theta - alpha)/cos(alpha) = -lambda2   (C+ / bell)
          f2 := W cos(theta + alpha)/cos(alpha) = -lambda2   (C- / plug,
                by the same line with psi = -alpha)

= Rao 1958 Eq. [12] p. 379 (Veen Eq. 2 p. 1194); the corpus's
"W cos(theta -/+ alpha)/cos(alpha) = -lambda2" with the sign selected
by the characteristic FAMILY. Since lambda2 is a CONSTANT (isoperimetric
multiplier), f2 is CONSTANT ALONG THE TERMINAL CHARACTERISTIC — Rao's
first integral. [Corpus row checked.]

STEP 6 (the second first integral). Insert (L.12) into (L.6):
W cos(theta) + lambda2 = W [cos(theta) cos(alpha) - cos(theta - alpha)]
/ cos(alpha) = -W sin(theta) tan(alpha) (addition formula), hence

  (L.13)  q rho W^2 sin^2(theta) tan(alpha) = -lambda3.

= Rao 1958 Eq. [13] p. 379 (Veen Eq. 3 p. 1194). Remark (normalization
of record): with q = 2 pi y^delta this reads 2 pi [y^delta rho W^2
sin^2 theta tan alpha] = -lambda3; the corpus table's form absorbs the
2 pi into lambda3 — same statement. [Corpus row checked, convention
declared.]

STEP 7 (endpoint transversality = the corner condition). The lip
ordinate y_E is free; the isoperimetric totals (mdot, x_E - x_C) are
fixed data independent of the endpoint variation. The variation of
I with moving upper limit contributes the boundary term f|_E delta y_E,
so stationarity requires the AUGMENTED DENSITY TO VANISH AT THE FREE
ENDPOINT:

  (L.14)  ( f1 + lambda2 f2^i + lambda3 f3 ) |_E = 0.

Evaluate at E on the C+ branch (phi = theta + alpha), substituting
(L.12) for lambda2 and (L.13) for lambda3. The three velocity terms
collapse by the identity sin(alpha) + sin(theta) cos(theta + alpha) =
sin(theta + alpha) cos(theta) (write sin(alpha) = sin((theta+alpha) -
theta) and expand):

  (L.15)  (p - pa) - (1/2) rho W^2 sin(2 theta_E) tan(alpha) = 0
          <=>  sin(2 theta_E) = (p - pa) cot(alpha) / ((1/2) rho W^2).

= Rao 1958 Eq. [14] p. 379 (Rao 1961 Eq. [6] p. 1490). Equivalent
rearrangement: pa = p - (1/2) rho W^2 sin(2 theta) tan(alpha) — exactly
the CSTR_PA corner formula of M0 VI.3. The C- (plug) case follows by
the substitution alpha -> -alpha, under which every step of §3.2 goes
through verbatim (the only alpha-dependencies are phi = theta +/- alpha
and the odd function tan(alpha)):

  (L.16)  sin(-2 theta_G) = (p - p_b) cot(alpha) / ((1/2) rho W^2),

the CSTR_PB '+'-sign corner (M0 VI.3), base pressure p_b in place of
pa. The +/- comes from the CHARACTERISTIC TYPE, not from the sign of
theta. [Corpus rows checked: Veen Eq. 4 vs Eq. 8, p. 1194.]

STEP 8 (doctrinal consequence, carried by the algebra above). The
ambient/base pressure enters ONLY through the endpoint condition
(L.15)/(L.16) — there is no third integral multiplier (h = 0,
Guderley-Hantsch). This is the structure the averaged system inherits:
in M0 T7 the single-phase corner residual R(xi) is exactly the
left-hand side of (L.15) per phase, and (**') is its weighted
mu-average. [Verified against five primary sources, D2 §b0.]

Summary of §3.2: the complete classical machinery — Eq. [11]
(characteristic surface), Eq. [12] (f2 invariant), Eq. [13] (second
integral), Eq. [14]/CSTR_PA-PB (corner) — is DERIVED here from the
single Lagrangian (L.4) in eight verifiable steps, each matched to its
page-verified corpus row. Class THEOREM.

------------------------------------------------------------------------------
## §3.3 The continuous adjoint problem for the same objective
##       (class THEOREM for the structure; component closed forms cited)

Steady Euler in conservation form on the smooth supersonic region
Omega between the kernel exit characteristic, the wall W_d, and Sigma:

  (L.17)  d_x F(U) + d_y G(U) + (delta/y) S(U) = 0,
          U = (rho, rho u, rho v, rho E),
          S = (rho v, rho u v, rho v^2, rho v H).

Linearization about a state U: with A = F'(U), B = G'(U),
C = (delta/y) S'(U),

  (L.18)  L dU := d_x (A dU) + d_y (B dU) + C dU = 0.

Adjoint field psi = (psi1..psi4) and adjoint operator, from the
duality pairing (divergence theorem, no regularity subtleties in the
smooth region):

  (L.19)  Int_Omega [ psi^T L dU - (L* psi)^T dU ] dOmega
          = Oint_dOmega psi^T (A n_x + B n_y) dU ds,
          L* psi := -A^T d_x psi - B^T d_y psi + C^T psi.

PROP. A1 (adjoint characteristics = flow characteristics). The
characteristic slopes of L* are those of L: the characteristic
determinant of the adjoint system is det(A^T sigma_x + B^T sigma_y) =
det( (A sigma_x + B sigma_y)^T ) = det(A sigma_x + B sigma_y), since
det(M^T) = det(M). Hence the adjoint field propagates along the SAME
C+/C- Mach lines and the same streamlines as the flow. QED.
(Consistent with the characteristic decomposition constructed
explicitly by Lozano-Ponsin 2025 (bank B3) and, in quasi-1D, by
Giles-Pierce 2001 (bank B2).) Class THEOREM.

Objective and constraint on Sigma in flux form (momentum theorem;
equal to the wall form in the S1 class — paper §2):

  (L.20)  J = Int_Sigma g(U, n) ds,
          g = [ (p - pa) n_x + rho u_n u ] q / (2 pi y^delta) ... —
          concretely, parameterized by y with n ds = (sin phi, -cos
          phi) dy/sin phi scaled so that J and (L.1) are the SAME
          integral: g dy = f1 dy; likewise the mass flux integrand
          equals f2^i.

(The identification of the flux parameterization with (L.1)-(L.2) is
elementary bookkeeping: u = W cos theta, v = W sin theta, u_n =
W sin(phi - theta)/sin phi per unit dy along Sigma. Written out in the
paper appendix; no content beyond trigonometry.)

Augmented functional J + lambda2 (mdot[U] - mdot). Its first variation
against admissible interior perturbations dU (those satisfying (L.18)
with fixed inflow data on the kernel characteristic and slip on the
wall) is, by (L.19), a PURE BOUNDARY expression once psi solves the
adjoint PDE L* psi = 0 in Omega with:

  (L.21)  wall W_d:   psi-slip condition (the combination psi2 n_x +
          psi3 n_y carries the wall pressure sensitivity; standard
          continuous-adjoint wall b.c. for thrust objectives);
  (L.22)  Sigma:      psi^T (A n_x + B n_y) dU = -(dg/dU + lambda2
          d(mass flux)/dU) dU   for every admissible dU on Sigma.

Class of (L.17)-(L.22): THEOREM (structure; the bookkeeping is
integration by parts). The CLOSED-FORM solution psi(x,y) for thrust
objectives in supersonic 2-D flow is bank B3's contribution
(Lozano-Ponsin 2025); we do not re-derive it — Lemma A needs only its
restriction to Sigma, which §3.4 pins down independently.

------------------------------------------------------------------------------
## §3.4 The identification, term by term (the lemma proper)

(i) "OPTIMAL CONTROL SURFACE = CHARACTERISTIC" == ADJOINT CLOSURE
SURFACE. On a surface Sigma that is NON-characteristic (spacelike),
the admissible trace variations dU|_Sigma span the full state space
per point (all four characteristic fields cross Sigma): (L.22) then
prescribes all four components of psi^T (A n_x + B n_y) — the adjoint
data are fully determined and generically inconsistent with closing
the variation WITHOUT solving the interior adjoint PDE (the surface
"sees" upstream). On a CHARACTERISTIC surface, one characteristic
field is tangent: admissible variations lose one dimension, (L.22)
becomes a CODIMENSION-ONE condition, and stationarity can close on
Sigma-data alone. The classical computation §3.2 is exactly this
closure: conditions (L.6)/(L.7)/(L.9) admit a simultaneous solution
precisely when tan^2(psi) = tan^2(alpha), i.e. (L.11) — Sigma IS a
Mach line. Statement (i) of the outline is therefore DERIVED at the
structural level: the Rao surface is the surface on which the adjoint
problem needs no interior solve — the terminal characteristic through
the lip. Class THEOREM* (within §3.0 scope; the dimension-counting
argument is complete, the EXPLICIT verification that the B3 adjoint
components satisfy (L.22) on Sigma is the PENDING numeric term-match,
falsifier O3.3).

(ii) f2 = ADJOINT RIEMANN INVARIANT; MULTIPLIERS = ADJOINT BOUNDARY
DATA. By (L.12), f2 = -lambda2 is constant along the terminal
characteristic; lambda2 enters (L.22) as the coefficient of the mass
flux in the adjoint boundary datum. So the SAME object is, read
variationally, Rao's first integral and, read adjointly, the boundary
datum that the adjoint characteristic carries UNCHANGED along Sigma —
i.e. the adjoint invariant of the tangent family (Prop. A1: same
characteristics; an invariant along a characteristic of L is an
invariant along the same line for L*). The mass multiplier lambda2 is
therefore the (constant) adjoint datum injected at the lip by the
objective + constraint, and the length multiplier lambda3 is its
second-integral twin (L.13) generated by the geometric constraint
(f3 = cot phi is Rao's own third function; Hoffman-Scofield-Thompson
JOTA 1972 carry the same structure with lambda4 constant, HTH 1971
Eq. 5 p. 1582). Class THEOREM* — the identification of CONSTANTS with
BOUNDARY DATA is complete by (L.12)+(L.22); the identification of f2
with the explicit component combination of the B3 adjoint vector
(which specific linear combination of psi1..psi4 equals
W cos(theta -/+ alpha)/cos(alpha) on Sigma) is PENDING the symbolic
pass (falsifier O3.3: construct the B2/B3 analytic adjoint on the
terminal characteristic of one TOC case and subtract; any residual
beyond discretization kills the claim as stated).

(iii) CORNER CONDITION == ADJOINT TRANSVERSALITY. (L.14) is the
vanishing of the augmented density at the free endpoint — in optimal-
control language, the transversality condition at a free terminal
point; in adjoint language, the compatibility of the wall adjoint
condition (L.21) with the Sigma datum (L.22) where wall and terminal
characteristic MEET (the lip E). The derived forms (L.15)/(L.16) are
exactly CSTR_PA/CSTR_PB of M0 VI.3 with the sign fixed by the family
of the tangent characteristic. Class THEOREM* (same status as (i):
structure complete, explicit adjoint-component check PENDING O3.3).

(iv) HOFFMAN'S MULTIPLIER FIELDS == INTERIOR CONTINUOUS ADJOINT;
E == ADJOINT RESIDUAL. Verified anchors (page-level, in-house corpus):
Hoffman 1967 formulates reacting-flow nozzle optimization with
Lagrange-multiplier FIELDS lambda1..lambda4 (+lambda5 per species)
satisfying PDEs along the SAME characteristics as the flow (his
single isoperimetric constraint carries the constant multiplier,
p. 672); his a-posteriori residual E (Eq. 78) vanishes on optimal
contours; p. 676 proves the algebraic corner dies for reacting gas
(E = 0 replaces it). The identification: his field system is the
continuous adjoint system L* psi = 0 (with source/species terms) in
multiplier notation — "the 1967 paper contains the continuous adjoint
avant la lettre" — and E is the adjoint-PDE residual functional, i.e.
the ancestor of the Level-C stationarity certificate (M0 VI.6, O3.2).
Class SCHEMA at the component level: the STRUCTURAL identification is
carried by Prop. A1 (fields on flow characteristics = adjoint
characteristics) + the constraint-multiplier reading above; the
COMPONENT-BY-COMPONENT map lambda_i <-> psi_j (including his
normalization and his Eq. 78 written as a weighted L* residual) is
PENDING a page-level re-read of Hoffman's Eqs. beyond the verified
anchors (only Eq. 78 / p. 672 / p. 676 are page-verified in-house;
per the radical-honesty rule we cite NO further equation numbers
until read). Falsifier: O3.2 — evaluate E (Eq. 78 specialized to
frozen gas) on the AD-computed adjoint field of the A1 engine;
nonvanishing E on a converged optimum, or wrong convergence order,
kills the identification.

------------------------------------------------------------------------------
## §3.5 What the lemma yields downstream (one paragraph for the paper)

The bridge turns every classical contouring condition into an adjoint
object with a machine-checkable certificate: f2-constancy becomes the
adjoint-invariant drift diagnostic (already used as such in the GENO
implementation), the corner conditions become endpoint residuals
(O3.3), and Hoffman's E becomes the adjoint-PDE residual (O3.2) — the
certificate stack of the averaged RDE system (M0 T7: per-phase
closed-form adjoints assembled under the weighted transversality (**'))
inherits fifty years of classical machinery at zero marginal cost.
This is the content P-1 consumes (its §5).

------------------------------------------------------------------------------
## §3.6 Claim register for this draft (delta vs outline §8)

| Claim | Class (this draft) | Status | Falsifier |
|---|---|---|---|
| (L.11) surface = characteristic (classical derivation) | THEOREM | DERIVED §3.2, corpus-checked | algebra is self-contained; any error is checkable line-by-line |
| (L.12)/(L.13) first integrals | THEOREM | DERIVED §3.2, corpus-checked | idem |
| (L.15)/(L.16) corner = endpoint transversality | THEOREM | DERIVED §3.2 step 7, == CSTR_PA/PB | idem |
| Prop. A1 adjoint chars = flow chars | THEOREM | DERIVED §3.3 | det identity |
| (i) Rao surface = adjoint closure surface | THEOREM* (scope §3.0) | structure DERIVED §3.4 | O3.3 term-match on one TOC case |
| (ii) f2 = adjoint invariant; lambda2/lambda3 = boundary data | THEOREM* | constants<->data DERIVED; component combo PENDING | O3.3 |
| (iii) corner = adjoint transversality | THEOREM* | structure DERIVED | O3.3 |
| (iv) Hoffman fields = interior adjoint; E = adjoint residual | SCHEMA (component map PENDING page re-read) | anchors verified (Eq. 78, p. 672, p. 676) | O3.2 (E -> 0 at O(h^2) on converged optimum) |
| (L.6)-(L.16) are EOS-general (gamma(T) frozen, homentropic) | THEOREM (audit §3.0) | DERIVED (only Gibbs + c^2 def used) | any homentropic gamma(T) counterexample; E4 oracle for the corner<->eps implementation twin |

PENDING register (all named, per acceptance rule):
 P-A1 O3.3 symbolic/numeric term match vs B2/B3 analytic adjoint on
      one TOC case — needs the A1 differentiable MOC engine (or a
      standalone symbolic pass; either discharges it).
 P-A2 Hoffman component map lambda_i <-> psi_j — needs page-level
      re-read of Hoffman 1967 beyond the verified anchors (human/G5-
      adjacent library task; NO equation numbers to be cited before).
 P-A3 O3.2 E-residual evaluation on the AD adjoint field — A1 engine.
None of P-A1..P-A3 blocks Lemma A as classed above; they discharge the
THEOREM*->THEOREM upgrades and the (iv) SCHEMA->THEOREM* upgrade.
