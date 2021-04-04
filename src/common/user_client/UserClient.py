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

# Import UUID (version 4) from UUID Python's Library
from uuid import uuid4


# Class of the User/Client
class UserClient:

    # Constructor of the User/Client
    def __init__(self, user_client_name):

        # The UUID (version 4) of the User/Client
        self.user_client_uuid = uuid4()

        # The name of the User/Client
        self.user_client_name = user_client_name

    # Return the UUID (version 4) of the User/Client
    def get_user_client_uuid(self):
        return self.user_client_uuid

    # Return the name of the User/Client
    def get_user_client_name(self):
        return self.user_client_name
