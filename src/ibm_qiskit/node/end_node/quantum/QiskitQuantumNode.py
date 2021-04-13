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

# Import the IBM Qiskit's Memory Module from
# the IBM_Qiskit.Node.Common.Memory.Modules
from src.ibm_qiskit.node.common.memory.modules import QiskitMemoryModule

# Import the IBM Qiskit's Communication Module from
# the IBM_Qiskit.Node.Common.Communication.Modules
from src.ibm_qiskit.node.common.communication.modules import QiskitCommunicationModule

# Import the Enumeration for the Memory Module Types from
# the Common.Enumerations
from src.common.enumerations import MemoryModuleTypes

# Import the Enumeration for the Communication Module Types from
# the Common.Enumerations
from src.common.enumerations import CommunicationModuleTypes


# Class of the IBM Qiskit's Quantum Node
class QiskitQuantumNode:

    # Constructor of the IBM Qiskit's Quantum Node
    def __init__(self, quantum_node_id):

        # The ID of the IBM Qiskit's Quantum Node
        self.quantum_node_id = quantum_node_id

        # The Owner Client Party of the IBM Qiskit's Quantum Node
        self.owner_client_party = None

        # The Boolean Flag, to keep the information about
        # the IBM Qiskit's Quantum Node is currently being owned by some Client/Party
        self.owned_by_client_party = False

        # The Memory Hardware Module of the IBM Qiskit's Quantum Node
        self.memory_hardware_module = \
            QiskitMemoryModule.QiskitMemoryModule(MemoryModuleTypes.QUANTUM_MEMORY_ENUM)

        # The Communication Hardware Interface of the IBM Qiskit's Quantum Node
        self.communication_hardware_module = \
            QiskitCommunicationModule.QiskitCommunicationModule(CommunicationModuleTypes.QUANTUM_COMMUNICATION_ENUM)

    # Attach some Owner Client Party to the IBM Qiskit's Quantum Node
    def attach_owner_client_party(self, owner_client_party):

        # Set the Owner Client Party of the IBM Qiskit's Quantum Node,
        # as the one given by argument
        self.owner_client_party = owner_client_party

        # Set the Boolean Flag, to keep the information about
        # the IBM Qiskit's Quantum Node is currently being owned by some Client/Party, as True
        self.owned_by_client_party = True

    # Release the current Owner Client Party from the IBM Qiskit's Quantum Node
    def release_owner_client_party(self):

        # Set the Owner Client Party of the IBM Qiskit's Quantum Node, as None
        self.owner_client_party = None

        # Set the Boolean Flag, to keep the information about
        # the IBM Qiskit's Quantum Node is currently being owned by some Client/Party, as False
        self.owned_by_client_party = False

    # Return the ID of the IBM Qiskit's Quantum Node
    def get_quantum_node_id(self):
        return self.quantum_node_id

    # Return the Owner Client Party, using the IBM Qiskit's Quantum Node
    def get_owner_client_party(self):
        return self.owner_client_party

    # Return the Boolean Flag, to keep the information about
    # the IBM Qiskit's Quantum Node is currently being owned by some Client/Party
    def is_owned_by_client_party(self):
        return self.owned_by_client_party

    # Return the Memory Hardware Module of the IBM Qiskit's Quantum Node
    def get_memory_hardware_module(self):
        return self.memory_hardware_module

    # Return the Communication Hardware Interface of the IBM Qiskit's Quantum Node
    def get_communication_hardware_module(self):
        return self.communication_hardware_module

    # Print the information about the IBM Qiskit's Quantum Node
    def print_info(self):

        # Some prints to draw a top left-side corner
        print(" __")
        print("|")
        print("|")

        # Print the Heading, with the ID of the IBM Qiskit's Quantum Node
        print("  Node #{}:\n".format(self.quantum_node_id))

        # Print the Sub-Heading, for the Owner Client/Party
        print("   - Owner Client/Party:")

        # If the IBM Qiskit's Quantum Node is owned by some Client/Party
        if self.is_owned_by_client_party():

            # Print the UUID of the Owner Client/Party
            print("     - Owner Client/Party's UUID: {};"
                  .format(self.owner_client_party.get_party_user_client().get_user_client_uuid()))

            # Print the name of the Owner Client/Party
            print("     - Owner Client/Party's Name: {};"
                  .format(self.owner_client_party.get_party_user_client().get_user_client_name()))

        # If the IBM Qiskit's Quantum Node is not owned by some Client/Party
        else:

            # Print the information about none Owner Client/Party for the IBM Qiskit's Quantum Node
            print("   -   Not owned by no Client/Party;")

        # Print the Tag for the Memory Module Type of
        # the IBM Qiskit's Quantum Node
        print("   - Memory Module Type's Tag: {};"
              .format(self.get_memory_hardware_module().get_memory_module_type_tag().lower()))

        # Print the Tag for the Communication Module Type of
        # the IBM Qiskit's Quantum Node
        print("   - Communication Module Type's Tag: {};"
              .format(self.get_communication_hardware_module().get_communication_module_type_tag().lower()))

        # Some prints to draw a bottom left-side corner
        print("|")
        print("|__")
