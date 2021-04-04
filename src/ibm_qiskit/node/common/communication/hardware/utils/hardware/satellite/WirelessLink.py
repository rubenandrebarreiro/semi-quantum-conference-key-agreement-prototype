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


# Class of the Wireless Link
class WirelessLink:

    # Constructor of the Wireless Link
    def __init__(self, wireless_link_id, wireless_link_distance_kms):

        # Initialise the ID of the Wireless Link
        self.wireless_link_id = wireless_link_id

        # Initialise the Distance (in kilometers) of the Wireless Link
        self.wireless_link_distance_kms = wireless_link_distance_kms

        # Initialise the Boolean Flag to keep the information about
        # the Wireless Link is configured or not
        self.wireless_link_configured = False

    # Return the ID of the Wireless Link
    def get_wireless_link_id(self):
        return self.wireless_link_id

    # Return the Distance (in kilometers) of the Wireless Link
    def get_wireless_link_distance_kms(self):
        return self.wireless_link_distance_kms

    # Return the Boolean Flag to keep the information about
    # the Wireless Link is configured or not
    def is_wireless_link_configured(self):
        return self.wireless_link_configured

    # Configure the Wireless Link, by setting
    # the value for the Boolean Flag to keep the information about
    # the Wireless Link is configured or not, as True
    def configure_wireless_link(self):

        # If the Wireless Link is not currently configured,
        # it is possible to configure this Wireless Link
        if not self.is_wireless_link_configured():

            # Set the Boolean Flag to keep the information about
            # the Wireless Link is configured or not, as True
            self.wireless_link_configured = True

        # If the Wireless Link is already configured,
        # it is not possible to configure this Wireless Link again
        else:

            # Raise a Valuer Error
            raise ValueError("The Wireless Link is already configured, "
                             "thus, it is not possible to configure it again!!!")

    # Unconfigure the Wireless Link, by setting
    # the value for the Boolean Flag to keep the information about
    # the Wireless Link is installed or not, as False
    def unconfigure_wireless_link(self):

        # If the Wireless Link is already configured,
        # it is possible to unconfigure this Wireless Link
        if self.is_wireless_link_configured():

            # Set the Boolean Flag to keep the information about
            # the Wireless Link is configured or not, as False
            self.wireless_link_configured = False

        # If the Wireless Link is not currently configured,
        # it is not possible to unconfigure this Wireless Link again
        else:

            # Raise a Valuer Error
            raise ValueError("The Wireless Link is already configured, "
                             "thus, it is not possible to configure it again!!!")
