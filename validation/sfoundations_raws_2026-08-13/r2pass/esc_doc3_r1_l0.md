# ESCALATION REFUTATION — DOC-3 r3 repair text, until-dry ROUND 1, lens l0

Lens: hyperbolic-systems / functional-analytic rigor. Date: 2026-08-18.
Target: `validation/sfoundations_raws_2026-08-13/phaseD_L4_implies_R1.md`,
ATTACK SCOPE STRICTLY = the r3 escalation-repair text of record — the E-4
repair for leg 14 (Proposition 1'': revision-log r3 block lines ~113-131;
Section 1.6 r3 passages: (D-coll), (H-UP-fam), Claim, rigor/label block,
retraction block + grounds, two-face proof STEPs 1-3 + UNION,
"why this does not prove too much", Status of (H-UP-fam), r3 mid-face
falsifier leg) and the A-2 amendment for leg 17 (Remark 1.5.5, lines
~531-548), plus the r3 consumer updates (3.4(3)(a) ~1297-1299, Section 5
clause (i) ~1561-1565, register row 1' ~1612, NG-9 row ~1668).

Specs consumed: `r2pass/VERDICT_r2pass.md` §2.1 (L0-7/L1-7 SUSTAINED-BREAKS,
L1-8 SUSTAINED-AMENDMENT), §3 (A-2), §4(c) (E-4 escalation spec), §5
(falsifiers, incl. the proves-too-much test). Full objection texts consumed:
`r2pass/refute_r2batch_l0.md` L0-7 (lines 483-534),
`r2pass/refute_r2batch_l1.md` L1-7 (475-522) and L1-8 (567-605).

DEDUP DECLARATION: no finding below re-raises a dispositioned objection.
L0-7/L1-7/L1-8 are engaged ONLY through discharge verification (§1); every
objection in §2 targets r3-NEW text (the restated Claim, the r3 proof, the
r3 honesty paragraph, the r3 falsifier leg, (D-coll)) with zero prior
adversarial coverage. No disposition is attacked as failed.

==============================================================================
## §1 DISCHARGE VERIFICATION (the repairs vs the sustained objections)

**E-4 / defect (a) (quantifier order) — DISCHARGED, verified at pen grade.**
The r3 display `eps_1 := d_0 / (2 lambda_max) > 0` is a constant of the
(D-coll) geometry and the collar base state alone: it depends on NO
exhausting subdomain. I re-ran the Step-1 window arithmetic: for
t in (t*, t* + eps_1], lambda_max (t - t*) <= d_0/2 < d_0, so R with
lambda_max (t - t*) < R < d_0 exists; the frustum's time-t section has
radius R - lambda_max (t - t*) > 0 and contains x_0. The eps_1(Omega_int')
degeneracy of the retracted proof has no analogue: no compactly-contained
exhaustion appears anywhere in the r3 argument. CHECK.

**E-4 / defect (b) (distance zero / trace ON the source face) — DISCHARGED,
verified.** The only trace the r3 proof ever CONCLUDES is on Gamma_mid — an
interior surface of C_h at fixed Euclidean distance >= d_0 > 0 from BOTH
data-carrying faces (Gamma_in^coll and Gamma_I) by (D-coll) — and it is
delivered by Lemma 1.4 (a THEOREM of the document, leg 13 CONFIRMED,
untouched by r3), evaluated at interior points of the frustum. No step
evaluates a finite-speed conclusion on a face at distance zero from itself.
The circular trace-feed is structurally absent: Step 2's input (Gamma_mid
trace) is produced by Step 1 from zero bulk data, not by the interior
problem; Step 3's input is the same Step-1 product, not a collar output.
CHECK.

**E-4 / construction and route conformance — CHECK.** The proof written is
the construction of the spec ("Lemma 1.4 frusta to the mid-collar face +
Theorem 1' on the half collar + (H-UP) on the enlarged interior"); the
(H-UP) restatement is the family-of-collar-depths form = route (r-b) of
L1-7 = L0-7's named route, declared in-text; route (r-a) declared NOT
consumed — verified: no trace-level-determinism clause appears in
(H-UP-fam). The label discipline is correctly conservative: SCHEMA per
J-r2p-1 retained in Section 1.6, 3.4(3)(a), Section 5(i), register row 1',
and NG-9, with restoration pinned to the E-4 adjudication "no earlier and
by no other channel". The finite-speed clause is genuinely gone from the
consumed hypothesis and its burden genuinely sits on proved Lemma 1.4.

**E-4 / proves-too-much test — PASSES SUBSTANTIVELY** (the derivation does
not prove uniqueness for a bare transmission coupling; my independent
verification is exactly the construction in ESC-L0-3 below — the exclusion
is real, but the printed paragraph attributes it to the wrong step:
amendment, not failure of discharge).

**A-2 (leg 17) — DISCHARGED, verified.** The r2 "acoustic eigenprojectors
degenerate (1/c factors against closing spectral gaps)" mechanism is
replaced by the sign-classification jump of the incoming/outgoing split;
the retired parenthetical is annotated of record (house never-erase
discipline); conclusion and scoping are unchanged, as the spec requires. I
re-checked the replacement mechanism independently: at u-bar.n in
{0, -c-bar} with c-bar > 0 the distinct-eigenvalue separations are bounded
below by c-bar and Lemma 0.2's eigenvectors (r_-/+ = (rho, -/+ c n,
rho c^2), entropy and shear modes) contain u-bar.n nowhere — the
eigenstructure is regular; what is discontinuous/ill-defined is the
subspace-valued incoming-modes map (incoming count 4 -> 1 across
{u-bar.n = 0}, 4 -> 5 across {u-bar.n = -c-bar}, undefined on the loci).
CHECK.

