"""Configuration module for the Maze Generator.

This module handles the parsing and validation of the configuration file
passed as a command-line argument. It uses Pydantic for data validation
and type enforcement.
"""

import sys
import os

from typing import Any, Self, Tuple
from pydantic import (BaseModel, Field, ValidationError, field_validator,
                      model_validator)


class IllegalArgumentError(Exception):
    """
    Custom exception raised when an invalid argument or configuration is
    encountered.
    """
    pass


class Config(BaseModel):
    """Data model representing the maze configuration.

    Attributes:
        width (int): The width of the maze. Must be greater than or equal to 0.
        height (int): The height of the maze. Must be greater than or
                      equal to 0.
        entry (Tuple[int, int]): The (x, y) coordinates of the maze entry.
        exit (Tuple[int, int]): The (x, y) coordinates of the maze exit.
        output_file (str): The path where the maze solution will be saved.
        perfect (bool): True if the maze have only 1 path between entry and
                        exit.
    """
    width: int = Field(ge=0)
    height: int = Field(ge=0)
    entry: Tuple[int, int]
    exit: Tuple[int, int]
    output_file: str
    perfect: bool

    @field_validator('entry', 'exit', mode='before')
    @classmethod
    def parse_coordinate(cls, coord: str) -> Tuple[int, int]:
        """Parses and validates a coordinate string.

        This validator transforms the string coordinate input ("0,0") into a
        tuple of integers before Pydantic validation occurs.

        Args:
            coord (str): The coordinate string to parse.

        Returns:
            Tuple[int, int]: A tuple containing the x and y coordinates.

        Raises:
            ValueError: If the coordinate format is invalid or values are not
                        integers.
        """
        if isinstance(coord, str):

            if len(coord) != 3:
                raise ValueError("Coordinates are invalid. (Use this format: "
                                 "'0,0')")
            if ',' not in coord:
                raise ValueError("Coordinates are invalid. (Use this format: "
                                 "'0,0')")

            splited_coord = coord.split(',')

            try:
                coord_x = int(splited_coord[0])
                coord_z = int(splited_coord[1])
            except ValueError:
                raise ValueError("ENTRY and EXIT need to be int()")

            tuple_coord = (coord_x, coord_z)
            return tuple_coord
        return coord

    @model_validator(mode='after')
    def valid_config_input(self) -> Self:
        return self


def check_arg() -> Config | None:
    """Validates command-line arguments and initiates configuration parsing.

    Checks if the correct number of arguments is provided and if config file
    exists. It acts as the entry point for the configuration workflow.

    Returns:
        Config | None: The validated Config object if successful,
                       None otherwise.

    Raises:
        IllegalArgumentError: If the number of arguments is incorrect.
        FileNotFoundError: If the provided configuration file does not exist.
    """
    if len(sys.argv) != 2:
        raise IllegalArgumentError("Usage: 'make run' or 'python3 "
                                   "a_maze_ing.py config.txt")

    config_file = sys.argv[1]
    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' "
                                "not found.")

    config_object = check_config_file(config_file)
    return config_object


def check_config_file(config_file: str) -> Config | None:
    """Parses the configuration file line by line.

    Reads the file, ignores comments and empty lines, checks for valid keys,
    and constructs a dictionary of configuration parameters.

    Args:
        config_file (str): The path to the configuration file.

    Returns:
        Config | None: The validated Config object if successful,
                       None otherwise.

    Raises:
        IllegalArgumentError: If the file contains syntax errors or
                              invalid keys.
    """
    valid_config_key = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE",
                        "PERFECT"]
    line_count = 0
    config = {}

    with open(config_file) as file:
        for line in file:
            line_count += 1

            if line.startswith('#') or line.startswith('\n'):
                continue

            key = line.split('=')
            if len(key) < 2:
                raise IllegalArgumentError(f"Syntax error at line {line_count}"
                                           "\nUsage: 'KEY=VALUE'")

            if key[0] not in valid_config_key:
                raise IllegalArgumentError(f"Key '{key[0]}' at line "
                                           f"{line_count} is not valid")
            key[1] = key[1].strip('\n')
            key[0] = key[0].lower()
            config.update({key[0]: key[1]})
    config_object = create_config(config)
    return config_object


def create_config(data: dict[str, Any]) -> Config | None:
    """Instantiates the Config model using the parsed data.

    Attempts to create a Config object from the provided dictionary.
    Catche and prints Pydantic validation errors if the data is invalid.

    Args:
        data (dict[str, Any]): A dictionary containing the raw configuration
                               data.

    Returns:
        Config | None: The validated Config object if successful,
                       None otherwise.
    """
    try:
        config_object = Config(**data)
        return config_object
    except ValidationError as e:
        print(f"{type(e).__name__}:")
        for item in e.errors():
            print(f"{item['loc']}: {item['msg']}")
        return None
