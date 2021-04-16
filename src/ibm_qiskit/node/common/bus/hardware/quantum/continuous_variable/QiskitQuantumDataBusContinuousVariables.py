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

# Import the IBM's Qiskit Hybrid Memory from the IBM_Qiskit.Node.Common.Memory.Hardware.Hybrid
from src.ibm_qiskit.node.common.memory.hardware.hybrid import QiskitHybridMemory

# Import the IBM's Qiskit Semi-Quantum Memory from the IBM_Qiskit.Node.Common.Memory.Hardware.Semi_Quantum
from src.ibm_qiskit.node.common.memory.hardware.semi_quantum import QiskitSemiQuantumMemory

# Import the IBM's Qiskit Quantum Memory from the IBM_Qiskit.Node.Common.Memory.Hardware.Quantum
from src.ibm_qiskit.node.common.memory.hardware.quantum import QiskitQuantumMemory

# Import the IBM's Qiskit Quantum Communication with Continuous Variables, by Fiber Optic Interface from
# the IBM_Qiskit.Node.Common.Memory.Hardware.Quantum.Continuous_Variable.Fiber_Optic
from src.ibm_qiskit.node.common.communication.hardware.quantum.continuous_variable.fiber_optic import \
    QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface

# Import the IBM's Qiskit Quantum Communication with Continuous Variables, by Satellite Interface from
# the IBM_Qiskit.Node.Common.Memory.Hardware.Quantum.Continuous_Variable.Satellite
from src.ibm_qiskit.node.common.communication.hardware.quantum.continuous_variable.satellite import \
    QiskitQuantumCommunicationContinuousVariablesSatelliteInterface


