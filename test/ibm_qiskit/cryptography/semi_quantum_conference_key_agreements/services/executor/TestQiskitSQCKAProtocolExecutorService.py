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

# Import Unittest for Python's Unitary Tests
import unittest

# Import Combinations from IterationTools Python's Library
from itertools import combinations

# Import Ceil from Math Python's Library
from math import ceil

# Import QiskitSQCKAProtocolExecutorService from IBM_Qiskit.Cryptography.SemiQuantumConferenceKeyAgreement
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreement\
    .services.executor.QiskitSQCKAProtocolExecutorService import \
    QiskitSQCKAProtocolExecutorService

# Import QiskitQuantumTrueRandomBinaryStringGenerator from IBM_Qiskit.Utils.Random_Generator.Binary.Quantum
from src.ibm_qiskit.utils.random_generator.binary.quantum import \
    QiskitQuantumTrueRandomBinaryStringGenerator

# Import Qiskit_Default_Num_Counts from IBM_Qiskit.Common.QiskitLibraryParameters
from src.ibm_qiskit.common.QiskitLibraryParameters import QISKIT_DEFAULT_NUM_COUNTS

# Import GHZ_STATE ID from Common.QuantumEntanglementTypes
from src.common.enumerations.QuantumEntanglementTypes import GHZ_STATE

# Import the User/Client from Common.Communication
from src.common.communication import UserClient

# Import Utilities from Common.Utilities
from src.common.utils.Utilities import Utilities


# Constants

# The Flag for the prints of Logging
LOGGING_FLAG = True


