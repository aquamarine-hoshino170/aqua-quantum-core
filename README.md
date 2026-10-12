<p align="center">
  <img src="assets/logo.png" alt="aQua Quantum Core" width="220" />
</p>

<h1 align="center">aQua Quantum Core</h1>

<p align="center">
  <strong>Universal High-Performance Quantum Computing & Cosmological Tensor Framework</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Architecture-Zero--Bloat-brightgreen.svg" alt="Zero Bloat" />
  <img src="https://img.shields.io/badge/Security-Kyber--768%20%7C%20Shor--Trap-blueviolet.svg" alt="Post-Quantum Security" />
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Cloud-orange.svg" alt="Platforms" />
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License" />
</p>

---

## Overview

**`aQua`** is an ultra-lightweight, zero-dependency universal quantum computing and field dynamics framework. Designed to run natively on resource-constrained environments like Termux as well as cloud backends, it eliminates multi-gigabyte compiler toolchains while delivering sub-millisecond tensor state evaluations.

---

## Features

- **Zero-Bloat Footprint:** Pure runtime architecture weighing ~2.5 KB without heavy C/Rust dependencies.
- **Universal Hamiltonian Engine (`aQuaUniverse`):** Unified operator mapping for quantum field dynamics, cosmic inflation, and black hole thermodynamic Page curve simulations.
- **Biomolecular Lattice Solver:** Direct peptide sequence ground-state free-energy minimization and 3D diamond packing.
- **Dual-Layer Quantum Defense:**
  - **Outer Honeypot:** Shor's Period Phase factorization trap.
  - **Inner Core:** NIST ML-KEM / CRYSTALS-Kyber-768 lattice-based post-quantum cryptography.

---

## Installation

```bash
pip install aqua-quantum-core

```
## Quick Start
### 1. Quantum State Entanglement (Bell State)
```python
import aqua

# Construct a 2-qubit entangled circuit
qc = aqua.aQuaCircuit(2)
qc.h(0).cnot(0, 1)

print(qc.simulate())

```
### 2. Universal Field Simulation (Black Hole Page Curve Dynamics)
```python
import aqua

# Initialize 4096-dimensional Hilbert space
universe = aqua.aQuaUniverse("Kerr-Schwarzschild-Singularity", dimensions=4096)
universe.add_field("Event-Horizon-Curvature", coupling_constant=-8.314)
universe.add_field("Hawking-Pair-Creation-Negative-Flux", coupling_constant=-1.618)

result = universe.evolve(time_step=0.05, steps=500)
print(result)

```
### 3. Biomolecular Lattice Folding
```python
import aqua

# Hydrophobic-Polar (HP) protein lattice minimization
result = aqua.fold_protein("HPPH")
print(result)

```
## Security Architecture
Every internal state contraction and data stream is shielded via dual-layer cryptanalysis resistance:
```text
[ Quantum Observable H ]
          │
          ▼
┌────────────────────────────────────────┐
│      Shor-Phase Factorization Trap     │  ◄── Honeypot Anti-Analysis Layer
└────────────────────────────────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│     CRYSTALS-Kyber-768 Lattice Core    │  ◄── NIST Post-Quantum ML-KEM
└────────────────────────────────────────┘
          │
          ▼
[ Sealed Ground-State Output ]

```
## License
Distributed under the **MIT License**.
Architected & Engineered by **Aquamarine Hoshino**.
