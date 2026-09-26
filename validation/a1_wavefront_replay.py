#!/usr/bin/env python3
"""THE WAVEFRONT REPLAY of the plug march (S41 2026-09-26, [F3/A1]): the
frozen schedule of a recorded march re-executed by ANTI-DIAGONAL BATCHES.

WHY. The march's replay (the objective and the class margin under jax.grad)
runs cell by cell in eager mode: ~9000 cells at (140,31), ~35000 at (280,61),
each a dispatch of the implicit cell solve plus its bookkeeping, forward and
backward -- measured 30-40 s per gradient at the coarse rung and 155 s at the
fine one, 96 XLA threads idle on 4 x 4 systems. The march is a wavefront: a
cell at (row j, column i) depends on the cell below it in its column and on
the previous column, so the cells of one anti-diagonal are independent. The
record (plug_march(graph=...)) writes the march's dataflow -- kind, output
key, input keys, static indices, schedule index of every cell, the wedge
aliases, the ordered wall and shroud outputs, the margin quads' corners --
and this module schedules it by LEVELS (the longest dependency path) and
solves every level's cells of one kind in ONE vmapped call of the same
implicit solver on the same recorded seeds: ~250 levels x 4 kinds instead
of ~9000 calls. The primal is the same Newton per lane (a batched
while_loop freezes the lanes that have converged), the parameters are built
from the same numbers, the margin aggregates the same corners in the same
order through the march's own margin_of_corners: the equality with the
sequential replay is GRADED by a1_twowall stage wavefront (WF-1..WF-3), not
assumed. Scope: the 4-wide shroud posing (no free jet, no x_traced, no
rotational nodes), the only one the graph records.
"""
import functools

import numpy as np
import jax
import jax.numpy as jnp

import a1_ideal_march_jax as A1
import a1_plug_march as PM

KINDS = ("wall", "int", "shroud", "lip")
# batches are padded to a multiple of `lane` lanes (duplicates of the last
# cell, dropped on output) so that the jitted steps compile once per (kind,
# padded size) instead of once per batch size -- measured: 566 batches of
# ~150 distinct sizes recompiled at every new schedule (170 s per replay
# against 2.5 s steady); the lane width is the caller's posing constant


