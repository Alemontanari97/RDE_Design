# ESCALATION REFUTATION — DOC-1 (phaseD_stop_proof.md, revision 4), legs 3 & 5
# Round 1, lens l1 (gas dynamics / physics, RH algebra, counterexamples)

Date: 2026-08-18. Until-dry ROUND 1 on the S-FOUNDATIONS-C escalation
repairs E-1/E-2 (`phaseD/phaseD_stop_proof.md` REVISION LOG §13,
revision 4). Scope per brief: ONLY the escalation-repair text for legs 3
and 5 — the §4 PERIODIZATION STEP rewrite (lines ~1176-1225), the G8/r2
row revision-4 edits (lines ~2077-2162), the audit-line clause (lines
~86-89), the §9 gamma-table annotation (lines ~2349-2356), the §12
superseded notes (lines ~2771-2775, 2794-2797), and the §13 log entries
themselves (lines 2800-2903) — PLUS discharge verification of the
sustained objections they answer (VERDICT_r2pass §2.1 rows L0-1/L1-1,
L1-2, L0-2; §4(c) specs E-1/E-2; full objection texts in
refute_r2batch_l0.md and refute_r2batch_l1.md, both read at the attacked
legs).

Dedup register (objections already dispositioned, NOT re-raised here):
L0-1/L1-1 (divergent "summing telescopes" line; chi' cancellation
absent; equality pairing unperiodized) — consumed by the (p1)-(p3)
rewrite, adequacy examined below. L1-2 (granted half conditional on an
unnamed thermal-stability condition) — consumed by the revision-4
clause, adequacy examined below; my ESC1-F2 attacks the ADEQUACY of that
disposition (the condition as now operationalized is still not the
sufficient one), which the dedup rule permits: the disposition itself
fails at one named point. L0-2 (s = 0 congruence mis-stitch; mediant
non-sequitur) — consumed by the rewording, examined below, no re-raise.
r2b-F6, r2b-F1, r2-F6 cited only as precedent/context. Pre-existing
structure NOT re-attacked: the stratum-(B)/front handling, the G2
Lipschitz-test consumption, the H8' class hypothesis, [S-XCONV] R1 —
all carry prior-round dispositions and the repairs do not alter them.

==============================================================================
## LEG 3 — §4 PERIODIZATION STEP rewrite (E-1)

### P3.1 The retraction ground (divergence claim) — CONFIRMED

Quote (lines 1176-1183): "the revision-3 mechanism 'summing telescopes
by periodicity' is RETRACTED: for T-periodic V the pairings
<mu, psi chi_k> below are EQUAL for every k, so the literal sum over k
in Z diverges unless the common value is zero, and nothing telescopes
among identical terms".

Strongest attack tried: deny k-independence (mu only distributionally
periodic, psi only torus-periodic). Fails: <mu, psi chi_k>
= <mu(. + kT), psi(. + kT) chi_0> = <mu, psi chi_0> by the change of
variables for distributions plus T-periodicity of mu (V T-periodic per
H8', quadruple pointwise in the state, distributional derivatives of
T-periodic L^inf functions are T-periodic) and of psi. Equal terms;
literal sum = ±infinity unless the common value is 0. The retraction is
correct as stated.

### P3.2 Step (p1), single-window pairing — CONFIRMED

Quote (lines 1192-1197): "<mu, psi chi_0> >= 0 is ONE legitimate
compact-support D'-pairing; it is k-independent ... NO sum over k is
taken anywhere."

Strongest attacks tried: (a) sign of the pairing needs chi_0 >= 0 —
holds: "partition of unity" (line 1190-1191) is by standard definition
nonnegative, and mu >= 0 in D' is a nonnegative Radon measure (Riesz),
so pairing with the nonnegative C_c^inf function psi chi_0 is >= 0;
(b) existence of such a chi_0 — standard construction
chi_0 = phi / Sum_k phi(. - kT) for any positive bump phi on (-T, T);
(c) k-independence — P3.1 computation. No hole.

