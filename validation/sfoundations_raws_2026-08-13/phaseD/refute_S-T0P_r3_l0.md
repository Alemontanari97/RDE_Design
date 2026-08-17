# ADVERSARIAL REFUTATION — [S-T0P]/[T-T0P] proof document, ROUND 3, LENS 0
# (functional-analytic rigor: spaces, operators, traces, compactness,
#  quantifiers, rigor-label algebra, falsifier rejection power, absence)

Target: validation/sfoundations_raws_2026-08-13/phaseD/phaseD_stop_proof.md
(revision 1, post round-1 disposition per its §10).

ORCHESTRATION NOTE (file naming, of record): the launching brief named this
pass "Round 1" and directed output to refute_S-T0P_r1_l0.md. That file
EXISTS, is CONSUMED of record by the target's §10 disposition table
(item-by-item, by F-number), and overwriting it would corrupt the audit
trail the document cites. Two further round-2 refutations
(refute_S-T0P_r2_l0.md, 11 findings; refute_S-T0P_r2_l1.md, 9 findings)
exist on disk, POSTDATE the revision-1 text, and are NOT yet consumed. This
pass is therefore written as ROUND 3, LENS 0, to the present file, per the
append-only artifact discipline (S-ORDINE R7/SR); the launch-brief label is
recorded here as stale. DEDUP CONTRACT: every finding below is checked NEW
against all 22 round-1 items (via the §10 disposition, which is accurate)
AND all 20 round-2 items (both files read in full this pass). Where a
finding extends a round-2 item, the extension is explicitly delimited.

STANDING CAVEAT FOR THE AUTHOR AGENT: the round-2 files are unconsumed;
nothing below repeats them, so revision 2 must consume THREE files
(r2_l0, r2_l1, r3_l0).

