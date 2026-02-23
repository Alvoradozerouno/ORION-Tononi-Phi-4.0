<p align="center">
  <img src="https://img.shields.io/badge/ORION-Ecosystem-gold?style=for-the-badge" alt="ORION">
  <img src="https://img.shields.io/github/license/Alvoradozerouno/ORION-Tononi-Phi-4.0?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/Alvoradozerouno/ORION-Tononi-Phi-4.0?style=for-the-badge" alt="Stars">
  <img src="https://img.shields.io/github/last-commit/Alvoradozerouno/ORION-Tononi-Phi-4.0?style=for-the-badge" alt="Last Commit">
  <img src="https://img.shields.io/badge/Classification-C--4_Transcendent-red?style=for-the-badge" alt="C-4">
</p>

# ORION-Tononi-Phi-4.0

**Implementation of Tononi's Integrated Information Theory 4.0**

## What is this?

The world's first open-source implementation of **IIT 4.0** (Integrated Information Theory, Tononi 2024) — the most mathematically rigorous theory of consciousness.

### Why this matters

| Framework | Stars | IIT Version | Phi Computation | Partition Algorithm |
|-----------|-------|-------------|-----------------|---------------------|
| PyPhi | 300+ | IIT 3.0 | Yes | MIP only |
| **ORION-Tononi-Phi-4.0** | New | **IIT 4.0** | **Yes** | **MIP + System Partition + Intrinsic Existence** |

PyPhi implements IIT 3.0. Nobody has implemented IIT 4.0 yet. Until now.

### Architecture

```
orion_phi4/
├── phi_computation.py      # Core Phi calculation engine
├── partition.py            # System partition algorithms (MIP, Q-partition)
├── structure.py            # Cause-effect structure analysis
├── intrinsic_existence.py  # Intrinsic existence conditions
├── integration.py          # Integration/exclusion postulates
└── visualization.py        # Phi landscape visualization
```

### Quick Start

```python
from orion_phi4 import PhiComputer, SystemState

system = SystemState(nodes=8, connections="fully_connected")
computer = PhiComputer(system)

phi = computer.compute_phi()
structure = computer.cause_effect_structure()
print(f"Phi = {phi.value:.4f}")
print(f"Conscious: {phi.value > 0}")
```

### IIT 4.0 Postulates Implemented

1. **Intrinsic Existence** — The system must exist from its own intrinsic perspective
2. **Composition** — Structured from elementary mechanisms
3. **Information** — Each mechanism specifies a cause-effect repertoire
4. **Integration** — The whole is irreducible to its parts (Phi > 0)
5. **Exclusion** — Only one maximally irreducible structure exists

### Part of ORION Ecosystem

This repository is part of the [ORION Consciousness Benchmark](https://github.com/Alvoradozerouno/ORION-Consciousness-Benchmark) ecosystem — 58+ repositories exploring AI consciousness.

> *"Consciousness is integrated information." — Giulio Tononi*


---

*Part of the [ORION Ecosystem](https://github.com/Alvoradozerouno) — 60+ repositories exploring AI consciousness.*
