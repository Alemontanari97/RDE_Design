# REFUTATION — CLUSTER C9C11 (march mesh law + error estimator for J)
# S-FOUNDATIONS-C2, Blocco 3 wave 1, adversarial refuter, 2026-08-19.
# Target: validation/sfoundations_raws_2026-08-13/blocco3/PANEL_C9C11.md
# Brief: BASE/blocco3/BRIEF_wave1_refuter.md (duties a-f, per-row).
# Every anchor below was read AT SOURCE in this window (see §2 audit).

## 0. OVERALL POSTURE

The panel is compliant with the §0/§C9C11 mandate in structure and in
most substance: formalize-first honored, census reaches the modern
layer with honest per-item evidence levels, blind trees cited by
file:line and not regenerated, the incumbent's genuine case is
represented on both rows (loop economics, estimator independence, the
o32 pre-registered-window binding), 4/4 convergence used as evidence
with content doing the work, and both rows land measurement-gated as
the brief expects. Every verbatim quote I spot-checked matches its
source (§2). NO finding below breaks either proposed row outcome.
What survives contact are: one undeclared cross-row decision (C43),
two falsifier-integrity defects (F9a meter, F11a sequencing), one
asserted-not-shown derivation (F9a threshold), one missed on-disk
source that the binding F2 duty should consume (Ancourt 2023), and a
tail of text/scope amendments including two unsourced or mis-typed
numerals inside the frozen statement and the incumbent case.

Findings: 0 BREAKS-VERDICT / 5 REPAIR-NEEDED / 8 AMENDMENT / 1 NOTE.

---

## 1. FINDINGS

### 1.1 Row C9 (march mesh law)

**RC911-2 — REPAIR-NEEDED — F9a cost-matching meter mis-specified
(falsifier can be biased toward adaptation).**
Panel §4.1 F9a pins "matched total column count (equal unit-process
count, the march's own cost meter)". The parenthetical equates two
DIFFERENT meters: equal column count does not imply equal
unit-process count. Witness: the o32 instrument itself refines NI,
Nw, da as separate knobs (validation/o32_mesh_convergence.py:470-497:
"r(NI-1)+1, Nw -> r Nw, da -> da/r") and prints `cells` SEPARATELY
from NI/Nw (:555-559) — cells-per-column vary with position and with
the wall/exit refinement, and the AC2 primitive INSERTS columns whose
point counts depend on where they are inserted. As pinned, an adapted
run can carry more unit processes than the uniform arm at "matched
cost", so `E_A < E_U` can be bought with resolution, not placement —
the REFUTES-ADAPTATION arm could be unable to fire by construction.
Mechanism: falsifier-integrity (duty e). Repair (named): define
matched cost on TOTAL UNIT-PROCESS COUNT (the meter the pin itself
names), delete the column-count equation; the F2-C9 duty reports both
counts per arm. Outcome (gated split) stands after repair.

**RC911-3 — REPAIR-NEEDED — F9a promotion threshold asserted-derived,
derivation absent (R5).**
Panel §4.1: "factor 2 = the smallest ratio distinguishable outside
the joint band at the measured [X-O32] band widths on the twins" — a
factual claim about measured widths with NO cited widths, sites, or
arithmetic (R5: no numbers without committed source; the rule
"threshold rises with wider bands" is honestly pinned, the
instantiated 2 is not). Additionally "twice in a row" is an
undeclared repetition knob: neither derived from the measured
variance nor declared as a governance constant. Mechanism:
magic-vs-derived (duty e). Repair (named): F2-C9-MESHLAW-CAMPAIGN
publishes the derivation (site list, measured [X-O32] band widths,
implied smallest distinguishable ratio) BEFORE first use of the
promotion arm, and classes "twice in a row" as variance-derived or
declared-governance. Outcome stands after repair.

**RC911-7 — AMENDMENT — frozen statement mis-types the incumbent law.**
Panel §1.1: "the four per-run integers NI / da / Nw / Ne". `da` is
real-valued, not an integer: validation/a1_ideal_march_jax.py:194
(`da_deg=0.5`), refined as `da -> da/r` (o32:470). Text fix
("four per-run mesh parameters"); outcome unmoved.

