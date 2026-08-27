# Rao (1961), "Spike Nozzle Contour for Optimum Thrust" — TRANSCRIBED DATA

G. V. R. Rao, Rocketdyne, Canoga Park, California.
*Planetary and Space Science*, Vol. 4, pp. 92–101 (1961).

PROVENANCE: transcribed 2026-08-13 from the full text supplied by the
owner (scanned PDF, OCR). THIS FILE IS THE MACHINE-READABLE COPY used
by `validation/rao1961_oracle.py`; the PDF itself is the artifact of
record and should sit beside it. Every number below is as printed;
transcription caveats are declared in §5 and are NOT silently repaired.

Until 2026-08-13 this paper had never been obtained and the project
record carried its tabulated numbers as "unverifiable and internally
inconsistent" (N-74, GENO side). §5 replaces that verdict with a
specific list.

---

## 1. The worked example

    gamma          = 1.23
    M_E            = 2.4          (Mach at the cowl lip, on the control surface)
    theta_E        = -8.25 deg    (flow angle there; Rao measures theta NEGATIVE from axial)
    p_b            = 0            (base pressure ASSUMED ZERO in all his computations)
    => p_a         = 0.0355 P_c   (a posteriori, from his Eq. (8))
    => X_D/R_E     = 1.164
       R_D/R_E     = 0.137
       pi R_E^2/A* = 3.81         (area ratio, epsilon)
       C_F         = 1.58         (vacuum thrust coefficient, his Eq. (12))

Text, p. 95: the ideal spike for the SAME area ratio 3.81 has
`X/R_E = 2.428` and `C_F = 1.591`, so the optimum reaches "0.993 times
the ideal thrust coefficient ... even though the length is only 47.9
per cent of the length of the ideal spike nozzle".

Second example: `M_E = 3.2`, `theta_E = -6 deg` -> `eps = 10.69`,
`L/R_E = 1.731`.

## 2. Table 1 — contour, gamma = 1.23, eps = 3.81, L/R_E = 1.164

    X/R_E      R/R_E     theta[deg]
     0.000     1.0000     ---        # cowl-lip location
    -0.109     0.9165    -51.92      # throat location on spike contour
    -0.016     0.7820    -50.10
     0.034     0.7280    -45.18
     0.087     0.6780    -41.21
     0.132     0.6400    -38.44
     0.192     0.5960    -35.59
     0.267     0.5450    -32.73
     0.314     0.5160    -31.21
     0.367     0.4840    -29.72
     0.429     0.4500    -28.23
     0.502     0.4130    -26.75
     0.588     0.3710    -25.32
     0.690     0.3240    -23.92
     0.815     0.2710    -22.59
     0.969     0.2090    -21.47
     1.164     0.1370    -19.73      # end point of the computed contour

## 3. Table 2 — contour, gamma = 1.23, eps = 10.69, L/R_E = 1.731

    X/R_E      R/R_E     theta[deg]
     0.000     1.0000     ---        # cowl-lip location
    -0.045     0.9856    -71.43      # throat location on spike contour
    -0.021     0.9170    -63.06
    -0.002     0.8860    -56.23
     0.024     0.8520    -50.27
     0.054     0.8180    -45.73
     0.101     0.7750    -40.56
     0.173     0.7180    -35.52
     0.245     0.6700    -32.04
     0.347     0.6110    -28.45
     0.413     0.5770    -26.66
     0.494     0.5370    -24.90
     0.594     0.4930    -23.12
     0.717     0.4420    -21.32
     0.874     0.3840    -19.56
     1.076     0.3160    -17.85
     1.347     0.2330    -16.34
     1.731     0.1260    -14.94      # end point of the computed contour

## 4. Table 3 — comparison of thrust coefficients

    description                          L/R_E   R_D/R_E   C_F      L/L_i   C_F/C_Fi
    optimum thrust contour, eps=10.69    1.731   0.126     1.7269   0.529   0.9967
    ideal spike contour,    eps=10.69    3.271   0.000     1.7326   1.00    1.00
      above contour truncated            1.731   0.23 [*]  1.7252   0.529   0.9957
    optimum thrust contour, eps=3.81     1.164   0.137     1.5804   0.479   0.9934
    ideal spike contour,    eps=3.81     2.433   0.000     1.5909   1.00    1.00
      above contour truncated            1.164   0.245     1.5783   0.479   0.9921

