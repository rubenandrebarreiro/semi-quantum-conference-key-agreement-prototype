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

# Import the possible Bipartite and Multipartite Quantum Entanglement Types and
# the Possible Configurations for Bell States
from src.common.enumerations.QuantumEntanglementTypes \
    import POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES, POSSIBLE_CONFIGURATIONS_BELL_STATES, \
    BELL_STATE, EPR_PAIR_STATE, BELL_STATE_PHI_PLUS, BELL_STATE_PHI_MINUS, BELL_STATE_PSI_PLUS, BELL_STATE_PSI_MINUS,\
    GHZ_STATE, W_STATE, DICKE_STATE, RESOURCE_STATE, GRAPH_STATE, CLUSTER_STATE


# Import Packages and Libraries

# Import QiskitBellState from IBM_Qiskit.Entanglements.Bipartite
from src.ibm_qiskit.entanglements.bipartite import QiskitBellState

# Import QiskitGHZState from IBM_Qiskit.Entanglements.Multipartite
from src.ibm_qiskit.entanglements.multipartite import QiskitGHZState

# Import QiskitWState from IBM_Qiskit.Entanglements.Multipartite
from src.ibm_qiskit.entanglements.multipartite import QiskitWState

# Import QiskitGraphState from IBM_Qiskit.Entanglements.Multipartite.Resource_States
from src.ibm_qiskit.entanglements.multipartite.resource_states import QiskitGraphState

# Import QiskitQuantumTrueRandomBinaryStringGenerator from IBM_Qiskit.Utils.Random_Generator.Binary.Quantum
from src.ibm_qiskit.utils.random_generator.binary.quantum import QiskitQuantumTrueRandomBinaryStringGenerator


# Constants

# The number of counts for simulation
NUM_COUNTS_FOR_SIMULATION = 1000


