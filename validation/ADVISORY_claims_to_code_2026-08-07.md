# ADVISORY — Claims-to-code traceability for the DEF/margin line
# (2026-08-07, inter-session window; every claim of the EQ-v2/S20
# story mapped to an EXECUTABLE verifier with a rejector that can
# kill it; to be built/ratified as carriers at S21 F0)

STATUS: advisory (untracked, ADR pattern). Numbers of record may
only come from the committed carriers named below once they land
(R5); nothing here is a measurement.

## NEW OBLIGATION G1 (surfaced by the user's robustness question)

G1 EXTENDED-VALUE MARGIN AT FAILED MARCHES: scipy trust-constr
evaluates constraints at TRIAL points; a trial beyond the
certifiability frontier kills the march mid-way, so the margin
constraint must return a FINITE NEGATIVE SURROGATE computed from the
partial march (the columns computed up to the failure), continuously
extending m(W) across the frontier. Without G1 the A' (margin-
constrained) optimizer can crash or stall at its first infeasible
trial. REJECTOR: a deliberate beyond-frontier trial in the A'
carrier must yield a finite surrogate and a recovered SQP step;
optimizer stall/crash = FAIL. Owner: Fase 1 (A'), BEFORE the
decisive run. (Safety net independent of G1: the certification gate
+ reject-and-shrink, proven by [X-AKNO] attempt 3 — 5 rejections
traversed, zero crashes.)

## CLAIM -> VERIFIER TABLE

C-1 "The S20 standoff was DEF-type coalescence at the control
    surface (as formally defined: same-family fold cusp ON the open
    terminal characteristic)".
    STATUS TODAY: NOT VERIFIED — consistent-with only. The S20
    record does not localize the failing cell (audit O4 + panel).
    VERIFIER (to build, S21 F0 step 1 — P0):
     (i) argmax-cell instrumentation in the cert dict of
         run_toc_record: position (x,y), cell kind, column index
         (additive, default-off like return_field);
     (ii) persistence of REJECTED designs in run_trsqp (today
         transient);
     (iii) the three-way locus test on the last certified base AND
         the rejected design's partial march: compute per-cell the
         (G)-margin val (Lambda-form, EOS-general) and the adjacent
         same-family crossing parameter.
    DECISION TABLE (each row can fire — this is a rejector-bearing
    test, not a confirmation ritual):
     (a) min-margin locus AND failing cell within the stencil
         radius of the terminal C+ chain -> DEF signature CONFIRMED
         (panel reading holds; H2 satisfied);
     (b) min-margin locus INTERIOR (upstream of the terminal C+,
         inside the wall's domain of dependence) -> INTERIOR
         CAUSTIC: the panel's DEF reading for S20 is FALSIFIED;
         the design's evaluation belongs to tier-1, and the margin
         constraint must exclude it (taxonomy case (c));
     (c) (G)-margin healthy at the failing cell yet Newton stalls
         -> NON-FOLD mechanism (spline/conditioning near the
         inserted knot; knot/station mismatch): BOTH readings
         falsified; the defect is class construction, not physics.
    CARRIER: extend [X-AKNO] or a new [X-LOCD]; the numbers enter
    the record only from the committed version.

C-2 "(G) Lambda-form boundary == Rao-Beck Eq.(4) for perfect gas".
    STATUS: THEOREM (hand proof ADVISORY_def_equivalence_proof +
    independent judge re-derivation).
    VERIFIER (to build): KAT on synthetic gamma=1.4 thermo — val
    from the Lambda-form vs Eq.(4) closed form over a (theta,alpha)
    grid, agreement at FD-derived tolerance; REJECTOR: any grid
    point beyond band. (Also suggested to GENO as a CTest.)

C-3 "At any fixed certification floor the exact DEF wall is
    REJECTED at fine mesh" (panel S1 sharpening).
    VERIFIER: twin falsifier leg 1 (pre-registered by the panel):
    march GENO's flagdef=1 wall (Table-2 short-DEF twin) in our
    engine on a refinement ladder -> cert_worst must cross 1 at
    fine mesh; AND the de-focused approximant family must certify
    (margin-positive neighbors exist). REJECTOR: DEF wall certifies
    at all r (kills the claim) or no approximant certifies (kills
    the containment reading).

C-4 "The S20 walk was approaching a DEF-sector optimum".
    Derived claim: verifiable only AFTER C-1 outcome (a) and C-3
    both pass; otherwise it falls with them.

C-5 "mu >= 0 <-> jump-depth minimality" (the panel's surplus
    prediction, no classical counterpart).
    DEMOTED TO SIGN TEST (2026-08-11, red-team RT-4): the verifier
    below tests the SIGN only; it is NOT decisive for O3 and no
    "magnitude consistent with the measured mu" clause may be
    attached until (i) the one-page derivation dJ/d(depth) =
    -mu*dm/d(depth) under H3 exists and (ii) the mu-estimator
    (KS-rho + floor-extrapolation) carries a derived band — under
    B-stationarity (O1 undischarged) no mu exists to measure.
    VERIFIER: GENO deeper-jump family (jump depth beyond the
    boundary landing) -> C_Fv must DECREASE monotonically.
    REJECTOR: C_Fv increasing on the deeper-jump family.

C-6 "The search CONTINUES even when trial profiles would carry an
    interior fold".
    (safety half) VERIFIED of record: [X-AKNO] attempt 3, 5
    rejections traversed, ordered return to the certified base.
    (progress half) NOT YET: requires A' + G1; verifier = the G1
    rejector above + an outcome-I convergence on a case whose
    optimum is margin-active.

## HONEST LIMITS OF CERTAINTY (Q1 of record)
 - Interior-shock designs are never EVALUATED in tier 0 (the field
   does not exist in the class); they are avoided (steering) and
   survived (gate). Evaluation of such designs = tier-1 machinery.
 - Unproven: MFCQ at the frontier (panel H3), KS conservativeness
   margin, the h->0/mu_0->0 double-limit order (O5). Each is a
   named conditional with an owner phase, not a silent assumption.