# Class
class MyTestCase(unittest.TestCase):

    def test_qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state(self):

        """ 1) Configuration of the Protocol's Parameters """

        # The number of Parties
        num_parties = 3

        # The number of Rounds
        num_rounds = 16

        # The number of Quantum Communication Channels
        num_quantum_communication_channels = 1

        # The Preparing Bases being used for the Protocol
        preparing_bases = ["X", "Z"]

        # The Quantum Entanglement Type, being used on the Protocol
        quantum_entanglement_type = GHZ_STATE

        # Create the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol Executor Service
        qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state = \
            QiskitSQCKAProtocolExecutorService()

        # Initialise the Protocol's Parameters for
        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol Executor Service
        qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
            .configure_protocol_parameters(num_parties, num_rounds, num_quantum_communication_channels,
                                           preparing_bases, quantum_entanglement_type)

        # If the boolean flag for the Logging printing is set to True
        if LOGGING_FLAG:

            # Retrieve the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
            qiskit_sqcka_protocol_parameters = \
                qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
                .get_protocol_parameters()

            # Print the header of the 1st Logging
            print("\n\n--- 1) CONFIGURED PARAMETERS OF THE PROTOCOL ---\n")

            # Print the sub-header for the information of
            # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
            print("The information of the Protocol's Parameters:")

            # Print the information about
            # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
            qiskit_sqcka_protocol_parameters.print_info()

        """ 2) Creation of the User/Clients """

        # The name of the Parties involved in the Protocol
        parties_names = ["Alice", "Bob_1", "Bob_2"]

        # Retrieve the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        qiskit_sqcka_protocol_parameters = \
            qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state \
            .get_protocol_parameters()

        # Retrieve the number of Parties of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        qiskit_sqcka_protocol_num_parties = qiskit_sqcka_protocol_parameters.get_num_parties()

        # The User/Clients of the Parties involved in the Protocol
        users_clients = []

        # For each Party involved in the Protocol
        for num_party in range(qiskit_sqcka_protocol_num_parties):

            # Create the respective User/Client,
            # with the name of the respective Party
            user_client = UserClient.UserClient(parties_names[num_party])

            # Append the previously created User/Client
            users_clients.append(user_client)

        # Print the header of the 2nd Logging
        print("\n\n--- 2) CONFIGURED USERS/CLIENTS OF THE PROTOCOL ---\n")

        # Print the sub-header for the information of the Users/Clients configured for the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print("The information of the Users/Clients Configured:\n")

        # For each User/Client involved in
        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        for num_user_client in range(len(users_clients)):

            # Print the number of the current User/Client
            print("User/Client #{}:".format((num_user_client + 1)))

            # Print the information about the User/Client
            users_clients[num_user_client].print_info()

        """ 3) Creation of 'artificial' Bipartite Pre-Shared Key Pairs, between the Parties """

        # The name of the Master Party of the Protocol
        master_party_name = "Alice"

        # Retrieve the number of Rounds of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        qiskit_sqcka_protocol_num_rounds = qiskit_sqcka_protocol_parameters.get_num_rounds()

        # Retrieve the probability of the all the receiving Parties reflect her destined Qubits,
        # in the same round of the Protocol, as the probability of occurrence of a X-Measurement Round happen
        # for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        qiskit_sqcka_protocol_probability_reflect_round = \
            qiskit_sqcka_protocol_parameters.get_probability_reflect_round()

        # Compute the number of Rounds that each Party will reflect the Qubits, without performing Z-Basis Measurement
        qiskit_sqcka_protocol_num_reflect_rounds = \
            ceil(qiskit_sqcka_protocol_probability_reflect_round * qiskit_sqcka_protocol_num_rounds)

        # If the number of the Parties involved in the Protocol are correct and well configured
        if qiskit_sqcka_protocol_num_parties == len(parties_names):

            # Create an empty list for the name of the Parties owners of the Bipartite Party Pairs
            bipartite_party_pairs_names = []

            # For each pair of the names of the Parties, involved in each valid Bipartite Pre-Shared Key
            for bipartite_party_pair_names in combinations(parties_names, 2):

                # Only if one of the names of the owner Parties is the same name of the Master Party
                if (bipartite_party_pair_names[0] is master_party_name) or \
                        (bipartite_party_pair_names[1] is master_party_name):

                    # Append the names of the Parties of the Bipartite Pre-Shared Key Pair to
                    # the list for the name of the Parties owners of the Bipartite Party Pairs
                    bipartite_party_pairs_names.append(bipartite_party_pair_names)

            # If all the names of the Parties owners of the Bipartite Pre-Shared Key Pairs were fulfilled
            if len(bipartite_party_pairs_names) == (qiskit_sqcka_protocol_num_parties - 1):

                # Create the IBM Qiskit's Quantum True Random Binary String Generator
                qiskit_quantum_true_random_binary_string_generator = \
                    QiskitQuantumTrueRandomBinaryStringGenerator \
                    .QiskitQuantumTrueRandomBinaryStringGenerator(
                        "qiskit_quantum_true_random_binary_string_generator",
                        num_rounds, QISKIT_DEFAULT_NUM_COUNTS
                    )

                # Forever loop, to be broken when the Hamming Weight is equal to
                # the number of Rounds that each Party will reflect the Qubits,
                # without performing Z-Basis Measurement
                while True:

                    # Create the Bipartite Pre-Shared Key, in binary,
                    # from the IBM Qiskit's Quantum True Random Binary String Generator
                    bipartite_pre_shared_key = \
                        qiskit_quantum_true_random_binary_string_generator.generate_true_random_binary_string()

                    # Compute the Hamming Weight of the previously created Bipartite Pre-Shared Key, in binary,
                    # from the IBM Qiskit's Quantum True Random Binary String Generator
                    bipartite_pre_shared_key_hamming_weight = \
                        Utilities.compute_hamming_weight(bipartite_pre_shared_key)

                    # If the Hamming Weight of the previously created Bipartite Pre-Shared Key, in binary,
                    # from the IBM Qiskit's Quantum True Random Binary String Generator, is equal to
                    # the number of Rounds that each Party will reflect the Qubits,
                    # without performing Z-Basis Measurement
                    if bipartite_pre_shared_key_hamming_weight == qiskit_sqcka_protocol_num_reflect_rounds:

                        # Break the forever loop
                        break

                # For each Pair of names of the Party owners of the Bipartite Pre-Shared Key Pair
                for bipartite_party_pair_names in bipartite_party_pairs_names:

                    # Initialise the names of the Parties of the Pair of Owners
                    party_name_1 = party_name_2 = None

                    # If the name of the Party #1 of the Pair of Owners is the name of the Master Party
                    if (bipartite_party_pair_names[0].upper() == master_party_name.upper()) and \
                            (bipartite_party_pair_names[1].upper() != master_party_name.upper()):

                        # Set the name of the Party #1
                        party_name_1 = bipartite_party_pair_names[0]

                        # Set the name of the Party #2
                        party_name_2 = bipartite_party_pair_names[1]

                    # If the name of the Party #2 of the Pair of Owners is the name of the Master Party
                    elif (bipartite_party_pair_names[0].upper() != master_party_name.upper()) and \
                            (bipartite_party_pair_names[1].upper() == master_party_name.upper()):

                        # Set the name of the Party #1
                        party_name_1 = bipartite_party_pair_names[1]

                        # Set the name of the Party #2
                        party_name_2 = bipartite_party_pair_names[0]

                    # Initialise the Users/Clients of the Pair of Owners
                    user_client_1 = user_client_2 = None

                    # For each User/Client involved in
                    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    for num_user_client in range(len(users_clients)):

                        # If the current User/Client has the same name of the Party #1
                        if users_clients[num_user_client].get_user_client_name() == party_name_1.lower():

                            # Set the User/Client #1
                            user_client_1 = users_clients[num_user_client]

                        # If the current User/Client has the same name of the Party #2
                        if users_clients[num_user_client].get_user_client_name() == party_name_2.lower():

                            # Set the User/Client #2
                            user_client_2 = users_clients[num_user_client]

                    # Add the previously created Bipartite Pre-Shared Key to
                    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
                        .add_protocol_bipartite_pre_shared_key(user_client_1, user_client_2,
                                                               bipartite_pre_shared_key)

                # Set the Bipartite Pre-Shared Keys of
                # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol, as initialised
                qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
                    .set_protocol_bipartite_pre_shared_keys_initialised()

            # If some name of a Party owners of in the Bipartite Pre-Shared key Pairs were not fulfilled
            else:

                # Raise a Value Error
                raise ValueError("The number of the names of the Parties owners of "
                                 "the Bipartite Pre-Shared Key Pairs are not correct!!!")

        # If the number of the Parties involved in the Protocol are not correct and well configured
        else:

            # Raise a Value Error
            raise ValueError("The Parameter of the number of Parties for the Test is wrong!!!")

        # If the boolean flag for the Logging printing is set to True
        if LOGGING_FLAG:

            # Retrieve the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
            # Bipartite Pre-Shared Keys
            qiskit_sqcka_protocol_bipartite_pre_shared_keys = \
                qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
                .get_protocol_bipartite_pre_shared_keys()

            # Retrieve the number of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
            # Bipartite Pre-Shared Keys
            num_bipartite_pre_shared_keys = len(qiskit_sqcka_protocol_bipartite_pre_shared_keys)

            # Print the header of the 3rd Logging
            print("\n\n--- 3) BIPARTITE PRE-SHARED KEY PAIRS OF THE PROTOCOL ---\n")

            # For each Bipartite Pre-Shared Key
            for current_num_bipartite_pre_shared_key in range(num_bipartite_pre_shared_keys):

                # Print the sub-header for the current Bipartite Pre-Shared Key
                print("Bipartite Pre-Shared Key Pair #{} (Hamming Weight = {}):"
                      .format((current_num_bipartite_pre_shared_key + 1), qiskit_sqcka_protocol_num_reflect_rounds))

                # Retrieve the current Bipartite Pre-Shared Key
                current_bipartite_pre_shared_key = \
                    qiskit_sqcka_protocol_bipartite_pre_shared_keys[current_num_bipartite_pre_shared_key]

                # Print the information about
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
                # current Bipartite Pre-Shared Key
                current_bipartite_pre_shared_key.print_info()

        """ 4) Creation of the Parties involved on the Protocol """

        # Retrieve the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Bipartite Pre-Shared Keys
        bipartite_pre_shared_keys = \
            qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state \
            .get_protocol_bipartite_pre_shared_keys()

        # Set the Parties (including the Master Party) of
        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
        # alongside the Bipartite Pre-Shared Keys they own/possess
        qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
            .set_protocol_parties(users_clients, parties_names, master_party_name, bipartite_pre_shared_keys)

        # If the boolean flag for the Logging printing is set to True
        if LOGGING_FLAG:

            # Retrieve the Parties of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            protocol_parties = \
                qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
                .get_protocol_parties()

            # Retrieve the number of Parties of
            # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            num_protocol_parties = len(protocol_parties)

            # Print the header of the 4th Logging
            print("\n\n--- 4) PARTIES INVOLVED IN THE PROTOCOL ---\n")

            # For each Party of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            for current_num_protocol_party in range(num_protocol_parties):

                # Print the information about the current Party of the
                # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                protocol_parties[current_num_protocol_party].print_info()

            # Retrieve the Master Party of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            protocol_master_party = \
                qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
                .get_protocol_master_party()

            # Print the header of the 4th Logging
            print("\n\n--- 4) MASTER PARTY INVOLVED IN THE PROTOCOL ---\n")

            # Print the information about the Master Party of the
            # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            protocol_master_party.print_info()

        """ 5) Initialisation of the final object for
        the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol """

        # Initialise the final object for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state.initialise_protocol()

        # Print the header of the 5th Logging
        print("\n\n--- 5) THE PROTOCOL WAS INITIALISED ---\n")

        """ 6) Configuration of the Nodes for the parties involved in
        the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol """

        # Configure the Nodes for the final Parties of
        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
            .configure_protocol_nodes()

        # Print the header of the 6th Logging
        print("\n\n--- 6) NODES CONFIGURED FOR THE PARTIES INVOLVED IN THE PROTOCOL ---\n")

        # Retrieve the previously configured Nodes for the Parties involved in
        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        protocol_configured_nodes = \
            qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
            .get_protocol_configured_nodes()

        # Retrieve the number of previously configured Nodes for the Parties involved in
        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        num_protocol_configured_nodes = len(protocol_configured_nodes)

        # For the previously configured Nodes for each Party involved in
        # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        for current_num_protocol_configured_node in range(num_protocol_configured_nodes):

            # Print the information of the current configured Node for the respective Party involved in
            # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
            protocol_configured_nodes[current_num_protocol_configured_node].print_info()

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
