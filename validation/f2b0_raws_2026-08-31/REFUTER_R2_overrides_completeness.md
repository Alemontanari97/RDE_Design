# REFUTER R2 — overrides + OUT + completeness + session-prompt refutation (F2-B0 first act)

Date: 2026-08-31. Executor: REFUTER R2 (adversarial plan referee), parts (b)+(c)+(d) of
finding `method:sroadmap-single-author-placements-unrefuted` (findings_registry; owner
"F2-B0 FIRST act"). Written incrementally during the pass.

METHOD. (b) Every row of `docs/ROADMAP_critical_path.md` §3 (89 overrides) opened against
its cited anchor (MAP = `docs/rde_nozzle_pipeline_decision_map.md` line; PROGRESS =
`docs/rde_nozzle_PROGRESS.md` BLOCCATO row; D6 = `docs/rde_nozzle_development_plan.md`
lines; ledger/findings/claims = the YAML rows), verdict CONFIRM or MOVE per row; §4
(73 OUT) checked per class with itemization of every suspicious row. (b2) the two
structural rules (F2 default sub-step; phase-token regex) attacked with samples.
(c) per candidate missing source: concrete check + verdict. (d) the F2-B0 prompt
(`validation/ADVISORY_F2B0_prompt_2026-08-31.md`) checked against D6 + derived roadmap +
PROGRESS + CLAUDE.md R1-R8. Tool, registries, docs NOT edited. No packages installed.
Registry rows were read via the tool's own parsers (read-only:
`sys.path.insert(0,'tools'); import roadmap_derive`) and verified 1:1 against §3/§4.

Verdicts: CONFIRM = anchor says what the reason claims, placement follows, no later
supersession found. MOVE/FLIP = placement flipped, with anchor. AMEND = placement stands
or is undecided but the printed reason/anchor is defective (reason-integrity defect).

---

## (b) The 89 declared overrides — verdict per row

### Nodes (25 rows)

| kind | id | placed at | verdict | anchor checked | note |
|---|---|---|---|---|---|
| node | PIN-WAVE | OUT:standing-user-pin | CONFIRM | MAP :61 (standing pin, corrector re-scoped); memory periodic-wave-data-scope | corrector duty consumers J-CT1/C-P4RZ are placed at F5 — nothing lost |
| node | C54 | OUT:touch-gated | FLIP -> F2.ENGINE | ledger C54 owner "next M0 D2.4 touch"; ledger C53 owner "F2 contract window: a placement-band remark in M0 D2.4" | the "next M0 D2.4 touch" is SCHEDULED inside a placed step: C53's duty writes into M0 D2.4 in the F2 contract window (F2.ENGINE). C54 should ride that window (or the OUT reason must name it). Low severity: C53 drags it in in practice |
| node | C55 | OUT:event-gated | CONFIRM (note) | ledger C55 owner "first multi-point instantiation of P_amb"; ledger header GATED-by-owner clause; D6:1145 (Annex B case D) | the event's phase home (F5, case D) is named in the reason itself; F5 re-budget entry re-reads Annex B, so the duty has a de-facto consumer. Asymmetric with the C54 flip only because case-D input is contingent while the D2.4 touch is scheduled |
| node | CONTRACT-F1..F10-block | F2.ENGINE | CONFIRM | D6:172-176 ("F2a: ... stage-A data-contract audits ... G6 loud-reject operative from HERE") + gate table :290 | |
| node | C49 | F2.REPR | CONFIRM | MAP :73 ("falls to F2 entry if the batch splits"; stage-2 REPRESENTATION row); ledger C49 owner (status MIXED = batch did not close); PROGRESS B19(b) | |
| node | S-5F | F2.REPR | CONFIRM | PROGRESS B15(d) ("S-5F rinviata F2-entry") + B-S5F row + B19(b); MAP :74 | |
| node | ROUTE-B | F2.REPR | CONFIRM | M0:1884-1885, :2177-2178 (deferred deriver, verified in-window); MAP :75; B19(b) ladder branch | |
| node | C51 | F2.REPR | CONFIRM | ledger C51 owner "rung-3a implementation window" (NO phase token — override required); PROGRESS B15(e) "C51 rung-3a F2"; B-S5F item "priorita C51 (confermata rung-3a F2)"; MAP :76 + E29 | |
| node | R22-CFD | F2.CFD-2 | CONFIRM | MAP :77 (USER-DECISION PENDING); PROGRESS B19(a) + B-CFD1 ("SI DECIDE POST-M-RED") | |
| node | C59 | F2.REPR | CONFIRM | MAP :78 (stage-2 row, "F2-entry census window") | |
| node | C28 | F2.ENGINE | CONFIRM | findings driver-nonsmooth:no-B-stationarity-certificate owner verified verbatim "F2 (with the GAP-1 window)" | that findings row itself lands at F2-B0 (trigger "F2 entry") — same-duty objects split across B0/ENGINE, see §b2 |
| node | SDP-CAND-8 | F2-B0 | CONFIRM | MAP :116 ("F2-entry engine census (mint-or-retire)"); PROGRESS NEXT item (3) engine cluster incl. SDP-CAND-8 | |
| node | CLG | F2.ENGINE | CONFIRM | MAP :115 (F2-CLG-SCALE, M0:3853 spec); M0:3768 [LAND-C4-LA4] block verified | |
| node | M-RED | F2.M-RED | CONFIRM | MAP :129 (F2-QUEUED); PROGRESS B19(c) "M-RED resta prima campagna F2" | |
| node | C30 | F2.ENGINE | CONFIRM | ledger C29 owner "F2 duty F2-DUTY-C29-MASKGRAIN"; MAP E22 (C30 lands FIRST) | override REQUIRED (C30 owner has no phase token; status DECIDED but owner non-empty -> no OUT rule) |
| node | R22F-FORCHETTA | F2.M-RED | CONFIRM | MAP :170 ("M-RED campaign + RES-CAP residues") | |
| node | T-DISC | OUT:landed | CONFIRM | MAP :171 (LANDED, open duty "—") | |
| node | OBJ-DOM | F2-B0 | CONFIRM | findings owner/trigger verified ("[OBJ-DOM] ... F2 entry"; "first F2 verdict consuming dJ/dthB") — TODAY at :212-213 | cited ":211-212" is off by one today — anchor-drift class (§b3) |
| node | DELTA-CARRIER | F2.ENGINE | CONFIRM | MAP :173 (SHIP-GATE ARMED, [DC-F2-1..5]) | |
| node | OPTSHIFT | F2.M-RED | CONFIRM | MAP :174 (owner "F2 in order: X-T3QS-5F / C51-route-B / M-RED gradient rider") | |
| node | D-44 | F3.TWIN | CONFIRM (note) | MAP :180; the owner/trigger of record live in findings litreview:residue-r22-r27 (TODAY at :2330, content verified: owner "F2 or F5 (D-44...)", trigger "before any public claim on cycle-average adequacy") | under the DERIVED order the earliest act producing a public adequacy claim is the TWIN verdict (F3.TWIN < F5) — earliest-consumer reading. Cited line ":1468" is STALE (today an unrelated row) — anchor-drift class |
| node | P34 | PAPER | CONFIRM | MAP :181 ("P-1/G5-G6 claims window"); findings claims:engine-level-staged... owner verified (today :2738) | |
| node | H20 | F3.PLUG | CONFIRM (strong) | D6:214-232 (F3 EXIT = certified plug optimum; plume-boundary solve is its prerequisite); findings plan:h20-c61-registry-homing OPEN critical at F3.PLUG carries the conflict; registry homing text verified (today :2726) | keeping H20 at F4b (non-critical path) would leave the decisive TWIN without a computable truncated-plug plume — exactly the failure class the roadmap exists to prevent |
| node | C61 | F3.PLUG | CONFIRM (strong) | ledger C61 owner "N2/F4b window" verified — the override is HONEST about moving against the registry; same conflict finding; claim C-HT4's falsifier requires a declared p_b closure | truncated-plug Isp (the TWIN quantity) is not computable without p_b — F3.PLUG is REQUIRED for path coherence |
| node | DUTY-10 | F5 | CONFIRM | D6:435-437 (F5b DUTY-10(a)) + :438-439 (F6 DUTY-10(b)) verified; MAP [MAP-AM-1] | the tool's single F5 step covers F5a/F5b — earlier slot correct |

