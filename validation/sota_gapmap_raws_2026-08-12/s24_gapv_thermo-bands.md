# S24 GAP VERIFICATION — FACET 6: THERMO CLOSURE + TOLERANCE/BAND CULTURE
**Verifier key**: thermo-bands · **Date**: 2026-08-12 (S24 window) · **Stance**: adversarial, default-REFUTED
**Finder position verified**: `s24_gap_thermo-bands.md` (read in full)

## Method (declared)
- Every file:line citation re-read at source (a1_ideal_march_jax.py, thermotab_c1_jax.py,
  a1_toc_variational_jax.py, margin_governor.py, margin_tolerance_backoff.py,
  adaptive_knot_optimize.py, locus_diagnosis.py, def_twin_falsifier.py, o32_mesh_convergence.py,
  o33_bench.py, numeric_allowlist.json, brick2_kickoff.md, AUDIT_agnostic_2026-08-07.md,
  ADVISORY_S24_thermo_closure_survey_2026-08-12.md, PROGRESS.md R23-R27, D6 plan, D4:215-219,
  M0:1295-1299, S24 log PROGRESS_2026-08-12_S24_f1b.md steps 1-2, 6, 9-10, 14-15).
- Probes RE-RUN by me: **P2** (`probe_band_models.py`, <1 s — reproduced exactly: 11.2%, 1853x,
  2.11x, threshold 0.3219) and **P1** (`probe_box_clamp.py`, 11.5 s wall on this run — every
  number reproduced exactly: 34.836 K, q_max = 3467.436 m/s / M 5.006, eps_box = 102.83,
  margins 1276.80 / 454.46 / 216.29 / 8.34 K, T_c1(1.05 q_max) = 863.2043 K with
  dT/dq = +5.4531e-1, edge physical slope −1.9359, dT/dq(1.02 q_max) = −1.2069e-1).
- Coverage cross-checked against: advisory C-A..C-D (§8), PROGRESS R23 (C-D registered, owner F2),
  R25 choice-ledger rows ("mesh AMR/DWR (F2)"; "universalita' K_RICH=4 (F2 audit)"), R26 (this
  gap-map in-flight), D6 tool-matrix ("DWR goal-oriented estimates" :740, :455), S24 panel
  conditions C1-C10 (log step 10), AUDIT findings F3 (:388-400), F5 (:416-428), F8 (:458-470).

---

## G1 — Box exit silent in both closures; C1 fails worse than the clamp
**VERDICT: DOWNGRADED (MEDIUM)** — measurement stands; the novelty claim vs the audit is REFUTED.
- Citations real and accurate (a1:350-353 jnp.interp clamp; thermotab:144 clipped searchsorted;
  :189-197 invert_h fixed 8 trips). All P1 numbers independently reproduced (see Method).
- **REFUTED sub-claim**: "the C1-branch extrapolation mode is a NEW datum not in the audit text"
  and the anchor characterization "AUDIT:386-398 (C-D, linear clamp only)". FALSE: AUDIT F3
  explicitly covers the C1 mode — ":394 'The quintic path is worse in the opposite direction:
  _locate clips the interval index, so outside the grid the quintic EXTRAPOLATES polynomially
  without bound and invert_h iterates on it'", repeated in the evidence (:396) and verifier note
  (:400). Both failure modes are already in the finding of record.
- **What survives (genuine sharpening of C-D)**: (i) the MEASUREMENT is new — sign-flipped,
  plausible-magnitude gradient (+0.545 vs physical −1.94; −0.12 at 1.02·q_max = 16x too shallow),
  proving a frozen-T/zero-grad detector spec'd on the clamp mode misses the C1 mode; (ii) the
  advisory's C-D RESTATEMENT (§8: rejector "for the silent clamp at T_TAB_LO/HI with dT/dq = 0")
  narrows the audit finding to clamp-only — a rejector built to that restated spec would pass the
  C1 branch. The C-D spec correction ("both modes") is a legitimate delta to a named conditional;
  owner stays F2, no new row minted.
