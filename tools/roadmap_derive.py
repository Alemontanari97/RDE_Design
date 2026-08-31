#!/usr/bin/env python3
"""roadmap_derive.py — the DERIVED roadmap (S-ROADMAP U1', 2026-08-31).

Carrier of record: validation/ADVISORY_Sroadmap_prompt_2026-08-31.md,
addendum F ("certainty by DERIVATION + LINT, never by reading").

This tool performs the machine JOIN  phase x atlas-objects x registries
and writes docs/ROADMAP_critical_path.md as a TABLE OF STEPS.  Nothing in
the output is authored: every row is a projection of the sources below,
every placement that is NOT a literal phase token in the source row is a
DECLARED OVERRIDE (section 3 of the output, each with its anchor), every
object that appears in no step carries an explicit OUT:<why> (section 4).

MACHINE SOURCES (all of record, all read here):
  D6      docs/rde_nozzle_development_plan.md      phase spine F0-F6 (+F1b)
          at the column-0 lines "F<n>  TITLE", the G-gate table (:282-290)
  MAP     docs/rde_nozzle_pipeline_decision_map.md (of record, refuter 0/0)
          consumed through its assert-gated extraction
  GRAPH   validation/spres_raws_2026-08-22/graph_derisk/pipeline_graph.json
          (79 nodes / 45 edges)
  LEDGER  docs/choice_ledger.yaml                  (62 rows C1..C62)
  FIND    docs/findings_registry.yaml              (OPEN rows + path: tag)
  CLAIMS  docs/claims_registry.yaml                THEORY objects still open
          as statements: class SCHEMA / CONJECTURE (kinds schema,
          conjecture, conditional, carrier-schema) — each must be consumed
          by a step (the phase whose work discharges or falsifies it) or
          carry OUT:<why>; THEOREM/THEOREM*/PRACTICE rows are CLOSED
          statements (indexed by lint xv) and are OUT by class, declared
  BLOC    docs/rde_nozzle_PROGRESS.md              BLOCCATO table (path: col)
  ATLAS   docs/atlas/*.md                          every phase mention F<n>

The critical path to the decisive TWIN (advisory sections B/E) is a
FILTERED VIEW (path: critical) of the step table — never a document
written by hand.  A hand edit of the output is rejected by the lint
tests/test_roadmap_coverage.py (group (xxiv)): the output carries a
content hash of its own body and the lint regenerates and compares.

Usage:
    python tools/roadmap_derive.py            # regenerate the doc
    python tools/roadmap_derive.py --check    # exit 1 if the doc is stale
"""
import hashlib
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

D6 = os.path.join(ROOT, 'docs', 'rde_nozzle_development_plan.md')
GRAPH = os.path.join(ROOT, 'validation', 'spres_raws_2026-08-22',
                     'graph_derisk', 'pipeline_graph.json')
LEDGER = os.path.join(ROOT, 'docs', 'choice_ledger.yaml')
FIND = os.path.join(ROOT, 'docs', 'findings_registry.yaml')
CLAIMS = os.path.join(ROOT, 'docs', 'claims_registry.yaml')
PROGRESS = os.path.join(ROOT, 'docs', 'rde_nozzle_PROGRESS.md')
ATLAS_DIR = os.path.join(ROOT, 'docs', 'atlas')
OUT_DOC = os.path.join(ROOT, 'docs', 'ROADMAP_critical_path.md')

PHASES = ('F0', 'F1', 'F1b', 'F2', 'F3', 'F4b', 'F5', 'F6')
GATES = ('G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6')
OPEN = ('CONFIRMED', 'DOWNGRADED')

