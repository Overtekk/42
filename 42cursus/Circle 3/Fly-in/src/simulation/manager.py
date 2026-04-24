# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  manager.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 07:50:25 by roandrie        #+#    #+#               #
#  Updated: 2026/04/02 12:26:55 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Simulation orchestrator module.

This module houses the Manager class, the central controller that ties together
map configuration, pathfinding, object instantiation (zones and drones),
graphical rendering, and the step-by-step turn execution logic of the
simulation.
"""

import re
import arcade
import argparse

from typing import Dict, List, Optional, Tuple

from src.utils.ui import Colors, Display
from src.maps_parser.parser import MapModel
from src.object.drones import Drone
from src.object.zone import Zone
from src.object.utils.type import ZoneType
from src.simulation.pathfinding import PathFinding
from src.simulation.output import LogOutput
from src.graphics.renderer import Renderer


class Manager():
    """
    Central controller orchestrating the drone routing simulation.

    The Manager is responsible for interpreting the parsed map data,
    instantiating the physical Zone and Drone objects, initializing the
    pathfinding weight map, managing the graphical renderer, and executing
    the core logical loop (turn resolution) until all drones reach the goal.

    Attributes:
        raw_nb_drones (int): The total number of drones to simulate.
        raw_start_hub (str): Raw configuration string for the starting zone.
        raw_end_hub (str): Raw configuration string for the destination zone.
        raw_hubs (List[str]): Raw configuration strings for intermediate zones.
        raw_connections (List[str]): Raw configuration strings for zone links.
        connection_map (Dict[str, List[str]]): Processed adjacency list of
                                              connections.
        args (List[str]): Command-line arguments passed to the program.
        map_name (str): The name of the currently loaded map file.
        running (bool): State flag indicating if the simulation is active.
        turns (int): The current turn counter.
        log_turn (List[str]): Temporary storage for movement logs in the
                              current turn.
        log_output (Dict[int, List[str]]): Master dictionary holding all turn
                                          logs.
        line (int): Line counter for the output log file.
        drones (Dict[int, Drone]): Instantiated Drone objects mapped by ID.
        zones (Dict[str, Zone]): Instantiated Zone objects mapped by name.
        start_name (str): The parsed name of the starting zone.
        end_name (str): The parsed name of the destination zone.
    """

    def __init__(self, map_config: MapModel,
                 connection_map: Dict[str, List[str]],
                 args: argparse.Namespace, map_name: str) -> None:
        """
        Initializes the simulation manager with the parsed map data.

        Args:
            map_config (MapModel): The validated Pydantic model containing map
                                   data.
            connection_map (Dict[str, List[str]]): The parsed adjacency list.
            args (List[str]): The parsed command-line arguments.
            map_name (str): The name of the map file being used.
        """
        # Init from map_config
        self.raw_nb_drones = map_config.nb_drones
        self.raw_start_hub = map_config.start_hub
        self.raw_end_hub = map_config.end_hub
        self.raw_hubs = map_config.hub
        self.raw_connections = map_config.connection

        self.connection_map = connection_map
        self.args = args
        self.map_name = map_name

        self.running = False
        self.turns = 0

        self.log_turn: List[str] = []
        self.log_output: Dict[int, List[str]] = {}
        self.line = 0

        # Init Object
        self.drones: Dict[int, Drone] = {}
        self.zones: Dict[str, Zone] = {}
        self.link_capacities: Dict[Tuple[str, str], int] = {}
        self.start_name: str | None = None
        self.end_name: str | None = None

        self._create_drones()
        self._create_zone(self.connection_map)
        self._parse_link_metadata()

    def run(self) -> None:
        """
        Starts the simulation lifecycle.

        Places drones at the spawn point, triggers the calculation of the
        pathfinding distance field across all zones, and launches the graphical
        Arcade rendering window.
        """
        print(f"{Colors.LIGHT_CYAN}=== Starting Simulation ==={Colors.END}\n")

        self._add_drones_to_spawn()
        path = PathFinding(self.connection_map, self.zones)

        if self.end_name:
            path.find_path(self.end_name)
        else:
            Display.error("Error in pathfinding. Can't find end zone.")
            return

        self._init_renderer()

    def simulate_one_turn(self) -> None:
        """
        Executes the logical calculations for a single simulation turn.

        This is the core engine of the program. It sorts drones based on their
        distance to the goal, evaluates available neighboring zones, checks
        capacity constraints, resolves movement intents (including multi-turn
        restricted movements), updates physical locations, and records the
        actions to the output logger. Automatically stops the simulation when
        the victory condition is met.
        """
        self.running = True
        self.turns += 1

        self.line += 1
        self.log_turn.clear()

        current_link_usage: Dict[Tuple[str, str], int] = {}

        sorted_drone_list = sorted(
            self.drones.values(), key=self._get_drone_weight
        )

        for drone in sorted_drone_list:
            flag_moving = False
            zone_to_move: Optional[Zone] = None
            neighbors_list: List[Zone] = []

            # Skip turn if drone have finish
            if drone.finish:
                continue

            loc = drone.get_location()
            if drone.is_moving and loc:
                loc_splitted = loc.split("-")
                zone_to_move = self.zones[loc_splitted[1]]
                flag_moving = True
                drone.is_moving = False

            if not flag_moving and loc:
                # Check neighbors zone of the drone location and add it to list
                for neighbors in self.zones[loc].get_next_zones():
                    # Skip if zone is blocked
                    if (self.zones[neighbors].metadata_zone_type
                            == ZoneType.BLOCKED):
                        continue
                    # Skip if zone is already visited by the drone
                    if self.zones[neighbors] in drone.visited_zones:
                        continue
                    # Skip if next have have bigger weight
                    if (self.zones[neighbors].weight < self.zones[loc].weight
                            or (self.zones[neighbors].weight ==
                                self.zones[loc].weight
                                and not self.zones[neighbors].is_occuped())):
                        neighbors_list.append(self.zones[neighbors])

                # Sort the list based on the weight of a zone
                sorted_neighbors = sorted(
                    neighbors_list,
                    key=lambda x: x.weight + (x.get_nb_drones() * 1.5)
                    )

                # Check if a zone have the capacity to acquiere the drone
                for zone in sorted_neighbors:
                    link_key = (min(loc, zone.name), max(loc, zone.name))
                    link_count = current_link_usage.get(link_key, 0)
                    link_max = self.link_capacities.get(link_key, 1)

                    if not zone.is_occuped() and link_count < link_max:
                        zone_to_move = zone
                        current_link_usage[link_key] = link_count + 1

                        if (zone_to_move.metadata_zone_type
                                == ZoneType.RESTRICTED):
                            drone.is_moving = True
                        break

                # Pass if no available zone has been found
                if zone_to_move is None:
                    continue

                # Reserved a slot of the upcoming drone
                zone_to_move.reserved_slot += 1

                # Move the drone to a connection
                if drone.is_moving:
                    for conn_name in zone_to_move.connection:
                        if conn_name == self.zones[loc].name:
                            self.zones[loc].remove_drone(drone)
                            drone.update_connection(conn_name, zone_to_move)
                            (self._save_move_in_log(
                                drone, zone_to_move, conn_name
                            ))
                            break
                    continue

            # Update drone location
            if not flag_moving:
                curr_loc = drone.get_location()
                if curr_loc:
                    self.zones[curr_loc].remove_drone(drone)

            if zone_to_move:
                drone.update_location(zone_to_move)
                drone.visited_zones.append(zone_to_move)
                zone_to_move.add_drone(drone)
                zone_to_move.reserved_slot -= 1

                # Add the move to the log list
                self._save_move_in_log(drone, zone_to_move)

        # Store the line once the turn is finished
        if len(self.log_turn) > 0:
            if self.args.show_more_logs:
                if self.end_name:
                    remain = self.zones[self.end_name].drones_on_it
                    log = ("\nDrones remaining: "
                           f"{self.raw_nb_drones - len(remain)}")
                self.log_turn.append(log)

            line_log = self.log_turn.copy()
            self.log_output[self.line] = line_log

            if self.args.show_logs or self.args.show_more_logs:
                print(f"{Colors.CYAN}Turn: {self.turns}{Colors.END}")
                print(self._print_log())

        # Stop the simulation if all drones are on the exit
        if (self.end_name and self.zones[self.end_name]
                .check_if_goal_full(self.raw_nb_drones)):
            self.running = False
            print(f"{Colors.BLUE}All drones have reached {self.end_name}"
                  f"{Colors.END}")
            output_manager = LogOutput(self.map_name, self.log_output)
            output_manager.write_log()

    def get_map_information(self) -> str:
        """
        Formats the raw map configuration into a readable string for debugging.

        Returns:
            str: A multi-line, color-formatted string detailing the map's
                 spawns, hubs, and connections.
        """
        # Variable to short strings.
        LB = f"{Colors.LIGHT_BLUE}{Colors.BOLD}"
        EB = f"{Colors.END}{Colors.LIGHT_BLUE}"

        map_info = f"{LB}\n=======Informations======\n\n{Colors.END}"
        map_info += (f"{LB}Number of drones:{EB} {self.raw_nb_drones}"
                     f"\n\n{Colors.END}")
        map_info += f"{LB}Start hub:{EB} {self.raw_start_hub}\n{Colors.END}"
        map_info += f"{LB}End hub:{EB} {self.raw_end_hub}\n\n{Colors.END}"
        map_info += f"{LB}List of hubs:\n{Colors.END}"
        for hub in self.raw_hubs:
            map_info += f"{Colors.LIGHT_BLUE}- {hub}\n"
        map_info += f"{LB}\nList of connections:\n{Colors.END}"
        for connection in self.raw_connections:
            map_info += f"{Colors.LIGHT_BLUE}- {connection}\n"
        map_info += f"{Colors.END}"

        return map_info

    def _get_drone_weight(self, drone: Drone) -> Tuple[float, float]:
        """
        Calculates the sorting priority of a drone for turn resolution.

        Drones closer to the goal (lower weight) are processed first to clear
        paths for those behind them.

        Args:
            drone (Drone): The drone to evaluate.

        Returns:
            Tuple[float, float]: A tuple containing the primary pathfinding
                                 weight and the secondary congestion weight.
        """
        location = drone.get_location()

        if location and "-" in location:
            split_location = location.split("-")
            return (self.zones[split_location[1]].weight,
                    float(self._get_drone_waiting(drone)))

        if location:
            return (self.zones[location].weight,
                    float(self._get_drone_waiting(drone)))

        return (0.0, 0.0)

    def _get_drone_waiting(self, drone: Drone) -> float:
        """
        Calculates the local congestion at the drone's target location.

        Args:
            drone (Drone): The drone whose destination congestion is being
                           evaluated.

        Returns:
            float: The number of drones currently occupying or arriving at the
                  target.
        """
        location = drone.get_location()

        if location and "-" in location:
            split_location = location.split("-")
            return float(self.zones[split_location[1]].get_nb_drones())

        if location:
            return float(self.zones[location].get_nb_drones())

        return 0.0

    def _save_move_in_log(self, drone_id: Drone, destination: Zone,
                          connection: Optional[str] = None) -> None:
        """
        Formats and records a drone's movement string into the turn log buffer.

        Args:
            drone_id (Drone): The drone that just moved.
            destination (Zone): The final physical zone the drone arrived at.
            connection (Zone, optional): The name of the connection string if
                                         the drone is mid-transit. Defaults to
                                         None.
        """
        if self.args.show_more_logs:
            if connection:
                log = f"{drone_id.id}-{connection}-{destination.name}"
            else:
                if destination.name == self.end_name:
                    log = f"{drone_id.id}-{destination.name}"
                else:
                    log = (f"{drone_id.id}-{destination.name} "
                           f"({len(destination.drones_on_it)}/"
                           f"{destination.metadata_max_drones})")
        else:
            if connection:
                log = f"{drone_id.id}-{connection}-{destination.name}"
            else:
                log = f"{drone_id.id}-{destination.name}"
        self.log_turn.append(log)

    def _print_log(self) -> str:
        """
        Concatenates the current turn's log buffer into a single string.

        Returns:
            str: The concatenated log string for the turn.
        """
        text_log = ""
        for item in self.log_turn:
            text_log += f"{item} "

        return text_log

    def _init_renderer(self) -> None:
        """
        Initializes the Arcade window and starts the graphical loop.

        Catches errors related to missing graphical assets and ensures the
        application exits gracefully if rendering fails.
        """
        try:
            Renderer(self.zones, self, self.drones, self.connection_map)
            arcade.run()
        except (OSError, FileNotFoundError) as e:
            Display.error(str(e))
            arcade.exit()
            return
        # except Exception as e:
        #     Display.error(e)
        #     arcade.exit()
        #     return 1

    def _create_drones(self) -> None:
        """
        Instantiates the required number of Drone objects based on map
        configuration.
        """
        for i in range(1, self.raw_nb_drones + 1):
            self.drones[i] = Drone(i)

    def _create_zone(self, connection_map: Dict[str, List[str]]) -> None:
        """
        Instantiates all Zone objects and populates the internal zones
        dictionary.

        Args:
            connection_map (Dict[str, List[str]]): The map's adjacency list.
        """
        # Start
        value = re.findall(r"\[[^\]]*\]|\S+", self.raw_start_hub)
        self.start_name = value[0]
        self._add_to_zone(value, connection_map.get(value[0], []), "start")

        # End
        value = re.findall(r"\[[^\]]*\]|\S+", self.raw_end_hub)
        self.end_name = value[0]
        self._add_to_zone(value, connection_map.get(value[0], []), "end")

        # Hubs
        for hubs in self.raw_hubs:
            value = re.findall(r"\[[^\]]*\]|\S+", hubs)
            self._add_to_zone(value, connection_map.get(value[0], []), "hub")

    def _add_to_zone(self, value: List[str], connection: List[str],
                     zone_type: str) -> None:
        """
        Helper method to parse zone strings and create a Zone instance.

        Args:
            value (List[str]): Split list containing zone properties.
            connection (List[str]): List of neighbor zone names.
            type (str): The functional type of the zone
                        (e.g., 'start', 'end', or None).
        """
        type_param = zone_type if zone_type in ["start", "end"] else "hub"

        if len(value) == 4:
            self.zones[value[0]] = Zone(value[0], int(value[1]), int(value[2]),
                                        value[3], connection, type_param)
        else:
            self.zones[value[0]] = Zone(value[0], int(value[1]), int(value[2]),
                                        None, connection, type_param)

    def _parse_link_metadata(self) -> None:
        """
        Parses raw connection strings to extract maximum link capacities.

        Iterates through the raw connection data, identifies the linked zones,
        and extracts the 'max_link_capacity' metadata. If no capacity is
        specified, it defaults to 1. Links are stored as sorted tuples to
        ensure bidirectional consistency.
        """
        for raw_connection in self.raw_connections:
            parts = re.findall(r"\[[^\]]*\]|\S+", raw_connection)
            zones = parts[0].split("-")

            sorted_keys = sorted((zones[0], zones[1]))
            link_key = (sorted_keys[0], sorted_keys[1])

            capacity = 1
            if len(parts) > 1:
                meta = parts[1].strip("[]")
                if "max_link_capacity=" in meta:
                    capacity = int(meta.split("=")[1])

            self.link_capacities[link_key] = capacity

    def _add_drones_to_spawn(self) -> None:
        """
        Places all instantiated drones into the designated starting zone.
        """
        if self.start_name:
            for drone in self.drones.values():
                self.zones[self.start_name].add_drone(drone)
                drone.update_location(self.zones[self.start_name])
                drone.visited_zones.append(self.zones[self.start_name])

    def _debug_get_data(self) -> None:
        """
        Development utility to print the state of all zones and drones.
        """
        for zone in self.zones.values():
            print(zone.get_zone_information())
        for drone in self.drones.values():
            print(drone.get_drone_information())

    def _debug_simulate_one_step(self) -> None:
        """
        Development utility to manually force a hardcoded single movement step.
        """
        self.turns += 1
        pos = self.drones[1].get_location()
        if pos:
            next_zone = self.connection_map[pos][0]
            self.drones[1].update_location(self.zones[next_zone])
            self.zones[pos].remove_drone(self.drones[1])
            self.zones[next_zone].add_drone(self.drones[1])
