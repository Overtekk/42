# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  zone.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 13:43:53 by roandrie        #+#    #+#               #
#  Updated: 2026/03/24 13:55:33 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Zone representation module.

This module defines the Zone class, representing individual nodes (hubs)
within the drone simulation network. It manages coordinates, capacities,
metadata parsing, and the tracking of drones currently occupying or
reserving space in the zone.
"""

from typing import List

from src.utils.ui import Colors
from src.object.utils.type import ZoneType
from src.object.drones import Drone


class Zone():
    """
    Logical representation of a node within the simulation grid.

    A Zone handles its spatial coordinates, connection links to other zones,
    and capacity constraints based on its parsed metadata. It also tracks
    which drones are currently present or incoming (reserved slots) to
    facilitate pathfinding and collision avoidance.

    Attributes:
        name (str): The unique identifier name of the zone.
        x (int): The X coordinate on the logical grid.
        y (int): The Y coordinate on the logical grid.
        connection (List[str]): A list of zone names directly connected to this
                                one.
        is_start (bool): Flag indicating if this zone is the initial spawn
                         point.
        is_end (bool): Flag indicating if this zone is the final destination.
        metadata_color (str): The CSS color name assigned to the zone.
        metadata_zone_type (ZoneType): The specific behavioral type of the
                                       zone.
        metadata_max_drones (int): The maximum number of drones allowed
                                   simultaneously.
        weight (int): Pathfinding cost associated with entering this zone.
        drones_on_it (List[Drone]): A list of drone objects currently located
                                    here.
        reserved_slot (int): The number of drones currently routing towards
                             this zone.
    """

    def __init__(self, name: str, x: int, y: int,
                 metadatata: str | None, connection: List[str],
                 type: str) -> None:
        """
        Initializes a new Zone instance.

        Args:
            name (str): The unique name of the zone.
            x (int): The horizontal coordinate.
            y (int): The vertical coordinate.
            metadata (str | None): Raw metadata string
                                   (e.g., '[color=red zone=blocked]').
            connection (List[str]): List of neighbor zone names.
            type (str): The structural type ('start', 'end', or None for
                        default hubs).
        """
        self.name = name
        self.x = x
        self.y = y
        raw_metadatata = metadatata
        self.connection = connection

        self.is_start = False
        self.is_end = False
        match type:
            case "start":
                self.is_start = True
            case "end":
                self.is_end = True

        # Default value
        self.metadata_color = "white"
        self.metadata_zone_type = ZoneType.NORMAL
        self.metadata_max_drones = 1
        if raw_metadatata is not None:
            self._write_metadata(raw_metadatata)

        # Weight of a visited zone used by the algorithm
        self.weight = 0.0

        # List of drones on the zone
        self.drones_on_it: List[Drone] = []
        self.reserved_slot = 0

    def is_occuped(self) -> bool:
        """
        Evaluates if the zone has reached its maximum drone capacity.

        End zones have infinite capacity. For all other zones, this considers
        both the drones currently on the zone and the drones that have
        reserved a slot to move there in the current turn.

        Returns:
            bool: True if the zone is full and cannot accept more drones,
                  False otherwise.
        """
        if self.is_end:
            return False

        if ((len(self.drones_on_it) + self.reserved_slot)
                >= self.metadata_max_drones):
            return True

        return False

    def get_next_zones(self) -> List[str]:
        """
        Retrieves the names of all connected neighboring zones.

        Returns:
            List[str]: A list of connected zone names.
        """
        return self.connection

    def get_nb_drones(self) -> int:
        """
        Calculates the total congestion level of the zone.

        End zones always return a congestion of 0. For standard zones, it
        returns the sum of physically present drones and incoming reserved
        drones.

        Returns:
            int: The total number of current and expected drones.
        """
        if self.is_end:
            return 0
        return len(self.drones_on_it) + self.reserved_slot

    def add_drone(self, drone_id: Drone) -> None:
        """
        Registers a drone as physically present on this zone.

        Args:
            drone_id (Drone): The drone object arriving at the zone.
        """
        self.drones_on_it.append(drone_id)

    def remove_drone(self, drone_id: Drone) -> None:
        """
        Unregisters a drone from this zone upon its departure.

        Args:
            drone_id (Drone): The drone object leaving the zone.
        """
        self.drones_on_it.remove(drone_id)

    def check_if_goal_full(self, nb_drones: int) -> bool:
        """
        Verifies if all simulation drones have successfully reached this zone.

        Args:
            nb_drones (int): The total number of drones spawned in the
                             simulation.

        Returns:
            bool: True if the current drone count matches the total simulation
                  count.
        """
        if len(self.drones_on_it) == nb_drones:
            return True
        return False

    def get_zone_information(self) -> str:
        """
        Formats the zone's internal state into a readable string for debugging.

        Returns:
            str: A multi-line, color-formatted string detailing coordinates,
                 metadata, connections, and occupying drones.
        """
        # Variable to short strings.
        LB = f"{Colors.LIGHT_BLUE}{Colors.BOLD}"
        EB = f"{Colors.END}{Colors.LIGHT_BLUE}"

        zone_info = f"{LB}\n=======Informations======\n\n{Colors.END}"
        zone_info += f"{LB}Zone name:{EB} {self.name}\n{Colors.END}"
        zone_info += f"{LB}Coordinates:{EB} x={self.x} y={self.y}{Colors.END}"
        zone_info += f"\n{LB}metadatata:\n{Colors.END}"
        zone_info += (f"{LB}- Color: {Colors.END}{Colors.LIGHT_BLUE}"
                      f"{self.metadata_color}\n")
        zone_info += (f"{LB}- Zone Type: {Colors.END}{Colors.LIGHT_BLUE}"
                      f"{self.metadata_zone_type}\n")
        zone_info += (f"{LB}- Max Drones: {Colors.END}{Colors.LIGHT_BLUE}"
                      f"{self.metadata_max_drones}\n\n")
        zone_info += f"{LB}Connection to:{EB} {self.connection}\n{Colors.END}"
        zone_info += f"{LB}Drones on zone:{EB} {self.drones_on_it}{Colors.END}"

        return zone_info

    def _write_metadata(self, raw_metadata: str) -> None:
        """
        Parses the raw metadata string to populate the zone's attributes.

        Strips brackets and splits the raw string into key-value pairs to set
        the color, zone type, and maximum drone capacity.

        Args:
            raw_metadata (str): The raw metadata string extracted from the map
                                file.
        """
        cleaned_metadata = raw_metadata.strip("[").strip("]")
        splitted_metadata = cleaned_metadata.split()

        for data in splitted_metadata:
            key, value = data.split("=")

            match key:
                case "color":
                    self.metadata_color = value

                case "zone":
                    match value:
                        case "normal":
                            self.metadata_zone_type = ZoneType.NORMAL
                        case "blocked":
                            self.metadata_zone_type = ZoneType.BLOCKED
                        case "priority":
                            self.metadata_zone_type = ZoneType.PRIORITY
                        case "restricted":
                            self.metadata_zone_type = ZoneType.RESTRICTED

                case "max_drones":
                    self.metadata_max_drones = int(value)