# ---------------------------------------------------------------------------
# STEPS (the row set of the output table).  Each step = one D6 phase or one
# named sub-window of a phase whose existence is itself of record (anchor in
# the `why` field).  Order = program order of record.
# ---------------------------------------------------------------------------
STEPS = [
    # id, phase, title, path, why (anchor of the step's existence)
    ('F0', 'F0', 'ORDER + INSTRUMENTATION', 'OUT:closed',
     'D6:37; closed by succession (F1 CLOSED, D6:91)'),
    ('F1', 'F1', 'GOVERNOR + P-2 CAPTURE', 'OUT:closed', 'D6:55, :91'),
    ('F1b', 'F1b', 'DEF ADJUDICATION (bell/TOC twin = current-sector twin)',
     'OUT:closed', 'D6:101, :137; advisory E: NOT the decisive twin'),
    ('F2-B0', 'F2', 'F2 BLOCCO 0 — entry act (engine cluster, hygiene, '
     'GENO health, TWIN protocol pre-registration, topology+modelling '
     'session)', 'critical',
     'PROGRESS NEXT + D6:160-171 (C6 pre-entry, G0/T2 consumed) + '
     'BLOCCATO B16/B19'),
    ('F2.REPR', 'F2', 'REPRESENTATION LADDER adjudication at F2-entry (user-'
     'ratified session "topologia+modellistica", BLOCCATO B16/B19(b)): '
     'per-phase 4-field axial (current) / 2.5D five-field S-5F / '
     'azimuthal marching C51-route-B (native helix) / hybrids / 3D-per-'
     'phase; fitted vs captured C49; stack C58/C60; the 3-D COUNTERPART '
     'decided here at convergence with the census protocol, field-'
     'reading pass on Harroun Figg. 12-20', 'critical',
     'PROGRESS B16 + B19(b) (ratified F2-entry, scope extended); MAP stage '
     '2 (C49, S-5F, ROUTE-B, C51, R22-CFD, C59); D6 has no named step '
     '(finding plan:representation-ladder-3d-counterpart-no-named-d6-step)'),
    ('F2.ENGINE', 'F2', 'F2a/F2b GENERAL ENGINE: F2a = DATA CONTRACT as the '
     'input surface (interface datum = per-phase profiles M_in, theta_in, '
     's, h0 on Gamma_d; stage-A audits Crocco/completeness/H-I2 + T0-'
     'flatness monitor, G6 LOUD REJECT from here; contact/slip = smeared '
     'stratified default; U3\' choking adjudication; SWIRL: F-swirl-1 '
     'contract field + F-swirl-2 monitor + DUTY-8 breakdown screen + D.14/'
     'D.16 angular-momentum rows; case-A generator of Annex B = specs-only '
     'Cantera chain) + F2b = stratified three-family march (C+/C-/'
     'streamline s,h0), thermo tables, certificates, bands, driver, '
     'extended (q;s,h0) margin with rejector', 'critical',
     'D6:160-213 (F2a :172-206, F2b :206-213); D6 duty rows :407-412; '
     'Annex B :1140-1148; D6 item 17 :1063-1090'),
    ('F2.M-RED', 'F2', 'M-RED reduction-residual campaign + deriver chain '
     '(X-T3QS-5F -> C51-route-B -> M-RED rider; delta/L_H)', 'critical',
     'PROGRESS B19(c) "M-RED resta prima campagna F2"; MAP E28/E29'),
    ('F2.CFD-2', 'F2', 'CFD-2 paired demo (Li-Xu template) + CFD-1 decision '
     '(post-M-RED)', 'critical',
     'PROGRESS B19(a); MAP :77 R22-CFD USER-DECISION PENDING'),
    ('F3.RK1', 'F3', 'Spike-level plug-march de-risk (RK1 front-load, '
     'AUTHORIZED parallel to F2) + RaoPlug S1/S2 entry condition',
     'critical', 'D6:222-223, :214-218; D6 §6 items 3-4'),
    ('F3.PLUG', 'F3', 'Plug/aerospike sector in the engine: plume-boundary '
     'solve (H20), p_b closure (C61/N2), spike Table-1 oracle, plug/C- '
     'mirror margin, transition duty (iii)', 'critical',
     'D6:214-232; advisory E; findings row plan:h20-c61-registry-homing-'
     'f4b-vs-d6-f3-plug'),
    ('F3.TWIN', 'F3', 'THE DECISIVE TWIN on the truncated plug: per-phase '
     'design vs classical design on I4 (<Pc>,T0,gamma) at IDENTICAL '
     'constraints, kill-or-validate, stop ~1% Isp; 2-D truncated-plug '
     'shape falsifier BEFORE the first certified plug optimum ships',
     'critical',
     'atlas CH6:440/:490/:712; D6:219-222 (F3 EXIT); advisory B/E'),
    ('F3.TOURNAMENT', 'F3', 'FULL-ENVELOPE OPTIMIZER: every geometry class '
     'in the engine (bell/TOC, plug, shrouded plug, E-D/other A_gen '
     'sectors) + the FINITE SECTOR TOURNAMENT at the true constraint '
     'vector (premium_bound device, M4 deflated continuation, census-'
     'lemma + PAP-RIM at F2-exit) -> S*(c) as OUTPUT; no named D6 step '
     'of record (finding plan:full-envelope-tournament-no-named-d6-step)',
     'non-critical',
     'problem_book :337-363 (SCHEMA); M0 tournament device (Part IV); '
     'atlas CH8 §1.2/§1.7/§3.5; advisory E "full envelope = F3 exit + '
     'F4b"; D6 F3 EXIT :219-222 covers ONE sector only'),
    ('F4b', 'F4b', 'DECLARED-TOPOLOGY FITTED FRONTS = OBLIQUE SHOCKS of the '
     'RDE exhaust entering through the datum (front taxonomy (b): data-'
     'borne / boundary-entering per-phase oblique wave system, plug/shroud '
     'lip shocks) treated as classical FITTED fronts with declared '
     'topology: U3 bordered solve + G12 linearization + adjoint jump '
     'conditions; X1 capturing-control rejection; optional fitted-CONTACT '
     'extension; NO interior birth-fitting (excluded by the margin '
     'governor, taxonomy (c)); order-interchangeable with F3 given F2 '
     'exit', 'non-critical', 'D6:233-251 (F4b), :292-311 (front taxonomy), '
     ':228-232'),
    ('F5', 'F5', 'RDE MACHINE = THE ARRIVAL POINT: an RDE datum in input '
     '(Annex B cases B = wave-structure model / C = partial experiment / '
     'D-G = mission, throttle, uncertainty, chamber coupling) -> CFD-to-'
     'CONTRACT PIPELINE for CAPTURED data (captured-shock detection, Gelb-'
     'Tadmor concentration lineage; RH-consistent sharp-state '
     'reconstruction, Paciorri-Bonfiglioli lineage; exact-RH projection '
     'with derived residual band + LOUD REJECT; synthetic smear-extract-'
     'compare KAT as oracle; U3 extraction-surface rule) -> F5a quasi-'
     'steady sweep T3-QS + certified cycle-averaged design Verdict + mu-'
     'instruments + G2 VALUE GATE; F5b G3 unsteadiness trigger as a NUMBER '
     '+ corrector; G4 decoupling; re-budget MANDATORY at entry',
     'non-critical', 'D6:252-274 (pipeline :256-268); Annex B :1133-1157; '
     'gate table :286-288; atlas CH10 §2(b)'),
    ('F6', 'F6', '3-D / HARDWARE BRIDGE (horizon, not budgeted): B-lite '
     'helical space-march demonstrator (G12-L1-3D brick, [S-BLITE]), the '
     'A5 wave-frame anchor (2-D unrolled-annulus reactive Euler, freezing, '
     'Newton-Krylov, bordered adjoint; G4 decoupling gate), 3-D MoC tool '
     'line (Ransom/Hoffman/Thompson to locate; NASA Rice-MoC3D/NPAC/SUPIN '
     'adjudication NOT landed), experimental anchor RK-E, HPC RK-F',
     'non-critical', 'D6:275-278, :646-666 (A5), §6 items 11-14; claims '
     'S-BLITE; memory nasa-nozzle-tools-exploration (landing PENDING)'),
    ('PAPER', 'PAPER', 'Paper / claims / literature stream (P-1 theory half '
     'from F2, freeze F2 exit; methods freeze + F3 showcase; G5 human '
     'pass before ANY submission)', 'paper', 'D6 §3 :684-734, :345-349'),
]
STEP_IDS = [s[0] for s in STEPS]
STEP_BY_ID = {s[0]: s for s in STEPS}

# Sub-step keyword rules inside F2 / F3 (applied AFTER the phase is fixed
# by a literal token in the source row; declared here, printed in the doc).
F2_SUBRULES = [
    ('F2.M-RED', r'M-RED|X-T3QS-5F|route-B|rung-3a|forchetta|OPTSHIFT|'
                 r'argmax-shift|reduction-residual'),
    ('F2.CFD-2', r'\bCFD\b|CFD-1|CFD-2|R22-CFD'),
    ('F2-B0', r'F2[- ]entry|F2 opening|F2-B0|first oracle block|'
              r'GENO repo|S-GENOAUDIT|G0/T2|session boundary|'
              r'F2-entry|BLOCCATO 14|touchpoint'),
]
F3_SUBRULES = [
    ('F3.TOURNAMENT', r'tournament|torneo|census-lemma|PAP-RIM|'
                      r'full-envelope|every geometry class|global '
                      r'exploration'),
    ('F3.TWIN', r'D-44|adequacy claim|PB-2|truncated-plug|\(value, ?delta\)'),
    ('F3.RK1', r'RaoPlug|RK1|plug-march'),
]

# Phase-token regex (declared exclusions: commit tags "[F1/...]",
# hyphen-prefixed ids "H-F1", "F-1", slash-prefixed "l1-F2/" forms).
PHASE_RX = re.compile(r'(?<![\w\-\[])F([0-6])(b|a)?(?![\w])')


