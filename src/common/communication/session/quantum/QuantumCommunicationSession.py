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

# Import DateTime from the DateTime Library, as date_time alias
from datetime import datetime as date_time

# Import TimestampGenerator from Common.Utils
from src.common.utils import TimestampGenerator


# Class of the Quantum Communication Session
class QuantumCommunicationSession:

    # Constructor of the Quantum Communication Session
    def __init__(self, quantum_communication_session_id, quantum_communication_duration_minutes,
                 user_client_1, user_client_2):

        # Initialise the ID of the Quantum Communication Session
        self.quantum_communication_session_id = quantum_communication_session_id

        # Initialise the User/Client #1 of the Quantum Communication Session
        self.user_client_1 = user_client_1

        # Initialise the User/Client #2 of the Quantum Communication Session
        self.user_client_2 = user_client_2

        # Initialise the Timestamp Generator of the Quantum Communication Session
        self.quantum_communication_session_timestamp_generator = \
            TimestampGenerator.TimestampGenerator("quantum-communication-session-{}-and-{}-{}"
                                                  .format(self.quantum_communication_session_id,
                                                          user_client_1.get_user_client_name(),
                                                          user_client_2.get_user_client_name()))

        # Initialise the Timestamp of the establishment of the Quantum Communication Session
        self.quantum_communication_session_established_timestamp_customised_format = \
            self.quantum_communication_session_timestamp_generator.get_now_customised_format()

        # Set the Duration (in minutes) of the Quantum Communication Session
        self.quantum_communication_duration_minutes = quantum_communication_duration_minutes

    # Verify if the Quantum Communication, already expired or not
    def is_quantum_communication_session_expired(self):

        # Retrieve the Timestamp of the current DateTime
        current_date_time_timestamp = \
            date_time.timestamp(date_time.now())

        # Retrieve the Timestamp of the expiration of
        # the Quantum Communication Session
        quantum_communication_session_expiration_timestamp = \
            self.quantum_communication_session_timestamp_generator\
                .get_now_plus_delta_timestamp(weeks_delta=0,
                                              days_delta=0,
                                              hours_delta=0,
                                              minutes_delta=self.quantum_communication_duration_minutes,
                                              seconds_delta=0,
                                              milliseconds_delta=0,
                                              microseconds_delta=0)

        # Set the Conditional Verification about if
        # the Quantum Communication Session is already expired or not
        is_quantum_communication_session_expired = \
            (current_date_time_timestamp > quantum_communication_session_expiration_timestamp)

        # Return if the Conditional Verification about if
        # the Quantum Communication Session is already expired or not
        return is_quantum_communication_session_expired
