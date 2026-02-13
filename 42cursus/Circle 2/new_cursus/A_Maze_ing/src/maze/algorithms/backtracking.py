# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  backtracking.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 16:16:22 by roandrie        #+#    #+#               #
#  Updated: 2026/02/09 09:34:07 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Recursive Backtracking maze generation algorithm.

This module implements the Depth-First Search (DFS) based maze generation
strategy, commonly known as Recursive Backtracking. It also includes
post-processing utilities to introduce loops into the maze for
"imperfect" generation modes.
"""

import random
import sys

from typing import Any

from maze.maze_customization import MAZE


def recursive_backtracking(generator: Any, rendering: bool) -> None:
    """Generates a perfect maze using the Recursive Backtracking algorithm.

    This function increases the system recursion limit to handle the grid
    size, selects a valid starting point ensuring parity alignment, and
    initiates the recursive `visit` function to carve paths.

    The algorithm works by:
    1. Choosing a starting cell.
    2. Randomly choosing an unvisited neighbor.
    3. Moving to that neighbor (breaking the wall between them).
    4. Recursively repeating step 2 until dead-end.
    5. Backtracking to the previous cell.

    Args:
        generator: The `MazeGenerator` instance containing the grid and
                   configuration.
        rendering: If True, visualizes the wall breaking process in
                   real-time.
    """
    recursion_limit = generator.width * generator.height
    sys.setrecursionlimit(recursion_limit)

    start_coords = generator.entry_coord

    if start_coords[0] % 2 == 0:
        if random.choice([True, False]):
            start_coords = (start_coords[0] + 1, start_coords[1])
        else:
            start_coords = (start_coords[0] - 1, start_coords[1])
    if start_coords[1] % 2 == 0:
        if random.choice([True, False]):
            start_coords = (start_coords[0], start_coords[1] + 1)
        else:
            start_coords = (start_coords[0], start_coords[1] - 1)

    start_coords_x, start_coords_y = start_coords
    generator.break_wall(start_coords_x, start_coords_y, rendering)

    def visit(x: int, y: int) -> None:
        walls_list = {}
        walls_random = []

        if 0 <= x - 2 < generator.width:
            if (generator.maze[(x - 2, y)] in
                    (MAZE.wall, MAZE.entry, MAZE.exit) and
                    generator.maze[(x - 1, y)] == MAZE.wall):
                walls_list.update({"west": x - 2})

        if x + 2 < generator.width:
            if (generator.maze[(x + 2, y)] in
                    (MAZE.wall, MAZE.entry, MAZE.exit) and
                    generator.maze[(x + 1, y)] == MAZE.wall):
                walls_list.update({"east": x + 2})

        if 0 <= y - 2 < generator.height:
            if (generator.maze[(x, y - 2)] in
                    (MAZE.wall, MAZE.entry, MAZE.exit) and
                    generator.maze[(x, y - 1)] == MAZE.wall):
                walls_list.update({"south": y - 2})

        if y + 2 < generator.height:
            if (generator.maze[(x, y + 2)] in
                    (MAZE.wall, MAZE.entry, MAZE.exit) and
                    generator.maze[(x, y + 1)] == MAZE.wall):
                walls_list.update({"north": y + 2})

        if len(walls_list) > 0:

            walls_random = list(walls_list)
            random.shuffle(walls_random)

            for item in walls_random:
                target_x, target_y = x, y
                mid_x, mid_y = x, y

                if item == "north":
                    target_y = walls_list[item]
                    mid_y = (y + target_y) // 2

                elif item == "south":
                    target_y = walls_list[item]
                    mid_y = (y + target_y) // 2

                elif item == "east":
                    target_x = walls_list[item]
                    mid_x = (x + target_x) // 2

                elif item == "west":
                    target_x = walls_list[item]
                    mid_x = (x + target_x) // 2

                if (generator.maze[(target_x, target_y)] in
                        (MAZE.wall, MAZE.entry, MAZE.exit) and
                        generator.maze[(mid_x, mid_y)] == MAZE.wall and
                        (mid_x, mid_y) not in generator.fourtytwo_coord):

                    generator.break_wall(target_x, target_y, rendering)
                    generator.break_wall(mid_x, mid_y, rendering)

                    visit(target_x, target_y)

    visit(start_coords_x, start_coords_y)


def break_random_walls(generator: Any, rendering: bool) -> None:
    """Removes additional walls to create an imperfect maze.

    Scans the generated maze for dead-ends or specific wall configurations
    and randomly removes walls to create loops and alternative paths.
    This is only executed if the `perfect` configuration is set to False.

    Args:
        generator: The `MazeGenerator` instance to modify.
        rendering: If True, updates the terminal display for each broken wall.
    """
    potential_wall_to_break = []

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for y in range(generator.height):
        for x in range(generator.width):
            if (generator.maze[(x, y)] == MAZE.empty):
                totals_walls = 0
                corner_walls = []
                for dir_x, dir_y in directions:
                    neighbour_x = dir_x + x
                    neighbour_y = dir_y + y

                    target_x = x + (dir_x * 2)
                    target_y = y + (dir_y * 2)

                    if (not (0 <= neighbour_x < generator.width and
                             0 <= neighbour_y < generator.height) or
                            generator.maze.get((neighbour_x, neighbour_y)) ==
                            MAZE.wall):
                        totals_walls += 1

                    if (0 < neighbour_x < generator.width and
                            0 < neighbour_y < generator.height and
                            0 < target_x < generator.width and
                            0 < target_y < generator.height and
                            generator.maze[(neighbour_x, neighbour_y)] ==
                            MAZE.wall and generator.maze[(target_x, target_y)]
                            == MAZE.empty):

                        corner_walls.append((neighbour_x, neighbour_y))

                if totals_walls >= 3 and len(corner_walls) > 0:
                    potential_wall_to_break.append(random.choice(corner_walls))

    for wall_x, wall_y in potential_wall_to_break:
        if random.choice([True, False]):
            generator.break_wall(wall_x, wall_y, rendering)