### Ledger (7 rows)

| kind | id | placed at | verdict | anchor checked | note |
|---|---|---|---|---|---|
| ledger | C30 | F2.ENGINE | CONFIRM | as node C30 | |
| ledger | C49 | F2.REPR | CONFIRM | as node C49 | owner literal "falls to F2 entry" would substep to F2-B0; override refines to the representation session, consistent with B16/B19(b) |
| ledger | C51 | F2.REPR | CONFIRM | as node C51 (owner has NO phase token: override required) | |
| ledger | C54 | OUT:touch-gated | FLIP -> F2.ENGINE | as node C54 | |
| ledger | C55 | OUT:event-gated | CONFIRM (note) | as node C55 | |
| ledger | C59 | F2.REPR | CONFIRM | as node C59 | |
| ledger | C61 | F3.PLUG | CONFIRM | as node C61 | without override the literal "F4b" token would place it at F4b — the override is the load-bearing act, carried with the OPEN conflict finding |

### Findings (21 rows)

| kind | id | placed at | verdict | anchor checked | note |
|---|---|---|---|---|---|
| finding | variational-driver:objective-omits-throat-panel | F2-B0 | CONFIRM | owner/trigger :212-213 ("[OBJ-DOM] ... F2 entry") | redundant with substep (trigger "F2 entry" hits the B0 rule) — documentary, correct |
| finding | engine-core:F5-underived-factors | F2.ENGINE | CONFIRM | owner "F2 (derivation paragraph...)"; trigger "F2 engine rebuild window" | ids are NEVER scanned by place() (owner+trigger only) — the "F5" in the id is structurally harmless; override documentary |
| finding | pipeline:Q3-certifiability-composition | F3.TWIN | CONFIRM (note) | trigger "before the first genuinely averaged shape problem (PB-2 class)"; owner literal "F5 entry (pre-F5 obligation)" | under the DERIVED order the first PB-2-class averaged shape problem is the TWIN (F3 < F5): the override is the conservative EARLIER placement; the owner literal alone would consume it too late |
| finding | engine-core:F3-table-clamp-silent | F2.ENGINE | CONFIRM | owner "...owner F2 - traced min/max-T"; trigger "F2 engine window / next X-THC1 touch" | id "F3-" never scanned; documentary |
| finding | oracles:a1-gp01-quasi1d-not-built | F2-B0 | CONFIRM | owner "F2 (D-20, priority)"; trigger "F2 entry (first oracle block)" | redundant with substep; correct |
| finding | oracles:geno-tocnoz-wall-thrust-double-count | F2-B0 | CONFIRM | owner "...impact audit ... F2 entry at the latest"; trigger "...(impact audit fires FIRST)" | I4 baseline = GENO thrust reference; the TWIN protocol consumes it — B0 correct |
| finding | twin-falsifier:c3-mesh-refinement-unadjudicated | F2.ENGINE | CONFIRM | trigger contains "branch F1" — a REAL regex hazard (matches F1, a CLOSED phase); override neutralizes it; owner "F2 (the C7 refine/enriched-class leg)" = engine window | grep probe (§b2): the ONLY open finding with a branch-label token in scanned text |
| finding | litreview:residue-r6-r29-corner-class-and-terminal-face-cone | F3.PLUG | CONFIRM (note) | owner "F2/F3 (R6, H-CLASS re-opening); F2/PB-2 (R29)"; trigger "next PB-2 cone-form derivation touch (R29)" | single-step placement drops the R6/F2 arm — acceptable because that arm (H-CLASS re-opening) is event-gated and mirrored by twin-falsifier:c6-outcome-i-never-reached, PLACED at F2.ENGINE |
| finding | litreview:residue-r8-r23-base-pressure-pb2-blocking | F3.PLUG | CONFIRM | trigger "PB-2 base-pressure closure window" = the C61/N2 window (row today at :2261) | |
| finding | litreview:residue-r22-r27-disentanglement-experiment-and-adjoint-weight-transfer | F3.TWIN | CONFIRM | owner "F2 or F5 (D-44; R22...)" (today :2330); the R22 CFD experiment is covered by the R22-CFD node at F2.CFD-2 (the reason itself names the second consumer) | |
| finding | moc-audit:ledger-c1-thermo-audit-outcome-bundle | F2-B0 | CONFIRM | trigger "(g) next CI/reproducibility audit of CASES/plugnoz" = GENO health step; PROGRESS NEXT (2) + B-GENO | |
| finding | theory:s5f-path-a-freevortex-stratified-gap | F2.REPR | CONFIRM | owner "S-5F decision dossier" (NO phase token: override required, else the row falls OUT) | the row's own text cites "BLOCCATO 14 (d)" where PROGRESS today numbers it B15(d) — registry-internal anchor drift, not a tool defect |
| finding | oracles:root-identity-replay-common-mode | F2.ENGINE | CONFIRM | owner "C20 Tier-0 ... duty F2-C20-CERTQUAL-CAMPAIGN" | |
| finding | theory:r22f-optimum-shift-gradient-route | F2.M-RED | CONFIRM | owner verified verbatim "F2, in order: X-T3QS-5F ... / C51-route-B / M-RED gradient-measurement rider" (today :2703) | redundant (sub-rule would match "M-RED"/"route-B") — documentary |
| finding | plume:free-boundary-solve-mechanics-missing | F3.PLUG | CONFIRM | trigger "first plug/E-D (external-expansion) sector campaign..." — under D6 plug campaigns are F3 (D6:214-232); conflict carried by the homing finding | |
| finding | oracles:o34-gradient-leg-unconsumed | F2-B0 | CONFIRM | trigger "F2 entry (oracle re-baseline)"; PROGRESS NEXT item (5) | |
| finding | plan:h20-c61-registry-homing-f4b-vs-d6-f3-plug | F3.PLUG | CONFIRM | its own owner text: "until then tools/roadmap_derive.py carries the override with this row as its citation" — the self-citation loop is DECLARED in the row of record | |
| finding | plan:full-envelope-tournament-no-named-d6-step | F3.TOURNAMENT | CONFIRM | owner "...until then tools/roadmap_derive.py carries the DERIVED step F3.TOURNAMENT (path non-critical)" | redundant (sub-rule matches "tournament"); documentary |
| finding | plan:representation-ladder-3d-counterpart-no-named-d6-step | F2.REPR | CONFIRM | owner "F2-B0 (the B16/B19(b) session executes it ... naming the step F2.REPR)" | without override the "F2-B0" token would substep to F2-B0; F2.REPR is that same session window modeled as its own step — consistent |
| finding | plan:nasa-3d-moc-tools-adjudication-not-landed | F2.REPR | CONFIRM | owner "...consumed by the F2.REPR session (duty a) and the C12 band duty (duty b)"; trigger "F2.REPR session opening" | |
| finding | method:sroadmap-single-author-placements-unrefuted | F2-B0 | CONFIRM | owner "F2-B0 FIRST act" — this pass executes it | |

