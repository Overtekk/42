# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/20 16:25:20 by roandrie        #+#    #+#               #
#  Updated: 2026/01/24 12:34:54 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Main script for the Maze Generator.

First, we check if all dependencies are installed. If no error have been found,
we can import everything and start to check the config file.
Then, construct the maze, output it and launch the 'game'.
"""

import sys

from src.utils.modules_check import module_checker


def main() -> int:
    """"Programm main entry point.

    Returns:
        int: 0 if no error occured, 1 or 2 otherwise.

    """
    try:
        try:
            module_checker()
        except ModuleNotFoundError as e:
            print(f"{type(e).__name__}: {e}", file=sys.stderr)
            return 2

        from src.utils.config import check_arg, IllegalArgumentError
        from src.maze.maze_generator import MazeGenerator

        config = check_arg()
        if config is None:
            return 2
        config_dict = config.model_dump()

        generator = MazeGenerator(**config_dict)
        generator.maze_generator()

    except (IllegalArgumentError, FileNotFoundError, ValueError) as e:

        print(f"{type(e).__name__}: {e}", file=sys.stderr)
        return 2

    # except Exception as e:
    #     print(f"Unexpected error of type - {type(e).__name__}: {e}",
    #           file=sys.stderr)
    #     return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
