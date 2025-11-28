/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   key_gestion.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 09:17:56 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/28 14:31:11 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

void	input(t_game *game, int keycode)
{
	if (keycode == KEY_W || keycode == KEY_UP)
		player_movement(game, game->map.player.y - 1, game->map.player.x);
	else if (keycode == KEY_S || keycode == KEY_DOWN)
		player_movement(game, game->map.player.y + 1, game->map.player.x);
	else if (keycode == KEY_A || keycode == KEY_LEFT)
		player_movement(game, game->map.player.y, game->map.player.x - 1);
	else if (keycode == KEY_D || keycode == KEY_RIGHT)
		player_movement(game, game->map.player.y, game->map.player.x + 1);
}

static	int	is_movement_key(int keycode)
{
	if (keycode == KEY_W || keycode == KEY_S
		|| keycode == KEY_A || keycode == KEY_D)
		return (1);
	if (keycode == KEY_UP || keycode == KEY_DOWN
		|| keycode == KEY_LEFT || keycode == KEY_RIGHT)
		return (1);
	return (0);
}

int	key_press(int keycode, t_game *game)
{
	if (keycode == KEY_ESC)
		close_game(game);
	if (is_movement_key(keycode) == 1)
	{
		input(game, keycode);
	}
	return (0);
}
