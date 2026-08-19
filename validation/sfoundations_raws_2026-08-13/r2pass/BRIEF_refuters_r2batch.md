# ADVERSARIAL REFUTATION BRIEF — batched r2 pass over the final-revision deltas

Role: adversarial refuter (one of two independent lenses; your task order
names yours). Repo root: the rde-lecture-code working tree. All paths
below are relative to `validation/sfoundations_raws_2026-08-13/`.

## Mission

The final revisions of three proof documents contain legs authored in the
LAST revision pass that have had ZERO adversarial coverage (the loops
capped NOT-DRY). Your job: attack EXACTLY those legs, at derivation
level. This is a content pass, not a label pass — the judge-assigned
rigor classes of record (VERDICT_phaseD_proofs1.md §3,
VERDICT_contract_and_L4R1.md B.3) are certified and are NOT re-litigated
here; if you believe a label is inconsistent with content you find, say
so as an objection, but your primary target is the mathematics of the
delta legs.

## Targets (the delta set, exhaustive)

DOC-1 `phaseD/phaseD_stop_proof.md` (revision 3), r3-new legs:
 1. [L-INC] (the new lemma, both strata uses);
 2. [L-STD] final no-topology pointwise argument (incl. countable-dense
    closure + eps_n union assembly);
 3. the periodization step;
 4. [P-HB3] (i') data-space mollification proof (the replacement of the
    null-graph step);
 5. the G8/r2 repricing (gap accounting for [C-XBVP](a')).

DOC-2 `phaseD/phaseD_meanswirl_formalization.md` (r3), r3-new legs:
 6. D.18 singular leg — both iff displays + the singular-density
    bookkeeping (atoms = n_phi[F_phi,rel] per row); NOTE: the two
    predecessor forms of this clause were FALSE (r1 divided by w_rel;
    r2 false on the front-carrying class) — highest-suspicion target;
 7. D.2 psi-existence three-step argument (closedness / periods /
    quasiconvexity) + the H-CVX arc wording (s-monotonicity discharge);
 8. D.16 gross normalizer;
 9. D.20 contact split (the r3 two-line RH algebra);
 10. D.10 theta-halves exhibit (the Gamma-flux zeroing);
 11. D.8 plane-stress rewording ((0)-channel exhaustiveness).

DOC-3 `phaseD_L4_implies_R1.md` (r2), r2-new proofs (the AUDIT-DEBT-r2
set of record):
 12. Theorem 1' (collar instantiation of the Theorem 1 energy argument);
 13. Lemma 1.4 (finite speed; shrinking-frustum positivity
     lambda_max S + S A(nu) >= 0 via the Lemma 1.2 similarity);
 14. Proposition 1'' bootstrap (t* maximality, modulo (H-UP));
 15. Lemma 3.2 (monotone-intersection; scope = uniform
     pure-pressurization only);
 16. Corollary 4 row-(a) in-class transport restatement;
 17. Remark 1.5.5 (ii') measurable-field restatement (good-sign boundary
     term, characteristic-inflow scoping);
 18. the Lopatinskii display.

## Method constraints

- Read each delta leg IN FULL in its document, with enough surrounding
  context to judge consumption (the revision blocks anchor each repair).
- DEDUP (cite-not-remint): objections already raised in the on-file
  round files (`phaseD/refute_S-T0P_r*.md`, `phaseD/refute_SWIRL-2D_r*.md`,
  `refute_L4R1_r*.md`) and consumed in the documents' disposition ledgers
  are NOT re-raised — unless you attack the DISPOSITION itself (then cite
  the finding ID you are re-opening and say why the consumption fails).
- Every objection: numbered (your lens prefix + running number), with the
  target leg number (1-18), a verbatim quote of the attacked text, the
  attack at derivation level, and a classification
  {BREAKS-THE-LEG, REPAIR-NEEDED, AMENDMENT/wording}.
- Every leg you examine and CANNOT break: record it as CONFIRMED with one
  sentence on the strongest attack you tried and why it fails. All 18
  legs must appear in your output exactly once (CONFIRMED or objected).
- Honesty rules: no objection stronger than your evidence; rejected
  attack attempts recorded where informative.

## Output

Write your full refutation file to the path named in your task order.
Structure: header (lens, date) -> per-leg sections 1..18 -> summary table
(leg | verdict CONFIRMED/OBJECTION-ids) -> `OVERALL: <n> objections, of
which <k> BREAKS-THE-LEG` -> falsifier for your own pass.
