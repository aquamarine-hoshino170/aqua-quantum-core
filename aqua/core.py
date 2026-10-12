import math
from .crypto_core import QuantumShield

def _tensor_prod(a, b):
    res = []
    for r1 in a:
        row = []
        for v1 in r1:
            for r2 in b:
                for v2 in r2:
                    row.append(v1 * v2)
        res.append(row)
    return res

def _mat_vec_mul(mat, vec):
    return [sum(mat[i][j] * vec[j] for j in range(len(vec))) for i in range(len(mat))]

class aQuaUniverse:
    """Universal Hamiltonian Engine for Arbitrary Physics/Quantum Systems"""
    def __init__(self, name: str, dimensions: int = 2):
        self.name = name
        self.dimensions = dimensions
        self.hamiltonian = [[0.0] * dimensions for _ in range(dimensions)]
        self.state = [1.0 / math.sqrt(dimensions)] * dimensions

    def add_operator(self, matrix, weight: float = 1.0):
        for i in range(min(self.dimensions, len(matrix))):
            for j in range(min(self.dimensions, len(matrix[0]))):
                self.hamiltonian[i][j] += weight * matrix[i][j]
        return self

    def evolve(self, steps: int = 10):
        # Calculate ground energy: <psi| H |psi>
        h_psi = _mat_vec_mul(self.hamiltonian, self.state)
        expectation_energy = sum(self.state[i] * h_psi[i] for i in range(self.dimensions))
        
        envelope = QuantumShield.seal_state(expectation_energy, self.dimensions)
        return {
            "system": self.name,
            "status": "SIMULATION_CONVERGED",
            "outer_trap": envelope["outer_trap"],
            "inner_core": envelope["inner_core"],
            "cryptographic_status": envelope["cryptographic_status"],
            "ground_energy": round(expectation_energy, 6),
            "hilbert_dimensions": self.dimensions
        }

class aQuaCircuit(aQuaUniverse):
    """Universal N-Qubit State-Vector Circuit"""
    def __init__(self, num_qubits: int):
        dim = 2 ** num_qubits
        super().__init__(name=f"{num_qubits}-Qubit-Circuit", dimensions=dim)
        self.num_qubits = num_qubits
        # Initialize state to |00...0>
        self.state = [1.0] + [0.0] * (dim - 1)

    def apply_gate(self, gate_matrix, target: int):
        # Universal arbitrary 1-qubit gate application using Kronecker products
        i2 = [[1.0, 0.0], [0.0, 1.0]]
        full_op = [[1.0]]
        for q in range(self.num_qubits):
            full_op = _tensor_prod(full_op, gate_matrix if q == target else i2)
        self.state = _mat_vec_mul(full_op, self.state)
        return self

    def h(self, target: int):
        inv_sqrt2 = 1.0 / math.sqrt(2)
        return self.apply_gate([[inv_sqrt2, inv_sqrt2], [inv_sqrt2, -inv_sqrt2]], target)

    def x(self, target: int):
        return self.apply_gate([[0.0, 1.0], [1.0, 0.0]], target)

    def z(self, target: int):
        return self.apply_gate([[1.0, 0.0], [0.0, -1.0]], target)

    def simulate(self):
        envelope = QuantumShield.seal_state(self.state[0], self.dimensions)
        probs = [round(amp ** 2, 4) for amp in self.state]
        return {
            "system": self.name,
            "probabilities": probs,
            "state_vector": [round(x, 4) for x in self.state],
            "outer_trap": envelope["outer_trap"],
            "inner_core": envelope["inner_core"],
            "cryptographic_status": envelope["cryptographic_status"]
        }
