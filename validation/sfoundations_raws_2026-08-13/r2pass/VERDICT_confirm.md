# VERDICT — S-FOUNDATIONS-C confirming round (until-dry closure pass), SUCCESSOR JUDGE

Date: 2026-08-19. Successor judge of record for the confirming round mandated
by `VERDICT_escalation.md` §6 R-1..R-3 (that verdict's §2/§3/§6 read first and
in full, per mandate). Paths relative to
`validation/sfoundations_raws_2026-08-13/`.

Inputs read IN FULL: the six confirming refutations
`r2pass/esc_doc{1,2,3}_confirm_l{0,1}.md`; `r2pass/VERDICT_escalation.md`
(§1-§7); the three target documents' newest revisions at every attacked
passage (doc1 = `phaseD/phaseD_stop_proof.md` revision 8, lines 2129-2380 +
§13 block 3825-4041; doc2 = `phaseD/phaseD_meanswirl_formalization.md` r7,
lines 1848-2142 + step-(1) chains 1920-1974; doc3 = `phaseD_L4_implies_R1.md`
r3.5, lines 915-990, 1015-1076, register 2013/2058-2081). Every quoted
passage adjudicated below was spot-checked verbatim against the on-disk
document THIS window; every refuter-vs-text or refuter-vs-refuter
disagreement was re-derived at pen grade (§5).

NULL=FAILURE CHECK: all six confirming slots exist on file, non-empty,
well-formed, two lenses per document, each ending in a machine summary;
each declares its scope sweep (grep-measured in its own window), its dedup
register, and its R-4 binding-rule audit. No slot dry-counted; no artifact
overwritten (all six were unclaimed filenames). PASS.

DRY CRITERION OF RECORD FOR THIS ROUND (orchestrator decision, declared in
the launching brief and adopted here): a document is DRY when the confirming
round sustains ZERO BREAKS-THE-LEG and ZERO REPAIR-NEEDED findings;
sustained AMENDMENTS (wording-class only) do NOT block dryness — each is
adjudicated below, the sustained ones are listed in §4, and they are applied
at the M0-landing composition citing this verdict (no further round). This
REFINES the documents' own zero-findings criterion; the refinement is the
caller's authority, not this judge's.

==============================================================================
## §1 PER-FINDING ADJUDICATION

Raised across the six files: doc1 = 7 (ECL0-1..3 l0 + ECR1-1..4 l1, with one
cross-lens merge); doc2 = 5 (CR-1/CR-2 l0 + R4L1-1..3 l1, with two cross-lens
merges); doc3 = 5 (ESC5-1..3 at l0 + ESC5-1..2 at l1 — NOTE OF RECORD: the
two doc3 lenses independently minted colliding "ESC5-*" IDs with DIFFERENT
contents; disambiguated here as ESC5-n(l0)/ESC5-n(l1); one cross-lens merge).
Distinct findings adjudicated: 6 + 3 + 4 = 13.

### DOC-1 (`phaseD/phaseD_stop_proof.md` revision 8, legs 3 + 5)

