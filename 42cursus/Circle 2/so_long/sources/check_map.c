/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_map.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/15 21:41:26 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/18 15:57:18 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"\


static	void	init_elements(t_game *game)
{
	game->character = 0;
	game->exit = 0;
	game->collectible = 0;
	game->map.error_north = 0;
	game->map.error_south = 0;
	game->map.error_west = 0;
	game->map.error_east = 0;
}

static	void	check_elements(t_game *game, int y, int x)
{
	if (game->map.grid[y][x] == 'P')
	{
		game->character++;
		game->map.player.x = x;
		game->map.player.y = y;
	}
	if (game->map.grid[y][x] == 'E')
		game->exit++;
	if (game->map.grid[y][x] == 'C')
		game->collectible++;
}

static	void	check_walls(t_game *game, int y, int x)
{
	if (y == 0 && game->map.grid[y][x] != '1')
		game->map.error_north = 1;
	if (x == 0 && game->map.grid[y][x] != '1')
		game->map.error_west = 1;
	if (x == (game->map.x - 1) && game->map.grid[y][x] != '1')
		game->map.error_east = 1;
	else if (y == (game->map.y - 1) && game->map.grid[y][x] != '1')
		game->map.error_south = 1;
}

static	int	check_errors(t_game *game)
{
	if (game->character != 1 || game->exit != 1 || game->collectible == 0)
		return (map_error(game), 1);
	if (game->map.error_north == 1 || game->map.error_south == 1)
		return (map_error(game), 1);
	if (game->map.error_west == 1 || game->map.error_east == 1)
		return (map_error(game), 1);
	return (0);
}

int	check_map(t_game *game)
{
	int	x;
	int	y;

	init_elements(game);
	print_map_debug(game);
	y = 0;
	while (y < game->map.y)
	{
		x = 0;
		while (x < game->map.x)
		{
			check_walls(game, y, x);
			check_elements(game, y, x);
			x++;
		}
		y++;
	}
	if (check_errors(game) == 1 && is_valid_path(game) == 1)
		return (1);
	return (0);
}
