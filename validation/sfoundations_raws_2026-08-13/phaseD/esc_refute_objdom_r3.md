# ESCALATED REFUTATION r3 — PHASE D MINOR (b) [OBJ-DOM]
# S-FOUNDATIONS-C4 escalation window, 2026-08-20. Role: ESCALATED
# REFUTER, single fused lens (math structure + carrier/bookkeeping
# contracts), round 3 (full form), per VERDICT_blocco2.md SS2.2/SS3
# E-2 and BRIEF_blocco2_phaseD_addendum_c4.md. Target: the round-3
# REVISED phaseD_minor_objdom.md (all [ESC-r3-0..1] markers + SS8
# disposition table), against esc_refute_objdom_r2.md,
# esc_refute_objdom_r1.md, refute_minor_objdom.md, and VERDICT_blocco2
# SS2.2/SS4 (read in full this window). This slot writes ONLY this
# file. Zero inflation: no actionable finding survives this round;
# everything checked is in the VERIFIED-SOUND note (ESC-OBJDOM-r3-1).
#
# Probes of record (BOTH re-run in THIS window, my own executions):
#   esc_probe_objdom_etrunc_order.py — exit 0, 4/4 rejectors PASS
#     (generic slope 3.0000; even slope 6.0002; coefficient ratio
#     1.0000/…/0.9999 across the sweep; rel-mismatch slope 1.001,
#     |rel|·tilt = 3.5 J-units/rad SCALING-ESTIMATE line reproduced;
#     endpoint/trap ratio −2 … −2.0001).
#   esc_probe_objdom_evenp_iff.py — exit 0, 4/4 rejectors PASS
#     (cubic p'(0)=0 slope 5.0071; coefficient ratio → 1.0007; even-p
#     slope 5.9986; generic slope 3.0000).
# All figures match those quoted in the round-3 revision (5.007,
# 1.0007, 5.999, 3.0000 — correct roundings of my measured outputs).

## PRIOR-OBJECTION RESOLUTION (r1 + r2 findings, verified in this window)

- ESC-OBJDOM-r1-1 (BREAK): RESOLVED IN FULL as of round 3 — the
  generic order statement was fixed in r2 (verified then and
  re-checked now: E_trunc = -(pi/6)*rtd*p'(0)*yt*th1^3 + O(th1^4),
  O((Dy)^{3/2}) cusp class, proof sketch off the inapplicable C^2
  bound), and the residual false IFF that r2 found in that fix is now
  ALSO fixed (see r2-1 below). No residue remains.
- ESC-OBJDOM-r1-2 (REPAIR): RESOLVED (r2 verdict carried; persisting
  checks re-done this window): P-1(1)+(2) dual declaration duty in
  place; F-1 three-branch. Branch (i) closed-form derivative
  re-derived independently — d/dthB = (1/n_B)*d/dth1 of (a.1) by
  product + Leibniz with y' = rtd*sin(th1) and p(0) plan-frozen
  (frozen-plan hypothesis carries n_B fixed, so (1/n_B) is
  legitimate): matches the printed formula symbol-for-symbol. Branch
  (ii) re-derived (G' = y*rtd*sin; modeling term
  2*pi*p'(th1)*G(th1)/n_B; relative (p'/2p)*th1: G ~ rtd*yt*th1^2/2
  against main p*y*rtd*th1 checks). The r2 item-7 degeneracy
  re-verified ANALYTICALLY this window: endpoint-p + trapezoid-in-y
  collapses exactly to branch (ii) because G(th1) =
  Int_0^{th1} y*rtd*sin dth = Int_{yt}^{y1} y dy = (y1^2 - yt^2)/2
  identically and the trapezoid of the linear integrand y in y is
  exact — so 2*pi*0.5*p(th1)*(yt + y1)*(y1 - yt) = 2*pi*p(th1)*G(th1).
  No uncovered combination.
- ESC-OBJDOM-r1-3 (AMENDMENT): RESOLVED and STILL ACCURATE — SR-12
  re-measure THIS window: docs/findings_registry.yaml:209 still
  carries the drifted anchors [":516-522", ":1130-1137"]; :213 still
  carries no LB-6(b) append. The [ESC-r2-3]
  ordered-not-yet-applied sentence remains true as dated and as of
  this read; consistent with SS0. (The landing remains owed to the
  orchestrator — bookkeeping state unchanged across all three rounds.)
- ESC-OBJDOM-r1-4 / ESC-OBJDOM-r2-2 (NOTEs): nothing was owed;
  correctly acknowledged in SS7/SS8.
