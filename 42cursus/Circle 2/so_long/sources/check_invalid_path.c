/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_invalid_path.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 10:53:14 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/18 16:37:13 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

/*
typedef struct s_path_check
{
    int    collectibles_found;
    int    exit_reached;
}   t_path_check;
*/

static	void	flood_fill(char **tab, t_game *game, int y, int x, t_path_check *status)
{
	/*
	typedef struct s_path_check
	{
    int    collectibles_found;
    int    exit_reached; // 0 (false) ou 1 (true)
	}   t_path_check;
	*/
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
	char	**tab;
	// t_path_check    status;
	// status.collectibles_found = 0;
	// status.exit_reached = 0;

	tab = malloc(sizeof(char *) * (game->map.y));
	// boucle pour copier (while puis strdup)
	tab[y++] = NULL;
	flood_fill(tab, game->map.player.y, game->map.player.x, &status);
	// regarder si collectibles + exit = ok
	// free la copie du tableau
	return (0);
}
