# ESCALATED REFUTATION r1 — PHASE D MINOR (b) [OBJ-DOM]
# S-FOUNDATIONS-C4 escalation window, 2026-08-20. Role: ESCALATED
# REFUTER, single fused lens (math structure + carrier/bookkeeping
# contracts), round 1, per VERDICT_blocco2.md SS2.2/SS3 E-2 and
# BRIEF_blocco2_phaseD_addendum_c4.md. Target: the REVISED
# phaseD_minor_objdom.md (all [ESC-r1-0..9] markers + disposition
# table) and refute_minor_objdom.md. This slot writes ONLY this file
# and its probe esc_probe_objdom_etrunc_order.py. Zero inflation:
# every finding anchored; everything else checked is in the
# VERIFIED-SOUND note (ESC-OBJDOM-r1-4).
#
# Probe of record (this window, exit 0 = counterexample stands):
#   validation/sfoundations_raws_2026-08-13/phaseD/
#   esc_probe_objdom_etrunc_order.py  (numpy only, pinned env, no
#   installs; 4 rejectors, all PASS, run 2026-08-20)

## FINDINGS

### ESC-OBJDOM-r1-1 [BREAK] — the applied repair [ESC-r1-1] is itself
unsound in clause (a.2): the truncation-order claim
"O((Dy)^3) ... hence O(th1^6)-class" is FALSE generically; the true
generic order is O(th1^3) — three orders larger — probe-demonstrated

