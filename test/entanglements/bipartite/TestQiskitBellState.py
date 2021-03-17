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

# Import N-Dimensional Arrays and Squared Roots from NumPy
from numpy import array, sqrt

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

# Import QiskitBellState from IBM_Qiskit.Entanglements.Bipartite
from ibm_qiskit.entanglements.bipartite import QiskitBellState


# Test Cases for prepare the Bell States
class PrepareBellStateTests(unittest.TestCase):

    # Test #1 for prepare the Bell States
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare of the Bell State (EPR Pair): |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩);
    def test_prepare_epr_pair_bell_state_phi_plus(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_epr_pair_bell_state_phi_plus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatephiplus", num_qubits)
        qiskit_classical_register_epr_pair_bell_state_phi_plus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatephiplus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatephiplus",
                                                      qiskit_quantum_register_epr_pair_bell_state_phi_plus,
                                                      qiskit_classical_register_epr_pair_bell_state_phi_plus,
                                                      global_phase=0)

        # Prepare the EPR Pair (Bell State) for 2 Qubits
        qiskit_quantum_circuit_epr_pair_bell_state_phi_plus = QiskitBellState \
            .QiskitBellState("bell_state_phi_plus_epr_pair",
                             "BELL_STATE_PHI_PLUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_epr_pair_bell_state_phi_plus.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's (EPR Pair) complex values
        qiskit_epr_pair_bell_state_phi_plus_array = array([((1. / sqrt(2.)) + 0.j),
                                                           (0. + 0.j),
                                                           (0. + 0.j),
                                                           ((1. / sqrt(2.)) + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the EPR Pair (Bell State) be prepared
        assert_allclose(final_state_vector, qiskit_epr_pair_bell_state_phi_plus_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare the Bell States
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare of the Bell State: |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩);
    def test_prepare_bell_state_phi_minus(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_phi_minus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatephiminus", num_qubits)
        qiskit_classical_register_bell_state_phi_minus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatephiminus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatephiminus",
                                                      qiskit_quantum_register_bell_state_phi_minus,
                                                      qiskit_classical_register_bell_state_phi_minus,
                                                      global_phase=0)

        # Prepare the Bell State: |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_phi_minus = QiskitBellState \
            .QiskitBellState("bell_state_phi_minus",
                             "BELL_STATE_PHI_MINUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_phi_minus.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_phi_minus_array = array([((1. / sqrt(2.)) + 0.j),
                                                   (0. + 0.j),
                                                   (0. + 0.j),
                                                   (-(1. / sqrt(2.)) + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_phi_minus_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare the Bell States
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare of the Bell State: |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩);
    def test_prepare_bell_state_psi_plus(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_psi_plus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatepsiplus", num_qubits)
        qiskit_classical_register_bell_state_psi_plus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatepsiplus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatepsiplus",
                                                      qiskit_quantum_register_bell_state_psi_plus,
                                                      qiskit_classical_register_bell_state_psi_plus,
                                                      global_phase=0)

        # Prepare the Bell State: |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_plus = QiskitBellState \
            .QiskitBellState("bell_state_psi_plus",
                             "BELL_STATE_PSI_PLUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_psi_plus.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_psi_plus_array = array([(0. + 0.j),
                                                  ((1. / sqrt(2.)) + 0.j),
                                                  ((1. / sqrt(2.)) + 0.j),
                                                  (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_psi_plus_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare the Bell States
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare of the Bell State: |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩);
    def test_prepare_bell_state_psi_minus(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_psi_minus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatepsiminus", num_qubits)
        qiskit_classical_register_bell_state_psi_minus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatepsiminus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatepsiminus",
                                                      qiskit_quantum_register_bell_state_psi_minus,
                                                      qiskit_classical_register_bell_state_psi_minus,
                                                      global_phase=0)

        # Prepare the Bell State: |ψ^+-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_minus = QiskitBellState \
            .QiskitBellState("bell_state_psi_minus",
                             "BELL_STATE_PSI_MINUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_psi_minus.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_psi_minus_array = array([(0. + 0.j),
                                                   ((1. / sqrt(2.)) + 0.j),
                                                   (-(1. / sqrt(2.)) + 0.j),
                                                   (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_psi_minus_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


# Test Cases for prepare and measure the Bell States (EPR Pairs), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
class PrepareAndMeasureEPRPairBellStatePhiPlusTests(unittest.TestCase):

    # Test #1 for prepare and measure the Bell States (EPR Pairs), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare of the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩);
    # 3) Measure the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩),
    #    by inverting the Quantum Circuit of Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩);
    def test_prepare_and_measure_epr_pair_bell_state_phi_plus_00(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_epr_pair_bell_state_phi_plus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatephiplus", num_qubits)
        qiskit_classical_register_epr_pair_bell_state_phi_plus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatephiplus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatephiplus",
                                                      qiskit_quantum_register_epr_pair_bell_state_phi_plus,
                                                      qiskit_classical_register_epr_pair_bell_state_phi_plus,
                                                      global_phase=0)

        # Prepare the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩), for 2 Qubits
        qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_phi_plus_epr_pair",
                             "BELL_STATE_PHI_PLUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩), for 2 Qubits
        qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_measured = QiskitBellState \
            .QiskitBellState("bell_state_phi_plus_epr_pair",
                             "BELL_STATE_PHI_PLUS",
                             qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_epr_pair_bell_state_phi_plus_array_00 = array([(1. + 0.j),
                                                              (0. + 0.j),
                                                              (0. + 0.j),
                                                              (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_epr_pair_bell_state_phi_plus_array_00, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare and measure the Bell States (EPR Pairs), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |01⟩, by applying the Pauli-X Gate on the 1st Qubit;
    # 3) Prepare of the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩);
    # 4) Measure the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩),
    #    by inverting the Quantum Circuit of Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩);
    def test_prepare_and_measure_epr_pair_bell_state_phi_plus_01(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_epr_pair_bell_state_phi_plus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatephiplus", num_qubits)
        qiskit_classical_register_epr_pair_bell_state_phi_plus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatephiplus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatephiplus",
                                                      qiskit_quantum_register_epr_pair_bell_state_phi_plus,
                                                      qiskit_classical_register_epr_pair_bell_state_phi_plus,
                                                      global_phase=0)

        # Prepare the Quantum State |01⟩, by applying the Pauli-X Gate on the 1st Qubit
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(0)

        # Prepare the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩), for 2 Qubits
        qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_phi_plus_epr_pair",
                             "BELL_STATE_PHI_PLUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩), for 2 Qubits
        qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_measured = QiskitBellState \
            .QiskitBellState("bell_state_phi_plus_epr_pair",
                             "BELL_STATE_PHI_PLUS",
                             qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_epr_pair_bell_state_phi_plus_array_01 = array([(0. + 0.j),
                                                              (1. + 0.j),
                                                              (0. + 0.j),
                                                              (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_epr_pair_bell_state_phi_plus_array_01, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare and measure the Bell States (EPR Pairs), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |10⟩, by applying the Pauli-X Gate on the 2nd Qubit;
    # 3) Prepare of the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩);
    # 4) Measure the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩),
    #    by inverting the Quantum Circuit of Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩);
    def test_prepare_and_measure_epr_pair_bell_state_phi_plus_10(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_epr_pair_bell_state_phi_plus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatephiplus", num_qubits)
        qiskit_classical_register_epr_pair_bell_state_phi_plus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatephiplus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatephiplus",
                                                      qiskit_quantum_register_epr_pair_bell_state_phi_plus,
                                                      qiskit_classical_register_epr_pair_bell_state_phi_plus,
                                                      global_phase=0)

        # Prepare the Quantum State |10⟩, by applying the Pauli-X Gate on the 2nd Qubit
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(1)

        # Prepare the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩), for 2 Qubits
        qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_phi_plus_epr_pair",
                             "BELL_STATE_PHI_PLUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩), for 2 Qubits
        qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_measured = QiskitBellState \
            .QiskitBellState("bell_state_phi_plus_epr_pair",
                             "BELL_STATE_PHI_PLUS",
                             qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_epr_pair_bell_state_phi_plus_array_10 = array([(0. + 0.j),
                                                              (0. + 0.j),
                                                              (1. + 0.j),
                                                              (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_epr_pair_bell_state_phi_plus_array_10, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare and measure the Bell States (EPR Pairs), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |11⟩,
    #    by applying the Pauli-X Gate on both of the 1st and 2nd Qubits;
    # 3) Prepare of the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩);
    # 4) Measure the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩),
    #    by inverting the Quantum Circuit of Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩);
    def test_prepare_and_measure_epr_pair_bell_state_phi_plus_11(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_epr_pair_bell_state_phi_plus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatephiplus", num_qubits)
        qiskit_classical_register_epr_pair_bell_state_phi_plus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatephiplus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatephiplus",
                                                      qiskit_quantum_register_epr_pair_bell_state_phi_plus,
                                                      qiskit_classical_register_epr_pair_bell_state_phi_plus,
                                                      global_phase=0)

        # Prepare the Quantum State |11⟩, by applying the Pauli-X Gate on both of the 1st and 2nd Qubits
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(0)
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(1)

        # Prepare the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩), for 2 Qubits
        qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_phi_plus_epr_pair",
                             "BELL_STATE_PHI_PLUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State (EPR Pair), |ϕ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩), for 2 Qubits
        qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_measured = QiskitBellState \
            .QiskitBellState("bell_state_phi_plus_epr_pair",
                             "BELL_STATE_PHI_PLUS",
                             qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_epr_pair_bell_state_phi_plus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_epr_pair_bell_state_phi_plus_array_11 = array([(0. + 0.j),
                                                              (0. + 0.j),
                                                              (0. + 0.j),
                                                              (1. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_epr_pair_bell_state_phi_plus_array_11, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


# Test Cases for prepare and measure the Bell States, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
class PrepareAndMeasureBellStatePhiMinusTests(unittest.TestCase):

    # Test #1 for prepare and measure the Bell States, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare of the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩);
    # 3) Measure the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
    #    by inverting the Quantum Circuit of Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩);
    def test_prepare_and_measure_bell_state_phi_minus_00(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_phi_minus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatephiminus", num_qubits)
        qiskit_classical_register_bell_state_phi_minus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatephiminus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatephiminus",
                                                      qiskit_quantum_register_bell_state_phi_minus,
                                                      qiskit_classical_register_bell_state_phi_minus,
                                                      global_phase=0)

        # Prepare the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_phi_minus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_phi_minus",
                             "BELL_STATE_PHI_MINUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_phi_minus_measured = QiskitBellState \
            .QiskitBellState("bell_state_phi_minus",
                             "BELL_STATE_PHI_MINUS",
                             qiskit_quantum_circuit_bell_state_phi_minus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_phi_minus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_phi_minus_array_00 = array([(1. + 0.j),
                                                      (0. + 0.j),
                                                      (0. + 0.j),
                                                      (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_phi_minus_array_00, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare and measure the Bell States, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |01⟩, by applying the Pauli-X Gate on the 1st Qubit;
    # 3) Prepare of the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩);
    # 4) Measure the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
    #    by inverting the Quantum Circuit of Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩);
    def test_prepare_and_measure_bell_state_phi_minus_01(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_phi_minus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatephiminus", num_qubits)
        qiskit_classical_register_bell_state_phi_minus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatephiminus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatephiminus",
                                                      qiskit_quantum_register_bell_state_phi_minus,
                                                      qiskit_classical_register_bell_state_phi_minus,
                                                      global_phase=0)

        # Prepare the Quantum State |01⟩, by applying the Pauli-X Gate on the 1st Qubit
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(0)

        # Prepare the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
        qiskit_quantum_circuit_epr_pair_bell_state_phi_minus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_phi_minus",
                             "BELL_STATE_PHI_MINUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_phi_minus_measured = QiskitBellState \
            .QiskitBellState("bell_state_phi_minus",
                             "BELL_STATE_PHI_MINUS",
                             qiskit_quantum_circuit_epr_pair_bell_state_phi_minus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_phi_minus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_phi_minus_array_01 = array([(0. + 0.j),
                                                      (1. + 0.j),
                                                      (0. + 0.j),
                                                      (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_phi_minus_array_01, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare and measure the Bell States, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |10⟩, by applying the Pauli-X Gate on the 2nd Qubit;
    # 3) Prepare of the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩);
    # 4) Measure the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
    #    by inverting the Quantum Circuit of Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩);
    def test_prepare_and_measure_bell_state_phi_minus_10(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_phi_minus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatephiminus", num_qubits)
        qiskit_classical_register_bell_state_phi_minus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatephiminus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatephiminus",
                                                      qiskit_quantum_register_bell_state_phi_minus,
                                                      qiskit_classical_register_bell_state_phi_minus,
                                                      global_phase=0)

        # Prepare the Quantum State |10⟩, by applying the Pauli-X Gate on the 2nd Qubit
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(1)

        # Prepare the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_phi_minus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_phi_minus",
                             "BELL_STATE_PHI_MINUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_phi_minus_measured = QiskitBellState \
            .QiskitBellState("bell_state_phi_minus",
                             "BELL_STATE_PHI_MINUS",
                             qiskit_quantum_circuit_bell_state_phi_minus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_phi_minus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_phi_minus_array_10 = array([(0. + 0.j),
                                                      (0. + 0.j),
                                                      (1. + 0.j),
                                                      (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_phi_minus_array_10, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare and measure the Bell States, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |11⟩,
    #    by applying the Pauli-X Gate on both of the 1st and 2nd Qubits;
    # 3) Prepare of the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩);
    # 4) Measure the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩),
    #    by inverting the Quantum Circuit of Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩);
    def test_prepare_and_measure_bell_state_phi_minus_11(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_phi_minus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatephiminus", num_qubits)
        qiskit_classical_register_bell_state_phi_minus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatephiminus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatephiminus",
                                                      qiskit_quantum_register_bell_state_phi_minus,
                                                      qiskit_classical_register_bell_state_phi_minus,
                                                      global_phase=0)

        # Prepare the Quantum State |11⟩, by applying the Pauli-X Gate on both of the 1st and 2nd Qubits
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(0)
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(1)

        # Prepare the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_phi_minus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_phi_minus",
                             "BELL_STATE_PHI_MINUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ϕ^-⟩ = 1/sqrt(2) x (|00⟩ - |11⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_phi_minus_measured = QiskitBellState \
            .QiskitBellState("bell_state_phi_minus",
                             "BELL_STATE_PHI_MINUS",
                             qiskit_quantum_circuit_bell_state_phi_minus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_phi_minus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_phi_minus_array_11 = array([(0. + 0.j),
                                                      (0. + 0.j),
                                                      (0. + 0.j),
                                                      (1. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_phi_minus_array_11, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


# Test Cases for prepare and measure the Bell States, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
class PrepareAndMeasureBellStatePsiPlusTests(unittest.TestCase):

    # Test #1 for prepare and measure the Bell States, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare of the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩);
    # 3) Measure the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
    #    by inverting the Quantum Circuit of Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩);
    def test_prepare_and_measure_bell_state_psi_plus_00(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_psi_plus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatepsiplus", num_qubits)
        qiskit_classical_register_bell_state_psi_plus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatepsiplus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatepsiplus",
                                                      qiskit_quantum_register_bell_state_psi_plus,
                                                      qiskit_classical_register_bell_state_psi_plus,
                                                      global_phase=0)

        # Prepare the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_plus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_psi_plus",
                             "BELL_STATE_PSI_PLUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_plus_measured = QiskitBellState \
            .QiskitBellState("bell_state_psi_plus",
                             "BELL_STATE_PSI_PLUS",
                             qiskit_quantum_circuit_bell_state_psi_plus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_psi_plus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_psi_plus_array_00 = array([(1. + 0.j),
                                                     (0. + 0.j),
                                                     (0. + 0.j),
                                                     (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_psi_plus_array_00, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare and measure the Bell States, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |01⟩, by applying the Pauli-X Gate on the 1st Qubit;
    # 3) Prepare of the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩);
    # 4) Measure the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
    #    by inverting the Quantum Circuit of Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩);
    def test_prepare_and_measure_bell_state_psi_plus_01(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_psi_plus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatepsiplus", num_qubits)
        qiskit_classical_register_bell_state_psi_plus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatepsiplus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatepsiplus",
                                                      qiskit_quantum_register_bell_state_psi_plus,
                                                      qiskit_classical_register_bell_state_psi_plus,
                                                      global_phase=0)

        # Prepare the Quantum State |01⟩, by applying the Pauli-X Gate on the 1st Qubit
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(0)

        # Prepare the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_plus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_psi_plus",
                             "BELL_STATE_PSI_PLUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_plus_measured = QiskitBellState \
            .QiskitBellState("bell_state_psi_plus",
                             "BELL_STATE_PSI_PLUS",
                             qiskit_quantum_circuit_bell_state_psi_plus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_psi_plus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_psi_plus_array_01 = array([(0. + 0.j),
                                                     (1. + 0.j),
                                                     (0. + 0.j),
                                                     (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_psi_plus_array_01, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare and measure the Bell States, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |10⟩, by applying the Pauli-X Gate on the 2nd Qubit;
    # 3) Prepare of the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|00⟩ + |11⟩);
    # 4) Measure the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
    #    by inverting the Quantum Circuit of Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩);
    def test_prepare_and_measure_bell_state_psi_plus_10(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_psi_plus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatepsiplus", num_qubits)
        qiskit_classical_register_bell_state_psi_plus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatepsiplus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatepsiplus",
                                                      qiskit_quantum_register_bell_state_psi_plus,
                                                      qiskit_classical_register_bell_state_psi_plus,
                                                      global_phase=0)

        # Prepare the Quantum State |10⟩, by applying the Pauli-X Gate on the 2nd Qubit
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(1)

        # Prepare the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_plus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_psi_plus",
                             "BELL_STATE_PSI_PLUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_plus_measured = QiskitBellState \
            .QiskitBellState("bell_state_psi_plus",
                             "BELL_STATE_PSI_PLUS",
                             qiskit_quantum_circuit_bell_state_psi_plus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_psi_plus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_psi_plus_array_10 = array([(0. + 0.j),
                                                     (0. + 0.j),
                                                     (1. + 0.j),
                                                     (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_psi_plus_array_10, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare and measure the Bell States, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |11⟩,
    #    by applying the Pauli-X Gate on both of the 1st and 2nd Qubits;
    # 3) Prepare of the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩);
    # 4) Measure the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩),
    #    by inverting the Quantum Circuit of Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩);
    def test_prepare_and_measure_bell_state_psi_plus_11(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_psi_plus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatepsiplus", num_qubits)
        qiskit_classical_register_bell_state_psi_plus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatepsiplus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatepsiplus",
                                                      qiskit_quantum_register_bell_state_psi_plus,
                                                      qiskit_classical_register_bell_state_psi_plus,
                                                      global_phase=0)

        # Prepare the Quantum State |11⟩, by applying the Pauli-X Gate on both of the 1st and 2nd Qubits
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(0)
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(1)

        # Prepare the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_plus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_psi_plus",
                             "BELL_STATE_PSI_PLUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ψ^+⟩ = 1/sqrt(2) x (|01⟩ + |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_plus_measured = QiskitBellState \
            .QiskitBellState("bell_state_psi_plus",
                             "BELL_STATE_PSI_PLUS",
                             qiskit_quantum_circuit_bell_state_psi_plus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_psi_plus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_psi_plus_array_11 = array([(0. + 0.j),
                                                     (0. + 0.j),
                                                     (0. + 0.j),
                                                     (1. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_psi_plus_array_11, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


# Test Cases for prepare and measure the Bell States, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
class PrepareAndMeasureBellStatePsiMinusTests(unittest.TestCase):

    # Test #1 for prepare and measure the Bell States, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare of the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩);
    # 3) Measure the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
    #    by inverting the Quantum Circuit of Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩);
    def test_prepare_and_measure_bell_state_psi_minus_00(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_psi_minus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatepsiminus", num_qubits)
        qiskit_classical_register_bell_state_psi_minus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatepsiminus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatepsiminus",
                                                      qiskit_quantum_register_bell_state_psi_minus,
                                                      qiskit_classical_register_bell_state_psi_minus,
                                                      global_phase=0)

        # Prepare the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_minus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_psi_minus",
                             "BELL_STATE_PSI_MINUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_minus_measured = QiskitBellState \
            .QiskitBellState("bell_state_psi_minus",
                             "BELL_STATE_PSI_MINUS",
                             qiskit_quantum_circuit_bell_state_psi_minus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_psi_minus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_psi_minus_array_00 = array([(1. + 0.j),
                                                      (0. + 0.j),
                                                      (0. + 0.j),
                                                      (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_psi_minus_array_00, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare and measure the Bell States, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |01⟩, by applying the Pauli-X Gate on the 1st Qubit;
    # 3) Prepare of the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩);
    # 4) Measure the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
    #    by inverting the Quantum Circuit of Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩);
    def test_prepare_and_measure_bell_state_psi_minus_01(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_psi_minus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatepsiplus", num_qubits)
        qiskit_classical_register_bell_state_psi_minus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatepsiminus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatepsiminus",
                                                      qiskit_quantum_register_bell_state_psi_minus,
                                                      qiskit_classical_register_bell_state_psi_minus,
                                                      global_phase=0)

        # Prepare the Quantum State |01⟩, by applying the Pauli-X Gate on the 1st Qubit
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(0)

        # Prepare the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_minus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_psi_minus",
                             "BELL_STATE_PSI_MINUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_minus_measured = QiskitBellState \
            .QiskitBellState("bell_state_psi_minus",
                             "BELL_STATE_PSI_MINUS",
                             qiskit_quantum_circuit_bell_state_psi_minus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_psi_minus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_psi_minus_array_01 = array([(0. + 0.j),
                                                      (1. + 0.j),
                                                      (0. + 0.j),
                                                      (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_psi_minus_array_01, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare and measure the Bell States, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |10⟩, by applying the Pauli-X Gate on the 2nd Qubit;
    # 3) Prepare of the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩);
    # 4) Measure the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
    #    by inverting the Quantum Circuit of Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩);
    def test_prepare_and_measure_bell_state_psi_minus_10(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_psi_minus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatepsiminus", num_qubits)
        qiskit_classical_register_bell_state_psi_minus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatepsiminus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatepsiminus",
                                                      qiskit_quantum_register_bell_state_psi_minus,
                                                      qiskit_classical_register_bell_state_psi_minus,
                                                      global_phase=0)

        # Prepare the Quantum State |10⟩, by applying the Pauli-X Gate on the 2nd Qubit
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(1)

        # Prepare the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_minus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_psi_minus",
                             "BELL_STATE_PSI_MINUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_minus_measured = QiskitBellState \
            .QiskitBellState("bell_state_psi_minus",
                             "BELL_STATE_PSI_MINUS",
                             qiskit_quantum_circuit_bell_state_psi_minus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_psi_minus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_psi_minus_array_10 = array([(0. + 0.j),
                                                      (0. + 0.j),
                                                      (1. + 0.j),
                                                      (0. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_psi_minus_array_10, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare and measure the Bell States, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩)
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 2 Qubits initialized in the state |00⟩;
    # 2) Prepare the Quantum State |11⟩,
    #    by applying the Pauli-X Gate on both of the 1st and 2nd Qubits;
    # 3) Prepare of the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩);
    # 4) Measure the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩),
    #    by inverting the Quantum Circuit of Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩);
    def test_prepare_and_measure_bell_state_psi_minus_11(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 2

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_bell_state_psi_minus = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrbellstatepsiminus", num_qubits)
        qiskit_classical_register_bell_state_psi_minus = \
            QiskitClassicalRegister.QiskitClassicalRegister("crbellstatepsiminus", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_2_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcbellstatepsiminus",
                                                      qiskit_quantum_register_bell_state_psi_minus,
                                                      qiskit_classical_register_bell_state_psi_minus,
                                                      global_phase=0)

        # Prepare the Quantum State |11⟩, by applying the Pauli-X Gate on both of the 1st and 2nd Qubits
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(0)
        qiskit_quantum_circuit_2_qubits.apply_pauli_x(1)

        # Prepare the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_minus_prepared = QiskitBellState \
            .QiskitBellState("bell_state_psi_minus",
                             "BELL_STATE_PSI_MINUS",
                             qiskit_quantum_circuit_2_qubits,
                             0, 1).prepare_bipartite_entanglement()

        # Measure the Bell State, |ψ^-⟩ = 1/sqrt(2) x (|01⟩ - |10⟩), for 2 Qubits
        qiskit_quantum_circuit_bell_state_psi_minus_measured = QiskitBellState \
            .QiskitBellState("bell_state_psi_minus",
                             "BELL_STATE_PSI_MINUS",
                             qiskit_quantum_circuit_bell_state_psi_minus_prepared,
                             0, 1).measure_bipartite_entanglement(is_final_measurement=False)

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_bell_state_psi_minus_measured.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Create an array with Bell State's complex values
        qiskit_bell_state_psi_minus_array_11 = array([(0. + 0.j),
                                                      (0. + 0.j),
                                                      (0. + 0.j),
                                                      (1. + 0.j)])

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Bell State be prepared
        assert_allclose(final_state_vector, qiskit_bell_state_psi_minus_array_11, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':

    # Test Cases for prepare the Bell States
    bell_states_prepare_tests_suite = unittest.TestLoader().loadTestsFromTestCase(PrepareBellStateTests)

    # Test Cases for prepare and measure the Bell States
    epr_pair_bell_states_phi_plus_prepare_and_measure_tests_suite = \
        unittest.TestLoader().loadTestsFromTestCase(PrepareAndMeasureEPRPairBellStatePhiPlusTests)
    bell_states_phi_minus_prepare_and_measure_tests_suite = \
        unittest.TestLoader().loadTestsFromTestCase(PrepareAndMeasureBellStatePhiMinusTests)
    bell_states_psi_plus_prepare_and_measure_tests_suite = \
        unittest.TestLoader().loadTestsFromTestCase(PrepareAndMeasureBellStatePsiPlusTests)
    bell_states_psi_minus_prepare_and_measure_tests_suite = \
        unittest.TestLoader().loadTestsFromTestCase(PrepareAndMeasureBellStatePsiMinusTests)

    # Create a Global for all the Test Cases established
    all_test_cases = unittest.TestSuite([bell_states_prepare_tests_suite,
                                         epr_pair_bell_states_phi_plus_prepare_and_measure_tests_suite,
                                         bell_states_phi_minus_prepare_and_measure_tests_suite,
                                         bell_states_psi_plus_prepare_and_measure_tests_suite,
                                         bell_states_psi_minus_prepare_and_measure_tests_suite])
