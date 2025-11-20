/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_invalid_path.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 10:53:14 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/20 14:10:48 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

static	void	flood_fill(char **tab, int y, int x, t_game *game)
{
	if (x < 0 || y < 0 || x >= game->map.x || y >= game->map.y)
		return ;
	if (tab[y][x] == '1' || tab[y][x] == 'V')
		return ;
	tab[y][x] = 'V';
	if (tab[y][x] == 'C')
		game->map.c_found++;
	if (tab[y][x] == 'E')
		game->map.exit_reached = 1;
	flood_fill(tab, y + 1, x, game);
	flood_fill(tab, y - 1, x, game);
	flood_fill(tab, y, x + 1, game);
	flood_fill(tab, y, x - 1, game);
}

int	is_valid_path(t_game *game)
{
	char	**tab;
	int		y;

	y = 0;
	game->map.c_found = 0;
	game->map.exit_reached = 0;
	tab = malloc(sizeof(char *) * (game->map.y));
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
	tab[y++] = NULL;
	flood_fill(tab, game->map.player.y, game->map.player.x, game);
	print_map_copy_debug(tab);
	free_memory_path(tab);
	ft_printf("\nCollectible = %d | Exit = %d\n", game->map.c_found, game->map.exit_reached);
	if (game->map.c_found == game->collectible && game->map.exit_reached == 1)
		return (0);
	return (ft_print_error(RED"Error\nMap path is blocked\n"), 1);
}
