# PHASE D MINOR (b) — [OBJ-DOM] OBJECTIVE-DOMAIN ADJUDICATION
# S-FOUNDATIONS-C4, Blocco 1 (Phase D remainder), 2026-08-20.
# AUTHOR slot per BRIEF_blocco2_phaseD.md MINORS (b). One refuter
# round + auto-escalation applies. This file is the ONLY file this
# slot writes.
#
# [ESC-r1-0] ESCALATED AUTHOR-REVISION round 1 (2026-08-20), per
# VERDICT_blocco2.md SS2.2 + E-2 (8/8 findings SUSTAINED, 3 CONTENT
# => full form; escalation mandate = BRIEF_blocco2_phaseD_addendum_c4
# .md). Revisions applied IN PLACE with markers [ESC-r1-<n>];
# disposition table appended at EOF. The OBJDOM-4 adjudication
# DIRECTION (fix-A of record at F2 entry; fix-B scoping interim) is
# UNCHANGED: verified GROUNDED by the refuter, overturned by no
# sustained finding (VERDICT SS2.2).
#
# [ESC-r2-0] ESCALATED AUTHOR-REVISION round 2 (2026-08-20), per
# esc_refute_objdom_r1.md (1 BREAK + 1 REPAIR + 1 AMENDMENT + 1
# VERIFIED-SOUND NOTE). All three actionable findings verified in
# THIS window before adoption (probe re-run exit 0, 4/4 rejectors
# PASS; E_trunc expansion re-derived symbolically; registry state
# re-measured per SR-12) and FIXED — none contested. Markers
# [ESC-r2-<n>]; round-2 disposition table appended at EOF (SS7).
# Probe of record: esc_probe_objdom_etrunc_order.py (refuter's,
# numpy-only, pinned env; re-run this window, exit 0). The OBJDOM-4
# adjudication DIRECTION, F-2, OBJDOM-2/3, and all record magnitudes
# remain UNCHANGED (per the refuter's own scope declarations).
#
# [ESC-r3-0] ESCALATED AUTHOR-REVISION round 3 (2026-08-20), per
# esc_refute_objdom_r2.md (1 BREAK + 1 VERIFIED-SOUND NOTE). The
# single actionable finding ESC-OBJDOM-r2-1 (the [ESC-r2-1] IFF
# clause false in the sufficiency direction) verified in THIS
# window before adoption: BOTH probes re-run exit 0 (4/4 rejectors
# each: esc_probe_objdom_etrunc_order.py, esc_probe_objdom_evenp_iff
# .py — the latter the r2 refuter's counterexample probe) AND the
# p3*th^3 expansion independently re-derived (E_trunc =
# (pi/10)*rtd*p3*yt*th1^5, coefficient matches). FIXED at all three
# anchor sites with the refuter's named one-clause repair, markers
# [ESC-r3-1]; round-3 disposition table appended at EOF (SS8).
# Nothing else touched: the generic O(th1^3) statement and its
# coefficient, (a.1)/(b)/(c), F-1's three branches, F-2, OBJDOM-2/
# 3/4, the adjudication DIRECTION, and all record magnitudes are
# UNCHANGED (the broken branch is consumed nowhere of record —
# conclusion-preserving per the refuter's own scope note).

## 0. Task spec and inputs of record (cited, not re-litigated)

Registry row: `variational-driver:objective-omits-throat-panel`
(docs/findings_registry.yaml:204-213, read [FULL]). Authorities
consumed (per the row's `source` and the audit chain, read [FULL] at
the cited ranges):

- ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md §1 (:50-158)
  — THE MERGED SLIVER ROW: settled identity, folded refuter
  precisions (i)-(v), magnitude table, verdict wording of record
  ("gradient axis governs"), [OBJ-DOM] owner/trigger definition.
- AUDIT_agnostic_2026-08-07.md :507-519 (the CONFIRMED finding +
  verifier note) and :533 (Dv-spread <= ~6 cross-unit caveat).
- Code, current tree (line numbers re-verified in THIS window,
  drifted from the audit's): objective declaration
  validation/a1_toc_variational_jax.py:22-27; arc stations loop
  :530-534 (`for k in range(1, n_B + 1): th = thB * k / n_B` — no
  theta=0 station); `thrust_J` :1179-1186 (trapezoids only supplied
  wall points). The registry row's `code` anchors (:516-522,
  :1130-1137) are DRIFTED relative to these facts; the row anchors
  should be refreshed at the landing (bookkeeping, noted for the
  judge).

The object of record (cited verbatim from the advisory §1, NOT
re-derived here; its own class there is adopted-verbatim
mathematical statement of the row):

    DJ_sliver(thB) = 2*pi * Int_0^{thB/n_B} p(th)*y(th)*rtd*sin(th) dth,
    p = kernel/fan flow on the fixed arc (W-independent),
    y(th) = yt + rtd*(1 - cos th);
    d(DJ_sliver)/dthB = 2*pi*p(th1)*y(th1)*rtd*sin(th1)/n_B > 0,
    deterministic and sign-definite within a frozen plan;
    piecewise-smooth with O(da^3) jumps across plan re-records.

Recorded magnitudes (of record, advisory §1.3, cited): gradient row
5.36e3 J-units/rad vs O3 acceptance 10*gtol ~= 9.3 (S20 instance) =
5.8e2x; worst-case Dv-coordinate spread <= ~6 (audit :533) leaves
>= ~1e2x. Value axis 1.0767e-4*p_t = O(da^2), Richardson-scoped,
F7-cancelling => no recorded verdict moves (advisory §1 folded
precisions (i)-(ii); consumed as-is).

---

## 1. Statements

### OBJDOM-1 [THEOREM] — Panel-term identity and exactness class

Statement. Let the design arc be the circle of radius rtd centered
at (0, yt + rtd), with stations th_k = thB*k/n_B, k = 1..n_B (n_B
frozen per record). Define the throat panel term

    DJ_panel(thB) = 2*pi * Int_0^{th1} p(th)*y(th)*rtd*sin(th) dth,
    th1 = thB/n_B,  y(th) = yt + rtd*(1 - cos th),

