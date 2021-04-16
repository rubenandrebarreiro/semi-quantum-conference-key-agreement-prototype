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


# Class of the IBM Qiskit's Classical Data Bus
class QiskitClassicalDataBus:

    def __init__(self, qiskit_classical_data_memory, qiskit_classical_communication_interface):

        # Set the Memory provided of the Classical Data Bus
        self.qiskit_classical_data_memory = qiskit_classical_data_memory

        # Set the Communication Interface of the Classical Data Bus
        self.qiskit_classical_communication_interface = qiskit_classical_communication_interface