**Residue:** the discharges above hold; the findings of §2 are
hypothesis-accounting and spec-precision defects OF THE NEW TEXT. None
re-opens L0-7(a)/(b) or L1-8 at their original severity.

==============================================================================
## §2 OBJECTIONS (r3-new text; verbatim quote + attack + class)

------------------------------------------------------------------------------
**ESC-L0-1 — class REPAIR-NEEDED. The bootstrap's maximality engine
consumes an INTERIOR solution-class/time-continuity hypothesis that the
restated Claim nowhere states.**

Quote (Section 1.6, r3 proof head and Step 3):
> "t* := sup{ t in [0, T_f] : U == 0 on Omega_up x [0, t] } (well-defined;
> the set contains t = 0 by the initial condition and continuity — this
> much of the r2 argument stands). [...] Suppose t* < T_f; by continuity
> U(., t*) = 0 on Omega_up."
and (STEP 3): "the two solutions have the same initial data at t*
(U(., t*) = 0)".

Attack (derivation level). "By continuity ... on Omega_up" is hypothesized
NOWHERE for the device data class. The Claim's hypothesis set is exactly
"Theorem 1''s hypotheses on the collar C_h, (D-coll), and (H-UP-fam)":
(H1.4) (C^1 solutions) is consumed collar-only BY DESIGN — for the S1
device class global C^1 of the perturbation fails exactly as (H1.1) does,
which is the document's own vacuousness argument for Theorem 1 — and
(H-UP-fam) as printed is a bare uniqueness property that names NO function
class, so neither time-continuity of the interior restriction nor the
existence of an a.e. t*-slice follows from it. The gap is load-bearing at
two places: (i) the left-closedness of {t : U == 0 on [0, t]} and the
conclusion U(., t*) = 0 on the INTERIOR (on the collar, (H1.4)-on-C_h
supplies it; on Omega_int^{h/2} nothing does); (ii) Step 3's consumption of
(H-UP-fam) "with the same initial data ... at a time t_0 = t*" presupposes
the restrictions are objects of the class over which the hypothesis
quantifies. Without a stated class the maximality argument does not start.
Repair: one hypothesis line — e.g. U^(i) in C([0, T_f]; L^2_loc(Omega_up))
with the Omega_int-restrictions in the class over which (H-UP-fam)
quantifies — or fold the class into (H-UP-fam)'s statement (whose precise
formulation is NG-9's burden anyway; then the Claim must SAY it delegates
the class). Not BREAKS: the deductive skeleton is unaffected once the
clause is written; this is the same grade the judge of record gave the
missing-named-condition defect L1-2 (SUSTAINED-REPAIR).

------------------------------------------------------------------------------
**ESC-L0-2 — class REPAIR-NEEDED. The restated Claim DROPPED the
same-forcing clause that Theorem 1's template carries; Step 1 consumes it
explicitly.**

