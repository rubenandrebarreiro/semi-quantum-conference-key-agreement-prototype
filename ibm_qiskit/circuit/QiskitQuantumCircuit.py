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

# Import Square Root and Exponential from NumPy
from numpy import sqrt, exp

# Import Quantum Circuit from IBM Qiskit
from qiskit import QuantumCircuit

# Import Operator from IBM Qiskit
from qiskit.quantum_info.operators import Operator


# Class for the IBM Qiskit's Quantum Circuit
class QiskitQuantumCircuit:

    # Constructor for IBM Qiskit's Quantum Circuit
    def __init__(self, name, quantum_registers, classical_registers, global_phase=0):
        # The name of the Qiskit's Quantum Circuit
        self.name = name

        # The Quantum Registers of the Qiskit's Quantum Circuit
        self.quantum_registers = quantum_registers

        # The Classical Registers of the Qiskit's Quantum Circuit
        self.classical_registers = classical_registers

        # The Global Phase of the Qiskit's Quantum Circuit
        self.global_phase = global_phase

        # The Quantum Circuit of the Qiskit's Quantum Circuit
        self.quantum_circuit = QuantumCircuit(quantum_registers.quantumRegister, classical_registers.classicalRegister,
                                              name=name, global_phase=global_phase)

    # Methods:

    # 1) Utils:

    # Apply a Barrier to a given interval of Qubits' indexes
    def apply_barriers(self, qubit_indexes):
        self.quantum_circuit.barrier(qubit_indexes)

    # 2) Single Qubit Gates:

    # Apply the Pauli-I Gate to a given Qubit's index
    def apply_pauli_i(self, qubit_index):
        self.quantum_circuit.id(qubit_index)

    # Apply the Pauli-X (NOT/Bit Flip) Gate to a given Qubit's index
    def apply_pauli_x(self, qubit_index):
        self.quantum_circuit.x(qubit_index)

    # Apply the Pauli-Y Gate to a given Qubit's index
    def apply_pauli_y(self, qubit_index):
        self.quantum_circuit.y(qubit_index)

    # Apply the Pauli-Z (Phase Flip) Gate to a given Qubit's index
    def apply_pauli_z(self, qubit_index):
        self.quantum_circuit.z(qubit_index)

    # Apply the Hadamard Gate to a given Qubit's index
    def apply_hadamard(self, qubit_index):
        self.quantum_circuit.h(qubit_index)

    # Apply the S Gate (pi/2) to a given Qubit's index
    def apply_phase_s(self, qubit_index):
        self.quantum_circuit.s(qubit_index)

    # Apply the T Gate (pi/4) to a given Qubit's index
    def apply_phase_t(self, qubit_index):
        self.quantum_circuit.t(qubit_index)

    # Apply the adjoint of the S Gate (-pi/2) to a given Qubit's index
    def apply_phase_s_adjoint(self, qubit_index):
        self.quantum_circuit.sdg(qubit_index)

    # Apply the adjoint of the T Gate (-pi/4) to a given Qubit's index
    def apply_phase_t_adjoint(self, qubit_index):
        self.quantum_circuit.tdg(qubit_index)

    # Apply the squared root of the Pauli-X (NOT/Bit Flip) Gate to a given Qubit's index
    def apply_squared_root_pauli_x(self, qubit_index):
        self.quantum_circuit.sx(qubit_index)

    # Apply the squared root of the Pauli-Y Gate to a given Qubit's index
    def apply_squared_root_pauli_y(self, qubit_index):
        squared_root_pauli_y_unitary_operator = Operator([
            [(1 + 1j) * (1 / 2), (1 + 1j) * -(1 / 2)],
            [(1 + 1j) * (1 / 2), (1 + 1j) * (1 / 2)]
        ])

        self.quantum_circuit.unitary(squared_root_pauli_y_unitary_operator, qubit_index)

    # Apply the squared root of the Pauli-Z (Phase Flip) Gate to a given Qubit's index
    def apply_squared_root_pauli_z(self, qubit_index):
        squared_root_pauli_z_unitary_operator = Operator([
            [1, 0],
            [0, 1j]
        ])

        self.quantum_circuit.unitary(squared_root_pauli_z_unitary_operator, qubit_index)

    # Apply the squared root of the Hadamard Gate to a given Qubit's index
    def apply_squared_root_hadamard(self, qubit_index):
        squared_root_hadamard_unitary_operator = Operator([
            [((2 + sqrt(2)) / 4) + (((2 - sqrt(2)) / 4) * 1j), ((sqrt(2) / 4) - (sqrt(2) / 4) * 1j)],
            [((sqrt(2) / 4) - (sqrt(2) / 4) * 1j), ((2 - sqrt(2)) / 4) + (((2 + sqrt(2)) / 4) * 1j)]
        ])

        self.quantum_circuit.unitary(squared_root_hadamard_unitary_operator, qubit_index)

    # Apply the squared root of the S Gate (sqrt(1/2)) Gate to a given Qubit's index
    def apply_squared_root_phase_s(self, qubit_index):
        squared_root_phase_s_unitary_operator = Operator([
            [1, 0],
            [0, sqrt(1j)]
        ])

        self.quantum_circuit.unitary(squared_root_phase_s_unitary_operator, qubit_index)

    # Apply the squared root of the T Gate (sqrt(1/4)) Gate to a given Qubit's index
    def apply_squared_root_phase_t(self, qubit_index):
        squared_root_phase_t_unitary_operator = Operator([
            [1, 0],
            [0, sqrt(exp((1 / sqrt(2) * (1 + 1j))))]
        ])

        self.quantum_circuit.unitary(squared_root_phase_t_unitary_operator, qubit_index)

    # Apply the Rotate X Gate to a given Qubit's index, by a given theta angle argument
    def apply_rx(self, qubit_index, theta):
        self.quantum_circuit.rx(theta, qubit_index)

    # Apply the Rotate Y Gate to a given Qubit's index, by a given theta angle argument
    def apply_ry(self, qubit_index, theta):
        self.quantum_circuit.ry(theta, qubit_index)

    # Apply the Rotate Z Gate to a given Qubit's index, by a given phi angle argument
    def apply_rz(self, qubit_index, phi):
        self.quantum_circuit.rz(phi, qubit_index)

    # Apply the U1 Gate to a given Qubit's index, by a given theta angle argument
    def apply_u1(self, qubit_index, theta):
        self.quantum_circuit.u1(theta, qubit_index)

    # Apply the U2 Gate to a given Qubit's index, by a given phi and lambda angle arguments
    def apply_u2(self, qubit_index, phi, lamb):
        self.quantum_circuit.u2(phi, lamb, qubit_index)

    # Apply the U3 Gate to a given Qubit's index, by a given theta, phi and lambda angle arguments
    def apply_u3(self, qubit_index, theta, phi, lamb):
        self.quantum_circuit.u3(theta, phi, lamb, qubit_index)

    # 2) Multi Qubit Gates:

    # Apply the SWAP Gate to given Qubits' indexes
    def apply_swap(self, qubit_index_1, qubit_index_2):
        self.quantum_circuit.swap(qubit_index_1, qubit_index_2)

    # Apply the iSWAP Gate to given Qubits' indexes
    def apply_i_swap(self, qubit_index_1, qubit_index_2):
        self.quantum_circuit.iswap(qubit_index_1, qubit_index_2)

    # Apply the Controlled-Pauli-X (CNOT) Gate to given Qubits' indexes (1 Control-Qubit and 1 Target-Qubit)
    def apply_controlled_x(self, control_qubit_index, target_qubit_index):
        self.quantum_circuit.cx(control_qubit_index, target_qubit_index)

    # Apply the Controlled-Pauli-Y Gate to given Qubits' indexes (1 Control-Qubit and 1 Target-Qubit)
    def apply_controlled_y(self, control_qubit_index, target_qubit_index):
        self.quantum_circuit.cy(control_qubit_index, target_qubit_index)

    # Apply the Controlled-Pauli-Z Gate to given Qubits' indexes (1 Control-Qubit and 1 Target-Qubit)
    def apply_controlled_z(self, control_qubit_index, target_qubit_index):
        self.quantum_circuit.cz(control_qubit_index, target_qubit_index)

    # Apply the Controlled-Hadamard Gate to given Qubits' indexes (1 Control-Qubit and 1 Target-Qubit)
    def apply_controlled_h(self, control_qubit_index, target_qubit_index):
        self.quantum_circuit.ch(control_qubit_index, target_qubit_index)

    # Apply the Controlled-S Gate (pi/2) to given Qubits' indexes (1 Control-Qubit and 1 Target-Qubit)
    def apply_controlled_phase_s(self, control_qubit_index, target_qubit_index):
        controlled_phase_s_unitary_operator = Operator([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1j]
        ])

        self.quantum_circuit.unitary(controlled_phase_s_unitary_operator, [control_qubit_index, target_qubit_index])

    # Apply the Controlled-T Gate (pi/4) to given Qubits' indexes (1 Control-Qubit and 1 Target-Qubit)
    def apply_controlled_phase_t(self, control_qubit_index, target_qubit_index):
        controlled_phase_t_unitary_operator = Operator([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, exp((1/sqrt(2) * (1 + 1j)))]
        ])

        self.quantum_circuit.unitary(controlled_phase_t_unitary_operator, [control_qubit_index, target_qubit_index])

    # Apply the Controlled-S-Adjoint Gate (-pi/2) to given Qubits' indexes (1 Control-Qubit and 1 Target-Qubit)
    def apply_controlled_phase_s_adjoint(self, control_qubit_index, target_qubit_index):
        controlled_phase_s_unitary_operator = Operator([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -1j]
        ])

        self.quantum_circuit.unitary(controlled_phase_s_unitary_operator, [control_qubit_index, target_qubit_index])

    # Apply the Controlled-T-Adjoint Gate (-pi/4) to given Qubits' indexes (1 Control-Qubit and 1 Target-Qubit)
    def apply_controlled_phase_t_adjoint(self, control_qubit_index, target_qubit_index):
        controlled_phase_t_unitary_operator = Operator([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, exp((1/sqrt(2) * (1 - 1j)))]
        ])

        self.quantum_circuit.unitary(controlled_phase_t_unitary_operator, [control_qubit_index, target_qubit_index])

