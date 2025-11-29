/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   player_movement.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 16:09:18 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 09:32:21 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

static	int	check_win_condition(t_game *game)
{
	int	x;
	int	y;

	x = game->map.exit.x;
	y = game->map.exit.y;
	if (game->collectible == 0)
	{
		print_img(game, game->sprite.exit_open, x, y);
		return (1);
	}
	return (0);
}

static	void	collect(t_game *game, int y, int x)
{
	game->map.grid[y][x] = '0';
	game->collectible--;
	ft_printf(BLUE"Collectible %d/%d\n", game->collectible,
		game->map.c_found, R);
}

static	void	print_movement(t_game *game)
{
	char	*move_count;

	game->step++;
	move_count = ft_itoa(game->step);
	ft_printf(BLUE"Step = %d\n", game->step, R);
	mlx_string_put(game->mlx, game->screen, 20, 20, 0x0066ff, "Steps: ");
	mlx_string_put(game->mlx, game->screen, 70, 20, 0x0066ff, move_count);
	free(move_count);
}

void	player_movement(t_game *game, int y, int x)
{
	int	old_x;
	int	old_y;

	old_x = game->map.player.x;
	old_y = game->map.player.y;
	if (game->map.grid[y][x] == '0' || game->map.grid[y][x] == 'C'
		|| game->map.grid[y][x] == 'P')
	{
		game->map.player.x = x;
		game->map.player.y = y;
		if (game->map.grid[y][x] == 'C')
			collect(game, y, x);
		print_img(game, game->sprite.player, game->map.player.x,
			game->map.player.y);
		print_img(game, game->sprite.floor, old_x, old_y);
		print_movement(game);
	}
	if (check_win_condition(game) == 1)
	{
		if (game->map.grid[y][x] == 'E')
			winning(game);
	}
}
