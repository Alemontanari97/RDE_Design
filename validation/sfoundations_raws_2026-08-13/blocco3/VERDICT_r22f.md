# VERDICT — R22-F CENTERPIECE CLOSURE (S-FOUNDATIONS-C4, Blocco 1 v2)

Role: R22F CLOSURE JUDGE. Session 2026-08-20. Loop of record:
until-dry FULL, three lenses (L0 variational / L1 PDE-hyperbolic /
L2 asymptotics-measure-scaling), rounds cap 4. Loop ended:
dry = false, rounds = 4, aborted = false (structured claim,
cross-checked in §3 below).

Target of record: validation/sfoundations_raws_2026-08-13/phaseD/
phaseD_r22f_centerpiece.md (author draft revision 1 + reviser passes
[REV2-r1-0..21], [REV2-r2-0..8], [REV2-r3-0..10], [REV2-r4-0..6];
2175 lines at closure [J-V2: measured `grep -c ""` this window],
incl. §9 graft table and §§10-13 disposition tables).

READ-DEPTH DECLARATIONS (this judge window):
- BRIEF_blocco2_phaseD.md (AS AMENDED): [FULL] (209 lines).
- BRIEF_blocco2_phaseD_addendum_c4.md: [FULL] (46 lines).
- phaseD_r22f_centerpiece.md: [FULL] (all 2176 lines, all markers,
  all tables, incl. the Part 5 table row-by-row).
- ALL TWELVE v2 refutation files [FULL]:
  phaseD_r22f_refute_r{1,2,3,4}_l{0,1,2}.md.
- Probe scripts' verdict lines: read for all 14 loop probes
  (r22f_v2_probe_r1_l0_fiber_sign_2eps.py, r1_l1_atom_mass.py,
  r1_l2_{drop_sign,two_eps,richardson_dof}.py,
  r2_l0_activeset_shift.py, r2_l1_interior_margin.py,
  r2_l2_{routed_mass,value_grad_gap}.py,
  r3_l0_nonconvex_feasible.py, r3_l1_gridmin_floor.py,
  r3_l2_epsU_pointwise.py, r4_l0_mu_identity_proxreg.py,
  r4_l2_proxreg_annulus.py) — every one carries an
  ALL-ASSERTS-PASS / PROBE-VERDICT terminal line consistent with the
  consuming refutation's claim; probes were RUN in the refuters'
  windows (of record); none re-run here (no fix below needs one).
- docs/findings_registry.yaml [SLICE :1445-1484] and
  docs/literature_registry.yaml [SLICES: giles_pierce_1997 :984-990,
  wanted_breitkopf_ulbrich :753-759, harroun_2021 :273-284] — read
  for the landing-row formats and current statuses (§7).
- Auxiliary carriers cited as [ADV] per the shared frame; CT-6
  respected throughout this verdict: no number from the four nozzle
  papers enters any bound, band, or cell value herein.

DELIVERY-CHECK (addendum_c4 (c), binding): the no-external-referee
structural declaration IS PRESENT in the forchetta table header
([REV2-r1-15], declared "this paragraph IS the table's header note"),
verbatim-class faithful to addendum_c4 :17-26 (verified by three
refuters at source: r1 fix, r2_l1 L1-11(c), r4_l2 L2-27(f)).
Delivery-check item: PASS.

==============================================================================
# 1. PER-PART RIGOR LABELS (duty i)

Every named statement of Parts 1-5, adjudicated at the class it holds
as printed AT CLOSURE (i.e. with all round-1..4 scopings; superseded
fragments never land). The right-sizing rule of addendum_c4 (b) is
applied to the gradient-level schema and its round-4 extension (L_H):
SCHEMA + named derivers is the accepted dry form there — demanding
closed form would have been a BREAK of the brief, and no lens made
that demand (verified, §2.3).

## Part 1 — [T-DISC]

