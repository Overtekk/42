# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_output.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:56:40 by rruiz           #+#    #+#               #
#  Updated: 2026/02/05 14:45:29 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Write maze to a compact textual output format.

The output format encodes the presence of surrounding walls for each
cell using a single hexadecimal digit per cell, followed by entry and
exit coordinates and the path directions as NSEW characters.
"""

from typing import Any

from maze.maze_customization import MAZE


def maze_output(generator: Any, path: Any) -> None:
    """Serialize the generated maze to the configured output file.

    Args:
        generator: MazeGenerator providing the grid and coordinates.
        path: Sequence of coordinates forming the solution path.
    """
    hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C",
            "D", "E", "F"]
    with open(generator.output_file, 'w') as f:
        for ty in range(1, generator.height - 1, 2):
            for tx in range(1, generator.width - 1, 2):
                decimal_val = 0
                if generator.maze[(tx, ty - 1)] == MAZE.wall:
                    decimal_val = decimal_val + 2**0
                if generator.maze[(tx + 1, ty)] == MAZE.wall:
                    decimal_val = decimal_val + 2**1
                if generator.maze[(tx, ty + 1)] == MAZE.wall:
                    decimal_val = decimal_val + 2**2
                if generator.maze[(tx - 1, ty)] == MAZE.wall:
                    decimal_val = decimal_val + 2**3
                f.write(hexa[decimal_val])
            f.write("\n")
        f.write('\n')
        entry_x, entry_y = generator.entry_coord
        f.write(f"{entry_x},{entry_y}\n")
        exit_x, exit_y = generator.exit_coord
        f.write(f"{exit_x},{exit_y}\n")
        path.append((entry_x, entry_y))
        path.reverse()
        directions = []
        for i in range(len(path) - 1):
            current_move = path[i]
            next_move = path[i + 1]

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
