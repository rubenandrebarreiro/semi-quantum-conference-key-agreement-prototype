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

# Import QiskitGHZState from IBM_Qiskit.Entanglements.Multipartite
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

        # Set the first and last indexes of the State Vector of the Qubits (i.e., |00...0⟩ and |11...1⟩),
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

        # Set the first and last indexes of the State Vector of the Qubits (i.e., |00...0⟩ and |11...1⟩),
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

        # Set the first and last indexes of the State Vector of the Qubits (i.e., |00...0⟩ and |11...1⟩),
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

        # Set the first and last indexes of the State Vector of the Qubits (i.e., |00...0⟩ and |11...1⟩),
        # of the GHZ State, for 6 Qubits, with the Complex Number value, 1/sqrt(2) x (1 + 0j)
        qiskit_ghz_state_6_qubits_array[0] = ((1. / sqrt(2.)) + 0.j)
        qiskit_ghz_state_6_qubits_array[(num_possible_outcomes - 1)] = ((1. / sqrt(2.)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 6 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_6_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


# Test Cases for prepare and measure the GHZ States, for 3 Qubits, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩)
class PrepareAndMeasureGHZState3Qubits(unittest.TestCase):

    # Test #1 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 3 Qubits initialized in the state |000⟩;
    # 2) Prepare of the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩);
    # 3) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩);
    def test_prepare_and_measure_ghz_state_3_qubits_000(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 3

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate3qubits", num_qubits)
        qiskit_classical_register_ghz_state_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate3qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate3qubits",
                                                      qiskit_quantum_register_ghz_state_3_qubits,
                                                      qiskit_classical_register_ghz_state_3_qubits,
                                                      global_phase=0)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩), for 3 Qubits
        qiskit_quantum_circuit_ghz_state_3_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_3_qubits",
                            qiskit_quantum_circuit_3_qubits,
                            0, [1, 2]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩), for 3 Qubits
        qiskit_quantum_circuit_ghz_state_000_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_3_qubits_000",
                            qiskit_quantum_circuit_ghz_state_3_qubits_prepared,
                            0, [1, 2]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_000_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 3 Qubits
        qiskit_ghz_state_3_qubits_array_000 = full((num_possible_outcomes,),
                                                   (0. + 0.j))

        # Set the first index of the State Vector of the Qubits (i.e., |000⟩),
        # of the GHZ State, for 3 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_3_qubits_array_000[0] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 3 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_3_qubits_array_000, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 3 Qubits initialized in the state |000⟩;
    # 2) Prepare the Quantum State, |010⟩, by applying the Pauli-X Gate on the second Qubit;
    # 3) Prepare of the GHZ State, for 3 Qubits, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩);
    # 4) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩);
    def test_prepare_and_measure_ghz_state_3_qubits_010(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 3

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate3qubits", num_qubits)
        qiskit_classical_register_ghz_state_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate3qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate3qubits",
                                                      qiskit_quantum_register_ghz_state_3_qubits,
                                                      qiskit_classical_register_ghz_state_3_qubits,
                                                      global_phase=0)

        # Prepare the Quantum State, |010⟩, by applying the Pauli-X Gate, on the second Qubit
        qiskit_quantum_circuit_3_qubits.apply_pauli_x(1)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩), for 3 Qubits
        qiskit_quantum_circuit_ghz_state_3_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_3_qubits",
                            qiskit_quantum_circuit_3_qubits,
                            0, [1, 2]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩), for 3 Qubits
        qiskit_quantum_circuit_ghz_state_000_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_3_qubits_010",
                            qiskit_quantum_circuit_ghz_state_3_qubits_prepared,
                            0, [1, 2]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_000_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 3 Qubits
        qiskit_ghz_state_3_qubits_array_010 = full((num_possible_outcomes,),
                                                   (0. + 0.j))

        # Set the third index of the State Vector of the Qubits (i.e., |010⟩),
        # of the GHZ State, for 3 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_3_qubits_array_010[2] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 3 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_3_qubits_array_010, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 3 Qubits initialized in the state |000⟩;
    # 2) Prepare the Quantum State, |101⟩, by applying the Pauli-X Gate on the first and third Qubits;
    # 3) Prepare of the GHZ State, for 3 Qubits, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩);
    # 4) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩);
    def test_prepare_and_measure_ghz_state_3_qubits_101(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 3

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate3qubits", num_qubits)
        qiskit_classical_register_ghz_state_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate3qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate3qubits",
                                                      qiskit_quantum_register_ghz_state_3_qubits,
                                                      qiskit_classical_register_ghz_state_3_qubits,
                                                      global_phase=0)

        # Prepare the Quantum State, |101⟩, by applying the Pauli-X Gate, on the first and third Qubits
        qiskit_quantum_circuit_3_qubits.apply_pauli_x(0)
        qiskit_quantum_circuit_3_qubits.apply_pauli_x(2)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩), for 3 Qubits
        qiskit_quantum_circuit_ghz_state_3_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_3_qubits",
                            qiskit_quantum_circuit_3_qubits,
                            0, [1, 2]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩), for 3 Qubits
        qiskit_quantum_circuit_ghz_state_101_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_3_qubits_101",
                            qiskit_quantum_circuit_ghz_state_3_qubits_prepared,
                            0, [1, 2]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_101_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 3 Qubits
        qiskit_ghz_state_3_qubits_array_101 = full((num_possible_outcomes,),
                                                   (0. + 0.j))

        # Set the fifth index of the State Vector of the Qubits (i.e., |101⟩),
        # of the GHZ State, for 3 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_3_qubits_array_101[5] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 3 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_3_qubits_array_101, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 3 Qubits initialized in the state |000⟩;
    # 2) Prepare the Quantum State, |111⟩, by applying the Pauli-X in all the Qubits;
    # 3) Prepare of the GHZ State, for 3 Qubits, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩);
    # 4) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩);
    def test_prepare_and_measure_ghz_state_3_qubits_111(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 3

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate3qubits", num_qubits)
        qiskit_classical_register_ghz_state_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate3qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate3qubits",
                                                      qiskit_quantum_register_ghz_state_3_qubits,
                                                      qiskit_classical_register_ghz_state_3_qubits,
                                                      global_phase=0)

        # Prepare the Quantum State, |111⟩, by applying the Pauli-X Gate, on all the Qubits
        qiskit_quantum_circuit_3_qubits.apply_pauli_x(0)
        qiskit_quantum_circuit_3_qubits.apply_pauli_x(1)
        qiskit_quantum_circuit_3_qubits.apply_pauli_x(2)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩), for 3 Qubits
        qiskit_quantum_circuit_ghz_state_3_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_3_qubits",
                            qiskit_quantum_circuit_3_qubits,
                            0, [1, 2]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|000⟩ + |111⟩), for 3 Qubits
        qiskit_quantum_circuit_ghz_state_111_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_3_qubits_111",
                            qiskit_quantum_circuit_ghz_state_3_qubits_prepared,
                            0, [1, 2]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_111_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 3 Qubits
        qiskit_ghz_state_3_qubits_array_111 = full((num_possible_outcomes,),
                                                   (0. + 0.j))

        # Set the fifth index of the State Vector of the Qubits (i.e., |101⟩),
        # of the GHZ State, for 3 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_3_qubits_array_111[(num_possible_outcomes - 1)] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 3 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_3_qubits_array_111, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


