# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_customization.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 16:35:27 by roandrie        #+#    #+#               #
#  Updated: 2026/02/09 09:22:49 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Visual and display constants used by maze rendering.

This module centralizes enums for visual symbols, color palettes,
display modes and small terminal animations. These enums are used
throughout the package to keep rendering consistent.
"""

from enum import Enum

from colorama import Fore, Style


class VISUAL(str, Enum):
    """Defines string constants for ASCII block rendering.

    These symbols are used to draw walls and spaces when the display mode
    is set to ASCII or Simple.

    Attributes:
        block: A double solid block character (██) for walls.
        empty_block: A double space string for empty paths.
        empty: A single space string for compact rendering.
    """
    block = "\u2588\u2588"
    empty_block = "  "
    empty = " "

    def __str__(self) -> str:
        """Return the string value of the enum member."""
        return self.value


class MAZE(Enum):
    """Defines integer constants representing cell types in the grid.

    These values map the internal logical state of a cell to a integer.

    Attributes:
        empty: Represents a navigable path.
        wall: Represents a wall or obstacle.
        exit: Represents the target exit point.
        entry: Represents the starting point.
        fortytwo: Represents the special decorative pattern.
    """
    empty = 0
    entry = 3
    exit = 2
    wall = 1
    fortytwo = 4


class COLORS(Enum):
    """Defines ANSI color codes for terminal output.

    This class wraps `colorama.Fore` constants to provide a unified
    access point for text coloration throughout the application.
    """
    green = Fore.GREEN
    black = Fore.BLACK
    blue = Fore.BLUE
    cyan = Fore.CYAN
    white = Fore.WHITE
    lightblack = Fore.LIGHTBLACK_EX
    lightblue = Fore.LIGHTBLUE_EX
    lightcyan = Fore.LIGHTCYAN_EX
    lightgreen = Fore.LIGHTGREEN_EX
    lightmagenta = Fore.LIGHTMAGENTA_EX
    lightred = Fore.LIGHTRED_EX
    lightwhite = Fore.LIGHTWHITE_EX
    lightyellow = Fore.LIGHTYELLOW_EX
    magenta = Fore.MAGENTA
    red = Fore.RED
    reset = Fore.RESET
    yellow = Fore.YELLOW

    def __str__(self) -> str:
        """Return the ANSI escape sequence as a string."""
        return str(self.value)


class EMOJI(str, Enum):
    """Defines Emoji constants for the 'emoji' display mode.

    These characters are used as an alternative to ASCII blocks for a
    more graphical terminal rendering.
    """
    white = "⬜"
    magenta = "🟪"
    blue = "🟦"
    brown = "🟫"
    yellow = "🟨"
    green = "🟩"
    red = "🟥"
    orange = "🟧"
    ft_1 = "🔳"
    ft_2 = "🔲"

    def __str__(self) -> str:
        """Return the emoji character as a string."""
        return self.value


class STYLE(Enum):
    """Defines ANSI style codes (brightness/dimming).

    Wraps `colorama.Style` to control text weight and reset states.
    """
    bright = Style.BRIGHT
    dim = Style.DIM
    reset = Style.RESET_ALL

    def __str__(self) -> str:
        """Return the ANSI style sequence as a string."""
        return str(self.value)


class ANIM(str, Enum):
    """Defines ANSI escape sequences for screen control.

    Used to clear the screen or lines during interactive rendering loops.
    """
    clear = "\033[J"
    clear_screen = "\033[2J\033[H"

    def __str__(self) -> str:
        """Return the ANSI escape sequence as a string."""
        return self.value


class DISPLAY_MODE(str, Enum):
    """Enumerates the available visualization modes.

    Attributes:
        ascii: Standard rendering using block characters and ANSI colors.
        simple: Simplified rendering using single characters (debugging).
        emoji: Graphical rendering using emoji squares.
    """
    ascii = "ascii"
    simple = "simple"
    emoji = "emoji"

    def __str__(self) -> str:
        """Return the mode identifier as a string."""
        return self.value


class ALGO_MODE(str, Enum):
    """Enumerates the available generation algorithms.

    Attributes:
        rb: Recursive Backtracking algorithm.
        hunt_kill: Hunt and Kill algorithm.
    """
    rb = "rb"
    hunt_kill = "huntandkill"

    def __str__(self) -> str:
        """Return the algorithm identifier as a string."""
        return self.value
