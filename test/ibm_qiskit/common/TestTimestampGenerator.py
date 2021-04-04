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

# Import the Timestamp Generator from the IBM's Qiskit's Common Package
from src.common.utils import TimestampGenerator


# Test Cases for Generation of Pseudo Random Timestamps
class TimestampPseudoRandomGeneratorTests(unittest.TestCase):

    # Test #1 for Generation of Timestamps
    # Description of the Test Case:
    # - Generate 10 Pseudo Random Timestamps, being valid for the next 2 minutes;
    def test_generate_10_pseudo_random_timestamps_valid_for_the_next_2_minutes(self):

        # Create the Timestamp's Generator
        timestamp_generator = TimestampGenerator.TimestampGenerator("timestamp_generator")

        # Set the number of Pseudo Random Timestamps to be generated, as 10
        num_pseudo_random_timestamps_to_generate = 10

        # Generate a collection of 10 Pseudo Random Timestamps
        pseudo_random_timestamps = timestamp_generator\
            .generate_random_timestamps(num_pseudo_random_timestamps_to_generate,
                                        weeks_delta=0, days_delta=0,
                                        hours_delta=0, minutes_delta=2, seconds_delta=60,
                                        milliseconds_delta=0, microseconds_delta=0)

        # Print the initial Logging for the Pseudo Random Timestamps being generated
        print("List of {} Pseudo Random Timestamps generated:\n".format(num_pseudo_random_timestamps_to_generate))

        # Set the number of current Pseudo Random Timestamps, currently generated, as 1
        current_num_pseudo_random_timestamps_generated = 1

        # For each Pseudo Random Timestamps
        for pseudo_random_timestamp in pseudo_random_timestamps:

            # Print the current Pseudo Random Timestamp
            print("Pseudo Random Timestamp {}: {}".format(current_num_pseudo_random_timestamps_generated,
                                                          pseudo_random_timestamp.strftime("%B %d, %Y - %H:%M:%S")))

            # Increases the number of current Pseudo Random Timestamps, currently generated
            current_num_pseudo_random_timestamps_generated = current_num_pseudo_random_timestamps_generated + 1

        # Dummy Assert Equal for Unittest
        self.assertEqual(True, True)


if __name__ == '__main__':

    # Test Cases for Generation of Pseudo Random Timestamps
    pseudo_random_timestamps_tests_suite = \
        unittest.TestLoader().loadTestsFromTestCase(TimestampPseudoRandomGeneratorTests)

    # Create a Global for all the Test Cases established
    all_test_cases = unittest.TestSuite([pseudo_random_timestamps_tests_suite])
