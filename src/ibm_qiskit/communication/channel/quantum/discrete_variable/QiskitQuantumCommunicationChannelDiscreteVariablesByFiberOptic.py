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

# Import CommunicationInterfacesModesTypes from the
from src.common.enumerations import CommunicationInterfacesModesTypes

# Import the IBM Qiskit's Quantum Communication with Discrete Variables, by Fiber Optic Interface
from src.ibm_qiskit.node.common.communication.hardware.quantum.discrete_variable.fiber_optic import \
    QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface

# Import QiskitQuantumCircuit from IBM_Qiskit.Circuit
from src.ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister


# Constants

# The number of Wires needed for the Quantum Communication, using Discrete Variables, by Fiber Optic Interface
NUM_QUBITS_BITS = 1


# Class of the IBM Qiskit's Quantum Communication Channel with Discrete Variables, By Fiber Optic
class QiskitQuantumCommunicationChannelDiscreteVariablesByFiberOptic:

    # Constructor of the IBM Qiskit's Quantum Channel with Discrete Variables, By Fiber Optic
    def __init__(self, fiber_optic_cable,
                 quantum_communication_discrete_variables_fiber_optic_interface_sender,
                 quantum_communication_discrete_variables_fiber_optic_interface_receiver):

        # If the Quantum Communication Interfaces are
        # IBM Qiskit's Quantum Communication with Discrete Variables, by Fiber Optic Interfaces
        if (isinstance(quantum_communication_discrete_variables_fiber_optic_interface_sender,
                       QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                       .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface)) and \
            (isinstance(quantum_communication_discrete_variables_fiber_optic_interface_receiver,
                        QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                        .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface)):

            # If the respective IBM Qiskit's Quantum Communication with Discrete Variables, by Fiber Optic Interfaces,
            # are set correctly, as Out and In Ports, regarding the Sender and the Receiver, respectively
            if (quantum_communication_discrete_variables_fiber_optic_interface_sender
                    .get_quantum_communication_discrete_variables_fiber_optic_interface_port_flag().upper() ==
                    CommunicationInterfacesModesTypes.OUT_PORT) and \
                (quantum_communication_discrete_variables_fiber_optic_interface_receiver
                 .get_quantum_communication_discrete_variables_fiber_optic_interface_port_flag() ==
                 CommunicationInterfacesModesTypes.IN_PORT):

                # Set the Fiber Optic Cable
                self.fiber_optic_cable = fiber_optic_cable

                # The Sender of the Quantum Communication, using Discrete Variables, by Fiber Optic Interface
                self.quantum_communication_discrete_variables_fiber_optic_interface_sender = \
                    quantum_communication_discrete_variables_fiber_optic_interface_sender

                # The Receiver of the Quantum Communication, using Discrete Variables, by Fiber Optic Interface
                self.quantum_communication_discrete_variables_fiber_optic_interface_receiver = \
                    quantum_communication_discrete_variables_fiber_optic_interface_receiver

                # Initialise the Quantum Register for
                # the IBM Qiskit's Quantum Communication Channel with Discrete Variables, By Fiber Optic Medium
                self.quantum_register_quantum_communication_channel_discrete_variables_fiber_optic = None

                # Initialise the Classical Register for
                # the IBM Qiskit's Quantum Communication Channel with Discrete Variables, By Fiber Optic Medium
                self.classical_register_quantum_communication_channel_discrete_variables_fiber_optic = None

                # Initialise the Quantum Circuit for
                # the IBM Qiskit's Quantum Communication Channel with Discrete Variables, By Fiber Optic Medium
                self.quantum_circuit_quantum_communication_channel_discrete_variables_fiber_optic = None

                # Set the boolean flag of the Idle Status of
                # the IBM Qiskit's Quantum Channel with Discrete Variables, By Fiber Optic, as True
                self.quantum_communication_channel_discrete_variables_fiber_optic_idle = True

            # If the respective IBM Qiskit's Quantum Communication with Discrete Variables, by Fiber Optic Interfaces,
            # are not set correctly, as In and Out Ports, respectively
            else:

                raise RuntimeError("The Ports of the Quantum Communication with Discrete Variables, "
                                   "by Fiber Optic Interfaces are not set correctly!!!")

        # If the Quantum Communication Interfaces are not
        # IBM Qiskit's Quantum Communication with Discrete Variables, by Fiber Optic Interfaces
        else:

            # Raise a Runtime Error
            raise RuntimeError("Only Quantum Communication with Discrete Variables, by Fiber Optic Interfaces "
                               "can be used on the Quantum Channel with Discrete Variables, by Fiber Optic!!!")

    # Initialise the Medium of the IBM Qiskit's Quantum Communication Channel,
    # using Discrete Variables, by Fiber Optics
    def initialise_quantum_communication_channel_medium(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = NUM_QUBITS_BITS

        # Initialisation of the IBM Qiskit's Quantum Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Medium
        self.quantum_register_quantum_communication_channel_discrete_variables_fiber_optic = \
            QiskitQuantumRegister \
            .QiskitQuantumRegister("qrquantumcommunicationchanneldiscretevariablesfiberopticmediumidle{}"
                                   .format(self),
                                   num_qubits)

        # Initialisation of the IBM Qiskit's Classical Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Medium
        self.classical_register_quantum_communication_channel_discrete_variables_fiber_optic = \
            QiskitClassicalRegister \
            .QiskitClassicalRegister("crquantumcommunicationchanneldiscretevariablesfiberopticmediumidle{}"
                                     .format(self.fiber_optic_cable.get_fiber_optic_cable_id()),
                                     num_bits)

        # Initialisation of the IBM Qiskit's Quantum Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Medium,
        # with one Quantum and Classical Registers
        self.quantum_circuit_quantum_communication_channel_discrete_variables_fiber_optic = \
            QiskitQuantumCircuit \
            .QiskitQuantumCircuit("qcquantumcommunicationchanneldiscretevariablesfiberopticmediumidle{}"
                                  .format(self.fiber_optic_cable.get_fiber_optic_cable_id()),
                                  self.quantum_register_quantum_communication_channel_discrete_variables_fiber_optic,
                                  self.classical_register_quantum_communication_channel_discrete_variables_fiber_optic,
                                  global_phase=0)

    # End a Quantum Communication,
    # through the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface
    def end_quantum_communication(self):

        # Reset (initialise) the IBM Qiskit's Quantum Circuit, Quantum Register and Classical Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface,
        # for the Sender Party
        self.quantum_communication_discrete_variables_fiber_optic_interface_sender.initialise_interface()

        # Reset (initialise) the IBM Qiskit's Quantum Circuit, Quantum Register and Classical Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface,
        # for the Receiver Party
        self.quantum_communication_discrete_variables_fiber_optic_interface_receiver.initialise_interface()

        # Set the boolean flag of the Idle Status of
        # the IBM Qiskit's Quantum Channel with Discrete Variables, By Fiber Optic, as True
        self.quantum_communication_channel_discrete_variables_fiber_optic_idle = True

    # Start a Quantum Communication Session,
    # through the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Fiber Optic Interface, between two Users/Clients
    def start_quantum_communication(self):

        # If the IBM Qiskit's Quantum Communication Channel,
        # using Discrete Variables, by Fiber Optic is currently Idle
        if self.quantum_communication_channel_discrete_variables_fiber_optic_idle:

            # Set the Quantum Communication Interface with Discrete Variables, by Fiber Optic Interface,
            # for the Sender, as Busy, at the moment
            self.quantum_communication_discrete_variables_fiber_optic_interface_sender\
                .set_quantum_communication_fiber_optic_interface_busy()

            # Set the Quantum Communication Interface with Discrete Variables, by Fiber Optic Interface,
            # for the Receiver, as Busy, at the moment
            self.quantum_communication_discrete_variables_fiber_optic_interface_receiver\
                .set_quantum_communication_fiber_optic_interface_busy()

            # Retrieve the Quantum Circuit for the Quantum Communication,
            # with Discrete Variables, by Fiber Optic, for the Sender
            quantum_circuit_quantum_communication_discrete_variables_fiber_optic_interface_sender = \
                self.quantum_communication_discrete_variables_fiber_optic_interface_sender\
                .get_qiskit_quantum_circuit_quantum_communication_fiber_optic_interface()

            # Retrieve the Quantum Circuit for the Quantum Communication,
            # with Discrete Variables, by Fiber Optic, for the Receiver
            quantum_circuit_quantum_communication_discrete_variables_fiber_optic_interface_receiver = \
                self.quantum_communication_discrete_variables_fiber_optic_interface_receiver\
                .get_qiskit_quantum_circuit_quantum_communication_fiber_optic_interface()

            # Create the temporary IBM Qiskit's Circuit, representing the first connection
            # (Sender -> Quantum Communication Fiber Optic)
            qiskit_quantum_circuit_temporary = \
                quantum_circuit_quantum_communication_discrete_variables_fiber_optic_interface_sender \
                .combine_quantum_circuit(
                    "qcquantumcommunicationdiscretevariablesfiberopticinterfacetemp{}"
                    .format(
                        self.fiber_optic_cable.get_fiber_optic_cable_id()
                    ),
                    self.quantum_circuit_quantum_communication_channel_discrete_variables_fiber_optic,
                    global_phase=0)

            # Create the final IBM Qiskit's Circuit, representing the second and last connection
            # (Sender -> Quantum Communication Fiber Optic -> Receiver)
            self.quantum_circuit_quantum_communication_channel_discrete_variables_fiber_optic = \
                qiskit_quantum_circuit_temporary \
                .combine_quantum_circuit(
                    "qcquantumcommunicationdiscretevariablesfiberopticinterfacestarted{}"
                    .format(
                        self.fiber_optic_cable.get_fiber_optic_cable_id()
                    ),
                    quantum_circuit_quantum_communication_discrete_variables_fiber_optic_interface_receiver,
                    global_phase=0)

            # Set the boolean flag of the Idle Status of
            # the IBM Qiskit's Quantum Channel with Discrete Variables, By Fiber Optic, as True
            self.quantum_communication_channel_discrete_variables_fiber_optic_idle = False

        # If the IBM Qiskit's Quantum Communication,
        # using Discrete Variables, by Fiber Optic Interface is currently being used
        else:

            # Raise a Value Error
            raise ValueError("The Quantum Communication, "
                             "using Discrete Variables, by Fiber Optic Interface is currently being used!!!")

    # Send the Quantum Information over Discrete Variables by Fiber Optic Channel Medium
    def send_quantum_information_over_discrete_variables_fiber_optic_channel(self):

        # If the Quantum Communication Channel with Discrete Variables, by Fiber Optic is not Idle
        if not self.quantum_communication_channel_discrete_variables_fiber_optic_idle:

            # Apply the SWAP Gate between the Sender's Qubit and Medium's Qubit
            self.quantum_circuit_quantum_communication_channel_discrete_variables_fiber_optic\
                .apply_swap(CommunicationInterfacesModesTypes.SENDER_INTERFACE_ID,
                            CommunicationInterfacesModesTypes.MEDIUM_INTERFACE_ID)

            # Apply the SWAP Gate between the Medium's Qubit and Receiver's Qubit
            self.quantum_circuit_quantum_communication_channel_discrete_variables_fiber_optic\
                .apply_swap(CommunicationInterfacesModesTypes.MEDIUM_INTERFACE_ID,
                            CommunicationInterfacesModesTypes.RECEIVER_INTERFACE_ID)

        # If the Quantum Communication Channel with Discrete Variables, by Fiber Optic is Idle
        else:

            # Raise the Runtime Error
            raise RuntimeError("The Quantum Communication Channel with Discrete Variables, "
                               "by Fiber Optic Interface, Medium is Idle!!!")
