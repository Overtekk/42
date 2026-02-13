# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  enemy.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/10 08:25:43 by roandrie        #+#    #+#               #
#  Updated: 2026/02/10 14:22:17 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Enemy controller for the 'Hunted' game mode.

This module defines the `Enemy` class, which manages the behavior of the
hostile entity within the maze. It handles the initialization, spawning
mechanics (ensuring distance from the player), and pathfinding logic
to chase the player using Breadth-First Search (BFS).
"""

from typing import Dict, Tuple

from maze import MazeGenerator
from maze.maze_customization import MAZE


class Enemy():
    """
    Represents the hostile entity in the maze.
    """

    def __init__(self, maze: MazeGenerator) -> None:
        """Initializes the enemy with a reference to the maze.

        Args:
            maze: The MazeGenerator instance containing the grid layout
                  and dimensions.

        Attributes:
            maze (MazeGenerator): Reference to the game maze grid and
                                  dimensions.
            display_enemy (str): The visual character representing the enemy.
            enemy_x (int): The current X-coordinate of the enemy.
            enemy_y (int): The current Y-coordinate of the enemy.
        """
        self.maze = maze
        self.display_enemy = "🦖"
        self.enemy_x = 0
        self.enemy_y = 0

    def spawn(self) -> None:
        """Determines and sets the initial spawn location of the enemy.

        Scans the maze starting from the bottom-right corner (near the exit)
        to find the first valid empty cell. This ensures the enemy starts
        as far away from the player as possible.
        """
        player_x, player_y = self.maze.entry_coord

        target_x = self.maze.width - 2
        target_y = self.maze.height - 2

        target_x = max(1, target_x)
        target_y = max(1, target_y)

        search_queue = [(target_x, target_y)]
        visited_coords = set()

        while search_queue:
            curr_x, curr_y = search_queue.pop(0)

            if not (0 <= curr_x < self.maze.width and
                    0 <= curr_y < self.maze.height):
                continue

            if (curr_x, curr_y) in visited_coords:
                continue
            visited_coords.add((curr_x, curr_y))

            if self.maze.maze[(curr_y, curr_x)] == MAZE.empty:
                if (curr_x, curr_y) != (player_x, player_y):
                    self.enemy_x = curr_x
                    self.enemy_y = curr_y
                    break

            neighbors = [
                (curr_x - 1, curr_y),
                (curr_x, curr_y - 1),
                (curr_x + 1, curr_y),
                (curr_x, curr_y + 1)
            ]
            search_queue.extend(neighbors)

        if self.enemy_x is None:
            print("Warning: No empty space found for enemy, defaulting to 1,1")
            self.enemy_x, self.enemy_y = 1, 1

    def move(self, player_x: int, player_y: int) -> None:
        """Calculates and executes the next move towards the player.

        Uses a Breadth-First Search (BFS) algorithm to find the shortest
        path from the enemy's current position to the player's position.
        The enemy moves one step along this path.

        Args:
            player_x: The current X-coordinate of the player.
            player_y: The current Y-coordinate of the player.
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        start = (self.enemy_x, self.enemy_y)
        end = (player_x, player_y)

        visited = []
        queue = []
        path = []
        came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}

        visited.append(start)
        queue.append(start)

        while len(queue) > 0:
            cell = queue.pop(0)

            if cell == end:
                while cell != start:
                    path.append(cell)
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
                        (MAZE.empty, MAZE.entry)):

                    queue.append(neighbour)
                    came_from[neighbour_x, neighbour_y] = (cell_x, cell_y)
                    visited.append(neighbour)

        if len(path) > 0:
            next_move = path[-1]
            self.enemy_x, self.enemy_y = next_move
        else:
            pass