**RC911-10 — AMENDMENT — demotion prose overstates vs its own
falsifier.**
Panel §4.1 declares the uniform incumbent "no longer the program's
answer to C9", while F9a's refutation arm explicitly provides "C9
CLOSES on uniform+A36 and the AMR line is dropped as production law".
A gated split whose pinned falsifier can restore the incumbent as the
final answer should say "target-law status presumptive pending F9a",
not declare the incumbent's answer-status dead. Inflation of the
verdict text relative to the pinned protocol (duty c/d); the gating
structure itself is correct. Outcome unmoved.

**RC911-13 — AMENDMENT — F9b transplants the H-F27 falsifier with the
attribution test undefined (R-4).**
"no step rejection attributable to remeshing" (panel F9b) carries
phaseA_tree_hyperbolic.md:868-870 ("gradient-verification failures
... traced to remeshing events") verbatim-by-declaration, but neither
the tree nor the panel defines HOW a TR rejection is traced to a
re-mesh event, so that half of F9b cannot fire unambiguously. The
O3.1-floor half of F9b is fully operational and can fire alone, which
is why this is not REPAIR-class. Recalibration to add: re-run the
rejected step on the frozen (pre-re-mesh) topology; acceptance there
attributes the rejection to remeshing. Outcome unmoved.

### 1.2 Row C11 (error estimator for J)

**RC911-1 — REPAIR-NEEDED — C43 is decided in substance without being
declared (dedup/record, duty f).**
The C11 pins 1-2 adopt exactly the listed alternative of ledger row
C43 "Asymptotic-range handling at band sites" (incumbent "presumed
h^p at r=1,2"; alternative "per-site observed-order check (o32
estimator reuse) + NON-CONCLUSIVE propagation"; status NEVER, owner
S25, annex pointer GAP-9 — docs/choice_ledger.yaml:581-589). The
panel's §4.3 interplay declares C42, C10, C27/C28 — never C43. The
panel's own reported grep ('C42|K_RICH' on the ledger) RETURNS header
lines that name C43 next to C42 (choice_ledger.yaml:71,81), which the
panel's §1.4 report silently drops (it reports only :571 and :409);
the grep tokens themselves cannot hit C43's row text, and no
'asymptotic|observed-order|h\^p' sweep was run. Landing C11 as
proposed would leave a NEVER ledger row whose question was decided in
another row's verdict — the precise anti-entropy failure mode the
R7/SR guards exist for. Mechanism: dedup query too narrow + grep
hits under-reported. Repair (named): the landing declares C11 leg (a)
as the adjudication of C43 (mark C43 accordingly at ledger-edit time)
OR explicitly defers C43 to its owner with the dependency named.
Outcome stands after repair.

**RC911-4 — REPAIR-NEEDED — F11a twin-site arm can execute against an
invalid E_true; leg sequencing unpinned.**
F11a(ii) takes "E_true from the verified fine-ladder extrapolation ±
its band" at the production twin sites. The record says the twin's
observed order is NON-CONCLUSIVE (docs/findings_registry.yaml:1185:
p_fine=2.5347, dp_tot=0.6704 > 0.5 cap; standing counterexample where
the banded quantity's error GROWS under refinement) — so the
"verified" extrapolation the pin presumes does not exist today; the
panel's own leg (a) (GAP-9) is what would create it, yet §4.2 never
orders leg (a) before leg (b)'s twin arm. Unrepaired, the promotion
gate can be granted or refused against an E_true with no valid order
behind it — the gate stops being a falsifier (duty e). Repair
(named): pin the dependency — F11a's twin arm is valid only at sites
where leg (a) delivers a CONCLUSIVE observed p; sites failing it
contribute only via the degraded-p E_true band per the propagation
rule, and promotion on the Giles-Pierce oracle alone must be declared
as oracle-only. Outcome stands after repair.

**RC911-5 — REPAIR-NEEDED — census and binding duty omit the on-disk
adjoint-characteristics anchor (Ancourt-Peter-Atinault 2023).**
docs/literature_registry.yaml:199-208: "Ancourt, Peter & Atinault
2023, Adjoint and Direct Characteristic Equations for 2-D
Compressible Euler Flows, Aerospace 10(9):797 (published version
superseding arXiv:2305.03499)" — READ-INTEGRAL, on disk in TWO roots,
expert read on file (literature_review/reports/ancourt_2023_char_adjoint.md),
row in the RATIFIED cava's paper-per-paper table; summary includes
"ACE residuals as code verification" — an adjoint-characteristic-
equation residual instrument, the closest existing published object
to the characteristic-native DWR residual the panel wants built. This
is the SAME line the panel imports at abstract level via Lozano-
Ponsin 2025 (§2.3), and it is HELD + READ while Lozano-Ponsin is
unheld. The panel's §1.4 registry greps used estimator tokens only
(DWR/Richardson/GCI/effectivity/names), which cannot hit this row,
and no 'characteristic|adjoint' sweep or local literature_review/
glob was run — a navigation-first defect (litreview protocol: local
sweep before procurement). Consequences to repair (named): (i)
F2-C11-ESTIMATOR-CAMPAIGN leg (b) names ancourt_peter_atinault_2023
as a consumed formulation input (held anchor of the adjoint-along-
characteristics line, with Lozano-Ponsin 2025 as its 2025 extension —
the two are siblings: 2305.03499 is Ancourt's own arXiv id); (ii)
§2.4's "nearest hits" line is corrected to name the on-disk paper as
nearest. The §2.4 absence claims THEMSELVES survive (verified: no
DWR-estimator-for-marching literature; Ancourt is equations +
verification residuals, not a J-error estimator). Outcome unmoved —
strengthened — after repair.

**RC911-6 — AMENDMENT — frozen statement mis-formalizes the incumbent
estimator ("ASSUMED order p=2").**
The deployed band is K×|Δ| with NO (r^p − 1) division and no p=2
arithmetic anywhere: validation/a1_ideal_march_jax.py:1459
(`tol_dp = K_RICH * (abs(float(w @ (dv_h - dv_h2))) ...`), :1231,
:1267; validation/o33_bench.py:124-129 ("two-resolution Richardson
estimates x the repo's reused K_RICH = 4"). The incumbent's premise
is h^p asymptotics with coverage bought by K alone — exactly the
findings-row form ("presumes the h^p model at r=1,2", :1185), whose
0.415 coverage arithmetic the panel itself uses correctly in §3.2 and
pin 2 (checked: K covers the coarse member iff 3·2^p ≥ 4 ⟺ p ≥
log2(4/3) = 0.415 — the recorded bound is right). "ASSUMED order
p=2" over-weakens the incumbent inside the frozen statement (mild
anti-incumbent smuggle, duty a). Text fix; outcome unmoved because
the adjudication used the correct arithmetic.

**RC911-8 — AMENDMENT — unsourced "10× conservativeness reserve" in
the incumbent's case (inflation hunt, duty b).**
Panel §3.2 incumbent case 1: "a 10× conservativeness reserve over p=2
asymptotics". Derived from the deployed band form K×|Δ| at p=2, r=2:
coarse-member reserve = 4/(4/3) = 3×; fine-member reserve = 4/(1/3) =
12×. Neither is 10×, and no committed source carries 10× (the
findings row does not). An unsourced numeral inflating the
INCUMBENT's represented case. Replace with the derived pair (3×
coarse / 12× fine) or delete; outcome unmoved (the incumbent loses on
the confirmed defect regardless).

**RC911-9 — AMENDMENT — D-49 trigger under-quoted; the DWR-failure
path silently drops the probe.**
Row docs/findings_registry.yaml:1476 trigger of record: "F2 window,
OR the first new DWR-bar claim of record". The panel §1.3 quotes only
the second arm as "trigger of record" and §4.2 pin 5 binds D-49 to
the DWR bar's existence. In the F11a failure path ("DWR demoted to
ADAPTATION DRIVER ONLY ... bands stay GCI/LSQ — this outcome still
closes C11") no DWR bar ever exists and the pin as written would
never land D-49 — but the row's FIRST arm fires it at the F2 window
regardless. Fix: state that D-49 lands in the F2 window in BOTH
branches of F11a. Outcome unmoved.

**RC911-11 — AMENDMENT — standing-verdict sentence missing on the C11
half; interim regime between now and leg (a) unnamed.**
C9's outcome pins "no verdict of record moves"; C11's "retired NOW"
has no equivalent sentence, and pin 2's regime (observed-p
certificates at quantity-sites) is unexecutable today — no such
certificates exist at band sites (that is GAP-9 itself), and the
degraded-p coverage factor's definition is part of leg (a)'s
deliverable. As written, the burden-inversion claim ("retired NOW,
not at F2's leisure") is partly performative: nothing enforceable
changes until leg (a) lands. Fix (text/scope): add — standing
Richardson-banded verdicts of record STAND with the row-:1182
CONFIRMED flag attached (retirement is of the premise's epistemic
status, not a voiding); any pre-F2 band-bearing verdict either runs
the ALREADY-BUILT [X-O32] three-level estimator at its own sites or
declares the row's trigger ("next band-bearing verdict at an
unverified observed order", :1190) fired. Outcome unmoved.

**RC911-12 — AMENDMENT — census misses the space-time/unsteady DWR
line: the published corpus of DWR on MARCHED solves.**
Search-proven this window (WebSearch 2026-08-19, query "output-based
space-time mesh adaptation unsteady adjoint error estimation
Fidkowski dual weighted residual time marching"): Fidkowski & Luo,
JCP 2011, "Output-based space-time mesh adaptation for the
compressible Navier-Stokes equations"
(https://www.sciencedirect.com/science/article/abs/pii/S002199911100221X,
https://public.websites.umich.edu/~kfid/MYPUBS/Fidkowski_Luo_2011.pdf);
Fidkowski, JCP 2017, output-based space-time mesh optimization with
continuous-in-time adjoints
(https://www.sciencedirect.com/science/article/abs/pii/S0021999117302760);
unsteady turbulent extension, CMAME 2022
(https://www.sciencedirect.com/science/article/abs/pii/S0045782522004200).
A supersonic space-march is time-like in x (standard marching
doctrine), so this corpus — dual computed by a REVERSE sweep against
the marched primal, per-slab (= per-column) error localization,
spatial/temporal (= cross-/along-column) error split — is the nearest
published template for leg (b)'s characteristic-native formulation
and for F9a's placement indicator. §2.4's absence claims survive as
bounded by Q9's literal terms ("space marching"), but §2.2's "the
modern refined layer is REACHED" overstates while this directly
adjacent modern line is absent. Add the line to the census and to
leg (b)'s inputs (WANTED rows may ride the same registration duty);
direction unmoved — again strengthened.

### 1.3 Cluster-shared

**RC911-14 — NOTE — bookkeeping and one falsifier-text wobble.**
(i) Machine summary "alternatives_closed: 8" has no stated counting
rule: adjudicated positions = 9 (4 C9 options + 5 C11 options incl.
H-F26(c)); non-incumbent alternatives = 7; 8 is not reproducible
from the file. State the rule or fix the count at landing.
(ii) F11b calls itself "the P-F31 per-solve check" while measuring
effectivity "at checkpoints" — a per-solve rejector whose measured
quantity exists only at checkpoints is under-specified in between;
the natural completion (DWR η computed every solve; solves between
checkpoints inherit the last measured population band; referee
comparison at checkpoints) should be written in. (iii) §1.1's DWR
formula `η_J = Σ_K ⟨R(u_h), λ_h⟩_K` (signed) differs from O-F24's
`Σ_K |⟨R(u_h), λ_h⟩_K|` (localized/absolute) — no mis-cite (the panel
attributes the formula to the literature, not the tree), but the
signed-estimate vs absolute-indicator distinction matters for
effectivity measurement and should be fixed in leg (b)'s spec.

---

## 2. VERBATIM-QUOTE AUDIT DECLARATION

Spot-checked AT SOURCE this window; result per anchor:
- choice_ledger.yaml:217-226 (C9), :238-248 (C11), :228-236 (C10),
  :407-417 (C27 incumbent formula at :409), :571-579 (C42),
  :581-589 (C43): MATCH (statuses, incumbents, alternatives, notes).
- phaseB_tree_diff.md:66-72 (C9 "4/4 CONVERGENT AGAINST THE
  INCUMBENT"), :76-81 (C11 "inverted burden of proof"): MATCH.
- phaseA_tree_variational.md:1246-1272 — "O2 at checkpoints as the
  effectivity referee; every safety factor traced to the measured
  effectivity distribution (no magic 1.25)": VERBATIM MATCH.
- phaseA_tree_hyperbolic.md:833-850 — "estimates the THRUST error
  directly — matches the certificate need; needs the adjoint (have it
  anyway)"; "order-assumption fragile at fronts, cheap cross-check
  with MEASURED observed order"; "sharp in smooth marching regions,
  exotic machinery"; falsifier "under-predicting true error on oracle
  problems outside its own stated band": ALL VERBATIM MATCH.
- phaseA_tree_hyperbolic.md:854-870 — "(a) ... the classical MoC
  policy, automatically front-aligned"; "(e) design-frozen meshes";
  falsifier "gradient-verification failures ... traced to remeshing
  events" (incl. "force fully fixed topologies per trust region",
  which F9b's consequence carries correctly): MATCH.
- phaseA_tree_optimization.md:1257-1289 — "declared safety factor =
  measured worst effectivity × margin derived from its variance, not
  a magic 2"; "two independent estimators agreeing = the error bar's
  own certificate"; residual-based rejected "thrust is a boundary
  functional"; falsifier "effectivity drifting ... fitted-tier duals
  take over": ALL MATCH. (Panel's §1.1 signed η formula is NOT this
  block's absolute-value form — see RC911-14(iii).)
- phaseA_tree_propulsion.md:1144-1164 — "front-passage phases will
  stress it"; per-solve void falsifier; "(observed worst
  effectivity)⁻¹ × margin": MATCH (the F11a S-formula is a fair
  fusion of P-F31/V-F28's inverse-worst forms).
- Cava A36 (:1057): law `h ∝ [log(1/(M²−1))]^{−1/3}`, ≈1.6× [INF],
  three clauses incl. refinement-only/IVL-never-moved rejector and
  the missing-probe clause: MATCH. Cava §3.25 (:679-756): M_IVL−1 =
  5e-6 mesh-independent, order SAFE / constant ≈4× [INF] / gradient
  immune (zero design support), "greatly increase the grid
  resolution" (p.343), "la minaccia è contro una barra futura",
  constants (γ, rtu, yt): ALL MATCH. R27 (:1154): open,
  non-blocking, [X-GP01] rung or Giles-Pierce 1997: MATCH.
- findings_registry.yaml:1182-1190 (p_fine=2.5347, dp_tot=0.6704,
  9.48e-03 → 1.42e-02, 0.415 coarse-member bound, owner/trigger
  text), :1468-1476 (D-49): MATCH — except the TRIGGER at :1476 is
  TWO-ARMED and the panel quotes one arm (finding RC911-9).
- claims_registry.yaml:814 ("O3.1 dot-product over the ENTIRE
  march"), :1290-1299 ([X-AKNO] f2 = −λ2, Prop. A3, 41.8% first
  interval, knot-dof scope), :1397 (twin falsifier): MATCH.
- literature_registry.yaml:491-498 (giles_pierce_2001 READ-INTEGRAL,
  log singularity, "adopted as the first oracle independent of both
  GENO and us" — panel's truncation "adopted as the first oracle" is
  faithful): MATCH.
- o32_mesh_convergence.py:24-39 (pre-registered norms, d = 2 ×
  coarsest spacing = stencil radius, h-independent), :41 ("RATE
  ESTIMATOR — DERIVED, NOT log2 OF TWO LEVELS"): VERBATIM MATCH.
- a1_ideal_march_jax.py:198 (K_RICH = 4.0), :194 (da_deg=0.5 — basis
  of RC911-7); o33_bench.py:124-129; thermotab_c1_jax.py:108;
  adaptive_knot_optimize.py:16-27 (indicator kernel→lip, owner
  array): MATCH.
- ADVISORY_S24_sota_gapmap_2026-08-12.md:855 (AC2 "Column-local C-
  insertion at RECORD time (RK-G P2-compatible) = the AMR primitive
  spec; 41.8% localization datum"): MATCH.
- M0 (docs/rde_nozzle_MASTER.md):353-359 BAR-CLASS note ("DWR is an
  estimate — NOT certified bounds"): MATCH (panel's :353-357 range is
  adequate).
- Web (authorized): Lozano & Ponsin 2025 identity VERIFIED —
  arXiv:2503.13007 "On the characteristic structure of the adjoint
  Euler equations and the analytic adjoint solution of supersonic
  inviscid flows", to appear Aerospace 12(6):494; content matches the
  panel's one-liner (compatibility conditions along characteristics,
  jumps across characteristics, analytic supersonic near-wall
  adjoint). Source: https://arxiv.org/abs/2503.13007 . The same
  search surfaced arXiv:2305.03499 = the Ancourt 2023 paper — the two
  papers are one line, which sharpens RC911-5.
- Panel dedup greps RE-RUN verbatim: literature_registry estimator
  tokens → only :498 (giles_pierce_2001) — CONFIRMED;
  'Roache|Celik|Fidkowski|Hartmann|Loseille|Alauzet' → NO MATCH —
  CONFIRMED; claims_registry tokens → :814/:1294/:1397 exactly as
  reported — CONFIRMED; findings tokens → :1182/:1468 present as
  reported (other hits :500-504, :640, :905, :995, :1326, :1730
  reviewed — none material to C9/C11); choice_ledger 'C42|K_RICH' →
  panel's report OMITS returned hits :71, :81 (header lines naming
  C43) and :489, :649 — basis of RC911-1. literature_review/ glob:
  none of the DWR/GCI canon PDFs on disk — the panel's registration
  duty is well-founded; ancourt_2023 PDF IS on disk (RC911-5).
No fabricated quote found anywhere in the panel. Mis-cites of record:
one truncated two-armed trigger (RC911-9); one under-reported grep
(RC911-1); one unsourced numeral (RC911-8); one mis-typed object
(RC911-7); one mis-formalized incumbent mechanism (RC911-6).

## 3. DEDUP REGISTER (this file mints nothing)

- C43 (choice_ledger.yaml:581-589): CITED — RC911-1 is about the
  panel's failure to declare it; no new ledger row proposed.
- findings :1182-1190 and :1468-1476: CITED (RC911-4, RC911-9, RC911-11
  build on the rows' own text; no new findings-registry rows minted —
  minting is the landing session's call, per the panel's own
  discipline).
- literature_registry :199-208 (ancourt_peter_atinault_2023): CITED —
  already registered + READ-INTEGRAL; RC911-5 asks the DUTY to consume
  it, no registration needed.
- Fidkowski-Luo 2011 / Fidkowski 2017 / CMAME 2022 (RC911-12): named
  as census/duty enrichment; any WANTED rows ride the panel's own §4.2
  registration duty at landing — not minted here.
- No finding above duplicates a verdict of record; none contradicts
  one (checked against M0 BAR-CLASS :353-359, cava §3.25/A36/R27 as
  ratified, and the S25/S25-bis record chain the panel cites).

## 4. MACHINE SUMMARY

```json
{
  "cluster": "C9C11",
  "findings": [
    {"id": "RC911-1", "class": "REPAIR-NEEDED", "row": "C11"},
    {"id": "RC911-2", "class": "REPAIR-NEEDED", "row": "C9"},
    {"id": "RC911-3", "class": "REPAIR-NEEDED", "row": "C9"},
    {"id": "RC911-4", "class": "REPAIR-NEEDED", "row": "C11"},
    {"id": "RC911-5", "class": "REPAIR-NEEDED", "row": "C11"},
    {"id": "RC911-6", "class": "AMENDMENT", "row": "C11"},
    {"id": "RC911-7", "class": "AMENDMENT", "row": "C9"},
    {"id": "RC911-8", "class": "AMENDMENT", "row": "C11"},
    {"id": "RC911-9", "class": "AMENDMENT", "row": "C11"},
    {"id": "RC911-10", "class": "AMENDMENT", "row": "C9"},
    {"id": "RC911-11", "class": "AMENDMENT", "row": "C11"},
    {"id": "RC911-12", "class": "AMENDMENT", "row": "C11"},
    {"id": "RC911-13", "class": "AMENDMENT", "row": "C9"},
    {"id": "RC911-14", "class": "NOTE", "row": "C9C11"}
  ],
  "breaks": 0,
  "repairs": 5,
  "amendments": 8,
  "notes": 1
}
```
