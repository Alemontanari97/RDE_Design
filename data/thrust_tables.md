# Analytical RDE thrust models - all propellant combinations

Conditions: phi = 1, p1 = 1 atm, T1 = 300 K, Pa = 1 atm (sea level). CJ states: SD Toolbox (Caltech) on Cantera 3.2; GRI-3.0 for H2/CH4/C2H4/C2H2/C3H8; kerosene = n-dodecane surrogate (Reitz thermo + GRI NOx thermo, equilibrium-only reduced set, validated to +0.19% on U_CJ vs the full mechanism).

Models: **PH** = Shepherd-Kasahara pressure-history, F/Mdot = K(P_CJ-P1)/(rho1 U_CJ) + [u_c + (P1-Pa)/(rho1 u_c)], K = 1.02 (air) / 1.54 (O2), u_c = 300 m/s; **AX** = SK axial flow, w = sqrt(2(h1-h(P,s2))) on the equilibrium isentrope through the CJ state, T/Mdot = w + (P-Pa)/(rho w) at the sonic point (matched-exit in parentheses conceptually within ~2-9%); **ST** = Stechmann-Heister mass-weighted blowdown cycle. gamma_e = equilibrium isentropic exponent rho2 a_eq^2/P2 at CJ. Isp_f = (T/Mdot)/(Y_f g0).

## Table 1 - CJ state and specific thrust (all combos, phi=1, 1 atm, 300 K)

| Mixture | U_CJ [m/s] | p2/p1 | T_CJ [K] | gamma_e | Y_f | T/Mdot PH [m/s] | T/Mdot AX [m/s] | Isp_f PH [s] | Isp_f AX [s] | Isp_f CFD lit [s] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| H2/air | 1969 | 15.46 | 2944 | 1.163 | 0.0285 | 1194 | 1353 | 4268 | 4838 | 4860^a |
| H2/O2 | 2836 | 18.64 | 3678 | 1.129 | 0.1119 | 2290 | 2124 | 2086 | 1936 | - |
| CH4/air | 1803 | 17.04 | 2778 | 1.168 | 0.0552 | 1119 | 1255 | 2068 | 2319 | - |
| CH4/O2 | 2390 | 29.14 | 3723 | 1.131 | 0.2004 | 1995 | 1903 | 1015 | 968 | - |
| C2H4/air | 1824 | 18.21 | 2924 | 1.161 | 0.0638 | 1134 | 1302 | 1813 | 2082 | 1990^a |
| C2H4/O2 | 2374 | 33.18 | 3934 | 1.139 | 0.2262 | 1979 | 1905 | 892 | 859 | 700^a |
| C2H2/air | 1867 | 18.97 | 3112 | 1.158 | 0.0705 | 1155 | 1356 | 1671 | 1961 | - |
| C2H2/O2 | 2425 | 33.59 | 4211 | 1.153 | 0.2456 | 2004 | 1929 | 832 | 801 | - |
| C3H8/air | 1800 | 18.10 | 2821 | 1.166 | 0.0603 | 1120 | 1272 | 1893 | 2149 | - |
| C3H8/O2 | 2357 | 35.93 | 3825 | 1.134 | 0.2161 | 1973 | 1912 | 931 | 902 | 1070^a |
| Kerosene(C12H26)/air | 1796 | 18.61 | 2836 | 1.165 | 0.0628 | 1120 | 1276 | 1817 | 2071 | - |
| Kerosene(C12H26)/O2 | 2341 | 40.61 | 3882 | 1.137 | 0.2235 | 1963 | 1915 | 896 | 874 | - |

^a Schwer & Kailasanath (2013) unsteady 2-D CFD, computed at 1.5 atm / 255 K fill - see Table 2 for the same-condition comparison. PH includes term II with u_c = 300 m/s (at p1 = Pa the pressure part vanishes).

## Table 2 - Literature convergence at SK Table-1 conditions (1.5 atm / 255 K fill)

| Case | U_CJ me/SK [m/s] | P_CJ me/SK [MPa] | gamma_e me/SK | Isp_f PH me/SK [s] | dPH% | Isp_f AX me/SK [s] | dAX% | CFD S&K [s] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| H2-air | 1983 / 1982 | 2.78 / 2.75 | 1.169 / 1.169 | 4702 / 4706 | -0.1 | 5395 / 5383 | +0.2 | 4860 |
| C2H4-air | 1836 / 1836 | 3.28 / 3.24 | 1.165 / 1.165 | 1957 / 1975 | -0.9 | 2285 / 2280 | +0.2 | 1990 |
| C2H4-O2 | 2403 / 2402 | 6.06 / 5.97 | 1.142 / 1.142 | 937 / 704 | +33.1 | 912 / 911 | +0.1 | 700 |
| C3H8-O2 | 2384 / 2383 | 6.55 / 6.46 | 1.137 / 1.137 | 974 / 1016 | -4.1 | 953 / 952 | +0.1 | 1070 |

Axial model reproduced to +-0.2% on 4/4 cases; PH reproduced on 3/4 (the published C2H4-O2 value of 704 s is inconsistent with the model equations and its own twin case C3H8-O2 - see vv_thrust.md, anomaly A1).

## Table 3 - Stechmann-Heister mass-weighted cycle Isp (fuel-O2, fill 1 atm / 300 K)

| Mixture | PR = p_CJ/p1 | gamma_e | c*_mw [m/s] | Isp mw eps=1 SL [s] | Isp mw aerospike SL [s] | Isp mw eps=1 vac [s] | Isp_f aerospike SL [s] | mw/time-avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| H2/O2 | 18.6 | 1.129 | 2181 | 237.1 | 265.7 | 274.0 | 2374 | 1.199 |
| CH4/O2 | 29.1 | 1.131 | 1814 | 205.7 | 239.2 | 227.9 | 1194 | 1.212 |
| C2H4/O2 | 33.2 | 1.139 | 1786 | 204.8 | 240.2 | 224.6 | 1062 | 1.217 |
| C2H2/O2 | 33.6 | 1.153 | 1806 | 207.6 | 242.7 | 227.4 | 989 | 1.220 |
| C3H8/O2 | 35.9 | 1.134 | 1777 | 204.7 | 242.2 | 223.3 | 1121 | 1.218 |
| Kerosene(C12H26)/O2 | 40.6 | 1.137 | 1757 | 204.2 | 243.8 | 221.0 | 1091 | 1.221 |

Isp = total-propellant-mass based (rocket convention); Isp_f = fuel-based. eps=1: exit = throat (no nozzle), directly comparable to the SK sonic axial model; ideal aerospike: Pe = Pa throughout the blowdown (Eq. 10). Low absolute values reflect the 1-atm fill pressure (Stechmann Table 1 cases run 20-200 atm chambers).

## Cross-model consistency (total-mass Isp [s], fuel-O2, sea level)

| Mixture | PH | AX sonic | ST eps=1 | spread % |
|---|---:|---:|---:|---:|
| H2/O2 | 233 | 217 | 237 | 9.0 |
| CH4/O2 | 203 | 194 | 206 | 5.8 |
| C2H4/O2 | 202 | 194 | 205 | 5.3 |
| C2H2/O2 | 204 | 197 | 208 | 5.4 |
| C3H8/O2 | 201 | 195 | 205 | 4.9 |
| Kerosene(C12H26)/O2 | 200 | 195 | 204 | 4.4 |
