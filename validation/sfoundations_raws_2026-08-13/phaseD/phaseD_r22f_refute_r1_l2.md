# R22-F REFUTATION — ROUND 1, LENS L2 (asymptotics / measure-and-scaling)

Session: S-FOUNDATIONS-C4, Blocco 1 v2, 2026-08-20. Target:
`phaseD/phaseD_r22f_centerpiece.md` (author draft revision 1, INCLUDING
[GRAFT-*]/[REV-*] markers). Numbering starts at R22F-L2-1 (no prior L2
round exists on disk; measured: no `phaseD_r22f_refute_r*_l2.md`, no
`R22F-L2-` ID anywhere under BASE). Persisting prior findings: 0.

LENS SCOPE HONORED: 3-6% swirl-energy scaling use; M-RED band derivations
(zero magic constants); epsilon-orders of the 2-epsilon transfer;
degenerate limits; forchetta evidence-class honesty (SE labels, CT-6,
definitional guards). RIGHT-SIZING RULE (addendum-c4 (b) / SR-C4-13)
APPLIED: no finding below demands a closed-form gradient bound; L2-1 asks
only that the mandated SCHEMA + named duty EXIST.

READ-DEPTH DECLARATIONS (this window):
- BRIEF_blocco2_phaseD.md [FULL]; BRIEF_blocco2_phaseD_addendum_c4.md
  [FULL]; phaseD_r22f_centerpiece.md [FULL] (all 841 lines incl. §9 graft
  table).
- docs/rde_nozzle_MASTER.md [SLICE :1070-1189] (D.6/D.9/D.10/D.12/D.18).
- swirl5f_judgeverify.md [SLICE :12-61, :92-158, :161-235];
  swirl5f_FINAL_report.md [SLICE :96-107, :436-459, :520-528, :620-628];
  DISPATCH_swirl5f.md [GREP anchors only].
- ADVISORY_litreview_confrontation_2026-08-13.md [SLICE :807, :826-834,
  :1113]; docs/findings_registry.yaml [SLICE :1459-1467, :2026];
  validation/o32_mesh_convergence.py [SLICE :20-44];
  SYNTHESIS_nozzle_rde_arrivals.md [SLICE :155-161, :223-229, :445-451,
  :622-627]; FIELD_ATLAS_targeted_c4.md [GREP :277-294 shroud lines].
- No paper re-read this window (no L2 finding needed one).

PROBES (pinned env, numpy only; all run PASS this window):
- `r22f_v2_probe_r1_l2_drop_sign.py` (feeds L2-3)
- `r22f_v2_probe_r1_l2_two_eps.py` (feeds L2-4)
- `r22f_v2_probe_r1_l2_richardson_dof.py` (feeds L2-6)

==============================================================================
## FINDINGS

### R22F-L2-1 — REPAIR (mandate coverage): channel (vi) OPTIMUM-SHIFT row
### and the design-gradient-level bound schema are ABSENT
ANCHORS: draft Part 5 table :663-669 (rows (i)-(v) only); §2.2 :294-326
(value-level schema only); the draft's own GAP FLAGS :746-749 (G-07) and
:657-662 (G-10) concur. BRIEF (as amended) :112-126: "(vi) OPTIMUM-SHIFT
channel ... the deliverable states the perturbation bound |argmax shift|
<= delta/mu with mu = the MEASURED engine curvature at S* ... and delta =
the DESIGN-GRADIENT-level bound on the residual (T-RED's section (2)
therefore delivers its bound schema at BOTH levels: value AND
design-gradient ...)". Both mandated elements are missing from the
deliverable text: no (vi) row exists in the table, and Part 2 carries no
gradient-level schema at any rigor class. Per the round-1 mandate-coverage
duty, missing mandated element = REPAIR. RIGHT-SIZING COMPLIANCE: an
honest SCHEMA (hypothesis list + bound structure + what-derives-it:
five-field content bound / route-B / M-RED gradient measurement) + the
delta/mu cell with mu = the segmented TR-Newton measured curvature
(Hessians of record) is a fully acceptable dry outcome — a closed form is
NOT demanded. The Fig. 18 per-term disposition (the other mandated
element checked by this duty) IS present (§2.3 table :378-384) — no
finding there.

