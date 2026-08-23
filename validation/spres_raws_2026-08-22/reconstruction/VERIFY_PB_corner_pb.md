# VERIFY: P-B (li_xu_lv_lv_song_2023) — "corner a p_b MEDIATO" (SYN:33 / LL-20)

Source-verification 2026-08-23, dubbio utente ("loro usano p0 e T0
mediate, credo — cosa sarebbe p_b li'?"). PDF letto MIRATO alle pp.
4-11 di `literature/li_xu_lv_lv_song_2023_rde_film_cooling_nozzle_ast136_108221.pdf`.
Arco di consumo: box nomenclatura CH5 (owner B5), riga LL-20
LINEAGE_LEDGER (correzione orchestratore), risposta utente.

## (a) Condizioni di ingresso del design — p0/T0 MEDIATE: CONFERMATO
- p. 5, §3.1: "it is empirically recognized that time-averaged
  stagnation parameters at the combustor exits of RDEs can be utilized
  as the aerodynamic constraints on the RDE nozzle design [20,25,41,42]".
- p. 8/10, §5.1: "The equivalent steady state is based on the
  time-averaged stagnation parameters at the throat that have been
  averaged in the spatial scale at each moment"; Fig. 16 (p. 10) da'
  p0/p_inf e T0 al combustor exit. L'utente ha ragione su questa parte.

## (b) Quale pressione governa i corner (costruzione Rao/Veen)
DUE corner distinti (Fig. 13, p. 8):
- Corner T (lip della SHROUD, superficie ST): Eq. 22, p. 8:
  "(p - p_inf) cot(a) / (1/2 rho V^2) = sin(2 theta)", "where p_inf
  denotes the ambient pressure" — pressione AMBIENTE, non mediata.
- Corner J (bordo della base dello SPIKE troncato, superficie KJ):
  Eq. 26, p. 8: "(p - p_b) cot(a) / (1/2 rho V^2) = sin(-2 theta)",
  "where p_b represents the averaged base pressure".
p_b compare anche nella spinta, Eq. 18 (p. 6): termine "+ pi r_J^2 p_b"
(base del plug), accanto a "- pi r_T^2 p_inf".

## (c) Eq. 26: testo esatto e fonte
Testo: come sopra ((b), quote verbatim). FONTE: NESSUNA citazione
sull'equazione; il metodo dell'intera §3.2 e' attribuito a Rao + "Veen
et al. [44]" (p. 6). Il paper NON dichiara mai da dove venga il VALORE
di p_b usato nel design (nessuna equazione, correlazione o rimando).
L'unico "averaged base pressure" quantitativo e' la VERIFICA steady
cold-flow (Fig. 5, p. 5: "Averaged base pressure at different NPRs",
esperimento Chutkey [37]) — media SPAZIALE sulla base del plug, dominio
steady. "Averaged" in Eq. 26 e' terminologia da plug troncato steady
(media sull'area di base), NON una media di ciclo RDE: il paper non
collega mai p_b al time-averaging della detonazione.

## (d) VERDETTO sul claim SYN:33 / LL-20 "corner a p_b MEDIATO"
**DA RIFORMULARE.** Verbatim-difendibile a meta' ("averaged base
pressure" e' parola del paper), ma fuorviante in contesto CH5, dove
"mediato" = time-averaged sul ciclo RDE: (i) dei due corner, quello a
p_b e' SOLO il corner J (base spike); il corner T usa p_inf ambiente
(Eq. 22); (ii) "averaged" in Eq. 26 = media spaziale sulla base
(lessico Rao/Veen plug troncato), senza alcun nesso dichiarato col
cycle-averaging; (iii) la mediazione RDE entra SOLO nei vincoli di
ristagno p0/T0 (p. 5 + §5.1), come sostiene l'utente.
Formulazione corretta proposta (per SYN:33/LL-20/box B5):
"Rao/Vander-Veen su stato steady da p0/T0 TIME-AVERAGED ('empirically
recognized', p. 5); chiusure dei corner: lip shroud a p_inf ambiente
(Eq. 22), base spike a p_b = 'averaged base pressure' (Eq. 26, media
spaziale di base, fonte e provenienza del valore NON dichiarate)."
LL-20 "(Eq. 26 senza fonte)": CONFERMATO e va rafforzato — senza fonte
E senza provenienza del valore numerico.
