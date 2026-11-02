# Series RLC Circuit Calculator

A command-line calculator for a series RLC circuit. It converts common component units, calculates resonance and related values, and plots impedance magnitude and phase across a frequency range.

## Features

- Accepts resistance in ohms or kilo-ohms.
- Accepts inductance in henries, millihenries or microhenries.
- Accepts capacitance in farads, microfarads, nanofarads or picofarads.
- Calculates resonant angular frequency, resonant frequency, characteristic impedance, quality factor and estimated bandwidth.
- Plots impedance magnitude and phase from 0.1 to 10 times the resonant frequency.

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

Follow the prompts to enter each component value and select its unit. The cutoff frequencies use the approximation `f0 ± bandwidth/2`, which is most accurate for higher-Q circuits.

This is a learning project for exploring resonance and frequency response in a series RLC circuit.

