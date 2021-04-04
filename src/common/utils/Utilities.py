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


# Class of Utilities
class Utilities:

    # Compute the Hamming Weight of a given Binary String
    @staticmethod
    def compute_hamming_weight(binary_string):

        # Initialise the Hamming Weight
        hamming_weight = 0

        # For each bit (binary digit)
        for current_bit in range(len(binary_string)):

            # If the current bit (binary digit) is set to 1
            if binary_string[current_bit] == "1":

                # Increase the Hamming Weight
                hamming_weight += 1

        # Return the computed Hamming Weight
        return hamming_weight
