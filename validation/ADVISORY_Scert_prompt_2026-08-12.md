# PROMPT DI SESSIONE — S-CERT "AUDIT DI CERTIFICAZIONE AGNOSTICO"
# (scritto 2026-08-12 alla coda di S25-bis; RATIFICATO dall'utente;
# censimento R33; collocazione di record: DOPO S-ORDINE (R32),
# PRIMA dell'apertura F2. La certificabilita' non si dichiara: SI
# MISURA con auditor ostili e privi di contesto.)

Sei nel repo rde-lecture-code, branch rde-nozzle-program. Verifica
HEAD (git log -3, tag attesi [F-SERVICE/*]); commit non tuoi =
FERMATI. GENO/ read-only, mai committato da qui. Suite/lint gated
su EXIT CODE, redirect-only; FREEZE edit durante consumer run.

QUESTA SESSIONE E' LA S-CERT. Obiettivo (ordine utente 2026-08-12):
misurare se la codebase e' "SOTA pressoche' totale e CERTIFICABILE
IN MODO AGNOSTICO" — cioe' se un estraneo ostile, dai soli
artefatti, puo' ri-verificare le claim e non riesce a falsificare
le meta-claim di certificazione. Precedente di forma:
AUDIT_agnostic_2026-08-07 (94 finding, find->verify Form 1) +
direttiva standing agnostic-milestone-review. QUESTA E' UNA
SESSIONE DI AUDIT: i finding atterrano con triage e owner; le
riparazioni NON si eseguono qui (salvo typo-class dichiarata).

## (1) APERTURA (R2)
Memorie: agnostic-milestone-review-directive,
agentic-orchestration-forms, orchestration-weight-sota,
s25bis-speed-complete; PROGRESS ORA + censimento (R32 consumata?
— se S-ORDINE non e' CHIUSA, questa sessione NON parte: l'audit
misura anche l'ordine); docs/findings_registry.yaml +
docs/claims_registry.yaml (le superfici d'audit); QUESTO prompt.
Gate pre-esecuzione con verdetto loggato.

## (2) IL PRINCIPIO DI AGNOSTICITA' (vincolante sui brief)
Gli auditor NON ricevono narrativa difensiva del progetto: il brief
da' SOLO (a) il perimetro repo, (b) le META-CLAIM da attaccare
(sotto), (c) lo schema di output. Possono leggere TUTTO (il corpus
E' la superficie), ma il loro default e' ostile: una claim e'
falsa finche' l'artefatto non la regge. Nessun auditor riceve i
verdetti delle sessioni come autorita' — solo come oggetti da
verificare.

## (3) LE META-CLAIM DI CERTIFICAZIONE SOTTO ATTACCO
MC1 "Ogni numero di record ha un carrier committato eseguibile"
    (R5): campiona numeri dai doc OF-RECORD -> traccia al carrier
    -> ESEGUI il carrier -> il numero si riproduce?
MC2 "Ogni tolleranza e' derivata, non magica": campiona bande ->
    ri-deriva dalla derivazione dichiarata -> coincide? (i lint
    numeric/ratchet girano e i loro rejector sparano?)
MC3 "Ogni claim ha un falsificatore che PUO' sparare": campiona
    claim/rejector -> esegui i rejector seminati -> sparano tutti?
MC4 "I registry sono completi e anti-re-mint": cerca finding in
    prosa NON a registro (post seeding S-ORDINE questo e'
    testabile); prova a costruire un re-mint che il lint non becca.
MC5 "La suite copre cio' che dichiara": mappa gruppi->claim; trova
    claim di copertura vacue; staleness/ondemand onesti?
MC6 "Un estraneo NAVIGA il progetto" (misura anche S-ORDINE): 10
    domande standard (dov'e' la prova di X? che status ha Y? dove
    si ri-esegue Z?) risolte da un agente context-free usando SOLO
    indici/registri/glossario — tempo e successo misurati.
MC7 "Le catene di provenienza reggono": per 5 verdetti storici
    campionati, risali sessione->commit->carrier->artifact senza
    buchi.
MC8 "OGNI RAMIFICAZIONE ALGORITMICA RISPONDE A UN'ESIGENZA PRECISA
    DEL PIANO" (lente primaria, ordine utente 2026-08-12 — R1
    elevata a meta-claim di sistema): campiona N leve/moduli/
    formulazioni -> per ciascuna traccia (i) l'esigenza del piano
    che la richiede (fase D6 / riga censimento / riga registry),
    (ii) la sua adjudication SOTA ai TRE livelli — algoritmico
    (alternative battute o registrate), fisico (l'ipotesi/regime
    che la giustifica), implementativo (gate + refuter + review);
    una ramificazione senza esigenza nominata o senza adjudication
    ai tre livelli = finding (orfano di sistema / SOTA non
    dimostrato), mai assorbito in silenzio.

## (4) IL WORKFLOW (find->verify Form 1, ~15-20 agenti)
FASE A — CAMPIONAMENTO STRATIFICATO (1 agente + tu): dalle
superfici (claims registry ~136, findings ~21+, gate [X-SPDB],
contatori speed, teoria M0 classi THEOREM/SCHEMA/CONJECTURE)
estrai il campione (15-25 claim full re-verification + i 7 attacchi
MC) con seme dichiarato e strati dichiarati (mai cherry-pick).
FASE B — AUDITOR PARALLELI per strato (effort medio/alto, brief
agnostici): ognuno attacca il suo campione + la sua MC; max-N
finding con drop dichiarati; ogni claim di difetto con evidenza
file:line + comando riprodotto.
FASE C — VERIFIER AVVERSARI (uno per auditor, default-REFUTE dei
finding: un finding sopravvive solo se il verifier non lo abbatte
sulle sorgenti).
FASE D — SINTESI + TRIAGE (P0/P1/P2, owner per riga) -> JUDGE ->
Form-3 RED-TEAM sul judge PRIMA dell'assorbimento.
Artefatti su file (validation/scert_raws_<data>/), full-text (path
mai slice), dedup contro i registry, peso riportato (shape+token).

## (5) VERDETTO DI SESSIONE (formato vincolante)
UNA riga di record: "CERTIFICABILE-CON-RESIDUI (N righe triaged,
tutte con owner)" oppure "NON-CERTIFICABILE (le M righe P0 che lo
bloccano)". Piu': il delta vs l'audit 2026-08-07 (righe chiuse/
aperte/nuove — la misura se il livello e' salito). Ogni residuo =
riga findings registry (mai prosa). Chiusura R3: censimento R33
consumata, NEXT = F2 (blocco 0: decisioni utente filelock/O5/M6 +
re-chain; poi il motore generale).

## TERMS
Sola lettura sul codice (audit, non repair); verdetti S14-S25bis
non rilitigati MA ri-verificabili (l'audit puo' scoprire che una
verifica non regge: quello e' un finding, non una rilitigazione);
R4/R5 vigenti; italiano chat, inglese doc/commit; chiusura R3
obbligatoria.
