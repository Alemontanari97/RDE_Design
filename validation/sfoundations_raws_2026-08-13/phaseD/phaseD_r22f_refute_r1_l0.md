# R22-F CENTERPIECE — REFUTATION, ROUND 1, LENS L0
# (variational/optimization structure: fiber lower bounds, J-variation,
# duality, channel (ii)/(vi) quantification structure)

Session: S-FOUNDATIONS-C4, Blocco 1 v2, 2026-08-20. Target:
validation/sfoundations_raws_2026-08-13/phaseD/phaseD_r22f_centerpiece.md
(author draft revision 1, INCLUDING [GRAFT-*]/[REV-*] markers and tables).
Numbering: no prior r22f refuter round exists on disk (checked by glob of
phaseD/ this window) — numbering starts at R22F-L0-1; persisting prior
findings re-counted = 0.

READ-DEPTH DECLARATIONS (this window):
- BRIEF_blocco2_phaseD.md (as amended): [FULL].
- BRIEF_blocco2_phaseD_addendum_c4.md: [FULL].
- phaseD_r22f_centerpiece.md: [FULL].
- swirl5f_fun.md §4 (SS4, :535-594) + DISPATCH_swirl5f.md :65: [SECTION]
  — load-bearing for R22F-L0-4, verified at source.
- docs/rde_nozzle_MASTER.md: [SECTION] at :74, :390-397 (thrust
  functional station), :860-919 (T-T3-MAP (a)-(d)), :1077-1183
  (D.6-D.18 block), :1252-1267 (per-streamtube ideal-thrust proof) —
  anchor verification for the draft's Part-1 citations.
- SYNTHESIS_nozzle_rde_arrivals.md, FIELD_ATLAS_targeted_c4.md, the four
  NOZZLE_RDE_STUDY dossiers: [NOT-READ] this window — no finding below
  leans on them (grafts not attacked at this lens).
Executable probe (standing preference honored): validation/
sfoundations_raws_2026-08-13/phaseD/r22f_v2_probe_r1_l0_fiber_sign_2eps.py
— ran, all asserts pass; all probe numbers are SYNTHETIC counter-model
inputs (CT-6 respected: no number from the four nozzle papers used).

MANDATE-COVERAGE DUTY (all lenses, round 1): channel (vi) with the
delta/mu schema is ABSENT (finding R22F-L0-1); the T-RED design-gradient-
level schema is ABSENT (finding R22F-L0-2); the Harroun Fig. 18 exhibit
WITH per-term disposition IS PRESENT and conforming (§2.3: page-verified
exhibit, data-anchored-shadow connection, per-term BOUNDED-here /
deferred-with-rows / M-RED table — mandate satisfied on that element).

------------------------------------------------------------------------

## R22F-L0-1 — REPAIR (mandate coverage): forchetta table has NO
## channel-(vi) OPTIMUM-SHIFT row

