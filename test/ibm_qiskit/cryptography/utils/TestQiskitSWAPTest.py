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

# Import required Libraries and Packages

# Import Unittest for Python's Unitary Tests
import unittest

# Import Aer, execute and QiskitError from Qiskit
from qiskit import Aer, execute

# Import QiskitQuantumCircuit from IBM_Qiskit.Circuit
from src.ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister

# Import QiskitGHZState from IBM_Qiskit.Entanglements.Multipartite
from src.ibm_qiskit.entanglements.multipartite import QiskitGHZState

# Import QiskitSWAPTest from IBM_Qiskit.Entanglements.
from src.ibm_qiskit.cryptography.utils import QiskitSWAPTest


# Constants

# The Boolean Flag for the printing of Debug/Statistic Information Flag
DEBUG_STATISTIC_INFORMATION_FLAG = True


# Test Cases for the IBM Qiskit's SWAP Test
class QiskitQuantumTrueRandomBinaryStringGeneratorTests(unittest.TestCase):

    # Test #1 for the SWAP Test, with no Eavesdropping
    # Description of the Test Case:
    # 1) Generate an Ancilla Qubit and two GHZ States,
    #    for 3 Qubits (the original and one copy);
    # 2) Check if the original GHZ State it is equal to its copy,
    #    using the Ancilla Qubit;
    def test_swap_test_ghz_state_3_qubits_with_no_eavesdropping(self):

        # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
        num_qubits = num_bits = (1 + (2 * 3))

        # Creation of the IBM Qiskit's Quantum and Classical Registers
        qiskit_quantum_register_swap_test_ghz_state_3_qubits = \
            QiskitQuantumRegister.QiskitQuantumRegister("qrswaptestghzstate3qubits", num_qubits)
        qiskit_classical_register_swap_test_ghz_state_3_qubits = \
            QiskitClassicalRegister.QiskitClassicalRegister("crswaptestghzstate3qubits", num_bits)

        # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
        qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = \
            QiskitQuantumCircuit.QiskitQuantumCircuit("qcswaptestghzstate3qubits",
                                                      qiskit_quantum_register_swap_test_ghz_state_3_qubits,
                                                      qiskit_classical_register_swap_test_ghz_state_3_qubits,
                                                      global_phase=0)

        # Prepare the GHZ State, for 3 Qubits
        qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = QiskitGHZState \
            .QiskitGHZState("swap_test_ghz_state_3_qubits_original",
                            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits,
                            1, [2, 3]).prepare_multipartite_entanglement()

        # Prepare the copy of the GHZ State, for 3 Qubits
        qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = QiskitGHZState \
            .QiskitGHZState("swap_test_ghz_state_3_qubits_copy",
                            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits,
                            4, [5, 6]).prepare_multipartite_entanglement()

        # Initiate the SWAP Test of the GHZ State, for 3 Qubits
        qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = QiskitSWAPTest \
            .QiskitSWAPTest("swap_test_ghz_state_3_qubits_final",
                            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits,
                            0, 0, [1, 2, 3], [4, 5, 6])\
            .perform_test_to_compare_quantum_states(is_final_measurement=True)

        # Getting the Backend for the QASM (Quantum ASseMbly) for the simulation of the Quantum Circuit
        # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
        qasm_backend = Aer.get_backend("qasm_simulator")

        # Execute the Quantum Circuit and store the Measurement results in a Dictionary Object,
        # for a frequency counting
        final_results_quantum_circuit_measurement = \
            execute(qiskit_quantum_circuit_swap_test_ghz_state_3_qubits.quantum_circuit, qasm_backend, shots=1)\
            .result().get_counts()

        # Retrieve the Bit from the Execution of the Quantum Circuit of the SWAP Test
        # NOTE:
        # - It is necessary to invert the order of the Bits from the Execution of
        #   the Quantum Circuit of the SWAP Test,
        #   since the resulting Bits are presented and ordered,
        #   from the most significant to the least significant one
        ancilla_bit_measurement_result = \
            int(list(final_results_quantum_circuit_measurement.keys())[0][::-1][0])

        # If the Boolean Flag for the printing of Debug/Statistic Information Flag is True
        if DEBUG_STATISTIC_INFORMATION_FLAG:

            # Print some debug/statistics information about the attempts of the SWAP Tests
            print("\n")
            print("------ SWAP Test #1 (with no Eavesdropping) ------")
            print("     - Num. SWAP Tests performed: {}".format(1))
            print("     - Num. SWAP Tests passed: {}".format(1))
            print("\n")

        # Verify if the Measurement Result of the Ancilla Qubit/Bit is equal to 0
        # (i.e., there is no Eavesdropping)
        assert(ancilla_bit_measurement_result == 0)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for the SWAP Test, with no Eavesdropping (for several attempts)
    # Description of the Test Case:
    # 1) Generate an Ancilla Qubit and two GHZ States,
    #    for 3 Qubits (the original and one copy);
    # 2) Check if the original GHZ State it is equal to its copy,
    #    using the Ancilla Qubit;
    def test_swap_test_ghz_state_3_qubits_with_no_eavesdropping_several_attempts(self):

        # Initialise the list of the Statistics for the Ancilla Qubit/Bit Measurement
        ancilla_bit_measurement_result_statistics_list = []

        # Set 6 attempts for the SWAP Test
        # (at average, in a 1/4 = 75% of the times, the Eavesdropping will be detected)
        num_test_attempts = 6

        # For each attempt of the SWAP Test
        for attempt in range(num_test_attempts):

            # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
            num_qubits = num_bits = (1 + (2 * 3))

            # Creation of the IBM Qiskit's Quantum and Classical Registers
            qiskit_quantum_register_swap_test_ghz_state_3_qubits = \
                QiskitQuantumRegister.QiskitQuantumRegister("qrswaptestghzstate3qubits", num_qubits)
            qiskit_classical_register_swap_test_ghz_state_3_qubits = \
                QiskitClassicalRegister.QiskitClassicalRegister("crswaptestghzstate3qubits", num_bits)

            # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = \
                QiskitQuantumCircuit.QiskitQuantumCircuit("qcswaptestghzstate3qubits",
                                                          qiskit_quantum_register_swap_test_ghz_state_3_qubits,
                                                          qiskit_classical_register_swap_test_ghz_state_3_qubits,
                                                          global_phase=0)

            # Prepare the GHZ State, for 3 Qubits
            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = QiskitGHZState \
                .QiskitGHZState("swap_test_ghz_state_3_qubits_original",
                                qiskit_quantum_circuit_swap_test_ghz_state_3_qubits,
                                1, [2, 3]).prepare_multipartite_entanglement()

            # Prepare the copy of the GHZ State, for 3 Qubits
            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = QiskitGHZState \
                .QiskitGHZState("swap_test_ghz_state_3_qubits_copy",
                                qiskit_quantum_circuit_swap_test_ghz_state_3_qubits,
                                4, [5, 6]).prepare_multipartite_entanglement()

            # Initiate the SWAP Test of the GHZ State, for 3 Qubits
            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = QiskitSWAPTest \
                .QiskitSWAPTest("swap_test_ghz_state_3_qubits_final",
                                qiskit_quantum_circuit_swap_test_ghz_state_3_qubits,
                                0, 0, [1, 2, 3], [4, 5, 6])\
                .perform_test_to_compare_quantum_states(is_final_measurement=True)

            # Getting the Backend for the QASM (Quantum ASseMbly) for the simulation of the Quantum Circuit
            # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
            qasm_backend = Aer.get_backend("qasm_simulator")

            # Execute the Quantum Circuit and store the Measurement results in a Dictionary Object,
            # for a frequency counting
            final_results_quantum_circuit_measurement = \
                execute(qiskit_quantum_circuit_swap_test_ghz_state_3_qubits.quantum_circuit, qasm_backend, shots=1)\
                .result().get_counts()

            # Retrieve the Bits from the Execution of the Quantum Circuit of the SWAP Test
            # NOTE:
            # - It is necessary to invert the order of the Bits from the Execution of
            #   the Quantum Circuit of the SWAP Test,
            #   since the resulting Bits are presented and ordered,
            #   from the most significant to the least significant one
            ancilla_bit_measurement_result = \
                int(list(final_results_quantum_circuit_measurement.keys())[0][::-1][0])

            # Append the Measurement Result of the current Ancilla Qubit
            ancilla_bit_measurement_result_statistics_list\
                .append(ancilla_bit_measurement_result)

        # Initialise the number of Tests passed, for no Eavesdropping detected
        num_tests_passed_with_no_eavesdropping = 0

        # For each attempt of the SWAP Test
        for current_test_attempt in range(num_test_attempts):

            # If the SWAP Test does not detect an Eavesdropping situation
            if ancilla_bit_measurement_result_statistics_list[current_test_attempt] == 0:

                # Increment the number of Tests passed, for no Eavesdropping detected
                num_tests_passed_with_no_eavesdropping += 1

        # If the Boolean Flag for the printing of Debug/Statistic Information Flag is True
        if DEBUG_STATISTIC_INFORMATION_FLAG:

            # Print some debug/statistics information about the attempts of the SWAP Tests
            print("\n")
            print("------ SWAP Test #2 (with no Eavesdropping) ------")
            print("     - Num. SWAP Tests performed: {}".format(num_test_attempts))
            print("     - Num. SWAP Tests passed: {}".format(num_tests_passed_with_no_eavesdropping))
            print("\n")

        # Verify if some of the Measurement Results of the Ancilla Qubits,
        # are different than 0 (i.e., there were detected some Eavesdropping situations)
        assert(num_tests_passed_with_no_eavesdropping == num_test_attempts)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for the SWAP Test, with Eavesdropping (for several attempts)
    # Description of the Test Case:
    # 1) Generate an Ancilla Qubit and two GHZ States,
    #    for 3 Qubits (the original and one copy);
    # 2) Check if the original GHZ State it is equal to its copy,
    #    using the Ancilla Qubit;
    def test_swap_test_ghz_state_3_qubits_with_eavesdropping_several_attempts(self):

        # Initialise the list of the Statistics for the Ancilla Qubit/Bit Measurement
        ancilla_bit_measurement_result_statistics_list = []

        # Set 6 attempts for the SWAP Test
        # (at average, in a 1/4 = 75% of the times, the Eavesdropping will be detected)
        num_test_attempts = 6

        # For each attempt of the SWAP Test
        for attempt in range(num_test_attempts):

            # The number of Qubits and Bits, for Quantum and Classical Registers, respectively
            num_qubits = num_bits = (1 + (2 * 3))

            # Creation of the IBM Qiskit's Quantum and Classical Registers
            qiskit_quantum_register_swap_test_ghz_state_3_qubits = \
                QiskitQuantumRegister.QiskitQuantumRegister("qrswaptestghzstate3qubits", num_qubits)
            qiskit_classical_register_swap_test_ghz_state_3_qubits = \
                QiskitClassicalRegister.QiskitClassicalRegister("crswaptestghzstate3qubits", num_bits)

            # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = \
                QiskitQuantumCircuit.QiskitQuantumCircuit("qcswaptestghzstate3qubits",
                                                          qiskit_quantum_register_swap_test_ghz_state_3_qubits,
                                                          qiskit_classical_register_swap_test_ghz_state_3_qubits,
                                                          global_phase=0)

            # Prepare the GHZ State, for 3 Qubits
            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = QiskitGHZState \
                .QiskitGHZState("swap_test_ghz_state_3_qubits_original",
                                qiskit_quantum_circuit_swap_test_ghz_state_3_qubits,
                                1, [2, 3]).prepare_multipartite_entanglement()

            # Prepare the copy of the GHZ State, for 3 Qubits
            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = QiskitGHZState \
                .QiskitGHZState("swap_test_ghz_state_3_qubits_copy",
                                qiskit_quantum_circuit_swap_test_ghz_state_3_qubits,
                                4, [5, 6]).prepare_multipartite_entanglement()

            # Apply the Pauli-X Gate to the 2nd Qubit of the original GHZ State, for 3 Qubits
            # (for the simulation of the Eavesdropping behaviour)
            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits.apply_pauli_x(2)

            # Initiate the SWAP Test of the GHZ State, for 3 Qubits
            qiskit_quantum_circuit_swap_test_ghz_state_3_qubits = QiskitSWAPTest \
                .QiskitSWAPTest("swap_test_ghz_state_3_qubits_final",
                                qiskit_quantum_circuit_swap_test_ghz_state_3_qubits,
                                0, 0, [1, 2, 3], [4, 5, 6])\
                .perform_test_to_compare_quantum_states(is_final_measurement=True)

            # Getting the Backend for the QASM (Quantum ASseMbly) for the simulation of the Quantum Circuit
            # (i.e., the Measurement Results as a Dictionary Object, for a frequency counting)
            qasm_backend = Aer.get_backend("qasm_simulator")

            # Execute the Quantum Circuit and store the Measurement results in a Dictionary Object,
            # for a frequency counting
            final_results_quantum_circuit_measurement = \
                execute(qiskit_quantum_circuit_swap_test_ghz_state_3_qubits.quantum_circuit, qasm_backend, shots=1)\
                .result().get_counts()

            # Retrieve the Bits from the Execution of the Quantum Circuit of the SWAP Test
            # NOTE:
            # - It is necessary to invert the order of the Bits from the Execution of
            #   the Quantum Circuit of the SWAP Test,
            #   since the resulting Bits are presented and ordered,
            #   from the most significant to the least significant one
            ancilla_bit_measurement_result = \
                int(list(final_results_quantum_circuit_measurement.keys())[0][::-1][0])

            # Append the Measurement Result of the current Ancilla Qubit
            ancilla_bit_measurement_result_statistics_list\
                .append(ancilla_bit_measurement_result)

        # Initialise the number of Tests passed, for no Eavesdropping detected
        num_tests_passed_with_no_eavesdropping = 0

        # For each attempt of the SWAP Test
        for current_test_attempt in range(num_test_attempts):

            # If the SWAP Test does not detect an Eavesdropping situation
            if ancilla_bit_measurement_result_statistics_list[current_test_attempt] == 0:

                # Increment the number of Tests passed, for no Eavesdropping detected
                num_tests_passed_with_no_eavesdropping += 1

        # If the Boolean Flag for the printing of Debug/Statistic Information Flag is True
        if DEBUG_STATISTIC_INFORMATION_FLAG:

            # Print some debug/statistics information about the attempts of the SWAP Tests
            print("\n")
            print("------ SWAP Test #3 (with Eavesdropping) ------")
            print("     - Num. SWAP Tests performed: {}".format(num_test_attempts))
            print("     - Num. SWAP Tests passed: {}".format(num_tests_passed_with_no_eavesdropping))
            print("\n")

        # Verify if some of the Measurement Results of the Ancilla Qubits,
        # are different than 0 (i.e., there were detected some Eavesdropping situations)
        assert(num_tests_passed_with_no_eavesdropping < num_test_attempts)

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':

    # Test Cases for the IBM Qiskit's SWAP Test
    swap_test_tests_suite = unittest.TestLoader()\
        .loadTestsFromTestCase(QiskitQuantumTrueRandomBinaryStringGeneratorTests)

    # Create a Global for all the Test Cases established
    all_test_cases = unittest.TestSuite([swap_test_tests_suite])
