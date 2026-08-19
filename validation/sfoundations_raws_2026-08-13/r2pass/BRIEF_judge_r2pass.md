# JUDGE BRIEF — r2 batched adversarial pass (S-FOUNDATIONS-C, Blocco 1)

Role: judge of record for the confirmation round mandated by LG-1
(findings row `orchestration:until-dry-confirm-direction-unproven`),
condition C-2 of `VERDICT_contract_and_L4R1.md` and the §2 dryness gap of
`phaseD/VERDICT_phaseD_proofs1.md`. Authority: adjudicate per-objection;
DOWNGRADE-ONLY relative to the standing judge labels (you may NOT upgrade
any label; label restoration paths, e.g. D.18's G-f battery, are NOT
yours — they belong to their named carriers). Paths relative to
`validation/sfoundations_raws_2026-08-13/`.

## Inputs (read in full)

1. `r2pass/refute_r2batch_l0.md` and `r2pass/refute_r2batch_l1.md` — the
   two lens refutations of the 18-leg delta set (target list of record in
   `r2pass/BRIEF_refuters_r2batch.md`).
2. `r2pass/refute_SEEDv2_KT1.md`, `r2pass/refute_SEEDv2_KT2.md` — the
   dual-seed slots, protocol v2 (`r2pass/SEED_PROTOCOL_v2.md` holds the
   key and the binary criteria; read it AFTER reading the seed outputs).
3. The three target documents at the attacked legs (verify quotes; spot
   re-derive where an objection and the text disagree).
4. The two standing verdicts (for label context and dedup adjudication):
   `phaseD/VERDICT_phaseD_proofs1.md`, `VERDICT_contract_and_L4R1.md`.

## Adjudication rules

- null=failure: a missing/empty refuter or seed file = the pass FAILS for
  that slot; say so loudly; no silent dry-counting.
- SEED LAYER FIRST: apply SEED_PROTOCOL_v2 criteria
  (KT-1 must be BROKEN with positive falsification at source; KT-2 must
  be SOUND-AS-LABELED). Report `{canary_killed, knowntrue_survived}` in a
  prominent §1. If either fails, the layer stays unproven in that
  direction: state the consequence (every survived leg rests on YOUR
  reading, and the Blocco-2 landing gate stays CLOSED) — do not soften.
- Per objection: verdict in {SUSTAINED-BREAKS, SUSTAINED-REPAIR,
  SUSTAINED-AMENDMENT, OVERRULED (with your own derivation-level
  reason)}. Verify quotes against the document text; an objection that
  misquotes is OVERRULED on that ground with the correct text cited.
- Per leg 1..18: final adjudication in {CONFIRMED (no sustained
  objection; both lenses covered it), CONFIRMED-WITH-AMENDMENTS (name
  them; wording-class only), OBJECTION-SURVIVING (any sustained
  BREAKS/REPAIR item -> escalation per the standing rule: that leg goes
  to full form, Form-2/until-dry, and CANNOT land in M0 this window)}.
- Dedup adjudication: if a refuter re-opened a consumed finding, judge
  whether the disposition attack is genuine or a re-mint.
- Consequence mapping (state explicitly in the verdict):
  (a) legs 1-5, 12-18 CONFIRMED -> C-2/AUDIT-DEBT-r2 DISCHARGED for
      those labels; M0 promotion unblocked at the standing judge labels;
  (b) legs 6-11 CONFIRMED -> the proofs-1 §2 dryness gap is closed for
      the r3 text (D.18 stays THEOREM* modulo G-f: its ground-(1)
      internal-consistency downgrade is NOT lifted by this pass);
  (c) any OBJECTION-SURVIVING leg -> named escalation item with owner =
      this session's orchestrator, and the corresponding M0 landing item
      is HELD OUT of the Blocco-2 package.

## Output

Write `r2pass/VERDICT_r2pass.md`: §1 seed layer (prominent) -> §2
per-objection adjudication table -> §3 per-leg final table (1..18) ->
§4 consequence map (landing gate per item) -> §5 falsifiers for this
verdict itself. Then RETURN (as your final structured answer) the
machine summary requested by your task order.