C_F here is the VACUUM thrust coefficient (his §4, below Eq. (12)).

THE ROW THAT MATTERS FOR THIS PROJECT: at equal length the variational
optimum beats the truncated ideal by
  eps = 3.81 : 1.5804 / 1.5783 = +0.133 %   (C_F/C_Fi 0.9934 vs 0.9921)
  eps = 10.69: 1.7269 / 1.7252 = +0.099 %   (           0.9967 vs 0.9957)
This is the SAME comparison the S23 paired ladder made on our world,
where the answer was -0.011 % +- 0.017 % (zero within band).

## 5. TRANSCRIPTION CAVEATS — declared, not repaired

  C-1  [*] Table 3, "above contour truncated" at eps=10.69, the R_D/R_E
       cell OCRs as "2.3". It cannot be 2.3: R_D/R_E is a radius
       fraction < 1, the un-truncated ideal has 0, and the eps=3.81
       twin reads 0.245. Recorded here as 0.23 with the reading
       DECLARED; verify against a clean scan before any use. No check
       in the carrier depends on it.
  C-2  Eqs. (8) and (9) OCR with p_b at point E and p_a at point D.
       That is inverted with respect to his own Eq. (3), where p_a acts
       on the lip area pi R_E^2 and p_b on the base pi R_D^2, and with
       respect to the caution paragraph, which discusses Eq. (9) as the
       BASE-pressure relation. Physical reading (and GENO's
       implementation): Eq. (8) at E carries p_a, Eq. (9) at D carries
       p_b.
  C-3  Text p. 95 gives the ideal-spike length ratio as 2.428; Table 3
       gives 2.433 for the same design (0.21 % apart). Both are
       transcribed as printed. This is the sharpest internal
       discrepancy found and it is SMALL.
  C-4  Table 1 row 2 (the throat) has X/R_E = -0.109 while row 3 has
       -0.016, i.e. X is NOT monotone across the first three rows. The
       throat sits upstream of the lip on the spike contour, so a
       non-monotone start is physically possible; flagged because a
       naive interpolation of the table will break on it.
  C-5  Fig. 5's axis label and several numerals in the scanned figures
       are illegible; NO figure-read value is transcribed here. Only
       table and body-text numbers are used.

## 6. Equation map (his symbols -> this project's objects)

    Eq. (5)   phi = theta - alpha            the control surface IS a characteristic
    Eq. (6)   w cos(-theta-alpha)/cos alpha = -lambda_2      <- our f2 invariant
    Eq. (7)   R rho w^2 sin^2 theta tan alpha = -lambda_3    <- the length multiplier
    Eq. (8)   [(p-p_a)/(rho w^2/2)] cot alpha = sin(-2 theta) at E   (see C-2)
    Eq. (9)   [(p-p_b)/(rho w^2/2)] cot alpha = sin(-2 theta) at D   (see C-2)
    Eq. (10)  d theta + (dw/w) cot alpha - [sin alpha sin theta / sin(theta-alpha)] dR/R = 0
    Eq. (11)  area ratio from the control-surface integral
    Eq. (12)  C_F from the control-surface integral (VACUUM)

## 7. Statements of his that bear on open questions here

  - "no restriction need be placed on the diameter of the spike ... the
    radius of the cowl lip can be also varied" — R_E is a free
    parameter of the family, which is the scale degree of freedom the
    GENO type-8 notes name as the only honest route to a third
    simultaneous constraint.
  - "it is not necessary that the spike contour terminate in a vertex
    on the axis" — truncation is inside his formulation, not a
    post-hoc cut.
  - "the spike contours computed for optimum thrust have LESS SURFACE
    AREA than the truncated ideal contours".
  - "changes in this portion of the contour [D to C, the base] would
    not alter the thrust performance", given p_b = 0.
