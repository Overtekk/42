# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  drone_sprite.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/26 15:00:53 by roandrie        #+#    #+#               #
#  Updated: 2026/03/26 15:05:45 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Graphical sprites and UI components for the Arcade simulation.

This module defines the visual representations of the drones.
"""

from typing import Any, List

import math
import arcade
from arcade.types import PathOrTexture

from src.object.drones import Drone
from src.graphics.graphics_settings import SpriteSetting


class DroneSprite(arcade.Sprite):
    """
    Visual representation of a drone.

    This sprite manages its own movement interpolation between zones
    and idle animations (swarming effect) when stationary.
    """

    def __init__(self, image_path: PathOrTexture, scale: float,
                 drone_data: Drone, id: int,
                 drone_sprites_anim: List[arcade.Texture]) -> None:
        """
        Initializes a visual representation of a drone.

        Sets up the sprite, its animation frames, and initializes state
        tracking variables for movement and idle swarming (oscillation).

        Args:
            image_path (PathOrTexture): The path to the drone's default sprite.
            scale (float): The scaling factor for the sprite.
            drone_data (Drone): The logical Drone object containing backend
                                data.
            id (int): The unique identifier of the drone.
            drone_sprites_anim (List[arcade.Texture]): A list of textures for
                                                       movement animation.
        """
        super().__init__(image_path, scale)

        self.drone_data = drone_data
        self.id = id
        self.location = self.drone_data.get_location()
        self.finish = drone_data.finish

        self.target_x = 0.0
        self.target_y = 0.0
        self.is_moving = False
        self.active_connection = ""

        self.cur_textures = 0
        self.time_counter = 0.0
        self.departure_timer = 0.0
        self.idle_texture = self.texture
        self.finish_texture = drone_sprites_anim[2]
        self.move_textures = drone_sprites_anim

    def on_update(self, delta_time: float) -> None:
        """
        Handles the movement and positional logic of the drone.

        If the drone is moving, it calculates the velocity vector towards its
        target and updates its coordinates.

        Args:
            delta_time (float): Time interval since the last frame.
        """
        if not self.is_moving:
            return

        if self.departure_timer > 0.0:
            self.departure_timer -= delta_time
            return

        dx = self.target_x - self.center_x
        dy = self.target_y - self.center_y

        distance = math.hypot(dx, dy)

        movement_in_pixels = SpriteSetting.DRONE_SPEED * delta_time

        if distance <= movement_in_pixels:
            self.center_x = self.target_x
            self.center_y = self.target_y
            self.is_moving = False
            self.location = self.drone_data.get_location()

            if not self.finish:
                self.finish = self.drone_data.finish

        else:
            angle = math.atan2(dy, dx)

            velocity_x = math.cos(angle) * (SpriteSetting.DRONE_SPEED
                                            * delta_time)
            velocity_y = math.sin(angle) * (SpriteSetting.DRONE_SPEED
                                            * delta_time)

            self.center_x += velocity_x
            self.center_y += velocity_y

    def update_animation(self, delta_time: float = 1 / 60,
                         *args: Any, **kwargs: Any) -> None:
        """
        Cycles through the drone's textures to create an animation.

        Switches textures based on the elapsed time if the drone is moving.
        Resets to the idle or finished texture when stationary.

        Args:
            delta_time (float): Time interval since the last frame.
                                Defaults to 1/60.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        if not self.is_moving:
            if self.drone_data.finish:
                self.texture = self.finish_texture
            else:
                self.texture = self.idle_texture

            self.scale = SpriteSetting.DRONE_SCALE
            self.cur_textures = 0
            return

        self.time_counter += delta_time
        self.scale = SpriteSetting.DRONE_SCALE - 0.2

        if self.time_counter > (0.1 / SpriteSetting.ANIM_SPEED):
            self.cur_textures = (self.cur_textures + 1) % 2
            self.texture = self.move_textures[self.cur_textures]

            self.time_counter = 0.0
