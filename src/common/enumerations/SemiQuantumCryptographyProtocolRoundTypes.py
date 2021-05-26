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

# The Enumerations and Constants

# The possible Semi-Quantum Cryptography Protocol Round Types
POSSIBLE_SEMI_QUANTUM_CRYPTOGRAPHY_PROTOCOL_ROUNDS_TYPES = ["SIFT", "CTRL",
                                                            "MEASURE_AND_RESEND", "REFLECT",
                                                            "SIFT_MEASURE_AND_RESEND", "CTRL_REFLECT"]

# The Bit for the SIFT (Measure and Resend) Rounds of the Protocol
SIFT_MEASURE_AND_RESEND_ROUND_BIT = 0

# The Bit for the CTRL (Reflect) Rounds of the Protocol
CTRL_REFLECT_ROUND_BIT = 1

# The String ID #1 for the SIFT (Measure and Resend) Rounds of the Protocol
SIFT_MEASURE_AND_RESEND_ROUND_1 = "SIFT"

# The String ID #2 for the SIFT (Measure and Resend) Rounds of the Protocol
SIFT_MEASURE_AND_RESEND_ROUND_2 = "MEASURE_AND_RESEND"

# The String ID #3 for the SIFT (Measure and Resend) Rounds of the Protocol
SIFT_MEASURE_AND_RESEND_ROUND_3 = "SIFT_MEASURE_AND_RESEND"

# The String ID #1 for the CTRL (Reflect) Rounds of the Protocol
CTRL_REFLECT_ROUND_1 = "CTRL"

# The String ID #2 for the SIFT (Reflect) Rounds of the Protocol
CTRL_REFLECT_ROUND_2 = "REFLECT"

# The String ID #3 for the SIFT (Reflect) Rounds of the Protocol
CTRL_REFLECT_ROUND_3 = "CTRL_REFLECT"