| Statement | Label | Reason |
|---|---|---|
| D1.1 admissible data class | DEFINITION | consumes standing pins H3/P1/H9 + [MS-T-MEASURE] D.9(ii); h0-convention carried as declared hypothesis switch (D.13 contract fact), not resolved — correct |
| D1.2 p-only projection + [REV2-r1-1] pin | DEFINITION | calibrated-scalars fiber pin (family's own mu-means) — makes eps_fib exactly the B-2-measured object; canonical-constant reading explicitly excluded |
| [T-DISC-1] fiber non-degeneracy | THEOREM* | proof by citation of D.6 THEOREM* + D.10 THEOREM + K-bar=0 (verifier-confirmed, ADVISORY prov.) + P1 non-breaker; conditionals (c1) G-a queued, (c2) H-AM0 per-dataset, (c3) ADVISORY provenance until the R-6 mint — all NAMED; hypotheses H1.1-H1.4 with the H1.3 FOLD-headroom clause (AG-1 valve, declared); falsifier printed |
| [T-DISC-2] leg (i) sign leg | THEOREM* (SCOPED) | exact per-streamline algebra; BOOKING-level under H2.2, on PHYSICAL-h0-FIXED comparisons only ([REV2-r1-2/3]); uncompensated DROP branch geometry-signed with the r_e = r_in degenerate corner named; actual-pair form correctly routed to M-RED/B-2, NOT asserted at theorem grade |
| [T-DISC-2] leg (ii) magnitude | SCALING-ESTIMATE | labeled, not a bound; B2 1.5-3% fold class + B1 companion, verifier-repaired forms, ADVISORY provenance declared |
| [T-DISC-2] LOWER-BOUND READING | split as printed | theorem-grade strictly-positive single-signed floor ONLY on the physical-h0-fixed branch; numeric floor estimate-class until B-2 measures; honest — no numeric lower bound at THEOREM grade |
| [T-DISC-3] 2-epsilon consequence | SCHEMA | two-leg reassembly [REV2-r1-4]: leg (a) per-surrogate upper (claim 10 verbatim, premise (U_G)); leg (b) irreducibility lower (premise (DR) named, midrange osc/2 probe-verified); [REV2-r2-1] corrected parenthetical is the landing form; inter-fiber unboundedness caveat printed — quantifier direction now sound (re-verified by L0/L2 at rounds 2-3) |
| [T-DISC-4] verdict semantics | SCHEMA | dichotomy assembly at the grades of its parts; (a) reads at booking level under the D1.2 pin and cites leg (b) for irreducibility ([REV2-r1-5]); (b) exoneration of the full-state average correctly scoped to the fiber axis; (c) prohibition = PRACTICE (D.12), cited not re-derived |

## Part 2 — [T-RED]

| Statement | Label | Reason |
|---|---|---|
| §2.0 entry contract + owned boundary | contract/PRACTICE | (U) declared OPEN; time-coupling half named G3/corrector-owned, not re-derived (brief order honored); [T-T0P] split-gap lists transcribed faithfully (L1-6(a) source-verified) |
| [T-RED-1] operator K | DEFINITION; identities THEOREM* (ADVISORY prov.) | wave-frame flux identity machine-witnessed (judgeverify ITEM 3.1) + re-derived by hand by L1 twice; census completeness stays G-f SCHEMA — NOT inflated (correct) |
| [T-RED-2](i) K-bar = 0 | THEOREM* | pen proof + machine witness; holds on full BV (a.c.+Cantor+atoms); ADVISORY provenance until the landing mint (R-6) |
| [T-RED-2](i) two-channel census | THEOREM* (conditional) | conditional on H-RED-2(SBV)/H-RED-3/H-RED-4 ([REV2-r1-6], at-site pointers [REV2-r2-2/4]); the Cantor-channel hole is closed by hypothesis, correctly |
| [T-RED-2](ii) first-order scales | SCALING-ESTIMATE | labeled; verifier-repaired forms only; the chi·beta_tau = beta_w closure is definition-level (stronger, correctly noted) |
| [T-RED-2](iii) on-ray St^2 | LICENSE-GATED (not usable) | X-T3QS-5F gate binding; J1 bar computed never argued away — correct gate discipline |
| [T-RED-2](iv) uniformity | OPEN (declared) | (U) + class-wide H-A1, deciders named |
| §2.2-bis [T-RED-2G] gradient-level schema | SCHEMA | the addendum (b) right-sized deliverable: delta defined via Moreau/support-function typing (B), evaluated at S*_red ([REV2-r3-2]); licensed forms (T)/(C) with cone-pairing rule (A); hypotheses H-G1..H-G6; three named derivers; NO closed form claimed. Round-4 completions: mu = J_TRUE curvature floor at every curvature sentence ([REV2-r4-1](a)); H-G6 curvature transfer with L_H UNDERIVED (SCHEMA + 3 named derivers, mirror of R-9) ([REV2-r4-1](b)); H-G5 convexity-only licensing ([REV2-r4-2]) |
| (F) value-route argmax-shift lemma | SCHEMA | algebra re-derived by L1 (r3 L1-15(d)) and L0 (r3 L0-18(b)), probe-verified with rate shown tight; measured-carrier-sound (J_red-side derivation, [REV2-r4-1](d)) — the ONLY route executable on the measured carrier today; eps_U at SAMPLED-SUP (estimate) class with refinement-stability license, instantiates-never-discharges ([REV2-r4-3]) |
| §2.3 physical exhibit (Harroun Fig. 18) + [GRAFT-G01] family | evidence exhibit ([PAGE]/[ADV-FIG]) | page-verified at source (r1 L1-6(d)); CONNECTION re-scoped to the K-carried subset with the D-4 misfiling guard honored ([REV2-r1-10]); per-term disposition table grades correct under the [REV2-r1-9] joint-nullity readings; CT-6 clean (swept every round). NOTE: the section HEADER is mechanically missing at closure — judge finding J-1, §5 |
| §2.4 G-c leg (ii) adjudication | DISCHARGE (citation-grade) | see the greppable disposition in §6; limits L1 (mechanism citation, not a theorem), L2 (rate constant stays [INF]), L3 (corrugated-sonic locus NOT covered, [REV2-r1-11]) all binding |
| §2.5 rigor summary | as amended | reads with the SBV conditional at-site ([REV2-r2-4]) |
| §2.6 Breitkopf-Ulbrich bearing | [ABS] one-sentence check | named F2 candidate template (g2b/front-differentiability), not consumed — exactly the brief's order |

## Part 3 — [M-RED]

| Statement | Label | Reason |
|---|---|---|
| Part 3 as a whole | PRACTICE (carrier spec) over THEOREM*/SCHEMA inputs | no measurement claimed; execution = F2 duty named (§3.6); claim-1 identity consumed at ADVISORY provenance with the mint riding the landing (R-6) |
| Bands B-1..B-4 + BAND RULE | PRACTICE (derived-band rules, rejectors armed) | zero magic constants verified executable-as-published by L2 probes: >=4-point St-ladder ([REV2-r1-12]); B-2 measure explicit in dmdot ([REV2-r1-13]); B-3 window-complement mass; B-4 registered-window license under the DOMAIN-margin floor ([REV2-r2-5](a)) with the per-mesh ladder re-check ([REV2-r3-5]) |
| Routing/determinacy rules | PRACTICE | MARGIN-EXCLUDED-PHASES bucket (Xi_sub not overloaded, [REV2-r2-5](b)); mu_routed = 0 primary rule in the [REV2-r3-4] aimed/verified timing form; declared marched-sector fallback with the exclusion line in the band algebra ([REV2-r2-5](c)) |
| §3.5 outcome semantics | PRACTICE | both outcomes pre-registered positive (T3-CONTROL); moves forchetta (ii)/(iii) [SE] -> MEASURED per family; class-wide still (U)-gated — correct |

## Part 4 — R22-CFD RE-SCOPE

| Statement | Label | Reason |
|---|---|---|
| CFD-1 / CFD-2 irreducible core | PRACTICE (scheduling-decision INPUT) | no decision taken (owner-field honored); CFD-2's verified limits transcribed faithfully from the confrontation record; dependency/cost/risk lines are presentation, each anchored |
| §4.2 the re-scope's teeth | SCHEMA-level consequence of Parts 1-3 | each "NOT needed for" clause cites the discharging part at its adjudicated grade — no overclaim found by any lens in four rounds |

## Part 5 — FORCHETTA TABLE

Header: the addendum-(c) structural declaration PRESENT ([REV2-r1-15])
+ [GRAFT-G10] nearest-referee enrichment (named and disqualified).
Cell rules enforced; CT-6 verified clean by L2 sweeps at every round
(no P-A..P-D numeral in any cell, bound, or band; the single round-1
leak was stripped, [REV2-r2-6](d)).

| Channel | Label of record | Reason |
|---|---|---|
| (i) time-coupling | BEST: conditional-zero (BOUND class, [T-T0P] SCHEMA strata, gap lists named); WORST: CLASS EXIT, NO number | asserting a number would exceed evidence — correctly refused; guards named |
| (ii) azimuthal reduction | structure THEOREM* (ADVISORY prov.); magnitudes [SE] with the good-fitted-sheet qualifier restored at all three sites ([REV2-r1-7], [REV2-r3-7]) | licensed phrasing verbatim incl. ">10% NOT EXCLUDED off-ray"; St^2 improvement correctly NOT banked (license-gated) |
| (iii) swirl content | [SE] magnitudes (B1-B5 repaired forms); sign leg THEOREM* under the [REV2-r1-2] scope ([REV2-r1-18](b)); shroud marker [REP] page-verified | MANDATORY worst-direction marker PRESENT (Paxson-Miki 58.1% -> ~71.5% of ideal at fixed area ratio, carrier findings_registry.yaml:2026 per [REV2-r1-17]) |
| (iv) averaging adequacy | [REP] external data at verified limits; R26 ranking threshold OPEN | Harroun 1.25-flat correctly read as non-discrimination datum, not proof of blindness |
| (v) model-form bars | measured internal instance ([T-EQBR]) + [REP] + DECLARED ANALOGY (R8 nozzleless->plug) | nothing above held class |
| (vi) OPTIMUM-SHIFT | SCHEMA both routes; delta AND L_H UNDERIVED — NO argmax-shift number at any grade, none from the measured carrier alone | the sharpest-threat channel lands honest: J_TRUE-floor mu with H-G6-gated carrier; convexity-only H-G5 (prox-regularity does NOT license — probes of record); value route measured-carrier-sound at sampled-sup class; connected-nonconvex no-coverage declared; brief :126 never-value-for-optimum sentence carried |
| §5.1 roll-up + HEADLINE | licensed phrasing, correctly scoped | no fake summation; (vi) seam declared ([REV2-r1-19]); fitted-sheet qualifier in the BEST bullet ([REV2-r3-7]) |

==============================================================================
# 2. FINDINGS LEDGER, AMENDMENTS, AND CONTESTED OBJECTIONS (duty ii)

## 2.1 Complete finding index (no refuter finding absent from files+verdict)

All 66 findings of the loop are ON FILE in the twelve round files and
indexed here (types: B=BREAK, R=REPAIR, A=AMENDMENT, N=NOTE):
- Round 1 (26): L0-1..3 R, L0-4 B, L0-5..6 R, L0-7..8 A, L0-9 N;
  L1-1..3 R, L1-4 A, L1-5 R, L1-6 N; L2-1..6 R, L2-7..9 A, L2-10..11 N.
- Round 2 (17): L0-10 B, L0-11..12 R, L0-13..14 A, L0-15 N; L1-7 R,
  L1-8..10 A, L1-11 N; L2-12 N, L2-13..14 R, L2-15..16 A, L2-17 N.
- Round 3 (13): L0-16 R, L0-17 A, L0-18 N; L1-12..14 A, L1-15 N;
  L2-18 N, L2-19 R, L2-20..22 A, L2-23 N.
- Round 4 (10): L0-19 B, L0-20 R, L0-21 A, L0-22 N; L1-16..17 N;
  L2-24 N, L2-25 B, L2-26 A, L2-27 N.
  [J-V2 COUNT CORRECTION, measured this window (SR-12; same defect
  class as L2-21): the per-round subtotals previously printed
  "(16)"/"(11)" for rounds 2/4; the per-ID lists above were ALWAYS
  correct and the grand totals unchanged — measured per-file header
  census: r2 = 6+5+6 = 17, r4 = 4+2+4 = 10; 26+17+13+10 = 66.]
Totals: 4 BREAKs, 23 REPAIRs, 22 AMENDMENTS, 17 NOTES.
Rounds 1-3 findings: every BREAK/REPAIR disposition was verified
RESOLVED AT ITS EDITED SITE by the following round's refuters (the
per-round PRIOR-OBJECTION VERIFICATION blocks, of record) — I ratify
those chains; no re-litigation is owed or performed. Round-4
dispositions are adjudicated by this verdict (§4).

