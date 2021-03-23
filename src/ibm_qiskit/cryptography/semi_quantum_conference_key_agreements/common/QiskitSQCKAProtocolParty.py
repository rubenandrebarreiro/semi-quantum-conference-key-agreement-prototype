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


# Class for IBM Qiskit's Party for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocolParty:

    # Constructor for IBM Qiskit's Party for the Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def __init__(self, party_name, master_status):

        # Set the Party's name
        self.party_name = party_name

        # Set the boolean flag, responsible to keep the information about if the Party is
        # the Master of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol or not
        self.master_status = master_status

    # Return the boolean flag, responsible to keep the information about if the Party is
    # the Master of the Semi-Quantum Conference Key Agreement (SQCKA) Protocol or not
    def is_master(self):

        return self.master_status

