# REFUTATION — MINOR (a) NTF (one round, complete)
# S-FOUNDATIONS-C4 Blocco 1 v2, 2026-08-20. Refuter slot per
# BRIEF_blocco2_phaseD.md MINORS (a). Target:
# validation/sfoundations_raws_2026-08-13/phaseD/phaseD_minor_ntf.md.
# Probe of record (executed this window, exit 0, both scenes stand):
# validation/sfoundations_raws_2026-08-13/phaseD/
#   r22f_v2_probe_minor_ntf_pass_bound_and_termination.py

## 0. Read-depth declarations (this refuter's own reads)

[FULL] BRIEF_blocco2_phaseD.md; BRIEF_blocco2_phaseD_addendum_c4.md;
phaseD_minor_ntf.md (target); s25bis_gap29_sweep.py;
s25bis_gap29_sweep.json.
[SECT] VERDICT_wave3.md (§1.1, §1.2, §7, §8, §9, machine block);
VERDICT_wave2.md (§2.8, §4.11, §4.14 + grep spans for C18/C20).
[LINES] docs/findings_registry.yaml :204-238 (rows [OBJ-DOM],
engine-core:F5-underived-factors, parametrization:natural-BC-lip-bias
head); docs/choice_ledger.yaml :324-333 (row C18);
validation/a1_ideal_march_jax.py :160-210, :427-485, :790-830,
:1440-1450.
[PAGES] Deuflhard CSM 35 (literature/deuflhard_2011_...csm35.pdf):
book pp. 51-52 (PDF 62-63), p. 131 (PDF 141), p. 148 (PDF 158);
Yamamoto 1986 (literature/yamamoto_1986_...numermath48.pdf): pp.
91-92 = PDF 1-2, RENDERED (no text layer — confirms the author's
declaration); Nocedal-Wright 2ed (literature/nocedal_wright_2006_
...2ed.pdf): book pp. 613-616 (PDF 632-635).
NOT READ (declared, with reason): SYNTHESIS_nozzle_rde_arrivals.md,
FIELD_ATLAS_targeted_c4.md, the four NOZZLE_RDE_STUDY_* dossiers —
this minor touches no nozzle-paper content; CT-6 is trivially
respected on both sides (verified: the author file contains no number
from the four nozzle papers).

## 1. Seam-consumption verification (brief-mandated check): AUTHOR COMPLIANT

1. VERDICT_wave2 §4.11 (:1067-1070): "the kappa-qualified band and
   the NEWTON_TOL_FACTOR derivation are one question (GAP-29 factor-2
   cliff)" — quoted by the author VERBATIM-correct (§0). VERIFIED.
2. VERDICT_wave3 §7 item 2 (:766-771): four riders (C34/C35 consume
   the floor as input; C17 joins the seam; C44 rides the same
   measured-noise object), one owner. The author's §0 restatement is
   faithful. VERIFIED.
3. VERDICT_wave3 §1.1 (C34) / §1.2 (C35) adopted forms: consumed
   as-is, not re-derived (C35's adopted xtol_u = floor_W/(K_RICH ×
   max(Dv)) referenced by object name only). No collision. VERIFIED.
4. Tier-1 window sharing: VERDICT_wave2 §2.8 (:753-754)
   "F2-C20-CERTQUAL-CAMPAIGN ... Tier-1 shared with C18" — the
   author's F2-NTF-FLOOR-POPULATION rides that window and mints no
   new one. VERIFIED.
5. Anchor-drift note: measured this window, choice_ledger.yaml row
   C18 sits at :324-333 (VERDICT_wave2 cites :315-324) — the author's
   drift note is CORRECT and cites by id. VERIFIED (SR-12 conformant).
6. Registry row engine-core:F5-underived-factors (:214-222): owner
   and trigger text quoted correctly; NEWTON_TOL_FACTOR = 100.0
   verified at a1_ideal_march_jax.py:200; loop/cert semantics
   verified at :444-448 and :795-828; O3.1 replay band verified at
   :1448 (= 10*NTF*EPS*scale, co-moves with NTF as the author says).
7. Author arithmetic re-verified from the committed carrier:
   0.7011026275409529*100 = 70.110; 1.033309604151919*50 = 51.665;
   70.110/51.665 = 1.357; 100/70.110 = 1.426; 2*100*EPS = 4.441e-14.
   ALL CORRECT.

## 2. Citation spot-verification at source (load-bearing cites)

