# CH7 — L'edificio dell'averaging: mean-swirl 2.5-D → centerpiece R22-F → forchetta → swirl5f (i tre piani saldati)

Status: capitolo di RICOSTRUZIONE S-PRES (2026-08-22/23). Non aggiudica nulla:
ancora al record e dichiara gli aperti. Nasce da una CORREZIONE UTENTE: la
catena delle dimostrazioni a convergenza sull'averaging esisteva su tre piani
separati e la sessione ha faticato a rintracciarla come oggetto unico. Questo
capitolo la salda in una sola narrativa navigabile, con le catene until-dry
esibite e i punti di saldatura nominati.
Consumo dichiarato: storyboard v3 deck ESA, banca Q&A red-team, mappa
riutilizzabile per le sessioni future.

Convenzione di provenienza (vale per tutto il capitolo): i tre piani hanno
TRE classi di provenienza diverse, e la disciplina di consumo è essa stessa
parte del record —
- PIANO 1 e PIANO 2 = raws Phase D (advisory-class fino ad absorption;
  labels `MS-*` document-local, `phaseD_meanswirl_formalization.md:250-254`);
- PIANO 3 = ADVISORY di finestra parallela con regola vincolante "panel
  grades are NOT record grades" (`validation/swirl5f_panel_2026-08-19/DISPATCH_swirl5f.md:118-128`).
Ogni numero dei paper citato sotto è dei paper (CT-6); ogni classe di rigore
è quella stampata alla chiusura del rispettivo giudice, mai auto-promossa.

---

## 1. Ricostruzione

### 1.1 La domanda unica dietro i tre piani

Il programma progetta l'ugello su un funzionale CICLO-MEDIATO per fasi
assiali 2D. Tre domande distinte, storicamente affrontate in tre finestre
diverse, sono in realtà UN solo edificio:

1. **Che cosa deve contenere lo stato per-fase perché la media non menta?**
   → PIANO 1: il modello di stato 2.5-D CON swirl (Phase D, mean-swirl
   formalization, D.1–D.20 + S.22).
2. **Che cosa si perde esattamente riducendo il 3-D wave-frame a fasi
   assiali, e quanto pesa?** → PIANO 2: il centerpiece R22-F
   ([T-DISC]/[T-RED]/[M-RED] + FORCHETTA).
3. **Qual è la macchina di grado descrittivo superiore, e quanto vale
   comprarla?** → PIANO 3: il panel swirl five-field (upgrade path A/B/C,
   bias B1–B5, escapes E1–E11).

Le prime due saldature sono scritte NEI file, testuali. Il piano 2
definisce il suo operatore K dichiarando "distributional form is
[MS-DEF-KRES] of record" — cioè D.18 del piano 1
(`phaseD_r22f_centerpiece.md:461-463`); la forchetta consuma le classi di
bias B1–B5 del piano 3 nelle celle (ii)/(iii)
(`phaseD_r22f_centerpiece.md:1502-1503`). La terza è una LETTURA DI
ASSEMBLAGGIO di questo capitolo, dichiarata come tale: i ponti testuali
piano 3 → piano 1 sono i pin B-1/B-2 da fissare nella riga D.13
(`DISPATCH_swirl5f.md:80`, :86) e il "3-stage upgrade path" A/B/C
(:101-102); "STAGED" in D.13 significa "staged replacement text for M0
VI.1" — staging per absorption (`phaseD_meanswirl_formalization.md:1130-1133`),
non "gradino di una scaletta": la scaletta unica è la composizione che
il capitolo esibisce, non una dichiarazione dei file.

### 1.2 PIANO 1 — Il modello di stato 2.5-D per-fase con swirl (che cosa entra)

Documento: `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md`
(3090 righe; landing draft del verdetto panel mean-swirl 2026-08-11 mai
atterrato verbatim in M0 — header :4-16). Venti enunciati D.1–D.20 + schema
S.22, OGNUNO con classe di rigore, gamma-status e falsificatore
(claim register §6, :2587-2613). Carrier sympy:
`phaseD_meanswirl_symcheck.py` — OVERALL PASS (C1–C4, 7 check sulle 6 righe
K; rejector R1 SPARA su accoppiamento geometrico corrotto, :18-22).

I pezzi portanti per il deck:

