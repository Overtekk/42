/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_invalid_path.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 10:53:14 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/25 15:37:53 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

static	void	flood_fill(char **tab, int y, int x, t_game *game)
{
	if (x < 0 || y < 0 || x >= game->map.x || y >= game->map.y)
		return ;
	if (tab[y][x] == '1' || tab[y][x] == 'V')
		return ;
	if (tab[y][x] == 'C')
		game->map.c_found++;
	if (tab[y][x] == 'E')
		game->map.exit_reached = 1;
	tab[y][x] = 'V';
	flood_fill(tab, y + 1, x, game);
	flood_fill(tab, y - 1, x, game);
	flood_fill(tab, y, x + 1, game);
	flood_fill(tab, y, x - 1, game);
}

static	void	init_elements(t_game *game)
{
	game->map.c_found = 0;
	game->map.exit_reached = 0;
}

int	is_valid_path(t_game *game)
{
	char	**tab;
	int		y;

	y = 0;
	init_elements(game);
	tab = malloc(sizeof(char *) * (game->map.y + 1));
	if (tab == NULL)
		return (ft_print_error(RED"Error\nMalloc failed.\n"), free (tab), 1);
	while (game->map.grid[y] != NULL)
	{
		tab[y] = ft_strdup(game->map.grid[y]);
		if (tab[y] == NULL)
		{
			ft_print_error(RED"Error\nMalloc failed while checking path.\n");
			return (free_memory_path(tab), 1);
		}
		y++;
	}
	tab[y] = NULL;
	flood_fill(tab, game->map.player.y, game->map.player.x, game);
	free_memory_path(tab);
	if (game->map.c_found == game->collectible && game->map.exit_reached == 1)
		return (0);
	return (path_error(game), 1);
}
