# REFUTATION — PANEL_REMMARCH (C5, C6, C8, C10, C12, C13, C14)
# S-FOUNDATIONS-C3 WAVE 3, 2026-08-20. Fused refuter, attacks PER-ROW.
# Mandate: BRIEF_wave3_refuter_judge.md REFUTERS (+ h1-h3) with the
# wave-1/wave-2 refuter duties verbatim. BASE =
# validation/sfoundations_raws_2026-08-13. Every anchor below was
# re-read AT THE SOURCE in this window; every grep re-run in-window
# (SR-12). No file edited except this one.

## 0. VERIFICATION BASIS (what was checked at source)

Ledger rows C5/C6/C8/C10/C12/C13/C14 read in full at
docs/choice_ledger.yaml:178-285; findings rows GAP-6 (:1155-1163),
GAP-8 (:1173-1181), GAP-23 (:1310-1318), GAP-24/warmstart
(:1319-1327), GAP-34 (:1373-1381), GAP-35 (:1382-1390),
carriers:control-surface-invariance-rejector-missing (:1588-1596),
swirl-f2a rows (:1816/:1825/:1834), D-49 (:1468-1476); code at
a1_toc_variational_jax.py:105-184, adaptive_knot_optimize.py:193-213
and :415-459, o33_bench.py:180-200, a1_ideal_march_jax.py:30-59,
:550-566, :638-650, :840-885, :975-1009, :1050-1109; diff anchors
phaseB_tree_diff.md:45-105, :370-399; condensed trees (optimization
:71-82, hyperbolic :100-128, variational :61-69/:220-224, propulsion
:162-172); full optimization tree :516/:548 (de Casteljau line
literally at :548) and :1549-1564 (O-F32 incl. cold-start-audit
falsifier); cava A7/C33/R27 at ADVISORY_litreview_confrontation
_2026-08-13.md:1024-1028/:1118-1122/:1152-1158; literature registry
:848-853/:556-570; VERDICT_wave2.md §2.9 (:760-794, scope boundary
:775-777 verbatim) and §4.10/§4.12. Panel greps G1/G2/G4/G5 re-run.

Verbatim-quote audit declaration: all load-bearing quotes checked
verbatim PASS except the line-anchor drifts in R3REMMARCH-10 and the
two content mis-reads that ground R3REMMARCH-1 and R3REMMARCH-5.
GAP-34 magnitudes (1.4%/4.4%, DOWNGRADED low), GAP-23 magnitudes
(2.2/17.5/170, cond(A)~6), GAP-24 (P3=6.7e-16, K_RICH floor formula),
GAP-6 (+0.17 a*, r=0.1 net 2.5, "proves fidelity, not accuracy"),
GAP-8 (O(h^2) coefficient bias, no order defect), C6 ledger note
("rationale measured wrong: solve vs operator"), C14 owner ("folded
into GAP-8 oracle"), wave-2 §2.9 scope boundary — all VERBATIM-exact.

---

## R3REMMARCH-1 — C14 — **REPAIR-NEEDED** (h1 valve audit: false load-bearing premise under the valve; D-47/R5 violation)

**Claim attacked:** §3.7/§4.7 — "the exit-line row j2 cells are
ALREADY COMPUTED (a1 header :49 …): the band costs a max() over
existing values"; falsifier F-C14-1 metric = "max_j |Me_j − Me_axis|"
over the exit line.

**Mechanism + witness:** the panel's own cited header line SAYS the
opposite of what the panel read into it — a1_ideal_march_jax.py:49:
"row j2 marches along the EXIT MACH LINE from the focus K (uniform
state, slope 1/sqrt(Me^2-1))". At source, the straightening-region
row-j2 cells are IMPOSED, not solved: a1:1082-1085 builds each cell
as `mach_new = [x_prev+dxe, y_prev+dxe/sqrt(Me_ach^2-1), qq, 0.0]`
with `qq` the single speed from Me_ach (:1050-1052). Every j2 cell on
the exit Mach line carries the IDENTICAL state, so
max_j |Me_j − Me_axis| ≡ 0 identically and F-C14-1 CAN NEVER FIRE.
This is a vacuous rejector — exactly the cava-D-47 discipline the
panel itself enforces at F-C8-1 and F-C12-2 but omitted on its own
C14 pin, and an R5 violation (a test that can only confirm). Under
duty (h1) this is the named failure mode: the row was declared
gap-accounting and the false premise ("already computed") rode in
under the LOAD-CLASS VALVE unexamined.

