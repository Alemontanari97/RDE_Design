# REFUTE_W2_minipass — Mini-pass di verifica sulle righe [W2-*] di CH1-CH6 (critic 21)

Slot C4 (refuter), onda W-C.a, 2026-08-23. Perimetro: le sole righe/edit
marcate [W2-*] nei capitoli CH1-CH6 (riparazioni wave-2, sessione 1) +
cammino delle tabelle "Disposizione riparazioni (W-A)" di CH7/CH8
(campione: tutte le ALTO + 5 casuali). ESCLUSE: §6 STORIA, sezioni nuove
W-B.1 (coperte da altri slot).

Metodo: (1) grep `W2-` su reconstruction/ (comando misurato in-window) →
mappa marker per capitolo; (2) cross-check tabella-disposizione ↔ marker
nel corpo per OGNI riga; (3) ancore campionate read-then-quote alla fonte
(priorità: classe ALTA/REPAIR + ogni ancora numerica portante).

---

## 0. Censimento marker (grep -n "W2-" su reconstruction/, in-window)

| Cap | righe tabella (APPLICATO) | marker nel corpo | esito |
|---|---|---|---|
| CH1 | 9 (R1-R9, :683-691) | R1-R9 tutti presenti (:9, :57, :71, :129, :358, :450, :458, :522, :543, :554, :570, :589) | COMPLETO |
| CH2 | 12 (R1-R12, :581-592) | R1-R12 tutti presenti (:21, :29, :117, :226, :227 [R4 = falsificatore riga T-T7FS], :233 [R5], :263, :267, :273, :281, :352, :379, :394, :424, :460) | COMPLETO |
| CH3 | 13 (R1-R13, :789-801) | R1-R13 tutti presenti (:30, :50, :61, :189, :295, :330, :375, :393, :435, :505, :510, :518, :533, :555, :562, :586, :618, :628-652) | COMPLETO |
| CH4 | 11 (R1-R11, :1004-1014) | R1-R11 tutti presenti (:131, :137, :167, :293, :305, :309, :323, :442, :444, :445, :552, :604, :640, :646) | COMPLETO |
| CH5 | 10 (R1-R10, :762-771) | R1-R10 tutti presenti (:27, :43, :155, :321, :468, :492, :494, :667, :693, :717, :739) | COMPLETO |
| CH6 | 11 (R1-R11, :734-744) | R1-R11 tutti presenti (:71, :78, :86, :111, :313, :423-424, :528, :551, :560-563, :585, :610, :639, :664, :675, :683, :713) | COMPLETO |

**66/66 riparazioni dichiarate APPLICATO hanno l'edit marcata nel corpo.
Nessuna riga di tabella orfana.** (CH6 :295 è un cross-ref a CH3 W2-R2,
non un marker CH6 — correttamente escluso dal conteggio.)

---

## 1. Ancore verificate alla fonte (read-then-quote, 26/66 campionate)