### BLOCCATO (5 rows)

| kind | id | placed at | verdict | anchor checked | note |
|---|---|---|---|---|---|
| bloc | B-G5 | PAPER | CONFIRM | D6:289 ("blocks SUBMISSIONS only, never work") + PROGRESS B-G5 (path paper) | |
| bloc | B-RAOPLUG | F3.RK1 | CONFIRM | D6:214-217 (F3 ENTRY: RaoPlug S1/S2 fix OR declared single-oracle status) + :222-223 (de-risk RK1 AUTHORIZED parallel to F2); D6 §6 items 3-4 verified (:830-835) | without override the row's tokens (F3,F3,F2) would double-place it; the RK1 pin is right |
| bloc | B12 | PAPER | CONFIRM | PROGRESS B12 (path paper; "trigger = finestra lit / claim che li cita"); WANTED rows in literature_registry | |
| bloc | B-CFD1 | F2.CFD-2 | CONFIRM (note) | PROGRESS B19(a) + B-CFD1 ("SI DECIDE POST-M-RED"; carrier cites MAP :77) | PROGRESS B-CFD1 carrier cell says "ROADMAP passo F2.CFD-1" — a step id that does NOT exist (step of record = F2.CFD-2). PROGRESS cell defect, F2-B0 hygiene item |
| bloc | B-GENO | F2-B0 | CONFIRM | PROGRESS NEXT item (2) (GENO health at F2 BLOCCO 0; BLOCCATO B-GENO) | |

### Claims (31 rows)

| kind | id | placed at | verdict | anchor checked | note |
|---|---|---|---|---|---|
| claim | C-D25U | F2.ENGINE | CONFIRM | scope = L4 shared conditional; completeness duty = findings foundations-U:U34-C0-bootstrap-circularity (placed F2-B0) | consumer split B0/ENGINE inside F2 — §b2 sub-window scatter note |
| claim | C-MAJDA | F4b | CONFIRM | D6:233-251 (fitted-front certificate class); scope "S1 canonicity ... across fitted shocks" | |
| claim | C-HT4 | F3.PLUG | CONFIRM | falsifier "executable only under a declared base-pressure closure p_b ... EMPIRICAL closure N2" = the C61/N2 window | |
| claim | C-IGMIX | OUT:priced-by-theorem | CONFIRM | falsifier needs a finite-rate computation — outside scope by user declaration (memory scope-pins-frozen-thermally-perfect); T-EQBR (THEOREM*) prices the bracket +6.3..+7.0% | no phase must consume it |
| claim | C-O33 | F2.ENGINE | CONFIRM | re-measure home = C7 refine/enriched-class leg = twin-falsifier:c3 owner (F2.ENGINE) — consistent pair | |
| claim | S-S1U | F2-B0 | CONFIRM + anchor AMEND | placement right (F2 theory window; theory:s-t0p-proof-writeup-pending owner "F2 theory window (first theory block)") — but the printed anchor "findings :1455" is TODAY a DIFFERENT row (a status line of driver-nonsmooth:flip-event-log-omission); the true row sits at :1554 | anchor-drift class (§b3) |
| claim | S-5F | F2.REPR | CONFIRM | PROGRESS B-S5F + B15(d) + B19(b) | |
| claim | S-N6SO | F2.REPR | CONFIRM | the S-5F path-A fork finding is placed F2.REPR; S-N6SO is its classification arm | |
| claim | J-OP11 | F3.TOURNAMENT | CONFIRM | falsifier verbatim "sector tournament with certified delta-bands contradicting the selected topology" | |
| claim | C-EQV2 | OUT:falsifier-executed | CONFIRM | D6:137-159 (F1b STATUS: "The twin RAN ... VERDICT: EQ-v2 = CONJECTURE + H-CLASS"); reopen trigger carried by twin-falsifier:c6-outcome-i-never-reached, PLACED at F2.ENGINE | exemplary OUT: the reopen event has a placed carrier |
| claim | S-BLITE | F6 | CONFIRM | D6:275-278 + §6 item 11 (:1012-1013) | |
| claim | C-P4RZ | F5 | CONFIRM | D6:271-273 (F5b corrector); scope "analytic residual of S-P4F" | |
| claim | S-XCONV | F2.ENGINE | CONFIRM | C28 duties [P-CERTKS] window; carrier X-IVXC in suite | |
| claim | C-XBVP | F4b | AMEND (re-adjudicate) | row verified: it conditions T-XWS — the SHOCK-FREE weak-strong theorem ("C^1 shock-free solution ... vs entropy weak solutions"); residues = (a) convexity (DISCHARGED at instance level via X-IVXC, an F2-suite carrier) + (b) weak-side trace technicalities. NOTHING in the row says F4b; the override's "across fitted fronts" phrase is not the row's text | placement not proven wrong (a fronted certificate-class discharge home is arguable) but rests on an unanchored gloss; candidate re-home = F2 theory window |
| claim | S-D25U-U1 | F2.ENGINE | CONFIRM | scope U1 executed; open residue -c (U5 NAMED MISSING) consumed with the C-D25U completeness duty | |
| claim | S-D25U-U34 | F4b | CONFIRM | D6:233-238 (U3 bordered solve = F4b machinery); scope U3+U4 fronts | |
| claim | S-ACFR | F4b | CONFIRM | scope "a-contraction attack on C-MAJDA/U3 ... extremal fronts only"; carrier X-ACFR | |
| claim | S-GBE | F5 | CONFIRM | findings registry-legacy:GBE-CONCAVITY-NEAR-FLOOR ("pre-F5", trigger "any F5/averaged verdict...") is itself placed F5 — consistent pair | |
| claim | C-MAJDA-3DT | F6 | AMEND (tension to resolve) | row verified: "gap G3 of the [T-T0P] stratum-(B) ledger; OWNER F2; consumed by stratum (B) only". The override reads by discharge machinery (multi-D unsteady Lopatinskii computable only at the F6 3-D/B-lite line) — consistent with the tool's DECLARED claim semantics ("the phase whose work discharges or falsifies") but contradicting the row's literal owner F2, with no superseding record cited | consequence to name: if [T-T0P] stratum (B) must close within F2, an F6-parked G3 makes that impossible by construction; if stratum (B) is deferrable past F2, the roadmap should say so. F2-B0 must re-affirm explicitly |
| claim | C-XINJ | F4b | MOVE -> F2-B0 | row verified: "gap G7 of the [T-T0P] ledger; OWNER F2; consumed at the stop-proof sec.4 endgame ONLY, plus by the G8 falsifier/feasibility gate"; discharge route (r-b) = "certified 1-D root-count over K by interval arithmetic ([X-T0P] item)" — and claim X-T0P is PLACED at F2-B0 | the override's F4b/DUTY-9 (RR/MR) association appears NOWHERE in the row; both named consumers and the named discharge instrument are F2 objects. Under the tool's own discharge semantics this row belongs with the X-T0P battery |
| claim | C-WSF | F4b | CONFIRM (note) | row verified: "gap G11 ... owner F2; ... primary discharge route = the in-house [S-ACFR]" — S-ACFR is F4b-placed and the falsifier needs a certified front INSTANCE (F4b machinery) | under discharge semantics F4b holds; the owner-F2 tension is the same class as C-MAJDA-3DT, but here the named discharge route is itself an F4b object |
| claim | S-T0P-G12 | F2-B0 | CONFIRM | scope "owner F2"; finding theory:s-t0p-proof-writeup-pending (F2 theory window) | |
| claim | X-T0P | F2-B0 | CONFIRM | scope "F2 commit-gated window" (battery build) | |
| claim | S-SDI | F2-B0 | AMEND (reason wrong) | row verified: S-SDI is the SWIRL5F PANEL'S F-2 mint (validation/swirl5f_panel_2026-08-19/), NOT an S-T0P family object as the printed reason states; upgrade path = house until-dry pass (theory window — the placement itself is defensible); it also "newly LICENSES the O5-lite comparison (C)" = an F2.M-RED-consumed license | correct the reason; weigh F2.M-RED as co-consumer |
| claim | C-XBVP-aprime | F4b | MOVE -> F2-B0 (or F2.ENGINE) | row verified: "Consumed by [T-T0P-U]/[T-T0P] stratum (A)" — the SHOCK-FREE stratum — "AND ... the 2-D [T-XWS] sandwich step"; the falsifier list ends "...the [X-T0P] segment line-search falsifier (executable layer, OWNER F2)" | the override calls it "consumed by the F4b certificate class" — contradicted by the row's own consumption statement (stratum A, not fronts); its executable falsifier layer is the F2-B0-placed X-T0P battery. Strongest wrong-direction override found |
| claim | C-R22F-DISC | F2.M-RED | CONFIRM | scope "(c2) H-AM0 ... checked per dataset"; MAP E28 | |
| claim | C-RED-SBV | F2.M-RED | CONFIRM | scope "(U) premise OPEN with deciders named"; MAP E28 (bands B-1/B-3) | |
| claim | C-DCRX-CERT | F2.ENGINE | CONFIRM | MAP :173 ([DC-F2-1..5] certificate-on-entry); M0:2616 [T-DCRX] block verified | |
| claim | T-DISC-3 | F2.M-RED | CONFIRM | M0:1343-1345 verified (forchetta channel chains, (U)-gating via M-RED) | |
| claim | T-DISC-4 | F2.M-RED | CONFIRM | same M0 anchor | |
| claim | T-RED-2G | F2.M-RED | CONFIRM | scope "delta AND L_H UNDERIVED, named derivers only"; M0:2175-2178 verified (deriver chain); MAP :174 | |

