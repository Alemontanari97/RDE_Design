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

LEXICAL TRAP OF RECORD (footnote for the paper, D2 §b0bis finding,
inserted S8 per PROGRESS NEXT-4): Rao-Beck AIAA 94-3264 speaks of
"variational calculus with ADJOINT constraints" — there "adjoint"
means ADJOINED (isoperimetric constraints appended to the functional
with constant multipliers), NOT the adjoint PDE problem of this
lemma. The two usages are unrelated; a reader (or referee) equating
them would read the bridge lemma as already published, which it is
not. The paper carries this as a footnote at the first occurrence of
"adjoint" in §3.

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
and with the Kraiko-school arbitrary-EOS scope.
ATTRIBUTION OF RECORD (D-07, 2026-08-13): the EOS-generality of the
Route-A first integrals is CLASSICAL AND FROM 1957 — Sternin obtained
the analogous relations for arbitrary two-parametric gas (Kraiko 2001
p.1348: "In the same year Sternin obtained analogous relations for
arbitrary two-parametric gas using the same technique"; published
1959), while Shmyglevskii 1957 is perfect-gas. THIS AUDIT IS A
RE-DERIVATION/extension of a 1957 result, never new generality.
Route-A lineage of record (cited "according to the account of Kraiko
et al. 2001, a party to the priority dispute"): Nikolskii (1950,
publ. 1957) -> Guderley-Hantsch 1955 (seat of the Busemann condition)
-> Shmyglevskii 1957 and Sternin 1957/59 -> Rao 1958/1961; priority
of OBTAINMENT to Sternin, of PUBLICATION in scientific print to Rao;
the Borisov-Shmyglevskii critique of Rao's METHOD does not touch the
result, and Rao revised the work (Miele ed. 1965). Independent
support: the Busemann condition Eq. (1) contains only primitive
variables (p, rho, V, alpha) — the endpoint condition is EOS-general
and the gamma = const dependence is a choice of expression. FORBIDDEN
PHRASE of record (claim 12 rider): the unqualified "first to do Rao
with variable gamma" — Sun 2019 (with Sun & Yu 2018, Chinese, unread)
is prior art occupying the "Rao-type construction with gamma(T)"
move; claim 12 stays INTACT because it is a MATHEMATICAL statement
about the stationarity system in primitive variables, an object that
does not exist in Sun 2019. The TRUE gamma = const
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

PROP. A2 (KERNEL SOLVABILITY on characteristic surfaces — THEOREM,
EOS-general (c fully symbolic), machine-verified: carrier
validation/pa1_symbolic_lemmaA.py Part 2, with family-specificity
rejector). Let Sigma be a Mach-characteristic surface (u_n = c, unit
normal n) and K_p(n) the primitive normal Jacobian, whose kernel at
u_n = c is spanned by the acoustic eigenvector
r- = (rho, -c n_x, -c n_y, rho c^2)^T. Then the trace covectors of
BOTH boundary functionals annihilate the kernel IDENTICALLY:
    <grad_V g, r-> = rho (u_n - c)(u - c n_x)  -> 0 on Sigma,
    <grad_V m, r-> = rho (u_n - c)             -> 0 on Sigma,
(g = thrust flux, m = mass flux; the conservative-variable statement
follows since grad_V = (dU/dV)^T grad_U and ker K_c = (dU/dV) ker K_p).
CONSEQUENCE: the adjoint boundary condition (L.22) on a characteristic
Sigma is SOLVABLE for psi for EVERY value of lambda2 — mere
admissibility/solvability imposes NO pointwise condition on Sigma.
The same contractions with the opposite-family eigenvector r+ do NOT
vanish (rejector-checked): the degeneracy is specific to the tangent
family. Computed fact of record (NOT an f2 claim): the off-surface
kernel ratio <grad g, r->/<grad m, r-> = u - c n_x equals
W cos(alpha) cos(theta+alpha) on the C+ surface — it does NOT
reproduce f2: the invariant does not live in the pointwise boundary
algebra.

