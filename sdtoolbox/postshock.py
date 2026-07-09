"""
SDToolbox 'postshock' module (official, GALCIT FM2018.001, rev. Jan 2021).
CJ detonation speed and post-shock states (frozen and equilibrium).
"""
import cantera as ct
import numpy as np
from sdtoolbox.thermo import eq_state, state


def LSQ_CJspeed(x, y):
    """Least-squares parabola fit to (x,y): a x^2 + b x + c, returns [a,b,c,R2,SSE,SST]."""
    k = 0
    X = X2 = X3 = X4 = 0.0
    Y = Y1 = Y2 = 0.0
    a = b = c = R2 = 0.0
    n = len(x)
    while k < n:
        X += x[k]; X2 += x[k]**2; X3 += x[k]**3; X4 += x[k]**4
        Y += y[k]; Y1 += y[k]*x[k]; Y2 += y[k]*x[k]**2
        k += 1
    m = float(Y)/float(n)
    den = (X3*float(n) - X2*X)
    temp = (den*(X*X2-X3*float(n))+X2*X2*(X*X-float(n)*X2)-X4*float(n)*(X*X-X2*float(n)))
    temp2 = (den*(Y*X2-Y2*float(n)) + (Y1*float(n)-Y*X)*(X4*float(n)-X2*X2))
    b = temp2/temp
    a = 1.0/den*(float(n)*Y1 - Y*X - b*(X2*float(n)-X*X))
    c = 1/float(n)*(Y - a*X2 - b*X)
    k = 0; SSE = 0.0; SST = 0.0
    f = np.zeros(len(x), float)
    while k < len(x):
        f[k] = a*x[k]**2 + b*x[k] + c
        SSE += (y[k] - f[k])**2
        SST += (y[k] - m)**2
        k += 1
    R2 = 1 - SSE/SST
    return [a, b, c, R2, SSE, SST]


def FHFP(w1, gas2, gas1):
    """Momentum & energy conservation error given shock speed and up/downstream states."""
    P1 = gas1.P; H1 = gas1.enthalpy_mass; r1 = gas1.density
    P2 = gas2.P; H2 = gas2.enthalpy_mass; r2 = gas2.density
    w1s = w1**2; w2s = w1s*(r1/r2)**2
    FH = H2 + 0.5*w2s - (H1 + 0.5*w1s)
    FP = P2 + r2*w2s - (P1 + r1*w1s)
    return [FH, FP]


def CJ_calc(gas, gas1, ERRFT, ERRFV, x):
    """CJ wave speed for a prescribed density ratio x via Reynolds' iterative (Newton) method."""
    T = 2000; r1 = gas1.density; V1 = 1/r1
    i = 0; DT = 1000; DW = 1000
    V = V1/x; r = 1/V; w1 = 2000
    [P, H] = eq_state(gas, r, T)
    while (abs(DT) > ERRFT*T or abs(DW) > ERRFV*w1):
        i += 1
        if i == 500:
            return
        [FH, FP] = FHFP(w1, gas, gas1)
        DT = T*0.02; Tper = T + DT
        Vper = V; Rper = 1/Vper; Wper = w1
        [Pper, Hper] = eq_state(gas, Rper, Tper)
        [FHX, FPX] = FHFP(Wper, gas, gas1)
        DFHDT = (FHX-FH)/DT; DFPDT = (FPX-FP)/DT
        DW = 0.02*w1; Wper = w1 + DW
        Tper = T; Rper = 1/V
        [Pper, Hper] = eq_state(gas, Rper, Tper)
        [FHX, FPX] = FHFP(Wper, gas, gas1)
        DFHDW = (FHX-FH)/DW; DFPDW = (FPX-FP)/DW
        J = DFHDT*DFPDW - DFPDT*DFHDW
        b = [DFPDW, -DFHDW, -DFPDT, DFHDT]
        a = [-FH, -FP]
        DT = (b[0]*a[0]+b[1]*a[1])/J; DW = (b[2]*a[0]+b[3]*a[1])/J
        DTM = 0.2*T
        if abs(DT) > DTM:
            DT = DTM*DT/abs(DT)
        T = T + DT; w1 = w1 + DW
        [P, H] = eq_state(gas, r, T)
    return [gas, w1]


def CJspeed(P1, T1, q, mech, fullOutput=False):
    """CJ detonation speed (m/s). Minimises wave speed over the equilibrium Hugoniot
    via a density-ratio sweep + least-squares parabola (official SDToolbox algorithm)."""
    numsteps = 20; maxv = 2.0; minv = 1.5
    w1 = np.zeros(numsteps+1, float)
    rr = np.zeros(numsteps+1, float)
    gas1 = ct.Solution(mech); gas = ct.Solution(mech)
    gas.TPX = T1, P1, q; gas1.TPX = T1, P1, q
    ERRFT = 1.0e-4; ERRFV = 1.0e-4
    T1 = gas1.T; P1 = gas1.P
    counter = 1; R2 = 0.0; cj_speed = 0.0
    a = b = c = dnew = 0.0
    while (counter <= 4) or (R2 < 0.99999):
        step = (maxv-minv)/float(numsteps); i = 0; x = minv
        while x <= maxv:
            gas.TPX = T1, P1, q
            [gas, temp] = CJ_calc(gas, gas1, ERRFT, ERRFV, x)
            w1[i] = temp; rr[i] = gas.density/gas1.density
            i += 1; x = x + step
        [a, b, c, R2, SSE, SST] = LSQ_CJspeed(rr, w1)
        dnew = -b/(2.0*a)
        minv = dnew - dnew*0.001; maxv = dnew + dnew*0.001
        counter += 1
        cj_speed = a*dnew**2 + b*dnew + c
    if fullOutput:
        return [cj_speed, R2, (rr, w1, dnew, a, b, c)]
    return cj_speed