with p(th) the frozen-plan kernel/fan arc flow. Then:
(a) [ESC-r1-1: restated per MIN-OBJDOM-1 (SUSTAINED) — the prior
    "exactly" bound a discrete trapezoid sum to a continuum
    integral; repair verified by re-derivation in this window]
    DEFINITION (fix-A functional, = protocol P-1's object):
    J_A := J_coded + DJ_panel, with J_coded the implemented
    trapezoid `thrust_J` over [th1, L] and DJ_panel the exact
    integral displayed above. Two identities, objects pinned:
    (a.1) DISCRETE, exact: the header objective over "(0, theta_B]"
    (:22-24) evaluated by the same trapezoid rule extended with the
    theta=0 station satisfies, by discrete additivity of the sum
    over the extended station partition,
        J_declared^trap = J_coded + DJ_panel^trap,
        DJ_panel^trap = 2*pi * 0.5*(p(0)*y(0) + p(th1)*y(th1))
                        * (y(th1) - y(0)),   y(0) = yt
    (the refuter's identity, 2*pi factor restored);
    (a.2) [ESC-r2-1: order RESTATED per ESC-OBJDOM-r1-1 (BREAK,
    probe-demonstrated; probe re-run + expansion re-derived
    symbolically in this window before adoption). The prior claim
    "O((Dy)^3) ... hence O(th1^6)-class" was FALSE generically: the
    standard single-interval trapezoid bound needs f = p*y to be
    C^2 in y ON THE PANEL, but dy/dth = rtd*sin(th) vanishes at
    th = 0, so th(y) ~ sqrt(2(y-yt)/rtd) and p(y) has a
    SQUARE-ROOT CUSP at the throat whenever p'(0) != 0 — the
    GENERIC case for accelerating transonic wall flow — and the
    cited bound is vacuous there.]
    DJ_panel^trap = DJ_panel + E_trunc, with
        E_trunc = -(pi/6)*rtd*p'(0)*yt*th1^3 + O(th1^4)  (generic),
    i.e. O(th1^3) absolute — O((Dy)^{3/2})-class in the y variable
    (sqrt-cusp bound), NOT O((Dy)^3). [ESC-r3-1: IFF clause
    RESTATED per ESC-OBJDOM-r2-1 (BREAK, probe-demonstrated;
    verified this window: both probes re-run exit 0, and the
    p3*th^3 expansion independently re-derived — trap p3*yt*rtd
    *th1^5/4 vs integral /5, difference x2*pi = (pi/10)*rtd*p3*yt
    *th1^5. The prior clause "recovered IFF p'(0) = 0 (p even in
    th at the throat)" was FALSE in the sufficiency direction: odd
    Taylor terms of p contribute independently (E_trunc linear in
    p), and p'''(0)*th^3/6 maps to a (y-yt)^{3/2} half-power whose
    single-interval trapezoid error is O(Dy^{5/2}) = O(th1^5).]
    The O((Dy)^3) = O(th1^6) class is recovered IFF p'(0) = 0 AND
    p'''(0) = 0 (p even in th through cubic order; full evenness
    sufficient but stronger than necessary — odd th^5 terms map to
    (y-yt)^{5/2}, trapezoid error O(Dy^{7/2}) = O(th1^7), below
    the th1^6 threshold); with p'(0) = 0 alone and p'''(0) != 0
    the order is O(th1^5) (Dy^{5/2} cusp: E_trunc =
    (pi/10)*rtd*(p'''(0)/6)*yt*th1^5 + h.o.t.). Declared EXTRA
    hypothesis, not generic (probe controls, this window: cubic
    p'(0)=0 slope 5.007, coefficient ratio -> 1.0007; even-p slope
    5.999; generic slope 3.0000, coefficient ratio 1.0000).
    E_trunc is generically NONZERO, numerically tiny at the record
    scale (sub-J-unit SCALING-ESTIMATE class — illustration only,
    magnitude of record = F2-measured), DECLARED, never called
    exact;
(b) DJ_panel is W-independent EXCEPT through the single DOF thB
    (the arc geometry and the arc flow are plan-frozen; the
    advisory's fix-A wording "makes the omitted area W-independent
    exactly" [ESC-r1-4: attribution corrected per MIN-OBJDOM-4 —
    the phrase is ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12
    .md SS1.4 :151, NOT the audit's; audit :507-519 carries only
    the suggested test :517] is the theta=0-anchor half of this
    statement);
(c) d(DJ_panel)/dthB = 2*pi*p(th1)*y(th1)*rtd*sin(th1)/n_B, the
    sliver derivative of record.

Hypotheses (strong, trivially checkable — AG-1 valve NOT invoked
here, this statement is load-bearing for the adjudication): frozen
plan (n_B, station topology fixed per record); p on the fixed arc
W-independent within the frozen plan (advisory §1 premise of
record); exact circular-arc geometry (code :531-534).

Proof sketch: (a.1) is additivity of the trapezoid SUM over the
extended station partition with matching endpoint station; (a.2)
is the direct th-expansion of trapezoid-minus-integral (leading
term -(pi/6)*rtd*p'(0)*yt*th1^3; equivalently the O((Dy)^{3/2})
cusp bound in the y variable — the standard O((Dy)^3) trapezoid
bound is INAPPLICABLE generically, f''(y) unbounded on the panel)
[ESC-r1-1][ESC-r2-1]; (b) all quantities in the integrand depend on W only
via thB under the hypotheses; (c) is the Leibniz rule at the upper
limit, identical to the advisory formula.

Falsifier (measured half = F2 duty, §3): in the A/B protocol of §2,
the measured |dJ_A/dthB - dJ_B/dthB| at the recorded W* must equal
the BRANCH-MATCHED analytic prediction of the repaired F-1
[ESC-r1-2][ESC-r2-2: the branch set is indexed by the declared
PANEL QUADRATURE RULE of P-1 (not only the p-sampling rule): every
implementable panel is a quadrature and AD returns the derivative
of the implemented quadrature, so the prediction must be the exact
derivative OF THAT RULE — see F-1 branches (i)-(iii)] within derived
AD/FD bars; a deviation beyond bars falsifies OBJDOM-1 (hidden
W-dependence of the arc flow or a geometry error) and re-opens the
adjudication.

### OBJDOM-2 [THEOREM*] — Fix-B's tolerance-absorption branch is dead at recorded magnitudes

Statement. At the S20 instance constants of record, fix-B's clause
"bound the argmax tilt into the derived KKT tolerance" requires
inflating the acceptance by a factor >= ~1e2: tilt/acceptance =
5.36e3 / 9.3 = 5.8e2, and the maximal Dv-coordinate discount of
record (<= ~6, audit :533) leaves >= 96x. Any gtol inflation of
that size contradicts the derived-tolerance discipline of record
(gtol = max(tol_dp, 1e-8*gscale), derivation adjudicated at audit
:533 REFUTED-component; R5: tolerances derived, not magic).
Therefore fix-B survives ONLY as its scoping clause (declare coded
J + scope value/gradient/Pa statements), never as an absorption.

Class THEOREM* because the inputs are measured record numbers
(5.36e3, 9.3, <=6), the inference is one division. Hypotheses
[ESC-r1-7: label aligned per MIN-OBJDOM-7 — this statement carries
OBJDOM-4 ground 1, hence LOAD-BEARING; AG-1 valve NOT invoked
(matching OBJDOM-1's treatment); the prior gap-accounting label is
retracted. The hypotheses remain strong and trivially checkable,
and each is separately covered by the two-sided F-2 falsifier]:
the S20 instance is the governing
instance for the O3 acceptance; the Dv spread bound <= 6 holds.
Falsifier: a future recorded instance with tilt/acceptance <= 1
after the Dv discount (the A/B protocol measures exactly this
ratio; see §2 assert (F-2)).

### OBJDOM-3 [THEOREM] — Pa-anchor: fix-A restores the declared drop; fix-B leaves it false-in-general

Statement. On the feasible set (lip height fixed by the equality
constraint of record; eps and L constrained per the header :25-27):
(a) under fix-A (integral anchored at theta=0), the ambient term
    Pa*(A_lip - A_0) has A_0 = throat area, a plan constant, and
    A_lip fixed by the lip constraint => the term is constant on
    the feasible set and Pa drops out of the argmax — the header's
    declared claim becomes true as stated;
(b) under fix-B (domain [th1, thB] declared of record), the anchor
    A(th1) = pi*y(th1)^2 varies with the DOF thB, so for any
    Pa != 0 the ambient term is NOT constant on the feasible set
    and the Pa-drop declaration is false; the current code is saved
    only by the vacuum objective (no Pa term exists anywhere —
    audit verifier note :519, advisory folded precision (iv),
    both cited as inputs).

Hypotheses: frozen n_B; feasible set as declared (:25-27); exact
arc geometry. Proof sketch: (a) constancy of both areas on the
feasible set; (b) dA(th1)/dthB = 2*pi*y(th1)*rtd*sin(th1)/n_B > 0
by the same Leibniz step as OBJDOM-1(c).

Falsifier: exhibit a feasible-set parametrization of record under
which A(th1) is constant while thB varies (none exists under the
frozen-n_B record; a change of the n_B freezing rule would be the
attacking move and must be declared as a plan change).

### OBJDOM-4 [PRACTICE] — THE ADJUDICATION (decision proposed of record; judge adjudicates)

**Fix-A is adopted as the objective-of-record at F2 entry; fix-B's
scoping clause is adopted as the INTERIM regime until fix-A's
implementation lands.** Grounds, in governing order:

1. GRADIENT AXIS GOVERNS (the brief's binding axis; advisory §1.3
   verdict wording of record): the finding is a stationarity-tilt
   claim; by OBJDOM-2 the tilt cannot be tolerated into the
   derived KKT band, so fix-B cannot discharge the gradient-axis
   defect — it can only rename it. Fix-A eliminates it identically
   (J_A's domain matches the declaration; AD then gives the exact
   gradient of the DECLARED functional — the clean
   discretize-then-optimize property of record now holds for the
   functional the docs claim).
2. Pa/anchor axis: by OBJDOM-3, fix-B leaves a declaration that is
   false for every non-vacuum ambient; fix-A makes it a theorem.
   F2 re-derives the objective for the stratified class anyway
   (advisory §1.4) — entering that derivation with a
   false-in-general anchor clause is a defect multiplier.
3. Cost asymmetry (gap-accounting, AG-1 valve applies —
   sufficient-not-optimized): fix-A's cost is one analytic,
   plan-frozen term (OBJDOM-1) plus a ONE-TIME re-baseline of
   recorded J values whose delta is the value-axis figure of
   record (1.0767e-4*p_t at the S20 instance), already adjudicated
   verdict-neutral (O(da^2), Richardson-scoped, F7-cancelling —
   advisory precisions (i)-(ii), cited). Fix-B's cost is a
   PERPETUAL scoping duty over value AND gradient AND Pa
   statements (precision (v): scoping only the value leaves the
   gradient dangling), re-owed at every future doc touch.
4. The interim regime is fix-B's scoping clause, all three axes,
   because the coded carrier stays internally consistent (AD =
   exact gradient of implemented J) and no recorded verdict moves
   today: until the F2 implementation lands, M0/doc statements
   referencing the design-wall pressure-thrust integral are scoped
   to domain [theta_1, theta_B], gradient statements to the coded
   J, and the Pa-drop claim carries the vacuum-objective proviso.

Falsifier for the adjudication as a decision: A/B assert (F-2) of
§2 — if the measured tilt at W* lands BELOW gtol after the Dv
discount, fix-B's absorption branch was viable and grounds 1
collapses; the adjudication re-opens (registry row reverts to
OPEN, judge notified). This is the two-sided rejector: the same
run can kill OBJDOM-1 (formula), OBJDOM-2 (magnitude), or the
decision itself.

### OBJDOM-5 [SCHEMA] — Sequencing consequence for minor (c) DELTA-CARRIER (binding composition note)

[ESC-r1-3: REWRITTEN per MIN-OBJDOM-3 (SUSTAINED) and the judge's
sequencing verdict (VERDICT_blocco2 §4(1)-(3)); the (H6') form
below is the judge-ratified repair, adopted after verification.
RETRACTED claim: "the panel term is common to both sides of the
distance at fixed thB-convention, so it cancels in delta IF both
sides use the same domain convention". That was WRONG: the two
sides of delta are evaluated on DIFFERENT walls (the ideal-march
ceiling contour and the TOC design wall), with thB_ideal !=
thB_TOC in general and th1 = thB/n_B further split by the
ceil-seam n_B = ceil(thB/da) (the advisory §1 O(da^3) jump seam),
so a shared domain convention does NOT make the panel term common:
the net contamination of delta is DJ_panel(ideal wall) -
DJ_panel(TOC wall), a difference of two O(da^2)-class values
cancelling only to leading order (shared throat-arc geometry via
the Sauer/IVL contract) — and the ceiling-side omission is the
ANTI-CONSERVATIVE direction (advisory §3.2 item 3: an
under-estimated ceiling is anti-conservative for delta).]

The delta-carrier ceiling evaluation inherits the same omission
(advisory §1.4 trigger clause: "the ceiling evaluation inherits the
same omission — §3.2(iv)"; row pipeline:delta-carrier-F2-entry
trigger "sequenced with/after [OBJ-DOM]"). Under this adjudication
the (c) relaxation lemma's REQUIRED hypothesis form is (H6'), two
branches, and the lemma must say WHICH branch it runs under — a
lemma silent on the domain, or declaring only a same-convention
clause, is non-compliant with this verdict [ESC-r1-3]:
  (H6'-A) the fix-A panel-inclusive functional is used on BOTH
    sides of delta ([OBJ-DOM-IMPL] landed and used on both sides);
    OR
  (H6'-B) both sides use the coded (panel-omitting) functional AND
    an EXPLICIT net-two-wall-panel band on |DJ_panel(ideal) -
    DJ_panel(TOC)| is included, with its anti-conservative sign
    declared, folded into the DC-5(a) upper-edge rule.
Ship-gate, re-pinned per the row-:300 "banded or repaired" license
correctly read (VERDICT_blocco2 §4(2)): no (value, delta) row
ships unless "[OBJ-DOM-IMPL] landed and used on both sides, OR the
net-panel band included". Class SCHEMA: composition statement,
proof obligation transferred to (c)'s lemma hypotheses ((H6') as
above).

---

## 2. Discharge protocol PINNED (the audit's analytic throat-panel A/B, protocol of record)

All steps below are MEASURED halves = F2 duty (named §3). Nothing
here is executed in this window (R5: no new number without a
committed carrier; every number quoted above is a record number
with its source cited).

- (P-1) Implement J_A = J_coded + DJ_panel(thB) with the declared
  panel rule (analytic-integral target) of OBJDOM-1 [ESC-r2-2:
  wording repaired per ESC-OBJDOM-r1-2 — "with the analytic panel"
  was unimplementable literally: p(th) is the numerical kernel/fan
  flow with no closed form, so every kernel-sampled implementation
  is a QUADRATURE]. The F2 carrier MUST declare BOTH:
  (1) the panel-pressure rule (p(th) sampling on [0, th1]: kernel
  arc-flow evaluation vs p(th1) frozen-endpoint approximation) —
  if the endpoint approximation is used, its error term is O(th1)
  relative on a panel already O(th1^2) absolute — declare the
  resulting order and its bar; AND
  (2) [ESC-r2-2] the PANEL QUADRATURE RULE actually implemented
  (theta=0-station trapezoid / closed-form endpoint / declared
  m-node composite in th), since F-1's prediction is
  branch-matched to it.
- (P-2) At the recorded W* (S20 instance of record), evaluate
  dJ/dthB under BOTH functionals through the engine's AD path,
  same engine key, same frozen plan (no re-record between A and B).
- (F-1) PRIMARY ASSERT (falsifies OBJDOM-1) [ESC-r1-2: repaired
  per MIN-OBJDOM-2 (SUSTAINED) — as previously pinned the assert
  could fire SPURIOUSLY in P-1's permitted endpoint branch]
  [ESC-r2-2: repair COMPLETED per ESC-OBJDOM-r1-2 — the round-1
  form still admitted a spurious fire in the KERNEL branch: its
  "no extra term" prediction (c) is exact only for the exact
  integral, which no kernel-sampled implementation computes; AD
  returns the derivative of the implemented QUADRATURE, differing
  from (c) by the quadrature-error derivative (probe rejector [3]:
  relative O(th1), measured slope 1.001, leading coefficient
  (p'/4p)*th1 — J-units/rad-scale at the record constants,
  SCALING-ESTIMATE ~3.5 J-units/rad at p'/p = 0.3/rad,
  illustration only — orders above any AD/FD-noise-class bar).
  F-1 is now BRANCH-MATCHED to the PANEL QUADRATURE RULE P-1(2)
  declares, three branches]:
  the measured AD difference is compared against the exact analytic
  derivative OF THE IMPLEMENTED panel quadrature rule —
  - (i) theta=0-station single-interval trapezoid rule (the
    advisory's fix-A station form, :150-151; kernel-sampled):
    prediction = exact d(DJ_panel^trap)/dthB, closed form in p(0),
    p(th1), p'(th1) (all available via the declared AD path):
    2*pi*[0.5*(p'(th1)*y(th1) + p(th1)*rtd*sin(th1))*(y(th1)-yt)
          + 0.5*(p(0)*yt + p(th1)*y(th1))*rtd*sin(th1)]/n_B
    (re-derived this window: d/dthB = (1/n_B)*d/dth1, product +
    Leibniz on the trapezoid form; p(0) plan-frozen at the fixed
    th = 0 station);
  - (ii) closed-form endpoint rule DJ~ = 2*pi*p(th1)*G(th1) with
    G(th1) = Int_0^{th1} y(th)*rtd*sin(th) dth: prediction =
    2*pi*[p(th1)*y(th1)*rtd*sin(th1) + p'(th1)*G(th1)]/n_B.
    The p'(th1)*G(th1)/n_B term is a MODELING term of the rule
    (relative order O(th1), (p'/p)*th1/2-class), part of the
    PREDICTION and never of the noise bar: it is orders above any
    AD/FD bar and must not be absorbed into the bar silently;
    p'(th1) = the arc-flow derivative along the arc, evaluated by
    the same AD path and declared in the F2 carrier. (This panel
    IS closed-form — G(th1) analytic — so AD matches this branch
    prediction exactly up to AD/FD noise.)
  - (iii) declared m-node composite rule in th: prediction = (c) +
    the rule's own quadrature-derivative term, either carried
    explicitly or bounded by a DERIVED bar shown below the AD/FD
    bar (declared, never silent).
  Assert: |measured difference - branch prediction| <= derived
  AD/FD bar (bar derivation = the O3.1 machinery of record, not a
  new constant; prediction (c) with no extra term is the EXACT-
  INTEGRAL TARGET, attained by no implemented branch — every
  branch prediction above reduces to (c) + that branch's declared
  quadrature-derivative term [ESC-r2-2]).
- (F-2) ADJUDICATION ASSERT (falsifies OBJDOM-2/OBJDOM-4 ground
  1): |dJ_A/dthB - dJ_B/dthB| > 10*gtol at W* after the Dv
  discount — EXPECTED TO FIRE per the record (5.8e2x). If it does
  NOT fire, the absorption branch was viable: adjudication
  re-opens (declared outcome, not a silent pass).
  [ESC-r1-8: Dv discount PINNED to an executable operation per
  MIN-OBJDOM-8. PRIMARY: convert the physical thB tilt row into
  scipy's u-coordinates by MULTIPLYING by the run's recorded
  Dv_thB coordinate scale — the recorded convention is x0 = W/Dv,
  jac = g*Dv (audit :529), hence dJ/du = dJ/dW * Dv_thB
  (multiplication; this corrects the refuter's "divide" phrasing
  against the recorded convention, verified this window) — then
  compare against 10*gtol. FALLBACK, iff the recorded Dv vector at
  W* is not retrievable: require tilt_phys/(10*gtol) > 6, i.e.
  discount the ratio by the worst-case Dv-spread bound 6 (audit
  :533, conservative) — the operation that produced the >= 96x
  record figure. The F2 carrier states which path executed.]
  [ESC-r1-6: declared delta from the audit's literal test per
  MIN-OBJDOM-6: audit :517 suggests asserting "< gtol at W*"
  (pass = tilt small); this protocol instead uses the O3
  acceptance comparator 10*gtol (advisory §1.3, the acceptance of
  record) with INVERTED expected-to-fire semantics (the tilt IS
  the finding). Deliberate, declared departure so the F2 executor
  faces ONE assert of record, not two nominally "of-record"
  asserts with different constants; no conclusion moves — 5.36e3
  exceeds either threshold by >= 5.7e2x / 5.8e2x.]
- (P-3) Re-run the OPT stage under J_A: the new W*_A must pass
  transversality at UNCHANGED derived gtol (no tolerance touched —
  that is the point of fix-A).
- (P-4) Re-baseline check (value axis): the recorded-J shift must
  equal DJ_panel(thB*) within Richardson bars, and the F7 band
  must be re-measured to confirm the cancellation prediction
  (advisory precision (ii)) survives the fix — a moved F7 verdict
  here would falsify the "verdict-neutral re-baseline" ground 3.

---

## 3. F2 DUTIES NAMED (measured halves; owner = F2 entry; trigger = registry row :212, character-exact quote [ESC-r1-5, per MIN-OBJDOM-5 — prior "verbatim" flag carried an advisory-phrasing prefix and is retracted]: "first F2 verdict consuming dJ/dthB AND before the R2 delta-carrier ships; discharge test = the audit's analytic throat-panel A/B")

- [OBJ-DOM-IMPL] fix-A implementation: analytic panel term +
  declared panel-pressure rule in a1_toc_variational_jax.py
  (stations/`thrust_J`), engine-key impact declared.
- [OBJ-DOM-AB] execute P-1..P-4 / F-1..F-2 with derived bars;
  registry row `variational-driver:objective-omits-throat-panel`
  updated (status per outcome; code anchors refreshed — current
  drifted anchors noted in §0).
- [OBJ-DOM-REBASE] one-time re-baseline table of recorded J values
  + F7 re-measure (P-4).
- INTERIM (doc landing, NOT F2 — orchestrator lands with the
  judge's verdict): the fix-B scoping clause on M0/doc value +
  gradient + Pa statements (all three axes, precision (v)),
  wording proposed §4.

## 4. Proposed landing text (for the judge's landing list, verbatim-ready)

M0 site (objective declaration vicinity): "OBJECTIVE DOMAIN
[OBJ-DOM adjudicated, Phase D 2026-08-20]: the functional of
record at F2 entry is the panel-inclusive J_A (domain [0,theta_B]
+ contour; fix-A). Until [OBJ-DOM-IMPL] lands, the executed
carrier computes the coded J on [theta_1, theta_B] + contour:
value, gradient, and Pa-drop statements about the carrier are
scoped to that domain, and the Pa-drop claim holds under the
vacuum objective only. Discharge = analytic throat-panel A/B
(F2 duty [OBJ-DOM-AB]); tilt of record 5.36e3 J-units/rad vs
acceptance 9.3 (advisory §1.3)."
Registry: owner field of row :204-213 gains "ADJUDICATED fix-A
(Phase D minor b), interim = fix-B scoping; duties
[OBJ-DOM-IMPL]/[OBJ-DOM-AB]/[OBJ-DOM-REBASE]"; code anchors
refreshed to :530-534, :1179-1186.

[ESC-r1-9] STATUS NOTE (escalation round 1): per VERDICT_blocco2
§2.2 ("NOT ADOPTED THIS WINDOW"), the landing text above did NOT
land at the judge window and remains PROPOSED; it lands only with
the escalation closure judge's verdict, and the interim fix-B
scoping regime lands with it (no doc statement changes before
then). Its content is compatible with this revision as-is: it
contains no OBJDOM-5 composition instruction (the refuted
instruction lived in §1 and is rewritten at [ESC-r1-3]). The
registry text above additionally carries the sequencing gate of
VERDICT_blocco2 §4(3) verbatim-by-reference: the escalated minor
(c) runs with/after the escalated minor (b); no (value, delta) row
ships before BOTH close and the (H6') branch is satisfied.
[ESC-r2-3: SR-12 repair per ESC-OBJDOM-r1-3 — the prior sentence
("Bookkeeping already landed...") was FALSE and carried no
in-window measurement.] Bookkeeping ORDERED at the judge window
per E-2/LB-6 (code anchor refresh; execution = orchestrator
landing, NOT yet applied as measured in THIS window 2026-08-20:
docs/findings_registry.yaml:209 read this window still carries the
drifted anchors :516-522 / :1130-1137, and the note field :213
carries no LB-6(b) append). Consistent with §0: the row anchors
are to be refreshed at the landing.

## 5. Read-depth declaration + PAPERS NEEDED

Papers consulted: NONE — the item is an internal adjudication over
record artifacts; no external literature bears on it (checked the
brief's arrivals list for bearing: optimization/adjoint corpus
addresses tolerance/adjoint derivations owned by minors (a)/(d),
not the objective-domain decision).
Internal reads, all [FULL] at the stated ranges:
docs/findings_registry.yaml:190-239;
validation/ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md:40-199;
validation/AUDIT_agnostic_2026-08-07.md:500-544;
validation/a1_toc_variational_jax.py:18-47, :500-549, :1110-1160,
:1179-1192; BRIEF_blocco2_phaseD.md (whole file).

PAPERS NEEDED: (empty)

---

## 6. [ESC-r1] DISPOSITION TABLE (escalation round 1, 2026-08-20 — every sustained finding of refute_minor_objdom.md / VERDICT_blocco2 §2.2)

| Finding | Class | Disposition | Marker | What was done |
|---|---|---|---|---|
| MIN-OBJDOM-1 | CONTENT | REPAIRED | [ESC-r1-1] | OBJDOM-1(a) restated: J_A := J_coded + DJ_panel is now a DEFINITION (the P-1 object); the exact identity is the DISCRETE (a.1) J_declared^trap = J_coded + DJ_panel^trap (trapezoid panel term, 2*pi factor restored to the refuter's identity, y(0)=yt); the integral-vs-trapezoid discrepancy declared as (a.2) O((Dy)^3) = O(th1^6)-class, generically nonzero. Proof sketch re-pointed to sum-additivity + truncation bound. Repair verified by re-derivation before adoption. [ESC-r2-1 CORRECTION: the (a.2) order stated in this row was itself FALSE generically (ESC-OBJDOM-r1-1 BREAK, probe-demonstrated): sqrt cusp of p(y) at the throat makes the standard bound vacuous; true generic order E_trunc = -(pi/6)*rtd*p'(0)*yt*th1^3 + O(th1^4) = O(th1^3); O(th1^6) iff p'(0)=0 AND p'''(0)=0 [ESC-r3-1: this echo's prior "iff p'(0)=0" was false in sufficiency (ESC-OBJDOM-r2-1); with p'(0)=0 alone and p'''(0)!=0 the order is O(th1^5)] (declared extra hypothesis). Restated in place at (a.2) + proof sketch.] |
| MIN-OBJDOM-2 | CONTENT | REPAIRED | [ESC-r1-2] | F-1 branch-matched to P-1's declared panel-pressure rule: kernel rule => prediction (c); endpoint rule => prediction gains the modeling term 2*pi*p'(th1)*G(th1)/n_B (verified: Leibniz + product rule; relative order O(th1)), carried in the PREDICTION, never absorbed into the AD/FD bar. OBJDOM-1's falsifier sentence updated to reference the branch-matched assert. Spurious-fire branch closed. [ESC-r2-2 CORRECTION: "closed" OVERREACHED (ESC-OBJDOM-r1-2 REPAIR): the KERNEL branch could still fire spuriously — its "no extra term" prediction holds only for the exact integral, unimplementable; any kernel-sampled panel is a quadrature and AD carries its quadrature-derivative term (probe rejector [3]: relative O(th1)). NOW closed by the three-branch F-1 (station-trapezoid / closed-form endpoint / declared composite) + P-1(2) panel-quadrature-rule declaration duty.] |
| MIN-OBJDOM-3 | CONTENT | REPAIRED | [ESC-r1-3] | OBJDOM-5 rewritten: same-convention cancellation claim RETRACTED (different walls, thB_ideal != thB_TOC, ceil-seam; net contamination = DJ_panel(ideal)-DJ_panel(TOC), leading-order-only cancellation, anti-conservative direction declared); required hypothesis form = judge-ratified (H6') two-branch (fix-A both sides OR both-coded + net-panel band folded into DC-5(a)); ship-gate re-pinned to the row-:300 "banded or repaired" license. Binding instruction to minor (c) now consistent with VERDICT §4(2). |
| MIN-OBJDOM-4 | WORDING | REPAIRED | [ESC-r1-4] | Attribution corrected in OBJDOM-1(b): the fix-A phrase is the advisory's (§1.4 :151), not the audit's. |
| MIN-OBJDOM-5 | WORDING | REPAIRED | [ESC-r1-5] | §3 trigger re-quoted character-exact from findings_registry.yaml:212 (verified this window); the non-verbatim "before the" prefix dropped with the retraction noted. |
| MIN-OBJDOM-6 | NOTE | REPAIRED | [ESC-r1-6] | F-2 now declares the deliberate departure from the audit's literal ":517 < gtol" test (comparator 10*gtol of record + inverted expected-to-fire semantics); one assert of record for the F2 executor; no conclusion moves (>= 5.7e2x / 5.8e2x either threshold). |
| MIN-OBJDOM-7 | NOTE | REPAIRED | [ESC-r1-7] | OBJDOM-2 hypothesis label aligned to OBJDOM-1's: LOAD-BEARING (carries OBJDOM-4 ground 1), AG-1 valve NOT invoked; gap-accounting label retracted; F-2 coverage of each hypothesis stated. |
| MIN-OBJDOM-8 | NOTE | REPAIRED (with direction correction) | [ESC-r1-8] | F-2 Dv discount pinned executable: PRIMARY = multiply physical tilt row by recorded Dv_thB (x0=W/Dv, jac=g*Dv, audit :529 — the refuter's "divide" phrasing corrected against the recorded convention, verified this window); FALLBACK (Dv not retrievable) = discount ratio by worst-case spread 6 (audit :533), the >= 96x record operation; executed path declared in the F2 carrier. |

Unchanged by design (VERDICT §2.2 positive record): OBJDOM-1(b)/(c),
OBJDOM-2 arithmetic and THEOREM* class, OBJDOM-3 in full, the
OBJDOM-4 adjudication direction (fix-A of record at F2 entry, fix-B
scoping clause interim), §3 duty structure, §4 landing text content
(status note [ESC-r1-9] added: remains PROPOSED until the escalation
closure judge; sequencing gate of VERDICT §4(3) carried).
No new numbers of record introduced in this revision; every quoted
number is a record number with source cited (R5). No probe script
needed: all three content repairs are definitional/analytic and were
verified by symbol-level re-derivation in this window (the measured
halves remain F2 duties as named in §3).
[ESC-r2-1 CORRECTION to the sentence above: the round-1
"verified by re-derivation" claim was itself IN ERROR on (a.2)'s
order (the re-derivation applied an inapplicable C^2 bound); the
round-2 restatement is PROBE-BACKED (esc_probe_objdom_etrunc_order
.py, 4/4 rejectors PASS, exit 0, re-run in the round-2 window) in
addition to the corrected symbolic expansion.]

---

## 7. [ESC-r2] DISPOSITION TABLE (escalation round 2, 2026-08-20 — every finding of esc_refute_objdom_r1.md)

| r1 finding | Class | Disposition | Marker | What was done |
|---|---|---|---|---|
| ESC-OBJDOM-r1-1 | BREAK | FIXED | [ESC-r2-1] | Verified before adoption (probe re-run this window, exit 0, 4/4 rejectors PASS; expansion independently re-derived: trapezoid-in-y minus integral = -rtd*p'(0)*yt*th1^3/12 + O(th1^4), x2*pi = -(pi/6)*rtd*p'(0)*yt*th1^3 — matches the refuter). (a.2) restated: generic E_trunc = -(pi/6)*rtd*p'(0)*yt*th1^3 + O(th1^4) = O(th1^3) absolute = O((Dy)^{3/2})-class in y (sqrt cusp, dy/dth -> 0 at throat); O((Dy)^3)=O(th1^6) holds IFF p'(0)=0 AND p'''(0)=0 [ESC-r3-1: biconditional corrected per ESC-OBJDOM-r2-1 — p'(0)=0 alone gives O(th1^5)], carried as declared extra hypothesis. Proof sketch re-pointed from the (inapplicable) standard trapezoid bound to the direct th-expansion / cusp bound. Round-1 disposition row MIN-OBJDOM-1 and the round-1 "no probe needed" closing note corrected in place with [ESC-r2-1] markers. "Numerically tiny, DECLARED, never called exact" retained (survives per the refuter's own scope note); (a.1), (b), (c), OBJDOM-2/3/4, F-2 untouched. |
| ESC-OBJDOM-r1-2 | REPAIR | FIXED | [ESC-r2-2] | Named repair adopted in full, one structural clause: P-1's declaration duty extended from the p-sampling rule alone to BOTH (1) p-sampling AND (2) the PANEL QUADRATURE RULE; P-1 reworded "with the analytic panel" -> "with the declared panel rule (analytic-integral target)". F-1 branch-matched to P-1(2), three branches: (i) theta=0-station trapezoid (fix-A station form) with exact closed-form derivative in p(0), p(th1), p'(th1) (formula independently re-derived this window: (1/n_B)*d/dth1 by product+Leibniz — matches the refuter's); (ii) closed-form endpoint rule (round-1 prediction, airtight per refuter verification); (iii) declared m-node composite with explicit or derived-bar-bounded quadrature-derivative term, never silent. OBJDOM-1's falsifier sentence re-pointed to the quadrature-rule branch set. Round-1 disposition row MIN-OBJDOM-2 "Spurious-fire branch closed" corrected in place (overreach acknowledged). F-2 and OBJDOM-4 untouched. |
| ESC-OBJDOM-r1-3 | AMENDMENT | FIXED | [ESC-r2-3] | Re-measured in THIS window per SR-12 before adoption: docs/findings_registry.yaml:204-213 read — :209 still carries drifted anchors [":516-522", ":1130-1137"], :213 has no LB-6(b) append. The false "already landed" sentence in [ESC-r1-9] replaced with the ordered-not-yet-applied form (execution = orchestrator landing), measurement cited, now consistent with §0. No math affected. |
| ESC-OBJDOM-r1-4 | NOTE | ACKNOWLEDGED (no action owed) | — | Verified-sound coverage record of [ESC-r1-1(a.1)/2-endpoint/3/4/5/6/7/8] + OBJDOM-2/3/4 + empty PAPERS NEEDED. Nothing to fix; record noted with thanks; no statement moves. |

CONTESTED: none — all three actionable findings verified true in
this window at source/probe before adoption.
Unchanged by design (refuter's own scope declarations honored):
OBJDOM-1(a.1)/(b)/(c), OBJDOM-2 (arithmetic, class, magnitudes),
OBJDOM-3 in full, the OBJDOM-4 adjudication DIRECTION (fix-A of
record at F2 entry; fix-B scoping interim), F-2 (both paths as
pinned at [ESC-r1-8]), §3 duty structure, §4 landing text content
(still PROPOSED per [ESC-r1-9]). No new numbers of record; the two
J-unit figures quoted in [ESC-r2-2] are the refuter's
SCALING-ESTIMATE illustrations, labeled as such (R5). Probe of
record for this round: esc_probe_objdom_etrunc_order.py (refuter's;
numpy-only, pinned env, no installs; re-run this window, exit 0) —
no additional probe script needed, none written.
Read-depth (round 2, this window): esc_refute_objdom_r1.md [FULL];
phaseD_minor_objdom.md [FULL, pre-revision]; VERDICT_blocco2.md
:130-300 + E-2/§4 [targeted]; docs/findings_registry.yaml:200-217
[FULL]; probe source + execution [FULL]. PAPERS NEEDED: (empty).

---

## 8. [ESC-r3] DISPOSITION TABLE (escalation round 3, 2026-08-20 — every finding of esc_refute_objdom_r2.md)

| r2 finding | Class | Disposition | Marker | What was done |
|---|---|---|---|---|
| ESC-OBJDOM-r2-1 | BREAK | FIXED | [ESC-r3-1] | Verified before adoption in THIS window: (1) BOTH probes re-run, exit 0, 4/4 rejectors PASS each — esc_probe_objdom_evenp_iff.py (cubic p'(0)=0 slope 5.007 vs IFF-predicted 6; coefficient ratio E_trunc/[(pi/10)*rtd*p3*yt*th1^5] -> 1.0007; even-p control slope 5.999; generic control slope 3.0000) and esc_probe_objdom_etrunc_order.py (generic slope 3.0000, ratio 1.0000, rel-mismatch slope 1.001, endpoint/trap ratio -2); (2) expansion independently re-derived: p = p0 + p3*th^3 gives trap/(2pi) = p3*yt*rtd*th1^5/4 vs integral/(2pi) = p3*yt*rtd*th1^5/5 at leading order, E_trunc = 2pi*rtd*p3*yt*th1^5/20 = (pi/10)*rtd*p3*yt*th1^5 = O(th1^5) — coefficient matches the refuter's; odd th^5 terms map to (y-yt)^{5/2}, trapezoid error O(Dy^{7/2}) = O(th1^7), below the th1^6 threshold, so the true characterization is E_trunc = O(th1^6) <=> p'(0)=0 AND p'''(0)=0. The refuter's named one-clause repair adopted VERBATIM-in-substance at all three anchor sites: SS1 (a.2) clause restated ("IFF p'(0)=0 AND p'''(0)=0 (p even in th through cubic order; full evenness sufficient but stronger than necessary); with p'(0)=0 alone and p'''(0)!=0 the order is O(th1^5), E_trunc = (pi/10)*rtd*(p'''(0)/6)*yt*th1^5 + h.o.t."), probe-control figures updated to this window's; SS6 row MIN-OBJDOM-1 echo corrected; SS7 row ESC-OBJDOM-r1-1 echo corrected. The false parenthetical gloss equating p'(0)=0 with evenness REMOVED. Nothing else moves: generic O(th1^3) statement + coefficient, necessity of p'(0)=0, (a.1)/(b)/(c), F-1 (no branch consumes E_trunc's order), F-2, OBJDOM-2/3/4, adjudication DIRECTION, all record magnitudes — untouched (conclusion-preserving; the p'(0)=0 branch is a declared EXTRA hypothesis invoked nowhere of record). |
| ESC-OBJDOM-r2-2 | NOTE | ACKNOWLEDGED (no action owed) | — | Verified-sound coverage record (items 1-13: probe re-runnability, SR-12 reproduction, character-exact trigger quote, code anchors, both r2 corrections' governing halves, branch-coverage attack finding no uncovered combination, F-1 preamble, probe constants, attribution/Dv re-verifications, bookkeeping contracts, unchanged-by-design list). Nothing to fix; record noted; no statement moves. |

CONTESTED: none — the single actionable finding verified true at
probe AND by independent re-derivation in this window before
adoption.
Unchanged by design (refuter's own scope declarations honored):
the generic (a.2) order statement -(pi/6)*rtd*p'(0)*yt*th1^3 +
O(th1^4) and its O((Dy)^{3/2}) class label, OBJDOM-1(a.1)/(b)/(c),
OBJDOM-2 (arithmetic, class, magnitudes), OBJDOM-3 in full, the
OBJDOM-4 adjudication DIRECTION (fix-A of record at F2 entry;
fix-B scoping interim), F-1 three-branch form, F-2 (both paths as
pinned at [ESC-r1-8]), SS3 duty structure, SS4 landing text
content (still PROPOSED per [ESC-r1-9]). No new numbers of record:
the O(th1^5) coefficient (pi/10)*rtd*(p'''(0)/6)*yt is an analytic
identity probe-checked in-window, not a record magnitude; the
probe-control slopes quoted are this window's measured rejector
outputs (R5, SR-12). Probes of record for this round: BOTH re-run
this window, exit 0 (numpy-only, pinned env, no installs); no new
probe script needed, none written (the r2 refuter's
esc_probe_objdom_evenp_iff.py already carries the counterexample
with rejectors that can fire).
Read-depth (round 3, this window): esc_refute_objdom_r2.md [FULL];
phaseD_minor_objdom.md [FULL, pre-revision]; VERDICT_blocco2.md
SS2-4 [as mandated, prior-window read carried + SS2.2/E-2 anchors
re-consulted]; both probe sources [FULL] + both executed this
window (exit 0 each). PAPERS NEEDED: (empty).