Quote (Section 1.6, r3 Claim):
> "Then two solutions with the same data on Omega_up (initial data +
> Gamma_in data/BC), differing arbitrarily downstream of Gamma_I, coincide
> on Omega_up x [0, T_f]."
against (STEP 1): "U is a C^1 solution of the homogeneous (LIN-U) on C_h
((H1.4); the forcings cancel on Omega_up)".

Attack (derivation level). Theorem 1's claim pins the convention in
parentheses: "two solutions of the linearized Euler system (same base
state, same forcing f on Omega_up)". The r3 restatement enumerates the
shared data as "initial data + Gamma_in data/BC" — forcing absent — while
its own Step 1 consumes exactly forcing-cancellation on Omega_up. As
literally read the Claim is refuted in one line: take U^(1), U^(2) with
identical initial and Gamma_in data and forcings differing on the collar;
then U solves an INHOMOGENEOUS system and U != 0 on Omega_up generically.
The same silent convention sits inside (H-UP-fam) ("two solutions with the
same initial data ..., the same Gamma_in data/BC, and the same trace ...
coincide" — same forcing unstated for "the linearized interior problem").
Repair: restore "and the same forcing f on Omega_up" to the Claim
(mirroring Theorem 1) and pin the forcing convention in (H-UP-fam) — or
restate both for the homogeneous difference problem. Class REPAIR, not
BREAKS: unlike the D.18 first iff there is no in-document witness against
the intended reading — the Theorem-1 template two subsections up supplies
it anaphorically — but the hypothesis line of record must carry the clause;
this document's r2/r3 history is precisely a history of consumed-but-
unstated hypotheses.

------------------------------------------------------------------------------
**ESC-L0-3 — class AMENDMENT. The "why this does not prove too much"
paragraph misattributes the exclusion mechanism to Step 1's unavailability;
the load-bearing exclusion is Step 3's domain enlargement.**

Quote (Section 1.6):
> "For a bare transmission coupling of two subdomains across a single face
> with no transmission condition, Step 1 is unavailable: there is no
> OVERLAP region with certified regularity on which a proved finite-speed
> lemma can carry zero data from one face to a SECOND face at positive
> distance. The two-face argument consumes exactly the two structural
> assets a bare coupling lacks: the W^{1,infinity} collar overlap ..."

Attack (derivation level; this is the judge's own §5 test run at its
sharpest instance). Take the strengthened bare coupling: two subdomains
joined at Gamma_in^coll with NO transmission condition, whose collar-side
region happens to be W^{1,infinity} with a margin outflow far face, and
whose interior-side hypothesis is uniqueness-given-face-trace ON ITS OWN
SIDE (domain stopping AT the coupling face — the honest bare-coupling
analogue of the r2 (H-UP)). For this instance Steps 1 AND 2 run verbatim:
Lemma 1.4 lives strictly inside the collar side and consumes nothing about
the coupling; MID-TRACE and the half-collar conclusion are TRUE (the
entering signal genuinely needs > eps_1 to reach Gamma_mid). "Step 1 is
unavailable" is therefore false for this instance. What fails — and what
actually blocks proves-too-much — is STEP 3: (H-UP-fam) at depth h/2
places the coupling face Gamma_in^coll in the INTERIOR of its domain
Omega_int^{h/2}, so the hypothesis quantifies only over pairs that solve
the PDE ACROSS the face; the bare coupling's glued pairs are not such
objects, and its own-side hypothesis is not (H-UP-fam). The cross-face
solvability encoded by the enlargement IS the transmission content a bare
coupling lacks. Conclusion of the paragraph TRUE (verified through exactly
this construction); printed mechanism wrong for the sharpest test case —
the same right-conclusion/wrong-mechanism class the judge sustained as
L1-8. Fix: one sentence naming the enlargement (coupling face interior to
the (H-UP-fam) domain) as the operative exclusion, with the overlap and
outflow face as the assets that make Steps 1-2 run.

------------------------------------------------------------------------------
**ESC-L0-4 — class AMENDMENT. r3 mid-face falsifier leg: "the upstream
field" is ambiguous in a paragraph that also uses "upstream-of-collar";
under the weaker reading the leg fires with a WRONG attribution.**

Quote (Section 1.6, falsifier):
> "probe the trace on the mid-collar face Gamma_mid over a window
> [t_p, t_p + d_0/(2 lambda_max)] following any instant t_p at which the
> upstream field is at the scheme bound: the mid-face trace must stay at
> the scheme bound over that FIXED window (the (MID-TRACE) step); a
> mid-face signal growing inside the window while the collar regularity
> monitors are green rejects Step 1's wiring (Lemma 1.4 on the collar),
> independently of (H-UP-fam)."

Attack (executor level — the class the judge sustained as L1-5). The same
paragraph's first leg watches "the upstream-of-collar response"
(= Omega_up \ C_h). If an executor reads "the upstream field" the same
way, the premise leaves the COLLAR field unconstrained at t_p: a pre-t_p
leak through Gamma_I (a Theorem-1'-wiring defect, invisible to the first
leg) contaminates the collar and produces in-window mid-face growth — the
leg fires while Step 1's wiring (Lemma 1.4) is sound: real rejection,
wrong printed attribution. The window logic is exact precisely under the
Omega_up-INCLUSIVE reading: with every point within distance d_0/2 of
Gamma_mid at the bound at t_p, any contaminant must enter through a face
at distance >= d_0 and travel at <= lambda_max, arriving no earlier than
d_0/lambda_max = 2x the window — so ANY in-window growth localizes to a
cone/speed violation in the collar. Fix: replace "the upstream field" with
"the field on all of Omega_up (collar included)" (and mirror in register
row 1''s falsifier cell, which inherits the ambiguity in condensed form).

------------------------------------------------------------------------------
**ESC-L0-5 — class AMENDMENT. The proof window can overrun [0, T_f].**

Quote (Section 1.6, STEP 1 and UNION):
> "Fix t in (t*, t* + eps_1] ..." / "U == 0 on Omega_up x [0, t* + eps_1]
> with the FIXED eps_1 above — contradicting the maximality of t*. Hence
> t* = T_f."

Attack. For t* in (T_f - eps_1, T_f) the window (t*, t* + eps_1] leaves
[0, T_f], where the solutions and every hypothesis are undefined; as
printed, Steps 1-3 are applied at times where there is no object. Every
occurrence must read eps_1' := min(eps_1, T_f - t*) (> 0), and the closing
line becomes: U == 0 on Omega_up x [0, min(t* + eps_1, T_f)], which
contradicts t* < T_f in both cases (either sup-violation at t* + eps_1' or
directly t* = T_f). One-token fix; no content moves.

------------------------------------------------------------------------------
**ESC-L0-6 — class AMENDMENT. STEP 2's hypothesis checklist omits (H1.4)
on C_{h/2}.**

Quote (Section 1.6, STEP 2):
> "its hypotheses hold — (H1.1') + (G3)-box on C_{h/2} subset C_h; (H1.2)
> on Gamma_w intersect del C_{h/2}; (H1.3) on Gamma_I; (D'') for C_{h/2}
> per (D-coll)."

Attack. Theorem 1' consumes FOUR numbered hypotheses — (H1.1'), (H1.2),
(H1.3), (H1.4) — plus (D''); the r3 verification list enumerates all but
(H1.4). It holds by restriction ((H1.4) on C_h restricts to C_{h/2}), so
nothing is false; but an escalation repair whose entire reason for
existence is hypothesis accounting must enumerate completely — this is the
verification list the E-4 adjudicator will re-run. Add "(H1.4) on C_{h/2}
by restriction".