==============================================================================
## A. RE-VERIFIED SOUND THIS ROUND (independent re-derivation; no objection)

 A1. [L-XWALL3] 5-component slip solve, re-derived from scratch:
     d(rho u) = 0; energy row => dH = 0; x-mom => (rho u)du + dp = n_x p';
     transverse rows => v dv + w dw = (v n_y + w n_z) p'/(rho u); Gibbs
     expansion of dH = 0 collapses to theta dS = -p'(u.n)/(rho u) = 0 at
     slip. Confirmed at abstract EOS, every g. (State-level; the
     r2-F2/r2-F5 application objections stand and are not repeated.)
 A2. [L-XC3D] (KEY), re-derived: along the frozen-M path, dp = -rho u du
     from the m2 relation makes dp/rho + u du = 0 identically, so
     theta dS = -dbeta in one line; S even in eps, S'(0) = 0, h_ww =
     -m1 g' S''(0) = g'/(theta rho u) > 0. The parity zeros of the mixed
     m_w entries confirmed. No new objection.
 A3. [L-COMPAT]: D_M eta = D_W Q_x (A_x)^{-1} = D_W E A_x (A_x)^{-1}
     = D_W E confirmed; Step-1 gradient-arbitrariness device sound.
 A4. [L-XSON3] parity/rotation factorization det J_5 = (rho u) det J_4
     at w = 0: confirmed entry-wise.
 A5. [L-STD] main chain (mollify in t, Fubini, countable-dense orbit,
     continuity, undo Phi): sound modulo the r2-F11 residues (closedness
     of N, eps_n bookkeeping) — not repeated.
 A6. (EI-x) as a class condition is the PHYSICAL entropy inequality:
     d_x eta + d_y q_y + d_z q_z + d_t q_t is literally the same
     distribution as d_t(-rho g) + div(-rho u g) regrouped; H7' therefore
     imposes no exotic admissibility — a point in the document's favor,
     recorded because no lens had said it.
 A7. Per-front jump sign: with S nondecreasing along particle paths the
     inequality -|N_sp| m [g(S)] <= 0 holds for EITHER sign of m with
     |m| >= m_min; the H6' two-sided clause is consistent.
 A8. [P-HB2] linearity + Fourier-line constraint; [P-HB3](i') case split:
     group algebra sound (modulo the r2_l0-F5 definitional/measure
     residues — not repeated).

==============================================================================
## B. NEW OBJECTIONS (round 3; none repeats a round-1 or round-2 item)

------------------------------------------------------------------------------
### r3-F1 — UNSTATED LOAD-BEARING INCLUSION H6' subset H7': the §2.3/§5
### assembly uses S1 elements AS COMPETITORS of [T-T0P-U] without ever
### establishing that they belong to the competitor class

CLAIM ATTACKED: §2.3 [T-T0P-E] proof ("By the S1-anchored uniqueness
property applied to the pair (q, g_tau q) — both S1"); §5 [T-T0P] proof
("By [T-T0P-U], any element of C(s) coincides with any S1 element: the
class has the S1-anchored uniqueness property").

DEFECT. [T-T0P-U] is a strong-vs-weak statement: strong side U per H6'-A,
competitor V per H7'/H8'. To derive the S1-anchored uniqueness property
from it, the §5 proof must apply it to pairs in which the SECOND member is
an S1 element (the pair (q, g_tau q) of §2.3; the pair (element, S1
element) of §5). That application is licit only if every S1 element IS an
H7' competitor, i.e. only under the inclusion

    H6' (S1 class)  subset  H7' (weak competitor class),

which requires, per the H7' definition: (a) the field satisfies (EI-x) in
D' for g = S on the slab; (b) it carries the [C-XBVP](b) normal-trace
package; (c) (via H8', already binding classwide) T-periodicity. The
document NEVER states or proves this inclusion. It is not vacuous:
 - On stratum (A) it is true and one-line (a C^1 field satisfies the
   equality case of (EI-x) by §3; a C^1 field on a per-sector C^{1,1}
   domain has classical strong traces, which embed in the Chen-Frid
   package) — but the line must be WRITTEN, because the THEOREM* label of
   (A) claims completeness modulo NAMED conditionals, and an unnamed
   membership lemma is a completeness defect of exactly the genus the
   document polices elsewhere.
 - On stratum (B) the inclusion is NOT free: (EI-x) for a piecewise-C^1
   field with fronts is exactly the per-front argument of §3, which is
   valid only for the H6'-admissible fronts (|m| >= m_min, G9), and the
   trace package across the front sheets needs a sentence (piecewise-C^1
   fields are BV_loc on compact subsets away from front intersections —
   finitely many transversal sheets make this true, but it is an
   argument, not a triviality).
The formal consequence as printed: §2.3's invocation "by the S1-anchored
uniqueness property applied to the pair (q, g_tau q)" is well-formed (the
property is hypothesized abstractly there — good), but §5's DERIVATION of
that property from [T-T0P-U] is a non sequitur without the inclusion:
[T-T0P-U] quantifies over H7' competitors, and an S1 element has not been
shown to be one. The gap sits precisely at the joint between the two
halves — the joint is the whole point of the document.

WHY NEW: no round-1 or round-2 item addresses the class membership of S1
elements as competitors. r2_l1-F3 is adjacent (it observes the pair is
C^1-vs-C^1 and proposes a cheaper classical route) but attacks the
conditional LOAD, not the missing membership lemma of the printed route;
r2_l0's survived-list re-verified L-EQV3's items, none of which is this
inclusion.

SEVERITY: MEDIUM (formal completeness of the headline assembly; the
repair is small but mandatory for the (A) label, and on (B) it surfaces
one more place where G9 does real work).

REPAIR: add a lemma [L-INC] (S1 subset H7'): statement, the three clauses
(a)-(c), one-paragraph proof per stratum, G9 cited on (B); cite it in §5
and in §2.3's proof line. Zero new mathematics; the (A) label becomes
honest on this axis.

------------------------------------------------------------------------------
### r3-F2 — G8 IS MINTED WITHOUT A FALSIFIER; §8's "each with owner and
### falsifier per §9" is FALSE for G8; and the pricing of G8 as a finite
### certifiable check is unsupported against the document's own
### [S-XCONV] R1 — the hull condition may be structurally infeasible

CLAIM ATTACKED: §8 registry paragraph: "NEW CONDITIONAL MINTS PROPOSED:
[C-MAJDA-3DT] (G3), [C-XINJ] (G7), [C-XBVP](a') (G8) — each with owner
and falsifier per §9"; §9/G8 row; the r2-F1/F4-adjacent pricing of G7/G8
as "certifiable finite checks".

DEFECT (three layers, all new).
 (a) MISSING FALSIFIER: the G8 ledger row contains discharge routes
     (r1-r3), an inheritance note, and an owner — and NO falsifier. G3's
     row has one (the bordered Lopatinskii determinant); G7's lives in
     L-XREC's falsifier line. For G8 nothing in §9 (row or falsifier
     table) names a test that could reject the hull/segment condition.
     One exists and is cheap to state: exhibit two K-branch states
     M_U, M_V in K_M whose segment leaves the branch or on whose segment
     the Hessian of eta loses definiteness (numeric line-search over the
     certified box — an [X-T0P]-class check). The §8 sentence quoted
     above is therefore FALSE as printed — an accounting defect of the
     exact class the round-1 l0-F10 disposition claims was FIXED.
 (b) FEASIBILITY UNPRICED: the document prices G8 (via r1) as a finite
     interval-certificate extension, and the unconsumed r2-F1/r2_l1-F4
     lean on that pricing to argue stratum (A) could keep THEOREM* after
     an in-window registration. But the document's OWN cited result
     [S-XCONV] R1 (subsonic indefiniteness, 60/60; "no convex extension
     of this eta exists across the sonic line") makes it a live
     possibility that conv(K_M) MEETS the sonic fold — in which case NO
     convex M-superset of K_M staying on the branch exists AT ALL, route
     r1 is infeasible in principle (not "not yet run"), the condition as
     minted is FALSE for the standing box, and the only surviving routes
     change the proof architecture (r2: W-variable Dafermos device) or
     the certificate object (r3: pair certificate). Whether conv(K_M)
     stays supersonic-side is a DECIDABLE, CHEAP geometric check on the
     certified box (min of u - c over the hull, computable by interval
     arithmetic on segment endpoints in M-space) — it is neither named
     as a feasibility gate for r1 nor scheduled. Under the
     doubts-to-convergence discipline, "r1 might be dead on arrival" is
     a named doubt with a named cheap experiment, and it is unscheduled.
 (c) ABSENCE (literature route ignored at the exact pressure point):
     the classical resolution of segment-vs-pointwise convexity for
     Euler entropies is that E = -rho g(S) is GLOBALLY convex in the
     CONSERVATIVE variables W on the physical region under named
     thermodynamic-stability conditions (Harten's entropy-family
     analysis; Godlewski-Raviart's convexity discussion: conditions on
     g', g'' and c_v). Global convexity in W kills the hull problem at
     its root (all comparison segments in W-space stay in the convex
     physical region), which is precisely why the document's own route
     r2 works — but the document presents r2 as one of three
     interchangeable bookkeeping options and cites NO source for the
     W-convexity fact it would consume, nor adds a novelty/technology
     query for it. The §9 query list has no entry of the form "entropy
     convexity conservative variables Euler thermodynamic stability".

WHY NEW: G8 was minted in revision 1; round-2 attacked its LABEL algebra
(r2-F1, r2_l1-F4: registration asymmetry) — not the missing falsifier,
not the feasibility question, not the W-convexity literature absence.

SEVERITY: MEDIUM-HIGH. (a) is a flat internal falsehood on the R5 axis;
(b) undercuts the repair route both unconsumed r2 verdicts rely on —
if the feasibility check fails, "REPAIRABLE by registering G8" is wrong
and stratum (A) needs the r2-route re-architecture before any THEOREM*;
(c) is the standard route the field would use and its absence has
already cost the document one wrong pricing narrative.

REPAIR: add the G8 falsifier line (segment check as in (a)); add the
hull-feasibility gate as the FIRST item of route r1 with the interval
check named; cite the W-convexity classical condition inside route r2
and add the query; re-issue the §8 sentence truthfully.

------------------------------------------------------------------------------
### r3-F3 — G5's PRICING OMITS ITS DEPENDENCY ON G8: the cone-localized
### lift is declared "bookkeeping of the same class as [C-XBVP](b)" while
### its stated mechanism consumes the segment estimates

CLAIM ATTACKED: §4 REMARK (lifting H8'): "the cone-slope condition
|relative flux| <= lambda_K eta(V|U) available on K from the same c_K,
C'_K constants ... This is bookkeeping of the same class as [C-XBVP](b),
named here and left as G5"; §9/G5 row ("standard technology, declared
not written").

DEFECT. The constants c_K, C'_K are the QUADRATIC SANDWICH constants,
which the revision itself declares to exist only modulo [C-XBVP](a') =
G8 ("These are Taylor estimates ALONG THE SEGMENT ... the hull/segment
condition is therefore LOAD-BEARING and is the named conditional
[C-XBVP](a') = G8"). The cone-slope condition additionally needs the
RELATIVE-FLUX upper bound |q_mu(V|U)| <= lambda_K eta(V|U) for mu in
{y, z, t} — one more segment-Taylor estimate on the same unproven hull
(the relative flux is a second-order remainder of F_mu against the
second-order lower bound of eta, both along [M_U, M_V]). So the G5 lift
is NOT "of the same class as (b)" (trace bookkeeping): it inherits the
full G8 conditional, and discharging G5 before G8 is impossible by the
document's own accounting. Neither the REMARK nor the G5 ledger row
declares the G5 -> G8 dependency; the gap-graph as printed is missing an
edge, and the M0-delta instruction (§8: "G5 is the named lift") would
export the mispricing to the reference of record.

WHY NEW: round-1 l1-F2/l0-F5 created H8'/G5; round-2 attacked H8''s
discharge sentence (r2-F9, r2_l1-F8) and the classical alternative
(r2_l1-F3) — no item concerns G5's dependency structure or its "(b)-class
bookkeeping" pricing.

SEVERITY: MEDIUM-LOW (no falsehood in a proof step; a mispriced gap
with a missing declared dependency, on the axis the ledger exists for).

REPAIR: one sentence in the REMARK and one in the G5 row: "G5 consumes
the G8 segment estimates (c_K, C'_K, lambda_K); discharge order G8 before
or with G5"; propagate to the §8 delta wording.

------------------------------------------------------------------------------
### r3-F4 — FALSIFIER LINES THAT DECLARE THEMSELVES IMPOSSIBLE: [P-HB2]
### and [P-HB3](i') carry rejectors with zero rejection power as printed

CLAIM ATTACKED: §6 [P-HB2] FALSIFIER ("exhibit a one-parameter invariance
group for genuinely two-speed data (violating Fourier uniqueness) —
impossible by the proof; the checkable content is the Fourier computation
itself"); §9 falsifier table, [P-HB3](i') row ("impossible by the proof;
the case computation is the checkable content").

DEFECT. R5 requires every claim to end with a test that COULD reject it.
A falsifier whose own text declares execution "impossible by the proof"
has, by construction, zero rejection power: it can never fire, so it
tests nothing. The parenthetical redirect ("the checkable content is the
computation") gestures at the right object but names no executable
check. This is not pedantry — the document itself retired the round-0
[P-HB3] falsifier for the opposite failure (it fired on the document's
own boundary class), so the falsifier-design axis is live and audited on
these exact propositions. An executable statement-level rejector exists
for both and costs one sentence each:
 - [P-HB2]: randomized two-line data (k1, k2, OM_1 != OM_2 sampled),
   CAS/numeric sweep over (a, b) in a lattice + continuity bound,
   verifying no nontrivial (a, b) satisfies both line constraints; a
   surviving (a, b) refutes the proposition (this CAN fire if the
   Fourier-uniqueness algebra is wrong).
 - [P-HB3](i'): synthetic transition-window data (n1 -> n2 profiles),
   same sweep; a surviving one-parameter family refutes (i').
Without such lines, the two propositions are the only claims in the
document whose falsifier slots are decorative.

WHY NEW: round-1 l0-F12(c) fixed falsifier TARGETS for [T-T0P-E];
round-2 r2-F6 fixed the [T-T0P-E] falsifier's implication structure and
r2_l1-F2(c) the G3 split-falsifier — no item touches the P-HB2/HB3(i')
falsifier lines' self-declared impossibility.

SEVERITY: LOW (labels unaffected; pure R5 hygiene on two rows).

REPAIR: replace "impossible by the proof" by the executable sweep
rejectors above (symbolic/numeric, [X-T0P]-battery class).

------------------------------------------------------------------------------
### r3-F5 — GAMMA ACCOUNTING, EXTENSION (explicitly delimited against
### r2_l1-F6): the G8 discharge routes r1/r3 are THEMSELVES ideal-gas
### instance certificates, so the "single gamma-restricted ingredient"
### sentence stays false even after the G7 repair

CLAIM ATTACKED: audit line ("the ONLY ideal-gas instance dependence is
the inherited [C-XBVP](a) definiteness certificate"); §9 gamma table
entries for L-XC3D and T-T0P-U/T-T0P; G8 row routes r1/r3.

DELIMITATION: r2_l1-F6 established that [C-XINJ]/G7 is a SECOND
gamma-restricted ingredient (classical only at ideal gas; r-b needs
certified table enclosures). This finding is the THIRD instance and is
about G8, which r2_l1-F6 does not mention.

DEFECT. Routes r1 and r3 for G8 are interval certificates run over the
certified box — i.e., over the [X-IVXC] gamma = 1.4 instance (r1: "re-run
the interval certificate on the enlarged box"; r3: "interval certificate
over PAIRS" on the (M, V) box, whose reduction [T-XRED] and whose
underlying Hessian data are the ideal-gas instance). If G8 is discharged
by r1 or r3, the chain's gamma-restricted surface gains a THIRD
instance-bound certificate (or a second independent one, r2's route
being the only abstract-EOS-capable option); on the standing gas model
(gamma(T) tabulated) both further need certified interpolation
enclosures, exactly as r2_l1-F6 noted for G7/r-b — a requirement neither
r1 nor r3 states. The per-statement gamma table already fails the
binding standard after r2_l1-F6; the repair, when executed, must count
G8 as well, or the corrected sentence will be false again the moment G8
is discharged by the routes the document itself ranks first. The honest
audit-line form is: "abstract EOS modulo G1, G7's EOS condition or
instance certificate, and G8's certificate instance (route-dependent);
route r2 is the only named G8 route that keeps the chain abstract-EOS."

WHY NEW: G8's routes exist only in revision 1; r2_l1-F6's list stops at
G7; no other item touches G8's gamma status.

SEVERITY: LOW-MEDIUM (mandated-axis accounting; one-sentence repairs in
three places, but only if executed TOGETHER with the r2_l1-F6 repair —
a partial fix would mint a new falsehood).

REPAIR: as stated; add the enclosure clause to r1/r3; flag r2 as the
gamma-clean route in the G8 row.

==============================================================================
## C. ABSENCE SWEEP (this round; beyond items already filed)

 - Bounded-domain relative-entropy/weak-strong literature (relative
   entropy for hyperbolic systems WITH boundary; Christoforou-Tzavaras-
   class treatments; boundary terms in Euler weak-strong arguments):
   the natural published home for the exact (w)/(d) trace clauses the
   unconsumed r2-F2/r2-F3/r2_l1-F5 demand; not in the §9 queries.
   (Complementary to, not repeating, r2_l0-F2's characteristic-boundary
   absence: that names the IBVP regularity literature; this names the
   relative-entropy-with-boundary literature.) Query to add: "relative
   entropy weak strong uniqueness boundary hyperbolic system trace".
 - Entropy convexity in conservative variables (Harten; Godlewski-
   Raviart): consumed by r3-F2(c) above; query named there.
 No further absences found this round; the convex-integration axis
 (r1), time-periodic classical axis (r2_l1-F3), and characteristic-
 boundary axis (r2_l0-F2) already cover the main known routes.

==============================================================================
## D. VERDICT

REPAIRABLE — and visibly converging: the algebraic core (§2 group
action, §3 bricks) has now survived three independent re-derivations;
every round-3 finding is formal-completeness, ledger-accounting, or
falsifier-hygiene, none touches a computation. But the document is NOT
sound as labeled in its present revision-1 state, for the accumulated
reasons: the two unconsumed round-2 files (label asymmetry r2-F1/
r2_l1-F4; structural trace hypotheses r2-F2/F3/r2_l1-F5; the refuted
margin conjecture r2_l1-F1; the gamma undercount r2_l1-F6) plus, from
this round: the unproven load-bearing inclusion H6' subset H7' (r3-F1),
a minted conditional with no falsifier and an unpriced feasibility risk
that conditions the standard repair route (r3-F2), a missing dependency
edge G5 -> G8 (r3-F3), two zero-power falsifier rows (r3-F4), and a
third gamma-restricted ingredient (r3-F5).

Priority for revision 2: r3-F2(b) FIRST (the hull-feasibility check
decides whether the r2-F1/r2_l1-F4 "register G7/G8 in-window and keep
THEOREM*" repair is even available); then r3-F1 (one lemma, unblocks
the (A) label); the rest are sentence-level. The §8 M0 delta must not
land before r3-F1/r3-F2/r3-F5 are resolved, for the same reason the
round-2 lens-1 verdict already gave: the delta as drafted would enshrine
an incomplete inheritance list.

Lens: functional-analytic rigor (l0). Round: 3. New objections: 5.
