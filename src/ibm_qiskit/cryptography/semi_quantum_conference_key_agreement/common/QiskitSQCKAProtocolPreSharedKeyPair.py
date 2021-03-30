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

# Import Enumerations and Constants

# Import TimestampGenerator from IBM_Qiskit.Common
from src.ibm_qiskit.common import TimestampGenerator


# Class of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Pre-Shared Key Pair
class QiskitSQCKAProtocolPreSharedKeyPair:

    # Constructor of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Pre-Shared Key
    def __init__(self, party_name_1, party_name_2, bipartite_pre_shared_key):
        self.party_name_1 = party_name_1.lower()
        self.party_name_2 = party_name_2.lower()
        self.bipartite_pre_shared_key = bipartite_pre_shared_key
        self.timestamp = \
            TimestampGenerator.TimestampGenerator("pre-shared-key-{}-{}"
                                                  .format(self.party_name_1.lower(),
                                                          self.party_name_2.lower())).get_now_timestamp()

    # Return the name of the Party #1
    def get_party_name_1(self):
        return self.party_name_1

    # Return the name of the Party #2
    def get_party_name_2(self):
        return self.party_name_2

    # Return the Bipartite Pre-Shared Key
    def get_bipartite_pre_shared_key(self):
        return self.bipartite_pre_shared_key

    # Return the Timestamp of the generation of the Bipartite Pre-Shared Key
    def get_timestamp(self):
        return self.timestamp

    # Print the information about
    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Bipartite Pre-Shared Key Pair
    def print_info(self):
        print(" - ( {} , {} ) [{}]: {}".format(self.party_name_1, self.party_name_2,
                                               self.timestamp, self.bipartite_pre_shared_key))
