#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cycles.py — Detonation-cycle thermodynamics after Wintenberger & Shepherd, validated.

Lecture-repo edition of project_build/src/cycles/cycles.py: verbatim physics and
validation stages; only import paths and file locations are adapted to this repo
(vendored sdtoolbox/ and data/ at the repo root, shared plot style in src/).

Implements, with equation-level references to the two source papers:

  [A] E. Wintenberger, J.E. Shepherd, "Thermodynamic Analysis of Combustion Processes
      for Propulsion Systems", AIAA 2004-1033 (2004).                        (Eqs. A#)
  [B] E. Wintenberger, J.E. Shepherd, "Thermodynamic Cycle Analysis for Propagating
      Detonations", J. Propulsion & Power 22(3):694-698, 2006.               (Eqs. B#)

Content
-------
1. ONE-GAMMA GAS DYNAMICS of steady combustion waves (pure NumPy):
   * classical Hugoniot at fixed static upstream state — jump ratios (A19-A20),
     M2(M1) from the energy equation (A21, quadratic in M2^2), entropy rise (A22);
   * entropy partition  s2-s1 = ds_min + ds_irr  (A23) computed from stagnation
     quantities: ds_min = Cp ln(Tt2/Tt1) (A31), ds_irr = -R ln(Pt2/Pt1) (A32);
   * stagnation Hugoniot at fixed upstream stagnation state (A40), weak-detonation
     asymptote (A41), steady-detonation existence limit q̃t < 1/(g^2-1) (A42);
   * ideal steady engine in flight: eta = 1 - (CpT0/qc)[(1+q̃t) e^(ds_irr/Cp) - 1]
     (A38), bounded by the Brayton value 1 - T0/Tt1 (A39);
   * closed cycles: Fickett-Jacobs one-gamma (B3 = A57 = Heiser & Pratt) with
     CJ Mach number M_CJ = sqrt(H+1)+sqrt(H), H = (g^2-1) qc/(2 g R T2) (B2);
     Brayton (A59); Humphrey (A60). Precompression: T2 = T1 pi_c^((g-1)/g), the
     pi_c factors cancel and (A57) holds with M_CJ evaluated at T2 (Paper A, A58).

2. FICKETT-JACOBS CYCLE WITH REAL (EQUILIBRIUM) THERMOCHEMISTRY — Cantera 3.2 +
   Shepherd's SD Toolbox. Paper-B state numbering: 1 initial reactants (T1,P1);
   2 isentropically compressed reactants (pi_c = P2/P1, frozen composition);
   3/4 CJ detonation products (moving / brought to rest — same thermodynamic
   state); 5 products expanded isentropically (shifting equilibrium) to P1;
   6 products cooled to T1 at P1.  Net specific work of the closed piston cycle
   w_net = h1 - h5 (First Law, A48/B1: only the 5->1 leg exchanges heat), so

       eta_FJ = (h1 - h5)/qc ,   qc = h1 - h6   (B1).

   Humphrey (UV-equilibrate at state 2) and Brayton (HP-equilibrate at P2) are
   computed from the same compressed state and the same formula with their own
   post-expansion enthalpy — the fixed-pi_c and fixed-peak-pressure comparisons
   of Paper A Figs. 26-27 (= Paper B Fig. 5).

3. THE ROTATING-VS-STANDING POINT (lecture figure fig_eta_fixed_stag):
   at the same flight condition M0 and the same qc/(Cp T0), a *standing* CJ wave
   (fixed stagnation state, A38 with ds_irr from the stagnation-Hugoniot CJ point)
   is the worst steady combustion mode, while a *propagating* CJ wave into the
   ram-compressed static charge (FJ cycle, A57 with M_CJ at T2 = Tt0 — the
   idealization relevant to PDE/RDE) beats even the ideal Brayton cycle.
   NB: the propagating/rotating reading is the lecture's interpretive step; the
   papers treat the propagating case as a generic closed system.

gamma bookkeeping (see validation/gamma_audit.md): all real-chemistry results here use
full shifting-equilibrium states — no constant gamma anywhere. Where a gamma is
*reported* per mixture, both values are given and labelled: gamma_e_CJ =
rho*a_eq^2/P at the CJ state (equilibrium isentropic exponent, the one used by
Shepherd-Kasahara as "gamma_e") and gamma_fr_CJ = cp/cv of the CJ products
(frozen). One-gamma model figures state their gamma explicitly (products value).

Provenance of the deprecated deck claim "p_t2/p_t1 ~ 0.0136" (standing detonation):
reproduced by this module as the total-pressure ratio across a complete CJ wave in
the one-gamma model with gamma = 1.2 and q/CpT1 = 5.24 (chosen to give M_CJ ~ 5.0):
Pt2/Pt1 = [(1+g M^2)/(1+g)] * [(1+(g-1)/2)/(1+(g-1)/2 M^2)]^(g/(g-1)) = 0.0135
(old scripts/validate.py sec. 6 / figs_more.py). It is NOT a number from either
assigned paper, and it applies the products' gamma (1.2) to the *reactant* ram
compression (gamma ~ 1.4), overstating the loss ~5x. Supported values (gamma=1.4):
0.074 at the classical-Hugoniot CJ benchmark (q̃=4, M_CJ=4.60) and 0.054 at the
stagnation-Hugoniot CJ benchmark (q̃t=0.8, M_CJ=5.00). A value of order 0.014
would need q̃t near the existence limit — cf. W&S AIAA 2003-0714 (not assigned).

Usage (stages keep each run short; results merge into data/cycles_ws.json):
    python src/cycles/cycles.py onegamma            # analytic anchors (instant)
    python src/cycles/cycles.py fj [--slice 0:6]    # eta_FJ, 12 mixtures (Cantera)
    python src/cycles/cycles.py sweep [--pics 1,2,5] [--mix CH4]  # 3-cycle pi_c sweep
    python src/cycles/cycles.py sweep --brayton-ext # Brayton-only pi_c 30..100
    python src/cycles/cycles.py validate            # -> data/cycles_validation.md
    python src/cycles/cycles.py plot                # -> figs/fig_*.png (7 figures)
    python src/cycles/cycles.py all                 # everything, in order
