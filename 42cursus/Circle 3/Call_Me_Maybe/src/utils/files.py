# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  files.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/27 14:15:34 by roandrie        #+#    #+#               #
#  Updated: 2026/03/31 17:03:22 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
File system utility functions.

This module provides helper functions to perform basic file system checks,
including verifying the existence of files and directories, and validating
file extensions for JSON compatibility.
"""

import pathlib


def is_folder_exist(path_to_folder: pathlib.Path) -> bool:
    """
    Check if a given path exists and is a directory.

    Args:
        path_to_folder (pathlib.Path): The path to verify.

    Returns:
        bool: True if the path exists and is a directory, False otherwise.
    """
    return path_to_folder.exists() and path_to_folder.is_dir()


def is_file_exist(file: pathlib.Path) -> bool:
    """
    Check if a given path exists and is a regular file.

    Args:
        file (pathlib.Path): The file path to verify.

    Returns:
        bool: True if the path exists and is a file, False otherwise.
    """
    return file.exists() and file.is_file()


def is_file_json(file: pathlib.Path) -> bool:
    """
    Check if a file has a .json extension.

    Args:
        file (pathlib.Path): The file path to check.

    Returns:
        bool: True if the file suffix is '.json', False otherwise.
    """
    return file.suffix == ".json"