### §b OUT ledger (73 rows) — grouped verdicts, every suspicious row itemized

**OUT:decided-no-open-duty nodes (C15, C24, C23, C3, C4, C46) + OUT:decided-no-owner ledger
(C3, C4, C15, C23, C24) — 11 rows: ALL CONFIRM.** Verified via the tool's parsers: each has
status DECIDED with open duty "—"/empty (nodes) or empty owner (ledger). C46 note: the node is
OUT but ledger C46 (owner "F2 window (unassigned) — residual lever only") is PLACED at
F2.ENGINE — the residual lever is carried; deliberate conservative asymmetry (MAP note_C46).

**OUT:landed (T-DISC), OUT:standing-user-pin (PIN-WAVE), OUT:priced-by-theorem (C-IGMIX),
OUT:falsifier-executed (C-EQV2), OUT touch/event C54/C55 (node+ledger):** verdicts as in the
override tables above (C54 x2 = FLIP; the rest CONFIRM).

**OUT:consumed BLOCCATO (B-VENUE, B-G0, B10, B11, B13, B14, B15, B16, B18, B19) — 10 rows:
ALL CONFIRM.** Each stato cell verified in PROGRESS: DECISA S4 / DECISO S10 / CONSUMATA (x5) /
RATIFICATA da B19(b) / CONSUMED CON PIVOT / CONSUMATO. Residue check: B16's execution residue
is consumed by the F2.REPR step (its why cites B16+B19(b)); B19's declared residues are the
separate PLACED rows B-CFD1 and B12. No consumed row hides an unconsumed duty.

**OUT:non-critical-touch-gated findings — 44 rows: 34 CONFIRM, 10 CHALLENGED.**
The dangerous discovery is a SYSTEMATIC false-OUT class caused by the phase-token regex (§b2):
the lookbehind `(?<![\w\-\[])` eats the hyphen of "pre-F5", so a row whose ONLY phase reference
is "pre-F5" carries no token and falls OUT as "touch-gated" although its owner names a
phase-bounded duty (consume BEFORE F5 = F5-entry at the latest). Grep-proven victims (owner
field "pre-F5", no other token, all path non-critical):

| id | owner says | verdict |
|---|---|---|
| cycle-avg-machinery:F2-gamma-ladder-staleness | "pre-F5 (C5): B1-equivalent live guard..." | FLIP -> F5 |
| cycle-avg-machinery:F3-bars-not-all-derived | "audit-P2 C3 remainder -> pre-F5: one-off dense probe..." | FLIP -> F5 |
| cycle-avg-machinery:F4-matched-fixedpoint-sensitivity | "pre-F5 (C5): one extra det_state..." | FLIP -> F5 |
| phase-diagrams:oracle-primary-never-confronted | "pre-F5: cross-record oracle test..." | FLIP -> F5 |
| phase-diagrams:gauge-hypothesis-no-rejector | "pre-F5: persist gauge_margin..." | FLIP -> F5 |
| phase-diagrams:ka-self-inflating-tolerance | "pre-F5: a-priori nested-grid bound..." | FLIP -> F5 |
| phase-diagrams:eps-tolerance-omits-quadrature-bar | "pre-F5: per-cell Richardson bar..."; trigger "the sector tournament consuming premium_bound at face value" | FLIP -> F3.TOURNAMENT (a PLACED step is named in its own trigger; F5 an acceptable fallback) |
| phase-diagrams:interp-bar-covers-only-ceiling-channel | "pre-F5: extend the exact-flash probe..." | FLIP -> F5 |