- Nocedal-Wright p. 614, eq. (A.30): "fl(x) = x(1+eps), |eps| <= u",
  u ~= 1.1e-16 for IEEE double = EPS/2. VERIFIED at source (PDF 633).
  H1's citation is good (see MIN-NTF-7 for the (A.31) extension).
- Deuflhard p. 148 (PDF 158), NLEQ-ERR: "Set a required error
  accuracy eps sufficiently above the machine precision" +
  termination "||dx_k|| <= XTOL". VERIFIED VERBATIM. The author's
  gloss (stated as unquantified practice; NTF = its quantification)
  is fair.
- Deuflhard pp. 130-131 (PDF 141), NLEQ-RES: "required residual
  accuracy eps sufficiently above the machine precision". VERIFIED.
- Deuflhard pp. 51-52 (PDF 62-63), (2.13)-(2.14): PRESENT as cited,
  but (2.14) reads ||dx_k||/(1 - Theta^2_{k-1}) <= XTOL — see
  MIN-NTF-4 (attribution precision).
- Yamamoto 1986 p. 92, Theorem 2 (Gragg-Tapia), eq. (7): two-sided
  bound 2||x_{n+1}-x_n||/(1+sqrt(1+4th^{2^n}/(1+th^{2^n})^2)) <=
  ||x*-x_n|| <= th^{2^n-1}||x_n-x_{n-1}||. VERIFIED on rendered
  pages. The lower-constant claim c_L >= 1/2 is TRUE and conservative
  (the actual worst denominator is 1+sqrt(2), giving c_L >=
  2/(1+sqrt(2)) ~= 0.828 — see MIN-NTF-10).

## 3. FINDINGS

