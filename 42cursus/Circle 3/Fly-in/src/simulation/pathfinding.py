# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  pathfinding.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/07 22:15:21 by roandrie        #+#    #+#               #
#  Updated: 2026/04/01 21:35:22 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Pathfinding and distance field calculation module.

This module implements a Dijkstra-based algorithm that calculates a
distance field (or heat map) from the destination hub backwards to all
other reachable zones. This allows drones to navigate dynamically by
always choosing the neighboring zone with the lowest cost weight,
facilitating autonomous traffic management.
"""

import heapq

from typing import Any, Dict, List

from src.object.zone import Zone
from src.object.utils.type import ZoneType


class PathFinding():
    """
    Pathfinding manager to calculate movement weights across the map.

    Instead of calculating a single fixed path for one drone, this class
    evaluates the entire map from the goal outwards, assigning a traversal
    cost (weight) to each zone based on distance and zone types.

    Attributes:
        connect_map (Dict[str, List[str]]): An adjacency list of the map's
                                            connections.
        zones (Dict[str, Zone]): A dictionary of all Zone objects mapped by
                                 their names.
    """

    def __init__(self, connect_map: Dict[str, List[str]],
                 zones: Dict[str, Zone]) -> None:
        """
        Initializes the PathFinding instance.

        Args:
            connect_map (Dict[str, List[str]]): Adjacency list mapping zones to
                                                neighbors.
            zones (Dict[str, Zone]): Dictionary of instantiated Zone objects.
        """
        self.connect_map = connect_map
        self.zones = zones

    def find_path(self, goal: str) -> List[str]:
        """
        Generates a distance field by assigning cost weights to all zones.

        Uses a priority queue to explore the map starting from the goal node
        and radiating outwards. It updates the internal `weight` attribute of
        each Zone object, which the drones will later use to make routing
        decisions.

        Args:
            goal (str): The destination zone name acting as the origin of the
                        gradient.

        Returns:
            List[str]: Currently returns an empty list, as the primary purpose
                       is side-effecting the Zone weights for the flow field.
        """
        goal_node = self._create_node(
            position=goal,
            cost=0
            )

        open_list = [(goal_node["cost"], goal)]  # Priority queue
        open_dict = {goal: goal_node}            # Quickly node lookup
        closed_set = set()                       # Explorer for nodes

        while open_list:
            # Get zone with lowest value
            _, current_pos = heapq.heappop(open_list)
            if current_pos in closed_set:
                continue

            current_node = open_dict[current_pos]

            # End the loop if the position is the end
            # if current_pos == start_node:
            #     return self._reconstruct_path(current_node)

            # Mark the position as visited
            closed_set.add(current_pos)
            self._calculte_weight(
                current_pos,
                open_dict[current_pos]["cost"]
                )

            # Explore neighbors
            for (neighbor, cost) in self._get_valid_neighbors(
                    current_pos).items():
                # Skip if already explored
                if neighbor in closed_set:
                    continue

                neighbor_cost = (current_node["cost"] + cost)

                # Create or update neighbor
                if neighbor not in open_dict:
                    node = self._create_node(
                        position=neighbor,
                        cost=neighbor_cost,
                        parent=current_node)

                    heapq.heappush(open_list, (node["cost"], neighbor))
                    open_dict[neighbor] = node

                # Better path to the neighbor
                elif neighbor_cost < open_dict[neighbor]["cost"]:
                    node = open_dict[neighbor]
                    node["cost"] = neighbor_cost
                    node["parent"] = current_node
                    heapq.heappush(open_list, (node["cost"], neighbor))

        return []

    def _create_node(self, position: str, cost: float = float('inf'),
                     parent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        """
        Creates a dictionary representing a pathfinding node.

        Args:
            position (str): The name of the zone.
            cost (float): The cumulative cost to reach this node.
            parent (Dict[str, Any] | None): The preceding node in the path
                                            structure.

        Returns:
            Dict[str, Any]: A structured dictionary containing node data.
        """
        return {
            "position": position,
            "cost": cost,
            "parent": parent
        }

    def _get_valid_neighbors(self, position: str) -> Dict[str, float]:
        """
        Retrieves all traversable neighbors and their specific entry costs.

        Filters out blocked zones and applies specific cost modifiers based
        on the zone's metadata type (e.g., restricted, priority).

        Args:
            position (str): The name of the current zone being evaluated.

        Returns:
            Dict[str, float]: A dictionary mapping neighbor names to their
                              traversal costs.
        """
        valid_neighbors: Dict[str, float] = {}

        for neighbor in self.connect_map[position]:

            match self.zones[neighbor].metadata_zone_type:
                case ZoneType.BLOCKED:
                    pass
                case ZoneType.RESTRICTED:
                    valid_neighbors[neighbor] = 3.0
                case ZoneType.PRIORITY:
                    valid_neighbors[neighbor] = 0.9
                case ZoneType.NORMAL:
                    valid_neighbors[neighbor] = 1

        return valid_neighbors

    def _calculte_weight(self, position: str, cost: float) -> None:
        """
        Assigns the calculated cumulative cost to the physical Zone object.

        Args:
            position (str): The name of the zone to update.
            cost (float): The final calculated distance weight from the goal.
        """
        self.zones[position].weight = cost
