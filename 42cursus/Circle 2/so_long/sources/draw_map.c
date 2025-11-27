/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   draw_map.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 09:10:01 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/27 11:25:51 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

void	print_img(t_game *game, void *img, int x, int y)
{
	mlx_put_image_to_window(game->mlx, game->screen, img,
		game->sprite.width * x, game->sprite.height * y);
}

int	set_img(t_game *game)
{
	game->sprite.height = 64;
	game->sprite.width = 64;
	game->sprite.player = mlx_xpm_file_to_image(game->mlx,
			"textures/characters.xpm",
			&(game->sprite.width), &(game->sprite.height));
	game->sprite.exit_close = mlx_xpm_file_to_image(game->mlx,
			"textures/exit_close.xpm",
			&(game->sprite.width), &(game->sprite.height));
	game->sprite.collectible = mlx_xpm_file_to_image(game->mlx,
			"textures/collectible.xpm",
			&(game->sprite.width), &(game->sprite.height));
	game->sprite.floor = mlx_xpm_file_to_image(game->mlx,
			"textures/floor.xpm",
			&(game->sprite.width), &(game->sprite.height));
	game->sprite.wall = mlx_xpm_file_to_image(game->mlx,
			"textures/walls.xpm",
			&(game->sprite.width), &(game->sprite.height));
	if (check_img_error(game) == 1)
		return (stop_game(game), 1);
	return (0);
}

void	draw_map(t_game *game)
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
			if (game->map.grid[y][x] == 'C')
				print_img(game, game->sprite.collectible, x, y);
			if (game->map.grid[y][x] == 'E')
				print_img(game, game->sprite.exit_close, x, y);
			x++;
		}
		y++;
	}
	print_img(game, game->sprite.player, game->map.player.x,
		game->map.player.y);
}
