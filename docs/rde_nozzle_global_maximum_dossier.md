# Global-maximum dossier — census and first screening (opened S15)

Status: DOSSIER OF RECORD, OPENED (2026-08-05, S15 deep-foundations
campaign, [RIGOR/C]). Anchor: (P)(iv) of M0 D2.6 — GLOBALITY as the
certified pair (S*, delta), standing goal = the delta -> 0 program.
This pass is a CENSUS AND FIRST SCREENING of the certified
global-search routes on the certified finite-dimensional class (the
working spline class A_h per topology sector), each with a
cost/hypotheses/preliminary-verdict card. RULE (mandate): NO route is
ADOPTED without a carrier — every verdict below is PRELIMINARY until
its named first brick runs. Registry: [PAP-GMAX].

Audit line: [Class: PRACTICE (screening adjudication; no new
mathematical claims; every "gives" statement is the published
guarantee of the named method class, cited method-level) | Falsifier:
a route card whose "needs" are shown unmet by its own first brick |
Carrier: none yet BY RULE — first bricks named in §6 | Gamma: n/a].

------------------------------------------------------------------------------
## §1 The object being globally maximized

Per topology sector: J_h : K ⊂ R^n -> R, n = spline DOF (order
10-30), K = the box/polytope cut by the constraint vector c (+ state
constraint g_sep via the active-set machinery). J_h is evaluated by
the certified per-phase march (A1 engine) and cycle quadrature;
dJ_h/dSigma by reverse-AD (Lemma B, O3.1-certified). Structure facts
that matter for global search:
 (a) J_h is PIECEWISE-smooth: march-topology events (RK-G: cell
     counts, shock identity, chord-foot branches) partition K into
     smooth cells with one-sided derivatives at the seams.
 (b) A certified LIPSCHITZ or INTERVAL bound for J_h over a box
     requires propagating interval enclosures through the march
     (interval Newton per cell) — not yet built; this single
     capability turns out to be the shared enabling brick of every
     certified route below (the dossier's structural finding, §5).
 (c) With the THERMOTAB C^1/Hermite duty executed (D6 item 9), the
     thermo closure becomes PIECEWISE-POLYNOMIAL — each MoC cell
     equation is then a polynomial system: the reduced per-phase
     problem is SEMIALGEBRAIC in principle. Recorded as a structural
     opportunity (feeds Card 2), not a claim.

------------------------------------------------------------------------------
## §2 Route cards

CARD 1 — LIPSCHITZ / INTERVAL BRANCH-AND-BOUND (Hansen/Neumaier
deterministic global optimization class; DIRECT as the non-certified
screener only).
 NEEDS: interval extension of J_h over boxes (b, above); bounded
   number of topology events per box (RK-G seams become branch
   boundaries — B&B handles them NATURALLY by splitting: a
   structural fit, noted).
 GIVES: TRUE certified global maximum over K to tolerance — i.e.
   EXACTLY the (S*, delta) deliverable with delta = the certified
   B&B gap. The only route in the census whose output IS the
   program's target object without translation.
 COST: worst-case exponential in n; realistic ONLY on low-dim
   reductions (2-4 DOF: eps, L, corner/lip parameters) or coarse
   subspaces; interval wrapping through a marching scheme is the
   known pain point (cost/tightness tradeoff unquantified for MoC).
 PRELIMINARY VERDICT: VIABLE-ON-REDUCTIONS; the eps-level machinery
   (phase diagram, certified sweeps) is already a 2-D instance in
   spirit; NOT viable directly on the full spline class. SYNERGY OF
   RECORD: the same interval substrate discharges C-XBVP(a) (the
   S-XCONV convexity box proof) — one investment, two payoffs.

CARD 2 — MOMENT/SOS HIERARCHIES (Lasserre; sparse TSSOS/chordal
variants).
 NEEDS: polynomial/semialgebraic problem data. Two honest sub-routes:
   (2a) certified polynomial SURROGATE p with |J_h - p| <= eta on K
        (remainder certification again needs Card 1's interval
        substrate) -> global max of p by SOS gives delta = SOS gap
        + 2 eta;
   (2b) native semialgebraic subproblems: with Hermite tables
        (§1(c)) the per-cell march equations are polynomial —
        small-case critical-point enumeration and PSD certificates
        become algebraic.
 GIVES: certified bounds with rational certificates (checkable
   independently — attractive for the Verdict format).
 COST: dimension curse (n ≳ 10-15 or degree ≳ 4 blows up even
   sparse); surrogate route inherits eta.
 PRELIMINARY VERDICT: NOT-VIABLE-FULL-SCALE; PROMISING for (i) PSD
   certificates over boxes — the S-XCONV Hessian positivity over the
   margin box is a NATIVE SOS problem (competes with Card 1 on the
   same first brick: deliberate experiment design), (ii) delta
   certificates on 2-3 DOF reductions.

CARD 3 — DEFLATED CONTINUATION + CERTIFIED EXCLUSION (Farrell
deflation; Krawczyk/interval-Newton exclusion tests).
 NEEDS: the B2 collocation route (already planned, A3) for deflated
   Newton enumeration of stationary contours; for CERTIFICATION,
   interval exclusion boxes proving no further stationary points —
   deflation alone is a heuristic enumerator (honest: it can miss
   basins; the plan already says "uniqueness never assumed").
 GIVES: the multiplicity map of (P); upgraded with exclusion sweeps
   on small K -> certified complete enumeration -> global max by
   finite comparison.
 COST: enumeration cost per stationary point moderate (Newton);
   exclusion sweep = same interval substrate as Card 1; realistic on
   low-dim K.
 PRELIMINARY VERDICT: ADOPTED-CLASS for local enumeration (already
   in D6 A3); its CERTIFIED completion is a Card-1-substrate client.
   No new adoption decision needed now.

CARD 4 — SECTOR TOURNAMENT (topology level; already of record).
 The global maximum over TOPOLOGIES is a finite max over sectors,
 each contributing its (S*, delta); the tournament device
 (premium_bound per cell, D2.6(iv)/T-OP11e) is the existing
 mechanism. DEPENDENCY: the sector census lemma (finiteness +
 definition class) — a NEXT-1 register item, with two T2-residue
 items (s2, s6) still awaiting second lens. Verdict: MECHANISM OF
 RECORD, blocked only by the census lemma writing.

------------------------------------------------------------------------------
## §3 Nonconvexity quantification (duty, so the choice is evidence-based)

Before any adoption: MEASURE the nonconvexity the routes must beat.
Three cheap instruments, all unlocked by brick 2 (dJ/dSigma):
 (i)   deflation count on a 2-DOF slice of A_h (how many stationary
       contours actually exist?);
 (ii)  reduced-Hessian spectrum along continuation paths (where does
       convexity fail?);
 (iii) the persisted premium_bound per cell as a basin-structure
       proxy at eps level (already computed, group (x)).
Declared as the FIRST EMPIRICAL DUTY of the dossier at brick-2
landing; until then every "nonconvex" statement stays qualitative
(consistent with M0 D2.6 MAXIMALITY(c)).

------------------------------------------------------------------------------
## §4 The delta -> 0 program, assembled from the census

Layered mechanism inventory (each certified, composable per cell/
sector; delta_total = min over applicable mechanisms):
 L1 STRUCTURED CLASSES: delta = 0 PROVEN where structure exists —
    M1 duality-gap attainment, M2 pointwise T3 transfer, M3
    unimodality (of record).
 L2 BOUND LADDER: delta = B - J(S*) with B = min(int-max, sonic-
    capped J_ideal, B_EK) — computable TODAY for any candidate (of
    record, groups (viii)/(xi)).
 L3 INTERVAL B&B on low-dim reductions: certified delta on the
    reduced coordinates (Card 1) — NEW, pending its brick.
 L4 CERTIFIED ENUMERATION on small K (Card 3 + exclusion): delta =
    0 within the enumerated class — NEW, pending substrate.
 L5 SECTOR TOURNAMENT: composes L1-L4 across topologies (Card 4).
The program's standing goal is the MONOTONE tightening of
delta_total down this ladder, never a single leap.

------------------------------------------------------------------------------
## §5 Structural finding of the census

All three certified routes reduce, at their first genuinely new
brick, to ONE shared capability: INTERVAL ENCLOSURE THROUGH THE
PER-PHASE MARCH (Card 1 needs it for bounds, Card 2a for surrogate
remainders, Card 3 for exclusion tests). Secondary opportunity: the
THERMOTAB Hermite duty makes the closure polynomial and opens the
native-SOS door (Card 2b). Consequence for planning: the dossier
does NOT fork the program into three method tracks; it adds ONE
substrate brick plus per-route thin adapters. This collapses the
apparent cost of "certified global search" substantially — the
census's main payoff.

------------------------------------------------------------------------------
## §6 Verdict table and named first bricks (no adopt without carrier)

| Route | Preliminary verdict | First brick (named, VERDICT-gated) |
|---|---|---|
| Interval B&B | VIABLE-ON-REDUCTIONS | X-IVXC candidate: interval certificate of the S-XCONV Hessian over the declared margin box (= C-XBVP(a) discharge; small, decisive, reuses the S15 T1b object) |
| Moment/SOS | PROMISING-SMALL | same target by SOS (PSD certificate over the box) — head-to-head with X-IVXC on cost/tightness; loser documented, not adopted |
| Deflation + exclusion | ADOPTED-CLASS (local, A3); certification pending substrate | Krawczyk exclusion sweep on the eps-level 2-D problem (machinery exists, groups (x)/(xii)) |
| Sector tournament | MECHANISM OF RECORD | census lemma writing (NEXT-1 register; T2 residue s2/s6 second lens pending) |
| Interval march substrate | THE shared enabler | feasibility spike: interval Newton through ONE MoC unit process with wrapping measured (days-scale; go/no-go number for Cards 1/2a/3) |

Adoption discipline: a route is ADOPTED only when its first brick
lands with VERDICT PASS and a registered carrier; until then this
dossier is a map, not a commitment.
