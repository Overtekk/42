/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_elements.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:46:00 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/28 14:14:20 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

void	init_elements(t_game *game)
{
	game->character = 0;
	game->exit = 0;
	game->collectible = 0;
	game->invalid_c = 0;
	game->map.error_north = 0;
	game->map.error_south = 0;
	game->map.error_west = 0;
	game->map.error_east = 0;
	game->map.c_found = 0;
	game->map.exit_reached = 0;
	game->step = 0;
}
