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
from src.ibm_qiskit.common import MemoryModuleTypes


# Import required Libraries and Packages

# Import the IBM Qiskit's Quantum Circuit from the IBM_Qiskit.Circuit
from src.ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister


# Class for the IBM Qiskit's Classical Memory
class QiskitClassicalMemory:

    # Constructor of the IBM Qiskit's Classical Memory
    def __init__(self, classical_memory_id, classical_memory_num_bits):

        # The ID of the IBM Qiskit's Classical Memory
        self.classical_memory_id = classical_memory_id

        # The number of Bits of the IBM Qiskit's Classical Memory
        self.classical_memory_num_bits = classical_memory_num_bits

        # The tag for the Memory Type for the IBM Qiskit's Classical Memory
        self.classical_memory_type_tag = MemoryModuleTypes.CLASSICAL_MEMORY_ENUM

        # Create the Classical Register for the IBM Qiskit's Classical Memory
        qiskit_classical_register_classical_memory = \
            QiskitClassicalRegister.QiskitClassicalRegister("crclassicalmemory{}".format(self.classical_memory_id),
                                                            classical_memory_num_bits)

        # The Quantum Circuit for this IBM Qiskit's Classical Memory
        self.qiskit_quantum_circuit_classical_memory = \
            QiskitQuantumCircuit\
            .QiskitQuantumCircuit("qcclassicalmemory{}".format(self.classical_memory_id),
                                  quantum_registers=None,
                                  classical_registers=qiskit_classical_register_classical_memory,
                                  global_phase=0, quantum_circuit=None,
                                  memory_enumeration_tag=self.classical_memory_type_tag)

    # Return the ID of the Classical Memory
    def get_classical_memory_id(self):
        return self.classical_memory_id

    # Return the number of Bits of the Classical Memory
    def get_classical_memory_num_bits(self):
        return self.classical_memory_num_bits

    # Return the tag for the Memory Type for the IBM Qiskit's Classical Memory
    def get_classical_memory_type_tag(self):
        return self.classical_memory_type_tag
