# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_config.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 14:14:51 by roandrie        #+#    #+#               #
#  Updated: 2026/02/05 16:11:13 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Configuration model for maze generation.

Defines validation rules for maze dimensions, coordinates and
runtime options. Uses `pydantic` for input parsing and validation.
"""

from pathlib import Path
from typing import Any, Self, Tuple

from pydantic import (BaseModel, Field, ValidationError, field_validator,
                      model_validator)

from .maze_errors import MazeConfigError
from .maze_fortytwo_pattern import get_fortytwo_pattern as ft_patt


class MazeConfig(BaseModel):
    """Pydantic model that represents validated maze configuration.

    Fields are validated for sensible ranges and formats. Helper
    validators convert string coordinates and enforce permitted
    display/algorithm values.
    """
    width: int = Field(ge=7)
    height: int = Field(ge=5)
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
        """Parse a coordinate string "x,y" into a tuple.

        Accepts either a tuple or a string. Raises `ValueError` for an
        invalid format.
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
        """Validate `display` field and normalize its value.

        Raises `MazeConfigError` if the value is not supported.
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
        """Validate `algorithm` field and normalize its value.

        Raises `MazeConfigError` if the value is not supported.
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
        """Perform cross-field validation after model construction.

        Ensures coordinates are inside bounds and that entry and exit
        are not overlapping or placed on reserved '42' pattern cells.
        """

        entry_x, entry_y = self.entry
        if not (0 <= entry_x < self.width and 0 <= entry_y < self.height):
            raise MazeConfigError(f"Entry coords: {self.entry} is outside maze"
                                  " dimensions.")

        exit_x, exit_y = self.exit
        if not (0 <= exit_x < self.width and 0 <= exit_y < self.height):
            raise MazeConfigError(f"Exit coords: {self.exit} is outside maze"
                                  " dimensions.")

        if self.entry == self.exit:
            raise MazeConfigError("Entry and Exit cannot be at the exact same "
                                  "position.")

        forty_two_coords = ft_patt(self.width, self.height)
        if self.entry in forty_two_coords:
            raise MazeConfigError("Can't place Entry here. Reserved to '42'")
        if self.exit in forty_two_coords:
            raise MazeConfigError("Can't place Exit here. Reserved to '42'")

        return self

    @classmethod
    def from_config_file(cls, filepath: str) -> "MazeConfig":
        """Create a `MazeConfig` instance from a simple key=value file.

        The expected keys are: width, height, entry, exit, output_file,
        perfect, seed, display, algorithm.

        Args:
            filepath: Path to the configuration file.

        Returns:
            MazeConfig: Validated configuration model.

        Raises:
            FileNotFoundError: If `filepath` does not exist.
            MazeConfigError: On malformed content or validation errors.
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
            for error in e.errors():
                msg = error['msg']
                if error['type'] == "string_pattern_mismatch":
                    msg = "File must end with '.txt'"
                elif error['type'] == "greater_than_equal":
                    msg = ("Too small (can't put 42 pattern). Must be at "
                           f"least {error['ctx']['ge']}")
                error_message = f"{error['loc'][0]}: {msg}"
            raise MazeConfigError(error_message)