### MIN-NTF-1 — CONTENT-OBJECTION. NTF-2's PASS bound constant is
wrong as stated: the "floor term is absorbed" parenthetical inverts
the triangle inequality.
Claim attacked (NTF-2, §8 line NTF-2, and NTF-3's UB): "a PASS ...
certifies ||z_hat - z*|| <= 2*NTF*EPS*sc (the floor term is
absorbed: at a PASS, step <= T already includes the floor
contribution)". Reason: the measured extra step is dz_hat = dz_exact
+ noise with ||noise|| <= floor (H3/NTF-1). A PASS gives ||dz_hat||
<= T, hence only ||dz_exact|| <= T + floor — noise bounded by the
floor can CANCEL part of the exact correction, it does not only
inflate the measured step. Composing with the (verified) exact
two-sided estimator gives error <= 2*(T + floor) <= 2*T*(1 + 1/eta)
under the author's own LB, NOT 2*T. EXECUTABLE COUNTEREXAMPLE
(probe scene A, exit-0 this window): 1D Newton instance, Theta =
0.497 <= 1/2 (H2 holds), injected noise exactly at the declared
floor = 0.8*T (eta = 1.25, the author's own bracket edge),
certificate ratio 0.990 => PASS, true error = 3.401*T > 2*T
(claimed bound violated by 1.70x); amended bound 2*(T+floor) = 3.6*T
holds (err/bound = 0.945). Named repair (amendment-sized): replace
the constant 2*T by 2*(T + floor_cell) (equivalently 2*T*(1+1/eta)
population-wide under LB), strike the "absorbed" parenthetical, and
propagate: NTF-3's UB becomes 2*(1+1/eta)*NTF*EPS*sc <= tol_min;
the window-nonemptiness condition becomes 2*(eta+1)*kappa_eff,max*
EPS*sc <= tol_min; §8's NTF-2 line re-stated. What SURVIVES the
repair (stated so the judge can right-size): the record-case window
margin (>11 orders) is untouched; the eta-bracket "same decade"
upper-edge argument survives (2*(eta+1) <= 7 < 10); the THEOREM*
label is recoverable on the repaired constant — the objection is to
the stated constant and its justification, not to the composition
architecture.

### MIN-NTF-2 — CONTENT-OBJECTION. NTF-3's UB compares a z-space
error to consumer-space tolerances with an undeclared unit-transfer
hypothesis.
Claim attacked: "(UB) 2*NTF*EPS*sc <= tol_min, where tol_min = the
tightest NTF-INDEPENDENT downstream tolerance consuming the
certified error ... On the record case: 2*100*EPS = 4.44e-14 (unit
scale) vs ... o31_tol = 7.65e-2 ... the window is open by >11
orders". Reason: the certified quantity is a PER-CELL STATE error
(z-space, infinity norm, a1:469); o31_tol tolerances an O3.1
DIRECTIONAL-DERIVATIVE agreement (adaptive_knot_optimize.o31_spot,
consumed via gradient/J values — sweep script :98-103). The z-error
reaches that consumer only through the evaluation/differentiation
chain, whose amplification the program's OWN record shows is large:
registry row engine:cross-lowering-gradient-floor (:328-336) [ADV]
carries "adjoint reassociation floor ~1e-8 rel through ~250 implicit
solves, FD amplification ~7 orders" — the very object minor (d)
derives. The UB inequality as written implicitly sets the transfer
factor to 1, and the ">11 orders" headline is a cross-space
comparison without the declared hypothesis. This is not saved by the
later composition remark ("must be checked against at composition
time, C41 P-tag") because the remark is attached to FUTURE tighter
consumers, while the record-case comparison is asserted NOW.
Named repair (amendment-sized, AG-1-conformant): state the UB as
2*(1+1/eta)*NTF*EPS*sc * A_c <= tol_c for each consumer c, with A_c
the (declared, sufficient-not-optimized) transfer factor, and
re-state the record case honestly: even at the cross-lowering row's
~7-order amplification class the window stays open by ~4 orders —
the CONCLUSION survives; the stated FORM does not. Rigor note: with
the repair, the "window inequality is exact [THEOREM*]" sentence
becomes conditional on the declared A_c, which is exactly what the
load-class valve licenses.

### MIN-NTF-3 — CONTENT-OBJECTION. NTF-4's conjunction ("always
exhausts 30 trips AND then fails certification") is false inside the
author's own floor model in the near-threshold regime, and the
pinned falsifier is over-broad as a consequence.
Claim attacked (NTF-4): "if NTF < kappa_eff(cell),
metric-termination is unreachable at that cell: the loop always
exhausts N_NEWTON = 30 trips ... AND the cell then fails
certification." Reason: kappa_eff is an ENVELOPE constant (H3 bounds
||delta||; it does not pin each evaluation). Near the threshold —
exactly the ntf50 arm's regime, envelope ~51.7 vs T = 50, 3.3%
apart — per-trip fluctuation lets the step dip below T at some trip:
the loop terminates ON THE METRIC early, while the fresh
certification sample still exceeds T at some cells => population
FAIL with metric-termination reached. EXECUTABLE COUNTEREXAMPLE
(probe scene B, exit-0 this window): T = 0.97*floor (NTF <
kappa_eff-envelope at every cell), 200 cells, H3-consistent sampled
steps: metric-termination reached at 200/200 cells (max 3 trips vs
cap 30), certification FAIL at 6/200 cells => population verdict
FAIL. Consequence for the pinned falsifier: as written ("trip-count
instrumentation ... showing metric-termination still reached at the
ntf50 arm's failing cells (would refute the same-threshold coupling
claim)"), it fires on data fully CONSISTENT with the floor model —
an F2 experiment designed to force a spurious retraction. Named
repair (amendment-sized): scope the unreachability claim to cells
with kappa_eff(cell) >= (1+m)*NTF for a declared fluctuation margin
m (deterministic-envelope regime), state the near-threshold regime
as a fluctuation band (termination-in-k-trips probability + FAIL
probability both nonzero — which, note, is ALSO the cleaner
explanation of why the ntf50 arm can carry worst ratio 1.033 while
still terminating), and re-pin F2-NTF-TERMCOUPLE-TRIPCOUNT's
falsifier accordingly (e.g. refutation requires metric-termination
with MARGIN — steps consistently below T*(1-band) — at cells whose
measured kappa_eff sits >= (1+m)*NTF). The SCHEMA label is honest;
the claim text and falsifier need the scoping.

### MIN-NTF-4 — WORDING. Deuflhard attribution of the upper
estimator. NTF-2(a) states ||z_k - z*|| <= ||dz_k||/(1 - Theta) <=
2||dz_k|| and cites "[Deuflhard CSM 35, termination criterion
(2.13)-(2.14), book pp. 51-52]". Verified at source: (2.13) is the
desirable criterion ||x_k - x*|| <= XTOL, and (2.14) is its cheap
substitute ||dx_k||/(1 - Theta^2_{k-1}) <= XTOL — denominator
1 - Theta^2_{k-1}, NOT 1 - Theta. The author's form is TRUE (it is
the geometric-series bound under uniform contraction Theta_j <=
Theta <= 1/2 for j >= k, which H2's contraction-ball hypothesis
supplies), but it is not the literal content of (2.13)-(2.14).
Fix: attribute as "geometric-series consequence of the contraction
(cf. Deuflhard (2.8)-(2.14), pp. 51-52)" or cite the Yamamoto eq.
(7) upper half instead (which IS a two-sided source, already cited
for the lower half). No mathematical damage; a THEOREM*-labeled
statement should not carry an imprecise equation-level attribution.

