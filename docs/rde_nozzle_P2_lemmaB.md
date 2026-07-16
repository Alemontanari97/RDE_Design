# P-2 LEMMA B DRAFT — §4 of the bridge paper: reverse-mode AD of a
# shock-fitted MOC march IS the discrete adjoint characteristic sweep

Status: DRAFT OF RECORD for paper §4 (2026-07-16, [F1/P-2], session S7).
Implements §4 of docs/rde_nozzle_P2_outline.md (outline of record
05001a5). Companion of docs/rde_nozzle_P2_lemmaA.md (paper §3 = the
continuous bridge). Executable demonstrator of record:
validation/g0_spike_jax_moc.py (S5, commit b07b47e — implicit
custom_vjp unit processes, 52/52 Jacobian entries within DERIVED
tolerance, negative control rejected). Every claim below carries a
rigor class and a falsifier; no "it can be seen that".

Rigor legend as in M0: THEOREM / THEOREM* / SCHEMA / CONJECTURE /
PRACTICE; PENDING = requires the A1 differentiable engine (O3 oracles),
named per item.

------------------------------------------------------------------------------
## §4.0 Scope, conventions, and two declared disambiguations

SCOPE. Discrete: a shock-FITTED method-of-characteristics space march
of the Zucrow-Hoffman Ch.17 class (M0 VI.2 semantics: unit processes
O(h^2) in average-coefficient form; interior point, direct/inverse
wall point, axis point, shock point on a fitted front), marching a
supersonic S1-regular region from an initial-value line, with design
vector d (wall spline DOFs, lip coordinates, and — in fitted mode —
nothing else: front positions are UNKNOWNS, §4.3). Objective J =
thrust in wall or control-surface form evaluated from the marched
states (paper §2 equality). Everything in this section is
FINITE-DIMENSIONAL: mesh-limit statements are quarantined in §4.5.

NAMING (declared to avoid two collisions). (1) THIS Lemma B — the
paper's discrete bridge — is unrelated to the internal "Lemma B
(stagnation-temperature similarity)" inside the proof of M0 Theorem 5
(T3), which is a similarity statement about the flow, not about
adjoints; the paper never cites the latter as "Lemma B". (2) The
Zucrow-Hoffman characteristic naming is used throughout as in the
Lemma-A draft §3.0 (C- slope tan(theta - alpha), C+ slope
tan(theta + alpha)).

GAMMA STATUS (standing directive of record, strengthened S5). The
transpose identity of this section is CLOSURE-AGNOSTIC, hence
EOS-general BY CONSTRUCTION: it operates at the level of the residual
maps R_k of the unit processes and never opens them — any EOS backend
(frozen gamma(T), arbitrary convex EOS, M0 VI.2) inherits it verbatim,
because transposition of a block-triangular Jacobian does not care
what the blocks contain. The g0 spike instantiates the unit processes
with the calorically perfect Prandtl-Meyer closure: a DECLARED ORACLE
instance (its own docstring declares exactly this), never a
load-bearing hypothesis of the lemma. Falsifier: exhibit an EOS
backend for which the reverse sweep of §4.2 fails the O3.1 dot-product
identity beyond the derived roundoff bar.

------------------------------------------------------------------------------
## §4.1 The fitted MOC march is a block-triangular nonlinear system
##      (class THEOREM — a definition plus one named hypothesis)