| # | Riparazione | Ancora dichiarata | Verifica alla fonte | esito |
|---|---|---|---|---|
| 1 | CH1 R1 (ALTA) | M0:602-628 [T-T0P] landed + 3 boundaries | M0:602 "THE [T-T0P] MAIN STATEMENT (landed 2026-08-19...)"; :614-615 quantificatore t-periodico; :617 "cl(Omega_march) only"; :618 "SLIP-FREE instances only" | REGGE |
| 2 | CH1 R2 (ALTA) | M0:4216-4219 caveat band-underinclusion | M0:4215-4219 "+2.0407e5 (+0.51%)... DECLARED band-underinclusion caveat... crude systematic bound ~6e4" (6e4/2.0407e5 ≈ 29% — il "~30% del datum" regge) | REGGE |
| 3 | CH1 R3 | P1:96-104 collasso del peso in T3 | P1:97-101 boxed warning "phase-independent EXACTLY in the T3 collapse class — there, and only there, (**') reduces to the naive unweighted average" | REGGE |
| 4 | CH1 R5 | M0:125-138 [T-NSW]; M0:139-169 m_n + (M-a)/(M-a') + W1-W4 | M0:130 [T-NSW]; :147 "m_n := u . n_m - c >= delta"; :159-166 split (M-a)/(M-a'); :167-169 finestra R1 W1-W4 | REGGE |
| 5 | CH2 R1 | M0:2812/2818 "verified formally"; registry :580 | M0:2812 "[T-T7FS] THEOREM-SCHEMA 8... SCHEMA"; :2818 "Stationarity structure (verified formally)"; claims_registry:580 statement L^1(dmu) + "(P)(ii) is a rigorous necessary condition" | REGGE |
| 6 | CH2 R4 | registry :586 forma negative-existential ritirata | claims_registry:586 falsifier "dJ /= Int F' dmu beyond bars... O3-class... the former negative-existential-over-envelopes form was not finitely observable" | REGGE |
| 7 | CH2 R5 | o33_bench.py:320-321 f3*, docstring :32; M0:2891 ancora ":292" stantia | o33_bench.py:289-295 = helper `drift()` (r.292 = `sc = np.mean(...)` DENTRO drift); :320-321 = formula f3* (L.13); :32 docstring f3*; M0:2890-2891 stampa davvero "(validation/o33_bench.py:292)" → il finding candidato di retro-audit CONTRO M0 (CH2 §3.8) è GENUINO | REGGE |
| 8 | CH3 R1 (alta) | M0:1883 parte avvettiva senza numero | M0:1883 riga sweep-advective: "magnitude MEASURED by M-RED (bands B-1/B-2)", nessun numero; il numero 0.007-0.09 = 0.7-9% vive a M0:1884 (pressure-work legs) e M0:1344 — coerente con l'edit del corpo (:502-505: 1883 ancora la SOLA parte avvettiva) | REGGE |
| 9 | CH3 R2 (alta) | M0:1309 regola di cella | M0:1309 "NO cell above its held evidence class" | REGGE |
| 10 | CH3 R7 | M0:2113-2118 branch-wise UNDEFINED | M0:2113-2118 TAIL [REV2-r4-2](d) "on a CONNECTED nonconvex set... branch-wise coverage is UNDEFINED — no global-argmax coverage is claimed" | REGGE |
| 11 | CH3 R8 (GAP alta) | M0:1886 confine viscoso | M0:1886 "separation / viscous content... outside inviscid class... NOT a K term — boundary named... no bound asserted" | REGGE |
| 12 | CH3 R13 | M0:1343 scoping Cor 5.1 | M0:1343 cella (i) BEST "Cor 5.1 scoping (cl(Omega_march), slip-free)" | REGGE |
| 13 | CH4 R1 | G0 :148, :167-169 gate S18 | G0:148 T2a def; :167-168 "t_GENO 0.299 s, T2a 0.116 <= 1.197 s PASS"; :168 "grad/solve 1.593 <= 4"; corpo CH4 :320-323 allineato | REGGE |
| 14 | CH4 R2 | C17 :342, C18 :353 verbatim | choice_ledger:342 "no derivation or panel adjudication of N_NEWTON found"; :353 "derivation itself still NEVER done" — entrambi verbatim | REGGE |
| 15 | CH4 R4 | R13 PROGRESS :191 = solo md5/N-74/knob | PROGRESS:191 "R13 GENO: md5 freeze s3 + N-74(+esteso) + knob jump-depth" — esattamente i tre item, nessun owner audit | REGGE |
| 16 | CH4 R5 | G0 :53-58 (caveat host) | G0:53 "adjoint overhead ~1.5%"; :55-58 caveat host + ratio decision-relevant — vedi F-1 (NOTE granularità) | REGGE con NOTE |
| 17 | CH4 R6 | G0 :202-210 scope X-GENOXC | G0:202-210 "certifies agreement at the INTERIOR UNIT PROCESS... NOT the profile-generation machinery... no assembled JAX MoC march" | REGGE |
| 18 | CH4 R9 | esistenza log S18 su disco | glob: `validation/PROGRESS_2026-08-06_S18_brick2run.md` ESISTE | REGGE |
| 19 | CH5 R1 | ADV-LX:25-31 caveat ISABE | ADVISORY_litmap_extension:25-31 CLAIM B "SURVIVES in the qualified form" + near-miss ISABE-2003-117 + "FULL TEXT UNREAD = residual risk #1" | REGGE |
| 20 | CH5 R2 | SYN:526-528 W-05; SYN:540-542 W-09 | SYN:526-528 W-05 Li-Xu-Huang 2022 "design-method PARENT... highest method-lineage bearing"; :540-542 W-09 Fievisohn "closest published cousin" | REGGE |
| 21 | CH5 R5 | LM:387-404 risultato classico, 5 fonti | LM:387-404 schema comune Rao/Hoffman, 2 vincoli isoperimetrici, h=0, superficie = caratteristica "a RESULT"; :401 "verified against five primary sources" | REGGE |
| 22 | CH6 R2 | checkpoint :468-469 baseline Gap B | sfoundations SESSION_STATE_checkpoint:467-469 "Gap B = J3D(x*_pf) - J3D(x*_legacy)... our functional vs Veen/Angelino-at-mean" — distinta da I4 come dichiarato | REGGE |
| 23 | CH6 R3 | M0:1335-1339 forma ancorata | M0:1338-1339 "[ORCH-HARV-1]... best-of-sweep != argmax: no published work optimizes the true 3D-unsteady case; sweep/redesign evidence is ranking-signal only" (+ checkpoint :472-476 concordante) | REGGE |
| 24 | CH6 R5 | M0:2320-2329 D-06 verbatim + near-miss | M0:2320-2322 locked formulation D-06 verbatim "never abbreviate"; :2322-2323 "'the first averaged-thrust variational problem' is DEAD of record"; :2324-2330 Efremov-Kraiko 2004 | REGGE |
| 25 | CH6 R6 | M0:2316-2319 sharpness; M0:3524-3525 nesting THEOREM | M0:2316-2319 "Sharpness: a length cap... break the nesting: then max Int < Int max STRICTLY"; M0:3524-3525 "the nesting and the constrained-KKT structure are THEOREM (standard)" | REGGE |
| 26 | CH6 R9 | M0:1348 value-route | M0:1348 (cella (vi)) "\|argmax shift\| ≤ 2·sqrt(eps_U/mu_red)" con eps_U sampled-sup — esattamente la forma citata dalla nuova Q7 | REGGE |