**(a) D.13 — il contratto STAGED [MS-DEF-CONTRACT]** (:1130-1187): la riga
CycleFamily di record che sostituisce il placeholder `[vorticity]` di M0
VI.1. È la SCALETTA del grado descrittivo: (+) riga w(y;ξ)/Γ(y;ξ) come
invariante trasportato (una incognita/equazione in più per unit process);
(+) h0 promosso a PROFILE-GRADE — con la Remark 4.1 che dimostra (THEOREM,
una riga: "un funzionale identicamente nullo sul suo dominio non rigetta
nulla") che un monitor di Δ_h0 su una classe dati che non può rappresentare
Δ_h0 ≠ 0 è VACUO, violazione R5 (:1189-1208); (+) i tre audit: TRIPLE
monitor D.14 (rejector G6), riga di audit del momento angolare D.16, margine
di spacelikeness m_n = ess inf (M_n − 1) in forma meridional-normal (il
total-Mach come quantità di audit è PROIBITO, :1147-1156). Clausola di
recovery: unicità dello stato ricostruito PROVATA per tutti i Mach sotto
AUD-cp+AUD-c2T (THEOREM, due righe + ri-derivazione indipendente, :1166-1178).

**(b) D.14 — il TRIPLE monitor** (:1210-1304): l'oggetto formale che decide
QUANDO la forma chiusa N6-2 (macchina Rao a due costanti) è lecita. Forma di
record OBS(ξ) in TOTAL VARIATION (finita su BV, riparazione r1 di una forma
sup che era +∞ esattamente sui dati stratificati che motivano il monitor,
:1226-1247). Onestà a valle di r3: la DIREZIONE LICENZIANTE è un gap SCHEMA
a DUE gambe (G-b1 lemma di sensitività |errore obiettivo| ≤ S·OBS con caso
W-extremum trattato; G-b2 costante di tolleranza derivata per campagna) —
la retraction "the FORM is no longer the gap" è di record (:1267-1293). La
direzione BLOCCANTE è conservativa e non affetta. Aspettativa di record,
unanime: i dati RDE reali generalmente FALLIRANNO la triple-uniformity e
ruoteranno sulla macchina field-level — "il mestiere del monitor è routing
onesto, non benedizione" (:1295-1298).

**(c) D.15 — GAMONLY, il falso-licenziamento** (:1306-1367): monitorare SOLO
lo swirl non basta. Clause 1 THEOREM (identità N6-3 machine-verified +
exhibit): esistono dati con Γ ≡ 0 e h0′ ≠ 0 su cui la chiusura puntuale
p = p(W, y) FALLISCE — un monitor Γ-only direbbe "uniform" e licenzierebbe
una forma chiusa falsa. Clause 2 (minimalità/iff) SCHEMA, quantificatore
all-admissible-variations load-bearing; la famiglia di cancellazione
Γ Γ′ = y² h0′ è esibita e il monitor OBS è CONSERVATIVO contro di essa
(bloccherebbe — safety note :1352-1356).

**(d) D.10 — SKE, il primo ordine non vincolato** (:1055-1096): il flusso di
energia cinetica di swirl E_θ > 0 strettamente sotto through-flow, e NON è
vincolato da nessun vincolo di flux-nullity (D.6) sotto NESSUNA misura:
l'exhibit θ-halves-at-each-radius cancella il flusso di Γ r-fiberwise con
E_θ arbitrario. Al livello di fluttuazione misurato del corpus
(σ/μ ≈ 0.70, numeri P-M citation-bound) i termini di covarianza e KE pesano
(σ/μ)² ≈ 0.5: PRIMO ORDINE, non cosmetico. Corollario operativo: il twin
zero-swirl (TWIN-A) è fair SOLO a livello net-flux e mis-attribuisce quattro
meccanismi nominati; il twin fair di record è TWIN-C (flux-consistent, E_θ
riportato come residuo dichiarato); TWIN-B REFUTED come fair (:1069-1087).

**(e) D.20 — la rothalpy, l'invariante che la riduzione spezza** (:2398-2462):
il flusso 3-D esatto NON trasporta h0 e Γ separatamente — trasporta solo
I = h0 − ΩΓ (D_rel I = 0 machine-verified; [I] = 0 attraverso fronti
mass-crossing, THEOREM*; [I] LIBERO sui contatti wave-frame, THEOREM). Il
modello 2.5-D per-fase li trasporta ENTRAMBI separatamente: la riduzione
SPEZZA un invariante esatto in due invarianti di modello, e l'errore di
splitting è esattamente la coppia di pumping D.19 (D_rel h0 = Ω·D_rel Γ).
Corollario (b): l'uniformità di rothalpy NON salva la licenza N6-2 — nessuna
scorciatoia oltre D.14 (:2424-2444).

**(f) §5 — che cosa il 2.5-D LASCIA CADERE** (:1439-2360): D.17 definisce il
sistema 3-D wave-frame (ξ ↔ φ: la label di fase È l'azimut nel wave frame,
:1443-1462); D.18 [MS-DEF-KRES] definisce le SEI righe K del residuo di
riduzione (mass/x-mom/r-mom/Γ/s/h0 sweep + termini TORQUE e WORK,
:1478-1483), in lettura DISTRIBUZIONALE (atomi sui fronti, identità di
ricombinazione triangolare parte della definizione, :1488-1527). Le due
clausole "iff" di D.18 stanno a SCHEMA per downgrade del giudice
(J-r2p-2/J-r2p-3,
`validation/sfoundations_raws_2026-08-13/r2pass/VERDICT_r2pass.md` —
attenzione al path: r2pass/ è SORELLA di phaseD/, non figlia; sotto
citato in breve come `r2pass/VERDICT_r2pass.md`), path di restauro =
batteria G-f (:2610, colonna classe). S.22 [MS-S-KBOUND] è il TARGET
statement del bound del residuo (SCHEMA; il candidato-norma r1 RITIRATO
a r2 con DOPPIA refutazione — atomi di K sui fronti, cono avvolto
azimutale ("refuted twice over", :2472-2488); le correzioni r3 (falsa
equivalenza sul sostituto) colpiscono il candidato SOSTITUTO, e la fork
di norma sul sostituto è registrata come decisione del T-RED owner,
:2464-2507).

**(g) La catena until-dry del piano 1** (il "chi lo ha giudicato"): SETTE
round di refutazione avversaria applicati IN PLACE, r1–r7 + r7.1
(header blocks :24-248), con ledger per-obiezione §6-bis..§6-quinquies
(:2693-3060). La copertura dei giudici, dichiarata per-tratto: i round
r1–r3 sono refutazioni APPLICATE DALL'AUTORE con ledger per-obiezione,
SENZA giudice separato; il giudice di batch `r2pass/VERDICT_r2pass.md`
copre il set r2-pass (downgrade J-r2p-2/3), e le amendment r7.1
(AM-1..AM-3) sono aggiudicate dal giudice del confirming round
`r2pass/VERDICT_confirm.md` §4 (:229-238) — il "giudice di batch" NON
copre la catena intera. CAVEAT VINCOLANTE, parte del verdetto: per
VERDICT_r2pass §1/§4 il verification layer è UNPROVEN in confirm
direction (known-true seed FAILED), "nothing in this revision may be
cited as layer-certified", e il Blocco-2 landing gate resta CLOSED per
il set r2-pass — caveat portato avanti VERBATIM fino a r7
(`phaseD_meanswirl_formalization.md:92-96`, :226-227). Il processo
documenta le proprie retraction NEL testo: quattro over-certificazioni
consecutive dell'assembly D.18 ANNOTATE con contatore (:209-211),
interruzione r5 riconciliata su file (:128-138), false-completeness
r2 corretta per annotazione mai per cancellazione (:40-47). Metodo di lavoro:
§7 absorption targets — questo doc = staging, l'atterraggio in M0/N6/D6 è un
pass R4 con siti nominati (:3061-3090).

### 1.3 PIANO 2 — Il centerpiece R22-F (che cosa si perde e quanto pesa)

Documento: `validation/sfoundations_raws_2026-08-13/phaseD/phaseD_r22f_centerpiece.md`
(2277 righe; mandato = riga registry `theory:r22-formal-decomposition`,
header :1-9). Giudici: `blocco3/VERDICT_r22f.md` (closure judge, labels §1
di record) e `blocco3/VERDICT_escalation_c4.md` (escalation E-1..E-5).

**PART 1 — [T-DISC], la condanna della media via fibre** (:108-431).
D1.2 definisce la proiezione p-only π (si tiene solo la traccia di pressione
P(ξ), il resto ai μ-mean della famiglia — fibra "calibrated-scalars",
pin [REV2-r1-1] :129-139). [T-DISC-1] (THEOREM*): la fibra sopra una P-trace
ammissibile contiene una famiglia a un parametro con (P, h0, s, mdot)
IDENTICI e E_θ da 0 a scala corpus, che soddisfa OGNI vincolo di record —
nessun vincolo determina E_θ dato (P, h0, s, mdot) (:150-206; consuma D.6 +
D.10 del piano 1 + K̄ = 0 del piano 3: le tre provenienze in un solo
enunciato). [T-DISC-2] = il LOWER BOUND di J-separazione nella fibra — "i
pesi" della condanna: gamba di segno THEOREM* (SCOPED: livello booking,
confronti physical-h0-fixed; ramo DROP non compensato geometry-signed con
angolo degenere r_e = r_in — :210-257), gamba di grandezza
SCALING-ESTIMATE dichiarata: classe B2 1.5–3% della spinta (fold), con la
companion B1 0.6–9% di p (:259-270). Lettura onesta di record: floor
strettamente positivo single-signed a THEOREM-grade SOLO sul ramo
physical-h0-fixed; NESSUN lower bound numerico a THEOREM grade
(:272-289). Design su pressione/media: CONVICTED strutturalmente
(la media non distingue membri della fibra con J diversi), con i pesi a
classe [SE] finché M-RED non misura (B-2).

**PART 2 — [T-RED], l'operatore di ciò che si perde** (:432-1182). Il
residuo di riduzione è ESPLICITO ed ESATTO:
K = (1/r) ∂_φ[F_φ,rel(W)] in senso distribuzionale, con F_φ,rel scritto
riga per riga (identità machine-witnessed, judgeverify ITEM 3.1) — e la
definizione dichiara che l'oggetto è [MS-DEF-KRES] del PIANO 1
(:459-481): la saldatura T-RED→D.18 è testuale, non interpretativa.
Risultati: (i) K̄ = 0 fiberwise THEOREM* su compositi BV periodici — la
riduzione NON ha canale di primo ordine mean-field; sopravvivono ESATTAMENTE
DUE canali di primo ordine, (J) accoppiamento atomi/salti e (H)
covarianza/isteresi a.c. — condizionale su H-RED-2(SBV) (:512-539);
(ii) scale di primo ordine [SE] verifier-repaired: Λ = 0.59–1.11·St_n,
termine di lavoro 0.7–9%, spina χ = ΩΓ/h0 = 0.06–0.20 con chiusura esatta
EOS-free χβ_τ = β_w (:540-548); (iii) la cancellazione on-ray O(St²)
esiste in-panel ma è LICENSE-GATED sul carrier X-T3QS-5F (F2): fino ad
allora la barra J1 si CALCOLA sui dati swirl, mai argomentata via
(:549-553); (iv) fatturazione della frontiera: la metà time-coupling è
G3/corrector-owned, [T-RED] è SOLO la metà azimuthal-structure (:449-457).

