# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  renderer.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 14:08:32 by roandrie        #+#    #+#               #
#  Updated: 2026/04/01 21:52:46 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Rendering module for the visual representation of the drones's journey using
the Arcade library.
"""

import arcade
import arcade.shape_list
import os
import random

from typing import TYPE_CHECKING, Dict, List, Optional, Set, Tuple

from src.graphics.graphics_settings import (WindowSettings, SpritePath,
                                            FontSettings, SpriteSetting,
                                            WindowAction)
from src.object.drones import Drone
from src.object.zone import Zone
from src.object.utils.type import ZoneType
from src.graphics.sprites.zone_sprite import ZoneSprite
from src.graphics.sprites.drone_sprite import DroneSprite
from src.graphics.sprites.window_sprite import WindowInfo
from src.graphics.sprites.icon_sprite import Icon


if TYPE_CHECKING:
    from src.simulation.manager import Manager


class Renderer(arcade.Window):
    """
    Manages the graphical user interface and rendering of the simulation.

    This class extends `arcade.Window` to create a visual representation of the
    drones navigating through the zones. It handles the window lifecycle,
    sprite loading, camera controls, and the synchronization between the
    logical simulation state (Manager) and the visual components.
    """

    def __init__(self, zones_dict: Dict[str, Zone], manager: 'Manager',
                 drones_dict: Dict[int, Drone],
                 connection_map: Dict[str, List[str]]) -> None:

        super().__init__(width=WindowSettings.WIDTH, antialiasing=True,
                         height=WindowSettings.HEIGHT, fullscreen=False,
                         title=WindowSettings.NAME, resizable=False,
                         center_window=True)
        """
        Initializes the simulation window and its graphical components.

        Sets up the window dimensions, anti-aliasing, and title based on
        global settings. It also initializes internal variable states, the
        camera system, UI texts, and pre-loads all necessary sprites and
        drawing data before the first render frame.

        Args:
            zones_dict (Dict[str, Zone]): Dictionary containing all
                                          instantiated zones.
            manager (Manager): The core simulation manager to interact with.
            drones_dict (Dict[int, Drone]): Dictionary containing all
                                            instantiated drones.
            connection_map (Dict[str, List[str]]): The map defining connections
                                                   between zones.
        """

        # Arguments
        self.zones_dict = zones_dict
        self.drones_dict = drones_dict
        self.connection_map = connection_map
        self.manager = manager

        self.zone_sprites_list: arcade.SpriteList[ZoneSprite] = (
                                                        arcade.SpriteList())
        self.drone_sprites_list: arcade.SpriteList[DroneSprite] = (
                                                        arcade.SpriteList())
        self.ui_sprites_list: arcade.SpriteList[arcade.Sprite] = (
                                                        arcade.SpriteList())
        self.legend_sprites_list: arcade.SpriteList[Icon] = (
                                                        arcade.SpriteList())
        self.connection_lines: (arcade.shape_list.
                                ShapeElementList[arcade.shape_list.Shape]) = (
            arcade.shape_list.ShapeElementList())

        self.zone_coords: Dict[str, Tuple[float, float]] = {}
        self.line_to_draw: List[Tuple[Tuple[float, float],
                                      Tuple[float, float]]] = []
        self.draw_lines: Set[Tuple[str, str]] = set()

        self.pause = False
        self.drones_moving = False
        self.started = False

        self.camera: arcade.camera.Camera2D = arcade.camera.Camera2D()
        self.static_camera: arcade.camera.Camera2D = arcade.camera.Camera2D()
        self.camera_zoom = 1.0
        self.default_camera_x, self.default_camera_y = self.camera.position

        self.window_info_state: WindowInfo | None = None
        self.window_info_offset_x = 0.0
        self.window_info_offset_y = 0.0

        # Call all needed methods
        self._load_custom_fonts()
        self._init_texts()
        self._load_sprites()
        self._calculate_line_to_draw()
        self._create_static_lines()

    def on_update(self, delta_time: float) -> None:
        """
        Updates the visual simulation state at each frame.

        Handles drone animations, triggers the logical simulation turns when
        drones finish their movements, and updates the UI elements' logic.

        Args:
            delta_time (float): Time interval since the last frame.
        """
        if not self.pause:
            for drone_sprite in self.drone_sprites_list:
                drone_sprite.on_update(delta_time)
                drone_sprite.update_animation(delta_time, None, None)

        if self.started and not self.pause and self.manager.running:
            self.drones_moving = False

            for drone_sprite in self.drone_sprites_list:
                if drone_sprite.is_moving:
                    self.drones_moving = True
                    break

            if not self.drones_moving:
                self.manager.simulate_one_turn()
                self._update_drone_sprite()

        for ui_elem in self.ui_sprites_list:
            if isinstance(ui_elem, WindowInfo):
                ui_elem.update_info(WindowAction.TURN)
                ui_elem.on_update(delta_time)

        self._update_visual_counts()

    def on_draw(self) -> None:
        """
        Renders all visual elements to the screen.

        Draws the background, connection lines zone sprites, drone sprites,
        and the user interface including the pause overlay.
        """
        self.clear()

        # Draw the background
        self.static_camera.use()
        arcade.draw_texture_rect(self.background, arcade.LBWH(
            0, 0, WindowSettings.WIDTH, WindowSettings.HEIGHT))

        # Main camera (affected by the zoom)
        self.camera.use()

        # Draw connections lines
        self.connection_lines.draw()

        # Draw sprites for zones and drones
        self.zone_sprites_list.draw()
        for sprite in self.zone_sprites_list:
            sprite.draw_ui()
        self.drone_sprites_list.draw()

        self.static_camera.use()
        # Draw legend
        self.legend_sprites_list.draw()
        for sprite_icon in self.legend_sprites_list:
            sprite_icon.draw_text()

        # Draw pause screen (gray font, pause button)
        if self.pause:
            arcade.draw_lrbt_rectangle_filled(
                0, WindowSettings.WIDTH, 0, WindowSettings.HEIGHT,
                color=(0, 0, 0, 150)
            )
        self.ui_sprites_list.draw()

        # Draw window informations
        for ui_element in self.ui_sprites_list:
            if isinstance(ui_element, WindowInfo):
                ui_element.draw_ui(self.pause)

        # Draw zones weights
        if self.manager.args.debug:
            for ui_elements in self.ui_sprites_list:
                if isinstance(ui_elements, WindowInfo):
                    ui_elements.debug_draw_hitboxes()

        # Draw start and finish text
        if not self.started:
            self.starting_text_ui.draw()
        if not self.manager.running and self.started:
            self.finished_text_ui.draw()

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """
        Handles keyboard input events.

        Manages the exit action, simulation start/pause toggle, and simulation
        speed adjustments (+ / -).

        Args:
            symbol (int): The pressed key symbol.
            modifiers (int): Bitwise 'and' of all modifier keys pressed.
        """
        if symbol == arcade.key.ESCAPE:
            arcade.exit()

        elif symbol == arcade.key.SPACE:
            if self.started:
                self.pause = not self.pause
                for ui_element in self.ui_sprites_list:
                    if isinstance(ui_element, WindowInfo):
                        ui_element.draw_ui(self.pause)

            elif not self.started:
                self.started = True
                self.manager.simulate_one_turn()
                self._update_drone_sprite()

        elif (symbol in [arcade.key.PLUS, arcade.key.NUM_ADD, arcade.key.EQUAL]
                and self.started):
            self._update_speed_animation(WindowAction.SPEED_PLUS)

        elif (symbol in [arcade.key.MINUS, arcade.key.NUM_SUBTRACT]
                and self.started):
            self._update_speed_animation(WindowAction.SPEED_MINUS)

    def on_mouse_scroll(self, x: int, y: int,
                        scroll_x: float, scroll_y: float) -> None:
        """
        Handles mouse scroll events to control camera zoom.

        Args:
            x (int): X-coordinate of the mouse.
            y (int): Y-coordinate of the mouse.
            scroll_x (float): Horizontal scroll amount.
            scroll_y (float): Vertical scroll amount.
        """
        self.camera_zoom *= 0.9 if scroll_y < 0 else 1.1

        self.camera_zoom = max(0.1, min(2.0, self.camera_zoom))
        self.camera.zoom = self.camera_zoom

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int,
                      buttons: int, modifiers: int) -> None:
        """
        Handles mouse drag events for camera panning and UI interaction.

        Allows the user to pan the main camera using the right mouse button
        or drag the UI window across the screen.

        Args:
            x (int): Current X-coordinate of the mouse.
            y (int): Current Y-coordinate of the mouse.
            dx (int): Change in X-coordinate.
            dy (int): Change in Y-coordinate.
            buttons (int): Buttons being pressed during the drag.
            modifiers (int): Modifier keys pressed.
        """
        # Allow camera movement
        if buttons == arcade.MOUSE_BUTTON_RIGHT:
            curr_x, curr_y = self.camera.position
            update_x = curr_x - (dx / self.camera_zoom)
            update_y = curr_y - (dy / self.camera_zoom)

            self.camera.position = (update_x, update_y)

        if self.window_info_state:
            target_x = x - self.window_info_offset_x
            target_y = y - self.window_info_offset_y
            half_width = self.window_info_state.width / 2
            half_height = self.window_info_state.height / 2

            self.window_info_state.center_x = max(
                half_width,
                min(target_x, WindowSettings.WIDTH - half_width)
            )
            self.window_info_state.center_y = max(
                half_height,
                min(target_y, WindowSettings.HEIGHT - half_height)
            )

            self.window_info_state.update_ui_position()

    def on_mouse_press(self, x: int, y: int,
                       button: int, modifiers: int) -> None:
        """
        Handles mouse press events for UI interactions and camera reset.

        Resets the camera to default on middle click and processes clicks
        on the UI window's hitboxes to trigger specific actions.

        Args:
            x (int): X-coordinate of the mouse click.
            y (int): Y-coordinate of the mouse click.
            button (int): The mouse button that was pressed.
            modifiers (int): Modifier keys pressed.
        """
        # Reset camera position
        if button == arcade.MOUSE_BUTTON_MIDDLE:
            self.camera.position = (self.default_camera_x,
                                    self.default_camera_y)

        for ui_element in reversed(self.ui_sprites_list):
            if isinstance(ui_element, WindowInfo):
                action = ui_element.get_ui_action(x, y)

                if action:
                    match action:
                        case WindowAction.CLOSE:
                            arcade.exit()

                        case WindowAction.REMOVE:
                            ui_element.is_imploding = True
                            self.pause = False
                            self._create_window_info_sprite()

                        case WindowAction.COPY:
                            ui_element.is_ejected = True
                            self.pause = False
                            self._create_window_info_sprite()

                        case WindowAction.SPEED_MINUS if self.started:
                            self._update_speed_animation(
                                WindowAction.SPEED_MINUS, ui_element)

                        case WindowAction.SPEED_PLUS if self.started:
                            self._update_speed_animation(
                                WindowAction.SPEED_PLUS, ui_element)

                        case WindowAction.TOGGLE_PAUSE if self.started:
                            self.pause = not self.pause

                        case WindowAction.MOVE:
                            self.window_info_state = ui_element
                            self.window_info_offset_x = x - ui_element.center_x
                            self.window_info_offset_y = y - ui_element.center_y
                    break

    def on_mouse_release(self, x: int, y: int,
                         button: int, modifiers: int) -> None:
        """
        Handles mouse release events.

        Clears the currently dragged UI window state to stop movement.

        Args:
            x (int): X-coordinate of the mouse release.
            y (int): Y-coordinate of the mouse release.
            button (int): The mouse button that was released.
            modifiers (int): Modifier keys pressed.
        """
        if self.window_info_state:
            self.window_info_state = None

    def _init_texts(self) -> None:
        """
        Initializes static textual UI elements.

        Sets up the 'start' and 'finished' texts used before and after the
        simulation.
        """
        # Text : start simulation
        self.starting_text_ui = arcade.Text(
            text="PRESS SPACE TO START", anchor_x="center", anchor_y="bottom",
            x=(WindowSettings.WIDTH / 2), y=(12 / 2),
            font_size=22, color=arcade.color.WHITE_SMOKE,
            font_name=FontSettings.PIXELMANIA_NAME
        )

        # Text : simulation finished
        self.finished_text_ui = arcade.Text(
            text="SIMULATION FINISHED", anchor_x="center", anchor_y="top",
            x=(WindowSettings.WIDTH / 2), y=(WindowSettings.HEIGHT - 40),
            font_size=12, color=arcade.color.WHITE_SMOKE,
            font_name=FontSettings.PIXELMANIA_NAME
        )

    def _load_custom_fonts(self) -> None:
        """
        Loads the required custom pixel fonts into the Arcade engine.

        Raises:
            FileNotFoundError: If the font files are not found at the
                               specified path.
        """
        try:
            arcade.load_font(FontSettings.PIXELOGIST_PATH)
            arcade.load_font(FontSettings.PIXELMANIA_PATH)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Font not found in PATH {e}")

    def _load_sprites(self) -> None:
        """
        Calculates map offsets and orchestrates the loading of all sprites.

        Determines the logical center of the map to align the camera and calls
        the initialization methods for the background, window, zones, and
        drones.

        Raises:
            OSError: If the base sprite directory does not exist.
            FileNotFoundError: If a specific sprite image file is missing.
        """
        if not os.path.exists("src/graphics/sprites/"):
            raise OSError("PATH 'src/graphics/sprites/' does snot exist.")

        try:
            # Calcule the offset to center all sprites
            x_coords = [zone.x for zone in self.zones_dict.values()]
            y_coords = [zone.y for zone in self.zones_dict.values()]

            min_x, max_x = min(x_coords), max(x_coords)
            min_y, max_y = min(y_coords), max(y_coords)

            center_logical_x = (min_x + max_x) / 2
            center_logical_y = (min_y + max_y) / 2

            # Change the offset based on the actual map
            SpriteSetting.OFFSET_X = ((WindowSettings.WIDTH / 2)
                                      - (center_logical_x
                                         * SpriteSetting.SPACING))
            SpriteSetting.OFFSET_Y = ((WindowSettings.HEIGHT / 2)
                                      - (center_logical_y
                                         * SpriteSetting.SPACING))

            # Load background
            self.background = arcade.load_texture(SpritePath.BACKGROUND)

            self._create_window_info_sprite()
            self._load_zones_sprites()
            self._load_drones_sprites()

            # Legend
            list_sprites_legends = {
                "START": SpritePath.START_HUB,
                "END": SpritePath.END_HUB,
                "NORMAL ZONE": SpritePath.DEFAULT_ZONE,
                "BLOCKED ZONE": SpritePath.ZONE_BLOCKED,
                "PRIORITY ZONE": SpritePath.ZONE_PRIORITY,
                "RESTRICTED ZONE": SpritePath.ZONE_RESTRICTED
            }

            legend_x = WindowSettings.WIDTH - 166
            legend_y = 168
            legend_step = 30

            for name, path in list_sprites_legends.items():
                icon = Icon(path, 0.4, name)

                icon.center_x = legend_x
                icon.center_y = legend_y
                icon.label_legend.x = legend_x + 15
                icon.label_legend.y = legend_y - 5

                self.legend_sprites_list.append(icon)

                legend_y -= legend_step

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Sprite not found in PATH {e}")

    def _load_zones_sprites(self) -> None:
        """
        Instantiates and positions sprites for every zone in the simulation.

        Maps the logical Zone objects to visual ZoneSprite objects based on
        their type (start, end, normal, blocked, etc.) and calculates their
        exact pixel coordinates.
        """
        for zone in self.zones_dict.values():
            if zone.is_start:
                zone_sprite = ZoneSprite(
                    SpritePath.START_HUB, SpriteSetting.ZONE_SCALE, zone,
                    self.manager
                )
            elif zone.is_end:
                zone_sprite = ZoneSprite(
                    SpritePath.END_HUB, SpriteSetting.ZONE_SCALE, zone,
                    self.manager
                )
            else:
                match zone.metadata_zone_type:
                    case ZoneType.NORMAL:
                        zone_sprite = ZoneSprite(
                            SpritePath.DEFAULT_ZONE,
                            SpriteSetting.ZONE_SCALE, zone, self.manager
                        )
                    case ZoneType.BLOCKED:
                        zone_sprite = ZoneSprite(
                            SpritePath.ZONE_BLOCKED,
                            SpriteSetting.ZONE_SCALE, zone, self.manager
                        )
                    case ZoneType.RESTRICTED:
                        zone_sprite = ZoneSprite(
                            SpritePath.ZONE_RESTRICTED,
                            SpriteSetting.ZONE_SCALE, zone, self.manager
                        )
                    case ZoneType.PRIORITY:
                        zone_sprite = ZoneSprite(
                            SpritePath.ZONE_PRIORITY,
                            SpriteSetting.ZONE_SCALE, zone, self.manager
                        )

            zone_sprite.center_x = ((zone.x * SpriteSetting.SPACING)
                                    + SpriteSetting.OFFSET_X)
            zone_sprite.center_y = ((zone.y * SpriteSetting.SPACING)
                                    + SpriteSetting.OFFSET_Y)

            zone_sprite.label_name_text.x = zone_sprite.center_x
            zone_sprite.label_name_text.y = zone_sprite.center_y - 35
            zone_sprite.label_count_text.x = zone_sprite.center_x + 20
            zone_sprite.label_count_text.y = zone_sprite.center_y + 30

            if self.manager.args.debug:
                zone_sprite.label_weight_text.x = zone_sprite.center_x
                zone_sprite.label_weight_text.y = zone_sprite.center_y + 30

            self.zone_sprites_list.append(zone_sprite)
            zone_sprite.update_drone_count(len(zone.drones_on_it))

            self.zone_coords[zone.name] = (zone_sprite.center_x,
                                           zone_sprite.center_y)

    def _load_drones_sprites(self) -> None:
        """
        Instantiates and positions sprites for every drone in the simulation.

        Maps the logical Drone objects to visual DroneSprite objects, setting
        their initial coordinates with a slight random offset to create a
        swarming effect.
        """
        drone_sprites_anim = [
                arcade.load_texture(SpritePath.DRONE_ANIM1),
                arcade.load_texture(SpritePath.DRONE_ANIM2),
                arcade.load_texture(SpritePath.DRONE_FINISH)
            ]

        for (id, drone) in self.drones_dict.items():
            drone_sprite = DroneSprite(SpritePath.DRONE,
                                       SpriteSetting.DRONE_SCALE,
                                       drone, id, drone_sprites_anim)
            drone_location = drone.get_location()
            if drone_location is not None:
                drone_x = self.zones_dict[drone_location].x
                drone_y = self.zones_dict[drone_location].y

                drone_sprite.center_x = ((drone_x * SpriteSetting.SPACING)
                                         + SpriteSetting.OFFSET_X +
                                         random.randint(-5, 5))
                drone_sprite.center_y = ((drone_y * SpriteSetting.SPACING)
                                         + SpriteSetting.OFFSET_Y +
                                         random.randint(-5, 5))
            self.drone_sprites_list.append(drone_sprite)

    def _create_window_info_sprite(self) -> None:
        """
        Initializes and positions the interactive UI window sprite.
        """
        window_info_sprite = WindowInfo(
                SpritePath.WINDOW_INFO, 1.5, self.manager
            )
        window_info_sprite.center_x = 155
        window_info_sprite.center_y = self.height - 100
        window_info_sprite.update_ui_position()
        self.ui_sprites_list.append(window_info_sprite)

    def _calculate_line_to_draw(self) -> None:
        """
        Pre-calculates drawing data for all zone connections.

        Creates unique identifiers and stores start/end coordinates for every
        edge in the connection map to optimize the rendering loop.
        """
        for zone_a, neighbors in self.connection_map.items():
            for zone_b in neighbors:
                node_a, node_b = sorted([zone_a, zone_b])
                connection_draw = (node_a, node_b)

                if connection_draw not in self.draw_lines:
                    coords_a = self.zone_coords[zone_a]
                    coords_b = self.zone_coords[zone_b]

                    self.line_to_draw.append((coords_a, coords_b))
                    self.draw_lines.add(connection_draw)

    def _create_static_lines(self) -> None:
        """
        Generates static line shapes for the GPU.

        Compiles all connection coordinates into a single ShapeElementList.
        This drastically reduces CPU overhead during the draw cycle.
        """
        for (start_x, start_y), (end_x, end_y) in self.line_to_draw:
            line = arcade.shape_list.create_line(
                start_x, start_y,
                end_x, end_y,
                arcade.color.WHITE,
                1.5
            )
            self.connection_lines.append(line)

    def _update_drone_sprite(self) -> None:
        """
        Synchronizes the visual drone sprites with logical simulation data.

        Calculates new target coordinates (with offsets) and delays for drones
        that have changed location in the backend Manager.
        """
        departure_delays: Dict[str, float] = {}

        for drone_sprite in self.drone_sprites_list:
            drone_obj = self.drones_dict[drone_sprite.id]

            new_location = drone_obj.get_location()
            if (new_location is not None and
                    new_location != drone_sprite.location):

                if new_location not in departure_delays:
                    departure_delays[new_location] = 0.0

                drone_sprite.departure_timer = departure_delays[new_location]
                departure_delays[new_location] += 0.1

                if "-" in new_location:
                    next_zone = new_location.split("-")
                    old_loc_x, old_loc_y = self.zone_coords[next_zone[0]]
                    new_loc_x, new_loc_y = self.zone_coords[next_zone[1]]

                    loc_x = (old_loc_x + new_loc_x) / 2
                    loc_y = (old_loc_y + new_loc_y) / 2

                else:
                    loc_x, loc_y = self.zone_coords[new_location]

                    loc_x += random.randint(-15, 15)
                    loc_y += random.randint(-15, 15)

                drone_sprite.target_x = loc_x
                drone_sprite.target_y = loc_y
                drone_sprite.is_moving = True

    def _update_visual_counts(self) -> None:
        """
        Updates the displayed drone count on every zone sprite.

        Counts the number of stationary visual drones currently occupying each
        zone and updates the zone's UI text label.
        """
        current_counts: Dict[str, int] = {}

        for zone_name in self.zones_dict.keys():
            current_counts[zone_name] = 0

        for drone_sprite in self.drone_sprites_list:
            if not drone_sprite.is_moving:
                if drone_sprite.location in current_counts:
                    current_counts[drone_sprite.location] += 1

        for zone_sprite in self.zone_sprites_list:
            if isinstance(zone_sprite, ZoneSprite):
                zone_sprite.update_drone_count(
                    current_counts.get(zone_sprite.zone_data.name, 0)
                )

    def _update_speed_animation(self, action: str,
                                ui_element: Optional[WindowInfo]
                                = None) -> None:
        """
        Modifies the global drone movement speed and updates the UI.

        Args:
            action (str): The specific speed action triggered
                          (SPEED_PLUS or SPEED_MINUS).
            ui_element (Optional[WindowInfo]): The UI window to update.
                                               Defaults to None.
        """
        if action == WindowAction.SPEED_PLUS:
            if SpriteSetting.DRONE_SPEED < 1000:
                SpriteSetting.DRONE_SPEED += 100

                if ui_element:
                    ui_element.update_info(WindowAction.SPEED_PLUS)
                else:
                    for ui_elem in self.ui_sprites_list:
                        if isinstance(ui_elem, WindowInfo):
                            ui_elem.update_info(WindowAction.SPEED_PLUS)

                if self.manager.args.debug:
                    print(f"Speed up: {SpriteSetting.DRONE_SPEED}")

        elif action == WindowAction.SPEED_MINUS:
            if SpriteSetting.DRONE_SPEED > 100:
                SpriteSetting.DRONE_SPEED -= 100

                if ui_element:
                    ui_element.update_info(WindowAction.SPEED_MINUS)
                else:
                    for ui_elem in self.ui_sprites_list:
                        if isinstance(ui_elem, WindowInfo):
                            ui_elem.update_info(WindowAction.SPEED_MINUS)

                if self.manager.args.debug:
                    print(f"Speed down: {SpriteSetting.DRONE_SPEED}")
