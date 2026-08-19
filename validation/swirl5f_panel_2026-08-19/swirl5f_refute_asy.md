# Adversarial referee report — asymptotics lens ('asy')
# Target: swirl5f_asy.md (five-field per-phase asymptotic structure)

Status: REFUTATION ARTIFACT (scratchpad, 2026-08-19). Referee brief:
independently re-derive the term orders and the homogeneity check,
then diff. Every referee claim below carries its own label from
{PROVEN-HERE, PROVEN-IN-RECORD, SCALING-ESTIMATE, HYPOTHESIS, OPEN}.
Independent machine check: `swirl5f_refute_asy_check.py` (this
directory; sympy, pinned env, no installs) — written from scratch
with an independent symbol set (full (x,r,φ)-dependent primitive
fields), NOT derived from the author's script. Output of record:
`REFEREE FAILS: NONE` for (1) the six-row K census (exact − reduced −
K ≡ 0 on the four dynamical rows, advective transcription), (2) the
independent r-weighted divergence-form flux homogeneity (all five
rows of F_x, F_r, F_φ,rel + the r-source, degree-1 under U → kU,
abstract T(e)), and (3) the K_h0 elimination structure (referee's
variant: under K_ρ = 0 and φ-uniform s, K_h0 = [w/(rρ)](c² −
w_rel²)∂_φρ — vanishing exactly on the |w_rel| = c kernel, consistent
with the record's E7/D.18 kernel and with the author's use). The two
"fails" my script prints for D.19(ii)/D.20 are my own check-design
artifact: the printed residual factors EXACTLY as c²D_relρ − D_relp =
−(entropy-row content), i.e. zero on-shell — verified by hand;
D.19(ii)/D.20 are also machine-verified in the record (C2/C3). The
author's script `swirl5f_ray_check.py` was re-run by me: reproduces
("FAILS: NONE", rejector fired True). [PROVEN-HERE for all of the
above.]

==============================================================================
## §1 Referee's independent re-derivation (what I checked from scratch)

1. MASTER FORMULA. From w_rel/r = w/r − Ω, w = ε_θΩR_m w̃, φ =
   (2π/n)φ̃, St_n = nΩτ_n/2π, τ_n ≈ L/U:
     (w_rel/r)∂_φ = −(U/L)·St_n·(1 − ε_θ w̃ R_m/r) ∂_φ̃ .
   Reproduced independently; the sweep/drift split and the identity
   Ω(n/2π) = St_n U/L are exact. [PROVEN-HERE — agrees with the
   target §1.2.]

2. GROUP IDENTITIES. δ = ε_θM_Ω/M_x; M_θ = ε_θM_Ω; Λ = nL/2πR_m =
   St_n M_x/M_Ω; χ = ε_θ(Ωr)²/h0 (exact) = ε_θM_Ω²(γ−1)(h/h0)
   (γ = const conversion — see Defect 6); β_w = p/(ρh0) =
   (γ−1)h/(γh0) (same caveat); β_τ = p/(ρΩr u_θ) = 1/(γM_Ω²ε_θ)
   (exact for thermally-perfect, γ local); χβ_τ = β_w (closes).
   Concordance: δ = 0.17–0.25 from f_θ = 3–6% and ε_θ = 0.15–0.20
   give M_Ω/M_x = 0.85–1.67 — reproduced. [PROVEN-HERE.]

3. ORDER TABLE. Every §2.2 entry re-derived from scratch:
   sweep a_q St_n; drift a_q ε_θ St_n; torque-vs-Γ-budget
   a_p St_n β_τ (via nL/2π = St_n U/Ω); torque-vs-axial a_pΛ; work
   a_p St_n β_w (via ΩnL/2πU = St_n). Numerical ranges reproduced
   at the author's declared working values (0.07–0.7 / 0.012–0.12 /
   0.08–0.83 / — / 0.007–0.09). [PROVEN-HERE — the ordering rows
   are correct as scale ratios.]

