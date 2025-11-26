/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_game.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 20:19:32 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/26 17:09:14 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

void	set_img(t_game *game)
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
}

void	print_img(t_game *game, void *img, int x, int y)
{
	mlx_put_image_to_window(game->mlx, game->screen, img,
		game->sprite.width * x, game->sprite.height * y);
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
}

static	int	key_press(int keycode, t_game *game)
{
	if (keycode == KEY_ESC)
		stop_game(game);
	return (0);
}

int	init_game(t_game *game)
{
	game->mlx = mlx_init();
	if (game->mlx == NULL)
		return (free (game->mlx), ft_print_error(RED"Error\nMLX connexion failed\n"), 1);
	game->screen = mlx_new_window(game->mlx, 64 * (game->map.x), 64 * (game->map.y), "Hungry Koala");
	if (game->screen == NULL)
	{
		free (game->mlx);
		return (ft_print_error(RED"Error\nFailed to create window\n"), 1);
	}
	set_img(game);
	draw_map(game);
	print_img(game, game->sprite.player, game->map.player.x, game->map.player.y);
	mlx_hook(game->screen, KeyPress, KeyPressMask, &key_press, game);
	mlx_loop(game->mlx);
	return (0);
}

// int mlx_hook(void *win_ptr, int x_event, int x_mask, int (*funct_ptr)(), void *param);
// if (game->sprite.player == NULL)
//		return (stop_game(game), 1);
