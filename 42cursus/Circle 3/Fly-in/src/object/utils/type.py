# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  type.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 11:40:10 by roandrie        #+#    #+#               #
#  Updated: 2026/03/24 11:52:28 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Zone type enumeration module.

This module provides the ZoneType enumeration, which defines the different
behavioral categories and traversal rules applied to hubs within the
simulation grid.
"""

from enum import Enum


class ZoneType(str, Enum):
    """
    Enumeration defining the behavioral types and routing costs of zones.

    Attributes:
        NORMAL (str): Standard zone with a default 1-turn movement cost.
        BLOCKED (str): Inaccessible zone that drones cannot enter or path
                       through.
        RESTRICTED (str): Slower zone requiring 2 turns of movement cost to
                          traverse.
        PRIORITY (str): Fast-track zone with a 1-turn cost, prioritized by
                        pathfinding.
    """
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"

    def __str__(self) -> str:
        """
        Returns the raw string value of the zone type enumeration member.

        Returns:
            str: The raw string value representing the zone type.
        """
        return self.value
