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
from src.common.enumerations import CommunicationModuleTypes

# Import the IBM Qiskit's Quantum Communication with Discrete Variables, by Fiber Optic Interface from
# the IBM_Qiskit.Node.Common.Communication.Hardware.Quantum.Discrete_Variable.Fiber_Optic
from src.ibm_qiskit.node.common.communication\
         .hardware.quantum.discrete_variable.fiber_optic import \
         QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface

# Import the IBM Qiskit's Quantum Communication with Discrete Variables, by Satellite Interface from
# the IBM_Qiskit.Node.Common.Communication.Hardware.Quantum.Discrete_Variable.Satellite
from src.ibm_qiskit.node.common.communication\
         .hardware.quantum.discrete_variable.satellite import \
         QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface

# Import the IBM Qiskit's Quantum Communication with Continuous Variables, by Fiber Optic Interface from
# the IBM_Qiskit.Node.Common.Communication.Hardware.Quantum.Continuous_Variable.Fiber_Optic
from src.ibm_qiskit.node.common.communication\
         .hardware.quantum.continuous_variable.fiber_optic import \
         QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface

# Import the IBM Qiskit's Quantum Communication with Continuous Variables, by Satellite Interface from
# the IBM_Qiskit.Node.Common.Communication.Hardware.Quantum.Continuous_Variable.Satellite
from src.ibm_qiskit.node.common.communication\
         .hardware.quantum.continuous_variable.satellite import \
         QiskitQuantumCommunicationContinuousVariablesSatelliteInterface

# Import the IBM Qiskit's Quantum Communication with Continuous Variables, by Fiber Optic Interface from
# the IBM_Qiskit.Node.Common.Communication.Hardware.Quantum.Continuous_Variable.Fiber_Optic
from src.ibm_qiskit.node.common.communication\
         .hardware.classical.fiber_optic import \
         QiskitClassicalCommunicationFiberOpticInterface

# Import the IBM Qiskit's Quantum Communication with Continuous Variables, by Satellite Interface from
# the IBM_Qiskit.Node.Common.Communication.Hardware.Quantum.Continuous_Variable.Satellite
from src.ibm_qiskit.node.common.communication\
         .hardware.classical.satellite import \
         QiskitClassicalCommunicationSatelliteInterface


