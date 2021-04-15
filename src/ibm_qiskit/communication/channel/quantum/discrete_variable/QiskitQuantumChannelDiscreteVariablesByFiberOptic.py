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


# Constants

# The number of Wires needed for the Quantum Communication, using Discrete Variables, by Fiber Optic Interface
NUM_QUBITS_BITS = 1


# Class of the IBM Qiskit's Quantum Channel with Discrete Variables, By Fiber Optic
class QiskitQuantumChannelDiscreteVariablesByFiberOptic:

    # Constructor of the IBM Qiskit's Quantum Channel with Discrete Variables, By Fiber Optic
    def __init__(self,
                 quantum_communication_interface_fiber_optic_out,
                 quantum_communication_interface_fiber_optic_in):

        # If the Quantum Communication Interfaces are
        # IBM Qiskit's Quantum Communication with Discrete Variables, by Fiber Optic Interfaces
        if (isinstance(quantum_communication_interface_fiber_optic_out,
                       QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                       .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface)) and \
            (isinstance(quantum_communication_interface_fiber_optic_in,
                        QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface
                        .QiskitQuantumCommunicationDiscreteVariablesFiberOpticInterface)):

            # If the respective IBM Qiskit's Quantum Communication with Discrete Variables, by Fiber Optic Interfaces,
            # are set correctly, as In and Out Ports, respectively
            if (quantum_communication_interface_fiber_optic_out
                    .get_quantum_communication_discrete_variables_fiber_optic_interface_port_flag().upper() ==
                    CommunicationInterfacesModesTypes.OUT_PORT) and \
                (quantum_communication_interface_fiber_optic_in
                 .get_quantum_communication_discrete_variables_fiber_optic_interface_port_flag() ==
                 CommunicationInterfacesModesTypes.IN_PORT):

                # The Out Port of the Quantum Communication, using Discrete Variables, by Fiber Optic Interface
                self.quantum_communication_interface_fiber_optic_out = \
                    quantum_communication_interface_fiber_optic_out

                # The In Port of the Quantum Communication, using Discrete Variables, by Fiber Optic Interface
                self.quantum_communication_interface_fiber_optic_in = \
                    quantum_communication_interface_fiber_optic_in

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
