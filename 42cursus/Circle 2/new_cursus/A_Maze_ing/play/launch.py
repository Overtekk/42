# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  launch.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/07 08:05:31 by roandrie        #+#    #+#               #
#  Updated: 2026/02/10 14:33:58 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Interactive maze game launcher and controller.

This module serves as the entry point for the "play" mode. It initializes
the game environment based on a configuration file, prompts the user to
select a play mode, and enters the main interactive loop where keyboard inputs
control the character.
"""

import sys
import readchar

from time import sleep
from colorama import Cursor

from maze import (MazeConfig, MazeGenerator, MazeConfigError,
                  MazeGenerationError)
from maze.maze_customization import (MAZE, STYLE, COLORS, ANIM, DISPLAY_MODE)
from enemy import Enemy

CURSOR_HIDE = "\033[?25l"
CURSOR_SHOW = "\033[?25h"


def launch_game() -> None:
    """Initializes the game environment and selects the game mode.

    Attempts to load the configuration from 'play/config.txt'. If successful,
    it prompts the user to choose the game mode, generates the maze
    accordingly, and passes control to the `play` loop.

    Catches and logs configuration or generation errors to stderr to ensure
    a clean exit on failure.
    """
    try:
        maze_configuration = MazeConfig.from_config_file("play/config.txt")

        maze = MazeGenerator(maze_configuration)

        print(f"{COLORS.magenta}{STYLE.bright}\nChoose gamemode:")
        print(f"{COLORS.lightcyan}1. Normal")
        print(f"{COLORS.lightcyan}2. Fog of war")
        print(f"{COLORS.lightcyan}3. Hunted{STYLE.reset}")

        while True:
            user_choice = input(f"{COLORS.lightgreen}Choice (1-3): "
                                f"{COLORS.reset}")
            try:
                choice = int(user_choice)
                if 1 <= choice <= 3:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f"{COLORS.red}❌ Error!{COLORS.reset}", end="",
                      flush=True)
                print(Cursor.UP(1) + "\r" + ANIM.clear, end="")

        if choice == 1:
            gamemode = "normal"
            print(f"{COLORS.green}✅ Launching 'normal play mode'\n")
            sleep(1)
            maze.maze_generator(rendering=True)
        elif choice == 2:
            gamemode = "fow"
            print(f"{COLORS.green}✅ Launching 'fog of war play mode'\n")
            sleep(1)
            print(ANIM.clear_screen, end="")
            maze.maze_generator(rendering=False)
        else:
            gamemode = "enemy"
            print(f"{COLORS.green}✅ Launching 'hunted play mode'\n")
            sleep(1)
            print(ANIM.clear_screen, end="")
            maze.maze_generator(rendering=True)

    except (FileNotFoundError, ValueError, MazeConfigError,
            MazeGenerationError) as e:
        print(f"{type(e).__name__}: {e}", file=sys.stderr)

    play(maze, gamemode)


def play(maze: "MazeGenerator", gamemode: str) -> None:
    """Executes the main interactive game loop.

    Captures keyboard input (WASD) to move the player, performs collision
    detection against walls and obstacles, and updates the terminal display.

    Args:
        maze: The `MazeGenerator` instance containing the grid and
              logic to be played.
        gamemode: A string indicating the active mode.
                  If "fow" (Fog of War) is selected, only the surrounding of
                  the player is rendered as he walk throught.
    """
    print(CURSOR_HIDE, end="", flush=True)
    player_pos = [maze.entry_x, maze.entry_y]
    exit_pos = [maze.exit_x, maze.exit_y]
    steps = 0
    obs_to_render = [
                    (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
                    (-2, 0),  (-1, 0), (1, 0),  (2, 0),
                    (-2, 1),  (-1, 1),  (0, 1),  (1, 1),  (2, 1)
                    ]

    if gamemode == "enemy":
        enemy = Enemy(maze)
        enemy.spawn()
        print(Cursor.POS((enemy.enemy_x * maze.step_x) + 1,
              enemy.enemy_y + maze.y_offset) + f"{enemy.display_enemy}",
              end="", flush=True)

    display_text(maze, steps)

    def render_fow(pos_x: int, pos_y: int) -> None:
        """Renders the visible area around the player (Fog of War)."""
        for dir_x, dir_y in obs_to_render:
            x, y = (pos_x + dir_x), (pos_y + dir_y)

            if (x, y) in maze.maze:
                curs_x = (x * maze.step_x) + 1
                curs_y = y + maze.y_offset

                if maze.display == DISPLAY_MODE.emoji:
                    if maze.maze[(x, y)] == MAZE.wall:
                        print(Cursor.POS(curs_x, curs_y) +
                              f"{maze.visual_wall}{COLORS.reset}", end="",
                              flush=True)
                    elif maze.maze[(x, y)] == MAZE.fortytwo:
                        print(Cursor.POS(curs_x, curs_y) +
                              f"{maze.visual_ft}{COLORS.reset}", end="",
                              flush=True)
                    elif maze.maze[(x, y)] == MAZE.exit:
                        print(Cursor.POS(curs_x, curs_y) +
                              f"{maze.visual_exit}{COLORS.reset}", end="",
                              flush=True)
                else:
                    if maze.maze[(x, y)] == MAZE.wall:
                        print(Cursor.POS(curs_x, curs_y) +
                              f"{maze.color_wall}{maze.visual_wall}"
                              f"{COLORS.reset}", end="", flush=True)
                    elif maze.maze[(x, y)] == MAZE.fortytwo:
                        print(Cursor.POS(curs_x, curs_y) +
                              f"{maze.color_ft}{maze.visual_wall}"
                              f"{COLORS.reset}", end="", flush=True)
                    elif maze.maze[(x, y)] == MAZE.exit:
                        print(Cursor.POS(curs_x, curs_y) +
                              f"{maze.color_exit}{maze.visual_wall}"
                              f"{COLORS.reset}", end="", flush=True)

    if gamemode == "fow":
        render_fow(player_pos[0], player_pos[1])

        px_screen_entry = (player_pos[0] * maze.step_x) + 1
        py_screen_entry = player_pos[1] + maze.y_offset
        px_screen_exit = (exit_pos[0] * maze.step_x) + 1
        py_screen_exit = exit_pos[1] + maze.y_offset
        if maze.display == DISPLAY_MODE.emoji:
            print(Cursor.POS(px_screen_entry, py_screen_entry) +
                  f"{maze.visual_entry}", end="", flush=True)
            print(Cursor.POS(px_screen_exit, py_screen_exit) +
                  f"{maze.visual_exit}", end="", flush=True)
        else:
            print(Cursor.POS(px_screen_entry, py_screen_entry) +
                  f"{COLORS.magenta}{maze.visual_wall}{COLORS.reset}",
                  end="", flush=True)
            print(Cursor.POS(px_screen_exit, py_screen_exit) +
                  f"{COLORS.red}{maze.visual_wall}{COLORS.reset}",
                  end="", flush=True)

    while True:
        old_x, old_y = player_pos[0], player_pos[1]
        new_x, new_y = old_x, old_y

        k = readchar.readkey()

        if k == 'w':
            new_y = old_y - 1
        elif k == 's':
            new_y = old_y + 1
        elif k == 'a':
            new_x = old_x - 1
        elif k == 'd':
            new_x = old_x + 1
        elif k == 'e':
            print(Cursor.POS(1, maze.height + maze.y_offset + 3) +
                  f"{COLORS.red}Goodbye 👋{COLORS.reset}")
            print(CURSOR_SHOW, end="", flush=True)
            break

        if (new_x, new_y) != (old_x, old_y):
            if maze.maze[(new_x, new_y)] in (MAZE.wall, MAZE.fortytwo):
                new_x, new_y = old_x, old_y
                if gamemode == "fow":
                    render_fow(old_x, old_y)
                continue

            else:
                maze.maze[(old_x, old_y)] = MAZE.empty
                player_pos[0], player_pos[1] = new_x, new_y
                maze.maze[(new_x, new_y)] = MAZE.entry
                maze.entry_x, maze.entry_y = new_x, new_y

                steps += 1
                display_text(maze, steps)

                curs_old_x = (old_x * maze.step_x) + 1
                curs_old_y = old_y + maze.y_offset
                curs_new_x = (new_x * maze.step_x) + 1
                curs_new_y = new_y + maze.y_offset

                if maze.display == DISPLAY_MODE.emoji:
                    print(Cursor.POS(curs_old_x, curs_old_y) +
                          f"{maze.visual_empty}{COLORS.reset}", end="",
                          flush=True)
                    print(Cursor.POS(curs_new_x, curs_new_y) +
                          f"{maze.visual_entry}{COLORS.reset}", end="",
                          flush=True)

                if maze.display in (DISPLAY_MODE.ascii, DISPLAY_MODE.simple):
                    print(Cursor.POS(curs_old_x, curs_old_y) +
                          f"{maze.visual_empty}{COLORS.reset}", end="",
                          flush=True)
                    print(Cursor.POS(curs_new_x, curs_new_y) +
                          f"{COLORS.magenta}{maze.visual_wall}{COLORS.reset}",
                          end="", flush=True)

                if gamemode == "fow":
                    render_fow(old_x, old_y)

                if gamemode == "enemy":
                    if (enemy.enemy_x == maze.exit_x and
                            enemy.enemy_y == maze.exit_y):
                        old_enemy_x = enemy.enemy_x
                        old_enemy_y = enemy.enemy_y
                        if maze.display == DISPLAY_MODE.emoji:
                            print(Cursor.POS((old_enemy_x * maze.step_x) + 1,
                                  old_enemy_y + maze.y_offset) +
                                  f"{maze.visual_exit}{COLORS.reset}", end="",
                                  flush=True)
                        else:
                            print(Cursor.POS((old_enemy_x * maze.step_x) + 1,
                                  old_enemy_y + maze.y_offset) +
                                  f"{COLORS.red}{maze.visual_wall}"
                                  f"{COLORS.reset}", end="", flush=True)
                    else:
                        print(Cursor.POS((enemy.enemy_x * maze.step_x) + 1,
                              enemy.enemy_y + maze.y_offset) +
                              f"{maze.visual_empty}{COLORS.reset}",
                              end="", flush=True)

                    enemy.move(new_x, new_y)

                    print(Cursor.POS((enemy.enemy_x * maze.step_x) + 1,
                          enemy.enemy_y + maze.y_offset) +
                          f"{enemy.display_enemy}", end="", flush=True)

        if gamemode == "enemy":
            if (new_x == enemy.enemy_x and new_y == enemy.enemy_y):
                print(Cursor.POS(1, maze.height + maze.y_offset + 3) +
                      f"{COLORS.red}Fail! The dino ate you.{COLORS.reset}")
                print(CURSOR_SHOW, end="", flush=True)
                break

        if (new_x == maze.exit_x and new_y == maze.exit_y):
            print(Cursor.POS(1, maze.height + maze.y_offset + 3) +
                  f"{COLORS.lightgreen}🎆🎆 GG! 🎆🎆{COLORS.reset}")
            print(CURSOR_SHOW, end="", flush=True)
            break


def display_text(maze: "MazeGenerator", steps: int) -> None:
    """Render the status text below the maze.

    Displays the quit instruction and the current step count. The text is
    centered horizontally relative to the maze width and positioned on the
    line immediately following the maze bottom margin.

    Args:
        maze: The `MazeGenerator` instance used to calculate positioning.
        steps: The current number of steps taken by the player.
    """
    if steps > 0:
        text_infos = f"Move: 'WASD', Quit: 'E' | Steps: {steps}"
    else:
        text_infos = f"Move: 'WASD', Quit: 'E' | Step: {steps}"
    line_y = maze.height + maze.y_offset + 1

    visual_width = maze.width // 2
    padding = " " * max(0, (visual_width - len(text_infos)) // 2)

    print(Cursor.POS(1, line_y) + f"{padding}{text_infos}{STYLE.reset}",
          end="", flush=True)


if __name__ == "__main__":
    launch_game()
