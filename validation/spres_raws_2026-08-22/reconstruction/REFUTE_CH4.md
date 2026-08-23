# REFUTE_CH4 — verdetto refuter su CH4 (La macchina e le scelte)

[S-PRES refuter pass, 2026-08-23. Mandato: anchor walk 100% dei claim
load-bearing + banco utente (4 domande) + buchi + overclaim scan.
Metodo: read-then-quote — ogni ancora citata dal capitolo APERTA in
finestra e confrontata alla classe dichiarata. File letti:
`docs/rde_nozzle_pipeline_decision_map.md` (integrale :1-339),
`docs/rde_nozzle_G0_decision.md` (:1-210),
`docs/choice_ledger.yaml` (righe C1-C31, C49, C55-C59 + conteggio
`grep -c "^- id: C"` = 62 misurato in questa finestra, SR-12),
`docs/rde_nozzle_PROGRESS.md` (:110-219),
`docs/literature_registry.yaml` (:368-382),
`docs/rde_nozzle_MASTER.md` (:3645-3704, blocco NTF [LAND-C4-LA2]),
memorie `s18-brick2-closed`, `moc-critical-independent-invariants`,
`s-genoaudit-parallel-incomplete`; esistenza
`validation/PROGRESS_2026-08-06_S18_brick2run.md` verificata su disco.]

## Esito dell'anchor walk (positivo, di record)

I numeri portanti REGGONO tutti alla classe dichiarata: 8 stadi / 79
nodi / 45 voci-arco / 4 superfici / tally 12-36-12-2 (mappa :33-36,
:262-309, riconcilia YES); refuter mappa 0/0/5/4 (:317-339); 52/52 +
controllo negativo (G0 :33-38); X-GENOXC 218/218 + controlli negativi
1%→0% e 84x (G0 :94-104); T1 1.593 / T2a 0.116 ≤ 1.197 (G0 :160-171);
KKT 7.745e-02 ≤ 1.156e-01, 91/91, max|dy| 1.86e-03, J* 2.7761688e+07,
4 tentativi (memoria s18 :27-39); velocità MET e catena 100.84→32.09→
5.58 / replay 0.236 / val_grad 0.449 / Hessiana 4.5-7.0 (PROGRESS
:119-125); floor cross-lowering ~1e-8 + disciplina una-lowering
(PROGRESS :130-154); GAP-29 NTF/2 flip + C_FLOOR/2, C_OPS/2 no-flip
≥2x headroom (PROGRESS :155-158; ledger C18 nota — la formulazione
del capitolo §1.3(g) è ESATTA sul ledger); blocco NTF con classi
THEOREM*/SCHEMA/PRACTICE come stampate (M0:3649 ff. + mappa :109);
S-CERT NON-CERTIFICABILE 2 P0, difetti migrati oggetto→certificatore,
MC8 8/8 (PROGRESS :211); C49 0-finding-refuter (ledger :692); C56
Hicken-Zingg p.164 + blind spot wrong-branch (ledger :769); Hoffman
1967 READ-INTEGRAL, Eq. (78) = certificato VI.3 (lit registry
:372-378); C55/C59 "question EMPTY" verbatim (mappa :66, :78); regola
"nessuna fase apre con NEVER sui componenti che consuma" (PROGRESS
:213). Nessun BREAK: nessun claim cade.

## Finding

