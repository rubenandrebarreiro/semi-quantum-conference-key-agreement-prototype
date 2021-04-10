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

# Import QiskitQuantumCircuit from IBM_Qiskit.Circuit
from src.ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister


# Constants

# The number of Wires needed for the Quantum Communication, using Discrete Variables, by Satellite Interface
NUM_WIRES = 3

# The Output Port of the Quantum Communication, using Discrete Variables, by Satellite Interface
OUTPUT_PORT = 0

# The Middle Media of the Quantum Communication, using Discrete Variables, by Satellite Interface
MIDDLE_MEDIA = 1

# The Input Port of the Quantum Communication, using Discrete Variables, by Satellite Interface
INPUT_PORT = 2


# Class for IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
class QiskitQuantumCommunicationDiscreteVariablesSatelliteInterface:

    # Constructor for IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
    def __init__(self, quantum_communication_satellite_interface_id):

        # Initialise the ID of the IBM Qiskit's Quantum Communication,
        # using Discrete Variables, by Satellite Interface
        self.quantum_communication_satellite_interface_id = quantum_communication_satellite_interface_id

        # Initialise the Wireless Link, as None
        self.wireless_link = None

        # Set the Boolean Flag, responsible to keep the information about if
        # the Wireless Link is configured or not
        self.wireless_link_configured = False

        # Initialise the IBM Qiskit's Quantum Circuit, Quantum Register and Classical Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
        self.qiskit_quantum_register_quantum_communication_satellite_interface = None
        self.qiskit_classical_register_quantum_communication_satellite_interface = None
        self.qiskit_quantum_circuit_quantum_communication_satellite_interface = None

        # Initialise the Boolean Flags, responsible to keep the information about the Idle status of
        # the Output/Input ports and Media Channel of the IBM Qiskit's Quantum Communication,
        # using Discrete Variable, by Satellite Interface
        self.quantum_signal_qubit_output_port_idle = True
        self.quantum_signal_qubit_media_channel_idle = True
        self.quantum_signal_qubit_input_port_idle = True

        # Initialise the Boolean Flag, responsible to keep the information about the Idle status of
        # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface, itself
        self.quantum_communication_satellite_interface_idle = True

        # Initialise the offsets, according to the number of Qubits of the Quantum Circuits,
        # of both, sender and receiver Users/Clients
        self.num_qubits_offset_sender = 0
        self.num_qubits_offset_receiver = 0

        # Initialise the Quantum Communication Session
        self.quantum_communication_sessions = []

    # Return the currently installed Wireless Link of
    # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
    def get_wireless_link(self):
        return self.wireless_link

    # Configure the a new Wireless Link to
    # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
    def configure_wireless_link(self, wireless_link):

        # If there is no Wireless Link currently configured, it is possible to configure one
        if not self.is_wireless_link_configured():
            self.wireless_link = wireless_link
            self.wireless_link_configured = True

        # If there is one Wireless Link already Configured, it is not possible to configure one
        else:

            # Raise a Value Error
            raise ValueError("One Wireless Link is already configured in "
                             "the Quantum Communication, using Discrete Variables, by Satellite Interface!!!")

    # Unconfigure the currently configured Wireless Link on
    # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
    def unconfigure_wireless_link(self):

        # If there is one Wireless Link already configured, it is possible to unconfigure none
        if self.is_wireless_link_configured():
            self.wireless_link = None
            self.wireless_link_configured = False

        # If there is no Wireless Link currently configured, it is not possible to unconfigure one
        else:

            # Raise a Value Error
            raise ValueError("No Wireless Link is currently configured in "
                             "the Quantum Communication, using Discrete Variables, by Satellite Interface!!!")

    # Return the Boolean Flag, responsible to keep the information about if
    # the Wireless Link is configured or not
    def is_wireless_link_configured(self):
        return self.wireless_link_configured

    # Return the IBM Qiskit's Quantum Register from the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Satellite Interface
    def get_qiskit_quantum_register_quantum_communication_satellite_interface(self):
        return self.qiskit_quantum_register_quantum_communication_satellite_interface

    # Return the IBM Qiskit's Classical Register from the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Satellite Interface
    def get_qiskit_classical_register_quantum_communication_satellite_interface(self):
        return self.qiskit_classical_register_quantum_communication_satellite_interface

    # Return the IBM Qiskit's Quantum Circuit from the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Satellite Interface
    def get_qiskit_quantum_circuit_quantum_communication_satellite_interface(self):
        return self.qiskit_quantum_circuit_quantum_communication_satellite_interface

    # Return the Boolean Flag, responsible to keep the information about the Idle status of
    # the Output port of the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Satellite Interface
    def is_quantum_signal_qubit_output_port_idle(self):
        return self.quantum_signal_qubit_output_port_idle

    # Return the Boolean Flag, responsible to keep the information about the Idle status of
    # the Media Channel of the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Satellite Interface
    def is_quantum_signal_qubit_media_channel_idle(self):
        return self.quantum_signal_qubit_media_channel_idle

    # Return the Boolean Flag, responsible to keep the information about the Idle status of
    # the Input port of the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Satellite Interface
    def is_quantum_signal_qubit_input_port_idle(self):
        return self.quantum_signal_qubit_input_port_idle

    # Return the Boolean Flag, responsible to keep the information about the Idle status of
    # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface itself
    def is_quantum_communication_satellite_interface_idle(self):
        return self.quantum_communication_satellite_interface_idle

    # Return the offset, according to the number of Qubits of the Quantum Circuits of Sender User/Client
    def get_num_qubits_offset_sender(self):
        return self.num_qubits_offset_sender

    # Return the offset, according to the number of Qubits of the Quantum Circuits of Receiver User/Client
    def get_num_qubits_offset_receiver(self):
        return self.num_qubits_offset_receiver

    # Initialise the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
    def initialise_interface(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = NUM_WIRES

        # Creation of the IBM Qiskit's Quantum Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
        self.qiskit_quantum_register_quantum_communication_satellite_interface = \
            QiskitQuantumRegister\
            .QiskitQuantumRegister("qrquantumcommunicationdiscretevariablessatelliteinterfaceidle{}"
                                   .format(self.quantum_communication_satellite_interface_id),
                                   num_qubits)

        # Creation of the IBM Qiskit's Classical Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
        self.qiskit_classical_register_quantum_communication_satellite_interface = \
            QiskitClassicalRegister\
            .QiskitClassicalRegister("crquantumcommunicationdiscretevariablessatelliteinterfaceidle{}"
                                     .format(self.quantum_communication_satellite_interface_id),
                                     num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface,
        # with one Quantum and Classical Registers
        self.qiskit_quantum_circuit_quantum_communication_satellite_interface = \
            QiskitQuantumCircuit\
            .QiskitQuantumCircuit("qcquantumcommunicationdiscretevariablessatelliteinterfaceidle{}"
                                  .format(self.quantum_communication_satellite_interface_id),
                                  self.qiskit_quantum_register_quantum_communication_satellite_interface,
                                  self.qiskit_classical_register_quantum_communication_satellite_interface,
                                  global_phase=0)

    # End a Quantum Communication,
    # through the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
    def end_quantum_communication_session(self):

        # Reset the IBM Qiskit's Quantum Circuit, Quantum Register and Classical Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
        self.qiskit_quantum_register_quantum_communication_satellite_interface = None
        self.qiskit_classical_register_quantum_communication_satellite_interface = None
        self.qiskit_quantum_circuit_quantum_communication_satellite_interface = None

        # Reset the Boolean Flags, responsible to keep the information about the Idle status of
        # the Output/Input ports and Media Channel of the IBM Qiskit's Quantum Communication,
        # using Discrete Variables, by Satellite Interface
        self.quantum_signal_qubit_output_port_idle = True
        self.quantum_signal_qubit_media_channel_idle = True
        self.quantum_signal_qubit_input_port_idle = True

        # Reset the Boolean Flag, responsible to keep the information about the Idle status of
        # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface itself
        self.quantum_communication_satellite_interface_idle = True

        # Reset the offsets, according to the number of Qubits of the Quantum Circuits,
        # of both, Sender and Receiver Users/Clients
        self.num_qubits_offset_sender = 0
        self.num_qubits_offset_receiver = 0

    # Start a Quantum Communication Session,
    # through the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Satellite Interface, between two Users/Clients
    def start_quantum_communication_session(self, qiskit_quantum_circuit_sender, qiskit_quantum_circuit_receiver):

        # Initialise the Boolean Flag about the Idle Status of
        # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Satellite Interface
        is_quantum_communication_fiber_optic_interface_completely_idle = \
            (self.quantum_signal_qubit_output_port_idle and
             self.quantum_signal_qubit_media_channel_idle and
             self.quantum_signal_qubit_input_port_idle and
             self.quantum_communication_satellite_interface_idle)

        # If the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic is currently Idle
        if is_quantum_communication_fiber_optic_interface_completely_idle:

            # Set the Boolean Flag, responsible to keep the information about the Idle status of
            # the IBM Qiskit's Quantum Communication,
            # using Discrete Variables, by Satellite Interface itself, as False
            self.quantum_communication_satellite_interface_idle = False

            # Retrieve the offsets, according to the number of Qubits of the Quantum Circuits,
            # of both, Sender and Receiver Users/Clients
            self.num_qubits_offset_sender = qiskit_quantum_circuit_sender.get_num_qubits()
            self.num_qubits_offset_receiver = qiskit_quantum_circuit_receiver.get_num_qubits()

            # Create the temporary IBM Qiskit's Circuit, representing the first connection
            # (Sender -> Quantum Communication Fiber Optic)
            qiskit_quantum_circuit_temporary = qiskit_quantum_circuit_sender\
                .combine_quantum_circuit("qcquantumcommunicationdiscretevariablessatelliteinterfacetemp{}"
                                         .format(self.quantum_communication_satellite_interface_id),
                                         self.qiskit_quantum_circuit_quantum_communication_satellite_interface,
                                         global_phase=0)

            # Create the final IBM Qiskit's Circuit, representing the second and last connection
            # (Sender -> Quantum Communication Fiber Optic -> Receiver)
            self.qiskit_quantum_circuit_quantum_communication_satellite_interface = \
                qiskit_quantum_circuit_temporary\
                .combine_quantum_circuit("qcquantumcommunicationdiscretevariablessatelliteinterfacestarted{}"
                                         .format(self.quantum_communication_satellite_interface_id),
                                         qiskit_quantum_circuit_receiver,
                                         global_phase=0)

        # If the IBM Qiskit's Quantum Communication,
        # using Discrete Variables, by Satellite is currently being used
        else:

            # Raise a Value Error
            raise ValueError("The Quantum Communication, "
                             "using Discrete Variables, by Satellite Interface is currently being used!!!")

    # Prepare the Quantum Signal, at the Output Port of the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Satellite Interface
    def prepare_quantum_signal_at_output_port(self):

        # Set the Boolean Flag, responsible to keep the information about the Idle status of
        # the Output port of the IBM Qiskit's Quantum Communication,
        # using Discrete Variables, by Satellite Interface, as False
        self.quantum_signal_qubit_output_port_idle = False

    # Hold the Quantum Signal, at the Media Channel of the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Satellite Interface
    def hold_quantum_signal_at_media_channel(self):

        # Set the Boolean Flag, responsible to keep the information about the Idle status of
        # the Output port of the IBM Qiskit's Quantum Communication,
        # using Discrete Variables, by Satellite Interface, as False
        self.quantum_signal_qubit_media_channel_idle = False

    # Prepare the Quantum Signal, at the Input Port of the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Satellite Interface
    def prepare_quantum_signal_at_input_port(self):

        # Set the Boolean Flag, responsible to keep the information about the Idle status of
        # the Input port of the IBM Qiskit's Quantum Communication,
        # using Discrete Variables, by Satellite Interface, as False
        self.quantum_signal_qubit_input_port_idle = False