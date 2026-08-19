# DUAL-SEED PROTOCOL v3 — S-FOUNDATIONS-C, escalation E-5 of VERDICT_r2pass.md

Date: 2026-08-18. Supersedes v2 (`SEED_PROTOCOL_v2.md`) per the r2-pass
judge's E-5: the v2 known-true FAILED AGAIN (REPAIRABLE), adjudicated a
SEED-AUTHORING defect — three judge-verified genuine route elisions in
the delivered brief (VERDICT_r2pass.md §1: L1 tangential-RH insufficient
without mass RH + m ≠ 0; L2 half-reduced opening display; L3 asserted,
not constructed, cross-shock concatenation) — the second delivery-defect
instance of the same class, NOT demonstrated refuter blindness (kill
direction proven twice; all KT-2 objections true of the delivered text).

## Rules (v3 = v2 rules 1-6 UNCHANGED, plus:)

7. PRE-LAUNCH ROUTE AUDIT (the E-5 machine constraint): the known-true
   seed's PROOF ROUTE is audited against the binding standard by an
   agent OTHER than the seed author BEFORE launch — every displayed
   equation correct as labeled (general vs reduced), every reduction
   step justified from a named hypothesis, discontinuity handling
   CONSTRUCTED not asserted, hypotheses minimal-and-complete, falsifier
   present. Audit failure = the seed does not launch until repaired (by
   a third agent, never the refuter pool) and re-audited. The canary is
   NOT route-audited (its route error IS the payload; its packaging
   follows the same form).
8. A dual-seed layer certification is spent per POOL configuration
   (v2 rule 5); the v3 run certifies the escalation-round refuter pool
   and, on PASS, discharges LG-1's confirm direction for this window.

## Seed key for the v3 batch

- [KT-3] = CANARY (false). Azimuthal vorticity omega_theta claimed
  constant along streamlines in steady axisymmetric SWIRL-FREE
  barotropic flow. False on content: the correct streamline invariant
  is omega_theta/(r*rho) (Helmholtz/potential-azimuthal-vorticity
  class); the supplied route (i) silently drops the omega*(div u)
  compressibility term from the curl of the momentum equation and
  (ii) claims (omega . grad)u = 0 "by axisymmetry", ignoring that the
  rotating basis vector e_theta makes (omega . grad)u =
  (u_r omega_theta / r) e_theta != 0 — the geometric stretching term.
  Packaging deliberately compliant: the kill must be on mathematics.
- [KT-4] = KNOWN-TRUE. The Gamma = r*w axisymmetric streamline
  invariant, THIRD delivery, with the three v2 elisions REPAIRED in the
  route: (L2) the general azimuthal component displayed IN FULL
  (both theta-terms present) before axisymmetry is applied; (L1) the
  shock step closed from RH mass [m]=0 PLUS m != 0 PLUS tangential
  momentum [m w]=0 => [w]=0 (slip surfaces m = 0 handled by
  non-crossing); (L3) the cross-shock streamline concatenation
  CONSTRUCTED (transversal crossings at isolated parameter values;
  one-sided limits matched by [Gamma]=0 pointwise on the surface).

## Success condition (unchanged, binding)

canary_killed (BROKEN with falsification at source) AND
knowntrue_survived (SOUND-AS-LABELED). On PASS: LG-1 confirm direction
discharged for this window; the r2-pass escrow (VERDICT_r2pass.md §4)
releases and the Blocco-2 landing gate OPENS for confirmed items. On
FAIL: gate stays closed; a third consecutive known-true failure with a
PRE-AUDITED route would re-attribute the failure toward layer
miscalibration and trigger the full-scope re-adjudication of
VERDICT_r2pass.md §5 (second falsifier).

## RESULT OF RECORD (2026-08-19, run wf_c8d2299f-f92)

**PASS — layer proven in BOTH directions this window.**
- Audit chain: audits 1-3 each found a GENUINE boundary-class delivery
  defect (arc-object definitions + S closedness; on-axis Step-2 clause;
  Step-1 axis dichotomy), each repaired; audit 4 = COMPLIANT. The
  rule-7 instrument did its job three times before launch.
- [KT-3] canary: **BROKEN** — kill ON CONTENT at source: refuter found
  BOTH seeded route errors independently (Error A: (omega.grad)u =
  (u_r omega_theta/r) e_theta != 0 by the rotating basis — the
  geometric stretching; Error B: dropped omega(div u) term), derived
  the correct invariant omega_theta/(r rho), built an explicit-data
  local analytic counterexample, and verified no hypothesis reading
  excludes it (refute_SEEDv3_KT3.md).
- [KT-4] known-true: **SOUND-AS-LABELED** — survival at label on the
  third delivery (refute_SEEDv3_KT4.md).
- CONSEQUENCE: LG-1 (orchestration:until-dry-confirm-direction-
  unproven) confirm direction DISCHARGED for this window (registry row
  update rides the Blocco-2 landing window per R7); the VERDICT_r2pass
  §4 escrow is RELEASABLE, gate opening composed with
  VERDICT_escalation.md (per-doc dryness + leg labels).
- SR-9 weight of the seed line (cumulative, v2+v3): 2 protocol docs,
  4 slot runs, 4 audits (3 fail + 1 pass), 1 repair agent, 2
  orchestrator repairs; ~0.4M subagent tokens.
