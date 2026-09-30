# ADVISORY — PROMPT DI SESSIONE "F2-B0" (carrier di record, 2026-08-31)

Stadio di confronto: chiusura S-ROADMAP (commit 620f6e9/160dd16/f1b0871;
log validation/PROGRESS_2026-08-31_Sroadmap.md; roadmap derivata
docs/ROADMAP_critical_path.md, lint (xxiv) PASS 16 passi; conteggi SR-12:
findings 259 [214 OPEN = 45 critical / 125 non-critical / 44 paper],
BLOCCATO 19 [3 critical], claims 163 [37 aperti], commit 298).
Arco di consumo: questa advisory -> sessione F2-B0 (contatore "F2 session
1/6") -> F2.REPR -> F2.ENGINE -> ... -> F3.TWIN. Autore: S-ROADMAP
(single-author; la sessione F2-B0 apre con la passata di refuter ANCHE su
questo prompt).

================================================================================
## A. APERTURA (R2 + R8, prima di qualsiasi lavoro)
R2: docs/START_HERE.md -> memoria (s-roadmap-closed, spres-session4-close,
s-genoaudit-parallel-incomplete, s25bis-speed-complete,
fservice-scert-double-session) -> M0 mirato (Parte VI + VI.4bis, Parte VII)
-> PROGRESS (ORA/NEXT/BLOCCATO tabella) -> D6 F2 :160-213 + gate table
:282-290 + Annex B :1133-1157 (lettura integrale delle righe, non grep)
-> `python tools/roadmap_derive.py` + `python tests/test_roadmap_coverage.py`
(PASS obbligatorio prima di ogni affermazione sul piano) -> dichiarare
fase F2 / passo F2-B0 / path critical.
R8 (su file, nel log di sessione, PRIMA dell'authoring): (i) consumatore =
l'orchestratore di F2.REPR/F2.ENGINE + il protocollo TWIN (persona: referee
avversario del piano); (ii) criteri d'uscita = sezione E; (iii) TETTO
d'orchestrazione dichiarato in apertura e riportato a R3 (SR-9): proposta =
max 4 agenti refuter/panel Fable, effort right-sized, artefatti su file,
resume-mai-relaunch, nessun round rituale; superamento = decisione utente.

## B. TOUCHPOINT UTENTE IN APERTURA (decisioni, non lavoro)
Presentare in una tabella e registrare la risposta in PROGRESS BLOCCATO:
 T1 Emendamento D6 per i passi F2.REPR e F3.TOURNAMENT (bozza:
    scratchpad S-ROADMAP d6_addendum_draft.md, riscrivibile dal testo dei
    findings plan:representation-ladder-... e plan:full-envelope-
    tournament-...): ratifica SI/NO/modifica -> se SI, addendum datato in
    docs/rde_nozzle_development_plan.md + override rimossi dal tool.
 T2 B-GENO: autorizzazione alla quarantena della patch audit
    (`git -C GENO checkout -- src/lib/MoC_Gen_m.f90 src/lib/Profile_m.f90`;
    patch conservata byte-identica in validation/RAW_geno_audit_
    instrumentation_2026-08-13.patch) + rebuild WSL + ri-esecuzione degli
    8 CASES/*/reference/checksums.md5 — dentro GENO, suo protocollo, suoi
    commit; un md5 che cambia = scoperta, mai bless.
 T3 Studio NASA (NASA_STUFF_Nozzle_Inlet/, Three-Dimensional-Nozzle-
    Design-Code/): atterrare (righe literature registry Kliegel-Levine
    1969 / Rice 2003 / NPAC / SUPIN + digest sotto validation/ + righe
    ADVISORY_INDEX + D6 item 12) OPPURE dichiarare esplorazione scartata
    con una riga; mai lasciare untracked.
 T4 Lean pricing + calendari ADR-D4 / estrazione P-1 (dossier di record,
    rinviati da C4 a F2-entry): decidere o rinviare con trigger.
 T5 Stray files non nostri (er.name, mailmap.txt, "t --count HEAD:q",
    literature_addition_nozzle_rde/): cancellare/ignorare/indicizzare.

## C. ORDINI DI SESSIONE (in QUEST'ORDINE; il passo 1 e' bloccante)
 1. PASSATA DI REFUTER (finding method:sroadmap-single-author-placements-
    unrefuted, path critical): (a) i 45 tag critical + campione casuale di
    30 non-critical (seme dichiarato) -> flip-or-confirm per riga con
    ancora; (b) gli 89 override + 73 OUT di tools/roadmap_derive.py ->
    ogni piazzamento confermato o spostato con ancora; (c) COMPLETENESS
    CRITIC: "quale sorgente NON e' input del join?" (candidati: claims
    THEOREM* con conditional aperte, flag_registry, literature WANTED con
    trigger, glossario duty-namespace, session-log HANDOFF blocks);
    (d) questo prompt stesso. Esito = tag flips + edit del tool +
    roadmap rigenerata + lint (xxiv) PASS + riga DISCHARGED con evidenza.
    Fino al PASS: "45 critical" NON citabile.
 2. ESECUZIONE delle decisioni T1-T5 se ratificate (T2 = unico tocco a
    GENO; conteggio md5 e fingerprint build nel log).
 3. FINESTRA ENGINE a convergenza (superficie A della decision map):
    C31 ottimizzatore A/B + [P-IPADJ] (adjudication 4bis-grade di
    trust-constr IP path), C57 tier esplorazione globale, C58 stack
    (delta-sweep 9(e) di G0 vs panorama 2026, float64 sub-asse), C60
    NAND vs SAND/LNKS, SDP-CAND-8 mint-or-retire, C32/C37 [P-QNCARRY]+
    [P-HESSREJ] unconditional. Forma: panel Form-2 con avvocato genuino
    dell'alternativa + refuter (direttiva choice-adjudication-
    convergence), input = ledger + decision map, esito = righe ledger
    DECIDED/MIXED con falsificatore e duty misurata.
 4. P0 di S-CERT residui: staleness import-closure + env fingerprint
    (audit-scert:staleness-import-closure-blind) + future-pass-dates
    (audit-scert:future-pass-dates-accepted) + h4-doctored-rejector-
    vacuous — fix in tests/test_claims_lint.py / test_ondemand_carriers.py
    con rejector seminato; carrier X-CDKAT re-stamp.
 5. O3.4 gamba gradiente (oracles:o34-gradient-leg-unconsumed): JAX grad
    vs GENO FD sulla marcia assemblata, o ri-scopo di D6 :826-830 con
    ragione dichiarata (dipende da T2 per il binario GENO).
 6. OBJ-DOM fix-A impl trigger check (variational-driver:objective-omits-
    throat-panel): il primo verdetto F2 che consuma dJ/dthB non puo'
    partire senza [OBJ-DOM-IMPL]; pinnare l'ordine con il delta-carrier
    ship-gate (E9).
 7. PROTOCOLLO TWIN PRE-REGISTRATO (deliverable di F2-B0, file in
    validation/ + riga findings/claims): configurazione (settore plug
    troncato = F3), classe dati (caso A Annex B; se caso B -> flip dei
    tag contract F2a, dichiarato), vincoli IDENTICI (eps, L, chiusura
    p_b, troncamento), rappresentazione di ENTRAMBI i bracci (=
    placeholder finche' F2.REPR non chiude — dichiarato), decision rule
    (materiale -> il metodo paga; piccolo -> la letteratura ha ragione a
    quel rango), stop ~1% Isp con banda (soglia banco di spinta 0.5-1%,
    D6 :779-782), both-outcomes pre-registrati, gate D-44 sul claim.
 8. EREDITA' S-PRES ingerita (BUILD_LOG CKP-S4-*, CONSECUTIO D4/D5,
    HARVEST H-1/H-4, finding atlas ch5-mislabel): una riga per item nel
    log, consumata o ri-owned.
 9. IGIENE F2-B0 (one-liner): i 5 owner stantii (ROADMAP §5-bis), C47
    classificazione numeric-lint (test-suite:numeric-lint-scope-hole),
    re-home H20/C61 SOLO se il touchpoint lo decide.
 10. R3 + R7: PROGRESS ORA tabella (contatore F2 session 1/6, HEAD, gate,
    BLOCKING misurate post-refuter), NEXT = F2.REPR (sessione
    topologia+modellistica, brief pronto), BLOCCATO tabella aggiornata,
    lint (vii)(xv)(xix)(xx)(xxii)(xxiii)(xxiv) verdi, suite plain quotata
    (MAI `-X utf8`), ADVISORY_INDEX righe, memoria, commit per pathspec,
    HANDOFF a F2.REPR.

## D. VINCOLI
Env pinnato (niente install/upgrade); GENO scrivibile SOLO per T2
autorizzato; Fable ovunque, mai downgrade; git add solo pathspec, mai -A,
mai GENO/; stray dirs untouched salvo T5; ogni numero da comando misurato
in finestra (SR-12); ogni orchestrazione con shape+round+token nel log
(SR-9); nessun claim "cammino completo" senza lint (xxiv) PASS.

## E. CRITERI D'USCITA (misurabili)
 E1 finding single-author-placements DISCHARGED con evidenza (flip count
    misurato: quante righe hanno cambiato tag / quanti override spostati).
 E2 lint (xxiv) PASS sulla roadmap rigenerata post-refuter; critical count
    nuovo citato come fatto di programma.
 E3 cluster engine: C31/C57/C58/C60 fuori da NEVER con verdetto datato;
    SDP-CAND-8 mint-or-retire.
 E4 protocollo TWIN pre-registrato su file, rejector nominati.
 E5 T1-T5 registrate (decise o rinviate con trigger); se T2 SI: GENO
    working tree pulito + 8 md5 riverificati nel log.
 E6 suite plain verde quotata; commit di chiusura; PROGRESS NEXT = F2.REPR.