## 2.2 AMENDMENTS — adjudication (all 22; SR-C4-10 per-amendment
## not-a-BREAK line)

Every amendment was applied by the reviser in-draft; the closure judge
adjudicates each CARRIED (the applied form lands). Not one is
rejected. "NaB" = the explicit not-a-BREAK line.

| ID | Verdict | Reason | NaB (SR-C4-10) |
|---|---|---|---|
| L0-7 | CARRIED ([REV2-r1-1]) | D1.2 pin (own mu-means) makes eps_fib the B-2-measured object — the only reading under which Part 1's scale sentences are non-vacuous | NaB: unpinned default was ambiguity, not a false assertion; no licensed claim was false under either reading before the pin |
| L0-8 | CARRIED ([REV2-r1-8] cond. (1)-(3)) | soundness conditions for a schema that did not yet exist — constructive, correctly filed A | NaB: no row existed to break; conditions were preconditions, not corrections of an asserted falsehood |
| L1-4 | CARRIED ([REV2-r1-9]) | joint-vs-per-part nullity: probe-witnessed; table-cell compression overstated what §2.2(i) held correctly | NaB: the correct joint statement existed in-draft at correct grade; only the compressed cell wording overreached |
| L2-7 | CARRIED ([REV2-r1-13]) | B-2 measure explicit (dmdot = rho u_x dA) — dimensional notation | NaB: intended object unambiguous from leg (i)'s per-streamline form; notation, not content |
| L2-8 | CARRIED ([REV2-r1-7]) | fitted-sheet qualifier restored — citation fidelity of a "verbatim" quote | NaB: the licensed phrasing existed at source; the draft under-quoted, it did not assert a new falsehood as its own |
| L2-9 | CARRIED ([REV2-r1-17]) | carrier name fixed to findings_registry.yaml:2026 (line + content verified exact) | NaB: number and line were exact; only the file name was wrong |
| L0-13 | CARRIED ([REV2-r2-3](E), R-12) | basin-radius deriver named (curvature re-measure ladder, M-RED rider extension) | NaB: an unnamed deriver is an executability gap in a spec, not a false bound |
| L0-14 | CARRIED ([REV2-r2-3](B)(C)) | Moreau/support-function typing declared; mu -> mu_curv rename AT LANDING + sign convention | NaB: type-ambiguity and symbol collision, both resolvable to the sound reading; nothing false asserted |
| L1-8 | CARRIED ([REV2-r2-5](b)(c)) | MARGIN-EXCLUDED-PHASES bucket (Xi_sub definition not overloaded) + coverage accounting | NaB: the load-bearing intent ("never into the march") was sound; misnomer + missing reporting line only |
| L1-9 | CARRIED ([REV2-r2-4]) | §2.5 SBV conditional marked at-site (landing-facing) | NaB: the semantic propagation was fully declared two sections away; protocol, not content |
| L1-10 | CARRIED ([REV2-r2-6](a), joint w/ L2-14) | [SE] tag removed from a gradient-level-void clause; replaced by derivable value-route SCHEMA | NaB: clause was hedged with "NO number asserted" in the same breath — a label defect, not a silent pass-off |
| L2-15 | CARRIED ([REV2-r2-2]/[REV2-r2-4]) | same at-site protocol fix as L1-9, second site | NaB: as L1-9 |
| L2-16 | CARRIED ([REV2-r2-6](d)) | "P-A 4%" numeral stripped from the (vi) cell, confined to [GRAFT-G07] | NaB: numeral was a gap-scale [ADV] marker citation within CT-6's letter; bright-line hygiene, cell value untouched ("delta UNDERIVED") |
| L0-17 | CARRIED ([REV2-r3-2]) | S*_red evaluation pin — the only computable choice, exactly what the VI chain consumes | NaB: pin of an implicit-but-forced reading; no other evaluation was licensed anywhere |
| L1-12 | CARRIED ([REV2-r3-4], joint w/ L2-22) | primary-rule timing reword (aimed-at-synthesis / verified-post-march) | NaB: detection instrument mandatory and exclusions declared-never-silent — the hole never reopened; timing wording only |
| L1-13 | CARRIED ([REV2-r3-5], R-15) | floor certificate tied to the registered o32 refinement ladder (probe: 1000x collapse of a sub-grid strip) | NaB: hypothesis (continuum min >= m0) was exactly right; M-RED is a spec, the missing piece was one instrument clause, load-bearing only at F2 execution |
| L1-14 | CARRIED ([REV2-r3-3](c), joint w/ L2-19's repair) | value-route a-posteriori check sentence per condition (1)'s own rule | NaB: premise was present in (F); the check sentence was missing, nothing false printed |
| L2-20 | CARRIED ([REV2-r3-7], joint w/ L0-18(g)) | headline fitted-sheet qualifier — third site of the L2-8 class | NaB: same class as L2-8 (AMENDMENT precedent); WORST line and [SE] tag were correct |
| L2-21 | CARRIED ([REV2-r3-8]) | round-2 amendment count 6/6 -> 7/7 at three sites (measured, SR-12 at source); L2-12 NOTE row added | NaB: arithmetic only — no disposition missing or wrong; every one of the seven is in the table with its edit |
| L2-22 | CARRIED ([REV2-r3-4]) | same site/fix as L1-12 | NaB: as L1-12 |
| L0-21 | CARRIED ([REV2-r4-3], joint w/ L2-26 — the STRONGER L2-26 form adopted, CONTAINING L0-21's stability clause; reviser's joint-adjudication note RATIFIED) | sampled sweep-sup is a finite-sample LOWER estimate; stability-under-refinement is the license condition ([REV2-r3-5] pattern, one instrument up) | NaB: nothing false asserted today — the premise was printed OPEN and declared; the defect was one implication in landing-facing text |
| L2-26 | CARRIED ([REV2-r4-3]) | SAMPLED-SUP (estimate) class label + instantiates-never-discharges rule; certified closure stays with (U)/S.22 (R-1) | NaB: route carries [SCHEMA], no number; demanding a certified uniform sup would demand the (U)-class theorem — forbidden regress per the right-sizing rule |

AMENDMENTS CARRIED: 22/22. REJECTED: 0.

## 2.3 CONTESTED / CONTESTED-BY-ADDENDUM-B objections

MEASURED FROM THE FILES (all four disposition tables §§10-13 + all
twelve refutation files): CONTESTED = 0 and CONTESTED-BY-ADDENDUM-B
= 0 in every round. This is not a blanket dismissal — it is a
verified absence: every refutation file carries an explicit
right-sizing-compliance line (e.g. r1_l0 "NOT a demand for a
closed-form gradient bound (SR-C4-13 respected)"; r3_l2 "L2-19
attacks the SOUNDNESS of a printed instantiation identity ...
attackable per the rule's own terms"; r4_l0 "the asked fix is itself
a SCHEMA + named deriver"), and the reviser contested nothing (all
dispositions FIXED/APPLIED). The judge-strain criterion therefore has
zero objections to strain against; there is nothing to sustain or
overrule in this category, and no finding was dismissed by anyone at
any round. SUSTAINED: 0. OVERRULED: 0.

==============================================================================
# 3. DRY CROSS-CHECK (duty iii, SR-C4-11)

Structured claim from the loop driver: dry = false, rounds = 4,
aborted = false, cap = 4.

RECOUNT FROM THE ACTUAL ROUND FILES (final round = round 4; quotes):
- phaseD_r22f_refute_r4_l0.md MACHINE SUMMARY: "breaks = 1
  (R22F-L0-19)"; "repairs = 1 (R22F-L0-20)"; "dry_at_this_lens: NO
  (1 BREAK + 1 REPAIR standing)".
- phaseD_r22f_refute_r4_l1.md MACHINE SUMMARY: "breaks: 0",
  "repairs: 0", "amendments: 0"; "dry_at_this_lens: YES (0 BREAKS,
  0 REPAIRs, 0 AMENDMENTS)".
