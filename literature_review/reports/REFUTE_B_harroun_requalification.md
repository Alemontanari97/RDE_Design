# REFUTE_B — Attacco alla requalifica "minaccia Harroun" (STAGE 4 — ADDENDUM 2 di VERIFICATION_FABLE_2026-08-13.md)

RUOLO: refuter avversariale, default = tesi sbagliata/auto-indulgente finché non regge.
FONTI LETTE DIRETTAMENTE (mai riassunti): Harroun 2021 PDF pp.5-8 e 9-13 (journal pp.664-672:
framework computazionale, Eq. (7), Fig. 17, Fig. 21, Eq. (10), Table 3, Fig. 22, Conclusions);
Stechmann JSR 56(3) pp.888-890 (§II: Eq. 1-14, assunzioni 1-4); M0 righe 510-760
([T-T3] con H1-H4, Lemma A/B/C, [T-T3-SI], [T-T3-MAP] breaker (a)-(e), PROTOCOL T3-CONTROL,
Harroun clause of record).

TESI SOTTO ATTACCO (testuale): "Il valutatore cieco di Harroun (c_F=1.25 per entrambi gli
aerospike) è la PROIEZIONE scalare-uniforme della nostra costruzione (snapshot 2-D a pressione
costante lungo un waveform 0-D alla Stechmann, media mass-weighted) — un membro della classe
T3-CONTROL la cui povertà informativa la NOSTRA teoria PREVEDE. La cecità non trasferisce
formalmente al nostro valutatore (stati di fase risolti in caratteristica). Restano: il
fatto-opportunità che i valutatori del campo sono ciechi; la non-dimostrazione che il nostro
discrimini al percento; il rischio condiviso della riduzione 2-D-per-fase."

---

## FATTI DI RECORD STABILITI SULLE FONTI (base di ogni verdetto)

