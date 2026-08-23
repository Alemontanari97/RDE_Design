# REFUTE_CH1 — Verdetto avversariale su CH1 (Formulazione e ladder)

Refuter S-PRES, 2026-08-23. Anchor walk eseguito al 100% dei claim load-bearing:
aperte e lette nella finestra M0:100-169, 440-461, 530-646, 985-1002, 2294-2352,
2812-2896, 2965-2979, 4200-4239; claims_registry:316-392, 1898-1924;
problem_book:518-575; P1_sections_5_7:60-109; findings_registry:1445-1458;
literature_map:14-31, 70-97; literature_registry:555-577; theorem_ledger
(sharpness, :350-356). Esito del walk: le ancore citate dal capitolo REGGONO
alla classe dichiarata in tutti i casi salvo i finding sotto; nessun claim cade.

## Tabella finding

| # | sito (riga capitolo) | classe | severita' | testo | fix proposto |
|---|---|---|---|---|---|
| 1 | §1.3 r.70-73; §3.1 r.211-216; Q5 r.321-328; Q6 r.330-337 | REPAIR | ALTA | Stato [S-T0P]/[T-T0P] SOTTO-RIPORTATO e boundaries mancanti. Il capitolo si ferma alla "meta' di equivarianza [T-T0P-E] THEOREM", ma M0:602-628 registra il MAIN STATEMENT [T-T0P] ATTERRATO (2026-08-19: steadification + canonicity, SCHEMA su entrambi gli strati, split gap lists G1-G12) con TRE boundaries di record che il capitolo non porta: (a) quantificatore ristretto alla classe t-periodica (l1-F2, M0:614-616); (b) conclusioni solo su cl(Omega_march); (c) SOLO istanze SLIP-FREE — e M0:618-619 dichiara testualmente "the excluded slip sheets are the physically generic RDE front type". Un esperto RDE ostile gioca ESATTAMENTE questa carta su Q5/Q6 (gli scarichi RDE sono pieni di slip lines) e il capitolo non ha la risposta pronta. | Aggiornare §1.3/§3/Q5/Q6: stato landed del main statement + i tre boundaries dichiarati; risposta pre-cotta al banco: "il teorema di steadificazione esclude le slip sheets per pricing G9 dichiarato; la restrizione e' di record, non nascosta; carrier owed [X-T0P], owner F2". |
| 2 | Q1 r.250-254; §5.6 r.363-367 | REPAIR | ALTA | Il datum +0.51% e' citato con lista caveat INCOMPLETA: manca la BAND-UNDERINCLUSION di record (M0:4216-4219: "class-representation error saturates M -> 2M and is under-covered by the M-vs-2M J-difference; crude systematic bound ~6e4") — cioe' un bound sistematico grezzo ~6e4 contro un surplus 2.0407e5 (~30%). Se il numero va su slide, quel caveat E' parte del numero (R5). | Aggiungere il caveat band-underinclusion (con il ~6e4 vs 2.0407e5) sia alla risposta Q1 sia al punto §5.6; il claim cap gia' citato resta. |
| 3 | Q1 r.248-250 | DOWNGRADE | MEDIA | "nella classe di collasso T3 la differenza e' ZERO per teorema" e' sopra-classe: per [T-T3-MAP] (claims:320, citato dal capitolo stesso in §1.5(v)) la coincidenza cycle-vs-steady e' "refuted as a general theorem and proved on the tier-1+vacuum corner (T-T3-SI)"; P1:96-104 prova solo il collasso del PESO w nella classe T3 (la trasversalita' pesata si riduce alla media naive), non l'identita' dei due programmi in tutta la classe. | Riformulare: "ZERO per teorema sul corner provato (T-T3-SI, tier-1+vacuum); nella classe T3 il peso e' fase-indipendente e (**') collassa alla media naive (P1:96-104)". |
| 4 | Q4 r.310-313 | REPAIR | MEDIA | La STRICTNESS (max Int < Int max) non ha prova SCRITTA nel record: M0:2316-2319 la enuncia come clausola di sharpness DOPO il QED (r.2315) e theorem_ledger:351-356 la ripete, sempre senza prova; nemmeno l'ipotesi implicita mu({xi: l(xi) > L}) > 0 e' enunciata. La risposta Q4 ("e' la clausola di sharpness dello stesso teorema, stesso scope") lascia intendere copertura dalla prova del nesting — che copre solo la parte positiva. | Risposta onesta al banco: "il nesting e' provato (M0:2303-2315 QED); la strictness e' clausola enunciata di record senza prova scritta; il carrier quantitativo e' PB-2 (OPEN)". Eventuale write-up della strictness = finding da mintare, non da riempire qui. |
| 5 | §1.1 r.28-31 | REPAIR | MEDIA | La narrativa usa la forma PLANAR-ONLY del certificato L4 ("ogni patch assialmente supersonica con margine"). Il certificato di record e' la forma NORMALE-MERIDIANA m_n := u . n_m - c >= delta + SPLIT (M-a)/(M-a'), con R1 condizionata alla finestra W1-W4 (M0:139-169); il "u_x - c" nudo su Gamma_d curva puo' licenziare una marcia ill-posed (tilted-element counterexample, M0:151-153). La tabella §2 cita L4-CERT come carrier ma la narrativa — quella che finisce sulle slide — porta la forma superata. | Una riga in §1.1: forma m_n di record + split certificate + finestra R1; "assialmente supersonica" solo come caso planare. |
| 6 | globale (Q1 r.248, r.251; §1.2 r.49; §1.4 r.90; §3.2 r.219; §1.5) | GAP | MEDIA | Comprensibilita' non-esperto: il capitolo usa senza definire T3/"classe di collasso" (che cos'e' il collasso: parete fissa -> Rao a <Pc>, litmap:20), rung 1/2/3 (usati in §1.2 PRIMA delle ladder bridges di §1.4), classe S1, "Table-1 states", "rappresentante DEF" (un panelist non sa che DEF = costruzione GENO di riferimento a 9 dof). Per il consumo storyboard/Q&A la storia non e' auto-contenuta. | Glossario di 5-6 righe in testa al capitolo (T3, S1, rung 1/2/3, DEF, Table-1) o definizione inline al primo uso. |
| 7 | §1.2 r.41-42 | NOTE | BASSA | "il punto dove vive TUTTA la pratica di progetto pubblicata del campo" e' un quantificatore universale ancorato a M0:122-124, che NON lo contiene (la ladder e' solo definita li'). Il supporto reale e' litmap:23 riga G5 ("All published MOC RDE designs average first, design second") — claim di survey, query-bounded. | Spostare l'ancora su litmap:23 e marcare la frase come [REP survey / query-bounded], come il capitolo gia' fa correttamente in Q2. |
| 8 | §3.1 r.211-216 | NOTE | BASSA | La riga findings `theory:s-t0p-proof-writeup-pending` porta un code-anchor STALE (findings_registry:1455 cita M0:463-498; il blocco [S-T0P] vive a M0:533+) e pre-data l'atterraggio del main statement (2026-08-19). Non e' difetto del capitolo, ma il deck non deve ereditare l'ancora stale ne' presentare come interamente owed cio' che e' parzialmente landed. | Nel capitolo: riconciliare esplicitamente cosa RESTA owed (write-up S1-level + batteria [X-T0P]) vs cosa e' landed (main statement con quantificatore t-periodico); segnalare la staleness del registry come manutenzione (fuori scope S-PRES). |
| 9 | §5.2 r.346-349 | NOTE | BASSA | "l'unica approssimazione della catena e' O(St)" su slide, accanto a uno stage-1 landed con restrizioni (t-periodic, slip-free, cl(Omega_march)): il wording di M0:444-450 e' scoped alla catena di formulazione (rung-2), ma il banco puo' giocare le condizionalita' stage-1 come "approssimazioni non dichiarate". | Sulla stessa slide: "unica approssimazione della CATENA DI FORMULAZIONE = O(St) (M0:444-450); le condizionalita' dello stage-1 sono ipotesi DICHIARATE del teorema, non approssimazioni" — con la lista breve. |

## Banco utente (sezione 4) — esito per domanda

- Q1 (fixed-(eps,L) vs Li-Xu mean-BC): struttura e ancore VERIFICATE (P1:72-94,
  :66-70; M0:2840-2845; quarantena Li-Xu litmap:79-91 correttamente portata).
  REGGE CON RIPARAZIONI: finding 2 (caveat banda) + finding 3 (scope del "ZERO
  per teorema").
- Q2 (cosa portiamo se P-B applica Rao a input mediati): REGGE. Le tre cose
  (T-T7RED/T-T4 come "quando l'assioma e' un teorema", sharpness/PB-2, sistema
  (**')) sono tutte ancorate e alla classe giusta; la chiusa e' onesta e non
  evasiva.
- Q3 (forma esatta del claim di novita'): REGGE — la migliore sezione del
  capitolo. Formulazione bloccata D-06 verbatim (M0:2320-2322), Efremov-Kraiko
  con pagina (M0:2324-2330), K-O 1970 (M0:2331-2338), lista caveat estesa e P0
  non letti dichiarati. Nessun finding.
- Q4 (prova e scope di max Int < Int max): REGGE CON RIPARAZIONE: la
  distinzione nesting/strictness c'e', ma va detto che la strictness e'
  clausola SENZA prova scritta di record (finding 4). Il quantitativo OPEN e'
  dichiarato correttamente.

## Overclaim scan

Nessun numero senza provenienza: +0.51%/2.0407e5/38x (M0:4212-4216),
0.04-0.34% (literature_registry:568, CT-6 rispettato, "numeri loro"),
Li-Xu +11.3%/27.6% non usati dal capitolo. Novita' sempre query-bounded
(G1/G5/G6). Superlativi residui: finding 7 ("TUTTA la pratica") e il
"first" di PB-2, che il capitolo tratta correttamente con la formulazione
bloccata. Nessun BREAK.

## VERDETTO

**REGGE-CON-RIPARAZIONI.**

Conteggio: BREAK 0 · REPAIR 4 (#1, #2, #4, #5) · DOWNGRADE 1 (#3) ·
GAP 1 (#6) · NOTE 3 (#7, #8, #9) — totale 9 finding.

Le due riparazioni piu' urgenti: #1 (stato [T-T0P] landed + boundaries
slip-free/t-periodic/cl(Omega_march) — la carta che il panel giochera') e
#2 (caveat band-underinclusion sul +0.51%, il numero destinato alla slide).
