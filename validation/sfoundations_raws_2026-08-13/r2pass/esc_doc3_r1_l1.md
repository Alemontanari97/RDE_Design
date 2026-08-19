# ESCALATION REFUTATION — DOC-3 (phaseD_L4_implies_R1.md), round 1, lens l1

**Slot**: adversarial refuter, until-dry ROUND 1 on the r3 escalation-repair text.
**Lens**: gas-dynamics / physics, RH algebra, counterexamples.
**Scope (strict)**: ONLY the r3-edited passages of `phaseD_L4_implies_R1.md` —
escalation **E-4** (leg 14: Proposition 1'' restatement, (D-coll), (H-UP-fam),
retraction block, two-face bootstrap, status/accounting, r3 mid-face falsifier
leg, consumer updates in 3.4(3)(a) / Section 5 clause (i) / register row 1' /
NG-9 row) and amendment **A-2** (leg 17: Remark 1.5.5 mechanism replacement),
per `r2pass/VERDICT_r2pass.md` §4(c) and §3. Theorem 1' (leg 12) and Lemma 1.4
(leg 13) are CONFIRMED-of-record and are NOT attacked; their statements are
consumed here only to check the r3 text's applications of them.
**Discharge audit mandate**: verify the repairs actually discharge L0-7
(`refute_r2batch_l0.md` lines 485-534), L1-7 and L1-8 (`refute_r2batch_l1.md`
lines 475-522, 567-605). **Dedup**: no objection already dispositioned is
re-raised; where a disposition is examined, the ID is cited and the disposition
is either confirmed or attacked on its own text.

Attack classes: {BREAKS-THE-LEG, REPAIR-NEEDED, AMENDMENT}. Every examined
passage that survived is listed CONFIRMED with the strongest attack tried.

==============================================================================
## §A DISCHARGE VERIFICATION (the sustained objections vs the delivered repairs)

### A.1 L0-7(a) / L1-7(i) — quantifier order, no uniform eps_1: **DISCHARGED**

