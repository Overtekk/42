# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  custom_errors.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 15:08:42 by roandrie        #+#    #+#               #
#  Updated: 2026/02/09 08:32:38 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Custom exception definitions for the application.

This module defines domain-specific exceptions used to handle errors
gracefully in the top-level script, allowing for cleaner exit codes
and user messages instead of raw stack traces.
"""


class ArgumentsError(Exception):
    """Exception raised for errors in the command-line arguments.

    This exception should be raised when the user fails to provide the
    expected input format (e.g., missing configuration file) or uses
    invalid flags.
    """
    pass
