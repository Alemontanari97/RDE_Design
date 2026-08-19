# ESCALATION REFUTATION — DOC-3 r3.4 repair text, until-dry ROUND 3, lens l1

Lens: gas-dynamics / physics, RH algebra, counterexamples. Date: 2026-08-19.
Target: `validation/sfoundations_raws_2026-08-13/phaseD_L4_implies_R1.md`,
ATTACK SCOPE = the escalation-repair text for leg 14 (Proposition 1'',
Section 1.6) and the leg-17 amendment A-2 chain (Remark 1.5.5), at the
NEWEST revision state of record — the r3.4 block (until-dry ROUND 3,
2026-08-19), which consumed `esc_doc3_r3_l0.md` (ESC3-1..3) and this
lens's round-2 file `esc_doc3_r2_l1.md` (ESC2-6..9) on top of the r3.3
state. Machine sweep of scope (grep "r3.4" on the target): the log block
(lines 18, 204-234), the "Which (H-UP) form" ESC2-7 scoping (line 733),
the proves-too-much slogan split (line 875), the third taxonomy bullet
(line 898), the Status-(a) box conjunct (line 942), the Status-(a)
variable-type trace clause (line 952), the falsifier contaminant
relabeling (line 1007), register row 1' (line 1912), and the NG-3
register mirror (line 1962). NO r3.4 marker exists inside the two-face
proof body (Claim, (D-coll), (H-UP-fam), STEPs 1-3, UNION — byte-level
r3.2 text) — the log's "NO step of the two-face proof moved this round"
is TRUE of the diffs. Remark 1.5.5 carries no r3.3/r3.4 marker (standing
r3.2 text; re-verified per the A-2 mandate, §1).

