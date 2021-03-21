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

# Import Libraries and Packages

# Import Unittest for Python's Unitary Tests
import unittest

# Import the Fulfillment Array function and Squared Roots from NumPy
from numpy import full, sqrt

# Import Assert_All_Close from NumPy.Testing
from numpy.testing import assert_allclose

# Import Aer and execute from Qiskit
from qiskit import Aer, execute

# Import QiskitQuantumCircuit from IBM_Qiskit.Circuit
from src.ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister

# Import QiskitWState from IBM_Qiskit.Entanglements.Multipartite
from src.ibm_qiskit.entanglements.multipartite import QiskitWState


# Test Cases for prepare the W States
class PrepareWStateTests(unittest.TestCase):

    # Test #1 for prepare the W States, for 3 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 3 Qubits initialized in the state |000⟩;
    # 2) Prepare of the W State, for 3 Qubits: |W_3⟩ = 1/sqrt(3) x (|001⟩ + |010⟩ + |100⟩);
    def test_prepare_w_state_3_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 3

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_w_state_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrwstate3", num_qubits)
        qiskit_classical_register_w_state_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crwstate3", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcwstate3",
                                                      qiskit_quantum_register_w_state_3_qubits,
                                                      qiskit_classical_register_w_state_3_qubits,
                                                      global_phase=0)

        # Prepare the W State, for 3 Qubits
        qiskit_quantum_circuit_w_state_3_qubits = QiskitWState \
            .QiskitWState("w_state_3_qubits",
                          qiskit_quantum_circuit_3_qubits,
                          [0, 1, 2]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_w_state_3_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of W State, for 3 Qubits
        qiskit_w_state_3_qubits_array = full((num_possible_outcomes,),
                                             (0. + 0.j))

        # Set the indexes of the State Vector of the Qubits (i.e., |001⟩, |010⟩ and |100⟩),
        # of the W State, for 3 Qubits, with the Complex Number value, 1/sqrt(3) x (1 + 0j)
        for current_qubit in range(num_qubits):

            # Compute the current index of the state vector, as a power of 2
            current_state_vector_index = (2 ** current_qubit)

            # Set the current index of the state vector to be |1⟩
            qiskit_w_state_3_qubits_array[current_state_vector_index] = ((1. / sqrt(num_qubits)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the W State, for 3 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_w_state_3_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare the W States, for 4 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 4 Qubits initialized in the state |0000⟩;
    # 2) Prepare of the W State, for 4 Qubits: |W_4⟩ = 1/sqrt(4) x (|0001⟩ + |0010⟩ + |0100⟩ + |1000⟩);
    def test_prepare_w_state_4_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 4

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_w_state_4_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrwstate4", num_qubits)
        qiskit_classical_register_w_state_4_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crwstate4", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_4_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcwstate4",
                                                      qiskit_quantum_register_w_state_4_qubits,
                                                      qiskit_classical_register_w_state_4_qubits,
                                                      global_phase=0)

        # Prepare the W State, for 4 Qubits
        qiskit_quantum_circuit_w_state_4_qubits = QiskitWState \
            .QiskitWState("w_state_4_qubits",
                          qiskit_quantum_circuit_4_qubits,
                          [0, 1, 2, 3]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_w_state_4_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of W State, for 4 Qubits
        qiskit_w_state_4_qubits_array = full((num_possible_outcomes,),
                                             (0. + 0.j))

        # Set the indexes of the State Vector of the Qubits (i.e., |0001⟩, |0010⟩, |0100⟩ and |1000⟩),
        # of the W State, for 4 Qubits, with the Complex Number value, 1/sqrt(4) x (1 + 0j)
        for current_qubit in range(num_qubits):

            # Compute the current index of the state vector, as a power of 2
            current_state_vector_index = (2 ** current_qubit)

            # Set the current index of the state vector to be |1⟩
            qiskit_w_state_4_qubits_array[current_state_vector_index] = ((1. / sqrt(num_qubits)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the W State, for 4 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_w_state_4_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare the W States, for 5 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 5 Qubits initialized in the state |00000⟩;
    # 2) Prepare of the W State, for 5 Qubits: |W_5⟩ = 1/sqrt(5) x (|00001⟩ + |00010⟩ + |00100⟩ + |01000⟩ + |10000⟩);
    def test_prepare_w_state_5_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 5

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_w_state_5_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrwstate5", num_qubits)
        qiskit_classical_register_w_state_5_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crwstate5", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_5_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcwstate5",
                                                      qiskit_quantum_register_w_state_5_qubits,
                                                      qiskit_classical_register_w_state_5_qubits,
                                                      global_phase=0)

        # Prepare the W State, for 5 Qubits
        qiskit_quantum_circuit_w_state_5_qubits = QiskitWState \
            .QiskitWState("w_state_5_qubits",
                          qiskit_quantum_circuit_5_qubits,
                          [0, 1, 2, 3, 4]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_w_state_5_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of W State, for 5 Qubits
        qiskit_w_state_5_qubits_array = full((num_possible_outcomes,),
                                             (0. + 0.j))

        # Set the indexes of the State Vector of the Qubits (i.e., |00001⟩, |00010⟩, |00100⟩, |01000⟩ and |10000⟩),
        # of the W State, for 5 Qubits, with the Complex Number value, 1/sqrt(5) x (1 + 0j)
        for current_qubit in range(num_qubits):

            # Compute the current index of the state vector, as a power of 2
            current_state_vector_index = (2 ** current_qubit)

            # Set the current index of the state vector to be |1⟩
            qiskit_w_state_5_qubits_array[current_state_vector_index] = ((1. / sqrt(num_qubits)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the W State, for 5 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_w_state_5_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare the W States, for 6 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 6 Qubits initialized in the state |00000⟩;
    # 2) Prepare of the W State, for 6 Qubits: |W_6⟩ = 1/sqrt(5) x (|00001⟩ + |00010⟩ + |00100⟩ + |01000⟩ + |10000⟩);
    def test_prepare_w_state_6_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 6

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_w_state_6_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrwstate6", num_qubits)
        qiskit_classical_register_w_state_6_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crwstate6", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_6_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcwstate6",
                                                      qiskit_quantum_register_w_state_6_qubits,
                                                      qiskit_classical_register_w_state_6_qubits,
                                                      global_phase=0)

        # Prepare the W State, for 6 Qubits
        qiskit_quantum_circuit_w_state_6_qubits = QiskitWState \
            .QiskitWState("w_state_6_qubits",
                          qiskit_quantum_circuit_6_qubits,
                          [0, 1, 2, 3, 4, 5]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_w_state_6_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of W State, for 6 Qubits
        qiskit_w_state_6_qubits_array = full((num_possible_outcomes,),
                                             (0. + 0.j))

        # Set the indexes of the State Vector of the Qubits (i.e., |000001⟩, |000010⟩, |000100⟩,
        # |001000⟩, |010000⟩ and |100000⟩), of the W State, for 6 Qubits,
        # with the Complex Number value, 1/sqrt(6) x (1 + 0j)
        for current_qubit in range(num_qubits):

            # Compute the current index of the state vector, as a power of 2
            current_state_vector_index = (2 ** current_qubit)

            # Set the current index of the state vector to be |1⟩
            qiskit_w_state_6_qubits_array[current_state_vector_index] = ((1. / sqrt(num_qubits)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the W State, for 6 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_w_state_6_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':

    # Test Cases for prepare the W States
    w_states_prepare_tests_suite = unittest.TestLoader().loadTestsFromTestCase(PrepareWStateTests)

    # Create a Global for all the Test Cases established
    all_test_cases = unittest.TestSuite([w_states_prepare_tests_suite])
