# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_generator.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 12:07:28 by roandrie        #+#    #+#               #
#  Updated: 2026/01/24 12:52:58 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random
import string
import time

from typing import Any, Dict, Optional, Set, Tuple
from colorama import Fore, Style


class MazeGenerator():

    def __init__(self, width: int, height: int, entry: Tuple[int, int],
                 exit: Tuple[int, int], output_file: str, perfect: bool,
                 seed: Optional[str | int] = None) -> None:
        # Check arguments first
        self._check_arg(width, 'width')
        self._check_arg(height, 'height')
        self._check_arg(entry, 'entry')
        self._check_arg(exit, 'exit')
        self._check_arg(output_file, 'output_file')
        self._check_arg(perfect, 'perfect')

        self.width = width
        self.height = height
        self.entry_coord = entry
        self.exit_coord = exit
        self.output_file = output_file
        self.perfect = perfect
        self.seed = seed
        # Generate seed if user didn't give it.
        if self.seed is None:
            self._generate_random_seed()

        # Unpacking coords.
        entry_x, entry_y = self.entry_coord
        exit_x, exit_y = self.exit_coord
        self.entry_x = entry_x
        self.entry_y = entry_y
        self.exit_x = exit_x
        self.exit_y = exit_y

        self.maze: Dict[Tuple[int, int], str] = {}
        self.empty = ' '
        self.border = f'{Fore.WHITE}\u2588\u2588'
        self.wall = f'{Fore.GREEN}\u2588\u2588'
        self.entry = f'{Fore.MAGENTA}\u2588\u2588'
        self.exit = f'{Fore.RED}\u2588\u2588'
        self.fourty_two = f'{Fore.LIGHTWHITE_EX}\u2588\u2588'

        self._validate_parameters()

    def maze_generator(self) -> None:
        loading = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

        print("\nGenerating Maze...", end='')

        for _ in range(2):
            for char in loading:
                print(f"{Fore.WHITE} {Style.BRIGHT} \r{char} Generating "
                      "Maze...", end="", flush=True)
                time.sleep(0.1)
        print("\rMaze Generated:       ")
        print(Style.RESET_ALL)

        self._generated_maze()
        self._print_42()
        self._print_maze()

    def get_maze_parameters(self) -> Dict[str, Any]:
        return {
            'Width': self.width,
            'Height': self.height,
            'Entry Coordinates': self.entry_coord,
            'Exit Coordinates': self.exit_coord,
            'Output file': self.output_file,
            'Perfect Maze?': self.perfect,
            'Seed': self.seed
        }

    def _check_arg(self, value: Any, name: str) -> None:
        rules: Dict[str, Any] = {
                'width': int,
                'height': int,
                'entry': tuple,
                'exit': tuple,
                'output_file': str,
                'perfect': bool,
                'seed': (str, int, type(None))
            }
        if name in rules:
            required_type = rules[name]
            if not isinstance(value, required_type):
                raise ValueError(f"'{name}' has wrong type. Expected "
                                 f"{required_type}")

    def _validate_parameters(self) -> None:
        if not (0 <= self.entry_x < self.width and 0 <= self.entry_y <
                self.height):
            raise ValueError("Entry cannot be outside walls.")
        if not (0 <= self.exit_x < self.width and 0 <= self.exit_y <
                self.height):
            raise ValueError("Exit cannot be outside walls.")

        if self.entry_coord == self.exit_coord:
            raise ValueError("Entry and Exit cannot be at the exact same "
                             "position.")

        if self.width < 7 or self.height < 5:
            raise ValueError("Dimensions too small for the '42' pattern.")

        coords_fourty_two = self._get_42_pattern(self.width, self.height)

        if self.entry_coord in coords_fourty_two:
            raise ValueError("Can't place Entry here. Reserved to '42'")
        if self.exit_coord in coords_fourty_two:
            raise ValueError("Can't place Exit here. Reserved to '42'")

    def _generate_random_seed(self) -> None:
        random_n = random.randint(0, 50)
        if random_n == 25:
            suffix = 'roandrie'
        elif random_n == 35:
            suffix = 'rruiz'
        else:
            suffix = ''
        length = random.randint(1, 101)
        random_seed = ''.join(random.choices(string.ascii_letters +
                                             string.digits, k=length))
        random_seed += suffix
        self.seed = random_seed

    @staticmethod
    def _get_42_pattern(width: int, height: int) -> Set[Tuple[int, int]]:
        center_x = width // 2
        center_y = height // 2

        pattern = {
            (center_x - 3, center_y), (center_x - 3, center_y - 1),
            (center_x - 3, center_y - 2), (center_x - 1, center_y),
            (center_x - 2, center_y), (center_x - 1, center_y + 1),
            (center_x - 1, center_y + 2), (center_x + 3, center_y + 2),
            (center_x + 2, center_y + 2), (center_x + 1, center_y + 2),
            (center_x + 1, center_y), (center_x + 1, center_y + 1),
            (center_x + 2, center_y), (center_x + 3, center_y),
            (center_x + 3, center_y - 1), (center_x + 3, center_y - 2),
            (center_x + 2, center_y - 2), (center_x + 1, center_y - 2)
        }
        return pattern

    def _print_42(self) -> None:
        pattern_coords = self._get_42_pattern(self.width, self.height)

        for coord in pattern_coords:
            if coord in self.maze:
                self.maze[coord] = self.fourty_two

    def _print_maze(self) -> None:
        total_cases = self.width * self.height
        if total_cases < 600:
            animate_char_by_char = True
        else:
            animate_char_by_char = False

        if animate_char_by_char:
            delay = 1.5 / total_cases
        else:
            delay = 1.0 / self.height

        print(self.border * (self.width + 2), flush=True)

        for y in range(self.height):
            print(self.border, end='', flush=True)

            if animate_char_by_char:
                for x in range(self.width):
                    print(self.maze[(x, y)], end='', flush=True)
                    time.sleep(delay)
            else:
                raw_line = "".join([self.maze[(x, y)] for x in
                                    range(self.width)])
                print(raw_line, end='', flush=True)
                time.sleep(delay)

            print(self.border, flush=True)

        print(self.border * (self.width + 2), flush=True)
        print(Style.RESET_ALL)

    def _generated_maze(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                self.maze[(x, y)] = self.wall

                if self.entry_x == x and self.entry_y == y:
                    self.maze[(x, y)] = self.entry
                if self.exit_x == x and self.exit_y == y:
                    self.maze[(x, y)] = self.exit
