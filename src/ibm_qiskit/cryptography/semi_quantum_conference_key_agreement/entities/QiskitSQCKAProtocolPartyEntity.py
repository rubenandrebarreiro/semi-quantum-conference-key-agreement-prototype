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

# Import Enumerations and Constants
from qiskit import Aer, execute

from src.common.enumerations.SemiQuantumCryptographyProtocolPartyEntityTypes \
    import POSSIBLE_SEMI_QUANTUM_CRYPTOGRAPHY_PROTOCOL_PARTY_ENTITY_TYPES, \
    QUANTUM_PARTY_ENTITY, SEMI_QUANTUM_PARTY_ENTITY

# Import the possible Bipartite and Multipartite Quantum Entanglement Types and
# the Possible Configurations for Bell States
from src.common.enumerations.QuantumEntanglementTypes \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES, POSSIBLE_CONFIGURATIONS_BELL_STATES, \
    BELL_STATE, EPR_PAIR_STATE, BELL_STATE_PHI_PLUS, BELL_STATE_PHI_MINUS, BELL_STATE_PSI_PLUS, BELL_STATE_PSI_MINUS,\
    GHZ_STATE, W_STATE, DICKE_STATE, RESOURCE_STATE, GRAPH_STATE, CLUSTER_STATE

# TODO
from src.common.enumerations.SemiQuantumCryptographyProtocolRoundTypes \
    import SIFT_MEASURE_AND_RESEND_ROUND_BIT, CTRL_REFLECT_ROUND_BIT, \
    SIFT_MEASURE_AND_RESEND_ROUND_3, CTRL_REFLECT_ROUND_3

# Import Packages and Libraries

# Import QiskitBellState from IBM_Qiskit.Entanglements.Bipartite
from src.ibm_qiskit.circuit import QiskitQuantumCircuit
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreement.common import QiskitSQCKAProtocolRound
from src.ibm_qiskit.entanglements.bipartite import QiskitBellState

# Import QiskitGHZState from IBM_Qiskit.Entanglements.Multipartite
from src.ibm_qiskit.entanglements.multipartite import QiskitGHZState

# Import QiskitWState from IBM_Qiskit.Entanglements.Multipartite
from src.ibm_qiskit.entanglements.multipartite import QiskitWState

# Import QiskitGraphState from IBM_Qiskit.Entanglements.Multipartite.Resource_States
from src.ibm_qiskit.entanglements.multipartite.resource_states import QiskitGraphState


# Constants

# The number of counts for simulation
NUM_COUNTS_FOR_SIMULATION = 1000


