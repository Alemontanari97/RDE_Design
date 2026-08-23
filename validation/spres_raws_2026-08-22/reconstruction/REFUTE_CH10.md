# REFUTE_CH10 — refutazione avversaria di CH10_data_contract.md

Slot C2 (refuter, giudizio), onda W-C.a, 2026-08-23. Oggetto:
`validation/spres_raws_2026-08-22/reconstruction/CH10_data_contract.md`
(capitolo NUOVO, nodo N-K, con integrazione guardia 17). **§6 STORIA
IGNORATA** (placeholder W-B.2; refuter C5 dopo). Campione: 100% delle
righe load-bearing (tutte le sezioni 1, 2, 3, 3-bis, 4, 5, 7, 8, DECK
FEED). Metodo: ogni ancora aperta alla fonte (read-then-quote); grep
chiave RIESEGUITI in finestra (C-SBVF repo-wide; Gelb/Tadmor/Paciorri
su literature_registry; line-numbers choice/findings ledger; verbatim
C-1bis e pin CKP-S2-1 confrontati carattere-per-carattere via script).
Scope: nessuna crescita oltre il brief.

## Verifiche meccaniche eseguite (comandi in finestra)

1. Verbatim C-1bis (guardia 11): script Python di confronto substring
   normalizzato (whitespace/hyphenation) tra i 3 blocchi citati in CH10
   e `SESSION_STATE_checkpoint.md:146-165` → **3/3 VERBATIM ESATTI**
   (head :146-153; closing argument :154-158; PRECISION :158-163).
2. Pin guardia 17: la stringa utente *"ci dovrebbe essere solo se la
   porzione pre gola è convergente e con gola tutta sonica o
   supersonica, o se la gola, anche throatless geometrica, è a patch
   subsoniche"* è VERBATIM in `SESSION2_LOG.md` (CKP-S2-1, :98-102) e
   compare 2 volte in CH10 (§1.2, Q7), entrambe esatte.
3. `grep -rn "C-SBVF" docs/ validation/spres_raws_2026-08-22/` →
   **unica occorrenza = CH10:134** (vedi F2).
4. `grep -in "gelb|tadmor|paciorri|bonfiglioli" docs/literature_registry.yaml`
   → solo :1142-1143 (`wanted_onofri_paciorri_2017_book`): l'eccezione
   A4 di CH10 §2b/§7(a) è CONFERMATA alla fonte (emendamento v2.1 §6b).
5. `grep -n "^- id: C50|^- id: C52|^- id: C53" docs/choice_ledger.yaml`
   → 694 / 716 / 726 (vedi F3).
6. `grep -in "adequac|adeguatezza" CH10` → 0 hit (guardia 6);
   `grep -in "two-stage|1450" CH10` → 0 hit (guardia 12).
7. Ancore M0 (:116-124, :125-138, :139-166, :977-1008, :1030,
   :1086-1103, :1184-1224, :3049-3099), D6 (:174-202, :256-267, :285-290,
   :808-815, :1132-1157), problem book :298-323, conditionals :1-60,
   findings :1661/:2317/:2530, theorem ledger :228-240,
   THROAT_FIELD_HARVEST :270-296/:395-410/:565-580/:605-615/:683-690/
   :758-768, LINEAGE_LEDGER (integrale), CH5 :1-55, design v2 :83/:130-136/
   :279-281/:359/:544, emendamento v2.1 §1g/GV-2/§5-bis/§6b — tutte
   aperte e confrontate.

---

## FINDINGS

