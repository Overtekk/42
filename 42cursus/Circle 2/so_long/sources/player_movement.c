/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   player_movement.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 16:09:18 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 12:14:40 by roandrie         ###   ########.fr       */
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
	int	total;

	game->map.grid[y][x] = '0';
	game->collectible--;
	total = game->map.c_found - game->collectible;
	ft_printf(BLUE"Collectible %d/%d\n", total, game->map.c_found, R);
}

static	void	print_movement(t_game *game)
{
	char	*move_count;
	char	*col_collected;
	char	*total;
	int		count;

	game->step++;
	count = game->map.c_found - game->collectible;
	move_count = ft_itoa(game->step);
	col_collected = ft_itoa(count);
	total = ft_itoa(game->map.c_found);
	ft_printf(BLUE"Step = %d\n", game->step, R);
	print_img(game, game->sprite.wall, 0, 0);
	print_img(game, game->sprite.wall, 1, 0);
	mlx_string_put(game->mlx, game->screen, 20, 20, 0xFFFFFF, "Steps: ");
	mlx_string_put(game->mlx, game->screen, 70, 20, 0xFFFFFF, move_count);
	mlx_string_put(game->mlx, game->screen, 20, 40, 0xFFFFFF, "Collectible: ");
	mlx_string_put(game->mlx, game->screen, 95, 40, 0xFFFFFF, col_collected);
	mlx_string_put(game->mlx, game->screen, 100, 40, 0xFFFFFF, "/");
	mlx_string_put(game->mlx, game->screen, 105, 40, 0xFFFFFF, total);
	free (move_count);
	free (col_collected);
	free (total);
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
