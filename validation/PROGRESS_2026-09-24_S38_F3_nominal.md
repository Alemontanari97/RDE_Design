# S38 — F3 session 2/4: the ideal spike of our world attains the ceiling at the nominal ambient; the tournament's far start is in class (2026-09-24 night, [F3/A1])

Owner's direction: "Committa se tutto è in regola e procedi con F3". Everything of S37 was
already committed and pushed (HEAD bb8d1a7 = origin); nothing was pending. This session is
F3 session 2/4 of the D6 ISS-4 counter. Session mose-a1, main tree `rde-nozzle-program`.
Communication in Italian; this log in English (CLAUDE.md).

## 1. The target and what the record already held
The F3 exit duty still owed after S37: "certified plug optimum ... in derived bands", which
the D6 status of record qualifies as "the tournament-grade A/B at the NOMINAL ambient". Read
before building anything:
- S28 ([X-OWTW], [X-OWO3], [X-OWS3]): value and motion halves on GENO's member, which expands
  to its own lip ambient 0.9949 PA; [X-OWS3] holds the BASIN licence only under [DIR-REOB].
- S29 [X-OWAB] and the owner's read of 16:45 that day: a posing that uses the reference inside
  the search (frozen zone, pinned tip, margin reference, start) gives CONFIRMATIONS of the
  instrument, never tournament rows; "the tournament is X-PTRN".
