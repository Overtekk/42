# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_fortytwo_pattern.py                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 14:41:10 by roandrie        #+#    #+#               #
#  Updated: 2026/02/02 15:47:12 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Set, Tuple


def get_fortytwo_pattern(width: int, height: int) -> Set[Tuple[int, int]]:
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
