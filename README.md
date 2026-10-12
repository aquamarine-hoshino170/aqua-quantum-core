# aQua Quantum Core (aQua)

Zero-bloat, high-performance Quantum Computing framework. All complex tensor linear algebra and state evaluations are offloaded seamlessly.

## Quick Start

```python
import aqua

# Create a 2-Qubit Entangled Circuit
qc = aqua.aQuaCircuit(2)
qc.h(0).cnot(0, 1)

# Execute via aQua Cloud Engine
result = qc.simulate()
print(result)
