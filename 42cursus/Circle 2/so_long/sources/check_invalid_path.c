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

static	void	flood_fill(char **tab, t_game *game)
{
	if (game->map.y > 0 || game->map.x > 0)
		return ;
	tab[y][x] = '1';
}

int	is_valid_path(t_game *game)
{
	char	**tab;
	int		y;
	int		size;

	size = game->map.y;
	tab = malloc(sizeof(char *) * (size + 1));
	tab = game->map.grid;
	tab[y++] = NULL;
	flood_fill(tab, game);
	return (0);
}
