/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_invalid_path.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 10:53:14 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/20 12:42:54 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

static	void	flood_fill(char **tab, int y, int x, t_path_check *status)
{
	if (x < 0 || y < 0 || x >= )
		return ;
	// arret si tab[y][x] = 1 ou deja visite
	// transformer les case visitee = V
	// compter les collectibles + exit (status->collectibles_found = status->collectibles_found + 1)
	// recursive en appelant les 4 voisins en bas
	// y-1, x
	// y+1, x
	// y, x-1
	// ym x+1
}

int	is_valid_path(t_game *game)
{
	t_path_check	status;
	char			**tab;
	int				y;

	y = 0;
	status.collectibles_found = 0;
	status.exit_reached = 0;
	tab = malloc(sizeof(char *) * (game->map.y));
	if (tab == NULL)
		return (ft_print_error("Error\nMalloc failed.\n"), free (tab), 1);
	while (game->map.grid[y] != NULL)
	{
		tab[y] = ft_strdup(game->map.grid[y]);
		if (tab[y] == NULL)
			return (free_memory_path(tab, game), 1);
		y++;
	}
	tab[y++] = NULL;
	flood_fill(tab, game->map.player.y, game->map.player.x, &status);
	// regarder si collectibles + exit = ok
	free_memory_path(tab, game);
	return (0);
}