Enumerate the unit processes of one march k = 1..N in the order the
marcher executes them (any topological order of the dependency DAG
works; the marcher's order is one). Unit process k computes a local
unknown block z_k in R^{n_k} (state and position of the new point:
n_k = 4 for an interior point [x, y, theta, M]; n_k = 2 for the
inverse wall point of the spike; n_k = 4 + n_front at a fitted shock
point, §4.3) as the solution of an implicit residual system

  (B.1)   R_k( z_k ; z_{pa(k)}, d ) = 0,      R_k : R^{n_k} -> R^{n_k},

where pa(k) — the PARENTS of k — are the indices of the already-
computed points that send a C+ or C- characteristic (or the wall/axis/
front constraint) into point k. Stack Z = (z_1, ..., z_N),
R = (R_1, ..., R_N):

  (B.2)   R(Z; d) = 0,        with       dR/dZ  BLOCK LOWER-TRIANGULAR

in the execution order (R_k depends only on z_k and z_j with j in
pa(k), j < k), with diagonal blocks

  (B.3)   J_k := dR_k/dz_k    (the local Newton matrix of process k).

HYPOTHESIS (S1-regularity, named): every J_k is nonsingular along the
march. This is not a convenience: J_k degenerates exactly where two
characteristics of the same family coalesce at the new point (limit
line / incipient wall shock) — i.e. the invertibility of the diagonal
blocks IS the discrete S1-membership monitor (M0 VI.2 boundary
function; the Newton-residual rejector of the g0 spike certifies it
per process, NEWTON_TOL_FACTOR * eps, derived).

THEOREM B0 (march = forward substitution). Under the hypothesis, the
MOC march is exactly the block forward-substitution solve of (B.2):
process k solves (B.1) by Newton on J_k given its parents. QED
(definitional once (B.1)-(B.3) are set up; the content is the SHAPE —
triangularity — which encodes the finite domain of dependence of the
discrete characteristics).

------------------------------------------------------------------------------
## §4.2 Reverse-mode AD = the transposed adjoint sweep along the SAME
##      discrete characteristics (class THEOREM — the paper's core)

Let J = J(Z, d) be any differentiable functional of the marched states
(the discrete thrust integral on the terminal characteristic or wall).
Define the discrete adjoint state Psi = (psi_1, ..., psi_N) by

  (B.4)   (dR/dZ)^T Psi = (dJ/dZ)^T,

so that, by the implicit function theorem on (B.2),

  (B.5)   dJ/dd = dJ/dd|_explicit - Psi^T (dR/dd).

THEOREM B1 (transposed sweep). Since dR/dZ is block lower-triangular,
(dR/dZ)^T is block UPPER-triangular, and (B.4) is solved by block
BACK-substitution in REVERSE execution order:

  (B.6)   psi_k = J_k^{-T} [ (dJ/dz_k)^T
                              - SUM_{m : k in pa(m)} (dR_m/dz_k)^T psi_m ].

Read structurally: the sparsity pattern of dR/dZ is the discrete
characteristic connectivity (point k receives from its C+/C- parents);
transposition REVERSES every edge of that DAG, so psi_k gathers
contributions from the processes that point k FEEDS — the adjoint
information propagates BACKWARD along the SAME discrete
characteristics the flow information came forward on. This is the
discrete twin of Prop. A1 of the Lemma-A draft (adjoint
characteristics = flow characteristics), obtained here by pure linear
algebra: det(M^T) = det(M) there, "transpose of triangular is
triangular the other way" here.

THEOREM B2 (reverse AD computes exactly (B.6)). Reverse-mode AD of the
march, with each unit process wrapped in an implicit-function custom
reverse rule (custom_vjp: the local backward pass solves J_k^T w =
zbar_k and returns -( dR_k/d(z_{pa(k)}, d) )^T w — never
differentiating through the Newton iterations), computes exactly the
recursion (B.6) and then (B.5). Proof: reverse accumulation on a
program DAG evaluates the transpose of the composite tangent map in
reverse execution order (Griewank-Walther, standard); the local
custom rule is the IFT-exact local transpose (the g0 spike's bwd,
lines "Jz.T w = zbar; pbar = -Jp^T w"); composing exact local
transposes in reverse order is precisely back-substitution on the
global block-upper-triangular system (B.4). QED.

COROLLARY B3 (the bridge, discrete side). By Lemma A (paper §3), the
continuous adjoint restricted to the terminal characteristic carries
the Rao/Kraiko machinery (f2 invariant, corner conditions). By B1-B2,
reverse AD of the fitted march IS the discrete adjoint characteristic
sweep. Hence "AD of a fitted MOC = the Rao/Kraiko conditions evaluated
discretely" — the identification is exact at finite dimension, with
the dot-product identity

  (B.7)   < (dZ/dd) v, w > = < v, (dZ/dd)^T w >     for all v, w

holding to machine roundoff BY CONSTRUCTION (both sides are the same
sequence of exact local solves read in opposite orders). (B.7) is
oracle O3.1 of the certificate stack; its derived tolerance
(operation-count times eps_mach) and its rejector discipline are
demonstrated in validation/g0_spike_jax_moc.py: 52/52 Jacobian entries
within the two-step-Richardson derived tolerance, Newton residuals
~1e-16, corrupted-vjp negative control REJECTED (35/36 out).
Class of B0-B3: THEOREM (finite-dimensional; the only hypothesis is
the named S1/J_k-invertibility). Falsifier: O3.1 failure at any unit
process of the A1 engine.

------------------------------------------------------------------------------
## §4.3 The fitted front differentiated as an EXPLICIT unknown
##      (class THEOREM finite-dim; the correspondence with the
##       continuous interior shock condition is SCHEMA)

At a fitted shock point the local unknown block is ENLARGED, not
smeared: z_k = (U_down, sigma_k) with U_down the downstream state and
sigma_k the front's local position/slope; the residual block stacks

  (B.8)   R_k = [ C+/C- compatibilities reaching the point from
                  upstream;  Rankine-Hugoniot jump across the front;
                  front geometry (slope consistency with the
                  neighbouring front points) ].

HYPOTHESIS (named, and structural): the front is TRANSVERSAL in the
Lax/Majda sense. Majda's shock-stability determinant is exactly the
statement that the linearized system (RH + incoming characteristics)
is uniquely solvable for (dU_down, dsigma) given upstream
perturbations — i.e. LAX/MAJDA TRANSVERSALITY == NONSINGULARITY OF
J_k = dR_k/dz_k AT THE FITTED FRONT. The IFT hypothesis of §4.1 is
therefore not an extra assumption at shocks: it is the S1 class
earning its keep (M0 D2.5: finitely many transversal fronts).

Consequences (THEOREM, finite-dim): (i) the front's sensitivities
dsigma/dd flow through the SAME implicit rule as any other unknown —
the front is differentiated as an explicit unknown, never as a
captured smear; (ii) in the reverse sweep the front carries its own
adjoint block (the multiplier of the RH constraint), deposited on the
front interface — the discrete twin of the continuous adjoint interior
shock condition (Giles-Pierce 2001, bank B2: adjoint continuous across
the shock with an interior boundary condition along it). The
DISCRETE-to-CONTINUOUS correspondence of (ii) is SCHEMA (it is a
mesh-limit statement; §4.5); the finite-dimensional statements (i)-(ii)
are THEOREM under transversality. Falsifier: O3.1 dot-product at the
shock-point unit process (the A1 engine's shock brick; the axisym +
shock-point spike extension is PROGRESS NEXT/T5); a singular J_k at a
front that Majda's determinant declares transversal would refute the
identification of the two nonsingularity conditions.

------------------------------------------------------------------------------
## §4.4 Where the Giles-Ulbrich trap would bite, and why fitting
##      bypasses it BY CONSTRUCTION (the citable point)

THE TRAP (published): for shock-CAPTURED conservative discretizations,
the discrete adjoint is adjoint-consistent at the shock only if the
scheme enforces, in the limit, an interior smearing condition — the
counterexamples and the repaired conditions are Giles-Ulbrich, SINUM
48:882-904 and 48:905-921 (2010); Lozano's mesh-divergent inviscid
adjoints (AIAA J 2018/2019 line) show the practical bite: refining the
mesh makes the captured adjoint WORSE near the shock. Mechanism: AD of
a captured march differentiates the numerical smear — an internal
layer whose width and internal structure are mesh artifacts — so the
discrete adjoint accumulates O(1) spurious content in the layer
instead of the delta-with-interface-condition structure of the
continuous adjoint.

THE BYPASS (this Lemma): a FITTED march has no smear to differentiate.
The front enters the residual system (B.8) as an explicit unknown
constrained by the EXACT Rankine-Hugoniot relations; its linearization
is the exact shock-shift derivative, and the reverse sweep produces
the interface multiplier structure directly (§4.3(ii)). The trap's
premise — "the shock is represented by the scheme's internal layer" —
is FALSE by construction for a fitted scheme. This bypass is a citable
point precisely because none of the three banks states the trap
structure next to the classical fitted machinery: the classical corpus
(bank B1) fits and never differentiates in the AD sense; the modern
adjoint banks (B2, B3) differentiate and treat capturing as the
default.

HONESTY CLAUSE (declared): "bypassed by construction" is a statement
about the DISCRETE system (THEOREM-grade at finite dimension, §4.3);
the claim that the fitted discrete adjoint CONVERGES to the Lemma-A
continuous field across the front, with order, is the mesh-limit
SCHEMA of §4.5 — the rigor frontier is G12 (multi-D fitted-shock shape
calculus: theorem only in 1-D [Bressan-Marson; Ulbrich], quasi-1D
design rigor [Cliff-Heinkenschloss-Shenoy], 2-D practice [Baeza et
al.]), cited as such in paper §6.

------------------------------------------------------------------------------
## §4.5 The mesh limit (class SCHEMA, falsifiers named)

CLAIM (SCHEMA): on a smooth contour family within the S1 class, as the
characteristic mesh h -> 0 the discrete adjoint field of §4.2
converges, at the unit-process order O(h^2), to the continuous adjoint
of Lemma A restricted to the discrete characteristics, and the AD
boundary gradient converges to the Rao-condition residual (Lemma A
(i)-(iii)). What is proved here: the finite-dimensional identity is
EXACT at every h (no consistency gap can be introduced by the
transpose — B2); what is NOT proved: that the forward unit processes'
O(h^2) consistency transfers to the adjoint with the same order across
a fitted front in 2-D (the G12 frontier). This is exactly the honest
split of the outline §1: THEOREM for the transpose identity, SCHEMA
for the mesh-limit consistency.
Falsifiers (executable, A1 engine): O3.2 — Hoffman E-residual on the
AD adjoint field must vanish at O(h^2) on a converged optimum (wrong
order or nonvanishing kills); O3.3 — AD boundary gradient vs Rao
condition residuals on a perturbed-contour family as h -> 0
(divergence kills); O3.4 — cross-code vs GENO finite differences
(dual-code, user decision S5: GENO stays Fortran).

------------------------------------------------------------------------------
## §4.6 Assembly toward the averaged system (one paragraph, points
##      to P-1; class THEOREM at fixed quadrature)

The cycle layer adds one outer structure: phases xi_1..xi_Q are
mutually independent given the shared contour (block-DIAGONAL in
phase), and the averaged objective is the mu-quadrature of per-phase
thrusts. The transpose of block-diagonal is block-diagonal: the
reverse sweep of the assembled system is the collection of per-phase
adjoint sweeps, each weighted by its quadrature weight — hence the
discrete averaged endpoint gradient assembles as the WEIGHTED
transversality (**') of M0 T7(c) (the classical corner residual R(xi)
times the positive kinematic weight w(xi), summed with mu-weights),
and NEVER as the naive unweighted average (test-rejected at eps level,
in-repo). At fixed quadrature this is THEOREM (same linear algebra as
B1); the quadrature-to-integral limit inherits the switch-splitting
discipline of M0 VI.4. This is the statement P-1 consumes in its §5.

------------------------------------------------------------------------------
## §4.7 Claim register for this draft (delta vs outline §8)

| Claim | Class (this draft) | Status | Falsifier |
|---|---|---|---|
| B0 march = block forward substitution | THEOREM | DERIVED §4.1 (definitional + named J_k hypothesis) | exhibit a marcher step outside (B.1) form |
| B1 adjoint solve = transposed back-substitution along same discrete characteristics | THEOREM | DERIVED §4.2 | linear algebra, checkable line-by-line |
| B2 reverse AD (implicit rules) computes exactly B1 | THEOREM | DERIVED §4.2; demonstrator g0 spike PASS (S5, b07b47e) | O3.1 dot-product failure at any unit process |
| B3 dot-product identity (B.7) at machine roundoff | THEOREM | DERIVED + demonstrated (52/52, derived tol, negative control rejected) | O3.1 |
| Front as explicit unknown; Lax/Majda transversality == J_k nonsingular | THEOREM (finite-dim) | DERIVED §4.3 | singular J_k at a Majda-transversal front |
| Front adjoint block = discrete twin of Giles-Pierce interior condition | SCHEMA (limit) / THEOREM (finite-dim structure) | DERIVED §4.3 | O3.2/O3.3 at the shock brick |
| Giles-Ulbrich trap bypassed by construction (no smear) | THEOREM (discrete premise) + declared honesty clause | DERIVED §4.4 | exhibit smear-dependence in a fitted march gradient |
| Mesh-limit adjoint consistency O(h^2) | SCHEMA | DECLARED §4.5 (G12 frontier) | O3.2 order test; O3.3 term match as h -> 0 |
| Cycle assembly = weighted (**'), never naive | THEOREM (fixed quadrature) | DERIVED §4.6 | eps-level wrong-averaging rejector (in-repo) |
| Transpose identity is EOS-general (closure-agnostic) | THEOREM | DERIVED §4.0/§4.2 (blocks never opened) | O3.1 failure under a gamma(T) backend |

PENDING register (named): P-B1 = O3.1 at the SHOCK-POINT unit process
— DISCHARGED AT BRICK LEVEL 2026-07-16 (session S8, [F2-prep/G0]):
validation/g0_spike_axisym_shock.py Brick B implements the fitted
shock point as an implicit unit process on the RH relations
(z = [beta, M2], custom_vjp + implicit rule, never unrolled) and
verifies (i) the O3.1 dot-product identity <w, dz/dp v> = <vjp(w), v>
against Richardson-derived FD tolerance (err 3.4e-12 vs tol 1.2e-9;
corrupted vjp REJECTED), (ii) the Lax certificate (M1n > 1, M2n < 1,
measured margins), (iii) the Lax/Majda == J_k-nonsingular
correspondence of §4.3 EXECUTABLY: beyond detachment Newton cannot
certify (rejected), and approaching the fold sigma_min(J_k)
degenerates with the fold exponent 1/2 (derived scaling band PASS).
Residual of P-B1 (declared): the same identity inside a full MARCH
with an inherited fitted sheet = A1 engine (Fase 2). P-B2 =
O3.2/O3.3 order tests (A1 engine) — still pending; the dual-route
order-scaling test of the S8 spike (Brick A, axisym source, band
[4,16] per halving) is its first brick-level instance. Neither blocks
the classes as stated (the finite-dim THEOREMs are self-contained;
the SCHEMA rows are declared as SCHEMA).