------------------------------------------------------------------------------
**ESC-L0-7 — class AMENDMENT. (D-coll)/Status (a): the Lipschitz property
of the interior domains Omega_int^s is consumed but never stipulated.**

Quote ((D-coll)): "with C_{h/2} a Lipschitz domain per (D'') and with the
uniform distance bound d_0 := dist(Gamma_mid, Gamma_in^coll union
Gamma_I) > 0." and (Status of (H-UP-fam), case (a)): "on Omega_int^s the
energy identity (EI) closes with the Gamma^coll_s boundary term killed
pointwise by the ZERO FULL TRACE of the difference".

Attack. Case (a)'s in-document-theorem claim runs (EI) on Omega_int^s,
which requires that domain to admit the divergence-theorem package — the
document's own (D'') discipline. (D-coll) stipulates Lipschitz-ness for
C_{h/2} but NOT for the complement Omega_int^{h/2} = Omega_up \
closure(C_{h/2}); a set difference of Lipschitz domains is not
automatically Lipschitz (it fails where Gamma_mid meets Gamma_w
tangentially). Load-bearing only in case (a) (case (b) delegates the whole
problem class to NG-9), so: add to (D-coll) "and Omega_int^{h/2} a
Lipschitz domain per (D'')" — or the transversality of Gamma_mid to
Gamma_w, from which it follows; same fix inherited by the family clause
("any fixed s in (0, h) with its d_0(s) > 0 runs verbatim" presumes the
same property at depth s).