def PostShock_fr(U1, P1, T1, q, mech):
    """Frozen post-shock (von Neumann) state at shock speed U1."""
    from sdtoolbox.config import ERRFT, ERRFV
    gas1 = ct.Solution(mech); gas = ct.Solution(mech)
    gas.TPX = T1, P1, q; gas1.TPX = T1, P1, q
    gas = shk_calc(U1, gas, gas1, ERRFT, ERRFV)
    return gas


def PostShock_eq(U1, P1, T1, q, mech):
    """Equilibrium post-shock state at shock speed U1."""
    from sdtoolbox.config import ERRFT, ERRFV
    gas1 = ct.Solution(mech); gas = ct.Solution(mech)
    if len(q) > 1:
        gas.TPX = T1, P1, q; gas1.TPX = T1, P1, q
    else:
        gas.TP = T1, P1; gas1.TP = T1, P1
    gas = shk_eq_calc(U1, gas, gas1, ERRFT, ERRFV)
    return gas


def shk_calc(U1, gas, gas1, ERRFT, ERRFV):
    """Frozen post-shock state (Reynolds' iterative method)."""
    from sdtoolbox.config import volumeBoundRatio
    r1 = gas1.density; V1 = 1/r1
    P1 = gas1.P; T1 = gas1.T
    i = 0; deltaT = 1000; deltaV = 1000
    Vg = V1/volumeBoundRatio; rg = 1/Vg
    Pg = P1 + r1*(U1**2)*(1-Vg/V1); Tg = T1*Pg*Vg/(P1*V1)
    [Pg, Hg] = state(gas, rg, Tg)
    V = Vg; r = rg; P = Pg; T = Tg; H = Hg
    while (abs(deltaT) > ERRFT*T or abs(deltaV) > ERRFV*V):
        i += 1
        if i == 500:
            print('shk_calc did not converge for U = ', U1); return gas
        [FH, FP] = FHFP(U1, gas, gas1)
        DT = T*0.02; Tper = T + DT; Vper = V; Rper = 1/Vper
        [Pper, Hper] = state(gas, Rper, Tper)
        [FHX, FPX] = FHFP(U1, gas, gas1)
        DFHDT = (FHX-FH)/DT; DFPDT = (FPX-FP)/DT
        DV = 0.02*V; Vper = V + DV; Tper = T; Rper = 1/Vper
        [Pper, Hper] = state(gas, Rper, Tper)
        [FHX, FPX] = FHFP(U1, gas, gas1)
        DFHDV = (FHX-FH)/DV; DFPDV = (FPX-FP)/DV
        J = DFHDT*DFPDV - DFPDT*DFHDV
        b = [DFPDV, -DFHDV, -DFPDT, DFHDT]; a = [-FH, -FP]
        deltaT = (b[0]*a[0]+b[1]*a[1])/J; deltaV = (b[2]*a[0]+b[3]*a[1])/J
        DTM = 0.2*T
        if abs(deltaT) > DTM:
            deltaT = DTM*deltaT/abs(deltaT)
        V2X = V + deltaV
        DVM = 0.5*(V1 - V) if V2X > V1 else 0.2*V
        if abs(deltaV) > DVM:
            deltaV = DVM*deltaV/abs(deltaV)
        T = T + deltaT; V = V + deltaV; r = 1/V
        [P, H] = state(gas, r, T)
    return gas


def shk_eq_calc(U1, gas, gas1, ERRFT, ERRFV):
    """Equilibrium post-shock state (Reynolds' iterative method)."""
    from sdtoolbox.config import volumeBoundRatio
    r1 = gas1.density; V1 = 1/r1
    P1 = gas1.P; T1 = gas1.T
    i = 0; deltaT = 1000; deltaV = 1000
    V = V1/volumeBoundRatio; r = 1/V
    P = P1 + r1*(U1**2)*(1-V/V1); T = T1*P*V/(P1*V1)
    [P, H] = eq_state(gas, r, T)
    while (abs(deltaT) > ERRFT*T or abs(deltaV) > ERRFV*V):
        i += 1
        if i == 500:
            print('shk_eq_calc did not converge for U = ', U1); return gas
        [FH, FP] = FHFP(U1, gas, gas1)
        DT = T*0.02; Tper = T + DT; Vper = V; Rper = 1/Vper
        [Pper, Hper] = eq_state(gas, Rper, Tper)
        [FHX, FPX] = FHFP(U1, gas, gas1)
        DFHDT = (FHX-FH)/DT; DFPDT = (FPX-FP)/DT
        DV = 0.02*V; Vper = V + DV; Tper = T; Rper = 1/Vper
        [Pper, Hper] = eq_state(gas, Rper, Tper)
        [FHX, FPX] = FHFP(U1, gas, gas1)
        DFHDV = (FHX-FH)/DV; DFPDV = (FPX-FP)/DV
        J = DFHDT*DFPDV - DFPDT*DFHDV
        b = [DFPDV, -DFHDV, -DFPDT, DFHDT]; a = [-FH, -FP]
        deltaT = (b[0]*a[0]+b[1]*a[1])/J; deltaV = (b[2]*a[0]+b[3]*a[1])/J
        DTM = 0.2*T
        if abs(deltaT) > DTM:
            deltaT = DTM*deltaT/abs(deltaT)
        V2X = V + deltaV
        DVM = 0.5*(V1 - V) if V2X > V1 else 0.2*V
        if abs(deltaV) > DVM:
            deltaV = DVM*deltaV/abs(deltaV)
        T = T + deltaT; V = V + deltaV; r = 1/V
        [P, H] = eq_state(gas, r, T)
    return gas
