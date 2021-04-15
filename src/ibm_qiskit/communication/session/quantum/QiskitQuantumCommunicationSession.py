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

# Import IBM Qiskit's Hybrid,
# Hybrid with Discrete Variables, Hybrid with Continuous Variables Nodes,
# from the IBM_Qiskit.Node.End_Node.Hybrid
from src.ibm_qiskit.node.end_node.hybrid import \
    QiskitHybridNode, QiskitHybridNodeWithDiscreteVariables, QiskitHybridNodeWithContinuousVariables

# Import IBM Qiskit's Semi-Quantum,
# Semi-Quantum with Discrete Variables, Semi-Quantum with Continuous Variables Nodes,
# from the IBM_Qiskit.Node.End_Node.Semi_Quantum
from src.ibm_qiskit.node.end_node.semi_quantum import \
    QiskitSemiQuantumNode, QiskitSemiQuantumNodeWithDiscreteVariables, QiskitSemiQuantumNodeWithContinuousVariables

# Import IBM Qiskit's Quantum,
# Quantum with Discrete Variables, Quantum with Continuous Variables Nodes,
# from the IBM_Qiskit.Node.End_Node.Quantum
from src.ibm_qiskit.node.end_node.quantum import \
    QiskitQuantumNode, QiskitQuantumNodeWithDiscreteVariables, QiskitQuantumNodeWithContinuousVariables

# Import DateTime from the DateTime Library, as date_time alias
from datetime import datetime as date_time

# Import TimestampGenerator from Common.Utils
from src.common.utils import TimestampGenerator


