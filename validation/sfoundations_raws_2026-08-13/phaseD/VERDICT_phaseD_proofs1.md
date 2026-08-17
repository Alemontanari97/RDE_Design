# VERDICT — Phase D proof loop 1 (S-T0P + SWIRL-2D), judge of record

Date: 2026-08-17 (S-FOUNDATIONS R35 window). Judge: single-agent,
until-dry convergence adjudication. Inputs read IN FULL:
`phaseD_stop_proof.md` (2683 lines, revision 3),
`phaseD_meanswirl_formalization.md` (2001 lines, revision r3),
ALL 13 `refute_*.md` round files, `refute_SEED_canary.md`,
`refute_SEED_knowntrue.md`. File census measured this window
(`wc -l *.md` in phaseD/): 6 S-T0P refuter files (63 findings:
r1_l0 F1-F12, r1_l1 F1-F10, r2_l0 r2-F1..F11 + r2b-F1..F6, r2_l1
F1-F14, r3_l0 r3-F1..F5, r3_l1 F1-F5), 7 SWIRL-2D refuter files
(O1-O12, O-1..O-9, N1-N9, N-1..N-6, R3-1..R3-7b, V-1..V-5+ORCH,
R4-0..R4-5). Loop-reported objection totals (caller of record):
S-T0P 22, SWIRL-2D 25 — both NOT-DRY at cap (2 rounds).

==============================================================================
## §1 ⚠️ VERIFICATION LAYER: UNPROVEN (dual-seed report, prominent)

DUAL-SEED RESULT OF RECORD: {canary_killed: TRUE,
knowntrue_survived: FALSE}.

**THE REFUTER LAYER IS UNPROVEN in the confirm direction.** Per the
S-CERT dual-seed discipline (null=failure), one of the two seeds did
not return the required outcome, so the layer is NOT certified as a
two-sided instrument this loop.

Judge decomposition of the failure (from reading both seed files):
- CANARY (false claim, "w itself is the streamline invariant"):
  verdict BROKEN, with a correct counterexample (inviscid strained
  vortex, r·w conserved to machine eps, w drifts 101%) and correct
  classical attribution. The KILL direction is PROVEN: the layer can
  reject false mathematics with positive falsification.
- KNOWN-TRUE (r·w streamline invariance): the refuter CONFIRMED the
  mathematical core true ("survives every truth-directed attack")
  but returned verdict REPAIRABLE, refusing the THEOREM label on
  binding-standard grounds (bare hypothesis list, no function space,
  no falsifier, inert gas clause). Under the binary criterion this
  is a FAILED survival. Failure mode: OVER-STRICTNESS (label-level
  false positive on a true statement), not blindness.

WEIGHING CONSEQUENCE, applied throughout this verdict:
1. Survival of a claim through the loop is NOT positive
   certification — every final label below rests on the judge's own
   reading of the written proofs, not on the layer's silence.
2. The NOT-DRY-at-cap statuses cannot be read as "defects remain
   inexhaustibly": an over-strict layer never runs dry by
   construction. However, both final-round refuter verdicts were
   REPAIRABLE (not BROKEN), and the label-relevant findings of every
   round were CONTENT findings verified in-document (Galilean-boost
   falsifier, BZT/Hugoniot-arc counterexample class, helical-front
   counterexamples (α)/(β), the 1.13c box hole, the unconsumed-file
   R4-0 audit break) — those stand independently of layer
   calibration and the downgrades they forced are NOT reversible.
3. No label below is upgraded past evidence; two are DOWNGRADED
   (§3.2, D.18 iffs) on internal-consistency grounds.

==============================================================================
## §2 Consumption + dryness audit

- CONSUMPTION: COMPLETE on both targets. Every finding ID in every
  on-file refuter appears in a disposition row (§10/§11/§12 of the
  stop-proof; §6-bis/§6-ter/§6-quater of the mean-swirl doc). The
  one audit-integrity break of the loop (SWIRL R4-0 / S-T0P §11
  honesty note: unconsumed round-2 files coexisting with
  completeness claims) was caught BY THE LOOP and consumed with
  in-place annotation, never erasure. Nothing on disk is dangling.