Specs consumed: `r2pass/VERDICT_r2pass.md` §2.1 (L0-7/L1-7
SUSTAINED-BREAKS; L1-8 SUSTAINED-AMENDMENT), §3 (A-2), §4(c) (E-4), §5
(falsifiers incl. the proves-too-much test). Full objection texts
consumed: `refute_r2batch_l0.md` L0-7, `refute_r2batch_l1.md` L1-7/L1-8.
Prior escalation rounds consumed IN FULL for dedup: `esc_doc3_r1_l0.md`
(ESC-L0-1..7), `esc_doc3_r1_l1.md` (F-1..F-6), `esc_doc3_r2_l0.md`
(ESC2-1..5), `esc_doc3_r2_l1.md` (ESC2-6..9, this lens's round 2),
`esc_doc3_r3_l0.md` (ESC3-1..3, the l0 round on the r3.3 state whose
dispositions r3.4 carries).

DEDUP DECLARATION: no dispositioned objection is re-raised at its own
content. L0-7/L1-7/L1-8, ESC-L0-1..7, F-1..F-6, ESC2-1..9, and ESC3-1..3
are engaged ONLY through discharge verification (§1); no disposition is
attacked as failed this round — all seven r3.4 dispositions are ADEQUATE
as dispositions. Every objection below targets r3.4-NEW text with zero
prior adversarial coverage: ESC3-4 attacks the tail clause of the slogan
the ESC2-6 disposition adopted (the tail is THIS LENS'S OWN round-2
proposed phrase — adoption does not immunize, and self-authorship does
not immunize either, symmetric with the ESC2-6/ESC2-7 precedent where
l0's adopted phrases were attacked; the defect became LIVE only through
the same-window interaction with the r3.4 third bullet); ESC3-5 attacks
a universal inside the ESC3-1 disposition's own new bullet; ESC3-6
attacks a third, previously unattacked clause of the Status-(a) premise
sentence (ESC3-2 and ESC2-8 touched the same sentence at other clauses —
the r3.4 log itself records same-sentence-different-clause as
no-collision). ID namespace continues the round-3 sequence after l0's
ESC3-1..3: **ESC3-4..ESC3-6**.

==============================================================================
## §1 DISCHARGE VERIFICATION (the r3.4 repairs vs the objections they
## answer, chained back to the sustained originals; pen grade, this lens)

**ESC3-1 (uncovered third face) — DISCHARGED.** The third bullet is
present and mechanism-correct: for a bare coupling across a face already
interior to Omega_int^h (e.g. planar {x = x_I − 2h}), STEPs 1-2 run (the
coupling face lies outside C_h, so on C_h the glued difference is a
single C^1 solution of the homogeneous system, (cl-F) giving forcing
cancellation) and the exclusion is (H-UP-fam)'s class quantification
itself. Robustness re-verified by this lens over the F-2-restricted
depth family: for every admissible s <= h/2 ... < h, C_s ⊂ C_h gives
Omega_int^s ⊇ Omega_int^h, so a face interior to Omega_int^h is interior
to EVERY admissible interior domain — no depth re-choice evades the
class quantification. The closing scope sentence ("Bullet 1's
enlargement mechanism is thereby scoped to the one face the enlargement
internalizes") matches l0's demanded fix. One universal inside the new
bullet's own text fails on a counterexample instance: ESC3-5 below
(does not re-open ESC3-1 — the missing CASE is now covered and the
operative mechanism is correctly named).

**ESC3-2 (missing box conjunct) — DISCHARGED.** The premise now reads
"W^{1,infinity} on all of Omega_up WITH (G3)-BOX VALUES" with the
coercivity mechanism stated (uniform symmetrizer bounds
s_min I <= S <= s_max I on Omega_int^s; the rho-bar -> 0 / c-bar^2 -> 0
Lipschitz drift counter-instance recorded). Physics re-check by this
lens: the Euler symmetrizer degenerates exactly at the vacuum/degenerate
boundary (S eigenvalues carry rho-bar and 1/c-bar^2 factors), so box
membership IS the coercivity input and the recorded counter-instance is
genuine. The SAME premise sentence still under-specifies its DOMAIN
(space vs space-time) — a third, distinct clause: ESC3-6 below.

**ESC3-3 (contaminant mislabels) — DISCHARGED.** The falsifier now names
the STANDING DOWNSTREAM PULSE (pre-existing at t_p, outside Omega_up,
unconstrained by the trigger) + post-t_p growth in the roughened
UPSTREAM exterior; the superseded r3.3 sentence is retained with both
mislabels recorded faithfully against l0's ESC3-3 text. Window
arithmetic re-verified for the pre-existing pulse: the pinned trigger
covers closure-adjacent collar content at t_p, so above-bound influence
enters closure(C_h) at time >= t_p; terminal collar segment >= d_0 at
theorem-grade lambda_max gives arrival >= t_p + d_0/lambda_max = t_p +
2x the probed window d_0/(2 lambda_max) — exact. Edge case tried: pulse
trace sitting ON Gamma_I (= del Omega_up, measure-zero, arguably outside
the trigger's domain) at t_p — harmless: entry through Gamma_I at
exactly t_p is the equality case "collar entry time >= t_p" the
arithmetic already carries. Register row 1' cell mirrors the corrected
labeling ("standing downstream pulse, pre-existing at t_p outside
Omega_up, + any post-t_p upstream-exterior growth — r3.4, ESC3-3") with
the arrival-time reading explicit. CHECK.

**ESC2-6 (half-false "certified" slogan) — DISCHARGED as demanded.** The
split form is in place: CERTIFIED at Gamma_mid (Lemma 1.4 on the
(M-c)-monitored collar), HYPOTHESIZED at Gamma_in^coll ((H-UP-fam)'s
cross-face class, the NG-9 modulo — "certified by nothing"); the
superseded r3.3 slogan is retained in annotation with the reserved-word
ground recorded. The NG-9 overclaim this lens raised is gone. The
UNCHANGED tail clause of the same slogan ("a bare coupling's face is
crossed by nothing" — this lens's own proposed phrase, adopted) is newly
falsifiable against the r3.4 third bullet: ESC3-4 below.

**ESC2-7 ("never an input" false universal) — DISCHARGED.** The block
now reads "never an EXOGENOUS input" with the proof's actual data flow
stated in-line (STEP 2 = Theorem 1' hypothesis (ii) supplied by
(MID-TRACE); STEP 3 = (H-UP-fam)'s same-trace clause; consumed only as
STEP 1's established result; not part of the Claim's data set) and the
r3.3 phrase recorded as the fourth wording-universal defect of the
block-family. Attack tried: hunt for any remaining uncontrolled datum
crossing a straddled face — none (the only straddled face is Gamma_mid;
walls are frustum BOUNDARY, not straddled; Gamma_in^coll and Gamma_I are
cleared by R < d_0). CHECK.

**ESC2-8 (H^1 clause over-claims 1.5.3's regimes) — DISCHARGED, branch
(r-ii) landed as specified.** The Status-(a) H^1 clause now carries
"AND modulo the VARIABLE-TYPE trace theory on Gamma_mid", the mechanism
(u-bar·n_mid unconstrained by (D-coll)/Theorem 1'/Status (a), may cross
{0, ±c-bar}; on those loci characteristic but NOT uniformly and NOT of
locally constant multiplicity — outside both 1.5.3 regimes; the
cross-reference to Remark 1.5.5's identical loci on Gamma_in), the named
discharge condition (splits with Gamma_mid uniformly noncharacteristic:
|u-bar·n_mid| and |u-bar·n_mid ∓ c-bar| bounded below — re-checked: the
three exclusions {0, −c, +c} are all covered and uniform
noncharacteristicity IS sufficient for 1.5.3's Friedrichs regime (i) on
the Lipschitz face), and the (r-i) W^{1,1} Gauss-Green alternative
NAMED-NOT-CONSUMED with the honest "not verified in this document".
Attack tried: does the printed clause CLAIM existence of a uniformly
noncharacteristic split (which case (a) could not guarantee — nothing
pins u·n_mid away from sonic/grazing values at depth h/2, where no L4
margin is hypothesized)? It does not — "for splits with" is
conditional-on-instance. Both residuals mirrored in NG-3. CHECK.

**ESC2-9 (missing NG-3 register mirror) — DISCHARGED.** The NG-3 row now
carries the r3.4 additions IN the row: (i) the Gamma_mid ∩ Gamma_w
corner curves with provenance ("introduced in Section-1.6 prose r3.3,
mirrored here r3.4") and consumer ("the Status-(a) H^1 run of (H-UP-fam)
(Prop 1'', Section 1.6)"); (ii) the ESC2-8 variable-type trace residual
with its discharge condition and the named-not-consumed alternative; and
the TRIGGER clause extended ("any Status-(a)/H^1 consumption of
(H-UP-fam) at Prop 1'' (r3.4)"). Consumer-navigation test re-run: a
consumer discharging NG-3 against its own row now cannot close the gap
while the curves/loci remain live — exactly the demanded property. CHECK.

**Chain to the sustained originals — re-verified this round.**
L0-7(a)/L1-7(i) (quantifier order): the proof body is unchanged since
r3.2; eps_1 = d_0/(2 lambda_max) is a (D-coll)+collar constant and
eps_1' = min(eps_1, T_f − t*) > 0 keeps the window in-domain; STEP 1's
R-choice has uniform slack (lambda_max·eps_1' <= d_0/2 < d_0) — remains
DISCHARGED. L0-7(b)/L1-7(ii) (trace ON the source face): the only trace
concluded or consumed is on Gamma_mid, at fixed distance >= d_0 from
both uncontrolled-data faces; dependency order strictly {t*-slice zero}
→ (MID-TRACE) → {STEP 2, STEP 3} → UNION — remains DISCHARGED. The
judge's proves-too-much test (VERDICT §5) re-run on the r3.4 three-bullet
taxonomy: seven instances tried this round — the six of this lens's
round 2 (bare couplings across Gamma_in^coll, Gamma_mid, a deep interior
face, a transversal partly-in-collar face; the accidental-C^1-glue pair;
the Gamma_I non-coupling) plus NEW: a coupling face x = x_I − 3h/4
BETWEEN Gamma_in^coll and Gamma_mid, interior to C_h AND to
Omega_int^{h/2} — both bullet 2 (frusta straddle it where it cuts the
outer half collar) and bullet 3 (states solve across it) apply, no gap;
the derivation still proves nothing for any bare coupling, and where a
glued pair accidentally solves across its face the concluded uniqueness
is honest. PASSES substantively; residual wording defects in the
taxonomy's universals = ESC3-4/ESC3-5 below. **A-2/L1-8 (leg 17) —
remains FULLY LANDED.** r3.4 touched nothing in Remark 1.5.5; this
lens's spectrum computation re-run: at u·n = 0 spec = {−c, 0(×3), +c},
at u·n = −c spec = {−2c, −c(×3), 0}; adjacent distinct gaps = c-bar,
all pairwise separations >= c-bar, extreme acoustic pair 2c-bar (F-6
wording exact); multiplicity pattern (1,3,1) constant, eigenvectors
u·n-independent (A(n) shifts by (u·n)I), projectors regular; the
discontinuous object is the incoming-modes subspace map (one regular
eigenvalue's sign crossing flips a fixed mode's class) — the A-2
mechanism of record. No consumer cites the retired "1/c factors"
mechanism unannotated. CHECK.

**r3.4 revision-log block — VERIFIED.** Counts: 7 IDs = 3 (ESC3-1..3)
+ 4 (ESC2-6..9) = 0 B + 1 R (ESC2-8) + 6 A — matches both round files'
summary tables. The characterization of this lens's round-2 file
(proves-too-much passes on six instances; ESC2-1/2/4 ADEQUATE; ESC2-3
adequate-as-to-content modulo ESC2-7; ESC2-5 PARTIALLY ADEQUATE →
ESC2-8 + ESC2-9; A-2 re-verified by spectrum computation) is faithful.
The characterization of l0's round-3 file (ESC2-1/2/3 discharged clean;
ESC2-4 modulo ESC3-3; ESC2-5 modulo ESC3-2; zero inadequate dispositions
on that lens) is faithful. The no-dedup-collision claim (ESC3-1 vs
ESC2-6 same paragraph different sentences; ESC3-2 vs ESC2-8 same
sentence different clauses) is TRUE. Every disposition row's claimed
edit is present in the body at the anchor named. "No justified-rebuttal
rows" consistent with all seven findings FIXED. CHECK.

==============================================================================
## §2 OBJECTIONS (r3.4 text; verbatim quote + attack + class)

------------------------------------------------------------------------------
**ESC3-4 — class AMENDMENT. The r3.4 slogan's tail predicate "a bare
coupling's face is crossed by nothing" is face-absolute where the truth
is pair-relative: under the structure-of-the-proof reading it
contradicts the slogan's own first half at Gamma_in^coll (the SAME face
is declared crossed-by-a-hypothesized-structure and, three lines later
as bullet 1's coupling face, crossed-by-nothing); under the
pair-supplies reading it is false on the accidental-C^1-glue instance.
Declared: the tail is this lens's own round-2 proposed phrase, adopted
by the ESC2-6 disposition — adoption does not immunize (house precedent
ESC2-6/ESC2-7), and the defect became live through the same-window
interaction with the r3.4 third bullet, whose exclusion mechanism is
precisely that the crossing structure EXISTS and the pair fails to
belong to it.**

Quote (Section 1.6, "Why this does not prove too much", r3.4 slogan):
> "The exclusion is FACE-DEPENDENT: every face of the two-face
> decomposition is crossed by a NAMED structure of the proof — a
> CERTIFIED one at Gamma_mid (Lemma 1.4 on the (M-c)-monitored collar,
> theorem-grade) and a HYPOTHESIZED one at Gamma_in^coll ((H-UP-fam)'s
> cross-face solution class, the NG-9 modulo — certified by nothing) —
> and a bare coupling's face is crossed by nothing."

Attack (equivocation exhibited on named instances; no single reading
survives all three bullets). Reading A ("crossed by X" = a named
structure of the PROOF supplies cross-face content at that face): the
first half asserts Gamma_in^coll is crossed by (H-UP-fam)'s hypothesized
class; bullet 1's bare coupling has face Gamma_in^coll; so the tail
asserts the same face is crossed by nothing — a contradiction within the
slogan (and bullet 3 makes reading A untenable generally: its own
mechanism is that (H-UP-fam)'s states solve "the PDE across EVERY face
interior to that domain", so every deep bare-coupling face IS crossed by
a named structure of the proof — the exclusion is that the PAIR is not
in that structure's class). Reading B ("crossed by X" = the configuration
under test supplies a structure crossing the face): then the tail fails
on the accidental-C^1-glue instance (take one global solution of the
interior problem and declare it a two-subdomain "coupling with no
transmission condition" at {x = x_I − 2h}: the pair the coupling admits
DOES solve across its face — and the uniqueness then concluded through
STEP 3 is the honest statement, so the CONCLUSION of the paragraph is
safe while the sentence of record is false). The bullets beneath carry
the correct pair-relative mechanisms, so no derivational content moves —
but this slogan is the sentence the E-4 adjudicator reads first, in the
block-family with four recorded wording-universal defects. Fix (one
clause, pair-relative): "...— and a bare-coupled pair belongs to no
structure of the proof that crosses its face (where a glued pair
accidentally does solve across its face, the concluded uniqueness is the
honest statement, not an over-proof)." **Class: AMENDMENT.**

------------------------------------------------------------------------------
**ESC3-5 — class AMENDMENT. The r3.4 third bullet's universal "the
bare-coupled pair does not [solve across the face] ... so the glued pair
is not in (H-UP-fam)'s class and STEP 3 has nothing to consume" is false
on the accidental-C^1-glue instance of the judge's own test class — the
fifth wording-universal defect minted at this block-family (the r3.4
text itself records the count at four).**

Quote (Section 1.6, third proves-too-much bullet, r3.4):
> "the operative exclusion is (H-UP-fam)'s class quantification ITSELF:
> the states it quantifies over solve the interior problem on all of
> Omega_int^{h/2}, hence the PDE across EVERY face interior to that
> domain, while the bare-coupled pair does not — the coupling supplies
> only piecewise uniqueness on the two pieces with the trace-feed across
> its face uncontrolled (the r2 circularity reproduced INSIDE the
> interior domain) — so the glued pair is not in (H-UP-fam)'s class and
> STEP 3 has nothing to consume."

Attack (counterexample inside the quantified class). The judge's §5 test
ranges over "ANY transmission coupling with NO transmission condition".
Instance: split Omega_int^{h/2} at Gamma'' = {x = x_I − 2h} into two
subdomains with NO transmission condition, and feed the proof a pair
whose members happen to glue C^1 across Gamma'' (e.g. restrictions of
two globally-defined interior solutions — nothing in a bare coupling
FORBIDS smooth gluing; it merely fails to REQUIRE it). For that pair the
quoted middle clause is false ("the bare-coupled pair does not" — it
does), the conclusion clause is false ("the glued pair is not in
(H-UP-fam)'s class" — it is: its members solve the interior problem on
all of Omega_int^{h/2}), and STEP 3 consumes it — legitimately, because
uniqueness for pairs that genuinely solve across the face is the honest
content of (H-UP-fam), not an over-proof. The true statement, and the
one that does the excluding work, is about what the COUPLING supplies:
it certifies no cross-face solvability, so the class-membership premise
of STEP 3 is unavailable AS A CONSEQUENCE OF THE COUPLING — while
individual pairs may still qualify on their own merits. Same defect
class as L1-4, ESC2-2, ESC2-3, ESC2-7 (a true mechanism stated as a
false universal), in the sentence carrying the ESC3-1 repair itself. No
proof step consumes the paragraph; the paragraph's conclusion is true on
the instance (verified: the concluded uniqueness is honest). Fix (one
clause): "...while the bare coupling CERTIFIES no such cross-face
solvability for its pairs — a glued pair enters (H-UP-fam)'s class only
if it happens to solve across the face, in which case the concluded
uniqueness is the honest statement — so STEP 3 has nothing the COUPLING
supplies to consume." **Class: AMENDMENT.**

------------------------------------------------------------------------------
**ESC3-6 — class AMENDMENT. The Status-(a) premise pins the base-state
regularity on the SPATIAL domain only ("W^{1,infinity} on all of
Omega_up"), against the document's own cylinder convention ((H1.1),
(H1.1')) — and the (EI)/Gronwall run the premise feeds consumes
time-regularity and time-uniform box bounds (∂_t S enters the volume
constant). Third missing/underspecified conjunct at the same premise
sentence, distinct from ESC3-2's box clause and ESC2-8's trace label
(same-sentence-different-clause, the no-collision pattern the r3.4 log
itself records).**

Quote (Section 1.6, Status of (H-UP-fam), case (a), r3.4-edited premise):
> "(a) If W-bar is W^{1,infinity} on all of Omega_up WITH (G3)-BOX
> VALUES (r3.4, repairs ESC3-2 — regularity and box membership are
> SEPARATE conjuncts everywhere in this document, (H1.1)/(H1.1'), ...)"

Attack (hypothesis accounting under the document's own convention — the
exact argument form the ESC3-2 parenthetical itself deploys). The two
conventions the parenthetical cites both pin the CYLINDER: (H1.1) is
"W^{1,infinity} on ALL of Omega_up x [0,T_f]" (Section 1.6 opening,
line ~668); (H1.1') is "W-bar in W^{1,infinity}(C_h x [0, T_f])"
(Theorem 1' hypothesis line). The premise as printed quantifies over
"Omega_up" alone — read literally, a base state Lipschitz in x on each
time slice but ROUGH IN TIME (e.g. W-bar(x, t) = W_0(x) + a(t) V(x)
with a in C^0 \ W^{1,infinity} staying inside the box) satisfies it,
while the (EI) run the case sketches fails: differentiating
E(t) = Int <S(W-bar) U, U> produces the volume term <(∂_t S) U, U>,
whose L^infinity bound is exactly the time-half of the W^{1,infinity}
hypothesis, and the Gronwall constant C_0 needs it uniformly on
[t_0, t_1]. The gap is not deliverable from the box clause (a pointwise
range condition, orthogonal to regularity — ESC3-2's own dichotomy).
Everywhere else the document writes the cylinder; this premise is the
only regularity hypothesis in Section 1.6 printed without it. Fix
(three words): "W^{1,infinity} on all of Omega_up x [0, T_f] WITH
(G3)-BOX VALUES". Load-bearing only for the smooth-base sanity
reduction (case (b)/NG-9 untouched; the two-face proof consumes nothing
of this). **Class: AMENDMENT.**

==============================================================================
## §3 CONFIRMED passages (strongest attack tried, each)

**C3L1-1 — the two-face proof core at r3.4 (Claim + (cl-F)/(cl-C),
(D-coll), (H-UP-fam) restricted quantifier, eps_1', STEPs 1-3, UNION):
CONFIRMED (byte-level r3.2 text; no new angle).** Attacks re-tried this
round: (α) the retracted r2 defects (a)/(b) against the standing text —
no analogue (uniform eps_1 from (D-coll); conclusions never evaluated on
a data-carrying face); (β) a rotating-wave collar base with azimuthal
speed exceeding the axial one — Lemma 1.4's lambda_max bounds spec A(nu)
for EVERY unit nu, no direction escapes the frustum shrink; (γ)
d_0-geometry evasion by tilting Gamma_mid until it grazes Gamma_I —
excluded by (D-coll)'s d_0 > 0 clause itself. Delivered strength stays
THEOREM modulo (H-UP-fam); LABEL OF RECORD SCHEMA per J-r2p-1, correctly
carried at every consumer site re-checked (Section 1.6 rigor block,
register row 1', the r3.4 log; restoration = the E-4 adjudication only).

**C3L1-2 — the ESC2-6 repair's split slogan, first half + annotation:
CONFIRMED (the tail clause is ESC3-4).** Strongest attack: whether
"CERTIFIED ... theorem-grade" at Gamma_mid overclaims — it does not
(Lemma 1.4 is THEOREM on the collar and (M-c) monitors exactly (H1.1') +
box there, the monitored-hypothesis accounting matching); whether the
NG-9 characterization "certified by nothing" is too strong — it is
exact (NG-9 row: SCHEMA, standard-physical, unwritten).

**C3L1-3 — the ESC2-7 repair ("never an EXOGENOUS input" + data-flow
parenthetical): CONFIRMED.** Strongest attack: hunt for a remaining
false universal in the corrected block — "no UNCONTROLLED data crosses a
straddled face" checked against every straddled face (only Gamma_mid;
its crossing datum is STEP-1-derived, controlled) and against the walls
(frustum boundary, not straddled). The exogenous/derived split now does
the (r-b)-distinguishing work correctly.

**C3L1-4 — the ESC3-1 repair's third bullet, mechanism core: CONFIRMED
(the pair-universal is ESC3-5).** Strongest attacks: (α) depth-family
evasion — fails, every admissible Omega_int^s contains a
face-interior-to-Omega_int^h in its interior (§1); (β) "STEPs 1-2 RUN"
verified on the instance (coupling face outside C_h, so U|C_h is a
single C^1 homogeneous solution given (cl-F)); (γ) the scoping sentence
("Bullet 1's enlargement mechanism ... scoped to the one face the
enlargement internalizes") — exact: the enlargement Omega_int^h →
Omega_int^{h/2} internalizes Gamma_in^coll and nothing else.

**C3L1-5 — the ESC3-2 repair (box conjunct + coercivity parenthetical):
CONFIRMED (the domain clause is ESC3-6).** Strongest attack: whether the
recorded counter-instance is physical — it is (Euler symmetrizer
degenerates at rho-bar → 0 / c-bar² → 0; a Lipschitz base can drive its
infimum to zero on a bounded domain); whether (H1.1') closes the gap off
the collar — it cannot (collar-only by construction, as the text states).

**C3L1-6 — the ESC2-8 repair (variable-type trace clause, branch r-ii):
CONFIRMED.** Strongest attacks: (α) sufficiency of the printed uniform
noncharacteristicity condition for 1.5.3's Friedrichs regime (i) —
holds (all three loci {0, ±c-bar} excluded with uniform bounds; A(n_mid)
uniformly nonsingular on the face); (β) whether the clause silently
claims existence of such a split in the device class — it does not
(conditional-on-instance phrasing; physically honest, since nothing pins
u·n_mid at depth h/2 where no L4 margin lives); (γ) whether the (r-i)
naming smuggles in an unverified consumption — it does not
("named-not-consumed ... not verified in this document").

**C3L1-7 — the ESC3-3 repair (contaminant relabeling + arithmetic +
register mirror): CONFIRMED.** Strongest attacks: the Gamma_I-boundary
edge case at t_p (equality case already carried, §1); collar-internal
post-t_p Gronwall amplification (absorbed in the scheme-bound language,
prior record — and a mid-face signal from broken collar dynamics is what
the leg must reject); wall-penetrating shortcut paths (impassable — the
terminal segment after the last Gamma_in^coll ∪ Gamma_I crossing lies in
closure(C_h)); the row-1' condensed cell parses correctly (arrival >=
t_p + d_0/lambda_max, with d_0/lambda_max = 2x window an exact equality).

**C3L1-8 — the ESC2-9 repair (NG-3 row + trigger): CONFIRMED.**
Strongest attack: the consumer-navigation test (discharge NG-3 against
its own row and check the Prop-1'' residuals survive) — they do: both
r3.4 additions and the trigger clause are in the row; provenance
("introduced ... r3.3, mirrored here r3.4") matches the actual edit
history, no back-dating.

**C3L1-9 — the r3.4 revision-log block: CONFIRMED.** Attack tried: any
disposition row without its body edit, any count mismatch vs the two
consumed round files, any unfaithful characterization of THIS LENS'S own
round-2 verdicts, any silent re-mint — none found (§1).

**C3L1-10 — leg-17 Remark 1.5.5 (A-2 + L1-8 + F-6 chain), r3.4-untouched,
re-verified per the brief: CONFIRMED — A-2 remains fully landed.**
Strongest fresh attack this round: perturb the base state so that TWO
loci coincide on Gamma_in (u-bar·n = 0 and u-bar·n = −c-bar at nearby
points with c-bar varying) hunting for a projector collision the
adjacent-gap wording would miss — fails: at every point the three
distinct eigenvalues keep pairwise separations >= c-bar(x) > 0 pointwise
(the (G3) box bounds c-bar below on the relevant sets), and the F-6
wording quantifies pointwise, not with a global constant. Spectrum
computation re-run at both loci (§1); conclusion/scoping unchanged; the
retired r2 mechanism survives only inside its annotation.

==============================================================================
## §4 SUMMARY TABLE

| ID | Passage (r3.4 text) | Class |
|---|---|---|
| ESC3-4 | proves-too-much slogan tail: "a bare coupling's face is crossed by nothing" — face-absolute predicate, contradicts the slogan's own first half at Gamma_in^coll under one reading and the accidental-C^1-glue instance under the other; pair-relative fix | AMENDMENT |
| ESC3-5 | third bullet's universal "the bare-coupled pair does not ... so the glued pair is not in (H-UP-fam)'s class" — false on the accidental-C^1-glue instance of the judge's test class; the coupling certifies nothing, individual pairs may qualify (honest uniqueness) | AMENDMENT |
| ESC3-6 | Status-(a) premise "W^{1,infinity} on all of Omega_up" omits the time cylinder of the document's own (H1.1)/(H1.1') convention; the (EI) run consumes ∂_t S and time-uniform bounds | AMENDMENT |

Totals: **3 objections = 0 BREAKS-THE-LEG + 0 REPAIR-NEEDED +
3 AMENDMENT.** Discharge verdicts (§1): ESC3-1 DISCHARGED (modulo
ESC3-5 in its own new sentence); ESC3-2 DISCHARGED (modulo ESC3-6,
same sentence, different clause); ESC3-3 DISCHARGED; ESC2-6 DISCHARGED
(modulo ESC3-4 on the adopted tail); ESC2-7, ESC2-8, ESC2-9 DISCHARGED
clean; L0-7(a)/(b) = L1-7(i)/(ii) remain DISCHARGED; the judge's
proves-too-much test PASSES substantively (seven instances this round);
A-2/L1-8/F-6 remains fully landed. No finding touches a step of the
two-face proof; all three findings are one-clause wording amendments in
the honesty commentary and the Status-(a) premise — the same dryness
signature lens l0 reported for its round 3 (ESC3-1..3, all AMENDMENT).
No label motion is proposed: SCHEMA per J-r2p-1 stands, restoration =
the E-4 adjudication only. This lens's dryness reading is subject to
the seed-protocol gate (LG-1/E-5), which this refutation does not and
cannot discharge.

==============================================================================
## §5 SELF-FALSIFIERS (what kills each finding)

- ESC3-4 dies if a SINGLE fixed reading of "crossed by" is exhibited
  under which the slogan is true on all three bullets' instances: the
  structure-of-the-proof reading fails at Gamma_in^coll (the slogan's
  own first half names its crossing structure while bullet 1 makes it a
  bare coupling's face), and the pair-supplies reading fails on the
  accidental-C^1-glue pair (which does supply cross-face solvability).
  It also dies if the accidental-glue configuration is shown excluded
  from "bare coupling" of record (no such exclusion is printed — a bare
  coupling imposes NO condition, hence forbids nothing).
- ESC3-5 dies if the accidental-C^1-glue pair is shown outside the
  judge's §5 test class ("ANY transmission coupling with NO transmission
  condition" — it is a transmission coupling with no condition), or if
  such a pair is shown NOT to lie in (H-UP-fam)'s class (its members
  solve the interior problem on all of Omega_int^{h/2} by construction),
  or if "the bare-coupled pair" is shown of record to denote only pairs
  with discontinuous glue (no such restriction is printed).
- ESC3-6 dies if the (EI)/Gronwall run is shown not to consume ∂_t S
  (it differentiates E(t) = Int <S U, U> in time — the term is
  unavoidable), or if a document convention is exhibited under which
  "on Omega_up" denotes the space-time cylinder of record (the cited
  conventions (H1.1)/(H1.1') spell the cylinder out explicitly — the
  opposite), or if W-bar is shown pinned time-independent at Status (a)
  (nothing in Section 1 pins it; (H1.1) explicitly allows t-dependence).

END — machine summary: {objections: 3, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc3_r3_l1.md}
