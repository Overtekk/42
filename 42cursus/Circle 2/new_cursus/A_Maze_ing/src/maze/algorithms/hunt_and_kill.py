# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  hunt_and_kill.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 10:55:56 by rruiz           #+#    #+#               #
#  Updated: 2026/02/10 15:25:26 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Hunt-and-kill maze generation algorithm implementation.

This module provides a function to generate mazes using the Hunt-and-Kill
algorithm. This method alternates between two phases:
1.  Kill (Random Walk): Carves a random path until it hits a dead end
    or an existing path.
2.  Hunt (Scan): Scans the grid for an unvisited cell adjacent to
    a visited one, connects it, and restarts the Kill phase from there.

This implementation also handles the "imperfect" maze logic (creating loops)
directly within the scanning phase if configured.
"""

from random import choice, shuffle

from typing import Any

from maze.maze_customization import MAZE


def hunt_and_kill(generator: Any, rendering: bool) -> None:
    """Executes the Hunt-and-Kill algorithm on the provided generator.

    The function modifies the `generator.maze` grid in-place. It respects
    the reserved '42' pattern coordinates by checking
    `generator.fourtytwo_coord` before carving walls.

    Args:
        generator: The `MazeGenerator` instance containing the grid state,
                  dimensions, and configuration (perfect/imperfect).
        rendering: If True, calls `generator.break_wall` with visualization
                   enabled to animate the process in the terminal.
    """
    targets = (MAZE.wall, MAZE.entry, MAZE.exit)
    x, y = generator.entry_x, generator.entry_y

    if x % 2 == 0:
        x += 1 if x < generator.width - 1 else -1
    if y % 2 == 0:
        y += 1 if y < generator.height - 1 else -1

    generator.break_wall(x, y, rendering)
    while True:
        # Kill phase #
        while True:
            directions = []
            if y - 2 > 0:
                directions.append("N")
            if x < generator.width - 2:
                directions.append("E")
            if y < generator.height - 2:
                directions.append("S")
            if x - 2 > 0:
                directions.append("W")
            neighbors = {}
            if "N" in directions and generator.maze[(x, y - 2)] in targets:
                if ((x, y - 2) not in generator.fourtytwo_coord
                        and (x, y - 1) not in generator.fourtytwo_coord):
                    neighbors["N"] = (x, y - 2)
            if "E" in directions and generator.maze[(x + 2, y)] in targets:
                if ((x + 2, y) not in generator.fourtytwo_coord
                        and (x + 1, y) not in generator.fourtytwo_coord):
                    neighbors["E"] = (x + 2, y)
            if "S" in directions and generator.maze[(x, y + 2)] in targets:
                if ((x, y + 2) not in generator.fourtytwo_coord
                        and (x, y + 1) not in generator.fourtytwo_coord):
                    neighbors["S"] = (x, y + 2)
            if "W" in directions and generator.maze[(x - 2, y)] in targets:
                if ((x - 2, y) not in generator.fourtytwo_coord
                        and (x - 1, y) not in generator.fourtytwo_coord):
                    neighbors["W"] = (x - 2, y)
            if len(neighbors) == 0:
                break
            dir = choice(list(neighbors.keys()))
            target_x, target_y = neighbors[dir]
            mid_x = (x + target_x) // 2
            mid_y = (y + target_y) // 2
            generator.break_wall(mid_x, mid_y, rendering)
            generator.break_wall(target_x, target_y, rendering)
            x, y = target_x, target_y
        # Hunt phase #
        found = False
        for ty in range(1, generator.height - 1, 2):
            for tx in range(1, generator.width - 1, 2):
                if (generator.maze[(tx, ty)] in targets
                        and (tx, ty) not in generator.fourtytwo_coord):
                    potential_neighbors = []
                    if (generator.maze.get((tx, ty - 2)) == MAZE.empty
                            and generator.maze.get((tx, ty - 2)) is not None
                            and (tx, ty - 1) not in generator.fourtytwo_coord):
                        potential_neighbors.append((tx, ty - 1))
                    if (generator.maze.get((tx + 2, ty)) == MAZE.empty
                            and generator.maze.get((tx + 2, ty)) is not None
                            and (tx + 1, ty) not in generator.fourtytwo_coord):
                        potential_neighbors.append((tx + 1, ty))
                    if (generator.maze.get((tx, ty + 2)) == MAZE.empty
                            and generator.maze.get((tx, ty + 2)) is not None
                            and (tx, ty + 1) not in generator.fourtytwo_coord):
                        potential_neighbors.append((tx, ty + 1))
                    if (generator.maze.get((tx - 2, ty)) == MAZE.empty
                            and generator.maze.get((tx - 2, ty)) is not None
                            and (tx - 1, ty) not in generator.fourtytwo_coord):
                        potential_neighbors.append((tx - 1, ty))

                    if potential_neighbors:
                        mid_x, mid_y = choice(potential_neighbors)
                        generator.break_wall(mid_x, mid_y, rendering)
                        generator.break_wall(tx, ty, rendering)

                        x, y = tx, ty
                        found = True
                        break
            if found:
                break
        if not found:
            break


def _creates_open_area(generator: Any, wx: int, wy: int) -> bool:
    """Checks if breaking wall at (wx, wy) would create a 2x2 empty block.

    A 2x2 open area makes the maze look too open and not labyrinthine.
    The cell (wx, wy) participates in four potential 2x2 squares; if any
    of them would become fully empty, return True.

    Args:
        generator: The MazeGenerator instance.
        wx: X coordinate of the wall to check.
        wy: Y coordinate of the wall to check.

    Returns:
        True if breaking the wall would create a 2x2 open area.
    """
    for dx, dy in [(0, 0), (-1, 0), (0, -1), (-1, -1)]:
        bx, by = wx + dx, wy + dy
        cells = [(bx, by), (bx + 1, by), (bx, by + 1), (bx + 1, by + 1)]
        if all(
            (cx, cy) == (wx, wy)
            or generator.maze.get((cx, cy)) == MAZE.empty
            for cx, cy in cells
        ):
            return True
    return False


def break_walls_hak(generator: Any, rendering: bool) -> None:
    """Removes walls at dead-ends to create an imperfect maze (multiple paths).

    Uses the same dead-end detection strategy as `break_random_walls`
    from the backtracking module: finds empty cells surrounded by 3 or
    more walls/borders, then breaks a wall toward an adjacent path cell
    to create loops. Respects the '42' pattern coordinates.

    If the dead-end pass does not create at least 2 distinct paths,
    a second pass targets any internal wall separating two empty cells,
    which is guaranteed to introduce a cycle.

    Args:
        generator: The `MazeGenerator` instance to modify.
        rendering: If True, animates the wall removal in the terminal.
    """
    potential_wall_to_break = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for y in range(generator.height):
        for x in range(generator.width):
            if generator.maze[(x, y)] == MAZE.empty:
                totals_walls = 0
                corner_walls = []
                for dir_x, dir_y in directions:
                    neighbour_x = dir_x + x
                    neighbour_y = dir_y + y
                    target_x = x + (dir_x * 2)
                    target_y = y + (dir_y * 2)

                    if (not (0 <= neighbour_x < generator.width
                             and 0 <= neighbour_y < generator.height)
                            or generator.maze.get((neighbour_x, neighbour_y))
                            == MAZE.wall):
                        totals_walls += 1

                    if (0 < neighbour_x < generator.width
                            and 0 < neighbour_y < generator.height
                            and 0 < target_x < generator.width
                            and 0 < target_y < generator.height
                            and generator.maze[(neighbour_x, neighbour_y)]
                            == MAZE.wall
                            and generator.maze[(target_x, target_y)]
                            == MAZE.empty
                            and (neighbour_x, neighbour_y) not in
                            generator.fourtytwo_coord):
                        corner_walls.append((neighbour_x, neighbour_y))

                if totals_walls >= 3 and len(corner_walls) > 0:
                    potential_wall_to_break.append(choice(corner_walls))

    shuffle(potential_wall_to_break)

    from ..maze_solver import MazeSolver

    for wall_x, wall_y in potential_wall_to_break:
        if choice([True, False]):
            if not _creates_open_area(generator, wall_x, wall_y):
                generator.break_wall(wall_x, wall_y, rendering)
                if MazeSolver(generator).path_checker() >= 2:
                    return

    for wall_x, wall_y in potential_wall_to_break:
        if generator.maze[(wall_x, wall_y)] == MAZE.wall:
            if not _creates_open_area(generator, wall_x, wall_y):
                generator.break_wall(wall_x, wall_y, rendering)
                if MazeSolver(generator).path_checker() >= 2:
                    return

    cycle_walls = []
    for y in range(1, generator.height - 1):
        for x in range(1, generator.width - 1):
            if (generator.maze[(x, y)] == MAZE.wall
                    and (x, y) not in generator.fourtytwo_coord):
                if (generator.maze.get((x - 1, y)) == MAZE.empty
                        and generator.maze.get((x + 1, y)) == MAZE.empty):
                    cycle_walls.append((x, y))
                elif (generator.maze.get((x, y - 1)) == MAZE.empty
                      and generator.maze.get((x, y + 1)) == MAZE.empty):
                    cycle_walls.append((x, y))

    shuffle(cycle_walls)
    for wall_x, wall_y in cycle_walls:
        if generator.maze[(wall_x, wall_y)] == MAZE.wall:
            if not _creates_open_area(generator, wall_x, wall_y):
                generator.break_wall(wall_x, wall_y, rendering)
                if MazeSolver(generator).path_checker() >= 2:
                    return
