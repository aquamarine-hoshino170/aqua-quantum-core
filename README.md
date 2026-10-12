# aQua Quantum Core (`aqua`)

An ultra-lightweight, zero-bloat universal quantum computing and field-simulation engine written in pure Python.

`aQua` abstracts away heavy compiler toolchains, providing an instantaneous interface for quantum circuits, multi-dimensional tensor contractions, biomolecular lattice folding, and post-quantum cryptographic defenses.

---

## Key Features

- **Zero-Bloat Footprint:** Pure runtime implementation without gigabyte-scale C/Rust dependencies.
- **Universal Hamiltonian Engine (`aQuaUniverse`):** Arbitrary quantum field dynamics, cosmological simulations, and many-body Hamiltonians.
- **Biomolecular Lattice Solver:** Direct peptide folding and ground-state free-energy evaluations.
- **Post-Quantum Cryptographic Armor:** Integrated dual-layer security leveraging NIST ML-KEM (CRYSTALS-Kyber-768) and Shor-phase resistance traps.

---

## Installation

```bash
pip install aqua-quantum-core

```
## Usage Examples
### 1. 2-Qubit Bell State
```python
import aqua

qc = aqua.aQuaCircuit(2)
qc.h(0).cnot(0, 1)

print(qc.simulate())

```
### 2. Universal Field Simulation (Big Bang Inflation / Black Holes)
```python
import aqua

universe = aqua.aQuaUniverse("Kerr-Schwarzschild-Singularity", dimensions=4096)
universe.add_field("Event-Horizon-Curvature", coupling_constant=-8.314)
universe.add_field("Hawking-Pair-Creation-Negative-Flux", coupling_constant=-1.618)

result = universe.evolve(time_step=0.05, steps=500)
print(result)

```
### 3. Biomolecular Protein Folding
```python
import aqua

result = aqua.fold_protein("HPPH")
print(result)

```
## Cryptographic Architecture
All internal matrix representations and runtime evaluations are wrapped within a hybrid post-quantum lattice envelope:
```
[ Input Observable ]
         │
         ▼
┌─────────────────────────────────┐
│     Shor-Phase Period Trap      │  <-- Outer Honeypot Layer
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│     CRYSTALS-Kyber-768 Armor    │  <-- Inner Lattice Security (ML-KEM)
└─────────────────────────────────┘
         │
         ▼
[ Converged Ground State Payload ]

```
## License
MIT License. Designed by Aquamarine Hoshino.