INDEPENDENT DUAL-ROUTE VERIFICATION of Prop. A2 (2026-07-16, session
S7 — operational session run concurrently, reconciled; carrier
validation/p2_pA1_symbolic_adjoint.py): the same annihilation
identity re-verified in CONSERVATIVE variables (the variable set the
Lemma-B discrete engine transposes), with a general-EOS Grueneisen
closure (p(rho, rho e); a, b free; exact c^2 = a + b h),
Weierstrass-exact zero tests, the explicit LEFT null covector
l.dU = dp - rho u_n du_n (l^T K = 0), the rank-3 certificate, three
negative controls (non-characteristic surface det K != 0; corrupted
datum; corrupted kernel), and the executable (L.20) bookkeeping
check (g ds = f1 dy, rho u_n ds = f2^i dy). It also records the
BOUNDARY-DATUM READING lemma (weaker than Prop. A3 by design,
consistent with Prop. A2): for any probe w with <grad m, w> = 1,
<grad g, w> = 0, the gauge-independent combination psi.(K w) equals
-lambda2 for EVERY adjoint solution — the constants <-> boundary
data half of (ii) in executable form; the transport half remains
Prop. A3's content, already of record.

------------------------------------------------------------------------------
## §3.4 The identification, term by term (the lemma proper)

(i) "OPTIMAL CONTROL SURFACE = CHARACTERISTIC" == ADJOINT CLOSURE
SURFACE. [REFINED 2026-07-16, rigor session: the first draft justified
this by a dimension-count on admissible trace variations; Prop. A2
shows that count is TOO LOOSE — for flux-type functionals the adjoint
boundary data are solvable on a characteristic surface for EVERY
lambda2, so mere solvability imposes nothing. The refined route:]
The content of Rao's conditions in adjoint language is NOT the
solvability of (L.22) but the STATIONARITY CLOSURE: requiring the
first variation of the augmented functional to vanish against all
pointwise surface-data variations (delta W, delta theta, delta phi) —
the calculus of §3.2 — is possible on Sigma-data alone precisely when
the three algebraic conditions (L.6)/(L.7)/(L.9) are simultaneously
solvable, which the factorization (L.10) shows happens exactly at
tan^2(psi) = tan^2(alpha), i.e. (L.11): Sigma IS a Mach line, and it
is the surface on which the adjoint problem needs no interior solve
(the terminal characteristic through the lip). In adjoint language
the closure is a statement about the TANGENT-FAMILY TRANSPORT along
Sigma (see (ii)), for which the characteristic surface is the only
carrier. Class THEOREM* (within §3.0 scope; the variational half is
THEOREM by §3.2 + machine verification; the adjoint-transport half is
the narrowed PENDING P-A1' — DISCHARGED 2026-07-16, see the PENDING
register; residual falsifier O3.3 [C-O33]).

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
BOUNDARY DATA is complete by (L.12)+(L.22). [Class of record since
the P-A1' discharge (2026-07-16, PENDING register below): THEOREM in
the §3.0 scope — registry ID T-LEMA-ii.] PRECISION OF RECORD
(rigor session 2026-07-16, Prop. A2): the explicit component
realization of f2 CANNOT be a pointwise kernel/boundary contraction
(the kernel ratio was computed and does NOT reproduce f2 — Prop. A2);
the narrowed PENDING P-A1' is therefore precisely stated: derive the
ADJOINT COMPATIBILITY (transport) RELATION along the tangent
characteristic for the thrust+mass adjoint and exhibit f2 as its
first integral (equivalently: which psi-combination is transported
invariantly along C+/-). Falsifier O3.3 unchanged: construct the
B2/B3 analytic adjoint on the terminal characteristic of one TOC case
and subtract; any residual beyond discretization kills the claim as
stated.

