# RLC Circuit Calculator

A command-line calculator for series, parallel and mixed RLC circuits. Choose how the resistor, inductor and capacitor are connected, enter their values and units, then view the calculated resonance information and impedance response graph.

## Features

- Supports R, L and C all in series or all in parallel.
- Supports mixed circuits where two components are in parallel and the third is in series.
- Accepts resistance in ohms or kilo-ohms.
- Accepts inductance in henries, millihenries or microhenries.
- Accepts capacitance in farads, microfarads, nanofarads or picofarads.
- Calculates resonance information where applicable and plots impedance magnitude and phase over a frequency sweep.

## Requirements

- Python 3
- Matplotlib

Install Matplotlib with:

```bash
python -m pip install matplotlib
```

## Run

```bash
python rlc_circuit_calculator.py
```

Follow the prompts to select the circuit arrangement, confirm the diagram and enter each component value with its unit.

This is a learning project for exploring resonance and frequency response in RLC circuits.