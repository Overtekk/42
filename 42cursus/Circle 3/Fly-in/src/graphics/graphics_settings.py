# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  graphics_settings.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 20:01:40 by roandrie        #+#    #+#               #
#  Updated: 2026/04/01 19:20:46 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Configuration settings and constants for the graphical interface.

This module centrally manages all hardcoded values related to the Arcade
window, file paths for assets (sprites and fonts), rendering scales,
and UI action identifiers.
"""

from random import random


DEFAULT_THEME = "src/graphics/sprites/default/"
SEAGULL_THEME = "src/graphics/sprites/seagull_theme/"

if random() < 0.3:
    PATH = SEAGULL_THEME
    ANIM_SPEED = 1
else:
    PATH = DEFAULT_THEME
    ANIM_SPEED = 5


class WindowSettings():
    """
    Defines core properties for the main Arcade simulation window.
    """
    WIDTH = 1280
    HEIGHT = 720
    NAME = "Fly-in"


class SpritePath():
    """
    Provides relative file paths to all image assets used for rendering
    sprites.
    """
    BACKGROUND = f"{PATH}background.png"
    WINDOW_INFO = "src/graphics/sprites/default/window_info.png"
    DRONE = f"{PATH}drone.png"
    DRONE_ANIM1 = f"{PATH}drone1.png"
    DRONE_ANIM2 = f"{PATH}drone2.png"
    DRONE_FINISH = f"{PATH}drone_finish.png"
    START_HUB = f"{PATH}start_hub.png"
    END_HUB = f"{PATH}end_hub.png"
    DEFAULT_ZONE = f"{PATH}default_zone.png"
    ZONE_BLOCKED = f"{PATH}zone_blocked.png"
    ZONE_PRIORITY = f"{PATH}zone_priority.png"
    ZONE_RESTRICTED = f"{PATH}zone_restricted.png"


class FontSettings():
    """
    Stores paths and reference names for custom typography loaded into Arcade.
    """
    PIXELOGIST_PATH = "src/graphics/sprites/font/Pixelogist.ttf"
    PIXELOGIST_NAME = "Pixelogist"
    PIXELMANIA_PATH = "src/graphics/sprites/font/Pixelmania.ttf"
    PIXELMANIA_NAME = "Pixelmania"


class SpriteSetting():
    """
    Defines numeric constants for sprite scaling, grid positioning, and speeds.
    """
    ZONE_SCALE = 1
    DRONE_SCALE = 0.9
    SPACING = 120
    OFFSET_X = 100.0
    OFFSET_Y = 100.0
    DRONE_SPEED = 100.0
    ANIM_SPEED = ANIM_SPEED


class WindowAction():
    """
    Enumerates string identifiers for interactive UI button actions.
    """
    CLOSE = "CLOSE"
    COPY = "COPY"
    REMOVE = "REMOVE"
    MOVE = "MOVE"
    SPEED_MINUS = "SPEED_MINUS"
    SPEED_PLUS = "SPEED_PLUS"
    TURN = "TURN"
    TOGGLE_PAUSE = "PAUSE"