Anchor: revised file §1 OBJDOM-1(a.2) ("E_trunc the single-interval
trapezoid truncation error: O((Dy)^3) with Dy = rtd*(1 - cos th1) =
O(th1^2), hence O(th1^6)-class") + proof sketch ("(a.2) is the
standard single-interval trapezoid truncation bound [ESC-r1-1]") +
disposition table row MIN-OBJDOM-1 ("the integral-vs-trapezoid
discrepancy declared as (a.2) O((Dy)^3) = O(th1^6)-class").

Reason (math): the coded rule trapezoids in y (thrust_J :1185-1186,
re-verified this window: dy = y[1:]-y[:-1]). The standard
single-interval bound E = -(Dy^3/12) f''(xi) requires f = p*y to be
C^2 in y ON THE PANEL. It is not, generically: dy/dth = rtd*sin(th)
vanishes at th = 0, so th(y) ~ sqrt(2(y-yt)/rtd) and p as a function
of y has a SQUARE-ROOT CUSP at the throat whenever p'(0) != 0 —
f''(y) is unbounded on the panel and the cited bound is vacuous.
p'(0) = rtd*(dp/dx)_throat != 0 is the GENERIC case for the kernel
arc flow (accelerating transonic wall flow at the throat). Direct
th-expansion (re-derived this window, probe-confirmed):
    E_trunc = -(pi/6)*rtd*p'(0)*yt*th1^3 + O(th1^4)  = O(th1^3),
NOT O(th1^6). The O(th1^6) class is recovered ONLY under the
additional hypothesis p'(0) = 0 (p even in th at the throat), which
the statement does not carry.

Probe evidence (esc_probe_objdom_etrunc_order.py, all rejectors
PASS): generic case log-log slope of |E_trunc| vs th1 = 3.0000
(claim: 6); coefficient ratio E_trunc/[-(pi/6)*rtd*p'(0)*yt*th1^3] =
1.0000 across the sweep; even-p control (p'(0) = 0) slope = 6.0002 —
the claimed order holds exactly and only there. Internal-consistency
cross-check (rejector [4]): E_endpoint = -2 * E_trap, both O(th1^3)
— the revision's own P-1 already declares the ENDPOINT rule's error
absolute-O(th1^3)-class ("O(th1) relative on a panel already
O(th1^2) absolute"); a trapezoid rule using strictly the same
endpoint information cannot be three orders better, so (a.2) as
printed was inconsistent with P-1 within the same revision.

Failure/consequence: a false order claim with an inapplicable proof
step inside a THEOREM-class statement — the same defect class
MIN-OBJDOM-1 killed in round 1 (exactness/order false under its own
definitions). SCOPE (honesty, no inflation): (a.1)'s discrete
identity, (b), (c), OBJDOM-2/3, the OBJDOM-4 adjudication and the
F-2 assert are ALL untouched; the corrected E_trunc remains
numerically sub-J-unit at the record instance (SCALING-ESTIMATE:
(pi/6)*0.45*|p'(0)|*th1^3 ~ 0.2-0.8 J-units at |p'| ~ p_t-class —
illustration only, no number of record), so "numerically tiny,
DECLARED, never called exact" survives; the ORDER does not.

Named repair: restate (a.2) as
  E_trunc = -(pi/6)*rtd*p'(0)*yt*th1^3 + O(th1^4), generic
  (O((Dy)^{3/2})-class in the y variable: p has a sqrt cusp in y at
  the throat since dy/dth -> 0); the O((Dy)^3) = O(th1^6) class
  holds iff p'(0) = 0 (declared extra hypothesis, not generic);
and re-point the proof sketch from "standard trapezoid truncation
bound" to the direct th-expansion (or the O(Dy^{3/2}) cusp bound).
Fix the disposition-table row [ESC-r1-1] accordingly. No other
statement moves.

### ESC-OBJDOM-r1-2 [REPAIR] — the applied repair [ESC-r1-2] is
incomplete: F-1's KERNEL branch still admits a spurious fire; the
disposition claim "Spurious-fire branch closed" overreaches

Anchor: revised file §2 (F-1) ("kernel arc-flow rule: prediction =
2*pi*p(th1)*y(th1)*rtd*sin(th1)/n_B (OBJDOM-1(c); no extra term)")
+ (P-1) ("Implement J_A = J_coded + DJ_panel(thB) with the analytic
panel of OBJDOM-1"; only the p-SAMPLING rule must be declared) +
disposition table row MIN-OBJDOM-2 ("Spurious-fire branch closed").

Reason (math + protocol): the kernel-branch prediction "(c); no
extra term" is exact ONLY if the implemented panel is the exact
integral. That is unimplementable literally: p(th) is the numerical
kernel/fan flow with no closed form, so every kernel-branch
implementation is a QUADRATURE, and AD returns the derivative of the
quadrature, differing from (c) by the quadrature-error derivative —
a modeling term of the implemented rule, exactly the object class
the revision itself rules "part of the PREDICTION and never of the
noise bar". The rule is unpinned by P-1 (P-1 pins only the
p-sampling choice). Concrete in-branch counterexample: the theta=0-
station single-interval trapezoid — the advisory's OWN first-named
fix-A form ("add the theta = 0 throat station", advisory :150-151)
and precisely OBJDOM-1(a.1)'s object, kernel-sampled hence in F-1's
kernel branch. Probe rejector [3]: its exact d/dth1 (= what AD
returns) differs from prediction (c) by a relative O(th1) term
(measured slope 1.001; leading coefficient (p'/4p)*th1), i.e.
J-units/rad scale at the record constants (SCALING-ESTIMATE: ~3.5
J-units/rad at p'/p = 0.3/rad, illustration only) — orders above
any AD/FD-noise-class bar, same class as the endpoint modeling term
[ESC-r1-2] refuses to absorb silently. An F2 executor implementing
fix-A as the advisory's own station form and asserting F-1 per its
letter reports OBJDOM-1 falsified on an artifact — the identical
failure shape MIN-OBJDOM-2 named, surviving in the other branch.

Scope: F-2 and the OBJDOM-4 adjudication are untouched (percent-
fraction terms against a 5.8e2x margin); the endpoint branch as
repaired is airtight (its panel IS closed-form, G(th1) analytic, so
AD matches the branch prediction exactly up to AD/FD noise —
verified).

Named repair (one structural clause): extend P-1's declaration duty
from the p-sampling rule to the PANEL QUADRATURE RULE, and
branch-match F-1 to it, three branches:
  (i) theta=0-station trapezoid rule (fix-A station form):
      prediction = exact d(DJ_panel^trap)/dthB, closed form in
      p(0), p(th1), p'(th1) (all available via the declared AD
      path):
      2*pi*[0.5*(p'(th1)*y(th1) + p(th1)*rtd*sin(th1))*(y(th1)-yt)
            + 0.5*(p(0)*yt + p(th1)*y(th1))*rtd*sin(th1)]/n_B;
  (ii) closed-form endpoint rule: the already-repaired prediction
      (c) + 2*pi*p'(th1)*G(th1)/n_B;
  (iii) declared m-node composite rule in th: prediction (c) + the
      rule's quadrature-derivative term, either carried explicitly
      or bounded by a DERIVED bar shown below the AD/FD bar
      (declared, never silent).
Reword P-1's "with the analytic panel" to "with the declared panel
rule (analytic-integral target)". Fix the disposition-table claim.

### ESC-OBJDOM-r1-3 [AMENDMENT] — [ESC-r1-9]'s "bookkeeping already
landed" is false as of this window (SR-12)

Anchor: revised file §4 [ESC-r1-9] ("Bookkeeping already landed at
the judge window per E-2: the code anchor refresh (registry row, §7
of the verdict).") vs docs/findings_registry.yaml READ THIS WINDOW
(:204-213): the code field at :209 still carries the DRIFTED anchors
["...:516-522", "...:1130-1137"], and the note field :213 carries no
LB-6(b) append. VERDICT_blocco2 E-2/LB-6 SCHEDULED the refresh
("lands now" = placed on the landing list the orchestrator applies
verbatim); as of this read it has NOT been executed. The sentence
also contradicts the same file's §0 ("the row anchors should be
refreshed at the landing"). Per SR-12 a repo-state claim must cite a
measurement in its own window; none is given.

Repair (one sentence): replace with "Bookkeeping ORDERED at the
judge window per E-2/LB-6 (code anchor refresh; execution =
orchestrator landing, not yet applied as of this revision's
window)." No math is affected; a reader trusting the current text
would skip the refresh and leave the row pointing at column-stack
code.

### ESC-OBJDOM-r1-4 [NOTE] — VERIFIED-SOUND record (coverage; all
checks in THIS window, at source)

- [ESC-r1-1] clause (a.1): discrete identity re-derived against the
  coded rule (thrust_J :1179-1186: trapezoid in y, 2*pi prefactor;
  stations :530-531 start k=1; y(0) = yt) — EXACT by sum additivity;
  the 2*pi restoration of the refuter's identity is correct. Only
  (a.2)'s order claim breaks (r1-1).
- [ESC-r1-2] endpoint-branch prediction: Leibniz + product rule
  re-derived; 2*pi*[p*y*rtd*sin + p'*G]/n_B correct; the (p'/p)*
  th1/2 relative-order label correct (G ~ rtd*yt*th1^2/2).
- [ESC-r1-3] OBJDOM-5 rewrite: conforms to the binding VERDICT
  SS4(1)-(3) text ((H6'-A)/(H6'-B) two-branch, ship-gate re-pinned
  to the row-:300 banded-or-repaired license; sequencing sentence
  verbatim). Ceil-seam n_B = ceil(thB/da) verified in code (:326,
  max(1, ceil)); anti-conservative direction and inheritance clauses
  verified at advisory :237-245 (SS3.2 items 3 and 4) and :155-157
  (SS1.4 trigger). The retraction of the same-convention claim is
  faithful to MIN-OBJDOM-3 as sustained.
- [ESC-r1-4]: the fix-A phrase "makes the omitted area W-independent
  exactly" verified AT :150-151 of the advisory and ABSENT from
  audit :507-519 (audit carries only the suggested test :517) —
  attribution repair correct.
- [ESC-r1-5]: the §3 trigger quote verified CHARACTER-EXACT against
  docs/findings_registry.yaml:212 this window (including the
  "; discharge test = ..." tail); the dropped "before the" prefix is
  indeed the advisory's phrasing (:155-156), not the row's.
- [ESC-r1-6]: audit :517 literal test ("< gtol at W*") verified at
  source; the declared departure (comparator 10*gtol of record,
  advisory :131, inverted expected-to-fire semantics) is accurate
  and the ">= 5.7e2x / 5.8e2x either threshold" claim holds
  (5.36e3/9.3 = 5.8e2; vs gtol alone even larger).
- [ESC-r1-7]: label alignment (load-bearing, valve NOT invoked)
  consistent with OBJDOM-1's treatment and the AG-1 valve rule.
- [ESC-r1-8]: direction correction INDEPENDENTLY re-verified at
  audit :529 ("x0 = W/Dv, jac = g*Dv"): u = W/Dv => dJ/du =
  (dJ/dW)*Dv — conversion to scipy's u-coordinates is a
  MULTIPLICATION by Dv_thB; the author's correction of the round-1
  refuter's "divide" is RIGHT. Fallback (spread-6 discount, audit
  :527/:533 block) = the recorded >= 96x operation; executable as
  pinned.
- OBJDOM-2 arithmetic (5.36e3/9.3 = 5.8e2, /6 => 96x) re-verified;
  OBJDOM-3(a)/(b) re-checked (dA/dthB Leibniz step correct); the
  OBJDOM-4 adjudication direction (fix-A of record at F2 entry,
  fix-B scoping interim) is NOT touched by any finding in this file
  — consistent with VERDICT SS2.2's expectation.
- PAPERS NEEDED (empty) in the revision: legitimate (internal
  adjudication; re-checked against the addendum carriers — no
  arrival bears on the objective-domain decision).

## READ-DEPTH DECLARATION (this window)

All internal, no papers consulted: phaseD_minor_objdom.md [FULL]
(revised, all markers); refute_minor_objdom.md [FULL];
VERDICT_blocco2.md [FULL]; BRIEF_blocco2_phaseD_addendum_c4.md
[FULL]; docs/findings_registry.yaml:200-244 [FULL];
validation/ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md
:40-164, :213-267 [FULL]; validation/AUDIT_agnostic_2026-08-07.md
:500-544 [FULL]; validation/a1_toc_variational_jax.py:18-47,
:515-549, :1165-1194 [FULL] + grep n_B/ceil (:326, :481, :692,
:794).

PAPERS NEEDED: (empty)

## MACHINE SUMMARY

findings: 1 BREAK (ESC-OBJDOM-r1-1: (a.2) truncation order
  O(th1^6) false, true generic O(th1^3), probe-demonstrated,
  clause-scoped), 1 REPAIR (ESC-OBJDOM-r1-2: F-1 kernel branch
  still spuriously fireable — quadrature rule unpinned; three-branch
  fix named), 1 AMENDMENT (ESC-OBJDOM-r1-3: "already landed"
  bookkeeping claim false this window, SR-12), 1 NOTE
  (verified-sound coverage).
not_dry: round 1 finds content — a further author pass is owed on
  r1-1/r1-2/r1-3 (all three are short, named, and conclusion-
  preserving).
adjudication: the OBJDOM-4 direction (fix-A of record at F2 entry;
  fix-B scoping interim) SURVIVES this round untouched; F-2 and all
  record magnitudes unaffected.
probe: esc_probe_objdom_etrunc_order.py exit 0 (4/4 rejectors PASS),
  re-runnable, numpy-only, pinned env.