# Class of the IBM Qiskit's Quantum Data Bus, with Continuous Variables
class QiskitQuantumDataBusContinuousVariables:

    # Constructor of the IBM Qiskit's Quantum Data Bus, with Continuous Variables
    def __init__(self, qiskit_quantum_data_memory, qiskit_quantum_communication_continuous_variables_interface):

        # If the type of Memory provided to the Quantum Data Bus, with Continuous Variables,
        # supports Quantum Data/Information (i.e., Hybrid, Semi-Quantum or Quantum Memories)
        if ((isinstance(qiskit_quantum_data_memory, QiskitHybridMemory.QiskitHybridMemory)) or
                (isinstance(qiskit_quantum_data_memory, QiskitSemiQuantumMemory.QiskitSemiQuantumMemory)) or
                (isinstance(qiskit_quantum_data_memory, QiskitQuantumMemory.QiskitQuantumMemory))):

            # Set the Memory provided of the Quantum Data Bus, with Continuous Variables
            self.qiskit_quantum_data_memory = qiskit_quantum_data_memory

            # If the type of Communication Interface provided to the Quantum Data Bus,
            # with Continuous Variables, supports Quantum Data/Information
            # (Quantum Communication with Continuous Variables, by Fiber Optic and/or Satellite Interfaces)
            if ((isinstance(qiskit_quantum_communication_continuous_variables_interface,
                            QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                            .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface)) or
                    (isinstance(qiskit_quantum_communication_continuous_variables_interface,
                                QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                                .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface))):

                # Set the Communication Interface of the Quantum Data Bus, with Continuous Variables
                self.qiskit_quantum_communication_continuous_variables_interface = \
                    qiskit_quantum_communication_continuous_variables_interface

                # Initialise the Quantum Circuit for the connection of the Quantum Data Bus, with Continuous Variables
                self.qiskit_quantum_data_bus_continuous_variables_quantum_circuit = None

            # If the type of Communication Interface provided to the Quantum Data Bus,
            # with Continuous Variables, supports Quantum Data/Information
            # (Quantum Communication with Continuous Variables, by Fiber Optic and/or Satellite Interfaces,
            #  as also, Classical Communication Interfaces)
            else:

                # Raise a Value Error
                raise ValueError("A Quantum Data Bus, with Continuous Variables "
                                 "can only handle Communication Interfaces that "
                                 "support management of Quantum Data/Information, with Continuous Variables, such as, "
                                 "Communication Interfaces that are Quantum with Continuous Variables, "
                                 "by Fiber Optic or Satellite!!!")

        # If the type of Memory provided to the Quantum Data Bus, with Continuous Variables,
        # does not supports Quantum Information (i.e., Classical Memories)
        else:

            # Raise a Value Error
            raise ValueError("A Quantum Data Bus, with Continuous Variables can only handle Memories that "
                             "support management of Quantum Data/Information, such as, "
                             "Memories that are Hybrid, Semi-Quantum or Quantum!!!")

    # Return the Memory associated to the Quantum Data Bus, with Continuous Variables
    def get_qiskit_quantum_data_memory(self):
        return self.qiskit_quantum_data_memory

    # Return the Quantum Communication Interface associated to the Quantum Data Bus, with Continuous Variables
    def get_qiskit_quantum_communication_continuous_variables_interface(self):
        return self.qiskit_quantum_communication_continuous_variables_interface

    # Disconnect the Memory and Communication Interface associated to the Quantum Data Bus, with Continuous Variables
    def disconnect_memory_with_communication_interface(self):
        self.qiskit_quantum_data_bus_continuous_variables_quantum_circuit = None

    # Connect the Memory and Communication Interface associated to the Quantum Data Bus, with Continuous Variables
    def connect_memory_with_communication_interface(self):

        # Retrieve the Memory associated to the Quantum Data Bus, with Continuous Variables
        qiskit_quantum_data_memory = self.get_qiskit_quantum_data_memory()

        # If the type of Memory associated to the Quantum Data Bus, with Continuous Variables,
        # supports Quantum Data/Information by a Hybrid Memory
        if isinstance(qiskit_quantum_data_memory, QiskitHybridMemory.QiskitHybridMemory):

            # Retrieve the Hybrid Memory associated to the Quantum Data Bus, with Continuous Variables
            qiskit_quantum_data_memory_quantum_circuit = \
                qiskit_quantum_data_memory.get_qiskit_quantum_circuit_hybrid_memory()

        # If the type of Memory associated to the Quantum Data Bus, with Continuous Variables,
        # supports Quantum Data/Information by a Semi-Quantum Memory
        elif isinstance(qiskit_quantum_data_memory, QiskitSemiQuantumMemory.QiskitSemiQuantumMemory):

            # Retrieve the Semi-Quantum Memory associated to the Quantum Data Bus, with Continuous Variables
            qiskit_quantum_data_memory_quantum_circuit = \
                qiskit_quantum_data_memory.get_qiskit_quantum_circuit_semi_quantum_memory()

        # If the type of Memory provided to the Quantum Data Bus, with Continuous Variables,
        # supports Quantum Data/Information by a Quantum Memory
        elif isinstance(qiskit_quantum_data_memory, QiskitQuantumMemory.QiskitQuantumMemory):

            # Retrieve the Quantum Memory associated to the Quantum Data Bus, with Continuous Variables
            qiskit_quantum_data_memory_quantum_circuit = \
                qiskit_quantum_data_memory.get_qiskit_quantum_circuit_quantum_memory()

        # If the type of Memory provided to the Quantum Data Bus, with Continuous Variables,
        # does not support Quantum Data/Information, at all
        else:

            # Raise a Value Error
            raise ValueError("A Quantum Data Bus, with Continuous Variables can only handle Memories that "
                             "support management of Quantum Data/Information, such as, "
                             "Memories that are Hybrid, Semi-Quantum or Quantum!!!")

        # Retrieve the Communication Interface associated to the Quantum Data Bus, with Continuous Variables
        qiskit_quantum_communication_continuous_variables_interface = \
            self.get_qiskit_quantum_communication_continuous_variables_interface()

        # If the type of Communication Interface provided to the Quantum Data Bus,
        # with Continuous Variables, supports Quantum Data/Information,
        # by a Quantum Communication with Continuous Variables, by Fiber Optic Interface
        if (isinstance(qiskit_quantum_communication_continuous_variables_interface,
                       QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                       .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface)):

            # Retrieve the Quantum Communication associated to the Quantum Data Bus, with Continuous Variables
            qiskit_quantum_communication_continuous_variables_interface_quantum_circuit = \
                qiskit_quantum_communication_continuous_variables_interface\
                .get_qiskit_quantum_circuit_quantum_communication_continuous_variables_fiber_optic_interface()

            # Set the Quantum Communication, with Continuous Variables, by Fiber Optic Interface, as Busy
            qiskit_quantum_communication_continuous_variables_interface \
                .set_quantum_communication_continuous_variables_fiber_optic_interface_busy()

        # If the type of Communication Interface provided to the Quantum Data Bus,
        # with Continuous Variables, supports Quantum Data/Information,
        # by a Quantum Communication with Continuous Variables, by Satellite Interface
        elif (isinstance(qiskit_quantum_communication_continuous_variables_interface,
                         QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                         .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface)):

            # Retrieve the Quantum Communication associated to the Quantum Data Bus, with Continuous Variables
            qiskit_quantum_communication_continuous_variables_interface_quantum_circuit = \
                qiskit_quantum_communication_continuous_variables_interface\
                .get_qiskit_quantum_circuit_quantum_communication_continuous_variables_satellite_interface()

            # Set the Quantum Communication, with Continuous Variables, by Satellite Interface, as Busy
            self.qiskit_quantum_communication_continuous_variables_interface \
                .set_quantum_communication_continuous_variables_satellite_interface_busy()

        # If the type of Communication Interface associated to the Quantum Data Bus,
        # with Continuous Variables, does not support Quantum Data/Information, with Continuous Variables, at all
        else:

            # Raise a Value Error
            raise ValueError("A Quantum Data Bus, with Continuous Variables "
                             "can only handle Communication Interfaces that "
                             "support management of Quantum Data/Information, with Continuous Variables, such as, "
                             "Communication Interfaces that are Quantum with Continuous Variables, "
                             "by Fiber Optic or Satellite!!!")

        # Create the temporary IBM Qiskit's Circuit, representing the connection between
        # the Memory provided to the Quantum Data Bus, with Continuous Variables and
        # the Communication Interface provided to the Quantum Data Bus, with Continuous Variables
        self.qiskit_quantum_data_bus_continuous_variables_quantum_circuit = \
            qiskit_quantum_data_memory_quantum_circuit \
            .combine_quantum_circuit(
                "qcquantumdatabuscontinuousvariables-{}-{}"
                .format(
                    self.qiskit_quantum_data_memory
                        .get_quantum_memory_id(),
                    self.qiskit_quantum_communication_continuous_variables_interface
                        .get_quantum_communication_continuous_variables_satellite_interface_id()
                ),
                qiskit_quantum_communication_continuous_variables_interface_quantum_circuit,
                global_phase=0)

        # If the type of Communication Interface provided to the Quantum Data Bus,
        # with Continuous Variables, supports Quantum Data/Information
        # (Quantum Communication with Continuous Variables, by Fiber Optic)
        if (isinstance(self.qiskit_quantum_communication_continuous_variables_interface,
                       QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface
                           .QiskitQuantumCommunicationContinuousVariablesFiberOpticInterface)):

            # Set the Quantum Communication, with Continuous Variables, by Fiber Optic Interface, as Idle
            self.qiskit_quantum_communication_continuous_variables_interface \
                .set_quantum_communication_continuous_variables_fiber_optic_interface_idle()

        # If the type of Communication Interface provided to the Quantum Data Bus,
        # with Continuous Variables, supports Quantum Data/Information
        # (Quantum Communication with Continuous Variables, by Fiber Optic and/or Satellite Interfaces)
        if (isinstance(self.qiskit_quantum_communication_continuous_variables_interface,
                       QiskitQuantumCommunicationContinuousVariablesSatelliteInterface
                           .QiskitQuantumCommunicationContinuousVariablesSatelliteInterface)):

            # Set the Quantum Communication, with Continuous Variables, by Satellite Interface, as Idle
            self.qiskit_quantum_communication_continuous_variables_interface \
                .set_quantum_communication_continuous_variables_satellite_interface_idle()

    # Exchange Quantum Data/Information between the provided slots/indexes
    # in the Memory and the Communication Interface, managing Quantum Data/Information with Continuous Variables
    def exchange_quantum_data_information_via_bus(self, qiskit_memory_qubit_slot_index,
                                                  qiskit_communication_interface_qubit_slot):

        # Apply the SWAP Gate to the IBM Qiskit's Quantum Circuit representing
        # the Quantum Data Bus, with Continuous Variables
        self.qiskit_quantum_data_bus_continuous_variables_quantum_circuit\
            .apply_swap(qiskit_memory_qubit_slot_index, qiskit_communication_interface_qubit_slot)