**Why REPAIR, not BREAK:** the row OUTCOME (decision logic unchanged;
certificate carries an exit-uniformity band + the control-surface
rejector) survives once the band is anchored to data that is actually
solved. Computed candidates already in G, still one-max() cheap:
(i) the last arc column at exit fire — interior cells
G[(j, i_exit)], j in (Nv, j2], computed via solver_int (:958 loop);
(ii) the straightening-region interior cells below the exit line,
computed via solver_int (:1093-1100), whose approach to `qq` tests
the uniform-exit premise from upstream; (iii) the mass-flow closure
mdot1+mdot2 vs mdot (:1086-1106), already accumulated. NAMED REPAIR:
re-anchor F-C14-1 to (i) (primary: max_j |M_j − Me_ach| over the
final marched column) with (iii) reported as the free companion
residual; strike the "row-j2 cells already computed" sentence; the
threshold-derivation and fallback (mass-flux-weighted read) clauses
carry over unchanged.

---

## R3REMMARCH-2 — C12 — **REPAIR-NEEDED** (the pinned rejector fails the panel's own pre-registered criterion on one channel)

**Claim attacked:** §3.5/§4.5 — the displaced-start-line rejector
"BREAKS the shared-start correlation with zero new modeling"; the
pre-registered criterion (§1): "a protocol WINS iff it breaks the
shared-start error correlation … any protocol that only re-exercises
the shared start LOSES by construction."

**Mechanism + witness:** the march has TWO channels by which the
Sauer start's model error enters the certified output. (1) The
characteristic-net/adjustment-layer channel: the displaced restart
rebuilds the net from the new data line — displacement DOES decorrelate
this channel; the panel's case is sound there. (2) The mdot→Me
channel: mdot is computed ONCE by Simpson on the Sauer IVL data
(a1:853-862) and the exit target Me comes from leggeAree(mdot, eps)
(:864-879). The march conserves mass to discretization order, so a
restart from a displaced line re-measures (or inherits) the SAME
mdot, and any first-order-Sauer error IN mdot shifts Me identically
in both the original and the displaced runs. On this channel the
displaced protocol "only re-exercises the shared start": the wall
contour of both runs is steered to the same (biased) Me, contour
agreement stays within band, and the rejector is blind BY
CONSTRUCTION — the very mechanism class (correlated error) GAP-6
indicts, reproduced one level up. The panel's coverage claim is
therefore stronger than its instrument; by its own frozen criterion
the protocol as pinned does not WIN outright.

**NAMED REPAIR (instrument-grade, scope-compatible):** either (a) add
a declared mdot-channel term to the composed band — e.g. the
Kliegel-Levine second-order mass-flow correction EVALUATED as a band
term (a formula evaluation feeding a bar; not an adoption of the
higher-order start, so the F4b/F5 scope clause is untouched), or
(b) declare the mdot/Me common mode as a NAMED EXCLUSION in the
delta text ("F-C12-1 certifies start-line invariance of the net;
the mdot channel is covered only at F4b/F5") so the certificate
never silently over-claims. Option (a) preferred: cheap, and it is
what makes the rejector's PASS meaningful at production rtu.
F-C12-2's vacuousness control does NOT cover this (a 10x wall-state
corruption fires through the net channel and would certify the
protocol while the mdot channel stays blind).

---

## R3REMMARCH-3 — C12 — AMENDMENT (operational ambiguity of "displace and restart")

F-C12-1 does not pin whether the displaced start is (a) the marched
solution on column +3 taken as the new data line, or (b) a fresh
Sauer IVL constructed at the displaced station. The two differ in
firing power and in what a PASS certifies; interpretation (a) is the
GAP-6 owner reading and is non-trivial (the fan/net is rebuilt from
the new line), but the protocol text should say so EX ANTE rather
than let F-C12-2 discover a wrong implementation ex post. One
sentence pins it: "displaced start = marched data on column +3 taken
as the new IVL; the fan is rebuilt from it."

---

## R3REMMARCH-4 — C13 — AMENDMENT (F-C13-3 not executable as written)

F-C13-3 pins "|v1/y1 − (dv/dy)_axis| within derived band on recorded
march cells at two NI" — but "(dv/dy)_axis" is not a computed
quantity anywhere in the march: v ≡ 0 on the axis cell, and the unit
process itself USES v1/y1 as the finite surrogate (axis residual
a1:555-566, sm = delta*c^2*vm/ym; predictor :642-650,
sm = delta*c1^2*v1/y1). As written the invariant compares the
surrogate to an oracle that does not exist. Pin the estimator: e.g.
(dv/dy)_axis estimated by two-NI Richardson of v1/y1 (the two-NI
data the same falsifier already orders), or the H-F19 one-term
series coefficient fitted on the recorded off-axis cells
(v = a1*y + O(y^3)). Outcome unmoved — the instrument suite stays;
the third leg just needs its operand defined.

