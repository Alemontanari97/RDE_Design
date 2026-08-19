# SEED OUTCOME REGISTRY — longitudinal refuter-calibration record

Minted 2026-08-19 (S-FOUNDATIONS-C boundary touchpoint; user-ratified
R3 proposal (c)-first-half). PURPOSE: every dual-seed slot outcome is a
CALIBRATION DATUM of the adversarial verification layer — this registry
accumulates them so the layer's kill/confirm behaviour becomes a
measured curve, not an anecdote. One row per seed slot execution;
protocol docs remain the per-batch authority
(validation/sfoundations_raws_2026-08-13/r2pass/SEED_PROTOCOL_v2.md,
SEED_PROTOCOL_v3.md). Update discipline: append rows in the window that
runs the slots; never rewrite history (SR-10 style).

## Rows (chronological)

| # | date | protocol | slot | claim (compressed) | truth | delivery quality | refuter verdict | binary outcome | adjudicated cause |
|---|------|----------|------|--------------------|-------|------------------|-----------------|----------------|-------------------|
| 1 | 2026-08-17 | v1 (proofs-1 loop) | canary | "w is the streamline invariant" (axisym swirl) | FALSE | bare claim | BROKEN (r·w counterexample, machine-eps demo) | kill ✓ | content kill — layer kill-direction proven |
| 2 | 2026-08-17 | v1 | known-true | "Γ = r·w constant along streamlines" (bare hypothesis list) | TRUE | DEFECTIVE (no spaces, no falsifier, A1 force clause missing) | REPAIRABLE | confirm ✗ | SEED-AUTHORING defect (v1 packaging); over-strictness correctly applied by refuter |
| 3 | 2026-08-18 | v2 (label-matched) | canary [KT-1] | "planar vorticity ω constant along streamlines" (compressible barotropic) | FALSE | compliant packaging | BROKEN (ω/ρ derived; CK counterexample) | kill ✓ | content kill — second proof of kill direction |
| 4 | 2026-08-18 | v2 | known-true [KT-2] | Γ = r·w, repaired packaging | TRUE | DEFECTIVE IN ROUTE (L1 tangential-RH insufficient; L2 half-reduced display; L3 concatenation asserted) | REPAIRABLE | confirm ✗ | SEED-AUTHORING defect #2 (route elisions, judge-verified genuine) — NOT layer blindness |
| 5 | 2026-08-19 | v3 (pre-launch route audit, rule 7) | canary [KT-3] | "azimuthal vorticity ω_θ constant along streamlines" (axisym swirl-free) | FALSE | compliant (audit not applied to canary by design) | BROKEN (both seeded errors found: rotating-basis stretching + ω·div u; explicit-data counterexample; judge re-derived) | kill ✓ | content kill — third proof |
| 6 | 2026-08-19 | v3 | known-true [KT-4] | Γ = r·w, third delivery, full route | TRUE | COMPLIANT (4 audits: 3 genuine boundary defects repaired pre-launch — arc objects + S closedness; on-axis Step-2; axis dichotomy) | SOUND-AS-LABELED | confirm ✓ | LAYER CONFIRM DIRECTION PROVEN (first time) — v3 PASS both directions |

## Audit-chain sub-rows (v3 rule-7 instrument, same window)

| audit # | verdict | defect found (all judged genuine) |
|---|---|---|
| 1 | NON-COMPLIANT | arc objects undefined + S-closedness missing (Defect A/B) |
| 2 | NON-COMPLIANT | [w]=0 derivation ill-formed at on-axis points of S |
| 3 | NON-COMPLIANT | axis dichotomy (Step-1 identity consumed at axis points) unjustified |
| 4 | COMPLIANT | — (slots launched) |

## Calibration readings (as of 2026-08-19; re-read at every append)

- KILL direction: 3/3 — every false seed killed ON CONTENT with
  falsification at source. No form-kill ever observed on a canary.
- CONFIRM direction: 1/3 raw — but BOTH failures adjudicated
  SEED-AUTHORING defects (route elisions), each objection
  judge-verified true of the delivered text; ZERO observed instances
  of refuter blindness or of a refuter accepting a defective delivery.
- Instrument lesson (standing): the binding standard is symmetric —
  refuters hold seeds to the same bar as real claims; the confirm
  direction is testable ONLY with audited-compliant deliveries
  (protocol v3 rule 7 exists because of rows 2 and 4).
- Spend: ~0.4M subagent tokens across v2+v3 (protocols, 6 slots,
  4 audits, 1 repair agent) — one-time per pool configuration
  (v2 rule 5 / v3 rule 8: unchanged pool across waves = no re-seed).
