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


# Class for IBM Qiskit's Parameters for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocolParameters:

    # Constructor for IBM Qiskit's Configuration for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def __init__(self, num_parties, num_rounds, num_quantum_communication_channels,
                 preparing_bases, quantum_entanglement_type):

        # Set the number of Parties
        self.num_parties = num_parties

        # Set the Number of Rounds
        self.num_rounds = num_rounds

        # Set the number of Quantum Communication Channels
        self.num_quantum_communication_channels = num_quantum_communication_channels

        # Create the list of Preparing Bases, in uppercase
        preparing_bases_upper = []

        # For each Preparing Base
        for preparing_base in preparing_bases:

            # Append the Preparing Base, in uppercase, to the list of Preparing Bases
            preparing_bases_upper.append(preparing_base.upper())

        # Set the Preparing Bases
        self.preparing_bases = preparing_bases_upper

        # Set the Quantum Entanglement Type to be used
        self.quantum_entanglement_type = quantum_entanglement_type.upper()

        # Set the probability of the all the receiving Parties reflect her destined Qubits,
        # in the same round of the Protocol, as the probability of occurrence of a X-Measurement Round happen
        self.probability_reflect_round = (1 / len(self.preparing_bases)) ** (self.num_parties - 1)

    # Return the number of Parties
    def get_num_parties(self):
        return self.num_parties

    # Return the number of Rounds
    def get_num_rounds(self):
        return self.num_rounds

    # Return the number of Quantum Communication Channels
    def get_num_quantum_communication_channels(self):
        return self.num_quantum_communication_channels

    # Return the Preparing Bases
    def get_preparing_bases(self):
        return self.preparing_bases

    # Return the Quantum Entanglement Type, being used
    def get_quantum_entanglement_type(self):
        return self.quantum_entanglement_type

    # Return the probability of the all the receiving Parties reflect her destined Qubits,
    # in the same round of the Protocol, as the probability of occurrence of a X-Measurement Round happen
    def get_probability_reflect_round(self):
        return self.probability_reflect_round

    # Print the information about
    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
    def print_info(self):

        # Print the number of Parties of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Num. Parties: {}".format(self.get_num_parties()))

        # Print the number of Rounds of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Num. Rounds: {}".format(self.get_num_rounds()))

        # Print the number of Quantum Communication Channels of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Num. Quantum Communication Channels: {}".format(self.get_num_quantum_communication_channels()))

        # Print the Preparing Bases of the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Preparing Bases: {}".format(self.get_preparing_bases()))

        # Print the Quantum Entanglement Type being used on the
        # IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Quantum Entanglement Type: {}".format(self.get_quantum_entanglement_type()))

        # Print the probability of the all the receiving Parties reflect her destined Qubits,
        # in the same round of the Protocol, as the probability of occurrence of a X-Measurement Round happen,
        # used on the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
        print(" - Probability of CTRL (Reflect without Measure in the Z-Basis): {}"
              .format(self.get_probability_reflect_round()))
