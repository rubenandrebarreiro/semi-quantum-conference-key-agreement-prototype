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

# Import Libraries and Packages

# Import NoPython mode of Just-In-Time and Parallel Range from Numba
from numba import jit, prange

# Import N-Dimensional Arrays from NumPy
from numpy import array

# Flag of parallelization to specify the parallelization parameter of Numba
USE_NUMBA_PARALLEL = True


# Class for the IBM Qiskit's Quantum Hadamard Transform
class QiskitQuantumHadamardTransform:

    # Constructor for IBM Qiskit's Quantum Hadamard Transform
    def __init__(self, name, quantum_circuit, qubits_indexes):
        self.name = name
        self.quantum_circuit = quantum_circuit
        self.qubits_indexes = qubits_indexes

    # Apply the Quantum Hadamard Transform to
    # the respective given Qubits' indexes in the IBM Qiskit's Quantum Circuit
    # Note: Change the Flag of parallelization "USE_NUMBA_PARALLEL" to
    #       specify the parallelization parameter of Numba
    @jit(nopython=False, forceobj=True, parallel=USE_NUMBA_PARALLEL)
    def apply_transform(self):

        # For each indexed Qubit
        for qubit_index in prange(array(self.qubits_indexes).shape[0]):

            # Apply the Hadamard Gate to the current Qubit index
            self.quantum_circuit.apply_hadamard(qubit_index)

        return self.quantum_circuit