ANCHOR: draft Part 5 table :663-669 (rows (i)-(v) only); [GRAFT-G07]
gap flag :738-749 already records the absence. BRIEF LINE: :112-126
(channel (vi) mandate, "(vi) OPTIMUM-SHIFT channel ... the deliverable
states the perturbation bound |argmax shift| <= delta/mu ...").
REASON: a mandated centerpiece element is missing from the deliverable
of record. The graft-reviser's flag is a flag, not a repair: the row
itself (best/worst cells, provenance, rigor class, what-tightens-it,
the "where the gradient-level bound is not yet derivable, the cell says
so and names what would derive it" clause) must be written. Addendum_c4
(b) (:8-15) right-sizes the content — SCHEMA + named duty is the
acceptable landing — but does not waive the row. NOT a demand for a
closed-form gradient bound (SR-C4-13 respected).

## R22F-L0-2 — REPAIR (mandate coverage): T-RED delivers the bound
## schema at the VALUE level only; the DESIGN-GRADIENT level is absent

ANCHOR: draft §2.2 :294-326 (value-level schema: mean nullity,
first-order scales, license gate, uniformity); §5 [GRAFT-G07] flag
:746-749 ("Part 2 does not deliver the design-gradient-level bound
schema alongside the value level"). BRIEF LINE: :120-125 ("T-RED's
section (2) therefore delivers its bound schema at BOTH levels: value
AND design-gradient of the residual operator on the admissible profile
manifold"). REASON: mandated element absent. Per addendum_c4 (b) the
acceptable form is an honest SCHEMA (hypothesis list + bound structure
+ what-derives-it: five-field content bound / route-B / M-RED gradient
measurement) at declared rigor class — the draft currently has NO
gradient-level section at all, which is below even the right-sized bar.
See R22F-L0-8 for the L0 soundness conditions the schema must carry.

## R22F-L0-3 — REPAIR (delivery-check): addendum-(c) structural
## declaration absent from the forchetta header/notes

ANCHOR: draft :657-662 (the graft-reviser's own GAP FLAG under
[GRAFT-G10]). CARRIER LINE: addendum_c4 (c) :17-26 ("MUST APPEAR IN THE
FORCHETTA TABLE ... stated in the table's header or notes ... This
declaration is a delivery-check item"). REASON: the no-external-referee
sentence of record (no unsteady c_F datum discriminates the
2D-per-phase-averaged prediction against 3D-unsteady truth; the Harroun
1.25-flat is quasi-cycle-averaged = the non-discrimination datum, not a
referee; the bracket closes only via our own R22-CFD or dedicated
procurement) is not yet in the draft's header/notes — G-10 carries the
enrichment and the consequence but not the record sentence itself.
Must land at revision.

## R22F-L0-4 — BREAK: [T-DISC-3] misapplies the 2-epsilon lemma; the
## statement as written is FALSE

ANCHOR: draft §1.3 :176-198, the claim at :184-189 ("if a designer
optimizes ANY functional that factors through pi (a pressure-only
surrogate ...), the resulting design is up to 2*eps_fib suboptimal for
the true J"), with eps_fib(P) := sup over the fiber of |J(s) − J(s')|
(:178-180). SOURCE VERIFIED: swirl5f_fun.md :546-564 — claim 10 of
record is a lemma about J_exact vs J_avg with premise
(U): sup_{Sigma in A} |J_exact[Sigma] − J_avg[Sigma]| <= eps, and
conclusion J_exact[Sigma*] >= sup_A J_exact − 2 eps; sharpness :566-570;
weakened-uniformity variant :575-582; DISPATCH_swirl5f.md :65.
REASON THE TRANSPLANT FAILS (quantifier direction): the lemma's eps is a
UNIFORM value-error bound for the SPECIFIC surrogate being optimized;
the fiber spread eps_fib does not bound |J_exact − f(pi(.))| for an
arbitrary f factoring through pi. EXECUTABLE COUNTEREXAMPLE (probe
PART A, ran, assert passed): two admissible designs in DIFFERENT fibers
(each fiber design-realized as a singleton => eps_fib = 0), surrogate
f == 0 (factors through pi), a legitimate argmax selection of f is
10-suboptimal while the draft's claimed ceiling 2*eps_fib = 0. The
statement is false for "ANY functional that factors through pi".
CONSEQUENCE DOWNSTREAM: [T-DISC-4](a) :208 ("the loss is not
recoverable by optimization downstream of pi ([T-DISC-3])") and the F5a
template sentence :189-191 inherit the defect until repaired.
REPAIR PATH (named; content is salvageable — this is why the break does
not kill Part 1): split the statement into its two sound directions,
each at its own grade:
  (a) IRREDUCIBILITY / LOWER form (the conviction direction): for EVERY
  f factoring through pi, sup_Sigma |J_exact − f(pi(.))| >= (1/2) x the
  within-fiber J-oscillation over any DESIGN-REALIZED same-fiber pair
  (two designs whose data lie in one fiber get one f-value); by the
  sharpness construction (:566-570) a legitimate argmax selection can
  then be up to the full oscillation suboptimal. This needs a
  DESIGN-REALIZABILITY premise, which the draft nowhere states:
  [T-DISC-1] constructs same-fiber DATA pairs, not designs — either
  name the premise (same-fiber pair realized as s(Sigma_1), s(Sigma_2)
  with Sigma_i admissible) or scope the consequence to the data-class
  reading and say so.
  (b) ADEQUACY / UPPER form: exactly claim 10 with J_avg replaced by
  the CHOSEN f, premise (U_f) sup_Sigma |J_exact − f(pi(.))| <= eps_f,
  conclusion 2*eps_f — per-surrogate, never with eps_fib substituted.
  Also: eps_fib must be design-indexed (sup over the traces reached by
  the design sweep), which the current per-P definition is not.

## R22F-L0-5 — REPAIR: [T-DISC-2](i) — pressure-thrust "fixity"
## mis-justified, and H2.2 is over-determined on actual solution pairs

ANCHOR: draft :132-138, specifically :136-137 ("The pressure-thrust
term Int (p − Pa) dA is FIXED within the fiber (same P trace)");
LOWER-BOUND READING :152-158; [T-DISC-4](a) :203-211. SOURCE VERIFIED:
the thrust functional of record evaluates momentum flux + (p − Pa) on
an ENCLOSING/EXIT surface (M0 :74, :390-397), not on the interface —
the fiber's shared P trace is the INTERFACE trace, so "(same P trace)"
is a non sequitur as a justification: within the theorem the fixity
holds only BY HYPOTHESIS H2.2 (fixed exit static-pressure trace), and
the proof sketch must say so.
DEEPER LIMB (probe PART B, ran): for ACTUAL per-phase solution pairs,
H2.2 + the fiber-fixed interface mdot is OVER-DETERMINED — at fixed
(h0, s, mdot, A_e) the exit pressure is an output, and turning on
Gamma moves it (+3.5% p_e in the synthetic quasi-1D counter-model; the
physical face of this shift is the draft's own B1 radial-equilibrium
companion, 0.6-9% of p). Hence leg (i) is a BOOKING-level comparison
(frozen exit conditions), and the LOWER-BOUND READING's "BOUNDED BELOW
BY A STRICTLY POSITIVE, SINGLE-SIGNED functional" plus [T-DISC-4](a)'s
"J separates within them single-signedly" are asserted about
within-fiber J-variation WITHOUT the booking qualifier — the actual-
pair statement needs the exit-pressure shift (B1) adjudicated in sign
against the E_theta debit, which the draft lists as a "companion"
(:148-151) but never composes. HONESTY NOTE (zero inflation): in the
probe's counter-model the actual Delta J (−2.041% of J) stays within
~0.2% of the booking Delta J (−2.037%) and keeps its sign — the
conclusion is plausibly robust; what is defective is the JUSTIFICATION
and the missing scope qualifier, not (on present evidence) the sign
claim itself. REPAIR: re-anchor the pressure-term fixity to H2.2,
label leg (i) explicitly as booking-level (fixed-exit-state
comparison), and either (a) add the actual-pair composition with B1's
sign adjudicated, or (b) scope [T-DISC-4](a) and the LOWER-BOUND
READING to the booking level, with the actual-pair form named as an
M-RED/B-2 measured question.

## R22F-L0-6 — REPAIR: DROP-convention branch of the [T-DISC-1] family
## reverses the sign leg; [T-DISC-2](i)/[T-DISC-3] composition has a
## convention seam

ANCHOR: draft :99-104 ([T-DISC-1] proof: "h0 fixed under the DROP
convention verbatim, and under the FOLD convention fixed provided ...
compensated"), :128-138 ([T-DISC-2](i) "strictly decreasing ... J(s_
lambda) strictly decreases in lambda^2"), :164 (H2.4 fold/drop switch),
:181-183 ([T-DISC-3] "> 0 by [T-DISC-1]+[T-DISC-2](i) wherever swirl
content is admissible"). REASON: under the DROP convention the booked
h0 is fixed while the TRUE total enthalpy grows with the added swirl,
h0_true(lambda) = h0_b + lambda^2 Gamma_0^2/(2 r_int^2); the exact
per-streamline algebra the draft itself cites then gives, at frozen
exit conditions, u_e^2(lambda) = u_e^2(0) + lambda^2 Gamma_0^2
(1/r_int^2 − 1/r_e^2): the within-fiber momentum thrust INCREASES with
swirl for r_e > r_int and is IDENTICALLY CONSTANT at r_e = r_int
(probe PART C, ran: +88889 m^2/s^2, 0, −90000 m^2/s^2 at r_e/r_int =
1.5, 1.0, 0.8). So the strict decrease claimed by leg (i) FAILS on the
DROP branch of the very family [T-DISC-1] admits, and at r_e = r_int
the DROP family exhibits ZERO separation — [T-DISC-3]'s "> 0 wherever
swirl content is admissible" does not follow from the cited
composition there (only the FOLD/compensated variant separates, and it
needs H1.3 headroom). This is CONSISTENT with the draft's own B2
repaired clause (geometry-signed DROP bias, channel (iii) BEST cell
:667) — the defect is that leg (i) and the (iii)-cell carry
incompatible sign stories with no seam. REPAIR: restrict leg (i) to
fixed-TRUE-h0 comparisons (FOLD or compensated variant; H1.3), state
the DROP branch as geometry-signed with the r_e vs r_int criterion
(matching B2), and re-derive [T-DISC-3]'s positivity as: eps_fib > 0
wherever the compensated variant is admissible (H1.3 headroom), with
the r_e = r_int no-headroom corner named as the degenerate case.

## R22F-L0-7 — AMENDMENT: D1.2's "phase-uniform default" is unpinned,
## and eps_fib's extent depends on the reading by orders of magnitude

ANCHOR: draft :52-56 (D1.2: pi "retains the per-phase pressure trace
P(xi) and replaces every other field by the phase-uniform default"),
:178-180 (eps_fib as fiber sup). REASON: "the phase-uniform default"
is not defined — if the default is the data's OWN mu-means, the fiber
fixes P plus all field means (the fiber coordinate = fluctuation +
swirl content, the object [T-DISC-1] actually sweeps and M-RED B-2
actually measures); if it is a canonical constant, the fiber is the
full preimage of the P trace and eps_fib includes arbitrary h0/s trace
variation — O(1)-scale, never bracketed by any B-2 measurement, and
[T-DISC-4](a)'s association of the conviction with the "1.5-3% class"
becomes a category slip. AMENDMENT: pin D1.2 (recommended: default =
the family's own mu-means, so the fiber is the calibrated-scalars
fiber and eps_fib is exactly the quantity M-RED's B-2/§3.5 outputs
speak to); propagate the pin into eps_fib's definition and the
[T-DISC-4](a) scale sentence.

## R22F-L0-8 — AMENDMENT: L0 soundness conditions for the delta/mu
## schema (to be carried into the channel-(vi) row when written)

ANCHOR: brief :117-126 (|argmax shift| <= delta/mu, mu = measured
engine curvature at S*, delta = design-gradient-level residual bound);
addendum_c4 (b) :8-15. REASON (constructive — no row exists yet to
break; the schema ITSELF is sound only under these named conditions,
and a row written without them would be unsound at this lens):
  (1) BASIN CLAUSE: the perturbation bound is the strongly-concave
  argmax-shift lemma; mu must be a curvature FLOOR (smallest reduced-
  Hessian eigenvalue) holding UNIFORMLY on a neighborhood containing
  the shift ball, not the point Hessian at S* alone. A point-measured
  mu licenses only the a-posteriori form: valid IF delta/mu <= the
  certified basin radius (state the check as part of the cell).
  (2) CONSTRAINED FORM: at an active-set optimum the correct mu is the
  reduced Hessian on the critical cone and delta the norm of the
  PROJECTED design-gradient residual (feasible directions only), with
  multiplier/margin shifts priced per the KKT-with-margin-multiplier
  formalization of record (S20 ladder) — an unconstrained-form cell at
  a constrained S* would overclaim.
  (3) METRIC CONSISTENCY: the segmented TR-Newton curvature of record
  is parameterization-dependent; delta must be measured in the DUAL
  norm of the SAME design-space metric in which mu is an eigenvalue,
  else delta/mu is not norm-invariant and the cell number is
  meaningless. Name the metric in the cell.
  (4) The right-sized landing (addendum (b)) then reads: schema (1)-(3)
  + named deriver of delta (five-field content bound / route-B / M-RED
  gradient measurement) — that IS an acceptable dry outcome at this
  lens.

## R22F-L0-9 — NOTE: verified-at-source items (positive record for the
## judge; no action)

(a) §3.5's eps wiring is CONSISTENT with claim 10 of record: the
lemma's eps is sup_Sigma |J_exact − J_avg| (swirl5f_fun.md :553-554) —
the reduction error, which is exactly what M-RED's per-family eps(F)
instantiates; the draft's per-family scoping with (U) held open
(:193-196, :559-563 of the draft) is the correct licensed reading.
The misapplication is confined to [T-DISC-3]'s p-only transplant
(R22F-L0-4). (b) Draft anchors spot-verified at source this window:
D.6 (M0:1077-1101), D.9 (M0:1131-1143), D.10 incl. the B-1
normalization trap (M0:1144-1161), D.12 (M0:1166-1172), D.18/
[MS-DEF-KRES] r7 pointer (M0:1173-1183), T-T3-MAP (c)/(d)
(M0:889-914), thrust-functional station (M0:74, :390-397) — all match
the draft's citations. (c) B-2's debit integrand (mdot-weighted
u_theta^2/(2 u_e), draft :532-536) is dimensionally and first-order
correct against the per-streamline relation. (d) Fig. 18 mandate
element conforming (see MANDATE-COVERAGE above).

------------------------------------------------------------------------

## PAPERS NEEDED

NONE for this refutation. (All attacks close on carriers already on
disk; no procurement would change any finding above.)

## MACHINE SUMMARY (round 1, lens L0)

breaks = 1 (R22F-L0-4)
repairs = 5 (R22F-L0-1, R22F-L0-2, R22F-L0-3, R22F-L0-5, R22F-L0-6)
amendments = 2 (R22F-L0-7, R22F-L0-8)
notes = 1 (R22F-L0-9)
persisting_prior = 0 (no prior r22f refuter round exists on disk)
probe: r22f_v2_probe_r1_l0_fiber_sign_2eps.py — 3 parts, all asserts
pass; synthetic numbers only (CT-6 clean).
