# PHASE D MINOR (b) — [OBJ-DOM] OBJECTIVE-DOMAIN ADJUDICATION
# S-FOUNDATIONS-C4, Blocco 1 (Phase D remainder), 2026-08-20.
# AUTHOR slot per BRIEF_blocco2_phaseD.md MINORS (b). One refuter
# round + auto-escalation applies. This file is the ONLY file this
# slot writes.

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
(a) J_declared = J_coded + DJ_panel exactly, where J_declared is the
    header objective over "(0, theta_B]" (a1_toc_variational_jax.py
    :22-24) evaluated by the same trapezoid rule extended with the
    theta=0 station, and J_coded is the implemented `thrust_J` over
    [th1, L];
(b) DJ_panel is W-independent EXCEPT through the single DOF thB
    (the arc geometry and the arc flow are plan-frozen; the audit's
    fix-A wording "makes the omitted area W-independent exactly" is
    the theta=0-anchor half of this statement);
(c) d(DJ_panel)/dthB = 2*pi*p(th1)*y(th1)*rtd*sin(th1)/n_B, the
    sliver derivative of record.

Hypotheses (strong, trivially checkable — AG-1 valve NOT invoked
here, this statement is load-bearing for the adjudication): frozen
plan (n_B, station topology fixed per record); p on the fixed arc
W-independent within the frozen plan (advisory §1 premise of
record); exact circular-arc geometry (code :531-534).

Proof sketch: (a) is additivity of the integral over [0,th1] u
[th1,L] with matching endpoint station; (b) all quantities in the
integrand depend on W only via thB under the hypotheses; (c) is the
Leibniz rule at the upper limit, identical to the advisory formula.

Falsifier (measured half = F2 duty, §3): in the A/B protocol of §2,
the measured |dJ_A/dthB - dJ_B/dthB| at the recorded W* must equal
the analytic prediction (c) within derived AD/FD bars; a deviation
beyond bars falsifies OBJDOM-1 (hidden W-dependence of the arc flow
or a geometry error) and re-opens the adjudication.

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
(sufficient-not-optimized, declared per AG-1 — this is
gap-accounting arithmetic): the S20 instance is the governing
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

The delta-carrier ceiling evaluation inherits the same omission
(advisory §1.4 trigger clause: "the ceiling evaluation inherits the
same omission — §3.2(iv)"; row pipeline:delta-carrier-F2-entry
trigger "sequenced with/after [OBJ-DOM]"). Under this adjudication:
the (c) relaxation lemma must state its functional as J_A
(panel-inclusive) OR explicitly as the coded J under the interim
scoping regime, and must say WHICH — a lemma silent on the domain
is non-compliant with this verdict. The delta semantics (distance
to the L-unconstrained fixed-eps ceiling) is unaffected in value
class (the panel term is common to both sides of the distance at
fixed thB-convention, so it cancels in delta IF both sides use the
same domain convention — that same-convention hypothesis is the
one (c) must declare). Class SCHEMA: composition statement, proof
obligation transferred to (c)'s lemma hypotheses.

---

## 2. Discharge protocol PINNED (the audit's analytic throat-panel A/B, protocol of record)

All steps below are MEASURED halves = F2 duty (named §3). Nothing
here is executed in this window (R5: no new number without a
committed carrier; every number quoted above is a record number
with its source cited).

- (P-1) Implement J_A = J_coded + DJ_panel(thB) with the analytic
  panel of OBJDOM-1. The panel-pressure rule (p(th) sampling on
  [0, th1]: kernel arc-flow evaluation vs p(th1) frozen-endpoint
  approximation) MUST be declared in the F2 carrier; if the
  endpoint approximation is used, its error term is O(th1) relative
  on a panel already O(th1^2) absolute — declare the resulting
  order and its bar.
- (P-2) At the recorded W* (S20 instance of record), evaluate
  dJ/dthB under BOTH functionals through the engine's AD path,
  same engine key, same frozen plan (no re-record between A and B).
- (F-1) PRIMARY ASSERT (falsifies OBJDOM-1): |dJ_A/dthB -
  dJ_B/dthB - 2*pi*p(th1)*y(th1)*rtd*sin(th1)/n_B| <= derived
  AD/FD bar (bar derivation = the O3.1 machinery of record, not a
  new constant).
- (F-2) ADJUDICATION ASSERT (falsifies OBJDOM-2/OBJDOM-4 grounds
  1): |dJ_A/dthB - dJ_B/dthB| > 10*gtol at W* after the Dv
  discount — EXPECTED TO FIRE per the record (5.8e2x). If it does
  NOT fire, the absorption branch was viable: adjudication
  re-opens (declared outcome, not a silent pass).
- (P-3) Re-run the OPT stage under J_A: the new W*_A must pass
  transversality at UNCHANGED derived gtol (no tolerance touched —
  that is the point of fix-A).
- (P-4) Re-baseline check (value axis): the recorded-J shift must
  equal DJ_panel(thB*) within Richardson bars, and the F7 band
  must be re-measured to confirm the cancellation prediction
  (advisory precision (ii)) survives the fix — a moved F7 verdict
  here would falsify the "verdict-neutral re-baseline" ground 3.

---

## 3. F2 DUTIES NAMED (measured halves; owner = F2 entry, trigger = registry row :212 verbatim: before the first F2 verdict consuming dJ/dthB AND before the R2 delta-carrier ships)

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
