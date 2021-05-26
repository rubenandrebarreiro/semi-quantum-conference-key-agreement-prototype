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

from src.common.enumerations import StrategiesForEavesdroppingDetection
from src.common.enumerations.SemiQuantumCryptographyProtocolPartyEntityTypes \
    import QUANTUM_PARTY_ENTITY, SEMI_QUANTUM_PARTY_ENTITY


# Import Packages and Libraries

# Import TODO
from src.common.enumerations.SemiQuantumCryptographyProtocolRoundTypes \
    import SIFT_MEASURE_AND_RESEND_ROUND_3, CTRL_REFLECT_ROUND_3

# Import QiskitSQCKAProtocol from IBM_Qiskit.Cryptography.Semi_Quantum_Conference_Key_Agreement
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreement \
    import QiskitSQCKAProtocol

# Import QiskitSQCKAProtocolParameters from IBM_Qiskit.Cryptography.Semi_Quantum_Conference_Key_Agreement.Common
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreement.common \
    import QiskitSQCKAProtocolParameters

# Import QiskitSQCKAProtocolParty from IBM_Qiskit.Cryptography.Semi_Quantum_Conference_Key_Agreement.Common
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreement.common \
    import QiskitSQCKAProtocolPreSharedKeyPair

# Import QiskitSQCKAProtocolParty from IBM_Qiskit.Cryptography.Semi_Quantum_Conference_Key_Agreement.Entities
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreement.entities \
    import QiskitSQCKAProtocolPartyEntity


