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

# Import required Enumerations and Constants

# Import the Communication Module Type from the IBM_Qiskit.Common
from src.common.enumerations import DataBusTypes

# Import the IBM Qiskit's Quantum Data/Information Bus with Discrete Variables from
# IBM_Qiskit.Node.Common.Bus.Hardware.Quantum.Discrete_Variable
from src.ibm_qiskit.node.common.bus.hardware.quantum.discrete_variable \
    import QiskitQuantumDataBusDiscreteVariables

# Import the IBM Qiskit's Quantum Data/Information Bus with Continuous Variables from
# IBM_Qiskit.Node.Common.Bus.Hardware.Quantum.Continuous_Variable
from src.ibm_qiskit.node.common.bus.hardware.quantum.continuous_variable \
    import QiskitQuantumDataBusContinuousVariables

# Import the IBM Qiskit's Classical Data/Information Bus from
# IBM_Qiskit.Node.Common.Bus.Hardware.Classical
from src.ibm_qiskit.node.common.bus.hardware.classical \
    import QiskitClassicalDataBus


# Class of the IBM Qiskit's Data Bus Hardware Module
class QiskitDataBusModule:

    # Constructor of the IBM Qiskit's Data Bus Hardware Module
    def __init__(self, data_bus_module_type_tag):

        # The Tag of the IBM Qiskit's Data Bus Hardware Type of the IBM Qiskit's Data Bus Hardware Module
        self.data_bus_module_type_tag = data_bus_module_type_tag

        # Initialise the IBM Qiskit's Quantum Data/Information Buses, with Discrete Variables
        self.qiskit_quantum_data_discrete_variables_buses = []

        # Initialise the IBM Qiskit's Quantum Data/Information Buses, with Continuous Variables
        self.qiskit_quantum_data_continuous_variables_buses = []

        # Initialise the IBM Qiskit's Classical Data/Information Buses
        self.qiskit_classical_data_buses = []

    # Return the Tag of the IBM Qiskit's Data/Information Bus Hardware Type of
    # the IBM Qiskit's Data/Information Bus Hardware Module
    def get_data_bus_module_type_tag(self):
        return self.data_bus_module_type_tag

    # Add an abstract IBM Qiskit's Data Bus to the IBM Qiskit's Data Bus Hardware Module
    def add_data_bus(self, qiskit_data_bus_to_add):

        # If the IBM Qiskit's Data/Information Bus Module is Quantum, with Discrete Variables,
        # only the IBM Qiskit's Quantum Data/Information Bus, with Discrete Variables can be added
        if self.data_bus_module_type_tag == DataBusTypes.QUANTUM_DATA_DISCRETE_VARIABLES_BUS_ENUM:

            # Check if the abstract IBM Qiskit's Data/Information Bus Hardware,
            # is compatible with the type of Data/Information Bus Hardware, for the case of a
            # Quantum Data/Information Bus Hardware with Discrete Variables, being given
            if isinstance(qiskit_data_bus_to_add,
                          QiskitQuantumDataBusDiscreteVariables
                          .QiskitQuantumDataBusDiscreteVariables):

                # Add the given abstract IBM Qiskit's Data/Information Bus Hardware to
                # the IBM Qiskit's Data/Information Bus Hardware Module
                self.qiskit_quantum_data_discrete_variables_buses.append(qiskit_data_bus_to_add)

            # The abstract IBM Qiskit's Data/Information Bus Hardware,
            # is not compatible with the type of Data/Information Bus Hardware, for the case of a
            # Quantum Data/Information Bus Hardware with Discrete Variables, being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware for Data/Information Bus!!!")

        # If the IBM Qiskit's Data/Information Bus Module is Quantum, with Continuous Variables,
        # only the IBM Qiskit's Quantum Data/Information Bus, with Continuous Variables can be added
        elif self.data_bus_module_type_tag == DataBusTypes.QUANTUM_DATA_CONTINUOUS_VARIABLES_BUS_ENUM:

            # Check if the abstract IBM Qiskit's Data/Information Bus Hardware,
            # is compatible with the type of Data/Information Bus Hardware, for the case of a
            # Quantum Data/Information Bus Hardware with Continuous Variables, being given
            if isinstance(qiskit_data_bus_to_add,
                          QiskitQuantumDataBusContinuousVariables
                          .QiskitQuantumDataBusContinuousVariables):

                # Add the given abstract IBM Qiskit's Data/Information Bus Hardware to
                # the IBM Qiskit's Data/Information Bus Hardware Module
                self.qiskit_quantum_data_continuous_variables_buses.append(qiskit_data_bus_to_add)

            # The abstract IBM Qiskit's Data/Information Bus Hardware,
            # is not compatible with the type of Data/Information Bus Hardware, for the case of a
            # Quantum Data/Information Bus Hardware with Continuous Variables, being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware for Data/Information Bus!!!")

        # If the IBM Qiskit's Data/Information Bus Module is Classical,
        # only the IBM Qiskit's Classical Data/Information Bus can be added
        elif self.data_bus_module_type_tag == DataBusTypes.CLASSICAL_DATA_BUS_ENUM:

            # Check if the abstract IBM Qiskit's Data/Information Bus Hardware,
            # is compatible with the type of Data/Information Bus Hardware, for the case of a
            # Classical Data/Information Bus Hardware, being given
            if isinstance(qiskit_data_bus_to_add,
                          QiskitClassicalDataBus
                          .QiskitClassicalDataBus):

                # Add the given abstract IBM Qiskit's Data/Information Bus Hardware to
                # the IBM Qiskit's Data/Information Bus Hardware Module
                self.qiskit_classical_data_buses.append(qiskit_data_bus_to_add)

            # The abstract IBM Qiskit's Data/Information Bus Hardware,
            # is not compatible with the type of Data/Information Bus Hardware, for the case of a
            # Classical Data/Information Bus Hardware, being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware for Data/Information Bus!!!")

        # If the IBM Qiskit's Data/Information Bus Module is not Quantum, with Discrete Variables,
        # neither Quantum, with Continuous Variables, neither Classical can be added
        else:

            # Raise a Value Error
            raise ValueError("It is impossible to add any type of Data/Information Bus Hardware to "
                             "this Data/Information Bus Module, due to an Unknown Hardware type of "
                             "Data/Information Bus Hardware Module!!!")

    # Remove an abstract IBM Qiskit's Data Bus to the IBM Qiskit's Data Bus Hardware Module
    def remove_data_bus(self, qiskit_data_bus_to_be_removed):

        # If the IBM Qiskit's Data/Information Bus Module is Quantum, with Discrete Variables,
        # only the IBM Qiskit's Quantum Data/Information Bus, with Discrete Variables can be removed
        if self.data_bus_module_type_tag == DataBusTypes.QUANTUM_DATA_DISCRETE_VARIABLES_BUS_ENUM:

            # Check if the abstract IBM Qiskit's Data/Information Bus Hardware,
            # is compatible with the type of Data/Information Bus Hardware, for the case of a
            # Quantum Data/Information Bus Hardware with Discrete Variables, being given
            if isinstance(qiskit_data_bus_to_be_removed,
                          QiskitQuantumDataBusDiscreteVariables
                          .QiskitQuantumDataBusDiscreteVariables):

                # Remove the given abstract IBM Qiskit's Data/Information Bus Hardware to
                # the IBM Qiskit's Data/Information Bus Hardware Module
                self.qiskit_quantum_data_discrete_variables_buses.remove(qiskit_data_bus_to_be_removed)

            # The abstract IBM Qiskit's Data/Information Bus Hardware,
            # is not compatible with the type of Data/Information Bus Hardware, for the case of a
            # Quantum Data/Information Bus Hardware with Discrete Variables, being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Hardware for Data/Information Bus!!!")

        # If the IBM Qiskit's Data/Information Bus Module is Quantum, with Continuous Variables,
        # only the IBM Qiskit's Quantum Data/Information Bus, with Continuous Variables can be removed
        elif self.data_bus_module_type_tag == DataBusTypes.QUANTUM_DATA_CONTINUOUS_VARIABLES_BUS_ENUM:

            # Check if the abstract IBM Qiskit's Data/Information Bus Hardware,
            # is compatible with the type of Data/Information Bus Hardware, for the case of a
            # Quantum Data/Information Bus Hardware with Continuous Variables, being given
            if isinstance(qiskit_data_bus_to_be_removed,
                          QiskitQuantumDataBusContinuousVariables
                          .QiskitQuantumDataBusContinuousVariables):

                # Remove the given abstract IBM Qiskit's Data/Information Bus Hardware to
                # the IBM Qiskit's Data/Information Bus Hardware Module
                self.qiskit_quantum_data_continuous_variables_buses.remove(qiskit_data_bus_to_be_removed)

            # The abstract IBM Qiskit's Data/Information Bus Hardware,
            # is not compatible with the type of Data/Information Bus Hardware, for the case of a
            # Quantum Data/Information Bus Hardware with Continuous Variables, being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Hardware for Data/Information Bus!!!")

        # If the IBM Qiskit's Data/Information Bus Module is Classical,
        # only the IBM Qiskit's Classical Data/Information Bus can be removed
        elif self.data_bus_module_type_tag == DataBusTypes.CLASSICAL_DATA_BUS_ENUM:

            # Check if the abstract IBM Qiskit's Data/Information Bus Hardware,
            # is compatible with the type of Data/Information Bus Hardware, for the case of a
            # Classical Data/Information Bus Hardware, being given
            if isinstance(qiskit_data_bus_to_be_removed,
                          QiskitClassicalDataBus
                          .QiskitClassicalDataBus):

                # Remove the given abstract IBM Qiskit's Data/Information Bus Hardware to
                # the IBM Qiskit's Data/Information Bus Hardware Module
                self.qiskit_classical_data_buses.append(qiskit_data_bus_to_be_removed)

            # The abstract IBM Qiskit's Data/Information Bus Hardware,
            # is not compatible with the type of Data/Information Bus Hardware, for the case of a
            # Classical Data/Information Bus Hardware, being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Hardware for Data/Information Bus!!!")

        # If the IBM Qiskit's Data/Information Bus Module is not Quantum, with Discrete Variables,
        # neither Quantum, with Continuous Variables, neither Classical can be removed
        else:

            # Raise a Value Error
            raise ValueError("It is impossible to remove any type of Data/Information Bus Hardware to "
                             "this Data/Information Bus Module, due to an Unknown Hardware type of "
                             "Data/Information Bus Hardware Module!!!")

    # Return the IBM Qiskit's Quantum Data/Information Bus with Discrete Variables,
    # in this IBM Qiskit's Data/Information Bus Module
    def get_qiskit_quantum_data_buses_discrete_variable(self):

        # If the IBM Qiskit's Data/Information Bus Module Hardware is Quantum with Discrete Variables,
        # then it can have IBM Qiskit's Quantum Data/Information Bus with Discrete Variables' Hardware
        if self.data_bus_module_type_tag == DataBusTypes.QUANTUM_DATA_DISCRETE_VARIABLES_BUS_ENUM:

            # Return the IBM Qiskit's Quantum Data/Information Bus
            return self.qiskit_quantum_data_discrete_variables_buses

        # If the IBM Qiskit's Data/Information Bus Module Hardware is not
        # Quantum with Discrete Variables, then it cannot have
        # IBM Qiskit's Quantum Data/Information Buses with Discrete Variables
        else:

            # Raise a Value Error
            raise ValueError("Only Quantum Data/Information Bus with Discrete Variables Modules' Hardware "
                             "can have Quantum Data/Information Buses with Discrete Variables' Hardware!!!")

    # Return the IBM Qiskit's Quantum Data/Information Bus with Continuous Variables,
    # in this IBM Qiskit's Data/Information Bus Module
    def get_qiskit_quantum_data_buses_continuous_variable(self):

        # If the IBM Qiskit's Data/Information Bus Module Hardware is Quantum with Continuous Variables,
        # then it can have IBM Qiskit's Quantum Data/Information Bus with Continuous Variables' Hardware
        if self.data_bus_module_type_tag == DataBusTypes.QUANTUM_DATA_CONTINUOUS_VARIABLES_BUS_ENUM:

            # Return the IBM Qiskit's Quantum Data/Information Bus
            return self.qiskit_quantum_data_continuous_variables_buses

        # If the IBM Qiskit's Data/Information Bus Module Hardware is not
        # Quantum with Continuous Variables, then it cannot have
        # IBM Qiskit's Quantum Data/Information Buses with Continuous Variables
        else:

            # Raise a Value Error
            raise ValueError("Only Quantum Data/Information Bus with Continuous Variables Modules' Hardware "
                             "can have Quantum Data/Information Buses with Continuous Variables' Hardware!!!")

    # Return the IBM Qiskit's Classical Data/Information Bus,
    # in this IBM Qiskit's Data/Information Bus Module
    def get_qiskit_classical_data_buses(self):

        # If the IBM Qiskit's Data/Information Bus Module Hardware is Classical,
        # then it can have IBM Qiskit's Classical Data/Information Bus Hardware
        if self.data_bus_module_type_tag == DataBusTypes.CLASSICAL_DATA_BUS_ENUM:

            # Return the IBM Qiskit's Classical Data/Information Bus
            return self.qiskit_classical_data_buses

        # If the IBM Qiskit's Data/Information Bus Module Hardware is not
        # Classical, then it cannot have IBM Qiskit's Classical Data/Information Buses
        else:

            # Raise a Value Error
            raise ValueError("Only Classical Data/Information Bus Modules' Hardware "
                             "can have Classical Data/Information Buses' Hardware!!!")
