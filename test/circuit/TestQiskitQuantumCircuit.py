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

# Import QiskitQuantumCircuit from IBM_Qiskit.Circuit
from ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister

# Import Aer and execute from Qiskit
from qiskit import Aer, execute

# Import N-Dimensional Arrays from NumPy
from numpy import array

# Import Assert_All_Close from NumPy.Testing
from numpy.testing import assert_allclose


# Test Cases for the Pauli-I Gate
class PauliIGateTests(unittest.TestCase):

    # Test #1 for the Pauli-I Gate
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 1 Qubit initialized in the state |0⟩;
    # 2) It is applied the Pauli-I Gate to the 1st Qubit, then, |0⟩ ↦ |0⟩;
    def test_apply_pauli_i_1(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 1

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_pauli_i_1 = QiskitQuantumRegister.QiskitQuantumRegister("qrpaulii1", num_qubits)
        qiskit_classical_register_pauli_i_1 = QiskitClassicalRegister.QiskitClassicalRegister("crpaulii1", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_pauli_i_1 = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcpaulii1",
                                                      qiskit_quantum_register_pauli_i_1,
                                                      qiskit_classical_register_pauli_i_1,
                                                      global_phase=0)

        # Apply the Pauli-I Gate to the 1st Qubit of the Quantum Circuit (|0⟩ ↦ |0⟩)
        qiskit_quantum_circuit_pauli_i_1.apply_pauli_i(qiskit_quantum_register_pauli_i_1.quantumRegister[0])

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')
        final_state_vector = \
            execute(qiskit_quantum_circuit_pauli_i_1.quantum_circuit, state_vector_backend).result().get_statevector()

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubit, after the Pauli-X Gate be applied
        assert_allclose(final_state_vector, array([(1. + 0.j), (0. + 0.j)]), rtol=1e-7, atol=0)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for the Pauli-I Gate
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 1 Qubit initialized in the state |0⟩;
    # 2) It is applied the Pauli-I Gate to the 1st Qubit, then, |0⟩ ↦ |0⟩;
    # 3) It is applied, again, the Pauli-I Gate to the 1st Qubit, then, |0⟩ ↦ |0⟩;
    def test_apply_pauli_i_2(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 1

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_pauli_i_2 = QiskitQuantumRegister.QiskitQuantumRegister("qrpaulii2", num_qubits)
        qiskit_classical_register_pauli_i_2 = QiskitClassicalRegister.QiskitClassicalRegister("crpaulii2", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_pauli_i_2 = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcpaulii2",
                                                      qiskit_quantum_register_pauli_i_2,
                                                      qiskit_classical_register_pauli_i_2,
                                                      global_phase=0)

        # Apply the Pauli-I Gate to the 1st Qubit of the Quantum Circuit (|0⟩ ↦ |0⟩)
        qiskit_quantum_circuit_pauli_i_2.apply_pauli_i(qiskit_quantum_register_pauli_i_2.quantumRegister[0])

        # Apply the Pauli-I Gate to the 1st Qubit of the Quantum Circuit, again (|0⟩ ↦ |0⟩)
        qiskit_quantum_circuit_pauli_i_2.apply_pauli_i(qiskit_quantum_register_pauli_i_2.quantumRegister[0])

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')
        final_state_vector = \
            execute(qiskit_quantum_circuit_pauli_i_2.quantum_circuit, state_vector_backend).result().get_statevector()

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubit,
        # after the two Pauli-I Gates be applied
        assert_allclose(final_state_vector, array([(1. + 0.j), (0. + 0.j)]), rtol=1e-7, atol=0)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


# Test Cases for the Pauli-X Gate
class PauliXGateTests(unittest.TestCase):

    # Test #1 for the Pauli-X Gate
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 1 Qubit initialized in the state |0⟩;
    # 2) It is applied the Pauli-X Gate to the 1st Qubit, then, |0⟩ ↦ |1⟩;
    def test_apply_pauli_x_1(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 1

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_pauli_x_1 = QiskitQuantumRegister.QiskitQuantumRegister("qrpaulix1", num_qubits)
        qiskit_classical_register_pauli_x_1 = QiskitClassicalRegister.QiskitClassicalRegister("crpaulix1", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_pauli_x_1 = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcpaulix1",
                                                      qiskit_quantum_register_pauli_x_1,
                                                      qiskit_classical_register_pauli_x_1,
                                                      global_phase=0)

        # Apply the Pauli-X Gate to the 1st Qubit of the Quantum Circuit (|0⟩ ↦ |1⟩)
        qiskit_quantum_circuit_pauli_x_1.apply_pauli_x(qiskit_quantum_register_pauli_x_1.quantumRegister[0])

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')
        final_state_vector = \
            execute(qiskit_quantum_circuit_pauli_x_1.quantum_circuit, state_vector_backend).result().get_statevector()

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubit, after the Pauli-X Gate be applied
        assert_allclose(final_state_vector, array([(0. + 0.j), (1. + 0.j)]), rtol=1e-7, atol=0)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for the Pauli-X Gate
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 1 Qubit initialized in the state |0⟩;
    # 2) It is applied the Pauli-X Gate to the 1st Qubit, then, |0⟩ ↦ |1⟩;
    # 3) It is applied, again, the Pauli-X Gate to the 1st Qubit, then, |1⟩ ↦ |0⟩;
    def test_apply_pauli_x_2(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 1

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_pauli_x_2 = QiskitQuantumRegister.QiskitQuantumRegister("qrpaulix2", num_qubits)
        qiskit_classical_register_pauli_x_2 = QiskitClassicalRegister.QiskitClassicalRegister("crpaulix2", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_pauli_x_2 = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcpaulix2",
                                                      qiskit_quantum_register_pauli_x_2,
                                                      qiskit_classical_register_pauli_x_2,
                                                      global_phase=0)

        # Apply the Pauli-X Gate to the 1st Qubit of the Quantum Circuit (|0⟩ ↦ |1⟩)
        qiskit_quantum_circuit_pauli_x_2.apply_pauli_x(qiskit_quantum_register_pauli_x_2.quantumRegister[0])

        # Apply the Pauli-X Gate to the 1st Qubit of the Quantum Circuit, again (|1⟩ ↦ |0⟩)
        qiskit_quantum_circuit_pauli_x_2.apply_pauli_x(qiskit_quantum_register_pauli_x_2.quantumRegister[0])

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')
        final_state_vector = \
            execute(qiskit_quantum_circuit_pauli_x_2.quantum_circuit, state_vector_backend).result().get_statevector()

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubit,
        # after the two Pauli-X Gates be applied
        assert_allclose(final_state_vector, array([(1. + 0.j), (0. + 0.j)]), rtol=1e-7, atol=0)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


# Test Cases for the Pauli-Y Gate
class PauliYGateTests(unittest.TestCase):

    # Test #1 for the Pauli-Y Gate
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 1 Qubit initialized in the state |0⟩;
    # 2) It is applied the Pauli-Y Gate to the 1st Qubit, then, |0⟩ ↦ |+i⟩;
    def test_apply_pauli_y_1(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 1

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_pauli_y_1 = QiskitQuantumRegister.QiskitQuantumRegister("qrpauliy1", num_qubits)
        qiskit_classical_register_pauli_y_1 = QiskitClassicalRegister.QiskitClassicalRegister("crpauliy1", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_pauli_y_1 = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcpauliy1",
                                                      qiskit_quantum_register_pauli_y_1,
                                                      qiskit_classical_register_pauli_y_1,
                                                      global_phase=0)

        # Apply the Pauli-Y Gate to the 1st Qubit of the Quantum Circuit (|0⟩ ↦ |+i⟩)
        qiskit_quantum_circuit_pauli_y_1.apply_pauli_y(qiskit_quantum_register_pauli_y_1.quantumRegister[0])

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')
        final_state_vector = \
            execute(qiskit_quantum_circuit_pauli_y_1.quantum_circuit, state_vector_backend).result().get_statevector()

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubit, after the Pauli-Y Gate be applied
        assert_allclose(final_state_vector, array([(0. + 0.j), (0. + 1.j)]), rtol=1e-7, atol=0)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for the Pauli-Y Gate
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 1 Qubit initialized in the state |0⟩;
    # 2) It is applied the Pauli-Y Gate to the 1st Qubit, then, |0⟩ ↦ |+i⟩;
    # 3) It is applied, again, the Pauli-Y Gate to the 1st Qubit, then, |+i⟩ ↦ |0⟩;
    def test_apply_pauli_y_2(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 1

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_pauli_y_2 = QiskitQuantumRegister.QiskitQuantumRegister("qrpauliy2", num_qubits)
        qiskit_classical_register_pauli_y_2 = QiskitClassicalRegister.QiskitClassicalRegister("crpauliy2", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_pauli_y_2 = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcpauliy2",
                                                      qiskit_quantum_register_pauli_y_2,
                                                      qiskit_classical_register_pauli_y_2,
                                                      global_phase=0)

        # Apply the Pauli-Y Gate to the 1st Qubit of the Quantum Circuit (|0⟩ ↦ |+i⟩)
        qiskit_quantum_circuit_pauli_y_2.apply_pauli_x(qiskit_quantum_register_pauli_y_2.quantumRegister[0])

        # Apply the Pauli-X Gate to the 1st Qubit of the Quantum Circuit, again (|+i⟩ ↦ |0⟩)
        qiskit_quantum_circuit_pauli_y_2.apply_pauli_x(qiskit_quantum_register_pauli_y_2.quantumRegister[0])

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')
        final_state_vector = \
            execute(qiskit_quantum_circuit_pauli_y_2.quantum_circuit, state_vector_backend).result().get_statevector()

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubit,
        # after the two Pauli-Y Gates be applied
        assert_allclose(final_state_vector, array([(1. + 0.j), (0. + 0.j)]), rtol=1e-7, atol=0)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


# Test Cases for the Pauli-Z Gate
class PauliZGateTests(unittest.TestCase):

    # Test #1 for the Pauli-Z Gate
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 1 Qubit initialized in the state |0⟩;
    # 2) It is applied the Pauli-Z Gate to the 1st Qubit, then, |0⟩ ↦ |0⟩;
    def test_apply_pauli_z_1(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 1

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_pauli_z_1 = QiskitQuantumRegister.QiskitQuantumRegister("qrpauliz1", num_qubits)
        qiskit_classical_register_pauli_z_1 = QiskitClassicalRegister.QiskitClassicalRegister("crpauliz1", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_pauli_z_1 = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcpauliz1",
                                                      qiskit_quantum_register_pauli_z_1,
                                                      qiskit_classical_register_pauli_z_1,
                                                      global_phase=0)

        # Apply the Pauli-Z Gate to the 1st Qubit of the Quantum Circuit (|0⟩ ↦ |0⟩)
        qiskit_quantum_circuit_pauli_z_1.apply_pauli_z(qiskit_quantum_register_pauli_z_1.quantumRegister[0])

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')
        final_state_vector = \
            execute(qiskit_quantum_circuit_pauli_z_1.quantum_circuit, state_vector_backend).result().get_statevector()

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubit, after the Pauli-Y Gate be applied
        assert_allclose(final_state_vector, array([(1. + 0.j), (0. + 0.j)]), rtol=1e-7, atol=0)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for the Pauli-Z Gate
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 1 Qubit initialized in the state |0⟩;
    # 2) It is applied the Pauli-Z Gate to the 1st Qubit, then, |0⟩ ↦ |0⟩;
    # 3) It is applied, again, the Pauli-Z Gate to the 1st Qubit, then, |0⟩ ↦ |0⟩;
    def test_apply_pauli_z_2(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 1

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_pauli_z_2 = QiskitQuantumRegister.QiskitQuantumRegister("qrpauliz2", num_qubits)
        qiskit_classical_register_pauli_z_2 = QiskitClassicalRegister.QiskitClassicalRegister("crpauliz2", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_pauli_z_2 = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcpauliz2",
                                                      qiskit_quantum_register_pauli_z_2,
                                                      qiskit_classical_register_pauli_z_2,
                                                      global_phase=0)

        # Apply the Pauli-Z Gate to the 1st Qubit of the Quantum Circuit (|0⟩ ↦ |0⟩)
        qiskit_quantum_circuit_pauli_z_2.apply_pauli_z(qiskit_quantum_register_pauli_z_2.quantumRegister[0])

        # Apply the Pauli-Z Gate to the 1st Qubit of the Quantum Circuit, again (|0⟩ ↦ |0⟩)
        qiskit_quantum_circuit_pauli_z_2.apply_pauli_z(qiskit_quantum_register_pauli_z_2.quantumRegister[0])

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')
        final_state_vector = \
            execute(qiskit_quantum_circuit_pauli_z_2.quantum_circuit, state_vector_backend).result().get_statevector()

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubit,
        # after the two Pauli-Z Gates be applied
        assert_allclose(final_state_vector, array([(1. + 0.j), (0. + 0.j)]), rtol=1e-7, atol=0)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':

    # Test Cases for the Pauli Gates
    pauli_i_gate_tests_suite = unittest.TestLoader().loadTestsFromTestCase(PauliIGateTests)
    pauli_x_gate_tests_suite = unittest.TestLoader().loadTestsFromTestCase(PauliXGateTests)
    pauli_y_gate_tests_suite = unittest.TestLoader().loadTestsFromTestCase(PauliYGateTests)
    pauli_z_gate_tests_suite = unittest.TestLoader().loadTestsFromTestCase(PauliZGateTests)

    all_test_cases = unittest.TestSuite([pauli_i_gate_tests_suite, pauli_x_gate_tests_suite,
                                         pauli_y_gate_tests_suite, pauli_z_gate_tests_suite])
