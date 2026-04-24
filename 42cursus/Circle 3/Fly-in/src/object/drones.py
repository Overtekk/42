# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  drones.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 15:11:21 by roandrie        #+#    #+#               #
#  Updated: 2026/03/24 13:49:45 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Drone representation module.

This module defines the Drone class, which represents the autonomous vehicles
navigating through the zones. It manages their identity, current physical
location, movement state, tracking of visited zones to prevent loops, and
completion status.
"""

from typing import TYPE_CHECKING, List

from src.utils.ui import Colors

if TYPE_CHECKING:
    from src.object.zone import Zone


class Drone():
    """
    Logical representation of a single drone in the simulation.

    Attributes:
        id (str): The unique formatted identifier of the drone (e.g., 'D1').
        current_location (str | None): The name of the zone or connection where
                                       the drone is currently located.
        visited_zones (list): A history of zone names the drone has visited
                              to prevent backtracking or infinite loops.
        is_moving (bool): Flag indicating if the drone is currently traversing
                          a connection between two zones.
        finish (bool): Flag indicating if the drone has successfully reached
                       the final destination hub.
    """

    def __init__(self, id: int) -> None:
        """
        Initializes a new Drone instance.

        Args:
            id (int): The numerical identifier used to generate the drone's
                     unique string ID.
        """
        self.id = f"D{id}"
        self.current_location: str | None = None

        self.visited_zones: List[Zone] = []

        self.is_moving = False
        self.finish = False

    def __repr__(self) -> str:
        """
        Returns the ID of the Drone instead of its memory address.

        Returns:
            str: The formatted ID representation of the drone.
        """
        return f"Drone(id={self.id})"

    def update_location(self, zone: 'Zone') -> None:
        """
        Updates the drone's location to a specific zone.

        Also evaluates if the newly entered zone is the simulation's end hub,
        updating the drone's completion status accordingly.

        Args:
            zone (Zone): The target zone object the drone has entered.
        """
        self.current_location = zone.name
        if zone.is_end:
            self.finish = True

    def update_connection(self, old_zone: str, next_zone: 'Zone') -> None:
        """
        Updates the drone's location to represent traversal across a
        connection.

        Formats the current location as a transitional state
        (e.g., 'ZoneA-ZoneB') to indicate the drone is moving between two
        distinct hubs.

        Args:
            old_zone (str): The name of the zone the drone is departing from.
            next_zone (Zone): The target zone object the drone is moving
                              towards.
        """
        self.current_location = f"{old_zone}-{next_zone.name}"

    def get_location(self) -> str | None:
        """
        Retrieves the current location identifier of the drone.

        Returns:
            str: The name of the current zone or the formatted connection
                string.
        """
        return self.current_location

    def get_drone_information(self) -> str:
        """
        Formats the drone's internal state into a readable string for
        debugging.

        Returns:
            str: A multi-line, color-formatted string detailing the drone's ID
                 and its current location in the simulation.
        """
        # Variable to short strings.
        LB = f"{Colors.LIGHT_BLUE}{Colors.BOLD}"
        EB = f"{Colors.END}{Colors.LIGHT_BLUE}"

        drone_info = f"{LB}\n=======Informations======\n\n{Colors.END}"
        drone_info += f"{LB}Drone ID:{EB} {self.id}\n{Colors.END}"
        drone_info += (f"{LB}Drone location:{EB} {self.current_location}"
                       f"{Colors.END}")

        return drone_info