### MIN-NTF-5 — WORDING. "NTF-INDEPENDENT" o31_tol is not measured
as NTF-independent. The sweep json (committed carrier) shows o31_tol
= 0.07646 (base) vs 0.07960 (ntf50): a 4.1% solution-mediated drift
across the 2x NTF arm. The formula carries no NTF factor
(structurally not NTF-proportional — the author's exclusion of the
co-moving replay band remains correct), but the flat label
"NTF-INDEPENDENT" contradicts the carrier it cites. Fix: "not
NTF-proportional (no NTF factor in its formula; measured 4%
solution-mediated drift across the ntf50 arm, declared)". Immaterial
to the window margin.

### MIN-NTF-6 — WORDING. The kappa_eff defining line is garbled:
"kappa_eff := ||J^{-1}|| * gamma_R * S_R / (EPS-normalized sc)". The
dimensionally coherent reading (which the surrounding text supports)
is kappa_eff = ||J^{-1}|| * gamma_R * S_R / sc, dimensionless, with
EPS factored out in front of the floor formula. As printed,
"(EPS-normalized sc)" invites reading an extra 1/EPS into kappa_eff.
Fix: one-line rewrite. (The measured-instance arithmetic is
unaffected — it never uses the symbolic form.)

### MIN-NTF-7 — NOTE. H1 cites (A.30) for "every stored/computed
scalar"; at source (verified) (A.30) is the STORAGE model and the
per-operation model is (A.31) (p. 615, same bound u). Extend the
citation to "(A.30)-(A.31)". Zero mathematical impact.

### MIN-NTF-8 — NOTE. The sweep json's k_newt field (= 2 in all
arms) is the THERMOTAB derived K_NEWT (c1["K_NEWT"], sweep script
:66), not a march trip count — so NTF-4's statement "the sweep json
has no per-cell trip field" is VERIFIED CORRECT, but a preempting
parenthetical naming k_newt's identity would stop the natural
misreading that trips were recorded at 2.

### MIN-NTF-9 — NOTE (rides MIN-NTF-1's repair). NTF-5 pins floor_W
:= NTF*EPS*sc "consumed by C34/C35 unchanged". After the MIN-NTF-1
repair the landing should state explicitly that consumers get the
THRESHOLD object T (correct for C35's premature-stop purpose,
verified against VERDICT_wave3 §1.2), while the certified ERROR
bound is the distinct, larger object 2*(T+floor) — two objects, one
sentence, so no downstream reader conflates them.

### MIN-NTF-10 — NOTE. Yamamoto eq. (7) actually yields c_L >=
2/(1+sqrt(2)) ~= 0.828 (worst case at theta -> 1), so the author's
c_L >= 1/2 is valid and conservative. AG-1-conformant as declared;
recorded so the F2 duty window knows ~1.66x tightening is available
for free if the FAIL-witness bound ever becomes binding.

### MIN-NTF-11 — NOTE. H2's "checkable from the recorded
contraction": the record carries no per-cell Theta (the march
records cert ratio and population count only, a1:793-828, and the
sweep adds none). As written it overstates current checkability;
honest form: "checkable from contraction data the F2 probes will
record". Small honesty patch, same class as the author's own
NTF-4 trip-count discipline.

### MIN-NTF-12 — NOTE. NTF-3's retro-validation sentence "50 <
kappa_eff,worst ~= 70.1, so FAIL is required" leans the base-arm
worst-cell kappa against the ntf50 arm, where the declared
worst-cell-may-differ caveat (NTF-1) applies; the self-contained
witness is the ntf50 arm's OWN measurement 51.665 > 50 (3.3%
margin — worth stating, since it shows how close to the cliff the
flip sits). Restate the caveat at the point of use; prediction
logic otherwise sound.

## 4. What was attacked and HELD (so the judge sees the coverage)

- Seam discipline (§1 above): fully compliant, no collisions, no
  re-derivation of C34/C35/Tier-1 objects; anchor-drift handling
  SR-12-exemplary.
- Brief-scope compliance: theory half only; gate REFORM correctly
  excluded; F2 duties named, none executed; no new window minted.
