"""
Semi-Quantum Conference Key Agreement (SQCKA)

Author:
- Ruben Andre Barreiro (r.barreiro@campus.fct.unl.pt)

Supervisors:
- Andre Nuno Souto (ansouto@fc.ul.pt)
- Antonio Maria Ravara (aravara@fct.unl.pt)

Acknowledgments:
- Paulo Alexandre Mateus (pmat@math.ist.utl.pt)
"""


# Class for the IBM Qiskit's Quantum Hadamard Transform
class QiskitQuantumHadamardTransform:

    # Constructor for IBM Qiskit's Quantum Hadamard Transform
    def __init__(self, name, quantum_circuit, qubits_indexes):
        self.name = name
        self.quantum_circuit = quantum_circuit
        self.qubits_indexes = qubits_indexes

    # Apply the Quantum Hadamard Transform to
    # the respective given Qubits' indexes in the IBM Qiskit's Quantum Circuit
    def apply_transform(self):

        # For each indexed Qubit
        for qubit_index in self.qubits_indexes:

            # Apply the Hadamard Gate to the current Qubit index
            self.quantum_circuit.apply_hadamard(qubit_index)

        return self.quantum_circuit
