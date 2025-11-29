/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   victory.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 15:22:48 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 12:24:45 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

static	void	draw_winning(t_game *game)
{
	int	x;
	int	y;

	y = 0;
	while (y < game->map.y)
	{
		x = 0;
		while (x < game->map.x)
		{
			print_img(game, game->sprite.floor, x, y);
			if (game->map.grid[y][x] == '1')
				print_img(game, game->sprite.wall, x, y);
			x++;
		}
		y++;
	}
}

void	winning(t_game *game)
{
	int	x;
	int	y;

	game->game_won = 1;
	mlx_clear_window(game->mlx, game->screen);
	x = (game->map.x * 64) / 2 - (300 / 2);
	y = (game->map.y * 64) / 2 - (300 / 2);
	draw_winning(game);
	mlx_put_image_to_window(game->mlx, game->screen,
		game->sprite.victory, x, y);
	mlx_string_put(game->mlx, game->screen, x + 100, y,
		0xFFFFFF, "Press ESC to quit");
	mlx_string_put(game->mlx, game->screen, x + 90, y + 320,
		0xFFFFFF, "I love graphic design <3");
	mlx_string_put(game->mlx, game->screen, x + 60, y + 280,
		0xFFFFFF, "Your kid as is belly full... for now");
}