4. K CENSUS (missing-term hunt, machine-executed). I wrote the
   unsteady cylindrical Euler rows (absolute velocity, advective
   form), substituted ∂_t → −Ω∂_φ, subtracted the ∂_φ-struck 2.5-D
   rows, and diffed against D.18's displayed K rows: identically
   zero on mass/x/r/Γ; s and h0 rows definitional. At the advective
   level the six-row list is complete — no seventh row exists in
   this transcription (completeness against an independent div-form
   symbol set remains G-f, as the target declares). ∂_φ-term count
   per row: mass 1, x 1, r 1, Γ 2 (sweep+torque), s 1, h0 2
   (sweep+work) — matches. [PROVEN-HERE, modulo the same G-f
   inheritance the target declares.]

5. HOMOGENEITY / P1–P5 (my lens's core duty). Independent
   transcription (r-weighted divergence form, Γ-row azimuthal flux
   r(ρw w_rel + p), energy relative flux w_rel(ρE+p) + Ωrp — the
   Ωrp term re-derived by me from F_φ(energy) − Ωr·ρE =
   w(ρE+p) − ΩrρE): every entry degree-1 in U with abstract T(e);
   sources degree-1; hence Jacobians ray-invariant (Euler) and
   D(kŴ-family) = k′Z. RH = differences of degree-1 fluxes ⟹
   fitted-sheet k-invariance: sound inference. P1 (U → kU at fixed
   u,v,w,T with Γ = rw fixed) correct. The 5F ray family remains a
   solution family (homogeneous system + degree-0 wall BC +
   k-scaled inflow). [PROVEN-HERE — the theorem's algebraic core
   SURVIVES my attack.]

==============================================================================
## §2 Numbered defects

DEFECT 1 — STALE RECORD LABEL INHERITED (D.18 iffs). MAJOR,
anchor/misquote class (e).
  Where: target lines "the two D.18 iffs at THEOREM*/SCHEMA per the
  judge (VERDICT §3.2, downgrades of record)" (inheritance
  declaration, §0), the SOURCES list ("D.18 iffs = THEOREM*/SCHEMA
  modulo G-f"), and §3.1 ("inherits D.18's THEOREM*/SCHEMA status
  per VERDICT §3.2").
  Fact of record: VERDICT_phaseD_proofs1.md §3.2 (the cited source)
  gave first iff → THEOREM*↓; that verdict is SUPERSEDED by the
  r2-BATCH judge — `r2pass/VERDICT_r2pass.md` lines 249–253: JUDGE
  DOWNGRADE J-r2p-2 (D.18 FIRST IFF: THEOREM*↓ → **SCHEMA**) and
  J-r2p-3 (SECOND IFF: THEOREM*↓ → **SCHEMA**), escalation E-3
  pending; the formalization document's own class block and §6
  register row carry "BOTH iff clauses SCHEMA per J-r2p-2/J-r2p-3"
  at four places (grep-verified). The target read that document "IN
  FULL" and still cites the older, superseded label. Since the
  target's §0 asserts "No claim below exceeds its record
  certification status", this is a live violation for claims 10, 20
  and the §3.1 K-governance sentence. [PROVEN-IN-RECORD —
  r2pass/VERDICT_r2pass.md:249–253; phaseD_meanswirl_formalization.md
  register row D.18.]
  Correction: replace all three occurrences with "both D.18 iffs =
  SCHEMA per J-r2p-2/J-r2p-3 (r2pass/VERDICT_r2pass.md §4(b)), E-3
  adjudication pending, restoration path = G-f battery; the
  phaseD_proofs1 VERDICT §3.2 THEOREM* label is superseded."
  Materiality: bounded — §2's ordering rides only G-f (correctly
  inherited at SCHEMA); but claim 10's inherited status and any
  downstream consumer of "THEOREM*" are inflated by one rung.

