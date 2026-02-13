# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_fortytwo_pattern.py                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 14:41:10 by roandrie        #+#    #+#               #
#  Updated: 2026/02/09 15:39:54 by rruiz           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Provide coordinates for the '42' decorative pattern.

The project reserves a set of coordinates near the maze center where
the "42" pattern is placed and must not be overwritten by entry,
exit or generation algorithms.
"""

from typing import Set, Tuple


def get_fortytwo_pattern(width: int, height: int) -> Set[Tuple[int, int]]:
    """Calculates the set of coordinates forming the '42' shape.

    The pattern is mathematically centered based on the provided dimensions.
    If the maze dimensions are insufficient (<= 9x9) to display the pattern
    without clipping, an empty set is returned.

    Args:
        width: The total width of the maze grid.
        height: The total height of the maze grid.

    Returns:
        Set[Tuple[int, int]]: A set of (x, y) tuples representing the
        coordinates reserved for the '42' pattern. Returns an empty set
        if the maze is too small.
    """
    if width <= 9 or height <= 9:
        return set()

    center_x, center_y = width // 2, height // 2

    if center_x % 2 == 0:
        center_x += 1

    if center_y % 2 == 0:
        center_y += 1

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
