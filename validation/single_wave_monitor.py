#!/usr/bin/env python3
"""THE SINGLE-WAVE MONITOR of the data contract [X-SWAV] (F2.ENGINE order 4(d), 2026-09-30; gates declared in
validation/PROGRESS_2026-09-30_F2ENGINE.md before this file was written).

The design (12 frozen phases) and the judge (the flow in the frame that turns with the wave) both assume the RDE
outflow is ONE wave turning rigidly and repeating itself. This monitor reads pressure histories at probes spread
around the annulus and answers: how many waves (W-1); does the pattern turn rigidly -- the signal at one probe is
the signal at another delayed by their angle over the wave speed (W-2); does the pattern repeat turn after turn
(W-3). It measures on the quantity the design consumes -- the 12 sector means of the pattern -- not on the raw
samples: the detonation peak is a spike a few samples wide, and any measure on the samples is a measure of where
the spike falls (the first form of this gate, RMS of the samples against the RMS the sectors discard, could not
see a 30 percent counter-turning wave: replaced the same evening, F2ENGINE log). Two lines, both derived: the
SHIFT of the sector means' average (what moves the cycle-averaged thrust, which follows the phases' pressure)
must stay below PILOT-WF's line, one third of the thrust-stand band (0.17 percent); the REDISTRIBUTION among
sectors (RMS of the sector-mean differences) must stay below the typical (median) step between adjacent sector
means of the record itself (below it the 12-sector description does not tell the two patterns apart; the smallest
step is not used: two sectors can be equal by chance, 0.0008 on the wall probes).

Data of record: _single_wave/thor_cav3_probes_last3ms.npz = the Q2D THOR_CAv3 chamber probes (wall1..5 at
x 18.8 mm, piastra1..5 at x 23.4 mm, 72 degrees apart), the last 3 ms of the run that gave the 12 phases.
Rejectors R-1..R-3 are seeded on the same record and must fire.
usage: .venv-a1/bin/python validation/single_wave_monitor.py [--data <npz>] [--group piastra|wall]"""
import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "_single_wave", "thor_cav3_probes_last3ms.npz")
N_SECTORS = 12
SHIFT_LINE = 0.0017                                              # one third of the thrust-stand band (PILOT-WF's line)
OK = True


def check(name, cond, detail=""):
    global OK
    OK &= bool(cond)
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, (" -- " + detail) if detail else ""))
    return bool(cond)


def resample(t, sig, dt):
    tu = np.arange(t[0], t[-1], dt)
    return tu, np.interp(tu, t, sig)


def period_of(sig, dt, tmin, tmax):
    """The fundamental period from the autocorrelation's first peak inside [tmin, tmax]."""
    x = sig - sig.mean()
    nfft = 1 << int(np.ceil(np.log2(2 * len(x))))
    X = np.fft.rfft(x, nfft)
    ac = np.fft.irfft(X * np.conj(X), nfft)[:len(x)]
    ac /= ac[0]
    lo, hi = int(tmin / dt), int(tmax / dt)
    k = lo + int(np.argmax(ac[lo:hi]))
    # parabolic refinement
    if 0 < k < len(ac) - 1:
        d = 0.5 * (ac[k - 1] - ac[k + 1]) / (ac[k - 1] - 2 * ac[k] + ac[k + 1])
        return (k + d) * dt
    return k * dt