---

## R3REMMARCH-5 — C10 — AMENDMENT (protocol field error + one on-disk census closure missing)

(i) F-C10-1 orders "the three single-direction refinements at r=2
(NI rows / da arc angle / Nw-Ne stations per o33_bench.refine
fields)" — but o33_bench's cfg has NO Ne field (make_case builds
cfg = {NI, Nw, da_deg, yt, rtu, rtd, xtronc}, o33_bench.py:189-191)
and refine touches exactly NI/Nw/da_deg (:195-200). "Nw-Ne … per
o33_bench.refine fields" names a nonexistent field; the GAP-35
direction triple maps to NI / da_deg / Nw. The protocol must name
the real fields or the duty is not executable as pinned.
(ii) Census-protocol compliance (§0-ter / brief (ii)): Fidkowski-
Darmofal 2011 — the output-based-adaptation review — is ON DISK per
the wave-3 brief's new-papers list and squarely adjacent to the
refinement-operator question, yet the C10 census neither consumes it
nor closes it by stated reason (the panel DID write such a stated-
reason line for Lauer-Ansell on C5). Materiality LOW (C9/C11 are
landed authority; the diagnostic-vs-production split would not
flip), so: add the stated-reason closure line, no re-census.

---

## R3REMMARCH-6 — C8 — AMENDMENT (K_RICH conditionality one-way; V-F7 advocacy transplant)

(i) The arming floor adopted verbatim from the GAP-24 owner consumes
K_RICH — a constant whose derivation status is EXACTLY what the FAM
slot's C42 adjudication (this same wave) must settle (ledger C42:
one numeral, roles censused, derivation program). The panel notifies
FAM of the new role (correct, RC27-8(iv) precedent) but the proposed
C8 delta text carries no reverse conditionality: if C42 lands a
per-role derived constant, the C8 floor must consume THAT, not the
literal. One clause in §4.3 closes the seam both ways ("floor
constant rides the C42 role-census outcome; derived per-role
constant substitutes on landing"). Outcome unmoved.
(ii) R-4 anti-transplant: citing V-F7 (fold-margin monitor,
inf_xi sigma_min of the linearized steady operator — a seed/
hysteresis instrument, already CONSUMED into C21 by VERDICT_wave2
§2.9 "V-F7 fold-margin monitor transferred to march cells") as one of
three tree supports for C8 arming is advocacy overreach: fold margins
say nothing about design-vector re-representation exactness. The C8
verdict does not need it (the findings-row theorem + measured P3
carry it alone; O-F32 is the genuinely pertinent tree voice, and the
panel correctly firewalls its cold-start audit to C21). Drop or
demote the V-F7 citation to avoid the double-counted-advocacy
pattern the wave-2 brief names (the O-F20 C28/C20 case).

---

## R3REMMARCH-7 — §4 dedup register — AMENDMENT (G5 query vacuous as recorded; G2 hit list filtered undeclared)

(i) G5 as recorded — `grep -n "circulation|vortex-core|on-axis"
docs/findings_registry.yaml` — is a LITERAL-string query without -E:
it matches nothing on any input, so the recorded command cannot
support the "no dedicated axis-circulation row" conclusion
(SR-12/g2 query auditability). Re-run in THIS window with the
corrected form `grep -nE "circulation|vortex-core|on-axis"`: hits
:407 (base-recirculation owner text) and :1290
(basis-oscillation-axis row) — neither a dedicated axis-circulation
row, so the panel's CONCLUSION (no mint; homed per G4 + diff
:374-376) SURVIVES on the corrected evidence; the register entry
must carry the corrected command.
(ii) G2 re-run returns :1243 and :1335 in addition to the two rows
the panel reports; the relevance filtering is fine but must be
declared ("4 hits, 2 relevant") — counts-vs-citations consistency is
a §0-ter table requirement.

---

## R3REMMARCH-8 — C6 — AMENDMENT (F-C6-1 separation asserted, not derived; O-F8 fallback object unstated)

