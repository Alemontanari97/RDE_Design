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

La saldatura non è narrativa a posteriori: è scritta NEI file. Il piano 2
definisce il suo operatore K dichiarando "distributional form is
[MS-DEF-KRES] of record" — cioè D.18 del piano 1
(`phaseD_r22f_centerpiece.md:461-463`); la forchetta consuma le classi di
bias B1–B5 del piano 3 nelle celle (ii)/(iii)
(`phaseD_r22f_centerpiece.md:1502-1503`); la scaletta descrittiva del piano 3
(path A/B/C) è l'estensione della riga di contratto STAGED D.13 del piano 1
(`phaseD_meanswirl_formalization.md:1130-1156`;
`DISPATCH_swirl5f.md:99-116`).

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
(J-r2p-2/J-r2p-3, `r2pass/VERDICT_r2pass.md`), path di restauro = batteria
G-f (:2610, colonna classe). S.22 [MS-S-KBOUND] è il TARGET statement del
bound del residuo (SCHEMA; il candidato-norma r1 RITIRATO due volte con le
ragioni scritte — atomi di K sui fronti, cono avvolto azimutale — e la
fork di norma registrata come decisione del T-RED owner, :2464-2507).

**(g) La catena until-dry del piano 1** (il "chi lo ha giudicato"): SETTE
round di refutazione avversaria applicati IN PLACE, r1–r7 + r7.1
(header blocks :24-248), con ledger per-obiezione §6-bis..§6-quinquies
(:2693-3060) e giudice di batch `r2pass/VERDICT_r2pass.md` di record. Il
processo è esso stesso documentato con onestà rara: quattro
over-certificazioni consecutive dell'assembly D.18 ANNOTATE con contatore
(:209-211), interruzione r5 riconciliata su file (:128-138), false-completeness
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
3. **La scaletta descrittiva è una sola**: D.13 STAGED (+w/Γ, h0
   profile-grade, TRIPLE, AM audit, m_n) = il gradino già scritto;
   path A/B/C = i gradini successivi, con la fork [T-N6-2] sul path A e la
   decisione utente pendente.
4. **Il metodo di lavoro è lo stesso sui tre piani**: staging → refutazione
   until-dry → giudice → absorption targets (§7 piano 1; landing list
   VERDICT_r22f §7 piano 2; registration duty §7 dispatch piano 3), con la
   regola di consumo "panel grades are not record grades" e i mint
   (sector-decomposition F-2, K̄ = 0) che RIDONO la landing window invece di
   auto-promuoversi.

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
| Convessità KS-margin-set a S* margin-active (R-14/RES-CAP-3) + gate O1 (R-13) | F2 / F4b theory WP |
| G-b1 lemma di sensitività del TRIPLE monitor (+ G-b2 tol per campagna) | N6 §5 line; gate di OGNI uso licenziante di D.14 |
| G-a check simbolico D.6/D.20-fronti; G-f batteria completezza D.18 (restaura le iff da SCHEMA) | task promozione D.6 (F2); carrier upgrade G-f |
| G-e vuoto empirico: NESSUN falsificatore §3 (F1–F4, A4) mai calcolato nel corpus | prima ingestione dataset (pin B-1/B-2 BLOCCANTI prima) |
| E5 magnitudine (Δx_s standoff) | misura dedicata (G-e/O5 window) |
| Pin bloccanti B-1 (normalizzazione A4) e B-2 (convenzione h0) nel testo D.13 | D.13/prima ingestione — BLOCKING |
| Assenza referee esterno per l'errore di spinta per-fase (dichiarazione strutturale forchetta) | si chiude SOLO con R22-CFD nostro o procurement (R-8 per la base-pressure) |
| Absorption non ancora eseguita: i tre piani sono raws/advisory UNTRACKED; landing list = VERDICT_r22f §7 + VERDICT_escalation_c4 §6 + dispatch §7 | orchestratore, landing window (R7/SR-6) |

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
[SE]. Ciò che si PERDE trattenendo lo swirl nel modello 2.5-D è invece
esattamente l'operatore K (sei righe + atomi) — di media nulla (K̄ = 0
THEOREM*), due soli canali di primo ordine, single-digit % plausibile
on-ray con fitted sheet, >10% non escluso off-ray [SE]. Guadagno netto:
si scambia un errore NON VINCOLABILE e invisibile alla media con un residuo
NOMINATO, a media nulla, misurabile (M-RED) e con la scaletta per ridurlo.

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
(claim 8, St_n-conditional).

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
somma finta: i canali non si sommano, l'aggregatore legittimo è M-RED.

**(4) "Dove sono le dimostrazioni until-dry di tutto questo e chi le ha
giudicate?"**
Tre catene, tutte su file. PIANO 1: 7 round r1–r7 (+r7.1) applicati in
place con ledger per-obiezione (§6-bis..§6-quinquies,
`phaseD_meanswirl_formalization.md:2693-3060`), giudice di batch
`r2pass/VERDICT_r2pass.md` (downgrade J-r2p-2/3 tuttora vincolanti sulle
iff di D.18), carrier `phaseD_meanswirl_symcheck.py` PASS con rejector che
spara. PIANO 2: 4 round × 3 lenti, 66 findings, 14 probe; closure judge
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