- NTF-1's floor-dominance inference from the two-arm contrast: the
  alternative hypothesis (damped linear-contraction tail tracking T)
  is REAL but is already covered by the author's own falsifier
  (i)/(ii) (tolerance-tracking + float32 scale-law contrast) — no
  finding, the falsifier can kill it.
- NTF-2's FAIL-witness direction ("error >= T/2 up to the floor
  term"): keeps the floor caveat, consistent with the corrected
  composition — HOLDS.
- NTF-3 LB (true root PASSes under the envelope + LB): HOLDS.
- Incumbent adjudication (100 = valid instance, headroom 1.426
  inside [1.25, 2.5]; flip = model prediction): arithmetic verified,
  HOLDS (with MIN-NTF-12's restated caveat).
- Two-sided-headroom honesty (C42 roles-4/5 precedent consumed,
  eta not blanket-"conservative"): HOLDS, good discipline.
- All four load-bearing literature citations exist at the declared
  pages with the claimed content (one attribution-precision fix,
  MIN-NTF-4).

## 5. PAPERS NEEDED

None new from this refutation. (The author's conditional Higham
entry and the deduplicated More-Wild entry are right-sized; the
counterexamples above needed no source beyond what is on disk.)

## 6. Machine summary

item: minor (a) NTF — refuter round 1 (complete, one round)
probe: r22f_v2_probe_minor_ntf_pass_bound_and_termination.py
  (executed this window, exit 0, scenes A+B both stand)
findings:
  MIN-NTF-1: CONTENT-OBJECTION — NTF-2 PASS constant 2*T false as
    stated ("absorbed" inverts triangle inequality); probe scene A:
    PASS at ratio 0.99 with true error 3.401*T > 2*T, Theta 0.497,
    noise within declared floor; repair = 2*(T+floor) with named
    propagation (NTF-3 UB, window condition, §8); architecture and
    record-case margin survive.
  MIN-NTF-2: CONTENT-OBJECTION — NTF-3 UB mixes z-space error with
    consumer-space tol without a declared transfer factor; program's
    own cross-lowering row (:328-336, ~7 orders) [ADV] names the
    threat; repair = declared A_c per consumer; conclusion (window
    open, ~4 orders worst-class) survives.
  MIN-NTF-3: CONTENT-OBJECTION — NTF-4 "always exhausts 30 trips AND
    fails" false in the near-threshold fluctuation regime of the
    author's own model (probe scene B: 200/200 metric-terminations,
    max 3 trips, 6/200 cert FAILs at T = 0.97*floor); pinned F2
    falsifier over-broad (would fire on model-consistent data);
    repair = envelope-margin scoping + re-pinned falsifier.
  MIN-NTF-4: WORDING — Deuflhard (2.14) denominator is
    1-Theta^2_{k-1}; re-attribute the 1/(1-Theta) form as the
    geometric-series consequence (or use Yamamoto eq. (7) upper half).
  MIN-NTF-5: WORDING — "NTF-INDEPENDENT" o31_tol drifts 4.1% across
    the ntf50 arm in the cited carrier; say "not NTF-proportional".
  MIN-NTF-6: WORDING — "(EPS-normalized sc)" garbled; kappa_eff =
    ||J^{-1}||*gamma_R*S_R/sc.
  MIN-NTF-7: NOTE — extend H1 citation to (A.30)-(A.31).
  MIN-NTF-8: NOTE — name json k_newt identity (thermotab K_NEWT).
  MIN-NTF-9: NOTE — floor_W = threshold object vs certified-error
    object: one disambiguating sentence at the landing.
  MIN-NTF-10: NOTE — c_L actually >= 0.828; 1/2 conservative, fine.
  MIN-NTF-11: NOTE — H2 "recorded contraction" overstates current
    records; point at the F2 probes.
  MIN-NTF-12: NOTE — restate worst-cell caveat at the NTF-3
    retro-validation sentence; ntf50's own 51.665 > 50 is the
    self-contained witness.
counts: {content_objections: 3, wording: 3, notes: 6}
seam_verification: AUTHOR COMPLIANT (6 checks, §1)
citation_spot_checks: 5 verified at source, 1 attribution fix
  (MIN-NTF-4)
escalation_input_for_judge: 3 content objections, ALL
  amendment-sized with named repair texts and named surviving
  content; none attacks the architecture (floor model + two-sided
  semantics + window form + seam position all HOLD).
papers_needed: none
