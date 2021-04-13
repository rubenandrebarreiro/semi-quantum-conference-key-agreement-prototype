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

# The possible existing types of Bipartite and Multipartite Quantum Entanglements
POSSIBLE_QUANTUM_ENTANGLEMENT_TYPES = ["BELL_STATE", "GHZ_STATE", "W_STATE", "DICKE_STATE",
                                       "RESOURCE_STATE", "GRAPH_STATE", "CLUSTER_STATE"]

# The possible configurations of Bipartite Quantum Entanglements (Bell States)
POSSIBLE_CONFIGURATIONS_BELL_STATES = ["EPR_PAIR_STATE", "BELL_STATE_PHI_PLUS", "BELL_STATE_PHI_MINUS",
                                       "BELL_STATE_PSI_PLUS", "BELL_STATE_PSI_MINUS"]

# The String ID for the Bell State
BELL_STATE = "BELL_STATE"

# The String ID for the EPR Pair State |ϕ^+⟩
EPR_PAIR_STATE = "EPR_PAIR_STATE"

# The String ID for the Bell State |ϕ^+⟩
BELL_STATE_PHI_PLUS = "BELL_STATE_PHI_PLUS"

# The String ID for the Bell State |ϕ^-⟩
BELL_STATE_PHI_MINUS = "BELL_STATE_PHI_MINUS"

# The String ID for the Bell State |ψ^+⟩
BELL_STATE_PSI_PLUS = "BELL_STATE_PSI_PLUS"

# The String ID for the Bell State |ψ^-⟩
BELL_STATE_PSI_MINUS = "BELL_STATE_PSI_MINUS"

# The String ID for the GHZ State
GHZ_STATE = "GHZ_STATE"

# The String ID for the W State
W_STATE = "W_STATE"

# The String ID for the Dicke State
DICKE_STATE = "DICKE_STATE"

# The String ID for the Resource State
RESOURCE_STATE = "RESOURCE_STATE"

# The String ID for the Graph State
GRAPH_STATE = "GRAPH_STATE"

# The String ID for the Cluster State
CLUSTER_STATE = "CLUSTER_STATE"