- DRYNESS: NOT-DRY, CONFIRMED for both. The final revisions
  (stop-proof revision 3; mean-swirl r3) have had ZERO adversarial
  passes against their own text: the newest repairs — S-T0P's
  [L-INC], the L-STD no-topology pointwise argument, the
  periodization step, the (i') data-space mollification proof, the
  G8/r2 repricing; SWIRL's D.18 singular leg, the ψ-existence
  three-step argument, the H-CVX arc wording, the D.16 gross
  normalizer — are single-authored and unrefuted. This is exactly
  what "lands at reduced label with named gaps" must mean: the
  reduced labels are of record, and the unrefuted-final-pass residue
  is named below as a loop-level gap (LG-1) with owner.

==============================================================================
## §3 FINAL RIGOR CLASSES (judge-assigned; ↓ marks a judge downgrade)

### §3.1 S-T0P → [T-T0P] block (`phaseD_stop_proof.md`)

| Statement | Doc label (rev 3) | JUDGE FINAL | Notes |
|---|---|---|---|
| [T-T0P-E] equivariance half | THEOREM | **THEOREM** | Complete conditional assembly (hypothesis = S1-anchored uniqueness, stated in-statement); abstract EOS; three-target falsifier (t1)-(t3) has genuine rejection power. |
| [L-EQV1], [L-EQV2], [L-EQV3], [L-INV] | THEOREM | **THEOREM** | Full-group L-EQV3 restatement sound; verbatim computations. |
| [L-STD] | THEOREM | **THEOREM** | Countable-dense closure + eps_n union + no-topology pointwise argument all written; EOS-free. Final pointwise argument is r3-new/unrefuted (LG-1). |
| [L-SPACE] | THEOREM | **THEOREM** | Re-scoped (determinacy in Remark only) — correct. |
| [L-COMPAT], [L-XSON3], [L-XREC], [L-XWALL3], [L-XC3D] | THEOREM | **THEOREM** | Pen proofs complete at abstract EOS; the [X-T0P] symbolic battery is the owed executable rejector layer (G-f-analog; owner F2) — labels hold as complete-proof-here, carrier duty named. |
| [T-T0P-U] stratum (A) | SCHEMA | **SCHEMA** | Correctly downgraded from THEOREM* under the uniform registration+content criterion (r2-F1/l1-F4): G7/G8 unregistered mints, G8 abstract-EOS route OPEN, H7' structural clauses (w1)-(w3)/(d1)-(d2). Upgrade path (u1)-(u3) named — future work, not this verdict. |
| [T-T0P-U] stratum (B) | SCHEMA | **SCHEMA** | Gap list complete only as of rev 3 (G3 + G11 + G9); counterexample-adjacent open mathematics; G9 breadth honestly priced (admissible class possibly empty of physical instances). |
| [T-T0P] main (both strata) | SCHEMA | **SCHEMA** | Split gap lists; quantifier restricted to the T-PERIODIC class until G5; conclusions on Omega_march only; slip-free instances only. |
| [L-INC] | THEOREM (A) / modulo G2,G9 (B) | **THEOREM (A) / SCHEMA-inherited (B)** | No new gap minted; correct. |
| [P-HB1] | THEOREM | **THEOREM** | [H8'-gen] repair sound. |
| [P-HB2] | THEOREM | **THEOREM** | Linearity-of-homomorphism clause in place; D(a,b) rejector has genuine firing power. |
| [P-HB3] (i') | THEOREM | **THEOREM** | count(s\|I) defined; data-space mollification proof replaces the null-graph step; r3-new/unrefuted (LG-1). |
| [P-HB3] (i'') | THEOREM (periodic switching) / REMARK (one-shot Z_d) | **THEOREM / REMARK** | Split correct; monitor signature sufficient-only. |
| [P-HB3] (ii)/(iii) assembly | PROPOSITION | **PROPOSITION** | Assembly of record-level declarations. |
| Cor 5.1, Cor 5.2 | corollaries at parent grade | **inherit SCHEMA** | Domain-scoped (cl(Omega_march)), slip-free caveat mandatory in M0 text. |
| Proposed mints [C-MAJDA-3DT], [C-XINJ], [C-XBVP](a'), [C-WSF], G12 route | proposed | **PROPOSED-MINT (not yet citable)** | Per the document's own criterion these do not count as cited conditionals until registry rows exist — which is precisely why (A) is SCHEMA. |

Gamma status of the block, confirmed as stated: machinery abstract
EOS; route-dependent instance surface (G1 [X-IVXC] γ=1.4; G7/r-b,
G8/r1/r3 further instance certificates; table-interpolation
enclosures needed on the standing γ(T) tabulated model); the
abstract-EOS status of the [T-T0P-U]/[T-T0P] chain is OPEN AT THE
ROUTE LEVEL (r2b-F1 accounting verified honest). Every statement
carries a falsifier; the theorem-level instance falsifier is
G10-gated (declared structurally-gated conditional carrier, owner
F2, trigger = capturing-mode twin) — compliant with the
never-postpone discipline as a named conditional.

### §3.2 SWIRL-2D mean-swirl formalization (`phaseD_meanswirl_formalization.md`)

| Statement | Doc label (r3) | JUDGE FINAL | Notes |
|---|---|---|---|
| D.1 [MS-DEF-STATE] | DEFINITION | **DEFINITION** | C4-gamrow-equiv PASS. |
| D.2 [MS-T-TRANSPORT] | THEOREM | **THEOREM** | H-FIB/H-REACH explicit; ψ-existence three-step argument written (closedness/periods/quasiconvexity); s-monotonicity under ARC H-CVX, discharged in closed form γ(T)-exact (G_fund machine-checked + 2 independent pen re-derivations, both agree; carrier-grade recomputation queued G-f). |
| D.3 [MS-T-CHAR] | THEOREM | **THEOREM** | Machine-verified (n6_swirl_kernel Part A). |
| D.4 [MS-T-SPACE] | THEOREM (planar + curved) | **THEOREM** | Curved M_n clause closes the N2 licensing hole; audit-wiring rejector armed. |
| D.5 [MS-T-MARGIN] | THEOREM | **THEOREM** | (ii) γ(T)-exact under AUD-c2T + u>0; (i)/(iii) EOS-general. |
| D.6 [MS-T-FLUXNULL] | THEOREM* | **THEOREM*** | Two named conditionals: (c1) assembled-balance symbolic check (queued, G-a) + (c2) H-AM0 (audited by concentration tests, else ASSUMED-PER-DATASET). Pen assembly independently reproduced by 4 panel positions; convention closure (r2) and plane-stress budget (r3) verified in-text. NOT downgraded: unlike G7/G8, (c1) is a verification debt on a written proof and H-AM0 is a hypothesis, not an unregistered consumed lemma. |
| Rmk 3.1 | THEOREM | **THEOREM** | One-line; EOS-free; dataset falsifier attached. |
| D.7 | THEOREM* | **THEOREM*** | Contrapositive of D.6, same conditionals. |
| D.8 census | DEFINITION + THEOREM* exhaustiveness | **DEFINITION + THEOREM*** | Exhaustive over {¬H-AM0..¬H-AM5} after the r1 (0)-channel and r3 plane-stress rewording. |
| D.9 [MS-T-MEASURE] (i),(ii) | THEOREM | **THEOREM** | Product-L¹ class stated; Z_n cell-sweep step written. (iii) DEFINITION. |
| D.10 [MS-T-SKE] | THEOREM + PRACTICE (twins) | **THEOREM + PRACTICE** | θ-halves exhibit (r3) now actually zeroes the Γ-flux; "unrecoverable" correctly scoped to the vaneless class. |
| D.11 | CONJECTURE | **CONJECTURE** | Correctly the lowest class; F3 falsifier awaits dataset (G-e). |
| D.12 | PRACTICE (prohibition) | **PRACTICE** | |
| D.13 [MS-DEF-CONTRACT] | DEFINITION + THEOREM (recovery uniqueness) | **DEFINITION + THEOREM** | Two-line F′>0 proof, all M, γ(T)-exact; existence under AUD-hRANGE (flag-never-extrapolate). |
| Rmk 4.1 | THEOREM | **THEOREM** | Vacuity argument; γ(T)-exact premise declared. |
| D.14 [MS-DEF-TRIPLE] | DEFINITION + SCHEMA (licensing leg, 2 gaps) | **DEFINITION + SCHEMA** | TV-form finite on BV; LICENSING direction gated on G-b1 (unproven sensitivity functional) + G-b2; BLOCKING direction usable now (conservative). Every licensing verdict must carry the G-b1 conditional explicitly. |
| D.15 [MS-T-GAMONLY] Clause 1 | THEOREM | **THEOREM** | Identity machine-verified + explicit exhibit. |
| D.15 Clause 2 | SCHEMA | **SCHEMA** | = the N6-3 strong-only-if leg (G-g); cancellation family with the Γ₀² proviso recorded. |
| D.16 [MS-DEF-AMAUDIT] | PRACTICE | **PRACTICE** | Gross normalizer + signed arming + backflow synthetic; residual target THEOREM*-backed by D.6. |
| D.17 [MS-DEF-3DWF] | DEFINITION | **DEFINITION** | |
| D.18 K list + completeness | DEFINITION (distributional) + SCHEMA (G-f) | **DEFINITION + SCHEMA** | Correct: C4 is internal consistency only (common-mode blind); completeness rides G-f. |
| D.18 FIRST iff | THEOREM | **THEOREM*** ↓ | JUDGE DOWNGRADE. "Bookkeeping by construction" is licensed only GIVEN the singular-density display (atoms = n_φ[F_φ,rel] per row), and the document itself declares that row-by-row bookkeeping "a pen computation ... [that] RIDES the G-f independent re-derivation". A clause whose load-bearing display is queued-for-carrier is complete MODULO a named, owned check — that is THEOREM* modulo G-f, by the document's own D.20 criterion. |
| D.18 SECOND iff (under H-NC + H-WR) | THEOREM | **THEOREM*** ↓ | JUDGE DOWNGRADE, two grounds. (1) Internal criterion consistency (the r2-F1 defect class): D.20's mass-crossing front clause — a pen jump-algebra leg, TWICE independently re-derived, carrier queued (G-a) — is labeled THEOREM*; D.18's singular leg is a pen jump-algebra leg with ZERO independent re-derivations, carrier rejectors queued (G-f), authored in the final unrefuted pass — it cannot sit a class above D.20's leg under one criterion. (2) Track record: the two predecessor forms of this clause were FALSE (r1 divided by w_rel; r2 false on the front-carrying class, R4-1), and the r3 form has had no adversarial pass. The a.c. leg's algebra I verify as sound by reading; the label is THEOREM* modulo the G-f executions (three kernel/front-instance rejectors + K_h0 sympy check + singular-density bookkeeping). Upgrade path: run the G-f battery (or one refutation pass over the r3 text) — content change not expected. |
| D.19 [MS-T-PUMP] | THEOREM (model-internal) + PRACTICE (bridge) | **THEOREM + PRACTICE** | C1/C2 machine-verified. |
| D.20 [MS-T-ROTH] | THEOREM (smooth + contacts) / THEOREM* (mass-crossing fronts) | **THEOREM / THEOREM*** | C3 + firing rejector R1; mass-crossing leg twice independently re-derived, carrier queued G-a; contact split (r3) is two-line RH algebra — sound. |
| S.22 [MS-S-KBOUND] | SCHEMA | **SCHEMA** | Target statement; g1 norm fork (split vs W^{−1,q}/dual-Lipschitz) is a declared design fork; g2a weak-vs-weak relabel and g2b known-broken contact regime are honest walls; g3 transit-integrated O(St). Input contract for T-RED. |

Gamma discipline: verified compliant — every statement carries one
of EOS-FREE (defined at r3) / EOS-GENERAL / γ(T)-EXACT; NO statement
in either document is γ=const-only. Falsifier discipline: verified
compliant — every claim ends with a falsifier, with reproduction-
vs-rejector correctly distinguished (r1 repair) and the two
structurally-gated carriers (G10; G-e datasets) declared with
owner + trigger.

==============================================================================
## §4 NAMED GAPS — consolidated ledger with owner-suggestions

S-T0P block (G1-G12, all confirmed correctly cited at point of use):
| Gap | Content | Owner-suggestion |
|---|---|---|
| G1 [C-XBVP](a) | abstract-EOS pointwise convexity (ideal-gas instance discharged, [X-IVXC]) | F2 ([X-T0P] extension) |
| G2 [C-XBVP](b) | 3-D t-slab trace package (b1)-(b4) + STRUCTURAL (b1')/(b2') = (d1)/(d2),(w1)-(w3) | F2 |
| G3 [C-MAJDA-3DT] | multi-D unsteady KL stability + H^s front uniqueness; sub-gap g3-b regularity bridge | F2 (registry row FIRST, per (u1)) |
| G4 | tilted-interface branch, clauses g4-a..g4-d; edge G4→G8 | F2 (primary cross-section case vacuous) |
| G5 | H8' lift via cone localization; edge G5→G8 (discharge order: G8 before/with G5) | F2 |
| G6 = H10 | existence not claimed | P7/D-S1 instance certification (standing) |
| G7 [C-XINJ] | global branch injectivity; routes r-a (abstract EOS) / r-b (certified 1-D root-count, both-roots-in-K criterion) | F2 ([X-T0P]; registry row per (u1)) |
| G8 [C-XBVP](a') | hull/segment convexity; FEASIBILITY GATE first (conv(K_M) vs sonic fold); NO viable abstract-EOS route named; edges G5→G8, G4→G8, G8-falsifier→G7-instrument | F2 (gate = first item of upgrade step (u2)) |
| G9 | slip-sheet exclusion — a WALL, no named route; both strata exclude the generic RDE front type | F2 (SCOPE DECISION — flag for user at a session boundary; "certified slip-free" instance check proposed for the S1 battery) |
| G10 | instance-falsifier carrier gating (capturing/unsteady twin) | F2, trigger = A1 capturing-mode capability |
| G11 [C-WSF] | weak-vs-fronted-strong uniqueness; primary route [S-ACFR] a-contraction transplant | F2 (registry row per (u1)) |
| G12 | minimal-load classical route for statement (i) (Li Ta-tsien/Secchi); kills the over-conditioned inheritance for (i) | F2; ALSO a novelty threat (P. Qu / H. Yuan queries owed at any paper claim) |
| + | [T-XWS] retro-annotation (the G8 gap sits unnamed in the 2-D proof of record) | SAME R4 window as the M0 delta |
| + | [X-T0P] symbolic battery (all §9 candidates, bundled with G7 r-b + G8 gate/falsifier, branch-continuation rule, box asserts) | F2, commit-gated carrier window |

SWIRL-2D block (G-a..G-g + loop-level):
| Gap | Content | Owner-suggestion |
|---|---|---|
| G-a | D.6 assembled-balance + D.20 rotating-frame RH symbolic check (one task, shared) | D.6 promotion task, F2 window |
| G-b1 | sensitivity FUNCTIONAL \|obj err\| ≤ S·OBS on BV, W-extremum case explicit | N6 §5 line — GATE for any licensing use of D.14 |
| G-b2 | per-campaign derived tolerance constant | first licensing campaign |
| G-c | S.22 (g1)-(g4): norm-pair fork (g1, merged with g3), g2a shock-free sub-scope / fitted-front route, g2b contact wall, g4 corrector composition | R22-F / T-RED line (S.22 = its input contract) |
| G-d | [S-5F] five-field optimality assembly | F2 |
| G-e | empirical vacuum: F1-F4, A4 never computed on any dataset | first chamber-CFD dataset ingestion window |
| G-f | D.18 K-completeness: independent re-derivation + metric/K-corruption + H-NC/H-WR kernel + FRONT-instance rejectors + K_h0 sympy check + singular-density bookkeeping + G_fund carrier-grade recomputation. NOW ALSO CARRIES the §3.2 judge downgrades: executing G-f is the named upgrade path of both D.18 iffs back to THEOREM | carrier upgrade, commit-gated, same window class as G-a |
| G-g | D.15 Clause 2 variation-quantifier/power-separation proof | N6 doc §5 line |
| LG-1 (loop-level, NEW, this verdict) | the final revisions of BOTH documents are unrefuted (NOT-DRY at cap) AND the verification layer is unproven in the confirm direction: the r3/rev-3 single-authored repairs have zero independent eyes | S-FOUNDATIONS orchestrator: either one confirmation round over the final texts, or absorb via the queued carrier executions (G-f/G-a/[X-T0P]) which mechanically check the newest legs; ALSO re-run the dual-seed with a repaired known-true protocol (seed delivered WITH hypothesis list + falsifier, so survival is decidable) before the next until-dry loop certifies itself |

==============================================================================
## §5 READY-TO-LAND verdicts (M0 / master-doc absorption)

S-T0P block — **READY-TO-LAND: YES, at the revision-3 labels
exactly**, conditional on the same-window R4 duties the document
itself names (all confirmed correct by this judge):
 (i) M0 [S-T0P] site → [T-T0P] SCHEMA both strata with SPLIT GAP
     LISTS — the M0 sentence must NOT be stated stronger than the
     proof: t-periodic-class quantifier, Omega_march domain,
     slip-free caveat, (i)-vs-(ii) G12 decomposition, gap-graph
     edges (G5→G8, G4→G8, G8-falsifier→G7-instr), two-tier
     G10-gated falsifier;
 (ii) registry rows for [C-MAJDA-3DT]/[C-XINJ]/[C-XBVP](a')/[C-WSF]
     + [L-INC] + G12 in the SAME window (SR discipline, no silent
     mint; until they exist the mints stay proposals and the SCHEMA
     labels are the ceiling);
 (iii) [T-XWS] retro-annotation (G8 names the 2-D gap too);
 (iv) [T-T0]/[T-SLRW] consumption sentences restricted per Cor 5.1.
 NOT-READY sub-item: NONE withheld — but any THEOREM* upgrade of
 stratum (A) is FORBIDDEN until (u1)-(u3) complete.

SWIRL-2D block — **READY-TO-LAND: YES for §7 items 1-6, at the §6
register labels WITH the two §3.2 judge downgrades applied**
(D.18 first/second iff land as THEOREM* modulo G-f, mirroring
D.20's mass-crossing leg; everything else at register label):
 - D.13 row → M0 VI.1 (item 1): READY (DEFINITION + recovery
   THEOREM).
 - H-AM block + D.6-D.12 → M0 Part III (item 2): READY (D.6/D.7/D.8
   at THEOREM* with (c1)/(c2) named; D.11 lands AS CONJECTURE).
 - D.15/D.19/D.20 cross-refs → N6 §5 (item 3): READY.
 - D.16 audit row + D.14 G6 rejector + carrier registration → D6
   plan (item 4): READY; carrier baseline row per lint (vii) in the
   same window; D.14 lands with the LICENSING leg explicitly
   SCHEMA-gated (G-b1) — blocking use only until G-b1.
 - T3-CONTROL (item 5): no change needed — confirmed.
 - L4/[D-CONTRACT] planar-only repair (item 6): READY and REQUIRED
   (the m_n form or an explicit planar pin — the current "u_x − c"
   certificate is planar-only; leaving M0 as-is would preserve a
   licensing hole D.4 has closed).
 The §7 gate (R4-0 precondition) is verified DISCHARGED: r2_l0
 consumed in §6-quater table (A), file census measured.

Both landings must cite this VERDICT file and carry the §1
verification-layer caveat: the loop's survivals are adversarially
pressured but not layer-certified.

==============================================================================
## §6 Judge falsifiers (this verdict is itself a claim)

- §3.2 D.18 downgrade: refuted if the G-f battery (front-instance
  rejector + singular-density bookkeeping + kernel checks) executes
  PASS with zero content change — then THEOREM is restored by note
  and the downgrade was conservative-only (the intended outcome).
- §2 consumption claim: refuted by exhibiting any finding ID in any
  phaseD refuter file absent from all disposition ledgers.
- §1 weighing: refuted if a repaired known-true dual-seed run
  (hypotheses + falsifier attached) again fails to survive — that
  would indicate layer blindness rather than over-strictness and
  would force re-adjudication of every survived label here.

SEED LINE (of record): dual-seed batch S-FOUNDATIONS Phase D,
2026-08-17 — canary_killed=TRUE (verdict BROKEN, positive
falsification at source verified by this judge); knowntrue_survived
=FALSE (verdict REPAIRABLE on a true core — confirm-direction
calibration failure). REFUTER LAYER: PROVEN to kill, UNPROVEN to
confirm. All final labels in §3 rest on the judge's direct reading.
