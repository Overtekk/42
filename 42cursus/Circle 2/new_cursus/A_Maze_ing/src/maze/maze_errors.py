# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_errors.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 14:13:47 by roandrie        #+#    #+#               #
#  Updated: 2026/02/09 09:17:34 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Defines the exception hierarchy for the maze package.

This module groups all custom exceptions under a common base class, allowing
callers to catch specific errors (configuration vs. generation) or handle
all package-specific failures generically.
"""


class MazeError(Exception):
    """Base exception class for all maze-related errors.

    All custom exceptions in this package inherit from this class,
    allowing a generic `except MazeError:` block to catch any
    internal failure without catching standard Python exceptions.
    """
    pass


class MazeConfigError(MazeError):
    """Exception raised for configuration and parameter errors.

    This error occurs when input data (from `config.txt` or arguments)
    is malformed, missing, or logically invalid (e.g., negative dimensions).
    """
    pass


class MazeGenerationError(MazeError):
    """Exception raised for runtime errors during maze generation.

    This error typically indicates a failure in the algorithm logic, such as
    the production of an unsolvable maze or an invalid internal state.
    """
    pass
