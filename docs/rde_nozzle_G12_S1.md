# G12 in the S1 class — shape calculus with fitted shocks via the
# x-as-time reading (attack of record)

Status: RIGOR ATTACK OF RECORD (2026-07-16, Sessione 8 dedicata,
[F1/G12-S1]). Target: the named gap G12 (multi-D shape derivative
across shocks: rigorous theory 1-D only — Bressan-Marson, Ulbrich;
quasi-1D design rigor Cliff et al.; 2-D practice). Result here: the
gap is REDUCED, inside the program's own working class, to the
verified 1-D-in-time theory by the observation that S1 MARCHING FLOW
IS A 1-D EVOLUTION, plus one machine-verified linear-algebra brick at
the front. Classes stated per item; citation honesty: Bressan-Marson
Comm. PDE 20:1491 (1995), Ulbrich, Majda stability, Li Ta-tsien(-Yu)
semiglobal framework are OF RECORD (D2 §b3 verified list / M0 D2.5);
the shift-differentiability-for-systems lead (Bressan-Guerra class)
is cited as TO-VERIFY only.

Gamma status (standing directive): all structural statements are in
primitive variables with c^2 free — EOS-GENERAL; the executable
carrier instantiates a perfect-gas oblique shock as declared
known-answer ORACLE only.

------------------------------------------------------------------------------
## §1 The observation (Lemma G12-L1): S1 marching flow IS 1-D evolution

Setting: smooth region of an S1 solution between wall y = w(x) and
inner boundary, with the AXIAL SPACELIKENESS margin of record
(N-SW/D2.6): u_x > c uniformly (min(M_x − 1) >= delta_S1, an AUDITED
per-phase quantity of the data contract).

LEMMA G12-L1 (evolution reading — THEOREM; eigenstructure
machine-verified, carrier §5). Under u > c (x-component), steady 2-D
Euler in primitive variables V = (rho, u, v, p),
    A_p(V) V_x + B_p(V) V_y = S (axisymmetric source),
has A_p INVERTIBLE (det A_p proportional to u^2(u^2 − c^2), verified
symbolically with c^2 free) and the pencil (A_p, B_p) has REAL
eigenvalues with COMPLETE eigenvectors:
    dy/dx = v/u (double; streamline family: entropy + tangential
    transport) and dy/dx = tan(theta ± alpha) (simple; Mach lines),
verified symbolically via the factorization
    det(B_p − lambda A_p) ∝ (v − lambda u)^2 [ (v − lambda u)^2
                                              − c^2 (1 + lambda^2) ].
