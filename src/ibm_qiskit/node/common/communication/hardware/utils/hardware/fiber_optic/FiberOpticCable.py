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


# Class of the Fiber Optic Cable
class FiberOpticCable:

    # Constructor of the Fiber Optic Cable
    def __init__(self, fiber_optic_cable_id, fiber_optic_cable_distance_kms):

        # Initialise the ID of the Fiber Optic Cable
        self.fiber_optic_cable_id = fiber_optic_cable_id

        # Initialise the Distance (in kilometers) of the Fiber Optic Cable
        self.fiber_optic_cable_distance_kms = fiber_optic_cable_distance_kms

        # Initialise the Boolean Flag to keep the information about
        # the Fiber Optic Cable is installed or not
        self.fiber_optic_cable_installed = False

    # Return the ID of the Fiber Optic Cable
    def get_fiber_optic_cable_id(self):
        return self.fiber_optic_cable_id

    # Return the Distance (in kilometers) of the Fiber Optic Cable
    def get_fiber_optic_cable_distance_kms(self):
        return self.fiber_optic_cable_distance_kms

    # Return the Boolean Flag to keep the information about
    # the Fiber Optic Cable is installed or not
    def is_fiber_optic_cable_installed(self):
        return self.fiber_optic_cable_installed

    # Install the Fiber Optic Cable, by setting
    # the value for the Boolean Flag to keep the information about
    # the Fiber Optic Cable is installed or not
    def install_fiber_optic_cable(self):

        # If the Fiber Optic Cable is not currently installed,
        # it is possible to install this Fiber Optic Cable
        if not self.is_fiber_optic_cable_installed():

            # Set the Boolean Flag to keep the information about
            # the Fiber Optic Cable is installed or not, as True
            self.fiber_optic_cable_installed = True

        # If the Fiber Optic Cable is already installed,
        # it is not possible to install this Fiber Optic Cable again
        else:

            # Raise a Valuer Error
            raise ValueError("The Fiber Optic Cable is already installed, "
                             "thus, it is not possible to install it again!!!")

    # Uninstall the Fiber Optic Cable, by setting
    # the value for the Boolean Flag to keep the information about
    # the Fiber Optic Cable is installed or not
    def uninstall_fiber_optic_cable(self):

        # If the Fiber Optic Cable is already installed,
        # it is possible to uninstall this Fiber Optic Cable
        if self.is_fiber_optic_cable_installed():

            # Set the Boolean Flag to keep the information about
            # the Fiber Optic Cable is installed or not, as False
            self.fiber_optic_cable_installed = False

        # If the Fiber Optic Cable is not currently installed,
        # it is not possible to uninstall this Fiber Optic Cable again
        else:

            # Raise a Valuer Error
            raise ValueError("The Fiber Optic Cable is already installed, "
                             "thus, it is not possible to install it again!!!")