F1. **Il valutatore di Harroun è VISCOSO e ambient-coupled.** Il framework è NASA Loci/CHEM,
Navier-Stokes con flussi viscosi F_v (Eq. 1-2, p.664), turbolenza Menter k-omega BSL + Sarkar*
(p.664), pareti adiabatiche NO-SLIP, mesh raffinata a y+=1.0 (p.665); dominio inizializzato a
1 atm sea-level, far-field P=1 atm / outlet 0.998 atm (Fig. 8, p.665). "All computations were
nonreacting" con gas reale non-calorico (cp(T) CHEMKIN, poly 4° ordine, p.664) — nemmeno H1/H1-C
è soddisfatta in senso stretto. Le simulazioni const-p per fase (§III.C p.670: "A series of
axisymmetric simulations of both the IE and flared geometries ... at different constant-pressure
inflow conditions spanning the pressure ratios of the detonation-wave cycle") vivono nello stesso
framework; la separazione È risolta per fase (p.670: "for the constant-pressure inflow case, once
enough time had passed for the flow to separate from the nozzle, the boundary layer reached a
quasi-steady-state condition"; Fig. 18 "Separated flow region").

F2. **Il waveform NON è "alla Stechmann" e la media NON è dichiarata mass-weighted.** Eq. (7)
p.666: P(θ) = −6.22 ln(θ/180 · 1/f) − 57.04 atm — decadimento LOGARITMICO, curve-fit da un CFD
2-D "unwrapped" precedente [27], calibrato su CTAP test 53 + rapporto di detonazione CEA; due
onde, 13.800 Hz; inflow a T UNIFORME 3400 K, "the incoming flow was not rotating and had no
vorticity" (p.666). Stechmann Eq. (13) è invece un ESPONENZIALE P_c(t)=P_R·P_init·e^(−λt)
(p.890) e la sua media mass-weighted è Eq. (4) (p.888). Harroun p.671 dice solo "averaging the
discrete constant-pressure axisymmetric computations for each point in time of the cycle":
NESSUN peso stampato. M0:713-715 registra già di record: "Harroun's averaging convention is
UNDECLARED (choking advisory 3-bis) so comparisons are ill-posed until a convention is pinned".
**La clausola "media mass-weighted" della tesi è un'importazione non verificata che CONTRADDICE
il registro del progetto stesso.**

F3. **Il pareggio è "roughly the same", arrotondato, su un totale dominato da un termine
condiviso.** p.671: "estimated the coefficient of thrust for both the IE and flared aerospike to
be 1.25; thus, the performance ... was estimated to be roughly the same for either design" —
tre cifre, nessuna barra. C_F = F/(P_c A_t) (Eq. 10) include la spinta al piano d'ingresso,
identica per costruzione tra le due geometrie (portata e waveform imposti uguali); i contributi
geometrico-sensibili (plug+cowl, Fig. 21) valgono |C_F| ≤ ~0.35, cioè una frazione minore del
totale 1.25. Il pareggio a 3 cifre vincola le differenze, non le annulla.

F4. **Le curve c_F(NPR) sono diverse, non-affini, e si incrociano.** Fig. 21 (lettura visiva
[IO], NPR 2-30): IE plug satura a ~+0.32, flared plug a ~+0.19, IE cowl NEGATIVO ~−0.1 su tutto
il range, flared cowl ~+0.05; le somme per geometria si incrociano (flared meglio a NPR basso,
IE meglio a NPR alto). La non-affinità ha una causa fisica documentata NEL paper: transizione
open-wake/closed-wake a NPR ≈ 6.7 (Fig. 17, p.669) e separazione a NPR bassi — fisica di base
region/ambiente che nessuna famiglia affine F = aP_c − P_a·b può rappresentare.

F5. **Le ipotesi di M0 [T-T3] (righe 518-523):** H1 un gamma frozen comune; H2' parete fissa,
FULL-FLOWING, uscita supersonica a OGNI fase (interno ambient-blind); H3 forma d'ingresso
adimensionale fase-indipendente; H4 unicità per fase; P_a COSTANTE (non necessariamente nulla:
l'affinità di Lemma C assorbe P_a costante); vincoli geometrici condivisi. La costruzione di
Lemma A è inviscida (BC di slip nominata a M0:540; il termine viscoso ∇·τ con μ=μ(T) rompe
l'omogeneità di grado 1 in k a (u,T) fissi — la similarità di scaling muore per flusso viscoso).
M0:660-664 (breaker (a)): "a mu-positive SEPARATED phase kills H2' and the affinity — collapse
dies even for J [SCHEMA]"; "separation is viscous, the machinery inviscid".

F6. **Ciò che T-T3 predice quando vale**: J[Σ] = F[Σ; <Pc>_μ] PUNTUALMENTE sullo spazio delle
forme (M0:524-526) — il collasso è sulle FASI a geometria fissa. Il valutatore collassato
F[·; <Pc>] è un valutatore steady classico PIENAMENTE discriminante tra geometrie. Il teorema
non enuncia da nessuna parte la degenerazione tra GEOMETRIE diverse.

---

## LINEA (1) — "LA NOSTRA TEORIA LO PREVEDE": **REFUTED**

La clausola portante della tesi è un DOPPIO abuso del teorema.

(1a) **Fuori ipotesi.** Il valutatore cieco di Harroun non è un membro della classe di collasso:
è RANS viscoso (F1: fuori dal frame inviscido in cui vive Lemma A/H4, F5), ambient-coupled con
base region e transizione di wake (F4: H2' "ambient-blind interior" violata), con fasi SEPARATE
a NPR basso (F1: H2' "full-flowing" violata su un insieme μ-positivo — esattamente il breaker
(a) che M0 dichiara UCCIDERE il collasso perfino per J), e gas non caloricamente/termicamente
frozen-γ uniforme (F1). Precisazione contro lo stesso brief d'attacco: P_a≠0 costante NON basta
da solo a rompere il collasso (Lemma C lo assorbe: J = a<Pc> − P_a·b, e c_F(NPR) = a/A_t −
P_a·b/(P_c A_t) varia con NPR pur restando F affine — la media È il valore alla media). Ciò che
rompe la stretta collassabilità è la NON-AFFINITÀ di F(P_c) prodotta da wake/separazione/
viscosità (F4) — e quella c'è, documentata (Fig. 17, Fig. 20). Quindi: la famiglia proiettata
di Harroun NON collassa strettamente, e attribuire la sua "povertà" al nostro teorema è usare
il teorema dove il nostro stesso registro dice che muore.

(1b) **Oggetto sbagliato anche DENTRO le ipotesi.** T-T3 predice il collasso sulle fasi, non la
cecità tra geometrie (F6). Il pareggio 1.25=1.25 è una degenerazione tra GEOMETRIE — un oggetto
su cui il teorema tace. In-ipotesi, due geometrie con (a_1,b_1)≠(a_2,b_2) pareggiano solo sul
luogo di codimensione 1 a_1<Pc>−P_a b_1 = a_2<Pc>−P_a b_2: un incrocio accidentale a quel <Pc>,
non una "povertà della proiezione". La teoria predice semmai che il valutatore medio ha
ESATTAMENTE il potere discriminante del valutatore steady a <Pc> — che povero non è.

(1c) **"Membro della classe T3-CONTROL"** è inoltre un uso improprio del registro: T3-CONTROL
(M0:734+) è un PROTOCOLLO di controllo pre-registrato (classe PRACTICE), non una classe di
valutatori; e la Harroun clause of record (M0:727-732) impone già la lettura "corner reading,
NOT an identification of Harroun's methodology with the formal tier-1 lab".

**Forma onesta sopravvissuta:** la proiezione p-only-uniforme scarta esattamente il contenuto
per fase che la nostra breaker map cataloga (θ, covarianza T-M, swirl, struttura wave-frame) —
questo È di record. Ma "la teoria PREVEDE la sua povertà informativa" no: fuori ipotesi la
teoria non parla, e in ipotesi prevede il contrario di una cecità tra geometrie.

## LINEA (2) — Coincidenza-di-misura vs povertà-della-proiezione: **TIENE (l'attacco); la tesi ne esce INDEBOLITA + 1 errore fattuale**

Il pareggio è l'uguaglianza (ARROTONDATA, F3) degli integrali di due curve c_F(NPR) DIVERSE e
INCROCIANTI (F4) sotto UNA misura: il waveform log Eq. (7) del test 53 a 13.800 Hz, con
convenzione di peso NON dichiarata (F2). Con curve che si incrociano, un waveform diverso
(P_R diverso, onda singola, fill diverso — cioè un'altra distribuzione di residenza in NPR)
genericamente rompe il pareggio e PUÒ invertire il ranking: è il canale di inversione
d'ordinamento già registrato (M0 T-T3-MAP(e), A26/A33; "every collapse-adjacent theorem
statement carries its convention and matching"). La lezione primaria del dato è dunque la
FRAGILITÀ DELLA CONVENZIONE DI MEDIA — che tocca ANCHE noi via la scelta di μ e del matching
(grado di libertà registrato; il protocollo T3-CONTROL impone ENTRAMBI i pesi proprio per
questo). La lettura auto-assolutoria "povertà della proiezione, come previsto" nasconde questa
metà della lezione ed è quindi indebolita nella sostanza.

**Errore fattuale della tesi (da correggere):** "media mass-weighted" — non stampata in Harroun
(F2), convenzione UNDECLARED per M0:713-715. L'attribuzione va rimossa o degradata a inferenza
via Stechmann Eq. (4), citando che il paper non la dichiara. Anche "waveform 0-D alla
Stechmann" va precisato: Eq. (7) è un log-fit da CFD unwrapped [27], non l'esponenziale
Eq. (13) di Stechmann.

**Riserva onesta a favore della tesi:** il pareggio è "roughly the same" a ~3 cifre su un totale
dominato dal termine d'ingresso condiviso (F3) — chiamarlo "uguaglianza di integrali" è
sovra-preciso in ENTRAMBE le direzioni; resta però vero che un solo numero aggregato sotto una
sola misura non può testimoniare né povertà strutturale né equivalenza delle geometrie. La
risoluzione del punto (misura alternativa ⇒ ranking diverso?) è decidibile solo con i dati
della tesi di Harroun (R2, P0 di record) o con R22.

## LINEA (3) — Il potere di ranking dell'informazione per fase: **INDEBOLITO (forma ristretta obbligatoria)**

Nessuna evidenza nel nostro impianto — numero, esperimento o teorema — mostra il nostro
aggregato separare due design che un valutatore p-only pareggia. Peggio per la tesi: l'evidenza
in-corner punta CONTRO. Nel corner tier-1 il collasso stesso PROVA che l'informazione extra non
muove l'aggregato (T-T3-SI: Isp fase-costante, uguaglianza di valore per OGNI ν; misura S18:
twin agreement +0.04%, corner measurement M0:719-726). Quindi il potere discriminante extra può
vivere SOLO nei canali breaker ((b) mixture form, (c) swirl-KE, (d) patch subsoniche,
(e) convenzioni) — esattamente dove il nostro impianto è a grado THEOREM*/SCHEMA/CONJECTURE,
non THEOREM. La tesi lo concede al punto (b) ("resta NON DIMOSTRATO") ma la retorica della
frase portante ("stati di fase risolti in caratteristica") INSINUA il trasferimento
informazione→ranking che non è stabilito. Forma corretta: "il nostro valutatore PORTA
l'informazione la cui assenza definisce la classe cieca; che quell'informazione muova il
ranking AGGREGATO al percento è esattamente R22 (aperto, P0); nel corner tier-1 la teoria
stessa prova che non lo muove."

## LINEA (4) — Rischio inviscido oltre al 2-D: **TIENE (l'attacco); la lista dei rischi condivisi era incompleta**

La fisica che separa i due aerospike negli esperimenti (Table 3, Fig. 22: separazione sul
flared a x≈5 cm nei casi low/mid; "drastic influence of the cowl on the flowfield", p.671) e il
meccanismo centrale del paper (ritardo di separazione da rinnovo del boundary layer ogni 72 μs,
Eq. (9) δ_m = 2√(μt_res/ρπ), p.670) sono VISCOSI, 3-D e con MEMORIA tra fasi. Le nostre marce
per fase sono meridionali, INVISCIDE e quasi-steady. Tre rischi distinti, non uno:
 (i) 2-D-per-fase — CONDIVISO con Harroun (i loro stessi autori lo incolpano, p.671);
 (ii) INVISCIDO — **NOSTRO e NON condiviso**: il valutatore "povero" di Harroun è RANS viscoso
 e la separazione la VEDE per fase (F1); il nostro no. Su questo canale l'ordinamento
 informativo della tesi si INVERTE;
 (iii) QUASI-STEADINESS per fase — CONDIVISO: il meccanismo residence-time è un effetto di
 memoria tra fasi invisibile a QUALUNQUE valutatore steady-per-fase (loro e nostro); è il
 canale che R22(b)-vs-(c) deve isolare.
Corollario che colpisce la clausola "PROIEZIONE": il loro valutatore è la proiezione del nostro
SOLO nel canale dei dati d'ingresso (p-only uniforme vs traccia s(ξ) risolta); nel canale del
campo è un SOVRAINSIEME (viscoso, turbolento, ambient-coupled, base flow). I due valutatori
sono informationalmente INCOMPARABILI, non ordinati per proiezione. La parola "proiezione"
senza questo qualificatore è falsa.

---

## VERDETTO COMPLESSIVO: **REFUTED nella clausola portante; sopravvive solo in forma ristretta**

- Linea (1) REFUTED — "la nostra teoria lo prevede" = abuso del teorema fuori dalle sue ipotesi
  (viscoso, separato, ambient-coupled = breaker (a) di M0) E oggetto sbagliato dentro le ipotesi
  (il collasso è sulle fasi, non tra geometrie).
- Linea (2) TIENE — il pareggio è una coincidenza-di-misura arrotondata sotto convenzione non
  dichiarata; la lezione primaria è la fragilità della convenzione di media, che tocca anche la
  nostra μ; errore fattuale "mass-weighted" da rimuovere (contraddice M0:713-715).
- Linea (3) INDEBOLITO — nessuna evidenza di potere di ranking del nostro aggregato; in-corner
  la teoria prova il contrario; forma ristretta obbligatoria, R22 decide.
- Linea (4) TIENE — il rischio inviscido va aggiunto (nostro, non condiviso: il loro valutatore
  la separazione la vede) più la quasi-steadiness per fase (condivisa); "proiezione" vale solo
  nel canale inflow, i valutatori sono incomparabili.

## FORMULAZIONE CORRETTA DI RECORD (proposta al panel)

"Il valutatore quasi-cycle-averaged di Harroun (c_F ≈ 1.25 per entrambi gli aerospike, 'roughly
the same', p.671) coincide con la proiezione scalare-uniforme della nostra costruzione SOLO nel
canale dei dati d'ingresso (waveform p-only Eq. (7) — log-fit da CFD unwrapped [27], T uniforme
3400 K, zero swirl; convenzione di media NON dichiarata, M0 T-T3-MAP(e)); nel canale del campo
è più ricco del nostro (RANS k-ω ambient-coupled, separazione risolta per fase): i due
valutatori sono informationalmente incomparabili. Il pareggio 1.25=1.25 NON è un'istanza del
collasso T-T3 (setup fuori H2'/inviscido: fasi separate = breaker (a); wake open/closed non
affine, Fig. 17) né una sua predizione (il collasso è sulle fasi a parete fissa, non tra
geometrie): è una coincidenza-di-misura arrotondata tra due curve c_F(NPR) diverse e incrocianti
(Fig. 21) sotto UN waveform — un'istanza del canale di fragilità della convenzione di media che
tocca anche la nostra scelta di μ (T3-CONTROL, entrambi i pesi, obbligatorio). Restano di
record: (a) il fatto-opportunità che i valutatori del campo usano dati d'ingresso p-only/0-D
per fase; (b) il potere discriminante al percento del nostro aggregato NON dimostrato — e
provato NULLO nel corner tier-1 — decisione a R22; (c) TRE rischi: 2-D-per-fase (condiviso),
quasi-steadiness per fase (condiviso), inviscido (nostro, non condiviso)."

## LIMITI DICHIARATI DI QUESTA REFUTAZIONE
- Le letture di Fig. 21/Fig. 17 sono visive [IO] (nessuna tabella nel paper); i valori ~0.32/
  ~0.19/−0.1/+0.05 e l'incrocio delle somme sono stime da grafico.
- L'identità del solver per le simulazioni const-p per fase (§III.C) con il framework viscoso
  §II.C è fortemente implicata dal testo ("All computations", stesso studio) ma non ristampata
  in §III.C.
- La convenzione di media di Harroun POTREBBE risultare mass-weighted nella tesi M.S. 2019
  (R2, P0): in tal caso cadrebbe l'errore fattuale F2 della tesi, ma NESSUN verdetto di linea
  cambierebbe (nessuno poggia sul peso specifico).
