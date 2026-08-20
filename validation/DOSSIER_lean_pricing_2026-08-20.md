# DOSSIER — Lean formalization pricing (user decision aid, presented
# at the S-FOUNDATIONS-C3 close per BLOCCATO 14/15; decision = USER,
# session-boundary class; this dossier prices, it does not decide)

## The question
Fund Lean (mathlib) mechanization of the central theorems? Value =
machine-checked symbol manipulation on the proof layer (a THIRD proof
leg beyond the panel/refuter half and the numeric-carrier half of the
dual-proof standard). Cost = formalization effort strongly dependent
on mathlib coverage of each theorem's mathematical substrate.

## Candidates (central, landed, rigor class of record) + per-item price
| Statement | Class | Substrate | Mathlib fit | Price | Value note |
|---|---|---|---|---|---|
| [T-XWALL] slip-wall relative-entropy flux annihilation | THEOREM (abstract EOS, every g) | algebraic identity + calculus | GOOD | **LOW-MED** | long sign-sensitive algebra = exactly where mechanization pays |
| [T-XSON] sonic bijection | THEOREM (abstract EOS) | monotonicity/inverse-function on explicit maps | GOOD | **LOW-MED** | same class; pairs naturally with T-XWALL |
| [T-T0P-E] equivariance (+ lemma family) | THEOREM (function-space complete) | symmetry/pushforward algebra on function spaces | MEDIUM | **MED** | setup cost (spaces), then structural algebra |
| L4=>R1 core | THEOREM/THEOREM* | genericity/measure statements (mu(Xi_sub)>0) | THIN | **MED-HIGH** | measure-genericity in Lean = real effort; value real (audit-grade hypothesis chain) |
| [T-XWS] weak-strong uniqueness (full chain) | THEOREM* (inherits C-XBVP(a,b)) | relative entropy on WEAK solutions, Gronwall, traces | FRONTIER | **HIGH** | weak-solution theory largely absent from mathlib; would force axiomatization => value collapses |
| [T-T0P] main | SCHEMA | marched BVP + gap lists | n/a | **NOT PRICEABLE YET** | SCHEMA class: mechanize only after full THEOREM status |

## Recommendation shape (if funded at all)
Start = the two abstract-EOS bricks [T-XWALL]+[T-XSON] (bounded,
high mechanization value, no axiomatization risk), option on
[T-T0P-E]. Do NOT start with [T-XWS]-full (axiomatized core =
certainty theater). Window: post-F2-entry side track, never on the
critical path; owner+session budget to be named at adoption.

## Honest counter-case (the do-nothing option)
Every candidate already carries the dual proof of record
(panel/refuter convergence + numeric carriers with rejectors); Lean
adds a third leg against symbol-manipulation error only. The
program's measured defect classes to date (this chain) are
process/citation/landing defects, NOT symbolic-algebra errors —
the marginal defect class Lean covers has zero caught instances so
far. Priced accordingly: legitimate to DECLINE or DEFER wholesale.

DECISION SLOT (user): fund-now (scope above) / defer-to-F2-entry /
decline. Recorded in BLOCCATO on answer.
