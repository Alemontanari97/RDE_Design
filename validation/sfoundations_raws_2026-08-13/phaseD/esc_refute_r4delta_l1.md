# R22-F CENTERPIECE — TARGETED ROUND-4-DELTA REFUTATION (RES-CAP-1),
# LENS L1 (PDE / hyperbolic structure). ONE ROUND.

Session: S-FOUNDATIONS-C4 escalation window, 2026-08-20. Slot E-5
(VERDICT_blocco2.md §3 E-5, carried by reference from VERDICT_r22f §4
RES-CAP-1). SCOPE RESTRICTED to the unrefuted round-4 delta of
phaseD_r22f_centerpiece.md: [REV2-r4-1] (mu functional identity +
H-G6/L_H), [REV2-r4-2] (instance-checked-convexity narrowing),
[REV2-r4-3] (eps_U sweep-sup licensing), [REV2-r4-5] ((vi)-row cell
edits), and the §13 disposition table. Out-of-scope observations are
filed as NOTE only. This file is the ONLY carrier file this slot
writes (plus its named probe script).

READ-DEPTH DECLARATIONS (this window):
- phaseD_r22f_centerpiece.md: [TARGETED-FULL at the delta] — all
  [REV2-r4-*] marker sites read in full at-site (:558-975 §2.2-bis +
  [REV2-r2-3]/[REV2-r3-1/2/3]/[REV2-r4-1/2/3] blocks; :1482 (vi) row
  as printed; :1496-1560 [REV2-r4-5]/[REV2-r3-6]; :1780-1835 R-13..
  R-17 residue blocks; :1900-1928 [REV2-r4-6]; :2110-2175 §13),
  plus greps for propagation checks (commands quoted at the findings).
- blocco3/VERDICT_r22f.md: §§1, 4, 5 [FULL]; §6 skimmed for context.
- blocco3/VERDICT_blocco2.md: §§1, 3, 4 [FULL at the E-5 mandate].
- phaseD_r22f_refute_r4_l0.md / _l1.md / _l2.md: [FULL] (413 + 223 +
  318 lines — the prescribed fix shapes are the delta's inputs).
- Rounds 1-3 refute files: [NOT-READ] this window — the delta's own
  superseded-fragment quotations and the two closure verdicts carry
  the needed round-1..3 context; no finding below leans on an unread
  round file.
- No M0 re-read; no paper read (no finding needs one).
EXECUTABLE PROBE (standing preference honored): validation/
sfoundations_raws_2026-08-13/phaseD/esc_probe_r4delta_lh_leg3_
blindness.py — WRITTEN and RUN this window, ALL ASSERTS PASS (parts
A/B feed E5-L1-2; part C feeds E5-L1-5). Synthetic counter-models
only; pinned-env numpy only; derived tolerances; CT-6 clean.

MEASURED COMMANDS OF THIS WINDOW (SR-12):
- `grep -n "REV2-r4" phaseD_r22f_centerpiece.md` → delta census (44
  marker lines; blocks at :58-71, :817-956, :1500-1546, :1810-1834,
  :1907-1928, :2115-2175; at-site pointers :606/:639/:647/:680/:717).
- `grep -n "engine curvature" phaseD_r22f_centerpiece.md` → :571,
  :1482 (in-cell, repaired), :1505 (superseded quote), :1683 (GAP
  FLAG history) — feeds E5-L1-1.
- `grep -n "delta/mu\|delta(S\*_red)/mu" ...` → live licensed-bound
  prints at :603/:609/:782/:1482 — feeds E5-L1-1.
- `grep -n "prox-regular" ...` → 15 sites; all licensing sites
  purged; survivors = superseded quotes (:898, :913, :1505/:1515,
  :1812), probe/rationale text, guarded R-17 sites (:906-911, :1798,
  :1831), and the LIVE R-14 parenthetical :1791 — feeds E5-L1-5/6.
- `grep -n "convexity/prox-regularity" ...` → :913, :1515, :1812
  (superseded quotes) + :1791 (live) — feeds E5-L1-6.

==============================================================================
## VERDICT SUMMARY (this lens, one round)

The round-4 delta is SOUND IN ITS CORE MOVES: the functional-identity
diagnosis and the H-G6 transfer inequality are correct (Weyl-type
eigenvalue transfer, valid on any cone under the M-operator-norm
reading); the (F) J_red-side one-line derivation is exact (re-derived
by hand below, E5-L1-7(a)); the convexity-only narrowing is a strict
narrowing with the Tietze–Nakajima clause correctly hypothesized; the
eps_U sampled-sup clause is the right class discipline; the six
(vi)-row cell edits are all present as described; the §13 table is
arithmetically exact against the three round-4 files. NO BREAK.
However the delta is INCOMPLETE in carriage and in the measurement-
class discipline it itself established: 2 REPAIRs + 3 AMENDMENTS +
2 NOTEs below. The loop's own precedent (RES-CAP-1's reason line:
refuter-prescribed text broke twice) recurs here in mild form — the
round-4 fix under-covers its own anchor list (E5-L1-1) and mints a
new sup-type measured object without the class label minted the same
round for eps_U (E5-L1-2).

