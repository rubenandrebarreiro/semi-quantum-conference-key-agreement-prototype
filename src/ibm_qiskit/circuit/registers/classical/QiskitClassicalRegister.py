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

# Import required Libraries and Packages

# Import Classical Register from IBM Qiskit
from qiskit import ClassicalRegister


# Class for the IBM Qiskit's Classical Register
class QiskitClassicalRegister:

    # Constructor for IBM Qiskit's Classical Register
    def __init__(self, name, num_bits):

        # The name of the Qiskit's Classical Register
        self.name = name

        # The number of the Bits of the Qiskit's Classical Register
        self.num_bits = num_bits

        # The Classical Register of the Qiskit's Classical Register
        self.classicalRegister = ClassicalRegister(name=name, size=num_bits)