# Class of the IBM Qiskit's Communication Hardware Module
class QiskitCommunicationModule:

    # Constructor of the IBM Qiskit's Communication Hardware Module
    def __init__(self, communication_module_type_tag):

        # The Tag of the IBM Qiskit's Communication Hardware Type of the IBM Qiskit's Communication Hardware Module
        self.communication_module_type_tag = communication_module_type_tag

        # Initialise the IBM Qiskit's Quantum Communication with Discrete Variables, by Fiber Optic Interfaces
        self.qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces = []

        # Initialise the IBM Qiskit's Quantum Communication with Discrete Variables, by Satellite Interfaces
        self.qiskit_quantum_communication_discrete_variable_satellite_interfaces = []

        # Initialise the IBM Qiskit's Quantum Communication with Continuous Variables, by Fiber Optic Interfaces
        self.qiskit_quantum_communication_continuous_variable_fiber_optic_interfaces = []

        # Initialise the IBM Qiskit's Quantum Communication with Continuous Variables, by Satellite Interfaces
        self.qiskit_quantum_communication_continuous_variable_satellite_interfaces = []

        # Initialise the IBM Qiskit's Classical Communication, by Fiber Optic Interface
        self.qiskit_classical_communication_fiber_optic_interfaces = []

        # Initialise the IBM Qiskit's Classical Communication, by Satellite Interface
        self.qiskit_classical_communication_satellite_interfaces = []

    # Return the Tag of the IBM Qiskit's Communication Hardware Type of the IBM Qiskit's Communication Hardware Module
    def get_communication_module_type_tag(self):
        return self.communication_module_type_tag

    # Add an abstract IBM Qiskit's Communication Hardware to the IBM Qiskit's Communication Interface Hardware Module
    def add_communication_interface(self, qiskit_communication_interface_to_add):

        # If the IBM Qiskit's Communication Hardware Module is Hybrid,
        # all the type of Communication Interface Hardware
        # (Quantum with Discrete Variables, Quantum with Continuous Variables and Classical) can be added
        if self.communication_module_type_tag == CommunicationModuleTypes.HYBRID_COMMUNICATION_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_add,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces\
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Hardware Interface Module
                self.qiskit_quantum_communication_continuous_variable_fiber_optic_interfaces\
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_continuous_variable_satellite_interfaces\
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_fiber_optic_interfaces\
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_satellite_interfaces\
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Hardware Module is Hybrid,
        # with Discrete Variables, only the type of Communication Interface Hardware
        # (Quantum with Discrete Variables and Classical) can be added
        elif self.communication_module_type_tag == \
                CommunicationModuleTypes.HYBRID_COMMUNICATION_DISCRETE_VARIABLES_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_add,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Continuous Variables to "
                                 "a Hybrid Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Continuous Variables to "
                                 "a Hybrid Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_fiber_optic_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_satellite_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Hardware Module is Hybrid,
        # with Continuous Variables, only the type of Communication Interface Hardware
        # (Quantum with Continuous Variables and Classical) can be added
        elif self.communication_module_type_tag == \
                CommunicationModuleTypes.HYBRID_COMMUNICATION_CONTINUOUS_VARIABLES_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_add,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Discrete Variables to "
                                 "a Hybrid Communication Interface Hardware Module with Continuous Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Discrete Variables to "
                                 "a Hybrid Communication Interface Hardware Module with Continuous Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_continuous_variable_fiber_optic_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_continuous_variable_satellite_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_fiber_optic_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_satellite_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Hardware Module is Quantum, only the type of
        # Communication Interface Hardware being Quantum, Quantum with Discrete Variables and
        # Quantum with Continuous Variables can be added
        elif self.communication_module_type_tag == CommunicationModuleTypes.QUANTUM_COMMUNICATION_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_add,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces\
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces\
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Hardware Interface Module
                self.qiskit_quantum_communication_continuous_variable_fiber_optic_interfaces\
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_continuous_variable_satellite_interfaces\
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Classical Communication Interface to "
                                 "a Quantum Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Classical Communication Interface to "
                                 "a Quantum Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Interface Hardware Interface Module is Quantum with Discrete Variables,
        # only the type of Communication Interface Hardware being Quantum with Discrete Variables can be added
        elif self.communication_module_type_tag == \
                CommunicationModuleTypes.QUANTUM_COMMUNICATION_DISCRETE_VARIABLES_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_add,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware Interface, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware Interface, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Continuous Variables to "
                                 "a Quantum Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Hardware Interface with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Continuous Variables to "
                                 "a Quantum Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Classical Communication Interface to "
                                 "a Quantum Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Classical Communication Interface to "
                                 "a Quantum Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware Interface, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Hardware Interface Module is Quantum with Continuous Variables,
        # only the type of Communication Hardware Interface being Quantum with Continuous Variables can be added
        elif self.communication_module_type_tag == \
                CommunicationModuleTypes.QUANTUM_COMMUNICATION_CONTINUOUS_VARIABLES_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Hardware Interface with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_add,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Discrete Variables to "
                                 "a Quantum Communication Interface Hardware Module with Continuous Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Hardware Interface with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Discrete Variables to "
                                 "a Quantum Communication Interface Hardware Module with Continuous Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Hardware Interface to
                # the IBM Qiskit's Communication Hardware Interface Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware Interface, for the case of a
            # Quantum Communication Hardware Interface with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Hardware Interface to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Classical Communication Interface to "
                                 "a Quantum Communication Interface Hardware Module with Continuous Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Classical Communication Interface to "
                                 "a Quantum Communication Interface Hardware Module with Continuous Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Interface Hardware Module is Classical,
        # only the type of Communication Interface Hardware being Classical can be added
        elif self.communication_module_type_tag == \
                CommunicationModuleTypes.CLASSICAL_COMMUNICATION_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_add,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Discrete Variables to "
                                 "a Classical Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Discrete Variables to "
                                 "a Classical Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Continuous Variables to "
                                 "a Classical Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication
                raise ValueError("It is not possible to add a Quantum Communication Interface "
                                 "with Continuous Variables to "
                                 "a Classical Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Add the given abstract IBM Qiskit's Communication Hardware Interface to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_fiber_optic_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_add,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Add the given abstract IBM Qiskit's Communication Hardware Interface to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_satellite_interfaces \
                    .append(qiskit_communication_interface_to_add)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Interface Hardware Module is Unknown,
        # no Communication Interface Hardware can be added and it will be raised a Value Error
        else:

            # Raise a Value Error
            raise ValueError("It is impossible to add any type of Communication Interface Hardware to "
                             "this Communication Interface Hardware Module, due to an Unknown Hardware type of "
                             "Communication Interface Hardware Module!!!")

    # Remove an abstract IBM Qiskit's Communication Interface Hardware from
    # the IBM Qiskit's Communication Interface Hardware Module
    def remove_communication_interface(self, qiskit_communication_interface_to_remove):

        # If the IBM Qiskit's Communication Hardware Module is Hybrid,
        # all the type of Communication Interface Hardware
        # (Quantum with Discrete Variables, Quantum with Continuous Variables and Classical) can be removed
        if self.communication_module_type_tag == CommunicationModuleTypes.HYBRID_COMMUNICATION_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_remove,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Hardware Interface Module
                self.qiskit_quantum_communication_continuous_variable_fiber_optic_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_continuous_variable_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_fiber_optic_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Hardware Module is Hybrid,
        # only the type of Communication Interface Hardware being
        # Quantum with Discrete Variables and Classical can be removed
        elif self.communication_module_type_tag == \
                CommunicationModuleTypes.HYBRID_COMMUNICATION_DISCRETE_VARIABLES_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_remove,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Continuous Variables from "
                                 "a Hybrid Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Continuous Variables from "
                                 "a Hybrid Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_fiber_optic_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Hardware Module is Hybrid,
        # only the type of Communication Interface Hardware being
        # Quantum with Continuous Variables and Classical can be removed
        elif self.communication_module_type_tag == \
                CommunicationModuleTypes.HYBRID_COMMUNICATION_CONTINUOUS_VARIABLES_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_remove,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Discrete Variables from "
                                 "a Hybrid Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Discrete Variables from "
                                 "a Hybrid Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_continuous_variable_fiber_optic_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_continuous_variable_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_fiber_optic_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Hardware Module is Quantum, only the type of
        # Communication Interface Hardware being Quantum, Quantum with Discrete Variables and
        # Quantum with Continuous Variables can be removed
        elif self.communication_module_type_tag == CommunicationModuleTypes.QUANTUM_COMMUNICATION_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_remove,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces\
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces\
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Hardware Interface Module
                self.qiskit_quantum_communication_continuous_variable_fiber_optic_interfaces\
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_continuous_variable_satellite_interfaces\
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Classical Communication Interface from "
                                 "a Quantum Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Classical Communication Interface from "
                                 "a Quantum Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Interface Hardware Interface Module is Quantum with Discrete Variables,
        # only the type of Communication Interface Hardware being Quantum with Discrete Variables can be removed
        elif self.communication_module_type_tag == \
                CommunicationModuleTypes.QUANTUM_COMMUNICATION_DISCRETE_VARIABLES_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_remove,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware Interface, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Interface Hardware to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware Interface, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Continuous Variables from "
                                 "a Quantum Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Hardware Interface with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Continuous Variables from "
                                 "a Quantum Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Classical Communication Interface from "
                                 "a Quantum Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Classical Communication Interface from "
                                 "a Quantum Communication Interface Hardware Module with Discrete Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware Interface, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Hardware Interface Module is Quantum with Continuous Variables,
        # only the type of Communication Hardware Interface being Quantum with Continuous Variables can be removed
        elif self.communication_module_type_tag == \
                CommunicationModuleTypes.QUANTUM_COMMUNICATION_CONTINUOUS_VARIABLES_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Hardware Interface with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_remove,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Discrete Variables from "
                                 "a Quantum Communication Interface Hardware Module with Continuous Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware, for the case of a Quantum Communication Hardware Interface with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Discrete Variables from "
                                 "a Quantum Communication Interface Hardware Module with Continuous Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Hardware Interface to
                # the IBM Qiskit's Communication Hardware Interface Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Hardware Interface, for the case of a
            # Quantum Communication Hardware Interface with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Hardware Interface to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_quantum_communication_discrete_variable_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Classical Communication Interface from "
                                 "a Quantum Communication Interface Hardware Module with Continuous Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Classical Communication Interface from "
                                 "a Quantum Communication Interface Hardware Module with Continuous Variables!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Interface Hardware Module is Classical,
        # only the type of Communication Interface Hardware being Classical can be removed
        elif self.communication_module_type_tag == \
                CommunicationModuleTypes.CLASSICAL_COMMUNICATION_ENUM:

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Fiber Optics Interface, being given
            if isinstance(qiskit_communication_interface_to_remove,
                          QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                          .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Discrete Variables from "
                                 "a Classical Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Discrete Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface
                            .QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Discrete Variables from "
                                 "a Classical Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication Interface
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Continuous Variables from "
                                 "a Classical Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                            .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Communication
                raise ValueError("It is not possible to remove a Quantum Communication Interface "
                                 "with Continuous Variables from "
                                 "a Classical Communication Interface Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Fiber Optics Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationFiberOpticInterface
                            .QiskitClassicalCommunicationFiberOpticInterface):

                # Remove the given abstract IBM Qiskit's Communication Hardware Interface to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_fiber_optic_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of a
            # Quantum Communication Interface Hardware with
            # Continuous Variables, by Satellite Interface, being given
            elif isinstance(qiskit_communication_interface_to_remove,
                            QiskitClassicalCommunicationSatelliteInterface
                            .QiskitClassicalCommunicationSatelliteInterface):

                # Remove the given abstract IBM Qiskit's Communication Hardware Interface to
                # the IBM Qiskit's Communication Interface Hardware Module
                self.qiskit_classical_communication_satellite_interfaces \
                    .remove(qiskit_communication_interface_to_remove)

            # Check if the abstract IBM Qiskit's Communication Interface Hardware is compatible with
            # the type of Communication Interface Hardware, for the case of an
            # Unknown Communication Interface Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Hardware for Communication Interface!!!")

        # If the IBM Qiskit's Communication Interface Hardware Module is Unknown,
        # no Communication Interface Hardware can be removed and it will be raised a Value Error
        else:

            # Raise a Value Error
            raise ValueError("It is impossible to remove any type of Communication Interface Hardware from "
                             "this Communication Interface Hardware Module, due to an Unknown Hardware type of "
                             "Communication Interface Hardware Module!!!")

    # Return the IBM Qiskit's Quantum Communication with Discrete Variables by Fiber Optic Interfaces,
    # in this IBM Qiskit's Communication Module
    def get_qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces(self):

        # If the IBM Qiskit's Communication Interface Module Hardware is Quantum or Quantum with Discrete Variables,
        # then it can have IBM Qiskit's Quantum Communication Interfaces with Discrete Variables' Hardware
        if (self.communication_module_type_tag ==
            CommunicationModuleTypes.QUANTUM_COMMUNICATION_ENUM) or \
                (self.communication_module_type_tag ==
                 CommunicationModuleTypes.QUANTUM_COMMUNICATION_DISCRETE_VARIABLES_ENUM):

            # Return the IBM Qiskit's Quantum Communication Interface with
            # Discrete Variables by Fiber Optic's Hardware
            return self.qiskit_quantum_communication_discrete_variable_fiber_optic_interfaces

        # If the IBM Qiskit's Communication Interface Module Hardware is not
        # Quantum neither Quantum with Discrete Variables,
        # then it cannot have IBM Qiskit's Quantum Communication with
        # Discrete Variables by Fiber Optic Interfaces' Hardware
        else:

            # Raise a Value Error
            raise ValueError("Only Quantum Communication Interface and "
                             "Quantum Communication Interface with Discrete Variables Modules' Hardware "
                             "can have Quantum Communication with Discrete Variables by "
                             "Fiber Optic Interface Hardware!!!")

    # Return the IBM Qiskit's Quantum Communication with Discrete Variables by Satellites Interfaces,
    # in this IBM Qiskit's Communication Module
    def get_qiskit_quantum_communication_discrete_variable_satellites_interfaces(self):

        # If the IBM Qiskit's Communication Interface Module Hardware is Quantum or Quantum with Discrete Variables,
        # then it can have IBM Qiskit's Quantum Communication Interfaces with Discrete Variables' Hardware
        if (self.communication_module_type_tag ==
            CommunicationModuleTypes.QUANTUM_COMMUNICATION_ENUM) or \
                (self.communication_module_type_tag ==
                 CommunicationModuleTypes.QUANTUM_COMMUNICATION_DISCRETE_VARIABLES_ENUM):

            # Return the IBM Qiskit's Quantum Communication Interface with
            # Discrete Variables by Satellite's Hardware
            return self.qiskit_quantum_communication_discrete_variable_satellite_interfaces

        # If the IBM Qiskit's Communication Interface Module Hardware is not
        # Quantum neither Quantum with Discrete Variables,
        # then it cannot have IBM Qiskit's Quantum Communication with
        # Discrete Variables by Satellite Interfaces' Hardware
        else:

            # Raise a Value Error
            raise ValueError("Only Quantum Communication Interface and "
                             "Quantum Communication Interface with Discrete Variables Modules' Hardware "
                             "can have Quantum Communication with Discrete Variables by "
                             "Satellite Interface Hardware!!!")

    # Return the IBM Qiskit's Quantum Communication with Continuous Variables by Fiber Optic Interfaces,
    # in this IBM Qiskit's Communication Module
    def get_qiskit_quantum_communication_continuous_variable_fiber_optic_interfaces(self):

        # If the IBM Qiskit's Communication Interface Module Hardware is Quantum or Quantum with Continuous Variables,
        # then it can have IBM Qiskit's Quantum Communication Interfaces with Continuous Variables' Hardware
        if (self.communication_module_type_tag ==
            CommunicationModuleTypes.QUANTUM_COMMUNICATION_ENUM) or \
                (self.communication_module_type_tag ==
                 CommunicationModuleTypes.QUANTUM_COMMUNICATION_CONTINUOUS_VARIABLES_ENUM):

            # Return the IBM Qiskit's Quantum Communication Interface with
            # Continuous Variables by Fiber Optic's Hardware
            return self.qiskit_quantum_communication_continuous_variable_fiber_optic_interfaces

        # If the IBM Qiskit's Communication Interface Module Hardware is not
        # Quantum neither Quantum with Continuous Variables,
        # then it cannot have IBM Qiskit's Quantum Communication with
        # Continuous Variables by Fiber Optic Interfaces' Hardware
        else:

            # Raise a Value Error
            raise ValueError("Only Quantum Communication Interface and "
                             "Quantum Communication Interface with Continuous Variables Modules' Hardware "
                             "can have Quantum Communication with Continuous Variables by "
                             "Fiber Optic Interface Hardware!!!")

    # Return the IBM Qiskit's Quantum Communication with Continuous Variables by Satellites Interfaces,
    # in this IBM Qiskit's Communication Module
    def get_qiskit_quantum_communication_continuous_variable_satellites_interfaces(self):

        # If the IBM Qiskit's Communication Interface Module Hardware is Quantum or Quantum with Continuous Variables,
        # then it can have IBM Qiskit's Quantum Communication Interfaces with Continuous Variables' Hardware
        if (self.communication_module_type_tag ==
            CommunicationModuleTypes.QUANTUM_COMMUNICATION_ENUM) or \
                (self.communication_module_type_tag ==
                 CommunicationModuleTypes.QUANTUM_COMMUNICATION_CONTINUOUS_VARIABLES_ENUM):

            # Return the IBM Qiskit's Quantum Communication Interface with
            # Continuous Variables by Satellite's Hardware
            return self.qiskit_quantum_communication_continuous_variable_satellite_interfaces

        # If the IBM Qiskit's Communication Interface Module Hardware is not
        # Quantum neither Quantum with Continuous Variables,
        # then it cannot have IBM Qiskit's Quantum Communication with
        # Continuous Variables by Satellite Interfaces' Hardware
        else:

            # Raise a Value Error
            raise ValueError("Only Quantum Communication Interface and "
                             "Quantum Communication Interface with Continuous Variables Modules' Hardware "
                             "can have Quantum Communication with Continuous Variables by "
                             "Satellite Interface Hardware!!!")

    # Return the IBM Qiskit's Classical Communication by Fiber Optic Interfaces,
    # in this IBM Qiskit's Communication Module
    def get_qiskit_classical_communication_fiber_optic_interfaces(self):

        # If the IBM Qiskit's Communication Interface Module Hardware is Classical,
        # then it can have IBM Qiskit's Classical Communication Interfaces' Hardware
        if self.communication_module_type_tag == CommunicationModuleTypes.CLASSICAL_COMMUNICATION_ENUM:

            # Return the IBM Qiskit's Classical Communication Interface by Fiber Optic's Hardware
            return self.qiskit_quantum_communication_continuous_variable_fiber_optic_interfaces

        # If the IBM Qiskit's Communication Interface Module Hardware is not
        # Classical, then it cannot have IBM Qiskit's Classical Communication
        # by Fiber Optic Interfaces' Hardware
        else:

            # Raise a Value Error
            raise ValueError("Only Classical Communication Interface Modules' Hardware "
                             "can have Classical Communication by Fiber Optic Interface Hardware!!!")

    # Return the IBM Qiskit's Classical Communication by Satellites Interfaces,
    # in this IBM Qiskit's Communication Module
    def get_qiskit_classical_communication_satellites_interfaces(self):

        # If the IBM Qiskit's Communication Interface Module Hardware is Classical,
        # then it can have IBM Qiskit's Classical Communication Interfaces' Hardware
        if self.communication_module_type_tag == CommunicationModuleTypes.CLASSICAL_COMMUNICATION_ENUM:

            # Return the IBM Qiskit's Quantum Communication Interface with
            # Continuous Variables by Satellite's Hardware
            return self.qiskit_quantum_communication_continuous_variable_satellite_interfaces

        # If the IBM Qiskit's Communication Interface Module Hardware is not
        # Classical, then it cannot have IBM Qiskit's Classical Communication
        # by Satellite Interfaces' Hardware
        else:

            # Raise a Value Error
            raise ValueError("Only Classical Communication Interface Modules' Hardware "
                             "can have Classical Communication by Satellite Interface Hardware!!!")