- Severity MEDIUM, not HIGH: no verdict/record number is affected today (exit-T margins 1276.8 K
  at eps = 4, ~350-450 K class at defnoz eps = 30; nothing fired). Extremal cases (a)-(c) are
  plausible and consistent with the P1 eps_box = 102.8 datum.

## G2 — Table box literals; no per-case q-range margin certificate
**VERDICT: CONFIRMED (MEDIUM)** — with the overlap made explicit.
- Citations real: a1:142-143 literals (N_TAB = 8192, 1050/3900); thermotab:31-32 the
  contains-every-realized-state hypothesis. No enforcement anywhere: AUDIT F3 grep of record
  (run_march/run_scan/make_run_scan_jit) + my grep of a1_toc_variational_jax.py for
  T_TAB_LO/T_TAB_HI/box = EMPTY (run_toc_record/run_toc_scan have no box check either).
- Measured margins reproduced exactly, including the two honest tight ones: stagnation margin
  **34.836 K** (undeclared anywhere) and **8.34 K at eps = 100**.
- Coverage check (the reason this is NOT a duplicate): C-D is a DETECTION rejector at box exit;
  C-C is fit-JOINT census; neither is a derived-box or per-run margin certificate. The
  hypothesis-without-rejector half is AUDIT F3 content (overlap declared); the case-envelope
  derivation + box-margin Verdict row is new actionable content and sits squarely under the
  standing generality directive (case-independent procedures). SOTA attribution (envelope-driven
  table generation, unification with C-C's ingest path) is fair.
- Severity MEDIUM: coverage/generality; no current record number wrong.

## G3 — K_RICH = 4 universal across >= 7 roles, derived in 1
**VERDICT: DOWNGRADED (MEDIUM)** — census verified fact-by-fact; already a registered open row;
one headline number corrected.
- All eight role citations verified at source (a1:145,1110; a1:1338-40 + a1_toc:1480-82;
  margin_governor:25-29; margin_tolerance_backoff:147; a1_toc:1403 + adaptive_knot_optimize:362;
  locus_diagnosis:276; brick2_kickoff:263-278 K_prac = 4 "reused, not invented";
  thermotab_c1:359 G-floor; allowlist:754 S_BAR note = the only quantitative rationale).
- **Already registered**: PROGRESS.md R25 open choice-ledger row "universalita' K_RICH=4
  (F2 audit)" — the finder admits it sharpens, does not mint. Under the verify criteria this
  cannot stand as a NEW gap; it stands as a sharpening ANNEX to the registered row (role census +
  per-role coverage statement are genuinely new quantitative content for that row).
- **CORRECTION to the headline threshold**: the deployed bands protect the COARSE member
  (contour_compare bands y_h at r = 1 vs GENO, a1:1106-1111; band_u bands u1, a1_toc:1420-21),
  so the coverage ratio is K(1 − 2^−p) and under-coverage begins at **p < log2(K/(K−1)) = 0.415**,
  not the fine-member 0.3219 the finder headlines (that formula K(2^p − 1) applies to the h/2
  member, which is not what the bands certify). The probe's own NOTE line ("always >1 for K=4,
  model valid") is mathematically false below p = 0.415. Net effect: the finder's concern is
  slightly STRONGER than stated, but the number of record for the annex must be 0.415.
- Role-4 caveat: L_TB's two-point sup is labeled "measured-sup surrogate" in the code and the S23
  [X-TBAK] ratification carries a demonstrated-firing falsifier — a DECLARED surrogate, not an
  undeclared gap; the census may list it only with that label. Role 3 (rho) the finder itself
  concedes is a derived ratio. The truly underived reuses are roles 5-7 (+ 8).
- Severity MEDIUM (sharpens a registered F2-audit row; no verdict shown wrong today — the p of
  record where measured is 2.5347).

## G4 — Pointwise two-resolution bands invalid across plan-topology flips
**VERDICT: CONFIRMED (MEDIUM)** — with two mandatory quoting caveats.
- Citations real: contour_compare a1:1099-1117 (raw e(x), no topology check); band_u
  a1_toc:1415-1427; o33_bench:96-106 band declaration; LB-c2 topology monitor EXISTS only in
  o32:545-557 and is wired into no band row (verified by reading all three band sites). DWR
  already named at D4:217, M0:1297, D6:740 and open row PROGRESS:247 — finder cited all honestly.
- P2b re-run reproduces 11.2% / 1853x / control 0-out. **Caveat 1 (quoting rule)**: P2b is a
  TUNED synthetic model — the stratum amplitude is chosen comparable to the smooth 0.75·C·h² term
  to reach the cancellation regime (the finder's own two failed parameterizations show the regime
  is not generic). The numbers demonstrate the MECHANISM; they are not repo measurements and must
  never be quoted as coverage failures of the bands of record.
- **Caveat 2 (partial in-repo precedent, strengthens actionability)**: the repo already KNOWS the
  isolated-zero-crossing collapse and CURED it at one site — a1_toc:1701-1712 applies a running
  max over adjacent samples on e_repr ("a POINTWISE band collapses and K_RICH x ~0 protects
  nothing") — the cure exists in-house and is simply not applied to contour_compare/band_u/o33
  field bands. Likewise the S24 panel condition C3 (mask self-consistency gate, i_cross drift
  folded into the F2 band, CONFOUNDED rungs excluded) already implements topology-conditioning
  for the ladder — precedent, not coverage of the band rows.
- Genuinely a gap: the PASS of record (62/62, 0/98) is conditional on an unchecked
  topology-consistency hypothesis, and the machinery to check it (LB-c2 census, running-max
  envelope) already exists. The [X-AKNO] skip-rule and defnoz wall-search extremal cases are
  real code paths (adaptive_knot_optimize:39-42 verified; S23/S24 wall-search re-record lesson
  of record). Eça-Hoekstra / DWR attributions correct.
- Severity MEDIUM (conditions verdicts of record on an unchecked hypothesis; no demonstrated
  in-repo under-coverage).

## G5 — Newton-floor constants are conventions; unit-mixed z-scale
**VERDICT: DOWNGRADED (LOW)** — fully registered content; the "additional" claim is REFUTED.
- Citations real (a1:145-147, :85-86 "spike factor convention"; thermotab:85; a1_toc:1434 and
  a1_march_scan:842 x10; a1:393 sc). The prescribed halved-constants sensitivity test is indeed
  never executed (grep over validation/ + docs/ = no execution artifact).
- **REFUTED sub-claim**: "Structural addition beyond the audit: the certification scale
  sc = max(1, max|z|) ... unit-mixed". AUDIT F8 `engine-core:F8-cert-scale-unit-mixing`
  (:458-470) IS this finding — same single-scalar-over-[x4,y4,u4,v4] point, same ~3
  orders-of-magnitude figure, same tol_eq propagation — and its verifier already adjudicated
  severity LOW with mitigating grounds (max-norm bound still valid; contour bands dominated by
  the Richardson estimate; no verdict-bearing check compromised).
- Additional accuracy debit: listing C_OPS = 100 as bare "repo convention" was already partially
  refuted inside the audit itself (F5 verifier note: op-count sketch "quintic evaluation,
  ~64 flops -> C = 100" at thermotab:38-40 — weakly derived).
- What survives: the S25 registration "execute AUDIT:426 exactly (halved-constants sweep +
  component-scaled z-metric)" — a scheduling nudge on two registered audit findings (F5 + F8),
  legitimately >30 s so not runnable in this pass. LOW (hygiene/scheduling; nothing new minted).

## G6 — No declared band-composition rule (sum vs max vs mixes)
**VERDICT: CONFIRMED (MEDIUM)**.
- All sites verified at source: SUM a1:1338-40, a1_toc:1480-82 (and yes, K_RICH multiplies the
  64-eps floor in contour_compare:1110 — category-mixing, conservative direction); MAX
  def_twin_falsifier:380-381 (band12) and :404 (band_dprime); heterogeneous unweighted sums
  :1122-1124 (band_f1 = K·dgeno + ye_res + rep + band_dprime), :1146-47 (max + drift), :1167-69
  (K·|Δd2| + Newton floor·cert_n). No composition policy exists anywhere (grep for
  GUM/RSS/composition over allowlist + M0 = chemistry hits only).
- P2c arithmetic verified trivially (re-run): K·max covers a+b by 2.11x when a ~ b; the intended
  4x is silently halved exactly when both mechanisms contribute. GUM JCGM 100:2008 / ASME V&V
  20-2009 attributions correct.
- **Honest datum to attach**: at the S24 numbers of record the max-composed D' band was dominated
  19:1 (cell = 3.03e-3 vs ds_land = 1.581e-4, log step 6), so no verdict of record is touched
  today — the extremal case (a) (cell ~ ds_land at a deep-DEF landing near a cell boundary) is
  the live risk. Fix correctly sized by the finder (one-paragraph declared policy + pass over
  the max sites). MEDIUM.

## G7 — Asymptotic-range hypothesis undeclared at band sites; o32 NON-CONCLUSIVE not propagated
**VERDICT: CONFIRMED (LOW)** — one severity notch below the finder.
- Citations verbatim-verified: o32 header :60-75 (S19 row of record RE-REPORTED NON-CONCLUSIVE,
  p_fine = 2.5347, dp_tot = 0.6704, pre-registered 0.5 cap, S21 re-adjudication text) and the
  observed_order estimator exists (o32:151-158+) — reuse-not-build is accurate. No band row
  carries or references an order check (consistent with all band-site reads above).
- Coherence gap real but mild, as the finder itself says: the binding S16 one-sided rule left the
  h^2 claim NOT killed, the coarse-member coverage at p >= 2 is 3x, and the NON-CONCLUSIVE
  verdict concerns the registered-norm field claim, not the band functionals themselves. The
  declaration ("band presumes asymptotic range; site order unverified") plus the cheap
  third-resolution GCI lever is a sound S25 registration. Threshold correction from G3 applies
  here too (0.415 coarse-member, not 0.3219). LOW.

## Drops audit (finder's 3 declared drops)
1. G-floor grid audit — drop LEGITIMATE: declared in-file with named substrate (thermotab:31-35,
   "declared: not an interval certificate ... PAP-GMAX"). Verified.
2. q-scan flux-window fallback — drop LEGITIMATE: AUDIT:448-456 confirmed (registered finding,
   Newton seeding, outside facet); the G2 credit note is accurate (the audit's own suggested fix
   :454 derives the scan window "from the table box (q_max from h0 - h(T_TAB_LO))").
3. o33 structural discriminators — drop LEGITIMATE: o33_bench:96-106 confirms the S21 honesty
   rewrite (declared-not-derived, P2-scheduled).

## Counts
- **CONFIRMED: 4** (G2 MEDIUM, G4 MEDIUM, G6 MEDIUM, G7 LOW)
- **DOWNGRADED: 3** (G1 MEDIUM — novelty-vs-audit clause refuted, measurement + C-D spec
  sharpening survive; G3 MEDIUM — registered-row sharpening only, threshold corrected to 0.415;
  G5 LOW — fully registered in AUDIT F5+F8, only the S25 execution registration survives)
- **REFUTED outright: 0** findings; **3 refuted sub-claims** (G1 "not in the audit text";
  G5 "structural addition beyond the audit"; G3/P2b-note "always >1 for K=4" + fine-member
  threshold as headline).
- **HIGH: 0** — no finding affects a verdict or record number as of today; every measured margin
  of record re-verified comfortable at the executed instances.
- Cross-cutting correction for the annex of record: the under-coverage threshold at the deployed
  (coarse-member) band sites is **p < log2(4/3) = 0.415**.
