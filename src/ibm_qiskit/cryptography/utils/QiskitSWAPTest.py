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


# Class for IBM Qiskit's SWAP Test
class QiskitSWAPTest:

    def __init__(self, name, quantum_circuit, ancilla_qubit_index, ancilla_bit_index,
                 quantum_state_qubits_indexes_1, quantum_state_qubits_indexes_2):

        # Set the name for the SWAP Test
        self.name = name

        # Set the Quantum Circuit for the SWAP Test
        self.quantum_circuit = quantum_circuit

        # Set the index of the Ancilla Qubit,
        # in the Quantum Circuit, for the SWAP Test
        self.ancilla_qubit_index = ancilla_qubit_index

        # Set the index for the Ancilla Bit,
        # in the Quantum Circuit, for the SWAP Test
        self.ancilla_bit_index = ancilla_bit_index

        # If the Quantum States have the same amount of Qubits
        if len(quantum_state_qubits_indexes_1) == len(quantum_state_qubits_indexes_2):

            # Set the two Quantum States for the SWAP Test
            self.quantum_state_qubits_indexes_1 = quantum_state_qubits_indexes_1
            self.quantum_state_qubits_indexes_2 = quantum_state_qubits_indexes_2

        # If the Quantum States for the SWAP Test does not have the same amount of Qubits
        else:

            # Raise a Value Error
            raise ValueError("The two Quantum States must have the same number of Qubits!!!")

    # Return the name of the SWAP Test
    def get_name(self):
        return self.name

    # Return the Quantum Circuit of the SWAP Test
    def get_quantum_circuit(self):
        return self.quantum_circuit

    # Return the index of the Ancilla Qubit,
    # in the Quantum Circuit, for the SWAP Test
    def get_ancilla_qubit_index(self):
        return self.ancilla_qubit_index

    # Return the index of the Ancilla Bit,
    # in the Quantum
    def get_ancilla_bit_index(self):
        return self.ancilla_bit_index

    # Return the indexes of the Qubits of the 1st Quantum State,
    # in the Quantum Circuit of the SWAP Test
    def get_quantum_state_qubits_indexes_1(self):
        return self.quantum_state_qubits_indexes_1

    # Return the indexes of the Qubits of the 2nd Quantum State,
    # in the Quantum Circuit of the SWAP Test
    def get_quantum_state_qubits_indexes_2(self):
        return self.quantum_state_qubits_indexes_2

    # Perform the SWAP Test itself, for the comparison of two Quantum States
    def perform_test_to_compare_quantum_states(self, is_final_measurement=True):

        # Apply the 1st Hadamard Gate to the Ancilla Qubit of
        # the Quantum Circuit, for the SWAP Test
        self.quantum_circuit.apply_hadamard(self.ancilla_qubit_index)

        # For each Pair of Qubits in both Quantum States
        for quantum_state_qubit_index_1, quantum_state_qubit_index_2 in \
            zip(self.quantum_state_qubits_indexes_1, self.quantum_state_qubits_indexes_2):

            # Apply the Controlled-SWAP (Fredkin) to the Quantum Circuit,
            # for the SWAP Test, with the Ancilla Qubit, acting as Control-Qubit,
            # and the Pair of Qubits of both Quantum States, acting as Target-Qubits
            self.quantum_circuit.apply_controlled_swap(self.ancilla_qubit_index,
                                                       quantum_state_qubit_index_1,
                                                       quantum_state_qubit_index_2)

        # Apply the 2nd Hadamard Gate to the Ancilla Qubit of
        # the Quantum Circuit, for the SWAP Test
        self.quantum_circuit.apply_hadamard(self.ancilla_qubit_index)

        # If is a final measurement
        if is_final_measurement:

            # Measure the Ancilla Qubit of the Quantum Circuit, for the SWAP Test
            self.quantum_circuit.measure_single_qubit(0, 0, self.ancilla_qubit_index, self.ancilla_bit_index)
