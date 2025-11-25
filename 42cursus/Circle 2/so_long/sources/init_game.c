/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_game.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 20:19:32 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/25 21:39:12 by roandrie         ###   ########.fr       */
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
	game->sprite.exit = mlx_xpm_file_to_image(game->mlx,
			"textures/exit_close.xpm",
			&(game->sprite.width), &(game->sprite.height));
}

void	print_img(t_game *game, void *img, int x, int y)
{
	mlx_put_image_to_window(game->mlx, game->screen, img,
		game->sprite.width * x, game->sprite.height * y);
}

int	init_game(t_game *game)
{
	game->mlx = mlx_init();
	if (game->mlx == NULL)
		return (ft_print_error(RED"Error\nMLX connexion failed\n"), 1);
	game->screen = mlx_new_window(game->mlx, 1920, 1080, "Hungry Koala");
	if (game->screen == NULL)
	{
		free (game->mlx);
		return (ft_print_error(RED"Error\nFailed to create window\n"), 1);
	}
	set_img(game);
	print_img(game, game->sprite.player, game->map.player.x, game->map.player.y);
	print_img(game, game->sprite.exit, game->map.player.x, game->map.player.y);
	mlx_loop(game->mlx);
	return (0);
}

// int mlx_hook(void *win_ptr, int x_event, int x_mask, int (*funct_ptr)(), void *param);
// if (game->sprite.player == NULL)
//		return (stop_game(game), 1);

/*
static	void	draw_map(t_game *game)
{
	game->sprite.player = mlx_xpm_file_to_image(game->mlx,
			"textures/characters.xpm",
			&game->sprite.width, &game->sprite.height);
	mlx_put_image_to_window(game->mlx, game->screen, game->sprite.player,
		game->map.player.x, game->map.player.y);
}
*/