- phaseD_r22f_refute_r4_l2.md COUNTS: "BREAKS: 1 (L2-25). REPAIRS: 0.
  AMENDMENTS: 1 (L2-26)."; "DRY VERDICT AT THIS LENS: NOT DRY
  (1 BREAK sustained)".
Final-round totals recounted: 2 BREAKs + 1 REPAIR (+2 AMENDMENTS)
filed across the three lenses. The brief's DRY criterion (zero
BREAKS/REPAIRS sustained at ALL THREE lenses in a round) is NOT met
at round 4. Twelve round files exist on disk (r1-r4 x L0/L1/L2),
consistent with rounds = 4 and aborted = false.
VERDICT: the structured dry claim (dry = false) is CONFIRMED against
the files. The reviser's §13 cap-round self-report ("round 4 was NOT
dry at L0/L2") is also consistent.

==============================================================================
# 4. ROUND-4 FIX ADJUDICATION AND NOT-DRY-AT-CAP RESIDUES (duty iv)

The round-4 findings were dispositioned FIXED/APPLIED by the reviser
([REV2-r4-0..6]) but the cap prevented a round-5 refutation of that
new text. The closure judge adjudicates the fixes on their merits:

- R22F-L0-19 (BREAK, mu functional identity) -> fix [REV2-r4-1]
  SUSTAINED AS FIXED: implements the refuter's own fix shape (a)-(d)
  verbatim-class (functional identity at every curvature sentence;
  H-G6 with L_H underived + 3 named derivers; (D) reworded with the
  superseded fragment verbatim; (F) declared measured-carrier-sound
  with the one-line J_red-side derivation). Probe legs A3/A4/A5 are
  the executable witnesses that the corrected family is exact and
  coherent. Cell carriage [REV2-r4-5](a)(c)(d)(f) verified present in
  the (vi) row as printed.
- R22F-L2-25 (BREAK) + R22F-L0-20 (REPAIR), joint -> fix [REV2-r4-2]
  SUSTAINED AS FIXED: H-G5 narrowed to convexity-only licensing
  (Tietze-Nakajima clause retained soundly); prox-regular disjunct
  WITHDRAWN as a licensing branch, retained only as the named F2
  curvature-corrected refinement (R-17); R-14 decider sentence carries
  the does-NOT-license clause with probe citations; connected-
  nonconvex no-coverage extension in [REV2-r3-1](b) tail and the
  WORST cell. Matches both refuters' fix shapes; a strict NARROWING
  that removes the false license without touching any other statement.
