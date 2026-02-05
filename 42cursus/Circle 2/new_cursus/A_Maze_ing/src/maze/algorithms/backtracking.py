# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  backtracking.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 16:16:22 by roandrie        #+#    #+#               #
#  Updated: 2026/02/03 12:59:45 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random
import sys

from typing import Any, Tuple

from ..maze_customization import MAZE


def recursive_backtracking(generator: Any, rendering: bool) -> None:
    recursion_limit = generator.width * generator.height
    sys.setrecursionlimit(recursion_limit)

    start_coords = _choose_random_starting_point(generator)
    start_coords_x, start_coords_y = start_coords

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


def _choose_random_starting_point(generator: Any) -> Tuple[int, int]:
    while True:
        x = random.randrange(1, generator.width, 2)
        y = random.randrange(1, generator.height, 2)

        coords = (x, y)

        if coords == generator.entry_coord:
            continue
        if coords == generator.exit_coord:
            continue
        if coords in generator.fourtytwo_coord:
            continue

        return coords


def break_random_walls(generator: Any, rendering: bool) -> None:
    n_wall_to_break = max(0, (generator.width - generator.height))

    while n_wall_to_break > 0:
        x = random.randrange(1, generator.width, 1)
        y = random.randrange(1, generator.height, 1)
        if generator.maze[(x, y)] == MAZE.wall:
            generator.break_wall(x, y, rendering)
            n_wall_to_break -= 1
