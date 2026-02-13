# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_output.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:56:40 by rruiz           #+#    #+#               #
#  Updated: 2026/02/13 10:40:49 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


"""Utilities for exporting the generated maze to a text file.

This module handles the serialization of the maze grid into a specific
hexadecimal format, along with the entry/exit points and the solution
path represented as cardinal directions.
"""

from typing import Any

from maze.maze_customization import MAZE


def maze_output(generator: Any, path: Any) -> None:
    """Writes the maze configuration and solution to the output file.

    The output format consists of:
    1. A grid of hexadecimal characters, where each character represents
       the configuration of walls surrounding a cell.
    2. The entry coordinates (x,y).
    3. The exit coordinates (x,y).
    4. The solution path expressed as a string of directions (N, S, E, W).

    Args:
        generator: The `MazeGenerator` instance containing the maze grid,
                  dimensions, and configuration.
        path: A list of (x, y) tuples representing the solution path.
    """
    hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C",
            "D", "E", "F"]
    targets = (MAZE.wall, generator.fourtytwo_coord)
    with open(generator.output_file, 'w') as f:
        for ty in range(1, generator.height - 1, 2):
            for tx in range(1, generator.width - 1, 2):
                decimal_val = 0
                if generator.maze[(tx, ty - 1)] in targets:
                    decimal_val = decimal_val + 2**0
                if generator.maze[(tx + 1, ty)] in targets:
                    decimal_val = decimal_val + 2**1
                if generator.maze[(tx, ty + 1)] in targets:
                    decimal_val = decimal_val + 2**2
                if generator.maze[(tx - 1, ty)] in targets:
                    decimal_val = decimal_val + 2**3
                f.write(hexa[decimal_val])
            f.write("\n")
        f.write('\n')

        entry_x = (generator.entry_coord[0] - 1) // 2
        entry_y = (generator.entry_coord[1] - 1) // 2
        f.write(f"{entry_x},{entry_y}\n")

        exit_x = (generator.exit_coord[0] - 1) // 2
        exit_y = (generator.exit_coord[1] - 1) // 2
        f.write(f"{exit_x},{exit_y}\n")

        if generator.entry_coord not in path:
            path.append(generator.entry_coord)

        path.reverse()
        directions = []
        for i in range(0, len(path) - 2, 2):
            current_move = path[i]
            next_move = path[i + 2]

            dir_x = next_move[0] - current_move[0]
            dir_y = next_move[1] - current_move[1]

            if dir_y < 0:
                directions.append("N")
            elif dir_y > 0:
                directions.append("S")
            elif dir_x > 0:
                directions.append("E")
            elif dir_x < 0:
                directions.append("W")

        f.write("".join(directions))
        f.write("\n")
