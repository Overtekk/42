# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  errors.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 17:42:28 by roandrie        #+#    #+#               #
#  Updated: 2026/03/24 13:44:10 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Custom error class to handles errors during the process.

All classes inherits from the Exception class.
"""


class ArgumentError(Exception):
    """
    Invalid Argument provided by the user.
    """
    pass


class MapError(Exception):
    """
    No maps found, error validating map.
    """
    pass


class SpriteError(Exception):
    """
    Sprite not found, or error while loading sprite.
    """
    pass
