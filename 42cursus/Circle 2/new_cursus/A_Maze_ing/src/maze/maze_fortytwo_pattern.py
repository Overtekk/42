# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_fortytwo_pattern.py                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 14:41:10 by roandrie        #+#    #+#               #
#  Updated: 2026/02/05 13:23:40 by rruiz           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Provide coordinates for the '42' decorative pattern.

The project reserves a set of coordinates near the maze center where
the "42" pattern is placed and must not be overwritten by entry,
exit or generation algorithms.
"""

from typing import Set, Tuple


def get_fortytwo_pattern(width: int, height: int) -> Set[Tuple[int, int]]:
    """Return a set of (x, y) coordinates forming the '42' pattern.

    Args:
        width: Maze width.
        height: Maze height.

    Returns:
        Set[Tuple[int, int]]: Coordinates reserved for the '42' pattern.
    """
    center_x, center_y = width // 2, height // 2

    return {
        (center_x - 3, center_y), (center_x - 3, center_y - 1),
        (center_x - 3, center_y - 2), (center_x - 1, center_y),
        (center_x - 2, center_y), (center_x - 1, center_y + 1),
        (center_x - 1, center_y + 2), (center_x + 3, center_y + 2),
        (center_x + 2, center_y + 2), (center_x + 1, center_y + 2),
        (center_x + 1, center_y), (center_x + 1, center_y + 1),
        (center_x + 2, center_y), (center_x + 3, center_y),
        (center_x + 3, center_y - 1), (center_x + 3, center_y - 2),
        (center_x + 2, center_y - 2), (center_x + 1, center_y - 2)
    }
