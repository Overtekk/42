# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_customization.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 16:35:27 by roandrie        #+#    #+#               #
#  Updated: 2026/02/05 09:33:54 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from enum import Enum

from colorama import Fore, Style


class VISUAL(str, Enum):
    block = "\u2588\u2588"
    empty_block = "  "
    empty = " "

    def __str__(self) -> str:
        return self.value


class MAZE(Enum):
    empty = 0
    entry = 3
    exit = 2
    wall = 1
    fortytwo = 4


class COLORS(Enum):
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
    bright = Style.BRIGHT
    dim = Style.DIM
    reset = Style.RESET_ALL

    def __str__(self) -> str:
        return str(self.value)


class ANIM(str, Enum):
    clear = "\033[J"
    clear_screen = "\033[2J\033[H"

    def __str__(self) -> str:
        return self.value


class DISPLAY_MODE(str, Enum):
    ascii = "ascii"
    simple = "simple"
    emoji = "emoji"

    def __str__(self) -> str:
        return self.value


class ALGO_MODE(str, Enum):
    rb = "rb"
    hunt_kill = "huntandkill"

    def __str__(self) -> str:
        return self.value
