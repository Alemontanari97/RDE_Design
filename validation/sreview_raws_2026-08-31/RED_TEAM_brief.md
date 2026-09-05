# RED TEAM BRIEF — the decisive number, extended from Q2 to Q0 (S-REVIEW order 6; carrier §C.6 + §G.4 + refuter PROMPT-45; 2026-09-05)

Persona: the skeptical JPP referee who will judge the decisive number, with
an RDE test engineer at their elbow. You attack the EXPERIMENT and the
QUESTION, not the machinery: "is this the experiment that convinces me?
which control, which band, which second number would I demand? does it
answer 'how to optimize an RDE nozzle' (Q0) or only 'does cycle design
beat mean design' (Q1)?"

Read (integrally, in this order): `validation/TWIN_PROTOCOL_preregistration_2026-08-31.md`
(the pre-registered decisive comparison: truncated plug, class-A specs-only
data, arm P per-phase vs arm C classical at the mean state, ~1% Isp with
the 0.5-1% thrust-stand band, rejectors R-TWIN-0..6, amendment A-1);
`validation/sreview_raws_2026-08-31/PROBLEM_STATEMENT_agnostic.md` (Q0 as
posed agnostically; §2 objectives, §8 budget, §9 what a referee asks);
`validation/sreview_raws_2026-08-31/st_scoping_number_run.log` (MEASURED
St_n: bell 0.35-0.60 at the record head count; plug class up to 1.41 —
the decisive sector); `docs/rde_nozzle_development_plan.md` :779-786 (G2
value gate, thrust-stand anchor NOTE), :1133-1157 (Annex B data cases);
`docs/rde_nozzle_problem_book.md` :451-478 (§8 St), :522-575 (PB-2 truncated
plug = "first genuinely averaged optimum"); `docs/rde_nozzle_MASTER.md`
:25-62 (the idea: T3/T4 collapse dichotomy, why mean design works on
full-flowing walls and must fail on the truncated plug), :746-760 ([T-T3]
statement), :2294-2310 ([T-T4] statement), :4250-4299 (certificate
version-binding, MEASURED); `docs/choice_ledger.yaml` rows C61 (base-
pressure closure, NEVER; Veen WG10-FAILED; Humphreys x2.45 argmax
sensitivity), C57, C59; `docs/rde_nozzle_pipeline_decision_map.md` Stage 7-8
(OPTSHIFT routes license NO number; D-44 adequacy gate; P34 staged-evidence
hierarchy never adjudicated; H20 free-plume solve homeless); the base-
pressure harvest (grep -rl "BASE_PRESSURE_HARVEST" validation/ and read
it); `validation/ADR_panel_2026-07-16.md` :126-146 (KEY FINDINGS: truncation
default alone decides the SIGN of a spike-vs-CP verdict; base pressure
~1% declared-unmodeled; physical lip vs circular-equivalent length +41%);
the F1b bell twin of record `validation/PROGRESS_2026-08-12_S24_f1b.md`
(search "+0.51%" and "cert-limited"); findings rows in
`docs/findings_registry.yaml` with ids containing `twin-protocol`,
`cert-verdict-recorder-dependence`, `objective-omits-throat-panel`,
`staged-evidence-hierarchy`.

MANDATORY QUESTIONS (each answered with: what the referee asks / what the
record answers today with anchors / the gap / a PROPOSED amendment to the
TWIN protocol §9 (dated, never applied by you) or CONFIRM with reasons /
how it changes the credibility or the cost of answering Q0):
 RT-1 UNCERTAINTY BUDGET BEFORE ANY RUN: is a 1% Isp difference resolvable
      above the sum of (base-pressure closure band on the truncated plug;
      frozen-vs-equilibrium thermochemistry; sensitivity to the shape of the
      cycle weights mu; discretization bands; the O(St) reduction term at the
      MEASURED St of the plug sector)? If the record has no numbers for a
      term, say so and state what would produce them cheaply.
 RT-2 THE STRONGEST OPPONENT: is "classical design at the mean state" the
      arm a competent designer would field? Would a duty-weighted or peak-
      designed classical plug close the gap? Is constraint identity (§5)
      enough, or does the classical arm need its own best truncation and
      base treatment?
 RT-3 EXTERNAL ANCHOR: the comparison lives inside one engine; what
      independent evidence (cross-code, high-fidelity computation,
      experiment) at which accuracy class would you demand before quoting
      the number, and is it inside the budget of the statement §8?
 RT-4 GENERALIZATION FROM n = 1: one propellant, one pressure, one
      geometry — what claim does a MATERIAL result license, and what does a
      SMALL result license? Which second point would you demand?
 RT-5 IS NOZZLE Isp THE RDE LEVER AT ALL (Q0 objective axis): versus
      combustor-side losses, injector backflow, operability — would a
      referee accept mean Isp on the nozzle as THE question, or ask for
      operability/robustness (statement §2 O-b/O-c) first?
 RT-6 Q2 vs Q0: does the truncated-plug head-to-head answer Q0 ("how to
      optimize") or only Q1 ("cycle beats mean")? If a different decisive
      experiment would answer Q0 better at equal cost, name it as a tuple
      (configuration; data class; comparator; metric; accuracy class;
      outcomes).
 RT-7 THE St NUMBER ON THE DECISIVE SECTOR: with St_n up to 1.4 on the
      plug class at the record head count, what must the protocol add
      (corrector term in the band stack, wave-frame evaluation of both
      arms, a lower-head-count instance, or a declared scope) before a
      quoted delta is credible?
 RT-8 REPRODUCIBILITY: the record measured that binary certification
      verdicts near the bound flip with recorder/version; is amendment A-1
      (certify with margin 1/K_RICH under a pinned recorder) enough for a
      referee, and what re-run/pin discipline would you demand for BOTH arms?
 RT-9 NEGATIVE OUTCOME: is the SMALL branch truly publishable as written
      (what would the paper claim, what would a referee ask for)?
 RT-10 ANYTHING ELSE a referee asks first that this list omits.

OUTPUT: write `validation/sreview_raws_2026-08-31/RED_TEAM_decisive_number.md`
(create it; sections RT-1..RT-10, each with the five fields above, plus a
final table "PROPOSED AMENDMENTS TO THE TWIN PROTOCOL (DA RATIFICARE)" with
columns id | amendment | evidence anchor | effect on credibility | effect
on cost, and a final VERDICT line: CONFIRM-with-reasons / AMEND / REPLACE
(with the replacement tuple)). Keep it under ~350 lines. Every [KNOWLEDGE]
claim you make carries author/year and a depth marker; anything not in the
literature registry (`docs/literature_registry.yaml`) is quoted UNVERIFIED.
Do not modify any other file; never install packages; never run git.
