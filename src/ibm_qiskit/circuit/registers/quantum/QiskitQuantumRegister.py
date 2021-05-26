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

# Import required Libraries and Packages

# Import Quantum Register from IBM Qiskit
from qiskit import QuantumRegister


# Class for the IBM Qiskit's Quantum Register
class QiskitQuantumRegister:

    # Constructor for IBM Qiskit's Quantum Register
    def __init__(self, name, num_qubits, quantum_register=None):

        # The name of the Qiskit's Quantum Register
        self.name = name

        # The number of the Qubits of the Qiskit's Quantum Register
        self.num_qubits = num_qubits

        # If the Quantum Register is None
        if quantum_register is None:

            # The Quantum Register of the Qiskit's Quantum Register
            self.quantum_register = QuantumRegister(name=name, size=num_qubits)

        # If the Quantum Register is not None
        else:

            # The Quantum Register of the Qiskit's Quantum Register
            self.quantum_register = quantum_register