==============================================================================
## FINDINGS

### E5-L1-1 — REPAIR: the [REV2-r4-1](a) functional-identity carriage
### is INCOMPLETE — two LIVE bare-mu sites escaped the at-site pointer
### pass, one of them named in the BREAK's own anchor list and
### executor-facing

ANCHORS (grep-verified this window): the (a) pointers were inserted at
condition (1) :606, form (T) :639, form (C) :647, plus the (D) read
:680 and the (F) measured-carrier pointer :717. Escaped LIVE sites:
(i) :570-571 — the §2.2-bis OBJECT paragraph itself: "||·||_{M*} the
    DUAL norm of the design-space metric M in which THE ENGINE
    CURVATURE mu is an eigenvalue". This is the schema's defining
    paragraph identifying mu WITH the engine (J_red) curvature — the
    exact conflation R22F-L0-19 broke, still printed at the definition
    site. Under the r4 identity mu is the J_TRUE floor and the engine
    curvature only instantiates it UNDER H-G6; the sentence's
    metric-naming function survives a one-bracket repair ("the metric
    of the engine's design parameterization, in which the MEASURED
    CARRIER is an eigenvalue [mu itself = the J_TRUE floor,
    [REV2-r4-1](a)]").
(ii) :777-784 — [REV2-r3-2]'s printed bound "||S*_true − S*_red|| ≤
    delta(S*_red)/mu. A future M-RED gradient-rider executor evaluates
    delta at S*_red and at no other point." — the MOST executor-facing
    gradient-route sentence in the file, bare mu, no H-G6 gate. This
    site was in R22F-L0-19's OWN anchor list (r4_l0 :121-123 cites
    ":735-742 prints the bound"); the fix shape's site list (forms
    (T)/(C) + condition (1)) under-covered the anchors and the reviser
    applied the fix shape faithfully — the RES-CAP-1 exposure class
    exactly (a defect of the prescription, not of its application).
