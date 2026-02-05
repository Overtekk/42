# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_customization.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 16:35:27 by roandrie        #+#    #+#               #
#  Updated: 2026/02/05 13:23:14 by rruiz           ###   ########.fr        #
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
    """Terminal visual symbols used for maze rendering.

    These constants represent the characters or strings used to
    display walls and empty spaces depending on the selected
    `DISPLAY_MODE`.

    Attributes:
        block: Double-block character used for dense/full-block
            rendering.
        empty_block: Two spaces used for empty cells when a block
            visual is preferred.
        empty: Single space used for simple display mode.
    """
    block = "\u2588\u2588"
    empty_block = "  "
    empty = " "

    def __str__(self) -> str:
        return self.value


class MAZE(Enum):
    """Semantic cell types used in the internal maze grid.

    Values are small integers to keep memory and output compact.
    """
    empty = 0
    entry = 3
    exit = 2
    wall = 1
    fortytwo = 4


class COLORS(Enum):
    """Named terminal color codes used for printing the maze."""
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
        return str(self.value)


class EMOJI(str, Enum):
    """Emoji symbols used when `DISPLAY_MODE.emoji` is selected."""
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
        return self.value


class STYLE(Enum):
    """Terminal text style constants (bright/dim/reset)."""
    bright = Style.BRIGHT
    dim = Style.DIM
    reset = Style.RESET_ALL

    def __str__(self) -> str:
        return str(self.value)


class ANIM(str, Enum):
    """Small terminal animation and control sequences."""
    clear = "\033[J"
    clear_screen = "\033[2J\033[H"

    def __str__(self) -> str:
        return self.value


class DISPLAY_MODE(str, Enum):
    """Available rendering modes for the maze display."""
    ascii = "ascii"
    simple = "simple"
    emoji = "emoji"

    def __str__(self) -> str:
        return self.value


class ALGO_MODE(str, Enum):
    """Supported maze generation algorithms."""
    rb = "rb"
    hunt_kill = "huntandkill"

    def __str__(self) -> str:
        return self.value
