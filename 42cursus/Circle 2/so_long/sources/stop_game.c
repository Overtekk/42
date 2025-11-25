/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stop_game.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 21:03:14 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/25 21:21:07 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

int	stop_game(t_game *game)
{
	//mlx_destroy_image(game->mlx, game->sprite.player);
	mlx_destroy_window(game->mlx, game->screen);
	mlx_destroy_display(game->mlx);
	free(game->mlx);
	return (0);
}