DEFECT 2 — DRIFT CENSUS MISCOUNT; "EXHAUSTIVE" IS FALSE AS PRINTED.
MAJOR, missing-term class (a) at the enumeration level (order-level
impact NIL).
  Where: §2.3(i): "the five DRIFT pieces (w/r)∂_φ(ρ, u, v, Γ, s)";
  echoed in the author's summary ("all five advective rows").
  Referee's count: SIX. K_h0 = (w_rel/r)∂_φh0 + (Ω/ρ)∂_φp splits as
  −Ω∂_φh0 + (w/r)∂_φh0 + (Ω/ρ)∂_φp: the drift-of-h0 piece
  (w/r)∂_φh0, O(a_h0 ε_θ St_n), satisfies the census's own
  interaction criterion exactly as the s-piece does. It is even
  PRESENT in the target's own §2.1 ("sweep of h0: a_h0St_n
  (1 + O(ε_θ))") and §2.2 table line ("DRIFT ... in all rows") —
  the document contradicts itself between §2.2 ("all rows") and
  §2.3 ("five"). A census labeled "exhaustive ... [PROVEN-HERE by
  inspection]" with a member missing from the enumeration is
  exactly the defect class this program prosecutes. [PROVEN-HERE.]
  Correction: "(i) the six DRIFT pieces — (1/r)∂_φ(ρw) on the mass
  row and (w/r)∂_φ(u, v, Γ, s, h0) — O(a_q ε_θ St_n)." (Note also
  the mass-row drift is (1/r)∂_φ(ρw) = (w/r)∂_φρ + (ρ/r)∂_φw, not
  bare (w/r)∂_φρ; same order, but the census's shorthand drops the
  ∂_φw half.) No magnitude changes anywhere.

DEFECT 3 — R2's HEADLINE NUMBER IS VARIANT-CONDITIONAL. MAJOR,
proof-gap class (d).
  Where: §3.2 R2: "4F either drops u_θ²/2 from h0 ... or folds it
  into meridional KE ... The removed axial-velocity/thrust bias:
  ΔV/V ≈ −δ_exit²/2 ≈ −(1.5–3)%. POSITIVE-DEFINITE ... no
  cancellation ever protects a 4F model from it."
  Referee derivation: the displayed ΔV/V = −δ_exit²/2 is the FOLD
  variant only (4F books total h0 including swirl content, spends
  it all meridionally). In the DROP variant (interface contract
  hands meridional-only h0_m(ψ) = h0(ψ) − Γ(ψ)²/2r_in(ψ)²), the 4F
  exit KE is 2(h0 − h) − Γ²/r_in² against the truth
  2(h0 − h) − Γ²/r_exit²: the bias is (Γ²/2V²)(1/r_in² − 1/r_exit²)
  — GEOMETRY-DEPENDENT, signed by the radius change, and ≈ 0 when
  r_exit ≈ r_in per streamline. [PROVEN-HERE, three lines above.]
  D.10's E_θ > 0 (THEOREM) is about the flux booking, and does NOT
  by itself make the 4F THRUST bias positive-definite in both
  variants; which variant the current engine implements is a D.13
  contract fact not stated in the target. The 1.5–3% number feeds
  §3.4's headline (see Defect 4).
  Correction: split R2 into R2-fold (ΔV/V = −δ_exit²/2, 1.5–3%,
  single-signed — as derived) and R2-drop (bias
  (δ²/2)(1 − r_in²/r_exit²), geometry-signed, |·| ≤ the fold value
  for r_exit ≥ r_in), and state which variant the engine's
  interface contract instantiates before quoting one number.

