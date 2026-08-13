# ADVISORY — S24 DE-side margin-bucket adjudication: adversarial panel verdict
**Judge-adjudicated in one round** (repo standing rule; Form-2 panel-to-convergence)

- **Date**: 2026-08-12
- **Workflow id**: wf_f609fe99-469 (ordered mid-session S24, of record at session log step 9)
- **Participants**: E1 = classical gasdynamics / Rao-Beck fidelity; E2 = variational / KKT
  structure; E3 = numerics / discretization; dedicated REFUTER (attacks R1-R9);
  JUDGE (this document). Position files: scratchpad `s24_panel_E1-classical.md`,
  `s24_panel_E2-variational.md`, `s24_panel_E3-numerics.md`, `s24_panel_REFUTER.md`.
- **Subject**: the S24 single-author margin-bucket scope adjudication of record
  (commits 366c2d7 + cf7afda; session log `validation/PROGRESS_2026-08-12_S24_f1b.md`
  steps 6-9): *val is a construction-surface criterion; leg-2 margin = KS of the
  (G)/Lambda-form val over the DE-SIDE bucket (registered terminal-C+ chain nodes
  strictly lipward of the last val = 0 crossing); rung-frozen lane mask; march
  certification = the shock guard; mild instances degenerate to the whole control
  surface; branch semantics F1-F7 adopted verbatim.*
- **Pattern**: untracked ADR (validation/ advisory of record). Gate: the decisive
  [X-DEFTW] campaign run was HELD pending this verdict (user order, step 9).

## The question

Is the S24 DE-side margin-bucket adjudication
(a) FAITHFUL to the Rao-Beck DEF logic;
(b) CONSISTENT with EQ-v2 Direction A/H2 and the pre-registered falsifier branch
    semantics F1-F7;
(c) a legitimate ENLARGEMENT of the explorable design domain (nonempty feasible set
    at deep instances, march certification guarding shocks);
(d) safe to consume for the DECISIVE ladder campaign of this session?

## MEASURED FACTS (restated of record; session log steps 6-9)

- **M1 (whole-field bucket infeasible; val < 0 on certified fields, both codes)**:
  first derive run (whole-field [X-MGOV] S22 bucket) FAILED with
  m_ref = -8.0840e-01 at BOTH the GENO-seeded design and its perturbation,
  bit-identical; the minimum sits in the W-independent attachment region
  (theta ~ 46 deg) and MATCHES val ~ -0.81 (-0.8084 measured) that the SAME
  monitor reads at the attachment of GENO's own certified, A4-verified
  (rel 4.163e-4) defnoz output field.
