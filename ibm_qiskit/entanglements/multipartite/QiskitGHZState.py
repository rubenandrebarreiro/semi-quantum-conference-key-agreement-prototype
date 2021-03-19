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


# Class for IBM Qiskit's Bell State
class QiskitGHZState:

    # Constructor for IBM Qiskit's Bell State
    def __init__(self, name, quantum_circuit, control_qubit_index, target_qubits_indexes):
        self.name = name
        self.quantum_circuit = quantum_circuit
        self.control_qubit_index = control_qubit_index
        self.target_qubits_indexes = target_qubits_indexes

        # The number of Qubits of the given IBM Qiskit's Quantum Circuit
        num_qubits_quantum_circuit = quantum_circuit.get_num_qubits()

        # If the number of Qubits of the given IBM Qiskit's Quantum Circuit is strictly lower than 2,
        # a Value Error exception will be raised
        if num_qubits_quantum_circuit < 3:

            # Raise the Value Error exception
            raise ValueError("It is impossible to create a GHZ State, from a IBM Qiskit's Quantum Circuit with "
                             "less than 3 Qubits!!!")

    # Prepare the multipartite entanglement for the Bell State configured
    def prepare_multipartite_entanglement(self):

        # Apply a Barrier to the Control-Qubit
        self.quantum_circuit.apply_barrier(self.control_qubit_index)

        # Apply Barriers to the interval of Target-Qubits
        self.quantum_circuit.apply_barriers_interval(self.target_qubits_indexes)

        # Apply the Hadamard Gate to the Control-Qubit index
        self.quantum_circuit.apply_hadamard(self.control_qubit_index)

        # For each Target-Qubit
        for target_qubit_index in self.target_qubits_indexes:

            # Apply the Controlled-Pauli-X (CNOT) Gate to the Control-Qubit and current Target-Qubit
            self.quantum_circuit.apply_controlled_x(self.control_qubit_index, target_qubit_index)

        # Apply a Barrier to the Control-Qubit
        self.quantum_circuit.apply_barrier(self.control_qubit_index)

        # Apply Barriers to the interval of Target-Qubits
        self.quantum_circuit.apply_barriers_interval(self.target_qubits_indexes)

        # Return the IBM Qiskit's Bell State, as a multipartite entanglement
        return self.quantum_circuit

    # Measure the multipartite entanglement for the GHZ State configured
    def measure_multipartite_entanglement(self, is_final_measurement=True):

        # Set the Control-Bit and Target-Bits,
        # for the measurement of the Control-Qubit and Target-Qubits, respectively
        control_bit_index, target_bits_indexes = self.control_qubit_index, self.target_qubits_indexes

        # Apply a Barrier to the Control-Qubit
        self.quantum_circuit.apply_barrier(self.control_qubit_index)

        # Apply Barriers to the interval of Target-Qubits
        self.quantum_circuit.apply_barriers_interval(self.target_qubits_indexes)

        # Reverse the list of Target-Qubits
        target_qubits_indexes_reversed = self.target_qubits_indexes.reverse()

        # For each Target-Qubit
        for target_qubit_index_reversed in target_qubits_indexes_reversed:

            # Apply the Controlled-Pauli-X (CNOT) Gate to the Control-Qubit and current Target-Qubit
            self.quantum_circuit.apply_controlled_x(self.control_qubit_index, target_qubit_index_reversed)

        # Apply the Hadamard Gate to the Control-Qubit index
        self.quantum_circuit.apply_hadamard(self.control_qubit_index)

        # Apply a Barrier to the Control-Qubit
        self.quantum_circuit.apply_barrier(self.control_qubit_index)

        # Apply Barriers to the interval of Target-Qubits
        self.quantum_circuit.apply_barriers_interval(self.target_qubits_indexes)

        # If is a final measurement
        if is_final_measurement:

            # Measure the Control-Qubit of the Quantum Circuit, for the GHZ State
            self.quantum_circuit.measure_single_qubit(self.control_qubit_index, control_bit_index)

            # Measure the Target-Qubits of the Quantum Circuit, for the GHZ State
            self.quantum_circuit.measure_qubits_interval(self.target_qubits_indexes,
                                                         target_bits_indexes)

        # Return the IBM Qiskit's GHZ State, as a multipartite entanglement
        return self.quantum_circuit