STATUS UPGRADE (rigor session 2026-07-16, second pass — P-A1'
DISCHARGED; the paragraph above records the narrowing, kept for the
audit trail). PROP. A3 (f2 = the transported adjoint invariant —
THEOREM within the irrotational homentropic scope, EOS-GENERAL;
machine-verified: validation/pa1_symbolic_lemmaA.py Part 3, PASS with
corrupted-pair rejector): (a) the multiplier(adjoint)-field PDEs of
the classical two-field formulation (continuity-multiplier lambda2-
field, irrotationality-multiplier lambda1-field; DERIVED IN-HOUSE by
parts, only d rho/dV = -rho V/c^2 used) are solved, for EVERY
admissible flow, by the closed-form family
    (lambda1, lambda2) = a (y^d rho v, u) + b (0, 1).
Published anchor (found by the in-house literature pass, page-
verified): Humphreys-Thompson-Hoffman AIAA J 9(8):1581 (1971)
p. 1583 ("lambda1 = y rho V sin theta, lambda2 = V cos theta ...
satisfy the partial differential equations ... for any velocity
distribution"); compatibility form d lambda1 -/+ y rho cot(alpha)
d lambda2 = 0 along Mach lines: Hoffman-Scofield-Thompson JOTA
10(3):133 (1972) Eqs. (21)-(23). (b) Imposing the terminal-
characteristic transversality E = lambda1 -/+ lambda2 y^d rho
cot(alpha) = 0 (JOTA Eq. (26)/(34) C+; HTH Eq. (20) C-) on this
family yields EXACTLY V cos(theta -/+ alpha)/cos(alpha) = -b/a =
const: Rao's f2, with the constant component b of lambda2 (a =
thrust normalization) as the transported datum. QED. Identification
(ii) is therefore THEOREM in the declared scope; O3.3 becomes a
numeric cross-check of the A1 engine, no longer load-bearing.
ROTATIONAL SCOPE NOTE (user question of record): the two-field
closed form is irrotational-homentropic; for ROTATIONAL (and
reacting) inflow the transport lives in Hoffman 1967's four-field
system (Eqs. (49)-(51)/(54), mapped in (iv)) and the Kraiko-school
extensions (arbitrary vortical inflow, D2 §b0) — the identification
survives at the FIELD level, the two-constant reduction does not;
this is the boundary the averaged program's per-phase brick respects
(M0 VI.2 mandates rotational MOC; Guderley 1959 extended the
classical side to nonuniform entropy, per the Hoffman-1967
introduction read).

(iii) CORNER CONDITION == ADJOINT TRANSVERSALITY. (L.14) is the
vanishing of the augmented density at the free endpoint — in optimal-
control language, the transversality condition at a free terminal
point; in adjoint language, the compatibility of the wall adjoint
condition (L.21) with the Sigma datum (L.22) where wall and terminal
characteristic MEET (the lip E). The derived forms (L.15)/(L.16) are
exactly CSTR_PA/CSTR_PB of M0 VI.3 with the sign fixed by the family
of the tangent characteristic. Class THEOREM* [C-O33] (same status as (i):
structure complete, explicit adjoint-component check PENDING O3.3).

(iv) HOFFMAN'S MULTIPLIER FIELDS == INTERIOR CONTINUOUS ADJOINT;
E == ADJOINT RESIDUAL. [UPGRADED 2026-07-16, rigor session: FULL
page-level read of Hoffman 1967 (AIAA J 5(4):670-676) executed on the
in-house PDF; every equation number below is post-read verified.
SYMBOL CORRECTION of record: earlier program docs paraphrased the
fields as "lambda1..lambda4 (+lambda5)"; Hoffman's actual notation is
h_1..h_4 (field multipliers, one per flow PDE), g_i (i = 1..n, one
field per species equation), C_1 (constant isoperimetric multiplier),
C_2(x) (streamline-constraint multiplier along the wall AC).]