# Class of the IBM Qiskit's Party Entity for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocolPartyEntity:

    # Constructor of the IBM Qiskit's Party Entity for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def __init__(self, party_entity_id, party_user_client, resources_context, distributor_status_flag, bipartite_pre_shared_keys):

        # If the Resources' Context for the IBM Qiskit's Party Entity for
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol is valid
        if resources_context.upper() in POSSIBLE_SEMI_QUANTUM_CRYPTOGRAPHY_PROTOCOL_PARTY_ENTITY_TYPES:

            # Set the 1st possible validation condition for configuration of Resources' Context for
            # the IBM Qiskit's Party Entity for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            boolean_validation_1 = \
                (distributor_status_flag and (resources_context.upper() == QUANTUM_PARTY_ENTITY))

            # Set the 2nd possible validation condition for configuration of Resources' Context for
            # the IBM Qiskit's Party Entity for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            boolean_validation_2 = \
                (not distributor_status_flag and (resources_context.upper() == SEMI_QUANTUM_PARTY_ENTITY))

            # If the configuration of the Resources' Context for the IBM Qiskit's Party Entity for
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol is valid
            if boolean_validation_1 or boolean_validation_2:

                # Set the ID for the IBM Qiskit's Party Entity for
                # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                self.party_entity_id = party_entity_id

                # Set the User/Client for the IBM Qiskit's Party Entity for
                # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                self.party_user_client = party_user_client

                # Set the Resources' Context of the IBM Qiskit's Party Entity for
                # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                self.resources_context = resources_context.lower()

                # Set the boolean flag, responsible to keep the information about if the Party Entity is
                # the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol or not
                self.distributor_status_flag = distributor_status_flag

                # Set the Pre-Shared Key, previously established between the Party Entities
                self.bipartite_pre_shared_keys = bipartite_pre_shared_keys

            # If the configuration of the Resources' Context for
            # the IBM Qiskit's Party Entity for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol is not valid
            else:

                # If the Party Entity is set to be the Distributor of
                # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                if distributor_status_flag:

                    # Raise a Runtime Error
                    raise RuntimeError("The Distributor the Semi-Quantum Conference Key Agreement (SQCKA) Protocol "
                                       "should only have Quantum Resources!!!")

                # If the Party Entity is not set to be the Distributor of
                # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                else:

                    # Raise a Runtime Error
                    raise RuntimeError("A Receiver Party Entity of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol "
                                       "should only have Semi-Quantum Resources!!!")

        # If the Resources' Context for the IBM Qiskit's Party Entity for
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol is not valid
        else:

            # Raise a Runtime Error
            raise RuntimeError("The Resources' Context for this Party Entity is not valid!!!")

    # Return the ID for the IBM Qiskit's Party Entity for
    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def get_party_entity_id(self):
        return self.party_entity_id

    # Return the User/Client for the IBM Qiskit's Party Entity for
    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def get_party_user_client(self):
        return self.party_user_client

    # Return the Resources' Context of the IBM Qiskit's Party Entity for
    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def get_resources_context(self):
        return self.resources_context

    # Retrieve the boolean flag, responsible to keep the information about if the Party Entity is
    # the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol or not
    def is_distributor(self):
        return self.distributor_status_flag

    # Return the Bipartite Pre-Shared Keys that the Party Entity possesses with other Parties
    def get_bipartite_pre_shared_keys(self):
        return self.bipartite_pre_shared_keys

    # Print the information about
    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Party Entity
    def print_info(self):

        # Some prints to draw a top left-side corner
        print(" __")
        print("|")
        print("|")

        # Print the ID of the User/Client of the Party Entity involved on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        print(" - Party Entity's ID: {}".format(self.party_entity_id))

        # Print the UUID of the User/Client of the Party Entity involved on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        print(" - Party Entity's User/Client's UUID: {}".format(self.get_party_user_client().get_user_client_uuid()))

        # Print the Name of the User/Client of the Party Entity involved on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        print(" - Party Entity's User/Client's Name: {}".format(self.get_party_user_client().get_user_client_name()))

        # Print the Resources' Context of the IBM Qiskit's Party Entity for
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        print(" - Party Entity's Resources' Context: {}".format(self.get_resources_context()))

        # Print the Distributor status of the Party Entity involved on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        print(" - Party Entity's Distributor Status: {}".format(self.is_distributor()))

        # Retrieve the Bipartite Pre-Shared Keys owned/possessed by the Party involved on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        bipartite_pre_shared_keys = self.get_bipartite_pre_shared_keys()

        # If the Party Entity is the Distributor of
        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if self.is_distributor() and (self.get_resources_context().lower() == QUANTUM_PARTY_ENTITY.lower()):

            # Retrieve the number of the Bipartite Pre-Shared Keys
            # owned/possessed by the Party Entity involved on
            # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            num_bipartite_pre_shared_keys = len(bipartite_pre_shared_keys)

            # Print the header of the Bipartite Pre-Shared Keys
            # owned/possessed by the Party Entity involved on
            # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            print("\n\n - {} Bipartite Pre-Shared Key(s) owned:\n".format(num_bipartite_pre_shared_keys))

            # For each Bipartite Pre-Shared Keys owned/possessed by the Party Entity involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            for current_num_bipartite_pre_shared_key in range(num_bipartite_pre_shared_keys):

                # Print the information about the current Bipartite Pre-Shared Keys
                # owned/possessed by the Party Entity involved on the
                # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                print("   [{}]".format((current_num_bipartite_pre_shared_key + 1)), end='')
                bipartite_pre_shared_keys[current_num_bipartite_pre_shared_key].print_info()

        # If the Party Entity is not the Distributor of
        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Initialise the number of the Bipartite Pre-Shared Keys
            # owned/possessed by the Party Entity involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            num_bipartite_pre_shared_keys = 1

            # Retrieve the Bipartite Pre-Shared Key owned/possessed by the Party Entity involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol, as single instance
            bipartite_pre_shared_key = bipartite_pre_shared_keys

            # Print the header of the Bipartite Pre-Shared Keys owned/possessed by the Party Entity
            # involved on the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            print("\n\n - {} Bipartite Pre-Shared Key(s) owned:\n".format(num_bipartite_pre_shared_keys))

            # Print the information about the current Bipartite Pre-Shared Keys
            # owned/possessed by the Party Entity involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            print("   [{}]".format(num_bipartite_pre_shared_keys), end='')
            bipartite_pre_shared_key.print_info()

        # Some prints to draw a bottom left-side corner
        print("|")
        print("|__")

    # Create the Round for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def create_protocol_round(self, num_round, num_qubits_and_bits_for_quantum_circuit):

        # If the Party is the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if self.is_distributor() and (self.get_resources_context().lower() == QUANTUM_PARTY_ENTITY.lower()):

            # Retrieve the Bipartite Pre-Shared Keys of the Distributor of
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            bipartite_pre_shared_keys = self.get_bipartite_pre_shared_keys()

            # Retrieve the bit of the Pre-Shared Key, corresponding to the current round
            round_type_bit = bipartite_pre_shared_keys[0].get_bipartite_pre_shared_key()[num_round]  # TODO

            # If the bit of the Pre-Shared Key, corresponding to the current round is zero
            # (i.e., a SIFT / Measure and Resend Round)
            if int(round_type_bit) == SIFT_MEASURE_AND_RESEND_ROUND_BIT:

                # Set the ID of the SIFT / Measure and Resend Round
                round_type_id = SIFT_MEASURE_AND_RESEND_ROUND_3

            # If the bit of the Pre-Shared Key, corresponding to the current round is zero
            # (i.e., a CTRL / Reflect Round)
            else:

                # Set the ID of the CTRL / Reflect Round
                round_type_id = CTRL_REFLECT_ROUND_3

            # Creation of the IBM Qiskit's Quantum Register
            qiskit_quantum_register_sqcka_protocol_round = \
                QiskitQuantumRegister.QiskitQuantumRegister("qrsqckaround{}".format(num_round),
                                                            num_qubits_and_bits_for_quantum_circuit)

            # Creation of the IBM Qiskit's Classical Register
            qiskit_classical_register_sqcka_protocol_round = \
                QiskitClassicalRegister.QiskitClassicalRegister("crsqckaround{}".format(num_round),
                                                                num_qubits_and_bits_for_quantum_circuit)

            # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
            qiskit_quantum_circuit_sqcka_protocol_round = \
                QiskitQuantumCircuit.QiskitQuantumCircuit("qcsqckaround{}".format(num_round),
                                                          qiskit_quantum_register_sqcka_protocol_round,
                                                          qiskit_classical_register_sqcka_protocol_round,
                                                          global_phase=0)

            # Create the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            qiskit_sqcka_protocol_round = \
                QiskitSQCKAProtocolRound\
                .QiskitSQCKAProtocolRound(num_round, round_type_id,
                                          qiskit_quantum_circuit_sqcka_protocol_round)

            # Return the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            return qiskit_sqcka_protocol_round

        # If the Party is not the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Raise the Runtime Error exception
            raise RuntimeError("Only the Distributor Party Entity can create "
                               "the Rounds for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol!!!")

    # Prepare a Bipartite or Multipartite Quantum Entanglement
    def prepare_quantum_entanglement(self, quantum_entanglement_type, num_parties, protocol_round,
                                     bell_state_type=None, qubits_edges_indexes_for_resource_state=None):

        # If the Party is the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if self.is_distributor() and (self.get_resources_context().lower() == QUANTUM_PARTY_ENTITY.lower()):

            # If the specified type of Quantum Entanglement is one of the possible configurations for
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            if quantum_entanglement_type.upper() in POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES:

                # Retrieve the Quantum Circuit of the Protocol Round
                quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

                # If the Quantum Entanglement to prepare is a Bell State
                if quantum_entanglement_type.upper() == BELL_STATE:

                    # If the number of parties involved is higher than 2
                    if num_parties > 2:

                        # If the configuration of the Bell State is specified
                        if bell_state_type is not None:

                            # If the configuration of the Bell State is possible
                            if bell_state_type in POSSIBLE_CONFIGURATIONS_BELL_STATES:

                                # If the Bipartite Entangled State is Bell State (EPR Pair):
                                # - |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
                                if (bell_state_type == EPR_PAIR_STATE) or (bell_state_type == BELL_STATE_PHI_PLUS):

                                    # Prepare the EPR Pair (Bell State) for 2 Qubits
                                    qiskit_quantum_circuit_epr_pair_bell_state_phi_plus = QiskitBellState \
                                        .QiskitBellState((BELL_STATE_PHI_PLUS + "_" + EPR_PAIR_STATE).lower(),
                                                         BELL_STATE_PHI_PLUS,
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Update the Quantum Circuit for the EPR Pair (Bell State) for 2 Qubits, for the Protocol Round
                                    protocol_round.update_qiskit_quantum_circuit(qiskit_quantum_circuit_epr_pair_bell_state_phi_plus)

                                    # Return the Protocol Round updated
                                    return protocol_round

                                # If the Bipartite Entangled State is Bell State:
                                # - |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
                                elif bell_state_type == BELL_STATE_PHI_MINUS:

                                    # Prepare the Bell State: |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
                                    qiskit_quantum_circuit_bell_state_phi_minus = QiskitBellState \
                                        .QiskitBellState(BELL_STATE_PHI_MINUS.lower(),
                                                         BELL_STATE_PHI_MINUS,
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Update the Quantum Circuit for the Bell State for 2 Qubits, for the Protocol Round
                                    protocol_round.update_qiskit_quantum_circuit(qiskit_quantum_circuit_bell_state_phi_minus)

                                    # Return the Protocol Round updated
                                    return protocol_round

                                # If the Bipartite Entangled State is Bell State:
                                # - |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
                                elif bell_state_type == BELL_STATE_PSI_PLUS:

                                    # Prepare the Bell State: |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
                                    qiskit_quantum_circuit_bell_state_psi_plus = QiskitBellState \
                                        .QiskitBellState(BELL_STATE_PSI_PLUS.lower(),
                                                         BELL_STATE_PSI_PLUS,
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Update the Quantum Circuit for the Bell State for 2 Qubits, for the Protocol Round
                                    protocol_round.update_qiskit_quantum_circuit(qiskit_quantum_circuit_bell_state_psi_plus)

                                    # Return the Protocol Round updated
                                    return protocol_round

                                # If the Bipartite Entangled State is Bell State:
                                # - |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
                                elif bell_state_type == BELL_STATE_PSI_MINUS:

                                    # Prepare the Bell State: |ψ^+-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
                                    qiskit_quantum_circuit_bell_state_psi_minus = QiskitBellState \
                                        .QiskitBellState(BELL_STATE_PSI_MINUS.lower(),
                                                         BELL_STATE_PSI_MINUS,
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Update the Quantum Circuit for the Bell State for 2 Qubits, for the Protocol Round
                                    protocol_round.update_qiskit_quantum_circuit(qiskit_quantum_circuit_bell_state_psi_minus)

                                    # Return the Protocol Round updated
                                    return protocol_round

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
                elif quantum_entanglement_type.upper() == GHZ_STATE:

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
                                            control_qubit_index, target_qubits_indexes) \
                            .prepare_multipartite_entanglement()

                        # Update the Quantum Circuit for the GHZ State for n parties, for the Protocol Round
                        protocol_round.update_qiskit_quantum_circuit(qiskit_quantum_circuit_ghz_state)

                        # Return the Protocol Round updated
                        return protocol_round

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use GHZ States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 3 Parties!!!")

                # If the Quantum Entanglement to prepare is a W State
                elif quantum_entanglement_type.upper() == W_STATE:

                    # If the number of parties involved is higher than 2
                    if num_parties > 2:

                        # Set the list of Qubits
                        qubits_indexes = list(range(0, num_parties))

                        # Prepare the W State, for multiple Qubits
                        qiskit_quantum_circuit_w_state = QiskitWState \
                            .QiskitWState("w_state_qubits",
                                          quantum_circuit,
                                          qubits_indexes) \
                            .prepare_multipartite_entanglement()

                        # Update the Quantum Circuit for the W State for n parties, for the Protocol Round
                        protocol_round.update_qiskit_quantum_circuit(qiskit_quantum_circuit_w_state)

                        # Return the Protocol Round updated
                        return protocol_round

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use W States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 3 Parties!!!")

                # If the Quantum Entanglement to prepare is a Dicke State
                elif quantum_entanglement_type.upper() == DICKE_STATE:

                    # TODO - Handle this situation
                    return

                # If the Quantum Entanglement to prepare is a Resource State
                elif quantum_entanglement_type.upper() == RESOURCE_STATE:

                    # If the number of parties involved is higher than 1
                    if num_parties > 1:

                        # Set the list of Qubits
                        qubits_indexes = list(range(0, num_parties))

                        # Prepare the Resource State, as a Graph State by default, for multiple Qubits
                        qiskit_quantum_circuit_resource_state = QiskitGraphState \
                            .QiskitGraphState("resource_state_qubits",
                                              quantum_circuit,
                                              qubits_indexes,
                                              qubits_edges_indexes_for_resource_state) \
                            .prepare_multipartite_entanglement()

                        # Update the Quantum Circuit for the Resource State for n parties, for the Protocol Round
                        protocol_round.update_qiskit_quantum_circuit(qiskit_quantum_circuit_resource_state)

                        # Return the Protocol Round updated
                        return protocol_round

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use Resource States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 2 Parties!!!")

                # If the Quantum Entanglement to prepare is a Graph State
                elif quantum_entanglement_type.upper() == GRAPH_STATE:

                    # If the number of parties involved is higher than 1
                    if num_parties > 1:

                        # Set the list of Qubits
                        qubits_indexes = list(range(0, num_parties))

                        # Prepare the Resource State, as a Graph State by default, for multiple Qubits
                        qiskit_quantum_circuit_graph_state = QiskitGraphState \
                            .QiskitGraphState("graph_state_qubits",
                                              quantum_circuit,
                                              qubits_indexes,
                                              qubits_edges_indexes_for_resource_state) \
                            .prepare_multipartite_entanglement()

                        # Update the Quantum Circuit for the Graph State for n parties, for the Protocol Round
                        protocol_round.update_qiskit_quantum_circuit(qiskit_quantum_circuit_graph_state)

                        # Return the Protocol Round updated
                        return protocol_round

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use Graph States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 2 Parties!!!")

                # If the Quantum Entanglement to prepare is a Cluster State
                elif quantum_entanglement_type.upper() == CLUSTER_STATE:

                    # TODO - Handle this situation
                    return

            # If the specified type of Quantum Entanglement is not one of the possible configurations for
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            else:

                # Raise a Value Error
                raise ValueError("The Quantum Entanglement specified for the Protocol is not possible to use!!!")

        # If the Party is not the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Raise a Runtime Error
            raise RuntimeError("Only the Distributor Party Entity can prepare Quantum Entanglements!!!")

    # Send the Quantum Data/Information to the Semi-Quantum Party Entities,
    # over the Quantum Communication Channels
    def send_quantum_data_information_to_semi_quantum_party_entities(self, num_parties, protocol_round):

        # If the Party is the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if self.is_distributor() and (self.get_resources_context().lower() == QUANTUM_PARTY_ENTITY.lower()):

            # Retrieve the Quantum Circuit of the Protocol Round
            quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

            # For each Semi-Quantum Entity
            for current_num_semi_quantum_entities in range(1, num_parties):

                # Apply the Swap Gate, between the Qubits of the Distributor Party Entity and
                # the Qubits of the Quantum Communication Channel
                quantum_circuit.apply_swap(current_num_semi_quantum_entities,
                                           (num_parties + current_num_semi_quantum_entities - 1))

                # Apply Barriers to all the Qubits of the Quantum Circuit for
                # the Round of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                quantum_circuit.apply_barriers_to_all()

            # Update the Quantum Circuit of the Protocol Round
            protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

            # Return the Protocol Round updated
            return protocol_round

        # If the Party is not the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Raise a Runtime Error
            raise RuntimeError("Only the Distributor Party Entity can send the Quantum Data/Information, "
                               "over the Quantum Communication Channels!!!")

    # Receive the Quantum Data/Information from the Distributor, over the Quantum Communication Channels
    def receive_quantum_data_information_from_distributor(self, num_parties, protocol_round):

        # If the Party is not the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if not self.is_distributor() and \
                (self.get_resources_context().lower() == SEMI_QUANTUM_PARTY_ENTITY.lower()):

            # Retrieve the Quantum Circuit of the Protocol Round
            quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

            # Apply the Swap Gate, between the Qubits of the Distributor and
            # the Qubits of the Quantum Communication Channel
            quantum_circuit.apply_swap((num_parties + self.party_entity_id - 1),
                                       ((2 * num_parties) + self.party_entity_id - 2))

            # Apply Barriers to all the Qubits of the Quantum Circuit for
            # the Round of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            quantum_circuit.apply_barriers_to_all()

            # Update the Quantum Circuit of the Protocol Round
            protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

            # Return the Protocol Round updated
            return protocol_round

        # If the Party is the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Raise a Runtime Error
            raise RuntimeError("Only the Semi-Quantum Receiver Party Entities "
                               "can receive the Quantum Data/Information, "
                               "over the Quantum Communication Channels!!!")

    # Measure and Resend the Qubit, or just Reflect it, according to the Pre-Shared Key
    def measure_and_resend_or_reflect_qubit(self, num_parties, protocol_round):

        # If the Party is not the Distributor of the Protocol and the Party possesses only
        # one Pre-Shared Key between itself and the Distributor of the Protocol
        if (not self.is_distributor()) and \
                (self.get_resources_context().lower() == SEMI_QUANTUM_PARTY_ENTITY.lower()) and \
                (not isinstance(self.bipartite_pre_shared_keys, list)):

            # Retrieve the bipartite Pre-Shared Key, with the Distributor of the Protocol
            pre_shared_key_bits = self.bipartite_pre_shared_keys.get_bipartite_pre_shared_key()

            # Retrieve the number of the Protocol Round
            num_round = protocol_round.get_num_round()

            # Retrieve the Quantum Circuit of the Protocol Round
            quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

            # Compute the index of the Quantum Circuit,
            # according to the respective qubit and bit of the Semi-Quantum Party Entity
            qubit_bit_index = ((2 * num_parties) + self.party_entity_id - 2)

            # It is a SIFT Round, thus, the Semi-Quantum Entity Party, will Measure and Resend the Qubit
            # back again to the Distributor of the Protocol (more probable)
            if int(pre_shared_key_bits[num_round]) == SIFT_MEASURE_AND_RESEND_ROUND_BIT:

                # Print the information about the respective operation on the Qubit (Particle)
                print("{} measured the Qubit (Particle) received, in the Z-Basis (Computational Basis)!!!"
                      .format(self.get_party_user_client().get_user_client_name()))

                # Prepare and Measure the Qubit in the Z-Basis (Computational Basis),
                # according to the Party Entity's ID
                quantum_circuit.prepare_measure_single_qubit_in_z_basis(0, 0, qubit_bit_index, qubit_bit_index,
                                                                        is_final_measurement=True)

            # It is a CTRL Round, thus, the Semi-Quantum Entity Party, will just Reflect the Qubit,
            # to the Distributor of the Protocol, without measure it (less probable)
            elif int(pre_shared_key_bits[num_round]) == CTRL_REFLECT_ROUND_BIT:

                # Print the information about the respective operation on the Qubit (Particle)
                print("{} reflected the Qubit (Particle) received!!!"
                      .format(self.get_party_user_client().get_user_client_name()))

                # Apply the Pauli-I to the Qubit,
                # according to the Party Entity's ID
                quantum_circuit.apply_pauli_i(qubit_bit_index)

            # Print a blank line
            print("\n")

            # Update the Quantum Circuit of the Protocol Round
            protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

            # Return the Protocol Round updated
            return protocol_round

        # If the Party is the Distributor of the Protocol and the Party possesses
        # all the bipartite Pre-Shared Keys between itself and the other PARTIES
        else:

            # Raise the Value Error exception
            raise ValueError("The Distributor Party is not allowed to SIFT (Measure and Resend) Rounds or "
                             "just Reflect the Qubits (CTRL Rounds)!!!")

    # Execute the Quantum Circuit of the Protocol Round, if it is a SIFT (Measure and Resend) Round
    # NOTE: This function should be executed only once, and only, by the Distributor Party Entity,
    #       in order to ensure that its execution is unique
    def execute_protocol_round_quantum_circuit_for_sift_rounds(self, num_parties, protocol_round):

        # Only the Distributor Party Entity is allowed to check
        # if it is required to execute the Quantum Circuit of the Protocol Round,
        # in order to allow the Semi-Quantum Party Entities to extract
        # the correct results of the Protocol Round of
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
        # since the Quantum Circuit should only be executed once,
        # due to the truly random correlated results of the Bipartite and Multipartite Entanglements
        # NOTES:
        # 1) In practice, should be the Semi-Quantum Party Entities to execute the Quantum Circuit,
        #    but execute it more than once, can lead to random (and wrong) results;
        #    And thus, this function should be delegated to the Distributor Party Entity,
        #    to ensure that the operation is someway unique, regarding a Protocol Round;
        if self.is_distributor() and (self.get_resources_context().lower() == QUANTUM_PARTY_ENTITY.lower()):

            # Retrieve the number of the Protocol Round
            num_round = protocol_round.get_num_round()

            # Retrieve the Bipartite Pre-Shared Keys of the Distributor of
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            bipartite_pre_shared_keys = self.get_bipartite_pre_shared_keys()

            # Retrieve the bit of the Pre-Shared Key, corresponding to the current round
            round_type_bit = bipartite_pre_shared_keys[0].get_bipartite_pre_shared_key()[num_round]  # TODO

            # Retrieve the Quantum Circuit of the Protocol Round
            quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

            # It is a SIFT (Measure and Resend) Round, thus, the Semi-Quantum Party Entity,
            # will Measure and Resend the Qubit back again to the Distributor of the Protocol (more probable)
            if int(round_type_bit) == SIFT_MEASURE_AND_RESEND_ROUND_BIT:

                # Prepare and Measure the Qubit in the Z-Basis (Computational Basis),
                # according to the Distributor Party Entity's ID
                # NOTE: This is necessary, since the Quantum Circuit will be executed only once;
                quantum_circuit.prepare_measure_single_qubit_in_z_basis(0, 0, 0, 0, is_final_measurement=True)

                # Getting the Backend for the QASM (Quantum ASseMbly) for the simulation of the Quantum Circuit
                # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
                qasm_backend = Aer.get_backend("qasm_simulator")

                # Execute the Quantum Circuit and store the Measurement results in a Dictionary Object,
                # for a frequency counting
                final_results_quantum_circuit_measurement = \
                    execute(quantum_circuit.quantum_circuit, qasm_backend, shots=1).result().get_counts()

                # Retrieve the Bits from the Execution of the Quantum Circuit of
                # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                # NOTE:
                # - It is necessary to invert the order of the Bits from the Execution of
                #   the Quantum Circuit of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                #   since the resulting Bits are presented and ordered,
                #   from the most significant to the least significant one
                circuit_bits = list(final_results_quantum_circuit_measurement.keys())[0][::-1]

                # Concatenate the Bits from the Distributor
                protocol_sift_round_results = (circuit_bits[0] + circuit_bits[(2 * num_parties) - 1:])

                # Apply Barriers to all the Qubits of the Quantum Circuit for
                # the Round of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                quantum_circuit.apply_barriers_to_all()

                # Update the Quantum Circuit of the SIFT (Measure and Resend) Round of the Protocol
                protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

                # Save the Results of the SIFT (Measure and Resend) Round of the Protocol
                protocol_round.save_round_results(protocol_sift_round_results)

                # Return the Protocol Round updated
                return protocol_round

            # Apply Barriers to all the Qubits of the Quantum Circuit for
            # the Round of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            quantum_circuit.apply_barriers_to_all()

            # Update the Quantum Circuit, ready to be just sent back, CTRL (Reflect) Round of the Protocol
            protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

            # Return the Protocol Round updated
            return protocol_round

        # If it is not the Distributor Party Entity, then, it cannot execute
        # the Quantum Circuit for the SIFT (Measure and Resend) Rounds of
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Raise a Runtime Error
            raise RuntimeError("Only the Distributor Party Entity can execute the "
                               "Quantum Circuits for the SIFT (Measure and Resend) Rounds of "
                               "the Semi-Quantum Conference Key Agreement (SQCKA) Protocol!!!")

    # Reset the Qubits of the Quantum Circuit of the SIFT (Measure and Resend) Round
    # NOTE: This function should be executed only once, and only, by the Distributor Party Entity,
    #       in order to ensure that its execution is unique
    def reset_qubits_to_resend_for_sift_rounds(self, protocol_round):

        # Only the Distributor Party Entity is allowed to reset
        # the Quantum Circuit of a SIFT (Measure and Resend) Round of
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
        # since the Quantum Circuit should only be executed once,
        # due to the truly random correlated results of the Bipartite and Multipartite Entanglements
        # NOTES:
        # 1) In practice, should be the Semi-Quantum Party Entities to reset its own Qubits,
        #    in the Quantum Circuit, but reset it more than once, can lead to wrong results;
        #    And thus, this function should be delegated to the Distributor Party Entity,
        #    to ensure that the operation is someway unique, regarding a Protocol Round;
        if self.is_distributor() and (self.get_resources_context().lower() == QUANTUM_PARTY_ENTITY.lower()):

            # Retrieve the number of the Protocol Round
            num_round = protocol_round.get_num_round()

            # Retrieve the Bipartite Pre-Shared Keys of the Distributor of
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            bipartite_pre_shared_keys = self.get_bipartite_pre_shared_keys()

            # Retrieve the bit of the Pre-Shared Key, corresponding to the current round
            round_type_bit = bipartite_pre_shared_keys[0].get_bipartite_pre_shared_key()[num_round]  # TODO

            # Retrieve the Quantum Circuit of the Protocol Round
            quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

            # It is a SIFT (Measure and Resend) Round, thus, the Semi-Quantum Party Entity,
            # will Measure and Resend the Qubit back again to the Distributor of the Protocol (more probable)
            if int(round_type_bit) == SIFT_MEASURE_AND_RESEND_ROUND_BIT:

                # Reset all the Qubits of the Quantum Circuit for
                # the Round of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                quantum_circuit.reset_all()

                # Print the information about resetting the Quantum Circuit,
                # after the Z-Basis (Computational Basis) Measurement,
                # for the current Measure and Resend (SIFT Operation) Round
                print("Resetting the Qubits (Particles) of the Quantum Circuit,\n"
                      "after the Z-Basis (Computational Basis) Measurement...")

                # Print the blank line
                print("\n")

                # Update the Quantum Circuit of the Protocol, which was reset
                protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

            # Return the Protocol Round updated
            return protocol_round

        # If it is not the Distributor Party Entity, then, it cannot reset
        # the Quantum Circuit for the SIFT (Measure and Resend) Rounds of
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Raise a Runtime Error
            raise RuntimeError("Only the Distributor Party Entity can reset the Qubits of "
                               "the Quantum Circuits for the SIFT (Measure and Resend) Rounds of "
                               "the Semi-Quantum Conference Key Agreement (SQCKA) Protocol!!!")

    # Prepare the Qubits of the Quantum Circuit of the SIFT (Measure and Resend) Round,
    # of the Distributor Party Entity and of the Semi-Quantum Party Entities that,
    # will send them back over the Quantum Communication Channels
    def prepare_qubits_to_be_sent_back_for_sift_rounds(self, num_parties, protocol_round):

        # If the Party Entity is the Distributor of
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if self.is_distributor() and (self.get_resources_context().lower() == QUANTUM_PARTY_ENTITY.lower()):

            # Retrieve the number of the Protocol Round
            num_round = protocol_round.get_num_round()

            # Retrieve the Bipartite Pre-Shared Keys of the Distributor of
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            bipartite_pre_shared_keys = self.get_bipartite_pre_shared_keys()

            # Retrieve the bit of the Pre-Shared Key, corresponding to the current round
            round_type_bit = bipartite_pre_shared_keys[0].get_bipartite_pre_shared_key()[num_round]  # TODO

            # Retrieve the Quantum Circuit of the Protocol Round
            quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

            # It is a SIFT (Measure and Resend) Round, thus, the Semi-Quantum Party Entity,
            # will Measure and Resend the Qubit back again to the Distributor of the Protocol (more probable)
            if int(round_type_bit) == SIFT_MEASURE_AND_RESEND_ROUND_BIT:

                # Retrieve the Bits of the results of the Protocol Round
                protocol_round_results = protocol_round.get_round_results()

                # Retrieve the Bit of the result of the Protocol Round,
                # regarding the Distributor Party Entity
                protocol_round_result_bit = protocol_round_results[0]

                # If the Bit of the result of the Protocol Round,
                # regarding the Distributor Party Entity, is 0
                if int(protocol_round_result_bit) == 0:

                    # Apply the Pauli-I to the Qubit,
                    # according to the Party Entity's ID
                    quantum_circuit.apply_pauli_i(0)

                # If the Bit of the result of the Protocol Round,
                # regarding the Distributor Party Entity, is 1
                elif int(protocol_round_result_bit) == 1:

                    # Apply the Pauli-X to the Qubit,
                    # according to the Party Entity's ID
                    quantum_circuit.apply_pauli_x(0)

        # If the Party Entity is not the Distributor of
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Retrieve the number of the Protocol Round
            num_round = protocol_round.get_num_round()

            # Retrieve the bipartite Pre-Shared Key, with the Party Entity of the Protocol
            pre_shared_key_bits = self.bipartite_pre_shared_keys.get_bipartite_pre_shared_key()

            # Retrieve the Bit of the Pre-Shared Key, corresponding to the current round
            round_type_bit = pre_shared_key_bits[num_round]  # TODO

            # Retrieve the Quantum Circuit of the Protocol Round
            quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

            # It is a SIFT (Measure and Resend) Round, thus, the Semi-Quantum Party Entity,
            # will Measure and Resend the Qubit back again to the Distributor of the Protocol (more probable)
            if int(round_type_bit) == SIFT_MEASURE_AND_RESEND_ROUND_BIT:

                # Compute the index of the Quantum Circuit,
                # according to the respective qubit and bit of the Semi-Quantum Party Entity
                qubit_bit_index = ((2 * num_parties) + self.party_entity_id - 2)

                # Retrieve the Bits of the results of the Protocol Round
                protocol_round_results = protocol_round.get_round_results()

                # Retrieve the Bit of the result of the Protocol Round,
                # regarding the Distributor Party Entity
                protocol_round_result_bit = protocol_round_results[self.party_entity_id]

                # If the Bit of the result of the Protocol Round,
                # regarding the Distributor Party Entity, is 0
                if int(protocol_round_result_bit) == 0:

                    # Apply the Pauli-I to the Qubit,
                    # according to the Party Entity's ID
                    quantum_circuit.apply_pauli_i(qubit_bit_index)

                    # Print the information about flipping or not the state of
                    # the Qubit (Particle) on the Quantum Circuit of the current Round,
                    # to introducing the Qubit (Particle) in the same state it was found,
                    # after the Z-Basis (Computational Basis) Measurement,
                    # for the current Measure and Resend (SIFT Operation) Round
                    print("{} does not flipped the Qubit (Particle) (i.e., setting it to |0⟩), before resend it..."
                          .format(self.get_party_user_client().get_user_client_name()))

                # If the Bit of the result of the Protocol Round,
                # regarding the Distributor Party Entity, is 1
                elif int(protocol_round_result_bit) == 1:

                    # Apply the Pauli-X to the Qubit,
                    # according to the Party Entity's ID
                    quantum_circuit.apply_pauli_x(qubit_bit_index)

                    # Print the information about flipping or not the state of
                    # the Qubit (Particle) on the Quantum Circuit of the current Round,
                    # to introducing the Qubit (Particle) in the same state it was found,
                    # after the Z-Basis (Computational Basis) Measurement,
                    # for the current Measure and Resend (SIFT Operation) Round
                    print("{} flipped the Qubit (Particle) (i.e., setting it to |1⟩), before resend it..."
                          .format(self.get_party_user_client().get_user_client_name()))

                # Print the blank line
                print("\n")

        # Update the Quantum Circuit, ready to be just sent back, CTRL (Reflect) Round of the Protocol
        protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

        # Return the Protocol Round updated
        return protocol_round

    # Send back the Quantum Data/Information to the Distributor Party Entity,
    # over the Quantum Communication Channels
    def send_back_quantum_data_information_to_distributor_party_entity(self, num_parties, protocol_round):

        # If the Party is not the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if not self.is_distributor() and \
                (self.get_resources_context().lower() == SEMI_QUANTUM_PARTY_ENTITY.lower()):

            # Retrieve the Quantum Circuit of the Protocol Round
            quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

            # Compute the index of the Quantum Circuit,
            # according to the respective Qubit and Bit of the Semi-Quantum Party Entity
            qubit_bit_index_semi_quantum_party_entity = ((2 * num_parties) + self.party_entity_id - 2)

            # Compute the index of the Quantum Circuit,
            # according to the respective Qubit and Bit of the Semi-Quantum Party Entity
            qubit_bit_index_fiber_optic = (num_parties + self.party_entity_id - 1)

            # Apply the Swap Gate, between the Qubits of the Distributor Party Entity and
            # the Qubits of the Quantum Communication Channel
            quantum_circuit.apply_swap(qubit_bit_index_semi_quantum_party_entity,
                                       qubit_bit_index_fiber_optic)

            # Update the Quantum Circuit of the Protocol Round
            protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

            # Return the Protocol Round updated
            return protocol_round

        # If the Party is not the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Raise a Runtime Error
            raise RuntimeError("Only the Semi-Quantum Party Entities can send back the Quantum Data/Information, "
                               "over the Quantum Communication Channels!!!")

    # Receive back the Quantum Data/Information from the Semi-Quantum Party Entities,
    # over the Quantum Communication Channels
    def receive_back_quantum_data_information_from_semi_quantum_party_entities(self, num_parties, protocol_round):

        # If the Party Entity is the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if self.is_distributor() and (self.get_resources_context().lower() == QUANTUM_PARTY_ENTITY.lower()):

            # Retrieve the Quantum Circuit of the Protocol Round
            quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

            # For each Semi-Quantum Entity
            for current_num_semi_quantum_entity in range(1, num_parties):

                # Apply the Swap Gate, between the Qubits of the Distributor Party Entity and
                # the Qubits of the Quantum Communication Channel
                quantum_circuit.apply_swap((num_parties + current_num_semi_quantum_entity - 1),
                                           current_num_semi_quantum_entity)

                # Apply Barriers to all the Qubits of the Quantum Circuit for
                # the Round of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                quantum_circuit.apply_barriers_to_all()

            # Update the Quantum Circuit of the Protocol Round
            protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

            # Return the Protocol Round updated
            return protocol_round

        # If the Party is not the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Raise a Runtime Error
            raise RuntimeError("Only the Distributor Party Entity can send the Quantum Data/Information, "
                               "over the Quantum Communication Channels!!!")

    # Prepare to Measurement of a Bipartite or Multipartite Quantum Entanglement, by inverting Quantum Circuit
    def measure_quantum_entanglement_by_inverting_quantum_circuit(self, quantum_entanglement_type,
                                                                  num_parties, protocol_round,
                                                                  bell_state_type=None,
                                                                  qubits_edges_indexes_for_resource_state=None):

        # If the current Round of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if protocol_round.get_type_round() == CTRL_REFLECT_ROUND_3:

            # If the Party Entity is the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            if self.is_distributor() and (self.get_resources_context().lower() == QUANTUM_PARTY_ENTITY.lower()):

                # Retrieve the Quantum Circuit of the Protocol Round
                quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

                # If the Quantum Entanglement to prepare is a Bell State
                if quantum_entanglement_type.upper() == BELL_STATE:

                    # If the number of parties involved is higher than 2
                    if num_parties > 2:

                        # If the configuration of the Bell State is specified
                        if bell_state_type is not None:

                            # If the configuration of the Bell State is possible
                            if bell_state_type in POSSIBLE_CONFIGURATIONS_BELL_STATES:

                                # If the Bipartite Entangled State is Bell State (EPR Pair):
                                # - |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
                                if (bell_state_type == EPR_PAIR_STATE) or (bell_state_type == BELL_STATE_PHI_PLUS):

                                    # Prepare the inverse of the EPR Pair (Bell State) for 2 Qubits
                                    quantum_circuit = QiskitBellState \
                                        .QiskitBellState((BELL_STATE_PHI_PLUS + "_" + EPR_PAIR_STATE).lower(),
                                                         BELL_STATE_PHI_PLUS,
                                                         quantum_circuit,
                                                         0, 1).measure_bipartite_entanglement()

                                    # Getting the Backend for the QASM (Quantum ASseMbly) for
                                    # the simulation of the Quantum Circuit
                                    # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
                                    qasm_backend = Aer.get_backend("qasm_simulator")

                                    # Execute the Quantum Circuit and store the Measurement results
                                    # in a Dictionary Object, for a frequency counting
                                    final_results_quantum_circuit_measurement = \
                                        execute(quantum_circuit.quantum_circuit, qasm_backend, shots=1)\
                                        .result().get_counts()

                                    # Retrieve the Bits from the Execution of the Quantum Circuit of
                                    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                                    # NOTE:
                                    # - It is necessary to invert the order of the Bits from
                                    #   the Execution of the Quantum Circuit of
                                    #   the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                                    #   since the resulting Bits are presented and ordered,
                                    #   from the most significant to the least significant one
                                    circuit_bits = list(final_results_quantum_circuit_measurement.keys())[0][::-1]

                                    # Retrieve the Bits for the Measurement of the Multipartite Entanglement State
                                    protocol_sift_round_results = circuit_bits[:num_parties]

                                    # Update the Quantum Circuit of the CTRL (Reflected) Round of the Protocol
                                    protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

                                    # Save the Results of the CTRL (Reflected) Round of the Protocol
                                    protocol_round.save_round_results(protocol_sift_round_results)

                                    # Return the Protocol Round updated
                                    return protocol_round

                                # If the Bipartite Entangled State is Bell State:
                                # - |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
                                elif bell_state_type == BELL_STATE_PHI_MINUS:

                                    # Prepare the inverse of
                                    # the Bell State: |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
                                    quantum_circuit = QiskitBellState \
                                        .QiskitBellState(BELL_STATE_PHI_MINUS.lower(),
                                                         BELL_STATE_PHI_MINUS,
                                                         quantum_circuit,
                                                         0, 1).measure_bipartite_entanglement()

                                    # Getting the Backend for the QASM (Quantum ASseMbly) for
                                    # the simulation of the Quantum Circuit
                                    # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
                                    qasm_backend = Aer.get_backend("qasm_simulator")

                                    # Execute the Quantum Circuit and store the Measurement results
                                    # in a Dictionary Object, for a frequency counting
                                    final_results_quantum_circuit_measurement = \
                                        execute(quantum_circuit.quantum_circuit, qasm_backend, shots=1) \
                                        .result().get_counts()

                                    # Retrieve the Bits from the Execution of the Quantum Circuit of
                                    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                                    # NOTE:
                                    # - It is necessary to invert the order of the Bits from
                                    #   the Execution of the Quantum Circuit of
                                    #   the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                                    #   since the resulting Bits are presented and ordered,
                                    #   from the most significant to the least significant one
                                    circuit_bits = list(final_results_quantum_circuit_measurement.keys())[0][::-1]

                                    # Retrieve the Bits for the Measurement of the Multipartite Entanglement State
                                    protocol_sift_round_results = circuit_bits[:num_parties]

                                    # Update the Quantum Circuit of the CTRL (Reflected) Round of the Protocol
                                    protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

                                    # Save the Results of the CTRL (Reflected) Round of the Protocol
                                    protocol_round.save_round_results(protocol_sift_round_results)

                                    # Return the Protocol Round updated
                                    return protocol_round

                                # If the Bipartite Entangled State is Bell State:
                                # - |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
                                elif bell_state_type == BELL_STATE_PSI_PLUS:

                                    # Prepare the inverse of
                                    # the Bell State: |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
                                    quantum_circuit = QiskitBellState \
                                        .QiskitBellState(BELL_STATE_PSI_PLUS.lower(),
                                                         BELL_STATE_PSI_PLUS,
                                                         quantum_circuit,
                                                         0, 1).measure_bipartite_entanglement()

                                    # Getting the Backend for the QASM (Quantum ASseMbly) for
                                    # the simulation of the Quantum Circuit
                                    # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
                                    qasm_backend = Aer.get_backend("qasm_simulator")

                                    # Execute the Quantum Circuit and store the Measurement results
                                    # in a Dictionary Object, for a frequency counting
                                    final_results_quantum_circuit_measurement = \
                                        execute(quantum_circuit.quantum_circuit, qasm_backend, shots=1) \
                                        .result().get_counts()

                                    # Retrieve the Bits from the Execution of the Quantum Circuit of
                                    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                                    # NOTE:
                                    # - It is necessary to invert the order of the Bits from
                                    #   the Execution of the Quantum Circuit of
                                    #   the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                                    #   since the resulting Bits are presented and ordered,
                                    #   from the most significant to the least significant one
                                    circuit_bits = list(final_results_quantum_circuit_measurement.keys())[0][::-1]

                                    # Retrieve the Bits for the Measurement of the Multipartite Entanglement State
                                    protocol_sift_round_results = circuit_bits[:num_parties]

                                    # Update the Quantum Circuit of the CTRL (Reflected) Round of the Protocol
                                    protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

                                    # Save the Results of the CTRL (Reflected) Round of the Protocol
                                    protocol_round.save_round_results(protocol_sift_round_results)

                                    # Return the Protocol Round updated
                                    return protocol_round

                                # If the Bipartite Entangled State is Bell State:
                                # - |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
                                elif bell_state_type == BELL_STATE_PSI_MINUS:

                                    # Prepare the inverse of
                                    # the Bell State: |ψ^+-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
                                    quantum_circuit = QiskitBellState \
                                        .QiskitBellState(BELL_STATE_PSI_MINUS.lower(),
                                                         BELL_STATE_PSI_MINUS,
                                                         quantum_circuit,
                                                         0, 1).measure_bipartite_entanglement()

                                    # Getting the Backend for the QASM (Quantum ASseMbly) for
                                    # the simulation of the Quantum Circuit
                                    # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
                                    qasm_backend = Aer.get_backend("qasm_simulator")

                                    # Execute the Quantum Circuit and store the Measurement results
                                    # in a Dictionary Object, for a frequency counting
                                    final_results_quantum_circuit_measurement = \
                                        execute(quantum_circuit.quantum_circuit, qasm_backend, shots=1) \
                                        .result().get_counts()

                                    # Retrieve the Bits from the Execution of the Quantum Circuit of
                                    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                                    # NOTE:
                                    # - It is necessary to invert the order of the Bits from
                                    #   the Execution of the Quantum Circuit of
                                    #   the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                                    #   since the resulting Bits are presented and ordered,
                                    #   from the most significant to the least significant one
                                    circuit_bits = list(final_results_quantum_circuit_measurement.keys())[0][::-1]

                                    # Retrieve the Bits for the Measurement of the Multipartite Entanglement State
                                    protocol_sift_round_results = circuit_bits[:num_parties]

                                    # Update the Quantum Circuit of the CTRL (Reflected) Round of the Protocol
                                    protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

                                    # Save the Results of the CTRL (Reflected) Round of the Protocol
                                    protocol_round.save_round_results(protocol_sift_round_results)

                                    # Return the Protocol Round updated
                                    return protocol_round

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
                elif quantum_entanglement_type.upper() == GHZ_STATE:

                    # If the number of parties involved is higher than 2
                    if num_parties > 2:

                        # Set the Control-Qubit
                        control_qubit_index = 0

                        # Set the list of Target-Qubits
                        target_qubits_indexes = list(range(1, num_parties))

                        # Prepare the GHZ State, for multiple Qubits
                        quantum_circuit = QiskitGHZState \
                            .QiskitGHZState("ghz_state_qubits",
                                            quantum_circuit,
                                            control_qubit_index, target_qubits_indexes) \
                            .measure_multipartite_entanglement()

                        # Getting the Backend for the QASM (Quantum ASseMbly) for
                        # the simulation of the Quantum Circuit
                        # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
                        qasm_backend = Aer.get_backend("qasm_simulator")

                        # Execute the Quantum Circuit and store the Measurement results
                        # in a Dictionary Object, for a frequency counting
                        final_results_quantum_circuit_measurement = \
                            execute(quantum_circuit.quantum_circuit, qasm_backend, shots=1) \
                            .result().get_counts()

                        # Retrieve the Bits from the Execution of the Quantum Circuit of
                        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        # NOTE:
                        # - It is necessary to invert the order of the Bits from
                        #   the Execution of the Quantum Circuit of
                        #   the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                        #   since the resulting Bits are presented and ordered,
                        #   from the most significant to the least significant one
                        circuit_bits = list(final_results_quantum_circuit_measurement.keys())[0][::-1]

                        # Retrieve the Bits for the Measurement of the Multipartite Entanglement State
                        protocol_sift_round_results = circuit_bits[:num_parties]

                        # Update the Quantum Circuit of the CTRL (Reflected) Round of the Protocol
                        protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

                        # Save the Results of the CTRL (Reflected) Round of the Protocol
                        protocol_round.save_round_results(protocol_sift_round_results)

                        # Return the Protocol Round updated
                        return protocol_round

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use GHZ States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 3 Parties!!!")

                # If the Quantum Entanglement to prepare is a W State
                elif quantum_entanglement_type.upper() == W_STATE:

                    # If the number of parties involved is higher than 2
                    if num_parties > 2:

                        # Set the list of Qubits
                        qubits_indexes = list(range(0, num_parties))

                        # Prepare the W State, for multiple Qubits
                        quantum_circuit = QiskitWState \
                            .QiskitWState("w_state_qubits",
                                          quantum_circuit,
                                          qubits_indexes) \
                            .measure_multipartite_entanglement()

                        # Getting the Backend for the QASM (Quantum ASseMbly) for
                        # the simulation of the Quantum Circuit
                        # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
                        qasm_backend = Aer.get_backend("qasm_simulator")

                        # Execute the Quantum Circuit and store the Measurement results
                        # in a Dictionary Object, for a frequency counting
                        final_results_quantum_circuit_measurement = \
                            execute(quantum_circuit.quantum_circuit, qasm_backend, shots=1) \
                            .result().get_counts()

                        # Retrieve the Bits from the Execution of the Quantum Circuit of
                        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        # NOTE:
                        # - It is necessary to invert the order of the Bits from
                        #   the Execution of the Quantum Circuit of
                        #   the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                        #   since the resulting Bits are presented and ordered,
                        #   from the most significant to the least significant one
                        circuit_bits = list(final_results_quantum_circuit_measurement.keys())[0][::-1]

                        # Retrieve the Bits for the Measurement of the Multipartite Entanglement State
                        protocol_sift_round_results = circuit_bits[:num_parties]

                        # Update the Quantum Circuit of the CTRL (Reflected) Round of the Protocol
                        protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

                        # Save the Results of the CTRL (Reflected) Round of the Protocol
                        protocol_round.save_round_results(protocol_sift_round_results)

                        # Return the Protocol Round updated
                        return protocol_round

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use W States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 3 Parties!!!")

                # If the Quantum Entanglement to prepare is a Dicke State
                elif quantum_entanglement_type.upper() == DICKE_STATE:

                    # TODO - Handle this situation
                    return

                # If the Quantum Entanglement to prepare is a Resource State
                elif quantum_entanglement_type.upper() == RESOURCE_STATE:

                    # If the number of parties involved is higher than 1
                    if num_parties > 1:

                        # Set the list of Qubits
                        qubits_indexes = list(range(0, num_parties))

                        # Prepare the Resource State, as a Graph State by default, for multiple Qubits
                        quantum_circuit = QiskitGraphState \
                            .QiskitGraphState("resource_state_qubits",
                                              quantum_circuit,
                                              qubits_indexes,
                                              qubits_edges_indexes_for_resource_state) \
                            .measure_multipartite_entanglement()

                        # Getting the Backend for the QASM (Quantum ASseMbly) for
                        # the simulation of the Quantum Circuit
                        # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
                        qasm_backend = Aer.get_backend("qasm_simulator")

                        # Execute the Quantum Circuit and store the Measurement results
                        # in a Dictionary Object, for a frequency counting
                        final_results_quantum_circuit_measurement = \
                            execute(quantum_circuit.quantum_circuit, qasm_backend, shots=1) \
                            .result().get_counts()

                        # Retrieve the Bits from the Execution of the Quantum Circuit of
                        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        # NOTE:
                        # - It is necessary to invert the order of the Bits from
                        #   the Execution of the Quantum Circuit of
                        #   the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                        #   since the resulting Bits are presented and ordered,
                        #   from the most significant to the least significant one
                        circuit_bits = list(final_results_quantum_circuit_measurement.keys())[0][::-1]

                        # Retrieve the Bits for the Measurement of the Multipartite Entanglement State
                        protocol_sift_round_results = circuit_bits[:num_parties]

                        # Update the Quantum Circuit of the CTRL (Reflected) Round of the Protocol
                        protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

                        # Save the Results of the CTRL (Reflected) Round of the Protocol
                        protocol_round.save_round_results(protocol_sift_round_results)

                        # Return the Protocol Round updated
                        return protocol_round

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use Resource States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 2 Parties!!!")

                # If the Quantum Entanglement to prepare is a Graph State
                elif quantum_entanglement_type.upper() == GRAPH_STATE:

                    # If the number of parties involved is higher than 1
                    if num_parties > 1:

                        # Set the list of Qubits
                        qubits_indexes = list(range(0, num_parties))

                        # Prepare the Resource State, as a Graph State by default, for multiple Qubits
                        quantum_circuit = QiskitGraphState \
                            .QiskitGraphState("graph_state_qubits",
                                              quantum_circuit,
                                              qubits_indexes,
                                              qubits_edges_indexes_for_resource_state) \
                            .measure_multipartite_entanglement()

                        # Getting the Backend for the QASM (Quantum ASseMbly) for
                        # the simulation of the Quantum Circuit
                        # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
                        qasm_backend = Aer.get_backend("qasm_simulator")

                        # Execute the Quantum Circuit and store the Measurement results
                        # in a Dictionary Object, for a frequency counting
                        final_results_quantum_circuit_measurement = \
                            execute(quantum_circuit.quantum_circuit, qasm_backend, shots=1) \
                            .result().get_counts()

                        # Retrieve the Bits from the Execution of the Quantum Circuit of
                        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        # NOTE:
                        # - It is necessary to invert the order of the Bits from
                        #   the Execution of the Quantum Circuit of
                        #   the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                        #   since the resulting Bits are presented and ordered,
                        #   from the most significant to the least significant one
                        circuit_bits = list(final_results_quantum_circuit_measurement.keys())[0][::-1]

                        # Retrieve the Bits for the Measurement of the Multipartite Entanglement State
                        protocol_sift_round_results = circuit_bits[:num_parties]

                        # Update the Quantum Circuit of the CTRL (Reflected) Round of the Protocol
                        protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

                        # Save the Results of the CTRL (Reflected) Round of the Protocol
                        protocol_round.save_round_results(protocol_sift_round_results)

                        # Return the Protocol Round updated
                        return protocol_round

                    # If the number of parties involved is equal or lower than 2
                    else:

                        # Raise a Value Error
                        raise ValueError("It is impossible to use Graph States for "
                                         "Semi-Quantum Conference Key Agreement (SQCKA) with less than 2 Parties!!!")

                # If the Quantum Entanglement to prepare is a Cluster State
                elif quantum_entanglement_type.upper() == CLUSTER_STATE:

                    # TODO - Handle this situation
                    return

                # If the specified type of Quantum Entanglement is not one of the possible configurations for
                # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                else:

                    # Raise a Value Error
                    raise ValueError("The Quantum Entanglement specified for the Protocol is not possible to use!!!")

            # If the Party is not the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            else:

                # Raise a Runtime Error
                raise RuntimeError("Only the Distributor Party Entity can prepare Quantum Entanglements!!!")

        # Return the Protocol Round updated
        return protocol_round

    # Measure the Qubits of the Quantum Circuit of the CTRL (Reflect) Round,
    # which were reflected back from the Semi-Quantum Party Entities to the Distributor Party Entity,
    # over the Quantum Communication Channels
    def measure_quantum_data_information_for_ctrl_rounds(self, num_parties, protocol_round):

        # If the current Round of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if protocol_round.get_type_round() == CTRL_REFLECT_ROUND_3:

            # If the Party Entity is the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            if self.is_distributor() and (self.get_resources_context().lower() == QUANTUM_PARTY_ENTITY.lower()):

                # Retrieve the Quantum Circuit of the Protocol Round
                quantum_circuit = protocol_round.get_qiskit_quantum_circuit()

                # Create the list of the range of the Qubits and Bits
                num_qubits_bits_indexes = list(range(0, num_parties))

                # Measure the Qubits on the Quantum Memory of the Distributor Party Entity
                quantum_circuit.measure_qubits_interval(0, 0, num_qubits_bits_indexes, num_qubits_bits_indexes)

                # Getting the Backend for the QASM (Quantum ASseMbly) for the simulation of the Quantum Circuit
                # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
                qasm_backend = Aer.get_backend("qasm_simulator")

                # Execute the Quantum Circuit and store the Measurement results in a Dictionary Object,
                # for a frequency counting
                final_results_quantum_circuit_measurement = \
                    execute(quantum_circuit.quantum_circuit, qasm_backend, shots=1).result().get_counts()

                # Retrieve the Bits from the Execution of the Quantum Circuit of
                # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                # NOTE:
                # - It is necessary to invert the order of the Bits from the Execution of
                #   the Quantum Circuit of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                #   since the resulting Bits are presented and ordered,
                #   from the most significant to the least significant one
                circuit_bits = list(final_results_quantum_circuit_measurement.keys())[0][::-1]

                # Retrieve the Bits for the Measurement of the Multipartite Entanglement State
                protocol_sift_round_results = circuit_bits[:num_parties]

                # Update the Quantum Circuit of the CTRL (Reflected) Round of the Protocol
                protocol_round.update_qiskit_quantum_circuit(quantum_circuit)

                # Save the Results of the CTRL (Reflected) Round of the Protocol
                protocol_round.save_round_results(protocol_sift_round_results)

                # Return the Protocol Round updated
                return protocol_round

            # If the Party is not the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            else:

                # Raise a Runtime Error
                raise RuntimeError("Only the Distributor Party Entity can measure the "
                                   "reflected back Multipartite Entanglement,\n"
                                   "over the Quantum Communication Channels!!!")

        # Return the Protocol Round updated
        return protocol_round
