# S-LBML written for real — the Lemma-B mesh limit
# (consistency + stability + Lax equivalence for the fitted-AD tangent)

Status: RIGOR ATTACK OF RECORD (2026-08-06, S16 deep-foundations
campaign second tranche, T4b [RIGOR/A]). This document executes the
five named steps of the S-LBML architecture
(docs/rde_nozzle_remaining_conditionals.md §3) at written level: the
claim that the DISCRETE fitted-AD tangent — and hence, by the exact
transpose identity of Lemma B, the discrete adjoint/gradient —
converges to the continuum shift-derivative of THEOREM G12-S1 on
certified references. The S16 front bricks (U3-L1 uniform floors,
U3-H1 bordered nonsingularity) slot EXACTLY into the front-stability
step — writing S-LBML now, after U3/U4, is the cheap order.
Registry: [S-LBML] (existing entry upgraded: statement + doc/proof
pointers). No new carrier (sufficiency discipline: the executable
falsifiers are the EXISTING pre-registered O3 oracles — O3.2 order
check, O3.3 term match, G12-S1 F2 FD-vs-AD; a new carrier would
duplicate them).

Audit line: [Class: SCHEMA (numerical-analysis bookkeeping written;
asymptotic statement, function-space constants from the D2.5-U
machinery) | Falsifier: O3.2 (measured order < 2 - tol on smooth
certified references kills the rate claim), O3.3 (term mismatch),
G12-S1 F2 (FD-vs-AD divergence at fitted shocks) | Carrier: none new
(O3 oracles of record; [T-LEMB] transpose identity machine-verified,
O3.1 dot product 2.7e-10 on the assembled march [X-A1IM]) | Gamma:
EOS-general (the estimates use only the certified-class structure)].

VERDICT UP FRONT: the mesh limit is now WRITTEN as a five-step
Lax-equivalence argument whose stability constants are LITERALLY the
D2.5-U five-constant certificate (U1-U4, now all written) and whose
front step is the discrete shadow of the S16 bordered solve. Honest
prices surfaced by the writing: (LB-c1) the ORDER-h^2 rate needs
interior regularity one degree above certified membership (C^3 along
characteristics on smooth regions) — on C^1-only references
consistency survives but the RATE de-rates (convergence without the
exponent); (LB-c2) the limit is taken AT FIXED MARCH TOPOLOGY — the
same stratum clause c2 of [S-D25U-U34], connecting to RK-G (the
one-sided gradients at re-record boundaries are exactly the
boundaries of this statement's validity).

------------------------------------------------------------------------------
## §1 Objects and claim

March = the fitted MoC x-evolution of record ([X-A1IM] instance;
G12-L1 class): unit process of step h on the characteristic triad,
walls by the slip reflection solve, fronts by the implicit RH rule
(front = explicit unknown; Lemma B (B.1)-(B.3)). Discrete tangent =
the h-parametrized linearization the AD march computes; discrete
gradient = its EXACT finite-dimensional transpose ([T-LEMB], no
approximation at this step — machine fact, O3.1). Continuum target =
the shift-derivative assembled in G12-L3: classical linearization on
smooth regions + linearized RH coupling at fronts + front-shift
linear ODEs.

CLAIM (S-LBML). On a certified reference (five-constant certificate,
fixed front topology), as h -> 0 the discrete tangent converges to
the continuum shift-derivative, with order h^2 under LB-c1; the
discrete gradient converges in the dual pairing at the same order.

------------------------------------------------------------------------------
## §2 The five steps, written

 (i) CONSISTENCY (smooth regions). The unit process is a one-step
     method of order h^2 for the characteristic ODEs (Taylor against
     d/dx_i[v_i] = F_i; the O3.2 order check is the executable
     falsifier of exactly this statement). The TANGENT system is the
     parameter-derivative of the same ODEs; differentiating the unit
     process w.r.t. inputs commutes with the Taylor expansion
     PROVIDED the underlying fields have one more derivative than
     the estimate consumes: truncation of the differentiated scheme
     at order h^2 needs C^3 regularity along characteristics.
     [LB-c1 DECLARED: certified membership gives piecewise C^1;
     interior C^3 on smooth regions is TYPICAL (piecewise-smooth
     references) but is an added clause for the RATE — without it,
     consistency holds at reduced order and convergence survives
     without the h^2 exponent. Honest, not hidden.]
 (ii) STABILITY (the D2.5-U machinery, discrete). The linearized
     discrete march obeys a discrete Gronwall along discrete
     characteristics with the SAME constant inventory as U1-U4:
      - coefficient Lipschitz bounds: U1's K_0..K_3(delta, C_geo,
        C_dat, 1/h_min) evaluated on the certified reference;
      - wall legs: the discrete reflection solve is uniformly
        solvable with the closed-form bound |R| of [T-U2RG]
        (degeneracy only at q = c, excluded by the margin);
      - front legs: the discrete implicit rule solves the
        DISCRETIZED BORDERED SYSTEM of [S-D25U-U34] §2.1; by U3-L1
        (uniform s_min, |dH/dsigma'|) and U3-H1 (Lopatinskii scalar,
        instance-certified X-U3BD) the continuum matrix is uniformly
        invertible on K_delta, hence so is the discrete one for h
        below a threshold h_0(delta, C_0) (perturbation of a
        uniformly nonsingular matrix — the h-perturbation is O(h) by
        step (i));
      - composition: the discrete characteristics obey the same
        slope bounds (T1) for h <= h_0, so the U4 counting lemmas
        (N_b bounce count via h_min; N_X crossing count; N_F from
        the entropy budget) bound the discrete composition
        VERBATIM. Discrete stability constant = LIP_shocked-type
        composition, explicit in the five constants.
 (iii) LAX EQUIVALENCE (tangent). Consistency (i) + stability (ii)
     => convergence of the discrete tangent on smooth regions at the
     consistency order: the error obeys the perturbed discrete
     Gronwall with the truncation as source (linear problem — the
     classical equivalence argument applies verbatim; no
     nonlinear-scheme subtleties enter the TANGENT system).
 (iv) TRANSPOSE (gradient). The discrete gradient is the EXACT
     transpose of the convergent discrete tangent ([T-LEMB]; O3.1
     dot-product at machine precision on the assembled march). A
     finite-dimensional transpose is norm-preserving onto the dual:
     gradient convergence in the dual pairing at the SAME order —
     nothing is lost at this step, and nothing needs proving beyond
     the identity already machine-verified.
 (v) FRONTS. The implicit-rule front derivative solves the
     discretized linearized RH + impinging row; by (ii)'s uniform
     invertibility the discrete front-shift ODE is a stable one-step
     method for the continuum front-shift ODE of G12-L3, consistent
     at the unit-process order (the RH residual is evaluated with
     the same h^2 quadratures): front-shift convergence at the same
     order. The front C^2 bound of [S-D25U-U34] §3(d2) supplies the
     regularity the front-ODE consistency consumes — self-supplied,
     no new hypothesis. QED (architecture -> written argument).

