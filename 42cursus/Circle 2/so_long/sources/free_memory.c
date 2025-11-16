/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   free_memory.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:10:34 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/15 23:58:26 by roandrie         ###   ########.fr       */
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

void	free_map_list(char *line, t_list *map_list)
{
	free (line);
	ft_lstclear(&map_list, free);
	ft_print_error(RED"Error\nMalloc failed while reading line.\n");
}