# Class for the Executor Service of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocolExecutorService:

    # Constructor of the Executor Service of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def __init__(self):

        # Initialise the Object representing the Protocol itself
        self.qiskit_sqcka_protocol = None

        # Initialise the boolean flag for the initialisation status of the Protocol itself
        self.qiskit_sqcka_protocol_initialised = False

        # Initialise the Parties involved in the Protocol
        self.qiskit_sqcka_protocol_party_entities = None

        # Initialise the boolean flag for the initialisation of the Parties involved in the Protocol
        self.qiskit_sqcka_protocol_party_entities_initialised = False

        # Initialise the Distributor Party of the Protocol
        self.qiskit_sqcka_protocol_distributor_party_entity = None

        # Initialise the boolean flag for the initialisation of the Distributor Party of the Protocol
        self.qiskit_sqcka_protocol_distributor_party_entity_initialised = False

        # Initialise the Bipartite Pre-Shared Keys used between the Parties, involved in the Protocol
        self.qiskit_sqcka_protocol_bipartite_pre_shared_keys = []

        # Initialise the boolean flag for the initialisation of
        # the Bipartite Pre-Shared Keys used between the Parties, involved in the Protocol
        self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised = False

        # Initialise the Parameters of the Protocol
        self.qiskit_sqcka_protocol_parameters = None

        # Initialise the boolean flag for the initialisation of the Parameters of the Protocol
        self.qiskit_sqcka_protocol_parameters_initialised = False

        # Initialise the boolean flag for the start status of the process of the Protocol
        self.qiskit_sqcka_protocol_started = False

    # Return the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def get_qiskit_sqcka_protocol(self):

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol is already initialised
        if self.qiskit_sqcka_protocol_initialised:

            # Return the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            return self.qiskit_sqcka_protocol

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol is not initialised yet
        else:

            # Return none
            return None

    # Set the Party Entities of the Protocol
    def set_protocol_party_entities(self, users_clients, party_entities_names,
                                    distributor_party_entity_name, bipartite_pre_shared_keys):

        # If the Bipartite Pre-Shared Keys were already be established
        if self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised:

            # Retrieve the number of Users/Clients
            num_users_clients = len(users_clients)

            # Retrieve the number of Party Entities
            num_parties = len(party_entities_names)

            # If the number of Party Entities and Users/Clients are the same
            if num_parties == num_users_clients:

                # Create the list of Party Entities' Names
                party_entities_names_lower = []

                # For each Party Entity's Name
                for party_entity_name in party_entities_names:

                    # Append the Party Entity's Name, in lowercase,
                    # to the list of Party Entities' Names
                    party_entities_names_lower.append(party_entity_name.lower())

                # Change the Party Entity's Name, for the lowercase
                distributor_party_entity_name_lower = distributor_party_entity_name.lower()

                # If the Party Entity's Name, responsible for the distribution of
                # the Common Secret Key (Conference Key),
                # is not present in the list of Party Entities' Names involved
                if distributor_party_entity_name_lower not in party_entities_names_lower:

                    # Raise the Value Error exception
                    raise ValueError("The Party Name specified to be the Distributor "
                                     "(i.e., the party responsible for the distribution of the Common Secret Key "
                                     "(Conference Key) between the parties involved is not present in "
                                     "the list of Parties' Names involved on the Protocol!!!")

                # Redefine the list of the Party Entities involved in the Protocol,
                # according to the number of them
                self.qiskit_sqcka_protocol_party_entities = ([None] * num_parties)

                # For each Party Entity involved in the Protocol
                for current_party_entity_id in range(num_parties):

                    # Retrieve the name of the current Party Entity
                    current_party_entity_name = party_entities_names_lower[current_party_entity_id]

                    # Initialise the User/Client for the current Party Entity
                    current_party_entity_user_client = None

                    # For each User/Client involved in the Protocol
                    for current_num_user_client in range(num_users_clients):

                        # If the name of the current Party Entity corresponds to
                        # the current User/Client
                        if current_party_entity_name == \
                                users_clients[current_num_user_client].get_user_client_name().lower():

                            # Retrieve the current User/Client
                            current_party_entity_user_client = users_clients[current_num_user_client]

                            # The pretended User/Client was found, so the loop can be broken
                            break

                    # If the current Party is the Distributor Party Entity
                    if current_party_entity_name.lower() == distributor_party_entity_name_lower.lower():

                        # Initialize the object of the Party Entity, as the Distributor of the Protocol
                        # noinspection PyTypeChecker
                        self.qiskit_sqcka_protocol_party_entities[current_party_entity_id] = \
                            QiskitSQCKAProtocolPartyEntity \
                            .QiskitSQCKAProtocolPartyEntity(current_party_entity_id, current_party_entity_user_client,
                                                            QUANTUM_PARTY_ENTITY, True, bipartite_pre_shared_keys)

                        # Set the Distributor Party Entity of the Protocol
                        self.set_protocol_distributor_party_entity(self.qiskit_sqcka_protocol_party_entities[current_party_entity_id])

                    # If the current Party is not the Distributor Party Entity
                    else:

                        # Initialise the bipartite Pre-Shared Key
                        bipartite_pre_shared_key = None

                        # For each bipartite Pre-Shared Key
                        for current_bipartite_pre_shared_key in range(len(bipartite_pre_shared_keys)):

                            # Retrieve the current bipartite Pre-Shared Key
                            bipartite_pre_shared_key = bipartite_pre_shared_keys[current_bipartite_pre_shared_key]

                            # If the current bipartite Pre-Shared Key is owned by the current Party Entity
                            if bipartite_pre_shared_key \
                                    .get_user_client_2().get_user_client_name() == current_party_entity_name:

                                # The pretended bipartite Pre-Shared Key was found, so the loop can be broken
                                break

                        # Initialize the object of the Party, as a Normal Party Entity
                        # noinspection PyTypeChecker
                        self.qiskit_sqcka_protocol_party_entities[current_party_entity_id] = \
                            QiskitSQCKAProtocolPartyEntity \
                            .QiskitSQCKAProtocolPartyEntity(current_party_entity_id, current_party_entity_user_client,
                                                            SEMI_QUANTUM_PARTY_ENTITY, False, bipartite_pre_shared_key)

                # Set the boolean flag for the initialisation of the Party Entities of the Protocol, as True
                self.qiskit_sqcka_protocol_party_entities_initialised = True

            # If the number of Users/Clients and Party Entities are not the same
            else:

                # Raise a Value Error
                raise ValueError("The number of Users/Clients and Party Entities are not the same!!!")

        # If the Bipartite Pre-Shared Keys were not established yet
        else:

            # Raise a Value Error
            raise ValueError("The Bipartite Pre-Shared Keys were not established yet!!!")

    # Return the Party Entities of the Protocol
    def get_protocol_party_entities(self):

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # list of Parties were already initialised
        if self.qiskit_sqcka_protocol_party_entities_initialised:

            # Return the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's list of Parties
            return self.qiskit_sqcka_protocol_party_entities

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # list of Parties were not initialised yet
        else:

            # Return none
            return None

    # Set the Distributor Party Entity of the Protocol
    def set_protocol_distributor_party_entity(self, qiskit_sqcka_protocol_distributor_party_entity):

        # Set the Distributor Party Entity of the Protocol
        self.qiskit_sqcka_protocol_distributor_party_entity = \
            qiskit_sqcka_protocol_distributor_party_entity

        # Set the boolean flag for the initialisation of
        # the Distributor Party Entity of the Protocol, as True
        self.qiskit_sqcka_protocol_distributor_party_entity_initialised = True

    # Return the Distributor Party Entity of the Protocol
    def get_protocol_distributor_party_entity(self):

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Distributor Party Entity were already initialised
        if self.qiskit_sqcka_protocol_distributor_party_entity_initialised:

            # Return the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
            # Distributor Party Entity
            return self.qiskit_sqcka_protocol_distributor_party_entity

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Distributor Party Entity were not initialised yet
        else:

            # Return none
            return None

    # Set the Bipartite Pre-Shared Keys, as initialised
    def set_protocol_bipartite_pre_shared_keys_initialised(self):

        # If there are already fulfilled all the Bipartite Pre-Shared Keys,
        # it is possible to set the boolean flag as True
        if len(self.qiskit_sqcka_protocol_bipartite_pre_shared_keys) == \
                (self.qiskit_sqcka_protocol_parameters.get_num_parties() - 1):

            # Set the boolean flag for the initialisation of
            # the Bipartite Pre-Shared Keys used between the Parties, involved in the Protocol, as True
            self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised = True

        # If it is not possible to set the boolean flag as True, because of missing Bipartite Pre-Shared Keys,
        # or even, to more Bipartite Pre-Shared Keys configured than the allowed number of them
        else:

            # Raise Value Error
            raise ValueError("There are less or more Bipartite Pre-Shared Keys specified to "
                             "be configured in the Protocol!!!")

    # Add a Bipartite Pre-Shared Key to the Protocol
    def add_protocol_bipartite_pre_shared_key(self, user_client_1, user_client_2,
                                              bipartite_pre_shared_key_binary_string):

        # If the Parameters of the Protocol were already configured
        if self.qiskit_sqcka_protocol_parameters_initialised:

            # If it is possible to add one more Bipartite Pre-Shared Key
            if len(self.qiskit_sqcka_protocol_bipartite_pre_shared_keys) < \
                    (self.qiskit_sqcka_protocol_parameters.get_num_parties() - 1):

                # Create a Bipartite Pre-Shared Key object
                qiskit_sqcka_protocol_bipartite_pre_shared_key = \
                    QiskitSQCKAProtocolPreSharedKeyPair \
                    .QiskitSQCKAProtocolPreSharedKeyPair(user_client_1, user_client_2,
                                                         bipartite_pre_shared_key_binary_string)

                # Add the previously created Bipartite Pre-Shared Key object to
                # the list of the Bipartite Pre-Shared Keys
                self.qiskit_sqcka_protocol_bipartite_pre_shared_keys \
                    .append(qiskit_sqcka_protocol_bipartite_pre_shared_key)

            # If it is not possible to add one more Bipartite Pre-Shared Key
            else:

                # Raise a Value Error
                raise ValueError("It is only possible to add {} Bipartite Pre-Shared Keys to the Protocol!!!"
                                 .format((self.qiskit_sqcka_protocol_parameters.get_num_parties() - 1)))

        # If the Parameters of the Protocol were not configured yet
        else:

            # Raise a Value Error
            raise ValueError("The Parameters of the Protocol need to "
                             "be configured before add any Bipartite Pre-Shared Key!!!")

    # Return all the Bipartite Pre-Shared Key of the Protocol
    def get_protocol_bipartite_pre_shared_keys(self):

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Bipartite Pre-Shared Keys were already initialised
        if self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised:

            # Return the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
            # Bipartite Pre-Shared Keys
            return self.qiskit_sqcka_protocol_bipartite_pre_shared_keys

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Bipartite Pre-Shared Keys were not initialised yet
        else:

            # Return none
            return None

    # Configure the Parameters of the Protocol
    def configure_protocol_parameters(self, num_parties, num_rounds,
                                      num_physical_quantum_communication_channels,
                                      num_physical_classical_communication_channels,
                                      quantum_signal_variable_mode_type,
                                      communication_physical_medium_type,
                                      preparing_bases, quantum_entanglement_type,
                                      strategy_for_eavesdropping_detection,
                                      communication_path_edges_between_parties_names=None,
                                      communication_path_distances_between_parties_names=None):

        # Initialise the Parameters of the Protocol
        self.qiskit_sqcka_protocol_parameters = \
            QiskitSQCKAProtocolParameters \
            .QiskitSQCKAProtocolParameters(num_parties, num_rounds,
                                           num_physical_quantum_communication_channels,
                                           num_physical_classical_communication_channels,
                                           quantum_signal_variable_mode_type,
                                           communication_physical_medium_type,
                                           preparing_bases, quantum_entanglement_type,
                                           strategy_for_eavesdropping_detection,
                                           communication_path_edges_between_parties_names,
                                           communication_path_distances_between_parties_names)

        # Set the boolean flag for the initialisation of Parameters of the Protocol, as True
        self.qiskit_sqcka_protocol_parameters_initialised = True

    # Return the Parameters of the Protocol
    def get_protocol_parameters(self):

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Parameters were already initialised
        if self.qiskit_sqcka_protocol_parameters_initialised:

            # Return the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
            return self.qiskit_sqcka_protocol_parameters

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Parameters were not initialised yet
        else:

            # Return none
            return None

    # Initialise the Protocol, as its initial version, ready to be executed
    def initialise_protocol(self):

        # If the Protocol itself was not initialised yet
        if self.qiskit_sqcka_protocol_initialised is not True:

            # Create a boolean flag to check if it is possible to initialise the Protocol
            protocol_initialisation_flag = self.qiskit_sqcka_protocol_parameters_initialised \
                                           and self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised \
                                           and self.qiskit_sqcka_protocol_party_entities_initialised \
                                           and self.qiskit_sqcka_protocol_distributor_party_entity_initialised

            # If all the conditions for the initialisation of the Protocol are verified
            if protocol_initialisation_flag:

                # Retrieve the Party Entities' objects involved in the Protocol
                party_entities = self.get_protocol_party_entities()

                # Retrieve the Distributor Party Entity's objects involved in the Protocol
                distributor_party_entity = self.get_protocol_distributor_party_entity()

                # Retrieve the Bipartite Pre-Shared Keys involved in the Protocol
                bipartite_pre_shared_keys = self.get_protocol_bipartite_pre_shared_keys()

                # Retrieve the Parameters' configuration of the Protocol
                parameters = self.get_protocol_parameters()

                # Set the final object for the
                # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                # given its respective arguments
                self.qiskit_sqcka_protocol = QiskitSQCKAProtocol \
                    .QiskitSQCKAProtocol(party_entities, distributor_party_entity, bipartite_pre_shared_keys, parameters)

                # Delete obsolete attributes of the Class
                self.delete_obsolete_attributes()

                # Set the Protocol itself as being initialised,
                # putting the respective boolean flag as True
                self.qiskit_sqcka_protocol_initialised = True

            # If some condition for the initialisation of the Protocol is not verified
            else:

                # Raise the Value Error
                raise ValueError("Some configurations of the Protocol are not set yet!!!")

        # If the Protocol itself was already initialised yet
        else:

            # Raise a Value Error
            raise ValueError("The Protocol was already initialised!!!")

    # Delete obsolete attributes of the Class, after the Protocol be initialised
    def delete_obsolete_attributes(self):

        # Delete/Free the Distributor Party Entity of the Protocol
        del self.qiskit_sqcka_protocol_distributor_party_entity

        # Delete/Free the boolean flag for the initialisation of
        # the Distributor Party Entity of the Protocol
        del self.qiskit_sqcka_protocol_distributor_party_entity_initialised

        # Delete/Free the Bipartite Pre-Shared Keys used between
        # the Party Entities, involved in the Protocol
        del self.qiskit_sqcka_protocol_bipartite_pre_shared_keys

        # Delete/Free the boolean flag for the initialisation of
        # the Bipartite Pre-Shared Keys used between the Party Entities, involved in the Protocol
        del self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised

        # Delete/Free the Parameters of the Protocol
        del self.qiskit_sqcka_protocol_parameters

        # Delete/Free the boolean flag for the initialisation of Parameters of the Protocol
        del self.qiskit_sqcka_protocol_parameters_initialised

    # Start the execution process of the Protocol
    def start_protocol(self):

        # If the Semi-Quantum Conference Key Agreement (SQCKA) Protocol was not started yet
        if not self.qiskit_sqcka_protocol_started:

            # Retrieve the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            qiskit_sqcka_protocol = self.get_qiskit_sqcka_protocol()

            # Retrieve the number of Parties involved in
            # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            qiskit_sqcka_protocol_num_parties = qiskit_sqcka_protocol.get_parameters().get_num_parties()

            # Retrieve the number of Rounds for
            # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            qiskit_sqcka_protocol_num_rounds = qiskit_sqcka_protocol.get_parameters().get_num_rounds()

            # Retrieve the type of the Quantum Entanglement intended for
            # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            qiskit_sqcka_protocol_entanglement_type = \
                qiskit_sqcka_protocol.get_parameters().get_quantum_entanglement_type()

            # Set the number of Qubits required for the Quantum Circuits,
            # for the Rounds of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            num_qubits_and_bits_for_protocol_round_quantum_circuit = \
                ((3 * qiskit_sqcka_protocol_num_parties) - 2)

            # Retrieve the Distributor Party Entity of
            # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            qiskit_sqcka_protocol_distributor_party_entity = \
                self.qiskit_sqcka_protocol \
                .get_distributor_party_entity()

            # For each Round of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            for current_qiskit_sqcka_protocol_num_round in range(qiskit_sqcka_protocol_num_rounds):

                # Print the header of the current round of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                print("---------------------------- ROUND #{} ----------------------------"
                      .format(current_qiskit_sqcka_protocol_num_round))
                print("\n")

                # Create the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                sqcka_protocol_round = \
                    qiskit_sqcka_protocol_distributor_party_entity \
                    .create_protocol_round(current_qiskit_sqcka_protocol_num_round,
                                           num_qubits_and_bits_for_protocol_round_quantum_circuit)

                # Print the type of the current Round of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                print("This Round is a {}...".format(sqcka_protocol_round.get_type_round()))
                print("\n")

                # Prepare the Multipartite Entanglement of the Round for
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                sqcka_protocol_round = \
                    qiskit_sqcka_protocol_distributor_party_entity \
                    .prepare_quantum_entanglement(qiskit_sqcka_protocol_entanglement_type,
                                                  qiskit_sqcka_protocol_num_parties, sqcka_protocol_round)

                # Retrieve the Quantum Circuit for the previously
                # prepared Multipartite Entanglement of the Round for
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                quantum_entanglement_quantum_circuit = \
                    sqcka_protocol_round.get_qiskit_quantum_circuit()

                # Getting the Backend for the State Vector Representation
                # (i.e., the Quantum State represented as State Vector)
                state_vector_backend = Aer.get_backend('statevector_simulator')

                # Execute the Quantum Circuit and store the Quantum State in a final state vector
                final_state_vector = execute(quantum_entanglement_quantum_circuit.quantum_circuit,
                                             state_vector_backend).result().get_statevector()

                # Initialise the list for the valid Quantum States of
                # the previously prepared Multipartite Entanglement of the Round for
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                valid_quantum_states_binary_prepared_quantum_entanglement = []

                # Retrieve the list of the Party Entities of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                protocol_party_entities = self.get_protocol_party_entities()

                # Retrieve the number of the Party Entities of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                num_protocol_party_entities = len(protocol_party_entities)

                # Build the required Binary format for the possible valid Quantum States of
                # the previously prepared Multipartite Entanglement of the Round for
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                binary_format = "{0:0"
                binary_format += "{}".format(num_protocol_party_entities)
                binary_format += "b}"

                # For each coefficient of the State Vector of
                # the previously prepared Multipartite Entanglement of the Round for
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                for current_coefficient_state_vector_index in range(len(final_state_vector)):

                    # If the current coefficient of the State Vector of
                    # the previously prepared Multipartite Entanglement of the Round for
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol, is a valid one
                    if final_state_vector[current_coefficient_state_vector_index] != (0 + 0.0j):

                        # Convert the current valid Quantum State of
                        # the previously prepared Multipartite Entanglement of the Round for
                        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                        # to a Binary format
                        current_valid_quantum_state_prepared_quantum_entanglement_binary = \
                            binary_format.format(current_coefficient_state_vector_index)

                        # Append the current valid Quantum State of
                        # the previously prepared Multipartite Entanglement of the Round for
                        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                        # in a Binary format, to the list of valid ones
                        valid_quantum_states_binary_prepared_quantum_entanglement\
                            .append(current_valid_quantum_state_prepared_quantum_entanglement_binary)

                # Initialise the String representation of the Ket Notation of
                # the Quantum State for the previously prepared Multipartite Entanglement of
                # the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                prepared_quantum_entanglement_string_representation = "|Ψ⟩ = "

                # Retrieve the number of the valid Quantum States of
                # the previously prepared Multipartite Entanglement of the Round for
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                num_valid_quantum_states_prepared_quantum_entanglement = \
                    len(valid_quantum_states_binary_prepared_quantum_entanglement)

                # If there is only one valid Quantum States of
                # the previously prepared Multipartite Entanglement of the Round for
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                if num_valid_quantum_states_prepared_quantum_entanglement > 1:

                    # Append the coefficient of the Multipartite Entanglement to
                    # the String representation of the Ket Notation of
                    # the Quantum State for the previously prepared Multipartite Entanglement of
                    # the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    prepared_quantum_entanglement_string_representation += \
                        "1/sqrt({}) × (".format(num_valid_quantum_states_prepared_quantum_entanglement)

                # For each valid Quantum State in a Binary format of
                # the previously prepared Multipartite Entanglement of the Round for
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                for current_num_valid_quantum_state_binary_prepared_quantum_entanglement in \
                        range(num_valid_quantum_states_prepared_quantum_entanglement):

                    # Append the current valid Quantum State in a Binary format to
                    # the String representation of the Ket Notation of
                    # the Quantum State for the previously prepared Multipartite Entanglement of
                    # the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    prepared_quantum_entanglement_string_representation += \
                        "|{}⟩".format(valid_quantum_states_binary_prepared_quantum_entanglement[
                                         current_num_valid_quantum_state_binary_prepared_quantum_entanglement])

                    # If there is more than one valid Quantum State in a Binary format of
                    # the previously prepared Multipartite Entanglement of the Round for
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    if num_valid_quantum_states_prepared_quantum_entanglement > 1:

                        # If it is the last valid Quantum State in a Binary format of
                        # the previously prepared Multipartite Entanglement of the Round for
                        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        if (current_num_valid_quantum_state_binary_prepared_quantum_entanglement ==
                           (num_valid_quantum_states_prepared_quantum_entanglement - 1)):

                            # Append the last right parenthesis to the String representation of the Ket Notation of
                            # the Quantum State for the previously prepared Multipartite Entanglement of
                            # the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                            prepared_quantum_entanglement_string_representation += ")"

                        # If it is not the last valid Quantum State in a Binary format of
                        # the previously prepared Multipartite Entanglement of the Round for
                        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        else:

                            # Append the sum symbol to the String representation of the Ket Notation of
                            # the Quantum State for the previously prepared Multipartite Entanglement of
                            # the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                            prepared_quantum_entanglement_string_representation += " + "

                # Print the information about the previously prepared
                # Multipartite Entanglement, by the Distributor Party Entity,
                # of the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                print("{} (Distributor Party Entity) prepared the Multipartite Entanglement State ({}):\n- {}"
                      .format(qiskit_sqcka_protocol_distributor_party_entity
                              .get_party_user_client().get_user_client_name(),
                              qiskit_sqcka_protocol.get_parameters().get_quantum_entanglement_type(),
                              prepared_quantum_entanglement_string_representation))

                # Prepare the Multipartite Entanglement of the Round for
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                sqcka_protocol_round = \
                    qiskit_sqcka_protocol_distributor_party_entity \
                    .send_quantum_data_information_to_semi_quantum_party_entities(qiskit_sqcka_protocol_num_parties,
                                                                                  sqcka_protocol_round)

                # Print a blank line
                print("\n")

                # Print the information about the previously prepared
                # Multipartite Entanglement, by the Distributor Party Entity,
                # of the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                print("{} (Distributor Party Entity) send the Multipartite Entanglement State ({}),"
                      "\nto the respective Semi-Quantum Party Entities..."
                      .format(qiskit_sqcka_protocol_distributor_party_entity
                              .get_party_user_client().get_user_client_name(),
                              qiskit_sqcka_protocol.get_parameters().get_quantum_entanglement_type()))

                # For each Party Entity of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                for current_num_protocol_party_entity in range(num_protocol_party_entities):

                    # Retrieve the current Party Entity of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    current_protocol_party_entity = protocol_party_entities[current_num_protocol_party_entity]

                    # If the current Party Entity of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    # is not the Distributor Party Entity
                    if not current_protocol_party_entity.is_distributor():

                        # Receive the Quantum Data/Information from the current Party Entity of
                        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        sqcka_protocol_round = \
                            current_protocol_party_entity\
                            .receive_quantum_data_information_from_distributor(num_protocol_party_entities,
                                                                               sqcka_protocol_round)

                        # Print a blank line
                        print("\n")

                        # Print the information about the previously prepared
                        # Multipartite Entanglement, by the Distributor Party Entity,
                        # of the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        print("{} (Semi-Quantum Party Entity) received its Qubit (Particle) from"
                              "\nthe Multipartite Entanglement State ({}), from the Distributor Party Entity..."
                              .format(current_protocol_party_entity
                                      .get_party_user_client().get_user_client_name(),
                                      qiskit_sqcka_protocol.get_parameters().get_quantum_entanglement_type()))

                # Print a blank line
                print("\n")

                # For each Party Entity of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                for current_num_protocol_party_entity in range(num_protocol_party_entities):

                    # Retrieve the current Party Entity of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    current_protocol_party_entity = protocol_party_entities[current_num_protocol_party_entity]

                    # If the current Party Entity of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    # is not the Distributor Party Entity
                    if not current_protocol_party_entity.is_distributor():

                        # The current Party Entity Measure and Resend (SIFT Operation)
                        # or just Reflect (CTRL Operation) the Particle (Qubit),
                        # accordingly to the respective Bit of the Pre-Shared Key
                        sqcka_protocol_round = \
                            current_protocol_party_entity\
                            .measure_and_resend_or_reflect_qubit(num_protocol_party_entities,
                                                                 sqcka_protocol_round)

                # Execute the Quantum Circuit of the current Round of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                # for the case of it, being a Measure and Resend (SIFT Operation) Round
                sqcka_protocol_round = \
                    qiskit_sqcka_protocol_distributor_party_entity\
                    .execute_protocol_round_quantum_circuit_for_sift_rounds(num_protocol_party_entities,
                                                                            sqcka_protocol_round)

                # Retrieve the Results of the execution of the Quantum Circuit of the current Round of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                # for the the case of it, being a Measure and Resend (SIFT Operation) Round
                sqcka_protocol_round_results = sqcka_protocol_round.get_round_results()

                # If the results of the current Round of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol are not None,
                # and the current Round is a Measure and Resend (SIFT Operation) Round
                if (sqcka_protocol_round_results is not None) and \
                        (sqcka_protocol_round.get_type_round() == SIFT_MEASURE_AND_RESEND_ROUND_3):

                    # Print the Information about the obtained correlated state of
                    # the Measurement on the Multipartite Entanglement used
                    print("It was obtained the result: |{}⟩...".format(sqcka_protocol_round_results))

                    # Print a blank line
                    print("\n")

                # Reset the Qubits (Particles) on the Quantum Circuit of the current Round of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                # for the the case of it, being a Measure and Resend (SIFT Operation) Round
                sqcka_protocol_round = \
                    qiskit_sqcka_protocol_distributor_party_entity\
                    .reset_qubits_to_resend_for_sift_rounds(sqcka_protocol_round)

                # For each Party Entity of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                for current_num_protocol_party_entity in range(num_protocol_party_entities):

                    # Retrieve the current Party Entity of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    current_protocol_party_entity = protocol_party_entities[current_num_protocol_party_entity]

                    # Prepare the Qubits (Particles) on the Quantum Circuit of the current Round of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                    # for the the case of it, being a Measure and Resend (SIFT Operation) Round,
                    # in order to be sent back in the same state it were found, after the Measurement
                    sqcka_protocol_round = \
                        current_protocol_party_entity\
                        .prepare_qubits_to_be_sent_back_for_sift_rounds(num_protocol_party_entities,
                                                                        sqcka_protocol_round)

                # For each Party Entity of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                for current_num_protocol_party_entity in range(num_protocol_party_entities):

                    # Retrieve the current Party Entity of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    current_protocol_party_entity = protocol_party_entities[current_num_protocol_party_entity]

                    # If the current Party Entity of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    # is not the Distributor Party Entity
                    if not current_protocol_party_entity.is_distributor():

                        # The current Party Entity of
                        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                        # not being the Distributor Party Entity, send back the Qubits (Particles),
                        # to the Distributor Party Entity
                        sqcka_protocol_round = \
                            current_protocol_party_entity\
                            .send_back_quantum_data_information_to_distributor_party_entity(
                                num_protocol_party_entities, sqcka_protocol_round)

                        # If the current Round of
                        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        # is a Measure and Resend (SIFT Operation) Round
                        if sqcka_protocol_round.get_type_round() == SIFT_MEASURE_AND_RESEND_ROUND_3:

                            # Print the information about the previously prepared
                            # Multipartite Entanglement, by the Distributor Party Entity,
                            # of the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                            print("{} (Semi-Quantum Party Entity) sent back its recreated measured Qubit (Particle) of\n"
                                  "the Multipartite Entanglement State ({}), to the respective Distributor Party Entity..."
                                  .format(current_protocol_party_entity.get_party_user_client().get_user_client_name(),
                                          qiskit_sqcka_protocol.get_parameters().get_quantum_entanglement_type()))

                        # If the current Round of
                        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        # is a Reflect (CTRL Operation) Round
                        elif sqcka_protocol_round.get_type_round() == CTRL_REFLECT_ROUND_3:

                            # Print the information about the previously prepared
                            # Multipartite Entanglement, by the Distributor Party Entity,
                            # of the Round for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                            print("{} (Semi-Quantum Party Entity) sent back its unmeasured Qubit (Particle) of\n"
                                  "the Multipartite Entanglement State ({}), to the Distributor Party Entity..."
                                  .format(current_protocol_party_entity.get_party_user_client().get_user_client_name(),
                                          qiskit_sqcka_protocol.get_parameters().get_quantum_entanglement_type()))

                        # Print a blank line
                        print("\n")

                # The Distributor Party Entity of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                # receives back the Quantum Data/Information sent from the other Semi-Quantum Party Entities
                sqcka_protocol_round = \
                    qiskit_sqcka_protocol_distributor_party_entity \
                    .receive_back_quantum_data_information_from_semi_quantum_party_entities(
                        num_protocol_party_entities, sqcka_protocol_round)

                # If the Strategy for Eavesdropping Detection is a Measurement by Inverting Quantum Circuit
                if qiskit_sqcka_protocol.get_parameters().get_strategy_for_eavesdropping_detection() == \
                        StrategiesForEavesdroppingDetection.MEASUREMENT_BY_INVERTING_QUANTUM_CIRCUIT:

                    # The Distributor Party Entity of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    # invert and measure the Quantum Circuit containing the Quantum Data/Information reflected back
                    # from the other Semi-Quantum Party Entities, for the case of the Reflect (CTRL) Rounds
                    sqcka_protocol_round = \
                        qiskit_sqcka_protocol_distributor_party_entity \
                        .measure_quantum_entanglement_by_inverting_quantum_circuit(
                            qiskit_sqcka_protocol_entanglement_type,
                            num_protocol_party_entities, sqcka_protocol_round)

                    # If the current Round of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    # is a Reflect (CTRL) Round
                    if sqcka_protocol_round.get_type_round() == CTRL_REFLECT_ROUND_3:

                        # It was received the expected results for
                        # the Measurement performed on the Quantum Entanglement
                        if sqcka_protocol_round.get_round_results() == ("0" * num_protocol_party_entities):

                            # Print the information about the measured reflected Multipartite Entanglement State,
                            # sent back from the Semi-Quantum Party Entities to the Distributor Party Entity, for the case of,
                            # the current Round of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                            # be a Reflect (CTRL) Round
                            print("{} (Distributor Party Entity) measured "
                                  "the Multipartite Entanglement State ({}) reflected back,\n"
                                  "inverting the Quantum Circuit and it obtained the following state:\n- |{}⟩ (OK, as expected)\n"
                                  .format(qiskit_sqcka_protocol_distributor_party_entity
                                          .get_party_user_client().get_user_client_name(),
                                          qiskit_sqcka_protocol.get_parameters().get_quantum_entanglement_type(),
                                          sqcka_protocol_round.get_round_results()))

                        # It was not received the expected results for
                        # the Measurement performed on the Quantum Entanglement
                        else:

                            # Print the information about the measured reflected Multipartite Entanglement State,
                            # sent back from the Semi-Quantum Party Entities to the Distributor Party Entity, for the case of,
                            # the current Round of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                            # be a Reflect (CTRL) Round
                            print("{} (Distributor Party Entity) measured "
                                  "the Multipartite Entanglement State ({}) reflected back,\n"
                                  "inverting the Quantum Circuit and it obtained the following state:\n- |{}⟩ (NOT OK, not expected)\n"
                                  .format(qiskit_sqcka_protocol_distributor_party_entity
                                          .get_party_user_client().get_user_client_name(),
                                          qiskit_sqcka_protocol.get_parameters().get_quantum_entanglement_type(),
                                          sqcka_protocol_round.get_round_results()))

                            # Print the information about the Detection of Eavesdropping
                            print("ALERT: Eavesdropping detected!!!")

                # If the Strategy for Eavesdropping Detection is a SWAP Test
                elif qiskit_sqcka_protocol.get_parameters().get_strategy_for_eavesdropping_detection() == \
                    StrategiesForEavesdroppingDetection.SWAP_TEST:

                    # TODO - SWAP Test not done yet
                    return

                # If the Strategy for Eavesdropping Detection is a Statistical Test
                elif qiskit_sqcka_protocol.get_parameters().get_strategy_for_eavesdropping_detection() == \
                    StrategiesForEavesdroppingDetection.STATISTICAL_TEST:

                    # The Distributor Party Entity of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    # measure the Quantum Data/Information reflected back from the other Semi-Quantum Party Entities,
                    # for the case of the Reflect (CTRL) Rounds
                    sqcka_protocol_round = \
                        qiskit_sqcka_protocol_distributor_party_entity \
                        .measure_quantum_data_information_for_ctrl_rounds(
                            num_protocol_party_entities, sqcka_protocol_round)

                    # If the current Round of
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    # is a Reflect (CTRL) Round
                    if sqcka_protocol_round.get_type_round() == CTRL_REFLECT_ROUND_3:

                        # Print the information about the measured reflected Multipartite Entanglement State,
                        # sent back from the Semi-Quantum Party Entities to the Distributor Party Entity, for the case of,
                        # the current Round of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                        # be a Reflect (CTRL) Round
                        print("{} (Distributor Party Entity) measured "
                              "the Multipartite Entanglement State ({}) reflected back..."
                              .format(qiskit_sqcka_protocol_distributor_party_entity
                                      .get_party_user_client().get_user_client_name(),
                                      qiskit_sqcka_protocol.get_parameters().get_quantum_entanglement_type()))

                # Print the the separator for the current Round of
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                print("-------------------------------------------------------------------")
                print("\n")

            # Print multiple blank lines
            print("\n\n\n\n\n\n")
