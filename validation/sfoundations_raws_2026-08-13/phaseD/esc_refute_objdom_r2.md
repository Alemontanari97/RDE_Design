# ESCALATED REFUTATION r2 — PHASE D MINOR (b) [OBJ-DOM]
# S-FOUNDATIONS-C4 escalation window, 2026-08-20. Role: ESCALATED
# REFUTER, single fused lens (math structure + carrier/bookkeeping
# contracts), round 2, per VERDICT_blocco2.md SS2.2/SS3 E-2 and
# BRIEF_blocco2_phaseD_addendum_c4.md. Target: the round-2 REVISED
# phaseD_minor_objdom.md (all [ESC-r2-0..3] markers + SS7 disposition
# table), against refute_minor_objdom.md, VERDICT_blocco2 SS2.2/SS4,
# and esc_refute_objdom_r1.md (prior-objection resolution verified).
# This slot writes ONLY this file and its probe
# esc_probe_objdom_evenp_iff.py. Zero inflation: every finding
# anchored; everything else checked is in the VERIFIED-SOUND note
# (ESC-OBJDOM-r2-2).
#
# Probes of record (BOTH re-run in THIS window):
#   esc_probe_objdom_etrunc_order.py (r1 refuter's) — exit 0, 4/4
#     rejectors PASS: re-runnable as claimed by [ESC-r2-0].
#   esc_probe_objdom_evenp_iff.py (NEW, this round) — exit 0, 4/4
#     rejectors PASS: counterexample for ESC-OBJDOM-r2-1 stands.

## PRIOR-OBJECTION RESOLUTION (r1 findings, verified in this window)

- ESC-OBJDOM-r1-1 (BREAK): RESOLVED in its governing half — the
  generic order claim is now correct ((a.2): E_trunc =
  -(pi/6)*rtd*p'(0)*yt*th1^3 + O(th1^4), O(th1^3) absolute,
  O((Dy)^{3/2}) cusp class; proof sketch re-pointed off the
  inapplicable C^2 bound; both disposition-row echoes corrected).
  Independently re-derived this window: series expansion gives
  E/(2pi) = -rtd*p'(0)*yt*th1^3/12 exactly as printed; the cusp-bound
  cross-check in the y variable reproduces the SAME coefficient
  (-(1/6)*p1*sqrt(2/rtd)*yt*Dy^{3/2} with Dy = rtd*th1^2/2 =
  -rtd*p1*yt*th1^3/12) — the two routes agree term-for-term. BUT the
  restatement introduces a NEW false clause in the non-generic
  branch: see ESC-OBJDOM-r2-1 below.
- ESC-OBJDOM-r1-2 (REPAIR): RESOLVED — the named three-branch repair
  is adopted verbatim and is sound (verification in ESC-OBJDOM-r2-2:
  branch (i) closed-form derivative re-derived and matches; branch
  (ii) re-derived; branch coverage attacked, no uncovered
  combination found).
- ESC-OBJDOM-r1-3 (AMENDMENT): RESOLVED — the replaced sentence is a
  dated in-window measurement, and it REPRODUCES in THIS window
  (SR-12 re-measure, see ESC-OBJDOM-r2-2 item 2).
- ESC-OBJDOM-r1-4 (NOTE): no action was owed; correctly acknowledged.

## FINDINGS

### ESC-OBJDOM-r2-1 [BREAK] — the [ESC-r2-1] restatement introduces a
new false clause: "O(th1^6) is recovered IFF p'(0) = 0" fails in the
SUFFICIENCY direction — with p'(0) = 0 and p'''(0) != 0 the true
order is O(th1^5), probe-demonstrated