Control group proving the mechanism: sibling rows with the SAME "pre-F5" owners whose trigger
happens to repeat a bare "F5" token (problem-statement:flatness-monitor-unarmed,
cycle-avg-machinery:F1-dual-route-tautology, cycle-avg-machinery:F6-silent-clamp-unchoked,
problem-statement:pv-bars-no-evaluator, registry-legacy:GBE-CONCAVITY-NEAR-FLOOR) are all
PLACED at F5. The 8 above differ ONLY in not repeating the token. Near-victim saved by another
token: foundations-U:U34-C0-bootstrap-circularity ("pre-F2" eaten; trigger "F2 entry" saves it).

Two more challenged rows outside the pre-F5 class:

| id | why challenged | verdict |
|---|---|---|
| swirl5f:c8-cj-locus-naming-approximate | owner "C51 adjudication window (the loci identification is its direct input)" — C51 is a PLACED object (F2.REPR); a placed window is named as owner, so the row HAS a consuming step and OUT mislabels it | FLIP -> F2.REPR |
| process:orchestrator-acts-file-carrier-sweep | owner/trigger name "Blocco-5 COVERAGE GATE (this session family ... this session or C3)" — a PAST window (S-FOUNDATIONS C3/C4; coverage-gate PASS of record 2026-08-21, PROGRESS R35). A row whose owner window already ran is stale-open, not touch-gated | NOT touch-gated: close-with-evidence or re-home (F2-B0 registry hygiene) |

Remaining 34 OUT:non-critical-touch-gated rows: CONFIRM — each verified as genuinely
touch-gated (next-carrier-touch class: o33/o32/d1 benches, X-IVXC x2, 1E3-prefactor,
qmapping datestamp, q_formal, gamma12 constants, golden-tables, t3-lattice, orphan-lint,
[X-AKNO] x3, joint-refine, dprime-winner, val-diag, F6-node-check, moc-audit d3 sibling),
user/env-gated (conditional:filelock-lru-cap, infra:scheduled-ci-multiplatform), event-gated
(bench:speed-measurement-variance, orchestration:until-dry, bench:campaign-carry,
speed-cond:n3-campaign, twin-falsifier:c5-deeper-jump = GENO-repo-owned), F-SERVICE-windowed
(litreview:graft-a6-a26-a27, graft-a9-a10, graft-a14-a28), or duty-mirrored by a placed object
(conditional:P-TRFLOOR -> ledger C34 duty F2-C34-TRFLOOR-DERIVE at F2.ENGINE; swirl5f:flag3 ->
the St-carrier build named in problem-statement:st-marginal-numbers-uncarried [paper path ->
PAPER]; swirl5f:flag1 problem-book touch; orchestration:spec-seeding standing rule).

**§b measured totals: 89 override rows -> 82 CONFIRM / 2 FLIP (C54 node+ledger) /
2 MOVE (C-XINJ, C-XBVP-aprime) / 3 AMEND (C-MAJDA-3DT, C-XBVP, S-SDI).
73 OUT rows -> 61 CONFIRM / 12 challenged (C54 x2 FLIP; 8 pre-F5 FLIP -> F5 (one preferring
F3.TOURNAMENT); swirl5f:c8-cj-locus FLIP -> F2.REPR; process:orchestrator-acts stale-owner
label defect). All flips are path non-critical except none — no critical object was wrongly
OUT and no wrong-phase critical placement was found.**

---

## (b2) The two structural rules, attacked

### Rule 1 — F2 default substep() -> F2.ENGINE (full replay + samples)

Replayed place() for EVERY open finding without override (script over the tool's own
parsers). Default-to-ENGINE verdict: CORRECT on the sampled engine-family rows
(margin-governor:G1-three-jump-channels, variational-driver:dv-roundtrip...,
cell-cert:certify-no-conditioning-qualification, thermo-bands:bands-not-topology-conditioned,
constraints:multiplier-rejector-missing — all genuinely engine-window work). Two sub-rule
defects found, both OVER-CAPTURE by keyword, neither crossing a phase boundary:

1. CFD-2 sub-rule over-match: `\bCFD\b` fires on incidental dataset mentions.
   - swirl-f2a:angular-momentum-audit-row-missing -> F2.CFD-2 (trigger "...first ingested
     periodic chamber-CFD dataset"). Its owner is "F2a"; its siblings f-swirl-1/f-swirl-2 sit
     at F2.ENGINE; the F2.ENGINE step title itself owns "D.14/D.16 angular-momentum rows"
     (D6 item 17). MOVE -> F2.ENGINE (build at F2a; the CFD dataset is the ARMING event).
   - contract:phase-gauge-jitter-alignment-unpinned -> F2.CFD-2 (trigger "(CFD or rig)").
     Owner literal "F2 contract window"; ledger C50 (F2.ENGINE) is "sequenced with" this row
     — the declared sequencing is broken across sub-steps. MOVE -> F2.ENGINE.
   - contract:design-sweep-invariance-falsifier-missing -> F2.CFD-2: borderline-CONFIRM (the
     multi-geometry ingestion really is the CFD-campaign window; registration duty earlier).
2. F2-B0 sub-rule over-match: any "F2 entry" in a trigger pulls the whole row to B0, so
   same-family siblings split (variational-driver:negative-control-N2-missing at F2-B0 vs
   dv-roundtrip at F2.ENGINE; driver-nonsmooth:no-B-stationarity-certificate at F2-B0 while
   its paired node C28 is at F2.ENGINE; claim C-D25U at F2.ENGINE vs its completeness finding
   at F2-B0; claim S-T0P at F2.ENGINE vs S-T0P-G12/X-T0P/S-SDI at F2-B0). Direction is
   CONSERVATIVE (B0 precedes ENGINE — over-early, never late): no MOVE required, but the
   B0/ENGINE boundary is keyword noise, not adjudication. Same class: the F2.REPR step title
   says "stack C58/C60" while C57/C58/C60/SDP-CAND-8 are consumed at F2-B0 (PROGRESS NEXT(3)
   engine cluster; MAP surface A includes C31, which the roadmap instead lists at F2.ENGINE)
   — authored-title overlap across the same F2-entry window, informational only.
   Verdict: the sub-step split inside F2 is NOISY-BUT-CONSERVATIVE; do not cite sub-step
   membership (B0 vs ENGINE vs CFD-2 lists) as adjudicated fact without the row's own text.
3. BLOCCATO victim of the M-RED sub-rule: B-S5F -> F2.M-RED because its item text contains
   "rung-3a" (the M-RED regex). Its owner is "utente al touchpoint F2-entry (dentro la
   sessione B16)" and EVERY other S-5F object (node, claim, path-A finding) is at F2.REPR.
   MOVE B-S5F -> F2.REPR (needs a BLOC_OVERRIDES row). Non-critical path; real misplacement.

### Rule 2 — phase-token regex PHASE_RX

