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
    def __init__(self, parties, master_party, bipartite_pre_shared_keys, parameters):

        # The Parties involved in the Protocol
        self.parties = parties

        # The Master Party of the Protocol
        self.master_party = master_party

        # The Bipartite Pre-Shared Keys used between the Parties, involved in the Protocol
        self.bipartite_pre_shared_keys = bipartite_pre_shared_keys

        # The Parameters of the Protocol
        self.parameters = parameters

    # Return the Parties of the Protocol
    def get_parties(self):
        return self.parties

    # Return the Master Party of the Protocol
    def get_master_party(self):
        return self.master_party

    # Return the Bipartite Pre-Shared Keys, being used on the Protocol
    def get_bipartite_pre_shared_keys(self):
        return self.bipartite_pre_shared_keys

    # Return the Parameters of the Protocol
    def get_parameters(self):
        return self.parameters