Anchor (three sites): revised file SS1 OBJDOM-1(a.2) ("The O((Dy)^3)
= O(th1^6) class is recovered IFF p'(0) = 0 (p even in th at the
throat) — a declared EXTRA hypothesis"); SS6 disposition row
MIN-OBJDOM-1 [ESC-r2-1 CORRECTION] ("O(th1^6) iff p'(0)=0 (declared
extra hypothesis)"); SS7 disposition row ESC-OBJDOM-r1-1
("O((Dy)^3)=O(th1^6) holds IFF p'(0)=0, carried as declared extra
hypothesis").

Reason (math): E_trunc is a LINEAR functional of p (both the
trapezoid and the integral are linear in p), so odd Taylor terms of
p contribute independently. The r1 mechanism does not stop at the
first odd term: under th(y) ~ sqrt(2(y-yt)/rtd), the odd term
p3*th^3 (p3 = p'''(0)/6; p'(0) = 0) maps to a (y-yt)^{3/2}
HALF-POWER of f(y) = p*y on the panel — f'' ~ (y-yt)^{-1/2} is again
unbounded, and the single-interval trapezoid error of a Dy^{3/2}
term is O(Dy^{5/2}) = O(th1^5), not O(Dy^3) = O(th1^6). Direct
series expansion (this window): with p = p0 + p3*th^3,
    I/(2pi) = rtd*[p0*yt*th1^2/2 + p0*(rtd/2 - yt/6)*th1^4/4
              + p3*yt*th1^5/5] + O(th1^6),
    T/(2pi) = rtd*[p0*yt*th1^2/2 + p0*(rtd/8 - yt/24)*th1^4
              - p0*(rtd/8 - yt/24)*th1^4 ... (p0 part cancels
              IDENTICALLY: f linear in y => trapezoid exact)
              + p3*yt*th1^5/4] + O(th1^6),
    E_trunc = 2pi*rtd*p3*yt*th1^5*(1/4 - 1/5)
            = (pi/10)*rtd*p3*yt*th1^5 + h.o.t.  = O(th1^5).
The TRUE characterization is:
    E_trunc = O(th1^6)  <=>  p'(0) = 0 AND p'''(0) = 0
(odd th^5 terms map to (y-yt)^{5/2}, whose trapezoid error is
O(Dy^{7/2}) = O(th1^7), below the th1^6 threshold — so exactly the
first TWO odd derivatives must vanish; full evenness of p in th is
sufficient but stronger than necessary). p'(0) = 0 alone is
NECESSARY (r1 result, unchanged) and NOT sufficient. The
parenthetical gloss "(p even in th at the throat)" silently equates
a single-derivative condition with evenness; the r1 refuter's own
finding claimed only NECESSITY ("recovered ONLY under p'(0) = 0");
the author's restatement upgraded it to a biconditional — an
overreach BEYOND the named repair, new text of this revision.

Probe evidence (esc_probe_objdom_evenp_iff.py, all rejectors PASS,
exit 0, this window): [1] p = 1 + 0.3*th^3 (p'(0) = 0): log-log
slope of |E_trunc| vs th1 = 5.007 (IFF-claim predicts 6); [2]
coefficient ratio E_trunc/[(pi/10)*rtd*p3*yt*th1^5] -> 1.0007 across
the sweep; [3] control, p even (1 - 0.3*th^2): slope 5.999 —
evenness IS sufficient, control intact; [4] control, generic
p'(0) != 0: slope 3.0000 — the r1 necessity result unchanged. Sweep
points all below the record thB = 0.2007 and above the diagnosed
float64 noise floor.

Failure/consequence + SCOPE (honesty, no inflation): a false
biconditional standing in a THEOREM-class clause — the same defect
class as r1-1, one branch deeper. It is CONCLUSION-PRESERVING:
nothing of record consumes the p'(0) = 0 branch (the hypothesis is
"declared EXTRA", invoked nowhere); the generic O(th1^3) statement,
its coefficient, (a.1), (b), (c), F-1's three branch predictions
(none uses E_trunc's order), F-2, OBJDOM-2/3, and the OBJDOM-4
adjudication DIRECTION are all untouched; no record magnitude moves.
Physically the panel flow is an accelerating transonic expansion
(p'(0) != 0 generic), so the broken branch is doubly non-governing.

Named repair (one clause, three sites): replace "recovered IFF
p'(0) = 0 (p even in th at the throat)" with "recovered IFF p'(0) =
0 AND p'''(0) = 0 (p even in th through cubic order; full evenness
sufficient); with p'(0) = 0 alone and p'''(0) != 0 the order is
O(th1^5) (Dy^{5/2} cusp: E_trunc = (pi/10)*rtd*(p'''(0)/6)*yt*th1^5
+ h.o.t.)" — and echo the same correction in the SS6 and SS7
disposition rows. No other statement moves.

### ESC-OBJDOM-r2-2 [NOTE] — VERIFIED-SOUND record (coverage; all
checks in THIS window, at source or by independent re-derivation)

1. Probe re-runnability ([ESC-r2-0]'s claim): the r1 probe
   esc_probe_objdom_etrunc_order.py re-run THIS window — exit 0, 4/4
   rejectors PASS, output figures match those quoted in the revision
   (generic slope 3.0000, even slope 6.0002, coefficient ratio
   1.0000, rel-mismatch 6.562e-04 x tilt = 3.5 J-units/rad).
2. [ESC-r2-3] SR-12 measurement REPRODUCES: docs/findings_registry
   .yaml:204-213 read this window — :209 still carries the drifted
   anchors [":516-522", ":1130-1137"]; :213 carries no LB-6(b)
   append. The ordered-not-yet-applied sentence is accurate as
   dated; consistent with SS0.
3. SS3 trigger quote re-verified CHARACTER-EXACT against
   docs/findings_registry.yaml:212 in this window (including the
   "; discharge test = ..." tail).
4. Code anchors re-verified in the current tree: :22-27 objective
   header "(0, theta_B]" + Pa clause; :326 n_B = max(1,
   ceil(thB/da)); :530-534 stations k = 1..n_B (no theta=0 station);
   :1179-1186 thrust_J trapezoid in y over supplied points. All as
   stated.
5. [ESC-r2-1] governing half re-derived independently: generic
   E_trunc coefficient -(pi/6)*rtd*p'(0)*yt*th1^3 confirmed by
   series AND by the y-variable cusp route (identical coefficient);
   O((Dy)^{3/2}) label consistent (Dy^{3/2} ~ th1^3); "+O(th1^4)"
   remainder valid as an upper bound. Only the IFF clause breaks
   (r2-1).
6. [ESC-r2-2] branch (i) prediction re-derived from (a.1) by
   (1/n_B)*d/dth1 (product + Leibniz, y' = rtd*sin(th1), p(0)
   plan-frozen at the FIXED th = 0 station so no dp(0)/dthB term):
   matches the printed closed form symbol-for-symbol. Branch (ii)
   re-derived (G' = y*rtd*sin; modeling term 2*pi*p'(th1)*G(th1)/n_B;
   relative (p'/2p)*th1-class via G ~ rtd*yt*th1^2/2). Branch (iii)
   catch-all with declared-or-derived-bar term: sound.
7. Branch-coverage attack (cross-axis combinations of P-1(1)
   p-sampling x P-1(2) quadrature): the endpoint-p + trapezoid-in-y
   combination DEGENERATES EXACTLY to branch (ii) — G(th1) =
   Int_0^{th1} y*rtd*sin dth = (y1^2 - yt^2)/2 identically (exact
   change of variable), and the trapezoid of the linear integrand y
   in y is exact, so 2*pi*0.5*(p(th1)*yt + p(th1)*y1)*(y1 - yt) =
   2*pi*p(th1)*G(th1). Branch (i) is explicitly pinned
   kernel-sampled; the governing clause ("the prediction must be the
   exact derivative OF THAT RULE") covers any residual combination
   via (iii). NO uncovered branch found — the r1-2 repair closes the
   spurious-fire family.
8. F-1 preamble consistency: "prediction (c) ... attained by no
   implemented branch" — structurally true (every branch prediction
   = (c) + that branch's quadrature-derivative term; checked for (i)
   and (ii) explicitly).
9. Probe constants match the advisory SS1.3 record instance at
   source (yt = 1, rtd = 0.45, th1 = da = 0.008727, n_B = 23, thB =
   0.2007, tilt 5.36e3, acceptance 9.3, value 1.0767e-4*p_t —
   verified at advisory :113-120, :131).
10. [ESC-r1-4] attribution re-verified: "makes the omitted area
   W-independent exactly" IS advisory :151; audit :507-519 carries
   only the suggested test (:517 "< gtol at W*"), so [ESC-r1-6]'s
   declared-departure sentence is accurate; the ">= 5.7e2x / 5.8e2x
   either threshold" figures hold as lower bounds (5.36e3/9.3 = 576;
   vs gtol alone 5.8e3x).
11. [ESC-r1-8] Dv direction re-verified at audit :529 ("x0 = W/Dv,
   jac = g*Dv"): u = W/Dv => dJ/du = (dJ/dW)*Dv_thB —
   MULTIPLICATION, as pinned; fallback spread-6 = the recorded 96x
   operation (audit :527/:533).
12. Bookkeeping contracts: SS7 disposition table covers all four r1
   findings with in-place corrections to the SS6 rows they touched;
   [ESC-r2-*] markers all present and pointed; single-file
   discipline respected (no extra author files); header tallies
   match the r1 machine summary; PAPERS NEEDED (empty) remains
   legitimate (internal adjudication; re-checked, no arrival bears).
13. Unchanged-by-design list honored: OBJDOM-2/3/4, F-2, SS3 duty
   structure, SS4 landing text (still PROPOSED per [ESC-r1-9]) —
   none touched by the r2 edits beyond their declared scope.

## READ-DEPTH DECLARATION (this window)

All internal, no papers consulted: phaseD_minor_objdom.md [FULL]
(round-2 revised, all markers); esc_refute_objdom_r1.md [FULL];
refute_minor_objdom.md [FULL]; VERDICT_blocco2.md [FULL];
docs/findings_registry.yaml:200-217 [FULL];
validation/ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md
:100-158 [FULL at range]; validation/AUDIT_agnostic_2026-08-07.md
:505-536 [FULL at range]; validation/a1_toc_variational_jax.py
:18-31, :322-329, :524-537, :1175-1187 [FULL at ranges]; both probe
sources [FULL] + both executed this window (exit 0 each).

PAPERS NEEDED: (empty)

## MACHINE SUMMARY

findings: 1 BREAK (ESC-OBJDOM-r2-1: the [ESC-r2-1] restatement's
  "O(th1^6) IFF p'(0)=0" false in the sufficiency direction — true
  condition p'(0)=0 AND p'''(0)=0; with p'''(0)!=0 the order is
  O(th1^5), coefficient (pi/10)*rtd*p3*yt, probe-demonstrated;
  clause-scoped, conclusion-preserving, three anchor sites, one-clause
  named repair), 1 NOTE (verified-sound coverage, items 1-13).
not_dry: round 2 finds content — a further author pass is owed on
  r2-1 (short, named, conclusion-preserving; three echo sites).
prior_objections: r1-1 resolved in its governing half (new overreach
  = r2-1); r1-2 resolved in full (branch coverage attacked, holds);
  r1-3 resolved and reproduces under SR-12 re-measurement this
  window; r1-4 acknowledged, nothing owed.
adjudication: the OBJDOM-4 direction (fix-A of record at F2 entry;
  fix-B scoping interim) SURVIVES this round untouched; F-1/F-2 as
  pinned survive; all record magnitudes unaffected.
probes: esc_probe_objdom_etrunc_order.py exit 0 (4/4) re-run this
  window; esc_probe_objdom_evenp_iff.py exit 0 (4/4) NEW this window;
  both numpy-only, pinned env, re-runnable.
