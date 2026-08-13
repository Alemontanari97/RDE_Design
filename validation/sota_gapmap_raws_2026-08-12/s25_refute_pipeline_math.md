# S25 DEDICATED REFUTER — Form-2 convergence round 1
## Target: `validation/ADVISORY_S25_pipeline_sense_math_2026-08-12.md` (single-expert one-pass math-structure review)

Date: 2026-08-12. Mandate: default-REFUTE every load-bearing claim, argued
at SOURCE (repo files + record docs), read-only, no code execution.
Sources read this pass: M0 D2.6 + Part III [T-GB]/[T-T4] + Part VI
S20/S21/S22/S23/S24 registration blocks; `docs/claims_registry.yaml`
(C-EQV2, X-DEFTW rows); `validation/a1_ideal_march_jax.py` (docstring);
`validation/a1_toc_variational_jax.py` (:1-96, :160-260, :330-490,
:938-1012); `validation/margin_governor.py` (:1-70, :130-247);
`validation/def_twin_falsifier.py` (:600-651, :1240-1289);
`validation/ADVISORY_S24_sota_gapmap_2026-08-12.md` (all 36 GAP rows,
AC1-AC16, Q1-Q10, C1-C45); `validation/AUDIT_agnostic_2026-08-07.md`
(:495-539); `validation/t3qs_sweep_protection.py` (:1-45);
`tests/run_all.py` (:56, :91); M0 :580 [T-T3-SI], :644-651 [T-T3-MAP],
:734 T3-CONTROL, :785-811 [T-T4]. Verification greps re-run:
`J_ideal|bound[ _-]ladder` over `validation/*.py` (0 matches);
`frac_bad|discontinu` over `validation/*.md`;
`supp(mu)|intersection over` over `docs/`.

Label: refuter position, round 1 — not a converged verdict. Everything
below cites the anchor it stands on.

---

## §1 CLAIM-BY-CLAIM ADJUDICATION

### R1 — "outcome-II points sit on a set with no continuum object; no theorem — and currently no conjecture with a falsifier — connects them to any (P_t) as h->0; EQ-v2 Direction A untestable; mu unmeasurable"

**VERDICT: SURVIVES-WEAKENED.** The mathematical gap is real and the
record itself registers it; the "not even a conjecture-with-falsifier"
clause is FALSE at the letter and materially under-credits the record.

What the record actually holds (all verified at source):