==============================================================================
## §3 CONFIRMED passages (strongest attack tried, each)

**C-1 — (H-UP-fam) statement + "two deltas" honesty block + route
declaration: CONFIRMED** (modulo ESC-L0-1/2's class/forcing clauses, which
are charged to the Claim). Attacks tried: (α) family-vs-single-depth
strength inflation — disarmed in-text (the parenthetical declares only
s = h/2 consumed and why the family is stated); (β) the "S1-class burden
... exactly that of the r2 (H-UP)" claim — holds: the added strip is
W^{1,infinity} territory where uniqueness-given-full-face-trace is routine
energy content, and the interior front/slip-line set is identical; note
the enlarged domain additionally requires solvability ACROSS Gamma_in^coll
(regular there), which adds no S1 burden; (γ) hunt for a smuggled
trace-level-determinism (route r-a) clause — none found.

**C-2 — STEP 1 (the core discharge): CONFIRMED.** Attacks tried and
failed: uniformity re-check (eps_1 is a (D-coll)-geometry constant — the
exhaustion degeneracy has no analogue); Euclidean-vs-intrinsic distance in
a wrapped/non-convex geometry (harmless: Lemma 1.4 is applied with
O = C_h and intersects everything with O, and the EUCLIDEAN bound R < d_0
keeps B(x_0, R) off Gamma_in^coll and Gamma_I regardless of connectivity
of B ∩ C_h); rim points x_0 near Gamma_w (wall portions are admissible
frustum boundary in Lemma 1.4, as the text notes); time-dependent base
(the r3 lambda_max takes sup over C_h x [0, T_f], at least as strong as
Lemma 1.4's display); section-radius positivity at the window endpoint
(R - lambda_max(t - t*) > 0 by construction). The concluded object is a
trace on an INTERIOR surface at distance >= d_0 from every data-carrying
face — defect (b)'s structure is absent.

**C-3 — STEP 3 + UNION wiring: CONFIRMED** given ESC-L0-1/5. The
consumption of (H-UP-fam) at s = h/2 is exact: Gamma^coll_{h/2} =
Gamma_mid by (D-coll)'s splitting clause; zero difference-trace = same
trace; the decomposition Omega_int^{h/2} ∪ Gamma_mid ∪ C_{h/2} covers
Omega_up. Attack tried: whether MID-TRACE covers the closed window
(t = t* is supplied by (H1.4)-continuity on closure(C_h)); whether STEP 3
needs any sign information on Gamma_mid (it does not — the hypothesis is
trace-matching, not dissipativity, exactly as Status (a)'s pointwise-kill
shows).

**C-4 — retraction block + retraction grounds: CONFIRMED.** Checked line
by line against L0-7 (refute_r2batch_l0.md 493-517) and L1-7
(refute_r2batch_l1.md 485-522): the quoted r2 proof is verbatim; grounds
(a)/(b) faithfully transcribe the two defects including the
proves-too-much sentence; the never-erase discipline is observed. Attack
tried: hunting a residual consumer of the retracted step — none found.

**C-5 — revision-log r3 disposition table + consumer updates: CONFIRMED.**
Cross-checked mutually and against the verdict: SCHEMA-per-J-r2p-1 carried
consistently in Section 1.6, 3.4(3)(a), Section 5 clause (i), register row
1', NG-9; restoration pinned to the E-4 adjudication only; legs 12/13
verified genuinely untouched (no r3 marker in Theorem 1' or Lemma 1.4
text); NG-9's r3 delta statement matches the (H-UP-fam) text. Attack
tried: grep for any consumer still citing "THEOREM modulo (H-UP)"
unqualified — none.

**C-6 — leg-17 A-2 text (Remark 1.5.5): CONFIRMED — the amendment is
delivered per spec and the new mechanism is correct.** Strongest attacks
tried: (α) "keep mutual spectral gaps equal to c-bar" — pairwise, the
extreme pair (u.n - c, u.n + c) has gap 2c-bar; read as
distinct-eigenvalue separation (the operative quantity for projector
regularity, all separations >= c-bar with adjacent pairs = c-bar) the
sentence is exact, it transcribes judge act (vii), and no consumer uses
the literal "equal"; attack fails to find load-bearing falsehood. (β) The
discontinuity sentence names only {u-bar.n = 0} and {u-bar.n = -c-bar},
omitting {u-bar.n = +c-bar} — immaterial: the example's scoping sentence
excludes all three loci, and on an inflow face the motivating class meets
only the two named. (γ) Eigenvector-regularity claim re-checked against
Lemma 0.2 (acoustic eigenvectors (rho, -/+ c n, rho c^2), entropy/shear
modes: none contains u-bar.n) — holds. (δ) Conclusion/scoping unchanged as
the spec demands — verified against the r2 text structure (the
constant-multiplicity scoping and the "no consumer at a characteristic
inflow point" sentence are intact).

==============================================================================
## §4 Summary table

| ID | Passage | Class |
|---|---|---|
| ESC-L0-1 | proof head "by continuity ... on Omega_up" + STEP 3 initial slice | REPAIR-NEEDED |
| ESC-L0-2 | restated Claim (forcing clause dropped; Step 1 consumes it) | REPAIR-NEEDED |
| ESC-L0-3 | "why this does not prove too much" mechanism attribution | AMENDMENT |
| ESC-L0-4 | r3 mid-face falsifier leg, "the upstream field" | AMENDMENT |
| ESC-L0-5 | window overrun of [0, T_f] | AMENDMENT |
| ESC-L0-6 | STEP 2 checklist omits (H1.4) | AMENDMENT |
| ESC-L0-7 | (D-coll)/Status (a): Omega_int^s Lipschitz unstipulated | AMENDMENT |

Totals: 7 objections = 0 BREAKS-THE-LEG + 2 REPAIR-NEEDED + 5 AMENDMENT.
Confirmed passages: C-1..C-6 (each with strongest attack recorded).
Discharge verdicts (§1): E-4 defects (a) and (b) DISCHARGED; proves-too-much
test passes substantively (ESC-L0-3 corrects the attribution); A-2
DISCHARGED. Nothing here re-opens L0-7/L1-7/L1-8 at original severity, and
no finding contests the SCHEMA label discipline (which is correct as
printed).

## §5 Self-falsifiers (what kills each finding)

- ESC-L0-1 dies if a stated hypothesis of the r3 Claim (or a clause of
  (H-UP-fam) as printed) is exhibited from which time-continuity of the
  interior restriction and the t*-slice property follow for the S1 device
  class; note (H1.4) cannot serve — it is consumed "on the collar C_h"
  only, and its global form fails for the device class by the document's
  own Section-1.6 vacuousness argument.
- ESC-L0-2 dies if "data" is shown DEFINED in this document to include
  forcing, or if the Claim's "two solutions" is shown to bind to Theorem
  1's parenthetical (same forcing) by an explicit cross-reference rather
  than anaphora.
- ESC-L0-3 dies if for EVERY coupling with no transmission condition
  Step 1 is genuinely unavailable — i.e., if the strengthened bare
  coupling (W^{1,infinity} collar side + outflow far face + own-side
  uniqueness) is shown out of the class the paragraph's "bare transmission
  coupling" quantifies over AND the paragraph is shown to say so.
- ESC-L0-4 dies if "the upstream field" is shown pinned to Omega_up
  (collar included) by the document's notation of record (a definition,
  not usage precedent — usage in the same paragraph points both ways).
- ESC-L0-5 dies if the window (t*, t* + eps_1] is shown to stay in
  [0, T_f] under the printed hypotheses (it is not: t* < T_f is the only
  bound in force).
- ESC-L0-6/7 die if the omitted items ((H1.4) on C_{h/2}; Lipschitz
  Omega_int^s) are shown stated elsewhere in the r3 text (grep found
  neither).

END — machine summary: {objections: 7, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc3_r1_l0.md}