- ESC-OBJDOM-r2-1 (BREAK): RESOLVED — the false biconditional
  "O(th1^6) IFF p'(0)=0" is replaced at ALL THREE anchor sites
  (SS1 (a.2); SS6 row MIN-OBJDOM-1 echo; SS7 row ESC-OBJDOM-r1-1
  echo — the [ESC-r3-1] marker sweep of the file shows markers at
  exactly the declared sites: header :28/:38, (a.2) :128, SS6 :520,
  SS7 :553, SS8 :578/:582, and nowhere else, confirming the
  "nothing else touched" claim). Soundness of the adopted repair
  verified independently below (note item 1). The SS7 echo's
  compressed form "p'(0)=0 alone gives O(th1^5)" is TRUE as a
  big-O upper-bound statement (attained generically, i.e. whenever
  p'''(0)!=0; smaller when p'''(0)=0 too — an upper-bound class
  violates nothing), and the full qualified statement lives at the
  primary site (a.2) — no defect.

## FINDINGS

### ESC-OBJDOM-r3-1 [NOTE] — VERIFIED-SOUND record (coverage; all
checks in THIS window, at source, by probe execution, or by
independent re-derivation). NO actionable finding: this round is DRY.

1. THE [ESC-r3-1] REPAIR IS SOUND — the corrected biconditional
   verified in BOTH directions by independent derivation (monomial
   decomposition of E_trunc, which is linear in p, under th(y) =
   sqrt(2(y-yt)/rtd)*(1 + O(y-yt)); single-interval trapezoid error
   of u^s on [0,h] = h^{s+1}*(1/2 - 1/(s+1))):
   - th^1 term (s = 1/2): error coefficient (1/2 - 2/3) = -1/6,
     giving -(1/6)*p'(0)*yt*sqrt(2/rtd)*Dy^{3/2} =
     -rtd*p'(0)*yt*th1^3/12, x2*pi = -(pi/6)*rtd*p'(0)*yt*th1^3 —
     the generic O(th1^3) statement reconfirmed (nonzero coefficient:
     yt > 0, rtd > 0).
   - th^3 term (s = 3/2): error coefficient (1/2 - 2/5) = 1/10,
     giving (1/10)*p3*yt*(2/rtd)^{3/2}*Dy^{5/2} =
     rtd*p3*yt*th1^5/20, x2*pi = (pi/10)*rtd*p3*yt*th1^5 with p3 =
     p'''(0)/6 — the O(th1^5) branch and its printed coefficient
     (pi/10)*rtd*(p'''(0)/6)*yt EXACT (probe rejector [2] ratio →
     1.0007 reproduced this window).
   - th^5 term (s = 5/2): error coefficient (1/2 - 2/7) = 3/14,
     order Dy^{7/2} = O(th1^7) — the revision's NEW clause beyond the
     r2 refuter's named repair ("full evenness sufficient but
     stronger than necessary — odd th^5 terms … O(th1^7), below the
     th1^6 threshold") is attacked as new-text-of-this-revision and
     VERIFIED CORRECT: O(th1^7) is higher order than th1^6, so p5
     need not vanish; exactly the first TWO odd derivatives must.
   - Even powers of th are analytic functions of y (1 - cos th =
     (y-yt)/rtd inverts analytically for th^2), so the even part
     contributes the standard O(Dy^3) = O(th1^6); linearity of
     E_trunc in p forbids cross-terms. Hence, for the smooth
     kernel/fan arc flow: E_trunc = O(th1^6) <=> p'(0) = 0 AND
     p'''(0) = 0 — the adopted clause is the true characterization;
     "p even in th through cubic order" is its correct paraphrase.
2. BOTH probes re-executed by THIS refuter (not merely trusted):
   exit 0, 4/4 rejectors each; every figure quoted in [ESC-r3-0],
   (a.2), and SS8 matches my measured outputs at correct rounding
   (5.0071→5.007, 5.9986→5.999, 3.0000, 1.0007, 1.001, −2). The
   SS8 hand-expansion (trap/(2pi) = p3*yt*rtd*th1^5/4 vs
   integral/(2pi) = /5; difference x2*pi = (pi/10)*rtd*p3*yt*th1^5)
   re-done: 1/4 − 1/5 = 1/20 — correct.
3. Repair-site completeness: all three anchor sites named by
   ESC-OBJDOM-r2-1 carry the correction; marker sweep (item above)
   confirms NO unmarked edits — the unchanged-by-design list
   ((a.1)/(b)/(c), generic (a.2) order + coefficient, F-1 three
   branches, F-2 both paths, OBJDOM-2/3/4, adjudication DIRECTION,
   SS3 duties, SS4 landing text still PROPOSED per [ESC-r1-9]) is
   honored. Spot-checks of passages quoted verbatim by the r1/r2
   refuters (F-1 branch (i)/(ii) formulas, F-2 [ESC-r1-8] Dv text,
   §3 trigger header) reproduce unchanged.
4. SR-12 re-measurements at source, this window:
   docs/findings_registry.yaml:204-213 read — :209 drifted anchors
   persist, :213 un-appended (item r1-3 above); :212 trigger text
   matches the §3 header quote CHARACTER-EXACT (including the
   "; discharge test = the audit's analytic throat-panel A/B" tail).
5. Code anchors re-verified in the current tree:
   validation/a1_toc_variational_jax.py:22-27 header objective
   "(0, theta_B]" + Pa-drop clause; :530-534 stations k = 1..n_B (no
   theta=0 station; y = yt + rtd*(1-cos th) exact arc); :1179-1186
   thrust_J trapezoid in y over supplied points with 2*pi prefactor.
   All as stated in SS0 and consumed by (a.1).
6. Arithmetic of record re-checked: 5.36e3/9.3 = 576 → 5.8e2; /6 →
   96x; fallback threshold form tilt_phys/(10*gtol) > 6 consistent
   with the 96x record operation. Dv direction: u = W/Dv => dJ/du =
   (dJ/dW)*Dv_thB — multiplication, as pinned (audit :529 convention
   re-read).
7. Bookkeeping contracts: SS8 covers both r2 findings (1 BREAK FIXED,
   1 NOTE acknowledged — matches the r2 machine summary tallies);
   CONTESTED: none is accurate (the finding was probe-true);
   single-file discipline respected (no new author files; no new
   probe written, correctly — the r2 counterexample probe already
   carries firing rejectors); round-3 read-depth declaration present
   and honest (prior-window VERDICT read carried + anchors
   re-consulted — acceptable under the context-usage discipline for
   a same-slot continuation); PAPERS NEEDED (empty) remains
   legitimate (internal adjudication; the r22 arrivals corpus bears
   on minors (a)/(d), not on this domain decision — re-checked).
8. Conclusion-preservation confirmed: nothing of record consumes the
   p'(0)=0 branch (declared EXTRA hypothesis, invoked nowhere); no
   F-1 branch prediction uses E_trunc's order; no record magnitude
   moved in round 3; the OBJDOM-4 adjudication DIRECTION (fix-A of
   record at F2 entry; fix-B scoping interim) stands exactly as at
   VERDICT_blocco2 SS2.2's expectation, now with the (a.2) branch
   ladder fully correct.

## READ-DEPTH DECLARATION (this window)

All internal, no papers consulted: phaseD_minor_objdom.md [FULL]
(round-3 revised, all markers); esc_refute_objdom_r2.md [FULL];
esc_refute_objdom_r1.md [FULL]; refute_minor_objdom.md [FULL];
VERDICT_blocco2.md [FULL] (SS2.2 + SS3 E-2 + SS4 the mandate
sections); docs/findings_registry.yaml:200-217 [FULL];
validation/a1_toc_variational_jax.py:18-31, :526-537, :1175-1187
[FULL at ranges]; both probe sources [FULL] + both EXECUTED this
window (exit 0 each, outputs quoted in the header).

PAPERS NEEDED: (empty)

## MACHINE SUMMARY

findings: 0 BREAK, 0 REPAIR, 0 AMENDMENT, 1 NOTE (ESC-OBJDOM-r3-1
  verified-sound coverage, items 1-8; includes independent
  both-direction verification of the corrected biconditional and of
  the revision's new beyond-named-repair O(th1^7) clause).
dry: TRUE — round 3 finds no actionable defect; the escalation loop's
  until-dry condition is met at this lens. Closure-judge ready.
prior_objections: r1-1 resolved in full (its r2 residue r2-1 now
  fixed); r1-2 resolved (branch (i)/(ii) re-derived, degeneracy
  identity re-proven analytically); r1-3 resolved and reproduces
  under SR-12 this window (registry landing still owed to the
  orchestrator, correctly stated as ordered-not-applied); r2-1
  resolved at all three anchor sites with sound repair; r1-4/r2-2
  nothing owed.
adjudication: the OBJDOM-4 direction (fix-A of record at F2 entry;
  fix-B scoping interim) SURVIVES round 3 untouched; F-1 three-branch
  and F-2 both-path falsifiers stand as pinned; all record magnitudes
  unaffected; the §4 landing text remains PROPOSED pending the
  escalation closure judge.
probes: esc_probe_objdom_etrunc_order.py exit 0 (4/4) and
  esc_probe_objdom_evenp_iff.py exit 0 (4/4), BOTH re-run by this
  refuter this window; numpy-only, pinned env, re-runnable as claimed.
