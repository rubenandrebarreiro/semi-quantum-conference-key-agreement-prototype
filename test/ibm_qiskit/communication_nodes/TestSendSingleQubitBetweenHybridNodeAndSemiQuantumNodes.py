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

# Import Unittest for Python's Unitary Tests
import unittest

# Import N-Dimensional Arrays and Squared Roots from NumPy
from numpy import array, sqrt

# Import Assert_All_Close from NumPy.Testing
from numpy.testing import assert_allclose


# Test Cases for the Sending of a Single Qubit between Hybrid Node and Semi-Quantum Node(s)
class SendSingleQubitBetweenHybridNodeAndSemiQuantumNodesTests(unittest.TestCase):

    # Test #1 for the Sending of a Single Qubit between Quantum Node and Semi-Quantum Node(s)
    # Description of the Test Case:
    # - Alice (with a Quantum Node) prepares a Single Qubit prepared in
    #   the X Basis (Diagonal Basis), in her Hybrid Memory;
    # - Alice outputs the Single Qubit, from the Hybrid Memory to
    #   the Quantum Communication, with Discrete Variables Interface,
    #   via the Quantum Data/Information Bus, with Discrete Variables;
    # - Alice sends the Single Qubit to Bob, through the Quantum Communication Channel,
    #   via Fiber Optic Cable, for Discrete Variables, in Fiber Optic;
    # - Bob inputs the Single Qubit, from the Quantum Communication
    #   with Discrete Variables Interface, to the Semi-Quantum Memory,
    #   via the Quantum Data/Information Bus, with Discrete Variables;
    # - Bob measures the Single Qubit in his Semi-Quantum Memory,
    #   in the Z Basis (Computation Basis);
    def test_send_single_qubit_between_quantum_alice_and_semi_quantum_bob(self):


        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
