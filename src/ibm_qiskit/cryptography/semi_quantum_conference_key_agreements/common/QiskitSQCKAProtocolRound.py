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


# Class for IBM Qiskit's Round for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocolRound:

    # Constructor for IBM Qiskit's Round for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def __init__(self, num_current_round, quantum_circuit, time_slots, owner_times):
        self.num_current_round = num_current_round
        self.quantum_circuit = quantum_circuit
        self.time_slots = time_slots
        self.party_owner_times = owner_times
