# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  custom_errors.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 15:08:42 by roandrie        #+#    #+#               #
#  Updated: 2026/02/05 13:25:10 by rruiz           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Custom lightweight errors used by the top-level script."""


class ArgumentsError(Exception):
    """Raised when command-line arguments are missing or invalid."""
    pass
