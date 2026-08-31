# PROGRESS — cycle-averaged variational nozzle program (living state)

> Single source of truth della progressione. Aggiornare a OGNI chiusura
> di sessione/fase (CLAUDE.md R3). PROTOCOLLO DI APERTURA (R2, dalla
> S-ROADMAP 2026-08-31): docs/START_HERE.md PER PRIMO, poi memoria di
> progetto, M0 (per profondità), D6 (stati/gate), questo file e la
> roadmap DERIVATA docs/ROADMAP_critical_path.md (rigenerata da
> tools/roadmap_derive.py, lint (xxiv)). Forma snella (U5 S-ROADMAP):
> ORA = tabella, NEXT = un passo atomico, BLOCCATO = tabella con
> `path:`, censimento = UNA tabella in place (SR-7), storia integrale
> in docs/rde_nozzle_PROGRESS_ARCHIVE.md (append-only, SR-10).

## ORA (2026-08-31, S-ROADMAP CHIUSA — R38 CONSUMED)

| campo | valore (misurato in finestra, SR-12) |
|---|---|
| Fase D6 | F2 GENERAL ENGINE **non ancora aperta** (contatore "F2 session 0/6"); F0/F1/F1b CLOSED di record (D6 :91, :137); F3/F4b/F5/F6 non aperte |
| HEAD | branch `rde-nozzle-program`; apertura S-ROADMAP = bff3338; commit di chiusura elencati nel log |
| Ultimo gate | lint registri (xix)/(xx)/(xxii)/(xxiii) + roadmap (xxiv) PASS; suite completa: esito quotato nel log |
| Ultima sessione | S-ROADMAP (advisory ADVISORY_Sroadmap_prompt_2026-08-31.md CONSUMED; log validation/PROGRESS_2026-08-31_Sroadmap.md) |
| Passo atomico | vedi NEXT (F2-B0) |
| Cammino critico | docs/ROADMAP_critical_path.md — DERIVATO (D6 × atlas × registri incl. claims SCHEMA/CONJECTURE), 16 passi, vista `path: critical` = F2-B0 → F2.REPR → F2.ENGINE → F2.M-RED → F2.CFD-2 → F3.RK1∥ → F3.PLUG → F3.TWIN → F3.TOURNAMENT → PAPER; nessun cammino "completo" citabile senza il PASS di lint (xxiv); emendamento D6 per F2.REPR/F3.TOURNAMENT = bozza in attesa di ratifica utente |
| BLOCKING attive | findings `path: critical` 44 / BLOCCATO `path: critical` 3 (tabella sotto) |
| Budget orchestrazione | S-ROADMAP: tetto dichiarato inline-only, 0 subagenti, 0 token subagente (SR-9) |
| Registri | findings 258 (213 OPEN = 44 critical / 125 non-critical / 44 paper); choice 62; claims 163; lit 174 + 9 bulk; glossario 47 fam + 244; ADVISORY_INDEX 108 file + 5 block |
| GENO health | patch strumentazione NON inerte nel working tree GENO (src/lib/MoC_Gen_m.f90 +42, Profile_m.f90 +95 incl. AUDIT VARIANT B; diff == validation/RAW_geno_audit_instrumentation_2026-08-13.patch, md5 822ca4f); build WSL ultima = link error (Jul 17); quarantena + ri-baseline md5 = passo BLOCKING F2-B0 (ROADMAP) — GENO letto SOLO in read-only in S-ROADMAP |

## NEXT (atomico)
F2-B0 (F2 BLOCCO 0, contatore 0/6; R8 gate-first in apertura; passi derivati F2-B0 -> F2.REPR): (1)
rileggere docs/ROADMAP_critical_path.md rigenerata (lint xxiv PASS);
(2) GENO health: quarantena patch (comando pre-verificato nel log
S-ROADMAP) + ri-baseline md5 con build — su autorizzazione utente
(BLOCCATO B-GENO); (3) finestra engine a convergenza (cluster
C31/C57/C58/C60/[P-IPADJ] + SDP-CAND-8); (4) P0 staleness
import-closure; (5) O3.4 gamba gradiente; (6) sessione
topologia+modellistica (BLOCCATO 16 ratificata a F2-entry, con dossier
S-5F/C51/C58/C60); (7) PROTOCOLLO TWIN pre-registrato (config, vincoli
identici, decision rule, stop ~1% Isp; dati = caso A Annex B, settore
plug troncato = F3); (8) eredità S-PRES da ingerire (BUILD_LOG CKP-S4-*,
CONSECUTIO D4/D5, HARVEST H-1/H-4, finding atlas ch5). Poi M-RED (prima
campagna F2, nessun pull-forward).