- Declared exclusions HOLD for the probed classes: grep over ALL open findings owner/trigger
  and ALL open-class claims scope/falsifier/statement for branch-label contexts
  (`branch F<n>`, `F<n>-F<n>`, `leg F<n>`) finds EXACTLY two objects —
  twin-falsifier:c3-mesh-refinement-unadjudicated ("branch F1") and C-EQV2 ("F1-F7" twice) —
  BOTH overridden. Ids are never scanned (place() reads owner+trigger only), so
  "F5-underived"/"F3-table"-class id tokens are structurally harmless; no un-overridden
  victim exists in the current registries. CONFIRM.
- FOUND DEFECT (systemic): the lookbehind `(?<![\w\-\[])` also eats genuine hyphen-joined
  phase references "pre-F5"/"pre-F2"/"post-F2". Result: 8 findings whose ONLY phase reference
  is "pre-F5" fall OUT as "touch-gated" (itemized with FLIP -> F5 in the OUT section above);
  near-victims are saved only by accidental second tokens (U34-C0-bootstrap "pre-F2" saved by
  trigger "F2 entry"). All victims non-critical: no critical-path damage, but the OUT:why
  misdescribes a phase-bounded duty class.
- Atlas-side leak (navigation-only): the en-dash is NOT in the exclusion class, so falsifier
  ranges like "F1–F4" (CH7_averaging_edifice.md :383 — falsifier NUMBERS, not phases) inject
  a spurious F1 mention AND a spurious F4b mention; CH2:493 "[F1/T7-FS + F1/P7]" leaks its
  second token past the `[` exclusion. Affects atlas mention counts (370) and per-step atlas
  navigation lists only — no object placement flows through parse_atlas. LOW.

## (b3) Anchor integrity (systemic note)

