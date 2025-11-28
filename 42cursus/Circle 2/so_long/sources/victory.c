/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   victory.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 15:22:48 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/28 15:45:59 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

void	winning(t_game *game)
{
	int	x;
	int	y;

	game->game_won = 1;
	mlx_clear_window(game->mlx, game->screen);
	x = (game->map.x * 64) / 2 - (300 / 2);
    y = (game->map.y * 64) / 2 - (300 / 2);
	mlx_put_image_to_window(game->mlx, game->screen,
		game->sprite.victory, x, y);
	mlx_string_put(game->mlx, game->screen, x + 100, y,
        0xFFFFFF, "Press ESC to quit");
	mlx_string_put(game->mlx, game->screen, x + 90, y + 320,
        0xFFFFFF, "I love graphic design <3");
}
