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

# Import QiskitQuantumCircuit from IBM_Qiskit.Circuit
from src.ibm_qiskit.circuit import QiskitQuantumCircuit

# Import QiskitClassicalRegister from IBM_Qiskit.Circuit.Classical
from src.ibm_qiskit.circuit.registers.classical import QiskitClassicalRegister

# Import QiskitQuantumRegister from IBM_Qiskit.Circuit.Quantum
from src.ibm_qiskit.circuit.registers.quantum import QiskitQuantumRegister


# Constants

# The number of Qubits and Bits needed, for Coin (just 1)
NUM_QUBITS_FOR_COIN = NUM_BITS_FOR_COIN = 1


# Class for IBM Qiskit's Quantum Coin Tossing
class QiskitQuantumCoinTossing:

    def __init__(self, name_quantum_coin_tossing):
        self.name_quantum_coin_tossing = name_quantum_coin_tossing
        self.tossed = False

    def toss_coin(self):

        # If the Coin was not tossed yet
        if not self.tossed:

            # Creation of the IBM Qiskit's Quantum and Classical Registers
            qiskit_quantum_register_coin_tossing = \
                QiskitQuantumRegister\
                .QiskitQuantumRegister("qrcoin{}qubit(s)".format(NUM_QUBITS_FOR_COIN), NUM_QUBITS_FOR_COIN)
            qiskit_classical_register_coin_tossing = \
                QiskitClassicalRegister\
                .QiskitClassicalRegister("crcoin{}qubit(s)".format(NUM_QUBITS_FOR_COIN), NUM_QUBITS_FOR_COIN)

            # Creation of the IBM Qiskit's Quantum Circuit with one Quantum and Classical Registers
            qiskit_quantum_circuit_coin_tossing = \
                QiskitQuantumCircuit.QiskitQuantumCircuit("qccoin{}qubit(s)".format(NUM_QUBITS_FOR_COIN),
                                                          qiskit_quantum_register_coin_tossing,
                                                          qiskit_classical_register_coin_tossing,
                                                          global_phase=0)

            # Apply the Hadamard Gate to the Qubit, representing the Coin
            qiskit_quantum_circuit_coin_tossing.apply_hadamard((NUM_QUBITS_FOR_COIN - 1))

            # Measure the Qubit, representing the Coin, storing the result on the respective Bit
            qiskit_quantum_circuit_coin_tossing.measure_single_qubit((NUM_QUBITS_FOR_COIN - 1), (NUM_BITS_FOR_COIN - 1))

        # If the Coin was already tossed
        else:

            raise ValueError("This coin was already tossed!")
