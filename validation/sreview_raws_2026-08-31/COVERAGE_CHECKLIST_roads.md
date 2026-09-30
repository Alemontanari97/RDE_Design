# COVERAGE CHECKLIST — road families and pin table for the ROAD judge ONLY (never shown to a de-novo deriver; S-REVIEW 2026-09-05, carrier §G.2 + refuter PROMPT-27/39/41)

Applied AFTER Stage A by the ROAD (SP0) diff judge: a road family absent
from all four de-novo trees is added by the judge, marked
"orchestrator-seeded", and its weight is reported SEPARATELY from the
derived roads. A road = TUPLE (objective; time treatment; spatial
representation; solver + information for the optimizer; search strategy +
guarantee class; decisive result); (a)-(e) differ on the time/
representation axes, (f) on the objective axis, (g) on the design-variable
axis, (h) is any hybrid stated as a tuple with different DESIGN and
EVALUATION entries. Distinct = differs in >= 1 entry.

| id | road family (user list §G.2) | record status (cite-only) |
|---|---|---|
| (a) | mean-state steady design + unsteady verification (the RDE literature's practice) | comparator arm C of the TWIN (§4); T3 says WHY it works on full-flowing walls |
| (b) | cycle-averaged functional with per-phase decomposition (the program's road) | M0 Part I-II; VI.4bis(i)(ii); rung 2 of Part V |
| (c) | direct unsteady optimization with time-domain adjoint | Part V row 2 (RPO/space-time tier, PRACTICE); O5 oracle; C60 SAND re-entry note |
| (d) | STEADY optimization in the wave frame (3-D helical field; B-lite/route-B; azimuthal dynamics exact, no St) | M0 Part V [S-BLITE] :3027-3044 (backstop, never the road); C51 NEVER; S-T0P/T-T0P quotient claims |
| (e) | ROM / space-time / data-driven surrogates + global optimization | C57 alternatives (adjoint-free at genuine best); no record instance |
| (f) | robust optimization over the envelope (cases D-F) — if the true lever is operability, not cycle-vs-mean | Annex B cases D-F; PB-5; C55 NEVER; P_amb slot |
| (g) | alternative physical levers as the primary object (base pressure, truncation, temporal dual-bell) | C61 NEVER (Veen WG10-FAILED), H20 homeless, N1 temporal dual-bell channel, ADR-D4 truncation band |
| (h) | hybrids — DESIGN per-phase, EVALUATE both arms in the wave frame (St-free delta at evaluation level; per-phase residual touches only the argmax) — the user's example; the record's objects [T-RED]/OPTSHIFT/M-RED make this a CLAIM WITH FALSIFIER, not a premise (refuter PROMPT-35) | [T-RED] M0 :1734; OPTSHIFT (decision map Stage 7: routes license NO number); M-RED campaign row |

## Pin table (level 3; T2 provisional, PENDING-USER): per road, which pins it NEEDS and which it RELAXES

| pin | statement §1 status | record home |
|---|---|---|
| P-WAVE pure periodic single-mode rotating wave, fixed n | USER PIN with monitor (T0 flatness, SPECIFIED not armed) | D-MU scope note; VI.4bis; H-A1 |
| P-GAS frozen thermally-perfect mixture, single phase | USER PIN | scope-pins memory; tables backend; H-E4 |
| P-DATA class A specs-only for the decisive test | TWIN §3 (flip clause) | Annex B case A |
| P-AXI axisymmetric walls and control surfaces | H-A2 | D1 §9 |
| P-PA constant ambient per operating point | H-Pa DISCHARGED as theory hypothesis (case-D product measure) | D1 §9 pass-2 note |

Road (d) is exact ONLY under P-WAVE; road (f) exists only if P-WAVE is
relaxed to a mode measure; road (b) needs P-WAVE for T0 and the O(St)
corrector for its bar; road (a) needs none of them but answers a narrower
question. The ROAD judge states this per road with the tree evidence.

## Measured scoping input (§H.2): [X-STSC] 2026-09-05
bell (L = 4 yt) St_n in [0.35, 0.60] at the record head count (MARGINAL);
plug class St_n in [0.27, 1.41] (worst n = 3, end-of-cycle T0, 20%
truncation) -> the frozen-time road alone is NOT defensible on the decisive
sector at the record head count; acoustic compactness He up to 1.4.