- **M2 (D'-crossing geometry, both legs)**: the lip-C+ chain traced on GENO's own
  field crosses val = 0 at D' = (5.2015, 3.4073) [r1] vs (5.1994, 3.4058) [r2],
  two-resolution agreement 2.613e-3 INSIDE the K_RICH band 1.2122e-2; den(D') =
  0.684 (the GENO |den| < 1e-10 guard cannot bite there); the chain is
  val-NEGATIVE kernelward of D'. Leg-2 seed: chain 144 nodes, 56 registered CS,
  crossing at chain idx 95, min DE val = +1.0848e-2 at idx 96 (just lipward);
  min |den| on the CS = 5.655e-1.
- **M3 (whole-CS bucket infeasible; DE-side restores feasibility)**: the CS-bucket
  derive run measured min CS val = -3.806e-01 at the KERNEL END at the GENO seed,
  ALL 8 bump candidates infeasible (-0.36..-0.40). Hence every bucket containing
  the attachment or the sub-D' chain segment has an EMPTY feasible set at this
  instance for the whole class INCLUDING the classical DEF design read through the
  same monitor. The DE-side bucket restores m_ref = +4.2357e-3, N = 45 DE lanes;
  pre-registered ladder mu0 = {2.1178e-3, 1.0589e-3, 5.2946e-4, 2.6473e-4},
  rho = K_RICH ln(N)/mu0_min = 5.7518e+4, KS gap = 6.618e-5 (ladder/rho
  arithmetic independently re-verified by E3 and by the judge — matches to all
  printed digits).

## Per-question verdicts

### (a) Faithful to the Rao-Beck DEF logic — **YES (unanimous, 4/4)**

E1 (CONFIRM): the paper evaluates the Eq. (4) object ONLY at candidate points D on
the terminal right Mach line (verbatim "leads to the following relation at the
point D", p.2; Fig. 2 is a state-plane boundary; Nomenclature: "D' — points in the
invalid region of the right Mach lines"); no field criterion exists in the read
corpus (Hoffman 1967 = corner condition, a different object). val < 0 upstream of
D' is DEFINITIONAL to the DEF regime — the PM compression exists for no other
reason (paper p.3/4: invalid points D' "can be brought back to the valid boundary"
by isentropic jumps). E1's sharpening (supports the adjudication): via the S4 hand
proof, val = 0 is a POLE of the reduced DE-march ODE (dtheta/dR ~ 1/val) — val > 0
along DE is the march solvability condition, implicit classically because the
construction starts ON the boundary and moves lipward. E2/E3 concur from the GENO
source: the last-non-positive/maximal-positive-suffix rule is the direct-problem
mirror of GENO's own jb-overwrite at every (-,+) crossing + xstar bisection +
`xsol < xstar -> pmcompression_solve` dispatch (Rao_m.f90 L519-523, L538-558,
L577-582, L646-651; landing window (0, 1e-6) at L547). Strictly-lipward exclusion
of the crossing node is the REQUIRED discretization of the classical equality
val(D) = 0 (E3: including it "would re-create the fixed-floor infeasibility of the
exact DEF wall at every rung"). Refuter attacks R1 (fold-vs-val), R3 (off-chain
val < 0), R4 (multiple crossings) all FAIL on measured facts (den(D') = 0.684;
M1; single crossing measured on both legs; mirrored last-crossing rule in GENO
source). Conditions accruing: C9 (naming + existence-limit declarations).

### (b) Consistent with EQ-v2 Direction A/H2 + F1-F7 — **YES, WITH MANDATORY DECLARATIONS**

E2: the DE-side bucket "is the only bucket under which Direction A's statement is
well-formed at a deep-DEF instance"; the crossing-end cusp is the self-consistent
D'-analog; as mu0 -> 0 the binding migrates to the crossing end and val at the
active cusp -> 0 — exactly the classical landing inside GENO's (0, 1e-6) window;
EQ-v2's pre-registered zero set is val's NUMERATOR zero (refuter's own
re-derivation: Lambda*tan(alpha)*sin(theta) = sin(theta-2alpha) IS the Eq. (4)
boundary, NOT den = 0). Branch by branch: F1/F3/F7 untouched; F6 STRENGTHENED
(1-D consecutive-run census is the meaningful H1 object; the whole-field census
would have fired vacuously at every design of this class); F4 intact on the
ladder direction; F5 remains capable of firing (persistent lip-end binding = H2
lip-corner exclusion). BUT the step-8 sentence "Branch semantics F1-F7 UNTOUCHED"
is an OVERCLAIM of record: two F5 kill limbs are RE-ROUTED (axis-side -> F2
position-vs-D'; field-interior caustics -> march-cert + F4 margin-inactive
branch), F2's on-characteristic half is satisfied BY CONSTRUCTION (its remaining
content = position along the chain), and the F1/F4 joint-refinement halves are
UNEXECUTABLE as committed (no refine stage — judge source check, main()
L1145-1158). Conditions: C1, C2, C7, C8. With those declared, every H1/H2-killing
mechanism retains a firing path (Refuter R6, limb-by-limb).

### (c) Legitimate enlargement of the explorable design domain — **YES (unanimous)**

The enlargement is measured, not argued: feasible set EMPTY (M1, M3) -> NONEMPTY
(m_ref = +4.2357e-3) under the DE scope, and the emptiness held for the CLASS
including GENO's own DEF design — E3: "A constraint with empty feasible set prices
nothing — EQ-v2's KKT statement requires the DE scope or it is vacuous at deep
instances." No shocked-field admission channel opens: "val < 0 was NEVER the shock
guard: S22 branch (c) proved certification fails at HEALTHY val (0.61-0.86) and
the K_disc ~ A_0 bridge is FALSIFIED" (E3; M0 of record). The shock guard — per-cell
Newton march certification with derived tolerances — is RETAINED (rung-start gate,
REQ-NONSTALL walk-gate rejector, G1 finite surrogate). Sufficiency of the guard is
PRACTICE conditional on H-int (interior-fold-freeness of the inverse net), an
INHERITED declared conditional (C1 field-level rejector, owner F2, census row 10),
not created by this adjudication (Refuter R3: "the residual guard question is the
already-structurally-gated C1, not a new gap"). The terminal-rung certification
gap is closed by condition C4. KS <= vmin makes the enforced set an inner
approximation — conservative, never permissive (E2). Mild-instance degeneration
(no crossing -> whole CS -> feasibility-equivalent to [X-MGOV] at eps = 4, min
field val 0.68) reconciles the S22 record without retroactive edits.

### (d) Safe to consume for the decisive ladder campaign — **YES, CONDITIONED (GO)**

No position sustains NO-GO. The refuter's net: "I could not construct a failure
that produces a false CONFIRM, and the measured facts (M1-M3, den(D') = 0.684,
GENO's own last-crossing + jump logic) close every kill line." All surviving
defects are attribution/declaration-class: they can make a branch fire SPURIOUSLY
or contaminate a site call (never a false CONFIRM), or they under-declare a
semantic delta. Every one is cheap, consumes already-logged quantities or one-line
asserts, and none touches the bucket definition or the kill criteria. The
post-hoc-surgery attack (R9) FAILS: the literally pre-registered problem "has an
EMPTY feasible set at this instance ... running it as worded is impossible, so
SOME adjudication was forced"; the replacement is derived from the
pre-registration's OWN cited theory and GENO's own source logic, was declared and
COMMITTED before the decisive run, and the deviation stays DECLARED in M0 (C1/C2).

## Disagreements resolved (expert vs refuter vs record, verbatim where verdict-moving)

**DR-1 — "Branch semantics F1-F7 UNTOUCHED" (step 8) vs E2/Refuter.**
Refuter R6: "the F5 axis-limb ->F2 and interior-caustic ->cert/F4 re-routings are
real semantic deltas to the pre-registered branch map and must be DECLARED in the
R4/M0 registration, or 'branch semantics untouched' is an overclaim." E2: "two
narrowings (F2's on-characteristic half by construction; F5's interior =
chain-interior with field duty on certification) that must be DECLARED in the
verdict wording (they are consequences of the object correction, not alterations
of the tests)." E1 does not contradict (notes F2 "is the ONLY branch comparing the
two lanes' intersection point ... pre-registered and armed; adequate").
**RESOLUTION: refuter's declaration duty ADOPTED as blocking record condition
(C1). The substance — every kill path retained — is unanimous (Refuter R6 itself:
FAILS as "unfalsifiable/vacuous"). The step-8 sentence is qualified of record, not
retracted in substance.**

**DR-2 — Refuter R8 vs E3 R1 on refinement.**
R8 dismissed the strict-lipward gap partly because "the exclusion vanishes under
refinement (the refine stage is the F1/F4 joint-refinement half)". E3: "the
'refine' stage that the docstring pre-registers ... is NOT implemented: main()
dispatches only leg1/derive/campaign ... As committed, the verbatim F1 clause ...
and the F4 refinement half are UNEXECUTABLE." **Judge source check (this round):
main() L1145-1158 has NO refine path; F1 note L1036 itself names the missing
stage. E3 is right on the fact. R8's kill-failure verdict still stands on its
first leg (the F2 band includes K_RICH * r_chain, present at L1030-1031), so R8
remains FAILED-as-kill; but the refinement-dependent half of its dismissal is
CONTINGENT on C7. C7 adopted, blocking for F1/F4 verdict wording.**

**DR-3 — mask-drift risk direction: E2 (d)-gap / E3 R2 vs Refuter R5.**
Refuter: "exploit => fired branch, not false confirm." E3: "a machinery artifact
(mask staleness) would masquerade as the scientific 'BF does not -> 0' rejection —
the worst failure mode here." E2 names the three contamination channels (F4
tracking fires/clears spuriously; F2 band lacks crossing drift; end-vs-interior
site flip). **RESOLUTION: no contradiction — all three agree no false-CONFIRM
channel exists; the risk is ATTRIBUTION of a fired branch. Since a fired
pre-registered branch is a verdict of record, attribution integrity is BLOCKING:
C3 adopted (judge-merged from E2 R-i/R-ii/R-iii + E3 R2 + Refuter R5(ii); the
three formulations are substantively identical — same gate quantity, same
STENCIL_RADIUS threshold, same re-freeze-once semantics).**

**DR-4 — Refuter R1 (mu should price the fold den = 0, not val).**
Self-resolved by the refuter's own re-derivation: "EQ-v2's own pre-registered zero
set IS val's numerator zero (the Eq.(4)/Rao-Beck boundary), NOT den = 0. The
attack's premise contradicts the statement of record it claims to defend." Plus
measured den(D') = 0.684. No expert dissents. **RESOLUTION: attack FAILS; the
surviving sliver (den -> 0+ with theta < alpha is val-feasible while df2/dV = 0)
is a monitoring duty, not a bucket defect — C6 adopted; note it is not specific to
the DE bucket (the S22 whole-field bucket accepts the same pole branch).**

**DR-5 — E1 CONFIRM (no repairs) vs E2/E3/Refuter REPAIR(named).**
Not a substantive conflict: E1's scope (classical fidelity) generates only
declaration-level annotations (adopted, C9); the repairs live in the branch-map,
mask-drift and instrumentation domains E1 did not adjudicate. **RESOLUTION: net
panel verdict = REPAIR(named) -> conditional GO. No unanimity manufactured: E1's
CONFIRM stands within its scope; the panel verdict is the conjunction.**

**DR-6 (minor, judge source check) — E3 R4 wording vs carrier.**
E3 asked to add "cert_worst (and N_DE, n_act)" to the rung record; the source
shows n_act IS already stored inside the census tuple (L993, census = (n_act,
n_cl)); cert_worst and N_DE are genuinely absent, and the cert gate (L919-925)
guards rung STARTS only. **RESOLUTION: C4 keeps cert_worst + N_DE as the required
additions (making n_act explicit costs nothing and is folded in).**

## Named conditions (every surviving repair; each with owner and placement)

Carrier conditions C3-C6, C10 land in `validation/def_twin_falsifier.py` and the
derive stage re-runs PASS **BEFORE the decisive campaign run**. Record conditions
C1, C2, C8, C9 land in the same-session M0/R4 registration; C1 and C7 land
**before any F1-F7 verdict becomes of record**.

- **C1 [RECORD, blocking]** Branch-map declaration: qualify "branch semantics
  F1-F7 UNTOUCHED" of record to "kill criteria unchanged; margin OBJECT re-scoped;
  two F5 limbs re-routed (axis-side -> F2 position-vs-D'; field-interior caustics
  -> march-cert + F4 margin-inactive branch); F2's on-characteristic half by
  construction". Owner: S24 (R4 step, this session). [Refuter#1 + E2 narrowings]
- **C2 [RECORD]** EQ-v2 Direction-A clause corrected at constant content: the fold
  "touches the CONSTRUCTION SURFACE only at D'" (not "the computed domain");
  register the instance-class-sensitive bucket-scope boundary (mild = whole-CS
  degeneration, eps = 4 coincidence with [X-MGOV]; deep = DE-side). Owner: S24 R4.
  [E2(b)4 + step 7/8 accrued duties]
- **C3 [CARRIER, blocking, pre-run]** Rung mask self-consistency gate: per rung
  log |i_cross(start) - i_cross(end)| and the frozen-vs-re-derived val_min delta;
  drift > STENCIL_RADIUS chain nodes => the rung's F2/F4/F5 readings are declared
  mask-confounded and the rung repeats ONCE with a re-frozen mask at the same mu0
  (declared), else blocked-with-named-cause; fold measured drift into the F2 band
  and the F4 activity allowance; record the gate outcome per rung in the campaign
  artifact. Owner: S24 carrier. [E2 R-i/R-ii/R-iii = E3 R2 + Refuter R5(ii),
  judge-merged]
- **C4 [CARRIER, pre-run]** Terminal certification gate + per-rung record: assert
  st_new cert_worst <= 1.0 on the final rung before F1-F7 consume its J/wall; add
  cert_worst and N_DE (n_act made explicit) to every rung dict. Also the
  containment of the declared G1 penalty-scale weakness: a lane-count (N_DE) drop
  is a declared adjudication item; the penalty formula is NOT re-derived ad hoc.
  Owner: S24 carrier. [E3 R4 = Refuter#3; E3(d)4]
- **C5 [CARRIER, pre-run]** Mask-mapping identity rejector at derive: the
  masked-lane KS min at the start design must reproduce the chain-record m_ref
  within gap + derived band (a mapping error breaks it grossly); derive re-run
  PASS. Owner: S24 carrier. [E3 R3]
- **C6 [CARRIER, pre-run]** Rung-level den monitor: carry den_min over the DE
  bucket into every campaign rung log, tied to the registered den-vs-val = 0
  semantic delta (measure the val-feasible den-pole branch never approaches).
  Owner: S24 carrier. [Refuter#2]
- **C7 [SCOPE/RECORD, blocking for F1/F4 wording]** Refine stage: implement the
  pre-registered "refine" stage, OR formally re-scope F1/F4 to the ladder
  direction with the joint-refinement half carried as a NAMED conditional,
  declared before any F1/F4 verdict of record. Owner: S24 declaration; if carried
  as conditional, discharge owner = the pre-authorized optional session (S24+1),
  else F2 entry (judge-added placement, consistent with the session's [P4] budget
  rule). [E3 R1; qualifies Refuter R8]
- **C8 [RECORD]** Site-label quoting rule: "crossing-end binding = expected
  classical D' site" is quotable only TOGETHER WITH the F2 |argmin - D'_GENO|
  distance — the label alone is self-referential. Owner: S24 R4. [Refuter#4, R2
  residue]
- **C9 [RECORD, declaration-level]** (i) D/D' naming note: spatially coincident,
  state-distinct (the jump is a state discontinuity at fixed location); (ii) the
  empty-DE-bucket case (all-negative registered chain) DECLARED as the direct
  image of the classical existence limit ("no control surface and hence no
  optimum thrust nozzle can be defined"), with its loud-failure semantics
  (m_ref = nan -> feasible-start check fails). Owner: S24 R4. [E1 nuances 1-2 +
  E1 existence-limit audit]
- **C10 [LOG]** PRACTICE tags: the F4 tracking factor 3 and the F1 monotonicity
  slack 1e-12 declared PRACTICE (one line each) in the campaign log. Owner: S24
  carrier/log. [E3 R5]

## Non-blocking residuals noted (per the positions' own words; NOT conditions)

- Crossing-count logging at bucket build (E3: "Cheap add, not blocking"; F6 census
  covers multiplicity; single crossing measured at this instance).
- Per-rung shape-adaptation counters: global counters printed per rung — E3:
  "adequate, keep" (0 events measured at derive).
- TR-SQP chatter near KS ties at rho = 5.75e4: "a budget risk inside the [P4]
  cap, not an unsoundness" (E3) — monitor wall time per rung against the anchor.
- Reflected-family (C-) folds invisible to any C+ val monitor: registered UNPROVEN
  scope limit owned by F3 entry — "No regression introduced" (Refuter R6(e)).

## THE DECISION LINE

**campaign GO** — conditioned on C3/C4/C5/C6/C10 landed in the carrier with derive
re-run PASS before the decisive run, and C1/C2/C7/C8/C9 landed as same-session
declarations/registrations (C1 and C7 before any F1-F7 verdict becomes of record).
No re-adjudication of the bucket definition is required or licensed by any
position.

## Red-team compliance note

No manufactured unanimity: E1 = CONFIRM (scope: classical fidelity); E2, E3,
Refuter = REPAIR(named); the panel verdict is the conjunction (GO conditioned on
the named repairs). Judge-added items, labeled as such: the DR-2 and DR-6 source
checks (main() dispatch; rung-record contents), the C3 merge, the C7 conditional
discharge placement, and the pre-run vs record placement split of the condition
list. Every other claim above is carried by at least one position file, with the
verdict-moving ones quoted verbatim. No classical-optimality wording anywhere in
this advisory (O3 hard gate; CLAIM CAP of record honored — F7 wording stays "the
direct-side surplus prediction fails on this instance" if it fires).
