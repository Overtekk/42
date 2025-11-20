/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_invalid_path.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 10:53:14 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/20 13:04:57 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

static	void	flood_fill(char **tab, int y, int x, t_path_check *status)
{
	if (x < 0 || y < 0 || x >= || y >= )
		return ;
	if (tab[y][x] == '1' || tab[y][x] == 'V')
		return ;
	tab[y][x] = 'V';
	if (tab[y][x] == 'C')
		status->c_found++;
	if (tab[y][x] == 'E')
		status->exit_reached = 1;
	flood_fill(tab, y + 1, x, status);
	flood_fill(tab, y - 1, x, status);
	flood_fill(tab, y, x + 1, status);
	flood_fill(tab, y, x - 1, status);
}

int	is_valid_path(t_game *game)
{
	t_path_check	status;
	char			**tab;
	int				y;

	y = 0;
	status.c_found = 0;
	status.exit_reached = 0;
	tab = malloc(sizeof(char *) * (game->map.y));
	if (tab == NULL)
		return (ft_print_error("Error\nMalloc failed.\n"), free (tab), 1);
	while (game->map.grid[y] != NULL)
	{
		tab[y] = ft_strdup(game->map.grid[y]);
		if (tab[y] == NULL)
			return (free_memory_path(tab), 1);
		y++;
	}
	tab[y++] = NULL;
	flood_fill(tab, game->map.player.y, game->map.player.x, &status);
	free_memory_path(tab);
	if (status.c_found != game->collectible && status.exit_reached == 0)
		return (ft_print_error("Error\nMap path is blocked"), 1);
	return (0);
}
