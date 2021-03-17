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

POSSIBLE_CONFIGURATIONS_BELL_STATES = ["EPR_PAIR_STATE", "BELL_STATE_PHI_PLUS", "BELL_STATE_PHI_MINUS",
                                       "BELL_STATE_PSI_PLUS", "BELL_STATE_PSI_MINUS"]


# Class for IBM Qiskit's Bell State
class QiskitBellState:

    # Constructor for IBM Qiskit's Bell State
    def __init__(self, name, bell_state_type, quantum_circuit, control_qubit_index, target_qubit_index):
        self.name = name
        self.bell_state_type = bell_state_type.upper()
        self.quantum_circuit = quantum_circuit
        self.control_qubit_index = control_qubit_index
        self.target_qubit_index = target_qubit_index

        # The number of Qubits of the given IBM Qiskit's Quantum Circuit
        num_qubits_quantum_circuit = quantum_circuit.get_num_qubits()

        # If the number of Qubits of the given IBM Qiskit's Quantum Circuit is strictly lower than 2,
        # a Value Error exception will be raised
        if num_qubits_quantum_circuit < 2:

            # Raise the Value Error exception
            raise ValueError("It is impossible to create a Bell State, from a IBM Qiskit's Quantum Circuit with "
                             "less than 2 Qubits!!!")

        # If the configuration given for the Bell State is not valid
        if self.bell_state_type not in POSSIBLE_CONFIGURATIONS_BELL_STATES:

            # Raise the Value Error exception
            raise ValueError("The configuration for the Bell State is not valid!!!")

    # Prepare the bipartite entanglement for the Bell State configured
    def prepare_bipartite_entanglement(self):

        # If the Bell State is |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
        if self.bell_state_type == "EPR_PAIR_STATE" or self.bell_state_type == "BELL_STATE_PHI_PLUS":

            # Apply the Hadamard Gate to the Control-Qubit index
            self.quantum_circuit.apply_hadamard(self.control_qubit_index)

            # Apply the Controlled-Pauli-X (CNOT) Gate to the given Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_controlled_x(self.control_qubit_index, self.target_qubit_index)

            # Apply Barriers to the interval of Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_barriers_interval([self.control_qubit_index, self.target_qubit_index])

        # If the Bell State is |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
        elif self.bell_state_type == "BELL_STATE_PHI_MINUS":

            # Apply the Hadamard Gate to the Control-Qubit index
            self.quantum_circuit.apply_hadamard(self.control_qubit_index)

            # Apply the Pauli-Z (Phase Flip) to the Control-Qubit index
            self.quantum_circuit.apply_pauli_z(self.control_qubit_index)

            # Apply the Controlled-Pauli-X (CNOT) Gate to the given Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_controlled_x(self.control_qubit_index, self.target_qubit_index)

            # Apply Barriers to the interval of Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_barriers_interval([self.control_qubit_index, self.target_qubit_index])

        # If the Bell State is |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
        elif self.bell_state_type == "BELL_STATE_PSI_PLUS":

            # Apply the Hadamard Gate to the Control-Qubit index
            self.quantum_circuit.apply_hadamard(self.control_qubit_index)

            # Apply the Pauli-X (NOT/Bit Flip) Gate to the Target-Qubit index
            self.quantum_circuit.apply_pauli_x(self.target_qubit_index)

            # Apply the Controlled-Pauli-X (CNOT) Gate to the given Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_controlled_x(self.control_qubit_index, self.target_qubit_index)

            # Apply Barriers to the interval of Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_barriers_interval([self.control_qubit_index, self.target_qubit_index])

        # If the Bell State is |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
        elif self.bell_state_type == "BELL_STATE_PSI_MINUS":

            # Apply the Hadamard Gate to the Control-Qubit index
            self.quantum_circuit.apply_hadamard(self.control_qubit_index)

            # Apply the Pauli-X (NOT/Bit Flip) Gate to the Target-Qubit index
            self.quantum_circuit.apply_pauli_x(self.target_qubit_index)

            # Apply the Controlled-Pauli-X (CNOT) Gate to the given Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_controlled_x(self.control_qubit_index, self.target_qubit_index)

            # Apply the Pauli-Z (Phase Flip) Gate to the Target-Qubit index
            self.quantum_circuit.apply_pauli_z(self.target_qubit_index)

            # Apply Barriers to the interval of Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_barriers_interval([self.control_qubit_index, self.target_qubit_index])

        # Return the IBM Qiskit's Bell State, as a bipartite entanglement
        return self.quantum_circuit

    # Measure the bipartite entanglement for the Bell State configured
    def measure_bipartite_entanglement(self, is_final_measurement=True):

        # Set the Control-Bit and Target-Bit,
        # for the measurement of the Control-Qubit and Target-Qubit, respectively
        control_bit_index, target_bit_index = self.control_qubit_index, self.target_qubit_index

        # If the Bell State is |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
        if self.bell_state_type == "EPR_PAIR_STATE" or self.bell_state_type == "BELL_STATE_PHI_PLUS":

            # Apply Barriers to the interval of Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_barriers_interval([self.control_qubit_index, self.target_qubit_index])

            # Apply the Controlled-Pauli-X (CNOT) Gate to the given Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_controlled_x(self.control_qubit_index, self.target_qubit_index)

            # Apply the Hadamard Gate to the Control-Qubit index
            self.quantum_circuit.apply_hadamard(self.control_qubit_index)

            # If is a final measurement
            if is_final_measurement:

                # Measure the Control-Qubit and Target-Qubit of the Quantum Circuit, for the Bell State
                self.quantum_circuit.measure_qubits_interval([self.control_qubit_index, self.target_qubit_index],
                                                             [control_bit_index, target_bit_index])

        # If the Bell State is |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
        elif self.bell_state_type == "BELL_STATE_PHI_MINUS":

            # Apply Barriers to the interval of Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_barriers_interval([self.control_qubit_index, self.target_qubit_index])

            # Apply the Controlled-Pauli-X (CNOT) Gate to the given Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_controlled_x(self.control_qubit_index, self.target_qubit_index)

            # Apply the Pauli-Z (Phase Flip) to the Control-Qubit index
            self.quantum_circuit.apply_pauli_z(self.control_qubit_index)

            # Apply the Hadamard Gate to the Control-Qubit index
            self.quantum_circuit.apply_hadamard(self.control_qubit_index)

            # If is a final measurement
            if is_final_measurement:

                # Measure the Control-Qubit and Target-Qubit of the Quantum Circuit, for the Bell State
                self.quantum_circuit.measure_qubits_interval([self.control_qubit_index, self.target_qubit_index],
                                                             [control_bit_index, target_bit_index])

        # If the Bell State is |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
        elif self.bell_state_type == "BELL_STATE_PSI_PLUS":

            # Apply Barriers to the interval of Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_barriers_interval([self.control_qubit_index, self.target_qubit_index])

            # Apply the Controlled-Pauli-X (CNOT) Gate to the given Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_controlled_x(self.control_qubit_index, self.target_qubit_index)

            # Apply the Pauli-X (NOT/Bit Flip) Gate to the Target-Qubit index
            self.quantum_circuit.apply_pauli_x(self.target_qubit_index)

            # Apply the Hadamard Gate to the Control-Qubit index
            self.quantum_circuit.apply_hadamard(self.control_qubit_index)

            # If is a final measurement
            if is_final_measurement:

                # Measure the Control-Qubit and Target-Qubit of the Quantum Circuit, for the Bell State
                self.quantum_circuit.measure_qubits_interval([self.control_qubit_index, self.target_qubit_index],
                                                             [control_bit_index, target_bit_index])

        # If the Bell State is |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
        elif self.bell_state_type == "BELL_STATE_PSI_MINUS":

            # Apply Barriers to the interval of Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_barriers_interval([self.control_qubit_index, self.target_qubit_index])

            # Apply the Pauli-Z (Phase Flip) Gate to the Target-Qubit index
            self.quantum_circuit.apply_pauli_z(self.target_qubit_index)

            # Apply the Controlled-Pauli-X (CNOT) Gate to the given Control-Qubit and Target-Qubit
            self.quantum_circuit.apply_controlled_x(self.control_qubit_index, self.target_qubit_index)

            # Apply the Pauli-X (NOT/Bit Flip) Gate to the Target-Qubit index
            self.quantum_circuit.apply_pauli_x(self.target_qubit_index)

            # Apply the Hadamard Gate to the Control-Qubit index
            self.quantum_circuit.apply_hadamard(self.control_qubit_index)

            # If is a final measurement
            if is_final_measurement:

                # Measure the Control-Qubit and Target-Qubit of the Quantum Circuit, for the Bell State
                self.quantum_circuit.measure_qubits_interval([self.control_qubit_index, self.target_qubit_index],
                                                             [control_bit_index, target_bit_index])

        # Return the IBM Qiskit's Bell State, as a bipartite entanglement
        return self.quantum_circuit