### P3.3 Step (p2), field terms via Sum chi_k == 1 — CONFIRMED

Quote (lines 1198-1203): "for T-periodic h in L^1_loc(R_t),
Int_R h chi_0 dt = Int_0^T h (Sum_k chi_k) dt = Int_0^T h dt (unfold
the k-translates onto one period)."

Re-derived: Int_R h chi_0 = Sum_k Int_{kT}^{(k+1)T} h chi_0
= Int_0^T h(t) Sum_k chi_0(t + kT) dt (h(t + kT) = h(t)), and
Sum_k chi_0(t + kT) = Sum_k chi_k(t) = 1; the sum is locally finite
(supports subordinate to the period cover), so Fubini/rearrangement is
legitimate. Applied to each field term (quadruple component times
(d psi) chi_0, compact x-support), this is exactly the identification
claimed. Strongest attack tried: integrability of h chi_0 on R —
guaranteed by compact support of chi_0 and h in L^1_loc. No hole.

### P3.4 Step (p3), cutoff-derivative cancellation — CONFIRMED

Quote (lines 1204-1213): "the d_t term pairs against d_t(psi chi_0)
= (d_t psi) chi_0 + psi chi_0', producing the extra term
Int (q_t o V) psi chi_0' dt dV_x = Int over one period of
(q_t o V) psi (Sum_k chi_k') = 0, since differentiating
Sum_k chi_k == 1 gives Sum_k chi_k' == 0."

Re-derived: unfolding as in (p2) with h = (q_t o V) psi gives
Int_0^T h Sum_k chi_0'(t + kT) dt; the translate sum is locally finite,
hence termwise differentiable, and Sum_k chi_k == 1 gives
Sum_k chi_k' == 0. Strongest attack tried: termwise differentiation of
an infinite sum — discharged by local finiteness (subordination to
{(kT - T, kT + T)}), which the construction supplies. This IS the
cancellation L0-1 demanded be written; it now is. No hole.

Together P3.2-P3.4 close the conversion completely: <mu, psi chi_0>
equals the torus distributional pairing of the divergence against psi
(x, y, z terms carry no cutoff derivative; the t term splits per (p3)),
and is >= 0 by (p1). The rewritten step is a complete proof at the
document's own "the line must be WRITTEN" standard.

### P3.5 The (EU-x) EQUALITY-pairing rider — CONFIRMED

Quote (lines 1216-1225): "the weak form of (EU-x) for V is tested
against the non-compactly-supported Lipschitz field D_W E(U), which is
T-periodic in t (U is T-periodic on the slab, H8'); testing against
D_W E(U) . (test) chi_0 componentwise and applying (p1)-(p3) verbatim
(with equality in place of the inequality sign) yields the torus form
of the equality pairing."

Strongest attacks tried: (a) Lipschitz-ness of D_W E(U) — inside the
PROOF OF (A) (line 1158) U is C^1 on the compact slab and D_W E is
C^inf away from vacuum (rho >= rho_min on K), so D_W E(U) is C^1,
hence Lipschitz; the stratum-(B) front question is pre-existing
structure outside this repair (dedup). (b) T-periodicity of the test —
H8' covers the strong side since revision 1 (l0-F5/l1-F2); correct.
(c) applying (p1)-(p3) "verbatim" to an equality — for the zero
distribution every window pairing is 0 and k-independence is trivial;
(p2)/(p3) convert field and cutoff terms identically (the integrands
W(V)-, F_mu(V)-components times D_W E(U)-components times psi are
T-periodic since BOTH V and U are). This closes L0-1's second clause
exactly. No hole.

### P3.6 §13 retraction-falsifier — **OBJECTION ESC1-F1, class AMENDMENT**

Verbatim quote (§13, lines 2832-2836): "FALSIFIER of the retraction: a
finite value of Sum_k <mu, psi chi_k> for some nonzero T-periodic
mu >= 0 and admissible psi, {chi_k} — kills the divergence claim (and
with it the ground of the rewrite, not the rewritten argument itself,
which never sums over k)."

Attack (false-positive power — the r2-F6 defect class, which this
document has already retired once at the [T-T0P-E] claim site): the
firing condition as printed is satisfiable by benign instances that
refute nothing. Take any nonzero T-periodic mu >= 0 and an admissible
psi supported (in x, y, z) away from supp mu: then <mu, psi chi_0> = 0,
every term vanishes, and Sum_k <mu, psi chi_k> = 0 — a FINITE value
for a NONZERO mu, meeting the printed condition. But the divergence
claim of record (lines 1178-1181) carries the carve-out "unless the
common value is zero", so this instance is CONSISTENT with the claim:
the falsifier fires against a true claim. The missing clause is
nonzeroness of the COMMON VALUE, not of mu. Repair (one clause):
"a finite value of Sum_k <mu, psi chi_k> WITH <mu, psi chi_0> != 0".
Class AMENDMENT: the falsifier is auxiliary (it guards the retraction
ground; the rewritten (p1)-(p3) argument never sums over k, as the
entry itself notes), and the divergence claim it guards is true (P3.1).
Per R5/the document's own rejector discipline, falsifiers must not
fire on benign instances.

### E-1 DISCHARGE VERDICT: **DISCHARGED**

The VERDICT_r2pass E-1 spec (three-step argument: single-window
D'-pairing; Sum chi_k == 1 on the field terms; Sum chi_k' == 0 killing
the cutoff-derivative terms; plus the statement that the (EU-x)
EQUALITY pairing rides the same identity) is executed clause-for-clause
as (p1)/(p2)/(p3) plus the rider paragraph; statement, hypotheses (H8'
both sides, H7' test class) and labels unchanged as required; the
r2b-F6 disposition is genuinely re-closed by written argument (the §12
entry carries the supersession note, lines 2771-2775, so no stale
"telescoping" claim survives as of-record text — grep-verified: the
only remaining occurrences are the retraction itself and the superseded
§12 note). The one residue is the ESC1-F1 falsifier wording above.

==============================================================================
## LEG 5 — G8/r2 repricing, revision-4 edits (E-2)

### P5.1 The added thermal-stability clause — **OBJECTION ESC1-F2, class REPAIR-NEEDED**

Verbatim quote (G8 row, lines 2084-2094): "MODULO A NAMED
THERMAL-STABILITY CONDITION (added in revision 4 per L1-2):
W-convexity of -rho g(S) is NOT a free consequence of the §1 gas model
(Gibbs closure + c^2 > 0 + theta > 0 pin NO sign of e_SS); the
classical results cited additionally require thermal stability —
e_SS > 0 (equivalently c_v-type positivity / s-concavity in (specific
volume, internal energy) / Bethe-Weyl class: the same class G7 route
r-a already names)".

And (lines 2099-2102): "FALSIFIER of the added condition-claim: derive
e_SS > 0 from Gibbs closure + c^2 > 0 + theta > 0 alone (kills L1-2
and restores the unconditional grant)."

Derivation-level attack (thermodynamic consistency + counterexample —
my lens). The word "equivalently", extended over the whole slash-list,
is FALSE at abstract EOS, and the condition as OPERATIONALIZED
(headline e_SS > 0; breaking mechanism keyed to e_SS <= 0; falsifier
promising that e_SS > 0 "restores the unconditional grant") is
NECESSARY but NOT SUFFICIENT for delivered item (i). Three steps:

(1) What item (i) actually needs (g = id, the certified instance). The
classical equivalence: -rho s is convex in W = (rho, m, E) if and only
if s(v, e) is concave, v = 1/rho. The forward direction (the one that
breaks the grant) at pen grade: restrict W-convexity to the affine
slice {m = 0}; there -rho s(1/rho, E/rho) is the perspective transform
h(rho, E) = rho f(1/rho, E/rho) of f = -s restricted to the affine
section a = 1, and for two points (v_i, e_i) with rho_i = 1/v_i,
E_i = e_i/v_i, convexity of h delivers exactly the convexity
inequality for f at the reweighted combination lambda' = lambda
rho_1/rho_bar — sweeping all of {v > 0} x R. Hence -rho s convex in W
==> s(v, e) concave. Concavity of s(v, e) is (given theta = e_S > 0,
standard partial-Legendre inversion) equivalent to JOINT convexity of
e(v, s), i.e. to the THREE conditions e_vv > 0 (= c^2 > 0, since
c^2 = v^2 e_vv), e_SS > 0 (= c_v > 0, since c_v = theta/e_SS), AND the
determinant/cross-term condition e_vv e_SS >= (e_vS)^2 (the Grueneisen
bound). The §1 model pins the first; revision 4 adds the second;
NOBODY pins the third.

(2) Counterexample class (in-§1-class EOS with e_SS > 0 breaking item
(i)). Take the local EOS patch, primitive e(v, s):
    e = e_0 - p_0 (v - v_0) + theta_0 (s - s_0)
        + (A/2)(v - v_0)^2 + (B/2)(s - s_0)^2 + C (v - v_0)(s - s_0),
with A = B = 1, C = 2, theta_0 > 0, p_0 > 0. Define p := -e_v,
theta := e_s — the Gibbs closure e_rho = p/rho^2, e_S = theta holds
IDENTICALLY by construction. Near the patch center: c^2 = v^2 e_vv
= v^2 A > 0, theta > 0, e_SS = B = 1 > 0 — ALL §1 pins PLUS the
revision-4 condition hold. But the (v, s)-Hessian [[A, C], [C, B]] has
determinant AB - C^2 = -3 < 0: e(v, s) is NOT jointly convex, so
s(v, e) is NOT concave, so by (1) -rho s is NOT convex in W on the
corresponding region — there exist W-directions along which the
second derivative of E = -rho s is negative, and the granted lower
sandwich E(V|U) >= c|DeltaW|^2 FAILS for short segments in those
directions. Delivered item (i) breaks WITH the named condition
satisfied.

(3) Consequences for the printed text. (a) "equivalently ...
s-concavity ... / Bethe-Weyl class" is false: given the §1 pins,
e_SS > 0 is equivalent to c_v-type positivity ONLY (that pair is
fine); s-concavity is STRICTLY STRONGER (it adds the Grueneisen
determinant condition), and it — not e_SS > 0 — is the condition the
cited classical results actually run on (L1-2's own text said the
route "runs through concavity of s as a function of (specific volume,
internal energy)"; the judge's slash-list named a condition CLASS; the
revision-4 text is what promoted the list to an equivalence). (b) The
falsifier's clause "restores the unconditional grant" is false: even
if e_SS > 0 were derivable from the §1 pins, item (i) would remain
conditional on the determinant condition, per (2). (c) The breaking
mechanism as printed ("e_SS <= 0 somewhere on K BREAKS delivered item
(i)") is TRUE (necessary direction — see P5.2) but is not the only
in-class breaking mechanism, so reading it as delimiting the condition
under-prices the gap. Net: the r2 granted-half accounting is STILL
short by one named condition — the same defect class L1-2 was
sustained for, one level down. The L1-2/E-2(a) disposition is NOT
fully discharged.

Repair (accounting text, no route-level change — the correction again
STRENGTHENS the no-viable-abstract-EOS-route conclusion): name the
condition as FULL thermodynamic stability = s(v, e)-concavity
(equivalently joint convexity of e(v, s): c^2 > 0 [already §1] AND
e_SS > 0 AND e_vv e_SS >= (e_vS)^2), with e_SS > 0 = its c_v part (the
part provably missing from §1) and the determinant/Grueneisen bound =
the second part equally unpinned by §1; drop "equivalently" over the
slash-list or restrict it to the e_SS/c_v pair; fix the falsifier to
"derive s(v, e)-concavity from the §1 pins alone" (or delete "restores
the unconditional grant"); propagate the naming to the audit line
(lines 86-89), the §9 gamma table (lines 2349-2356) and the §13
entries (lines 2837-2859), whose current wording all carry the
"named thermal-stability condition" singular. The AUD-cp discharge
note SURVIVES the repair unchanged (see P5.3: at the standing
gamma(T) thermally-perfect closure the cross term vanishes, so
c_v > 0 discharges the FULL condition there).

Class: REPAIR-NEEDED, not BREAKS — the leg is a gap-accounting row;
its route-level conclusions (r2 partial, coercivity OPEN, no named
viable abstract-EOS route, gamma table unchanged) survive and are
strengthened by the finding; but the accounting text must change, by
the same severity logic the judge applied to L1-2 itself. Not a
re-raise of L1-2: that finding priced the ABSENCE of any named
condition; this one prices the revision-4 naming as sufficient — text
that did not exist before revision 4.

### P5.2 The in-class breaking mechanism — CONFIRMED

Quote (lines 2094-2096): "An in-class abstract EOS with c^2 > 0,
theta > 0 and e_SS <= 0 somewhere on K BREAKS delivered item (i)".

Verified (necessary direction): -rho s convex in W ==> (restriction to
lines varying E at fixed rho, m) s_ee <= 0, and s_ee = -e_SS/theta^3,
so e_SS < 0 at a point kills convexity outright and e_SS = 0 kills the
UNIFORM quadratic lower bound c|DeltaW|^2 (degenerate direction).
Existence of such an in-class EOS: e = -s^2/2 + 10 s + v^2/2 near
(v, s) = (1, 0) has theta = 10 - s > 0, c^2 = v^2 > 0, e_SS = -1.
True as printed. Strongest attack tried: none survives — the statement
is the easy direction of P5.1's chain.

### P5.3 The gamma(T) discharge note — CONFIRMED

Quote (lines 2097-2099): "On the STANDING gamma(T) thermally-perfect
closure it is DISCHARGED by the AUD-cp-class finite audit (c_v > 0),
so it prices the ABSTRACT-EOS accounting only."

Verified at pen grade INCLUDING the stronger condition my ESC1-F2
demands: for a thermally perfect gas p = rho R T, e = e(T),
ds = de/T + R dv/v gives s(v, e) = Int de/T(e) + R ln v + const, so
s_ee = -1/(c_v T^2) < 0, s_vv = -R/v^2 < 0, s_ev = 0 — the Hessian is
DIAGONAL negative-definite whenever c_v > 0: the cross-term condition
is automatic at the standing closure, so the AUD-cp c_v > 0 audit
discharges the FULL s-concavity there, not merely e_SS > 0. The
discharge claim is correct and survives the ESC1-F2 repair verbatim.
(This also confirms the row's "prices the ABSTRACT-EOS accounting
only" sentence.)

### P5.4 The L0-2 rewording (s = 0 / two-point obstruction) — CONFIRMED

Quote (lines 2110-2126): "the segment-Taylor integrand D^2 G_U(W_s) is
at every s > 0 a TWO-POINT object (U != W_s: curvature evaluated at
W_s against the multiplier D_W E(U) anchored at U, congruent to NO
M-Hessian at all) with NO definiteness certificate, on or off the
branch — THIS is the open obstruction. (Reworded in revision 4 per
L0-2: the revision-3 sentence attached [S-XCONV] R1 at s = 0, where
the congruence D^2 G_U(W_U) = DF_x^T Hess_M(eta)(M_U) DF_x ... in fact
yields the certified DEFINITE block — the s = 0 base point is
SUPERSONIC-BRANCH ... at subsonic W_s even the ONE-POINT congruent
object is indefinite by [S-XCONV] R1 — an auxiliary fact, not the
mechanism.)"

Re-derived: with G_U(W) = Q_x(W) - D_W E(U).F_x(W) and Q_x = eta o F_x,
D^2 G_U(W_s) = DF_x^T Hess_M(eta)(M_s) DF_x
+ (D_M eta(M_s) - D_M eta(M_U)) . D^2 F_x(W_s) — using
D_W E(U) = D_M eta(M_U) (L-COMPAT). At s = 0 the second term vanishes
and the first is the congruence at the SUPERSONIC base M_U: DEFINITE
by the certified pointwise block. At s > 0 the second (two-point) term
is present and carries no certificate. Exactly the judge's Act (iii)
and the L0-2 repair spec, transcribed correctly this time. Strongest
attacks tried: (a) invertibility of DF_x at subsonic W_s for the
"auxiliary fact" (inertia transfer of [S-XCONV] R1 needs the
congruence nondegenerate) — holds: the L-XSON3 determinant vanishes
only at u = 0 and u = c, so at 0 < u < c the congruence is by an
invertible map and indefiniteness transfers; (b) "congruent to NO
M-Hessian at all" as a literal universal — read as "not congruent via
the natural change of variables to the M-Hessian at any single point",
the judge's own phrase; pricing prose, no derivation rides on it. No
hole.

### P5.5 The restored mediant clause — CONFIRMED

Quote (lines 2127-2139): "u = m1/rho is a mediant under convex
combination AND c moves with (rho, S) — S is not affine in W, and
W-averaging deposits velocity variance into internal energy, raising c
(the mixing mechanism, verified by l1's exhibit) — so two supersonic
states can average subsonic (... the pair is EXPECTED-NOT-EXHIBITED —
no certified subsonic-average pair is on file, and none is needed for
the OPEN verdict: the burden sits on r2's unproven coercivity, not on
this pricing)".

The load-bearing second clause is restored exactly per the L0-2 repair
spec, and the spec's either/or (exhibit a pair OR mark
expected-not-exhibited) is met by the marker. Strongest attack tried:
kill the mechanism itself. It survives — construction: ideal gas
gamma = 1.4, two states with equal rho, S, u = 1.05 c_0 and OPPOSITE
transverse velocity v = +/- 2 c_0; the W-average has the same rho and
u, zero transverse velocity, and internal energy raised by v^2/2
= 2 c_0^2, so c_new^2 = c_0^2 (1 + 2 gamma(gamma - 1)) = 2.12 c_0^2,
c_new ~ 1.456 c_0 > u: subsonic average from two supersonic states.
(Not a number of record — pen-grade check of the mechanism only; the
states sit outside the K box, which is irrelevant to the {u > c}
non-convexity claim as stated.) The honesty split ("mechanism verified
/ pair not exhibited") is internally consistent: l1's exhibit was a
mechanism argument, not a certified pair, and the row says exactly
that. No hole.

### P5.6 Status line, audit line, gamma table, §13 consistency — CONFIRMED (modulo ESC1-F2)

Quote (lines 2144-2154): "STATUS of r2 (honest status line of record,
revision 4): a PARTIAL reduction MODULO the named thermal-stability
condition ... + OPEN x-flux segment coercivity (a G8-equivalent
problem). CONSEQUENCE OF RECORD: NO named viable abstract-EOS G8 route
exists at this revision".

The status line matches the E-2 spec's demanded wording verbatim; the
audit line (lines 86-89), the §9 gamma table (lines 2349-2356) and the
§13 label summary all carry the same two-piece r2 residue coherently;
grep confirms no stale copy of the retracted "only abstract-EOS route"
or "kills the hull problem" sentences outside their retraction
contexts; "route-level conclusions UNCHANGED" (§13 header claim) is
accurate — no label motion, consistent with VERDICT_r2pass §4(a).
Strongest attack tried: hunt a consistency gap between the four sites
— none found; the ESC1-F2 naming defect propagates to all four
uniformly (anchors listed in the ESC1-F2 repair), which is the one
change they need.

### E-2 DISCHARGE VERDICT: **E-2(b)/L0-2 DISCHARGED; E-2(a)/L1-2 PARTIALLY DISCHARGED**

The L0-2 rewording spec is executed completely and correctly (P5.4,
P5.5). The L1-2 spec is executed FORMALLY (condition added, AUD-cp
note added, status line as demanded) but the condition as
operationalized is the necessary marker, not the sufficient condition,
and the added "equivalently" gloss plus the falsifier's "restores the
unconditional grant" clause are false at abstract EOS (ESC1-F2): the
granted-half accounting remains short by the Grueneisen/determinant
piece of thermodynamic stability. One further repair pass on the
naming closes it; nothing at route level moves.

==============================================================================
## Summary table

| # | Passage | Class | Verdict |
|---|---------|-------|---------|
| P3.1 | retraction ground (divergence claim) | — | CONFIRMED |
| P3.2 | (p1) single-window pairing | — | CONFIRMED |
| P3.3 | (p2) field-term identification | — | CONFIRMED |
| P3.4 | (p3) chi' cancellation | — | CONFIRMED |
| P3.5 | (EU-x) equality-pairing rider | — | CONFIRMED |
| P3.6 | §13 retraction-falsifier | **ESC1-F1 AMENDMENT** | false-positive firing condition; add nonzero-common-value clause |
| P5.1 | thermal-stability clause + falsifier | **ESC1-F2 REPAIR-NEEDED** | "equivalently" gloss false; e_SS > 0 necessary-not-sufficient (Grueneisen determinant condition unpinned); counterexample class exhibited |
| P5.2 | e_SS <= 0 breaking mechanism | — | CONFIRMED |
| P5.3 | AUD-cp gamma(T) discharge | — | CONFIRMED (survives ESC1-F2 repair) |
| P5.4 | s = 0 / two-point rewording | — | CONFIRMED |
| P5.5 | restored mediant clause | — | CONFIRMED |
| P5.6 | status/audit/table/§13 consistency | — | CONFIRMED (modulo ESC1-F2 propagation) |

Discharge verdicts: E-1 DISCHARGED; E-2(b) DISCHARGED; E-2(a)
PARTIALLY DISCHARGED (ESC1-F2).

Counts: 2 objections total (1 REPAIR-NEEDED, 1 AMENDMENT), 0
BREAKS-THE-LEG. 10 passages examined and CONFIRMED with strongest
attacks recorded.

==============================================================================
## Falsifiers for THIS refutation (how to kill my findings)

- Kills ESC1-F2: a proof that -rho g(S) (g = id) is convex in W under
  ONLY Gibbs closure + c^2 > 0 + theta > 0 + e_SS > 0 (i.e., that the
  determinant condition e_vv e_SS >= (e_vS)^2 is implied by those
  four); OR a demonstration that my quadratic e(v, s) patch (A = B = 1,
  C = 2) violates one of the §1 pins on every neighborhood of its
  center; OR a reading of the printed row under which "equivalently"
  demonstrably scopes ONLY over the e_SS/c_v pair AND the falsifier's
  "restores the unconditional grant" is not of-record text. My m = 0
  perspective-slice derivation ( -rho s convex ==> s(v, e) concave) is
  the load-bearing step: refute it and ESC1-F2 falls.
- Kills ESC1-F1: a demonstration that the printed falsifier condition
  ("finite value ... for some nonzero T-periodic mu >= 0 and
  admissible psi") CANNOT be met with zero common value — i.e. that
  admissibility of psi forces <mu, psi chi_0> > 0 for nonzero mu (no
  such constraint is printed; psi ranges over all nonnegative
  T-periodic torus tests).
- Kills any CONFIRMED verdict: a derivation-level break in the quoted
  passage that my recorded strongest attack missed; in particular
  P3.3/P3.4 die if the local-finiteness/termwise-differentiation step
  is shown to fail for a partition of unity subordinate to the period
  cover (it cannot: supports are compact and the cover is locally
  finite by construction), and P5.4 dies if the Hessian-split identity
  D^2(eta o F_x) = DF_x^T Hess(eta) DF_x + D_M eta . D^2 F_x is shown
  wrong (chain rule; it is not).

END — {objections: 2, breaks: 0,
file: validation/sfoundations_raws_2026-08-13/r2pass/esc_doc1_r1_l1.md}