# Test Cases for prepare and measure the GHZ States, for 4 Qubits, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩)
class PrepareAndMeasureGHZState4Qubits(unittest.TestCase):

    # Test #1 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 4 Qubits initialized in the state |0000⟩;
    # 2) Prepare of the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩);
    # 3) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩);
    def test_prepare_and_measure_ghz_state_4_qubits_0000(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 4

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_4_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate4qubits", num_qubits)
        qiskit_classical_register_ghz_state_4_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate4qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_4_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate4qubits",
                                                      qiskit_quantum_register_ghz_state_4_qubits,
                                                      qiskit_classical_register_ghz_state_4_qubits,
                                                      global_phase=0)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩), for 4 Qubits
        qiskit_quantum_circuit_ghz_state_4_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_4_qubits",
                            qiskit_quantum_circuit_4_qubits,
                            0, [1, 2, 3]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩), for 4 Qubits
        qiskit_quantum_circuit_ghz_state_0000_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_4_qubits_0000",
                            qiskit_quantum_circuit_ghz_state_4_qubits_prepared,
                            0, [1, 2, 3]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_0000_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 4 Qubits
        qiskit_ghz_state_4_qubits_array_0000 = full((num_possible_outcomes,),
                                                    (0. + 0.j))

        # Set the first index of the State Vector of the Qubits (i.e., |0000⟩),
        # of the GHZ State, for 4 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_4_qubits_array_0000[0] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 4 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_4_qubits_array_0000, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 4 Qubits initialized in the state |0000⟩;
    # 2) Prepare the Quantum State, |0100⟩, by applying the Pauli-X Gate on the third Qubit;
    # 3) Prepare of the GHZ State, for 4 Qubits, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩);
    # 4) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩);
    def test_prepare_and_measure_ghz_state_4_qubits_0100(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 4

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_4_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate4qubits", num_qubits)
        qiskit_classical_register_ghz_state_4_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate4qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_4_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate4qubits",
                                                      qiskit_quantum_register_ghz_state_4_qubits,
                                                      qiskit_classical_register_ghz_state_4_qubits,
                                                      global_phase=0)

        # Prepare the Quantum State, |0100⟩, by applying the Pauli-X Gate, on the third Qubit
        qiskit_quantum_circuit_4_qubits.apply_pauli_x(2)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩), for 4 Qubits
        qiskit_quantum_circuit_ghz_state_4_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_4_qubits",
                            qiskit_quantum_circuit_4_qubits,
                            0, [1, 2, 3]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩), for 4 Qubits
        qiskit_quantum_circuit_ghz_state_0100_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_4_qubits_0100",
                            qiskit_quantum_circuit_ghz_state_4_qubits_prepared,
                            0, [1, 2, 3]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_0100_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 4 Qubits
        qiskit_ghz_state_4_qubits_array_0100 = full((num_possible_outcomes,),
                                                    (0. + 0.j))

        # Set the third index of the State Vector of the Qubits (i.e., |0100⟩),
        # of the GHZ State, for 4 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_4_qubits_array_0100[4] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 4 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_4_qubits_array_0100, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 4 Qubits initialized in the state |0000⟩;
    # 2) Prepare the Quantum State, |1011⟩, by applying the Pauli-X Gate on the first and third Qubits;
    # 3) Prepare of the GHZ State, for 4 Qubits, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩);
    # 4) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩);
    def test_prepare_and_measure_ghz_state_4_qubits_1011(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 4

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_4_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate4qubits", num_qubits)
        qiskit_classical_register_ghz_state_4_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate4qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_4_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate4qubits",
                                                      qiskit_quantum_register_ghz_state_4_qubits,
                                                      qiskit_classical_register_ghz_state_4_qubits,
                                                      global_phase=0)

        # Prepare the Quantum State, |1011⟩, by applying the Pauli-X Gate, on the first, second and forth Qubits
        qiskit_quantum_circuit_4_qubits.apply_pauli_x(0)
        qiskit_quantum_circuit_4_qubits.apply_pauli_x(1)
        qiskit_quantum_circuit_4_qubits.apply_pauli_x(3)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩), for 4 Qubits
        qiskit_quantum_circuit_ghz_state_4_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_4_qubits",
                            qiskit_quantum_circuit_4_qubits,
                            0, [1, 2, 3]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩), for 4 Qubits
        qiskit_quantum_circuit_ghz_state_1011_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_4_qubits_1011",
                            qiskit_quantum_circuit_ghz_state_4_qubits_prepared,
                            0, [1, 2, 3]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_1011_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 4 Qubits
        qiskit_ghz_state_4_qubits_array_1011 = full((num_possible_outcomes,),
                                                    (0. + 0.j))

        # Set the fifth index of the State Vector of the Qubits (i.e., |1011⟩),
        # of the GHZ State, for 4 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_4_qubits_array_1011[11] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 4 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_4_qubits_array_1011, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 4 Qubits initialized in the state |0000⟩;
    # 2) Prepare the Quantum State, |1111⟩, by applying the Pauli-X in all the Qubits;
    # 3) Prepare of the GHZ State, for 4 Qubits, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩);
    # 4) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩);
    def test_prepare_and_measure_ghz_state_4_qubits_1111(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 4

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_4_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate4qubits", num_qubits)
        qiskit_classical_register_ghz_state_4_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate4qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_4_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate4qubits",
                                                      qiskit_quantum_register_ghz_state_4_qubits,
                                                      qiskit_classical_register_ghz_state_4_qubits,
                                                      global_phase=0)

        # Prepare the Quantum State, |1111⟩, by applying the Pauli-X Gate, on all the Qubits
        qiskit_quantum_circuit_4_qubits.apply_pauli_x(0)
        qiskit_quantum_circuit_4_qubits.apply_pauli_x(1)
        qiskit_quantum_circuit_4_qubits.apply_pauli_x(2)
        qiskit_quantum_circuit_4_qubits.apply_pauli_x(3)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩), for 4 Qubits
        qiskit_quantum_circuit_ghz_state_4_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_4_qubits",
                            qiskit_quantum_circuit_4_qubits,
                            0, [1, 2, 3]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩), for 4 Qubits
        qiskit_quantum_circuit_ghz_state_1111_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_4_qubits_1111",
                            qiskit_quantum_circuit_ghz_state_4_qubits_prepared,
                            0, [1, 2, 3]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_1111_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 4 Qubits
        qiskit_ghz_state_4_qubits_array_1111 = full((num_possible_outcomes,),
                                                    (0. + 0.j))

        # Set the last index of the State Vector of the Qubits (i.e., |1111⟩),
        # of the GHZ State, for 4 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_4_qubits_array_1111[(num_possible_outcomes - 1)] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 4 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_4_qubits_array_1111, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