DEFECT 4 — CLAIM 16 ("LARGEST UNPROTECTED BIAS CLASS ... PROVEN-HERE
assembly") OVERCLAIMS ITS LABEL. MAJOR, class (d).
  Where: §3.4 CONSEQUENCE; claim register row 16.
  The assembly compares QUANTIFIED removed biases (1.5–6%-class)
  against retained classes whose unprotected content is
  UNQUANTIFIED of record: (i) the jump-localized first-order
  residue's absorption by the fitted sheet is the pre-registered
  CONJECTURE P-ii (T3QS B3/B4 — the target itself says so in §2.4);
  (ii) real cycles are off-ray (two-parameter (P0,T0) + the
  target's own H3-w expectation of failure, §4.4) with area terms
  carrying unmeasured a_w; (iii) at St_n → 1 the first-order
  framework's own parameter a·St_n ≈ 0.7 is not small (the target's
  §2.5 concedes pointwise O(1)), and E1's per-transit ΔΓ/Γ ≈ 0.83
  feeds the SAME E_θ/h0 bookkeeping at order χ·ΔΓ/Γ ≈ up to 9% in
  h0 — nominally comparable to the removed class. The clause "(c)
  is priced by the corrector/S.22 program" prices nothing today:
  S.22 is SCHEMA with g1–g4 open and g2b KNOWN-BROKEN on contacts.
  [PROVEN-IN-RECORD for the statuses; SCALING-ESTIMATE for the
  E1-feedthrough number.]
  Corrected claim (referee's version): "5F removes the largest
  QUANTIFIED unprotected coherent bias class; the retained sweep
  class is mean-protected at first order ON-RAY, with its
  unprotected remainder (jump residue, off-ray area, in-duct
  torque feed-through) unquantified of record and nominally
  comparable at St_n → 1 — the upgrade's net-value claim is
  therefore St_n-conditional pending P-ii/S.22." That is a
  PROVEN-HERE ordering statement; the printed absolute form is not.

DEFECT 5 — UNSURFACED HYPOTHESIS: SWIRL CO-ROTATION SIGN. MINOR,
class (c).
  Where: G5/D3: M_rel = M_Ω(1 − ε_θ), "magnitude 1.2–2.1"; master
  formula drift coefficient.
  ε_θ is used unsigned throughout, but M_rel = M_Ω(1 − ε_θ) assumes
  CO-ROTATING swirl (w > 0, wave sense). The record's own D.11
  (CONJECTURE) expects the plain-mean swirl net COUNTER-wave, which
  gives M_rel = M_Ω(1 + |ε_θ|) — farther from the lock-in kernel
  (E7) and from the C51 marching threshold. The target's choice is
  the CONSERVATIVE side for both consumers, but under the file's
  own discipline a sign convention that moves a named group's range
  is a hypothesis to surface, not to leave implicit. [PROVEN-HERE
  (algebra) + PROVEN-IN-RECORD (D.11 status).]
  Correction: add "(H-sgn) ε_θ > 0 co-rotating at the phases that
  dominate the march; counter-swirl phases have M_rel =
  M_Ω(1 + |ε_θ|) (larger margin) and a sign-flipped drift
  coefficient — orders unchanged, ranges one-sided conservative."

DEFECT 6 — γ = CONST CONVERSION BOUNDARY UNNAMED IN χ, β_w. MINOR,
class (c) (standing gamma-variable directive).
  Where: D5 ("(Ωr)² = M_Ω²c² = M_Ω²(γ−1)h for the γ(T) closure at
  working γ"), D6.
  c² = (γ−1)h is CALORICALLY-PERFECT algebra (h = c_pT); under the
  γ(T)-exact closure of record h = ∫c_p dT ≠ c²/(γ−1) in general.
  The exact definitions (χ = ε_θ(Ωr)²/h0, β_w = p/(ρh0)) and the
  closure χβ_τ = β_w survive with LOCAL γ read as γ(T) only
  approximately. The "at working γ" hedge exists but the standing
  directive requires the γ = const boundary NAMED. β_τ =
  1/(γM_Ω²ε_θ) is exact for thermally-perfect gas (p/ρ = c²/γ with
  local γ). [PROVEN-HERE.]
  Correction: one sentence: "the (γ−1)h forms of χ and β_w are
  γ = const conversions of the exact ratios ε_θ(Ωr)²/h0 and
  p/(ρh0); magnitudes SCALING-ESTIMATE at working γ."

DEFECT 7 — INTERNAL COEFFICIENT INCONSISTENCIES (three instances).
MINOR, class (b) (numbers, not orders).
  (7a) E1: "Δε_θ ≈ a_p St_n/(γM_Ω²) ≈ 0.15 a_p St_n". At the file's
  OWN declared working values (γ = 1.2, M_Ω = 2, §2.2 header):
  1/(γM_Ω²) = 0.208, not 0.15; range over the stated M_Ω = 1.5–2.5:
  0.13–0.37. The headline range "0.01–0.10" should read ≈
  0.015–0.15 at working values (top of range +50%). (7b) §2.1
  torque-vs-axial "≈ 0.5 a_p St_n": working M_x/M_Ω = 1.5/2 = 0.75
  gives 0.75 a_p St_n; 0.5 corresponds to no declared value pair
  (edge 1/1.7 = 0.59 at best). (7c) D4: "Λ ... 0.75·St_n working,
  i.e. 0.05–0.9": 0.75 × (0.1–1) = 0.075–0.75; the full
  M_x/M_Ω = 0.59–1.11 band gives 0.06–1.11; "0.05–0.9" matches
  neither. [PROVEN-HERE, arithmetic.] Correction: recompute all
  three from one declared tuple and propagate to the E1 headline
  and the summary. No ordering conclusion changes.

DEFECT 8 — a_Γ HYPOTHESIS UNNAMED UNDER THE "CO-LEADING" CLAIM.
MINOR, class (c).
  Where: §2.1 K_Γ ("torque ≈ sweep-of-Γ — CO-LEADING"). The
  comparison a_p St_n β_τ vs a_Γ St_n needs a_Γ ~ a_p; G2's
  hypothesis line covers a_ρ, a_u (and flags a_s, a_h0) but never
  names a_Γ. On swirl data with phase-locked Γ profiles a_Γ could
  be ≪ a_p, making torque strictly dominant (the target's own
  ε_θ → 0 limit, generalized). [PROVEN-HERE (inspection).]
  Correction: add a_Γ to the G2 hypothesis list; state co-leading
  as "for a_Γ ~ a_p".

DEFECT 9 — D.5(ii) SCOPE CAVEAT NOT CARRIED INTO R3. MINOR, class (e).
  Where: §3.2 R3 cites D.5(ii) for the margin direction. D.5(ii)'s
  own scope sentence: "this is a STATE-sensitivity statement ...
  across twins that hold other quantities fixed the induced (u, v)
  readjustment is a solution property, priced by its own
  comparison, not by this formula." R3's ΔM_x/M_x = +(γ−1)M_θ²/4
  is the fixed-(u,v) piece only; the 4F-vs-5F solution comparison
  re-adjusts (u,v) at the same order (R1's mass-flux
  redistribution). Direction claim survives; the printed number is
  the state-sensitivity part alone. [PROVEN-IN-RECORD (D.5 scope) +
  PROVEN-HERE.] Correction: one clause carrying the caveat.

DEFECT 10 — ADVECTIVE/DIV-FORM BRIDGE UNSTATED. MINOR, class (e).
  §2.1–2.3 order the ADVECTIVE K rows; §2.4 and §4 use the
  DIV-FORM F_φ,rel atoms. D.18 (r4, L1-5) makes the two readings
  equal only MODULO the invertible triangular K_ρ recombination
  (div-row = advective row + coeff·K_ρ, with ρ factors on s/h0) —
  and brands transcribing one as the other "exactly the
  type-mismatch defect class this document prosecutes". Order-level
  impact NIL (each recombination adds an O(a St_n)-class piece),
  but the file should state the bridge once. [PROVEN-IN-RECORD.]

DEFECT 11 — E5/§2.4 OBLIQUITY NOTATION AMBIGUOUS BY n/2π. MINOR,
class (b, cosmetic).
  §2.4: "n_φ/n_x ~ Λ·(∂x_s/∂φ)/L on a helical sheet x = x_s(φ)".
  With φ the PHYSICAL azimuth (as "x = x_s(φ)" reads), n_φ/n_x =
  x_s′/r = (∂x_s/∂φ)/R_m, which is (n/2π)× the displayed formula;
  the display is correct only for the CELL coordinate φ̃ ∈ [0,1).
  The E5 operational form Λ·(Δx_s/L) (per-cell modulation) is the
  correct one. [PROVEN-HERE: normal of x − x_s(φ) = 0 is
  ∝ (1, 0, −x_s′/r) in (x, r, rφ).] Correction: write the sheet as
  x = x_s(φ̃) or carry the n/2π.

DEFECT 12 — ADJOINT-LEG INHERITANCE ANCHOR INCOMPLETE. MINOR,
class (e).
  §4.2 P4 / claim 17 inherit "the S1 conditional" for adjoint
  uniqueness. The record's named condition for the FIVE-field
  adjoint solve is N6 §4: "per-phase well-posedness of L*h = K
  (inherits the D2.5 conditional [C-D25U])", with the optimality
  ASSEMBLY (wall transversality with centrifugal contribution,
  corners) separately SCHEMA. J_1 needs only the response-adjoint
  solve, so the target's structure is right, but the precise
  inherited conditional is D2.5/[C-D25U] via N6 §4-§5, not a bare
  "S1 apparatus". [PROVEN-IN-RECORD, N6 §4–§5.] Correction: name
  D2.5/[C-D25U] in claim 17's conditional list.

DEFECT 13 — SCRIPT HYGIENE (does not affect verdicts). MINOR.
  `swirl5f_ray_check.py`: line 49 dead code (Γ-row entry built then
  overwritten at line 53 — momentum form used, declared, r-factor
  immaterial for homogeneity); the non-ray rejector's `d_bad` is
  computed and unused (`d_bad2` is the live check, and it is
  correct). RH homogeneity and sheet k-invariance are inferred, not
  machine-checked — the FILE scopes its machine-check sentence
  honestly, but any committed carrier (the named F2 duty) must add
  RH rows + a corrupted-source rejector (the author's R1′ rejects
  only the non-ray direction, not a transcription error in
  F_φ,rel: my independent transcription now covers that
  common-mode hole for this review). [PROVEN-HERE.]

NON-DEFECTS verified against my own attack (for the next stage's
economy): the master formula; every §2.2 order entry; the six-row K
census completeness at the advective level (machine-executed
independently); torque/work single-mechanism (χβ_τ = β_w exact);
S.22-g3 reconciliation (§2.5 reading is correct); R1's derivation
and magnitude (γM_θ²α_gap, ln → α_gap thin-annulus step exact);
FLAG-1 (fair reading of problem book §8:462-464 — the "≪" is indeed
an overstatement at measured ε_θ); the concordance check (0.85–1.67
reproduced); C51 anchor (|u_θ − Ωr| > a matches ledger line 671);
M_Ω/Λ/χ new-namedness (grep over docs/ finds no prior naming —
query-bounded to docs/); H3-w is genuinely required for P5 at five
fields and is properly surfaced with its O(a_w St_n) channel; the
E7 kernel statement matches D.18's proof text; E8's g2b quote is
accurate; P1–P5 survive an independent r-weighted transcription
including the Ωrp energy content.

==============================================================================
## §3 Per-main-claim verdicts

| # | Author claim (summary numbering) | Verdict |
|---|---|---|
| 1 | Group census + master formula + new-named groups + concordance + FLAG-1 | CONFIRMED (Defects 5, 6, 7c, and the M_Ω range note: 1.5–2.5 imports the D_CJ physical argument — concordance alone gives 1.0–3.3) |
| 2 | Residual ordering (sweep/drift/torque/work rows + G-f inheritance) | CONFIRMED as scale ratios; §2.3 census exhaustiveness REFUTED AS PRINTED (Defect 2: six drift pieces, not five; internal contradiction with §2.2 "all rows"); ordering magnitudes unaffected |
| 3 | 4F→5F removed errors R1–R5 + protection asymmetry | R1 CONFIRMED; R2 GAP-NAMED (Defect 3: fold-variant only); R3 CONFIRMED (Defect 9 caveat); R4, R5 CONFIRMED; claim 16 "largest unprotected class" GAP-NAMED (Defect 4: holds as QUANTIFIED-class ordering, St_n-conditional, pending P-ii/S.22) |
| 4 | Five-field ray-cancellation P1–P6 under H3+(H3-w), machine-checked | CONFIRMED at the stated algebraic grade (independently re-verified, incl. a transcription the author's script does not cover); inheritance anchors need Defects 1, 12 repairs; committed-carrier duty correctly named |
| 5 | Escape list E1–E11 | CONFIRMED in structure and groups; E1 coefficient inconsistent with own working values (Defect 7a); E5 notation (Defect 11); no missing escape found by this lens |
| — | §0 inheritance declaration ("no claim exceeds record status") | REFUTED as printed for the D.18 iff labels (Defect 1 — SCHEMA of record, not THEOREM*/SCHEMA); correct for G-f |

BOTTOM LINE (referee): no CRITICAL defect. The asymptotic core —
master formula, order table, six-row census at the advective level,
and the five-field homogeneity/ray-cancellation algebra — SURVIVES
independent re-derivation and an independent machine check. Four
MAJOR defects require repair before the file is consumed downstream:
one stale record-label inheritance (D.18 iffs are SCHEMA per
J-r2p-2/3), one false exhaustiveness claim (drift census 5 vs 6),
one variant-conditional headline number (R2), and one label
overclaim on the value-proposition assembly (claim 16). All four
have exact corrections written above; none changes an order-of-
magnitude conclusion, but Defects 3 and 4 together weaken the
upgrade's net-value claim from absolute to
"largest-QUANTIFIED-class, St_n-conditional".

ARTIFACTS: this file; `swirl5f_refute_asy_check.py` (independent
referee check, output quoted in §0). No repo file touched.
