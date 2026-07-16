# rde-lecture-code — Istruzioni di codebase

## ⚠️ PROTOCOLLO DI ADERENZA AL PIANO (OBBLIGATORIO, da 2026-07-16) ⚠️

Il programma di ricerca "cycle-averaged variational nozzle" (branch
`rde-nozzle-program`) segue un piano a fasi con gate. Queste regole
esistono perché il filo col piano non si perda MAI e perché la teoria
si arricchisca a ogni passo invece di disperdersi.

### R1 — Nessun passo orfano
Ogni unità di lavoro (commit, analisi, doc) DICHIARA a quale fase/task
del piano appartiene (`docs/rde_nozzle_development_plan.md`, fasi
A0-A7 / task T*): tag `[F<fase>/<task>]` o riferimento esplicito nel
messaggio di commit. Se non sai in quale fase si colloca un passo,
fermati e chiediti perché lo stai facendo.

### R2 — Apertura di sessione
Prima di qualsiasi lavoro: (1) leggere la memoria di progetto;
(2) leggere `docs/rde_nozzle_MASTER.md` (M0 — riferimento di record:
in conflitto con altri doc, M0+D1-D7 vincono); (3) leggere
`docs/rde_nozzle_PROGRESS.md` (ORA/NEXT/BLOCCATO); (4) dichiarare
esplicitamente da dove si riparte e in quale fase del piano.

### R3 — Chiusura di fase e di sessione (rendicontazione obbligatoria)
A fine sessione, e SEMPRE a fine fase: aggiornare
`docs/rde_nozzle_PROGRESS.md` con ORA (stato reale: commit, test,
gate), NEXT (passo atomico successivo), BLOCCATO (decisioni/gate
esterni), e una voce di LOG (fatto / deviazioni dal piano DICHIARATE /
verdetti). La sessione N+1 deve poter ripartire leggendo solo
memoria + M0 + PROGRESS. Un lavoro lasciato a metà senza che PROGRESS
dica dove e come riprenderlo è una violazione, non una dimenticanza.

### R4 — Retro-propagazione della teoria (nessuna parte si perde)
Ogni intuizione teorica, correzione, numero-di-record o concordanza
scoperta DURANTE l'implementazione va scritta nei documenti di teoria
(M0 e/o D1-D7) NELLA STESSA SESSIONE, con classe di rigore dichiarata
(THEOREM/THEOREM*/SCHEMA/CONJECTURE/PRACTICE). I documenti di teoria
sono la sorgente del paper (P-1, venue JPP): nulla può vivere solo nel
codice, nei messaggi di commit o nella conversazione. Un commit che
tocca risultati teoricamente rilevanti senza il delta corrispondente
in M0/D-doc è INCOMPLETO. (Precedenti d'esempio: le remark EAP e S-H
in M0 Parte III; la correzione E8; i numeri del probe γ in D3 §5.2.)

### R5 — Disciplina dei numeri e dei claim (invariata, ereditata)
Nessun numero senza script committato + test; i test devono poter
RIGETTARE (rejector), non solo confermare; tolleranze derivate, non
magiche; ogni claim con ipotesi esplicite e falsificatore; claim di
novità sempre query-bounded; ogni risultato del tool nel formato
Verdict (contorno + certificati + barre + record oracoli).

### R6 — Gate
G1 (oracoli T3/T4/O3) è assoluto: nessuna "scienza" da una macchina
non certificata. G5 (passaggio umano Kraiko-1979/PMM) blocca ogni
SUBMISSION, non il lavoro. Gli altri gate (G0, G2, G3, G4, G6) come da
piano D6.

## Riferimenti canonici (ordine di lettura)
0. `docs/rde_nozzle_MASTER.md` (M0) — teoria di record, prove complete.
0b. `docs/rde_nozzle_PROGRESS.md` — stato vivente (ORA/NEXT/BLOCCATO/LOG).
1. `docs/rde_nozzle_development_plan.md` (D6) — fasi, gate, tool matrix.
2. D1-D5, D7 — profondità per argomento (mappa in M0 Parte VII).
Le note storiche (`cycle_averaged_variational_nozzle.md`,
`mathematical_foundations_rde_nozzle.md`) portano banner di
supersessione: consultabili, mai citabili contro M0.

## Preferenze
Comunicazione in italiano; codice, doc e commit in inglese. Ambiente
Python/Cantera: vedi memoria `python-env-cantera` (numpy pinnato).
Branch di lavoro: `rde-nozzle-program` (mai su main). GENO/ è un repo
git indipendente: mai aggiungerlo ai commit di questo repo.