Every MAP line anchor cited in §3 was re-verified and HOLDS (MAP :61 :73 :74 :75 :76 :77 :78
:115 :116 :129 :152 :170 :171 :173 :174 :180 :181, E22/E28/E29, [MAP-AM-1]). Every D6 and M0
line anchor checked HOLDS (D6 :37 :55 :91 :101 :137 :160-213 :214-232 :233-251 :252-274
:275-278 :282-290 :289 :345-349 :407-443 :435-439 :646-666 :684-734 :779-782 :830-835
:1012-1042 :1063-1090 :1133-1157 :1142; M0 :1343-1345 :1884-1885 :2175-2178 :2616 :3649
:3768). The FINDINGS-REGISTRY line anchors inherited from the MAP era are STALE: the registry
grew ~240 -> 258 rows since 2026-08-21, shifting rows by ~+100..+210 lines. Checked cases:
":1455" (S-S1U reason) is now a status line of an unrelated row — true row at :1554; ":1468"
(D-44) -> true row at :2330; ":2092" -> :2261; ":2498" -> :2703; ":2519" -> :2726; ":2530"
-> :2738; ":211-212" -> :212-213. In EVERY case the quoted TEXT exists verbatim in the
id-addressed row (verified via the parsers), so no placement falls — but §3 line-number
citations into findings_registry.yaml must be treated as MAP-era and re-derived by id, not
line. Repair candidate for F2-B0: cite registry rows by id (the MAP's own convention).

---

## (c) COMPLETENESS CRITIC — which source is NOT an input of the join?

Join inputs of record (tool header, verified against the code): D6 spine+gates, pipeline
graph JSON (79 nodes), choice ledger (62), findings OPEN rows, claims SCHEMA/CONJECTURE (37),
PROGRESS BLOCCATO (19), atlas phase mentions. Candidates checked one by one:

### (c-i) claims THEOREM* with open conditionals — NOT an input as a class; NOTHING LOST
Enumerated ALL 17 THEOREM* rows (tool parser; class tally 72 PRACTICE / 37 THEOREM /
34 SCHEMA / 17 THEOREM* / 3 CONJECTURE = 163, matches roadmap §7). Checked each for open
conditionals ("pending", "conditional", "residue", "owner F2"):
T-T4 (conditional on the C-HT4 closure -> C-HT4 SCHEMA, PLACED F3.PLUG); T-EQBR (magnitude
guard -> finding audit-scert:teqbr-magnitude-unguarded, PLACED F2-B0); T-LEMA-i/-iii
("component combination pending O3.3" -> C-O33 SCHEMA, PLACED F2.ENGINE); T-LEMA-iv (O3.2
falsifier -> S-LBML falsifier leg, PLACED F2.ENGINE); T-P3 (scoped S21; falsifier executable
on certified data); T-G12S1 (residues R-G12.1..3 -> carried inside C-D25U -c and S-LBML,
both PLACED); T-T7FS (R-T7.1/2 -> C-D25U family, PLACED); T-P7S1 (R-P7.2 named in-row;
certified-argmax question = C28/C38 windows, PLACED); S-P4F (residual MINTED as C-P4RZ,
PLACED F5); T-XWS (conditioned by C-XBVP, PLACED); T-DISC/T-DISC-1/T-DISC-2 (conditional
family MINTED as C-R22F-DISC, PLACED F2.M-RED); T-RED/T-RED-2 (MINTED as C-RED-SBV, PLACED
F2.M-RED); T-DCRX (MINTED as C-DCRX-CERT, PLACED F2.ENGINE).
VERDICT: the "THEOREM* = closed statement" assumption is SAFE TODAY because the registry
discipline mints every open conditional as its own SCHEMA/findings row (which ARE inputs).
RESIDUAL RISK (structural, no current victim): nothing ENFORCES that discipline — a future
THEOREM* with an in-row-only conditional would fall out silently. Improvement candidate:
lint asserting every THEOREM* whose scope/falsifier matches /pending|conditional on|owner
F[0-9]/ names a registered open-class id.

### (c-ii) flag_registry.yaml — NOT an input; NOTHING LOST (check run)
Parsed all 45 rows (keyed `- flag:`; fields flag/default/meaning/read_sites/covering_gate/
tested_pairs/untested_cartesian/note — NO owner, NO trigger, NO status). It is a code
INVENTORY (which gate covers which env flag), not a duty registry. The single duty-bearing
row (A1_VMAP_HESS, gate-rejected default / adoption candidate) is mirrored TWICE in join
inputs: findings engine:vmap-hessian-adjoint-divergence (PLACED F2-B0) and ledger C48
(PLACED F2.ENGINE; "flag A1_VMAP_HESS=1 interim" quoted in the node duty). Untested-cartesian
cells are suite-coverage remarks owned by lint (xx). No open flag lacks a consumer.

### (c-iii) literature_registry.yaml WANTED rows — NOT an input; umbrella coverage verified,
one named near-gap. 178 rows, 80 WANTED (measured this window). Coverage mechanism:
(a) BLOCCATO B12 (PLACED at PAPER; owner/trigger "utente/procurement; finestra lit / claim
che li cita") is the declared umbrella — note its item text names only the P0 subset
(ISABE-2003-117, Bogdanov 2002, Harroun 2019, Shmyglevskii 1962) while the override reason
generalizes to "WANTED procurement rows"; (b) blocking WANTED rows with named consumers all
have PLACED carriers: wanted_kliegel_levine_1969 -> plan:nasa-3d duty (b) [F2.REPR];
wanted_tillyaeva_1975 -> theory:s5f-path-a mixed-lemma (i) [F2.REPR]; Giles-Ulbrich x2 +
Lozano 2019 -> D6 F4b ENTRY gate text, visible in the roadmap's F4b ENTRY cell;
wanted_shmyglevskii_1962 -> litreview:residue-r5-r28 [PAPER]. NAMED NEAR-GAP (no row lost,
binding loose): wanted_li_xu_huang_2022_design_method is the Li-Xu template the F2.CFD-2
step NAMES in its title, yet no placed object binds that procurement to F2.CFD-2 — it rides
only the generic B12 umbrella. Recommend (F2-B0, one line): name it in the CFD-2 brief.

### (c-iv) glossary.yaml — NOT an input; NOTHING LOST (check run)
Navigation object (families/tokens/resolver). The 41 duty-namespace lines (F2-C*-... tokens,
DUTY-1..15) sampled against the ledger: every F2-C* token seen (C9-MESHLAW, C11-ESTIMATOR,
C31-ENGINE-AB, C33-CONSTRHESS, C1-CONTROL-CHART, C2-NOTAKNOT, C20-CERTQUAL, C21-SEEDCERT,
C34-TRFLOOR, C36-DVREFRESH, C41-BAND, C27-AGGCOND) is a PROJECTION of a ledger owner string
that IS a join input (all present in ledger owners, all placed). DUTY-1..15 live in D6
:400-443 (spine text). The glossary adds no independent open duty.

### (c-v) session-log HANDOFF blocks — NOT an input; ONE concrete leak found, consumed by
the prompt's T5 in this very window. Swept the 3 most recent logs + the S4 BUILD_LOG
handoff. PROGRESS_2026-08-21_SfoundationsC4.md HANDOFF carries: (1) "PENDING-DECLARED:
literature_addition_nozzle_rde/ holds ONE file-locked duplicate — delete + rmdir at next
window when the lock clears": NO registry row and NO roadmap object carries this item — it
survived S-PRES and S-ROADMAP unconsumed (still untracked in this session's start git
snapshot). It IS named in the F2-B0 prompt touchpoint T5, and at my check time the directory
is GONE from the working tree (T5 executed in-session). VERDICT: real leak-pattern of the
HANDOFF channel (an item can survive only in prompts), zero remaining loss. (2) The same
HANDOFF's USER ITEMS (G5 send, Lean, procurement, ADR-D4/P-1 calendars) are all mirrored by
PLACED BLOCCATO rows (B-G5, B17, B12, B9). PROGRESS_2026-08-22_Spres1.md HANDOFF: R3-DELEGA
items marked executed 2026-08-23 in the log itself. PROGRESS_2026-08-31_Sroadmap.md: its
handoff IS PROGRESS NEXT (the F2-B0 carrier). S4 BUILD_LOG :534-557 -> PROGRESS NEXT item (8).

### (c-vi) EXTRA candidate found by this critic: the PROGRESS CENSIMENTO table (R1-R38) —
NOT an input; ONE censimento-only open object named. The BLOCCATO table is joined; the
censimento table is NOT, and it carries open SCHED/GATED rows. Mirror check (open rows):
R4c X-T3SI-conv (F5a hard) -> D6 :433-434 duty row + claims falsifier text (:313); R5c/R6c
census-lemma + PAP-RIM (F2-exit) -> F3.TOURNAMENT step why + J-OP11 scope + memory pins;
R9c X-SCANM replay probes (F2) -> findings :598 declared-residual note (owner F2 engine
rebuild; row PLACED); R10 (F2b carrier) -> registry-legacy:FALSIFIERS-WITHOUT-CARRIERS
[PAPER] + D6 F0 text; R11 Lemma-B across-shocks (F5a at latest) -> content carried by
S-LBML/C-MAJDA/T-G12S1 residues (PLACED; the F5a DEADLINE itself lives only in censimento);
R12 a-B2 (F3 entry) -> D6 :415 DUTY-14; R13 -> B-GENO + moc-audit rows; R18 O5 numpy ->
memory + B15 (note: R18 still says GATED while B15 says ADOTTATO — internal PROGRESS
tension, one line to reconcile at R3); R21 -> twin-falsifier:c3 [F2.ENGINE]; R23 C-B/C-C/C-D
-> C25/C26 ledger rows [F2.ENGINE]; R24 contact-front certificates (F4b) -> D6 :246-247 +
litreview:residue-r16 [F4b]. THE ONE UNMIRRORED OBJECT: **R27 "quarantena B1 (identita
(6)-vs-(G) Shmyglevskii)" — QUESTION, falsifier named ([X-VMON] grid), owner F4b, and BY
DECLARATION "NON e' un finding"** — it exists ONLY in the censimento; the roadmap's F4b step
does not list it and no registry row carries it. Not path-critical (F4b, non-critical), but
a genuine open object invisible to the join. Recommend: mint a findings row (path
non-critical, owner F4b) or declare censimento QUESTION rows a join input.

### (c) VERDICT
No CRITICAL object lacks a consuming step from any non-input source. Concrete findings:
1 censimento-only object (R27, F4b, low) + 1 proven-then-consumed HANDOFF leak (C4 duplicate
dir, closed by prompt T5 in-window) + 1 near-gap binding (wanted_li_xu_huang_2022 vs
F2.CFD-2) + 1 structural residual (THEOREM* conditional-minting discipline unenforced by
lint) + the pre-F5 regex class of (b2), already counted in the OUT flips. Each candidate
source was checked CONCRETELY (parse + grep + row-by-row mirror), not by inspection.

---

## (d) Refutation of the F2-B0 session prompt (validation/ADVISORY_F2B0_prompt_2026-08-31.md)

Checked against D6, the derived roadmap, PROGRESS, atlas CH6, problem_book, Annex B, and
CLAUDE.md R1-R8. The prompt is SUBSTANTIVELY CLEAN on all five checks:
(1) NO ordered item names a wrong phase/owner — items 1-10 are all F2-B0-owned per PROGRESS
NEXT (1)-(8) + the ROADMAP F2-B0 row; the engine cluster of item 3 follows MAP surface A +
PROGRESS NEXT(3), which is BETTER grounded than the roadmap's mechanical C31-at-F2.ENGINE
split; item 5's D6 :826-830 re-scope target verified (those lines are the O3.4
gradient-leg clause). (2) Cited files exist — tests/test_claims_lint.py,
tests/test_ondemand_carriers.py, tests/test_roadmap_coverage.py,
validation/RAW_geno_audit_instrumentation_2026-08-13.patch, deck_build/BUILD_LOG.md,
swirl5f_panel_2026-08-19/ all verified on disk; the T3/T5 stray paths (er.name, mailmap.txt,
"t --count HEAD:q", literature_addition_nozzle_rde/, NASA_STUFF_Nozzle_Inlet/,
Three-Dimensional-Nozzle-Design-Code/) existed in the session-start git snapshot and are
GONE at check time = T3/T5 already executed this window, consistent with the T-register in
PROGRESS_2026-08-31_F2B0.md. (3) Counts MATCH the roadmap of record exactly: OPEN 214 =
45/125/44; BLOCCATO 19 [3 critical]; claims 163 [37 open]; "89 override + 73 OUT"; 16 passi;
"45 tag critical" in item 1(a). (4) TWIN protocol item 7 CONSISTENT with D6:219-222 (2-D
truncated-plug shape falsifier BEFORE the first certified plug optimum ships), D6:779-782
VERIFIED VERBATIM ("THRUST-STAND-CLASS accuracy (~0.5-1%). Note only, no row"), Annex B
:1142 VERIFIED (case A; active channels N1, N2 = truncated plug, N4; NOT N3), atlas CH6
:440 / :490-491 / :712 VERIFIED (twin famiglia-vs-I4; "vincoli IDENTICI (stesso eps, L,
chiusura, settore)"; comparator I4 "ZERO computed instances"), problem_book :348 (truncation
L_p + p_b declared (N2)); the "caso B -> flip dei tag contract F2a" clause matches the
roadmap §0 falsifier clause. (5) NO material contradiction with CLAUDE.md R1-R8 (R2 sequence
complete incl. lint xxiv; R8 declaration with consumer/exit-criteria/ceiling; R5/SR-12
measured-number clauses; R7 closure list in item 10; G1 untouched; GENO = T2-only under its
own protocol; Fable pin honored; git pathspec-only).

