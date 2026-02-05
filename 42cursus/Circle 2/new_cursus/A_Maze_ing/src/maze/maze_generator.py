# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_generator.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 12:07:28 by roandrie        #+#    #+#               #
#  Updated: 2026/02/05 10:04:54 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

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
from src.maze.output import maze_output


class MazeGenerator():

    txt_white = f"{COLORS.white}{STYLE.bright}"

    def __init__(self, config: MazeConfig) -> None:
        # Import config
        self.cfg = config

        # Maze parameters
        self.width = config.width
        self.height = config.height
        self.entry_coord = config.entry
        self.exit_coord = config.exit
        self.output_file = config.output_file
        self.perfect = config.perfect
        self.seed = config.seed
        self.display = config.display
        self.algorithm = config.algorithm

        # Generate seed if user didn't give it.
        if self.seed is None:
            self._generate_random_seed()

        # Correct coordinates for the different algorithms
        self._correcting_coords()

        # Unpacking coords.
        entry_x, entry_y = self.entry_coord
        exit_x, exit_y = self.exit_coord
        self.entry_x, self.entry_y = entry_x, entry_y
        self.exit_x, self.exit_y = exit_x, exit_y

        self.fourtytwo_coord = ft_patt(self.width, self.height)

        self.maze: Dict[Tuple[int, int], Any] = {}

        # Defaults color and visual
        self.color_wall = COLORS.lightwhite
        self.color_ft = COLORS.yellow
        self.color_entry = COLORS.magenta
        self.color_exit = COLORS.red
        self.color_path = COLORS.cyan

        self.visual_empty: str | VISUAL
        self.visual_wall: str | VISUAL

        # Configure rendering based on display
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
        if (rendering and self.display in (DISPLAY_MODE.ascii,
                                           DISPLAY_MODE.emoji)
                                           and regen is False):
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

        # Start the random sequence based on the seed given/generated
        if regen is False:
            random.seed(self.seed)
        else:
            self._generate_random_seed()
            random.seed(self.seed)

        self._fill_maze()

        if rendering:
            self.print_maze()

        self._choose_algo(rendering)

        # Check if the maze can be solved
        from src.maze.maze_solver import MazeSolver
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
            print(Cursor.POS(1, self.height + self.y_offset))

    def get_maze_parameters(self) -> Dict[str, Any]:
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
            time.sleep(0.001)

    def print_maze(self) -> None:
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

    def _choose_algo(self, rendering: bool) -> None:
        if self.algorithm == ALGO_MODE.rb and self.perfect:
            recursive_backtracking(self, rendering)
        elif self.algorithm == ALGO_MODE.rb and self.perfect is False:
            recursive_backtracking(self, rendering)
            break_random_walls(self, rendering)

        elif self.algorithm == ALGO_MODE.hunt_kill:
            hunt_and_kill(self, rendering)

    def _correcting_coords(self) -> None:
        if self.entry_coord[0] == 0:
            self.entry_coord = (self.entry_coord[0] + 1, self.entry_coord[1])
            self.exit_coord = (self.exit_coord[0] + 1, self.exit_coord[1])
            self.width += 1

        if self.entry_coord[1] == 0:
            self.entry_coord = (self.entry_coord[0], self.entry_coord[1] + 1)
            self.exit_coord = (self.exit_coord[0], self.exit_coord[1] + 1)
            self.height += 1

        if self.algorithm in (ALGO_MODE.rb, ALGO_MODE.hunt_kill):
            if self.width % 2 == 0:
                self.width += 1
            if self.height % 2 == 0:
                self.height += 1

        if self.exit_coord[0] >= self.width - 1:
            self.exit_coord = (self.width - 2, self.exit_coord[1])
        if self.exit_coord[1] >= self.height - 1:
            self.exit_coord = (self.exit_coord[0], self.height - 2)

    def _fill_maze(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                if x == self.entry_x and y == self.entry_y:
                    self.maze[(x, y)] = MAZE.entry
                elif x == self.exit_x and y == self.exit_y:
                    self.maze[(x, y)] = MAZE.exit
                elif (x, y) in self.fourtytwo_coord:
                    self.maze[(x, y)] = MAZE.fortytwo
                else:
                    self.maze[(x, y)] = MAZE.wall

    def _customize_maze_walls_color(self) -> str:
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

        user_choice = input(f"{self.txt_white}Enter choice: ")
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
        random_seed = ''.join(random.choices(string.ascii_letters +
                                             string.digits,
                                             k=random.randint(1, 101)))
        self.seed = random_seed

    def _apply_wall_color(self, choice: int, rotate: bool = False) -> None:
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
        algo = {
            1: ALGO_MODE.rb,
            2: ALGO_MODE.hunt_kill
        }

        self.algorithm = algo.get(choice, ALGO_MODE.rb)
