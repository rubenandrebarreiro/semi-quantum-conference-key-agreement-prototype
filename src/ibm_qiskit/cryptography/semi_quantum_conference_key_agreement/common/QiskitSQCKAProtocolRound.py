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
    def __init__(self, num_round, qiskit_quantum_circuit, party_owner_times):
        self.num_round = num_round
        self.qiskit_quantum_circuit = qiskit_quantum_circuit
        self.party_owner_times = party_owner_times

    # Return the Number of the Round of the Protocol
    def get_num_round(self):
        return self.num_round

    # Return the Quantum Circuit of the Round of the Protocol
    def get_qiskit_quantum_circuit(self):
        return self.qiskit_quantum_circuit

    # Return the Party's Owner Times for the Slots of the Rounds of the Protocol
    def get_party_owner_times(self):
        return self.party_owner_times

    def print_info(self):
        print