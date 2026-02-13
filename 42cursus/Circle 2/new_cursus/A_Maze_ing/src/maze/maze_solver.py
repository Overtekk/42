# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_solver.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 08:52:18 by roandrie        #+#    #+#               #
#  Updated: 2026/02/10 13:21:08 by rruiz           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Maze path-finding and solving utilities.

This module provides the `MazeSolver` class, which implements algorithms
to solve generated mazes. It includes a Breadth-First Search (BFS) for
finding the shortest path and a recursive Depth-First Search (DFS) for
counting all possible solution paths. It also handles the visual rendering
of these paths in the terminal.
"""

import time

from typing import Any, Dict, List, Tuple
from colorama import Cursor

from .maze_generator import MazeGenerator
from .maze_customization import COLORS, MAZE, DISPLAY_MODE


class MazeSolver():
    """Finds and renders paths through a generated maze.

    This class encapsulates the pathfinding logic (BFS/DFS) and the
    visualization methods required to animate or print the solution
    over the existing maze in the terminal.

    Attributes:
        maze (MazeGenerator): A reference to the maze generator instance
            containing the grid data and configuration.
        path (List[Tuple[int, int]]): A list of (x, y) coordinates
            representing the solved path. The path is stored in reverse
            order (from exit to entry).
    """

    def __init__(self, maze: MazeGenerator) -> None:
        """Initializes the solver with a target maze.

        Args:
            maze: The `MazeGenerator` instance to be solved.
        """
        self.maze = maze
        self.path: List[Tuple[int, int]] = []

    def find_path(self) -> None:
        """Discovers the shortest path from entry to exit using BFS.

        Uses the Breadth-First Search algorithm to explore the grid layer
        by layer. Once the exit is found, the path is reconstructed
        backwards using a `came_from` map.

        The resulting path is stored in `self.path` starting from the
        exit coordinates down to the entry coordinates (excluded).
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        start = (self.maze.entry_x, self.maze.entry_y)
        end = (self.maze.exit_x, self.maze.exit_y)

        visited = []
        queue = []
        came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}

        visited.append(start)
        queue.append(start)

        while len(queue) > 0:
            cell = queue.pop(0)

            if cell == end:
                while cell != self.maze.entry_coord:
                    self.path.append(cell)
                    cell = came_from[cell]
                break

            cell_x, cell_y = cell

            for move_x, move_y in directions:
                neighbour_x = cell_x + move_x
                neighbour_y = cell_y + move_y
                neighbour = (neighbour_x, neighbour_y)

                if ((0 <= neighbour_x < self.maze.width and
                     0 <= neighbour_y < self.maze.height) and
                        neighbour not in visited and
                        self.maze.maze[(neighbour_x, neighbour_y)] in
                        (MAZE.empty, MAZE.exit)):

                    queue.append(neighbour)
                    came_from[neighbour_x, neighbour_y] = (cell_x, cell_y)
                    visited.append(neighbour)

    def path_checker(self) -> int:
        """Determines the number of valid paths from entry to exit.

        This method uses a recursive Depth-First Search (DFS) with backtracking
        to explore possible routes. It includes an optimization to stop the
        search immediately once more than one path is found, as its primary
        purpose is to distinguish between a perfect maze (unique path) and an
        imperfect one.

        Returns:
            int: The number of paths found. Returns 0 if unsolvable, 1 if
                 unique, and caps at 2 if multiple paths exist.
        """
        number_of_paths = 0

        def explore_recursive(x: int, y: int,
                              visited: set[Any]) -> bool | None:
            """Recursively explores the maze to find valid paths to the exit.

            This inner function performs a Depth-First Search (DFS) from
            the given coordinates. It updates the nonlocal `number_of_paths`
            counter when the exit is reached.

            Args:
                x: Current x-coordinate.
                y: Current y-coordinate.
                visited: A set of coordinates already visited in the current
                         recursion stack to prevent cycles.

            Returns:
                bool: True if the search should be aborted (i.e., more than one
                      path has been found), False otherwise.
            """
            nonlocal number_of_paths
            if number_of_paths > 1:
                return True

            if (x, y) == (self.maze.exit_x, self.maze.exit_y):
                number_of_paths += 1
                return number_of_paths > 1

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for move_x, move_y in directions:
                neighbor_x = x + move_x
                neighbor_y = y + move_y
                neighbor = (neighbor_x, neighbor_y)

                if ((0 <= neighbor_x < self.maze.width and
                    0 <= neighbor_y < self.maze.height) and
                        neighbor not in visited and
                        self.maze.maze[(neighbor_x, neighbor_y)] in
                        (MAZE.empty, MAZE.exit)):

                    visited.add(neighbor)
                    if explore_recursive(neighbor_x, neighbor_y, visited):
                        return True
                    visited.remove(neighbor)
            return False

        visited = {(self.maze.entry_x, self.maze.entry_y)}
        explore_recursive(self.maze.entry_x, self.maze.entry_y, visited)

        return number_of_paths

    def print_maze_solver(self) -> None:
        """Renders the entire maze with the solution path highlighted.

        Iterates through the grid and prints each cell. If a cell is part
        of `self.path`, it is rendered with the specific path color or
        symbol defined in the maze configuration.

        This method is typically used to redraw the maze statically after
        computation.
        """
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                cell = self.maze.maze[(x, y)]
                current_color = COLORS.reset
                symbol_to_print = self.maze.visual_empty

                if x == self.maze.entry_x and y == self.maze.entry_y:
                    if self.maze.display == DISPLAY_MODE.emoji:
                        symbol_to_print = self.maze.visual_entry
                    else:
                        symbol_to_print = self.maze.visual_wall
                        current_color = self.maze.color_entry

                elif x == self.maze.exit_x and y == self.maze.exit_y:
                    if self.maze.display == DISPLAY_MODE.emoji:
                        symbol_to_print = self.maze.visual_exit
                    else:
                        current_color = self.maze.color_exit
                        symbol_to_print = self.maze.visual_wall

                elif cell == MAZE.fortytwo:
                    if self.maze.display == DISPLAY_MODE.emoji:
                        symbol_to_print = self.maze.visual_ft
                    else:
                        current_color = self.maze.color_ft
                        symbol_to_print = self.maze.visual_wall

                elif cell == MAZE.empty:
                    if (x, y) in self.path:
                        if self.maze.display == DISPLAY_MODE.emoji:
                            symbol_to_print = self.maze.visual_path
                        else:
                            current_color = self.maze.color_path
                            symbol_to_print = self.maze.visual_wall
                    else:
                        pass

                elif cell == MAZE.wall:
                    if self.maze.display == DISPLAY_MODE.emoji:
                        symbol_to_print = self.maze.visual_wall
                    else:
                        current_color = self.maze.color_wall
                        symbol_to_print = self.maze.visual_wall

                print(f"{current_color}{symbol_to_print}{COLORS.reset}",
                      end="")
            print()

    def print_path(self) -> None:
        """Animates the solution path on the terminal.

        Iterates through `self.path` in reverse order (to go from Entry
        to Exit) and calls `_anim_path` to draw each step with a delay.
        Finally, moves the cursor below the maze to prevent overwriting.
        """
        for x, y in reversed(self.path):
            if (x, y) == self.maze.exit_coord:
                break
            self._anim_path(x, y)

        print(Cursor.POS(1, self.maze.height + 1))

    def _anim_path(self, x: int, y: int) -> None:
        """Draws a single path cell at the specific cursor position.

        Calculates the terminal cursor position based on the maze's
        rendering steps (offsets and character width) and prints the
        path symbol.

        Args:
            x: The grid X coordinate of the cell.
            y: The grid Y coordinate of the cell.
        """
        curs_x = (x * self.maze.step_x) + 1
        curs_y = y + self.maze.y_offset + 1

        if self.maze.display == DISPLAY_MODE.emoji:
            symbol: Any = self.maze.visual_path
        else:
            symbol = self.maze.visual_wall
        color = self.maze.color_path

        print(Cursor.POS(curs_x, curs_y) + f"{color}{symbol}{COLORS.reset}",
              end="", flush=True)
        time.sleep(0.003)