- S30 [X-PTRN] (`a1_plug_tournament.py`, at the nominal ambient on [X-AFAN]'s member): start A
  (the member) 4/4, "no resolved gain over the member"; starts B (1.5 percent perturbation) and
  C (ramp to the planar streamline, 0.84 m away) DEAD at segment 0, then NOT RESTORABLE with the
  restoration phase added the same day (`_plug_tournament/k81n41_v2/run_campaign_s20_i8_*`).
- RECORD GAP found: [X-PTRN] has NO registry row (the S30 log says "the [X-PTRN] row is coined
  here"; `git log -S "id: X-PTRN"` finds nothing). Not silent to the lint only because no
  docs/*.md brackets it. To be coined in the session that re-runs its derive (a registry row
  needs a pass-of-record date after the last commit of its carrier).

MEASURED FIRST, THEN ABANDONED (declared): a walk design on the [X-RAOSQ] v3 posing with the
member as reference (stages bands/walk, scratch of this session). Its bands (e_rep 2.05e-3 m,
the 8-knot spline's representation error, bands 8-16 mm per direction) put the perturbed and a
uniform-turn start INSIDE every band (0.7x, 0.6x) and the only discriminating generic start, the
chord, is uncertified at K 81 (2.5e10) and folds in region R -- and the posing is the one the
owner's S29 read excludes from tournaments. Its code was removed before the record run.

## 2. [X-OWNM]: the ideal spike attains the [T-GB] ceiling at the nominal ambient, 7/7
`validation/ourworld_nominal.py` + `ourworld_nominal_cases.json` (new). The member = fan_axi at
[X-AFAN]'s record (241 x 241, cert 0.027) in our world at the NOMINAL PA 7.614420e5 Pa (CH4/O2
NASA tables, a variable-gamma gas; inflow Mach 2.0 at the lip); designs marched from the
vertical cut at x0 1.50 m through its field (81 rows), the [X-RAOSQ] v3 representation used
only to march. Above the terminal ray the field at x0 is uniform at (q_e, 0, PA), so J_total =
J + rho_e q_e^2 pi (y_E^2 - y_top^2) is the thrust of everything downstream of the cut, and M0's
Prop. 7 (THEOREM* within [C-GBCS]) bounds it by mdot V_id, V_id = q_at_pa = 2742.136 m/s.

| rung | member cert | min margin in R | J_total [N] | deficit to mdot V_id |
|---|---|---|---|---|
| K 41 | 0.026 | +0.0318 (927 cells) | 1.16186625e8 | -2.347e-3 |
| K 81 | 0.149 | +0.0573 (1936 cells) | 1.16314850e8 | -1.246e-3 |
| K 161 | 0.037 | +0.1013 (3966 cells) | 1.16383701e8 | -6.549e-4 |

- D-1 construction certified; D-2 the member certifies on every rung; D-3 no fold in region R;
  D-4 mass: start line + uniform part = mdot to -1.17e-4, inside the construction's declared
  residuals (inflow 1.26e-4 at its leading ray + tip floor share 1.0e-4).
- **D-5 THE CEILING ATTAINED**: the deficit falls at the observed order 0.913; its Richardson
  limit is **+2.2e-5** (first-order limit -6.4e-5), inside K_RICH x the order uncertainty
  3.45e-4. The M1 corollary (duality gap zero) measured on our own construction at the nominal
  ambient: no design of the class can exceed the member by more than that band.
- **R-1 PAIRED REJECTOR**: the member beats the 1.5-percent perturbed design -- in class in R
  (+0.0318 / +0.0573 / +0.1013) -- by +3252 / +3990 / +4203 N (2.8e-5 .. 3.6e-5 of J) on the
  three rungs, above K_RICH x its change between rungs (2950 N). Tight (ratio 1.10), declared.
- **R-2 CLASS REJECTOR**: the chord between the design's endpoints folds in R (-0.471 / -0.677).
- READINGS, the flatness of the valley (paired, K 81 / K 161): the chord (6.5 cm from the
  member, out of class) is +3.07e4 / +3.12e4 N (2.6e-4 of J) below the member; a uniform-turn
  wall 1.1 cm away only +247 / +247 N (2.1e-6). The value certifies the optimum's VALUE through
  the bound; it cannot locate its SHAPE within a centimetre -- the class and the finder do.

Unpaired, the value band of the tournament's instrument (K_RICH |J(K) - J(2K-1)|: 2.4e-3 of
J at K 81) cannot see any of these designs; paired on the same rungs they resolve.

## 3. The tournament's far start is in class (a READING, probe in RDE/handoff)
`RDE/handoff/f3_2026-09-24/ptrn_start_class_probe.py` + its log (scratch, not of record): the
three starts of [X-PTRN]'s S30 campaign at its (81,41) posing, graded by the whole-net fold
census, by the region-R margin (the S34 criterion) and by the tournament's own bucket class
(floor mu0_1 = m_ref/2 = 0.0435, m_ref = the member's worst bucket cell):

| start | cert | folded (whole net) | min margin in R | bucket min / KS - mu0 |
|---|---|---|---|---|
| A the member | 0.43 | 0 / 915 | +0.0893 | +0.0871 / +0.0435 |
| B 1.5 percent perturbation | 0.14 | 620 / 2068 | -0.7300 | -0.7300 / -0.7735 |
| C ramp to the planar streamline | 0.44 | 0 / 402 | +0.0620 | +0.0003 / -0.0433 |

C, the generic far start (0.84 m from the member at the tail), is IN CLASS by the region-R
criterion: it failed S30 only through the self-referential bucket floor at a cell outside R.
So the finder test the tournament could not run -- the direct machinery finding the member
from far away at the nominal ambient -- is posable from C WITHOUT restoration, with the class
constraint in region R (the S34-S35 practice). B folds in R and stays a restoration case.

## 4. Declared
- Exit duty (c) "at least ONE var-gamma or stratified plug instance": DECLARED CLOSED -- every
  our-world plug row marches the CH4/O2 frozen NASA tables (gamma(T) variable): [X-OWTW],
  [X-OWO3], [X-OWS3] (S28) and [X-OWNM] (today).
- Exit duty (a): its VALUE half is certified by the bound at the nominal ambient ([X-OWNM]:
  the member attains mdot V_id, and every design is below it within [C-GBCS]); its FINDER half
  (the optimiser re-obtaining the member from a generic far start at the nominal ambient) is the
  tournament's campaign from C with the class in R -- multi-hour, the SECOND and last decisive
  campaign D6 ISS-4 allows this instance (the first: S30's overnight leg), launched on the
  owner's word as the carrier states. Not launched here.
- Budget: decisive runs this session ~50 min (derives, the K ladder, the probes, the re-run of
  record); well inside the 3 h cap.
- SR-9: no agent orchestration.

## 5. HANDOFF
- Files of record: `validation/ourworld_nominal.py` + `ourworld_nominal_cases.json` (new), this
  log, the index row, registry [X-OWNM], M0 Part VI addendum S38, PROGRESS (R38 2/4, ORA/NEXT-F3,
  BLOCCATO 20 j) + archive, D6 F3 status. Figure `validation/_ourworld_nominal/figs/
  18_ceiling_nominal.png` (generator RDE/handoff/f3_2026-09-24/ownm_fig.py, not committed).
- NEXT (owner's word): the tournament's finder campaign from C at the nominal ambient with the
  class in region R; coin [X-PTRN]'s registry row with its re-run derive; then the two-wall
  stretch.

## 6. Conformity
**The owner's condition** ("committa se tutto è in regola e procedi con F3"): S37 was already
committed and pushed (nothing pending); F3 continued as session 2/4 with the exit duties the
record can close without the multi-hour campaign:

| exit leg | carrier | verdict |
|---|---|---|
| (a) certified plug optimum, VALUE half at the nominal ambient | [X-OWNM] | 7/7 PASS |
| (c) at least one var-gamma plug instance | our-world rows on the NASA tables | declared closed |
| (a) FINDER half from a generic far start | the tournament from start C | posable (C in class in R); campaign on the owner's word |

The owner's check page: `validation/_ourworld_nominal/figs/18_ceiling_nominal.png` (generator
RDE/handoff/f3_2026-09-24/ownm_fig.py, presentation only).

**Conformity** (CLAUDE.md R1-R7, SR-1..SR-12):
- Branch `rde-nozzle-program`, main tree; identity AlexFalco5; explicit pathspecs; GENO never
  added. Push on the owner's standing word, after the commits.
- R1: `[F3/A1][S38]`, F3 session 2/4 (measured: the counter instituted in S37 at 1/4). R3: this
  log; PROGRESS ORA-F3 / NEXT-F3 in place, R38 (counter 2/4, exits) and BLOCCATO 20 (j) new; the
  outgoing blocks and row verbatim in PROGRESS_ARCHIVE under the 2026-09-24 notte (S38) banner;
  D6 F3 status paragraph; HANDOFF (section 5, RDE/handoff/F3_HANDOFF_2026-09-24.md).
- R4: M0 Part VI LINE ADDENDUM S38, two items with classes.
- R5 / SR-2: registry row [X-OWNM] (kind carrier, ondemand env=jax, pass 2026-09-24, suite
  none, falsifier named). The tournament start-class numbers are a READING from a scratch probe
  kept in RDE/handoff (not a registry claim). [X-PTRN]'s missing row is declared, not bracketed
  in docs (the orphan lint), to be coined with its re-run derive. SR-1: the index row. SR-5: no
  A1_* flag. SR-9: none.
- SR-6: files of record committed: `validation/ourworld_nominal.py`,
  `validation/ourworld_nominal_cases.json` (new; numeric ratchet clean after moving the
  uniform-turn grid and bracket into the JSON; the derive of record re-run on that code:
  identical numbers); this log; the index; PROGRESS + archive; D6; M0; the registry. Not
  committed, by design: the figure and its generator, the probe and its log, the stage JSON and
  logs in `validation/_ourworld_nominal/`. The abandoned walk posing's artefacts were deleted.
- Lints on the tree of the first commit (measured 2026-09-24 ~21:50): numeric PASS (127 files,
  0 ratchet violations); advisory index PASS (130 rows, 0 violations); claims lint 2 violations
  = PROGRESS and D6 citing [X-OWNM], which lands in the second commit (the ordering rule). Full
  suite on the same tree: 15/23 = the seven environmental reds + (xv) for the ordering reason,
  86 s (a first measurement read 14/23: (vii) caught one literal of the carrier, moved into the
  JSON, the derive re-run with identical numbers); data/phase_diagram.*,
  data/q_mapping.* and figs/phase_diagram_op11.png restored with git checkout before the commit.
- Two commits, as the line's practice: (1) carrier + data + this log + index + PROGRESS/archive
  + D6; (2) registry + M0 + this log's measurement line.
