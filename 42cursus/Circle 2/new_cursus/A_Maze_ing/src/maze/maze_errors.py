# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_errors.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 14:13:47 by roandrie        #+#    #+#               #
#  Updated: 2026/02/05 13:24:19 by rruiz           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Custom exception types for the maze package.

Provide a small hierarchy of exceptions that callers can catch for
configuration and generation related errors.
"""


class MazeError(Exception):
    """Base class for maze-related errors."""
    pass


class MazeConfigError(MazeError):
    """Raised when a provided configuration is invalid."""
    pass


class MazeGenerationError(MazeError):
    """Raised when generation fails or produces an unsolvable maze."""
    pass
