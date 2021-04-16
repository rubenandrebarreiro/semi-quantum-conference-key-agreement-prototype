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

# Import QiskitQuantumCircuit from IBM_Qiskit.Circuit
from src.ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister


# Constants

# The number of Wires needed for the Quantum Communication, using Discrete Variables, by Fiber Optic Interface
NUM_QUBITS_BITS = 1


# Class for IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface
class QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface:

    # Constructor for IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface
    def __init__(self, quantum_communication_discrete_variables_fiber_optic_interface_id,
                 quantum_communication_discrete_variables_fiber_optic_interface_port_flag):

        # If the Port Flag for the IBM Qiskit's Quantum Communication,
        # using Discrete Variables, by Fiber Optic Interface, is valid
        if (quantum_communication_discrete_variables_fiber_optic_interface_port_flag.upper() ==
            CommunicationInterfacesModesTypes.OUT_PORT) or \
                (quantum_communication_discrete_variables_fiber_optic_interface_port_flag.upper() ==
                    CommunicationInterfacesModesTypes.IN_PORT):

            # Initialise the ID of the IBM Qiskit's Quantum Communication,
            # using Discrete Variables, by Fiber Optic Interface
            self.quantum_communication_discrete_variables_fiber_optic_interface_id = \
                quantum_communication_discrete_variables_fiber_optic_interface_id

            # Initialise the Port Flag for the IBM Qiskit's Quantum Communication,
            # using Discrete Variables, by Fiber Optic Interface
            self.quantum_communication_discrete_variables_fiber_optic_interface_port_flag = \
                quantum_communication_discrete_variables_fiber_optic_interface_port_flag.upper()

            # Initialise the Fiber Optic Cable, as None
            self.fiber_optic_cable = None

            # Set the Boolean Flag, responsible to keep the information about if
            # the Fiber Optic Cable is installed or not
            self.fiber_optic_cable_installed = False

            # Initialise the IBM Qiskit's Quantum Circuit, Quantum Register and Classical Register,
            # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface
            self.qiskit_quantum_register_quantum_communication_discrete_variables_fiber_optic_interface = None
            self.qiskit_classical_register_quantum_communication_discrete_variables_fiber_optic_interface = None
            self.qiskit_quantum_circuit_quantum_communication_discrete_variables_fiber_optic_interface = None

            # Initialise the Boolean Flag, responsible to keep the information about the Idle status of
            # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface, itself
            self.quantum_communication_discrete_variables_fiber_optic_interface_idle = True

        # If the Port Flag for the IBM Qiskit's Quantum Communication,
        # using Discrete Variables, by Fiber Optic Interface, is not valid
        else:

            # Raise a Value Error
            raise ValueError("The Port Flag for this Fiber Optic Interface is not valid!!!")

    # Return the ID of the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Fiber Optic Interface
    def get_quantum_communication_discrete_variables_fiber_optic_interface_id(self):
        return self.quantum_communication_discrete_variables_fiber_optic_interface_id

    # Return the Port Flag for the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Fiber Optic Interface
    def get_quantum_communication_discrete_variables_fiber_optic_interface_port_flag(self):
        return self.quantum_communication_discrete_variables_fiber_optic_interface_port_flag

    # Return the currently installed Fiber Optic Cable of
    # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface
    def get_fiber_optic_cable(self):
        return self.fiber_optic_cable

    # Install the a new Fiber Optic Cable to
    # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface
    def install_fiber_optic_cable(self, fiber_optic_cable):

        # If there is no Fiber Optic Cable currently installed, it is possible to install one
        if not self.is_fiber_optic_cable_installed():
            self.fiber_optic_cable = fiber_optic_cable
            self.fiber_optic_cable_installed = True

        # If there is one Fiber Optic Cable already installed, it is not possible to install one
        else:

            # Raise a Value Error
            raise ValueError("One Fiber Optic Cable is already installed in "
                             "the Quantum Communication, using Discrete Variables, by Fiber Optic Interface!!!")

    # Uninstall the currently installed Fiber Optic Cable on
    # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface
    def uninstall_fiber_optic_cable(self):

        # If there is one Fiber Optic Cable already installed, it is possible to uninstall none
        if self.is_fiber_optic_cable_installed():
            self.fiber_optic_cable = None
            self.fiber_optic_cable_installed = False

        # If there is no Fiber Optic Cable currently installed, it is not possible to uninstall one
        else:

            # Raise a Value Error
            raise ValueError("No Fiber Optic Cable is currently installed in "
                             "the Quantum Communication, using Discrete Variables, by Fiber Optic Interface!!!")

    # Return the Boolean Flag, responsible to keep the information about if
    # the Fiber Optic Cable is installed or not
    def is_fiber_optic_cable_installed(self):
        return self.fiber_optic_cable_installed

    # Return the IBM Qiskit's Quantum Register from the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Fiber Optic Interface
    def get_qiskit_quantum_register_quantum_communication_discrete_variables_fiber_optic_interface(self):
        return self.qiskit_quantum_register_quantum_communication_discrete_variables_fiber_optic_interface

    # Return the IBM Qiskit's Classical Register from the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Fiber Optic Interface
    def get_qiskit_classical_register_quantum_communication_discrete_variables_fiber_optic_interface(self):
        return self.qiskit_classical_register_quantum_communication_discrete_variables_fiber_optic_interface

    # Return the IBM Qiskit's Quantum Circuit from the IBM Qiskit's Quantum Communication,
    # using Discrete Variables, by Fiber Optic Interface
    def get_qiskit_quantum_circuit_quantum_communication_discrete_variables_fiber_optic_interface(self):
        return self.qiskit_quantum_circuit_quantum_communication_discrete_variables_fiber_optic_interface

    # Return the Boolean Flag, responsible to keep the information about the Idle status of
    # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface itself
    def is_quantum_communication_fiber_optic_interface_idle(self):
        return self.quantum_communication_discrete_variables_fiber_optic_interface_idle

    # Set the Boolean Flag, responsible to keep the information about the Idle status of
    # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface itself, as False
    def set_quantum_communication_discrete_variables_fiber_optic_interface_busy(self):
        self.quantum_communication_discrete_variables_fiber_optic_interface_idle = False

    # Set the Boolean Flag, responsible to keep the information about the Idle status of
    # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface itself, as True
    def set_quantum_communication_discrete_variables_fiber_optic_interface_idle(self):
        self.quantum_communication_discrete_variables_fiber_optic_interface_idle = True

    # Initialise the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface
    def initialise_interface(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = NUM_QUBITS_BITS

        # Creation of the IBM Qiskit's Quantum Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface
        self.qiskit_quantum_register_quantum_communication_discrete_variables_fiber_optic_interface = \
            QiskitQuantumRegister\
            .QiskitQuantumRegister("qrquantumcommunicationdiscretevariablesfiberopticinterfaceidle{}"
                                   .format(self.quantum_communication_discrete_variables_fiber_optic_interface_id),
                                   num_qubits)

        # Creation of the IBM Qiskit's Classical Register,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface
        self.qiskit_classical_register_quantum_communication_discrete_variables_fiber_optic_interface = \
            QiskitClassicalRegister\
            .QiskitClassicalRegister("crquantumcommunicationdiscretevariablesfiberopticinterfaceidle{}"
                                     .format(self.quantum_communication_discrete_variables_fiber_optic_interface_id),
                                     num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit,
        # for the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface,
        # with one Quantum and Classical Registers
        self.qiskit_quantum_circuit_quantum_communication_discrete_variables_fiber_optic_interface = \
            QiskitQuantumCircuit\
            .QiskitQuantumCircuit(
                "qcquantumcommunicationdiscretevariablesfiberopticinterfaceidle{}"
                .format(self.quantum_communication_discrete_variables_fiber_optic_interface_id),
                self.qiskit_quantum_register_quantum_communication_discrete_variables_fiber_optic_interface,
                self.qiskit_classical_register_quantum_communication_discrete_variables_fiber_optic_interface,
                global_phase=0)

        # Initialise the Boolean Flag, responsible to keep the information about the Idle status of
        # the IBM Qiskit's Quantum Communication, using Discrete Variables, by Fiber Optic Interface, itself
        self.quantum_communication_discrete_variables_fiber_optic_interface_idle = True