1. The tier ladder (P_t) + margin-multiplier KKT is REGISTERED
   formalization, classes declared (M0:1595-1617: nesting/constrained-KKT
   = THEOREM, ladder/A_t = SCHEMA), and it is EXECUTABLE
   (`margin_governor.py:8-15` states the carrier implements exactly that
   formulation). The expert credits this ("the program's honest
   formalization") — consistent.
2. "K_disc ~ A_0" was a REGISTERED CONJECTURE WITH A NAMED FALSIFIER
   (M0:1619-1624: "evaluate the Eq. (4)/Sternin validity relation ...
   along the walk: it must approach its boundary where certification
   degrades, else the bridge is dead") — executed and FALSIFIED
   (M0:1773-1782), with a standing rule that future bridge claims carry
   per-instance monitors. So the program POSED the set-level link and
   MEASURED its death. That is epistemically stronger than "no
   conjecture": a falsified named conjecture is falsification DATA, and
   the expert's own R1 header cites it.
3. [C-EQV2] is a LIVE registry row of `kind: conjecture` with a
   POPULATED FALSIFIER FIELD (`docs/claims_registry.yaml:1387-1398`:
   "the pre-registered twin falsifier F1-F7 (F1b): wall-contour gap not
   shrinking in the Richardson two-code band, cusp not converging to
   D', f2 drifting beyond the S19 bar, BF not vanishing under
   refinement, ..."), whose Direction A explicitly speaks of the JOINT
   CONTINUUM LIMIT h->0, KS rho->inf, mu_0->0 (M0:1657-1662) with the
   limit order registered as obligation O5 (M0:1724-1725; S24 carries O5
   as a named conditional, M0:2076-2078). Its carrier [X-DEFTW]
   (registry :1870-1881) EXECUTED in S24. H-CLASS is a NAMED HYPOTHESIS
   ADDED to that conjecture (M0:2042-2046), whose failure is MEASURED at
   the executed class — and the record's exact wording is "the
   falsifier's decisive content is UNREACHED **at this class**" with
   named exits C7/F2 (M0:2053-2056). A conjecture one of whose named
   hypotheses measurably fails in the executed class is not "no
   conjecture with a falsifier": it is a conjecture whose falsifier ran
   and returned a class-scoped obstruction.

What survives of R1, precisely: (i) no registered statement — theorem or
conjecture — links the ARGMAX over K_h (the outcome-II point itself,
which is margin-INACTIVE and KKT-open, hence outside EQ-v2-A's
margin-active subject) to a KKT point of any (P_t); (ii) the only
SET-level link (the bridge) is dead with no successor (GAP-1 text:
"No successor quantifier exists", gap map :69-71); (iii) at the executed
ladder "the mu_0->0 limit set of margin-active KKT points is EMPTY"
(M0:2052-2053) and mu = 0 identically (M0:2078-2080), so no measured mu
exists at tier-0 — and independently of that, O1 undischarged means mu
carries the B-stationarity qualifier anyway (M0:1712-1714). Q1's sharp
form is a fair restatement of what the record already says about itself.

Required repairs before absorption: (a) delete/replace "and currently no
conjecture with a falsifier" — the accurate sentence is "the two
registered statements aimed at this link are, respectively, FALSIFIED
(bridge, S22) and hypothesis-blocked at the executed class (EQ-v2-A +
H-CLASS, S24), with named exits (C7, GAP-1) and the limit-order question
already registered as O5"; (b) "EQ-v2 Direction A untestable (S24 says
this)" must carry the record's own scope — "at this class"
(M0:2053-2054), since C7 (refine/enriched class) is exactly the
registered route by which it becomes testable; (c) the numeric
parenthetical "certification degrades at val 0.61-0.86 ... three
instances" conflates instances: 0.612-0.620/0.651-0.857 are the
S20-instance walk numbers (M0:1750-1755); the S24 deep-DEF instance
degrades at DE-bucket val 7.31e-2 = 33x its floor (M0:2047-2049) — a
different bucket scope and a number an order of magnitude smaller. The
correct instance-spanning statement is "certification degrades at val
far above the fold floor in every instance (0.61-0.86 at S20/S22; 33x
the tightest floor at S24)".

### R2 — "cheapest closure: a brick-1 ideal-march ceiling at the same (eps, thermo) turns outcome-II into (value, delta) verdicts"

**VERDICT: SURVIVES-WEAKENED.** The composition claim (pair dormant at
the engine rung; executable with committed bricks) is verified; the
cited PROOF SKETCH is the wrong lemma, and the bound needs a named
qualification list before any carrier could ship it.

Verified in the expert's favor:
- Grep claim TRUE at the letter: `J_ideal|bound[ _-]ladder` matches
  NOTHING in `validation/*.py` (re-run this pass; earlier hits are the
  `a1_ideal_march_jax` module NAME only). No GAP row, AC row, or C row
  of the S24 map covers a delta/globality field (all 36+16+45 read).
- D2.6 is a real anchor (M0:206 "[D-P] D2.6") and (iv) DECLARES delta
  against a ladder that ALREADY NAMES "sonic-capped J_ideal" as a member
  (M0:304-307) — so the expert's proposal is the executable carrier of
  an already-declared object, strengthening the "dormant, not absent"
  framing.
- The brick exists and is the right object: `a1_ideal_march_jax.py:2-5`
  — "IDEAL nozzle expanded to the exit Mach implied by eps", per-cell
  certified, exit Mach from eps via the leggeAree twin (:41-42), contour
  = the mdot bounding streamline (:49-53), same tabulated leaf.

Refutations/qualifications:

1. **The cited proof is insufficient as stated.** "Truncation only
   loses; the classical dF/dA argument on the supersonic branch"
   compares an ideal nozzle to a TRUNCATION OF ITSELF (that is the
   [T-GB] sharpening's use, M0:845-856). It does NOT bound a
   NON-UNIFORM-EXIT TOC design at the same eps. The ordering
   J_TOC(eps, L) <= J_ideal(eps) needs the FIXED-EXIT-AREA RELAXATION
   lemma: with the momentum theorem on {IVL, wall, axis, exit disk
   x = L}, J = Int_exit (p + rho u_x^2) dA − C_IVL with C_IVL
   W-independent (shared Sauer IVL data contract, `a1:37-40`);
   maximizing the exit integral over leaf states at fixed A_e = eps·A_t
   and fixed mdot gives, pointwise in the Lagrangian
   p + rho q^2 cos^2(theta) − lambda rho q cos(theta): theta = 0
   optimal GIVEN u_x > 0, and d/dq = rho (1 − M^2)(q − lambda), a
   maximum at the uniform supersonic root q = lambda — i.e. exactly the
   ideal march's uniform exit at Me(eps). This is a T-GB-STYLE argument
   restricted to fixed area (the "misalignment loses" + relaxation
   pieces of M0:830-855), not the truncation argument. It is provable
   inside the program's own hypotheses BECAUSE the certified class
   supplies u_x − c > 0 per cell (which kills the cos(theta) = −1
   boundary pathology AND pins the supersonic root, M > 1 pointwise).
   If R2 enters the record, this lemma needs its own M0 row with a
   rigor class; the advisory's parenthetical would not survive a
   referee.
2. **The length cap does NOT break the ordering — but it changes what
   delta MEANS.** The exit-plane argument never references L, so
   J_ideal(eps) >= J_TOC(eps, L) for every L: valid. But then
   delta = J_ideal(eps) − J_TOC upper-bounds the true gap to the
   CONSTRAINED global optimum J*(eps, L) while conflating it with the
   irreducible length-cap price J_ideal(eps) − J*(eps, L) > 0. Under
   D2.6's own form ("delta = B − J[S*], B = min of the bound ladder")
   this is a legitimate ladder member; the advisory's stronger sentence
   "the program cannot answer 'how far from optimal is the design you
   certified?'" is answered by this carrier only in the upper-bound
   sense, and any Verdict row must say "distance to the
   length-unconstrained fixed-eps ceiling", never "distance to global at
   (eps, L)".
3. **"Certified ceiling" needs its own bands.** The ceiling property is
   a continuum statement; the computed J_ideal is per-cell certified at
   the algebra level only. A conservative bound statement is
   J* <= J_ideal_true <= J_ideal_computed + (two-resolution band) +
   (eps-achievement correction): the ideal march STOPS at
   |M − Me| < 1e-5 and re-targets Me := achieved M (`a1:46-48`), and
   the lip/eps residual is finite (measured 4.4938e-3 at the twin,
   M0:1983-1984). An UNDER-estimated ceiling is anti-conservative for
   delta.
4. **The ceiling side inherits the throat-panel omission.** Both bricks
   evaluate J by trapezoid over returned wall points; the registered
   AUDIT finding `variational-driver:objective-omits-throat-panel`
   (see 5a below) applies to the ceiling evaluation too and must be
   repaired or banded BEFORE "outcome-II could ship as (value, delta)
   TODAY" is literally true. "Today" is a small overstatement: today
   plus one declared panel/band repair.
5. Same-(eps, thermo) is necessary but not sufficient: the comparison
   also requires the SAME IVL/mdot (holds — shared Sauer data contract)
   and the same leaf (holds — same tables); state these as hypotheses in
   the carrier.

### R3 — "the averaged structure has no executable carrier; mu enters executed code only at rung 1"

**VERDICT: SURVIVES-WEAKENED.** True as scoped to the averaged
OPTIMALITY structure and to numeric 2-D carriers; the flat "mu enters
executed code only at rung 1" is overdrawn against an executed, in-suite
carrier, and "the compositional risk is nowhere named" needs one
qualification.

- REFUTED at the letter: `validation/t3qs_sweep_protection.py` (run in
  the CI suite as item (xvi), `tests/run_all.py:56,:91`) is an EXECUTED
  carrier of a genuinely AVERAGED statement: the T3-QS proof chain
  P1-P6 verifies, EOS-general and with three rejectors (R1-R3 must
  fail detectably), that the first-order sweep correction's CYCLE
  INTEGRAL vanishes on the smooth part and reduces to the wave-passage
  jump residue (P6, `t3qs:32-34`) — an adjoint-weighted mu-integral
  statement, symbolic but executable and rejector-gated. It is not
  rung-1 quasi-1D code (`src/thrust`), so "only at rung 1" is false
  unless "executed code" is silently restricted to numeric field
  carriers. The accurate sentence: "the mu-averaged OPTIMALITY
  conditions (T7(b), (**'), VI.4 switch-splits, VI.4bis quadrature)
  have no executable carrier; the averaged DATA/correction structure
  has exactly one, symbolic ([T3-QS], suite item xvi), plus the rung-1
  numeric cycle machinery."
- SURVIVES: no carrier of T7(b)/(**')/VI.4bis quadrature exists
  anywhere in `validation/` or `src/` (checked by construction of the
  carrier inventory in the gap map + grep); every certified 2-D result
  is single-phase under the T0 -> T3/[T-T3-SI] license (M0:580,
  :644-651), which the expert credits correctly.
- WEAKENED on "nowhere named": the intersection-over-phases COMPOSITION
  is a registered reasoning pattern at rung 1 — [T-T4]'s proof runs on
  "the intersection over xi" of per-phase argmax sets and its Sharpness
  clause names exactly the breakage mode (length cap/base pressure ->
  "max Int < Int max STRICTLY", the mu-averaged corner condition, PB-2
  "THE FIRST GENUINELY AVERAGED SHAPE PROBLEM", M0:794-811). What is
  genuinely absent — and survives as R3's core — is the
  CERTIFIABILITY-side composition: K(xi) intersections, xi-indexed
  margin buckets/D'-analogs, xi-dependent crossing index, branch
  gradients under xi-dependent plan topology (Q3 a-c). No registered
  text poses those; T3-CONTROL (M0:734) is physics-side, as the expert
  says.

### R4 — "one model-class mismatch, twelve symptoms; every driver-side gap row is a symptom of this ONE mismatch"

**VERDICT: SURVIVES-WEAKENED.** The nonsmooth-class axis is real and
the GAP-1+GAP-2-first repair order is defensible (GAP-1's own SOTA row
cites MPCC/bundle machinery; GAP-19/27 explicitly couple to it). The
UNIFICATION as stated is rhetorical over-grouping with internally
inconsistent row lists:

- Row-list inconsistency (judge-quality, verified against the advisory
  text): the §1.3 R4 header cites {GAP-4, 13, 14, 15, 16, 17, 19, 27,
  31, 33} (10 rows); §2.5's "twelve symptoms" list cites {GAP-4, 2, 15,
  19, 16, 17, 27, 13, 14, 31, 12} (11 rows). GAP-33 appears ONLY in the
  header and is never argued; GAP-2 and GAP-12 appear ONLY in §2.5.
  Neither list has twelve members (twelve holds only if the [NEW]
  frac_bad note is counted in silently).
- Per-row adjudication against the gap map's own CLASS fields:
  * Squarely on the C^2-mismatch axis (4): GAP-2 (B-stationarity — the
    piecewise-smooth stationarity notion itself), GAP-27 (hard-min
    one-hot at derived rho — "RIGOR-GAP on the smoothness premise",
    :729), GAP-13 (discretely-moving crossing index vs smooth driver),
    GAP-19 (BFGS on ~rho/4 constraint curvature — the stiff aggregate).
  * Coupled/partial (4): GAP-4 (an R5 underived-constant defect whose
    BITE exists because outcome-II has no certificate — coupling via
    GAP-2, but the defect itself is tolerance hygiene), GAP-15 (an
    ADJUDICATION LAPSE, "NOT-SOTA/INCOMPLETE" :444 — the cold-restart
    COST is segmentation-induced, the defect is process), GAP-16 (the
    kink/seam FD risk half is on-axis, :466-467; the missing-rejector
    half is R5 hygiene valid for any smooth problem), GAP-17
    (EFFICIENCY-GAP :491; exposure couples to rho stiffness, defect is
    generic staleness).
  * Off-axis, misfiled under the unification (3-4): GAP-12 (multiplier
    rejector hygiene — R5 "every consumed number needs a rejector",
    :372), GAP-14 ("counted event != bounded event" bookkeeping
    invariant, :421 — needed under ANY problem class), GAP-31
    (record-keeping undercount on the log of record, :802-803), GAP-33
    (xtol literal — pure R5 constant, :812-815, and never argued by the
    advisory). A problem-class upgrade makes NONE of these four moot;
    the gap map already prices them as S25-cheap independently.
- Consequence for the repair-order claim: "after which most of the
  incremental hardening rows become either moot or cheap" — they are
  cheap ALREADY per the map's own OWNER/PLACEMENT fields; the honest
  claim is narrower: GAP-1+GAP-2 (with GAP-27's derived-budget clause,
  which GAP-1's surrogate would otherwise inherit, :741-742) upgrade
  outcome-II semantics; the hygiene rows proceed orthogonally.

### 5(a) [NEW, §2.4] "moving arc-sliver omitted from the objective, deterministic tilt in dJ/dtheta_B, not covered by any GAP row"

**VERDICT: FACT SURVIVES (re-verified at source); the [NEW] FLAG IS
REFUTED — this is a re-mint of a REGISTERED, VERIFIER-CONFIRMED audit
finding; and the magnitude framing is PARTIALLY CONTRADICTED by that
registered finding.**

- Mechanism re-verified at source this pass: arc stations run
  `for k in range(1, n_B + 1): th = thB * k / n_B`
  (`a1_toc_variational_jax.py:367-371`) — no theta = 0 station;
  `out["wall"]` stacks only station points (:386-415, :468);
  `thrust_J` trapezoids only supplied points (:953-960);
  `n_B = max(1, int(np.ceil(thB / da)))` (:233) — the ceil seam across
  records is real; the docstring DECLARES the sector "(0, theta_B]"
  (:23-24), so the coded domain [theta_1, theta_B] differs from the
  declared one even at fixed h. The tilt formula's structure
  (d(omitted)/dthB = p·2pi·y·rtd·sin(theta_1)/n_B > 0, deterministic
  sign) is correct.
- DEDUP REFUTATION: `validation/AUDIT_agnostic_2026-08-07.md:507-519`,
  finding `[CONFIRMED | medium | correlated-error]
  variational-driver:objective-omits-throat-panel`, contains the SAME
  mechanism, the SAME no-theta=0 evidence, the SAME derivative formula
  ("d(missing panel)/dthB ≈ 2π·p_throat·y·rtd·sin(thB/n_B)/n_B"), the
  SAME O3.1-blindness observation (AD and FD differentiate the same
  truncated J — correlated by construction), the SAME fix menu
  (add the analytic panel, or bound the bias into the derived KKT
  tolerance), PLUS a sub-finding the advisory MISSES: the Pa-drop
  declaration presumes the integral anchored at the constant throat
  area A_0, while the truncated integral's anchor A(theta_1) varies
  with thB — a registered caveat against the advisory's §1.2.3
  "theorem-level" wording (harmless at Pa = 0, live for any Pa > 0
  reading). The AUDIT is a registered artifact of record (S21 ingested
  it; the S24 gap map itself uses it as coverage authority in AC8/AC9),
  so the advisory's dedup duty — even as self-scoped to "the registered
  SOTA/rigor map" — is not discharged by checking the gap map alone.
  "Not covered by any GAP row" is literally true and misleading:
  covered by the registered audit, CONFIRMED-medium, currently unfixed
  (code unchanged at today's line numbers).
- MAGNITUDE CONTRADICTION: the advisory says the tilt is
  "order-of-magnitude 1e-4 relative to J at the twin instance, below
  every current discrimination band". The registered verifier note
  (AUDIT :519) computes the thB-GRADIENT-row bias at O(1e3) J-units
  against the O3 acceptance 10·gtol ≈ 9.3 of the S20 record — "orders
  of magnitude ABOVE the declared KKT tolerance". Both can hold
  (value-relative vs gradient-row), but the load-bearing comparison for
  a TILT is the gradient one, and there the registered number says
  ABOVE, not below. The advisory's LOW severity and "below every
  current discrimination band" understate the registered state (AUDIT
  kept it MEDIUM). Refuter-added precisions for the judge: (i) the
  omission is O(da^2) (theta_1 ≈ da) and da IS refined in the
  two-resolution protocol (`a1:88-93`), so the VALUE-side term is
  inside the Richardson measurement scope and vanishes in the h->0
  limit — it is a sign-deterministic truncation term, not a
  non-vanishing model bias; (ii) the F7 band of record is a
  CLASS-resolution band (K_RICH·|J_def(M) − J_def(2M)|,
  `def_twin_falsifier.py:1246-1272`), in which the sliver CANCELS
  (same cfg/thB both sides), and in the F7 difference J_last − J_def
  only the differential sliver between the two designs' thB enters —
  far below the 2.04e5 surplus: no S24 verdict moves; (iii) the twin's
  cross-code J comparison never existed (F7 runs the GENO
  representative "through the SAME objective", :1246-1247; GENO's own
  CF = 1.7285 is parsed for GENO-internal agreement only, :335), so
  the sliver has never faced a cross-code J oracle — if one is ever
  built (e.g. vs GENO CF integrating from theta = 0), the convention
  delta must be declared first.
- Fix adjudication: the advisory's two closure options are the audit's
  suggested test restated; "either is fine; silence is the only wrong
  option" — agreed, but the record has not been silent: it registered
  the finding thirteen months of sessions ago (2026-08-07) with a
  named test; the advisory should CITE it and inherit its magnitude,
  not re-mint at lower severity.

### 5(b) [NEW, §2.5] "frac_bad discontinuity of the G1 surrogate inside trust-constr; continuity declared only at frac_bad = 0"

**VERDICT: SURVIVES** (the strongest of the advisory's [NEW] items),
with two refuter precisions.

- Verified at source: `margin_governor.py:175-201` — `fin2` is a
  boolean lane mask; `n_fin = jnp.sum(fin2)` is an integer count;
  `frac_bad = (n_act − n_fin)/n_act` (:200) jumps by 1/n_act when any
  lane crosses finite/nonfinite as W moves, so the returned margin
  jumps by K_RICH·m_ref/n_act; identically in the S24 campaign variant
  `make_margin_fn_cs` with denominator n_sel
  (`def_twin_falsifier.py:640, :648`). The function is consumed by
  scipy trust-constr through the margin_factory NonlinearConstraint
  slot (`margin_governor.py:206-247`; gap map :81 ":1179-1182") — a
  genuine discontinuity inside the traced constraint the TR machinery
  models as C^2.
- The declaration state is exactly as the advisory says: the [X-MGOV]
  header declares "finite negative at every representable W,
  continuous at frac_bad = 0 (exact KS recovered bit-for-bit)"
  (`margin_governor.py:44-47`); M0:1800-1806 declares finiteness +
  exact-KS-at-zero-failures; NOTHING declares the jump across
  lane-failure boundaries.
- Dedup CLEAN (checked against the full registry): GAP-27 covers the
  one-hot gradient/curvature of the KS aggregate (a stiff-but-continuous
  axis); AC12 covers argmin-tie CHATTER; GAP-14 covers the crop
  denominator; C27's open axis is "conditioning", not set-membership
  discontinuity; the gap-map raws verified continuity AT zero only
  (`s24_gapv_constraints.md:270`). No registered row states this jump.
  The [NEW] flag is legitimate here.
- Refuter precisions: (i) the finding UNDERSTATES the mechanism — the
  KS term itself is computed over the CHANGING finite-lane subset, so
  ks_part jumps too when a lane enters/exits `fin2` (:193-199), a
  second channel of the same origin, plus the n_fin -> 0 fallback
  switch (:199) as a third; one clause should cover all three;
  (ii) "subsumed by GAP-1/GAP-2's repair" is plausible but not
  automatic — the G1 surrogate keeps its REQ-NONSTALL steering duty
  independently of the cert surrogate (M0:1783-1790 governor
  re-scoping), so the declaration clause is owed regardless of the
  GAP-1 outcome.

### 6 — Judge-quality findings on the advisory itself

1. **No file:line anchors anywhere.** Every mechanism claim (including
   both [NEW] items) is argued at function granularity with zero line
   anchors, against a house standard where the gap map anchors every
   row. For §2.4 this directly enabled the dedup miss.
2. **Dedup scope too narrow, and one miss found**: the advisory's
   declared dedup universe is the S24 gap map only; the repo's coverage
   universe demonstrably includes AUDIT_agnostic (the gap map's own
   AC8/AC9 rows adjudicate against it). One re-mint found (§2.4 =
   AUDIT `objective-omits-throat-panel`); the other [NEW] items checked
   clean (frac_bad; R2 composition; §2.1 IVL-envelope note is distinct
   from GAP-6/AC14 and was correctly kept separate).
3. **Instance-number conflation in R1** (0.61-0.86 attributed to three
   instances; S24's datum is 7.31e-2 DE-bucket at 33x floor) — see R1.
4. **Unbounded superlatives**: "the strongest of its kind this reviewer
   knows of in the nozzle-design literature" (twice, §1.4/§2.6) — under
   the repo's R5 novelty discipline these are non-citable as filed
   (no query bound); harmless as reviewer color, must not migrate into
   record docs.
5. **Internal row-list inconsistency in R4** (header vs §2.5 vs
   "twelve") — see R4.
6. Correctly-credited items verified this pass (stated for fairness):
   D2.6 anchor real; grep claim in R2 true; GAP citations in §2.3/§2.5
   accurate against the map (GAP-5/21/34, C-rows); the §1.2.4
   S22->S24 bucket-history reading matches M0:1926-1953; the
   frac_bad = 0 declaration quote is verbatim-accurate; T-T3-SI/T-T3-MAP
   crediting in §1.1 accurate.

---

## §2 CONVERGENCE TABLE

| # | Claim | Refuter verdict | Settled? | What a judge round must decide |
|---|-------|-----------------|----------|--------------------------------|
| R1 | No continuum object behind K; outcome-II = value + falsification data | SURVIVES-WEAKENED | YES on substance (record agrees with itself); wording repairs (a)-(c) of §1.R1 are mechanical | Nothing substantive; ratify the corrected wording ("no LIVE link FOR THE EXECUTED CLASS; bridge falsified; EQ-v2-A hypothesis-blocked at this class with named exits") |
| R2 | Ideal-march ceiling => (value, delta) at engine rung | SURVIVES-WEAKENED | Composition existence/absence SETTLED (grep + ladder declaration verified); NOT settled: proof obligation + delta semantics | (i) adopt the fixed-exit-area relaxation lemma (not dF/dA) as the carrier's proof obligation with an M0 rigor class; (ii) delta wording = "distance to the L-unconstrained fixed-eps ceiling"; (iii) sequence the throat-panel/band repair BEFORE the carrier ("today" -> "today + one declared repair") |
| R3 | Averaged structure carrier-less; mu only at rung 1 | SURVIVES-WEAKENED | YES with scope correction (T3-QS symbolic carrier exists, in-suite; T-T4 names the composition pattern at rung 1) | None; accept the re-scoped statement (optimality structure carrier-less; Q3's certifiability-composition genuinely unposed) |
| R4 | Twelve GAPs = one C^2 mismatch | SURVIVES-WEAKENED | NOT settled as filed | Fix the row set before it becomes a repair-order argument of record: on-axis {2, 27, 13, 19}, coupled {4, 15, 16, 17}, excluded {12, 14, 31, 33}; re-derive the "moot or cheap" consequence from the corrected set |
| 5a | Arc-sliver [NEW] | FACT SURVIVES / NOVELTY REFUTED / MAGNITUDE PART-CONTRADICTED | Novelty SETTLED against (registered AUDIT precedence, :507-519); magnitude NOT settled | Whether the registered gradient-side figure (O(1e3) vs 10·gtol ≈ 9.3, S20 units) or the advisory's value-side 1e-4 governs severity — decidable by the audit's own suggested test or the S25 arithmetic, no argument needed; then file as the AUDIT row's discharge, not as [NEW] |
| 5b | frac_bad discontinuity [NEW] | SURVIVES | YES (dedup clean, mechanism verified, declaration gap real) | Only registration form: one clause covering all THREE jump channels (frac_bad, KS-subset, n_fin=0 fallback), owner with/independent of GAP-1 |
| 6 | Judge-quality | — | Anchors/dedup-scope/superlatives: SETTLED findings | Require anchors + AUDIT-inclusive dedup in any second pass |

Bottom line of the table: 0 claims REFUTED outright at the substance
level; 4 SURVIVES-WEAKENED (R1-R4); 1 SURVIVES clean (5b); 1 split
(5a: fact yes, novelty no, magnitude contested). The advisory's two
"most important" [NEW] findings split exactly: (b) is its best content,
(a) is its worst process failure.

---

## §3 NOTES FOR THE JUDGE ROUND (narrow, pre-formulated)

1. R4 row set (the only genuinely open ARGUMENT): does the unification
   claim survive with the corrected 4+4 set, and does the repair-order
   corollary survive once the excluded rows are priced independently?
2. R2 proof obligation: ratify the relaxation-lemma requirement and the
   delta semantics; decide whether the carrier waits for the
   throat-panel repair (refuter: yes — the ceiling side is
   anti-conservative without it).
3. 5a disposition: file the §2.4 content as a DISCHARGE INPUT to AUDIT
   `variational-driver:objective-omits-throat-panel` (which already
   owns the test), severity inherited MEDIUM until the gradient-vs-gtol
   arithmetic is done at the current instances; strike the [NEW] flag.
4. R1/R3 wording repairs: mechanical; no disagreement left to argue.

*Refuter position, Form-2 round 1, read-only. Every verdict above is
anchored; any judge overrule should cite an anchor this file missed.*
