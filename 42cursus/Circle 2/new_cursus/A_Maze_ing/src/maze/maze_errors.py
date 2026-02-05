# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_errors.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 14:13:47 by roandrie        #+#    #+#               #
#  Updated: 2026/01/27 16:45:44 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class MazeError(Exception):
    pass


class MazeConfigError(MazeError):
    pass


class MazeGenerationError(MazeError):
    pass
