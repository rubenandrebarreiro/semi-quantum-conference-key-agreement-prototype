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

# Import the IBM Qiskit's Communication Module from
# the IBM_Qiskit.Node.Common.Data_Bus.Modules
from src.ibm_qiskit.node.common.data_bus.modules import QiskitDataBusModule

# Import the Enumeration for the Node Types from
# the Common.Enumerations
from src.common.enumerations import NodeTypes

# Import the Enumeration for the Memory Module Types from
# the Common.Enumerations
from src.common.enumerations import MemoryModuleTypes

# Import the Enumeration for the Communication Module Types from
# the Common.Enumerations
from src.common.enumerations import CommunicationModuleTypes

# Import the Enumeration for the Data/Information Bus Module Types from
# the Common.Enumerations
from src.common.enumerations import DataBusTypes


# Class of the IBM Qiskit's Hybrid Node
class QiskitHybridNode:

    # Constructor of the IBM Qiskit's Hybrid Node
    def __init__(self, hybrid_node_id):

        # The ID of the IBM Qiskit's Hybrid Node
        self.hybrid_node_id = hybrid_node_id

        # The Tag of the Type of the IBM Qiskit's Hybrid Node
        self.hybrid_node_type_tag = \
            NodeTypes.HYBRID_NODE_ENUM

        # The Owner Client Party of the IBM Qiskit's Hybrid Node
        self.owner_client_party = None

        # The Boolean Flag, to keep the information about
        # the IBM Qiskit's Hybrid Node is
        # currently being owned by some Client/Party
        self.owned_by_client_party = False

        # The Memory Hardware Module of the IBM Qiskit's Hybrid Node
        self.memory_hardware_module = \
            QiskitMemoryModule.QiskitMemoryModule(MemoryModuleTypes.HYBRID_MEMORY_ENUM)

        # The Communication Hardware Interface of the IBM Qiskit's Hybrid Node
        self.communication_hardware_module = \
            QiskitCommunicationModule\
            .QiskitCommunicationModule(CommunicationModuleTypes.QUANTUM_COMMUNICATION_ENUM)

        # The Data/Information Bus Module of the IBM Qiskit's Hybrid Node, for Discrete Variables
        self.data_bus_hardware_discrete_variables_module = \
            QiskitDataBusModule.QiskitDataBusModule(DataBusTypes.QUANTUM_DATA_DISCRETE_VARIABLES_BUS_ENUM)

        # The Data/Information Bus Module of the IBM Qiskit's Hybrid Node, for Continuous Variables
        self.data_bus_hardware_continuous_variables_module = \
            QiskitDataBusModule.QiskitDataBusModule(DataBusTypes.QUANTUM_DATA_CONTINUOUS_VARIABLES_BUS_ENUM)

    # Attach some Owner Client Party to the IBM Qiskit's Hybrid Node
    def attach_owner_client_party(self, owner_client_party):

        # Set the Owner Client Party of the IBM Qiskit's Hybrid Node,
        # as the one given by argument
        self.owner_client_party = owner_client_party

        # Set the Boolean Flag, to keep the information about
        # the IBM Qiskit's Hybrid Node
        # is currently being owned by some Client/Party, as True
        self.owned_by_client_party = True

    # Release the current Owner Client Party from the IBM Qiskit's Hybrid Node
    def release_owner_client_party(self):

        # Set the Owner Client Party of the IBM Qiskit's Hybrid Node, as None
        self.owner_client_party = None

        # Set the Boolean Flag, to keep the information about
        # the IBM Qiskit's Hybrid Node
        # is currently being owned by some Client/Party, as False
        self.owned_by_client_party = False

    # Return the ID of the IBM Qiskit's Hybrid Node
    def get_hybrid_node_id(self):
        return self.hybrid_node_id

    # Return the Tag of the Type of the IBM Qiskit's Hybrid Node
    def get_hybrid_node_type_tag(self):
        return self.hybrid_node_type_tag

    # Return the Owner Client Party, using the IBM Qiskit's Hybrid Node
    def get_owner_client_party(self):
        return self.owner_client_party

    # Return the Boolean Flag, to keep the information about
    # the IBM Qiskit's Hybrid Node is currently being owned by some Client/Party
    def is_owned_by_client_party(self):
        return self.owned_by_client_party

    # Return the Memory Hardware Module of the IBM Qiskit's Hybrid Node
    def get_memory_hardware_module(self):
        return self.memory_hardware_module

    # Return the Communication Hardware Interface of the IBM Qiskit's Hybrid Node
    def get_communication_hardware_module(self):
        return self.communication_hardware_module

    # Return the Quantum Data/Information Bus Hardware, with Discrete Variables Module of
    # the IBM Qiskit's Hybrid Node
    def get_quantum_data_bus_discrete_variables_hardware_module(self):
        return self.data_bus_hardware_discrete_variables_module

    # Return the Quantum Data/Information Bus Hardware, with Continuous Variables Module of
    # the IBM Qiskit's Hybrid Node
    def get_quantum_data_bus_continuous_variables_hardware_module(self):
        return self.data_bus_hardware_continuous_variables_module

    # Print the information about the IBM Qiskit's Hybrid Node
    def print_info(self):

        # Some prints to draw a top left-side corner
        print(" __")
        print("|")
        print("|")

        # Print the Heading, with the ID of the IBM Qiskit's Hybrid Node
        print("  Node #{}:\n".format(self.hybrid_node_id))

        # Print the Sub-Heading, for the Owner Client/Party
        print("   - Owner Client/Party:")

        # If the IBM Qiskit's Hybrid Node, is owned by some Client/Party
        if self.is_owned_by_client_party():

            # Print the UUID of the Owner Client/Party
            print("     - Owner Client/Party's UUID: {};"
                  .format(self.owner_client_party.get_party_user_client().get_user_client_uuid()))

            # Print the name of the Owner Client/Party
            print("     - Owner Client/Party's Name: {};"
                  .format(self.owner_client_party.get_party_user_client().get_user_client_name()))

        # If the IBM Qiskit's Hybrid Node, is not owned by some Client/Party
        else:

            # Print the information about none Owner Client/Party for
            # the IBM Qiskit's Hybrid Node
            print("   -   Not owned by no Client/Party;")

        # Print the Tag of the Type of the IBM Qiskit's Hybrid Node
        print("   - Node's Type Tag: {};".format(self.hybrid_node_type_tag))

        # Print the Tag for the Memory Module Type of
        # the IBM Qiskit's Hybrid Node
        print("   - Memory Module Type's Tag: {};"
              .format(self.get_memory_hardware_module().get_memory_module_type_tag().lower()))

        # Print the Tag for the Quantum Data/Information Bus, with Discrete Variables Module Type of
        # the IBM Qiskit's Hybrid Node
        print("   - Quantum Communication with Discrete Variables Module Type's Tag: {};"
              .format(self.get_quantum_data_bus_discrete_variables_hardware_module()
                      .get_data_bus_module_type_tag().lower()))

        # Print the Tag for the Quantum Data/Information Bus, with Continuous Variables Module Type of
        # the IBM Qiskit's Hybrid Node
        print("   - Quantum Communication with Continuous Variables Module Type's Tag: {};"
              .format(self.get_quantum_data_bus_continuous_variables_hardware_module()
                      .get_data_bus_module_type_tag().lower()))

        # Some prints to draw a bottom left-side corner
        print("|")
        print("|__")
