# REFUTATION — SEED-C (dual-seed slot, adversarial refuter)

Date: 2026-08-17. Role: adversarial refuter, dual-seed batch, S-FOUNDATIONS
hypothesis audit. Sources: in-repo record only (M0, problem book D1,
claims registry). No external tools installed; no environment mutation.

## 0. Target claim (verbatim, standalone)

> "For rotating detonation engine nozzle design, the interface data
> family may be taken INDEPENDENT of the nozzle geometry in ALL
> regimes, including when part of the interface is axially subsonic,
> because detonation products always exit the combustor supersonically;
> rigor class THEOREM, no monitor needed."

The claim has four load-bearing components:
 (C1) independence of the data family from nozzle geometry Sigma in ALL
      regimes;
 (C2) validity extends to interfaces with axially subsonic patches;
 (C3) justification: "detonation products always exit the combustor
      supersonically";
 (C4) grading: THEOREM, with NO monitor required.

Verdict up front: **REFUTED-AS-GRADED**. Every component fails against
the committed record; C2 and C3 are contradicted by theorems and
definitions of record, C3 additionally rests on a frame conflation the
problem book explicitly forbids, and C4 contradicts a mandatory-monitor
clause in M0. Details and anchors follow.

## 1. Objection O1 — The physical premise (C3) is false, and false by
##    the record's own taxonomy

The premise "detonation products always exit the combustor
supersonically" equivocates between RELATIVE (wave-frame / CJ)
supersonicity and AXIAL supersonicity. The problem book was written
precisely to preclude this conflation:

- `docs/rde_nozzle_problem_book.md:257-266` — definitions of record:
  the AXIAL sonic surface u_x = c governs full-state prescription on
  axial interfaces; the RELATIVE sonic surface |w| = c (CJ locus)
  governs operator type only. "EXPLICITLY, to preclude any conflation:
  CJ-sonicity licenses NO axial MOC — axial marching requires u_x > c
  pointwise ... |w| > c only guarantees real Mach cones, whose
  time-like directions in the wave frame are near-azimuthal (helical),
  so no axial plane near the chamber is spacelike even where the
  relative flow is supersonic."

- `docs/rde_nozzle_problem_book.md:294-297` — axially subsonic patches
  are "the GENERIC case for raw chamber-exit data; the patches are
  exactly the CJ-unshielded sectors: fresh fill, deflagrative zone,
  oblique-shock tail." I.e., the record does not merely allow the
  subsonic case — it declares it GENERIC at the raw chamber exit.

So the "because" clause is physically wrong (fresh-fill and
deflagrative sectors are not detonation-processed supersonic exhaust)
and, even where products ARE CJ-supersonic in the relative frame, that
supersonicity is the WRONG kind: it does not deliver the axial
causal shielding the independence claim needs. A premise that is false
in the record's own vocabulary cannot ground a THEOREM.

## 2. Objection O2 — C1+C2 contradict the interface contract of record
##    (D-CONTRACT / L4-default)

M0 D2.4 (`docs/rde_nozzle_MASTER.md:116-137`) is the interface
contract of record:

- Full-state data are licensed "only on axially supersonic patches —
  see L4; subsonic patches: incoming invariants + impedance closure or
  choking closure, decision tree in D1 §4.3bis" (M0:119-121).
- The L4-DEFAULT note (M0:125-137, dated 2026-08-06) states the exact
  boundary of the theorem-grade regime: on the L4 class (EVERY patch
  axially supersonic WITH MARGIN, standing certificate u_x - c >= delta)
  mdot-independence is EXACT and mean upstream influence is "EXCLUDED
  BY THEOREM ([T-NSW])". Subsonic patches survive only "as a DECLARED
  CASE-CLASS ... whose closures carry H2/H-I2 as class assumptions
  with the existing monitors (choking margin, R2
  characteristic-direction audit) and the documented Verdict
  downgrades."

