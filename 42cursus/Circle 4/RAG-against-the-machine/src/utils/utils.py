# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  utils.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/29 13:40:01 by roandrie        #+#    #+#               #
#  Updated: 2026/09/09 11:38:05 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import pathlib
import os

from rich.console import Console
from rich.errors import StyleSyntaxError
from rich.style import Style

# :---------:
#   CHECKER
# :---------:


def is_folder_exist(path_to_folder: pathlib.Path | str) -> bool:
    """
    Check if a given path exists and is a directory.

    Args:
        path_to_folder (pathlib.Path): The path to verify.

    Returns:
        bool: True if the path exists and is a directory, False otherwise.
    """
    if not isinstance(path_to_folder, pathlib.Path):
        path_to_folder = pathlib.Path(path_to_folder)

    return path_to_folder.exists() and path_to_folder.is_dir()


def is_file_exist(file: pathlib.Path | str) -> bool:
    """
    Check if a given path exists and is a regular file.

    Args:
        file (pathlib.Path): The file path to verify.

    Returns:
        bool: True if the path exists and is a file, False otherwise.
    """
    if not isinstance(file, pathlib.Path):
        file = pathlib.Path(file)

    return file.exists() and file.is_file()


def check_file_extension(file: pathlib.Path | str, extension: str) -> bool:
    """
    Check if a file has the intended extension.

    Args:
        file (pathlib.Path): The file path to check.

    Returns:
        bool: True if the file suffix is right, False otherwise.
    """
    if not isinstance(file, pathlib.Path):
        file = pathlib.Path(file)

    if not extension.startswith("."):
        extension = f".{extension}"
    return file.suffix == extension


def check_perm_can_read(path: pathlib.Path | str) -> bool:
    """
    Check if a file have the permission to be read

    Args:
        file (pathlib.Path): The file path to check.

    Returns:
        bool: True if the file have the read permission, False otherwise.
    """
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)

    return os.access(path, os.R_OK)


def check_perm_can_write(path: pathlib.Path | str) -> bool:
    """
    Check if a file have the permission to be writted

    Args:
        file (pathlib.Path): The file path to check.

    Returns:
        bool: True if the file have the write permission, False otherwise.
    """
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)

    return os.access(path, os.W_OK)


def check_perm_can_execute(path: pathlib.Path | str) -> bool:
    """
    Check if a file have the permission to be executed

    Args:
        file (pathlib.Path): The file path to check.

    Returns:
        bool: True if the file have the execution permission, False otherwise.
    """
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)

    return os.access(path, os.X_OK)


# :---------:
#   DISPLAY
# :---------:

STANDARD_CONSOLE: Console = Console()
ERROR_CONSOLE: Console = Console(stderr=True)


def print_error(message: str | ValueError) -> None:
    """
    Displays a formatted error message on the standard error stream.

    Args:
        message (str): The specific error description to be displayed.
    """
    prefix: str = "[ERROR]: "
    content: str = f"{message}"
    ERROR_CONSOLE.print(f"[bold red]{prefix + content}[/bold red]")


def print_success(message: str) -> None:
    """
    Display a formatted success message on the standard stream.

    Args:
        message (str): The specific message to be displayed.
    """
    STANDARD_CONSOLE.print(f"[green]{message}[/green]")


def print_warn(message: str) -> None:
    """
    Display a formatted warn message on the standard error stream.

    Args:
        message (str): The specific warning message to be displayed.
    """
    prefix: str = "[WARNING]: "
    content: str = f"{message}"
    ERROR_CONSOLE.print(f"[bold yellow]{prefix + content}[/bold yellow]")


def print_log(message: str, color: str = "white") -> None:
    """
    Display a formatted log message on the standard stream using 'log' from
    rich. Using '_stack_offset' allow good naming for the file.

    Args:
        message (str): The specific message to be displayed.
    """
    style_rule = _check_color_validation(color)

    STANDARD_CONSOLE.log(message, _stack_offset=2, style=style_rule)


def print_rule(message: str = "", color: str = "bold blue") -> None:
    """
    Display a horizontal rule with a message at the center and with a
    specific color. If the color doesn't exist or isn't specify, the color
    bold blue will by the default color.

    Args:
        message (str): The specific message to be displayed.
        color (str): The color used for the rule.
    """
    style_rule = _check_color_validation(color)

    STANDARD_CONSOLE.rule(message, style=style_rule)


def print_with_color(message: str, color: str = "white") -> None:
    """
    Print a standard message with a specific color requested by the user. If
    the color don't exist, default color will be white.

    Args:
        message (str): The specific message to be displayed.
        color (str): The color used for the print.
    """
    style_rule = _check_color_validation(color)

    STANDARD_CONSOLE.print(f"[{style_rule}]{message}[/{style_rule}]")


# :-------------------:
#   PRIVATE FUNCTIONS
# :-------------------:


def _check_color_validation(color: str) -> str:
    """Validate that a rich color name is supported.

    Args:
        color: Requested color name.

    Returns:
        str: Valid color or the default white style.
    """
    style_rule: str = color

    try:
        Style.parse(style_rule)

    except StyleSyntaxError:
        style_rule = "white"
        print_error(f"'{color}' is unkown. Switching to default (white).")

    return style_rule
