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

# Import the possible Bipartite and Multipartite Quantum Entanglement Types and
# the Possible Configurations for Bell States
from src.ibm_qiskit.common.QuantumEntanglementTypes \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES, POSSIBLE_CONFIGURATIONS_BELL_STATES

# Import QiskitBellState from IBM_Qiskit.Entanglements.Bipartite
from src.ibm_qiskit.entanglements.bipartite import QiskitBellState

# Import QiskitGHZState from IBM_Qiskit.Entanglements.Multipartite
from src.ibm_qiskit.entanglements.multipartite import QiskitGHZState

# Import QiskitWState from IBM_Qiskit.Entanglements.Multipartite
from src.ibm_qiskit.entanglements.multipartite import QiskitWState

# Import QiskitGraphState from IBM_Qiskit.Entanglements.Multipartite.Resource_States
from src.ibm_qiskit.entanglements.multipartite.resource_states import QiskitGraphState


# Class for IBM Qiskit's Party for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocolParty:

    # Constructor for IBM Qiskit's Party for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def __init__(self, party_id, party_name, master_status_flag, bipartite_pre_shared_keys):

        # Set the Party's ID
        self.party_id = party_id

        # Set the Party's name
        self.party_name = party_name

        # Set the boolean flag, responsible to keep the information about if the Party is
        # the Master of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol or not
        self.master_status_flag = master_status_flag

        # Set the Pre-Shared Key, previously established between the parties
        self.bipartite_pre_shared_keys = bipartite_pre_shared_keys

    # Return the boolean flag, responsible to keep the information about if the Party is
    # the Master of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol or not
    def is_master(self):

        return self.master_status_flag

    # Prepare a Bipartite or Multipartite Quantum Entanglement
    def prepare_quantum_entanglement(self, quantum_entanglement_type, num_parties, quantum_circuit,
                                     bell_state_type=None, qubits_edges_indexes_for_resource_state=None):

        # If the Party is not the Master of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if not self.master_status_flag:

            # Raise the Value Error exception
            raise ValueError("The Party Name specified to be the Master "
                             "(i.e., the party responsible for the distribution of the Common Secret Key "
                             "(Conference Key) between the parties involved is not present in "
                             "the list of Parties' Names involved!!!")

        # If the Party is the Master of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # If the specified type of Quantum Entanglement is one of the possible configurations for
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            if quantum_entanglement_type.upper() in POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES:

                # If the Quantum Entanglement to prepare is a Bell State
                if quantum_entanglement_type.upper() == "BELL_STATE":

                    # If the number of parties involved is higher than 2
                    if num_parties > 2:

                        # If the configuration of the Bell State is specified
                        if bell_state_type is not None:

                            # If the configuration of the Bell State is possible
                            if bell_state_type in POSSIBLE_CONFIGURATIONS_BELL_STATES:

                                # If the Bipartite Entangled State is Bell State (EPR Pair):
                                # - |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
                                if (bell_state_type == "EPR_PAIR_STATE") or (bell_state_type == "BELL_STATE_PHI_PLUS"):

                                    # Prepare the EPR Pair (Bell State) for 2 Qubits
                                    qiskit_quantum_circuit_epr_pair_bell_state_phi_plus = QiskitBellState \
                                        .QiskitBellState("bell_state_phi_plus_epr_pair",
                                                         "BELL_STATE_PHI_PLUS",
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Return the EPR Pair (Bell State) for 2 Qubits
                                    return qiskit_quantum_circuit_epr_pair_bell_state_phi_plus

                                # If the Bipartite Entangled State is Bell State:
                                # - |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
                                elif bell_state_type == "BELL_STATE_PHI_MINUS":

                                    # Prepare the Bell State: |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
                                    qiskit_quantum_circuit_bell_state_phi_minus = QiskitBellState \
                                        .QiskitBellState("bell_state_phi_minus",
                                                         "BELL_STATE_PHI_MINUS",
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Return the Bell State for 2 Qubits
                                    return qiskit_quantum_circuit_bell_state_phi_minus

                                # If the Bipartite Entangled State is Bell State:
                                # - |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
                                elif bell_state_type == "BELL_STATE_PSI_PLUS":

                                    # Prepare the Bell State: |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
                                    qiskit_quantum_circuit_bell_state_psi_plus = QiskitBellState \
                                        .QiskitBellState("bell_state_psi_plus",
                                                         "BELL_STATE_PSI_PLUS",
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Return the Bell State for 2 Qubits
                                    return qiskit_quantum_circuit_bell_state_psi_plus

                                # If the Bipartite Entangled State is Bell State:
                                # - |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
                                elif bell_state_type == "BELL_STATE_PSI_MINUS":

                                    # Prepare the Bell State: |ψ^+-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
                                    qiskit_quantum_circuit_bell_state_psi_minus = QiskitBellState \
                                        .QiskitBellState("bell_state_psi_minus",
                                                         "BELL_STATE_PSI_MINUS",
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Return the Bell State for 2 Qubits
                                    return qiskit_quantum_circuit_bell_state_psi_minus

                            # If the configuration of the Bell State is not possible
                            else:

                                # Raise a Value Error
                                raise ValueError("The configuration of the Bell State specified is not possible!!!")

                        # If the configuration of the Bell State is not specified
                        else:

                            # Raise a Value Error
                            raise ValueError("The configuration of the Bell State is not specified!!!")

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use GHZ States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 3 Parties!!!")

                # If the Quantum Entanglement to prepare is a GHZ State
                elif quantum_entanglement_type.upper() == "GHZ_STATE":

                    # If the number of parties involved is higher than 2
                    if num_parties > 2:

                        # Set the Control-Qubit
                        control_qubit_index = 0

                        # Set the list of Target-Qubits
                        target_qubits_indexes = list(range(1, num_parties))

                        # Prepare the GHZ State, for multiple Qubits
                        qiskit_quantum_circuit_ghz_state = QiskitGHZState \
                            .QiskitGHZState("ghz_state_qubits",
                                            quantum_circuit,
                                            control_qubit_index, target_qubits_indexes)\
                            .prepare_multipartite_entanglement()

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use GHZ States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 3 Parties!!!")

                    # Return the Quantum Circuit for the GHZ State for n parties
                    return qiskit_quantum_circuit_ghz_state

                # If the Quantum Entanglement to prepare is a W State
                elif quantum_entanglement_type.upper() == "W_STATE":

                    # If the number of parties involved is higher than 2
                    if num_parties > 2:

                        # Set the list of Qubits
                        qubits_indexes = list(range(0, num_parties))

                        # Prepare the W State, for multiple Qubits
                        qiskit_quantum_circuit_w_state = QiskitWState \
                            .QiskitWState("w_state_qubits",
                                          quantum_circuit,
                                          qubits_indexes)\
                            .prepare_multipartite_entanglement()

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use W States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 3 Parties!!!")

                    # Return the Quantum Circuit for the W State for n parties
                    return qiskit_quantum_circuit_w_state

                # If the Quantum Entanglement to prepare is a Resource State
                elif quantum_entanglement_type.upper() == "RESOURCE_STATE":

                    # If the number of parties involved is higher than 1
                    if num_parties > 1:

                        # Set the list of Qubits
                        qubits_indexes = list(range(0, num_parties))

                        # Prepare the Resource State, as a Graph State by default, for multiple Qubits
                        qiskit_quantum_circuit_resource_state = QiskitGraphState \
                            .QiskitGraphState("resource_state_qubits",
                                              quantum_circuit,
                                              qubits_indexes,
                                              qubits_edges_indexes_for_resource_state)\
                            .prepare_multipartite_entanglement()

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use Resource States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 2 Parties!!!")

                    # Return the Quantum Circuit for the Resource State for n parties
                    return qiskit_quantum_circuit_resource_state

                # If the Quantum Entanglement to prepare is a Graph State
                elif quantum_entanglement_type.upper() == "GRAPH_STATE":

                    # If the number of parties involved is higher than 1
                    if num_parties > 1:

                        # Set the list of Qubits
                        qubits_indexes = list(range(0, num_parties))

                        # Prepare the Resource State, as a Graph State by default, for multiple Qubits
                        qiskit_quantum_circuit_graph_state = QiskitGraphState \
                            .QiskitGraphState("graph_state_qubits",
                                              quantum_circuit,
                                              qubits_indexes,
                                              qubits_edges_indexes_for_resource_state)\
                            .prepare_multipartite_entanglement()

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use Graph States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 2 Parties!!!")

                    # Return the Quantum Circuit for the Graph State for n parties
                    return qiskit_quantum_circuit_graph_state

                # If the Quantum Entanglement to prepare is a Cluster State
                elif quantum_entanglement_type.upper() == "CLUSTER_STATE":

                    # TODO - Handle this situation
                    return

            # If the specified type of Quantum Entanglement is not one of the possible configurations for
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            else:

                # Raise a Value Error
                raise ValueError("The Quantum Entanglement specified for the Protocol is not possible to use!!!")

    # Measure and Resend the Qubit, or just Reflect it, according to the Pre-Shared Key
    def measure_and_resend_or_reflect_qubit(self, quantum_circuit, num_round, timestamp):

        # If the Party is not the Master of the Protocol and the Party possesses only
        # one Pre-Shared Key between itself and the Master of the Protocol
        if (not self.master_status_flag) and (len(self.bipartite_pre_shared_keys) == 1):

            # Retrieve the bipartite Pre-Shared Key, with the Master of the Protocol
            pre_shared_key_bits = self.bipartite_pre_shared_keys[0][1]

            # It is a SIFT Round, thus, the Normal Party, will Measure and Resend the Qubit
            # back again to the Master of the Protocol (more probable)
            if pre_shared_key_bits[num_round] == 0:

                # Prepare and Measure the Qubit in the Z-Basis (Computational Basis),
                # according to the Party's ID
                quantum_circuit.prepare_measure_single_qubit_in_z_basis((self.party_id - 1),
                                                                        (self.party_id - 1),
                                                                        is_final_measurement=True)

            # It is a CTRL Round, thus, the Normal Party, will just Reflect the Qubit,
            # to the Master of the Protocol, without measure it (less probable)
            elif pre_shared_key_bits[num_round] == 1:

                # Apply the Pauli-I to the Qubit,
                # according to the Party's ID
                quantum_circuit.apply_pauli_i(self.party_id - 1)

        # If the Party is the Master of the Protocol and the Party possesses
        # all the bipartite Pre-Shared Keys between itself and the other PARTIES
        else:

            # Raise the Value Error exception
            raise ValueError("The Master Party cannot Measure and Resend (SIFT Rounds) or "
                             "just Reflect the Qubits (CTRL Rounds)!!!")