def delay_of(a, b, dt, T):
    """The delay of b behind a (b(t) = a(t - tau)) from the circular cross-correlation over one period, in [0, T)."""
    n = int(round(T / dt))
    m = (len(a) // n) * n
    xa = (a[:m] - a[:m].mean()).reshape(-1, n).mean(0)
    xb = (b[:m] - b[:m].mean()).reshape(-1, n).mean(0)
    cc = np.array([np.dot(xa, np.roll(xb, -k)) for k in range(n)])
    k = int(np.argmax(cc))
    d = 0.0
    km, kp = (k - 1) % n, (k + 1) % n
    den = cc[km] - 2 * cc[k] + cc[kp]
    if den < 0:
        d = 0.5 * (cc[km] - cc[kp]) / den
    return ((k + d) % n) * dt


def wave_count(delays_deg, T, dth_deg):
    """delays: {angle: tau}. n such that tau = n * angle/360 * T (mod T) for both angles; None if none fits n <= 4."""
    best = None
    for n in range(1, 5):
        err = 0.0
        for ang, tau in delays_deg.items():
            pred = (n * ang / 360.0 * T) % T
            e = abs(tau - pred) % T
            err = max(err, min(e, T - e) / T)
        if best is None or err < best[1]:
            best = (n, err)
    return best


def fold(sig, t, T, phase0=0.0):
    """The signal folded onto the wave frame: phase in [0, 1), value."""
    ph = ((t - t[0]) / T + phase0) % 1.0
    return ph, sig


def sector_means(ph, sig):
    """The 12 sector means of the pattern (phase in [0, 1))."""
    edges = np.linspace(0, 1, N_SECTORS + 1)
    idx = np.clip(np.searchsorted(edges, ph, side="right") - 1, 0, N_SECTORS - 1)
    return np.array([sig[idx == k].mean() for k in range(N_SECTORS)])


def run(t, sigs, thetas, label, verbose=True):
    """The three gates on a set of probe histories. Returns (n_waves, rigid residual, limit, repeat residual)."""
    dt = float(np.median(np.diff(t))) * 0.5
    tu = None
    S = []
    for s in sigs:
        tu, su = resample(t, s, dt)
        S.append(su)
    S = np.array(S)
    # W-1: the period of every probe, in each half of the window
    per = np.array([period_of(s, dt, 50e-6, 1000e-6) for s in S])
    half = S.shape[1] // 2
    perA = np.array([period_of(s[:half], dt, 50e-6, 1000e-6) for s in S])
    perB = np.array([period_of(s[half:], dt, 50e-6, 1000e-6) for s in S])
    T = float(np.median(per))
    spread = float((per.max() - per.min()) / T)
    delays = {}
    for i in range(len(S)):
        for j in range(len(S)):
            if i == j:
                continue
            ang = (thetas[i] - thetas[j]) % 360.0                # probe j sees the pattern later by ang/360 T if it turns toward decreasing theta
            if abs(ang - 72.0) < 1.0 or abs(ang - 144.0) < 1.0:
                delays.setdefault(round(ang), []).append(delay_of(S[i], S[j], dt, T))
    dl = {a: float(np.median(v)) for a, v in delays.items()}
    n, err = wave_count(dl, T, 72.0)
    nA, errA = wave_count({a: float(np.median([delay_of(S[i][:half], S[j][:half], dt, float(np.median(perA))) for i in range(len(S)) for j in range(len(S))
                                                 if i != j and abs(((thetas[i] - thetas[j]) % 360.0) - a) < 1.0])) for a in dl}, float(np.median(perA)), 72.0)
    nB, errB = wave_count({a: float(np.median([delay_of(S[i][half:], S[j][half:], dt, float(np.median(perB))) for i in range(len(S)) for j in range(len(S))
                                                 if i != j and abs(((thetas[i] - thetas[j]) % 360.0) - a) < 1.0])) for a in dl}, float(np.median(perB)), 72.0)
    if verbose:
        print("  %s: period %.2f us (%.0f Hz), spread over probes %.2e; delays %s us; wave count %d (fit error %.3f of T), "
              "halves %d / %d" % (label, T * 1e6, 1.0 / T, spread, {a: round(v * 1e6, 1) for a, v in dl.items()}, n, err, nA, nB))
    w1 = check("W-1 %s: one wave, the same in both halves of the window (period spread %.1e <= 1e-2, delays fit n = 1 within 5 percent of T)"
               % (label, spread), spread <= 1e-2 and n == 1 and nA == 1 and nB == 1 and err <= 0.05)
    # the 12 sector means of every probe, folded onto the wave frame with the delay of its angle (probe 0 = the reference)
    pm = float(S[0].mean())
    means = []
    for i in range(len(S)):
        tau = ((thetas[0] - thetas[i]) % 360.0) / 360.0 * T
        ph = ((tu - tu[0] - tau) / T) % 1.0
        means.append(sector_means(ph, S[i]) / pm)
    means = np.array(means)
    steps = np.abs(np.diff(np.concatenate([means[0], means[0][:1]])))
    lim = float(np.median(steps))                                     # the typical step between adjacent sectors (the smallest can be a chance near-equality: 0.0008 on the wall probes)
    # W-2: rigid turning -- the sector means of every probe against the reference's
    d = means[1:] - means[0]
    shift = float(np.abs(d.mean(1)).max())
    rig = float(np.sqrt((d ** 2).mean(1)).max())
    w2 = check("W-2 %s: rigid turning -- sector means probe by probe: shift of the average %.4f <= %.4f, redistribution (RMS) %.4f <= %.4f (the median sector step)"
               % (label, shift, SHIFT_LINE, rig, lim), shift <= SHIFT_LINE and rig <= lim)
    # W-3: repeats -- the sector means turn after turn (reference probe), consecutive turns and first against last
    nT = int(round(T / dt))
    m = (len(S[0]) // nT) * nT
    turns = S[0][:m].reshape(-1, nT)
    ph1 = np.arange(nT) / nT
    tm = np.array([sector_means(ph1, tr) / pm for tr in turns])
    dd = np.vstack([np.diff(tm, axis=0), (tm[-1] - tm[0])[None, :]])
    shift3 = float(np.abs(dd.mean(1)).max())
    rep = float(np.sqrt((dd ** 2).mean(1)).max())
    w3 = check("W-3 %s: repeats -- sector means turn after turn (%d turns): shift %.4f <= %.4f, redistribution %.4f <= %.4f"
               % (label, len(tm), shift3, SHIFT_LINE, rep, lim), shift3 <= SHIFT_LINE and rep <= lim)
    if verbose:
        print("    sector means / mean pressure (reference probe): %s" % np.array2string(means[0], precision=3))
    return n, rig, lim, rep, T, (w1, w2, w3)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=DATA)
    ap.add_argument("--group", default="piastra", choices=("piastra", "wall"))
    a = ap.parse_args()
    d = np.load(a.data)
    names = [str(n) for n in d["names"]]
    sel = [i for i, n in enumerate(names) if n.startswith(a.group)]
    t = d["t"]
    sigs = [d[names[i]] for i in sel]
    th = np.array([d["theta_deg"][i] for i in sel])
    print("== [F2.ENGINE] the single-wave monitor [X-SWAV] on %s (%d probes at %s deg, %.2f ms, %d samples) ==" % (a.group, len(sel), np.round(th, 1), (t[-1] - t[0]) * 1e3, len(t)))
    n, rig, lim, rep, T, _ = run(t, sigs, th, "record")
    # ---- rejectors, seeded on the record
    print("-- rejectors (seeded, must fire) --")
    dt = float(np.median(np.diff(t)))
    # R-1: a second wave turning the OTHER way, 30 percent of the pattern: built by folding the record's own pattern
    tu, ref = resample(t, sigs[0], dt)
    ph = ((tu - tu[0]) / T) % 1.0
    order = np.argsort(ph)
    pat_ph, pat = ph[order], ref[order] - ref.mean()
    def pattern_at(phase):
        return np.interp(phase % 1.0, pat_ph, pat, period=1.0)
    sig2 = []
    for s, thi in zip(sigs, th):
        tu_i, si = resample(t, s, dt)
        # the counter-turning copy: phase advances with +theta instead of -theta
        sig2.append(si + 0.3 * pattern_at((tu_i - tu_i[0]) / T + 2 * thi / 360.0))
    _, rig2, lim2, _, _, (a1, a2, a3) = run(tu, sig2, th, "R-1 counter-wave", verbose=False)
    check("R-1 a counter-turning wave at 30 percent FIRES W-2 (redistribution %.4f against the line %.4f; the record alone %.4f)" % (rig2, lim2, rig), not a2)
    # R-2: the wave count doubled in the second half: the second half of every probe replaced by the pattern at 2x
    sig3 = []
    for s, thi in zip(sigs, th):
        tu_i, si = resample(t, s, dt)
        half = len(si) // 2
        s2 = si.copy()
        s2[half:] = si.mean() + pattern_at(2.0 * ((tu_i[half:] - tu_i[0]) / T - thi / 360.0))
        sig3.append(s2)
    _, _, _, _, _, (b1, b2, b3) = run(tu, sig3, th, "R-2 count doubled in the second half", verbose=False)
    check("R-2 the wave count changing inside the window FIRES W-1", not b1)
    # R-3: a slow drift of the mean, 10 percent over the window
    sig4 = []
    for s in sigs:
        tu_i, si = resample(t, s, dt)
        sig4.append(si * (1.0 + 0.10 * (tu_i - tu_i[0]) / (tu_i[-1] - tu_i[0])))
    _, _, _, rep4, _, (c1, c2, c3) = run(tu, sig4, th, "R-3 drifting mean", verbose=False)
    check("R-3 a 10 percent drift of the mean over the window FIRES W-3", not c3)
    print("VERDICT: %s" % ("PASS" if OK else "FAIL"))
    sys.exit(0 if OK else 1)


if __name__ == "__main__":
    main()
