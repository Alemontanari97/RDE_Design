# REFUTE_C28 — adversarial refutation of PANEL_C28 (Blocco 3, wave 1)
S-FOUNDATIONS-C2, 2026-08-19. Refuter of record for cluster C28 (single row).
Inputs read IN FULL: BASE/blocco3/PANEL_C28.md; BASE/blocco3/BRIEF_wave1_panels.md
§0+§C28; anchors re-read AT SOURCE (list in the audit declaration). BASE =
validation/sfoundations_raws_2026-08-13. No file outside blocco3/ edited; env
pinned; no git mutations (read-only `git ls-files`/`git log` used as measurement
commands only).

**Overall posture.** The panel's proposed row outcome — CONVERGED-panel with
measurement-gated SPLIT, hybrid (d) with the GAP-1 KS-max instantiation of (b),
incumbent SUPERSEDED-as-sole-representation but RETAINED as absolute verifier,
adoption capped at ADOPTED-FOR-MEASUREMENT behind a named F2 duty — SURVIVES
this refutation on content. No finding below breaks the verdict. Three findings
are REPAIR-NEEDED (a misfiring falsifier pin, an evidence-status inflation
repeated three times, and a census family missing against the §0.2
no-loss-by-omission rule — all repairable in the panel text with the record
already in hand); five are AMENDMENTS; three NOTES. The heavy machinery checked
out: every M0 anchor (K-definition :1990-2011, ladder+KKT-with-margin-multiplier
:2111-2185 incl. :2126-2132/:2155-2157, taxonomy :2164-2177, O1 :2256-2259,
X-VMON :2222-2238, O4+bridge-falsification :2285-2335, X-MGOV :2336-2353),
every tree quote (V-F32/H-F24/O-F20/P-F33), the diff anchors (:143-155,
:347-350), GAP-1/GAP-2 (:65-105/:107-139), the facet long form, the four
registry dedup greps, and the ledger row :419-427 verified verbatim or
verbatim-compatible at source. Census spot-checks: arXiv:2605.29757 and
arXiv:2501.07383 exist and the disjunctive-MPCC one-liner ("outperform
Kanzow-Schwartz and Scholtes at high accuracy") is SUPPORTED by that paper's
own abstract (fetched 2026-08-19) — that inflation candidate was hunted and
DROPPED.

---

## FINDINGS (per-row; the cluster is the single row C28)

### RC28-1 — REPAIR-NEEDED — pin F-3 as written is a misfiring falsifier (duty e, d/R-4)
**Claim attacked.** F-3: "on the mild S18 instance the surrogate must be
strictly inactive (μ_c = 0) and the walk bit-comparable to the record; any
drift kills the zero-cost-far-from-frontier claim and re-prices the choice."
**Mechanism.** Adding ANY inequality constraint switches scipy trust-constr
from `equality_constrained_sqp` to `tr_interior_point` — measured of record on
the installed scipy 1.18.0 (facet Probe C, s24_gap_driver-nonsmooth.md:36-39:
`if canonical.n_ineq == 0: method='equality_constrained_sqp' else:
method='tr_interior_point'`; findings row `driver-nonsmooth:ip-path-unadjudicated`,
docs/findings_registry.yaml:1239: "any inequality switches the method").
The recorded S18 mild walk predates S22 and is equality-only ⇒ SQP path. The
F-3 walk carries the KS-max inequality ⇒ IP path: a DIFFERENT algorithm with
cold barrier restarts, and even against a margin-armed IP baseline the extra
constraint row changes the barrier subproblem (extra slack + log-barrier term
perturbs every iterate at O(μ_barrier/slack) ≠ 0). In this repo
"bit-comparable/bit-identical" is literal (M0:2290, certdiag 30→300
bit-identical, M0:2058-2062). Therefore F-3 fires GENERICALLY on the
engine-path switch, refuting nothing about pricing cost — a falsifier whose
firing does not discriminate the hypothesis it is pinned to. The threshold is
not derived; it is the gapmap's own unmeasured prediction (gapmap :91-92,
facet :109-112 "walk bit-comparable to today's") transplanted into a binding
pin without recalibration — R-4, and internally inconsistent with the panel's
OWN risk (4) (IP-path permanence, §3.2) and with its own duty carrying
[P-IPADJ] "on the same critical path".
**Named repair (outcome unmoved).** Re-pin F-3 at MATCHED engine
path/constraint-set: baseline = the same walk re-run identically except the
cert row (same scipy method, same constraint count minus one, or governor-armed
IP-vs-IP A/B per the [P-IPADJ] option in findings :1243); pass criterion =
μ_c = 0 strictly at every accepted iterate AND J/step-count/record-count deltas
inside the existing derived bands (bitwise only where the path is provably
identical); route the path-switch delta itself to [P-IPADJ], which the duty
already names. With this repair F-3 becomes a genuine cost falsifier and the
gated split stands unchanged.

