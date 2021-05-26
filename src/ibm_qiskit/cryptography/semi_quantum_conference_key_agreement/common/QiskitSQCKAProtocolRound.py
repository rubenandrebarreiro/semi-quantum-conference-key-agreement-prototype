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
    def __init__(self, num_round, type_round, qiskit_quantum_circuit, party_entity_owner_times=None):

        # Set the number of the Round
        self.num_round = num_round

        # Set the type of the Round
        self.type_round = type_round

        # Set the IBM Qiskit's Quantum Circuit for the Round
        self.qiskit_quantum_circuit = qiskit_quantum_circuit

        # Set the Results of the Round
        self.round_results = None

        # Set the Party Entity's Owner Times for
        # the Slots of the Rounds of the Protocol
        self.party_entity_owner_times = party_entity_owner_times

    # Return the Number of the Round of the Protocol
    def get_num_round(self):
        return self.num_round

    # Return the Type of the Round of the Protocol
    def get_type_round(self):
        return self.type_round

    # Return the Quantum Circuit of the Round of the Protocol
    def get_qiskit_quantum_circuit(self):
        return self.qiskit_quantum_circuit

    # Update the Quantum Circuit of the Round of the Protocol
    def update_qiskit_quantum_circuit(self, qiskit_quantum_circuit):
        self.qiskit_quantum_circuit = qiskit_quantum_circuit

    # Return the Results of the Round of the Protocol
    def get_round_results(self):
        return self.round_results

    # Save the Results of the Round of the Protocol
    def save_round_results(self, round_results):
        self.round_results = round_results

    # Return the Party Entity's Owner Times for
    # the Slots of the Rounds of the Protocol
    def get_party_owner_times(self):
        return self.party_entity_owner_times
