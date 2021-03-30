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

# Import GHZ_STATE ID from IBM_Qiskit.Common.QuantumEntanglementTypes
from src.ibm_qiskit.common.QuantumEntanglementTypes import GHZ_STATE

# Import Utilities from IBM_Qiskit.Common.Utilities
from src.ibm_qiskit.common.Utilities import Utilities


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

        """ 2) Creation of 'artificial' Bipartite Pre-Shared Key Pairs, between the Parties """

        # Retrieve the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        qiskit_sqcka_protocol_parameters = \
            qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state \
            .get_protocol_parameters()

        # The name of the Parties involved in the Protocol
        parties_names = ["Alice", "Bob_1", "Bob_2"]

        # The name of the Master Party of the Protocol
        master_party_name = "Alice"

        # Retrieve the number of Rounds of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        qiskit_sqcka_protocol_num_rounds = qiskit_sqcka_protocol_parameters.get_num_rounds()

        # Retrieve the number of Parties of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        qiskit_sqcka_protocol_num_parties = qiskit_sqcka_protocol_parameters.get_num_parties()

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

                # For each Pair of names of the Party owners of the Bipartite Pre-Shared Key Pair
                for bipartite_party_pair_names in bipartite_party_pairs_names:

                    # Create the IBM Qiskit's Quantum True Random Binary String Generator
                    qiskit_quantum_true_random_binary_string_generator = \
                        QiskitQuantumTrueRandomBinaryStringGenerator\
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

                    # The name of the Party #1 and #2
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

                    # Add the previously created Bipartite Pre-Shared Key to
                    # the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
                    qiskit_sqcka_protocol_executor_service_16_rounds_3_parties_2_bases_1_channel_ghz_state\
                        .add_protocol_bipartite_pre_shared_key(party_name_1, party_name_2, bipartite_pre_shared_key)

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

            # Print the header of the 2nd Logging
            print("\n\n--- 2) BIPARTITE PRE-SHARED KEY PAIRS OF THE PROTOCOL ---\n")

            # For each Bipartite Pre-Shared Key
            for current_num_bipartite_pre_shared_key in range(num_bipartite_pre_shared_keys):

                # Print the sub-header for the current Bipartite Pre-Shared Key
                print("Bipartite Pre-Shared Key Pair #{}:".format((current_num_bipartite_pre_shared_key + 1)))

                # Retrieve the current Bipartite Pre-Shared Key
                current_bipartite_pre_shared_key = \
                    qiskit_sqcka_protocol_bipartite_pre_shared_keys[current_num_bipartite_pre_shared_key]

                # Print the information about
                # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
                # current Bipartite Pre-Shared Key
                current_bipartite_pre_shared_key.print_info()

                # Dummy print, to add a blank line
                print()

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