### RC28-2 — REPAIR-NEEDED — "Probe B ... (committed)" is false of record, stated three times (duty b inflation, R5)
**Claim attacked.** §3.1 "Probe B Arm 1 (committed, analytic toy, :93-96)";
§3.2 "Probe B Arm 2 (committed)"; §4 "(Probe B is an analytic toy, committed;
census gives no precedent to lean on)".
**Witness.** The facet declares the probes ran as "pure python/scipy in the
scratchpad" (s24_gap_driver-nonsmooth.md:23-25; Probe B =
`probe_B_frontier_kkt.py`, :28). Measured this window: `git ls-files | grep -i
"probe_b\|probe_B"` → 0 hits; tracked probe scripts are only
gamma_cycle_probe.py / test_gamma_probe.py / acontraction_front_probe.py;
validation/sota_gapmap_raws_2026-08-12/ contains .md files only. The gapmap
itself never says "committed" — it says "measured — Probe B (analytic toy,
both verifiers reproduced)" (:93). What is committed is the ADVISORY carrying
the numbers, not the script. Under R5 ("no numbers without committed script +
test") the label is load-bearing: the panel launders scratchpad-probe numbers
(4.6e-11, μ=0.709, 2.9e-3, 7.1e-2) into committed-carrier status inside the
verdict text, while its own inflation check asserts "every number carries its
committed anchor".
**Named repair (outcome unmoved).** Relabel everywhere: "scratchpad-run,
reproduced by both S24 verifiers, numbers carried in the committed advisory
(gapmap :93-96; facet :28-35)"; and add to the F2 duty that the [P-CERTKS]
pilot commits its own carrier+test before any Probe-B-class number enters a
Verdict. The verdict already caps adoption at toy-probe evidence, so the gated
split stands after relabeling; left unrepaired, the C28 ledger row would
inherit a false provenance claim.

### RC28-3 — REPAIR-NEEDED — a modern representation family is missing from options AND census: adaptive-accuracy/inexact TR-SQP (duty b census completeness; §0.2 "an option loses only by STATED REASON, never by omission")
**The missing line (named, search-proven this window).** Treat the solver's
certification/accuracy demands as CONTROLLED INEXACTNESS inside a globally
convergent TR-SQP — implementable accuracy criteria per iterate, refine when
and where needed — instead of constraining W away from bd(K): Ziems–Ulbrich,
"Adaptive Multilevel Inexact SQP Methods for PDE-Constrained Optimization",
SIOPT 21(1):1-40 (2011), doi 10.1137/080743160; control-constraint sequel
SIOPT doi 10.1137/110848645; inexact TR-SQP-filter, COAP (2015) doi
10.1007/s10589-015-9793-x; Kouri–Heinkenschloss inexact-evaluation TR lineage.
Applied to frontier (ii) it reads: adapt NEWTON_TOL_FACTOR·ε·scale demands
and/or the N_NEWTON budget along the walk so the "frontier" moves with the
optimizer — a fifth representation (e), distinct from (a)-(d). None of the 7
census queries touches it (q5 is failure-penalization, not accuracy control);
no census axis and no §3.5 closure row names it. As the panel stands, this
family loses by omission, which the mandate §0.2 forbids.
**Named repair (record-closable now, outcome unmoved).** Add the axis + a
§3.5 row 9, CLOSED by stated reason already of record on both halves of
K = K_phys ∩ K_budget (M0:2005-2011): (i) the tolerance half is a CERTIFICATE
— "the certification floor is a tolerance and does not move" (M0:2010-2011);
the honesty frame makes floor-relaxation non-negotiable (facet :18-21) — so
the inexactness road may never touch it; (ii) the budget half is EXPLICITLY
the only enlargeable half, and the record MEASURED enlargement to be
non-binding at the frontier instances: certdiag 8/8 GENUINE — every rejection
bit-identical under N_NEWTON 30 → 300 with the floor untouched (M0:2058-2062;
brief §C28 "certdiag 8/8 genuine"). The road targets exactly the two dials
the record pins; it is admissible at most as F2 budget-scheduling economics
OUTSIDE the verdict loop. Stating this costs four sentences and makes the
census claim "no source ... prices a marched solver's per-cell
Newton-certification ratio" robust against the obvious referee counter
("the inexact-SQP school handles solver-accuracy limits differently").

### RC28-4 — AMENDMENT — conservatism gap understated by up to 2× for the adopted shifted form (duty e thresholds; d/R-4)
§3.2 risk (2): "the derived-ρ discipline bounds the gap at ln(N)/ρ =
s_min/K_RICH". Derivation against the adopted form: with
max_i r_i ≤ KSmax_ρ(r) ≤ max_i r_i + s, s = ln(N)/ρ (facet :72-73), enforcing
KSmax ≤ 1 − s guarantees kept-designs only for max r_i ≤ 1 − 2s (excluded ⇒
KSmax > 1−s ⇒ max r_i > 1−2s), so the certifiable-but-possibly-excluded band is
max r_i ∈ (1 − 2s, 1] — worst-case width 2·ln(N)/ρ, not ln(N)/ρ. The stated
gap=s is the KS-MIN governor's bound (M0:2338-2339, no shift) transplanted
onto the SHIFTED KS-max constraint without recalibration. Note the unshifted
form KSmax ≤ 1 is ALREADY sufficient (max ≤ KSmax ≤ 1) with band width s —
the −s shift buys the robustness F-1 leans on ("gate never fires on accepted
iterates") at the price of the second s. Repair text: state the ≤ 2·ln(N)/ρ
band (or adjudicate shift-vs-no-shift explicitly), and have duty item 2 report
the REALIZED exclusion band at the frontier-class walk. Outcome unmoved: cost
still vanishes far from the frontier and the F2 duty measures the real gap.

### RC28-5 — AMENDMENT — stale code/doc anchors presented as current (duty: mis-cites; SR-12 spirit)
Measured this window against the tree at HEAD: the P4 gate is at
a1_toc_variational_jax.py:~1520 ("P4 gate: record at segment base not
certified"), NOT :935-938 (those lines are the build-time safe-where dummy
certification check); P3(ii) accepted-iterate gate is at :1849-1867, NOT
:1158-1161 (an engine-cache key block); margin_factory is at :1257 (signature),
:1346 (doc), :1912-1913 (consumption), NOT :1179-1182 (= thrust_J);
proximal-bundle in D6 is at docs/rde_nozzle_development_plan.md:743, NOT :738
(and "Kiwiel" does not appear in D6 — the name rides the facet). All inherited
from the S24-era gapmap/facet written before the S25/S25-bis driver rewrite
(commits 1806ae2/8046434/ea2abce touched the file 2026-08-13). Every named
OBJECT exists exactly as described — anchor fix only, in §1(a), §3.2
(margin_factory slot), §3.5.6, §4. When quoting the gapmap AS the gapmap, keep
its line refs but tag them "(gapmap-era lines; current sites: ...)".

### RC28-6 — AMENDMENT — census recency compliance sentence false for axis 1 (duty b recency honesty)
"Every census axis reaches ≥ 2023" — axis 1's newest cited item is the
parallel-adaptive-kriging paper, AIAA Journal Vol. 59, 2021 (doi
10.2514/1.J059915; verified by search this window); the rest of the axis is
1979/2007/~2015/2018. Axes 2-5 do reach 2023-2026 as claimed. Repair: correct
to "axes 2-5 reach ≥ 2023; axis 1 (aggregation family) newest = 2021 here —
its modern refinement layer is C27's mandate (interplay already named)", or
add a ≥ 2023 aggregation source. The modern-refined-literature requirement is
otherwise genuinely met where this panel's verdict leans (axes 2-4).

### RC28-7 — AMENDMENT — cava grep count wrong: 5 hits, not 3 (SR-12)
Panel §2: "`C28` → 3 hits (lines 36, 854, 1231)". Measured this window:
`grep -n "C28" validation/ADVISORY_litreview_confrontation_2026-08-13.md` →
FIVE hits: 36, 854, 1116, 1231, 1245. Line 1116 is the cava's own C28
correction row itself (base-drag three-magnitudes separation) and 1245 is
D-50 (Harroun G-d downgrade application list naming C28). Both are the same
numbering-collision family the panel identified; the CONCLUSION ("the ratified
cava contributes NO row to this cluster") survives on all five hits — the
count and line list must be corrected. A declared measured grep with a wrong
count is exactly what SR-12 exists to prevent.

### RC28-8 — AMENDMENT — "already past that trigger" over-states O-F20's falsifier condition (duty c fairness to the re-scoped alternative)
§3.3: "the measured record (three campaigns pinned ON the true frontier) is
already past that trigger". O-F20's trigger is "inner-region optimum presses
the provable boundary with POSITIVE MULTIPLIER" (:1129-1133): no provable
inner region was ever derived, and no multiplier of record exists — O1 is OPEN
and μ is UNDEFINED until discharged (M0:2256-2259), a qualifier the panel
itself carries everywhere else. The trigger as stated was never evaluated;
what the panel has is an a-fortiori INFERENCE (walks pin on bd(K) itself, so
any conservative inner approximation of K would a fortiori be pressed).
Rewrite as inference, not measurement. Outcome unmoved: the re-scope of (c)
stands independently on S22 (v)/(vi) (bd(K) is a numerical-class boundary
invisible to physical-region reasoning, M0:2318-2335), which is measured.

### RC28-9 — NOTE — taxonomy class mislabeled vs the M0 anchor cited in the same sentence
§2 axis 2: "certification-type constraints = Nonquantifiable-Unrelaxable-
Simulation(-Hidden), 'the worst kind'". M0:2167-2171 (the anchor the sentence
cites as confirmed) registers the class as Known-Unrelaxable-Simulation-
NONQUANTIFIABLE — Known, not Hidden (the constraint's existence is known; only
its value is revealed post-march) — and the quoted phrase of record is "the
worst TRACTABLE kind". The "(-Hidden)" gloss imports the census umbrella term
into the class string and the dropped word weakens the M0 sentence's point.
One-line wording fix in the census; no consequence for the adjudication (the
remedy "quantify a margin" is identical).

### RC28-10 — NOTE — the panel under-uses pipeline-sense R1; the ledger note it corrects is itself mis-glossed
ADVISORY_S25_pipeline_sense_CONVERGED_2026-08-12.md:191-199 not only carries
'"no successor quantifier exists", GAP-1' (a QUOTE of GAP-1, scoped to the
set-level bridge) — the SAME sentence names "GAP-1's in-KKT certification
surrogate" among the NAMED EXITS. So the proposed row edit ("stop reading 'no
successor'") is not merely consistent with the record: it is already
half-written in the very advisory the current ledger note cites; and that
ledger note's gloss ("adjudicates no alternative representation",
choice_ledger.yaml:427) is imprecise against its own source. When F2 executes
the row edit, quote R1's full sentence — it converts the crux ("the ledger
lags M0") from panel assertion into record.

### RC28-11 — NOTE — P-F33's boundary-ambiguity falsifier not carried into the pins
P-F33's falsifier ("champion's certifiability margins at optimum sit inside
their own error bars → the certificate is boundary-ambiguous and must say so",
phaseA_tree_propulsion.md:1210-1212) is the one tree falsifier with no
counterpart among F-1/F-2/F-3 or the reporting pins. It is C38-adjacent
(outcome-declaration semantics; C38 named as interplay, correctly not decided
here) — cheap to add at F2 as a reporting pin: μ_c and KSmax at the returned
base ship with their derived bands, and a base whose surrogate-active margin
sits inside its own band is declared boundary-ambiguous, not optimal.