WHY IT MATTERS: an executor consuming [REV2-r3-2] (or the OBJECT
paragraph) without the remote [REV2-r4-1] block reproduces probe
r4_l0 PART A's 100x violation with every printed at-site check
passing. The loop's own carriage standard (R22F-L0-16, REPAIR: a
hypothesis must be carried at EVERY licensing site, never flat)
applies verbatim to the identity declaration.
WHY REPAIR, NOT BREAK: the global declaration [REV2-r4-1](a) ("at
every curvature sentence") exists in-file and disambiguates a
whole-file reading; the defect is carriage completeness — the L0-16
precedent class.
FIX SHAPE (two bracket insertions, append-only markers, nothing
removed): at :571 and :782, the same at-site bracket as :606/:639/:647
("[mu = the J_TRUE floor, [REV2-r4-1](a); measured-carrier
instantiation only UNDER H-G6, [REV2-r4-1](c)]"). The landing list
(L-2, [REV2-r4-6](a)) inherits both touches.

### E5-L1-2 — AMENDMENT (probe parts A and B, RUN): H-G6 deriver
### leg (3) lacks the measurement-class discipline the SAME round
### minted for eps_U — the measured directional Hessian-gap is a
### DIRECTIONAL, FINITE-SAMPLE lower estimate of L_H, blind in both
### the direction and the sub-sample dimensions, and it enters
### mu_eff = mu_meas − L_H ANTI-conservatively

ANCHORS: [REV2-r4-1](b) STATUS :846-853 — "(3) M-RED gradient-rider
EXTENSION — divided differences of the MEASURED gradient gaps along
the §3.6 design sweep = measured directional Hessian-gap"; R-15
extension :1816-1822 — the leg "rides the same rider" but the
[REV2-r4-3] SAMPLED-SUP class label + stability clause is stated FOR
eps_U ONLY; R-16 :1823-1830 names no class for the leg-(3)
measurement.
DEFECT (two limbs, both probe-witnessed):
(a) DIRECTIONAL BLINDNESS (probe PART A): L_H is an M-operator-norm
    sup over the ball; divided differences along the sweep see only
    ||(H_true − H_red)·d_sweep|| for sweep directions. Counter-model:
    Hessian gap concentrated in the off-sweep direction — the sampled
    directional gap is IDENTICALLY ZERO at every sampling density
    (so it is trivially "sustained under sweep-sampling refinement":
    even a [REV2-r4-3]-pattern stability clause does NOT catch it),
    while the true L_H = 0.99·mu and the bound computed with
    mu_eff = mu_meas − L_H_sampled is violated 100x — unbounded as
    c → mu — with H-G5 convex (full space), metric consistent,
    constant Hessians (any (E)-ladder certificate passes), H-G4 moot,
    and the functional identity honored. The defect is ISOLATED to
    the measurement class of the deriver.
(b) SUB-SAMPLE-WIDTH BLINDNESS (probe PART B): a C¹ curvature spike
    of half-width h_sweep/8 strictly between sweep samples gives
    sampled gradient gaps EXACTLY ZERO at two refinement levels
    (hence sampled directional Hessian-gap = 0 and, incidentally,
    sampled delta = 0), while the actual argmax shift is macroscopic
    (0.037) and the true 1-D L_H = 2548 >> mu. The exact mirror, one
    derivative up, of the round-4 part-G spike that motivated
    [REV2-r4-3] itself.
ANTI-CONSERVATIVE DIRECTION, stated: an UNDER-estimated L_H
OVER-estimates mu_eff and hence UNDER-states delta/mu_eff — an
overclaim of optimum coverage; same direction as the eps_U defect
L0-21/L2-26 fixed, one derivative up.
WHY AMENDMENT, NOT BREAK/REPAIR: nothing false is asserted today —
L_H is UNDERIVED, R-16 forbids any number until it "lands", and no
licensing occurs; the defect is that "lands" is undefined for a
MEASURED deriver leg, and the file's own instantiates-never-
discharges discipline ([REV2-r4-3]) is not carried to it. Identical
classification structure to L0-21/L2-26 (both AMENDMENT).
FIX SHAPE (one clause in H-G6 STATUS + carriage into R-15/R-16, the
[REV2-r4-3] template): "the leg-(3) measurement instantiates L_H at
SAMPLED-DIRECTIONAL (estimate) class ONLY — a finite-sample lower
estimate along the SWEPT directions alone; off-sweep curvature-gap
content and sub-sample-width structure are declared UN-EXCLUDED
(probe of record esc_probe_r4delta_lh_leg3_blindness.py parts A-B);
a directional estimate NEVER lands L_H by itself — landing requires
deriver (1) or (2) at norm level, or a declared direction-coverage
certificate; until then mu_eff licenses NO number (R-16 unchanged)."

### E5-L1-3 — AMENDMENT: H-G6 definitional completeness — three
### missing guards (second-order existence; L_H norm typing; mu_eff
### positivity)

ANCHORS: H-G6 :839-845; H-G3 :586-589 ("differentiable-front regime —
no crossing events inside the perturbation ball"); the typing
precedent [REV2-r2-3](B) :655-663 (delta's Moreau/Riesz typing block,
minted after the L0-14(a) attack); R-17 :1831-1834 (prints "> 0").
LIMBS (this lens's turf — front regularity is the L1 seam):
(a) EXISTENCE / SECOND-ORDER FRONT REGULARITY: L_H := sup_ball
    ||H_true − H_red||_M presupposes H_true EXISTS ball-wide. For a
    front-carrying J_true, H-G3's first-order differentiable-front
    regime delivers gradients, not Hessians: second design
    derivatives of the front-atom pairings carry front ACCELERATION
    terms (∂²_S x_front) and exist only in a twice-differentiable
    front regime (no grazing/tangency events at second order). Where
    J_true is C¹-but-not-C² on the ball, L_H is undefined/infinite —
    the honest outcome is REFUSAL, but no printed clause says so, and
    the leg-(3) measurement would return finite directional values
    while the true transfer is unbounded (the E5-L1-2(b) spike is the
    finite-height shadow of exactly this). The same clause licenses
    the (b)-sentence "by the adjoint representation it decomposes
    along the same (J)/(H) channels at second order" — true at schema
    grade ONLY under second-order shape-differentiability + the
    H-RED-2(SBV) measure-stability that excludes Cantor-channel
    curvature content.
(b) NORM TYPING: "||H_true − H_red||_M" is untyped. The Weyl-type
    transfer mu_true_floor ≥ mu_meas − L_H (valid, checked this
    window, on any cone) requires the M-OPERATOR norm
    (sup_{||d||_M=1} |d^T(H_true − H_red)d|, i.e. the norm of the
    M-Riesz-lifted operator); a mismatched (e.g. weighted-Frobenius)
    reading breaks norm-invariance exactly as condition (3) warns
    for delta. delta received the full (B) typing block after the
    same class of attack; L_H received none.
(c) POSITIVITY GUARD: mu_eff = mu_meas − L_H licenses nothing unless
    mu_eff > 0; R-17's parallel clause prints "> 0", H-G6 does not.
    One executor guard sentence ("mu_eff ≤ 0 ⇒ instantiation refused,
    declared") closes it.
WHY AMENDMENT: no false assertion today (nothing licenses until L_H
lands); three one-clause completions of newly-minted hypothesis text.
FIX SHAPE: add to H-G6: "(existence) H_true is twice differentiable
on the certified ball — the second-order strengthening of H-G3; a
front-topology or grazing event inside the ball exits to the g2b
calculus, named exit, and L_H is DECLARED UNDEFINED there (refusal,
not a number); (typing) ||·||_M = the M-operator norm via the (B)
Riesz identification; (guard) mu_eff > 0 required, else instantiation
refused." Landing rides L-2 ([REV2-r4-6](a)).

### E5-L1-4 — AMENDMENT: mu symbol overload inside the (vi) BEST cell
### + a one-symbol landing rename for a two-object family — the
### landed text can re-conflate exactly what L0-19 broke

ANCHORS: [REV2-r4-1](d) :865-874 — "The two routes' mu are DISTINCT
objects and are never again treated as one"; the (vi) BEST cell
:1482 — opens "mu = the curvature floor of J_TRUE" then prints the
value route "2·sqrt(eps_U/mu)" whose mu is "legitimately the measured
carrier as-is" — ONE symbol, two declared-distinct objects, in a
single landing-facing cell, disambiguated only by mid-cell
parentheses; [REV2-r4-1](a) tail + [REV2-r2-3](C): at landing the
schema's curvature symbol is renamed mu_curv "and carries this
identity" (= the J_TRUE floor) — NO second symbol is assigned to the
value route's J_red floor. An M0 landing editor applying the rename
uniformly would stamp the J_TRUE identity onto the value-route
formula, whose soundness rests precisely on its mu being the J_RED
floor ((d)'s own derivation) — the re-conflation risk is created by
the delta's own rename instruction.
WHY AMENDMENT: the draft text is internally disambiguated (nothing
false as printed); the defect is a landing-instruction ambiguity in
[REV2-r4-6](a)/(b).
FIX SHAPE (naming only): the landing list assigns TWO symbols —
mu_curv (gradient route, J_TRUE floor, H-G6-gated) and mu_red (value
route, measured J_red floor, carrier-as-is per [REV2-r4-1](d)) — and
the (vi) cell's two formulas land with their own symbols; one
sentence in [REV2-r4-6] carries it.

### E5-L1-5 — REPAIR (probe part C, RUN; seam declared: feasible-set
### geometry is L0 turf, filed here under the zero-inflation-outranks-
### turf protocol — the defect sits in r4-minted residue text this
### slot must clear): the R-17 refinement clause, listed as an R-14
### DECIDER, is satisfiable ON THE ROUND'S OWN COUNTER-MODEL — its
### derivation-as-specified would re-license the probe-killed geometry

ANCHORS: [REV2-r4-2](a) :906-911 — the prox-regular branch "retained
ONLY as a NAMED F2 REFINEMENT candidate carrying the curvature-
corrected floor clause (mu_eff = mu − |lambda*|·kappa_max > 0,
kappa_max = ... 1/r_prox; SCHEMA, deriver named ...)"; R-14 deciders
:1793-1802 — "... OR the F2 curvature-corrected prox-regular
refinement ([REV2-r4-2](a)) ..."; R-17 :1831-1834 — "NOT a licensing
branch until derived".
DEFECT: the clause repairs the wrong horn ALONE. The round-4 record
contains TWO distinct prox-regular failure modes: (i) the effective-
curvature horn (r4_l0 PART B: boundary concave toward the feasible
side, mu − |lambda|·kappa correction — what R-17 prices), and (ii)
the segment-feasibility/topology horn (r4_l2 annulus parts A-F:
antipodal argmax migration through the hole, form-(T) support-
function residual = 0 — what NO curvature formula can price). On the
annulus counter-model OF RECORD the printed R-17 clause PASSES:
mu_eff = mu − |lambda*|·kappa_max = eps > 0 (probe part C, RUN:
lambda* = mu − eps, kappa_max = 1/r_prox = 1), while the re-licensed
form-(T) bound is delta_T/mu_eff = 0 against actual shift 2. The
local second-fundamental-form floor is CLASSICAL and therefore
DERIVABLE exactly as specified — an F2 executor can honestly derive
everything R-17 asks for and the R-14 decider branch then reads
"decided", re-licensing forms (T)/(F) on prox-regular sets where the
same window's probe already exhibits unbounded failure with every
printed check passing.
WHY REPAIR, NOT BREAK: guarded today ("NOT a licensing branch until
derived" — nothing false is licensed at closure); the defect is a
decider/refinement SPECIFICATION whose stated satisfaction condition
does not cover its exposure — the L0-20 class (a licensing line whose
stated form does not cover its exposure), one guard-level removed.
WHY NOT out-of-scope: R-17, the R-14 decider rewording, and the
retention clause are all [REV2-r4-2]/[REV2-r4-4] minted text.
FIX SHAPE (one scope clause at R-17 + mirrored in the R-14 decider):
"the curvature-corrected clause prices the effective-curvature horn
ONLY and can license at most LOCAL-argmax tracking; any derived form
additionally requires a segment-feasibility clause (the segment
between S*_red and the candidate argmax feasible — the H-G5 rationale
property), absent which the annulus counter-model of record
(r22f_v2_probe_r4_l2_proxreg_annulus.py; esc_probe_r4delta_lh_leg3_
blindness.py part C) is the standing refuter any derivation must
refuse; GLOBAL-argmax coverage on prox-regular nonconvex sets remains
un-claimable by this refinement." R-14's decider branch carries the
same clause so its discharge cannot be read from the formula alone.

### E5-L1-6 — NOTE: live R-14 parenthetical retains the withdrawn
### pairing (hygiene touch at landing; nothing false)

:1791 "OPEN (no convexity/prox-regularity certificate of record
exists ...)" is LIVE text (the r4-2(b) edit reworded only the decider
sentence that follows). As an ABSENCE claim it is true a fortiori and
licenses nothing; but it re-prints the withdrawn pairing in
landing-facing residue text ([REV2-r4-6](c) lands R-14). One-word
touch at landing: "no convexity certificate (nor any other licensing
certificate)". No class above NOTE is warranted.

### E5-L1-7 — NOTE: verified-green ledger of this targeted pass
### (zero credit inflation; each item checked this window)

(a) (F) J_red-side derivation re-derived by hand: strong concavity of
    J_red + first-order optimality of S*_red on the convex feasible
    set (H-G5) give J_red(x1) − J_red(x2) ≥ (mu_red/2)·shift²; the
    eps_U premise at the two argmaxes gives 0 ≤ J_true(x2) −
    J_true(x1) ≤ 2·eps_U − (mu_red/2)·shift² — the printed chain is
    EXACT and its mu is legitimately the measured carrier. The
    asymmetry statement (value route measured-carrier-sound, gradient
    route H-G6-gated) is correct.
(b) H-G6 transfer inequality checked: Weyl-type eigenvalue transfer
    min_cone(−H_true) ≥ min_cone(−H_red) − ||E|| holds on ANY cone
    under the M-operator-norm reading (the E5-L1-3(b) typing is what
    makes it a theorem); sign convention (C) composes correctly.
(c) [REV2-r4-2] narrowing verified: strict narrowing, nothing else
    touched; Tietze–Nakajima stated with its closed+connected
    hypothesis inline (an executor must check connectedness of
    C ∩ ball — stated, so no false license); prox-regular purge
    complete at every LICENSING site (grep of record above; survivors
    are superseded quotes, guarded R-17 sites, and :1791 → E5-L1-6).
(d) [REV2-r4-3] verified: the adopted L2-26 form CONTAINS L0-21's
    stability clause as the estimate-class license condition —
    strictly stronger than both fix shapes, a-fortiori claim sound;
    the [REV2-r3-3](b) "until measured" sentence is correctly READ
    under the clause (in-place retention per the file's READ-AS
    protocol). The block's final sentence closes grammatically at
    :956 — the J-1 splice clobbered ONLY the "## 2.3" header + the
    exhibit lead-in, confirming VERDICT_r22f RES-CAP-6's
    content-intact adjudication; the landing repair prescribed there
    suffices.
(e) [REV2-r4-5](a)-(f) all verified PRESENT in the printed (vi) row
    (:1482) exactly as described, superseded fragments quoted; the
    row's honesty spine (no number at any grade, none from the
    carrier alone, brief-:126 sentence) intact.
(f) §13 verified: counts 2 BREAKs / 1 REPAIR / 2 AMENDMENTS / 5 NOTEs
    match the three round-4 files' machine summaries (L0 1/1/1/1,
    L1 0/0/0/2, L2 1/0/1/2); joint-resolution declarations match the
    fix sites; the "4 at-site functional-identity pointers" line
    reads correctly as {condition (1), (T), (C), (F)} with the (D)
    pointer listed separately.
(g) OUT-OF-SCOPE observations (NOTE only, no action this window):
    (i) delta's own deriver leg (3) (M-RED gradient measurement,
    round-1 text) shares the E5-L1-2 blindness limbs (probe part B
    shows sampled delta = 0 with a real shift) — retro-propagation
    candidate for the escalated-minor/M-RED windows; (ii)
    VERDICT_blocco2 :62-64's dry-status parenthetical "L0: 1 BREAK +
    1 REPAIR" omits L0's amendment (harmless — dry=false and the
    census 66 are unaffected); (iii) the GAP FLAG at :1682-1684
    quotes the BRIEF's own "mu = measured engine curvature" wording —
    historical process text, does not land, no touch owed.

