"""GENO file exchange for the revalidation (2026-10-07): synthetic constant-gamma thermo written CONSISTENTLY
(p(T0) = P0 exactly, so GENO's dimensional pressures are physical), input decks, and readers of the outputs.
GENO itself (bin/GENO of /data10/falco/RDE/codes/GENO, branch exp/ws-c-prod-nozzles 28c7e7a = origin) is run on
s3 by run_geno.sh; it is never modified.

GENO thermo conventions (read from a1_ideal_march_jax.parse_plt/parse_nasa and the GENO CASES files):
  NASA-7 file: name, 'G', molar mass [g/mol], Tlow, Thigh, Tbreak; 3 rows of 5 E15.8 coefficients
  (upper a1..a5 | upper a6 a7, lower a1..a3 | lower a4..a7). Constant cp: a1 = gamma/(gamma-1), the rest 0, so
  h(T) = cp T and s(T) = cp ln T (mass units, R = Runi/M, Runi = 8.31451).
  plt: header, then rows 'gamma h[kJ/kg] s[kJ/kg/K] T[K] p[bar] x_1': the chamber row fixes h0, s0, T0, p0;
  GENO's pressure is p = 1e5 exp((s(T) - s0)/R), so s0 = cp ln T0 - R ln(P0/1e5) makes p(T0) = P0.
"""
import os
import struct

import numpy as np

RUNI_GENO = 8.31451


def write_thermo(d, tag, gamma, R, T0, P0):
    # the file's own precision defines GENO's gas: round M (F9.5) and a1 (E15.8) first, then derive the
    # effective (gamma, R) GENO will see and make the chamber row consistent with THEM (p(T0) = P0 exactly)
    M = float("%.5f" % (1000.0 * RUNI_GENO / R))     # g/mol, as printed
    a1 = float("%.8E" % (gamma / (gamma - 1.0)))      # as printed
    R = 1000.0 * RUNI_GENO / M
    gamma = a1 / (a1 - 1.0)
    cp = a1 * R
    f = lambda v: ("%15.8E" % v).replace("E", "E")    # noqa: E731
    with open(os.path.join(d, "thermo_%s.dat" % tag), "w") as fh:
        fh.write("Synthetic_1sp    G%9.5f                               10.000  5000.000 1000.    1\n" % M)
        fh.write(f(a1) + f(0.0) + f(0.0) + f(0.0) + f(0.0) + "    2\n")
        fh.write(f(0.0) + f(0.0) + f(a1) + f(0.0) + f(0.0) + "    3\n")
        fh.write(f(0.0) + f(0.0) + f(0.0) + f(0.0) + "                   4\n")
    h0 = cp * T0 / 1000.0
    s0 = (cp * np.log(T0) - R * np.log(P0 / 1.0e5)) / 1000.0
    row = "   %.15E  %.15E  %.15E  %.15E  %.15E  1.0000E+00\n" % (gamma, h0, s0, T0, P0 / 1.0e5)
    with open(os.path.join(d, "%s.plt" % tag), "w") as fh:
        fh.write("#  gammafz     h           s           t           p           Synthetic_1sp\n")
        fh.write(row + row + row)
        fh.write("#  gammafz     h           s           t           p           Synthetic_1sp\n")
    return dict(M=M, cp=cp, h0=h0, s0=s0, gamma=gamma, R=R)


def write_input(d, sections):
    with open(os.path.join(d, "input.ini"), "w") as fh:
        for sec, kv in sections.items():
            fh.write("[%s]\n" % sec)
            for k, v in kv.items():
                fh.write("%s = %s\n" % (k, v))
            fh.write("\n")


def read_kv(path):
    out = {}
    for ln in open(path):
        if "=" in ln:
            k, v = ln.split("=", 1)
            try:
                out[k.strip()] = float(v.split()[0])
            except (ValueError, IndexError):
                out[k.strip()] = v.strip()
    return out


def read_field(d, name, n_cols):
    """GENO writeoutput binary: j2 rows of l float64 (stream), l = n_cols (the run's printed i)."""
    raw = open(os.path.join(d, name), "rb").read()
    n = len(raw) // 8
    if n % n_cols:
        raise ValueError("%s: %d values not a multiple of %d columns" % (name, n, n_cols))
    return np.frombuffer(raw, dtype="<f8").reshape(n // n_cols, n_cols)


def migdal_dims(log_path):
    """(i_cm, i_cp) of the profile phase and (j2_cm, j2_cp) of the kernel, from GENO's stdout."""
    i_cm = i_cp = j2_cm = j2_cp = None
    for ln in open(log_path):
        if "Migdal kernel complete" in ln:
            t = ln.replace("=", " ").split()
            j2_cm, j2_cp = int(t[t.index("j2_cm") + 1]), int(t[t.index("j2_cp") + 1])
        if "Migdal profile complete" in ln:
            t = ln.replace("=", " ").split()
            i_cm, i_cp = int(t[t.index("i_cm") + 1]), int(t[t.index("i_cp") + 1])
    return i_cm, i_cp, j2_cm, j2_cp


def read_row(d, name, n_cols, row=0):
    """One row (default: row 1 = the wall) of a GENO writeoutput binary without loading the field."""
    with open(os.path.join(d, name), "rb") as fh:
        fh.seek(8 * n_cols * row)
        return np.fromfile(fh, dtype="<f8", count=n_cols)


def migdal_walls(d):
    """GENO type-9 run -> dict(cm=(x, y, p), cp=(x, y, p)) on row 1 (the walls), zero padding removed, plus the
    performance numbers. Row 1 of sol_cm / sol_cp is the wall (main.f90 run_migdal writes profile_*.dat from
    sol%x(1, :), sol%y(1, :) with the same zero test)."""
    i_cm, i_cp, _, _ = migdal_dims(os.path.join(d, "run.log"))
    out = dict(perf=read_kv(os.path.join(d, "performance.dat")))
    for k, n in (("cm", i_cm), ("cp", i_cp)):
        X, Y, P = (read_row(d, "%s_%s.dat" % (v, k), n) for v in ("x", "y", "p"))
        ok = (X != 0.0) | (Y != 0.0)
        out[k] = (X[ok], Y[ok], P[ok])
    return out
