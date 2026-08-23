# HISTORIAN_INV_a — inventario rami (c) dei capitoli CH1-CH4, CH7 (slot B8a, W-B.2)

- **Stadio di confronto**: censimento dei rami (c) dei trittici §6 scritti da
  B8a (CH1, CH2, CH3, CH4, CH7), contro il record aggiudicato citato riga per
  riga nei §6 stessi.
- **Arco di consumo**: CH-REF (P-v) + retro-audit del deck (join su
  data+processo+verdetto); sezione FUORI-PERIMETRO per l'orchestratore/W-C.
- Data: 2026-08-23. Regola applicata: MAI ancore di Fase A fabbricate
  (F-des-3); le 12 righe SILENT del ledger (C2 cond., C5, C15, C16, C22, C23,
  C30, C40, C45, C46, C47, C48) sono ramo (c) per definizione (dichiarato in
  CH4 §6 testata).

## 1. Rami (c) per capitolo (argomento / doppia prova alternativa o ASSENTE / ancora)

### CH1 (7 argomenti; split (a)=3, (b)=0, (c)=4 — T-5 è SPLIT per gamba)
| Argomento (c) | Doppia prova alternativa | Ancora |
|---|---|---|
| T-1 pin dati H3 (pin utente, fuori perimetro derivativo per costruzione) | pricing boundary [S-T0P] + monitor T0-flatness armato + routing PB-5 | M0:560-561; M0 VI.4bis(v); M0:108-114 |
| T-5 gamba [T-T4] | PAN-S14 arbiter-confirmed + carrier X-GRP06/10/12 + falsificatore O2 | M0:397; claims_registry:329-340 |
| T-5 gamba SHARPNESS (max∫<∫max strictly) | **ASSENTE — FINDING F-1**: clausola enunciata senza prova scritta E carrier PB-2 mai eseguito | M0:2316-2319; problem_book:532-536; CH1 §4 Q4 [W2-R4] |
| T-6 [T-T3-MAP] | audit S24 T2a (precondizione nominata ESEGUITA) + corner T-T3-SI provato | M0:4138-4140; M0:879 |
| T-7 gamba [S-GBE] | carrier eseguibile X-GBE PASS | claims_registry:1843-1854 |
| T-7 gamba [S-BLITE] | **ASSENTE — FINDING F-2**: SCHEMA con brick nominato G12-L1-3D MAI eseguito | M0:3027-3044 |

