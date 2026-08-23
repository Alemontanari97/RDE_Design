# WA_A3 — verifica storyboard righe critic 2-3 + sweep guardie 1/2/3/6/8

Slot A3 (verifier, onda W-A), 2026-08-23. Stadio di confronto:
`STORYBOARD.md` (lettura integrale) vs `COMPLETENESS_CRITIC.md` righe 2-3
(BLOCKING) vs `ATLAS_RESEARCH_DESIGN_v2.md` §D (righe 466-467, celle N-v e
I-ii, dichiarate "GIÀ DISPOSTE dall'orchestratore — A3 verifica"). Arco di
consumo: log di chiusura onda W-A + input storyboard v3. Verifica
avversariale: le dichiarazioni dell'orchestratore trattate come claim da
confutare, non come premesse.

---

## Riga critic 2 (cella N-v) — PONTE B1, numero "4-13"

**ESITO: DISPOSTA-VERIFICATA — forma (b), kicker riformulato senza claim di
composizione.**

Evidenza (STORYBOARD.md:92-99, slide B1): il kicker recita "il campo
pubblica leve da +4-7% Isp col choking [CT-1, numeri loro] e migrazioni da
~13 punti di ideale a pari area ratio [shroud Paxson-Miki 58.1→71.5, ADV]"
con nota esplicita in slide: "[CRITIC riga 2: il composito '4-13 punti' non
aggiudicato è RIMOSSO; restano i due estremi coi loro anchor separati,
CT-6]".

Controlli eseguiti:
- Il composito "4-13" NON appare in nessun punto dello storyboard (lettura
  integrale; unica occorrenza = la nota di rimozione stessa). Nessuna
  composizione residua da aggiudicare.
- I due estremi restano ciascuno col SUO anchor: "+4-7%" → CT-1 (coperto in
  mappa, CH5 SYN per critic riga 2); "~13 punti / 58.1→71.5" → shroud
  Paxson-Miki ADV (coperto CH3:216-219 per critic riga 2; consumato anche
  da C12 con la stessa ancora e la stessa qualifica "a AREA RATIO FISSATO").
- Le due leve sono grandezze DIVERSE (Δ%Isp vs punti-di-ideale a eps
  fissato) e il kicker riformulato le tiene separate — esattamente ciò che
  la composizione "4-13" violava.
- Coerenza con §D nota [V2-R16](d) (:455-456: "resta sospeso finché la
  composizione non è aggiudicata"): la route scelta è la rimozione, non
  l'aggiudicazione — ammessa dalla disposizione critic 2 ("o riformulazione
  del kicker"). Nessun residuo sospeso.

Nessuna debolezza bloccante. Watch-point v3 (non-finding): "~13 punti" resta
un'aritmetica sui numeri loro (71.5−58.1); all'authoring la slide deve
mantenere la qualifica "dell'ideale, a pari area ratio" e il CT-6 — già
presenti nello storyboard.

## Riga critic 3 (cella I-ii) — C13, forma choice ledger

**ESITO: DISPOSTA-VERIFICATA — forma CH4 W2-R2 usata esattamente.**

Evidenza (STORYBOARD.md:369-377, slide C13): "8 stadi, 62 scelte
algoritmiche TIPIZZATE a registro — 48 aggiudicate a convergenza con
alternative pesate + falsificatore, 2 SINGLE-AUTHOR dichiarate (C17/C18,
duty F2), 12 NEVER dichiarate con owner e trigger" + tally on-slide
"12 DECIDED / 36 MIXED / 12 NEVER / 2 SA" + nota "[CRITIC riga 3 applicata:
coerenza con CH4 W2-R2]".

Controlli eseguiti:
- La forma richiesta ("62 TIPIZZATE, 48 aggiudicate") è quella usata,
  verbatim nella sostanza; il verbo incriminato ("62 ADJUDICATE") è assente.
- Aritmetica interna coerente: 48 + 2 SA + 12 NEVER = 62; tally
  12+36+12+2 = 62; 12 DECIDED + 36 MIXED = 48 aggiudicate. L'incoerenza
  interna denunciata dal critic (62-aggiudicate vs tally) è sanata.