**F1 — REPAIR — righe 275-281 (§3.2), 345-353 (§4.5), 374-376 (§5),
557-565 (Q5), 618-623 (DECK FEED 5) — [T-DISC] presentato SOPRA
l'ancora (classi e attribuzione delle conseguenze).**
Claim di CH10: "[T-DISC-1]/[T-DISC-2] dimostrano che la fibra … è
non-degenere e J-separante: due dataset con la STESSA P(theta) e
contenuto full-state diverso producono ottimi diversi" (§3.2); "
Dimostrato: … [T-DISC] 1/2/3" (§5); "Classe: THEOREM (scope classe A
dichiarato)" (DECK FEED 5); "due motori con la stessa traccia di
pressione e swirl/h0 diversi hanno ottimi diversi" (Q5).
Evidenza alla fonte (`docs/rde_nozzle_MASTER.md`):
(a) [T-DISC-1] è **THEOREM\*** ("conditionals inherited and named
below", :1031); (b) [T-DISC-2] è **split-grade, declared per leg** —
il sign leg è THEOREM\* **SCOPED, BOOKING level under H2.2, su
confronti PHYSICAL-h0-FIXED** (:1086-1098), col ramo uncompensated-DROP
**geometry-signed a separazione ZERO nel corner degenere** (nessun
floor positivo asserito, :1194-1198); (c) la conseguenza "ottimi
diversi" è [T-DISC-3], che è **SCHEMA** (:1184-1185) e nella gamba (b)
richiede la premessa **(DR) design-realizability NAMED, "checked per
family at M-RED time"** (:1210-1216). Quindi: "ottimi diversi"
attribuito a T-DISC-1/2 = attribuzione sbagliata; "Dimostrato …
1/2/3" e "Classe: THEOREM" = classe sopra l'ancora (T-DISC-3 è
SCHEMA); Q5 "swirl/h0 diversi" contraddice il sign leg (h0-trace
FISSA nel confronto) e il pin [REV2-r1-1] (la fibra calibrated-scalars
fissa anche le mu-medie: ciò che varia è contenuto di
fluttuazione+swirl, :1010-1020).
Riparazione proposta: dichiarare i gradi per gamba (THEOREM\* /
split-grade / SCHEMA) in §4.5 e §5; attribuire "ottimi diversi" a
[T-DISC-3](b) con (DR) nominata; riformulare Q5 ("stessa traccia di
pressione e stesse medie di ciclo, contenuto di fluttuazione/swirl
diverso ⇒ J diversi per [T-DISC-1]+[T-DISC-2](i) dove il confronto
physical-h0-fixed è ammissibile; sull'ottimizzazione, [T-DISC-3](b),
SCHEMA con premessa (DR)"); DECK FEED 5 classe → "THEOREM\*/SCHEMA per
gamba, scope classe A". La sostanza dell'argomento di chiusura REGGE
(la proiezione perde informazione J-rilevante per teorema, dentro lo
scope): è la CLASSE che va giù di un gradino, non il claim.
NB: il verbatim del checkpoint ("T-DISC CONVICTS") resta citabile
com'è — è la prosa NON-quote di CH10 che deve portare i gradi.

**F2 — REPAIR — righe 131-137 (§1.4) — condizionale analitico
"C-SBVF" INESISTENTE.**
Claim: "i condizionali analitici (C-D25U …; C-SBVF) — enunciati UNA
volta nel ledger". Evidenza: `grep -rn "C-SBVF" docs/ validation/spres_raws_2026-08-22/`
→ unica occorrenza = CH10 stesso. Il ledger
(`docs/rde_nozzle_conditionals.md`) enuncia DUE condizionali
analitici: **C-D25U** (:18) e **C-MAJDA** (:77) — nessun C-SBVF in
alcun registro. Riparazione: C-SBVF → C-MAJDA (o rimozione del secondo
nome se fuori-nodo). Id inesistente presentato come contenuto di
ledger = violazione navigation-first; riparazione a una parola.

**F3 — REPAIR — righe 443 (card C52 campo 1), 464 (card C53 campo 1)
— anchor di riga ERRATI sul choice ledger.**
CH10 cita C52 = `docs/choice_ledger.yaml:726` e C53 = `:737`.
Misurato in finestra: **C52 = :716, C53 = :726** (C50 = :694 è
corretto). Così come scritti, l'anchor di C52 punta alla riga di C53 e
quello di C53 dentro/oltre C53. Contenuto delle card (id, alternative,
status NEVER, evidence #D-1/#D-2, finestre F2) VERIFICATO ESATTO al
ledger; solo i numeri di riga sono sbagliati.

**F4 — REPAIR — righe 125-127 (§1.3) — anchor errato per l'invariante
Annex B.**
Claim: "'a generator emitting off-manifold data is a generator bug'
(`docs/rde_nozzle_development_plan.md:1155-1157`)". Misurato: la frase
è a **:1150-1151** ("stage-A audits apply to GENERATED data too (a
generator emitting off-manifold data is a generator bug)"); :1155-1157
è il build-status dei casi. Citazione verbatim corretta, anchor da
spostare. (Nota minore collegata: Annex B termina a :1157; i puntatori
":1132-1160" di Q1/DECK FEED 1 sovra-spannano di 3 righe, innocuo.)

**F5 — REPAIR — righe 96-105 (§1.2) — guardia 17: il grassetto
"decoupling ⇔ choking pieno" SOVRA-ESTENDE il pin (da "solo se" a
biconditional).**
Il pin utente (CKP-S2-1, verbatim verificato) e la guardia 17 danno:
(i) decoupling asseribile **SOLO SE** choking pieno (necessità della
condizione per il claim); (ii) patch subsoniche ⇒ feedback ESISTE.
Nessuna delle due dà la SUFFICIENZA (choking pieno ⇒ decoupling) come
pin; la direzione di sufficienza esiste nel record solo al livello
MEDIO e sulla classe: [T-NSW] esclude l'influenza **media** a monte su
L4-DEFAULT (M0 :128-130), lettura a piccole perturbazioni. CH10 lo
qualifica subito dopo il grassetto ("[T-NSW] esclude l'influenza media
a monte esattamente su quella classe") — ma il formulone "**decoupling
⇔ choking pieno**" è esattamente la stringa che finirà on-slide, e in
quella forma il pin interpretativo è trasformato in equivalenza.
Riparazione: "decoupling ⇒ choking pieno (condizione di ammissibilità
del claim; il feedback c'è con patch subsoniche); la direzione inversa
vale al livello MEDIO su L4-DEFAULT per [T-NSW]" — due direzioni
separate, gradi dichiarati. Il RESTO del cablaggio guardia 17 è
FEDELE: verbatim esatto (2/2), pre-gola convergente presente,
"lungo ciclo e azimut" dalla lettura di record, throatless-geometrica
resa, confine unstart dichiarato (§1.2 e Q7), O1-O4 coerente; Q7 usa
correttamente la sola forma "asseribile SOLO sotto".

**F6 — NOTE — righe 384-389 (§5, aperto U3') — "la premessa SCOPERTA
di U3' è esattamente il choking pieno": "esattamente" sovra-stringe.**
D6 :191-202 dà come premessa di U3 la "per-phase axially-supersonic
surface downstream of the throat"; il "choking pieno" della guardia 17
include ANCHE la pre-gola convergente, e U3' possiede anche corrector
e monitor eseguibile. L'identificazione è dichiarata interpretativa
("In termini della regola di interpretazione") e quindi ammissibile,
ma "esattamente" andrebbe ammorbidito ("la premessa scoperta di U3' è
la metà gola/superficie-sonica del choking pieno").

**F7 — NOTE — righe 70-74 (§1.2, ancoraggio 2) — citazione CUCITA
dall'harvest.**
CH10 virgoletta come stringa unica *"corrugated sonic line: axial
Mach 0.85 → 1.33, crossing M=1 TWICE per cycle"*. L'harvest
(`THROAT_FIELD_HARVEST_c4.md:399-404`) ha DUE frammenti distinti:
"corrugated sonic line: axial Mach 0.85 -> 1.33 across circumference"
e "the sonic line is crossed TWICE per cycle". Contenuto fedele, forma
non verbatim: marcare come parafrasi o citare i due frammenti.

**F8 — NOTE (= HIT guardia 13) — righe 194-201 (§2a), 300 (LL-6),
564 (Q5) — "30→2atm" fuori-quote vs harvest di record; caveat CT-6
assente alla prima occorrenza.**
Fuori dalle citazioni del checkpoint, CH10 ripete "30→2atm" (LL-6;
Q5 "30→2 atm … numeri di harroun_2021"). L'harvest di record dà
"log-decay sawtooth, **30 -> ~2-6 atm** per 180-deg sector" (S1 :608;
anche :296). Il "2 atm" secco è la compressione del checkpoint, non il
numero dell'harvest. Inoltre la PRIMA occorrenza dei numeri Harroun
(§2a righe 194-201) porta la citazione ma non il caveat di
non-riproduzione (arriva solo in Q5 e DECK FEED 4). Riparazione:
"30→~2-6 atm" nelle occorrenze non-quote + caveat CT-6 alla prima
occorrenza (o nota CT-6 a livello di capitolo).

**F9 — REPAIR — righe 472-477 (card C53, campo 4) — violazione
GV-2: il campo 4 non CHIUDE col token canonico.**
GV-2 (emendamento v2.1 §1g): "il campo 4 deve chiudere con UNO dei due
token canonici". Nella card C53 dopo "**ATTUALE(perimetro: …,
data-check 2026-08-23)**" segue la "Nota harvest a favore della futura
aggiudicazione…": il lint 8 (copertura TOTALE, grep sui token) può
firare. Riparazione: spostare la nota fuori dal campo 4 (in coda alla
card o nel campo 6). Per il resto le tre card sono **6/6 campi** con
date parsabili nei campi 2 e 4 e token ATTUALE presenti (C50 e C52
CONFORMI a GV-2; contenuti verificati a `choice_ledger.yaml` C50/C52/
C53 e a VERDICT_C50_form2 §4 via la riga evidence del ledger).

**F10 — NOTE — capitolo intero — cella K-v non etichettata.**
Il design v2 assegna a B2 "celle K-i..K-v" (:544); K-v = "U3' aperto,
owner F2a; contratto MAI freezato prima" (:359). CH10 etichetta K-i
(§1), K-iii (§2a), K-ii (§2b), K-iv (§3.1) ma il contenuto K-v
(coperto in §1.5/§5) non porta l'etichetta di cella — il check di
copertura §M joina sulle celle. Riparazione a un'etichetta in §5.

**F11 — NOTE — §1.4 vs §1.5/§5 — namespace "U3" non disambiguato.**
Nel capitolo convivono i discharger U1-U5 di C-D25U (§1.4, §4.6) e la
regola d'estrazione U3/U3' di D6 (§1.5, §5, Q6): due namespace
distinti con lo stesso simbolo. Il capitolo fa la nota di
disambiguazione per "L4" (dovere di precisione dichiarato in testa) ma
non per "U3" — stessa classe di rischio per il lettore del deck.

**F12 — NOTE — righe 49-57 (§1.2, intro citazione) — span dichiarato
":158-165" vs citazione ":158-163".**
Il testo PRECISION citato termina a "never silently averaged."
(:163); :163-165 è la coda di routing ("All of this -> CH10 …") non
citata. La citazione in calce dice :158-163 (giusto); l'intro dice
:158-165. Difendibile (lo span intero è il blocco routato a CH10), ma
i due numeri nello stesso paragrafo divergono.

---

## TABELLA DISPOSIZIONE (V-N2 — compilata dal refuter C2)

| # | classe | riga/e CH10 | disposizione proposta | stato |
|---|--------|-------------|------------------------|-------|
| F1 | REPAIR | 275-281, 345-353, 374-376, 557-565, 618-623 | gradi per gamba dichiarati (THEOREM\*/split/SCHEMA); "ottimi diversi" → [T-DISC-3](b) con (DR); Q5 riformulata (h0-trace fissa, mu-medie fisse); DECK FEED 5 classe corretta | PENDING riparazione writer (resume B2) |
| F2 | REPAIR | 131-137 | C-SBVF → C-MAJDA | PENDING |
| F3 | REPAIR | 443, 464 | anchor C52 → :716, C53 → :726 | PENDING |
| F4 | REPAIR | 125-127 | anchor → D6 :1150-1153 (e opz. :1132-1160 → :1132-1157) | PENDING |
| F5 | REPAIR | 96-105 | "⇔" → due direzioni separate: "⇒" (pin, ammissibilità) + inversa SOLO al livello medio [T-NSW]/L4-DEFAULT | PENDING |
| F6 | NOTE | 384-389 | "esattamente" → identificazione parziale dichiarata | PENDING |
| F7 | NOTE | 70-74 | quote cucita → parafrasi o doppio frammento | PENDING |
| F8 | NOTE | 194-201, 300, 564 | "30→~2-6 atm" fuori-quote + CT-6 alla prima occorrenza | PENDING |
| F9 | REPAIR | 472-477 | nota harvest fuori dal campo 4 (GV-2) | PENDING |
| F10 | NOTE | — | etichetta K-v in §5 | PENDING |
| F11 | NOTE | 131-137, 143-153 | nota namespace U3 (come la nota L4) | PENDING |
| F12 | NOTE | 49-57 | intro → ":158-163" (o dichiarare il tail di routing) | PENDING |

Nessun finding respinto in partenza; nessun DECLASSATO (le ancore
verificate reggono ovunque tranne i punti sopra). 0 BREAK: nessun
claim load-bearing cade — F1 è un difetto di CLASSE/attribuzione su un
argomento che nel suo scope regge; tutti gli altri sono anchor/forma.

## Verifiche POSITIVE di record (ciò che REGGE, camminato)

- **Guardia 11**: 3/3 citazioni C-1bis VERBATIM (script); Γ_d≠throat
  detto GIUSTO in §1.2, Q2 e DECK FEED 3-4 (stazione
  supersonica-con-margine a valle del rilascio, m_n ≥ delta, sonic
  line corrugata come PERCHÉ, patch subsoniche = case-class O1-O4 mai
  mediate in silenzio); i tre ancoraggi (M0 :125-138, harvest
  :399-406/:611, problem book :302-317) tutti confermati alla fonte.
- **Guardia 17**: pin utente VERBATIM (2/2), lettura di record fedele a
  CKP-S2-1 in §1.2/§5-U3'/Q7 (unico eccesso = F5 "⇔"); Q7 nella forma
  corretta "solo sotto"; unstart boundary dichiarato in entrambe le sedi.
- **BC p-only ≡ proiezione π di [T-DISC] (attenzione iii)**: REGGE.
  D1.2 a M0 :1004-1008 definisce π: s(xi) ↦ (P(xi), uniform), "the
  EAP-style / pressure-only reading"; CH10 cita il pin [REV2-r1-1]
  (fibra = calibrated-scalars) in §4.5. Il BC Harroun (P(θ) + costanti
  fisse: harvest :274-296, :608) dipende SOLO dalla traccia P, quindi è
  costante su ogni fibra: la conviction sui surrogati π-factoring lo
  copre a fortiori — l'identificazione di classe è corretta (i gradi
  della conviction sono l'oggetto di F1, non l'identificazione).
- **G6**: quote verbatim vs D6 :808-810 ✓; estensione :811-815 ✓;
  tabella :290 ✓; "mai esercitato su dataset reale" = dichiarazione
  onesta presente (§5, DECK FEED 2).
- **Eccezione A4 non-registry** (§2b/§7a): grep rieseguito, 0 righe
  Gelb-Tadmor, Paciorri solo come WANTED :1142 — conforme
  all'emendamento §6b e alla forma [V2-R5].
- **§3-bis lineage**: join dichiarato sul LINEAGE_LEDGER; LL-6/LL-24/
  LL-2/LL-13/LL-5 + SEED-4 verificati riga per riga (quote :27-29
  esatta); tutti gli id registry citati esistono (grep misurato).
- **D.13/stage-A/monitor** (M0 VI.1 :3049-3099): tutte le
  trascrizioni fedeli (m_n = ess inf, TOTAL Mach PROIBITO, TRIPLE
  G-b1/G-b2 con direzione BLOCKING, B-1 ~4x, B-2 hypothesis-switch a
  M0 :999-1002, recovery THEOREM + AUD-hRANGE).
- **Aperti onesti**: U3' PREMISE-OPEN con quote verbatim D6 :201-202;
  contact/slip con ownership e default corretti (D6 :176-190);
  perimetro/canali residui di §4 conforme guardia 16 (theorem ledger
  :234-240 verificato per il front-block 1-D/multi-D).

## Q&A SEED (ordine ⑤; domanda → risposta → ancora → backup)

1. *"Che input vi serve da noi?"* → Al minimo le specs (caso A:
   propellente, φ, pressione media, geometria annulus, Pa): tool fully
   predictive a quel rung, stage di evidenza = PREDICTION (P34,
   dichiarato); ogni dato in più sale la scala B-G con classe
   dichiarata e macchina a valle identica. → D6 :1132-1157 (Annex B);
   findings :2530 (rider S-PRES). → Backup: tabella casi A-G + riga
   "stage: prediction" stampata.
2. *"Perché non le condizioni alla gola?"* → Γ_d NON è la gola: la
   sonic line RDE è corrugata (M=1 attraversata due volte per ciclo);
   il contratto chiede la stazione a valle dove m_n ≥ delta è
   misurato. → M0 :116-138; harvest :399-406/:611 (KP18 Fig. 6, CT-6).
   → Backup: crop KP18-F6 + schema m_n.
3. *"Harroun/Paxson lo fanno da anni con un BC imposto: che
   aggiungete?"* → Il loro BC è p-only = la proiezione π di [T-DISC]
   D1.2; dentro la classe A, [T-DISC-1] (THEOREM\*) + [T-DISC-2](i)
   (THEOREM\* scoped) danno fibre non-degeneri e J-separazione dove il
   confronto physical-h0-fixed è ammissibile; la conseguenza
   sull'ottimizzazione è [T-DISC-3](b) (SCHEMA, premessa (DR)
   nominata). Il contratto staged D.13 è la riparazione theorem-driven
   e la loro linea è antenato DICHIARATO (LL-6/LL-24). → M0 :1004-1008,
   :1030, :1086, :1184; LINEAGE_LEDGER :27-29, :46-48, :99-100.
   → Backup: slide gradi-per-gamba (mai "THEOREM" secco: è la forma
   post-F1).
4. *"L'ugello retro-agisce sulla camera?"* → Regola di record (pin
   utente): il decoupling è asseribile SOLO sotto choking pieno
   (pre-gola convergente + gola/superficie sonica tutta
   sonica-o-supersonica lungo ciclo e azimut); con patch subsoniche il
   feedback C'È (canali di risalita). Al livello MEDIO, su L4-DEFAULT,
   l'esclusione dell'influenza a monte è [T-NSW] (teorema); la linea
   imposed-BC del campo presuppone il decoupling senza citarne la
   condizione. Unstart = fuori dalla lettura a piccole perturbazioni,
   confine dichiarato. → SESSION2_LOG CKP-S2-1; GUARD_CHECKLIST
   guardia 17; M0 :128-130. → Backup: slide due-direzioni (necessità
   pin / sufficienza-media [T-NSW]) — forma post-F5.
5. *"Quando freezate il contratto d'estrazione?"* → Non prima di U3'
   (owner F2a): "NO freeze of the extraction contract before" —
   PREMISE-OPEN di record, dichiararlo È la risposta. → D6 :191-202,
   :264-267. → Backup: card U3' con trigger.
6. *"Come sapete che il dataset è buono? L'avete mai rigettato?"* →
   Stage-A + T0 flatness a soglia derivata + TRIPLE/D.16 + recovery
   con flag-never-extrapolate; fallimento = G6 loud-reject. Il gate
   non è MAI stato esercitato su un dataset reale — dichiarazione
   onesta, il falsificatore di N-K è vivo. → D6 :808-815; M0
   :3067-3087. → Backup: lista audit stage-A + riga "SPECIFIED-NOT-ARMED".
7. *"Che cosa NON è ancora deciso nel contratto?"* → Tre scelte con
   card stampate: C50 (metrica prodotto AGGIUDICATA, istanziazione =
   duty F2, flip F-ARCH pre-registrato), C52 e C53 (NON aggiudicate,
   finestra F2 contract window). → choice_ledger :694/:716/:726.
   → Backup: le tre decision card 6/6.
8. *"I vostri lignaggi di front-extraction (Gelb-Tadmor, Paciorri)
   non sono nel vostro registro letteratura."* → Vero e DICHIARATO:
   eccezione non-registry di record (decisione A4, grep misurato 0
   righe), vicino citabile `wanted_onofri_paciorri_2017_book`; upgrade
   solo alla finestra di promozione R7. → emendamento v2.1 §6b;
   registry :1142. → Backup: riga eccezione + path di promozione.

## CONTEGGIO GUARDIE (17/17 camminate)

| guardia | esito |
|---|---|
| 1 (gerarchia C-3bis col tallone (J)) | CLEAN (mai enunciata nel capitolo) |
| 2 (non-sequitur T1c) | CLEAN (assente) |
| 3 (naming rung quasi-1D) | CLEAN (assente) |
| 4 ("il campo" istanziato) | CLEAN (P-A..P-D via CH5 §1.1; harroun/miki/paxson_miki con id registry) |
| 5 (SOTA con asse §C o query-bounded) | CLEAN (§7c: §C-3 :279, §C-5 :281 verificati; divergenze dichiarate) |
| 6 (D-44 mai adequacy) | CLEAN (grep 0 hit, search-proven) |
| 7 (P34 stage su claim engine-level) | CLEAN (caso A/Q1/DECK FEED 1 = "prediction" dichiarato; nessun altro claim engine-level) |
| 8 (best-of-sweep) | CLEAN (nessun numero di campagna) |
| 9 (novità query-bounded) | CLEAN (deferita a CH5/G14; nessun mint nuovo, §3/§3-bis) |
| 10 (lineage solo dal LEDGER) | CLEAN (join {LL-id, componente} dichiarato; righe verificate) |
| 11 (Γ_d ≠ throat + verbatim C-1bis) | CLEAN (3/3 verbatim; contenuto giusto; NOTE F12 sullo span intro) |
| 12 (two-stage :1450) | CLEAN (grep 0 hit) |
| 13 (CT-6 numeri altrui) | **HIT** (F8: "30→2atm" fuori-quote vs "~2-6 atm" harvest; caveat assente alla prima occorrenza) |
| 14 (decision card 6/6 + GV-2) | **HIT** (F9: campo 4 di C53 non chiude col token; per il resto 3 card 6/6 conformi) |
| 15 (convergence provenance) | CLEAN sulla parte valutabile (il join è su §6 STORIA = W-B.2/C5 e sul retro-audit Blocco 2 — dichiarato FUORI-PERIMETRO sotto) |
| 16 (regola di classe [GV-4]) | CLEAN (perimetro + canali residui con classe in §4; nessun "coperto perché teoremi" senza canali) |
| 17 (feedback ugello→camera) | **HIT** (F5: "⇔" sovra-estende il pin "solo se"; verbatim e resto del cablaggio fedeli) |

**Guardie HIT: 3 (13, 14, 17). CLEAN: 14.**

## FUORI-PERIMETRO (dichiarato)

- §6 STORIA (righe 485-488): placeholder W-B.2 — ESCLUSA per ordine di
  brief; refuter C5 (W-C.b) la camminerà (guardia 15 piena lì).
- Adjudicazione delle righe LINEAGE_LEDGER in sé (CANDIDATE): è il
  passo C6 di W-C — qui verificata SOLO la fedeltà di CH10 al ledger.
- VERDICT_C50_form2.md / VERDICT_contract_and_L4R1.md: verificati via
  le righe evidence del choice ledger (contenuto delle card confrontato
  col testo del ledger, che è l'autorità C50 di record); i due file
  raws non sono stati riaperti riga-per-riga (le card non citano
  numeri nuovi oltre il ledger).
- Convergence provenance dei DECK FEED (guardia 15): dovere del
  retro-audit Blocco 2 / join §6, non del capitolo in questa onda.

## VERDETTO

**REGGE-CON-RIPARAZIONI.**
0 BREAK / 6 REPAIR (F1-F5, F9) / 0 GAP / 6 NOTE (F6-F8, F10-F12).
Le fondamenta del capitolo reggono alla refutazione avversaria: tutte
le ancore load-bearing verificate alla fonte tengono, i tre verbatim
C-1bis e i due pin guardia-17 sono esatti, l'identificazione
BC-p-only ≡ π regge, l'eccezione A4 e il lineage sono conformi. Le
riparazioni obbligatorie prima del consumo storyboard/deck: F1 (gradi
[T-DISC] per gamba — l'unica sostanziale), F2 (C-SBVF inesistente),
F5 (⇔ → solo-se), F3/F4 (anchor), F9 (GV-2). Nessuna riparazione
cambia una conclusione: cambiano classi, attribuzioni e anchor.
