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

# The possible existing types of Bipartite and Multipartite Quantum Entanglements
POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES = ["BELL_STATE", "GHZ_STATE", "W_STATE", "RESOURCE_STATE", "GRAPH_STATE"]

# The possible configurations of Bipartite Quantum Entanglements (Bell States)
POSSIBLE_CONFIGURATIONS_BELL_STATES = ["EPR_PAIR_STATE", "BELL_STATE_PHI_PLUS", "BELL_STATE_PHI_MINUS",
                                       "BELL_STATE_PSI_PLUS", "BELL_STATE_PSI_MINUS"]