def phase_of_token(m):
    n, suf = m.group(1), m.group(2)
    if n == '1' and suf == 'b':
        return 'F1b'
    if n == '4':
        return 'F4b'          # F4a dissolved into F1b (D6:233) — declared
    return 'F' + n


def phases_in(text):
    return [phase_of_token(m) for m in PHASE_RX.finditer(text or '')]


# ---------------------------------------------------------------------------
# DECLARED OVERRIDES — every placement that is not a literal phase token in
# the source row.  id -> (step, reason).  Printed in section 3 of the doc.
# A missing override for an unresolvable object is an ERROR (no silent
# default), except for the OUT rules of `out_reason()`.
# ---------------------------------------------------------------------------
NODE_OVERRIDES = {
    'PIN-WAVE': ('OUT:standing-user-pin', 'memory periodic-wave-data-scope; '
                 'corrector re-scope owned by F5b (row text)'),
    'CONTRACT-F1..F10-block': ('F2.ENGINE', 'F2a owns the contract '
                               '(D6:172-176, G6 operative from F2a)'),
    'S-5F': ('F2.REPR', 'PROGRESS B15(d)/B-S5F + B19(b): build decision in '
             'the F2-entry representation session'),
    'C49': ('F2.REPR', 'fitted-front vs captured = representation axis; '
            'falls to F2 entry (MAP :73); B19(b) session'),
    'C59': ('F2.REPR', 'F2-entry census window (MAP :78); temporal-form axis '
            'of the same representation decision'),
    'ROUTE-B': ('F2.REPR', 'native helical treatment = the azimuthal-'
                'marching branch of the representation ladder (B19(b)); '
                'also deriver in the E29 chain consumed by F2.M-RED'),
    'C51': ('F2.REPR', 'rung-3a wave-frame solver implicit BVP vs azimuthal '
            'marching = representation choice adjudicated in the B19(b) '
            'session (PROGRESS B15(e) priority confirmed); MAP E29'),
    'R22-CFD': ('F2.CFD-2', 'PROGRESS B19(a): CFD-2 in F2 queue, CFD-1 '
                'post-M-RED'),
    'C55': ('OUT:event-gated', 'ledger C55 sequencing clause: adjudication '
            'owed at first multi-point P_amb instantiation (Annex B case D)'),
    'C54': ('OUT:touch-gated', 'ledger C54: flips DECIDED at the next M0 '
            'D2.4 touch (one-line annotation)'),
    'T-DISC': ('OUT:landed', 'MAP stage 7: LANDED, open duty "—"'),
    'D-44': ('F3.TWIN', 'the TWIN is the first public adequacy claim; '
             'MAP :180 + findings :1468'),
    'P34': ('PAPER', 'MAP :181 P-1/G5-G6 claims window'),
    'H20': ('F3.PLUG', 'D6:214-227 precedence over the registry F4b homing '
            '(findings plan:h20-c61-registry-homing-f4b-vs-d6-f3-plug)'),
    'C61': ('F3.PLUG', 'same override as H20 (advisory E)'),
    'DUTY-10': ('F5', 'MAP [MAP-AM-1]: DUTY-10(a) F5b, (b) F6 — placed at '
                'the earlier slot'),
    'OBJ-DOM': ('F2-B0', 'trigger "first F2 verdict consuming dJ/dthB" '
                '(findings :211-212); consumed again at F3.TWIN'),
    'DELTA-CARRIER': ('F2.ENGINE', 'ship-gate ARMED for every (value,delta) '
                      'row (MAP :173); consumed again at F3.TWIN'),
    'OPTSHIFT': ('F2.M-RED', 'MAP :174 owner "F2, in order ... M-RED rider"'),
    'R22F-FORCHETTA': ('F2.M-RED', 'MAP :170 "M-RED campaign + RES-CAP '
                       'residues"'),
    'CLG': ('F2.ENGINE', 'MAP :115 F2-CLG-SCALE'),
    'SDP-CAND-8': ('F2-B0', 'MAP :116 F2-entry engine census'),
    'M-RED': ('F2.M-RED', 'MAP :129 F2-QUEUED'),
    'C28': ('F2.ENGINE', 'duties [P-CERTKS]+[P-BSTAT] in the GAP-1/GAP-2 '
            'window = F2 (findings driver-nonsmooth:no-B-stationarity-'
            'certificate owner "F2 (with the GAP-1 window)")'),
    'C30': ('F2.ENGINE', 'C30 lands FIRST and instruments C29 (owner '
            'F2-DUTY-C29-MASKGRAIN) — same F2 window'),
}
LEDGER_OVERRIDES = {
    'C51': NODE_OVERRIDES['C51'], 'C55': NODE_OVERRIDES['C55'],
    'C54': NODE_OVERRIDES['C54'], 'C61': NODE_OVERRIDES['C61'],
    'C30': NODE_OVERRIDES['C30'], 'C49': NODE_OVERRIDES['C49'],
    'C59': NODE_OVERRIDES['C59'],
}
FINDING_OVERRIDES = {
    # critical rows whose owner/trigger has no phase token or whose literal
    # token is not the consuming step of record
    'pipeline:Q3-certifiability-composition':
        ('F3.TWIN', 'trigger "before the first genuinely averaged shape '
                    'problem (PB-2 class)" = the TWIN problem'),
    'litreview:residue-r8-r23-base-pressure-pb2-blocking':
        ('F3.PLUG', 'p_b closure = C61/N2 (advisory E; D6 F3)'),
    'litreview:residue-r6-r29-corner-class-and-terminal-face-cone':
        ('F3.PLUG', 'R29 = PB-2 cone-form derivation touch (plug sector)'),
    'plume:free-boundary-solve-mechanics-missing':
        ('F3.PLUG', 'H20 override (see NODE_OVERRIDES)'),
    'plan:h20-c61-registry-homing-f4b-vs-d6-f3-plug':
        ('F3.PLUG', 'the override citation row itself'),
    'litreview:residue-r22-r27-disentanglement-experiment-and-adjoint-weight-transfer':
        ('F3.TWIN', 'D-44 gate on the first public adequacy claim = TWIN; '
                    'R22 experiment = F2.CFD-2 (second consumer)'),
    'theory:r22f-optimum-shift-gradient-route':
        ('F2.M-RED', 'owner "F2, in order: X-T3QS-5F / C51-route-B / '
                     'M-RED rider"'),
    'oracles:geno-tocnoz-wall-thrust-double-count':
        ('F2-B0', 'impact audit fires FIRST at F2 entry (I4 baseline = '
                  'Rao/GENO thrust reference)'),
    'moc-audit:ledger-c1-thermo-audit-outcome-bundle':
        ('F2-B0', 'GENO health step (plugnoz CTest reproducibility, item g)'),
    'variational-driver:objective-omits-throat-panel':
        ('F2-B0', 'OBJ-DOM override'),
    'oracles:a1-gp01-quasi1d-not-built':
        ('F2-B0', 'owner "F2 (D-20, priority)", trigger "F2 entry (first '
                  'oracle block)"'),
    'oracles:o34-gradient-leg-unconsumed':
        ('F2-B0', 'trigger "F2 entry (oracle re-baseline)"'),
    'oracles:root-identity-replay-common-mode':
        ('F2.ENGINE', 'duty F2-C20-CERTQUAL-CAMPAIGN Tier-0'),
    'engine-core:F5-underived-factors':
        ('F2.ENGINE', 'NTF derivation duty F2-live (C18); the "F5" in the '
                      'id is the audit finding number, not a phase'),
    'plan:representation-ladder-3d-counterpart-no-named-d6-step':
        ('F2.REPR', 'the step minted by this finding'),
    'plan:nasa-3d-moc-tools-adjudication-not-landed':
        ('F2.REPR', 'landing decision belongs to the representation session '
                    '(duty a: G12-L1-3D cross-check; duty b: Kliegel-Levine band)'),
    'theory:s5f-path-a-freevortex-stratified-gap':
        ('F2.REPR', 'S-5F decision dossier = the representation session'),
    'method:sroadmap-single-author-placements-unrefuted':
        ('F2-B0', 'owner: F2-B0 FIRST act (refuter pass over tags + '
                  'overrides)'),
    'plan:full-envelope-tournament-no-named-d6-step':
        ('F3.TOURNAMENT', 'the step minted by this finding (anchors in the '
                          'step row)'),
    'twin-falsifier:c3-mesh-refinement-unadjudicated':
        ('F2.ENGINE', 'owner "F2 (the C7 refine/enriched-class leg)"; the '
                      '"branch F1" in the trigger is a twin BRANCH label '
                      '(F1-F7), not the plan phase'),
    'engine-core:F3-table-clamp-silent':
        ('F2.ENGINE', 'id "F3-" = audit finding number, not a phase; owner '
                      'F2 engine window'),
}

