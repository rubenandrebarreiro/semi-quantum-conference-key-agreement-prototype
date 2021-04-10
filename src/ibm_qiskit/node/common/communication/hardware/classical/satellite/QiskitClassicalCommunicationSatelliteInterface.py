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


# Class for IBM Qiskit's Classical Communication, by Satellite Interface
class QiskitClassicalCommunicationSatelliteInterface:

    # Constructor for IBM Qiskit's Classical Communication, by Satellite Interface
    def __init__(self, classical_communication_satellite_interface_id):

        # Initialise the ID of the IBM Qiskit's Classical Communication, by Satellite Interface
        self.classical_communication_satellite_interface_id = \
            classical_communication_satellite_interface_id
