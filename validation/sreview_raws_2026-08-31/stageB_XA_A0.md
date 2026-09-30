# Stage-B item XA — "The certifiability frontier IS the physical validity boundary" — ADVOCATE position (round 0)

## Question
Should the design loop treat the boundary of the certifiable set K_disc (designs whose marched state passes every per-cell certificate) as the physical shock-free validity boundary A_0 of the per-phase field (Sternin/Rao-Beck boundary function), so that a certification failure is read as a PHYSICAL constraint (the design has left the shock-free class) rather than as a numerical-class artifact?

## Proposed falsifier (for agreement)
A certification failure occurring at a design whose Sternin/Rao-Beck validity monitor is HEALTHY everywhere (validity value far above its threshold at every rejected cell) falsifies the identification K_disc ≈ A_0 on that instance; conversely, failures concentrated exactly where the validity monitor approaches zero support it.

## Position
1. The per-cell Newton certificate of the fitted march fails when the local characteristic geometry degenerates — precisely the mechanism by which Sternin's validity boundary is approached (the boundary function val → 0 as the wall-reflected characteristics coalesce; M0 VI.2 gives the closed-form monitor val = [Λ·B·(A+B) − (A−B)]/[1 + Λ·(A+B)]). Where the physics degenerates, the numerics degenerate: the two boundaries coincide.
2. The S20 obstruction (five rejected designs crawling along the frontier with cert_worst ≈ 1.06-2.46 while the certified prefix stayed bit-identical) is exactly the signature of a design walking INTO the forbidden zone: the optimizer pushes toward a DEF-type coalescence at the control surface (Rao-Beck AIAA 94-3264 Eq. (4)), and the certificate refuses it. Reading this as a numerical-class artifact throws away the physics.
3. Consequence for the road: the margin-constrained formulation with a KS-aggregated fold margin (M0 Part VI ladder) is the correct treatment because the constraint IS the physical one; no re-formulation of the certifier is needed, and the S22 governor [X-MGOV] should be read as enforcing Sternin's boundary.
4. Cost: zero new machinery; credibility of the decisive comparison RISES because certification failures become physically interpretable (a referee accepts "shock-free class boundary" more readily than "numerical class construction").

## Anchors
M0 VI.2 (:3111-3116) validity monitor; M0 Part VI LADDER + margin multiplier; memory of record of the S20 adjudication (root cause = formulation gap, Sternin boundary as the forbidden zone); Rao-Beck 1994 [KNOWLEDGE, full]; ledger C28 (cert-frontier representation).

## What would make me abandon it
The falsifier above firing on a recorded instance: a certification failure at cells where the validity monitor is healthy (val ≫ threshold), which would show bd(K_disc) is a numerical-class boundary and not A_0.