BLOC_OVERRIDES = {
    'B-CFD1': ('F2.CFD-2', 'PROGRESS B19(a): CFD-1 decided POST-M-RED, '
               'inside the F2 CFD window'),
    'B-GENO': ('F2-B0', 'PROGRESS NEXT item (2): GENO health at F2 BLOCCO 0'),
    'B-G5': ('PAPER', 'G5 blocks SUBMISSIONS only (D6:289)'),
    'B12': ('PAPER', 'WANTED procurement rows consumed by lit/claim windows'),
    'B-RAOPLUG': ('F3.RK1', 'D6:214-218 F3 ENTRY condition; de-risk RK1 '
                  'authorized parallel to F2 (D6:222-223)'),
}

# THEORY objects (claims registry, class SCHEMA/CONJECTURE): placement by
# the phase whose work discharges or falsifies the statement; anchors =
# the claim's own falsifier/scope + the D6/registry row that owns the work.
CLAIM_OVERRIDES = {
    'C-IGMIX': ('OUT:priced-by-theorem', 'finite-rate bracket priced by '
                '[T-EQBR] (D6 scope pin P1: finite-rate outside by '
                'declaration, T-EQBR = the necessity guard)'),
    'S-S1U': ('F2-B0', 'findings :1455 trigger (equivariance+uniqueness S1) '
              'fires at any external act; F2 theory window'),
    'S-N6SO': ('F2.REPR', 'non-free-vortex swirl closure = the S-5F path-A '
               'fork (findings theory:s5f-path-a-freevortex-stratified-gap)'),
    'J-OP11': ('F3.TOURNAMENT', 'falsifier = "sector tournament with '
               'certified delta-bands contradicting the selected topology"'),
    'C-EQV2': ('OUT:falsifier-executed', 'the pre-registered twin F1-F7 RAN '
               'in F1b (S24): EQ-v2 = CONJECTURE + H-CLASS of record; '
               're-opens only at a margin-active outcome (findings twin-'
               'falsifier:c6-outcome-i-never-reached, F2)'),
    'S-XCONV': ('F2.ENGINE', 'certified-box convexity schema = C28/C20 '
                'certification window ([P-CERTKS]); carrier X-IVXC in suite'),
    'S-D25U-U1': ('F2.ENGINE', 'C-D25U completeness (findings foundations-'
                  'U:U34-C0-bootstrap-circularity, pre-F2/F2 entry)'),
    'S-D25U-U34': ('F4b', 'fitted-front bordered solve U3/U4 = F4b machinery '
                   '(D6:233-238)'),
    'S-ACFR': ('F4b', 'a-contraction front route = fitted-front certificate '
               'class (F4b; carrier X-ACFR in suite)'),
    'C-MAJDA-3DT': ('F6', '3-D Lopatinskii (eta_y, eta_z) = the B-lite/3-D '
                    'helical march conditional (G12-L1-3D brick, F6)'),
    'C-XINJ': ('F4b', 'second supersonic root on a certified front = fitted-'
               'front admissibility (DUTY-9 RR/MR row, F4b)'),
    'C-WSF': ('F4b', 'a-contraction weight/shift inequality on a certified '
              'front (F4b certificate class)'),
    'S-T0P-G12': ('F2-B0', 'stop-proof gap route; findings theory:s-t0p-'
                  'proof-writeup-pending (F2 theory window)'),
    'X-T0P': ('F2-B0', 'the owed X-T0P rejector battery (same finding)'),
    'S-SDI': ('F2-B0', 'S-T0P family mint (same theory window)'),
    'C-XBVP-aprime': ('F4b', 'Cauchy-BVP transfer conditional across fitted '
                      'fronts (revision-10 list, stop_proof §13); consumed '
                      'by the F4b certificate class'),
    'C-R22F-DISC': ('F2.M-RED', 'per-dataset H-AM0 check = M-RED/forchetta '
                    'campaign (MAP E28)'),
    'C-RED-SBV': ('F2.M-RED', 'SBV composite hypothesis of [T-RED] = M-RED '
                  'band B-1/B-3 (MAP E28)'),
    'C-DCRX-CERT': ('F2.ENGINE', 'delta-carrier certificate-on-entry '
                    '[DC-F2-1..5] (MAP :173)'),
    'T-DISC-4': ('F2.M-RED', 'fiber-axis exoneration schema; class-wide '
                 'reading (U)-gated on M-RED (M0:1344)'),
    'T-RED-2G': ('F2.M-RED', 'argmax-shift schema gated on delta/L_H '
                 'derivers (OPTSHIFT row, MAP :174)'),
    'C-D25U': ('F2.ENGINE', 'THE shared analytic conditional (L4 ledger); '
               'completeness/bootstrap duty findings foundations-U:U34-C0-'
               'bootstrap-circularity (pre-F2) + L4 statement rows'),
    'C-MAJDA': ('F4b', 'THE shared front conditional across fitted shocks = '
                'F4b certificate class (D6:233-251)'),
    'C-HT4': ('F3.PLUG', 'declared MODEL CLOSURE: sonic-capped ideal '
              'adaptation, PB-2 truncation/base-pressure = the plug sector '
              '(C61/N2 closure)'),
    'C-O33': ('F2.ENGINE', 'numeric residual of the O3.3 corner row, '
              'quantified; re-measured in the richer adaptive class = C7 '
              'refine leg (findings twin-falsifier:c3-mesh-refinement-'
              'unadjudicated, F2)'),
    'S-5F': ('F2.REPR', 'five-field build decision = the representation '
             'session (PROGRESS B-S5F, B19(b))'),
    'S-BLITE': ('F6', 'B-lite helical space-march demonstrator (D6:275-278, '
                'item 11)'),
    'C-P4RZ': ('F5', 'analytic residual of S-P4F (O(St) license, cycle '
               'monodromy) = F5b corrector window (D6:271-273)'),
    'C-XBVP': ('F4b', 'Cauchy->BVP transfer residuals across fitted fronts '
               '(findings theory-core:F4-CXBVP-ledger-dangling-pointer for '
               'the ledger mint; certificate class F4b)'),
    'S-GBE': ('F5', 'ergodic transfer of the G-B ceiling = F5a bound-ladder '
              'consumer (findings registry-legacy:GBE-CONCAVITY-NEAR-FLOOR, '
              'pre-F5)'),
    'T-DISC-3': ('F2.M-RED', '2-epsilon optimization consequence of [T-DISC], '
                 'class-wide reading (U)-gated on M-RED (M0:1344)'),
}