------------------------------------------------------------------------------
## §3 Conditional inventory (inherited + minted here, priced)

 - inherits [C-D25U]: the stability constants ARE the -a machinery
   (U1-U4, all now written — this doc consumed them, which is why
   S-LBML was sequenced after T1);
 - inherits [C-MAJDA] in its sharpened in-class form U3-H1 (the
   front-solve invertibility; instance-certified, class-level = the
   B1 interval brick);
 - LB-c1 interior regularity for the h^2 RATE (declared above;
   violation channel: O3.2 measures the actual order — the clause is
   SELF-MONITORING through the pre-registered oracle);
 - LB-c2 fixed march topology (= [S-D25U-U34] c2; RK-G policy is the
   operational companion: re-record events are the statement's
   boundaries, kink detection its runtime monitor).

------------------------------------------------------------------------------
## §4 What this buys, honestly bounded

G12-S1's residue R-G12.3 ("mesh limit: SCHEMA, target identified")
now points at a WRITTEN argument instead of a named architecture;
Lemma B's honesty clause tightens one more notch: exact discrete
transpose (machine fact) + written continuum limit (this doc) +
pre-registered falsifiers (O3.2/O3.3/F2) that can KILL the rate
claim on real runs. NOT claimed: uniformity of the limit ACROSS
topology strata (LB-c2), rates on C^1-only references (LB-c1), and
anything about the OPTIMIZATION iterates (TR-SQP convergence is
brick-2 territory, untouched).

------------------------------------------------------------------------------
## §5 Residue

 - The O3.2/O3.3 executions on the assembled A1 engine remain the
   EXECUTABLE half (pre-registered, brick-2 kickoff unlocks O3.3) —
   this doc is the continuum half only.
 - Axisymmetric source terms: zeroth-order, change no step —
   declared (same scope note as U3/U4).
 - A quantitative h_0(delta, C_0) (the mesh threshold below which
   the discrete front solve inherits invertibility) is explicit in
   principle from the O(h) perturbation bound + the U3-L1 floors;
   writing its constant chain is bookkeeping deferred until a
   carrier needs the number (no number minted here without one).