def _pad(n, lane):
    return -(-n // lane) * lane


def plan(graph):
    """Slots and levels of a recorded graph (numpy, once per record)."""
    N = int(graph["N"])
    alias = graph["alias"]
    slot = {(j, 1): j - 1 for j in range(1, N + 1)}
    cells = graph["cells"]
    n = N
    for c in cells:
        slot[c["out"]] = n
        n += 1

    def sl(k):
        return slot[alias.get(k, k)]
    level = np.zeros(n, dtype=int)
    clev = np.zeros(len(cells), dtype=int)
    for ci, c in enumerate(cells):
        lv = 1 + max(level[sl(k)] for k in c["inp"])
        level[slot[c["out"]]] = lv
        clev[ci] = lv
    batches = []
    for lv in range(1, int(clev.max()) + 1):
        here = np.where(clev == lv)[0]
        for kind in KINDS:
            idx = [ci for ci in here if cells[ci]["kind"] == kind]
            if not idx:
                continue
            b = dict(kind=kind, out=np.array([slot[cells[ci]["out"]] for ci in idx]),
                     inp=np.array([[sl(k) for k in cells[ci]["inp"]] for ci in idx]),
                     zi=np.array([cells[ci]["zi"] for ci in idx]))
            if kind == "wall":
                b["x_next"] = np.array([cells[ci]["x_next"] for ci in idx], dtype=float)
            if kind == "shroud":
                b["seg"] = np.array([cells[ci]["seg"] for ci in idx])
            batches.append(b)
    return dict(n_slots=n, N=N, batches=batches, n_levels=int(clev.max()), n_cells=len(cells),
                wall=np.array([slot[k] for k in graph["wall_out"]]),
                shroud=np.array([slot[k] for k in graph["shroud_out"]]),
                quads=(np.array([[sl(k) for k in q] for q in graph["quads"]]) if graph["quads"]
                       else np.zeros((0, 4), dtype=int)))


_STEPS = {}


def _steps(solvers, ta):
    """One jitted function per cell kind: gather the inputs, build the
    parameters, solve the padded batch (vmap of the implicit solver on the
    recorded seeds, gradient-stopped), post-process, scatter the outputs --
    one dispatch per batch instead of ~8 (compiled once per padded size;
    cached per solver set)."""
    key = tuple(id(f) for f in solvers.values())
    if key in _STEPS:
        return _STEPS[key]
    vs = {k: jax.vmap(lambda z0, p, f=f: f(z0, p, ta)) for k, f in solvers.items()}

    @functools.partial(jax.jit, static_argnames=("n_",))
    def s_int(P, inp, outi, z0, n_):
        p = jnp.concatenate([P[inp[:, 0]], P[inp[:, 1]]], axis=1)
        out = vs["int"](jax.lax.stop_gradient(z0), p)
        return P.at[outi].set(out[:n_])

    @functools.partial(jax.jit, static_argnames=("n_",))
    def s_wall(P, inp, outi, z0, n_, x4w, sx, sy, ssl):
        y4w = jnp.interp(x4w, sx, sy)
        sl_ = jnp.interp(x4w, sx, ssl)
        p = jnp.concatenate([P[inp[:, 0]], P[inp[:, 1]], jnp.stack([x4w, y4w, sl_], axis=1)], axis=1)
        z = vs["wall"](jax.lax.stop_gradient(z0), p)
        out = jnp.stack([x4w, y4w, z[:, 1], sl_ * z[:, 1]], axis=1)
        return P.at[outi].set(out[:n_])

    @functools.partial(jax.jit, static_argnames=("n_",))
    def s_shroud(P, inp, outi, z0, n_, seg, sxs, sys_, sss):
        xA, yA, sA = sxs[seg], sys_[seg], sss[seg]
        xB, yB, sB = sxs[seg + 1], sys_[seg + 1], sss[seg + 1]
        p = jnp.concatenate([P[inp[:, 0]], jnp.stack([xA, yA, sA, xB, yB, sB], axis=1)], axis=1)
        z = vs["shroud"](jax.lax.stop_gradient(z0), p)
        y4, s4 = PM.hermite_seg(z[:, 0], xA, yA, sA, xB, yB, sB)
        out = jnp.stack([z[:, 0], y4, z[:, 1], s4 * z[:, 1]], axis=1)
        return P.at[outi].set(out[:n_])

    @functools.partial(jax.jit, static_argnames=("n_",))
    def s_lip(P, inp, outi, z0, n_, sxs, sys_, sss):
        npad = inp.shape[0]
        tail = jnp.broadcast_to(jnp.stack([sxs[-1], sys_[-1], sss[-1]]), (npad, 3))
        p = jnp.concatenate([P[inp[:, 0]], P[inp[:, 1]], tail], axis=1)
        z = vs["lip"](jax.lax.stop_gradient(z0), p)
        out = jnp.stack([jnp.broadcast_to(sxs[-1], (npad,)), jnp.broadcast_to(sys_[-1], (npad,)),
                         z[:, 1], sss[-1] * z[:, 1]], axis=1)
        return P.at[outi].set(out[:n_])

    _STEPS[key] = dict(int=s_int, wall=s_wall, shroud=s_shroud, lip=s_lip)
    return _STEPS[key]


def replay(pl, sched, stations, shroud, start, tab, delta, lane, margin=None):
    """The replay: returns dict(wall, shroud, margin_ks, margin_min, margin_n)
    -- the pieces J_of and the class read -- differentiable in the traced
    station and shroud arrays; lane = the batch padding width."""
    ta = A1.tab_arrays(tab)
    sx, sy, ssl = stations
    sxs, sys_, sss = shroud
    x0, ys0, us0, vs0 = start
    N = pl["N"]
    x0a = np.atleast_1d(np.asarray(x0, dtype=float))
    if x0a.size == 1:
        x0a = np.full(N, float(x0a[0]))
    P0 = jnp.asarray(np.stack([x0a, np.asarray(ys0, float), np.asarray(us0, float), np.asarray(vs0, float)], axis=1))
    P = jnp.zeros((pl["n_slots"], 4)).at[:N].set(P0)
    solvers = dict(
        int=A1.get_solver(("intbu", delta), lambda: PM.make_resid_interior_bu(delta))[0],
        wall=A1.get_solver(("wb", delta), lambda: PM.make_resid_wallbot(delta))[0],
        shroud=A1.get_solver(("wt", delta), lambda: PM.make_resid_walltop(delta))[0],
        lip=A1.get_solver(("wtlip", delta), lambda: A1.make_resid_inwall(delta))[0])
    steps = _steps(solvers, ta)
    zrec = sched.d["z"]
    for b in pl["batches"]:
        kind = b["kind"]
        n_ = len(b["out"])
        npad = _pad(n_, lane)
        pad = np.r_[np.arange(n_), np.full(npad - n_, n_ - 1)]     # lanes, the last repeated
        inp = jnp.asarray(b["inp"][pad])
        outi = jnp.asarray(b["out"])
        z0 = jnp.asarray(np.stack([zrec[i] for i in b["zi"]])[pad])
        if kind == "int":
            P = steps["int"](P, inp, outi, z0, n_)
        elif kind == "wall":
            P = steps["wall"](P, inp, outi, z0, n_, jnp.asarray(b["x_next"][pad]), sx, sy, ssl)
        elif kind == "shroud":
            P = steps["shroud"](P, inp, outi, z0, n_, jnp.asarray(b["seg"][pad]), sxs, sys_, sss)
        else:
            P = steps["lip"](P, inp, outi, z0, n_, sxs, sys_, sss)
    res = dict(wall=P[pl["wall"]], shroud=P[pl["shroud"]], margin_ks=None, margin_min=None,
               margin_n=int(pl["quads"].shape[0]))
    if margin is not None and pl["quads"].shape[0]:
        q = pl["quads"]
        n_c = q.shape[0]
        PAD = int(margin.get("pad", 0) or 0)
        if PAD > 0:
            n_cp = -(-n_c // PAD) * PAD
            qp = np.concatenate([q, np.repeat(q[-1:], n_cp - n_c, axis=0)], axis=0)
            mask = jnp.asarray(np.arange(n_cp) < n_c)
        else:
            qp, mask = q, None
        cA, cB, cC, cD = [P[qp[:, k]][:, :2] for k in range(4)]
        v = PM.margin_of_corners(cA, cB, cC, cD, mask, margin)
        res["margin_min"] = jnp.min(v)
        res["margin_ks"] = -jax.scipy.special.logsumexp(-margin["rho"] * v) / margin["rho"]
    return res
