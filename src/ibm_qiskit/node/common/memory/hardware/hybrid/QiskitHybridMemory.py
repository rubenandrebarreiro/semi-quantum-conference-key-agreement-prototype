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

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister


# Class for the IBM Qiskit's Hybrid Memory
class QiskitHybridMemory:

    # Constructor of the IBM Qiskit's Hybrid Memory
    def __init__(self, hybrid_memory_id, hybrid_memory_num_qubits, hybrid_memory_num_bits):

        # The ID of the IBM Qiskit's Hybrid Memory
        self.hybrid_memory_id = hybrid_memory_id

        # The number of Qubits of the IBM Qiskit's Hybrid Memory
        self.hybrid_memory_num_qubits = hybrid_memory_num_qubits

        # The number of Bits of the IBM Qiskit's Hybrid Memory
        self.hybrid_memory_num_bits = hybrid_memory_num_bits

        # The tag for the Memory Type for the IBM Qiskit's Hybrid Memory
        self.hybrid_memory_type_tag = MemoryModuleTypes.HYBRID_MEMORY_ENUM

        # Create the Quantum Register for the IBM Qiskit's Hybrid Memory
        qiskit_quantum_register_hybrid_memory = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrhybridmemory{}".format(self.hybrid_memory_id),
                                                        hybrid_memory_num_qubits)

        # Create the Classical Register for the IBM Qiskit's Hybrid Memory
        qiskit_classical_register_hybrid_memory = \
            QiskitClassicalRegister.QiskitClassicalRegister("crhybridmemory{}".format(self.hybrid_memory_id),
                                                            hybrid_memory_num_bits)

        # The Quantum Circuit for this IBM Qiskit's Hybrid Memory
        self.qiskit_quantum_circuit_hybrid_memory = \
            QiskitQuantumCircuit\
            .QiskitQuantumCircuit("qchybridmemory{}".format(self.hybrid_memory_id),
                                  quantum_registers=qiskit_quantum_register_hybrid_memory,
                                  classical_registers=qiskit_classical_register_hybrid_memory,
                                  global_phase=0, quantum_circuit=None,
                                  memory_enumeration_tag=self.hybrid_memory_type_tag)

    # Return the ID of the Hybrid Memory
    def get_hybrid_memory_id(self):
        return self.hybrid_memory_id

    # Return the number of Qubits of the Hybrid Memory
    def get_hybrid_memory_num_qubits(self):
        return self.hybrid_memory_num_qubits

    # Return the number of Bits of the Hybrid Memory
    def get_hybrid_memory_num_bits(self):
        return self.hybrid_memory_num_bits

    # Return the tag for the Memory Type for the IBM Qiskit's Hybrid Memory
    def get_hybrid_memory_type_tag(self):
        return self.hybrid_memory_type_tag
