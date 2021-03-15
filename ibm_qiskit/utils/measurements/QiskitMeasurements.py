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


# Class for the IBM Qiskit's Measurements
class QiskitMeasurements:

    def __init__(self, name, quantum_circuit, is_final_measurement=True):
        self.name = name
        self.quantum_circuit = quantum_circuit
        self.is_final_measurement = is_final_measurement

    # Measure all the Qubits in the X-Basis
    def measure_all_qubits_in_x_basis(self):

        # For each indexed Qubit
        for qubit_index in range(self.quantum_circuit.get_number_qubits()):

            # Apply a Barrier to the current Qubit index, to ensure the previous operations were all performed
            self.quantum_circuit.apply_barrier(qubit_index)

            # Apply the Hadamard Gate to the current Qubit index, to prepare it in the X-Basis
            self.quantum_circuit.apply_hadamard(qubit_index)

        # If it is the final measurement, measure all the Qubits in the X-Basis
        if self.is_final_measurement:

            # Measure all Qubits to their respective Bits
            self.quantum_circuit.measure_all_qubits()

        # Return the Quantum Circuit with all the Qubits prepared/measured in the X-Basis
        return self.quantum_circuit

    # Measure all the Qubits in the Y-Basis
    def measure_all_qubits_in_y_basis(self):

        # For each indexed Qubit
        for qubit_index in range(self.quantum_circuit.get_number_qubits()):

            # Apply a Barrier to the current Qubit index, to ensure the previous operations were all performed
            self.quantum_circuit.apply_barrier(qubit_index)

            # Apply the Hadamard Gate to the current Qubit index, to prepare it in the X-Basis
            self.quantum_circuit.apply_hadamard(qubit_index)

            # Apply, then, the Phase S to the current Qubit index, to, finally, prepare it in the Y-Basis
            self.quantum_circuit.apply_phase_s(qubit_index)

        # If it is the final measurement, measure all the Qubits in the Y-Basis
        if self.is_final_measurement:

            # Measure all Qubits to their respective Bits
            self.quantum_circuit.measure_all_qubits()

        # Return the Quantum Circuit with all the Qubits prepared/measured in the Y-Basis
        return self.quantum_circuit

    # Measure all the Qubits in the Y-Basis
    def measure_all_qubits_in_z_basis(self):

        # For each indexed Qubit
        for qubit_index in range(self.quantum_circuit.get_number_qubits()):

            # Apply a Barrier to the current Qubit index, to ensure the previous operations were all performed
            self.quantum_circuit.apply_barrier(qubit_index)

            # Apply the Pauli-I Gate to the current Qubit index,
            # to prepare it in the Z-Basis (i.e., the Standard Measurement)
            self.quantum_circuit.apply_pauli_i(qubit_index)

        # If it is the final measurement, measure all the Qubits in the Z-Basis
        if self.is_final_measurement:

            # Measure all Qubits to their respective Bits
            self.quantum_circuit.measure_all_qubits()

        # Return the Quantum Circuit with all the Qubits prepared/measured in the Z-Basis
        return self.quantum_circuit