Runs from anywhere: paths resolve relative to this file.
Rev 2026-07-09: vN point on fig_cycles_pv rendered by sampling the Rayleigh
function (log-axis collinearity of 2, CJ, vN); p_vN/p_CJ stored and validated.
"""
import argparse, datetime, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # repo root (src/cycles -> repo)
DATA = os.path.join(ROOT, 'data')
JSON_PATH = os.path.join(DATA, 'cycles_ws.json')
VAL_PATH  = os.path.join(DATA, 'cycles_validation.md')
DODEQ = os.path.join(DATA, 'dodecane_eq_thermo.yaml')
sys.path.insert(0, ROOT)                               # vendored SD Toolbox (sdtoolbox/)
sys.path.insert(0, os.path.join(ROOT, 'src'))          # shared plot style (src/style.py)

# ----------------------------------------------------------------------------
# 0. incremental JSON store
# ----------------------------------------------------------------------------
def load_store():
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH) as f: return json.load(f)
    return {}

def save_section(name, payload):
    d = load_store()
    if name in d and isinstance(d[name], dict) and isinstance(payload, dict):
        d[name].update(payload)
    else:
        d[name] = payload
    d.setdefault('meta', {})
    d['meta'].update({
        'script': 'src/cycles/cycles.py',
        'updated': datetime.date.today().isoformat(),
        'sources': ['AIAA 2004-1033 (Paper A)', 'JPP 22(3):694-698 2006 (Paper B)'],
        'state_numbering': 'Paper B: 1 init, 2 compressed, 3/4 CJ, 5 expanded to P1, 6 cooled to T1',
        'gamma_note': ('real-chemistry results are full shifting-equilibrium (no constant gamma); '
                       'gamma_e_CJ = rho*a_eq^2/P at CJ (equilibrium isentropic exponent), '
                       'gamma_fr_CJ = cp/cv frozen at CJ — do not mix (see validation/gamma_audit.md)'),
        'claim_0136': ('deprecated: 0.0136 = one-gamma Pt2/Pt1 across full CJ wave with gamma=1.2, '
                       'q/CpT1=5.24 (old validate.py sec.6); not in the papers; products gamma applied '
                       'to reactant ram compression. Supported (gamma=1.4): 0.074 classical q~=4, '
                       '0.054 stagnation q~t=0.8.'),
    })
    with open(JSON_PATH, 'w') as f:
        json.dump(d, f, indent=1, default=float)
    print(f'[cycles_ws] wrote section "{name}" -> {JSON_PATH}')

# ----------------------------------------------------------------------------
# 1. one-gamma model (Paper A Sec. II-V, Paper B Eqs. 2-3)
# ----------------------------------------------------------------------------
def cj_mach(qhat, g):
    """CJ Mach numbers, Eq. (B2): M_CJ = sqrt(H+1) +/- sqrt(H), H = (g+1) qhat / 2,
    qhat = qc/(Cp T) at the pre-wave temperature. '+' root = detonation CJ_U,
    '-' root = deflagration CJ_L (tangency of Rayleigh line and Hugoniot)."""
    H = 0.5 * (g + 1.0) * qhat
    return np.sqrt(H + 1.0) + np.sqrt(H), np.sqrt(H + 1.0) - np.sqrt(H)

def jump_ratios(M1, M2, g):
    """Static jump ratios across a steady combustion wave, Eqs. (A19)-(A20).
    Returns P2/P1, v2/v1, T2/T1."""
    p = (1.0 + g * M1**2) / (1.0 + g * M2**2)                      # (A20)
    v = (M2**2 * (1.0 + g * M1**2)) / (M1**2 * (1.0 + g * M2**2))  # 1/(A19)
    return p, v, p * v

def hugoniot_M2sq(M1, qhat, g):
    """Classical Hugoniot: solve the energy equation (A21) for M2^2 at given M1
    and qhat = qc/CpT1 (fixed static upstream state). Quadratic in x = M2^2:
      x^2 [L g^2 - C (g-1)/2] + x [2 L g - C] + L = 0,
      L = qhat + 1 + (g-1) M1^2 / 2,   C = (1 + g M1^2)^2 / M1^2.
    Returns (x_small, x_large) or (nan, nan) if no real solution."""
    L = qhat + 1.0 + 0.5 * (g - 1.0) * M1**2
    C = (1.0 + g * M1**2)**2 / M1**2
    a = L * g**2 - 0.5 * C * (g - 1.0)
    b = 2.0 * L * g - C
    disc = b * b - 4.0 * a * L
    if disc < 0: return np.nan, np.nan
    r = np.sqrt(disc)
    x1, x2 = (-b - r) / (2 * a), (-b + r) / (2 * a)
    return min(x1, x2), max(x1, x2)

def stag_hugoniot_M2sq(M1, qt, g):
    """Stagnation Hugoniot: solve (A40) for M2^2 at given M1 and
    qt = qc/(Cp Tt1) (fixed upstream stagnation state). Quadratic in x = M2^2:
      x^2 [K g^2 - C (g-1)/2] + x [2 K g - C] + K = 0,
      K = (1+qt) M1^2 (1 + (g-1) M1^2/2),   C = (1 + g M1^2)^2."""
    K = (1.0 + qt) * M1**2 * (1.0 + 0.5 * (g - 1.0) * M1**2)
    C = (1.0 + g * M1**2)**2
    a = K * g**2 - 0.5 * C * (g - 1.0)
    b = 2.0 * K * g - C
    disc = b * b - 4.0 * a * K
    if disc < 0: return np.nan, np.nan
    r = np.sqrt(disc)
    x1, x2 = (-b - r) / (2 * a), (-b + r) / (2 * a)
    return min(x1, x2), max(x1, x2)

def stag_cj_mach(qt, g):
    """CJ points of the stagnation Hugoniot: setting M2 = 1 in (A40) gives
      y^2 [(g^2-1)(1+qt) - g^2] + 2 y [(g+1)(1+qt) - g] - 1 = 0,  y = M1^2.
    Returns (M_CJU or nan, M_CJL). The detonation root exists iff
    qt < 1/(g^2-1) — the existence condition (A42)."""
    a = (g**2 - 1.0) * (1.0 + qt) - g**2
    b = 2.0 * ((g + 1.0) * (1.0 + qt) - g)
    disc = b * b + 4.0 * a
    if disc < 0: return np.nan, np.nan
    r = np.sqrt(disc)
    roots = np.array([(-b - r) / (2 * a), (-b + r) / (2 * a)])
    roots = np.sort(roots[roots > 0])
    if len(roots) == 2:   return np.sqrt(roots[1]), np.sqrt(roots[0])
    elif len(roots) == 1: return np.nan, np.sqrt(roots[0])   # qt above (A42) limit
    return np.nan, np.nan

def entropy_partition(M1, M2, g):
    """Entropy rise and its partition across the wave (perfect gas).
    Returns dict with ds/R total (A22), ds_min/R (A31), ds_irr/R (A32),
    Pt2/Pt1 and Tt2/Tt1."""
    p, v, T = jump_ratios(M1, M2, g)
    f = lambda M: 1.0 + 0.5 * (g - 1.0) * M**2
    Tt = T * f(M2) / f(M1)
    Pt = p * (f(M2) / f(M1))**(g / (g - 1.0))
    ds  = (g / (g - 1.0)) * np.log(T) - np.log(p)      # (A22)
    dsm = (g / (g - 1.0)) * np.log(Tt)                 # (A31)
    return dict(P2P1=p, v2v1=v, T2T1=T, ds_R=ds, dsmin_R=dsm,
                dsirr_R=-np.log(Pt), Pt2Pt1=Pt, Tt2Tt1=Tt)

def pt_ratio_cj_wave(M, g):
    """Total-pressure ratio across a complete CJ wave (M2 = 1) at wave Mach M:
    Pt2/Pt1 = [(1+gM^2)/(1+g)] [(1+(g-1)/2)/(1+(g-1)M^2/2)]^(g/(g-1)).
    Combination of (A20) and isentropic stagnation definitions (A25)."""
    f = lambda m: 1.0 + 0.5 * (g - 1.0) * m**2
    return (1.0 + g * M**2) / (1.0 + g) * (f(1.0) / f(M))**(g / (g - 1.0))

def pt_ratio_shock(M, g):
    """Inert normal-shock total-pressure ratio (the leading ZND shock)."""
    t1 = ((g + 1.0) * M**2 / 2.0 / (1.0 + 0.5 * (g - 1.0) * M**2))**(g / (g - 1.0))
    t2 = ((g + 1.0) / (2.0 * g * M**2 - (g - 1.0)))**(1.0 / (g - 1.0))
    return t1 * t2

def eta_steady(Q0, tau, dsirr_R, g):
    """Ideal steady engine in flight, Eq. (A38):
    eta = 1 - (CpT0/qc) [ (1 + qt) exp(ds_irr/Cp) - 1 ],
    with Q0 = qc/CpT0, tau = Tt1/T0 = 1+(g-1)M0^2/2, qt = Q0/tau.
    Bound (A39): eta <= 1 - 1/tau (ideal Brayton, ds_irr = 0)."""
    qt = Q0 / tau
    return 1.0 - (1.0 / Q0) * ((1.0 + qt) * np.exp(dsirr_R * (g - 1.0) / g) - 1.0)

def eta_fj_1g(qhat1, g, pic=1.0):
    """Fickett-Jacobs one-gamma efficiency, Eq. (B3) = (A57):
    eta = 1 - (CpT1/qc) [ (1/M^2) ((1+gM^2)/(1+g))^((g+1)/g) - 1 ],
    M = M_CJ evaluated at the precompressed temperature T2 = T1 pic^((g-1)/g)
    (A58: the pi_c factors cancel; qhat1 = qc/CpT1)."""
    tau = pic**((g - 1.0) / g)
    M, _ = cj_mach(qhat1 / tau, g)
    bracket = (1.0 / M**2) * ((1.0 + g * M**2) / (1.0 + g))**((g + 1.0) / g)
    return 1.0 - (bracket - 1.0) / qhat1

def eta_brayton_1g(pic, g):
    """Brayton, Eq. (A59): eta = 1 - pic^(-(g-1)/g). Independent of qc."""
    return 1.0 - pic**(-(g - 1.0) / g)

def eta_humphrey_1g(qhat1, g, pic=1.0):
    """Humphrey, Eq. (A60):
    eta = 1 - (CpT1/qc) [ (1 + g qhat1 pic^(-(g-1)/g))^(1/g) - 1 ]."""
    return 1.0 - ((1.0 + g * qhat1 * pic**(-(g - 1.0) / g))**(1.0 / g) - 1.0) / qhat1

def hugoniot_pv(vhat, qhat, g):
    """Classical Hugoniot P2/P1 as a function of v2/v1 (from A15 with A17-A18):
    P = [2(1+g qhat)/(g-1) - (v-1)] / [2 v/(g-1) + (v-1)].
    Passes through the CV point (v=1, P=1+g*qhat) and CP point (v=1+qhat, P=1);
    the segment between them has (P-1)/(v-1) > 0: forbidden (imaginary mass flux)."""
    num = 2.0 * (1.0 + g * qhat) / (g - 1.0) - (vhat - 1.0)
    den = 2.0 * vhat / (g - 1.0) + (vhat - 1.0)
    return num / den

def ds_R_pv(P, v, g):
    """Entropy rise from static ratios: ds/R = g/(g-1) ln(T2/T1) - ln(P2/P1)."""
    return (g / (g - 1.0)) * np.log(P * v) - np.log(P)

# ---- benchmark evaluation -------------------------------------------------
def classical_benchmark(g=1.4, qhat=4.0):
    """Spec Sec. 3.1: classical Hugoniot, fixed static state."""
    Mu, Ml = cj_mach(qhat, g)
    out = {}
    for tag, M in (('CJU', Mu), ('CJL', Ml)):
        d = entropy_partition(M, 1.0, g); d['M1'] = M
        d['irr_frac'] = d['dsirr_R'] / d['ds_R']
        out[tag] = d
    return out

def stagnation_benchmark(g=1.4, qt=0.8, M0=5.0):
    """Spec Sec. 3.2: stagnation Hugoniot, fixed stagnation state + engine at M0."""
    Mu, Ml = stag_cj_mach(qt, g)
    tau = 1.0 + 0.5 * (g - 1.0) * M0**2
    Q0 = qt * tau
    out = {'dsmin_R': (g / (g - 1.0)) * np.log(1.0 + qt),
           'q_limit': 1.0 / (g**2 - 1.0), 'Q0': Q0, 'tau': tau}
    for tag, M in (('CJU', Mu), ('CJL', Ml)):
        d = entropy_partition(M, 1.0, g); d['M1'] = M
        d['ds_R'] = out['dsmin_R'] + d['dsirr_R']   # common upstream isentrope
        d['eta_M0'] = eta_steady(Q0, tau, d['dsirr_R'], g)
        out[tag] = d
    out['CP'] = {'eta_M0': 1.0 - 1.0 / tau, 'ds_R': out['dsmin_R'], 'dsirr_R': 0.0}
    # weak-detonation asymptote (A41)
    out['M2_asymptote'] = np.sqrt((1.0 - (g - 1.0) * qt + np.sqrt(1.0 - (g**2 - 1.0) * qt))
                                  / (g * (g - 1.0) * qt))
    return out

def eta_vs_M0(g=1.4, Q0=4.8, M0=None):
    """eta(M0) for the four idealizations of Sec. 3 of this module's docstring.
    Returns dict of arrays; standing-detonation entries are nan below the
    existence limit (A42): M0_min = sqrt(2 (Q0 (g^2-1) - 1)/(g-1))."""
    if M0 is None: M0 = np.linspace(0.05, 8.0, 320)
    tau = 1.0 + 0.5 * (g - 1.0) * M0**2
    qt = Q0 / tau
    eta_cp = 1.0 - 1.0 / tau                       # (A39) ideal Brayton bound
    eta_dfl, eta_det, eta_fjr = [], [], []
    for t, q in zip(tau, qt):
        Mu, Ml = stag_cj_mach(q, g)
        eta_dfl.append(eta_steady(Q0, t, entropy_partition(Ml, 1.0, g)['dsirr_R'], g)
                       if np.isfinite(Ml) else np.nan)
        eta_det.append(eta_steady(Q0, t, entropy_partition(Mu, 1.0, g)['dsirr_R'], g)
                       if np.isfinite(Mu) else np.nan)
        eta_fjr.append(eta_fj_1g(Q0, g, pic=t**(g / (g - 1.0))))  # ram pi_c
    M0_min = np.sqrt(2.0 * (Q0 * (g**2 - 1.0) - 1.0) / (g - 1.0))
    return dict(M0=M0, eta_cp=eta_cp, eta_defl=np.array(eta_dfl),
                eta_det=np.array(eta_det), eta_fj_ram=np.array(eta_fjr),
                M0_min_det=M0_min, Q0=Q0, gamma=g)

def stage_onegamma():
    cb = classical_benchmark()
    sb = stagnation_benchmark()
    em = eta_vs_M0()
    fam = {'qcRT1': [10, 20, 30, 40], 'gamma': 1.2,
           'note': 'Paper A Fig. 22 family; qhat1 = (qc/RT1)*(g-1)/g'}
    for q in fam['qcRT1']:
        qh = q * (1.2 - 1.0) / 1.2
        fam[f'eta_pic1_q{q}']  = eta_fj_1g(qh, 1.2, 1.0)
        fam[f'eta_pic10_q{q}'] = eta_fj_1g(qh, 1.2, 10.0)
        fam[f'eta_pic50_q{q}'] = eta_fj_1g(qh, 1.2, 50.0)
    old = dict(gamma=1.2, qhat=5.24)
    Mold, _ = cj_mach(old['qhat'], old['gamma'])
    old['M_CJ'] = Mold; old['Pt2Pt1'] = pt_ratio_cj_wave(Mold, old['gamma'])
    payload = {
        'classical_g1.4_q4': {k: {kk: float(vv) for kk, vv in v.items()} for k, v in cb.items()},
        'stagnation_g1.4_qt0.8_M05': json.loads(json.dumps(sb, default=float)),
        'eta_M0_anchors': {
            'Q0': em['Q0'], 'gamma': em['gamma'], 'M0_min_det': float(em['M0_min_det']),
            'at_M0_5': {'eta_cp': float(np.interp(5.0, em['M0'], em['eta_cp'])),
                        'eta_defl': float(np.interp(5.0, em['M0'], em['eta_defl'])),
                        'eta_det': float(np.interp(5.0, em['M0'], em['eta_det'])),
                        'eta_fj_ram': float(np.interp(5.0, em['M0'], em['eta_fj_ram']))}},
        'family_A22': fam,
        'fig_A16': {f'g{g}_M{M}': float(eta_fj_1g(2.0 * ((M**2 - 1)**2 / (4 * M**2)) / (g + 1.0), g))
                    for g in (1.2, 1.1) for M in (2, 4, 6, 10)},
        'deprecated_0136_reproduction': {k: float(v) for k, v in old.items()},
        'pt_anchors': {'shock_only_M5_g1.4': float(pt_ratio_shock(5.0, 1.4)),
                       'cj_wave_M4.60_g1.4': float(pt_ratio_cj_wave(cb['CJU']['M1'], 1.4)),
                       'cj_wave_M5.00_g1.4': float(pt_ratio_cj_wave(5.0, 1.4))},
    }
    save_section('onegamma', payload)
    a = payload['eta_M0_anchors']['at_M0_5']
    print(f"  classical CJ det: ds/R={cb['CJU']['ds_R']:.3f} (irr {100*cb['CJU']['irr_frac']:.1f}%), "
          f"Pt2/Pt1={cb['CJU']['Pt2Pt1']:.4f} | CJ defl: ds/R={cb['CJL']['ds_R']:.3f} "
          f"(irr {100*cb['CJL']['irr_frac']:.1f}%)")
    print(f"  stagnation CJ det: ds/R={sb['CJU']['ds_R']:.3f}, Pt2/Pt1={sb['CJU']['Pt2Pt1']:.4f}, "
          f"eta(M0=5)={sb['CJU']['eta_M0']:.4f} | defl {sb['CJL']['eta_M0']:.4f} | CP {sb['CP']['eta_M0']:.4f}")
    print(f"  eta at M0=5: det {a['eta_det']:.3f}, defl {a['eta_defl']:.3f}, CP {a['eta_cp']:.3f}, "
          f"FJ-ram {a['eta_fj_ram']:.3f}; det exists for M0 > {payload['eta_M0_anchors']['M0_min_det']:.2f}")
    print(f"  deprecated 0.0136 reproduced: {old['Pt2Pt1']:.4f} at M_CJ={old['M_CJ']:.2f} "
          f"(g=1.2, q^=5.24) — one-gamma artifact, not a paper value")

# ----------------------------------------------------------------------------
# 2. real-chemistry cycles (Cantera + SD Toolbox)
# ----------------------------------------------------------------------------
# (label, composition, mechanism), phi = 1 throughout — thin view of the
# shared registry src/common/mixtures.py (same labels, X strings and
# mechanisms as before the refactor; kerosene = n-dodecane surrogate)
from src.common import mixtures as _mixreg
MIXTURES = _mixreg.cycles_view()

def _heat_of_combustion(mech, X, T1, P1):
    """qc = h1 - h6 (B1): reactants at (T1,P1) minus products equilibrated at
    (T1,P1). Route via HP then TP equilibration for robustness at 300 K."""
    import cantera as ct
    gas = ct.Solution(mech); gas.TPX = T1, P1, X
    h1 = gas.enthalpy_mass
    gas.equilibrate('HP')          # adiabatic products (hot, easy convergence)
    gas.TP = T1, P1
    gas.equilibrate('TP')          # cool at (T1,P1): state 6
    return h1 - gas.enthalpy_mass, gas.enthalpy_mass, 1.0 / gas.density

def _expand_eq(gas, P_end, n=40, path=None):
    """Shifting-equilibrium isentropic expansion to P_end (states on the
    equilibrium isentrope through the current state; A45 / SK 'h=h(P,s)')."""
    s = gas.entropy_mass
    for P in np.geomspace(gas.P, P_end, n):
        gas.SP = s, P
        gas.equilibrate('SP')
        if path is not None: path.append((1.0 / gas.density, gas.P))
    return gas

def three_cycles(label, X, mech, T1=300.0, P1=1e5, pic=1.0,
                 n_exp=40, want_paths=False, do_HB=True):
    """FJ / Humphrey / Brayton from the same initial and compressed states.
    Returns result dict (and path dict if want_paths)."""
    import cantera as ct
    from src.common.cj_core import cj_state          # canonical SDT CJ chain
    gas = ct.Solution(mech); gas.TPX = T1, P1, X
    h1, s1, v1 = gas.enthalpy_mass, gas.entropy_mass, 1.0 / gas.density
    qc, h6, v6 = _heat_of_combustion(mech, X, T1, P1)
    paths = {'comp': [(v1, P1)]}
    # state 2: frozen isentropic precompression of the reactants (B step b)
    P2 = pic * P1
    if pic > 1.0:
        for P in np.geomspace(P1, P2, 25):
            gas.SP = s1, P                      # composition frozen: no reaction
            if want_paths: paths['comp'].append((1.0 / gas.density, gas.P))
    T2, v2 = gas.T, 1.0 / gas.density
    a2_fr = gas.sound_speed
    res = dict(label=label, X=X, mech=os.path.basename(mech), T1=T1, P1=P1,
               pic=pic, T2=T2, qc_MJkg=qc / 1e6, v1=v1, v2=v2, v6=v6)
    # --- Fickett-Jacobs: CJ detonation into state 2 (B steps c-e) ---
    # canonical CJ chain via src/common/cj_core (adapter; same SDT calls,
    # same floating-point formulas as the historical inline block)
    cjr, prod = cj_state(X, p1=P2, T1=T2, mech=mech, return_gas=True)
    Ucj = cjr['U_CJ']
    res.update(U_CJ=Ucj, M_CJ=cjr['M_CJ'], P_CJ_bar=cjr['p2'] / 1e5,
               pipk_FJ=cjr['p2'] / P1, T_CJ=cjr['T2'], v_CJ=1.0 / cjr['rho2'],
               u_p=Ucj * (1.0 - (1.0 / cjr['rho2']) / v2),  # (A49): u_p = U(1-rho1/rho2)
               gamma_e_CJ=cjr['gamma_e'],
               gamma_fr_CJ=cjr['gamma_fr'])
    pf = [] if want_paths else None
    _expand_eq(prod, P1, n=n_exp, path=pf)                    # 4 -> 5
    res['eta_FJ'] = (h1 - prod.enthalpy_mass) / qc            # (B1)
    res['v5_FJ'] = 1.0 / prod.density
    if want_paths: paths['fj_exp'] = pf; paths['fj_cj'] = [res['v_CJ'], res['P_CJ_bar'] * 1e5]
    if do_HB:
        # --- Humphrey: constant-volume combustion at state 2 ---
        gh = ct.Solution(mech); gh.TPX = T2, P2, X
        gh.equilibrate('UV')
        res.update(pipk_H=gh.P / P1, T3_H=gh.T)
        ph = [] if want_paths else None
        if want_paths: ph.append((1.0 / gh.density, gh.P))
        _expand_eq(gh, P1, n=n_exp, path=ph)
        res['eta_H'] = (h1 - gh.enthalpy_mass) / qc
        res['v5_H'] = 1.0 / gh.density
        if want_paths: paths['hu_exp'] = ph
        # --- Brayton: constant-pressure combustion at P2 ---
        gb = ct.Solution(mech); gb.TPX = T2, P2, X
        gb.equilibrate('HP')
        res.update(pipk_B=pic, T3_B=gb.T, v3_B=1.0 / gb.density)
        pb = [] if want_paths else None
        if want_paths: pb.append((1.0 / gb.density, gb.P))
        _expand_eq(gb, P1, n=n_exp, path=pb)
        res['eta_B'] = (h1 - gb.enthalpy_mass) / qc
        res['v5_B'] = 1.0 / gb.density
        if want_paths: paths['br_exp'] = pb
    return (res, paths) if want_paths else res

def stage_fj(slice_str=None):
    """eta_FJ for the 12 mixtures at (300 K, 1 bar, pi_c = 1). Spec Sec. 3.3."""
    sel = MIXTURES
    if slice_str:
        i0, i1 = (int(t) if t else None for t in slice_str.split(':'))
        sel = MIXTURES[i0:i1]
    for label, X, mech in sel:
        # state 5 is a state function (equilibrium isentrope endpoint): a short
        # SP-equilibrate ladder suffices for eta; paths use n_exp=60 elsewhere.
        r = three_cycles(label, X, mech, do_HB=False, n_exp=12)
        keep = ('label X mech qc_MJkg U_CJ M_CJ P_CJ_bar T_CJ gamma_e_CJ '
                'gamma_fr_CJ u_p eta_FJ v1 v5_FJ').split()
        save_section('fj_mixtures', {label: {k: r[k] for k in keep}})
        print(f"  {label:14s} U_CJ={r['U_CJ']:7.1f} m/s  M_CJ={r['M_CJ']:5.2f}  "
              f"P_CJ={r['P_CJ_bar']:6.2f} bar  g_e={r['gamma_e_CJ']:.3f} "
              f"(g_fr={r['gamma_fr_CJ']:.3f})  qc={r['qc_MJkg']:5.2f} MJ/kg  "
              f"eta_FJ={r['eta_FJ']:.4f}", flush=True)

SWEEP_MIXES = {  # mix key -> (label, X, sweep section, pv-loop section)
    'C3H8': ('C3H8/air', 'C3H8:1,O2:5,N2:18.8', 'sweep_C3H8_air', 'pv_loops_pic5'),
    'CH4':  ('CH4/air',  'CH4:1,O2:2,N2:7.52',  'sweep_CH4_air',  'pv_loops_pic5_CH4'),
}

def stage_sweep(pics_str=None, brayton_ext=False, mix='C3H8'):
    """3-cycle pi_c sweep, stoichiometric (spec Sec. 3.4 / Figs. A26-A27).
    mix='C3H8': the papers' anchor mixture (Figs. A25-A27 = B2/B5), kept as
    validation basis. mix='CH4': lecture display mixture (standard fuel), same
    pipeline, checked against the spec fuel-air band. Stores pv-diagram paths
    at pi_c = 5 (Fig. B2/A25). --brayton-ext extends the Brayton curve alone
    to high pi_c for the fixed-peak-pressure comparison (C3H8 anchor only)."""
    label, X, sweep_sec, pv_sec = SWEEP_MIXES[mix]
    mech = 'gri30.yaml'
    if brayton_ext:
        import cantera as ct
        pts = []
        for pic in [30., 50., 70., 100.]:
            gas = ct.Solution(mech); gas.TPX = 300., 1e5, X
            h1, s1 = gas.enthalpy_mass, gas.entropy_mass
            qc, _, _ = _heat_of_combustion(mech, X, 300., 1e5)
            gas.SP = s1, pic * 1e5
            gas.equilibrate('HP')
            _expand_eq(gas, 1e5, n=25)
            pts.append(dict(pic=pic, eta_B=(h1 - gas.enthalpy_mass) / qc, pipk_B=pic))
            print(f"  Brayton pic={pic:5.1f}  eta={pts[-1]['eta_B']:.4f}")
        save_section('brayton_ext_C3H8_air', pts)
        return
    pics = [float(t) for t in (pics_str or '1,1.5,2,3,5,7,10,14,20').split(',')]
    store = load_store().get(sweep_sec, {'points': []})
    pts = {round(p['pic'], 4): p for p in store.get('points', [])}
    for pic in pics:
        want = abs(pic - 5.0) < 1e-9
        r = three_cycles(label, X, mech, pic=pic, n_exp=60 if want else 30,
                         want_paths=want)
        if want:
            r, paths = r
            save_section(pv_sec, {
                'comp': paths['comp'], 'fj_exp': paths['fj_exp'],
                'hu_exp': paths['hu_exp'], 'br_exp': paths['br_exp'],
                'states': {k: r[k] for k in ('v1 v2 v_CJ P_CJ_bar v5_FJ v5_H v5_B '
                                             'v3_B pipk_H v6 T2').split()},
                'pic': 5.0, 'label': label})
        keep = ('pic eta_FJ eta_H eta_B pipk_FJ pipk_H pipk_B M_CJ U_CJ '
                'P_CJ_bar T2 qc_MJkg').split()
        pts[round(pic, 4)] = {k: r[k] for k in keep}
        print(f"  pic={pic:5.2f}  eta FJ/H/B = {r['eta_FJ']:.4f}/{r['eta_H']:.4f}/"
              f"{r['eta_B']:.4f}   peak p/p1 = {r['pipk_FJ']:6.1f}/{r['pipk_H']:6.1f}/"
              f"{r['pipk_B']:5.1f}")
    save_section(sweep_sec,
                 {'T1': 300., 'P1': 1e5, 'X': X, 'mech': mech,
                  'points': [pts[k] for k in sorted(pts)]})

# ----------------------------------------------------------------------------
# 3. validation against specs/thermo_spec.md anchors
# ----------------------------------------------------------------------------
def stage_validate():
    d = load_store()
    og, fj = d.get('onegamma', {}), d.get('fj_mixtures', {})
    sw = d.get('sweep_C3H8_air', {}).get('points', [])
    bx = d.get('brayton_ext_C3H8_air', [])
    rows, section = [], [None]
    def row(name, paper, ours, tol, kind='abs', note=''):
        if ours is None or (isinstance(ours, float) and not np.isfinite(ours)):
            rows.append((section[0], name, paper, 'MISSING', '-', '-', 'FAIL', note)); return
        dev = ours - paper
        ok = abs(dev) <= tol if kind == 'abs' else abs(dev) <= tol * abs(paper)
        tstr = f'±{tol:g}' if kind == 'abs' else f'±{100*tol:g}%'
        rows.append((section[0], name, f'{paper:g}', f'{ours:.4g}',
                     f'{dev:+.3g}', tstr, 'PASS' if ok else 'FAIL', note))
    def brow(name, cond, note=''):
        rows.append((section[0], name, 'True', str(bool(cond)), '-', '-',
                     'PASS' if cond else 'FAIL', note))
    C = og.get('classical_g1.4_q4', {}); S = og.get('stagnation_g1.4_qt0.8_M05', {})
    section[0] = 'Classical Hugoniot (γ=1.4, q̃=4) — spec §3.1 [calc]'
    U, L = C.get('CJU', {}), C.get('CJL', {})
    row('M_CJ (detonation CJ_U)', 4.60, U.get('M1'), 0.005, 'rel')
    row('M_CJ (deflagration CJ_L)', 0.217, L.get('M1'), 0.005, 'rel')
    row('P2/P1 at CJ_U', 12.8, U.get('P2P1'), 0.01, 'rel')
    row('P2/P1 at CJ_L', 0.44, L.get('P2P1'), 0.01, 'rel')
    row('v2/v1 at CJ_U', 0.60, U.get('v2v1'), 0.01, 'rel')
    row('v2/v1 at CJ_L', 9.4, L.get('v2v1'), 0.01, 'rel')
    row('T2/T1 at CJ_U', 7.68, U.get('T2T1'), 0.005, 'rel')
    row('T2/T1 at CJ_L', 4.19, L.get('T2T1'), 0.005, 'rel')
    row('Δs/R at CJ_U (branch min)', 4.59, U.get('ds_R'), 0.005, 'rel')
    row('Δs/R at CJ_L (branch max)', 5.83, L.get('ds_R'), 0.005, 'rel')
    row('Δs_min/R at CJ_U', 1.98, U.get('dsmin_R'), 0.01, 'rel')
    row('Δs_min/R at CJ_L', 5.62, L.get('dsmin_R'), 0.01, 'rel')
    row('Δs_irr/R at CJ_U', 2.61, U.get('dsirr_R'), 0.01, 'rel')
    row('Δs_irr/R at CJ_L', 0.21, L.get('dsirr_R'), 0.01, 'abs')
    row('irreversible fraction, det [%]', 57.0, 100 * U.get('irr_frac', np.nan), 0.5, 'abs')
    row('irreversible fraction, defl [%]', 3.6, 100 * L.get('irr_frac', np.nan), 0.5, 'abs')
    row('p_t2/p_t1 at CJ_U', 0.074, U.get('Pt2Pt1'), 0.02, 'rel',
        'supported value replacing deprecated 0.0136')
    row('p_t2/p_t1 at CJ_L', 0.81, L.get('Pt2Pt1'), 0.02, 'rel')
    section[0] = 'Stagnation Hugoniot (γ=1.4, q̃t=0.8) — spec §3.2 [calc]'
    U, L, P = S.get('CJU', {}), S.get('CJL', {}), S.get('CP', {})
    row('M_CJ_U (stagnation)', 5.00, U.get('M1'), 0.005, 'rel')
    row('M_CJ_L (stagnation)', 0.415, L.get('M1'), 0.005, 'rel')
    row('P2/P1 at CJ_U', 15.0, U.get('P2P1'), 0.01, 'rel')
    row('P2/P1 at CJ_L', 0.52, L.get('P2P1'), 0.01, 'abs')
    row('v2/v1 at CJ_U', 0.60, U.get('v2v1'), 0.01, 'rel')
    row('v2/v1 at CJ_L', 3.00, L.get('v2v1'), 0.01, 'rel')
    row('Δs/R at CJ_U', 4.98, U.get('ds_R'), 0.005, 'rel')
    row('Δs/R at CJ_L', 2.20, L.get('ds_R'), 0.005, 'rel')
    row('Δs_min/R (flat floor, A37)', 2.06, S.get('dsmin_R'), 0.005, 'rel')
    row('Δs_irr/R at CJ_U', 2.92, U.get('dsirr_R'), 0.01, 'rel')
    row('Δs_irr/R at CJ_L', 0.14, L.get('dsirr_R'), 0.005, 'abs')
    row('p_t2/p_t1 at CJ_U', 0.054, U.get('Pt2Pt1'), 0.02, 'rel',
        'supported value replacing deprecated 0.0136')
    row('p_t2/p_t1 at CJ_L', 0.87, L.get('Pt2Pt1'), 0.02, 'rel')
    row('η at M0=5, standing CJ det', 0.345, U.get('eta_M0'), 0.005, 'abs')
    row('η at M0=5, CJ deflagration', 0.818, L.get('eta_M0'), 0.005, 'abs')
    row('η at M0=5, CP (=1-T0/Tt1)', 0.833, P.get('eta_M0'), 0.005, 'abs')
    row('weak-det asymptote M2→ (A41)', 1.61, S.get('M2_asymptote'), 0.01, 'rel')
    row('existence limit q̃t (A42)', 1.042, S.get('q_limit'), 0.005, 'rel')
    section[0] = 'One-γ cycle figures — spec §3.3 [fig ±0.02; low-M/low-q reads ±0.04*]'
    F = og.get('fig_A16', {}); A = og.get('family_A22', {})
    for M, ref, tol in ((2, 0.10, 0.04), (4, 0.21, 0.04), (6, 0.28, 0.04), (10, 0.34, 0.02)):
        row(f'η_FJ(M_CJ={M}), γ=1.2 (A16)', ref, F.get(f'g1.2_M{M}'), tol, 'abs',
            '*' if tol > 0.02 else '')
    for M, ref in ((2, 0.05), (4, 0.11), (6, 0.15), (10, 0.21)):
        row(f'η_FJ(M_CJ={M}), γ=1.1 (A16)', ref, F.get(f'g1.1_M{M}'), 0.02, 'abs')
    for q, r1, r10, r50 in ((10, .09, .35, .52), (20, .17, .41, .55),
                            (30, .22, .44, .57), (40, .26, .46, .58)):
        row(f'η_FJ(π_c=1),  qc/RT1={q} (A22)', r1, A.get(f'eta_pic1_q{q}'), 0.04, 'abs', '*')
        row(f'η_FJ(π_c=10), qc/RT1={q} (A22)', r10, A.get(f'eta_pic10_q{q}'), 0.04, 'abs', '*')
        row(f'η_FJ(π_c=50), qc/RT1={q} (A22)', r50, A.get(f'eta_pic50_q{q}'), 0.04, 'abs', '*')
    row('Brayton η(π_c=10), γ=1.2 (A59)', 1 - 10**(-1 / 6.), eta_brayton_1g(10, 1.2), 1e-9, 'abs')
    section[0] = 'FJ cycle, equilibrium chemistry (300 K, 1 bar, φ=1) — spec §3.3 [fig ±0.015]'
    def fjeta(k): return fj.get(k, {}).get('eta_FJ')
    row('η_FJ H2-air (paper 0.28-0.29)', 0.285, fjeta('H2/air'), 0.02, 'abs')
    row('η_FJ C2H4-air (paper ≈0.30)', 0.30, fjeta('C2H4/air'), 0.02, 'abs')
    row('η_FJ C3H8-air (paper 0.30-0.31)', 0.305, fjeta('C3H8/air'), 0.02, 'abs')
    row('η_FJ H2-O2 (paper ≈0.19, worst)', 0.19, fjeta('H2/O2'), 0.02, 'abs')
    row('η_FJ C2H4-O2 (paper 0.21-0.22)', 0.215, fjeta('C2H4/O2'), 0.02, 'abs')
    row('η_FJ C3H8-O2 (paper 0.22-0.23)', 0.225, fjeta('C3H8/O2'), 0.02, 'abs')
    fa = [fjeta(k) for k in ('H2/air', 'CH4/air', 'C2H4/air', 'C2H2/air',
                             'C3H8/air', 'kerosene/air') if fjeta(k)]
    fo = [fjeta(k) for k in ('H2/O2', 'CH4/O2', 'C2H4/O2', 'C2H2/O2',
                             'C3H8/O2', 'kerosene/O2') if fjeta(k)]
    brow('all fuel-air η_FJ in 0.27-0.32 band', fa and all(.27 <= e <= .32 for e in fa),
         f'range {min(fa):.3f}-{max(fa):.3f}' if fa else 'missing')
    brow('all fuel-O2 η_FJ in 0.18-0.25 band', fo and all(.18 <= e <= .25 for e in fo),
         f'range {min(fo):.3f}-{max(fo):.3f}' if fo else 'missing')
    brow('every fuel-air beats same fuel-O2 (dissociation)',
         all(fjeta(f + '/air') > fjeta(f + '/O2') for f in
             ('H2', 'CH4', 'C2H4', 'C2H2', 'C3H8', 'kerosene')
             if fjeta(f + '/air') and fjeta(f + '/O2')))
    brow('H2-O2 is the worst mixture', fo and fjeta('H2/O2') == min(fo))
    section[0] = '3-cycle π_c sweep, C3H8-air — spec §3.4 [fig ±0.025]'
    def at(pic, key):
        for p in sw:
            if abs(p['pic'] - pic) < 1e-6: return p.get(key)
    row('η_FJ(π_c=1) vs A19/B4 & thesis (0.30-0.31)', 0.305, at(1, 'eta_FJ'), 0.015, 'abs')
    row('η_FJ(π_c=1) vs A26 read (0.28)', 0.28, at(1, 'eta_FJ'), 0.035, 'abs', '†')
    row('η_H(π_c=1)', 0.27, at(1, 'eta_H'), 0.025, 'abs')
    row('η_B(π_c=1) = 0 exactly', 0.0, at(1, 'eta_B'), 1e-6, 'abs')
    row('η_FJ(π_c=5)', 0.45, at(5, 'eta_FJ'), 0.035, 'abs', '†')
    row('η_H(π_c=5)', 0.43, at(5, 'eta_H'), 0.035, 'abs', '†')
    row('η_B(π_c=5)', 0.31, at(5, 'eta_B'), 0.025, 'abs')
    row('η_FJ(π_c=10)', 0.52, at(10, 'eta_FJ'), 0.035, 'abs', '†')
    row('η_H(π_c=10)', 0.50, at(10, 'eta_H'), 0.035, 'abs', '†')
    row('η_B(π_c=10)', 0.40, at(10, 'eta_B'), 0.025, 'abs')
    row('η_FJ(π_c=20)', 0.59, at(20, 'eta_FJ'), 0.025, 'abs')
    row('η_H(π_c=20)', 0.57, at(20, 'eta_H'), 0.025, 'abs')
    row('η_B(π_c=20)', 0.48, at(20, 'eta_B'), 0.025, 'abs')
    brow('ordering FJ ≥ Humphrey > Brayton at every π_c',
         sw and all(p['eta_FJ'] >= p['eta_H'] > p['eta_B'] for p in sw))
    row('P_CJ/P1 at π_c=1 (fig A15: 18.2)', 18.2, at(1, 'pipk_FJ'), 0.03, 'rel')
    row('Humphrey peak p/p1 at π_c=1 (A27 start ≈9-10)', 9.5, at(1, 'pipk_H'), 0.1, 'rel')
    swm = d.get('sweep_CH4_air', {}).get('points', [])
    section[0] = ('3-cycle π_c sweep, CH4-air (lecture display mixture) — '
                  'spec §3.3 fuel-air band + CJ literature anchors')
    def atm(pic, key):
        for p in swm:
            if abs(p['pic'] - pic) < 1e-6: return p.get(key)
    if swm:
        row('η_FJ(π_c=1) in fuel-air band 0.28-0.31', 0.295, atm(1, 'eta_FJ'),
            0.015, 'abs', 'CH4 not in the papers\' fuel set: band check')
        row('η_FJ(π_c=1) sweep vs fj-stage consistency', fjeta('CH4/air') or np.nan,
            atm(1, 'eta_FJ'), 0.003, 'abs', 'same pipeline, independent runs')
        row('U_CJ [m/s] (CJ database, stoich CH4-air ≈1804)', 1804.0,
            atm(1, 'U_CJ'), 0.01, 'rel')
        row('P_CJ/P1 (CJ literature ≈17.2)', 17.2, atm(1, 'pipk_FJ'), 0.025, 'rel')
        row('η_B(π_c=1) = 0 exactly', 0.0, atm(1, 'eta_B'), 1e-6, 'abs')
        row('η_FJ(π_c=20) in fuel-air band ≈0.55-0.60 (A24)', 0.575,
            atm(20, 'eta_FJ'), 0.03, 'abs')
        brow('ordering FJ ≥ Humphrey > Brayton at every π_c (CH4-air)',
             swm and all(p['eta_FJ'] >= p['eta_H'] > p['eta_B'] for p in swm))
        brow('CH4-air η_FJ(π_c=1) between H2-air and C3H8-air (fuel ranking)',
             (fjeta('H2/air') or 0) < (atm(1, 'eta_FJ') or 0) < (fjeta('C3H8/air') or 1))
        vn = d.get('pv_loops_pic5_CH4', {}).get('vN')
        if vn:
            row('vN on the π_c=5 Rayleigh line: residual [%]', 0.0,
                100 * vn['rayleigh_residual'], 1.0, 'abs',
                'PostShock_fr at the cycle U_CJ — fig_cycles_pv ZND structure')
            brow('vN above CJ on the Rayleigh line (p_vN > p_CJ > p_2)',
                 vn['P_bar'] > (atm(5, 'P_CJ_bar') or np.inf) > 5.0,
                 f"p_vN/p_2 = {vn['p_vN_over_p2']:.2f}, "
                 f"p_CJ/p_2 = {(atm(5, 'P_CJ_bar') or np.nan) / 5.0:.2f}")
            row('p_vN/p_CJ (frozen ZND spike over CJ)', 1.8,
                vn.get('p_vN_over_p_CJ',
                       vn['P_bar'] / (atm(5, 'P_CJ_bar') or np.nan)),
                0.2, 'abs', 'expected ≈1.6–2.0 (one-γ strong-shock limit ≈ 2)')
        else:
            brow('vN state stored for fig_cycles_pv', False, 'run plot stage, then validate')
    else:
        brow('CH4-air display sweep computed', False, 'run sweep --mix CH4')
    section[0] = 'Fixed peak-pressure comparison (π\'_c) — spec §3.4 [fig ±0.03]'
    if sw and bx:
        allB = sorted([(p['pipk_B'], p['eta_B']) for p in sw] +
                      [(p['pipk_B'], p['eta_B']) for p in bx])
        xB, yB = zip(*allB)
        xH, yH = zip(*sorted((p['pipk_H'], p['eta_H']) for p in sw))
        xF, yF = zip(*sorted((p['pipk_FJ'], p['eta_FJ']) for p in sw))
        etaB50, etaH50, etaF50 = (float(np.interp(50., x, y)) for x, y in
                                  ((xB, yB), (xH, yH), (xF, yF)))
        row("η_B at π'_c=50", 0.58, etaB50, 0.03, 'abs')
        row("η_H at π'_c=50", 0.53, etaH50, 0.03, 'abs')
        row("η_FJ at π'_c=50", 0.47, etaF50, 0.03, 'abs')
        brow("ranking inversion: B > H > FJ at π'_c = 25, 50, 100",
             all(np.interp(pp, xB, yB) > np.interp(pp, xH, yH) > np.interp(pp, xF, yF)
                 for pp in (25., 50., 100.)))
    else:
        brow("π'_c comparison computed", False, 'run sweep + sweep --brayton-ext')
    section[0] = 'Deprecated claim 0.0136 — provenance'
    O = og.get('deprecated_0136_reproduction', {})
    row('old-deck model reproduced (γ=1.2, q̃=5.24)', 0.0136, O.get('Pt2Pt1'), 0.05, 'rel',
        'identified: one-γ artifact from old validate.py §6, NOT a paper value')
    npass = sum(1 for r in rows if r[6] == 'PASS'); nfail = len(rows) - npass
    lines = ['# V&V — cycles_ws.py vs specs/thermo_spec.md (Wintenberger-Shepherd)', '',
             f'*Generated by `src/cycles/cycles.py validate` on {datetime.date.today()}. '
             f'Model: one-γ analytic (Eqs. A19-A60, B2-B3) + Cantera 3.2 / SD Toolbox '
             f'shifting-equilibrium cycles. Results in `data/cycles_ws.json`.*', '',
             f'**{npass} PASS / {nfail} FAIL of {len(rows)} checks.**', '',
             '[calc] anchors = spec values recomputed from the papers\' own equations '
             '(authoritative); [fig] anchors = spec values read off paper figures '
             '(spec-stated uncertainty ±0.01-0.02 on η).', '']
    cur = None
    for s, name, paper, ours, dev, tol, ok, note in rows:
        if s != cur:
            lines += ['', f'## {s}', '',
                      '| quantity | paper | ours | Δ | tol | verdict | note |',
                      '|---|---|---|---|---|---|---|']
            cur = s
        lines.append(f'| {name} | {paper} | {ours} | {dev} | {tol} | **{ok}** | {note} |')
    vnn = d.get('pv_loops_pic5_CH4', {}).get('vN')
    lines += [
        '', '## Notes', '',
        '1. `*` rows: figure-read anchors at the crowded low-M_CJ / low-q end of paper '
        'Figs. 16/22, where the spec\'s own digitization uncertainty exceeds its nominal '
        '±0.02 (the γ=1.1 curve of the same figure and all four [calc]-grade curves match '
        'within ±0.02). The implementation is the verbatim closed form (B2)+(B3)=(A57); '
        'its internal consistency is proven by the identity η_FJ(A57) ≡ η(A11) evaluated '
        'with the CJ-wave total entropy rise (agrees to 5 decimals in this module).',
        '2. **Deprecated deck claim `p_t2/p_t1 ≈ 0.0136`**: reproduced exactly as the '
        'total-pressure ratio across a *complete* CJ wave in the one-γ model with γ=1.2 '
        'and q/CpT1 = 5.24 (old `scripts/validate.py` §6, mirrored in `figs_more.py`), '
        'i.e. the *products\'* γ applied also to the reactant ram compression — which '
        'overstates the loss ≈5×. It appears in neither assigned paper. Supported values '
        '(γ=1.4): **0.074** at the classical CJ benchmark (q̃=4, M_CJ=4.60) and **0.054** '
        'at the stagnation-Hugoniot CJ benchmark (q̃t=0.8, M_CJ=5.00); the *inert leading '
        'shock alone* at M=5 gives 0.062. Slide wording should say ≈94-95% of total '
        'pressure destroyed, not ~99%.',
        '3. Old `data/eta_fj_fixed.json` (one-γ with frozen γ≈1.24, see '
        '`validation/gamma_audit.md`) is superseded by the `fj_mixtures` section of '
        '`data/cycles_ws.json` (full equilibrium chemistry, both γ values reported '
        'and labelled).',
        '4. Kerosene = n-dodecane surrogate (`data/dodecane_eq_thermo.yaml`, 20-species '
        'equilibrium thermo, U_CJ within +0.19% of full mechanism); the paper\'s heavy '
        'fuel is JP10 (C10H16), so kerosene rows are band checks, not point anchors.',
        '5. `†` rows: paper Fig. A26 (=B5-left) is internally inconsistent with Fig. '
        'A19 (=B4) by 0.02-0.03 at the same point (propane-air, π_c=1: A26 read 0.28 vs '
        'A19 read 0.30-0.31); our pipeline lands on the A19 value (+0.002) and on the '
        'Wintenberger-thesis value (≈0.30), agrees with the one-γ γ=1.2 estimate at '
        'π_c=5 (0.484 vs 0.483), and converges to the A26 reads by π_c=20 (Δ ≤ 0.016). '
        'Tolerance for the mid-π_c A26 reads is therefore declared ±0.035.',
        '6. **Per-phase γ audit (2026-07-08, convergence pass)** — outcome PASS, full '
        'table in `validation/gamma_phase_audit.md`: every Cantera-cycle leg uses the '
        'physically correct properties (compression = frozen *reactant* isentrope; '
        'combustion/detonation = equilibrium jump with heat release, no γ assumption; '
        'expansion = shifting-equilibrium *product* isentrope), and every one-γ figure '
        'declares γ = 1.2 (detonation products, W&S model). Display mixture for '
        '`fig_cycles_pv`/`fig_cycles_eta` is now CH4-air (rows above); the C3H8-air '
        'paper anchors remain the validation basis. Mixture-to-q̃ traceability of the '
        'one-γ family: `data/q_mapping.md`.',
        '7. **fig_cycles_pv ZND annotation fix (2026-07-08; rendering refined '
        '2026-07-09)** — the earlier caption "ZND states lie on this chord" misstated '
        'the process: along the Rayleigh line the states are ordered 2 → CJ → vN in '
        'decreasing v, and the gas never traverses the chord 2 → CJ quasi-statically. '
        'The wave jumps discontinuously 2 → vN (leading shock, frozen composition: '
        '`PostShock_fr` at the cycle U_CJ), then the reaction zone descends the '
        'Rayleigh line vN → CJ as heat is released. Both p–v legs are now sampled '
        'from the same Rayleigh function p(v) = p_2 + (ρ_2 U_CJ)²(v_2 − v), so the '
        'log-scale rendering keeps 2, CJ and vN exactly collinear (a two-point chord '
        'would miss the CJ point on a log axis). '
        + (f"Computed vN (CH4-air, π_c = 5): p_vN = {vnn['P_bar']:.1f} bar "
           f"(p_vN/p_2 = {vnn['p_vN_over_p2']:.2f}, p_vN/p_CJ = "
           f"{vnn.get('p_vN_over_p_CJ', float('nan')):.2f} — within the expected "
           f"1.6–2 frozen-spike window), T_vN = {vnn['T']:.0f} K; collinearity "
           f"residual on the Rayleigh line {100 * vnn['rayleigh_residual']:.3g}% "
           f"(< 1%). Stored in `cycles_ws.json['pv_loops_pic5_CH4']['vN']`."
           if vnn else 'vN values pending: run the plot stage, then validate.'),
    ]
    with open(VAL_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f'[cycles_ws] {npass} PASS / {nfail} FAIL -> {VAL_PATH}')
    for r in rows:
        if r[6] == 'FAIL': print('   FAIL:', r[1], '| paper', r[2], '| ours', r[3])

# ----------------------------------------------------------------------------
# 4. figures (project style; overwrite the six cycle figures + one new)
# ----------------------------------------------------------------------------
def stage_plot():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from style import RED, TEAL, GRAY, LGRAY, GOLD, NAVY, save
    d = load_store()
    g = 1.4

    # -- fig_cycles_pv: p-v diagram of the three cycles, pi_c=5 (recreates
    #    Fig. B2/A25). Display mixture: CH4-air (lecture standard fuel); the
    #    papers' C3H8-air loops remain in cycles_ws.json['pv_loops_pic5'] as
    #    the validation anchor (dual basis declared in figs/figs_manifest.md).
    pv = d['pv_loops_pic5_CH4']; st = pv['states']
    # von Neumann state of the ZND wave: frozen (non-reactive) post-shock state
    # of the compressed reactants (state 2) behind a shock travelling at the
    # cycle's own CJ speed — same U_CJ as the cycle's CJ jump (sweep point
    # pi_c = 5, same run). Mass + momentum put 2, CJ and vN on one Rayleigh
    # line, p = p2 + (U_CJ/v2)^2 (v2 - v), ordered 2 -> CJ -> vN in decreasing
    # v. The gas does NOT traverse the chord 2 -> CJ quasi-statically: it jumps
    # discontinuously 2 -> vN (leading shock, frozen composition), then the
    # reaction zone descends the Rayleigh line vN -> CJ as heat is released.
    from sdtoolbox.postshock import PostShock_fr
    sws = d['sweep_CH4_air']
    p5 = next(p for p in sws['points'] if abs(p['pic'] - 5.0) < 1e-9)
    P2 = pv['pic'] * sws['P1']
    gvn = PostShock_fr(p5['U_CJ'], P2, st['T2'], sws['X'], sws['mech'])
    v_vN, P_vN = 1.0 / gvn.density, gvn.P
    mflx2 = (p5['U_CJ'] / st['v2'])**2                       # (rho2 U_CJ)^2
    ray = lambda v: (P2 + mflx2 * (st['v2'] - v)) * 1e-5     # Rayleigh line [bar]
    res_vN = abs(P_vN * 1e-5 - ray(v_vN)) / (P_vN * 1e-5)
    r_vN_CJ = P_vN * 1e-5 / st['P_CJ_bar']          # frozen-spike / CJ pressure
    assert res_vN < 0.01 and 1.4 < r_vN_CJ < 2.2, \
        (f'vN off the Rayleigh line (residual {res_vN:.2%}) or p_vN/p_CJ = '
         f'{r_vN_CJ:.2f} outside the expected 1.6-2 window for CJ detonations')
    save_section('pv_loops_pic5_CH4', {'vN': {
        'v': v_vN, 'P_bar': P_vN / 1e5, 'T': gvn.T, 'U_CJ': p5['U_CJ'],
        'p_vN_over_p2': P_vN / P2, 'p_vN_over_p_CJ': r_vN_CJ,
        'rayleigh_residual': res_vN,
        'def': 'PostShock_fr(U_CJ, P2, T2, X, mech): frozen post-shock (von Neumann) state'}})
    print(f"  vN state: p_vN = {P_vN/1e5:.1f} bar (p_vN/p2 = {P_vN/P2:.2f}, "
          f"p_vN/p_CJ = {r_vN_CJ:.2f}), v = {v_vN:.4f} m3/kg, T = {gvn.T:.0f} K; "
          f"Rayleigh residual {res_vN:.2e}")
    fig, ax = plt.subplots(figsize=(8.2, 6.4))
    comp = np.array(pv['comp']); fj = np.array(pv['fj_exp'])
    hu = np.array(pv['hu_exp']); br = np.array(pv['br_exp'])
    bar = 1e-5
    ax.plot(comp[:, 0], comp[:, 1] * bar, '-', color=GRAY, lw=1.6)
    # ZND structure on the Rayleigh line: dashed 2 -> vN = leading-shock jump
    # (discontinuous, not quasi-static); solid vN -> CJ = reaction zone. Both
    # legs are SAMPLED from the same Rayleigh function ray(v), not drawn as
    # two-point chords: on the log-p axis a straight chord would miss the CJ
    # point and break the collinearity 2 - CJ - vN that mass + momentum impose.
    v_shk = np.linspace(st['v2'], v_vN, 160)        # full chord 2 -> vN
    ax.plot(v_shk, ray(v_shk), '--', color=RED, lw=1.4, alpha=0.7)
    v_rz = np.linspace(v_vN, st['v_CJ'], 80)        # reaction zone vN -> CJ
    ax.plot(v_rz, ray(v_rz), '-', color=RED, lw=2.0, alpha=0.9, zorder=4)
    ax.plot(v_vN, P_vN * bar, 'o', ms=7, mfc='white', mec=RED, mew=1.6, zorder=6)
    ax.plot(fj[:, 0], fj[:, 1] * bar, '-', color=RED, lw=2.6,
            label='Fickett–Jacobs (detonation)')
    ax.plot([st['v2'], st['v2']], [5.0, st['pipk_H']], '--', color=TEAL, lw=2.2)
    ax.plot(hu[:, 0], hu[:, 1] * bar, '--', color=TEAL, lw=2.2,
            label='Humphrey (const. $v$)')
    ax.plot(br[:, 0], br[:, 1] * bar, ':', color=GRAY, lw=2.4,
            label='Brayton (const. $p$)')
    ax.plot([br[0, 0], st['v2']], [5.0, 5.0], ':', color=GRAY, lw=2.4)
    vmax = max(st['v5_B'], st['v5_H'], st['v5_FJ'])
    ax.plot([st['v6'], vmax], [1.0, 1.0], '-', color=GRAY, lw=1.2, alpha=0.8)
    for v, P, lab, dx, dy in [(st['v1'], 1.0, '1', 8, 8), (st['v2'], 5.0, '2', -14, -2),
                              (st['v_CJ'], st['P_CJ_bar'], '3,4 (CJ)', 12, -16),
                              (st['v5_FJ'], 1.0, '5', 0, 8), (st['v6'], 1.0, '6', -4, 8)]:
        ax.plot(v, P, 'o', color=GRAY, ms=6, zorder=5)
        ax.annotate(lab, (v, P), textcoords='offset points', xytext=(dx, dy), fontsize=13)
    # ZND-structure labels and direction arrows on the Rayleigh line
    via = lambda va, vb, t: va + t * (vb - va)
    vh1 = via(st['v2'], v_vN, 0.30)                # arrowhead on the shock jump
    ax.annotate('', xy=(vh1 - 0.007, ray(vh1 - 0.007)), xytext=(vh1, ray(vh1)),
                arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.2, alpha=0.8))
    vh2 = via(v_vN, st['v_CJ'], 0.62)              # arrowhead on the reaction zone
    ax.annotate('', xy=(vh2 + 0.007, ray(vh2 + 0.007)), xytext=(vh2, ray(vh2)),
                arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.2, alpha=0.9))
    ax.annotate('von Neumann state', (v_vN, P_vN * bar), textcoords='offset points',
                xytext=(10, 6), fontsize=12, color=RED)
    vt = st['v2'] - (19.0 - 5.0) * 1e5 / mflx2      # dashed leg at p = 19 bar
    ax.annotate('leading shock $2 \\to \\mathrm{vN}$:\ndiscontinuous jump (dashed),\nnot a quasi-static path',
                (vt, ray(vt)), xytext=(0.62, 26.0), fontsize=11, color=RED, va='top',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.1,
                                shrinkA=2, shrinkB=3))
    vt2 = st['v2'] - (82.0 - 5.0) * 1e5 / mflx2     # solid leg at p = 82 bar
    ax.annotate('reaction zone (ZND):\nstates descend the Rayleigh line\nfrom vN to the CJ point',
                (vt2, ray(vt2)), xytext=(0.42, 95.0), fontsize=11, color=RED, va='top',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.1,
                                shrinkA=2, shrinkB=3))
    ax.annotate('isentropic\ncompression $\\pi_c=5$', (0.38, 1.9), fontsize=11, color=GRAY)
    ax.set_yscale('log'); ax.set_ylim(0.8, 150); ax.set_xlim(0, 1.12 * vmax)
    ax.set_xlabel('specific volume  $v$  [m$^3$/kg]')
    ax.set_ylabel('pressure  $p$  [bar]')
    ax.legend(loc='upper right', frameon=False,
              title='CH$_4$–air, $\\phi=1$, 300 K, 1 bar')
    save(fig, 'fig_cycles_pv')

    # -- fig_cycles_eta: eta vs pi_c, three cycles, real chemistry (A26/B5-left)
    #    Display mixture CH4-air; C3H8-air paper anchor kept in the JSON/V&V.
    sw = d['sweep_CH4_air']['points']
    pic = [p['pic'] for p in sw]
    fig, ax = plt.subplots(figsize=(8.0, 5.4))
    ax.plot(pic, [p['eta_FJ'] for p in sw], '-', color=RED, lw=2.8,
            label='Fickett–Jacobs (detonation)')
    ax.plot(pic, [p['eta_H'] for p in sw], '--', color=TEAL, lw=2.4,
            label='Humphrey (const. volume)')
    ax.plot(pic, [p['eta_B'] for p in sw], ':', color=GRAY, lw=2.6,
            label='Brayton (const. pressure)')
    ax.set_xlabel('compression ratio  $\\pi_c = p_2/p_1$')
    ax.set_ylabel('thermal efficiency  $\\eta_{th}$')
    ax.set_xlim(1, 20); ax.set_ylim(0, 0.65)
    ax.legend(loc='lower right', frameon=False,
              title='CH$_4$–air, $\\phi=1$, equilibrium chemistry')
    ax.annotate('at fixed $\\pi_c$:  $\\eta_{FJ} \\gtrsim \\eta_{Humphrey} > \\eta_{Brayton}$\n'
                '(at fixed peak pressure the ranking inverts)',
                (0.03, 0.97), xycoords='axes fraction', ha='left', va='top',
                fontsize=12.5, color=RED)
    save(fig, 'fig_cycles_eta')

    # -- fig_cycle_family: one-gamma FJ family vs pi_c (A22), gamma=1.2.
    #    q_c/RT1 labels are traced to real stoichiometric mixtures via
    #    data/q_mapping.json (Cantera values; see data/q_mapping.md).
    fig, ax = plt.subplots(figsize=(8.4, 5.4))
    pics = np.linspace(1, 50, 220)
    curves = {}
    for q, c in zip((10, 20, 30, 40), (NAVY, TEAL, GOLD, RED)):
        qh = q * 0.2 / 1.2
        curves[q] = [eta_fj_1g(qh, 1.2, p) for p in pics]
        ax.plot(pics, curves[q], '-', color=c, lw=2.4, label=f'$q_c/RT_1 = {q}$')
    ax.plot(pics, [eta_brayton_1g(p, 1.2) for p in pics], ':', color=GRAY, lw=2.4,
            label='Brayton (any $q_c$)')
    try:
        with open(os.path.join(DATA, 'q_mapping.json')) as f:
            qr = {r['label']: r['qtilde_R'] for r in json.load(f)['mixtures']}
        txt = ('computed $q_c/RT_1$ of stoichiometric mixtures:\n'
               f"curve 30 $\\approx$ H$_2$–air ({qr['H2/air']:.0f}), "
               f"CH$_4$–air ({qr['CH4/air']:.0f});   "
               f"curve 40 $\\approx$ C$_2$H$_2$–air ({qr['C2H2/air']:.0f})\n"
               f"C$_3$H$_8$–air ({qr['C3H8/air']:.0f}) lies between curves 30 and 40")
        ax.annotate(txt, (0.025, 0.965), xycoords='axes fraction', va='top',
                    fontsize=11.5, color=GRAY)
    except (FileNotFoundError, KeyError):
        pass
    ax.set_xlabel('compression ratio  $\\pi_c$')
    ax.set_ylabel('detonation-cycle efficiency  $\\eta_{th}$')
    ax.set_xlim(1, 50); ax.set_ylim(0, 0.65)
    ax.legend(loc='lower right', frameon=False, ncol=2,
              title='$\\gamma = 1.2$ (detonation products, W&S one-$\\gamma$ model)')
    save(fig, 'fig_cycle_family')

    # -- fig_cj_entropy: entropy along the classical Hugoniot (A5), g=1.4, q=4
    qh = 4.0
    cb = classical_benchmark()
    fig, ax = plt.subplots(figsize=(8.0, 5.8))
    vdet = np.linspace(0.19, 1.0, 500); vfor = np.linspace(1.0, 1 + qh, 300)
    vdef = np.linspace(1 + qh, 15.0, 400)
    for vv, ls, cc, lw in ((vdet, '-', RED, 2.6), (vfor, ':', LGRAY, 2.0),
                           (vdef, '-', GOLD, 2.6)):
        P = hugoniot_pv(vv, qh, g)
        ax.plot(vv, ds_R_pv(P, vv, g), ls, color=cc, lw=lw)
    ax.axvspan(1.0, 1 + qh, color=LGRAY, alpha=0.15, lw=0)
    U, L = cb['CJU'], cb['CJL']
    ax.plot(U['v2v1'], U['ds_R'], 'o', color=RED, ms=9, zorder=5)
    ax.plot(L['v2v1'], L['ds_R'], 'o', color=GOLD, ms=9, zorder=5)
    ax.annotate('CJ detonation:\nbranch minimum\n$\\Delta s/R = %.2f$' % U['ds_R'],
                (U['v2v1'], U['ds_R']), xytext=(1.9, 4.05), fontsize=12, color=RED,
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.2), zorder=6)
    ax.annotate('CJ deflagration:\nbranch maximum\n$\\Delta s/R = %.2f$' % L['ds_R'],
                (L['v2v1'], L['ds_R']), xytext=(10.8, 4.35), fontsize=12, color=GOLD,
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.2))
    ax.axvline(1.0, color=GRAY, lw=0.8, ls=':')
    ax.annotate('initial state', (1.12, 3.92), fontsize=10, color=GRAY, va='bottom')
    ax.annotate('detonation\nbranch', (0.62, 7.25), fontsize=12, color=RED)
    ax.annotate('forbidden\n(no steady wave)', (2.55, 6.55), fontsize=11, color=GRAY)
    ax.annotate('deflagration\nbranch', (11.6, 7.3), fontsize=12, color=GOLD)
    ax.annotate('fixed initial static state:  $\\gamma=1.4$,  $q_c = 4\\,c_pT_1$',
                (0.985, 0.025), xycoords='axes fraction', ha='right', fontsize=11, color=GRAY)
    ax.set_xlabel('specific volume ratio  $v_2/v_1$')
    ax.set_ylabel('entropy rise  $\\Delta s/R$')
    ax.set_xlim(0, 15); ax.set_ylim(3.8, 8.2)
    save(fig, 'fig_cj_entropy')

    # -- fig_entropy_partition: ds_min vs ds_irr, CJ deflagration vs CJ detonation (A7)
    fig, ax = plt.subplots(figsize=(7.4, 5.8))
    labels = ['CJ deflagration\n$M_1 = 0.22$', 'CJ detonation\n$M_1 = M_{CJ} = 4.6$']
    mins = [L['dsmin_R'], U['dsmin_R']]; irrs = [L['dsirr_R'], U['dsirr_R']]
    xs = [0, 1]
    ax.bar(xs, mins, 0.52, color=TEAL, label='$\\Delta s_{min}$ (reversible heat addition)')
    ax.bar(xs, irrs, 0.52, bottom=mins, color=RED,
           label='$\\Delta s_{irr}$ (shock + finite-$M$ heat addition)')
    for x, m, i, pt in zip(xs, mins, irrs, (L['Pt2Pt1'], U['Pt2Pt1'])):
        tot = m + i
        ax.annotate(f'{100*i/tot:.1f}%\nirreversible', (x, tot + 0.16), ha='center',
                    fontsize=12.5, color=RED if i / tot > 0.5 else TEAL)
        ax.annotate(f'$p_{{t2}}/p_{{t1}} = {pt:.3g}$', (x, 0.6), ha='center', fontsize=12,
                    color='white')
    ax.set_xticks(xs); ax.set_xticklabels(labels, fontsize=13)
    ax.set_ylabel('entropy rise  $\\Delta s/R$')
    ax.set_ylim(0, 7.6)
    ax.annotate('classical Hugoniot, fixed static state,  $\\gamma=1.4$,  $q_c=4\\,c_pT_1$',
                (0.5, 0.965), xycoords='axes fraction', ha='center', fontsize=11, color=GRAY)
    ax.legend(loc='upper right', frameon=False, fontsize=11.5, bbox_to_anchor=(1.0, 0.92))
    save(fig, 'fig_entropy_partition')
    # -- fig_tp_loss: total-pressure ratio vs M (shock alone / complete CJ wave)
    fig, ax = plt.subplots(figsize=(7.8, 5.4))
    Ms = np.linspace(1.0, 7.0, 300)
    Mc = np.linspace(0.2, 7.0, 400)
    ax.semilogy(Mc, pt_ratio_cj_wave(Mc, g), '-', color=RED, lw=2.6,
                label='complete CJ wave (shock + heat release)')
    ax.semilogy(Ms, pt_ratio_shock(Ms, g), '--', color=NAVY, lw=2.2,
                label='inert leading shock alone')
    ax.axvspan(0, 1, color=LGRAY, alpha=0.25, lw=0)
    ax.annotate('deflagrations:\n$p_{t2}/p_{t1}\\approx 0.8$–$1$', (0.28, 0.30),
                fontsize=11.5, color=GRAY)
    for M, pt, lab, dx, dy in [(cb['CJU']['M1'], cb['CJU']['Pt2Pt1'],
                                'CJ, $q_c=4\\,c_pT_1$: 0.074', -10, 14),
                               (5.0, pt_ratio_cj_wave(5.0, g),
                                'CJ, $q_c=0.8\\,c_pT_{t1}$ ($M_0$=5): 0.054', -186, -34)]:
        ax.plot(M, pt, 'o', color=GOLD, ms=9, zorder=5, mec=GRAY)
        ax.annotate(lab, (M, pt), textcoords='offset points', xytext=(dx, dy), fontsize=11.5)
    ax.annotate('standing detonation ingests at $M_1 = M_{CJ}\\approx 4.5$–$5$:\n'
                '$\\approx$94–95% of total pressure destroyed\n'
                '(perfect gas, $\\gamma = 1.4$)',
                (0.97, 0.80), xycoords='axes fraction', ha='right', fontsize=12, color=RED)
    ax.set_xlabel('wave Mach number  $M_1$')
    ax.set_ylabel('total-pressure ratio  $p_{t2}/p_{t1}$')
    ax.set_xlim(0, 7); ax.set_ylim(0.01, 1.15)
    ax.legend(loc='lower left', frameon=False, fontsize=12)
    save(fig, 'fig_tp_loss')

    # -- fig_eta_fixed_stag (NEW): eta vs M0, standing vs propagating framing
    em = eta_vs_M0()
    fig, ax = plt.subplots(figsize=(8.2, 5.6))
    M0 = em['M0']
    ax.plot(M0, em['eta_fj_ram'], '-', color=RED, lw=2.8,
            label='propagating CJ det. into fresh charge + ram $\\pi_c$ (FJ; RDE/PDE)')
    ax.plot(M0, em['eta_cp'], ':', color=GRAY, lw=2.6,
            label='const.-$p$ combustion (ideal Brayton bound, A39)')
    ax.plot(M0, em['eta_defl'], '--', color=TEAL, lw=2.2,
            label='standing CJ deflagration (A38)')
    det = np.where(em['eta_det'] > -0.02, em['eta_det'], np.nan)
    ax.plot(M0, det, '-.', color=RED, lw=2.2,
            label='standing CJ detonation (A38)')
    ax.axvspan(0, em['M0_min_det'], color=LGRAY, alpha=0.2, lw=0)
    ax.annotate('no steady CJ-detonation\nsolution:  $q_c/c_pT_{t1} > 1/(\\gamma^2-1)$'
                '\n(existence limit, Eq. A42)', (1.55, 0.065), fontsize=11.5, color=GRAY)
    for y, c in ((0.833, GRAY), (0.818, TEAL), (0.345, RED)):
        ax.plot(5.0, y, 'o', ms=8, color=c, mec=GRAY, zorder=5)
    ax.annotate('0.833 / 0.818', (5.06, 0.755), fontsize=11.5, color=GRAY)
    ax.annotate('0.345', (5.1, 0.30), fontsize=11.5, color=RED)
    ax.annotate('same $q_c$, same flight $M_0$ — only the\nupstream framing differs:  '
                'fixed static\n(propagating) vs fixed stagnation (standing)\n'
                '$\\gamma=1.4$,  $q_c = 4.8\\,c_pT_0$',
                (0.02, 0.97), xycoords='axes fraction', va='top', fontsize=11.5, color=GRAY)
    ax.set_xlabel('flight Mach number  $M_0$')
    ax.set_ylabel('thermal efficiency  $\\eta_{th}$')
    ax.set_xlim(0, 8); ax.set_ylim(0, 1.0)
    ax.legend(loc='upper left', bbox_to_anchor=(-0.02, -0.16), ncol=2,
              frameon=False, fontsize=11)
    save(fig, 'fig_eta_fixed_stag')

# ----------------------------------------------------------------------------
# entry point
if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('stage', choices=['onegamma', 'fj', 'sweep', 'validate', 'plot', 'all'])
    ap.add_argument('--slice', default=None, help='fj: python slice over MIXTURES, e.g. 0:6')
    ap.add_argument('--pics', default=None, help='sweep: comma list of pi_c values')
    ap.add_argument('--brayton-ext', action='store_true',
                    help='sweep: Brayton-only extension pi_c = 30,50,70,100')
    ap.add_argument('--mix', default='C3H8', choices=sorted(SWEEP_MIXES),
                    help='sweep: mixture (C3H8 = paper anchor, CH4 = display)')
    a = ap.parse_args()
    if a.stage in ('onegamma', 'all'): stage_onegamma()
    if a.stage == 'fj': stage_fj(a.slice)
    if a.stage == 'all': stage_fj(None)
    if a.stage == 'sweep': stage_sweep(a.pics, a.brayton_ext, a.mix)
    if a.stage == 'all':
        stage_sweep(None); stage_sweep(None, brayton_ext=True)
        stage_sweep(None, mix='CH4')
    if a.stage in ('validate', 'all'): stage_validate()
    if a.stage in ('plot', 'all'): stage_plot()
