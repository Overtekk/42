/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_map.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/15 21:41:26 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/16 00:07:45 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"\


static	void	check_elements(t_game *game, int y, int x)
{
	if (game->map.grid[y][x] == 'P')
		game->character++;
	if (game->map.grid[y][x] == 'E')
		game->exit++;
	if (game->map.grid[y][x] == 'C')
		game->collectible++;
}

int	check_map(t_game *game)
{
	int	x;
	int	y;

	print_map_debug(game);
	y = 0;
	game->character = 0;
	game->exit = 0;
	game->collectible = 0;
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
	return (0);
}
