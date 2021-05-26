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

# Import shuffle from Random Library
from random import shuffle

# Import Aer and execute from Qiskit
from qiskit import Aer, execute, QiskitError

# Import QiskitQuantumCircuit from IBM_Qiskit.Circuit
from src.ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister

# Import QiskitQuantumHadamardTransform from IBM_Qiskit.Utils.Transforms
from src.ibm_qiskit.utils.transforms import QiskitQuantumHadamardTransform

# Import some important constant values, regarding some parameters of the IBM's Qiskit

# Import the maximum number of Qubits and the default number of Counts for
# the executions or simulations of Quantum Circuits on the IBM's Qiskit QASM Simulator
from src.ibm_qiskit.common.QiskitLibraryParameters import \
    QISKIT_LIBRARY_QASM_SIMULATOR_MAX_NUM_QUBITS, QISKIT_DEFAULT_NUM_COUNTS


# Class for IBM Qiskit's Quantum True Random Binary String Generator (QTRBSG)
class QiskitQuantumTrueRandomBinaryStringGenerator:

    # Constructor for IBM Qiskit's Quantum True Random Binary String Generator (QTRBSG)
    def __init__(self, name, binary_string_length=QISKIT_LIBRARY_QASM_SIMULATOR_MAX_NUM_QUBITS,
                 num_counts=QISKIT_DEFAULT_NUM_COUNTS):
        self.name = name
        self.binary_string_length = binary_string_length
        self.num_counts = num_counts

    # Generate a True Random Binary String
    def generate_true_random_binary_string(self, quantum_register_index, classical_register_index):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = self.binary_string_length

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_true_random_binary_string = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrtrbsg{}qubit(s)".format(num_qubits), num_qubits)
        qiskit_classical_register_true_random_binary_string = \
            QiskitClassicalRegister.QiskitClassicalRegister("crtrbsg{}qubit(s)".format(num_bits), num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_true_random_binary_string_generator = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qctrbsg{}qubit(s)".format(num_qubits),
                                                      qiskit_quantum_register_true_random_binary_string,
                                                      qiskit_classical_register_true_random_binary_string,
                                                      global_phase=0)

        # Setup of the range of Qubits' indexes
        qubit_indexes = range(0, num_qubits)

        # Apply the Quantum Hadamard Transform for n Qubit(s) for Quantum True Random Binary String Generator (QTRBSG)
        qiskit_quantum_hadamard_transform_circuit_true_random_binary_string = QiskitQuantumHadamardTransform \
            .QiskitQuantumHadamardTransform("quantum_hadamard_transform_{}_qubits".format(num_qubits),
                                            qiskit_quantum_circuit_true_random_binary_string_generator,
                                            qubit_indexes).apply_transform()

        # Measure all the Qubits of the Quantum Circuit
        qiskit_quantum_hadamard_transform_circuit_true_random_binary_string\
            .measure_all_qubits(quantum_register_index, classical_register_index)

        # Getting the Backend for the QASM (Quantum ASseMbly) for the simulation of the Quantum Circuit
        # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
        qasm_backend = Aer.get_backend("qasm_simulator")

        # Execute the Quantum Circuit and store the Measurement results in a Dictionary Object,
        # for a frequency counting
        final_results_frequency_counting = \
            execute(qiskit_quantum_hadamard_transform_circuit_true_random_binary_string.quantum_circuit,
                    qasm_backend, shots=self.num_counts).result().get_counts()

        # Try to retrieve one unique Quantum True Random Binary String (QTRBS) from
        # the most frequent (maximum) value of all the keys of the Dictionary for the frequency counting
        try:
            # If the most frequent (maximum) representation value of all the keys of the Dictionary for
            # the frequency counting is unique, retrieves that key value
            final_quantum_true_random_binary_string = final_results_frequency_counting.most_frequent()

        # It is not possible to retrieve one unique Quantum True Random Binary String (QTRBS) from
        # the most frequent (maximum) value of all the keys of the Dictionary for the frequency counting
        except QiskitError:

            # Convert the list of the several most frequent (maximum) values of all the keys of
            # the Dictionary for the frequency counting
            final_quantum_true_random_binary_string_list = list(final_results_frequency_counting.keys())

            # Duplicate the list of the several most frequent (maximum) values of all the keys of
            # the Dictionary for the frequency counting
            final_quantum_true_random_binary_string_list_shuffled = final_quantum_true_random_binary_string_list.copy()

            # Shuffle the list of the several most frequent (maximum) values of all the keys of
            # the Dictionary for the frequency counting
            shuffle(final_quantum_true_random_binary_string_list_shuffled)

            # Pop the first element of shuffled list of the several most frequent (maximum) values of all the keys of
            # the Dictionary for the frequency counting
            final_quantum_true_random_binary_string = final_quantum_true_random_binary_string_list_shuffled[0]

        # Return the final Quantum True Random Binary String (QTRBS)
        return final_quantum_true_random_binary_string