| # | sito (riga capitolo) | classe | severità | testo | fix proposto |
|---|---|---|---|---|---|
| 1 | :289-290 (§1.4 gate di produzione) | REPAIR | MEDIA | "T2a clean-host 0.116 s vs 4×0.286 s GENO = PASS" mescola due misure: 0.286 s è il t_GENO della nota S17 (G0 :148, run FAIL-as-implemented); la re-run S18 che dà il PASS misura t_GENO 0.299 s, soglia 4×0.299 = 1.197 s (G0 :167-169). Il capitolo stesso usa 1.197 nel claim 4 — internamente incoerente. | Scrivere "0.116 s ≤ 4×0.299 s = 1.197 s (G0 §4 nota S18)". |
| 2 | :446-448 (Q3, chiusa) | REPAIR | MEDIA | "la domanda onesta è… perché le altre 50 sono pesate — e la risposta è… 3 wave, 0 righe cassate". Delle 50 non-NEVER, 2 sono SINGLE-AUTHOR (C17/C18): il ledger dice esplicitamente "no derivation or panel adjudication of N_NEWTON found" (C17 nota :342) e C18 "derivation itself still NEVER done → status stays SINGLE-AUTHOR" (:353). Dire "50 pesate" al banco è sopra-record e un reviewer col ledger in mano lo vede. Inoltre "0 righe cassate" comprime "0 break / 0 refuter cassati" (PROGRESS :213) — difendibile ma da citare come sta. | "…perché 48 sono aggiudicate a convergenza (3 wave con refuter, 0 break) e le 2 SINGLE-AUTHOR restano dichiarate con duty F2 — anche quel numero è tipizzato". |
| 3 | :393-406 (Q1, metà TR-Newton) | REPAIR | MEDIA | La risposta anti-BFGS suona come chiusura definitiva ("la curvatura accumulata… non fa in tempo a formarsi"), ma il record tiene il quasi-Newton VIVO: C32 porta il challenger pinnato [P-QNCARRY] che entra UNCONDITIONAL a F2-entry (mappa :142 "F2 entry gains [P-QNCARRY]+[P-HESSREJ] (unconditional)"; C37 nota "the [P-QNCARRY] arm-B pin stands", E46). Un panelist che chieda "quindi il quasi-Newton è escluso per sempre?" riceverebbe dal deck una risposta più forte del record. | Aggiungere una frase: "il carry quasi-Newton non è morto: è un challenger pinnato ([P-QNCARRY]) che si misura a F2-entry — la scelta attuale è su numeri di QUESTO problema, non un dogma". |
| 4 | :473-475 (Q5, residuo GENO) | REPAIR | MEDIA | Due difetti: (a) "detto, con owner" — la memoria genoaudit NON nomina un owner/trigger di record per il completamento ("prima o poi va portata a completamento"; R13 in PROGRESS :191 copre solo md5-freeze/N-74/knob, trigger "prossima sessione GENO/s3"); (b) la risposta tace i due esiti sostanziali che il panel userebbe: l'accordo Ch.16≡Ch.17 è VACUO sul rotazionale (chiusura a un parametro, h0/s0 globali) e il ramo cross-stream mai esercitato — MA anche il positivo: unit process gemellati ESATTI vs Zucrow, Sauer book-exact, BC parete dimostrata (memoria genoaudit §2, §1). | Togliere "con owner" (o ancorare esplicitamente a R13 per la sola parte md5/strumentazione) e citare entrambe le metà: "l'audit parziale ha PROVATO esatti i processi unitari gemellati e ha mostrato che l'accordo tra i due backend GENO è vacuo sull'asse rotazionale — un motivo in più per cui i nostri oracoli decisivi sono GENO-indipendenti". |
| 5 | :480 (Q6) | REPAIR | BASSA | "(grad/solve ~1.5%, T1 ≤ 4)": 1.5% è l'OVERHEAD dell'adjoint; il RATIO grad/solve è ~1.01 a livello unit-process (G0 :53-58) e 1.593 a scala engine. Il §5 punto 3 usa l'etichetta giusta ("overhead ~1.5%"); qui è sbagliata. | "(overhead adjoint ~1.5%, ratio grad/solve 1.593 ≤ 4)". |
| 6 | :109-115, :493-494 (§1.3(a) e slide 1-4) | GAP | MEDIA | X-GENOXC 218/218 è presentato senza il confine di scope che G0 dichiara apposta "to prevent over-reading" (G0 :202-210): certifica il PROCESSO UNITARIO interno nel core supersonico pulito, NON la macchina di generazione profili; a G0 non esisteva marcia JAX assemblata. La copertura assemblata arriva solo con il 91/91 di S18. Su slide, un esperto che legga "218/218 cross-code" come validazione full-field la smonta con il documento nostro. | Una riga di scope accanto al 218/218: "a livello di processo unitario (il mattone differenziabile); il livello assemblato è coperto dall'oracolo 91/91 del run S18". |
| 7 | :277, :345 (J* citato) | GAP | MEDIA | J* = 2.7761688e+07 citato due volte senza dire COSA è J (funzionale di cosa? unità?). "2.78e7 di che cosa?" è la prima domanda di un panelist ostile davanti a quel numero. Se la definizione vive in CH1-CH3 serve il cross-ref esplicito; il capitolo da solo non risponde. | Cross-ref esplicito al capitolo che definisce il funzionale (o una parentesi "J = <definizione di record>, unità"); in mancanza, dichiarare OPEN il rimando. |
| 8 | :113 (prima occorrenza GENO) | GAP | BASSA | GENO compare in §1.3(a) senza definizione; per il panel ESA (nulla di scontato, da mandato S-PRES) serve una riga alla prima occorrenza. La spiegazione implicita arriva solo in Q5. | Alla prima occorrenza: "GENO = il codice MoC Fortran di riferimento del gruppo (repo indipendente, mai assunto bug-free)". |
| 9 | :344-345 (tabella claim 5-6) | NOTE | BASSA | Le ancore di record dei claim 5-6 sono SOLO la memoria `s18-brick2-closed` — che porta essa stessa il banner "point-in-time… verify against current code". Il carrier committato esiste: `validation/PROGRESS_2026-08-06_S18_brick2run.md` (verificato su disco), nominato dalla memoria stessa. | Aggiungere il log committato come ancora primaria, memoria come indice. |
| 10 | :268 (§1.4, P34) | NOTE | BASSA | "(1 dei 2 gap FORK-141 genuini)": come appartenenza è vero, ma come ordinale è falso — la mappa (PM-6, :332) fissa H20 = 1 of 2 (:2521) e P34 = 2 of 2 (:2530). La frase com'è può essere letta nell'ordine sbagliato appena corretto da un refuter. | "uno dei due gap FORK-141 genuini (l'altro è H20)". |
| 11 | :143-145 (§1.3(b)) | NOTE | BASSA | "a weight cannot referee itself" è attribuito a "(ledger C56…)"; la frase verbatim vive nella nota C11 (:279) / supplemento §4.2, non nella riga C56. Il supplemento è co-citato, quindi la sostanza regge; l'attribuzione va precisata. | Spostare l'attribuzione su "ledger C11 nota / supplemento §4.2". |
| 12 | :509-514 (slide onestà) | NOTE | BASSA | La slide-onestà usa S-CERT; il record contiene una seconda istanza della stessa tesi che un reviewer che scavi G0 troverà comunque: il LEDGER TRUTH REPAIR S25 (la riga "67 evals" di S18 dichiarata untruthful e ripricing [X-TOCV] di record, G0 :177-198). O si usa come secondo esempio ("il sistema corregge anche i nostri conteggi"), o si sta pronti alla domanda in Q&A bank. | Aggiungere alla banca Q&A: "avete mai pubblicato un numero poi risultato falso?" → risposta dal record G0 :177-198. |

