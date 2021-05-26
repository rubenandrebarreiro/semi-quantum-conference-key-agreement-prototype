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

# Import QuantumSignalVariableModeTypes from Common.Enumerations
from src.common.enumerations import QuantumSignalVariableModeTypes

# Import CommunicationPhysicalMediumTypes from Common.Enumerations
from src.common.enumerations import CommunicationPhysicalMediumTypes

# Import QuantumMeasurementBasisTypes from Common.Enumerations
from src.common.enumerations import QuantumMeasurementBasisTypes

# Import StrategiesForEavesdroppingDetection from Common.Enumerations
from src.common.enumerations import StrategiesForEavesdroppingDetection


# Constants

# The minimum number of necessary Parties for
# the IBM Qiskit's Parameters for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
MINIMUM_NUMBER_PARTIES = 2


# Class for IBM Qiskit's Parameters for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocolParameters:

    # Constructor for IBM Qiskit's Configuration for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def __init__(self, num_parties, num_rounds,
                 num_physical_quantum_communication_channels,
                 num_physical_classical_communication_channels,
                 quantum_signal_variable_mode_type,
                 communication_physical_medium_type,
                 preparing_bases, quantum_entanglement_type,
                 strategy_for_eavesdropping_detection,
                 communication_path_edges_between_parties_names=None,
                 communication_path_distances_between_parties_names=None):

        # If the number of Parties for the Protocol, is greater or equal than
        # the minimum number of necessary Parties for
        # the IBM Qiskit's Parameters for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        if num_parties >= MINIMUM_NUMBER_PARTIES:

            # If the Type of the Quantum Signal Variable Mode is valid
            if quantum_signal_variable_mode_type.upper() in \
               QuantumSignalVariableModeTypes.POSSIBLE_QUANTUM_SIGNAL_VARIABLE_MODES_TYPES:

                # If the Type of Communication Physical Medium is valid
                if communication_physical_medium_type.upper() in \
                   CommunicationPhysicalMediumTypes.POSSIBLE_COMMUNICATION_PHYSICAL_MEDIUM_TYPES:

                    # If the Strategy for Eavesdropping Detection is valid
                    if strategy_for_eavesdropping_detection in \
                        StrategiesForEavesdroppingDetection.POSSIBLE_STRATEGIES_FOR_EAVESDROPPING_DETECTION:

                        # Set the number of Parties
                        self.num_parties = num_parties

                        # Set the Number of Rounds
                        self.num_rounds = num_rounds

                        # Set the number of Physical Quantum Communication Channels
                        self.num_physical_quantum_communication_channels = \
                            num_physical_quantum_communication_channels

                        # Set the number of Physical Classical Communication Channels
                        self.num_physical_classical_communication_channels = \
                            num_physical_classical_communication_channels

                        # Set the Quantum Signal Variable Mode Type
                        self.quantum_signal_variable_mode_type = quantum_signal_variable_mode_type.upper()

                        # Set the Communication Physical Medium Type
                        self.communication_physical_medium_type = communication_physical_medium_type.upper()

                        # Create the list of Preparing Bases, in uppercase
                        preparing_bases_upper = []

                        # If it were provided some Preparing Bases for the Qubits
                        if preparing_bases is not None:

                            # For each Preparing Basis
                            for preparing_basis in preparing_bases:

                                # If the current Preparing Basis is valid
                                if preparing_basis.upper() in \
                                        QuantumMeasurementBasisTypes.POSSIBLE_QUANTUM_MEASUREMENT_BASIS_TYPES:

                                    # Append the current Preparing Basis, in uppercase,
                                    # to the list of Preparing Bases
                                    preparing_bases_upper.append(preparing_basis.upper())

                                # If the current Preparing Basis is not valid
                                else:

                                    # Raise a Value Error
                                    raise ValueError("The given Type of one of the Preparing Basis is not valid!!!")

                        # Set the Preparing Bases
                        self.preparing_bases = preparing_bases_upper

                        # Set the Quantum Entanglement Type to be used
                        self.quantum_entanglement_type = quantum_entanglement_type.upper()

                        # Set the Strategy for Eavesdropping Detection
                        self.strategy_for_eavesdropping_detection = strategy_for_eavesdropping_detection

                        # Set the probability of the all the receiving Parties reflect her destined Qubits,
                        # in the same round of the Protocol, as the probability of occurrence of
                        # a X-Measurement Round happen
                        self.probability_reflect_round = (1 / len(self.preparing_bases)) ** (self.num_parties - 1)

                        # If it will be used only one Communication Channel
                        if (self.num_physical_quantum_communication_channels == 1) and \
                                (self.num_physical_classical_communication_channels == 1):

                            # Retrieve the number of the Communication Path's Edges for the Parties' Names
                            num_communication_path_edges_between_parties_names = \
                                len(communication_path_edges_between_parties_names)

                            # If the number of the Communication Path's Edges for the Parties' Names
                            # are equal to the number of Parties
                            if num_communication_path_edges_between_parties_names == num_parties:

                                # Retrieve the 1st Path Edge of the Communication Path
                                first_path_edge = communication_path_edges_between_parties_names[0]

                                # Retrieve the last Path Edge of the Communication Path
                                last_path_edge = \
                                    communication_path_edges_between_parties_names[
                                        (num_communication_path_edges_between_parties_names - 1)
                                    ]

                                # If the 1st Party of the 1st Path Edge and
                                # the 2nd Party of the last 1st Path Edge of the Communication Path are the same
                                # (this is need to form closed cycle to simulate the go-and-back link
                                # from the Master Party to itself)
                                if first_path_edge[0].lower() == last_path_edge[1].lower():

                                    # Initialise a new Communication Path's Edges for the Parties' Names,
                                    # with all the Parties' Names of each Edge/Link, in lower case
                                    communication_path_edges_between_parties_names_all_lower = []

                                    # For each Edge/Link of the Communication Path between the Parties' Names
                                    for current_num_edge_link_parties_names in \
                                            range(num_communication_path_edges_between_parties_names):

                                        # Initialise the current Edge/Link of
                                        # the Communication Path between the Parties' Names, all in lower case
                                        current_edge_link_parties_names_lower = []

                                        # Retrieve the current Edge/Link of
                                        # the Communication Path between the Parties' Names
                                        current_edge_link_parties_names = \
                                            communication_path_edges_between_parties_names[
                                                current_num_edge_link_parties_names
                                            ]

                                        # Retrieve the Sender of the current Edge/Link of
                                        # the Communication Path between the Parties' Names
                                        sender_current_edge_link_parties_names = current_edge_link_parties_names[0]

                                        # Append the Sender of the current Edge/Link of
                                        # the Communication Path between the Parties' Names, in lower case
                                        current_edge_link_parties_names_lower\
                                            .append(sender_current_edge_link_parties_names.lower())

                                        # Retrieve the Receiver of the current Edge/Link of
                                        # the Communication Path between the Parties' Names
                                        receiver_current_edge_link_parties_names = current_edge_link_parties_names[1]

                                        # Append the Receiver of the current Edge/Link of
                                        # the Communication Path between the Parties' Names, in lower case
                                        current_edge_link_parties_names_lower\
                                            .append(receiver_current_edge_link_parties_names.lower())

                                        # Append the current Edge/Link to
                                        # the Communication Path between the Parties' Names, all in lower case
                                        communication_path_edges_between_parties_names_all_lower\
                                            .append(current_edge_link_parties_names_lower)

                                    # Set the Communication Path's Edges between the Parties' Names
                                    self.communication_path_edges_between_parties_names = \
                                        communication_path_edges_between_parties_names_all_lower

                                # If the 1st Party of the 1st Path Edge and
                                # the 2nd Party of the last 1st Path Edge of the Communication Path are not the same
                                # (this is need to form closed cycle to simulate the go-and-back link
                                # from the Master Party to itself)
                                else:

                                    # Raise a Value Error
                                    raise ValueError("The 1st Party of the 1st Path Edge and "
                                                     "the 2nd Party of the last 1st Path Edge of the Communication Path "
                                                     "need to be the same, to form a closed Cycle!!!")

                            # If the number of the Communication Path's Edges for the Parties' Names
                            # are not equal to the number of Parties
                            else:

                                # Raise a Value Error
                                raise ValueError("The Communication Path's Edges for the Parties' Names "
                                                 "must be equal to the number of Parties!!!")

                        # If it will be used more than one Communication Channel
                        elif (self.num_physical_quantum_communication_channels >= 1) and \
                             (self.num_physical_classical_communication_channels >= 1):

                            # Retrieve the number of the Communication Path's Edges for the Parties' Names
                            num_communication_path_edges_between_parties_names = \
                                len(communication_path_edges_between_parties_names)

                            # Retrieve the number of the Communication Path's Distances for the Parties' Names
                            num_communication_path_distances_between_parties_names = \
                                len(communication_path_distances_between_parties_names)

                            # If the number of the Communication Path's Edges for the Parties' Names
                            # are equal to the number of Parties and to the number of Distances involved
                            if ((num_communication_path_edges_between_parties_names // 2) == (num_parties - 1)) and \
                                    ((num_communication_path_edges_between_parties_names // 2) ==
                                     num_communication_path_distances_between_parties_names):

                                # Initialise a new Communication Path's Edges for the Parties' Names,
                                # with all the Parties' Names of each Edge/Link, in lower case
                                communication_path_edges_between_parties_names_all_lower = []

                                # For each Edge/Link of the Communication Path between the Parties' Names
                                for current_num_pair_edge_link_parties_names in \
                                        range(num_communication_path_edges_between_parties_names // 2):

                                    # Initialise the current Edge/Link of
                                    # the Communication Path between the Parties' Names, all in lower case #1
                                    current_edge_link_parties_names_lower_1 = []

                                    # Initialise the current Edge/Link of
                                    # the Communication Path between the Parties' Names, all in lower case #2
                                    current_edge_link_parties_names_lower_2 = []

                                    # Retrieve the current Edge/Link of
                                    # the Communication Path between the Parties' Names #1
                                    current_edge_link_parties_names_1 = \
                                        communication_path_edges_between_parties_names[
                                            (2 * current_num_pair_edge_link_parties_names)
                                        ]

                                    # Retrieve the current Edge/Link of
                                    # the Communication Path between the Parties' Names #2
                                    current_edge_link_parties_names_2 = \
                                        communication_path_edges_between_parties_names[
                                            ((2 * current_num_pair_edge_link_parties_names) + 1)
                                        ]

                                    # If the go-forward and go-back links are correct
                                    if (current_edge_link_parties_names_1[1] == current_edge_link_parties_names_2[0]) and \
                                            (current_edge_link_parties_names_1[0] == current_edge_link_parties_names_2[1]):

                                        # Retrieve the Sender of the current Edge/Link of
                                        # the Communication Path between the Parties' Names #1
                                        sender_current_edge_link_parties_names_1 = current_edge_link_parties_names_1[0]

                                        # Append the Sender of the current Edge/Link of
                                        # the Communication Path between the Parties' Names, in lower case #1
                                        current_edge_link_parties_names_lower_1 \
                                            .append(sender_current_edge_link_parties_names_1.lower())

                                        # Retrieve the Receiver of the current Edge/Link of
                                        # the Communication Path between the Parties' Names #1
                                        receiver_current_edge_link_parties_names_1 = current_edge_link_parties_names_1[1]

                                        # Append the Receiver of the current Edge/Link of
                                        # the Communication Path between the Parties' Names, in lower case #1
                                        current_edge_link_parties_names_lower_1 \
                                            .append(receiver_current_edge_link_parties_names_1.lower())

                                        # Retrieve the Sender of the current Edge/Link of
                                        # the Communication Path between the Parties' Names #2
                                        sender_current_edge_link_parties_names_2 = current_edge_link_parties_names_2[0]

                                        # Append the Sender of the current Edge/Link of
                                        # the Communication Path between the Parties' Names, in lower case #2
                                        current_edge_link_parties_names_lower_2 \
                                            .append(sender_current_edge_link_parties_names_2.lower())

                                        # Retrieve the Receiver of the current Edge/Link of
                                        # the Communication Path between the Parties' Names #2
                                        receiver_current_edge_link_parties_names_2 = current_edge_link_parties_names_2[1]

                                        # Append the Receiver of the current Edge/Link of
                                        # the Communication Path between the Parties' Names, in lower case #2
                                        current_edge_link_parties_names_lower_2 \
                                            .append(receiver_current_edge_link_parties_names_2.lower())

                                        # Append the current Edge/Link to
                                        # the Communication Path between the Parties' Names, all in lower case #1
                                        communication_path_edges_between_parties_names_all_lower \
                                            .append(current_edge_link_parties_names_lower_1)

                                        # Append the current Edge/Link to
                                        # the Communication Path between the Parties' Names, all in lower case #2
                                        communication_path_edges_between_parties_names_all_lower \
                                            .append(current_edge_link_parties_names_lower_2)

                                    # If the go-forward and go-back links are not correct
                                    else:

                                        # Raise a Value Error
                                        raise ValueError("The Go-Forward and Go-Back Communication Paths are not valid!!!")

                                # Set the Communication Path's Edges between the Parties' Names
                                self.communication_path_edges_between_parties_names = \
                                    communication_path_edges_between_parties_names_all_lower

                                # Set the Communication Path's Distances between the Parties' Names
                                self.communication_path_distances_between_parties_names = \
                                    communication_path_distances_between_parties_names

                            # If the number of the Communication Path's Edges for the Parties' Names
                            # are not equal to the number of Parties and to the number of Distances involved
                            else:

                                # Raise a Value Error
                                raise ValueError("The Communication Path's Edges for the Parties' Names "
                                                 "must be equal to the number of Parties!!!")

                    # If the Strategy for Eavesdropping Detection is not valid
                    else:

                        # Raise a Runtime Error
                        raise RuntimeError("The Strategy for Eavesdropping Detection is not valid!!!")

                # If the Type of the Communication Physical Medium is not valid
                else:

                    # Raise a Value Error
                    raise ValueError("The given Type of Communication Physical Medium is not valid!!!")

            # If the Type of the Quantum Signal Variable Mode is not valid
            else:

                # Raise a Value Error
                raise ValueError("The given Type of Quantum Signal Variable Mode is not valid!!!")

        # If the number of Parties for the Protocol, is lower than
        # the minimum number of necessary Parties for
        # the IBM Qiskit's Parameters for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
        else:

            # Raise a Value Error
            raise ValueError("The minimum number of Parties for "
                             "the Semi-Quantum Conference Key Agreement (SQCKA) Protocol is {}!!!"
                             .format(MINIMUM_NUMBER_PARTIES))

    # Return the number of Parties
    def get_num_parties(self):
        return self.num_parties

    # Return the number of Rounds
    def get_num_rounds(self):
        return self.num_rounds

    # Return the number of Physical Quantum Communication Channels
    def get_num_physical_quantum_communication_channels(self):
        return self.num_physical_quantum_communication_channels

    # Return the number of Physical Classical Communication Channels
    def get_num_physical_classical_communication_channels(self):
        return self.num_physical_classical_communication_channels

    # Return the type of the Quantum Signal Variable Mode
    def get_quantum_signal_variable_mode_type(self):
        return self.quantum_signal_variable_mode_type

    # Return the type of the Communication Physical Medium
    def get_communication_physical_medium_type(self):
        return self.communication_physical_medium_type

    # Return the Preparing Bases
    def get_preparing_bases(self):
        return self.preparing_bases

    # Return the Quantum Entanglement Type, being used
    def get_quantum_entanglement_type(self):
        return self.quantum_entanglement_type

    # Return the Strategy for Eavesdropping Detection
    def get_strategy_for_eavesdropping_detection(self):
        return self.strategy_for_eavesdropping_detection

    # Return the probability of the all the receiving Parties reflect her destined Qubits,
    # in the same round of the Protocol, as the probability of occurrence of a X-Measurement Round happen
    def get_probability_reflect_round(self):
        return self.probability_reflect_round

    # Return the Communication Path's Edges between the Parties' Names
    def get_communication_path_edges_between_parties_names(self):
        return self.communication_path_edges_between_parties_names

    # Return the Communication Path's Distances between the Parties' Names
    def get_communication_path_distances_between_parties_names(self):
        return self.communication_path_distances_between_parties_names

    # Print the information about
    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
    def print_info(self):

        # Print the number of Parties of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Num. Parties: {}".format(self.get_num_parties()))

        # Print the number of Rounds of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Num. Rounds: {}".format(self.get_num_rounds()))

        # Print the number of Physical Quantum Communication Channels of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Num. Physical Quantum Communication Channels: {}"
              .format(self.get_num_physical_quantum_communication_channels()))

        # Print the number of Physical Classical Communication Channels of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Num. Physical Classical Communication Channels: {}"
              .format(self.get_num_physical_classical_communication_channels()))

        # Print the type of the Quantum Signal Variable Mode of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Quantum Signal Variable Mode Type: {}"
              .format(self.get_quantum_signal_variable_mode_type()))

        # Print the type of the Communication Physical Medium of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Communication Physical Medium Type: {}"
              .format(self.get_communication_physical_medium_type()))

        # Print the Preparing Bases of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Preparing Bases: {}".format(self.get_preparing_bases()))

        # Print the Quantum Entanglement Type being used on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Quantum Entanglement Type: {}".format(self.get_quantum_entanglement_type()))

        # Print the Strategy for the Eavesdropping Detection used on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Strategy for Eavesdropping Detection: {}"
              .format(self.get_strategy_for_eavesdropping_detection()))

        # Print the probability of the all the receiving Parties reflect her destined Qubits,
        # in the same round of the Protocol, as the probability of occurrence of a X-Measurement Round happen,
        # used on the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Probability of CTRL (Reflect without Measure in the Z-Basis): {}"
              .format(self.get_probability_reflect_round()))

        # If it will be used only one Communication Channel
        if (self.num_physical_quantum_communication_channels == 1) and \
                (self.num_physical_classical_communication_channels == 1):

            # Initialise the String for the representation of
            # the Communication Path between the Parties' Names
            communication_path_edges_for_parties_names_string = "[ "

            # For each Edge/Link of the Communication Path between the Parties' Names
            for current_num_edge_link_parties_names in range(len(self.communication_path_edges_between_parties_names)):

                # Retrieve the current Edge/Link of the Communication Path between the Parties' Names
                current_edge_link_parties_names = \
                    self.communication_path_edges_between_parties_names[current_num_edge_link_parties_names]

                # The Sender Party Name of the current Edge/Link of
                # the Communication Path between the Parties' Names
                sender_party_name = current_edge_link_parties_names[0]

                # The Receiver Party Name of the current Edge/Link of
                # the Communication Path between the Parties' Names
                receiver_party_name = current_edge_link_parties_names[1]

                # Append the current Edge/Link Pair to the String for the representation of
                # the Communication Path between the Parties' Names
                communication_path_edges_for_parties_names_string += \
                    "({} → {})".format(sender_party_name, receiver_party_name)

                # If the current Edge/Link of the Communication Path between the Parties' Names is not the last one
                if current_num_edge_link_parties_names != \
                        (len(self.communication_path_edges_between_parties_names) - 1):

                    # Append a comma (;) to the String for the representation of
                    # the Communication Path between the Parties' Names
                    communication_path_edges_for_parties_names_string += "; "

            # Complete the String for the representation of
            # the Communication Path between the Parties' Names
            communication_path_edges_for_parties_names_string += " ]"

            # Print the the String for the representation of the Communication Path between the Parties' Names,
            # to be used on the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
            print(" - Communication Path between the Parties' Names: {}"
                  .format(communication_path_edges_for_parties_names_string))