The record therefore proves independence AS A THEOREM exactly on the
complement of the regime the claim wants to annex, and demotes it to
monitored class-assumption status on the subsonic patches. The claim
"independent in ALL regimes ... THEOREM" erases a scope boundary that
M0 states in a dated, ratified note. Mirrored in the claims registry:
`docs/claims_registry.yaml:121` ("full state only on axially supersonic
patches; declared closure on subsonic patches") and
`docs/claims_registry.yaml:229` (failure channels of the objective
equivalence explicitly include "subsonic interface patches").

## 3. Objection O3 — Named theorem-level counter-consequences of
##    subsonic patches (the claim's conclusion fails, not just its proof)

The record does not merely withhold the theorem on subsonic patches;
it derives POSITIVE Sigma-dependence consequences there:

- `docs/rde_nozzle_MASTER.md:421-425` ([T-O1] failure channels):
  "axially subsonic interface patches can make mdot Sigma-dependent",
  with the contrast stated in the very next sentence: "with a fully
  axially supersonic data interface (L4), (i) and the
  mdot-independence hold EXACTLY."
- `docs/rde_nozzle_problem_book.md:318-326` (mixed-interface
  DOWNGRADES, written into the Verdict): "H-I2 violated on the patches
  (real upstream information flux); H-F1 from THEOREM (q ≡ 0, fully
  supersonic interface) to hypothesis with MEASURED q; Prop. O1 at
  risk (mdot through subsonic sectors may depend on Sigma ...). The
  mathematics loses its theorems exactly where the physics says the
  chamber feels the nozzle — the formalization LOCALIZES the coupling
  channel rather than hiding it."

This is a direct hit: on an axially subsonic patch there is a real
upstream (nozzle -> chamber) information flux — acoustic/entropy
characteristics run upstream through the interface — so the data
family is COUPLED to Sigma by causality. Independence is not
"unproven" there; its negation is the recorded default, manageable
only via the O1-O4 closures (move Gamma_d, impedance BC, choking
surrogate, implicit anchor), each of which is a DECLARED modeling
closure with monitors, never a theorem.

## 4. Objection O4 — "No monitor needed" contradicts a mandatory
##    clause of the architecture

- `docs/rde_nozzle_MASTER.md:1437-1441` (VI.4bis(v)): "The flatness
  monitor itself is mandatory in every data contract." The T0-flatness
  monitor is the standing purity check of the pure-periodic scope
  (memory `periodic-wave-data-scope`; M0:108-114 routes mode
  transitions to the robust layer, "never silently averaged").
- On the subsonic case-class specifically, the closures "carry H2/H-I2
  as class assumptions with the existing monitors (choking margin, R2
  characteristic-direction audit)" (M0:132-134), and the audited
  quantities include "spacelikeness margin min(M_x - 1) per phase;
  H-I2/choking" (M0:1374).

So even in the regime where independence DOES hold as a theorem (L4),
the contract still requires monitors (flatness; the u_x - c >= delta
margin certificate is itself the monitored license). "No monitor
needed" is wrong in every regime, and doubly wrong in the annexed one.

## 5. Objection O5 — Grading discipline (R5 / claim-dual-proof standard)

Even setting aside content: a THEOREM grade requires explicit
hypotheses and a falsifier (CLAUDE.md R5; claim-dual-proof standard).
The claim states no hypotheses (it asserts "ALL regimes" precisely to
avoid stating the L4 hypothesis that makes the true theorem work), and
its justification (C3) is not a hypothesis but a false empirical
gloss. Under the repo's rigor ladder the honest maximal grade of the
independence statement is:

- THEOREM on the L4 class (axially supersonic with margin) — this is
  [T-NSW] + [T-TH0] L4 note, already of record;
- class-assumption (H2/H-I2, monitored, Verdict-downgraded) on the
  subsonic case-class — never THEOREM, and the O1-O4 decision tree is
  the recorded machinery for exactly this.

The claim as stated is thus a scope-inflation of an existing theorem
past its recorded failure channel, with the monitor clause deleted.

## 6. Steelman check (what would it take for the claim to survive?)

Attempted rescue 1 — "subsonic patches are measure-negligible": the
record prices this as option O3 (choking surrogate, "default when
sigma_sub (mu x area fraction) is small and thrust-lean",
problem_book:312-314) — a DECLARED, MONITORED surrogate with H2
margins, not a theorem, and conditional on smallness that must be
measured, i.e. a monitor. Fails to rescue C4 and the THEOREM grade.

Attempted rescue 2 — "CJ detonation exit is sonic-or-supersonic by
Chapman-Jouguet, so no upstream influence": refuted by O1 — CJ
sonicity is relative-frame; the axial projection is what governs
upstream influence through an axial interface (problem_book:257-266),
and the CJ-unshielded sectors are generically axially subsonic.

Attempted rescue 3 — "take Gamma_d far enough downstream that
everything is axially supersonic": that is exactly option O1 of the
decision tree — and it makes the data family depend on WHERE the
interface sits and freezes the intervening wall ("full rigor on a
reduced design class", problem_book:302-306). It recovers the theorem
by RESTRICTING the regime, which is the negation of "ALL regimes".

No rescue survives. The claim is not repairable by wording; its
quantifier ("ALL regimes") and its grade ("THEOREM, no monitor") are
each individually false against the record.

## 7. Verdict

**REFUTED-AS-GRADED.** The true statement of record is strictly
weaker: interface-data independence from Sigma is a THEOREM only on
the L4 class (every patch axially supersonic with margin, [T-NSW] /
[T-TH0] L4 note, M0 D2.4), always under the mandatory data-contract
monitors (T0 flatness; u_x - c >= delta margin); on axially subsonic
patches — the generic raw chamber-exit case — independence FAILS
(real upstream information flux, H-I2 violated, mdot possibly
Sigma-dependent, H-F1 demoted to measured-q hypothesis) and is
recoverable only through the declared, monitored O1-O4 closures. The
claim's physical premise conflates relative (CJ) with axial
supersonicity, a conflation the problem book explicitly forbids.

Anchors: docs/rde_nozzle_MASTER.md:116-137, 421-425, 1437-1441, 1374;
docs/rde_nozzle_problem_book.md:255-326; docs/claims_registry.yaml:121,
229; docs/rde_nozzle_hypothesis_ledger.md:114.
