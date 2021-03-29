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

# Import the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Party
# from IBM Qiskit's Cryptography.Semi_Quantum_Conference_Key_Agreement.Common Module
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreements.common.QiskitSQCKAProtocolParty import \
    QiskitSQCKAProtocolParty


# Class for IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA)
class QiskitSQCKAProtocol:

    # Constructor for IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA)
    def __init__(self, num_rounds, parties_names, party_name_master, bipartite_pre_shared_keys,
                 num_quantum_communication_channels, preparing_bases, quantum_entanglement_type):

        # The number of the rounds for the protocol
        self.num_rounds = num_rounds

        # Create the list of Parties' Names
        parties_names_upper = []

        # For each Party Name
        for party_name in parties_names:

            # Append the Party Name, in uppercase, to the list of Parties' Names
            parties_names_upper.append(party_name.upper())

        # Change the Party's Name, for the uppercase
        party_name_master_upper = party_name_master.upper()

        # If the Party Name, responsible for the distribution of the Common Secret Key (Conference Key),
        # is not present in the list of Parties' Names involved
        if party_name_master_upper not in parties_names_upper:

            # Raise the Value Error exception
            raise ValueError("The Party Name specified to be the Master "
                             "(i.e., the party responsible for the distribution of the Common Secret Key "
                             "(Conference Key) between the parties involved is not present in "
                             "the list of Parties' Names involved on the Protocol!!!")

        # Retrieve the number of parties involved in the Protocol
        num_parties = len(parties_names_upper)

        # The Dictionary for the Parties involved in the Protocol
        self.parties = {}

        # For each Party involved in the Protocol
        for current_party_id in range(num_parties):

            # Retrieve the name of the current Party
            current_party_name = parties_names_upper[current_party_id]

            # If the current Party is the Master Party
            if current_party_name.upper() == party_name_master_upper.upper():

                # Initialize the object of the Party, as the Master Party
                self.parties[current_party_id] = QiskitSQCKAProtocolParty(current_party_id, current_party_name.upper(),
                                                                          True,
                                                                          bipartite_pre_shared_keys[current_party_id])

            # If the current Party is not the Master Party
            else:

                # Initialize the object of the Party, as a Normal Party
                self.parties[current_party_id] = QiskitSQCKAProtocolParty(current_party_id, current_party_name.upper(),
                                                                          False,
                                                                          bipartite_pre_shared_keys[current_party_id])

        # The number of Quantum Communication Channels
        self.num_quantum_communication_channels = num_quantum_communication_channels

        # The Dictionary for the Protocol Rounds
        self.protocols_rounds = {}

        # For each round of the Protocol
        for current_num_round in range(num_rounds):

            # Initialize the object of the Round as None
            self.protocols_rounds[current_num_round] = None

        # Create the list of Preparing/Measurement Bases used for the protocol (i.e., X-, Y- and/or Z-Basis)
        preparing_bases_upper = []

        # For each Preparing/Measurement Basis
        for preparing_base in preparing_bases:

            # Append the Preparing/Measurement Basis, in uppercase,
            # to the list of Bases used in the protocol (i.e., X-, Y- and/or Z-Basis)
            preparing_bases_upper.append(preparing_base.upper())

        # Set the Preparing/Measurement Bases used for the protocol (i.e., X-, Y- and/or Z-Basis)
        self.preparing_bases_upper = list(set(preparing_bases_upper))

        # The type of Entanglement used for the protocol (i.e., GHZ, W or Graph States)
        self.quantum_entanglement_type = quantum_entanglement_type.upper()
