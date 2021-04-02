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
from src.ibm_qiskit.common import HardwareModuleTypes

# Import the IBM Qiskit's Hybrid Memory from IBM_Qiskit.Node.Common.Memory.Hardware.Hybrid
from src.ibm_qiskit.node.common.memory.hardware.hybrid import QiskitHybridMemory

# Import the IBM Qiskit's Quantum Memory from IBM_Qiskit.Node.Common.Memory.Hardware.Quantum
from src.ibm_qiskit.node.common.memory.hardware.quantum import QiskitQuantumMemory

# Import the IBM Qiskit's Classical Memory from IBM_Qiskit.Node.Common.Memory.Hardware.Classical
from src.ibm_qiskit.node.common.memory.hardware.classical import QiskitClassicalMemory


# Class of the IBM Qiskit's Memory Module
class QiskitMemoryModule:

    # Constructor of the IBM Qiskit's Memory Module
    def __init__(self, hardware_module_type_tag):

        # The Tag of the IBM Qiskit's Hardware Type of the IBM Qiskit's Memory Module
        self.hardware_module_type_tag = hardware_module_type_tag

        # Initialise the IBM Qiskit's Hybrid Memories of the IBM Qiskit's Memory Module
        self.qiskit_hybrid_memories = []
        self.qiskit_quantum_memories = []
        self.qiskit_classical_memories = []

    # Return the Tag of the IBM Qiskit's Hardware Type of the IBM Qiskit's Memory Module
    def get_hardware_module_type_tag(self):
        return self.hardware_module_type_tag

    # Add an abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
    def add_memory(self, qiskit_memory_to_add):

        # If the IBM Qiskit's Memory Module is Hybrid,
        # all the type of Memory Hardware (Hybrid, Quantum and Classical) can be added
        if self.hardware_module_type_tag == HardwareModuleTypes.HYBRID_HARDWARE_ENUM:

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory being given
            if isinstance(qiskit_memory_to_add, QiskitHybridMemory.QiskitHybridMemory):

                # Add the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_hybrid_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory being given
            elif isinstance(qiskit_memory_to_add, QiskitQuantumMemory.QiskitQuantumMemory):

                # Add the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_quantum_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory being given
            elif isinstance(qiskit_memory_to_add, QiskitClassicalMemory.QiskitClassicalMemory):

                # Add the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_classical_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Memory!!!")

        # If the IBM Qiskit's Memory Module is Quantum,
        # only Quantum Memory Hardware can be added
        elif self.hardware_module_type_tag == HardwareModuleTypes.QUANTUM_HARDWARE_ENUM:

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory being given
            if isinstance(qiskit_memory_to_add, QiskitHybridMemory.QiskitHybridMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to add a Hybrid Memory to a Quantum Memory Module!!!")

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory being given
            elif isinstance(qiskit_memory_to_add, QiskitQuantumMemory.QiskitQuantumMemory):

                # Add the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_quantum_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory being given
            elif isinstance(qiskit_memory_to_add, QiskitClassicalMemory.QiskitClassicalMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to add a Classical Memory to a Quantum Memory Module!!!")

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Memory!!!")

        # If the IBM Qiskit's Memory Module is Classical,
        # only Classical Memory Hardware can be added
        elif self.hardware_module_type_tag == HardwareModuleTypes.CLASSICAL_HARDWARE_ENUM:

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory being given
            if isinstance(qiskit_memory_to_add, QiskitHybridMemory.QiskitHybridMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to add a Hybrid Memory to a Quantum Memory Module!!!")

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory being given
            elif isinstance(qiskit_memory_to_add, QiskitQuantumMemory.QiskitQuantumMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to add a Classical Memory to a Quantum Memory Module!!!")

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory being given
            elif isinstance(qiskit_memory_to_add, QiskitClassicalMemory.QiskitClassicalMemory):

                # Add the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_classical_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Memory!!!")

        # If the IBM Qiskit's Memory Module is Unknown,
        # no Memory Hardware can be added and it will be raised a Value Error
        else:

            # Raise a Value Error
            raise ValueError("It is impossible to add any type of Memory to this Memory Module, "
                             "due to an Unknown Hardware type of Memory Module!!!")

    # Remove an abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
    def remove_memory(self, qiskit_memory_to_remove):

        # If the IBM Qiskit's Memory Module is Hybrid,
        # all the type of Memory Hardware (Hybrid, Quantum and Classical) can be removed
        if self.hardware_module_type_tag == HardwareModuleTypes.HYBRID_HARDWARE_ENUM:

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory being given
            if isinstance(qiskit_memory_to_remove, QiskitHybridMemory.QiskitHybridMemory):

                # Remove the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_hybrid_memories.remove(qiskit_memory_to_remove)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory being given
            elif isinstance(qiskit_memory_to_remove, QiskitQuantumMemory.QiskitQuantumMemory):

                # Remove the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_quantum_memories.remove(qiskit_memory_to_remove)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory being given
            elif isinstance(qiskit_memory_to_remove, QiskitClassicalMemory.QiskitClassicalMemory):

                # Remove the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_classical_memories.remove(qiskit_memory_to_remove)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Memory!!!")

        # If the IBM Qiskit's Memory Module is Quantum,
        # only Quantum Memory Hardware can be removed
        elif self.hardware_module_type_tag == HardwareModuleTypes.QUANTUM_HARDWARE_ENUM:

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory being given
            if isinstance(qiskit_memory_to_remove, QiskitHybridMemory.QiskitHybridMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to remove a Hybrid Memory to a Quantum Memory Module!!!")

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory being given
            elif isinstance(qiskit_memory_to_remove, QiskitQuantumMemory.QiskitQuantumMemory):

                # Add the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_quantum_memories.remove(qiskit_memory_to_remove)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory being given
            elif isinstance(qiskit_memory_to_remove, QiskitClassicalMemory.QiskitClassicalMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to remove a Classical Memory to a Quantum Memory Module!!!")

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Memory!!!")

        # If the IBM Qiskit's Memory Module is Classical,
        # only Classical Memory Hardware can be added
        elif self.hardware_module_type_tag == HardwareModuleTypes.CLASSICAL_HARDWARE_ENUM:

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory being given
            if isinstance(qiskit_memory_to_remove, QiskitHybridMemory.QiskitHybridMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to add a Hybrid Memory to a Quantum Memory Module!!!")

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory being given
            elif isinstance(qiskit_memory_to_remove, QiskitQuantumMemory.QiskitQuantumMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to remove a Classical Memory to a Quantum Memory Module!!!")

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory being given
            elif isinstance(qiskit_memory_to_remove, QiskitClassicalMemory.QiskitClassicalMemory):

                # Remove the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_classical_memories.remove(qiskit_memory_to_remove)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Memory!!!")

        # If the IBM Qiskit's Memory Module is Unknown,
        # no Memory Hardware can be added and it will be raised a Value Error
        else:

            # Raise a Value Error
            raise ValueError("It is impossible to remove any type of Memory to this Memory Module, "
                             "due to an Unknown Hardware type of Memory Module!!!")
