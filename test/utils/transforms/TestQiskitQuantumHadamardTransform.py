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

# Import Unittest for Python's Unitary Tests
import unittest

# Import N-Dimensional Arrays and Squared Roots from NumPy
from numpy import full, sqrt

# Import Assert_All_Close from NumPy.Testing
from numpy.testing import assert_allclose

# Import Aer and execute from Qiskit
from qiskit import Aer, execute

# Import QiskitQuantumCircuit from IBM_Qiskit.Circuit
from ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister

# Import QiskitQuantumHadamardTransform from IBM_Qiskit.Utils.Transforms
from ibm_qiskit.utils.transforms import QiskitQuantumHadamardTransform


# Test Cases for the Quantum Hadamard Transform
class QuantumHadamardTransformTests(unittest.TestCase):

    # Test #1 for the Quantum Hadamard Transform
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 1 Qubit initialized in the state |0⟩;
    # 2) It is applied the Hadamard Gate to all the Qubits, then, for each Qubit, |0⟩ ↦ |+⟩;
    def test_quantum_hadamard_transform_1_qubit(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 1

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_hadamard_1_qubit = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrhadamard1qubit", num_qubits)
        qiskit_classical_register_hadamard_1_qubit = \
            QiskitClassicalRegister.QiskitClassicalRegister("crhadamard1qubit", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_1_qubit = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qchadamard1qubit",
                                                      qiskit_quantum_register_hadamard_1_qubit,
                                                      qiskit_classical_register_hadamard_1_qubit,
                                                      global_phase=0)

        # Setup of the range of Qubits' indexes
        qubit_indexes = range(0, num_qubits)

        # Apply the Quantum Hadamard Transform for 1 Qubit
        qiskit_quantum_hadamard_transform_1_qubit_circuit = QiskitQuantumHadamardTransform\
            .QiskitQuantumHadamardTransform("quantum_hadamard_transform_1_qubit",
                                            qiskit_quantum_circuit_1_qubit,
                                            qubit_indexes).apply_transform()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_hadamard_transform_1_qubit_circuit.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the Quantum Hadamard Transform values
        qiskit_quantum_hadamard_1_qubit_array = full((num_possible_outcomes,),
                                                     (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubit,
        # after the Hadamard Gates be applied
        assert_allclose(final_state_vector, qiskit_quantum_hadamard_1_qubit_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for the Quantum Hadamard Transform
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |0⟩;
    # 2) It is applied the Hadamard Gate to all the Qubits, then, for each Qubit, |0⟩ ↦ |+⟩;
    def test_quantum_hadamard_transform_2_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_hadamard_2_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrhadamard2qubits", num_qubits)
        qiskit_classical_register_hadamard_2_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crhadamard2qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qchadamard2qubits",
                                                      qiskit_quantum_register_hadamard_2_qubits,
                                                      qiskit_classical_register_hadamard_2_qubits,
                                                      global_phase=0)

        # Setup of the range of Qubits' indexes
        qubit_indexes = range(0, num_qubits)

        # Apply the Quantum Hadamard Transform for 2 Qubits
        qiskit_quantum_hadamard_transform_2_qubits_circuit = QiskitQuantumHadamardTransform\
            .QiskitQuantumHadamardTransform("quantum_hadamard_transform_2_qubits",
                                            qiskit_quantum_circuit_2_qubits,
                                            qubit_indexes).apply_transform()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_hadamard_transform_2_qubits_circuit.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the Quantum Hadamard Transform values
        qiskit_quantum_hadamard_2_qubits_array = full((num_possible_outcomes,),
                                                      (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Hadamard Gates be applied
        assert_allclose(final_state_vector, qiskit_quantum_hadamard_2_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for the Quantum Hadamard Transform
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 3 Qubits initialized in the state |0⟩;
    # 2) It is applied the Hadamard Gate to all the Qubits, then, for each Qubit, |0⟩ ↦ |+⟩;
    def test_quantum_hadamard_transform_3_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 3

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_hadamard_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrhadamard3qubits", num_qubits)
        qiskit_classical_register_hadamard_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crhadamard3qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qchadamard3qubits",
                                                      qiskit_quantum_register_hadamard_3_qubits,
                                                      qiskit_classical_register_hadamard_3_qubits,
                                                      global_phase=0)

        # Setup of the range of Qubits' indexes
        qubit_indexes = range(0, num_qubits)

        # Apply the Quantum Hadamard Transform for 3 Qubits
        qiskit_quantum_hadamard_transform_3_qubits_circuit = QiskitQuantumHadamardTransform\
            .QiskitQuantumHadamardTransform("quantum_hadamard_transform_3_qubits",
                                            qiskit_quantum_circuit_3_qubits,
                                            qubit_indexes).apply_transform()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_hadamard_transform_3_qubits_circuit.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the Quantum Hadamard Transform values
        qiskit_quantum_hadamard_3_qubits_array = full((num_possible_outcomes,),
                                                      (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Hadamard Gates be applied
        assert_allclose(final_state_vector, qiskit_quantum_hadamard_3_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for the Quantum Hadamard Transform
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 4 Qubits initialized in the state |0⟩;
    # 2) It is applied the Hadamard Gate to all the Qubits, then, for each Qubit, |0⟩ ↦ |+⟩;
    def test_quantum_hadamard_transform_4_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 4

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_hadamard_4_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrhadamard4qubits", num_qubits)
        qiskit_classical_register_hadamard_4_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crhadamard4qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_4_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qchadamard4qubits",
                                                      qiskit_quantum_register_hadamard_4_qubits,
                                                      qiskit_classical_register_hadamard_4_qubits,
                                                      global_phase=0)

        # Setup of the range of Qubits' indexes
        qubit_indexes = range(0, num_qubits)

        # Apply the Quantum Hadamard Transform for 4 Qubits
        qiskit_quantum_hadamard_transform_4_qubits_circuit = QiskitQuantumHadamardTransform\
            .QiskitQuantumHadamardTransform("quantum_hadamard_transform_4_qubits",
                                            qiskit_quantum_circuit_4_qubits,
                                            qubit_indexes).apply_transform()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_hadamard_transform_4_qubits_circuit.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the Quantum Hadamard Transform values
        qiskit_quantum_hadamard_4_qubits_array = full((num_possible_outcomes,),
                                                      (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Hadamard Gates be applied
        assert_allclose(final_state_vector, qiskit_quantum_hadamard_4_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #5 for the Quantum Hadamard Transform
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 5 Qubits initialized in the state |0⟩;
    # 2) It is applied the Hadamard Gate to all the Qubits, then, for each Qubit, |0⟩ ↦ |+⟩;
    def test_quantum_hadamard_transform_5_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 5

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_hadamard_5_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrhadamard5qubits", num_qubits)
        qiskit_classical_register_hadamard_5_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crhadamard5qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_5_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qchadamard5qubits",
                                                      qiskit_quantum_register_hadamard_5_qubits,
                                                      qiskit_classical_register_hadamard_5_qubits,
                                                      global_phase=0)

        # Setup of the range of Qubits' indexes
        qubit_indexes = range(0, num_qubits)

        # Apply the Quantum Hadamard Transform for 5 Qubits
        qiskit_quantum_hadamard_transform_5_qubits_circuit = QiskitQuantumHadamardTransform\
            .QiskitQuantumHadamardTransform("quantum_hadamard_transform_5_qubits",
                                            qiskit_quantum_circuit_5_qubits,
                                            qubit_indexes).apply_transform()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_hadamard_transform_5_qubits_circuit.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the Quantum Hadamard Transform values
        qiskit_quantum_hadamard_5_qubits_array = full((num_possible_outcomes,),
                                                      (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Hadamard Gates be applied
        assert_allclose(final_state_vector, qiskit_quantum_hadamard_5_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #6 for the Quantum Hadamard Transform
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 6 Qubits initialized in the state |0⟩;
    # 2) It is applied the Hadamard Gate to all the Qubits, then, for each Qubit, |0⟩ ↦ |+⟩;
    def test_quantum_hadamard_transform_6_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 6

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_hadamard_6_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrhadamard6qubits", num_qubits)
        qiskit_classical_register_hadamard_6_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crhadamard6qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_6_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qchadamard6qubits",
                                                      qiskit_quantum_register_hadamard_6_qubits,
                                                      qiskit_classical_register_hadamard_6_qubits,
                                                      global_phase=0)

        # Setup of the range of Qubits' indexes
        qubit_indexes = range(0, num_qubits)

        # Apply the Quantum Hadamard Transform for 6 Qubits
        qiskit_quantum_hadamard_transform_6_qubits_circuit = QiskitQuantumHadamardTransform\
            .QiskitQuantumHadamardTransform("quantum_hadamard_transform_6_qubits",
                                            qiskit_quantum_circuit_6_qubits,
                                            qubit_indexes).apply_transform()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_hadamard_transform_6_qubits_circuit.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the Quantum Hadamard Transform values
        qiskit_quantum_hadamard_6_qubits_array = full((num_possible_outcomes,),
                                                      (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Hadamard Gates be applied
        assert_allclose(final_state_vector, qiskit_quantum_hadamard_6_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #7 for the Quantum Hadamard Transform
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 16 Qubits initialized in the state |0⟩;
    # 2) It is applied the Hadamard Gate to all the Qubits, then, for each Qubit, |0⟩ ↦ |+⟩;
    def test_quantum_hadamard_transform_16_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 16

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_hadamard_16_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrhadamard16qubits", num_qubits)
        qiskit_classical_register_hadamard_16_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crhadamard16qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_16_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qchadamard16qubits",
                                                      qiskit_quantum_register_hadamard_16_qubits,
                                                      qiskit_classical_register_hadamard_16_qubits,
                                                      global_phase=0)

        # Setup of the range of Qubits' indexes
        qubit_indexes = range(0, num_qubits)

        # Apply the Quantum Hadamard Transform for 16 Qubits
        qiskit_quantum_hadamard_transform_16_qubits_circuit = QiskitQuantumHadamardTransform\
            .QiskitQuantumHadamardTransform("quantum_hadamard_transform_16_qubits",
                                            qiskit_quantum_circuit_16_qubits,
                                            qubit_indexes).apply_transform()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_hadamard_transform_16_qubits_circuit.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the Quantum Hadamard Transform values
        qiskit_quantum_hadamard_16_qubits_array = full((num_possible_outcomes,),
                                                       (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Hadamard Gates be applied
        assert_allclose(final_state_vector, qiskit_quantum_hadamard_16_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #8 for the Quantum Hadamard Transform
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 25 Qubits initialized in the state |0⟩;
    # 2) It is applied the Hadamard Gate to all the Qubits, then, for each Qubit, |0⟩ ↦ |+⟩;
    def test_quantum_hadamard_transform_25_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 25

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_hadamard_25_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrhadamard25qubits", num_qubits)
        qiskit_classical_register_hadamard_25_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crhadamard25qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_25_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qchadamard25qubits",
                                                      qiskit_quantum_register_hadamard_25_qubits,
                                                      qiskit_classical_register_hadamard_25_qubits,
                                                      global_phase=0)

        # Setup of the range of Qubits' indexes
        qubit_indexes = range(0, num_qubits)

        # Apply the Quantum Hadamard Transform for 25 Qubits
        qiskit_quantum_hadamard_transform_25_qubits_circuit = QiskitQuantumHadamardTransform\
            .QiskitQuantumHadamardTransform("quantum_hadamard_transform_25_qubits",
                                            qiskit_quantum_circuit_25_qubits,
                                            qubit_indexes).apply_transform()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_hadamard_transform_25_qubits_circuit.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the Quantum Hadamard Transform values
        qiskit_quantum_hadamard_25_qubits_array = full((num_possible_outcomes,),
                                                       (1 / sqrt(num_possible_outcomes)) * (1. + 0.j))

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Hadamard Gates be applied
        assert_allclose(final_state_vector, qiskit_quantum_hadamard_25_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':

    # Test Cases for the Quantum Hadamard Transforms
    quantum_hadamard_transform_tests_suite = unittest.TestLoader().loadTestsFromTestCase(QuantumHadamardTransformTests)

    # Create a Global for all the Test Cases established
    all_test_cases = unittest.TestSuite([quantum_hadamard_transform_tests_suite])
