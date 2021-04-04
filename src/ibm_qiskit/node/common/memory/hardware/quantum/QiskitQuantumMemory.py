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

# Import the Memory Type from the IBM_Qiskit.Common
from src.common.enumerations import MemoryModuleTypes

# Import required Libraries and Packages

# Import the IBM Qiskit's Quantum Circuit from the IBM_Qiskit.Circuit
from src.ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister


# Class for the IBM Qiskit's Quantum Memory
class QiskitQuantumMemory:

    # Constructor of the IBM Qiskit's Quantum Memory
    def __init__(self, quantum_memory_id, quantum_memory_num_qubits):

        # The ID of the IBM Qiskit's Quantum Memory
        self.quantum_memory_id = quantum_memory_id

        # The number of Qubits of the IBM Qiskit's Quantum Memory
        self.quantum_memory_num_qubits = quantum_memory_num_qubits

        # The tag for the Memory Type for the IBM Qiskit's Quantum Memory
        self.quantum_memory_type_tag = MemoryModuleTypes.QUANTUM_MEMORY_ENUM

        # Create the Quantum Register for the IBM Qiskit's Quantum Memory
        qiskit_quantum_register_quantum_memory = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrquantummemory{}".format(self.quantum_memory_id),
                                                        quantum_memory_num_qubits)

        # The Quantum Circuit for this IBM Qiskit's Quantum Memory
        self.qiskit_quantum_circuit_quantum_memory = \
            QiskitQuantumCircuit\
            .QiskitQuantumCircuit("qcquantummemory{}".format(self.quantum_memory_id),
                                  quantum_registers=qiskit_quantum_register_quantum_memory,
                                  classical_registers=None,
                                  global_phase=0, quantum_circuit=None,
                                  memory_enumeration_tag=self.quantum_memory_type_tag)

    # Return the ID of the Quantum Memory
    def get_quantum_memory_id(self):
        return self.quantum_memory_id

    # Return the number of Qubits of the Quantum Memory
    def get_quantum_memory_num_qubits(self):
        return self.quantum_memory_num_qubits

    # Return the tag for the Memory Type for the IBM Qiskit's Quantum Memory
    def get_quantum_memory_type_tag(self):
        return self.quantum_memory_type_tag
