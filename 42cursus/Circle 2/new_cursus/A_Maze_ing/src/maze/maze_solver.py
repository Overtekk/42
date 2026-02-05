# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_solver.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 08:52:18 by roandrie        #+#    #+#               #
#  Updated: 2026/02/05 09:53:06 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import time

from typing import Dict, List, Tuple
from colorama import Cursor

from src.maze.maze_generator import MazeGenerator
from src.maze.maze_customization import COLORS, MAZE, DISPLAY_MODE


class MazeSolver():
    def __init__(self, maze: MazeGenerator) -> None:
        self.maze = maze
        self.path: List[Tuple[int, int]] = []

    def find_path(self) -> None:
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

    def print_maze_solver(self) -> None:
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
        for x, y in reversed(self.path):
            if (x, y) == self.maze.exit_coord:
                break
            self._anim_path(x, y)

        print(Cursor.POS(1, self.maze.height + 1))

    def _anim_path(self, x: int, y: int) -> None:
        curs_x = (x * self.maze.step_x) + 1
        curs_y = y + self.maze.y_offset + 1

        if self.maze.display == DISPLAY_MODE.emoji:
             symbol = self.maze.visual_path
        else:
             symbol = self.maze.visual_wall
        color = self.maze.color_path

        print(Cursor.POS(curs_x, curs_y) + f"{color}{symbol}{COLORS.reset}",
              end="", flush=True)
        time.sleep(0.003)
