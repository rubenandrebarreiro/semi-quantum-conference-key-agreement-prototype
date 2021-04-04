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


# Class of the IBM Qiskit's Classical Node
class QiskitClassicalNode:

    # Constructor of the IBM Qiskit's Semi-Quantum Node
    def __init__(self, semi_quantum_node_id, classical_memory_module, classical_communication_module):

        # The ID of the IBM Qiskit's Classical Node
        self.semi_quantum_node_id = semi_quantum_node_id

        # The Owner Client Party of the IBM Qiskit's Classical Node
        self.owner_client_party = None

        # The Boolean Flag, to keep the information about
        # the IBM Qiskit's Classical Node is currently being owned by some Client/Party
        self.owned_by_client_party = False

        # The Classical Memory Module of the IBM Qiskit's Classical Node
        self.classical_memory_module = classical_memory_module

        # TODO - Communication Module

    # Attach some Owner Client Party to the IBM Qiskit's Classical Node
    def attach_owner_client_party(self, owner_client_party):

        # Set the Owner Client Party of the IBM Qiskit's Classical Node,
        # as the one given by argument
        self.owner_client_party = owner_client_party

        # Set the Boolean Flag, to keep the information about
        # the IBM Qiskit's Classical Node is currently being owned by some Client/Party, as True
        self.owned_by_client_party = True

    # Release the current Owner Client Party from the IBM Qiskit's Classical Node
    def release_owner_client_party(self):

        # Set the Owner Client Party of the IBM Qiskit's Classical Node, as None
        self.owner_client_party = None

        # Set the Boolean Flag, to keep the information about
        # the IBM Qiskit's Classical Node is currently being owned by some Client/Party, as False
        self.owned_by_client_party = False

    # Return the ID of the IBM Qiskit's Classical Node
    def get_quantum_node_id(self):
        return self.semi_quantum_node_id

    # Return the Owner Client Party, using the IBM Qiskit's Classical Node
    def get_quantum_client_name(self):
        return self.owner_client_party

    # Return the Classical Memory Module of the IBM Qiskit's Classical Node
    def get_classical_memory_module(self):
        return self.classical_memory_module
