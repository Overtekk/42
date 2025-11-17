/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_map.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/15 21:41:26 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/17 12:50:32 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"\


static	void	init_elements(t_game *game)
{
	game->character = 0;
	game->exit = 0;
	game->collectible = 0;
	game->map_error = 0;
}

static	void	check_elements(t_game *game, int y, int x)
{
	if (game->map.grid[y][x] == 'P')
		game->character++;
	if (game->map.grid[y][x] == 'E')
		game->exit++;
	if (game->map.grid[y][x] == 'C')
		game->collectible++;
}

static	void	check_walls(t_game *game)
{
	int	i;

	i = 0;
	if (game->map.grid[0][i] == 1)
		i++;
	else
		game->map_error = 1;
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
			check_elements(game, y, x);
			x++;
		}
		y++;
	}
	if (game->character != 1 || game->exit != 1 || game->collectible == 0)
		return (map_error(game), 1);
	check_walls(game);
	return (0);
}