# Class of the IBM Qiskit's Quantum Communication Session
class QiskitQuantumCommunicationSession:

    # Constructor of the IBM Qiskit's Quantum Communication Session
    def __init__(self, quantum_communication_session_id, end_node_1, end_node_2,
                 quantum_communication_duration_hours,
                 quantum_communication_duration_minutes,
                 quantum_communication_duration_seconds,
                 quantum_communication_duration_milliseconds,
                 quantum_communication_duration_microseconds):

        # Retrieve the boolean flag to verify if the End Node #1 supports
        # the IBM Qiskit's Quantum Communication Session
        end_node_1_is_valid_for_quantum_communication_session = \
            ((isinstance(end_node_1, QiskitHybridNode
                         .QiskitHybridNode)) or
             (isinstance(end_node_1, QiskitHybridNodeWithDiscreteVariables
                         .QiskitHybridNodeWithDiscreteVariables)) or
             (isinstance(end_node_1, QiskitHybridNodeWithContinuousVariables
                         .QiskitHybridNodeWithContinuousVariables)) or
             (isinstance(end_node_1, QiskitSemiQuantumNode
                         .QiskitSemiQuantumNode)) or
             (isinstance(end_node_1, QiskitSemiQuantumNodeWithDiscreteVariables
                         .QiskitSemiQuantumNodeWithDiscreteVariables)) or
             (isinstance(end_node_1, QiskitSemiQuantumNodeWithContinuousVariables
                         .QiskitSemiQuantumNodeWithContinuousVariables)) or
             (isinstance(end_node_1, QiskitQuantumNode
                         .QiskitQuantumNode)) or
             (isinstance(end_node_1, QiskitQuantumNodeWithDiscreteVariables
                         .QiskitQuantumNodeWithDiscreteVariables)) or
             (isinstance(end_node_1, QiskitQuantumNodeWithContinuousVariables
                         .QiskitQuantumNodeWithContinuousVariables)))

        # Retrieve the boolean flag to verify if the End Node #2 supports
        # the IBM Qiskit's Quantum Communication Session
        end_node_2_is_valid_for_quantum_communication_session = \
            ((isinstance(end_node_2, QiskitHybridNode
                         .QiskitHybridNode)) or
             (isinstance(end_node_2, QiskitHybridNodeWithDiscreteVariables
                         .QiskitHybridNodeWithDiscreteVariables)) or
             (isinstance(end_node_2, QiskitHybridNodeWithContinuousVariables
                         .QiskitHybridNodeWithContinuousVariables)) or
             (isinstance(end_node_2, QiskitSemiQuantumNode
                         .QiskitSemiQuantumNode)) or
             (isinstance(end_node_2, QiskitSemiQuantumNodeWithDiscreteVariables
                         .QiskitSemiQuantumNodeWithDiscreteVariables)) or
             (isinstance(end_node_2, QiskitSemiQuantumNodeWithContinuousVariables
                         .QiskitSemiQuantumNodeWithContinuousVariables)) or
             (isinstance(end_node_2, QiskitQuantumNode
                         .QiskitQuantumNode)) or
             (isinstance(end_node_2, QiskitQuantumNodeWithDiscreteVariables
                         .QiskitQuantumNodeWithDiscreteVariables)) or
             (isinstance(end_node_2, QiskitQuantumNodeWithContinuousVariables
                         .QiskitQuantumNodeWithContinuousVariables)))

        # If the type of the End Node #1 supports a Quantum Communication Session
        if end_node_1_is_valid_for_quantum_communication_session:

            # If the type of the End Node #2 supports a Quantum Communication Session
            if end_node_2_is_valid_for_quantum_communication_session:

                # Initialise the ID of the Quantum Communication Session
                self.quantum_communication_session_id = quantum_communication_session_id

                # Initialise the End Node #1 of the Quantum Communication Session
                self.end_node_1 = end_node_1

                # Initialise the End Node #2 of the Quantum Communication Session
                self.end_node_2 = end_node_2

                # Initialise the Timestamp Generator of the Quantum Communication Session
                self.quantum_communication_session_timestamp_generator = \
                    TimestampGenerator.TimestampGenerator("quantum-communication-session-{}-and-{}-{}"
                                                          .format(self.quantum_communication_session_id,
                                                                  self.end_node_1.get_quantum_node_id(),
                                                                  self.end_node_2.get_quantum_node_id()))

                # Initialise the Timestamp of the establishment of the Quantum Communication Session
                self.quantum_communication_session_established_timestamp_customised_format = \
                    self.quantum_communication_session_timestamp_generator.get_now_customised_format()

                # Set the Duration of the Quantum Communication Session, in Hours
                self.quantum_communication_duration_hours = quantum_communication_duration_hours

                # Set the Duration of the Quantum Communication Session, in Minutes
                self.quantum_communication_duration_minutes = quantum_communication_duration_minutes

                # Set the Duration of the Quantum Communication Session, in Seconds
                self.quantum_communication_duration_seconds = quantum_communication_duration_seconds

                # Set the Duration of the Quantum Communication Session, in Milliseconds
                self.quantum_communication_duration_milliseconds = quantum_communication_duration_milliseconds

                # Set the Duration of the Quantum Communication Session, in Microseconds
                self.quantum_communication_duration_microseconds = quantum_communication_duration_microseconds

            # If the type of the End Node #1 does not support a Quantum Communication Session
            else:

                # Raise a Runtime Error
                raise RuntimeError("The End Node #1 does not support a Quantum Communication Session!!!")

        # If the type of the End Node #2 does not support a Quantum Communication Session
        else:

            # Raise a Runtime Error
            raise RuntimeError("The End Node #2 does not support a Quantum Communication Session!!!")

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
                                              hours_delta=self.quantum_communication_duration_hours,
                                              minutes_delta=self.quantum_communication_duration_minutes,
                                              seconds_delta=self.quantum_communication_duration_seconds,
                                              milliseconds_delta=self.quantum_communication_duration_milliseconds,
                                              microseconds_delta=self.quantum_communication_duration_microseconds)

        # Set the Conditional Verification about if
        # the Quantum Communication Session is already expired or not
        is_quantum_communication_session_expired = \
            (current_date_time_timestamp > quantum_communication_session_expiration_timestamp)

        # Return if the Conditional Verification about if
        # the Quantum Communication Session is already expired or not
        return is_quantum_communication_session_expired
