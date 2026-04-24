# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ui.py                                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 16:56:39 by roandrie        #+#    #+#               #
#  Updated: 2026/03/24 13:45:41 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
User Interface utility module for terminal output formatting.

This module provides classes and methods to facilitate the display of colored
messages, error logging, and loading animations within the terminal interface,
improving the overall user experience.
"""

import sys
import time

from enum import Enum
from typing import Tuple

from src.utils.x11_colors import X11_NAMES


class Display():
    """
    Utility class for standardizing terminal outputs.

    Provides static methods to output formatted error messages to the standard
    error stream and to display a visual loading animation in the standard
    output stream.
    """

    @staticmethod
    def error(message: str) -> None:
        """
        Outputs a formatted and colored error message to the standard error
        stream.

        Args:
            message (str): The specific error description to be displayed.
        """
        prefix = f"{Colors.BOLD}{Colors.RED}Error: {Colors.END}"
        content = f"{Colors.RED}{message}{Colors.END}"
        print(prefix + content, file=sys.stderr)

    @staticmethod
    def loading(wait_time: float) -> None:
        """
        Displays a spinning loading animation in the terminal for a specific
        duration.

        This method blocks the main execution thread while the animation is
        playing.

        Args:
            wait_time (float): The duration in tenths of a second (iterations)
                               to run the loading animation.
        """
        animation = "|/-\\"
        index = 0

        while wait_time >= 0:
            print(animation[index % len(animation)], end="\r")
            index += 1
            time.sleep(0.1)
            wait_time -= 1


class Colors(str, Enum):
    """
    Enumeration of ANSI color codes and text formatting styles.

    This class maps human-readable color names and styling options (like bold
    or italic) to their corresponding ANSI escape sequences for terminal usage.
    It also provides utility methods to convert standard X11/CSS color names
    into TrueColor ANSI sequences or RGB tuples.
    """

    WHITE = "\033[37m"
    RED = "\033[31m"
    BLACK = "\033[30m"
    GREEN = "\033[32m"
    BROWN = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    DARK_GRAY = "\033[30m"
    LIGHT_GRAY = "\033[37m"
    LIGHT_RED = "\033[31m"
    LIGHT_GREEN = "\033[32m"
    LIGHT_BLUE = "\033[34m"
    LIGHT_PURPLE = "\033[35m"
    LIGHT_CYAN = "\033[36m"
    LIGHT_WHITE = "\033[37m"

    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"

    END = "\033[0m"
    CLEARLINE = "\033[F\033[K"

    @staticmethod
    def get_rgb_code(color_name: str) -> str:
        """
        Transforms a CSS/X11 color name into an ANSI TrueColor escape sequence.

        If the provided color name is not found in the X11_NAMES dictionary,
        it defaults to returning the standard ANSI white sequence.

        Args:
            color_name (str): The standard name of the target color
                              (e.g., 'lime').

        Returns:
            str: The corresponding ANSI TrueColor escape sequence.
        """
        name = color_name.lower()
        if name not in X11_NAMES:
            return Colors.WHITE.value

        hex_code = X11_NAMES[name].lstrip('#')

        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)

        return f"\033[38;2;{r};{g};{b}m"

    @staticmethod
    def get_rgb_color(color_name: str) -> Tuple[int, int, int]:
        """
        Transforms a CSS/X11 color name into an RGB integer tuple.

        If the provided color name is not found in the X11_NAMES dictionary,
        it defaults to returning pure white (255, 255, 255).

        Args:
            color_name (str): The standard name of the target color
                              (e.g., 'lime').

        Returns:
            Tuple[int, int, int]: A tuple containing the Red, Green, and Blue
                                  integer values.
        """
        name = color_name.lower()
        if name not in X11_NAMES:
            return (255, 255, 255)

        hex_code = X11_NAMES[name].lstrip('#')

        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)

        return (int(r), int(g), int(b))

    def __str__(self) -> str:
        """
        Returns the raw ANSI escape sequence for the enumeration member.

        Returns:
            str: The raw ANSI color code.
        """
        return self.value