**ECL0-1 (root-quantifier parity clause, l.2162-2172 + summary 2173-2176 +
§13 falsifier 3831-3835): SUSTAINED-REPAIR-NEEDED.** Judge re-derivation
(full, at pen grade): (i) the parity bracketing ("e(v,.) passes from above
the level just after the first root to below it just before the second, so
an intermediate root with e_S <= 0 exists") is EXACT on an interval S-slice
(IVT at the first downward crossing) and CONSUMES the traversed interval
lying in the EOS domain; (ii) §1 pins no EOS domain — established, sustained
and consumed of record at ER3L1-2, whose accepted (m2)/(m3) patch witnesses
are partially-defined EOS; (iii) the refuter's two-branch witness CHECKS:
e = e0(v) + h_i(S) on (v-range) x ([0,1] ∪ [10,11]), h_1 = 5^S - 1 (range
[0,4], h_1' > 0, h_1'' > 0), h_2 = 1 + 2(S-10) + 0.1(S-10)^2 (range
[1,3.1] ⊂ (0,4), h_2' >= 2, h_2'' = 0.2) — Gibbs closure by construction,
c^2 = v^2 e0'' > 0, theta = h_i' > 0 at EVERY root (root-quantifier member
satisfied), Hess e = diag(e0'', h_i'') PD (strict pair + hull-theta
satisfied), totality satisfiable via the I1 branch (endpoint values 1.236
and 2.025 interior to (0,4)); at V (S_V = 10.5) the level 2.025 has an
I1-root AND the I2 data root, both theta > 0, NO intermediate root (nothing
between the branches is in the domain) — this is VERBATIM the §13 entry's
own registered kill condition ("exhibit a §1-class EOS with two theta > 0
roots ... and no theta <= 0 root between them"), firing; (iv) the chart is
two-valued at V, the per-segment continuation lands on
S_land = h_1^{-1}(2.025) ≠ S_V, and the granted item (i) for E = -rho S is
ill-posed as printed (S(W) not a function). Class adjudication: NOT wording
— a MISSING CONDITION MEMBER (S-slice connectedness) under which the
printed four-member condition of record fails to be sufficient on an
in-class witness, the exact E3L0-2 shape, REPAIR-NEEDED of the loop's own
severity calculus. The l1 lens's C.1 CONFIRMATION of the same passage does
not rebut it: l1's recorded strongest attacks (sign bookkeeping on
h = S^3 - 3S, v-domain exit, data-root landing) all ran on CONNECTED
domains — its own self-falsifier clause ("a derivation-level break the
recorded strongest attack missed") applies, and this judge sides with the
l0 witness on the re-derivation above. NOT BREAKS-THE-LEG (correctly
argued by the refuter): the route-level OPEN verdict is unmoved, the repair
strengthens the no-viable-abstract-EOS-route conclusion a sixth time, and
the clause is FREE at the standing gamma(T) closure (interval table domain,
AUD-cp discharge untouched — verified). Named repair adopted as the owed
spec: the slice-connectedness clause in the chart clauses + the §13
falsifier-line correction ("continuous e_S ON AN INTERVAL SLICE").

**ECL0-2 (l0) ≡ ECR1-1 (l1) (re-scoped falsifier consequent, l.2344-2361 +
§13 echo 3924-3928): SUSTAINED-AMENDMENT, merged at the clause.** Verified
verbatim on disk ("modulo the totality clause, which the whole-domain
reading also delivers"). Judge re-derivation: totality (eps(W_s) in the
range of e(v_s,.) at hull points) is domain/range GEOMETRY; pins constrain
e's derivatives where e is defined, never where it is defined — no reading
of "pins hold on the whole EOS domain" delivers it (witness class: the
a0-positive patch EOS, pins domain-wide, thin-S-band hull exits the range —
ER3L1-2's consumed mechanism). The transplant-inversion is documented: the
ER3L1-3 source text left totality OPEN ("modulo ER3L1-2's totality");
revision 8 appended the delivery claim — R-4 instance, both lenses
concurring independently. The else-branch under-enumeration (grant left
conditional on hull-theta alone, omitting the two chart members an
s-concavity-at-hull-states derivation presupposes) is exact. Class:
auxiliary falsifier-consequent text, the unbroken lineage class (EL0-4,
E2L0-2, E4L0-3, ER3L1-3 — all AMENDMENT of record); chart members retain
their own §13 falsifiers, so no false restoration can be silently recorded
without contradicting the register. AMENDMENT.

**ECL0-3 (§13 leg-3 dryness recital, l.3975-3981): SUSTAINED-AMENDMENT.**
Verified on disk: "zero sustained findings across l0 rounds 1-4 and l1
rounds 1-3" — false as printed (round 1 sustained EL0-1/EL0-2/ESC1-F1 at
leg 3, consumed AT revision 5, which the same sentence's "unchanged since
revision 5" presupposes; source rows verified in esc_doc1_r1_l0.md by the
refuter, self-consistency check by this judge). Count of record = the
escalation judge's (3 consecutive dry l0 rounds + 2 l1). Bookkeeping only;
the leg-3 dry STATUS is true and untouched. AMENDMENT.

**ECR1-2 (attribution witness restated without its determinant regime,
l.2212-2216 + §13 3874-3877): SUSTAINED-AMENDMENT.** Verified on disk:
the row prints "the (m2)-class quadratic patch with a0 large NEGATIVE
satisfies the strict pair everywhere", while (m2)'s printed exhibit
(l.2270-2272, verified) carries the OPPOSITE regime "a1^2 > e0'' b" —
under which the strict pair FAILS (judge arithmetic: e0'' = 2, a1 = 3,
b = 1 gives e0''b = 2 < 9 = a1^2). The valid witness (ER3L1-1's own,
regime e0''b > a1^2, a0 << 0) exists — the corrected attribution it
supports is true — but the load-bearing parameter clause was dropped in
restatement, against the row's own written-line standard. One-clause
repair as specified by the refuter. AMENDMENT.

**ECR1-3 (grant head + item-(i) annotation not propagated, l.2365-2374):
SUSTAINED-AMENDMENT.** Verified on disk: the operative granting sentence
still reads "under the STRICT + hull-theta condition of record" while
revision 8 itself enlarged the condition with the chart clauses and updated
every other carrier (header 102-105, status line, §9 table, §12-echo —
verified). The vacuous-satisfaction exposure is real (an empty root set
satisfies the universal root-quantifier; only totality excludes it) but
"condition of record" is a defined singular object (defined at 2129-2187
WITH the chart clauses), so a benign referential reading exists — the
ER3L1-3 precedent class exactly. Two-phrase repair as specified. AMENDMENT.

**ECR1-4 (honest residue (2) instance count, l.4019-4021):
SUSTAINED-AMENDMENT.** Verified on disk ("now SIX declared instances").
The refuter's file-measured partition (4 declared at rev 7 + 4 new distinct
events this window, two of them recorded as spec-seeded by the same §13
block's own entries) yields EIGHT distinct events / TEN seeded findings;
no six-event partition exists without dropping events the block itself
records. SR-12-grade bookkeeping repair. AMENDMENT.

### DOC-2 (`phaseD/phaseD_meanswirl_formalization.md` r7, leg 6 + leg-7 carrier)

**CR-1 (l0) ≡ R4L1-3 (l1) ((⟸) re-read third clause cites (1b),
l.2131-2142): SUSTAINED-AMENDMENT, merged at the clause.** Judge
re-derivation: clause (1b)'s printed derivation is "the same case chains
run at essential type" (l.2032), and the case chains START from "K = 0 as
a distribution then forces the meridional RH TOO" (l.1929-1930, verified)
and "What K = 0 ADDS on this stratum is the s-row atom ... K = 0 forces
m[s] = 0" (l.1967-1970, verified) — (1b) is K = 0-FED; "unconditionally"
means without-the-pin, not without-K = 0. Citing it inside the direction
whose GOAL is K = 0 is circular AS A CITATION. The direction is TRUE with
two valid routes ON THE PAGE (the conclusion's own without-pin gloss at
1858-1860, a ⟸ given; or the step-(3) decomposition applied to the given
∂_φV = 0), and the PINNED form closes outright via the sentence's own tail
("under the r7 pin N_F is in any case front-null"). Both lenses
independently adjudicated the R-2 counter question and this judge concurs:
a true conclusion with a mis-directed support citation is the R3L1-4
precedent class (AMENDMENT, counter NOT incremented) — the r7 certification
sentence claims clause GRADES, which are honest (verified by both lenses'
clause-by-clause checks); the over-certification counter STAYS AT FOUR.
One-phrase repair (either named route). AMENDMENT.

**CR-2 (l0) ≡ R4L1-1 (l1) ("(u1)" referent collision, l.1874-1877 vs
l.2037 + register row 2562 + ROUND-4 rows): SUSTAINED-AMENDMENT, merged.**
Verified verbatim on disk: "the (u1) limit-matching plus gluing ... is NOT
written and NOT claimed" (1874-1876) against "(u1), hereby WRITTEN" (2037).
Reconcilable by a full reader (the annotation's subject is the composite
N_F-point upgrade; step (1) writes the extension LEMMA and applies it off
N_F only — both statements true of their intended referents, verified),
but the single token denotes two contents in one revision — executor-facing
name ambiguity, the F-4/L1-5 prosecuted species. Rename/disambiguation
repair per the l1 spec (which subsumes the l0 phrasing). AMENDMENT.

**R4L1-2 ((1b) justification's underived universal, l.2028-2033):
SUSTAINED-AMENDMENT.** Verified verbatim on disk ("the essential jump is
read through approximate limits, which exist H²-a.e. ..."). Judge check:
the essential (Federer-type) jump set is BY DEFINITION the set where
two-sided approximate limits exist and differ, so (1b)'s stated content
quantifies only where limits exist — the printed existence universal is
UNCONSUMED by (1b)'s content, by step (3) (measure-level, per the
INSENSITIVITY NOTE's own r7 text at 2058-2066), and by the ⟸ re-read; its
only written support is the one-geometry sliver parenthetical. Unconsumed
underived supporting gloss = the L0-5/R3L1-2 precedent class; the clause's
STATED grade is delivered (both lenses verified the case chains at
essential type), so no over-grade and no counter increment. One-edit
restatement per the refuter's spec. AMENDMENT.

### DOC-3 (`phaseD_L4_implies_R1.md` r3.5, leg 14 + leg-17 carrier)

**ESC5-2(l0) ≡ ESC5-1(l1) (slogan escape clause unconditional,
l.921-926 vs bullet l.969): SUSTAINED-AMENDMENT, merged.** Verified
verbatim on disk: the slogan prints "it enters (H-UP-fam)'s delegated
class" unconditionally for BOTH exceptional branches, while the same
window's third bullet conditions kernel-jump entry on "if NG-9's
instantiation of the class admits it" and the retained ESC2-5 annotation
(l.1069-1073, verified) pins the class floor at C^1/H^1 grades. Judge
check: a piecewise-C^1 pair with a genuine kernel jump is NOT H^1 (its
distributional gradient carries a surface measure), so entry is
NG-9-instantiation-conditional exactly as the bullet says; the slogan —
the sentence read first — over-claims what the document's own delegation
withholds. Conclusion (no over-proof) true on both horns; no proof step
consumes the slogan. One-clause repair mirroring the bullet. AMENDMENT.

**ESC5-3(l0) (persistence gloss transplanted, l.972-973):
SUSTAINED-AMENDMENT.** Verified verbatim on disk ("and the jump persists
because those modes advect tangentially to the face" — attached to the
GENERAL characteristic loci). Judge re-derivation: distributional
solvability across the fixed face needs A(n)[U] = 0 pointwise in time;
entropy/shear jumps advect with u-bar; tangency AT the locus is
instantaneous — persistence requires the locus flow-invariant (e.g.
u-bar.n ≡ 0 on a face portion, steady base: a streamsurface portion), and
at an isolated grazing locus of a generic base the transported support
leaves {u-bar.n = 0}, where ker A(n) is trivial and A(n)[U] = 0 forces
[U] = 0 — the general mechanism is unproven and generically unavailable.
The l1 lens's C5L1-3(β) confirmation does NOT rebut this: its own recorded
re-derivation ("stationarity holds where the face is a base-flow
streamsurface portion") IS the flow-invariance qualifier the printed
sentence lacks — l1 read the bullet charitably; the block-family's six
recorded wording-universal defects and the enforced written-line standard
make the literal reading govern. ESC4-1's counterexample role and
disposition SURVIVE (the u-bar.n ≡ 0 steady subfamily is nonempty — both
lenses and this judge concur); R-4 instance, transplant from ESC4-1's
attack text. One-parenthetical restatement per the l0 spec. AMENDMENT.

**ESC5-2(l1) (depth-general enumeration vs Gamma_mid-pinned condition,
l.1048-1053): SUSTAINED-AMENDMENT.** Verified verbatim on disk. Judge
geometry check: the Status-(a) headline quantifies "at every depth with a
given (D-coll)-class split" (l.1036-1037, verified); for s < h/2,
Gamma_mid = Gamma^coll_{h/2} lies at distance h/2 - s INSIDE Omega_int^s
= Omega_up \ closure(C_s) — an interior surface — while the r3.5
parenthetical's own premise enumerates the actual boundary Gamma_in ∪
walls ∪ Gamma^coll_s; the printed condition therefore constrains the wrong
surface at every non-consumed depth. Right at the ONLY consumed depth
(s = h/2, printed of record), no consumed conclusion touched, generic
"n_mid" reading available — one naming clause + the NG-3 residual-(ii)
one-word mirror per the refuter's spec. AMENDMENT.

**ESC5-1(l0) (NG-3 trigger reach / row-1 pointer):
SUSTAINED-AMENDMENT-IN-REDUCED-SCOPE — the unreachable-consumer MECHANISM
is OVERRULED; the row-1 status-text staleness and the trigger's
literal-wording fragility are sustained as one navigational amendment.**
This is the round's one live refuter-vs-refuter conflict (l1's C5L1-7(γ)
attacked exactly this and recorded FAILS-TO-BITE). Judge adjudication at
derivation level, siding with l1 on the mechanism: the document's geometry
class poses Omega_up with the three named boundary faces (Gamma_in, walls,
Gamma_I), whose junction curves are constitutive — Remark 1.5.3(b) and the
NG-3 body name "the wall-interface corner curves" unconditionally (no
dihedral-angle qualifier; they are BC-junction curves, verified at
l.644-649 and the NG-3 row) — so EVERY in-scope H^1 consumption of
Theorem 1 is "on a domain with corners" and fires the trigger's first
clause; the consumer then reads the NG-3 ROW, whose r3.5 BODY names
residual (ii) with Gamma_in's loci explicitly (verified at l.2064):
navigation completes and the postulated no-trigger consumer family is
EMPTY in-class — this is l0's own named self-falsifier, met. What
SURVIVES: register row 1's status text "H^1 extension THEOREM* on smooth
portions, corners = NG-3" (l.2013, verified) is STALE against the r3.5
residual — Gamma_in's grazing loci are SMOOTH portions on which the 1.5.3
route is NOT delivered (the document's own r3.5 finding), so the row-1
label as printed over-covers and its pointer names only corners; the
trigger's "with corners" wording is likewise literal-reading fragile even
though it always fires in-class. Sustained repair = exactly the l0 spec's
fix (trigger first clause extended "or with variable-type (grazing/sonic)
loci on a data face"; row-1 pointer "corners + Gamma_in variable-type =
NG-3"), carried as robustness/navigation hygiene, NOT as a live
consumer-stranding defect. AMENDMENT (reduced scope).

==============================================================================
## §2 PER-DOC DRYNESS (refined criterion of record)

**DOC-1: NOT DRY.** Sustained: 1 REPAIR-NEEDED (ECL0-1) + 5 AMENDMENT
(ECL0-2≡ECR1-1, ECL0-3, ECR1-2, ECR1-3, ECR1-4). 0 BREAKS. The
REPAIR-NEEDED blocks dryness under the criterion of record.

**DOC-2: DRY.** Sustained: 0 BREAKS, 0 REPAIR-NEEDED, 3 AMENDMENT
(CR-1≡R4L1-3, CR-2≡R4L1-1, R4L1-2). First round of the doc2 loop with zero
proof-content repairs AND zero false printed displays; the over-certification
counter stays at FOUR (adjudicated at both lenses and by this judge — no
fifth over-grade); eighteen + fifteen delta passages confirmed with
strongest attacks recorded, including the round's two proof-content repairs
(the (p1)-(p3) pin sufficiency and the (1a)/(1b) grade separation), which
withstood fresh witness-construction attacks (the single-connected-front
self-accumulation variant, killed by (p2)).

**DOC-3: DRY.** Sustained: 0 BREAKS, 0 REPAIR-NEEDED, 4 AMENDMENT
(ESC5-2(l0)≡ESC5-1(l1), ESC5-3(l0), ESC5-2(l1), ESC5-1(l0) reduced-scope).
All five r3.5 dispositions verified ADEQUATE at both lenses (ESC4-2's
REPAIR of the last adjudicated round CONSUMED at derivation level; the
honesty clause — the round's centerpiece — confirmed at its strongest
reading: any single grazing point kills the uniform bound for a continuous
base, so "generically VIOLATED" is exact); the two-face proof core
byte-stable and freshly attacked again at both lenses (kernel-jump feeds at
Gamma_mid excluded by STEP 1 verbatim; proves-too-much re-run clean); A-2
re-verified untouched.

==============================================================================
## §3 LEG CLOSURES (per the R-1..R-3 closure authority)

**LEGS 3 + 5 (DOC-1): OPEN.** Doc1 NOT DRY — a sustained REPAIR-NEEDED
keeps both legs open per the mandate. Leg 3 remains held by the per-doc
rule ONLY (its thread is dry at both lenses of record; ECL0-3 corrected its
LEDGER, not its mathematics — no leg-3 body text carries any finding).
[T-T0P] main statement stays SCHEMA (no label motion — none was in
prospect). The G8/[C-XBVP](a') registry-row + gap-graph landing stays
BLOCKED. Escalation residue named in §6; NO further rounds this window per
mandate.

**LEG 6 (DOC-2): CLOSED — escalation E-3 CLOSES.** Doc2 DRY. Per
J-r2p-2/J-r2p-3 (KEPT, per mandate): the D.18 first and second iff labels
STAY SCHEMA — restoration ONLY through the G-f battery per the proofs-1
upgrade path — but the D.18 restated-text landing AT SCHEMA LABELS is
UNBLOCKED, with the §4 amendments applied at composition. A-1 (leg 7,
already released by VERDICT_escalation §4) re-confirmed untouched at both
lenses this round (grep-verified, no r7 marker in D.2).

**LEG 14 (DOC-3): CLOSED — escalation E-4 CLOSES; the ceiling is GRANTED.**
Doc3 DRY. Earned label, granted by this judge per the R-3 closure
authority: **Proposition 1'' = THEOREM modulo (H-UP-fam)** — the ceiling
"THEOREM modulo (H-UP)" in its honest family form, exactly the two
refuters' standing assessment, superseding the J-r2p-1 SCHEMA of record.
Basis: the two-face proof core (Claim with (cl-C)/(cl-F), (D-coll),
(H-UP-fam), eps_1', STEPs 1-3, UNION) is byte-stable since r3.2, confirmed
at both lenses at every round including this one, with the proves-too-much
test passing on every instance class raised across five rounds; every
honesty clause and residual is priced in-document and mirrored in NG-3
(owner F2), and the confirming round sustained nothing above wording
grade. The label travels WITH its printed moduli of record (the (H-UP-fam)
delegation incl. NG-9's class instantiation; the Status-(a) residuals as
priced). The Proposition-1'' landing item UNBLOCKS at this label, with the
§4 amendments applied at composition. A-2 (leg 17, already released)
re-confirmed untouched.

==============================================================================
## §4 AMENDMENTS TO CARRY (applied at the M0-landing composition citing
## this verdict — no further round; doc2 + doc3 only, per §2/§3)

- **AM-1 (doc2, CR-1≡R4L1-3):** in the (⟸) re-read third clause, replace
  "by step (1)'s unconditional clause (1b)" with a citation of the
  conclusion's own without-pin gloss (no essential-jump mass on the N_F
  residual — a ⟸ given), or of the step-(3) decomposition applied to the
  GIVEN ∂_φV = 0; both routes verified on-page.
- **AM-2 (doc2, CR-2≡R4L1-1):** disambiguate the "(u1)" token — the
  unclaimed composite upgrade at 1874-1876 renamed (e.g. "(u1')
  limit-matching AT N_F points plus the (u2) gluing"), with "(u1) itself,
  the extension lemma, IS written and consumed only off N_F"; mirror in
  register row 2562 and the ROUND-4 R3L1-1 row.
- **AM-3 (doc2, R4L1-2):** restate (1b)'s justification: approximate limits
  "exist BY DEFINITION at every essential-jump point, and at H²-a.e. point
  of each witness geometry of record (a pinching sliver has density 0 at
  density points of its accumulation set)" — dropping the underived
  unconsumed universal.
- **AM-4 (doc3, ESC5-2(l0)≡ESC5-1(l1)):** slogan escape clause gains the
  NG-9 conditional for the kernel branch: "...by accidental C^1 glue or —
  where NG-9's instantiation of the class admits it — by a kernel jump
  A(n)[U] = 0 ..."; mirror in the ESC3-5 disposition row.
- **AM-5 (doc3, ESC5-3(l0)):** persistence gloss restated to flow-invariant
  loci: "on a flow-invariant locus (e.g. a face portion with u-bar.n ≡ 0,
  steady base) the jump persists — the slip-line configuration; persistence
  in general is NG-9's territory with the rest of the transmission theory."
- **AM-6 (doc3, ESC5-2(l1)):** the Status-(a) discharge condition names the
  mid face family-wise: "the split's mid face Gamma^coll_s (= Gamma_mid at
  the consumed depth h/2) uniformly noncharacteristic ..."; NG-3 residual
  (ii)'s "Gamma_mid" generalized the same one word.
- **AM-7 (doc3, ESC5-1(l0) reduced scope):** NG-3 trigger first clause
  extended: "first consumption of Theorem 1 at H^1 regularity on a domain
  with corners OR with variable-type (grazing/sonic) loci on a data face";
  register row 1 pointer: "corners + Gamma_in variable-type = NG-3".

DOC-1's sustained findings are NOT in this list: they are the OPEN residue
of legs 3/5 (§6) and are consumed at the next doc1 revision, not at an M0
landing (doc1's landing items remain held out).

==============================================================================
## §5 JUDGE VERIFICATION ACTS BACKING THIS VERDICT

Quote fidelity: every adjudicated quote re-read against the on-disk
documents this window — doc1 lines 2129-2380 (condition of record with
chart clauses; witness restatement; falsifier consequent; grant head),
2259-2278 ((m2) printed regime), 3825-3840 (§13 E4L0-2 falsifier),
3966-4041 (leg-3 recital, label summary, honest residues); doc2 lines
1848-1899 (conclusion display + (u1) annotation), 1920-1974 (case chains),
2018-2142 ((1a)/(1b), (u1) written, insensitivity note, step (3), (⟸));
doc3 lines 915-990 (slogan + bullets + superseded annotations), 1015-1076
(Status (a) with r3.5 parenthetical, honesty clause, W^{1,1} route, ESC2-5
annotation), 2013 (register row 1), 2058-2081 (NG-3 row + register
discipline note). NO misquote found in any of the six confirming files.

Pen-grade re-derivations by this judge:
(i) ECL0-1's witness (full check recorded in §1 — branch ranges, root pair,
member-by-member satisfaction, falsifier firing, off-data-root landing);
and the parity argument's exactness ON interval slices (IVT at the first
downward crossing), locating the defect precisely at the domain-topology
rung. (ii) ECR1-2's arithmetic (e0''b = 2 < 9 = a1^2 at (m2)'s printed
parameters). (iii) CR-1/R4L1-3's circularity (the case chains' K = 0
consumption verified at source, lines 1929-1930 and 1967-1970; both rescue
routes verified on-page). (iv) R4L1-2's definitional argument (Federer-type
essential jump set presupposes existing approximate limits; consumption
map: step (3) measure-level per 2058-2066). (v) ESC5-2(l1)'s geometry
(Gamma_mid interior to Omega_int^s at distance h/2 - s for s < h/2; the
headline's every-depth scope verified at 1036-1037). (vi) The kernel-jump
pair's non-H^1 status (surface measure in the distributional gradient) and
the ESC2-5 grade floor (1069-1073). (vii) ESC5-3's transport mechanism
(A(n)[U] = 0 pointwise-in-time + trivial kernel off the locus forces
[U] = 0 where the advected support exits — persistence iff flow-invariant
locus). (viii) The ESC5-1(l0)-vs-C5L1-7(γ) conflict resolution: the
three-face boundary partition forces junction curves; 1.5.3(b)/NG-3 name
them of record without an angle qualifier; the trigger fires in-class,
the row body is reached — mechanism overruled; row-1 staleness verified
directly at line 2013 vs the r3.5 body at 2064. (ix) Doc2's
over-certification counter: re-checked that no r7 sentence prints a
strength above its written derivation given the two lenses' clause tables;
counter stays at FOUR. (x) Cross-lens merge validity (ECL0-2≡ECR1-1,
CR-1≡R4L1-3, CR-2≡R4L1-1, ESC5-2(l0)≡ESC5-1(l1)) — same clause, compatible
mechanisms, repairs mutually consistent (the more specific spec adopted in
§4 in each case).

==============================================================================
## §6 RESIDUES AND NEXT-STEP MAP (owner = the S-FOUNDATIONS-C orchestrator)

- **R-1' (doc1 / legs 3 + 5, the escalation residue of this window):**
  revision 9 owed on `phaseD/phaseD_stop_proof.md`, consuming ECL0-1
  (REPAIR: the slice-connectedness member written into the chart clauses —
  "each S-slice of the EOS domain over hull v-values an INTERVAL, under
  which the parity bracketing runs and the root map is continuous on the
  compact hull; else root uniqueness imposed directly as a member" — plus
  the §13 E4L0-2 falsifier-line correction) and the five sustained
  amendments (ECL0-2≡ECR1-1 consequent member arithmetic; ECL0-3 recital
  count; ECR1-2 witness regime; ECR1-3 grant-head propagation; ECR1-4
  instance count), followed by ONE two-lens confirming round on the rev-9
  delta — NEXT WINDOW (no further rounds this window, per mandate). The
  R-4 binding rule REMAINS IN FORCE and is now at eight-plus declared
  instances: three of this round's sustained findings (ECL0-1's parity
  mechanism, ECL0-2's inverted caveat, ESC5-3's persistence gloss) are
  transplant misfits — every rev-9 clause is restated against the row's
  own hypotheses.
- **R-2' (doc2 / leg 6):** CLOSED at this verdict; the D.18 restated-text
  landing (SCHEMA labels) composes with AM-1..AM-3 applied, citing this
  verdict; label restoration remains gated on the G-f battery ONLY.
  Standing guard for the landing scribe: the over-certification counter is
  at FOUR of record — the composed M0 text must not mint a fifth (no
  strength formula above the clauses' in-line grades).
- **R-3' (doc3 / leg 14):** CLOSED at this verdict with the label GRANT of
  §3; the Proposition-1'' landing composes at THEOREM modulo (H-UP-fam)
  with AM-4..AM-7 applied, citing this verdict. Standing owned residuals
  UNCHANGED: NG-3 (F2) carries the variable-type trace theory on Gamma_mid
  AND Gamma_in's grazing loci (generic in the motivating class — the
  honesty clause travels with every consumption); the W^{1,1} Gauss-Green
  route stays named-not-consumed; NG-9 keeps the class instantiation.
- **R-4' (ID hygiene, standing lesson):** the two doc3 lenses minted
  colliding "ESC5-*" namespaces this round (declared and disambiguated
  here); future parallel-lens launches assign per-lens ID prefixes in the
  brief.
- **R-5' (landing execution):** the Blocco-2 landing input is now
  VERDICT_escalation §4's released package PLUS this verdict's leg-6 and
  leg-14 items with AM-1..AM-7; held out: legs 3 and 5 items only.

==============================================================================
## §7 FALSIFIERS FOR THIS VERDICT

- ECL0-1 sustain: refuted by exhibiting a printed line of record making
  disconnected-S-slice EOS out-of-class (none found; §1 pins no domain,
  per the consumed ER3L1-2 record), or by breaking the witness
  construction at any checked member (each verified in §1/§5).
- The two overrules folded into ESC5-1(l0)'s reduced scope: refuted by
  exhibiting an admissible in-class Omega_up whose three named faces have
  empty junction curves (the partition argument forbids it for nonempty
  faces), or a document line de-naming smooth-junction curves from
  1.5.3(b)'s "corner curves".
- Every SUSTAINED-AMENDMENT: refuted by the specific self-falsifier
  recorded in its source refutation (each was checked against the document
  and found live).
- The doc2/doc3 DRY verdicts: refuted by showing a sustained finding of
  this round to be REPAIR-grade at derivation level (each class call is
  re-argued above with its precedent), or by exhibiting a confirming-round
  finding this verdict failed to adjudicate (the inventory is 13 distinct
  of 17 raised; the merge map is in §1/§5(x)).
- The leg-14 label grant: refuted by a derivation-level break of the
  two-face proof core (byte-stable, five rounds of failed fresh attacks on
  file) or by showing a consumed conclusion of Prop 1'' to depend on any
  passage carrying a sustained finding (all four doc3 amendments live in
  honesty commentary / naming / register text — verified).

END OF VERDICT — machine summary returned via structured output:
{doc1_dry: false, doc2_dry: true, doc3_dry: true,
legs_closed: [6, 14], legs_open: [3, 5],
leg14_label: "THEOREM modulo (H-UP-fam)",
amendments_to_carry: [AM-1..AM-7 as listed in §4],
verdict_file: validation/sfoundations_raws_2026-08-13/r2pass/VERDICT_confirm.md}
