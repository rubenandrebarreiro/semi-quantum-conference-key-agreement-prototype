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
    def __init__(self, party_name, master_status):

        # Set the Party's name
        self.party_name = party_name

        # Set the boolean flag, responsible to keep the information about if the Party is
        # the Master of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol or not
        self.master_status = master_status

    # Return the boolean flag, responsible to keep the information about if the Party is
    # the Master of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol or not
    def is_master(self):

        return self.master_status

    # Prepare a Bipartite or Multipartite Quantum Entanglement
    def prepare_quantum_entanglement(self, quantum_entanglement_type, num_parties, quantum_circuit,
                                     bell_state_type=None):

        # If the Party is not the Master of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if not self.master_status:

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

                    # TODO - Handle this situation
                    return

                # If the Quantum Entanglement to prepare is a Graph State
                elif quantum_entanglement_type.upper() == "GRAPH_STATE":

                    # TODO - Handle this situation
                    return

            # If the specified type of Quantum Entanglement is not one of the possible configurations for
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            else:

                # Raise a Value Error
                raise ValueError("The Quantum Entanglement specified for the Protocol is not possible to use!!!")