# OUT rules for phase-less objects (declared, printed).
OUT_STATUS_DECIDED = ('DECIDED', 'LANDED')


def out_reason(kind, obj):
    """Return an OUT:<why> for an object that names no phase, or None."""
    if kind == 'node':
        st = obj.get('status', '')
        od = (obj.get('open_duty') or '').strip()
        if od in ('', '—', '-') and any(st.startswith(s)
                                        for s in OUT_STATUS_DECIDED):
            return 'OUT:decided-no-open-duty'
    if kind == 'ledger':
        if obj.get('status') == 'DECIDED' and not obj.get('owner', '').strip():
            return 'OUT:decided-no-owner'
    if kind == 'finding':
        p = obj.get('path')
        if p == 'paper':
            return None            # paper rows go to the PAPER step
        if p == 'non-critical':
            return 'OUT:non-critical-touch-gated'
    if kind == 'bloc':
        if obj.get('path', '').startswith('OUT:'):
            return obj['path']
    if kind == 'claim':
        if obj.get('class') not in ('SCHEMA', 'CONJECTURE'):
            return 'OUT:closed-statement-class-%s' % obj.get('class')
    return None


# ---------------------------------------------------------------------------
# Parsers (strict subsets; every parser raises on an unexpected shape)
# ---------------------------------------------------------------------------
def read(path):
    return io.open(path, encoding='utf-8-sig').read()


def parse_d6():
    lines = read(D6).split('\n')
    phases = {}
    order = []
    cur = None
    for i, ln in enumerate(lines, 1):
        m = re.match(r'^(F[0-6]b?)\s+(.+)$', ln)   # F1b/F4b: 1 space
        if m and m.group(1) in PHASES:
            cur = m.group(1)
            phases[cur] = {'line': i, 'title': m.group(2).strip(),
                           'text': [ln]}
            order.append(cur)
            continue
        if cur and ln.startswith('### G-gate'):
            cur = None
        if cur:
            phases[cur]['text'].append(ln)
    if order != list(PHASES):
        raise SystemExit('D6 phase spine parse mismatch: %r' % order)
    for pid, ph in phases.items():
        body = ' '.join(t.strip() for t in ph['text'])
        ph['body'] = body
        ph['closed'] = bool(re.search(r'\b(EXECUTED AND CLOSED|CLOSED \d{4})',
                                      body))
        for key, rx in (('entry', r'ENTRY[^:]*:\s*(.*?)(?=\bEXIT\b|$)'),
                        ('exit', r'\bEXIT\b[^:]*:\s*(.*?)(?=\bFALLBACK\b|'
                                 r'\bBUDGET\b|\bSTATUS OF RECORD\b|$)'),
                        ('fallback', r'FALLBACK:\s*(.*?)(?=\bSTATUS OF '
                                     r'RECORD\b|\bBUDGET\b|$)')):
            m = re.search(rx, body)
            ph[key] = (m.group(1).strip() if m else '')
        # phases whose D6 block carries no ENTRY/EXIT label (F2): quote the
        # pre-entry / at-exit sentences instead (declared fallback)
        if not ph['entry']:
            m = re.search(r'([^.;]*pre-entry[^.;]*)', body)
            ph['entry'] = m.group(1).strip() if m else ''
        if not ph['exit']:
            m = re.search(r'([^.;]*at exit[^.;]*)', body)
            ph['exit'] = m.group(1).strip() if m else ''
    # gates table
    gates = {}
    for i, ln in enumerate(lines, 1):
        m = re.match(r'^\| (G[0-6])\s+\| (.*?) \| (.*?) \|$', ln)
        if m:
            gates[m.group(1)] = {'line': i, 'content': m.group(2),
                                 'bites': m.group(3)}
    if sorted(gates) != list(GATES):
        raise SystemExit('D6 gate table parse mismatch: %r' % sorted(gates))
    return phases, gates


def parse_graph():
    g = json.load(io.open(GRAPH, encoding='utf-8'))
    return g['nodes'], g


def parse_block_registry(text):
    entries, cur, curlist = [], None, None
    for n, ln in enumerate(text.splitlines(), 1):
        if re.match(r'^\s*(#|$)', ln):
            continue
        m = re.match(r'^- id:\s*(\S+)\s*$', ln)
        if m:
            cur = {'id': m.group(1)}
            curlist = None
            entries.append(cur)
            continue
        if re.match(r'^[\w-]+:\s*$', ln):
            cur, curlist = None, None
            continue
        m = re.match(r'^    - (.*)$', ln)
        if m:
            if curlist is None:
                raise ValueError('line %d list item outside block' % n)
            curlist.append(m.group(1).strip().strip('"'))
            continue
        m = re.match(r'^  (\w+):(?:\s(.*))?$', ln)
        if not m or cur is None:
            raise ValueError('line %d not in block subset: %r' % (n, ln))
        k, v = m.group(1), (m.group(2) or '').strip()
        if v == '':
            curlist = cur[k] = []
        elif v.startswith('['):
            cur[k] = [x.strip().strip('"') for x in v[1:-1].split(',')
                      if x.strip()]
            curlist = None
        else:
            cur[k] = v[1:-1] if re.match(r'^".*"$', v) else v
            curlist = None
    return entries