Findings (all LOW unless noted):

| id | severity | finding | anchor |
|---|---|---|---|
| PROMPT-1 | low | item 9 says "i 5 owner stantii (ROADMAP §5-bis)" — the derived §5-bis has 4 rows (measured: registry-legacy:G12-2B-PHANTOM-CHECK, problem-statement:label-namespace-collisions, problem-statement:geno-line-refs-unpinned, ledger-coherence:d3-claims-field-misnomer). Count not re-measured (SR-12-class slip) | ROADMAP §5-bis vs prompt :100 |
| PROMPT-2 | low-medium | T1's D6-addendum draft is carried as "scratchpad S-ROADMAP d6_addendum_draft.md" — a session-ephemeral path outside the repo record; of-record drafts belong in validation/ (artifact-connectedness rule). Mitigated in fact: the F2-B0 log T1 row records it recovered | prompt :32-36; PROGRESS_2026-08-31_F2B0.md T1 |
| PROMPT-3 | low | item 9 "re-home H20/C61 SOLO se il touchpoint lo decide" references a touchpoint that is NOT in table B (T1-T5); the homing finding's touchpoint of record is F2-exit/F3-entry. Vacuously safe (no T decides it -> no re-home) but imprecise | prompt :100-102 vs findings plan:h20-c61 owner |
| PROMPT-4 | low (upstream of the prompt) | PROGRESS ORA still says "213 OPEN = 44 critical" and "BLOCCATO critical 3" alongside registri "findings 258" — stale by exactly the finding this pass discharges (minted at f1b0871 AFTER the ORA edit): the record today is 259 rows / 214 OPEN / 45 critical (roadmap §7 + prompt header agree). ORA must be re-measured at this session's R3 | PROGRESS ORA :23/:25 vs ROADMAP §7 |
| PROMPT-5 | low | E3 reads "C31/C57/C58/C60 fuori da NEVER" — C31 and C58 are ALREADY MIXED, not NEVER (NEVER set of record: C25 C38 C51 C52 C53 C54 C55 C57 C59 C60 C61 C62); only C57/C60 of the cluster are NEVER. Intent clear (cluster adjudicated, duties measured), wording misstates two current statuses | choice_ledger statuses; MAP §10 tally |

No PROMPT finding is blocking; none touches phase, order, protocol substance, or counts.
The prompt PASSES refutation with the five wording/carrier notes above.

---

## MEASURED TOTALS (this pass)

- Overrides: 89 checked 1:1 -> **82 CONFIRM / 2 FLIP (C54 node + C54 ledger -> F2.ENGINE) /
  2 MOVE (C-XINJ -> F2-B0; C-XBVP-aprime -> F2-B0) / 3 AMEND (C-MAJDA-3DT owner-F2 tension
  to re-affirm; C-XBVP unanchored F4b gloss; S-SDI reason misattributes the family)**.
- OUT rows: 73 checked -> **61 CONFIRM / 12 challenged**: C54 x2 (above); 8 pre-F5 regex
  victims FLIP -> F5 (cycle-avg-machinery:F2-gamma-ladder-staleness, :F3-bars-not-all-derived,
  :F4-matched-fixedpoint-sensitivity; phase-diagrams:oracle-primary-never-confronted,
  :gauge-hypothesis-no-rejector, :ka-self-inflating-tolerance,
  :interp-bar-covers-only-ceiling-channel, and :eps-tolerance-omits-quadrature-bar ->
  F3.TOURNAMENT preferred); swirl5f:c8-cj-locus-naming-approximate FLIP -> F2.REPR;
  process:orchestrator-acts-file-carrier-sweep = stale-owner mislabel (close-with-evidence
  or re-home).
- Sub-step misplacements OUTSIDE the §3/§4 tables (replay of the mechanical rules): **3** —
  B-S5F -> F2.REPR (BLOCCATO, "rung-3a" hijack); swirl-f2a:angular-momentum-audit-row-missing
  -> F2.ENGINE and contract:phase-gauge-jitter-alignment-unpinned -> F2.ENGINE (CFD-keyword
  hijacks).
- CRITICAL-path integrity: **ZERO critical objects wrongly OUT; ZERO wrong-phase critical
  placements found.** All flips are non-critical-path; the two claim MOVEs relocate
  F4b -> F2 (earlier = conservative for the theory window).
- Completeness gaps: **1 censimento-only object (R27, F4b QUESTION, no join carrier) + 1
  HANDOFF leak proven then consumed by prompt T5 (literature_addition_nozzle_rde/) + 1
  near-gap binding (wanted_li_xu_huang_2022 vs F2.CFD-2) + 1 structural residual (THEOREM*
  conditional-minting discipline is convention, not lint)**. flag_registry / glossary /
  literature / HANDOFF / THEOREM* otherwise affirmatively clean per concrete checks.
- Prompt findings: **5 (PROMPT-1..5), all low / low-medium, none blocking; prompt otherwise
  CLEAN on phases, order, counts, TWIN spec, and R1-R8.**
- Systemic repairs recommended to the owner (F2-B0 orchestrator; this pass edited NOTHING
  outside this file): (i) regex — drop `\-` from the lookbehind or special-case
  `(?:pre|post)-F<n>` as a genuine token; (ii) add BLOC override B-S5F -> F2.REPR; (iii) two
  CFD-keyword finding overrides; (iv) C54 -> ride C53's window (or name that window in its
  OUT reason); (v) re-cite findings-registry anchors by id, not MAP-era line numbers;
  (vi) re-adjudicate C-MAJDA-3DT / C-XINJ / C-XBVP-aprime / C-XBVP / S-SDI against their own
  row texts (anchors in the §b claims table); (vii) PROGRESS hygiene: ORA counts (PROMPT-4),
  B-CFD1 carrier cell "F2.CFD-1" -> "F2.CFD-2", R18-vs-B15 O5 tension, R27 mint-or-declare.
