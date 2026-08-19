# ESCALATION REFUTATION — DOC-3 r3.3 repair text, until-dry ROUND 2, lens l1

Lens: gas-dynamics / physics, RH algebra, counterexamples. Date: 2026-08-19.
Target: `validation/sfoundations_raws_2026-08-13/phaseD_L4_implies_R1.md`,
ATTACK SCOPE = the escalation-repair text for leg 14 (Proposition 1'',
Section 1.6) and the leg-17 amendment A-2 chain (Remark 1.5.5), at the
NEWEST revision state of record — the r3.3 block (2026-08-19), which
consumed `esc_doc3_r2_l0.md` (ESC2-1..5) on top of the r3.2 state this
lens's round-1 predecessor attacked. The r3.3-NEW passages are: the
face-dependent "Why this does not prove too much" paragraph (repairs
ESC2-1 + ESC2-2, with the r3.2 wording retained in annotation), the
"Which (H-UP) form" straddling correction (ESC2-3), the rederived
falsifier window arithmetic through the terminal collar segment (ESC2-4,
mirrored in register row 1'), the Status-(a) scoping to (H1.4)-grade
pairs with the H^1-via-1.5.3 clause (ESC2-5), and the r3.3 revision-log
block itself (state-integrity reconciliation + ESC2 disposition table).

Specs consumed: `r2pass/VERDICT_r2pass.md` §2.1 (L0-7/L1-7
SUSTAINED-BREAKS; L1-8 SUSTAINED-AMENDMENT), §3 (A-2), §4(c) (E-4), §5
(falsifiers incl. the proves-too-much test). Full objection texts
consumed: `refute_r2batch_l0.md` L0-7 (lines 485-534),
`refute_r2batch_l1.md` L1-7 (475-522) and L1-8 (567-605). Prior
escalation rounds consumed IN FULL for dedup: `esc_doc3_r1_l0.md`
(ESC-L0-1..7), `esc_doc3_r1_l1.md` (F-1..F-6), `esc_doc3_r2_l0.md`
(ESC2-1..5). Statements of Theorem 1', Lemma 1.4, Theorem 1/(EI), 1.5.3,
1.5.5, the Section-6 register rows 1/1', Section 5 composite clause (i),
3.4(3)(a), and the NG-3/NG-9 rows read against every application the
repair text makes of them.

DEDUP DECLARATION: no dispositioned objection is re-raised at its own
content. L0-7/L1-7/L1-8, ESC-L0-1..7, F-1..F-6, and ESC2-1..5 are engaged
ONLY through discharge verification (§1). Where a finding below touches a
dispositioned ID, it attacks r3.3-NEW text that the disposition itself
introduced (ESC2-6 and ESC2-7 attack wording ADOPTED from the l0
refuter's proposed repair phrases — adoption does not immunize: the
proposer wrote repair guidance, not of-record text; ESC2-8 and ESC2-9
attack the ADEQUACY of the ESC2-5 disposition on its own new clause and
its missing register mirror, under the brief's rule "unless the
disposition itself fails — cite the ID and say why"). ID namespace
continues the round-2 sequence: ESC2-6..ESC2-9.

==============================================================================
## §1 DISCHARGE VERIFICATION (sustained objections and prior dispositions
## vs the r3.3 text, re-verified at pen grade by this lens)

**L0-7(a) / L1-7(i) (quantifier order) — remains DISCHARGED at r3.3.**
eps_1 := d_0/(2 lambda_max) is a fixed constant of (D-coll) + the collar
base state; eps_1' := min(eps_1, T_f − t*) > 0 keeps the window
in-domain. Re-derived: for t in (t*, t* + eps_1'],
lambda_max(t − t*) <= d_0/2 < d_0, so R in (lambda_max(t − t*), d_0)
exists with uniform slack at every window time. No subdomain-dependent
epsilon anywhere in the r3.3 argument. CHECK.

**L0-7(b) / L1-7(ii) (trace ON the source face) — remains DISCHARGED.**
The only trace the proof consumes is on Gamma_mid, at the fixed distance
>= d_0 from BOTH data-carrying faces. Re-derived from (D-coll):
dist(x_0, Gamma_in^coll ∪ Gamma_I) >= d_0 > R for every x_0 in Gamma_mid
and every admissible R, so B(x_0, R) misses both faces and the Lemma 1.4
frustum in O = C_h meets del O only in wall portions — Lemma 1.4's
admissible class exactly (wall term zero by Lemma 1.3/(H1.2); the margin
clause not even needed). L1-7's circularity is structurally absent at
r3.3: the dependency order is strictly {t*-slice zero} → (MID-TRACE) →
{STEP 2, STEP 3} → UNION; (MID-TRACE)'s derivation consumes NO face
input. CHECK.

**The proves-too-much test (VERDICT §5), run by this lens against the
r3.3 face-dependent paragraph — PASSES substantively.** Instances tried:
(i) bare coupling across Gamma_in^coll (ESC-L0-3's strengthened
instance): excluded by STEP 3's enlargement — I re-derived the geometry:
Gamma_in^coll ⊂ Omega_int^{h/2} = Omega_up \ closure(C_{h/2}) and
Gamma_in^coll ∩ ∂Omega_int^{h/2} = ∅ (the boundary is
Gamma_in ∪ walls ∪ Gamma_mid), so (H-UP-fam)'s states solve the PDE
across that face, which the bare-coupled pair does not; (ii) bare
coupling across Gamma_mid: STEP 1's frusta straddle it and need one C^1
solution of the homogeneous system on C_h — the glued object supplies
none, (MID-TRACE) never becomes available, and the interior-side member
being (H-UP-fam)-admissible closes the STEP-3 escape route (ESC2-2's
fix, verified); (iii) NEW this round — bare coupling across a face Σ
deep inside Omega_int^h (upstream of the collar): the glued object
restricted to C_h IS a genuine C^1 solution, so STEPs 1-2 run — but Σ is
interior to Omega_int^{h/2}, so the glued pair is not in (H-UP-fam)'s
class and STEP 3 has nothing to consume: excluded by the same bullet-1
mechanism (which the paragraph states for Gamma_in^coll but which holds
for every face interior to the enlarged domain); (iv) a transversal face
partly inside C_h: bullet 2's two-sided-regularity requirement bites on
the C_h portion; (v) a pair whose glue happens to be C^1 across the
coupling face: then it solves the PDE across it and the "uniqueness"
concluded is the honest statement, not an over-proof; (vi) coupling
across Gamma_I: NOT excluded and correctly so — one-way margin
dissipation with arbitrary downstream content is the theorem's own
claim, not a transmission coupling. No instance survives. The mechanism
of record is finally face-correct (third repair of this paragraph);
residual wording defect in its opening slogan = ESC2-6 below.

**ESC2-1 (wrong face) — DISCHARGED.** The r3.3 body now names
Gamma_in^coll as the face the enlargement internalizes, matching the
ESC-L0-3 log row; the r3.2 paragraph is retained verbatim in the
annotation with its three recorded defects, each of which I checked
against ESC2-1's text — faithful in content. ESC-L0-3's disposition is
RE-CLOSED. CHECK (modulo the ESC2-6 slogan).

**ESC2-2 (false universal "never Step 1") — DISCHARGED.** Replaced by
the face-dependent statement; the Gamma_mid-coupling instance is now
handled by bullet 2 with the (H-UP-fam)-admissibility of the
interior-side member stated. CHECK.

**ESC2-3 (straddling) — DISCHARGED as to its content, with a NEW defect
in the adopted wording.** "Nothing straddles a DATA-CARRYING face
(Gamma_in^coll or Gamma_I)" + "the frusta DO straddle Gamma_mid" is now
exactly true and states the mechanism. The appended clause "never an
input" is a fresh false universal = ESC2-7 below.

**ESC2-4 (falsifier arithmetic) — DISCHARGED, re-derived.** The r3.3
derivation routes the bound through the terminal collar segment: any
influence path from Gamma_in^coll ∪ Gamma_I to Gamma_mid has arclength
>= Euclidean distance >= d_0 inside closure(C_h) ((D-coll)); on that
segment lambda_max is theorem-grade (Lemma 1.4 with monitored (M-c)
regularity); entry above bound cannot predate t_p (pinned trigger: field
at the bound on ALL of Omega_up at t_p); hence arrival
>= t_p + d_0/lambda_max = t_p + 2 × the probed window
d_0/(2 lambda_max), regardless of exterior speeds. Attacks tried and
failed: wall-penetrating paths (impossible — walls bound the fluid
domain, so entry is via Gamma_in^coll or Gamma_I and the TERMINAL
segment after the last crossing lies in closure(C_h)); post-t_p
amplification INSIDE the collar (bounded by the certified collar
Gronwall factor, absorbed in "scheme bound" per the F-5 record — and a
mid-face signal from broken collar dynamics is exactly what the leg must
reject); pre-t_p sub-bound exterior content (at t_p it is at the bound
by the trigger; only post-t_p growth can exceed it); numerical
(CFL/implicit) propagation faster than lambda_max (absorbed in the
declared discretization-bound language of the harness, as for the
Theorem-1 falsifier). The superseded r3.2 sentence is retained with
ESC2-4's two defects faithfully recorded; register row 1''s falsifier
cell mirrors the terminal-collar-segment wording verbatim in condensed
form. CHECK.

**ESC2-5 (Status (a) scoping) — PARTIALLY ADEQUATE.** The core fix is
sound: "IS a theorem" now quantified over (H1.4)-grade (C^1) pairs, for
which the (EI) run on the (D'')-Lipschitz Omega_int^s closes with the
Gamma^coll_s term killed pointwise by the zero full trace (re-derived:
no sign information on A(n) needed where U = 0). But the clause the
disposition ADDED — the H^1-members extension "via the 1.5.3
mollification extension, THEOREM* modulo NG-3" — over-claims under the
document's own 1.5.3 framework (ESC2-8 below), and the corner-inventory
extension it declares is mirrored nowhere in the NG-3 register row
(ESC2-9 below).

**A-2 / L1-8 / F-6 chain (leg 17) — DISCHARGED at the current state,
re-verified by this lens's own spectrum computation.** At u·n = 0 the
spectrum of A(n) is {−c, 0(×3), +c}; at u·n = −c it is {−2c, −c(×3), 0}:
adjacent distinct gaps = c-bar, all pairwise separations >= c-bar,
extreme acoustic pair 2c-bar — the r3.2 wording is exact and the retired
"mutual = c-bar" phrase is annotated of record in both the Remark and
the log's L1-8 row. Multiplicity pattern (1,3,1) constant through both
loci; Lemma 0.2's eigenvectors u·n-independent (A(n) depends on u·n only
through the (u·n)I shift), so projector regularity holds with margin;
the sign-classification-jump mechanism matches L1-8's demanded repair,
and conclusion/scoping are unchanged per the A-2 spec. Strongest fresh
attack tried: the singular "a fixed, regular mode flips class" against
the 3-dimensional λ_0 crossing at grazing — already examined and
confirmed by this lens in round 1 (the triple-eigenspace reading is
recorded there); no new defect. r3.3 touched nothing in 1.5.5. CHECK —
A-2 remains fully landed.

**r3.3 log block (state-integrity reconciliation) — VERIFIED.** Each
"VERIFIED" outcome checked against the live body: (cl-C), (cl-F) at
three sites + register mirror, eps_1' threading + two-case UNION,
STEP-2 (H1.4) restriction, (D-coll) Lipschitz clause, F-2 restricted
quantifier with the s = h endpoint dropped, F-4 corrected attribution,
F-6 adjacent-gaps wording — all present and coherent; the ESC2
disposition table matches `esc_doc3_r2_l0.md` (0 B + 1 R + 4 A, incl.
the ESC-L0-3 inadequacy concurrence); "NO step of the two-face proof
moved this round" is true of the diffs (all five r3.3 edits live in
commentary/attribution/falsifier/status). CHECK.

==============================================================================
## §2 OBJECTIONS (r3.3 text; verbatim quote + attack + class)

------------------------------------------------------------------------------
**ESC2-6 — class AMENDMENT. The face-dependent paragraph's opening
slogan calls BOTH crossing structures "certified"; the structure
crossing Gamma_in^coll is (H-UP-fam)'s hypothesized class — the NG-9
modulo, precisely what no monitor certifies.**

Quote (Section 1.6, "Why this does not prove too much", r3.3 rewrite):
> "The exclusion is FACE-DEPENDENT: every face of the two-face
> decomposition is crossed by a certified structure, and a bare
> coupling's face is crossed by nothing."

Attack. In this document "certified" is a reserved word: the
monitored-hypothesis accounting block two paragraphs below distinguishes
what the monitors certify ((M-c) on the collar; (M-a)+(H-RW) on the
margin) from what is hypothesized ((H-UP-fam), delegated to NG-9,
label-gating SCHEMA). Under that standard the slogan is half false: at
Gamma_mid the crossing structure is indeed certified (Lemma 1.4 frusta
on the (M-c)-monitored collar, theorem-grade); at Gamma_in^coll the
crossing structure is (H-UP-fam)'s solution class solving the PDE across
the face — the UNPROVEN modulo of the whole proposition, certified by
nothing (NG-9 row: "SCHEMA (standard-physical, unwritten)"). A reader
landing this paragraph in M0 would read "certified" as pipeline-certified
and thereby overclaim exactly the NG-9 gap. The sentence is the l0
refuter's own proposed summary phrase (ESC2-1 repair tail), adopted
verbatim — adoption does not immunize it. The bullets beneath state the
mechanism correctly ("the states (H-UP-fam) quantifies over solve the
PDE ACROSS Gamma_in^coll"), so no derivational content moves. Fix (one
phrase): "every face of the decomposition is crossed by a NAMED
structure of the proof — a certified one at Gamma_mid (Lemma 1.4 on the
monitored collar), a hypothesized one at Gamma_in^coll ((H-UP-fam)'s
cross-face solution class, NG-9) — and a bare coupling's face is crossed
by nothing." **Class: AMENDMENT.**

------------------------------------------------------------------------------
**ESC2-7 — class AMENDMENT. "never an input" in the corrected "Which
(H-UP) form" block is a fresh false universal: (MID-TRACE) is exactly
the trace INPUT of STEP 2 (Theorem 1' hypothesis (ii)) and STEP 3
((H-UP-fam)'s same-trace clause) — the fourth wording defect minted at
this block-family, introduced by the ESC2-3 repair itself.**

Quote (Section 1.6, "Which (H-UP) form", r3.3 wording):
> "the frusta DO straddle Gamma_mid (balls centered on it), precisely
> because Gamma_mid carries no data: its trace is STEP 1's OUTPUT,
> produced from two-sided collar regularity, never an input"

Attack. Read against the proof's own data flow, "never an input" is
false: STEP 2 consumes the Gamma_mid trace as "hypothesis (ii) of
Theorem 1', supplied by (MID-TRACE)" — hypothesis (ii) is Theorem 1''s
DATA hypothesis on its upstream face, here Gamma_mid; STEP 3 consumes
"the same full trace on Gamma_mid x [t*, t* + eps_1']" as (H-UP-fam)'s
face-trace datum; and the document's own bullet 2 calls the same object
"(MID-TRACE) — [which] never becomes available" as the input STEP 3
lacks for a bare coupling ("its trace is STEP 1's OUTPUT, never an
input" thus contradicts "take the Gamma_mid trace as DATA" in the r3.3
annotation eight lines below). The true statement — and the one that
does the distinguishing work against (r-b)'s lens geometry — is: the
Gamma_mid trace is never an EXOGENOUS input (it is not part of the
Claim's data set, and no uncontrolled data crosses a straddled face); it
is STEP 1's derived output, consumed downstream by STEPs 2-3 as
established data. This is the identical defect class as the three prior
printings of the proves-too-much mechanism (a true mechanism stated as
a false universal), in the very block whose F-4 purpose is attribution
precision; the E-4 adjudicator reads this block. The wording is adopted
from ESC2-3's proposed fix ("whose trace is Step 1's output, not an
input") — the proposer's shorthand was scoped to the straddling
discussion; of-record it must be scoped explicitly. Fix: "...its trace
is STEP 1's OUTPUT, produced from two-sided collar regularity — never an
exogenous input (STEPs 2-3 consume it only as STEP 1's established
result)". **Class: AMENDMENT.**

------------------------------------------------------------------------------
**ESC2-8 — class REPAIR-NEEDED. Status (a)'s r3.3 H^1 clause claims the
1.5.3 mollification extension transfers to Omega_int^s at rigor
"THEOREM* modulo NG-3", but 1.5.3's smooth-portion machinery (Friedrichs
noncharacteristic + Rauch 1985 uniformly-characteristic
constant-multiplicity) covers NO regime containing Gamma_mid's
characteristic-type transition loci — a face on which nothing in
(D-coll) or Status (a) constrains u-bar·n. The ESC2-5 disposition's own
new clause carries the gap (dedup rule invoked: the disposition is
attacked on the text it added).**

Quote (Section 1.6, Status of (H-UP-fam), case (a), r3.3):
> "(H-UP-fam) IS a theorem of this document at every depth with a given
> (D-coll)-class split, FOR PAIRS OF (H1.4)-GRADE (C^1) MEMBERS of its
> delegated solution class — H^1 members via the 1.5.3 mollification
> extension, THEOREM* modulo NG-3, whose corner inventory then also
> includes the curves where Gamma_mid meets Gamma_w, never inventoried
> by 1.5.3"

Attack (hypothesis accounting under the document's own 1.5.3 framework;
gas-dynamics content of the gap). The (EI) run backing case (a) for H^1
members must run on Omega_int^s, whose boundary contains the NEW smooth
portion Gamma^coll_s = Gamma_mid. 1.5.3 of record handles exactly two
smooth-portion regimes: (i) noncharacteristic portions (plain Friedrichs
mollifiers) and (ii) uniformly characteristic portions of CONSTANT
multiplicity (Rauch 1985, cited load-bearing for the slip wall, where
u-bar·n ≡ 0 identically). Gamma_mid fits neither uniformly: it is an
interior transversal surface of the collar with NO normal-Mach
constraint anywhere in (D-coll), Theorem 1', or Status (a) — (H1.3)'s
margin lives on Gamma_I only — so u-bar·n_mid may cross {0, ±c-bar} on
it. On the loci where A(n_mid) becomes singular the boundary is
characteristic but NOT uniformly and NOT of locally constant
multiplicity (the type varies along the face): outside both named
theories. These are physically generic in the motivating class — the
same grazing/sonic loci that Remark 1.5.5 handles on Gamma_in and
explicitly scopes OUT of the constant-multiplicity theory ("valid ...
only on the NON-CHARACTERISTIC, constant-multiplicity part"); the
document itself, one section earlier, refuses to run trace machinery
through such loci without an explicit construction. The r3.3 clause
extends only the CORNER inventory (Gamma_mid ∩ Gamma_w) and is silent on
the face's variable type, so "H^1 members via the 1.5.3 mollification
extension, THEOREM* modulo NG-3" asserts a rigor label the cited
machinery does not deliver as cited: the accounting is incomplete by one
named condition (the judge's L1-2 precedent — "the accounting text must
change: repair, not wording"). Repair (either branch, one clause):
(r-i) pin the H^1 (EI) run on Omega_int^s to the plain H^1
divergence-theorem route and SAY so (for U in C([0,T_f]; H^1) ∩
C^1([0,T_f]; L^2) on a (D'')-Lipschitz domain, integration by parts
holds for H^1 members directly, with L^2 boundary traces — if the
document takes this route, the characteristic-type question on Gamma_mid
never arises and 1.5.3's Rauch debt is declared wall-specific); or
(r-ii) keep the 1.5.3-citation route and add the named residual: "modulo
NG-3 AND the variable-type trace theory on Gamma_mid (u-bar·n_mid
crossing {0, ±c-bar}); discharged for splits with Gamma_mid uniformly
noncharacteristic (|u-bar·n_mid| and |u-bar·n_mid ∓ c-bar| bounded
below)". Load-bearing only for the smooth-base sanity reduction (case
(b)/NG-9 untouched; the C^1-grade main scoping is sound), and the
two-face proof itself consumes NOTHING of this — but a rigor label of
record over-claims until one branch lands. **Class: REPAIR-NEEDED.**

------------------------------------------------------------------------------
**ESC2-9 — class AMENDMENT. The corner-inventory extension the ESC2-5
disposition declares is mirrored nowhere in the NG-3 register row: the
of-record gap accounting still inventories only wall-INTERFACE corners.**

Quotes. Disposition row (revision log, r3.3):
> "ESC2-5 | AMENDMENT | FIXED — ... (THEOREM* modulo NG-3, corner
> inventory extended to the curves Gamma_mid intersect Gamma_w); ...
> Section 1.6."

NG-3 register row (Section 7, unchanged since r2):
> "NG-3 | Wall-interface corner compatibility for the H^1 extension of
> Theorem 1 (Remark 1.5.3(b)); the C^1 core is complete and
> unconditional. **r2 additions**: ..."

Attack (register discipline, SR-class: counts/inventories live in their
registers, not in prose asides). The r3.3 Status-(a) sentence enlarges
NG-3's corner inventory by a new curve family (Gamma_mid ∩ Gamma_w,
"never inventoried by 1.5.3") — but the NG-3 row, the register of record
a consumer navigates to (navigation-first standard), still describes the
gap as wall-INTERFACE corner compatibility with r2 additions only, and
its trigger clause does not know that a Prop-1''-side consumption now
rides it. A consumer discharging NG-3 against its own row would close
the gap while the Gamma_mid ∩ Gamma_w curves remain live. The
disposition declared its edit site as "Section 1.6" only — the mirror is
missing BY the disposition's own design, which is why this is raised as
disposition-inadequacy rather than a new-content defect. Fix (one row
edit): add to NG-3 "r3.3 addition: corner inventory extended by the
curves Gamma_mid ∩ Gamma_w for the Status-(a) H^1 run of (H-UP-fam)
(Prop 1'', Section 1.6)" — or scope the Status-(a) clause to state that
its extension is local to Prop 1'' and flag it in NG-3's trigger.
**Class: AMENDMENT.**

==============================================================================
## §3 CONFIRMED passages (strongest attack tried, each)

**C2L1-1 — the two-face proof core at r3.3 (STEPs 1-3 + UNION with
(cl-C)/(cl-F)/eps_1'): CONFIRMED.** Attacks tried this round: (α)
swirl-dominated collar base (rotating-wave physics): Lemma 1.4's
lambda_max uses |u-bar| + c-bar, and spec A(nu) ⊂
[u·nu − c, u·nu + c] ⊂ [−lambda_max, lambda_max] for EVERY unit nu, so
azimuthal velocity cannot outrun the frustum shrink in any direction —
fails; (β) frustum-wall contact for x_0 near Gamma_w: allowed by Lemma
1.4's admissible class, wall term zero by Lemma 1.3 with (H1.2) held by
both solutions — fails; (γ) MID-TRACE left endpoint and a.e.-vs-
pointwise mismatch: U(·, t*) = 0 slice-wise by (cl-C) left-closedness,
and on C_h (H1.4) gives C^1, so pointwise zero — fails; (δ) UNION cover
exactness: Omega_up = Omega_int^{h/2} ⊔ (Gamma_mid ∩ Omega_up) ⊔
C_{h/2}, the remaining closure pieces (walls, Gamma_I) lie in ∂Omega_up
— fails; (ε) full-trace over-determination physics (prescribing all five
components on Gamma_mid): harmless for UNIQUENESS-given-agreement, no
existence claim is consumed — fails; (ζ) re-run of the retracted r2
defects (a)/(b) against the r3.3 text: no analogue (uniform eps_1;
conclusions never evaluated on a data-carrying face). The delivered
strength remains THEOREM modulo (H-UP-fam); LABEL OF RECORD SCHEMA per
J-r2p-1, correctly held at every consumer site checked (Section 1.6
rigor block, 3.4(3)(a), Section 5 clause (i), register row 1', NG-9).

**C2L1-2 — the r3.3 face-dependent proves-too-much bullets: CONFIRMED**
(modulo ESC2-6's slogan). Strongest attacks: the six coupling instances
of §1 (incl. the NEW third-face and transversal-face instances this
round); the geometry claim "Gamma_in^coll is INTERIOR to Omega_int^{h/2}"
re-derived from the (D-coll) definitions; bullet 2's note that the
interior-side member is (H-UP-fam)-admissible (it solves across
Gamma_in^coll) — consistent with (H-UP-fam)'s printed quantifier.

**C2L1-3 — the r3.3 annotation of record (superseded r3.2 paragraph +
three recorded defects): CONFIRMED.** Attack tried: misquote or
mis-recording of ESC2-1/ESC2-2 (a disposition-integrity failure) — the
retained paragraph and the three defects match the l0 round-2 text
faithfully in content, and the double-annotation chain (r3 sentence →
r3.2 retirement → r3.3 face-dependent correction) preserves every prior
wording per house discipline.

**C2L1-4 — r3.3 falsifier window arithmetic + register mirror:
CONFIRMED.** Strongest attacks: wall-path evasion, intra-collar
amplification, pre-t_p entry, numerical-speed evasion (§1, ESC2-4
block); the arithmetic d_0/lambda_max = 2 × d_0/(2 lambda_max) checked;
row 1''s condensed cell carries the terminal-collar-segment routing and
the exterior-speeds-unconstrained clause.

**C2L1-5 — Status (a) core (C^1-grade scoping + (EI) run + zero-trace
kill): CONFIRMED** (the H^1 clause is ESC2-8). Attack tried: whether the
Gamma^coll_s boundary term needs sign information where the difference's
trace vanishes — it does not (integrand <S A(n)U, U> = 0 pointwise at
U = 0); whether the run needs (H1.3)-type margin on Gamma_mid — it does
not (no Gamma_I portion on ∂Omega_int^s).

**C2L1-6 — "The two structural assets consumed" tail sentence:
CONFIRMED.** Strongest attack tried: "the W^{1,infinity} collar overlap
C_h \ closure(C_{h/2}) ..., on which Lemma 1.4 is a theorem" read as
locating STEP 1's Lemma-1.4 run on the overlap — which would be the
defect-(b) geometry reborn (frusta based ON the overlap's boundary face
Gamma_mid). Fails to break: each clause is literally true (Lemma 1.4 IS
a theorem on every W^{1,infinity} subregion, the overlap included; the
overlap IS the structural asset making the decomposition overlapping,
hence non-circular; (M-c)'s domain C_h covers it), and STEP 1's actual
application domain O = C_h is stated unambiguously in the proof. Noted
for the E-4 adjudicator as residual looseness riding ESC2-6's fix;
not counted as a finding.

**C2L1-7 — leg-17 Remark 1.5.5 at the current state (A-2 + F-6):
CONFIRMED — A-2 remains fully landed** (§1; spectra and eigenvector
independence re-derived by this lens; conclusion/scoping unchanged; no
consumer cites the retired mechanism unannotated).

**C2L1-8 — r3.3 revision-log block (reconciliation + disposition
table): CONFIRMED.** Attack tried: any VERIFIED claim without the
matching body edit, any count mismatch vs `esc_doc3_r2_l0.md`, any
silent re-mint — none found (§1).

==============================================================================
## §4 SUMMARY TABLE

| ID | Passage (r3.3 text) | Class |
|---|---|---|
| ESC2-6 | proves-too-much opening slogan: "crossed by a certified structure" — false for Gamma_in^coll (the crossing structure is the hypothesized (H-UP-fam) class = NG-9, certified by nothing) | AMENDMENT |
| ESC2-7 | "Which (H-UP) form" block: "its trace is STEP 1's OUTPUT ... never an input" — false universal; (MID-TRACE) is STEP 2's hypothesis-(ii) datum and STEP 3's same-trace datum | AMENDMENT |
| ESC2-8 | Status (a) H^1 clause: "via the 1.5.3 mollification extension, THEOREM* modulo NG-3" over-claims — 1.5.3's two smooth-portion regimes exclude Gamma_mid's variable characteristic type (u·n_mid crossing {0, ±c}); one named condition missing (ESC2-5 disposition partially inadequate) | REPAIR-NEEDED |
| ESC2-9 | NG-3 register row not mirrored: the r3.3 corner-inventory extension (Gamma_mid ∩ Gamma_w) lives only in a Section-1.6 prose aside | AMENDMENT |

Totals: 4 objections = 0 BREAKS-THE-LEG + 1 REPAIR-NEEDED + 3 AMENDMENT.
Discharge verdicts (§1): L0-7(a)/(b) = L1-7(i)/(ii) remain DISCHARGED at
r3.3; the proves-too-much test PASSES substantively (six instances);
A-2/L1-8/F-6 remain fully landed; ESC2-1, ESC2-2, ESC2-4 dispositions
ADEQUATE; ESC2-3 adequate as to content with a new defect in the adopted
wording (ESC2-7); ESC2-5 PARTIALLY ADEQUATE (ESC2-8 + ESC2-9). No
finding touches a step of the two-face proof; no label motion is
proposed — SCHEMA per J-r2p-1 stands, restoration = the E-4 adjudication
only.

==============================================================================
## §5 SELF-FALSIFIERS (what kills each finding)

- ESC2-6 dies if "certified" is shown to be defined of record to include
  hypothesized-with-declared-owner structures (it is not: the
  monitored-hypothesis accounting and the NG-9 row separate the two), or
  if (H-UP-fam)'s cross-face class is shown certified by a monitor.
- ESC2-7 dies if STEP 2 and STEP 3 are shown NOT to consume the
  Gamma_mid trace as a datum — refuted by the proof's own text
  ("hypothesis (ii) of Theorem 1', supplied by (MID-TRACE)"; "the same
  full trace on Gamma_mid").
- ESC2-8 dies if (r-i) the H^1 (EI) run on Omega_int^s is pinned of
  record to the plain H^1 divergence-theorem route with no
  characteristic-type debt (then the finding reduces to demanding that
  pin be written), or (r-ii) a uniform-noncharacteristic property of
  Gamma_mid is exhibited in (D-coll)/Status (a) (none exists — no
  normal-Mach constraint on the mid-face appears anywhere), or Rauch
  1985 is shown to cover variable-multiplicity characteristic-type
  transitions (its hypothesis is uniform characteristicity of constant
  multiplicity).
- ESC2-9 dies if an NG-3 row edit carrying the Gamma_mid ∩ Gamma_w
  curves is located in the register (grep of the Section-7 NG-3 row at
  the attacked state finds only the r2 additions), or if the register
  discipline is shown of record to allow inventory deltas to live in
  body prose without a row mirror.

END — machine summary: {objections: 4, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc3_r2_l1.md}
