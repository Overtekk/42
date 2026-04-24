# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  display.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/27 09:46:37 by roandrie        #+#    #+#               #
#  Updated: 2026/04/24 09:59:39 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Terminal output management utilities.

This module provides a centralized interface for displaying formatted
messages using the Rich library. It manages distinct output streams
(stdout and stderr) to ensure that logs and errors do not interfere with
potential structured outputs.

Attributes:
    standard_console (Console): The default console instance for standard
                                output.
    error_console (Console): A console instance configured specifically for
                             stderr.
"""

from rich.console import Console
from rich.errors import StyleSyntaxError
from rich.style import Style


standard_console: Console = Console()
error_console: Console = Console(stderr=True)


def print_error(message: str) -> None:
    """
    Displays a formatted error message on the standard error stream.

    Args:
        message (str): The specific error description to be displayed.
    """
    prefix: str = "Error: "
    content: str = f"{message}"
    error_console.print(f"[bold red]{prefix + content}[/bold red]")


def print_success(message: str) -> None:
    """
    Display a formatted success message on the standard stream.

    Args:
        message (str): The specific message to be displayed.
    """
    standard_console.print(f"[green]{message}[/green]")


def print_log(message: str) -> None:
    """
    Display a formatted log message on the standard stream using 'log' from
    rich. Using '_stack_offset' allow good naming for the file.

    Args:
        message (str): The specific message to be displayed.
    """
    standard_console.log(message, _stack_offset=2)


def print_rule(message: str, color: str = "bold blue") -> None:
    """
    Display a horizontal rule with a message at the center and with a
    specific color. If the color doesn't exist or isn't specify, the color
    bold blue will by the default color.

    Args:
        message (str): The specific message to be displayed.
        color (str): The color used for the rule.
    """
    style_rule: str = color

    try:
        Style.parse(style_rule)

    except StyleSyntaxError:
        style_rule = "bold blue"
        print_error(f"'{color}' is unkown. Switching to default (bold blue).")

    standard_console.rule(message, style=style_rule)


def print_visualizer(message: str) -> None:
    """
    Display a dynamically updating message on the standard stream.
    Allows in-place updates by modifying the 'end' parameter.

    Args:
        message (str): The specific message to be displayed.
        end (str, optional): The string appended after the output.
                             Defaults to "\n".
        flush (bool, optional): Whether to forcibly flush the stream.
                                Defaults to False.
    """
    padded_message: str = message + " " * 20

    standard_console.print(padded_message, end='', justify="center")
