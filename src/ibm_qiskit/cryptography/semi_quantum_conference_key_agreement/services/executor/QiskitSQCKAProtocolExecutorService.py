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

from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreement import QiskitSQCKAProtocol
from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreement.common import QiskitSQCKAProtocolParameters

from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreement.common.QiskitSQCKAProtocolParty import \
    QiskitSQCKAProtocolParty

from src.ibm_qiskit.cryptography.semi_quantum_conference_key_agreement\
    .common.QiskitSQCKAProtocolPreSharedKeyPair import \
    QiskitSQCKAProtocolPreSharedKeyPair


# Class for the Executor Service of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
class QiskitSQCKAProtocolExecutorService:

    # Constructor of the Executor Service of the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol
    def __init__(self):

        # The Object representing the Protocol itself
        self.qiskit_sqcka_protocol = None

        # The boolean flag for the initialisation status of the Protocol itself
        self.qiskit_sqcka_protocol_initialised = False

        # The Parties involved in the Protocol
        self.qiskit_sqcka_protocol_parties = None

        # The boolean flag for the initialisation of the Parties involved in the Protocol
        self.qiskit_sqcka_protocol_parties_initialised = False

        # The Master Party of the Protocol
        self.qiskit_sqcka_protocol_master_party = None

        # The boolean flag for the initialisation of the Master Party of the Protocol
        self.qiskit_sqcka_protocol_master_party_initialised = False

        # The Bipartite Pre-Shared Keys used between the Parties, involved in the Protocol
        self.qiskit_sqcka_protocol_bipartite_pre_shared_keys = []

        # The boolean flag for the initialisation of
        # the Bipartite Pre-Shared Keys used between the Parties, involved in the Protocol
        self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised = False

        # The Parameters of the Protocol
        self.qiskit_sqcka_protocol_parameters = None

        # The boolean flag for the initialisation of Parameters of the Protocol
        self.qiskit_sqcka_protocol_parameters_initialised = False

    # Set the Parties of the Protocol
    def set_protocol_parties(self, parties_names, master_party_name, bipartite_pre_shared_keys):

        # If the Bipartite Pre-Shared Keys were already be established
        if self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised:

            # Create the list of Parties' Names
            parties_names_lower = []

            # For each Party Name
            for party_name in parties_names:

                # Append the Party Name, in lowercase, to the list of Parties' Names
                parties_names_lower.append(party_name.lower())

            # Change the Party's Name, for the lowercase
            master_party_name_lower = master_party_name.lower()

            # If the Party Name, responsible for the distribution of the Common Secret Key (Conference Key),
            # is not present in the list of Parties' Names involved
            if master_party_name_lower not in parties_names_lower:

                # Raise the Value Error exception
                raise ValueError("The Party Name specified to be the Master "
                                 "(i.e., the party responsible for the distribution of the Common Secret Key "
                                 "(Conference Key) between the parties involved is not present in "
                                 "the list of Parties' Names involved on the Protocol!!!")

            # Retrieve the number of parties involved in the Protocol
            num_parties = len(parties_names_lower)

            # Redefine the list of the Parties involved in the Protocol, according to the number of them
            self.qiskit_sqcka_protocol_parties = [None] * num_parties

            # For each Party involved in the Protocol
            for current_party_id in range(num_parties):

                # Retrieve the name of the current Party
                current_party_name = parties_names_lower[current_party_id]

                # If the current Party is the Master Party
                if current_party_name.lower() == master_party_name_lower.lower():

                    # Initialize the object of the Party, as the Master Party
                    # noinspection PyTypeChecker
                    self.qiskit_sqcka_protocol_parties[current_party_id] = \
                        QiskitSQCKAProtocolParty(current_party_id, current_party_name.lower(),
                                                 True, bipartite_pre_shared_keys)

                    self.set_protocol_master_party(self.qiskit_sqcka_protocol_parties[current_party_id])

                # If the current Party is not the Master Party
                else:

                    # Initialise the bipartite Pre-Shared Key
                    bipartite_pre_shared_key = None

                    # For each bipartite Pre-Shared Key
                    for current_bipartite_pre_shared_key in range(len(bipartite_pre_shared_keys)):

                        # Retrieve the current bipartite Pre-Shared Key
                        bipartite_pre_shared_key = bipartite_pre_shared_keys[current_bipartite_pre_shared_key]

                        # If the current bipartite Pre-Shared Key is owned by the current Party
                        if bipartite_pre_shared_key.get_party_name_2() == current_party_name:

                            # The pretended bipartite Pre-Shared Key was found, so the loop can be broken
                            break

                    # Initialize the object of the Party, as a Normal Party
                    # noinspection PyTypeChecker
                    self.qiskit_sqcka_protocol_parties[current_party_id] = \
                        QiskitSQCKAProtocolParty(current_party_id, current_party_name.lower(),
                                                 False, bipartite_pre_shared_key)

            # Set the boolean flag for the initialisation of the Parties of the Protocol, as True
            self.qiskit_sqcka_protocol_parties_initialised = True

        # If the Bipartite Pre-Shared Keys were not established yet
        else:

            # Raise a Value Error
            raise ValueError("The Bipartite Pre-Shared Keys were not established yet!!!")

    # Return the Parties of the Protocol
    def get_protocol_parties(self):

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # list of Parties were already initialised
        if self.qiskit_sqcka_protocol_parties_initialised:

            # Return the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's list of Parties
            return self.qiskit_sqcka_protocol_parties

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # list of Parties were not initialised yet
        else:

            # Return none
            return None

    # Set the Master Party of the Protocol
    def set_protocol_master_party(self, master_party):

        # The Master Party of the Protocol
        self.qiskit_sqcka_protocol_master_party = master_party

        # Set the boolean flag for the initialisation of the Master Party of the Protocol, as True
        self.qiskit_sqcka_protocol_master_party_initialised = True

    # Return the Master Party of the Protocol
    def get_protocol_master_party(self):

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Master Party were already initialised
        if self.qiskit_sqcka_protocol_master_party_initialised:

            # Return the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Master Party
            return self.qiskit_sqcka_protocol_master_party

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Master Party were not initialised yet
        else:

            # Return none
            return None

    # Set the Bipartite Pre-Shared Keys, as initialised
    def set_protocol_bipartite_pre_shared_keys_initialised(self):

        # If there are already fulfilled all the Bipartite Pre-Shared Keys,
        # it is possible to set the boolean flag as True
        if len(self.qiskit_sqcka_protocol_bipartite_pre_shared_keys) == \
                (self.qiskit_sqcka_protocol_parameters.get_num_parties() - 1):

            # Set the boolean flag for the initialisation of
            # the Bipartite Pre-Shared Keys used between the Parties, involved in the Protocol, as True
            self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised = True

        # If it is not possible to set the boolean flag as True, because of missing Bipartite Pre-Shared Keys,
        # or even, to more Bipartite Pre-Shared Keys configured than the allowed number of them
        else:

            # Raise Value Error
            raise ValueError("There are less or more Bipartite Pre-Shared Keys specified to "
                             "be configured in the Protocol!!!")

    # Add a Bipartite Pre-Shared Key to the Protocol
    def add_protocol_bipartite_pre_shared_key(self, user_client_1, user_client_2,
                                              bipartite_pre_shared_key_binary_string):

        # If the Parameters of the Protocol were already configured
        if self.qiskit_sqcka_protocol_parameters_initialised:

            # If it is possible to add one more Bipartite Pre-Shared Key
            if len(self.qiskit_sqcka_protocol_bipartite_pre_shared_keys) < \
                    (self.qiskit_sqcka_protocol_parameters.get_num_parties() - 1):

                # Create a Bipartite Pre-Shared Key object
                qiskit_sqcka_protocol_bipartite_pre_shared_key = \
                    QiskitSQCKAProtocolPreSharedKeyPair(user_client_1, user_client_2,
                                                        bipartite_pre_shared_key_binary_string)

                # Add the previously created Bipartite Pre-Shared Key object to
                # the list of the Bipartite Pre-Shared Keys
                self.qiskit_sqcka_protocol_bipartite_pre_shared_keys\
                    .append(qiskit_sqcka_protocol_bipartite_pre_shared_key)

            # If it is not possible to add one more Bipartite Pre-Shared Key
            else:

                # Raise a Value Error
                raise ValueError("It is only possible to add {} Bipartite Pre-Shared Keys to the Protocol!!!"
                                 .format((self.qiskit_sqcka_protocol_parameters.get_num_parties() - 1)))

        # If the Parameters of the Protocol were not configured yet
        else:

            # Raise a Value Error
            raise ValueError("The Parameters of the Protocol need to "
                             "be configured before add any Bipartite Pre-Shared Key!!!")

    # Return all the Bipartite Pre-Shared Key of the Protocol
    def get_protocol_bipartite_pre_shared_keys(self):

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Bipartite Pre-Shared Keys were already initialised
        if self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised:

            # Return the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
            # Bipartite Pre-Shared Keys
            return self.qiskit_sqcka_protocol_bipartite_pre_shared_keys

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Bipartite Pre-Shared Keys were not initialised yet
        else:

            # Return none
            return None

    # Configure the Parameters of the Protocol
    def configure_protocol_parameters(self, num_parties, num_rounds, num_quantum_communication_channels,
                                      preparing_bases, quantum_entanglement_type):

        # Initialise the Parameters of the Protocol
        self.qiskit_sqcka_protocol_parameters = \
            QiskitSQCKAProtocolParameters\
            .QiskitSQCKAProtocolParameters(num_parties, num_rounds, num_quantum_communication_channels,
                                           preparing_bases, quantum_entanglement_type)

        # Set the boolean flag for the initialisation of Parameters of the Protocol, as True
        self.qiskit_sqcka_protocol_parameters_initialised = True

    # Return the Parameters of the Protocol
    def get_protocol_parameters(self):

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Parameters were already initialised
        if self.qiskit_sqcka_protocol_parameters_initialised:

            # Return the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's Parameters
            return self.qiskit_sqcka_protocol_parameters

        # If the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol's
        # Parameters were not initialised yet
        else:

            # Return none
            return None

    # Initialise the Protocol, as its initial version, ready to be executed
    def initialise_protocol(self):

        # If the Protocol itself was not initialised yet
        if self.qiskit_sqcka_protocol_initialised is not True:

            # Create a boolean flag to check if it is possible to initialise the Protocol
            protocol_initialisation_flag = self.qiskit_sqcka_protocol_parameters_initialised \
                                           and self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised \
                                           and self.qiskit_sqcka_protocol_parties_initialised \
                                           and self.qiskit_sqcka_protocol_master_party_initialised

            # If all the conditions for the initialisation of the Protocol are verified
            if protocol_initialisation_flag:

                # Retrieve the Parties' objects involved in the Protocol
                parties = self.get_protocol_parties()

                # Retrieve the Master Party's objects involved in the Protocol
                master_party = self.get_protocol_master_party()

                # Retrieve the Bipartite Pre-Shared Keys involved in the Protocol
                bipartite_pre_shared_keys = self.get_protocol_bipartite_pre_shared_keys()

                # Retrieve the Parameters' configuration of the Protocol
                parameters = self.get_protocol_parameters()

                # Set the final object for the IBM Qiskit's Semi-Quantum Conference Key Agreement (SQCKA) Protocol,
                # given its respective arguments
                self.qiskit_sqcka_protocol = QiskitSQCKAProtocol\
                    .QiskitSQCKAProtocol(parties, master_party, bipartite_pre_shared_keys, parameters)

                # Delete obsolete attributes of the Class
                self.delete_obsolete_attributes()

                # Set the Protocol itself as being initialised,
                # putting the respective boolean flag as True
                self.qiskit_sqcka_protocol_initialised = True

            # If some condition for the initialisation of the Protocol is not verified
            else:

                # Raise the Value Error
                raise ValueError("Some configurations of the Protocol are not set yet!!!")

        # If the Protocol itself was already initialised yet
        else:

            # Raise a Value Error
            raise ValueError("The Protocol was already initialised!!!")

    # Delete obsolete attributes of the Class, after the Protocol be initialised
    def delete_obsolete_attributes(self):

        # Delete/Free the Parties involved in the Protocol
        del self.qiskit_sqcka_protocol_parties

        # Delete/Free the boolean flag for the initialisation of the Parties involved in the Protocol
        del self.qiskit_sqcka_protocol_parties_initialised

        # Delete/Free the Master Party of the Protocol
        del self.qiskit_sqcka_protocol_master_party

        # Delete/Free the boolean flag for the initialisation of the Master Party of the Protocol
        del self.qiskit_sqcka_protocol_master_party_initialised

        # Delete/Free the Bipartite Pre-Shared Keys used between the Parties, involved in the Protocol
        del self.qiskit_sqcka_protocol_bipartite_pre_shared_keys

        # Delete/Free the boolean flag for the initialisation of
        # the Bipartite Pre-Shared Keys used between the Parties, involved in the Protocol
        del self.qiskit_sqcka_protocol_bipartite_pre_shared_keys_initialised

        # Delete/Free the Parameters of the Protocol
        del self.qiskit_sqcka_protocol_parameters

        # Delete/Free the boolean flag for the initialisation of Parameters of the Protocol
        del self.qiskit_sqcka_protocol_parameters_initialised