def parse_claims():
    entries, cur = [], None
    for n, ln in enumerate(read(CLAIMS).splitlines(), 1):
        if re.match(r'^\s*(#|$)', ln) or ln.strip() == 'entries:':
            continue
        m = re.match(r'^- id:\s*(\S+)\s*$', ln)
        if m:
            cur = {'id': m.group(1)}
            entries.append(cur)
            continue
        m = re.match(r'^  (\w+): (.*)$', ln)
        if not m or cur is None:
            raise SystemExit('claims line %d not in subset: %r' % (n, ln))
        k, v = m.group(1), m.group(2).strip()
        if v.startswith('['):
            cur[k] = [x.strip().strip('"') for x in v[1:-1].split(',')
                      if x.strip()]
        else:
            cur[k] = v[1:-1] if re.match(r'^".*"$', v) else v
    return entries


def parse_bloccato():
    lines = read(PROGRESS).split('\n')
    rows = []
    inside = False
    for ln in lines:
        if ln.startswith('## BLOCCATO'):
            inside = True
            continue
        if inside and ln.startswith('## '):
            break
        if inside and ln.startswith('| ') and not ln.startswith('| id ') \
                and not ln.startswith('|---'):
            cells = [c.strip() for c in ln.strip().strip('|').split('|')]
            if len(cells) != 6:
                raise SystemExit('BLOCCATO row with %d cells: %r'
                                 % (len(cells), ln[:80]))
            rows.append(dict(zip(('id', 'item', 'stato', 'path',
                                  'owner', 'carrier'), cells)))
    if not rows:
        raise SystemExit('BLOCCATO table not found in PROGRESS')
    return rows


def parse_atlas():
    mentions = []
    for fn in sorted(os.listdir(ATLAS_DIR)):
        if not fn.endswith('.md'):
            continue
        for i, ln in enumerate(read(os.path.join(ATLAS_DIR, fn))
                               .split('\n'), 1):
            for m in PHASE_RX.finditer(ln):
                mentions.append({'chapter': fn, 'line': i,
                                 'phase': phase_of_token(m),
                                 'snippet': ln.strip()[:90]})
    return mentions


# ---------------------------------------------------------------------------
# Placement
# ---------------------------------------------------------------------------
def substep(phase, text):
    if phase == 'F2':
        for sid, rx in F2_SUBRULES:
            if re.search(rx, text or '', re.I):
                return sid
        return 'F2.ENGINE'
    if phase == 'F3':
        for sid, rx in F3_SUBRULES:
            if re.search(rx, text or '', re.I):
                return sid
        return 'F3.PLUG'
    return phase


def place(kind, oid, obj, text, overrides):
    """-> (steps:list[str], out:str|None, override_reason:str|None)."""
    if oid in overrides:
        step, why = overrides[oid]
        if step.startswith('OUT:'):
            return [], step, why
        return [step], None, why
    if kind == 'finding' and obj.get('path') == 'paper':
        return ['PAPER'], None, None
    phs = []
    for p in phases_in(text):
        if p not in phs:
            phs.append(p)
    if kind == 'bloc' and obj.get('path', '').startswith('OUT:'):
        return [], obj['path'], None
    if phs:
        steps = []
        for p in phs:
            s = substep(p, text)
            if s not in steps:
                steps.append(s)
        return steps, None, None
    o = out_reason(kind, obj)
    if o:
        return [], o, None
    raise Unresolved('UNRESOLVED %s %s: no phase token, no override, no '
                     'OUT rule — text: %r' % (kind, oid, (text or '')[:140]))


class Unresolved(Exception):
    pass


_UNRES = []


def _place(kind, oid, obj, text, overrides):
    try:
        return place(kind, oid, obj, text, overrides)
    except Unresolved as e:
        _UNRES.append(str(e))
        return [], 'OUT:UNRESOLVED', None


def derive():
    phases, gates = parse_d6()
    nodes, graph = parse_graph()
    ledger = parse_block_registry(read(LEDGER))
    findings = [e for e in parse_block_registry(read(FIND))
                if e.get('status') in OPEN]
    bloc = parse_bloccato()
    atlas = parse_atlas()
    claims = parse_claims()
    claims_open = [e for e in claims
                   if e.get('class') in ('SCHEMA', 'CONJECTURE')]

    cover = {s: {'gates': [], 'nodes': [], 'ledger': [], 'findings': [],
                 'bloc': [], 'atlas': [], 'claims': []} for s in STEP_IDS}
    outs = []          # (kind, id, why)
    overrides = []     # (kind, id, step, why)

    # gates -> phases -> every step of that phase
    for gid, g in gates.items():
        phs = phases_in(g['bites'])
        if gid == 'G5':
            phs = ['F0'] + phs + ['PAPER']   # blocks SUBMISSIONS (:289)
        phs = [p for p in phs if p in PHASES or p == 'PAPER']
        for p in dict.fromkeys(phs):
            for s in STEP_IDS:
                if STEP_BY_ID[s][1] == p:
                    cover[s]['gates'].append(gid)
    # G1 "every science phase — F2/F3/F5" already captured by tokens.

    for n in nodes:
        text = ' '.join(str(n.get(k) or '') for k in ('open_duty',
                                                        'conditions',
                                                        'status'))
        steps, out, why = _place('node', n['id'], n, text, NODE_OVERRIDES)
        if out:
            outs.append(('node', n['id'], out))
        for s in steps:
            cover[s]['nodes'].append(n['id'])
        if why:
            overrides.append(('node', n['id'], steps[0] if steps else out,
                              why))
    for e in ledger:
        text = e.get('owner', '')
        steps, out, why = _place('ledger', e['id'], e, text, LEDGER_OVERRIDES)
        if out:
            outs.append(('ledger', e['id'], out))
        for s in steps:
            cover[s]['ledger'].append(e['id'])
        if why:
            overrides.append(('ledger', e['id'],
                              steps[0] if steps else out, why))
    for e in findings:
        if 'path' not in e:
            raise SystemExit('OPEN finding without path: %s' % e['id'])
        text = e.get('owner', '') + ' ' + e.get('trigger', '')
        steps, out, why = _place('finding', e['id'], e, text,
                                FINDING_OVERRIDES)
        if out:
            if e['path'] == 'critical':
                _UNRES.append('critical finding OUT: %s' % e['id'])
            outs.append(('finding', e['id'], out))
        for s in steps:
            cover[s]['findings'].append((e['id'], e['path']))
        if why:
            overrides.append(('finding', e['id'],
                              steps[0] if steps else out, why))
    for b in bloc:
        text = b['item'] + ' ' + b['owner']
        steps, out, why = _place('bloc', b['id'], b, text, BLOC_OVERRIDES)
        if out:
            if b['path'] == 'critical':
                _UNRES.append('critical BLOCCATO OUT: %s' % b['id'])
            outs.append(('bloc', b['id'], out))
        for s in steps:
            cover[s]['bloc'].append((b['id'], b['path']))
        if why:
            overrides.append(('bloc', b['id'], steps[0] if steps else out,
                              why))
    for e in claims:
        if e.get('class') not in ('SCHEMA', 'CONJECTURE'):
            continue          # closed statement classes: OUT by class rule
        text = ' '.join(str(e.get(k) or '') for k in ('scope', 'falsifier',
                                                        'statement'))
        steps, out, why = _place('claim', e['id'], e, text, CLAIM_OVERRIDES)
        if out:
            outs.append(('claim', e['id'], out))
        for s in steps:
            cover[s]['claims'].append((e['id'], e.get('class')))
        if why:
            overrides.append(('claim', e['id'], steps[0] if steps else out,
                              why))
    for m in atlas:
        # an atlas mention lands in EVERY step of its phase (the phase is
        # the join key of record — the atlas is indexed by object, D6 by
        # phase; the mention is listed once per step for navigation)
        placed = False
        for s in STEP_IDS:
            if STEP_BY_ID[s][1] == m['phase']:
                cover[s]['atlas'].append(m)
                placed = True
        if not placed:
            raise SystemExit('atlas mention with no step: %r' % m)

    if _UNRES:
        raise SystemExit(chr(10).join(_UNRES) + chr(10) + '%d UNRESOLVED objects — add '
                         'a declared override or an OUT rule' % len(_UNRES))
    closed_steps = [s for s in STEP_IDS if STEP_BY_ID[s][3] == 'OUT:closed']
    stale = []
    for s in closed_steps:
        for oid, tag in cover[s]['findings']:
            stale.append((s, oid, tag))
        for oid in cover[s]['ledger']:
            stale.append((s, oid, 'ledger'))
        for oid in cover[s]['nodes']:
            stale.append((s, oid, 'node'))
    return dict(phases=phases, gates=gates, nodes=nodes, graph=graph,
                ledger=ledger, findings=findings, bloc=bloc, atlas=atlas,
                cover=cover, outs=outs, overrides=overrides, stale=stale,
                claims=claims, claims_open=claims_open)


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def clip(s, n):
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


