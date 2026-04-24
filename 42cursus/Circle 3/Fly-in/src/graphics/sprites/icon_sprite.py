# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  icon_sprite.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/27 08:30:37 by roandrie        #+#    #+#               #
#  Updated: 2026/03/27 10:12:30 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Graphical sprites and UI components for the Arcade simulation.

This module defines the visual representations of the the legend on the botton
right. Used for the user to know what sprite is used for.
"""

import arcade

from arcade.types import PathOrTexture
from src.graphics.graphics_settings import FontSettings


class Icon(arcade.Sprite):
    """
    Visual representation of an icon and is associate name.
    """

    def __init__(self, image_path: PathOrTexture, scale: float,
                 legend: str) -> None:
        """
        Initializes a visual representation of an icon.

        Sets up the sprite image, scales it, and prepares the text labels for
        displaying the icon name.

        Args:
            image_path (PathOrTexture): The path to the zone's sprite asset.
            scale (float): The scaling factor for the sprite.
            legend (str): The name of the icon.
        """
        super().__init__(image_path, scale)

        self.label_legend = arcade.Text(
            text=legend, x=0, y=0, anchor_x="left", anchor_y="center",
            color=arcade.color.WHITE_SMOKE, font_size=12,
            font_name=FontSettings.PIXELOGIST_NAME
        )

    def draw_text(self) -> None:
        """
        Renders the UI overlays for the icon sprite.

        Draws the text label.
        """
        self.label_legend.draw()
