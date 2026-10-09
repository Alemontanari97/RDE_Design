"""Common harness of the revalidation tests (2026-10-07).

Every test script: imports the MODEL as a black box (validation/a1_*.py), compares it with an independent
reference (ref/exact.py, GENO outputs), prints one line per check, writes out/<test>.json and figs/NN_*.png, and
exits 1 if any check fails. Tolerances are derived in each script from a stated error model (written next to the
check), never tuned to the result.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RV = os.path.dirname(HERE)                       # _revalidation_2026-10-07
VAL = os.path.dirname(RV)                        # RDE_Design/validation
sys.path.insert(0, VAL)
sys.path.insert(0, HERE)
OUT, FIGS, LOGS = (os.path.join(RV, d) for d in ("out", "figs", "logs"))
SDT = os.path.join(VAL, "_cycle_family", "sdt_ch4_phi1_pcp20")

import numpy as np                                # noqa: E402


class Report:
    def __init__(self, name):
        self.name, self.rows, self.t0 = name, [], time.time()
        print("=" * 100, flush=True)
        print("TEST %s   (%s)" % (name, time.strftime("%Y-%m-%d %H:%M:%S")), flush=True)

    def check(self, label, value, tol, ok=None, unit=""):
        """PASS iff |value| <= tol (or ok when given). value/tol are printed as measured."""
        if ok is None:
            ok = bool(np.isfinite(value) and abs(value) <= tol)
        self.rows.append(dict(label=label, value=float(value) if np.isscalar(value) else value,
                              tol=float(tol) if tol is not None else None, ok=bool(ok), unit=unit))
        print("  [%s] %-70s value %-12s tol %-12s %s" % ("PASS" if ok else "FAIL", label,
              "%.3e" % value if np.isscalar(value) else str(value), "%.3e" % tol if tol is not None else "-",
              unit), flush=True)
        return ok

    def reject(self, label, value, tol, unit=""):
        """REJECTOR (repo rule R5: a test must be able to reject). The check named in `label` is applied, with its own
        tolerance `tol`, to a deliberately corrupted model; the row PASSES iff the corruption is CAUGHT: |value| > tol
        with a FINITE value (a non-finite value is not a detection: the uncorrupted check may be non-finite too)."""
        caught = bool(np.isfinite(value) and abs(value) > tol)
        self.rows.append(dict(label="rejector: " + label, value=float(value), tol=float(tol), ok=caught, unit=unit,
                              rejector=True))
        print("  [%s] %-70s value %-12s tol %-12s %s" % ("PASS" if caught else "FAIL", "rejector: " + label,
              "%.3e" % value, "%.3e" % tol, "(caught)" if caught else "(NOT caught)"), flush=True)
        return caught

    def note(self, msg):
        print("  " + msg, flush=True)

    def save(self, extra=None):
        n_ok = sum(r["ok"] for r in self.rows)
        res = dict(test=self.name, n_pass=n_ok, n=len(self.rows), rows=self.rows,
                   seconds=time.time() - self.t0, extra=extra or {})
        with open(os.path.join(OUT, self.name + ".json"), "w") as f:
            json.dump(res, f, indent=1, default=float)
        print("RESULT %s: %d / %d checks pass  (%.1f s)" % (self.name, n_ok, len(self.rows), time.time() - self.t0),
              flush=True)
        return 0 if n_ok == len(self.rows) else 1


def sdt_gas():
    return json.load(open(os.path.join(SDT, "gas_mean.json")))


def sdt_phases():
    return json.load(open(os.path.join(SDT, "family_K12.json")))


def model_table(gamma, R, T0, P0, T_tab):
    """The model's own constant-gamma table, built exactly as the two-wall carrier builds it
    (a1_twowall.TwoWall.__init__: A1.prep_tab(tab_gconst(gam, R, T0, P0, T_tab)))."""
    import a1_ideal_march_jax as A1
    import a1_twowall as T
    tab = A1.prep_tab(T.tab_gconst(gamma, R, T0, P0, T_tab))
    return tab, A1.tab_arrays(tab)


def savefig(fig, name):
    path = os.path.join(FIGS, name)
    fig.savefig(path, dpi=130, bbox_inches="tight")
    print("  figure: %s" % path, flush=True)
    return path
