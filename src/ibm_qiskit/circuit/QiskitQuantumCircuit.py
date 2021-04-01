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

# Import Squared Root and Exponential from NumPy
from numpy import sqrt, exp

# Import Quantum Circuit from IBM Qiskit
from qiskit import QuantumCircuit

# Import Operator from IBM Qiskit
from qiskit.quantum_info.operators import Operator

# Import IBM Qiskit's Quantum Register from IBM_Qiskit.Circuit.Registers.Quantum
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister

# Import IBM Qiskit's Classical Register from IBM_Qiskit.Circuit.Registers.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister


# Class for the IBM Qiskit's Quantum Circuit
class QiskitQuantumCircuit:

    # Constructor for IBM Qiskit's Quantum Circuit
    def __init__(self, name, quantum_registers=None, classical_registers=None, global_phase=0,
                 quantum_circuit=None, memory_enumeration_tag=None):

        # The name of the Qiskit's Quantum Circuit
        self.name = name

        # The Enumeration Tag used, for the case of this Quantum Circuit represent a Memory
        self.memory_enumeration_tag = memory_enumeration_tag

        # If there is no given any Quantum Circuit, it will be created a new one,
        # according to the given Quantum and Classical Registers
        if quantum_circuit is None:

            # If the Quantum and Classical Registers given as arguments are not None
            # (i.e., a Quantum Circuit equivalent to a hybrid Quantum-Classical Memory)
            if (quantum_registers is not None) and (classical_registers is not None):

                # The Quantum Registers of the Qiskit's Quantum Circuit
                self.quantum_registers = quantum_registers

                # The Classical Registers of the Qiskit's Quantum Circuit
                self.classical_registers = classical_registers

                # The Global Phase of the Qiskit's Quantum Circuit
                self.global_phase = global_phase

                # If the Quantum Circuit it will be composed by a single Quantum Register and Classical Register
                if (isinstance(quantum_registers, QiskitQuantumRegister.QiskitQuantumRegister) and
                        isinstance(classical_registers, QiskitClassicalRegister.QiskitClassicalRegister)):

                    # The Quantum Circuit of the Qiskit's Quantum Circuit
                    self.quantum_circuit = \
                        QuantumCircuit(quantum_registers.quantum_register,
                                       classical_registers.classical_register,
                                       name=name, global_phase=global_phase)

                # If the Quantum Circuit it will be composed by multiple Quantum Registers and Classical Registers
                elif (isinstance(quantum_registers, list) and
                        isinstance(classical_registers, list)):

                    # The Quantum Circuit of the Qiskit's Quantum Circuit
                    self.quantum_circuit = \
                        QuantumCircuit([quantum_register.quantum_register for quantum_register in quantum_registers],
                                       [classical_register.classical_register for classical_register in
                                        classical_registers],
                                       name=name, global_phase=global_phase)

            # If the Classical Register given as argument is None, but the Quantum Register do not
            # (i.e., a Quantum Circuit equivalent to a pure Quantum Memory)
            elif (quantum_registers is not None) and (classical_registers is None):

                # Initialise the Classical Registers as None
                self.classical_registers = None

                # If the Quantum Circuit it will be composed by a single Quantum Register
                if isinstance(quantum_registers, QiskitQuantumRegister.QiskitQuantumRegister):

                    # The Quantum Circuit of the Qiskit's Quantum Circuit
                    self.quantum_circuit = \
                        QuantumCircuit(quantum_registers.quantum_register,
                                       name=name, global_phase=global_phase)

                # If the Quantum Circuit it will be composed by multiple Quantum Registers
                elif isinstance(quantum_registers, list):

                    # The Quantum Circuit of the Qiskit's Quantum Circuit
                    self.quantum_circuit = \
                        QuantumCircuit([quantum_register.quantum_register for quantum_register in quantum_registers],
                                       name=name, global_phase=global_phase)

            # If the Quantum Register given as argument is None, but the Classical Register do not
            # (i.e., a Quantum Circuit equivalent to a pure Classical Memory)
            elif (quantum_registers is None) and (classical_registers is not None):

                # Initialise the Quantum Registers as None
                self.quantum_registers = None

                # If the Quantum Circuit it will be composed by a single Classical Register
                if isinstance(classical_registers, QiskitClassicalRegister.QiskitClassicalRegister):

                    # The Quantum Circuit of the Qiskit's Quantum Circuit
                    self.quantum_circuit = \
                        QuantumCircuit(classical_registers.classical_register,
                                       name=name, global_phase=global_phase)

                # If the Quantum Circuit it will be composed by multiple Classical Registers
                elif isinstance(classical_registers, list):

                    # The Quantum Circuit of the Qiskit's Quantum Circuit
                    self.quantum_circuit = \
                        QuantumCircuit([classical_register.classical_register for classical_register in classical_registers],
                                       name=name, global_phase=global_phase)

        # If there is given one Quantum Circuit, the same it will be used
        else:

            # The Quantum Registers of the Qiskit's Quantum Circuit
            self.quantum_registers = quantum_registers

            # The Classical Registers of the Qiskit's Quantum Circuit
            self.classical_registers = classical_registers

            # Set the given Quantum Circuit as the one given as argument
            self.quantum_circuit = quantum_circuit

    # Methods:

    # 1) Utilities:

    # Return the number of Qubits of the Quantum Circuit
    def get_num_qubits(self):
        return self.quantum_circuit.num_qubits

    # Return the number of Bits of the Quantum Circuit
    def get_num_bits(self):
        return self.quantum_circuit.num_clbits

    # Return the reverted Circuit (i.e., the reverted Quantum Gates)
    def reverse_quantum_circuit(self):
        return self.quantum_circuit.reverse_ops()

    # Combine the Quantum Circuit with another one, and return the resulting combination of Quantum Circuits
    def combine_quantum_circuit(self, combined_quantum_circuit_name, other_quantum_circuit, global_phase=0):

        # Create a new Quantum Circuit resulted from the previously combined Quantum Circuits
        combined_quantum_circuit = self.quantum_circuit.combine(other_quantum_circuit.quantum_circuit)

        # Retrieve the Quantum Registers of the combined Quantum Circuits
        quantum_registers = combined_quantum_circuit.qregs

        # Retrieve the Classical Registers of the combined Quantum Circuits
        classical_registers = combined_quantum_circuit.cregs

        # Create the object for the IBM Qiskit's Quantum Circuit, from the previously combined one
        qiskit_combined_quantum_circuit = \
            QiskitQuantumCircuit(combined_quantum_circuit_name, quantum_registers, classical_registers,
                                 global_phase, combined_quantum_circuit)

        # Return the object for the IBM Qiskit's Quantum Circuit, from the previously combined one
        return qiskit_combined_quantum_circuit

    # Apply a Barrier to a given Qubit's index
    def apply_barrier(self, qubit_index):

        # The number of Qubits of the Quantum Circuit
        num_qubits_quantum_circuit = self.get_num_qubits()

        # If the Qubit's index is higher or equal than the number of Qubits of the Quantum Circuit,
        # a Value Error exception will be raised
        if qubit_index >= num_qubits_quantum_circuit:
            raise ValueError("The Qubits' indexes must be strictly lower than {}!!!"
                             .format(num_qubits_quantum_circuit))

        # Apply a Barrier to the given Qubit's index
        self.quantum_circuit.barrier(qubit_index)

    # Apply a Barrier to a given interval of Qubits' indexes
    def apply_barriers_interval(self, qubit_indexes):

        # The number of Qubits of the Quantum Circuit
        num_qubits_quantum_circuit = self.get_num_qubits()

        # Remove duplicated Qubits' indexes (just for the case)
        qubit_indexes = list(dict.fromkeys(qubit_indexes))

        # The maximum index of the given interval of Qubits' indexes
        max_qubit_index = max(qubit_indexes)

        # If the maximum Qubit's index is higher or equal than the number of Qubits of the Quantum Circuit,
        # a Value Error exception will be raised
        if max_qubit_index >= num_qubits_quantum_circuit:

            # Raise the Value Error exception
            raise ValueError("The Qubits' indexes must be strictly lower than {}!!!"
                             .format(num_qubits_quantum_circuit))

        # For each Qubit's index
        for qubit_index in qubit_indexes:
            # Apply a Barrier to the current Qubit's index
            self.quantum_circuit.barrier(qubit_index)

    # Apply a Barrier to all Qubits' indexes
    def apply_barriers_to_all(self):

        # The number of Qubits of the Quantum Circuit
        num_qubits_quantum_circuit = self.get_num_qubits()

        # For each Qubit's index
        for qubit_index in range(num_qubits_quantum_circuit):
            # Apply a Barrier to the current Qubit's index
            self.quantum_circuit.barrier(qubit_index)

    # 2) Measurements:

    # Measure a given single Qubit's index
    def measure_single_qubit(self, quantum_register_index, classical_register_index, qubit_index, bit_index):

        # The number of Qubits of the Quantum Circuit
        num_qubits_quantum_circuit = self.get_num_qubits()

        # If the Qubit's index is higher or equal than the number of Qubits of the Quantum Circuit,
        # a Value Error exception will be raised
        if qubit_index >= num_qubits_quantum_circuit:

            # Raise the Value Error exception
            raise ValueError("The Qubits' indexes must be strictly lower than {}!!!"
                             .format(num_qubits_quantum_circuit))

        # Measure the given Qubit's index to the given Bit's index
        self.quantum_circuit.measure(self.quantum_registers[quantum_register_index].quantum_register[qubit_index],
                                     self.classical_registers[classical_register_index].classical_register[bit_index])

    # Measure a given interval of Qubits' indexes
    def measure_qubits_interval(self, qubit_indexes, bit_indexes):

        # The number of Qubits of the Quantum Circuit
        num_qubits_quantum_circuit = self.get_num_qubits()

        # The number of Bits of the Quantum Circuit
        num_bits_quantum_circuit = self.get_num_bits()

        # Remove duplicated Qubits' indexes (just for the case)
        qubit_indexes = list(dict.fromkeys(qubit_indexes))

        # Remove duplicated Bits' indexes (just for the case)
        bit_indexes = list(dict.fromkeys(bit_indexes))

        # The maximum index of the given interval of Qubits' indexes
        max_qubit_index = max(qubit_indexes)

        # The maximum index of the given interval of Bits' indexes
        max_bit_index = max(bit_indexes)

        # If the maximum Qubit's index is higher or equal than the number of Qubits of the Quantum Circuit,
        # a Value Error exception will be raised
        if max_qubit_index >= num_qubits_quantum_circuit:
            # Raise the Value Error exception
            raise ValueError("The Qubits' indexes must be strictly lower than {}!!!"
                             .format(num_qubits_quantum_circuit))

        # If the maximum Bit's index is higher or equal than the number of Bits of the Quantum Circuit,
        # a Value Error exception will be raised
        if max_bit_index >= num_bits_quantum_circuit:
            # Raise the Value Error exception
            raise ValueError("The Bits' indexes must be strictly lower than {}!!!"
                             .format(num_bits_quantum_circuit))

        # If the number of Qubits' and Bits' indexes is different
        if len(qubit_indexes) != len(bit_indexes):
            # Raise the Value Error exception
            raise ValueError("The number of Qubits' and Bits' indexes must be equal!!!")

        # For each Qubit's and Bit's index
        for qubit_index, bit_index in zip(qubit_indexes, bit_indexes):
            # Measure the given Qubit's index to the given Bit's index
            self.quantum_circuit.measure(self.quantum_registers.quantum_register[qubit_index],
                                         self.classical_registers.classical_register[bit_index])

    # Measure all Qubits' indexes to all Bits' indexes
    def measure_all_qubits(self):

        # The number of Qubits of the Quantum Circuit
        num_qubits_quantum_circuit = self.get_num_qubits()

        # The number of Bits of the Quantum Circuit
        num_bits_quantum_circuit = self.get_num_bits()

        # For each Qubit's and Bit's index
        for qubit_index, bit_index in zip(range(num_qubits_quantum_circuit), range(num_bits_quantum_circuit)):
            # Measure the given Qubit's index to the given Bit's index
            self.quantum_circuit.measure(self.quantum_registers.quantum_register[qubit_index],
                                         self.classical_registers.classical_register[bit_index])

    # Measure all Qubits' (predefined by IBM Qiskit)
    def measure_all_qubits_predefined(self):

        # Measure all Qubits in the Quantum Circuit
        self.quantum_circuit.measure_all()

    # Prepare/Measure a given Qubit's index in the X-Basis
    def prepare_measure_single_qubit_in_x_basis(self, quantum_register_index, classical_register_index,
                                                qubit_index, bit_index, is_final_measurement=True):

        # Apply a Barrier to the given Qubit index, to ensure the previous operations were all performed
        self.apply_barrier(qubit_index)

        # Apply the Hadamard Gate to the given Qubit index, to prepare it in the X-Basis
        self.apply_hadamard(qubit_index)

        # If it is the final measurement, measure the given Qubit in the X-Basis
        if is_final_measurement:

            # Measure the given Qubit's index to the given Bit's index
            self.measure_single_qubit(quantum_register_index, classical_register_index, qubit_index, bit_index)

        # Return the Quantum Circuit with all the Qubits prepared/measured in the X-Basis
        return self.quantum_circuit

    # Prepare/Measure a given Qubit's index in the Y-Basis
    def prepare_measure_single_qubit_in_y_basis(self, quantum_register_index, classical_register_index,
                                                qubit_index, bit_index, is_final_measurement=True):

        # Apply a Barrier to the given Qubit index, to ensure the previous operations were all performed
        self.apply_barrier(qubit_index)

        # Apply the Hadamard Gate to the given Qubit index, to prepare it in the X-Basis
        self.apply_hadamard(qubit_index)

        # Apply, then, the Phase S to the given Qubit index, to, finally, prepare it in the Y-Basis
        self.apply_phase_s(qubit_index)

        # If it is the final measurement, measure the given Qubit in the Y-Basis
        if is_final_measurement:

            # Measure the given Qubit's index to the given Bit's index
            self.measure_single_qubit(quantum_register_index, classical_register_index, qubit_index, bit_index)

        # Return the Quantum Circuit with all the Qubits prepared/measured in the Y-Basis
        return self.quantum_circuit

    # Prepare/Measure a given Qubit's index in the Z-Basis
    def prepare_measure_single_qubit_in_z_basis(self, quantum_register_index, classical_register_index,
                                                qubit_index, bit_index, is_final_measurement=True):

        # Apply a Barrier to the given Qubit index, to ensure the previous operations were all performed
        self.apply_barrier(qubit_index)

        # Apply the Pauli-I Gate to the current Qubit index,
        # to prepare it in the Z-Basis (i.e., the Standard Measurement)
        self.apply_pauli_i(qubit_index)

        # If it is the final measurement, measure the given Qubit in the Z-Basis
        if is_final_measurement:

            # Measure the given Qubit's index to the given Bit's index
            self.measure_single_qubit(quantum_register_index, classical_register_index, qubit_index, bit_index)

        # Return the Quantum Circuit with all the Qubits prepared/measured in the Z-Basis
        return self.quantum_circuit

    # Prepare/Measure all the Qubits in the X-Basis
    def measure_all_qubits_in_x_basis(self, is_final_measurement=True):

        # For each indexed Qubit
        for qubit_index in range(self.get_num_qubits()):
            # Apply a Barrier to the current Qubit index, to ensure the previous operations were all performed
            self.apply_barrier(qubit_index)

            # Apply the Hadamard Gate to the current Qubit index, to prepare it in the X-Basis
            self.apply_hadamard(qubit_index)

        # If it is the final measurement, measure all the Qubits in the X-Basis
        if is_final_measurement:

            # Measure all Qubits to their respective Bits
            self.measure_all_qubits()

        # Return the Quantum Circuit with all the Qubits prepared/measured in the X-Basis
        return self.quantum_circuit

    # Prepare/Measure all the Qubits in the Y-Basis
    def measure_all_qubits_in_y_basis(self, is_final_measurement=True):

        # For each indexed Qubit
        for qubit_index in range(self.get_num_qubits()):

            # Apply a Barrier to the current Qubit index, to ensure the previous operations were all performed
            self.apply_barrier(qubit_index)

            # Apply the Hadamard Gate to the current Qubit index, to prepare it in the X-Basis
            self.apply_hadamard(qubit_index)

            # Apply, then, the Phase S to the current Qubit index, to, finally, prepare it in the Y-Basis
            self.apply_phase_s(qubit_index)

        # If it is the final measurement, measure all the Qubits in the Y-Basis
        if is_final_measurement:

            # Measure all Qubits to their respective Bits
            self.measure_all_qubits()

        # Return the Quantum Circuit with all the Qubits prepared/measured in the Y-Basis
        return self.quantum_circuit

    # Prepare/Measure all the Qubits in the Z-Basis
    def measure_all_qubits_in_z_basis(self, is_final_measurement=True):

        # For each indexed Qubit
        for qubit_index in range(self.get_num_qubits()):
            # Apply a Barrier to the current Qubit index, to ensure the previous operations were all performed
            self.apply_barrier(qubit_index)

            # Apply the Pauli-I Gate to the current Qubit index,
            # to prepare it in the Z-Basis (i.e., the Standard Measurement)
            self.apply_pauli_i(qubit_index)

        # If it is the final measurement, measure all the Qubits in the Z-Basis
        if is_final_measurement:
            # Measure all Qubits to their respective Bits
            self.measure_all_qubits()

        # Return the Quantum Circuit with all the Qubits prepared/measured in the Z-Basis
        return self.quantum_circuit

    # 3) Single Qubit Gates:

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
    def apply_rx(self, theta, qubit_index):
        self.quantum_circuit.rx(theta, qubit_index)

    # Apply the Rotate Y Gate to a given Qubit's index, by a given theta angle argument
    def apply_ry(self, theta, qubit_index):
        self.quantum_circuit.ry(theta, qubit_index)

    # Apply the Rotate Z Gate to a given Qubit's index, by a given phi angle argument
    def apply_rz(self, phi, qubit_index):
        self.quantum_circuit.rz(phi, qubit_index)

    # Apply the U1 Gate to a given Qubit's index, by a given theta angle argument
    def apply_u1(self, theta, qubit_index):
        self.quantum_circuit.u1(theta, qubit_index)

    # Apply the U2 Gate to a given Qubit's index, by a given phi and lambda angle arguments
    def apply_u2(self, phi, lamb, qubit_index):
        self.quantum_circuit.u2(phi, lamb, qubit_index)

    # Apply the U3 Gate to a given Qubit's index, by a given theta, phi and lambda angle arguments
    def apply_u3(self, theta, phi, lamb, qubit_index):
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
            [0, 0, 0, exp((1 / sqrt(2) * (1 + 1j)))]
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
            [0, 0, 0, exp((1 / sqrt(2) * (1 - 1j)))]
        ])

        self.quantum_circuit.unitary(controlled_phase_t_unitary_operator, [control_qubit_index, target_qubit_index])