# Test Cases for prepare and measure the GHZ States, for 5 Qubits, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩)
class PrepareAndMeasureGHZState5Qubits(unittest.TestCase):

    # Test #1 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 5 Qubits initialized in the state |00000⟩;
    # 2) Prepare of the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩);
    # 3) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩);
    def test_prepare_and_measure_ghz_state_4_qubits_0000(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 5

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_5_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate5qubits", num_qubits)
        qiskit_classical_register_ghz_state_5_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate5qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_5_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate5qubits",
                                                      qiskit_quantum_register_ghz_state_5_qubits,
                                                      qiskit_classical_register_ghz_state_5_qubits,
                                                      global_phase=0)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩), for 5 Qubits
        qiskit_quantum_circuit_ghz_state_5_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_5_qubits",
                            qiskit_quantum_circuit_5_qubits,
                            0, [1, 2, 3, 4]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩), for 5 Qubits
        qiskit_quantum_circuit_ghz_state_00000_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_5_qubits_00000",
                            qiskit_quantum_circuit_ghz_state_5_qubits_prepared,
                            0, [1, 2, 3, 4]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_00000_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 3 Qubits
        qiskit_ghz_state_5_qubits_array_00000 = full((num_possible_outcomes,),
                                                     (0. + 0.j))

        # Set the first index of the State Vector of the Qubits (i.e., |0000⟩),
        # of the GHZ State, for 5 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_5_qubits_array_00000[0] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 5 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_5_qubits_array_00000, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 5 Qubits initialized in the state |00000⟩;
    # 2) Prepare the Quantum State, |01000⟩, by applying the Pauli-X Gate on the forth Qubit;
    # 3) Prepare of the GHZ State, for 5 Qubits, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩);
    # 4) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩);
    def test_prepare_and_measure_ghz_state_5_qubits_01000(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 5

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_5_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate5qubits", num_qubits)
        qiskit_classical_register_ghz_state_5_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate5qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_5_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate5qubits",
                                                      qiskit_quantum_register_ghz_state_5_qubits,
                                                      qiskit_classical_register_ghz_state_5_qubits,
                                                      global_phase=0)

        # Prepare the Quantum State, |01000⟩, by applying the Pauli-X Gate, on the forth Qubit
        qiskit_quantum_circuit_5_qubits.apply_pauli_x(3)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩), for 5 Qubits
        qiskit_quantum_circuit_ghz_state_5_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_5_qubits",
                            qiskit_quantum_circuit_5_qubits,
                            0, [1, 2, 3, 4]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩), for 5 Qubits
        qiskit_quantum_circuit_ghz_state_01000_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_5_qubits_01000",
                            qiskit_quantum_circuit_ghz_state_5_qubits_prepared,
                            0, [1, 2, 3, 4]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_01000_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 5 Qubits
        qiskit_ghz_state_5_qubits_array_01000 = full((num_possible_outcomes,),
                                                     (0. + 0.j))

        # Set the third index of the State Vector of the Qubits (i.e., |01000⟩),
        # of the GHZ State, for 5 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_5_qubits_array_01000[8] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 5 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_5_qubits_array_01000, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 5 Qubits initialized in the state |00000⟩;
    # 2) Prepare the Quantum State, |10011⟩, by applying the Pauli-X Gate on the first, second and fifth Qubits;
    # 3) Prepare of the GHZ State, for 5 Qubits, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩);
    # 4) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩);
    def test_prepare_and_measure_ghz_state_5_qubits_10011(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 5

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_5_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate5qubits", num_qubits)
        qiskit_classical_register_ghz_state_5_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate5qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_5_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate5qubits",
                                                      qiskit_quantum_register_ghz_state_5_qubits,
                                                      qiskit_classical_register_ghz_state_5_qubits,
                                                      global_phase=0)

        # Prepare the Quantum State, |10011⟩, by applying the Pauli-X Gate, on the first, second and fifth Qubits
        qiskit_quantum_circuit_5_qubits.apply_pauli_x(0)
        qiskit_quantum_circuit_5_qubits.apply_pauli_x(1)
        qiskit_quantum_circuit_5_qubits.apply_pauli_x(4)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩), for 5 Qubits
        qiskit_quantum_circuit_ghz_state_5_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_5_qubits",
                            qiskit_quantum_circuit_5_qubits,
                            0, [1, 2, 3, 4]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|0000⟩ + |1111⟩), for 5 Qubits
        qiskit_quantum_circuit_ghz_state_10011_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_5_qubits_10011",
                            qiskit_quantum_circuit_ghz_state_5_qubits_prepared,
                            0, [1, 2, 3, 4]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_10011_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 5 Qubits
        qiskit_ghz_state_5_qubits_array_10011 = full((num_possible_outcomes,),
                                                     (0. + 0.j))

        # Set the fifth index of the State Vector of the Qubits (i.e., |10011⟩),
        # of the GHZ State, for 5 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_5_qubits_array_10011[19] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 5 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_5_qubits_array_10011, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare and measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 5 Qubits initialized in the state |00000⟩;
    # 2) Prepare the Quantum State, |11111⟩, by applying the Pauli-X in all the Qubits;
    # 3) Prepare of the GHZ State, for 5 Qubits, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩);
    # 4) Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩),
    #    by inverting the Quantum Circuit of GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩);
    def test_prepare_and_measure_ghz_state_5_qubits_1111(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 5

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_ghz_state_5_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrghzstate5qubits", num_qubits)
        qiskit_classical_register_ghz_state_5_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crghzstate5qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_5_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcghzstate5qubits",
                                                      qiskit_quantum_register_ghz_state_5_qubits,
                                                      qiskit_classical_register_ghz_state_5_qubits,
                                                      global_phase=0)

        # Prepare the Quantum State, |11111⟩, by applying the Pauli-X Gate, on all the Qubits
        qiskit_quantum_circuit_5_qubits.apply_pauli_x(0)
        qiskit_quantum_circuit_5_qubits.apply_pauli_x(1)
        qiskit_quantum_circuit_5_qubits.apply_pauli_x(2)
        qiskit_quantum_circuit_5_qubits.apply_pauli_x(3)
        qiskit_quantum_circuit_5_qubits.apply_pauli_x(4)

        # Prepare the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩), for 5 Qubits
        qiskit_quantum_circuit_ghz_state_5_qubits_prepared = QiskitGHZState \
            .QiskitGHZState("ghz_state_5_qubits",
                            qiskit_quantum_circuit_5_qubits,
                            0, [1, 2, 3, 4]).prepare_multipartite_entanglement()

        # Measure the GHZ State, |ψ⟩ = 1/sqrt(2) x (|00000⟩ + |11111⟩), for 5 Qubits
        qiskit_quantum_circuit_ghz_state_11111_measured = QiskitGHZState \
            .QiskitGHZState("ghz_state_5_qubits_1111",
                            qiskit_quantum_circuit_ghz_state_5_qubits_prepared,
                            0, [1, 2, 3, 4]).measure_multipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_ghz_state_11111_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of GHZ State, for 5 Qubits
        qiskit_ghz_state_5_qubits_array_11111 = full((num_possible_outcomes,),
                                                     (0. + 0.j))

        # Set the last index of the State Vector of the Qubits (i.e., |11111⟩),
        # of the GHZ State, for 5 Qubits, with the Complex Number value, (1 + 0j)
        qiskit_ghz_state_5_qubits_array_11111[(num_possible_outcomes - 1)] = (1. + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the GHZ State, for 5 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_ghz_state_5_qubits_array_11111, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':

    # Test Cases for prepare the GHZ States
    ghz_states_prepare_tests_suite = unittest.TestLoader().loadTestsFromTestCase(PrepareGHZStateTests)

    # Test Cases for prepare and measure the GHZ State, for 3 Qubits
    ghz_states_3_qubits_prepare_tests_suite = unittest.TestLoader()\
        .loadTestsFromTestCase(PrepareAndMeasureGHZState3Qubits)

    # Test Cases for prepare and measure the GHZ State, for 4 Qubits
    ghz_states_4_qubits_prepare_tests_suite = unittest.TestLoader()\
        .loadTestsFromTestCase(PrepareAndMeasureGHZState4Qubits)

    # Test Cases for prepare and measure the GHZ State, for 5 Qubits
    ghz_states_5_qubits_prepare_tests_suite = unittest.TestLoader()\
        .loadTestsFromTestCase(PrepareAndMeasureGHZState5Qubits)

    # Create a Global for all the Test Cases established
    all_test_cases = unittest.TestSuite([ghz_states_prepare_tests_suite,
                                         ghz_states_3_qubits_prepare_tests_suite,
                                         ghz_states_4_qubits_prepare_tests_suite,
                                         ghz_states_5_qubits_prepare_tests_suite])
