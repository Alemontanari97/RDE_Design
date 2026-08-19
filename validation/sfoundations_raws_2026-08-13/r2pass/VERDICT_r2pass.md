# VERDICT — r2 batched adversarial pass (S-FOUNDATIONS-C, Blocco 1)

Date: 2026-08-18. Judge of record for the confirmation round mandated by
LG-1 (`orchestration:until-dry-confirm-direction-unproven`), condition C-2
of `VERDICT_contract_and_L4R1.md`, and the §2 dryness gap of
`phaseD/VERDICT_phaseD_proofs1.md`. Authority: per-objection adjudication;
DOWNGRADE-ONLY relative to the standing judge labels (no upgrades here;
restoration paths belong to their named carriers, e.g. D.18's G-f battery).
Paths relative to `validation/sfoundations_raws_2026-08-13/`.

Inputs read IN FULL: `r2pass/refute_r2batch_l0.md` (672 lines),
`r2pass/refute_r2batch_l1.md` (689 lines), `r2pass/refute_SEEDv2_KT1.md`,
`r2pass/refute_SEEDv2_KT2.md`, `r2pass/SEED_PROTOCOL_v2.md` (after the
seed outputs, per brief), `r2pass/BRIEF_refuters_r2batch.md`,
`r2pass/BRIEF_slot_KT1.md`, `r2pass/BRIEF_slot_KT2.md`, the two standing
verdicts, and the three target documents at every attacked leg (quote
verification + spot re-derivation; acts listed in §2.0).

NULL=FAILURE CHECK: all four slot outputs exist on file, non-empty,
well-formed; both lens files cover all 18 legs exactly once with the
required summary tables and self-falsifiers; both seed files end in a
mandatory-vocabulary verdict. No slot is dry-counted. PASS.

==============================================================================
## §1 ⚠️ SEED LAYER (prominent) — {canary_killed: TRUE, knowntrue_survived: FALSE}

**KT-1 (canary): KILLED — criterion MET.** Verdict BROKEN with positive
falsification at source: the refuter identified the exact defective step
(the supplied curl route silently drops the omega·div(u) term;
curl[(u·grad)u] = (u·grad)omega + omega·div(u) in 2-D), derived the correct
invariant omega/rho, and constructed a rigorous in-hypothesis
counterexample (Cauchy–Kovalevskaya solution off analytic non-characteristic
data). JUDGE RE-DERIVATION: the vector-identity computation, the
potential-vorticity derivation, and the pointwise counterexample algebra
(v_x = −c²eps/U0, u_x = −V0·eps/(1−M²), (u·grad)omega = −omega·div u ≠ 0
at the origin) were re-run at pen grade and all CHECK. This matches the
protocol key exactly (kill on content; packaging compliant). The KILL
direction of the layer is PROVEN — for the second time.

**KT-2 (known-true): FAILED — criterion NOT met.** Required verdict
SOUND-AS-LABELED; returned REPAIRABLE. Per SEED_PROTOCOL_v2 rule 3 this
COUNTS AS LAYER FAILURE, no exceptions. Judge decomposition (from
`BRIEF_slot_KT2.md` read against the refutation):
- The refuter's truth analysis is flawless: nine attack channels opened
  and correctly rejected; the core (Gamma = r·w streamline invariance)
  confirmed true; the EOS-FREE audit correct.
- The three label defects it names are GENUINE in the delivered route,
  verified by this judge at pen grade: (L1) the route's shock step
  ("RH tangential momentum with n_theta = 0 forces [w] = 0",
  BRIEF_slot_KT2.md lines 40-41 and 64-65) is literally insufficient —
  the raw tangential RH is [m·w] = 0, which the slip-surface case
  (m = 0, [w] arbitrary) satisfies; closing it needs RH mass [m] = 0
  plus m ≠ 0, neither invoked; (L2) the opening display (line 60) omits
  (w/r)∂w/∂theta while retaining ∂p/∂theta — a half-applied-axisymmetry
  internal inconsistency in the delivered "general" component; (L3) the
  cross-shock streamline concatenation is asserted, not constructed.
- CONSEQUENCE FOR ATTRIBUTION: the v2 delivery repaired the v1 packaging
  (A1/A3/A4 landed; A2's function spaces landed) but the PROOF ROUTE was
  not brought to the binding standard — "nothing formal left to refuse"
  (protocol rule 2) was NOT achieved. This is a SEED-AUTHORING defect,
  second instance of the same class, NOT demonstrated refuter blindness:
  the same agent pool killed the canary on pure content and its KT-2
  objections are true statements about the delivered text.

**BINARY OUTCOME AND CONSEQUENCE (not softened):**
- The verification layer remains **UNPROVEN in the confirm direction**.
  Every CONFIRMED leg in §3 rests on THIS JUDGE'S OWN READING of the
  refuter analyses and of the target documents — not on layer-certified
  silence.
- Per SEED_PROTOCOL_v2 success condition: **the Blocco-2 landing gate
  stays CLOSED** — no M0 landing may consume the r2-pass confirmations
  this window. LG-1 stays OPEN.
- The proofs-1 §6 falsifier ("a repaired known-true failing again ...
  forces re-adjudication of every survived label") FIRES formally. Its
  diagnostic clause ("would indicate layer blindness") is contradicted by
  the evidence above (kill direction proven twice; all three KT-2
  objections judge-verified genuine), but the operative consequence is
  APPLIED throughout this verdict: no label below is treated as
  layer-certified; every adjudication is a direct judge reading. The
  demanded re-adjudication of the survived labels of the proofs-1 loop is
  exactly what §3 of this verdict performs for the 18-leg delta set; the
  labels NOT covered by these 18 legs keep their proofs-1 §1 caveat
  ("rest on the judge's own reading") unchanged and un-upgraded.
- ESCALATION E-5 (§4): seed protocol v3 required — the known-true's
  route must be pre-audited against the binding standard by an agent
  OTHER than the seed author before launch; a third dual-seed run must
  pass before any until-dry loop certifies itself.

==============================================================================
## §2 Per-objection adjudication

### §2.0 Judge verification acts backing this table

Quote fidelity: all 11 quoted passages located and matched verbatim
(DOC-1 lines 1166-1176 and 2024-2063; DOC-2 lines 243-249, 1299-1326,
1349-1459; DOC-3 lines 504-515, 547-567, 1298-1303 region). NO misquote
found — no objection is overruled on quote grounds. Spot re-derivations
performed by this judge: (i) K operator identity => first-iff forward
direction fails (Exact = Reduced + K gives Exact=0 <=> Reduced = −K, not
the printed conjunction); (ii) partition-of-unity pairing: the terms
<mu, psi·chi_k> are k-independent by joint T-periodicity, so the literal
sum over k in Z diverges unless zero — the operative content is
Sum_k chi_k ≡ 1 plus Sum_k chi_k' ≡ 0, absent from the printed line;
(iii) D²G_U(W_s) = DF_x^T D²eta(M_s) DF_x + (D_M eta(M_s) −
D_M eta(M_U))·D²F_x(W_s): the congruence to the M-Hessian holds ONLY at
s = 0 (M_s = M_U), where the base state is supersonic-branch; at s > 0
the extra two-point term is present; (iv) DOC-1 §1 gas model (lines
174-178) pins ONLY Gibbs closure + c² > 0 + theta > 0 — no e_SS/c_v
condition; Harten/Godlewski–Raviart W-convexity of −rho·g(S) requires a
thermal-stability condition beyond these; (v) DOC-2 §0 (lines 139-162)
admits finitely many C¹ wave-steady front hypersurfaces on D × S¹ with
NO exclusion of locally-azimuthal (n_m = 0) strata — the helical
detonation front being declared in-scope rules out the only reading that
would exclude them; the printed singular-leg chain consumes
n̂ = n_m/|n_m|, undefined there; (vi) grep of DOC-2 for "normalization":
three hits (line 137 Stokes-psi; line 1317 = the attacked parenthetical
itself; line 1848 D.3 det) — NO declared surface-measure normalization
exists; (vii) eigenvalues u·n − c, u·n, u·n + c keep mutual gaps = c > 0
at u·n in {0, −c}: the eigenstructure is regular there; the
incoming/outgoing CLASSIFICATION is what jumps; (viii) the D.20 contact
split and Lemma 3.2 bracketing re-checked (agree with both lenses);
(ix) KT-1/KT-2 acts listed in §1.

DEDUP ADJUDICATION: no re-mint found. The three disposition attacks are
GENUINE under the brief's rule: L0-1/L1-1 attack the ADEQUACY of the
r2b-F6 disposition (the newly written line, zero prior coverage, carries
the sketch's gap); L0-3/L1-3 attack the ADEQUACY of the R4-1 disposition
(the r3-NEW distributional display R4-1's repair produced); L1-2
declares and holds its distinction from r2b-F1 (prices the GRANTED half,
not the coercivity conflation). All other objections target
final-revision text with zero prior adversarial coverage.

### §2.1 Adjudication table

Merged defects share a row-group; judge severity binds both IDs.

| ID(s) | Leg | Refuter class | JUDGE VERDICT | Derivation-level ground |
|---|---|---|---|---|
| L0-1 + L1-1 | 3 | REPAIR / AMENDMENT | **SUSTAINED-REPAIR** (both IDs; severity adjudicated UP from L1's wording-class) | Act (ii): the printed mechanism ("summing telescopes by periodicity") is divergent as literally written; the entire nontrivial content (single-window pairing + Sum chi_k ≡ 1 on field terms + Sum chi_k' ≡ 0 killing the cutoff-derivative terms) is absent, and the same periodization is silently needed for the (EU-x) EQUALITY pairing in the same display. Held to the document's own minted standard for exactly this step ("one line, but the line must be WRITTEN"), the written line is not the proof — proof-content repair, not wording. The r2b-F6 disposition is NOT adequately discharged. Conclusion true; class hypothesis right. |
| L0-2 | 5 | AMENDMENT | **SUSTAINED-AMENDMENT** | Act (iii): "at s = 0 CONGRUENT ... hence INDEFINITE at subsonic states" mis-stitches two true facts — at s = 0 the base point is supersonic-branch (congruent object DEFINITE); the true obstruction at s > 0 is the two-point integrand with NO definiteness certificate; and the mediant parenthetical lost the load-bearing "c moves with (rho,S)" clause in transcription (l1's mixing-exhibit verification supplies exactly that mechanism, confirming the CLAIM while confirming the printed justification incomplete). The OPEN verdict survives and strengthens; wording repair as specified by L0-2. |
| L1-2 | 5 | REPAIR | **SUSTAINED-REPAIR** | Act (iv): the granted half of route r2 (W-convexity of E = −rho·g(S) delivering the lower sandwich (i)) is conditional on a thermal-stability condition (e_SS > 0 / s-concavity / Bethe–Weyl class) NOT in the §1 gas model and not named in the row — an in-class EOS with c² > 0, theta > 0, e_SS ≤ 0 somewhere on K breaks delivered item (i). The r2 gap accounting is incomplete by one named condition; honest status line = "partial reduction MODULO named thermal-stability condition + open x-flux coercivity" (discharged at the standing gamma(T) closure by the AUD-cp-class c_v > 0 audit). Strengthens, not weakens, the row's no-viable-abstract-EOS-route conclusion — but the accounting text must change: repair, not wording. |
| L0-3 + L1-3 | 6 | BREAKS / BREAKS | **SUSTAINED-BREAKS** | Act (i): the FIRST IFF is FALSE in the ⟹ direction as printed. K is DEFINED by Exact = Reduced + K; hence Exact(V) = 0 ⟺ Reduced(V) = −K(V), NOT the printed conjunction. Two valid witnesses: (w1) any smooth phi-dependent exact wave-frame solution (the document's central object) has K ≠ 0 with LHS true; (w2) the document's OWN example (alpha), recorded two paragraphs above the display, satisfies the exact system distributionally while the text itself asserts BOTH RHS conjuncts fail ("the sections do not solve the per-phase system"; "in (alpha)/(beta) the singular part is NONZERO"). A biconditional carrying a "(bookkeeping, now true)" certification and refuted by its own recorded example is broken as printed. Repair is a one-line restatement (unconditional identity + the two true conditionals, or the quantifier prefix), but the display of record is a false mathematical statement: BREAKS. The R4-1 disposition is NOT adequately discharged. |
| L0-4 | 6 | REPAIR | **SUSTAINED-REPAIR** (over l1's confirmation of the same leg — l1's own re-derivation consumes n̂ and the meridional rows identically, so it does not cover the attacked stratum) | Act (v): locally-azimuthal (n_m = 0) front strata are in-class (§0 admits them; H-WR front-trace reading makes them mass-crossing), invisible to the meridional sections, and the printed chain cannot start there (n̂ = n_m/|n_m| is 0/0; the "K = 0 reduction to meridional RH" is vacuous since [F_m·n_m] ≡ 0). The surviving rows ([u]=[v]=0, g cont ≠ 0, g[w]+[p]=0, [s]=0 via the K_s atom, energy) form the RH system of an azimuthal normal shock with zero entropy jump — closing it to zero jumps is NOT derivable from H-NC + H-WR alone (EOS-free, an isentropic nontrivial jump is not excluded without a convexity/admissibility ingredient the hypothesis line does not carry). The conclusion "removable where n_phi ≠ 0" is UNPROVED on the n_m = 0 stratum; recoverable in-class (entropy-circulation or admissibility argument), but no such argument is in the document. Named case gap: repair (write the case or exclude it by hypothesis). |
| L0-5 | 6 | AMENDMENT | **SUSTAINED-AMENDMENT** | Act (vi): "the declared surface-measure normalization" references a declaration that does not exist anywhere in the document; and the meridional-cancellation "difference" identity is a Jacobian identity between two DIFFERENT measures/normals that the G-f spec should NAME as a check target. Wording repair as specified. |
| L1-4 | 6 | AMENDMENT | **SUSTAINED-AMENDMENT** | "On an exact 3-D solution the 3-D RH atoms vanish", quantified row-by-row over the SIX K rows, is false for the s row (exact solutions carry the entropy-production atom m[s] > 0 at mass-crossing shocks). The chain survives because it consumes the vanish-sentence only for conservation rows and the s-row atom comes from the operator identity directly. Scope the sentence to conservation-form rows. |
| L1-5 | 6 | AMENDMENT | **SUSTAINED-AMENDMENT** | The divergence-form smooth-region residual is (1/r)∂_phi F_phi,rel per row = advective K row + (u, v, Gamma, h0)·K_rho — the printed identification "(a.c. part) the displayed smooth-region K rows" is false as a row-by-row identity (true modulo the invertible triangular recombination, under which K = 0 is equivalent in both readings). Both iffs unaffected; but a G-f executor transcribing the displayed rows as the div-form a.c. parts would build a checker that fails on correct fields — the recombination identity goes into the definition and the G-f rejector spec. |
| L0-6 + L1-6 | 7 | AMENDMENT / AMENDMENT | **SUSTAINED-AMENDMENT** | Genuine nonlinearity is G_fund ≠ 0; an all-arc G_fund < 0 (BZT) EOS is genuinely nonlinear yet is exactly what the clause exists to exclude — "equivalently" is false as an equivalence. One-phrase fix: "i.e. genuinely nonlinear WITH the convex (compressive-shock) orientation". No content change; the displayed inequality is the operative hypothesis and the gamma(T) discharge (independently re-derived by BOTH lenses this pass, agreeing with the printed closed form) gives G_fund > 1. |
| L0-7 + L1-7 | 14 | BREAKS / REPAIR | **SUSTAINED-BREAKS** (both IDs; severity adjudicated UP from l1's repair-class) | Two independent defects in the quoted step, jointly fatal as printed: (a) quantifier order — eps_1 depends on Omega_int' and degenerates as Omega_int' exhausts Omega_int; no uniform eps_1 exists as displayed; (b) the face Gamma_in^coll is at distance ZERO from itself — finite propagation speed controls the solution at positive distance from the source face and can never deliver the TRACE ON the face, which is precisely what "in particular the interior-side trace ... stays zero" asserts. The bootstrap feeds each side's output into the other's input with no independent control of the coupling trace; as both lenses note, the argument verbatim would "prove" uniqueness for ANY transmission coupling with no transmission condition — it proves too much, hence proves nothing. The repair routes (two-face/half-collar overlap, or trace-level determinism folded into (H-UP)) both RESTATE the hypothesis: the printed statement "THEOREM modulo (H-UP)" is unproven from (H-UP) as stated. BREAKS. Theorem 1' (leg 12) is untouched and remains the unconditional content. |
| L1-8 | 17 | AMENDMENT | **SUSTAINED-AMENDMENT** | Act (vii): at u·n in {0, −c} with c > 0 the spectral gaps equal c and the eigenprojectors are regular; what degenerates is the incoming/outgoing SIGN CLASSIFICATION (the incoming-modes subspace map is discontinuous/ill-defined at the crossing), which is the true and sufficient reason the prescription fails to define a measurable N(x) there. Conclusion and scoping stand; the "1/c factors against closing spectral gaps" parenthetical describes a c → 0 degeneracy not at issue. Mechanism rewording only. |

**Counts (by objection ID; 15 raised = 7 l0 + 8 l1):**
SUSTAINED-BREAKS 4 (L0-3, L1-3, L0-7, L1-7 — 2 distinct defects);
SUSTAINED-REPAIR 4 (L0-1, L1-1, L0-4, L1-2 — 3 distinct defects);
SUSTAINED-AMENDMENT 7 (L0-2, L0-5, L0-6, L1-4, L1-5, L1-6, L1-8 — 6
distinct defects); OVERRULED 0. Distinct-defect count: 11 (2 B / 3 R /
6 A). No objection was overruled: every quoted passage matched, and
every attack survived judge re-derivation at the level it claims.

==============================================================================
## §3 Per-leg final adjudication (1..18)

Counting rule of record: CONFIRMED = no sustained objection, both lenses
covered the leg; CONFIRMED-WITH-AMENDMENTS = sustained wording-class
only; OBJECTION-SURVIVING = any sustained BREAKS/REPAIR -> escalation
(Form-2/until-dry; the corresponding M0 landing item is HELD OUT of the
Blocco-2 package).

| Leg | Target | l0 | l1 | **JUDGE FINAL** |
|---|---|---|---|---|
| 1 | [L-INC] both strata | CONFIRMED | CONFIRMED | **CONFIRMED** |
| 2 | [L-STD] no-topology pointwise argument | CONFIRMED | CONFIRMED | **CONFIRMED** |
| 3 | periodization step | L0-1 R | L1-1 A | **OBJECTION-SURVIVING** (E-1) |
| 4 | [P-HB3](i') data-space mollification | CONFIRMED | CONFIRMED | **CONFIRMED** |
| 5 | G8/r2 repricing | L0-2 A | L1-2 R | **OBJECTION-SURVIVING** (E-2; L0-2 amendment rides E-2) |
| 6 | D.18 singular leg + both iffs + atoms | L0-3 B, L0-4 R, L0-5 A | L1-3 B, L1-4 A, L1-5 A | **OBJECTION-SURVIVING** (E-3) |
| 7 | D.2 psi-existence + H-CVX arc | L0-6 A | L1-6 A | **CONFIRMED-WITH-AMENDMENTS** (A-1) |
| 8 | D.16 gross normalizer | CONFIRMED | CONFIRMED | **CONFIRMED** |
| 9 | D.20 contact split | CONFIRMED | CONFIRMED | **CONFIRMED** (now three independent derivations of record) |
| 10 | D.10 theta-halves exhibit | CONFIRMED | CONFIRMED | **CONFIRMED** |
| 11 | D.8 plane-stress rewording | CONFIRMED | CONFIRMED | **CONFIRMED** |
| 12 | Theorem 1' (collar) | CONFIRMED | CONFIRMED | **CONFIRMED** |
| 13 | Lemma 1.4 (finite speed) | CONFIRMED | CONFIRMED | **CONFIRMED** |
| 14 | Proposition 1'' bootstrap | L0-7 B | L1-7 R | **OBJECTION-SURVIVING** (E-4) |
| 15 | Lemma 3.2 (monotone intersection) | CONFIRMED | CONFIRMED | **CONFIRMED** |
| 16 | Corollary 4 row-(a) in-class | CONFIRMED | CONFIRMED | **CONFIRMED** |
| 17 | Remark 1.5.5 (ii') | CONFIRMED | L1-8 A | **CONFIRMED-WITH-AMENDMENTS** (A-2) |
| 18 | Lopatinskii display | CONFIRMED | CONFIRMED | **CONFIRMED** |

Totals: 12 CONFIRMED + 2 CONFIRMED-WITH-AMENDMENTS = **14 confirmed**;
**4 OBJECTION-SURVIVING: legs 3, 5, 6, 14.**

AMENDMENTS OF RECORD (wording-class, to carry into the eventual M0
landing of their confirmed legs):
- **A-1** (leg 7; L0-6/L1-6): in D.2 H-CVX, replace "(equivalently: the
  front's wave family is genuinely nonlinear along the connecting arc)"
  with "(i.e. genuinely nonlinear WITH the convex (compressive-shock)
  orientation)" — GN ⟺ G_fund ≠ 0, not G_fund > 0.
- **A-2** (leg 17; L1-8): in Remark 1.5.5, replace the "acoustic
  eigenprojectors degenerate (Lemma 0.2 arithmetic: 1/c factors against
  closing spectral gaps)" mechanism with the sign-classification jump of
  the incoming/outgoing split (the eigenstructure is regular at
  u-bar·n in {0, −c-bar} for c-bar > 0; the incoming-modes subspace map
  is what is discontinuous/ill-defined there).

==============================================================================
## §4 Consequence map (landing gate per item)

**GLOBAL OVERRIDE (seed layer, §1): the Blocco-2 landing gate is CLOSED
for the ENTIRE r2-pass confirmation set this window.** Per
SEED_PROTOCOL_v2's success condition, no M0 landing may consume these
confirmations while the layer is unproven in the confirm direction. The
per-item mapping below states what each confirmation is worth the moment
the gate opens (v3 dual-seed PASS, or an explicit orchestrator/user
decision to accept judge-reading-only certification); the HELD-OUT items
stay held out regardless of the gate.

(a) C-2 / AUDIT-DEBT-r2 (`VERDICT_contract_and_L4R1.md` J-3):
- The mandated targeted adversarial pass over the r2-delta set has been
  EXECUTED (two independent lenses, all 7 r2-new proofs covered).
- DISCHARGED-IN-ESCROW for legs 12, 13, 15, 16, 17 (with A-2), 18: the
  standing B.3 labels (Theorem 1' THEOREM; Lemma 1.4 THEOREM; Lemma 3.2
  THEOREM*; Cor 4 row-(a) THEOREM in-class; (ii') THEOREM; Lopatinskii
  display) are confirmed at their labels; M0 promotion of these becomes
  unblocked when the global gate opens.
- NOT discharged for leg 14: **JUDGE DOWNGRADE J-r2p-1** — Proposition
  1'' drops from "THEOREM modulo (H-UP)" to **SCHEMA** (named repair
  route: restate (H-UP) for the half-collar/two-face decomposition or
  with trace-level determinism, and rewrite the bootstrap; both lenses
  converge on the same construction from in-document ingredients). The
  B.3 J-1 clause "the modulo-form stands as literal text" is REFUTED by
  this pass: the literal modulo-form is unproven from (H-UP) as stated.
  The J-1 device-class effective label (SCHEMA-conditional, NG-9) was
  already at SCHEMA — this downgrade extends it to the modulo-form
  itself. M0 landing item HELD OUT (E-4).
- DOC-1 legs of set (a): legs 1, 2, 4 confirmed — the [L-INC], [L-STD],
  [P-HB3](i') rows land at their §3.1 labels when the gate opens. Legs 3
  and 5 HELD OUT (E-1, E-2): the [T-T0P] main-statement landing (which
  consumes the §4 proof head) and the G8/[C-XBVP](a') registry-row +
  gap-graph landing (which consume the G8 row text) wait for their
  repairs. [T-T0P] main was already SCHEMA — no further label motion;
  the repairs are text-level.

(b) proofs-1 §2 dryness gap (r3 texts):
- CLOSED-IN-ESCROW for legs 7 (with A-1), 8, 9, 10, 11: the r3-new
  legs of D.2, D.16, D.20, D.10, D.8 now carry a genuine two-lens
  adversarial pass; their §3.2 labels stand as of record.
- NOT closed for leg 6 (D.18). D.18's ground-(1) internal-consistency
  downgrade is NOT lifted by this pass (not this judge's to lift), and
  the pass found worse: **JUDGE DOWNGRADE J-r2p-2** — D.18 FIRST IFF
  drops from THEOREM*↓ to **SCHEMA** (the display is false as printed in
  the ⟹ direction; a restatement, not a check, is required — G-f cannot
  repair a false biconditional direction). **JUDGE DOWNGRADE J-r2p-3** —
  D.18 SECOND IFF drops from THEOREM*↓ to **SCHEMA** (in-class n_m = 0
  case gap; the printed chain cannot start on that stratum and the
  hypothesis set H-NC + H-WR is insufficient to close it EOS-free).
  Restoration path (NOT this pass's): the E-3 Form-2 escalation writes
  the restated first iff, the n_m = 0 case (or hypothesis exclusion),
  and the L0-5/L1-4/L1-5 amendments; the G-f battery then carries the
  labels back up per the proofs-1 upgrade path. M0 landing item HELD
  OUT (E-3).

(c) OBJECTION-SURVIVING legs -> named escalations, owner = THIS
SESSION'S ORCHESTRATOR; each goes to full form, Form-2/until-dry, and
CANNOT land in M0 this window:
- **E-1 (leg 3)**: rewrite the DOC-1 §4 periodization line as the
  three-step argument (single-window D'-pairing; Sum chi_k ≡ 1 applied
  to the field terms; Sum chi_k' ≡ 0 killing the cutoff-derivative
  terms), and state that the (EU-x) EQUALITY pairing rides the same
  identity. Statement unchanged; r2b-F6 disposition re-closed by the
  rewrite.
- **E-2 (leg 5)**: G8/r2 row — add the named thermal-stability
  condition (e_SS > 0 / s-concavity / Bethe–Weyl class) to the granted
  half, with the note that the standing gamma(T) closure discharges it
  via the AUD-cp-class c_v > 0 audit (L1-2); apply the L0-2 rewording
  (two-point integrand as the true obstruction; restore the
  "c moves with (rho, S)" clause or exhibit/flag the subsonic-average
  pair). The route-level OPEN conclusion and the gamma table are
  unchanged.
- **E-3 (leg 6)**: D.18 — restate the first iff (unconditional identity
  Exact = Reduced + K + the two true conditionals, or the quantifier
  prefix); write the n_m = 0 singular-leg case (entropy/admissibility
  argument) or exclude the stratum by explicit hypothesis in the second
  iff's statement; land amendments L0-5 (name the measure-normalization
  identity in the G-f spec; fix the "declared" parenthetical), L1-4
  (scope the atoms-vanish sentence to conservation rows), L1-5 (state
  the triangular recombination in the definition and in the G-f
  rejector spec). Labels per J-r2p-2/3 until then.
- **E-4 (leg 14)**: Proposition 1'' — restate (H-UP) (half-collar-face
  decomposition / family of collar depths, or trace-level determinism =
  the NG-9 machinery folded into the hypothesis) and rewrite the
  bootstrap via the two-face argument both lenses converge on (Lemma
  1.4 frusta to the mid-collar face + Theorem 1' on the half collar +
  (H-UP) on the enlarged interior). Label per J-r2p-1 until then.
- **E-5 (seed layer)**: LG-1 stays OPEN. Seed protocol v3: the
  known-true seed's PROOF ROUTE is pre-audited against the binding
  standard by an agent other than the seed author before launch (the v2
  failure is a delivery defect — three judge-verified genuine route
  elisions — not demonstrated refuter blindness); third dual-seed run
  required before any until-dry loop certifies itself. The proofs-1 §6
  re-adjudication trigger is on the record as FIRED; its application
  here = §1's no-layer-certification rule + this §3's re-reading of the
  18-leg delta set.
- **E-6 (gate)**: Blocco-2 landing package for the r2-pass set is
  BLOCKED this window (global override above). Nothing in this verdict
  may be cited as "layer-certified"; citations of confirmed legs must
  carry "judge-read, layer unproven in confirm direction (VERDICT_r2pass
  §1)".

==============================================================================
## §5 Falsifiers for THIS verdict

- §1 canary adjudication: refuted if the KT-1 counterexample fails to
  check — march the Section-3 Cauchy problem (U0 = 0.5c(R0), V0 ≠ 0,
  eps ≠ 0, gamma = 1.4) with a high-order solver; if omega stays
  constant along the streamline within a truncation-derived band while
  omega/rho drifts, the canary kill was wrong and the layer's kill
  direction is UNPROVEN (re-opening §1 entirely).
- §1 known-true adjudication: refuted if any of the three KT-2 defects
  is shown absent from the delivered brief — e.g. a derivation of
  [w] = 0 from the tangential-momentum condition ALONE on an m ≠ 0
  surface (kills L1), or a demonstration that the line-60 display IS
  the general azimuthal component (kills L2). Then the refuter verdict
  was miscalibrated, the failure re-attributes to layer blindness, and
  the proofs-1 §6 re-adjudication applies at FULL scope (every survived
  label of both loops), not the delivery-defect scope adjudicated here.
- §2 L0-3/L1-3 (first iff): refuted by a derivation of Exact(V) = 0 ⟹
  K(V) = 0 from the operator identity, or by showing example (alpha)
  fails to solve the exact system distributionally / has zero K atom —
  mechanically decidable by the G-f front-instance rejector run on
  (alpha).
- §2 L0-4 (n_m = 0): refuted by exhibiting an in-class exclusion of
  n_m = 0 front strata in DOC-2 §0/§5 (this judge's read found none:
  §0 lines 139-162), or by a proof closing the azimuthal-shock RH
  system ([u]=[v]=0, g cont ≠ 0, g[w]+[p]=0, [s]=0, energy row) to zero
  jumps from H-NC + H-WR alone, EOS-free.
- §2 L0-7/L1-7 (bootstrap): refuted by a valid derivation of the
  face-trace vanishing on [t*, t* + eps] from EXACTLY the printed
  (H-UP); note the derivation must not prove the same conclusion for a
  transmission coupling with no transmission condition (the
  proves-too-much test).
- §2 L1-2: refuted by deriving e_SS > 0 (equivalently c_v > 0) from
  Gibbs closure + c² > 0 + theta > 0 alone.
- Severity adjudications (L0-1/L1-1 to REPAIR; L0-7/L1-7 to BREAKS):
  refuted if the printed lines are shown to parse as complete arguments
  under their literal reading (for leg 3: a finite value of the full
  partition-sum pairing for nonzero T-periodic mu; for leg 14: closure
  of the printed quantifier order with a uniform eps_1).
- §3/§4 bookkeeping: any leg mapped to the wrong consequence class, any
  finding ID above absent from the two refuter files, or any quote
  mismatch against the target documents (grep-checkable) refutes the
  corresponding row.

END OF VERDICT — machine summary returned via structured output:
{canary_killed: true, knowntrue_survived: false,
layer_proven_both_directions: false, objections_total: 15,
sustained_breaks: 4, sustained_repair: 4, sustained_amendment: 7,
overruled: 0, legs_confirmed: 14, legs_surviving: [3, 5, 6, 14],
landing_gate_open: false}
