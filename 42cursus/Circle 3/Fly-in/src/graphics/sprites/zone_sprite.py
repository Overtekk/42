# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  zone_sprite.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 14:34:19 by roandrie        #+#    #+#               #
#  Updated: 2026/03/26 15:05:02 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Graphical sprites and UI components for the Arcade simulation.

This module defines the visual representations of the zones.
"""

from typing import TYPE_CHECKING

import arcade
from arcade.types import PathOrTexture

from src.object.zone import Zone
from src.utils.ui import Colors
from src.graphics.graphics_settings import FontSettings


if TYPE_CHECKING:
    from src.simulation.manager import Manager


class ZoneSprite(arcade.Sprite):
    """
    Visual representation of a simulation zone.

    This sprite handles the display of a physical hub/node on the map,
    including its name, the number of drones currently occupying it,
    and its pathfinding weight (in debug mode).
    """

    def __init__(self, image_path: PathOrTexture,
                 scale: float, zone_data: Zone, manager: 'Manager') -> None:
        """
        Initializes a visual representation of a simulation zone.

        Sets up the sprite image, scales it, and prepares the text labels for
        displaying the zone's name, current drone count, and pathfinding
        weight.

        Args:
            image_path (PathOrTexture): The path to the zone's sprite asset.
            scale (float): The scaling factor for the sprite.
            zone_data (Zone): The logical Zone object containing backend data.
            manager (Manager): The core simulation manager.
        """
        super().__init__(image_path, scale)

        self.zone_data = zone_data
        self.max_drones = self.zone_data.metadata_max_drones
        self.manager = manager

        # Override zone name if it's too long
        self.zone_name = self.zone_data.name
        if len(self.zone_data.name) > 12:
            self.zone_name = self.zone_data.name[:12]
            self.zone_name += "..."

        # Write zone name
        self.label_name_text = arcade.Text(
            text=self.zone_name, x=0, y=0, anchor_x="center", anchor_y="top",
            color=Colors.get_rgb_color(self.zone_data.metadata_color),
            font_name=FontSettings.PIXELOGIST_NAME, font_size=10
            )

        # Write drones count
        self.label_count_text = arcade.Text(
            text="", x=0, y=0, anchor_x="left", anchor_y="baseline",
            color=arcade.color.FLORAL_WHITE,
            font_name=FontSettings.PIXELOGIST_NAME, font_size=13
        )

        # Write zone weight (for debug mode)
        if self.manager.args.debug:
            weight = str(self.zone_data.weight)

            if len(weight) > 8:
                weight = weight[:8]

            self.label_weight_text = arcade.Text(
                text=f"{weight}", bold=True, italic=False,
                x=0, y=0, anchor_x="center", anchor_y="center",
                color=arcade.color.WHITE_SMOKE,
                font_name="arial", font_size=18
            )

    def update_drone_count(self, visual_count: int) -> None:
        """
        Updates the textual display of the drone count on the zone.

        Formats the text differently depending on whether the zone is a start
        hub, end hub, or a regular zone with a maximum capacity.

        Args:
            visual_count (int): The current number of drones occupying the
                                zone.
        """
        if self.zone_data.is_start:
            text_drone = f"{visual_count}"
        elif self.zone_data.is_end:
            text_drone = f"{visual_count}"
        else:
            text_drone = f"{visual_count}/{self.max_drones}"

        self.label_count_text.text = text_drone

    def draw_ui(self) -> None:
        """
        Renders the UI overlays for the zone sprite.

        Draws the zone's name, current capacity count, and debug information
        (pathfinding weight) directly above or below the sprite.
        """
        # text_width = self.label_name_text.content_width
        # text_height = self.label_name_text.content_height
        # text_x = self.label_name_text.x
        # text_y = self.label_name_text.y

        # arcade.draw.draw_lbwh_rectangle_filled(
        #     text_x - (text_width / 2) - 1, text_y - text_height - 2.5,
        #     text_width + 3, text_height + 0.6,
        #     (0, 0, 0, 190)
        #     )

        self.label_name_text.draw()
        self.label_count_text.draw()

        if self.manager.args.debug:
            self.label_weight_text.draw()
