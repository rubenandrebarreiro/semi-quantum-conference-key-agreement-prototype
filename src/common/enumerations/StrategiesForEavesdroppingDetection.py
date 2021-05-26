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

# The possible Strategies for Eavesdropping Detection
POSSIBLE_STRATEGIES_FOR_EAVESDROPPING_DETECTION = ["MEASUREMENT_BY_INVERTING_QUANTUM_CIRCUIT",
                                                   "SWAP_TEST", "STATISTICAL_TEST"]

# The String ID of the Strategy of Measurement by Inverting Quantum Circuit
MEASUREMENT_BY_INVERTING_QUANTUM_CIRCUIT = "MEASUREMENT_BY_INVERTING_QUANTUM_CIRCUIT"

# The String ID of the Strategy of SWAP Test
SWAP_TEST = "SWAP_TEST"

# The String ID of the Strategy of Statistical Test
STATISTICAL_TEST = "STATISTICAL_TEST"
