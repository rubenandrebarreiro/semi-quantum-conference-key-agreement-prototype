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

# Import TimestampGenerator from Common.Utils
from src.common.utils import TimestampGenerator


# Class of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Pre-Shared Key Pair
class QiskitSQCKAProtocolPreSharedKeyPair:

    # Constructor of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Pre-Shared Key
    def __init__(self, user_client_uuid_1, user_client_uuid_2,
                 user_client_name_1, user_client_name_2, bipartite_pre_shared_key):
        self.user_client_uuid_1 = user_client_uuid_1
        self.user_client_uuid_2 = user_client_uuid_2
        self.user_client_name_1 = user_client_name_1.lower()
        self.user_client_name_2 = user_client_name_2.lower()
        self.bipartite_pre_shared_key = bipartite_pre_shared_key
        self.timestamp = \
            TimestampGenerator.TimestampGenerator("pre-shared-key-{}-{}"
                                                  .format(self.user_client_name_1.lower(),
                                                          self.user_client_name_2.lower())).get_now_timestamp()

    # Return the UUID of the User/Client #1
    def get_user_client_uuid_1(self):
        return self.user_client_uuid_1

    # Return the UUID of the User/Client #2
    def get_user_client_uuid_2(self):
        return self.user_client_uuid_2

    # Return the Name of the User/Client #1
    def get_user_client_name_1(self):
        return self.user_client_name_1

    # Return the Name of the User/Client #2
    def get_user_client_name_2(self):
        return self.user_client_name_2

    # Return the Bipartite Pre-Shared Key
    def get_bipartite_pre_shared_key(self):
        return self.bipartite_pre_shared_key

    # Return the Timestamp of the generation of the Bipartite Pre-Shared Key
    def get_timestamp(self):
        return self.timestamp

    # Print the information about
    # the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Bipartite Pre-Shared Key Pair
    def print_info(self):
        print(" - ( {} , {} ) [{}]: {}\n".format(self.user_client_name_1, self.user_client_name_2,
                                                 self.timestamp, self.bipartite_pre_shared_key))
