/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   free_memory.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:10:34 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/15 21:09:39 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

void	free_memory(t_game *game)
{
	int	y;

	y = 0;
	while (game->map.grid[y] != NULL)
	{
		free(game->map.grid[y]);
		y++;
	}
	free (game->map.grid);
	free (game);
}