## BLOCCATO / GATE APERTI (tabella; `path:` = triage rispetto al TWIN decisivo; storia integrale delle voci in PROGRESS_ARCHIVE)

| id | item | stato | path | owner + trigger | carrier |
|---|---|---|---|---|---|
| B-G5 | G5 passaggio umano Kraiko-1979/PMM: blocca le SUBMISSION P-1/P-2/P-3, non il lavoro; pacchetto d'invio pronto, residuo = invio dall'account istituzionale | LOCK (utente) | paper | utente; trigger = prima submission | validation/G5_dispatch_email.md + G5_pmm_toc_sweep_1957-1990.md |
| B-VENUE | Venue P-2 (AIAA J primaria + arXiv a G5∧bozza; fallback Aerospace; JOTA terziaria) | DECISA S4 (delega) | OUT:consumed | — | docs/rde_nozzle_P2_outline.md §7 |
| B-ADR | ADR panel 2026-07-16: ratifica utente PENDENTE; nessuna implementazione; esecuzione gated alla finestra ADR-D4 (con B9) | APERTO | non-critical | utente; trigger = finestra ADR-D4 (calendario fissato al touchpoint F2-entry, B17) | validation/ADR_panel_2026-07-16.md (non committato) |
| B-G0 | G0 stack decision: JAX primario, Julia+Enzyme alternate, GENO dual-code; residuo toolchain CHIUSO; falsificatore loop-speed armato (MET S25/S25-bis) | DECISO S10 | OUT:consumed | ratifica utente solo su trade-off fuori criteri D6 | docs/rde_nozzle_G0_decision.md |
| B-RAOPLUG | RaoPlug S1/S2 fix in GENO (o status single-oracle Rao-1961 Table-1 dichiarato): ENTRY di F3 (D6 :214-218), prerequisito OP-2/PB-2 | APERTO, mai attaccato | critical | repo GENO, suo protocollo (R13); trigger = F3 entry (de-risk RK1 autorizzato in parallelo a F2) | D6 §6 item 3 |
| B9 | ADR-D4: headline spike re-bless 242.5 s constrained + trunc 0.20 DECISE; esecuzione (README/examples/test/REBLESS) gated alla finestra ADR-D4 col RIDER G-11 (mappa definizioni, banda transiente P-B, chiusura p_b + sensibilità Humphreys ×2.45, Veen WG10-FAILED, Purdue CTAP) | DECISA, esecuzione gated | non-critical | finestra ADR-D4 (touchpoint F2-entry fissa il calendario); il rider p_b viaggia già su C61 + finding litreview:residue-r8-r23 (critical) | SYNTHESIS_nozzle_rde_arrivals.md CT-4; BASE_PRESSURE_HARVEST_c4.md |
| B10 | Ratifiche D-01/C31-minimale/C30 + decisioni A2=(a), D-49 esclusa | CONSUMATA 2026-08-13 | OUT:consumed | — | PROGRESS_2026-08-13_Fservice.md |
| B11 | Schedulazione R22-lit (disentanglement 3D/3D-mediato/2D) come primo blocco F2 | CONSUMATA da B19(a) (CFD-2 in coda F2, CFD-1 post-M-RED) | OUT:consumed | — | riga B19 |
| B12 | P0 procurement: ISABE-2003-117, Bogdanov 2002, tesi Harroun 2019, Shmyglevskii PMM 26(1) 1962 (+ top-3 harvest e 3 ask fermi di B19) | APERTO (WANTED) | paper | utente/procurement; trigger = finestra lit / claim che li cita | docs/literature_registry.yaml (righe WANTED) |
| B13 | Due one-liner CLAUDE.md (ban mutazioni env + sessioni parallele); memory-mirror UD-5-sub NO | CONSUMATA 2026-08-13 | OUT:consumed | — | CLAUDE.md Preferenze |
| B14 | Touchpoint confine Fase C (P_amb slot, cava litreview, seed registry, slot Sonnet 141-fork, rotazione) | CONSUMATA 2026-08-19; residui migrati in B15 | OUT:consumed | — | PROGRESS_2026-08-19_SfoundationsC.md |
| B15 | Touchpoint C3: BLOCCATO 9 decisa; O5 numpy 2.5.2 ADOTTATO (env misurato 2.5.2); Lean con dossier; S-5F rinviata F2-entry; C51 rung-3a F2; G9 slip-sheet F2-entry; AG-1 standing; papers 18 arrivi | CONSUMATA 2026-08-20 | OUT:consumed | — | PROGRESS_2026-08-20_SfoundationsC3.md |
| B16 | Proposta sessione "topologia-e-modellistica" (campo IE aerospike Harroun Figg. 12-20 + aggiudicazione rappresentazioni 4-campi / 5-field / route-B / ibridi / 3D) | RATIFICATA da B19(b) a F2-entry (scope esteso field-reading) | OUT:consumed | esecuzione = passo F2-B0 (ROADMAP) | PROGRESS_ARCHIVE (testo integrale) |
| B17 | Touchpoint C4 apertura: meter fresco; Lean DEFER a F2-entry (dossier di record); calendari ADR-D4 + estrazione P-1 fissati al touchpoint F2-entry; 3 ask paper fermi | CONSUMATO 2026-08-20 con residui (Lean, calendari, ask) | non-critical | touchpoint F2-entry (utente) | validation/DOSSIER_lean_pricing_2026-08-20.md |
| B18 | S-PRES milestone ESA (catena C4 → S-PRES → F2) | CONSUMED CON PIVOT 2026-08-25 (deck utente fuori repo; prove-per-atlas TRACE/CONSECUTIO/HARVEST) | OUT:consumed | eredità a F2-entry in NEXT | deck_build/BUILD_LOG.md + trace/ |
| B19 | Touchpoint C4 chiusura: CFD-2 in coda F2; CFD-1 post-M-RED; B16 ratificata F2-entry; M-RED prima campagna F2; procurement top-3 + 3 ask | CONSUMATO 2026-08-21 (decisioni di record) | OUT:consumed | residui aperti = B-CFD1, B12 | PROGRESS_2026-08-21_SfoundationsC4.md |
| B-CFD1 | Decisione CFD-1 (test del pin su configurazione accoppiata reale, ~12M celle, canale partner/procurement) — SI DECIDE POST-M-RED con dossier + criteri PM22-conforme vs Jourdaine-patologico | APERTO, gated post-M-RED | critical | utente; trigger = chiusura campagna M-RED (banda eps) | pipeline_decision_map.md :77 (R22-CFD); ROADMAP passo F2.CFD-1 |
| B-GENO | GENO health: quarantena patch audit (revert 2 file, patch conservata byte-identica in validation/RAW_geno_audit_instrumentation_2026-08-13.patch) + ri-baseline md5 (8 CASES/*/reference/checksums.md5) con build WSL; write in GENO = autorizzazione utente (repo indipendente, suo protocollo) | APERTO (S-ROADMAP: report + comando pre-verificato, nessuna scrittura) | critical | utente autorizza a F2-B0; trigger = prima misura nominale GENO (twin leg / oracolo O2/O3.4) | log S-ROADMAP §U6; LEDGER_dubbi_moc_2026-08-13.md §D |
| B-S5F | Decisione build [S-5F] (percorso A free-vortex / B five-field engine+adjoint / C procurement dati tangenziali; fork lemma-misto vs monitored-neglect, finding theory:s5f-path-a…) + priorità C51 (confermata rung-3a F2) | RINVIATA a F2-entry (B15(d)) | non-critical | utente al touchpoint F2-entry (dentro la sessione B16) | swirl5f_panel_2026-08-19/ DISPATCH §9 |

## CENSIMENTO â€” TABELLA CONSOLIDATA R1-R36 (S-ORDINE 2026-08-13, S8;
## estesa in-place R34-R36 dalle finestre 2026-08-13:
## una riga per item, stato = il blocco delta PIU' RECENTE che la
## tocca; la storia dei delta vive VERBATIM in
## docs/rde_nozzle_PROGRESS_ARCHIVE.md. REGOLA SR-7: questa tabella
## si edita IN PLACE, i blocchi-delta sono VIETATI; il lint censimento
## (single-table grep) e la riga di checklist R3 la proteggono.)

| R | item | stato | owner + trigger (se aperta) | artefatti |
|---|---|---|---|---|
| R1 | scipy res.v convention | CONSUMED S24 | â€” | log S24 (T1) |
| R2 | audit 5-righe S18 | CONSUMED S24 | â€” | log S24 (T2a, clausola T-T3-MAP) |
| R3c | C4 chiusura meccanica | CONSUMED S25 | â€” | commit 32459ca (ondemand tipizzato + staleness link) |
| R4c | X-T3SI-conv corner dry-run | SCHED | F5a entry hard; check opportunistico a ogni R3 | â€” |
| R5c | census-lemma (S15 + emendamenti D2.1) | SCHED | F2-exit (finestra freeze metodi; F3-entry se F3 apre prima) | PANEL_topology_census + pin utente |
| R6c | PAP-RIM (matrice strade x inserzioni) | SCHED | F2-exit, stessa finestra | roads-insertion-matrix directive |
| R7c | review G0/T2 | CONSUMED S25 | â€” | rde_nozzle_G0_decision.md par.4 nota S25 |
| R8c | residui S19 (b)/(c)/(d) | SCHED | F2b (leve upgradability P-2; freeze intatto) | â€” |
| R9c | X-SCANM replay probes | SCHED | F2 | â€” |
| R10 | rejector field-level C1 | GATED | owner F2, trigger = carrier F2b (scioglie la conditional freeze P-2; 3 istanze della classe) | â€” |
| R11 | Lemma-B across-shocks | SCHED | F5a entry al piu' tardi | â€” |
| R12 | a-B2 | SCHED | F3 entry | â€” |
| R13 | GENO: md5 freeze s3 + N-74(+esteso) + knob jump-depth | GATED | repo GENO, SUO protocollo; trigger = prossima sessione GENO/s3 | RAW_geno_audit_instrumentation (patch 2026-08-13) |
| R14 | ownership advisory | CLOSED | â€” | BLOCCATO 7 (decisione utente) |
| R15 | G5 (passaggio umano Kraiko/PMM) | LOCK | utente (blocca SUBMISSION, non lavoro) | G5_pmm_toc_sweep (OF-RECORD) |
| R16 | acquisizioni letteratura | CONSUMED-with-residue | residuo: Salas (condizionale F4b) + WANTED list (10 righe nel literature registry, incl. P0 procurement handoff 2026-08-13) | docs/literature_registry.yaml |
| R17 | preprint | LOCK | utente | â€” |
| R18 | O5 ordine dei limiti (numpy 2.5.2) | GATED | decisione utente a confine sessione (gamba C7; S24+1 opz altrimenti F2 entry) | registry: conditional-class O5 |
| R19 | mu sign test | CONSUMED S24 | â€” | log S24 (mu=0 sul ladder; meta' GENO -> R13) |
| R20 | item F2/F3/F5a gia' di record | CARRIED | near-axis, duties F2a incl. mean_swirl, DUTY-4(i), U3', (q;s,h0)+[X-TBAK], plug/C- mirror, X-T3CTRL | D6 F2/F3 |
| R21 | C7 gamba refine/classe-ricca + O5 | SCHED | S24+1 opzionale pre-autorizzata, altrimenti F2 entry | â€” |
| R22 | ENGINE SPEED | CONSUMED S25+S25bis | â€” | contatore di record: segmento 14.9-20.1 s vs 30 MET, campagna 10-14 min vs 25 MET; [X-SPDB] |
| R23 | survey termo condizioni | CONSUMED-with-residue | C-A SCARICATA S25; C-B/C-C/C-D GATED (owner F2 / primo ingest ATLAS); flag GPLv3 FLINT lato GENO | ADVISORY_S24_thermo_closure_survey |
| R24 | certificati FRONTI DI CONTATTO (schema Shmyglevskii) | GATED | owner F4b | dispatch A2 |
| R25 | CHOICE LEDGER | EXTRACTED S-ORDINE | righe aperte (25 NEVER + 14 single-author) vivono nel ledger tipizzato con owner per riga | docs/choice_ledger.yaml (48 righe, lint xix famiglia f) |
| R26 | advisory gap-map | CONSUMED S25 + SEEDED S-ORDINE | â€” | ADVISORY_S24_sota_gapmap (ingested + 63 righe nel findings registry, tranche S7b) |
| R27 | quarantena B1 (identita' (6)-vs-(G) Shmyglevskii) | QUESTION | falsificatore nominato ([X-VMON] grid), owner F4b; NON e' un finding | â€” |
| R28 | numeric-lint scope hole | CONSUMED-AS-CHANNEL S25bis | classificazione dei 622 letterali = F2-entry (riga registry) | tier ratchet (vii), baseline per-file |
| R29 | pipeline-sense expert review (standing) | STANDING | prossima istanza = primo tocco algoritmico F2 | direttiva + convergenze S25/S25bis |
| R30 | S25-bis (M5c+M6+cap) | CONSUMED S25bis | â€” | PROGRESS_2026-08-12_S25bis_speed.md |
| R31 | FINDINGS-AS-CODE | LANDED + SEEDED S-ORDINE | tranche residue NOMINATE: (c) refuter/red-team S25-S25bis, (d) consumption map 4 advisory, (e) corpus lit 2026-08-13 (~101 confrontation + ~40 MoC/GENO) â€” prima duty della prossima finestra di seeding | docs/findings_registry.yaml (20 -> 135 righe; lint xix) |
| R32 | S-ORDINE de-entropizzazione | CONSUMED-with-declared-split 2026-08-13 | split di record (regola contratto S7): tranche seeding (c) refuter/red-team S25-S25bis + (d) consumption map 4 advisory + (e) corpus lit 13-08 (~101+~40) = coda NOMINATA della prossima finestra seeding; il resto ESEGUITO (piano convergiuto+red-team, snapshot durabilita', indice 92, 4 registry nuovi, glossario 163, seeding 20->135, PROGRESS slim multiset-0, memoria, gate NOTHING-LOST PASS con rejector+loss-hunter provati, riconciliazione 516 scarto 0, CLAUDE.md R7+README ratificati) | ADVISORY_SORDINE_plan_2026-08-13 + PROGRESS_2026-08-13_Sordine.md |
| R33 | S-CERT audit certificazione agnostico | CONSUMED 2026-08-13 | verdetto vincolante: NON-CERTIFICABILE, 2 P0 a HEAD ((vii) riparato in chiusura dichiarata; staleness import-closure = owner F2); P0-integrita' audit scaricato via dual-seed; triage completo a registro (157 righe findings); delta vs 2026-08-07: vecchio tier P0 consumato-verificato, difetti migrati oggetto->certificatore; MC8 sopravvive 8/8 | ADVISORY_Scert_prompt CONSUMED + PROGRESS_2026-08-13_Scert.md + scert_raws_2026-08-13/ |
| R34 | REGIME STANDING anti-entropia SR-1..SR-12 | STANDING | enforcement = lint (xix)/(xx)/(xxii)/(xxiii) con rejector + checklist CLAUDE.md R7 (ratificata 2026-08-13); NON si consuma, si mantiene | ADVISORY_SORDINE_plan_2026-08-13 par.5 |
| R35 | S-FOUNDATIONS (teoria-prima-di-F2, ordine utente 2026-08-13: "arrivare al motore generale con tutta la teoria costruita e dimostrata") | CONSUMED PIENO 2026-08-21 (parte C4 2026-08-20/21: FASE D dimostrata e atterrata a convergenza (centerpiece R22F 4 round x 3 lenti + escalation 4 minori TUTTI DRY + E-5; M0 riceve [T-DISC]/[T-RED]/[T-DCRX]/NTF/CLG/[R22F-FORCHETTA] con classi finali; G-c (ii) scaricata-citabile); Fase C completata a 62 righe (C59-C62 coniate: forma-temporale, NAND/SAND, p_b-closure, quadratura — 7 istanze classe no-row totali); COVERAGE GATE PASS dual-seed provato; PIPELINE DECISION MAP di record (62 nodi/45 archi, refuter 0/0); campagne letteratura (nozzle-RDE 0-BREAK, field atlas, base-pressure, throat) + emendamento protocollo censimento su sfida utente sostenuta; touchpoint chiusura: CFD-2 in F2/CFD-1 post-M-RED, BLOCCATO 16 ratificata F2-entry, M-RED resta F2, procurement top-3+3; catena aggiornata C4 -> S-PRES -> F2; log PROGRESS_2026-08-21_SfoundationsC4.md. Parte C3: Blocco 0 + WAVE 3 COMPLETI â€” 33 righe ledger aggiudicate e ATTERRATE con 0 break (76 finding, 21 repair/39 amendment sostenuti, 0 refuter cassati, escalation-per-regola zero); C50 escalata a Form-2 PIENA su ordine utente: VERDICT_C50_form2 = metrica-unica product-form che SUPERSEDE lo split-by-role (0 residui forced-pick); confirm-on-repairs istanza 2 = SECONDA cattura vera (CR-W3-R10-1: annotazione [T-XWS] dichiarata ma assente in M0 â€” riparata in-window, sunset definitivamente morto); retro-sweep catena su domanda utente (1 tensione naming preset-Uno senza falsificatore, 8 ancore arricchimento, PAIR-8 = SCREEN dichiarato dopo sfida utente sostenuta, PAIR-9 wrong-cite annotato); passa REM incondizionata 20/20 pulita (judge non in strain, criterio pre-registrato); C58 coniata (fondazione AD/JAX â€” user catch, terza istanza classe no-row dopo C49/C56, entry contract = corpus adjudicato); ledger a 58 righe = 12 DECIDED/36 MIXED/2 SA/8 NEVER misurati, tutte le NEVER trigger-armed; 21 arrivi paper registrati/promossi (15 UNREAD->READ-PARTIAL con pagine dichiarate); direttive utente a strumento: valvola AG-1 adottata, enumerazione foundation-choice + arrivals-mapping = categorie coverage gate, PIPELINE DECISION MAP = deliverable C4; SPLIT residuo su meter >75% -> C4: Blocco 2 Fase D (centerpiece 3-lenti, brief pronto) + Blocco 3 chiusura catena; log PROGRESS_2026-08-20_SfoundationsC3.md. Parte C2 2026-08-19 sera: doc1 DRY leg 3+5 CHIUSI + [T-T0P] main atterrato + Fase C onde 1-2 AGGIUDICATE E ATTERRATE (16 righe ledger, C56/C57 coniate, confirm-on-repairs istanza 1 = cattura vera) + audit agnostico triagiato + direttive 8/9+D/E a registro; SPLIT residuo -> C3: wave 3 + Blocco 4 centerpiece + Blocco 5; log PROGRESS_2026-08-19_SfoundationsC2.md. Parte 1 2026-08-17: Fase 0 + Fase A 141 fork + Fase B diff + audit ipotesi + contratto/L4R1 + prove-1 + coverage gate; sessione C Blocchi 0-2 2026-08-18/19: passata r2 15-obiezioni/0-respinte + escalation E-1..E-4 + seed v3 LAYER PROVATO NEI 2 SENSI + leg 6/14 CHIUSI (leg 14 = "THEOREM modulo (H-UP-fam)" guadagnata) + GATE APERTO + LANDING M0/registry COMPLETO ([L4-CERT] m_n+split-cert+W1-W4; claims 149/findings 240/C53; suite 23/23 post-riparazione (vii)); SPLIT residuo = Blocchi 3-5 (Fase C right-sized + centerpiece T-DISC/T-RED/M-RED + ledger fork/coverage gate/R3) in sessione fresca (rotazione ratificata) + doc1 leg 3+5 rev-10 prima azione parallela; log PROGRESS_2026-08-19_SfoundationsC.md) | collocazione: DOPO F-SERVICE+S-CERT, PRIMA di F2. Scope MISURATO (cross-reconciliation 2026-08-13, sweep 13 doc + raws + archivio, standard severo: 1 upgrade C46->DECIDED, 25 NEVER CONFERMATE con nota per-riga): (a) aggiudicazione a convergenza delle scelte F2-CONSUMATE tra le 25 NEVER + meta'-panel delle 13 single-author (panel Form-2 con avvocato genuino dell'alternativa + refuter; input = ledger riconciliato + MC8 di S-CERT); le measurement-gated convergono su protocollo+falsificatore pinnati, meta' misurata = entry duty VINCOLANTE F2; righe F3/F4b/F5-owned chiudono all'ingresso della LORO fase (regola: nessuna fase apre con NEVER sui componenti che consuma); (b) teoria pre-derivabile di classe (a): derivazione NTF, aggiudicazione BC GAP-5, [OBJ-DOM], lemma rilassamento delta-carrier, assorbimento M0 mean-swirl, bound cross-lowering (parte derivabile); (c) DECISIONE UTENTE in-sessione: pin census-lemma+PAP-RIM (resta F2-exit vs anticipo pre-F2) | docs/choice_ledger.yaml (RECONCILIATION block) + questo log STEP 13 |
| R36 | F-SERVICE ratifiche (finestra pre-S-CERT, catena 1e188a9; RINUMERATA R35->R36 alla riconciliazione col conio parallelo di R35=S-FOUNDATIONS, 3961d3d 14:54 < ea2abce 15:23: il primo conio tiene il numero â€” i riferimenti "census R35" nel messaggio di ea2abce e nel log di finestra leggono QUESTA riga) | CONSUMED 2026-08-13 | â€” | ADVISORY_Fservice_Scert_prompt (Parte 1) + PROGRESS_2026-08-13_Fservice.md: D-01/C31-min/C30 ratificate+eseguite; batch R4 REV-3 ([S-T0P], [T-T7CN], C-HEXO/H-EXO, PB-2 bloccata, E4 lineage, non-contenimenti h/i/j); 5 carrier REFUTE_C riparati SR-11 (o33 R8/R9/R10, mgov dual clause, a1 regime decl; gate ri-eseguiti, stampi 13-08); esclusioni nominate D-49 (limite campione S-CERT, conferma utente)/D-20/GENO-owned; A2=(a) pinnata |
| R37 | S-PRES milestone ESA (catena C4 -> S-PRES -> F2; item BLOCCATO 18) | CONSUMED CON PIVOT 2026-08-25 (S1-S4; deck finale = utente, Desktop/Presentazione_ESA.pptx fuori repo; chiusura = prove-per-atlas TRACE/CONSECUTIO/HARVEST; 2 finding mintate; lint xix/xx/xxii verdi alla chiusura 2026-08-31) | — | log S1 PROGRESS_2026-08-22_Spres1 + SESSION2_LOG + deck_build/BUILD_LOG.md (S3+S4) + trace/ + act_rework/ ; commits c4dc1d0..78c19a9 |
| R38 | S-ROADMAP (U1'-U7: roadmap DERIVATA D6xatlasxregistri + lint copertura (xxiv), START_HERE + record_query + lint manifest, triage soli-tag path:, R8 gate-first, PROGRESS snello, GENO health, P1_outline) | CONSUMED 2026-08-31 (inline only, 0 subagenti; addenda E/F eseguiti: cammino DERIVATO, deviazioni dello schema D = finding method:sroadmap-schema-authored-from-partial-context SUPERSEDED + plan:h20-c61-registry-homing… CONFIRMED critical; triage 211->213 OPEN = 44/125/44 (2 chiusure con evidenza, 5 mint: schema advisory, homing H20/C61, torneo full-envelope senza passo D6, representation ladder/controparte 3D senza passo D6, tool NASA non atterrati); GENO = passo BLOCKING B-GENO) | residui: B-GENO (utente), lint (xxiv) rigenerato a ogni apertura (R8) | validation/PROGRESS_2026-08-31_Sroadmap.md + docs/ROADMAP_critical_path.md + tools/roadmap_derive.py + tests/test_roadmap_coverage.py |

## LOG SESSIONI
I log per-sessione vivono in validation/PROGRESS_*.md (indice:
validation/ADVISORY_INDEX.md). La storia integrale di questo file
(stati precedenti, delta censimento, NEXT storici, log S1-S25bis)
e' in docs/rde_nozzle_PROGRESS_ARCHIVE.md (append-only, SR-10).

Ultime sessioni (1 riga/sessione, puntatore al log; storia completa nell'archivio):
| data | sessione | esito | log |
|---|---|---|---|
| 2026-08-21 | S-FOUNDATIONS-C4 (R35) | CONSUMED PIENO: Fase D a convergenza, pipeline decision map, coverage gate PASS | validation/PROGRESS_2026-08-21_SfoundationsC4.md |
| 2026-08-22/25 | S-PRES S1-S4 (R37) | CONSUMED CON PIVOT: deck utente fuori repo; prove-per-atlas TRACE/CONSECUTIO/HARVEST | validation/PROGRESS_2026-08-22_Spres1.md; spres_raws_2026-08-22/SESSION2_LOG.md; deck_build/BUILD_LOG.md |
| 2026-08-31 | S-ROADMAP (R38) | CONSUMED: roadmap DERIVATA + lint (xxiv), START_HERE/record_query, triage path:, R8, PROGRESS snello, GENO health (BLOCKING), P1_outline | validation/PROGRESS_2026-08-31_Sroadmap.md |

