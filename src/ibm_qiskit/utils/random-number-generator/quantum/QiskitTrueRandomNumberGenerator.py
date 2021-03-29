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

# Import Packages and Libraries

# Import Mathematics
from math import floor, log

# Import QiskitQuantumCircuit from IBM_Qiskit.Circuit
from src.ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister

# Class for the IBM Qiskit's Quantum True Random Number Generator (TRNG)
from src.ibm_qiskit.utils.transforms import QiskitQuantumHadamardTransform


# Class for IBM Qiskit's Quantum True Random Number Generator (TRNG)
class QiskitQuantumTrueRandomNumberGenerator:

    # Constructor for IBM Qiskit's Quantum True Random Number Generator (TRNG)
    def __init__(self, name, number_type, number_lower_bound=0, number_upper_bound=1):
        self.name = name
        self.number_type = number_type.upper()
        self.number_lower_bound = number_lower_bound
        self.number_upper_bound = number_upper_bound

        delta_interval = (self.number_upper_bound - self.number_lower_bound)

        if self.number_type == "INTEGER":
            self.binary_length = (floor(log(delta_interval, 2)) + 1)
        elif self.number_type == "FLOATING_POINT_16_EXPONENT":
            self.binary_length = (floor(log(16, 2)) + 1)
        elif self.number_type == "FLOATING_POINT_8_EXPONENT":
            self.binary_length = (floor(log(8, 2)) + 1)

    # Generate a True Random Number
    def generate_true_random_number(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = self.binary_length

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_true_random_number = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrtrng{}qubit(s)".format(num_qubits), num_qubits)
        qiskit_classical_register_true_random_number = \
            QiskitClassicalRegister.QiskitClassicalRegister("crtrng{}qubit(s)".format(num_bits), num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_true_random_number_generator = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qctrng{}qubit(s)".format(num_qubits),
                                                      qiskit_quantum_register_true_random_number,
                                                      qiskit_classical_register_true_random_number,
                                                      global_phase=0)

        # Setup of the range of Qubits' indexes
        qubit_indexes = range(0, num_qubits)

        # Apply the Quantum Hadamard Transform for n Qubit(s) for True Random Number Generator (TRNG)
        qiskit_quantum_hadamard_transform_circuit_trng = QiskitQuantumHadamardTransform \
            .QiskitQuantumHadamardTransform("quantum_hadamard_transform_{}_qubits".format(num_qubits),
                                            qiskit_quantum_circuit_true_random_number_generator,
                                            qubit_indexes).apply_transform()
