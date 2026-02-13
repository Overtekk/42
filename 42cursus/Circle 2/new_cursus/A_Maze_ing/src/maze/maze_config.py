# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_config.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 14:14:51 by roandrie        #+#    #+#               #
#  Updated: 2026/02/10 14:55:54 by rruiz           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Configuration management for the maze generator.

This module defines the data model for the application using Pydantic.
It handles parsing of the configuration file, type conversion, and deep
semantic validation (bounds checking, collisions with reserved patterns).
"""

from pathlib import Path
from typing import Any, Self, Tuple

from pydantic import (BaseModel, Field, ValidationError, field_validator,
                      model_validator)

from .maze_errors import MazeConfigError
from .maze_fortytwo_pattern import get_fortytwo_pattern as ft_patt


class MazeConfig(BaseModel):
    """Data model representing the runtime configuration.

    This class enforces strict typing and logical constraints on the
    maze parameters. It is typically instantiated via `from_config_file`.

    Attributes:
        width (int): Grid width (min: 3).
        height (int): Grid height (min: 3).
        entry (Tuple[int, int]): Coordinates (x, y) of the starting point.
        exit (Tuple[int, int]): Coordinates (x, y) of the ending point.
        output_file (str): Path for the output file (must end in .txt).
        perfect (bool): If True, generates a perfect maze (no loops).
        seed (str | int | None): Seed for the random number generator.
        display (str | None): Rendering mode ('ascii' or 'emoji').
        algorithm (str | None): Algorithm choice ('rb' or 'huntandkill').
    """
    width: int = Field(ge=3)
    height: int = Field(ge=3)
    entry: Tuple[int, int]
    exit: Tuple[int, int]
    output_file: str = Field(pattern=r'.+\.txt$')
    perfect: bool
    seed: str | int | None = None
    display: str | None = "ascii"
    algorithm: str | None = "rb"

    @field_validator('entry', 'exit', mode='before')
    @classmethod
    def parse_coordinate(cls, coord: str) -> Tuple[int, int]:
        """Parses a coordinate string into a tuple of integers.

        Allows the user to provide coordinates in the config file as a
        string "x,y".

        Args:
            coord: A string in format "x,y" or an already parsed tuple.

        Returns:
            Tuple[int, int]: The parsed (x, y) coordinates.

        Raises:
            ValueError: If the format is incorrect or values are not integers.
        """
        if isinstance(coord, tuple):
            return coord

        if isinstance(coord, str):
            if len(coord) < 3:
                raise ValueError("Coordinates are invalid. (Use this format: "
                                 "'0,0')")
            if ',' not in coord:
                raise ValueError("Coordinates are invalid. (Use this format: "
                                 "'0,0')")

            splited_coord = coord.split(',')
            if len(splited_coord) != 2:
                raise ValueError("Coordinates are invalid. (Use this format: "
                                 "'0,0')")

            try:
                coord_x = int(splited_coord[0])
                coord_z = int(splited_coord[1])
            except ValueError:
                raise ValueError("ENTRY and EXIT need to be int()")

            tuple_coord = (coord_x, coord_z)
            return tuple_coord
        return coord

    @field_validator('display')
    @classmethod
    def validate_display_mode(cls, display: str | None) -> str:
        """Normalizes and validates the display mode.

        Args:
            display: The raw string from the config (case-insensitive).

        Returns:
            str: The normalized mode ('ascii' or 'emoji').

        Raises:
            MazeConfigError: If the mode is unknown.
        """
        valid_display = ["ascii", "emoji"]

        if display is not None:
            value = display.lower()
        else:
            value = "emoji"

        if value not in valid_display:
            raise MazeConfigError(f"Invalid display mode. Use {valid_display}")
        return value

    @field_validator('algorithm')
    @classmethod
    def validate_algorithm_mode(cls, algo: str | None) -> str:
        """Normalizes and validates the algorithm selection.

        Args:
            algo: The raw string from the config (case-insensitive).

        Returns:
            str: The normalized algorithm identifier ('rb' or 'huntandkill').

        Raises:
            MazeConfigError: If the algorithm is unknown.
        """
        valid_algo = ["rb", "huntandkill"]

        if algo is not None:
            value = algo.lower()
        else:
            value = "rb"

        if value not in valid_algo:
            raise MazeConfigError(f"Invalid algorithm mode. Use {valid_algo}")
        return value

    @model_validator(mode='after')
    def valid_config_input(self) -> Self:
        """Performs cross-field logic validation after model creation.

        Checks that:
        1. Entry and Exit coordinates are within grid bounds.
        2. Entry and Exit are not identical.
        3. Entry and Exit do not overlap with the reserved '42' pattern.

        Returns:
            Self: The validated model instance.

        Raises:
            MazeConfigError: If any logical constraint is violated.
        """
        entry_x, entry_y = self.entry
        if not (0 <= entry_x < self.width and 0 <= entry_y < self.height):
            raise MazeConfigError(f"Entry coords: {self.entry} is outside maze"
                                  " dimensions.")

        exit_x, exit_y = self.exit
        if not (0 <= exit_x < self.width and 0 <= exit_y < self.height):
            raise MazeConfigError(f"Exit coords: {self.exit} is outside maze"
                                  " dimensions.")

        if self.width == 3 and self.height == 3:
            raise MazeConfigError("Maze dimensions are invalid")

        if self.entry == self.exit:
            raise MazeConfigError("Entry and Exit cannot be at the exact same "
                                  "position.")

        forty_two_coords = ft_patt(self.width, self.height)
        if self.entry in forty_two_coords:
            raise MazeConfigError("Can't place Entry here. Reserved to '42'")
        if self.exit in forty_two_coords:
            raise MazeConfigError("Can't place Exit here. Reserved to '42'")

        neighbor_entry = [(self.entry[0] + 1, self.entry[1]),
                          (self.entry[0], self.entry[1] - 1),
                          (self.entry[0] - 1, self.entry[1]),
                          (self.entry[0], self.entry[1] + 1)]
        if self.exit in neighbor_entry:
            raise MazeConfigError("Entry and Exit cannot be side by side.")

        return self

    @classmethod
    def from_config_file(cls, filepath: str) -> "MazeConfig":
        """Parses a key-value text file to create a configuration instance.

        Reads a file line by line, ignoring comments (#) and empty lines.
        It maps keys to the model fields and handles Pydantic validation
        errors by converting them into user-friendly `MazeConfigError`.

        Args:
            filepath: Path to the configuration file (e.g., 'config.txt').

        Returns:
            MazeConfig: A fully validated configuration object.

        Raises:
            FileNotFoundError: If the file does not exist.
            MazeConfigError: If the file format is invalid or validation fails.
        """
        path = Path(filepath)
        if not path.is_file():
            raise FileNotFoundError("Missing config file")

        valid_config_key = {"width", "height", "entry", "exit", "output_file",
                            "perfect", "seed", "display", "algorithm"}
        raw_config: dict[str, Any] = {}

        try:
            with open(path, 'r') as file:
                for i, line in enumerate(file, 1):
                    line = line.strip()

                    if line.startswith('#') or not line:
                        continue
                    if "=" not in line:
                        raise MazeConfigError(f"Error at line {i} ({line})")

                    key, value = line.split('=', 1)
                    key = key.strip().lower()
                    value = value.strip()

                    if key not in valid_config_key:
                        raise MazeConfigError(f"Key: '{key}' at line {i}"
                                              " is not valid")
                    else:
                        raw_config[key] = value
        except Exception as e:
            raise MazeConfigError(e)

        try:
            return cls(**raw_config)
        except ValidationError as e:
            # Custom error formatting to make Pydantic errors readable
            # for the end user.
            for error in e.errors():
                msg = error['msg']
                if error['type'] == "string_pattern_mismatch":
                    msg = "File must end with '.txt'"
                elif error['type'] == "greater_than_equal":
                    msg = (f"Too small. Must be at least {error['ctx']['ge']}")
                error_message = f"{error['loc'][0]}: {msg}"
            raise MazeConfigError(error_message)
