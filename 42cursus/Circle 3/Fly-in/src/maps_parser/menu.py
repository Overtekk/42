# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  menu.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 18:48:26 by roandrie        #+#    #+#               #
#  Updated: 2026/03/24 13:47:52 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Function to show a menu to the user with all maps availables and also maps
that containts errors so the user can correct them.
"""

import re
import os

from time import sleep
from typing import Tuple

from src.utils.ui import Colors
from src.maps_parser.parser import MapModel, Maps


def print_menu(maps: Maps) -> Tuple[str, MapModel] | int:
    """Displays an interactive terminal menu for map selection.

    Navigates through available map categories, allows the user to inspect
    parsing errors from invalid map files, and handles the final selection
    of a valid map for the simulation.

    Args:
        maps (Maps): An object containing categorized valid maps and a
                     dictionary of invalid maps with their respective
                     parsing errors.

    Returns:
        Tuple[str, MapModel]: A tuple containing the file name of the
                              selected map and its parsed MapModel object.
                              (Note: Returns the integer 0 if the user
                              chooses to exit the application).
    """

    # Constant to defines the width of the menu
    WIDTH = 40
    # Define the order of categories
    order = ["easy", "medium", "hard", "other", "custom", "challenger"]

    available_categories = list(maps.maps_dict.keys())

    def custom_sort(name: str) -> int:
        """Utilitary function to sort maps categories based on a order.

        Args:
            name (str): the item to sort.

        Returns:
            int: index of the sorted item.
        """
        name_lower = name.lower()
        if name_lower in order:
            return order.index(name_lower)
        return len(order)

    available_categories.sort(key=custom_sort)

    category = {i: name for i, name in enumerate(available_categories, 1)}

    def get_title() -> str:
        """Get the project's title of the project.

        Returns:
            str: the title project.
        """
        return f"{Colors.LIGHT_CYAN}{Colors.BOLD}Fly-in{Colors.END}"

    def get_subtitle() -> str:
        """Short string to explain to the user how to select map.

        Returns:
            str: the string with the explanation.
        """
        return f"{Colors.BLUE}Choose your map using the numpad{Colors.END}"

    def center(text: str, width: int) -> str:
        """Center a text based on a with.

        Args:
            text (str): the text to center.
            width (int): the width to calculate.

        Returns:
            str: string centered with spaces.
        """
        visible_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
        visible_len = len(visible_text)

        padding = ((width + 2) - visible_len) // 2

        return " " * padding + text

    def print_header() -> None:
        """
        Print the header of the project containing the title and the
        subtitle and clear the terminal screen.
        """
        os.system("clear")
        print("")
        print(f"{Colors.LIGHT_WHITE}┏" + "━" * WIDTH + f"┓{Colors.END}")
        print(center(get_title(), WIDTH))
        print("")
        print(center(get_subtitle(), WIDTH))
        print(f"{Colors.LIGHT_WHITE}┗" + "━" * (WIDTH) + f"┛{Colors.END}")
        print("")

    def print_error_input() -> None:
        """
        Print an error if the user input is incorrect and clear the line.
        """
        print(f"{Colors.CLEARLINE}{Colors.RED}❌ERROR{Colors.END}",
              end="", flush=True)
        sleep(0.6)
        print("\r\033[K\033[A", end="")

    curr_category = None

    # Main loop the show the menu until a map is selected or the user leave
    while True:
        user_input = None
        choice = None
        print_header()

        # Show category menu
        if curr_category is None:
            for i, name in category.items():
                print(f"{Colors.BOLD}{Colors.LIGHT_BLUE}{i}: {name.title()}"
                      f"{Colors.END}")

            if maps.invalid_maps_dict:
                print(f"\n{Colors.BOLD}{Colors.LIGHT_BLUE}{len(category) + 1}"
                      f": Invalid maps{Colors.END}")

            print(f"\n{Colors.BOLD}{Colors.LIGHT_WHITE}0: Leave{Colors.END}")

            while True:
                user_input = input(f"\n{Colors.ITALIC}Choice: {Colors.END}")
                try:
                    choice = int(user_input)
                    if 0 <= choice <= len(category) + 1:
                        break
                    else:
                        raise ValueError

                except ValueError:
                    print_error_input()

            if choice == 0:
                print(f"{Colors.GREEN}\n👋 Bye!{Colors.END}")
                return 0
            if choice == len(category) + 1:
                curr_category = "invalid"
            else:
                curr_category = category[choice]

        # Show invalid maps
        elif curr_category == "invalid":
            invalid_list = [map for list in maps.invalid_maps_dict.values()
                            for map in list]

            for i, (name, error) in enumerate(invalid_list, 1):
                print(f"{Colors.BOLD}{Colors.LIGHT_BLUE}{i}: {Colors.ITALIC}"
                      f"{name}{Colors.END}")

            print(f"\n{Colors.BOLD}{Colors.LIGHT_WHITE}0: Back{Colors.END}")

            while True:
                user_input = input(f"\n{Colors.ITALIC}Choice: {Colors.END}")
                try:
                    choice = int(user_input)
                    if 0 <= choice <= len(invalid_list):
                        break
                    else:
                        raise ValueError

                except ValueError:
                    print_error_input()

            if choice == 0:
                curr_category = None
            else:
                selected_map = invalid_list[choice - 1]
                print(f"\n{Colors.RED}{Colors.BOLD}Error in '{selected_map[0]}"
                      f"':\n{Colors.ITALIC}{selected_map[1]}{Colors.END}")
                input("\nPress Enter to continue...")
                curr_category = "invalid"

        # Show maps menu
        else:
            maps_list = maps.maps_dict[curr_category]
            maps_selection = {i: name for i, name in enumerate(maps_list, 1)}

            if len(maps_selection) == 0:
                print(f"{Colors.BOLD}{Colors.LIGHT_BLUE}No map in this folder."
                      f" Maybe an error?{Colors.END}")
            else:
                for i, name in maps_selection.items():
                    print(f"{Colors.BOLD}{Colors.LIGHT_BLUE}{i}: "
                          f"{Colors.ITALIC}{name}{Colors.END}")

            print(f"\n{Colors.BOLD}{Colors.LIGHT_WHITE}0: Back{Colors.END}")

            while True:
                user_input = input(f"\n{Colors.ITALIC}Choice: {Colors.END}")
                try:
                    choice = int(user_input)
                    if 0 <= choice <= len(maps_selection):
                        break
                    else:
                        raise ValueError

                except ValueError:
                    print_error_input()

            if choice == 0:
                curr_category = None
            else:
                print(f"\n{Colors.YELLOW}Selected map: {Colors.GREEN}"
                      f"{maps_selection[choice]}{Colors.END}")
                selected = maps_selection[choice]
                return (selected, maps.connection_map[selected])

        print_header()
