# T7 and P7 in function space — the first-order system and existence
# for the problem of record (P), attacked

Status: RIGOR ATTACK OF RECORD (2026-07-16, Sessione 8-rigore,
[F1/T7-FS + F1/P7]). ANCHOR (standing user directive: always remember
the objective): the objective is (P) of M0 D2.6 — compute the pair
(S*, delta). Its clause (i) NEEDS existence of the argmax; its clause
(ii) NEEDS the averaged system T7 to be a rigorous first-order
necessary condition. THIS document supplies exactly those two
upgrades in the working class, from the bricks proven earlier today
(G12-S1 per-phase shape derivative; the P3 measurability composition;
the audited uniform margins). Nothing here exceeds (P); everything
here serves it.

Verification-sufficiency discipline (standing): BOTH results are
FUNCTION-SPACE statements — no symbolic carrier can close them; their
finite-dimensional bricks are already machine-verified elsewhere
(pa1_symbolic_lemmaA.py, g12_shock_linearization.py, n6_swirl_kernel
.py); the analytic steps below are named and classed. Gamma status:
EOS-general throughout (only margins and energy bounds are used).

------------------------------------------------------------------------------
## §1 THEOREM T7-FS (differentiation under the cycle integral —
##     T7 upgraded from SCHEMA to THEOREM* in the S1 class)

Setting: a fixed topology sector; working spline class A_h(c) with
uniform C^{1,1} bound; per mu-a.e. xi the unique S1 solution with the
AUDITED uniform margins of D2.6 (axial spacelikeness, boundary-
function margin, front count/strength margins on shocked phases,
uniform supersonicity M_E >= M_min > 1 at lips); switch phases
mu-null (T7's standing hypothesis, unchanged).

CLAIM. For every admissible variation dSigma:
 (a) xi -> F'[Sigma; s(xi)](dSigma) exists mu-a.e. (per-phase shape
     derivative: classical Hadamard density at smooth phases;
     THEOREM G12-S1 at shocked phases), is mu-MEASURABLE, and is
     UNIFORMLY BOUNDED: |F'[Sigma; s(xi)](dSigma)| <= C ||dSigma||
     with C from the margins only.
 (b) The difference quotients are uniformly dominated in xi.
 (c) Hence J[Sigma] = Int F dmu is shape-differentiable with
         dJ[Sigma](dSigma) = Int_Xi F'[Sigma; s(xi)](dSigma) dmu(xi):
     the mu-averaged wall condition T7(b) and the WEIGHTED
     transversality (**') are genuine L^1(dmu) statements — T7 is the
     RIGOROUS first-order necessary condition of (P)(ii) in this
     class.
 (d) The weight w(xi) of the (**') factorization is measurable and
     L^infinity(dmu).

PROOF (steps, each classed).
 (i)  Per-phase existence of F': smooth phases = classical shape
      calculus (Hadamard) at C^1 solutions — THEOREM of record;
      shocked phases = THEOREM G12-S1 (front-shift derivative;
      residues R-G12.1..3 inherited and named). [Bricks proven.]
 (ii) MEASURABILITY: the derivative map (data) -> (Hadamard density)
      is continuous on the margin-certified data set (same solution-
      map continuity used in P3 step (iii), extended to first
      derivatives by the same D2.5 semiglobal estimates — conditional
      R-T7.1); xi -> s(xi) measurable (contract R3); composition
      measurable. [P3 argument, one degree higher.]
 (iii) UNIFORM BOUND: the Hadamard density is a pointwise algebraic
      expression in (p, rho, V, theta, alpha, geometry) plus front
      terms controlled by the G12-L2 nonsingular linearized RH; all
      factors are bounded by the energy bound (V <= sqrt(2 h0_max)),
      the uniform supersonicity (cos alpha >= sqrt(1 - 1/M_min^2)),
      the C^{1,1} geometry bound, and the front-strength margins
      (which bound the inverse of the equilibrated linearized RH —
      the certified s_min of the carrier). No step needs more than
      the audited margins. [Algebraic + certified bricks.]
 (iv) DOMINATION OF QUOTIENTS: |F[Sigma + t dSigma; s(xi)] -
      F[Sigma; s(xi)]| <= C t ||dSigma|| uniformly in xi, for t small:
      this is the uniform-in-xi Lipschitz stability of the per-phase
      solution map in the C^1 wall topology — the D2.5-inherited
      estimate (named conditional R-T7.1; across fronts it inherits
      R-G12.1). [Function space — the one genuinely analytic input.]
 (v)  Dominated convergence on the difference quotients gives (c)
      (Gateaux; Frechet under a uniform differentiability modulus —
      named R-T7.2). QED.
 (d): w(xi) is an explicit algebraic factor in the same bounded
      quantities (M0 T7(c)); measurable by (ii), bounded by (iii).

CLASS: THEOREM* — conditionals: R-T7.1 [C-D25U] (uniform Lipschitz/derivative
stability of the S1 solution map: the SAME D2.5 semiglobal-estimate
conditional the whole program declares — nothing new is assumed),
R-T7.2 (Frechet vs Gateaux modulus), R-G12.1..3 inherited at shocked
phases. Falsifier: a certified cycle family (margins uniform) where
the exchanged derivative dJ /= Int F' dmu beyond bars (executable
once A1 computes both sides independently — an O3-class oracle).

CONSEQUENCE FOR (P): clause (ii) of D2.6 is now a THEOREM*-grade
necessary condition, not a formal schema: any S* the pipeline
delivers MUST satisfy the averaged system, and a Verdict's KKT/(**')
residuals are checks of a rigorous condition.

