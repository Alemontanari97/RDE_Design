#!/bin/bash
# Build the A1 Brick 2 document (LaTeX, GENO-theory-document format)
# and install it as docs/rde_nozzle_A1_brick2_thrust.pdf.
# Engine: tectonic (self-contained; s2 has no TeX Live).
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
TECTONIC="${TECTONIC:-/data10/falco/bin/tectonic}"
cd "$HERE"
# figures (cached: fast unless checkpoints changed)
# ../../.venv-a1/bin/python make_figures.py
"$TECTONIC" main.tex
cp main.pdf ../rde_nozzle_A1_brick2_thrust.pdf
echo "installed -> $(readlink -f ../rde_nozzle_A1_brick2_thrust.pdf)"
