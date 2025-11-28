/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_game.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 20:19:32 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/28 14:26:33 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

int	init_game(t_game *game)
{
	game->mlx = mlx_init();
	if (game->mlx == NULL)
		return (free (game->mlx),
			ft_print_error(RED"Error\nMLX connexion failed\n"), 1);
	game->screen = mlx_new_window(game->mlx, 64 * (game->map.x),
			64 * (game->map.y), "Hungry Koala");
	if (game->screen == NULL)
		return (free (game->mlx),
			ft_print_error(RED"Error\nFailed to create window\n"), 1);
	if (set_img(game) == 1)
		return (ft_print_error(RED"Error\nSprite hasn't loaded\n"), 1);
	draw_map(game);
	mlx_hook(game->screen, KeyPress, KeyPressMask, &key_press, game);
	mlx_hook(game->screen, 17, 0, close_game, game);
	mlx_loop(game->mlx);
	stop_game(game);
	return (0);
}
