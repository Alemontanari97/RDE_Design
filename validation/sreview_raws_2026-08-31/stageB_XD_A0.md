# Stage-B item XD — "The two-level Richardson safety constant K = 4 is universal across every band site of the certificate stack" — ADVOCATE position (round 0)

## Question
Can the single numeral K_RICH = 4 be used as the safety constant of every two-level Richardson band in the certificate stack (contour bands, objective bands, gradient tolerances, margin floors, ship-time backoffs), so that no per-site derivation of the safety factor is needed?

## Proposed falsifier (for agreement)
A band site where the observed convergence order p_obs measured from three resolutions is below the value at which the two-level estimate with K = 4 still covers the true error (the record's own threshold p_obs >= 0.415 at r = 2), i.e. a site where K = 4 under-covers the measured error.

## Position
1. The two-level Richardson estimate with a safety factor is the standard practice (Roache's GCI uses Fs = 3 for two grids, 1.25 for three grids [KNOWLEDGE, full]); a single conservative constant K = 4 exceeds the two-grid factor and is therefore universally safe.
2. The record uses K_RICH in eight roles already (ledger C42) without any measured failure; universality is the simplest reading and avoids a proliferation of derived constants.
3. Consequence for the decisive comparison: the band stack of the two arms uses one safety constant, making the bands directly comparable.
4. Cost: zero; credibility: neutral-to-positive (simplicity).

## Anchors
docs/choice_ledger.yaml C41, C42, C43; M0 VI.6; Roache 1994/1997 [KNOWLEDGE, full].