(i) F-C6-1 asserts the incumbent guard "passes" the synthetic
ratio-1e3 control. At source the incumbent guard is an
insertion-time check (site closer than dx_loc = median LOCAL station
spacing to a knot => rejected, adaptive_knot_optimize.py:210-212):
whether a ratio-1e3 configuration is ADMITTED depends on the local
station density (GAP-23's degradation law — the guard weakens as the
march refines). On a coarse-station synthetic case the incumbent may
also reject, making the control INCONCLUSIVE rather than separating.
Add the branch: "if the incumbent also rejects, instantiate the
control at the GAP-23 trigger configuration (Nw>=240 / max_ins>=3)
where the degradation law admits it, or declare the separation not
reproduced." The flip itself is safe either way (it rests on GAP-23's
measured object mismatch, not on this control), hence AMENDMENT.
(ii) R-4: the O-F8 de Casteljau fallback is transplanted from
constraint certification (Bernstein bounds on the design curve,
optimization tree :516-548) to interpolation-operator conditioning
without stating WHAT the subdivision certifies in the C6 context
(presumably a Bernstein-form bound on cardinal amplitude over the
knot interval). One sentence names the transplanted object or the
fallback naming is decorative.

**Single-author discharge (C6):** the declaration is brief-mandated
and correctly placed; with (i)/(ii) as amendments the discharge
itself stands — the flip's evidentiary base (GAP-23 measurement + Q1
census + pre-registered criterion) survived genuine attack here.

---

## R3REMMARCH-9 — C5 — **NO-ATTACK-FOUND** on the verdict (declared, with reason) + NOTE

Attacked and held: (i) the nesting argument is code-verified — knots
are stored as normalized xi and mapped affinely through live xB
(a1_toc:110-118 comment block including "moving affinely with xB
exactly as the uniform class does"; wall_geometry :176-183
xs = xB + (L−xB)·xi), so physical-x anchoring genuinely breaks class
membership under xB motion — the stated structural cost is real, not
rhetorical; (ii) GAP-34 magnitudes and DOWNGRADED-low status quoted
verbatim (:1373-1381); the materiality call is the row's own
verifier-corrected record, used in the honest direction; (iii) all
three alternatives steelmanned with stated, checkable costs;
free-knot rejection correctly cited to D6 item 9 at its code echo
(:114-115); (iv) F-C5-1 has a derived-threshold clause with a
pre-registered replay control (S18 4.4% must flag or the derivation
must say why) — a genuinely firing monitor, D-47-compliant; (v) the
trees-silent claim matches diff :51 and §5 :398 exactly. Residual
NOTE (no class): the Q6 absence-of-a-modern-line claim rests on
[ABS]-depth snippets — honestly marked as such in the panel; the
census closes by stated search, which is what §0-ter asks.

---

## R3REMMARCH-10 — cross-row — AMENDMENT (anchor drifts; content verified correct at the true lines)