# Class of the IBM Qiskit's Party for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocolParty:

    # Constructor of the IBM Qiskit's Party for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def __init__(self, party_id, party_user_client, master_status_flag, bipartite_pre_shared_keys):

        # Set the ID for the IBM Qiskit's Party for
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        self.party_id = party_id

        # Set the User/Client for the IBM Qiskit's Party for
        # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        self.party_user_client = party_user_client

        # Set the boolean flag, responsible to keep the information about if the Party is
        # the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol or not
        self.distributor_status_flag = master_status_flag

        # Set the Pre-Shared Key, previously established between the parties
        self.bipartite_pre_shared_keys = bipartite_pre_shared_keys

    # Return the ID for the IBM Qiskit's Party for
    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def get_party_id(self):
        return self.party_id

    # Return the User/Client for the IBM Qiskit's Party for
    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def get_party_user_client(self):
        return self.party_user_client

    # Retrieve the boolean flag, responsible to keep the information about if the Party is
    # the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol or not
    def is_distributor(self):
        return self.distributor_status_flag

    # Return the Bipartite Pre-Shared Keys that the Party possesses with other Parties
    def get_bipartite_pre_shared_keys(self):
        return self.bipartite_pre_shared_keys

    # Print the information about
    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Party
    def print_info(self):

        # Some prints to draw a top left-side corner
        print(" __")
        print("|")
        print("|")

        # Print the ID of the User/Client of the Party involved on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        print(" - Party's ID: {}".format(self.party_id))

        # Print the UUID of the User/Client of the Party involved on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        print(" - Party's User/Client's UUID: {}".format(self.get_party_user_client().get_user_client_uuid()))

        # Print the Name of the User/Client of the Party involved on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        print(" - Party's User/Client's Name: {}".format(self.get_party_user_client().get_user_client_name()))

        # Print the Distributor status of the Party involved on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        print(" - Party's Distributor Status: {}".format(self.is_distributor()))

        # Retrieve the Bipartite Pre-Shared Keys owned/possessed by the Party involved on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        bipartite_pre_shared_keys = self.get_bipartite_pre_shared_keys()

        # If the Party is the Distributor of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if self.is_distributor():

            # Retrieve the number of the Bipartite Pre-Shared Keys owned/possessed by the Party involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            num_bipartite_pre_shared_keys = len(bipartite_pre_shared_keys)

            # Print the header of the Bipartite Pre-Shared Keys owned/possessed by the Party involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            print("\n\n - {} Bipartite Pre-Shared Key(s) owned:\n".format(num_bipartite_pre_shared_keys))

            # For each Bipartite Pre-Shared Keys owned/possessed by the Party involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            for current_num_bipartite_pre_shared_key in range(num_bipartite_pre_shared_keys):

                # Print the information about the current Bipartite Pre-Shared Keys
                # owned/possessed by the Party involved on the
                # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                print("   [{}]".format((current_num_bipartite_pre_shared_key + 1)), end='')
                bipartite_pre_shared_keys[current_num_bipartite_pre_shared_key].print_info()

        # If the Party is not the Distributor of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Initialise the number of the Bipartite Pre-Shared Keys owned/possessed by the Party involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            num_bipartite_pre_shared_keys = 1

            # Retrieve the Bipartite Pre-Shared Key owned/possessed by the Party involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol, as single instance
            bipartite_pre_shared_key = bipartite_pre_shared_keys

            # Print the header of the Bipartite Pre-Shared Keys owned/possessed by the Party involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            print("\n\n - {} Bipartite Pre-Shared Key(s) owned:\n".format(num_bipartite_pre_shared_keys))

            # Print the information about the current Bipartite Pre-Shared Keys
            # owned/possessed by the Party involved on the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            print("   [{}]".format(num_bipartite_pre_shared_keys), end='')
            bipartite_pre_shared_key.print_info()

        # Some prints to draw a bottom left-side corner
        print("|")
        print("|__")

    # Generate the True Random String for the Distributor Party's Raw Key
    def generate_true_random_binary_string_for_master_party_raw_key(
        self, true_random_binary_string_for_master_party_raw_key_length
    ):

        # If the Party is the Distributor of the Protocol
        if self.is_distributor():

            # Create the True Random Binary String Generator for the SQCKA's
            true_random_binary_string_generator_for_master_party_raw_key = \
                QiskitQuantumTrueRandomBinaryStringGenerator\
                .QiskitQuantumTrueRandomBinaryStringGenerator(
                    "true_random_binary_string_generator_for_master_party_raw_key",
                    true_random_binary_string_for_master_party_raw_key_length,
                    NUM_COUNTS_FOR_SIMULATION
                )

            # Generate the final True Random Binary String from the Generator, previously created,
            # for the initial Raw Key of the Protocol's Distributor Party
            initial_true_random_binary_string_for_master_party_raw_key = \
                true_random_binary_string_generator_for_master_party_raw_key.generate_true_random_binary_string()

            # Return the initial Raw Key of the Protocol's Distributor Party
            return initial_true_random_binary_string_for_master_party_raw_key

        # If the Party is not the Distributor of the Protocol
        else:

            # Raise a Value Error
            raise ValueError("Only the Distributor Party can generate the initial Raw Key!!!")

    # Prepare a Bipartite or Multipartite Quantum Entanglement
    def prepare_quantum_entanglement(self, quantum_entanglement_type, num_parties, quantum_circuit,
                                     bell_state_type=None, qubits_edges_indexes_for_resource_state=None):

        # If the Party is not the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if not self.is_distributor():

            # Raise the Value Error exception
            raise ValueError("The Party Name specified to be the Distributor "
                             "(i.e., the party responsible for the distribution of the Common Secret Key "
                             "(Conference Key) between the parties involved is not present in "
                             "the list of Parties' Names involved!!!")

        # If the Party is the Distributor of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # If the specified type of Quantum Entanglement is one of the possible configurations for
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            if quantum_entanglement_type.upper() in POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES:

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
                                        .QiskitBellState((BELL_STATE_PHI_PLUS+"_"+EPR_PAIR_STATE).lower(),
                                                         BELL_STATE_PHI_PLUS,
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Return the EPR Pair (Bell State) for 2 Qubits
                                    return qiskit_quantum_circuit_epr_pair_bell_state_phi_plus

                                # If the Bipartite Entangled State is Bell State:
                                # - |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
                                elif bell_state_type == BELL_STATE_PHI_MINUS:

                                    # Prepare the Bell State: |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
                                    qiskit_quantum_circuit_bell_state_phi_minus = QiskitBellState \
                                        .QiskitBellState(BELL_STATE_PHI_MINUS.lower(),
                                                         BELL_STATE_PHI_MINUS,
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Return the Bell State for 2 Qubits
                                    return qiskit_quantum_circuit_bell_state_phi_minus

                                # If the Bipartite Entangled State is Bell State:
                                # - |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
                                elif bell_state_type == BELL_STATE_PSI_PLUS:

                                    # Prepare the Bell State: |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
                                    qiskit_quantum_circuit_bell_state_psi_plus = QiskitBellState \
                                        .QiskitBellState(BELL_STATE_PSI_PLUS.lower(),
                                                         BELL_STATE_PSI_PLUS,
                                                         quantum_circuit,
                                                         0, 1).prepare_bipartite_entanglement()

                                    # Return the Bell State for 2 Qubits
                                    return qiskit_quantum_circuit_bell_state_psi_plus

                                # If the Bipartite Entangled State is Bell State:
                                # - |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
                                elif bell_state_type == BELL_STATE_PSI_MINUS:

                                    # Prepare the Bell State: |ψ^+-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
                                    qiskit_quantum_circuit_bell_state_psi_minus = QiskitBellState \
                                        .QiskitBellState(BELL_STATE_PSI_MINUS.lower(),
                                                         BELL_STATE_PSI_MINUS,
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
                elif quantum_entanglement_type.upper() == W_STATE:

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
                elif quantum_entanglement_type.upper() == CLUSTER_STATE:

                    # TODO - Handle this situation
                    return

            # If the specified type of Quantum Entanglement is not one of the possible configurations for
            # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            else:

                # Raise a Value Error
                raise ValueError("The Quantum Entanglement specified for the Protocol is not possible to use!!!")

    # Measure and Resend the Qubit, or just Reflect it, according to the Pre-Shared Key
    def measure_and_resend_or_reflect_qubit(self, quantum_circuit, num_round, timestamp):

        # If the Party is not the Distributor of the Protocol and the Party possesses only
        # one Pre-Shared Key between itself and the Distributor of the Protocol
        if (not self.is_distributor()) and (len(self.bipartite_pre_shared_keys) == 1):

            # Retrieve the bipartite Pre-Shared Key, with the Distributor of the Protocol
            pre_shared_key_bits = self.bipartite_pre_shared_keys[0][1]

            # It is a SIFT Round, thus, the Normal Party, will Measure and Resend the Qubit
            # back again to the Distributor of the Protocol (more probable)
            if pre_shared_key_bits[num_round] == 0:

                # Prepare and Measure the Qubit in the Z-Basis (Computational Basis),
                # according to the Party's ID
                quantum_circuit.prepare_measure_single_qubit_in_z_basis((self.party_id - 1),
                                                                        (self.party_id - 1),
                                                                        is_final_measurement=True)

            # It is a CTRL Round, thus, the Normal Party, will just Reflect the Qubit,
            # to the Distributor of the Protocol, without measure it (less probable)
            elif pre_shared_key_bits[num_round] == 1:

                # Apply the Pauli-I to the Qubit,
                # according to the Party's ID
                quantum_circuit.apply_pauli_i(self.party_id - 1)

        # If the Party is the Distributor of the Protocol and the Party possesses
        # all the bipartite Pre-Shared Keys between itself and the other PARTIES
        else:

            # Raise the Value Error exception
            raise ValueError("The Distributor Party cannot Measure and Resend (SIFT Rounds) or "
                             "just Reflect the Qubits (CTRL Rounds)!!!")
