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

# Import the IBM Qiskit's Hybrid Memory from IBM_Qiskit.Node.Common.Memory.Hardware.Hybrid
from src.ibm_qiskit.node.common.memory.hardware.hybrid import QiskitHybridMemory

# Import the IBM Qiskit's Semi-Quantum Memory from IBM_Qiskit.Node.Common.Memory.Hardware.Semi_Quantum
from src.ibm_qiskit.node.common.memory.hardware.semi_quantum import QiskitSemiQuantumMemory

# Import the IBM Qiskit's Quantum Memory from IBM_Qiskit.Node.Common.Memory.Hardware.Quantum
from src.ibm_qiskit.node.common.memory.hardware.quantum import QiskitQuantumMemory

# Import the IBM Qiskit's Classical Memory from IBM_Qiskit.Node.Common.Memory.Hardware.Classical
from src.ibm_qiskit.node.common.memory.hardware.classical import QiskitClassicalMemory


# Class of the IBM Qiskit's Memory Hardware Module
class QiskitMemoryModule:

    # Constructor of the IBM Qiskit's Memory Hardware Module
    def __init__(self, memory_module_type_tag):

        # The Tag of the IBM Qiskit's Memory Hardware Type of the IBM Qiskit's Memory Hardware Module
        self.memory_module_type_tag = memory_module_type_tag

        # Initialise the IBM Qiskit's Hybrid Memories' Hardware of the IBM Qiskit's Memory Hardware Module
        self.qiskit_hybrid_memories = []

        # Initialise the IBM Qiskit's Semi-Quantum Memories' Hardware of the IBM Qiskit's Memory Hardware Module
        self.qiskit_semi_quantum_memories = []

        # Initialise the IBM Qiskit's Quantum Memories' Hardware of the IBM Qiskit's Memory Hardware Module
        self.qiskit_quantum_memories = []

        # Initialise the IBM Qiskit's Classical Memories' Hardware of the IBM Qiskit's Memory Hardware Module
        self.qiskit_classical_memories = []

    # Return the Tag of the IBM Qiskit's Memory Hardware Type of the IBM Qiskit's Memory Hardware Module
    def get_memory_module_type_tag(self):
        return self.memory_module_type_tag

    # Add an abstract IBM Qiskit's Memory Hardware to the IBM Qiskit's Memory Hardware Module
    def add_memory(self, qiskit_memory_to_add):

        # If the IBM Qiskit's Memory Hardware Module is Hybrid,
        # all the type of Memory Hardware (Hybrid, Quantum and Classical) can be added
        if self.memory_module_type_tag == MemoryModuleTypes.HYBRID_MEMORY_ENUM:

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory Hardware being given
            if isinstance(qiskit_memory_to_add, QiskitHybridMemory.QiskitHybridMemory):

                # Add the given abstract IBM Qiskit's Memory Hardware to the IBM Qiskit's Memory Hardware Module
                self.qiskit_hybrid_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Semi-Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitSemiQuantumMemory.QiskitSemiQuantumMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory Hardware
                raise ValueError("It is not possible to add a Semi-Quantum Memory to "
                                 "a Hybrid Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitQuantumMemory.QiskitQuantumMemory):

                # Add the given abstract IBM Qiskit's Memory Hardware to the IBM Qiskit's Memory Hardware Module
                self.qiskit_quantum_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitClassicalMemory.QiskitClassicalMemory):

                # Add the given abstract IBM Qiskit's Memory Hardware to the IBM Qiskit's Memory Hardware Module
                self.qiskit_classical_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware Memory!!!")

        # If the IBM Qiskit's Memory Hardware Module is Semi-Quantum,
        # only Semi-Quantum Memory Hardware can be added
        elif self.memory_module_type_tag == MemoryModuleTypes.SEMI_QUANTUM_MEMORY_ENUM:

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory Hardware being given
            if isinstance(qiskit_memory_to_add, QiskitHybridMemory.QiskitHybridMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory Hardware
                raise ValueError("It is not possible to add a Hybrid Memory to "
                                 "a Semi-Quantum Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Semi-Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitSemiQuantumMemory.QiskitSemiQuantumMemory):

                # Add the given abstract IBM Qiskit's Memory Hardware to the IBM Qiskit's Memory Hardware Module
                self.qiskit_semi_quantum_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitQuantumMemory.QiskitQuantumMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory Hardware
                raise ValueError("It is not possible to add a Quantum Memory to "
                                 "a Semi-Quantum Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitClassicalMemory.QiskitClassicalMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory Hardware
                raise ValueError("It is not possible to add a Classical Memory to "
                                 "a Semi-Quantum Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Hardware Memory!!!")

        # If the IBM Qiskit's Memory Hardware Module is Quantum,
        # only Quantum Memory Hardware can be added
        elif self.memory_module_type_tag == MemoryModuleTypes.QUANTUM_MEMORY_ENUM:

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory Hardware being given
            if isinstance(qiskit_memory_to_add, QiskitHybridMemory.QiskitHybridMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory Hardware
                raise ValueError("It is not possible to add a Hybrid Memory to "
                                 "a Quantum Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Semi-Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitSemiQuantumMemory.QiskitSemiQuantumMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory Hardware
                raise ValueError("It is not possible to add a Semi-Quantum Memory to "
                                 "a Quantum Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitQuantumMemory.QiskitQuantumMemory):

                # Add the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Hardware Module
                self.qiskit_quantum_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitClassicalMemory.QiskitClassicalMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory Hardware
                raise ValueError("It is not possible to add a Classical Memory to "
                                 "a Quantum Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Memory Hardware!!!")

        # If the IBM Qiskit's Memory Hardware Module is Classical,
        # only Classical Memory Hardware can be added
        elif self.memory_module_type_tag == MemoryModuleTypes.CLASSICAL_MEMORY_ENUM:

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory Hardware being given
            if isinstance(qiskit_memory_to_add, QiskitHybridMemory.QiskitHybridMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory Hardware
                raise ValueError("It is not possible to add a Hybrid Memory to "
                                 "a Classical Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Semi-Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitSemiQuantumMemory.QiskitSemiQuantumMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to add a Semi-Quantum Memory to "
                                 "a Classical Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitQuantumMemory.QiskitQuantumMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to add a Quantum Memory to "
                                 "a Classical Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory Hardware being given
            elif isinstance(qiskit_memory_to_add, QiskitClassicalMemory.QiskitClassicalMemory):

                # Add the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Hardware Module
                self.qiskit_classical_memories.append(qiskit_memory_to_add)

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to add an Unknown Memory Hardware!!!")

        # If the IBM Qiskit's Memory Hardware Module is Unknown,
        # no Memory Hardware can be added and it will be raised a Value Error
        else:

            # Raise a Value Error
            raise ValueError("It is impossible to add any type of Memory Hardware to this Memory Hardware Module, "
                             "due to an Unknown Hardware type of Memory Hardware Module!!!")

    # Remove an abstract IBM Qiskit's Memory Hardware to the IBM Qiskit's Memory Hardware Module
    def remove_memory(self, qiskit_memory_to_remove):

        # If the IBM Qiskit's Memory Hardware Module is Hybrid,
        # all the type of Memory Hardware (Hybrid, Quantum and Classical) can be removed
        if self.memory_module_type_tag == MemoryModuleTypes.HYBRID_MEMORY_ENUM:

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory Hardware being given
            if isinstance(qiskit_memory_to_remove, QiskitHybridMemory.QiskitHybridMemory):

                # Remove the given abstract IBM Qiskit's Memory Hardware to the IBM Qiskit's Memory Hardware Module
                self.qiskit_hybrid_memories.remove(qiskit_memory_to_remove)

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_remove, QiskitQuantumMemory.QiskitQuantumMemory):

                # Remove the given abstract IBM Qiskit's Memory Hardware to the IBM Qiskit's Memory Hardware Module
                self.qiskit_quantum_memories.remove(qiskit_memory_to_remove)

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory Hardware being given
            elif isinstance(qiskit_memory_to_remove, QiskitClassicalMemory.QiskitClassicalMemory):

                # Remove the given abstract IBM Qiskit's Memory Hardware to the IBM Qiskit's Memory Hardware Module
                self.qiskit_classical_memories.remove(qiskit_memory_to_remove)

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Memory Hardware!!!")

        # If the IBM Qiskit's Memory Hardware Module is Quantum,
        # only Quantum Memory Hardware can be removed
        elif self.memory_module_type_tag == MemoryModuleTypes.QUANTUM_MEMORY_ENUM:

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory Hardware being given
            if isinstance(qiskit_memory_to_remove, QiskitHybridMemory.QiskitHybridMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory Hardware
                raise ValueError("It is not possible to remove a Hybrid Memory to a Quantum Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_remove, QiskitQuantumMemory.QiskitQuantumMemory):

                # Add the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Hardware Module
                self.qiskit_quantum_memories.remove(qiskit_memory_to_remove)

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory Hardware being given
            elif isinstance(qiskit_memory_to_remove, QiskitClassicalMemory.QiskitClassicalMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to remove a Classical Memory to "
                                 "a Quantum Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Memory Hardware!!!")

        # If the IBM Qiskit's Memory Module Hardware is Classical,
        # only Classical Memory Hardware can be added
        elif self.memory_module_type_tag == MemoryModuleTypes.CLASSICAL_MEMORY_ENUM:

            # Check if the abstract IBM Qiskit's Memory is compatible with the type of Memory Hardware,
            # for the case of a Hybrid Memory Hardware being given
            if isinstance(qiskit_memory_to_remove, QiskitHybridMemory.QiskitHybridMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory Hardware
                raise ValueError("It is not possible to add a Hybrid Memory to a Quantum Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Quantum Memory Hardware being given
            elif isinstance(qiskit_memory_to_remove, QiskitQuantumMemory.QiskitQuantumMemory):

                # Raise a Value Error, according to the given abstract IBM Qiskit's Memory
                raise ValueError("It is not possible to remove a Classical Memory to "
                                 "a Quantum Memory Hardware Module!!!")

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Classical Memory Hardware being given
            elif isinstance(qiskit_memory_to_remove, QiskitClassicalMemory.QiskitClassicalMemory):

                # Remove the given abstract IBM Qiskit's Memory to the IBM Qiskit's Memory Module
                self.qiskit_classical_memories.remove(qiskit_memory_to_remove)

            # Check if the abstract IBM Qiskit's Memory Hardware is compatible with the type of Memory Hardware,
            # for the case of a Unknown Memory Hardware being given
            else:

                # Raise a Value Error
                raise ValueError("It is not possible to remove an Unknown Memory Hardware!!!")

        # If the IBM Qiskit's Memory Module is Unknown,
        # no Memory Hardware can be added and it will be raised a Value Error
        else:

            # Raise a Value Error
            raise ValueError("It is impossible to remove any type of Memory to this Memory Hardware Module, "
                             "due to an Unknown Hardware type of Memory Hardware Module!!!")

    # Return the IBM Qiskit's Hybrid Memories' Hardware of the IBM Qiskit's Memory Hardware Module
    def get_qiskit_hybrid_memories(self):

        # If the IBM Qiskit's Memory Module Hardware is Hybrid,
        # then it can have IBM Qiskit's Hybrid Memories' Hardware
        if self.memory_module_type_tag == MemoryModuleTypes.HYBRID_MEMORY_ENUM:

            # Return the IBM Qiskit's Hybrid Memories' Hardware
            return self.qiskit_hybrid_memories

        # If the IBM Qiskit's Memory Module Hardware is not Hybrid,
        # then it cannot have IBM Qiskit's Hybrid Memories' Hardware
        else:

            # Raise a Value Error
            raise ValueError("Only Hybrid Memory Modules' Hardware can have Hybrid Memory Hardware!!!")

    # Return the IBM Qiskit's Quantum Memories' Hardware of the IBM Qiskit's Memory Hardware Module
    def get_qiskit_quantum_memories(self):

        # If the IBM Qiskit's Memory Module Hardware is Hybrid,
        # then it can have IBM Qiskit's Quantum Memories' Hardware
        if self.memory_module_type_tag == MemoryModuleTypes.HYBRID_MEMORY_ENUM:

            # Return the IBM Qiskit's Quantum Memories' Hardware
            return self.qiskit_quantum_memories

        # If the IBM Qiskit's Memory Module Hardware is Quantum,
        # then it can have IBM Qiskit's Quantum Memories' Hardware
        elif self.memory_module_type_tag == MemoryModuleTypes.QUANTUM_MEMORY_ENUM:

            # Return the IBM Qiskit's Quantum Memories' Hardware
            return self.qiskit_quantum_memories

        # If the IBM Qiskit's Memory Module Hardware is not Hybrid neither Quantum,
        # then it cannot have IBM Qiskit's Quantum Memories' Hardware
        else:

            # Raise a Value Error
            raise ValueError("Only Hybrid and Quantum Memory Modules' Hardware can have Quantum Memory Hardware!!!")

    # Return the IBM Qiskit's Classical Memories' Hardware of the IBM Qiskit's Memory Hardware Module
    def get_qiskit_classical_memories(self):

        # If the IBM Qiskit's Memory Module Hardware is Hybrid,
        # then it can have IBM Qiskit's Classical Memories' Hardware
        if self.memory_module_type_tag == MemoryModuleTypes.HYBRID_MEMORY_ENUM:

            # Return the IBM Qiskit's Classical Memories' Hardware
            return self.qiskit_classical_memories

        # If the IBM Qiskit's Memory Module Hardware is Classical,
        # then it can have IBM Qiskit's Classical Memories' Hardware
        elif self.memory_module_type_tag == MemoryModuleTypes.QUANTUM_MEMORY_ENUM:

            # Return the IBM Qiskit's Classical Memories' Hardware
            return self.qiskit_classical_memories

        # If the IBM Qiskit's Memory Module Hardware is not Hybrid neither Classical,
        # then it cannot have IBM Qiskit's Classical Memories' Hardware
        else:

            # Raise a Value Error
            raise ValueError("Only Hybrid and Classical Memory Modules' Hardware can have Quantum Memory Hardware!!!")
