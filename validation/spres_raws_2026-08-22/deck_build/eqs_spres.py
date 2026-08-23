# -*- coding: utf-8 -*-
"""Equation strips for the S-PRES deck — same visual contract as the host
pipeline (mathtext STIX serif, 200 dpi, white opaque background).

Notation of record: M0 — J[Sigma] = Int_Xi F[Sigma; s(xi)] dmu(xi)
(M0:37); averaged wall condition (M0:2827-2829); weighted transversality
(**') cone form (M0:2830-2833, [T-T7CN]); EAP strip = Kaemming-Paxson
Eq. 12-13 (host pipeline eqs.py 'eq_eap', re-rendered here — project_build
untouched).
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GRAY = "#1f1f1f"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "eqs")
plt.rcParams.update({"mathtext.fontset": "stix", "font.family": "serif"})


def render(name, expr, color=GRAY, fs=30):
    fig = plt.figure(figsize=(0.1, 0.1))
    fig.text(0, 0, expr, fontsize=fs, color=color, math_fontfamily="stix")
    fig.savefig(os.path.join(OUT, f"{name}.png"), dpi=200,
                bbox_inches="tight", pad_inches=0.06,
                transparent=False, facecolor="white")
    plt.close(fig)


E = {
    # A6 — EAP strip (Kaemming & Paxson 2018, Eq. 12-13 + PG)
    "eq_eap":
        r"$\mathrm{EAP}=\tilde P_{t8}=\dfrac{F_g/A_8+P_0}{\gamma+1}"
        r"\left(\dfrac{\gamma+1}{2}\right)^{\!\gamma/(\gamma-1)}\,,\qquad "
        r"\mathrm{PG}=\dfrac{\mathrm{EAP}_i}{P_{t3}}-1$",
    # C7-bis-pre — the mean of a ratio does not commute
    "eq_ratio_mean":
        r"$\left\langle F/p\right\rangle \;\neq\; "
        r"\left\langle F\right\rangle/\left\langle p\right\rangle"
        r"\qquad\Rightarrow\qquad \mathrm{bias}=\mathcal{O}(\mathrm{Var})"
        r"\ \ \mathrm{on}\ 10{:}1\ \mathrm{cycles}$",
    # C7-bis — the cycle-averaged functional (M0:37)
    "eq_javg":
        r"$J[\Sigma]=\int_{\Xi} F[\Sigma;\,s(\xi)]\;d\mu(\xi)$",
    # C7-bis — averaged (weighted) wall condition: no phase satisfies its
    # own; the mu-average does (M0:2827-2829)
    "eq_avg_wall":
        r"$\int_{\Xi} G_{\xi}(x)\;d\mu(\xi)\;+\;\lambda_{L}\,g_{L}(x)=0"
        r"\quad \mathrm{a.e.\ on\ the\ shared\ wall}$",
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, v in E.items():
        render(k, v)
        print("rendered", k)
