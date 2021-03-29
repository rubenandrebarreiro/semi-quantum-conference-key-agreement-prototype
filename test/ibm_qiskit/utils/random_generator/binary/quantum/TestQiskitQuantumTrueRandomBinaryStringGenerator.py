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

# Import the QiskitQuantumTrueRandomBinaryStringGenerator from IBM_Qiskit.Utils.Random_Generator.Binary.Quantum
from src.ibm_qiskit.utils.random_generator.binary.quantum import QiskitQuantumTrueRandomBinaryStringGenerator


# Test Cases for the IBM Qiskit's Quantum True Random Binary String Generator (QTRBSG)
class QiskitQuantumTrueRandomBinaryStringGeneratorTests(unittest.TestCase):

    # Test #1 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate one single Quantum True Random Binary String (QTRBS), with a length of 10 bits, for 1 count;
    def test_quantum_one_single_true_random_binary_string_generator_length_10_bits_1_count(self):

        # Set the length of the True Random Binary String, as 10 bits
        binary_string_length = 10

        # Set the number of frequency counting, as 1, for the Measurement results of
        # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
        num_counts = 1

        # The Quantum Circuit for the Quantum True Random Binary String Generator,
        # for a length of 10 bits and 1 count
        qiskit_quantum_true_random_binary_string_generator_10_bits = QiskitQuantumTrueRandomBinaryStringGenerator \
            .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                          .format(binary_string_length),
                                                          binary_string_length=binary_string_length,
                                                          num_counts=num_counts)

        # Generate one single Quantum True Random Binary String (QTRBS), with a length of 10 bits and 1 count
        final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_10_bits = \
            qiskit_quantum_true_random_binary_string_generator_10_bits.generate_true_random_binary_string()

        # Print the initial Logging information for the Test #1
        print("\n\nTEST #1 for the IBM Qiskit's True Random Binary String Generation:\n")

        # Print the True Random Binary String, generated with a length of 10
        print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
            1, binary_string_length, num_counts,
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_10_bits)
        )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #2 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate one single Quantum True Random Binary String (QTRBS), with a length of 10 bits, for 1000 counts;
    def test_quantum_one_single_true_random_binary_string_generator_length_10_bits_1000_counts(self):

        # Set the length of the True Random Binary String, as 10 bits
        binary_string_length = 10

        # Set the number of frequency counting, as 1000, for the Measurement results of
        # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
        num_counts = 1000

        # The Quantum Circuit for the Quantum True Random Binary String Generator,
        # for a length of 10 bits and 1000 counts
        qiskit_quantum_true_random_binary_string_generator_10_bits = QiskitQuantumTrueRandomBinaryStringGenerator\
            .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                          .format(binary_string_length),
                                                          binary_string_length=binary_string_length,
                                                          num_counts=num_counts)

        # Generate one single Quantum True Random Binary String (QTRBS), with a length of 10 bits and 1000 counts
        final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_10_bits = \
            qiskit_quantum_true_random_binary_string_generator_10_bits.generate_true_random_binary_string()

        # Print the initial Logging information for the Test #2
        print("\n\nTEST #2 for the IBM Qiskit's True Random Binary String Generation:\n")

        # Print the True Random Binary String, generated with a length of 10
        print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
            1, binary_string_length, num_counts,
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_10_bits)
        )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #3 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate one single Quantum True Random Binary String (QTRBS), with a length of 20 bits, for 1 count;
    def test_quantum_one_single_true_random_binary_string_generator_length_20_bits_1_count(self):

        # Set the length of the True Random Binary String, as 20 bits
        binary_string_length = 20

        # Set the number of frequency counting, as 1, for the Measurement results of
        # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
        num_counts = 1

        # The Quantum Circuit for the Quantum True Random Binary String Generator,
        # for a length of 20 bits and 1 count
        qiskit_quantum_true_random_binary_string_generator_20_bits = QiskitQuantumTrueRandomBinaryStringGenerator \
            .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                          .format(binary_string_length),
                                                          binary_string_length=binary_string_length,
                                                          num_counts=num_counts)

        # Generate one single Quantum True Random Binary String (QTRBS), with a length of 20 bits and 1 count
        final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_20_bits = \
            qiskit_quantum_true_random_binary_string_generator_20_bits.generate_true_random_binary_string()

        # Print the initial Logging information for the Test #3
        print("\n\nTEST #3 for the IBM Qiskit's True Random Binary String Generation:\n")

        # Print the True Random Binary String, generated with a length of 20 bits
        print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
            1, binary_string_length, num_counts,
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_20_bits)
        )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #4 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate one single Quantum True Random Binary String (QTRBS), with a length of 20 bits, for 1000 counts;
    def test_quantum_one_single_true_random_binary_string_generator_length_20_bits_1000_counts(self):

        # Set the length of the True Random Binary String, as 20
        binary_string_length = 20

        # Set the number of frequency counting, as 1000, for the Measurement results of
        # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
        num_counts = 1000

        # The Quantum Circuit for the Quantum True Random Binary String Generator,
        # for a length of 30 bits and 1000 counts
        qiskit_quantum_true_random_binary_string_generator_20_bits = QiskitQuantumTrueRandomBinaryStringGenerator\
            .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                          .format(binary_string_length),
                                                          binary_string_length=binary_string_length,
                                                          num_counts=num_counts)

        # Generate one single Quantum True Random Binary String (QTRBS), with a length of 20 bits and 1000 counts
        final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_20_bits = \
            qiskit_quantum_true_random_binary_string_generator_20_bits.generate_true_random_binary_string()

        # Print the initial Logging information for the Test #4
        print("\n\nTEST #4 for the IBM Qiskit's True Random Binary String Generation:\n")

        # Print the True Random Binary String, generated with a length of 20
        print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
            1, binary_string_length, num_counts,
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_20_bits)
        )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #5 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate one single Quantum True Random Binary String (QTRBS), with a length of 30 bits, for 1 count;
    def test_quantum_one_single_true_random_binary_string_generator_length_30_bits_1_count(self):

        # Set the length of the True Random Binary String, as 30 bits
        binary_string_length = 30

        # Set the number of frequency counting, as 1, for the Measurement results of
        # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
        num_counts = 1

        # The Quantum Circuit for the Quantum True Random Binary String Generator,
        # for a length of 30 bits and 1 count
        qiskit_quantum_true_random_binary_string_generator_30_bits = QiskitQuantumTrueRandomBinaryStringGenerator \
            .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                          .format(binary_string_length),
                                                          binary_string_length=binary_string_length,
                                                          num_counts=num_counts)

        # Generate one single Quantum True Random Binary String (QTRBS), with a length of 30 bits and 1 count
        final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_30_bits = \
            qiskit_quantum_true_random_binary_string_generator_30_bits.generate_true_random_binary_string()

        # Print the initial Logging information for the Test #5
        print("\n\nTEST #5 for the IBM Qiskit's True Random Binary String Generation:\n")

        # Print the True Random Binary String, generated with a length of 30 bits
        print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
            1, binary_string_length, num_counts,
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_30_bits)
        )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #6 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate one single Quantum True Random Binary String (QTRBS), with a length of 30 bits, for 1000 counts;
    def test_quantum_one_single_true_random_binary_string_generator_length_30_bits_1000_counts(self):

        # Set the length of the True Random Binary String, as 30
        binary_string_length = 30

        # Set the number of frequency counting, as 1000, for the Measurement results of
        # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
        num_counts = 1000

        # The Quantum Circuit for the Quantum True Random Binary String Generator,
        # for a length of 30 bits and 1000 counts
        qiskit_quantum_true_random_binary_string_generator_30_bits = QiskitQuantumTrueRandomBinaryStringGenerator\
            .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                          .format(binary_string_length),
                                                          binary_string_length=binary_string_length,
                                                          num_counts=num_counts)

        # Generate one single Quantum True Random Binary String (QTRBS), with a length of 30 bits and 1000 counts
        final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_30_bits = \
            qiskit_quantum_true_random_binary_string_generator_30_bits.generate_true_random_binary_string()

        # Print the initial Logging information for the Test #6
        print("\n\nTEST #6 for the IBM Qiskit's True Random Binary String Generation:\n")

        # Print the True Random Binary String, generated with a length of 20
        print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
            1, binary_string_length, num_counts,
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_30_bits)
        )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)
    
    # Test #7 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate 10 Quantum True Random Binary Strings (QTRBS), with a length of 10 bits, for 1 count;
    def test_quantum_10_true_random_binary_string_generators_length_10_bits_1_count(self):

        # Print the initial Logging information for the Test #7
        print("\n\nTEST #7 for the IBM Qiskit's True Random Binary String Generation:\n")

        # For each iteration of a total of 10
        for current_random_binary_string in range(10):

            # Set the length of the True Random Binary String, as 10 bits
            binary_string_length = 10

            # Set the number of frequency counting, as 1, for the Measurement results of
            # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
            num_counts = 1

            # The Quantum Circuit for the Quantum True Random Binary String Generator,
            # for a length of 10 bits and 1 count
            qiskit_quantum_true_random_binary_string_generator_10_bits = QiskitQuantumTrueRandomBinaryStringGenerator \
                .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                              .format(binary_string_length),
                                                              binary_string_length=binary_string_length,
                                                              num_counts=num_counts)

            # Generate one single Quantum True Random Binary String (QTRBS), with a length of 10 bits and 1 count
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_10_bits = \
                qiskit_quantum_true_random_binary_string_generator_10_bits.generate_true_random_binary_string()

            # Print the True Random Binary String, generated with a length of 10
            print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
                (current_random_binary_string + 1), binary_string_length, num_counts,
                final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_10_bits)
            )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #8 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate 10 Quantum True Random Binary Strings (QTRBS), with a length of 10 bits, for 1000 counts;
    def test_quantum_10_true_random_binary_string_generators_length_10_bits_1000_counts(self):

        # Print the initial Logging information for the Test #8
        print("\n\nTEST #8 for the IBM Qiskit's True Random Binary String Generation:\n")

        # For each iteration of a total of 10
        for current_random_binary_string in range(10):

            # Set the length of the True Random Binary String, as 10 bits
            binary_string_length = 10

            # Set the number of frequency counting, as 1000, for the Measurement results of
            # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
            num_counts = 1000

            # The Quantum Circuit for the Quantum True Random Binary String Generator,
            # for a length of 10 bits and 1000 counts
            qiskit_quantum_true_random_binary_string_generator_10_bits = QiskitQuantumTrueRandomBinaryStringGenerator \
                .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                              .format(binary_string_length),
                                                              binary_string_length=binary_string_length,
                                                              num_counts=num_counts)

            # Generate one single Quantum True Random Binary String (QTRBS), with a length of 10 bits and 1000 counts
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_10_bits = \
                qiskit_quantum_true_random_binary_string_generator_10_bits.generate_true_random_binary_string()

            # Print the True Random Binary String, generated with a length of 10
            print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
                (current_random_binary_string + 1), binary_string_length, num_counts,
                final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_10_bits)
            )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #9 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate 10 Quantum True Random Binary Strings (QTRBS), with a length of 20 bits, for 1 count;
    def test_quantum_10_true_random_binary_string_generators_length_20_bits_1_count(self):

        # Print the initial Logging information for the Test #9
        print("\n\nTEST #9 for the IBM Qiskit's True Random Binary String Generation:\n")

        # For each iteration of a total of 10
        for current_random_binary_string in range(10):

            # Set the length of the True Random Binary String, as 20 bits
            binary_string_length = 20

            # Set the number of frequency counting, as 1, for the Measurement results of
            # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
            num_counts = 1

            # The Quantum Circuit for the Quantum True Random Binary String Generator,
            # for a length of 20 bits and 1 count
            qiskit_quantum_true_random_binary_string_generator_20_bits = QiskitQuantumTrueRandomBinaryStringGenerator \
                .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                              .format(binary_string_length),
                                                              binary_string_length=binary_string_length,
                                                              num_counts=num_counts)

            # Generate one single Quantum True Random Binary String (QTRBS), with a length of 20 bits and 1 count
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_20_bits = \
                qiskit_quantum_true_random_binary_string_generator_20_bits.generate_true_random_binary_string()

            # Print the True Random Binary String, generated with a length of 20
            print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
                (current_random_binary_string + 1), binary_string_length, num_counts,
                final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_20_bits)
            )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #10 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate 10 Quantum True Random Binary Strings (QTRBS), with a length of 20 bits, for 1000 counts;
    def test_quantum_10_true_random_binary_string_generators_length_20_bits_1000_counts(self):

        # Print the initial Logging information for the Test #10
        print("\n\nTEST #10 for the IBM Qiskit's True Random Binary String Generation:\n")

        # For each iteration of a total of 10
        for current_random_binary_string in range(10):

            # Set the length of the True Random Binary String, as 20 bits
            binary_string_length = 20

            # Set the number of frequency counting, as 1000, for the Measurement results of
            # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
            num_counts = 1000

            # The Quantum Circuit for the Quantum True Random Binary String Generator,
            # for a length of 20 bits and 1000 counts
            qiskit_quantum_true_random_binary_string_generator_20_bits = QiskitQuantumTrueRandomBinaryStringGenerator \
                .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                              .format(binary_string_length),
                                                              binary_string_length=binary_string_length,
                                                              num_counts=num_counts)

            # Generate one single Quantum True Random Binary String (QTRBS), with a length of 20 bits and 1000 counts
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_20_bits = \
                qiskit_quantum_true_random_binary_string_generator_20_bits.generate_true_random_binary_string()

            # Print the True Random Binary String, generated with a length of 20
            print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
                (current_random_binary_string + 1), binary_string_length, num_counts,
                final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_20_bits)
            )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #11 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate 10 Quantum True Random Binary Strings (QTRBS), with a length of 30 bits, for 1 count;
    def test_quantum_10_true_random_binary_string_generators_length_30_bits_1_count(self):

        # Print the initial Logging information for the Test #11
        print("\n\nTEST #11 for the IBM Qiskit's True Random Binary String Generation:\n")

        # For each iteration of a total of 10
        for current_random_binary_string in range(10):

            # Set the length of the True Random Binary String, as 30 bits
            binary_string_length = 30

            # Set the number of frequency counting, as 1, for the Measurement results of
            # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
            num_counts = 1

            # The Quantum Circuit for the Quantum True Random Binary String Generator,
            # for a length of 30 bits and 1 count
            qiskit_quantum_true_random_binary_string_generator_30_bits = QiskitQuantumTrueRandomBinaryStringGenerator \
                .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                              .format(binary_string_length),
                                                              binary_string_length=binary_string_length,
                                                              num_counts=num_counts)

            # Generate one single Quantum True Random Binary String (QTRBS), with a length of 30 bits and 1 count
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_30_bits = \
                qiskit_quantum_true_random_binary_string_generator_30_bits.generate_true_random_binary_string()

            # Print the True Random Binary String, generated with a length of 30
            print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
                (current_random_binary_string + 1), binary_string_length, num_counts,
                final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_30_bits)
            )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)

    # Test #12 for the Quantum True Random Binary String Generator (QTRBSG)
    # Description of the Test Case:
    # 1) Generate 10 Quantum True Random Binary Strings (QTRBS), with a length of 30 bits, for 1000 counts;
    def test_quantum_10_true_random_binary_string_generators_length_30_bits_1000_counts(self):

        # Print the initial Logging information for the Test #12
        print("\n\nTEST #12 for the IBM Qiskit's True Random Binary String Generation:\n")

        # For each iteration of a total of 10
        for current_random_binary_string in range(10):

            # Set the length of the True Random Binary String, as 30 bits
            binary_string_length = 30

            # Set the number of frequency counting, as 1000, for the Measurement results of
            # the simulation of the Quantum Circuit, using the Backend for the QASM (Quantum ASseMbly)
            num_counts = 1000

            # The Quantum Circuit for the Quantum True Random Binary String Generator,
            # for a length of 30 bits and 1000 counts
            qiskit_quantum_true_random_binary_string_generator_30_bits = QiskitQuantumTrueRandomBinaryStringGenerator \
                .QiskitQuantumTrueRandomBinaryStringGenerator("quantum_true_random_binary_string_generator_{}_qubits"
                                                              .format(binary_string_length),
                                                              binary_string_length=binary_string_length,
                                                              num_counts=num_counts)

            # Generate one single Quantum True Random Binary String (QTRBS), with a length of 30 bits and 1000 counts
            final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_30_bits = \
                qiskit_quantum_true_random_binary_string_generator_30_bits.generate_true_random_binary_string()

            # Print the True Random Binary String, generated with a length of 30
            print("- True Random Binary String #{} ( length = {} ; counts = {} ): {}".format(
                (current_random_binary_string + 1), binary_string_length, num_counts,
                final_results_frequency_counting_for_qiskit_quantum_true_random_binary_string_generator_30_bits)
            )

        # Perform a Dummy Loop for 5 steps, for a clear print of the Logging information
        for dummy_print_step in range(5):
            pass

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':

    # Test Cases for the IBM Qiskit's Quantum True Random Binary String Generator
    quantum_true_random_binary_string_generator_tests_suite = unittest.TestLoader()\
        .loadTestsFromTestCase(QiskitQuantumTrueRandomBinaryStringGeneratorTests)

    # Create a Global for all the Test Cases established
    all_test_cases = unittest.TestSuite([quantum_true_random_binary_string_generator_tests_suite])
