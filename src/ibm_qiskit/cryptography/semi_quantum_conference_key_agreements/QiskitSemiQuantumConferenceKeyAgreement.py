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


# Class for IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA)
class QiskitSemiQuantumConferenceKeyAgreement:

    # Constructor for IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA)
    def __init__(self, num_rounds, parties_names, party_name_master,
                 num_quantum_communication_channels, preparing_bases, quantum_entanglement_type):

        # The number of the rounds for the protocol
        self.num_rounds = num_rounds

        # Create the list of Parties' Names
        parties_names_upper = []

        # For each Party Name
        for party_name in parties_names:

            # Append the Party Name, in uppercase, to the list of Parties' Names
            parties_names_upper.append(party_name.upper())

        # Set the Parties' Names
        self.parties_names = parties_names_upper

        # Set the number of Parties
        self.num_parties = len(self.parties_names)

        # Change the Party's Name, for the uppercase
        party_name_master_upper = party_name_master.upper()

        # If the Party Name, responsible for the distribution of the Common Secret Key (Conference Key),
        # is not present in the list of Parties' Names involved
        if party_name_master_upper not in self.parties_names:

            # Raise the Value Error exception
            raise ValueError("The Party Name specified to be the Master "
                             "(i.e., the party responsible for the distribution of the Common Secret Key "
                             "(Conference Key) between the parties involved is not present in "
                             "the list of Parties' Names involved!!!")

        # If the Party Name, responsible for the distribution of the Common Secret Key (Conference Key),
        # is present in the list of Parties' Names involved
        else:

            # Set the Party's Name being the Master of the protocol
            self.party_name_master = party_name_master

        # The number of Quantum Communication Channels
        self.num_quantum_communication_channels = num_quantum_communication_channels

        # If the number of Quantum Communication Channels used is just one,
        # it is necessary to established time slots for each particle of the Party, in each round of the protocol
        if self.num_quantum_communication_channels == 1:

            # Set the total number of time slots
            self.num_time_slots = ((self.num_parties - 1) * self.num_rounds)

        # If the number of Quantum Communication Channels used is equal to the number of parties involved,
        # it is necessary to established time slots for each particle of the Party, in each round of the protocol
        elif self.num_quantum_communication_channels == self.num_parties:

            # Set the total number of time slots, as the number of rounds
            self.num_time_slots = num_rounds

        # TODO - Something else, regarding the number of time slots

        # The attribution of the Time Slots, for the several rounds of the protocol
        self.time_slots_attributions = []

        # Create the list of Preparing/Measurement Bases used for the protocol (i.e., X-, Y- and/or Z-Basis)
        preparing_bases_upper = []

        # For each Preparing/Measurement Basis
        for preparing_base in preparing_bases:

            # Append the Preparing/Measurement Basis, in uppercase,
            # to the list of Bases used in the protocol (i.e., X-, Y- and/or Z-Basis)
            preparing_bases_upper.append(preparing_base.upper())

        # Set the Preparing/Measurement Bases used for the protocol (i.e., X-, Y- and/or Z-Basis)
        self.preparing_bases_upper = preparing_bases_upper

        # The type of Entanglement used for the protocol (i.e., GHZ, W or Graph States)
        self.quantum_entanglement_type = quantum_entanglement_type.upper()