## Banco utente — giudizio per domanda

- **Q1 (TR-Newton/fiducia)**: regge nel merito, non evasiva, ancore
  vere; incompleta sul challenger quasi-Newton vivo (finding 3).
- **Q2 (cos'è/cosa non certifica)**: la risposta MIGLIORE del
  capitolo — 5 non-coperture tutte verificate alle ancore (C57 :138,
  D-44 :180, C56 :769, C20 :365-376, C19 :363). REGGE senza riparazioni.
- **Q3 (12 NEVER)**: struttura della risposta corretta e ancorata
  (:296-309, :66, :78, PROGRESS :213); la chiusa "50 pesate" è
  l'unico punto sopra-record (finding 2).
- **Q4 (adjoint discreto vs continuo)**: onesta e alla classe giusta —
  distingue esattezza-al-discreto (fatto, 52/52) da dual-consistency
  (SCHEMA + F11d mai eseguito), cita la ragione pubblicata Hicken-Zingg
  per cui il check non si condona. REGGE senza riparazioni. È il
  modello di come vanno scritte le altre.

## Overclaim scan

Nessun superlativo non ancorato; nessun claim di novità (nessuno
richiesto: capitolo cite-only); tutti i numeri portano carrier o
comando misurato; CT-6 rispettato (Hoffman/Hicken-Zingg/Masters citati
come loro). Gli unici numeri difettosi sono i finding 1 e 5 (misure
nostre mal accoppiate/etichettate, non bande inventate).

## VERDETTO

**REGGE-CON-RIPARAZIONI.**
Conteggio: **0 BREAK / 5 REPAIR / 3 GAP / 4 NOTE** (12 finding totali;
0 DOWNGRADE — le classi dichiarate reggono ovunque alle ancore).

Riparazioni più urgenti: (1) finding 2 — Q3 "50 pesate" → "48
aggiudicate + 2 SINGLE-AUTHOR dichiarate" (è la risposta che finisce
al banco, e il ledger la smentisce com'è); (2) finding 1 — la coppia
0.116/0.286 nel gate di produzione va riallineata alla misura S18
(0.299 → 1.197), perché è un numero da slide internamente incoerente
col claim 4 dello stesso capitolo.
