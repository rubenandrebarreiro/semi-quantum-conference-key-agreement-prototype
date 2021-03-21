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
# Import Libraries and Packages

# Import the Arc-cosine function and Squared Roots from NumPy
from numpy import arccos, sqrt


# Class for IBM Qiskit's W State
class QiskitWState:

    # Constructor for IBM Qiskit's W State
    def __init__(self, name, quantum_circuit, qubits_indexes):
        self.name = name
        self.quantum_circuit = quantum_circuit
        self.qubits_indexes = qubits_indexes

        # The number of Qubits of the given IBM Qiskit's Quantum Circuit
        num_qubits_quantum_circuit = quantum_circuit.get_num_qubits()

        # If the number of Qubits of the given IBM Qiskit's Quantum Circuit is strictly lower than 3,
        # a Value Error exception will be raised
        if num_qubits_quantum_circuit < 3:

            # Raise the Value Error exception
            raise ValueError("It is impossible to create a W State, from a IBM Qiskit's Quantum Circuit with "
                             "less than 3 Qubits!!!")

    # Prepare the multipartite entanglement for the W State configured
    def prepare_multipartite_entanglement(self):

        # Compute the number of Qubits of the W State
        num_qubits = len(self.qubits_indexes)

        # Apply Barriers to the interval of Qubits
        self.quantum_circuit.apply_barriers_interval(self.qubits_indexes)

        # Apply the Pauli-X Gate to the last Qubit index
        self.quantum_circuit.apply_pauli_x(self.qubits_indexes[(num_qubits - 1)])

        # For each Operator's Index, with exception of the last one
        for operator_index in range(num_qubits - 1):

            # Compute the theta angle of the arc-cosine, for the current Operator's Index,
            # counting from the end
            theta = arccos(sqrt(1 / (num_qubits - operator_index)))

            # Apply the Ry Gate, regarding the theta angle and the current Operator's Index,
            # less two indexes counting from the end
            self.quantum_circuit.apply_ry(-theta, self.qubits_indexes[(num_qubits - operator_index - 2)])

            # Apply the Controlled-Z Gate, regarding the Qubit of the current Operator's Index and the previous one,
            # counting from the end, as the Control-Qubit and Target-Qubit, respectively
            self.quantum_circuit.apply_controlled_z(self.qubits_indexes[(num_qubits - operator_index - 1)],
                                                    self.qubits_indexes[(num_qubits - operator_index - 2)])

            # Apply the Ry Gate, regarding the theta angle and the current Operator's Index,
            # less one index counting from the end
            self.quantum_circuit.apply_ry(theta, self.qubits_indexes[(num_qubits - operator_index - 2)])

            # Apply a Barrier, to the Qubit of the current Operator's Index, counting from the end
            self.quantum_circuit.apply_barrier(self.qubits_indexes[(num_qubits - operator_index - 1)])

        # For each Operator's Index, with exception of the last one
        for operator_index in range(num_qubits - 1):

            # Apply the Controlled-X Gate, regarding the Qubit of the previous Operator's Index and the current one,
            # counting from the end, as the Control-Qubit and Target-Qubit, respectively
            self.quantum_circuit.apply_controlled_x(self.qubits_indexes[(num_qubits - operator_index - 2)],
                                                    self.qubits_indexes[(num_qubits - operator_index - 1)])

        # Apply Barriers to the interval of Qubits
        self.quantum_circuit.apply_barriers_interval(self.qubits_indexes)

        # Return the IBM Qiskit's W State, as a multipartite entanglement
        return self.quantum_circuit

    # Measure the multipartite entanglement for the W State configured
    def measure_multipartite_entanglement(self, is_final_measurement=True):

        # Compute the number of Qubits of the W State
        num_qubits = len(self.qubits_indexes)

        # Set the Bits for the measurement of the Qubits, respectively
        bits_indexes = self.qubits_indexes

        # Apply Barriers to the interval of Qubits
        self.quantum_circuit.apply_barriers_interval(self.qubits_indexes)

        # For each Operator's Index, with exception of the last one
        for operator_index in range(num_qubits - 1):

            # Apply the Controlled-X Gate, regarding the Qubit of the current Operator's Index and the next one,
            # as the Control-Qubit and Target-Qubit, respectively
            self.quantum_circuit.apply_controlled_x(self.qubits_indexes[operator_index],
                                                    self.qubits_indexes[(operator_index + 1)])

        # For each Operator's Index, with exception of the last one
        for operator_index in range(num_qubits - 1):

            # Compute the theta angle of the arc-cosine, for the current Operator's Index, plus two indexes
            theta = arccos(sqrt(1 / (operator_index + 2)))

            # Apply a Barrier, to the Qubit of the current Operator's Index, plus one index
            self.quantum_circuit.apply_barrier(self.qubits_indexes[(operator_index + 1)])

            # Apply the Ry Gate, regarding the theta angle and the current Operator's Index
            self.quantum_circuit.apply_ry(-theta, self.qubits_indexes[operator_index])

            # Apply the Controlled-Z Gate, regarding the Qubit of the next Operator's Index and the current one,
            # as the Control-Qubit and Target-Qubit, respectively
            self.quantum_circuit.apply_controlled_z(self.qubits_indexes[(operator_index + 1)],
                                                    self.qubits_indexes[operator_index])

            # Apply the Ry Gate, regarding the theta angle and the current Operator's Index,
            self.quantum_circuit.apply_ry(theta, self.qubits_indexes[operator_index])

        # Apply the Pauli-X Gate to the last Qubit index
        self.quantum_circuit.apply_pauli_x(self.qubits_indexes[(num_qubits - 1)])

        # Apply Barriers to the interval of Qubits
        self.quantum_circuit.apply_barriers_interval(self.qubits_indexes)

        # If is a final measurement
        if is_final_measurement:

            # Measure the Qubits of the Quantum Circuit, for the W State
            self.quantum_circuit.measure_qubits_interval(self.qubits_indexes,
                                                         bits_indexes)

        # Return the IBM Qiskit's W State, as a multipartite entanglement
        return self.quantum_circuit
