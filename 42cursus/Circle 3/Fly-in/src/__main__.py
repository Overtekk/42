# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __main__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 18:28:19 by roandrie        #+#    #+#               #
#  Updated: 2026/04/01 21:54:37 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Entry point for the program. It will check arguments and parse it. Call the
needeed class to check if the map is valid and launch the simulation.
"""

import sys
import argparse

from pathlib import Path

from src.utils.ui import Display
from src.utils.errors import ArgumentError, MapError
from src.utils.module_checker import module_checker


def main() -> int:
    try:

        # Check if a module is missing if user don't use make or uv
        try:
            module_checker()
        except ModuleNotFoundError as e:
            Display.error(f"{e}")
            return 2

        from src.maps_parser.parser import Maps, MapModel
        from src.maps_parser.menu import print_menu
        from src.simulation.manager import Manager

        # Init the paser and add arguments to it
        parser = argparse.ArgumentParser(
            prog="Fly-in",
            description=("Design an efficient drone routing system that "
                         "navigates multiple drones through connected zones "
                         "while minimizing simulation turns and handling "
                         "movement constraints.")
        )
        parser.add_argument(
            "filepath",
            nargs="?",
            default=None,
            help=("launch the main program script. You can specify a map to "
                  "use instead of having the whole menu. (Maps are stored in "
                  "the folder 'maps').")
        )
        parser.add_argument(
            "-d", "--debug",
            action="store_true",
            help="Launch the program with the debug mode."
        )
        parser.add_argument(
            "-sl", "--show_logs",
            action="store_true",
            help=("show the logs output directly in the console while the "
                  "simulation is running.")
        )
        parser.add_argument(
            "-sml", "--show_more_logs",
            action="store_true",
            help=("show more informations in the logs output (number of drones"
                  " still in progress, zones capacity etc...). If this "
                  "argument is added, '--show_logs' isn't needeed.")
        )
        args = parser.parse_args()

        # If a map is provided in the argument call validator for only this
        # map
        if args.filepath is not None:
            map = MapModel.is_map_valid(Path(args.filepath))
            map_name = args.filepath.split("/")
            map_name = map_name[-1]
        # Otherwise, check the Maps folder and check all maps
        else:
            map_model = Maps()
            map_tuple = print_menu(map_model)

            if not isinstance(map_tuple, tuple):
                return 0

            map_name, map = map_tuple
            map_name += ".txt"

            if not isinstance(map, MapModel):
                return 0

            Display.loading(1 * 10)  # Display a loading logo for visual
            print("\n")

        # Launch main simulation
        my_manager = Manager(map, map.connection_map, args, map_name)
        my_manager.run()

    except (ArgumentError, MapError) as e:
        Display.error(f"{e}")
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())

    except KeyboardInterrupt:
        print("")
        Display.error("\nProgram interrupted by user.")
        sys.exit(130)

    # except Exception as e:
    #     Display.error(f"{e}")
    #     sys.exit(1)
