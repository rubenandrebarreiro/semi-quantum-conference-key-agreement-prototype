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

# Import QiskitGraphState from IBM_Qiskit.Entanglements.Multipartite.Resource_States
from src.ibm_qiskit.entanglements.multipartite.resource_states import QiskitGraphState


# Test Cases for prepare the Graph States (Resource States)
class PrepareGraphStateTests(unittest.TestCase):

    # Test #1 for prepare the Graph States, for 3 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 3 Qubits initialized in the state |000⟩;
    # 2) The Edges are: {(0,1) ; (1,2)}, this is a three-vertex path, P_3 = {0 <-> 1 <-> 2};
    # 3) Prepare of the Graph State, for 3 Qubits:
    #    |P_3⟩ = 1/sqrt(8) x (|000⟩ + |001⟩ + |010⟩ - |011⟩ +
    #                         |100⟩ + |101⟩ - |110⟩ + |111⟩);
    def test_prepare_graph_state_3_qubits_vertex_path_1(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 3

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_graph_state_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrgraphstate3qubits", num_qubits)
        qiskit_classical_register_graph_state_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crgraphstate3qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcgraphstate3qubits",
                                                      qiskit_quantum_register_graph_state_3_qubits,
                                                      qiskit_classical_register_graph_state_3_qubits,
                                                      global_phase=0)

        # Prepare the Graph State, for 3 Qubits, representing a three-vertex path, P_3 = {1 <-> 0 <-> 2},
        # |P_3⟩ = 1/sqrt(8) x (|000⟩ + |001⟩ + |010⟩ - |011⟩ +
        #                      |100⟩ + |101⟩ - |110⟩ + |111⟩);
        qiskit_quantum_circuit_graph_state_3_qubits = QiskitGraphState \
            .QiskitGraphState("graph_state_3_qubits",
                              qiskit_quantum_circuit_3_qubits,
                              [0, 1, 2], [[0, 1], [1, 2]]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_graph_state_3_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of Graph State, for 3 Qubits
        qiskit_graph_state_3_qubits_array = full((num_possible_outcomes,),
                                                 ((1./sqrt(num_possible_outcomes)) + 0.j))

        # Set the changed phases of the Qubits, regarding the Edges of the Graph
        qiskit_graph_state_3_qubits_array[3] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_3_qubits_array[6] = (-(1./sqrt(num_possible_outcomes)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Graph State (Resource State), for 3 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_graph_state_3_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for prepare the Graph States, for 3 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 3 Qubits initialized in the state |000⟩;
    # 2) The Edges are: {(0,1) ; (0,2)}, this is a three-vertex path, P_3 = {1 <-> 0 <-> 2};
    # 3) Prepare of the Graph State, for 3 Qubits:
    #    |P_3⟩ = 1/sqrt(8) x (|000⟩ + |001⟩ + |010⟩ - |011⟩ +
    #                         |100⟩ - |101⟩ + |110⟩ + |111⟩);
    def test_prepare_graph_state_3_qubits_vertex_path_2(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 3

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_graph_state_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrgraphstate3qubits", num_qubits)
        qiskit_classical_register_graph_state_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crgraphstate3qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcgraphstate3qubits",
                                                      qiskit_quantum_register_graph_state_3_qubits,
                                                      qiskit_classical_register_graph_state_3_qubits,
                                                      global_phase=0)

        # Prepare the Graph State, for 3 Qubits, representing a three-vertex path, P_3 = {1 <-> 0 <-> 2},
        # |P_3⟩ = 1/sqrt(8) x (|000⟩ + |001⟩ + |010⟩ - |011⟩ +
        #                      |100⟩ - |101⟩ + |110⟩ + |111⟩);
        qiskit_quantum_circuit_graph_state_3_qubits = QiskitGraphState \
            .QiskitGraphState("graph_state_3_qubits",
                              qiskit_quantum_circuit_3_qubits,
                              [0, 1, 2], [[0, 1], [0, 2]]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_graph_state_3_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of Graph State, for 3 Qubits
        qiskit_graph_state_3_qubits_array = full((num_possible_outcomes,),
                                                 ((1./sqrt(num_possible_outcomes)) + 0.j))

        # Set the changed phases of the Qubits, regarding the Edges of the Graph
        qiskit_graph_state_3_qubits_array[3] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_3_qubits_array[5] = (-(1./sqrt(num_possible_outcomes)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Graph State (Resource State), for 3 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_graph_state_3_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for prepare the Graph States, for 3 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 3 Qubits initialized in the state |000⟩;
    # 2) The Edges are: {(0,1) ; (0,2) ; (1,2)}, this is a triangle, K_3
    # 3) Prepare of the Graph State, for 3 Qubits:
    #    |K_3⟩ = 1/sqrt(8) x (|000⟩ + |001⟩ + |010⟩ - |011⟩ +
    #                         |100⟩ - |101⟩ - |110⟩ - |111⟩);
    def test_prepare_graph_state_3_qubits_triangle(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 3

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_graph_state_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrgraphstate3qubits", num_qubits)
        qiskit_classical_register_graph_state_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crgraphstate3qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcgraphstate3qubits",
                                                      qiskit_quantum_register_graph_state_3_qubits,
                                                      qiskit_classical_register_graph_state_3_qubits,
                                                      global_phase=0)

        # Prepare the Graph State, for 3 Qubits, representing a triangle, K_3,
        # |K_3⟩ = 1/sqrt(8) x (|000⟩ + |001⟩ + |010⟩ - |011⟩ +
        #                      |100⟩ - |101⟩ - |110⟩ - |111⟩);
        qiskit_quantum_circuit_graph_state_3_qubits = QiskitGraphState \
            .QiskitGraphState("graph_state_3_qubits",
                              qiskit_quantum_circuit_3_qubits,
                              [0, 1, 2], [[0, 1], [0, 2], [1, 2]]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_graph_state_3_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of Graph State, for 3 Qubits
        qiskit_graph_state_3_qubits_array = full((num_possible_outcomes,),
                                                 ((1./sqrt(num_possible_outcomes)) + 0.j))

        # Set the changed phases of the Qubits, regarding the Edges of the Graph
        qiskit_graph_state_3_qubits_array[3] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_3_qubits_array[5] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_3_qubits_array[6] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_3_qubits_array[7] = (-(1./sqrt(num_possible_outcomes)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Graph State (Resource State), for 3 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_graph_state_3_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for prepare the Graph States, for 4 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 4 Qubits initialized in the state |0000⟩;
    # 2) The Edges are: {(0,1) ; (2,3)}, this is a four-vertex path, P_4 = {0 <-> 1 ; 2 <-> 3};
    # 3) Prepare of the Graph State, for 4 Qubits:
    #    |P_4⟩ = 1/4 x (|0000⟩ + |0001⟩ + |0010⟩ - |0011⟩ +
    #                   |0100⟩ + |0101⟩ + |0110⟩ - |0111⟩ +
    #                   |1000⟩ + |1001⟩ + |1010⟩ - |1011⟩ -
    #                   |1100⟩ - |1101⟩ - |1110⟩ + |1111⟩);
    def test_prepare_graph_state_4_qubits_vertex_path_1(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 4

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_graph_state_4_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrgraphstate4qubits", num_qubits)
        qiskit_classical_register_graph_state_4_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crgraphstate4qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_4_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcgraphstate4qubits",
                                                      qiskit_quantum_register_graph_state_4_qubits,
                                                      qiskit_classical_register_graph_state_4_qubits,
                                                      global_phase=0)

        # Prepare the Graph State, for 4 Qubits, representing a four-vertex path, P_4 = {0 <-> 1 ; 2 <-> 3},
        # |P_4⟩ = 1/4 x (|0000⟩ + |0001⟩ + |0010⟩ - |0011⟩ +
        #                |0100⟩ + |0101⟩ + |0110⟩ - |0111⟩ +
        #                |1000⟩ + |1001⟩ + |1010⟩ - |1011⟩ -
        #                |1100⟩ - |1101⟩ - |1110⟩ + |1111⟩);
        qiskit_quantum_circuit_graph_state_4_qubits = QiskitGraphState \
            .QiskitGraphState("graph_state_4_qubits",
                              qiskit_quantum_circuit_4_qubits,
                              [0, 1, 2, 3], [[0, 1], [2, 3]]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_graph_state_4_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of Graph State, for 4 Qubits
        qiskit_graph_state_4_qubits_array = full((num_possible_outcomes,),
                                                 ((1./sqrt(num_possible_outcomes)) + 0.j))

        # Set the changed phases of the Qubits, regarding the Edges of the Graph
        qiskit_graph_state_4_qubits_array[3] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[7] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[11] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[12] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[13] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[14] = (-(1./sqrt(num_possible_outcomes)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Graph State (Resource State), for 4 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_graph_state_4_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #5 for prepare the Graph States, for 4 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 4 Qubits initialized in the state |0000⟩;
    # 2) The Edges are: {(0,1) ; (0,2) ; (2,3)}, this is a four-vertex path, P_4 = {1 <-> 0 <-> 2 <-> 3};
    # 3) Prepare of the Graph State, for 4 Qubits:
    #    |P_4⟩ = 1/4 x (|0000⟩ + |0001⟩ + |0010⟩ - |0011⟩ +
    #                   |0100⟩ - |0101⟩ + |0110⟩ + |0111⟩ +
    #                   |1000⟩ + |1001⟩ + |1010⟩ - |1011⟩ -
    #                   |1100⟩ + |1101⟩ - |1110⟩ - |1111⟩);
    def test_prepare_graph_state_4_qubits_vertex_path_2(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 4

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_graph_state_4_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrgraphstate4qubits", num_qubits)
        qiskit_classical_register_graph_state_4_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crgraphstate4qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_4_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcgraphstate4qubits",
                                                      qiskit_quantum_register_graph_state_4_qubits,
                                                      qiskit_classical_register_graph_state_4_qubits,
                                                      global_phase=0)

        # Prepare the Graph State, for 4 Qubits, representing a four-vertex path, P_4 = {1 <-> 0 <-> 2 <->3},
        # |P_4⟩ = 1/4 x (|0000⟩ + |0001⟩ + |0010⟩ - |0011⟩ +
        #                |0100⟩ - |0101⟩ + |0110⟩ + |0111⟩ +
        #                |1000⟩ + |1001⟩ + |1010⟩ - |1011⟩ -
        #                |1100⟩ + |1101⟩ - |1110⟩ - |1111⟩);
        qiskit_quantum_circuit_graph_state_4_qubits = QiskitGraphState \
            .QiskitGraphState("graph_state_4_qubits",
                              qiskit_quantum_circuit_4_qubits,
                              [0, 1, 2, 3], [[0, 1], [0, 2], [2, 3]]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_graph_state_4_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of Graph State, for 4 Qubits
        qiskit_graph_state_4_qubits_array = full((num_possible_outcomes,),
                                                 ((1./sqrt(num_possible_outcomes)) + 0.j))

        # Set the changed phases of the Qubits, regarding the Edges of the Graph
        qiskit_graph_state_4_qubits_array[3] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[5] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[11] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[12] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[14] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[15] = (-(1./sqrt(num_possible_outcomes)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Graph State (Resource State), for 4 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_graph_state_4_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #6 for prepare the Graph States, for 4 Qubits
    # Description of the Test Case:
    # 1) The Quantum Circuit is created with a Quantum Register,
    #    with 4 Qubits initialized in the state |0000⟩;
    # 2) The Edges are: {(0,1) ; (0,2) ; (1,3) ; (2,3)}, this is a square, K_4;
    # 3) Prepare of the Graph State, for 4 Qubits:
    #    |K_4⟩ = 1/4 x (|0000⟩ + |0001⟩ + |0010⟩ - |0011⟩ +
    #                   |0100⟩ - |0101⟩ + |0110⟩ + |0111⟩ +
    #                   |1000⟩ + |1001⟩ - |1010⟩ + |1011⟩ -
    #                   |1100⟩ + |1101⟩ + |1110⟩ + |1111⟩);
    def test_prepare_graph_state_4_qubits_square(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = 4

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_graph_state_4_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrgraphstate4qubits", num_qubits)
        qiskit_classical_register_graph_state_4_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crgraphstate4qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_4_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcgraphstate4qubits",
                                                      qiskit_quantum_register_graph_state_4_qubits,
                                                      qiskit_classical_register_graph_state_4_qubits,
                                                      global_phase=0)

        # Prepare the Graph State, for 4 Qubits, representing a square, K_4,
        # |K_4⟩ = 1/4 x (|0000⟩ + |0001⟩ + |0010⟩ - |0011⟩ +
        #                |0100⟩ - |0101⟩ + |0110⟩ + |0111⟩ +
        #                |1000⟩ + |1001⟩ - |1010⟩ + |1011⟩ -
        #                |1100⟩ + |1101⟩ + |1110⟩ + |1111⟩);
        qiskit_quantum_circuit_graph_state_4_qubits = QiskitGraphState \
            .QiskitGraphState("graph_state_4_qubits",
                              qiskit_quantum_circuit_4_qubits,
                              [0, 1, 2, 3], [[0, 1], [0, 2], [1, 3], [2, 3]]).prepare_multipartite_entanglement()

        # Getting the Backend for the State Vector Representation
        # (i.e., the Quantum State represented as State Vector)
        state_vector_backend = Aer.get_backend('statevector_simulator')

        # Execute the Quantum Circuit and store the Quantum State in a final state vector
        final_state_vector = \
            execute(qiskit_quantum_circuit_graph_state_4_qubits.quantum_circuit,
                    state_vector_backend).result().get_statevector()

        # Compute the number of possible outcomes (i.e., 2^(num_qubits))
        num_possible_outcomes = (2 ** num_qubits)

        # Create and fill an array with the complex values, of Graph State, for 4 Qubits
        qiskit_graph_state_4_qubits_array = full((num_possible_outcomes,),
                                                 ((1./sqrt(num_possible_outcomes)) + 0.j))

        # Set the changed phases of the Qubits, regarding the Edges of the Graph
        qiskit_graph_state_4_qubits_array[3] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[5] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[10] = (-(1./sqrt(num_possible_outcomes)) + 0.j)
        qiskit_graph_state_4_qubits_array[12] = (-(1./sqrt(num_possible_outcomes)) + 0.j)

        # Assert All Close, from NumPy's Testing, for the State Vector of the Qubits,
        # after the Graph State (Resource State), for 4 Qubits, be prepared
        assert_allclose(final_state_vector, qiskit_graph_state_4_qubits_array, rtol=1e-7, atol=1e-7)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':

    # Test Cases for prepare the Graph States (Resource States)
    graph_states_prepare_tests_suite = unittest.TestLoader().loadTestsFromTestCase(PrepareGraphStateTests)

    # Create a Global for all the Test Cases established
    all_test_cases = unittest.TestSuite([graph_states_prepare_tests_suite])
