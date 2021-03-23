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


# Class for IBM Qiskit's Graph State (Resource State)
class QiskitGraphState:

    # Constructor for IBM Qiskit's Graph State (Resource State)
    def __init__(self, name, quantum_circuit, qubits_vertices_indexes, qubits_edges_indexes):
        self.name = name
        self.quantum_circuit = quantum_circuit
        self.qubits_vertices_indexes = qubits_vertices_indexes
        self.qubits_edges_indexes = qubits_edges_indexes

        # The number of Qubits of the given IBM Qiskit's Quantum Circuit
        num_qubits_quantum_circuit = quantum_circuit.get_num_qubits()

        # If the number of Qubits of the given IBM Qiskit's Quantum Circuit is strictly lower than 2,
        # a Value Error exception will be raised
        if num_qubits_quantum_circuit < 2:

            # Raise the Value Error exception
            raise ValueError("It is impossible to create a Graph State (Resource State),"
                             "from a IBM Qiskit's Quantum Circuit with "
                             "less than 2 Qubits!!!")

    # Prepare the multipartite entanglement for the Graph State (Resource State) configured
    def prepare_multipartite_entanglement(self):

        # Apply Barriers to the interval of Qubits, representing the Vertices of the Graph
        self.quantum_circuit.apply_barriers_interval(self.qubits_vertices_indexes)

        # For each Qubit, representing the Vertex of the Graph
        for qubit_vertex_index in self.qubits_vertices_indexes:

            # Apply the Hadamard Gate to the current Qubit, representing a vertex
            self.quantum_circuit.apply_hadamard(qubit_vertex_index)

        # Apply Barriers to the interval of Qubits, representing the Vertices of the Graph
        self.quantum_circuit.apply_barriers_interval(self.qubits_vertices_indexes)

        # For each pair of Qubits, representing an Edge of the Graph
        for qubits_edges_pair_indexes in self.qubits_edges_indexes:

            # Apply the Controlled-Z Gate to the two Qubits, representing the current Edge of the Graph
            self.quantum_circuit.apply_controlled_z(self.qubits_vertices_indexes[qubits_edges_pair_indexes[0]],
                                                    self.qubits_vertices_indexes[qubits_edges_pair_indexes[1]])

        # Apply Barriers to the interval of Qubits, representing the Vertices of the Graph
        self.quantum_circuit.apply_barriers_interval(self.qubits_vertices_indexes)

        # Return the IBM Qiskit's Graph State (Resource State) State, as a multipartite entanglement
        return self.quantum_circuit

    # Measure the multipartite entanglement for the Graph State (Resource State) configured
    def measure_multipartite_entanglement(self, is_final_measurement=True):

        # Set the Bits, representing the Vertices of the Graph,
        # for the measurement of their respective Qubits
        bits_vertices_indexes = self.qubits_vertices_indexes

        # Apply Barriers to the interval of Qubits, representing the Vertices of the Graph
        self.quantum_circuit.apply_barriers_interval(self.qubits_vertices_indexes)

        # Duplicate the list of Qubits, representing the Vertices of the Graph
        qubits_vertices_indexes_reversed = self.qubits_vertices_indexes.copy()

        # Reverse the list of duplicated Qubits, representing the Vertices of the Graph
        qubits_vertices_indexes_reversed.reverse()

        # Duplicate the list of Qubits, representing the Edges of the Graph
        qubits_edges_indexes_reversed = self.qubits_edges_indexes.copy()

        # Reverse the list of duplicated Qubits, representing the Edges of the Graph
        qubits_edges_indexes_reversed.reverse()

        # For each pair of Qubits, in reversed order, representing an Edge of the Graph
        for qubits_edges_pair_indexes in self.qubits_edges_indexes:

            # Apply the Controlled-Z Gate to the two Qubits, representing the current Edge of the Graph
            self.quantum_circuit.apply_controlled_z(self.qubits_vertices_indexes[qubits_edges_pair_indexes[0]],
                                                    self.qubits_vertices_indexes[qubits_edges_pair_indexes[1]])

        # Apply Barriers to the interval of Qubits, representing the Vertices of the Graph
        self.quantum_circuit.apply_barriers_interval(self.qubits_vertices_indexes)

        # For each Qubit, in reversed order, representing the Vertex of the Graph
        for qubit_vertex_index_reversed in qubits_vertices_indexes_reversed:

            # Apply the Hadamard Gate to the current Qubit, representing a vertex
            self.quantum_circuit.apply_hadamard(qubit_vertex_index_reversed)

        # Apply Barriers to the interval of Qubits, representing the Vertices of the Graph
        self.quantum_circuit.apply_barriers_interval(self.qubits_vertices_indexes)

        # If is a final measurement
        if is_final_measurement:

            # Measure the Qubits, representing the vertices of the Graph, of the Quantum Circuit,
            # for the Graph State (Resource State)
            self.quantum_circuit.measure_qubits_interval(self.qubits_vertices_indexes,
                                                         bits_vertices_indexes)

        # Return the IBM Qiskit's Graph State (Resource State), as a multipartite entanglement
        return self.quantum_circuit