### R22F-L2-2 — REPAIR (delivery-check): addendum-(c) structural
### declaration absent from the forchetta header/notes
ANCHORS: draft :647-662 (G-10 enrichment present; its own GAP FLAG states
the record sentence itself is absent); addendum_c4 §(c): the
no-external-referee declaration (incl. the Harroun-1.25
quasi-cycle-averaged qualifier and the CONSEQUENCE sentence) "MUST APPEAR
IN THE FORCHETTA TABLE ... This declaration is a delivery-check item."
The graft carries the enrichment and the consequence, not the declaration
of record. One-paragraph repair: land the addendum-(c) sentence verbatim
in the table header or notes.

### R22F-L2-3 — REPAIR (load-bearing; executable counterexample):
### [T-DISC-2](i) sign leg is FALSE on DROP-convention fiber families;
### zero-separation degeneracy unnamed
ANCHORS: draft :128-138 ("Hence J separates single-signedly: J(s_lambda)
strictly decreases in lambda^2"), quantified over the [T-DISC-1] family
which EXPLICITLY includes the DROP variant (:100-104 "h0 fixed under the
DROP convention verbatim"); LOWER-BOUND READING :151-158 ("BOUNDED BELOW
BY A STRICTLY POSITIVE, SINGLE-SIGNED functional"); inherited by
[T-DISC-4](a) :203-211 and the forchetta (iii) rigor column :667 ("sign
leg of the debit THEOREM*").
DEFECT: the exact relation u_e^2 = 2(h0 − h(p_e,s)) − v_e^2 − Gamma^2/r_e^2
uses the PHYSICAL total enthalpy; the fiber fixes the h0-TRACE. Under the
DROP convention these differ: h0_phys(lambda) = h0_data + Gamma^2/(2 r_in^2)
varies along the fiber, and the within-fiber variation becomes
Delta u_e^2 = Gamma^2 (1/r_in^2 − 1/r_e^2): strictly INCREASING thrust for
r_e > r_in and IDENTICALLY ZERO at r_e = r_in (degenerate fiber
direction). Probe `r22f_v2_probe_r1_l2_drop_sign.py`: DROP with
r_e = 2 r_in gives u_e up 1.67% at lambda = 1 (J increases, pressure term
fixed) — "strictly decreases" falsified; DROP with r_e = r_in gives u_e
constant over the whole family — the "strictly positive" lower-bound
reading fails there. RECORD CORROBORATION: this is the record's own
algebra — judgeverify §5.2 :174-190 (drop bias = (δ_int²/2)(1 − r_in²/r_exit²),
"Geometry-signed, ≈ 0 at r_exit ≈ r_in", verifier R-B) and FINAL_report
§1 B2 row :100; the probe also reproduces the R-B boundary
(|drop|/fold = r_e²/r_in² − 1, = 1 at r_e = √2 r_in) exactly.
REPAIR (one paragraph, latent in the record): scope leg (i) THEOREM* to
PHYSICAL-h0-fixed fiber comparisons (FOLD convention, or the DROP family
with the compensated-exhibit variant); route the uncompensated DROP
family to the geometry-signed formula of record (single-signed PER FAMILY
with sign set by r_e/r_in, ≈ 0 at r_e ≈ r_in — name this degeneracy in
the hypothesis/falsifier text, beside R-7); propagate the scoping to the
LOWER-BOUND READING, [T-DISC-4](a), and the (iii) rigor column. NOT
label-inflated to BREAK: the theorem core (physical-h0-fixed separation)
survives intact under the probe's own FOLD leg, and the fix is the same
class as the record's R-B one-line repair. It blocks dry like any REPAIR.

### R22F-L2-4 — REPAIR (executable counterexample): [T-DISC-3]
### mis-assembles the 2-epsilon lemma (wrong epsilon, wrong quantifier)
ANCHORS: draft :176-198, specifically :179-180 (eps_fib(P) := sup over
the fiber of |J(s) − J(s')| — the fiber DIAMETER of J) and :184-188 ("if
a designer optimizes ANY functional that factors through pi ... the
resulting design is up to 2·eps_fib suboptimal for the true J, and NO
refinement of the p-only data can reduce this").
RECORD FORM (verified at source, FINAL_report :450-452): premise =
sup_A |J_exact − J_avg| ≤ ε for the GIVEN surrogate (the (U) sup-error),
conclusion = 2ε-suboptimality of that surrogate's maximizer; two-point
weakening (ε₁ + ε₂ + η) proven.
DEFECT: substituting ε := fiber diameter while quantifying over ANY
pi-factoring functional yields a false upper bound: a p-only surrogate
with the wrong INTER-fiber ranking incurs suboptimality set by the
inter-fiber J-range, unbounded by fiber diameters. Probe
`r22f_v2_probe_r1_l2_two_eps.py`: 2-fiber class with sup eps_fib = 0.10,
adversarial surrogate → suboptimality 1.05 > 2·sup eps_fib = 0.20 (the
record lemma itself stays intact with ε = that surrogate's own sup-error
1.05). The sentence also conflates an upper bound ("up to 2·eps_fib")
with the irreducibility floor ("NO refinement can reduce this").
REPAIR (reassembly, both legs citable): (a) per-surrogate leg = claim 10
verbatim: any surrogate G = g∘pi with sup-error ε_G is ≤ 2ε_G-suboptimal;
(b) irreducibility leg = the BEST pi-factoring surrogate (fiber midrange)
has sup-error exactly sup_P eps_fib(P)/2 — probe-verified — so even the
optimal p-only pipeline risks up to sup_P eps_fib(P) (equivalently cite
the record's two-point ε₁+ε₂+η weakening for the two-fiber form); the
G2/F5a conditional-gain template then binds ε to the surrogate actually
used, measured/assumed per family. Grade can stay SCHEMA; the current
assembly is unsound as printed, which is attackable per the right-sizing
rule's own terms.

### R22F-L2-5 — REPAIR (measure theory): "exactly TWO first-order
### channels" overreaches the stated class — the Cantor part is unowned
ANCHORS: draft §2.2(i) :295-308 ("exactly TWO first-order channels
survive in J: (J) the atom/jump pairing ... and (H) the a.c.
covariance/hysteresis channel"), over H-RED-2 :288-289 ("periodic BV
composite class in phi (bounded S1 fields, finitely many front crossings
per period)"); §2.5 :453-454 ("Two-channel reduction: THEOREM*
conditional on H-RED-3/H-RED-4").
DEFECT: BV admits a nonzero Cantor part (bounded + finitely many jumps
does NOT imply SBV); the draft's own mean-nullity leg enumerates "a.c. +
Cantor + atoms included" (:300, faithful to judgeverify §3.3 :115), yet
the first-order pairing census assigns only atoms → (J) and a.c. → (H):
on a BV-with-Cantor field the two printed channels do not exhaust
⟨psi, K⟩, and the Cantor contribution belongs to neither. The record
carries the same silent drop (judgeverify :122-124 "moving the atom mass
to the (J) channel gives J₁ = ⟨ψ̄, atom content⟩ − Cov^{ac}") — the
THEOREM* label here must not inherit it.
REPAIR (cheap, AG-1-valve-compatible: strong trivially-checkable
hypothesis): add the Cantor-free clause to H-RED-2 (W piecewise-a.c. in
phi — SBV; trivially true for the intended piecewise-smooth composite
class with fronts), or add the third channel line explicitly. Propagate
one word into §2.5's grade line.

### R22F-L2-6 — REPAIR (band derivation, executable): M-RED band B-1's
### uncertainty estimator does not exist on the declared ladder
ANCHORS: draft §3.4 :525-531 ("three-point Richardson on the St-ladder;
C2 = measured second divided difference, its uncertainty = the ladder's
third difference").
DEFECT (dof count): k ladder points support divided differences of order
≤ k−1; a three-point ladder yields the second divided difference (= C2)
with ZERO residual dof — "the ladder's third difference" does not exist.
Probe `r22f_v2_probe_r1_l2_richardson_dof.py` demonstrates (0 third
differences on 3 points; well-defined and correctly behaving on 4). The
zero-magic-constants rule (Part 3 header, :473-474; BAND RULE :550-552)
requires the declared estimator to be executable as published.
REPAIR: declare a ≥ 4-point St-ladder (uncertainty = the third divided
difference, now defined), or bind the uncertainty to the (D)-sweep
residual across the full ladder — either keeps the band derivation
publishable as written.

### R22F-L2-7 — AMENDMENT (dimensional notation): B-2's integral measure
ANCHORS: draft :533-534 ("the E_theta debit measured per family =
mdot-weighted ∮ u_theta^2/(2 u_e) dA at exit").
As printed the literal-dA reading is dimensionally not a thrust debit
(velocity × area); the intended object is ∮ u_theta²/(2 u_e) dṁ with
dṁ = ρ u_x dA (then N: consistent with leg (i)'s per-streamline debit
Γ²/(2 r_e² u_e) per unit mass flux). Write the measure explicitly.

### R22F-L2-8 — AMENDMENT (citation fidelity of the licensed phrasing):
### the fitted-sheet condition was dropped from the "verbatim" quote
ANCHORS: draft :306-308 ("'single-digit % plausible on-ray, >10% NOT
excluded off-ray' — cited verbatim as the licensed phrasing") and the
forchetta (ii) BEST cell :666. SOURCE (FINAL_report :436-437): "single-
digit-% total PLAUSIBLE on ray-like sawtooth cycles WITH A GOOD FITTED
SHEET; >10% NOT EXCLUDED on ...". The fitted-sheet qualifier is
load-bearing (it is what M-RED leg (E) tests) and the quote is not
verbatim without it. Restore the qualifier in §2.2(i) and the (ii) BEST
cell (or drop the word "verbatim" and cite the licensed phrasing with
both conditions named).

### R22F-L2-9 — AMENDMENT (anchor naming): "C25 corrections registry
### :2026"
ANCHOR: draft forchetta (iii) WORST cell :667. The C25 correction text
(V7 = argmax ~71.5%, V5 recommended 70.0%, "percentage POINTS of ideal")
lives verbatim at docs/findings_registry.yaml:2026 (verified this
window); no file named "corrections registry" exists (measured: ls
docs/*registr*). Line number and content are exact — fix the carrier
name to findings_registry.

### R22F-L2-10 — NOTE (record-side, no draft action): the D.10 "~4x /
### 0.3-2.5%" pairing is internally tensioned in the RECORD, not the draft
The draft (:144-146) cites M0 :1156-1161 faithfully ("the h0-normalized
reading is ~4x smaller (0.3-2.5%)"). At source the nominal ~4x of 3-6%
gives 0.75-1.5%, and judgeverify :35-37 computes 0.45-2% at concordant
numbers while the judge printed 0.3-2.5%. A record-side blemish owned by
the M0 D.10 row; the draft asserts nothing above the record and needs no
edit. Flagged for the closure judge's landing-notes only.

### R22F-L2-11 — NOTE (verified-green ledger, zero credit inflation):
### L2-checkable chains that SURVIVED source verification this window
(a) spike-core band √(ε_θ·χ/2) → 0.065-0.14 exact at the adjudicated
χ = 0.06-0.20, ε_θ = 0.15-0.20 (judgeverify §1.2, R-A) ✓; (b) β_w =
p/(ρh0) is the record's own STRONGER EOS-free definition-level form
(judgeverify :29-33), NOT a draft alteration — attack considered and
withdrawn ✓; (c) work-term 0.007-0.09 (:33-34) ✓; (d) Λ = 0.59-1.11·St_n
(R-C) ✓; (e) forchetta (iii)/(v) cell numbers B1 0.6-9% (working
1.5-4%), B2 1.5-3% fold with the √2·r_in clause, B3 0.5-2.5% in T, B5
10-14° all match FINAL_report :99-103, and B2 vs B5 are cross-consistent
(tan²(10-14°)/2 = 1.5-3.1%) ✓; (f) B-4's pre-registered-norms citation
o32_mesh_convergence.py:24-38 exact ✓; (g) shroud marker 58.1→~71.5 (V7
argmax; V5 70.0%) matches advisory :807/:828 and the atlas :289 ✓; (h)
CT-6 respected: no P-A..P-D number enters any table cell, bound, or band
— all confined to [ADV] notes with the ceiling restated ✓; (i) the
definitional guards mandated by SYNTHESIS (e) (RMSD_theta operative rule
in the stronger [REV-NRS-2] form + film-cooling caveat [REV-NRS-3]) are
present in G-04 ✓; (j) Fig. 18 per-term disposition present and each
disposition stays within held evidence (§2.3) ✓; (k) Hoffman scale
0.04-0.34% and the +0.51% in-class datum match advisory :826-833 ✓; (l)
the §2.1 flux identity and the §5.4 equivalent-form identities re-derived
by hand here, row-for-row exact ✓.

==============================================================================
## COUNTS (this round, this lens)
BREAKS: 0. REPAIRS: 6 (L2-1, L2-2, L2-3, L2-4, L2-5, L2-6).
AMENDMENTS: 3 (L2-7, L2-8, L2-9). NOTES: 2 (L2-10, L2-11).
Persisting prior findings re-counted: 0 (no prior L2 round exists).
DRY VERDICT AT THIS LENS: NOT DRY (6 REPAIRS sustained; 0 BREAKS).

## PAPERS NEEDED
NONE. (No L2 finding requires a source not already on disk.)