### CH2 (7 argomenti; split (a)=2, (b)=0, (c)=4 — T-5 è SPLIT per gamba)
| Argomento (c) | Doppia prova alternativa | Ancora |
|---|---|---|
| T-2 [T-P3] | PAN-S14 16/16 (2026-07-22) + bench O3.3 PASS criterio primario S19 ([C-O33] quantificata) | commit `7be8b98`; memoria `s19-o33-campaign`; P1:200-203 |
| T-3 locus S19 kernel-stopped | falsificatore misurato a due decadi (2.9e-01 vs 9.4809e-03) + audit di scope C1 S21 | M0:3305, :3613; M0:368, :2821 |
| T-4 forma a cono (**') + [T-T7CN] | prova di record con controesempio + rejector S3/A39 armato + cross-check KT2015 | M0:2862-2874; M0:2830-2861 |
| T-5 gamba TWIN WARNING | prova esistenziale c'è; seconda prova di RILEVANZA (falsificatore a due segni sul parco) **ASSENTE — FINDING F-3** | M0:2895-2907; CH2 §2 riga twin ("esecuzione non trovata", §3.6) |
| T-7 genealogia K-O/Hoffman | confronto litreview avversario alla riga (25 paper, 2026-08-13) | `validation/ADVISORY_litreview_confrontation_2026-08-13.md`; litmap:451-456 |

### CH3 (6 argomenti; split (a)=3, (b)=0, (c)=3)
| Argomento (c) | Doppia prova alternativa | Ancora |
|---|---|---|
| T-1 correzione formal-first (decisione metodologica) | decomposizione ESEGUITA a convergenza in C4 con giudici | findings_registry:1459-1468; `blocco3/VERDICT_r22f.md` (2026-08-20) |
| T-5 canale (vi) delta/L_H UNDERIVED | escalation E-5 delta-r4 0 BREAK sulla DICHIARAZIONE + probe nonconvex; il numero è assente PER COSTRUZIONE (aperto strutturato, owner F2, deriver ordinati) — NON finding | `blocco3/VERDICT_escalation_c4.md`; M0:1946-1952, :2078-2112 |
| T-6 M-RED (esecuzione) | spec refutata da probe (bande riparate) + giudice PART 3; esecuzione F2-QUEUED sotto G1 — NON finding (structurally-gated dichiarato) | `phaseD_r22f_centerpiece.md:1237-1374`; `VERDICT_r22f.md:90-97` |

### CH4 (8 argomenti; split (a)=1, (b)=3, (c)=4)
| Argomento (c) | Doppia prova alternativa | Ancora |
|---|---|---|
| T-1 C58 stack JAX (fuori perimetro diff C1-C48) | flip clause quantificata armata (T1/T2a misurati) + review S25 G0/T2 | `docs/rde_nozzle_G0_decision.md` §4 :144-198; memoria `s25-engine-speed` |
| T-6 velocità S25/S25-bis | diff-refuter avversario (2 difetti veri riparati) + diff convergiuto 21/4/0/0 | commit `07400a4`; `ADVISORY_S25bis_diff_convergence_2026-08-12.md` |
| T-7 mappa pipeline | passaggio refuter dedicato 0 BREAK/0 REPAIR/5 AMENDMENT/4 NOTE | `docs/rde_nozzle_pipeline_decision_map.md:317-339` |
| T-8 S-CERT + incidente 23/23 | l'audit ostile context-free È la seconda prova; incidente colto dal rejector di conteggio SR-12 | PROGRESS :211 (R33); commit `c9bacd9` vs `7dea386` |
| (testata) 12 righe SILENT del ledger | sotto la granularità degli alberi ciechi — ramo (c) per definizione, doppia prova = i carrier per-riga del ledger dove esistono | `phaseB_tree_diff.md:393-399`; `docs/choice_ledger.yaml` |

### CH7 (6 argomenti; split (a)=4, (b)=0, (c)=2)
| Argomento (c) | Doppia prova alternativa | Ancora |
|---|---|---|
| T-1 correzione utente C-1 (evento storico) | il trittico stesso (join C5 su data+processo+verdetto) | CH7 header :3-8; memoria `artifact-connectedness-rule` |
| T-6 saldatura 3 (scaletta descrittiva unica) | **ASSENTE — FINDING F-4**: lettura di assemblaggio single-pass W-B.1, refutazione W-C attesa; si scarica al pass W-C sul capitolo | CH7 §1.5.3; `DISPATCH_swirl5f.md:80, :101-102` |

## 2. FINDING "doppia prova ASSENTE" (totale B8a: 4)

| ID | Capitolo | Contenuto | Scarico nominato |
|---|---|---|---|
| F-1 | CH1 §6 T-5 | sharpness di THEOREM 6 enunciata senza prova scritta; carrier PB-2 mai eseguito | write-up da mintare (W2-R4) + campagna PB-2 (owner: nessuna data di record) |
| F-2 | CH1 §6 T-7 | [S-BLITE] SCHEMA con brick G12-L1-3D nominato mai eseguito | esecuzione brick (finestra F2) |
| F-3 | CH2 §6 T-5 | twin warning: falsificatore di rilevanza a due segni mai eseguito sul parco | esecuzione a cap unilaterale attivo (regime-qualified) |
| F-4 | CH7 §6 T-6 | saldatura 3 = lettura di assemblaggio senza seconda prova | refutazione onda W-C sul capitolo |

## 3. FUORI-PERIMETRO (finding che toccano file non miei)

1. **Collisione di namespace "C31"**: nel corpus S-PRES "C31" indica SIA la
   riga ledger optimizer engine (`docs/choice_ledger.yaml:481-493`) SIA la
   ratifica utente della forma a cono di T7(c) (F-SERVICE 2026-08-13,
   memoria `fservice-scert-double-session`). CH1/CH2 usano la seconda,
   CH4 la prima. Il join del retro-audit deck (C5) e lo storyboard devono
   disambiguare a ogni occorrenza ("ratifica C31" vs "ledger C31") — owner:
   storyboard v3 / W-C / GUARD_CHECKLIST (file non miei).
2. **Ancora stale nota ma fuori dai miei file**: la riga findings
   `docs/findings_registry.yaml:1455` cita M0:463-498 per [S-T0P] che vive a
   M0:533+ (già dichiarata in CH1 §3.1 [W2-R8] come manutenzione fuori scope
   S-PRES) — la segnalo qui solo perché il retro-audit che joina sul mio §6
   T-3 di CH1 NON deve ereditare quell'ancora. Nessun edit fatto da me.

## 4. Nota di budget/strategia (dichiarazione d'onda)

Strategia dichiarata eseguita con UNA deviazione: la sezione 3 dell'indice
(git log integrale, ~290 righe) NON è stata letta per intero — interrogata
via grep mirati (2 finestre) per tenere il cap; nessun argomento è rimasto
senza data per questo. Capitoli letti una volta, mirati a §1-§2 (CH1 letto
integrale perché primo). Scrittura incrementale: 5 edit separate + questo
file.