Le 40 riparazioni non campionate ad ancora: verificate a livello
marker-nel-corpo + coerenza tabella↔testo (censimento §0), non alla fonte.

---

## 2. Cammino tabelle "Disposizione riparazioni (W-A)" CH7/CH8

Campione da brief: tutte le ALTO (3) + 5 casuali (CH7 #5, #10, #12;
CH8 #5, #9).

| Riga | classe | edit dichiarata | edit trovata nel corpo | esito |
|---|---|---|---|---|
| CH7 #2 | REPAIR classificato ALTO | §1.2(g)+§4(4): caveat UNPROVEN/layer-certified, VERDICT_confirm §4 giudice AM-1..AM-3, distinzione author-applied vs giudicati | CH7:151-156 (tutte e tre le componenti (a)/(b)/(c)) + :530-535 ("COL SUO CAVEAT VINCOLANTE... UNPROVEN... be cited as layer-certified... gate CLOSED") | PRESENTE |
| CH8 #1 | REPAIR ALTA | loop C-HT4 esteso in §4(2)(b), §5 item 2, §2 riga [T-T4] | CH8:322 (riga [T-T4]: inherits `:336`, falsificatore `:181` sotto C61+H20, C-N2), :461-463 (§4(2)(b)), :509 (§5 item 2) — tre siti, tutti presenti | PRESENTE |
| CH8 #2 | REPAIR ALTA | connessione S0 declassata a CONGETTURALE con quote census | CH8:114 e :439 quote "conjecturally connected (hub argument owed, CEN-O4)"; fonte verificata: `validation/PANEL_topology_census_2026-07-22.md:68` porta la frase | PRESENTE + fonte REGGE |
| CH7 #5 | REPAIR/MEDIA | saldatura 3 = lettura di assemblaggio | CH7:48 "ASSEMBLAGGIO di questo capitolo, dichiarata come tale" (§1.1) + :303 "[lettura di assemblaggio..." (§1.5(3)) + :50 "3-stage upgrade path" A/B/C con DISPATCH :80/:86 | PRESENTE |
| CH7 #10 | NOTE/BASSA | comparativo → enunciato fattuale | CH7:159 "documenta le proprie retraction NEL testo" | PRESENTE |
| CH7 #12 | NOTE/BASSA | nuova §1.6 Glossa minima | CH7:317 "### 1.6 Glossa minima" con le 4 voci (booking level a :327) | PRESENTE |
| CH8 #5 | GAP/MEDIA | "Tre pezzi" → "Quattro pezzi" + (d) chart | CH8:472 "Quattro pezzi, tutti gia' nominati nel record" + :481 (d) F2-C1-CONTROL-CHART-MIGRATION owner F2 | PRESENTE |
| CH8 #9 | NOTE/BASSA | ancora corretta findings :2519 + glossa ":2521 ordinal" | CH8:189 "docs/findings_registry.yaml:2519 — la mappa lo cita come ':2521 ordinal'" | PRESENTE |

8/8 righe campionate: l'edit dichiarata esiste nel testo del capitolo.
Nessuna riga RIPARATO trovata senza edit corrispondente.

---

## 3. Findings

| # | classe | file:riga | evidenza |
|---|---|---|---|
| F-1 | NOTE (granularità d'ancora, nessun claim falso) | `validation/spres_raws_2026-08-22/reconstruction/CH4_machine_choices.md:643-646` | La parentesi "(overhead adjoint ~1.5%, ratio grad/solve 1.593 ≤ 4) (G0 `:55-59`)" cita :55-59, che copre il SOLO caveat host (G0:55-58, dove il ratio stampato è ~1.01 unit-process); "~1.5%" vive a G0:53 e "1.593 ≤ 4" a G0:168 (engine, S18). Entrambi i numeri sono di record e correttamente ancorati altrove nel capitolo (claim 3 `:442` → G0:33-59; gate `:323` → G0:168). Rischio: un retro-audit pedante della slide leggerebbe :55-59 e non troverebbe 1.593. Riparazione suggerita (1 riga): "(G0 `:53-58`; 1.593 a `:168`)". NON blocca: la sostanza di W2-R5 (etichette corrette) è applicata e vera. |
| F-2 | CONFERMA POSITIVA (non difetto) | `validation/o33_bench.py:289-295, :320-321` vs `docs/rde_nozzle_MASTER.md:2891` | Il finding candidato di retro-audit CONTRO M0 dichiarato da CH2 W2-R5 (§3.8) è GENUINO: M0:2891 stampa ":292", la r.292 reale è dentro l'helper `drift()`, la formula f3* (L.13) vive a :320-321 con docstring :32. La riparazione è corretta e il finding va mintato come previsto. |

Nessun finding di classe BREAK o REPAIR: nessuna riparazione dichiarata
APPLICATO è risultata assente, nessuna ancora campionata ha fallito il
read-then-quote.

---

## 4. Q&A SEED

Nessun seed nuovo: il solo candidato emerso ("quante altre ancore M0
sono stantie come :2891?") è già armato dal capitolo stesso (CH2 §3.8,
regola S-PRES: claim che fallisce il walk = finding del registro) e dal
retro-audit dichiarato del deck (addendum 3 C4). Duplicarlo qui sarebbe
entropia.

---

## 5. FUORI-PERIMETRO (dichiarato)

1. §6 STORIA e sezioni nuove W-B.1 di tutti i capitoli — coperte da
   altri slot W-C (da brief).
2. Le 40 riparazioni W2 non campionate ad ancora: verificate SOLO a
   livello marker+coerenza tabella (censimento §0 = 66/66); le loro
   ancore restano coperte dal retro-audit di deck (100% load-bearing,
   addendum 3 C4), non da questo mini-pass.
3. CH7 righe #1, #3, #4, #6-#9, #11 e CH8 righe #3, #4, #6-#8, #10:
   fuori campione (brief: ALTO + 5 casuali).
4. Staleness findings_registry:1455 (CH1 W2-R8): dichiarata dal capitolo
   stesso manutenzione fuori scope S-PRES — non verificata qui.
5. Nessuna verifica di CONTENUTO nuovo: questo pass giudica che le
   riparazioni siano applicate e ancorate, non ri-aggiudica le scelte.

---

## 6. VERDETTO

**REGGE — mini-pass PASS.**

- Censimento: 66/66 riparazioni [W2-*] CH1-CH6 dichiarate APPLICATO
  hanno l'edit marcata nel corpo; 0 righe orfane.
- Ancore: 26/66 campionate read-then-quote alla fonte (tutte le
  ALTA/REPAIR portanti incluse): 26/26 REGGONO; 1 NOTE di granularità
  (F-1, riparazione a 1 riga suggerita, non bloccante); 1 conferma
  positiva (F-2: il finding anti-M0 di CH2 è genuino).
- Tabelle CH7/CH8: 8/8 righe campionate (3 ALTO + 5 casuali) hanno
  l'edit corrispondente nel testo; fonte census :68 verificata.
- 0 BREAK, 0 riparazioni mancanti, 0 ancore fallite.
