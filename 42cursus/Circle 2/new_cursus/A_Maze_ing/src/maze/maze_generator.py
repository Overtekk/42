# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_generator.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 12:07:28 by roandrie        #+#    #+#               #
#  Updated: 2026/02/11 15:03:37 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Maze generation core.

This module provides the `MazeGenerator` class which builds a maze
representation and renders it to terminal or writes it to an output
file. It coordinates display formatting, algorithm selection and
seeded random generation.
"""

import random
import string
import time

from typing import Any, Dict, Tuple
from colorama import Cursor

from .maze_config import MazeConfig
from .maze_errors import MazeGenerationError
from .maze_fortytwo_pattern import get_fortytwo_pattern as ft_patt
from .maze_customization import (COLORS, STYLE, ANIM, DISPLAY_MODE, ALGO_MODE,
                                 MAZE, VISUAL, EMOJI)
from .algorithms import (recursive_backtracking, hunt_and_kill,
                         break_random_walls)
from .output import maze_output


class MazeGenerator():
    """Manages the lifecycle of a maze: configuration, generation, and
       rendering.

    This class serves as the central hub for the application. It maintains
    the grid state (walls, paths, entry, exit), handles the coordinate
    adjustments required by generation algorithms, and manages the
    visual output to the terminal.

    Attributes:
        cfg (MazeConfig): The configuration object containing user preferences.
    """

    # Global variable to render text in bright white.
    txt_white = f"{COLORS.white}{STYLE.bright}"

    def __init__(self, config: MazeConfig) -> None:
        """Initialize the generator from a `MazeConfig`.

        If no seed is provided, generate a random one and start the
        randomization based on it. Correct the coordinates (entry, exit, grid)
        for no errors in the algorithm generation. And create the variable maze
        that will contain all the maze informations.
        Scales the dimensions from a cell-based grid to a block-based grid
        (2N + 1) to accommodate walls as physical coordinates.

        Args:
            config: MazeConfig containing all the config validate by the
            MazeConfig class.
        """
        # Import config.
        self.cfg = config
        # Export config into the class.
        self.width = config.width * 2 + 1
        self.height = config.height * 2 + 1
        self.entry_coord = (config.entry[0] * 2 + 1, config.entry[1] * 2 + 1)
        self.exit_coord = (config.exit[0] * 2 + 1, config.exit[1] * 2 + 1)
        self.output_file = config.output_file
        self.perfect = config.perfect
        self.seed = config.seed
        self.display = config.display
        self.algorithm = config.algorithm

        # Generate seed if user didn't give it and launch the random sequence.
        if self.seed is None:
            self._generate_random_seed()
        random.seed(self.seed)

        # Correct coordinates, entry and exit for the algorithms.
        self._correcting_coords()

        # Unpacking coords.
        entry_x, entry_y = self.entry_coord
        exit_x, exit_y = self.exit_coord
        self.entry_x, self.entry_y = entry_x, entry_y
        self.exit_x, self.exit_y = exit_x, exit_y

        # Check the 42 pattern.
        self.fourtytwo_coord = ft_patt(self.width, self.height)

        # Create the maze dict to store all informations.
        self.maze: Dict[Tuple[int, int], Any] = {}

        # Defaults color and visual.
        self.color_wall = COLORS.lightwhite
        self.color_ft = COLORS.yellow
        self.color_entry = COLORS.magenta
        self.color_exit = COLORS.red
        self.color_path = COLORS.cyan

        self.visual_empty: str | VISUAL
        self.visual_wall: str | VISUAL | EMOJI

        # Configure rendering based on display.
        if self.display == DISPLAY_MODE.ascii:
            self.visual_empty = VISUAL.empty_block
            self.visual_wall = VISUAL.block
            self.step_x = 2

        elif self.display == DISPLAY_MODE.emoji:
            self.visual_empty = VISUAL.empty_block
            self.visual_wall = EMOJI.white
            self.visual_ft = EMOJI.ft_1
            self.visual_entry = EMOJI.magenta
            self.visual_exit = EMOJI.red
            self.visual_path = EMOJI.blue
            self.step_x = 2

        else:
            self.visual_empty = VISUAL.empty
            self.visual_wall = "#"
            self.step_x = 1

    def maze_generator(self, rendering: bool = False,
                       regen: bool = False) -> None:
        """Orchestrates the full maze generation workflow.

        This method executes the pipeline in the following order:
        1. Handles UI customization (colors) if rendering is enabled.
        2. Initializes the grid.
        3. Executes the selected generation algorithm.
        4. Validates that the maze is solvable.
        5. Performs post-processing (e.g., breaking extra walls for
           'imperfect' mazes).
        6. Writes the result to the output file.

        Args:
            rendering: If True, displays real-time animations and menus
                       to the terminal.
            regen: If True, generates a new random seed before running;
                   otherwise, uses the existing configuration seed.

        Raises:
            MazeGenerationError: If the generated maze is theoretically
                                 unsolvable.
        """
        if (rendering and
            self.display in (DISPLAY_MODE.ascii, DISPLAY_MODE.emoji) and
                regen is False):
            print(ANIM.clear, end="")
            while True:
                user_choice = self._customize_maze_walls_color()
                if user_choice == "ok":
                    break

        if regen is False:
            loading = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
            text_generating = " Generating Maze..."

        text_generated = "-Maze Generated-"
        if self.algorithm == ALGO_MODE.rb:
            text_algo_display = "Mode: recursive backtracking"
        elif self.algorithm == ALGO_MODE.hunt_kill:
            text_algo_display = "Mode: hunt and kill"
        if rendering:
            text_algo_display += f" | Display: {self.display}"

        # Align cursor based of lines of texts writted
        self.y_offset = 3

        # Clear screen to render the maze if rendering is True
        if rendering:
            print(ANIM.clear_screen, end="")

        # Calculate based on the width to center the text
        visual_width = self.width
        if rendering:
            if self.display in (DISPLAY_MODE.ascii, DISPLAY_MODE.emoji):
                visual_width = self.width
            else:
                visual_width = self.width // 2
        if regen is False:
            filling = " " * max(0, ((visual_width -
                                     (len(text_generating) // 2))))

        # Print the loading text
        if regen is False:
            for _ in range(2):
                for char in loading:
                    print(f"\r{filling}{self.txt_white}{char}"
                          f"{text_generating}", end="", flush=True)
                    time.sleep(0.1)

        filling = " " * max(0, ((visual_width - (len(text_generated) // 2))))
        print(f"\r{filling}{text_generated}    ")

        filling = " " * max(0, ((visual_width -
                                 (len(text_algo_display) // 2))))
        print(f"\r{filling}{text_algo_display}{STYLE.reset}")

        # Regenerate a maze if the maze is re-generated.
        if regen is True:
            self._generate_random_seed()
            random.seed(self.seed)

        self._fill_maze()

        if rendering:
            self.print_maze()

        self._choose_algo(rendering)

        # Check if the maze can be solved
        from .maze_solver import MazeSolver
        solver = MazeSolver(self)
        solver.find_path()
        if len(solver.path) <= 0:
            if rendering:
                print(Cursor.POS(1, self.height + self.y_offset))
            raise MazeGenerationError("This maze cannot be resolve. Omg, "
                                      "this is so rare!")

        maze_output(self, solver.path)

        # Put the cursor at the bottom of the screen
        if rendering:
            print(Cursor.POS(1, self.y_offset), end="")
            self.print_maze()
            if (len(self.fourtytwo_coord) <= 0):
                print(f"{COLORS.red}{STYLE.bright}ERROR: '42' pattern can't be"
                      f" printed!{STYLE.reset}")
            print(Cursor.POS(1, self.height + self.y_offset))

    def get_maze_parameters(self) -> Dict[str, Any]:
        """Retrieves the current configuration state of the generator.

        Returns:
            Dict[str, Any]: A dictionary containing key parameters like
                            dimensions, seed, algorithm, and file paths.
        """
        return {
            'Width': self.width,
            'Height': self.height,
            'Entry Coordinates': self.entry_coord,
            'Exit Coordinates': self.exit_coord,
            'Output file': self.output_file,
            'Perfect Maze?': self.perfect,
            'Seed': self.seed,
            'Display mode': self.display,
            'Algorithm': self.algorithm
        }

    def break_wall(self, x: int, y: int, rendering: bool) -> None:
        """Transforms a wall cell into an empty path cell.

        Updates the internal grid state and, if rendering is enabled,
        updates the specific character on the terminal screen without
        redrawing the entire maze.

        Args:
            x: The grid X coordinate of the wall to remove.
            y: The grid Y coordinate of the wall to remove.
            rendering: If True, visualizes the wall removal immediately for
                       animation.
        """
        self.maze[(x, y)] = MAZE.empty

        if rendering:
            curs_x = (x * self.step_x) + 1
            curs_y = y + self.y_offset

            symbol = self.visual_empty
            color = COLORS.reset

            if x == self.entry_x and y == self.entry_y:
                if self.display == DISPLAY_MODE.emoji:
                    symbol = self.visual_entry
                else:
                    symbol = self.visual_wall
                    color = self.color_entry

            elif x == self.exit_x and y == self.exit_y:
                if self.display == DISPLAY_MODE.emoji:
                    symbol = self.visual_exit
                else:
                    symbol = self.visual_wall
                    color = self.color_entry

            print(Cursor.POS(curs_x, curs_y) + f"{color}{symbol}"
                  f"{COLORS.reset}", end="", flush=True)
            if self.height < 100 or self.width < 100:
                time.sleep(0.001)

    def print_maze(self) -> None:
        """Renders the current state of the entire maze to the terminal.

        Iterates through every cell in the grid and prints the
        appropriate symbol (ASCII or Emoji) and color code based on the
        current display settings.
        """
        for y in range(self.height):
            for x in range(self.width):
                cell = self.maze[(x, y)]
                current_color = COLORS.reset
                symbol_to_print = self.visual_empty

                if x == self.entry_x and y == self.entry_y:
                    if self.display == DISPLAY_MODE.emoji:
                        symbol_to_print = self.visual_entry
                    else:
                        symbol_to_print = self.visual_wall
                        current_color = self.color_entry

                elif x == self.exit_x and y == self.exit_y:
                    if self.display == DISPLAY_MODE.emoji:
                        symbol_to_print = self.visual_exit
                    else:
                        symbol_to_print = self.visual_wall
                        current_color = self.color_exit

                elif cell == MAZE.fortytwo:
                    if self.display == DISPLAY_MODE.emoji:
                        symbol_to_print = self.visual_ft
                    else:
                        symbol_to_print = self.visual_wall
                        current_color = self.color_ft

                elif cell == MAZE.wall:
                    current_color = self.color_wall
                    symbol_to_print = self.visual_wall

                print(f"{current_color}{symbol_to_print}{COLORS.reset}",
                      end="")
            print()

    def _is_breakable(self, x: int, y: int) -> bool:
        """Checks if the wall at the given coordinates is breakable.

        This method checks adjacent cells (up, down, left, right).
        If at least one of them is a target (empty, entry, or exit),
        the wall is considered breakable.

        Args:
            x (int): The x-coordinate of the wall to check.
            y (int): The y-coordinate of the wall to check.

        Returns:
            bool: True if the wall can be broken, False otherwise.
        """
        targets = (MAZE.empty, MAZE.entry, MAZE.exit)
        if ((self.maze[(x + 1, y)] in targets or
            self.maze[(x - 1, y)] in targets or
            self.maze[(x, y + 1)] in targets or
                self.maze[(x, y - 1)] in targets)):
            return True
        return False

    def _choose_algo(self, rendering: bool) -> None:
        """Dispatches the generation process to the selected algorithm.

        Based on `self.algorithm` and `self.perfect`, this method calls
        the appropriate external function (Recursive Backtracking or
        Hunt-and-Kill).

        Args:
            rendering: Passed to the algorithm functions to enable or
                disable real-time visualization during generation.
        """
        if self.algorithm == ALGO_MODE.rb and self.perfect:
            recursive_backtracking(self, rendering)
        elif self.algorithm == ALGO_MODE.rb and self.perfect is False:
            recursive_backtracking(self, rendering)
            break_random_walls(self, rendering)

        elif self.algorithm == ALGO_MODE.hunt_kill:
            hunt_and_kill(self, rendering)
            if not self.perfect:
                from .algorithms.hunt_and_kill import break_walls_hak
                break_walls_hak(self, rendering)

    def _correcting_coords(self) -> None:
        """Validates and clamps entry/exit points to the nearest valid passage.

        Ensures coordinates are odd-indexed to reside within passage blocks
        and prevents spawning inside the reserved '42' pattern or outside
        the grid boundaries.
        """

        def clamp_to_odd(value: int, max_value: int) -> int:
            """Adjusts a coordinate to the nearest odd index within grid
               bounds.

            This utility ensures that coordinates provided by the user or
            generated by algorithms always land on a passage (odd block)
            and never on a wall (even block) or outside the grid.

            Args:
                value (int): The raw coordinate value to be adjusted.
                max_limit (int): The total size of the grid dimension
                                 (width or height).

            Returns:
                int: The closest valid odd coordinate within the maze passages.
            """
            if value < 1:
                return 1
            if value >= max_value - 1:
                last_index = max_value - 2

                if last_index % 2 == 0:
                    return last_index - 1
                return last_index
            if value % 2 == 0:
                return value + 1

            return value

        ent_x, ent_y = self.entry_coord
        ext_x, ext_y = self.exit_coord

        # Coords adjustments;
        self.entry_coord = (clamp_to_odd(ent_x, self.width),
                            clamp_to_odd(ent_y, self.height))
        self.exit_coord = (clamp_to_odd(ext_x, self.width),
                           clamp_to_odd(ext_y, self.height))

        # Security : if entry and exit are in the same place.
        if self.entry_coord == self.exit_coord:
            new_ext_x = clamp_to_odd(self.exit_coord[0] + 2, self.width)
            if new_ext_x == self.exit_coord[0]:
                new_ext_x = clamp_to_odd(self.exit_coord[0] - 2, self.width)
            self.exit_coord = (new_ext_x, self.exit_coord[1])

        # Avoid 42 pattern.
        ft_pattern = ft_patt(self.width, self.height)
        while self.exit_coord in ft_pattern:
            new_ext_y = clamp_to_odd(self.exit_coord[1] + 2, self.height)
            if new_ext_y == self.exit_coord[1]:
                new_ext_y = clamp_to_odd(self.exit_coord[1] - 4, self.height)
            self.exit_coord = (self.exit_coord[0], new_ext_y)

    def _fill_maze(self) -> None:
        """Initializes the grid with the starting state.

        Sets the entry, exit, and special '42' pattern cells to their
        respective types. All other cells are initialized as walls,
        ready to be carved by the generation algorithm.
        """
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.entry_coord:
                    self.maze[(x, y)] = MAZE.entry
                elif (x, y) == self.exit_coord:
                    self.maze[(x, y)] = MAZE.exit
                elif (x, y) in self.fourtytwo_coord:
                    self.maze[(x, y)] = MAZE.fortytwo
                else:
                    self.maze[(x, y)] = MAZE.wall

    def _customize_maze_walls_color(self) -> str:
        """Prompts the user to select a color scheme for the walls.

        Displays a menu of available colors (depending on whether ASCII
        or Emoji mode is active) and captures the user's input.

        Returns:
            str: Returns "ok" if a valid choice was made, otherwise
                returns an empty string (used for loop control in the
                caller).
        """
        print(f"{self.txt_white}Choose walls color:")

        if self.display == DISPLAY_MODE.ascii:
            print(f"{COLORS.white}1. White\t {COLORS.blue}3. Blue\t "
                  f"{COLORS.lightyellow}5. Yellow")
            print(f"{COLORS.magenta}2. Magenta\t {COLORS.cyan}4. Cyan\t "
                  f"{COLORS.green}6. Green")

        else:
            print(f"{COLORS.white}1. White\t {COLORS.blue}3. Blue\t "
                  f"{COLORS.lightyellow}5. Yellow")
            print(f"{COLORS.magenta}2. Magenta\t {COLORS.yellow}4. Brown\t "
                  f"{COLORS.green}6. Green")

        user_choice = input(f"{self.txt_white}Enter choice (1-6): ")
        try:
            choice = int(user_choice)

            if choice >= 1 and choice <= 6:
                print(Cursor.UP(4) + ANIM.clear, end="")
                self._apply_wall_color(choice)
                return "ok"
            else:
                raise ValueError

        except ValueError:
            print(f"{COLORS.red}Invalid choice. Choose between 1 and 6.",
                  end="", flush=True)
            time.sleep(1)
            print(Cursor.UP(5) + "\r" + ANIM.clear, end="")
        return ""

    def _generate_random_seed(self) -> None:
        """Generates a random alphanumeric seed string.

        Creates a random string containing letters and digits (length
        between 1 and 100) to serve as the seed for `random.seed()`.
        This ensures unique maze generation when no specific seed is
        provided by the user.
        """
        random_seed = ''.join(random.choices(string.ascii_letters +
                                             string.digits,
                                             k=random.randint(1, 101)))
        self.seed = random_seed

    def _apply_wall_color(self, choice: int, rotate: bool = False) -> None:
        """Applies a color theme or emoji set to the maze walls.

        Maps the user's numeric choice to specific ANSI color codes or
        Emoji constants defined in `maze_customization`.

        Args:
            choice: The user's menu selection index.
            rotate: Randomizes the color of special '42' pattern cells
                    if set to True.
        """
        color = {
            1: COLORS.lightwhite,
            2: COLORS.magenta,
            3: COLORS.blue,
            4: COLORS.cyan,
            5: COLORS.lightyellow,
            6: COLORS.lightgreen,
            7: COLORS.lightmagenta,
            8: COLORS.green,
            9: COLORS.lightblue
        }

        emoji = {
            1: EMOJI.white,
            2: EMOJI.magenta,
            3: EMOJI.blue,
            4: EMOJI.brown,
            5: EMOJI.yellow,
            6: EMOJI.green,
            7: EMOJI.red,
            8: EMOJI.orange
        }

        random_ft = {
            1: EMOJI.ft_1,
            2: EMOJI.ft_2,
        }

        # Apply user choice color for ascii
        if self.display == DISPLAY_MODE.ascii:
            self.color_wall = color.get(choice, COLORS.lightwhite)

            # Prevent the same color from wall-entry
            if choice == 2:
                self.color_entry = color.get(7, COLORS.lightmagenta)
            else:
                self.color_entry = color.get(2, COLORS.magenta)

            # Prevent the same color from wall-path solution
            if choice == 4:
                self.color_path = color.get(6, COLORS.lightgreen)
            else:
                self.color_path = color.get(4, COLORS.cyan)

        # Apply user choice color for emoji
        else:
            if choice == 9:
                choice = 8

            self.visual_wall = emoji.get(choice, EMOJI.white)

            # Prevent the same color from wall-entry
            if choice == 2:
                self.visual_entry = emoji.get(5, EMOJI.white)
            else:
                self.visual_entry = emoji.get(2, EMOJI.magenta)

            # Prevent the same color from wall-exit
            if choice == 7:
                self.visual_exit = emoji.get(8, EMOJI.orange)
            else:
                self.visual_exit = emoji.get(7, EMOJI.red)

            # Prevent the same color from wall-path solution
            if choice == 3:
                self.visual_path = emoji.get(6, EMOJI.brown)
            else:
                self.visual_path = emoji.get(3, EMOJI.blue)

        # Rotate the color of the 42
        if rotate:
            r = random.randint(0, 20)
            if r % 2 == 0:
                if self.display == DISPLAY_MODE.ascii:
                    rcolor = random.randint(1, 9)
                    if rcolor == choice:
                        self.color_ft = COLORS.lightblack
                    else:
                        self.color_ft = color.get(rcolor, COLORS.lightblack)

                if self.display == DISPLAY_MODE.emoji:
                    rcolor = random.randint(1, 2)
                    self.visual_ft = random_ft.get(rcolor, EMOJI.ft_1)

        if self.color_ft == self.color_wall:
            self.color_ft = COLORS.lightblack

    def _apply_algo_change(self, choice: int) -> None:
        """Updates the generation algorithm based on user input.

        Args:
            choice: The integer corresponding to the user's menu selection
                    (1 for Recursive Backtracking, 2 for Hunt and Kill).
        """
        algo = {
            1: ALGO_MODE.rb,
            2: ALGO_MODE.hunt_kill
        }

        self.algorithm = algo.get(choice, ALGO_MODE.rb)