Batched mis-cites (duty: a mis-cite is a finding; none load-bearing,
all content re-verified at the true anchors in §0):
- GAP-8 row is findings :1173-1181, panel cites ":1176-1183"
  (overshoots into the next row's header).
- GAP-6 row is :1155-1163, panel cites ":1155-1164" (last line
  belongs to thermo-bands:bands-not-topology-conditioned).
- wanted_eca_hoekstra_2014 id sits at literature :852-853; panel
  cites ":850-851" twice — :850 is the PREVIOUS wanted row's owner
  line (f2-c11 registration rider).
- insertion_site spans adaptive_knot_optimize.py:197-213; panel
  cites ":195-212".
Repair at the judge/landing: correct the four anchors in the delta
texts that carry them (the C10 §4.4 delta cites ":850" verbatim).

---

## R3REMMARCH-11 — C12/C13 — NOTE (h3 scope-clause audit: honored, one wording caution)

C12: the higher-order branch is genuinely NOT adjudicated (no
verdict, no adoption; K-L full texts correctly deferred as the
branch's conditional procurement). CAUTION: the proposed delta wording
"census ranking RECORDED: Kliegel-Levine presumptive first candidate"
edges toward pre-deciding the F4b/F5 panel's opening order; label it
"census evidence recorded (Q3 2026-08-20)" rather than a ranking so
the branch owner inherits evidence, not a verdict. C13: the swirl/
axis-circulation obstruction is NAMED-not-decided with correct homes
(diff :374-376 verbatim; swirl-f2a rows :1816/:1825/:1834 verified;
S-5F chain cited as consumer) — no phase-owned territory crossed.
C7-adjacent material (insertion-only ratchet, :1328) correctly left
to REMPOL.

---

## R3REMMARCH-12 — slot-wide — NOTE (h2 authority-consistency: PASS)

Checked at source: VERDICT_wave2 §2.9 scope boundary quoted exactly
(:775-777 "fixed march topology + fixed seed set; seed validity under
remeshing/redistribution is F9b's object") and CONSUMED, not
re-opened — the C8/C21 disjointness composition is faithful;
the K_RICH role notification follows the §4.12/RC27-8(iv) discipline
(FAM owns the census, this panel only notifies — correct direction);
wave-1 C9/C11 and the C9C11 supplement are consumed via the ledger
rows :221-252 which carry the verdict text verbatim (checked against
the rows) — C10's composition declaration ("mesh LAW and ESTIMATOR
untouched; this row governs the OPERATOR only") is consistent with
both; no landed outcome is contradicted anywhere in the panel.

---

## PER-ROW COVERAGE MAP (duty g4)

- C5:  R3REMMARCH-9 (declared no-attack with reason + note)
- C6:  R3REMMARCH-8 (amendment x2)
- C8:  R3REMMARCH-6 (amendment x2)
- C10: R3REMMARCH-5 (amendment x2)
- C12: R3REMMARCH-2 (REPAIR), -3 (amendment), -11 (note)
- C13: R3REMMARCH-4 (amendment), -11 (note)
- C14: R3REMMARCH-1 (REPAIR)
- slot-wide: -7 (dedup register), -10 (anchors), -12 (h2 PASS)

R-4 anti-transplant audit instances (8): O-F8→C6 (finding -8ii),
V-F26→C8 (held: backbone claim used only as arming support, native
context declared), V-F7→C8 (finding -6ii), O-F32→C8 (held: cold-start
audit correctly firewalled to C21), H-F15/H-F16→C12 (held: recorded
into the F4b/F5 home, not adopted), H-F19-parity→C13 (finding -4:
operand undefined), H-F19-swirl→C13 (held: named-not-decided,
consumers correct), P-F22→C14 (held: consumed via the existing
findings row, no re-mint).

ESCALATION FLAG for the judge: R3REMMARCH-1 and -2 are CONTENT
objections; if sustained, the standing rule escalates C14 and C12 to
full form UNLESS the judge adopts the named repairs verbatim in the
same verdict (both repairs are text-level, cheap, and leave each
row's outcome class unchanged — the dry criterion of record counts
them as sustained REPAIRS either way).

Dedup register (this file): no new row proposed by this refutation;
both repairs edit falsifier texts pinned by the panel; the corrected
G5 command replaces the recorded one in the panel's own register.

## MACHINE SUMMARY

```
cluster: REMMARCH
findings:
  - {id: R3REMMARCH-1,  class: REPAIR-NEEDED, row: C14}
  - {id: R3REMMARCH-2,  class: REPAIR-NEEDED, row: C12}
  - {id: R3REMMARCH-3,  class: AMENDMENT,     row: C12}
  - {id: R3REMMARCH-4,  class: AMENDMENT,     row: C13}
  - {id: R3REMMARCH-5,  class: AMENDMENT,     row: C10}
  - {id: R3REMMARCH-6,  class: AMENDMENT,     row: C8}
  - {id: R3REMMARCH-7,  class: AMENDMENT,     row: slot-dedup}
  - {id: R3REMMARCH-8,  class: AMENDMENT,     row: C6}
  - {id: R3REMMARCH-9,  class: NOTE,          row: C5}
  - {id: R3REMMARCH-10, class: AMENDMENT,     row: cross-row-anchors}
  - {id: R3REMMARCH-11, class: NOTE,          row: C12+C13-scope}
  - {id: R3REMMARCH-12, class: NOTE,          row: slot-authorities}
breaks: 0
repairs: 2
amendments: 7
notes: 3
key_witnesses:
  - "R3REMMARCH-1: a1_ideal_march_jax.py:1082-1085 imposes uniform state qq on every row-j2 exit-line cell => F-C14-1 metric == 0 identically (vacuous rejector; panel's own header cite :49 says 'uniform state')"
  - "R3REMMARCH-2: mdot from Sauer IVL Simpson (a1:853-862) fixes Me via leggeAree (:864-879) identically in original and displaced runs => Sauer error in the mdot channel invisible to F-C12-1 by construction (fails the panel's own pre-registered win criterion on that channel)"
per_row_coverage: {C5: no-attack-declared, C6: attacked, C8: attacked, C10: attacked, C12: attacked, C13: attacked, C14: attacked}
escalation_note: "R3REMMARCH-1/-2 are content objections; named text-level repairs provided; if adopted verbatim by the judge the row outcome classes stand"
```