**PART 3 — [M-RED], il metodo di misura** (:1184-1391): spec di carrier
(PRACTICE), zero CFD, zero costanti magiche. Strumento = protocollo O5-lite
(A)-(E) — J_exact vs J_avg; vs J_avg + J1^K; F_true(ξ) vs F_2D(ξ) puntuale
(discrimina (J) da (H), licenziato dall'identità di settore claim 1);
St-sweep esponente (→2 on-ray, →1 off-ray); fitted-sheet ON/OFF — con i pin
BLOCCANTI B-1/B-2 del dispatch swirl5f obbligatori PRIMA del run
(:1202-1213). Famiglie F-a..F-d certificate in-house (:1221-1235); bande
B-1..B-4 DERIVATE con le derivazioni pubblicate (Richardson ≥ 4 punti,
misura esplicita dmdot, floor di margine di DOMINIO con re-check su mesh
ladder — ogni riparazione da probe refuter di record, :1237-1374). Esito:
sposta le colonne (ii)/(iii) della forchetta da [SE] a MEASURED sulle
famiglie certificate; il class-wide resta gated su (U) (:1376-1384).

**PART 5 — la FORCHETTA** (:1458-1743; mandato utente verbatim in testa:
"mi devi dare onestamente quale è la forchetta da aspettarsi, la situazione
migliore e peggiore"). Sei canali, ogni cella bound-or-estimate dichiarato +
classe + provenienza + "what tightens it" in ordine di programma. Header
strutturale di record: NESSUN REFEREE ESTERNO PUBBLICATO esiste per l'errore
di spinta per-fase; la forchetta si CHIUDE solo via R22-CFD nostro o
procurement dedicato (:1485-1497). Headline di record (:1731-1743): BEST
on-ray single-digit % plausibile (con qualificatore good-fitted-sheet
restaurato in TRE siti dopo che tre round lo hanno trovato caduto — 
:1745-1755), canale medio esattamente nullo (THEOREM*), debito booking
1.5–3% [SE]; WORST off-ray >10% NON escluso [SE], marcatore di direzione
peggiore = shroud Paxson-Miki 58.1% → ~71.5% dell'ideale ad area ratio
fisso (dato [REP], più grande dell'intera linea di design area-ratio, non
spiegato dagli autori); canale (vi) OPTIMUM-SHIFT: δ E L_H UNDERIVED —
NESSUN numero di argmax-shift a nessun grado (:1506).

**La catena until-dry del piano 2**: 4 round × 3 lenti
(L0 variazionale / L1 PDE-iperbolica / L2 asintotica-misura) = 66 findings
(4 BREAK, 23 REPAIR, 22 AMENDMENT, 17 NOTE), 14 probe eseguiti dai refuter,
disposizioni §§10-13 append-only con frammenti superseded citati verbatim
(`VERDICT_r22f.md:508-521`). Verdetto giudice: NOT-DRY-AT-CAP ma
APPROVED FOR LANDING con residui RES-CAP nominati; labels §1 = autorità
unica (:510-513, :49-123). Escalation E-5 (delta round-4): un round, tre
lenti, 0 BREAK unanime, 3 REPAIR judge-verified; le quattro escalation
minori E-1..E-4 chiuse DRY; 53/53 findings SUSTAINED
(`VERDICT_escalation_c4.md:542-553`).

### 1.4 PIANO 3 — swirl5f: la macchina di grado superiore (quanto vale comprarla)

Documento: `validation/swirl5f_panel_2026-08-19/DISPATCH_swirl5f.md`
(finestra parallela 2026-08-17→19; 10 agenti, ~2.0M token, 4 deriver a
lente distinta + 4 refuter avversari + giudice + judge-verifier sympy;
45 defect items TUTTI disposti, 11 contraddizioni cross-lens risolte con
algebra ri-eseguita; verdetto CONVERGED-WITH-THREE-NAMED-EDITS, :12-33).

Contenuti consumati dall'edificio:
- **K̄ = 0 UNCONDITIONAL** confermato dal verifier (:64, :147) — la gamba
  (c) di [T-DISC-1] e il cuore di [T-RED-2](i).
- **Classi di bias B1–B5 quantificate [SE]** (:63): B1 equilibrio radiale
  0.6–9% di p; B2 booking swirl-KE 1.5–3% spinta (fold; drop-variant
  |bias| ≤ δ_int²/2, ≤ fold iff r_exit ≤ √2·r_in — edit verifier R-B);
  B3 stato/margine; B4 bypass licenza N6-3; B5 swirl d'uscita 10–14°.
  Consumate dalle celle forchetta (ii)/(iii).
- **Escapes E1–E11** (:68): la lista CHIUSA di ciò che NESSUNA macchina
  per-fase cattura, con pin di lettura di record (user catch): la famiglia
  per-fase ricostruisce SOLO l'ombra data-anchored x_s(ξ) delle sheet
  elicoidali interne; i segmenti di fronte azimuthally-fed sono
  IRRAGGIUNGIBILI dalla marcia assiale (corollario zero-winding). E5
  magnitudine DISPUTED-OPEN.
- **Adjoint five-field [S-5F]**: core PROVEN in-panel (due trasposizioni a
  mano + due machine check), ma resta SCHEMA di record finché le gambe OPEN
  non chiudono (lip/corner, contact-crossing, ecc.) (:59); risoluzione
  sonic-exit REFUTED-AND-REPLACED e verifier-CONFIRMED (:60).
- **Pin di contratto BLOCCANTI B-1/B-2** (:71-86): trappola di
  normalizzazione A4 (KE- vs h0-frazione, fattore ~4; test discriminante:
  solo la lettura KE dà Ωr ≈ D_CJ) e pin di convenzione h0 (decide la
  variante fold/drop di B2). Da fissare nella riga D.13 PRIMA di ogni
  ingestione dati — sono il ponte operativo piano 3 → piano 1.
- **La scaletta di upgrade path A/B/C** (:99-116): A = free-vortex carry;
  B = build five-field engine+adjoint; C = procurement dati tangenziali.
  DECISIONE UTENTE PENDENTE di record (:179-183), NON presa dal panel. Con
  l'annotazione utente [T-N6-2] di record: il carry free-vortex di path A è
  THEOREM solo sotto (rΓ, h0, s) UNIFORMI — su campi per-fase stratificati
  la combinazione NON è un teorema di record; il dossier S-5F deve
  presentare la fork (lemma misto da scrivere vs monitored-neglect armato
  dal TRIPLE monitor) prima di ogni adozione di path A (:105-113).

### 1.5 Le saldature, esibite

1. **T-RED vive in D.18**: l'operatore K del piano 2 È [MS-DEF-KRES] del
   piano 1 per dichiarazione testuale (`phaseD_r22f_centerpiece.md:461-463`);
   il censimento delle sei righe avvettive + atomi è il claim 2 del panel
   (PROVEN-HERE in-panel, 3 derivazioni indipendenti) mentre la completezza
   div-form resta G-f SCHEMA — i gradi NON gonfiati nel consumo (:474-481).
2. **La forchetta consuma entrambi i vicini**: celle (ii)/(iii) = covarianza
   mean-swirl (D.9/D.10, piano 1) + bias B1–B5 (piano 3), con la seam
   dichiarata — (iii) è canale di fedeltà DATI, (ii) è canale di RIDUZIONE,
   stessa fisica swirl, aggregatore legittimo solo la misura congiunta
   M-RED F-c (`phaseD_r22f_centerpiece.md:1713-1722`).
3. **La scaletta descrittiva è una sola** [lettura di assemblaggio del
   capitolo, dichiarata — non una saldatura testuale come le prime due]:
   D.13 (+w/Γ, h0 profile-grade, TRIPLE, AM audit, m_n) = il gradino già
   scritto; path A/B/C = i gradini successivi, con la fork [T-N6-2] sul
   path A e la decisione utente pendente. Ancore dei ponti reali: pin
   B-1/B-2 → riga D.13 (`DISPATCH_swirl5f.md:80`, :86) + "3-stage
   upgrade path" (:101-102).
4. **Il metodo di lavoro è lo stesso sui tre piani**: staging → refutazione
   until-dry → giudice → absorption targets (§7 piano 1; landing list
   VERDICT_r22f §7 piano 2; registration duty §7 dispatch piano 3), con la
   regola di consumo "panel grades are not record grades" e i mint
   (sector-decomposition F-2, K̄ = 0) che RIDONO la landing window invece di
   auto-promuoversi.

### 1.6 Glossa minima (per il consumo storyboard/Q&A, pubblico misto)

- **on-ray / off-ray**: sulla/fuori dalla famiglia di cicli quasi-stazionari
  "ray-like" (es. dente di sega) — on-ray l'errore di riduzione scala come
  St², off-ray come St (esponente = leg (D) di M-RED,
  `phaseD_r22f_centerpiece.md:1206`; frase licenziata :527-533).
- **fitted sheet**: la sheet del fronte FITTATA sui dati — l'ombra
  data-anchored x_s(ξ) del fronte elicoidale usata dalla famiglia per-fase;
  "good fitted sheet" è qualificatore load-bearing dell'headline, testato da
  M-RED leg (E) (ibid. :528-533).
- **booking level**: confronto a condizioni di USCITA CONGELATE (geometria +
  traccia di pressione statica d'uscita fissate, ipotesi H2.2): ciò che il
  funzionale registra a dati fissati, NON la coppia di soluzioni reali
  (actual-pair → M-RED B-2; ibid. :229-232, :248-257).
- **St_n**: il piccolo parametro della riduzione — avvolgimento azimutale
  delle bicaratteristiche 3-D per transito meridionale, O(St) per transito
  (`phaseD_meanswirl_formalization.md:2483-2488`).

---

## 2. Stato per-claim

| Claim | Classe | Ancora | Carrier / falsificatore |
|---|---|---|---|
| Stato per-fase 2.5-D (D.1) + trasporto (s,h0,Γ) (D.2) | DEFINITION / THEOREM (H-FIB, arc H-CVX espliciti) | `phaseD_meanswirl_formalization.md:2591-2592` | symcheck C4-gamrow-equiv PASS; controesempio-falsificatore |
| D.13 contratto STAGED (riga w/Γ, h0 profile-grade, m_n) + recovery unica ∀M | DEFINITION + THEOREM (clausola recovery) | ibid. :1130-1187, :2604 | stage-A audits = rejectors; istanza-tabella a due stati |
| Remark 4.1 — monitor h0 su classe pre-swirl = VACUO | THEOREM (γ(T)-exact nella premessa) | ibid. :1189-1208 | exhibit di recovery con h0 dipendente da y |
| D.14 TRIPLE monitor OBS in TV | DEFINITION + gap SCHEMA 2 gambe (G-b1/G-b2) sulla direzione licenziante; blocco conservativo intatto | ibid. :1210-1304, :2606 | falsificatore a due limbi (backflow-guard; contour oltre tolleranza propagata) |
| D.15 Γ-only = falso licenziamento | Clause 1 THEOREM; Clause 2 SCHEMA | ibid. :1306-1367, :2607 | N6-3 machine-verified + exhibit; famiglia di cancellazione |
| D.10 E_θ > 0 primo ordine non vincolato; TWIN-A unfair, TWIN-C di record | THEOREM + PRACTICE (righe twin) | ibid. :1055-1096, :2601 | panel A4 (con pin B-1); T3-CONTROL limb (iv) |
| D.16 audit momento angolare (balance-residual, arming firmato + backflow) | PRACTICE rejector-gated, target THEOREM*-backed (D.6) | ibid. :1369-1436, :2608 | arming test con torque noto; dataset doctored deve FALLIRE |
| D.18 sei righe K distribuzionali; clausole iff | DEFINITION + SCHEMA (completezza G-f; ENTRAMBE le iff SCHEMA per downgrade giudice J-r2p-2/3) | ibid. :1464-1527, :2610 | batteria G-f (spec estesa 4 volte, istanze rejector nominate) |
| D.20 rothalpy: la riduzione spezza I = h0 − ΩΓ | THEOREM (smooth + contatti) / THEOREM* (fronti mass-crossing) | ibid. :2398-2462 | carrier C3+R1 PASS (rejector spara); falsificatore contact-clause |
| S.22 bound del residuo | SCHEMA (target; fork di norma registrata) | ibid. :2464-2507, :2613 | test caso degenere K ≡ 0 |
| [T-DISC-1] fibra non degenere (nessun vincolo fissa E_θ) | THEOREM* (condizionali c1-c3 nominati) | `phaseD_r22f_centerpiece.md:150-206`; `VERDICT_r22f.md:65` | falsificatore: UN vincolo di record che determini E_θ da (P,h0,s,mdot) |
| [T-DISC-2] separazione-J: segno / grandezza | THEOREM* (SCOPED booking, physical-h0-fixed) / SCALING-ESTIMATE 1.5–3% | ibid. :208-305; `VERDICT_r22f.md:66-68` | istanza con ∂(mdot·u_e)/∂Γ² ≥ 0; famiglia sotto barra B-2 |
| [T-RED-1] K esplicito ed esatto = [MS-DEF-KRES] | DEFINITION; identità THEOREM* (prov. ADVISORY) | ibid. :459-481; `VERDICT_r22f.md:77` | judgeverify ITEM 3.1 sympy + doppia derivazione a mano L1 |
| K̄ = 0 ⇒ due soli canali primo ordine (J)/(H) | THEOREM* (condizionale SBV; prov. ADVISORY fino a mint R-6) | ibid. :512-539; `DISPATCH_swirl5f.md:64` | verifier-confirmed; witness sympy |
| Scale primo ordine Λ, χ, spike-core | SCALING-ESTIMATE (forme verifier-repaired R-A/R-C) | ibid. :540-548 | bande judge-verified (jv_check.py) |
| Cancellazione on-ray St² | LICENSE-GATED (non usabile) | ibid. :549-553; `DISPATCH_swirl5f.md:58` | carrier X-T3QS-5F (F2) = la licenza |
| M-RED protocollo O5-lite + bande B-1..B-4 | PRACTICE (spec; esecuzione = duty F2 §3.6) | ibid. :1184-1391; `VERDICT_r22f.md:90-97` | rejector di banda (esponente→1; localizzazione uccisa da mismatch fuori finestra) |
| Forchetta 6 canali + headline | per-cella (BOUND cond. / [SE] / [REP] / SCHEMA); NESSUNA cella sopra la sua classe | ibid. :1499-1506, :1731-1743; `VERDICT_r22f.md:106-122` | M-RED sposta (ii)/(iii) a MEASURED; R22-CFD chiude |
| (vi) OPTIMUM-SHIFT: δ e L_H UNDERIVED, nessun numero di argmax-shift | SCHEMA entrambe le route | ibid. :1506; `VERDICT_r22f.md:121` | derivers nominati (X-T3QS-5F → C51-B → rider M-RED → R22-CFD-1) |
| Bias B1–B5 quantificate | [SE] (assembly repaired; St_n-conditional) | `DISPATCH_swirl5f.md:63` | pin B-1/B-2 + dataset test D.11/[H-sgn] |
| Escapes E1–E11 lista chiusa + lettura ombra/zero-winding | D+R panel; E5 DISPUTED-OPEN | ibid. :68 | misura Δx_s standoff modulation |
| Adjoint 5F core / sonic-exit quotient | PROVEN in-panel; [S-5F] resta SCHEMA di record | ibid. :59-60 | gambe OPEN nominate; wiring engine duty |
| Identità sector-decomposition J_exact = ∫F_true dμ | THEOREM in-panel; NON di record — MINT CANDIDATE F-2 | ibid. :56 | mint nella landing window; fino ad allora ADVISORY dichiarato a ogni consumo |

---

## 3. Gli APERTI (owner/trigger — mai riempiti qui)

| Aperto | Owner / trigger |
|---|---|
| DECISIONE UTENTE S-5F build path A/B/C (con fork [T-N6-2] su path A) | UTENTE, confine di sessione (`DISPATCH_swirl5f.md:179-183`; memoria swirl5f-panel) |
| DECISIONE UTENTE priorità C51 (il dispatch ne RAFFORZA il caso, claims 6/13) | UTENTE (ibid.) |
| (U) uniformità S.22 sub-scope + H-A1 class-wide (R-1) — decide la lettura class-wide di [T-DISC-3]/[T-RED-2](iv) | F2, teorema S.22 shock-free sub-scope |
| C-T1 bound off-ray (">10% NOT excluded") (R-2) | M-RED famiglia F-d / O5-lite |
| Licenza X-T3QS-5F (R-5) — sblocca il St² on-ray | F2, carrier committato |
| Mint F-2 (sector-decomposition) + grado record K̄ = 0 (R-6) | landing window M0/R4 |
| L_H curvature-transfer UNDERIVED (R-16/RES-CAP-2) + δ gradient-bound (R-9) — il canale (vi) resta senza numero | F2: X-T3QS-5F Hessian-level → C51-route-B → rider M-RED |
| R-12 certified basin radius per il check a-posteriori di argmax-shift (curvature re-measure ladder su palle attorno a S*) | estensione del rider M-RED §3.6 (F2) (`phaseD_r22f_centerpiece.md:1796-1800`) |
| R-15/RES-CAP-4 eps_U sampled-sup + ladder re-check (consumato dalla value-route della cella (vi)) | rider M-RED §3.6 / protocol run (F2) (`phaseD_r22f_centerpiece.md:1836-1852`; `VERDICT_r22f.md:528-529`) |
| Convessità KS-margin-set a S* margin-active (R-14/RES-CAP-3) + gate O1 (R-13) | F2 / F4b theory WP |
| G-b1 lemma di sensitività del TRIPLE monitor (+ G-b2 tol per campagna) | N6 §5 line; gate di OGNI uso licenziante di D.14 |
| G-a check simbolico D.6/D.20-fronti; G-f batteria completezza D.18 (restaura le iff da SCHEMA) | task promozione D.6 (F2); carrier upgrade G-f |
| G-e vuoto empirico: NESSUN falsificatore §3 (F1–F4, A4) mai calcolato nel corpus | prima ingestione dataset (pin B-1/B-2 BLOCCANTI prima) |
| E5 magnitudine (Δx_s standoff) | misura dedicata (G-e/O5 window) |
| Pin bloccanti B-1 (normalizzazione A4) e B-2 (convenzione h0) nel testo D.13 | D.13/prima ingestione — BLOCKING |
| Assenza referee esterno per l'errore di spinta per-fase (dichiarazione strutturale forchetta) | si chiude SOLO con R22-CFD nostro o procurement (R-8 per la base-pressure) |
| Absorption non ancora eseguita: i tre piani sono raws/advisory UNTRACKED; landing list = VERDICT_r22f §7 + VERDICT_escalation_c4 §6 + dispatch §7 | orchestratore, landing window (R7/SR-6) |

Questa tabella è una SELEZIONE orientata al deck, non un censimento: la
lista completa dei residui è il centerpiece §6 (R-1..R-17,
`phaseD_r22f_centerpiece.md:1783-1861`) + RES-CAP-1..6
(`VERDICT_r22f.md:526-531`) — chi risponde in Q&A sulla cella (vi)
consulta QUELLA lista, non questa.

---

## 3-bis. ANTENATI DIRETTI (lineage claim, nodo N-E) [W-B.1/B7]

Join dichiarato (contratto [F-des-4], LINEAGE_LEDGER.md:8-16): ogni
claim di novità di questo nodo cita ≥1 riga LL (lint 7); prosa integrale
nelle parti sorgente (Pn.r). Stato righe: CANDIDATE fino al pass del
refuter C6 (LL-13/LL-14 sono seed utente, confermati dalle parti,
restano attaccabili). Formato: antenato → cosa fa → cosa gli manca.

- **LL-14 Kraiko-Tillyaeva 2015** (`kraiko_tillyaeva_2015`, registry
  :498; componenti 3/11/12). Cosa fa: problema conjugate/moltiplicatori
  COMPLETO per ugello Laval (inclusa la parte subsonica), catena
  Route B→A interna alla scuola ((2.2)→(2.9)→(2.10)→(2.12), CONCESSA di
  record) + antenati di certificati: (2.9) = re-espressione del residuo
  Hoffman-E, (2.5)-(2.6) = terza classe di certificato F4b, (2.11) =
  candidato oracolo adjoint closed-form [O6] [P2.S-2; matrix
  part2:51-68]. Cosa gli manca: famiglia MEDIATA (tutto single-state),
  adjoint discreto/AD, soglie derivate e rejector sui certificati. È la
  scuola che possiede il precedente swirling (riga 2.2(f) di G5, §7(a)).
- **LL-13 Fievisohn** (Yu JPP 33(1) 2017 method-paper + PhD UMD 2016,
  **[IO]** da sweep-disco di record; il nozzled AIAA 2018-0881 =
  `wanted_fievisohn_2018_quasi2d_moc`, registry :1280, [REP]-bounded,
  procurement RAISED; componenti 1?/5/6/7/10/15). Cosa fa: IL cugino
  pubblicato più vicino — wave-frame ESPLICITO ("wave-fixed reference
  frame", la stessa mossa del nostro quoziente), rotational shock-fitted
  MoC con unit process Zucrow-Hoffman + slip-line dedicato, inflow BC
  feed-coupled [P2.S-1; matrix part2:443-500]. Cosa gli manca: il ciclo
  è ENDOGENO (iterato a convergenza, non classe-dati IMPOSTA con
  monitor), mai design, mai famiglia per-fase, mai ottimalità/certificati;
  nessun capitolo ugello nel TOC del PhD — l'estensione nozzled vive
  solo nel paper assente da disco (nessun claim oltre la riga [REP]).
- **LL-9 Wintenberger-Shepherd 2004** (`wintenberger_shepherd_2004`,
  registry :261; componente 9). Cosa fa: audit di bilancio entropico
  PER-PHASE (Eqq. (23), (31)-(32), (38) — graft A35, wiring già in
  src/cycles con 3 condizioni vincolanti) [P1.9; matrix part1:210-222].
  Cosa gli manca: l'identità di decomposizione del funzionale J (il
  nostro mint-pending F-2) e ogni struttura di design sulla famiglia.

Perimetro di novità conseguente: il campo possiede il quoziente
wave-frame operativo (LL-13), la macchina moltiplicatori+certificati
single-state (LL-14) e l'audit per-fase (LL-9); ciò che nessuna riga
porta è l'edificio a tre piani di questo capitolo — stato 2.5-D
per-fase CON residuo di riduzione nominato + forchetta + scaletta di
upgrade; sul lato swirling-contouring il claim di novità resta BOUNDED
dal procurement Tillyaeva 1975 (§7(a)).

---

## 4. Domande da panel (banco utente, con risposta)

**(1) "Cosa perdiamo con lo swirl e cosa guadagniamo rispetto a fare design
su pressione media?"**
Il design su pressione/media è CONVICTED via fibre: sopra la stessa traccia
di pressione (e gli stessi scalari calibrati) vive una famiglia a un
parametro con contenuto swirl da 0 a scala corpus che NESSUN vincolo di
record distingue ([T-DISC-1] THEOREM*), e J si separa dentro la fibra in
modo single-signed a livello booking ([T-DISC-2](i) THEOREM* scoped) con
peso di classe 1.5–3% della spinta [SE] più la companion B1 0.6–9% di p
[SE]. Scope della gamba di segno, dichiarato dal record: single-signed
vale sui confronti physical-h0-fixed (FOLD o variante compensata); il
ramo DROP non compensato è geometry-signed con separazione IDENTICAMENTE
ZERO a r_e = r_in (`phaseD_r22f_centerpiece.md:237-247`), e la
separazione ACTUAL-PAIR (exit state libero — ciò che un design reale fa)
NON è asserita ad alcun grado teorematico: è la domanda misurata M-RED
banda B-2 (:248-257, :287-289). Ciò che si PERDE trattenendo lo swirl
nel modello 2.5-D è invece esattamente l'operatore K (sei righe +
atomi) — di media nulla (K̄ = 0 THEOREM*), due soli canali di primo
ordine, single-digit % plausibile on-ray con fitted sheet, >10% non
escluso off-ray [SE]. Guadagno netto: si scambia un errore NON VINCOLATO
DA ALCUN VINCOLO DI RECORD (falsificatore APERTO: esibire UN vincolo di
record che determini E_θ da (P, h0, s, mdot) uccide il teorema —
`phaseD_r22f_centerpiece.md:201-203`; non-vincolato-dal-record ≠
impossibilità di vincolo) e invisibile alla media con un residuo
NOMINATO, a media nulla, misurabile (M-RED) e con la scaletta per
ridurlo. Clausola di RILEVANZA, portata dal record stesso (:426-430): il
falsificatore della condanna non è della sua verità ma del suo peso — se
l'eps_fib misurato da M-RED cade sotto il più piccolo delta di design
che il programma certifichi, "the conviction is real but priced
irrelevant for our class"; la condanna è strutturale, il suo PESO
relativo al residuo K è la misura CONGIUNTA M-RED (famiglie F-c),
pre-registrata — finché non misura ENTRAMBI, il confronto 1.5–3% [SE]
vs ">10% non escluso off-ray" resta dichiarato aperto.

**(2) "Qual è la scaletta di proposte per aumentare il grado descrittivo, e
a che punto è la decisione?"**
Gradino già scritto: la riga D.13 STAGED (w/Γ trasportato, h0 profile-grade
con la vacuity Remark 4.1, TRIPLE monitor G6, audit AM, margine m_n).
Gradini successivi: path A (free-vortex carry — con la fork [T-N6-2] di
record: teorema SOLO su (rΓ, h0, s) uniformi, su campi stratificati serve
il lemma misto O il monitored-neglect armato dal TRIPLE), path B (engine +
adjoint five-field: core adjoint PROVEN in-panel, [S-5F] resta SCHEMA),
path C (procurement dati tangenziali — il corpus ha un VUOTO search-proven
sul campo tangenziale time-mean). Stato decisione: PENDENTE DI RECORD,
è una decisione utente a confine di sessione, non presa dal panel
(`DISPATCH_swirl5f.md:179-183`); la giustificazione quantificata esiste
(claim 8, St_n-conditional). Contesto di record che pesa sulla
decisione: l'aspettativa unanime di D.14 è che i dati RDE reali
generalmente FALLIRANNO la triple-uniformity e ruoteranno sulla macchina
field-level — "il mestiere del monitor è routing onesto, non
benedizione" (`phaseD_meanswirl_formalization.md:1294-1298`): un peso
dichiarato a favore dei gradini B/C e dell'urgenza della decisione
stessa.

**(3) "Cosa si perde facendo design per fasi assiali invece che 3D, e i
relativi pesi di ognuno?"**
La risposta di record è la FORCHETTA a sei canali
(`phaseD_r22f_centerpiece.md:1499-1506`): (i) time-coupling — zero
condizionale sulla classe certificata ([T-T0P], gap lists nominate), CLASS
EXIT senza numero nel worst; (ii) riduzione azimutale — il volto di K:
media nulla, on-ray single-digit % plausibile (fitted sheet), off-ray >10%
non escluso [SE]; (iii) contenuto swirl — B1 0.6–9% di p, B2 1.5–3% spinta
(fold), B5 10–14°, tutte [SE], marcatore worst-direction = shroud
Paxson-Miki (58.1→~71.5% dell'ideale, [REP]); (iv) adeguatezza ~1% a
livello SIZING [REP], soglia di RANKING OPEN (R26); (v) model-form: frozen
+6.3..+7.0% sull'istanza interna, base-pressure = ANALOGIA dichiarata;
(vi) optimum-shift: NESSUN numero a nessun grado (δ e L_H underived) — il
canale più tagliente atterra onesto. In più la lista chiusa E1–E11 di ciò
che nessuna macchina per-fase cattura, con la lettura zero-winding (le
sheet elicoidali interne entrano solo come ombra data-anchored). Nessuna
somma finta: i canali non si sommano; M-RED (famiglie F-c) è
l'aggregatore legittimo della SOLA coppia swirl (ii)+(iii) — stessa
fisica, seam dichiarata (`phaseD_r22f_centerpiece.md:1715-1722`); gli
altri canali hanno owner propri: (i) è conditional-zero G3/corrector-owned
(:449-457, :1722), (vi) compone con gli altri SOLO attraverso lo schema
delta/mu (:1724-1729).

**(4) "Dove sono le dimostrazioni until-dry di tutto questo e chi le ha
giudicate?"**
Tre catene, tutte su file. PIANO 1: 7 round r1–r7 (+r7.1) applicati in
place con ledger per-obiezione (§6-bis..§6-quinquies,
`phaseD_meanswirl_formalization.md:2693-3060`) — copertura giudici
dichiarata: r1–r3 = refutazioni applicate dall'autore, ledger-only,
senza giudice separato; il set r2-pass è giudicato da
`r2pass/VERDICT_r2pass.md` (downgrade J-r2p-2/3 tuttora vincolanti sulle
iff di D.18) COL SUO CAVEAT VINCOLANTE (verification layer UNPROVEN in
confirm direction, known-true seed FAILED: "nothing in this revision may
be cited as layer-certified", Blocco-2 landing gate CLOSED per il set
r2-pass, portato avanti verbatim fino a r7 — :92-96, :226-227); le
amendment r7.1 AM-1..AM-3 sono aggiudicate dal confirming-round judge
`r2pass/VERDICT_confirm.md` §4 (:229-238). Carrier
`phaseD_meanswirl_symcheck.py` PASS con rejector che spara. PIANO 2: 4 round × 3 lenti, 66 findings, 14 probe; closure judge
`blocco3/VERDICT_r22f.md` (NOT-DRY-AT-CAP, approved-for-landing, labels §1
= autorità unica) + escalation judge `blocco3/VERDICT_escalation_c4.md`
(E-1..E-4 DRY, E-5 0-BREAK unanime, 53/53 sustained). PIANO 3: 4 deriver +
4 refuter + giudice + judge-verifier sympy (10 agenti, ~2.0M token),
verdetto CONVERGED-WITH-THREE-NAMED-EDITS con le tre edit APPLICATE
(`DISPATCH_swirl5f.md:26-33, :140-152`). Tratto distintivo da mostrare: le
retraction sono NEL testo (contatore di over-certificazione a QUATTRO su
D.18; "the FORM is no longer the gap" ritirata; headline fitted-sheet
restaurata tre volte) — il processo rigetta davvero, non conferma.

---

## 5. Cosa deve dire il deck

1. **Un edificio, tre piani**: che cosa entra nello stato per-fase (2.5-D
   con swirl, D.1–D.20), che cosa si perde esattamente (operatore K
   esplicito, [T-RED]≡[MS-DEF-KRES]), quanto costa salire (swirl5f path
   A/B/C) — mostrare la saldatura testuale, non tre slide scollegate.
   [classe: struttura di record, ancore §1.5]
2. **La media è convicted, con i pesi**: nessun vincolo di record fissa
   E_θ data la pressione ([T-DISC-1] THEOREM*); separazione-J single-signed
   a booking level (THEOREM* scoped) con classe 1.5–3% spinta + B1 0.6–9%
   di p [SE — dichiarare la classe a voce].
3. **Il residuo di riduzione ha media nulla e due soli canali**: K̄ = 0
   (THEOREM*), (J)+(H), single-digit % plausibile on-ray con fitted sheet,
   >10% non escluso off-ray [SE]; il St² on-ray esiste ma è LICENSE-GATED —
   il deck NON lo banca.
4. **La forchetta onesta come artefatto**: sei canali, best/worst per
   canale, nessun referee esterno esiste, nessuna somma finta, e il canale
   optimum-shift SENZA numero (δ, L_H underived) — l'onestà è il punto di
   forza da mostrare a ESA, non una debolezza da nascondere. [per-cella,
   classi in tabella]
5. **Il monitor decide, non benedice**: TRIPLE monitor in TV con rejector
   G6; Γ-only falsamente licenzia (THEOREM); aspettativa dichiarata che i
   dati reali ruotino sulla macchina field-level. [THEOREM + PRACTICE]
6. **Due decisioni utente pendenti, dichiarate come tali**: S-5F build path
   (A con fork [T-N6-2] / B / C) e priorità C51 — il deck le presenta come
   candidates of record per la slide ASK, con la giustificazione
   quantificata [SE] e i pin bloccanti B-1/B-2 già pronti per la prima
   ingestione dati.

---

*(§6 STORIA: territorio W-B.2 — non scritto qui, numerazione riservata.)*

## 7. POSIZIONAMENTO / CONFORMITY (celle E-ii forma [V2-R6] + residuo E-iii) [W-B.1/B7]

### 7(a) STRUMENTI — mean-swirl / trasporto Γ = R·w sui CARRIER SURROGATI di record

Il posizionamento del trasporto di swirl per-fase (riga w/Γ del
contratto D.13, §1.2(a)) contro il precedente classico si fa — per
disciplina di record — su TRE carrier surrogati, non sul paper primario:

1. **D6 G5, riga di contenuto 2.2(f)** (D6 :803-806, verificata alla
   riga in finestra): "swirling-flow control-surface contouring —
   Tillyaeva Izv. AN MZhG 1975 no. 3 full-text check against T-N6-2's
   free-vortex closure". La riga è un DUTY del gate letteratura G5
   (scope extension PAN-S14), non un confronto eseguito: il record ha
   già nominato il check, non lo ha fatto.
2. **`kraiko_tillyaeva_2015`** (registry :498) = la GENEALOGIA: la
   scuola Kraiko-Tillyaeva possiede sia la catena moltiplicatori→
   certificati (LL-14, §3-bis) sia l'autrice del precedente swirling —
   il posizionamento passa per la scuola letta [IO/REP di riga], mai
   per il paper non letto.
3. **[T-N6-2] free-vortex come TERMINE INTERNO**: la chiusura
   free-vortex è già dentro la nostra macchina come carry di path A,
   con l'annotazione utente di record (DISPATCH_swirl5f.md:105-113,
   verificata alla riga): THEOREM SOLO sotto (rΓ, h0, s) UNIFORMI; su
   campi per-fase stratificati la combinazione NON è un teorema di
   record — fork lemma-misto vs monitored-neglect armato dal TRIPLE
   monitor (D.14), da presentare prima di ogni adozione.

**Confronto diretto con `wanted_tillyaeva_1975` = PENDING-PROCUREMENT
DICHIARATO** (registry :742-746, verificata alla riga): status WANTED,
paths [], russo [HARD] per INDEX.md, owner di riga "Next lit window —
N6-2 novelty bound; closest classical antecedent to our data class".
Regola vincolante di questa sezione: NESSUN summary del paper assente —
ciò che si può dire di Tillyaeva 1975 è SOLO l'identità della riga
registry e il duty 2.2(f) di G5; ogni claim di novità sul contouring
con swirl resta BOUNDED da questo procurement (lo dice l'owner stesso:
"novelty bound"). Fino al full-text check, lo slot slide corrispondente
porta la forma onesta "precedente candidato, non letto, procurement
aperto" — mai una posizione di merito.

### 7(b) SENSO [V2-R9] — i precedenti dell'edificio averaging 2.5-D

Che cosa fa il campo con le medie, senza struttura per-fase (ancora
CH5 §1.1, verificata in finestra): la prassi dei quattro paper del
corpus C4 è la **media GLOBALE** — campo mediato su tempo e fase in UN
solo stato steady equivalente, poi design classico su quello stato
(CH5:27-39, box di record): P-A rampa Angelino a input time-averaged,
P-B MoC max-thrust su UN singolo stato mediato globalmente con corner a
p_b mediato, P-C nessun design nuovo, P-D esplicitamente non
ottimizzato (CH5:52-71); comunanza C-1 "average-then-classical-design"
mai testata a livello di ranking (= la nostra questione aperta R26) e
C-5 "nessuno dei quattro è una riduzione per-phase" (CH5:73-80). Le
istanze quasi-1D del campo (blowdown 0-D per-phase LL-3, EAP rung
int-max LL-4 — righe del ledger, casa CH5/CH2) mediano senza operatore
di residuo.

Il gap che l'edificio occupa: il campo media SENZA contabilità di ciò
che la media perde; l'edificio dei tre piani mette accanto alla media
l'operatore di ciò che si perde (K esplicito, §1.3) e il suo prezzo
(forchetta, §1.3 PART 5). Guardia 16 (regola di classe), applicata a
questo enunciato: il canale MEDIO è coperto da teorema con perimetro
dichiarato — K̄ = 0 vale FIBERWISE su compositi BV periodici,
condizionale H-RED-2(SBV) (centerpiece :512-539) — e i canali RESIDUI
non coperti sono nominati con classe: (J) atomi/salti sui fronti
(primo ordine NON soppresso, delta underived — il tallone (J), guardia
1) e (H) covarianza/isteresi a.c. ([SE] per le scale, §2). Nessuna
gerarchia di gap si enuncia qui oltre questo perimetro.

### 7(c) STANDARD DI RIFERIMENTO (asse §C)

Asse governante: **§C-1 (copertura letteratura, classe PRISMA)** —
criterio di conformità: read-status onesto stampato (WANTED con paths
[], [IO]/[REP] per cella nella matrice lineage), claim di
assenza/novità SOLO query-bounded, procurement dichiarato con owner di
riga; il PENDING-PROCUREMENT Tillyaeva di §7(a) è l'istanza esatta
della disciplina (il confronto NON si fa finché la fonte non è letta).
Divergenza dichiarata: adottiamo la disciplina (query+flusso+status),
non la checklist PRISMA formale. Secondo asse citato: §C-2 (GRADE-class)
per le classi per-cella della forchetta (§2), mai sopra la loro classe.

**DECISION CARD C51 — non-aggiudicata** (obbligo emendamento v2.1 §1g
per le righe NEVER presentate; questo capitolo presenta la decisione
pendente in §1.4/§5.6):

| campo | contenuto |
|---|---|
| 1. scelta | C51 — solver wave-frame rung-3a: implicit BVP (freezing + Newton-Krylov, incumbent M0) vs MARCHING azimutale dell'orbita periodica (choice_ledger.yaml:706-714, status NEVER) |
| 2. alternative censite (data+fonte) | marching azimutale emerso BLIND dal formalizer PDE (mint 2026-08-17, VERDICT_contract_and_L4R1.md#D-5); input diretto appended 2026-08-19: swirl5f claim 6 (spacelikeness ≡ \|w_rel\| > c, loci di degenerazione ≡ kernel loci D.18 — verifier-confirmed, advisory) |
| 3. verdetto | **NON AGGIUDICATA** (sequenza del giudice stesso: aggiudicazione dovuta a implementation time, non prima) |
| 4. RECENCY/SOTA check | censimento datato 2026-08-17/19 (perimetro: blind-contract diff + panel swirl5f). **ATTUALE(perimetro: ledger C51 + DISPATCH_swirl5f, data-check 2026-08-23)** |
| 5. falsificatore / criterio | condizione di regime hyperbolicity-in-alpha: fuori dal regime \|w_rel\| > c il marching muore strutturalmente (cuore del criterio di decisione, nota di riga) |
| 6. trigger ri-esame (finestra) | rung-3a implementation window (owner di riga); la PRIORITÀ di C51 è decisione utente pendente di record (DISPATCH_swirl5f.md:100-101; §3 riga 2) — candidate per la slide ASK |

---

## Disposizione riparazioni (W-A, 2026-08-23)

Applicazione dei 12 finding di `REFUTE_CH7.md` (verdetto refuter:
REGGE-CON-RIPARAZIONI, 0 BREAK / 6 REPAIR / 3 GAP / 3 NOTE). Ogni ancora
citata ri-verificata alla fonte in questa finestra prima dell'uso
(read-then-quote: centerpiece :158-160, :201-206, :223-257, :272-289,
:426-430, :527-533, :1206, :1715-1729, :1783-1861; meanswirl :92-96,
:226-227, :229-238, :1130-1133, :1294-1298, :2472-2493; VERDICT_r22f
:526-531; DISPATCH :80, :86, :101-104; esistenza su disco di
`validation/sfoundations_raws_2026-08-13/r2pass/VERDICT_r2pass.md` e
`VERDICT_confirm.md` confermata via glob).

| # | classe | che cosa è cambiato | esito |
|---|---|---|---|
| 1 | GAP/MEDIA | §4 risposta (1): aggiunta la clausola di RILEVANZA della condanna col falsificatore del record (`phaseD_r22f_centerpiece.md:426-430`) — "real but priced irrelevant" se eps_fib < delta di design; peso relativo a K = misura congiunta M-RED F-c, pre-registrata | RIPARATO |
| 2 | REPAIR/MEDIA — **classificato ALTO dall'orchestratore, aggiudicato esplicitamente: ACCOLTO IN PIENO** (le tre omissioni (a)/(b)/(c) sono reali, verificate alle ancore :92-96, :226-227, :229-238; la domanda (4) chiede esattamente questa onestà) | §1.2(g) e §4 risposta (4): (a) caveat vincolante VERDICT_r2pass §1/§4 citato come parte del verdetto (layer UNPROVEN, "nothing... layer-certified", gate Blocco-2 CLOSED, carried verbatim fino a r7); (b) `r2pass/VERDICT_confirm.md` §4 nominato come giudice delle AM-1..AM-3 di r7.1; (c) distinzione dichiarata r1–r3 author-applied/ledger-only vs set giudicati (r2-pass, confirm) — "il giudice di batch NON copre la catena intera" | RIPARATO |
| 3 | REPAIR/MEDIA | §4 risposta (1): "errore NON VINCOLABILE" → "non vincolato da alcun vincolo di record", con falsificatore APERTO citato (:201-203) e la distinzione non-vincolato-dal-record ≠ impossibilità | RIPARATO |
| 4 | REPAIR/MEDIA | §4 risposta (1): frase di scope della gamba di segno — physical-h0-fixed (FOLD/compensato); ramo DROP non compensato geometry-signed, separazione ≡ 0 a r_e = r_in (:237-247); actual-pair NON asserita ad alcun grado, → M-RED B-2 (:248-257, :287-289) | RIPARATO |
| 5 | REPAIR/MEDIA | §1.1 e §1.5(3): saldatura 3 ri-dichiarata LETTURA DI ASSEMBLAGGIO del capitolo (non testuale), ancorata ai ponti reali B-1/B-2 → D.13 (`DISPATCH_swirl5f.md:80`, :86) e "3-stage upgrade path" (:101-102); "STAGED" restituito al suo significato di record (staged replacement text per M0 VI.1, :1130-1133) | RIPARATO |
| 6 | REPAIR/BASSA | §1.2(f): "ritirato due volte" → ritirato a r2 con DOPPIA refutazione ("refuted twice over", :2472-2488); correzioni r3 attribuite al candidato SOSTITUTO, fork di norma sul sostituto = decisione T-RED owner | RIPARATO |
| 7 | REPAIR/BASSA | §4 risposta (3): aggregatore M-RED scopato alla SOLA coppia (ii)+(iii) (:1715-1722); owner degli altri canali nominati ((i) G3/corrector :449-457; (vi) solo via schema delta/mu :1724-1729). §1.5(2) già correttamente seam-scoped: invariato | RIPARATO |
| 8 | GAP/BASSA | §3: clausola esplicita "selezione, non censimento" con puntatore alla lista completa (centerpiece §6 R-1..R-17 :1783-1861 + RES-CAP-1..6 `VERDICT_r22f.md:526-531`); aggiunte le righe R-12 (certified basin radius) e R-15/RES-CAP-4 (eps_U sampled-sup + ladder re-check, value-route cella (vi)) | RIPARATO |
| 9 | GAP/BASSA | §4 risposta (2): aggiunta l'aspettativa unanime di record D.14 (:1294-1298) col suo peso dichiarato sulla decisione A/B/C | RIPARATO |
| 10 | NOTE/BASSA | §1.2(g): "documentato con onestà rara" (comparativo non ancorato, guardia 9) → enunciato fattuale "documenta le proprie retraction NEL testo" | RIPARATO |
| 11 | NOTE/BASSA | §1.2(f) (prima occorrenza): path completo `validation/sfoundations_raws_2026-08-13/r2pass/VERDICT_r2pass.md` + avviso "sorella di phaseD/, non figlia"; occorrenze successive dichiarate abbreviazioni | RIPARATO |
| 12 | NOTE/BASSA | Nuova §1.6 "Glossa minima": on-ray/off-ray, fitted sheet, booking level, St_n — quattro definizioni di una riga, ognuna ancorata al sito di record (il glossario `docs/glossary.yaml` non porta queste voci: verificato via grep in finestra, quindi glossa in-capitolo e non pointer) | RIPARATO |

Bilancio: 12/12 RIPARATI, 0 declassati, 0 respinti. Guardie toccate:
G9 (finding 10, comparativo rimosso), G1/G2/G3 non ingaggiate dalle
edit (nessuna gerarchia di gap C-3bis, nessun claim rung/T1c aggiunto),
G4 non ingaggiata (nessun "campo" generico introdotto), G13/CT-6
invariati (nessun numero di paper aggiunto). Nessun nuovo id di
letteratura introdotto (tutte le ancore nuove sono file di record del
repo). Arco di consumo: questo capitolo riparato = base stabile per B7
(W-B.1) e per lo storico B8a; le sezioni §3-bis/§6/§7/DECK FEED restano
territorio W-B, non toccato.

---

## DECK FEED (asserzioni candidate-slide, assertion-evidence) [W-B.1/B7]

1. "Un edificio, tre piani: che cosa entra nello stato per-fase (2.5-D
   con swirl), che cosa si perde esattamente (operatore K esplicito),
   quanto costa salire (path A/B/C) — con le saldature esibite, non tre
   slide scollegate." — ancora §1.5; centerpiece :461-463 — classe:
   struttura di record (provenienze per-piano dichiarate).
2. "Il design su pressione media è convicted via fibre: nessun vincolo
   di record fissa E_theta dati (P, h0, s, mdot); pesi di classe
   1.5-3% spinta + B1 0.6-9% di p, dichiarati [SE]." — ancora
   centerpiece :150-206, :259-270 — classe THEOREM* (gamba di segno
   scoped) + [SE].
3. "Il residuo di riduzione ha media NULLA e due soli canali di primo
   ordine: (J) fronti (delta underived — il tallone si dichiara sempre)
   e (H) covarianza; SBV-conditional." — ancora centerpiece :512-539 —
   classe THEOREM* + guardie 1/16.
4. "La forchetta onesta a sei canali: best on-ray single-digit %
   plausibile (fitted sheet), worst off-ray >10% non escluso; il canale
   optimum-shift SENZA numero (delta, L_H underived) — l'onestà
   mostrata, non nascosta." — ancora centerpiece :1499-1506,
   :1731-1743 — classe per-cella (nessuna sopra la sua).
5. "Il monitor decide, non benedice: TRIPLE monitor in total variation;
   un monitor Gamma-only licenzierebbe il falso; aspettativa dichiarata
   che i dati reali ruotino sulla macchina field-level." — ancora
   meanswirl :1210-1304, :1306-1367, :1294-1298 — classe THEOREM
   (clause 1) + SCHEMA (gap licenziante) + PRACTICE.
6. "Il confronto col precedente classico più vicino (Tillyaeva 1975) è
   PENDING-PROCUREMENT dichiarato: WANTED, russo [HARD], owner nominato
   — la slide porta la forma onesta, mai un summary del paper
   assente." — ancora registry :742-746; D6 :803-806 — classe:
   disciplina §C-1 (read-status di record).
7. "Il cugino pubblicato più vicino è Fievisohn (wave-frame rotational
   MoC, [IO] dal method-paper 2017): mai design, mai famiglia per-fase
   — il quoziente esiste nel campo, l'edificio no." — ancora LL-13;
   matrix part2:443-500 — classe [IO] con riga nozzled [REP]-bounded.
8. "Due decisioni utente pendenti presentate come ASK: S-5F path A/B/C
   (con la fork [T-N6-2] su path A) e priorità C51 (card
   non-aggiudicata stampata)." — ancora DISPATCH :100-113; §7 card
   C51 — classe: decisioni pendenti di record.