- R22F-L0-21 + L2-26 (AMENDMENTS, joint) -> [REV2-r4-3] CARRIED
  (adjudicated in §2.2; the reviser's stronger-form-containment note
  is ratified — L0-21's own reason line concedes nothing false was
  asserted while the premise stays OPEN, which the adopted
  no-discharge form preserves a fortiori).

## Residues at cap (named exactly; held out per the escalation rule;
## NONE label-inflated — no grade in §1 rests on their absence)

- RES-CAP-1 — UNREFUTED ROUND-4 DELTA: the [REV2-r4-1/2/3] text, the
  [REV2-r4-5] (vi)-row cell edits, and the §13 table are
  judge-verified (above) but have had NO refuter round (cap).
  Loop precedent makes this a real exposure: rounds 3 and 4 each
  found defects in text the refuters themselves had prescribed
  (L2-19 on the r2 fix wording; L0-20/L2-25 on the r3 fix wording).
  HELD OUT per the escalation rule: one targeted single-round
  refutation pass restricted to the [REV2-r4-*] delta (three lenses,
  brief-:158-style one-round + auto-escalation form) is owed at the
  next window, before or at the M0 landing of §2.2-bis and the (vi)
  row. Until it runs, those two landing items carry a DECLARED
  "round-4 delta unrefereed" line at the landing site (the other
  landing items are round-3-refereed text and carry no such line).
- RES-CAP-2 = R-16: curvature-transfer residual L_H (H-G6) UNDERIVED
  — SCHEMA + named derivers (X-T3QS-5F Hessian-level bound;
  C51-route-B; M-RED gradient-rider divided-difference extension).
  An acceptable dry outcome per addendum_c4 (b); never label-inflated.
- RES-CAP-3 = R-14 (as reworded [REV2-r4-2](b)): H-G5 convexity
  status of the KS-aggregated fold-margin feasible set at a
  margin-active S* — OPEN; deciders: convexity certificate
  (prox-regularity certificate does NOT license), OR the R-17 F2
  refinement, OR branch-wise value-dominance where a component
  decomposition exists.
- RES-CAP-4 = R-15 (extended): eps_U sweep-sup measurement at
  SAMPLED-SUP class + sweep-refinement stability re-check + per-mesh
  floor-certificate ladder — all named parts of the M-RED §3.6 rider
  (F2).
- RES-CAP-5 = R-17: prox-regular curvature-corrected refinement
  (mu_eff = mu − |lambda*|·kappa_max; SCHEMA) — optional F2
  refinement, NOT a licensing branch until derived.