def render(d):
    ph, cover = d['phases'], d['cover']
    L = []
    L.append('# ROADMAP — critical path to the decisive TWIN (DERIVED, never '
             'authored)')
    L.append('')
    L.append('Generated by `tools/roadmap_derive.py` (S-ROADMAP U1\', '
             'advisory addendum F). **DO NOT EDIT BY HAND** — lint group '
             '(xxiv) `tests/test_roadmap_coverage.py` regenerates this '
             'file in memory and rejects any drift (content hash in the '
             'footer). Sources: D6 phase spine + gate table, pipeline '
             'decision map (via `graph_derisk/pipeline_graph.json`), '
             'choice ledger, findings registry (OPEN rows, `path:` tag), '
             'PROGRESS BLOCCATO table, every phase mention in '
             '`docs/atlas/*.md`.')
    L.append('')
    L.append('## 0. The decisive number (quoted from the record, not '
             'restated)')
    L.append('')
    L.append('Head-to-head TWIN: per-phase design vs classical design on I4 '
             '(⟨Pc⟩, T0, γ) at IDENTICAL constraints, twin-first, '
             'kill-or-validate (atlas CH6 :440 / :490 / :712; comparator = '
             'ZERO computed instances). The break theorem holds on the '
             'TRUNCATED PLUG, whose sector is F3 GEOMETRY CLASSES (D6:214-'
             '227) — the bell/TOC twin of F1b (+0.51% ± 30%, cert-limited) '
             'is the current-sector twin, not the decisive one (advisory E). '
             'Data class of the TWIN = case A of D6 Annex B (:1142: active '
             'channels N1, N2 = truncated plug, N4; NOT N3) unless the F2-B0 '
             'protocol pre-registration says otherwise — that is the '
             'falsifier of the `non-critical` tag on the contract rows.')
    L.append('')
    L.append('## 1. Steps (one row = one D6 phase or one sub-window of '
             'record; columns are projections of the sources)')
    L.append('')
    L.append('| step | D6 phase (anchor) | status | gates | ENTRY (D6) | '
             'EXIT / falsifier (D6) | FALLBACK (D6) | owner | nodes | '
             'ledger | findings crit/nc/paper | BLOCCATO | open claims '
             '(SCHEMA/CONJ) | atlas | path |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    for sid, pid, title, path, why in STEPS:
        c = cover[sid]
        p = ph.get(pid)
        if p:
            status = ('CLOSED' if p['closed'] else
                      'CLOSED-by-succession' if pid == 'F0' else
                      'NEXT (0/6)' if pid == 'F2' else 'NOT-OPENED')
            anchor = 'D6:%d' % p['line']
            entry, exit_, fb = (clip(p['entry'], 140), clip(p['exit'], 140),
                                clip(p['fallback'], 90))
        else:
            status, anchor = 'parallel track', 'D6 §3'
            entry, exit_, fb = ('from F2 (theory half)',
                                'G5 human pass before any submission',
                                'P-2 on S19 two-knob numbers (D6:90)')
        owner = ('program (PROGRESS counter "%s session m/n")' % pid
                 if pid in ('F2', 'F3', 'F4b') else
                 'user (G5) + program' if pid == 'PAPER' else 'program')
        nf = c['findings']
        crit = sum(1 for _, t in nf if t == 'critical')
        nc = sum(1 for _, t in nf if t == 'non-critical')
        pa = sum(1 for _, t in nf if t == 'paper')
        L.append('| **%s** %s | %s (%s; %s) | %s | %s | %s | %s | %s | %s | '
                 '%d | %d | %d/%d/%d | %d | %d | %d | %s |'
                 % (sid, title, pid, anchor,
                    clip(re.sub(r'^D6:\d+;\s*', '', why), 80), status,
                    ' '.join(dict.fromkeys(c['gates'])) or '—', entry or '—',
                    exit_ or '—', fb or '—', owner, len(c['nodes']),
                    len(c['ledger']), crit, nc, pa, len(c['bloc']),
                    len(c['claims']), len(c['atlas']), path))
    L.append('')
    L.append('## 2. CRITICAL PATH = filtered view (`path: critical` steps, '
             'program order)')
    L.append('')
    crit_steps = [s for s in STEPS if s[3] == 'critical']
    L.append(' → '.join('**%s**' % s[0] for s in crit_steps)
             + ' → **PAPER** (methods freeze at F2 exit + F3 showcase; G5)')
    L.append('')
    L.append('Order of record: F2.CFD-2 sits INSIDE F2 (PROGRESS B19(a) '
             '"in coda F2"), hence BEFORE the F3 plug sector; the advisory '
             'schema D/E order "TWIN → CFD-2" is a deviation of the '
             'authored schema (section 5). F3.RK1 runs PARALLEL to F2 '
             '(D6:222-223). F4b is order-interchangeable with F3 given F2 '
             'exit (D6:228-232) and carries no critical object.')
    L.append('')
    for sid, pid, title, path, why in crit_steps:
        c = cover[sid]
        L.append('### %s — %s' % (sid, title))
        cf = [i for i, t in c['findings'] if t == 'critical']
        cb = [i for i, t in c['bloc'] if t == 'critical']
        L.append('- critical findings (%d): %s' % (len(cf), ', '.join(cf)
                                                    or '—'))
        L.append('- critical BLOCCATO (%d): %s' % (len(cb), ', '.join(cb)
                                                    or '—'))
        L.append('- nodes (%d): %s' % (len(c['nodes']),
                                       ', '.join(c['nodes']) or '—'))
        L.append('- ledger rows (%d): %s' % (len(c['ledger']),
                                             ', '.join(c['ledger']) or '—'))
        L.append('- open theory objects consumed (%d): %s'
                 % (len(c['claims']),
                    ', '.join('%s [%s]' % x for x in c['claims']) or '—'))
        L.append('')
    L.append('## 3. Declared overrides (placement not given by a literal '
             'phase token in the source row)')
    L.append('')
    L.append('| kind | id | placed at | reason (anchor) |')
    L.append('|---|---|---|---|')
    for kind, oid, step, why in d['overrides']:
        L.append('| %s | %s | %s | %s |' % (kind, oid, step, why))
    L.append('')
    L.append('## 4. OUT ledger (objects in no step, each with its why)')
    L.append('')
    L.append('| kind | id | OUT:why |')
    L.append('|---|---|---|')
    for kind, oid, why in d['outs']:
        L.append('| %s | %s | %s |' % (kind, oid, why))
    L.append('')
    L.append('## 5. Deviations of the advisory schema D/B vs this derivation '
             '(finding method:sroadmap-schema-authored-from-partial-context)')
    L.append('')
    L.append('1. F3, F4b, F5, F6 absent from schema D (F3 admitted in E).')
    L.append('2. The decisive TWIN is an F3 object (plug sector), not F2.')
    L.append('3. "P-1" in schema D row 6 = D6 paper-stream line "methods '
             'freeze (F2 exit) + showcase (F3)", not P-1-numeric (F5a).')
    L.append('4. CFD-2 is inside F2 (B19(a)), before F3 — not after the TWIN.')
    L.append('5. BLOCCATO count 17 (advisory) vs %d rows measured here; '
             'atlas phase mentions 290 (advisory) vs %d measured under the '
             'declared regex.' % (len(d['bloc']), len(d['atlas'])))
    L.append('6. H20/C61 are homed at F4b by the registries and at F3 by '
             'D6 — carried as an override + an OPEN critical finding, not '
             'silently re-homed.')
    L.append('')
    L.append('## 5-bis. STALE OWNERS — open objects whose owner names a '
             'CLOSED phase (derived; re-home duty = F2-B0 hygiene)')
    L.append('')
    if d['stale']:
        L.append('| closed step | id | kind/path |')
        L.append('|---|---|---|')
        for s, oid, tag in d['stale']:
            L.append('| %s | %s | %s |' % (s, oid, tag))
    else:
        L.append('none')
    L.append('')
    L.append('## 6. Appendix (machine): per-step object lists')
    L.append('')
    for sid, pid, title, path, why in STEPS:
        c = cover[sid]
        L.append('### %s' % sid)
        L.append('- gates: %s' % (', '.join(dict.fromkeys(c['gates'])) or '—'))
        L.append('- nodes: %s' % (', '.join(c['nodes']) or '—'))
        L.append('- ledger: %s' % (', '.join(c['ledger']) or '—'))
        for tag in ('critical', 'non-critical', 'paper'):
            ids = [i for i, t in c['findings'] if t == tag]
            if ids:
                L.append('- findings %s (%d): %s' % (tag, len(ids),
                                                     ', '.join(ids)))
        if c['bloc']:
            L.append('- BLOCCATO: %s' % ', '.join('%s [%s]' % b
                                                   for b in c['bloc']))
        if c['claims']:
            L.append('- open claims (SCHEMA/CONJECTURE): %s'
                     % ', '.join('%s [%s]' % x for x in c['claims']))
        if c['atlas']:
            by = {}
            for m in c['atlas']:
                by.setdefault(m['chapter'], []).append(str(m['line']))
            L.append('- atlas mentions (%d): %s'
                     % (len(c['atlas']),
                        '; '.join('%s :%s' % (k, ','.join(v))
                                  for k, v in sorted(by.items()))))
        L.append('')
    L.append('## 7. Counts (measured by this tool)')
    L.append('')
    nf = len(d['findings'])
    L.append('- phases %d (+PAPER track) / gates %d / graph nodes %d / '
             'ledger rows %d / OPEN findings %d (critical %d, non-critical '
             '%d, paper %d) / BLOCCATO rows %d / atlas mentions %d'
             % (len(d['phases']), len(d['gates']), len(d['nodes']),
                len(d['ledger']), nf,
                sum(1 for e in d['findings'] if e['path'] == 'critical'),
                sum(1 for e in d['findings'] if e['path'] == 'non-critical'),
                sum(1 for e in d['findings'] if e['path'] == 'paper'),
                len(d['bloc']), len(d['atlas'])))
    L.append('- claims registry %d rows: %d open-class (SCHEMA/CONJECTURE) '
             'placed-or-OUT; THEOREM/THEOREM*/PRACTICE = %d closed '
             'statements (OUT by class, indexed by lint xv)'
             % (len(d['claims']), len(d['claims_open']),
                len(d['claims']) - len(d['claims_open'])))
    L.append('- overrides %d / OUT %d' % (len(d['overrides']),
                                          len(d['outs'])))
    body = '\n'.join(L) + '\n'
    h = hashlib.sha256(body.encode('utf-8')).hexdigest()
    return body + '\n<!-- roadmap-derive content-hash: %s -->\n' % h


def stored_hash(text):
    m = re.search(r'<!-- roadmap-derive content-hash: ([0-9a-f]{64}) -->',
                  text)
    return m.group(1) if m else None


def body_hash(text):
    # the split consumes the newline that OPENS the footer line; the body
    # keeps its own trailing newline, so nothing is re-appended here
    body = re.split(r'\n<!-- roadmap-derive content-hash: ', text)[0]
    return hashlib.sha256(body.encode('utf-8')).hexdigest()


def main(argv):
    d = derive()
    text = render(d)
    if '--check' in argv:
        try:
            cur = io.open(OUT_DOC, encoding='utf-8').read()
        except OSError:
            print('ROADMAP missing'); return 1
        ok = cur == text
        print('ROADMAP %s' % ('FRESH' if ok else 'STALE — re-run the tool'))
        return 0 if ok else 1
    io.open(OUT_DOC, 'w', encoding='utf-8', newline='\n').write(text)
    print('wrote %s (%d steps, %d overrides, %d OUT, %d atlas mentions)'
          % (os.path.relpath(OUT_DOC, ROOT), len(STEPS), len(d['overrides']),
             len(d['outs']), len(d['atlas'])))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