---

## VERBATIM-QUOTE AUDIT DECLARATION
Spot-checked at source this window (2026-08-19), quote-bearing sites first:
- Trees: phaseA_tree_variational.md:1373-1411 (three quoted phrases + falsifier
  — VERBATIM, incl. "arguably the most distinctive structural choice of the
  whole formulation"); phaseA_tree_hyperbolic.md:774-795 ("a certificate is
  not tradeable" :782-783; multiplier-prices quote :788-791; LICQ falsifier
  :792-795 — VERBATIM); phaseA_tree_optimization.md:1095-1133 ("constraint
  with values, not a boolean" :1102-1103; extreme-barrier :1096-1098;
  "never a certificate" :1107; falsifier quote with honest ellipsis
  :1129-1133 — VERBATIM); phaseA_tree_propulsion.md:1192-1212 ("grind or lie"
  :1209, "optima live ON boundaries" :1208 — VERBATIM).
- Diff: phaseB_tree_diff.md:143-155 + :347-350 ("the strongest single
  methodological validation in the diff" — VERBATIM).
- M0: :1990-2011, :2111-2185 (KKT-with-margin-multiplier :2126-2132 VERBATIM;
  THEOREM/SCHEMA classes :2155-2157), :2164-2177 (see RC28-9 for the two
  wording deviations), :2222-2238, :2256-2259, :2285-2335 ((v)/(vi) VERBATIM
  incl. "CANNOT capture the S20-instance certifiability frontier"; standing
  rule :2325-2327), :2336-2353 (ρ formula, N=3498, R-GRAD numbers).
- Gapmap :65-139 (GAP-1/GAP-2 incl. :77-78 census-row-10 gloss, :89-96 probe
  and exposure lines) and facet s24_gap_driver-nonsmooth.md :15-39, :60-114,
  :488-499 (Probe B numbers incl. 2.9e-3 at :32; drop-item 2 :492-494;
  "The binary P4 gate stays as the verifier of record in every formulation"
  :21 — VERBATIM).
- Registries: choice_ledger.yaml:407-427 (C28 row + note VERBATIM);
  findings_registry.yaml:1136-1144, :1236-1244; claims_registry.yaml:1365,
  :1391-1397; literature_registry grep
  `Kreisselmeier|Poon|Scholtes|MPCC|Audet|bundle|manifold sampling|Burke` → 0
  rows (panel's absence claim REPRODUCED); choice_ledger greps
  `certifiab|P4-gate|frontier` → only :420 and `TR-SQP|MPCC|nonsmooth` → 0
  (REPRODUCED); findings grep `P-CERTKS|P-BSTAT|KSmax|KS-max` → only :1143
  (REPRODUCED); inventory_seg6_memory.md:157 ("MPCC" in the seeded list —
  VERBATIM).
- Pipeline-sense :188-200 (R1 context — see RC28-10).
- Cava lines 36/854/1116/1231/1245 (see RC28-7).
- Census web spot-checks: arXiv:2605.29757 EXISTS (Lämmel–Shikhman 2026) and
  its abstract SUPPORTS the panel's "outperform ... at high accuracy"
  one-liner (inflation candidate hunted, dropped); arXiv:2501.07383 EXISTS;
  AIAA kriging doi 10.2514/1.J059915 = 2021 (RC28-6); Ziems–Ulbrich SIOPT
  2011 lineage EXISTS (RC28-3).
Mis-cites found by this audit: RC28-5 (four stale anchors), RC28-7 (grep
count), RC28-9 (taxonomy class + dropped word), RC28-2 ("committed" label).
All other checked citations accurate.

## DEDUP REGISTER (findings vs existing rows — nothing re-minted)
- RC28-1 rides findings row `driver-nonsmooth:ip-path-unadjudicated`
  (:1236-1244) and the facet's Probe C — it recalibrates the panel's pin, adds
  no new row; the repair folds into the F-3 text + the already-named [P-IPADJ]
  duty.
- RC28-2 is an R5-discipline text repair; no registry row exists or is needed
  (the F2 [P-CERTKS] carrier commitment is already implied by R5 and now
  stated).
- RC28-3 is a census/§3.5 addition CLOSED on M0:2005-2011 + certdiag 8/8
  (M0:2058-2062); no ledger/findings row minted — if F2 ever revisits budget
  scheduling, it mints its own row then. No literature_registry rows exist for
  the lineage (grep above, 0 hits) — consistent with the panel's own deferral
  of lit-row minting to F2 adoption.
- RC28-4/5/6/7/8/9/10/11 are text/scope corrections to PANEL_C28.md itself;
  none contradicts a verdict of record; RC28-10 strengthens the panel's crux
  with the record's own words.
- Checked against BASE/phaseB_tree_diff.md and the r2pass verdicts: no finding
  above re-litigates a verdict of record (§0 rule honored).

## MACHINE SUMMARY
```json
{
  "cluster": "C28",
  "findings": [
    {"id": "RC28-1", "class": "REPAIR-NEEDED", "row": "C28"},
    {"id": "RC28-2", "class": "REPAIR-NEEDED", "row": "C28"},
    {"id": "RC28-3", "class": "REPAIR-NEEDED", "row": "C28"},
    {"id": "RC28-4", "class": "AMENDMENT", "row": "C28"},
    {"id": "RC28-5", "class": "AMENDMENT", "row": "C28"},
    {"id": "RC28-6", "class": "AMENDMENT", "row": "C28"},
    {"id": "RC28-7", "class": "AMENDMENT", "row": "C28"},
    {"id": "RC28-8", "class": "AMENDMENT", "row": "C28"},
    {"id": "RC28-9", "class": "NOTE", "row": "C28"},
    {"id": "RC28-10", "class": "NOTE", "row": "C28"},
    {"id": "RC28-11", "class": "NOTE", "row": "C28"}
  ],
  "breaks": 0,
  "repairs": 3,
  "amendments": 5,
  "notes": 3
}
```