- Nessun conteggio vecchio o non qualificato altrove: sweep dello storyboard
  per altre occorrenze del ledger (C13-pre rimanda al ledger come ancora dei
  perché; C14 dichiara il cluster F2-entry APERTO) — nessuna riga reintroduce
  "62 aggiudicate" né conteggi divergenti.

---

## Sweep guardie 1/2/3/6/8 (GUARD_CHECKLIST.md) sullo storyboard

Metodo: camminata integrale slide-per-slide, riporto HIT/CLEAN; borderline
elencati come input v3, non riparati.

| guardia | esito | dettaglio |
|---|---|---|
| 1 (gerarchia C-3bis mai senza tallone (J)) | CLEAN | La gerarchia (A)>(B) NON è mai enunciata nello storyboard: C7-bis e C17 dicono solo "Gap B misurabile in-house / Gap A bounded-only" (STORYBOARD.md:224-227, 398-401) senza ordinamento di grandezza; il canale (J) compare in C10 con deriver nominati (:325-326). Watch-point authoring: se in sala il confronto Gap A/Gap B scivola in un ordinamento, il tallone (J) va detto. |
| 2 (non-sequitur T1c bandito) | CLEAN, 1 borderline | C7-ter inserto (:273-280): T1c riqualificato al suo rango con disclaimer STAMPATO "mai presentato come la prova del confronto di formulazione" — conforme. Borderline da sorvegliare in v3/authoring: lo stesso inserto aggancia T1c al "pattern 'argmax mobile a valore piatto' di Humphreys e P-B"; l'analogia deve restare a livello di pattern (fragilità dell'argmax), mai diventare evidenza del gap di contouring vincolato. |
| 3 (rung quasi-1D mai "1-DOF nozzle case") | CLEAN, 1 borderline | C7-ter riga (1) (:234-240) è ESEMPLARE: "l'oracolo eseguibile... la parete non è variabile, conta solo l'area ε — NON è un ugello alla Rao" con la precisazione utente incorporata. Borderline: C7-bis-pre (:203-205) "Il nostro rung-1 quasi-1D È il livello Stechmann" — Stechmann valuta FAMIGLIE di ugelli fisse (bell vs aerospike): l'equazione "rung-1 = livello Stechmann" rischia di ripresentare il rung come caso-di-valutazione-ugello; in v3 precisare "è il livello di RIDUZIONE di Stechmann (0-D per-fase), non una valutazione di famiglie d'ugello". |
| 6 (D-44: mai adequacy per contour ranking) | CLEAN | C11 porta la guardia on-slide ("[D-44: bracket, MAI adequacy]", :335-336); C7 tiene Level-2 ranking "OPEN, R26" (:187-188); C9 "ESONERATA" è scoped all'asse-fibra con classe THEOREM* (:317-321), non un claim di adequacy per ranking. Nessuna cella sopra la sua classe trovata. |
| 8 (best-of-sweep ≠ argmax) | CLEAN | La guardia è citata on-slide in C3 TAKEAWAY (:125-126, applicata al campo). I nostri claim d'ottimo portano il meccanismo dichiarato: C8-bis "OTTIMO GLOBALE = torneo FINITO... cross-sector licenziato dal geometry-free bound" + verdetto rung-ridotto a classe THEOREM con carrier X-GRP10/12 (:302-310); C16 = numeri di velocità, non ottimi. Nessun numero di campagna presentato come ottimo globale non meccanizzato. |

**Conteggio violazioni: 0 HIT netti; 2 borderline (guardie 2 e 3) come
input storyboard v3.** Nota fuori-mandato (già nota al critic, righe 4/8:
la sorgente CH8 §1.7 della guardia 8 e la fase F3 per C17 sono in scrittura
W-B.1 — le slide C13/C17 ne dipendono per il retro-audit del Blocco 2).

## VERDETTO A3

Riga critic 2: **DISPOSTA-VERIFICATA** (forma (b) — composito rimosso,
estremi separati con anchor). Riga critic 3: **DISPOSTA-VERIFICATA** (forma
CH4 W2-R2 esatta, aritmetica coerente). La dichiarazione "GIÀ DISPOSTE
dall'orchestratore" di §D è **VERA** per entrambe. Guardie 1/2/3/6/8:
0 violazioni, 2 borderline nominati.
