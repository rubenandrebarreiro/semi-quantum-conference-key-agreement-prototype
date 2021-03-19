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

# Import N-Dimensional Arrays, the Fulfillment Array function and Squared Roots from NumPy
from numpy import array, full, sqrt

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

# Import QiskitBellState from IBM_Qiskit.Entanglements.Multipartite
from src.ibm_qiskit.entanglements.multipartite import QiskitGHZState


# Test Cases for prepare the GHZ States
class PrepareGHZStateTests(unittest.TestCase):

    # Test #1 for prepare the GHZ States, for 3 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 3 Qubits initialized in the state |000⟩;
    # 2) Prepare of the GHZ State, for 3 Qubits: |GHZ_3⟩ = 1/sqrt(2) x (|000⟩ + |111⟩);
    def test_prepare_ghz_state_3_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 3

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate3", num_qubits)
        qiskit_classical_register_ghz_state_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate3", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate3",
                                                      qiskit_quantum_register_ghz_state_3_qubits,
                                                      qiskit_classical_register_ghz_state_3_qubits,
                                                      global_phase=0)

        # Prepare the GHZ State, for 3 Qubits
        qiskit_quantum_circuit_ghz_state_3_qubits = QiskitGHZState \
            .QiskitGHZState("ghz_state_3_qubits",
                            qiskit_quantum_circuit_3_qubits,
                            0, [1, 2]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_3_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 3 Qubits
        qiskit_ghz_state_3_qubits_array = full((num_possible_outcomes,),
                                               (0. + 0.j))

        # Set the first and last Qubits (i.e., |00...0⟩ and |11...1⟩),
        # of the GHZ State, for 3 Qubits, with the Complex Number value, 1/sqrt(2) x (1 + 0j)
        qiskit_ghz_state_3_qubits_array[0] = ((1. / sqrt(2.)) + 0.j)
        qiskit_ghz_state_3_qubits_array[(num_possible_outcomes - 1)] = ((1. / sqrt(2.)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 3 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_3_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare the GHZ States, for 4 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 4 Qubits initialized in the state |0000⟩;
    # 2) Prepare of the GHZ State, for 4 Qubits: |GHZ_4⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩);
    def test_prepare_ghz_state_4_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 4

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_4_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate4", num_qubits)
        qiskit_classical_register_ghz_state_4_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate4", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_4_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate4",
                                                      qiskit_quantum_register_ghz_state_4_qubits,
                                                      qiskit_classical_register_ghz_state_4_qubits,
                                                      global_phase=0)

        # Prepare the GHZ State, for 4 Qubits
        qiskit_quantum_circuit_ghz_state_4_qubits = QiskitGHZState \
            .QiskitGHZState("ghz_state_4_qubits",
                            qiskit_quantum_circuit_4_qubits,
                            0, [1, 2, 3]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_4_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 4 Qubits
        qiskit_ghz_state_4_qubits_array = full((num_possible_outcomes,),
                                               (0. + 0.j))

        # Set the first and last Qubits (i.e., |00...0⟩ and |11...1⟩),
        # of the GHZ State, for 4 Qubits, with the Complex Number value, 1/sqrt(2) x (1 + 0j)
        qiskit_ghz_state_4_qubits_array[0] = ((1. / sqrt(2.)) + 0.j)
        qiskit_ghz_state_4_qubits_array[(num_possible_outcomes - 1)] = ((1. / sqrt(2.)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 4 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_4_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare the GHZ States, for 5 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 5 Qubits initialized in the state |00000⟩;
    # 2) Prepare of the GHZ State, for 5 Qubits: |GHZ_5⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩);
    def test_prepare_ghz_state_5_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 5

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_5_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate5", num_qubits)
        qiskit_classical_register_ghz_state_5_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate5", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_5_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate5",
                                                      qiskit_quantum_register_ghz_state_5_qubits,
                                                      qiskit_classical_register_ghz_state_5_qubits,
                                                      global_phase=0)

        # Prepare the GHZ State, for 5 Qubits
        qiskit_quantum_circuit_ghz_state_5_qubits = QiskitGHZState \
            .QiskitGHZState("ghz_state_5_qubits",
                            qiskit_quantum_circuit_5_qubits,
                            0, [1, 2, 3, 4]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_5_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 5 Qubits
        qiskit_ghz_state_5_qubits_array = full((num_possible_outcomes,),
                                               (0. + 0.j))

        # Set the first and last Qubits (i.e., |00...0⟩ and |11...1⟩),
        # of the GHZ State, for 5 Qubits, with the Complex Number value, 1/sqrt(2) x (1 + 0j)
        qiskit_ghz_state_5_qubits_array[0] = ((1. / sqrt(2.)) + 0.j)
        qiskit_ghz_state_5_qubits_array[(num_possible_outcomes - 1)] = ((1. / sqrt(2.)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 5 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_5_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare the GHZ States, for 6 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 6 Qubits initialized in the state |000000⟩;
    # 2) Prepare of the GHZ State, for 6 Qubits: |GHZ_6⟩ = 1/sqrt(2) x (|000000⟩ + |111111⟩);
    def test_prepare_ghz_state_6_qubits(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 6

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_6_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate6", num_qubits)
        qiskit_classical_register_ghz_state_6_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate6", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_6_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate6",
                                                      qiskit_quantum_register_ghz_state_6_qubits,
                                                      qiskit_classical_register_ghz_state_6_qubits,
                                                      global_phase=0)

        # Prepare the GHZ State, for 6 Qubits
        qiskit_quantum_circuit_ghz_state_6_qubits = QiskitGHZState \
            .QiskitGHZState("ghz_state_6_qubits",
                            qiskit_quantum_circuit_6_qubits,
                            0, [1, 2, 3, 4, 5]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_6_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 6 Qubits
        qiskit_ghz_state_6_qubits_array = full((num_possible_outcomes,),
                                               (0. + 0.j))

        # Set the first and last Qubits (i.e., |00...0⟩ and |11...1⟩),
        # of the GHZ State, for 6 Qubits, with the Complex Number value, 1/sqrt(2) x (1 + 0j)
        qiskit_ghz_state_6_qubits_array[0] = ((1. / sqrt(2.)) + 0.j)
        qiskit_ghz_state_6_qubits_array[(num_possible_outcomes - 1)] = ((1. / sqrt(2.)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 6 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_6_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':

    # Test Cases for prepare the GHZ States
    ghz_states_prepare_tests_suite = unittest.TestLoader().loadTestsFromTestCase(PrepareGHZStateTests)

    # Create a Global for all the Test Cases established
    all_test_cases = unittest.TestSuite([ghz_states_prepare_tests_suite])