------------------------------------------------------------------------------
## §2 THEOREM P7-S1 (existence of the argmax — (P)(i) attacked)

CLAIM. On the margin-certified admissible class
    A_h^delta(c) = { Sigma in A_h(c) : all S1 audit margins >= delta }
(delta > 0 the certification level of record), the argmax of J
EXISTS: (P)(i) has a solution S* in A_h^delta(c).

PROOF (steps, classed).
 (i)  COMPACTNESS: A_h(c) is a bounded finite-dimensional spline
      family (bounded DOFs from c + the uniform C^{1,1} bound) —
      closed and bounded in finite dimension, hence COMPACT. (The
      infinite-dimensional closure argument — Ascoli/Chenais uniform
      cone — is the classical route and holds too, but is not needed
      for the WORKING class: finite dimension suffices. Symbolic-
      sufficiency note: this step is elementary, no carrier needed.)
 (ii) CLOSEDNESS of the margin constraint: each audit margin
      (boundary function, spacelikeness, front strength) is a
      CONTINUOUS functional of Sigma on the certified set (same
      solution-map continuity, conditional R-P7.1 = R-T7.1);
      "margin >= delta" defines a CLOSED subset. Hence A_h^delta(c)
      is compact.
 (iii) CONTINUITY of J: per-phase F[.; s(xi)] is continuous in Sigma
      at margin-certified points (R-P7.1), uniformly bounded in xi
      (§1(iii) bounds), so J is continuous by dominated convergence.
 (iv) Weierstrass: continuous function on a compact set attains its
      maximum. QED.

THE FAILURE BOUNDARY, made precise: existence is proven ON EACH
certified level set A_h^delta. If the maximizing value increases as
delta -> 0 (the optimizer pushes against the S1 boundary: incipient
wall shock, front tangency, loss of marching supersonicity), the sup
over the UNCERTIFIED class may be unattained or leave S1 — this is
EXACTLY what the monitored failure boundary of record detects
(boundary function -> 0). The pipeline's obligation, now
theorem-shaped: report the margins AT S*; an S* on the boundary of
its level set is flagged, and the statement "argmax exists" is
always relative to the certified class — which is the only class the
certificates cover anyway. (P)(i)'s "monitored failure boundary"
language is hereby the boundary of the compact sets of this theorem.

CLASS: THEOREM* — conditional R-P7.1 [C-D25U] (continuity of the solution map
and of the margins: D2.5-inherited, same as R-T7.1); residue R-P7.2
(the certified argmax may differ from the uncertified sup — declared
and REPORTED, never hidden). Falsifier: a certified maximizing
sequence in a fixed level set with no convergent-subsequence limit
attaining the sup (would contradict compactness/continuity — checks
R-P7.1).

------------------------------------------------------------------------------
## §3 What remains open after this document (honest tail)

 - R-T7.1/R-P7.1: the uniform semiglobal stability estimates — the
   ONE analytic conditional everything shares with D2.5; writing it
   from the Li-Yu framework (smooth regions) + G12-S1 front analysis
   is the single most valuable remaining function-space task
   (it would simultaneously firm T7-FS, P7-S1, P3, S1-U step A1).
 - Five-field swirl optimality system (N6 §4) — SCHEMA, own session.
 - P4 Fredholm + quantitative remainder (D3 §3 addendum) — own
   session.
 - Lemma B mesh-limit consistency proof — target stated (G12-S1).
 - Second-order theory — unattacked (checked numerically per
   Verdict).

With T7-FS and P7-S1 in place, the theoretical chain of (P) reads:
existence (P7-S1, THEOREM*) -> necessary conditions (T7-FS, THEOREM*)
-> multipliers (P3, THEOREM*) -> per-phase closed forms (Lemma A,
THEOREM in scope) -> globality mechanisms (M1/M2/M3, THEOREM/THEOREM*)
-> delta-certificate (bound ladder, THEOREM + executable). No
load-bearing SCHEMA remains between the definition of (P) and its
certified solution in the S1 shock-free class; across fronts every
statement inherits ONE declared conditional (D2.5), named everywhere
it appears.