- RES-CAP-6 = J-1 (JUDGE FINDING, this verdict only — present in no
  round file, recorded here per duty (ii)'s absence rule): the
  "## 2.3" section header and the exhibit paragraph's lead-in words
  were mechanically CLOBBERED by the round-4 in-place insertion — at
  closure the [REV2-r4-3] block's final sentence runs directly into
  "Harroun 2021 Fig. 18, printed p. 669 ..." (draft :956), and grep
  confirms no "## 2.3" header exists in the file, while §2.2-bis,
  the (ii) WORST cell ("page-verified §2.3"), and §9 all reference
  §2.3. CONTENT IS INTACT (exhibit paragraph, [GRAFT-G01] family,
  CONNECTION block, per-term disposition table all present and
  unchanged since round 1's verification). DISPOSITION: editorial
  repair REQUIRED AT LANDING — restore the header line
  "## 2.3 [T-RED-3] Physical exhibit of record + per-term
  disposition" (and the lead-in "PHYSICAL EXHIBIT OF RECORD
  (page-verified this window):") immediately before "Harroun 2021
  Fig. 18, printed p. 669" via an append-only [REV2-J1] marker
  quoting this verdict. Not a content BREAK; a document-integrity
  defect of the final splice.
Standing residues R-1..R-13 (§6 of the draft) are NAMED there with
deciders and are not cap residues; they carry unchanged.

FORWARDED RECORD-SIDE NOTE (from L2-10, [REV2-r1-21]): the M0 D.10
row's "~4x / 0.3-2.5%" internal tension is a RECORD-side blemish
(nominal ~4x of 3-6% = 0.75-1.5%; judgeverify computed 0.45-2%). The
draft cites the record faithfully and needs no edit; the landing
window should carry a one-line reconcile note to the M0 D.10 row
owner. Recorded here so the finding is absent from neither the round
files nor this verdict.

==============================================================================
# 5. ESCALATION / PROCESS NOTES

- Loop shape of record: 4 rounds x 3 lenses, 12 refutation files, 14
  probes (all RUN in their windows, ALL-ASSERTS-PASS verdict lines
  verified), 22 amendments, 4 BREAKs (all fixed in-loop or
  judge-sustained at cap), 23 REPAIRs (all fixed; every rounds-1-3
  fix verified at-site by the next round's refuters). Persisting
  prior objections re-counted by refuters: 1 total across the loop
  (L0-6 limb -> L0-12, closed at round 2); 0 at rounds 3-4.
- Right-sizing (addendum (b)) was honored by all parties in all
  rounds: no lens demanded a closed-form gradient bound; the
  gradient-level SCHEMA + named derivers (delta, and at round 4 L_H)
  is the accepted dry form, adjudicated at SCHEMA here — label
  inflation checked in both directions (no [SE] tag survives on a
  derivation-void clause; no SCHEMA is presented as a bound).
- The escalation rule is exercised ONLY as RES-CAP-1 (targeted
  round-4-delta refutation pass); nothing else escalates. No residue
  is label-inflated into the grades of §1.

==============================================================================
# 6. G-c LEG (ii) DISPOSITION (duty v, SR-C4-18 — greppable)

G-c leg (ii): DISCHARGED-citable — SUSTAINED by this verdict. The
Giles & Pierce 1997 [FULL] read (all 17 pages) found the
region-of-influence argument in citable form (§3.2 + Fig. 1,
pp. 12-13: Mach-line influence reaching the sonic line unless the
sonic line is perpendicular to the streamlines; "lateral pressure
relief mechanism prevents the singular response"), source-verified
verbatim at the PDF by the L1 refuter (r1 L1-3, quotes checked
against pp. 12-14) and unchanged through all four rounds. Applied to
the program's orthogonal-by-construction Sauer IVL, it supports the
quasi-1D log model at the exposed strip — the advisory §3.25
standing assumption is now literature-anchored. DECLARED LIMITS
BINDING: L1 (the paper's 2D statement is self-graded heuristic — the
discharge licenses the MECHANISM citation, not a theorem); L2 (the
quantitative ≈4x ln-budget constant stays [INF]; conversion =
X-GP01, R27 leg (i), R-4 — UNCHANGED, still open); L3 (the
interface-side corrugated-sonic locus is NOT covered by this
discharge — gated by the domain-margin floor m0 and X-GP01,
[REV2-r1-11]/[REV2-r2-5](a)). Registry and lit-registry row updates
ride the landing (§7).

==============================================================================
# 7. LANDING LIST (duty vi — exact sites + verbatim row texts;
# orchestrator applies verbatim; SR-C4-17 honored: the forchetta's
# landing site is NAMED)

## 7.1 M0 insertions (docs/rde_nozzle_MASTER.md)

L-A [T-DISC] -> M0 Part III, NEW BLOCK inserted immediately AFTER the
T-T3-MAP block (i.e. after M0:943 [J-V2 ANCHOR CORRECTION, measured
this window: the T-T3-MAP block runs M0:854-:943 and ends with the
Harroun clause of record; PROTOCOL T3-CONTROL begins at M0:945 — the
previously printed ":919" fell INSIDE the block and must not be used],
between the block and PROTOCOL T3-CONTROL, adjacent to the breaker
census it completes with the projection axis). Content: [T-DISC-1/2/3/4] as
printed AT CLOSURE with grades per §1 of this verdict and ALL
scopings ([REV2-r1-1..5], [REV2-r2-1]); the superseded sentences
NEVER land ([REV2-r1-21]/[REV2-r2-8](b) binding).

L-B [T-RED] + §2.2-bis -> M0 D.18 cross-reference site
([MS-DEF-KRES] block, M0:1173-1183): replace the "NOT transcribed
here" pointer content with the explicit operator, hypothesis lists
(incl. H-RED-2(SBV)), the two-channel THEOREM* with its conditional
list in the [REV2-r2-4] form, the per-term disposition table
([REV2-r1-9/10] readings), and §2.2-bis AS AMENDED THROUGH
[REV2-r4-1/2/3] — executing AT LANDING: the mu -> mu_curv rename
carrying the J_TRUE functional identity ([REV2-r2-3](C) +
[REV2-r4-1](a)); H-G6 + R-16; convexity-only H-G5 (R-17 as the named
F2 refinement); eps_U SAMPLED-SUP class + stability clause. K-bar=0
MINT at record grade executes here (R-6), retiring the ADVISORY-
provenance conditional (c3) of [T-DISC-1] and the §2.2(i) provenance
line in the same edit. CARRY the RES-CAP-1 "round-4 delta
unrefereed" declared line on §2.2-bis and the (vi) row only.
EDITORIAL PRE-STEP (J-1): restore the "## 2.3" header in the
centerpiece file per RES-CAP-6 before transcription.

L-C FORCHETTA TABLE — LANDING SITE NAMED (SR-C4-17):
docs/rde_nozzle_MASTER.md, Part III, NEW SECTION titled
"[R22F-FORCHETTA] — Adequacy bracket of record (2D-per-phase-averaged
vs 3D-unsteady; user-facing)", placed immediately AFTER the new
[T-DISC] block of L-A (so it sits beside T-T3-MAP and the breaker
census its channels consume), with a one-line cross-pointer FROM the
D.18/[MS-DEF-KRES] site of L-B ("channels (ii)/(vi) quantified face:
see [R22F-FORCHETTA], Part III"). Content transcribed VERBATIM from
Part 5 at closure: the [REV2-r1-15] header declaration (addendum-(c)
sentence of record), the [GRAFT-G10] enrichment note, the CELL RULES
line, the six-channel table with the [REV2-r4-5] cell readings, the
notes blocks [GRAFT-G02..G07] under their CT-6 ceiling banner, and
§5.1 (roll-up + headline with the fitted-sheet qualifier). This
table is the user-facing adequacy bracket of record until
M-RED/R22-CFD tighten it (post-close addendum C3 mandate).

L-D M-RED SPEC: the carrier of record REMAINS
validation/sfoundations_raws_2026-08-13/phaseD/
phaseD_r22f_centerpiece.md Part 3 (spec, not theory) — M0 receives
ONE pointer line at the L-B site: "Residual-functional measurement
spec (M-RED, bands B-1..B-4, F2 execution): centerpiece Part 3, of
record." The F2 duty enters the registry (row 3 below). The
[GRAFT-G05] landing rider [REV-NRS-5] executes here too: P-B F-01
(time-averaged stagnation constraints "empirically recognized",
citing P-D) = one candidate cross-cite line in the M0 T-T3-MAP
context, [ADV] provenance.

L-E Part 4 = the R22-CFD scheduling-decision dossier for the user
touchpoint — NOT landed in M0; the orchestrator presents it (per the
mandate row's owner field, decision post-convergence).

L-F record-side note: one-line reconcile flag to the M0 D.10 row
("~4x of 3-6% vs printed 0.3-2.5% vs judgeverify 0.45-2%" — L2-10,
forwarded §4).

## 7.2 findings_registry.yaml — verbatim row texts

(1) UPDATE existing row id theory:r22-formal-decomposition
(:1459-1467): ADD field (verbatim):

  evidence: "S-FOUNDATIONS-C4 Blocco 1 v2 EXECUTED to cap-4 (2026-08-20; carrier validation/sfoundations_raws_2026-08-13/phaseD/phaseD_r22f_centerpiece.md, closure blocco3/VERDICT_r22f.md): (1) [T-DISC-1] THEOREM* + [T-DISC-2](i) THEOREM* (booking-level, physical-h0-fixed scope) + [T-DISC-3/4] SCHEMA — the p-only reduction CONVICTED with zero CFD, the full-state per-phase average exonerated on the fiber axis; (2) [T-RED] operator DEFINITION + K-bar=0 THEOREM* + two-channel THEOREM* (SBV-conditional) + design-gradient-level SCHEMA (sec.2.2-bis; delta AND L_H underived, named derivers) landed at D.18/[MS-DEF-KRES]; (3) M-RED carrier spec with derived bands B-1..B-4 (F2 duty named); (4) R22-CFD re-scoped to CFD-1/CFD-2, scheduling dossier presented not decided; (5) FORCHETTA adequacy bracket landed M0 Part III [R22F-FORCHETTA]; G-c leg (ii) DISCHARGED-citable (GP1997 sec.3.2+Fig.1 pp.12-13; limits L1/L2/L3; X-GP01 quantitative residue unchanged); NOT-DRY-AT-CAP: 2 BREAKs + 1 REPAIR at round 4, all judge-sustained as fixed; residues RES-CAP-1..6 named in the verdict (round-4 delta unrefereed = the held-out escalation)"

(2) NEW row (verbatim):

  - id: theory:r22f-optimum-shift-gradient-route
    status: CONFIRMED
    severity: medium
    magnitude: "channel (vi) OPTIMUM-SHIFT of record: |argmax shift| <= delta/mu is SCHEMA-licensed only — delta (design-gradient residual, R-9) AND L_H (curvature-transfer residual, H-G6/R-16) UNDERIVED; mu of the licensed gradient-route forms = the J_TRUE curvature floor, and the measured segmented TR-Newton carrier is a J_RED Hessian instantiating it only under H-G6 (mu_eff = mu_meas - L_H) — until L_H lands the gradient route licenses NO number even a-posteriori from the measured carrier alone; the VALUE route (|shift| <= 2*sqrt(eps_U/mu), Theta(sqrt(eps)) tight) is the only measured-carrier-executable route, eps_U instantiated at SAMPLED-SUP (estimate) class under the sweep-refinement stability license, never discharged; licensing requires H-G5 feasible-set CONVEXITY (a prox-regularity certificate does NOT license — probes of record); KS-margin-set convexity at a margin-active S* OPEN (R-14); connected-nonconvex global-argmax coverage NOT claimed by any form"
    source: "validation/sfoundations_raws_2026-08-13/phaseD/phaseD_r22f_centerpiece.md#2.2-bis"
    code: ["validation/sfoundations_raws_2026-08-13/phaseD/r22f_v2_probe_r4_l0_mu_identity_proxreg.py", "validation/sfoundations_raws_2026-08-13/phaseD/r22f_v2_probe_r4_l2_proxreg_annulus.py"]
    mechanism: rigor-gap
    owner: "F2, in order: X-T3QS-5F five-field content bound (value + Hessian level) / C51-route-B / M-RED gradient-measurement rider (centerpiece sec.3.6: delta at S*_red, (E) basin-radius curvature ladder R-12, eps_U sweep-sup R-15, directional Hessian-gap for L_H R-16); O1 discharge gates form (C) at a margin-active S* (R-13)"
    trigger: "any argmax-shift number quoted at any grade; any tightening of the forchetta (vi) cells; M-RED rider execution"

(3) NEW row (verbatim):

  - id: pipeline:m-red-campaign
    status: CONFIRMED
    severity: medium
    magnitude: "M-RED = carrier spec of record (centerpiece Part 3): O5-lite legs (A)-(E) on certified families F-a..F-d with derived bands B-1..B-4 — >=4-point St-ladder Richardson (B-1); E_theta debit in dmdot = rho u_x dA (B-2); channel-split window-complement mass (B-3); registered h-independent window under the marched-DOMAIN margin floor m0 with per-mesh ladder re-check (B-4); MARGIN-EXCLUDED-PHASES bucket (Xi_sub not overloaded); mu_routed = 0 primary rule (aimed at synthesis, verified by the post-march one-scan) with declared marched-sector fallback; outcomes move forchetta channels (ii)/(iii) from SCALING-ESTIMATE to MEASURED per family (class-wide still (U)-gated); both outcomes pre-registered positive (T3-CONTROL)"
    source: "validation/sfoundations_raws_2026-08-13/phaseD/phaseD_r22f_centerpiece.md#PART 3"
    code: []
    mechanism: instrumentation-gap
    owner: "F2 queue: 'M-RED campaign (O5-lite (A)-(E) on families F-a..F-d with bands B-1..B-4)' + the sec.3.6 gradient-measurement rider — beside X-T3QS-5F and the S.22 sub-scope theorem; runs under G1 + the T3-CONTROL protocol row; blocking pre-run pins B-1/B-2 (D.13 contract rows) + (J)/(H) a.c.-only convention"
    trigger: "F2 entry; any consumption of a forchetta (ii)/(iii) MEASURED reading"

(4) R27 carrier update (ADVISORY_litreview_confrontation
:1154 mirror / wherever R27 is tracked) — append (verbatim):
"R27 leg (ii) DISCHARGED-citable 2026-08-20 (R22F centerpiece §2.4;
VERDICT_r22f §6): GP1997 §3.2 + Fig. 1 (pp. 12-13) read [FULL];
applied to the orthogonal-by-construction Sauer IVL the
lateral-relief escape is unavailable at the exposed strip — the
quasi-1D log model is literature-anchored. Leg (i) quantitative
residue (≈4x [INF] constant; X-GP01) UNCHANGED. New limit L3: the
interface-side corrugated-sonic locus is NOT covered by this
discharge (domain-margin gate m0 + X-GP01 deciders)."

## 7.3 literature_registry.yaml — lit promotions (earned by reads,
## with where_read + pages)

(a) id giles_pierce_1997 — PROMOTION READ-PARTIAL -> READ-INTEGRAL
(earned by the [FULL] read, all 17 pages). Verbatim edits:
  status: READ-INTEGRAL
  where_read: APPEND
    - "validation/sfoundations_raws_2026-08-13/phaseD/phaseD_r22f_centerpiece.md#2.4"
  summary: "Green's-function adjoint construction; quasi-1D sonic-throat logarithmic singularity (sec.3.1.1 pp.11-12) with shock continuity (sec.3.1.2 p.12); the 2D region-of-influence / lateral-pressure-relief dichotomy keyed on sonic-line/streamline obliquity (sec.3.2 + Fig.1 pp.12-13; self-graded heuristic); stagnation-streamline n^{-1/2} singularity (pp.14-15). Basis of the G-c leg-(ii) DISCHARGED-citable verdict (R22F centerpiece sec.2.4, all 17 pages read 2026-08-20)."

(b) id wanted_breitkopf_ulbrich — NO status promotion ([ABS] does not
exceed READ-PARTIAL). APPEND where_read:
    - "validation/sfoundations_raws_2026-08-13/phaseD/phaseD_r22f_centerpiece.md#2.6"
and append to identity: "; R22F bearing check 2026-08-20 ([ABS],
p.1 of 34): C1 shock-position/inter-shock-state dependence via
reference-space front-fixing transformation — retained as named F2
candidate TEMPLATE for the front-differentiability duties
(g2b/contact-crossing calculus; M-RED leg (E) fitted-sheet
sensitivity), NOT consumed."

(c) id harroun_2021 — status READ-INTEGRAL unchanged. APPEND
where_read:
    - "validation/sfoundations_raws_2026-08-13/phaseD/phaseD_r22f_centerpiece.md#2.3-exhibit"
(Fig. 18, printed p. 669 = PDF p. 10, page-rendered and re-verified
2026-08-20; the physical exhibit of record for the [T-RED] phenomenon
class, verbatim quote checked at source.)

No other lit promotions are earned: all other sources were consumed
BY CITATION from documents of record (declared in the draft's
read-depth block); the four NOZZLE_RDE dossier papers stay at their
dossier-established statuses (CT-6 ceiling respected — mechanism/
topology only, no number consumed).

==============================================================================
# 8. MACHINE SUMMARY (duty vii)

verdict: NOT-DRY-AT-CAP; all cap-round findings judge-adjudicated
  FIXED/CARRIED; deliverable APPROVED FOR LANDING with the RES-CAP-1
  declared line on §2.2-bis + the (vi) row and the J-1 editorial
  header repair executed first
dry: false (confirmed against round files; recount §3: r4 = 2 BREAKs
  + 1 REPAIR + 2 AMENDMENTS across L0/L2; L1 dry)
rounds: 4 (cap 4); aborted: false; round files: 12/12 on disk
findings_total: 66 (4 BREAKs, 23 REPAIRs, 22 AMENDMENTS, 17 NOTES)
amendments_carried: 22/22 (0 rejected; per-amendment not-a-BREAK
  lines in §2.2, SR-C4-10)
contested: 0; contested_by_addendum_b: 0 (verified absence, §2.3);
  contested_sustained: 0
g_c_leg_ii: DISCHARGED-citable (limits L1/L2/L3; X-GP01 residue open)
forchetta_landing_site: docs/rde_nozzle_MASTER.md Part III, new
  section [R22F-FORCHETTA] immediately after the new [T-DISC] block
  adjacent to T-T3-MAP; cross-pointer from D.18/[MS-DEF-KRES]
residues: RES-CAP-1 (unrefuted [REV2-r4-*] delta — targeted one-round
  refutation pass owed), RES-CAP-2/R-16 (L_H underived), RES-CAP-3/
  R-14 (KS-margin-set convexity OPEN), RES-CAP-4/R-15 (eps_U
  sampled-sup + ladder re-checks, F2), RES-CAP-5/R-17 (prox-regular
  curvature-corrected refinement, optional F2), RES-CAP-6/J-1
  (missing '## 2.3' header — editorial repair at landing); standing
  R-1..R-13 unchanged
lit_promotions: giles_pierce_1997 -> READ-INTEGRAL (§7.3(a));
  where_read anchors added for breitkopf_ulbrich [ABS] and
  harroun_2021 [PAGE]

==============================================================================
# 9. [J-V2] JUDGE RE-VERIFICATION ADDENDUM (append-only; v2
# continuation window, 2026-08-20 — prior judge window quota-killed
# after writing §§1-8; this window INDEPENDENTLY re-verified every
# load-bearing claim against the primary files before ratifying)

Measured re-verifications (commands run THIS window, SR-12):
- Finding census: `grep -hoE '^#+ R22F-L[0-2]-[0-9]+ — (BREAK|REPAIR|
  AMENDMENT|NOTE)'` over all 12 round files, unique -> 66 findings
  = 4 BREAK / 23 REPAIR / 22 AMENDMENT / 17 NOTE. Grand totals and
  the per-ID round lists of §2.1 CONFIRMED; per-round subtotals for
  rounds 2/4 were misprinted and are CORRECTED in place (17 and 10;
  correction marker in §2.1).
- Amendment set: the 22 AMENDMENT IDs measured from the files match
  the §2.2 table's 22 rows one-for-one (no amendment missing, none
  extra). CARRIED 22/22 stands.
- CONTESTED census: `grep -ci CONTESTED` = 0 in all twelve round
  files; the centerpiece's four disposition tables each print
  "CONTESTED 0; CONTESTED-BY-ADDENDUM-B 0". §2.3's verified-absence
  reading CONFIRMED.
- Dry cross-check quotes (§3): re-grepped verbatim from
  phaseD_r22f_refute_r4_l{0,1,2}.md — "breaks = 1 (R22F-L0-19)" /
  "repairs = 1 (R22F-L0-20)" / "dry_at_this_lens: NO"; "breaks: 0 ...
  dry_at_this_lens: YES"; "BREAKS: 1 (L2-25). REPAIRS: 0.
  AMENDMENTS: 1 (L2-26)." / "NOT DRY (1 BREAK sustained)". Final
  round = 2 BREAKs + 1 REPAIR + 2 AMENDMENTS; dry=false CONFIRMED.
- J-1 (RES-CAP-6): header listing of the centerpiece confirms NO
  "## 2.3" header exists (sections jump 2.2-bis :557 -> 2.4 :1058);
  the [REV2-r4-3] clause runs directly into "Harroun 2021 Fig. 18,
  printed p. 669" at draft :956; exhibit content ([GRAFT-G01] family,
  CONNECTION block, per-term table) intact. Editorial-repair-at-
  landing disposition stands.
- Forchetta mandates at source: [REV2-r1-15] addendum-(c) structural
  declaration present as table-header note (:1461); [GRAFT-G10]
  (:1445); mandatory Paxson-Miki worst-direction marker present in
  the (iii) WORST cell (58.1% -> ~71.5% of ideal at fixed area
  ratio, carrier findings_registry.yaml C25 block at :2026) and
  echoed in the (vi) EMPIRICAL MARKERS; brief-:126 never-value-for-
  optimum sentence carried in the (vi) row; [SE] labels present.
- G-c leg (ii): centerpiece §2.4 verdict line at :1097 ("G-c leg
  (ii) DISCHARGED-citable"); §6 of this verdict re-read against it —
  limits L1/L2/L3 as printed there. CONFIRMED.
- Probes: all 14 loop probe scripts carry terminal pass/verdict
  print lines (ALL ASSERTS PASS / PROBE VERDICT / "ALL PROBE PARTS
  RAN; every assert passed." / "PROBE PASS: all assertions hold.");
  runs are of record in the refuters' windows; none re-run (no fix
  in this verdict needs one).
- Landing anchors measured: findings_registry.yaml mandate row id at
  :1459; literature_registry.yaml ids harroun_2021 :273,
  wanted_breitkopf_ulbrich :753, giles_pierce_1997 :984 (status
  READ-PARTIAL -> promotion direction of §7.3(a) valid); M0
  T-T3-MAP block :854-:943, [MS-DEF-KRES]/D.18 block :1173-1183.
  The L-A anchor ":919" was WRONG (inside the block) and is
  CORRECTED in place to ":943" (marker in §7.1); all other anchors
  verified as printed. Centerpiece length re-measured: 2175 lines
  (corrected in the header block).
- Rigor-label spot-verification at source: [T-DISC-1] THEOREM* with
  named conditionals (:152); K-bar=0 THEOREM* (:1009/:1136);
  §2.2-bis grade SCHEMA with addendum-(b) form declared (:557-566);
  (vi) row cell text carries [REV2-r4-5] readings (delta AND L_H
  UNDERIVED; convexity-only H-G5; SAMPLED-SUP value route). §1's
  labels stand as printed.
Corrections applied this window: THREE, all bookkeeping-class
(per-round subtotals 17/10; L-A anchor :919 -> :943; line count
2176 -> 2175) — none touches any grade, adjudication, residue, or
row text. The verdict of record = §§1-8 as corrected + this addendum.
