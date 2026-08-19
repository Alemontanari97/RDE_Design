# DUAL-SEED PROTOCOL v2 (repaired) — S-FOUNDATIONS-C, Blocco 1(a)

Date: 2026-08-17. Repairs the seed-design defect adjudicated of record in
`phaseD/VERDICT_phaseD_proofs1.md` §1 and carried by findings-registry row
`orchestration:until-dry-confirm-direction-unproven` (LG-1): the v1
known-true seed was delivered as a bare claim (no hypothesis list, no
function space, no falsifier), so a correctly-calibrated refuter applying
the binding standard was FORCED to return REPAIRABLE on a true statement —
a protocol defect, not a layer defect. The known-true failed twice for
over-strictness; the kill direction was proven both times.

## Rules (v2, binding for every dual-seed batch from this window)

1. SINGLE-CLAIM seeds: each seed slot carries exactly ONE claim. Never
   fused legs (truth-judgment and label-judgment must not be entangled by
   the seed's own packaging).
2. LABEL-MATCHED delivery: the seed claim is delivered AT the standard its
   rigor label requires — explicit hypothesis list, named function spaces,
   regularity clauses, EOS/gamma status declared, FALSIFIER attached, and
   the author's proof route supplied. Consequence: the canary can die ONLY
   on content (its packaging is compliant), and the known-true's survival
   is DECIDABLE (nothing formal left to refuse).
3. Binary criteria (unchanged from v1, now decidable):
   - canary (false claim)      -> required refuter verdict: BROKEN, with
     positive falsification at source;
   - known-true (true claim)   -> required refuter verdict:
     SOUND-AS-LABELED (REPAIRABLE now counts as layer failure: per the
     proofs-1 judge falsifier §6, a repaired known-true failing again
     indicates blindness/miscalibration and forces re-adjudication of
     every survived label of the loop it certifies).
4. Seed slots are DEDICATED agents receiving the same refutation-brief
   form as real slots; filenames and brief text carry no tell. The
   canary/known-true key lives only in this protocol file and in the
   judge brief.
5. Seeding is tied to the CONFIGURATION of the verification pool, not to
   waves: one dedicated pair per DISTINCT pool; unchanged pool across
   waves = no re-seed (session prompt, Blocco 3 rule 6).
6. null=failure accounting unchanged.

## Seed key for THIS batch (r2 batched adversarial pass)

- [KT-1] (planar vorticity streamline invariance, compressible barotropic)
  = CANARY. False on content: the supplied curl-of-momentum route silently
  drops the omega*div(u) stretching term; in compressible planar
  barotropic flow the streamline invariant is omega/rho, not omega. The
  packaging (hypotheses, spaces, falsifier) is deliberately compliant:
  the kill must happen on mathematics.
- [KT-2] (Gamma = r*w streamline invariance, axisymmetric, repaired
  delivery) = KNOWN-TRUE. This is the v1 seed's mathematical core
  re-delivered WITH the four repairs the v1 refuter itself named (A1
  no-azimuthal-force clause, A2 function spaces + RH lemma, A3
  EOS-free demotion of the gas clause, A4 falsifier). Using the repaired
  form of the SAME claim executes the proofs-1 judge's own §6 falsifier
  for the §1 weighing verbatim.

## Success condition for the layer this batch

canary_killed = TRUE AND knowntrue_survived = TRUE. Any other outcome:
the layer stays UNPROVEN in the failing direction, the LG-1 row stays
OPEN, and no M0 landing may consume the r2-pass confirmations (Blocco 2
gate stays closed).
