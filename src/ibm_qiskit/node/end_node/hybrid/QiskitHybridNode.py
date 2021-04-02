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


# Class of the IBM Qiskit's Hybrid Node
class QiskitHybridNode:

    # Constructor of the IBM Qiskit's Hybrid Node
    def __init__(self, hybrid_node_id, hybrid_memory):

        # The ID of the IBM Qiskit's Hybrid Node
        self.hybrid_node_id = hybrid_node_id

        # The Owner Client Party of the IBM Qiskit's Hybrid Node
        self.owner_client_party = None

        # The Boolean Flag, to keep the information about
        # the IBM Qiskit's Hybrid Node is currently being owned by some Client/Party
        self.owned_by_client_party = False

        # The Hybrid Memory of the IBM Qiskit's Hybrid Node
        self.hybrid_memory = hybrid_memory

        # TODO - Communication Module

    # Attach some Owner Client Party to the IBM Qiskit's Hybrid Node
    def attach_owner_client_party(self, owner_client_party):

        # Set the Owner Client Party of the IBM Qiskit's Hybrid Node,
        # as the one given by argument
        self.owner_client_party = owner_client_party

        # Set the Boolean Flag, to keep the information about
        # the IBM Qiskit's Hybrid Node is currently being owned by some Client/Party, as True
        self.owned_by_client_party = True

    # Release the current Owner Client Party from the IBM Qiskit's Hybrid Node
    def release_owner_client_party(self):

        # Set the Owner Client Party of the IBM Qiskit's Hybrid Node,
        # as None
        self.owner_client_party = None

        # Set the Boolean Flag, to keep the information about
        # the IBM Qiskit's Hybrid Node is currently being owned by some Client/Party, as False
        self.owned_by_client_party = False

    # Return the ID of the IBM Qiskit's Hybrid Node
    def get_hybrid_node_id(self):
        return self.hybrid_node_id

    # Return the Owner Client Party, using the IBM Qiskit's Hybrid Node
    def get_owner_client_name(self):
        return self.owner_client_party

    # Return the Hybrid Memory of the IBM Qiskit's Hybrid Node
    def get_hybrid_memory(self):
        return self.hybrid_node_id
