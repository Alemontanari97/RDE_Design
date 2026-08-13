# S21 ADDENDUM PROMPT (2026-08-11 — integrates the red team, the
# use-case duties, and the RDE-choking analysis into the RUNNING S21
# F0; paste as an in-session order. Advisory, untracked.)

ADDENDUM ALLA S21 IN CORSO — da eseguire PRIMA del duty "panel R4
absorption" di F0, perché corregge il testo che quel duty
assorbirebbe. Quattro blocchi:

A [RED-TEAM CORRECTIONS — vincolanti prima di assorbire EQ-v2 in
M0/D-doc; fonte: validation/ADVISORY_redteam_2026-08-11.md, 18
issue di cui 6 high su tre bersagli]. Minimo obbligatorio (gli
high):
 (1) RT-1: la frase "the S20 standoff is the PREDICTED SIGNATURE of
 a DEF-sector optimum" è sintesi AGGIUNTA dal giudice — i panelist
 dicevano "consistent with (not proven by)", e il 41.8% del residuo
 all'ATTACCO suggerisce anche binding interno. Riformulare ovunque
 in: "consistent with a DEF-sector optimum AND equally with an
 interior-binding tier-1 optimum until O4 (localization) runs".
 (2) RT-2: separare i due lembi di S1 (fold-on-boundary+interior
 certification = HOLDS unanime; closure-membership = OPEN pending
 approximant existence) e correggere l'attribuzione "all four
 state" (solo il refuter lo afferma).
 (3) RT-3: aggiungere H7 = selection/global-max among margin-active
 KKT points a EQ-v2 (o togliere "KKT nonuniqueness" dalla lista
 assorbita); dichiarare l'indebolimento silenzioso optimum ->
 construction in Direction B.
 (4) RT-4: il test mu/deeper-jump e' declassato a SIGN TEST finche'
 non esistono la derivazione one-page dJ/d(depth) = -mu*dm/d(depth)
 sotto H3 e la banda dell'estimatore di mu (KS-rho + floor
 extrapolation). "Decisive for O3" e' ritirato.
 (5) Applicare anche gli issue medi/alti dei bersagli plan-v3 e
 audit-refuted (leggerli dal file; gli high del plan-v3 e i 2 high
 dell'audit-refuted vanno adjudicati esplicitamente nel log). In
 particolare, TRE adjudicazioni esplicite obbligatorie:
 (5a) ISS-1-CONTACT-SLIP-UNOWNED [high]: la macchineria U3/U4 e'
 shock-only PER COSTRUZIONE (clausola F1 = Lax shock di famiglia
 acustica); nessuna fase possiede le discontinuita' di
 contatto/slip. Assegnare l'ownership (F2a default
 stratificato-liscio per degenerazione lineare + F4b opzione
 fitted-contact con la sua teoria) e correggere la
 hypothesis-coverage map.
 (5b) o32-refutation-hides-verdict-moving-rule-change [high]:
 RE-ADJUDICARE la riga obiettivo di O3.2 (S19): il commit di
 verdetto 514e267 ha riscritto la regola (one-sided + cap
 raddoppiato a 1.0) e dp_tot = 0.6704 NON sarebbe conclusivo sotto
 il cap pre-registrato 0.5. Aggiudicare: o la pre-dichiarazione
 in-log del passo 4 S19 (correzione adottata prima di leggere i
 rate) regge come emendamento legittimo di regola-errata-derivata
 — con la contraddizione 0.5-vs-derivazione dichiarata li' — e
 allora il verdetto sta MA la riga va annotata "conclusiva solo
 sotto il cap corretto"; oppure non regge e la riga obiettivo va
 ri-riportata NON-CONCLUSIVA. Nessuna terza via silenziosa.
 (5c) judge-totals-do-not-match-body [high]: GIA' CORRETTO
 (2026-08-11) nell'header di AUDIT_agnostic: totali veri = 82
 CONFIRMED (13 high), 12 REFUTED, seeds 4C/3R; ogni testo a valle
 che cita "86/8" va corretto. Verificare che il triage P0-P2
 copra i 13 high reali (5 high in piu' rispetto al conteggio
 vecchio: ri-triage esplicito nel log).
 Inoltre da plan-v3 [medium ma strutturali]: istanziare i budget
 per-fase (anchor misurato + cap wall-clock + max campagne, oggi
 solo F1 li ha — i fallback "auto-firing" delle altre fasi non
 possono scattare per regola); rendere il freeze P-2 davvero
 DATATO (data di calendario + artefatto che la registra + chi la
 misura); adjudicare esplicitamente la proposta del realist di
 SGANCIARE P-2 da F1 (freeze a F0+1 a qualita' fallback) invece
 del coupling attuale — decisione utente, non default; sanare
 l'incoerenza flagdef-KAT "landed" (gate F0/F1b) vs "DISPATCHED"
 (testo D6 ratificato): il gate d'ingresso F1b deve dipendere solo
 da cio' che QUESTO repo controlla, con il KAT GENO come
 conditional esterna nominata.

B [USE-CASE DUTIES — assorbire U1-U3 da
validation/ADVISORY_use_case_interface_2026-08-07.md (incl. il
survey addendum U1 con le due linee verificate: unstructured
shock-fitting Paciorri-Bonfiglioli; concentration method
Gelb-Tadmor) nella spina F ratificata: U1 -> F5-entry (upgrade del
case-B generator a pipeline CFD->contratto, estrazione-fronte con
oracolo); U2 -> F2a/F4b (contatto: default stratificato-liscio per
degenerazione lineare, fitted opzionale); U3 -> F2a/F5-entry
(regola della superficie di estrazione) MA con lo stato PREMISE-
OPEN del blocco C qui sotto].

C [U3' — ANALISI CHOKING RDE, il buco scoperto dall'utente: "un RDE
non vale Sauer o simili; il concetto di choking va analizzato
profondamente"]. La U3 come formulata PRESUPPONE che esista una
superficie per-fase assialmente supersonica a valle della gola —
un'intuizione da ugello steady (Sauer/choking stazionario) il cui
trasferimento all'RDE (gola investita da pattern rotante non
uniforme, non stazionario) NON e' stabilito; la stessa mappa
letteratura registra claim per cui "steady criteria are invalid".
DUTY U3': adjudicazione formale del choking per-fase — sotto quali
ipotesi (e con quale monitor eseguibile) la decomposizione
quasi-steady ammette una superficie sonica/di estrazione per-fase
ben definita; quale correzione porta il correttore; quando la
risposta e' NO e serve il patch subsonico con chiusura dichiarata.
SURVEY BASE: gli advisory di lettura profonda in arrivo (workflow
wf_c60ded86-a48: Stechmann 2018 INTEGRALE, Kaemming-Paxson EAP
INTEGRALE, dossier Harroun-line; + reader dedicato: Paxson-Miki-
Perkins-Yungster AIAA 2022-4107 = Aviation_2022_final.pdf TROVATO
nella dir sopra, LETTURA INTEGRALE in corso — la mappa ne registra
"the choked chamber exit decouples cycle from nozzle", il claim
PIU' direttamente rilevante, in page-verify col reader) +
l'acquisizione utente residua: Harroun-Heister-Ruf JPP 37(5) 2021
+ AIAA 2019-0197. OWNER: F2a (contratto dati); la regola U3 resta
PREMISE-OPEN finche' U3' non chiude; nessun freeze del contratto
d'estrazione prima.

D [FETCH LIST utente, DATATA — AGGIORNATA 2026-08-11 sera]: residuo
UNICO = AIAA 2019-0197 (compagno di Harroun; possibile sede vera
della frase misquotata, vedi E). ARRIVATI E LETTI INTEGRALMENTE:
Stechmann JSR 2019, Kaemming-Paxson EAP, Paxson-Miki AIAA
2022-4107, Harroun JPP 37(5) 2021, Gonzalez-Viana 2025. GIA' SU
DISCO identificati: Giles-Ulbrich SINUM 2010 Parte 1 E Parte 2
(literature/080727464.pdf, 09078078x.pdf — gate F4b!),
Lozano-Ponsin 2025, Wolanski PCI 2013, Shepherd-Kasahara GALCIT
2017 (rde_model_report.pdf, lettura in coda). Restano in lista F0:
Sternin 1962, Shmyglevskii 1981; Moretti/Salas condizionale.

E [ESITI DEL CENSIMENTO CHOKING — assorbire
validation/ADVISORY_rde_choking_2026-08-11.md]:
 (E1) MISQUOTE VERDICT-ADJACENT da correggere in F0/R4: la frase
 virgolettata "near-perfect time-averaged expansion" attribuita a
 Harroun 2021 in literature_map righe ~20, ~63-65, ~639 NON ESISTE
 nel paper (cercata su 14/14 pagine); sostituire con parafrasi
 fedele + anchor (p.670 profili simili post-ricompressione, p.671
 C_F 1.25 con caveat 2-D, CONTRO le contro-evidenze pp.660/666-669);
 regrade P1_sections_2_4 §4.5 (duty scaricato, eco MISTA
 page-verified); NON riattribuire la frase a Harroun 2019/AIAA
 2019-0197 senza page-verify. PARADOSSO A FAVORE: la novita' T3
 esce RAFFORZATA (nessun collapse enunciato in letteratura).
 (E2) U3' AFFILATA: contratto d'estrazione A DUE REGIMI per
 costruzione (patch per-fase assialmente supersoniche -> hand-off
 caratteristico; patch subsoniche -> chiusura dichiarata O1/O2/O3
 PROMOSSA A PORTANTE — K-P Fig.6: M_assiale 0.86-1.33 alla gola nel
 caso sano); criterio = M_ASSIALE (non totale — Paxson-Miki Fig.3 e'
 Mach totale col tangenziale dentro); certificato di decoupling =
 versione eseguibile della premessa Paxson-Miki; caveat quench da
 restrizione di gola (Harroun p.661) come validita' DATI.
 (E3) Registrare gli arrivi (D) nel registro acquisizioni e
 schedulare: page-verify Giles-Ulbrich x2 (sblocca l'entry F4b),
 lettura Shepherd-Kasahara (choking-rilevante).

TERMS: tutto il resto del prompt S21 invariato; le correzioni A
sono TESTO degli advisory prima dell'assorbimento (non riaprono i
verdetti del panel: li riportano a cio' che i panelist hanno
davvero detto — e' l'esito del red-team, la forma piu' pura del
metodo doppia-prova); R5/R4 invariati; log S21 registra questo
addendum come ordine utente datato.