The r3 proof sets `eps_1 := d_0 / (2 lambda_max)` (line ~654) with
d_0 = dist(Gamma_mid, Gamma_in^coll ∪ Gamma_I) > 0 fixed by (D-coll) and
lambda_max = sup over C_h × [0,T_f] of (|u-bar| + c-bar), finite by (H1.1') +
(G3)-box on the collar. This eps_1 is a constant of the collar geometry and
the collar base state, declared BEFORE any subdomain enters, and no
exhausting-family quantifier appears anywhere in the r3 argument. Re-derived:
for t in (t*, t*+eps_1], lambda_max·(t−t*) ≤ d_0/2 < d_0, so the required R
with lambda_max(t−t*) < R < d_0 exists — the window arithmetic closes with
uniform slack. Defect (a) is gone at the root, not patched.

### A.2 L0-7(b) / L1-7(ii) — trace ON the source face at distance zero: **DISCHARGED**

The face whose trace the continuation consumes is now Gamma_mid — an INTERIOR
surface of the collar at the FIXED distance d_0 from BOTH data-carrying faces
(Gamma_in^coll and Gamma_I). (MID-TRACE) is derived by Lemma 1.4 frusta based
at points x_0 ∈ Gamma_mid with radius R < d_0: I verified that
B(x_0, R) ∩ (Gamma_in^coll ∪ Gamma_I) = ∅ (dist(x_0, ·) ≥ d_0 > R), so the
frustum meets ∂C_h only in wall portions — exactly Lemma 1.4's admissible
class, with the interface clause not even needed. The conclusion is evaluated
at interior points of the collar (positive frustum radius at time t), never on
a face carrying uncontrolled data. The circularity is structurally absent: the
mid-trace derivation consumes NO face input (only U(·,t*) = 0 on collar balls,
supplied by t*-maximality + continuity); Theorem 1' (STEP 2) and (H-UP-fam)
(STEP 3) then each consume (MID-TRACE) as an already-established output.
Defect (b) is gone.

### A.3 The proves-too-much test (VERDICT §5, leg-14 falsifier note): **PASSED**

I ran the judge's own test against the new proof: for a bare transmission
coupling of two subdomains across one face with no transmission condition,
STEP 1 is unavailable — there is no certified-W^{1,infinity} overlap region in
which a proved finite-speed lemma can carry zero data from the coupling
surface's neighborhood to a second surface at positive distance. The delivered
argument consumes exactly the two structural assets a bare coupling lacks
(the monitored collar overlap for Lemma 1.4; the margin outflow face for
Theorem 1'), and the document says so explicitly (lines ~695-703). The r3
paragraph's self-application of the test is correct as written.

### A.4 (H-UP) restatement vs the E-4 spec: **COMPLIANT** (one attribution nit, F-4 below)

E-4 demanded: restate (H-UP) (half-collar-face decomposition / family of
collar depths, OR trace-level determinism) and rewrite the bootstrap via the
two-face argument (Lemma 1.4 frusta to the mid-collar face + Theorem 1' on the
half collar + (H-UP) on the enlarged interior). Delivered: (H-UP-fam)
family-of-depths uniqueness form + (D-coll), two-face bootstrap exactly per
spec, route (r-a) explicitly NOT consumed, r2 proof retracted-and-retained
with grounds matching L0-7(a)/(b) = L1-7(i)/(ii) verbatim in content, label
held at SCHEMA per J-r2p-1 with the restoration channel named. The two
declared deltas vs the r2 (H-UP) are content-honest: (i) the
finite-speed clause is genuinely no longer consumed anywhere (STEP 3 uses
uniqueness only; STEP 1's finite speed is Lemma 1.4 on the collar, a proved
statement); (ii) the S1-burden invariance claim checks — the S1 discontinuity
set lies in Omega_up \ C_h ⊆ Omega_int^s for EVERY depth s, since (H1.1')
makes W-bar W^{1,infinity} on all of C_h, so enlarging the interior by collar
territory adds no front.

### A.5 L1-8 / A-2 (leg 17): **DISCHARGED**

A-2 demanded the eigenprojector-degeneracy mechanism be replaced by the
sign-classification jump of the incoming/outgoing split, with the
eigenstructure declared regular at u-bar·n ∈ {0, −c-bar} for c-bar > 0. The r3
Remark 1.5.5 does exactly that, retires the "1/c factors against closing
spectral gaps" parenthetical with an of-record annotation naming it a c → 0
mechanism not at issue, and leaves conclusion and scoping unchanged — all
three A-2 requirements. RH-algebra re-check (this lens): Lemma 0.2's
eigenvectors r_∓ = (rho, ∓c n, rho c²), r_s, r_{t_i} do not depend on u-bar·n
at all (A(n) depends on u·n only through the (u·n)I diagonal shift), so
"unaffected" is true and even understated; at u·n = −c it is the λ_+ mode
crossing zero (incoming count 4 → 5 into supersonic inflow), at u·n = 0 the
triple λ_0 eigenspace crosses (grazing/injector rim) — the fixed-mode
class-flip mechanism is the correct one at both loci.

==============================================================================
## §B ATTACKED PASSAGES

------------------------------------------------------------------------------
### F-1 — REPAIR-NEEDED (leg 14): the restated Claim (and (H-UP-fam), and Status (a)) omit the same-forcing clause the proof consumes

Verbatim quotes (all r3-restated text):

> "**Claim.** Assume Theorem 1''s hypotheses on the collar C_h, (D-coll), and
> (H-UP-fam). Then two solutions with the same data on Omega_up (initial data
> + Gamma_in data/BC), differing arbitrarily downstream of Gamma_I, coincide
> on Omega_up x [0, T_f]."  (~line 608)

> "has the UNIQUENESS property: two solutions with the same initial data on
> Omega_int^s at a time t_0, the same Gamma_in data/BC, and the same trace on
> Gamma^coll_s x [t_0, t_1] coincide on Omega_int^s x [t_0, t_1]."  (~line 593)

> "U is a C^1 solution of the homogeneous (LIN-U) on C_h ((H1.4); the
> forcings cancel on Omega_up)"  (~line 665)

> "(a) If W-bar is W^{1,infinity} on all of Omega_up, (H-UP-fam) IS a theorem
> of this document at every depth"  (~line 706)

Attack (derivation level, counterexample lens). Theorem 1 defines its solution
pair WITH the clause "(same base state, same forcing f on Omega_up)" — that
clause is load-bearing: it is what makes the difference U solve the
HOMOGENEOUS (LIN-U) on Omega_up. The r3-restated Claim replaces it with an
explicit enumeration — "(initial data + Gamma_in data/BC)" — that DROPS the
forcing clause, while the r3 proof consumes it in so many words ("the forcings
cancel on Omega_up"): STEP 1 needs homogeneity on C_h, and STEP 3's
(H-UP-fam) needs it on Omega_int^{h/2}. Counterexample against the literal
statements: take W-bar W^{1,infinity} on all of Omega_up (so even Status (a)'s
unconditional case applies), U^(2) := 0 with f^(2) := 0, and U^(1) the solution
generated by a forcing f^(1) = phi compactly supported in
Omega_int^{h/2} × (0, T_f) with zero initial data — physically, a per-phase
heat-release/source perturbation inside the rotating-wave region, upstream of
the collar. The pair satisfies every hypothesis the r3 Claim enumerates (same
initial data on Omega_up; same Gamma_in data/BC; nothing differs downstream of
Gamma_I) and every clause of (H-UP-fam)'s enumeration on any window before the
signal reaches the faces, yet U^(1) ≠ U^(2) on Omega_int^{h/2}. The same pair
refutes Status (a)'s sentence "(H-UP-fam) IS a theorem of this document" as
literally quantified — the (EI) argument sketched there silently uses the
homogeneous difference. The defect is a statement-enumeration omission, not a
proof defect: the proof handles forcing correctly, and Theorem 1 two
subsections up spells the clause out. But the r3 Claim and (H-UP-fam) are the
register-consumable statements of record (row 1', Section 5(i)) — a consumer
transcribing them gets a false statement.
Repair (one clause, three sites): add "same forcing on Omega_up" (equivalently
"solutions of the same linearized problem on Omega_up, forcing free
downstream") to the Claim's parenthetical; add "same forcing on Omega_int^s"
(or "of the same interior problem") to (H-UP-fam)'s uniqueness enumeration;
let Status (a) inherit it. Until landed, the "delivered strength = THEOREM
modulo (H-UP-fam)" sentence is qualified by exactly this clause.
**Class: REPAIR-NEEDED** (statement/accounting must change contentfully —
same shape as the judge's L1-2 precedent, "incomplete by one named
condition"; not BREAKS: the two-face architecture is untouched and the
intended reading is recoverable from Theorem 1's frame on the same page).

------------------------------------------------------------------------------
### F-2 — AMENDMENT (leg 14): (H-UP-fam)'s family quantifier ranges over an unconstructed family, and its stated range (0, h] contradicts its own parenthetical

Verbatim quote (~lines 589-597):

> "For every collar depth s in (0, h], the linearized interior problem on
> Omega_int^s := Omega_up \ closure(C_s) — ... — has the UNIQUENESS property
> ... (The proof below consumes ONLY the depth s = h/2, with
> Gamma^coll_{h/2} = Gamma_mid; the family form is stated because the mid-face
> depth is a choice, not a structure — any fixed s in (0, h) with its
> d_0(s) > 0 runs verbatim.)"

Attack. (i) The family {C_s, Gamma^coll_s : s in (0, h]} is defined nowhere
for the general Lipschitz axisymmetric geometry: C_h itself is hypothesized
(Theorem 1'), C_{h/2} and Gamma_mid are supplied by (D-coll), the planar case
gives the obvious foliation — but "the one-sided collar of Gamma_I of depth s"
for arbitrary s has no construction in the document, so the hypothesis
quantifies over objects the reader cannot instantiate. (ii) The stated range
includes s = h, where Gamma^coll_h = Gamma_in^coll and d_0(h) = 0; the
parenthetical's own verbatim-runs clause is stated for "any fixed s in (0, h)
with its d_0(s) > 0", excluding the endpoint the displayed range includes.
Including s = h is mathematically harmless (it reproduces the r2 uniqueness
clause, never consumed by the new proof), but the hypothesis of record is then
strictly stronger than anything used, over a family partly undefined and with
an endpoint its own commentary disowns. Since the proof consumes ONLY s = h/2
— whose existence and Lipschitz split is exactly (D-coll)'s content — the
defect does not propagate into the derivation.
Repair wording: either state (H-UP-fam) at the single consumed depth h/2 ("at
the (D-coll) split"), or keep the family form with the quantifier restricted
to "every s for which a (D-coll)-class split (C_s, Gamma^coll_s, d_0(s) > 0)
is given". **Class: AMENDMENT.**

------------------------------------------------------------------------------
### F-3 — AMENDMENT (leg 14): the bootstrap window overruns T_f near the final time

Verbatim quotes (~lines 662, 691-693):

> "STEP 1 ... Fix t in (t*, t* + eps_1] and x_0 in Gamma_mid ..."

> "UNION. ... U == 0 on Omega_up x [0, t* + eps_1] with the FIXED eps_1 above
> — contradicting the maximality of t*."

Attack. If t* > T_f − eps_1, times t in (T_f, t* + eps_1] do not belong to the
solution's domain [0, T_f]: STEP 1 evaluates U at nonexistent times and the
UNION display asserts vanishing on a window exceeding the domain. The argument
is repaired by one substitution — run the three steps on
(t*, t* + min(eps_1, T_f − t*)] and conclude either the contradiction (when
t* + eps_1 ≤ T_f) or directly U == 0 on Omega_up × [0, T_f] (when not). No
content moves; the retracted r2 display had the same silent convention and it
went unflagged in round 2, but the escalation text is held to the document's
own minted standard ("the line must be WRITTEN"). **Class: AMENDMENT.**

------------------------------------------------------------------------------
### F-4 — AMENDMENT (leg 14, audit trail): "the (H-UP) form consumed is L1-7's route (r-b)" misattributes which lens supplied the hypothesis FORM

Verbatim quote (disposition table row L1-7, ~line 124, repeated at ~line 599):

> "the (H-UP) form consumed is L1-7's route (r-b) = L0-7's named repair route
> (half-collar/two-face, family of collar depths)"

Attack (against the disposition's own text; not a re-raise of L1-7 — its
mathematical content is discharged, §A.2). L1-7 offered (r-a) = the (H-UP)
RESTATEMENT route (trace-level determinism folded into the hypothesis) and
(r-b) = "a two-sided lens-shaped energy argument STRADDLING the face" — an
argument shape, explicitly not a hypothesis restatement, and one whose
geometry (a lens across Gamma_in^coll) the delivered proof does not use: the
r3 frusta live wholly inside C_h and nothing straddles any face. The (H-UP)
FORM actually consumed — family of collar depths — is L0-7's parenthetical
"(or for a family of collar depths)". The judge's E-4 merge legitimately
identifies the CONSTRUCTION both lenses converge on; the r3 sentence goes
further and equates (r-b), as written, with the delivered hypothesis form.
A future auditor reading L1-7 against this disposition will not find the
claimed match. Repair wording: "the construction is the one both lenses
converge on (E-4's spec); the (H-UP) FORM consumed is L0-7's family-of-depths
restatement; L1-7's (r-b) ingredients (Lemma 1.4 frustum + (H-UP)-class
estimate) are consumed, its lens geometry is not; (r-a) is NOT consumed."
**Class: AMENDMENT** (attribution wording in the of-record audit trail;
no derivational content moves).

------------------------------------------------------------------------------
### F-5 — AMENDMENT (leg 14): the r3 mid-face falsifier leg's trigger predicate is ambiguous and can false-reject under one natural reading

Verbatim quote (~lines 732-737):

> "in the roughened-exterior run, probe the trace on the mid-collar face
> Gamma_mid over a window [t_p, t_p + d_0/(2 lambda_max)] following any
> instant t_p at which the upstream field is at the scheme bound: the
> mid-face trace must stay at the scheme bound over that FIXED window (the
> (MID-TRACE) step)"

Attack (R5 discipline: a falsifier must reject correctly, in both
directions). STEP 1's prediction requires the field at t_p to be at the
scheme bound on the collar balls B(x_0, R) ∩ C_h, R < d_0 — i.e. ON THE
COLLAR around Gamma_mid. The trigger says "the upstream field", two sentences
after the same paragraph uses "the upstream-of-collar response" for the
upstream-of-collar region. Under the reading "upstream-of-collar field at the
bound" (collar state unconstrained at t_p), a correct implementation can
legitimately show mid-face growth inside the window — sourced by collar
content present at t_p — and the leg would false-reject sound wiring. Under
the reading "field on Omega_up (collar included)", the leg is exactly the
(MID-TRACE) prediction and is correct, including its window constant
d_0/(2 lambda_max) = eps_1 (checked against STEP 1's arithmetic; a Gronwall
factor e^{C_0 eps_1} on the bound is absorbed in "scheme bound" language).
Repair wording: "...at which the field ON THE COLLAR C_h (a fortiori on
Omega_up) is at the scheme bound...". **Class: AMENDMENT.**

------------------------------------------------------------------------------
### F-6 — AMENDMENT (leg 17): "mutual spectral gaps equal to c-bar" is false for the extreme acoustic pair

Verbatim quote (Remark 1.5.5, r3 text, ~lines 536-538; same phrase in the
revision-log L1-8 row, ~line 125):

> "for c-bar > 0 the eigenvalues u-bar.n - c-bar, u-bar.n, u-bar.n + c-bar
> keep mutual spectral gaps equal to c-bar at those loci"

Attack (RH algebra). The pairwise gaps of the three distinct eigenvalues are
|λ_0 − λ_−| = c, |λ_+ − λ_0| = c, and |λ_+ − λ_−| = 2c: at u·n = 0 the
spectrum is {−c, 0(×3), +c}, at u·n = −c it is {−2c, −c(×3), 0} — in both
cases the (λ_−, λ_+) gap is 2c-bar, not c-bar. "Mutual ... equal to c-bar" is
literally false for that pair. The load-bearing fact — the minimum gap between
distinct eigenvalues stays ≥ c-bar > 0, so no eigenvalue collision and no
projector degeneracy occurs at the crossings — is true and is all the
regularity claim needs. The phrase is inherited from VERDICT_r2pass act (vii)
("keep mutual gaps = c > 0") and from L1-8's own text ("keep MUTUAL gaps equal
to c"); the escalation text is nevertheless the text of record and should not
carry a false equality into M0. Repair wording: "keep ADJACENT spectral gaps
equal to c-bar (all pairwise gaps ≥ c-bar)". Conclusion, mechanism, and
scoping unaffected. **Class: AMENDMENT.**

==============================================================================
## §C CONFIRMED PASSAGES (strongest attack tried, each)

- **(D-coll)** (~lines 582-587). Attack tried: whether d_0 > 0 plus the
  Lipschitz split can fail to exist for a legitimate collar (nonconvex duct,
  wall-touching mid-face boundary curve). Fails to break: (D-coll) is a
  HYPOTHESIS, honestly declared, trivially satisfiable in the planar
  station-cut case the pipeline uses (d_0 = h/2), and the wall-corner points
  of Gamma_mid are covered because Lemma 1.4's conclusion holds on
  F ∩ (closure(O) × [t_0, t_1]) and U is C¹ up to the closure. CONFIRMED.
- **eps_1 uniformity display** (~line 654). Attack tried: hidden state
  dependence of lambda_max (time-dependent base). Fails: the sup is taken
  over C_h × [0, T_f] of record, majorizing Lemma 1.4's per-region constant;
  finiteness from (H1.1') + (G3)-box. CONFIRMED (modulo F-3's T_f cap).
- **STEP 1** (~lines 659-676). Attacks tried: (i) frustum touching
  Gamma_in^coll or Gamma_I — killed by dist(x_0,·) ≥ d_0 > R, ball
  arithmetic re-derived; (ii) Lemma 1.4 hypothesis mismatch (zero-data set,
  wall-only boundary contact, C¹ class, homogeneity) — all match the
  CONFIRMED Lemma 1.4 statement verbatim (homogeneity itself is F-1's clause,
  charged there, correctly handled in the proof); (iii) closed-window left
  endpoint of (MID-TRACE) — supplied by U(·, t*) = 0 via continuity, stated.
  CONFIRMED.
- **STEP 2** (~lines 678-683). Attack tried: Theorem 1' time-shifted without
  restatement (non-autonomous coefficients), and (D'') for C_{h/2}. Fails:
  the energy argument is time-local (Gronwall from E(t*) = 0), hypotheses
  (H1.1')-(H1.4) hold on the subwindow by restriction, and (D-coll) supplies
  the Lipschitz clause for C_{h/2} explicitly. The hypothesis-(ii) full-trace
  agreement on Gamma_mid is exactly (MID-TRACE), pointwise for the C¹
  representative — no trace-theory debt. CONFIRMED.
- **STEP 3 + UNION** (~lines 685-693). Attack tried: partition gap or
  double-use of the mid trace — Omega_up = Omega_int^{h/2} ⊔ Gamma_mid ⊔
  C_{h/2} is exact (walls and Gamma_I are not in the open Omega_up), and
  (MID-TRACE) is an established output consumed by both sides, not a
  circularly fed input. Residual circularity hunt (this round's core duty):
  none — the dependency order is strictly t*-data → (MID-TRACE) → {STEP 2,
  STEP 3}. CONFIRMED (modulo F-3's window cap).
- **Retraction block** (~lines 620-645). Attack tried: whether the retained
  r2 text or the retraction grounds misstate L0-7/L1-7 (a disposition-level
  failure). Fails: the quoted retracted proof matches the round-2 quotes
  verbatim, and grounds (a)/(b) reproduce the two defects at full strength,
  including the proves-too-much sentence. Retained-not-erased per house
  discipline. CONFIRMED.
- **"Why this does not prove too much"** (~lines 695-703). Attack tried:
  find a bare-coupling instantiation that survives the paragraph's test
  (§A.3). Fails. CONFIRMED.
- **Status (a)/(b) of (H-UP-fam)** (~lines 705-718). Attacks tried: (i) the
  (a)-case energy argument needs a sign on A(n) at the face — it does not
  (integrand zero pointwise where the full trace vanishes; re-derived);
  (ii) the S1-burden-unchanged claim — holds, fronts lie outside C_h for
  every depth (§A.4); (iii) NG-9 scope drift — the r3 NG-9 row correctly
  narrows to uniqueness-only and correctly notes the Prop 1'' label is gated
  on the E-4 adjudication, not on NG-9 alone. CONFIRMED (modulo F-1's clause
  in the (a)-case sentence).
- **Label/rigor block** (~lines 612-618). Attack tried: whether "delivered
  strength = THEOREM modulo (H-UP-fam)" jumps the judge's downgrade-only
  channel. Fails: the label OF RECORD is kept SCHEMA per J-r2p-1, the
  restoration channel is named as the E-4 adjudication "and no other", and
  the strength sentence is a self-assessment explicitly subordinated to it
  (qualified by F-1 until the clause lands). CONFIRMED.
- **Consumer updates** (revision log ~lines 127-131 vs body). Checked all
  four named sites: 3.4(3)(a) (~line 1298), Section 5 clause (i)
  (~lines 1561-1565), register row 1' (~line 1612, including the r3 mid-face
  falsifier leg and the dropped finite-speed clause), NG-9 row (~line 1668).
  All carry (H-UP-fam) + SCHEMA-per-J-r2p-1 consistently; grep of every "r3"
  token in the document shows no edit outside the declared E-4/A-2 scope +
  log/register. Attack tried: a consumer still citing "(H-UP)" or "THEOREM
  modulo" unhedged — none found. CONFIRMED.
- **A-2 replacement mechanism** (Remark 1.5.5, ~lines 531-548). Attacks
  tried: (i) eigenvector claim — Lemma 0.2's eigenvectors are u·n-independent,
  so regularity at the crossings is exact; (ii) crossing arithmetic — at
  u·n = −c it is λ_+ that crosses zero (count 4→5), at u·n = 0 the triple λ_0
  (grazing): both consistent with "a fixed, regular mode flips class as its
  eigenvalue crosses zero"; (iii) "ill-defined ON them" over-claims under a
  strict-sign convention (span{λ<0} is defined on the locus) — fails to
  break: the prescription "the same characteristic components" must classify
  the zero-eigenvalue mode, for which the incoming/outgoing split genuinely
  gives no answer, matching L1-8's own "at the crossing point ill-defined";
  (iv) the retirement annotation — correctly identifies the retired
  parenthetical as a c → 0 mechanism, which is L1-8's exact point.
  CONFIRMED (modulo F-6's gap wording).

==============================================================================
## §D SUMMARY TABLE

| ID | Target (r3 text) | Class | One-line claim |
|---|---|---|---|
| F-1 | Prop 1'' Claim + (H-UP-fam) + Status (a) | REPAIR-NEEDED | Same-forcing clause omitted from the statement enumerations; proof consumes it; literal statements refutable by an interior source-perturbation pair |
| F-2 | (H-UP-fam) quantifier | AMENDMENT | Family (0, h] quantifies over an unconstructed collar family; s = h endpoint contradicts the row's own d_0(s) > 0 parenthetical; only s = h/2 is consumed |
| F-3 | STEP 1 window / UNION display | AMENDMENT | eps_1 window overruns T_f when t* > T_f − eps_1; cap at min(eps_1, T_f − t*) |
| F-4 | Disposition row L1-7 / "Which (H-UP) form" | AMENDMENT | (r-b) as written is a face-straddling lens argument, not the delivered hypothesis form; the form is L0-7's family-of-depths route |
| F-5 | r3 mid-face falsifier leg | AMENDMENT | "upstream field at the scheme bound" ambiguous; the collar-inclusive reading is the correct trigger, the other false-rejects |
| F-6 | Remark 1.5.5 + log row L1-8 | AMENDMENT | "mutual spectral gaps equal to c-bar" false for the (λ−, λ+) pair (gap 2c-bar); operative fact is min gap ≥ c-bar |

**BREAKS-THE-LEG: 0. REPAIR-NEEDED: 1 (F-1). AMENDMENT: 5 (F-2..F-6).
Total findings: 6.**

Discharge verdicts: L0-7(a),(b) DISCHARGED; L1-7(i),(ii) DISCHARGED (with the
F-4 attribution nit in the audit trail); L1-8/A-2 DISCHARGED (with the F-6
wording nit). The two-face bootstrap survives this lens's strongest attacks:
no residual circularity, the proves-too-much test passes, and the delivered
strength is THEOREM modulo (H-UP-fam) ONCE F-1's one-clause statement repair
lands — label motion remains the E-4 adjudication's alone (J-r2p-1).

==============================================================================
## §E SELF-FALSIFIERS (what kills each finding)

- F-1 dies if a same-forcing stipulation for the Proposition-1''/(H-UP-fam)
  solution pairs is exhibited in the r3 text (not merely in Theorem 1's
  frame) — i.e. if "same data on Omega_up" is shown DEFINED anywhere of
  record to include the forcing.
- F-2 dies if a general-geometry construction of the depth-s collar family
  is located in the document, and the s = h endpoint is shown consistent
  with the d_0(s) > 0 clause.
- F-3 dies if the document declares a convention extending solutions or
  windows past T_f, or if t* + eps_1 ≤ T_f is somewhere guaranteed.
- F-4 dies if L1-7's (r-b) text is shown to state a hypothesis restatement
  in the family-of-depths form (it states "a two-sided lens-shaped energy
  argument straddling the face").
- F-5 dies if "the upstream field" is pinned of record to mean the field on
  all of Omega_up including the collar, in which case the leg is correct as
  written.
- F-6 dies if all pairwise gaps at the loci are shown equal to c-bar —
  refuted by the displayed spectra themselves ({−c, 0, c}: |λ_+ − λ_−| = 2c).