Hence the system is quasilinear hyperbolic WITH x AS TIME, of
constant multiplicity — exactly the class of the Li Ta-tsien(-Yu)
semiglobal C^1 theory that D2.5 already invokes for S1
well-posedness. CONSEQUENCE: on smooth regions, continuous and C^1
dependence of the solution on boundary data and on the (wall-fitted,
C^2) boundary is the 1-D-IN-TIME theory of record, with x-intervals
finite (the nozzle length) — no new analysis is needed beyond the
declared D2.5 framework. QED (the eigenstructure computations are the
carrier's Part 1; the well-posedness import is D2.5 of record).

Wall-fitted transform: y = eta * w(x) (eta in [0,1]) maps the
variable domain to a fixed strip; w enters the coefficients through
w, w' (C^1 in the coefficients for w in C^2): shape dependence
becomes COEFFICIENT dependence — the standard reduction, stated for
completeness.

------------------------------------------------------------------------------
## §2 The front brick (Lemma G12-L2): linearized RH is nonsingular
##     strictly inside the Lax condition — and singular exactly at
##     characteristic fronts

A fitted transversal front y = sigma(x) with unit normal n(sigma')
carries the RH residual system (EOS-general form)
    H(V_plus; V_minus, sigma') :=
      [ rho u_n ]        = 0
      [ p + rho u_n^2 ]  = 0
      [ u_t ]            = 0
      [ h + (u_n^2 + u_t^2)/2 ] = 0
(u_n = (sigma' u − v)/sqrt(1+sigma'^2), u_t = (u + sigma' v)/
sqrt(1+sigma'^2)).

LEMMA G12-L2 (THEOREM; machine-verified numerically at a known-answer
oracle with derived tolerances + TWO structural rejectors).
 (a) dH/dV_plus = K_p(n)|_{V_plus} — the normal flux Jacobian — with
     det ∝ u_n^2 (u_n^2 − c^2). STRICTLY INSIDE the Lax condition
     (0 < u_n_plus < c_plus < ... < u_n_minus) this is NONSINGULAR on
     the downstream side: the linearized RH system determines
     delta V_plus uniquely from (delta V_minus, delta sigma').
 (b) dH/dsigma' /= 0 at NONZERO shock strength: the front-shift
     sensitivity is genuinely present; the linear ODE for the front
     perturbation delta sigma(x) (obtained by projecting the
     linearized RH transport along the front) is well-defined.
 (c) DEGENERATION IS EXACTLY CHARACTERISTIC: as the front tends to a
     Mach line (zero strength, u_n -> c), det dH/dV_plus -> 0 AND
     dH/dsigma' -> 0 — the same kernel degeneracy as Prop. A2 (docs/
     rde_nozzle_P2_lemmaA.md): the shape calculus loses the front
     unknown exactly where the front ceases to be a shock. This is
     the honest boundary of the front brick, and it is DETECTED by
     the same audit (shock-strength margin) the S1 monitor already
     carries.
Carrier: validation/g12_shock_linearization.py (symbolic det
identities with c^2 free; numeric oracle M1 = 2.5, beta = 40 deg,
gamma = 1.4 with SVD-based derived tolerances; rejectors: (R1)
characteristic-front singularity must be DETECTED, (R2) a corrupted
RH row must break the known-answer oracle).

------------------------------------------------------------------------------
## §3 Assembly (Lemma G12-L3) and the theorem

LEMMA G12-L3 (composite shift-derivative — SCHEMA with the assembly
derived, gaps named). At a CERTIFIED S1 reference solution (finitely
many noninteracting Lax-transversal fitted fronts, graphs over x,
margins uniform — all a-posteriori certified quantities per D2.5),
the derivative of the solution map (w, U_0) -> (U, sigma) is the
PIECEWISE object: classical linearization on each smooth region
(G12-L1) coupled at fronts by the linearized RH brick (G12-L2), the
front shifts delta sigma_k solving linear ODEs in x. These are
EXACTLY the objects the fitted-AD march computes (Lemma B (B.1)-(B.3)
of record: front = explicit unknown, implicit rule on RH): the
discrete gradient is the discretization of THIS derivative.
The thrust functional J (wall integral of (p − pa) n_x + shear-free
slip) is then differentiable with Hadamard density = the classical
smooth-region formula plus bounded front-shift terms; the shifts
enter J through CONTINUOUS quantities (pressure is continuous along
the wall; fronts meet the wall transversally in S1), so J is
FRECHET-differentiable in w even though the state derivative is only
a shift-derivative.

THEOREM G12-S1 (shape differentiability in the marching class —
THEOREM* [C-D25U, C-MAJDA]; conditionals NAMED below). Under (H1) uniform axial
spacelikeness margin, (H2) certified S1 reference (finitely many
noninteracting Lax fronts with uniform strength margin, transversal
wall/front intersections), (H3) wall perturbations in C^2 with the
wall-fitted transform: the map w -> J[w] is Frechet-differentiable,
its derivative is the Hadamard density of record (smooth formula +
front terms), and the fitted-AD march computes a convergent
discretization of it. In particular the shape gradient used by the
pipeline has a CONTINUUM THEOREM behind it in the S1 class — the G12
gap, within this class, reduces to the two named conditionals:

 R-G12.1 (region regularity ACROSS the interval): semiglobal C^1
     existence on each smooth region between fronts is the D2.5
     framework (of record); its uniformity in the perturbation
     parameter is inherited from the same estimates — CONDITIONAL
     exactly as D2.5 canonicity (nothing new is assumed).
 R-G12.2 (shift-differentiability citation): the abstract statement
     "piecewise-C^1-with-Lax-fronts solutions are shift-
     differentiable in their data" is stated here with the explicit
     construction (G12-L1 + G12-L2 + ODE assembly); the CLASS-level
     precedent for 1-D systems (Bressan-Guerra-type) is a TO-VERIFY
     lead — our claim does NOT rest on it (the construction is
     self-contained at the formal level), but the citation must be
     verified before P-1/P-2 cite the theorem.
 R-G12.3 (mesh limit): the statement that the DISCRETE fitted-AD
     gradient converges to this continuum derivative at the
     unit-process order is the Lemma-B mesh-limit clause — upgraded
     from "SCHEMA, frontier G12" to "SCHEMA, target identified:
     consistency of the discretized G12-L1/L2 objects", with the O3
     oracles as its falsifiers. The circularity is BROKEN: Lemma B's
     honesty clause no longer points at an open frontier but at a
     stated continuum theorem.
     [WRITTEN, dated 2026-08-06 (S16 T4b, [S-LBML] docs/
     rde_nozzle_LBML.md): the five-step Lax-equivalence argument is
     executed at written level — stability = the D2.5-U five-constant
     machinery (U1-U4 written), front step = the S16 bordered-solve
     bricks (U3-L1/U3-H1); clauses LB-c1 (regularity for the h^2
     rate, self-monitoring via O3.2) and LB-c2 (fixed topology)
     declared.]

Falsifiers: (F1) carrier rejectors (§2); (F2) O3.3-class numeric — FD
shape gradient vs AD gradient at a fitted-shock case (A1 engine): a
divergence beyond derived bars at certified margins kills G12-S1 as
stated; (F3) any S1-certified case where J fails one-sided
directional differentiability (would contradict the assembly).

------------------------------------------------------------------------------
## §4 What this buys the program (one paragraph)

The pipeline's shape gradient at shocked phases — previously honest
only as "exact discrete + open continuum" — now has a stated
continuum theorem in the exact class the pipeline certifies at
runtime (margins already audited: spacelikeness, boundary function,
front count, and now shock-strength). Lemma B §4's honesty clause
tightens; P-1's §5/§9 can cite G12-S1 instead of only naming the
frontier; the residues R-G12.1..3 are inherited conditionals or
verification tasks, not new mathematics.

------------------------------------------------------------------------------
## §5 Claim register

| Claim | Class | Carrier / falsifier |
|---|---|---|
| G12-L1 eigenstructure (det A_p ∝ u^2(u^2−c^2); pencil factorization; completeness) | THEOREM (EOS-general) | carrier Part 1 (symbolic, c^2 free) |
| G12-L1 evolution reading => D2.5 theory applies with x as time | THEOREM* (imports D2.5 of record [C-D25U]) | — (framework identification) |
| G12-L2(a) linearized RH nonsingular strictly inside Lax | THEOREM | carrier Part 2 numeric + det identity; rejector R1 |
| G12-L2(c) degeneration exactly characteristic (= Prop. A2 kernel) | THEOREM | carrier Part 2 limit check |
| G12-L3 assembly = fitted-AD objects | SCHEMA (derived; regularity conditional) | O3 oracles (A1) |
| THEOREM G12-S1 | THEOREM* (R-G12.1..3 named; inherits [C-D25U, C-MAJDA]) | F1-F3 above |
