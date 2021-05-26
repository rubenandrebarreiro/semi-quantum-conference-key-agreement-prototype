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


# Class for IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocol:

    # Constructor for IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def __init__(self, party_entities, distributor_party_entity, bipartite_pre_shared_keys, parameters):

        # Set the Party Entities involved in the Protocol
        self.party_entities = party_entities

        # Set the Distributor Party Entity of the Protocol
        self.distributor_party_entity = distributor_party_entity

        # Set the Bipartite Pre-Shared Keys used between the Parties, involved in the Protocol
        self.bipartite_pre_shared_keys = bipartite_pre_shared_keys

        # Set the Parameters of the Protocol
        self.parameters = parameters

        # Initialise the list of the Rounds of the Protocol
        self.protocol_rounds = []

    # Return the Party Entities of the Protocol
    def get_party_entities(self):
        return self.party_entities

    # Return the Distributor Party Entity of the Protocol
    def get_distributor_party_entity(self):
        return self.distributor_party_entity

    # Return the Bipartite Pre-Shared Keys, being used on the Protocol
    def get_bipartite_pre_shared_keys(self):
        return self.bipartite_pre_shared_keys

    # Return the Parameters of the Protocol
    def get_parameters(self):
        return self.parameters

    # Return the list of the Rounds of the Protocol
    def get_protocol_rounds(self):
        return self.parameters

    # Add a Round of the Protocol
    def add_protocol_round(self, protocol_round):
        self.protocol_rounds.append(protocol_round)
