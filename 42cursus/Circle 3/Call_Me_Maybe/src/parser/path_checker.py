# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  path_checker.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/27 14:27:44 by roandrie        #+#    #+#               #
#  Updated: 2026/04/22 10:57:04 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Path validation module for the Call Me Maybe tool.

This module provides high-level validation for file system paths provided via
the command line interface. It verifies the existence of input files, checks
for JSON extensions, manages directory creation for output files, and strictly
enforces read/write/execute permissions to ensure system stability.
"""

from pathlib import Path

import pathlib
import os
import argparse

from src.utils import is_file_exist, is_folder_exist, is_file_json


def validate_json_input(path_str: str) -> pathlib.Path:
    """
    Validate that a given path points to an existing, readable JSON file.

    This function is intended to be used as a 'type' factory for argparse.
    It ensures the file exists on the disk, has a valid .json extension,
    and that the current user has read permissions.

    Args:
        path_str (str): The raw string path provided by the user.

    Raises:
        argparse.ArgumentTypeError: If the file does not exist, is not a
                                    JSON file, or is not readable.

    Returns:
        pathlib.Path: The validated path object.
    """
    path: Path = pathlib.Path(path_str)

    if not is_file_exist(path):
        raise argparse.ArgumentTypeError(f"File '{path}' does not exist.")

    if not is_file_json(path):
        raise argparse.ArgumentTypeError(f"File '{path}' is not json.")

    if not os.access(path, os.R_OK):
        raise argparse.ArgumentTypeError(f"File '{path}' can't be read. Check "
                                         "your permissions.")

    return path


def validate_json_output(path_str: str) -> pathlib.Path:
    """
    Validate and prepare the output path for result storage.

    Verifies the .json extension and checks if the parent directory is
    writable. If the parent directory does not exist, it creates it
    recursively. It also touches the file to ensure it can be created/accessed.

    Args:
        path_str (str): The raw string path provided by the user.

    Raises:
        argparse.ArgumentTypeError: If the extension is invalid, if write
                                    permissions are denied for the directory,
                                    or if the file cannot be read after
                                    creation.

    Returns:
        pathlib.Path: The validated and prepared path object.
    """
    path: Path = pathlib.Path(path_str)

    if path.suffix != ".json":
        raise argparse.ArgumentTypeError(f"File '{path}' is not json.")

    # Match 'input' folder
    folder_parent: Path = path.parent

    if not is_folder_exist(folder_parent):
        folder_parent.mkdir(parents=True, exist_ok=True)

    # Match 'data' folder
    if (not os.access(folder_parent.parent, os.W_OK | os.X_OK)
            or not os.access(folder_parent, os.W_OK | os.X_OK)):
        raise argparse.ArgumentTypeError("Write permission denied for "
                                         f"directory '{folder_parent}")

    path.touch(exist_ok=True)

    if not os.access(path, os.R_OK):
        raise argparse.ArgumentTypeError(f"File '{path}' can't be read. Check "
                                         "your permissions.")

    return path