==============================================================================
## PAPERS NEEDED

NONE for this refutation. (All findings close on the delta text, the
round-4 files, and the probe of this window; no procurement would
change any finding above.)

## MACHINE SUMMARY (targeted r4-delta pass, lens L1)

breaks = 0
repairs = 2 (E5-L1-1 identity-carriage completeness; E5-L1-5 R-17/R-14
  decider specification)
amendments = 3 (E5-L1-2 leg-(3) measurement class; E5-L1-3 H-G6
  existence/typing/positivity guards; E5-L1-4 mu symbol split at
  landing)
notes = 2 (E5-L1-6 R-14 parenthetical hygiene; E5-L1-7 verified-green
  ledger incl. out-of-scope observations)
probe: esc_probe_r4delta_lh_leg3_blindness.py — RUN, ALL ASSERTS PASS
  (A: directional L_H blindness, 100x violation sustained under every
  sweep refinement; B: sub-sample-width curvature spike, sampled gaps
  identically zero at two refinement levels vs macroscopic shift;
  C: R-17 clause passes on the annulus of record with form-(T) bound
  0 vs shift 2). CT-6 clean; derived tolerances.
core_moves_of_the_delta: SUSTAINED (no BREAK; the [REV2-r4-1/2/3]
  repairs are sound as far as they reach — the findings above are
  completeness/carriage/class-label defects, all with named one-clause
  fix shapes; none label-inflates any §1 grade).
escalation_note_for_the_judge: per the E-1..E-4 precedent the named
  fix shapes above are INPUTS, not adopted text; the M0 landing of
  §2.2-bis and the (vi) row should carry them (or a declared
  residue line) before the "round-4 delta unrefereed" declared line
  is retired.
