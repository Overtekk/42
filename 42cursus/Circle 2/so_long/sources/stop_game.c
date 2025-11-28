/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stop_game.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 21:03:14 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/28 14:36:22 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

int	check_img_error(t_game *game)
{
	if (game->sprite.player == NULL || game->sprite.exit_close == NULL
		|| game->sprite.exit_open == NULL || game->sprite.collectible == NULL
		|| game->sprite.wall == NULL || game->sprite.floor == NULL)
		return (1);
	return (0);
}

int	close_game(t_game *game)
{
	ft_printf(RED"Game closed\n"R);
	mlx_loop_end(game->mlx);
	return (0);
}

int	stop_game(t_game *game)
{
	if (game->sprite.player != NULL)
		mlx_destroy_image(game->mlx, game->sprite.player);
	if (game->sprite.exit_close != NULL)
		mlx_destroy_image(game->mlx, game->sprite.exit_close);
	if (game->sprite.exit_open != NULL)
		mlx_destroy_image(game->mlx, game->sprite.exit_open);
	if (game->sprite.collectible != NULL)
		mlx_destroy_image(game->mlx, game->sprite.collectible);
	if (game->sprite.wall != NULL)
		mlx_destroy_image(game->mlx, game->sprite.wall);
	if (game->sprite.floor != NULL)
		mlx_destroy_image(game->mlx, game->sprite.floor);
	mlx_destroy_window(game->mlx, game->screen);
	mlx_destroy_display(game->mlx);
	free(game->mlx);
	return (0);
}