THE COMPONENT MAP (page-verified):
| Hoffman object (his Eq., page) | Adjoint reading |
|---|---|
| h_1 = multiplier of continuity L_1; h_2, h_3 = x-/y-momentum; h_4 = pressure/energy operator (his Eq. 4); augmented functional Eq. (17), p. 672 | the PRIMITIVE-FORM adjoint 4-vector (conjugate to (mass, mom-x, mom-y, energy); conservative psi via the (dU/dV)^T transform of Prop. A2's bookkeeping) |
| g_i, multiplier of species M_i (Eq. 15); g_i = 0 along BC (Eq. 34, p. 673) | adjoint species components with ZERO terminal data |
| C_1 (constant, Eqs. 12/17) | isoperimetric multiplier (general G: length Eq. 67, surface area Eq. 70, arc length Eq. 73, weight Eq. 76) |
| h_1 = C_2 on the wall AC (Eq. 29); h_1(X_C) = C_2(X_C) via Eq. (63); h_1[x, eta(x)] along AC Eq. (65) (constant-length case Eq. 68) | wall adjoint boundary condition + endpoint transversality (the reacting-gas corner analogue) |
| interior multiplier PDEs Eqs. (35)-(39), nonhomogeneous terms K_3, K_4, J_i Eqs. (42)-(44)/(55)-(57), p. 673-674 | the adjoint PDE system L* h = K (nonhomogeneous through reaction sources) |
| combined (8+2n) system hyperbolic; characteristics = gas streamlines AND gas Mach lines (p. 674); multiplier compatibility along streamlines Eqs. (49)-(51), along Mach lines Eq. (54) | adjoint characteristics = flow characteristics (Prop. A1, INSTANCED in print in 1967); Eq. (54) IS the adjoint transport relation along C+/- |
| BC data on the terminal characteristic: Eqs. (31), (33), (34); the FIFTH relation Eq. (32) deliberately NOT imposed (p. 673) | adjoint terminal data; the redundant relation = transversality surplus |
| E := y h_1 - (u y' - v) h_3 (Eq. 78 == the unused Eq. 32), evaluated along BC; "if E is everywhere zero along BC ... the contour is indeed the optimum" (p. 676) | a-posteriori ADJOINT RESIDUAL certificate — the 1967 ancestor of the Level-C stationarity certificate (M0 VI.6, O3.2) |
| p. 673: with BC non-characteristic, FIVE independent boundary relations arise -> "the problem would be overspecified"; forcing BC = left-running Mach line leaves four -> "the choice of the control surface BC is not arbitrary" | the CLASSICAL ANCESTOR of Prop. A2's refined route for identification (i): the characteristic surface is selected by the count of imposable adjoint boundary conditions — published in 1967, in multiplier language |

Class THEOREM* [C-D25U] (component map explicit and page-verified at the
operator level; the identification is now two-sided in print). What
remains PENDING: (P-A3/O3.2) numeric — evaluate E on the AD-computed
adjoint field of the A1 engine, convergence at the unit-process order;
falsifier unchanged (nonvanishing E on a converged optimum kills).
NEW ROUTE OF RECORD FOR P-A1' (from this read): specialize Hoffman
Eq. (54) (multiplier compatibility along Mach lines) to frozen
homentropic flow (g_i = 0, sources K, J -> inert limit) and integrate
along the terminal characteristic with data (31)/(33)/(63): the first
integral must be Rao's f2 = -lambda2 (Eq. [12]). Discharging this
derivation completes the transport half of (ii) with a PUBLISHED
transport equation as the starting point — strongest possible form of
the bridge (Rao 1958 <- Hoffman 1967 -> modern adjoint, all
equation-numbered).

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
| (L.11) surface = characteristic (classical derivation) | THEOREM | DERIVED §3.2, corpus-checked + MACHINE-VERIFIED (sympy, 8 identities + rejector: validation/pa1_symbolic_lemmaA.py Part 1, EOS-general closure rules) | algebra self-contained + executable carrier |
| Prop. A2 kernel solvability (adjoint b.c. solvable for ANY lambda2 on characteristic Sigma; family-specific) | THEOREM (EOS-general, c symbolic) | MACHINE-VERIFIED (Part 2 + rejector R2) | any state where the r- contractions fail to vanish at u_n = c |
| (L.12)/(L.13) first integrals | THEOREM | DERIVED §3.2, corpus-checked | idem |
| (L.15)/(L.16) corner = endpoint transversality | THEOREM | DERIVED §3.2 step 7, == CSTR_PA/PB | idem |
| Prop. A1 adjoint chars = flow chars | THEOREM | DERIVED §3.3 | det identity |
| (i) Rao surface = adjoint closure surface | THEOREM* (scope §3.0; inherits [C-O33]) | structure DERIVED §3.4 | O3.3 term-match on one TOC case |
| (ii) f2 = adjoint invariant; lambda2/lambda3 = boundary data | THEOREM* → THEOREM (P-A1' discharged 2026-07-16; registry [T-LEMA-ii]) | constants<->data DERIVED; component combo PENDING | O3.3 |
| (iii) corner = adjoint transversality | THEOREM* (inherits [C-O33]) | structure DERIVED | O3.3 |
| (iv) Hoffman fields = interior adjoint; E = adjoint residual | SCHEMA → THEOREM* (P-A2 discharged 2026-07-16, §3.4(iv); inherits [C-D25U]) | anchors verified (Eq. 78, p. 672, p. 676) | O3.2 (E -> 0 at O(h^2) on converged optimum) |
| (L.6)-(L.16) are EOS-general (gamma(T) frozen, homentropic) | THEOREM (audit §3.0) | DERIVED (only Gibbs + c^2 def used) | any homentropic gamma(T) counterexample; E4 oracle for the corner<->eps implementation twin |

PENDING register (all named, per acceptance rule):
 P-A1' [DISCHARGED 2026-07-16, rigor session second pass] Prop. A3:
      transport route closed — in-house derivation of the two-field
      multiplier PDEs + HTH closed-form pair + terminal transversality
      => f2 = const, machine-verified (Part 3, PASS, rejector).
      Scope: irrotational homentropic, EOS-general. Rotational
      extension = Hoffman four-field system (route named in (iv)).
 P-A2 [DISCHARGED 2026-07-16, rigor session] Full page-level read of
      Hoffman 1967 executed in-house; component map written in
      §3.4(iv) (upgraded to THEOREM*); symbol correction of record
      (h_1..h_4, g_i, C_1, C_2). Residual numeric half lives in P-A3.
 P-A3 O3.2 E-residual evaluation on the AD adjoint field — A1 engine.
None of P-A1..P-A3 blocks Lemma A as classed above; they discharge the
THEOREM*->THEOREM upgrades and the (iv) SCHEMA->THEOREM* upgrade.

------------------------------------------------------------------------------
## §3.7 NUMERIC STATUS OF RECORD (2026-08-06, session S19 — the
##      pre-registered O3.2/O3.3 campaign; carriers [X-O32], [X-O33B])

Class of everything below: PRACTICE (measurement); it moves no claim's
rigor class by itself, it discharges or fails the numeric conditionals.

(a) LOCUS CORRECTION OF RECORD. Rao's control surface is the C+
through the lip traced BACK and STOPPED at the kernel boundary (the
last C- emitted by the fixed throat arc), not the whole C+ down to the
axis. On the full chain f2 drifts 2.9e-01 and (ii) looks falsified; on
the classical surface f2 is constant to 9.5e-03. The campaign's first
implementation had the locus wrong — recorded because the wrong number
is the one a reader would otherwise reproduce. See P2_outline §5
addendum (i).

(b) IDENTIFICATION (ii), f2 = -lambda2, MEASURED ON TWO INDEPENDENT
DESIGNS. On the S18 converged design f2 = 2665.38 with drift 9.5e-03
along the control surface; on GENO's own type-2 (Rao) contour, marched
by the same engine, f2 = 2666.03 with drift 8.0e-03. The two Rao
constants agree to 2.4e-04 relative — an order of magnitude tighter
than either drift, i.e. the residual is the instance's discretization,
identical for both designs, and NOT a property of either. The
wrong-family combination u - v tan(alpha) drifts 8.6x more on the same
surface (pre-registration item (c), fired as intended).

(c) THE ADJOINT COMPATIBILITY RELATION on our field, in the Prop. A3
two-field gauge (lambda1 = y rho v, lambda2 = u): the corpus relation
d(lambda1) -/+ y rho cot(alpha) d(lambda2) = 0 cancels to a mean
fraction 1.6e-04 on the C+ family and 2.3e-04 on the C- family with
the sign that belongs to each family, and saturates at EXACTLY 1.0
with the other sign. This is the compatibility-residual coordinate the
O3.3 protocol registers, and its wrong-sign control is the sharpest
rejector in the bench.

(d) IDENTIFICATION (iii), the corner row. With the exit ordinate
constrained, (L.14) reads dJ/dy_lip = 2 pi y_E [p_E - (1/2) rho_E W_E^2
sin(2 theta_E) tan(alpha_E)] (pa = 0). Measured: the AD side
1.054906e+07 against the classical side 9.893197e+06 = 6.6e-02
relative on the 8-node design, MESH-INDEPENDENT (6.6295e-02 at r=1 vs
6.6368e-02 at r=2), and 2.0e-02 on a faithful Rao wall at the same
mesh, falling further under refinement there. Reading of record: the
identity is SUPPORTED and converging in both limits that separate our
instance from the continuum optimum, and is NOT confirmed at a
Richardson band on any single finite-dimensional instance — which is
what an identity of the continuum optimum should do. [C-O33] therefore
stays OPEN with its residual now QUANTIFIED and its dominant term
IDENTIFIED as the design class, not the discretization.

(e) THE PRIMARY KILL CRITERION PASSED. On a feasible one-parameter
family around the optimum the AD directional derivative and the
classical Rao residual vanish at the SAME design within the derived
bar — the gradient-level term match that P2_outline §5(b) designates
as primary.

(f) O3.2 / P-A3 STATUS, honestly bounded. The mesh-convergence half
ran ([X-O32]): the objective's exponent is 2.53 on the fine triple,
the apparatus is validated by a first-order control that reads 0.9997
+/- 6e-04, and the ADJOINT exponent is NOT MEASURABLE on a refinement
ladder because refinement cannot hold the march topology fixed — this
is clause LB-c2 of [S-LBML] biting, not a failure of the transpose.
S21 RE-ADJUDICATION OF RECORD (2026-08-11, red-team on the audit
refutations): the objective row's CONCLUSIVENESS is re-reported
NON-CONCLUSIVE under the PRE-REGISTERED cap (dp_tot = 0.6704 > 0.5
of the carrier commit 6ea29e3; the in-verdict-commit doubling to
1.0 cannot bind post hoc). The rate claim stays NOT KILLED (binding
one-sided S16 falsifier, p_fine = 2.5347); no downstream claim may
cite the objective exponent as CONCLUSIVELY second-order; named
lever = a finer ladder driving dp_tot < 0.5.
The Hoffman-E evaluation proper (E on the pointwise AD adjoint FIELD)
is NOT executed: it needs the adjoint field extracted by residual
injection (a source tau added through the custom_vjp solver's p
argument, so that dJ/dtau is the discrete multiplier of that cell's
compatibility row). P-A3 stays open with that procedure named.
