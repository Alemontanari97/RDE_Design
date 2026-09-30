# -*- coding: utf-8 -*-
"""CKP-S3-1 lean-register patch, batch 2 (specs_c12 C7-C12 + specs_c34)."""
from _patch_ckps31_a import patch

patch("specs_c12.py", [
 # C7-bis-pre cards
 ('''            cards=[
                ("Stechmann 2019 — 0-D per phase",
                 "blowdown per phase, declared mass-weighted mean — but on FIXED nozzle families"),
                ("Harroun 2021 — 2D-axi per phase",
                 "solutions at the cycle's pressure ratios, then averaged thrust coefficients — but the mean of a RATIO does not commute: on 10:1 cycles the bias is first-order in the variance, and the paper does not declare its weight"),
                ("Fievisohn — wave-frame MoC",
                 "the closest cousin: rotational MoC in the wave frame — never design, never a per-phase family"),
                ("This programme — the variational optimum ON the family",
                 "never posed before; our simplest reduction rung IS Stechmann's reduction level — with the correct mean PROVEN"),
            ],''',
  '''            cards=[
                ("Stechmann et al. 2019",
                 "0-D blowdown per phase, declared mass-weighted mean — on fixed nozzle families"),
                ("Harroun et al. 2021",
                 "2D-axi at cycle pressure ratios, then averaged thrust coefficients — but the mean of a ratio does not commute, and the weight is undeclared"),
                ("Fievisohn & Yu 2017",
                 "wave-frame method of characteristics — the closest cousin: never design, never a family"),
                ("This programme",
                 "the variational optimum ON the family — never posed before"),
            ],'''),
 # C7-bis theorem band
 ('''            theorem_band=("The deciding theorem: no single phase satisfies its own wall condition — the "
                          "weighted mean does. The cycle-optimal nozzle is optimal at no single operating "
                          "point; of three natural averages, only the weighted one is necessary — the others "
                          "fail outside one identified degenerate case."),''',
  '''            theorem_band=("The deciding theorem: no single phase satisfies its own wall condition — the "
                          "weighted mean does. The cycle-optimal nozzle is optimal at no single operating point."),'''),
 # C7-ter honesty band
 ('''            honesty_band=("Its size at contouring is open — and not presumed small: 10:1 imposed inlet swings, "
                          "~6:1 throat, ~20:1 combustor; the expert panel: 'the error could be large.' The "
                          "answering computation has not run: the machine is ready — first campaign of the "
                          "phase opening now."),''',
  '''            honesty_band=("Its size at contouring is open — not presumed small (10:1 inlet, ~6:1 throat, "
                          "~20:1 combustor swings). The machine is ready: it is the first campaign of the "
                          "phase now opening."),'''),
 # C8
 ('title="Within the declared data class, per-phase is not an approximation — it is a change of coordinates"',
  'title="Per-phase is not an approximation — it is a change of coordinates"'),
 ('''            bullets=[
                "For a pure periodic rotating wave — monitored on stagnation-temperature flatness — the flow is STEADY in the wave frame: the per-phase family is an exact quotient, with ONE declared approximation (Strouhal-order) and its hypotheses printed.",
                "The global time average — the field's — mixes the phases: it is the crudest reduction, not ours.",
            ],''',
  '''            bullets=[
                "In the declared class (pure rotating wave) the flow is steady in the wave frame: the family is an exact change of coordinates, with one declared approximation.",
                "The global time average mixes the phases — the cruder reduction, not ours.",
            ],'''),
 ('''            tag=("This step has a declared proof structure (equivariance route), "
                 "not yet the complete proof — and we write that on the slide."),''',
  '''            tag=("Proof structure declared; complete proof in progress — stated openly."),'''),
 # C9
 ('title="Same pressure trace, different thrust: what the average can and cannot see"',
  'title="Same pressure trace, different thrust"'),
 ('''            bullets=[
                "Two flows with the SAME pressure trace but different swirl and fluctuation content produce different thrust — established without a single CFD run: the pressure-only reduction is CONDEMNED (its final step carries a declared proof structure with its explicit premise — we distinguish it from the theorem).",
                "The full-state per-phase mean is EXONERATED on that axis. The stakes: 1.5–3% of thrust, with contributions up to 9% of pressure.",
                "Contract consequence: the field imposes only pressure at the boundary — that projection loses thrust information; our full-state contract IS the repair.",
            ],''',
  '''            bullets=[
                "Same pressure trace, different swirl content → different thrust — no CFD needed: a pressure-only description cannot rank designs.",
                "The full-state per-phase mean passes on this axis. Stakes: 1.5–3% of thrust.",
                "The field imposes only pressure at the boundary — our full-state contract is the repair.",
            ],'''),
 # C10
 ('title="What the reduction drops is an explicit operator — measurable, not hoped small"',
  'title="What the reduction drops is explicit — and measurable"'),
 ('''            bullets=[
                "What the reduction discards is not a hope: it is an EXPLICIT operator, with machine-verified identities; its mean channel is exactly ZERO — proven.",
                "At first order exactly two channels survive: the jumps at the fronts (the declared HEEL: their size has no number yet) and the covariance.",
                "The residual is not 'negligible' — it is MEASURABLE, and the campaign that measures it is the first of the phase opening now.",
                "The published face: instantaneous lateral force is 25–35% of axial, rotates at wave frequency — and averages to zero.",
            ],''',
  '''            bullets=[
                "The discarded terms form an explicit operator; its mean channel is exactly zero — proven.",
                "Two first-order channels survive: front jumps (no number yet — our declared weak point) and covariance.",
                "Both are measurable — the first campaign of the new phase measures them.",
                "Published face: lateral force 25–35% of axial, rotating, averaging to zero.",
            ],'''),
 # C11
 ('title="Our honesty table: the residual error, channel by channel"',
  'title="The residual error, channel by channel"'),
 ('''            bullets=[
                "Channels do not sum. Best case: single-digit percent plausible; off-axis, above 10% is not excluded.",
                "Our one in-class number (+0.51%) carries ~30% uncertainty — against Rao's classical 0.04–0.34% (their numbers).",
                "No external referee exists for this error: we close the bracket, or it stays open.",
            ],''',
  '''            bullets=[
                "Channels do not sum. Best case: single-digit %; off-axis, >10% not excluded.",
                "Our one in-class number: +0.51% ± ~30% — Rao's classical scale: 0.04–0.34%.",
                "No external referee exists: we close the bracket, or it stays open.",
            ],'''),
 # C12
 ('title="The worst-direction marker is published: a shroud worth 13 points of ideal"',
  'title="The largest adverse signal is published: a shroud worth 13 points"'),
 ('''            bullets=[
                "Adding a shroud lifts a plug from 58.1% to ~71.5% of ideal at FIXED area ratio — more than the entire area-ratio design line, unexplained by the authors.",
                "We keep it on record as a candidate swirl-breaker.",
            ],''',
  '''            bullets=[
                "A shroud lifts a plug from 58.1% to ~71.5% of ideal at fixed area ratio — unexplained by the authors.",
                "On record as a candidate swirl-interaction effect.",
            ],'''),
])

