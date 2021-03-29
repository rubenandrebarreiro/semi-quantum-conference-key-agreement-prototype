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

# Import Packages and Libraries

# Import the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
# from IBM Qiskit's Cryptography.Semi_Quantum_Conference_Key_Agreement Module
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreements.QiskitSQCKAProtocol import \
    QiskitSQCKAProtocol

# Import the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Party
# from IBM Qiskit's Cryptography.Semi_Quantum_Conference_Key_Agreement Module
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreements.common.QiskitSQCKAProtocolParty import \
    QiskitSQCKAProtocolParty

# Import the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Round
# from IBM Qiskit's Cryptography.Semi_Quantum_Conference_Key_Agreement Module
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreements.common.QiskitSQCKAProtocolRound import \
    QiskitSQCKAProtocolRound


# Class for the Executor of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocolExecutor:

    def __init__(self, num_rounds, parties_names, party_name_master, bipartite_pre_shared_keys,
                 num_quantum_communication_channels, preparing_bases, quantum_entanglement_type):

        self.qiskit_qcka_protocol = QiskitSQCKAProtocol(num_rounds, parties_names, party_name_master,
                                                        bipartite_pre_shared_keys, num_quantum_communication_channels,
                                                        preparing_bases, quantum_entanglement_type.upper)

        self.qiskit_qcka_protocol_parties = {}
        self.qiskit_qcka_protocol_master_party = None

        for current_party_id in range(len(parties_names)):

            if parties_names[current_party_id].upper() == party_name_master.upper():

                self.qiskit_qcka_protocol_parties[current_party_id] = \
                    QiskitSQCKAProtocolParty(current_party_id, parties_names[current_party_id], True,
                                             bipartite_pre_shared_keys)

                self.qiskit_qcka_protocol_master_party = self.qiskit_qcka_protocol_parties[current_party_id]

            else:

                self.qiskit_qcka_protocol_parties[current_party_id] = \
                    QiskitSQCKAProtocolParty(current_party_id, parties_names[current_party_id], False,
                                             bipartite_pre_shared_keys[current_party_id])

        if (self.qiskit_qcka_protocol_master_party is None) or\
                (self.qiskit_qcka_protocol_master_party.is_master() is not True):

            raise ValueError("The Semi-Quantum Conference Key Agreement (QCKA) Protocol "
                             "needs a Master Party to be configured!!!")

        self.qiskit_qcka_protocol_rounds = {}

        for current_protocol_round in range(num_rounds):

            self.qiskit_qcka_protocol_rounds[current_protocol_round] = None