patch("specs_c34.py", [
 # C13-pre
 ('title="Why an adjoint, which one — and how the machine can say no"',
  'title="Why an adjoint, which one — and how results are checked"'),
 ('''            cards=[
                ("ADJOINT",
                 "one extra solve gives the gradient with respect to ALL design freedoms at once — and it is not a modern idea: Hoffman's 1967 multiplier fields, along the same characteristics"),
                ("DISCRETE-EXACT",
                 "we differentiate EXACTLY the problem the computer solves: the backward gradient IS the transposed adjoint of the march — an algebraic identity verified to machine precision. Optimality understood in the continuum; the number computed with zero gradient approximation"),
                ("OPTIMIZER",
                 "segmented trust-region Newton with MEASURED curvature — chosen for robustness on kinked-curvature problems and for certifiable steps, against weighed, documented alternatives"),
                ("CERTIFICATE",
                 "every condition checked a posteriori with a DERIVED threshold — never a magic number — plus independent oracles that can REJECT"),
            ],''',
  '''            cards=[
                ("ADJOINT",
                 "one extra solve → the gradient for all design variables at once (Hoffman 1967's multiplier fields)"),
                ("DISCRETE-EXACT",
                 "we differentiate exactly the problem the computer solves — identity verified at machine precision"),
                ("OPTIMIZER",
                 "trust-region Newton with measured curvature — robust, certifiable steps; alternatives weighed"),
                ("CERTIFICATE",
                 "conditions checked with derived thresholds + independent checks built to reject"),
            ],'''),
 # C13-val
 ('''            bullets=[
                "On the classical maximum-thrust problem, our optimizer — exact adjoint + trust-region Newton, a route fully independent of the classical construction — RECOVERS Rao's contour: max deviation ~2·10⁻³ of the throat radius, inside the derived cross-code error band.",
                "Two independent routes, one contour: the new method rests on a machine that already passes the benchmark the field recognizes.",
            ],''',
  '''            bullets=[
                "By a route independent of the classical construction, the machine recovers Rao's contour: max deviation ~2·10⁻³ of throat radius.",
                "Two routes, one contour — the field's benchmark, passed.",
            ],'''),
 # C13
 ('title="From theory to a design machine: every choice on the record, with its falsifier"',
  'title="From theory to a design machine: every choice on record"'),
 ('''            bullets=[
                "Eight stages, from the data contract to the final verdict — every algorithmic choice is on the register: the adjudicated ones carry weighed alternatives and a falsifier; the ones NOT yet taken are declared too, with owner and window. The graph shows what we have not decided.",
                "And the comparison with the field: no published design method delivers its result inside a verification chain built to reject it.",
            ],''',
  '''            bullets=[
                "Eight stages, data contract → verdict; adjudicated choices carry weighed alternatives and a test that can reject them — open ones are declared, with owner and window.",
                "No published design method ships inside a chain built to reject it.",
            ],'''),
 # C14
 ('''            bullets=[
                "The driver: segmented trust-region Newton on a discrete-exact gradient.",
                "Said openly: this cluster will be re-examined at the next phase entry — a 2026 replacement candidate is named, with a pre-registered comparison at equal constraints. The solver census is dated, and we declare it.",
            ],''',
  '''            bullets=[
                "The driver: segmented trust-region Newton on an exact gradient.",
                "Declared: this cluster is re-examined at next phase entry — 2026 candidate named, comparison pre-registered.",
            ],'''),
 # C15
 ('title="How the machine knows it is not lying"',
  'title="How results are verified: certificates that can fail"'),
 ('''            bullets=[
                "The gradient is exact for the discrete problem actually solved — verified at machine precision and independently cross-checked against a second code, with negative controls that reject.",
                "Every certificate has a DERIVED threshold — and the threshold bites: halving it flips the verdict. A certificate that cannot fail is not a certificate.",
                "Discretization error has its own estimator with an independent referee; model error its per-channel bracket — never mixed. The front uses the only scheme that can carry a gradient certificate — for a published reason (Giles–Ulbrich).",
                "No result leaves the machine alone: contour, certificates, bars and verdict travel together.",
            ],''',
  '''            bullets=[
                "Gradient exact for the discrete problem; cross-checked on a second code, with negative controls.",
                "Thresholds are derived, and they bite: halving one flips the verdict.",
                "Discretization and model error never mixed — each has its own estimator or bracket.",
                "Results ship together: contour, certificates, bars, verdict.",
            ],'''),
 # C16
 ('''            footline="Every acceleration lever passed an invariance gate: same results, certificates included. Our measurements, on a declared host.",''',
  '''            footline="Every speed lever passed an invariance gate: same results, same certificates. Our measurements, host declared.",'''),
 # C16-bis
 ('title="The machine that says NO — to us"',
  'title="We commissioned a hostile audit — and the chain failed us"'),
 ('''            timeline_cards=[
                ("Audit 1 — self-check threat", "we built the way our self-check could lie, exhibited it with a negative control, closed it with a solver-independent verification"),
                ("Audit 2 — hostile, commissioned", "verdict: NOT CERTIFIABLE — two named defects: one repaired immediately and declared, one with an owner and a deadline"),
            ],
            bullets=[
                "Every audit passes only if it confirms truth AND rejects falsehood — a purpose-built decoy WAS rejected before the verdict counted.",
                "Cross-code agreement is never treated as truth: claims rest on invariants independent of both codes.",
                "Between the two audits, defects migrated from the certified object to the certifier: the floor rose. The system works because it fails us.",
            ],''',
  '''            timeline_cards=[
                ("Audit 1 — self-check threat", "we built the way our self-check could fail silently, exposed it, closed it with a solver-independent verification"),
                ("Audit 2 — hostile, commissioned", "verdict: not certifiable — two named defects; one repaired and declared, one with owner and deadline"),
            ],
            bullets=[
                "Audits must also reject falsehood: a planted decoy was rejected before verdicts counted.",
                "Cross-code agreement is never treated as truth.",
                "Across the audits, defects moved from the object to the certifier: the floor rose.",
            ],'''),
 # C17-pre
 ('title="Which gap dominates? — the honest map"',
  'title="Which gap dominates — the honest map"'),
 ('''            hypothesis=("Working hypothesis — declared, falsifiable, not a theorem: at fixed constraints the "
                        "formulation gap dominates (three suppression results on the smooth model gap; none on "
                        "the formulation gap)."),
            heel=("Always said with its heel: front jumps are the unsuppressed first order of the model gap — "
                  "no number yet; if large, the model can dominate anyway."),
            death_line=("Programme death needs TWO independent failures, each measurable: the head-to-head "
                        "(cheap, runs first) and the residual legs."),''',
  '''            hypothesis=("Working hypothesis (declared, falsifiable): at fixed constraints the formulation "
                        "gap dominates — three suppression results on the model gap, none on formulation."),
            heel=("Stated with its weak point: front jumps are unsuppressed — no number yet; if large, the "
                  "model gap can dominate."),
            death_line=("Programme failure needs two independent misses — both measurable: head-to-head + "
                        "residual measurement."),'''),
 # C17
 ('''            kill_line=("Honest death criterion: measured gain below ~1% Isp → the programme pivots — it does "
                       "not insist."),''',
  '''            kill_line=("Declared stop criterion: measured gain below ~1% Isp → pivot to certification & "
                       "operability."),'''),
 # C17-bis
 ('''            intro=("The head-to-head choice IS taken: no pre-milestone number — the machine is ready and the "
                   "comparison is the first campaign of the phase (previous slide)."),''',
  '''            intro=("The head-to-head choice is taken: no pre-milestone number — it runs as the first "
                   "campaign of the phase."),'''),
 # C19
 ('title="A method you can audit — and a machine fast enough to make validation economic"',
  'title="A method you can audit — fast enough to validate economically"'),
 ('''            closing=("Our honesty is not a disclaimer: it is instrumented inside the method — you saw the "
                     "limits written on the slides, with their evidence levels."),''',
  '''            closing=("Honesty here is not a disclaimer — it is built into the method: limits stated on "
                     "the slides, with their evidence levels."),'''),
])
print("BATCH 2 DONE")
